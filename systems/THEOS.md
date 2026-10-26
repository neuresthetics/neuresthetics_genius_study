---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 8
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
    summary: 'Draft (systems batch S11): filled from Britannica "Theosophy" (Melton). A 2 (0.5, alt 3);
      B BELOW_THRESHOLD; D 1 (0.5, alt 2); C, E UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S11 audit fix: B BELOW_THRESHOLD -> 3 @0.5 (alt 2).'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from Britannica Kids theosophy: Blavatsky/Olcott 1875, Secret Doctrine
      principles, reincarnation, Adyar. Keep prior axis scores.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Fill adherents/estimate gloss from existing sources (order-of-magnitude / qualitative). Axes
      unchanged.
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score C_ledger 3 (0.5) karma/reincarnation from sources on file (P44d). E UNKNOWN; A/B/D
      already scored.
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score E_scope 2 (0.5) from sources on file. Alternatives named.
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
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: Religious philosophy with mysticism; Society as NRM — 0.7 esoteric.
  family:
    value: "Theosophy ('divine wisdom'): modern form identified with the Theosophical Society (Blavatsky/Olcott,\
      \ 1875); eternal unknown principle, cycles, over-soul, reincarnation"
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; Secret Doctrine
    how_known: Britannica Kids.
  parent_traditions:
    value:
    - 'Ancient mystical/philosophical theosophy (Pythagoras, Plato, Plotinus Enneads)'
    - '19th-c. spiritualism milieu'
    - "Blavatsky's synthesis with Eastern thought"
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica Kids.
  related_codes:
  - code: ANTHRO
    relation: neighbor (easily confused)
    note: Steiner split from Theosophy
  - code: HERMET
    relation: neighbor (easily confused)
    note: different corpus
  - code: IDEAL
    relation: neighbor (easily confused)
    note: over-soul language ≠ automatic IDEAL
  - code: BUDDH
    relation: overlaps
    note: Society influenced Buddhist/Hindu revival per source
origins:
  founding_era:
    value: Theosophical Society founded 1875 in New York; Adyar base from 1878; Secret Doctrine 1888
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica Kids.
  founding_region:
    value: 'New York City founding; international HQ Adyar, India'
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica Kids.
  founders_or_key_figures:
    value:
    - Helena Petrovna Blavatsky
    - Henry Steel Olcott
    - Annie Besant (leader to 1933)
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica Kids.
  key_texts:
  - value: 'The Secret Doctrine (Blavatsky, 1888)'
    certainty: 1.0
    cites:
    - source: S1
      locator: Secret Doctrine
    how_known: Britannica Kids.
  - value: 'Plotinus, Enneads (ancient antecedent cited)'
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica Kids.
metaphysics:
  god_nature_relation:
    value: 'Eternal unchangeable principle about which no knowledge/speculation is possible; universe
      eternal with appearing/disappearing smaller universes; souls identified with over-soul, an aspect
      of the unknown principle.'
    stance: God in Nature and beyond it
    certainty: 0.5
    cites:
    - source: S1
      locator: Secret Doctrine
    how_known: Unknown principle + over-soul; stance 0.5.
  deity_personal:
    value: Unknown principle beyond speculation; spiritual reality that may be called God — leans impersonal
      Absolute.
    stance: impersonal
    certainty: 0.5
    cites:
    - source: S1
      locator: opening; Secret Doctrine
    how_known: '0.5.'
  intervention:
    value: Not a personal intervention doctrine in this short article; mystical experience of spiritual
      reality.
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: Silence on miracles/intervention.
  miracles:
    value: Investigation of mysterious laws and unknown powers claimed as a Society goal; not a miracle
      affirmation doctrine.
    stance: not addressed
    certainty: 0.5
    cites:
    - source: S1
      locator: goals
    how_known: '0.5.'
  petition_and_prayer:
    value: 'Meditation, revelation, intuition beyond normal consciousness — contemplative more than petition.'
    stance: contemplative only
    certainty: 0.5
    cites:
    - source: S1
      locator: mysticism
    how_known: '0.5.'
  afterlife:
    value: Series of rebirths/reincarnations; soul continues quest for spiritual growth.
    stance: rebirth
    certainty: 1.0
    cites:
    - source: S1
      locator: Secret Doctrine
    how_known: Britannica Kids.
  moral_ledger:
    value: Rebirth tied to spiritual growth quest; karma not named in this short article.
    stance: impersonal consequence
    certainty: 0.5
    cites:
    - source: S1
      locator: Secret Doctrine
    how_known: '0.5 without explicit karma word.'
  authority:
    value: "Founder Blavatsky's Secret Doctrine; Society leadership (Olcott, Besant); mystical experience\
      \ beyond normal consciousness."
    stance: 'both, revelation first'
    certainty: 0.5
    cites:
    - source: S1
      locator: opening; Secret Doctrine
    how_known: '0.5 founder + mysticism.'
  reserved_exemptions:
    value: Not addressed.
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: Silence.
  teleology_in_nature:
    value: Cyclic universes; spiritual growth through rebirth — cosmic process more than designer purposes.
    stance: immanent ends
    certainty: 0.5
    cites:
    - source: S1
      locator: Secret Doctrine
    how_known: '0.5.'
  necessity_and_freedom:
    value: Soul obliged to go through series of rebirths — necessity language; free will not developed.
    certainty: 0.5
    cites:
    - source: S1
      locator: Secret Doctrine
    how_known: Thin.
