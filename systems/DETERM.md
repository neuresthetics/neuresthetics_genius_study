---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 4
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S5 for Jason)
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
    summary: 'Draft (systems batch S5): filled from SEP "Causal Determinism" (Hoefer). A BELOW_THRESHOLD; B 4 (0.7); E 4 (0.5); C, D UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S5 audit follow-up: E_scope note citing P44(b). No value change.'
identity:
  id: DETERM
  v7_1_number: 28
  v7_1_label: Determinism
  display_label: Determinism
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: metaphysical thesis
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP.
  family:
    value: TODO
  parent_traditions:
    value: TODO
  related_codes: []
origins:
  founding_era:
    value: Ancient; 'first became subject to clarification and mathematical analysis in the eighteenth century'
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP.
  founding_region:
    value: TODO
  founders_or_key_figures:
    value:
    - Pierre-Simon Laplace
    - Gottfried Wilhelm Leibniz
    certainty: 0.7
    cites:
    - source: S1
      locator: §1–2
    how_known: SEP quotes Laplace and discusses Leibniz; 0.7.
  key_texts: []
metaphysics:
  god_nature_relation:
    value: 'Not fixed: determinism and theological views are ''easy to disentangle, barring certain strong theological commitments''; for Leibniz God may will that things be so.'
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: SEP.
  deity_personal:
    value: TODO
    stance: TODO
  intervention:
    value: 'None within the thesis: ''every event is necessitated by antecedent events and conditions together with the laws of nature''.'
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: introduction
    how_known: SEP's rough definition; 0.7.
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
    value: TODO
    stance: TODO
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
    value: BELOW_THRESHOLD
    how_known: 'The thesis is compatible with and without God (S1 §2): members differ (P44b).'
    note: 'Evidence: S1 §2.'
  B_cause:
    value: 4
    rationale: 'Every event necessitated by antecedent conditions and the laws of nature: no exceptions and no chance (P40).'
    certainty: 0.7
    cites:
    - source: S1
      locator: introduction
    how_known: Fixed by the stance; 0.7 because SEP gives the definition 'roughly speaking'.
  C_ledger:
    value: UNKNOWN
    how_known: Not addressed in the sources read.
  D_authority:
    value: UNKNOWN
    how_known: Not addressed in the sources read.
  E_scope:
    value: 4
    rationale: 'On the world''s order (P7): every event under the same laws, so no group is exempt.'
    certainty: 0.5
    cites:
    - source: S1
      locator: introduction
    how_known: 'Implied by the stance, not stated: 0.5.'
    note: 'P44(b): the stance itself fixes E (every event under the same laws, so no exception for any group); hence a score, not UNKNOWN.'
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
  L: 9
  P: 8
  E: 9
  V: 9
  X: 8
  total: 43
  scoring_note: Determinism scores high for its logical rigor and alignment with empirical causality, providing a foundational view of reality, but tempered by ongoing debates in quantum physics and free will.
  source: v7.1 data book, section 6 table (tables[4]) row 28 and section 7 scoring notes
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
  use_when: The person's own writing affirms causal determinism as the main worldview (considered for Spinoza, stage 3).
  do_not_use_when: A determinist physics alone does not make the worldview DETERM; Spinoza's God-or-Nature is PANT.
  neighbors: []
review:
  data_quality_flags: []
  open_questions:
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Carl Hoefer
  year: 2023
  citation: Carl Hoefer. "Causal Determinism." Stanford Encyclopedia of Philosophy. First published January 23, 2003; substantive revision September 21, 2023. https://plato.stanford.edu/entries/determinism-causal/.
  url: https://plato.stanford.edu/entries/determinism-causal/
  accessed: '2026-10-15'
  reliability_note: Peer-reviewed reference entry.
---

# Determinism (DETERM)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44. The v7.1 scores and note are unchanged.

## Summary

'Causal determinism is, roughly speaking, the idea that every event is necessitated by antecedent events and conditions together with the laws of nature' [S1].

## Core metaphysics

Lawful necessitation; compatible with theism or not [S1].

## Position on the LIO axes

- A BELOW_THRESHOLD.
- B 4 (0.7), E 4 (0.5).
- C, D UNKNOWN.

## Schools and variants

TODO

## Science

Whether quantum mechanics is non-deterministic is 'highly debatable' [S1].

## Coding guidance

Stated determinist worldview only.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> DETERM (43/50) — Determinism. Determinism scores high for its logical rigor and alignment with empirical causality, providing a foundational view of reality, but tempered by ongoing debates in quantum physics and free will.

## Open questions

- Adherents are TODO.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7 (score E on the world's order when the stub is filled).
- 2026-10-15 (systems batch S5): read the listed sources; quotations checked word for word against the fetched page text with a script. Britannica Top Questions (AI-generated) not used. Axes under P44.
- 2026-10-15 (S5 audit follow-up): E_scope note added (P44(b)).
