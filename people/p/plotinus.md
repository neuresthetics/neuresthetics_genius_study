---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA8)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-21
  change_log:
    - {date: 2026-10-21, by: "Grok Bot", summary: "RQ-AA8-1 resolved yes by Jason (2026-10-21, P49): B 3 at 0.5 from SEP's reconstruction (basis scholarly_reconstruction), alternative 2. Still not plotted (A BELOW_THRESHOLD)."}
    - {date: 2026-10-20, by: "Grok Bot", summary: "AA8 audit fixes: B reason corrected (SEP §2 does set out a view of nature); B stays UNKNOWN pending RQ-AA8-1; SEP summary dropped as a statement (not a scholarly edition); 'mature age of fifty' cited."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA8, order P32: F 3, rank 211). Source: SEP 'Plotinus' (Paul Kalligas, 2024, read in full). Born 204 CE (inferred from Porphyry, S1); settled in Rome late 244; his treatises 'began to be composed ten years after his arrival in Rome' (about 254) and continued until his death in 270 (S1). Lasting work: the treatises collected by Porphyry as the Enneads; he 'is generally regarded as the founder of Late Antique Platonism, sometimes termed Neoplatonism' (S1). Span 254–270 at 0.5 (composition range, RQ-Z9-N1; start inferred), age 50. Worldview: PLATO at 0.5 (scholarly_reconstruction): 'Plato's figure dominates Plotinus' thought' (S1). A BELOW_THRESHOLD: the One is 'beyond being' and transcendent (A 1 lead), but everything proceeds from it by emanation (A 2 lead); no source read settles the reading. Not a scientist; B UNKNOWN pending RQ-AA8-1 (held for Jason): S1 §2 does reconstruct his account of nature (laws 'constant and immutable'; the same causes 'inexorably produce the same effects, provided that no other exogenous factor enters into play'); mid_basin BELOW_THRESHOLD. Not plotted. Draft, not reviewed."}

