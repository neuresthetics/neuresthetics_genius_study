---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA7)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-20
  change_log:
    - {date: 2026-10-20, by: "Grok Bot", summary: "AA8 audit fix: ICM 2022 survey locator §2.2."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA7, order P32: F 3, rank 206, provisional). Sources: the IMU's 2014 Fields Medal statement 'The Work of Maryam Mirzakhani' (read in full) and the Simons Foundation obituary (Sumner, 2017, read in full). Lasting work (after the AA7 audit, v8's call on the auditor's advice): the Eskin–Mirzakhani(–Mohammadi) 'magic wand' theorems (arXiv preprints 2013); the ICM 2022 survey by Jon Chaika and Barak Weiss (S4, EMS Press, read in full; authors and wording verified) says 'This work has revolutionized the study of dynamics on translation surfaces and has already had many applications in geometry'. The 2004 thesis results are dropped as lasting (P13, Lamarr/Johnson precedent: 'decisive step forward' and 'new and unexpected proof' are prize-time praise) and kept as a major work. Span 2013, age 36, at 0.5. Mathematician, not a scientist. Worldview: no own words read. primary_system UNKNOWN; A UNKNOWN; B UNKNOWN; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}

identity:
  id: mirzakhani-maryam
  display_name: "Maryam Mirzakhani"
  roster:
    canonical_name: "Maryam Mirzakhani"
    rank: 206
    F: 3
    models: [Claude, GPT, Grok]
    band: "core (3–4)"
    status: "provisional"
    field: "mathematics"
    field_bucket: "mathematics"
  full_name: {value: "Maryam Mirzakhani", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "IMU."}
  native_name: {value: UNKNOWN, how_known: "Persian script form not printed in the sources read."}
  aliases:
    - {name: "Maryam-Mirzakhani", kind: "roster alias"}

