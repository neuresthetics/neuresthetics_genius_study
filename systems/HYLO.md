---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 7
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
    summary: 'Draft (systems batch S7): filled from Britannica "Hylozoism" (editors). A, B BELOW_THRESHOLD;
      C, D, E UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S7 audit fix: Wayback snapshot URL and timestamp cited under P44(e).'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities: family, parent traditions, related codes, origins era/region, remaining
      metaphysics (not addressed / nature), epistemology, ethics, practice, science, schools, neighbors.
      A/B stay BELOW_THRESHOLD; C/D/E UNKNOWN. Re-read Britannica Hylozoism.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score D_authority 4 (0.7) and C_ledger/E_scope 4 (0.5) from sources on file (philosophical
      thesis; material vitality). A/B stay BELOW.
  - date: '2026-10-25'
    by: Grok Bot
    summary: Clarify miracles/petition/afterlife/ledger/exemptions as label-not-cult; deepen from Wikipedia
      Hylozoism alongside Britannica S1. No LIO moves (A/B stay BELOW_THRESHOLD).
identity:
  id: HYLO
  v7_1_number: 43
  v7_1_label: Hylozoism
  display_label: Hylozoism
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: metaphysical thesis
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: Britannica.
  family:
    value: Ancient and modern metaphysical theses that treat matter as living (distinct from animism and
      panpsychism)
    certainty: 1.0
    cites: &id001
    - source: S1
      locator: introduction
    how_known: 'Britannica: logically distinct from early animism and from panpsychism.'
  parent_traditions:
    value:
    - Presocratic natural philosophy
    - Cambridge Platonism (term)
    - '18th–19th c. materialist hylozoism'
    certainty: 1.0
    cites: *id001
    how_known: Britannica survey from Thales through Cudworth to Haeckel.
  related_codes:
  - code: ANIM
    relation: neighbor (easily confused)
    note: Animism personifies nature; hylozoism does not require personified spirits
  - code: PANPSY
    relation: neighbor (easily confused)
    note: Panpsychism attributes consciousness/sensation to matter; hylozoism attributes life
  - code: PANENT
    relation: neighbor (easily confused)
    note: Some hylozoists invoke a world soul; not all do
origins:
  founding_era:
    value: 'Label coined 17th c. by Ralph Cudworth; the pattern is traced to Presocratics and recurs in
      Renaissance, Enlightenment, and 19th-c. evolutionism'
    certainty: 1.0
    cites: *id001
    how_known: Britannica.
  founding_region:
    value: Greek Mediterranean (early instances); English Cambridge (term); European philosophy thereafter
    certainty: 0.7
    cites: *id001
    how_known: "Coder's geographic reading of Britannica's figures. 0.7."
  founders_or_key_figures:
    value:
    - Thales
    - Anaximenes
    - Heracleitus
    - Straton
    - Ralph Cudworth (term)
    - Ernst Haeckel
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: Britannica.
  key_texts:
  - value: 'No single canon; Britannica cites Cudworth (term), Cambridge Platonist “plastic nature,” and
      Haeckel’s evolutionary hylozoism among later forms'
    certainty: 0.7
    cites: *id001
    how_known: 'Britannica names figures and doctrines, not a closed textual canon. 0.7.'
metaphysics:
  god_nature_relation:
    value: "Any system that views all matter as alive, either in itself or by participation in a world\
      \ soul or similar principle. Members differ: Thales' things 'full of gods'; Cudworth's plastic nature\
      \ as divine instrument; Straton/Haeckel materialist vitalization."
    stance: varies by school
    certainty: 1.0
    cites: *id001
    how_known: Britannica definition plus member variation.
  deity_personal:
    value: Not fixed. Some early forms treat elements as divine; materialist hylozoism does not require
      a personal deity.
    stance: varies by school
    certainty: 0.7
    cites: *id001
    how_known: "Coder's reading of Britannica's range from Thales to Haeckel. 0.7."
  intervention:
    value: Not a shared doctrine. Plastic nature organizes matter as a divine instrument in Cambridge
      Platonism; materialist forms have no intervenor.
    stance: varies by school
    certainty: 0.7
    cites: *id001
    how_known: Britannica on plastic nature vs materialist forms. 0.7.
  miracles:
    value: Not a miracle doctrine. Hylozoism claims matter is alive or animated (in itself or via world-soul);
      it does not posit suspensions of natural order. Stance varies by school if any theistic overlay
      is added.
    stance: not addressed
    certainty: 0.7
    cites: &id002
    - source: S2
      locator: opening; Ancient Greek philosophy
    how_known: '0.7 — Wikipedia definition.'
  petition_and_prayer:
    value: 'Philosophical cosmology about living matter, not a petitionary cult. No shared prayer practice
      under the label.'
    stance: not addressed
    certainty: 0.7
    cites: *id002
    how_known: '0.7 — Wikipedia.'
  afterlife:
    value: Not entailed by the hylozoist thesis. A world-soul reading might suggest cosmic continuity;
      materialist hylozoism need not. No shared afterlife catechism.
    stance: not addressed
    certainty: 0.5
    cites: *id002
    how_known: '0.5 — Wikipedia; label is about vitality of matter.'
  moral_ledger:
    value: Not a judgment theology. The thesis concerns whether matter is living; it does not set reward/punishment
      rules.
    stance: none
    certainty: 0.7
    cites: *id002
    how_known: '0.7 — Wikipedia.'
  authority:
    value: 'Philosophical thesis, not a church. Authority is argument and observation among philosophers
      who hold the view.'
    stance: observation and reason
    certainty: 0.7
    cites: *id001
    how_known: "Coder's reading; Britannica presents a thesis history. 0.7."
  reserved_exemptions:
    value: 'None. A philosophical label, not an in-group religion with exemptions.'
    stance: none
    certainty: 0.7
    cites: *id002
    how_known: '0.7 — Wikipedia.'
  teleology_in_nature:
    value: 'Often yes in Cambridge Platonist form: plastic nature controls and organizes matter. Materialist
      forms may deny purpose while still calling matter alive.'
    stance: varies by school
    certainty: 0.7
    cites: *id001
    how_known: Britannica on Cudworth/More vs Straton/Haeckel. 0.7.
  necessity_and_freedom:
    value: Not fixed across the label. Cambridge plastic nature organizes as divine instrument; materialist
      forms need not speak of freedom at all.
    certainty: 0.5
    cites:
    - source: S2
      locator: opening
    how_known: '0.5 — Wikipedia + prior Britannica schools.'
