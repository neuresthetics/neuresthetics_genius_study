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
    summary: 'Draft (systems batch S11, thin): filled from Britannica "Yazīdī" (editors). A 2 (0.5, alt 1); C 2 (0.5, alt 1); B, D, E UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
identity:
  id: YAZID
  v7_1_number: 66
  v7_1_label: Yazidism (Yezidism)
  display_label: Yazidism (Yezidism)
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: religion
    certainty: 1.0
    cites:
    - source: S1
      locator: article
    how_known: '''Kurdish religious minority''.'
  family:
    value: TODO
  parent_traditions:
    value: TODO
  related_codes: []
origins:
  founding_era:
    value: 12th century
    certainty: 0.7
    cites:
    - source: S1
      locator: article
    how_known: Britannica.
  founding_region:
    value: Kurdish mountains of northern Iraq
    certainty: 1.0
    cites:
    - source: S1
      locator: article
    how_known: Britannica.
  founders_or_key_figures:
    value:
    - Sheikh ʿAdī ibn Musāfir
    certainty: 0.7
    cites:
    - source: S1
      locator: article
    how_known: 'Britannica: Sufi order founded in Lālish, early 12th century.'
  key_texts: []
metaphysics:
  god_nature_relation:
    value: '''a supreme creator god made the world and then ended his involvement with it, leaving it in the control of seven divine beings''.'
    stance: creator distinct from creation
    certainty: 1.0
    cites:
    - source: S1
      locator: article
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
    value: 2
    rationale: '''a supreme creator god made the world and then ended his involvement with it, leaving it in the control of seven divine beings''; the chief is Malak Ṭāʾūs.'
    certainty: 0.5
    cites: &id001
    - source: S1
      locator: article
    how_known: '0.5: a withdrawn creator and divine beings in control of the world. Alternative 1.'
    alternatives:
    - value: 1
      note: Named alternative.
      cites: *id001
  B_cause:
    value: UNKNOWN
    how_known: Not addressed in the sources read.
  C_ledger:
    value: 2
    rationale: '''The breaking of divine laws is expiated by way of metempsychosis, or transmigration of souls''; ''Heaven and hell are also included in Yazīdī mythology''.'
    certainty: 0.5
    cites: &id002
    - source: S1
      locator: article
    how_known: '0.5: an expiation-through-rebirth ledger beside heaven and hell; no karma-type law stated, so P44(d) does not apply. Alternative 1.'
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
  scoring_note: Yazidism scores moderately low due to its esoteric and oral-based nature, emphasizing spiritual liberation through reincarnation and angelic veneration within a monotheistic frame.
  source: v7.1 data book, section 6 table (tables[4]) row 66 and section 7 scoring notes
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
  use_when: The person was born into the Yazidi community.
  do_not_use_when: Kurdish Muslims are ISLAM.
  neighbors: []
review:
  data_quality_flags:
  - 'Thin: unsigned editors’ article; the scriptures it names may be 19th-century compilations.'
  open_questions:
  - A signed or peer-reviewed source.
  - 'Adherents: Britannica gives 200,000 to 1,000,000; cite a demographic source.'
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Britannica Editors
  citation: 'The Editors of Encyclopaedia Britannica. "Yazīdī." Encyclopaedia Britannica. https://www.britannica.com/topic/Yazidi. Wayback Machine snapshot 2026-09-15 02:30:31 UTC: https://web.archive.org/web/20260915023031/https://www.britannica.com/topic/Yazidi.'
  url: https://www.britannica.com/topic/Yazidi
  accessed: '2026-10-15'
  reliability_note: 'Unsigned editors’ article (revised by Noah Tesch); full article read. P44(e): read in the Wayback copy (https://web.archive.org/web/20260915023031/https://www.britannica.com/topic/Yazidi); live page not compared (live Britannica times out from the box).'
---

# Yazidism (Yezidism) (YAZID)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

The Yazīdīs are a 'Kurdish religious minority'; their religion 'includes elements of ancient Iranian religions as well as elements of Judaism, Nestorian Christianity, and Islam' [S1].

## Core metaphysics

Withdrawn creator; seven divine beings; Malak Ṭāʾūs [S1].

## Position on the LIO axes

- A 2 (0.5, alt 1); C 2 (0.5, alt 1).
- B, D, E UNKNOWN.

## Schools and variants

TODO

## Science

TODO

## Coding guidance

Yazidis.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> YAZID (23/50) — Yazidism (Yezidism). Yazidism scores moderately low due to its esoteric and oral-based nature, emphasizing spiritual liberation through reincarnation and angelic veneration within a monotheistic frame.

## Open questions

- Fuller source.
- Adherents.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7 (score E on the world's order when the stub is filled).
- 2026-10-15 (systems batch S11): read the listed sources; quotations checked word for word against the fetched page text. Britannica pages read in Wayback copies under P44(e); AI Top Questions not used.
