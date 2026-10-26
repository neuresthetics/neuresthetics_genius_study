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
    summary: 'Draft (systems batch S9): filled from Britannica "Native American Religions" (Jocks). A,
      B, D BELOW_THRESHOLD; C, E UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from Britannica Native American religions (Sullivan): diversity/no generic
      religion, place, spirit-in-all, participation over doctrine, oral narrative, death as transition.
      Keep A/B BELOW_THRESHOLD; C/E UNKNOWN; D BELOW_THRESHOLD (P45 umbrella).'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Fill adherents/estimate gloss from existing sources (order-of-magnitude / qualitative). Axes
      unchanged.
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score D_authority 1 (0.7) tradition/ancestors; C_ledger 4 (0.5) no fixed universal ledger
      text. A/B stay BELOW (community variance).
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score E_scope 1 (0.5) from sources on file. Alternatives named.
  - date: '2026-10-25'
    by: Grok Bot
    summary: Fill reserved_exemptions and necessity_and_freedom from Wikipedia Native American religion.
      No LIO moves.
identity:
  id: NATAM
  v7_1_number: 55
  v7_1_label: Native American Traditions
  display_label: Native American Traditions
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: indigenous or traditional religion
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; diversity
    how_known: 'Britannica: indigenous North/South American traditions.'
  family:
    value: Umbrella for highly localized indigenous North American (and related) religious traditions;
      no single Native American religion
    certainty: 1.0
    cites:
    - source: S1
      locator: diversity and common themes
    how_known: Britannica stresses impossibility of a generic NATAM religion.
  parent_traditions:
    value:
    - Local indigenous cosmologies of the Americas (pre- and post-contact)
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  related_codes:
  - code: ANIM
    relation: overlaps
    note: 'spirit/power in plants, animals, landforms'
  - code: ABORIG
    relation: neighbor (easily confused)
    note: Australian Dreaming is a different continent tradition
  - code: VODUN
    relation: neighbor (easily confused)
    note: different African-diaspora lineages
origins:
  founding_era:
    value: Pre-contact indigenous traditions with continuous adaptation; not a single founding date
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; adaptation
    how_known: Britannica.
  founding_region:
    value: North and South America; highly localized to specific places and communities
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; place
    how_known: Britannica.
  founders_or_key_figures:
    value:
    - 'No single founder; local elders and ceremonial specialists; later movements e.g. Ghost Dance, Native
      American Church'
    certainty: 1.0
    cites:
    - source: S1
      locator: adaptation; ceremonies
    how_known: Britannica.
  key_texts:
  - value: 'Oral narratives (creation, migration, moral stories); not sacred texts in the Western fixed-doctrine
      sense'
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; oral
    how_known: 'Britannica: lacked sacred texts and fixed doctrines.'
metaphysics:
  god_nature_relation:
    value: 'No sacred/profane dualism; spirit or power moves in all things (plants, animals, mountains,
      clouds). Some traditions speak of a Creator/Great Spirit (e.g. Iroquois); others are decentralized
      (e.g. Koyukon Raven).'
    stance: varies by school
    certainty: 1.0
    cites:
    - source: S1
      locator: North America; diversity
    how_known: Britannica contrast Iroquois vs Koyukon.
  deity_personal:
    value: 'Varies: personal Creator language in some communities; many powerful other-than-human persons;
      mythic beings contiguous with this world.'
    stance: varies by school
    certainty: 1.0
    cites:
    - source: S1
      locator: diversity; common beliefs
    how_known: Britannica.
  intervention:
    value: 'Other-than-human persons and powers interact with living humans; vision quests, Sacred Pipe,
      ceremonial contact. Boundaries between worlds are permeable.'
    stance: regular
    certainty: 0.7
    cites:
    - source: S1
      locator: North America; ceremonies
    how_known: Britannica.
  miracles:
    value: "Not framed as 'miracles' vs natural law; spirit-power in ordinary and ceremonial life."
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S1
      locator: North America
    how_known: Western miracle category poorly maps; silence on the word.
  petition_and_prayer:
    value: Sacred Pipe as communication with sacred beings; vision quests petition spirit beings for aid;
      ceremonial work.
    stance: petition answered
    certainty: 0.7
    cites:
    - source: S1
      locator: ceremonies
    how_known: Britannica ceremonies section.
  afterlife:
    value: 'Death understood as a transition, not an ending; heterogeneous beliefs; humans as complex
      entities with diverging essences after death.'
    stance: varies by school
    certainty: 1.0
    cites:
    - source: S1
      locator: death; common themes
    how_known: Britannica.
  moral_ledger:
    value: No fixed universal moral code text; instruction in proper behaviour toward kin and other-than-human
      relatives; clowning/shaming as social correction.
    stance: none
    certainty: 0.5
    cites:
    - source: S1
      locator: participation; oral
    how_known: No ledger doctrine; 0.5.
  authority:
    value: 'Oral tradition, restricted knowledge with initiation, local place-memory, ceremonial participation.
      Not a single written revelation.'
    stance: tradition or ancestors
    certainty: 0.7
    cites:
    - source: S1
      locator: diversity; place
    how_known: Britannica.
  reserved_exemptions:
    value: 'Umbrella label across many nations. Some ceremonial knowledge is restricted by initiation,
      age, or nation membership; not one shared exemption doctrine. Avoid pan-Indian overclaim.'
    stance: varies by school
    certainty: 0.5
    cites: &id001
    - source: S2
      locator: opening; Beliefs
    how_known: '0.5 — Wikipedia Native American religion.'
  teleology_in_nature:
    value: Nature bears revelation; animals as progenitors/teachers; not framed as designer teleology.
    stance: immanent ends
    certainty: 0.5
    cites:
    - source: S1
      locator: nature and animals
    how_known: '0.5 coder reading.'
  necessity_and_freedom:
    value: 'Varies widely by nation. Vision, ceremony, and kinship agency appear often; scholastic free-will
      debate is not the frame.'
    certainty: 0.5
    cites: *id001
    how_known: '0.5 — Wikipedia Native American religion.'
