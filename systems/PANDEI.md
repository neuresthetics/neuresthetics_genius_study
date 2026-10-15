---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 4
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
    summary: 'Draft (systems batch S6, P45 lower tier): filled from Lane, Zygon 2021 (peer-reviewed). A 4, B 4, D 4 at 0.5 (P45 cap); C, E UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S6 audit fix: confirmed only Lane’s general claims are scored; 0.5 cap and advocate flag kept.'
identity:
  id: PANDEI
  v7_1_number: 25
  v7_1_label: Pandeism
  display_label: Pandeism
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: metaphysical thesis
    certainty: 0.5
    cites:
    - source: S1
      locator: introduction
    how_known: P45 lower tier, capped 0.5.
  family:
    value: TODO
  parent_traditions:
    value: TODO
  related_codes: []
origins:
  founding_era:
    value: 'The term: ''The first scholarly use of “pandeist” (Ger. Pandeisten) to denote a doctrine distinct from deism and pantheism came only in the mid-nineteenth century'''
    certainty: 0.5
    cites:
    - source: S1
      locator: introduction
    how_known: P45 lower tier (Lane citing Mapson 2016).
  founding_region:
    value: TODO
  founders_or_key_figures:
    value: TODO
  key_texts: []
metaphysics:
  god_nature_relation:
    value: '''Pandeism is the belief that God chose to wholly become our Universe, imposing principles at this Becoming that have fostered the lawful evolution of multifarious structures''.'
    stance: identity
    certainty: 0.5
    cites:
    - source: S1
      locator: abstract
    how_known: P45 lower tier.
  deity_personal:
    value: TODO
    stance: TODO
  intervention:
    value: TODO
    stance: TODO
  miracles:
    value: '''Against theism, pandeism argues that miracles in Hume’s sense do not exist''.'
    stance: denied
    certainty: 0.5
    cites:
    - source: S1
      locator: introduction
    how_known: P45 lower tier.
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
    value: 4
    rationale: 'God wholly became the Universe: identity with the world.'
    certainty: 0.5
    cites:
    - source: S1
      locator: abstract
    how_known: P45 cap 0.5.
  B_cause:
    value: 4
    rationale: No miracles in Hume's sense; lawful evolution from principles imposed at the Becoming.
    certainty: 0.5
    cites:
    - source: S1
      locator: introduction
    how_known: P45 cap 0.5.
  C_ledger:
    value: UNKNOWN
    how_known: Not addressed in the sources read.
  D_authority:
    value: 4
    rationale: Pandeism 'allies itself with science both substantively and methodologically'.
    certainty: 0.5
    cites:
    - source: S1
      locator: introduction
    how_known: P45 cap 0.5; the author advocates a specific form (living God pandeism).
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
schools_and_variants:
- name: Living God pandeism (LGP)
  form: scholastic or philosophical
  how_it_differs: The Universe 'inherits all of God’s unsurpassable attributes'.
  lio_difference: None stated.
  certainty: 0.5
  cites:
  - source: S1
    locator: abstract
- name: Death of God pandeism (DGP)
  form: scholastic or philosophical
  how_it_differs: God ceases to exist at the Becoming.
  lio_difference: None stated.
  certainty: 0.5
  cites:
  - source: S1
    locator: God’s Reason for Becoming
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
  scoring_note: Pandeism scores high for its elegant synthesis of theism and naturalism, providing a coherent, empirically friendly alternative to interventionist religions, though slightly limited by its speculative transformative premise.
  source: v7.1 data book, section 6 table (tables[4]) row 25 and section 7 scoring notes
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
  use_when: The person's own writing holds that God became the universe (not a creator who withdrew, DEISM; not God = Nature without a Becoming, PANT).
  do_not_use_when: Spinoza is PANT; a creator who stays distinct is DEISM.
  neighbors: []
review:
  data_quality_flags:
  - P45 lower tier only (one peer-reviewed advocate article); all claims capped at 0.5.
  open_questions:
  - An encyclopedia or survey source.
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
  reliability_note: 'P45 lower tier: peer-reviewed journal article (an anonymous reviewer is thanked) by an independent researcher who advocates pandeism; claims capped at 0.5. No encyclopedia entry exists (SEP, IEP none; Britannica pandeism page has no text). Only Lane’s general claims about pandeism are scored (A: definition; B: no Humean miracles; D: alliance with science); his living-God-pandeism (LGP) arguments are not (S6 audit fix).'
---

# Pandeism (PANDEI)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

Lane (Zygon, 2021): 'Pandeism is the belief that God chose to wholly become our Universe' [S1]. P45 lower tier; capped at 0.5.

## Core metaphysics

God became the world; no Humean miracles [S1].

## Position on the LIO axes

- A 4, B 4, D 4 (all 0.5, P45).
- C, E UNKNOWN.

## Schools and variants

Living God and death of God pandeism [S1].

## Science

TODO

## Coding guidance

God-became-universe only.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> PANDEI (44/50) — Pandeism. Pandeism scores high for its elegant synthesis of theism and naturalism, providing a coherent, empirically friendly alternative to interventionist religions, though slightly limited by its speculative transformative premise.

## Open questions

- Encyclopedia source.
- Adherents are TODO.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7 (score E on the world's order when the stub is filled).
- 2026-10-15 (systems batch S6): read the listed sources; quotations checked word for word against the fetched page text. Britannica Top Questions (AI-generated) not used. Axes under P44; PANDEI and PANEND under P45.
- 2026-10-15 (S6 audit fix): scope note on Lane.
