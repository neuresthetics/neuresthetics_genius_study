---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 5
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
    summary: 'Draft (systems batch S12): filled from Britannica "Falun Gong" (Ownby). B 1 (0.5, alt 2);
      D 1 (0.5, alt 2); A, C, E UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from Britannica Falun Gong (Ownby): Li Hongzhi 1992, Zhuan falun, qigong
      offshoot, higher-level cultivation, diaspora/media. Keep B=1 D=1; A C E UNKNOWN.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Fill adherents/estimate gloss from existing sources (order-of-magnitude / qualitative). Axes
      unchanged.
identity:
  id: FALUNG
  v7_1_number: 75
  v7_1_label: Falun Gong (Falun Dafa)
  display_label: Falun Gong (Falun Dafa)
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: new religious movement
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: Spiritual movement from qigong; PRC branded cult; 0.7 NRM vs self-cultivation.
  family:
    value: 'Falun Gong / Falun Dafa: Li Hongzhi (1992) offshoot of qigong; Zhuan falun as sacred text;
      revolving dharma wheel installed in followers'
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; rise
    how_known: Britannica.
  parent_traditions:
    value:
    - Chinese qigong movement (1950s TCM amalgam; 1980s–90s boom)
    - Traditional Chinese medicine / self-cultivation
    certainty: 1.0
    cites:
    - source: S1
      locator: background
    how_known: Britannica.
  related_codes:
  - code: BUDDH
    relation: neighbor (easily confused)
    note: Dharma Wheel language ≠ Buddhism identity
  - code: TAO
    relation: neighbor (easily confused)
    note: qigong/TCM milieu not Daoism-as-philosophy
  - code: CHNFOLK
    relation: overlaps
    note: Chinese popular cultivation context
origins:
  founding_era:
    value: Founded 1992 by Li Hongzhi; Zhuan falun 1994; Li to US 1998; PRC ban after April 25 1999 Beijing
      protest
    certainty: 1.0
    cites:
    - source: S1
      locator: rise; controversy
    how_known: Britannica.
  founding_region:
    value: "China; diaspora especially US and Canada after Li's departure"
    certainty: 1.0
    cites:
    - source: S1
      locator: diaspora
    how_known: Britannica.
  founders_or_key_figures:
    value:
    - Li Hongzhi (Master Li)
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  key_texts:
  - value: Zhuan falun (1994; transcription of nine-part lecture series; sacred focus after 1998)
    certainty: 1.0
    cites:
    - source: S1
      locator: controversy
    how_known: Britannica.
metaphysics:
  god_nature_relation:
    value: Revolving wheel purifying bodies in another dimension; demonic and apocalyptic themes in Zhuan
      falun; not classical theism in this article.
    stance: not addressed
    certainty: 0.5
    cites:
    - source: S1
      locator: rise; controversy
    how_known: God doctrine thin; 0.5.
  deity_personal:
    value: Master Li relationship via text; deity doctrine not detailed.
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S1
      locator: controversy
    how_known: Silence.
  intervention:
    value: Li installs revolving wheel purifying in another dimension; ongoing Master relationship via
      rereading text.
    stance: regular
    certainty: 0.7
    cites:
    - source: S1
      locator: rise; controversy
    how_known: Britannica.
  miracles:
    value: Body purification in another dimension; qigong paranormal/ESP currents in broader movement.
    stance: affirmed
    certainty: 0.5
    cites:
    - source: S1
      locator: rise; background
    how_known: '0.5.'
  petition_and_prayer:
    value: Practice centered on reading Zhuan falun and cultivation; petition not detailed.
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S1
      locator: controversy
    how_known: Thin.
  afterlife:
    value: Apocalyptic themes noted; details thin in article.
    stance: not addressed
    certainty: 0.5
    cites:
    - source: S1
      locator: controversy
    how_known: Thin.
  moral_ledger:
    value: Not a clear ledger doctrine in this article.
    stance: none
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: Silence.
  authority:
    value: Founder Li Hongzhi; Zhuan falun as sacred text focus; Master Li relationship sustained by rereading.
    stance: founder
    certainty: 0.7
    cites:
    - source: S1
      locator: controversy
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
    value: Not addressed as teleology doctrine.
    stance: none
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: Silence.
  necessity_and_freedom:
    value: Not addressed.
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Silence.
lio_axes:
  A_locus:
    value: 'UNKNOWN'
    how_known: Not addressed in the sources read.
  B_cause:
    value: 1
    rationale: "Falun Gong is named for 'the revolving wheel that Li promised to install in his followers,\
      \ purifying their bodies “in another dimension”'; Zhuan falun 'stressed demonic and apocalyptic\
      \ themes'."
    certainty: 0.5
    cites: &id001
    - source: S1
      locator: Rise in popularity
    how_known: '0.5: Li’s message also sought to dispel qigong’s links with “faith healing”. Alternative
      2.'
    alternatives:
    - value: 2
      note: Named alternative.
      cites: *id001
  C_ledger:
    value: 'UNKNOWN'
    how_known: Not addressed in the sources read.
  D_authority:
    value: 1
    rationale: "Zhuan falun 'would henceforth serve as the focus of Falun Gong practice. Followers were\
      \ to read and reread the sacred text, sustaining their relationship with Master Li'."
    certainty: 0.5
    cites: &id002
    - source: S1
      locator: Controversy
    how_known: '0.5: a sacred text and master; observation is not discussed. Alternative 2.'
    alternatives:
    - value: 2
      note: Named alternative.
      cites: *id002
  E_scope:
    value: 'UNKNOWN'
    how_known: Not addressed in the sources read.
