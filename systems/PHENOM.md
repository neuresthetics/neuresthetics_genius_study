---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 3
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
    summary: 'Draft (systems batch S4): filled from SEP "Phenomenology" (Smith). All axes UNKNOWN: a method that brackets existence questions. v7.1 scores and note unchanged. Not reviewed.'
identity:
  id: PHENOM
  v7_1_number: 23
  v7_1_label: Phenomenology
  display_label: Phenomenology
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: philosophical school or method
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: '''the study of structures of consciousness as experienced from the first-person point of view''.'
  family:
    value: TODO
  parent_traditions:
    value: TODO
  related_codes: []
origins:
  founding_era:
    value: Early twentieth century
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP.
  founding_region:
    value: TODO
  founders_or_key_figures:
    value:
    - Edmund Husserl
    - Martin Heidegger
    - Jean-Paul Sartre
    - Maurice Merleau-Ponty
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP.
  key_texts: []
metaphysics:
  god_nature_relation:
    value: 'Not addressed: Husserl proposed ''bracketing'' the question of the existence of the natural world.'
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: SEP.
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
    value: TODO
    stance: TODO
  necessity_and_freedom:
    value: TODO
lio_axes:
  A_locus:
    value: UNKNOWN
    how_known: Not addressed in the sources read.
  B_cause:
    value: UNKNOWN
    how_known: Not addressed in the sources read.
  C_ledger:
    value: UNKNOWN
    how_known: Not addressed in the sources read.
  D_authority:
    value: UNKNOWN
    how_known: Not addressed in the sources read.
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
  scoring_note: Phenomenology scores high for its methodical exploration of experience, providing foundational insights into consciousness with strong logical and empirical ties, though focused more on description than prediction.
  source: v7.1 data book, section 6 table (tables[4]) row 23 and section 7 scoring notes
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
  use_when: The person's main stated worldview is phenomenological method.
  do_not_use_when: PHENOM sets no axes; score from the person. Religious phenomenologists keep their own God-view.
  neighbors: []
review:
  data_quality_flags: []
  open_questions:
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: David Woodruff Smith
  year: 2013
  citation: David Woodruff Smith. "Phenomenology." Stanford Encyclopedia of Philosophy. First published November 16, 2003; substantive revision December 16, 2013. https://plato.stanford.edu/entries/phenomenology/.
  url: https://plato.stanford.edu/entries/phenomenology/
  accessed: '2026-10-15'
  reliability_note: Peer-reviewed reference entry.
---

# Phenomenology (PHENOM)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44. The v7.1 scores and note are unchanged.

## Summary

'Phenomenology is the study of structures of consciousness as experienced from the first-person point of view' [S1]; it 'came into its own in the early 20th century in the works of Husserl, Heidegger, Sartre, Merleau-Ponty and others' [S1].

## Core metaphysics

Existence bracketed [S1].

## Position on the LIO axes

All UNKNOWN.

## Schools and variants

TODO

## Science

TODO

## Coding guidance

Score from the person.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> PHENOM (45/50) — Phenomenology. Phenomenology scores high for its methodical exploration of experience, providing foundational insights into consciousness with strong logical and empirical ties, though focused more on description than prediction.

## Open questions

- Adherents are TODO.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7 (score E on the world's order when the stub is filled).
- 2026-10-15 (systems batch S4): read the listed sources; quotations checked word for word against the fetched page text with a script. Axes under P44.
