---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 5
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S8 for Jason)
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
    summary: 'Draft (systems batch S8): filled from Britannica "Shintō" (Hirai). A 3 (0.5, alt 2); B, C, D, E UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'P44(e) compliance (with the S7 fixes): Wayback snapshot URL and timestamp cited.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S8 audit fix: B UNKNOWN -> 2 @0.5 (alt 1) from the full article; A how_known adds Hirata and musubi.'
identity:
  id: SHINTO
  v7_1_number: 45
  v7_1_label: Shinto
  display_label: Shinto
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: religion
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
    value: Japan
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: Britannica.
  founders_or_key_figures:
    value:
    - None (no founder)
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: '''Shintō has no founder''.'
  key_texts: []
metaphysics:
  god_nature_relation:
    value: '''Ancient Shintō was polytheistic. People found kami in nature, which ruled seas or mountains, as well as in outstanding men.'''
    stance: many gods within nature
    certainty: 1.0
    cites:
    - source: S1
      locator: Early clan religion and ceremonies
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
    value: 3
    rationale: Kami ('sacred or divine power, specifically the various gods or deities') are found in nature and in outstanding men.
    certainty: 0.5
    cites: &id001
    - source: S1
      locator: introduction; Early clan religion
    - source: S2
      locator: Fukko Shintō
    how_known: '0.5: gods within nature fit 3 (as JAIN, CHNFOLK); kami of ideas such as creation make 2 the alternative. Full read: Hirata''s creator god and other-world retribution ''were not accepted into the main current of Shintō''; Motoori''s musubi, ''the mystical power of becoming or of creation'', is the reason for alternative 2.'
    alternatives:
    - value: 2
      note: Named alternative.
      cites: *id001
  B_cause:
    value: 2
    rationale: 'Petitionary prayer to protecting kami: ''prayers were offered for the safety of the state and people''; children visit the shrine ''to give thanks for kami’s protection''; Motoori''s ''absolute faith—according to which all problems beyond human capability were turned over to kami''.'
    certainty: 0.5
    cites: &id002
    - source: S3
      locator: Political and social roles
    - source: S4
      locator: rites of passage
    - source: S2
      locator: Fukko Shintō
    how_known: '0.5 (S8 audit ruling): protection and answered prayer, with no doctrine of miracles stated. Alternative 1.'
    alternatives:
    - value: 1
      note: Named alternative.
      cites: *id002
  C_ledger:
    value: UNKNOWN
    how_known: Not addressed in the sources read.
  D_authority:
    value: UNKNOWN
    how_known: '''no official sacred scriptures in the strict sense, and no fixed dogmas'' (S1); no positive authority stated.'
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
schools_and_variants:
- name: Shrine Shintō
  form: other
  how_it_differs: Main current; includes the defunct State Shintō.
  lio_difference: None stated.
  certainty: 1.0
  cites:
  - source: S1
    locator: Nature and varieties
- name: Sect Shintō
  form: other
  how_it_differs: 13 major sects from the 19th century, each with a founder or systematizer.
  lio_difference: None stated.
  certainty: 1.0
  cites:
  - source: S1
    locator: Nature and varieties
- name: Folk Shintō
  form: other
  how_it_differs: No formal organization or doctrine; roadside images and agricultural rites.
  lio_difference: None stated.
  certainty: 1.0
  cites:
  - source: S1
    locator: Nature and varieties
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: TODO
v7_1_rubric:
  label: authorial v7.1 scores
  L: 8
  P: 8
  E: 6
  V: 6
  X: 4
  total: 32
  scoring_note: Shinto scores moderately due to its elegant focus on natural harmony and ritual purity, offering cultural and ethical coherence but constrained by supernatural elements and traditional authority over empirical rigor.
  source: v7.1 data book, section 6 table (tables[4]) row 45 and section 7 scoring notes
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
  use_when: The person practised Shintō as their own religion.
  do_not_use_when: Japanese nationality or shrine attendance as custom alone is not enough.
  neighbors: []
