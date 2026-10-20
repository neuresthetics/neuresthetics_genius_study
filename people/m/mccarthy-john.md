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
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA3, order P32: F 3, rank 190). Sources: Nils Nilsson's National Academy of Sciences Biographical Memoir (2012, read in full) and Stanford Computer Science's memorial notice. Lasting work: the term and field 'artificial intelligence', named in the Dartmouth proposal 'submitted to the Rockefeller Foundation in August 1955' (formal submission, P30 #1), and LISP, 'the language of choice for AI research', whose 1960 paper 'established the theoretical foundations'; span 1955–1960, age 28. Own words: his Stanford home page, 'I mention that I am indeed an atheist ... the evidence on the god question is in about the same state as the evidence on the werewolf question' (also quoted by Nilsson). Undated; the reference to Dawkins's 'come out' campaign places it decades after the span, so P20 caps it at 0.5. primary_system ATHE 0.5 (written_profession), alt AGNOS (he disclaims proof); A 4 at 0.5, alt BELOW_THRESHOLD; not a scientist as listed (P30, P33: a term, a programming language and logic-based AI are not testable claims about nature), B UNKNOWN, and scientist status is ruling question RQ-AA3-1 (not result-changing unless B is scored); C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD (P10). Not plotted. Draft, not reviewed."}

identity:
  id: mccarthy-john
  display_name: "John McCarthy"
  roster:
    canonical_name: "John McCarthy"
    rank: 190
    F: 3
    models: [Claude, DeepSeek, GPT]
    band: "core (3–4)"
    status: "core"
    field: "computer science"
    field_bucket: "computer science / AI"
  full_name: {value: "John McCarthy", certainty: 0.7, cites: [{source: S1, locator: "p. 3"}], how_known: "Nilsson."}
  native_name: {value: "John McCarthy", certainty: 0.7, cites: [{source: S1, locator: "p. 3"}], how_known: "Nilsson."}
  aliases:
    - {name: "John-McCarthy", kind: "roster alias"}

basics:
  birth:
    date: {value: "1927-09-04", certainty: 0.7, cites: [{source: S1, locator: "p. 3"}], how_known: "Nilsson."}
    place: {value: "Boston, Massachusetts", modern_name: "Boston, Massachusetts, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "p. 3"}], how_known: "Nilsson."}
  death:
    date: {value: "2011-10-24", certainty: 0.7, cites: [{source: S1, locator: "p. 1"}, {source: S2, locator: "para. 1"}], how_known: "Nilsson; Stanford."}
    place: {value: UNKNOWN, how_known: "Stanford's notice does not give the place; not stated in the sources read."}
  first_lasting_contribution_year: {value: 1955, certainty: 0.7, cites: [{source: S1, locator: "p. 5"}, {source: S2, locator: "para. 1"}], how_known: "The Dartmouth proposal naming 'artificial intelligence' was 'submitted to the Rockefeller Foundation in August 1955' (S1); 'coining that name in 1955' (S2); formal submission (P30 #1)."}
  era_bucket: {value: "1950 on", certainty: 1.0, cites: [{source: S1, locator: "p. 5"}], how_known: "1955–1960 (P2)."}
  region_of_birth: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "p. 3"}], how_known: "USA (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S2, locator: "para. 3"}], how_known: "Dartmouth, MIT, Stanford."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "English papers."}
  occupations: {value: ["computer scientist", "mathematician"], certainty: 0.7, cites: [{source: S2, locator: "para. 1, 3"}], how_known: "Stanford."}

