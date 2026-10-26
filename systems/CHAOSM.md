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
    summary: 'Draft (systems batch S10, P45 lower tier): filled from Meletiadis, Aries 2025 (peer-reviewed).
      A, B BELOW_THRESHOLD; rest UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from Encyclopedia.com Chaos Magick: Spare/Sherwin/Carroll, belief-as-tool,
      sigils, IOT 1977, no objective gods. Keep A/B BELOW_THRESHOLD; C D E UNKNOWN.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Fill adherents/estimate gloss from existing sources (order-of-magnitude / qualitative). Axes
      unchanged.
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score A4 D4 C4 (0.7) from Britannica/Chaos Magick materials on file (no objective gods; practitioner-designed
      ritual). B stays BELOW.
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Fill implied axes (E=4@0.5) from sources on file / P44(c) where naturalistic. Alternatives
      named.'
identity:
  id: CHAOSM
  v7_1_number: 59
  v7_1_label: Chaos Magick
  display_label: Chaos Magick
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: esoteric or occult tradition
    certainty: 1.0
    cites:
    - source: S2
      locator: opening
    how_known: 'Encyclopedia.com: form of magical practice.'
  family:
    value: 'Chaos Magick: modern magical practice treating belief as tool; order as imposed; power from
      subconscious; sigil magic; IOT'
    certainty: 1.0
    cites:
    - source: S2
      locator: opening
    how_known: Encyclopedia.com.
  parent_traditions:
    value:
    - "Austin Osman Spare's sigil magic / critique of ceremonial magic"
    - Thelemic milieu as the dominance being reacted against
    - 'Eastern notions (Brahman, Tao, Atman=Brahman) as analogies'
    certainty: 1.0
    cites:
    - source: S2
      locator: opening
    how_known: Encyclopedia.com.
  related_codes:
  - code: THELEM
    relation: neighbor (easily confused)
    note: Chaos Magick developed against Thelemic dominance
  - code: WICCA
    relation: neighbor (easily confused)
    note: different Neo-Pagan/occult stream
  - code: HERMET
    relation: neighbor (easily confused)
    note: rejects traditional ceremonial surplus
origins:
  founding_era:
    value: England 1960s informal Circle of Chaos; IOT founded 1977; Carroll Liber Null / Psychonaut later
      1980s
    certainty: 1.0
    cites:
    - source: S2
      locator: opening; IOT
    how_known: Encyclopedia.com.
  founding_region:
    value: England; IOT contact London
    certainty: 1.0
    cites:
    - source: S2
      locator: IOT
    how_known: Encyclopedia.com.
  founders_or_key_figures:
    value:
    - Austin Osman Spare (forerunner)
    - Ray Sherwin (originator of chaos magical theory per entry)
    - 'Peter J. Carroll (Liber Null, Psychonaut, IOT rituals)'
    certainty: 1.0
    cites:
    - source: S2
      locator: opening
    how_known: Encyclopedia.com.
  key_texts:
  - value: Book of Results; Theatre of Magick (Sherwin)
    certainty: 1.0
    cites:
    - source: S2
      locator: IOT
    how_known: Encyclopedia.com.
  - value: 'Liber Null & Psychonaut (Carroll, 1987)'
    certainty: 1.0
    cites:
    - source: S2
      locator: sources
    how_known: Encyclopedia.com.
  - value: Liber Null editions studied in Meletiadis 2025 (peer-reviewed; P45 cap 0.5)
    certainty: 0.5
    cites:
    - source: S1
      locator: full article
    how_known: Prior P45 journal source kept.
