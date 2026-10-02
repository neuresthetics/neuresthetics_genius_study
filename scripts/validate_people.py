#!/usr/bin/env python3
"""
Validate person files (people/<shard>/<id>.md) against schema/person.schema.json and the roster.

Checks
  1. The file has YAML front matter that passes the JSON Schema (every filled claim has a value,
     a certainty, at least one citation and a how_known note; sentinels are TODO / UNKNOWN / BELOW_THRESHOLD).
  2. The id is in data/roster/person_ids.csv as active, and the file sits at the path listed there.
  3. identity.roster matches the person's row in data/roster/roster.csv exactly.
  4. Worldview codes (primary, secondary, candidates) exist in systems/; filled worldview codes and LIO axis
     scores carry a basis, and certainty does not exceed the basis ceiling (1.0 / 0.7 / 0.5; CODING_GUIDE §3).
  5. Every citation (front matter and [S#] in the body) points at a listed source; unused sources are warned.
  6. Collaborator roster_ids exist in person_ids.csv.
  7. The body has every required section heading.
  8. data/reference/regions.csv (P3 country-to-region table) uses exactly the schema's region values, with no
     duplicate countries.

Usage
  python3 scripts/validate_people.py                     # all person files
  python3 scripts/validate_people.py people/f/faraday-michael.md
  python3 scripts/validate_people.py --strict            # warnings count as errors
  python3 scripts/validate_people.py --template          # also check templates/person.template.md parses
Exit status 0 = all files pass.
"""
import argparse, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.records import (REPO, read_record, load_schema, schema_errors, common_checks, read_csv, system_codes,
                         person_files, fill_counts, walk)

REQUIRED_SECTIONS = ["Summary", "Contribution and impact", "Childhood and education", "Adult working worldview",
                     "Heritage (context only)", "Timing", "Lane B notes (labeled belief model)", "Open questions",
                     "Research log"]


def roster_view(row):
    return {"canonical_name": row["canonical_name"], "rank": int(row["rank"]), "F": int(row["F"]),
            "models": row["models"].split(";"), "band": row["band"], "status": row["status"],
            "field": row["field"], "field_bucket": row["field_bucket"]}


def check_person(path, schema, ids, roster, codes, is_template=False):
    errors, warnings = [], []
    try:
        data, body = read_record(path)
    except Exception as e:  # noqa: BLE001
        return [f"cannot read: {e}"], [], None
    errors += schema_errors(schema, data)
    e2, w2 = common_checks(data, body, REQUIRED_SECTIONS)
    errors += e2; warnings += w2
    ident = data.get("identity") or {}
    pid = ident.get("id")
    if not is_template:
        rel = os.path.relpath(path, REPO).replace(os.sep, "/")
        row = ids.get(pid)
        if row is None:
            errors.append(f"identity/id '{pid}' is not in data/roster/person_ids.csv")
        else:
            if row["status"] != "active":
                errors.append(f"identity/id '{pid}' is {row['status']} in person_ids.csv")
            if row["path"] != rel:
                errors.append(f"file is at {rel} but person_ids.csv says {row['path']}")
            rrow = roster.get(row["canonical_name"])
            if rrow is None:
                errors.append(f"'{row['canonical_name']}' is not in roster.csv")
            else:
                want = roster_view(rrow)
                got = ident.get("roster") or {}
                for k, v in want.items():
                    if got.get(k) != v:
                        errors.append(f"identity/roster/{k}: file has {got.get(k)!r}, roster.csv has {v!r}")
    wv = data.get("worldview") or {}
    for key in ("primary_system", "secondary_system"):
        c = wv.get(key) or {}
        v = c.get("value")
        if isinstance(v, str) and v not in {"TODO", "UNKNOWN", "BELOW_THRESHOLD"} and v not in codes:
            errors.append(f"worldview/{key}: code {v!r} is not a file in systems/")
    worldview_claims = [("worldview/" + k, wv.get(k) or {}) for k in ("primary_system", "secondary_system")] + \
        [("worldview/lio_axes/" + k, v or {}) for k, v in (wv.get("lio_axes") or {}).items()]
    for where, c in worldview_claims:
        v = c.get("value")
        if v is not None and not (isinstance(v, str) and v in {"TODO", "UNKNOWN", "BELOW_THRESHOLD"}) and not c.get("basis"):
            errors.append(f"{where}: a filled worldview claim needs basis (written_profession / consistent_private_letters / scholarly_reconstruction)")
    for i, c in enumerate(wv.get("candidate_codes_considered") or []):
        if c.get("code") not in codes:
            errors.append(f"worldview/candidate_codes_considered/{i}: code {c.get('code')!r} is not a file in systems/")
    for p, d in walk(data.get("collaborators") or []):
        rid = d.get("roster_id")
        if rid and rid not in ids:
            errors.append(f"collaborators/{'/'.join(p)}: roster_id {rid!r} is not in person_ids.csv")
    return errors, warnings, data


