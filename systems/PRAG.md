---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 4
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
    summary: 'Draft (systems batch S2): filled from SEP "Pragmatism" (Legg and Hookway). A and D BELOW_THRESHOLD (pragmatists differ); B, C, E UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'T2: B_cause searched, unchanged; search logged.'
identity:
  id: PRAG
  v7_1_number: 10
  v7_1_label: Pragmatism
  display_label: Pragmatism
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: philosophical school or method
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: '''a philosophical tradition that – very broadly – understands knowing the world as inseparable from agency within it''.'
  family:
    value: TODO
  parent_traditions:
    value: TODO
  related_codes: []
origins:
  founding_era:
    value: Late nineteenth century (classical pragmatists)
    certainty: 0.7
    cites:
    - source: S1
      locator: §1
    how_known: Peirce (1839–1914) first defined it; exact date not quoted. 0.7.
  founding_region:
    value: TODO
  founders_or_key_figures:
    value:
    - Charles Sanders Peirce
    - William James
    - John Dewey
    - Jane Addams
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: SEP.
  key_texts: []
metaphysics:
  god_nature_relation:
    value: 'Varies: James ''put these themes to work exploring truth in religion''.'
    stance: varies by school
    certainty: 0.7
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
    how_known: 'Pragmatists differ (P44b): James explored truth in religion; SEP gives no shared God-view.'
    note: 'Evidence: S1 §1–2.'
  B_cause:
    value: UNKNOWN
    how_known: Not addressed in S1.
  C_ledger:
    value: UNKNOWN
    how_known: Not addressed in S1.
  D_authority:
    value: BELOW_THRESHOLD
    how_known: 'Inquiry tested against experience is the shared method (S1), but James allows that a theological proposition can be made true by ''a value for concrete life'' (1907: 40), so members differ (P44b).'
    note: 'Alternative: 3 (fallibilist inquiry, Peirce).'
    alternatives:
    - value: 3
      note: Peirce and Dewey line.
      cites:
      - source: S1
        locator: §2
  E_scope:
    value: UNKNOWN
    how_known: Not addressed in S1.
epistemology:
  value: 'The Pragmatic Maxim: ''a rule for clarifying the meaning of hypotheses by tracing their implications for experience in specific situations''; ''a fallibilist, anti-Cartesian explication of the norms that govern inquiry''.'
  certainty: 1.0
  cites:
  - source: S1
    locator: opening; §2
  how_known: SEP.
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
  P: 9
  E: 10
  V: 10
  X: 9
  total: 48
  scoring_note: Pragmatism excels in practical, evidence-based problem-solving, with a high score reflecting its adaptability and real-world focus.
  source: v7.1 data book, section 6 table (tables[4]) row 10 and section 7 scoring notes
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
  use_when: The person's own writing adopts the Pragmatic Maxim or the classical pragmatists' theory of truth as their main worldview.
  do_not_use_when: Practical or applied habits of mind are not PRAG; nor is a scientist's fallibilism alone.
  neighbors: []
review:
  data_quality_flags: []
  open_questions:
  - Adherents are TODO.
  - 'T2 (2026-10-15): B_cause searched in topic sources; unchanged. See research log.'
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Catherine Legg; Christopher Hookway
  year: 2024
  citation: Legg, Catherine, and Christopher Hookway. "Pragmatism." Stanford Encyclopedia of Philosophy. First published August 16, 2008; substantive revision September 30, 2024. https://plato.stanford.edu/entries/pragmatism/.
  url: https://plato.stanford.edu/entries/pragmatism/
  accessed: '2026-10-15'
  reliability_note: Peer-reviewed reference entry.
---

# Pragmatism (PRAG)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1). The v7.1 scores and note are unchanged.

## Summary

Pragmatism 'understands knowing the world as inseparable from agency within it' [S1]. Peirce 'first defined and defended the view'; James 'further developed and ably popularized it'; Dewey and Addams turned it toward social improvement [S1, §1].

## Core metaphysics

Varies [S1].

## Position on the LIO axes

- A BELOW_THRESHOLD, D BELOW_THRESHOLD (alt 3): pragmatists differ.
- B, C, E UNKNOWN.

## Schools and variants

Classical (Peirce, James), second classical generation (Dewey, Addams), neopragmatism (Rorty) [S1].

## Science

TODO

## Coding guidance

Use only for a stated pragmatist worldview.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> PRAG (48/50) — Pragmatism. Pragmatism excels in practical, evidence-based problem-solving, with a high score reflecting its adaptability and real-world focus.

## Open questions

- Adherents are TODO.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7 (score E on the world's order when the stub is filled).
- 2026-10-15 (systems batch S2): read the listed sources; quotations checked against the fetched page text. Axes follow P44(b): a value only where the stance itself fixes it; UNKNOWN where the source is silent; BELOW_THRESHOLD where members differ.
- 2026-10-15 (targeted A/B pass, batch T2): searched topic-specific sources (SEP entries on causation, occasionalism, Abhidharma) for a statement fixing the missing axis; quotations checked word for word against fetched page text. PRAG: SEP 'Pragmatism' (Legg and Hookway, 2024) searched for naturalism, supernatural, miracle: Dewey's 'naturalism' and his view that 'removing faith in supernatural entities will not destroy religion', vs James's 'Will to Believe' faith. Neither is a statement on exceptions in nature, so not used for BELOW_THRESHOLD. Lead: SEP 'William James' on piecemeal supernaturalism (Varieties). B stays UNKNOWN.
