---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z9)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z9, order P32: F 3, rank 173). Basics from Britannica (George Woodcock, signed). Own words: 'Notes on the Way' (Time and Tide, 1940; orwell.ru transcription of CEJL, unofficial web copy), before the span: religious belief 'had to be abandoned', 'in essence a lie'; hope for 'human brotherhood without the need for a \"next world\"'. Collective, not first-person, so primary_system BELOW_THRESHOLD (leads ATHE, SECHUM); A BELOW_THRESHOLD; B UNKNOWN (not a scientist); C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD. Span 1945–1949, age 42. Not plotted. Draft, not reviewed."}

identity:
  id: orwell-george
  display_name: "George Orwell"
  roster:
    canonical_name: "George Orwell"
    rank: 173
    F: 3
    models: [DeepSeek, GPT, Grok]
    band: "core (3–4)"
    status: "core"
    field: "literature"
    field_bucket: "literature"
  full_name: {value: "Eric Arthur Blair", certainty: 0.7, cites: [{source: S1, locator: "Pseudonym of"}], how_known: "Britannica."}
  native_name: {value: "George Orwell", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica (pen name)."}
  aliases:
    - {name: "Eric Arthur Blair", kind: "birth name"}
    - {name: "George-Orwell", kind: "roster alias"}

basics:
  birth:
    date: {value: "1903-06-25", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Motihari, Bengal", modern_name: "Motihari, Bihar, India", polity_then: "British India", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "1950-01-21", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "London", modern_name: "London, United Kingdom", polity_then: "United Kingdom", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1945, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Animal Farm (1945), one of his 'profoundly influential novels'."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "1945 (P2)."}
  region_of_birth: {value: "South Asia", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "India (P3; regions.csv)."}
  region_of_work: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "England."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "English."}
  occupations: {value: ["novelist", "essayist", "critic", "journalist"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

contribution:
  fields: {value: ["literature", "political writing"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Animal Farm", year: 1945, kind: "work", lasting: "'profoundly influential novels' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    - {value: "Nineteen Eighty-four", year: 1949, kind: "work", lasting: "'profoundly influential novels'; 'solidified his reputation as an almost prophetic voice' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  evidence_of_impact:
    - {value: "An almost prophetic voice in 20th-century literature", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works:
    - {value: "Homage to Catalonia", year: 1938, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Profoundly influential novelist (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Father, minor official in the Indian Civil Service", role: "father", certainty: 0.7, cites: [{source: S1, locator: "Early life"}], how_known: "Britannica."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling:
    - {value: "Eton College", stage: "grammar or secondary school", years: "1917–1921", certainty: 0.7, cites: [{source: S1, locator: "Early life"}], how_known: "Britannica."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1945–1949", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "'Notes on the Way' (1940, before the span; unofficial web copy): religious belief 'had to be abandoned', 'in essence a lie'; brotherhood 'without the need for a \"next world\"'. A collective, historical claim, not a first-person statement of his own belief, so BELOW_THRESHOLD. Leads ATHE and SECHUM."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: ATHE, reason: "Lead."}
    - {code: SECHUM, reason: "Lead: human brotherhood without a next world."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "No first-person locus view read; the 1940 essay speaks of society (P20)."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30); no statement on nature's order."}
    C_ledger: {value: UNKNOWN, how_known: "'men know that they are mortal' and brotherhood without a 'next world' (S2) point to C 4, but collective and from a web copy; not scored."}
    D_authority: {value: UNKNOWN, how_known: "Not scored."}
    E_scope: {value: UNKNOWN, how_known: "Not scored."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD, so the P4 test cannot be applied."}
  statements:
    - text: "It was absolutely necessary that the soul should be cut away. Religious belief, in the form in which we had known it, had to be abandoned. By the nineteenth century it was already in essence a lie, a semi-conscious device for keeping the rich rich and the poor poor."
      cites: [{source: S2, locator: "para. 1"}]
      date: "1940-03-30"
      context: "'Notes on the Way', Time and Tide; before the span."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-19
      note: "orwell.ru transcription of the CEJL text; not checked against a printing."
  changes_over_life: []
  coder_notes: "As I Please (1944) on personal immortality and Such, Such Were the Joys on his loss of faith; check the CEJL printing to lift the web-copy cap."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated in the sources read."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1945–1949", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Animal Farm (1945) to Nineteen Eighty-four (1949) (P29, P30)."}
  age_at_first_lasting_contribution: {value: 42, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "1945 − 1903 = 42 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: "1940 ('Notes on the Way')", certainty: 0.5, cites: [{source: S2, locator: "para. 1"}], how_known: "Published essay."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Fiction and essays (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "British Broadcasting Corporation (Indian service)", role: "head", years: "1941–1943", kind: "other", certainty: 0.5, cites: [{source: S1, locator: "From The Road to Wigan Pier to World War II"}], how_known: "Britannica; start year approximate."}
collaborators:
  - {value: "Eileen O'Shaughnessy", relation: "family", note: "wife; typist and copy editor", certainty: 0.7, cites: [{source: S1, locator: "Against imperialism"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 173"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Only a collective statement read, from an unofficial web copy."
  open_questions:
    - "CEJL printing; As I Please 1944."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "George Woodcock"
    citation: "Woodcock, George. 'George Orwell.' Encyclopaedia Britannica (rev. 2026). https://www.britannica.com/biography/George-Orwell"
    url: "https://www.britannica.com/biography/George-Orwell"
    accessed: 2026-10-19
    reliability_note: "Signed article; body cited, question boxes not used (P26)."
    used_for: [identity, basics, contribution, childhood, worldview, timing, lane_b, institutions, collaborators]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "George Orwell"
    citation: "Orwell, George. 'Notes on the Way.' Time and Tide (30 March and 6 April 1940); CEJL (1968). Transcription at orwell.ru. https://orwell.ru/library/articles/notes/english/e_notew"
    url: "https://orwell.ru/library/articles/notes/english/e_notew"
    accessed: 2026-10-19
    reliability_note: "Unofficial web copy of a published essay (capped at 0.7, CODING_GUIDE §7)."
    used_for: [worldview, timing]
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

George Orwell (1903–1950), novelist and essayist [S1]. Draft: BELOW_THRESHOLD (leads ATHE, SECHUM). Not plotted.

## Life and work

Burma, Paris, London, Spain, Jura [S1].

## Contribution and impact

Animal Farm; Nineteen Eighty-four [S1].

## Childhood and education

Eton [S1].

## Adult working worldview

Religious belief 'had to be abandoned' (1940) [S2].

## Heritage (context only)

Not stated.

## Timing

1945–1949, age 42 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- CEJL printing.

## Research log

- 2026-10-19: Read Britannica (Woodcock); 'Notes on the Way'.
