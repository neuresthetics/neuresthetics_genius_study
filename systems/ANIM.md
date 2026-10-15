---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 4
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
    summary: 'Draft (systems batch S7): filled from Britannica "Animism" (Park). A BELOW_THRESHOLD (alt 3); B 1 (0.5, alt 0); C, D, E UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S7 audit fix: A quote starts at “no ground for supposing”.'
identity:
  id: ANIM
  v7_1_number: 40
  v7_1_label: Animism
  display_label: Animism
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: religion
    certainty: 1.0
    cites:
    - source: S1
      locator: Importance in the study of culture and religion
    how_known: '''not a single creed or doctrine but a view of the world''.'
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
    - Edward Burnett Tylor (term; Primitive Culture, 1871)
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: Britannica.
  key_texts: []
metaphysics:
  god_nature_relation:
    value: '''belief in innumerable spiritual beings concerned with human affairs and capable of helping or harming human interests''.'
    stance: many gods within nature
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
    how_known: 'Spirits indwell nature (Tylor: ''sun and stars, trees and rivers, winds and clouds, become personal animate creatures''), but ''no ground for supposing that polytheistic and monotheistic ideas were excluded'' (S1).'
    note: 'Members differ (P44(b)). Alternative: 3.'
    alternatives:
    - value: 3
      note: Named alternative.
      cites:
      - source: S1
        locator: Importance; Tylor’s theory
  B_cause:
    value: 1
    rationale: Spirits are 'capable of helping or harming human interests'; rites aim 'to influence powerful spirits and so control important natural events'.
    certainty: 0.5
    cites: &id001
    - source: S1
      locator: introduction; Tylor’s theory
    how_known: 0.5; the second quote is Tylor’s account. Alternative 0.
    alternatives:
    - value: 0
      note: Named alternative.
      cites: *id001
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
  scoring_note: Animism scores moderately as a spiritual philosophy emphasizing universal life and harmony, providing cultural depth but constrained by supernatural assumptions and modest empirical alignment.
  source: v7.1 data book, section 6 table (tables[4]) row 40 and section 7 scoring notes
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
  use_when: The person's own writing avows a world of indwelling spirits.
  do_not_use_when: Romantic nature reverence alone is not ANIM; matter-as-alive without spirits is HYLO.
  neighbors: []
review:
  data_quality_flags: []
  open_questions:
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: George Kerlin Park
  citation: Park, George Kerlin. "Animism." Encyclopaedia Britannica. https://www.britannica.com/topic/animism.
  url: https://www.britannica.com/topic/animism
  accessed: '2026-10-15'
  reliability_note: Signed article by an anthropologist; read through the Tylor section. AI Top Questions ignored.
---

# Animism (ANIM)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

Animism is 'belief in innumerable spiritual beings concerned with human affairs' [S1]; the term 'denotes not a single creed or doctrine but a view of the world' [S1].

## Core metaphysics

Indwelling spirits [S1].

## Position on the LIO axes

- A BELOW_THRESHOLD (alt 3); B 1 (0.5, alt 0).
- C, D, E UNKNOWN.

## Schools and variants

TODO

## Science

TODO

## Coding guidance

Avowed spirit worldview only.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> ANIM (32/50) — Animism. Animism scores moderately as a spiritual philosophy emphasizing universal life and harmony, providing cultural depth but constrained by supernatural assumptions and modest empirical alignment.

## Open questions

- Adherents are TODO.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7 (score E on the world's order when the stub is filled).
- 2026-10-15 (systems batch S7): read the listed sources; quotations checked word for word against the fetched page text. Britannica pages read in their full Wayback Machine copies (curl and WebFetch time out on the live site); Britannica AI Top Questions not used.
- 2026-10-15 (S7 audit fix): A quote trimmed.
