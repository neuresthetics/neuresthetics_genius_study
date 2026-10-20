---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA6)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA6, order P32: F 3, rank 204). Sources: MIT News obituary (2016, read in full) and Patrick Winston's CSAIL obituary (read in full). Lasting work: co-founding the MIT AI Laboratory (1959, S1), which with his early papers 'firmly established Minsky as one of the founders of Artificial Intelligence' (S2); the Theory of Frames (mid-1970s), with 'high impact on Artificial Intelligence as an emerging engineering discipline' (S2), dated 1974 at 0.5 (S2 says 'mid 1970s'); The Society of Mind (1985), 'considered a seminal exploration of intellectual structure and function' (S1). Span 1959–1985, age 32. Not a scientist as listed, following McCarthy (RQ-AA3-1): an institution, a knowledge-representation scheme and a theory of mind's architecture make no testable claim about nature as listed. Worldview: no own words read; lead ATHE (secondary web summaries of a Closer To Truth interview, not read). primary_system UNKNOWN; A UNKNOWN; B UNKNOWN; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}

identity:
  id: minsky-marvin
  display_name: "Marvin Minsky"
  roster:
    canonical_name: "Marvin Minsky"
    rank: 204
    F: 3
    models: [Claude, DeepSeek, GPT]
    band: "core (3–4)"
    status: "core"
    field: "computer science"
    field_bucket: "computer science / AI"
  full_name: {value: "Marvin Minsky", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "MIT News."}
  native_name: {value: "Marvin Minsky", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "MIT News."}
  aliases:
    - {name: "Marvin-Minsky", kind: "roster alias"}

basics:
  birth:
    date: {value: "1927-08-09", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "MIT News."}
    place: {value: "New York City", modern_name: "New York City, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S2, locator: "text"}], how_known: "Winston; MIT News: 'A native New Yorker'."}
  death:
    date: {value: "2016-01-24", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "MIT News."}
    place: {value: "Boston, Massachusetts", modern_name: "Boston, Massachusetts, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "MIT News: Brigham and Women's Hospital."}
  first_lasting_contribution_year: {value: 1959, certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Co-founded the AI Laboratory 'the following year' after joining MIT in 1958 (S1)."}
  era_bucket: {value: "1950 on", certainty: 1.0, cites: [{source: S1, locator: "text"}], how_known: "1959 (P2)."}
  region_of_birth: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "USA (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "MIT."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "English books."}
  occupations: {value: ["computer scientist", "mathematician", "professor"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "MIT News."}

contribution:
  fields: {value: ["artificial intelligence", "computer science", "cognitive science"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "MIT News."}
  lasting_original_contributions:
    - {value: "MIT Artificial Intelligence Laboratory (co-founded with John McCarthy)", year: 1959, kind: "institution", lasting: "with his early work, 'firmly established Minsky as one of the founders of Artificial Intelligence' (S2); now CSAIL (S1)", certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S2, locator: "text"}], how_known: "MIT News: 1959; Winston: 'late 1950s', as the AI Group."}
    - {value: "Theory of Frames ('A Framework for Representing Knowledge')", year: 1974, kind: "theory", lasting: "'had high impact on Artificial Intelligence as an emerging engineering discipline: the popular expert-system shells ... all offered tools for ... frames' (S2)", certainty: 0.5, cites: [{source: S2, locator: "text"}], how_known: "Winston: 'mid 1970s'; 1974 not printed in the sources read."}
    - {value: "The Society of Mind", year: 1985, kind: "work", lasting: "'considered a seminal exploration of intellectual structure and function' (S1)", certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S2, locator: "text"}], how_known: "MIT News and Winston: 1985."}
  evidence_of_impact:
    - {value: "A.M. Turing Award (1969)", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "MIT News."}
  major_works:
    - {value: "First neural network simulator", year: 1951, kind: "device", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "MIT News."}
    - {value: "The Emotion Machine", year: 2006, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "MIT News."}
  honours:
    - {value: "A.M. Turing Award", year: 1969, certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "MIT News."}
    - {value: "Japan Prize", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "MIT News; year not given."}
  definition_fit: {value: "clearly meets", rationale: "One of the founders of AI (S2).", certainty: 0.7, cites: [{source: S2, locator: "text"}], how_known: "Winston."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household: []
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling:
    - {value: "Fieldston School; Bronx High School of Science; Phillips Academy; Harvard (BA 1950); Princeton (PhD mathematics 1954)", certainty: 0.7, cites: [{source: S2, locator: "text"}, {source: S1, locator: "text"}], how_known: "Winston; MIT News."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1959–1985", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: {value: UNKNOWN, how_known: "No own words on belief read. Lead ATHE from secondary summaries of a Closer To Truth interview (not read)."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: ATHE, reason: "Lead only: unread interview."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing first-hand read (P19)."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist as listed (P30, P33; RQ-AA3-1 McCarthy precedent); no statement on nature read."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, so the P4 test cannot be applied (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "Read the Closer To Truth interview transcript or The Society of Mind's 'Soul' chapter for own words."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated in the sources read."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1959–1985", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "AI Laboratory (1959) to The Society of Mind (1985), the first and last listed lasting items (P29, P30)."}
  age_at_first_lasting_contribution: {value: 32, certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "1959 − 1927 = 32 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "AI and theory of mind (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "Massachusetts Institute of Technology", role: "professor; co-founder of the AI Laboratory; founding member of the Media Lab", years: "1958–2016", kind: "university", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "MIT News."}
collaborators:
  - {value: "John McCarthy", relation: "collaborator", note: "co-founded the AI Laboratory", certainty: 0.7, cites: [{source: S2, locator: "text"}], how_known: "Winston."}
  - {value: "Seymour Papert", relation: "collaborator", note: "Perceptrons; Society of Mind theory", certainty: 0.7, cites: [{source: S2, locator: "text"}], how_known: "Winston."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 204"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Worldview: no source read; scientist status per RQ-AA3-1."
  open_questions:
    - "Own words on religion; scientist status (frames, Society of Mind)."

sources:
  - id: S1
    type: secondary
    kind: "institutional page"
    author: "MIT News Office"
    citation: "'Marvin Minsky, \"father of artificial intelligence,\" dies at 88.' MIT News, 25 January 2016. https://news.mit.edu/2016/marvin-minsky-obituary-0125"
    url: "https://news.mit.edu/2016/marvin-minsky-obituary-0125"
    accessed: 2026-10-19
    reliability_note: "Institutional obituary, read in full."
    used_for: [identity, basics, contribution, timing, institutions]
  - id: S2
    type: secondary
    kind: "other"
    author: "Patrick H. Winston"
    citation: "Winston, Patrick H. 'Marvin Minsky' (obituary). MIT CSAIL. https://people.csail.mit.edu/phw/obituary.html"
    url: "https://people.csail.mit.edu/phw/obituary.html"
    accessed: 2026-10-19
    reliability_note: "Obituary by a colleague and former student, read in full."
    used_for: [contribution, childhood, collaborators]
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

Marvin Minsky (1927–2016), AI pioneer [S1, S2]. Draft: worldview UNKNOWN. Not plotted.

## Life and work

New York; Harvard; Princeton; MIT [S1, S2].

## Contribution and impact

AI Lab 1959; frames; Society of Mind 1985 [S1, S2].

## Childhood and education

Bronx Science; Harvard [S2].

## Adult working worldview

None read.

## Heritage (context only)

Not stated.

## Timing

1959–1985, age 32 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Own words.

## Research log

- 2026-10-19: Read MIT News and Winston obituaries.
