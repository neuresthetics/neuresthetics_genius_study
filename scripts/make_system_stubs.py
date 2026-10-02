#!/usr/bin/env python3
"""
Create one stub file per belief system (systems/<CODE>.md) from the v7.1 data book.

Reads data/sources/v7_1/neuresthetics_v7_combined.json:
  documents.data_book.content.tables[4]      the 77-system rubric (#, Abbr, System, Tot, L, P, E, V, X)
  documents.data_book.content.paragraphs     section 7 "Belief systems — scoring notes", one paragraph per system
  documents.data_book.content.tables[3]      coding rules (ported into coding_guidance where a rule names a code)

Writes a stub only when systems/<CODE>.md does not exist, or exists with review_status `stub`
(so re-running never overwrites a file someone has worked on). Use --dry-run to see what it would do.

Run:  python3 scripts/make_system_stubs.py [--dry-run]
"""
import argparse, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.records import REPO, read_record

V7_JSON = os.path.join(REPO, "data", "sources", "v7_1", "neuresthetics_v7_combined.json")
OUT = os.path.join(REPO, "systems")
TODAY = "2026-10-01"
# Decision P7 (2026-10-02): every stub carries a note on how E_scope is to be scored.
P7_DATE = "2026-10-02"
P7_LOG = ("Decision P7: E_scope note added. E is not scored in a stub; when it is, score it on the world's order "
          "(same rules for every kind of being and event, no in-group exceptions in this-world events). Salvation "
          "and moral community go on C_ledger.")
P7_E_NOTE = ("Not scored (stub). When filled, score on the world's order (decision P7, 2026-10-02): the same rules "
             "for every kind of being and event, and no in-group exceptions in this-world events (fortune, protection, "
             "answered petition, miracles for the favoured). Salvation, reward and punishment, and moral community go "
             "on C_ledger. The v7.1 rubric's E column (direct empirical compatibility) is a different axis; the v7.1 "
             "scoring note below may mix domains, so recheck it against this rule.")
NOTE_RE = re.compile(r"^(?P<code>[A-Z0-9_]+) \((?P<tot>\d+)/50\) — (?P<rest>.*)$", re.S)

# Display labels that differ from v7.1, both approved on 2026-10-01 (docs/OPEN_DECISIONS.md S1, S2).
DISPLAY_LABELS = {
    "CLTHEI": "Interventionist personal theism",
    "PANT": "Pantheism (Spinozistic/naturalistic 'God = Universe')",
}
LABEL_NOTES = {
    "CLTHEI": "v7.1 used 'Classical Theism' for both CLASS_THEISM and CLTHEI. The display label keeps the code and separates the names (approved 2026-10-01, OPEN_DECISIONS S1).",
    "PANT": "The v7.1 label is cut off mid-word in both the data book table and the Word file. The display label is the full original from V6_(history)/V6/beliefCoherence.json (approved 2026-10-01, OPEN_DECISIONS S2).",
}
# Coding guidance added by decisions (docs/OPEN_DECISIONS.md S6). Appended to use_when; replaces the do_not_use_when TODO.
DECISION_GUIDANCE = {
    "ATHE": ("v8 rule (decision S6, 2026-10-01): reverent language about nature that fails the two-part PANT test is ATHE (or SECHUM if the public identity is the humanist movement). See systems/PANT.md and docs/CODING_GUIDE.md section 5.",
             "The person's own writing identifies God or the divine with Nature as a whole and gives the whole a mark beyond feeling (unity, necessity or eternity, something mind-like, or value): PANT. Explicit suspension: AGNOS. Public identity is the humanist movement: SECHUM."),
    "STOIC": ("v8 rule (decision S6, 2026-10-01): ancient Stoics, and anyone whose avowed school is Stoicism (founders rule; 'Primary = dominant working metaphysics'). SEP 'Pantheism' (Mander, rev. 2023) treats Stoic physicalism as an ancient form of pantheism, but the Stoic God is argued to be personal and providential, one 'to whom we might approach in prayer', which is not the PANT circle.",
              "A later thinker who takes the Stoic or Spinozist identity of God and Nature without the providential, prayer-hearing deity, and who passes the two-part PANT test: PANT."),
    "PANENT": ("v8 rule (decision S6, 2026-10-01): the person's own writing keeps a divine reality that includes the world but also exceeds it. v7.1's label names 'some Kabbalah/Advaita forms'; use PANENT for those only when the person's writing says this.",
               "Advaita Vedanta or Kabbalah by membership alone: code the host tradition (HINDU, JUDA) as primary. God identified with Nature as a whole, with nothing beyond it: PANT, if the two-part test is passed."),
}
# Stubs changed by a decision get record_version 2 and a second change_log entry.
DECISION_LOG = {
    "CLTHEI": "Display label approved (OPEN_DECISIONS S1); CLASS_THEISM relation changed to 'neighbor (easily confused)' (S5).",
    "CLASS_THEISM": "CLTHEI relation changed to 'neighbor (easily confused)' (OPEN_DECISIONS S5).",
    "ATHE": "Coding guidance from the PANT boundary rules (OPEN_DECISIONS S6).",
    "STOIC": "Coding guidance and PANT neighbor from the PANT boundary rules (OPEN_DECISIONS S6).",
    "PANENT": "Coding guidance and neighbors from the PANT boundary rules (OPEN_DECISIONS S6).",
}

