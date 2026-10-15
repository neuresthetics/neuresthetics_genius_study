---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 3
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S2 for Jason)
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
    summary: 'Draft (systems batch S2): filled from the Council for Secular Humanism page (primary self-definition). A, B, C, D 4; E 4 at 0.5. v7.1 scores and note unchanged. Not reviewed.'
identity:
  id: SECHUM
  v7_1_number: 8
  v7_1_label: Secular Humanism
  display_label: Secular Humanism
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: ethical or civic movement
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: '''a comprehensive, non-religious lifestance''. Coder''s classification, 0.7.'
  family:
    value: Naturalism; humanism
    certainty: 1.0
    cites:
    - source: S1
      locator: A naturalistic philosophy
    how_known: Own definition.
  parent_traditions:
    value: TODO
  related_codes:
  - code: ATHE
    relation: neighbor (easily confused)
  - code: AGNOS
    relation: neighbor (easily confused)
origins:
  founding_era:
    value: TODO
  founding_region:
    value: TODO
  founders_or_key_figures:
    value:
    - Paul Kurtz
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Named as founder of the Council for Secular Humanism and Free Inquiry.
  key_texts:
  - value: Humanist Manifesto II
    year: 1973
    certainty: 1.0
    cites:
    - source: S1
      locator: A consequentialist ethical system
    how_known: Quoted on the page.
  - value: A Secular Humanist Declaration
    certainty: 0.7
    cites:
    - source: S1
      locator: Explanations
    how_known: Listed as an explanation on the page; date not given.
metaphysics:
  god_nature_relation:
    value: '''nature (the world of everyday physical experience) is all there is''; ''Naturalism asserts that supernatural entities like God do not exist''.'
    stance: no God
    certainty: 1.0
    cites:
    - source: S1
      locator: A naturalistic philosophy
    how_known: Own definition.
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
    value: Ethics 'is consequential, to be judged by results', against command ethics 'attributed to divine authority'; 'No god will save us … we must save ourselves' (Humanist Manifesto II).
    stance: none
    certainty: 1.0
    cites:
    - source: S1
      locator: A consequentialist ethical system
    how_known: Own definition.
  authority:
    value: '''reliable knowledge is best obtained when we query nature using the scientific method''.'
    stance: observation and reason
    certainty: 1.0
    cites:
    - source: S1
      locator: A naturalistic philosophy
    how_known: Own definition.
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
    rationale: Supernatural entities like God do not exist; nature is all there is. A 4 for a no-God system (P44a).
    certainty: 1.0
    cites:
    - source: S1
      locator: A naturalistic philosophy
    how_known: Own explicit definition.
  B_cause:
    value: 4
    rationale: Nature is all there is, so nothing outside it to make exceptions.
    certainty: 0.7
    cites:
    - source: S1
      locator: A naturalistic philosophy
    how_known: The page states naturalism, not a doctrine of exceptionless law; 0.7.
  C_ledger:
    value: 4
    rationale: 'No divine ledger: ethics judged by results; ''No god will save us''.'
    certainty: 0.7
    cites:
    - source: S1
      locator: A consequentialist ethical system
    how_known: Own statement; ledger language is the coder's, 0.7.
  D_authority:
    value: 4
    rationale: The scientific method; knowledge gained without appeal to the natural world is unreliable.
    certainty: 1.0
    cites:
    - source: S1
      locator: A naturalistic philosophy
    how_known: Own explicit statement.
  E_scope:
    value: 4
    rationale: 'On the world''s order (P7): nature is all there is, so no agent to exempt a group.'
    certainty: 0.5
    cites:
    - source: S1
      locator: A naturalistic philosophy
    how_known: Fixed by the naturalist stance but not stated; 0.5.
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
  scoring_note: Secular Humanism scores near-perfect by integrating rational ethics with empirical science, promoting human flourishing without dogma, though its focus on welfare adds a minor subjective layer.
  source: v7.1 data book, section 6 table (tables[4]) row 8 and section 7 scoring notes
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
  use_when: 'v7.1 coding rule (Atheism vs Agnosticism): ATHE = positive naturalism. AGNOS = explicit suspension. SECHUM if the public identity is humanist movement rather than metaphysics.'
  do_not_use_when: Do not use for a person whose only stated view is disbelief in God (ATHE) or suspension (AGNOS); SECHUM needs a humanist public identity or the lifestance (S1).
  neighbors:
  - code: ATHE
    relation: neighbor (easily confused)
  - code: AGNOS
    relation: neighbor (easily confused)
review:
  data_quality_flags:
  - Only the movement's own page read; Britannica has no secular-humanism article.
  open_questions:
  - An independent encyclopedia source.
  - Adherents are TODO.
sources:
- id: S1
  type: primary
  kind: institutional page
  author: Council for Secular Humanism (Free Inquiry)
  citation: Council for Secular Humanism. "What is Secular Humanism?" Free Inquiry. https://secularhumanism.org/what-is-secular-humanism/.
  url: https://secularhumanism.org/what-is-secular-humanism/
  accessed: '2026-10-15'
  reliability_note: The movement's own page (primary for self-definition); undated. Britannica has no 'secular humanism' article (404).
---

# Secular Humanism (SECHUM)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1). The v7.1 scores and note are unchanged.

## Summary

Secular humanism is 'a comprehensive, non-religious lifestance incorporating: A naturalistic philosophy; A cosmic outlook rooted in science; A consequentialist ethical system' [S1]. It is 'broader than atheism' [S1]. Founder of the Council for Secular Humanism: Paul Kurtz (1925–2012) [S1].

## Core metaphysics

Nature is all there is; God does not exist [S1].

## Position on the LIO axes

- A 4 (1.0), D 4 (1.0) [S1].
- B 4 (0.7), C 4 (0.7) [S1].
- E 4 (0.5): fixed by naturalism, not stated.

## Schools and variants

TODO

## Science

'A cosmic outlook rooted in science'; humans as 'undesigned, unintended beings who arose through evolution' [S1].

## Coding guidance

SECHUM if the public identity is the humanist movement rather than metaphysics (v7.1 rule).

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> SECHUM (49/50) — Secular Humanism. Secular Humanism scores near-perfect by integrating rational ethics with empirical science, promoting human flourishing without dogma, though its focus on welfare adds a minor subjective layer.

## Open questions

- Independent source.
- Adherents are TODO.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7 (score E on the world's order when the stub is filled).
- 2026-10-15 (systems batch S2): read the listed sources; quotations checked against the fetched page text. Axes follow P44(b): a value only where the stance itself fixes it; UNKNOWN where the source is silent; BELOW_THRESHOLD where members differ.
