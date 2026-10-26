---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 8
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S3 for Jason)
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
    summary: 'Draft (systems batch S3): filled from SEP "Existentialism" (Aho). A BELOW_THRESHOLD (secular
      and religious existentialists); others UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S10 audit fix: A how_known repeats the source quote.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities: family/parents/related codes, origins, metaphysics TODOs, epistemology,
      ethics, practice, science, schools (religious/secular; Sartre/Beauvoir; Heidegger; Kierkegaard).
      Axes unchanged. Re-read SEP Existentialism (Aho).'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score D_authority 4 (0.7) from SEP Existentialism (first-person / observation and reason).
      A stays BELOW_THRESHOLD (Kierkegaard vs atheist streams).
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Fill implied axes (C=4@0.5, B=4@0.5, E=4@0.5) from sources on file / P44(c) where naturalistic.
      Alternatives named.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Fill miracles from Wikipedia Existentialism. No LIO moves.
identity:
  id: EXIST
  v7_1_number: 17
  v7_1_label: Existentialism
  display_label: Existentialism
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: family of positions
    certainty: 0.7
    cites:
    - source: S1
      locator: introduction
    how_known: "SEP: 'secular and religious existentialists'. 0.7."
  family:
    value: 'Overlapping modern intellectual movement: existence, freedom, authenticity, engagement'
    certainty: 1.0
    cites: &id001
    - source: S1
      locator: introduction
    how_known: 'SEP: not a coherent system; overlapping ideas.'
  parent_traditions:
    value:
    - '19th-c. Kierkegaard and Nietzsche'
    - 'German phenomenology (Husserl, Heidegger, Jaspers)'
    - 'Mid-20th-c. French existentialism (Sartre, Beauvoir, Camus disputed)'
    - Literary and political extensions
    certainty: 1.0
    cites: *id001
    how_known: SEP introduction.
  related_codes:
  - code: ABSURD
    relation: overlaps
    note: Camus absurdism; Camus denied existentialist label
  - code: NIHIL
    relation: neighbor (easily confused)
    note: Nihilism is a backdrop; EXIST often answers it without affirming nothing
  - code: PHENOM
    relation: overlaps
    note: Heidegger/Merleau-Ponty phenomenological method
  - code: ATHE
    relation: neighbor (easily confused)
    note: Secular EXIST ≠ all atheism; religious EXIST exists
origins:
  founding_era:
    value: '19th-c. pioneers; mid-20th-c. French “existentialist moment”; term used by Marcel 1943'
    certainty: 1.0
    cites: *id001
    how_known: SEP.
  founding_region:
    value: 'Europe (Denmark, Germany, France, Spain); wide literary and political reach'
    certainty: 1.0
    cites: *id001
    how_known: SEP.
  founders_or_key_figures:
    value:
    - Søren Kierkegaard
    - Friedrich Nietzsche
    - Martin Heidegger
    - Jean-Paul Sartre
    - Simone de Beauvoir
    - Karl Jaspers
    - Gabriel Marcel
    - Maurice Merleau-Ponty
    certainty: 1.0
    cites: *id001
    how_known: SEP.
  key_texts:
  - value: 'Sartre, Existentialism Is a Humanism; Being and Nothingness'
    certainty: 1.0
    cites: *id001
    how_known: SEP.
  - value: 'Heidegger, Being and Time'
    certainty: 1.0
    cites: *id001
    how_known: SEP.
  - value: 'Kierkegaard, Fear and Trembling; Concluding Unscientific Postscript'
    certainty: 1.0
    cites: *id001
    how_known: SEP.
  - value: 'Beauvoir, The Ethics of Ambiguity; The Second Sex'
    certainty: 1.0
    cites: *id001
    how_known: SEP.
