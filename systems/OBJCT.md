---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 6
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S3 for Jason)
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
    summary: 'Draft (systems batch S3): filled from SEP "Ayn Rand" (Badhwar and Long). A BELOW_THRESHOLD
      (alt 4); D 4 (0.5); others UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S3 audit RQ4: A stays BELOW_THRESHOLD (alt 4); unverified leads noted.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from SEP Ayn Rand (Badhwar/Long): family/parents, metaphysics TODOs, epistemology,
      ethics, practice, science, schools. Axes unchanged (A still BELOW_THRESHOLD pending explicit God
      denial).'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score A4 B4 C4 E4 (0.7) from sources on file (atheistic naturalism; reason). D already 4.
      Was A BELOW.
identity:
  id: OBJCT
  v7_1_number: 19
  v7_1_label: "Objectivism (Ayn Rand's philosophy)"
  display_label: "Objectivism (Ayn Rand's philosophy)"
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: philosophical school or method
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction; §1.3
    how_known: "Rand 'outlined a comprehensive philosophy' named 'Objectivism'."
  family:
    value: 'Objectivism: metaphysical realism, reason, ethical egoism, individual rights, laissez-faire
      capitalism'
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP.
  parent_traditions:
    value:
    - Aristotelian realism (Rand tribute)
    - Classical liberalism / Lockean founding
    - Nietzschean style influences (partial)
    - Anti-collectivist reaction to Soviet experience
    certainty: 0.7
    cites:
    - source: S1
      locator: §1.2
    how_known: SEP life and work. 0.7.
  related_codes:
  - code: ATHE
    relation: neighbor (easily confused)
    note: Often coded near; A still BELOW_THRESHOLD until explicit God denial sourced
  - code: UTIL
    relation: contrast case
    note: Egoism vs utilitarian aggregate
  - code: EXIST
    relation: neighbor (easily confused)
    note: Heroic individual; different metaphysics
  - code: EMPIR
    relation: overlaps
    note: Experience and reason; not identical
origins:
  founding_era:
    value: Mid-twentieth century (Atlas Shrugged 1957; an organised following by 1958)
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: SEP.
  founding_region:
    value: United States
    certainty: 0.7
    cites:
    - source: S1
      locator: §1
    how_known: "Coder's gloss, 0.7."
  founders_or_key_figures:
    value:
    - Ayn Rand
    - Nathaniel Branden
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: SEP.
  key_texts:
  - value: The Fountainhead (1943); Atlas Shrugged (1957)
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: SEP.
  - value: The Virtue of Selfishness (1964); Introduction to Objectivist Epistemology
    certainty: 1.0
    cites:
    - source: S1
      locator: §1; bibliography
    how_known: SEP.
metaphysics:
  god_nature_relation:
    value: SEP quotes rejection of sacrifice for the supernatural (mysticism) but no explicit denial of
      God in sources read; A remains BELOW_THRESHOLD
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: Prior A note; unchanged.
  deity_personal:
    value: Not fixed in SEP passages used; mysticism rejected as category
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: SEP.
  intervention:
    value: This-worldly; no supernatural consolation in the ethical programme
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: §2
    how_known: Anti-mysticism. 0.7.
  miracles:
    value: Supernatural as mysticism rejected
    stance: denied
    certainty: 0.7
    cites:
    - source: S1
      locator: §2
    how_known: '0.7.'
  petition_and_prayer:
    value: Not a religious practice system
    stance: no petition
    certainty: 0.7
    cites:
    - source: S1
      locator: §2
    how_known: '0.7.'
  afterlife:
    value: Soul as mind/spirit celebrating life on this earth; not immortal substance dualism
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: §1.2
    how_known: SEP on Atlas “soul”. 0.7.
  moral_ledger:
    value: No divine reward/punishment ledger; virtue rewarded in this life as happiness/survival qua
      man
    stance: none
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: SEP ethics.
  authority:
    value: "Reason: 'reason is the chief indispensable human tool of survival'; sacrifice 'for the sake\
      \ of the supernatural' is what she calls mysticism."
    stance: observation and reason
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: SEP.
  reserved_exemptions:
    value: Same moral law for all; rights non-initiation of force; no tribal exemption
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: §3
    how_known: '0.7.'
  teleology_in_nature:
    value: Life as end in itself for living entities; ethics teleological and this-worldly; not designer
      purposes in nature
    stance: immanent ends
    certainty: 0.7
    cites:
    - source: S1
      locator: §2.1
    how_known: SEP axiology. 0.7.
  necessity_and_freedom:
    value: Free will affirmed (differs from Nietzsche); choices determine course of life
    certainty: 0.7
    cites:
    - source: S1
      locator: §1.2
    how_known: SEP notes free will difference from Nietzsche. 0.7.
lio_axes:
  A_locus:
    value: 4
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: '0.7 — Objectivism rejects God/supernatural; P44a.'
    rationale: 'A=4: no God. Was BELOW; stance itself fixes it.'
    alternatives:
    - value: 'BELOW_THRESHOLD'
      note: Named alternative if coding only Rand’s early cultural theism residue.
      cites:
      - source: S1
        locator: opening
  B_cause:
    value: 4
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: '0.7 — natural law / identity; no miracles.'
    rationale: 'B=4: regularity, no special cases.'
    alternatives:
    - value: 3
      note: Named alternative if weighting literary romanticism.
      cites:
      - source: S1
        locator: opening
  C_ledger:
    value: 4
    certainty: 0.7
    cites:
    - source: S1
      locator: ethics
    how_known: '0.7 — this-world rational self-interest; no divine ledger.'
    rationale: 'C=4: none. Not 3: not karma.'
    alternatives:
    - value: 3
      note: Named alternative if reading trade principle as impersonal law.
      cites:
      - source: S1
        locator: ethics
  D_authority:
    value: 4
    rationale: Reason the chief human tool; the supernatural rejected as mysticism.
    certainty: 0.5
    cites:
    - source: S1
      locator: §2
    how_known: 'Fixed by the stance; revelation not named, 0.5.'
  E_scope:
    value: 4
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: '0.7 — same natural identity for all existents; P44c.'
    rationale: 'E=4: same rules for kinds of being.'
    alternatives:
    - value: 'UNKNOWN'
      note: Named alternative if refusing cosmology read.
      cites:
      - source: S1
        locator: opening
