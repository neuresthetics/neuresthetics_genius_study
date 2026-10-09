"""Shared helpers for person and system records: front-matter parsing, schema checks, claim walking."""
import collections, csv, json, os, re

import yaml
from jsonschema import Draft202012Validator

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SENTINELS = {"TODO", "UNKNOWN", "BELOW_THRESHOLD"}
BASIS_CERTAINTY = {"written_profession": 1.0, "consistent_private_letters": 0.7, "recorded_interview": 0.7, "scholarly_reconstruction": 0.5,
                   "inference_from_work": 0.5}  # inference_from_work: decision P24, schema 1.3
CITE_IN_BODY = re.compile(r"\[(S\d+(?:[^\]]*)?)\]")
SOURCE_ID = re.compile(r"\bS\d+\b")


class _Loader(yaml.SafeLoader):
    """SafeLoader that keeps dates as plain strings (so 2026-10-01 stays '2026-10-01')."""


_Loader.yaml_implicit_resolvers = {
    k: [(tag, rx) for tag, rx in v if tag != "tag:yaml.org,2002:timestamp"]
    for k, v in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def read_record(path):
    """Return (front_matter_dict, body_text). Raises ValueError if the file has no front matter."""
    text = open(path, encoding="utf-8").read()
    if not text.startswith("---\n"):
        raise ValueError("file must start with a '---' YAML front-matter block")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("front matter is not closed with a '---' line")
    data = yaml.load(text[4:end], Loader=_Loader)
    if not isinstance(data, dict):
        raise ValueError("front matter is not a mapping")
    return data, text[end + 5:]


def load_schema(name):
    with open(os.path.join(REPO, "schema", name), encoding="utf-8") as fh:
        schema = json.load(fh)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema)


def schema_errors(validator, data):
    out = []
    for e in sorted(validator.iter_errors(data), key=lambda e: list(map(str, e.absolute_path))):
        where = "/".join(map(str, e.absolute_path)) or "(top)"
        msg = e.message
        if e.validator in ("anyOf", "oneOf", "if", "allOf") and e.context:
            msg += " | " + "; ".join(sorted({c.message for c in e.context})[:3])
        out.append(f"{where}: {msg}")
    return out


def walk(node, path=()):
    """Yield (path, dict) for every mapping in the tree."""
    if isinstance(node, dict):
        yield path, node
        for k, v in node.items():
            yield from walk(v, path + (str(k),))
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from walk(v, path + (str(i),))


def claims(data):
    """Yield (path, claim) for every claim object (a mapping with a 'value' key)."""
    for p, d in walk(data):
        if "value" in d and p and p[-1] != "alternatives" and (len(p) < 2 or p[-2] != "alternatives"):
            yield p, d


INTERVIEW_FLAG = "(interview)"


def is_interview(c):
    """True for a claim that rests on interview evidence (decision P8, as signed off by Jason on
    2026-10-02): basis recorded_interview, or a how_known that starts with the '(interview)' flag."""
    if not isinstance(c, dict):
        return False
    return c.get("basis") == "recorded_interview" or str(c.get("how_known") or "").startswith(INTERVIEW_FLAG)


def claim_state(c):
    v = c.get("value")
    return v if isinstance(v, str) and v in SENTINELS else "FILLED"


def cited_sources(data):
    ids = set()
    for _, d in walk(data):
        if "source" in d and isinstance(d["source"], str) and SOURCE_ID.fullmatch(d["source"]):
            ids.add(d["source"])
    return ids


def body_sources(body):
    """Source ids cited in the Markdown body as [S1, p. 3] or [S1; S2]. Inline `code` and fenced blocks are skipped."""
    body = re.sub(r"```.*?```", "", body, flags=re.S)
    body = re.sub(r"`[^`\n]*`", "", body)
    ids = set()
    for m in CITE_IN_BODY.finditer(body):
        ids.update(SOURCE_ID.findall(m.group(1)))
    return ids


