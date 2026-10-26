---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 4
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S7 for Jason)
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
    summary: 'Draft (systems batch S7): filled from Goossaert, "Chinese Religion: Popular Religion", Encyclopedia
      of Religion (2005). A 3 (0.5); B 1 (0.5, alt 0); C 1 (0.5); D 1 (0.5, alt 2); E 1 (0.5, alt 0).
      v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities: family/parents/related codes, origins, remaining metaphysics, epistemology,
      ethics, practice, science, schools; add Pew 2023 S2 on folk belief/practices. LIO axes unchanged
      (A3 B1 C1 D1 E1 at 0.5). Goossaert S1 kept.'
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
    how_known: "'a scholarly construct which does not correspond to any traditional Chinese notion or\
      \ institution'."
  family:
    value: 'Chinese popular / folk religion (minjian xinyang); scholarly construct overlapping Confucian,
      Daoist, and Buddhist practice'
    certainty: 1.0
    cites:
    - &id002
      source: S1
      locator: introduction
    - &id001
      source: S2
      locator: Chinese folk religions
    how_known: 'Goossaert: scholarly construct; Pew: also called folk belief or minjian xinyang.'
  parent_traditions:
    value:
    - Shang-era shamanism / local cult
    - Ancestor veneration shared with Confucian practice
    - Syncretic uptake of Buddhist and Daoist figures
    certainty: 1.0
    cites:
    - *id001
    - *id002
    how_known: 'Pew history: folk religions from Shang shamanism; intertwine with Three Teachings.'
  related_codes:
  - code: CONFUC
    relation: overlaps
    note: Ancestor rites and filial piety permeate folk practice
  - code: TAO
    relation: overlaps
    note: 'Daoist immortals, priests, fengshui underpinnings'
  - code: BUDDH
    relation: overlaps
    note: Guanyin/Buddha incense and Hungry Ghost / Ullambana overlap
  - code: ANIM
    relation: neighbor (easily confused)
    note: 'Local spirits and ghosts, but bureaucratic pantheon is more than generic animism'
origins:
  founding_era:
    value: Recorded as early as Shang dynasty (c. 1600–1046 B.C.E.); continues as diffuse popular practice
    certainty: 1.0
    cites: &id003
    - *id001
    how_known: Pew.
  founding_region:
    value: China (and historically Chinese cultural sphere)
    certainty: 1.0
    cites: *id003
    how_known: Pew.
  founders_or_key_figures:
    value:
    - No single founder
    - 'Local deities (Mazu, Caishen, Guanyin as folk goddess)'
    - Culture heroes (Guan Yu)
    - Ancestors
    - Clerical specialists / mediums
    certainty: 1.0
    cites:
    - source: S2
      locator: Chinese folk religions
    - source: S1
      locator: Theology
    how_known: Pew names folk deities; Goossaert on clerical specialists.
  key_texts:
  - value: 'No common canon (Goossaert); practice via temples, mediums, spirit-writing, calendrical rites
      rather than a single scripture'
    certainty: 1.0
    cites:
    - source: S1
      locator: Theology; Social structures
    how_known: Goossaert.
