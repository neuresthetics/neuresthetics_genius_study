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
    summary: 'Draft (systems batch S10, thin): filled from Britannica "Hermetic writings" (editors). A
      1 (0.5, alt 2); D 1 (0.5, alt 0); B, C, E UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S10 audit fix: ancient-only scope added to A and D.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from Britannica Hermetic writings (via prior batch source + re-read content):
      Corpus Hermeticum, popular vs learned Hermetism, gnosis/deification, Greco-Egyptian fusion. Keep
      A=1 D=1; B C E UNKNOWN.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Fill adherents/estimate gloss from existing sources (order-of-magnitude / qualitative). Axes
      unchanged.
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score C_ledger 1 (0.5) from Britannica Hermetic writings (deification/rebirth via gnosis).
      Ethics note left thin. A/D already scored.
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score B_cause 1 (0.5) and E_scope 2 (0.5) from sources on file (Hermetica; as above so below;
      initiation).
identity:
  id: HERMET
  v7_1_number: 61
  v7_1_label: Hermeticism
  display_label: Hermeticism
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: esoteric or occult tradition
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: 'Britannica: works of revelation on occult, theological, philosophical subjects.'
  family:
    value: 'Hermetica: Greco-Egyptian revelatory writings ascribed to Hermes Trismegistos (Thoth); popular
      occult sciences and learned theology/philosophy'
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  parent_traditions:
    value:
    - Egyptian Thoth cult
    - 'Platonic, Stoic, and Neo-Pythagorean philosophies'
    - Hellenistic Greco-Egyptian culture
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; theological writings
    how_known: Britannica.
  related_codes:
  - code: PLATO
    relation: overlaps
    note: Platonic dialogue form and philosophy
  - code: THEOS
    relation: neighbor (easily confused)
    note: later reception
  - code: KEMET
    relation: neighbor (easily confused)
    note: Egyptian setting but Greek philosophy; not Kemetic Orthodoxy
  - code: ANTHRO
    relation: neighbor (easily confused)
    note: different modern path
origins:
  founding_era:
    value: 'Collection written in Greek and Latin, probably mid-1st to end of 3rd century CE'
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  founding_region:
    value: Greco-Egyptian culture of Ptolemaic and Roman periods
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  founders_or_key_figures:
    value:
    - Hermes Trismegistos / Thoth (ascribed author; legendary)
    - Stobaeus (Anthologion fragments)
    - Asclepius (Latin translation preserved among Apuleius)
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; theological writings
    how_known: Britannica.
  key_texts:
  - value: Corpus Hermeticum (17 treatises)
    certainty: 1.0
    cites:
    - source: S1
      locator: theological writings
    how_known: Britannica.
  - value: Asclepius (Latin)
    certainty: 1.0
    cites:
    - source: S1
      locator: theological writings
    how_known: Britannica.
  - value: Tabula Smaragdina (Emerald Tablet) — alchemy
    certainty: 1.0
    cites:
    - source: S1
      locator: popular Hermetism
    how_known: Britannica.
