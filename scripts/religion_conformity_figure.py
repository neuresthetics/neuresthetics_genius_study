#!/usr/bin/env python3
"""Counts and one figure for religion_conformity. Does not draw the other figures.

Usage:
    python3 scripts/religion_conformity_figure.py
    python3 scripts/religion_conformity_figure.py --no-figure

Writes figures/religion_conformity_stated_x_gap.png (stated affiliation by practice gap).
Prints frequency tables. Lane A counts only. Not a test of the Lane B hypothesis.
"""
import argparse
import collections
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.records import REPO, person_files, read_record

STATED_ORDER = [
    "christian_catholic", "christian_protestant", "christian_orthodox", "christian_other",
    "jewish", "muslim", "hindu", "buddhist", "confucian", "daoist", "other_stated",
    "secular", "mixed", "none_stated", "unknown",
]
PRESSURE_ORDER = ["low", "moderate", "high", "severe", "unknown"]
GAP_ORDER = ["aligned", "mixed", "divergent", "unknown"]


def load():
    rows = []
    for path in person_files():
        data, _ = read_record(path)
        block = data.get("religion_conformity") or {}
        stated = (block.get("stated_affiliation") or {}).get("label")
        pressure = (block.get("conformity_pressure") or {}).get("level")
        gap = (block.get("practice_gap") or {}).get("gap")
        rows.append({
            "id": (data.get("identity") or {}).get("id"),
            "name": (data.get("identity") or {}).get("display_name"),
            "stated": stated,
            "pressure": pressure,
            "gap": gap,
            "gap_evidence": (block.get("practice_gap") or {}).get("evidence") or "",
            "stated_detail": (block.get("stated_affiliation") or {}).get("detail") or "",
            "pressure_evidence": (block.get("conformity_pressure") or {}).get("evidence") or "",
        })
    return rows


def print_table(title, order, counts):
    print(title)
    n = sum(counts.values())
    for key in order:
        c = counts.get(key, 0)
        if c or key in counts:
            print(f"  {key:24} {c:4}  {100 * c / n if n else 0:5.1f}%")
    extra = [k for k in counts if k not in order]
    for key in extra:
        print(f"  {key:24} {counts[key]:4}")
    print(f"  {'total':24} {n:4}")


def main():
    ap = argparse.ArgumentParser(description="Religion-conformity counts and one figure")
    ap.add_argument("--no-figure", action="store_true")
    ap.add_argument("--out", default=os.path.join(REPO, "figures", "religion_conformity_stated_x_gap.png"))
    a = ap.parse_args()
    rows = load()
    stated = collections.Counter(r["stated"] for r in rows)
    pressure = collections.Counter(r["pressure"] for r in rows)
    gap = collections.Counter(r["gap"] for r in rows)
    print_table("stated_affiliation", STATED_ORDER, stated)
    print()
    print_table("conformity_pressure", PRESSURE_ORDER, pressure)
    print()
    print_table("practice_gap", GAP_ORDER, gap)
    print()
    cross = collections.Counter((r["stated"], r["gap"]) for r in rows)
    print("stated_affiliation x practice_gap")
    header = " ".join(f"{g[:3]:>5}" for g in GAP_ORDER)
    print(f"  {'label':24} {header}")
    for s in STATED_ORDER:
        cells = " ".join(f"{cross[(s, g)]:5d}" for g in GAP_ORDER)
        if any(cross[(s, g)] for g in GAP_ORDER):
            print(f"  {s:24} {cells}")
    if a.no_figure:
        return 0
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    labels = [s for s in STATED_ORDER if any(cross[(s, g)] for g in GAP_ORDER)]
    fig, ax = plt.subplots(figsize=(8.2, max(3.6, 0.38 * len(labels) + 1.8)))
    colors = {"aligned": "#4C78A8", "mixed": "#F2C14E", "divergent": "#E45756", "unknown": "#C8C8C8"}
    y = list(range(len(labels)))
    left = [0] * len(labels)
    for g in GAP_ORDER:
        vals = [cross[(s, g)] for s in labels]
        ax.barh(y, vals, left=left, color=colors[g], label=g, height=0.72)
        left = [a + b for a, b in zip(left, vals)]
    ax.set_yticks(y)
    ax.set_yticklabels(labels)
    ax.invert_yaxis()
    ax.set_xlabel("People")
    ax.set_title("Stated affiliation × practice gap (Lane A counts)")
    ax.legend(frameon=False, ncol=4, loc="upper center", bbox_to_anchor=(0.5, -0.18))
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.tight_layout()
    fig.subplots_adjust(bottom=0.22)
    fig.text(0.01, 0.01, "Genius Study · descriptive counts only · not a test of the Lane B hypothesis", fontsize=8, color="#444")
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    fig.savefig(a.out, dpi=140)
    print(f"\nwrote {a.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