basics:
  birth:
    date: {value: "1977", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "IMU: 'Born in 1977'; day not given in the sources read."}
    place: {value: "Tehran", modern_name: "Tehran, Iran", polity_then: "Imperial State of Iran", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "IMU."}
  death:
    date: {value: "2017-07-14", certainty: 0.7, cites: [{source: S2, locator: "para. 2"}], how_known: "Simons Foundation."}
    place: {value: UNKNOWN, how_known: "Place of death not stated in the sources read."}
  first_lasting_contribution_year: {value: 2013, certainty: 0.5, cites: [{source: S1, locator: "References"}, {source: S4, locator: "§2.2"}], how_known: "Eskin–Mirzakhani preprint arXiv:1302.3320 (2013), the first public statement (P30); lasting per S4 ('has revolutionized the study of dynamics on translation surfaces'). 0.5: one lasting source."}
  era_bucket: {value: "1950 on", certainty: 1.0, cites: [{source: S1, locator: "Biography"}], how_known: "2013 (P2)."}
  region_of_birth: {value: "Middle East and North Africa", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "Iran (P3 exception: MENA)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "Harvard, Princeton, Stanford; home-region alternative MENA (AA6 rule)."}
  sex_as_recorded: {value: "female", certainty: 0.7, cites: [{source: S2, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "References"}], how_known: "English papers."}
  occupations: {value: ["mathematician", "professor"], certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "IMU."}

contribution:
  fields: {value: ["mathematics", "geometry", "dynamical systems"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "IMU."}
  lasting_original_contributions:
    - {value: "Eskin–Mirzakhani(–Mohammadi) 'magic wand' theorems: rigidity of the SL2(R) action on moduli space (with Alex Eskin and Amir Mohammadi)", year: 2013, kind: "discovery", lasting: "'This work has revolutionized the study of dynamics on translation surfaces and has already had many applications in geometry' (S4, Chaika and Weiss, ICM 2022); 'a major breakthrough' (S1)", certainty: 0.5, cites: [{source: S1, locator: "p. 3; References"}, {source: S4, locator: "§2.2"}], how_known: "arXiv preprints 1302.3320 and 1305.3015 (2013), the first public statements (P30). 0.5: one lasting source."}
  evidence_of_impact:
    - {value: "Fields Medal 2014, the first woman to receive it", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S2, locator: "para. 1"}], how_known: "Simons Foundation."}
  major_works:
    - {value: "PhD thesis, Harvard (simple closed geodesics; Weil–Petersson volumes; new proof of Witten's conjecture)", year: 2004, kind: "other", certainty: 0.7, cites: [{source: S1, locator: "pp. 2–3; Biography"}], how_known: "IMU; not lasting under P13 (AA7 audit)."}
    - {value: "'Growth of the number of simple closed geodesics on hyperbolic surfaces', Annals of Mathematics", year: 2008, kind: "paper or paper series", certainty: 0.7, cites: [{source: S1, locator: "References"}], how_known: "IMU."}
    - {value: "'Ergodic theory of the earthquake flow'", year: 2008, kind: "paper or paper series", certainty: 0.7, cites: [{source: S1, locator: "References"}], how_known: "IMU."}
  honours:
    - {value: "Fields Medal", year: 2014, certainty: 0.7, cites: [{source: S2, locator: "para. 1"}], how_known: "Simons Foundation."}
    - {value: "Satter Prize (AMS)", year: 2013, certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "IMU."}
    - {value: "Blumenthal Award", year: 2009, certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "IMU."}
  definition_fit: {value: "clearly meets", rationale: "Fields Medal; striking and highly original contributions (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "IMU."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household: []
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling:
    - {value: "Iranian IMO team (gold 1994, 1995); Sharif University, Tehran; Harvard PhD 2004 under Curtis McMullen", certainty: 0.7, cites: [{source: S2, locator: "para. 3"}, {source: S1, locator: "Biography"}], how_known: "Simons; IMU."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "2013", certainty: 0.5, cites: [{source: S1, locator: "Biography; References"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: {value: UNKNOWN, how_known: "No own words on belief read."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered: []
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing first-hand read (P19)."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist: a mathematician (P30); no statement on nature read."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, so the P4 test cannot be applied (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "Interviews (Quanta 2014; Clay Institute 2008) may have own words; not read."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated in the sources read."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "2013", certainty: 0.5, cites: [{source: S1, locator: "References"}, {source: S4, locator: "§2.2"}], how_known: "The one listed lasting item (P29, P30); 0.5."}
  age_at_first_lasting_contribution: {value: 36, certainty: 0.5, cites: [{source: S1, locator: "Biography"}], how_known: "2013 − 1977 = 36 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "Hyperbolic geometry and moduli spaces (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "Princeton University; Clay Mathematics Institute", role: "assistant professor; research fellow", years: "2004–2008", kind: "university", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "IMU."}
  - {value: "Stanford University", role: "professor", years: "2008–2017", kind: "university", certainty: 0.7, cites: [{source: S2, locator: "para. 4"}], how_known: "Simons."}
collaborators:
  - {value: "Curtis McMullen", relation: "teacher", note: "PhD advisor", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "IMU."}
  - {value: "Alex Eskin", relation: "collaborator", note: "rigidity theorem", certainty: 0.7, cites: [{source: S1, locator: "p. 3"}], how_known: "IMU."}

review:
  roster_status_reason: {value: "Provisional in v8 (F 3).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 206"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Worldview: no source."
    - "One lasting source (S4); span at 0.5."
  open_questions:
    - "A lasting source for the 2004 thesis results would restore 2004 (age 27) as an alternative."

sources:
  - id: S1
    type: secondary
    kind: "institutional page"
    author: "International Mathematical Union"
    citation: "International Mathematical Union. 'The Work of Maryam Mirzakhani.' Fields Medal 2014 news release. https://www.mathunion.org/fileadmin/IMU/Prizes/Fields/2014/news_release_mirzakhani.pdf"
    url: "https://www.mathunion.org/fileadmin/IMU/Prizes/Fields/2014/news_release_mirzakhani.pdf"
    accessed: 2026-10-19
    reliability_note: "Prize statement, read in full."
    used_for: [identity, basics, contribution, childhood, timing, institutions, collaborators]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "Thomas Sumner"
    citation: "Sumner, Thomas. 'Remembering the Life and Contributions of Fields Medalist Maryam Mirzakhani.' Simons Foundation, 20 July 2017. https://www.simonsfoundation.org/news/fields-medalist-maryam-mirzakhani-dies-at-40/"
    url: "https://www.simonsfoundation.org/news/fields-medalist-maryam-mirzakhani-dies-at-40/"
    accessed: 2026-10-19
    reliability_note: "Obituary, read in full."
    used_for: [identity, contribution, childhood, institutions]
  - id: S3
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [review]
  - id: S4
    type: secondary
    kind: "book chapter"
    author: "Jon Chaika; Barak Weiss"
    citation: "Chaika, Jon, and Barak Weiss. 'The horocycle flow on the moduli space of translation surfaces.' Proceedings of the International Congress of Mathematicians 2022, vol. 5, pp. 3412–3430. EMS Press. doi:10.4171/ICM2022/89"
    url: "https://ems.press/books/standalone/277/5520"
    accessed: 2026-10-19
    reliability_note: "Open-access survey, read in full; authors and wording verified."
    used_for: [basics, contribution, timing]
---

## Summary

Maryam Mirzakhani (1977–2017), mathematician [S1, S2]. Draft: worldview UNKNOWN. Not plotted.

## Life and work

Tehran; Harvard; Princeton; Stanford [S1, S2].

## Contribution and impact

Eskin–Mirzakhani 2013 [S1, S4].

## Childhood and education

Sharif; Harvard [S1, S2].

## Adult working worldview

None read.

## Heritage (context only)

Not stated.

## Timing

2013 (0.5), age 36 [S1, S4].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Lasting source for the thesis.

## Research log

- 2026-10-20: AA8 audit fix: ICM 2022 survey locator §2.2.
- 2026-10-19: Read IMU Fields statement; Simons obituary.