lio_axes:
  A_locus:
    value: 'BELOW_THRESHOLD'
    how_known: "Members differ: Iroquois elders speak of 'the Creator’s “Original Instructions”', whereas\
      \ 'the Koyukon universe is notably decentralized' (S1)."
    note: P44(b).
  B_cause:
    value: 'BELOW_THRESHOLD'
    how_known: "Mythic beings 'inhabit and affect either this world or some other world'; 'Actions, words,\
      \ and thoughts are understood in many traditions to have power in the world' (S1). Many, not all."
  C_ledger:
    value: 4
    certainty: 0.5
    cites:
    - source: S1
      locator: ethics
    how_known: '0.5 — no fixed universal moral code text; kin/other-than-human etiquette.'
    rationale: 'C=4 at 0.5: no shared personal divine ledger. Alternative BELOW for variance.'
    alternatives:
    - value: 'BELOW_THRESHOLD'
      note: 'Named alternative: heterogeneous afterlife/ledger beliefs.'
      cites:
      - source: S1
        locator: afterlife
  D_authority:
    value: 1
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: '0.7 — oral tradition, initiation, place-memory; stance tradition or ancestors.'
    rationale: 'D=1: ancestral/oral. Was BELOW; reconstructionist/general Britannica form supports 1 with
      BELOW alternative for variance.'
    alternatives:
    - value: 'BELOW_THRESHOLD'
      note: 'Named alternative: hundreds of nations differ.'
      cites:
      - source: S1
        locator: opening
  E_scope:
    value: 1
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — nation/tribe specific ceremony and land'
    rationale: E=1 at 0.5. Family BELOW also named.
    alternatives:
    - value: 'BELOW_THRESHOLD'
      note: 'Named alternative: many nations differ.'
      cites:
      - source: S1
        locator: opening
epistemology:
  value: 'Oral narrative, place-based knowledge, restricted/initiated knowledge; participation valued
    over doctrinal belief; actions, words, and thoughts have power.'
  certainty: 1.0
  cites:
  - source: S1
    locator: diversity; participation
  how_known: Britannica.
ethics:
  value: 'Cooperation and devotion to kin; generosity as religious act (giveaway, potlatch); treat other-than-human
    relatives as kin; good-hearted ceremonial participation.'
  certainty: 1.0
  cites:
  - source: S1
    locator: cooperation; generosity
  how_known: Britannica.
practice:
  ritual_and_practice:
    value: 'Localized ceremonies: Sun Dance, Sacred Pipe, vision quest, coming-of-age, Ghost Dance (historical
      revitalization), dance; Native American Church as creative adaptation.'
    certainty: 1.0
    cites:
    - source: S1
      locator: ceremonies; adaptation
    how_known: Britannica.
  community_form:
    value: Kin and community–centered; no single church; many local nations and later pan-Indian movements.
    certainty: 1.0
    cites:
    - source: S1
      locator: participation; adaptation
    how_known: Britannica.
