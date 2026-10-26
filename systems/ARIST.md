---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 5
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S2 for Jason)
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
    summary: 'Draft (systems batch S2): filled from SEP "Aristotle", "Aristotle''s Natural Philosophy"
      and "Aristotle''s Ethics". A 1 at 0.5; B BELOW_THRESHOLD (alt 3); C, D, E UNKNOWN. v7.1 scores and
      note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: "S2 audit (WEAKEN #4b): god_nature_relation stance → 'separate first cause, not creator (eternal\
      \ world)' (new schema value, ruled 2026-10-15). No score change."
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from SEP Aristotle + natphil + ethics: family/parents, metaphysics TODOs,
      epistemology/practice/science/schools. Axes unchanged.'
identity:
  id: ARIST
  v7_1_number: 11
  v7_1_label: Aristotelianism
  display_label: Aristotelianism
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: philosophical school or method
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: 'SEP: the Lyceum; its members later called Peripatetics.'
  family:
    value: 'Peripatetic / Lyceum philosophy: hylomorphism, four causes, immanent teleology, virtue ethics'
    certainty: 1.0
    cites:
    - source: S1
      locator: §1; §8–9
    - source: S3
      locator: §1
    how_known: SEP.
  parent_traditions:
    value:
    - Plato’s Academy
    - Lyceum / Peripatetics
    - 'Later Aristotelianism (Islamic, Scholastic)'
    certainty: 1.0
    cites:
    - source: S1
      locator: §1; §14
    how_known: SEP.
  related_codes:
  - code: STOIC
    relation: neighbor (easily confused)
    note: Shared virtue vocabulary; different physics
  - code: PLATO
    relation: parent tradition
    note: Student then critic of Plato
  - code: EPICUR
    relation: contrast case
    note: Rival Hellenistic physics/ethics
origins:
  founding_era:
    value: '4th century BCE (Aristotle, 384–322 BCE; Lyceum set up on his return to Athens in 335)'
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: SEP.
  founding_region:
    value: Athens
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: SEP.
  founders_or_key_figures:
    value:
    - Aristotle
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: SEP.
  key_texts:
  - value: Physics
    author: Aristotle
    certainty: 1.0
    cites:
    - source: S2
      locator: introduction
    how_known: 'SEP: bk. 8 establishes the unmoved mover.'
  - value: Metaphysics
    author: Aristotle
    certainty: 1.0
    cites:
    - source: S1
      locator: §4
    - source: S2
      locator: introduction
    how_known: SEP.
  - value: Nicomachean Ethics
    author: Aristotle
    certainty: 1.0
    cites:
    - source: S3
      locator: §1
    how_known: SEP.
