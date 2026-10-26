---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 7
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S5 for Jason)
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
    summary: 'Draft (systems batch S5): filled from SEP "Panpsychism" (Goff, Seager and Allen-Hermanson).
      A BELOW_THRESHOLD; others UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S10 audit fix: A BELOW_THRESHOLD now quote-backed (Spinoza line; cosmopsychism is not pantheism).'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities: family/parents/related codes, origins, metaphysics TODOs (varies/not addressed),
      epistemology, ethics, practice, science, schools (constitutive/emergentist; micro vs cosmo; Russellian).
      A stays BELOW_THRESHOLD; B–E UNKNOWN. Re-read SEP Panpsychism (Goff et al.).'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score D_authority 4 (0.7) from SEP/IEP panpsychism materials on file (philosophical argument).
      A stays BELOW.
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Fill implied axes (C=4@0.5, E=4@0.5, B=4@0.5) from sources on file / P44(c) where naturalistic.
      Alternatives named.'
identity:
  id: PANPSY
  v7_1_number: 33
  v7_1_label: Panpsychism (consciousness inherent in matter)
  display_label: Panpsychism (consciousness inherent in matter)
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: metaphysical thesis
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: "'the view that mentality is fundamental and ubiquitous in the natural world'."
  family:
    value: Metaphysical theses that mentality (esp. experience) is fundamental and ubiquitous in nature
    certainty: 1.0
    cites: &id001
    - source: S1
      locator: introduction
    how_known: SEP definition.
  parent_traditions:
    value:
    - Presocratic mind-in-nature debates
    - Spinoza/Leibniz dual-aspect and monad readings
    - '19th-c. panpsychism'
    - Contemporary analytic philosophy of mind
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: SEP history section.
  related_codes:
  - code: HYLO
    relation: neighbor (easily confused)
    note: Hylozoism attributes life; panpsychism attributes mentality/experience
  - code: IDEAL
    relation: neighbor (easily confused)
    note: Some idealist panpsychisms; SEP focuses naturalistic panexperientialism
  - code: PANENT
    relation: neighbor (easily confused)
    note: Cosmopsychism ≠ pantheism (SEP)
  - code: ANIM
    relation: neighbor (easily confused)
    note: 'Personified spirits are ANIM, not micro-experience'
origins:
  founding_era:
    value: Ancient precursors; 19th-c. heyday; contemporary analytic revival
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: SEP.
  founding_region:
    value: Western philosophy (SEP focus); East and West historically noted
    certainty: 1.0
    cites: *id001
    how_known: SEP introduction.
  founders_or_key_figures:
    value:
    - Thales / Anaxagoras (precursors)
    - Spinoza
    - Leibniz
    - William James
    - A. N. Whitehead
    - 'Contemporary: Chalmers, Strawson, Goff, et al. (as surveyed)'
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: SEP history.
  key_texts:
  - value: SEP surveys James Principles; Whitehead; Nagel 1979; Strawson; Chalmers; recent collections
    certainty: 0.7
    cites:
    - source: S1
      locator: §1
    how_known: SEP. 0.7.
metaphysics:
  god_nature_relation:
    value: "Varies: Spinoza's substance identified with God; William James's panpsychism grew from neutral\
      \ monism."
    stance: varies by school
    certainty: 0.7
    cites:
    - source: S1
      locator: §2
    how_known: SEP.
  deity_personal:
    value: 'Varies: Spinoza God-substance readings; cosmopsychism not pantheism; many analytic forms are
      non-theistic.'
    stance: varies by school
    certainty: 0.7
    cites:
    - source: S1
      locator: §1; §2.4
    how_known: SEP. 0.7.
  intervention:
    value: Not a miracle religion; a metaphysics of mind in nature.
    stance: not addressed
    certainty: 1.0
    cites: *id001
    how_known: SEP.
  miracles:
    value: Not addressed as shared doctrine.
    stance: not addressed
    certainty: 1.0
    cites: *id001
    how_known: SEP.
  petition_and_prayer:
    value: Not a cult practice of the thesis.
    stance: not addressed
    certainty: 1.0
    cites: *id001
    how_known: SEP.
  afterlife:
    value: Not fixed by panpsychism as such.
    stance: not addressed
    certainty: 1.0
    cites: *id001
    how_known: SEP.
  moral_ledger:
    value: Not a shared moral-judgment theology.
    stance: none
    certainty: 1.0
    cites: *id001
    how_known: SEP is philosophy of mind.
  authority:
    value: 'Philosophical argument (anti-emergence, intrinsic natures, etc.).'
    stance: observation and reason
    certainty: 0.7
    cites:
    - source: S1
      locator: §3
    how_known: SEP arguments section. 0.7.
  reserved_exemptions:
    value: Not addressed.
    stance: none
    certainty: 1.0
    cites: *id001
    how_known: SEP.
  teleology_in_nature:
    value: Not required; some cosmopsychist variants (e.g. Goff fine-tuning discussion in SEP) add agency
      — not the default.
    stance: varies by school
    certainty: 0.7
    cites:
    - source: S1
      locator: §2.4
    how_known: '0.7.'
  necessity_and_freedom:
    value: Not a shared free-will doctrine; mental causation is a motivation for some Russellian forms.
    certainty: 0.7
    cites:
    - source: S1
      locator: §2.5
    how_known: SEP Russellian monism. 0.7.
