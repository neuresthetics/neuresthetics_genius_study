#!/usr/bin/env python3
"""Draw the four descriptive figures in figures/ from the repo's own data files.

Usage:
    pip install -r scripts/requirements.txt -r scripts/requirements-figures.txt
    python scripts/make_figures.py                # write figures/*.png
    python scripts/make_figures.py --out DIR      # write somewhere else

The figures are descriptive only. They show what is in the roster and in the draft
records. They are not results, and no frequency or ranking claim should be read from
them. Every value comes from:
    data/sources/model_lists/*.csv   raw row counts per model list
    data/roster/roster.csv           per-model presence columns, status, field_bucket
    schema/person.schema.json        the 13 study regions
    people/**/*.md                   region_of_birth and worldview.lio_axes
    systems/*.md                     lio_axes
"""
import argparse, collections, json, os, sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Rectangle  # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from matplotlib.lines import Line2D  # noqa: E402
import math  # noqa: E402
from lib.records import (REPO, read_record, read_csv, person_files, people_axis_points)  # noqa: E402

FOOTER = "Genius Study v8.0-alpha · descriptive only, no results"
MODELS = ["Claude", "DeepSeek", "Gemini", "GPT", "Grok"]
LIST_FILES = {"Claude": "geniiClaude.csv", "DeepSeek": "geniiDeepSeek.csv", "Gemini": "geniiGemini.csv",
              "GPT": "geniiGPT.csv", "Grok": "geniiGrok.csv"}
SOURCED_SYSTEMS = ["CLASS_THEISM", "CLTHEI", "CHRIST", "ISLAM", "JUDA", "DEISM", "STOIC", "PLATO", "PANT"]
AXES = ["A_locus", "B_cause", "C_ledger", "D_authority", "E_scope"]
DPI = 170


def footer(fig, source):
    """Source line on the left, one line above the study footer on the right, so they never overlap."""
    fig.text(0.01, 0.035, source, ha="left", va="bottom", fontsize=8, color="#555555")
    fig.text(0.99, 0.008, FOOTER, ha="right", va="bottom", fontsize=8, color="#555555")


def save(fig, out, name):
    path = os.path.join(out, name)
    fig.savefig(path, dpi=DPI, metadata={"Software": None})
    plt.close(fig)
    print("wrote", os.path.relpath(path, REPO) if path.startswith(REPO) else path)


def value(node):
    return node.get("value") if isinstance(node, dict) else node


def roster():
    return read_csv(os.path.join(REPO, "data", "roster", "roster.csv"))


# 1 ------------------------------------------------------------------------
def fig_list_overlap(out):
    rows = roster()
    n_lists = collections.Counter(sum(int(r[m]) for m in MODELS) for r in rows)
    raw = {}
    for m, f in LIST_FILES.items():
        raw[m] = len(read_csv(os.path.join(REPO, "data", "sources", "model_lists", f)))
    present = {m: sum(int(r[m]) for r in rows) for m in MODELS}

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(12, 5.2), gridspec_kw={"width_ratios": [1.1, 1]})
    ks = [1, 2, 3, 4, 5]
    vals = [n_lists.get(k, 0) for k in ks]
    bars = a1.bar([str(k) for k in ks], vals, color="#4C72B0")
    for b, v in zip(bars, vals):
        a1.text(b.get_x() + b.get_width() / 2, v + 12, f"{v:,}", ha="center", fontsize=10)
    a1.set_xlabel("number of the five model lists that name the person")
    a1.set_ylabel("people in the roster")
    a1.set_title(f"Roster people by number of lists (n = {len(rows):,})", fontsize=12)
    a1.set_ylim(0, max(vals) * 1.12)
    a1.spines[["top", "right"]].set_visible(False)

    x = range(len(MODELS))
    w = 0.38
    b1 = a2.bar([i - w / 2 for i in x], [raw[m] for m in MODELS], w, label="raw rows in the list", color="#AAAAAA")
    b2 = a2.bar([i + w / 2 for i in x], [present[m] for m in MODELS], w, label="roster people it names", color="#4C72B0")
    for bs in (b1, b2):
        for b in bs:
            a2.text(b.get_x() + b.get_width() / 2, b.get_height() + 8, f"{int(b.get_height()):,}", ha="center", fontsize=9)
    a2.set_xticks(list(x), MODELS)
    a2.set_ylabel("count")
    a2.set_title(f"Each raw list (total raw rows = {sum(raw.values()):,})", fontsize=12)
    a2.legend(frameon=False, fontsize=9)
    a2.spines[["top", "right"]].set_visible(False)
    a2.set_ylim(0, max(raw.values()) * 1.12)

    fig.suptitle("Where the candidate roster comes from: five LLM-generated lists (V6 period)", fontsize=13)
    footer(fig, "Source: data/roster/roster.csv (per-model columns), data/sources/model_lists/*.csv. "
             "Raw rows include repeats (Gemini lists most names twice, First Last and Last-First) and aliases merged by the rebuild.")
    fig.tight_layout(rect=(0, 0.06, 1, 0.95))
    save(fig, out, "roster_list_overlap.png")


