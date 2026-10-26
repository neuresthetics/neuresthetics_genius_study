---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 8
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
    summary: 'Draft (systems batch S6): filled from IEP "Jain Philosophy" (Webb) and Britannica "Jainism"
      (Dundas). A 3 (0.5, alt 4); C 3 (0.5, alt 4); E 4 (0.5); B, D UNKNOWN. v7.1 scores and note unchanged.
      Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S6 audit fix: C cites P44(d); Britannica byline credited to Strohl, Dundas and Britannica
      Editors.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S7 audit fix: rotating Britannica bylines noted (P44(e)).'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'T1: B_cause UNKNOWN -> 3 (0.5, alt 2) from IEP "Jain Philosophy" (S1).'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'T1 audit fix: B cites P41; alternative 4 primary, 2 secondary; karma quote located.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from IEP Jain Philosophy (Webb) + Britannica Jainism: family/parents, metaphysics
      TODOs, epistemology/ethics/practice/science/schools (Śvetāmbara/Digambara). Axes unchanged.'
identity:
  id: JAIN
  v7_1_number: 37
  v7_1_label: Jainism
  display_label: Jainism
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: religion
    certainty: 1.0
    cites:
    - source: S2
      locator: introduction
    how_known: Britannica.
  family:
    value: Path to soul purity via ahimsa and ascetic conquest of passions; independent Indian tradition
      (not Hindu sect)
    certainty: 1.0
    cites:
    - source: S2
      locator: introduction; Overview
    how_known: Britannica.
  parent_traditions:
    value:
    - Śramaṇa / renunciant movements of eastern India
    - 'Tirthankara lineage (Parshvanatha, Mahavira)'
    - Śvetāmbara and Digambara monastic streams
    certainty: 1.0
    cites:
    - source: S2
      locator: Early history
    how_known: Britannica.
  related_codes:
  - code: HINDU
    relation: neighbor (easily confused)
    note: Shared vocabulary; independent
  - code: BUDDH
    relation: neighbor (easily confused)
    note: Contemporary śramaṇa milieu
  - code: ATHE
    relation: neighbor (easily confused)
    note: Denies creator god; still has gods within cosmos
origins:
  founding_era:
    value: '7th–5th century BCE'
    certainty: 1.0
    cites:
    - source: S2
      locator: Early history
    how_known: Britannica.
  founding_region:
    value: 'Ganges basin, eastern India'
    certainty: 1.0
    cites:
    - source: S2
      locator: Early history
    how_known: Britannica.
  founders_or_key_figures:
    value:
    - Parshvanatha
    - Mahavira
    certainty: 1.0
    cites:
    - source: S2
      locator: Early history
    how_known: "Britannica: Jains believe the tradition 'does not have a historical founder'."
  key_texts:
  - value: Śvetāmbara canon; Digambara Prakrit works; Tattvārtha-sūtra (both communities)
    certainty: 1.0
    cites:
    - source: S2
      locator: Top Questions / sacred texts
    - source: S1
      locator: References
    how_known: Britannica + IEP.
metaphysics:
  god_nature_relation:
    value: "'What is denied is a creator god above all. The universe is eternal, matter and souls being\
      \ equally uncreated. The universe contains gods ... but there is no being outside it exercising\
      \ control over it.'"
    stance: many gods within nature
    certainty: 1.0
    cites:
    - source: S1
      locator: metaphysics
    how_known: IEP.
  deity_personal:
    value: Gods exist within the universe and may be worshipped for various reasons; all subject to karma;
      no creator outside
    stance: personal
    certainty: 1.0
    cites:
    - source: S1
      locator: Metaphysics
    how_known: IEP.
  intervention:
    value: No external creator control; liberation by purging karma through own effort
    stance: none
    certainty: 1.0
    cites:
    - source: S1
      locator: Metaphysics
    how_known: IEP.
  miracles:
    value: Not centered on creator miracles; kevala omniscience of perfected souls
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S1
      locator: Epistemology and Logic
    how_known: '0.7.'
  petition_and_prayer:
    value: Temple worship and festivals for Tirthankaras; gods may be worshipped for various reasons;
      core path is ascetic practice
    stance: petition answered
    certainty: 0.7
    cites:
    - source: S2
      locator: Top Questions / practices
    - source: S1
      locator: Metaphysics
    how_known: '0.7.'
  afterlife:
    value: Infinite prior lives; rebirth until release (moksha) by purging all karma
    stance: rebirth
    certainty: 1.0
    cites:
    - source: S1
      locator: Metaphysics
    how_known: IEP.
  moral_ledger:
    value: Karma as material substance binding soul to body; good and bad karma both impede liberation;
      ahimsa central
    stance: karma-type law
    certainty: 1.0
    cites:
    - source: S1
      locator: Metaphysics; Ethics
    how_known: IEP.
  authority:
    value: 'Right knowledge, faith, practice (Three Jewels); scriptures and Tirthankara teaching; kevala
      of perfected souls'
    stance: revelation
    certainty: 0.7
    cites:
    - source: S2
      locator: Top Questions / beliefs
    - source: S1
      locator: Epistemology and Logic
    how_known: '0.7 — also reason/pramāṇas.'
  reserved_exemptions:
    value: Same causal karma for all jivas; no creator-granted exemption
    stance: none
    certainty: 1.0
    cites:
    - source: S1
      locator: Metaphysics
    how_known: IEP.
  teleology_in_nature:
    value: Universal chain of cause and effect; anekāntavāda (many-sided reality); no creator teleology
    stance: immanent ends
    certainty: 0.7
    cites:
    - source: S2
      locator: Top Questions / beliefs
    how_known: '0.7.'
  necessity_and_freedom:
    value: Every event has a definite cause; liberation through disciplined effort and vows
    certainty: 0.7
    cites:
    - source: S2
      locator: Top Questions / beliefs
    - source: S1
      locator: Ethics
    how_known: '0.7.'
