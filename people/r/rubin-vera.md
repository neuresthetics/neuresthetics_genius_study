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
    - {date: 2026-10-20, by: "Grok Bot", summary: "AA10 audit fix: if the thesis result ever counts, span alternative 1950–1970 (December 1950 AAS talk), age 22."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA10, order P32: F 3, rank 221). Sources: Britannica scholars edition, signed by Kelly Gisonna (read in full); ADS record of Rubin and Ford 1970 (S3). Lasting: galaxy rotation evidence for dark matter; 'The existence of dark matter was previously only a conjecture but was confirmed through Rubin's work' (S1); the Andromeda rotation paper appeared in ApJ 159 (February 1970) (S3). The 1951 supergalactic-plane result ('now known to be evidence of the supergalactic plane') is listed as a major work, not lasting (AA10 audit: it says the result was right, not that it lasted; Mirzakhani line). If it ever counts, P30 dates it to her December 1950 AAS talk: span alternative 1950–1970, age 22. Span 1970, age 42. Scientist: B 3 at 0.5, alt 4 (P35). Worldview UNKNOWN; heritage Jewish 0.7. Not plotted. Draft, not reviewed."}

identity:
  id: rubin-vera
  display_name: "Vera Rubin"
  roster:
    canonical_name: "Vera Rubin"
    rank: 221
    F: 3
    models: [Claude, DeepSeek, Gemini]
    band: "core (3–4)"
    status: "core"
    field: "astronomy"
    field_bucket: "astronomy"
  full_name: {value: "Vera Florence Cooper Rubin", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  native_name: {value: "Vera Rubin", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  aliases:
    - {name: "Vera Cooper", kind: "birth name"}

basics:
  birth:
    date: {value: "1928-07-23", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
    place: {value: "Philadelphia, Pennsylvania", modern_name: "Philadelphia, Pennsylvania, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  death:
    date: {value: "2016-12-25", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
    place: {value: "Princeton, New Jersey", modern_name: "Princeton, New Jersey, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1970, certainty: 0.7, cites: [{source: S1, locator: "The supergalactic plane, dark matter, and legacy"}, {source: S3, locator: "abstract record"}], how_known: "Work with Ford at Carnegie from 1965 (S1); published as Rubin and Ford, ApJ 159, 379, February 1970 (S3); P30 publication."}
  era_bucket: {value: "1950 on", certainty: 1.0, cites: [{source: S1, locator: "The supergalactic plane, dark matter, and legacy"}], how_known: "1970 (P2)."}
  region_of_birth: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "United States (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "The supergalactic plane, dark matter, and legacy"}], how_known: "Carnegie Institution, Washington, D.C."}
  sex_as_recorded: {value: "female", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "English papers."}
  occupations: {value: ["astronomer"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}

contribution:
  fields: {value: ["astronomy"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Flat galaxy rotation curves (Andromeda, with W. Kent Ford, then many galaxies) as evidence for dark matter halos", year: 1970, kind: "discovery", lasting: "'The existence of dark matter was previously only a conjecture but was confirmed through Rubin's work' (S1)", certainty: 0.7, cites: [{source: S1, locator: "The supergalactic plane, dark matter, and legacy"}, {source: S3, locator: "abstract record"}], how_known: "Rubin and Ford, 'Rotation of the Andromeda Nebula from a Spectroscopic Survey of Emission Regions', ApJ 159 (1970) (S3)."}
  evidence_of_impact:
    - {value: "Vera C. Rubin Observatory (renamed December 2019)", kind: "named after them", certainty: 0.7, cites: [{source: S1, locator: "Legacy and Vera C. Rubin Observatory"}], how_known: "Britannica."}
    - {value: "National Medal of Science (1993)", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "Legacy and Vera C. Rubin Observatory"}], how_known: "Britannica."}
  major_works:
    - {value: "Master's thesis on motions of 109 galaxies ('Rotation of the Universe'), 'now known to be evidence of the supergalactic plane'", year: 1951, kind: "other", certainty: 0.7, cites: [{source: S1, locator: "The supergalactic plane, dark matter, and legacy"}], how_known: "Cornell M.A. 1951 (S1)."}
    - {value: "Doctoral dissertation on galaxy clustering (Georgetown)", year: 1954, kind: "other", certainty: 0.7, cites: [{source: S1, locator: "The supergalactic plane, dark matter, and legacy"}], how_known: "Britannica."}
  honours:
    - {value: "National Medal of Science", year: 1993, certainty: 0.7, cites: [{source: S1, locator: "Legacy and Vera C. Rubin Observatory"}], how_known: "Britannica."}
  definition_fit: {value: "clearly meets", rationale: "Dark matter evidence (S1).", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Younger of two daughters of Jewish immigrants: father Philip Cooper (born Pesach Kobchefski, Vilnius), electrical engineer at Bell Telephone; mother Rose Applebaum (from Bessarabia)", role: "family", certainty: 0.7, cites: [{source: S1, locator: "Family and childhood"}], how_known: "Britannica."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling:
    - {value: "Vassar College (B.A. astronomy 1948); Cornell (M.A. 1951); Georgetown (Ph.D. 1954, adviser George Gamow)", certainty: 0.7, cites: [{source: S1, locator: "Education and early career; The supergalactic plane"}], how_known: "Britannica."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1970", certainty: 0.7, cites: [{source: S1, locator: "The supergalactic plane, dark matter, and legacy"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: {value: UNKNOWN, how_known: "No own words on belief read in S1."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: JUDA, reason: "Heritage only: Jewish immigrant parents (S1)."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing first-hand read (P19)."}
    B_cause: 
      value: 3
      basis: inference_from_work
      certainty: 0.5
      cites: [{source: S1, locator: "The supergalactic plane, dark matter, and legacy"}]
      how_known: "Scientist (P30). B from working science with no statement of their own on law and exception, so 3 at 0.5, alternative 4, never 4 (P35)."
      rationale: "Inferred unseen mass from measured orbital velocities under gravitation (S1): lawful nature in her science. Alternative 4."
      alternatives:
        - {value: 4, note: "Working science cannot tell lawful-with-exceptions from exceptionless (P35).", cites: [{source: S1, locator: "The supergalactic plane, dark matter, and legacy"}]}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, so the P4 test cannot be applied (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "Lead: her published interviews (e.g., Lightman and Brawer, Origins, 1990) may contain own words on religion; not read."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: "Jewish", certainty: 0.7, cites: [{source: S1, locator: "Family and childhood"}], how_known: "'daughters of Jewish immigrants from eastern Europe' (S1)."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1970", certainty: 0.7, cites: [{source: S1, locator: "The supergalactic plane, dark matter, and legacy"}], how_known: "The one lasting item (P29, P30). Alternative 1950–1970 only if the thesis result were counted as lasting (December 1950 AAS talk)."}
  age_at_first_lasting_contribution: {value: 42, certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S3, locator: "abstract record"}], how_known: "1970 − 1928 = 42 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Galaxy dynamics (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "Carnegie Institution, Department of Terrestrial Magnetism", role: "astronomer", years: "1965–UNKNOWN", kind: "research institute", certainty: 0.7, cites: [{source: S1, locator: "The supergalactic plane, dark matter, and legacy"}], how_known: "Britannica."}
collaborators:
  - {value: "W. Kent Ford", relation: "collaborator", note: "Andromeda rotation work", certainty: 0.7, cites: [{source: S1, locator: "The supergalactic plane, dark matter, and legacy"}], how_known: "Britannica."}
  - {value: "George Gamow", relation: "teacher", note: "doctoral adviser", certainty: 0.7, cites: [{source: S1, locator: "The supergalactic plane, dark matter, and legacy"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 221"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Worldview: no source."
    - "1951 supergalactic result not listed as lasting (P13 borderline)."
  open_questions:
    - "Own words on belief (interviews)."
    - "If the thesis result ever counts as lasting: dated by her talk at the 84th AAS meeting, Haverford, 27–29 December 1950 (P30), so span alternative 1950–1970, age 22 (AA10 audit; AAS history page not read here)."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Kelly Gisonna"
    citation: "Gisonna, Kelly. 'Vera Rubin.' Encyclopaedia Britannica (scholars edition). https://kids.britannica.com/scholars/article/Vera-Rubin/635711"
    url: "https://kids.britannica.com/scholars/article/Vera-Rubin/635711"
    accessed: 2026-10-19
    reliability_note: "Signed article, scholars edition, read in full."
    used_for: [identity, basics, contribution, childhood, heritage, timing, institutions, collaborators]
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
    type: secondary
    kind: "database"
    author: "NASA ADS"
    citation: "Rubin, V. C., and W. K. Ford Jr. 'Rotation of the Andromeda Nebula from a Spectroscopic Survey of Emission Regions.' Astrophysical Journal 159 (1970): 379–403. doi:10.1086/150317. ADS record https://ui.adsabs.harvard.edu/abs/1970ApJ...159..379R/abstract"
    url: "https://ui.adsabs.harvard.edu/abs/1970ApJ...159..379R/abstract"
    accessed: 2026-10-19
    reliability_note: "Bibliographic record and abstract read."
    used_for: [contribution, timing]
---

## Summary

Vera Rubin (1928–2016), astronomer [S1]. Draft: worldview UNKNOWN. Not plotted.

## Life and work

Philadelphia; Washington [S1].

## Contribution and impact

Dark matter evidence 1970 [S1, S3].

## Childhood and education

Vassar; Cornell; Georgetown [S1].

## Adult working worldview

None read.

## Heritage (context only)

Jewish (heritage).

## Timing

1970, age 42 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Own words; 1951 item.

## Research log

- 2026-10-20: AA10 audit fix: if the thesis result ever counts, span alternative 1950–1970 (December 1950 AAS talk), age 22.
- 2026-10-20: Read Britannica (Gisonna, scholars edition); ADS record.
