---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 5
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S4 for Jason)
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
    summary: 'Draft (systems batch S4): filled from SEP "Phenomenology" (Smith). All axes UNKNOWN: a method
      that brackets existence questions. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities: family, parents, related codes, remaining metaphysics (bracketed / not
      addressed), epistemology (intentionality, epoché), practice, science, schools (Husserl, Heidegger,
      Sartre, Merleau-Ponty). Axes stay UNKNOWN (method brackets existence). Source: SEP Smith.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Fill adherents/estimate gloss from existing sources (order-of-magnitude / qualitative). Axes
      unchanged.
identity:
  id: PHENOM
  v7_1_number: 23
  v7_1_label: Phenomenology
  display_label: Phenomenology
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: philosophical school or method
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: "'the study of structures of consciousness as experienced from the first-person point of\
      \ view'."
  family:
    value: Twentieth-century philosophical method studying structures of consciousness from the first-person
      point of view
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction; §1
    how_known: SEP.
  parent_traditions:
    value:
    - "Brentano's descriptive psychology"
    - Kantian transcendental themes (via Husserl)
    - 'Earlier reflective practice (Descartes, Hume, Kant)'
    certainty: 1.0
    cites:
    - source: S1
      locator: §3; §4
    how_known: SEP history sections.
  related_codes:
  - code: EXIST
    relation: overlaps
    note: Sartre and others link phenomenology to existentialism; EXIST when existence/freedom thesis
      is primary
  - code: IDEAL
    relation: neighbor (easily confused)
    note: "Husserl's transcendental turn debated as idealism; not automatic IDEAL"
  - code: KANT
    relation: neighbor (easily confused)
    note: shared transcendental idiom; different method
  - code: SOLIP
    relation: contrast case
    note: 'bracketing is methodological, not a claim that only one mind exists'
origins:
  founding_era:
    value: Early twentieth century
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP.
  founding_region:
    value: 'Austria and Germany (Husserl); later France (Sartre, Merleau-Ponty)'
    certainty: 1.0
    cites:
    - source: S1
      locator: §4
    how_known: SEP.
  founders_or_key_figures:
    value:
    - Edmund Husserl
    - Martin Heidegger
    - Jean-Paul Sartre
    - Maurice Merleau-Ponty
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP.
  key_texts:
  - value: Logical Investigations
    author: Edmund Husserl
    year: 1900
    certainty: 1.0
    cites:
    - source: S1
      locator: §3; §4
    how_known: SEP.
  - value: Ideas I
    author: Edmund Husserl
    year: 1913
    certainty: 1.0
    cites:
    - source: S1
      locator: §4
    how_known: SEP.
  - value: Being and Time
    author: Martin Heidegger
    year: 1927
    certainty: 1.0
    cites:
    - source: S1
      locator: §4
    how_known: SEP.
  - value: Phenomenology of Perception
    author: Maurice Merleau-Ponty
    year: 1945
    certainty: 1.0
    cites:
    - source: S1
      locator: §4
    how_known: SEP.
