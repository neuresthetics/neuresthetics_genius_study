---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 7
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S6 for Jason)
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
    summary: 'Draft (systems batch S6, P45 lower tier): filled from one passage in Lane, Zygon 2021. A
      2 (0.5); B BELOW_THRESHOLD; rest UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S6 audit fix: B how_known reworded (joint inference; deist half suggests unused); scope
      note on Lane.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities: kind/family/parents/related codes, origins, metaphysics TODOs, epistemology,
      ethics, practice, science, schools (deist half vs theist panentheism). Axes unchanged (P45). Re-read
      Lane Zygon 2021.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score D_authority 4 (0.5) and C_ledger 4 (0.5) from sources on file (philosophical; often
      naturalistic). A already 2; B BELOW.
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score E_scope 4 (0.5) from sources on file. Alternatives named.
identity:
  id: PANEND
  v7_1_number: 26
  v7_1_label: Panendeism
  display_label: Panendeism
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: metaphysical thesis
    certainty: 0.7
    cites:
    - source: S1
      locator: introduction
    how_known: Lane treats panendeism as a named hybrid; 0.7.
  family:
    value: Hybrid of panentheism (world in God) with a deist non-interventionist stance
    certainty: 0.7
    cites:
    - source: S1
      locator: introduction
    how_known: Lane groups with panentheism; deist half named in prior fill.
  parent_traditions:
    value:
    - Panentheism (world in / exceeding God)
    - Deism (non-intervening deity)
    - Modern science–religion hybrids
    certainty: 0.7
    cites:
    - source: S1
      locator: introduction
    how_known: Lane + name morphology. 0.7.
  related_codes:
  - code: PANENT
    relation: neighbor (easily confused)
    note: Same “world in God” A reading; PANENT allows world to affect God / intervention forms
  - code: DEISM
    relation: overlaps
    note: 'Deist half: power unused'
  - code: PANDEI
    relation: neighbor (easily confused)
    note: 'Pandeism: God became the universe; panendeism: universe in exceeding God'
  - code: PANT
    relation: neighbor (easily confused)
    note: 'Pantheism: identity, nothing beyond'
origins:
  founding_era:
    value: Modern label (Lane 2021 discusses living/death-of-God forms of related pandeism; panendeism
      as named hybrid)
    certainty: 0.5
    cites:
    - source: S1
      locator: introduction
    how_known: Term modern; P45 lower tier. 0.5.
  founding_region:
    value: Anglophone philosophy of religion / science–religion literature
    certainty: 0.5
    cites:
    - source: S1
      locator: introduction
    how_known: '0.5.'
  founders_or_key_figures:
    value:
    - William C. Lane (Zygon 2021 discussion)
    - Broader panentheist / deist lineage (contrast)
    certainty: 0.5
    cites:
    - source: S1
      locator: introduction
    how_known: Advocate source; 0.5.
  key_texts:
  - value: 'Lane, “Living God Pandeism: Evidential Support,” Zygon 2021 (discusses panendeism alongside)'
    certainty: 0.7
    cites:
    - source: S1
      locator: introduction
    how_known: Sole peer-reviewed source on file.
