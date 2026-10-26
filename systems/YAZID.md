---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 4
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S9 for Jason)
  model_used: Grok Bot executor agent; direct reads of the cited pages
  collected_on: '2026-10-01'
  last_updated: '2026-10-25'
  change_log:
  - date: '2026-10-01'
    by: scripts/make_system_stubs.py
    summary: Stub created from v7.1 data book table 4 and section 7.
  - date: '2026-10-02'
    by: scripts/make_system_stubs.py
    summary: 'Decision P7: E_scope note added. E is not scored in a stub; when it is, score it on the
      world''s order (same rules for every kind of being and event, no in-group exceptions in this-world
      events). Salvation and moral community go on C_ledger.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'Draft (systems batch S11, thin): filled from Britannica "Yazīdī" (editors). A 2 (0.5, alt
      1); C 2 (0.5, alt 1); B, D, E UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from Britannica: family, kind, origins (Sheikh Adi; Lalish), full metaphysics
      (creator withdraws; Peacock Angel; metempsychosis; heaven/hell), practice, scriptures. Keep A=2,
      C=2; score D_authority 1 (0.5) from scripture/tradition; E stays UNKNOWN.'
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
      locator: opening
    how_known: 'Britannica: Kurdish religious minority.'
  family:
    value: Kurdish religious minority with syncretic roots (ancient Iranian, Jewish, Nestorian Christian,
      Islamic elements); distinct endogamous community
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  parent_traditions:
    value:
    - Ancient Iranian religions
    - Sufi ʿAdwiyyah order of Sheikh ʿAdī ibn Musāfir (12th c.)
    - Local Kurdish mountain traditions; Umayyad-lineage veneration
    certainty: 1.0
    cites:
    - source: S1
      locator: history paragraphs
    how_known: Britannica.
  related_codes:
  - code: ZORO
    relation: neighbor (easily confused)
    note: Iranian elements; not Zoroastrianism
  - code: ISLAM
    relation: neighbor (easily confused)
    note: Sufi origin of Adi; community left Islamic norms
  - code: DRUZE
    relation: neighbor (easily confused)
    note: both closed Middle Eastern minorities
  - code: THSAT
    relation: contrast case
    note: Peacock Angel is not Satan worship; outsiders' mislabel
origins:
  founding_era:
    value: Distinct community by mid-12th century around Mosul after Sheikh ʿAdī (early 12th c.); beliefs
      developed away from Islamic norms by 15th century
    certainty: 1.0
    cites:
    - source: S1
      locator: history paragraphs
    how_known: Britannica.
  founding_region:
    value: Kurdish mountains of northern Iraq (Lālish north of Mosul); now also SE Turkey, N Syria, Caucasus,
      Iran; diaspora in Germany
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; history
    how_known: Britannica.
  founders_or_key_figures:
    value:
    - Sheikh ʿAdī ibn Musāfir (Sufi; settled Lālish; chief saint; achieved divinity via metempsychosis)
    - Chief sheikh (supreme religious head)
    - Emir/prince (secular head)
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; history; cosmology
    how_known: Britannica.
  key_texts:
  - value: Kitāb al-jilwah (Book of Revelation)
    certainty: 0.7
    cites:
    - source: S1
      locator: closing
    how_known: 'Britannica: suspected 19th-c. compilation reflecting oral tradition.'
  - value: Maṣḥaf rash (Black Book)
    certainty: 0.7
    cites:
    - source: S1
      locator: closing
    how_known: 'Britannica: same caveat.'
  - value: Corpus of hymns in Kurdish
    certainty: 1.0
    cites:
    - source: S1
      locator: closing
    how_known: Britannica.