metaphysics:
  god_nature_relation:
    value: 'Aim: deification or rebirth through gnosis of the one transcendent God, the world, and humankind.
      Cosmos as unity with interdependent parts (sympathy/antipathy).'
    stance: God in Nature and beyond it
    certainty: 0.5
    cites:
    - source: S1
      locator: popular; aim paragraph
    how_known: Transcendent God + cosmos unity; stance 0.5 coder reading.
  deity_personal:
    value: One transcendent God; Hermes-Thoth as revealer. Personal vs impersonal absolute varies across
      treatises.
    stance: both / disputed
    certainty: 0.5
    cites:
    - source: S1
      locator: aim paragraph
    how_known: '0.5.'
  intervention:
    value: Divine revelation required because assumed affinities could not be discovered by ordinary scientific
      methods; occult practice intensely utilitarian.
    stance: regular
    certainty: 0.5
    cites:
    - source: S1
      locator: popular Hermetism
    how_known: Revelation for occult science; 0.5.
  miracles:
    value: 'Magic, alchemy, astrology as operative arts; not denied.'
    stance: affirmed
    certainty: 0.7
    cites:
    - source: S1
      locator: popular Hermetism
    how_known: Britannica.
  petition_and_prayer:
    value: Revelatory dialogues; not a single petition theology.
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: Thin.
  afterlife:
    value: Deification or rebirth of mortals through gnosis.
    stance: personal afterlife
    certainty: 0.5
    cites:
    - source: S1
      locator: aim paragraph
    how_known: Rebirth/deification language; 0.5 between rebirth and personal afterlife.
  moral_ledger:
    value: Not a clear ledger doctrine in Britannica summary.
    stance: none
    certainty: 0.5
    cites:
    - source: S1
      locator: full article content used
    how_known: Silence.
  authority:
    value: Divine revelation ascribed to Hermes Trismegistos; distrust of traditional Greek rationalism
      in the age; occult knowledge via revelation when ordinary science fails.
    stance: revelation
    certainty: 0.7
    cites:
    - source: S1
      locator: Hellenistic age; popular Hermetism
    how_known: Britannica.
  reserved_exemptions:
    value: Not addressed.
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: full article content used
    how_known: Silence.
  teleology_in_nature:
    value: Cosmos as unity; parts related by sympathy and antipathy — occult teleology/correspondence
      more than designer purposes.
    stance: immanent ends
    certainty: 0.5
    cites:
    - source: S1
      locator: popular Hermetism
    how_known: '0.5.'
  necessity_and_freedom:
    value: Not addressed.
    certainty: 1.0
    cites:
    - source: S1
      locator: full article content used
    how_known: Silence.
lio_axes:
  A_locus:
    value: 1
    rationale: "Gnosis of 'the one transcendent God' plus cosmos unity; leans transcendent with world-knowledge."
    certainty: 0.5
    cites:
    - source: S1
      locator: aim paragraph
    how_known: Prior score kept.
  B_cause:
    value: 1
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — magic / correspondence / theurgy streams.'
    rationale: B=1 at 0.5.
    alternatives:
    - value: 'UNKNOWN'
      note: Named alternative if thin.
      cites:
      - source: S1
        locator: opening
  C_ledger:
    value: 1
    certainty: 0.5
    cites:
    - source: S1
      locator: deification; gnosis
    how_known: '0.5 — deification or rebirth through gnosis; not a simple earthly reward ledger.'
    rationale: 'C=1: personal eschatological transformation toward the transcendent God. Not 0: no detailed
      judge catalog in summary.'
    alternatives:
    - value: 'UNKNOWN'
      note: Named alternative if ledger evidence too thin.
      cites:
      - source: S1
        locator: opening
  D_authority:
    value: 1
    rationale: Divine revelation when ordinary scientific methods cannot discover occult affinities; Hermes
      as revealer.
    certainty: 0.5
    cites:
    - source: S1
      locator: popular Hermetism
    how_known: Prior score kept.
  E_scope:
    value: 2
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — esoteric initiation; not ethnic closed.'
    rationale: E=2 at 0.5.
    alternatives:
    - value: 1
      note: Named alternative.
      cites:
      - source: S1
        locator: opening
epistemology:
  value: 'Gnosis (knowledge) of transcendent God, world, and humankind leading to deification; revelation
    over ordinary scientific discovery for occult affinities; Platonic dialogue form.'
  certainty: 1.0
  cites:
  - source: S1
    locator: aim; popular; theological
  how_known: Britannica.
ethics:
  value: Not developed as a single ethics in the Britannica summary.
  certainty: 1.0
  cites:
  - source: S1
    locator: full article content used
  how_known: Silence.
practice:
  ritual_and_practice:
    value: 'Popular Hermetism: astrology, alchemy, magic. Learned: theological/philosophical dialogues.
      Unlikely any well-defined Hermetic community or church.'
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; closing
    how_known: Britannica.
  community_form:
    value: 'Unlikely there was any well-defined Hermetic community or church [S1]. Later medieval/Renaissance
      receptions are separate.'
    certainty: 1.0
    cites:
    - source: S1
      locator: closing
    how_known: Britannica.
