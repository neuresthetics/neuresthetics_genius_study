---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch F)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-15
  change_log:
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch F, order P32: F 5, rank 33). Basics from Britannica and Yale News. No statement of hers on religion or on the order of nature was found. Not a scientist under P30/P33 (her lasting contributions are a manual and compilers, not theories about natural systems). All worldview fields UNKNOWN; mid_basin UNKNOWN. Draft, not reviewed."}

identity:
  id: hopper-grace
  display_name: "Grace Hopper"
  roster:
    canonical_name: "Grace Hopper"
    rank: 33
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: computer science
    field_bucket: "computer science / AI"
  full_name: {value: "Grace Brewster Murray Hopper", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts ('Née: Grace Brewster Murray'; 'Also known as')"}], how_known: "Britannica alone."}
  native_name: {value: UNKNOWN, how_known: "English."}
  aliases:
    - {name: "Grace-Hopper", kind: "roster alias"}
    - {name: "Hopper-Grace", kind: "roster alias"}

basics:
  birth:
    date: {value: "1906-12-09", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "title (year only)"}], how_known: "Day from Britannica alone; Yale News gives the years 1906–1992."}
    place: {value: "New York, New York, U.S.", modern_name: "New York City, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica alone."}
  death:
    date: {value: "1992-01-01", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "title (year only)"}], how_known: "Day from Britannica alone."}
    place: {value: "Arlington, Virginia, U.S.", modern_name: "Arlington, Virginia, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica alone."}
  first_lasting_contribution_year: {value: 1946, certainty: 0.7, cites: [{source: S1, locator: "second paragraph (A Manual of Operation for the Automatic Sequence Controlled Calculator, 1946)"}], how_known: "Earliest listed lasting contribution (P13); Britannica alone."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S1, locator: "1946"}], how_known: "From 1946 (P2)."}
  region_of_birth: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "United States (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "United States."}
  sex_as_recorded: {value: "female", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [English], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica (US career)."}
  occupations: {value: ["mathematician", "naval officer", "computer programmer"], certainty: 0.7, cites: [{source: S1, locator: "opening; third paragraph"}], how_known: "Britannica."}

contribution:
  fields: {value: ["computer programming", "programming languages"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "A Manual of Operation for the Automatic Sequence Controlled Calculator (Harvard Mark I)", year: 1946, kind: work, lasting: "'the first extensive treatment of how to program a computer' (S1)", certainty: 0.7, cites: [{source: S1, locator: "second paragraph"}], how_known: "Britannica alone."}
    - {value: "One of the first compilers; coined the word 'compiler'", year: 1949, kind: invention, lasting: "compilers translate programmer instructions into machine code (S1)", certainty: 0.5, cites: [{source: S1, locator: "third paragraph"}], how_known: "Britannica says she joined Eckert-Mauchly in 1949 'where she designed' it; the start year of the design is not given, so 1949 is the earliest it could be and may be later (§8 undated starts). It does not move the first-lasting year, which is 1946."}
    - {value: "Flow-Matic, the first English-language data-processing compiler (her division)", year: 1957, kind: invention, lasting: "'inspired the development of COBOL' (S1)", certainty: 0.7, cites: [{source: S1, locator: "third paragraph"}], how_known: "Britannica alone."}
  evidence_of_impact:
    - {value: "National Medal of Technology, 1991; USS Hopper commissioned 1996; more than 40 honorary degrees", kind: "other", certainty: 0.7, cites: [{source: S2, locator: "paragraph on honours"}], how_known: "Yale News."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Compilers and English-like languages underlie later programming (S1).", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading. Beyer (2009), per a review, argues her role has been mythologised (not read)."}

childhood:
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
  parents_and_household: []
  household_circumstances: {value: TODO}
  schooling:
    - {value: "Vassar College, B.A.", stage: university, run_by: private, years: "–1928", ages: "–22", certainty: 0.7, cites: [{source: S1, locator: "second paragraph"}], how_known: "Britannica."}
    - {value: "Yale University, M.A. 1930, Ph.D. 1934 (mathematics)", stage: university, run_by: private, years: "1928–1934", ages: "22–28", certainty: 0.7, cites: [{source: S1, locator: "second paragraph"}], how_known: "Britannica; the start year is the coder's inference from the B.A."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: TODO}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1946–1957", certainty: 0.7, cites: [{source: S1, locator: "dates"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Britannica and Yale News read; web search found no statement of hers on religion. Beyer (2009) and the 1968 Smithsonian oral history not read."}
  primary_system: {value: UNKNOWN, how_known: "No statement of her own found."}
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "No evidence in the sources read; not coded."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing read."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist under P30/P33: her lasting contributions are a manual and compilers (devices and software), not theories about natural systems; no statement on nature found (P16)."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read."}
    D_authority: {value: UNKNOWN, how_known: "Nothing read."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7)."}
  mid_basin: {value: UNKNOWN, how_known: "A and B are UNKNOWN (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "Coder's call: compilers count as inventions under P33, so she is not a scientist and B needs a statement."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: TODO}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1946–1957", certainty: 0.7, cites: [{source: S1, locator: "dates"}], how_known: "1946 to 1957, first to last listed lasting contribution (P29, P30). Her COBOL advocacy in the 1960s is described as promotion, not an original contribution, so it is not listed."}
  age_at_first_lasting_contribution: {value: 40, certainty: 0.7, cites: [{source: S1, locator: "opening; 1946"}], how_known: "1946 − 1906 = 40 (P30)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No statement read."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Nothing read."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Nothing read."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "Doctorate in mathematics (Yale 1934) gives documented exposure to proof.", certainty: 0.5, cites: [{source: S1, locator: "second paragraph"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "second paragraph"}], how_known: "Childhood mathematics not read."}
  circle_present: {value: "unclear", rationale: "Nothing read.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No reading possible."
  notes: ""

institutions:
  - {value: "Vassar College", role: "mathematics teacher", years: "to 1943", kind: university, certainty: 0.7, cites: [{source: S1, locator: "second paragraph"}], how_known: "Britannica."}
  - {value: "Harvard University, Bureau of Ordnance Computation Project", role: "naval officer, then civilian research fellow", years: "1944–1949", kind: university, certainty: 0.7, cites: [{source: S1, locator: "second paragraph"}], how_known: "Britannica; end year is when she joined Eckert-Mauchly."}
  - {value: "Eckert-Mauchly Computer Corp. (later Remington Rand, Sperry Rand)", role: "head programmer", years: "1949–", kind: commercial, certainty: 0.7, cites: [{source: S1, locator: "third paragraph"}], how_known: "Britannica."}
collaborators: []

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 33"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "The popular claim that she was the first woman with a Yale mathematics doctorate is disputed: a Technology and Culture review of Beyer (2009) says she was the eleventh. Not used in this record."
  open_questions:
    - "Read Beyer (2009) and the 1968 Smithsonian oral history for any statement on religion."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "Britannica Editors. \"Grace Hopper.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Grace-Hopper."
    url: "https://www.britannica.com/biography/Grace-Hopper"
    accessed: 2026-10-15
    reliability_note: "Article body only; the AI 'Top Questions' box is not used."
    used_for: [identity, basics, contribution, childhood, worldview, timing, lane_b, institutions]
  - id: S2
    type: tertiary
    kind: institutional page
    author: "Yale News"
    citation: "\"Grace Murray Hopper (1906-1992): A legacy of innovation and service.\" Yale News, 10 February 2017."
    url: "https://news.yale.edu/2017/02/10/grace-murray-hopper-1906-1992-legacy-innovation-and-service"
    accessed: 2026-10-15
    reliability_note: "University news page; read through a search-index excerpt."
    used_for: [basics, contribution]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Grace Hopper

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Grace Hopper (1906–1992), American mathematician and naval officer, wrote the Mark I manual and designed early compilers [S1, S2]. No statement of hers on religion was found. Draft: all worldview fields UNKNOWN; mid_basin UNKNOWN.

## Life and work

Vassar and Yale; Naval Reserve from 1943; Harvard Mark I; Eckert-Mauchly and UNIVAC I; rear admiral [S1].

## Contribution and impact

Mark I manual (1946), early compiler, Flow-Matic (1957) [S1]; National Medal of Technology [S2].

## Childhood and education

Vassar B.A. 1928; Yale Ph.D. 1934 [S1].

## Adult working worldview

Unknown [S1].

## Heritage (context only)

Not researched [S1].

## Timing

First lasting contribution 1946, at 40 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Mathematics doctorate; otherwise unclear [S1].

## Open questions

- Beyer (2009); Smithsonian oral history (1968).

## Research log

- 2026-10-15: Read Britannica and Yale News; web search for her religious views found nothing.
