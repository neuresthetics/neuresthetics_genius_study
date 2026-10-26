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
    summary: 'Decision P7: E_scope note added. E is not scored in a stub; when it is, score it on the
      world''s order (same rules for every kind of being and event, no in-group exceptions in this-world
      events). Salvation and moral community go on C_ledger.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'Draft (systems batch S10, thin): filled from Britannica "Anthroposophy" (editors, one paragraph).
      D BELOW_THRESHOLD; rest UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S10 audit fix: D BELOW_THRESHOLD -> 1 @0.5 (alt 2).'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from short Britannica: family, Steiner, spiritual worlds via enhanced consciousness,
      Anthroposophical Society 1912 Dornach. Keep D=1; other axes UNKNOWN (article very short).'
identity:
  id: ANTHRO
  v7_1_number: 58
  v7_1_label: Anthroposophy
  display_label: Anthroposophy
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: esoteric or occult tradition
    certainty: 0.7
    cites:
    - source: S1
      locator: full article
    how_known: 'Britannica: philosophy of contacting spiritual worlds; Society. 0.7 between philosophy
      and esoteric.'
  family:
    value: 'Rudolf Steiner''s anthroposophy: human intellect can contact spiritual worlds; enhanced consciousness
      perceives spiritual worlds independent of the senses'
    certainty: 1.0
    cites:
    - source: S1
      locator: full article
    how_known: Britannica.
  parent_traditions:
    value:
    - Rudolf Steiner's synthesis (Austrian philosopher, scientist, artist)
    - Earlier Theosophical milieu (historical context; not detailed in this short article)
    certainty: 0.5
    cites:
    - source: S1
      locator: full article
    how_known: Steiner named; Theosophy link not in this Britannica blurb — 0.5.
  related_codes:
  - code: THEOS
    relation: neighbor (easily confused)
    note: Steiner's path diverged from Theosophy; use ANTHRO for anthroposophy
  - code: HERMET
    relation: neighbor (easily confused)
    note: different corpus
  - code: IDEAL
    relation: neighbor (easily confused)
    note: spiritual worlds ≠ automatic IDEAL