def common_checks(data, body, required_sections):
    """Checks shared by people and systems. Returns (errors, warnings)."""
    errors, warnings = [], []
    sources = data.get("sources") or []
    ids = [s.get("id") for s in sources if isinstance(s, dict)]
    dup = {i for i in ids if ids.count(i) > 1}
    if dup:
        errors.append(f"sources: duplicate ids {sorted(dup)}")
    known = set(ids)
    for sid in sorted(cited_sources(data) - known):
        errors.append(f"front matter cites {sid}, which is not in sources")
    for sid in sorted(body_sources(body) - known):
        errors.append(f"body cites [{sid}], which is not in sources")
    used = cited_sources(data) | body_sources(body)
    for sid in sorted(known - used):
        warnings.append(f"source {sid} is listed but never cited")
    for p, c in claims(data):
        basis = c.get("basis")
        if basis and claim_state(c) == "FILLED":
            # The basis sets a ceiling (CODING_GUIDE §3): certainty may sit below it (contested readings,
            # indirect evidence) but never above it, and must be one of the three levels.
            # recorded_interview (decision P8, schema 1.2) has the same 0.7 ceiling as consistent letters.
            want = BASIS_CERTAINTY[basis] if basis in BASIS_CERTAINTY else None
            cert = c.get("certainty")
            if want is not None and (cert not in (1.0, 0.7, 0.5) or cert > want):
                errors.append(f"{'/'.join(p)}: basis {basis} allows certainty at most {want} (1.0 / 0.7 / 0.5), got {cert}")
        if basis == "recorded_interview" and not str(c.get("how_known") or "").startswith(INTERVIEW_FLAG):
            # P8 (Jason, 2026-10-02): interview-based fields carry a visible flag.
            errors.append(f"{'/'.join(p)}: basis recorded_interview needs how_known to start with '{INTERVIEW_FLAG}' (P8)")
        if claim_state(c) == "FILLED" and c.get("certainty") is not None and not c.get("cites"):
            errors.append(f"{'/'.join(p)}: filled claim without citations")
    headings = re.findall(r"^## (.+?)\s*$", body, flags=re.M)
    for h in required_sections:
        if h not in headings:
            errors.append(f"body is missing the section '## {h}'")
    rec = data.get("record") or {}
    if rec.get("review_status") == "reviewed" and not (rec.get("reviewed_by") and rec.get("reviewed_on")):
        errors.append("record: review_status 'reviewed' needs reviewed_by and reviewed_on")
    return errors, warnings


def fill_counts(data, top_keys=None):
    """Count claim states per top-level section."""
    out = {}
    for p, c in claims(data):
        sec = p[0]
        if top_keys and sec not in top_keys:
            continue
        out.setdefault(sec, {"FILLED": 0, "TODO": 0, "UNKNOWN": 0, "BELOW_THRESHOLD": 0})
        out[sec][claim_state(c)] += 1
    return out


