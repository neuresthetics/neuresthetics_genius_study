#!/usr/bin/env python3
"""
Assign stable person ids (slugs like `newton-isaac`) to every roster row.

Reads   data/roster/roster.csv, data/roster/id_overrides.csv, data/roster/person_ids.csv (if it exists)
Writes  data/roster/person_ids.csv

Rules (see docs/METHOD.md, "Person ids"):
  * An id, once in person_ids.csv, is never renamed or reused. The script only appends.
  * New ids come from id_overrides.csv if the name is listed there, otherwise from the slug rule:
      - strip accents and parenthetical alternates ("Ibn Sina (Avicenna)" -> "Ibn Sina")
      - lowercase, every run of non-letters/digits -> "-"
      - mononyms stay as they are (aristotle); "X of Y", "X the Great", Ibn/Al-/Abu names and
        Italian "da"/"di" names keep their written order (augustine-of-hippo, ibn-sina, leonardo-da-vinci)
      - otherwise family name first: the last word, or the last word plus any particles before it
        (van, von, de, du, der, den, la, le, ten, ter, y) -> newton-isaac, van-gogh-vincent
      - Jr./Sr./II/III move to the end (king-martin-luther-jr)
      - a clash gets -2, -3 ... and is reported so a human can pick a better override
  * A roster name that is no longer in the roster keeps its row with status `retired` (never deleted).
    If its row in roster.csv was renamed, add the old -> new pair to id_overrides.csv with the old id.
  * Shard = first character of the id; the person file lives at people/<shard>/<id>.md.

Run:  python3 scripts/assign_ids.py            (update person_ids.csv)
      python3 scripts/assign_ids.py --check    (exit 1 if person_ids.csv would change)
"""
import csv, os, re, sys, unicodedata, argparse, io

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROSTER = os.path.join(REPO, "data", "roster", "roster.csv")
OVERRIDES = os.path.join(REPO, "data", "roster", "id_overrides.csv")
IDS = os.path.join(REPO, "data", "roster", "person_ids.csv")
COLS = ["id", "canonical_name", "shard", "path", "status", "assigned_in", "rule", "note"]
FIRST_ROSTER = "v8"

SPECIAL = {'ø': 'o', 'Ø': 'O', 'ł': 'l', 'Ł': 'L', 'ß': 'ss', 'æ': 'ae', 'Æ': 'AE',
           'đ': 'd', 'Đ': 'D', 'ı': 'i', 'œ': 'oe', 'Œ': 'OE', 'ð': 'd', 'þ': 'th'}
PARTICLES = {"van", "von", "de", "du", "der", "den", "la", "le", "ten", "ter", "y", "del", "della", "dos", "das"}
SUFFIXES = {"jr", "sr", "ii", "iii", "iv"}
KEEP_ORDER_PREFIX = ("ibn ", "al-", "al ", "abu ", "bin ")
KEEP_ORDER_WORDS = {"of", "the", "da", "di"}


def deaccent(s):
    s = ''.join(SPECIAL.get(c, c) for c in s)
    return ''.join(c for c in unicodedata.normalize('NFKD', s) if not unicodedata.combining(c))


def slugify(s):
    s = deaccent(s).lower().replace("'", "").replace("’", "")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def slug_rule(name):
    """Return (slug, rule) for a roster canonical name."""
    base = re.sub(r"\s*\(.*?\)\s*", " ", name).strip()
    words = base.replace(",", " ").split()
    suffix = []
    while words and words[-1].lower().strip(".") in SUFFIXES:
        suffix.insert(0, words.pop().strip("."))
    low = " ".join(words).lower()
    if len(words) <= 1:
        rule = "mononym"
        ordered = words
    elif low.startswith(KEEP_ORDER_PREFIX) or any(w.lower() in KEEP_ORDER_WORDS for w in words[1:]):
        rule = "written order (of/the/da/di or Arabic ibn/al-/abu)"
        ordered = words
    else:
        i = len(words) - 1
        while i - 1 >= 1 and words[i - 1].lower() in PARTICLES:
            i -= 1
        if words[i].lower() == "y" and i - 1 >= 1:   # Spanish "Ramón y Cajal": both family names
            i -= 1
        family, given = words[i:], words[:i]
        ordered = family + given
        rule = "family name first"
    if suffix:
        rule += " + suffix last"
    return slugify(" ".join(ordered + suffix)), rule


def read_csv(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def build():
    roster = [r["canonical_name"] for r in read_csv(ROSTER)]
    overrides = {r["canonical_name"]: r for r in read_csv(OVERRIDES)}
    existing = read_csv(IDS)
    by_name = {r["canonical_name"]: r for r in existing}
    used = {r["id"] for r in existing}
    out, report = [dict(r) for r in existing], []
    for name in roster:
        if name in by_name:
            row = next(r for r in out if r["canonical_name"] == name)
            row["status"] = "active"
            continue
        if name in overrides:
            slug, rule = overrides[name]["id"].strip(), "override: " + overrides[name]["reason"].strip()
        else:
            slug, rule = slug_rule(name)
        base, n = slug, 2
        while slug in used:
            slug = f"{base}-{n}"; n += 1
        if slug != base:
            report.append(f"CLASH {name!r}: {base} taken, assigned {slug}; consider an override")
        used.add(slug)
        out.append(dict(id=slug, canonical_name=name, shard=slug[0], path=f"people/{slug[0]}/{slug}.md",
                        status="active", assigned_in=FIRST_ROSTER, rule=rule, note=""))
    names = set(roster)
    for r in out:
        if r["canonical_name"] not in names and r["status"] == "active":
            r["status"] = "retired"
            report.append(f"RETIRED {r['id']} ({r['canonical_name']}) no longer in roster.csv")
    for r in out:
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", r["id"]):
            sys.exit(f"bad id {r['id']!r} for {r['canonical_name']!r}")
    return out, report


def render(rows):
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=COLS, lineterminator="\n")
    w.writeheader(); w.writerows(rows)
    return buf.getvalue()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="exit 1 if person_ids.csv is out of date")
    a = ap.parse_args()
    rows, report = build()
    text = render(rows)
    old = open(IDS, encoding="utf-8").read() if os.path.exists(IDS) else ""
    for line in report:
        print(line)
    if a.check:
        print("person_ids.csv up to date" if text == old else "person_ids.csv OUT OF DATE (run scripts/assign_ids.py)")
        sys.exit(0 if text == old else 1)
    open(IDS, "w", encoding="utf-8").write(text)
    print(f"{len(rows)} ids ({sum(r['status'] == 'active' for r in rows)} active) -> {os.path.relpath(IDS, REPO)}")


if __name__ == "__main__":
    main()