metaphysics:
  god_nature_relation:
    value: "'the unmoved mover of the universe, a supra-physical entity, without which the physical domain\
      \ could not remain in existence'; 'the first and final cause of all motion'."
    stance: 'separate first cause, not creator (eternal world)'
    certainty: 1.0
    cites:
    - source: S2
      locator: introduction
    - source: S1
      locator: §3
    how_known: SEP.
    note: 'New stance value added for this case (S2 audit RQ1, ruled 2026-10-15): SEP gives an eternal
      universe whose motion depends on a separate unmoved mover, not a created world.'
  deity_personal:
    value: Unmoved mover as pure actuality / thought thinking itself; not a personal intervening creator
      of a beginning
    stance: impersonal
    certainty: 0.7
    cites:
    - source: S1
      locator: §10
    - source: S2
      locator: introduction
    how_known: '0.7 — “personal” debated.'
  intervention:
    value: Unmoved mover as final cause of motion; not craftsman intervention in a created world
    stance: none
    certainty: 0.7
    cites:
    - source: S2
      locator: introduction
    how_known: '0.7.'
  miracles:
    value: Natural philosophy seeks immanent explanation; miracle doctrine not central
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S1
      locator: §4.2; §9
    how_known: '0.7.'
  petition_and_prayer:
    value: Not a core Aristotelian practice doctrine; civic religion in Politics context
    stance: not addressed
    certainty: 0.5
    cites:
    - source: S1
      locator: §12
    how_known: '0.5 — SEP overview thin on cult.'
  afterlife:
    value: Soul as form of body; active intellect debates; not a clear personal heaven doctrine in core
      treatises
    stance: varies by school
    certainty: 0.7
    cites:
    - source: S1
      locator: §11
    how_known: '0.7 — later Peripatetic/scholastic variance.'
  moral_ledger:
    value: No cosmic karma ledger; eudaimonia via virtue; political justice in the city
    stance: none
    certainty: 0.7
    cites:
    - source: S3
      locator: §1
    how_known: '0.7.'
  authority:
    value: Phainomena and endoxa; demonstration from first principles; nous of principles; not revelation
    stance: observation and reason
    certainty: 1.0
    cites:
    - source: S1
      locator: §3–4
    how_known: SEP.
  reserved_exemptions:
    value: Same natural causes for all; no in-group miracle exemption
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: §7–9
    how_known: '0.7.'
  teleology_in_nature:
    value: "Nature is 'an inner principle of change and being at rest' (Physics 2.1); final causes are\
      \ 'what these processes and entities are for'."
    stance: immanent ends
    certainty: 1.0
    cites:
    - source: S2
      locator: §1
    how_known: SEP.
  necessity_and_freedom:
    value: Voluntary action and deliberation in ethics; natural necessity in physics; akrasia puzzles
    certainty: 1.0
    cites:
    - source: S1
      locator: §3; §12
    - source: S3
      locator: §1
    how_known: SEP.
lio_axes:
  A_locus:
    value: 1
    rationale: "A separate, supra-physical unmoved mover on which the physical domain depends; not a creator\
      \ in time (an 'eternal chain of motions')."
    certainty: 0.5
    cites:
    - source: S2
      locator: introduction
    how_known: '0–4 scale (P1). Transcendent is fixed by the stance; personhood is not addressed in the
      sources read, so 0.5 (alternative 2).'
  B_cause:
    value: 'BELOW_THRESHOLD'
    how_known: 'Natures are inner principles of change and the chain of motions is eternal (S2), but the
      sources read do not address exceptions or miracles.'
    note: 'Alternative: 3. Evidence: S2 §1, §4.'
  C_ledger:
    value: 'UNKNOWN'
    how_known: 'Not addressed in the sources read (S3 treats eudaimonia, not a divine ledger).'
  D_authority:
    value: 'UNKNOWN'
    how_known: Revelation not addressed in the sources read.
  E_scope:
    value: 'UNKNOWN'
    how_known: Not addressed in the sources read.
epistemology:
  value: Phainomena and endoxic method; demonstration (apodeixis); nous of first principles; dialectic
    toward principles
  certainty: 1.0
  cites:
  - source: S1
    locator: §3–4
  how_known: SEP.
ethics:
  value: Eudaimonia and aretê; virtue as mean; practical wisdom (phronēsis); friendship and the political
    animal
  certainty: 1.0
  cites:
  - source: S3
    locator: §1
  - source: S1
    locator: §12
  how_known: SEP.
practice:
  ritual_and_practice:
    value: Philosophical research and teaching in the Lyceum; civic and household ethics; no single salvation
      cult
    certainty: 0.7
    cites:
    - source: S1
      locator: §1; §12
    how_known: '0.7.'
  community_form:
    value: Lyceum / Peripatetics; later school tradition; polis as ethical context
    certainty: 1.0
    cites:
    - source: S1
      locator: §1; §12
    how_known: SEP.
science:
  historical_stance:
    value: 'Foundational for logic, biology, physics, metaphysics; empirical observation with teleology'
    certainty: 1.0
    cites:
    - source: S1
      locator: §1; §4.2
    how_known: SEP.
  current_stance:
    value: Abiding scholarly and philosophical engagement across traditions
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction; §14
    how_known: SEP.
