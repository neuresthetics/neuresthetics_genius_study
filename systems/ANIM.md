---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 8
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S7 for Jason)
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
    summary: 'Draft (systems batch S7): filled from Britannica "Animism" (Park). A BELOW_THRESHOLD (alt
      3); B 1 (0.5, alt 0); C, D, E UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S7 audit fix: A quote starts at “no ground for supposing”.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from Britannica animism (Park/Tylor survey): innumerable spiritual beings,
      particularism, practical communication, not a single creed. Keep A BELOW_THRESHOLD; B=1; C D E UNKNOWN.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Fill adherents/estimate gloss from existing sources (order-of-magnitude / qualitative). Axes
      unchanged.
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score D_authority 1 (0.7) from Britannica Animism (tradition/ancestors; oral). A stays BELOW;
      B already 1.
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score C_ledger 1 (0.5) and E_scope 1 (0.5) from sources on file (spirit reciprocity; local
      peoples).
identity:
  id: ANIM
  v7_1_number: 40
  v7_1_label: Animism
  display_label: Animism
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: family of positions
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Not a single creed; range of beliefs/practices.
  family:
    value: 'Animism: belief in innumerable spiritual beings concerned with human affairs, able to help
      or harm; often spirits in nature'
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  parent_traditions:
    value:
    - Ethnographic tribal religions worldwide
    - "Tylor's Primitive Culture (1871) theoretical framing (historical scholarship)"
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; Tylor
    how_known: Britannica.
  related_codes:
  - code: NATAM
    relation: overlaps
    note: many Native traditions described with animistic features
  - code: ABORIG
    relation: overlaps
    note: Dreaming/totemism often discussed under animism
  - code: SHINTO
    relation: neighbor (easily confused)
    note: kami not reducible to ANIM umbrella
origins:
  founding_era:
    value: Prehistoric / ethnographic present; term currency from Tylor 1871 — not a founded religion
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  founding_region:
    value: Worldwide in tribal and indigenous contexts; not a single homeland
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  founders_or_key_figures:
    value:
    - No founder; Edward Burnett Tylor (scholar who coined currency of the term)
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  key_texts:
  - value: No sacred text; ethnographic field studies; Tylor Primitive Culture (scholarship)
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
metaphysics:
  god_nature_relation:
    value: Innumerable spirits in nature and human affairs; particularistic powers; not one universal
      God. May coexist with polytheistic/monotheistic ideas.
    stance: many gods within nature
    certainty: 0.7
    cites:
    - source: S1
      locator: opening; importance
    how_known: Britannica.
  deity_personal:
    value: 'Spirits as personal beings who help or harm; nature spirits, ghosts, ancestor gods.'
    stance: personal
    certainty: 0.7
    cites:
    - source: S1
      locator: opening; objects
    how_known: Britannica.
  intervention:
    value: 'Spirits regularly involved in food, illness, danger; divination and propitiation.'
    stance: regular
    certainty: 1.0
    cites:
    - source: S1
      locator: daily lives
    how_known: Britannica.
  miracles:
    value: Not framed as miracles vs natural law.
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: Silence.
  petition_and_prayer:
    value: Communication with spirits about practical matters; propitiatory observances; genuine worship
      rare.
    stance: petition answered
    certainty: 0.7
    cites:
    - source: S1
      locator: daily lives; vs other religions
    how_known: Britannica.
  afterlife:
    value: "Ghosts and ancestor spirits; doctrine of souls in Tylor's series; varies by people."
    stance: varies by school
    certainty: 0.7
    cites:
    - source: S1
      locator: Tylor; opening
    how_known: Britannica.
  moral_ledger:
    value: Practical taboos and propitiation more than cosmic ledger; lasting moral relationships with
      some supernaturals possible.
    stance: none
    certainty: 0.5
    cites:
    - source: S1
      locator: daily lives
    how_known: '0.5.'
  authority:
    value: 'Grassroots, not doctrinaire from above; diviners identify responsible spirits; no single revelation.'
    stance: tradition or ancestors
    certainty: 0.5
    cites:
    - source: S1
      locator: daily lives
    how_known: '0.5.'
  reserved_exemptions:
    value: Not addressed.
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: Silence.
  teleology_in_nature:
    value: World alive and interconnected; spirits animate nature — not designer teleology.
    stance: immanent ends
    certainty: 0.5
    cites:
    - source: S1
      locator: nature FAQ
    how_known: '0.5.'
  necessity_and_freedom:
    value: Not addressed.
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Silence.
lio_axes:
  A_locus:
    value: 'BELOW_THRESHOLD'
    how_known: "Spirits indwell nature (Tylor: 'sun and stars, trees and rivers, winds and clouds, become\
      \ personal animate creatures'), but 'no ground for supposing that polytheistic and monotheistic\
      \ ideas were excluded' (S1)."
    note: 'Members differ (P44(b)). Alternative: 3.'
    alternatives:
    - value: 3
      note: Named alternative.
      cites:
      - source: S1
        locator: Importance; Tylor’s theory
  B_cause:
    value: 1
    rationale: "Spirits are 'capable of helping or harming human interests'; rites aim 'to influence powerful\
      \ spirits and so control important natural events'."
    certainty: 0.5
    cites: &id001
    - source: S1
      locator: introduction; Tylor’s theory
    how_known: '0.5; the second quote is Tylor’s account. Alternative 0.'
    alternatives:
    - value: 0
      note: Named alternative.
      cites: *id001
  C_ledger:
    value: 1
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — reciprocity with spirits; not a single heaven ledger.'
    rationale: C=1 at 0.5.
    alternatives:
    - value: 'UNKNOWN'
      note: Named alternative if family too thin.
      cites:
      - source: S1
        locator: opening
  D_authority:
    value: 1
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: '0.7 — stance tradition or ancestors; oral/place knowledge.'
    rationale: 'D=1: ancestral/tradition. Not 0: no single closed revelation.'
    alternatives:
    - value: 2
      note: Named alternative if coding spirit-encounter as mixed personal gnosis.
      cites:
      - source: S1
        locator: opening
  E_scope:
    value: 1
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — local spirits and peoples; not universal same-rules naturalism.'
    rationale: E=1 at 0.5. BELOW also named for vast variance.
    alternatives:
    - value: 'BELOW_THRESHOLD'
      note: 'Named alternative: animism is a family.'
      cites:
      - source: S1
        locator: opening