def check_regions(schema):
    """data/reference/regions.csv must use exactly the schema's region values (decision P3)."""
    errors = []
    enum = None
    for alt in schema.schema["$defs"]["region"]["properties"]["value"]["anyOf"]:
        if "enum" in alt:
            enum = set(alt["enum"])
    rows = read_csv(os.path.join(REPO, "data", "reference", "regions.csv"))
    used = {r["study_region"] for r in rows}
    for r in rows:
        if r["study_region"] not in enum:
            errors.append(f"regions.csv: {r['country_or_area']!r} has study_region {r['study_region']!r}, not a schema region")
    for v in sorted(enum - used):
        errors.append(f"regions.csv: schema region {v!r} has no country")
    names = [r["iso3"] for r in rows]
    for n in sorted({n for n in names if names.count(n) > 1}):
        errors.append(f"regions.csv: duplicate iso3 {n}")
    return errors, len(rows)


def main():
    ap = argparse.ArgumentParser(description="Validate person files")
    ap.add_argument("files", nargs="*")
    ap.add_argument("--strict", action="store_true", help="treat warnings as errors")
    ap.add_argument("--template", action="store_true", help="also validate templates/person.template.md (schema only)")
    a = ap.parse_args()
    schema = load_schema("person.schema.json")
    ids = {r["id"]: r for r in read_csv(os.path.join(REPO, "data", "roster", "person_ids.csv"))}
    roster = {r["canonical_name"]: r for r in read_csv(os.path.join(REPO, "data", "roster", "roster.csv"))}
    codes = system_codes()
    files = [os.path.abspath(f) for f in a.files] or person_files()
    targets = [(f, False) for f in files]
    if a.template:
        targets.append((os.path.join(REPO, "templates", "person.template.md"), True))
    if not targets:
        print("no person files found"); return 0
    n_bad = 0
    rerr, nreg = check_regions(schema)
    print(("PASS" if not rerr else "FAIL") + f" data/reference/regions.csv  {nreg} countries")
    for e in rerr:
        print(f"  ERROR {e}")
    n_bad += bool(rerr)
    for f, tmpl in targets:
        errors, warnings, data = check_person(f, schema, ids, roster, codes, is_template=tmpl)
        if a.strict:
            errors, warnings = errors + warnings, []
        rel = os.path.relpath(f, REPO)
        status = "PASS" if not errors else "FAIL"
        n_bad += bool(errors)
        counts = ""
        if data is not None:
            fc = fill_counts(data)
            tot = {k: sum(s[k] for s in fc.values()) for k in ("FILLED", "TODO", "UNKNOWN", "BELOW_THRESHOLD")}
            counts = f"  claims: {tot['FILLED']} filled, {tot['TODO']} TODO, {tot['UNKNOWN']} UNKNOWN, {tot['BELOW_THRESHOLD']} below threshold"
        print(f"{status} {rel}{counts}")
        for e in errors:
            print(f"  ERROR {e}")
        for w in warnings:
            print(f"  warn  {w}")
    print(f"\n{len(targets) - n_bad}/{len(targets)} files pass")
    return 1 if n_bad else 0


if __name__ == "__main__":
    sys.exit(main())