lio_axes:
  A_locus:
    value: 'BELOW_THRESHOLD'
    how_known: "Panpsychists differ on God (P44(b)). Spinoza 'regarded both mind and matter as simply\
      \ aspects (or attributes) of the eternal, infinite and unique substance he identified with God Himself'\
      \ (S1 §1); for contemporary forms, 'Cosmopsychism is not to be confused with pantheism: the view\
      \ that the universe is God' (S1 §2.4), and panpsychism 'has recently enjoyed a revival in analytic\
      \ philosophy' (S1, introduction)."
    note: 'Evidence: S1 §2.'
  B_cause:
    value: 4
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — no miracle doctrine in analytic panpsychism.'
    rationale: B=4 at 0.5.
    alternatives:
    - value: 'UNKNOWN'
      note: Named alternative if refusing P44(c) implied score.
      cites:
      - source: S1
        locator: opening
  C_ledger:
    value: 4
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — metaphysical thesis; no shared divine ledger.'
    rationale: C=4 at 0.5.
    alternatives:
    - value: 'UNKNOWN'
      note: Named alternative if refusing P44(c) implied score.
      cites:
      - source: S1
        locator: opening
  D_authority:
    value: 4
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: '0.7 — philosophical argument (anti-emergence, intrinsic natures); stance observation and
      reason.'
    rationale: 'D=4: argument over revelation. Not 3: Spinoza-theistic readings are schools.'
    alternatives:
    - value: 3
      note: Named alternative if coding cosmopsychism-with-God as primary.
      cites:
      - source: S1
        locator: opening
  E_scope:
    value: 4
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — mind/experience widespread; same order (P44c-ish).'
    rationale: E=4 at 0.5.
    alternatives:
    - value: 'UNKNOWN'
      note: Named alternative if refusing P44(c) implied score.
      cites:
      - source: S1
        locator: opening
epistemology:
  value: 'Arguments from hard problem / anti-emergence, intrinsic natures of matter, and related; combination
    problem is the chief internal challenge.'
  certainty: 1.0
  cites:
  - source: S1
    locator: §3–4
  how_known: SEP.
ethics:
  value: Not a shared ethical program; metaphysical thesis about mind.
  certainty: 1.0
  cites: *id001
  how_known: SEP.
practice:
  ritual_and_practice:
    value: 'Philosophical thesis, not a ritual religion.'
    certainty: 1.0
    cites: *id001
    how_known: SEP.
  community_form:
    value: Academic debate in philosophy of mind.
    certainty: 1.0
    cites: *id001
    how_known: SEP.
science:
  historical_stance:
    value: Engages physics’ silence on intrinsic natures (Russell/Eddington line) and neuroscience’s hard
      problem.
    certainty: 1.0
    cites:
    - source: S1
      locator: §3.2
    how_known: SEP.
  current_stance:
    value: Live analytic research programme; combination problem unsolved by consensus; some link to IIT
      (Mørch) noted in SEP.
    certainty: 1.0
    cites:
    - source: S1
      locator: §2.2; §4.2
    how_known: SEP.
schools_and_variants:
- name: Constitutive micropsychism
  form: scholastic or philosophical
  how_it_differs: Macro consciousness grounded in micro experience
  lio_difference: A still BELOW_THRESHOLD for family
  certainty: 1.0
  cites:
  - source: S1
    locator: §2.2