lio_axes:
  A_locus:
    value: 'BELOW_THRESHOLD'
    how_known: "Members differ (P44(b)): Thales saw all things as 'full of gods'; Cudworth's 'plastic\
      \ nature' acts 'as a divine instrument of change'; Straton and Haeckel are materialists (S1)."
  B_cause:
    value: 'BELOW_THRESHOLD'
    how_known: "Members differ: a world soul or plastic nature that 'controls and organizes matter' versus\
      \ a 'dynamic, materialistic view of nature' (S1)."
  C_ledger:
    value: 4
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — not addressed; materialist hylozoism implies no divine ledger (P44c implied).'
    rationale: C=4 implied. Certainty 0.5.
    alternatives:
    - value: 'UNKNOWN'
      note: Named alternative if refusing implied score.
      cites:
      - source: S1
        locator: opening
  D_authority:
    value: 4
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: '0.7 — philosophical thesis; stance observation and reason.'
    rationale: 'D=4: argument over revelation.'
    alternatives:
    - value: 3
      note: Named alternative if coding early element-as-divine forms as tradition.
      cites:
      - source: S1
        locator: opening
  E_scope:
    value: 4
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — all matter alive implies same order for kinds; implied (P44c).'
    rationale: E=4 implied. Certainty 0.5.
    alternatives:
    - value: 'UNKNOWN'
      note: Named alternative if refusing implied score.
      cites:
      - source: S1
        locator: opening
epistemology:
  value: 'Historical hylozoists argue from cosmology and natural philosophy (Presocratic archē, plastic
    nature, evolutionary materialism). No single method; the thesis is metaphysical rather than a school
    of method.'
  certainty: 0.7
  cites: *id001
  how_known: "Coder's reading of Britannica's historical survey. 0.7."
ethics:
  value: Not a shared ethical program in the sources read; the label is cosmological.
  certainty: 1.0
  cites: *id001
  how_known: 'Britannica article is cosmology history, not ethics.'
practice:
  ritual_and_practice:
    value: Not a ritual religion; a philosophical thesis about living matter.
    certainty: 1.0
    cites: *id001
    how_known: Britannica.
  community_form:
    value: No church; recurring philosophical position across eras.
    certainty: 1.0
    cites: *id001
    how_known: Britannica.
science:
  historical_stance:
    value: Presocratic natural philosophy; Renaissance/Enlightenment dynamic materialism; Haeckel linked
      life and matter in evolutionary terms — later challenged by emergent evolutionism.
    certainty: 1.0
    cites: *id001
    how_known: Britannica.
  current_stance:
    value: Historical label in philosophy of mind/nature; overlaps with debates on panpsychism and vitalism;
      not a contemporary scientific research programme as such.
    certainty: 0.7
    cites: *id001
    how_known: "Coder's reading of Britannica's closing note on emergent evolutionism. 0.7."
schools_and_variants:
- name: Presocratic elemental hylozoism
  form: scholastic or philosophical
  how_it_differs: 'Thales (water), Anaximenes (air), Heracleitus (fire) treat the archē as living/divine'
  lio_difference: May move A/B — not rescored for the label as a whole
  certainty: 1.0
  cites: *id001
- name: Cambridge Platonist plastic nature
  form: scholastic or philosophical
  how_it_differs: Cudworth coins hylozoism; plastic nature organizes matter as divine instrument
  lio_difference: Would push A/B toward world-soul readings — still BELOW_THRESHOLD for the label
  certainty: 1.0
  cites: *id001