lio_axes:
  A_locus:
    value: 2
    rationale: "Monism: 'an overarching, all-encompassing unity that subsumes all differentiation', with\
      \ 'God is utterly transcendent and impersonal' and creation as 'spiritual emanations from God'."
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
    rationale: "The 'higher psychic and spiritual powers' are studied under the Third Object, 'to investigate\
      \ unexplained laws of Nature and the powers latent in human beings'; the 'fascination with supernatural\
      \ or other extraordinary occurrences' is framed as unexplained law, not exemption."
    certainty: 0.5
    cites: &id002
    - source: S1
      locator: Beliefs
    - source: S1
      locator: History
    how_known: '0.5: the movement’s agreed position (S11 audit); Blavatsky’s phenomena from the Masters
      give alternative 2.'
    alternatives:
    - value: 2
      note: Named alternative.
      cites: *id002
  C_ledger:
    value: 3
    certainty: 0.5
    cites:
    - source: S1
      locator: karma; reincarnation
    how_known: '0.5 — karma/reincarnation as impersonal moral-causal law (P44d).'
    rationale: 'C=3: impersonal ledger. Alternative 1 if Masters as personal judges.'
    alternatives:
    - value: 1
      note: Named alternative if coding Masters/Hierarchy as personal judges.
      cites:
      - source: S1
        locator: opening
  D_authority:
    value: 1
    rationale: "Contact with spiritual reality 'through intuition, meditation, revelation, or some other\
      \ state transcending normal human consciousness'; Blavatsky claimed 'regular contact with a brotherhood\
      \ of Great Masters'."
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
    value: 2
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — root races / Masters hierarchy; esoteric grades'
    rationale: E=2 at 0.5.
    alternatives:
    - value: 1
      note: Named alternative for stronger in-group occultism.
      cites:
      - source: S1
        locator: opening
epistemology:
  value: 'Mystical experience of spiritual reality via meditation, revelation, intuition; study of comparative
    religion, philosophy, science; investigate mysterious laws and unknown powers.'
  certainty: 1.0
  cites:
  - source: S1
    locator: mysticism; goals
  how_known: Britannica Kids.
ethics:
  value: Form a nucleus of the universal brotherhood of humanity (Society goal).
  certainty: 1.0
  cites:
  - source: S1
    locator: goals
  how_known: Britannica Kids.