def read_csv(path):
    with open(path, encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def system_codes():
    d = os.path.join(REPO, "systems")
    return {f[:-3] for f in os.listdir(d) if f.endswith(".md") and f != "README.md"} if os.path.isdir(d) else set()


def person_files():
    root = os.path.join(REPO, "people")
    out = []
    for dirpath, _, files in os.walk(root):
        for f in files:
            if f.endswith(".md") and f != "README.md":
                out.append(os.path.join(dirpath, f))
    return sorted(out)


def system_files():
    d = os.path.join(REPO, "systems")
    return sorted(os.path.join(d, f) for f in os.listdir(d) if f.endswith(".md") and f != "README.md")


def people_axis_points():
    """Split the person records for the person chart and its README caption.

    Returns (points, not_scorable). points are the records with both A_locus and B_cause scored (integers);
    they are the plotted base. not_scorable are the other records, each a dict with name and reason; they are
    left out of every denominator and reported separately (DECIDED (Jason, 2026-10-08), OPEN_DECISIONS P34).
    Each point is a dict with name, A, B, their certainties and interview flags, and mid_basin.
    Shared by scripts/make_figures.py and scripts/progress_status.py."""
    pts, out = [], []
    for f in person_files():
        d, _ = read_record(f)
        lio = d["worldview"]["lio_axes"]
        a, b = lio["A_locus"], lio["B_cause"]
        okA, okB = isinstance(a.get("value"), int), isinstance(b.get("value"), int)
        if not (okA and okB):
            reason = "both axes" if not (okA or okB) else ("A_locus" if not okA else "B_cause")
            out.append({"name": d["identity"]["display_name"], "reason": reason,
                        "A": a.get("value"), "B": b.get("value")})
            continue
        mb = d["worldview"].get("mid_basin") or {}
        pts.append({"name": d["identity"]["display_name"], "A": a["value"], "B": b["value"],
                    "cA": a.get("certainty"), "cB": b.get("certainty"),
                    "iA": is_interview(a), "iB": is_interview(b),
                    "mid_basin": mb.get("value") if isinstance(mb, dict) else mb})
    return pts, out


def not_scorable_summary(out):
    """Plain-words breakdown of the people left out of the chart base, e.g.
    '17 with no A_locus score, 3 with no B_cause score, 3 with neither'."""
    c = collections.Counter(p["reason"] for p in out)
    parts = []
    if c["A_locus"]:
        parts.append(f"{c['A_locus']} with no A_locus score")
    if c["B_cause"]:
        parts.append(f"{c['B_cause']} with no B_cause score")
    if c["both axes"]:
        parts.append(f"{c['both axes']} with neither")
    return ", ".join(parts)


# The region drawn on the person chart: the study focus, the LIO pole on both axes.
CHART_CERT = 0.7  # both axes at certainty >= 0.7


def in_focus(p):
    """Study focus: the LIO pole on both axes (A_locus >= 3 and B_cause >= 3)."""
    return p["A"] >= 3 and p["B"] >= 3


def firm(p):
    """Both axes at certainty >= 0.7."""
    return all(isinstance(c, (int, float)) and c >= CHART_CERT for c in (p["cA"], p["cB"]))


def focus_counts(pts):
    """(in_box, base, faded_in_box). The base is the plotted people at certainty >= 0.7 on both axes; in_box
    is those of them in the study-focus region. faded_in_box are plotted in the region below 0.7 on at least
    one axis; they are outside the base and not counted."""
    base = [p for p in pts if firm(p)]
    return (sum(1 for p in base if in_focus(p)), len(base),
            sum(1 for p in pts if in_focus(p) and not firm(p)))


def people_chart_caption():
    """README caption for figures/people_cause_locus.png, computed from the records. Every count uses only the
    people scorable for it; the rest are reported as not scorable yet (OPEN_DECISIONS P34)."""
    pts, out = people_axis_points()
    bs = sorted({p["B"] for p in pts})
    if not bs:
        brange = "no person has both axes scored"
    elif len(bs) == 1:
        brange = f"every plotted person is B_cause {bs[0]}"
    else:
        brange = ("every plotted person is B_cause " + ", ".join(map(str, bs[:-1])) + f" or {bs[-1]}")
    fi, fb, ff = focus_counts(pts)
    # Left two columns are B_cause 0 and 1. Mention them only when the plotted records leave them empty.
    left = ""
    if pts and all(p["B"] >= 2 for p in pts):
        left = (" Nobody plotted scores in the left two columns "
                "(miracles or intervention, or mostly intervention).")
    faded = (f" {ff} more {'is' if ff == 1 else 'are'} plotted in the box at lower certainty and "
             f"{'is' if ff == 1 else 'are'} not counted.") if ff else ""
    ns = (f" **Not scorable yet:** {len(out)} coded {'person lacks' if len(out) == 1 else 'people lack'} a score on "
          f"at least one axis ({not_scorable_summary(out)}; the value is UNKNOWN or BELOW_THRESHOLD). They are not "
          f"plotted and are left out of every count here, not counted as outside the box.") if out else ""
    return (f"*Draft person scores: where God is (up the chart) against how things happen (across the chart). "
            f"The shaded top-right box is the only region marked: the study focus, God as the order of nature "
            f"and nature as lawful (A_locus ≥ 3 and B_cause ≥ 3). Plotted: the {len(pts)} coded people with both "
            f"axes scored; {brange}.{left} Focus count: {fi} of the {fb} people scored at certainty ≥ 0.7 on both "
            f"axes are in the box (the base is those {fb}).{faded}{ns} These are unreviewed, hand-picked drafts, "
            f"not a sample, and there is no base rate, so no over- or under-representation claim can be made "
            f"from them. Each surname sits next to its dot. A faded dot is a less certain score "
            f"(below 0.7 on at least one axis).*")
