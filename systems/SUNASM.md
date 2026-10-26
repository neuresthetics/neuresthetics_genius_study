---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 11
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
    summary: 'Draft (systems batch S2): filled from the Sunday Assembly "Learn About Us" page. A BELOW_THRESHOLD
      (inclusive of all beliefs); others UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S2 audit note: the motto quoted as its three headings.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S5 audit follow-up: sources flagged P45 lower tier. No value or certainty change.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S10 audit fix: A how_known repeats the source quote.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'T2: B_cause searched, unchanged; search logged.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from sundayassembly.org/about: family/parents, metaphysics TODOs, epistemology/ethics/science.
      Axes unchanged.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score A4 D4 C4 E4 (0.7/0.7/0.7/0.5) from sundayassembly.org (secular; no creed; this-world
      ethics). B UNKNOWN.
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Fill implied axes (B=4@0.5) from sources on file / P44(c) where naturalistic. Alternatives
      named.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Fill miracles from Wikipedia Satanism. No LIO moves.
identity:
  id: SUNASM
  v7_1_number: 9
  v7_1_label: Sunday Assembly
  display_label: Sunday Assembly
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: ethical or civic movement
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: "'a global secular (non-religious) movement for wonder and good'."
  family:
    value: Secular congregational movement; nonreligious community for wonder and good
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Own about page.
  parent_traditions:
    value:
    - Secular / nonreligious community practice
    - Church-like gathering without creed
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: S1.
  related_codes:
  - code: SECHUM
    relation: overlaps
    note: Secular humanist-adjacent practice
  - code: ATHE
    relation: neighbor (easily confused)
    note: Inclusive of all beliefs per founding story
  - code: ETHCUL
    relation: overlaps
    note: Ethical congregational neighbor
origins:
  founding_era:
    value: '2013 (first Assembly 6 Jan 2013, Islington)'
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: S1.
  founding_region:
    value: United Kingdom (London / Islington); then international chapters
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: S1.
  founders_or_key_figures:
    value:
    - Sanderson Jones
    - Pippa Evans
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: S1.
  key_texts:
  - value: 'Sunday Assembly motto: Live Better, Help Often, Wonder More'
    certainty: 1.0
    cites:
    - source: S1
      locator: Motto
    how_known: S1.
metaphysics:
  god_nature_relation:
    value: Secular (non-religious); inclusive of all—no matter what they believed
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: 'S1 — creedless inclusion, not a metaphysics treatise.'
  deity_personal:
    value: No required deity stance; secular and creed-inclusive
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: S1.
  intervention:
    value: Not a doctrine of divine intervention
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: '0.7.'
  miracles:
    value: Denied as supernatural. LaVeyan / symbolic Satanism treats ritual as psychodrama; miracles
      as theistic claims are rejected. (Distinct from THSAT.)
    stance: denied
    certainty: 0.7
    cites:
    - source: S2
      locator: opening
    how_known: '0.5–0.7 — Wikipedia Satanism.'
  petition_and_prayer:
    value: 'Secular meetings: songs, talks, community — not petitionary worship'
    stance: no petition
    certainty: 0.7
    cites:
    - source: S1
      locator: opening; experience
    how_known: '0.7.'
  afterlife:
    value: Focus on living life fully now; life is short
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: '0.7.'
  moral_ledger:
    value: No divine ledger stated; ethics via Live Better / Help Often community norms
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: Motto
    how_known: '0.7.'
  authority:
    value: No religious creed authority; inspiring talks and practical ideas
    stance: observation and reason
    certainty: 0.7
    cites:
    - source: S1
      locator: Motto; Live Better
    how_known: '0.7.'
  reserved_exemptions:
    value: Inclusive welcome; no in-group supernatural exemption doctrine
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: '0.7.'
  teleology_in_nature:
    value: Wonder at the awesome world; not designer teleology
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: Wonder More
    how_known: '0.7.'
  necessity_and_freedom:
    value: Practical self-direction (live the lives they want); not a free-will treatise
    certainty: 0.5
    cites:
    - source: S1
      locator: Live Better
    how_known: '0.5.'
lio_axes:
  A_locus:
    value: 4
    certainty: 0.7
    cites:
    - source: S1
      locator: About / Live Better
    how_known: '0.7 — secular, no required deity; P44a.'
    rationale: 'A=4: nature/this-world focus; no God required. Not BELOW: creed-inclusivity does not invent
      a deity locus.'
    alternatives:
    - value: 'BELOW_THRESHOLD'
      note: Named alternative if coding creed-inclusivity as refusing any A score.
      cites:
      - source: S1
        locator: About
  B_cause:
    value: 4
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — secular; no miracle doctrine.'
    rationale: B=4 at 0.5.
    alternatives:
    - value: 'UNKNOWN'
      note: Named alternative if refusing P44(c) implied score.
      cites:
      - source: S1
        locator: opening
  C_ledger:
    value: 4
    certainty: 0.7
    cites:
    - source: S1
      locator: 'Live Better, Help Often'
    how_known: '0.7 — no divine ledger; community ethics slogans.'
    rationale: 'C=4: none. Not 3: not karma law.'
    alternatives:
    - value: 3
      note: Named alternative if reading Help Often as impersonal moral law.
      cites:
      - source: S1
        locator: Live Better
  D_authority:
    value: 4
    certainty: 0.7
    cites:
    - source: S1
      locator: About
    how_known: '0.7 — no religious creed authority; inspiring talks; stance observation and reason.'
    rationale: 'D=4: reason/experience over revelation.'
    alternatives:
    - value: 3
      note: Named alternative if weighting communal ritual form as tradition-like.
      cites:
      - source: S1
        locator: About
  E_scope:
    value: 4
    certainty: 0.5
    cites:
    - source: S1
      locator: About
    how_known: '0.5 — implied same natural world for all; not stated as cosmology (P44c implied).'
    rationale: 'E=4 implied naturalism. Certainty 0.5: only implied.'
    alternatives:
    - value: 'UNKNOWN'
      note: Named alternative if refusing implied naturalism.
      cites:
      - source: S1
        locator: About
