---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 3
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S4 for Jason)
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
    summary: 'Draft (systems batch S4): filled from SEP "Skepticism" (Comesaña and Klein). A BELOW_THRESHOLD (suspension, as AGNOS); others UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
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
    value: Epistemology (Pyrrhonian, Cartesian, Humean forms)
    certainty: 1.0
    cites:
    - source: S1
      locator: §2–6
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
    value: TODO
  key_texts: []
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
    how_known: Universal suspension of judgment (S1) holds no locus view; treated as AGNOS (P20 logic, P44b).
    note: 'Evidence: S1 §2.'
  B_cause:
    value: UNKNOWN
    how_known: Not addressed in the sources read.
  C_ledger:
    value: UNKNOWN
    how_known: Not addressed in the sources read.
  D_authority:
    value: UNKNOWN
    how_known: Not addressed in the sources read.
  E_scope:
    value: UNKNOWN
    how_known: Not addressed in the sources read.
epistemology:
  value: '''Pyrrhonian Skepticism, then, is universal skepticism'': ''the Pyrrhonian skeptic suspends judgment''.'
  certainty: 1.0
  cites:
  - source: S1
    locator: §2
  how_known: SEP.
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
  P: 9
  E: 10
  V: 10
  X: 8
  total: 46
  scoring_note: Scepticism scores high for its rigorous promotion of doubt and evidence, fostering critical thinking essential for genius-level inquiry, though it may limit absolute commitments.
  source: v7.1 data book, section 6 table (tables[4]) row 20 and section 7 scoring notes
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
  use_when: The person's own writing adopts philosophical skepticism (suspension of judgment) as the main worldview, e.g. Hume's own 'mitigated' scepticism (candidate, stage 3).
  do_not_use_when: Scientific caution or doubt about religion alone is not SCEPT; suspension on God only is AGNOS.
  neighbors: []
review:
  data_quality_flags: []
  open_questions:
  - Ancient Skepticism (SEP) not yet read for the school history.
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Juan Comesaña; Peter Klein
  year: 2026
  citation: Juan Comesaña and Peter Klein. "Skepticism." Stanford Encyclopedia of Philosophy. First published December 8, 2001; substantive revision January 11, 2026. https://plato.stanford.edu/entries/skepticism/.
  url: https://plato.stanford.edu/entries/skepticism/
  accessed: '2026-10-15'
  reliability_note: Peer-reviewed reference entry.
---

# Scepticism (Skepticism) (SCEPT)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44. The v7.1 scores and note are unchanged.

## Summary

SEP presents three basic forms of philosophical skepticism (Pyrrhonian, Cartesian, Humean); 'Pyrrhonian Skepticism, then, is universal skepticism' [S1].

## Core metaphysics

Not addressed [S1].

## Position on the LIO axes

- A BELOW_THRESHOLD.
- B to E UNKNOWN.

## Schools and variants

TODO

## Science

TODO

## Coding guidance

Avowed philosophical skeptics; suspension on God only is AGNOS.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> SCEPT (46/50) — Scepticism (Skepticism). Scepticism scores high for its rigorous promotion of doubt and evidence, fostering critical thinking essential for genius-level inquiry, though it may limit absolute commitments.

## Open questions

- School history.
- Adherents are TODO.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7 (score E on the world's order when the stub is filled).
- 2026-10-15 (systems batch S4): read the listed sources; quotations checked word for word against the fetched page text with a script. Axes under P44.
