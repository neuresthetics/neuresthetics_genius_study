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
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA3, order P32: F 3, rank 188). Source: Britannica, signed by Robert Simpson and Karl Geiringer (scholars edition, read in full). Lasting work: Ein deutsches Requiem, 'still considered one of the most significant works of 19th-century choral music'; dated by its 'first performance at Bremen on Good Friday, 1868' (premiere, P30 #1). That Bremen performance is commonly said to have lacked the fifth movement, added for the complete Leipzig performance of 1869 (coder's knowledge, not in the source read); under RQ-Z8-1 an incomplete premiere dates only what was played, so 0.5 with 1869 as the alternative. Worldview: no own words read. Britannica calls the Requiem 'a large, objective, nonreligious humane vision' and his 'essential quality is perhaps stoicism', describing the music, not a profession. primary_system UNKNOWN (leads SECHUM, CHRIST: biblical texts 'selected by the composer'); A UNKNOWN; not a scientist; C, D, E UNKNOWN; mid_basin UNKNOWN. Span 1868, age 35. Not plotted. Draft, not reviewed."}

identity:
  id: brahms-johannes
  display_name: "Johannes Brahms"
  roster:
    canonical_name: "Johannes Brahms"
    rank: 188
    F: 3
    models: [Claude, DeepSeek, Grok]
    band: "core (3–4)"
    status: "core"
    field: "music"
    field_bucket: "music"
  full_name: {value: "Johannes Brahms", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  native_name: {value: "Johannes Brahms", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  aliases: []

basics:
  birth:
    date: {value: "1833-05-07", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
    place: {value: "Hamburg", modern_name: "Hamburg, Germany", polity_then: "Free City of Hamburg (German Confederation)", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  death:
    date: {value: "1897-04-03", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
    place: {value: "Vienna", modern_name: "Vienna, Austria", polity_then: "Austria-Hungary", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1868, certainty: 0.5, cites: [{source: S1, locator: "The young pianist and music director"}], how_known: "'first performance at Bremen on Good Friday, 1868' (S1); premiere (P30 #1). 0.5 because the Bremen performance is reported to have lacked the fifth movement (RQ-Z8-1: an incomplete premiere dates only the part played); alternative 1869, the complete performance (not in the source read)."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "The young pianist and music director"}], how_known: "1868 or 1869, one bucket (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Germany (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "The young pianist and music director"}], how_known: "Vienna from 1863."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["German"], certainty: 0.7, cites: [{source: S1, locator: "The young pianist and music director"}], how_known: "German texts."}
  occupations: {value: ["composer", "pianist", "conductor"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}

contribution:
  fields: {value: ["music"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Ein deutsches Requiem (A German Requiem)", year: 1868, kind: "work", lasting: "'still considered one of the most significant works of 19th-century choral music' (S1)", certainty: 0.5, cites: [{source: S1, locator: "The young pianist and music director"}], how_known: "Britannica; premiere Bremen, Good Friday 1868 (0.5, see first-lasting year)."}
  evidence_of_impact:
    - {value: "'The great master of symphonic and sonata style in the second half of the 19th century'; the 'three great Bs'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "Introduction; Maturity and fame"}], how_known: "Britannica."}
  major_works:
    - {value: "Symphony No. 1 in C Minor", year: 1876, kind: "composition", certainty: 0.7, cites: [{source: S1, locator: "Maturity and fame"}], how_known: "Britannica: 'completed in 1876 and first heard in the same year'; not called lasting."}
    - {value: "Symphony No. 4 in E Minor", year: 1885, kind: "composition", certainty: 0.5, cites: [{source: S1, locator: "Maturity and fame"}], how_known: "Britannica: 1884–85; premiere year not given."}
  honours:
    - {value: "Honorary degree, University of Breslau", year: 1879, kind: "award", certainty: 0.7, cites: [{source: S1, locator: "Maturity and fame"}], how_known: "Britannica."}
  definition_fit: {value: "clearly meets", rationale: "The great master of symphonic and sonata style in the second half of the 19th century (S1).", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Son of Jakob Brahms, an impecunious horn and double bass player", role: "father", certainty: 0.7, cites: [{source: S1, locator: "The young pianist and music director"}], how_known: "Britannica."}
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
  working_years: {value: "1868", certainty: 0.5, cites: [{source: S1, locator: "The young pianist and music director"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: {value: UNKNOWN, how_known: "No own words read. Britannica: the Requiem, 'based on biblical texts selected by the composer', expresses 'a large, objective, nonreligious humane vision'; 'his essential quality is perhaps stoicism' (S1). These describe the music, not a profession. Leads SECHUM and CHRIST."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: SECHUM, reason: "Lead: 'nonreligious humane vision' (S1, of the Requiem)."}
    - {code: CHRIST, reason: "Lead: biblical texts chosen by him; Four Serious Songs (1896) (S1)."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing first-hand read (P19)."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30); no statement on nature read."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, so the P4 test cannot be applied (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "Read his letters on the Requiem texts (to Carl Reinthaler, 1867) and Musgrave's A Brahms Reader; check the 1868 Bremen programme (fifth movement) against a source."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated in the source read."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1868", certainty: 0.5, cites: [{source: S1, locator: "The young pianist and music director"}], how_known: "The one listed lasting work, dated by its premiere (P29, P30 #1); alternative 1869."}
  age_at_first_lasting_contribution: {value: 35, certainty: 0.5, cites: [{source: S1, locator: "Introduction; The young pianist and music director"}], how_known: "1868 − 1833 = 35 (P30 year difference); 36 on the 1869 alternative."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Musical architecture, not geometric argument (S1).", certainty: 0.5, cites: [{source: S1, locator: "Aims and achievements"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "Gesellschaft der Musikfreunde, Vienna", role: "principal conductor", years: "1872–1875", kind: "employer", certainty: 0.7, cites: [{source: S1, locator: "The young pianist and music director; Maturity and fame"}], how_known: "Britannica."}
collaborators:
  - {value: "Robert Schumann", relation: "mentor or employer", note: "1853 article launched him", certainty: 0.7, cites: [{source: S1, locator: "The young pianist and music director"}], how_known: "Britannica."}
  - {value: "Joseph Joachim", relation: "collaborator", note: "violinist", certainty: 0.7, cites: [{source: S1, locator: "The young pianist and music director"}], how_known: "Britannica."}
  - {value: "Clara Schumann", relation: "collaborator", note: "lifelong friend", certainty: 0.7, cites: [{source: S1, locator: "The young pianist and music director"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 188"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Premiere may have been incomplete (RQ-Z8-1)."
  open_questions:
    - "Requiem letters; Bremen programme."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Robert Simpson and Karl Geiringer"
    citation: "Simpson, Robert, and Karl Geiringer. 'Johannes Brahms.' Encyclopaedia Britannica (scholars edition). https://kids.britannica.com/scholars/article/Johannes-Brahms/16167"
    url: "https://kids.britannica.com/scholars/article/Johannes-Brahms/16167"
    accessed: 2026-10-19
    reliability_note: "Signed article, read in full."
    used_for: [identity, basics, contribution, childhood, worldview, timing, institutions, collaborators]
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

Johannes Brahms (1833–1897), composer [S1]. Draft: UNKNOWN (leads SECHUM, CHRIST). Not plotted.

## Life and work

Hamburg; Vienna [S1].

## Contribution and impact

A German Requiem, 1868 [S1].

## Childhood and education

Piano with Cossel and Marxsen [S1].

## Adult working worldview

None read.

## Heritage (context only)

Not stated.

## Timing

1868, age 35 (0.5) [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Requiem letters.

## Research log

- 2026-10-19: Read Britannica (Simpson, Geiringer).