metaphysics:
  god_nature_relation:
    value: "'the material and spiritual realms are not separate. The universe is a whole organic system';\
      \ gods are 'dead human beings endowed with exceptional ling'."
    stance: many gods within nature
    certainty: 1.0
    cites:
    - source: S1
      locator: Theology
    how_known: Encyclopedia of Religion.
  deity_personal:
    value: Personal gods and ghosts who intervene; hierarchical pantheon (Heaven/Jade Emperor in Goossaert);
      deities often deified humans or culture heroes
    stance: personal
    certainty: 1.0
    cites:
    - &id004
      source: S1
      locator: Theology
    - &id005
      source: S2
      locator: Beliefs and practices
    how_known: Goossaert Theology; Pew deity worship.
  intervention:
    value: Miracles and answered prayers as ling; ghosts can cause illness/accidents; efficacy (ling/lingyan)
      drives which gods people approach
    stance: regular
    certainty: 1.0
    cites:
    - *id004
    - *id005
    how_known: Goossaert; Pew on efficacy.
  miracles:
    value: Affirmed as manifestations of ling (efficacious response)
    stance: affirmed
    certainty: 1.0
    cites: &id006
    - *id004
    how_known: Goossaert.
  petition_and_prayer:
    value: Burning incense and making wishes (xuyuan); offerings of food and spirit money; contractual
      cult relations
    stance: petition answered
    certainty: 1.0
    cites:
    - *id005
    - *id004
    how_known: Pew; Goossaert.
  afterlife:
    value: Ancestors and ghosts continue; Hungry Ghost / Lunar July visits; post-mortem courts of hell
      in Goossaert’s account of retribution
    stance: personal afterlife
    certainty: 0.7
    cites:
    - *id004
    - *id005
    how_known: Combined Goossaert hell courts and Pew ghost month. 0.7 (rebirth vs personal judgment mix).
  moral_ledger:
    value: "'actions carry retribution (conceived either as automatic karma accounting, or, more often,\
      \ as a post-mortem judicial process administered in courts of hell)'."
    stance: personal reward and punishment
    certainty: 1.0
    cites:
    - source: S1
      locator: Theology
    how_known: Encyclopedia of Religion.
  authority:
    value: 'No common canon; spirit-writing, mediums, divination; theology entrusted to clerical specialists;
      practice often lay and local'
    stance: tradition or ancestors
    certainty: 0.7
    cites:
    - source: S1
      locator: Theology; Social structures
    - source: S2
      locator: Beliefs and practices
    how_known: Goossaert; Pew on ancestors/local temples. Alt D=2 already on axis. 0.7.
  reserved_exemptions:
    value: Cults are reciprocal and often exclusive between a community and a deity; not a universalist
      exemption doctrine in the sources read
    stance: some
    certainty: 0.5
    cites: *id006
    how_known: Aligned with E=1 coding; 0.5.
  teleology_in_nature:
    value: Organic universe; fate (ming) and fortune (yun); fengshui harmony of persons and environment
    stance: immanent ends
    certainty: 0.7
    cites:
    - *id004
    - *id005
    how_known: Goossaert organic system; Pew supernatural forces. 0.7.
  necessity_and_freedom:
    value: Ming (fate) often treated as predestined; yun (fortune) changeable via ritual and divination
      (Pew)
    certainty: 0.7
    cites: &id010
    - *id005
    how_known: Pew. 0.7.
lio_axes:
  A_locus:
    value: 3
    rationale: Gods are deified dead humans inside one organic universe; Heaven (the Jade emperor) heads
      a bureaucratic pantheon.
    certainty: 0.5
    cites:
    - source: S1
      locator: Theology
    how_known: '0.5: as EPICUR and JAIN, gods within nature fit 3.'
  B_cause:
    value: 1
    rationale: "'Miracles and the answering of prayers are manifestations of ling'; ghosts 'can cause\
      \ illnesses and accidents'."
    certainty: 0.5
    cites: &id007
    - source: S1
      locator: Theology
    how_known: "0.5: frequent intervention within one cosmology that evolves 'according to known rules'.\
      \ Alternative 0."
    alternatives:
    - value: 0
      note: Named alternative.
      cites: *id007
  C_ledger:
    value: 1
    rationale: Retribution mostly by a post-mortem judicial process in courts of hell; sometimes automatic
      karma.
    certainty: 0.5
    cites:
    - source: S1
      locator: Theology
    how_known: '0.5: mostly personal judgment.'
  D_authority:
    value: 1
    rationale: "No common canon; spirit-writing revelations, mediums and divination; theology 'entrusted\
      \ to clerical specialists'."
    certainty: 0.5
    cites: &id008
    - source: S1
      locator: Theology; Social structures
    how_known: '0.5. Alternative 2.'
    alternatives:
    - value: 2
      note: Named alternative.
      cites: *id008
  E_scope:
    value: 1
    rationale: "On the world's order (P7): 'All cults are reciprocal, contractual relations between a\
      \ human community and a deity'; some gods help devotees 'in an exclusive relationship'."
    certainty: 0.5
    cites: &id009
    - source: S1
      locator: Theology
    how_known: '0.5. Alternative 0.'
    alternatives:
    - value: 0
      note: Named alternative.
      cites: *id009
