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
    summary: "Decision P7: E_scope note added. E is not scored in a stub; when it is, score it on the\
      \ world's order (same rules for every kind of being and event, no in-group exceptions in this-world\
      \ events). Salvation and moral community go on C_ledger."
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'Draft (systems batch S11, thin): filled from Britannica "Mandaeanism" (editors). A 1 (0.5,
      alt 0); B 1 (0.5); C, D, E UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from Britannica: family (Gnostic), origins, metaphysics (supreme deity,
      Archons, gnosis, baptism magic), practice, texts (Ginza, Book of John). Keep A=1 B=1; score D_authority
      1 (0.5) from gnosis/scripture; C E UNKNOWN.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Fill adherents/estimate gloss from existing sources (order-of-magnitude / qualitative). Axes
      unchanged.
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score C_ledger 1 (0.5) from Britannica Mandaeanism (soul salvation via gnosis; ascent past
      Archons). Deepen ethics/practice notes. E UNKNOWN.
identity:
  id: MANDAE
  v7_1_number: 65
  v7_1_label: Mandaeism
  display_label: Mandaeism
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: religion
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: 'Britannica: ancient Middle Eastern religion still surviving.'
  family:
    value: "Living Gnostic religion (mandayya 'having knowledge'); dualistic salvation by esoteric gnosis;\
      \ elaborate baptism cult"
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; dualism paragraph
    how_known: Britannica.
  parent_traditions:
    value:
    - Gnostic dualism (compared to Manichaeism)
    - Possible Babylonian / Iranian elements
    - 'Jewish affinities (OT familiarity, marriage ethic, purity, Hebrew angelology) — origin debated'
    certainty: 0.7
    cites:
    - source: S1
      locator: opening; origin debate
    how_known: Britannica; origins conjectural.
  related_codes:
  - code: ZORO
    relation: neighbor (easily confused)
    note: Iranian calendar/words noted; not Zoroastrianism
  - code: CHRIST
    relation: contrast case
    note: Jesus viewed as false messiah; John the Baptist revered
  - code: JUDA
    relation: neighbor (easily confused)
    note: affinities only
  - code: YAZID
    relation: neighbor (easily confused)
    note: both Middle Eastern minorities; different cosmologies
origins:
  founding_era:
    value: Beginnings usually dated somewhere in the first three centuries CE; origin highly conjectural
      (SW Mesopotamia vs Syro-Palestinian Nasorean exodus)
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  founding_region:
    value: 'Debated: southwestern Mesopotamia vs Syro-Palestine; surviving in Iraq and Khuzistan (SW Iran)'
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  founders_or_key_figures:
    value:
    - John the Baptist (revered; miracles of healing through baptism)
    - Hibil Ziwa (heavenly saviour in baptism text)
    - Nasoreans (priestly caste) vs Mandaiia (laity)
    certainty: 1.0
    cites:
    - source: S1
      locator: baptism; texts
    how_known: Britannica. Jesus rejected as false messiah.
  key_texts:
  - value: Ginza (Book of Adam) — cosmological treatise
    certainty: 1.0
    cites:
    - source: S1
      locator: texts
    how_known: Britannica.
  - value: Book of John — activities of John the Baptist
    certainty: 1.0
    cites:
    - source: S1
      locator: texts
    how_known: Britannica.
  - value: Book of the Zodiac — magical and astrological texts
    certainty: 1.0
    cites:
    - source: S1
      locator: texts
    how_known: Britannica.
  - value: Baptism of Hibil Ziwa — purification of the heavenly saviour
    certainty: 1.0
    cites:
    - source: S1
      locator: texts
    how_known: Britannica.
