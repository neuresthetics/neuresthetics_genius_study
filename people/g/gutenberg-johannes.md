---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA3)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "AA3 audit fix (v8's call on the auditor's advice): alternative birth about 1400, age about 55. Signed Britannica article (Lehmann-Haupt) added as S3; only part of it was read and it did not confirm the Bible date in the body, so the span stays 0.5."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA3, order P32: F 3, rank 189). Source: Britannica (students edition, read in full). Lasting work: printing with movable metal type, 'one of the world's greatest inventions' whose method 'endured almost unchanged for five centuries'; dated by the Gutenberg Bible, 'completed before or in 1455' (publication, P30 #1), at 0.5 with 1454 (the Türkenkalender, 'printed in 1454') as the alternative. Birth '1395?' and death 'probably ... February 3, 1468', so age about 60 at 0.5; alternative birth about 1400, age about 55 (AA3 audit advice). The signed Britannica article (Lehmann-Haupt, S3) gives 'born 14th century, Mainz' and the Fust judgment of 6 November 1455. An invention, not a theory (P33): not a scientist, B UNKNOWN. No own words: worldview all UNKNOWN (lead CHRIST: printed the Bible; pension from the archbishop of Mainz). Not plotted. Draft, not reviewed."}

identity:
  id: gutenberg-johannes
  display_name: "Johannes Gutenberg"
  roster:
    canonical_name: "Johannes Gutenberg"
    rank: 189
    F: 3
    models: [Gemini, GPT, Grok]
    band: "core (3–4)"
    status: "core"
    field: "invention"
    field_bucket: "invention / engineering"
  full_name: {value: "Johannes Gensfleisch zur Laden zum Gutenberg", certainty: 0.7, cites: [{source: S1, locator: "para. 3"}], how_known: "Britannica."}
  native_name: {value: "Johannes Gutenberg", certainty: 0.7, cites: [{source: S1, locator: "heading"}], how_known: "Britannica."}
  aliases:
    - {name: "Gutenberg-Johannes", kind: "roster alias"}
    - {name: "Johannes-Gutenberg", kind: "roster alias"}
    - {name: "Johann Gutenberg", kind: "other"}

