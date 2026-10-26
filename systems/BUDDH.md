---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 6
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S6 for Jason)
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
    summary: 'Draft (systems batch S6): filled from SEP "Buddha" (Siderits). A BELOW_THRESHOLD (alt 4);
      B BELOW_THRESHOLD; C 3 (0.5, alt 4); D, E UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S6 audit fix: C cites P44(d).'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'T2: A_locus searched, unchanged; search logged.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from SEP Buddha (Siderits): family/parents/origins, metaphysics TODOs,
      epistemology/ethics/practice/science/schools. Axes unchanged.'
identity:
  id: BUDDH
  v7_1_number: 35
  v7_1_label: Buddhism
  display_label: Buddhism
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: religion
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP.
  family:
    value: 'Śramaṇa-rooted path of liberation from suffering via Four Noble Truths, non-self, karma/rebirth;
      later Theravāda, Mahāyāna, Vajrayāna streams'
    certainty: 1.0
    cites:
    - source: S1
      locator: §1–2
    how_known: SEP.
  parent_traditions:
    value:
    - Śramaṇa renunciant movements of North India
    - Early Nikāya / Āgama teachings
    - Abhidharma and later Mahāyāna schools
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: SEP.
  related_codes:
  - code: HINDU
    relation: neighbor (easily confused)
    note: Shared Indian milieu; Buddhism rejects Vedic authority
  - code: JAIN
    relation: neighbor (easily confused)
    note: Śramaṇa cousin; different metaphysics
  - code: STOIC
    relation: contrast case
    note: Different non-self / passion analyses
  - code: NIHIL
    relation: neighbor (easily confused)
    note: Non-self ≠ moral nihilism
origins:
  founding_era:
    value: 'The Buddha, fl. circa 450 BCE'
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP.
  founding_region:
    value: Gangetic basin; present India–Nepal border (Śākya clan)
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: SEP.
  founders_or_key_figures:
    value:
    - The Buddha (Gautama)
    - Later Abhidharma / Madhyamaka / Yogācāra teachers
    certainty: 1.0
    cites:
    - source: S1
      locator: §1; closing
    how_known: SEP.
  key_texts:
  - value: 'Nikāyas / Āgamas (Four Noble Truths, non-self discourses); later Abhidharma and Mahāyāna sūtras'
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction; Primary Sources
    how_known: SEP.
metaphysics:
  god_nature_relation:
    value: Early teachings include gods within saṃsāra; no creator Brahman; later Mahāyāna buddha/bodhisattva
      cosmologies vary
    stance: varies by school
    certainty: 1.0
    cites:
    - source: S1
      locator: §1; §4
    how_known: SEP.
  deity_personal:
    value: Gods as sentient beings in rebirth; not a creator person; later devotion to buddhas/bodhisattvas
    stance: varies by school
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: SEP.
  intervention:
    value: No external creator control; liberation by insight and path; upāya and bodhisattva aid in some
      Mahāyāna streams
    stance: varies by school
    certainty: 0.7
    cites:
    - source: S1
      locator: §2; §5
    how_known: '0.7.'
  miracles:
    value: Tradition attributes superhuman cognitive powers to buddhas; SEP entry brackets those for philosophical
      focus
    stance: varies by school
    certainty: 0.7
    cites:
    - source: S1
      locator: §1; §5
    how_known: '0.7.'
  petition_and_prayer:
    value: 'Early path centers meditation and insight; later popular Buddhism includes refuge, offerings,
      Pure Land petition'
    stance: varies by school
    certainty: 0.7
    cites:
    - source: S1
      locator: §2
    how_known: '0.7 — SEP focuses on philosophical Buddha.'
  afterlife:
    value: "All sentient beings, 'including humans, non-human animals, gods, and the inhabitants of various\
      \ hells', undergo rebirth; the ideal is liberation from it."
    stance: rebirth
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: SEP.
  moral_ledger:
    value: "'rebirth is governed by the causal laws of karma (good actions cause pleasant fruit for the\
      \ agent, evil actions cause unpleasant fruit, etc.)'."
    stance: karma-type law
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: SEP.
  authority:
    value: Buddha’s word authoritative within tradition; later schools debate scripture vs reason; philosophical
      defense vs Brahmanical schools
    stance: revelation
    certainty: 0.7
    cites:
    - source: S1
      locator: §5
    how_known: '0.7 — also reason.'
  reserved_exemptions:
    value: Same causal karma for agents; no creator-granted exemption from natural order
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: §4
    how_known: '0.7.'
  teleology_in_nature:
    value: Dependent origination; middle path between eternalism and annihilationism; no creator teleology
    stance: immanent ends
    certainty: 0.7
    cites:
    - source: S1
      locator: §2
    how_known: '0.7.'
  necessity_and_freedom:
    value: Causal series of psychophysical elements; intentional action (cetanā) as karma; liberation
      by extinguishing defilements
    certainty: 1.0
    cites:
    - source: S1
      locator: §2; §4
    how_known: SEP.
