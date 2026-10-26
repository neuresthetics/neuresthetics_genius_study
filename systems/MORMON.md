---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 6
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
    summary: 'Draft (systems batch S11): filled from Britannica "Church of Jesus Christ of Latter-day
      Saints" (Melton), introduction and Scriptures pages. A 1 (0.5, alt 0); C 1 (0.5, alt 0); D 1 (0.5,
      alt 0); B, E UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S11 audit fix: title corrected to Doctrine and Covenants.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'T1: B_cause searched, still UNKNOWN; search logged.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from Britannica LDS (Melton): Smith 1830, Book of Mormon, Godhead, continuing
      revelation, temple/missionary practice, Community of Christ neighbor. Keep A=1 C=1 D=1; B E UNKNOWN.'
identity:
  id: MORMON
  v7_1_number: 71
  v7_1_label: Mormonism (The Church of Jesus Christ of Latter-day Saints)
  display_label: Mormonism (The Church of Jesus Christ of Latter-day Saints)
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: religion
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: 'Britannica: church founded 1830.'
  family:
    value: 'Church of Jesus Christ of Latter-day Saints (LDS / Mormonism): restorationist Christian movement;
      Book of Mormon; continuing revelation; unique Godhead'
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  parent_traditions:
    value:
    - 19th-century American Christian revivalism
    - Claimed restoration of primitive Christian church
    - Israelite-in-America narrative (Book of Mormon)
    certainty: 1.0
    cites:
    - source: S1
      locator: history; opening
    how_known: Britannica.
  related_codes:
  - code: CHRIST
    relation: offshoot
    note: restorationist; diverges on Godhead and scripture
  - code: RAEL
    relation: neighbor (easily confused)
    note: both cite Smith among prophets — different cosmologies
origins:
  founding_era:
    value: 1830 (church founded; Book of Mormon published), western New York
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; history
    how_known: Britannica.
  founding_region:
    value: United States (NY → Ohio/Missouri/Illinois → Utah); HQ Salt Lake City
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; history
    how_known: Britannica.
  founders_or_key_figures:
    value:
    - Joseph Smith
    - Brigham Young
    - Wilford Woodruff (1890 Manifesto)
    - 'Community of Christ line: Joseph Smith III'
    certainty: 1.0
    cites:
    - source: S1
      locator: history
    how_known: Britannica.
  key_texts:
  - value: Book of Mormon (1830)
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; Book of Mormon FAQ
    how_known: Britannica.
  - value: Bible (as scripture alongside Book of Mormon)
    certainty: 1.0
    cites:
    - source: S1
      locator: Book of Mormon FAQ
    how_known: Britannica.
  - value: Doctrine and Covenants (related Britannica topic)
    certainty: 0.7
    cites:
    - source: S1
      locator: related topics
    how_known: Named related.
