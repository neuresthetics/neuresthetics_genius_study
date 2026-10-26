---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 6
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
    summary: 'Draft (systems batch S8): filled from SEP "Daoism" (Hansen) and IEP "Daoist Philosophy"
      (Littlejohn). A, B, D BELOW_THRESHOLD; C, E UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from SEP Daoism (2025 entry): dào as natural possibility paths, Laozi/Zhuangzi,
      Ru-Mo foil, science-friendly naturalism; religious Daoism separate. Keep A/B/D BELOW_THRESHOLD;
      C E UNKNOWN.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Fill adherents/estimate gloss from existing sources (order-of-magnitude / qualitative). Axes
      unchanged.
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score C_ledger 4 (0.5) from SEP Daoism (normative naturalism; not afterlife ledger). A/B/D
      stay BELOW (phil vs religious schools).
identity:
  id: TAO
  v7_1_number: 46
  v7_1_label: Taoism (Daoism)
  display_label: Taoism (Daoism)
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: philosophical school or method
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: SEP treats Chinese philosophical Daoism; religious Daoism separate — 0.7.
  family:
    value: 'Philosophical Daoism: normative naturalism around dào (path/way) as structure of natural possibility;
      Laozi and Zhuangzi classical texts'
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: SEP.
  parent_traditions:
    value:
    - Classical Chinese philosophy (Warring States)
    - Critique of Confucian-Mohist (Ru-Mo) human dào debate
    - Later Han category dàojiā
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; history
    how_known: SEP.
  related_codes:
  - code: CONFUC
    relation: contrast case
    note: Ru human dào vs natural dào
  - code: BUDDH
    relation: overlaps
    note: Zen/Chan accommodation historically
  - code: FALUNG
    relation: neighbor (easily confused)
    note: qigong NRM ≠ philosophical Daoism
origins:
  founding_era:
    value: Classical period 5th–3rd c. BCE (Laozi/Zhuangzi texts); Han coinage of Daoist school
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; history
    how_known: SEP.
  founding_region:
    value: China
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: SEP.
  founders_or_key_figures:
    value:
    - Laozi (text tradition)
    - Zhuangzi
    - Shen Dao / Hui Shi (early phase mentions)
    - Wang Bi / Guo Xiang (received texts)
    - 'Modern: Yan Fu, Jin Yuelin, Chen Guying'
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; history
    how_known: SEP.
  key_texts:
  - value: Daode Jing (Laozi)
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: SEP.
  - value: Zhuangzi
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: SEP.
metaphysics:
  god_nature_relation:
    value: Natural dào of cosmos; nature neutral toward ways of life; not a commanding God. Holistic/monist
      tendencies; religious Daoism treated as separate topic.
    stance: no God
    certainty: 0.5
    cites:
    - source: S1
      locator: opening; cosmology
    how_known: Philosophical naturalism; 0.5 — some Absolute-dào readings exist.
  deity_personal:
    value: No supernatural ego as normative authority; Huang-Lao cult historically separate from philosophical
      project.
    stance: no deity
    certainty: 0.5
    cites:
    - source: S1
      locator: opening; history
    how_known: '0.5 philosophical focus.'
  intervention:
    value: 'Not theistic intervention; dào as structure of possibility, not force/cause.'
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: cosmology
    how_known: SEP.
  miracles:
    value: Not a miracle religion in SEP philosophical framing.
    stance: denied
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5.'
  petition_and_prayer:
    value: Not petitionary theism in philosophical Daoism.
    stance: no petition
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: SEP focus.
  afterlife:
    value: Not a focus; Zen accommodation treated ordinary life not Nirvana dualism.
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S1
      locator: history
    how_known: Thin.
  moral_ledger:
    value: Normative naturalism / path-following; not afterlife ledger.
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: SEP.
  authority:
    value: Anti-authoritarian; skeptical of sage/performative authority; science as preferred social dào
      for knowing nature — observation and reason lean.
    stance: observation and reason
    certainty: 0.5
    cites:
    - source: S1
      locator: opening; cosmology
    how_known: '0.5 — axes keep D BELOW_THRESHOLD for school variance.'
  reserved_exemptions:
    value: Not addressed.
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: Silence.
  teleology_in_nature:
    value: Nature not biased to benefit humans (vs Mohism); dào of opportunities not commands.
    stance: none
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — or immanent ends; left none.'
  necessity_and_freedom:
    value: Rejects Shen Dao fatalism; non-committal on determinism; no Western free-will theory; choice
      among possible paths.
    certainty: 1.0
    cites:
    - source: S1
      locator: cosmology; opening
    how_known: SEP.
