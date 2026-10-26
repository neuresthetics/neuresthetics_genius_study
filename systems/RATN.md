---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 9
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S1 for Jason)
  model_used: Grok Bot executor agent; direct reads of the cited pages
  collected_on: '2026-10-01'
  last_updated: '2026-10-25'
  change_log:
  - date: '2026-10-01'
    by: scripts/make_system_stubs.py
    summary: Stub created from v7.1 data book table 4 and section 7.
  - date: '2026-10-02'
    by: scripts/make_system_stubs.py
    summary: "Decision P7: E_scope note added. E is not scored in a stub; when it is, score it on the\
      \ world's order (same rules for every kind of being and event, no in-group exceptions in this-world\
      \ events). Salvation and moral community go on C_ledger."
  - date: '2026-10-02'
    by: scripts/make_system_stubs.py
    summary: "Decision P22 (stage 3 lens audit): one-line use_when against CLASS_THEISM, marked as v8's\
      \ pick."
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'Draft (systems batch S1): filled from SEP "Rationalism vs. Empiricism". D 3 at 0.5; A BELOW_THRESHOLD;
      B, C and E UNKNOWN. The P22 use_when line is kept. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S1 audit (WEAKEN): D_authority 3 (0.5) → BELOW_THRESHOLD, alternative 3, under P44(b).'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S10 audit fix: A BELOW_THRESHOLD now quote-backed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'T2: B_cause UNKNOWN -> BELOW_THRESHOLD (alt 3), quote-backed; SEP Leibniz on Causation and
      Occasionalism added.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'T2 audit fix: B BELOW_THRESHOLD now based on Spinoza (4, SEP Spinoza added as S4) vs Leibniz
      (3); Malebranche background only; quote marks fixed.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from SEP Rationalism vs Empiricism (Markie/Folescu): family/parents, metaphysics
      TODOs, ethics/practice/science/schools. Axes unchanged.'
identity:
  id: RATN
  v7_1_number: 7
  v7_1_label: Rationalism
  display_label: Rationalism
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: philosophical school or method
    certainty: 1.0
    cites:
    - source: S1
      locator: §1.1
    how_known: SEP.
  family:
    value: Significant concepts/knowledge gained independently of sense experience (innate knowledge and/or
      innate concepts; intuition/deduction for external-world claims)
    certainty: 1.0
    cites:
    - source: S1
      locator: §1.1
    how_known: SEP.
  parent_traditions:
    value:
    - 'Continental rationalism textbook cluster (Descartes, Spinoza, Leibniz — labels cautioned)'
    - Platonic recollection antecedents
    - Early modern epistemology
    certainty: 0.7
    cites:
    - source: S1
      locator: §1; §3
    how_known: SEP. 0.7.
  related_codes:
  - code: EMPIR
    relation: contrast case
    note: Paired dispute
  - code: IDEAL
    relation: overlaps
    note: Some rationalists develop idealist metaphysics
  - code: DETERM
    relation: neighbor (easily confused)
    note: Spinoza etc.; not identical to RATN
  - code: SCEPT
    relation: contrast case
    note: Rationalism often denies skepticism for some domain
origins:
  founding_era:
    value: Early modern (17th–18th c.) as named dispute; Platonic antecedents
    certainty: 1.0
    cites:
    - source: S1
      locator: §1; §3
    how_known: SEP.
  founding_region:
    value: Western Europe (textbook “Continental” casting); not a single founding city
    certainty: 0.7
    cites:
    - source: S1
      locator: §1
    how_known: '0.7.'
  founders_or_key_figures:
    value:
    - René Descartes
    - Baruch Spinoza
    - G. W. Leibniz
    - Plato (recollection antecedent)
    certainty: 1.0
    cites:
    - source: S1
      locator: §1; §3
    how_known: SEP.
  key_texts:
  - value: 'Descartes, Meditations / Rules; Leibniz, New Essays; Plato, Meno (recollection)'
    certainty: 1.0
    cites:
    - source: S1
      locator: §2–3
    how_known: SEP.
