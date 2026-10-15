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
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch L, order P32: F 5, rank 76). Basics from Britannica (Robert E. Conot), signed body through the Newark years; Top Questions not cited. Worldview from Edward Marshall's interview, 'No Immortality of the Soul', New York Times, 2 October 1910 (transcript on sundaymagazine.org; NYT archive abstract; Edison Papers bibliography). primary_system BELOW_THRESHOLD; A BELOW_THRESHOLD; B 4 (0.5, alt 3; interview, partly the interviewer's paraphrase); mid_basin BELOW_THRESHOLD. Not plotted. Draft, not reviewed."}

identity:
  id: edison-thomas
  display_name: "Thomas Edison"
  roster:
    canonical_name: "Thomas Edison"
    rank: 76
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: invention
    field_bucket: "invention / engineering"
  full_name: {value: "Thomas Alva Edison", certainty: 0.7, cites: [{source: S1, locator: "header ('In full')"}], how_known: "Britannica."}
  native_name: {value: UNKNOWN, how_known: "English."}
  aliases:
    - {name: "Wizard of Menlo Park", kind: other}

basics:
  birth:
    date: {value: "1847-02-11", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Milan, Ohio, U.S.", modern_name: "Milan, Ohio, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "1931-10-18", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "West Orange, New Jersey, U.S.", modern_name: "West Orange, New Jersey, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1874, certainty: 0.5, cites: [{source: S1, locator: "Newark paragraph"}], how_known: "Quadruplex telegraph, sold to Gould in December 1874; the only lasting invention the signed body read dates (phonograph and lamp dates are in the Top Questions box or the undated summary). 0.5."}
  era_bucket: {value: "1750 to 1849", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "Birth year bucket (P2)."}
  region_of_birth: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "United States (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "New Jersey."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [English], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
  occupations: {value: ["inventor", "entrepreneur"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
contribution:
  fields: {value: ["electrical engineering", "telegraphy", "sound recording"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Quadruplex telegraph (four messages on one wire)", year: 1874, kind: invention, lasting: "'one of the larger payments for any invention up to that time' (S1)", certainty: 0.5, cites: [{source: S1, locator: "Newark paragraph"}], how_known: "Britannica; dated by the December 1874 sale (0.5)."}
    - {value: "Phonograph, incandescent lamp, first commercial electric light and power system; the first industrial research laboratory", kind: "body of work", lasting: "'a critical role in introducing the modern age of electricity' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Undated in the body read."}
  evidence_of_impact:
    - {value: "1,093 patents, a world record", kind: "other", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father Samuel Edison, Jr., lighthouse keeper and carpenter at Fort Gratiot from 1854; mother Nancy Elliot Edison", role: parents, certainty: 0.7, cites: [{source: S1, locator: "family paragraph; 'Early years'"}], how_known: "Britannica."}
  household_circumstances: {value: "Seventh and last child, fourth surviving; early hearing problems", certainty: 0.7, cites: [{source: S1, locator: "family paragraph"}], how_known: "Britannica."}
  schooling:
    - {value: "School at Port Huron, attended sporadically for five years; left 1859", stage: "elementary school", run_by: other, certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
    - {value: "Avid and omnivorous reading", stage: "self-directed", run_by: other, certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
    - {value: "Apprentice telegrapher (1863)", stage: apprenticeship, run_by: other, certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [English], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1874", certainty: 0.5, cites: [{source: S1, locator: "Newark paragraph"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system:
    value: BELOW_THRESHOLD
    basis: recorded_interview
    certainty: 0.5
    cites: [{source: S2, locator: "transcript"}, {source: S3, locator: "'Communicating with the Dead'"}]
    rationale: "Denies personal immortality and, by the interviewer's account, anything 'supernatural'; says nothing read about God. Candidates DETERM, ATHE, AGNOS. The Edison Papers report that he also held that units of consciousness exist before and after death (S3), which cuts against a plain materialist code."
    how_known: "(interview) One 1910 newspaper interview; nothing on God."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: DETERM, reason: "'all there is ... be explained along material lines' (interviewer's paraphrase)."}
    - {code: ATHE, reason: "Denies immortality of the soul; no God statement."}
    - {code: AGNOS, reason: "'I don't know' on what becomes of the will."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "(interview) No statement placing or denying God in what was read; the denial of immortality does not place God (P20)."}
    B_cause:
      value: 4
      basis: recorded_interview
      certainty: 0.5
      cites: [{source: S2, locator: "transcript (opening)"}, {source: S4, locator: "p. 15 (abstract)"}]
      how_known: "(interview) The no-exception claim is the interviewer's paraphrase (reported speech); his own words add 'nature's methods are not loose' (NYT p. 15, OCR abstract); 0.5, alternative named."
      rationale: "He had come to the conclusion 'that there is no \"supernatural\" ... that all there is ... can or will, soon or late, be explained along material lines' (Marshall's paraphrase): a stated order with no exception (P40). Named alternative: 3 (P41), since the strict wording is the interviewer's, not his."
    C_ledger: {value: UNKNOWN, how_known: "(interview) He denies reward in heaven ('Shall I, if I am good and earn reward, go to heaven when I die? No -- no'), which bears on C; not scored at this reading (coder's call)."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read (P7)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A is BELOW_THRESHOLD."}
  statements:
    - text: "I cannot believe in the immortality of the soul."
      cites: [{source: S2, locator: "transcript"}]
      date: "1910-10-02"
      context: "Edward Marshall interview, New York Times, 2 October 1910, pp. 1, 15 (S3 bibliography)."
      axes: [C_ledger]
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
    - text: "Searching the inner structure of all things for the fundamental, Edison told me he had come to the conclusion that there is no \"supernatural,\" or \"supernormal,\" as the psychic researchers put it -- that all there is, that all there has been, all there ever will be, can or will, soon or late, be explained along material lines"
      cites: [{source: S2, locator: "transcript (opening)"}]
      date: "1910-10-02"
      context: "Marshall's paraphrase in the same interview."
      axes: [B_cause]
      kind: "reported speech"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
  changes_over_life: []
  coder_notes: "Coder's call. The 1910 interview falls well after the dated working year (1874); the Forum interview 'Has Man an Immortal Soul?' (1926) and the 'units of consciousness' idea (S3) are the leads."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "American", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1874", certainty: 0.5, cites: [{source: S1, locator: "Newark paragraph"}], how_known: "Only one dated listed contribution in the body read (P29, P30); TODO: date the phonograph and lamp from the signed body."}
  age_at_first_lasting_contribution: {value: 27, certainty: 0.5, cites: [{source: S1, locator: "opening; Newark paragraph"}], how_known: "1874 − 1847 = 27 (P30)."}
  first_evidence_of_lio_type_views: {value: "1910, age 63: no 'supernatural'; all 'explained along material lines' (interviewer's paraphrase)", year: 1910, age: 63, certainty: 0.5, cites: [{source: S2, locator: "transcript"}], how_known: "(interview) Earlier interviews (e.g. with Lathrop, S3) not read: 'earlier works not read' (P30 #7)."}
  lio_views_relative_to_major_work: {value: "after major work", certainty: 0.5, cites: [{source: S2, locator: "transcript"}], how_known: "1910, after the dated 1874; the period is incompletely dated."}
  worldview_during_major_work: {value: BELOW_THRESHOLD, how_known: "As primary_system."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Not read.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Not read."}
  circle_present: {value: "unclear", rationale: "No God statement read.", certainty: 0.5, cites: [{source: S2, locator: "transcript"}], how_known: "Coder's reading."}
  reading: "Materialist on the soul; God not addressed."
  notes: ""

institutions:
  - {value: "Western Union Telegraph Company", role: inventor, kind: "patron or funder", certainty: 0.7, cites: [{source: S1, locator: "Newark paragraph"}], how_known: "Britannica."}
collaborators:
  - {value: "Frank L. Pope", relation: collaborator, certainty: 0.7, cites: [{source: S1, locator: "New York paragraph"}], how_known: "Partnership."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S5, locator: "roster.csv, rank 76"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags: []
  open_questions:
    - "Read the 1910 NYT pages (facsimile) and the 1926 Forum interview; date the phonograph and lamp."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Robert E. Conot"
    citation: "Conot, Robert E. \"Thomas Edison.\" Encyclopaedia Britannica, updated 14 October 2026. https://www.britannica.com/biography/Thomas-Edison."
    url: "https://www.britannica.com/biography/Thomas-Edison"
    accessed: 2026-10-15
    reliability_note: "Signed body (Conot, with Britannica Editors) through the Newark years; Top Questions not cited."
    used_for: [identity, basics, contribution, childhood, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: secondary
    kind: other
    author: "The Sunday Magazine (sundaymagazine.org)"
    citation: "\"'No Immortality Of The Soul' Says Thomas A. Edison.\" Excerpt of Edward Marshall's New York Times interview of 2 October 1910. https://www.sundaymagazine.org/p/no-immortality-of-the-soul-says-thomas-a-edison."
    url: "https://www.sundaymagazine.org/p/no-immortality-of-the-soul-says-thomas-a-edison"
    accessed: 2026-10-15
    reliability_note: "Web transcription with ellipses; secondary quotation."
    used_for: [worldview, timing, lane_b]
  - id: S3
    type: secondary
    kind: "institutional page"
    author: "Thomas A. Edison Papers, Rutgers University"
    citation: "Thomas A. Edison Papers. \"Edison's Published Articles and Select Interviews\" and \"Communicating with the Dead\" (digital exhibit). https://edison.rutgers.edu/edison-s-published-articles-and-select-interviews."
    url: "https://edison.rutgers.edu/edison-s-published-articles-and-select-interviews"
    accessed: 2026-10-15
    reliability_note: "Scholarly editing project; seen through search result text (bibliography lists the 1910 NYT interview, misprinting the year as 1890)."
    used_for: [worldview]
  - id: S4
    type: secondary
    kind: other
    author: "The New York Times"
    citation: "Marshall, Edward. \"'No Immortality of the Soul' Says Thomas A. Edison.\" New York Times, 2 October 1910, pp. 1, 15. https://www.nytimes.com/1910/10/02/archives/-no-immortality-of-the-soul-says-thomas-a-edison-in-fact-he-doesnt-.html."
    url: "https://www.nytimes.com/1910/10/02/archives/-no-immortality-of-the-soul-says-thomas-a-edison-in-fact-he-doesnt-.html"
    accessed: 2026-10-15
    reliability_note: "Archive page OCR excerpt seen through search result text only."
    used_for: [worldview]
  - id: S5
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Thomas Edison

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Thomas Edison (1847–1931), American inventor [S1]. Draft: primary_system BELOW_THRESHOLD; A BELOW_THRESHOLD; B 4 at 0.5 (alt 3); mid_basin BELOW_THRESHOLD. Not plotted.

## Life and work

Port Huron; telegrapher; Newark; Menlo Park [S1].

## Contribution and impact

Quadruplex (1874); phonograph; incandescent lamp; 1,093 patents [S1].

## Childhood and education

Sporadic schooling; self-taught reader [S1].

## Adult working worldview

1910: 'I cannot believe in the immortality of the soul' [S2].

## Heritage (context only)

See front matter [S1].

## Timing

First dated lasting contribution 1874, at 27 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Unclear [S2].

## Open questions

- 1910 facsimile; 1926 Forum interview.

## Research log

- 2026-10-15: Read Britannica (Conot) through Newark; the 1910 interview transcript (sundaymagazine.org).