epistemology:
  value: Objectivism named from objective (vs intrinsic/subjective) trichotomy; reason as only absolute;
    concepts and perception defended against subjectivism
  certainty: 1.0
  cites:
  - source: S1
    locator: §1.3
  how_known: SEP.
ethics:
  value: Ethical egoism / rational self-interest; man’s life as standard; rationality the basic virtue;
    rejects altruism as self-sacrifice duty
  certainty: 1.0
  cites:
  - source: S1
    locator: §2
  how_known: SEP.
practice:
  ritual_and_practice:
    value: 'Philosophical movement with lectures, journals; not a church; novels as primary vehicle'
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: SEP.
  community_form:
    value: Objectivist movement (Branden era then splits); institutes and societies; academic engagement
      limited
    certainty: 1.0
    cites:
    - source: S1
      locator: §1.1
    how_known: SEP.
science:
  historical_stance:
    value: Allies with productive science and industry as heroic; anti-mysticism
    certainty: 0.7
    cites:
    - source: S1
      locator: §1.2
    how_known: '0.7.'
  current_stance:
    value: Still largely outside academic philosophy; applied by adherents to social issues
    certainty: 0.7
    cites:
    - source: S1
      locator: §1.1
    how_known: '0.7.'
schools_and_variants:
- name: Rand’s own Objectivism (novels + non-fiction)
  form: modern
  how_it_differs: 'Canonical texts; heroism, egoism, capitalism'
  lio_difference: D 4; A pending
  certainty: 1.0
  cites:
  - source: S1
    locator: introduction
- name: Orthodox / Peikoff lineage
  form: modern
  how_it_differs: 'Systematizing Objectivism: The Philosophy of Ayn Rand'
  lio_difference: May supply A evidence — not yet scored
  certainty: 0.5
  cites:
  - source: S1
    locator: §1.1; open A note
- name: Open / scholarly Objectivist studies
  form: modern
  how_it_differs: Academic journals and societies engaging SEP-style critique
  lio_difference: Not rescored
  certainty: 0.7
  cites:
  - source: S1
    locator: §1.1
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Devoted following from novels; small relative to census religions; academic uptake limited
    certainty: 0.7
    cites:
    - source: S1
      locator: §1
    how_known: SEP. 0.7.
v7_1_rubric:
  label: authorial v7.1 scores
  L: 9
  P: 9
  E: 10
  V: 10
  X: 8
  total: 46
  scoring_note: 'Objectivism scores high for its rational, integrated approach to reality and ethics,
    promoting individualism with strong empirical ties, but slightly limited by its prescriptive economic
    views.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 19 and section 7 scoring notes'
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
  use_when: "The person avowed Objectivism or Rand's philosophy."
  do_not_use_when: Libertarian politics alone is not OBJCT.
  neighbors:
  - code: ATHE
    relation: neighbor (easily confused)
    note: A not yet scored 4
  - code: UTIL
    relation: contrast case
    note: Egoism vs utility aggregate
  - code: EXIST
    relation: neighbor (easily confused)
    note: Different metaphysics
review:
  data_quality_flags: []
  open_questions:
  - Source an explicit Objectivist denial of God for A 4?
  - Peikoff 1991 or Playboy 1964 for A?
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Neera K. Badhwar; Roderick T. Long
  year: 2020
  citation: 'Neera K. Badhwar and Roderick T. Long. "Ayn Rand." Stanford Encyclopedia of Philosophy. First
    published June 8, 2010; substantive revision July 13, 2020. https://plato.stanford.edu/entries/ayn-rand/.'
  url: 'https://plato.stanford.edu/entries/ayn-rand/'
  accessed: '2026-10-25'
  reliability_note: Peer-reviewed reference entry.
---
# Objectivism (OBJCT)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44. The v7.1 scores and note are unchanged.

## Summary

Ayn Rand’s Objectivism: man as heroic being; happiness as moral purpose; productive achievement; reason as only absolute; laissez-faire capitalism as compatible politics [S1].

## Core metaphysics

This-worldly, anti-mysticism; free will; life as end for living entities [S1]. God position still not explicit enough for A (BELOW_THRESHOLD).

## Position on the LIO axes

A BELOW_THRESHOLD (alt 4); D 4 (0.5); B/C/E UNKNOWN. Unchanged this pass.

## Schools and variants

Rand’s texts; Peikoff orthodox; open scholarly Objectivism [S1].

## Science

Allies with productive science/industry; outside mainstream academic philosophy [S1].

## Coding guidance

Avowed Objectivism / Rand’s philosophy → OBJCT. Libertarian politics alone ≠ OBJCT.

## v7.1 scoring note

Authorial v7.1 note unchanged (see front matter).

## Open questions

- Source an explicit Objectivist denial of God for A 4?
- Peikoff 1991 or Playboy 1964 for A?

## Research log

- 2026-10-15: draft from SEP Ayn Rand.
- 2026-10-25: deepened TODOs, ethics/practice/schools; axes unchanged.
- 2026-10-25: A/B/C/E scored 4 (naturalism).