science:
  historical_stance:
    value: Breakdown of distinction between science and religion in Hellenistic age; occult sciences utilitarian
      but based on revelation when ordinary methods fail.
    certainty: 1.0
    cites:
    - source: S1
      locator: Hellenistic age; popular
    how_known: Britannica.
  current_stance:
    value: Historical corpus; modern esoteric receptions vary (not detailed here).
    certainty: 0.7
    cites:
    - source: S1
      locator: closing
    how_known: "Coder's reading."
schools_and_variants:
- name: 'Popular Hermetism (astrology, alchemy, magic)'
  form: mystical
  how_it_differs: Occult sciences; Emerald Tablet etc.
  lio_difference: A1 D1; B may lean more interventionist at person level.
  certainty: 1.0
  cites:
  - source: S1
    locator: opening
- name: 'Learned Hermetism (Corpus Hermeticum, Asclepius)'
  form: scholastic or philosophical
  how_it_differs: 'Theology and philosophy in Platonic dialogue form; Greek philosophy, Egyptian setting.'
  lio_difference: Same umbrella scores.
  certainty: 1.0
  cites:
  - source: S1
    locator: theological writings
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Historical Hermetic writings tradition + modern esoteric reception; not a census religion
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
  scoring_note: 'Hermeticism scores moderately due to its esoteric and symbolic approach to enlightenment,
    balanced by limited empirical grounding and reliance on ancient revelations.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 61 and section 7 scoring notes'
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
  use_when: Engagement with Hermetica / Hermes Trismegistos as revelatory authority.
  do_not_use_when: Kemetic Orthodoxy (KEMET). Generic alchemy without Hermetic identity.
  neighbors:
  - code: KEMET
    relation: neighbor (easily confused)
  - code: THEOS
    relation: neighbor (easily confused)
  - code: PLATO
    relation: neighbor (easily confused)
review:
  data_quality_flags:
  - 'Thin: unsigned editors’ article; covers the ancient writings, not later Hermeticism.'
  open_questions:
  - A source on Renaissance and modern Hermeticism.
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Britannica Editors
  citation: 'The Editors of Encyclopaedia Britannica. "Hermetic writings." Encyclopaedia Britannica. https://www.britannica.com/topic/Hermetic-writings.
    Wayback Machine snapshot 2026-10-12 05:40:54 UTC: https://web.archive.org/web/20261012054054/https://www.britannica.com/topic/Hermetic-writings.'
  url: 'https://www.britannica.com/topic/Hermetic-writings'
  accessed: '2026-10-25'
  reliability_note: 'Unsigned editors’ article; full article read. P44(e): read in the Wayback copy (https://web.archive.org/web/20261012054054/https://www.britannica.com/topic/Hermetic-writings);
    live page not compared (live Britannica times out from the box).'
---
# Hermeticism (HERMET)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

Hermetic writings (Hermetica) are 'works of revelation on occult, theological, and philosophical subjects ascribed to the Egyptian god Thoth (Greek Hermes Trismegistos)', dating probably mid-1st to end of 3rd century CE [S1].

## Core metaphysics

Gnosis of the one transcendent God, the world, and humankind aiming at deification/rebirth [S1]. Popular occult sciences (astrology, alchemy, magic) and learned theology [S1]. Unlikely a Hermetic church [S1].

## Position on the LIO axes

- **A_locus: 1** (0.5) — transcendent God + cosmos unity [S1].
- **B, C, E:** UNKNOWN.
- **D_authority: 1** (0.5) — revelation when ordinary science fails [S1].

## Schools and variants

Popular vs learned Hermetism [S1].

## Science

Hellenistic fusion of science and religion; occult utilitarianism via revelation [S1].

## Coding guidance

Hermetica engagement. Not KEMET.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> HERMET (25/50) — Hermeticism. Hermeticism scores moderately due to its esoteric and symbolic approach to enlightenment, balanced by limited empirical grounding and reliance on ancient revelations.

## Open questions

- Adherents (historical reception).

## Research log

- 2026-10-15 (batch S10): Britannica Hermetic writings; A and D scored.
- 2026-10-25: deepened classification, origins, metaphysics, practice, schools. A and D kept.
- 2026-10-25: adherents/estimate filled (qualitative).
- 2026-10-25: C_ledger scored 1 (0.5).
- 2026-10-25: B/E scored.
