---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 4
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S4 for Jason)
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
    summary: 'Draft (systems batch S4): filled from SEP "Skepticism" (Comesaña and Klein). A BELOW_THRESHOLD
      (suspension, as AGNOS); others UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities: family/parents/related codes, origins, metaphysics TODOs, epistemology,
      ethics, practice, science, schools (Humean, Cartesian, Pyrrhonian). Axes unchanged. Re-read SEP
      Skepticism (Comesaña/Klein).'
identity:
  id: SCEPT
  v7_1_number: 20
  v7_1_label: Scepticism (Skepticism)
  display_label: Scepticism (Skepticism)
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: epistemic stance
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP treats skepticism as a family of epistemological positions.
  family:
    value: 'Philosophical skepticism: suspend judgment on propositions common-sense takes as known'
    certainty: 1.0
    cites: &id001
    - source: S1
      locator: §1–2
    how_known: SEP.
  parent_traditions:
    value:
    - Ancient Pyrrhonism
    - Cartesian evil-demon / external-world doubt
    - Humean inductive skepticism
    - Contemporary closure/contextualism debates
    certainty: 1.0
    cites: *id001
    how_known: SEP structure.
  related_codes:
  - code: NIHIL
    relation: overlaps
    note: Epistemological nihilism is a harsh cousin
  - code: EMPIR
    relation: neighbor (easily confused)
    note: Empiricism is a positive programme; skepticism challenges knowledge claims
  - code: RATN
    relation: neighbor (easily confused)
    note: Rationalism vs skeptical challenge
  - code: AGNOS
    relation: neighbor (easily confused)
    note: Religious agnosticism ≠ general philosophical skepticism
origins:
  founding_era:
    value: Ancient roots; modern Cartesian/Humean forms; ongoing analytic debate
    certainty: 1.0
    cites: *id001
    how_known: SEP (labels without strict historical claim).
  founding_region:
    value: Western philosophy (Greece; early modern Europe; Anglophone analytic)
    certainty: 0.7
    cites: *id001
    how_known: SEP focus. 0.7.
  founders_or_key_figures:
    value:
    - Pyrrhonian tradition (Agrippa modes)
    - Descartes (method of doubt / evil genius)
    - Hume (induction)
    - Contemporary discussants surveyed in SEP
    certainty: 1.0
    cites: *id001
    how_known: SEP.
  key_texts:
  - value: 'Descartes, Meditations'
    certainty: 1.0
    cites:
    - source: S1
      locator: §4
    how_known: SEP.
  - value: 'Hume, Treatise (induction)'
    certainty: 1.0
    cites:
    - source: S1
      locator: §3
    how_known: SEP.
metaphysics:
  god_nature_relation:
    value: Not addressed in SEP; Pyrrhonian suspension is universal.
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S1
      locator: §2
    how_known: SEP gives no God-view.
  deity_personal:
    value: Not a shared theology; Descartes uses God later to escape doubt; Pyrrhonian suspension is universal
      including about God
    stance: not addressed
    certainty: 1.0
    cites: *id001
    how_known: 'SEP: god not the topic; Pyrrhonian universality noted in prior record.'
  intervention:
    value: Not addressed as doctrine
    stance: not addressed
    certainty: 1.0
    cites: *id001
    how_known: SEP.
  miracles:
    value: Not addressed as doctrine
    stance: not addressed
    certainty: 1.0
    cites: *id001
    how_known: SEP.
  petition_and_prayer:
    value: Not a cult practice
    stance: not addressed
    certainty: 1.0
    cites: *id001
    how_known: SEP.
  afterlife:
    value: Not addressed as shared doctrine
    stance: not addressed
    certainty: 1.0
    cites: *id001
    how_known: SEP.
  moral_ledger:
    value: Not a moral-judgment theology; epistemological thesis
    stance: none
    certainty: 1.0
    cites: *id001
    how_known: SEP.
  authority:
    value: 'Challenge to claims of knowledge/justification; Agrippa modes against unsupported assertion,
      circularity, infinite regress'
    stance: observation and reason
    certainty: 0.7
    cites:
    - source: S1
      locator: §6
    how_known: SEP Pyrrhonian section. 0.7.
  reserved_exemptions:
    value: None as supernatural doctrine; contextualism varies standards by conversation
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: §5
    how_known: '0.7.'
  teleology_in_nature:
    value: Not a teleology doctrine; epistemological thesis
    stance: none
    certainty: 1.0
    cites:
    - source: S1
      locator: §1–2
    how_known: SEP.
  necessity_and_freedom:
    value: Not a free-will metaphysics; about justification and knowledge
    certainty: 1.0
    cites: *id001
    how_known: SEP.
lio_axes:
  A_locus:
    value: 'BELOW_THRESHOLD'
    how_known: 'Universal suspension of judgment (S1) holds no locus view; treated as AGNOS (P20 logic,
      P44b).'
    note: 'Evidence: S1 §2.'
  B_cause:
    value: 'UNKNOWN'
    how_known: Not addressed in the sources read.
  C_ledger:
    value: 'UNKNOWN'
    how_known: Not addressed in the sources read.
  D_authority:
    value: 'UNKNOWN'
    how_known: Not addressed in the sources read.
  E_scope:
    value: 'UNKNOWN'
    how_known: Not addressed in the sources read.
