---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 4
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
    summary: 'Draft (systems batch S11): filled from Britannica "Theosophy" (Melton). A 2 (0.5, alt 3); B BELOW_THRESHOLD; D 1 (0.5, alt 2); C, E UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S11 audit fix: B BELOW_THRESHOLD -> 3 @0.5 (alt 2).'
identity:
  id: THEOS
  v7_1_number: 63
  v7_1_label: Theosophy
  display_label: Theosophy
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: esoteric or occult tradition
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: '''occult movement originating in the 19th century''.'
  family:
    value: TODO
  parent_traditions:
    value: TODO
  related_codes: []
origins:
  founding_era:
    value: '1875'
    certainty: 1.0
    cites:
    - source: S1
      locator: History
    how_known: Britannica.
  founding_region:
    value: TODO
  founders_or_key_figures:
    value:
    - Helena Petrovna Blavatsky
    - Henry Steel Olcott
    - William Quan Judge
    certainty: 1.0
    cites:
    - source: S1
      locator: History
    how_known: Theosophical Society, New York, 1875.
  key_texts: []
metaphysics:
  god_nature_relation:
    value: '''most theosophists also affirm an overarching, all-encompassing unity that subsumes all differentiation''; ''God is utterly transcendent and impersonal'', ''creation is the product of spiritual emanations from God''.'
    stance: God in Nature and beyond it
    certainty: 1.0
    cites:
    - source: S1
      locator: Beliefs
    how_known: Britannica.
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
    value: 2
    rationale: 'Monism: ''an overarching, all-encompassing unity that subsumes all differentiation'', with ''God is utterly transcendent and impersonal'' and creation as ''spiritual emanations from God''.'
    certainty: 0.5
    cites: &id001
    - source: S1
      locator: Beliefs
    how_known: '0.5: an impersonal transcendent God within an all-embracing unity. Alternative 3.'
    alternatives:
    - value: 3
      note: Named alternative.
      cites: *id001
  B_cause:
    value: 3
    rationale: The 'higher psychic and spiritual powers' are studied under the Third Object, 'to investigate unexplained laws of Nature and the powers latent in human beings'; the 'fascination with supernatural or other extraordinary occurrences' is framed as unexplained law, not exemption.
    certainty: 0.5
    cites: &id002
    - source: S1
      locator: Beliefs
    - source: S1
      locator: History
    how_known: '0.5: the movement’s agreed position (S11 audit); Blavatsky’s phenomena from the Masters give alternative 2.'
    alternatives:
    - value: 2
      note: Named alternative.
      cites: *id002
  C_ledger:
    value: UNKNOWN
    how_known: Not addressed in the sources read.
  D_authority:
    value: 1
    rationale: Contact with spiritual reality 'through intuition, meditation, revelation, or some other state transcending normal human consciousness'; Blavatsky claimed 'regular contact with a brotherhood of Great Masters'.
    certainty: 0.5
    cites: &id003
    - source: S1
      locator: Beliefs
    - source: S1
      locator: History
    how_known: '0.5: the Second Object also encourages study of science. Alternative 2.'
    alternatives:
    - value: 2
      note: Named alternative.
      cites: *id003
  E_scope:
    value: UNKNOWN
    how_known: Not addressed in the sources read.
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
  E: 4
  V: 5
  X: 3
  total: 25
  scoring_note: Theosophy scores moderately due to its ambitious syncretic approach to spiritual unity, balanced by unverified esoteric claims and reliance on revelation over empirical methods.
  source: v7.1 data book, section 6 table (tables[4]) row 63 and section 7 scoring notes
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
  use_when: The person was a member of the Theosophical Society or self-identified as a theosophist.
  do_not_use_when: Anthroposophy is ANTHRO; generic New Age interest is not enough.
  neighbors: []
review:
  data_quality_flags: []
  open_questions:
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: J. Gordon Melton
  citation: 'Melton, J. Gordon. "Theosophy." Encyclopaedia Britannica. https://www.britannica.com/topic/theosophy. Wayback Machine snapshot 2026-07-05 14:56:39 UTC: https://web.archive.org/web/20260705145639/https://www.britannica.com/topic/theosophy.'
  url: https://www.britannica.com/topic/theosophy
  accessed: '2026-10-15'
  reliability_note: 'Signed article (historian of American religion); introduction, Beliefs and History read. P44(e): read in the Wayback copy (https://web.archive.org/web/20260705145639/https://www.britannica.com/topic/theosophy); live page not compared (live Britannica times out from the box).'
---

# Theosophy (THEOS)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

Theosophy is an 'occult movement originating in the 19th century with roots that can be traced to ancient Gnosticism and Neoplatonism' [S1].

## Core metaphysics

Monism with an impersonal transcendent God; emanation [S1].

## Position on the LIO axes

- A 2 (0.5, alt 3); B 3 (0.5, alt 2); D 1 (0.5, alt 2).
- C, E UNKNOWN.

## Schools and variants

TODO

## Science

TODO

## Coding guidance

Theosophical Society members.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> THEOS (25/50) — Theosophy. Theosophy scores moderately due to its ambitious syncretic approach to spiritual unity, balanced by unverified esoteric claims and reliance on revelation over empirical methods.

## Open questions

- Adherents are TODO.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7 (score E on the world's order when the stub is filled).
- 2026-10-15 (systems batch S11): read the listed sources; quotations checked word for word against the fetched page text. Britannica pages read in Wayback copies under P44(e); AI Top Questions not used.
- 2026-10-15 (S11 audit fix): B BELOW_THRESHOLD -> 3 @0.5 (alt 2).