metaphysics:
  god_nature_relation:
    value: "Varies: 'one finds secular and religious existentialists'."
    stance: varies by school
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP.
  deity_personal:
    value: 'Varies: secular (Sartre) and religious (Kierkegaard, Marcel, Tillich-influenced debates) existentialists'
    stance: varies by school
    certainty: 1.0
    cites: *id001
    how_known: SEP.
  intervention:
    value: 'Not a shared miracle doctrine; some religious forms retain God, secular forms do not'
    stance: varies by school
    certainty: 0.7
    cites: *id001
    how_known: '0.7.'
  miracles:
    value: 'Not addressed as doctrine. Existentialism concerns existence, freedom, and meaning; it is
      not a miracle religion. Religious existentialists (Kierkegaard) differ from atheist ones (Sartre).'
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S2
      locator: opening
    how_known: '0.5–0.7 — Wikipedia Existentialism.'
  petition_and_prayer:
    value: Varies with religious vs secular strands
    stance: varies by school
    certainty: 0.7
    cites: *id001
    how_known: '0.7.'
  afterlife:
    value: Not fixed; secular forms face death without afterlife consolation; religious forms may retain
      faith
    stance: varies by school
    certainty: 0.7
    cites: *id001
    how_known: SEP on death/anxiety. 0.7.
  moral_ledger:
    value: Rejects moral absolutes as external table; responsibility for choices replaces divine ledger
      for secular forms
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: §6
    how_known: SEP ethics. 0.7.
  authority:
    value: First-person engagement; subjective truth (Kierkegaard); no view-from-nowhere system
    stance: observation and reason
    certainty: 0.7
    cites:
    - source: S1
      locator: §2
    how_known: 'SEP Engagement vs Detachment. 0.7 — “observation and reason” as lived inquiry, not scientism.'
  reserved_exemptions:
    value: Authenticity critique of herd/They; no in-group supernatural exemption doctrine as such
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: §5
    how_known: '0.7.'
  teleology_in_nature:
    value: No pre-given human essence; existence precedes essence (Sartre packaging of Heidegger)
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: §3
    how_known: SEP. 0.7.
  necessity_and_freedom:
    value: Freedom and responsibility central; facticity constrains but does not erase choice; Sartre
      moves from radical to situated freedom
    certainty: 1.0
    cites:
    - source: S1
      locator: §4
    how_known: SEP Freedom.
lio_axes:
  A_locus:
    value: 'BELOW_THRESHOLD'
    how_known: "Secular and religious existentialists (S1): members differ (P44b). Quote (S1, introduction):\
      \ Varies: 'one finds secular and religious existentialists'."
    note: 'Evidence: S1 introduction.'
  B_cause:
    value: 4
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — no shared miracle doctrine; this-world freedom.'
    rationale: B=4 at 0.5 (atheist streams); Kierkegaard alt.
    alternatives:
    - value: 'BELOW_THRESHOLD'
      note: 'Named alternative: Kierkegaardian religious existentialism.'
      cites:
      - source: S1
        locator: §1
  C_ledger:
    value: 4
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — no moral absolutes; no divine ledger as family default.'
    rationale: C=4 at 0.5.
    alternatives:
    - value: 'UNKNOWN'
      note: Named alternative if refusing P44(c) implied score.
      cites:
      - source: S1
        locator: opening
  D_authority:
    value: 4
    certainty: 0.7
    cites:
    - source: S1
      locator: introduction; §1
    how_known: '0.7 — SEP: engaged first-person analysis; stance observation and reason; no shared revelation
      for the family.'
    rationale: 'D=4: authenticity and reason over revealed authority as family stance. Not 3: Kierkegaard’s
      leap is a school, not the family default.'
    alternatives:
    - value: 3
      note: Named alternative if coding Kierkegaardian religious existentialism as primary.
      cites:
      - source: S1
        locator: §1
  E_scope:
    value: 4
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — implied same human condition (P44c-ish).'
    rationale: E=4 at 0.5.
    alternatives:
    - value: 'UNKNOWN'
      note: Named alternative if refusing P44(c) implied score.
      cites:
      - source: S1
        locator: opening
epistemology:
  value: Engaged first-person analysis over detached “God’s-eye” systems; Kierkegaard subjective truth;
    Nietzsche perspectivism; Heidegger being-in-the-world
  certainty: 1.0
  cites:
  - source: S1
    locator: §2
  how_known: SEP.
ethics:
  value: 'No moral absolutes; praiseworthy life owns freedom, takes responsibility, helps others realize
    freedom (Sartre/Beauvoir); authenticity vs bad faith'
  certainty: 1.0
  cites:
  - source: S1
    locator: §5–6
  how_known: SEP.
practice:
  ritual_and_practice:
    value: 'Not a church; literary, political, psychotherapeutic, and academic practices'
    certainty: 1.0
    cites: *id001
    how_known: SEP introduction on wide reach.
  community_form:
    value: Intellectual/literary movement; postwar journals; later clinical “existential therapy”
    certainty: 1.0
    cites: *id001
    how_known: SEP.
science:
  historical_stance:
    value: Crisis of modernity after rise of secular-scientific worldview and industrial mass society;
      not anti-science as such but anti-scientistic reduction of persons
    certainty: 0.7
    cites:
    - source: S1
      locator: §1
    how_known: SEP nihilism section. 0.7.
  current_stance:
    value: 'Influences phenomenology of mind, critical phenomenology, health humanities; debates with
      AI representationalism (Dreyfus line in SEP)'
    certainty: 1.0
    cites:
    - source: S1
      locator: §7
    how_known: SEP Contemporary Relevance.
