---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 5
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
    summary: 'Draft (systems batch S6): filled from IEP "Jain Philosophy" (Webb) and Britannica "Jainism" (Dundas). A 3 (0.5, alt 4); C 3 (0.5, alt 4); E 4 (0.5); B, D UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S6 audit fix: C cites P44(d); Britannica byline credited to Strohl, Dundas and Britannica Editors.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S7 audit fix: rotating Britannica bylines noted (P44(e)).'
identity:
  id: JAIN
  v7_1_number: 37
  v7_1_label: Jainism
  display_label: Jainism
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: religion
    certainty: 1.0
    cites:
    - source: S2
      locator: introduction
    how_known: Britannica.
  family:
    value: TODO
  parent_traditions:
    value: TODO
  related_codes: []
origins:
  founding_era:
    value: 7th–5th century BCE
    certainty: 1.0
    cites:
    - source: S2
      locator: Early history
    how_known: Britannica.
  founding_region:
    value: Ganges basin, eastern India
    certainty: 1.0
    cites:
    - source: S2
      locator: Early history
    how_known: Britannica.
  founders_or_key_figures:
    value:
    - Parshvanatha
    - Mahavira
    certainty: 1.0
    cites:
    - source: S2
      locator: Early history
    how_known: 'Britannica: Jains believe the tradition ''does not have a historical founder''.'
  key_texts: []
metaphysics:
  god_nature_relation:
    value: '''What is denied is a creator god above all. The universe is eternal, matter and souls being equally uncreated. The universe contains gods ... but there is no being outside it exercising control over it.'''
    stance: many gods within nature
    certainty: 1.0
    cites:
    - source: S1
      locator: metaphysics
    how_known: IEP.
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
    value: 3
    rationale: No creator and no being outside the universe; gods exist inside it.
    certainty: 0.5
    cites: &id001
    - source: S1
      locator: metaphysics
    how_known: 'As EPICUR: gods within nature fit 3 (alternative 4).'
    alternatives:
    - value: 4
      note: Named alternative.
      cites: *id001
  B_cause:
    value: UNKNOWN
    how_known: Not addressed in the sources read.
  C_ledger:
    value: 3
    rationale: Karma and rebirth govern gods and humans alike; no judging creator.
    certainty: 0.5
    cites: &id002
    - source: S1
      locator: metaphysics
    how_known: 'Karma rule (P44(d)): an impersonal moral ledger is C 3 @0.5, alternative 4. Karma: impersonal, but still a moral ledger.'
    alternatives:
    - value: 4
      note: Named alternative.
      cites: *id002
  D_authority:
    value: UNKNOWN
    how_known: Not addressed in the sources read.
  E_scope:
    value: 4
    rationale: 'On the world''s order (P7): gods ''are all just as subject to karma and rebirth as human beings are''; no being outside exercises control.'
    certainty: 0.5
    cites:
    - source: S1
      locator: metaphysics
    how_known: 'Implied: 0.5.'
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
  E: 6
  V: 8
  X: 4
  total: 36
  scoring_note: Jainism scores relatively high due to its rigorous ethical system and focus on non-violence, providing strong moral coherence, but limited by metaphysical elements like karma and souls that reduce empirical alignment.
  source: v7.1 data book, section 6 table (tables[4]) row 37 and section 7 scoring notes
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
  use_when: The person self-identifies as Jain.
  do_not_use_when: Ahimsa or vegetarianism alone is not JAIN.
  neighbors: []
review:
  data_quality_flags: []
  open_questions:
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Mark Owen Webb
  citation: Webb, Mark Owen. "Jain Philosophy." Internet Encyclopedia of Philosophy. https://iep.utm.edu/jain/.
  url: https://iep.utm.edu/jain/
  accessed: '2026-10-15'
  reliability_note: Peer-reviewed reference entry; undated page.
- id: S2
  type: tertiary
  kind: encyclopedia
  author: G. Ralph Strohl; Paul Dundas; Britannica Editors
  citation: Strohl, G. Ralph, Paul Dundas, and Britannica Editors. "Jainism." Encyclopaedia Britannica, updated 15 September 2026. https://www.britannica.com/topic/Jainism.
  url: https://www.britannica.com/topic/Jainism
  accessed: '2026-10-15'
  reliability_note: 'Signed article; first page read. AI Top Questions ignored. Byline lists Strohl and Dundas (checked in the Wayback copy, S6 audit fix). Bylines rotate between snapshots: the live page read 2026-10-15 showed Dundas and Britannica Editors; the Wayback copy lists Strohl and Dundas (P44(e): both recorded).'
---

# Jainism (JAIN)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

Jainism is an 'Indian religion teaching a path to spiritual purity and enlightenment through disciplined nonviolence' [S2]. It is 'frequently said to be atheistic. What is denied is a creator god above all' [S1].

## Core metaphysics

Eternal uncreated universe; gods within it subject to karma [S1].

## Position on the LIO axes

- A 3 (0.5, alt 4), C 3 (0.5, alt 4), E 4 (0.5).
- B, D UNKNOWN.

## Schools and variants

Shvetambara and Digambara [S2].

## Science

TODO

## Coding guidance

Self-identified Jains.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> JAIN (36/50) — Jainism. Jainism scores relatively high due to its rigorous ethical system and focus on non-violence, providing strong moral coherence, but limited by metaphysical elements like karma and souls that reduce empirical alignment.

## Open questions

- Adherents are TODO.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7 (score E on the world's order when the stub is filled).
- 2026-10-15 (systems batch S6): read the listed sources; quotations checked word for word against the fetched page text. Britannica Top Questions (AI-generated) not used. Axes under P44; PANDEI and PANEND under P45.
- 2026-10-15 (S6 audit fix): C_ledger cites P44(d). Britannica byline corrected.
- 2026-10-15 (S7 audit fix): byline note.
