---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 3
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
    summary: 'Draft (systems batch S1): filled from the movement''s own site (the-brights.net home and Vision pages; primary for self-definition). No encyclopedia entry found. Founders and dates TODO. v7.1 scores and note unchanged. Not reviewed.'
identity:
  id: BRGHTS
  v7_1_number: 3
  v7_1_label: Brights (The Brights Movement)
  display_label: Brights (The Brights Movement)
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: ethical or civic movement
    certainty: 0.7
    cites:
    - source: S2
      locator: Vision
    how_known: The site describes a civic constituency of people with naturalistic worldviews; coder's classification, 0.7.
  family:
    value: Naturalism (civic)
    certainty: 1.0
    cites:
    - source: S1
      locator: home
    how_known: '''All of us have a naturalistic worldview, free of supernatural or mystical elements.'''
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
    value: 'Naturalistic: a bright is ''a person whose worldview is naturalistic (no supernatural and mystical elements)''.'
    stance: no God
    certainty: 1.0
    cites:
    - source: S1
      locator: home
    how_known: The movement's own definition.
  deity_personal:
    value: TODO
    stance: TODO
  intervention:
    value: 'None: worldviews ''free of the supernatural deities, forces, and entities''.'
    stance: none
    certainty: 1.0
    cites:
    - source: S2
      locator: Vision
    how_known: Own site.
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
    value: 4
    rationale: No supernatural deities; naturalistic worldview.
    certainty: 0.7
    cites:
    - source: S1
      locator: home
    - source: S2
      locator: Vision
    how_known: 0–4 scale (P1). Own definition; A for a system with no God-term follows ATHE (ruling question), so 0.7.
  B_cause:
    value: 4
    rationale: No supernatural forces or entities, so no miracle or exception.
    certainty: 0.7
    cites:
    - source: S2
      locator: Vision
    how_known: '0–4 scale (P1). 0.7: the site states the worldview, not a doctrine of law.'
  C_ledger:
    value: 4
    rationale: No supernatural agent to keep a moral ledger.
    certainty: 0.5
    cites:
    - source: S2
      locator: Vision
    how_known: Inferred, 0.5.
  D_authority:
    value: 4
    rationale: Naturalistic explanations; principles held 'as values, not dogma'.
    certainty: 0.5
    cites:
    - source: S1
      locator: home
    - source: S2
      locator: Vision
    how_known: Inferred from the self-definition; revelation not mentioned. 0.5.
  E_scope:
    value: 4
    rationale: 'On the world''s order (P7): no supernatural forces to favour a group.'
    certainty: 0.5
    cites:
    - source: S2
      locator: Vision
    how_known: Inferred, 0.5.
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
  scoring_note: The Brights Movement scores highly for its evidence-based naturalism and civic focus, serving as a practical extension of atheism with strong coherence.
  source: v7.1 data book, section 6 table (tables[4]) row 3 and section 7 scoring notes
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
  use_when: The person publicly identifies as a Bright (the self-applied label); otherwise use ATHE or SECHUM on their stated views.
  do_not_use_when: 'Do not infer BRGHTS from naturalism alone: it is a self-chosen civic label (S1).'
  neighbors: []
review:
  data_quality_flags:
  - Only the movement's own pages were read; no independent encyclopedia entry was found. Founders, founding date and membership are TODO.
  open_questions:
  - Founding (an independent source is needed).
  - Adherents are TODO.
sources:
- id: S1
  type: primary
  kind: institutional page
  author: The Brights' Net
  citation: The Brights' Net. "Who are The Brights?" https://www.the-brights.net/.
  url: https://www.the-brights.net/
  accessed: '2026-10-15'
  reliability_note: The movement's own site (primary for its self-definition); no date on the page.
- id: S2
  type: primary
  kind: institutional page
  author: The Brights' Net
  citation: The Brights' Net. "The Vision." https://www.the-brights.net/vision/.
  url: https://www.the-brights.net/vision/
  accessed: '2026-10-15'
  reliability_note: The movement's own site; no date on the page.
---

# Brights (The Brights Movement) (BRGHTS)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1). The v7.1 scores and note are unchanged.

## Summary

The Brights describe themselves as people who 'have a naturalistic worldview, free of supernatural or mystical elements' [S1, home]. A 'bright' (n.) is 'a person whose worldview is naturalistic (no supernatural and mystical elements)' [S1]. Founders and date are TODO (no independent source read).

## Core metaphysics

Worldviews 'free of the supernatural deities, forces, and entities' [S2, Vision].

## Position on the LIO axes

- A 4 (0.7), B 4 (0.7): no supernatural entities or forces [S1; S2].
- C, D, E 4 (0.5): inferred from the self-definition [S2].

## Schools and variants

TODO

## Science

TODO

## Coding guidance

Use only for a self-described Bright; otherwise ATHE or SECHUM.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> BRGHTS (49/50) — Brights (The Brights Movement). The Brights Movement scores highly for its evidence-based naturalism and civic focus, serving as a practical extension of atheism with strong coherence.

## Open questions

- Founders, date and an independent source.
- Adherents are TODO.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7 (score E on the world's order when the stub is filled).
- 2026-10-15 (systems batch S1): read the listed sources; quotations checked word for word against the fetched page text with a script. Britannica Top Questions boxes (AI-generated) not used.
