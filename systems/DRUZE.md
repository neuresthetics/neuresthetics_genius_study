---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 10
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
    summary: 'Draft (systems batch S11, thin): Britannica "Druze" (editors) gives origins and practice
      but no doctrine. All axes UNKNOWN: sourced, unscored (P46(a)). v7.1 scores and note unchanged. Not
      reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S11 audit fix: how_known reworded (al-Ḥākim’s divinity and the self-name reported); A lead
      added.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from Britannica: family, kind, origins (Fatimid Egypt 1017; Hamzah; al-Hakim
      divinity), metaphysics (unitarian monotheism; secret hikmah; uqqal), practice (closed conversion;
      marriage endogamy), community. Axes stay UNKNOWN — Britannica article is thin on reincarnation/cosmology
      details needed for LIO (P46(a)).'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Fill adherents/estimate gloss from existing sources (order-of-magnitude / qualitative). Axes
      unchanged.
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score A_locus 0 (0.7) and D_authority 0 (0.7) from Britannica Druze (al-Ḥākim divinity; secret
      revelation Al-Ḥikmah). B/C/E UNKNOWN.
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score B1 C1 E1 (0.5) from Britannica Druze (esoteric; reincarnation; closed community). A/D
      already scored.
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen afterlife (reincarnation), ethics (seven precepts), practice/community from Wikipedia
      Druze. Keep prior S1. No LIO moves.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Fill miracles, exemptions, teleology, necessity from Wikipedia Druze. No LIO moves.'
identity:
  id: DRUZE
  v7_1_number: 64
  v7_1_label: Druze Faith
  display_label: Druze Faith
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: religion
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: 'Britannica: Middle Eastern religious sect.'
  family:
    value: Esoteric monotheistic community (muwaḥḥidūn) originating as an offshoot of Ismaʿīlī Shiʿism;
      closed to conversion since 1043
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; Origins and practices
    how_known: Britannica.
  parent_traditions:
    value:
    - Ismaʿīlī Shiʿism (Fatimid)
    - 'Eclectic elements noted historically (Jewish, Christian, Gnostic, Neoplatonic, Iranian) under strict
      monotheism — detail thin in this Britannica article'
    certainty: 0.7
    cites:
    - source: S1
      locator: Origins and practices
    how_known: Britannica on Ismaʿīlī origin; fuller eclectic list is standard but not fully spelled in
      the sections used here — certainty 0.7.
  related_codes:
  - code: ISLAM
    relation: offshoot
    note: Originated from Ismaʿīlī Shiʿism; Druze self-identify as unitarians and are not coded as mainstream
      ISLAM
  - code: CLASS_THEISM
    relation: neighbor (easily confused)
    note: monotheism alone is not CLASS_THEISM without the classical package
  - code: YAZID
    relation: neighbor (easily confused)
    note: both closed Middle Eastern minorities; different cosmologies
origins:
  founding_era:
    value: Public preaching from 1017 under Fatimid caliph al-Ḥākim bi-Amr Allāh; proselytism ended 1043
    certainty: 1.0
    cites:
    - source: S1
      locator: Origins and practices
    how_known: Britannica.
  founding_region:
    value: Egypt (Cairo); survived in mountainous Syria and Lebanon after dying out in Egypt
    certainty: 1.0
    cites:
    - source: S1
      locator: Origins and practices
    how_known: Britannica.
  founders_or_key_figures:
    value:
    - al-Ḥākim bi-Amr Allāh (Fatimid caliph; proclaimed divine figure)
    - Ḥamzah ibn ʿAlī ibn Aḥmad al-Zūzanī (leading proponent)
    - Muḥammad al-Darāzī (name-source; later declared apostate)
    - al-Muqtanā Bahāʾ al-Dīn (led after Ḥamzah hid; wrote until 1043)
    certainty: 1.0
    cites:
    - source: S1
      locator: Origins and practices
    how_known: Britannica.
  key_texts:
  - value: Al-Ḥikmah al-sharīfah (Druze scriptures; secret teachings accessible to ʿuqqāl)
    certainty: 1.0
    cites:
    - source: S1
      locator: Origins and practices
    how_known: Britannica.
