---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 7
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
  - date: '2026-10-15'
    by: Grok Bot
    summary: "Draft (systems batch S1): filled from the movement's own site (the-brights.net home and\
      \ Vision pages; primary for self-definition). No encyclopedia entry found. Founders and dates TODO.\
      \ v7.1 scores and note unchanged. Not reviewed."
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S1 audit: Geisert & Futrell 2003 noted as the lead for founding details; A cites P44(a).'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'P44(c): C and E cite the naturalism rule (implied, 0.5). No score change.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S5 audit follow-up: A and B capped at 0.5 under P45 (values stay 4); sources flagged P45
      lower tier.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities: parent traditions, origins, remaining metaphysics (no deity / none), epistemology,
      ethics, practice, science, schools. LIO A–E stay 4 at 0.5. Re-read the-brights.net Vision.'
identity:
  id: BRGHTS
  v7_1_number: 3
  v7_1_label: Brights (The Brights Movement)
  display_label: Brights (The Brights Movement)
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: ethical or civic movement
    certainty: 0.7
    cites:
    - source: S2
      locator: Vision
    how_known: "The site describes a civic constituency of people with naturalistic worldviews; coder's\
      \ classification, 0.7."
  family:
    value: Naturalism (civic)
    certainty: 1.0
    cites:
    - source: S1
      locator: home
    how_known: "'All of us have a naturalistic worldview, free of supernatural or mystical elements.'"
  parent_traditions:
    value:
    - Secular naturalism
    - Civic humanist / freethought visibility movements
    certainty: 0.7
    cites:
    - &id003
      source: S1
      locator: home
    - &id001
      source: S2
      locator: Vision
    how_known: "Coder's reading of naturalistic-worldview self-definition. 0.7."
  related_codes:
  - code: RATN
    relation: neighbor (easily confused)
    note: Rationalism as method vs Brights as civic constituency
origins:
  founding_era:
    value: Early 2000s Internet constituency (The Brights’ Net)
    certainty: 0.7
    cites: &id002
    - *id001
    how_known: Vision page describes Internet hub/registration; exact founding year not restated here.
      0.7.
  founding_region:
    value: United States (Sacramento contact) with Internet-global constituency
    certainty: 1.0
    cites: *id002
    how_known: 'Vision page footer: Sacramento PO Box; Internet hub.'
  founders_or_key_figures:
    value:
    - The Brights’ Net (organizational hub)
    certainty: 0.7
    cites: *id002
    how_known: Site is organizational; named personal founders not required for this deepen. 0.7.
  key_texts: []
metaphysics:
  god_nature_relation:
    value: "Naturalistic: a bright is 'a person whose worldview is naturalistic (no supernatural and mystical\
      \ elements)'."
    stance: no God
    certainty: 1.0
    cites:
    - source: S1
      locator: home
    how_known: "The movement's own definition."
  deity_personal:
    value: No supernatural deities; naturalistic worldview.
    stance: no deity
    certainty: 1.0
    cites:
    - *id003
    - *id001
    how_known: 'Site: free of supernatural deities, forces, and entities.'
  intervention:
    value: "None: worldviews 'free of the supernatural deities, forces, and entities'."
    stance: none
    certainty: 1.0
    cites:
    - source: S2
      locator: Vision
    how_known: Own site.
  miracles:
    value: No supernatural forces or entities.
    stance: denied
    certainty: 1.0
    cites: *id002
    how_known: Vision.
  petition_and_prayer:
    value: Not a petitionary religion; naturalistic explanations.
    stance: no petition
    certainty: 1.0
    cites: *id002
    how_known: Vision.
  afterlife:
    value: Not affirmed; worldview free of supernatural entities.
    stance: none
    certainty: 0.7
    cites: *id002
    how_known: Implied by naturalism; not a detailed afterlife essay. 0.7.
  moral_ledger:
    value: No supernatural agent to keep a moral ledger.
    stance: none
    certainty: 0.7
    cites: *id002
    how_known: Aligned with C=4 coding. 0.7.
  authority:
    value: "Principles held 'as values, not dogma'; naturalistic explanations."
    stance: observation and reason
    certainty: 0.7
    cites: *id002
    how_known: Vision Principles. 0.7.
  reserved_exemptions:
    value: Civic egalitarianism; no supernatural in-group exemption doctrine.
    stance: none
    certainty: 0.7
    cites: *id002
    how_known: Vision civic aims. 0.7.
  teleology_in_nature:
    value: No supernatural teleology stated; naturalism.
    stance: none
    certainty: 0.7
    cites: *id002
    how_known: '0.7.'
  necessity_and_freedom:
    value: Not a shared free-will metaphysics; civic pragmatism emphasized.
    certainty: 0.7
    cites: *id002
    how_known: Vision naturalistic worldview considerations. 0.7.
