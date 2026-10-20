---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z7)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z7 audit fix (P10): mid_basin false 0.5 -> BELOW_THRESHOLD; RQ-Z7-1 answered: A 3 at 0.5 holds (Franklin precedent)."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z7, order P32: F 3, rank 163). Basics from Britannica (Michael Ruse, signed). Own words: Psychology Today interview (1998) and Salon interview (2006), both after the span: 'a provisional deist is someone like myself who leaves it open'; 'I do feel confident that there is no intervention of a deity in the origin of life and humanity'; raised 'a devout Southern Baptist'. Scientist (P30). Span 1971–1975. primary_system DEISM (0.5, alt AGNOS); A 3 (0.5; alts 1 and BELOW_THRESHOLD): explicit denial of a personal, intervening God (P20), with at most an impersonal 'creative force'; B 3 (0.5, alt 4; P35, P16 addendum); C, D, E UNKNOWN; mid_basin false (0.5; A ≥ 3 branch). Plotted (A 3, B 3). Draft, not reviewed."}

identity:
  id: wilson-edward-o
  display_name: "E. O. Wilson"
  roster:
    canonical_name: "Edward O. Wilson"
    rank: 163
    F: 3
    models: [Claude, Gemini, GPT]
    band: "core (3–4)"
    status: "core"
    field: "biology"
    field_bucket: "biology / life science"
  full_name: {value: "Edward Osborne Wilson", certainty: 0.7, cites: [{source: S1, locator: "In full"}], how_known: "Britannica."}
  native_name: {value: "Edward O. Wilson", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  aliases:
    - {name: "E-O-Wilson", kind: "roster alias"}
    - {name: "E.O. Wilson", kind: "roster alias"}
    - {name: "Edward O- Wilson", kind: "roster alias"}
    - {name: "Wilson-Edward O-", kind: "roster alias"}

basics:
  birth:
    date: {value: "1929-06-10", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Birmingham, Alabama", modern_name: "Birmingham, Alabama, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "2021-12-26", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Burlington, Massachusetts", modern_name: "Burlington, Massachusetts, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1971, certainty: 0.5, cites: [{source: S1, locator: "body"}], how_known: "The Insect Societies (1971), 'his definitive work'; earlier pheromone and taxon-cycle work is undated in the body, so 0.5."}
  era_bucket: {value: "1950 on", certainty: 1.0, cites: [{source: S1, locator: "body"}], how_known: "1971 (P2)."}
  region_of_birth: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "USA (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "body"}], how_known: "Harvard."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Inferred."}
  occupations: {value: ["biologist", "entomologist", "professor"], certainty: 0.7, cites: [{source: S1, locator: "body"}], how_known: "Britannica."}

