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
The not-scorable person list sits between
<!-- BEGIN GENERATED: not_scorable --> and <!-- END GENERATED: not_scorable -->;
it is computed by lib.records.not_scorable_readme_list().
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
from lib.records import REPO, read_record, read_csv, person_files, system_files, people_chart_caption, not_scorable_readme_list  # noqa: E402

README = os.path.join(REPO, "README.md")
BEGIN, END = "<!-- BEGIN GENERATED: progress -->", "<!-- END GENERATED: progress -->"
CAP_BEGIN, CAP_END = "<!-- BEGIN GENERATED: people_chart_caption -->", "<!-- END GENERATED: people_chart_caption -->"
NS_BEGIN, NS_END = "<!-- BEGIN GENERATED: not_scorable -->", "<!-- END GENERATED: not_scorable -->"

# MANUAL rows. No file in the repo records these as data, so they are kept here by hand.
# Keep these short: point to reports/, docs/, and CHANGELOG.md for the long batch trail.
AUDITS = (
    "Early work: 9 blind lens runs on four claim packets — see "
    "[reports/audit_2026-10-02.md](reports/audit_2026-10-02.md). "
    "Stage 3 person batches and belief-system batches S1–S12 were each blind-audited with fixes applied. "
    "Rulings live in [docs/OPEN_DECISIONS.md](docs/OPEN_DECISIONS.md); "
    "batch-by-batch history is in [CHANGELOG.md](CHANGELOG.md)."
)
NEXT_STEPS = (
    "Deepening of all 228 coded person files is done; P47–P50 darkness/hollow cues are applied; "
    "charts refreshed (88 plotted, 140 not scorable). "
    "Systems pass complete (66 sourced, 10 sourced but unscored, 1 stub). "
    "Roster frozen — no new people. "
    "Open for Jason (not blocking): Augustine mid_basin under P4; Linnaeus span end 1758 (RQ-Z5-N1). "
    "Revised rubric has not started. "
    "Details: [docs/OPEN_DECISIONS.md](docs/OPEN_DECISIONS.md), [CHANGELOG.md](CHANGELOG.md)."
)



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
    past_stub = [d for d in systems if d["record"]["review_status"] != "stub"]
    # P46(a): sourced only with at least one value or BELOW_THRESHOLD; all-UNKNOWN = "sourced, unscored"
    unscored = sum(1 for d in past_stub if all((n or {}).get("value") == "UNKNOWN" for n in d["lio_axes"].values()))
    sourced = len(past_stub) - unscored
    settled, n_dec = decisions()
    tag = latest_tag()
    other = len(roster) - st["core"] - st["provisional"] - st["review"]
    rows = [
        ("Roster people", f"{len(roster):,}: {st['core']} core, {st['provisional']} provisional, {st['review']} review"
                          + (f", {other} new names still need a status" if other else "")),
        ("People coded (of core)", f"{coded} / {st['core']} (draft, unreviewed)"),
        ("Belief systems sourced", f"{sourced} / {len(systems)} (P46; plus {unscored} sourced, unscored; the rest are stubs)"),
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
    if NS_BEGIN not in updated or NS_END not in updated:
        sys.exit(f"README.md has no {NS_BEGIN} ... {NS_END} block")
    i, j = updated.index(NS_BEGIN), updated.index(NS_END) + len(NS_END)
    updated = updated[:i] + NS_BEGIN + "\n" + not_scorable_readme_list() + "\n" + NS_END + updated[j:]
    if a.check:
        if updated != text:
            print("README.md progress table, person-chart caption, or not-scorable list is out of date; run scripts/progress_status.py")
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