# 2 ------------------------------------------------------------------------
def fig_core_composition(out):
    rows = roster()
    core = [r for r in rows if r["status"] == "core"]
    buckets_all = sorted({r["field_bucket"] for r in rows})
    fb = collections.Counter(r["field_bucket"] for r in core)
    schema = json.load(open(os.path.join(REPO, "schema", "person.schema.json"), encoding="utf-8"))
    regions = [v for alt in schema["$defs"]["region"]["properties"]["value"]["anyOf"] for v in alt.get("enum", [])]
    core_names = {r["canonical_name"] for r in core}
    coded = collections.Counter()
    n_coded = 0
    for f in person_files():
        d, _ = read_record(f)
        if d["identity"]["roster"]["canonical_name"] in core_names:
            n_coded += 1
            coded[value(d["basics"]["region_of_birth"])] += 1

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(13, 7.5), gridspec_kw={"width_ratios": [1, 1.15]})
    reg = list(reversed(regions))
    a1.barh(reg, [coded.get(r, 0) for r in reg], color="#DD8452")
    for i, r in enumerate(reg):
        a1.text(coded.get(r, 0) + 0.05, i, str(coded.get(r, 0)), va="center", fontsize=9)
    a1.set_xlim(0, max(max(coded.values(), default=1) + 1, 5))
    a1.set_xlabel("core people with a coded region of birth")
    a1.set_title(f"Study region (13): only {n_coded} of {len(core)} core people\nhave a region yet "
                 f"(region comes from the person record)", fontsize=11)
    a1.spines[["top", "right"]].set_visible(False)

    fbs = sorted(buckets_all, key=lambda b: (fb.get(b, 0), b))
    a2.barh(fbs, [fb.get(b, 0) for b in fbs], color="#4C72B0")
    for i, b in enumerate(fbs):
        a2.text(fb.get(b, 0) + 0.8, i, str(fb.get(b, 0)), va="center", fontsize=9)
    a2.set_xlabel("core people")
    a2.set_title(f"Field bucket ({len(buckets_all)}): all {len(core)} core people", fontsize=11)
    a2.set_xlim(0, max(fb.values()) * 1.12)
    a2.spines[["top", "right"]].set_visible(False)

    fig.suptitle("Composition of the candidate roster, which comes from LLM-generated lists (not a finding)", fontsize=13)
    footer(fig, "Source: data/roster/roster.csv (status = core, field_bucket); people/**/*.md (region_of_birth).")
    fig.tight_layout(rect=(0, 0.06, 1, 0.95))
    save(fig, out, "core_by_region_field.png")


# 3 ------------------------------------------------------------------------
def fig_people_cause_locus(out):
    """Surnames sit next to their dots on a 5x5 grid. Only the top-right study focus is shaded.
    Full 0-4 range on both axes. People come from people_axis_points(), not a hardcoded list."""
    short_names = {"Galileo Galilei": "Galileo", "Ibn Sina (Avicenna)": "Ibn Sina"}
    # Plain words for the 0-4 scale (CODING_GUIDE §6: 0 pole, 1 leans, 2 mixed, 3 leans other pole with a stated exception, 4 pole)
    y_labels = ["A person outside\nthe world", "Mostly a person\noutside the world", "Mixed",
                "Mostly the order\nof nature", "The order of nature\nitself (or no\nseparate God)"]
    x_labels = ["Miracles /\nintervention", "Mostly\nintervention", "Mixed",
                "Lawful, with a stated\nexception", "Lawful, no\nexceptions"]
    focus, dot = "#DD8452", "#3B6AA0"

    def short(name):
        return short_names.get(name, name.split()[-1])

    pts, _ = people_axis_points()
    cells = collections.defaultdict(list)
    for p in pts:
        cells[(p["B"], p["A"])].append(p)

    fig = plt.figure(figsize=(16, 11))
    ax = fig.add_axes((0.15, 0.13, 0.82, 0.72))
    ax.set_xlim(-0.5, 4.5)
    ax.set_ylim(-0.5, 4.5)

    # The one highlighted region: top right.
    ax.add_patch(Rectangle((2.5, 2.5), 2, 2, facecolor=focus, alpha=0.16, lw=0, zorder=0))
    ax.add_patch(Rectangle((2.5, 2.5), 2, 2, fill=False, edgecolor=focus, lw=2.5, zorder=1))
    ax.text(2.56, 4.44, "The focus:\nGod as nature's order,\nnature fully lawful", ha="left", va="top",
            fontsize=13, fontweight="bold", color="#A0522D", zorder=5)

    # Cells: a small grid of dots, surname to the right of each dot.
    for (b, a), ps in cells.items():
        ps = sorted(ps, key=lambda p: short(p["name"]))
        n = len(ps)
        ncols = 1 if n <= 5 else 2  # one column fits long surnames; two only for crowded cells
        nrows = math.ceil(n / ncols)
        colw = 0.9 / ncols
        rowh = min(0.24, 0.8 / max(nrows, 1))
        for i, p in enumerate(ps):
            c, r = divmod(i, nrows)  # fill down each column first
            x = b - 0.42 + c * colw
            y = a + (nrows - 1) / 2 * rowh - r * rowh
            cert = min(p["cA"], p["cB"])
            faded = cert < 0.7
            ax.scatter(x, y, s=120, color=dot, alpha=0.28 if faded else 0.95,
                       edgecolor="#999999" if faded else "black", lw=0.8, zorder=3)
            ax.text(x + 0.05, y, short(p["name"]), ha="left", va="center", fontsize=12,
                    color="#777777" if faded else "#111111", zorder=4)

    ax.set_xticks(range(5), x_labels, fontsize=11.5)
    ax.set_yticks(range(5), y_labels, fontsize=11.5)
    ax.tick_params(which="both", length=0, pad=8)
    ax.set_xticks([k + 0.5 for k in range(4)], minor=True)
    ax.set_yticks([k + 0.5 for k in range(4)], minor=True)
    ax.grid(which="minor", color="#DDDDDD", lw=1)
    ax.grid(which="major", visible=False)
    for s in ax.spines.values():
        s.set_color("#BBBBBB")
    ax.set_xlabel("How do things happen?", fontsize=15, labelpad=12)
    ax.set_ylabel("Where is God?", fontsize=15, labelpad=12)

    fig.text(0.5, 0.955, "Who sees God as the order of nature, and nature as fully lawful?",
             ha="center", fontsize=20, fontweight="bold")
    fig.text(0.5, 0.915, f"Draft scores for {len(pts)} hand-picked people; not a sample, not a result.",
             ha="center", fontsize=13.5, color="#444444")
    leg = [Line2D([0], [0], marker="o", ls="", markersize=10, markerfacecolor=dot, markeredgecolor="black", alpha=0.95),
           Line2D([0], [0], marker="o", ls="", markersize=10, markerfacecolor=dot, markeredgecolor="#999999", alpha=0.28)]
    ax.legend(leg, ["score as drafted", "faded = less certain score"], loc="upper left", fontsize=11,
              frameon=True, framealpha=0.95, edgecolor="#DDDDDD")
    fig.text(0.01, 0.012, "Source: draft person records in neuresthetics/neuresthetics_genius_study (people/), "
             "unreviewed. Genius Study v8.0-alpha, descriptive only, no results.",
             ha="left", va="bottom", fontsize=8.5, color="#888888")
    save(fig, out, "people_cause_locus.png")