origins:
  founding_era:
    value: Anthroposophical Society founded 1912
    certainty: 1.0
    cites:
    - source: S1
      locator: full article
    how_known: Britannica.
  founding_region:
    value: Europe; Society now based in Dornach, Switzerland, with branches worldwide
    certainty: 1.0
    cites:
    - source: S1
      locator: full article
    how_known: Britannica.
  founders_or_key_figures:
    value:
    - Rudolf Steiner
    - Albert Steffen (key person per Britannica related)
    certainty: 1.0
    cites:
    - source: S1
      locator: full article; key people
    how_known: Britannica.
  key_texts:
  - value: Not named in this short Britannica article (Steiner's corpus implied)
    certainty: 1.0
    cites:
    - source: S1
      locator: full article
    how_known: Silence.
metaphysics:
  god_nature_relation:
    value: Spiritual world(s) comprehensible to pure thought and accessible to latent faculties; humans
      originally participated in spiritual processes through dreamlike consciousness. God-nature relation
      not specified as classical theism.
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S1
      locator: full article
    how_known: Britannica blurb; no God doctrine.
  deity_personal:
    value: Not addressed as personal God doctrine; spiritual worlds and spiritual perception.
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: full article
    how_known: Silence.
  intervention:
    value: Not addressed.
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: full article
    how_known: Silence.
  miracles:
    value: Not addressed.
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: full article
    how_known: Silence.
  petition_and_prayer:
    value: Not addressed.
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: full article
    how_known: Silence.
  afterlife:
    value: Not addressed in this article.
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: full article
    how_known: Silence.
  moral_ledger:
    value: Not addressed.
    stance: none
    certainty: 0.5
    cites:
    - source: S1
      locator: full article
    how_known: Silence.
  authority:
    value: Enhanced spiritual perception / faculties of knowledge latent in all humans; spiritual world
      'comprehensible to pure thought' but 'fully accessible only' to those faculties. Founder Steiner.
      Mix of reason and spiritual revelation — leans revelation/esoteric.
    stance: both, revelation first
    certainty: 0.5
    cites:
    - source: S1
      locator: full article
    how_known: Coder's reading of short blurb; 0.5.
  reserved_exemptions:
    value: Not addressed.
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: full article
    how_known: Silence.
  teleology_in_nature:
    value: Not addressed.
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: full article
    how_known: Silence.
  necessity_and_freedom:
    value: Not addressed.
    certainty: 1.0
    cites:
    - source: S1
      locator: full article
    how_known: Silence.
lio_axes:
  A_locus:
    value: UNKNOWN
    how_known: No God-locus doctrine in short Britannica (P44).
  B_cause:
    value: UNKNOWN
    how_known: Silent (P44).
  C_ledger:
    value: UNKNOWN
    how_known: Silent (P44).
  D_authority:
    value: 1
    rationale: Spiritual perception beyond the senses; founder-developed faculty. Leans revelation/esoteric
      over ordinary observation.
    certainty: 0.5
    cites:
    - source: S1
      locator: full article
    how_known: Prior score kept; short article.
  E_scope:
    value: UNKNOWN
    how_known: Silent (P44).
epistemology:
  value: Human intellect can contact spiritual worlds; pure thought comprehends them; full access via
    latent faculties of spiritual perception independent of the senses; originally dreamlike participation
    in spiritual processes.
  certainty: 1.0
  cites:
  - source: S1
    locator: full article
  how_known: Britannica.
ethics:
  value: Not described in this short article.
  certainty: 1.0
  cites:
  - source: S1
    locator: full article
  how_known: Silence.
practice:
  ritual_and_practice:
    value: Not described in this article (Waldorf education and applied fields are widely associated but
      not in this Britannica blurb).
    certainty: 1.0
    cites:
    - source: S1
      locator: full article
    how_known: Silence — do not invent Waldorf from memory without cite.
  community_form:
    value: Anthroposophical Society (1912), based in Dornach, Switzerland, with branches around the world.
    certainty: 1.0
    cites:
    - source: S1
      locator: full article
    how_known: Britannica.
science:
  historical_stance:
    value: Steiner described as philosopher, scientist, and artist; claims spiritual perception beyond
      sensory science. Article too short for a full science stance.
    certainty: 0.5
    cites:
    - source: S1
      locator: full article
    how_known: Coder's reading.
  current_stance:
    value: Not addressed.
    certainty: 1.0
    cites:
    - source: S1
      locator: full article
    how_known: Silence.
schools_and_variants:
- name: Anthroposophical Society (Dornach)
  form: modern
  how_it_differs: Institutional home of Steiner's anthroposophy.
  lio_difference: D=1; other axes UNKNOWN.
  certainty: 1.0
  cites:
  - source: S1
    locator: full article
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
  scoring_note: Anthroposophy scores moderately due to its ambitious integration of spirit and science,
    offering innovative applications but limited by revelatory and unempirical elements.
  source: v7.1 data book, section 6 table (tables[4]) row 58 and section 7 scoring notes
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
  use_when: Anthroposophy / Steiner / Anthroposophical Society identity.
  do_not_use_when: Theosophy without Steinerian anthroposophy — use THEOS.
  neighbors:
  - code: THEOS
    relation: neighbor (easily confused)
  - code: HERMET
    relation: neighbor (easily confused)
review:
  data_quality_flags:
  - 'Thin: one-paragraph editors’ article.'
  open_questions:
  - A signed or peer-reviewed source.
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Britannica Editors
  citation: 'The Editors of Encyclopaedia Britannica. "Anthroposophy." Encyclopaedia Britannica. https://www.britannica.com/topic/anthroposophy.
    Wayback Machine snapshot 2026-10-09 13:54:13 UTC: https://web.archive.org/web/20261009135413/https://www.britannica.com/topic/anthroposophy.'
  url: https://www.britannica.com/topic/anthroposophy
  accessed: '2026-10-25'
  reliability_note: 'Short unsigned editors’ article (one paragraph). P44(e): read in the Wayback copy
    (https://web.archive.org/web/20261009135413/https://www.britannica.com/topic/anthroposophy); live
    page not compared (live Britannica times out from the box).'
---
# Anthroposophy (ANTHRO)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

Anthroposophy is a 'philosophy based on the premise that the human intellect has the ability to contact spiritual worlds', formulated by Rudolf Steiner; Anthroposophical Society founded 1912, based in Dornach [S1].

## Core metaphysics

Spiritual worlds comprehensible to pure thought and to latent faculties of spiritual perception independent of the senses [S1]. Classical God doctrines not in this short article.

## Position on the LIO axes

- **A, B, C, E:** UNKNOWN.
- **D_authority: 1** (0.5) — spiritual perception beyond the senses [S1].

## Schools and variants

Anthroposophical Society [S1].

## Science

Steiner as philosopher/scientist/artist; spiritual perception beyond sensory science [S1].

## Coding guidance

Steinerian anthroposophy. Not THEOS.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> ANTHRO (25/50) — Anthroposophy. Anthroposophy scores moderately due to its ambitious integration of spirit and science, offering innovative applications but limited by revelatory and unempirical elements.

## Open questions

- Fuller Steiner doctrine source (Britannica article is one short paragraph).
- Adherents / Waldorf etc. need separate cites.

## Research log

- 2026-10-15 (batch S10): Britannica anthroposophy; D scored.
- 2026-10-25: deepened classification, origins, metaphysics, epistemology, community from re-read. D kept.
