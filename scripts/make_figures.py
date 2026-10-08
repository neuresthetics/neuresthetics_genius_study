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
from lib.records import (REPO, read_record, read_csv, person_files, is_interview, people_axis_points,  # noqa: E402
                         in_focus, focus_counts)

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
    """Markers sit on a small grid inside their (B, A) cell, so they never overlap, and carry a number.
    Names and scores go in a key panel beside the plot (several columns if needed), so there are no
    labels on the plot that could collide. The layout cannot fail for any number of people."""
    pts, _ = people_axis_points()
    # Study-focus people (top right) come first in the numbering and the key.
    pts = sorted(pts, key=lambda p: (not in_focus(p), -p["A"], p["B"], p["name"]))
    ff, fn = focus_counts(pts)
    cells = collections.defaultdict(list)
    for k, p in enumerate(pts, 1):
        p["k"] = k
        cells[(p["B"], p["A"])].append(p)
    n_rows_key = 12
    ncols = max(1, -(-len(pts) // n_rows_key))
    W = 9.5 + 4.4 * ncols
    fig = plt.figure(figsize=(W, 8.0))
    left = 1.75 / W
    axw = 6.6 / W
    ax = fig.add_axes((left, 0.15, axw, 0.70))
    kx0 = left + axw + 0.25 / W
    FOCUS = "#DD8452"
    # Primary region: the study focus, the LIO pole on both axes.
    ax.add_patch(Rectangle((2.5, 2.5), 2, 2, facecolor=FOCUS, alpha=0.20, lw=0, zorder=0))
    ax.add_patch(Rectangle((2.5, 2.5), 2, 2, fill=False, edgecolor=FOCUS, lw=2.2, zorder=1))
    focus_h = Rectangle((0, 0), 1, 1, facecolor=FOCUS, alpha=0.35, edgecolor=FOCUS, lw=2)
    leg = ax.legend([focus_h],
                    [f"Study focus: LIO pole on both axes (A ≥ 3, B ≥ 3)\n{ff} at certainty ≥ 0.7 on both axes ({fn} plotted)"],
                    loc="upper left", fontsize=8.5, frameon=True, framealpha=0.9, edgecolor="#CCCCCC")
    leg.get_texts()[0].set_fontweight("bold")
    for (b, a), ps in cells.items():
        cols = max(1, int(-(-len(ps) ** 0.5 // 1)))
        rws = -(-len(ps) // cols)
        sp = min(0.2, 0.8 / max(cols, rws))
        size = min(150, (sp * 0.85 * 6.6 / 5 * 72) ** 2)  # marker diameter stays below the grid spacing
        for i, p in enumerate(ps):
            r, c = divmod(i, cols)
            x = b + (c - (cols - 1) / 2) * sp
            y = a - (r - (rws - 1) / 2) * sp
            cert = min(p["cA"], p["cB"])
            # Opacity follows the lower certainty, with a clear step at the 0.7 bar the regions are counted at.
            alpha = 0.3 if cert < 0.7 else 0.75 + 0.25 * (cert - 0.7) / 0.3
            ax.scatter(x, y, s=size, color="#4C72B0", alpha=alpha, edgecolor="black" if cert >= 0.7 else "#777777",
                       lw=0.6, zorder=3)
            ax.text(x, y, str(p["k"]), ha="center", va="center", fontsize=6.5, color="white" if cert >= 0.7 else "black",
                    zorder=4, fontweight="bold")
    ax.set_xlim(-0.5, 4.5)
    ax.set_ylim(-0.5, 4.5)
    ax.set_xticks(range(5), ["0\ninterventionist", "1", "2", "3", "4\nLIO pole"])
    ax.set_yticks(range(5), ["0 interventionist", "1", "2", "3", "4 LIO pole"])
    ax.set_xlabel("B_cause (0–4)")
    ax.set_ylabel("A_locus (0–4)")
    ax.grid(alpha=0.25)
    fig.suptitle(f"Study focus: who sits at the LIO pole on both axes (top right)\n"
                 f"the {len(pts)} draft person records with both axes scored, B_cause vs A_locus; "
                 "opacity = lower of the two certainties; numbers refer to the key",
                 fontsize=11, x=0.5, y=0.97)

    def tag(c, i):
        return f"{c}{' (interview)' if i else ''}"

    fig.text(kx0, 0.87, "Key (study focus first, in bold): number, name; A score @ certainty, B score @ certainty", fontsize=8.5,
             fontweight="bold", va="bottom")
    colw = (1 - kx0 - 0.01) / ncols
    texts = []
    for idx, p in enumerate(pts):
        col, row = divmod(idx, n_rows_key)
        y0 = 0.85 - row * 0.058
        texts.append(fig.text(kx0 + col * colw, y0, f"{p['k']:>2}. {p['name']}", fontsize=8, va="top",
                              fontweight="bold" if in_focus(p) else "normal"))
        texts.append(fig.text(kx0 + col * colw + 0.012, y0 - 0.024,
                              f"A {p['A']} @ {tag(p['cA'], p['iA'])}, B {p['B']} @ {tag(p['cB'], p['iB'])}",
                              fontsize=7.5, va="top", color="#333333"))
    fig.text(kx0, 0.075, "\"(interview)\" after a certainty: that axis rests on interview evidence (decision P8).",
             fontsize=7.5, va="bottom", color="#333333")
    # Shrink the key font until every line fits its column; never fails, only gets smaller.
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    limit = colw * fig.bbox.width - 6
    while max(t.get_window_extent(r).width for t in texts) > limit and texts[0].get_fontsize() > 4:
        for t in texts:
            t.set_fontsize(t.get_fontsize() - 0.5)
        fig.canvas.draw()
    footer(fig, "Source: people/**/*.md, worldview.lio_axes. Unreviewed hand-picked drafts; not a sample, "
                "no base rate, so no over- or under-representation claim.")
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