# Coding rules from data book section 5 (tables[3]) that name a code. Quoted verbatim.
RULES = {
    "PANT": ("Pantheism", None),
    "ATHE": ("Atheism vs Agnosticism", None),
    "AGNOS": ("Atheism vs Agnosticism", None),
    "SECHUM": ("Atheism vs Agnosticism", None),
    "CLASS_THEISM": ("Split theisms", None),
    "CLTHEI": ("Split theisms", None),
    "CHRIST": ("Split theisms", "Scientists with church membership"),
    "ISLAM": ("Split theisms", None),
    "JUDA": ("Split theisms", None),
    "BUDDH": ("Founders", None),
}
NEIGHBORS = {
    "PANT": [("ATHE", "neighbor (easily confused)", "shares the no-exemption stance; differs on the entity-term (v7.1 two-lane paper, LIO section)"),
             ("PANENT", "neighbor (easily confused)", "God includes the world but also exceeds it"),
             ("PANDEI", "neighbor (easily confused)", None), ("PANPSY", "neighbor (easily confused)", None)],
    "ATHE": [("AGNOS", "neighbor (easily confused)", "explicit suspension rather than positive naturalism"),
             ("SECHUM", "neighbor (easily confused)", "public identity is the humanist movement"),
             ("PANT", "neighbor (easily confused)", "shares the no-exemption stance; differs on the entity-term")],
    "AGNOS": [("ATHE", "neighbor (easily confused)", None), ("SECHUM", "neighbor (easily confused)", None)],
    "SECHUM": [("ATHE", "neighbor (easily confused)", None), ("AGNOS", "neighbor (easily confused)", None)],
    "CLASS_THEISM": [("CLTHEI", "neighbor (easily confused)", "v7.1 coding rule: CLASS_THEISM is not CLTHEI"),
                     ("CHRIST", "neighbor (easily confused)", None), ("ISLAM", "neighbor (easily confused)", None),
                     ("JUDA", "neighbor (easily confused)", None), ("ARIST", "parent tradition", None)],
    "CLTHEI": [("CLASS_THEISM", "neighbor (easily confused)", "v7.1 coding rule: CLTHEI is not CLASS_THEISM"),
               ("CHRIST", "neighbor (easily confused)", None), ("ISLAM", "neighbor (easily confused)", None),
               ("JUDA", "neighbor (easily confused)", None)],
    "CHRIST": [("CLASS_THEISM", "neighbor (easily confused)", None), ("CLTHEI", "neighbor (easily confused)", None)],
    "ISLAM": [("CLASS_THEISM", "neighbor (easily confused)", None), ("CLTHEI", "neighbor (easily confused)", None)],
    "JUDA": [("CLASS_THEISM", "neighbor (easily confused)", None), ("CLTHEI", "neighbor (easily confused)", None)],
    "STOIC": [("PANT", "neighbor (easily confused)", "SEP: Stoic physicalism is an ancient form of pantheism; the providential Stoic God is not the PANT circle (S6)")],
    "PANENT": [("PANT", "neighbor (easily confused)", "God identified with Nature, with nothing beyond it (S6)"),
               ("HINDU", "neighbor (easily confused)", "Advaita Vedanta defaults to HINDU (S6)"),
               ("JUDA", "neighbor (easily confused)", "Kabbalah defaults to JUDA (S6)")],
}


