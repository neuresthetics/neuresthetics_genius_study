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
    summary: 'Draft (systems batch S11): filled from Britannica "Zoroastrianism" (Duchesne-Guillemin),
      introduction, Beliefs and mythology, and Cosmology pages. A 1 (0.5, alt 0); C 0 (0.7, alt 1); B,
      D, E UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'T1: B_cause searched, still UNKNOWN; search logged.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from Britannica Zoroastrianism (Duchesne-Guillemin): Ahura Mazdā vs Angra
      Mainyu, free choice, Avesta, Parsis. Keep prior axis scores.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Fill adherents/estimate gloss from existing sources (order-of-magnitude / qualitative). Axes
      unchanged.
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score D_authority 0 (0.7) and B_cause 1 (0.7) from Britannica Zoroastrianism (Gāthās/Avesta
      revelation; cosmic dualistic struggle). C already 0.
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
      locator: opening
    how_known: Britannica.
  family:
    value: 'Zoroastrianism: ancient Iranian religion of Zarathushtra; Ahura Mazdā; dualistic struggle
      with Angra Mainyu; Avesta'
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; beliefs FAQ
    how_known: Britannica.
  parent_traditions:
    value:
    - Pre-Zoroastrian Iranian / Indo-Iranian polytheism
    - "Zarathushtra's reformation elevating Ahura Mazdā"
    certainty: 1.0
    cites:
    - source: S1
      locator: pre-Zoroastrian; reformation
    how_known: Britannica.
  related_codes:
  - code: CLASS_THEISM
    relation: overlaps
    note: supreme creator with dualistic twist
  - code: JUDA
    relation: neighbor (easily confused)
    note: 'possible influence, not identity'
  - code: CHRIST
    relation: neighbor (easily confused)
    note: 'influence thesis, not identity'
origins:
  founding_era:
    value: Zarathushtra flourished before the 6th century BCE (traditional); eastern Iran before Cyrus
    certainty: 0.7
    cites:
    - source: S1
      locator: opening; reformation
    how_known: Dating uncertain.
  founding_region:
    value: Ancient Iran; survives in Iran and among Parsis in India
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  founders_or_key_figures:
    value:
    - Zarathushtra / Zoroaster
    - Vishtāspa (protector in tradition)
    - Magi (Achaemenid priestly role)
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; Magi
    how_known: Britannica.
  key_texts:
  - value: Avesta (includes Gāthās)
    certainty: 1.0
    cites:
    - source: S1
      locator: beliefs FAQ
    how_known: Britannica.
metaphysics:
  god_nature_relation:
    value: Ahura Mazdā creator in primeval battle with Angra Mainyu; monotheistic and dualistic; good
      assured of triumph; omnipotence temporarily limited.
    stance: creator distinct from creation
    certainty: 0.7
    cites:
    - source: S1
      locator: nature; beliefs FAQ
    how_known: Britannica.
  deity_personal:
    value: Ahura Mazdā as wise Lord; Amesha Spentas; later Mithra/Anahita.
    stance: personal
    certainty: 1.0
    cites:
    - source: S1
      locator: reformation
    how_known: Britannica.
  intervention:
    value: Cosmic dualistic struggle enlisting humans.
    stance: regular
    certainty: 0.7
    cites:
    - source: S1
      locator: nature
    how_known: Britannica.
  miracles:
    value: Not the internal focus.
    stance: not addressed
    certainty: 0.5
    cites:
    - source: S1
      locator: nature
    how_known: Thin.
  petition_and_prayer:
    value: Fire cult; ritual purity; petition mechanics thin in extract.
    stance: not addressed
    certainty: 0.5
    cites:
    - source: S1
      locator: nature
    how_known: Thin.
  afterlife:
    value: "Evil's followers suffer then all humanity eternal bliss after Ahura Mazdā's victory."
    stance: personal afterlife
    certainty: 0.7
    cites:
    - source: S1
      locator: beliefs FAQ
    how_known: Britannica.
  moral_ledger:
    value: "Free choice enlistment; eventual suffering for evil's followers."
    stance: personal reward and punishment
    certainty: 0.7
    cites:
    - source: S1
      locator: nature; beliefs FAQ
    how_known: Britannica.
  authority:
    value: "Prophet Zarathushtra's Gāthās / Avesta; Magi historically."
    stance: revelation
    certainty: 0.7
    cites:
    - source: S1
      locator: opening; Magi
    how_known: Britannica.
  reserved_exemptions:
    value: Not addressed.
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: Silence.
  teleology_in_nature:
    value: Cosmic struggle toward triumph of good; purity vs defilement.
    stance: "designer's purposes"
    certainty: 0.5
    cites:
    - source: S1
      locator: nature
    how_known: '0.5.'
  necessity_and_freedom:
    value: Humans enlist by capacity for free choice; soul and body.
    certainty: 1.0
    cites:
    - source: S1
      locator: nature
    how_known: Britannica.
