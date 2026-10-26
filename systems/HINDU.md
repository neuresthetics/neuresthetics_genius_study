---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 9
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S8 for Jason)
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
    summary: 'Draft (systems batch S8): filled from Britannica "Hinduism" (Narayanan) and IEP "Hindu Philosophy"
      (Ranganathan). A, D BELOW_THRESHOLD; C 3 (0.5, alt 4, P44(d)); B, E UNKNOWN. v7.1 scores and note
      unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'P44(e) compliance (with the S7 fixes): Wayback snapshot URL and timestamp cited.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S8 audit fix: C 3 @0.5 -> BELOW_THRESHOLD (alt 3).'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'T1: B_cause searched, still UNKNOWN; search logged.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'T1 audit fix: avatar doctrine recorded as a lead for B; B stays UNKNOWN.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from Britannica Hinduism (Narayanan) + IEP Hindu Philosophy (Ranganathan):
      family/parents, metaphysics TODOs as varies, epistemology/ethics/practice/science/schools (darśanas).
      Axes unchanged.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score C_ledger 3 (0.5) karma rule P44(d) from Britannica/IEP (impersonal moral-causal law).
      Was BELOW_THRESHOLD. A/D stay BELOW.
identity:
  id: HINDU
  v7_1_number: 47
  v7_1_label: Hinduism (Sanatana Dharma)
  display_label: Hinduism (Sanatana Dharma)
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: religion
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: Britannica.
  family:
    value: Cumulative Vedic-linked traditions; no single shared comprehensive doctrine; textual openness
      to Vedas as working definition of Hindu philosophy
    certainty: 1.0
    cites:
    - source: S2
      locator: §1.b
    how_known: IEP.
  parent_traditions:
    value:
    - Vedic / śruti corpus
    - 'Smṛti (epics, Purāṇas, dharmaśāstra)'
    - Six āstika darśanas
    - Neo-Hindu / Vedānta reformulations
    certainty: 1.0
    cites:
    - source: S2
      locator: introduction; §3
    how_known: IEP.
  related_codes:
  - code: BUDDH
    relation: neighbor (easily confused)
    note: Shared Indian milieu; different textual stance
  - code: JAIN
    relation: neighbor (easily confused)
    note: Shared karma/rebirth vocabulary; independent
  - code: SIKH
    relation: neighbor (easily confused)
    note: Later Indic; distinct
origins:
  founding_era:
    value: Texts and practices from the 2nd millennium BCE or earlier
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: Britannica.
  founding_region:
    value: Indian subcontinent
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: Britannica.
  founders_or_key_figures:
    value:
    - No single founder
    - Śaṅkara (Advaita)
    - Rāmānuja (Viśiṣṭādvaita)
    - Madhva (Dvaita)
    - Patañjali (Yoga)
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    - source: S2
      locator: §3.f
    how_known: Britannica + IEP.
  key_texts:
  - value: Vedas (incl. Upaniṣads); Bhagavad Gītā; Brahma/Vedānta Sūtras; smṛti epics and Purāṇas
    certainty: 1.0
    cites:
    - source: S2
      locator: §2
    how_known: IEP.
metaphysics:
  god_nature_relation:
    value: 'Varies widely: polytheism/sectarian monotheism; Vedānta Brahman=Ātman debates; Neo-Hindu impersonal
      Ultimate'
    stance: varies by school
    certainty: 1.0
    cites:
    - source: S2
      locator: §1.a.ii; §3.f
    how_known: IEP.
  deity_personal:
    value: 'Personal deities (Viṣṇu, Śiva, Devī) and impersonal nirguṇa Brahman both attested'
    stance: varies by school
    certainty: 1.0
    cites:
    - source: S2
      locator: §3.f.iii–v
    how_known: IEP.
  intervention:
    value: 'Avatars, grace, and ritual efficacy vary by school; Brahman as source/support of cosmos in
      Upaniṣadic streams'
    stance: varies by school
    certainty: 0.7
    cites:
    - source: S2
      locator: §2.a.ii; §3.f
    how_known: '0.7.'
  miracles:
    value: Purāṇic/epic wonders; not a single miracle doctrine
    stance: varies by school
    certainty: 0.7
    cites:
    - source: S2
      locator: §2.b
    how_known: '0.7.'
  petition_and_prayer:
    value: 'Sacrifice, bhakti, mantra, temple worship widespread; Pūrvamīmāṃsā emphasizes Vedic injunction'
    stance: petition answered
    certainty: 1.0
    cites:
    - source: S2
      locator: §2.a.i; §3.e
    how_known: IEP.
  afterlife:
    value: Saṃsāra and mokṣa central in most streams; early Pūrvamīmāṃsā downplays liberation
    stance: varies by school
    certainty: 1.0
    cites:
    - source: S2
      locator: §1.a.iii; §3.e
    how_known: IEP. Used rebirth/liberation via karma stance already filled.
  moral_ledger:
    value: "karma 'denotes the moral, psychological spiritual and physical causal consequences of morally\
      \ significant past choices'."
    stance: karma-type law
    certainty: 1.0
    cites:
    - source: S2
      locator: §1.a.i
    how_known: IEP.
  authority:
    value: Vedas as śruti for āstika schools; smṛti secondary; reason/pramāṇas vary by darśana; Neo-Hindu
      meta-religion claims
    stance: revelation
    certainty: 0.7
    cites:
    - source: S2
      locator: §1.b; §3
    how_known: IEP. 0.7 — many also use reason.
  reserved_exemptions:
    value: Varṇa-āśrama duties differ by caste/stage; not miracle exemptions for an in-group vs physics
    stance: none
    certainty: 0.5
    cites:
    - source: S2
      locator: §1.a.iv; §2.b
    how_known: 'Coder: social duty ≠ E-scope exemption. 0.5.'
  teleology_in_nature:
    value: Closed ethical cosmos of reciprocal sacrifice in karma-kāṇḍa; Brahman as source in jñāna-kāṇḍa;
      varies
    stance: varies by school
    certainty: 0.7
    cites:
    - source: S2
      locator: §2.a
    how_known: '0.7.'
  necessity_and_freedom:
    value: Karma constrains rebirth; Vedānta commentators affirm jīva agency with Brahman dispensing fruits;
      Sāṅkhya minimizes puruṣa agency
    certainty: 0.7
    cites:
    - source: S2
      locator: §3.c; §3.f.ii
    how_known: '0.7.'
