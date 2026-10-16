---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 6
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S8 for Jason)
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
    summary: 'Draft (systems batch S8, thin): one sentence in Britannica "Modern Paganism" (Doyle White). A BELOW_THRESHOLD; rest UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'P44(e) compliance (with the S7 fixes): Wayback snapshot URL and timestamp cited.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S8 audit fix: Britannica generic sentence dropped; re-sourced from kemet.org FAQ (House of Netjer) under P45(a). A UNKNOWN; B 1 @0.5 (P45 cap). Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S9 audit: P46(b) applied (organization named; plurality noted). Scores unchanged.'
identity:
  id: KEMET
  v7_1_number: 50
  v7_1_label: Kemetism (Kemetic Orthodoxy/Egyptian Reconstructionism)
  display_label: Kemetism (Kemetic Orthodoxy/Egyptian Reconstructionism)
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: religion
    certainty: 0.5
    cites:
    - source: S1
      locator: FAQ
    how_known: 'P45 lower tier: own statement.'
  family:
    value: TODO
  parent_traditions:
    value: TODO
  related_codes: []
origins:
  founding_era:
    value: TODO
  founding_region:
    value: TODO
  founders_or_key_figures:
    value:
    - Rev. Tamara Siuda (Nisut Hekatawy)
    certainty: 0.5
    cites:
    - source: S1
      locator: FAQ
    how_known: 'P45 lower tier: own statement; for Kemetic Orthodoxy only.'
  key_texts: []
metaphysics:
  god_nature_relation:
    value: '''We do recognize ourselves as polytheists, as we do acknowledge the existence of, and worship, many gods.'''
    stance: not addressed
    certainty: 0.5
    cites:
    - source: S1
      locator: FAQ
    how_known: P45 lower tier.
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
    value: UNKNOWN
    how_known: The FAQ affirms that many gods exist but does not place them in or beyond nature (S1).
  B_cause:
    value: 1
    rationale: '''When Netjer interacts with the Kemetic Orthodox within a ritual context, it is very intimate, personal, and face-to-face, more often than not in the form of Saq, or oracular, full trance possessions''.'
    certainty: 0.5
    cites:
    - source: S1
      locator: FAQ
    how_known: 'P45 cap 0.5. Covers Kemetic Orthodoxy, one organization within Kemetism. P46(b): this value describes the House of Netjer (Kemetic Orthodoxy) only, not all members; no other organization read, so no disagreement found.'
  C_ledger:
    value: UNKNOWN
    how_known: Not addressed in the source read.
  D_authority:
    value: UNKNOWN
    how_known: Not addressed in the source read.
  E_scope:
    value: UNKNOWN
    how_known: Not addressed in the source read.
epistemology:
  value: TODO
ethics:
  value: TODO
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
  L: 7
  P: 6
  E: 5
  V: 6
  X: 3
  total: 27
  scoring_note: Kemetism scores moderately due to its revival of ancient Egyptian balance and justice principles, offering ethical coherence but limited by mythic reconstruction and lack of empirical rigor.
  source: v7.1 data book, section 6 table (tables[4]) row 50 and section 7 scoring notes
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
  use_when: The person self-identifies with Egypt reconstructionist Paganism (Kemetism).
  do_not_use_when: Interest in ancient myth alone is not enough.
  neighbors: []
review:
  data_quality_flags:
  - 'P45 lower tier only: the House of Netjer’s own FAQ (Kemetic Orthodoxy, one organization; the FAQ says it is not a Neo-Pagan group). Capped at 0.5.'
  - 'P46(b): one organization (the House of Netjer (Kemetic Orthodoxy)); Kemetism is plural: Kemetic Orthodoxy is one organization among several Kemetic groups and solitary practitioners.'
  open_questions:
  - 'Leads: Krogh & Pillifant 2004, Sociology of Religion 65(2) (abstract: Kemetic Orthodoxy "is monistic ... based on ritual authority"); Harrison 2017 chapter. Not read in full.'
  - Adherents are TODO.
sources:
- id: S1
  type: primary
  kind: institutional page
  author: The House of Netjer
  citation: The House of Netjer. "Frequently Asked Questions." Kemet.org (Kemetic Orthodoxy). https://www.kemet.org/faq.
  url: https://www.kemet.org/faq
  accessed: '2026-10-15'
  reliability_note: 'P45 lower tier (a): the movement’s own published statement; claims capped at 0.5. Site copyright 1993–2020; undated page. P46(b): stands for the House of Netjer (Kemetic Orthodoxy) only. Kemetism is plural: Kemetic Orthodoxy is one organization among several Kemetic groups and solitary practitioners. A peer-reviewed source on the whole movement would take precedence.'
---

# Kemetism (Kemetic Orthodoxy/Egyptian Reconstructionism) (KEMET)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

Kemetic Orthodoxy (House of Netjer) describes itself as polytheist: 'we do acknowledge the existence of, and worship, many gods' [S1]. P45 lower tier.

## Core metaphysics

Many gods; ritual possession [S1].

## Position on the LIO axes

- B 1 (0.5, P45).
- A, C, D, E UNKNOWN.

## Schools and variants

TODO

## Science

TODO

## Coding guidance

Self-identified Kemetic / Kemetic Orthodox.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> KEMET (27/50) — Kemetism (Kemetic Orthodoxy/Egyptian Reconstructionism). Kemetism scores moderately due to its revival of ancient Egyptian balance and justice principles, offering ethical coherence but limited by mythic reconstruction and lack of empirical rigor.

## Open questions

- Scholarly leads not read.
- Adherents are TODO.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7 (score E on the world's order when the stub is filled).
- 2026-10-15 (systems batch S8): read the listed sources; quotations checked word for word against the fetched page text. Britannica pages read in full Wayback Machine copies (live site times out); AI Top Questions not used.
- 2026-10-15: P44(e) Wayback citation.
- 2026-10-15 (S8 audit fix): generic modern-Paganism sentence dropped; re-sourced from the movement’s own published statement under P45(a), capped at 0.5.
- 2026-10-15: P46(b) organization-scope notes added.