metaphysics:
  god_nature_relation:
    value: Godhead of distinct beings (God, Jesus Christ, Holy Spirit); not classical Trinity. Faithful
      may attain God's fullness and become gods.
    stance: creator distinct from creation
    certainty: 0.5
    cites:
    - source: S1
      locator: beliefs FAQ; opening
    how_known: 0.5 — distinct beings; exaltation complicates classical creator/creature.
  deity_personal:
    value: Personal Godhead; continuing revelation; Christ for salvation and resurrection.
    stance: personal
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; beliefs
    how_known: Britannica.
  intervention:
    value: Continuing revelation; angel Moroni; day-to-day guidance revelations in early church; Second
      Coming/millennial kingdom.
    stance: regular
    certainty: 0.7
    cites:
    - source: S1
      locator: opening; history
    how_known: Britannica.
  miracles:
    value: Visionary and revelatory events central to founding narrative.
    stance: affirmed
    certainty: 0.5
    cites:
    - source: S1
      locator: history
    how_known: 0.5 — stance enum may need check.
  petition_and_prayer:
    value: Prayer and ordinances (baptism, Holy Spirit); proxy baptism for dead.
    stance: petition answered
    certainty: 0.7
    cites:
    - source: S1
      locator: practices FAQ
    how_known: Britannica.
  afterlife:
    value: All receive some glory; exaltation/become gods for faithful; resurrection; millennial kingdom;
      Earth becomes celestial sphere for righteous.
    stance: personal afterlife
    certainty: 1.0
    cites:
    - source: S1
      locator: beliefs FAQ
    how_known: Britannica.
  moral_ledger:
    value: Futures determined by own actions and grace of God; ordinances essential.
    stance: personal reward and punishment
    certainty: 0.7
    cites:
    - source: S1
      locator: opening; beliefs
    how_known: Britannica — C=1 kept.
  authority:
    value: Living prophets/presidents; continuing revelation; respect for authority; Council of Twelve
      / church presidency.
    stance: revelation
    certainty: 0.7
    cites:
    - source: S1
      locator: opening; history
    how_known: Britannica — D=1 kept.
  reserved_exemptions:
    value: Not addressed as formal exemptions category.
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: Silence.
  teleology_in_nature:
    value: Millennial/teleological history toward Zion and Second Coming more than nature design.
    stance: designer's purposes
    certainty: 0.5
    cites:
    - source: S1
      locator: history
    how_known: 0.5.
  necessity_and_freedom:
    value: Actions and grace determine futures — agency emphasized in popular teaching; not fixed in S1
      as free-will theory.
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: Thin.
lio_axes:
  A_locus:
    value: 1
    rationale: Father, Son and Holy Spirit, 'These three beings—the Godhead—are considered to be distinct
      entities (a doctrine known as tritheism)'; 'faithful members of the church may receive God’s fullness
      and thus become gods themselves'.
    certainty: 0.5
    cites: &id001
    - source: S2
      locator: Scriptures
    how_known: '0.5: personal divine beings; their place in nature is not stated. Alternative 0.'
    alternatives:
    - value: 0
      note: Named alternative.
      cites: *id001
  B_cause:
    value: UNKNOWN
    how_known: Not fixed by the sources read (T1 search logged, 2026-10-15).
  C_ledger:
    value: 1
    rationale: '''people’s futures are determined by their own actions as well as by the grace of God'';
      afterlife kingdoms (celestial, terrestrial, ''telestial'') and ''some degree of glory'' for nearly
      all.'
    certainty: 0.5
    cites: &id002
    - source: S2
      locator: Scriptures
    how_known: '0.5: reward by God with graded glory. Alternative 0.'
    alternatives:
    - value: 0
      note: Named alternative.
      cites: *id002
  D_authority:
    value: 1
    rationale: '''belief in continuing revelation''; church presidents are ''regarded as prophets'', and
      their revelations are added to the Doctrine and Covenants.'
    certainty: 0.5
    cites: &id003
    - source: S1
      locator: introduction
    - source: S2
      locator: Scriptures
    how_known: '0.5: the source does not set revelation against observation. Alternative 0.'
    alternatives:
    - value: 0
      note: Named alternative.
      cites: *id003
  E_scope:
    value: UNKNOWN
    how_known: Not addressed in the sources read.
epistemology:
  value: Continuing revelation through prophets; restored church; scripture (Bible + Book of Mormon +
    other).
  certainty: 1.0
  cites:
  - source: S1
    locator: opening
  how_known: Britannica.
ethics:
  value: Family emphasis; Word of Wisdom prohibitions (alcohol, tobacco, coffee, tea); education; work
    ethic; faith, repentance, ordinances.
  certainty: 1.0
  cites:
  - source: S1
    locator: opening; practices
  how_known: Britannica.
practice:
  ritual_and_practice:
    value: Baptism (age 8+), priesthood offices, missionary service, temple work including proxy baptism;
      Word of Wisdom.
    certainty: 1.0
    cites:
    - source: S1
      locator: practices FAQ
    how_known: Britannica.
  community_form:
    value: Hierarchical church HQ Salt Lake City; wards/stakes; Community of Christ separate denomination
      (Independence, MO).
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; history
    how_known: Britannica.
science:
  historical_stance:
    value: Promotes education; Book of Mormon historical claims contested outside the church — not a science
      program.
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: 0.5 coder.
  current_stance:
    value: Not fixed in S1.
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: Silence.
schools_and_variants:
- name: Church of Jesus Christ of Latter-day Saints (Salt Lake)
  form: modern
  how_it_differs: Mainstream; abandoned polygamy (1890 Manifesto).
  lio_difference: A=1 C=1 D=1 kept.
  certainty: 1.0
  cites:
  - source: S1
    locator: opening; history
- name: Community of Christ (former RLDS)
  form: reform
  how_it_differs: Rejected Young; Independence HQ; ~250k.
  lio_difference: May differ — not rescored.
  certainty: 1.0
  cites:
  - source: S1
    locator: opening; history
