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
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z7 audit fix (P10): mid_basin false 0.5 -> BELOW_THRESHOLD; A 4 is only at 0.5, under the 0.7 bar."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z6 audit fixes (blind audit at 85859f0, run 1; Z6-21, Z6-22 FAIL; v8's call on the auditor's advice): 'I remember very precisely the moment at which I stopped believing in God' is stated non-belief, not suspension (P38 reasoning; CODING_GUIDE §1), so primary_system AGNOS -> ATHE 0.5, alt AGNOS; A BELOW_THRESHOLD -> 4 at 0.5, alts BELOW_THRESHOLD and 3 (P20 explicit denial of a God that cares; Chomsky, Penrose, Sen precedents); mid_basin BELOW_THRESHOLD -> false at 0.5 (A 4 >= 3). Raskin page dated 2022-03-01 (page metadata datePublished), as Chomsky's in Z2. Now plotted, faded, at A 4 / B 3."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z6, order P32: F 3, rank 158). Basics from his Nobel autobiography (2002). Own voice: interview with Max Raskin (undated web page; after the span): never religious as an adult; lost his faith at about 15: 'maybe I could believe in God, but I could not believe in a God that cared whether or not I masturbate ... if I can't imagine God caring about me, then we were irrelevant to each other, and it really didn't matter whether he existed or not'; no afterlife; 'There's nothing mystical'. A scientist (P30, P35 addendum: experimental claims about human judgment, as Skinner). Span 1974–1979. primary_system AGNOS (0.5, alt BELOW_THRESHOLD); A BELOW_THRESHOLD; B 3 (0.5, alt 4; P35); C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD. Not plotted (no A). Draft, not reviewed."}

identity:
  id: kahneman-daniel
  display_name: "Daniel Kahneman"
  roster:
    canonical_name: "Daniel Kahneman"
    rank: 158
    F: 3
    models: [Claude, DeepSeek, GPT]
    band: "core (3–4)"
    status: "core"
    field: "psychology"
    field_bucket: "psychology / neuroscience"
  full_name: {value: "Daniel Kahneman", certainty: 0.7, cites: [{source: S1, locator: "Early years"}], how_known: "Nobel autobiography."}
  native_name: {value: "Daniel Kahneman", certainty: 0.7, cites: [{source: S1, locator: "Early years"}], how_known: "Nobel autobiography."}
  aliases:
    - {name: "Daniel-Kahneman", kind: "roster alias"}