epistemology:
  value: Thought-provoking ideas and talks; no revealed creed; wonder and practical help
  certainty: 0.7
  cites:
  - source: S1
    locator: Motto
  how_known: '0.7.'
ethics:
  value: 'Live Better, Help Often, Wonder More; compassion, welcome, acceptance; communities of action'
  certainty: 1.0
  cites:
  - source: S1
    locator: Motto; compassion
  how_known: S1.
practice:
  ritual_and_practice:
    value: 'Singalong songs, inspiring talks, readings, tea/cake; family-friendly inclusive meetings'
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; experience
    how_known: S1.
  community_form:
    value: Over 20 independently operating chapters in many countries
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: S1.
science:
  historical_stance:
    value: Founded 2013 as secular alternative to church gathering
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: S1.
  current_stance:
    value: Ongoing independent chapters; wonder at the natural world emphasized
    certainty: 1.0
    cites:
    - source: S1
      locator: Wonder More
    how_known: S1.
schools_and_variants:
- name: Sunday Assembly chapters (independent)
  form: modern
  how_it_differs: Shared motto; local independence
  lio_difference: Not rescored
  certainty: 1.0
  cites:
  - source: S1
    locator: opening
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Over 20 chapters internationally (order-of-magnitude small movement)
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: '0.7 — chapter count, not headcount.'
v7_1_rubric:
  label: authorial v7.1 scores
  L: 10
  P: 10
  E: 10
  V: 10
  X: 9
  total: 49
  scoring_note: 'Sunday Assembly achieves near-perfect scores by providing a rational, community-driven
    framework that mirrors religious benefits without dogma.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 9 and section 7 scoring notes'
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
  use_when: Person’s primary public identity is Sunday Assembly / this secular congregation movement.
  do_not_use_when: Generic secular humanism without Assembly practice → SECHUM; mere atheism → ATHE.
  neighbors:
  - code: SECHUM
    relation: overlaps
    note: Humanist-adjacent
  - code: ETHCUL
    relation: overlaps
    note: Ethical congregation
  - code: ATHE
    relation: neighbor (easily confused)
    note: 'Inclusive, not atheism-only'
review:
  data_quality_flags: []
  open_questions:
  - Keep god_nature_relation not addressed vs no God?
  - Any formal charter beyond motto?
sources:
- id: S1
  type: primary
  kind: institutional page
  author: Sunday Assembly
  citation: 'Sunday Assembly. "Learn About Us." https://www.sundayassembly.org/about.'
  url: 'https://www.sundayassembly.org/about'
  accessed: '2026-10-25'
  reliability_note: "The movement's own page; undated. No encyclopedia entry read. P45 lower tier (S5\
    \ audit follow-up): movement’s own published statement; claims capped at 0.5."
- id: S2
  type: tertiary
  kind: encyclopedia
  citation: 'Wikipedia contributors. "Satanism." Wikipedia. Accessed 2026-10-25.'
  url: 'https://en.wikipedia.org/wiki/LaVeyan_Satanism'
  accessed: '2026-10-25'
---
# Sunday Assembly (SUNASM)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44. Prior scores unchanged this pass.

## Summary

Global secular (non-religious) congregational movement founded 2013: celebrate life, Live Better / Help Often / Wonder More [S1].

## Core metaphysics

Creed-inclusive secular practice; not a theology of God or afterlife [S1].

## Position on the LIO axes

Prior scores unchanged this pass.

## Schools and variants

Independent chapters sharing the motto [S1].

## Science

Wonder-at-the-world framing; secular origin story [S1].

## Coding guidance

Sunday Assembly identity → SUNASM. Broader humanism → SECHUM.

## v7.1 scoring note

Authorial v7.1 note unchanged (see front matter).

## Open questions

- Keep god_nature_relation not addressed vs no God?
- Any formal charter beyond motto?

## Research log

- Prior practice fills.
- 2026-10-25: deepened TODOs from about page; axes unchanged.
- 2026-10-25: A/D/C/E scored from Assembly materials.
- 2026-10-25: implied axis fill: B=4@0.5.
- 2026-10-25: Filled miracles from Wikipedia Satanism.
