---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 3
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S9 for Jason)
  model_used: Grok Bot executor agent; direct reads of the cited pages
  collected_on: 2026-10-01
  last_updated: '2026-10-15'
  change_log:
  - date: 2026-10-01
    by: scripts/make_system_stubs.py
    summary: Stub created from v7.1 data book table 4 and section 7.
  - date: 2026-10-02
    by: scripts/make_system_stubs.py
    summary: 'Decision P7: E_scope note added. E is not scored in a stub; when it is, score it on the world''s order (same rules for every kind of being and event, no in-group exceptions in this-world events). Salvation and moral community go on C_ledger.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'Draft (systems batch S12): filled from Britannica "Thelema" (Doyle White). A BELOW_THRESHOLD; B 1 (0.5, alt 2); D 1 (0.5, alt 2); C, E UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
identity:
  id: THELEM
  v7_1_number: 74
  v7_1_label: Thelema (Crowley/Ordo Templi Orientis)
  display_label: Thelema (Crowley/Ordo Templi Orientis)
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: esoteric or occult tradition
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: '''commonly regarded as a form of both esotericism and occultism''.'
  family:
    value: TODO
  parent_traditions:
    value: TODO
  related_codes: []
origins:
  founding_era:
    value: '1904'
    certainty: 1.0
    cites:
    - source: S1
      locator: Origins and history
    how_known: The Book of the Law, April 1904.
  founding_region:
    value: TODO
  founders_or_key_figures:
    value:
    - Aleister Crowley
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: Britannica.
  key_texts: []
metaphysics:
  god_nature_relation:
    value: TODO
    stance: TODO
  deity_personal:
    value: TODO
    stance: TODO
  intervention:
    value: TODO
    stance: TODO
  miracles:
    value: TODO
    stance: TODO
  petition_and_prayer:
    value: TODO
    stance: TODO
  afterlife:
    value: TODO
    stance: TODO
  moral_ledger:
    value: TODO
    stance: TODO
  authority:
    value: TODO
    stance: TODO
  reserved_exemptions:
    value: TODO
    stance: TODO
  teleology_in_nature:
    value: TODO
    stance: TODO
  necessity_and_freedom:
    value: TODO
lio_axes:
  A_locus:
    value: BELOW_THRESHOLD
    how_known: '''Attitudes to this theology nevertheless vary among Thelemites. Some are theists and believe that Thelema’s deities literally exist, whereas others are atheists and regard such entities as symbolic figures'' (S1).'
    note: P44(b).
  B_cause:
    value: 1
    rationale: Crowley defined magick as 'the Science and Art of causing Change to occur in conformity with Will'; sex magic is used 'to concentrate the Thelemite’s will to achieve specific aims'.
    certainty: 0.5
    cites: &id001
    - source: S1
      locator: Beliefs and practices
    how_known: '0.5: atheist Thelemites may read magick differently. Alternative 2.'
    alternatives:
    - value: 2
      note: Named alternative.
      cites: *id001
  C_ledger:
    value: UNKNOWN
    how_known: Not addressed in the sources read.
  D_authority:
    value: 1
    rationale: '''The tradition centers on a text, The Book of the Law, that Crowley claimed to have received from a supernatural source in 1904'', ''audibly delivered to him by Aiwass''.'
    certainty: 0.5
    cites: &id002
    - source: S1
      locator: introduction
    - source: S1
      locator: Origins and history
    how_known: '0.5: revelation is central; no ranking against observation given. Alternative 2.'
    alternatives:
    - value: 2
      note: Named alternative.
      cites: *id002
  E_scope:
    value: UNKNOWN
    how_known: Not addressed in the sources read.
epistemology:
  value: TODO
ethics:
  value: '''Do what thou wilt shall be the whole of the Law''; ''Love is the law, love under will''.'
  certainty: 1.0
  cites:
  - source: S1
    locator: Beliefs and practices
  how_known: Britannica.
practice:
  ritual_and_practice:
    value: TODO
  community_form:
    value: TODO
science:
  historical_stance:
    value: TODO
  current_stance:
    value: TODO
schools_and_variants: []
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: TODO
v7_1_rubric:
  label: authorial v7.1 scores
  L: 6
  P: 5
  E: 3
  V: 4
  X: 2
  total: 20
  scoring_note: Thelema scores low overall due to its heavy reliance on occult revelation and unverified magick, though it fosters individual empowerment and creative spiritual exploration.
  source: v7.1 data book, section 6 table (tables[4]) row 74 and section 7 scoring notes
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
  use_when: The person self-identifies as a Thelemite or was an OTO / A∴A∴ member.
  do_not_use_when: Wicca is WICCA; chaos magic is CHAOSM.
  neighbors: []
review:
  data_quality_flags: []
  open_questions:
  - 'Adherents: Hedenborg White estimate 5,000–10,000 (2020), as reported in S1; cite directly.'
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Ethan Doyle White
  citation: 'Doyle White, Ethan. "Thelema." Encyclopaedia Britannica. https://www.britannica.com/topic/Thelema. Wayback Machine snapshot 2026-02-17 11:24:05 UTC: https://web.archive.org/web/20260217112405/https://www.britannica.com/topic/Thelema.'
  url: https://www.britannica.com/topic/Thelema
  accessed: '2026-10-15'
  reliability_note: 'Signed article; full article read. P44(e): read in the Wayback copy (https://web.archive.org/web/20260217112405/https://www.britannica.com/topic/Thelema); live page not compared (live Britannica times out from the box).'
---

# Thelema (Crowley/Ordo Templi Orientis) (THELEM)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

Thelema is a 'religion established by the British occultist Aleister Crowley in the 1900s', centred on The Book of the Law [S1].

## Core metaphysics

Nuit, Hadit, Ra-Hoor-Khuit; True Will; magick [S1].

## Position on the LIO axes

- A BELOW_THRESHOLD; B 1 (0.5, alt 2); D 1 (0.5, alt 2).
- C, E UNKNOWN.

## Schools and variants

TODO

## Science

TODO

## Coding guidance

Thelemites.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> THELEM (20/50) — Thelema (Crowley/Ordo Templi Orientis). Thelema scores low overall due to its heavy reliance on occult revelation and unverified magick, though it fosters individual empowerment and creative spiritual exploration.

## Open questions

- Adherents.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7 (score E on the world's order when the stub is filled).
- 2026-10-15 (systems batch S12): read the listed sources; quotations checked word for word against the fetched page text. Britannica pages read in Wayback copies under P44(e); AI Top Questions not used.
