---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch J)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-15
  change_log:
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch J, order P32: F 5, rank 64). Basics from Britannica (McCully), signed body through 1903 (the fetch returned only that part). No worldview statement read. primary_system UNKNOWN; A, B, C, D, E UNKNOWN; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Audit fixes (fallacy_catalog audit of 81b9098, run 1). mid_basin BELOW_THRESHOLD -> UNKNOWN (P19)."}

identity:
  id: picasso-pablo
  display_name: "Pablo Picasso"
  roster:
    canonical_name: "Pablo Picasso"
    rank: 64
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: art
    field_bucket: arts
  full_name: {value: "Pablo Diego José Francisco de Paula Juan Nepomuceno Crispín Crispiniano María Remedios de la Santísima Trinidad Ruiz Picasso", certainty: 0.7, cites: [{source: S1, locator: "header ('In full')"}], how_known: "Britannica; sources vary on the order."}
  native_name: {value: UNKNOWN, how_known: "Spanish, Latin script."}
  aliases:
    - {name: "Pablo Ruiz", kind: "birth name"}

basics:
  birth:
    date: {value: "1881-10-25", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Málaga, Spain", modern_name: "Málaga, Spain", polity_then: "Kingdom of Spain", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "1973-04-08", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Mougins, France", modern_name: "Mougins, France", polity_then: "France", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1901, certainty: 0.5, cites: [{source: S1, locator: "'Discovery of Paris'"}], how_known: "Blue Period works from 1901 (P13); Cubism (his main lasting contribution) is dated only in the Top Questions box, not cited; 0.5."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S1, locator: "'Discovery of Paris'"}], how_known: "From 1901 (P2)."}
  region_of_birth: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Spain is Southern Europe in regions.csv (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.5, cites: [{source: S1, locator: "opening ('Spanish expatriate'); 'Discovery of Paris'"}], how_known: "France (Western Europe); coder's reading, 0.5."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [Spanish], certainty: 0.5, cites: [{source: S1, locator: "'Early years'"}], how_known: "Coder's reading (0.5); he also spoke Catalan (S1)."}
  occupations: {value: ["painter", "sculptor", "printmaker", "ceramicist", "stage designer"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
contribution:
  fields: {value: ["painting", "sculpture"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Cubism (with Georges Braque)", kind: theory, lasting: "(S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica; no year in the signed body read (P39)."}
    - {value: "Blue Period paintings", year: 1901, kind: work, lasting: "(S1)", certainty: 0.5, cites: [{source: S1, locator: "'Discovery of Paris'"}], how_known: "Begun 1901."}
    - {value: "La Vie", year: 1903, kind: work, lasting: "'enigmatic' (S1)", certainty: 0.5, cites: [{source: S1, locator: "'Discovery of Paris'"}], how_known: "Lasting status the coder's reading (0.5)."}
  evidence_of_impact:
    - {value: "'one of the greatest and most-influential artists of the 20th century'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father José Ruiz Blasco, professor of drawing; mother Maria Picasso López", role: parents, certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  household_circumstances: {value: TODO}
  schooling:
    - {value: "La Llotja art academy, Barcelona", stage: "grammar or secondary school", run_by: other, years: "1895–1897", ages: "14–16", certainty: 0.5, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica; stage and end year the coder's reading (0.5)."}
    - {value: "Royal Academy of San Fernando, Madrid", stage: other, run_by: other, years: "1897", ages: "16", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: TODO}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1901–1903", certainty: 0.5, cites: [{source: S1, locator: "'Discovery of Paris'"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: {value: UNKNOWN, how_known: "No statement read; Britannica says only that he 'superstitiously believed that work would keep him alive' (not a system)."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered: []
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "No statement read."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist; no statement on nature read (P16)."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read (P7)."}
  mid_basin: {value: UNKNOWN, how_known: "A is UNKNOWN; UNKNOWN takes precedence (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "Coder's call; no primary source on religion found in the time available. Collected interviews (e.g., Zervos, Gilot) would need P43-style handling."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Andalusian", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1901–1903", certainty: 0.5, cites: [{source: S1, locator: "'Discovery of Paris'"}], how_known: "First to last dated listed contribution (P29, P30); later works undated in the part read, so the end year is too early."}
  age_at_first_lasting_contribution: {value: 20, certainty: 0.5, cites: [{source: S1, locator: "opening; 'Discovery of Paris'"}], how_known: "1901 − 1881 = 20 (P30)."}
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

institutions:
  []
collaborators:
  - {value: "Georges Braque", relation: collaborator, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 64"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags: []
  open_questions:
    - "Find a primary statement on religion (letters; interview books under P43)."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Marilyn McCully"
    citation: "McCully, Marilyn. \"Pablo Picasso.\" Encyclopaedia Britannica, updated 15 October 2026. https://www.britannica.com/biography/Pablo-Picasso."
    url: "https://www.britannica.com/biography/Pablo-Picasso"
    accessed: 2026-10-15
    reliability_note: "Signed body (opening, 'Early years', 'Discovery of Paris'); Top Questions not cited."
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

# Pablo Picasso

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Pablo Picasso (1881–1973), Spanish painter and sculptor, co-creator of Cubism [S1]. Draft: all worldview fields UNKNOWN. Not plotted.

## Life and work

Málaga, A Coruña, Barcelona, Madrid, Paris [S1].

## Contribution and impact

See front matter [S1].

## Childhood and education

See front matter [S1].

## Adult working worldview

No statement read [S1].

## Heritage (context only)

See front matter [S1].

## Timing

See front matter [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Unclear [S1].

## Open questions

- Find a primary statement on religion (letters; interview books under P43).

## Research log

- 2026-10-15: Read Britannica (McCully) body through 1903.
