---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 5
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S7 for Jason)
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
    summary: 'Draft (systems batch S7): filled from Britannica "Cao Dai" (editors). A 1 (0.5, alt 0); B 1 (0.5); C 3 (0.5, alt 4); D 1 (0.5); E UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S6 audit fix: C cites P44(d).'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S7 audit fix: Wayback snapshot URL and timestamp cited under P44(e); B ceiling note.'
identity:
  id: CAODAI
  v7_1_number: 41
  v7_1_label: Caodaism
  display_label: Caodaism
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: religion
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: '''syncretist modern Vietnamese religious movement''.'
  family:
    value: TODO
  parent_traditions:
    value: TODO
  related_codes: []
origins:
  founding_era:
    value: 1919 séance; formally established 1926
    certainty: 1.0
    cites:
    - source: S1
      locator: history
    how_known: Britannica.
  founding_region:
    value: Vietnam (Tay Ninh)
    certainty: 1.0
    cites:
    - source: S1
      locator: history
    how_known: Britannica.
  founders_or_key_figures:
    value:
    - Ngo Van Chieu
    certainty: 1.0
    cites:
    - source: S1
      locator: history
    how_known: Britannica.
  key_texts: []
metaphysics:
  god_nature_relation:
    value: Cao Dai is 'a Taoist epithet for the supreme god'; 'God is represented as an eye in a triangle'.
    stance: creator distinct from creation
    certainty: 0.7
    cites:
    - source: S1
      locator: introduction
    how_known: Britannica.
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
    value: '''theories of karma and rebirth from Buddhism''.'
    stance: karma-type law
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: Britannica.
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
    value: 1
    rationale: A supreme god who communicates with humans.
    certainty: 0.5
    cites: &id001
    - source: S1
      locator: introduction; history
    how_known: '0.5: the article does not describe the god’s nature further. Alternative 0.'
    alternatives:
    - value: 0
      note: Named alternative.
      cites: *id001
  B_cause:
    value: 1
    rationale: Chieu 'received a communication from the supreme deity during a table-moving séance'.
    certainty: 0.5
    cites:
    - source: S1
      locator: history
    how_known: '0.5: one founding event; no general doctrine of intervention stated. 0.5 is the ceiling: the séance is a communication, not a physical intervention (S7 audit).'
  C_ledger:
    value: 3
    rationale: Karma and rebirth taken from Buddhism.
    certainty: 0.5
    cites: &id002
    - source: S1
      locator: introduction
    how_known: 'Karma rule (P44(d)): an impersonal moral ledger is C 3 @0.5, alternative 4. Karma and rebirth from Buddhism.'
    alternatives:
    - value: 4
      note: Named alternative.
      cites: *id002
  D_authority:
    value: 1
    rationale: Founded on séance revelation; a Catholic-style hierarchy with a pope.
    certainty: 0.5
    cites:
    - source: S1
      locator: introduction; history
    how_known: 0.5.
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
  E: 6
  V: 6
  X: 4
  total: 32
  scoring_note: Caodaism scores moderately due to its innovative syncretism promoting religious unity, offering ethical and spiritual coherence but limited by revelatory elements and modest empirical alignment.
  source: v7.1 data book, section 6 table (tables[4]) row 41 and section 7 scoring notes
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
  use_when: The person self-identifies as Caodaist.
  do_not_use_when: Vietnamese nationality alone is not CAODAI.
  neighbors: []
review:
  data_quality_flags: []
  open_questions:
  - A fuller source on Cao Dai doctrine.
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Britannica Editors
  citation: 'The Editors of Encyclopaedia Britannica. "Cao Dai." Encyclopaedia Britannica. https://www.britannica.com/topic/Cao-Dai. Wayback Machine snapshot 2026-05-04 19:37:58 UTC: https://web.archive.org/web/20260504193758/https://www.britannica.com/topic/Cao-Dai.'
  url: https://www.britannica.com/topic/Cao-Dai
  accessed: '2026-10-15'
  reliability_note: 'Short unsigned editors’ article. P44(e): read in the Wayback copy (https://web.archive.org/web/20260504193758/https://www.britannica.com/topic/Cao-Dai), counted as the full article, no P45 cap. Live page timed out on 2026-10-15, so no live comparison; byline in the copy: Britannica Editors.'
---

# Caodaism (CAODAI)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

Cao Dai is a 'syncretist modern Vietnamese religious movement with a strongly nationalist political character' [S1].

## Core metaphysics

Supreme god; karma and rebirth [S1].

## Position on the LIO axes

- A 1, B 1, D 1 (0.5); C 3 (0.5, alt 4).
- E UNKNOWN.

## Schools and variants

TODO

## Science

TODO

## Coding guidance

Self-identified Caodaists.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> CAODAI (32/50) — Caodaism. Caodaism scores moderately due to its innovative syncretism promoting religious unity, offering ethical and spiritual coherence but limited by revelatory elements and modest empirical alignment.

## Open questions

- Fuller source.
- Adherents are TODO.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7 (score E on the world's order when the stub is filled).
- 2026-10-15 (systems batch S7): read the listed sources; quotations checked word for word against the fetched page text. Britannica pages read in their full Wayback Machine copies (curl and WebFetch time out on the live site); Britannica AI Top Questions not used.
- 2026-10-15 (S6 audit fix): C_ledger cites P44(d).
- 2026-10-15 (S7 audit fix): P44(e) Wayback citation.
