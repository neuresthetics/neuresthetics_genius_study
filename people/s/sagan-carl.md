---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch O)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-17
  last_updated: 2026-10-17
  change_log:
    - {date: 2026-10-17, by: "Grok Bot", summary: "Record created (stage 3 batch O, order P32: F 4, rank 88). Basics from Britannica (Helge Kragh, signed; body only). Worldview from the 1981 U.S. Catholic interview ('God and Carl Sagan', 1 May 1981), read on the U.S. Catholic site. Scientist (P30: planetary atmospheres, nuclear winter). primary_system AGNOS (0.5, alt SECHUM); A BELOW_THRESHOLD (agnostic, no locus view, P20); B 3 (0.5, alt 4; P35); D 4 (0.5); mid_basin BELOW_THRESHOLD. Not plotted. Draft, not reviewed."}
    - {date: 2026-10-17, by: "Grok Bot", summary: "Batch O audit: A BELOW_THRESHOLD now also cites P38 (explicit suspension with no stated disbelief). Value unchanged."}

identity:
  id: sagan-carl
  display_name: "Carl Sagan"
  roster:
    canonical_name: "Carl Sagan"
    rank: 88
    F: 4
    models: [Claude, DeepSeek, GPT, Grok]
    band: "core (3–4)"
    status: core
    field: astronomy
    field_bucket: astronomy
  full_name: {value: "Carl Sagan", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica; middle name not read."}
  native_name: {value: UNKNOWN, how_known: "English."}
  aliases:
    - {name: "Carl-Sagan", kind: "roster alias"}

basics:
  birth:
    date: {value: "1934-11-09", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Brooklyn, New York, U.S.", modern_name: "Brooklyn, New York, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "1996-12-20", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Seattle, Washington", modern_name: "Seattle, Washington, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1977, certainty: 0.5, cites: [{source: S1, locator: "awards paragraph"}], how_known: "The Dragons of Eden, Pulitzer Prize for nonfiction 1978 (S1); 1977 is its publication year, not given in S1 (coder's inference from the 1978 prize; may be earlier). His research on planetary atmospheres is undated in the body (P39). The Cosmic Connection (1973) 'earned him prominence' but is not marked as lasting. Coder's pick (P13)."}
  era_bucket: {value: "1950 on", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "From 1977 (P2); every candidate year (1973–1983) gives the same bucket."}
  region_of_birth: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "United States (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Berkeley, Harvard, Cornell."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [English], certainty: 0.7, cites: [{source: S1, locator: "titles"}], how_known: "Britannica."}
  occupations: {value: ["astronomer", "science writer", "professor"], certainty: 0.7, cites: [{source: S1, locator: "opening; Cornell paragraph"}], how_known: "Britannica."}