epistemology:
  value: 'Efficacy (ling): gods and rites are judged by whether requests are answered; divination, mediumship,
    and spirit-writing as knowledge channels; no single scriptural test.'
  certainty: 1.0
  cites:
  - *id005
  - *id004
  how_known: Pew efficacy; Goossaert mediums/spirit-writing.
ethics:
  value: Filial piety and proper ancestor care; reciprocal obligations with deities; improper neglect
    of ancestors yields wandering ghosts and punishment (Pew/Goossaert).
  certainty: 1.0
  cites:
  - *id005
  - *id004
  how_known: Pew filial piety section; Goossaert retribution.
practice:
  ritual_and_practice:
    value: 'Ancestor gravesite rites, incense and wishes, Hungry Ghost / Ghost Festival offerings, auspicious
      days, fengshui, lucky charms; temple and home practice'
    certainty: 1.0
    cites: *id010
    how_known: Pew.
  community_form:
    value: 'Diffuse family, village, and temple cults rather than membership churches; low formal affiliation
      vs high practice rates (Pew)'
    certainty: 1.0
    cites:
    - &id011
      source: S2
      locator: Affiliation
    how_known: Pew affiliation.
science:
  historical_stance:
    value: Modern Chinese elites and states often labeled folk practice mixin (superstition) vs zongjiao;
      campaigns against superstition in Republican and PRC periods
    certainty: 1.0
    cites:
    - source: S2
      locator: 'History of Confucianism, Taoism and folk religions in China'
    how_known: Pew history section.
  current_stance:
    value: 'Some practices (fengshui, Mazu) tolerated as custom; folk religion not one of five official
      PRC religions; practitioners may treat fengshui as science or hire Daoist priests'
    certainty: 1.0
    cites: *id010
    how_known: Pew.
schools_and_variants:
- name: Local deity and earth-god cults
  form: popular
  how_it_differs: 'Tutelage gods, Mazu, Caishen, local shrines — core of what surveys call folk religion'
  lio_difference: Axes already coded for this diffuse form
  certainty: 1.0
  cites: *id003
- name: Ancestor-focused practice
  form: popular
  how_it_differs: Gravesite rites and Ghost Festival; overlaps Confucian xiao
  lio_difference: Does not by itself move LIO off current scores
  certainty: 1.0
  cites: *id010
- name: Syncretic temple practice (Buddhist/Daoist figures)
  form: popular
  how_it_differs: 'Guanyin, Buddha incense, immortals housed with folk deities'
  lio_difference: Coding risk of BUDDH/TAO — use CHNFOLK when folk frame dominates
  certainty: 1.0
  cites: *id010
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: 'Formal folk-religion identity ~3% in 2018 CGSS, but far more Chinese adults engage related
      practices (gravesite visits, incense, fengshui, auspicious days)'
    certainty: 1.0
    cites:
    - *id011
    - *id005
    how_known: Pew affiliation and practice statistics.
    year: 2018
    scope: Mainland China (CGSS/CFPS as reported by Pew)
v7_1_rubric:
  label: authorial v7.1 scores
  L: 8
  P: 8
  E: 6
  V: 6
  X: 4
  total: 32
  scoring_note: 'Chinese Folk Religion scores moderately due to its flexible syncretism for daily life
    and harmony, blending traditions effectively but constrained by supernatural elements and cultural
    authority over empirical rigor.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 42 and section 7 scoring notes'
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
  use_when: The person practised Chinese local cults and ancestor rites as their own religion.
  do_not_use_when: 'Institutional Confucians are CONFUC, Buddhists BUDDH, Daoists TAO.'
  neighbors:
  - code: CONFUC
    relation: neighbor (easily confused)
    note: Institutional/scholarly Confucians → CONFUC
  - code: TAO
    relation: neighbor (easily confused)
    note: Ordained Daoist identity → TAO
  - code: BUDDH
    relation: neighbor (easily confused)
    note: Buddhist identity with monastery frame → BUDDH