lio_axes:
  A_locus:
    value: 3
    rationale: No creator and no being outside the universe; gods exist inside it.
    certainty: 0.5
    cites: &id001
    - source: S1
      locator: metaphysics
    how_known: 'As EPICUR: gods within nature fit 3 (alternative 4).'
    alternatives:
    - value: 4
      note: Named alternative.
      cites: *id001
  B_cause:
    value: 3
    rationale: "Scored on the system's account of nature under P41 (by analogy: a controller is denied,\
      \ but no exceptionless law is stated): 'The universe is eternal, matter and souls being equally\
      \ uncreated. The universe contains gods who may be worshipped for various reasons, but there is\
      \ no being outside it exercising control over it' (S1). 'The gods and other superhuman beings are\
      \ all just as subject to karma and rebirth as human beings are' (S1, same section)."
    certainty: 0.5
    cites: &id002
    - source: S1
      locator: metaphysics section
    how_known: 'P41: B 3 at 0.5, alternative 4 (no stated no-exception claim). Secondary alternative 2:
      gods inside the universe may be worshipped, but the source never says that worship changes the course
      of nature.'
    alternatives:
    - value: 4
      note: 'P41 alternative: no stated exceptionless law.'
      cites: *id002
    - value: 2
      note: 'Secondary: worship of in-world gods; the source does not say it changes nature.'
      cites: *id002
  C_ledger:
    value: 3
    rationale: Karma and rebirth govern gods and humans alike; no judging creator.
    certainty: 0.5
    cites: &id003
    - source: S1
      locator: metaphysics
    how_known: 'Karma rule (P44(d)): an impersonal moral ledger is C 3 @0.5, alternative 4. Karma: impersonal,
      but still a moral ledger.'
    alternatives:
    - value: 4
      note: Named alternative.
      cites: *id003
  D_authority:
    value: 'UNKNOWN'
    how_known: Not addressed in the sources read.
  E_scope:
    value: 4
    rationale: "On the world's order (P7): gods 'are all just as subject to karma and rebirth as human\
      \ beings are'; no being outside exercises control."
    certainty: 0.5
    cites:
    - source: S1
      locator: metaphysics
    how_known: 'Implied: 0.5.'
epistemology:
  value: 'Anekānta / naya / syādvāda: multifaceted reality; pramāṇas include perception, testimony, extrasensory,
    kevala; fallibilism'
  certainty: 1.0
  cites:
  - source: S1
    locator: Epistemology and Logic
  how_known: IEP.
ethics:
  value: Ahimsa as cardinal; five vows (monastic mahāvratas / lay aṇuvratas); aim to stop karma accumulation;
    vegetarianism
  certainty: 1.0
  cites:
  - source: S1
    locator: Ethics
  - source: S2
    locator: Overview
  how_known: IEP + Britannica.
practice:
  ritual_and_practice:
    value: 'Ascetic care (mouth-cloth, no eating after dark); temple worship; fasting; confession; meditation'
    certainty: 1.0
    cites:
    - source: S2
      locator: Top Questions / practices
    how_known: Britannica.
  community_form:
    value: Monks/nuns and laity; Śvetāmbara and Digambara; largely India-centered diaspora
    certainty: 1.0
    cites:
    - source: S2
      locator: Early history; Overview
    how_known: Britannica.