basics:
  birth:
    date: {value: "1395", certainty: 0.5, cites: [{source: S1, locator: "heading"}, {source: S3, locator: "Introduction"}], how_known: "Britannica students: '1395?'; 'born ... in the late 14th century' (S1); signed article: 'born 14th century' (S3). Alternative: about 1400 (v8's call on the auditor's advice, AA3), within the late-14th-century range."}
    place: {value: "Mainz", modern_name: "Mainz, Germany", polity_then: "Electorate of Mainz (Holy Roman Empire)", certainty: 0.7, cites: [{source: S1, locator: "para. 3"}], how_known: "Britannica."}
  death:
    date: {value: "1468-02-03", certainty: 0.5, cites: [{source: S1, locator: "para. 5"}], how_known: "Britannica: 'probably died in Mainz on February 3, 1468'."}
    place: {value: "Mainz", modern_name: "Mainz, Germany", polity_then: "Electorate of Mainz (Holy Roman Empire)", certainty: 0.5, cites: [{source: S1, locator: "para. 5"}], how_known: "Britannica: 'probably'."}
  first_lasting_contribution_year: {value: 1455, certainty: 0.5, cites: [{source: S1, locator: "para. 5"}], how_known: "The Bible 'was completed before or in 1455' (S1); publication (P30 #1). Alternative 1454: the Türkenkalender, set by him, 'printed in 1454' (S1)."}
  era_bucket: {value: "1400 to 1599", certainty: 0.7, cites: [{source: S1, locator: "para. 4–5"}], how_known: "1454–1455 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "para. 3"}], how_known: "Germany (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "para. 3–5"}], how_known: "Strassburg; Mainz."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Latin", "German"], certainty: 0.5, cites: [{source: S1, locator: "para. 5"}], how_known: "Latin Bible; German calendar (coder's reading)."}
  occupations: {value: ["metalworker", "printer"], certainty: 0.7, cites: [{source: S1, locator: "para. 1, 3"}], how_known: "Britannica."}

contribution:
  fields: {value: ["printing"], certainty: 0.7, cites: [{source: S1, locator: "para. 1"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Printing with movable metal type (the Gutenberg press; the 42-line Bible)", year: 1455, kind: "invention", lasting: "'his method of using movable metal type endured almost unchanged for five centuries'; 'one of the world's greatest inventions' (S1)", certainty: 0.5, cites: [{source: S1, locator: "para. 1–2, 5"}], how_known: "Britannica; dated by the Bible's completion, 'before or in 1455' (0.5)."}
  evidence_of_impact:
    - {value: "Led to a great increase in literacy and the spread of knowledge", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "para. 2"}], how_known: "Britannica."}
  major_works:
    - {value: "Türkenkalender", year: 1454, kind: "other", certainty: 0.7, cites: [{source: S1, locator: "para. 5"}], how_known: "Britannica: printed 1454."}
  honours:
    - {value: "Pension from the archbishop of Mainz", year: 1465, kind: "other", certainty: 0.7, cites: [{source: S1, locator: "para. 6"}], how_known: "Britannica."}
  definition_fit: {value: "clearly meets", rationale: "One of the world's greatest inventions (S1).", certainty: 0.7, cites: [{source: S1, locator: "para. 2"}], how_known: "Britannica."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Father of the upper classes, with a managerial post at the Mainz mint", role: "father", certainty: 0.7, cites: [{source: S1, locator: "para. 3"}], how_known: "Britannica."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
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
  working_years: {value: "1455", certainty: 0.5, cites: [{source: S1, locator: "para. 5"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: {value: UNKNOWN, how_known: "No own words survive in the source read. Lead CHRIST: printed the Bible and a Psalter's groundwork; pension from the archbishop (S1). Printing a Bible is a commercial and craft fact, not a profession."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Lead: the Bible; archbishop's pension (S1)."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing first-hand read (P19)."}
    B_cause: {value: UNKNOWN, how_known: "An invention, not a theory (P33); no statement on nature read."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, so the P4 test cannot be applied (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "Few personal documents survive (lawsuit records); look for a scholar's account of his religious life (e.g. Kapr, Johann Gutenberg: The Man and His Invention, 1996)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated in the source read."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1455", certainty: 0.5, cites: [{source: S1, locator: "para. 5"}], how_known: "The one listed lasting work, dated by the Bible's completion (P29, P30 #1); alternative 1454."}
  age_at_first_lasting_contribution: {value: 60, certainty: 0.5, cites: [{source: S1, locator: "heading; para. 5"}], how_known: "1455 − 1395 = 60 (P30 year difference); birth year uncertain ('1395?'); alternative about 55 on a birth about 1400."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Craft invention (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions: []
collaborators:
  - {value: "Johann Fust", relation: "mentor or employer", note: "financier and partner from 1450; won a lawsuit against him", certainty: 0.7, cites: [{source: S1, locator: "para. 5"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 189"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Birth year uncertain."
  open_questions:
    - "Scholarly account of his religious life."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Britannica Editors"
    citation: "'Johannes Gutenberg.' Britannica (students edition). https://kids.britannica.com/students/article/Johannes-Gutenberg/274706"
    url: "https://kids.britannica.com/students/article/Johannes-Gutenberg/274706"
    accessed: 2026-10-19
    reliability_note: "Encyclopedia article, read in full; unsigned."
    used_for: [identity, basics, contribution, childhood, worldview, timing, collaborators]
  - id: S2
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [review]
  - id: S3
    type: tertiary
    kind: "encyclopedia"
    author: "Hellmut E. Lehmann-Haupt"
    citation: "Lehmann-Haupt, Hellmut E. 'Johannes Gutenberg.' Encyclopaedia Britannica. https://www.britannica.com/biography/Johannes-Gutenberg"
    url: "https://www.britannica.com/biography/Johannes-Gutenberg"
    accessed: 2026-10-19
    reliability_note: "Signed article; the fetched copy covers the introduction, Life and the start of the Invention section (to the 1455 Fust judgment); the Bible's completion date was not in the part read, so the span stays 0.5."
    used_for: [identity, basics]
---

## Summary

Johannes Gutenberg (1395?–1468), printer [S1]. Draft: all UNKNOWN; invention (P33). Not plotted.

## Life and work

Mainz; Strassburg [S1].

## Contribution and impact

Movable metal type; the Bible, 1455 [S1].

## Childhood and education

Not stated.

## Adult working worldview

None read.

## Heritage (context only)

Not stated.

## Timing

1455, age about 60, or about 55 (0.5) [S1, S3].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Religious life.

## Research log

- 2026-10-19: AA3 audit fix (v8's call on the auditor's advice): alternative birth about 1400, age about 55. Signed Britannica article (Lehmann-Haupt) added as S3; only part of it was read and it did not confirm the Bible date in the body, so the span stays 0.5.
- 2026-10-19: Read Britannica (students); signed Britannica (Lehmann-Haupt), partly.
