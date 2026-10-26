---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 6
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S2 for Jason)
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
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'Draft (systems batch S2): filled from SEP "Pragmatism" (Legg and Hookway). A and D BELOW_THRESHOLD
      (pragmatists differ); B, C, E UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'T2: B_cause searched, unchanged; search logged.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from SEP Pragmatism (Legg/Hookway): family/parents/region, metaphysics
      TODOs, ethics, practice, science, schools (Peirce, James, Dewey, neopragmatism). Axes unchanged.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Score D_authority 4 (0.7) from SEP Pragmatism (experience, experiment, community of inquiry).
      Was BELOW_THRESHOLD.'
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
      locator: introduction
    how_known: 'SEP: philosophical tradition.'
  family:
    value: Knowing the world as inseparable from agency within it; pragmatic clarification of concepts
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP.
  parent_traditions:
    value:
    - American philosophy (Metaphysical Club ~1870)
    - Empiricism (radicalized)
    - Evolutionary science context
    - Later neopragmatism and New Pragmatism
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: SEP.
  related_codes:
  - code: EMPIR
    relation: overlaps
    note: Empiricist attitude radicalized
  - code: UTIL
    relation: overlaps
    note: James links pragmatism to utilitarian ethics
  - code: IDEAL
    relation: neighbor (easily confused)
    note: Royce interlocutor; absolute idealism contrast
  - code: SCEPT
    relation: contrast case
    note: Fallibilism vs Cartesian skepticism
origins:
  founding_era:
    value: United States around 1870; Peirce then James popularization 1898/1907
    certainty: 1.0
    cites:
    - source: S1
      locator: §1.1
    how_known: SEP.
  founding_region:
    value: United States (Harvard Metaphysical Club); later worldwide networks
    certainty: 1.0
    cites:
    - source: S1
      locator: §1.1
    how_known: SEP.
  founders_or_key_figures:
    value:
    - Charles Sanders Peirce
    - William James
    - John Dewey
    - Jane Addams
    - Richard Rorty (neopragmatism)
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: SEP.
  key_texts:
  - value: 'Peirce, “How to Make Our Ideas Clear” (1878); James, Pragmatism (1907); Dewey, Logic / Democracy
      and Education'
    certainty: 1.0
    cites:
    - source: S1
      locator: §2; §4
    how_known: SEP.
metaphysics:
  god_nature_relation:
    value: 'Varies: James explores religious truth; Dewey naturalizes the sacred as quality of experience;
      Peirce later theistic arguments; not a shared creed'
    stance: varies by school
    certainty: 1.0
    cites:
    - source: S1
      locator: §5.1
    how_known: SEP philosophy of religion.
  deity_personal:
    value: Varies by school (Jamesian faith; Deweyan non-supernatural; Peirce late theism)
    stance: varies by school
    certainty: 1.0
    cites:
    - source: S1
      locator: §5.1
    how_known: SEP.
  intervention:
    value: Not a shared intervention doctrine; method dissolves idle metaphysical disputes
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: §2.2
    how_known: SEP method focus.
  miracles:
    value: Not a shared miracle doctrine
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP.
  petition_and_prayer:
    value: James studies prayer/mystical experience empirically; not a required practice
    stance: varies by school
    certainty: 0.7
    cites:
    - source: S1
      locator: §5.1
    how_known: Varieties. 0.7.
  afterlife:
    value: Not a shared doctrine
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP.
  moral_ledger:
    value: 'Not a divine ledger; ethics tied to inquiry, democracy, utility/plural values by school'
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: §5.2
    how_known: '0.7.'
  authority:
    value: 'Experience, experiment, community of inquiry; fallibilism over revelation or Cartesian certainty'
    stance: observation and reason
    certainty: 1.0
    cites:
    - source: S1
      locator: §4
    how_known: SEP epistemology.
  reserved_exemptions:
    value: No in-group miracle exemptions as doctrine
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: §4.1
    how_known: '0.7.'
  teleology_in_nature:
    value: Inquiry and growth metaphors; Peirce evolutionary love; not classical designer teleology as
      shared creed
    stance: varies by school
    certainty: 0.7
    cites:
    - source: S1
      locator: §5.1–5.2
    how_known: '0.7.'
  necessity_and_freedom:
    value: James treats free will vs determinism as practically reconcilable once consequences clarified;
      fallibilist agency
    certainty: 0.7
    cites:
    - source: S1
      locator: §2.2
    how_known: SEP James. 0.7.
lio_axes:
  A_locus:
    value: 'BELOW_THRESHOLD'
    how_known: 'Pragmatists differ (P44b): James explored truth in religion; SEP gives no shared God-view.'
    note: 'Evidence: S1 §1–2.'
  B_cause:
    value: 'UNKNOWN'
    how_known: Not addressed in S1.
  C_ledger:
    value: 'UNKNOWN'
    how_known: Not addressed in S1.
  D_authority:
    value: 4
    certainty: 0.7
    cites:
    - source: S1
      locator: introduction; Pragmatic Maxim
    how_known: '0.7 — experience, experiment, fallibilism; stance observation and reason.'
    rationale: 'D=4: inquiry and consequences outrank revelation as family method. Not 3: James’s will-to-believe
      is a school tension, not the family default.'
    alternatives:
    - value: 3
      note: Named alternative if coding James’s will-to-believe as making faith co-equal with inquiry.
      cites:
      - source: S1
        locator: James
  E_scope:
    value: 'UNKNOWN'
    how_known: Not addressed in S1.