lio_axes:
  A_locus:
    value: 1
    rationale: "'unifying under the worship of one supreme god'; in the Vidēvdāt 'Ahura Mazdā and the\
      \ Destructive Spirit opposed each other by creating, respectively, the good and the bad things'."
    certainty: 0.5
    cites: &id001
    - source: S1
      locator: Nature and significance
    - source: S2
      locator: God
    how_known: '0.5: a creator god opposed by an antigod; dualism and the later pantheon give alternative
      0 or 2. Alternative 0.'
    alternatives:
    - value: 0
      note: Named alternative.
      cites: *id001
  B_cause:
    value: 1
    certainty: 0.7
    cites:
    - source: S1
      locator: dualism; cosmic struggle
    how_known: '0.7 — cosmic dualistic struggle enlisting humans; intervention regular.'
    rationale: 'B=1: special cosmic struggle / divine enlistment. Not 0: not only petitionary miracle
      catalog.'
    alternatives:
    - value: 0
      note: Named alternative if coding Ahura Mazdā interventions as miracle-class 0.
      cites:
      - source: S1
        locator: opening
  C_ledger:
    value: 0
    rationale: "The soul crosses 'the Bridge of the Requiter. It leads the good souls to paradise, but\
      \ the bad ones fall into hell'; 'The soul has also to undergo a judgment; it appears before Mithra\
      \ and his two companions'."
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
    value: 0
    certainty: 0.7
    cites:
    - source: S1
      locator: Zarathushtra; Avesta
    how_known: '0.7 — prophet Zarathushtra’s Gāthās / Avesta; stance revelation.'
    rationale: 'D=0: revelation outranks. Not 1: prophetic scripture, not open ancestral custom alone.'
    alternatives:
    - value: 1
      note: Named alternative if coding Magi tradition as co-equal.
      cites:
      - source: S1
        locator: Magi
  E_scope:
    value: 'UNKNOWN'
    how_known: Not addressed in the sources read.
epistemology:
  value: Prophetic revelation (Gāthās); Avesta; Magi interpretation.
  certainty: 1.0
  cites:
  - source: S1
    locator: opening; Magi
  how_known: Britannica.
ethics:
  value: Lofty rational ethics with ritual purity; fasting/celibacy proscribed except purificatory ritual;
    optimistic.
  certainty: 1.0
  cites:
  - source: S1
    locator: nature
  how_known: Britannica.
practice:
  ritual_and_practice:
    value: Fire cult; purity rules; temple fire; Magian customs historically.
    certainty: 1.0
    cites:
    - source: S1
      locator: nature; Magi
    how_known: Britannica.
  community_form:
    value: Iranian communities; Parsis in India; Magi historically.
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
science:
  historical_stance:
    value: External Greek link to astrology/magic; not internal science treatise.
    certainty: 0.5
    cites:
    - source: S1
      locator: nature
    how_known: External.
  current_stance:
    value: Not addressed.
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Silence.
schools_and_variants:
- name: Iranian Zoroastrian communities
  form: regional
  how_it_differs: Continuity in Iran.
  lio_difference: Prior scores.
  certainty: 1.0
  cites:
  - source: S1
    locator: opening
- name: Parsis (India)
  form: regional
  how_it_differs: '10th-c. immigrant descendants.'
  lio_difference: Same.
  certainty: 1.0
  cites:
  - source: S1
    locator: opening
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Parsi/Zoroastrian communities (India/Iran/diaspora); tens to hundreds of thousands (order-of-magnitude)
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
  scoring_note: 'Zoroastrianism scores moderately low due to its revelatory dualism and limited empirical
    alignment, though it pioneered ethical monotheism influencing later religions.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 67 and section 7 scoring notes'
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
  use_when: Zoroastrian / Parsi / Zarathushtrian identity.
  do_not_use_when: Generic dualism without Zoroastrian identity. Manichaeism (not coded here).
  neighbors:
  - code: CLASS_THEISM
    relation: neighbor (easily confused)
  - code: JUDA
    relation: neighbor (easily confused)
