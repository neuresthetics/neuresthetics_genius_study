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
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA10, order P32: F 3, rank 220). Source: Britannica scholars edition, signed by Olin Jeuck Eggen (read in full). Lasting: his body of accurate naked-eye observations, 'the most accurate possible before the invention of the telescope', which 'paved the way for future discoveries'; 'What Tycho accomplished ... remains an outstanding accomplishment of the Renaissance'; with his data 'Kepler laid the groundwork for the work of Sir Isaac Newton' (S1). Dated from De nova stella (1573), the first published result of the programme, to his leaving Uraniborg (1597), where 'The major portion of Tycho's lifework ... had already been done'. Span 1573–1597 at 0.5 (alternative start 1576, the Ven grant), age 27. Scientist: B 3 at 0.5, alt 4 (P35). Worldview UNKNOWN. Not plotted. Draft, not reviewed."}

identity:
  id: brahe-tycho
  display_name: "Tycho Brahe"
  roster:
    canonical_name: "Tycho Brahe"
    rank: 220
    F: 3
    models: [Claude, DeepSeek, Gemini]
    band: "core (3–4)"
    status: "core"
    field: "astronomy"
    field_bucket: "astronomy"
  full_name: {value: "Tycho Brahe", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  native_name: {value: "Tycho Brahe", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  aliases: []

basics:
  birth:
    date: {value: "1546-12-14", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
    place: {value: "Knudstrup, Scania", modern_name: "Knudstrup, Scania (now in Sweden)", polity_then: "Kingdom of Denmark", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica: 'Knudstrup, Scania, Denmark'; Scania is now in Sweden (coder's note)."}
  death:
    date: {value: "1601-10-24", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
    place: {value: "Prague", modern_name: "Prague, Czech Republic", polity_then: "Kingdom of Bohemia (Holy Roman Empire)", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1573, certainty: 0.5, cites: [{source: S1, locator: "Youth and education"}], how_known: "'his publication of his observations of it in De nova stella in 1573' (S1): first public statement of the observing programme (P30). 0.5: the lasting claim is for the whole body of observations; alternative 1576 (Uraniborg)."}
  era_bucket: {value: "1400 to 1599", certainty: 1.0, cites: [{source: S1, locator: "Youth and education"}], how_known: "1573 (P2); the 1576 alternative is in the same bucket."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Scania (now Sweden; then Denmark): Northern Europe either way (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "Mature career"}], how_known: "Ven (Uraniborg), where the span took place (AA6 rule)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Latin"], certainty: 0.5, cites: [{source: S1, locator: "Youth and education"}], how_known: "Coder's reading: De nova stella (Latin title)."}
  occupations: {value: ["astronomer", "instrument maker"], certainty: 0.7, cites: [{source: S1, locator: "Introduction; Mature career"}], how_known: "Britannica."}

contribution:
  fields: {value: ["astronomy"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Body of naked-eye astronomical observations (new star of 1572 beyond the Moon; comet of 1577 beyond the Moon; positions of more than 777 fixed stars; planetary observations used by Kepler)", year: 1573, kind: "body of work", lasting: "'paved the way for future discoveries'; 'remains an outstanding accomplishment of the Renaissance'; with those data 'Kepler laid the groundwork for the work of Sir Isaac Newton' (S1)", certainty: 0.5, cites: [{source: S1, locator: "Introduction; Youth and education; Mature career"}], how_known: "From De nova stella (1573) through Uraniborg (1576–1597) (S1); 0.5 on the start year."}
  evidence_of_impact:
    - {value: "Kepler built on his data", kind: "institutional or technological lineage", certainty: 0.7, cites: [{source: S1, locator: "Mature career"}], how_known: "Britannica."}
  major_works:
    - {value: "De nova stella", year: 1573, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "Youth and education"}], how_known: "Britannica."}
    - {value: "Geo-heliocentric (Tychonic) system", year: UNKNOWN, kind: "other", certainty: 0.7, cites: [{source: S1, locator: "Mature career"}], how_known: "Britannica; undated; not lasting."}
  honours:
    - {value: "Island of Ven and observatory funding from Frederick II", year: 1576, certainty: 0.7, cites: [{source: S1, locator: "Mature career"}], how_known: "Britannica."}
  definition_fit: {value: "clearly meets", rationale: "Most accurate pre-telescope observations; Kepler's data (S1).", certainty: 0.7, cites: [{source: S1, locator: "Mature career"}], how_known: "Britannica."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Father a privy councillor and governor of Helsingborg castle; raised by his childless uncle Jørgen at Tostrup", role: "family", certainty: 0.7, cites: [{source: S1, locator: "Youth and education"}], how_known: "Britannica."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling:
    - {value: "Universities of Copenhagen (law, 1559–62) and Leipzig (1562–65); then Wittenberg, Rostock, Basel, Augsburg", certainty: 0.7, cites: [{source: S1, locator: "Youth and education"}], how_known: "Britannica."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1573–1597", certainty: 0.5, cites: [{source: S1, locator: "Youth and education; Mature career"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: {value: UNKNOWN, how_known: "No own words on belief read in S1."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered: []
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing first-hand read (P19)."}
    B_cause: 
      value: 3
      basis: inference_from_work
      certainty: 0.5
      cites: [{source: S1, locator: "Mature career"}]
      how_known: "Scientist (P30). B from working science with no statement of their own on law and exception, so 3 at 0.5, alternative 4, never 4 (P35)."
      rationale: "Systematic measurement of celestial positions to correct the tables; the new star and comet placed beyond the Moon (S1): lawful nature in his science. Alternative 4."
      alternatives:
        - {value: 4, note: "Working science cannot tell lawful-with-exceptions from exceptionless (P35).", cites: [{source: S1, locator: "Mature career"}]}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, so the P4 test cannot be applied (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "Leads: Thoren, The Lord of Uraniborg (1990); Christianson, On Tycho's Island (2000). S1 says he was 'at odds with ... king, church, and nobility' when he left Ven; that is about his duties, not belief."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated in S1."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1573–1597", certainty: 0.5, cites: [{source: S1, locator: "Youth and education; Mature career"}], how_known: "De nova stella (1573) to leaving Uraniborg (1597), where 'the major portion' of the lifework was done (P29, P30); 0.5 following the item. Alternatives 1576–1597 and 1573–1601 (data left at death)."}
  age_at_first_lasting_contribution: {value: 27, certainty: 0.5, cites: [{source: S1, locator: "Introduction; Youth and education"}], how_known: "1573 − 1546 = 27 (P30 year difference); alternative 30 (1576)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Observational astronomy (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "Uraniborg observatory, Ven", role: "founder and director", years: "1576–1597", kind: "research institute", certainty: 0.7, cites: [{source: S1, locator: "Mature career"}], how_known: "Britannica."}
  - {value: "Court of Emperor Rudolf II, Prague", role: "imperial patronage", years: "1599–1601", kind: "patron or funder", certainty: 0.7, cites: [{source: S1, locator: "Mature career"}], how_known: "Britannica."}
collaborators:
  - {value: "Johannes Kepler", relation: "student or assistant", note: "pupil and assistant in his final years; inherited the data", certainty: 0.7, cites: [{source: S1, locator: "Mature career"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 220"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Worldview: no source."
    - "Span start 1573 vs 1576."
  open_questions:
    - "Own words on belief (Thoren 1990; correspondence)."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Olin Jeuck Eggen"
    citation: "Eggen, Olin Jeuck. 'Tycho Brahe.' Encyclopaedia Britannica (scholars edition). https://kids.britannica.com/scholars/article/Tycho-Brahe/16148"
    url: "https://kids.britannica.com/scholars/article/Tycho-Brahe/16148"
    accessed: 2026-10-19
    reliability_note: "Signed article, scholars edition, read in full."
    used_for: [identity, basics, contribution, childhood, timing, institutions, collaborators]
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

Tycho Brahe (1546–1601), Danish astronomer [S1]. Draft: worldview UNKNOWN. Not plotted.

## Life and work

Scania; Copenhagen; Leipzig; Ven; Prague [S1].

## Contribution and impact

Observations 1573–1597 [S1].

## Childhood and education

Copenhagen; Leipzig [S1].

## Adult working worldview

None read.

## Heritage (context only)

Not stated.

## Timing

1573–1597, age 27 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Own words.

## Research log

- 2026-10-20: Read Britannica (Eggen, scholars edition).
