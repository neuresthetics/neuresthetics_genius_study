---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 4
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S9 for Jason)
  model_used: Grok Bot executor agent; direct reads of the cited pages
  collected_on: '2026-10-01'
  last_updated: '2026-10-25'
  change_log:
  - date: '2026-10-01'
    by: scripts/make_system_stubs.py
    summary: Stub created from v7.1 data book table 4 and section 7.
  - date: '2026-10-02'
    by: scripts/make_system_stubs.py
    summary: 'Decision P7: E_scope note added. E is not scored in a stub; when it is, score it on the
      world''s order (same rules for every kind of being and event, no in-group exceptions in this-world
      events). Salvation and moral community go on C_ledger.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'Draft (systems batch S12): filled from Britannica "Scientology" (Melton). A BELOW_THRESHOLD;
      B, C, D, E UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from Britannica Scientology (Melton): Hubbard, Dianetics to Scientology,
      thetan/engrams/auditing, eight dynamics, CSI/RTC. Keep A BELOW_THRESHOLD; B C D E UNKNOWN.'
identity:
  id: SCIENT
  v7_1_number: 77
  v7_1_label: Scientology
  display_label: Scientology
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: new religious movement
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Church of Scientology founded 1954; international movement.
  family:
    value: 'Scientology: Hubbard movement from Dianetics (1950) to religious Scientology; thetan, engrams,
      auditing, operating thetan levels'
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; beliefs
    how_known: Britannica.
  parent_traditions:
    value:
    - Hubbard's Dianetics mental therapy
    - Resemblance to Eastern reincarnation and Western Gnostic tradition (per Britannica)
    - Brief prior Hubbard involvement in Californian Thelemic group (noted under Thelema article; not
      detailed here)
    certainty: 0.7
    cites:
    - source: S1
      locator: opening; beliefs
    how_known: Britannica Scientology + cross-ref.
  related_codes:
  - code: THELEM
    relation: neighbor (easily confused)
    note: historical Hubbard contact ≠ Thelema identity
  - code: BRGHTS
    relation: contrast case
    note: Scientology claims religious/spiritual salvage
  - code: SECHUM
    relation: contrast case
    note: different humanism
origins:
  founding_era:
    value: Dianetics 1950; Church of Scientology founded 1954; Hubbard resigns offices 1966; OT research
      at sea
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; organization
    how_known: Britannica.
  founding_region:
    value: United States; now operates in 150+ countries
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; present
    how_known: Britannica.
  founders_or_key_figures:
    value:
    - L. Ron Hubbard
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  key_texts:
  - value: 'Dianetics: The Modern Science of Mental Health (1950)'
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  - value: Hubbard's Scientology writings (published and unpublished considered scriptures)
    certainty: 1.0
    cites:
    - source: S1
      locator: Hubbard early life
    how_known: Britannica.
metaphysics:
  god_nature_relation:
    value: Thetans originated with original Cause; trapped in MEST; eight dynamics culminate in infinity
      or God. Church does not prescribe specific teachings about God; members free to conclude God's nature.
    stance: varies by school
    certainty: 0.7
    cites:
    - source: S1
      locator: beliefs
    how_known: Britannica — why A is BELOW_THRESHOLD.
  deity_personal:
    value: Belief in Supreme Being affirmed as cultural observation by Hubbard; no prescribed deity doctrine.
    stance: not addressed
    certainty: 0.5
    cites:
    - source: S1
      locator: beliefs
    how_known: 0.5 — Hubbard affirms but church does not prescribe.
  intervention:
    value: Not classical deity intervention; auditing/tech as path to free thetan.
    stance: not addressed
    certainty: 0.5
    cites:
    - source: S1
      locator: beliefs
    how_known: Thin theistic intervention.
  miracles:
    value: Exteriorization and OT abilities claimed; medical establishment conflict.
    stance: affirmed
    certainty: 0.5
    cites:
    - source: S1
      locator: beliefs; controversy
    how_known: 0.5.
  petition_and_prayer:
    value: Auditing counseling central; not petitionary prayer doctrine.
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S1
      locator: auditing
    how_known: Silence on petition.
  afterlife:
    value: Thetans inhabited other bodies before present — reincarnation-like; salvage of human spirit.
    stance: rebirth
    certainty: 0.7
    cites:
    - source: S1
      locator: beliefs
    how_known: Britannica.
  moral_ledger:
    value: 'Survival principle: survival-oriented actions good/pleasure; countersurvival destructive.
      Not afterlife ledger.'
    stance: impersonal consequence
    certainty: 0.5
    cites:
    - source: S1
      locator: beliefs
    how_known: 0.5.
  authority:
    value: Hubbard scriptures; RTC ultimate ecclesiastical authority for teachings/trademarks; CSI coordinates.
    stance: founder
    certainty: 0.7
    cites:
    - source: S1
      locator: organization
    how_known: Britannica — D could be 1 but kept UNKNOWN per prior (P44 no move without clear prior intent).
  reserved_exemptions:
    value: Not addressed.
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: Silence.
  teleology_in_nature:
    value: Original Cause purpose was creation of effect; thetans created MEST.
    stance: immanent ends
    certainty: 0.5
    cites:
    - source: S1
      locator: beliefs
    how_known: 0.5.
  necessity_and_freedom:
    value: Goal to free thetan to function freely; not classical free-will thesis.
    certainty: 0.7
    cites:
    - source: S1
      locator: beliefs
    how_known: Britannica.
