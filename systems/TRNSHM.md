---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 7
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
    summary: 'Draft (systems batch S2): filled from Britannica "Transhumanism" (Ostberg). A BELOW_THRESHOLD
      (materialist majority, some religious variants); others UNKNOWN. v7.1 scores and note unchanged.
      Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S10 audit fix: A how_known repeats the source quote.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities: family/parents/related codes, founding region, metaphysics TODOs, epistemology,
      ethics, practice, science, schools (extropian, WTA/Humanity+, singularity). LIO axes unchanged.
      Re-read Britannica Transhumanism (Ostberg).'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score D_authority 4 (0.7) and C_ledger 4 (0.7) from sources on file (sci/tech argument; this-world
      ethics). A stays BELOW.
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Fill implied axes (B=4@0.5, E=4@0.5) from sources on file / P44(c) where naturalistic. Alternatives
      named.'
identity:
  id: TRNSHM
  v7_1_number: 13
  v7_1_label: Transhumanism
  display_label: Transhumanism
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: ethical or civic movement
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: "'philosophical and scientific movement'; coder's classification, 0.7."
  family:
    value: Philosophical and scientific movement for technological human enhancement
    certainty: 1.0
    cites: &id003
    - source: S1
      locator: opening
    how_known: Britannica.
  parent_traditions:
    value:
    - Julian Huxley “transhumanism” (1957)
    - '1980s futurism/cryonics/nanotech advocacy'
    - Extropianism; WTA / Humanity+
    certainty: 1.0
    cites: &id001
    - &id004
      source: S1
      locator: History
    how_known: Britannica History.
  related_codes:
  - code: SCIENT
    relation: neighbor (easily confused)
    note: Scientology is a different NRM; not TRNSHM
  - code: RAEL
    relation: neighbor (easily confused)
    note: Raëlian cloning/ET frame is not generic transhumanism
  - code: BRGHTS
    relation: neighbor (easily confused)
    note: Naturalistic civic label ≠ enhancement programme
origins:
  founding_era:
    value: Term popularized 1957 (Julian Huxley); organizations from the 1980s; WTA 1998
    certainty: 1.0
    cites:
    - source: S1
      locator: History
    how_known: Britannica.
  founding_region:
    value: 'Anglophone / North Atlantic (UK, US, Canada) with international WTA/Humanity+; Silicon Valley
      patronage noted'
    certainty: 1.0
    cites: *id001
    how_known: Britannica History.
  founders_or_key_figures:
    value:
    - Julian Huxley
    - Max More
    - Nick Bostrom
    - David Pearce
    - Natasha Vita-More
    - Ray Kurzweil
    certainty: 1.0
    cites:
    - source: S1
      locator: History; Ethics and philosophy
    how_known: Britannica.
  key_texts:
  - value: 'Julian Huxley, “Transhumanism” (1957)'
    certainty: 1.0
    cites: *id001
    how_known: Britannica.
  - value: 'K. Eric Drexler, Engines of Creation (1986)'
    certainty: 1.0
    cites: *id001
    how_known: Britannica.
  - value: 'Kurzweil, The Singularity Is Near (2005)'
    certainty: 1.0
    cites: &id002
    - &id005
      source: S1
      locator: Ethics and philosophy
    how_known: Britannica.
