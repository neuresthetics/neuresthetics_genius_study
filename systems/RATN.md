---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 8
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
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S1 audit (WEAKEN): D_authority 3 (0.5) → BELOW_THRESHOLD, alternative 3, under P44(b).'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S10 audit fix: A BELOW_THRESHOLD now quote-backed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'T2: B_cause UNKNOWN -> BELOW_THRESHOLD (alt 3), quote-backed; SEP Leibniz on Causation and Occasionalism added.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'T2 audit fix: B BELOW_THRESHOLD now based on Spinoza (4, SEP Spinoza added as S4) vs Leibniz (3); Malebranche background only; quote marks fixed.'
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
    how_known: 'Rationalists differ on God (P44(b)): ''Some include metaphysical claims, such as that God exists''; on innate knowledge, ''According to others, God provided us with it at creation. Still others say it is part of our nature through natural selection'' (S1 §1).'
    note: 'Evidence: S1 §1 (Intuition/Deduction and Innate Knowledge theses).'
  B_cause:
    value: BELOW_THRESHOLD
    how_known: 'Members differ on B. S1 warns that ''Descartes, Spinoza and Leibniz are mistakenly seen as applying a reason-centered epistemology to a common metaphysical agenda'' (§1). Spinoza gives 4: ''Nor does God perform miracles, since there are no, and cannot be, departures whatsoever from the necessary course of nature'' (S4, §2). Leibniz gives 3: he wants a world that ''unfolds'' naturally ''without the direct intervention of God'' and rejects occasionalism as ''a perpetual miracle'', yet allows events that ''surpass all the force of creatures'', such as the Creation and the Incarnation (S2, §3). Background only: Malebranche''s occasionalism, ''there is only one true cause because there is only one true God'' (S3).'
    note: P44(b). Spinoza 4 vs Leibniz 3. Alternative 3.
    cites: &id001
    - source: S1
      locator: §1
    - source: S4
      locator: §2
    - source: S2
      locator: §3
    alternatives:
    - value: 3
      note: Named alternative (Leibniz).
      cites: *id001
  C_ledger:
    value: UNKNOWN
    how_known: Not addressed in S1.
  D_authority:
    value: BELOW_THRESHOLD
    how_known: 'P44(b): the theses are relative to subject area, and SEP does not discuss revelation, so members differ; the sources read do not mention revelation.'
    note: 'Alternative: 3 (observation and reason over revelation in the covered areas). Changed from 3 (0.5) after the S1 audit.'
    alternatives:
    - value: 3
      note: Coder's first reading in batch S1.
      cites:
      - source: S1
        locator: §1
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
- id: S2
  type: tertiary
  kind: encyclopedia
  author: Bobro, Marc, and Tobias Flattery
  year: 2026
  citation: Bobro, Marc, and Tobias Flattery. "Leibniz on Causation." Stanford Encyclopedia of Philosophy. https://plato.stanford.edu/entries/leibniz-causation/
  url: https://plato.stanford.edu/entries/leibniz-causation/
  accessed: '2026-10-15'
  reliability_note: Signed SEP entry (substantive revision 2026-09-30); §3 on occasionalism and miracles read.
- id: S3
  type: tertiary
  kind: encyclopedia
  author: Lee, Sukjae
  year: 2019
  citation: Lee, Sukjae. "Occasionalism." Stanford Encyclopedia of Philosophy. https://plato.stanford.edu/entries/occasionalism/
  url: https://plato.stanford.edu/entries/occasionalism/
  accessed: '2026-10-15'
  reliability_note: Signed SEP entry; introduction and Leibniz comparison read. Malebranche is not named a rationalist in S1; used only as the contrasting case.
- id: S4
  type: tertiary
  kind: encyclopedia
  author: Nadler, Steven
  year: 2023
  citation: Nadler, Steven. "Baruch Spinoza." Stanford Encyclopedia of Philosophy. https://plato.stanford.edu/entries/spinoza/
  url: https://plato.stanford.edu/entries/spinoza/
  accessed: '2026-10-15'
  reliability_note: Signed SEP entry (2023 revision); §2 (Ethics) read.
---

# Rationalism (RATN)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1). The v7.1 scores and note are unchanged.

## Summary

Rationalism holds, by the Intuition/Deduction Thesis, that some propositions in a subject area are knowable by intuition alone or by deduction from intuited ones [S1, §1]. Some rationalists include 'metaphysical claims, such as that God exists'; some hold innate knowledge that, 'According to others, God provided us with it at creation' [S1, §1]. SEP names Descartes, Spinoza and Leibniz as the Continental Rationalists [S1].

## Core metaphysics

Varies: the named rationalists differ on God [S1].

## Position on the LIO axes

- D BELOW_THRESHOLD (alt 3): reason independent of experience, but members differ [S1, §1].
- A BELOW_THRESHOLD: God often known a priori; locus varies.
- B BELOW_THRESHOLD (alt 3): Spinoza (no miracles, 4) vs Leibniz (3); Malebranche background [S1, S4, S2, S3].
- C, E UNKNOWN.

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
- 2026-10-15 (S1 audit fixes, run 1: 5 HOLD, 2 WEAKEN): D_authority to BELOW_THRESHOLD (alt 3) under P44(b).
- 2026-10-15 (S10 audit fix): A BELOW_THRESHOLD now quote-backed.
- 2026-10-15 (targeted A/B pass, batch T2): searched topic-specific sources (SEP entries on causation, occasionalism, Abhidharma) for a statement fixing the missing axis; quotations checked word for word against fetched page text. RATN: B fixed as BELOW_THRESHOLD from S1, SEP "Leibniz on Causation" and SEP "Occasionalism".
- 2026-10-15 (T2 audit fixes, /workspace/genius_study_audit/gs_dc95c1a_T2/run1/): RATN B rebased on Spinoza vs Leibniz; SEP "Baruch Spinoza" (Nadler) added, quote checked word for word.
