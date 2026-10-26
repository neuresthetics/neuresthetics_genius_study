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
    summary: 'Draft (systems batch S7): filled from SEP "Confucius" (Csikszentmihalyi). A BELOW_THRESHOLD
      (alt 2); B 3 (0.5); C 3 (0.5, alt 4); D 2 (0.5, alt 1); E UNKNOWN. v7.1 scores and note unchanged.
      Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S7 audit fix: C 3 @0.5 -> UNKNOWN (lead 4); P44(d) needs a stated karma-type law.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from SEP Confucius (Csikszentmihalyi): ritual psychology, five virtues,
      family/state, Mandate of Heaven naturalized. Keep A BELOW_THRESHOLD; B=3 D=2.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Fill adherents/estimate gloss from existing sources (order-of-magnitude / qualitative). Axes
      unchanged.
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score C_ledger 4 (0.5) from SEP Confucius (virtue/political consequences; no karma-type law).
      B/D already scored.
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score E_scope 4 (0.5) from sources on file. Alternatives named.
identity:
  id: CONFUC
  v7_1_number: 44
  v7_1_label: Philosophical Confucianism
  display_label: Philosophical Confucianism
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: philosophical school or method
    certainty: 0.5
    cites:
    - source: S1
      locator: §1
    how_known: '0.5 — also Ru ritual specialists and temple cult; SEP focuses on philosophical Confucius.'
  family:
    value: 'Confucius / Ru tradition: ritual psychology, virtue cultivation (ren, yi, li, zhi, xin), family–state
      ethics; Analects-centered philosophical reading'
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; §3–5
    how_known: SEP.
  parent_traditions:
    value:
    - Zhou ritual and classical culture
    - Ru specialists in ritual and music
    - "Later Mencius/Xunzi and Neo-Confucian developments (beyond this entry's focus)"
    certainty: 1.0
    cites:
    - source: S1
      locator: §1; opening
    how_known: SEP.
  related_codes:
  - code: TAO
    relation: contrast case
    note: natural dào vs Ru human path
  - code: BUDDH
    relation: neighbor (easily confused)
    note: Neo-Confucian engagement with Buddhism
  - code: CHRIST
    relation: neighbor (easily confused)
    note: Jesuit/Enlightenment readings as Natural Theology
origins:
  founding_era:
    value: Confucius trad. 551–479 BCE; Analects compilation debated (wide Han circulation 1st c. BCE)
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: SEP.
  founding_region:
    value: 'China (Lu / Zou, modern Shandong)'
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: SEP.
  founders_or_key_figures:
    value:
    - Confucius (Kongzi)
    - 'Disciples (Yan Yuan, Zi Lu, Zengzi, etc.)'
    - Mencius / Xunzi as major developers
    - Zhu Xi (Neo-Confucian Four Books curriculum)
    certainty: 1.0
    cites:
    - source: S1
      locator: §1–2
    how_known: SEP.
  key_texts:
  - value: Analects (Lunyu)
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: SEP.
  - value: Records of Ritual and related ritual compilations
    certainty: 1.0
    cites:
    - source: S1
      locator: §2–3
    how_known: SEP.
  - value: 'Classics (Odes, Documents, etc.) as curriculum'
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: SEP.
metaphysics:
  god_nature_relation:
    value: Inherited Zhou Mandate of Heaven / High God; Analects moves toward naturalized Heaven that
      need not speak; personal virtue more than direct intercession.
    stance: varies by school
    certainty: 0.5
    cites:
    - source: S1
      locator: §5
    how_known: A BELOW_THRESHOLD kept — Heaven underdetermined across readings.
  deity_personal:
    value: Zhou anthropomorphized Heaven/High God historically; Analects naturalizing trend; not classical
      theism.
    stance: varies by school
    certainty: 0.5
    cites:
    - source: S1
      locator: §5
    how_known: '0.5.'
  intervention:
    value: "Classical Mandate: Heaven replaces bad rulers; Confucius as uncrowned king counters simple\
      \ reward; Analects: Heaven's support via virtue/culture more than direct miracles."
    stance: rare
    certainty: 0.5
    cites:
    - source: S1
      locator: §5
    how_known: B=3 kept from prior coding.
  miracles:
    value: Not a miracle religion in SEP philosophical focus.
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: Silence.
  petition_and_prayer:
    value: Ancestral sacrifice and reverence; wisdom may keep distance from ghosts while serving people
      (Analects 6.22).
    stance: varies by school
    certainty: 0.5
    cites:
    - source: S1
      locator: §3; §4
    how_known: '0.5.'
  afterlife:
    value: Ancestral rites and mourning; not a detailed personal afterlife doctrine in SEP focus.
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S1
      locator: §3
    how_known: Thin.
  moral_ledger:
    value: No karma-type law in entry; virtue and political/moral consequences; C UNKNOWN kept.
    stance: none
    certainty: 0.5
    cites:
    - source: S1
      locator: prior audit note
    how_known: Prior S7; entry no karma.
  authority:
    value: 'Tradition, classics, sages, ritual mastery — not prophetic revelation. D=2 kept.'
    stance: tradition or ancestors
    certainty: 0.5
    cites:
    - source: S1
      locator: §1; §4
    how_known: '0.5 — alternative founder/sage emphasis.'
  reserved_exemptions:
    value: Not addressed.
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: Silence.
  teleology_in_nature:
    value: Mandate/Heaven political teleology historically; naturalized readings reduce designer talk.
    stance: varies by school
    certainty: 0.5
    cites:
    - source: S1
      locator: §5
    how_known: '0.5.'
  necessity_and_freedom:
    value: Habituation and nurture emphasized (Analects 17.2); cultivation program; not Western free-will
      theory.
    certainty: 0.7
    cites:
    - source: S1
      locator: §4
    how_known: SEP.
