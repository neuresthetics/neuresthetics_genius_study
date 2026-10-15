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
    summary: 'Draft (systems batch S7): filled from Goossaert, "Chinese Religion: Popular Religion", Encyclopedia of Religion (2005). A 3 (0.5); B 1 (0.5, alt 0); C 1 (0.5); D 1 (0.5, alt 2); E 1 (0.5, alt 0). v7.1 scores and note unchanged. Not reviewed.'
identity:
  id: CHNFOLK
  v7_1_number: 42
  v7_1_label: Chinese Folk Religion (Shenism)
  display_label: Chinese Folk Religion (Shenism)
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: religion
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: '''a scholarly construct which does not correspond to any traditional Chinese notion or institution''.'
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
    value: TODO
  key_texts: []
metaphysics:
  god_nature_relation:
    value: '''the material and spiritual realms are not separate. The universe is a whole organic system''; gods are ''dead human beings endowed with exceptional ling''.'
    stance: many gods within nature
    certainty: 1.0
    cites:
    - source: S1
      locator: Theology
    how_known: Encyclopedia of Religion.
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
    value: '''actions carry retribution (conceived either as automatic karma accounting, or, more often, as a post-mortem judicial process administered in courts of hell)''.'
    stance: personal reward and punishment
    certainty: 1.0
    cites:
    - source: S1
      locator: Theology
    how_known: Encyclopedia of Religion.
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
    rationale: Gods are deified dead humans inside one organic universe; Heaven (the Jade emperor) heads a bureaucratic pantheon.
    certainty: 0.5
    cites:
    - source: S1
      locator: Theology
    how_known: '0.5: as EPICUR and JAIN, gods within nature fit 3.'
  B_cause:
    value: 1
    rationale: '''Miracles and the answering of prayers are manifestations of ling''; ghosts ''can cause illnesses and accidents''.'
    certainty: 0.5
    cites: &id001
    - source: S1
      locator: Theology
    how_known: '0.5: frequent intervention within one cosmology that evolves ''according to known rules''. Alternative 0.'
    alternatives:
    - value: 0
      note: Named alternative.
      cites: *id001
  C_ledger:
    value: 1
    rationale: Retribution mostly by a post-mortem judicial process in courts of hell; sometimes automatic karma.
    certainty: 0.5
    cites:
    - source: S1
      locator: Theology
    how_known: '0.5: mostly personal judgment.'
  D_authority:
    value: 1
    rationale: No common canon; spirit-writing revelations, mediums and divination; theology 'entrusted to clerical specialists'.
    certainty: 0.5
    cites: &id002
    - source: S1
      locator: Theology; Social structures
    how_known: 0.5. Alternative 2.
    alternatives:
    - value: 2
      note: Named alternative.
      cites: *id002
  E_scope:
    value: 1
    rationale: 'On the world''s order (P7): ''All cults are reciprocal, contractual relations between a human community and a deity''; some gods help devotees ''in an exclusive relationship''.'
    certainty: 0.5
    cites: &id003
    - source: S1
      locator: Theology
    how_known: 0.5. Alternative 0.
    alternatives:
    - value: 0
      note: Named alternative.
      cites: *id003
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
  P: 8
  E: 6
  V: 6
  X: 4
  total: 32
  scoring_note: Chinese Folk Religion scores moderately due to its flexible syncretism for daily life and harmony, blending traditions effectively but constrained by supernatural elements and cultural authority over empirical rigor.
  source: v7.1 data book, section 6 table (tables[4]) row 42 and section 7 scoring notes
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
  use_when: The person practised Chinese local cults and ancestor rites as their own religion.
  do_not_use_when: Institutional Confucians are CONFUC, Buddhists BUDDH, Daoists TAO.
  neighbors: []
review:
  data_quality_flags: []
  open_questions:
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Vincent Goossaert
  year: 2005
  citation: 'Goossaert, Vincent. "Chinese Religion: Popular Religion." In Encyclopedia of Religion, 2nd ed., edited by Lindsay Jones. Detroit: Macmillan Reference USA, 2005. Online at Encyclopedia.com.'
  url: https://www.encyclopedia.com/environment/encyclopedias-almanacs-transcripts-and-maps/chinese-religion-popular-religion
  accessed: '2026-10-15'
  reliability_note: Signed scholarly encyclopedia entry (Encyclopedia of Religion, 2nd ed.), read in the Encyclopedia.com copy. Britannica has no full article on Chinese religion.
---

# Chinese Folk Religion (Shenism) (CHNFOLK)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

Chinese popular religion 'is a scholarly construct'; most practices belong to 'a single system, best termed “Chinese religion”' [S1].

## Core metaphysics

Gods, ghosts and ancestors in one organic universe [S1].

## Position on the LIO axes

- A 3; B 1 (alt 0); C 1; D 1 (alt 2); E 1 (alt 0); all 0.5.

## Schools and variants

TODO

## Science

TODO

## Coding guidance

Practising local religion.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> CHNFOLK (32/50) — Chinese Folk Religion (Shenism). Chinese Folk Religion scores moderately due to its flexible syncretism for daily life and harmony, blending traditions effectively but constrained by supernatural elements and cultural authority over empirical rigor.

## Open questions

- Adherents are TODO.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7 (score E on the world's order when the stub is filled).
- 2026-10-15 (systems batch S7): read the listed sources; quotations checked word for word against the fetched page text. Britannica pages read in their full Wayback Machine copies (curl and WebFetch time out on the live site); Britannica AI Top Questions not used.