epistemology:
  value: Higher-level cultivation; reread sacred Zhuan falun; originally presented against fraud/faith-healing
    associations of qigong.
  certainty: 1.0
  cites:
  - source: S1
    locator: rise; controversy
  how_known: Britannica.
ethics:
  value: Not developed as a single ethics treatise in this article (freedom-of-religion framing in diaspora
    advocacy).
  certainty: 0.5
  cites:
  - source: S1
    locator: diaspora
  how_known: Thin.
practice:
  ritual_and_practice:
    value: 'Qigong-style cultivation; reread Zhuan falun; peaceful media protests historically; diaspora
      media (Epoch Times, NTD, Sound of Hope); Shen Yun performing arts.'
    certainty: 1.0
    cites:
    - source: S1
      locator: controversy; diaspora
    how_known: Britannica.
  community_form:
    value: Nationwide organization in China 1992–95; diaspora networks after ban; no single encyclopedia
      membership figure trusted (2–60 million range noted).
    certainty: 0.7
    cites:
    - source: S1
      locator: rise; diaspora
    how_known: Britannica.
science:
  historical_stance:
    value: Emerged from qigong boom that claimed scientific status for qigong energy; critics called superstition;
      Li emphasized higher-level cultivation over faith healing.
    certainty: 1.0
    cites:
    - source: S1
      locator: background; rise
    how_known: Britannica.
  current_stance:
    value: Not a single science doctrine post-diaspora.
    certainty: 0.7
    cites:
    - source: S1
      locator: diaspora
    how_known: Thin.
schools_and_variants:
- name: Mainland Falun Gong (pre-1999 / underground)
  form: regional
  how_it_differs: PRC banned as heretical cult after 1999.
  lio_difference: B1 D1.
  certainty: 1.0
  cites:
  - source: S1
    locator: controversy
- name: Diaspora Falun Gong / media organs
  form: modern
  how_it_differs: 'Epoch Times, Shen Yun, Western advocacy.'
  lio_difference: Same scores.
  certainty: 1.0
  cites:
  - source: S1
    locator: diaspora
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Falun Gong practitioners; PRC suppression makes counts contested
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — qualitative from listed source; not a genius-rate denominator.'
v7_1_rubric:
  label: authorial v7.1 scores
  L: 6
  P: 5
  E: 2
  V: 3
  X: 1
  total: 17
  scoring_note: 'Falun Gong scores low due to its reliance on supernatural claims and authority over evidence,
    making it less compatible with empirical science despite ethical appeals.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 75 and section 7 scoring notes'
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
  use_when: Falun Gong / Falun Dafa / Li Hongzhi practice identity.
  do_not_use_when: Generic qigong without Falun Gong identity. Buddhism.
  neighbors:
  - code: BUDDH
    relation: neighbor (easily confused)
  - code: TAO
    relation: neighbor (easily confused)
  - code: CHNFOLK
    relation: neighbor (easily confused)
review:
  data_quality_flags:
  - The article is mostly history; doctrine is thin.
  open_questions:
  - 'A source on Falun Gong doctrine (truthfulness, compassion, forbearance; karma).'
  - 'Adherents: S1 cites estimates of 2 to 60 million (1992–95).'
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: David Ownby
  citation: 'Ownby, David. "Falun Gong." Encyclopaedia Britannica. https://www.britannica.com/topic/Falun-Gong.
    Wayback Machine snapshot 2026-10-06 23:44:42 UTC: https://web.archive.org/web/20261006234442/https://www.britannica.com/topic/Falun-Gong.'
  url: 'https://www.britannica.com/topic/Falun-Gong'
  accessed: '2026-10-25'
  reliability_note: 'Signed article (historian of Chinese religion); full article read. Mostly history;
    little doctrine. P44(e): read in the Wayback copy (https://web.archive.org/web/20261006234442/https://www.britannica.com/topic/Falun-Gong);
    live page not compared (live Britannica times out from the box).'
---
# Falun Gong / Falun Dafa (FALUNG)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

Falun Gong (Falun Dafa), founded by Li Hongzhi in 1992, is a qigong offshoot emphasizing higher-level cultivation and Zhuan falun; banned in PRC after 1999; active diaspora [S1].

## Core metaphysics

Revolving dharma wheel purifying in another dimension; Master Li via sacred text; apocalyptic themes in Zhuan falun [S1].

## Position on the LIO axes

- **A, C, E:** UNKNOWN.
- **B: 1** — wheel/purification intervention [S1].
- **D: 1** — founder/text authority [S1].

## Schools and variants

Mainland vs diaspora/media [S1].

## Science

Qigong scientific-status history; Li against fraud associations [S1].

## Coding guidance

Falun Gong identity. Not generic qigong.

## v7.1 scoring note

> FALUNG (17/50) — Falun Gong (Falun Dafa). Falun Gong scores low due to its reliance on supernatural claims and authority over evidence, making it less compatible with empirical science despite ethical appeals.

## Open questions

- Fuller Zhuan falun doctrine for A/C.

## Research log

- Prior batch: Britannica Falun Gong; B D scored.
- 2026-10-25: deepened. Axes kept.
- 2026-10-25: adherents/estimate filled (qualitative).
