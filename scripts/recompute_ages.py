#!/usr/bin/env python3
"""
Recompute the age fields in person records under decision P30 (rule 5): age = event year − birth year,
with no month adjustment.

Age fields (schema/person.schema.json):
  * timing.age_at_first_lasting_contribution   = basics.first_lasting_contribution_year − birth year
  * `age` on any item or event that has a `year` (childhood events, early science, changes_over_life,
    timing.first_evidence_of_lio_type_views, ...)          = year − birth year
  * `ages` on a schooling stage that has `years`          = years − birth year
The birth year is the year of basics.birth.date.value, as recorded (Julian dates keep their own year).

String ages keep their wording: each number in the age is replaced, in order, by the matching year in the
year field minus the birth year ("c. 1655–1661" with birth 1642 gives "c. 13–19"). A parenthetical in the
year field is ignored. When the year field has one year and the age is a range of two consecutive numbers
(month uncertainty), the range becomes the one computed age. Anything else (no year, numbers that do not
line up, a year outside birth year to birth year + 130) is left alone and listed as "not computable".

Only age values change. With --write, a changed age_at_first_lasting_contribution also gets one sentence
added to its how_known, the body sentence that restates it ("<year>, at <age>") is updated, and each changed
record gets record_version + 1, last_updated and a change_log line. Other ages in the body (a source's "at 14")
are not touched; check them by hand.
The script edits the file text in place and then re-reads it to check that nothing else changed.

Usage
  python3 scripts/recompute_ages.py --check  [--exclude id1,id2 ...]   # exit 1 if any age would change
  python3 scripts/recompute_ages.py --write  [--exclude id1,id2 ...] [--csv reports/p30_age_changes.csv]
  python3 scripts/recompute_ages.py --check people/b/bohr-niels.md     # one file
"""
import argparse, copy, csv, datetime, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.records import REPO, read_record, person_files, walk  # noqa: E402

SENT = {"TODO", "UNKNOWN", "BELOW_THRESHOLD"}
NUM = re.compile(r"\d+")
LOG_SUMMARY = ("P30 rule 5 age sweep: ages recomputed as event year − birth year, with no month adjustment "
               "(scripts/recompute_ages.py; every change is in reports/p30_age_changes.csv). No other value changed.")


def birth_year(data):
    v = (((data.get("basics") or {}).get("birth") or {}).get("date") or {}).get("value")
    m = re.match(r"^(-?\d+)", str(v)) if v is not None and str(v) not in SENT else None
    return int(m.group(1)) if m else None


def years_in(s, by):
    """The years in a year field, in order, ignoring parentheticals. None if any is implausible."""
    s = re.sub(r"\([^)]*\)", "", str(s))
    ys = [int(x) for x in NUM.findall(s)]
    if not ys or any(y < by or y > by + 130 for y in ys):
        return None
    return ys


def recompute(age, year, by):
    """Return the recomputed age (same type as `age`), or None if it cannot be computed."""
    if by is None or by < 0 or year is None or age is None or str(age) in SENT or str(year) in SENT:
        return None
    if isinstance(year, int) and isinstance(age, int):
        return year - by if by <= year <= by + 130 else None
    ys = years_in(year, by)
    if ys is None:
        return None
    a = str(age)
    nums = list(NUM.finditer(a))
    if not nums:
        return None
    if len(nums) == len(ys):
        out, last = [], 0
        for m, y in zip(nums, ys):
            out += [a[last:m.start()], str(y - by)]
            last = m.end()
        new = "".join(out) + a[last:]
    elif len(ys) == 1 and len(nums) == 2 and int(nums[1].group()) == int(nums[0].group()) + 1 \
            and re.fullmatch(r"\s*[–-]\s*", a[nums[0].end():nums[1].start()]):
        new = a[:nums[0].start()] + str(ys[0] - by) + a[nums[1].end():]
    else:
        return None
    if isinstance(age, int):
        return int(new) if new.strip().isdigit() else None
    return new


