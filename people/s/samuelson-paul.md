---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA8)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA8, order P32: F 3, rank 209). Sources: Britannica (scholars edition, unsigned, read in full) and NobelPrize.org facts page (read in full). Lasting work: the textbook Economics (1948), 'considered a classic' (S1) and 'the world's best selling economic textbook' (S2). Span 1948, age 33. Foundations of Economic Analysis (1947), the multiplier–accelerator model and revealed preference are 'of particular influence' (S1) but undated in the sources read or not called lasting; recorded as major works. Economist, not a scientist (Friedman precedent). Worldview: no own words read; born into a Jewish family that emigrated from Poland (S2). primary_system UNKNOWN; A UNKNOWN; B UNKNOWN; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}

identity:
  id: samuelson-paul
  display_name: "Paul Samuelson"
  roster:
    canonical_name: "Paul Samuelson"
    rank: 209
    F: 3
    models: [Claude, Gemini, GPT]
    band: "core (3–4)"
    status: "core"
    field: "economics"
    field_bucket: "social science"
  full_name: {value: "Paul Anthony Samuelson", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  native_name: {value: "Paul Samuelson", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  aliases:
    - {name: "Paul-Samuelson", kind: "roster alias"}
    - {name: "Samuelson-Paul", kind: "roster alias"}

basics:
  birth:
    date: {value: "1915-05-15", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Born"}], how_known: "Britannica; Nobel."}
    place: {value: "Gary, Indiana", modern_name: "Gary, Indiana, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "2009-12-13", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Belmont, Massachusetts", modern_name: "Belmont, Massachusetts, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1948, certainty: 0.7, cites: [{source: S1, locator: "para. 4"}], how_known: "Economics (1948), 'considered a classic' (S1); publication (P30)."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "para. 4"}], how_known: "1948 (P2)."}
  region_of_birth: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "USA (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "para. 2"}], how_known: "MIT."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "English."}
  occupations: {value: ["economist", "professor", "columnist"], certainty: 0.7, cites: [{source: S1, locator: "para. 2, 4"}], how_known: "Britannica."}

contribution:
  fields: {value: ["economics"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Economics: An Introductory Analysis (textbook)", year: 1948, kind: "work", lasting: "'considered a classic' (S1); 'has become the world's best selling economic textbook' (S2)", certainty: 0.7, cites: [{source: S1, locator: "para. 4"}, {source: S2, locator: "Life"}], how_known: "Britannica; Nobel."}
  evidence_of_impact:
    - {value: "Nobel Prize in Economic Sciences 1970, 'for his fundamental contributions to nearly all branches of economic theory'", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Prize motivation"}], how_known: "Britannica; Nobel."}
  major_works:
    - {value: "Foundations of Economic Analysis", year: 1947, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "para. 3"}], how_known: "Britannica: 'provides the basic theme of his work'."}
    - {value: "Multiplier–accelerator model; theory of revealed preference", year: UNKNOWN, kind: "paper or paper series", certainty: 0.7, cites: [{source: S1, locator: "para. 3"}], how_known: "Britannica: 'Of particular influence'; undated in S1."}
  honours:
    - {value: "Nobel Prize in Economic Sciences", year: 1970, certainty: 0.7, cites: [{source: S2, locator: "Prize motivation"}], how_known: "Nobel."}
  definition_fit: {value: "clearly meets", rationale: "Nobel laureate; classic textbook (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Jewish family that had emigrated from Poland", role: "family", certainty: 0.7, cites: [{source: S2, locator: "Life"}], how_known: "Nobel."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling:
    - {value: "University of Chicago (BA 1935); Harvard (PhD 1941)", certainty: 0.7, cites: [{source: S1, locator: "para. 2"}], how_known: "Britannica."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1948", certainty: 0.7, cites: [{source: S1, locator: "para. 4"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: {value: UNKNOWN, how_known: "No own words on belief read."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: JUDA, reason: "Heritage only: Jewish family (S2)."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing first-hand read (P19)."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30; Friedman precedent); no statement on nature read."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, so the P4 test cannot be applied (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "Read his autobiographical essays (e.g. in Collected Scientific Papers) for own words."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: "Jewish", certainty: 0.7, cites: [{source: S2, locator: "Life"}], how_known: "Nobel: 'born ... into a Jewish family that had emigrated from Poland'."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1948", certainty: 0.7, cites: [{source: S1, locator: "para. 4"}], how_known: "The one listed lasting item (P29, P30)."}
  age_at_first_lasting_contribution: {value: 33, certainty: 0.7, cites: [{source: S1, locator: "opening; para. 4"}], how_known: "1948 − 1915 = 33 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Mathematical economics (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "Massachusetts Institute of Technology", role: "professor of economics", years: "1940–2009", kind: "university", certainty: 0.7, cites: [{source: S1, locator: "para. 2"}], how_known: "Britannica."}
collaborators: []

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 209"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Worldview: no source."
  open_questions:
    - "A dated lasting source for Foundations (1947) or revealed preference would widen the span."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "The Editors of Encyclopaedia Britannica"
    citation: "'Paul Samuelson.' Encyclopaedia Britannica (scholars edition). https://kids.britannica.com/scholars/article/Paul-Samuelson/65248"
    url: "https://kids.britannica.com/scholars/article/Paul-Samuelson/65248"
    accessed: 2026-10-19
    reliability_note: "Unsigned article, read in full."
    used_for: [identity, basics, contribution, timing, institutions]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "Nobel Prize Outreach"
    citation: "'Paul A. Samuelson – Facts.' NobelPrize.org. https://www.nobelprize.org/prizes/economic-sciences/1970/samuelson/facts/"
    url: "https://www.nobelprize.org/prizes/economic-sciences/1970/samuelson/facts/"
    accessed: 2026-10-19
    reliability_note: "Facts page, read in full."
    used_for: [identity, contribution, childhood, heritage]
  - id: S3
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

Paul Samuelson (1915–2009), economist [S1]. Draft: worldview UNKNOWN. Not plotted.

## Life and work

Gary; Chicago; Harvard; MIT [S1].

## Contribution and impact

Economics (1948) [S1, S2].

## Childhood and education

Chicago; Harvard [S1].

## Adult working worldview

None read.

## Heritage (context only)

Jewish [S2].

## Timing

1948, age 33 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Wider span.

## Research log

- 2026-10-19: Read Britannica (scholars edition); Nobel facts.