metaphysics:
  god_nature_relation:
    value: "Dualistic: supreme deity beyond heavenly spheres; evil Archons obstruct the soul's ascent\
      \ to reunion with the supreme deity."
    stance: creator distinct from creation
    certainty: 0.5
    cites:
    - source: S1
      locator: dualism paragraph
    how_known: "Supreme deity vs cosmos/Archons; 'creator' framing is coder gloss at 0.5."
  deity_personal:
    value: Supreme deity (personhood not fully stated); heavenly saviour Hibil Ziwa; Archons as rulers.
      John the Baptist as revered miracle-worker.
    stance: both / disputed
    certainty: 0.5
    cites:
    - source: S1
      locator: dualism; texts
    how_known: Personhood of supreme deity not stated (matches prior A note).
  intervention:
    value: 'Baptism as magical process giving immortality, purification, physical health; John performed
      miracles of healing through baptism.'
    stance: regular
    certainty: 0.7
    cites:
    - source: S1
      locator: baptism paragraph
    how_known: Britannica.
  miracles:
    value: Miracles of healing through baptism; baptism as magical process.
    stance: affirmed
    certainty: 1.0
    cites:
    - source: S1
      locator: baptism paragraph
    how_known: Britannica.
  petition_and_prayer:
    value: Elaborate cultic ritual especially baptism; petition theology not separately stated.
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S1
      locator: baptism paragraph
    how_known: Ritual clear; petition framing thin.
  afterlife:
    value: Salvation of the soul via gnosis; ascent through heavenly spheres past Archons to reunion with
      supreme deity; baptism gives immortality.
    stance: personal afterlife
    certainty: 0.7
    cites:
    - source: S1
      locator: dualism; baptism
    how_known: "Coder's reading of ascent/immortality language."
  moral_ledger:
    value: Not a clear reward/punishment ledger in Britannica; salvation via gnosis. Strong support for
      marriage and forbids sexual license.
    stance: none
    certainty: 0.5
    cites:
    - source: S1
      locator: dualism paragraph
    how_known: "Silence on karma/hell ledger; 'none' = not stated."
  authority:
    value: Esoteric gnosis of divine origin; sacred books (Ginza etc.); priestly Nasoreans. Revelation/gnosis
      over public observation.
    stance: revelation
    certainty: 0.7
    cites:
    - source: S1
      locator: opening; dualism; texts
    how_known: "Coder's reading."
  reserved_exemptions:
    value: Not addressed as physics exemptions.
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: full article
    how_known: Silence.
  teleology_in_nature:
    value: "Astrological Book of the Zodiac; not a designer's-purposes doctrine stated."
    stance: none
    certainty: 0.5
    cites:
    - source: S1
      locator: texts
    how_known: Thin.
  necessity_and_freedom:
    value: Not addressed.
    certainty: 1.0
    cites:
    - source: S1
      locator: full article
    how_known: Silence.
lio_axes:
  A_locus:
    value: 1
    rationale: "'evil Archons (rulers) obstruct the ascent of the soul through the heavenly spheres to\
      \ reunion with the supreme deity'."
    certainty: 0.5
    cites:
    - source: S1
      locator: dualism paragraph
    how_known: '0.5: supreme deity beyond spheres; personhood not stated. Alternative 0.'
    alternatives:
    - value: 0
      cites:
      - source: S1
        locator: dualism paragraph
      note: If supreme deity is read as fully transcendent personal pole.
  B_cause:
    value: 1
    rationale: "John the Baptist 'performed miracles of healing through baptism, which the Mandaeans viewed\
      \ as a magical process giving immortality, purification, and physical health'."
    certainty: 0.5
    cites:
    - source: S1
      locator: baptism paragraph
    how_known: '0.5.'
  C_ledger:
    value: 1
    certainty: 0.5
    cites:
    - source: S1
      locator: salvation; ascent
    how_known: '0.5 — salvation of soul via gnosis and ascent; not a simple earthly reward ledger.'
    rationale: 'C=1: personal/eschatological salvation frame with supreme deity reunion. Not 0: Britannica
      does not detail earthly reward/punishment judge.'
    alternatives:
    - value: 2
      note: Named alternative if weighting cultic purity rules as mixed ledger.
      cites:
      - source: S1
        locator: cultic
    - value: 'UNKNOWN'
      note: Named alternative if refusing score from thin ledger evidence.
      cites:
      - source: S1
        locator: opening
  D_authority:
    value: 1
    rationale: Esoteric gnosis and sacred books; priestly caste. Leans revelation; not scored 0 because
      magical/ritual knowledge is also practical.
    certainty: 0.5
    cites:
    - source: S1
      locator: dualism; texts
    how_known: New from authority stance; 0.5 with UNKNOWN alternative.
    alternatives:
    - value: 'UNKNOWN'
      cites:
      - source: S1
        locator: opening
      note: "If Gnostic 'knowledge' is judged not to fix D."
  E_scope:
    value: 'UNKNOWN'
    how_known: Priest/laity distinction and cultic purity do not clearly fix E under P7.
epistemology:
  value: "Salvation through esoteric knowledge (gnosis) of the soul's divine origin; sacred cosmological\
    \ and ritual texts; priestly Nasoreans vs laity."
  certainty: 1.0
  cites:
  - source: S1
    locator: opening; dualism
  how_known: Britannica.
