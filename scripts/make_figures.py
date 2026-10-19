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
from lib.records import (REPO, read_record, read_csv, person_files, people_axis_points, P43_PEOPLE, short_label)  # noqa: E402

FOOTER = "Genius Study v8.0-alpha · descriptive only, no results"
MODELS = ["Claude", "DeepSeek", "Gemini", "GPT", "Grok"]
LIST_FILES = {"Claude": "geniiClaude.csv", "DeepSeek": "geniiDeepSeek.csv", "Gemini": "geniiGemini.csv",
              "GPT": "geniiGPT.csv", "Grok": "geniiGrok.csv"}
SOURCED_SYSTEMS = ["CLASS_THEISM", "CLTHEI", "CHRIST", "ISLAM", "JUDA", "DEISM", "STOIC", "PLATO", "PANT",
                   "ATHE", "AGNOS", "BRGHTS", "EMPIR", "ETHCUL", "RATN",
                   "SECHUM", "SUNASM", "PRAG", "ARIST", "EFFALT", "TRNSHM",
                   "ABSURD", "CYNIC", "EPICUR", "EXIST", "NIHIL", "OBJCT",
                   "SCEPT", "KANT", "PHENOM", "UTIL",
                   "PANDEI", "PANEND", "BUDDH", "JAIN", "SOLIP",
                   "BAHAI", "ANIM", "CAODAI", "CHNFOLK", "HYLO", "CONFUC",
                   "SHINTO", "TAO", "HINDU", "HEATH", "HELLEN", "KEMET",
                   "RODNOV", "WICCA", "ABORIG", "BON", "NATAM", "SANTER",
                   "VODUN", "ANTHRO", "CHAOSM", "HERMET", "SIKH",
                   "THEOS", "DRUZE", "MANDAE", "YAZID", "ZORO", "MORMON",
                   "THSAT", "THELEM", "FALUNG", "RAEL", "SCIENT",
                   "DETERM", "LVSAT", "PANENT", "HEDON", "PANPSY", "IDEAL"]
AXES = ["A_locus", "B_cause", "C_ledger", "D_authority", "E_scope"]
DPI = 170


# Label layout ---------------------------------------------------------------
from matplotlib.font_manager import FontProperties  # noqa: E402
from matplotlib.textpath import TextToPath  # noqa: E402

_T2P = TextToPath()


def text_width_in(label, fs, bold=False):
    """Width of a label in inches at font size fs (points)."""
    prop = FontProperties(size=fs, weight="bold" if bold else "normal")
    w, _, _ = _T2P.get_text_width_height_descent(label, prop, ismath=False)
    return w / 72.0


def fit_cell(labels, cell_w, cell_h, fs_max, fs_min=7.5, dot_gap=0.05, head=(), max_cols=4, bold_head=True,
             line=1.45, usable_w=0.92, usable_h=0.84, pad=0.08):
    """Pick (ncols, fs) for one grid cell so that no label overlaps its neighbour.
    cell_w, cell_h: the cell's size in inches. labels fill columns below `head` labels, which take full-width rows.
    Prefers the largest font, then the fewest columns. dot_gap is the dot-to-text offset and pad the clear space
    before the next column's marker, both in cell units."""
    n = len(labels)
    fs = fs_max
    while fs >= fs_min - 1e-9:
        rowh = fs * line / 72.0 / cell_h                    # one text line, in cell units
        ok = []
        for ncols in range(1, max_cols + 1):
            if n == 0 and ncols > 1:
                break
            nrows = len(head) + (math.ceil(n / ncols) if n else 0)
            if nrows * rowh > usable_h:
                continue
            colw = usable_w / ncols
            wide = max((text_width_in(t, fs) / cell_w for t in labels), default=0)
            hw = max((text_width_in(t, fs, bold_head) / cell_w for t in head), default=0)
            if dot_gap + wide + pad <= colw and dot_gap + hw <= usable_w:
                ok.append((ncols, nrows))
        if ok:
            # Largest font first; then the fewest columns that keep a cell to about six rows.
            short = [c for c, r in ok if r <= 6]
            return (short[0] if short else ok[0][0]), fs
        fs -= 0.5
    return max_cols, fs_min


