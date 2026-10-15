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
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch K, order P32: F 5, rank 67). Basics from Britannica (Ernst van de Wetering), signed body through 'Early years' only; Top Questions not cited. No worldview statement read. primary_system UNKNOWN; A, B, C, D, E UNKNOWN; mid_basin UNKNOWN (P19). Not plotted. Draft, not reviewed."}

identity:
  id: rembrandt
  display_name: "Rembrandt"
  roster:
    canonical_name: "Rembrandt"
    rank: 67
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: art
    field_bucket: arts
  full_name: {value: "Rembrandt Harmenszoon van Rijn", certainty: 0.7, cites: [{source: S1, locator: "header ('In full')"}], how_known: "Britannica."}
  native_name: {value: UNKNOWN, how_known: "Dutch, Latin script."}
  aliases:
    - {name: "Rembrandt van Rijn", kind: "roster alias"}

basics:
  birth:
    date: {value: "1606-07-15", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica; Holland used the Gregorian calendar."}
    place: {value: "Leiden, Dutch Republic", modern_name: "Leiden, Netherlands", polity_then: "Dutch Republic", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "1669-10-04", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Amsterdam, Dutch Republic", modern_name: "Amsterdam, Netherlands", polity_then: "Dutch Republic", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1642, certainty: 0.5, cites: [{source: S1, locator: "opening section ('Night Watch (1640/42)')"}], how_known: "The only work the signed body read dates; earlier works are dated only in the Top Questions box, which is not cited. End year of 1640/42 (0.5)."}
  era_bucket: {value: "1600 to 1749", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "Whole life in the bucket (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Netherlands (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Leiden, Amsterdam."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [Dutch], certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading (0.5)."}
  occupations: {value: ["painter", "printmaker"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
contribution:
  fields: {value: ["painting", "printmaking"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Night Watch", year: 1642, kind: work, lasting: "'clearly a turning point in his stylistic development' (S1)", certainty: 0.5, cites: [{source: S1, locator: "opening section"}], how_known: "Dated 1640/42; end year used (0.5)."}
  evidence_of_impact:
    - {value: "Regarded from the Romantic era 'as one of the greatest figures in art history'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening section"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father Harmen Gerritszoon van Rijn, miller; mother Neeltgen Willemsdochter van Zuytbrouck, from a family of bakers", role: parents, certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  household_circumstances: {value: "Fourth of six surviving children of ten; not from a family of artists", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  schooling:
    - {value: "Elementary school (c. 1612–16)", stage: "elementary school", run_by: other, certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
    - {value: "Latin School, Leiden (c. 1616–20): biblical studies and classics", stage: "grammar or secondary school", run_by: other, certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica; completion unclear."}
    - {value: "Enrolled at Leiden University, 20 May 1620, probably without attending", stage: university, run_by: other, certainty: 0.5, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica says enrolment did not imply attendance."}
    - {value: "Trained with Jacob van Swanenburgh (Leiden, about three years), then Pieter Lastman (Amsterdam, six months)", stage: apprenticeship, run_by: private, certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica, after Orlers (1641)."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: TODO}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1642", certainty: 0.5, cites: [{source: S1, locator: "opening section"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: {value: UNKNOWN, how_known: "No statement read; biblical 'history pieces' are commissions and subjects, not avowed belief."}
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
  coder_notes: "Coder's call; few writings of his survive. Subject matter is not avowed belief."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Dutch (Leiden)", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1642", certainty: 0.5, cites: [{source: S1, locator: "opening section"}], how_known: "Only one dated listed contribution (P29, P30); TODO: date earlier works from the signed body."}
  age_at_first_lasting_contribution: {value: 36, certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "1642 − 1606 = 36 (P30)."}
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
  - {value: "Pieter Lastman", relation: teacher, certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  - {value: "Jan Lievens", relation: collaborator, certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Worked closely together after c. 1625."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 67"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags: []
  open_questions:
    - "Read the rest of the signed body (Leiden period onward) to date earlier works."
    - "Find any letters of his on religion."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Ernst van de Wetering"
    citation: "van de Wetering, Ernst. \"Rembrandt.\" Encyclopaedia Britannica, updated 30 September 2026. https://www.britannica.com/biography/Rembrandt-van-Rijn."
    url: "https://www.britannica.com/biography/Rembrandt-van-Rijn"
    accessed: 2026-10-15
    reliability_note: "Signed body through 'Early years'; Top Questions not cited; later pages timed out."
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

# Rembrandt

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Rembrandt (1606–1669), Dutch Baroque painter and printmaker [S1]. Draft: all worldview fields UNKNOWN. Not plotted.

## Life and work

Leiden; training with van Swanenburgh and Lastman; Amsterdam [S1].

## Contribution and impact

Night Watch (1640/42) [S1].

## Childhood and education

Latin School, Leiden [S1].

## Adult working worldview

No statement read [S1].

## Heritage (context only)

See front matter [S1].

## Timing

First dated lasting contribution 1642, at 36 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Unclear [S1].

## Open questions

- Read the rest of the signed body to date earlier works.

## Research log

- 2026-10-15: Read Britannica (van de Wetering) opening and 'Early years'.