- name: Polygamy-practicing factions
  form: other
  how_it_differs: Rejected mainstream abandonment of plural marriage.
  lio_difference: Do not assume same scores.
  certainty: 1.0
  cites:
  - source: S1
    locator: history
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: TODO
v7_1_rubric:
  label: authorial v7.1 scores
  L: 7
  P: 6
  E: 3
  V: 3
  X: 2
  total: 21
  scoring_note: Mormonism scores moderately low due to its heavy reliance on unique revelations and scriptures
    over empirical evidence, though it provides strong community and family-oriented coherence.
  source: v7.1 data book, section 6 table (tables[4]) row 71 and section 7 scoring notes
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
  use_when: LDS / Mormon / Community of Christ identity (note denomination).
  do_not_use_when: Generic Protestant/Christian without restorationist/LDS identity.
  neighbors:
  - code: CHRIST
    relation: neighbor (easily confused)
  - code: RAEL
    relation: neighbor (easily confused)
review:
  data_quality_flags:
  - v7.1 table 4 label is truncated; v7_1_label is taken from the section 7 scoring note.
  open_questions:
  - Community of Christ differs on some revelations (S2); not split.
  - 'Adherents: Britannica says more than 16 million (early 21st century); cite a demographic source.'
  - 'T1 (2026-10-15): B_cause search logged in the research log; still UNKNOWN.'
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: J. Gordon Melton
  citation: 'Melton, J. Gordon. "Church of Jesus Christ of Latter-day Saints." Encyclopaedia Britannica.
    https://www.britannica.com/topic/Church-of-Jesus-Christ-of-Latter-day-Saints. Wayback Machine snapshot
    2026-10-09 23:47:53 UTC: https://web.archive.org/web/20261009234753/https://www.britannica.com/topic/Church-of-Jesus-Christ-of-Latter-day-Saints.'
  url: https://www.britannica.com/topic/Church-of-Jesus-Christ-of-Latter-day-Saints
  accessed: '2026-10-25'
  reliability_note: 'Signed article; introduction and history read. P44(e): read in the Wayback copy (https://web.archive.org/web/20261009234753/https://www.britannica.com/topic/Church-of-Jesus-Christ-of-Latter-day-Saints);
    live page not compared (live Britannica times out from the box).'
- id: S2
  type: tertiary
  kind: encyclopedia
  author: J. Gordon Melton
  citation: 'Melton, J. Gordon. "Church of Jesus Christ of Latter-day Saints: Scriptures." Encyclopaedia
    Britannica. https://www.britannica.com/topic/Church-of-Jesus-Christ-of-Latter-day-Saints/Scriptures.
    Wayback Machine snapshot 2026-10-09 23:47:52 UTC: https://web.archive.org/web/20261009234752/https://www.britannica.com/topic/Church-of-Jesus-Christ-of-Latter-day-Saints/Scriptures.'
  url: https://www.britannica.com/topic/Church-of-Jesus-Christ-of-Latter-day-Saints/Scriptures
  accessed: '2026-10-15'
  reliability_note: 'Later page of the same signed article (scriptures and doctrines). P44(e): read in
    the Wayback copy (https://web.archive.org/web/20261009234752/https://www.britannica.com/topic/Church-of-Jesus-Christ-of-Latter-day-Saints/Scriptures);
    live page not compared (live Britannica times out from the box).'
---
# Church of Jesus Christ of Latter-day Saints / Mormonism (MORMON)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

LDS church founded by Joseph Smith (1830): Book of Mormon, restored church, continuing revelation, distinct Godhead, family and missionary emphasis; Salt Lake HQ [S1].

## Core metaphysics

Personal Godhead of distinct beings; exaltation; millennial Second Coming; actions plus grace [S1].

## Position on the LIO axes

- **A: 1, C: 1, D: 1** kept.
- **B, E:** UNKNOWN.

## Schools and variants

Salt Lake LDS; Community of Christ; polygamy factions [S1].

## Science

Education valued; not a science program [S1].

## Coding guidance

LDS/Mormon identity; note denomination.

## v7.1 scoring note

> MORMON (21/50) — Mormonism (The Church of Jesus Christ of Latter-day Saints). Mormonism scores moderately low due to its heavy reliance on unique revelations and scriptures over empirical evidence, though it provides strong community and family-oriented coherence.

## Open questions

- Whether Community of Christ needs separate scoring later.

## Research log

- Prior: A C D scored.
- 2026-10-25: deepened from Britannica LDS (Melton). Axes kept.