lio_axes:
  A_locus:
    value: 'BELOW_THRESHOLD'
    how_known: "Members differ (P44(b)): SEP reads classical Daoism as naturalist, assigning normative\
      \ guidance 'to something outside the ego, but not to a supernatural ego' (S1); religious Daoism\
      \ began with 'revelations from the deified Laozi' (S2)."
    note: 'Alternative: 3.'
    alternatives:
    - value: 3
      note: Named alternative.
      cites:
      - source: S1
        locator: metaphysics
      - source: S2
        locator: §1
  B_cause:
    value: 'BELOW_THRESHOLD'
    how_known: Naturalist classical reading (S1) versus revelations from immortals and deities in Shangqing
      Daoism (S2).
  C_ledger:
    value: 4
    certainty: 0.5
    cites:
    - source: S1
      locator: ethics
    - source: S2
      locator: opening
    how_known: '0.5 — normative naturalism / path-following; not afterlife ledger (P44c-style for philosophical
      Daoism).'
    rationale: 'C=4: none. Certainty 0.5: religious Daoism may differ.'
    alternatives:
    - value: 'BELOW_THRESHOLD'
      note: Named alternative if coding religious Daoism immortality/judgment streams as co-equal.
      cites:
      - source: S1
        locator: opening
  D_authority:
    value: 'BELOW_THRESHOLD'
    how_known: "'naturalist philosophical project' (S1) versus mediums who 'claimed to receive revelations\
      \ from immortals' (S2)."
  E_scope:
    value: 'UNKNOWN'
    how_known: Not addressed in the sources read.
epistemology:
  value: "Know-how / learning paths; mild skepticism — overlooked possibilities; science best current\
    \ social dào for understanding nature's structure; open-minded."
  certainty: 1.0
  cites:
  - source: S1
    locator: opening; epistemology sections
  how_known: SEP.
ethics:
  value: Normative naturalism; curiosity and open-mindedness; environmental ethics affinity; not Ru-Mo
    imperial utilitarianism; walk two paths / harmony with others as natural.
  certainty: 1.0
  cites:
  - source: S1
    locator: opening; moral theory
  how_known: SEP.
practice:
  ritual_and_practice:
    value: 'Philosophical Daoism: skilled ordinary practice (e.g. Zhuangzi butcher); religious Daoism
      (monasteries, Huang-Lao) is separate per SEP.'
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; history
    how_known: SEP.
  community_form:
    value: Philosophical school / text traditions; religious institutions separate topic.
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: SEP.
science:
  historical_stance:
    value: Modern Daoists embraced science; Needham thesis controversial; science as preferred dào for
      knowing nature.
    certainty: 1.0
    cites:
    - source: S1
      locator: history; cosmology
    how_known: SEP.
  current_stance:
    value: 'Naturalism not scientism; science good-at telling about dào, does not choose dào s.'
    certainty: 1.0
    cites:
    - source: S1
      locator: cosmology
    how_known: SEP.
schools_and_variants:
- name: Laozi / Daode Jing line
  form: scholastic or philosophical
  how_it_differs: Earlier phase; rejection of social constructs.
  lio_difference: Umbrella BELOW_THRESHOLD.
  certainty: 1.0
  cites:
  - source: S1
    locator: history
