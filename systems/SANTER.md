---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 7
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
    summary: "Decision P7: E_scope note added. E is not scored in a stub; when it is, score it on the\
      \ world's order (same rules for every kind of being and event, no in-group exceptions in this-world\
      \ events). Salvation and moral community go on C_ledger."
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'Draft (systems batch S9): filled from Britannica "Santería" (Murphy). B 1 (0.5, alt 0);
      D 1 (0.5); E 1 (0.5, alt 0); A, C UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from Britannica Santería (Murphy): Yoruba/Cuba, orishas–saints correspondence,
      Ifá, initiation, bembé mediumship. Keep B=1 D=1 E=1; A C UNKNOWN.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Fill adherents/estimate gloss from existing sources (order-of-magnitude / qualitative). Axes
      unchanged.
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score A_locus 0 (0.7) and C_ledger 1 (0.5) from sources on file (orishas personal; ritual
      reciprocity). B/D/E already scored.
  - date: '2026-10-25'
    by: Grok Bot
    summary: Fill reserved_exemptions from Wikipedia Santería. No LIO moves.
identity:
  id: SANTER
  v7_1_number: 56
  v7_1_label: Santería (Lucumí/Regla de Ocha)
  display_label: Santería (Lucumí/Regla de Ocha)
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: religion
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: 'Britannica: religious tradition of African origin developed in Cuba.'
  family:
    value: 'Santería / Lucumí / Regla de Ocha: Yoruba-origin orisha religion developed in Cuba; correspondences
      with Catholic saints'
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  parent_traditions:
    value:
    - Yoruba orisha religion (West Africa)
    - Roman Catholic piety in colonial Cuba (saint correspondences)
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  related_codes:
  - code: VODUN
    relation: neighbor (easily confused)
    note: Haitian Vodou also African-diaspora orisha-related but distinct
  - code: CHRIST
    relation: overlaps
    note: saint correspondences; not reducible to Catholicism
  - code: ANIM
    relation: neighbor (easily confused)
    note: 'orishas are specific deities, not generic animism'
origins:
  founding_era:
    value: Developed in Cuba among enslaved Yoruba in the first decades of the 19th century; spread after
      1959 Cuban Revolution
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; diaspora
    how_known: Britannica.
  founding_region:
    value: 'Cuba; spread throughout Latin America and the United States (esp. Miami, New York)'
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; diaspora
    how_known: Britannica.
  founders_or_key_figures:
    value:
    - Yoruba nations in Cuba (collective)
    - babalawo priesthood
    - Lydia Cabrera (key scholar/person per Britannica)
    certainty: 0.7
    cites:
    - source: S1
      locator: opening; key people
    how_known: No single founder; Cabrera listed as key person.
  key_texts:
  - value: Ifá oracle corpus / oral and priestly knowledge (not a single public scripture in Britannica
      summary)
    certainty: 0.7
    cites:
    - source: S1
      locator: divination
    how_known: Ifá described; no single named book.
