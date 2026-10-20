---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z6)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z7 audit notes: 1453 kept (installation; RQ-Z7-N1 now codifies unveiling or installation as the P30 #1 event for artworks). S3 note corrected: the Gattamelata article text was read."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z6 audit fixes (blind audit at 85859f0, run 1; Z6-40 FAIL, not result-changing): Gattamelata's lasting status and the span end re-cited from the question box (P26) to Britannica's 'Gattamelata' topic article (S3): 'established a prototype for equestrian monuments in the West'. Year 1453 kept as the public installation (P30 #1), completion 1447–1450 noted. Span 1415–1453, age 29 unchanged."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z6, order P32: F 3, rank 160). Source: Britannica (H. W. Janson, signed; opening and 'Early career' read). No own words on religion read; religious commissions are work, not profession (P16). Not a scientist. Span 1415–1453 (St. Mark and St. George, c. 1415; Gattamelata 1447–53). primary_system UNKNOWN (lead CHRIST); A, B, C, D, E UNKNOWN; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}

identity:
  id: donatello
  display_name: "Donatello"
  roster:
    canonical_name: "Donatello"
    rank: 160
    F: 3
    models: [Gemini, GPT, Grok]
    band: "core (3–4)"
    status: "core"
    field: "art"
    field_bucket: "arts"
  full_name: {value: "Donato di Niccolò di Betto Bardi", certainty: 0.7, cites: [{source: S1, locator: "Original name in full"}], how_known: "Britannica."}
  native_name: {value: "Donatello", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica (diminutive of Donato)."}
  aliases:
    - {name: "Donato di Niccolò di Betto Bardi", kind: "birth name"}

basics:
  birth:
    date: {value: "1386", certainty: 0.5, cites: [{source: S1, locator: "Born"}], how_known: "Britannica: c. 1386."}
    place: {value: "Florence", modern_name: "Florence, Italy", polity_then: "Republic of Florence", certainty: 0.7, cites: [{source: S1, locator: "Born"}], how_known: "Britannica."}
  death:
    date: {value: "1466-12-13", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "Died"}], how_known: "Britannica."}
    place: {value: "Florence", modern_name: "Florence, Italy", polity_then: "Republic of Florence", certainty: 0.7, cites: [{source: S1, locator: "Died"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1415, certainty: 0.5, cites: [{source: S1, locator: "'Early career'"}], how_known: "St. Mark and St. George, both completed c. 1415: 'The full power of Donatello first appeared'."}
  era_bucket: {value: "1400 to 1599", certainty: 1.0, cites: [{source: S1, locator: "'Early career'"}], how_known: "1415 (P2)."}
  region_of_birth: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "Born"}], how_known: "Italy (P3)."}
  region_of_work: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Florence, Rome, Siena, Padua."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Italian", "Latin"], certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Inferred (Latin inscriptions)."}
  occupations: {value: ["sculptor"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

contribution:
  fields: {value: ["sculpture"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "St. Mark and St. George, Orsanmichele", year: 1415, kind: work, lasting: "'for the first time since Classical antiquity ... the human body is rendered as a self-activating functional organism' (S1)", certainty: 0.5, cites: [{source: S1, locator: "'Early career'"}], how_known: "Britannica; c. 1415."}
    - {value: "Schiacciato relief (St. George Killing the Dragon)", year: 1417, kind: method, lasting: "his 'bold new mode of relief' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Early career'"}], how_known: "Britannica: 1416–17."}
    - {value: "Gattamelata equestrian monument", year: 1453, kind: work, lasting: "'The statue established a prototype for equestrian monuments in the West' (S3)", certainty: 0.5, cites: [{source: S3, locator: "opening"}], how_known: "Britannica 'Gattamelata' (S3): 'completed between 1447 and 1450 but was not installed on its pedestal ... until 1453'. Year 1453 = public installation, a single dated year (P30 #1), so P12's range rule does not apply; RQ-Z7-N1 (Z7 audit) codifies installation or unveiling as the dating event for artworks; the completion range 1447–1450 is noted (by P12 it would give item year 1447 and, as the period end, 1450 under P30 rule 4)."}
  evidence_of_impact:
    - {value: "One of the greatest of all Italian Renaissance artists", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works:
    - {value: "Feast of Herod (Siena font)", year: 1427, kind: artwork, certainty: 0.7, cites: [{source: S1, locator: "'Early career'"}], how_known: "Britannica: 1423–27."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "One of the greatest Renaissance artists (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Niccolò di Betto Bardi, father, wool carder", role: father, certainty: 0.7, cites: [{source: S1, locator: "'Early career'"}], how_known: "Britannica."}
  household_circumstances: {value: "Humble origins (wool carder's son)", certainty: 0.7, cites: [{source: S1, locator: "'Early career'"}], how_known: "Britannica."}
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
  working_years: {value: "1415–1453", certainty: 0.5, cites: [{source: S1, locator: "'Early career'"}, {source: S3, locator: "opening"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: {value: UNKNOWN, how_known: "No own words read. Lead CHRIST: religious commissions (S1); work, not profession (P16)."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Lead only."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing read in his words (P19)."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30)."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read."}
    D_authority: {value: UNKNOWN, how_known: "Nothing read."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read."}
  mid_basin: {value: UNKNOWN, how_known: "A and B are UNKNOWN (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "Britannica: 'little is known about his character and personality'; look for contracts, tax declarations (catasto) or letters with religious language."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Florentine", certainty: 0.7, cites: [{source: S1, locator: "Born"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1415–1453", certainty: 0.5, cites: [{source: S1, locator: "'Early career'"}, {source: S3, locator: "opening"}], how_known: "St. Mark and St. George (c. 1415) to the Gattamelata's installation in 1453 (S3; completed 1447–1450; P29, P30 #1)."}
  age_at_first_lasting_contribution: {value: 29, certainty: 0.5, cites: [{source: S1, locator: "Born; 'Early career'"}], how_known: "1415 − 1386 = 29 (P30 year difference); both years approximate."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Sculpture; uses linear perspective but no proof (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions: []
collaborators:
  - {value: "Lorenzo Ghiberti", relation: "mentor or employer", note: "workshop member 1404–07", certainty: 0.7, cites: [{source: S1, locator: "'Early career'"}], how_known: "Britannica."}
  - {value: "Filippo Brunelleschi", relation: "rival or critic", note: "friends, later estranged", certainty: 0.7, cites: [{source: S1, locator: "'Early career'"}], how_known: "Britannica."}
  - {value: "Michelozzo", relation: collaborator, note: "partnership", certainty: 0.7, cites: [{source: S1, locator: "'Early career'"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 160"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "No own-voice text read."
  open_questions:
    - "Contracts, catasto, letters."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "H. W. Janson"
    citation: "Janson, H. W. 'Donatello.' Encyclopaedia Britannica. https://www.britannica.com/biography/Donatello"
    url: "https://www.britannica.com/biography/Donatello"
    accessed: 2026-10-19
    reliability_note: "Signed article; body cited, question boxes flagged (P26)."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, collaborators]
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
    author: "The Editors of Encyclopaedia Britannica (revised by Kathleen Kuiper)"
    citation: "'Gattamelata.' Encyclopaedia Britannica. https://www.britannica.com/topic/Gattamelata"
    url: "https://www.britannica.com/topic/Gattamelata"
    accessed: 2026-10-19
    reliability_note: "Topic article body, read (opening; same text on Britannica's scholars edition); not a question box."
    used_for: [contribution, timing]
---

## Summary

Donatello (c. 1386–1466), sculptor [S1]. Draft: all worldview fields UNKNOWN (lead CHRIST). Not plotted.

## Life and work

Florence, Rome, Siena, Padua [S1].

## Contribution and impact

St. Mark, St. George, schiacciato, David, Gattamelata [S1].

## Childhood and education

Wool carder's son; Ghiberti's workshop [S1].

## Adult working worldview

Not known from his words.

## Heritage (context only)

Florentine [S1].

## Timing

1415–1453, age 29 [S1, S3].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Archival documents.

## Research log

- 2026-10-19: Read Britannica (Janson), opening and 'Early career'.
- 2026-10-19: Z6 audit fixes: Gattamelata re-cited to Britannica's topic article.
