---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 4
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S1 for Jason)
  model_used: Grok Bot executor agent; direct reads of the cited pages
  collected_on: 2026-10-01
  last_updated: '2026-10-15'
  change_log:
  - date: 2026-10-01
    by: scripts/make_system_stubs.py
    summary: Stub created from v7.1 data book table 4 and section 7.
  - date: 2026-10-02
    by: scripts/make_system_stubs.py
    summary: 'Decision P7: E_scope note added. E is not scored in a stub; when it is, score it on the world''s order (same rules for every kind of being and event, no in-group exceptions in this-world events). Salvation and moral community go on C_ledger.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'Draft (systems batch S1): filled from SEP "Rationalism vs. Empiricism" (Markie and Folescu). An epistemology: D 3 at 0.5; A, C and E UNKNOWN; B BELOW_THRESHOLD. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S1 audit (WEAKEN): D_authority 3 (0.5) → BELOW_THRESHOLD, alternative 3, under P44(b).'
identity:
  id: EMPIR
  v7_1_number: 4
  v7_1_label: Empiricism
  display_label: Empiricism
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: epistemic stance
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: 'SEP: a thesis about the sources of knowledge, relative to a subject area.'
  family:
    value: Epistemology (empiricism versus rationalism)
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: SEP.
  parent_traditions:
    value: TODO
  related_codes: []
origins:
  founding_era:
    value: TODO
  founding_region:
    value: TODO
  founders_or_key_figures:
    value:
    - John Locke
    - George Berkeley
    - David Hume
    - Thomas Reid
    certainty: 0.7
    cites:
    - source: S1
      locator: §1, §3
    how_known: SEP lists 'Locke, Hume, and Reid, the British Empiricists' and warns the classification 'should only be adopted with great caution'. 0.7.
  key_texts: []
metaphysics:
  god_nature_relation:
    value: Not addressed by the thesis; individual empiricists differ.
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S1
      locator: §1
    how_known: SEP defines the thesis without theology.
  deity_personal:
    value: TODO
    stance: TODO
  intervention:
    value: TODO
    stance: TODO
  miracles:
    value: TODO
    stance: TODO
  petition_and_prayer:
    value: TODO
    stance: TODO
  afterlife:
    value: TODO
    stance: TODO
  moral_ledger:
    value: TODO
    stance: TODO
  authority:
    value: 'Experience: ''We have no source of knowledge in S or for the concepts we use in S other than experience.'''
    stance: observation and reason
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: SEP, Empiricism Thesis.
  reserved_exemptions:
    value: TODO
    stance: TODO
  teleology_in_nature:
    value: TODO
    stance: TODO
  necessity_and_freedom:
    value: TODO
lio_axes:
  A_locus:
    value: UNKNOWN
    how_known: The Empiricism Thesis is about knowledge; SEP gives no locus view for empiricism as such.
  B_cause:
    value: BELOW_THRESHOLD
    how_known: SEP reports Hume on causation (known by habit, not reason), which bears on knowledge of laws but not on whether exceptions occur.
    note: 'Evidence: S1 §1 on Hume''s causation.'
  C_ledger:
    value: UNKNOWN
    how_known: Not addressed.
  D_authority:
    value: BELOW_THRESHOLD
    how_known: 'P44(b): the Empiricism Thesis is relative to subject area and Locke put reason ''on equal footing with experience'', so members differ; the sources read do not mention revelation.'
    note: 'Alternative: 3 (observation and reason over revelation in the covered areas). Changed from 3 (0.5) after the S1 audit.'
    alternatives:
    - value: 3
      note: Coder's first reading in batch S1.
      cites:
      - source: S1
        locator: §1
  E_scope:
    value: UNKNOWN
    how_known: Not addressed.
epistemology:
  value: TODO
ethics:
  value: TODO
practice:
  ritual_and_practice:
    value: TODO
  community_form:
    value: TODO
science:
  historical_stance:
    value: TODO
  current_stance:
    value: TODO
schools_and_variants: []
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: TODO
v7_1_rubric:
  label: authorial v7.1 scores
  L: 10
  P: 10
  E: 10
  V: 10
  X: 9
  total: 49
  scoring_note: Empiricism is foundational to science, scoring high for its evidence-driven approach, with minor deduction for induction limitations.
  source: v7.1 data book, section 6 table (tables[4]) row 4 and section 7 scoring notes
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
  use_when: The person's own writing makes experience the only source of knowledge (the Empiricism Thesis) and that is their main stated worldview.
  do_not_use_when: 'Do not use for scientists by default: empiricism is an epistemology and sets no God-view (S1). Score axes from the person''s own statements.'
  neighbors: []
review:
  data_quality_flags: []
  open_questions:
  - How to score A and B for an epistemology with no stated theology (ruling question).
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Peter Markie; M. Folescu
  year: 2021
  citation: Markie, Peter, and M. Folescu. "Rationalism vs. Empiricism." Stanford Encyclopedia of Philosophy. First published August 19, 2004; substantive revision September 2, 2021. https://plato.stanford.edu/entries/rationalism-empiricism/.
  url: https://plato.stanford.edu/entries/rationalism-empiricism/
  accessed: '2026-10-15'
  reliability_note: Peer-reviewed reference entry.
---

# Empiricism (EMPIR)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1). The v7.1 scores and note are unchanged.

## Summary

Empiricism holds that 'We have no source of knowledge in S or for the concepts we use in S other than experience' [S1, §1]. SEP warns that the Locke–Hume–Reid camp versus Descartes–Spinoza–Leibniz 'should only be adopted with great caution' [S1].

## Core metaphysics

None as such: a thesis about knowledge [S1].

## Position on the LIO axes

- D BELOW_THRESHOLD (alt 3): experience the only source in the covered areas, but members differ [S1, §1].
- B BELOW_THRESHOLD: Hume on causation [S1].
- A, C, E UNKNOWN.

## Schools and variants

Subject-relative forms: an empiricist about some subjects may be a rationalist about others [S1, §1].

## Science

TODO

## Coding guidance

Use only when the person's main stated worldview is the Empiricism Thesis; never as a default for scientists.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> EMPIR (49/50) — Empiricism. Empiricism is foundational to science, scoring high for its evidence-driven approach, with minor deduction for induction limitations.

## Open questions

- A and B for a pure epistemology (ruling question).
- Adherents are TODO.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7 (score E on the world's order when the stub is filled).
- 2026-10-15 (systems batch S1): read the listed sources; quotations checked word for word against the fetched page text with a script. Britannica Top Questions boxes (AI-generated) not used.
- 2026-10-15 (S1 audit fixes, run 1: 5 HOLD, 2 WEAKEN): D_authority to BELOW_THRESHOLD (alt 3) under P44(b).