lio_axes:
  A_locus:
    value: 'BELOW_THRESHOLD'
    how_known: "Members differ: 'it is not true that all Hindus are polytheists'; Vaiṣṇava and Śaiva traditions\
      \ hold one deity is genuinely God (S2), and Sāṅkhya explains the cosmos by Prakṛti and Puruṣa (S2)."
    note: P44(b).
  B_cause:
    value: 'UNKNOWN'
    how_known: 'Not fixed by the sources read (T1 search logged, 2026-10-15).'
  C_ledger:
    value: 3
    certainty: 0.5
    cites:
    - source: S1
      locator: karma
    - source: S2
      locator: karma
    how_known: '0.5 — karma as impersonal moral-causal law (P44d); schools differ on deity-judgment overlay.'
    rationale: 'C=3: impersonal ledger (karma), not personal divine judge as family default. Alternative
      4 if reading some streams as no ledger.'
    alternatives:
    - value: 4
      note: Named alternative if coding streams that deny karmic moral law.
      cites:
      - source: S2
        locator: opening
    - value: 1
      note: Named alternative if coding bhakti personal-judge streams as primary.
      cites:
      - source: S1
        locator: bhakti
  D_authority:
    value: 'BELOW_THRESHOLD'
    how_known: "Hindu philosophy shares 'a textual connection to certain core Hindu religious texts (the\
      \ Vedas)', but Sāṅkhya 'does not explicitly attempt to align itself with the authority of the Vedas'\
      \ (S2)."
    note: 'Alternative: 1.'
    alternatives:
    - value: 1
      note: Named alternative.
      cites:
      - source: S2
        locator: §1.b; Sāṅkhya
  E_scope:
    value: 'UNKNOWN'
    how_known: Not addressed in the sources read.
epistemology:
  value: No single epistemology; Nyāya four pramāṇas; Mīmāṃsā/Vedānta foundational Vedas; Yoga/Sāṅkhya
    distinctive; Neo-Hindu universalism
  certainty: 1.0
  cites:
  - source: S2
    locator: §3
  how_known: IEP.
ethics:
  value: 'Puruṣārthas (dharma, artha, kāma, mokṣa); varṇa-āśrama; Gītā karmayoga/bhakti; ahimsa later
    prominent under Jain/Buddhist influence; schools disagree'
  certainty: 1.0
  cites:
  - source: S2
    locator: §1.a.iii; §2.b.ii; §3.g
  how_known: IEP.
practice:
  ritual_and_practice:
    value: 'Sacrifice, temple, pilgrimage, yoga, bhakti, household rites; regional diversity'
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: Britannica.
  community_form:
    value: 'Temple communities, monastic lineages (e.g. Śaṅkara maṭhas), caste/household structures, modern
      movements'
    certainty: 1.0
    cites:
    - source: S2
      locator: §3.f.iii; §4
    how_known: IEP.
science:
  historical_stance:
    value: Rich mathematical/astronomical/medical traditions in Indic civilization; philosophical schools
      variously engage or bracket natural philosophy
    certainty: 0.5
    cites:
    - source: S2
      locator: introduction
    how_known: Coder gloss — not detailed in sources read. 0.5.
  current_stance:
    value: Neo-Hinduism framed partly as response to Western scientism; living global religion
    certainty: 0.7
    cites:
    - source: S2
      locator: §4
    how_known: '0.7.'
