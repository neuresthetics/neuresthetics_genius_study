---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 7
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S8 for Jason)
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
    summary: 'Draft (systems batch S8): filled from Britannica "Heathenry" (Doyle White). A BELOW_THRESHOLD
      (alt 3); rest UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'P44(e) compliance (with the S7 fixes): Wayback snapshot URL and timestamp cited.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S10 audit fix: A how_known repeats the source quote.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from Britannica Heathenry (Doyle White): Germanic Neo-Pagan reconstruction,
      kindreds, polytheism, folkish vs universalist, Nine Noble Virtues. Keep A BELOW_THRESHOLD; B C D
      E UNKNOWN.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Fill adherents/estimate gloss from existing sources (order-of-magnitude / qualitative). Axes
      unchanged.
identity:
  id: HEATH
  v7_1_number: 48
  v7_1_label: Heathenry (Ásatrú/Norse-Germanic Paganism)
  display_label: Heathenry (Ásatrú/Norse-Germanic Paganism)
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: reconstructionist religion
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: Revival/continuation framing of extinct Germanic religions; also Neo-Pagan NRM — 0.7 reconstructionist.
  family:
    value: 'Heathenry: modern Pagan religion inspired by pre-Christian religions of Germanic-speaking
      societies (esp. Old Norse); also Ásatrú, Forn Sed, Odinism, Northern Tradition'
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  parent_traditions:
    value:
    - Pre-Christian Germanic polytheisms (esp. Old Norse/Icelandic textual record)
    - '19th–20th c. Romantic/völkisch receptions'
    - '1970s Neo-Pagan revival'
    certainty: 1.0
    cites:
    - source: S1
      locator: origins
    how_known: Britannica.
  related_codes:
  - code: WICCA
    relation: neighbor (easily confused)
    note: different Neo-Pagan stream
  - code: HELLEN
    relation: neighbor (easily confused)
    note: Greek reconstructionist
  - code: RODNOV
    relation: neighbor (easily confused)
    note: Slavic Rodnoverie
origins:
  founding_era:
    value: Modern formation from early 20th-c. völkisch groups; renewed impetus in the 1970s; Internet-era
      growth 1990s–2000s
    certainty: 1.0
    cites:
    - source: S1
      locator: origins
    how_known: Britannica.
  founding_region:
    value: 'Europe and North America (Germany, Austria historically; US, Britain, Iceland, Norway, Sweden)'
    certainty: 1.0
    cites:
    - source: S1
      locator: origins; opening
    how_known: Britannica.
  founders_or_key_figures:
    value:
    - No single founder; early völkisch groups; later national kindreds and solitary practitioners
    certainty: 1.0
    cites:
    - source: S1
      locator: origins
    how_known: Britannica.
  key_texts:
  - value: Medieval Old Norse textual corpus (primary historical inspiration)
    certainty: 1.0
    cites:
    - source: S1
      locator: origins; beliefs
    how_known: Britannica.
  - value: Nine Noble Virtues (modern codification many Heathens follow)
    certainty: 1.0
    cites:
    - source: S1
      locator: beliefs
    how_known: Britannica.
metaphysics:
  god_nature_relation:
    value: 'Usually polytheistic; gods/goddesses (Odin, Thor, Freyja etc.) often regarded as independently
      existing; some treat as symbolic. Lesser nature spirits; Yggdrasill cosmic tree from Old Norse sources.'
    stance: many gods within nature
    certainty: 0.7
    cites:
    - source: S1
      locator: beliefs
    how_known: Polytheism primary; 0.7 vs varies.
  deity_personal:
    value: Most regard divinities as independently existing persons; some symbolic only.
    stance: both / disputed
    certainty: 1.0
    cites:
    - source: S1
      locator: beliefs
    how_known: Britannica.
  intervention:
    value: Worship of gods; not a single intervention doctrine detailed.
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S1
      locator: beliefs
    how_known: Thin on intervention mechanics.
  miracles:
    value: Not addressed.
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: beliefs
    how_known: Silence.
  petition_and_prayer:
    value: Worship implied; mechanics not detailed in this article.
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S1
      locator: beliefs
    how_known: Thin.
  afterlife:
    value: Not detailed in this Britannica article.
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: beliefs
    how_known: Silence.
  moral_ledger:
    value: Nine Noble Virtues as behavioural code; not an afterlife ledger.
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: beliefs
    how_known: Britannica.
  authority:
    value: No single authority; historical/archaeological fidelity emphasized by many; kindreds and national
      orgs; folkish vs universalist split.
    stance: varies by school
    certainty: 1.0
    cites:
    - source: S1
      locator: beliefs; origins
    how_known: Britannica.
  reserved_exemptions:
    value: Not addressed.
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: Silence.
  teleology_in_nature:
    value: Lesser spirits of the natural world; not designer teleology.
    stance: immanent ends
    certainty: 0.5
    cites:
    - source: S1
      locator: beliefs
    how_known: '0.5.'
  necessity_and_freedom:
    value: Not addressed.
    certainty: 1.0
    cites:
    - source: S1
      locator: beliefs
    how_known: Silence.
lio_axes:
  A_locus:
    value: 'BELOW_THRESHOLD'
    how_known: "Most hold the gods exist independently, some see them only as symbols (S1). Members differ\
      \ (P44(b)). Quote (S1, Beliefs and practices): 'Heathens are usually polytheistic ... Most Heathens\
      \ regard these divinities as having an independent existence, but some practitioners perceive them\
      \ only as symbolic figures.'"
    note: 'Alternative: 3.'
    alternatives:
    - value: 3
      note: Named alternative.
      cites:
      - source: S1
        locator: Beliefs and practices
  B_cause:
    value: 'UNKNOWN'
    how_known: Not addressed in the sources read.
  C_ledger:
    value: 'UNKNOWN'
    how_known: Not addressed in the sources read.
  D_authority:
    value: 'UNKNOWN'
    how_known: "'There has never been a single authority in charge of Heathenry' (S1); no positive source\
      \ of authority stated beyond historical sources."
  E_scope:
    value: 'UNKNOWN'
    how_known: Not addressed in the sources read.