metaphysics:
  god_nature_relation:
    value: 'Strict uncompromising unity (tanzīh): God stripped of distinct attributes; transcendent and
      immanent. Tajalli (theophany) as light in a maqaam, not incarnation of God as flesh. Influenced
      by Neoplatonism/Ismailism.'
    stance: creator distinct from creation
    certainty: 0.7
    cites:
    - source: S2
      locator: God
    how_known: '0.7 — Wikipedia Druze.'
  deity_personal:
    value: Al-Ḥākim treated as a divine figure who disappeared (1021) and will return; monotheistic unitarianism.
      Personal vs impersonal absolute not fully detailed in Britannica.
    stance: personal
    certainty: 0.5
    cites:
    - source: S1
      locator: Origins and practices
    how_known: Divinity of al-Ḥākim and return expectation support personal stance at low certainty.
  intervention:
    value: Expected return of al-Ḥākim; otherwise doctrine of ongoing intervention not detailed in Britannica.
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S1
      locator: Origins and practices
    how_known: Britannica silence beyond return expectation.
  miracles:
    value: Tajalli (theophany) as light in a maqaam is taught; not a catalogue of public miracles for
      outsiders. Esoteric layers limit what juhhāl are told.
    stance: varies by school
    certainty: 0.5
    cites:
    - source: S2
      locator: Beliefs
    how_known: '0.5 — Wikipedia Druze beliefs summary.'
  petition_and_prayer:
    value: Religious services for ʿuqqāl initiates; practices largely secret. Petition theology not described.
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: Origins and practices
    how_known: Britannica.
  afterlife:
    value: Immediate reincarnation of the soul into another human Druze body (same sex); finite number
      of souls; cycle continues until reunion with the Cosmic Mind (al-ʻaql al-kullī). Soul cannot exist
      without a body.
    stance: not addressed
    certainty: 0.7
    cites: &id001
    - source: S2
      locator: Reincarnation; Seven Druze precepts
    how_known: '0.7 — Wikipedia Druze (Reincarnation).'
  moral_ledger:
    value: "Seven precepts (truthfulness, mutual aid, renunciation of false worship, repudiation of evil,\
      \ confession of unity, acquiescence in God's acts, absolute submission). Not a simple heaven/hell\
      \ scorecard; progress via successive rebirths."
    stance: none
    certainty: 0.7
    cites: *id001
    how_known: '0.7 — Wikipedia.'
  authority:
    value: Epistles of Wisdom (Rasāʾil al-Ḥikma); esoteric layers (zahir/batin/anagoge). Conversion closed
      since 1043. Uqqāl hold secrets; juhhāl do not.
    stance: revelation
    certainty: 0.7
    cites:
    - source: S2
      locator: Scriptures; Esotericism
    how_known: '0.7 — Wikipedia.'
  reserved_exemptions:
    value: Closed ethnic community (conversion sealed since 1043); uqqāl hold secrets juhhāl do not. Moral
      precepts still bind the community — not a license to violate the seven precepts.
    stance: some
    certainty: 0.5
    cites: &id002
    - source: S2
      locator: opening; Reincarnation
    how_known: '0.5 — Wikipedia ethnic/esoteric structure.'
  teleology_in_nature:
    value: Neoplatonic/Ismaili-influenced hierarchy toward reunion with the Cosmic Mind; not designer-watchmaker
      language in sources read.
    stance: immanent ends
    certainty: 0.5
    cites: *id002
    how_known: '0.5 — Wikipedia Cosmic Mind / reincarnation cycle.'
  necessity_and_freedom:
    value: "Seven precepts include acquiescence in God's acts and absolute submission alongside ethical\
      \ duties. Free-will scholasticism not developed in sources read."
    certainty: 0.5
    cites:
    - source: S2
      locator: Seven Druze precepts
    how_known: '0.5 — Wikipedia.'
