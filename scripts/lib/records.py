"""Shared helpers for person and system records: front-matter parsing, schema checks, claim walking."""
import csv, json, os, re

import yaml
from jsonschema import Draft202012Validator

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SENTINELS = {"TODO", "UNKNOWN", "BELOW_THRESHOLD"}
BASIS_CERTAINTY = {"written_profession": 1.0, "consistent_private_letters": 0.7, "scholarly_reconstruction": 0.5}
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
            want = BASIS_CERTAINTY[basis] if basis in BASIS_CERTAINTY else None
            cert = c.get("certainty")
            if want is not None and (cert not in (1.0, 0.7, 0.5) or cert > want):
                errors.append(f"{'/'.join(p)}: basis {basis} allows certainty at most {want} (1.0 / 0.7 / 0.5), got {cert}")
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