metaphysics:
  god_nature_relation:
    value: God exceeds the Universe; the Universe exists in God (Lane’s grouping with panentheism)
    stance: God in Nature and beyond it
    certainty: 0.5
    cites:
    - source: S1
      locator: introduction
    how_known: P45 cap 0.5.
  deity_personal:
    value: Living-God forms imply some consciousness; death-of-God forms differ; not fixed for all panendeists
    stance: varies by school
    certainty: 0.5
    cites:
    - source: S1
      locator: introduction
    how_known: Lane’s living/death variants for pandeism family. 0.5.
  intervention:
    value: Deist half suggests retained power unused; no regular miracles assumed
    stance: none
    certainty: 0.5
    cites:
    - source: S1
      locator: introduction
    how_known: Prior B BELOW_THRESHOLD note; 0.5.
  miracles:
    value: No Humean miracles assumed in the deist half
    stance: denied
    certainty: 0.5
    cites:
    - source: S1
      locator: introduction
    how_known: '0.5.'
  petition_and_prayer:
    value: Not a petitionary church religion in the deist reading
    stance: no petition
    certainty: 0.5
    cites:
    - source: S1
      locator: introduction
    how_known: '0.5.'
  afterlife:
    value: Not fixed in sources read
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: Not in Lane passage used.
  moral_ledger:
    value: Not fixed in sources read
    stance: none
    certainty: 0.5
    cites:
    - source: S1
      locator: introduction
    how_known: Not a judgment religion in the deist half. 0.5.
  authority:
    value: Science-allied method in Lane’s related pandeism; panendeism inherits observation-and-reason
      lean
    stance: observation and reason
    certainty: 0.5
    cites:
    - source: S1
      locator: introduction
    how_known: '0.5; advocate.'
  reserved_exemptions:
    value: No in-group miracle exemptions claimed in sources
    stance: none
    certainty: 0.5
    cites:
    - source: S1
      locator: introduction
    how_known: '0.5.'
  teleology_in_nature:
    value: Lawful cosmos; designer-style purpose at Becoming not required for panendeism specifically
    stance: varies by school
    certainty: 0.5
    cites:
    - source: S1
      locator: introduction
    how_known: '0.5.'
  necessity_and_freedom:
    value: Not fixed; deist half leaves freedom under laws
    certainty: 0.5
    cites:
    - source: S1
      locator: introduction
    how_known: '0.5.'
lio_axes:
  A_locus:
    value: 2
    rationale: God exceeds the Universe; the Universe exists in God.
    certainty: 0.5
    cites:
    - source: S1
      locator: introduction
    how_known: P45 cap 0.5; one passage.
  B_cause:
    value: 'BELOW_THRESHOLD'
    how_known: "Lane infers the power to intervene jointly for panentheism and panendeism: 'God therefore\
      \ retains power to intervene in the world “from outside”' (S1). The deist half of panendeism suggests\
      \ the power goes unused, so no value is fixed. P45 lower tier."
    note: 'P45 lower tier. Alternative: 3 (the deist element).'
    alternatives:
    - value: 3
      note: Named alternative.
      cites:
      - source: S1
        locator: introduction
  C_ledger:
    value: 4
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — not a developed ethical/ledger programme; implied none.'
    rationale: C=4 at 0.5.
    alternatives:
    - value: 'UNKNOWN'
      note: Named alternative if refusing implied.
      cites:
      - source: S1
        locator: opening
  D_authority:
    value: 4
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — philosophical argument; stance observation and reason; P45 lower tier.'
    rationale: D=4 at 0.5. Alternative BELOW if religious panendeism streams.
    alternatives:
    - value: 'BELOW_THRESHOLD'
      note: Named alternative if religious overlays co-equal.
      cites:
      - source: S1
        locator: opening
  E_scope:
    value: 4
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — all is God / same divine order'
    rationale: E=4 at 0.5.
    alternatives:
    - value: 'UNKNOWN'
      note: Named alternative if refusing.
      cites:
      - source: S1
        locator: opening
epistemology:
  value: Allies with scientific method in Lane’s cluster; evidence from cosmology/evolution argued for
    living-God forms
  certainty: 0.5
  cites:
  - source: S1
    locator: introduction
  how_known: Advocate; 0.5.
ethics:
  value: Not a developed ethical programme in sources read; inherits from host panentheist/deist ethics
  certainty: 0.5
  cites:
  - source: S1
    locator: introduction
  how_known: '0.5.'
practice:
  ritual_and_practice:
    value: Philosophical/theological thesis; not a church
    certainty: 0.7
    cites:
    - source: S1
      locator: introduction
    how_known: '0.7.'
  community_form:
    value: Sparse self-identification; science–religion writers
    certainty: 0.5
    cites:
    - source: S1
      locator: introduction
    how_known: '0.5.'
science:
  historical_stance:
    value: Modern hybrid built to sit with science
    certainty: 0.5
    cites:
    - source: S1
      locator: introduction
    how_known: '0.5.'
  current_stance:
    value: Lane argues evidential support from cosmology; still niche
    certainty: 0.5
    cites:
    - source: S1
      locator: introduction
    how_known: Advocate; 0.5.
schools_and_variants:
- name: Panendeism (world in exceeding God; non-intervening)
  form: modern
  how_it_differs: Keeps transcendence-plus-immanence of panentheism with deist unused power
  lio_difference: A 2; B BELOW_THRESHOLD (alt 3)
  certainty: 0.5
  cites:
  - source: S1
    locator: introduction