# 4 ------------------------------------------------------------------------
def fig_systems_axes(out):
    import numpy as np
    labels, vals, certs = [], [], []
    for code in SOURCED_SYSTEMS:
        d, _ = read_record(os.path.join(REPO, "systems", f"{code}.md"))
        labels.append(code)
        row, crow = [], []
        for k in AXES:
            node = d["lio_axes"].get(k) or {}
            v = node.get("value")
            row.append(v if isinstance(v, int) else np.nan)
            crow.append(node.get("certainty"))
        vals.append(row)
        certs.append(crow)
    m = np.array(vals, dtype=float)
    fig, ax = plt.subplots(figsize=(9, 7.2))
    cmap = plt.get_cmap("RdYlBu").copy()
    cmap.set_bad("#DDDDDD")
    im = ax.imshow(np.ma.masked_invalid(m), cmap=cmap, vmin=0, vmax=4, aspect="auto")
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            if np.isnan(m[i, j]):
                ax.add_patch(Rectangle((j - 0.5, i - 0.5), 1, 1, fill=False, hatch="///", edgecolor="#888888", lw=0))
                ax.text(j, i, "TODO", ha="center", va="center", fontsize=9)
            else:
                ax.text(j, i, f"{int(m[i, j])}\n({certs[i][j]})", ha="center", va="center", fontsize=10,
                        color="white" if m[i, j] in (0, 4) else "black")
    ax.set_xticks(range(len(AXES)), AXES)
    ax.set_yticks(range(len(labels)), labels)
    ax.set_xticks([x - 0.5 for x in range(1, len(AXES))], minor=True)
    ax.set_yticks([y - 0.5 for y in range(1, len(labels))], minor=True)
    ax.grid(which="minor", color="white", lw=1.5)
    ax.tick_params(which="minor", length=0)
    cb = fig.colorbar(im, ax=ax, ticks=range(5), fraction=0.04)
    cb.ax.set_yticklabels(["0 interventionist", "1", "2", "3", "4 LIO pole"])
    ax.set_title("The 9 sourced belief-system drafts on the v8 LIO axes\n"
                 "cell = score (certainty); grey hatched = TODO", fontsize=11)
    footer(fig, "Source: systems/*.md, lio_axes (v8 coder drafts, unreviewed; not the v7.1 rubric). "
             "The other 68 systems are stubs.")
    fig.tight_layout(rect=(0, 0.06, 1, 1))
    save(fig, out, "systems_axes.png")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(REPO, "figures"))
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    fig_list_overlap(a.out)
    fig_core_composition(a.out)
    fig_people_cause_locus(a.out)
    fig_systems_axes(a.out)


if __name__ == "__main__":
    main()