epistemology:
  value: "The Pragmatic Maxim: 'a rule for clarifying the meaning of hypotheses by tracing their implications\
    \ for experience in specific situations'; 'a fallibilist, anti-Cartesian explication of the norms\
    \ that govern inquiry'."
  certainty: 1.0
  cites:
  - source: S1
    locator: opening; §2
  how_known: SEP.
ethics:
  value: 'Diverse: James links to utilitarian ethics; Dewey problem-centered moral inquiry and democratic
    ideal; Peirce late normative science of ethics under aesthetics/logic'
  certainty: 1.0
  cites:
  - source: S1
    locator: §5.2
  how_known: SEP.
practice:
  ritual_and_practice:
    value: 'Method and inquiry practice; education and social reform (Dewey, Addams); not a church'
    certainty: 1.0
    cites:
    - source: S1
      locator: §5.4
    how_known: SEP.
  community_form:
    value: Academic and reform networks; progressive-era settlements; contemporary research networks worldwide
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: SEP.
science:
  historical_stance:
    value: Peirce’s laboratory philosophy; scientific method as model of inquiry
    certainty: 1.0
    cites:
    - source: S1
      locator: §2.1
    how_known: SEP.
  current_stance:
    value: 'Continues in philosophy of science, democracy theory, education; neopragmatist and New Pragmatist
      strands'
    certainty: 1.0
    cites:
    - source: S1
      locator: §1.2
    how_known: SEP.
schools_and_variants:
- name: Peircean pragmaticism
  form: scholastic or philosophical
  how_it_differs: Maxim as logical principle; truth as end of inquiry; scientific realism lean
  lio_difference: Not rescored
  certainty: 1.0
  cites:
  - source: S1
    locator: §2.1; §3.1
- name: Jamesian pragmatism
  form: scholastic or philosophical
  how_it_differs: Mediating philosophy; plural truth; Will to Believe; religious comfort as truth-relevant
  lio_difference: May soften A/D vs Peirce — not rescored
  certainty: 1.0
  cites:
  - source: S1
    locator: §2.2; §3.2
- name: Deweyan pragmatism / progressive
  form: modern
  how_it_differs: Inquiry transforms situations; democracy as way of life; education
  lio_difference: Not rescored
  certainty: 1.0
  cites:
  - source: S1
    locator: §4.2; §5.2
- name: Neopragmatism (Rorty et al.)
  form: modern
  how_it_differs: Anti-representationalism; vocabularies; truth as endorsement/cautionary
  lio_difference: Not rescored
  certainty: 1.0
  cites:
  - source: S1
    locator: §1.2
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Philosophical tradition; not a census religion
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP.
v7_1_rubric:
  label: authorial v7.1 scores
  L: 10
  P: 9
  E: 10
  V: 10
  X: 9
  total: 48
  scoring_note: 'Pragmatism excels in practical, evidence-based problem-solving, with a high score reflecting
    its adaptability and real-world focus.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 10 and section 7 scoring notes'
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
  use_when: 'Person’s writing centers pragmatic method, fallibilist inquiry, or classical/neo pragmatist
    lineage as main worldview.'
  do_not_use_when: Mere practicality or “what works” slogans without the philosophical tradition.
  neighbors:
  - code: EMPIR
    relation: overlaps
    note: Empiricist root
  - code: UTIL
    relation: overlaps
    note: Jamesian ethics link
  - code: SCEPT
    relation: contrast case
    note: Fallibilism ≠ skepticism
review:
  data_quality_flags: []
  open_questions:
  - Score A/D by school (James religious vs Dewey naturalist)?
  - Keep neopragmatism under PRAG or split later?
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Catherine Legg; Christopher Hookway
  year: 2024
  citation: 'Legg, Catherine, and Christopher Hookway. "Pragmatism." Stanford Encyclopedia of Philosophy.
    First published August 16, 2008; substantive revision September 30, 2024. https://plato.stanford.edu/entries/pragmatism/.'
  url: 'https://plato.stanford.edu/entries/pragmatism/'
  accessed: '2026-10-25'
  reliability_note: Peer-reviewed reference entry.
---
# Pragmatism (PRAG)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44. The v7.1 scores and note are unchanged.

## Summary

Pragmatism: knowing the world as inseparable from agency within it; Peirce’s Maxim, James’s mediating method, Dewey’s inquiry and democracy [S1].

## Core metaphysics

Varies by school on God/religion; shared fallibilist, experience-rich epistemology; not a church creed [S1].

## Position on the LIO axes

Axes left UNKNOWN / prior coding unchanged this pass (qualities fill only).

## Schools and variants

Peirce; James; Dewey; neopragmatism [S1].

## Science

Laboratory philosophy / scientific method as inquiry model [S1].

## Coding guidance

Philosophical pragmatist lineage → PRAG. Vague “what works” alone ≠ PRAG.

## v7.1 scoring note

Authorial v7.1 note unchanged (see front matter).

## Open questions

- Score A/D by school (James religious vs Dewey naturalist)?
- Keep neopragmatism under PRAG or split later?

## Research log

- Prior partial fill (epistemology).
- 2026-10-25: deepened from SEP Pragmatism; axes unchanged.
- 2026-10-25: D_authority scored 4 (0.7).
