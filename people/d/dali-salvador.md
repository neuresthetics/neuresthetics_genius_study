---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch K)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-15
  change_log:
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch K, order P32: F 5, rank 71). Basics from Britannica (Britannica Editors, unsigned); Top Questions not cited. No worldview statement read; the 1950–70 religious-themed paintings are subjects, not avowed belief. primary_system UNKNOWN; A, B, C, D, E UNKNOWN; mid_basin UNKNOWN (P19). Not plotted. Draft, not reviewed."}

identity:
  id: dali-salvador
  display_name: "Salvador Dalí"
  roster:
    canonical_name: "Salvador Dalí"
    rank: 71
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: art
    field_bucket: arts
  full_name: {value: "Salvador Felipe Jacinto Dalí y Domenech", certainty: 0.7, cites: [{source: S1, locator: "header ('In full')"}], how_known: "Britannica."}
  native_name: {value: UNKNOWN, how_known: "Catalan/Spanish, Latin script."}
  aliases:
    - {name: "Salvador Dali", kind: "roster alias"}

basics:
  birth:
    date: {value: "1904-05-11", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Figueras, Catalonia, Spain", modern_name: "Figueres, Spain", polity_then: "Kingdom of Spain", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "1989-01-23", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Figueras, Spain", modern_name: "Figueres, Spain", polity_then: "Spain", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1929, certainty: 0.7, cites: [{source: S1, locator: "'Surrealism'"}], how_known: "Un Chien andalou (1929), with Buñuel; his mature style dates from 1929 (S1)."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "Birth year bucket (P2)."}
  region_of_birth: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Spain (P3)."}
  region_of_work: {value: "Southern Europe", certainty: 0.5, cites: [{source: S1, locator: "'Surrealism'; 'Later career'"}], how_known: "Spain and Paris; United States 1940–55 (0.5)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [Spanish, French], certainty: 0.5, cites: [{source: S1, locator: "'Early life'"}], how_known: "Catalan at home; Spanish and French learned (0.5)."}
  occupations: {value: ["painter", "printmaker", "filmmaker"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
contribution:
  fields: {value: ["painting", "film"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Un Chien andalou (with Luis Buñuel)", year: 1929, kind: work, lasting: "Surrealist film (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Surrealism'"}], how_known: "Britannica."}
    - {value: "The Persistence of Memory", year: 1931, kind: work, lasting: "'Perhaps the most famous of those enigmatic images' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Surrealism'"}], how_known: "Britannica."}
  evidence_of_impact:
    - {value: "'the best-known Surrealist artist' for his 1929–37 paintings", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "'Surrealism'"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Atheist father; Roman Catholic mother", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica: father 'a notary, atheist, and Republican'; mother 'a Roman Catholic'."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father Salvador Dalí Cusí, notary; mother Felipa Domènech Ferrés (d. 1921)", role: parents, certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}
  household_circumstances: {value: "An elder brother, also named Salvador, died nine months before his birth; sister Ana María born 1908", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}
  schooling:
    - {value: "Real Academia de Bellas Artes de San Fernando, Madrid (from c. 1921)", stage: "other", run_by: "state or municipal", certainty: 0.5, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica; art academy (0.5)."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [Catalan], certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}
  notable_events:
    - {value: "Death of his mother", year: 1921, certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1929–1931", certainty: 0.7, cites: [{source: S1, locator: "'Surrealism'"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: {value: UNKNOWN, how_known: "No statement read. The religious-themed paintings of 1950–70 are subjects, not avowed belief, and fall after the working years."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered: []
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "No statement read."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist; nothing read (P16)."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read (P7)."}
  mid_basin: {value: UNKNOWN, how_known: "A and B UNKNOWN (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "Coder's call. The Secret Life of Salvador Dalí (1942) is the lead for any statement."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Catalan", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Catholic mother, atheist father", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1929–1931", certainty: 0.7, cites: [{source: S1, locator: "'Surrealism'"}], how_known: "First to last listed lasting contribution (P29, P30)."}
  age_at_first_lasting_contribution: {value: 25, certainty: 0.7, cites: [{source: S1, locator: "opening; 'Surrealism'"}], how_known: "1929 − 1904 = 25 (P30)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None read."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "None read."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Not read."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Not read.", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Not read."}
  circle_present: {value: "unclear", rationale: "No worldview statement read.", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  reading: "No scorable worldview statement."
  notes: ""

institutions: []
collaborators:
  - {value: "Luis Buñuel", relation: collaborator, certainty: 0.7, cites: [{source: S1, locator: "'Surrealism'"}], how_known: "Two films."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 71"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags: []
  open_questions:
    - "Read The Secret Life of Salvador Dalí (1942) for a statement on God or nature."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "Britannica Editors. \"Salvador Dalí.\" Encyclopaedia Britannica, updated 29 August 2026. https://www.britannica.com/biography/Salvador-Dali."
    url: "https://www.britannica.com/biography/Salvador-Dali"
    accessed: 2026-10-15
    reliability_note: "Unsigned editors' body; Top Questions not cited."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, collaborators]
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

# Salvador Dalí

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Salvador Dalí (1904–1989), Spanish Surrealist painter and filmmaker [S1]. Draft: all worldview fields UNKNOWN. Not plotted.

## Life and work

Figueras; Madrid academy; Paris Surrealists; United States 1940–55 [S1].

## Contribution and impact

Un Chien andalou (1929); The Persistence of Memory (1931) [S1].

## Childhood and education

Atheist father, Catholic mother [S1].

## Adult working worldview

No statement read [S1].

## Heritage (context only)

Catalan [S1].

## Timing

First lasting contribution 1929, at 25 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Unclear [S1].

## Open questions

- The Secret Life of Salvador Dalí (1942).

## Research log

- 2026-10-15: Read Britannica (Editors) full body.
