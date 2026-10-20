---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z5)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z5, order P32: F 3, rank 153). Source: Britannica (Andrew Graham-Dixon, signed; opening, 'Becoming Caravaggio', 'Tragic childhood' read). No own words on religion read; religious commissions are work, not profession (P16). Not a scientist. Span 1601–1604 at 0.5 (Conversion of St. Paul 1601; Entombment 1602–04, latest year P30 #4), from captions. primary_system UNKNOWN (lead CHRIST); A UNKNOWN; B UNKNOWN; C, D, E UNKNOWN; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}

identity:
  id: caravaggio
  display_name: "Caravaggio"
  roster:
    canonical_name: "Caravaggio"
    rank: 153
    F: 3
    models: [Claude, GPT, Grok]
    band: "core (3–4)"
    status: core
    field: art
    field_bucket: arts
  full_name: {value: "Michelangelo Merisi", certainty: 0.7, cites: [{source: S1, locator: "Also known as"}], how_known: "Britannica."}
  native_name: {value: "Michelangelo Merisi da Caravaggio", certainty: 0.5, cites: [{source: S1, locator: "'Tragic childhood'"}], how_known: "Named after the town (S1); form of the full name the coder's."}
  aliases:
    - {name: "Michelangelo Merisi", kind: "birth name"}

basics:
  birth:
    date: {value: "1571-09-29", calendar: gregorian, certainty: 0.5, cites: [{source: S1, locator: "'Tragic childhood'"}], how_known: "Inferred from his name (feast of St Michael), per Britannica."}
    place: {value: "Caravaggio (or Milan), Lombardy", modern_name: "Caravaggio, Lombardy, Italy", polity_then: "Duchy of Milan", certainty: 0.5, cites: [{source: S1, locator: "Born; 'Tragic childhood'"}], how_known: "'probably born in the small town of Caravaggio'."}
  death:
    date: {value: "1610-07-18", calendar: gregorian, certainty: 0.5, cites: [{source: S1, locator: "Died"}], how_known: "Britannica: July 18/19, 1610."}
    place: {value: "Porto Ercole, Tuscany", modern_name: "Porto Ercole, Italy", polity_then: "State of the Presidi", certainty: 0.7, cites: [{source: S1, locator: "Died"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1601, certainty: 0.5, cites: [{source: S1, locator: "caption, The Conversion of St. Paul"}], how_known: "Earliest dated work named in what was read; earlier works named but undated (P12)."}
  era_bucket: {value: "1600 to 1749", certainty: 1.0, cites: [{source: S1, locator: "caption"}], how_known: "1601 (P2)."}
  region_of_birth: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "Born"}], how_known: "Italy (P3)."}
  region_of_work: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Rome; later Naples and Malta."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Italian"], certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Inferred."}
  occupations: {value: ["painter"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

contribution:
  fields: {value: ["painting"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "The Conversion of St. Paul (second version), Santa Maria del Popolo", year: 1601, kind: work, lasting: "listed among his best-known works (S1)", certainty: 0.5, cites: [{source: S1, locator: "caption; 'What is Caravaggio best known for?'"}], how_known: "Question box (P26), so 0.5."}
    - {value: "The Entombment of Christ", year: 1604, kind: work, lasting: "listed among his best-known works (S1)", certainty: 0.5, cites: [{source: S1, locator: "'Becoming Caravaggio' caption (1602–04)"}], how_known: "Range; latest year (P30 #4)."}
  evidence_of_impact:
    - {value: "Shaped Rembrandt, Velázquez, Géricault and filmmakers", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "'Becoming Caravaggio'"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "'His influence on the course of Western art has been immense' (S1).", certainty: 0.7, cites: [{source: S1, locator: "'Becoming Caravaggio'"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated (Catholic Lombardy is the setting only)."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Fermo Merisi, father, stonemason (d. 1577)", role: father, certainty: 0.7, cites: [{source: S1, locator: "'Tragic childhood'"}], how_known: "Britannica."}
    - {value: "Lucia Aratori, mother", role: mother, certainty: 0.7, cites: [{source: S1, locator: "'Tragic childhood'"}], how_known: "Britannica."}
  household_circumstances: {value: "Artisan family; father and most male relatives died of plague in 1577", certainty: 0.7, cites: [{source: S1, locator: "'Tragic childhood'"}], how_known: "Britannica."}
  schooling: []
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events:
    - {value: "Plague deaths of father, grandparents and uncle", year: 1577, certainty: 0.7, cites: [{source: S1, locator: "'Tragic childhood'"}], how_known: "Britannica."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1601–1604", certainty: 0.5, cites: [{source: S1, locator: "captions"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing read."}
  primary_system: {value: UNKNOWN, how_known: "No own words read. Lead CHRIST (Catholic): large-scale religious commissions (S1); religious subjects are work, not profession (P16)."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Lead only."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing read in his words (P19)."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30); nothing read."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read."}
    D_authority: {value: UNKNOWN, how_known: "Nothing read."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read."}
  mid_basin: {value: UNKNOWN, how_known: "A and B are UNKNOWN (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "Read the Roman and Maltese archival documents (e.g. his 1603 libel-trial testimony) and his admission to the Order of St John for any religious language."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Lombard", certainty: 0.5, cites: [{source: S1, locator: "'Tragic childhood'"}], how_known: "Coder's summary."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1601–1604", certainty: 0.5, cites: [{source: S1, locator: "captions"}], how_known: "Dated lasting works named in what was read (P29, P30); later works (e.g. Beheading of St. John) undated there."}
  age_at_first_lasting_contribution: {value: 30, certainty: 0.5, cites: [{source: S1, locator: "Born; caption"}], how_known: "1601 − 1571 = 30 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Painting (S1).", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "No views read.", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions: []
collaborators:
  - {value: "Costanza Colonna", relation: other, note: "patron; refuge and protection", certainty: 0.7, cites: [{source: S1, locator: "'Tragic childhood'"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 153"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "No own-voice text read; only the first sections of Britannica read."
  open_questions:
    - "Archival testimony; Maltese knighthood documents."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Andrew Graham-Dixon"
    citation: "Graham-Dixon, Andrew. \"Caravaggio.\" Encyclopaedia Britannica (updated 20 September 2026). https://www.britannica.com/biography/Caravaggio"
    url: "https://www.britannica.com/biography/Caravaggio"
    accessed: 2026-10-19
    reliability_note: "Signed article; body cited, question boxes flagged (P26)."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, collaborators]
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

## Summary

Caravaggio (1571–1610), painter [S1]. Draft: all worldview fields UNKNOWN (lead CHRIST). Not plotted.

## Life and work

Lombardy, Rome, Naples, Malta [S1].

## Contribution and impact

Religious works of radical realism and chiaroscuro [S1].

## Childhood and education

Stonemason's son; plague losses in 1577 [S1].

## Adult working worldview

Not known from his words.

## Heritage (context only)

Lombard [S1].

## Timing

1601–1604, age 30 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Archival testimony.

## Research log

- 2026-10-19: Read Britannica (Graham-Dixon), first sections.
