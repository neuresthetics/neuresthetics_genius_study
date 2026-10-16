---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 5
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
    summary: 'Draft (systems batch S11): filled from Britannica "Church of Jesus Christ of Latter-day Saints" (Melton), introduction and Scriptures pages. A 1 (0.5, alt 0); C 1 (0.5, alt 0); D 1 (0.5, alt 0); B, E UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S11 audit fix: title corrected to Doctrine and Covenants.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'T1: B_cause searched, still UNKNOWN; search logged.'
identity:
  id: MORMON
  v7_1_number: 71
  v7_1_label: Mormonism (The Church of Jesus Christ of Latter-day Saints)
  display_label: Mormonism (The Church of Jesus Christ of Latter-day Saints)
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: religion
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: '''church that traces its origins to a religion founded by Joseph Smith in the United States in 1830''.'
  family:
    value: TODO
  parent_traditions:
    value: TODO
  related_codes: []
origins:
  founding_era:
    value: '1830'
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: Britannica.
  founding_region:
    value: United States (western New York)
    certainty: 1.0
    cites:
    - source: S1
      locator: History
    how_known: Britannica.
  founders_or_key_figures:
    value:
    - Joseph Smith
    - Brigham Young
    certainty: 1.0
    cites:
    - source: S1
      locator: History
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
    value: 1
    rationale: Father, Son and Holy Spirit, 'These three beings—the Godhead—are considered to be distinct entities (a doctrine known as tritheism)'; 'faithful members of the church may receive God’s fullness and thus become gods themselves'.
    certainty: 0.5
    cites: &id001
    - source: S2
      locator: Scriptures
    how_known: '0.5: personal divine beings; their place in nature is not stated. Alternative 0.'
    alternatives:
    - value: 0
      note: Named alternative.
      cites: *id001
  B_cause:
    value: UNKNOWN
    how_known: Not fixed by the sources read (T1 search logged, 2026-10-15).
  C_ledger:
    value: 1
    rationale: '''people’s futures are determined by their own actions as well as by the grace of God''; afterlife kingdoms (celestial, terrestrial, ''telestial'') and ''some degree of glory'' for nearly all.'
    certainty: 0.5
    cites: &id002
    - source: S2
      locator: Scriptures
    how_known: '0.5: reward by God with graded glory. Alternative 0.'
    alternatives:
    - value: 0
      note: Named alternative.
      cites: *id002
  D_authority:
    value: 1
    rationale: '''belief in continuing revelation''; church presidents are ''regarded as prophets'', and their revelations are added to the Doctrine and Covenants.'
    certainty: 0.5
    cites: &id003
    - source: S1
      locator: introduction
    - source: S2
      locator: Scriptures
    how_known: '0.5: the source does not set revelation against observation. Alternative 0.'
    alternatives:
    - value: 0
      note: Named alternative.
      cites: *id003
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
  E: 3
  V: 3
  X: 2
  total: 21
  scoring_note: Mormonism scores moderately low due to its heavy reliance on unique revelations and scriptures over empirical evidence, though it provides strong community and family-oriented coherence.
  source: v7.1 data book, section 6 table (tables[4]) row 71 and section 7 scoring notes
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
  use_when: The person was a Latter-day Saint (LDS or Community of Christ).
  do_not_use_when: Other Restorationist churches are CHRIST.
  neighbors: []
review:
  data_quality_flags:
  - v7.1 table 4 label is truncated; v7_1_label is taken from the section 7 scoring note.
  open_questions:
  - Community of Christ differs on some revelations (S2); not split.
  - 'Adherents: Britannica says more than 16 million (early 21st century); cite a demographic source.'
  - 'T1 (2026-10-15): B_cause search logged in the research log; still UNKNOWN.'
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: J. Gordon Melton
  citation: 'Melton, J. Gordon. "Church of Jesus Christ of Latter-day Saints." Encyclopaedia Britannica. https://www.britannica.com/topic/Church-of-Jesus-Christ-of-Latter-day-Saints. Wayback Machine snapshot 2026-10-09 23:47:53 UTC: https://web.archive.org/web/20261009234753/https://www.britannica.com/topic/Church-of-Jesus-Christ-of-Latter-day-Saints.'
  url: https://www.britannica.com/topic/Church-of-Jesus-Christ-of-Latter-day-Saints
  accessed: '2026-10-15'
  reliability_note: 'Signed article; introduction and history read. P44(e): read in the Wayback copy (https://web.archive.org/web/20261009234753/https://www.britannica.com/topic/Church-of-Jesus-Christ-of-Latter-day-Saints); live page not compared (live Britannica times out from the box).'
- id: S2
  type: tertiary
  kind: encyclopedia
  author: J. Gordon Melton
  citation: 'Melton, J. Gordon. "Church of Jesus Christ of Latter-day Saints: Scriptures." Encyclopaedia Britannica. https://www.britannica.com/topic/Church-of-Jesus-Christ-of-Latter-day-Saints/Scriptures. Wayback Machine snapshot 2026-10-09 23:47:52 UTC: https://web.archive.org/web/20261009234752/https://www.britannica.com/topic/Church-of-Jesus-Christ-of-Latter-day-Saints/Scriptures.'
  url: https://www.britannica.com/topic/Church-of-Jesus-Christ-of-Latter-day-Saints/Scriptures
  accessed: '2026-10-15'
  reliability_note: 'Later page of the same signed article (scriptures and doctrines). P44(e): read in the Wayback copy (https://web.archive.org/web/20261009234752/https://www.britannica.com/topic/Church-of-Jesus-Christ-of-Latter-day-Saints/Scriptures); live page not compared (live Britannica times out from the box).'
---

# Mormonism (The Church of Jesus Christ of Latter-day Saints) (MORMON)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

The Church of Jesus Christ of Latter-day Saints 'traces its origins to a religion founded by Joseph Smith in the United States in 1830' [S1].

## Core metaphysics

A Godhead of three distinct beings; continuing revelation; exaltation [S1, S2].

## Position on the LIO axes

- A 1 (0.5, alt 0); C 1 (0.5, alt 0); D 1 (0.5, alt 0).
- B, E UNKNOWN.

## Schools and variants

TODO

## Science

TODO

## Coding guidance

Latter-day Saints.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> MORMON (21/50) — Mormonism (The Church of Jesus Christ of Latter-day Saints). Mormonism scores moderately low due to its heavy reliance on unique revelations and scriptures over empirical evidence, though it provides strong community and family-oriented coherence.

## Open questions

- Community of Christ.
- Adherents.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7 (score E on the world's order when the stub is filled).
- 2026-10-15 (systems batch S11): read the listed sources; quotations checked word for word against the fetched page text. Britannica pages read in Wayback copies under P44(e); AI Top Questions not used.
- 2026-10-15 (S11 audit fix): title corrected to Doctrine and Covenants.
- 2026-10-15 (targeted A/B pass, batch T1): searched the sources below for a statement fixing B_cause; quotations checked word for word against fetched page text. MORMON: Britannica LDS page and Scriptures page re-searched: only 'laying on of hands for the gifts of the Holy Spirit'; no statement on miracles or natural law. B stays UNKNOWN.