identity:
  id: plotinus
  display_name: "Plotinus"
  roster:
    canonical_name: "Plotinus"
    rank: 211
    F: 3
    models: [Claude, DeepSeek, Grok]
    band: "core (3–4)"
    status: "core"
    field: "philosophy"
    field_bucket: "philosophy"
  full_name: {value: "Plotinus", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Writings"}], how_known: "SEP."}
  native_name: {value: UNKNOWN, how_known: "Greek form not printed in the source read."}
  aliases: []

basics:
  birth:
    date: {value: "204", certainty: 0.5, cites: [{source: S1, locator: "1. Life and Writings"}], how_known: "SEP: 'we may infer that he was born in 204 CE' (from Porphyry)."}
    place: {value: "Egypt", modern_name: "Egypt", polity_then: "Roman Egypt", certainty: 0.5, cites: [{source: S1, locator: "1. Life and Writings"}], how_known: "SEP: 'a native of Egypt'; town not given."}
  death:
    date: {value: "270", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Writings"}], how_known: "SEP."}
    place: {value: UNKNOWN, how_known: "Place of death not stated in S1 (he taught in Rome until his death)."}
  first_lasting_contribution_year: {value: 254, certainty: 0.5, cites: [{source: S1, locator: "1. Life and Writings"}], how_known: "Treatises 'began to be composed ten years after his arrival in Rome' (late 244), so about 254; 'Plotinus began composing his works approximately in the last sixteen years of his life, which means he started when he was already at the mature age of fifty' (S1); composition range (RQ-Z9-N1); 0.5."}
  era_bucket: {value: "-500 to 499", certainty: 1.0, cites: [{source: S1, locator: "1. Life and Writings"}], how_known: "254, and every year of his life, falls in -500 to 499 (P2)."}
  region_of_birth: {value: "Middle East and North Africa", certainty: 0.5, cites: [{source: S1, locator: "1. Life and Writings"}], how_known: "Egypt (P3)."}
  region_of_work: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Writings"}], how_known: "Rome, where the span took place (AA6 rule); home-region alternative MENA."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Ancient Greek"], certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Treatises in Greek; inferred from the Greek terms SEP quotes."}
  occupations: {value: ["philosopher", "teacher"], certainty: 0.7, cites: [{source: S1, locator: "1. Life and Writings"}], how_known: "SEP."}

contribution:
  fields: {value: ["philosophy", "metaphysics"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "SEP."}
  lasting_original_contributions:
    - {value: "The treatises collected by Porphyry as the Enneads (the One, Intellect, Soul)", year: 254, kind: "body of work", lasting: "'Plotinus is generally regarded as the founder of Late Antique Platonism, sometimes termed Neoplatonism'; 'one of the supreme intellectual achievements of the period that has come to be called Late Antiquity' (S1)", certainty: 0.5, cites: [{source: S1, locator: "1. Life and Writings; opening"}], how_known: "Composed from about 254 to 270 (S1)."}
  evidence_of_impact:
    - {value: "Founder of Neoplatonism; influence on the Middle Ages and Renaissance", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Founder of Neoplatonism (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household: []
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling:
    - {value: "Studied with Ammonius Saccas in Alexandria from age 28, for eleven years", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Writings"}], how_known: "SEP."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "254–270", certainty: 0.5, cites: [{source: S1, locator: "1. Life and Writings"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: 
    value: PLATO
    basis: scholarly_reconstruction
    certainty: 0.5
    cites: [{source: S1, locator: "opening; 1. Life and Writings"}]
    how_known: "Scholar's reconstruction: SEP (Kalligas)."
    rationale: "'Plato's figure dominates Plotinus' thought, constituting the key source of inspiration for [his] worldview' (S1); founder of Late Antique Platonism. 0.5: reconstruction from one scholarly source."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: PLATO, reason: "Coded at 0.5 (S1)."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "The One is the 'supreme ontological principle', 'beyond being' (S1): transcendent (A 1 lead); but all other principles come to be by 'emanation' from it (S1) (A 2 lead). No reading reaches 0.5 over the other."}
    B_cause:
      value: 3
      basis: scholarly_reconstruction
      certainty: 0.5
      cites: [{source: S1, locator: "§2"}]
      how_known: "Scholarly reconstruction (P49, RQ-AA8-1 resolved yes by Jason, 2026-10-21). Not a scientist (P30). SEP §2 (read in full) reconstructs his account of nature: the laws of Nature 'remain constant and immutable' (III 1.10) and the same causes 'inexorably produce the same effects, provided that no other exogenous factor enters into play'. 0.5 is the scholarly_reconstruction ceiling."
      rationale: "Account of nature (P6): constant laws and fixed causation, with the stated proviso of an 'exogenous factor' as the limited exception, so B 3. Alternative 2 if the proviso is read as an open door for the soul's and higher principles' action in nature."
      alternatives:
        - {value: 2, note: "Proviso read as an unlimited exception.", cites: [{source: S1, locator: "§2"}]}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD, so the P4 test cannot be applied (Pavlov pattern)."}
  statements: []
  changes_over_life: []
  coder_notes: "The SEP sentence behind PLATO ('Plato's figure dominates Plotinus' thought ...') is a scholar's summary, not his words, so it is not listed as a statement (AA8 audit: an encyclopedia entry is not a scholarly edition under P21). He opposed the Gnostics' malevolent creator and upheld the goodness of the sensible world (S1). PLATO system file: check its axes against the One."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "254–270", certainty: 0.5, cites: [{source: S1, locator: "1. Life and Writings"}], how_known: "Composition range of the treatises, about 254 to his death in 270 (RQ-Z9-N1); start inferred, 0.5."}
  age_at_first_lasting_contribution: {value: 50, certainty: 0.5, cites: [{source: S1, locator: "1. Life and Writings"}], how_known: "254 − 204 = 50 (P30 year difference); S1: 'he started when he was already at the mature age of fifty'."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Metaphysics of the One (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions: []
collaborators:
  - {value: "Ammonius Saccas", relation: "teacher", note: "Alexandria", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Writings"}], how_known: "SEP."}
  - {value: "Porphyry", relation: "student or assistant", note: "editor of the Enneads; Life of Plotinus", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Writings"}], how_known: "SEP."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 211"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Span and age inferred (0.5)."
  open_questions:
    - "A_locus reading of the One (transcendent vs emanationist)."
    - "B rests on a scholarly reconstruction (P49); a primary passage (Enneads III 1.10) would lift it."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Paul Kalligas"
    citation: "Kalligas, Paul. 'Plotinus.' Stanford Encyclopedia of Philosophy (2024). https://plato.stanford.edu/entries/plotinus/"
    url: "https://plato.stanford.edu/entries/plotinus/"
    accessed: 2026-10-19
    reliability_note: "Signed entry, read in full."
    used_for: [identity, basics, contribution, childhood, worldview, timing, collaborators]
  - id: S2
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [review]
---

## Summary

Plotinus (204–270), founder of Neoplatonism [S1]. Draft: PLATO (0.5). Not plotted.

## Life and work

Egypt; Alexandria; Rome [S1].

## Contribution and impact

Enneads, c. 254–270 [S1].

## Childhood and education

Ammonius Saccas [S1].

## Adult working worldview

Plato dominates his thought [S1].

## Heritage (context only)

Not stated.

## Timing

254–270 (0.5), age 50 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- A reading.

## Research log

- 2026-10-20: AA8 audit fixes: B reason corrected (SEP §2 does set out a view of nature); B stays UNKNOWN pending RQ-AA8-1; SEP summary dropped as a statement (not a scholarly edition); 'mature age of fifty' cited.
- 2026-10-19: Read SEP (Kalligas).
- 2026-10-21: RQ-AA8-1 resolved yes by Jason (2026-10-21, P49): B 3 at 0.5 from SEP's reconstruction (basis scholarly_reconstruction), alternative 2. Still not plotted (A BELOW_THRESHOLD).