metaphysics:
  god_nature_relation:
    value: No objective gods/demons; chaos as Order beyond understanding (analogous to Brahman/Tao); universe
      one vast everchanging whole.
    stance: no God
    certainty: 0.5
    cites:
    - source: S2
      locator: opening
    how_known: No objective gods; 0.5 vs mystical Absolute reading.
  deity_personal:
    value: Do not believe in gods or demons with objective existence; images from popular culture for
      ritual drama.
    stance: no deity
    certainty: 0.7
    cites:
    - source: S2
      locator: opening
    how_known: Encyclopedia.com.
  intervention:
    value: Power from subconscious discharged via ritual drama; not external deity intervention.
    stance: none
    certainty: 0.5
    cites:
    - source: S2
      locator: opening
    how_known: '0.5 — magical efficacy without gods.'
  miracles:
    value: Magical results via sigils/will; not theistic miracles.
    stance: reinterpreted as natural
    certainty: 0.5
    cites:
    - source: S2
      locator: opening
    how_known: '0.5 subconscious-natural reading.'
  petition_and_prayer:
    value: Not petition to gods; inner-self exercises and self-designed ritual.
    stance: no petition
    certainty: 0.7
    cites:
    - source: S2
      locator: opening
    how_known: Encyclopedia.com.
  afterlife:
    value: Not addressed.
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S2
      locator: opening
    how_known: Silence.
  moral_ledger:
    value: Not addressed.
    stance: none
    certainty: 0.7
    cites:
    - source: S2
      locator: opening
    how_known: Silence.
  authority:
    value: "Practitioner's subconscious / own designed ritual; Spare/Sherwin/Carroll texts; IOT as optional\
      \ org."
    stance: observation and reason
    certainty: 0.5
    cites:
    - source: S2
      locator: opening
    how_known: Experimental/inner; 0.5 vs founder texts.
  reserved_exemptions:
    value: Not addressed.
    stance: none
    certainty: 0.7
    cites:
    - source: S2
      locator: opening
    how_known: Silence.
  teleology_in_nature:
    value: Order imposed; chaos as Order beyond understanding — not designer teleology.
    stance: none
    certainty: 0.5
    cites:
    - source: S2
      locator: opening
    how_known: '0.5.'
  necessity_and_freedom:
    value: Not addressed as free-will thesis.
    certainty: 1.0
    cites:
    - source: S2
      locator: opening
    how_known: Silence.
lio_axes:
  A_locus:
    value: 4
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: '0.7 — no objective gods/demons; images as ritual drama; P44a.'
    rationale: 'A=4: no transcendent personal God with objective existence. Was BELOW; stance itself fixes
      absence.'
    alternatives:
    - value: 'BELOW_THRESHOLD'
      note: Named alternative if coding practitioners who treat chaos as deity-like.
      cites:
      - source: S1
        locator: opening
  B_cause:
    value: 'BELOW_THRESHOLD'
    how_known: "Carroll's definitions conflict: 'Magic may be defined as the science and art of willed\
      \ change in perception', yet elsewhere 'magic is change, any change, which includes effects on the\
      \ natural environment' (Meletiadis's reading, S1)."
    note: Alternatives 1 and 3. P45 cap.
  C_ledger:
    value: 4
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — not addressed; implied none (P44c-style for no-spiritual-judge forms).'
    rationale: C=4 implied none. Certainty 0.5.
    alternatives:
    - value: 'UNKNOWN'
      note: Named alternative if refusing implied score.
      cites:
      - source: S1
        locator: opening
  D_authority:
    value: 4
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: '0.7 — practitioner’s subconscious / own designed ritual; stance observation and reason.'
    rationale: 'D=4: self-designed method over revelation. Not 3: no church scripture as primary.'
    alternatives:
    - value: 2
      note: Named alternative if weighting Spare/Carroll lineage texts as tradition.
      cites:
      - source: S1
        locator: opening
  E_scope:
    value: 4
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — no objective gods; implied same chaos/order.'
    rationale: E=4 at 0.5.
    alternatives:
    - value: 'UNKNOWN'
      note: Named alternative if refusing P44(c) implied score.
      cites:
      - source: S1
        locator: opening
epistemology:
  value: Universe intuited not defined; belief as tool; direct experience/knowledge of Atman=Brahman analogy;
    experimental practice.
  certainty: 1.0
  cites:
  - source: S2
    locator: opening
  how_known: Encyclopedia.com.
ethics:
  value: Not a single ethical system in this entry.
  certainty: 1.0
  cites:
  - source: S2
    locator: opening
  how_known: Silence.
practice:
  ritual_and_practice:
    value: Sigils; self-designed provocative ritual as drama to arouse subconscious; basic inner-self
      exercises; IOT rituals in Liber Null.
    certainty: 1.0
    cites:
    - source: S2
      locator: opening; IOT
    how_known: Encyclopedia.com.
  community_form:
    value: Informal Circle of Chaos (1960s); Initiates of Thanateros (IOT) 1977; also solitary practice
      implied.
    certainty: 1.0
    cites:
    - source: S2
      locator: IOT
    how_known: Encyclopedia.com.