metaphysics:
  god_nature_relation:
    value: Often central in classical rationalist metaphysics (Descartes God; Spinoza substance); not
      required of every rationalist epistemology
    stance: varies by school
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: SEP.
  deity_personal:
    value: Varies (Descartes personal God; Spinoza non-personal substance)
    stance: varies by school
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: SEP.
  intervention:
    value: Varies by school; not the defining RATN thesis
    stance: varies by school
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP.
  miracles:
    value: Not the defining thesis
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP.
  petition_and_prayer:
    value: Not a practice system
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP.
  afterlife:
    value: Varies (substance dualism etc.); not required for RATN label
    stance: varies by school
    certainty: 0.7
    cites:
    - source: S1
      locator: §1
    how_known: '0.7.'
  moral_ledger:
    value: Some place ethical truths under intuition/deduction; not a shared divine ledger
    stance: varies by school
    certainty: 0.7
    cites:
    - source: S1
      locator: §1
    how_known: '0.7.'
  authority:
    value: Reason / intuition and deduction; often superiority or indispensability of reason theses
    stance: observation and reason
    certainty: 1.0
    cites:
    - source: S1
      locator: §1.1
    how_known: SEP.
  reserved_exemptions:
    value: No religious census exemption as shared creed
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: introduction
    how_known: '0.7.'
  teleology_in_nature:
    value: Varies (Leibniz etc.); not definitional of RATN
    stance: varies by school
    certainty: 0.7
    cites:
    - source: S1
      locator: §1
    how_known: '0.7.'
  necessity_and_freedom:
    value: 'Often claims necessary truths known a priori (math, some metaphysics); free will varies by
      figure'
    certainty: 0.7
    cites:
    - source: S1
      locator: §2
    how_known: '0.7.'
lio_axes:
  A_locus:
    value: 'BELOW_THRESHOLD'
    how_known: "Rationalists differ on God (P44(b)): 'Some include metaphysical claims, such as that God\
      \ exists'; on innate knowledge, 'According to others, God provided us with it at creation. Still\
      \ others say it is part of our nature through natural selection' (S1 §1)."
    note: 'Evidence: S1 §1 (Intuition/Deduction and Innate Knowledge theses).'
  B_cause:
    value: 'BELOW_THRESHOLD'
    how_known: "Members differ on B. S1 warns that 'Descartes, Spinoza and Leibniz are mistakenly seen\
      \ as applying a reason-centered epistemology to a common metaphysical agenda' (§1). Spinoza gives\
      \ 4: 'Nor does God perform miracles, since there are no, and cannot be, departures whatsoever from\
      \ the necessary course of nature' (S4, §2). Leibniz gives 3: he wants a world that 'unfolds' naturally\
      \ 'without the direct intervention of God' and rejects occasionalism as 'a perpetual miracle', yet\
      \ allows events that 'surpass all the force of creatures', such as the Creation and the Incarnation\
      \ (S2, §3). Background only: Malebranche's occasionalism, 'there is only one true cause because\
      \ there is only one true God' (S3)."
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
    value: 'UNKNOWN'
    how_known: Not addressed in S1.
  D_authority:
    value: 'BELOW_THRESHOLD'
    how_known: 'P44(b): the theses are relative to subject area, and SEP does not discuss revelation,
      so members differ; the sources read do not mention revelation.'
    note: 'Alternative: 3 (observation and reason over revelation in the covered areas). Changed from
      3 (0.5) after the S1 audit.'
    alternatives:
    - value: 3
      note: "Coder's first reading in batch S1."
      cites:
      - source: S1
        locator: §1
  E_scope:
    value: 'UNKNOWN'
    how_known: Not addressed in S1.
epistemology:
  value: Adopt Innate Knowledge and/or Innate Concept theses; Intuition/Deduction for substantive external-world
    claims distinguishes strong rationalism from empiricist use of I/D for relations of ideas
  certainty: 1.0
  cites:
  - source: S1
    locator: §1.1–2
  how_known: SEP.
ethics:
  value: Some rationalists/intuitionists place moral truths under a priori intuition; not one school ethics
  certainty: 0.7
  cites:
  - source: S1
    locator: §1
  how_known: SEP. 0.7.
practice:
  ritual_and_practice:
    value: 'Philosophical method (meditation, demonstration); not a church'
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP.
  community_form:
    value: Academic tradition; textbook Continental rationalists cluster (labels cautioned)
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: SEP.
science:
  historical_stance:
    value: Often intertwined with early modern natural philosophy; Descartes has empiricist leanings in
      natural philosophy per SEP caution
    certainty: 0.7
    cites:
    - source: S1
      locator: introduction; §1
    how_known: '0.7.'
  current_stance:
    value: 'Live in debates on a priori knowledge, intuition, nativism (e.g. language, folk psychology)'
    certainty: 0.7
    cites:
    - source: S1
      locator: §3–4
    how_known: '0.7.'
schools_and_variants:
- name: Classical Continental rationalism (Descartes–Spinoza–Leibniz cluster)
  form: scholastic or philosophical
  how_it_differs: Innate ideas / demonstration; diverse metaphysics
  lio_difference: Not rescored
  certainty: 1.0
  cites:
  - source: S1
    locator: §1
- name: Platonic recollection / Forms antecedent
  form: scholastic or philosophical
  how_it_differs: Knowledge as recollection; abstract Forms
  lio_difference: Not rescored
  certainty: 1.0
  cites:
  - source: S1
    locator: §3