science:
  historical_stance:
    value: Not a science–religion dualism in indigenous cosmologies; plants/animals/landforms carry revelation.
    certainty: 0.7
    cites:
    - source: S1
      locator: North America
    how_known: Britannica epistemology contrast.
  current_stance:
    value: Not addressed as a single modern science stance.
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Silence.
schools_and_variants:
- name: Iroquois longhouse Creator tradition (example)
  form: regional
  how_it_differs: Creator with Original Instructions; qualities reminiscent of Christian deity language.
  lio_difference: Umbrella still BELOW_THRESHOLD / UNKNOWN — do not score this school alone without a
    dedicated article.
  certainty: 1.0
  cites:
  - source: S1
    locator: diversity
- name: Koyukon decentralized cosmos (example)
  form: regional
  how_it_differs: Raven as flawed creator among many powers.
  lio_difference: Same umbrella caution.
  certainty: 1.0
  cites:
  - source: S1
    locator: diversity
- name: Native American Church (adaptation)
  form: modern
  how_it_differs: Blends ancient ritual with Christian influences.
  lio_difference: Separate coding if primary identity is NAC.
  certainty: 1.0
  cites:
  - source: S1
    locator: adaptation
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Umbrella for many Indigenous North American traditions; not one membership body
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — qualitative from listed source; not a genius-rate denominator.'
v7_1_rubric:
  label: authorial v7.1 scores
  L: 7
  P: 6
  E: 5
  V: 5
  X: 3
  total: 26
  scoring_note: 'Native American Traditions score moderately due to their profound connection to nature
    and ancestors, offering rich cultural and ethical coherence but limited by reliance on oral revelation
    and lack of empirical rigor.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 55 and section 7 scoring notes'
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
  use_when: "Person's primary engagement is with indigenous North American ceremonial/religious traditions\
    \ under this umbrella."
  do_not_use_when: Australian Aboriginal Dreaming (ABORIG). Generic animism without Native American identity
    (ANIM). Single-nation deep coding when a nation-specific source exists — prefer that over NATAM umbrella.
  neighbors:
  - code: ANIM
    relation: neighbor (easily confused)
  - code: ABORIG
    relation: neighbor (easily confused)
review:
  data_quality_flags: []
  open_questions:
  - Split by tradition?
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Christopher Jocks
  citation: 'Jocks, Christopher. "Native American Religions." Encyclopaedia Britannica. https://www.britannica.com/topic/Native-American-religion.
    Wayback Machine snapshot 2026-10-02 22:43:50 UTC: https://web.archive.org/web/20261002224350/https://www.britannica.com/topic/Native-American-religion.'
  url: 'https://www.britannica.com/topic/Native-American-religion'
  accessed: '2026-10-25'
  reliability_note: 'Signed article; introduction and North America overview read. P44(e): read in the
    Wayback copy (https://web.archive.org/web/20261002224350/https://www.britannica.com/topic/Native-American-religion);
    live page timed out on 2026-10-15, so no live comparison.'
- id: S2
  type: tertiary
  kind: encyclopedia
  citation: 'Wikipedia contributors. "Native American religion." Wikipedia. Accessed 2026-10-25.'
  url: 'https://en.wikipedia.org/wiki/Native_American_religion'
  accessed: '2026-10-25'
---
# Native American Traditions (NATAM)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

Umbrella for diverse, highly localized indigenous North (and South) American religious traditions — 'no such thing as a generic Native American religion' [S1]. Spirit/power in all things; place, oral narrative, participation over doctrine [S1].

## Core metaphysics

Sacred/more-sacred rather than sacred/profane; other-than-human persons; permeable worlds; death as transition [S1]. Creator vs decentralized cosmologies both attested [S1].

## Position on the LIO axes

Umbrella kept **BELOW_THRESHOLD** on A, B, D and **UNKNOWN** on C, E (P45) — diversity forbids a single axis profile without nation-specific sources.

## Schools and variants

Iroquois Creator language vs Koyukon Raven; Navajo individual vs Pueblo communal ritual; Native American Church adaptation [S1].

## Science

Indigenous cosmologies do not split sacred from nature the Western way [S1].

## Coding guidance

Umbrella only. Prefer nation-specific evidence when available. Not ABORIG.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> NATAM (26/50) — Native American Traditions. Native American Traditions score moderately due to their profound connection to nature and ancestors, offering rich cultural and ethical coherence but limited by reliance on oral revelation and lack of empirical rigor.

## Open questions

- Nation-specific deep files when people records need them.
- South American coverage thinner in the North America–heavy article sections used.

## Research log

- 2026-10-15 (batch S9): Britannica Native American religion; umbrella BELOW_THRESHOLD.
- 2026-10-25: deepened classification, origins, metaphysics, ethics, practice, schools. Axes unchanged.
- 2026-10-25: adherents/estimate filled (qualitative).
- 2026-10-25: D/C scored.
- 2026-10-25: E_scope scored 1 (0.5).
- 2026-10-25: Filled exemptions/necessity from Wikipedia Native American religion.