lio_axes:
  A_locus:
    value: 'BELOW_THRESHOLD'
    how_known: "Gods are among the beings who undergo rebirth, and the tradition competed with 'Brahmanical\
      \ schools that posit an omniscient creator' (S1), but the entry states no position on God for all\
      \ schools."
    note: 'Alternative: 4.'
    alternatives:
    - value: 4
      note: Named alternative.
      cites:
      - source: S1
        locator: §2
  B_cause:
    value: 'BELOW_THRESHOLD'
    how_known: Rebirth under causal laws (S1); the entry also reports a passage on supernormal cognitive
      powers. Not fixed.
    note: 'Evidence: S1.'
  C_ledger:
    value: 3
    rationale: 'Karma: an impersonal causal law that brings good and bad fruit to the agent; no judging
      person.'
    certainty: 0.5
    cites: &id001
    - source: S1
      locator: §2
    how_known: 'Karma rule (P44(d)): an impersonal moral ledger is C 3 @0.5, alternative 4. Karma: impersonal,
      but still a moral ledger.'
    alternatives:
    - value: 4
      note: Named alternative.
      cites: *id001
  D_authority:
    value: 'UNKNOWN'
    how_known: Not addressed in the sources read.
  E_scope:
    value: 'UNKNOWN'
    how_known: Not addressed in the sources read.
epistemology:
  value: 'Insight via meditation-enhanced observation plus philosophical rationality; hostility to unobservable
    entities (Pohapāda, Tevijja); two truths in later tradition; omniscience claims debated'
  certainty: 1.0
  cites:
  - source: S1
    locator: §3; §5
  how_known: SEP.
ethics:
  value: 'Suffering cessation as aim; common-sense morality as initial step; three defilements (desire,
    aversion, ignorance); intention central to karma; non-self undercuts egoistic motives'
  certainty: 1.0
  cites:
  - source: S1
    locator: §2; §4
  how_known: SEP.
practice:
  ritual_and_practice:
    value: Eightfold path training; meditation; insight; monastic renunciation and lay morality
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: SEP.
  community_form:
    value: 'Saṅgha (monastic) and laity; Theravāda, Mahāyāna, Vajrayāna institutional forms'
    certainty: 0.7
    cites:
    - source: S1
      locator: §2; closing
    how_known: '0.7 — SEP focuses on early philosophy.'
science:
  historical_stance:
    value: Reductionist analysis of persons; conventional vs ultimate truth; Abhidharma taxonomies
    certainty: 0.7
    cites:
    - source: S1
      locator: §2
    how_known: '0.7.'
  current_stance:
    value: Living world religion; Buddhist philosophy active in analytic dialogue
    certainty: 0.7
    cites:
    - source: S1
      locator: closing
    how_known: '0.7.'