science:
  historical_stance:
    value: Science (like religion) seen as imposed order-system that dismisses the uncontrollable; chaos
      beyond categories.
    certainty: 0.7
    cites:
    - source: S2
      locator: opening
    - source: S1
      locator: Liber Null focus
    how_known: Encyclopedia.com.
  current_stance:
    value: Not a science program; experimental magical method.
    certainty: 0.7
    cites:
    - source: S2
      locator: opening
    how_known: Coder reading.
schools_and_variants:
- name: IOT (Illuminates/Initiates of Thanateros)
  form: modern
  how_it_differs: Formal org from 1977; Carroll Liber Null rituals.
  lio_difference: A/B BELOW_THRESHOLD umbrella.
  certainty: 1.0
  cites:
  - source: S2
    locator: IOT
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Chaos magic practitioners; occult subculture; no census
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
  scoring_note: 'Chaos Magick scores moderately due to its innovative, flexible approach to personal empowerment
    and magick, balanced by subjective elements that reduce empirical and predictive strength.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 59 and section 7 scoring notes'
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
  use_when: Chaos Magick / IOT / Carroll-Sherwin-Spare chaos magical identity.
  do_not_use_when: Thelema (THELEM). Generic ceremonial magic without chaos method.
  neighbors:
  - code: THELEM
    relation: neighbor (easily confused)
  - code: WICCA
    relation: neighbor (easily confused)
review:
  data_quality_flags:
  - 'P45 lower tier only: one peer-reviewed article centred on the early editions of Liber Null. Capped
    at 0.5.'
  open_questions:
  - A survey of the whole current (post-1990s).
  - Adherents are TODO.
sources:
- id: S1
  type: secondary
  kind: journal article
  author: Vasileios M. Meletiadis
  citation: 'Meletiadis, Vasileios M. "“Book Zero” through the Years." Aries 25, no. 1 (2025): 25–55.
    https://doi.org/10.1163/15700593-tat00004. Read in Wayback snapshot 2026-10-12 03:44:54 UTC: https://web.archive.org/web/20261012034454/https://brill.com/view/journals/arie/25/1/article-p25_2.xml.'
  url: 'https://doi.org/10.1163/15700593-tat00004'
  accessed: '2026-10-25'
  reliability_note: 'P45 lower tier (b): peer-reviewed scholarship defining the current; claims capped
    at 0.5. No encyclopedia entry found. The study centres on the 1978 and 1981 editions of Carroll’s
    Liber Null. Crossref gives online publication 2023-08-17.'
- id: S2
  type: secondary
  kind: encyclopedia
  url: 'https://www.encyclopedia.com/science/encyclopedias-almanacs-transcripts-and-maps/chaos-magick'
  accessed: '2026-10-25'
  citation: 'Encyclopedia.com. "Chaos Magick." Accessed 2026-10-25. https://www.encyclopedia.com/science/encyclopedias-almanacs-transcripts-and-maps/chaos-magick.'
---
# Chaos Magick (CHAOSM)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

Chaos Magick is a modern magical practice (England 1960s–) treating belief as a tool, denying objective gods, locating power in the subconscious; Spare forerunner, Sherwin/Carroll, IOT 1977 [S2].

## Core metaphysics

Chaos as Order beyond understanding; no objective deities; ritual as drama [S2].

## Position on the LIO axes

- **A, B:** BELOW_THRESHOLD (prior).
- **C, D, E:** UNKNOWN.

## Schools and variants

IOT; informal Circle of Chaos [S2].

## Science

Science as imposed order-system [S2].

## Coding guidance

Chaos Magick identity. Not THELEM.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> CHAOSM (25/50) — Chaos Magick. Chaos Magick scores moderately due to its innovative, flexible approach to personal empowerment and magick, balanced by subjective elements that reduce empirical and predictive strength.

## Open questions

- Whether D could move from UNKNOWN to observation-and-reason at 0.5 — left UNKNOWN (P44).

## Research log

- Prior: DOI/source batch; A/B BELOW_THRESHOLD.
- 2026-10-25: deepened from Encyclopedia.com Chaos Magick (S2). Axes kept.
- 2026-10-25: adherents/estimate filled (qualitative).
- 2026-10-25: A/D/C scored.
- 2026-10-25: implied axis fill: E=4@0.5.