lio_axes:
  A_locus:
    value: BELOW_THRESHOLD
    how_known: Members 'are free to reach their own conclusions as to God’s nature'; 'the church does
      not prescribe specific teachings about God' (S1).
    note: Members differ by design (P44(b)).
  B_cause:
    value: UNKNOWN
    how_known: Not addressed in the sources read.
  C_ledger:
    value: UNKNOWN
    how_known: Not addressed in the sources read.
  D_authority:
    value: UNKNOWN
    how_known: Not addressed in the sources read.
  E_scope:
    value: UNKNOWN
    how_known: Not addressed in the sources read.
epistemology:
  value: Auditing with E-meter to bring engrams to consciousness; OT levels as restricted sacred training;
    Hubbard writings as scripture.
  certainty: 1.0
  cites:
  - source: S1
    locator: auditing; organization
  how_known: Britannica.
ethics:
  value: Survival-oriented action as good; eight dynamics expand identification; opposition to psychiatry/consciousness-altering
    drugs via CCHR.
  certainty: 0.7
  cites:
  - source: S1
    locator: beliefs; controversy
  how_known: Britannica.
practice:
  ritual_and_practice:
    value: Auditing; training to Clear then OT levels; churches/missions licensed; Flag Service Organization
      for higher OT; ship Freewinds for OT-VIII.
    certainty: 1.0
    cites:
    - source: S1
      locator: organization
    how_known: Britannica.
  community_form:
    value: Local churches/missions; CSI; RTC; Advanced Organization centers; celebrity adherents noted.
    certainty: 1.0
    cites:
    - source: S1
      locator: organization; present
    how_known: Britannica.
science:
  historical_stance:
    value: Began as claimed science of the mind (Dianetics); conflict with medicine/psychiatry; E-meter
      FDA raid 1963; religious framing later.
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; controversy
    how_known: Britannica.
  current_stance:
    value: Church opposes psychiatry as denying spiritual nature; presents spiritual technology.
    certainty: 0.7
    cites:
    - source: S1
      locator: controversy
    how_known: Britannica.
schools_and_variants:
- name: Church of Scientology (CSI/RTC)
  form: modern
  how_it_differs: Institutional Scientology.
  lio_difference: A BELOW_THRESHOLD; others UNKNOWN.
  certainty: 1.0
  cites:
  - source: S1
    locator: organization
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: TODO
v7_1_rubric:
  label: authorial v7.1 scores
  L: 6
  P: 5
  E: 2
  V: 3
  X: 1
  total: 17
  scoring_note: Scientology scores low due to its pseudoscientific claims and reliance on founder authority
    over empirical evidence, despite structured self-improvement appeals.
  source: v7.1 data book, section 6 table (tables[4]) row 77 and section 7 scoring notes
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
  use_when: Church of Scientology / Dianetics–Scientology identity.
  do_not_use_when: Generic self-help without Scientology. Thelema.
  neighbors:
  - code: THELEM
    relation: neighbor (easily confused)
  - code: BRGHTS
    relation: contrast case
review:
  data_quality_flags: []
  open_questions:
  - 'B and D: auditing and the E-meter are described but not as a stance on nature or authority.'
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: J. Gordon Melton
  citation: 'Melton, J. Gordon. "Scientology." Encyclopaedia Britannica. https://www.britannica.com/topic/Scientology.
    Wayback Machine snapshot 2026-09-26 21:46:58 UTC: https://web.archive.org/web/20260926214658/https://www.britannica.com/topic/Scientology.'
  url: https://www.britannica.com/topic/Scientology
  accessed: '2026-10-25'
  reliability_note: 'Signed article; beliefs section read. P44(e): read in the Wayback copy (https://web.archive.org/web/20260926214658/https://www.britannica.com/topic/Scientology);
    live page not compared (live Britannica times out from the box).'
---
# Scientology (SCIENT)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

Scientology emerged from Hubbard's Dianetics (1950) into the Church of Scientology (1954): thetan, engrams, auditing, OT levels, eight dynamics [S1].

## Core metaphysics

Thetans trapped in MEST; God/infinity as eighth dynamic without prescribed deity doctrine [S1].

## Position on the LIO axes

- **A:** BELOW_THRESHOLD — no prescribed God doctrine [S1].
- **B, C, D, E:** UNKNOWN (D could be founder=1; left UNKNOWN this pass — P44).

## Schools and variants

CSI/RTC institutional church [S1].

## Science

From science-of-mind claim to religious tech; psychiatry conflict [S1].

## Coding guidance

Scientology identity.

## v7.1 scoring note

> SCIENT (17/50) — Scientology. Scientology scores low due to its pseudoscientific claims and reliance on founder authority over empirical evidence, despite structured self-improvement appeals.

## Open questions

- Score D=1 (founder/RTC) at 0.5? Left UNKNOWN pending Jason.

## Research log

- Prior batch: Britannica Scientology; A BELOW_THRESHOLD.
- 2026-10-25: deepened. Axes kept; note D question.