lio_axes:
  A_locus:
    value: 'BELOW_THRESHOLD'
    how_known: "Heaven moves from an 'anthropomorphized cosmic power' (Zhou) toward a 'naturalized' concept\
      \ in the Analects (S1). Not fixed for the system."
    note: 'Alternative: 2.'
    alternatives:
    - value: 2
      note: Named alternative.
      cites:
      - source: S1
        locator: §5
  B_cause:
    value: 3
    rationale: "'Even when Heaven’s support is cited in the Analects, it is not a matter of direct intercession,\
      \ but expressed through personal virtue or cultural patterns.'"
    certainty: 0.5
    cites:
    - source: S1
      locator: §5
    how_known: '0.5: the Analects only; the inherited Zhou view had supernatural intercession.'
  C_ledger:
    value: 4
    certainty: 0.5
    cites:
    - source: S1
      locator: ethics
    how_known: '0.5 — virtue and political/moral consequences; no karma-type law in entry.'
    rationale: 'C=4: none as divine/karmic ledger. Certainty 0.5.'
    alternatives:
    - value: 3
      note: Named alternative if reading Heaven’s Mandate as impersonal moral law.
      cites:
      - source: S1
        locator: Heaven
  D_authority:
    value: 2
    rationale: "Benevolence 'is grounded in tradition'; Confucius sought to preserve the Zhou ritual system."
    certainty: 0.5
    cites: &id001
    - source: S1
      locator: §4
    how_known: '0.5: tradition and sages, not revelation. Alternative 1.'
    alternatives:
    - value: 1
      note: Named alternative.
      cites: *id001
  E_scope:
    value: 4
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — same human nature / li and ren as general order'
    rationale: E=4 at 0.5.
    alternatives:
    - value: 'UNKNOWN'
      note: Named alternative if refusing.
      cites:
      - source: S1
        locator: opening
epistemology:
  value: 'Study of Odes, ritual, music; model emulation; situational dialogue; wisdom as knowing others/situations;
    underdetermined textual tradition.'
  certainty: 1.0
  cites:
  - source: S1
    locator: §2; §4
  how_known: SEP.
ethics:
  value: 'Virtue cultivation: benevolence, righteousness, ritual propriety, wisdom, trustworthiness; filial
    piety as root; role ethics in family and state; Golden Rule–like formulations debated.'
  certainty: 1.0
  cites:
  - source: S1
    locator: §4–5
  how_known: SEP.
