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
    summary: 'Draft (systems batch S10, thin): filled from Britannica "Anthroposophy" (editors, one paragraph).
      D BELOW_THRESHOLD; rest UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S10 audit fix: D BELOW_THRESHOLD -> 1 @0.5 (alt 2).'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from short Britannica: family, Steiner, spiritual worlds via enhanced consciousness,
      Anthroposophical Society 1912 Dornach. Keep D=1; other axes UNKNOWN (article very short).'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Fill adherents/estimate gloss from existing sources (order-of-magnitude / qualitative). Axes
      unchanged.
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen ethics (Lucifer/Ahriman balance; Christ Representative), afterlife/karma, practice
      (Waldorf/biodynamic). Score C_ledger 3 (0.5) karma; A_locus 1 (0.5) Christ-centered spiritual worlds.
      S2 Wikipedia.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score B_cause 1 (0.5) and E_scope 2 (0.5) from Wikipedia Anthroposophy (spiritual science;
      Steiner hierarchy).
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
    value: "Rudolf Steiner's anthroposophy: human intellect can contact spiritual worlds; enhanced consciousness\
      \ perceives spiritual worlds independent of the senses"
    certainty: 1.0
    cites:
    - source: S1
      locator: full article
    how_known: Britannica.
  parent_traditions:
    value:
    - "Rudolf Steiner's synthesis (Austrian philosopher, scientist, artist)"
    - Earlier Theosophical milieu (historical context; not detailed in this short article)
    certainty: 0.5
    cites:
    - source: S1
      locator: full article
    how_known: Steiner named; Theosophy link not in this Britannica blurb — 0.5.
  related_codes:
  - code: THEOS
    relation: neighbor (easily confused)
    note: "Steiner's path diverged from Theosophy; use ANTHRO for anthroposophy"
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
    value: 'Europe; Society now based in Dornach, Switzerland, with branches worldwide'
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
  - value: "Not named in this short Britannica article (Steiner's corpus implied)"
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
    value: Christ being / Representative of Humanity as central spiritual entity; Lucifer and Ahriman
      as polar spiritual adversaries; not conventional personal theism alone
    certainty: 0.7
    cites:
    - source: S2
      locator: Ethics; Christ as the center
    how_known: '0.7 — Wikipedia Christology/ethics sections.'
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
    value: Reincarnation of the human spirit; life review after death; karmic preparation for next incarnation
    certainty: 0.7
    cites:
    - source: S2
      locator: Nature of the human being; reincarnation
    how_known: '0.7 — Wikipedia on Steiner’s reincarnation/karma teaching.'
  moral_ledger:
    value: Karma linking lives; moral development required before spiritual faculties unfold
    certainty: 0.7
    cites:
    - source: S2
      locator: reincarnation; karma
    how_known: '0.7 — Wikipedia.'
  authority:
    value: "Enhanced spiritual perception / faculties of knowledge latent in all humans; spiritual world\
      \ 'comprehensible to pure thought' but 'fully accessible only' to those faculties. Founder Steiner.\
      \ Mix of reason and spiritual revelation — leans revelation/esoteric."
    stance: 'both, revelation first'
    certainty: 0.5
    cites:
    - source: S1
      locator: full article
    how_known: "Coder's reading of short blurb; 0.5."
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
    value: 1
    certainty: 0.5
    cites:
    - source: S2
      locator: Christ as the center
    - source: S1
      locator: spiritual worlds
    how_known: '0.5 — spiritual worlds + Christ being; not mid-basin deism; not atheism.'
    rationale: 'A=1: transcendent spiritual persons/worlds with Christ center. Certainty 0.5: complex
      Christology.'
    alternatives:
    - value: 0
      note: Named alternative if coding stronger transcendence-only reading.
      cites:
      - source: S2
        locator: Christ
    - value: 2
      note: Named alternative if coding Goethean nature-spirit immanence more heavily.
      cites:
      - source: S2
        locator: Union of science and spirit
  B_cause:
    value: 1
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — spiritual hierarchies / supersensible perception claims.'
    rationale: B=1 at 0.5.
    alternatives:
    - value: 'UNKNOWN'
      note: Named alternative if thin.
      cites:
      - source: S1
        locator: opening
  C_ledger:
    value: 3
    certainty: 0.5
    cites:
    - source: S2
      locator: karma
    how_known: '0.5 — karma across lives as impersonal moral-causal law (P44d).'
    rationale: 'C=3: karmic impersonal ledger. Alternative 1 if coding Christ-judgment streams.'
    alternatives:
    - value: 1
      note: Named alternative if coding Christ as personal judge of lives.
      cites:
      - source: S2
        locator: Christ
    - value: 4
      note: Named alternative if reading ethical individualism as no ledger.
      cites:
      - source: S2
        locator: Philosophy of Freedom
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
    value: 2
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — esoteric grades / initiation; not closed ethnic in-group.'
    rationale: E=2 at 0.5.
    alternatives:
    - value: 1
      note: Named alternative.
      cites:
      - source: S1
        locator: opening
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
  value: Good as balance between Lucifer (pride/creativity) and Ahriman (materialism/intellect); Christ
    / Representative of Humanity mediates; moral development prerequisite to spiritual perception
  certainty: 0.7
  cites:
  - source: S2
    locator: Ethics
  - source: S1
    locator: opening
  how_known: '0.7 — Wikipedia Ethics section; Britannica confirms spiritual-perception path.'
