---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z10)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z10 audit fixes (FAIL, P13; v8's calls on the auditor's advice): 'achieved recognition as a noted inventor' is not a lasting claim about the device, and its later use is only in the Top Questions box (P26), so no lasting work is supported; the patent moves to major_works, dated by its 10 June 1941 filing (formal submission, P30 #1). Span 1942 -> UNKNOWN; age and era UNKNOWN. Not plotted."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z10, order P32: F 3, rank 177). Basics from Britannica (Britannica Editors; body only, the Top Questions box not cited, P26); the patent from Google Patents (US 2,292,387, 'Secret communication system', filed 1941-06-10, granted 1942-08-11, inventors Hedy Kiesler Markey and George Antheil). No own-voice statement on religion or nature read. Not a scientist (invention, P33). All worldview fields UNKNOWN. Span 1942 (patent grant), age 29 (birth 1913/14; earlier year used, as for Chaucer). Not plotted. Draft, not reviewed."}

identity:
  id: lamarr-hedy
  display_name: "Hedy Lamarr"
  roster:
    canonical_name: "Hedy Lamarr"
    rank: 177
    F: 3
    models: [Gemini, GPT, Grok]
    band: "core (3–4)"
    status: "core"
    field: "invention"
    field_bucket: "invention / engineering"
  full_name: {value: "Hedy Lamarr", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  native_name: {value: "Hedwig Eva Maria Kiesler", certainty: 0.7, cites: [{source: S1, locator: "heading"}], how_known: "Britannica: original name."}
  aliases:
    - {name: "Hedy-Lamarr", kind: "roster alias"}
    - {name: "Lamarr-Hedy", kind: "roster alias"}
    - {name: "Hedwig Eva Maria Kiesler", kind: "birth name"}
    - {name: "Hedy Kiesler Markey", kind: "other"}

basics:
  birth:
    date: {value: "1913-11-09", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Britannica: 'November 9, 1913/14'; year uncertain."}
    place: {value: "Vienna", modern_name: "Vienna, Austria", polity_then: "Austria-Hungary", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "2000-01-19", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "near Orlando, Florida", modern_name: "Orlando, Florida, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: UNKNOWN, how_known: "No lasting work supported (P13): Britannica's body says only that she 'achieved recognition as a noted inventor'; the device's later use is in the Top Questions box (P26). Z10 audit."}
  era_bucket: {value: UNKNOWN, how_known: "No first lasting year (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Austria (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Hollywood from 1937."}
  sex_as_recorded: {value: "female", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English", "German"], certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Inferred."}
  occupations: {value: ["film actress", "inventor"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

contribution:
  fields: {value: ["radio communications"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions: []
  evidence_of_impact:
    - {value: "Recognized as a noted inventor years after her screen career", kind: "other", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works:
    - {value: "Frequency-hopping 'secret communication system' (with George Antheil), US patent 2,292,387", year: 1941, kind: "device", certainty: 0.7, cites: [{source: S2, locator: "front page"}], how_known: "Filed 10 June 1941 (formal submission, the P30 #1 dating event), granted 11 August 1942. Not a supported lasting contribution (P13, P26)."}
    - {value: "Algiers", year: 1938, kind: "other", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
    - {value: "Samson and Delilah", year: 1949, kind: "other", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
  honours: []
  definition_fit: {value: "arguable", rationale: "Film star; inventor recognized late (S1).", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Prosperous Viennese banker", role: "father", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
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
  working_years: {value: UNKNOWN, how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: {value: UNKNOWN, how_known: "No statement on religion read."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered: []
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing first-hand read (P19)."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P33: the device is an invention); no statement on nature read."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: UNKNOWN, how_known: "A and B are UNKNOWN (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "Ecstasy and Me (1966) was disowned by her (she sued its collaborators, S1), so it supports at most 0.5 (P29); interviews and Shearer's biography (2010) are leads."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated in the source read."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: UNKNOWN, how_known: "No supported lasting work (P13; Z10 audit). The patent would date to its 1941 filing (P30 #1) if a source called it lasting."}
  age_at_first_lasting_contribution: {value: UNKNOWN, how_known: "No first lasting year."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Device invention (S1, S2).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "Metro-Goldwyn-Mayer", role: "contract actress", years: "1938–1945", kind: "employer", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
collaborators:
  - {value: "George Antheil", relation: "collaborator", note: "co-inventor", certainty: 0.7, cites: [{source: S2, locator: "front page"}], how_known: "Patent."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 177"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "No worldview statement read."
  open_questions:
    - "Interviews; biographies."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Britannica Editors"
    citation: "'Hedy Lamarr.' Encyclopaedia Britannica. https://www.britannica.com/biography/Hedy-Lamarr"
    url: "https://www.britannica.com/biography/Hedy-Lamarr"
    accessed: 2026-10-19
    reliability_note: "Unsigned article; body cited, question boxes not used (P26)."
    used_for: [identity, basics, contribution, childhood, timing, institutions]
  - id: S2
    type: primary
    kind: "archive record"
    author: "Hedy Kiesler Markey and George Antheil"
    citation: "Markey, Hedy Kiesler, and George Antheil. 'Secret communication system.' US Patent 2,292,387, filed 10 June 1941, granted 11 August 1942. Google Patents. https://patents.google.com/patent/US2292387A/en"
    url: "https://patents.google.com/patent/US2292387A/en"
    accessed: 2026-10-19
    reliability_note: "Patent record (dates and inventors read)."
    used_for: [basics, contribution, timing, collaborators]
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

Hedy Lamarr (1913/14–2000), film star and inventor [S1]. Draft: all UNKNOWN. Not plotted.

## Life and work

Vienna; Hollywood [S1].

## Contribution and impact

Frequency-hopping patent, filed 1941 [S2].

## Childhood and education

Private tutors; Reinhardt's school [S1].

## Adult working worldview

None read.

## Heritage (context only)

Not stated.

## Timing

UNKNOWN (no supported lasting work).

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Interviews.

## Research log

- 2026-10-19: Read Britannica; patent record.
