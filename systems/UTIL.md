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
    summary: 'Draft (systems batch S4): filled from SEP "The History of Utilitarianism" (Driver). A BELOW_THRESHOLD (theological and secular utilitarians); others UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
identity:
  id: UTIL
  v7_1_number: 24
  v7_1_label: Utilitarianism
  display_label: Utilitarianism
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: philosophical school or method
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: An approach to normative ethics, 'a species of consequentialism'.
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
    value:
    - Jeremy Bentham
    - John Stuart Mill
    - Henry Sidgwick
    - William Paley
    certainty: 1.0
    cites:
    - source: S1
      locator: §1–3
    how_known: SEP.
  key_texts: []
metaphysics:
  god_nature_relation:
    value: 'Varies: theological utilitarians (Paley; Newcome: ''divine beneficence consists in God’s promotion of happiness'') and classical secular forms.'
    stance: varies by school
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
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
    how_known: 'Theological and secular utilitarians differ (S1): P44(b).'
    note: 'Evidence: S1 §1.'
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
  value: '''the moral quality of an action or policy is entirely a function of its consequences''.'
  certainty: 1.0
  cites:
  - source: S1
    locator: introduction
  how_known: SEP.
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
schools_and_variants:
- name: Theological utilitarianism
  form: scholastic or philosophical
  how_it_differs: Grounds utility in God's design (Paley, Gay, Newcome); 'the lack of any theoretical necessity in appealing to God would result in its diminishing appeal'.
  lio_difference: A toward 0–1.
  certainty: 1.0
  cites:
  - source: S1
    locator: §1
- name: Classical utilitarianism
  form: scholastic or philosophical
  how_it_differs: 'Bentham and Mill: the value to be promoted is pleasure.'
  lio_difference: None stated.
  certainty: 1.0
  cites:
  - source: S1
    locator: §2
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: TODO
v7_1_rubric:
  label: authorial v7.1 scores
  L: 9
  P: 9
  E: 9
  V: 10
  X: 8
  total: 45
  scoring_note: Utilitarianism scores high for its empirical and rational approach to ethics, optimizing for collective good with practical applications, though slightly limited by measurement abstractions and potential oversimplification.
  source: v7.1 data book, section 6 table (tables[4]) row 24 and section 7 scoring notes
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
  use_when: The person's own writing adopts utilitarian ethics as the main worldview (Bentham, Mill).
  do_not_use_when: UTIL sets no God-view; score axes from the person. Effective altruism members are EFFALT.
  neighbors: []
review:
  data_quality_flags: []
  open_questions:
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Julia Driver
  year: 2025
  citation: Julia Driver. "The History of Utilitarianism." Stanford Encyclopedia of Philosophy. First published March 27, 2009; substantive revision July 31, 2025. https://plato.stanford.edu/entries/utilitarianism-history/.
  url: https://plato.stanford.edu/entries/utilitarianism-history/
  accessed: '2026-10-15'
  reliability_note: Peer-reviewed reference entry.
---

# Utilitarianism (UTIL)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44. The v7.1 scores and note are unchanged.

## Summary

Utilitarianism is 'one of the most powerful and persuasive approaches to normative ethics', 'a species of consequentialism' [S1]. Bentham developed 'the first systematic account' [S1].

## Core metaphysics

Varies [S1].

## Position on the LIO axes

- A BELOW_THRESHOLD.
- B to E UNKNOWN.

## Schools and variants

Theological and classical [S1].

## Science

TODO

## Coding guidance

Score axes from the person.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> UTIL (45/50) — Utilitarianism. Utilitarianism scores high for its empirical and rational approach to ethics, optimizing for collective good with practical applications, though slightly limited by measurement abstractions and potential oversimplification.

## Open questions

- Adherents are TODO.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7 (score E on the world's order when the stub is filled).
- 2026-10-15 (systems batch S4): read the listed sources; quotations checked word for word against the fetched page text with a script. Axes under P44.