metaphysics:
  god_nature_relation:
    value: "Varies: 'characterized as a materialist and atheist or agnostic philosophy', but 'some transhumanists\
      \ have espoused theories that resemble or even adapt New Age, Buddhist, or Christian beliefs' (e.g.\
      \ Tipler's God as a cosmic computerized intelligence)."
    stance: varies by school
    certainty: 1.0
    cites:
    - source: S1
      locator: Ethics and philosophy
    how_known: Britannica.
  deity_personal:
    value: 'Often materialist atheist/agnostic; some adapt New Age, Buddhist, Christian, or Tipler Omega/God-as-computation
      ideas'
    stance: varies by school
    certainty: 1.0
    cites: *id002
    how_known: Britannica.
  intervention:
    value: Not a shared miracle doctrine; technological intervention in human biology is the point.
    stance: not addressed
    certainty: 0.7
    cites: *id002
    how_known: 'Coder: tech enhancement ≠ divine intervention. 0.7.'
  miracles:
    value: Not a religious miracle thesis; technological transformation claims.
    stance: not addressed
    certainty: 0.7
    cites: *id003
    how_known: '0.7.'
  petition_and_prayer:
    value: Not a petitionary religion as such.
    stance: no petition
    certainty: 0.7
    cites: *id002
    how_known: Materialist/agnostic characterization. 0.7.
  afterlife:
    value: 'Some pursue cryonics, mind uploading, computational resurrection (Tipler/Kurzweil themes);
      not required of all transhumanists'
    stance: varies by school
    certainty: 0.7
    cites: *id002
    how_known: Britannica ethics section. 0.7.
  moral_ledger:
    value: 'Ethical debate centers this-world equity, rights of enhanced vs non-enhanced, eugenics analogies
      — not a divine ledger'
    stance: none
    certainty: 0.7
    cites: *id002
    how_known: Britannica. 0.7.
  authority:
    value: 'Scientific/technological argument and futurist advocacy organizations (WTA/Humanity+, institutes);
      not a single revealed scripture'
    stance: observation and reason
    certainty: 0.7
    cites: *id001
    how_known: Britannica History. 0.7.
  reserved_exemptions:
    value: Critics fear enhanced elites claiming superior rights; the movement’s stated aim is often universal
      betterment — contested
    stance: varies by school
    certainty: 0.5
    cites: *id002
    how_known: Fukuyama critique in Britannica. 0.5.
  teleology_in_nature:
    value: Humanity directed toward posthuman via tech; some borrow Omega-point style cosmic teleology
      (Tipler)
    stance: varies by school
    certainty: 0.7
    cites: *id002
    how_known: '0.7.'
  necessity_and_freedom:
    value: Kurzweil predicts machines appearing to develop free will; movement emphasizes proactive expansion
      of potential (extropy vs entropy)
    certainty: 0.7
    cites: *id002
    how_known: Britannica. 0.7.
lio_axes:
  A_locus:
    value: 'BELOW_THRESHOLD'
    how_known: "Members differ (P44b): materialist, atheist or agnostic for most, with New Age, Buddhist\
      \ and Christian adaptations (S1). Quote (S1, Ethics and philosophy): Varies: 'characterized as a\
      \ materialist and atheist or agnostic philosophy', but 'some transhumanists have espoused theories\
      \ that resemble or even adapt New Age, Buddhist, or Christian beliefs' (e.g. Tipler's God as a cosmic\
      \ computerized intelligence)."
    note: 'Evidence: S1, Ethics and philosophy. Alternative: 4 for the materialist majority.'
  B_cause:
    value: 4
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — sci/tech; no miracle doctrine as default.'
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
      locator: opening
    how_known: '0.7 — this-world equity/enhancement debates; not a divine ledger.'
    rationale: 'C=4: none. Not 3: cryonics/upload are tech hopes, not karma.'
    alternatives:
    - value: 'BELOW_THRESHOLD'
      note: Named alternative if coding Omega Point / God-as-computation streams as ledger.
      cites:
      - source: S1
        locator: opening
  D_authority:
    value: 4
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: '0.7 — scientific/technological argument; stance observation and reason.'
    rationale: 'D=4: science/tech over revelation as family method. Not 3: New Age/religious adaptations
      are schools, not default.'
    alternatives:
    - value: 3
      note: Named alternative if coding Tipler/religious transhumanism as primary.
      cites:
      - source: S1
        locator: opening
  E_scope:
    value: 4
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — materialist default; same natural order.'
    rationale: E=4 at 0.5.
    alternatives:
    - value: 'UNKNOWN'
      note: Named alternative if refusing P44(c) implied score.
      cites:
      - source: S1
        locator: opening
epistemology:
  value: Futurism from scientific trends; advocacy for responsible application of emerging tech; internal
    ethical debate as tech becomes actual
  certainty: 1.0
  cites:
  - *id004
  - *id005
  how_known: Britannica.
ethics:
  value: 'Central tension: eliminate disease/improve life vs risks of inequity, eugenics-like exploitation,
    and “frightful moral cost” to human rights (Fukuyama in Britannica)'
  certainty: 1.0
  cites: *id002
  how_known: Britannica Ethics and philosophy.
practice:
  ritual_and_practice:
    value: 'Research advocacy, cryonics, enhancement tech interest, space colonization talk — not a church
      liturgy'
    certainty: 1.0
    cites: *id001
    how_known: Britannica History.
  community_form:
    value: 'Organizations (Extropy Institute, WTA/Humanity+), institutes, Silicon Valley–linked projects'
    certainty: 1.0
    cites: *id001
    how_known: Britannica.
