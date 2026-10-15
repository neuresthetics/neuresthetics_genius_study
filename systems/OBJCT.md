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
    summary: 'Draft (systems batch S3): filled from SEP "Ayn Rand" (Badhwar and Long). A BELOW_THRESHOLD (alt 4); D 4 (0.5); others UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
identity:
  id: OBJCT
  v7_1_number: 19
  v7_1_label: Objectivism (Ayn Rand's philosophy)
  display_label: Objectivism (Ayn Rand's philosophy)
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: philosophical school or method
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction; §1.3
    how_known: Rand 'outlined a comprehensive philosophy' named 'Objectivism'.
  family:
    value: TODO
  parent_traditions:
    value: TODO
  related_codes: []
origins:
  founding_era:
    value: Mid-twentieth century (Atlas Shrugged 1957; an organised following by 1958)
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: SEP.
  founding_region:
    value: United States
    certainty: 0.7
    cites:
    - source: S1
      locator: §1
    how_known: Coder's gloss, 0.7.
  founders_or_key_figures:
    value:
    - Ayn Rand
    - Nathaniel Branden
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: SEP.
  key_texts: []
metaphysics:
  god_nature_relation:
    value: TODO
    stance: TODO
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
    value: 'Reason: ''reason is the chief indispensable human tool of survival''; sacrifice ''for the sake of the supernatural'' is what she calls mysticism.'
    stance: observation and reason
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
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
    value: BELOW_THRESHOLD
    how_known: SEP reports Rand rejecting sacrifice for the supernatural (mysticism) but quotes no denial of God.
    note: 'Evidence: S1 §2.'
    alternatives:
    - value: 4
      note: Named alternative.
      cites:
      - source: S1
        locator: §2
  B_cause:
    value: UNKNOWN
    how_known: Not addressed in the sources read.
  C_ledger:
    value: UNKNOWN
    how_known: Not addressed in the sources read.
  D_authority:
    value: 4
    rationale: Reason the chief human tool; the supernatural rejected as mysticism.
    certainty: 0.5
    cites:
    - source: S1
      locator: §2
    how_known: Fixed by the stance; revelation not named, 0.5.
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
  scoring_note: Objectivism scores high for its rational, integrated approach to reality and ethics, promoting individualism with strong empirical ties, but slightly limited by its prescriptive economic views.
  source: v7.1 data book, section 6 table (tables[4]) row 19 and section 7 scoring notes
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
  use_when: The person avowed Objectivism or Rand's philosophy.
  do_not_use_when: Libertarian politics alone is not OBJCT.
  neighbors: []
review:
  data_quality_flags: []
  open_questions:
  - A source for Rand's atheism (her own writing).
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Neera K. Badhwar; Roderick T. Long
  year: 2020
  citation: Neera K. Badhwar and Roderick T. Long. "Ayn Rand." Stanford Encyclopedia of Philosophy. First published June 8, 2010; substantive revision July 13, 2020. https://plato.stanford.edu/entries/ayn-rand/.
  url: https://plato.stanford.edu/entries/ayn-rand/
  accessed: '2026-10-15'
  reliability_note: Peer-reviewed reference entry.
---

# Objectivism (Ayn Rand's philosophy) (OBJCT)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44. The v7.1 scores and note are unchanged.

## Summary

Ayn Rand (1905–1982) 'outlined a comprehensive philosophy' in novels and essays; she 'derives the name of her philosophical system, “Objectivism”', from the trichotomy of intrinsic, subjective and objective [S1].

## Core metaphysics

Objective reality known by reason [S1, §1.3].

## Position on the LIO axes

- A BELOW_THRESHOLD (alt 4).
- D 4 (0.5).
- B, C, E UNKNOWN.

## Schools and variants

TODO

## Science

TODO

## Coding guidance

Avowed Objectivists only.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> OBJCT (46/50) — Objectivism (Ayn Rand's philosophy). Objectivism scores high for its rational, integrated approach to reality and ethics, promoting individualism with strong empirical ties, but slightly limited by its prescriptive economic views.

## Open questions

- A source for Rand's atheism.
- Adherents are TODO.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7 (score E on the world's order when the stub is filled).
- 2026-10-15 (systems batch S3): read the listed sources; quotations checked word for word against the fetched page text with a script. Axes under P44.
