---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z9)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z9 audit (RQ-Z9-1, v8's call on the auditor's advice): not a scientist as listed; B stays UNKNOWN, not plotted. Leads added: prize motivation 'discoveries and inventions'; interview 'theory' and 'for discovering how the brain worked'."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z9, order P32: F 3, rank 171). Basics from NobelPrize.org facts (Physics 2024). Own words: Nobel Prize interview, 6 December 2024 (NobelPrize.org transcript), after the span: parents 'both atheists'; at his Christian school belief in God 'seemed to me it was just obvious nonsense, and it turns out I was right'; 'other people also don't believe in God'. primary_system ATHE (0.5, alt AGNOS); A 4 (0.5, alts BELOW_THRESHOLD and 3; P20, Chomsky and Kahneman precedents). Not a scientist as listed: the Boltzmann machine is called an 'invention' (S1; P33; Hassabis precedent), so B UNKNOWN pending RQ-Z9-1. C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD (A ≥ 3 only at 0.5, P10). Span 1983–1985, age 36. Not plotted (no B). Draft, not reviewed."}

identity:
  id: hinton-geoffrey
  display_name: "Geoffrey Hinton"
  roster:
    canonical_name: "Geoffrey Hinton"
    rank: 171
    F: 3
    models: [Claude, DeepSeek, GPT]
    band: "core (3–4)"
    status: "provisional"
    field: "computer science"
    field_bucket: "computer science / AI"
  full_name: {value: "Geoffrey Hinton", certainty: 0.7, cites: [{source: S1, locator: "heading"}], how_known: "NobelPrize.org."}
  native_name: {value: "Geoffrey Hinton", certainty: 0.7, cites: [{source: S1, locator: "heading"}], how_known: "NobelPrize.org."}
  aliases:
    - {name: "Geoffrey-Hinton", kind: "roster alias"}

basics:
  birth:
    date: {value: "1947-12-06", certainty: 0.7, cites: [{source: S1, locator: "Born"}], how_known: "NobelPrize.org."}
    place: {value: "London", modern_name: "London, United Kingdom", polity_then: "United Kingdom", certainty: 0.7, cites: [{source: S1, locator: "Born"}], how_known: "NobelPrize.org."}
  death:
    date: {value: UNKNOWN, how_known: "Living (not stated as dead in the sources read)."}
    place: {value: UNKNOWN, how_known: "Living."}
  first_lasting_contribution_year: {value: 1983, certainty: 0.7, cites: [{source: S1, locator: "Work"}], how_known: "Boltzmann machine, 1983–1985 (range start, P12)."}
  era_bucket: {value: "1950 on", certainty: 1.0, cites: [{source: S1, locator: "Work"}], how_known: "1983 (P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "Born"}], how_known: "UK (P3)."}
  region_of_work: {value: "North America", certainty: 0.5, cites: [{source: S1, locator: "Affiliation"}], how_known: "Toronto at the award; place of the 1983–85 work not stated in the source read, so 0.5."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Inferred."}
  occupations: {value: ["computer scientist", "professor"], certainty: 0.7, cites: [{source: S1, locator: "Affiliation"}], how_known: "NobelPrize.org."}

contribution:
  fields: {value: ["machine learning", "artificial neural networks"], certainty: 0.7, cites: [{source: S1, locator: "Prize motivation"}], how_known: "NobelPrize.org."}
  lasting_original_contributions:
    - {value: "Boltzmann machine", year: 1983, kind: "invention", lasting: "'The invention became significant, for example, for classifying and creating images' (S1); Nobel Prize 2024", certainty: 0.7, cites: [{source: S1, locator: "Work"}], how_known: "NobelPrize.org: 'In 1983–1985, Geoffrey Hinton used tools from statistical physics to create the Boltzmann machine'."}
  evidence_of_impact:
    - {value: "Nobel Prize in Physics 2024 'for foundational discoveries and inventions that enable machine learning with artificial neural networks'", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "Prize motivation"}], how_known: "NobelPrize.org."}
  major_works: []
  honours:
    - {value: "Nobel Prize in Physics", year: 2024, certainty: 0.7, cites: [{source: S1, locator: "heading"}], how_known: "NobelPrize.org."}
  definition_fit: {value: "clearly meets", rationale: "Foundational work on neural-network learning (S1).", certainty: 0.7, cites: [{source: S1, locator: "Prize motivation"}], how_known: "NobelPrize.org."}