ethics:
  value: Strongly supports marriage and forbids sexual license (unlike many Gnostic systems); Jewish-ethic
    parallels noted; cultic purity.
  certainty: 1.0
  cites:
  - source: S1
    locator: opening; dualism
  how_known: Britannica.
practice:
  ritual_and_practice:
    value: Elaborate baptismal cult; John the Baptist revered; Jesus as false messiah; cultic purity;
      marriage strongly supported
    certainty: 1.0
    cites:
    - source: S1
      locator: baptism; ethics
    how_known: Britannica.
  community_form:
    value: Surviving communities in Iraq and Khuzistan; Nasoreans (priests) vs Mandaiia (laity).
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
science:
  historical_stance:
    value: Magical and astrological texts (Book of the Zodiac); not a natural-science programme.
    certainty: 1.0
    cites:
    - source: S1
      locator: texts
    how_known: Britannica.
  current_stance:
    value: Not addressed.
    certainty: 1.0
    cites:
    - source: S1
      locator: full article
    how_known: Silence.
schools_and_variants:
- name: Nasoreans (priests) vs Mandaiia (laity)
  form: other
  how_it_differs: Priestly caste vs laity; same religion.
  lio_difference: Axes for the religion as a whole.
  certainty: 1.0
  cites:
  - source: S1
    locator: opening
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Living ethno-religious community (Iraq/Iran diaspora); Britannica no precise count in stub
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
  V: 4
  X: 2
  total: 23
  scoring_note: 'Mandaeism scores moderately low due to its esoteric gnostic focus and reliance on revelation
    over empirical methods, though it provides a unique framework for spiritual ascent and ethical living.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 65 and section 7 scoring notes'
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
  use_when: Mandaean / Sabian Mandaean identity or practice.
  do_not_use_when: Other Gnostic reconstructions without Mandaean identity. Christians who revere John
    — not MANDAE.
  neighbors:
  - code: CHRIST
    relation: neighbor (easily confused)
  - code: YAZID
    relation: neighbor (easily confused)
  - code: ZORO
    relation: neighbor (easily confused)
review:
  data_quality_flags:
  - 'Thin: short editors’ article.'
  open_questions:
  - A signed or peer-reviewed source.
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Britannica Editors
  citation: 'The Editors of Encyclopaedia Britannica. "Mandaeanism." Encyclopaedia Britannica. https://www.britannica.com/topic/Mandaeanism.
    Wayback Machine snapshot 2026-09-19 05:36:51 UTC: https://web.archive.org/web/20260919053651/https://www.britannica.com/topic/Mandaeanism.'
  url: 'https://www.britannica.com/topic/Mandaeanism'
  accessed: '2026-10-25'
  reliability_note: 'Unsigned editors’ article; full short article read. P44(e): read in the Wayback copy
    (https://web.archive.org/web/20260919053651/https://www.britannica.com/topic/Mandaeanism); live page
    not compared (live Britannica times out from the box).'
---
# Mandaeanism (MANDAE)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

Mandaeanism (from mandayya, 'having knowledge') is an 'ancient Middle Eastern religion still surviving in Iraq and Khuzistan', 'usually treated as a Gnostic sect' [S1].

## Core metaphysics

Dualistic: soul's ascent past evil Archons to supreme deity via gnosis [S1]. Elaborate baptism cult; John the Baptist revered; Jesus a false messiah [S1]. Marriage affirmed; sexual license forbidden [S1].

## Position on the LIO axes

- **A_locus: 1** (0.5; alt 0) — supreme deity beyond spheres [S1].
- **B_cause: 1** (0.5) — baptism as magical healing/immortality [S1].
- **C_ledger:** UNKNOWN.
- **D_authority: 1** (0.5; alt UNKNOWN) — gnosis and sacred books [S1].
- **E_scope:** UNKNOWN.

## Schools and variants

Nasoreans (priests) vs Mandaiia (laity) [S1].

## Science

Magical/astrological texts; not natural science [S1].

## Coding guidance

Living Mandaean identity.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> MANDAE (23/50) — Mandaeism. Mandaeism scores moderately low due to its esoteric gnostic focus and reliance on revelation over empirical methods, though it provides a unique framework for spiritual ascent and ethical living.

## Open questions

- Adherents.

## Research log

- 2026-10-15 (batch S11): Britannica Mandaeanism; A and B scored.
- 2026-10-25: deepened classification, origins, metaphysics, practice, texts; D_authority 1 (0.5). Re-read Britannica.
- 2026-10-25: adherents/estimate filled (qualitative).
- 2026-10-25: C_ledger scored; ritual_and_practice filled from Britannica.