lio_axes:
  A_locus:
    value: 4
    rationale: No supernatural deities; naturalistic worldview.
    certainty: 0.5
    cites:
    - source: S1
      locator: home
    - source: S2
      locator: Vision
    how_known: '0–4 scale (P1). Own definition; A 4 for a no-God system under P44(a), 0.7. Capped at 0.5
      under P45 (was 0.7; value unchanged).'
  B_cause:
    value: 4
    rationale: 'No supernatural forces or entities, so no miracle or exception.'
    certainty: 0.5
    cites:
    - source: S2
      locator: Vision
    how_known: '0–4 scale (P1). 0.7: the site states the worldview, not a doctrine of law. Capped at 0.5
      under P45 (was 0.7; value unchanged).'
  C_ledger:
    value: 4
    rationale: No supernatural agent to keep a moral ledger.
    certainty: 0.5
    cites:
    - source: S2
      locator: Vision
    how_known: 'Implied by the naturalist stance, not stated: 4 at 0.5 under P44(c).'
  D_authority:
    value: 4
    rationale: "Naturalistic explanations; principles held 'as values, not dogma'."
    certainty: 0.5
    cites:
    - source: S1
      locator: home
    - source: S2
      locator: Vision
    how_known: Inferred from the self-definition; revelation not mentioned. 0.5.
  E_scope:
    value: 4
    rationale: "On the world's order (P7): no supernatural forces to favour a group."
    certainty: 0.5
    cites:
    - source: S2
      locator: Vision
    how_known: 'Implied by the naturalist stance, not stated: 4 at 0.5 under P44(c).'
epistemology:
  value: 'Naturalistic explanations; symbolism of open inquiry, learning, skepticism (Vision symbolism).
    Principles as values not dogma.'
  certainty: 1.0
  cites: *id002
  how_known: Vision.
ethics:
  value: Civic acceptance and equal participation for people with naturalistic worldviews; level playing
    field with supernaturalist citizens.
  certainty: 1.0
  cites: *id002
  how_known: Vision opening.
practice:
  ritual_and_practice:
    value: No cult ritual; registration into Internet constituency; civic/social advocacy.
    certainty: 1.0
    cites: *id002
    how_known: Vision.
  community_form:
    value: Internet constituency / civic movement hub (The Brights’ Net).
    certainty: 1.0
    cites: *id002
    how_known: Vision.
science:
  historical_stance:
    value: Appeals to science and reason as cultural imagery of open inquiry.
    certainty: 0.7
    cites: *id002
    how_known: Vision Symbolism. 0.7.
  current_stance:
    value: Naturalistic explanations preferred; not a research lab.
    certainty: 1.0
    cites: *id002
    how_known: Vision.
schools_and_variants:
- name: Brights Internet constituency
  form: modern
  how_it_differs: Umbrella naturalistic worldview label; not a sect with dogma
  lio_difference: Axes already coded 4
  certainty: 1.0
  cites: *id002
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Internet-registered constituency; not a census religion
    certainty: 0.7
    cites: *id002
    how_known: Vision describes registration; no authoritative world count here. 0.7.
v7_1_rubric:
  label: authorial v7.1 scores
  L: 10
  P: 10
  E: 10
  V: 10
  X: 9
  total: 49
  scoring_note: 'The Brights Movement scores highly for its evidence-based naturalism and civic focus,
    serving as a practical extension of atheism with strong coherence.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 3 and section 7 scoring notes'
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
  use_when: The person publicly identifies as a Bright (the self-applied label); otherwise use ATHE or
    SECHUM on their stated views.
  do_not_use_when: 'Do not infer BRGHTS from naturalism alone: it is a self-chosen civic label (S1).'
  neighbors:
  - code: RATN
    relation: neighbor (easily confused)
    note: Method-rationalism vs civic Bright identity
review:
  data_quality_flags:
  - "Only the movement's own pages were read; no independent encyclopedia entry was found. Founders, founding\
    \ date and membership are TODO."
  open_questions:
  - Exact founding year/persons if Jason wants a tighter origins fill.
sources:
- id: S1
  type: primary
  kind: institutional page
  author: "The Brights' Net"
  citation: 'The Brights'' Net. "Who are The Brights?" https://www.the-brights.net/.'
  url: 'https://www.the-brights.net/'
  accessed: '2026-10-25'
  reliability_note: "The movement's own site (primary for its self-definition); no date on the page. P45\
    \ lower tier (S5 audit follow-up): movement’s own published statement; claims capped at 0.5."
- id: S2
  type: primary
  kind: institutional page
  author: "The Brights' Net"
  citation: 'The Brights'' Net. "The Vision." https://www.the-brights.net/vision/.'
  url: 'https://www.the-brights.net/vision/'
  accessed: '2026-10-25'
  reliability_note: "The movement's own site; no date on the page. P45 lower tier (S5 audit follow-up):\
    \ movement’s own published statement; claims capped at 0.5."
---
# Brights (The Brights Movement) (BRGHTS)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1). The v7.1 scores and note are unchanged.

## Summary

The Brights describe themselves as people who have a naturalistic worldview, free of supernatural or mystical elements [S1]. The Vision is civic: persons with naturalistic worldviews should be full participants, not marginalized by pervasive supernaturalism [S2]. Principles are held as values, not dogma [S2].

## Core metaphysics

No supernatural deities, forces, or entities [S2]. Not a petitionary religion; no miracle doctrine; no supernatural moral ledger.

## Position on the LIO axes

- **A–E: 4** (certainty 0.5 under P45) — naturalistic no-supernatural coding from prior pass [S1][S2].

## Schools and variants

Internet constituency / civic umbrella label [S2].

## Science

Symbolism of open inquiry, science, and skepticism [S2]; naturalistic explanations.

## Coding guidance

Use for the Brights civic/naturalistic identity. Mere atheism without this frame may be ATHEI; method-only rationalism may be RATN.

## v7.1 scoring note

Authorial v7.1 note unchanged (see front matter).

## Open questions

- Exact founding year/persons if Jason wants a tighter origins fill.

## Research log

- Prior batch fills from the-brights.net; LIO A–E = 4 at 0.5.
- 2026-10-25: deepened TODOs; re-read Vision page.