practice:
  ritual_and_practice:
    value: Not detailed as ritual system in this short article; Society organizational and study focus.
    certainty: 0.7
    cites:
    - source: S1
      locator: goals
    how_known: Silence on liturgy.
  community_form:
    value: Theosophical Society; international HQ Adyar; small membership but influential.
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica Kids.
science:
  historical_stance:
    value: Society goal includes study of science alongside religion/philosophy; investigate mysterious
      laws of nature.
    certainty: 1.0
    cites:
    - source: S1
      locator: goals
    how_known: Britannica Kids.
  current_stance:
    value: Not addressed beyond historical Society goals.
    certainty: 0.7
    cites:
    - source: S1
      locator: goals
    how_known: Thin.
schools_and_variants:
- name: Theosophical Society (Adyar)
  form: modern
  how_it_differs: Blavatsky/Olcott/Besant institutional line.
  lio_difference: Prior THEOS scores.
  certainty: 1.0
  cites:
  - source: S1
    locator: opening
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Theosophical Society historical membership; modern remnant societies; not a mass religion
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — qualitative from listed source; not a genius-rate denominator.'
v7_1_rubric:
  label: authorial v7.1 scores
  L: 7
  P: 6
  E: 4
  V: 5
  X: 3
  total: 25
  scoring_note: 'Theosophy scores moderately due to its ambitious syncretic approach to spiritual unity,
    balanced by unverified esoteric claims and reliance on revelation over empirical methods.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 63 and section 7 scoring notes'
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
  use_when: Theosophical Society / Blavatsky theosophy identity.
  do_not_use_when: "Anthroposophy (ANTHRO). Generic 'divine wisdom' mysticism without Society link."
  neighbors:
  - code: ANTHRO
    relation: neighbor (easily confused)
  - code: HERMET
    relation: neighbor (easily confused)
review:
  data_quality_flags: []
  open_questions:
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: J. Gordon Melton
  citation: 'Melton, J. Gordon. "Theosophy." Encyclopaedia Britannica. https://www.britannica.com/topic/theosophy.
    Wayback Machine snapshot 2026-07-05 14:56:39 UTC: https://web.archive.org/web/20260705145639/https://www.britannica.com/topic/theosophy.'
  url: 'https://www.britannica.com/topic/theosophy'
  accessed: '2026-10-25'
  reliability_note: 'Signed article (historian of American religion); introduction, Beliefs and History
    read. P44(e): read in the Wayback copy (https://web.archive.org/web/20260705145639/https://www.britannica.com/topic/theosophy);
    live page not compared (live Britannica times out from the box).'
---
# Theosophy (THEOS)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

Modern theosophy is largely identified with the Theosophical Society (1875, Blavatsky and Olcott); 'divine wisdom'; Secret Doctrine principles include an unknowable eternal principle, cyclic universes, over-soul, reincarnation [S1].

## Core metaphysics

Unknown principle; over-soul; obligatory rebirths for spiritual growth [S1].

## Position on the LIO axes

Prior scores kept (see YAML).

## Schools and variants

Theosophical Society (Adyar) [S1].

## Science

Society goals include studying science and mysterious laws of nature [S1].

## Coding guidance

Blavatsky/Society theosophy. Not ANTHRO.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> THEOS (25/50) — Theosophy. Theosophy scores moderately due to its ambitious syncretic approach to spiritual unity, balanced by unverified esoteric claims and reliance on revelation over empirical methods.

## Open questions

- Fuller Secret Doctrine axis pass if Jason wants score moves.

## Research log

- 2026-10-15 (batch S11): Britannica theosophy; axes set.
- 2026-10-25: deepened from Britannica Kids theosophy article. Axes kept.
- 2026-10-25: adherents/estimate filled (qualitative).
- 2026-10-25: C_ledger scored 3 (0.5).
- 2026-10-25: E_scope scored 2 (0.5).