metaphysics:
  god_nature_relation:
    value: Supreme creator god made the world then ended involvement; world left to seven divine beings
      headed by Malak Ṭāʾūs (Peacock Angel).
    stance: creator distinct from creation
    certainty: 1.0
    cites:
    - source: S1
      locator: cosmogony paragraph
    how_known: Britannica.
  deity_personal:
    value: Personal supreme creator (withdrawn); personal Peacock Angel worshipped in peacock form; Sheikh
      ʿAdī divinized via metempsychosis.
    stance: personal
    certainty: 1.0
    cites:
    - source: S1
      locator: cosmogony; metempsychosis
    how_known: Britannica.
  intervention:
    value: Creator ended involvement; seven divine beings control the world. Ongoing intervention by Peacock
      Angel/beings is implied by worship; not detailed as miracle frequency.
    stance: regular
    certainty: 0.5
    cites:
    - source: S1
      locator: cosmogony
    how_known: Coder's reading; certainty 0.5; alternative 'rare' if control ≠ regular miracles.
  miracles:
    value: Not stated as a miracle doctrine; sanjaq peacock effigies and saint cult imply sacred efficacy.
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S1
      locator: cosmogony
    how_known: Britannica silence on 'miracles' term.
  petition_and_prayer:
    value: Worship of Malak Ṭāʾūs; annual pilgrimage to Sheikh ʿAdī's tomb at Lālish; sanjaqs circulated.
    stance: petition answered
    certainty: 0.5
    cites:
    - source: S1
      locator: cosmogony; closing
    how_known: Worship and pilgrimage; petition-answer theology not explicit — 0.5.
  afterlife:
    value: Metempsychosis (transmigration) for progressive purification; heaven and hell also in mythology;
      Sheikh ʿAdī achieved divinity through metempsychosis.
    stance: rebirth
    certainty: 1.0
    cites:
    - source: S1
      locator: metempsychosis paragraph
    how_known: Britannica. Heaven/hell coexist with rebirth.
  moral_ledger:
    value: Breaking divine laws expiated by metempsychosis; heaven and hell also present.
    stance: personal reward and punishment
    certainty: 0.7
    cites:
    - source: S1
      locator: metempsychosis paragraph
    how_known: Coder's reading; not karma-type law per prior P44(d) note on file.
  authority:
    value: Sacred scriptures (with oral-tradition caveat), Kurdish hymns, chief sheikh as supreme religious
      head; tradition and revelation over public science.
    stance: tradition or ancestors
    certainty: 0.7
    cites:
    - source: S1
      locator: opening; closing
    how_known: Coder's reading of Britannica.
  reserved_exemptions:
    value: Not addressed as physics exemptions. Myth of separate creation (Adam not Eve) and purity taboos
      structure community boundaries.
    stance: none
    certainty: 0.5
    cites:
    - source: S1
      locator: mythology; purity
    how_known: Community segregation is not the same as reserved natural-law exemptions — leave none at
      0.5.
  teleology_in_nature:
    value: Not addressed.
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: full article
    how_known: Silence.
  necessity_and_freedom:
    value: Not addressed.
    certainty: 1.0
    cites:
    - source: S1
      locator: full article
    how_known: Silence.
lio_axes:
  A_locus:
    value: 2
    rationale: '''a supreme creator god made the world and then ended his involvement with it, leaving
      it in the control of seven divine beings''; the chief is Malak Ṭāʾūs.'
    certainty: 0.5
    cites:
    - source: S1
      locator: cosmogony paragraph
    how_known: '0.5: withdrawn creator and divine beings in control. Alternative 1.'
    alternatives:
    - value: 1
      cites:
      - source: S1
        locator: cosmogony paragraph
      note: If withdrawn creator still counts as stronger transcendence pole.
  B_cause:
    value: UNKNOWN
    how_known: Creator withdrawal vs divine beings' control does not fix miracle/law pole clearly (P44).
  C_ledger:
    value: 2
    rationale: '''The breaking of divine laws is expiated by way of metempsychosis''; ''Heaven and hell
      are also included in Yazīdī mythology''.'
    certainty: 0.5
    cites:
    - source: S1
      locator: metempsychosis paragraph
    how_known: '0.5: rebirth expiation beside heaven/hell; not karma-type (P44(d)). Alternative 1.'
    alternatives:
    - value: 1
      cites:
      - source: S1
        locator: metempsychosis paragraph
      note: If heaven/hell personal judgment is weighted more.
  D_authority:
    value: 1
    rationale: Scriptures, hymns, and chief sheikh as supreme religious head; tradition/revelation over
      observation. Not pure revelation pole (oral + contested book dating).
    certainty: 0.5
    cites:
    - source: S1
      locator: opening; closing
    how_known: New from authority stance; 0.5 with UNKNOWN alternative if tradition alone is judged not
      to fix D.
    alternatives:
    - value: UNKNOWN
      cites:
      - source: S1
        locator: closing
      note: If 19th-c. book caveat blocks scoring.
  E_scope:
    value: UNKNOWN
    how_known: Endogamy and separate-creation myth structure community, but E scores this-world order
      exceptions, not salvation membership (P7). Not scored.
epistemology:
  value: Oral tradition and sacred books (with authenticity caveats); hymns; authority of chief sheikh.
    Esoteric community knowledge; contact with outsiders discouraged.
  certainty: 0.7
  cites:
  - source: S1
    locator: closing; purity
  how_known: Coder's reading.