childhood:
  family_religion: {value: "Atheist parents", certainty: 0.7, cites: [{source: S2, locator: "'What personal qualities are important'"}], how_known: "(interview) 'my parents who were both atheists'."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household: []
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling:
    - {value: "Christian private school, from age seven", stage: "other", years: "1954–", certainty: 0.5, cites: [{source: S2, locator: "'What personal qualities are important'"}], how_known: "(interview); start year from his age.", run_by: "religious body"}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1983–1985", certainty: 0.7, cites: [{source: S1, locator: "Work"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: 
    value: ATHE
    basis: recorded_interview
    certainty: 0.5
    cites: [{source: S2, locator: "'What personal qualities are important'"}]
    how_known: "(interview) 2024, after the span (P20), so 0.5."
    rationale: "Stated non-belief: belief in God 'seemed to me it was just obvious nonsense, and it turns out I was right'; 'other people also don't believe in God'. Alternative AGNOS (no general claim beyond his schoolfellows' belief)."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: ATHE, reason: "Coded at 0.5."}
    - {code: AGNOS, reason: "Alternative."}
  lio_axes:
    A_locus: 
      value: 4
      basis: recorded_interview
      certainty: 0.5
      cites: [{source: S2, locator: "'What personal qualities are important'"}]
      how_known: "(interview) 2024, after the span; P20 cap 0.5."
      rationale: "Stated disbelief in God scored as A 4, as Chomsky and Kahneman (P20, P38). Alternatives BELOW_THRESHOLD (no locus view as such) and 3."
      alternatives:
        - {value: BELOW_THRESHOLD, note: "Disbelief without a locus view.", cites: [{source: S2, locator: "'What personal qualities are important'"}]}
        - {value: 3, note: "Denies only the schoolroom God.", cites: [{source: S2, locator: "'What personal qualities are important'"}]}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist as listed: the Boltzmann machine is called an 'invention' (S1); P33 and the Hassabis precedent. No own statement on nature read (P16). RQ-Z9-1 answered (v8's call on the auditor's advice): not a scientist as listed, so B stays UNKNOWN and he does not plot. Leads only: the prize motivation names 'discoveries and inventions' (S1), and in the interview he calls the Boltzmann machine a 'theory' built as a machine 'for discovering how the brain worked' (S2); neither puts a theory on the lasting list (P35 addendum). Were one listed, B would be 3 at 0.5 (P35) and he would plot, faded, at A 4 / B 3."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is at least 3 only at 0.5; P10 caps mid_basin by the certainty of the tested condition, below the 0.7 bar, so BELOW_THRESHOLD."}
  statements:
    - text: "One was my parents who were both atheists sent me to a Christian school, a Christian private school, from the age of seven. Everybody at the school believed in God. The teachers believed in God and the other kids believed in God. It seemed to me it was just obvious nonsense, and it turns out I was right."
      cites: [{source: S2, locator: "'What personal qualities are important'"}]
      date: "2024-12-06"
      context: "Nobel Prize interview, Stockholm; after the span."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
  changes_over_life: []
  coder_notes: "RQ-Z9-1 answered no (Z9 audit; Hassabis, Knuth, Tao precedents): the Boltzmann machine is an invention (P33), and Nobel's 'inspired by the structure of the brain' is not a testable claim about organisms. Leads: 'discoveries and inventions' (prize motivation, S1); 'theory' and 'for discovering how the brain worked' (interview, S2). A listed theory (e.g. backpropagation, 1986, if a source called it a lasting theory of learning in brains) would change this. Backpropagation (1986) was not in the source read."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: "None (atheist parents)", certainty: 0.7, cites: [{source: S2, locator: "'What personal qualities are important'"}], how_known: "(interview)."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1983–1985", certainty: 0.7, cites: [{source: S1, locator: "Work"}], how_known: "Boltzmann machine, 1983–1985 (P29, P30)."}
  age_at_first_lasting_contribution: {value: 36, certainty: 0.7, cites: [{source: S1, locator: "Born; Work"}], how_known: "1983 − 1947 = 36 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: "c. 1954 onward (disbelief at his Christian school from age seven)", certainty: 0.5, cites: [{source: S2, locator: "'What personal qualities are important'"}], how_known: "(interview)."}
  lio_views_relative_to_major_work: {value: "before major work", certainty: 0.5, cites: [{source: S2, locator: "'What personal qualities are important'"}], how_known: "(interview)."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Statistical learning models (S1).", certainty: 0.5, cites: [{source: S1, locator: "Work"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "University of Toronto", role: "professor", years: UNKNOWN, kind: "university", certainty: 0.7, cites: [{source: S1, locator: "Affiliation"}], how_known: "NobelPrize.org (affiliation at the award)."}
collaborators:
  - {value: "John J. Hopfield", relation: "other", note: "co-laureate 2024", certainty: 0.7, cites: [{source: S1, locator: "heading"}], how_known: "NobelPrize.org."}

review:
  roster_status_reason: {value: "Provisional in v8 (F 3).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 171"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Own words from one interview long after the span."
  open_questions:
    - "RQ-Z9-1 scientist status; backpropagation sources."

sources:
  - id: S1
    type: tertiary
    kind: "institutional page"
    author: "Nobel Prize Outreach"
    citation: "'Geoffrey Hinton – Facts – 2024.' NobelPrize.org. https://www.nobelprize.org/prizes/physics/2024/hinton/facts/"
    url: "https://www.nobelprize.org/prizes/physics/2024/hinton/facts/"
    accessed: 2026-10-19
    reliability_note: "Official prize facts page."
    used_for: [identity, basics, contribution, timing, lane_b, institutions, collaborators]
  - id: S2
    type: primary
    kind: "other"
    author: "Geoffrey Hinton, interviewed for NobelPrize.org"
    citation: "'Transcript from an interview with Geoffrey Hinton.' NobelPrize.org (recorded 6 December 2024). https://www.nobelprize.org/prizes/physics/2024/hinton/1925103-interview-transcript/"
    url: "https://www.nobelprize.org/prizes/physics/2024/hinton/1925103-interview-transcript/"
    accessed: 2026-10-19
    reliability_note: "Official interview transcript (recorded_interview, P8)."
    used_for: [childhood, worldview, heritage, timing]
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

Geoffrey Hinton (b. 1947), computer scientist [S1]. Draft: ATHE (0.5); A 4 (0.5); B UNKNOWN (not a scientist, RQ-Z9-1). Not plotted.

## Life and work

London; Toronto [S1].

## Contribution and impact

Boltzmann machine; neural-network learning [S1].

## Childhood and education

Atheist parents; Christian school [S2].

## Adult working worldview

Belief in God 'obvious nonsense' [S2].

## Heritage (context only)

None religious [S2].

## Timing

1983–1985, age 36 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- RQ-Z9-1.

## Research log

- 2026-10-19: Read NobelPrize.org facts and interview transcript.