- name: Contemporary nativism / intuitionism strands
  form: modern
  how_it_differs: Chomsky-style capacities vs propositional innate knowledge; moral intuitionism
  lio_difference: 'Coding caution: capacities ≠ classical RATN'
  certainty: 0.7
  cites:
  - source: S1
    locator: §3–4
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: 'Philosophical position, not a census religion'
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP.
v7_1_rubric:
  label: authorial v7.1 scores
  L: 10
  P: 10
  E: 10
  V: 10
  X: 9
  total: 49
  scoring_note: 'Rationalism excels in logical rigor and evidence prioritization, scoring high overall
    but docked slightly for occasional over-reliance on deduction in non-empirical contexts.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 7 and section 7 scoring notes'
revised_rubric:
  status: not started
  L:
    score: 'TODO'
    rationale: ''
  P:
    score: 'TODO'
    rationale: ''
  E:
    score: 'TODO'
    rationale: ''
  V:
    score: 'TODO'
    rationale: ''
  X:
    score: 'TODO'
    rationale: ''
coding_guidance:
  use_when: Person affirms innate knowledge/concepts or a priori substantive knowledge of the external
    world via reason/intuition.
  do_not_use_when: Mere praise of “reason” or STEM competence; subject-relative — can coexist with EMPIR
    in other domains.
  neighbors:
  - code: EMPIR
    relation: contrast case
    note: Paired dispute
  - code: IDEAL
    relation: overlaps
    note: Some metaphysical overlap
  - code: SCEPT
    relation: contrast case
    note: Often anti-skeptical for a domain
review:
  data_quality_flags: []
  open_questions:
  - When to code Chomsky-style nativism as RATN vs leave unscored?
  - Split Spinoza into separate substance monism later?
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Peter Markie; M. Folescu
  year: 2021
  citation: 'Markie, Peter and M. Folescu, “Rationalism vs. Empiricism,” Stanford Encyclopedia of Philosophy
    (Fall 2021 Edition), Edward N. Zalta (ed.).'
  url: 'https://plato.stanford.edu/entries/rationalism-empiricism/'
  accessed: '2026-10-25'
  reliability_note: Peer-reviewed reference entry.
- id: S2
  type: tertiary
  kind: encyclopedia
  author: 'Bobro, Marc, and Tobias Flattery'
  year: 2026
  citation: 'Bobro, Marc, and Tobias Flattery. "Leibniz on Causation." Stanford Encyclopedia of Philosophy.
    https://plato.stanford.edu/entries/leibniz-causation/'
  url: 'https://plato.stanford.edu/entries/leibniz-causation/'
  accessed: '2026-10-15'
  reliability_note: Signed SEP entry (substantive revision 2026-09-30); §3 on occasionalism and miracles
    read.
- id: S3
  type: tertiary
  kind: encyclopedia
  author: 'Lee, Sukjae'
  year: 2019
  citation: 'Lee, Sukjae. "Occasionalism." Stanford Encyclopedia of Philosophy. https://plato.stanford.edu/entries/occasionalism/'
  url: 'https://plato.stanford.edu/entries/occasionalism/'
  accessed: '2026-10-15'
  reliability_note: Signed SEP entry; introduction and Leibniz comparison read. Malebranche is not named
    a rationalist in S1; used only as the contrasting case.
- id: S4
  type: tertiary
  kind: encyclopedia
  author: 'Nadler, Steven'
  year: 2023
  citation: 'Nadler, Steven. "Baruch Spinoza." Stanford Encyclopedia of Philosophy. https://plato.stanford.edu/entries/spinoza/'
  url: 'https://plato.stanford.edu/entries/spinoza/'
  accessed: '2026-10-15'
  reliability_note: Signed SEP entry (2023 revision); §2 (Ethics) read.
---
# Rationalism (RATN)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44. The v7.1 scores and note are unchanged.

## Summary

Rationalism: significant concepts or knowledge independent of sense experience; innate knowledge/concepts and/or intuition-deduction for external-world claims [S1].

## Core metaphysics

Varies widely (Descartes God, Spinoza substance); defining thesis is epistemological [S1].

## Position on the LIO axes

Axes left BELOW_THRESHOLD / prior; this pass fills qualities only.

## Schools and variants

Classical Continental cluster; Platonic antecedent; contemporary nativism/intuitionism (coding caution) [S1].

## Science

Intertwined with early modern natural philosophy; live in a priori / nativism debates [S1].

## Coding guidance

Innate knowledge/concepts or a priori substantive external-world knowledge → RATN. “Likes reason” alone ≠ RATN.

## v7.1 scoring note

Authorial v7.1 note unchanged (see front matter).

## Open questions

- When to code Chomsky-style nativism as RATN vs leave unscored?
- Split Spinoza into separate substance monism later?

## Research log

- 2026-10-25: deepened from SEP Rationalism vs Empiricism; axes unchanged.