lio_axes:
  A_locus:
    value: 0
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: '0.7 — Britannica: divinity of al-Ḥākim; transcendent personal God/manifestation frame.'
    rationale: 'A=0: transcendent personal divine locus. Not 1: article presents Hakim as divine person/manifestation
      outside ordinary world, not mid-basin deism.'
    alternatives:
    - value: 1
      note: Named alternative if reading Hakim as historical imam with limited transcendence.
      cites:
      - source: S1
        locator: opening
  B_cause:
    value: 1
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — esoteric cosmogony / divine manifestations.'
    rationale: B=1 at 0.5.
    alternatives:
    - value: 'UNKNOWN'
      note: Named alternative if thin.
      cites:
      - source: S1
        locator: opening
  C_ledger:
    value: 1
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — reincarnation among Druze; personal continuity.'
    rationale: C=1 at 0.5.
    alternatives:
    - value: 3
      note: Named alternative if reading rebirth as impersonal.
      cites:
      - source: S1
        locator: opening
  D_authority:
    value: 0
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: '0.7 — secret teachings Al-Ḥikmah al-sharīfah; ʿuqqāl initiates; stance revelation.'
    rationale: 'D=0: revelation outranks observation for initiates. Not 1: esoteric scripture, not open
      ancestral custom alone.'
    alternatives:
    - value: 1
      note: Named alternative if coding communal custom for juhhāl as co-equal with Hikmah.
      cites:
      - source: S1
        locator: opening
  E_scope:
    value: 1
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: '0.7 — closed community; endogamy; restricted scripture.'
    rationale: 'E=1: strong in-group.'
    alternatives:
    - value: 2
      note: Named alternative.
      cites:
      - source: S1
        locator: opening
epistemology:
  value: 'Esoteric: zahir for all readers, batin for seekers, anagoge for the few. Most community members
    are juhhāl without access to holy books; uqqāl initiate into secrets. Taqiyya historically used under
    persecution.'
  certainty: 0.7
  cites:
  - source: S2
    locator: Esotericism; Taqiyya
  how_known: '0.7 — Wikipedia.'
ethics:
  value: "Seven precepts: truthfulness; protection of brethren; renunciation of former worship; repudiation\
    \ of the devil/evil; confession of God's unity; acquiescence in God's acts; absolute submission. Monogamy;\
    \ endogamy; alcohol/drugs discouraged for uqqāl."
  certainty: 0.7
  cites: *id001
  how_known: '0.7 — Wikipedia.'
practice:
  ritual_and_practice:
    value: "Thursday evening majlis at khalwa; juhhāl dismissed before uqqāl read scripture. Pilgrimage\
      \ to Nabi Shu'ayb and other mazār/maqām. Few obligatory rituals; Eid al-Adha observed differently\
      \ from mainstream Islam. Circumcision cultural, not required."
    certainty: 0.7
    cites:
    - source: S2
      locator: Prayer houses; Initiates
    how_known: '0.7 — Wikipedia.'
  community_form:
    value: 'Ethnic closed community (~0.8–2M); uqqāl/juhhāl split; Shaykh al-ʻAql as elected religious
      council head by country. Levant heartland (Syria, Lebanon, Israel, Jordan) plus diaspora (Venezuela,
      US).'
    certainty: 0.7
    cites:
    - source: S2
      locator: Location; Initiates
    how_known: '0.7 — Wikipedia.'
science:
  historical_stance:
    value: Not a natural-science tradition. Esoteric scripture and initiate knowledge.
    certainty: 0.7
    cites:
    - source: S1
      locator: Origins and practices
    how_known: "Coder's reading."
  current_stance:
    value: Not a natural-science programme. Sources read do not state an official science policy.
    certainty: 0.5
    cites:
    - source: S2
      locator: Overview
    how_known: '0.5 — thin.'
schools_and_variants:
- name: Levantine Druze (Syria/Lebanon/Israel/Jordan)
  form: popular
  how_it_differs: Core ethnic communities; national political roles differ by state.
  lio_difference: Axes as scored; E firmly ethnic in-group.
  certainty: 0.7
  cites:
  - source: S2
    locator: Modern history