contribution:
  fields: {value: ["planetary science", "astrobiology", "science popularization"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Research on planetary atmospheres (Venus, Jupiter) and prebiotic synthesis of amino and nucleic acids", year: UNKNOWN, kind: theory, lasting: "'Sagan did important research on planetary atmospheres, in astrobiology, and on the origin of life on Earth' (S1)", certainty: 0.7, cites: [{source: S1, locator: "early work paragraph; reputation paragraph"}], how_known: "Britannica; undated. A theory or result about natural systems, so he is a scientist (P30)."}
    - {value: "The Dragons of Eden", year: 1977, kind: work, lasting: "Pulitzer Prize for nonfiction, 1978 (S1)", certainty: 0.5, cites: [{source: S1, locator: "awards paragraph"}], how_known: "Britannica gives the prize year; the publication year is the coder's inference."}
    - {value: "Cosmos (television series and book, with Ann Druyan)", year: 1980, kind: work, lasting: "'the height of his public fame'; the book 'became a best seller' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Planetary Society paragraph"}], how_known: "Britannica."}
    - {value: "Nuclear winter (co-author of the paper introducing the concept)", year: 1983, kind: "concept or term", lasting: "'introduced the concept of \"nuclear winter\"' (S1)", certainty: 0.7, cites: [{source: S1, locator: "political paragraph"}], how_known: "Britannica."}
    - {value: "The Demon-Haunted World", year: 1996, kind: work, lasting: "'his last major book' (S1)", certainty: 0.5, cites: [{source: S1, locator: "pseudoscience paragraph"}], how_known: "Britannica; lasting status is the coder's reading; closes the period."}
  evidence_of_impact:
    - {value: "Pulitzer Prize (1978), NASA Distinguished Public Service Medal (1977, 1981), Ørsted Medal (1990), NAS Public Welfare Medal (1994)", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "awards paragraph"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "arguable", rationale: "Britannica says 'he made his reputation primarily as a spokesman for science and a popularizer of astronomy' (S1), though his research is called important.", certainty: 0.5, cites: [{source: S1, locator: "reputation paragraph"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
  parents_and_household: []
  household_circumstances: {value: TODO}
  schooling:
    - {value: "University of Chicago (B.A., M.A. physics 1955–56; Ph.D. astronomy and astrophysics 1960)", stage: university, years: "–1960", certainty: 0.7, cites: [{source: S1, locator: "education paragraph"}], how_known: "Britannica."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [English], certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1977–1996", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "'In my view, they nearly don't communicate at all'; science has 'a fair amount to say to religion mainly about the nature of evidence'", certainty: 0.7, cites: [{source: S2, locator: "science and religion exchange"}], how_known: "(interview) His own words (P8)."}
  primary_system:
    value: AGNOS
    basis: recorded_interview
    certainty: 0.5
    cites: [{source: S2, locator: "God and 'first cause' exchanges"}, {source: S1, locator: "religion sentence"}]
    rationale: "'An atheist is someone who is certain that God does not exist ... I know of no such compelling evidence'; 'I am extremely uncomfortable with dogmatic atheists ... I'm also uncomfortable with dogmatic believers'; 'If we don't know the answer, why are we under so much pressure to make up our minds' (1981). Britannica: 'he denied that he was an atheist' and 'wanted to replace [conventional religion] with a scientifically based belief system'. Named alternative: SECHUM."
    how_known: "(interview) One interview in the working years (0.7 ceiling); 0.5 because an alternative is named."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: AGNOS, reason: "Explicit suspension of judgement on God."}
    - {code: SECHUM, reason: "Britannica's 'scientifically based belief system'; no membership read."}
    - {code: ATHE, reason: "He denies being an atheist."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "(interview) An agnostic with no stated locus view gets A BELOW_THRESHOLD (P20), and explicit suspension with no stated disbelief stays BELOW_THRESHOLD (P38): 'I don't know of any compelling evidence for the old man in the sky', but 'a universe that does not exclude a traditional Western or Eastern god, but that does not require one either' (S2)."}
    B_cause:
      value: 3
      basis: inference_from_work
      certainty: 0.5
      cites: [{source: S1, locator: "early work paragraph; reputation paragraph"}]
      rationale: "Scored on his working science (P6, P30): research on planetary atmospheres and the origin of life. Working science alone gives B 3 at 0.5, alternative 4, never 4 (P35). The interview supports a lawful nature ('I can't imagine anyone denying the existence of the laws of nature') but states no exceptionless order (P40)."
      how_known: "Inferred from the working science (P24, P35)."
      alternatives:
        - {value: 4, note: "P35 alternative.", cites: [{source: S1, locator: "early work paragraph"}]}
    C_ledger: {value: UNKNOWN, how_known: "(interview) He would be 'delighted if there were a life after death' and calls near-death reports 'anecdotal'; nothing on reward or punishment."}
    D_authority:
      value: 4
      basis: recorded_interview
      certainty: 0.5
      cites: [{source: S2, locator: "science and religion exchange"}]
      rationale: "Evidence over authority: 'science has a fair amount to say to religion mainly about the nature of evidence. The idea of putting faith in an ancient argument from authority which is not to be questioned seems to me to have dire and dangerous implications'; 'I'm afraid religion doesn't throw away enough trust.'"
      how_known: "(interview) His own words; 0.5 because the remark mixes epistemic and political concerns."
    E_scope: {value: UNKNOWN, how_known: "Nothing read on the world's order as such (P7)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A is BELOW_THRESHOLD."}
  statements:
    - text: "Those who raise questions about the God hypothesis and the soul hypothesis are by no means all atheists. An atheist is someone who is certain that God does not exist, someone who has compelling evidence against the existence of God. I know of no such compelling evidence."
      cites: [{source: S2, locator: "reply to 'That seems to leave the question up in the air'"}]
      date: "1981-05-01"
      context: "Interview, U.S. Catholic, May 1981 (S2)."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-17
    - text: "We see a universe that does not exclude a traditional Western or Eastern god, but that does not require one either."
      cites: [{source: S2, locator: "reply to 'Where does God fit into this view?'"}]
      date: "1981-05-01"
      context: "Same interview."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-17
    - text: "I also think science has a fair amount to say to religion mainly about the nature of evidence. The idea of putting faith in an ancient argument from authority which is not to be questioned seems to me to have dire and dangerous implications for politics."
      cites: [{source: S2, locator: "science and religion exchange"}]
      date: "1981-05-01"
      context: "Same interview."
      axes: [D_authority]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-17
  changes_over_life: []
  coder_notes: "Coder's call. The often-quoted line 'if by God one means the set of physical laws that govern the universe, then clearly there is such a God' is attributed to U.S. News & World Report (1991) and was not read; the 1981 text read here has a different wording ('I can't imagine anyone denying the existence of the laws of nature'). Lead: The Varieties of Scientific Experience (Gifford Lectures, 1985)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "American", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1977–1996", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "First to last dated listed lasting contribution (P29, P30)."}
  age_at_first_lasting_contribution: {value: 43, certainty: 0.5, cites: [{source: S1, locator: "opening; 1977"}], how_known: "1977 − 1934 = 43 (P30)."}
  first_evidence_of_lio_type_views: {value: "1981: agnostic on God; evidence over authority", year: 1981, certainty: 0.5, cites: [{source: S2, locator: "interview"}], how_known: "Earlier writings not read for this (P30 #7)."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.5, cites: [{source: S2, locator: "interview"}], how_known: "1981, inside 1977–1996."}
  worldview_during_major_work: {value: "Agnostic on God; lawful nature; evidence over authority", certainty: 0.5, cites: [{source: S2, locator: "interview"}], how_known: "(interview) Coder's summary."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Not read for this.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Not read."}
  circle_present: {value: "unclear", rationale: "Agnostic.", certainty: 0.5, cites: [{source: S2, locator: "interview"}], how_known: "Coder's reading."}
  reading: "Agnostic; awe at a lawful cosmos."
  notes: ""

institutions:
  - {value: "Harvard University and Smithsonian Astrophysical Observatory", role: "researcher", years: "1962–1968", kind: university, certainty: 0.7, cites: [{source: S1, locator: "education paragraph"}], how_known: "Britannica."}
  - {value: "Cornell University (Laboratory for Planetary Studies)", role: "director; professor", years: "1968–1996", kind: university, certainty: 0.7, cites: [{source: S1, locator: "Cornell paragraph"}], how_known: "Britannica."}
  - {value: "The Planetary Society", role: "co-founder", years: "1980–", kind: other, certainty: 0.7, cites: [{source: S1, locator: "Planetary Society paragraph"}], how_known: "Britannica."}
collaborators:
  - {value: "Ann Druyan", relation: family, note: "wife; co-writer of Cosmos", certainty: 0.7, cites: [{source: S1, locator: "Planetary Society paragraph"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 88"}], how_known: "Study roster."}
  controversies:
    - {value: "Critics called his arguments against traditional religion simplistic", certainty: 0.7, cites: [{source: S1, locator: "religion sentence"}], how_known: "Britannica."}
  data_quality_flags: []
  open_questions:
    - "Read The Varieties of Scientific Experience (1985 lectures) and the 1991 U.S. News piece for a statement on law and exception (B) or on God's locus (A)."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Helge Kragh"
    citation: "Kragh, Helge. \"Carl Sagan.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Carl-Sagan. Read in Wayback snapshot 20261004211412."
    url: "https://www.britannica.com/biography/Carl-Sagan"
    accessed: 2026-10-17
    reliability_note: "Signed article. Body only; Top Questions not cited."
    used_for: [identity, basics, contribution, childhood, worldview, timing, institutions, collaborators, review]
  - id: S2
    type: primary
    kind: other
    author: "Carl Sagan (interviewed by U.S. Catholic)"
    citation: "\"God and Carl Sagan: Is the cosmos big enough for both of them?\" A U.S. Catholic interview, published 1 May 1981. https://uscatholic.org/articles/198105/god-and-carl-sagan-is-the-cosmos-big-enough-for-both-of-them/"
    url: "https://uscatholic.org/articles/198105/god-and-carl-sagan-is-the-cosmos-big-enough-for-both-of-them/"
    accessed: 2026-10-17
    reliability_note: "The publisher's own archive text of a question-and-answer interview, read directly (P8). The interviewer is not named on the page (Edward Wakin per secondary attributions)."
    used_for: [worldview, timing, lane_b]
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

# Carl Sagan

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Carl Sagan (1934–1996), American astronomer and science writer [S1]. Draft: primary_system AGNOS (0.5, alt SECHUM; interview); A BELOW_THRESHOLD (interview); B 3 at 0.5 (alt 4); D 4 at 0.5 (interview); mid_basin BELOW_THRESHOLD. Not plotted.

## Life and work

Chicago PhD 1960; Harvard, then Cornell from 1968 [S1].

## Contribution and impact

Planetary atmospheres, Cosmos (1980), nuclear winter (1983) [S1].

## Childhood and education

Not read.

## Adult working worldview

Agnostic on God; evidence over authority (1981) [S2].

## Heritage (context only)

American [S1].

## Timing

First lasting contribution 1977, at 43 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Agnostic [S2].

## Open questions

- Gifford Lectures (1985) for A and B.

## Research log

- 2026-10-17: Read Britannica (Kragh, Wayback 20261004211412) and the 1981 U.S. Catholic interview directly.