ethics:
  value: 'Religious purity: food taboos, blue clothing taboo, avoid pronouncing Shayṭān; endogamy; caste
    system. Divine-law breaking expiated via metempsychosis.'
  certainty: 1.0
  cites:
  - source: S1
    locator: purity; metempsychosis
  how_known: Britannica.
practice:
  ritual_and_practice:
    value: Worship of Peacock Angel (peacock form; sanjaqs); annual pilgrimage to Sheikh ʿAdī's tomb at
      Lālish; purity taboos.
    certainty: 1.0
    cites:
    - source: S1
      locator: cosmogony; closing
    how_known: Britannica.
  community_form:
    value: Endogamous; strict caste; chief sheikh (religious) and emir (secular); 200,000–1,000,000; diaspora
      after persecution.
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; history
    how_known: Britannica.
science:
  historical_stance:
    value: Not a natural-science tradition. Avoidance of formal education noted historically as purity/contact
      concern.
    certainty: 0.7
    cites:
    - source: S1
      locator: purity
    how_known: Coder's reading.
  current_stance:
    value: Not addressed as modern science policy.
    certainty: 1.0
    cites:
    - source: S1
      locator: full article
    how_known: Silence.
schools_and_variants:
- name: Yazidi community (Lālish-centered)
  form: regional
  how_it_differs: Single people/religion; caste internal differentiation rather than denominations.
  lio_difference: A2 C2 D1 as scored; B E UNKNOWN.
  certainty: 1.0
  cites:
  - source: S1
    locator: opening
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
  scoring_note: Yazidism scores moderately low due to its esoteric and oral-based nature, emphasizing
    spiritual liberation through reincarnation and angelic veneration within a monotheistic frame.
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
  use_when: Yazidi by community identity or affirmed Yazidi faith.
  do_not_use_when: Not Satanism/THSAT. Not Zoroastrianism. Not Kurdish Muslims.
  neighbors:
  - code: ZORO
    relation: neighbor (easily confused)
  - code: THSAT
    relation: neighbor (easily confused)
  - code: DRUZE
    relation: neighbor (easily confused)
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
  citation: 'The Editors of Encyclopaedia Britannica. "Yazīdī." Encyclopaedia Britannica. https://www.britannica.com/topic/Yazidi.
    Wayback Machine snapshot 2026-09-15 02:30:31 UTC: https://web.archive.org/web/20260915023031/https://www.britannica.com/topic/Yazidi.'
  url: https://www.britannica.com/topic/Yazidi
  accessed: '2026-10-25'
  reliability_note: 'Unsigned editors’ article (revised by Noah Tesch); full article read. P44(e): read
    in the Wayback copy (https://web.archive.org/web/20260915023031/https://www.britannica.com/topic/Yazidi);
    live page not compared (live Britannica times out from the box).'
---
# Yazidi (YAZID)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

Yazīdīs are a 'Kurdish religious minority' whose religion 'includes elements of ancient Iranian religions as well as elements of Judaism, Nestorian Christianity, and Islam' [S1]. Religious centre: tomb of Sheikh ʿAdī at Lālish [S1].

## Core metaphysics

Supreme creator made the world then withdrew; seven divine beings led by Malak Ṭāʾūs (Peacock Angel) control it [S1]. Metempsychosis expiates broken divine laws; heaven and hell also in mythology [S1]. Not Devil worship [S1].

## Position on the LIO axes

- **A_locus: 2** (0.5; alt 1) — withdrawn creator + seven beings [S1].
- **B_cause:** UNKNOWN.
- **C_ledger: 2** (0.5; alt 1) — metempsychosis + heaven/hell [S1].
- **D_authority: 1** (0.5; alt UNKNOWN) — scripture/tradition/sheikh [S1].
- **E_scope:** UNKNOWN (P7).

## Schools and variants

One people/religion with internal caste, not denominations [S1].

## Science

Not a science tradition [S1].

## Coding guidance

Yazidi identity. Never THSAT.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> YAZID (23/50) — Yazidism (Yezidism). Yazidism scores moderately low due to its esoteric and oral-based nature, emphasizing spiritual liberation through reincarnation and angelic veneration within a monotheistic frame.

## Open questions

- Adherents detail / diaspora counts.

## Research log

- 2026-10-15 (batch S11): Britannica Yazidi; A and C scored.
- 2026-10-25: deepened classification, origins, metaphysics, practice; D_authority 1 (0.5). Re-read Britannica.
