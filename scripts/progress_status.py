#!/usr/bin/env python3
"""Write the progress status table in README.md from the repo's own files.

Usage:
    python scripts/progress_status.py            # rewrite the table in README.md
    python scripts/progress_status.py --stdout   # print the table instead
    python scripts/progress_status.py --check    # exit 1 if the README table is out of date

The table sits between the markers <!-- BEGIN GENERATED: progress --> and
<!-- END GENERATED: progress --> in README.md. The caption of the person chart sits between
<!-- BEGIN GENERATED: people_chart_caption --> and <!-- END GENERATED: people_chart_caption -->;
it is computed by lib.records.people_chart_caption() from the same records the chart plots.
Everything outside the markers is hand-written.

Where each row comes from:
    roster counts      data/roster/roster.csv (status column)
    people coded       person files in people/ whose roster status is core
    systems sourced    systems/*.md whose review_status is not "stub"
    decisions          the summary table in docs/OPEN_DECISIONS.md (rows marked "decided")
    latest tag         `git tag --sort=-creatordate` (falls back to "none" outside a git checkout)
    audits, next steps MANUAL: the AUDITS and NEXT_STEPS constants below. Update them by hand.
"""
import argparse, collections, os, re, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.records import REPO, read_record, read_csv, person_files, system_files, people_chart_caption  # noqa: E402

README = os.path.join(REPO, "README.md")
BEGIN, END = "<!-- BEGIN GENERATED: progress -->", "<!-- END GENERATED: progress -->"
CAP_BEGIN, CAP_END = "<!-- BEGIN GENERATED: people_chart_caption -->", "<!-- END GENERATED: people_chart_caption -->"

# MANUAL rows. No file in the repo records these as data, so they are kept here by hand.
AUDITS = ("9 blind lens runs on four batches: 3 on a 115-claim packet (eff4700), 2 on a 147-claim packet (e648145), 2 on a "
          "124-claim packet (d9903b7/43cecc4; fixes at 6f37cd6) and 2 on a 165-claim packet (b21655b; run 1 155 hold / 10 weaken, "
          "run 2 160 hold / 5 weaken, 0 wrong; agreement 156/165, κ 0.37; fixes applied at 3bcd59c); see "
          "[reports/audit_2026-10-02.md](reports/audit_2026-10-02.md). Stage 3: 4 blind runs on the first 12 records (stage 3-a: "
          "561 claims at 59a8371; stage 3-b: 420 claims at 3db6511); their method rulings are decisions P14–P28; one blind run on the stage 3-b rulings (93 claims at 6155174: 88 hold, 4 weaken, 1 fail, fixed at 4c10399) gave P29; lens's runs on the v8.a rulings packet (34a73c4) and the v8.b P29 packet (e930597) gave P30; the P30 span-alignment audit (7a52a3f) gave P31")
NEXT_STEPS = ("Stage 3 (everyone else with F ≥ 3) has started: the first 12 records (Spinoza, Descartes, Pascal, Leibniz, Kant, "
              "Hume, Darwin, Gauss, Riemann, Turing, Noether, von Neumann) are drafts that still need to apply P29 and P30 (the stage 3-b six "
              "follow P14–P28 on main; the stage 3-a six also still need P14–P28); the other 31 records follow P14–P28 (schema 1.3) and "
              "P30's age rule, and their worldview.working_years now equals timing.major_work_period (P30 addendum); under P31 (continuity rule) all 55 values the span audit flagged stand; the strict-period alternative is in reports/period_rule_sensitivity.md; source the stubs on the S7 backlog "
              "(ATHE, AGNOS, KANT, SCEPT, RATN, EMPIR, IDEAL); the revised rubric has not started")


def latest_tag():
    try:
        out = subprocess.run(["git", "-C", REPO, "tag", "--sort=-creatordate"], capture_output=True, text=True, check=True)
        tags = [t for t in out.stdout.split() if t]
        return f"`{tags[0]}`" if tags else "none"
    except (OSError, subprocess.CalledProcessError):
        return "none"


def decisions():
    rows = re.findall(r"^\| ([RPS]\d+) \|.*\|\s*([^|]*?)\s*\|\s*$",
                      open(os.path.join(REPO, "docs", "OPEN_DECISIONS.md"), encoding="utf-8").read(), re.M)
    ids = {}
    for i, status in rows:
        ids.setdefault(i, status)
    settled = sum(1 for s in ids.values() if s.lower().startswith("decided"))
    return settled, len(ids)


def table():
    roster = read_csv(os.path.join(REPO, "data", "roster", "roster.csv"))
    st = collections.Counter(r["status"] for r in roster)
    core_names = {r["canonical_name"] for r in roster if r["status"] == "core"}
    coded = 0
    for f in person_files():
        d, _ = read_record(f)
        if d["identity"]["roster"]["canonical_name"] in core_names:
            coded += 1
    systems = [read_record(f)[0] for f in system_files()]
    sourced = sum(1 for d in systems if d["record"]["review_status"] != "stub")
    settled, n_dec = decisions()
    tag = latest_tag()
    other = len(roster) - st["core"] - st["provisional"] - st["review"]
    rows = [
        ("Roster people", f"{len(roster):,}: {st['core']} core, {st['provisional']} provisional, {st['review']} review"
                          + (f", {other} new names still need a status" if other else "")),
        ("People coded (of core)", f"{coded} / {st['core']} (draft, unreviewed)"),
        ("Belief systems sourced", f"{sourced} / {len(systems)} (the rest are stubs)"),
        ("Decisions settled", f"{settled} / {n_dec}"),
        ("Audits", AUDITS),
        ("Latest tag", tag + (" (prerelease)" if re.search(r"alpha|beta|rc", tag) else "")),
        ("Next steps", NEXT_STEPS),
    ]
    out = [BEGIN,
           "<!-- Generated by scripts/progress_status.py; the Audits and Next steps rows are manual constants in that script. -->",
           "", "| Item | Status |", "|---|---|"]
    out += [f"| {k} | {v} |" for k, v in rows]
    out += ["", END]
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stdout", action="store_true")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    new = table()
    if a.stdout:
        print(new)
        return
    text = open(README, encoding="utf-8").read()
    if BEGIN not in text or END not in text:
        sys.exit(f"README.md has no {BEGIN} ... {END} block")
    i, j = text.index(BEGIN), text.index(END) + len(END)
    updated = text[:i] + new + text[j:]
    if CAP_BEGIN not in updated or CAP_END not in updated:
        sys.exit(f"README.md has no {CAP_BEGIN} ... {CAP_END} block")
    i, j = updated.index(CAP_BEGIN), updated.index(CAP_END) + len(CAP_END)
    updated = updated[:i] + CAP_BEGIN + "\n" + people_chart_caption() + "\n" + CAP_END + updated[j:]
    if a.check:
        if updated != text:
            print("README.md progress table or person-chart caption is out of date; run scripts/progress_status.py")
            sys.exit(1)
        print("README.md progress table up to date")
        return
    if updated != text:
        open(README, "w", encoding="utf-8").write(updated)
        print("updated README.md progress table")
    else:
        print("README.md progress table already up to date")


if __name__ == "__main__":
    main()
