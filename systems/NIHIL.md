---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 3
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S3 for Jason)
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
    summary: 'Draft (systems batch S3): filled from IEP "Nihilism" (Pratt). A BELOW_THRESHOLD (alt 4); others UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
identity:
  id: NIHIL
  v7_1_number: 18
  v7_1_label: Nihilism
  display_label: Nihilism
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: family of positions
    certainty: 0.7
    cites:
    - source: S1
      locator: introduction
    how_known: '''few philosophers would claim to be nihilists''. 0.7.'
  family:
    value: TODO
  parent_traditions:
    value: TODO
  related_codes: []
origins:
  founding_era:
    value: TODO
  founding_region:
    value: TODO
  founders_or_key_figures:
    value:
    - Friedrich Nietzsche
    certainty: 0.7
    cites:
    - source: S1
      locator: introduction
    how_known: 'IEP: most often associated with Nietzsche, who diagnosed it rather than embraced it. 0.7.'
  key_texts: []
metaphysics:
  god_nature_relation:
    value: 'Not addressed directly: ''A true nihilist would believe in nothing''; Nietzsche argued its effects would ''destroy all moral, religious, and metaphysical convictions''.'
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: IEP.
  deity_personal:
    value: TODO
    stance: TODO
  intervention:
    value: TODO
    stance: TODO
  miracles:
    value: TODO
    stance: TODO
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
    value: TODO
    stance: TODO
  reserved_exemptions:
    value: TODO
    stance: TODO
  teleology_in_nature:
    value: '''cosmic purposelessness''.'
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: introduction
    how_known: IEP names it a nihilistic theme. 0.7.
  necessity_and_freedom:
    value: TODO
lio_axes:
  A_locus:
    value: BELOW_THRESHOLD
    how_known: '''A true nihilist would believe in nothing'' (S1) implies no God, but the source states no position on God (P44b).'
    note: 'Evidence: S1.'
    alternatives:
    - value: 4
      note: Named alternative.
      cites:
      - source: S1
        locator: introduction
  B_cause:
    value: UNKNOWN
    how_known: Not addressed in the sources read.
  C_ledger:
    value: UNKNOWN
    how_known: Not addressed in the sources read.
  D_authority:
    value: UNKNOWN
    how_known: Nihilism holds 'that nothing can be known' (S1), so neither revelation nor observation is an authority; the axis is not fixed.
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
  E: 10
  V: 10
  X: 8
  total: 46
  scoring_note: Nihilism provides a stark, evidence-based critique of meaning, with high coherence in its rejection.
  source: v7.1 data book, section 6 table (tables[4]) row 18 and section 7 scoring notes
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
  use_when: The person's own writing affirms that all values are baseless (nihilism as held, not diagnosed).
  do_not_use_when: Do not code Nietzsche or others who diagnose nihilism as NIHIL.
  neighbors: []
review:
  data_quality_flags: []
  open_questions:
  - D for a stance that denies knowledge (UNKNOWN used).
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Alan Pratt
  citation: Alan Pratt. "Nihilism." Internet Encyclopedia of Philosophy. https://iep.utm.edu/nihilism/.
  url: https://iep.utm.edu/nihilism/
  accessed: '2026-10-15'
  reliability_note: Peer-reviewed reference entry; undated page.
---

# Nihilism (NIHIL)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44. The v7.1 scores and note are unchanged.

## Summary

'Nihilism is the belief that all values are baseless and that nothing can be known or communicated' [S1]. It is 'most often associated with Friedrich Nietzsche' [S1].

## Core metaphysics

Nothing believed; cosmic purposelessness [S1].

## Position on the LIO axes

- A BELOW_THRESHOLD (alt 4).
- B to E UNKNOWN.

## Schools and variants

TODO

## Science

TODO

## Coding guidance

Held, not diagnosed, nihilism.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> NIHIL (46/50) — Nihilism. Nihilism provides a stark, evidence-based critique of meaning, with high coherence in its rejection.

## Open questions

- D for a stance that denies knowledge.
- Adherents are TODO.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7 (score E on the world's order when the stub is filled).
- 2026-10-15 (systems batch S3): read the listed sources; quotations checked word for word against the fetched page text with a script. Axes under P44.
