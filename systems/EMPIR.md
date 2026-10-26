---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 6
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S1 for Jason)
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
    summary: 'Draft (systems batch S1): filled from SEP "Rationalism vs. Empiricism" (Markie and Folescu).
      An epistemology: D 3 at 0.5; A, C and E UNKNOWN; B BELOW_THRESHOLD. v7.1 scores and note unchanged.
      Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S1 audit (WEAKEN): D_authority 3 (0.5) → BELOW_THRESHOLD, alternative 3, under P44(b).'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'T2: A_locus searched, unchanged; search logged.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from SEP Rationalism vs Empiricism (Markie/Folescu): family/parents, metaphysics
      TODOs as not addressed/varies, ethics/practice/science/schools. Axes unchanged.'
identity:
  id: EMPIR
  v7_1_number: 4
  v7_1_label: Empiricism
  display_label: Empiricism
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: philosophical school or method
    certainty: 1.0
    cites:
    - source: S1
      locator: §1.2
    how_known: SEP epistemology dispute.
  family:
    value: Knowledge and concepts from experience (sense and/or reflection); reject innate knowledge/concepts
      for the subject area
    certainty: 1.0
    cites:
    - source: S1
      locator: §1.2
    how_known: SEP Empiricism Thesis.
  parent_traditions:
    value:
    - 'British empiricism (Locke, Hume, Reid — labels cautioned)'
    - Early modern epistemology
    - Later logical positivism / verificationism strands
    certainty: 0.7
    cites:
    - source: S1
      locator: §1
    how_known: SEP cautions labels. 0.7.
  related_codes:
  - code: RATN
    relation: contrast case
    note: Paired dispute; same SEP entry
  - code: PRAG
    relation: overlaps
    note: Radicalized empiricist attitude
  - code: SCEPT
    relation: overlaps
    note: Humean limits of knowledge
  - code: UTIL
    relation: neighbor (easily confused)
    note: Often co-travel historically; different question
origins:
  founding_era:
    value: Early modern period (17th–18th c.); labels later (Kant onward)
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: SEP.
  founding_region:
    value: Western Europe (esp. Britain in textbook casting); not a single founding city
    certainty: 0.7
    cites:
    - source: S1
      locator: §1
    how_known: '0.7.'
  founders_or_key_figures:
    value:
    - John Locke
    - David Hume
    - Thomas Reid
    - A. J. Ayer (later positivist form)
    certainty: 1.0
    cites:
    - source: S1
      locator: §1–2
    how_known: SEP examples.
  key_texts:
  - value: 'Locke, Essay Concerning Human Understanding; Hume, Enquiry / Treatise; Ayer, Language, Truth
      and Logic'
    certainty: 1.0
    cites:
    - source: S1
      locator: bibliography; §2
    how_known: SEP.
metaphysics:
  god_nature_relation:
    value: Not a shared theology; Locke allows intuition/deduction of God; Hume curtails metaphysics
    stance: varies by school
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: SEP.
  deity_personal:
    value: Varies (Locke theism; Hume skeptical of natural theology)
    stance: varies by school
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: SEP.
  intervention:
    value: Not a shared doctrine
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP.
  miracles:
    value: Hume famously skeptical of miracle testimony; not universal empiricist creed
    stance: varies by school
    certainty: 0.7
    cites:
    - source: S1
      locator: §1.2 (extension)
    how_known: Coder note. 0.7.
  petition_and_prayer:
    value: Not a practice system
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP.
  afterlife:
    value: Not a shared doctrine
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP.
  moral_ledger:
    value: Not a divine ledger as doctrine; moral knowledge debated empirically vs intuition
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: §1
    how_known: '0.7.'
  authority:
    value: Experience (sensation and reflection) as source of ideas/knowledge in the subject area
    stance: observation and reason
    certainty: 1.0
    cites:
    - source: S1
      locator: §1.2
    how_known: SEP.
  reserved_exemptions:
    value: No religious in-group exemption as shared creed
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: introduction
    how_known: '0.7.'
  teleology_in_nature:
    value: Not a shared teleology; Hume challenges necessary connection in nature
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: §2–4
    how_known: '0.7.'
  necessity_and_freedom:
    value: Matters of fact vs relations of ideas (Hume); necessity often linguistic/conceptual for empiricists;
      free will not the core EMPIR thesis
    certainty: 0.7
    cites:
    - source: S1
      locator: §2
    how_known: '0.7.'
lio_axes:
  A_locus:
    value: 'UNKNOWN'
    how_known: The Empiricism Thesis is about knowledge; SEP gives no locus view for empiricism as such.
  B_cause:
    value: 'BELOW_THRESHOLD'
    how_known: 'SEP reports Hume on causation (known by habit, not reason), which bears on knowledge of
      laws but not on whether exceptions occur.'
    note: "Evidence: S1 §1 on Hume's causation."
  C_ledger:
    value: 'UNKNOWN'
    how_known: Not addressed.
  D_authority:
    value: 'BELOW_THRESHOLD'
    how_known: "P44(b): the Empiricism Thesis is relative to subject area and Locke put reason 'on equal\
      \ footing with experience', so members differ; the sources read do not mention revelation."
    note: 'Alternative: 3 (observation and reason over revelation in the covered areas). Changed from
      3 (0.5) after the S1 audit.'
    alternatives:
    - value: 3
      note: "Coder's first reading in batch S1."
      cites:
      - source: S1
        locator: §1
  E_scope:
    value: 'UNKNOWN'
    how_known: Not addressed.
