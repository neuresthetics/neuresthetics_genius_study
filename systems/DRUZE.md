---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 5
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
    - Eclectic elements noted historically (Jewish, Christian, Gnostic, Neoplatonic, Iranian) under strict
      monotheism — detail thin in this Britannica article
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
    value: Strict monotheism; self-name muwaḥḥidūn ('unitarians'). Movement proclaimed al-Ḥākim a divine
      figure (condemned as heresy by Fatimid establishment, which held caliphs divinely appointed but
      not themselves divine).
    stance: creator distinct from creation
    certainty: 0.5
    cites:
    - source: S1
      locator: opening; Origins and practices
    how_known: Unitarian monotheism is clear; classical creator/creation framing is coder gloss at 0.5
      — fuller hikmah cosmology not in Britannica.
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
    value: Not addressed in the Britannica sections read.
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: Origins and practices
    how_known: Britannica silence.
  petition_and_prayer:
    value: Religious services for ʿuqqāl initiates; practices largely secret. Petition theology not described.
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: Origins and practices
    how_known: Britannica.
  afterlife:
    value: Not described in the Britannica article read (v7.1 note mentions reincarnation; that claim
      is not sourced here — leave not addressed).
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: full article used
    how_known: Britannica silence on reincarnation in the fetched text; do not invent from v7.1 note.
  moral_ledger:
    value: Not described in the source read.
    stance: none
    certainty: 0.5
    cites:
    - source: S1
      locator: full article used
    how_known: Silence; 'none' means no ledger doctrine stated, not a positive denial.
  authority:
    value: Secret teachings of Al-Ḥikmah al-sharīfah; elite initiates (ʿuqqāl) alone have full access.
      Founding missionaries and pastoral letters of al-Muqtanā. Revelation/esoteric scripture, not public
      observation-and-reason.
    stance: revelation
    certainty: 0.7
    cites:
    - source: S1
      locator: Origins and practices
    how_known: Coder's reading of Britannica on hikmah and ʿuqqāl.
  reserved_exemptions:
    value: Not addressed as cosmology of natural-law exemptions. Taqiyyah (outward denial under persecution)
      is a social concession noted in older reference material, not developed here.
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: Origins and practices
    how_known: Britannica silence on physics exemptions.
  teleology_in_nature:
    value: Not addressed.
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: full article used
    how_known: Britannica silence.
  necessity_and_freedom:
    value: Not addressed in the source read.
    certainty: 1.0
    cites:
    - source: S1
      locator: full article used
    how_known: Britannica silence.
lio_axes:
  A_locus:
    value: UNKNOWN
    how_known: Britannica establishes unitarian monotheism, al-Ḥākim's divinity claim, and secret hikmah,
      but lacks the reincarnation/cosmology detail needed to score LIO under P44. Stay unscored (P46(a)).
  B_cause:
    value: UNKNOWN
    how_known: Britannica establishes unitarian monotheism, al-Ḥākim's divinity claim, and secret hikmah,
      but lacks the reincarnation/cosmology detail needed to score LIO under P44. Stay unscored (P46(a)).
  C_ledger:
    value: UNKNOWN
    how_known: Britannica establishes unitarian monotheism, al-Ḥākim's divinity claim, and secret hikmah,
      but lacks the reincarnation/cosmology detail needed to score LIO under P44. Stay unscored (P46(a)).
  D_authority:
    value: UNKNOWN
    how_known: Britannica establishes unitarian monotheism, al-Ḥākim's divinity claim, and secret hikmah,
      but lacks the reincarnation/cosmology detail needed to score LIO under P44. Stay unscored (P46(a)).
  E_scope:
    value: UNKNOWN
    how_known: Britannica establishes unitarian monotheism, al-Ḥākim's divinity claim, and secret hikmah,
      but lacks the reincarnation/cosmology detail needed to score LIO under P44. Stay unscored (P46(a)).
epistemology:
  value: 'Esoteric: only ʿuqqāl (''knowers'') fully access Al-Ḥikmah al-sharīfah. Ordinary members do
    not. Conversion closed since 1043.'
  certainty: 1.0
  cites:
  - source: S1
    locator: Origins and practices
  how_known: Britannica.
ethics:
  value: Not developed as a public ethical system in Britannica. Community cohesion, endogamy, and political
    loyalty are emphasized historically.
  certainty: 0.7
  cites:
  - source: S1
    locator: opening; Origins and practices
  how_known: Coder's reading.
practice:
  ritual_and_practice:
    value: Many religious practices kept secret even from the community as a whole; full participation
      reserved for ʿuqqāl. No conversion in or out; intermarriage rare and discouraged.
    certainty: 1.0
    cites:
    - source: S1
      locator: Origins and practices
    how_known: Britannica.
  community_form:
    value: Close-knit hereditary community in Lebanon, Syria, and Israel (plus smaller diasporas); politically
      significant; >1,000,000 early 21st century per Britannica.
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; History sections
    how_known: Britannica.
science:
  historical_stance:
    value: Not a natural-science tradition. Esoteric scripture and initiate knowledge.
    certainty: 0.7
    cites:
    - source: S1
      locator: Origins and practices
    how_known: Coder's reading.
  current_stance:
    value: Not addressed as a science stance in Britannica.
    certainty: 1.0
    cites:
    - source: S1
      locator: full article used
    how_known: Britannica silence.
schools_and_variants:
- name: ʿuqqāl (initiate knowers) vs ordinary members
  form: other
  how_it_differs: Only ʿuqqāl fully access hikmah and services; not separate denominations.
  lio_difference: Axes UNKNOWN for the community as a whole.
  certainty: 1.0
  cites:
  - source: S1
    locator: Origins and practices
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
  scoring_note: Druze Faith scores moderately low due to its esoteric and revelatory focus, though it
    provides a cohesive framework for monotheism and reincarnation within a secretive tradition.
  source: v7.1 data book, section 6 table (tables[4]) row 64 and section 7 scoring notes
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
  - 'Thin: little doctrine in the source (al-Ḥākim''s divinity and the self-name ''unitarians'' only);
    teachings are secret. All axes UNKNOWN.'
  open_questions:
  - 'A lead: the movement began by ''proclaiming al-Ḥākim a divine figure'' and the Druze call themselves
    ''unitarians'' (S1); a doctrinal source is needed to say what this implies for A.'
  - A signed or peer-reviewed source on Druze doctrine (unity of God, reincarnation).
  - 'Adherents: Britannica says more than 1,000,000 (early 21st century); cite a demographic source.'
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Britannica Editors
  citation: 'The Editors of Encyclopaedia Britannica. "Druze." Encyclopaedia Britannica. https://www.britannica.com/topic/Druze.
    Wayback Machine snapshot 2026-01-09 03:32:33 UTC: https://web.archive.org/web/20260109033233/https://www.britannica.com/topic/Druze.'
  url: https://www.britannica.com/topic/Druze
  accessed: '2026-10-25'
  reliability_note: 'Unsigned editors’ article; origins, practices and history only, no doctrine. Newest
    2026 snapshot (20260925005116) was a bot-check page. P44(e): read in the Wayback copy (https://web.archive.org/web/20260109033233/https://www.britannica.com/topic/Druze);
    live page not compared (live Britannica times out from the box).'
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