schools_and_variants:
- name: Nyāya–Vaiśeṣika
  form: scholastic or philosophical
  how_it_differs: 'Logic, atomism, natural theology strands'
  lio_difference: Not rescored
  certainty: 1.0
  cites:
  - source: S2
    locator: §3.a–b
- name: Sāṅkhya–Yoga
  form: scholastic or philosophical
  how_it_differs: Dualism prakṛti/puruṣa; Yoga practical aṣṭāṅga
  lio_difference: Not rescored
  certainty: 1.0
  cites:
  - source: S2
    locator: §3.c–d
- name: Pūrvamīmāṃsā
  form: scholastic or philosophical
  how_it_differs: Vedic ritual authority; early texts omit mokṣa
  lio_difference: May differ on A/C — not rescored
  certainty: 1.0
  cites:
  - source: S2
    locator: §3.e
- name: Vedānta (Advaita / Viśiṣṭādvaita / Dvaita / Bhedābheda)
  form: scholastic or philosophical
  how_it_differs: Brahman–jīva metaphysics diverge sharply
  lio_difference: A/D may move by subschool — keep BELOW_THRESHOLD
  certainty: 1.0
  cites:
  - source: S2
    locator: §3.f
- name: Neo-Hinduism
  form: modern
  how_it_differs: Universalism / Vedānta-as-meta-religion
  lio_difference: Not rescored
  certainty: 1.0
  cites:
  - source: S2
    locator: §4
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: 'Nearly one billion worldwide; ~80% of India (early 21st c. Britannica)'
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: Britannica.
v7_1_rubric:
  label: authorial v7.1 scores
  L: 8
  P: 7
  E: 5
  V: 5
  X: 3
  total: 28
  scoring_note: 'Hinduism scores moderately due to its profound philosophical depth and ethical systems,
    accommodating diverse paths to enlightenment, but limited by supernatural claims and scriptural authority
    over empirical evidence.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 47 and section 7 scoring notes'
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
  use_when: 'Person’s primary religious identification is Hindu / sanatana dharma / Vedic-linked tradition,
    or primary philosophy is an āstika darśana.'
  do_not_use_when: 'Buddhist, Jain, or Sikh self-ID; do not force one LIO score across all Hindu subschools.'
  neighbors:
  - code: BUDDH
    relation: neighbor (easily confused)
    note: Shared milieu
  - code: JAIN
    relation: neighbor (easily confused)
    note: Independent
review:
  data_quality_flags: []
  open_questions:
  - Score LIO by major Vedānta subschool later?
  - Avatar doctrine for B still a lead only?
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Vasudha Narayanan; Britannica Editors
  citation: 'Narayanan, Vasudha, and Britannica Editors. "Hinduism." Encyclopaedia Britannica. https://www.britannica.com/topic/Hinduism.
    Wayback Machine snapshot 2026-10-07 01:10:21 UTC: https://web.archive.org/web/20261007011021/https://www.britannica.com/topic/Hinduism.'
  url: 'https://www.britannica.com/topic/Hinduism'
  accessed: '2026-10-25'
  reliability_note: 'Signed article; introduction and "The term Hinduism" read. P44(e): read in the Wayback
    copy (https://web.archive.org/web/20261007011021/https://www.britannica.com/topic/Hinduism); live
    page timed out on 2026-10-15, so no live comparison.'
- id: S2
  type: tertiary
  kind: encyclopedia
  author: Shyam Ranganathan
  citation: 'Ranganathan, Shyam. "Hindu Philosophy." Internet Encyclopedia of Philosophy. https://iep.utm.edu/hindu-ph/.'
  url: 'https://iep.utm.edu/hindu-ph/'
  accessed: '2026-10-25'
  reliability_note: Peer-reviewed; undated page.
---
# Hinduism (HINDU)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44. The v7.1 scores and note are unchanged.

## Summary

Major world religion of the Indian subcontinent: cumulative Vedic-linked traditions, not one doctrine. Nearly one billion adherents [S1]. Hindu philosophy = views with textual connection to Vedas [S2].

## Core metaphysics

Varies by school: deities and Brahman; karma and mokṣa common but not universal; authority of Vedas for āstika schools [S2].

## Position on the LIO axes

A/C/D BELOW_THRESHOLD; B/E UNKNOWN — unchanged (too much school variance for a single score).

## Schools and variants

Six darśanas; Vedānta subschools; Neo-Hinduism [S2].

## Science

Neo-Hinduism partly framed vs Western scientism [S2].

## Coding guidance

Hindu / āstika primary → HINDU. Do not flatten all subschools to one LIO score.

## v7.1 scoring note

Authorial v7.1 note unchanged (see front matter).

## Open questions

- Score LIO by major Vedānta subschool later?
- Avatar doctrine for B still a lead only?

## Research log

- Prior partial fills (karma ledger; T1 audit).
- 2026-10-25: deepened from Britannica + IEP; axes unchanged.
- 2026-10-25: C_ledger scored 3 (0.5) karma rule.