def q(s):
    """YAML double-quoted scalar."""
    return json.dumps(s, ensure_ascii=False)


def load():
    d = json.load(open(V7_JSON, encoding="utf-8"))["documents"]["data_book"]["content"]
    hdr, *rows = d["tables"][4]
    rows = [dict(zip(hdr, r)) for r in rows]
    rules = {r[0]: r[1] for r in d["tables"][3][1:]}
    notes = {}
    paras = [p["text"] if isinstance(p, dict) else p for p in d["paragraphs"]]
    for p in paras:
        m = NOTE_RE.match(p.strip())
        if m:
            notes[m["code"]] = (int(m["tot"]), m["rest"].strip(), p.strip())
    return rows, notes, rules


def split_label(code, rest, table_label):
    """'Atheism (...). Atheism achieves ...' -> label, note. PANT's note has no separate label."""
    if code == "PANT":
        return table_label, rest
    head = table_label.rstrip("…")
    if rest.startswith(head):
        i = rest.find(". ", len(head) - 1)
        if i > 0:
            return rest[:i], rest[i + 2:]
    i = rest.find(". ")
    return rest[:i], rest[i + 2:]


TODO_TEXT = "{value: TODO}"


def stub(row, note, rules):
    code = row["Abbr"]
    tot, rest, para = note
    label, scoring = split_label(code, rest, row["System"])
    disp = DISPLAY_LABELS.get(code, label)
    status = "approved" if code in DISPLAY_LABELS else "as in v7.1"
    use_when, dont = "TODO", "TODO"
    if code in RULES:
        r1, r2 = RULES[code]
        use_when = f"v7.1 coding rule ({r1}): {rules[r1]}" + (f" Also ({r2}): {rules[r2]}" if r2 else "")
    if code == "BUDDH":
        dont = "TODO"
    if code in DECISION_GUIDANCE:
        extra, dont = DECISION_GUIDANCE[code]
        use_when = extra if use_when == "TODO" else f"{use_when} {extra}"
    neigh = NEIGHBORS.get(code, [])
    L = []
    P = L.append
    P("---")
    P("record:")
    P("  record_type: system")
    P('  schema_version: "1.1"')
    P(f"  record_version: {(2 if code in DECISION_LOG else 1) + 1}")  # +1 for the P7 note
    P("  review_status: stub")
    P("  collected_by: scripts/make_system_stubs.py")
    P("  model_used: none (ported from the v7.1 data book)")
    P(f"  collected_on: {TODAY}")
    P(f"  last_updated: {P7_DATE}")
    P("  change_log:")
    P(f"    - {{date: {TODAY}, by: scripts/make_system_stubs.py, summary: \"Stub created from v7.1 data book table 4 and section 7.\"}}")
    if code in DECISION_LOG:
        P(f"    - {{date: {TODAY}, by: scripts/make_system_stubs.py, summary: {q(DECISION_LOG[code])}}}")
    P(f"    - {{date: {P7_DATE}, by: scripts/make_system_stubs.py, summary: {q(P7_LOG)}}}")
    P("identity:")
    P(f"  id: {code}")
    P(f"  v7_1_number: {int(row['#'])}")
    P(f"  v7_1_label: {q(label)}")
    P(f"  display_label: {q(disp)}")
    P(f"  label_status: {q(status)}")
    P("  aliases: []")
    P("classification:")
    for k in ("kind", "family", "parent_traditions"):
        P(f"  {k}: {TODO_TEXT}")
    if neigh:
        P("  related_codes:")
        for c, rel, n in neigh:
            P(f"    - {{code: {c}, relation: {q(rel)}" + (f", note: {q(n)}" if n else "") + "}")
    else:
        P("  related_codes: []")
    P("origins:")
    for k in ("founding_era", "founding_region", "founders_or_key_figures"):
        P(f"  {k}: {TODO_TEXT}")
    P("  key_texts: []")
    P("metaphysics:")
    for k in ("god_nature_relation", "deity_personal", "intervention", "miracles", "petition_and_prayer", "afterlife",
              "moral_ledger", "authority", "reserved_exemptions", "teleology_in_nature"):
        P(f"  {k}: {{value: TODO, stance: TODO}}")
    P(f"  necessity_and_freedom: {TODO_TEXT}")
    P("lio_axes:")
    for k in ("A_locus", "B_cause", "C_ledger", "D_authority"):
        P(f"  {k}: {TODO_TEXT}")
    P(f"  E_scope: {{value: TODO, note: {q(P7_E_NOTE)}}}")
    P(f"epistemology: {TODO_TEXT}")
    P(f"ethics: {TODO_TEXT}")
    P("practice:")
    P(f"  ritual_and_practice: {TODO_TEXT}")
    P(f"  community_form: {TODO_TEXT}")
    P("science:")
    P(f"  historical_stance: {TODO_TEXT}")
    P(f"  current_stance: {TODO_TEXT}")
    P("schools_and_variants: []")
    P("adherents:")
    P('  use: "context only — never a genius-rate denominator"')
    P(f"  estimate: {TODO_TEXT}")
    P("v7_1_rubric:")
    P('  label: "authorial v7.1 scores"')
    for k in ("L", "P", "E", "V", "X"):
        P(f"  {k}: {int(row[k])}")
    P(f"  total: {int(row['Tot'])}")
    P(f"  scoring_note: {q(scoring)}")
    P('  source: "v7.1 data book, section 6 table (tables[4]) row ' + row['#'] + ' and section 7 scoring notes"')
    P("revised_rubric:")
    P('  status: "not started"')
    for k in ("L", "P", "E", "V", "X"):
        P(f"  {k}: {{score: TODO, rationale: \"\"}}")
    P("coding_guidance:")
    P(f"  use_when: {q(use_when)}")
    P(f"  do_not_use_when: {q(dont)}")
    if neigh:
        P("  neighbors:")
        for c, rel, n in neigh:
            P(f"    - {{code: {c}, relation: {q(rel)}}}")
    else:
        P("  neighbors: []")
    P("review:")
    flags = []
    if code in LABEL_NOTES:
        flags.append(LABEL_NOTES[code])
    if row["System"].endswith("…") and code != "PANT":
        flags.append("v7.1 table 4 label is truncated; v7_1_label is taken from the section 7 scoring note.")
    P("  data_quality_flags:" + ("" if flags else " []"))
    for f in flags:
        P(f"    - {q(f)}")
    P("  open_questions: []")
    P("sources: []")
    P("---")
    P("")
    P(f"# {disp} ({code})")
    P("")
    P("> Stub. Only the v7.1 scores and scoring note are filled in, copied from the data book. Everything else is TODO. "
      "See `docs/RUNBOOK.md` (systems) for how to fill it in.")
    P("")
    for h in ("Summary", "Core metaphysics", "Position on the LIO axes", "Schools and variants", "Science",
              "Coding guidance"):
        P(f"## {h}")
        P("")
        P("TODO")
        P("")
    P("## v7.1 scoring note")
    P("")
    P(f"Verbatim from the v7.1 data book, section 7 (authorial; not a finding):")
    P("")
    P(f"> {para}")
    P("")
    P("## Open questions")
    P("")
    P("None yet.")
    P("")
    P("## Research log")
    P("")
    P(f"- {TODAY}: stub created by `scripts/make_system_stubs.py`.")
    P(f"- {P7_DATE}: E_scope note added for decision P7 (score E on the world's order when the stub is filled).")
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    rows, notes, rules = load()
    assert len(rows) == 77, len(rows)
    missing = [r["Abbr"] for r in rows if r["Abbr"] not in notes]
    if missing:
        sys.exit(f"no section 7 note for {missing}")
    os.makedirs(OUT, exist_ok=True)
    wrote = kept = 0
    for r in rows:
        path = os.path.join(OUT, f"{r['Abbr']}.md")
        if os.path.exists(path):
            try:
                data, _ = read_record(path)
                if (data.get("record") or {}).get("review_status") != "stub":
                    kept += 1
                    continue
            except Exception:
                kept += 1
                continue
        if not a.dry_run:
            open(path, "w", encoding="utf-8").write(stub(r, notes[r["Abbr"]], rules))
        wrote += 1
    print(f"{'would write' if a.dry_run else 'wrote'} {wrote} stubs; kept {kept} non-stub files")


if __name__ == "__main__":
    main()
