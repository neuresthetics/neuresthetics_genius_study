#!/usr/bin/env python3
"""
Validate belief-system files (systems/<CODE>.md) against schema/system.schema.json and the v7.1 data book.

Checks
  1. YAML front matter passes the JSON Schema (same claim rules as person files).
  2. identity.id matches the file name; all 77 v7.1 codes have a file, and no file has an unknown code
     (a new code is allowed only if identity.v7_1_number is absent — not possible in schema 1.0, so any
     new system needs a schema bump; see docs/OPEN_DECISIONS.md).
  3. v7_1_rubric (L, P, E, V, X, total, number) equals data book tables[4], and scoring_note equals the
     section 7 paragraph, character for character. The v7.1 scores are authorial and frozen here.
  4. related_codes / neighbors / schools_and_variants codes exist.
  5. Citations resolve to listed sources; required body sections exist.
  6. Warns if L+P+E+V+X != total (reported, not "fixed": the data book is the record of v7.1).

Usage
  python3 scripts/validate_systems.py                 # all 77
  python3 scripts/validate_systems.py systems/PANT.md
  python3 scripts/validate_systems.py --strict
"""
import argparse, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.records import REPO, read_record, load_schema, schema_errors, common_checks, system_files, fill_counts, walk

V7_JSON = os.path.join(REPO, "data", "sources", "v7_1", "neuresthetics_v7_combined.json")
REQUIRED_SECTIONS = ["Summary", "Core metaphysics", "Position on the LIO axes", "Schools and variants", "Science",
                     "Coding guidance", "v7.1 scoring note", "Open questions", "Research log"]
NOTE_RE = re.compile(r"^(?P<code>[A-Z0-9_]+) \((?P<tot>\d+)/50\) — (?P<rest>.*)$", re.S)


def data_book():
    d = json.load(open(V7_JSON, encoding="utf-8"))["documents"]["data_book"]["content"]
    hdr, *rows = d["tables"][4]
    rows = {r[1]: dict(zip(hdr, r)) for r in rows}
    paras = {}
    for p in d["paragraphs"]:
        t = (p["text"] if isinstance(p, dict) else p).strip()
        m = NOTE_RE.match(t)
        if m:
            paras[m["code"]] = m["rest"]
    return rows, paras


def main():
    ap = argparse.ArgumentParser(description="Validate belief-system files")
    ap.add_argument("files", nargs="*")
    ap.add_argument("--strict", action="store_true")
    a = ap.parse_args()
    schema = load_schema("system.schema.json")
    rows, paras = data_book()
    all_files = system_files()
    codes = {os.path.basename(f)[:-3] for f in all_files}
    files = [os.path.abspath(f) for f in a.files] or all_files
    n_bad = 0
    global_errors = []
    if not a.files:
        for c in sorted(set(rows) - codes):
            global_errors.append(f"v7.1 code {c} has no file in systems/")
        for c in sorted(codes - set(rows)):
            global_errors.append(f"systems/{c}.md is not one of the 77 v7.1 codes")
    for f in files:
        errors, warnings = [], []
        rel = os.path.relpath(f, REPO)
        code = os.path.basename(f)[:-3]
        try:
            data, body = read_record(f)
        except Exception as e:  # noqa: BLE001
            print(f"FAIL {rel}\n  ERROR cannot read: {e}"); n_bad += 1; continue
        errors += schema_errors(schema, data)
        e2, w2 = common_checks(data, body, REQUIRED_SECTIONS)
        errors += e2; warnings += w2
        ident = data.get("identity") or {}
        if ident.get("id") != code:
            errors.append(f"identity/id {ident.get('id')!r} does not match file name {code}")
        row = rows.get(code)
        rub = data.get("v7_1_rubric") or {}
        if row:
            want = {"L": int(row["L"]), "P": int(row["P"]), "E": int(row["E"]), "V": int(row["V"]), "X": int(row["X"]),
                    "total": int(row["Tot"])}
            for k, v in want.items():
                if rub.get(k) != v:
                    errors.append(f"v7_1_rubric/{k}: file has {rub.get(k)!r}, data book has {v}")
            if ident.get("v7_1_number") != int(row["#"]):
                errors.append(f"identity/v7_1_number: file has {ident.get('v7_1_number')!r}, data book has {row['#']}")
            rest = paras.get(code, "")
            if rub.get("scoring_note") and rub["scoring_note"] not in rest:
                errors.append("v7_1_rubric/scoring_note is not verbatim from data book section 7")
            s = sum(want[k] for k in "LPEVX")
            if s != want["total"]:
                warnings.append(f"v7.1 L+P+E+V+X = {s} but data book total = {want['total']} (kept as published)")
        for p, d in walk({k: data.get(k) for k in ("classification", "coding_guidance", "schools_and_variants")}):
            c = d.get("code")
            if c and c not in codes:
                errors.append(f"{'/'.join(p)}: code {c!r} is not a file in systems/")
        if a.strict:
            errors, warnings = errors + warnings, []
        n_bad += bool(errors)
        fc = fill_counts(data)
        tot = {k: sum(s_[k] for s_ in fc.values()) for k in ("FILLED", "TODO", "UNKNOWN", "BELOW_THRESHOLD")}
        status = (data.get("record") or {}).get("review_status")
        print(f"{'PASS' if not errors else 'FAIL'} {rel}  [{status}]  claims: {tot['FILLED']} filled, {tot['TODO']} TODO")
        for e in errors:
            print(f"  ERROR {e}")
        for w in warnings:
            print(f"  warn  {w}")
    for e in global_errors:
        print(f"ERROR {e}")
    print(f"\n{len(files) - n_bad}/{len(files)} files pass" + (f"; {len(global_errors)} set-level errors" if global_errors else ""))
    return 1 if (n_bad or global_errors) else 0


if __name__ == "__main__":
    sys.exit(main())