contribution:
  fields: {value: ["artificial intelligence", "computer science"], certainty: 0.7, cites: [{source: S2, locator: "para. 1"}], how_known: "Stanford."}
  lasting_original_contributions:
    - {value: "The name and research programme 'artificial intelligence' (Dartmouth proposal)", year: 1955, kind: "concept or term", lasting: "'one of the founders of artificial intelligence (AI), coining that name in 1955' (S2); the proposal's definition and the field 'to which McCarthy devoted his scientific career' (S1)", certainty: 0.7, cites: [{source: S1, locator: "p. 5"}, {source: S2, locator: "para. 1"}], how_known: "Nilsson; Stanford; submitted August 1955."}
    - {value: "LISP", year: 1960, kind: "invention", lasting: "'LISP soon became the language of choice for AI research' (S1); 'became the language of choice for programming AI systems' (S2)", certainty: 0.7, cites: [{source: S1, locator: "p. 7"}, {source: S2, locator: "para. 1"}], how_known: "Designed from 1958; dated by the 1960 paper 'Recursive Functions of Symbolic Expressions and Their Computation by Machine, Part I' (publication, P30 #1)."}
  evidence_of_impact:
    - {value: "ACM Turing Award; National Medal of Science; Kyoto Prize", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S2, locator: "para. 4"}], how_known: "Stanford."}
  major_works:
    - {value: "Recursive Functions of Symbolic Expressions and Their Computation by Machine, Part I", year: 1960, kind: "paper or paper series", certainty: 0.7, cites: [{source: S1, locator: "p. 7"}], how_known: "Nilsson."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Founder and namer of the field of AI; LISP (S1, S2).", certainty: 0.7, cites: [{source: S2, locator: "para. 1"}], how_known: "Stanford."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Father John Patrick McCarthy, an Irish Catholic immigrant; mother Ida Glatt, a Lithuanian Jewish immigrant; both Communist Party members in the 1930s", role: "family", certainty: 0.7, cites: [{source: S1, locator: "p. 3"}], how_known: "Nilsson."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling:
    - {value: "Caltech (BS, mathematics); Princeton (PhD, mathematics)", certainty: 0.7, cites: [{source: S2, locator: "para. 3"}], how_known: "Stanford."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1955–1960", certainty: 0.7, cites: [{source: S1, locator: "p. 5, 7"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: 
    value: ATHE
    basis: written_profession
    certainty: 0.5
    cites: [{source: S3, locator: "closing paragraph"}, {source: S1, locator: "p. 21, n. 34"}]
    how_known: "His own home page; undated, but the Dawkins 'come out' reference places it decades after the span (P20 cap 0.5)."
    rationale: "'I mention that I am indeed an atheist' (S3). Alternative AGNOS: 'one need not claim to have a proof that no gods exist' (S3), though he judges the evidence like that for werewolves."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: ATHE, reason: "Coded at 0.5: self-described atheist."}
    - {code: AGNOS, reason: "Alternative: disclaims proof."}
  lio_axes:
    A_locus: 
      value: 4
      basis: written_profession
      certainty: 0.5
      cites: [{source: S3, locator: "closing paragraph"}]
      how_known: "His own words, after the span (P20 cap 0.5)."
      rationale: "Evidence for gods like that for werewolves (S3): no God, so 4. Alternative BELOW_THRESHOLD: the claim is about evidence, not a stated locus."
      alternatives:
        - {value: BELOW_THRESHOLD, note: "A claim about evidence, not a locus (S3).", cites: [{source: S3, locator: "closing paragraph"}]}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist as listed (P30, P33): naming a field, a programming language and logic-based AI make no testable claims about nature; no statement on nature read. Ruling question RQ-AA3-1."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "BELOW_THRESHOLD, not UNKNOWN: the A ≥ 3 branch reads A only (P10), and A 4 is scored only at 0.5."}
  statements:
    - text: "Responding to Richard Dawkins's pestering his fellow atheists to \"come out\", I mention that I am indeed an atheist. To count oneself as an atheist one need not claim to have a proof that no gods exist. One need merely think that the evidence on the god question is in about the same state as the evidence on the werewolf question."
      cites: [{source: S3, locator: "closing paragraph"}]
      context: "His Stanford home page, 'About John McCarthy'; undated, after the span (Dawkins's 'come out' campaign)."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "Read on his own page as maintained at Stanford; the same text is quoted by Nilsson (S1, n. 34). No date recorded (P12)."
  changes_over_life: []
  coder_notes: "Look for a dated version of the page (Internet Archive) to fix the year; check his essays on his site for statements on nature or mind."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Irish Catholic father, Lithuanian Jewish mother", certainty: 0.7, cites: [{source: S1, locator: "p. 3"}], how_known: "Nilsson."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1955–1960", certainty: 0.7, cites: [{source: S1, locator: "p. 5, 7"}], how_known: "From the 1955 proposal to the 1960 LISP paper, the listed lasting works (P29, P30 #1)."}
  age_at_first_lasting_contribution: {value: 28, certainty: 0.7, cites: [{source: S1, locator: "p. 3, 5"}], how_known: "1955 − 1927 = 28 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "Formal logic and recursive function theory (S1).", certainty: 0.5, cites: [{source: S1, locator: "p. 7"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "Stanford University", role: "professor; founder of the Stanford AI Laboratory", years: "1962–2011", kind: "university", certainty: 0.7, cites: [{source: S2, locator: "para. 3"}], how_known: "Stanford; end year his death."}
  - {value: "Massachusetts Institute of Technology", role: "faculty; co-founded the MIT AI Project", years: "1958–1962", kind: "university", certainty: 0.7, cites: [{source: S2, locator: "para. 3"}], how_known: "Stanford."}
collaborators:
  - {value: "Marvin Minsky", relation: "collaborator", note: "MIT AI Project", certainty: 0.7, cites: [{source: S2, locator: "para. 3"}], how_known: "Stanford."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 190"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Profession undated, after the span."
  open_questions:
    - "RQ-AA3-1 scientist status; date of the home page text."

sources:
  - id: S1
    type: secondary
    kind: "book chapter"
    author: "Nils J. Nilsson"
    citation: "Nilsson, Nils J. 'John McCarthy, 1927–2011.' Biographical Memoirs, National Academy of Sciences (2012). https://ai.stanford.edu/~nilsson/John_McCarthy.pdf"
    url: "https://ai.stanford.edu/~nilsson/John_McCarthy.pdf"
    accessed: 2026-10-19
    reliability_note: "Scholarly memoir by a colleague, read in full."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "Stanford University, Department of Computer Science"
    citation: "'Professor John McCarthy.' Stanford Computer Science, In Memoriam (October 2011). https://legacy.cs.stanford.edu/memoriam/professor-john-mccarthy"
    url: "https://legacy.cs.stanford.edu/memoriam/professor-john-mccarthy"
    accessed: 2026-10-19
    reliability_note: "Departmental memorial notice, read in full."
    used_for: [identity, basics, contribution, institutions, collaborators]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "John McCarthy"
    citation: "McCarthy, John. 'About John McCarthy.' Personal home page, Stanford University. https://www-formal.stanford.edu/jmc/personal.html"
    url: "https://www-formal.stanford.edu/jmc/personal.html"
    accessed: 2026-10-19
    reliability_note: "His own page on the university server, read in full; undated."
    used_for: [worldview]
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

John McCarthy (1927–2011), computer scientist [S1, S2]. Draft: ATHE (0.5); A 4 at 0.5; B UNKNOWN. Not plotted.

## Life and work

Boston; Los Angeles; MIT; Stanford [S1, S2].

## Contribution and impact

Artificial intelligence (1955); LISP (1960) [S1, S2].

## Childhood and education

Caltech; Princeton [S2].

## Adult working worldview

'I am indeed an atheist' (undated) [S3].

## Heritage (context only)

Irish Catholic and Lithuanian Jewish parents [S1].

## Timing

1955–1960, age 28 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Scientist status; date of the page.

## Research log

- 2026-10-19: Read Nilsson's memoir; Stanford notice; his home page.