def report_overlaps(fig, name):
    """Print any overlapping label boxes (labels against labels and against markers). Used to check the charts."""
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    boxes = []
    for ax in fig.axes:
        for t in ax.texts:
            if t.get_text().strip():
                boxes.append(("text", t.get_text(), t.get_window_extent(r)))
        for c in ax.collections:
            sizes = c.get_sizes()
            for k, (x, y) in enumerate(c.get_offsets()):
                px, py = c.get_offset_transform().transform((x, y))
                area = sizes[k % len(sizes)] if len(sizes) else 36
                rad = math.sqrt(area) / 2 * fig.dpi / 72.0
                from matplotlib.transforms import Bbox
                boxes.append(("dot", "", Bbox([[px - rad, py - rad], [px + rad, py + rad]])))
    hits = []
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            a, b = boxes[i], boxes[j]
            if a[0] == "dot" and b[0] == "dot":
                continue
            if a[2].overlaps(b[2]):
                ov = min(a[2].x1, b[2].x1) - max(a[2].x0, b[2].x0), min(a[2].y1, b[2].y1) - max(a[2].y0, b[2].y0)
                if ov[0] > 1 and ov[1] > 1:
                    hits.append((a[1] or "<dot>", b[1] or "<dot>"))
    print(f"{name}: {len(hits)} label overlaps" + (": " + "; ".join(f"{x} / {y}" for x, y in hits[:20]) if hits else ""))
    return hits


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
    """Surnames sit next to their dots on a 5x5 grid. No region is shaded or labeled (Jason, 2026-10-08).
    Full 0-4 range on both axes. People come from people_axis_points(), not a hardcoded list."""
    # Plain words for the 0-4 scale (CODING_GUIDE §6: 0 pole, 1 leans, 2 mixed, 3 leans other pole with a stated exception, 4 pole)
    y_labels = ["A person outside\nthe world", "Mostly a person\noutside the world", "Mixed",
                "Mostly the order\nof nature", "The order of nature\nitself (or no\nseparate God)"]
    x_labels = ["Miracles /\nintervention", "Mostly\nintervention", "Mixed",
                "Lawful, with a stated\nexception", "Lawful, no\nexceptions"]
    dot = "#3B6AA0"

    def label(p):
        return short_label(p["name"]) + ("*" if p["name"] in P43_PEOPLE else "")

    pts, not_scorable = people_axis_points()
    cells = collections.defaultdict(list)
    for p in pts:
        cells[(p["B"], p["A"])].append(p)

    W, H = 18, 13
    AX = (0.14, 0.12, 0.84, 0.74)
    fig = plt.figure(figsize=(W, H))
    ax = fig.add_axes(AX)
    ax.set_xlim(-0.5, 4.5)
    ax.set_ylim(-0.5, 4.5)
    cell_w, cell_h = W * AX[2] / 5, H * AX[3] / 5

    # Cells: a small grid of dots, surname to the right of each dot. Columns and font size are fitted per cell
    # (fit_cell) so that no label runs into the next column or row.
    for (b, a), ps in cells.items():
        ps = sorted(ps, key=label)
        labs = [label(p) for p in ps]
        n = len(ps)
        ncols, fs = fit_cell(labs, cell_w, cell_h, fs_max=12, dot_gap=0.05, max_cols=3)
        nrows = math.ceil(n / ncols)
        colw = 0.92 / ncols
        rowh = min(0.24, 0.8 / max(nrows - 1, 1))
        for i, p in enumerate(ps):
            c, r = divmod(i, nrows)  # fill down each column first
            x = b - 0.44 + c * colw
            y = a + (nrows - 1) / 2 * rowh - r * rowh
            cert = min(p["cA"], p["cB"])
            faded = cert < 0.7
            ax.scatter(x, y, s=120, color=dot, alpha=0.28 if faded else 0.95,
                       edgecolor="#999999" if faded else "black", lw=0.8, zorder=3)
            ax.text(x + 0.05, y, labs[i], ha="left", va="center", fontsize=fs,
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

    fig.text(0.5, 0.955, "Where coded people fall: where God is vs. how things happen",
             ha="center", fontsize=20, fontweight="bold")
    fig.text(0.5, 0.925, f"Draft scores for the {len(pts)} hand-picked people with both axes scored; not a sample, not a result."
             + (f"\n{len(not_scorable)} more coded people are not scorable yet (an axis is UNKNOWN or below threshold) "
                "and are not shown or counted." if not_scorable else ""),
             ha="center", va="top", fontsize=13.5, color="#444444")
    leg = [Line2D([0], [0], marker="o", ls="", markersize=10, markerfacecolor=dot, markeredgecolor="black", alpha=0.95),
           Line2D([0], [0], marker="o", ls="", markersize=10, markerfacecolor=dot, markeredgecolor="#999999", alpha=0.28)]
    names = ["score as drafted", "faded = less certain score"]
    if any(p["name"] in P43_PEOPLE for p in pts):
        leg.append(Line2D([0], [0], ls="", marker=""))
        names.append("* = disputed interview wording\n   (Craft books), capped at 0.5 (P43)")
    ax.legend(leg, names, loc="upper left", fontsize=11,
              frameon=True, framealpha=0.95, edgecolor="#DDDDDD")
    fig.text(0.01, 0.012, "Source: draft person records in neuresthetics/neuresthetics_genius_study (people/), "
             "unreviewed. Genius Study v8.0-alpha, descriptive only, no results.",
             ha="left", va="bottom", fontsize=8.5, color="#888888")
    report_overlaps(fig, "people_cause_locus.png")
    save(fig, out, "people_cause_locus.png")


# 4 ------------------------------------------------------------------------
def fig_systems_axes(out):
    import numpy as np
    labels, vals, certs, labs = [], [], [], []
    for code in SOURCED_SYSTEMS:
        d, _ = read_record(os.path.join(REPO, "systems", f"{code}.md"))
        if all((n or {}).get("value") == "UNKNOWN" for n in d["lio_axes"].values()):
            continue  # P46(a): sourced, unscored; counted with the stubs
        labels.append(code)
        row, crow, lrow = [], [], []
        for k in AXES:
            node = d["lio_axes"].get(k) or {}
            v = node.get("value")
            row.append(v if isinstance(v, int) else np.nan)
            lrow.append({"BELOW_THRESHOLD": "BELOW\nTHRESH."}.get(v, str(v)))
            crow.append(node.get("certainty"))
        vals.append(row)
        certs.append(crow)
        labs.append(lrow)
    m = np.array(vals, dtype=float)
    fig, ax = plt.subplots(figsize=(9, 20))
    cmap = plt.get_cmap("RdYlBu").copy()
    cmap.set_bad("#DDDDDD")
    im = ax.imshow(np.ma.masked_invalid(m), cmap=cmap, vmin=0, vmax=4, aspect="auto")
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            if np.isnan(m[i, j]):
                ax.add_patch(Rectangle((j - 0.5, i - 0.5), 1, 1, fill=False, hatch="///", edgecolor="#888888", lw=0))
                ax.text(j, i, labs[i][j], ha="center", va="center", fontsize=7)
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
    ax.set_title(f"The {len(labels)} sourced belief-system drafts on the v8 LIO axes\n"
                 "cell = score (certainty); grey hatched = no score (TODO, UNKNOWN or BELOW_THRESHOLD)", fontsize=11)
    footer(fig, "Source: systems/*.md, lio_axes (v8 coder drafts, unreviewed; not the v7.1 rubric). "
             f"The other {sum(1 for f in os.listdir(os.path.join(REPO, 'systems')) if f.endswith('.md') and f != 'README.md') - len(labels)} systems are stubs or sourced but unscored (P46).")
    fig.tight_layout(rect=(0, 0.06, 1, 1))
    save(fig, out, "systems_axes.png")


# 5, 6 --------------------------------------------------------------------
SYS_COLOR = "#C8582A"
PEOPLE_COLOR = "#3B6AA0"
Y_LABELS = ["A person outside\nthe world", "Mostly a person\noutside the world", "Mixed",
            "Mostly the order\nof nature", "The order of nature\nitself (or no\nseparate God)"]
X_LABELS = ["Miracles /\nintervention", "Mostly\nintervention", "Mixed",
            "Lawful, with a stated\nexception", "Lawful, no\nexceptions"]


SHORT = {"CLTHEI": "Interv. theism", "CLASS_THEISM": "Classical theism", "CONFUC": "Confucianism",
         "NATAM": "Native American", "ABORIG": "Aboriginal traditions", "CHNFOLK": "Chinese folk",
         "LVSAT": "LaVeyan Satanism", "THSAT": "Theistic Satanism", "ETHCUL": "Ethical Culture",
         "SUNASM": "Sunday Assembly", "EFFALT": "Effective Altruism", "SECHUM": "Sec. humanism"}


def sys_name(code, d):
    if code in SHORT:
        return SHORT[code]
    lab = d["identity"]["display_label"].split(" (")[0].strip()
    return lab if len(lab) <= 22 else code


def system_axis_points():
    """Sort the sourced systems by what is settled on B_cause (x) and A_locus (y).
    grid: both numeric; a_only: A numeric, B not; b_only: B numeric, A not; neither: the rest (incl. sourced, unscored).
    Stubs are left out."""
    grid, a_only, b_only, neither, unscored, stubs = [], [], [], [], [], []
    for f in sorted(os.listdir(os.path.join(REPO, "systems"))):
        if not f.endswith(".md") or f == "README.md":
            continue
        code = f[:-3]
        d, _ = read_record(os.path.join(REPO, "systems", f))
        if d["record"]["review_status"] == "stub":
            stubs.append(code)
            continue
        A, B = d["lio_axes"]["A_locus"], d["lio_axes"]["B_cause"]
        a, b = A.get("value"), B.get("value")
        it = {"code": code, "label": sys_name(code, d), "A": a, "B": b, "kind": "system"}
        if all(value(n) == "UNKNOWN" for n in d["lio_axes"].values()):
            unscored.append(it)
        elif isinstance(a, int) and isinstance(b, int):
            it["faded"] = min(A.get("certainty") or 0, B.get("certainty") or 0) < 0.7
            grid.append(it)
        elif isinstance(a, int):
            it["faded"] = (A.get("certainty") or 0) < 0.7
            a_only.append(it)
        elif isinstance(b, int):
            it["faded"] = (B.get("certainty") or 0) < 0.7
            b_only.append(it)
        else:
            neither.append(it)
    return grid, a_only, b_only, neither, unscored, stubs


def _style(it):
    sysm = it["kind"] == "system"
    f = it.get("faded")
    col = SYS_COLOR if sysm else PEOPLE_COLOR
    tcol = ("#B08A7A" if sysm else "#777777") if f else ("#7A2E10" if sysm else "#111111")
    return sysm, f, col, tcol


def _mark(ax, x, y, it, fs):
    sysm, f, col, tcol = _style(it)
    # Shrink markers with the font in crowded cells so that stacked diamonds and dots do not touch.
    size = min(110 if sysm else 95, (fs * (0.95 if sysm else 1.1)) ** 2)
    ax.scatter(x, y, s=size, marker="D" if sysm else "o", color=col, alpha=0.30 if f else 0.95,
               edgecolor="#999999" if f else "black", lw=0.8, zorder=3, clip_on=False)
    ax.text(x + 0.045, y, it["label"], ha="left", va="center", fontsize=fs, fontweight="bold" if sysm else "normal",
            color=tcol, zorder=4, clip_on=False)


def _draw_cells(ax, items):
    """Systems take full-width rows at the top of a cell; people fill columns below. Columns and font size are
    fitted per cell (fit_cell) from the axes' size so that labels do not overlap."""
    fig = ax.figure
    bb = ax.get_position()
    cell_w = fig.get_figwidth() * bb.width / 5
    cell_h = fig.get_figheight() * bb.height / 5
    cells = collections.defaultdict(list)
    for it in items:
        cells[(it["B"], it["A"])].append(it)
    for (b, a), its in cells.items():
        syss = sorted([i for i in its if i["kind"] == "system"], key=lambda i: i["label"])
        ppl = sorted([i for i in its if i["kind"] != "system"], key=lambda i: i["label"])
        ncols, fs = fit_cell([i["label"] for i in ppl], cell_w, cell_h, fs_max=10, fs_min=7,
                             dot_gap=0.045, head=[i["label"] for i in syss], max_cols=3, line=1.4)
        prow = math.ceil(len(ppl) / ncols) if ppl else 0
        nrows = len(syss) + prow
        rowh = min(0.2, 0.8 / max(nrows - 1, 1))
        top = a + (nrows - 1) / 2 * rowh
        colw = 0.92 / ncols
        for i, it in enumerate(syss):
            _mark(ax, b - 0.44, top - i * rowh, it, fs)
        for i, it in enumerate(ppl):
            c, r = divmod(i, prow)
            _mark(ax, b - 0.44 + c * colw, top - (len(syss) + r) * rowh, it, fs)


def _layout(fig):
    L, R, BOT, TOP = 0.30, 0.79, 0.25, 0.86     # main grid
    ax = fig.add_axes((L, BOT, R - L, TOP - BOT))
    left = fig.add_axes((0.155, BOT, 0.13, TOP - BOT), sharey=ax)
    bot = fig.add_axes((L, 0.065, R - L, 0.155), sharex=ax)
    box = fig.add_axes((0.81, 0.065, 0.18, TOP - 0.065))
    ax.set_xlim(-0.5, 4.5)
    ax.set_ylim(-0.5, 4.5)
    for a in (ax, left, bot):
        a.tick_params(which="both", length=0, pad=6)
        a.grid(which="major", visible=False)
    ax.set_xticks([k + 0.5 for k in range(4)], minor=True)
    ax.set_yticks([k + 0.5 for k in range(4)], minor=True)
    ax.grid(which="minor", color="#DDDDDD", lw=1)
    ax.tick_params(labelbottom=False, labelleft=False)
    for sp in ax.spines.values():
        sp.set_color("#BBBBBB")
    left.set_xlim(0, 1)
    left.set_xticks([])
    left.set_yticks(range(5), Y_LABELS, fontsize=10.5)
    left.set_ylabel("Where is God?", fontsize=14, labelpad=10)
    bot.set_ylim(0, 1)
    bot.set_yticks([])
    bot.set_xticks(range(5), X_LABELS, fontsize=10.5)
    bot.set_xlabel("How do things happen?", fontsize=14, labelpad=8)
    for a, title in ((left, "how things happen:\nnot settled"), (bot, "where God is: not settled")):
        a.set_facecolor("#F4F1EC")
        for sp in a.spines.values():
            sp.set_color("#999999")
            sp.set_linestyle((0, (3, 2)))
    left.set_title("how things happen:\nnot settled", fontsize=10.5, color="#555555", style="italic", pad=6)
    bot.text(-0.48, 0.97, "where God is: not settled", ha="left", va="top", fontsize=10.5, color="#555555", style="italic")
    for k in [k + 0.5 for k in range(4)]:
        left.axhline(k, color="#DDDDDD", lw=1)
        bot.axvline(k, color="#DDDDDD", lw=1)
    box.set_axis_off()
    return ax, left, bot, box


def _draw_strips(left, bot, a_only, b_only):
    rows = collections.defaultdict(list)
    for it in a_only:
        rows[it["A"]].append(it)
    for a, its in rows.items():
        its = sorted(its, key=lambda i: i["label"])
        n = len(its)
        rowh = min(0.19, 0.8 / max(n - 1, 1))
        for i, it in enumerate(its):
            _mark(left, 0.07, a + (n - 1) / 2 * rowh - i * rowh, it, 9.5)
    cols = collections.defaultdict(list)
    for it in b_only:
        cols[it["B"]].append(it)
    for b, its in cols.items():
        its = sorted(its, key=lambda i: i["label"])
        n = len(its)
        rowh = min(0.16, 0.72 / max(n - 1, 1))
        for i, it in enumerate(its):
            _mark(bot, b - 0.43, 0.45 + (n - 1) / 2 * rowh - i * rowh, it, 9)


def _draw_box(box, neither, unscored, stubs):
    box.add_patch(Rectangle((0, 0), 1, 1, transform=box.transAxes, facecolor="#F4F1EC", edgecolor="#999999",
                            ls=(0, (3, 2)), lw=1))
    lines = ["neither axis settled"]
    y = 0.975
    box.text(0.05, y, lines[0], ha="left", va="top", fontsize=11, color="#555555", style="italic", transform=box.transAxes)
    y -= 0.04
    for it in sorted(neither, key=lambda i: i["label"]):
        box.text(0.07, y, "◇ " + it["label"], ha="left", va="top", fontsize=9.5, color="#7A2E10", fontweight="bold",
                 transform=box.transAxes)
        y -= 0.026
    y -= 0.015
    box.text(0.05, y, "sourced, no axis scored", ha="left", va="top", fontsize=10, color="#555555", style="italic",
             transform=box.transAxes)
    y -= 0.034
    for it in sorted(unscored, key=lambda i: i["label"]):
        box.text(0.07, y, "◇ " + it["label"], ha="left", va="top", fontsize=9.5, color="#B08A7A", transform=box.transAxes)
        y -= 0.026
    if stubs:
        y -= 0.015
        box.text(0.05, y, f"not shown, stub: {', '.join(stubs)}", ha="left", va="top", fontsize=8.5, color="#888888",
                 transform=box.transAxes)


def _legend(ax, people=False):
    leg = [Line2D([0], [0], marker="D", ls="", markersize=9, markerfacecolor=SYS_COLOR, markeredgecolor="black", alpha=0.95),
           Line2D([0], [0], marker="D", ls="", markersize=9, markerfacecolor=SYS_COLOR, markeredgecolor="#999999", alpha=0.30)]
    names = ["belief system", "faded = capped at 0.5"]
    if people:
        leg.insert(0, Line2D([0], [0], marker="o", ls="", markersize=9, markerfacecolor=PEOPLE_COLOR, markeredgecolor="black"))
        names = ["person", "belief system", "faded = less certain (people < 0.7;\nsystems capped at 0.5)"]
    return leg, names


def fig_systems_cause_locus(out):
    grid, a_only, b_only, neither, unscored, stubs = system_axis_points()
    fig = plt.figure(figsize=(18, 12.5))
    ax, left, bot, box = _layout(fig)
    _draw_cells(ax, grid)
    _draw_strips(left, bot, a_only, b_only)
    _draw_box(box, neither, unscored, stubs)
    n = len(grid) + len(a_only) + len(b_only) + len(neither) + len(unscored)
    fig.text(0.5, 0.965, "Where coded belief systems fall: where God is vs. how things happen",
             ha="center", fontsize=20, fontweight="bold")
    fig.text(0.5, 0.932, f"All {n} sourced systems. Grid: both axes settled ({len(grid)}). Shaded strips and box: an axis not settled "
             "(unknown, or members differ).", ha="center", va="top", fontsize=12.5, color="#444444")
    leg, names = _legend(ax)
    ax.legend(leg, names, loc="upper left", fontsize=10, frameon=True, framealpha=0.95, edgecolor="#DDDDDD")
    fig.text(0.01, 0.008, "Source: draft system records (systems/*.md), unreviewed. Genius Study v8.0-alpha, descriptive only, no results.",
             ha="left", va="bottom", fontsize=8.5, color="#888888")
    report_overlaps(fig, "systems_cause_locus.png")
    save(fig, out, "systems_cause_locus.png")


def fig_people_systems_overlay(out):
    grid, a_only, b_only, neither, unscored, stubs = system_axis_points()
    pts, not_scorable = people_axis_points()
    items = [{"B": p["B"], "A": p["A"], "kind": "person", "faded": min(p["cA"], p["cB"]) < 0.7,
              "label": short_label(p["name"]) + ("*" if p["name"] in P43_PEOPLE else "")}
             for p in pts]
    fig = plt.figure(figsize=(22, 15.5))
    ax, left, bot, box = _layout(fig)
    _draw_cells(ax, items + grid)
    _draw_strips(left, bot, a_only, b_only)
    _draw_box(box, neither, unscored, stubs)
    fig.text(0.5, 0.965, "People and belief systems: where God is vs. how things happen",
             ha="center", fontsize=20, fontweight="bold")
    fig.text(0.5, 0.932, f"{len(pts)} hand-picked people (circles; not a sample) and all sourced systems (diamonds). "
             f"Strips and box: systems with an axis not settled. {len(not_scorable)} people not yet scorable are not shown.",
             ha="center", va="top", fontsize=12, color="#444444")
    leg, names = _legend(ax, people=True)
    if any(p["name"] in P43_PEOPLE for p in pts):
        leg.append(Line2D([0], [0], ls="", marker=""))
        names.append("* = disputed interview wording (P43)")
    ax.legend(leg, names, loc="upper left", fontsize=10, frameon=True, framealpha=0.95, edgecolor="#DDDDDD")
    fig.text(0.01, 0.008, "Source: draft person and system records, unreviewed. Genius Study v8.0-alpha, descriptive only, no results.",
             ha="left", va="bottom", fontsize=8.5, color="#888888")
    report_overlaps(fig, "people_systems_overlay.png")
    save(fig, out, "people_systems_overlay.png")




def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(REPO, "figures"))
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    fig_list_overlap(a.out)
    fig_core_composition(a.out)
    fig_people_cause_locus(a.out)
    fig_systems_axes(a.out)
    fig_systems_cause_locus(a.out)
    fig_people_systems_overlay(a.out)


if __name__ == "__main__":
    main()
