---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 3
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S6 for Jason)
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
    summary: 'Draft (systems batch S6, P45 lower tier): filled from one passage in Lane, Zygon 2021. A 2 (0.5); B BELOW_THRESHOLD; rest UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
identity:
  id: PANEND
  v7_1_number: 26
  v7_1_label: Panendeism
  display_label: Panendeism
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: TODO
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
    value: '''Panentheism and panendeism offer other maps. On each of them, God exceeds the Universe; the Universe exists in God.'''
    stance: God in Nature and beyond it
    certainty: 0.5
    cites:
    - source: S1
      locator: introduction
    how_known: 'P45 lower tier: one defining passage.'
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
    value: 2
    rationale: God exceeds the Universe; the Universe exists in God.
    certainty: 0.5
    cites:
    - source: S1
      locator: introduction
    how_known: P45 cap 0.5; one passage.
  B_cause:
    value: BELOW_THRESHOLD
    how_known: '''God therefore retains power to intervene in the world “from outside”'' (S1): a power, with no statement on its use.'
    note: 'P45 lower tier. Alternative: 3 (the deist element).'
    alternatives:
    - value: 3
      note: Named alternative.
      cites:
      - source: S1
        locator: introduction
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
  L: 9
  P: 9
  E: 9
  V: 9
  X: 8
  total: 44
  scoring_note: Panendeism scores high for its elegant fusion of deism and pantheism, providing a conscious yet non-interventionist divine model with strong logical and empirical alignment.
  source: v7.1 data book, section 6 table (tables[4]) row 26 and section 7 scoring notes
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
  use_when: The person's own writing names panendeism or holds a non-intervening God in whom the universe exists.
  do_not_use_when: Process theology and other panentheism is PANENT; a creator outside the world is DEISM.
  neighbors: []
review:
  data_quality_flags:
  - 'P45 lower tier only: one defining passage in a pandeist article; deist content of panendeism not sourced.'
  open_questions:
  - A source that defines panendeism at length.
  - Adherents are TODO.
sources:
- id: S1
  type: secondary
  kind: journal article
  author: William C. Lane
  year: 2021
  citation: 'Lane, William C. "Living God Pandeism: Evidential Support." Zygon: Journal of Religion and Science (first published 4 June 2021). https://doi.org/10.1111/zygo.12704.'
  url: https://onlinelibrary.wiley.com/doi/10.1111/zygo.12704
  accessed: '2026-10-15'
  reliability_note: 'P45 lower tier: peer-reviewed journal article (an anonymous reviewer is thanked) by an independent researcher who advocates pandeism; claims capped at 0.5. No encyclopedia entry exists (SEP, IEP none; Britannica pandeism page has no text).'
---

# Panendeism (PANEND)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

Lane (Zygon, 2021) groups panendeism with panentheism: 'God exceeds the Universe; the Universe exists in God' [S1]. P45 lower tier.

## Core metaphysics

Universe in God [S1].

## Position on the LIO axes

- A 2 (0.5).
- B BELOW_THRESHOLD (alt 3).
- C, D, E UNKNOWN.

## Schools and variants

TODO

## Science

TODO

## Coding guidance

Named panendeism only.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> PANEND (44/50) — Panendeism. Panendeism scores high for its elegant fusion of deism and pantheism, providing a conscious yet non-interventionist divine model with strong logical and empirical alignment.

## Open questions

- A fuller source.
- Adherents are TODO.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7 (score E on the world's order when the stub is filled).
- 2026-10-15 (systems batch S6): read the listed sources; quotations checked word for word against the fetched page text. Britannica Top Questions (AI-generated) not used. Axes under P44; PANDEI and PANEND under P45.
