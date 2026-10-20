---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA5)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA5, order P32: F 3, rank 197). Sources: NASA biography by Margot Lee Shetterly (2016, read in full) and Presbyterian Church (U.S.A.) news (2017, read in full); Blount's statement (Union Presbyterian Seminary, 2020) seen as a search excerpt only. Lasting work: the orbital-flight equations of 'Determination of Azimuth Angle at Burnout for Placing a Satellite Over a Selected Earth Position' (1960, with Ted Skopinski), and the 1962 hand verification of John Glenn's orbital trajectory, 'the work that she would become most known for' (S1). Lasting status is arguable (no source calls a result lasting; 'pioneering legacy', S1), so 0.5; span 1960–1962 at 0.5, age 42. Not a scientist: trajectory computation applies known laws rather than stating a new result about nature (P30, by analogy with P33); ruling question RQ-AA5-1. Worldview: decades of church office (finance chair, choir, church officer; PC(USA) calls her a ruling elder) and her pastor's report of 'deep' Christian faith, but no profession of her own read, so BELOW_THRESHOLD with lead CHRIST (Toni Morrison precedent, RQ-Y2); ruling question RQ-AA5-2. A UNKNOWN; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}

identity:
  id: johnson-katherine
  display_name: "Katherine Johnson"
  roster:
    canonical_name: "Katherine Johnson"
    rank: 197
    F: 3
    models: [DeepSeek, GPT, Grok]
    band: "core (3–4)"
    status: "core"
    field: "mathematics"
    field_bucket: "mathematics"
  full_name: {value: "Katherine G. Johnson", certainty: 0.7, cites: [{source: S2, locator: "headline"}], how_known: "PC(USA)."}
  native_name: {value: "Katherine Johnson", certainty: 0.7, cites: [{source: S1, locator: "title"}], how_known: "NASA."}
  aliases:
    - {name: "Katherine-Johnson", kind: "roster alias"}

basics:
  birth:
    date: {value: "1918-08-26", certainty: 0.7, cites: [{source: S1, locator: "facts box"}], how_known: "NASA."}
    place: {value: "White Sulphur Springs, West Virginia", modern_name: "White Sulphur Springs, West Virginia, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "facts box; para. 1"}], how_known: "NASA."}
  death:
    date: {value: "2020-02-24", certainty: 0.7, cites: [{source: S1, locator: "final paragraph"}], how_known: "NASA."}
    place: {value: UNKNOWN, how_known: "Not stated in the sources read."}
  first_lasting_contribution_year: {value: 1960, certainty: 0.5, cites: [{source: S1, locator: "para. 4"}], how_known: "'In 1960, she and engineer Ted Skopinski coauthored' the report 'laying out the equations describing an orbital spaceflight in which the landing position of the spacecraft is specified' (S1); a NASA report (P30 #1). 0.5: no source calls it lasting; alternatives 1961 (Shepard trajectory) and 1962 (Glenn verification)."}
  era_bucket: {value: "1950 on", certainty: 1.0, cites: [{source: S1, locator: "para. 4–5"}], how_known: "1960–1962 (P2)."}
  region_of_birth: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "para. 1"}], how_known: "USA (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "para. 2"}], how_known: "Langley, Virginia."}
  sex_as_recorded: {value: "female", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "para. 4"}], how_known: "English reports."}
  occupations: {value: ["mathematician", "aerospace technologist"], certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S2, locator: "text"}], how_known: "NASA; PC(USA)."}