epistemology:
  value: Communication with spirits; divination when trouble occurs; open/eclectic rather than closed
    doctrine.
  certainty: 1.0
  cites:
  - source: S1
    locator: daily lives; vs other
  how_known: Britannica.
ethics:
  value: Respect and reciprocity with natural/spirit world; avoid trouble via taboos; practical more than
    metaphysical ethics.
  certainty: 0.7
  cites:
  - source: S1
    locator: nature; daily lives
  how_known: Britannica.
practice:
  ritual_and_practice:
    value: 'Propitiation, taboos, divination, ritual cleansing, cures; particularistic handling of local
      spirits.'
    certainty: 1.0
    cites:
    - source: S1
      locator: daily lives; opening
    how_known: Britannica.
  community_form:
    value: Grassroots tribal/local; does not easily align with centralized political authority.
    certainty: 1.0
    cites:
    - source: S1
      locator: daily lives
    how_known: Britannica.
science:
  historical_stance:
    value: "Tylor framed as early natural philosophy; modern anthropology rejects evolutionary 'primitive\
      \ mind' premise."
    certainty: 1.0
    cites:
    - source: S1
      locator: importance; Tylor
    how_known: Britannica.
  current_stance:
    value: Not a science program; ethnographic category.
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: Coder reading.
schools_and_variants:
- name: Local animistic traditions (umbrella)
  form: regional
  how_it_differs: 'Particularistic; examples Sami, Ojibwa, Buryat, Australian totems.'
  lio_difference: A BELOW_THRESHOLD; B=1.
  certainty: 1.0
  cites:
  - source: S1
    locator: examples
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Umbrella ethnographic category; not a membership body
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — qualitative from listed source; not a genius-rate denominator.'
v7_1_rubric:
  label: authorial v7.1 scores
  L: 8
  P: 7
  E: 6
  V: 7
  X: 4
  total: 32
  scoring_note: 'Animism scores moderately as a spiritual philosophy emphasizing universal life and harmony,
    providing cultural depth but constrained by supernatural assumptions and modest empirical alignment.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 40 and section 7 scoring notes'
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
  use_when: "Person's primary frame is animistic spirit-in-nature / innumerable spirits without a more\
    \ specific code fitting better."
  do_not_use_when: 'Prefer NATAM, ABORIG, SHINTO, VODUN, SANTER when those identities fit. Not a dump
    for all indigenous religion.'
  neighbors:
  - code: NATAM
    relation: neighbor (easily confused)
  - code: SHINTO
    relation: neighbor (easily confused)
  - code: ABORIG
    relation: neighbor (easily confused)
review:
  data_quality_flags: []
  open_questions:
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: George Kerlin Park
  citation: 'Park, George Kerlin. "Animism." Encyclopaedia Britannica. https://www.britannica.com/topic/animism.'
  url: 'https://www.britannica.com/topic/animism'
  accessed: '2026-10-25'
  reliability_note: Signed article by an anthropologist; read through the Tylor section. AI Top Questions
    ignored.
---
# Animism (ANIM)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

Animism is belief in innumerable spiritual beings concerned with human affairs; not a single creed but a worldview range, often in tribal contexts [S1].

## Core metaphysics

Particularistic spirits in nature and human life; practical communication; grassroots [S1].

## Position on the LIO axes

- **A:** BELOW_THRESHOLD — too various for one locus [S1].
- **B: 1** — regular spirit involvement [S1].
- **C, D, E:** UNKNOWN.

## Schools and variants

Local traditions only under umbrella [S1].

## Science

Historical Tylor framing vs modern anthropology [S1].

## Coding guidance

Umbrella — prefer specific codes when available.

## v7.1 scoring note

> ANIM (32/50) — Animism. Animism scores moderately as a spiritual philosophy emphasizing universal life and harmony, providing cultural depth but constrained by supernatural assumptions and modest empirical alignment.

## Open questions

- When to prefer ANIM vs NATAM/ABORIG for a person record.

## Research log

- Prior batch: Britannica animism; B scored.
- 2026-10-25: deepened. Axes kept.
- 2026-10-25: adherents/estimate filled (qualitative).
- 2026-10-25: D_authority scored 1.
- 2026-10-25: C/E scored.
