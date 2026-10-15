---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 4
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
  - date: 2026-10-02
    by: scripts/make_system_stubs.py
    summary: 'Decision P22 (stage 3 lens audit): one-line use_when against CLASS_THEISM, marked as v8''s pick.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'Draft (systems batch S1): filled from SEP "Rationalism vs. Empiricism". D 3 at 0.5; A BELOW_THRESHOLD; B, C and E UNKNOWN. The P22 use_when line is kept. v7.1 scores and note unchanged. Not reviewed.'
identity:
  id: RATN
  v7_1_number: 7
  v7_1_label: Rationalism
  display_label: Rationalism
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: epistemic stance
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: 'SEP: theses about sources of knowledge.'
  family:
    value: Epistemology (rationalism versus empiricism)
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: SEP.
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
    - René Descartes
    - Baruch Spinoza
    - Gottfried Wilhelm Leibniz
    certainty: 0.7
    cites:
    - source: S1
      locator: §1
    how_known: 'SEP: ''the Continental Rationalists'', with its caution on the classification. 0.7.'
  key_texts: []
metaphysics:
  god_nature_relation:
    value: 'Varies by school: Descartes, Spinoza and Leibniz differ.'
    stance: varies by school
    certainty: 0.7
    cites:
    - source: S1
      locator: §1
    how_known: SEP names them as rationalists; their God-views are not given there.
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
    value: 'Reason: by the Intuition/Deduction Thesis some propositions are knowable by intuition alone or deduced from them; some rationalists include ''metaphysical claims, such as that God exists''.'
    stance: observation and reason
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: SEP.
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
    how_known: God is a typical object of a priori knowledge for rationalists (S1 §1), and some held innate knowledge was given by God at creation, but the named rationalists differ on God (Descartes, Spinoza, Leibniz).
    note: 'Evidence: S1 §1 (Intuition/Deduction and Innate Knowledge theses).'
  B_cause:
    value: UNKNOWN
    how_known: Not addressed in S1.
  C_ledger:
    value: UNKNOWN
    how_known: Not addressed in S1.
  D_authority:
    value: 3
    rationale: 'Intuition and deduction yield knowledge independently of experience, including of God; revelation is given no role. 3 not 4: the theses are relative to a subject area.'
    certainty: 0.5
    cites:
    - source: S1
      locator: §1
    how_known: 0–4 scale (P1). SEP does not discuss revelation; inferred, 0.5.
  E_scope:
    value: UNKNOWN
    how_known: Not addressed in S1.
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
  scoring_note: Rationalism excels in logical rigor and evidence prioritization, scoring high overall but docked slightly for occasional over-reliance on deduction in non-empirical contexts.
  source: v7.1 data book, section 6 table (tables[4]) row 7 and section 7 scoring notes
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
  use_when: 'v8''s pick (decision P22, 2026-10-02; one-line clarification against CLASS_THEISM, the rest of the stub is not yet sourced): use RATN when the person''s own writing makes reason working from innate ideas or first principles the main route to God and the world, and argues to God from the idea of God or from reason alone (ontological or idea-based arguments); a person whose main argument for God runs from the world, a posteriori (first cause, contingency, design), to the simple, immutable God of the Aristotelian-Thomistic-Falsafa line is CLASS_THEISM.'
  do_not_use_when: 'A posteriori arguments to the simple, immutable God (first cause, contingency, design): CLASS_THEISM (P22). God identified with Nature (Spinoza): check PANT.'
  neighbors: []
review:
  data_quality_flags: []
  open_questions:
  - How to score A and B for an epistemology (ruling question).
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Peter Markie; M. Folescu
  year: 2021
  citation: Markie, Peter, and M. Folescu. "Rationalism vs. Empiricism." Stanford Encyclopedia of Philosophy. First published August 19, 2004; substantive revision September 2, 2021. https://plato.stanford.edu/entries/rationalism-empiricism/.
  url: https://plato.stanford.edu/entries/rationalism-empiricism/
  accessed: '2026-10-15'
  reliability_note: Peer-reviewed reference entry.
---

# Rationalism (RATN)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1). The v7.1 scores and note are unchanged.

## Summary

Rationalism holds, by the Intuition/Deduction Thesis, that some propositions in a subject area are knowable by intuition alone or by deduction from intuited ones [S1, §1]. Some rationalists include 'metaphysical claims, such as that God exists'; some hold innate knowledge that, 'According to others, God provided us with it at creation' [S1, §1]. SEP names Descartes, Spinoza and Leibniz as the Continental Rationalists [S1].

## Core metaphysics

Varies: the named rationalists differ on God [S1].

## Position on the LIO axes

- D 3 (0.5): reason independent of experience [S1, §1].
- A BELOW_THRESHOLD: God often known a priori; locus varies.
- B, C, E UNKNOWN.

## Schools and variants

Subject-relative forms; the Innate Knowledge and Innate Concept theses [S1, §1].

## Science

TODO

## Coding guidance

P22 rule kept: RATN for reason-first, idea-based routes to God; a posteriori arguments go to CLASS_THEISM.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> RATN (49/50) — Rationalism. Rationalism excels in logical rigor and evidence prioritization, scoring high overall but docked slightly for occasional over-reliance on deduction in non-empirical contexts.

## Open questions

- A and B for a pure epistemology (ruling question).
- Adherents are TODO.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7 (score E on the world's order when the stub is filled).
- 2026-10-15 (systems batch S1): read the listed sources; quotations checked word for word against the fetched page text with a script. Britannica Top Questions boxes (AI-generated) not used.
