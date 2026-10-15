---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 3
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
    summary: 'Draft (systems batch S5): filled from SEP "Panpsychism" (Goff, Seager and Allen-Hermanson). A BELOW_THRESHOLD; others UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
identity:
  id: PANPSY
  v7_1_number: 33
  v7_1_label: Panpsychism (consciousness inherent in matter)
  display_label: Panpsychism (consciousness inherent in matter)
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: metaphysical thesis
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: '''the view that mentality is fundamental and ubiquitous in the natural world''.'
  family:
    value: TODO
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
    value: 'Varies: Spinoza''s substance identified with God; William James''s panpsychism grew from neutral monism.'
    stance: varies by school
    certainty: 0.7
    cites:
    - source: S1
      locator: §2
    how_known: SEP.
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
    how_known: 'Panpsychists differ on God (Spinoza versus secular analytic forms) (S1): P44(b).'
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
  L: 8
  P: 8
  E: 7
  V: 9
  X: 7
  total: 39
  scoring_note: Panpsychism scores moderately high as an innovative philosophy bridging consciousness and matter, with strong logical appeal but tempered by speculative elements and incomplete empirical support.
  source: v7.1 data book, section 6 table (tables[4]) row 33 and section 7 scoring notes
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
  use_when: The person's own writing holds that mentality is fundamental and ubiquitous in nature (considered for Riemann, stage 3).
  do_not_use_when: Spinoza is PANT. PANPSY sets no God-view.
  neighbors: []
review:
  data_quality_flags: []
  open_questions:
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Philip Goff; William Seager; Sean Allen-Hermanson
  year: 2022
  citation: Philip Goff and William Seager and Sean Allen-Hermanson. "Panpsychism." Stanford Encyclopedia of Philosophy. First published May 23, 2001; substantive revision May 13, 2022. https://plato.stanford.edu/entries/panpsychism/.
  url: https://plato.stanford.edu/entries/panpsychism/
  accessed: '2026-10-15'
  reliability_note: Peer-reviewed reference entry.
---

# Panpsychism (consciousness inherent in matter) (PANPSY)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44. The v7.1 scores and note are unchanged.

## Summary

'Panpsychism is the view that mentality is fundamental and ubiquitous in the natural world'; proponents see it as 'an attractive middle way between physicalism on the one hand and dualism on the other' [S1].

## Core metaphysics

Mind fundamental; God-view varies [S1].

## Position on the LIO axes

- A BELOW_THRESHOLD.
- B to E UNKNOWN.

## Schools and variants

Cosmopsychism and micropsychism [S1].

## Science

TODO

## Coding guidance

Score axes from the person.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> PANPSY (39/50) — Panpsychism (consciousness inherent in matter). Panpsychism scores moderately high as an innovative philosophy bridging consciousness and matter, with strong logical appeal but tempered by speculative elements and incomplete empirical support.

## Open questions

- Adherents are TODO.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7 (score E on the world's order when the stub is filled).
- 2026-10-15 (systems batch S5): read the listed sources; quotations checked word for word against the fetched page text with a script. Britannica Top Questions (AI-generated) not used. Axes under P44.
