---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z3)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z3, order P32: F 3, rank 147). Source: Britannica (Marcel Florkin, signed). No own words on religion read; Catholic setting (Leuven, imperial court) and a pilgrimage to the Holy Sepulchre in 1564 are leads. A scientist (P30: anatomy from his own dissections). Span 1543 (Fabrica). primary_system UNKNOWN (lead CHRIST); A UNKNOWN; B 3 (0.5, alt 4); C, D, E UNKNOWN; mid_basin UNKNOWN. Not plotted (no A). Draft, not reviewed."}

identity:
  id: vesalius-andreas
  display_name: "Andreas Vesalius"
  roster:
    canonical_name: "Andreas Vesalius"
    rank: 147
    F: 3
    models: [Claude, DeepSeek, Gemini]
    band: "core (3–4)"
    status: core
    field: medicine
    field_bucket: medicine
  full_name: {value: "Andreas Vesalius", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  native_name: {value: "Andries van Wesel", certainty: 0.7, cites: [{source: S1, locator: "opening (Flemish)"}], how_known: "Britannica."}
  aliases:
    - {name: "Vesalius-Andreas", kind: "roster alias"}
    - {name: "Andries van Wesel", kind: "birth name"}

basics:
  birth:
    date: {value: "1514-12", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica: December 1514."}
    place: {value: "Brussels, Duchy of Brabant", modern_name: "Brussels, Belgium", polity_then: "Habsburg Netherlands", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "1564-06", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica: June 1564."}
    place: {value: "Zacynthus (Zakynthos)", modern_name: "Zakynthos, Greece", polity_then: "Republic of Venice", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1543, certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "De humani corporis fabrica, printed in Basel in 1543."}
  era_bucket: {value: "1400 to 1599", certainty: 1.0, cites: [{source: S1, locator: "'Life'"}], how_known: "1543 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Belgium (P3)."}
  region_of_work: {value: "Southern Europe", certainty: 0.5, cites: [{source: S1, locator: "'Life'"}], how_known: "Padua (the Fabrica's dissections and drawings); later the imperial court and Madrid; 0.5."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Latin"], certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Latin titles."}
  occupations: {value: ["physician", "anatomist", "lecturer in surgery (Padua)", "imperial physician"], certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica."}

contribution:
  fields: {value: ["anatomy", "medicine"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "De humani corporis fabrica libri septem", year: 1543, kind: work, lasting: "'the first comprehensive textbook of anatomy'; 'After Vesalius, anatomy became a scientific discipline' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Life'"}], how_known: "Britannica."}
  evidence_of_impact:
    - {value: "After Vesalius, anatomy became a scientific discipline", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica."}
  major_works: []
  honours:
    - {value: "Made a count, with a lifetime pension, by Charles V", year: 1556, certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica."}
  definition_fit: {value: "clearly meets", rationale: "Founder of modern anatomy (S1).", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated; Catholic Brabant is the setting only."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household: []
  household_circumstances: {value: "Family of physicians and pharmacists", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica."}
  schooling:
    - {value: "Catholic University of Leuven", stage: university, run_by: "religious body", years: "1529–1533", certainty: 0.5, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica; run_by the coder's reading of 'Catholic University', 0.5."}
    - {value: "University of Paris medical school", stage: university, run_by: other, years: "1533–1536", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1543", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing read."}
  primary_system: {value: UNKNOWN, how_known: "No own words read. Lead CHRIST (Catholic): Catholic University of Leuven, service to Charles V and Philip II, pilgrimage to the Holy Sepulchre in 1564 (S1)."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Lead only (setting and pilgrimage, S1)."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing read in his words (P19)."}
    B_cause:
      value: 3
      basis: scholarly_reconstruction
      certainty: 0.5
      cites: [{source: S1, locator: "'Life'"}]
      how_known: "A scientist with working science only (P30: anatomy from his own dissections, 'critically evaluating ancient texts', S1), so B 3 at 0.5, alternative 4 (P35)."
      rationale: "P35."
      alternatives:
        - {value: 4, note: "P35 alternative.", cites: [{source: S1, locator: "'Life'"}]}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read."}
    D_authority: {value: UNKNOWN, how_known: "Observation over Galen's authority is medical, not religious (P16)."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read."}
  mid_basin: {value: UNKNOWN, how_known: "A UNKNOWN."}
  statements: []
  changes_over_life: []
  coder_notes: "Read the Fabrica's dedication to Charles V for any religious language."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Brabantine (Flemish)", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1543", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "The Fabrica (1543), the only lasting work named (P29, P30)."}
  age_at_first_lasting_contribution: {value: 29, certainty: 0.7, cites: [{source: S1, locator: "opening; 'Life'"}], how_known: "1543 − 1514 = 29 (P30 year difference; Britannica: 'not yet 28' in early 1543, an inconsistency in the source with his December 1514 birth)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Descriptive anatomy (S1).", certainty: 0.5, cites: [{source: S1, locator: "'Life'"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "No views read.", certainty: 0.5, cites: [{source: S1, locator: "'Life'"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "University of Padua", role: "lecturer in surgery", years: "1537–1543", kind: university, certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica."}
  - {value: "Household of Emperor Charles V; court of Philip II", role: physician, years: "1543–1564", kind: other, certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica."}
collaborators:
  - {value: "Galen", roster_id: galen, relation: "rival or critic", note: "corrected Galenic anatomy", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 147"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "No own-voice text read."
  open_questions:
    - "Fabrica preface; letters."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Marcel Florkin"
    citation: "Florkin, Marcel. \"Andreas Vesalius.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Andreas-Vesalius. Read live 2026-10-19."
    url: "https://www.britannica.com/biography/Andreas-Vesalius"
    accessed: 2026-10-19
    reliability_note: "Signed article; body cited, question boxes not (P26)."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [review]
---

# Andreas Vesalius

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Andreas Vesalius (1514–1564), Renaissance anatomist [S1]. Draft: primary_system UNKNOWN (lead CHRIST); A UNKNOWN; B 3 (0.5, alt 4). Not plotted.

## Life and work

Brussels, Leuven, Paris, Padua, the imperial court [S1].

## Contribution and impact

The Fabrica (1543) [S1].

## Childhood and education

Family of physicians [S1].

## Adult working worldview

Not known from his words [S1].

## Heritage (context only)

Brabantine [S1].

## Timing

1543, age 29 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Own-voice reading.

## Research log

- 2026-10-19: Read Britannica (Florkin).
