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
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch J, order P32: F 5, rank 63). Basics from Britannica (Britannica Editors, unsigned). Scientist under P30 (algebra, astronomy). The quatrains are not scored: Britannica says some scholars doubt he wrote poetry and that the verses appeared under his name only two centuries after his death (P42). primary_system UNKNOWN; A UNKNOWN; B 3 at 0.5 (alt 4) from working science only (P35); C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD. Not plotted. Draft, not reviewed."}

identity:
  id: khayyam-omar
  display_name: "Omar Khayyam"
  roster:
    canonical_name: "Omar Khayyam"
    rank: 63
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: mathematics
    field_bucket: mathematics
  full_name: {value: "Ghiyāth ad-Din Abū al-Fatḥ ʿUmar ibn Ibrahīm al-Khaiyāmī an-Nīshaburi", certainty: 0.7, cites: [{source: S1, locator: "header ('Also known as')"}], how_known: "Britannica."}
  native_name: {value: UNKNOWN, how_known: "Persian script not in the source read."}
  aliases:
    - {name: "Omar Khayyám", kind: transliteration}

basics:
  birth:
    date: {value: "1048-05-18", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica; Julian-era date."}
    place: {value: "Neyshābūr, Khorāsān", modern_name: "Nishapur, Iran", polity_then: "Khorasan", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "1131-12-04", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Neyshābūr", modern_name: "Nishapur, Iran", polity_then: "Khorasan", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1075, certainty: 0.5, cites: [{source: S1, locator: "calendar paragraph"}], how_known: "Jalālī calendar, adopted in 1075 (P13); the algebra treatise, on which his reputation 'principally rests', is undated and may be earlier, so 0.5."}
  era_bucket: {value: "500 to 1399", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "Whole life in the bucket (P2)."}
  region_of_birth: {value: "Middle East and North Africa", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Iran is Middle East and North Africa in regions.csv (P3)."}
  region_of_work: {value: "Middle East and North Africa", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Neyshābūr and Eṣfahān (Iran); also Samarkand (Central Asia); 0.5."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [Arabic], certainty: 0.5, cites: [{source: S1, locator: "algebra treatise title"}], how_known: "Arabic treatise title; Persian quatrains are of disputed authorship (0.5)."}
  occupations: {value: ["mathematician", "astronomer"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
contribution:
  fields: {value: ["algebra", "geometry", "astronomy"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Treatise on Demonstration of Problems of Algebra (cubic equations by intersecting conics)", kind: work, lasting: "his mathematical reputation 'principally rests' on it (S1)", certainty: 0.7, cites: [{source: S1, locator: "Samarkand paragraph"}], how_known: "Undated (P39)."}
    - {value: "Jalālī calendar", year: 1075, kind: discovery, lasting: "'more accurate than the present Gregorian calendar' (S1)", certainty: 0.7, cites: [{source: S1, locator: "calendar paragraph"}], how_known: "Adopted 1075."}
  evidence_of_impact:
    - {value: "Critique of Euclid's parallels influenced John Wallis", kind: "assessment by a later major figure", certainty: 0.7, cites: [{source: S1, locator: "Eṣfahān paragraph"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father possibly a tentmaker (source of the name Khayyam)", role: father, certainty: 0.5, cites: [{source: S1, locator: "name paragraph"}], how_known: "Britannica: 'may have been derived'."}
  household_circumstances: {value: TODO}
  schooling:
    - {value: "Education in the sciences and philosophy in Neyshābūr", stage: other, run_by: other, certainty: 0.7, cites: [{source: S1, locator: "name paragraph"}], how_known: "Britannica."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: TODO}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: UNKNOWN, how_known: "Equals timing.major_work_period (UNKNOWN)."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: {value: UNKNOWN, how_known: "Only the quatrains speak to religion, and their attribution is doubted (S1; P42)."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered: []
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "No statement of his own read; the quatrains (which Britannica says doubt divine providence) are not scored under P42."}
    B_cause:
      value: 3
      basis: inference_from_work
      certainty: 0.5
      cites: [{source: S1, locator: "mathematics and calendar paragraphs"}]
      how_known: "Working science only (P35)."
      rationale: "Algebra, calendar astronomy and critiques of Euclid; no statement of his own on law and exception, so B 3 at 0.5 with 4 as the named alternative (P35)."
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read (P7)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A is UNKNOWN."}
  statements: []
  changes_over_life: []
  coder_notes: "Coder's call. P42: Britannica reports doubt that he wrote poetry, that contemporaries took no notice of his verse, and that quatrains appeared under his name only two centuries later; FitzGerald's version is 'extremely free'. So no quatrain is scored. His philosophical treatises were not read."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Persian", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: UNKNOWN, how_known: "Only one contribution dated (P39)."}
  age_at_first_lasting_contribution: {value: 27, certainty: 0.5, cites: [{source: S1, locator: "opening; calendar paragraph"}], how_known: "1075 − 1048 = 27 (P30)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No statement read."}
  lio_views_relative_to_major_work: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "B from working science only."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Not read."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Not read.", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Not read."}
  circle_present: {value: "unclear", rationale: "No worldview statement read.", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  reading: "No scorable worldview statement."
  notes: ""

institutions:
  - {value: "Court of the Seljuq sultan Malik-Shāh, Eṣfahān (observatory)", role: astronomer, kind: "patron or funder", certainty: 0.7, cites: [{source: S1, locator: "calendar paragraph"}], how_known: "Britannica."}
collaborators:
  []

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 63"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags: []
  open_questions:
    - "Read his philosophical treatises (e.g., on existence) for statements of his own."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "Britannica Editors. \"Omar Khayyam.\" Encyclopaedia Britannica, updated 29 September 2026. https://www.britannica.com/biography/Omar-Khayyam-Persian-poet-and-astronomer."
    url: "https://www.britannica.com/biography/Omar-Khayyam-Persian-poet-and-astronomer"
    accessed: 2026-10-15
    reliability_note: "Unsigned editors' article body; Top Questions not cited."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions]
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

# Omar Khayyam

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Omar Khayyam (1048–1131), Persian mathematician and astronomer [S1]. Draft: primary_system UNKNOWN; A UNKNOWN; B 3 at 0.5 (P35); not plotted. Quatrains not scored (P42).

## Life and work

Neyshābūr, Samarkand, Eṣfahān [S1].

## Contribution and impact

See front matter [S1].

## Childhood and education

See front matter [S1].

## Adult working worldview

No statement of his own read; quatrains of doubted authorship not scored [S1].

## Heritage (context only)

See front matter [S1].

## Timing

See front matter [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Unclear [S1].

## Open questions

- Read his philosophical treatises (e.g., on existence) for statements of his own.

## Research log

- 2026-10-15: Read Britannica (Editors) body.