metaphysics:
  god_nature_relation:
    value: "Not addressed: Husserl proposed 'bracketing' the question of the existence of the natural\
      \ world."
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: SEP.
  deity_personal:
    value: Not fixed by the method. Husserlian epoché brackets the existence of the natural world; practitioners
      may hold theism or atheism separately.
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: §1; §4
    how_known: SEP on bracketing and on ethics/ontology at the horizon.
  intervention:
    value: Not fixed by the method. Husserlian epoché brackets the existence of the natural world; practitioners
      may hold theism or atheism separately.
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: §1; §4
    how_known: SEP on bracketing and on ethics/ontology at the horizon.
  miracles:
    value: Not fixed by the method. Husserlian epoché brackets the existence of the natural world; practitioners
      may hold theism or atheism separately.
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: §1; §4
    how_known: SEP on bracketing and on ethics/ontology at the horizon.
  petition_and_prayer:
    value: Not fixed by the method. Husserlian epoché brackets the existence of the natural world; practitioners
      may hold theism or atheism separately.
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: §1; §4
    how_known: SEP on bracketing and on ethics/ontology at the horizon.
  afterlife:
    value: Not fixed by the method. Husserlian epoché brackets the existence of the natural world; practitioners
      may hold theism or atheism separately.
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: §1; §4
    how_known: SEP on bracketing and on ethics/ontology at the horizon.
  moral_ledger:
    value: 'Not a divine ledger doctrine. Ethics appears on the horizon (empathy, will, Levinas on the
      face of the other) without a shared afterlife theology.'
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: §5
    how_known: "Coder's reading of SEP ethics section."
  authority:
    value: 'First-person description, reflection, and analysis of lived experience. Not revelation. Variants
      add hermeneutic interpretation (Heidegger) or engagement with experimental psychology (Merleau-Ponty).'
    stance: observation and reason
    certainty: 0.7
    cites:
    - source: S1
      locator: §2
    how_known: "Coder's reading of SEP methods; 'observation' here is reflective description of experience."
  reserved_exemptions:
    value: Not addressed as cosmology. Method claims no in-group exemption from how experience is structured.
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: §1
    how_known: "Coder's reading; method not a cosmology of exemptions."
  teleology_in_nature:
    value: "Not addressed as designer's purposes. Intentionality is directedness of consciousness, not\
      \ natural teleology in the scholastic sense."
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: introduction; §1
    how_known: "Coder's reading."
  necessity_and_freedom:
    value: Varies by school. Sartre stresses radical freedom of choice; Merleau-Ponty binds subjectivity
      to body and world; Husserl focuses on structures of consciousness rather than a free-will doctrine.
    certainty: 1.0
    cites:
    - source: S1
      locator: §4; §5
    how_known: SEP.
lio_axes:
  A_locus:
    value: 'UNKNOWN'
    how_known: Method brackets existence questions; does not fix cosmology (P44).
  B_cause:
    value: 'UNKNOWN'
    how_known: Method brackets existence questions; does not fix cosmology (P44).
  C_ledger:
    value: 'UNKNOWN'
    how_known: Method brackets existence questions; does not fix cosmology (P44).
  D_authority:
    value: 3
    rationale: 'First-person description and analysis of experience over revelation; not laboratory natural
      science, so not 4. Alt UNKNOWN if reflective method is judged not to fix D.'
    certainty: 0.5
    cites:
    - source: S1
      locator: §2
    how_known: 'Borderline: method is epistemic, not a cosmology of authority. Certainty 0.5; alternative
      UNKNOWN.'
    alternatives:
    - value: 'UNKNOWN'
      cites:
      - source: S1
        locator: §1
      note: If bracketing means the method sets no authority stance for LIO.
  E_scope:
    value: 'UNKNOWN'
    how_known: Method brackets existence questions; does not fix cosmology (P44).
epistemology:
  value: 'Study of structures of consciousness as experienced from the first person; intentionality (directedness
    toward objects via content/meaning). Classical methods: pure description, hermeneutic interpretation,
    analysis; Husserlian epoché brackets the natural attitude.'
  certainty: 1.0
  cites:
  - source: S1
    locator: introduction; §1; §2
  how_known: SEP.
ethics:
  value: 'Historically on the horizon rather than the center. Analyses of will, valuing, empathy, and
    (in Levinas) the face of the other; Sartre and Beauvoir develop existential ethics from phenomenological
    bases. No single PHENOM ethics.'
  certainty: 0.7
  cites:
  - source: S1
    locator: §5
  how_known: SEP §5.
practice:
  ritual_and_practice:
    value: 'Philosophical practice: reflective description, epoché, hermeneutic interpretation. Not a
      religious ritual system.'
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: SEP.
  community_form:
    value: 'Academic and literary movement (Freiburg, Paris, later analytic philosophy of mind), not a
      membership religion.'
    certainty: 1.0
    cites:
    - source: S1
      locator: §4
    how_known: SEP.
science:
  historical_stance:
    value: Husserl opposed reducing logic and meaning to mere psychology; Merleau-Ponty engaged experimental
      psychology (e.g. phantom limb). Classical phenomenology often kept a sanctuary beyond natural science
      while analyzing experience that science must also explain.
    certainty: 1.0
    cites:
    - source: S1
      locator: §3; §4; §6
    how_known: SEP.
  current_stance:
    value: "Issues of consciousness, intentionality, and qualia overlap philosophy of mind and cognitive\
      \ science; 'neurophenomenology' mixes methods. Discipline itself remains philosophical."
    certainty: 1.0
    cites:
    - source: S1
      locator: §2; §6; §7
    how_known: SEP.