- name: Emergentist / fusionist panpsychism
  form: scholastic or philosophical
  how_it_differs: Macro minds fundamental products of micro subjects
  lio_difference: May move axes — not rescored
  certainty: 1.0
  cites:
  - source: S1
    locator: §2.2
- name: Cosmopsychism
  form: scholastic or philosophical
  how_it_differs: Cosmic-level consciousness grounds or coexists with parts; ≠ pantheism
  lio_difference: May move A — still BELOW_THRESHOLD for family
  certainty: 1.0
  cites:
  - source: S1
    locator: §2.4
- name: Russellian monism (panpsychist form)
  form: scholastic or philosophical
  how_it_differs: Intrinsic natures of physics are phenomenal; aims to fix causal closure + hard problem
  lio_difference: Not rescored
  certainty: 1.0
  cites:
  - source: S1
    locator: §2.5
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Not a census religion; philosophical position
    certainty: 1.0
    cites: *id001
    how_known: SEP.
v7_1_rubric:
  label: authorial v7.1 scores
  L: 8
  P: 8
  E: 7
  V: 9
  X: 7
  total: 39
  scoring_note: 'Panpsychism scores moderately high as an innovative philosophy bridging consciousness
    and matter, with strong logical appeal but tempered by speculative elements and incomplete empirical
    support.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 33 and section 7 scoring notes'
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
  use_when: "The person's own writing holds that mentality is fundamental and ubiquitous in nature (considered\
    \ for Riemann, stage 3)."
  do_not_use_when: Spinoza is PANT. PANPSY sets no God-view.
  neighbors:
  - code: HYLO
    relation: neighbor (easily confused)
    note: Life ≠ mentality
  - code: ANIM
    relation: neighbor (easily confused)
    note: Personified spirits → ANIM
review:
  data_quality_flags: []
  open_questions:
  - Can A be scored for Spinoza-leaning vs atheistic analytic forms without P44(b) collapse?
  - 'Panprotopsychism: same code or separate?'
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Philip Goff; William Seager; Sean Allen-Hermanson
  year: 2022
  citation: 'Philip Goff and William Seager and Sean Allen-Hermanson. "Panpsychism." Stanford Encyclopedia
    of Philosophy. First published May 23, 2001; substantive revision May 13, 2022. https://plato.stanford.edu/entries/panpsychism/.'
  url: 'https://plato.stanford.edu/entries/panpsychism/'
  accessed: '2026-10-25'
  reliability_note: Peer-reviewed reference entry.
---
# Panpsychism (consciousness inherent in matter) (PANPSY)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44. The v7.1 scores and note are unchanged.

## Summary

Panpsychism is the view that mentality is fundamental and ubiquitous in the natural world [S1]. Contemporary analytic forms are mostly panexperientialist (experience all the way down), not pancognitivist (thought in electrons) [S1]. SEP surveys history from Presocratics through James and Whitehead to the present revival [S1].

## Core metaphysics

Mentality (experience) in nature’s base [S1]. Schools: constitutive vs emergentist; micropsychism vs cosmopsychism; Russellian monism [S1]. Cosmopsychism is not pantheism [S1]. Not a cult religion: petition, miracles, and afterlife are not shared doctrines.

## Position on the LIO axes

- **A_locus:** BELOW_THRESHOLD — panpsychists differ on God (Spinoza vs others; cosmopsychism ≠ pantheism) [S1] (P44(b)).
- **B–E:** UNKNOWN.

## Schools and variants

Constitutive micropsychism; emergentist/fusionist forms; cosmopsychism; Russellian panpsychism [S1].

## Science

Intrinsic-natures argument from physics’ mathematical/nomic vocabulary; hard-problem motivation; combination problem as chief objection [S1].

## Coding guidance

Consciousness/mentality in matter → PANPSY. Living matter without mentality claim → HYLO. Personified spirits → ANIM.

## v7.1 scoring note

Authorial v7.1 note unchanged (see front matter).

## Open questions

- Can A be scored for Spinoza-leaning vs atheistic analytic forms without P44(b) collapse?
- Panprotopsychism: same code or separate?

## Research log

- 2026-10-15 batch: A BELOW_THRESHOLD from SEP.
- 2026-10-25: deepened TODOs; re-read SEP Panpsychism.
- 2026-10-25: D_authority scored 4 (0.7).
- 2026-10-25: implied axis fill: C=4@0.5, E=4@0.5, B=4@0.5.