def plan(data):
    """List of changes (path tuple, key, old, new) and of skipped age fields (path, key, value, reason)."""
    by = birth_year(data)
    changes, skipped = [], []
    t = (data.get("timing") or {}).get("age_at_first_lasting_contribution") or {}
    fl = ((data.get("basics") or {}).get("first_lasting_contribution_year") or {}).get("value")
    old = t.get("value")
    if isinstance(old, int) and isinstance(fl, int) and by is not None:
        if fl - by != old:
            changes.append((("timing", "age_at_first_lasting_contribution"), "value", old, fl - by))
    elif old not in SENT and old is not None:
        skipped.append((("timing", "age_at_first_lasting_contribution"), "value", old, "no integer first lasting year"))
    for p, d in walk(data):
        for key, ykey in (("age", "year"), ("ages", "years")):
            if key not in d:
                continue
            new = recompute(d[key], d.get(ykey), by)
            if new is None:
                if str(d[key]) not in SENT:
                    skipped.append((p, key, d[key], f"no usable {ykey}" if d.get(ykey) is None else "not computable"))
            elif new != d[key]:
                changes.append((p, key, d[key], new))
    return changes, skipped


def yaml_scalar(v):
    return str(v) if isinstance(v, int) else '"' + str(v).replace("\\", "\\\\").replace('"', '\\"') + '"'


def scalar_patterns(key, v):
    """Regexes for `key: v` as it may be written in a flow mapping."""
    s = re.escape(str(v))
    pats = [rf"\b{key}: {s}(?=[,}}\s])"] if isinstance(v, int) else []
    pats += [rf'\b{key}: "{s}"', rf"\b{key}: '{s}'", rf"\b{key}: {s}(?=[,}}])"]
    return pats


def apply_changes(path, text, data, changes, today):
    """Edit the text line by line. Each change is found on the line whose flow mapping parses to the node."""
    import yaml
    lines = text.split("\n")
    end = text.find("\n---\n", 4)
    fm_last = text[:end].count("\n")
    for p, key, old, new in changes:
        node = data
        for k in p:
            node = node[int(k)] if isinstance(node, list) else node[k]
        hit = None
        for i in range(1, fm_last + 1):
            line = lines[i]
            body = re.sub(r"^\s*(-\s+|[A-Za-z_][\w]*:\s+)", "", line, count=1)
            if not body.startswith("{"):
                continue
            try:
                parsed = yaml.safe_load(body)
            except Exception:  # noqa: BLE001
                continue
            if isinstance(parsed, dict) and parsed.get(key) == old and parsed.get("value") == node.get("value") \
                    and (p[-1] != "age_at_first_lasting_contribution" or line.lstrip().startswith("age_at_first_lasting_contribution:")):
                if hit is not None:
                    raise SystemExit(f"{path}: {'/'.join(p)} matches more than one line")
                hit = i
        if hit is None:
            raise SystemExit(f"{path}: cannot find the line for {'/'.join(p)}")
        line = lines[hit]
        for pat in scalar_patterns(key, old):
            line2, n = re.subn(pat, f"{key}: {yaml_scalar(new)}", line, count=1)
            if n:
                break
        else:
            raise SystemExit(f"{path}: cannot rewrite {key} on line {hit + 1}")
        if p == ("timing", "age_at_first_lasting_contribution"):
            fl = data["basics"]["first_lasting_contribution_year"]["value"]
            add = (f" P30 (rule 5): {fl} − {birth_year(data)} = {new}, with no month adjustment; was {old}"
                   f" until the P30 age sweep ({today}).")
            line2, n = re.subn(r'(how_known: "(?:[^"\\]|\\.)*?)"', lambda m: m.group(1) + add + '"', line2, count=1)
            if not n:
                raise SystemExit(f"{path}: cannot extend how_known on line {hit + 1}")
        lines[hit] = line2
    # bookkeeping: record_version, last_updated, change_log
    out = "\n".join(lines)
    out = fix_body(path, out, data, changes)
    out, n1 = re.subn(r"^(  record_version: )(\d+)", lambda m: m.group(1) + str(int(m.group(2)) + 1), out, count=1, flags=re.M)
    out, n2 = re.subn(r"^(  last_updated: ).*$", lambda m: m.group(1) + today, out, count=1, flags=re.M)
    m = re.search(r"^  change_log:\n((?:    - .*\n)+)", out, flags=re.M)
    if not (n1 and n2 and m):
        raise SystemExit(f"{path}: record_version, last_updated or change_log not found")
    entry = f'    - {{date: {today}, by: "Grok Bot", summary: "{LOG_SUMMARY}"}}\n'
    out = out[:m.end()] + entry + out[m.end():]
    return out