epistemology:
  value: 'Empiricism Thesis: no source of knowledge/concepts in subject S other than experience; reject
    innate knowledge and innate concepts for that S'
  certainty: 1.0
  cites:
  - source: S1
    locator: §1.2
  how_known: SEP.
ethics:
  value: 'Extension: some empiricists treat morals as sentiment/taste (Hume); others allow empirical inquiry
    into moral facts; not one school ethics'
  certainty: 0.7
  cites:
  - source: S1
    locator: §1; §2
  how_known: SEP. 0.7.
practice:
  ritual_and_practice:
    value: Philosophical method and critique of a priori metaphysics; not a church
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP.
  community_form:
    value: Academic tradition; textbook “British empiricists” cluster (labels cautioned)
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: SEP.
science:
  historical_stance:
    value: Allies with experimental natural philosophy; curtails speculative metaphysics
    certainty: 1.0
    cites:
    - source: S1
      locator: §1–2
    how_known: SEP.
  current_stance:
    value: 'Live in philosophy of science, experimental philosophy debates, and critiques of a priori
      method'
    certainty: 0.7
    cites:
    - source: S1
      locator: §1
    how_known: '0.7.'
schools_and_variants:
- name: Classical British empiricism (Locke–Hume–Reid cluster)
  form: scholastic or philosophical
  how_it_differs: Tabula rasa / impressions-ideas; Reid common-sense variant
  lio_difference: Not rescored
  certainty: 1.0
  cites:
  - source: S1
    locator: §1
- name: Logical positivism / verificationism
  form: modern
  how_it_differs: Cognitively meaningful = tautology or empirically verifiable (Ayer)
  lio_difference: Not rescored
  certainty: 1.0
  cites:
  - source: S1
    locator: §2
- name: Subject-relative empiricism
  form: scholastic or philosophical
  how_it_differs: Can be empiricist in physics and rationalist in math — SEP relativizes by subject
  lio_difference: 'Coding: specify subject'
  certainty: 1.0
  cites:
  - source: S1
    locator: §1
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: 'Philosophical position, not a census religion'
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP.
v7_1_rubric:
  label: authorial v7.1 scores
  L: 10
  P: 10
  E: 10
  V: 10
  X: 9
  total: 49
  scoring_note: 'Empiricism is foundational to science, scoring high for its evidence-driven approach,
    with minor deduction for induction limitations.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 4 and section 7 scoring notes'
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
  use_when: Person’s epistemology centers experience as sole source for the relevant subject; rejects
    innate knowledge/concepts there.
  do_not_use_when: Mere “practical” or scientific attitude without the empiricist thesis; do not auto-code
    all scientists EMPIR.
  neighbors:
  - code: RATN
    relation: contrast case
    note: Paired SEP dispute
  - code: PRAG
    relation: overlaps
    note: Empiricist attitude radicalized
  - code: SCEPT
    relation: overlaps
    note: Humean limits
review:
  data_quality_flags: []
  open_questions:
  - Keep subject-relative coding note prominent?
  - Split positivism later?
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Peter Markie; M. Folescu
  year: 2021
  citation: 'Markie, Peter and M. Folescu, “Rationalism vs. Empiricism,” Stanford Encyclopedia of Philosophy
    (Fall 2021 Edition), Edward N. Zalta (ed.).'
  url: 'https://plato.stanford.edu/entries/rationalism-empiricism/'
  accessed: '2026-10-25'
  reliability_note: Peer-reviewed reference entry.
---
# Empiricism (EMPIR)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44. The v7.1 scores and note are unchanged.

## Summary

Empiricism: experience as the source of knowledge and concepts in a subject area; reject innate knowledge/concepts for that area [S1].

## Core metaphysics

Not a shared theology; Locke vs Hume diverge on God/metaphysics. Method curtails speculative a priori metaphysics [S1].

## Position on the LIO axes

Axes left UNKNOWN / BELOW_THRESHOLD as prior; this pass fills qualities only.

## Schools and variants

Classical British cluster; logical positivism; subject-relative empiricism [S1].

## Science

Allies with experimental natural philosophy [S1].

## Coding guidance

Empiricist thesis for the relevant subject → EMPIR. Scientist ≠ automatic EMPIR.

## v7.1 scoring note

Authorial v7.1 note unchanged (see front matter).

## Open questions

- Keep subject-relative coding note prominent?
- Split positivism later?

## Research log

- 2026-10-25: deepened from SEP Rationalism vs Empiricism; axes unchanged.
