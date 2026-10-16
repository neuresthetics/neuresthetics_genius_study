---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 4
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S9 for Jason)
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
    summary: 'Draft (systems batch S10, thin): filled from Britannica "Anthroposophy" (editors, one paragraph). D BELOW_THRESHOLD; rest UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S10 audit fix: D BELOW_THRESHOLD -> 1 @0.5 (alt 2).'
identity:
  id: ANTHRO
  v7_1_number: 58
  v7_1_label: Anthroposophy
  display_label: Anthroposophy
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: philosophical school or method
    certainty: 0.7
    cites:
    - source: S1
      locator: article
    how_known: '''philosophy based on the premise that the human intellect has the ability to contact spiritual worlds''.'
  family:
    value: TODO
  parent_traditions:
    value: TODO
  related_codes: []
origins:
  founding_era:
    value: Anthroposophical Society founded 1912
    certainty: 1.0
    cites:
    - source: S1
      locator: article
    how_known: Britannica.
  founding_region:
    value: TODO
  founders_or_key_figures:
    value:
    - Rudolf Steiner
    certainty: 1.0
    cites:
    - source: S1
      locator: article
    how_known: Britannica.
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
    value: 1
    rationale: Steiner sought 'a faculty for spiritual perception independent of the senses', since the spiritual world is 'fully accessible only to the faculties of knowledge latent in all humans'.
    certainty: 0.5
    cites: &id001
    - source: S1
      locator: article
    how_known: '0.5: the founder’s stated stance; supersensible perception is placed above the senses for spiritual knowledge. Alternative 2 (pure thought also named).'
    alternatives:
    - value: 2
      note: Named alternative.
      cites: *id001
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
  L: 7
  P: 6
  E: 4
  V: 5
  X: 3
  total: 25
  scoring_note: Anthroposophy scores moderately due to its ambitious integration of spirit and science, offering innovative applications but limited by revelatory and unempirical elements.
  source: v7.1 data book, section 6 table (tables[4]) row 58 and section 7 scoring notes
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
  use_when: The person self-identifies with Anthroposophy.
  do_not_use_when: Waldorf schooling or biodynamic farming alone is not enough.
  neighbors: []
review:
  data_quality_flags:
  - 'Thin: one-paragraph editors’ article.'
  open_questions:
  - A signed or peer-reviewed source.
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Britannica Editors
  citation: 'The Editors of Encyclopaedia Britannica. "Anthroposophy." Encyclopaedia Britannica. https://www.britannica.com/topic/anthroposophy. Wayback Machine snapshot 2026-10-09 13:54:13 UTC: https://web.archive.org/web/20261009135413/https://www.britannica.com/topic/anthroposophy.'
  url: https://www.britannica.com/topic/anthroposophy
  accessed: '2026-10-15'
  reliability_note: 'Short unsigned editors’ article (one paragraph). P44(e): read in the Wayback copy (https://web.archive.org/web/20261009135413/https://www.britannica.com/topic/anthroposophy); live page not compared (live Britannica times out from the box).'
---

# Anthroposophy (ANTHRO)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

Anthroposophy is a 'philosophy based on the premise that the human intellect has the ability to contact spiritual worlds', formulated by Rudolf Steiner [S1].

## Core metaphysics

A spiritual world open to pure thought and to latent faculties [S1].

## Position on the LIO axes

- D 1 (0.5, alt 2).
- A, B, C, E UNKNOWN.

## Schools and variants

TODO

## Science

TODO

## Coding guidance

Self-identified anthroposophists.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> ANTHRO (25/50) — Anthroposophy. Anthroposophy scores moderately due to its ambitious integration of spirit and science, offering innovative applications but limited by revelatory and unempirical elements.

## Open questions

- Fuller source.
- Adherents are TODO.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7 (score E on the world's order when the stub is filled).
- 2026-10-15 (systems batch S10): read the listed sources; quotations checked word for word against the fetched page text. Britannica pages read in Wayback copies under P44(e); AI Top Questions not used.
- 2026-10-15 (S10 audit fix): D BELOW_THRESHOLD -> 1 @0.5 (alt 2).