contribution:
  fields: {value: ["orbital mechanics", "spaceflight trajectory analysis"], certainty: 0.7, cites: [{source: S1, locator: "para. 3–5"}], how_known: "NASA."}
  lasting_original_contributions:
    - {value: "Equations for placing a satellite over a selected Earth position (report with Ted Skopinski)", year: 1960, kind: "method", lasting: "'equations describing an orbital spaceflight in which the landing position of the spacecraft is specified' (S1); no source calls them lasting; her 'pioneering legacy' (S1)", certainty: 0.5, cites: [{source: S1, locator: "para. 4"}], how_known: "NASA biography."}
    - {value: "Hand verification of John Glenn's orbital trajectory (Friendship 7)", year: 1962, kind: "other", lasting: "'the work that she would become most known for' (S1)", certainty: 0.5, cites: [{source: S1, locator: "para. 5"}, {source: S2, locator: "text"}], how_known: "NASA; PC(USA); fame rather than a stated lasting result."}
  evidence_of_impact:
    - {value: "Presidential Medal of Freedom (2015)", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "para. 6"}], how_known: "NASA."}
  major_works:
    - {value: "Trajectory analysis for Alan Shepard's Freedom 7", year: 1961, kind: "other", certainty: 0.7, cites: [{source: S1, locator: "para. 3"}], how_known: "NASA."}
  honours: []
  definition_fit: {value: "arguable", rationale: "Credited authorship and celebrated verification; no source names a lasting original result (S1, S2).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household: []
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling:
    - {value: "West Virginia State College (B.S. mathematics and French, 1937); first black graduate students at West Virginia University (1939)", certainty: 0.7, cites: [{source: S1, locator: "facts box; para. 1–2"}], how_known: "NASA."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1960–1962", certainty: 0.5, cites: [{source: S1, locator: "para. 4–5"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "No profession of her own read. Practice: member of Carver Memorial Presbyterian Church 'for more than 50 years', serving 'in several leadership roles including ... its finance chair' (S2); her former pastor Brian Blount called her Christian faith 'deep' (S3, search excerpt). Practice and a pastor's account without her words: lead CHRIST (Toni Morrison precedent, RQ-Y2)."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Lead: Presbyterian church office and practice (S2, S3)."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing first-hand read (P19)."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (RQ-AA5-1): trajectory computation applies known laws; no statement on nature read."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, so the P4 test cannot be applied (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "Her memoir My Remarkable Journey (2021, with Joylette Hylick and Katherine Moore) and Shetterly's Hidden Figures may hold her own words on faith."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated in the sources read."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1960–1962", certainty: 0.5, cites: [{source: S1, locator: "para. 4–5"}], how_known: "From the 1960 report to the 1962 Glenn verification, the listed lasting works (P29, P30 #1); 0.5 as both are lasting only at 0.5."}
  age_at_first_lasting_contribution: {value: 42, certainty: 0.5, cites: [{source: S1, locator: "facts box; para. 4"}], how_known: "1960 − 1918 = 42 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "Analytic geometry of orbits (S1).", certainty: 0.5, cites: [{source: S1, locator: "para. 4"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "NACA / NASA Langley Research Center", role: "mathematician (computer); aerospace technologist", years: "1953–1986", kind: "government or state body", certainty: 0.7, cites: [{source: S1, locator: "facts box"}], how_known: "NASA."}
collaborators:
  - {value: "Ted Skopinski", relation: "collaborator", note: "co-author of the 1960 report", certainty: 0.7, cites: [{source: S1, locator: "para. 4"}], how_known: "NASA."}
  - {value: "Dorothy Vaughan", relation: "mentor or employer", note: "head of West Area Computing", certainty: 0.7, cites: [{source: S1, locator: "para. 2"}], how_known: "NASA."}
  - {value: "W. W. Schieffelin Claytor", relation: "mentor or employer", note: "college mathematics mentor", certainty: 0.7, cites: [{source: S1, locator: "para. 1"}], how_known: "NASA."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 197"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Lasting status arguable."
    - "Worldview from practice only."
  open_questions:
    - "RQ-AA5-1 scientist status; RQ-AA5-2 practice without profession."

sources:
  - id: S1
    type: secondary
    kind: "institutional page"
    author: "Margot Lee Shetterly"
    citation: "Shetterly, Margot Lee. 'Katherine Johnson Biography.' NASA (22 November 2016). https://www.nasa.gov/centers-and-facilities/langley/katherine-johnson-biography/"
    url: "https://www.nasa.gov/centers-and-facilities/langley/katherine-johnson-biography/"
    accessed: 2026-10-19
    reliability_note: "Signed NASA biography by the author of Hidden Figures, read in full."
    used_for: [identity, basics, contribution, childhood, timing, institutions, collaborators]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "Presbyterian Church (U.S.A.)"
    citation: "'Real-life \"Hidden Figures\" mathematician Katherine G. Johnson is longtime Presbyterian.' PC(USA) News (26 January 2017). https://pcusa.org/news-storytelling/news/2017/1/26/real-life-hidden-figures-mathematician-katherine-g-johnson-longtime"
    url: "https://pcusa.org/news-storytelling/news/2017/1/26/real-life-hidden-figures-mathematician-katherine-g-johnson-longtime"
    accessed: 2026-10-19
    reliability_note: "Denominational news article, read in full."
    used_for: [identity, contribution, worldview]
  - id: S3
    type: secondary
    kind: "institutional page"
    author: "Brian K. Blount"
    citation: "Blount, Brian K. 'President Brian Blount statement on passing of Katherine Johnson.' Union Presbyterian Seminary (24 February 2020). https://www.upsem.edu/newsroom/president-brian-blount-statement-on-passing-of-katherine-johnson/"
    url: "https://www.upsem.edu/newsroom/president-brian-blount-statement-on-passing-of-katherine-johnson/"
    accessed: 2026-10-19
    reliability_note: "Her former pastor's statement, seen only as a search excerpt (the page text did not load)."
    used_for: [worldview]
  - id: S4
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

Katherine Johnson (1918–2020), NASA mathematician [S1]. Draft: BELOW_THRESHOLD (lead CHRIST). Not plotted.

## Life and work

White Sulphur Springs; Langley [S1].

## Contribution and impact

Orbital equations (1960); Glenn verification (1962) [S1].

## Childhood and education

West Virginia State; WVU [S1].

## Adult working worldview

Practice only [S2, S3].

## Heritage (context only)

Not stated.

## Timing

1960–1962, age 42 (0.5) [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- RQ-AA5-1; RQ-AA5-2.

## Research log

- 2026-10-19: Read NASA (Shetterly); PC(USA) 2017; Blount excerpt.