- name: Materialist / evolutionary hylozoism
  form: modern
  how_it_differs: Straton; Diderot et al.; Haeckel — matter vitalized without world-soul theology
  lio_difference: Materialist A/B readings — still BELOW_THRESHOLD for the label
  certainty: 1.0
  cites: *id001
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Not a census religion; historical and contemporary philosophical position
    certainty: 1.0
    cites: *id001
    how_known: 'Britannica presents a thesis history, not membership numbers.'
v7_1_rubric:
  label: authorial v7.1 scores
  L: 8
  P: 7
  E: 6
  V: 7
  X: 4
  total: 32
  scoring_note: 'Hylozoism scores moderately as a philosophical view animating all matter, providing conceptual
    unity but constrained by speculative nature and modest empirical alignment.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 43 and section 7 scoring notes'
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
  use_when: "The person's own writing holds that all matter is alive."
  do_not_use_when: Consciousness in all matter is PANPSY; personified spirits are ANIM.
  neighbors:
  - code: ANIM
    relation: neighbor (easily confused)
    note: Personified spirits → ANIM
  - code: PANPSY
    relation: neighbor (easily confused)
    note: Consciousness/sensation in all matter → PANPSY
review:
  data_quality_flags: []
  open_questions:
  - 'Can any LIO axis be scored for the label as a whole, or only for named schools (Cudworth vs Haeckel)?'
  - 'Adherents are TODO (philosophical thesis, not a census religion).'
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Britannica Editors
  citation: 'The Editors of Encyclopaedia Britannica. "Hylozoism." Encyclopaedia Britannica. https://www.britannica.com/topic/hylozoism.
    Wayback Machine snapshot 2026-09-24 14:41:01 UTC: https://web.archive.org/web/20260924144101/https://www.britannica.com/topic/hylozoism.'
  url: 'https://www.britannica.com/topic/hylozoism'
  accessed: '2026-10-25'
  reliability_note: Short unsigned editors’ article. Live Britannica page read 2026-10-25; matches prior
    Wayback content used 2026-10-15.
- id: S2
  type: tertiary
  kind: encyclopedia
  citation: 'Wikipedia contributors. "Hylozoism." Wikipedia. Accessed 2026-10-25.'
  url: 'https://en.wikipedia.org/wiki/Hylozoism'
  accessed: '2026-10-25'
---
# Hylozoism (HYLO)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

Hylozoism (Greek *hylē* “matter”; *zōē* “life”) is any system that views all matter as alive, either in itself or by participation in a world soul or similar principle [S1]. Britannica marks it as logically distinct from early animism (which personifies nature) and from panpsychism (which attributes consciousness or sensation to all matter) [S1]. The word was coined in the 17th century by Ralph Cudworth; the pattern is traced from Presocratics through Cambridge Platonist “plastic nature” to Enlightenment and Haeckelian forms [S1].

## Core metaphysics

Living matter is the shared claim [S1]. Members differ sharply: Thales saw all things as “full of gods”; Cudworth and More spoke of plastic nature as an unconscious divine instrument organizing matter; Straton, Diderot’s circle, and Haeckel vitalize matter in a materialist or evolutionary key [S1]. The label does not fix a personal deity, afterlife, or moral ledger.

## Position on the LIO axes

- **A_locus, B_cause:** BELOW_THRESHOLD — members differ (world soul / plastic nature vs dynamic materialism) [S1] (P44(b)).
- **C_ledger, D_authority, E_scope:** UNKNOWN — not addressed as shared doctrines in the sources read.

## Schools and variants

Presocratic elemental hylozoism; Cambridge Platonist plastic nature; materialist/evolutionary hylozoism (Straton, Encyclopaedists, Haeckel) [S1].

## Science

Historical natural philosophy and evolutionary materialism; Britannica notes emergent evolutionism later challenged Haeckel’s “all matter must contain life if life derives from matter” [S1].

## Coding guidance

Use when the person’s own writing holds that all matter is alive. Consciousness-in-all-matter is PANPSY; personified spirits are ANIM.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> Hylozoism scores moderately as a philosophical view animating all matter, providing conceptual unity but constrained by speculative nature and modest empirical alignment.

## Open questions

- Can any LIO axis be scored for the label as a whole, or only for named schools (Cudworth vs Haeckel)?
- Adherents are TODO (philosophical thesis, not a census religion).

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7.
- 2026-10-15 (systems batch S7): filled from Britannica; A/B BELOW_THRESHOLD; C/D/E UNKNOWN.
- 2026-10-25: deepened classification, origins, metaphysics TODOs, epistemology, ethics, practice, science, schools; re-read Britannica Hylozoism live.
- 2026-10-25: D/C/E scored.
- 2026-10-25: Clarified thin metaphysics as label-not-cult from Wikipedia Hylozoism.