epistemology:
  value: 'Core topic: Humean (induction), Cartesian (external world via closure + skeptical hypotheses),
    Pyrrhonian (universal suspension; Agrippa trilemma). Responses: foundationalism, coherentism, infinitism,
    contextualism, etc.'
  certainty: 1.0
  cites: *id001
  how_known: SEP entire entry.
ethics:
  value: Not a shared ethical programme; Pyrrhonians sought ataraxia via suspension amid disagreement
  certainty: 0.7
  cites:
  - source: S1
    locator: §6
  how_known: SEP. 0.7.
practice:
  ritual_and_practice:
    value: 'Philosophical method (modes, thought experiments); not a church'
    certainty: 1.0
    cites: *id001
    how_known: SEP.
  community_form:
    value: Academic epistemology; ancient schools historically
    certainty: 1.0
    cites: *id001
    how_known: SEP.
science:
  historical_stance:
    value: Humean form targets inductive science foundations; philosophy of science often traces to that
      problem
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; §3
    how_known: SEP.
  current_stance:
    value: 'Live analytic research on closure, contextualism, hinge epistemology, etc.'
    certainty: 1.0
    cites: *id001
    how_known: SEP.
schools_and_variants:
- name: Humean skepticism
  form: scholastic or philosophical
  how_it_differs: Blocks non-deductive expansion of knowledge (induction)
  lio_difference: Not rescored
  certainty: 1.0
  cites:
  - source: S1
    locator: §3
- name: Cartesian skepticism
  form: scholastic or philosophical
  how_it_differs: External-world doubt via skeptical hypotheses + closure
  lio_difference: Not rescored
  certainty: 1.0
  cites:
  - source: S1
    locator: §4
- name: Pyrrhonian skepticism
  form: scholastic or philosophical
  how_it_differs: Universal suspension; Agrippa modes
  lio_difference: Strongest A/B UNKNOWN pressure
  certainty: 1.0
  cites:
  - source: S1
    locator: §6
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Not a census religion; philosophical position
    certainty: 1.0
    cites: *id001
    how_known: SEP.
v7_1_rubric:
  label: authorial v7.1 scores
  L: 9
  P: 9
  E: 10
  V: 10
  X: 8
  total: 46
  scoring_note: 'Scepticism scores high for its rigorous promotion of doubt and evidence, fostering critical
    thinking essential for genius-level inquiry, though it may limit absolute commitments.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 20 and section 7 scoring notes'
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
  use_when: "The person's own writing adopts philosophical skepticism (suspension of judgment) as the\
    \ main worldview, e.g. Hume's own 'mitigated' scepticism (candidate, stage 3)."
  do_not_use_when: Scientific caution or doubt about religion alone is not SCEPT; suspension on God only
    is AGNOS.
  neighbors:
  - code: AGNOS
    relation: neighbor (easily confused)
    note: God-focused vs general knowledge challenge
  - code: NIHIL
    relation: overlaps
    note: Epistemic nihilism
  - code: EMPIR
    relation: neighbor (easily confused)
    note: Positive empiricism ≠ skepticism
review:
  data_quality_flags: []
  open_questions:
  - Pyrrhonian self-refutation debates — keep UNKNOWN on axes.
  - Ordinary “I’m skeptical” speech ≠ SCEPT code.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Juan Comesaña; Peter Klein
  year: 2026
  citation: 'Juan Comesaña and Peter Klein. "Skepticism." Stanford Encyclopedia of Philosophy. First published
    December 8, 2001; substantive revision January 11, 2026. https://plato.stanford.edu/entries/skepticism/.'
  url: 'https://plato.stanford.edu/entries/skepticism/'
  accessed: '2026-10-25'
  reliability_note: Peer-reviewed reference entry.
---
# Skepticism (philosophical) (SCEPT)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1). The v7.1 scores and note are unchanged.

## Summary

Philosophical skepticism claims we should suspend judgment on propositions common sense treats as known [S1]. SEP organizes three forms: Humean (induction), Cartesian (external world), and Pyrrhonian (universal) [S1].

## Core metaphysics

Not a shared theology or afterlife doctrine [S1]. Epistemology is the subject: justification, knowledge, Agrippa’s trilemma [S1].

## Position on the LIO axes

Axes left as previously coded (see front matter); this pass fills qualities without rescoring.

## Schools and variants

Humean; Cartesian; Pyrrhonian [S1].

## Science

Humean form is a standing problem for inductive science; live analytic literature [S1].

## Coding guidance

Philosophical skepticism about knowledge → SCEPT. Religious “I don’t know about God” alone → AGNOS. Extreme “nothing is true/valuable” may be NIHIL.

## v7.1 scoring note

Authorial v7.1 note unchanged (see front matter).

## Open questions

- Pyrrhonian self-refutation debates — keep UNKNOWN on axes.
- Ordinary “I’m skeptical” speech ≠ SCEPT code.

## Research log

- Prior fill from SEP Skepticism.
- 2026-10-25: deepened TODOs; re-read SEP (Comesaña/Klein; updated 2026).