metaphysics:
  god_nature_relation:
    value: 'Orishas: personified natural forces, deified ancestors, or primordial divinities; relationships
      via sacrifice and mediumship. High God not detailed in this article.'
    stance: many gods within nature
    certainty: 0.7
    cites:
    - source: S1
      locator: orishas; opening
    how_known: Britannica orisha description.
  deity_personal:
    value: 'Orishas are personal deities who claim devotees as children, heal, and prophesy through mediums.'
    stance: personal
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; bembés
    how_known: Britannica.
  intervention:
    value: 'Orishas guide in crisis, protect, heal, prophesy through mediums at bembés; regular ceremonial
      exchange.'
    stance: regular
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; rituals
    how_known: Britannica.
  miracles:
    value: Healing and prophecy through orisha mediums; not denied.
    stance: affirmed
    certainty: 0.7
    cites:
    - source: S1
      locator: bembés
    how_known: Britannica.
  petition_and_prayer:
    value: Ifá consultation and prescribed sacrifice; offerings at home altars and feasts.
    stance: petition answered
    certainty: 1.0
    cites:
    - source: S1
      locator: Ifá
    how_known: Britannica.
  afterlife:
    value: Not detailed in this Britannica article (ori / indwelling spirit mentioned in related orisha
      material).
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Silence in main article.
  moral_ledger:
    value: Not a clear afterlife ledger; oracle and sacrifice structure practical obligations.
    stance: none
    certainty: 0.5
    cites:
    - source: S1
      locator: Ifá
    how_known: '0.5.'
  authority:
    value: Ifá oracle via babalawo; initiation into orisha mysteries; orisha speech through mediums.
    stance: 'both, revelation first'
    certainty: 0.7
    cites:
    - source: S1
      locator: Ifá; initiation
    how_known: Divination/initiation as revelation-like authority.
  reserved_exemptions:
    value: 'Initiatory priesthood (santeros/santeras, babalawos) holds ritual knowledge; clients still
      under orisha reciprocity and taboos — not a moral free pass.'
    stance: some
    certainty: 0.5
    cites:
    - source: S2
      locator: opening
    how_known: '0.5–0.7 — Wikipedia Santería.'
  teleology_in_nature:
    value: Orishas as personified natural forces — immanent sacred powers.
    stance: immanent ends
    certainty: 0.5
    cites:
    - source: S1
      locator: orishas
    how_known: '0.5.'
  necessity_and_freedom:
    value: ori-inu as indwelling spirit determining character and fate (related Britannica orisha material);
      free will not developed here.
    certainty: 0.5
    cites:
    - source: S1
      locator: orishas FAQ
    how_known: Thin; 0.5.
lio_axes:
  A_locus:
    value: 0
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: '0.7 — orishas as personal deities; Olodumare high God frame in related Yoruba streams.'
    rationale: 'A=0: personal gods. Not 2: not pantheism.'
    alternatives:
    - value: 1
      note: Named alternative if weighting high God distantism.
      cites:
      - source: S1
        locator: opening
  B_cause:
    value: 1
    rationale: "'Through the bodies of their mediums the orishas are believed to interact with the congregation\
      \ directly and heal and prophesy'."
    certainty: 0.5
    cites: &id001
    - source: S1
      locator: article
    how_known: '0.5. Alternative 0.'
    alternatives:
    - value: 0
      note: Named alternative.
      cites: *id001
  C_ledger:
    value: 1
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — ritual reciprocity with orishas; not fully mapped ledger in source.'
    rationale: 'C=1 at 0.5: personal spiritual reciprocity. Alternative UNKNOWN.'
    alternatives:
    - value: 'UNKNOWN'
      note: Named alternative if evidence too thin.
      cites:
      - source: S1
        locator: opening
  D_authority:
    value: 1
    rationale: "In the Ifá oracle a priest 'interprets the fall of consecrated palm nuts to reveal the\
      \ orishas’ response'."
    certainty: 0.5
    cites:
    - source: S1
      locator: article
    how_known: '0.5: divination as revelation.'
  E_scope:
    value: 1
    rationale: "On the world's order (P7): orishas 'provide their devotees with protection, wisdom, and\
      \ success'."
    certainty: 0.5
    cites: &id002
    - source: S1
      locator: article
    how_known: '0.5: favour to devotees. Alternative 0.'
    alternatives:
    - value: 0
      note: Named alternative.
      cites: *id002
epistemology:
  value: 'Access to orishas through divination (Ifá palm nuts), initiation, and mediumship; priestly interpretation.'
  certainty: 1.0
  cites:
  - source: S1
    locator: Ifá; rituals
  how_known: Britannica.
ethics:
  value: Not developed as a single ethical system in this article; practical guidance via oracle prescriptions.
  certainty: 0.7
  cites:
  - source: S1
    locator: Ifá
  how_known: Silence on ethics treatise.
practice:
  ritual_and_practice:
    value: 'Divination, sacrifice (including animal sacrifice protected in U.S. Supreme Court case), initiation/crowning,
      bembé drum dances with possession mediumship, home altars.'
    certainty: 1.0
    cites:
    - source: S1
      locator: rituals; practice today
    how_known: Britannica.
  community_form:
    value: 'House/ile structures under orisha priesthood; tens of thousands initiated, millions who consult;
      Miami/New York diasporas.'
    certainty: 0.7
    cites:
    - source: S1
      locator: diaspora
    how_known: Britannica estimates.
