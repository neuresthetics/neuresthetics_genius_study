---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 10
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S8 for Jason)
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
    summary: 'Draft (systems batch S8): filled from Britannica "Shintō" (Hirai). A 3 (0.5, alt 2); B,
      C, D, E UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'P44(e) compliance (with the S7 fixes): Wayback snapshot URL and timestamp cited.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S8 audit fix: B UNKNOWN -> 2 @0.5 (alt 1) from the full article; A how_known adds Hirata
      and musubi.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S9 audit fix: S1 reliability_note now points to the later pages S2–S4.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from Britannica Shintō (Hirai): kami way, no founder/fixed dogmas, Shrine/Sect/Folk
      types, purification, Imperial history. Axes kept.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Fill adherents/estimate gloss from existing sources (order-of-magnitude / qualitative). Axes
      unchanged.
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score D_authority 1 (0.7) and C_ledger 4 (0.7) from Britannica Shinto (tradition/shrines;
      purity not karma ledger).
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score E_scope 1 (0.5) from sources on file. Alternatives named.
identity:
  id: SHINTO
  v7_1_number: 45
  v7_1_label: Shinto
  display_label: Shinto
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: religion
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: 'Britannica: indigenous Japanese religion.'
  family:
    value: "Shintō ('way of kami'): indigenous Japanese veneration of kami (sacred powers/deities/spirits)\
      \ in nature and ancestors; no single founder or fixed dogmas"
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  parent_traditions:
    value:
    - Yayoi-period agricultural rites and shamanism
    - Later Confucian/Daoist/Buddhist influence
    - Imperial Household cult history
    certainty: 1.0
    cites:
    - source: S1
      locator: origins; history
    how_known: Britannica.
  related_codes:
  - code: BUDDH
    relation: overlaps
    note: long shinbutsu shūgō amalgamation
  - code: ANIM
    relation: neighbor (easily confused)
    note: kami not reducible to ANIM umbrella
  - code: CONFUC
    relation: overlaps
    note: ethical influence historically
origins:
  founding_era:
    value: Indigenous; Yayoi roots (~3rd–2nd c. BCE); term distinguishes from Buddhism after 6th c. CE
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; origins
    how_known: Britannica.
  founding_region:
    value: Japan
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  founders_or_key_figures:
    value:
    - No founder; Imperial Household and clan ujigami cults; Sect Shintō founders (19th c.); scholars
      e.g. Motoori Norinaga
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; nature
    how_known: Britannica.
  key_texts:
  - value: No official sacred scriptures in the strict sense; classical myths/classics; later sect writings
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
metaphysics:
  god_nature_relation:
    value: Kami inhabit natural elements/phenomena and ancestral spirits; musubi creative power; polytheistic
      ancient Shintō.
    stance: many gods within nature
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; kami
    how_known: Britannica.
  deity_personal:
    value: 'Kami have divine personalities and respond to prayers; also abstract powers (growth, judgment).'
    stance: personal
    certainty: 0.7
    cites:
    - source: S1
      locator: kami FAQ
    how_known: Britannica.
  intervention:
    value: Kami guide toward truthful living; respond to prayers; blessings via purification.
    stance: regular
    certainty: 0.7
    cites:
    - source: S1
      locator: kami; beliefs
    how_known: Britannica.
  miracles:
    value: Not framed vs natural law.
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: Silence.
  petition_and_prayer:
    value: Prayers at shrines; priests for special rites; kami respond.
    stance: petition answered
    certainty: 0.7
    cites:
    - source: S1
      locator: shrines; kami
    how_known: Britannica.
  afterlife:
    value: Yomi (Hades) in three-world myth; also Tokoyo utopia beyond sea; continuity with ancestors
      (tsunagari).
    stance: varies by school
    certainty: 0.5
    cites:
    - source: S1
      locator: early clan; beliefs
    how_known: '0.5 — multiple cosmologies.'
  moral_ledger:
    value: 'No original sin; purity/sincerity (makoto, magokoro); not a karma ledger in S1.'
    stance: none
    certainty: 0.5
    cites:
    - source: S1
      locator: beliefs
    how_known: '0.5.'
  authority:
    value: 'No fixed dogmas; tradition, shrines, Imperial history; Sect founders for Kyōha.'
    stance: tradition or ancestors
    certainty: 0.7
    cites:
    - source: S1
      locator: opening; nature
    how_known: Britannica.
  reserved_exemptions:
    value: Not addressed.
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: Silence.
  teleology_in_nature:
    value: Musubi as creative/harmonizing power of kami; not designer teleology.
    stance: immanent ends
    certainty: 0.5
    cites:
    - source: S1
      locator: beliefs
    how_known: '0.5.'
  necessity_and_freedom:
    value: Not addressed.
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Silence.
lio_axes:
  A_locus:
    value: 3
    rationale: "Kami ('sacred or divine power, specifically the various gods or deities') are found in\
      \ nature and in outstanding men."
    certainty: 0.5
    cites: &id001
    - source: S1
      locator: introduction; Early clan religion
    - source: S2
      locator: Fukko Shintō
    how_known: "0.5: gods within nature fit 3 (as JAIN, CHNFOLK); kami of ideas such as creation make\
      \ 2 the alternative. Full read: Hirata's creator god and other-world retribution 'were not accepted\
      \ into the main current of Shintō'; Motoori's musubi, 'the mystical power of becoming or of creation',\
      \ is the reason for alternative 2."
    alternatives:
    - value: 2
      note: Named alternative.
      cites: *id001
  B_cause:
    value: 2
    rationale: "Petitionary prayer to protecting kami: 'prayers were offered for the safety of the state\
      \ and people'; children visit the shrine 'to give thanks for kami’s protection'; Motoori's 'absolute\
      \ faith—according to which all problems beyond human capability were turned over to kami'."
    certainty: 0.5
    cites: &id002
    - source: S3
      locator: Political and social roles
    - source: S4
      locator: rites of passage
    - source: S2
      locator: Fukko Shintō
    how_known: '0.5 (S8 audit ruling): protection and answered prayer, with no doctrine of miracles stated.
      Alternative 1.'
    alternatives:
    - value: 1
      note: Named alternative.
      cites: *id002
  C_ledger:
    value: 4
    certainty: 0.7
    cites:
    - source: S1
      locator: ethics; purity
    how_known: '0.7 — purity/sincerity; no original sin; not a karma ledger in S1.'
    rationale: 'C=4: none. Not 3: not karma.'
    alternatives:
    - value: 3
      note: Named alternative if reading purity pollution as impersonal moral law.
      cites:
      - source: S1
        locator: purity
  D_authority:
    value: 1
    certainty: 0.7
    cites:
    - source: S1
      locator: opening; authority
    how_known: '0.7 — no fixed dogmas; tradition, shrines, Imperial history; stance tradition or ancestors.'
    rationale: 'D=1: tradition. Not 0: not single closed revelation for Shinto as such.'
    alternatives:
    - value: 2
      note: Named alternative if coding Sect Shinto founders as mixed.
      cites:
      - source: S1
        locator: Sect
  E_scope:
    value: 1
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — kami and shrine locality; purity/ritual in-group'
    rationale: E=1 at 0.5.
    alternatives:
    - value: 2
      note: Named alternative for State Shinto universalism.
      cites:
      - source: S1
        locator: opening