- name: 'Contrast: intervening panentheism'
  form: modern
  how_it_differs: World affects God; persuasion/top-down causation in some forms (SEP)
  lio_difference: Code PANENT
  certainty: 1.0
  cites:
  - source: S2
    locator: introduction; §3
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Few named adherents; technical hybrid label
    certainty: 0.7
    cites:
    - source: S1
      locator: introduction
    how_known: '0.7.'
v7_1_rubric:
  label: authorial v7.1 scores
  L: 9
  P: 9
  E: 9
  V: 9
  X: 8
  total: 44
  scoring_note: 'Panendeism scores high for its elegant fusion of deism and pantheism, providing a conscious
    yet non-interventionist divine model with strong logical and empirical alignment.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 26 and section 7 scoring notes'
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
  use_when: "The person's own writing names panendeism or holds a non-intervening God in whom the universe\
    \ exists."
  do_not_use_when: Process theology and other panentheism is PANENT; a creator outside the world is DEISM.
  neighbors:
  - code: PANENT
    relation: neighbor (easily confused)
    note: Intervention / world-affects-God vs unused power
  - code: PANDEI
    relation: neighbor (easily confused)
    note: Became-universe vs universe-in-God
  - code: DEISM
    relation: overlaps
    note: Deist half
review:
  data_quality_flags:
  - 'P45 lower tier only: one defining passage in a pandeist article; deist content of panendeism not
    sourced.'
  open_questions:
  - Is panendeism distinct enough from DEISM+PANENT dual-coding?
  - Should living-God vs unused-power forms get separate axes?
sources:
- id: S1
  type: secondary
  kind: journal article
  author: William C. Lane
  year: 2021
  citation: 'Lane, William C. "Living God Pandeism: Evidential Support." Zygon: Journal of Religion and
    Science (first published 4 June 2021). https://doi.org/10.1111/zygo.12704.'
  url: 'https://onlinelibrary.wiley.com/doi/10.1111/zygo.12704'
  accessed: '2026-10-25'
  reliability_note: 'P45 lower tier: peer-reviewed journal article (an anonymous reviewer is thanked)
    by an independent researcher who advocates pandeism; claims capped at 0.5. No encyclopedia entry exists
    (SEP, IEP none; Britannica pandeism page has no text). Only Lane’s general definitional claims are
    scored, not his own living-God-pandeism arguments (S6 audit fix).'
- id: S2
  type: tertiary
  kind: encyclopedia
  author: John Culp
  year: 2023
  citation: 'John Culp. "Panentheism." Stanford Encyclopedia of Philosophy. Substantive revision Mon Apr
    24, 2023.'
  url: 'https://plato.stanford.edu/entries/panentheism/'
  accessed: '2026-10-25'
  reliability_note: 'Peer encyclopedia; used for contrast with panentheism, not to rescore panendeism.'
---
# Panendeism (PANEND)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

Lane (Zygon, 2021) groups panendeism with panentheism: God exceeds the Universe; the Universe exists in God [S1]. The deist half suggests retained power unused [S1]. P45 lower tier.

## Core metaphysics

World in / exceeded by God [S1]. Contrast intervening panentheism [S2]. Not a church religion.

## Position on the LIO axes

Axes left as previously coded (A 2 at 0.5; B BELOW_THRESHOLD alt 3; C/D/E UNKNOWN). This pass fills qualities without rescoring.

## Schools and variants

Panendeism proper vs intervening panentheism (PANENT) [S1][S2].

## Science

Built as science-compatible hybrid; Lane argues evidential support [S1].

## Coding guidance

Named panendeism / unused-power world-in-God → PANEND. Intervening or world-affects-God → PANENT. God-became-universe → PANDEI.

## v7.1 scoring note

Authorial v7.1 note unchanged (see front matter).

## Open questions

- Is panendeism distinct enough from DEISM+PANENT dual-coding?
- Should living-God vs unused-power forms get separate axes?

## Research log

- Prior fill from Lane Zygon 2021.
- 2026-10-25: deepened TODOs; added SEP Panentheism as contrast source; axes unchanged.
- 2026-10-25: D/C scored at 0.5.
- 2026-10-25: E_scope scored 4 (0.5).
