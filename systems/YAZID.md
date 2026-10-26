---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 7
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
    summary: "Decision P7: E_scope note added. E is not scored in a stub; when it is, score it on the\
      \ world's order (same rules for every kind of being and event, no in-group exceptions in this-world\
      \ events). Salvation and moral community go on C_ledger."
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'Draft (systems batch S11, thin): filled from Britannica "Yazīdī" (editors). A 2 (0.5, alt
      1); C 2 (0.5, alt 1); B, D, E UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from Britannica: family, kind, origins (Sheikh Adi; Lalish), full metaphysics
      (creator withdraws; Peacock Angel; metempsychosis; heaven/hell), practice, scriptures. Keep A=2,
      C=2; score D_authority 1 (0.5) from scripture/tradition; E stays UNKNOWN.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Fill adherents/estimate gloss from existing sources (order-of-magnitude / qualitative). Axes
      unchanged.
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score E_scope 1 (0.5) from Britannica Yazīdī (created separately; endogamy; purity taboos).
      Deepen B_cause UNKNOWN→1 (0.5) for sanjaq/peacock worship ritual power. A/C/D unchanged.
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen practice/festivals, epistemology (qewls), cosmogony detail, schools from Wikipedia
      Yazidism. Keep Britannica S1. No LIO moves.'
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
    value: 'Kurdish religious minority with syncretic roots (ancient Iranian, Jewish, Nestorian Christian,
      Islamic elements); distinct endogamous community'
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
    note: "Peacock Angel is not Satan worship; outsiders' mislabel"
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
    value: 'Kurdish mountains of northern Iraq (Lālish north of Mosul); now also SE Turkey, N Syria, Caucasus,
      Iran; diaspora in Germany'
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
    value: 'Monotheism: remote creator (Xwedê) entrusts the world to seven self-emanated angels headed
      by Tawûsî Melek (Peacock Angel). Divine triad of God / Tawûsî Melek / Sheikh Adi / Sultan Ezid hypostases;
      Xudans of natural elements. Peacock Angel is not Satan in Yazidi belief.'
    stance: creator distinct from creation
    certainty: 0.7
    cites: &id001
    - source: S2
      locator: Principal beliefs; Festivals
    how_known: '0.8 — Wikipedia Yazidism summarizing Asatrian/Arakelova/Allison.'
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
    how_known: "Coder's reading; certainty 0.5; alternative 'rare' if control ≠ regular miracles."
  miracles:
    value: Not stated as a miracle doctrine; sanjaq peacock effigies and saint cult imply sacred efficacy.
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S1
      locator: cosmogony
    how_known: "Britannica silence on 'miracles' term."
  petition_and_prayer:
    value: "Worship of Malak Ṭāʾūs; annual pilgrimage to Sheikh ʿAdī's tomb at Lālish; sanjaqs circulated."
    stance: petition answered
    certainty: 0.5
    cites:
    - source: S1
      locator: cosmogony; closing
    how_known: Worship and pilgrimage; petition-answer theology not explicit — 0.5.
  afterlife:
    value: 'Metempsychosis (kirasgorîn, change of shirt) for progressive purification; cyclic bedîl/dewr
      alongside linear eschatology; heaven/hell mythology also present. Collective purification floods
      (tofan) through water, fire, air.'
    stance: rebirth
    certainty: 0.7
    cites:
    - source: S2
      locator: Rebirth and concept of time
    how_known: '0.7 — Wikipedia.'
  moral_ledger:
    value: Breaking divine laws expiated by metempsychosis; heaven and hell also present.
    stance: personal reward and punishment
    certainty: 0.7
    cites:
    - source: S1
      locator: metempsychosis paragraph
    how_known: "Coder's reading; not karma-type law per prior P44(d) note on file."
  authority:
    value: Oral qewls (hymns) as highest authority; Baba Sheikh and Mir; caste lineages (sheikh/pir/murid);
      written Mishurs and debated Black Book / Book of Revelation secondary.
    stance: tradition or ancestors
    certainty: 0.7
    cites:
    - source: S2
      locator: Yazidi sacred texts
    how_known: '0.7 — Wikipedia.'
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
    rationale: "'a supreme creator god made the world and then ended his involvement with it, leaving\
      \ it in the control of seven divine beings'; the chief is Malak Ṭāʾūs."
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
    value: 1
    certainty: 0.5
    cites:
    - source: S1
      locator: sanjaqs; Sheikh Adi
    how_known: '0.5 — peacock sanjaqs circulated; Sheikh ʿAdī divinity via metempsychosis; not a full
      miracle catalog.'
    rationale: 'B=1: ritual/power special cases present. Not 0: Britannica does not center petitionary
      miracle doctrine.'
    alternatives:
    - value: 'UNKNOWN'
      note: Named alternative if evidence too thin for B.
      cites:
      - source: S1
        locator: opening
  C_ledger:
    value: 2
    rationale: "'The breaking of divine laws is expiated by way of metempsychosis'; 'Heaven and hell are\
      \ also included in Yazīdī mythology'."
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
    rationale: 'Scriptures, hymns, and chief sheikh as supreme religious head; tradition/revelation over
      observation. Not pure revelation pole (oral + contested book dating).'
    certainty: 0.5
    cites:
    - source: S1
      locator: opening; closing
    how_known: New from authority stance; 0.5 with UNKNOWN alternative if tradition alone is judged not
      to fix D.
    alternatives:
    - value: 'UNKNOWN'
      cites:
      - source: S1
        locator: closing
      note: If 19th-c. book caveat blocks scoring.
  E_scope:
    value: 1
    certainty: 0.5
    cites:
    - source: S1
      locator: mythology; purity
    how_known: '0.5 — created separately from rest of humankind; endogamy; purity taboos vs outsiders.'
    rationale: 'E=1: in-group exceptional status in cosmogony and practice. Not 0: not only hidden miracle-exceptions;
      stated separate creation.'
    alternatives:
    - value: 0
      note: Named alternative if reading separate creation as stronger in-group exception.
      cites:
      - source: S1
        locator: mythology
    - value: 'UNKNOWN'
      note: Named alternative if scoring only this-world event exceptions (P7).
      cites:
      - source: S1
        locator: opening