practice:
  community_form:
    value: 'Anthroposophical Society (Goetheanum, Dornach); Waldorf schools; Camphill; biodynamic farms;
      applied cultural movements'
    certainty: 0.7
    cites:
    - source: S2
      locator: Claimed applications
    - source: S1
      locator: opening
    how_known: '0.7 — Wikipedia applications; Britannica society context.'
  ritual_and_practice:
    value: Meditation and moral self-discipline (How to Know Higher Worlds); eurythmy; artistic work;
      applied education/agriculture/medicine streams
    certainty: 0.7
    cites:
    - source: S2
      locator: Paths of spiritual development; Eurythmy
    how_known: '0.7 — Wikipedia.'
science:
  historical_stance:
    value: 'Steiner described as philosopher, scientist, and artist; claims spiritual perception beyond
      sensory science. Article too short for a full science stance.'
    certainty: 0.5
    cites:
    - source: S1
      locator: full article
    how_known: "Coder's reading."
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
  how_it_differs: "Institutional home of Steiner's anthroposophy."
  lio_difference: D=1; other axes UNKNOWN.
  certainty: 1.0
  cites:
  - source: S1
    locator: full article
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Anthroposophical Society and Waldorf network; Britannica no global census here
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
  scoring_note: 'Anthroposophy scores moderately due to its ambitious integration of spirit and science,
    offering innovative applications but limited by revelatory and unempirical elements.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 58 and section 7 scoring notes'
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
  url: 'https://www.britannica.com/topic/anthroposophy'
  accessed: '2026-10-25'
  reliability_note: 'Short unsigned editors’ article (one paragraph). P44(e): read in the Wayback copy
    (https://web.archive.org/web/20261009135413/https://www.britannica.com/topic/anthroposophy); live
    page not compared (live Britannica times out from the box).'
- id: S2
  type: tertiary
  kind: encyclopedia
  citation: 'Wikipedia contributors, "Anthroposophy," Wikipedia (accessed 2026-10-25). Cross-check with
    Britannica S1.'
  url: 'https://en.wikipedia.org/wiki/Anthroposophy'
  accessed: '2026-10-25'
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
- 2026-10-25: adherents/estimate filled (qualitative).
- 2026-10-25: ethics/afterlife/practice deepened from Wikipedia S2; A/C scored.
- 2026-10-25: B/E scored.
