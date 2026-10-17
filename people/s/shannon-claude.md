---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch O)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-17
  last_updated: 2026-10-17
  change_log:
    - {date: 2026-10-17, by: "Grok Bot", summary: "Record created (stage 3 batch O, order P32: F 4, rank 89). Basics from Britannica (George Markowsky, signed; body only). Worldview from Anthony Liversidge's interview (Omni, August 1987), read in the version printed in Shannon's Collected Papers (IEEE Press, 1993; PDF on gwern.net). primary_system ATHE (0.7); A 4 (0.7); B 3 (0.5, alt 4; P41); mid_basin false (0.7). Plotted (faded on B). Draft, not reviewed."}

identity:
  id: shannon-claude
  display_name: "Claude Shannon"
  roster:
    canonical_name: "Claude Shannon"
    rank: 89
    F: 4
    models: [Claude, DeepSeek, Gemini, GPT]
    band: "core (3–4)"
    status: core
    field: mathematics
    field_bucket: mathematics
  full_name: {value: "Claude Elwood Shannon", certainty: 0.7, cites: [{source: S2, locator: "profile, opening"}], how_known: "Liversidge's profile; Britannica body gives 'Claude Shannon'."}
  native_name: {value: UNKNOWN, how_known: "English."}
  aliases:
    - {name: "Claude-Shannon", kind: "roster alias"}
    - {name: "Shannon-Claude", kind: "roster alias"}

basics:
  birth:
    date: {value: "1916-04-30", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Petoskey, Michigan, U.S.", modern_name: "Petoskey, Michigan, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "2001-02-24", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Medford, Massachusetts", modern_name: "Medford, Massachusetts, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1940, certainty: 0.7, cites: [{source: S1, locator: "master's thesis paragraph"}], how_known: "A Symbolic Analysis of Relay and Switching Circuits (1940), 'called one of the most significant master's theses of the 20th century' (S1)."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S1, locator: "master's thesis paragraph"}], how_known: "From 1940 (P2); 1948 gives the same bucket."}
  region_of_birth: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "United States (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Bell Labs, MIT."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [English], certainty: 0.7, cites: [{source: S1, locator: "titles"}], how_known: "Britannica."}
  occupations: {value: ["mathematician", "electrical engineer", "professor"], certainty: 0.7, cites: [{source: S1, locator: "opening; MIT sentence"}], how_known: "Britannica."}