contribution:
  fields: {value: ["myrmecology", "sociobiology", "biodiversity"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "The Insect Societies", year: 1971, kind: "work", lasting: "'his definitive work on ants and other social insects' (S1)", certainty: 0.7, cites: [{source: S1, locator: "body"}], how_known: "Britannica."}
    - {value: "Sociobiology: The New Synthesis (kin-selection account of altruism)", year: 1975, kind: "theory", lasting: "founded sociobiology as its 'foremost proponent' (S1)", certainty: 0.7, cites: [{source: S1, locator: "body"}], how_known: "Britannica."}
  evidence_of_impact:
    - {value: "Crafoord Prize 1990; Pulitzer Prizes 1979 and 1991", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "body"}], how_known: "Britannica."}
  major_works:
    - {value: "On Human Nature", year: 1978, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "body"}], how_known: "Britannica."}
    - {value: "Consilience", year: 1998, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "body"}], how_known: "Britannica."}
  honours:
    - {value: "Crafoord Prize", year: 1990, certainty: 0.7, cites: [{source: S1, locator: "body"}], how_known: "Britannica."}
  definition_fit: {value: "clearly meets", rationale: "World authority on ants; founder of sociobiology (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "Southern Baptist (fundamentalist)", certainty: 0.7, cites: [{source: S3, locator: "'You grew up in a religious family?'"}], how_known: "(interview) 'I grew up as a Southern Baptist with strict adherence to the Bible'."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household: []
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling: []
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["English"], certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Inferred."}
  notable_events:
    - {value: "Childhood eye injury and adolescent partial deafness turned him from birds to insects", certainty: 0.7, cites: [{source: S1, locator: "body"}], how_known: "Britannica."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1971–1975", certainty: 0.5, cites: [{source: S1, locator: "body"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: 
    value: DEISM
    basis: recorded_interview
    certainty: 0.5
    cites: [{source: S2, locator: "'What do you mean by that?'"}, {source: S3, locator: "'I've heard you call yourself a deist'"}]
    how_known: "(interview) 1998 and 2006, after the span (P20), so 0.5."
    rationale: "Self-described 'provisional deist': 'a deist is a person who's willing to buy the idea that some creative force determined the parameters of the universe'; 'leaves it open'. Alternative AGNOS: he leaves the question open, though he rejects the label."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: DEISM, reason: "Coded: his own label."}
    - {code: AGNOS, reason: "Alternative: 'leaves it open'; he rejects the label."}
  lio_axes:
    A_locus: 
      value: 3
      basis: recorded_interview
      certainty: 0.5
      cites: [{source: S2, locator: "'You call yourself a deist'"}, {source: S3, locator: "'distinction between theism and deism'"}]
      how_known: "(interview) After the span (P20), 0.5."
      rationale: "Explicit denial of a personal, intervening God ('no intervention of a deity in the origin of life and humanity'; 'evolutionary biology leaves very little room for a theistic God'), scored under P20. What he leaves open is 'some creative force' or 'super-intelligent force', not a person, so 3. Alternatives: 1 (a deist creator, as the DEISM system); BELOW_THRESHOLD (open question)."
      alternatives:
        - {value: 1, note: "Deist creator read as a distant transcendent person.", cites: [{source: S2, locator: "'You call yourself a deist'"}]}
        - {value: BELOW_THRESHOLD, note: "The creator question left open.", cites: [{source: S3, locator: "'provisional'"}]}
    B_cause: 
      value: 3
      basis: inference_from_work
      certainty: 0.5
      cites: [{source: S1, locator: "body"}, {source: S3, locator: "'I do feel confident'"}]
      how_known: "Scientist (P30): working science, plus his statement of no divine intervention in life's origin; no stated no-exception claim for all nature (P35, P16 addendum)."
      rationale: "B 3 at 0.5 with 4 as the alternative (P35)."
      alternatives:
        - {value: 4, note: "P35 alternative.", cites: [{source: S1, locator: "body"}]}
    C_ledger: {value: UNKNOWN, how_known: "Not scored."}
    D_authority: {value: UNKNOWN, how_known: "Not scored."}
    E_scope: {value: UNKNOWN, how_known: "Not scored."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is at least 3 only at 0.5; P10 caps mid_basin by the certainty of the tested condition, below the 0.7 bar, so BELOW_THRESHOLD (Chomsky, Sen, Russell, Franklin precedents; Z7 audit)."}
  statements:
    - text: "I've been doing a kind of Pascalian waffling as a deist. I think being an atheist is to claim knowledge you cannot have. And to say you're agnostic is to arrogantly dismiss the whole thing by saying that it's unknowable. But a provisional deist is someone like myself who leaves it open. You see, evolutionary biology leaves very little room for a theistic God."
      cites: [{source: S2, locator: "'You call yourself a deist'"}]
      date: "1998-09"
      context: "Psychology Today interview; after the span."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
    - text: "But I do feel confident that there is no intervention of a deity in the origin of life and humanity."
      cites: [{source: S3, locator: "'I've heard you call yourself a deist'"}]
      date: "2006-03-21"
      context: "Salon interview; after the span."
      axes: [A_locus, B_cause]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
  changes_over_life:
    - {value: "Devout Southern Baptist in youth; converted by evolutionary biology at the University of Alabama", year: 1946, certainty: 0.5, cites: [{source: S3, locator: "'By the time you got to college'"}], how_known: "(interview); year from college entry, approximate."}
  coder_notes: "RQ-Z7-1 answered by the Z7 audit: A 3 at 0.5 holds (he leaves a remote creator open and refuses the atheist label; Franklin precedent; P38 does not apply), alternative 1 fair."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: "Southern Baptist", certainty: 0.7, cites: [{source: S3, locator: "'You grew up in a religious family?'"}], how_known: "(interview)."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1971–1975", certainty: 0.5, cites: [{source: S1, locator: "body"}], how_known: "The Insect Societies (1971) to Sociobiology (1975) (P29, P30); later works lie outside the core span by the coder's call."}
  age_at_first_lasting_contribution: {value: 42, certainty: 0.5, cites: [{source: S1, locator: "opening; body"}], how_known: "1971 − 1929 = 42 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: "c. 1946–1949 (conversion to evolution at university)", certainty: 0.5, cites: [{source: S3, locator: "'By the time you got to college'"}], how_known: "(interview)."}
  lio_views_relative_to_major_work: {value: "before major work", certainty: 0.5, cites: [{source: S3, locator: "'By the time you got to college'"}], how_known: "(interview)."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Field biology and taxonomy (S1).", certainty: 0.5, cites: [{source: S1, locator: "body"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "Harvard University", role: "professor; curator in entomology", years: "1956–1997", kind: "university", certainty: 0.7, cites: [{source: S1, locator: "body"}], how_known: "Britannica."}
collaborators:
  - {value: "W. L. Brown", relation: "collaborator", note: "character displacement", certainty: 0.7, cites: [{source: S1, locator: "body"}], how_known: "Britannica."}
  - {value: "Bert Hölldobler", relation: "collaborator", note: "The Ants (1990)", certainty: 0.7, cites: [{source: S1, locator: "body"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 163"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Own words only from interviews decades after the span (P20)."
  open_questions:
    - "Naturalist (1994) and On Human Nature (1978) first-hand on religion."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Michael Ruse"
    citation: "Ruse, Michael. 'E.O. Wilson.' Encyclopaedia Britannica (rev. 2026). https://www.britannica.com/biography/Edward-O-Wilson"
    url: "https://www.britannica.com/biography/Edward-O-Wilson"
    accessed: 2026-10-19
    reliability_note: "Signed article; body cited, Top Questions not used (P26)."
    used_for: [identity, basics, contribution, childhood, timing, lane_b, institutions, collaborators]
  - id: S2
    type: primary
    kind: "other"
    author: "E. O. Wilson, interviewed by Psychology Today"
    citation: "'E.O. Wilson Is on Top of the World.' Psychology Today (September 1998). https://www.psychologytoday.com/us/articles/199809/eo-wilson-is-on-top-of-the-world"
    url: "https://www.psychologytoday.com/us/articles/199809/eo-wilson-is-on-top-of-the-world"
    accessed: 2026-10-19
    reliability_note: "Published interview transcript (recorded_interview, P8)."
    used_for: [worldview]
  - id: S3
    type: primary
    kind: "other"
    author: "E. O. Wilson, interviewed by Steve Paulson"
    citation: "Paulson, Steve. '\"Religious belief itself is an adaptation\".' Salon (21 March 2006). https://www.salon.com/2006/03/21/wilson_19/"
    url: "https://www.salon.com/2006/03/21/wilson_19/"
    accessed: 2026-10-19
    reliability_note: "Published interview transcript (recorded_interview, P8)."
    used_for: [childhood, worldview, heritage, timing]
  - id: S4
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

E. O. Wilson (1929–2021), biologist [S1]. Draft: DEISM (0.5); A 3, B 3 at 0.5. Plotted.

## Life and work

Alabama; Harvard 1956–97 [S1].

## Contribution and impact

Insect Societies; Sociobiology; biodiversity [S1].

## Childhood and education

Southern Baptist upbringing [S3].

## Adult working worldview

Provisional deist; no intervening God [S2, S3].

## Heritage (context only)

Southern Baptist by birth [S3].

## Timing

1971–1975, age 42 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Naturalist first-hand.

## Research log

- 2026-10-19: Read Britannica (Ruse); Psychology Today and Salon interviews.