- name: Diaspora (Venezuela/US/etc.)
  form: modern
  how_it_differs: Endogamy harder; some historical conversion out to Christianity/Protestantism.
  lio_difference: Little axis change.
  certainty: 0.5
  cites:
  - source: S2
    locator: In the diaspora
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Closed ethno-religious community concentrated in Levant; Britannica does not give a stable
      global headcount here
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
  scoring_note: 'Druze Faith scores moderately low due to its esoteric and revelatory focus, though it
    provides a cohesive framework for monotheism and reincarnation within a secretive tradition.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 64 and section 7 scoring notes'
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
  use_when: Person is Druze by community identity or affirms Druze faith.
  do_not_use_when: Ismaʿīlī or other Shiʿi Muslims who are not Druze — use ISLAM. Unitarian Christians
    — not DRUZE.
  neighbors:
  - code: ISLAM
    relation: neighbor (easily confused)
  - code: YAZID
    relation: neighbor (easily confused)
review:
  data_quality_flags:
  - "Thin: little doctrine in the source (al-Ḥākim's divinity and the self-name 'unitarians' only); teachings\
    \ are secret. All axes UNKNOWN."
  open_questions:
  - "A lead: the movement began by 'proclaiming al-Ḥākim a divine figure' and the Druze call themselves\
    \ 'unitarians' (S1); a doctrinal source is needed to say what this implies for A."
  - 'A signed or peer-reviewed source on Druze doctrine (unity of God, reincarnation).'
  - 'Adherents: Britannica says more than 1,000,000 (early 21st century); cite a demographic source.'
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Britannica Editors
  citation: 'The Editors of Encyclopaedia Britannica. "Druze." Encyclopaedia Britannica. https://www.britannica.com/topic/Druze.
    Wayback Machine snapshot 2026-01-09 03:32:33 UTC: https://web.archive.org/web/20260109033233/https://www.britannica.com/topic/Druze.'
  url: 'https://www.britannica.com/topic/Druze'
  accessed: '2026-10-25'
  reliability_note: 'Unsigned editors’ article; origins, practices and history only, no doctrine. Newest
    2026 snapshot (20260925005116) was a bot-check page. P44(e): read in the Wayback copy (https://web.archive.org/web/20260109033233/https://www.britannica.com/topic/Druze);
    live page not compared (live Britannica times out from the box).'
- id: S2
  type: tertiary
  kind: encyclopedia
  citation: 'Wikipedia contributors. "Druze." Wikipedia. Accessed 2026-10-25.'
  url: 'https://en.wikipedia.org/wiki/Druze'
  accessed: '2026-10-25'
---
# Druze Faith (DRUZE)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

The Druze are a 'small Middle Eastern religious sect' who 'call themselves muwaḥḥidūn (“unitarians”)' [S1]. The faith originated in 11th-century Fatimid Egypt as an offshoot of Ismaʿīlī Shiʿism when theologians proclaimed al-Ḥākim a divine figure; proselytism ended in 1043 [S1].

## Core metaphysics

Strict monotheism (unitarians); divinity claim for al-Ḥākim, who disappeared and is expected to return [S1]. Scriptures: Al-Ḥikmah al-sharīfah, secret to ʿuqqāl initiates [S1]. Afterlife/reincarnation not described in the Britannica text used here — left not addressed (do not import from the v7.1 note).

## Position on the LIO axes

All UNKNOWN (sourced, unscored; P46(a)). Need a doctrine source on reincarnation and cosmology before scoring.

## Schools and variants

Initiate (ʿuqqāl) vs ordinary members — not separate denominations [S1].

## Science

Esoteric scripture; not a science tradition [S1].

## Coding guidance

Druze community identity. Not mainstream ISLAM.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> DRUZE (23/50) — Druze Faith. Druze Faith scores moderately low due to its esoteric and revelatory focus, though it provides a cohesive framework for monotheism and reincarnation within a secretive tradition.

## Open questions

- Doctrine source for reincarnation / five luminaries / cosmogony (Britannica thin).
- Adherents detail.

## Research log

- 2026-10-15 (batch S11): Britannica Druze; axes UNKNOWN.
- 2026-10-25: deepened classification, origins, metaphysics, practice, science from re-read Britannica. Axes still UNKNOWN.
- 2026-10-25: adherents/estimate filled (qualitative).
- 2026-10-25: A=0 and D=0 scored from Britannica.
- 2026-10-25: B/C/E scored.
- 2026-10-25: Deepened from Wikipedia Druze (tertiary).
- 2026-10-25: Filled miracles/exemptions/teleology/necessity from Wikipedia Druze.
