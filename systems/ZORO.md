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
    summary: 'Draft (systems batch S11): filled from Britannica "Zoroastrianism" (Duchesne-Guillemin), introduction, Beliefs and mythology, and Cosmology pages. A 1 (0.5, alt 0); C 0 (0.7, alt 1); B, D, E UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
identity:
  id: ZORO
  v7_1_number: 67
  v7_1_label: Zoroastrianism (Mazdayasna)
  display_label: Zoroastrianism (Mazdayasna)
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: religion
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: '''ancient pre-Islamic religion of Iran''.'
  family:
    value: TODO
  parent_traditions:
    value: TODO
  related_codes: []
origins:
  founding_era:
    value: before the 6th century BCE
    certainty: 0.7
    cites:
    - source: S1
      locator: introduction
    how_known: Zarathushtra 'flourished before the 6th century bce'.
  founding_region:
    value: Iran
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: Britannica.
  founders_or_key_figures:
    value:
    - Zarathushtra (Zoroaster)
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: '''traditionally regarded as the founder''.'
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
    rationale: '''unifying under the worship of one supreme god''; in the Vidēvdāt ''Ahura Mazdā and the Destructive Spirit opposed each other by creating, respectively, the good and the bad things''.'
    certainty: 0.5
    cites: &id001
    - source: S1
      locator: Nature and significance
    - source: S2
      locator: God
    how_known: '0.5: a creator god opposed by an antigod; dualism and the later pantheon give alternative 0 or 2. Alternative 0.'
    alternatives:
    - value: 0
      note: Named alternative.
      cites: *id001
  B_cause:
    value: UNKNOWN
    how_known: Not addressed in the sources read.
  C_ledger:
    value: 0
    rationale: The soul crosses 'the Bridge of the Requiter. It leads the good souls to paradise, but the bad ones fall into hell'; 'The soul has also to undergo a judgment; it appears before Mithra and his two companions'.
    certainty: 0.7
    cites: &id002
    - source: S3
      locator: Cosmology
    how_known: '0.7: judgment of persons by gods. Alternative 1.'
    alternatives:
    - value: 1
      note: Named alternative.
      cites: *id002
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
  L: 7
  P: 6
  E: 4
  V: 4
  X: 2
  total: 23
  scoring_note: Zoroastrianism scores moderately low due to its revelatory dualism and limited empirical alignment, though it pioneered ethical monotheism influencing later religions.
  source: v7.1 data book, section 6 table (tables[4]) row 67 and section 7 scoring notes
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
  use_when: The person was Zoroastrian or Parsi by practice.
  do_not_use_when: Manichaeism is not ZORO.
  neighbors: []
review:
  data_quality_flags: []
  open_questions:
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Jacques Duchesne-Guillemin
  citation: 'Duchesne-Guillemin, Jacques. "Zoroastrianism." Encyclopaedia Britannica. https://www.britannica.com/topic/Zoroastrianism. Wayback Machine snapshot 2026-01-01 12:47:08 UTC: https://web.archive.org/web/20260101124708/https://www.britannica.com/topic/Zoroastrianism.'
  url: https://www.britannica.com/topic/Zoroastrianism
  accessed: '2026-10-15'
  reliability_note: 'Signed article (Indo-Iranian studies); introduction and Nature and significance read. Newest 2026 snapshot (20261001082722) was a bot-check page. P44(e): read in the Wayback copy (https://web.archive.org/web/20260101124708/https://www.britannica.com/topic/Zoroastrianism); live page not compared (live Britannica times out from the box).'
- id: S2
  type: tertiary
  kind: encyclopedia
  author: Jacques Duchesne-Guillemin
  citation: 'Duchesne-Guillemin, Jacques. "Zoroastrianism: Beliefs and mythology." Encyclopaedia Britannica. https://www.britannica.com/topic/Zoroastrianism/Beliefs-and-mythology. Wayback Machine snapshot 2026-07-21 18:53:41 UTC: https://web.archive.org/web/20260721185341/https://www.britannica.com/topic/Zoroastrianism/Beliefs-and-mythology.'
  url: https://www.britannica.com/topic/Zoroastrianism/Beliefs-and-mythology
  accessed: '2026-10-15'
  reliability_note: 'Later page of the same signed article. P44(e): read in the Wayback copy (https://web.archive.org/web/20260721185341/https://www.britannica.com/topic/Zoroastrianism/Beliefs-and-mythology); live page not compared (live Britannica times out from the box).'
- id: S3
  type: tertiary
  kind: encyclopedia
  author: Jacques Duchesne-Guillemin
  citation: 'Duchesne-Guillemin, Jacques. "Zoroastrianism: Cosmology." Encyclopaedia Britannica. https://www.britannica.com/topic/Zoroastrianism/Cosmology. Wayback Machine snapshot 2026-01-30 12:14:29 UTC: https://web.archive.org/web/20260130121429/https://www.britannica.com/topic/Zoroastrianism/Cosmology.'
  url: https://www.britannica.com/topic/Zoroastrianism/Cosmology
  accessed: '2026-10-15'
  reliability_note: 'Later page of the same signed article. P44(e): read in the Wayback copy (https://web.archive.org/web/20260130121429/https://www.britannica.com/topic/Zoroastrianism/Cosmology); live page not compared (live Britannica times out from the box).'
---

# Zoroastrianism (Mazdayasna) (ZORO)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

Zoroastrianism is an 'ancient pre-Islamic religion of Iran' that 'contains both monotheistic and dualistic features' [S1].

## Core metaphysics

Ahura Mazdā against Angra Mainyu; free choice; judgment of souls [S1–S3].

## Position on the LIO axes

- A 1 (0.5, alt 0); C 0 (0.7, alt 1).
- B, D, E UNKNOWN.

## Schools and variants

TODO

## Science

TODO

## Coding guidance

Zoroastrians and Parsis.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> ZORO (23/50) — Zoroastrianism (Mazdayasna). Zoroastrianism scores moderately low due to its revelatory dualism and limited empirical alignment, though it pioneered ethical monotheism influencing later religions.

## Open questions

- Adherents are TODO.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7 (score E on the world's order when the stub is filled).
- 2026-10-15 (systems batch S11): read the listed sources; quotations checked word for word against the fetched page text. Britannica pages read in Wayback copies under P44(e); AI Top Questions not used.