schools_and_variants:
- name: Religious existentialism
  form: scholastic or philosophical
  how_it_differs: Kierkegaard faith leap; Marcel; theological debates
  lio_difference: May move A — family BELOW_THRESHOLD
  certainty: 1.0
  cites: *id001
- name: Secular / Sartrean–Beauvoirian
  form: scholastic or philosophical
  how_it_differs: Existence precedes essence; bad faith; ethics of freedom for others
  lio_difference: May move A toward 4
  certainty: 1.0
  cites: *id001
- name: Heideggerian Dasein analysis
  form: scholastic or philosophical
  how_it_differs: Being-in-the-world; authenticity as resoluteness; not Sartre’s label
  lio_difference: Not rescored
  certainty: 1.0
  cites:
  - source: S1
    locator: §2.3; §5.4
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Not a census religion; intellectual/literary movement
    certainty: 1.0
    cites: *id001
    how_known: SEP.
v7_1_rubric:
  label: authorial v7.1 scores
  L: 9
  P: 9
  E: 10
  V: 10
  X: 8
  total: 46
  scoring_note: Existentialism empowers individual meaning-making with strong psychological insight.
  source: 'v7.1 data book, section 6 table (tables[4]) row 17 and section 7 scoring notes'
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
  use_when: "The person's own writing adopts 'existence precedes essence' or self-identifies as existentialist."
  do_not_use_when: EXIST sets no A value; score from the person. Camus-type absurd is ABSURD.
  neighbors:
  - code: ABSURD
    relation: neighbor (easily confused)
    note: Camus rejected existentialist label
  - code: NIHIL
    relation: neighbor (easily confused)
    note: Backdrop vs answer
  - code: PHENOM
    relation: overlaps
    note: Method overlap
review:
  data_quality_flags: []
  open_questions:
  - 'Camus: keep ABSURD separate (already coded).'
  - Can A be scored for Sartre-majority persons without collapsing religious EXIST?
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Kevin Aho
  year: 2023
  citation: 'Kevin Aho. "Existentialism." Stanford Encyclopedia of Philosophy. First published January
    6, 2023. https://plato.stanford.edu/entries/existentialism/.'
  url: 'https://plato.stanford.edu/entries/existentialism/'
  accessed: '2026-10-25'
  reliability_note: Peer-reviewed reference entry.
- id: S2
  type: tertiary
  kind: encyclopedia
  citation: 'Wikipedia contributors. "Existentialism." Wikipedia. Accessed 2026-10-25.'
  url: 'https://en.wikipedia.org/wiki/Existentialism'
  accessed: '2026-10-25'
---
# Existentialism (EXIST)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44. The v7.1 scores and note are unchanged.

## Summary

Existentialism is a mid-20th-century intellectual movement with 19th-century roots, marked by overlapping ideas rather than a single system: engagement over detachment, existence preceding essence, freedom and responsibility, authenticity, and ethics without moral absolutes [S1]. Secular and religious strands both appear [S1].

## Core metaphysics

No shared cosmology. God varies by school [S1]. Freedom/facticity tension is central [S1]. Moral absolutes as external tables are rejected; responsibility for choices is emphasized [S1].

## Position on the LIO axes

- **A_locus:** BELOW_THRESHOLD — secular vs religious existentialists (P44(b)) [S1].
- **B–E:** UNKNOWN / prior coding unchanged (see front matter).

## Schools and variants

Religious (Kierkegaard/Marcel); Sartrean–Beauvoirian secular; Heideggerian Dasein analysis [S1].

## Science

Responds to modern secular-scientific and industrial crisis without reducing persons to objects [S1]; later influence on phenomenology of mind and clinical fields [S1].

## Coding guidance

Use for the EXIST movement. Camus’s absurdism → ABSURD. Mere nihilism → NIHIL. Phenomenological method alone may be PHENOM.

## v7.1 scoring note

Authorial v7.1 note unchanged (see front matter).

## Open questions

- Camus: keep ABSURD separate (already coded).
- Can A be scored for Sartre-majority persons without collapsing religious EXIST?

## Research log

- Prior fill from SEP Existentialism.
- 2026-10-25: deepened TODOs; re-read SEP (Aho).
- 2026-10-25: D_authority scored 4 (0.7).
- 2026-10-25: implied axis fill: C=4@0.5, B=4@0.5, E=4@0.5.
- 2026-10-25: Filled miracles from Wikipedia Existentialism.