practice:
  ritual_and_practice:
    value: Zhou ritual and music performance with reverence; mourning; curriculum of classics; temple
      offerings historically.
    certainty: 1.0
    cites:
    - source: S1
      locator: §1; §3
    how_known: SEP.
  community_form:
    value: Master–disciple teaching; later imperial examination/scholar-official culture; Ru specialists.
    certainty: 1.0
    cites:
    - source: S1
      locator: §1–2
    how_known: SEP.
science:
  historical_stance:
    value: Not a natural-science program; knowledge of names of birds/plants noted as part of Odes study.
    certainty: 0.7
    cites:
    - source: S1
      locator: §4
    how_known: SEP aside.
  current_stance:
    value: Modern readings as moral philosophy / virtue ethics.
    certainty: 0.7
    cites:
    - source: S1
      locator: §1
    how_known: SEP.
schools_and_variants:
- name: Analects / early Confucius dialogues
  form: scholastic or philosophical
  how_it_differs: SEP primary focus; historically underdetermined.
  lio_difference: A BELOW_THRESHOLD; B=3 D=2.
  certainty: 1.0
  cites:
  - source: S1
    locator: opening; §2
- name: Mencius vs Xunzi lines
  form: scholastic or philosophical
  how_it_differs: Human nature and cultivation programs diverge.
  lio_difference: May move axes — not rescored.
  certainty: 1.0
  cites:
  - source: S1
    locator: §4
- name: Neo-Confucianism (e.g. Zhu Xi)
  form: scholastic or philosophical
  how_it_differs: li/qi cosmology; Four Books curriculum.
  lio_difference: Beyond SEP focus — separate care.
  certainty: 1.0
  cites:
  - source: S1
    locator: §1
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Philosophical/civil tradition across East Asia; not a single membership church
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
  scoring_note: 'Confucianism scores moderately due to its profound ethical system for societal harmony,
    grounded in human relationships, but limited by traditional authority and modest empirical scope beyond
    social sciences.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 44 and section 7 scoring notes'
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
  use_when: Confucian / Ru / Analects-centered identity as primary philosophical or cultural frame.
  do_not_use_when: "Philosophical Daoism alone. Generic 'Chinese tradition' without Confucian frame —\
    \ consider CHNFOLK."
  neighbors:
  - code: TAO
    relation: contrast case
  - code: BUDDH
    relation: neighbor (easily confused)
  - code: CHNFOLK
    relation: neighbor (easily confused)
review:
  data_quality_flags: []
  open_questions:
  - Neo-Confucianism not read.
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Mark Csikszentmihalyi
  year: 2024
  citation: 'Csikszentmihalyi, Mark. "Confucius." Stanford Encyclopedia of Philosophy. First published
    March 31, 2020; substantive revision May 2, 2024. https://plato.stanford.edu/entries/confucius/.'
  url: 'https://plato.stanford.edu/entries/confucius/'
  accessed: '2026-10-25'
  reliability_note: Peer-reviewed reference entry on Confucius and the Analects; later Confucianism not
    covered.
---
# Confucianism / Confucius (CONFUC)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

SEP Confucius: historically underdetermined philosophy centered on ritual psychology, virtue cultivation, and family–state ethics; Analects and related dialogues [S1].

## Core metaphysics

Zhou Mandate of Heaven inherited and partly naturalized; authority in tradition and sages more than revelation [S1].

## Position on the LIO axes

- **A:** BELOW_THRESHOLD — Heaven readings diverge [S1].
- **B: 3, D: 2** kept.
- **C, E:** UNKNOWN.

## Schools and variants

Analects focus; Mencius/Xunzi; Neo-Confucianism beyond entry [S1].

## Science

Not a natural-science program [S1].

## Coding guidance

Confucian/Ru identity; not CHNFOLK dump.

## v7.1 scoring note

> CONFUC (32/50) — Philosophical Confucianism. Confucianism scores moderately due to its profound ethical system for societal harmony, grounded in human relationships, but limited by traditional authority and modest empirical scope beyond social sciences.

## Open questions

- Whether Neo-Confucianism needs distinct coding later.

## Research log

- Prior: SEP Confucius; B=3 D=2.
- 2026-10-25: deepened ritual/virtues/politics from same SEP. Axes kept.
- 2026-10-25: adherents/estimate filled (qualitative).
- 2026-10-25: C_ledger scored 4 (0.5).
- 2026-10-25: E_scope scored 4 (0.5).
