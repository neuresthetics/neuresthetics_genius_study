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
    summary: 'Draft (systems batch S6): filled from SEP "Buddha" (Siderits). A BELOW_THRESHOLD (alt 4); B BELOW_THRESHOLD; C 3 (0.5, alt 4); D, E UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
identity:
  id: BUDDH
  v7_1_number: 35
  v7_1_label: Buddhism
  display_label: Buddhism
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: religion
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
    value: The Buddha, fl. circa 450 BCE
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP.
  founding_region:
    value: TODO
  founders_or_key_figures:
    value:
    - The Buddha
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP.
  key_texts: []
metaphysics:
  god_nature_relation:
    value: TODO
    stance: TODO
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
    value: All sentient beings, 'including humans, non-human animals, gods, and the inhabitants of various hells', undergo rebirth; the ideal is liberation from it.
    stance: rebirth
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: SEP.
  moral_ledger:
    value: '''rebirth is governed by the causal laws of karma (good actions cause pleasant fruit for the agent, evil actions cause unpleasant fruit, etc.)''.'
    stance: karma-type law
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: SEP.
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
    how_known: Gods are among the beings who undergo rebirth, and the tradition competed with 'Brahmanical schools that posit an omniscient creator' (S1), but the entry states no position on God for all schools.
    note: 'Alternative: 4.'
    alternatives:
    - value: 4
      note: Named alternative.
      cites:
      - source: S1
        locator: §2
  B_cause:
    value: BELOW_THRESHOLD
    how_known: Rebirth under causal laws (S1); the entry also reports a passage on supernormal cognitive powers. Not fixed.
    note: 'Evidence: S1.'
  C_ledger:
    value: 3
    rationale: 'Karma: an impersonal causal law that brings good and bad fruit to the agent; no judging person.'
    certainty: 0.5
    cites: &id001
    - source: S1
      locator: §2
    how_known: '0.5: impersonal (toward 4) but still a moral ledger (alternative 4).'
    alternatives:
    - value: 4
      note: Named alternative.
      cites: *id001
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
  E: 7
  V: 7
  X: 5
  total: 37
  scoring_note: Buddhism scores relatively high due to its profound philosophical and practical approach to ending suffering, blending ethics and meditation with strong psychological alignment, but tempered by metaphysical elements like rebirth that reduce empirical compatibility.
  source: v7.1 data book, section 6 table (tables[4]) row 35 and section 7 scoring notes
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
  use_when: The person self-identifies as Buddhist or their own writing adopts its doctrines (karma, rebirth, liberation).
  do_not_use_when: Meditation practice or Buddhist interest alone is not BUDDH; Mahāyāna devotional forms may differ on A.
  neighbors: []
review:
  data_quality_flags: []
  open_questions:
  - Later schools (Mahāyāna, Vajrayāna) not read.
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Mark Siderits
  year: 2023
  citation: Siderits, Mark. "Buddha." Stanford Encyclopedia of Philosophy. First published February 17, 2011; substantive revision March 6, 2023. https://plato.stanford.edu/entries/buddha/.
  url: https://plato.stanford.edu/entries/buddha/
  accessed: '2026-10-15'
  reliability_note: Peer-reviewed reference entry; covers the Buddha’s teachings, not every later school.
---

# Buddhism (BUDDH)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

The Buddha's teachings 'concern the quest for liberation from suffering' [S1]; rebirth 'is governed by the causal laws of karma' [S1].

## Core metaphysics

Rebirth, karma, liberation [S1].

## Position on the LIO axes

- A BELOW_THRESHOLD (alt 4), B BELOW_THRESHOLD.
- C 3 (0.5, alt 4).
- D, E UNKNOWN.

## Schools and variants

TODO

## Science

TODO

## Coding guidance

Self-identified Buddhists.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> BUDDH (37/50) — Buddhism. Buddhism scores relatively high due to its profound philosophical and practical approach to ending suffering, blending ethics and meditation with strong psychological alignment, but tempered by metaphysical elements like rebirth that reduce empirical compatibility.

## Open questions

- Later schools.
- Adherents are TODO.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7 (score E on the world's order when the stub is filled).
- 2026-10-15 (systems batch S6): read the listed sources; quotations checked word for word against the fetched page text. Britannica Top Questions (AI-generated) not used. Axes under P44; PANDEI and PANEND under P45.
