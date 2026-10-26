---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 5
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S3 for Jason)
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
    summary: 'Draft (systems batch S3): filled from SEP "Epicurus" (Konstan). A 3 (0.5, alt 4), B 3 (0.5),
      C 4 (0.7), D 4 (0.7), E 4 (0.5). v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: "S3 audit (WEAKEN #3b): the swerve is Epicurus' doctrine (known chiefly through Lucretius\
      \ and Cicero); B alternative 4 named; A reasoning noted. Values unchanged."
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from SEP Epicurus: family/parents/origins, metaphysics TODOs, epistemology/ethics/practice/science/schools.
      Axes unchanged.'
identity:
  id: EPICUR
  v7_1_number: 16
  v7_1_label: Epicureanism
  display_label: Epicureanism
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: philosophical school or method
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: "'a complete and interdependent system'."
  family:
    value: 'Hellenistic atomist school: pleasure as absence of pain/disturbance; radical materialism;
      therapeutic philosophy'
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP.
  parent_traditions:
    value:
    - Democritean atomism
    - Garden school at Athens
    - 'Later Epicureanism (Lucretius, Philodemus)'
    certainty: 1.0
    cites:
    - source: S1
      locator: §1–3
    how_known: SEP.
  related_codes:
  - code: STOIC
    relation: contrast case
    note: Rival Hellenistic ethics
  - code: HEDON
    relation: overlaps
    note: Pleasure-centered; Epicurus is a specific school
  - code: ATHE
    relation: neighbor (easily confused)
    note: Gods exist but unconcerned
origins:
  founding_era:
    value: Epicurus 341–270 BCE; Garden founded Athens ~307/06 BCE
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: SEP.
  founding_region:
    value: 'Athens (Garden); earlier Samos, Colophon, Mytilene, Lampsacus'
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: SEP.
  founders_or_key_figures:
    value:
    - Epicurus
    - Lucretius
    - Philodemus
    - Diogenes of Oenoanda
    certainty: 1.0
    cites:
    - source: S1
      locator: §1–2
    how_known: SEP.
  key_texts:
  - value: 'Letters to Herodotus, Menoeceus, Pythocles; Principal Doctrines; Lucretius De rerum natura'
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: SEP.
metaphysics:
  god_nature_relation:
    value: "Gods exist, 'immortal and indestructible', within an atomistic materialist universe; 'do not\
      \ imagine that they concern themselves about human beings and their behavior'."
    stance: many gods within nature
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction; §4
    how_known: SEP.
  deity_personal:
    value: Gods as anthropomorphic blessed beings known via simulacra; not intervening persons
    stance: personal
    certainty: 0.7
    cites:
    - source: S1
      locator: §4; §6
    how_known: '0.7 — nature of gods debated in literature.'
  intervention:
    value: Do not imagine gods concern themselves about human beings and their behavior
    stance: none
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP.
  miracles:
    value: Naturalistic explanations for meteorological/planetary phenomena; open mind without decisive
      verification
    stance: reinterpreted as natural
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP.
  petition_and_prayer:
    value: 'Prayer as receptivity to vision of divine blessedness, not petitioning favors; conventional
      cult encouraged'
    stance: contemplative only
    certainty: 1.0
    cites:
    - source: S1
      locator: §6
    how_known: SEP.
  afterlife:
    value: "None: radical materialism disproves 'the possibility of the soul’s survival after death, and\
      \ hence the prospect of punishment in the afterlife'."
    stance: none
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP.
  moral_ledger:
    value: No cosmic moral ledger or postmortem punishment; justice as compact neither to harm nor be
      harmed
    stance: none
    certainty: 1.0
    cites:
    - source: S1
      locator: §5
    how_known: SEP.
  authority:
    value: "Empiricist: 'sensations, together with the perception of pleasure and pain, are infallible\
      \ criteria'."
    stance: observation and reason
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP.
  reserved_exemptions:
    value: Same atomic physics for all; no special exemption for the wise from natural law
    stance: none
    certainty: 1.0
    cites:
    - source: S1
      locator: §3
    how_known: SEP.
  teleology_in_nature:
    value: No Platonic Forms or creator design; naturalistic evolution of worlds and societies; atoms
      and void
    stance: none
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction; §3
    how_known: SEP.
  necessity_and_freedom:
    value: Atomic swerve introduces indeterminacy; better myths than paralyzing determinism; voluntary
      action debated
    certainty: 1.0
    cites:
    - source: S1
      locator: §4
    how_known: SEP.