review:
  data_quality_flags: []
  open_questions:
  - When does incense-to-Buddha practice tip from CHNFOLK into BUDDH for person coding?
  - Should Taiwan / diaspora folk religion be the same code without regional variant notes?
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Vincent Goossaert
  year: 2005
  citation: 'Goossaert, Vincent. "Chinese Religion: Popular Religion." In Encyclopedia of Religion, 2nd
    ed., edited by Lindsay Jones. Detroit: Macmillan Reference USA, 2005. Online at Encyclopedia.com.'
  url: 'https://www.encyclopedia.com/environment/encyclopedias-almanacs-transcripts-and-maps/chinese-religion-popular-religion'
  accessed: '2026-10-25'
  reliability_note: 'Signed scholarly encyclopedia entry (Encyclopedia of Religion, 2nd ed.), read in
    the Encyclopedia.com copy. Britannica has no full article on Chinese religion.'
- id: S2
  type: secondary
  kind: institutional page
  author: Pew Research Center
  year: 2023
  citation: 'Pew Research Center. "Confucianism, Taoism and Chinese folk religions." In Measuring Religion
    in China, August 30, 2023. https://www.pewresearch.org/religion/2023/08/30/confucianism-taoism-and-chinese-folk-religions/.'
  url: 'https://www.pewresearch.org/religion/2023/08/30/confucianism-taoism-and-chinese-folk-religions/'
  accessed: '2026-10-25'
  reliability_note: 'Research-center survey synthesis with cited Chinese surveys (CGSS, CFPS, CLDS). Lane
    A public record.'
---
# Chinese Folk Religion (Shenism) (CHNFOLK)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

Chinese popular religion is a scholarly construct for a diffuse system of local cults, ancestor rites, and deity/ghost practice [S1]. Pew also calls it folk belief or *minjian xinyang*, recorded from the Shang dynasty and deeply intertwined with Confucian, Daoist, and Buddhist elements [S2]. Formal affiliation is rare; practice (gravesite visits, incense, fengshui, auspicious days) is much more common [S2].

## Core metaphysics

Material and spiritual realms are not separate; the universe is an organic system; gods are often deified humans with *ling* [S1]. Petition and miracle are affirmed as efficacious response; ghosts intervene; retribution via hell courts or karma [S1]. Pew stresses efficacy (*ling*/*lingyan*) and contractual, need-based engagement with gods [S2].

## Position on the LIO axes

- **A 3** (0.5) — gods within one organic universe [S1].
- **B 1** (0.5, alt 0) — frequent *ling* intervention [S1].
- **C 1** (0.5) — mostly personal post-mortem judgment [S1].
- **D 1** (0.5, alt 2) — mediums, spirit-writing, no common canon [S1].
- **E 1** (0.5, alt 0) — reciprocal/exclusive cult relations [S1].

## Schools and variants

Local deity cults; ancestor-focused practice; syncretic temples housing Buddhist/Daoist figures [S2].

## Science

Modern elites often classed folk practice as *mixin* (superstition) versus *zongjiao*; PRC does not list folk religion among five official religions [S2].

## Coding guidance

Local cults and ancestor rites as the person’s own religion. Institutional Confucians → CONFUC; ordained Daoists → TAO; Buddhist identity → BUDDH.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> Chinese Folk Religion scores moderately due to its flexible syncretism for daily life and harmony, blending traditions effectively but constrained by supernatural elements and cultural authority over empirical rigor.

## Open questions

- When does incense-to-Buddha practice tip from CHNFOLK into BUDDH for person coding?
- Should Taiwan / diaspora folk religion be the same code without regional variant notes?

## Research log

- 2026-10-01: stub created.
- 2026-10-15 (systems batch S7): filled from Goossaert Encyclopedia of Religion; LIO scored at 0.5.
- 2026-10-25: deepened TODOs; added Pew 2023 S2; LIO unchanged.
