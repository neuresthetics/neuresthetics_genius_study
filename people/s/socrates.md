---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch L)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-15
  change_log:
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch L, order P32: F 5, rank 73). Basics from Britannica (Richard Kraut), signed body through 'Xenophon'; Top Questions not cited. Socrates wrote nothing; his words survive only as character speech in Plato and Xenophon, and scholars disagree which dialogues convey the historical Socrates (S1), so nothing is scored (P42). primary_system UNKNOWN; A–E UNKNOWN; mid_basin UNKNOWN (P19). First lasting contribution UNKNOWN (undated, P39). Not plotted. Draft, not reviewed."}

identity:
  id: socrates
  display_name: "Socrates"
  roster:
    canonical_name: "Socrates"
    rank: 73
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: philosophy
    field_bucket: philosophy
  full_name: {value: "Socrates", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  native_name: {value: "Σωκράτης", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Greek form; coder's transcription (0.5)."}
  aliases: []

basics:
  birth:
    date: {value: "-470", calendar: julian, certainty: 0.5, cites: [{source: S1, locator: "opening ('c. 470 bce')"}], how_known: "Britannica gives c. 470 BCE (0.5); proleptic Julian."}
    place: {value: "Athens", modern_name: "Athens, Greece", polity_then: "Athens", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "-399", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Athens", modern_name: "Athens, Greece", polity_then: "Athens", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: UNKNOWN, how_known: "He wrote nothing; his conversations are undated (P39)."}
  era_bucket: {value: "-500 to 499", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "Whole life in the bucket (P2)."}
  region_of_birth: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Greece (P3)."}
  region_of_work: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Athens."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [Ancient Greek], certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading (0.5)."}
  occupations: {value: ["philosopher"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
contribution:
  fields: {value: ["philosophy", "ethics"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Socratic conversation (questioning about the human excellences), known through Plato and Xenophon", kind: method, lasting: "'profound influence on Classical antiquity and Western philosophy' (S1)", certainty: 0.5, cites: [{source: S1, locator: "opening; 'Philosophical and literary sources'"}], how_known: "Undated (P39); reconstructed from others' writings (0.5)."}
  evidence_of_impact:
    - {value: "His thought 'exerted a profound influence on Classical antiquity and Western philosophy'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
  parents_and_household: []
  household_circumstances: {value: TODO}
  schooling: []
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: TODO}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: UNKNOWN, how_known: "Equals timing.major_work_period (UNKNOWN, P39)."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "He wrote nothing."}
  primary_system: {value: UNKNOWN, how_known: "He wrote nothing; his views come only through Plato's and Xenophon's characters, and scholars disagree which dialogues convey the historical Socrates (S1). No source read attributes a specific theology to the historical Socrates (P42)."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered: []
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "No attributable statement (P42). Plato's Apology and Xenophon's Memorabilia I are the leads."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist; nothing attributable (P16, P42)."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read (P7)."}
  mid_basin: {value: UNKNOWN, how_known: "A and B UNKNOWN (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "Coder's call. The charge of impiety (S1) is the accusers' claim, not his avowed view; Britannica's Top Questions box (AI-generated) says he 'did reject the city's gods' and is not cited."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Athenian", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: UNKNOWN, how_known: "Undated (P39)."}
  age_at_first_lasting_contribution: {value: UNKNOWN, how_known: "Undated (P39)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None attributable."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "None attributable."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Not attributable."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Wrote nothing.", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Not known."}
  circle_present: {value: "unclear", rationale: "No attributable statement.", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  reading: "No scorable worldview statement."
  notes: ""

institutions: []
collaborators:
  - {value: "Plato", relation: "student or assistant", certainty: 0.7, cites: [{source: S1, locator: "'Philosophical and literary sources'"}], how_known: "Member of his circle."}
  - {value: "Xenophon", relation: "student or assistant", certainty: 0.7, cites: [{source: S1, locator: "'Xenophon'"}], how_known: "Member of his circle."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 73"}], how_known: "Study roster."}
  controversies:
    - {value: "Which dialogues convey the historical Socrates", certainty: 0.7, cites: [{source: S1, locator: "'Philosophical and literary sources'"}], how_known: "Britannica."}
  data_quality_flags: []
  open_questions:
    - "Find a scholarly source that attributes a specific religious view (e.g. the daimonion, piety in the Apology) to the historical Socrates (P42)."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Richard Kraut"
    citation: "Kraut, Richard. \"Socrates.\" Encyclopaedia Britannica, updated 29 August 2026. https://www.britannica.com/biography/Socrates."
    url: "https://www.britannica.com/biography/Socrates"
    accessed: 2026-10-15
    reliability_note: "Signed body through 'Xenophon'; Top Questions not cited."
    used_for: [identity, basics, contribution, worldview, heritage, timing, lane_b, collaborators, review]
  - id: S2
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Socrates

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Socrates (c. 470–399 BCE), Athenian philosopher who wrote nothing [S1]. Draft: all worldview fields UNKNOWN (P42). Not plotted.

## Life and work

Athens; tried for impiety and executed, 399 BCE [S1].

## Contribution and impact

Known through Plato and Xenophon [S1].

## Childhood and education

Not read [S1].

## Adult working worldview

Nothing attributable [S1].

## Heritage (context only)

Athenian [S1].

## Timing

Undated [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Unclear [S1].

## Open questions

- A scholarly attribution of a specific religious view to the historical Socrates.

## Research log

- 2026-10-15: Read Britannica (Kraut) opening through 'Xenophon'.