science:
  historical_stance:
    value: 'Coalesced around computing, space travel, cryopreservation, nanotech; heyday of orgs in 1980s–90s'
    certainty: 1.0
    cites: *id001
    how_known: Britannica.
  current_stance:
    value: 'Engages present biotech/AI/neurotech; ethics moved from future to present as stem cells, IVF,
      brain chips, AI arrived'
    certainty: 1.0
    cites: *id002
    how_known: Britannica.
schools_and_variants:
- name: Extropianism
  form: modern
  how_it_differs: Libertarian overcoming of limits; extropy vs entropy (More/Bell)
  lio_difference: May move D/E — not rescored
  certainty: 1.0
  cites: *id001
- name: WTA / Humanity+
  form: modern
  how_it_differs: Academic/international framing; safe ethical tech use
  lio_difference: Not rescored
  certainty: 1.0
  cites: *id001
- name: Singularity / Kurzweil line
  form: modern
  how_it_differs: Human–AI merge; disease/aging/death resolved by ~2045 prediction
  lio_difference: May move afterlife/teleology readings
  certainty: 1.0
  cites: *id002
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: 'Movement/organizations, not a census religion; Silicon Valley patronage noted'
    certainty: 0.7
    cites: *id001
    how_known: Britannica; no world membership count. 0.7.
v7_1_rubric:
  label: authorial v7.1 scores
  L: 10
  P: 10
  E: 9
  V: 10
  X: 8
  total: 47
  scoring_note: 'Transhumanism scores high for its rational, tech-driven optimism, bridging current science
    with future potential.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 13 and section 7 scoring notes'
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
  use_when: "The person's own writing advocates technological transcendence of human limits (posthuman)\
    \ as their main worldview."
  do_not_use_when: Enthusiasm for technology or life extension alone is not TRNSHM; TRNSHM sets no A value.
  neighbors:
  - code: RAEL
    relation: neighbor (easily confused)
    note: Raëlian religion ≠ generic TRNSHM
  - code: SCIENT
    relation: neighbor (easily confused)
    note: Different NRM
review:
  data_quality_flags: []
  open_questions:
  - Should Kurzweilian singularity spiritualism tip some persons to a different code?
  - 'LIO: keep UNKNOWN/prior scores — tech immortality ≠ classical afterlife axis without care.'
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: René Ostberg
  citation: 'Ostberg, René. "Transhumanism." Encyclopaedia Britannica. https://www.britannica.com/topic/transhumanism.'
  url: 'https://www.britannica.com/topic/transhumanism'
  accessed: '2026-10-25'
  reliability_note: Signed article by a Britannica associate editor. Article text only; AI-generated Top
    Questions ignored. SEP has no entry (404).
---
# Transhumanism (TRNSHM)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1). The v7.1 scores and note are unchanged.

## Summary

Transhumanism is a philosophical and scientific movement that advocates using current and emerging technologies (genetic engineering, cryonics, AI, nanotechnology) to augment human capabilities and improve the human condition, aiming toward a “posthuman” species [S1]. Term popularized by Julian Huxley (1957); organizations from the 1980s; WTA 1998 / Humanity+ 2008 [S1].

## Core metaphysics

Often materialist atheist/agnostic, but some adapt New Age, Buddhist, Christian, or Tipler-style cosmic computation ideas [S1]. Cryonics, mind uploading, and singularity talk supply afterlife-like hopes for some strands — not required of all.

## Position on the LIO axes

Axes left as previously coded (see front matter); this pass fills qualities without rescoring.

## Schools and variants

Extropianism; WTA/Humanity+; Kurzweil singularity line [S1].

## Science

From futurist anticipation to present biotech/AI/neurotech ethics [S1].

## Coding guidance

Technological enhancement movement. Raëlian religion → RAEL; Scientology → SCIENT.

## v7.1 scoring note

Authorial v7.1 note unchanged (see front matter).

## Open questions

- Should Kurzweilian singularity spiritualism tip some persons to a different code?
- LIO: tech immortality ≠ classical afterlife axis without care.

## Research log

- Prior fill from Britannica.
- 2026-10-25: deepened TODOs; re-read Britannica Transhumanism (Ostberg).
- 2026-10-25: D/C scored.
- 2026-10-25: implied axis fill: B=4@0.5, E=4@0.5.