schools_and_variants:
- name: Theravāda / early Nikāya
  form: scholastic or philosophical
  how_it_differs: Pali canon; non-self + karma/rebirth as classical package
  lio_difference: Not rescored
  certainty: 1.0
  cites:
  - source: S1
    locator: §1–2
- name: Abhidharma schools
  form: scholastic or philosophical
  how_it_differs: Systematic metaphysics of dharmas; Personalist minority
  lio_difference: Not rescored
  certainty: 1.0
  cites:
  - source: S1
    locator: §2; §5
- name: Mahāyāna (Madhyamaka / Yogācāra / Pure Land / Chan)
  form: scholastic or philosophical
  how_it_differs: 'Emptiness, mind-only, devotion, or meditation-alone emphases'
  lio_difference: A/B/D may move — keep BELOW_THRESHOLD / UNKNOWN
  certainty: 0.7
  cites:
  - source: S1
    locator: §2; closing
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Major world religion; hundreds of millions (order-of-magnitude; not from S1)
    certainty: 0.5
    cites:
    - source: S1
      locator: introduction
    how_known: Coder gloss — SEP not a census. 0.5.
v7_1_rubric:
  label: authorial v7.1 scores
  L: 9
  P: 9
  E: 7
  V: 7
  X: 5
  total: 37
  scoring_note: 'Buddhism scores relatively high due to its profound philosophical and practical approach
    to ending suffering, blending ethics and meditation with strong psychological alignment, but tempered
    by metaphysical elements like rebirth that reduce empirical compatibility.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 35 and section 7 scoring notes'
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
  use_when: 'Person’s primary religious identification is Buddhist, or philosophy centers Buddhist non-self
    / Four Noble Truths.'
  do_not_use_when: Mere mindfulness fashion without Buddhist tradition; do not flatten all schools to
    one LIO score.
  neighbors:
  - code: HINDU
    relation: neighbor (easily confused)
    note: Rejects Vedas
  - code: JAIN
    relation: neighbor (easily confused)
    note: Different non-self / soul
  - code: NIHIL
    relation: neighbor (easily confused)
    note: Non-self ≠ nihilism
review:
  data_quality_flags: []
  open_questions:
  - Score D from Buddha-authority vs philosophical reason?
  - Mahāyāna Pure Land for B/petition — separate school score later?
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Mark Siderits
  year: 2023
  citation: 'Siderits, Mark. "Buddha." Stanford Encyclopedia of Philosophy. First published February 17,
    2011; substantive revision March 6, 2023. https://plato.stanford.edu/entries/buddha/.'
  url: 'https://plato.stanford.edu/entries/buddha/'
  accessed: '2026-10-25'
  reliability_note: 'Peer-reviewed reference entry; covers the Buddha’s teachings, not every later school.'
---
# Buddhism (BUDDH)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44. The v7.1 scores and note are unchanged.

## Summary

Teachings of the Buddha (Gautama, fl. ~450 BCE) on liberation from suffering: Four Noble Truths, non-self, karma and rebirth [S1].

## Core metaphysics

No creator; gods within saṃsāra; dependent origination; conventional vs ultimate truth in later tradition [S1].

## Position on the LIO axes

A/B BELOW_THRESHOLD; C3; D/E UNKNOWN — unchanged this pass (school variance).

## Schools and variants

Theravāda / Nikāya; Abhidharma; Mahāyāna streams [S1].

## Science

Reductionist person-analysis; living philosophical tradition [S1].

## Coding guidance

Buddhist self-ID / Buddhist philosophy → BUDDH. Mindfulness alone ≠ BUDDH.

## v7.1 scoring note

Authorial v7.1 note unchanged (see front matter).

## Open questions

- Score D from Buddha-authority vs reason?
- Pure Land / Mahāyāna for B later?

## Research log

- Prior afterlife/karma fills and T1 audit.
- 2026-10-25: deepened from SEP Buddha; axes unchanged.