review:
  data_quality_flags: []
  open_questions:
  - Later sections (beliefs, practices) not read.
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Naofusa Hirai; Britannica Editors
  citation: 'Hirai, Naofusa, and Britannica Editors. "Shintō." Encyclopaedia Britannica. https://www.britannica.com/topic/Shinto. Wayback Machine snapshot 2026-10-03 18:03:43 UTC: https://web.archive.org/web/20261003180343/https://www.britannica.com/topic/Shinto.'
  url: https://www.britannica.com/topic/Shinto
  accessed: '2026-10-15'
  reliability_note: 'Signed article (Kokugakuin emeritus professor); introduction to early history read. P44(e): read in the Wayback copy (https://web.archive.org/web/20261003180343/https://www.britannica.com/topic/Shinto); live page timed out on 2026-10-15, so no live comparison.'
- id: S2
  type: tertiary
  kind: encyclopedia
  author: Naofusa Hirai; Britannica Editors
  citation: 'Hirai, Naofusa, and Britannica Editors. "Shintō: Shintō reaction against Buddhism." Encyclopaedia Britannica. https://www.britannica.com/topic/Shinto/Shinto-reaction-against-Buddhism. Wayback Machine snapshot 2025-11-25 14:48:08 UTC: https://web.archive.org/web/20251125144808/https://www.britannica.com/topic/Shinto/Shinto-reaction-against-Buddhism.'
  url: https://www.britannica.com/topic/Shinto/Shinto-reaction-against-Buddhism
  accessed: '2026-10-15'
  reliability_note: 'Later page of the same signed article (S8 audit fix). P44(e): read in the Wayback copy (https://web.archive.org/web/20251125144808/https://www.britannica.com/topic/Shinto/Shinto-reaction-against-Buddhism); live page not compared.'
- id: S3
  type: tertiary
  kind: encyclopedia
  author: Naofusa Hirai; Britannica Editors
  citation: 'Hirai, Naofusa, and Britannica Editors. "Shintō: Political and social roles." Encyclopaedia Britannica. https://www.britannica.com/topic/Shinto/Political-and-social-roles. Wayback Machine snapshot 2025-10-08 20:43:06 UTC: https://web.archive.org/web/20251008204306/https://www.britannica.com/topic/Shinto/Political-and-social-roles.'
  url: https://www.britannica.com/topic/Shinto/Political-and-social-roles
  accessed: '2026-10-15'
  reliability_note: 'Later page of the same signed article (S8 audit fix). P44(e): read in the Wayback copy (https://web.archive.org/web/20251008204306/https://www.britannica.com/topic/Shinto/Political-and-social-roles); live page not compared.'
- id: S4
  type: tertiary
  kind: encyclopedia
  author: Naofusa Hirai; Britannica Editors
  citation: 'Hirai, Naofusa, and Britannica Editors. "Shintō: Ritual practices and institutions." Encyclopaedia Britannica. https://www.britannica.com/topic/Shinto/Ritual-practices-and-institutions. Wayback Machine snapshot 2026-10-06 22:19:34 UTC: https://web.archive.org/web/20261006221934/https://www.britannica.com/topic/Shinto/Ritual-practices-and-institutions.'
  url: https://www.britannica.com/topic/Shinto/Ritual-practices-and-institutions
  accessed: '2026-10-15'
  reliability_note: 'Later page of the same signed article (S8 audit fix). P44(e): read in the Wayback copy (https://web.archive.org/web/20261006221934/https://www.britannica.com/topic/Shinto/Ritual-practices-and-institutions); live page not compared.'
---

# Shinto (SHINTO)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

Shintō: 'indigenous religious beliefs and practices of Japan'; it 'has no founder, no official sacred scriptures in the strict sense, and no fixed dogmas' [S1].

## Core metaphysics

Kami in nature and people [S1].

## Position on the LIO axes

- A 3 (0.5, alt 2); B 2 (0.5, alt 1).
- C, D, E UNKNOWN.

## Schools and variants

Shrine, Sect and Folk Shintō [S1].

## Science

TODO

## Coding guidance

Practising Shintō.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> SHINTO (32/50) — Shinto. Shinto scores moderately due to its elegant focus on natural harmony and ritual purity, offering cultural and ethical coherence but constrained by supernatural elements and traditional authority over empirical rigor.

## Open questions

- Later sections.
- Adherents are TODO.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7 (score E on the world's order when the stub is filled).
- 2026-10-15 (systems batch S8): read the listed sources; quotations checked word for word against the fetched page text. Britannica pages read in full Wayback Machine copies (live site times out); AI Top Questions not used.
- 2026-10-15: P44(e) Wayback citation.
- 2026-10-15 (S8 audit fix): later article pages read; B scored.