epistemology:
  value: Qewls orally transmitted by clergy; esoteric community knowledge; contact with outsiders historically
    discouraged. Authenticity of published holy books debated; qewls now being collected into a written
    corpus.
  certainty: 0.7
  cites:
  - source: S2
    locator: Yazidi sacred texts
  how_known: '0.7 — Wikipedia.'
ethics:
  value: 'Religious purity (food and clothing taboos vary by community); endogamy and caste marriage rules;
    divine-law breaking expiated via metempsychosis. Elements (fire, water, air, earth) not to be polluted.'
  certainty: 0.7
  cites: *id001
  how_known: '0.7 — Wikipedia + prior Britannica.'
practice:
  ritual_and_practice:
    value: Sun-facing prayer; baptism (mor kirin) at White Spring; annual Feast of the Assembly pilgrimage
      to Lalish (tomb of Sheikh Adi); Çarşema Sor New Year; Îda Êzî; Tawûsgeran (peacock sanjaq tours);
      village tiwafs. Animal sacrifice and fasting before Îda Êzî.
    certainty: 0.7
    cites:
    - source: S2
      locator: Festivals; Customs
    how_known: '0.8 — Wikipedia.'
  community_form:
    value: 'Endogamous castes: sheikhs, pirs, murids; Mir (secular) and Baba Sheikh (religious); headquarters
      Lalish. Diaspora after persecution; Kurmanji language of liturgy.'
    certainty: 0.7
    cites:
    - source: S2
      locator: Religious organisation
    how_known: '0.8 — Wikipedia.'
science:
  historical_stance:
    value: Not a natural-science tradition. Avoidance of formal education noted historically as purity/contact
      concern.
    certainty: 0.7
    cites:
    - source: S1
      locator: purity
    how_known: "Coder's reading."
  current_stance:
    value: Not a natural-science programme. Diaspora communities engage secular education; sources read
      do not state an official science policy.
    certainty: 0.5
    cites:
    - source: S2
      locator: Purity and taboos
    how_known: '0.5 — thin.'
schools_and_variants:
- name: Iraqi / Sinjar–Lalish mainstream
  form: popular
  how_it_differs: Core community around Lalish and Sinjar; Adawiyya heritage via Sheikh Adi.
  lio_difference: Axes as scored.
  certainty: 0.7
  cites:
  - source: S2
    locator: Overview
- name: Caucasus / Armenia–Georgia diaspora streams
  form: regional
  how_it_differs: Long-settled communities; some converts to Christianity not accepted as Yazidi by others.
  lio_difference: Little axis change; endogamy pressure may ease in diaspora.
  certainty: 0.5
  cites:
  - source: S2
    locator: Purity and taboos
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Yazidi ethno-religious community; Britannica discusses persecution/diaspora more than a fixed
      headcount
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — qualitative from listed source; not a genius-rate denominator.'
v7_1_rubric:
  label: authorial v7.1 scores
  L: 7
  P: 6
  E: 4
  V: 4
  X: 2
  total: 23
  scoring_note: 'Yazidism scores moderately low due to its esoteric and oral-based nature, emphasizing
    spiritual liberation through reincarnation and angelic veneration within a monotheistic frame.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 66 and section 7 scoring notes'
revised_rubric:
  status: not started
  L:
    score: 'TODO'
    rationale: ''
  P:
    score: 'TODO'
    rationale: ''
  E:
    score: 'TODO'
    rationale: ''
  V:
    score: 'TODO'
    rationale: ''
  X:
    score: 'TODO'
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
  url: 'https://www.britannica.com/topic/Yazidi'
  accessed: '2026-10-25'
  reliability_note: 'Unsigned editors’ article (revised by Noah Tesch); full article read. P44(e): read
    in the Wayback copy (https://web.archive.org/web/20260915023031/https://www.britannica.com/topic/Yazidi);
    live page not compared (live Britannica times out from the box).'
- id: S2
  type: tertiary
  kind: encyclopedia
  citation: 'Wikipedia contributors. "Yazidism." Wikipedia. Accessed 2026-10-25.'
  url: 'https://en.wikipedia.org/wiki/Yazidism'
  accessed: '2026-10-25'
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
- 2026-10-25: adherents/estimate filled (qualitative).
- 2026-10-25: E_scope and B_cause scored at 0.5.
- 2026-10-25: Deepened from Wikipedia Yazidism (tertiary).
