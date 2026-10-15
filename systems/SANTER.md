---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 3
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
    summary: 'Draft (systems batch S9): filled from Britannica "Santería" (Murphy). B 1 (0.5, alt 0); D 1 (0.5); E 1 (0.5, alt 0); A, C UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
identity:
  id: SANTER
  v7_1_number: 56
  v7_1_label: Santería (Lucumí/Regla de Ocha)
  display_label: Santería (Lucumí/Regla de Ocha)
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: religion
    certainty: 1.0
    cites:
    - source: S1
      locator: article
    how_known: '''a religious tradition of African origin that was developed in Cuba''.'
  family:
    value: TODO
  parent_traditions:
    value: TODO
  related_codes: []
origins:
  founding_era:
    value: 19th century
    certainty: 0.7
    cites:
    - source: S1
      locator: article
    how_known: 'Britannica: Yoruba enslaved in the first decades of the 19th century.'
  founding_region:
    value: Cuba (Yoruba origin)
    certainty: 1.0
    cites:
    - source: S1
      locator: article
    how_known: Britannica.
  founders_or_key_figures:
    value: TODO
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
    how_known: The orishas are described as deities who act in the world; their relation to nature and any supreme god is not stated (S1).
  B_cause:
    value: 1
    rationale: '''Through the bodies of their mediums the orishas are believed to interact with the congregation directly and heal and prophesy''.'
    certainty: 0.5
    cites: &id001
    - source: S1
      locator: article
    how_known: 0.5. Alternative 0.
    alternatives:
    - value: 0
      note: Named alternative.
      cites: *id001
  C_ledger:
    value: UNKNOWN
    how_known: Not addressed in the sources read.
  D_authority:
    value: 1
    rationale: In the Ifá oracle a priest 'interprets the fall of consecrated palm nuts to reveal the orishas’ response'.
    certainty: 0.5
    cites:
    - source: S1
      locator: article
    how_known: '0.5: divination as revelation.'
  E_scope:
    value: 1
    rationale: 'On the world''s order (P7): orishas ''provide their devotees with protection, wisdom, and success''.'
    certainty: 0.5
    cites: &id002
    - source: S1
      locator: article
    how_known: '0.5: favour to devotees. Alternative 0.'
    alternatives:
    - value: 0
      note: Named alternative.
      cites: *id002
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
  E: 5
  V: 5
  X: 3
  total: 26
  scoring_note: Santería scores moderately due to its rich syncretic traditions and emphasis on spiritual balance, offering cultural coherence but limited by supernatural elements and lack of empirical rigor.
  source: v7.1 data book, section 6 table (tables[4]) row 56 and section 7 scoring notes
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
  use_when: The person was initiated into or practised Santería / Lukumí.
  do_not_use_when: Cuban heritage alone is not enough.
  neighbors: []
review:
  data_quality_flags: []
  open_questions:
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Joseph M. Murphy
  citation: 'Murphy, Joseph M.. "Santería." Encyclopaedia Britannica. https://www.britannica.com/topic/Santeria. Wayback Machine snapshot 2026-10-12 06:32:21 UTC: https://web.archive.org/web/20261012063221/https://www.britannica.com/topic/Santeria.'
  url: https://www.britannica.com/topic/Santeria
  accessed: '2026-10-15'
  reliability_note: 'Signed article (scholar of Santería); full short article read. P44(e): read in the Wayback copy (https://web.archive.org/web/20261012063221/https://www.britannica.com/topic/Santeria); live page timed out on 2026-10-15, so no live comparison.'
---

# Santería (Lucumí/Regla de Ocha) (SANTER)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

Santería is 'a religious tradition of African origin that was developed in Cuba'; it 'is based upon the development of personal relationships through divination, sacrifice, initiation, and mediumship' with the orishas [S1].

## Core metaphysics

Orishas [S1].

## Position on the LIO axes

- B 1 (alt 0), D 1, E 1 (alt 0); all 0.5.
- A, C UNKNOWN.

## Schools and variants

TODO

## Science

TODO

## Coding guidance

Initiated or practising.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> SANTER (26/50) — Santería (Lucumí/Regla de Ocha). Santería scores moderately due to its rich syncretic traditions and emphasis on spiritual balance, offering cultural coherence but limited by supernatural elements and lack of empirical rigor.

## Open questions

- Adherents are TODO.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7 (score E on the world's order when the stub is filled).
- 2026-10-15 (systems batch S9): read the listed sources; quotations checked word for word against the fetched page text. Britannica pages read in Wayback copies under P44(e); AI Top Questions not used.