science:
  historical_stance:
    value: Not addressed as a science doctrine.
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Silence.
  current_stance:
    value: Not addressed.
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Silence.
schools_and_variants:
- name: Lucumí / Regla de Ocha (Cuban)
  form: regional
  how_it_differs: Core Cuban development; saint–orisha correspondences.
  lio_difference: B1 D1 E1 as umbrella.
  certainty: 1.0
  cites:
  - source: S1
    locator: opening
- name: Diaspora Santería (U.S./Latin America)
  form: modern
  how_it_differs: Post-1959 spread; public recognition including legal protection of sacrifice.
  lio_difference: Same scores.
  certainty: 1.0
  cites:
  - source: S1
    locator: diaspora; practice today
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Afro-Caribbean Lucumí/Santería practitioners; hidden/initiatory; no reliable public census
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — qualitative from listed source; not a genius-rate denominator.'
v7_1_rubric:
  label: authorial v7.1 scores
  L: 7
  P: 6
  E: 5
  V: 5
  X: 3
  total: 26
  scoring_note: 'Santería scores moderately due to its rich syncretic traditions and emphasis on spiritual
    balance, offering cultural coherence but limited by supernatural elements and lack of empirical rigor.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 56 and section 7 scoring notes'
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
  use_when: 'Santería, Lucumí, Regla de Ocha, orisha religion of Cuban Yoruba lineage.'
  do_not_use_when: Haitian Vodou (VODUN). Generic Catholicism despite saint correspondences.
  neighbors:
  - code: VODUN
    relation: neighbor (easily confused)
  - code: CHRIST
    relation: neighbor (easily confused)
review:
  data_quality_flags: []
  open_questions:
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Joseph M. Murphy
  citation: 'Murphy, Joseph M.. "Santería." Encyclopaedia Britannica. https://www.britannica.com/topic/Santeria.
    Wayback Machine snapshot 2026-10-12 06:32:21 UTC: https://web.archive.org/web/20261012063221/https://www.britannica.com/topic/Santeria.'
  url: 'https://www.britannica.com/topic/Santeria'
  accessed: '2026-10-25'
  reliability_note: 'Signed article (scholar of Santería); full short article read. P44(e): read in the
    Wayback copy (https://web.archive.org/web/20261012063221/https://www.britannica.com/topic/Santeria);
    live page timed out on 2026-10-15, so no live comparison.'
- id: S2
  type: tertiary
  kind: encyclopedia
  citation: 'Wikipedia contributors. "Santería." Wikipedia. Accessed 2026-10-25.'
  url: 'https://en.wikipedia.org/wiki/Santer%C3%ADa'
  accessed: '2026-10-25'
---
# Santería (Lucumí/Regla de Ocha) (SANTER)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

Santería is a Yoruba-origin orisha religion developed in Cuba and spread through the Americas; named from correspondences between orishas and Catholic saints; also called Lucumí / religion of the orishas [S1].

## Core metaphysics

Personal orishas accessed by divination, sacrifice, initiation, and mediumship; guide, protect, heal, prophesy [S1].

## Position on the LIO axes

- **A, C:** UNKNOWN.
- **B_cause: 1** — regular orisha intervention/sacrifice exchange [S1].
- **D_authority: 1** — Ifá/initiation/mediumship [S1].
- **E_scope: 1** — house/priestly community form [S1].

## Schools and variants

Cuban Lucumí core; post-1959 diaspora [S1].

## Science

Not addressed [S1].

## Coding guidance

Cuban Yoruba orisha lineage. Not VODUN.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> SANTER (26/50) — Santería (Lucumí/Regla de Ocha). Santería scores moderately due to its rich syncretic traditions and emphasis on spiritual balance, offering cultural coherence but limited by supernatural elements and lack of empirical rigor.

## Open questions

- High God / Olodumare doctrine needs a fuller source than this Britannica page.
- Afterlife / ori doctrine.

## Research log

- 2026-10-15 (batch S9): Britannica Santería; B D E scored.
- 2026-10-25: deepened classification, origins, metaphysics, practice. Axes kept.
- 2026-10-25: adherents/estimate filled (qualitative).
- 2026-10-25: A/C scored.
- 2026-10-25: Filled reserved_exemptions from Wikipedia Santería.