contribution:
  fields: {value: ["information theory", "switching theory", "cryptography"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Boolean algebra as the theory of relay and switching circuits (A Symbolic Analysis of Relay and Switching Circuits)", year: 1940, kind: theory, lasting: "'established the theoretical underpinnings of digital circuits' (S1)", certainty: 0.7, cites: [{source: S1, locator: "master's thesis paragraph"}], how_known: "Britannica. A theory about physical circuits, so he is counted a scientist (P30, coder's call)."}
    - {value: "Information theory ('A Mathematical Theory of Communication')", year: 1948, kind: theory, lasting: "'his framework and terminology are still used' (S1)", certainty: 0.7, cites: [{source: S1, locator: "1948 paragraph"}], how_known: "Britannica."}
  evidence_of_impact:
    - {value: "Framework and terminology of information theory 'still used'; applied in cognition, biology, linguistics, psychology, economics and physics", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "1948 paragraphs"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
  parents_and_household: []
  household_circumstances: {value: TODO}
  schooling:
    - {value: "University of Michigan (B.S. mathematics and electrical engineering, 1936); MIT (S.M., Ph.D., 1940)", stage: university, years: "–1940", certainty: 0.7, cites: [{source: S1, locator: "education paragraph"}], how_known: "Britannica."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [English], certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1940–1948", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "Information theory is not 'a substitute for belief in a God': 'I certainly would not!'", certainty: 0.7, cites: [{source: S2, locator: "interview, religion exchange"}], how_known: "(interview) His own words (P8)."}
  primary_system:
    value: ATHE
    basis: recorded_interview
    certainty: 0.7
    cites: [{source: S2, locator: "interview, Wiener question"}]
    rationale: "'I am an atheist to begin with. I believe in evolutionary theory and that we are basically machines, but a very complex type ... A natural device. I see no God involved or anything like that.' Both halves of the ATHE label are stated: no God, and humans as natural devices."
    how_known: "(interview) One interview, his own words, 0.7 ceiling (P8); no plausible alternative named."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: ATHE, reason: "Self-described atheist; humans 'a natural device'."}
    - {code: DETERM, reason: "'basically machines' is about humans, not a general determinism."}
  lio_axes:
    A_locus:
      value: 4
      basis: recorded_interview
      certainty: 0.7
      cites: [{source: S2, locator: "interview, Wiener question"}]
      rationale: "No God (P38): 'I am an atheist to begin with ... I see no God involved or anything like that'; 'I don't happen to be a religious man'."
      how_known: "(interview) One interview, his own words (P8)."
    B_cause:
      value: 3
      basis: recorded_interview
      certainty: 0.5
      cites: [{source: S2, locator: "interview, Wiener question"}]
      rationale: "Account of nature (P6): humans are 'basically machines', 'A natural device', with 'no God involved' and evolution accepted. That denies intervention in human nature but states no exceptionless order (P40), so B 3 at 0.5, alternative 4 (P41). As a scientist (P30) his working science alone would give the same (P35)."
      how_known: "(interview) P41 cap."
      alternatives:
        - {value: 4, note: "P41/P35 alternative: no stated exceptionless law.", cites: [{source: S2, locator: "interview, Wiener question"}]}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read."}
    D_authority: {value: UNKNOWN, how_known: "Nothing read."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7)."}
  mid_basin: {value: false, certainty: 0.7, cites: [{source: S2, locator: "interview, Wiener question"}], how_known: "(interview) A 4 at 0.7: the A ≥ 3 branch reads A only (P10)."}
  statements:
    - text: "That's a heavily loaded question! Let me say this. I am an atheist to begin with. I believe in evolutionary theory and that we are basically machines, but a very complex type, far more so than any machine man has made yet. So in a way that's both a Yes and a No. We are kind of an extreme case of mechanical device - by mechanical I don't mean just metals are involved, of course, gears and so on. A natural device. I see no God involved or anything like that."
      cites: [{source: S2, locator: "interview, Wiener question"}]
      date: "1987"
      context: "Reply to whether he agrees with Norbert Wiener that there is no basic distinction between man and machine; Liversidge interview, Omni, August 1987, as printed in the Collected Papers (S2)."
      axes: [A_locus, B_cause]
      kind: "recorded interview"
      verified_against: "scholarly edition"
      verified_on: 2026-10-17
      note: "S2 says the Omni text appeared 'in a slightly different form'; a second wording ('I'm an atheist to begin with ... I see no God involved') circulates for the Omni version (seen in search text only). Both deny God."
    - text: "I don't happen to be a religious man and I don't think it would help if I were! OMNI: You wouldn't want to say information theory is a substitute for belief in a God? Shannon: I certainly would not!"
      cites: [{source: S2, locator: "interview, religion exchange"}]
      date: "1987"
      context: "Same interview."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "scholarly edition"
      verified_on: 2026-10-17
  changes_over_life: []
  coder_notes: "Coder's call. The interview (1987) is well after the working years (1940–1948), so the scores describe his later view; nothing earlier was read. Counting switching theory as a theory about physical systems (P30) is the coder's call; B is the same either way."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "American", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1940–1948", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "First to last listed lasting contribution (P29, P30)."}
  age_at_first_lasting_contribution: {value: 24, certainty: 0.7, cites: [{source: S1, locator: "opening; 1940"}], how_known: "1940 − 1916 = 24 (P30)."}
  first_evidence_of_lio_type_views: {value: "1987: atheist; humans 'a natural device'", year: 1987, certainty: 0.5, cites: [{source: S2, locator: "interview"}], how_known: "Only the 1987 interview read (P30 #7)."}
  lio_views_relative_to_major_work: {value: "after major work", certainty: 0.5, cites: [{source: S2, locator: "interview"}], how_known: "1987, after 1948; earlier writings not read."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Nothing read from 1940–1948."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Not read for this.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Not read."}
  circle_present: {value: "no", rationale: "'I see no God involved'.", certainty: 0.5, cites: [{source: S2, locator: "interview"}], how_known: "Coder's reading."}
  reading: "Atheist; humans as natural machines."
  notes: ""

institutions:
  - {value: "Bell Telephone Laboratories", role: "mathematician (research)", years: "1941–1972", kind: "research institute", certainty: 0.7, cites: [{source: S1, locator: "Bell Labs sentences"}], how_known: "Britannica."}
  - {value: "Massachusetts Institute of Technology", role: "professor", years: "1956–1978", kind: university, certainty: 0.7, cites: [{source: S1, locator: "MIT sentence"}], how_known: "Britannica (visiting 1956, faculty 1958, emeritus 1978)."}
collaborators:
  - {value: "Vannevar Bush", relation: "mentor or employer", note: "differential analyzer at MIT", certainty: 0.7, cites: [{source: S1, locator: "education paragraph"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 89"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Interview read in the Collected Papers version; the Omni text differs slightly."
  open_questions:
    - "Compare with the Omni (August 1987) printed text."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "George Markowsky"
    citation: "Markowsky, George. \"Claude Shannon.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Claude-Shannon. Read in Wayback snapshot 20261011204843."
    url: "https://www.britannica.com/biography/Claude-Shannon"
    accessed: 2026-10-17
    reliability_note: "Signed article. Body only; Top Questions not cited."
    used_for: [identity, basics, contribution, childhood, timing, institutions, collaborators]
  - id: S2
    type: primary
    kind: "scholarly edition"
    author: "Anthony Liversidge"
    citation: "Liversidge, Anthony. \"Profile of Claude Shannon.\" In Claude Elwood Shannon: Collected Papers, ed. N. J. A. Sloane and A. D. Wyner (New York: IEEE Press, 1993), pp. xix ff.; first in Omni, August 1987. PDF: https://gwern.net/doc/cs/algorithm/information/1987-liversidge.pdf"
    url: "https://gwern.net/doc/cs/algorithm/information/1987-liversidge.pdf"
    accessed: 2026-10-17
    reliability_note: "Scan of the Collected Papers printing, read directly; question-and-answer interview in his own words (P8)."
    used_for: [identity, worldview, timing, lane_b]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-17
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Claude Shannon

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Claude Shannon (1916–2001), American mathematician and electrical engineer, founder of information theory [S1]. Draft: primary_system ATHE (0.7, interview); A 4 at 0.7 (interview); B 3 at 0.5 (alt 4; interview); mid_basin false (0.7). Plotted (faded).

## Life and work

Michigan, MIT; Bell Labs 1941–72; MIT faculty from 1956 [S1].

## Contribution and impact

Switching-circuit theory (1940) and information theory (1948) [S1].

## Childhood and education

Not read.

## Adult working worldview

'I am an atheist to begin with' (1987) [S2].

## Heritage (context only)

American [S1].

## Timing

First lasting contribution 1940, at 24 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No circle [S2].

## Open questions

- Omni text comparison.

## Research log

- 2026-10-17: Read Britannica (Markowsky, Wayback 20261011204843) and the Liversidge profile (Collected Papers scan) directly.