review:
  data_quality_flags: []
  open_questions:
  - Adherents are TODO.
  - 'T1 (2026-10-15): B_cause search logged in the research log; still UNKNOWN.'
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Jacques Duchesne-Guillemin
  citation: 'Duchesne-Guillemin, Jacques. "Zoroastrianism." Encyclopaedia Britannica. https://www.britannica.com/topic/Zoroastrianism.
    Wayback Machine snapshot 2026-01-01 12:47:08 UTC: https://web.archive.org/web/20260101124708/https://www.britannica.com/topic/Zoroastrianism.'
  url: 'https://www.britannica.com/topic/Zoroastrianism'
  accessed: '2026-10-25'
  reliability_note: 'Signed article (Indo-Iranian studies); introduction and Nature and significance read.
    Newest 2026 snapshot (20261001082722) was a bot-check page. P44(e): read in the Wayback copy (https://web.archive.org/web/20260101124708/https://www.britannica.com/topic/Zoroastrianism);
    live page not compared (live Britannica times out from the box).'
- id: S2
  type: tertiary
  kind: encyclopedia
  author: Jacques Duchesne-Guillemin
  citation: 'Duchesne-Guillemin, Jacques. "Zoroastrianism: Beliefs and mythology." Encyclopaedia Britannica.
    https://www.britannica.com/topic/Zoroastrianism/Beliefs-and-mythology. Wayback Machine snapshot 2026-07-21
    18:53:41 UTC: https://web.archive.org/web/20260721185341/https://www.britannica.com/topic/Zoroastrianism/Beliefs-and-mythology.'
  url: 'https://www.britannica.com/topic/Zoroastrianism/Beliefs-and-mythology'
  accessed: '2026-10-25'
  reliability_note: 'Later page of the same signed article. P44(e): read in the Wayback copy (https://web.archive.org/web/20260721185341/https://www.britannica.com/topic/Zoroastrianism/Beliefs-and-mythology);
    live page not compared (live Britannica times out from the box).'
- id: S3
  type: tertiary
  kind: encyclopedia
  author: Jacques Duchesne-Guillemin
  citation: 'Duchesne-Guillemin, Jacques. "Zoroastrianism: Cosmology." Encyclopaedia Britannica. https://www.britannica.com/topic/Zoroastrianism/Cosmology.
    Wayback Machine snapshot 2026-01-30 12:14:29 UTC: https://web.archive.org/web/20260130121429/https://www.britannica.com/topic/Zoroastrianism/Cosmology.'
  url: 'https://www.britannica.com/topic/Zoroastrianism/Cosmology'
  accessed: '2026-10-25'
  reliability_note: 'Later page of the same signed article. P44(e): read in the Wayback copy (https://web.archive.org/web/20260130121429/https://www.britannica.com/topic/Zoroastrianism/Cosmology);
    live page not compared (live Britannica times out from the box).'
---
# Zoroastrianism (ZORO)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

Zoroastrianism is the ancient Iranian religion of Zarathushtra: Ahura Mazdā vs Angra Mainyu, free human enlistment, Avesta; survives in Iran and among Parsis [S1].

## Core metaphysics

Monotheistic and dualistic features; good assured of triumph; free choice; purity ethics [S1].

## Position on the LIO axes

Prior scores kept (see YAML).

## Schools and variants

Iranian communities; Parsis [S1].

## Science

Not an internal science doctrine [S1].

## Coding guidance

Zoroastrian/Parsi identity.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> ZORO (23/50) — Zoroastrianism (Mazdayasna). Zoroastrianism scores moderately low due to its revelatory dualism and limited empirical alignment, though it pioneered ethical monotheism influencing later religions.

## Open questions

- Amesha Spentas / eschatology for C-axis refinement.

## Research log

- 2026-10-15 (batch S11): Britannica Zoroastrianism; axes set.
- 2026-10-25: deepened classification, origins, metaphysics, ethics, practice. Axes kept.
- 2026-10-25: adherents/estimate filled (qualitative).
- 2026-10-25: D/B scored.