basics:
  birth:
    date: {value: "1934", certainty: 0.7, cites: [{source: S1, locator: "Early years"}], how_known: "His own words: 'born in Tel Aviv ... in 1934'."}
    place: {value: "Tel Aviv", modern_name: "Tel Aviv, Israel", polity_then: "Mandatory Palestine", certainty: 0.7, cites: [{source: S1, locator: "Early years"}], how_known: "Nobel autobiography (family domiciled in Paris)."}
  death:
    date: {value: UNKNOWN, how_known: "Not in the sources read."}
    place: {value: UNKNOWN, how_known: "Not in the sources read."}
  first_lasting_contribution_year: {value: 1974, certainty: 0.7, cites: [{source: S1, locator: "references"}], how_known: "Tversky and Kahneman, 'Judgment under uncertainty: Heuristics and biases', Science (1974)."}
  era_bucket: {value: "1950 on", certainty: 1.0, cites: [{source: S1, locator: "references"}], how_known: "1974 (P2)."}
  region_of_birth: {value: "Middle East and North Africa", certainty: 0.7, cites: [{source: S1, locator: "Early years"}], how_known: "Israel (P3; regions.csv)."}
  region_of_work: {value: "Middle East and North Africa", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Hebrew University and the Van Leer Institute, Jerusalem, for most of 1974–78; then North America, so 0.5."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English", "Hebrew"], certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Inferred."}
  occupations: {value: ["psychologist", "professor"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Nobel autobiography."}

contribution:
  fields: {value: ["psychology of judgment and decision-making", "behavioral economics"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Nobel autobiography."}
  lasting_original_contributions:
    - {value: "Heuristics and biases (with Amos Tversky)", year: 1974, kind: theory, lasting: "Nobel Prize 2002 (S1)", certainty: 0.7, cites: [{source: S1, locator: "references; text"}], how_known: "Nobel autobiography."}
    - {value: "Prospect theory (with Amos Tversky)", year: 1979, kind: theory, lasting: "'prospect theory undoubtedly afforded some legitimacy' to behavioral economics (S1)", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Nobel autobiography (Kahneman and Tversky, 1979)."}
  evidence_of_impact:
    - {value: "Nobel Memorial Prize in Economic Sciences 2002", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "heading"}], how_known: "NobelPrize.org."}
  major_works: []
  honours:
    - {value: "Nobel Memorial Prize in Economic Sciences", year: 2002, certainty: 0.7, cites: [{source: S1, locator: "heading"}], how_known: "NobelPrize.org."}
  definition_fit: {value: "clearly meets", rationale: "Founded the heuristics-and-biases programme and prospect theory (S1).", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Nobel."}

childhood:
  family_religion: {value: "Jewish (Lithuanian Jews in Paris); mother's family moderately religious", certainty: 0.7, cites: [{source: S1, locator: "Early years"}, {source: S2, locator: "Rabbi Kahaneman"}], how_known: "Nobel autobiography; (interview)."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated beyond a moderately religious maternal family."}
  parents_and_household:
    - {value: "Father, chief of research at a chemical factory", role: father, certainty: 0.7, cites: [{source: S1, locator: "Early years"}], how_known: "Nobel autobiography."}
    - {value: "Rabbi Kahaneman of the Ponevezh Yeshiva, paternal uncle", role: other, certainty: 0.7, cites: [{source: S2, locator: "Rabbi Kahaneman"}], how_known: "(interview)."}
  household_circumstances: {value: "Jewish family in occupied France 1940–44; emigrated to Palestine 1946", certainty: 0.7, cites: [{source: S1, locator: "Early years"}, {source: S2, locator: "Rabbi Kahaneman"}], how_known: "Nobel autobiography; interview."}
  schooling:
    - {value: "Religious school, Jerusalem and Tel Aviv", stage: "elementary school", run_by: "religious body", years: "1946–1949", certainty: 0.5, cites: [{source: S2, locator: "Rabbi Kahaneman"}], how_known: "(interview); years approximate."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["French", "Hebrew"], certainty: 0.5, cites: [{source: S1, locator: "Early years"}], how_known: "Inferred."}
  notable_events:
    - {value: "Lost his religious faith at about 15", year: 1949, certainty: 0.5, cites: [{source: S2, locator: "Rabbi Kahaneman"}], how_known: "(interview); year from his age."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1974–1979", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: 
    value: ATHE
    basis: recorded_interview
    certainty: 0.5
    cites: [{source: S2, locator: "Rabbi Kahaneman"}]
    how_known: "(interview) 2022; After the span, so capped at 0.5 (P20). Stated non-belief: 'I remember very precisely the moment at which I stopped believing in God'; never religious as an adult; no afterlife; 'There's nothing mystical'."
    rationale: "ATHE: stated non-belief is more than suspension (P38 reasoning; AGNOS is explicit suspension, CODING_GUIDE §1). v8's call on the auditor's advice (Z6 audit, Z6-21). Alternative AGNOS: 'maybe I could believe in God'; 'it really didn't matter whether he existed or not'."
    alternatives:
      - {value: AGNOS, note: "'maybe I could believe in God ... it really didn't matter whether he existed or not' read as suspension.", cites: [{source: S2, locator: "Rabbi Kahaneman"}]}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: ATHE, reason: "Coded at 0.5: 'stopped believing in God' (Z6 audit)."}
    - {code: AGNOS, reason: "Alternative: 'maybe I could believe in God'; existence 'didn't matter'."}
  lio_axes:
    A_locus:
      value: 4
      basis: recorded_interview
      certainty: 0.5
      cites: [{source: S2, locator: "Rabbi Kahaneman"}]
      how_known: "(interview) 2022; Explicit denial of a personal, intervening God is scored (CODING_GUIDE §6, P20): 'I could not believe in a God that cared'; 'I stopped believing in God'. The retrospective covers his whole adult life, span included; after the span, so 0.5."
      rationale: "By analogy with P38 and the Sen, Chomsky and Penrose precedents. v8's call on the auditor's advice (Z6 audit, Z6-22)."
      alternatives:
        - {value: BELOW_THRESHOLD, note: "Indifference ('irrelevant to each other') rather than a locus view.", cites: [{source: S2, locator: "Rabbi Kahaneman"}]}
        - {value: 3, note: "Denies only a caring God ('maybe I could believe in God').", cites: [{source: S2, locator: "Rabbi Kahaneman"}]}
    B_cause: 
      value: 3
      basis: inference_from_work
      certainty: 0.5
      cites: [{source: S1, locator: "text"}]
      how_known: "A scientist with working science (P30; P35 addendum: testable claims about human judgment, experiments published in Science), so B 3 at 0.5, alternative 4 (P35)."
      rationale: "P35."
      alternatives:
        - {value: 4, note: "P35 alternative.", cites: [{source: S1, locator: "text"}]}
    C_ledger: {value: UNKNOWN, how_known: "'Do you believe in an afterlife? No.' (interview) not scored (coder's call)."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is at least 3 only at 0.5; P10 caps mid_basin by the certainty of the tested condition, below the 0.7 bar, so BELOW_THRESHOLD (Chomsky, Sen, Russell, Franklin precedents; Z7 audit)."}
  statements:
    - text: "I was walking home, and I had the insight that maybe I could believe in God, but I could not believe in a God that cared whether or not I masturbate. That was a very sudden insight. That if I can't imagine God caring about me, then we were irrelevant to each other, and it really didn't matter whether he existed or not. And that was the end of the religion for me."
      cites: [{source: S2, locator: "Rabbi Kahaneman"}]
      context: "Interview with Max Raskin; recalling age about 15; after the span."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "Page dated 2022-03-01 (page metadata)."
  changes_over_life: []
  coder_notes: "Psychology counts as science here under the P35 addendum (Skinner); flag if the auditor reads him as social science."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Lithuanian Jewish", certainty: 0.7, cites: [{source: S1, locator: "Early years"}], how_known: "Nobel autobiography."}
  religious_heritage_by_birth: {value: "Jewish", certainty: 0.7, cites: [{source: S1, locator: "Early years"}], how_known: "Nobel autobiography."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1974–1979", certainty: 0.7, cites: [{source: S1, locator: "text; references"}], how_known: "Heuristics and biases (1974) to prospect theory (1979) (P29, P30)."}
  age_at_first_lasting_contribution: {value: 40, certainty: 0.7, cites: [{source: S1, locator: "Early years; references"}], how_known: "1974 − 1934 = 40 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: "c. 1949 (loss of faith at about 15)", certainty: 0.5, cites: [{source: S2, locator: "Rabbi Kahaneman"}], how_known: "(interview)."}
  lio_views_relative_to_major_work: {value: "before major work", certainty: 0.5, cites: [{source: S2, locator: "Rabbi Kahaneman"}], how_known: "(interview)."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Experimental psychology (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "Hebrew University of Jerusalem", role: professor, years: "1961–1978", kind: university, certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Nobel autobiography; years approximate."}
collaborators:
  - {value: "Amos Tversky", relation: collaborator, note: "heuristics and biases; prospect theory", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Nobel autobiography."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 158"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Only own words on religion are a 2022 interview after the span."
  open_questions:
    - "Death date from a tertiary source."

sources:
  - id: S1
    type: primary
    kind: "published work by the subject"
    author: "Daniel Kahneman"
    citation: "Kahneman, Daniel. 'Biographical.' NobelPrize.org (2002). https://www.nobelprize.org/prizes/economic-sciences/2002/kahneman/biographical/"
    url: "https://www.nobelprize.org/prizes/economic-sciences/2002/kahneman/biographical/"
    accessed: 2026-10-19
    reliability_note: "His own Nobel autobiography."
    used_for: [identity, basics, contribution, childhood, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: primary
    kind: "other"
    author: "Daniel Kahneman, interviewed by Max Raskin"
    citation: "Raskin, Max. 'Interview with Daniel Kahneman.' maxraskin.com (2022-03-01). https://www.maxraskin.com/interviews/daniel-kahneman"
    url: "https://www.maxraskin.com/interviews/daniel-kahneman"
    accessed: 2026-10-19
    reliability_note: "Published interview transcript (recorded_interview, P8); dated 2022-03-01 in the page metadata (datePublished)."
    used_for: [childhood, worldview, timing]
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

Daniel Kahneman (b. 1934), psychologist [S1]. Draft: ATHE (0.5, alt AGNOS); A 4 (0.5); B 3 (0.5, alt 4). Plotted, faded.

## Life and work

Paris, occupied France, Jerusalem, North America [S1].

## Contribution and impact

Heuristics and biases; prospect theory [S1].

## Childhood and education

Religious schooling; faith lost at 15 [S2].

## Adult working worldview

Stopped believing in God at about 15 [S2].

## Heritage (context only)

Lithuanian Jewish [S1].

## Timing

1974–1979, age 40 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Death date.

## Research log

- 2026-10-19: Read Nobel autobiography; Raskin interview.
- 2026-10-19: Z6 audit fixes: ATHE, A 4; Raskin page date from metadata.