- name: Zhuangzi mature Daoism
  form: scholastic or philosophical
  how_it_differs: Accepts language as natural; pluralist paths.
  lio_difference: Same.
  certainty: 1.0
  cites:
  - source: S1
    locator: history
- name: Religious Daoism (dàojiào)
  form: other
  how_it_differs: SEP treats as separate topic from philosophical project.
  lio_difference: Do not assume same scores — may need distinct coding.
  certainty: 1.0
  cites:
  - source: S1
    locator: opening
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Philosophical Daoism + religious Daoist institutions in China/diaspora; vast historical influence
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — qualitative from listed source; not a genius-rate denominator.'
v7_1_rubric:
  label: authorial v7.1 scores
  L: 8
  P: 8
  E: 6
  V: 6
  X: 4
  total: 32
  scoring_note: 'Taoism scores moderately due to its profound emphasis on natural harmony and practical
    wisdom, blending philosophy and religion effectively, but constrained by mystical elements and traditional
    authority over rigorous empirical methods.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 46 and section 7 scoring notes'
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
  use_when: Philosophical Daoism / Lao-Zhuang naturalism identity.
  do_not_use_when: Religious Daoist liturgical identity without philosophical frame — flag separately.
    Falun Gong. Confucianism.
  neighbors:
  - code: CONFUC
    relation: contrast case
  - code: BUDDH
    relation: neighbor (easily confused)
  - code: FALUNG
    relation: neighbor (easily confused)
review:
  data_quality_flags: []
  open_questions:
  - Split philosophical and religious Daoism? (v7.1 has one code.)
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Chad Hansen
  year: 2025
  citation: 'Hansen, Chad. "Daoism." Stanford Encyclopedia of Philosophy. First published April 19, 2025.
    https://plato.stanford.edu/entries/daoism/.'
  url: 'https://plato.stanford.edu/entries/daoism/'
  accessed: '2026-10-25'
  reliability_note: Peer-reviewed; a naturalist reading of classical philosophical Daoism.
- id: S2
  type: tertiary
  kind: encyclopedia
  author: Ronnie Littlejohn
  citation: 'Littlejohn, Ronnie. "Daoist Philosophy." Internet Encyclopedia of Philosophy. https://iep.utm.edu/daoism/.'
  url: 'https://iep.utm.edu/daoism/'
  accessed: '2026-10-25'
  reliability_note: Peer-reviewed; covers classical and religious Daoism. Undated page.
---
# Daoism / Taoism (TAO)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

Philosophical Daoism (SEP): naturalist project around dào as structure of natural possibility; Laozi and Zhuangzi; foil to Ru-Mo human dào debate; religious Daoism treated separately [S1].

## Core metaphysics

Holistic natural dào; nature neutral; not commanding God; science-friendly modern reception [S1].

## Position on the LIO axes

- **A, B, D:** BELOW_THRESHOLD — school/religious vs philosophical variance [S1].
- **C, E:** UNKNOWN.

## Schools and variants

Laozi; Zhuangzi; religious Daoism separate [S1].

## Science

Modern Daoists embrace science as best social dào for knowing nature [S1].

## Coding guidance

Philosophical Daoism. Flag religious Daoism separately.

## v7.1 scoring note

> TAO (32/50) — Taoism (Daoism). Taoism scores moderately due to its profound emphasis on natural harmony and practical wisdom, blending philosophy and religion effectively, but constrained by mystical elements and traditional authority over rigorous empirical methods.

## Open questions

- Whether religious Daoism needs its own code later.

## Research log

- Prior: SEP daoism; BELOW_THRESHOLD axes.
- 2026-10-25: deepened from SEP Daoism (first published 2025-04-19). Axes kept.
- 2026-10-25: adherents/estimate filled (qualitative).
- 2026-10-25: C_ledger scored 4 (0.5).
