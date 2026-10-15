---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 3
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S7 for Jason)
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
    summary: 'Draft (systems batch S7): filled from Britannica "Hylozoism" (editors). A, B BELOW_THRESHOLD; C, D, E UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
identity:
  id: HYLO
  v7_1_number: 43
  v7_1_label: Hylozoism
  display_label: Hylozoism
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: metaphysical thesis
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: Britannica.
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
    - Thales
    - Anaximenes
    - Heracleitus
    - Straton
    - Ralph Cudworth (term)
    - Ernst Haeckel
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: Britannica.
  key_texts: []
metaphysics:
  god_nature_relation:
    value: '''any system that views all matter as alive, either in itself or by participation in the operation of a world soul or some similar principle''.'
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: Britannica.
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
    value: BELOW_THRESHOLD
    how_known: 'Members differ (P44(b)): Thales saw all things as ''full of gods''; Cudworth''s ''plastic nature'' acts ''as a divine instrument of change''; Straton and Haeckel are materialists (S1).'
  B_cause:
    value: BELOW_THRESHOLD
    how_known: 'Members differ: a world soul or plastic nature that ''controls and organizes matter'' versus a ''dynamic, materialistic view of nature'' (S1).'
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
  L: 8
  P: 7
  E: 6
  V: 7
  X: 4
  total: 32
  scoring_note: Hylozoism scores moderately as a philosophical view animating all matter, providing conceptual unity but constrained by speculative nature and modest empirical alignment.
  source: v7.1 data book, section 6 table (tables[4]) row 43 and section 7 scoring notes
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
  use_when: The person's own writing holds that all matter is alive.
  do_not_use_when: Consciousness in all matter is PANPSY; personified spirits are ANIM.
  neighbors: []
review:
  data_quality_flags: []
  open_questions:
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Britannica Editors
  citation: The Editors of Encyclopaedia Britannica. "Hylozoism." Encyclopaedia Britannica. https://www.britannica.com/topic/hylozoism.
  url: https://www.britannica.com/topic/hylozoism
  accessed: '2026-10-15'
  reliability_note: Short unsigned editors’ article. Read in its Wayback Machine copy (snapshot 2026-09-24); the live page timed out.
---

# Hylozoism (HYLO)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

Hylozoism is 'any system that views all matter as alive' [S1], distinct from animism and panpsychism.

## Core metaphysics

Living matter [S1].

## Position on the LIO axes

- A, B BELOW_THRESHOLD.
- C, D, E UNKNOWN.

## Schools and variants

TODO

## Science

TODO

## Coding guidance

All-matter-alive only.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> HYLO (32/50) — Hylozoism. Hylozoism scores moderately as a philosophical view animating all matter, providing conceptual unity but constrained by speculative nature and modest empirical alignment.

## Open questions

- Adherents are TODO.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7 (score E on the world's order when the stub is filled).
- 2026-10-15 (systems batch S7): read the listed sources; quotations checked word for word against the fetched page text. Britannica pages read in their full Wayback Machine copies (curl and WebFetch time out on the live site); Britannica AI Top Questions not used.