epistemology:
  value: Practice and sincerity over formal philosophy; purification to commune with kami; myths and shrine
    tradition.
  certainty: 1.0
  cites:
  - source: S1
    locator: opening; beliefs
  how_known: Britannica.
ethics:
  value: 'Sincerity, true heart, purification; humanity as children of kami (worthy of respect); tsunagari
    with ancestors/descendants.'
  certainty: 1.0
  cites:
  - source: S1
    locator: beliefs
  how_known: Britannica.
practice:
  ritual_and_practice:
    value: 'Shrines (jinja), torii, purification, matsuri festivals, harvest rites; visit at convenience
      not weekly services.'
    certainty: 1.0
    cites:
    - source: S1
      locator: shrines; society
    how_known: Britannica.
  community_form:
    value: Shrine Shintō parish (ujiko); Sect organizations; Folk roadside/agricultural; State Shintō
      defunct after WWII.
    certainty: 1.0
    cites:
    - source: S1
      locator: nature; society
    how_known: Britannica.
science:
  historical_stance:
    value: Not a science program.
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: Coder reading.
  current_stance:
    value: Not addressed.
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: Silence.
schools_and_variants:
- name: Shrine Shintō (Jinja)
  form: regional
  how_it_differs: Main current; includes defunct State Shintō structure historically.
  lio_difference: Axes kept.
  certainty: 1.0
  cites:
  - source: S1
    locator: nature
- name: Sect Shintō (Kyōha)
  form: modern
  how_it_differs: '13+ sects from ~19th c. with founders/systematizers.'
  lio_difference: May differ — not rescored.
  certainty: 1.0
  cites:
  - source: S1
    locator: nature
- name: Folk Shintō (Minzoku)
  form: popular
  how_it_differs: 'No formal org; roadside images, rural agricultural rites.'
  lio_difference: Same umbrella.
  certainty: 1.0
  cites:
  - source: S1
    locator: nature
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Japanese shrine practice and related; often cultural affiliation rather than exclusive membership
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — qualitative from listed source; not a genius-rate denominator.'
v7_1_rubric:
  label: authorial v7.1 scores
  L: 8
  P: 8
  E: 6
  V: 6
  X: 4
  total: 32
  scoring_note: 'Shinto scores moderately due to its elegant focus on natural harmony and ritual purity,
    offering cultural and ethical coherence but constrained by supernatural elements and traditional authority
    over empirical rigor.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 45 and section 7 scoring notes'
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
  use_when: Shintō / kami shrine identity as primary.
  do_not_use_when: Japanese Buddhist temple identity without Shintō frame. Generic ANIM.
  neighbors:
  - code: BUDDH
    relation: neighbor (easily confused)
  - code: ANIM
    relation: neighbor (easily confused)
