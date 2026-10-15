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
  - date: 2026-10-01
    by: scripts/make_system_stubs.py
    summary: Coding guidance and neighbors from the PANT boundary rules (OPEN_DECISIONS S6).
  - date: 2026-10-02
    by: scripts/make_system_stubs.py
    summary: 'Decision P7: E_scope note added. E is not scored in a stub; when it is, score it on the world''s order (same rules for every kind of being and event, no in-group exceptions in this-world events). Salvation and moral community go on C_ledger.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'Draft (systems batch S5): filled from SEP "Panentheism" (Culp). A 2 (0.7); B BELOW_THRESHOLD (alt 2); C, D, E UNKNOWN. S6 rule kept. v7.1 scores and note unchanged. Not reviewed.'
identity:
  id: PANENT
  v7_1_number: 30
  v7_1_label: Panentheism (Process Theology, some Kabbalah/Advaita forms)
  display_label: Panentheism (Process Theology, some Kabbalah/Advaita forms)
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: family of positions
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: 'SEP: ''a rich diversity of panentheistic understandings''.'
  family:
    value: TODO
  parent_traditions:
    value: TODO
  related_codes:
  - code: PANT
    relation: neighbor (easily confused)
    note: God identified with Nature, with nothing beyond it (S6)
  - code: HINDU
    relation: neighbor (easily confused)
    note: Advaita Vedanta defaults to HINDU (S6)
  - code: JUDA
    relation: neighbor (easily confused)
    note: Kabbalah defaults to JUDA (S6)
origins:
  founding_era:
    value: Term first used by Karl Krause in 1821
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: SEP.
  founding_region:
    value: TODO
  founders_or_key_figures:
    value:
    - Karl Krause
    - Alfred North Whitehead
    - Charles Hartshorne
    - Philip Clayton
    - Arthur Peacocke
    certainty: 0.7
    cites:
    - source: S1
      locator: §1–3
    how_known: SEP names them as sources or advocates; 0.7.
  key_texts: []
metaphysics:
  god_nature_relation:
    value: '''Panentheism considers God and the world to be inter-related with the world being in God and God being in the world'', ''without losing the distinct identity of either God or the world''.'
    stance: God in Nature and beyond it
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP.
  deity_personal:
    value: TODO
    stance: TODO
  intervention:
    value: Varies; for some, 'Neither God’s actions nor the world is completely determined', and history is 'the result of divine persuasion and is open' (Clayton).
    stance: varies by school
    certainty: 0.7
    cites:
    - source: S1
      locator: §3
    how_known: SEP; forms differ.
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
    rationale: 'The world in God and God in the world, with distinct identities: the middle of the axis.'
    certainty: 0.7
    cites:
    - source: S1
      locator: introduction
    how_known: Stated by SEP; specific forms differ, so 0.7.
  B_cause:
    value: BELOW_THRESHOLD
    how_known: 'Forms differ (S1): divine persuasion and top-down causation in some, laws chosen by God in others.'
    note: 'Alternative: 2.'
    alternatives:
    - value: 2
      note: Named alternative.
      cites:
      - source: S1
        locator: §3
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
  E: 8
  V: 9
  X: 7
  total: 42
  scoring_note: Panentheism scores high for its dynamic integration of divinity with the universe, providing philosophical depth and compatibility with science, though slightly limited by transcendent metaphysical elements.
  source: v7.1 data book, section 6 table (tables[4]) row 30 and section 7 scoring notes
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
  use_when: 'v8 rule (decision S6, 2026-10-01): the person''s own writing keeps a divine reality that includes the world but also exceeds it. v7.1''s label names ''some Kabbalah/Advaita forms''; use PANENT for those only when the person''s writing says this.'
  do_not_use_when: 'Advaita Vedanta or Kabbalah by membership alone: code the host tradition (HINDU, JUDA) as primary. God identified with Nature as a whole, with nothing beyond it: PANT, if the two-part test is passed.'
  neighbors:
  - code: PANT
    relation: neighbor (easily confused)
  - code: HINDU
    relation: neighbor (easily confused)
  - code: JUDA
    relation: neighbor (easily confused)
review:
  data_quality_flags:
  - v7.1 table 4 label is truncated; v7_1_label is taken from the section 7 scoring note.
  open_questions:
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: John Culp
  year: 2023
  citation: John Culp. "Panentheism." Stanford Encyclopedia of Philosophy. First published December 4, 2008; substantive revision April 24, 2023. https://plato.stanford.edu/entries/panentheism/.
  url: https://plato.stanford.edu/entries/panentheism/
  accessed: '2026-10-15'
  reliability_note: Peer-reviewed reference entry.
---

# Panentheism (Process Theology, some Kabbalah/Advaita forms) (PANENT)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44. The v7.1 scores and note are unchanged.

## Summary

'Panentheism considers God and the world to be inter-related with the world being in God and God being in the world' [S1]. Krause first used the label in 1821; modern forms developed 'under the influence of German Idealism, Whiteheadian process philosophy, and current scientific thought' [S1].

## Core metaphysics

God includes and exceeds the world [S1].

## Position on the LIO axes

- A 2 (0.7).
- B BELOW_THRESHOLD (alt 2).
- C, D, E UNKNOWN.

## Schools and variants

TODO

## Science

TODO

## Coding guidance

S6 rule: a divine reality that includes the world but also exceeds it. Kabbalah defaults to JUDA and Advaita to HINDU.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> PANENT (42/50) — Panentheism (Process Theology, some Kabbalah/Advaita forms). Panentheism scores high for its dynamic integration of divinity with the universe, providing philosophical depth and compatibility with science, though slightly limited by transcendent metaphysical elements.

## Open questions

- Adherents are TODO.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7 (score E on the world's order when the stub is filled).
- 2026-10-15 (systems batch S5): read the listed sources; quotations checked word for word against the fetched page text with a script. Britannica Top Questions (AI-generated) not used. Axes under P44.