schools_and_variants:
- name: Husserlian / transcendental phenomenology
  form: scholastic or philosophical
  how_it_differs: Epoché; science of the essence of consciousness; noema/noesis.
  lio_difference: Brackets world-existence; axes UNKNOWN for method.
  certainty: 1.0
  cites:
  - source: S1
    locator: §4
- name: Heideggerian hermeneutic / existential phenomenology
  form: scholastic or philosophical
  how_it_differs: Being-in-the-world; resists bracketing; practical comportment over representational
    intentionality.
  lio_difference: Still not a shared God cosmology; code EXIST when that is primary.
  certainty: 1.0
  cites:
  - source: S1
    locator: §4
- name: 'French existential phenomenology (Sartre, Merleau-Ponty)'
  form: scholastic or philosophical
  how_it_differs: Freedom and the look (Sartre); lived body (Merleau-Ponty).
  lio_difference: Person-level coding for God-view.
  certainty: 1.0
  cites:
  - source: S1
    locator: §4
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Academic philosophical tradition; not a religion or membership census
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: '0.7 — qualitative from listed source; not a genius-rate denominator.'
v7_1_rubric:
  label: authorial v7.1 scores
  L: 9
  P: 9
  E: 9
  V: 10
  X: 8
  total: 45
  scoring_note: 'Phenomenology scores high for its methodical exploration of experience, providing foundational
    insights into consciousness with strong logical and empirical ties, though focused more on description
    than prediction.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 23 and section 7 scoring notes'
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
  use_when: "The person's main stated worldview is phenomenological method."
  do_not_use_when: PHENOM sets no axes; score from the person. Religious phenomenologists keep their own
    God-view.
  neighbors:
  - code: EXIST
    relation: neighbor (easily confused)
  - code: IDEAL
    relation: neighbor (easily confused)
  - code: SOLIP
    relation: neighbor (easily confused)
review:
  data_quality_flags: []
  open_questions:
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: David Woodruff Smith
  year: 2013
  citation: 'David Woodruff Smith. "Phenomenology." Stanford Encyclopedia of Philosophy. First published
    November 16, 2003; substantive revision December 16, 2013. https://plato.stanford.edu/entries/phenomenology/.'
  url: 'https://plato.stanford.edu/entries/phenomenology/'
  accessed: '2026-10-25'
  reliability_note: Peer-reviewed reference entry.
---
# Phenomenology (PHENOM)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44. The v7.1 scores and note are unchanged.

## Summary

'Phenomenology is the study of structures of consciousness as experienced from the first-person point of view' [S1]; it 'came into its own in the early 20th century in the works of Husserl, Heidegger, Sartre, Merleau-Ponty and others' [S1]. Central structure: intentionality [S1].

## Core metaphysics

Existence of the natural world is bracketed in Husserlian epoché [S1]. The method does not fix a God-view; practitioners differ [S1].

## Position on the LIO axes

- **A, B, C, E:** UNKNOWN — method brackets existence (P44).
- **D_authority: 3** (certainty 0.5; alternative UNKNOWN) — first-person description and analysis [S1].

## Schools and variants

Husserlian transcendental; Heideggerian hermeneutic; French existential (Sartre, Merleau-Ponty) [S1].

## Science

Opposed to psychologism about logic; later contact with experimental psychology and philosophy of mind [S1].

## Coding guidance

Score axes from the person. Religious phenomenologists keep their own God-view. EXIST when existential thesis is primary.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> PHENOM (45/50) — Phenomenology. Phenomenology scores high for its methodical exploration of experience, providing foundational insights into consciousness with strong logical and empirical ties, though focused more on description than prediction.

## Open questions

- Adherents are TODO.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7.
- 2026-10-15 (systems batch S4): SEP Smith; axes under P44.
- 2026-10-25: deepened classification, metaphysics, epistemology, practice, science, schools; D_authority 3 (0.5). Re-read SEP.
- 2026-10-25: adherents/estimate filled (qualitative).