epistemology:
  value: Religion assembled from historical and archaeological sources; many seek greater fidelity to
    pre-Christian evidence than earlier Heathenry.
  certainty: 1.0
  cites:
  - source: S1
    locator: opening; origins
  how_known: Britannica.
ethics:
  value: 'Nine Noble Virtues (modern list many follow); wide disagreement on race, gender, sexuality aligned
    with folkish vs universalist branches.'
  certainty: 1.0
  cites:
  - source: S1
    locator: beliefs
  how_known: Britannica.
practice:
  ritual_and_practice:
    value: 'Kindred meetings; solitary practice common; symbols Mjöllnir, runes, valknut. Specific rite
      forms not detailed here.'
    certainty: 0.7
    cites:
    - source: S1
      locator: beliefs
    how_known: Britannica thin on rite detail.
  community_form:
    value: 'Kindreds, sometimes national orgs; many solitaries; low tens of thousands internationally.'
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; beliefs
    how_known: Britannica.
science:
  historical_stance:
    value: Heavy appeal to historical and archaeological evidence as basis for reconstruction.
    certainty: 1.0
    cites:
    - source: S1
      locator: origins
    how_known: Britannica.
  current_stance:
    value: Not a science doctrine beyond historical method preference.
    certainty: 0.7
    cites:
    - source: S1
      locator: origins
    how_known: Coder reading.
schools_and_variants:
- name: Universalist Heathenry
  form: modern
  how_it_differs: Nonracial vision; majority by 2015 survey per Britannica.
  lio_difference: Axes unchanged at umbrella.
  certainty: 1.0
  cites:
  - source: S1
    locator: origins
- name: Folkish Heathenry
  form: modern
  how_it_differs: Racial religion for biological descendants of Germanic peoples; contested within movement.
  lio_difference: Same umbrella scores; E/ethics differ socially not metaphysically scored here.
  certainty: 1.0
  cites:
  - source: S1
    locator: origins
- name: Ásatrú / Forn Sed / Odinism labels
  form: modern
  how_it_differs: Alternate names; Ásatrú often Norse-focused.
  lio_difference: Same umbrella.
  certainty: 1.0
  cites:
  - source: S1
    locator: opening
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Modern Heathenry / Ásatrú groups; small organized Pagan presence
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
  V: 6
  X: 3
  total: 27
  scoring_note: 'Heathenry scores moderately due to its cultural revival of Germanic polytheism, emphasizing
    honor and nature, but limited by supernatural elements and reconstructionist authority over empirical
    rigor.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 48 and section 7 scoring notes'
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
  use_when: 'Heathenry, Ásatrú, Forn Sed, Odinism, Northern Tradition as Germanic Neo-Pagan identity.'
  do_not_use_when: 'Wicca. Hellenismos. Rodnoverie. Folkish political identity without religious practice
    — still HEATH if they practice Heathenry, but note the branch.'
  neighbors:
  - code: WICCA
    relation: neighbor (easily confused)
  - code: HELLEN
    relation: neighbor (easily confused)
  - code: RODNOV
    relation: neighbor (easily confused)
review:
  data_quality_flags: []
  open_questions:
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Ethan Doyle White
  citation: 'Doyle White, Ethan. "Heathenry." Encyclopaedia Britannica. https://www.britannica.com/topic/Heathenry.
    Wayback Machine snapshot 2026-03-04 08:05:02 UTC: https://web.archive.org/web/20260304080502/https://www.britannica.com/topic/Heathenry.'
  url: 'https://www.britannica.com/topic/Heathenry'
  accessed: '2026-10-25'
  reliability_note: 'Signed article (historian of modern Paganism). P44(e): read in the Wayback copy (https://web.archive.org/web/20260304080502/https://www.britannica.com/topic/Heathenry);
    live page timed out on 2026-10-15, so no live comparison.'
---
# Heathenry (Ásatrú/Norse-Germanic Paganism) (HEATH)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

Heathenry is a modern Pagan religion inspired by pre-Christian Germanic (esp. Old Norse) religions; also called Ásatrú, Forn Sed, Odinism, Northern Tradition [S1].

## Core metaphysics

Usually polytheistic (Odin, Thor, Freyja, etc.); some symbolic readings; nature spirits; Yggdrasill [S1]. Folkish vs universalist split [S1].

## Position on the LIO axes

- **A_locus:** BELOW_THRESHOLD — polytheism vs symbolic variance [S1].
- **B, C, D, E:** UNKNOWN.

## Schools and variants

Universalist majority (by 2015 survey in source); folkish minority; name variants [S1].

## Science

Reconstruction from historical/archaeological sources [S1].

## Coding guidance

Germanic Neo-Pagan. Not WICCA.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> HEATH (27/50) — Heathenry (Ásatrú/Norse-Germanic Paganism). Heathenry scores moderately due to its cultural revival of Germanic polytheism, emphasizing honor and nature, but limited by supernatural elements and reconstructionist authority over empirical rigor.

## Open questions

- Blót/sumbel rite detail needs a fuller practice source.
- Afterlife (Valhalla etc.) not in this encyclopedia article — leave not addressed.

## Research log

- Prior batches: Britannica Heathenry; A BELOW_THRESHOLD.
- 2026-10-25: deepened classification, origins, metaphysics, ethics, schools. Axes kept.
- 2026-10-25: adherents/estimate filled (qualitative).
