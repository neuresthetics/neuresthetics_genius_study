---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z7)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z7, order P32: F 3, rank 161). Basics from Britannica (body). His words on God (Music Is My Mistress, 1973, pp. 262, 267–269: 'Every man prays in his own language, and there is no language that God does not understand'; 'Now I can say openly what I have been saying to myself on my knees') were seen only as quoted on secondary pages; the archive.org scans are borrow-only and were not read. Second-hand quotations alone (V3), so primary_system UNKNOWN (lead CHRIST); A, B, C, D, E UNKNOWN; mid_basin UNKNOWN. Not a scientist. Span 1926–1943. Not plotted. Draft, not reviewed."}

identity:
  id: ellington-duke
  display_name: "Duke Ellington"
  roster:
    canonical_name: "Duke Ellington"
    rank: 161
    F: 3
    models: [Claude, Gemini, GPT]
    band: "core (3–4)"
    status: "review"
    field: "music"
    field_bucket: "music"
  full_name: {value: "Edward Kennedy Ellington", certainty: 0.7, cites: [{source: S1, locator: "Also known as"}], how_known: "Britannica."}
  native_name: {value: "Duke Ellington", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  aliases:
    - {name: "Edward Kennedy Ellington", kind: "birth name"}
    - {name: "Duke-Ellington", kind: "roster alias"}

basics:
  birth:
    date: {value: "1899-04-29", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Washington, D.C.", modern_name: "Washington, D.C., United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "1974-05-24", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "New York City", modern_name: "New York, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1926, certainty: 0.7, cites: [{source: S1, locator: "Ellington's ensemble"}], how_known: "'East St. Louis Toodle-oo' (1926), named among the 'masterpieces' of his early style."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "Ellington's ensemble"}], how_known: "1926 (P2)."}
  region_of_birth: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "USA (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "Ellington's ensemble"}], how_known: "New York; wide touring."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Inferred."}
  occupations: {value: ["pianist", "composer", "bandleader"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

contribution:
  fields: {value: ["jazz", "big-band jazz"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "'East St. Louis Toodle-oo' and 'Black and Tan Fantasy' (jungle style)", year: 1926, kind: "work", lasting: "'masterpieces' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Ellington's ensemble"}], how_known: "Britannica: 1926, 1927."}
    - {value: "Black, Brown and Beige", year: 1943, kind: "work", lasting: "first in a series of suites (S1)", certainty: 0.5, cites: [{source: S1, locator: "Classical forms"}], how_known: "Britannica; lastingness the coder's call, so the span end is 0.5."}
  evidence_of_impact:
    - {value: "The greatest jazz composer and bandleader of his time", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works:
    - {value: "Mood Indigo", year: 1930, kind: "composition", certainty: 0.7, cites: [{source: S1, locator: "Ellington's ensemble"}], how_known: "Britannica."}
    - {value: "Sacred Concerts (three)", year: 1973, kind: "composition", certainty: 0.7, cites: [{source: S1, locator: "Classical forms"}], how_known: "Britannica: 1965, 1968, 1973."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Greatest jazz composer of his time (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Methodist (father) and Baptist (mother) per a secondary summary of Music Is My Mistress; not read first-hand."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household: []
  household_circumstances: {value: "Secure middle-class family in Washington, D.C.", certainty: 0.7, cites: [{source: S1, locator: "Early life and career"}], how_known: "Britannica."}
  schooling: []
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1926–1943", certainty: 0.5, cites: [{source: S1, locator: "Ellington's ensemble; Classical forms"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: {value: UNKNOWN, how_known: "His words seen only second-hand (V3): Music Is My Mistress (1973), quoted on secondary pages, speaks of praying 'on my knees' and of God's 'total understanding'; also the three Sacred Concerts (work, not profession, P16). Lead CHRIST."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Lead: Sacred Concerts; prayer and God in his memoir (second-hand)."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Second-hand only (V3)."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30); 'miracles have happened' (second-hand, about honest communication) is not a statement about nature."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: UNKNOWN, how_known: "A and B are UNKNOWN (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "Read Music Is My Mistress (Doubleday 1973), pp. 259–270, first-hand (archive.org borrow copy, id musicismymistres00elli)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "African American", certainty: 0.7, cites: [{source: S1, locator: "Classical forms"}], how_known: "Britannica (portrayal of African-American history; My People)."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1926–1943", certainty: 0.5, cites: [{source: S1, locator: "Ellington's ensemble; Classical forms"}], how_known: "East St. Louis Toodle-oo (1926) to Black, Brown and Beige (1943) (P29, P30); end is the coder's call."}
  age_at_first_lasting_contribution: {value: 27, certainty: 0.7, cites: [{source: S1, locator: "opening; Ellington's ensemble"}], how_known: "1926 − 1899 = 27 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Music (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions: []
collaborators:
  - {value: "Billy Strayhorn", relation: "collaborator", note: "composing-arranging partner 1939–67", certainty: 0.7, cites: [{source: S1, locator: "Legacy"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Review in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 161"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Own words on religion seen only second-hand; the autobiography scan is borrow-only."
  open_questions:
    - "Music Is My Mistress first-hand."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Britannica Editors"
    citation: "'Duke Ellington.' Encyclopaedia Britannica (rev. 2026). https://www.britannica.com/biography/Duke-Ellington"
    url: "https://www.britannica.com/biography/Duke-Ellington"
    accessed: 2026-10-19
    reliability_note: "Unsigned editorial article; body cited, not the question boxes (P26)."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, collaborators]
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

Duke Ellington (1899–1974), jazz composer and bandleader [S1]. Draft: all worldview fields UNKNOWN (lead CHRIST). Not plotted.

## Life and work

Washington, New York, world tours [S1].

## Contribution and impact

Jungle style; Mood Indigo; suites; Sacred Concerts [S1].

## Childhood and education

Middle-class Washington family [S1].

## Adult working worldview

Not read first-hand.

## Heritage (context only)

African American [S1].

## Timing

1926–1943, age 27 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Music Is My Mistress first-hand.

## Research log

- 2026-10-19: Read Britannica; found the memoir quotes only second-hand.
