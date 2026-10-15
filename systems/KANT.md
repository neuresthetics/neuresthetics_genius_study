---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 4
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S4 for Jason)
  model_used: Grok Bot executor agent; direct reads of the cited pages
  collected_on: 2026-10-01
  last_updated: '2026-10-15'
  change_log:
  - date: 2026-10-01
    by: scripts/make_system_stubs.py
    summary: Stub created from v7.1 data book table 4 and section 7.
  - date: 2026-10-02
    by: scripts/make_system_stubs.py
    summary: 'Decision P7: E_scope note added. E is not scored in a stub; when it is, score it on the world''s order (same rules for every kind of being and event, no in-group exceptions in this-world events). Salvation and moral community go on C_ledger.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'Draft (systems batch S4): filled from SEP "Immanuel Kant" (Rohlf) and "Kant’s Philosophy of Religion" (Pasternack and Fugate). A 1 (0.5), B 3 (0.5), C BELOW_THRESHOLD (alt 1), D 3 (0.5), E UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S4 audit (WEAKEN #2): A_locus 1 (0.5) → 0 (0.5), alternative 1; miracle quote labelled ''SEP, reporting AK 6:52''; note that the architect limit is on theoretical proof only. Stance kept.'
identity:
  id: KANT
  v7_1_number: 22
  v7_1_label: Kantianism
  display_label: Kantianism
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: philosophical school or method
    certainty: 0.7
    cites:
    - source: S2
      locator: introduction
    how_known: Kant 'is the central figure in modern philosophy'. Coder's classification, 0.7.
  family:
    value: TODO
  parent_traditions:
    value: TODO
  related_codes: []
origins:
  founding_era:
    value: Late eighteenth century (Kant, 1724–1804)
    certainty: 1.0
    cites:
    - source: S2
      locator: introduction
    how_known: SEP.
  founding_region:
    value: Königsberg, Prussia
    certainty: 0.7
    cites:
    - source: S2
      locator: §1
    how_known: SEP life section; 0.7.
  founders_or_key_figures:
    value:
    - Immanuel Kant
    certainty: 1.0
    cites:
    - source: S2
      locator: introduction
    how_known: SEP.
  key_texts:
  - value: Critique of Pure Reason
    author: Immanuel Kant
    certainty: 1.0
    cites:
    - source: S1
      locator: §3
    how_known: SEP.
  - value: Religion within the Boundaries of Mere Reason
    author: Immanuel Kant
    certainty: 1.0
    cites:
    - source: S1
      locator: overview
    how_known: SEP.
metaphysics:
  god_nature_relation:
    value: God as a postulate of practical reason, rooted in the highest good; theoretically, the design argument reaches 'an architect of the world' but not an infinite creator.
    stance: creator distinct from creation
    certainty: 1.0
    cites:
    - source: S1
      locator: §3.4–3.5
    how_known: SEP.
    note: The 'architect of the world' limit applies to the theoretical proof only (Kant rejects the step from a 'Wise Author of Nature' to an infinite creator); the practical postulate is of a moral author of the world (S4 audit RQ2).
  deity_personal:
    value: TODO
    stance: TODO
  intervention:
    value: TODO
    stance: TODO
  miracles:
    value: 'SEP, reporting AK 6:52: reason ''does not contest the possibility or actuality'' of miracles (and grace, mysteries); ''it just cannot incorporate them into its maxims of thought or action''.'
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: Religion, part 1
    how_known: SEP.
  petition_and_prayer:
    value: TODO
    stance: TODO
  afterlife:
    value: TODO
    stance: TODO
  moral_ledger:
    value: TODO
    stance: TODO
  authority:
    value: '''human reason gives itself the moral law, which is our basis for belief in God, freedom, and immortality''.'
    stance: both, reason first
    certainty: 1.0
    cites:
    - source: S2
      locator: introduction
    how_known: SEP.
  reserved_exemptions:
    value: TODO
    stance: TODO
  teleology_in_nature:
    value: TODO
    stance: TODO
  necessity_and_freedom:
    value: TODO
lio_axes:
  A_locus:
    value: 0
    rationale: God postulated by practical reason as a transcendent, personal moral author of the world; the study scores that pattern A 0 (as Locke, Bacon, Boyle).
    certainty: 0.5
    cites:
    - source: S1
      locator: §3.5.1
    - source: S2
      locator: introduction
    how_known: '0.5: God here is a practical postulate, not knowledge, and personhood is the coder''s reading. Alternative 1. Changed from 1 (0.5) after the S4 audit.'
    alternatives:
    - value: 1
      note: Thinly personal moral author.
      cites:
      - source: S1
        locator: §3.5.1
  B_cause:
    value: 3
    rationale: 'Miracles are not contested but cannot enter the maxims of thought or action: nature is treated as lawful.'
    certainty: 0.5
    cites:
    - source: S1
      locator: Religion, part 1
    how_known: '0.5: inferred from SEP, reporting AK 6:52.'
  C_ledger:
    value: BELOW_THRESHOLD
    how_known: The postulates of God and immortality are rooted in the highest good (S1 §3.4–3.5); SEP excerpts read do not state the proportion of happiness to virtue.
    note: 'Alternative: 1 (God secures the highest good).'
    alternatives:
    - value: 1
      note: Named alternative.
      cites:
      - source: S1
        locator: §3.4
  D_authority:
    value: 3
    rationale: 'Reason first: religion within the boundaries of mere reason; revelation treated, but reason gives the moral law that grounds belief in God.'
    certainty: 0.5
    cites:
    - source: S2
      locator: introduction
    - source: S1
      locator: overview
    how_known: Stance label both, reason first; 0.5.
  E_scope:
    value: UNKNOWN
    how_known: Not addressed in the sources read.
epistemology:
  value: TODO
ethics:
  value: TODO
practice:
  ritual_and_practice:
    value: TODO
  community_form:
    value: TODO
science:
  historical_stance:
    value: TODO
  current_stance:
    value: TODO
schools_and_variants: []
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: TODO
v7_1_rubric:
  label: authorial v7.1 scores
  L: 9
  P: 9
  E: 9
  V: 10
  X: 8
  total: 45
  scoring_note: Kantianism scores high for its logical rigor and emphasis on universal duty, providing a foundational deontological framework, though slightly limited by abstraction from real-world variability.
  source: v7.1 data book, section 6 table (tables[4]) row 22 and section 7 scoring notes
revised_rubric:
  status: not started
  L:
    score: TODO
    rationale: ''
  P:
    score: TODO
    rationale: ''
  E:
    score: TODO
    rationale: ''
  V:
    score: TODO
    rationale: ''
  X:
    score: TODO
    rationale: ''
coding_guidance:
  use_when: Kant (founders rule), or a person whose own writing adopts the Critical philosophy and the moral postulates.
  do_not_use_when: Kantian ethics alone (categorical imperative) without the religion of reason; check DEISM for a natural-religion creed.
  neighbors: []
review:
  data_quality_flags: []
  open_questions:
  - 'C: SEP passage on happiness proportioned to virtue not yet quoted.'
  - Kant's person record should now be re-checked against this file (primary_system BELOW_THRESHOLD cited the stub).
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Lawrence Pasternack; Courtney Fugate
  year: 2025
  citation: Lawrence Pasternack and Courtney Fugate. "Kant’s Philosophy of Religion." Stanford Encyclopedia of Philosophy. First published June 22, 2004; substantive revision October 13, 2025. https://plato.stanford.edu/entries/kant-religion/.
  url: https://plato.stanford.edu/entries/kant-religion/
  accessed: '2026-10-15'
  reliability_note: Peer-reviewed reference entry.
- id: S2
  type: tertiary
  kind: encyclopedia
  author: Michael Rohlf
  year: 2024
  citation: Michael Rohlf. "Immanuel Kant." Stanford Encyclopedia of Philosophy. First published May 20, 2010; substantive revision July 31, 2024. https://plato.stanford.edu/entries/kant/.
  url: https://plato.stanford.edu/entries/kant/
  accessed: '2026-10-15'
  reliability_note: Peer-reviewed reference entry.
---

# Kantianism (KANT)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44. The v7.1 scores and note are unchanged.

## Summary

Kant 'synthesized early modern rationalism and empiricism' [S2]. On his view 'human reason gives itself the moral law, which is our basis for belief in God, freedom, and immortality' [S2]. 'Kant has long been seen as hostile to religion', which SEP says belies his positive philosophy of religion [S1].

## Core metaphysics

Transcendental idealism [S2]; God and immortality as postulates of practical reason [S1, §3.5].

## Position on the LIO axes

- A 0 (0.5, alt 1), B 3 (0.5), D 3 (0.5).
- C BELOW_THRESHOLD (alt 1).
- E UNKNOWN.

## Schools and variants

TODO

## Science

TODO

## Coding guidance

Kant by the founders rule.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> KANT (45/50) — Kantianism. Kantianism scores high for its logical rigor and emphasis on universal duty, providing a foundational deontological framework, though slightly limited by abstraction from real-world variability.

## Open questions

- C quote.
- Re-check the Kant person record.
- Adherents are TODO.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7 (score E on the world's order when the stub is filled).
- 2026-10-15 (systems batch S4): read the listed sources; quotations checked word for word against the fetched page text with a script. Axes under P44.
- 2026-10-15 (S4 audit fixes, run 1: 11 HOLD, 1 WEAKEN): A 0 (0.5, alt 1); miracle quote labelled SEP, reporting AK 6:52; architect-limit note.
