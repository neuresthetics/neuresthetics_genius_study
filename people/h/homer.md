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
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch F, order P32: F 5, rank 37). Basics from Britannica (G. S. Kirk). Whether Homer existed is uncertain; nothing is known of him beyond the name attached to the poems (S1). The gods of the Iliad and Odyssey are narrative: characters' and the narrative's words are not the author's view. All worldview fields UNKNOWN; mid_basin UNKNOWN. Undated works (P39). Draft, not reviewed."}

identity:
  id: homer
  display_name: "Homer"
  roster:
    canonical_name: "Homer"
    rank: 37
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: literature
    field_bucket: literature
  full_name: {value: "Homer", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Only the name is known (S1)."}
  native_name: {value: UNKNOWN, how_known: "Greek form not recorded in the source read."}
  aliases: []

basics:
  birth:
    date: {value: UNKNOWN, how_known: "Britannica gives only 'flourished 9th or 8th century bce?'."}
    place: {value: UNKNOWN, how_known: "'Ionia?' with a question mark (S1); traditions also name Chios."}
  death:
    date: {value: UNKNOWN, how_known: "Not given."}
    place: {value: UNKNOWN, how_known: "Not given."}
  first_lasting_contribution_year: {value: UNKNOWN, how_known: "The poems are undated; Britannica places him only in the 9th or 8th century BCE, with a question mark (P39)."}
  era_bucket: {value: "before -500", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts; 'Early references' (quotations from the poems by the mid-7th century BCE)"}], how_known: "Every possible working year (9th–8th century BCE; the poems are quoted by the mid-7th century) is before 500 BCE (P39); Britannica alone, 0.7."}
  region_of_birth: {value: UNKNOWN, how_known: "Birthplace uncertain ('Ionia?')."}
  region_of_work: {value: UNKNOWN, how_known: "'Ionia?' only; not coded."}
  sex_as_recorded: {value: "male", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Recorded as male by tradition; existence itself uncertain."}
  languages_of_work: {value: [Greek], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  occupations: {value: ["epic poet"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

contribution:
  fields: {value: ["epic poetry"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Iliad", year: UNKNOWN, kind: work, lasting: "basis of Greek education and culture; 'the most important poems of the classical European tradition' (S1)", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Authorship 'probable' but disputed (S1), so 0.5."}
    - {value: "Odyssey", year: UNKNOWN, kind: work, lasting: "as above (S1)", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "As above."}
  evidence_of_impact:
    - {value: "Basis of Greek education; model for Virgil's Aeneid; revived in Byzantium and the Renaissance", kind: "standard textbook canon", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "arguable", rationale: "The poems clearly meet the bar; whether a single person 'Homer' made them is uncertain (S1).", certainty: 0.5, cites: [{source: S1, locator: "opening; Q&A on authorship"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Nothing known."}
  family_religious_practice: {value: UNKNOWN, how_known: "Nothing known."}
  parents_and_household: []
  household_circumstances: {value: UNKNOWN, how_known: "Nothing known."}
  schooling: []
  early_mathematics: {value: UNKNOWN, how_known: "Nothing known."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Nothing known."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Nothing known."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: UNKNOWN, how_known: "Undated works (P39)."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No statement outside the poems; the poems are narrative."}
  primary_system: {value: UNKNOWN, how_known: "Nothing in the poet's own voice separable from the narrative. Herodotus credits Homer and Hesiod with 'the formulation of Greek theology' (via S1), which describes the poems' influence, not the poet's belief."}
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: HELLEN, reason: "Modern reconstructionist code; the poems are a source for it, not a profession of it. Rejected."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Gods in the poems are characters; their words and the narrative's events are not the author's view (coder's call)."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist; divine interventions in the plot are narrative, not a statement about nature."}
    C_ledger: {value: UNKNOWN, how_known: "As for A."}
    D_authority: {value: UNKNOWN, how_known: "As for A. The invocation of the Muse is a poetic convention (coder's call)."}
    E_scope: {value: UNKNOWN, how_known: "As for A (P7)."}
  mid_basin: {value: UNKNOWN, how_known: "A and B are UNKNOWN (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "Coder's call: a fictional character's words, and events of a narrative, are not the author's view; nothing in the poems is coded as Homer's worldview."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Greek (Ionian, by tradition)", certainty: 0.5, cites: [{source: S1, locator: "Quick Facts"}], how_known: "Britannica with a question mark."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Nothing known."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Nothing known."}
  childhood_catechism: {value: UNKNOWN, how_known: "Nothing known."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: UNKNOWN, how_known: "Undated works (P39)."}
  age_at_first_lasting_contribution: {value: UNKNOWN, how_known: "Undated (P39)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No statement."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Nothing known of the person."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Nothing known."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Oral tradition; nothing on the person.", certainty: 0.5, cites: [{source: S1, locator: "Q&A on oral composition"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Nothing known."}
  circle_present: {value: "unclear", rationale: "Nothing in the poet's own voice.", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  reading: "No reading possible."
  notes: ""

institutions: []
collaborators: []

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 37"}], how_known: "Study roster."}
  controversies:
    - {value: "Whether Homer existed and whether one poet shaped both epics", certainty: 0.7, cites: [{source: S1, locator: "Q&A; opening"}], how_known: "Britannica."}
  data_quality_flags:
    - "Existence uncertain; roster treats 'Homer' as a person. Raised for Jason (roster status is his call)."
  open_questions:
    - "None for worldview; a roster status review may be warranted."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Geoffrey S. Kirk"
    citation: "Kirk, Geoffrey S. \"Homer.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Homer-Greek-poet."
    url: "https://www.britannica.com/biography/Homer-Greek-poet"
    accessed: 2026-10-15
    reliability_note: "Signed article by a Homer scholar; Q&A header used only for authorship facts that the body repeats."
    used_for: [identity, basics, contribution, worldview, heritage, timing, lane_b, review]
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

# Homer

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Homer, the presumed author of the Iliad and the Odyssey, flourished perhaps in the 9th or 8th century BCE in Ionia [S1]. Whether he existed is uncertain [S1]. Draft: all worldview fields UNKNOWN; mid_basin UNKNOWN.

## Life and work

Nothing is known beyond the name attached to the poems [S1].

## Contribution and impact

The two epics, basis of Greek education and of the classical European tradition [S1].

## Childhood and education

Nothing known [S1].

## Adult working worldview

The gods in the poems are narrative and are not coded as the poet's view [S1].

## Heritage (context only)

Ionian Greek by tradition [S1].

## Timing

Undated (P39) [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Unclear [S1].

## Open questions

- Roster status.

## Research log

- 2026-10-15: Read Britannica (Kirk).
