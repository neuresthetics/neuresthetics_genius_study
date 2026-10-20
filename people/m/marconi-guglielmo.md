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
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z10, order P32: F 3, rank 176). Basics from NobelPrize.org (biographical, Les Prix Nobel 1909). Own words: his public address opening Vatican Radio, 12 February 1931 (Vatican Radio's own history page, archived; English translation of the Italian), after the span: 'With the help of Almighty God, who allows the many mysterious forces of nature to be used by man'. Not a scientist: wireless telegraphy is an invention (P33). primary_system CHRIST (0.5, alt BELOW_THRESHOLD: ceremonial words); A 1 (0.5, alts 0 and BELOW_THRESHOLD); B UNKNOWN (no statement on law or exception, P16); C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD (A ≤ 1 only at 0.5, B UNKNOWN). Span 1896–1900, age 22. Not plotted (no B). Draft, not reviewed."}

identity:
  id: marconi-guglielmo
  display_name: "Guglielmo Marconi"
  roster:
    canonical_name: "Guglielmo Marconi"
    rank: 176
    F: 3
    models: [Claude, DeepSeek, Gemini]
    band: "core (3–4)"
    status: "core"
    field: "invention"
    field_bucket: "invention / engineering"
  full_name: {value: "Guglielmo Marconi", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "NobelPrize.org."}
  native_name: {value: "Guglielmo Marconi", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "NobelPrize.org."}
  aliases:
    - {name: "Marconi-Guglielmo", kind: "roster alias"}

basics:
  birth:
    date: {value: "1874-04-25", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "NobelPrize.org."}
    place: {value: "Bologna", modern_name: "Bologna, Italy", polity_then: "Kingdom of Italy", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "NobelPrize.org."}
  death:
    date: {value: "1937-07-20", certainty: 0.7, cites: [{source: S1, locator: "closing"}], how_known: "NobelPrize.org."}
    place: {value: "Rome", modern_name: "Rome, Italy", polity_then: "Kingdom of Italy", certainty: 0.7, cites: [{source: S1, locator: "closing"}], how_known: "NobelPrize.org."}
  first_lasting_contribution_year: {value: 1896, certainty: 0.7, cites: [{source: S1, locator: "para. 1"}], how_known: "'the world's first patent for a system of wireless telegraphy' (1896); the patent is the dating event."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "para. 1"}], how_known: "1896 (P2)."}
  region_of_birth: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Italy (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "para. 1"}], how_known: "England from 1896."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Italian", "English"], certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Inferred."}
  occupations: {value: ["inventor", "electrical engineer", "businessman", "senator"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "NobelPrize.org."}

contribution:
  fields: {value: ["wireless telegraphy", "radio"], certainty: 0.7, cites: [{source: S1, locator: "para. 1"}], how_known: "NobelPrize.org."}
  lasting_original_contributions:
    - {value: "System of wireless telegraphy", year: 1896, kind: "invention", lasting: "Nobel Prize in Physics 1909 for it (S1); 'the world's first patent for a system of wireless telegraphy'", certainty: 0.7, cites: [{source: S1, locator: "para. 1; honours"}], how_known: "NobelPrize.org; patent 1896."}
    - {value: "Tuned (syntonic) telegraphy, patent No. 7777", year: 1900, kind: "invention", lasting: "'his famous patent No. 7777' (S1)", certainty: 0.5, cites: [{source: S1, locator: "para. 1"}], how_known: "NobelPrize.org; 'famous' read as lasting, the coder's call."}
  evidence_of_impact:
    - {value: "Nobel Prize in Physics 1909 (with Braun)", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "honours"}], how_known: "NobelPrize.org."}
  major_works:
    - {value: "First transatlantic wireless signals, Poldhu to St John's", year: 1901, kind: "other", certainty: 0.7, cites: [{source: S1, locator: "para. 1"}], how_known: "NobelPrize.org."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Pioneer of wireless telegraphy (S1).", certainty: 0.7, cites: [{source: S1, locator: "para. 1"}], how_known: "NobelPrize.org."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Giuseppe Marconi, Italian country gentleman", role: "father", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "NobelPrize.org."}
    - {value: "Annie Jameson, of Daphne Castle, County Wexford", role: "mother", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "NobelPrize.org."}
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
  working_years: {value: "1896–1900", certainty: 0.7, cites: [{source: S1, locator: "para. 1"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: 
    value: CHRIST
    basis: written_profession
    certainty: 0.5
    cites: [{source: S2, locator: "Marconi's address"}]
    how_known: "Public broadcast address, 12 February 1931, after the span (P20), so 0.5; text from Vatican Radio's own page (the institution's copy, RQ-Z8-2), in English translation of the Italian; audio not checked."
    rationale: "Introduces the Pope to 'the Faithful of all the world' and credits 'Almighty God'; kneels and kisses the papal ring (S2, narrative). Alternative BELOW_THRESHOLD: ceremonial words at a papal event, no doctrine stated."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Coded at 0.5: public address at Vatican Radio."}
  lio_axes:
    A_locus: 
      value: 1
      basis: written_profession
      certainty: 0.5
      cites: [{source: S2, locator: "Marconi's address"}]
      how_known: "1931 address, after the span (P20); one sentence, so 0.5."
      rationale: "'Almighty God, who allows the many mysterious forces of nature to be used by man': a God distinct from nature who governs its forces, 1. Alternative 0 (fully transcendent personal God) and BELOW_THRESHOLD (ceremonial)."
      alternatives:
        - {value: 0, note: "Fully transcendent, personal.", cites: [{source: S2, locator: "Marconi's address"}]}
        - {value: BELOW_THRESHOLD, note: "Ceremonial formula.", cites: [{source: S2, locator: "Marconi's address"}]}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P33: wireless telegraphy is an invention). 'mysterious forces of nature' says nothing on law or exception (P16)."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus ≤ 1 only at 0.5 and B_cause UNKNOWN; P10 caps mid_basin below the 0.7 bar."}
  statements:
    - text: "With the help of Almighty God, who allows the many mysterious forces of nature to be used by man, I have been able to prepare this instrument which will accord to the Faithful of all the world the consolation of hearing the voice of the Holy Father."
      cites: [{source: S2, locator: "Marconi's address"}]
      date: "1931-02-12"
      context: "Inauguration of Vatican Radio; after the span."
      axes: [A_locus]
      kind: "other"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "Public broadcast address; English text as given by Vatican Radio itself (archived page), translated from the Italian. Audio and Italian original not checked."
  changes_over_life: []
  coder_notes: "Check the Italian original (Vatican Radio or L'Osservatore Romano, 13 February 1931); his 1937 statements on faith and the annulment of his first marriage (1927) are further leads."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated in the sources read (Italian father, Irish mother)."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1896–1900", certainty: 0.7, cites: [{source: S1, locator: "para. 1"}], how_known: "First wireless patent (1896) to patent No. 7777 (1900) (P29, P30)."}
  age_at_first_lasting_contribution: {value: 22, certainty: 0.7, cites: [{source: S1, locator: "opening; para. 1"}], how_known: "1896 − 1874 = 22 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Experimental engineering (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "Wireless Telegraph & Signal Company (Marconi's Wireless Telegraph Company)", role: "founder", years: "1897–1937", kind: "commercial", certainty: 0.5, cites: [{source: S1, locator: "para. 1"}], how_known: "NobelPrize.org; end year his death, coder's estimate."}
collaborators:
  - {value: "William Preece", relation: "mentor or employer", note: "Post Office engineer-in-chief", certainty: 0.7, cites: [{source: S1, locator: "para. 1"}], how_known: "NobelPrize.org."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 176"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "One ceremonial public sentence, after the span."
  open_questions:
    - "Italian original of the 1931 address."

sources:
  - id: S1
    type: tertiary
    kind: "institutional page"
    author: "Nobel Foundation"
    citation: "'Guglielmo Marconi – Biographical.' NobelPrize.org (from Les Prix Nobel, 1909; Nobel Lectures, Physics 1901–1921). https://www.nobelprize.org/prizes/physics/1909/marconi/biographical/"
    url: "https://www.nobelprize.org/prizes/physics/1909/marconi/biographical/"
    accessed: 2026-10-19
    reliability_note: "Biography written at the time of the award."
    used_for: [identity, basics, contribution, childhood, timing, lane_b, institutions, collaborators]
  - id: S2
    type: primary
    kind: "institutional page"
    author: "Guglielmo Marconi (Vatican Radio)"
    citation: "Vatican Radio. 'Our history' (with Marconi's address of 12 February 1931). Archived 2013-04-30. https://web.archive.org/web/20130430073929/http://en.radiovaticana.va/chisiamo_9.asp"
    url: "https://web.archive.org/web/20130430073929/http://en.radiovaticana.va/chisiamo_9.asp"
    accessed: 2026-10-19
    reliability_note: "The broadcasting institution's own text of the address, in English translation; seen in search excerpt of the archived page."
    used_for: [worldview]
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

Guglielmo Marconi (1874–1937), inventor of wireless telegraphy [S1]. Draft: CHRIST (0.5); A 1 (0.5); B UNKNOWN. Not plotted.

## Life and work

Bologna; England [S1].

## Contribution and impact

Wireless telegraphy [S1].

## Childhood and education

Privately educated [S1].

## Adult working worldview

'With the help of Almighty God' (1931) [S2].

## Heritage (context only)

Not stated.

## Timing

1896–1900, age 22 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Italian original.

## Research log

- 2026-10-19: Read NobelPrize.org biography; Vatican Radio history page.