def fix_body(path, text, data, changes):
    """The body restates the first-lasting age as "<year>, at <age>" (Timing section). Update the first
    "at <age>" in the same sentence after the year when it is the old value; print what was changed."""
    end = text.find("\n---\n", 4) + 5
    head, body = text[:end], text[end:]
    for p, key, old, new in changes:
        if p != ("timing", "age_at_first_lasting_contribution"):
            continue
        fl = str(data["basics"]["first_lasting_contribution_year"]["value"])
        out, pos = [], 0
        for m in re.finditer(rf"\b{fl}\b", body):
            if m.start() < pos:
                continue
            stop = re.search(r"[.\n]", body[m.end():])
            seg_end = m.end() + (stop.start() if stop else len(body) - m.end())
            a = re.search(r"\bat (?:about )?(?:age )?(\d+)\b", body[m.end():seg_end])
            if a and a.group(1) == str(old):
                i = m.end() + a.start(1)
                out += [body[pos:i], str(new)]
                pos = i + len(a.group(1))
                print(f"  body {os.path.basename(path)}: '{body[m.start():seg_end].strip()}' -> age {new}")
        body = "".join(out) + body[pos:]
    return head + body


def verify(path, before, changes, today):
    """Re-read the file and check that only the planned fields changed."""
    after, _ = read_record(path)
    want = copy.deepcopy(before)
    for p, key, old, new in changes:
        node = want
        for k in p:
            node = node[int(k)] if isinstance(node, list) else node[k]
        node[key] = new
        if p == ("timing", "age_at_first_lasting_contribution"):
            node["how_known"] = after["timing"]["age_at_first_lasting_contribution"]["how_known"]
    want["record"]["record_version"] = before["record"]["record_version"] + 1
    want["record"]["last_updated"] = today
    want["record"]["change_log"] = before["record"]["change_log"] + [after["record"]["change_log"][-1]]
    if after != want:
        raise SystemExit(f"{path}: re-read differs from the plan; restore it with git checkout and check the script")
    left, _ = plan(after)
    if left:
        raise SystemExit(f"{path}: ages still differ after writing: {left}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="report changes; exit 1 if any")
    mode.add_argument("--write", action="store_true", help="write the changes into the files")
    ap.add_argument("--exclude", action="append", default=[], help="person ids to skip (comma-separated, repeatable)")
    ap.add_argument("--csv", help="write the change list (person, field, old, new) to this CSV")
    ap.add_argument("--quiet", action="store_true", help="do not list the age fields that cannot be computed")
    ap.add_argument("files", nargs="*")
    a = ap.parse_args()
    exclude = {x.strip() for e in a.exclude for x in e.split(",") if x.strip()}
    files = [os.path.abspath(f) for f in a.files] or person_files()
    today = datetime.date.today().isoformat()
    rows, n_skipped, n_files = [], 0, 0
    for f in files:
        pid = os.path.basename(f)[:-3]
        if pid in exclude:
            continue
        data, _ = read_record(f)
        changes, skipped = plan(data)
        n_skipped += len(skipped)
        if not a.quiet:
            for p, key, v, why in skipped:
                print(f"  skip {pid}: {'/'.join(p)}.{key} = {v!r} ({why})")
        for p, key, old, new in changes:
            field = "/".join(p) + ("" if key == "value" else "." + key)
            rows.append({"person": pid, "field": field, "old": old, "new": new})
            print(f"{'CHANGE' if a.check else 'write '} {pid}: {field}: {old!r} -> {new!r}")
        if changes and a.write:
            text = open(f, encoding="utf-8").read()
            new_text = apply_changes(f, text, data, changes, today)
            with open(f, "w", encoding="utf-8") as fh:
                fh.write(new_text)
            verify(f, data, changes, today)
        if changes:
            n_files += 1
    if a.csv:
        with open(a.csv, "w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=["person", "field", "old", "new"])
            w.writeheader()
            w.writerows(rows)
    verb = "would change" if a.check else "changed"
    print(f"\n{len(rows)} age values {verb} in {n_files} records; {n_skipped} age fields not computable (left as they are); "
          f"{len(exclude)} ids excluded.")
    sys.exit(1 if (a.check and rows) else 0)


if __name__ == "__main__":
    main()
