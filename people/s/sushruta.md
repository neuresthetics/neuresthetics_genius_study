---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA10)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA10, order P32: F 3, rank 219). Source: Britannica scholars edition (unsigned, read in full; three paragraphs). He 'flourished c. 6th century bce'; birth and death UNKNOWN. Lasting: the Sushruta-samhita, 'the main source of knowledge about surgery in ancient India', an 'influential treatise' with 'groundbreaking operations' (S1); lasting at 0.5 (thin wording, P13 borderline). No year: first lasting year, span, age UNKNOWN; era UNKNOWN under P39 (no dated work; candidate 'before -500' from the floruit). Attribution: S1 credits the treatise to him without qualification, but only one short source was read; the text's own date and authorship are not tested here (P42, Sun Tzu precedent). Worldview UNKNOWN. B UNKNOWN pending attribution, alternative B 3 at 0.5 (Galen precedent: empirical surgery and dissection). Not plotted. Draft, not reviewed."}

identity:
  id: sushruta
  display_name: "Sushruta"
  roster:
    canonical_name: "Sushruta"
    rank: 219
    F: 3
    models: [Claude, DeepSeek, Grok]
    band: "core (3–4)"
    status: "core"
    field: "medicine"
    field_bucket: "medicine"
  full_name: {value: "Sushruta", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  native_name: {value: UNKNOWN, how_known: "Sanskrit script not printed in S1."}
  aliases:
    - {name: "Suśruta", kind: "transliteration"}

basics:
  birth:
    date: {value: UNKNOWN, how_known: "Not stated; S1 gives only a floruit (c. 6th century BCE)."}
    place: {value: UNKNOWN, how_known: "Not stated in S1."}
  death:
    date: {value: UNKNOWN, how_known: "Not stated."}
    place: {value: UNKNOWN, how_known: "Not stated."}
  first_lasting_contribution_year: {value: UNKNOWN, how_known: "The Sushruta-samhita is undated in S1 (P39; Sun Tzu precedent)."}
  era_bucket: {value: UNKNOWN, how_known: "No dated lasting work (P39 strict); floruit 'c. 6th century bce' (S1) gives 'before -500' as the candidate, but 'c.' leaves the -500 edge open."}
  region_of_birth: {value: "South Asia", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "'ancient Indian surgeon' (S1); place not given (P3)."}
  region_of_work: {value: "South Asia", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Ancient India (S1)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded ('his')."}
  languages_of_work: {value: UNKNOWN, how_known: "Not stated in S1 (Sanskrit presumed, not sourced)."}
  occupations: {value: ["surgeon"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

contribution:
  fields: {value: ["medicine", "surgery"], certainty: 0.7, cites: [{source: S1, locator: "opening; para. 2"}], how_known: "Britannica: shalya tantra; Ayurveda."}
  lasting_original_contributions:
    - {value: "Sushruta-samhita (treatise on surgery: rhinoplasty, lithotomy, removal of a dead fetus, dissection methods)", year: UNKNOWN, kind: "work", lasting: "'his influential treatise Sushruta-samhita, the main source of knowledge about surgery in ancient India' (S1)", certainty: 0.5, cites: [{source: S1, locator: "opening; para. 2"}], how_known: "Undated in S1; 0.5 because 'influential' and 'groundbreaking' are thin lasting wording (P13 borderline) and the attribution is untested."}
  evidence_of_impact: []
  major_works: []
  honours: []
  definition_fit: {value: "arguable", rationale: "Pioneering surgery (S1); dating and authorship untested.", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household: []
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
  working_years: {value: UNKNOWN, how_known: "Equals timing.major_work_period (UNKNOWN)."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: {value: UNKNOWN, how_known: "No own words or scholarly reconstruction of belief in S1."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered: []
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing read (P19)."}
    B_cause: {value: UNKNOWN, how_known: "Held UNKNOWN: surgery and dissection would make him a scientist under the Galen precedent (alternative B 3 at 0.5, alt 4, P35), but whether the samhita's methods are his own work is untested (P42)."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, so the P4 test cannot be applied (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "Read a scholarly history of Indian medicine (e.g., Wujastyk, The Roots of Ayurveda; Meulenbeld, A History of Indian Medical Literature) for the date and layers of the samhita."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: UNKNOWN, how_known: "No dated lasting item (P29, P30)."}
  age_at_first_lasting_contribution: {value: UNKNOWN, how_known: "Birth and work dates UNKNOWN."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Surgery (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions: []
collaborators: []

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 219"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Life and work undated; era UNKNOWN (P39)."
    - "Attribution of the samhita untested (P42)."
    - "One short source."
  open_questions:
    - "Date and authorship layers of the Sushruta-samhita."
    - "Scientist for B if the attribution holds (Galen precedent)?"

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "The Editors of Encyclopaedia Britannica"
    citation: "'Sushruta.' Encyclopaedia Britannica (scholars edition). https://kids.britannica.com/scholars/article/Sushruta/599307"
    url: "https://kids.britannica.com/scholars/article/Sushruta/599307"
    accessed: 2026-10-19
    reliability_note: "Unsigned article, scholars edition, read in full."
    used_for: [identity, basics, contribution]
  - id: S2
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

Sushruta (fl. c. 6th century BCE), surgeon [S1]. Draft: undated; worldview UNKNOWN. Not plotted.

## Life and work

Ancient India [S1].

## Contribution and impact

Sushruta-samhita [S1].

## Childhood and education

Not stated.

## Adult working worldview

None read.

## Heritage (context only)

Not stated.

## Timing

UNKNOWN.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Dating; attribution.

## Research log

- 2026-10-20: Read Britannica (scholars edition).