review:
  data_quality_flags: []
  open_questions:
  - 'Later sections (beliefs, practices) not read.'
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Naofusa Hirai; Britannica Editors
  citation: 'Hirai, Naofusa, and Britannica Editors. "Shintō." Encyclopaedia Britannica. https://www.britannica.com/topic/Shinto.
    Wayback Machine snapshot 2026-10-03 18:03:43 UTC: https://web.archive.org/web/20261003180343/https://www.britannica.com/topic/Shinto.'
  url: 'https://www.britannica.com/topic/Shinto'
  accessed: '2026-10-25'
  reliability_note: 'Signed article (Kokugakuin emeritus professor); Introduction and early history read
    here; the later pages are S2–S4 (same article). P44(e): read in the Wayback copy (https://web.archive.org/web/20261003180343/https://www.britannica.com/topic/Shinto);
    live page timed out on 2026-10-15, so no live comparison.'
- id: S2
  type: tertiary
  kind: encyclopedia
  author: Naofusa Hirai; Britannica Editors
  citation: 'Hirai, Naofusa, and Britannica Editors. "Shintō: Shintō reaction against Buddhism." Encyclopaedia
    Britannica. https://www.britannica.com/topic/Shinto/Shinto-reaction-against-Buddhism. Wayback Machine
    snapshot 2025-11-25 14:48:08 UTC: https://web.archive.org/web/20251125144808/https://www.britannica.com/topic/Shinto/Shinto-reaction-against-Buddhism.'
  url: 'https://www.britannica.com/topic/Shinto/Shinto-reaction-against-Buddhism'
  accessed: '2026-10-25'
  reliability_note: 'Later page of the same signed article (S8 audit fix). P44(e): read in the Wayback
    copy (https://web.archive.org/web/20251125144808/https://www.britannica.com/topic/Shinto/Shinto-reaction-against-Buddhism);
    live page not compared.'
- id: S3
  type: tertiary
  kind: encyclopedia
  author: Naofusa Hirai; Britannica Editors
  citation: 'Hirai, Naofusa, and Britannica Editors. "Shintō: Political and social roles." Encyclopaedia
    Britannica. https://www.britannica.com/topic/Shinto/Political-and-social-roles. Wayback Machine snapshot
    2025-10-08 20:43:06 UTC: https://web.archive.org/web/20251008204306/https://www.britannica.com/topic/Shinto/Political-and-social-roles.'
  url: 'https://www.britannica.com/topic/Shinto/Political-and-social-roles'
  accessed: '2026-10-25'
  reliability_note: 'Later page of the same signed article (S8 audit fix). P44(e): read in the Wayback
    copy (https://web.archive.org/web/20251008204306/https://www.britannica.com/topic/Shinto/Political-and-social-roles);
    live page not compared.'
- id: S4
  type: tertiary
  kind: encyclopedia
  author: Naofusa Hirai; Britannica Editors
  citation: 'Hirai, Naofusa, and Britannica Editors. "Shintō: Ritual practices and institutions." Encyclopaedia
    Britannica. https://www.britannica.com/topic/Shinto/Ritual-practices-and-institutions. Wayback Machine
    snapshot 2026-10-06 22:19:34 UTC: https://web.archive.org/web/20261006221934/https://www.britannica.com/topic/Shinto/Ritual-practices-and-institutions.'
  url: 'https://www.britannica.com/topic/Shinto/Ritual-practices-and-institutions'
  accessed: '2026-10-25'
  reliability_note: 'Later page of the same signed article (S8 audit fix). P44(e): read in the Wayback
    copy (https://web.archive.org/web/20261006221934/https://www.britannica.com/topic/Shinto/Ritual-practices-and-institutions);
    live page not compared.'
---
# Shintō (SHINTO)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

Shintō is Japan's indigenous way of kami: no founder, no fixed dogmas; Shrine, Sect, and Folk types; purification and sincerity [S1].

## Core metaphysics

Many kami in nature and ancestors; musubi; respond to prayer [S1].

## Position on the LIO axes

Axes kept from prior coding (not re-scored this pass).

## Schools and variants

Shrine / Sect / Folk [S1].

## Science

Not a science program [S1].

## Coding guidance

Shintō identity; not ANIM dump.

## v7.1 scoring note

> SHINTO (32/50) — Shinto. Shinto scores moderately due to its elegant focus on natural harmony and ritual purity, offering cultural and ethical coherence but constrained by supernatural elements and traditional authority over empirical rigor.

## Open questions

- Axis rescore when Jason wants shrine vs sect differentiation.

## Research log

- Prior batch: thin fill.
- 2026-10-25: deepened from Britannica Shintō (Hirai). Axes kept.
- 2026-10-25: adherents/estimate filled (qualitative).
- 2026-10-25: D/C scored.
- 2026-10-25: E_scope scored 1 (0.5).