lio_axes:
  A_locus:
    value: 3
    rationale: 'Gods exist inside a materialist universe and do not concern themselves with humans: no
      transcendent person.'
    certainty: 0.5
    cites:
    - source: S1
      locator: introduction; §4
    how_known: '0.5, alternative 4. The gods exist as material beings inside the cosmos, so P44(a) (no
      God gives 4) does not apply; divine beings located within nature fit 3. Their indifference bears
      on C and E (both 4), not on locus (S3 audit RQ1).'
    alternatives:
    - value: 4
      note: If material gods within nature are read as the immanent pole.
      cites:
      - source: S1
        locator: introduction
  B_cause:
    value: 3
    rationale: "No divine intervention and a naturalistic account of nature, but the swerve, Epicurus'\
      \ doctrine of uncaused atomic deviation (attested chiefly in later sources, including Lucretius\
      \ and Cicero), is chance within nature, so not exceptionless law (P40)."
    certainty: 0.5
    cites:
    - source: S1
      locator: introduction; §3
    how_known: "0.5: the swerve is Epicurus' doctrine, known chiefly through Lucretius and Cicero (S1);\
      \ its reading as a bar to B 4 is the coder's (P40: 4 only where exceptions and chance are both ruled\
      \ out). Alternative 4."
    alternatives:
    - value: 4
      note: If the swerve is read as natural indeterminacy compatible with B 4.
      cites:
      - source: S1
        locator: §3
  C_ledger:
    value: 4
    rationale: No afterlife punishment and gods indifferent to human behaviour.
    certainty: 0.7
    cites:
    - source: S1
      locator: introduction
    how_known: 'Stated by the system (P44c), 0.7.'
  D_authority:
    value: 4
    rationale: Sensations are infallible criteria; empiricist theory of knowledge.
    certainty: 0.7
    cites:
    - source: S1
      locator: introduction
    how_known: 'Stated; revelation not discussed, 0.7.'
  E_scope:
    value: 4
    rationale: "On the world's order (P7): indifferent gods favour no group."
    certainty: 0.5
    cites:
    - source: S1
      locator: introduction
    how_known: 'Implied by the stance (P44c), 0.5.'
epistemology:
  value: 'Empiricist: sensations and pathē infallible criteria; error from added opinion; counterwitnessing
    and analogy to the invisible; Canon'
  certainty: 1.0
  cites:
  - source: S1
    locator: introduction; §3–4
  how_known: SEP.
ethics:
  value: Happiness as absence of bodily pain and mental disturbance (ataraxia); natural/necessary vs empty
    desires; friendship essential; avoid politics where possible
  certainty: 1.0
  cites:
  - source: S1
    locator: introduction; §4; §6
  how_known: SEP.
practice:
  ritual_and_practice:
    value: Memorization of doctrines; therapeutic exercises; friendship communities; conventional cult
      without fear
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction; §6
    how_known: SEP.
  community_form:
    value: Garden school; later Epicurean communities and rituals (e.g. 20th); rings with Epicurus image
    certainty: 1.0
    cites:
    - source: S1
      locator: §6
    how_known: SEP.
science:
  historical_stance:
    value: Atomism; naturalistic meteorology; explanations of gravity/magnetism; open mind without decisive
      verification
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction; §3
    how_known: SEP.
  current_stance:
    value: Historical school; revived in modern receptions of Lucretius/atomism
    certainty: 0.7
    cites:
    - source: S1
      locator: closing
    how_known: '0.7.'
schools_and_variants:
- name: Classical Garden Epicureanism
  form: scholastic or philosophical
  how_it_differs: Epicurus + early associates
  lio_difference: Not rescored
  certainty: 1.0
  cites:
  - source: S1
    locator: §2
- name: 'Roman / later Epicureanism (Lucretius, Philodemus)'
  form: scholastic or philosophical
  how_it_differs: Latin verse exposition; Herculaneum pedagogy
  lio_difference: Not rescored
  certainty: 1.0
  cites:
  - source: S1
    locator: §1
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Historical school; no modern mass census (ancient Garden + later receptions)
    certainty: 0.7
    cites:
    - source: S1
      locator: §2; §6
    how_known: '0.7 — SEP not a census.'
v7_1_rubric:
  label: authorial v7.1 scores
  L: 9
  P: 9
  E: 10
  V: 10
  X: 8
  total: 46
  scoring_note: 'Epicureanism balances pleasure with reason, scoring high for its empirical roots in atomism
    and ethics.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 16 and section 7 scoring notes'
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
  use_when: 'Person’s philosophy centers Epicurean atomism, ataraxia, or Garden ethics.'
  do_not_use_when: Mere hedonism slogans without Epicurean physics/therapy; modern party-Epicurean branding
    alone.
  neighbors:
  - code: STOIC
    relation: contrast case
    note: Rival Hellenistic
  - code: HEDON
    relation: overlaps
    note: Broader pleasure ethics
  - code: ATHE
    relation: neighbor (easily confused)
    note: 'Gods exist, unconcerned'
review:
  data_quality_flags: []
  open_questions:
  - Confirm god_nature_relation stance enum for unconcerned gods
  - Swerve / free will for necessity score later?
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: David Konstan
  year: 2022
  citation: 'David Konstan. "Epicurus." Stanford Encyclopedia of Philosophy. First published January 10,
    2005; substantive revision July 8, 2022. https://plato.stanford.edu/entries/epicurus/.'
  url: 'https://plato.stanford.edu/entries/epicurus/'
  accessed: '2026-10-25'
  reliability_note: Peer-reviewed reference entry.
---
# Epicureanism (EPICUR)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44. The v7.1 scores and note are unchanged.

## Summary

Complete system of Epicurus (341–270 BCE): atomism, empiricist knowledge, pleasure as absence of pain/disturbance, therapy against fear of gods and death [S1].

## Core metaphysics

Atoms and void; gods exist but unconcerned; no afterlife; swerve and freedom [S1].

## Position on the LIO axes

Prior scores unchanged this pass.

## Schools and variants

Garden; later Lucretius/Philodemus [S1].

## Science

Naturalistic physics and meteorology [S1].

## Coding guidance

Epicurean philosophy → EPICUR. Party-hedonism alone ≠ EPICUR.

## v7.1 scoring note

Authorial v7.1 note unchanged (see front matter).

## Open questions

- God-stance enum for unconcerned gods?
- Swerve for necessity later?

## Research log

- Prior partial fills.
- 2026-10-25: deepened from SEP Epicurus; axes unchanged.