schools_and_variants:
- name: Classical Peripatetic / Lyceum
  form: scholastic or philosophical
  how_it_differs: Aristotle and early school
  lio_difference: Not rescored
  certainty: 1.0
  cites:
  - source: S1
    locator: §1
- name: Later Aristotelianism (Islamic / Scholastic)
  form: scholastic or philosophical
  how_it_differs: Reception with theology (e.g. Aquinas)
  lio_difference: May move A/B — keep prior
  certainty: 0.7
  cites:
  - source: S1
    locator: §14
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Historical school with vast later influence; not a modern mass religion
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction; §14
    how_known: SEP.
v7_1_rubric:
  label: authorial v7.1 scores
  L: 9
  P: 9
  E: 10
  V: 10
  X: 9
  total: 47
  scoring_note: 'Aristotelianism lays foundational empirical and logical groundwork, scoring high despite
    historical limitations.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 11 and section 7 scoring notes'
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
  use_when: Person’s primary philosophy is Aristotelian / Peripatetic / virtue-ethics-in-Aristotle’s-framework.
  do_not_use_when: Mere “moderation” slogans; Thomism as primary → prefer THOM if that code fits better.
  neighbors:
  - code: STOIC
    relation: neighbor (easily confused)
    note: Virtue rivals
  - code: PLATO
    relation: parent tradition
    note: Teacher
review:
  data_quality_flags: []
  open_questions:
  - deity_personal stance “impersonal” valid?
  - Active intellect / afterlife for later school scores?
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Christopher Shields
  year: 2020
  citation: 'Shields, Christopher. "Aristotle." Stanford Encyclopedia of Philosophy. First published September
    25, 2008; substantive revision August 25, 2020. https://plato.stanford.edu/entries/aristotle/.'
  url: 'https://plato.stanford.edu/entries/aristotle/'
  accessed: '2026-10-25'
  reliability_note: Peer-reviewed reference entry.
- id: S2
  type: tertiary
  kind: encyclopedia
  author: Istvan Bodnar
  year: 2023
  citation: 'Bodnar, Istvan. "Aristotle''s Natural Philosophy." Stanford Encyclopedia of Philosophy. First
    published May 26, 2006; substantive revision April 24, 2023. https://plato.stanford.edu/entries/aristotle-natphil/.'
  url: 'https://plato.stanford.edu/entries/aristotle-natphil/'
  accessed: '2026-10-25'
  reliability_note: Peer-reviewed reference entry.
- id: S3
  type: tertiary
  kind: encyclopedia
  author: Richard Kraut
  year: 2026
  citation: 'Kraut, Richard. "Aristotle''s Ethics." Stanford Encyclopedia of Philosophy. First published
    May 1, 2001; substantive revision August 11, 2026. https://plato.stanford.edu/entries/aristotle-ethics/.'
  url: 'https://plato.stanford.edu/entries/aristotle-ethics/'
  accessed: '2026-10-25'
  reliability_note: Peer-reviewed reference entry.
---
# Aristotelianism (ARIST)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44. The v7.1 scores and note are unchanged.

## Summary

Aristotle (384–322 BCE) and the Lyceum: logic, hylomorphism, four causes, immanent teleology, eudaimonia [S1][S2][S3].

## Core metaphysics

Unmoved mover; form and matter; teleology in nature without craftsman design [S1][S2].

## Position on the LIO axes

Prior scores (A1 B BELOW_THRESHOLD; C/D/E UNKNOWN) unchanged this pass.

## Schools and variants

Lyceum; later Islamic/Scholastic Aristotelianism [S1].

## Science

Foundational across sciences; empirical + teleological [S1].

## Coding guidance

Aristotelian primary → ARIST. Thomism primary → THOM if coded separately.

## v7.1 scoring note

Authorial v7.1 note unchanged (see front matter).

## Open questions

- Impersonal stance for unmoved mover?
- Afterlife / active intellect later?

## Research log

- Prior god/teleology/ethics fills.
- 2026-10-25: deepened TODOs from SEP; axes unchanged.