science:
  historical_stance:
    value: Detailed cosmology and taxonomy of living beings by senses; causal metaphysics
    certainty: 0.7
    cites:
    - source: S1
      locator: Metaphysics
    how_known: '0.7.'
  current_stance:
    value: Living minority religion; philosophy studied in Indian philosophy curricula
    certainty: 0.7
    cites:
    - source: S2
      locator: Overview
    how_known: '0.7.'
schools_and_variants:
- name: Śvetāmbara
  form: reform
  how_it_differs: White-robed monastics; female liberation possible; Valabhi canon
  lio_difference: Not rescored
  certainty: 1.0
  cites:
  - source: S2
    locator: Early history
- name: Digambara
  form: reform
  how_it_differs: Sky-clad monks; denies liberation from female body; distinct scripture stance
  lio_difference: Not rescored
  certainty: 1.0
  cites:
  - source: S2
    locator: Early history
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: More than six million; vast majority in India
    certainty: 1.0
    cites:
    - source: S2
      locator: Overview
    how_known: Britannica.
v7_1_rubric:
  label: authorial v7.1 scores
  L: 9
  P: 9
  E: 6
  V: 8
  X: 4
  total: 36
  scoring_note: 'Jainism scores relatively high due to its rigorous ethical system and focus on non-violence,
    providing strong moral coherence, but limited by metaphysical elements like karma and souls that reduce
    empirical alignment.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 37 and section 7 scoring notes'
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
  use_when: 'Person’s primary religious identification is Jain / Jaina, or philosophy centers Jain metaphysics/ethics.'
  do_not_use_when: Mere vegetarianism or ahimsa slogans without Jain tradition.
  neighbors:
  - code: HINDU
    relation: neighbor (easily confused)
    note: Independent
  - code: BUDDH
    relation: neighbor (easily confused)
    note: Śramaṇa cousin
  - code: ATHE
    relation: neighbor (easily confused)
    note: No creator ≠ ATHE alone
review:
  data_quality_flags: []
  open_questions:
  - Confirm afterlife stance enum fits reincarnation
  - D_authority still UNKNOWN — score from Three Jewels + scripture?
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Mark Owen Webb
  citation: 'Webb, Mark Owen. "Jain Philosophy." Internet Encyclopedia of Philosophy. https://iep.utm.edu/jain/.'
  url: 'https://iep.utm.edu/jain/'
  accessed: '2026-10-25'
  reliability_note: Peer-reviewed reference entry; undated page.
- id: S2
  type: tertiary
  kind: encyclopedia
  author: G. Ralph Strohl; Paul Dundas; Britannica Editors
  citation: 'Strohl, G. Ralph, Paul Dundas, and Britannica Editors. "Jainism." Encyclopaedia Britannica,
    updated 15 September 2026. https://www.britannica.com/topic/Jainism.'
  url: 'https://www.britannica.com/topic/Jainism'
  accessed: '2026-10-25'
  reliability_note: 'Signed article; first page read. AI Top Questions ignored. Byline lists Strohl and
    Dundas (checked in the Wayback copy, S6 audit fix). Bylines rotate between snapshots: the live page
    read 2026-10-15 showed Dundas and Britannica Editors; the Wayback copy lists Strohl and Dundas (P44(e):
    both recorded).'
---
# Jainism (JAIN)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44. The v7.1 scores and note are unchanged.

## Summary

Indian religion of spiritual purity through ahimsa and ascetic conquest; Parshvanatha and Mahavira; independent of Hinduism [S2].

## Core metaphysics

Eternal universe; souls and matter; no creator god; gods within cosmos subject to karma; liberation by purging karma [S1].

## Position on the LIO axes

Prior scores (A3 B3 C3 E4; D UNKNOWN) unchanged this pass.

## Schools and variants

Śvetāmbara and Digambara [S2].

## Science

Causal cosmology; living minority tradition [S1][S2].

## Coding guidance

Jain self-ID / Jain philosophy → JAIN. Vegetarianism alone ≠ JAIN.

## v7.1 scoring note

Authorial v7.1 note unchanged (see front matter).

## Open questions

- Confirm afterlife stance enum.
- Score D from Three Jewels + scripture?

## Research log

- Prior axis work and T1 audit.
- 2026-10-25: deepened TODOs from IEP + Britannica; axes unchanged.
