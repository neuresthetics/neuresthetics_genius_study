---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch N)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-17
  last_updated: 2026-10-17
  change_log:
    - {date: 2026-10-17, by: "Grok Bot", summary: "Record created (stage 3 batch N, order P32: F 4, rank 86). Basics from Britannica (Britannica Editors, unsigned; body only). Worldview from his signature on Humanist Manifesto II (1973), read on the American Humanist Association page (Wayback 20261006044056), whose signers pledge 'general support' 'while not necessarily endorsing every detail'. primary_system SECHUM (0.5, alt ATHE); A 4 (0.5); B 3 (0.5, alt 4; P41 and P35); C 4 (0.5); D 4 (0.5); mid_basin BELOW_THRESHOLD (A at 0.5). Plotted (faded). Draft, not reviewed."}
    - {date: 2026-10-17, by: "Grok Bot", summary: "Batch N audit fix (#15, v8's ruling on RQ2): added his own working-years text, Science and Human Behavior (1953; B.F. Skinner Foundation PDF, read directly): 'we must assume that behavior is lawful and determined' (p. 6) and 'The hypothesis that man is not free is essential to the application of scientific method to the study of human behavior' (p. 447). B 3 → 4 at 0.5, alternative 3. Timing fields now date the first LIO-type evidence to 1953, during the major work."}

identity:
  id: skinner-b-f
  display_name: "B.F. Skinner"
  roster:
    canonical_name: "B.F. Skinner"
    rank: 86
    F: 4
    models: [Claude, DeepSeek, Gemini, GPT]
    band: "core (3–4)"
    status: core
    field: psychology
    field_bucket: "psychology / neuroscience"
  full_name: {value: "B.F. Skinner", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica gives initials only; 'Burrhus Frederic' not read in a cited source."}
  native_name: {value: UNKNOWN, how_known: "English."}
  aliases:
    - {name: "B-F-Skinner", kind: "roster alias"}

basics:
  birth:
    date: {value: "1904-03-20", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Susquehanna, Pennsylvania, U.S.", modern_name: "Susquehanna, Pennsylvania, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "1990-08-18", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Cambridge, Massachusetts", modern_name: "Cambridge, Massachusetts, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1938, certainty: 0.5, cites: [{source: S1, locator: "Minnesota sentence"}], how_known: "The Behavior of Organisms (1938), the first dated work in the body of the 'influential exponent of behaviourism' (S1). The Skinner box is undated. 1938 is the coder's pick (P13)."}
  era_bucket: {value: "1850 to 1949", certainty: 0.5, cites: [{source: S1, locator: "Minnesota sentence"}], how_known: "From 1938 (P2)."}
  region_of_birth: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "United States (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Harvard, Minnesota, Indiana."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [English], certainty: 0.7, cites: [{source: S1, locator: "titles"}], how_known: "Britannica."}
  occupations: {value: ["psychologist", "professor", "author"], certainty: 0.7, cites: [{source: S1, locator: "opening; Harvard paragraph"}], how_known: "Britannica."}

contribution:
  fields: {value: ["behaviourism", "experimental psychology"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "The Behavior of Organisms: operant behaviour and reinforcement", year: 1938, kind: theory, lasting: "'Central to his approach is the concept of reinforcement'; 'influenced a generation of psychologists' (S1)", certainty: 0.5, cites: [{source: S1, locator: "Minnesota sentence; Harvard paragraph"}], how_known: "Britannica; pairing the 1938 book with reinforcement is the coder's reading."}
    - {value: "Skinner box", year: UNKNOWN, kind: invention, lasting: "'has been adopted in pharmaceutical research' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Harvard paragraph"}], how_known: "Britannica; undated."}
    - {value: "Beyond Freedom and Dignity", year: 1971, kind: work, lasting: "'generated considerable controversy' (S1)", certainty: 0.5, cites: [{source: S1, locator: "books paragraph"}], how_known: "Britannica; lasting status is the coder's reading."}
  evidence_of_impact:
    - {value: "'influenced a generation of psychologists'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "Harvard paragraph"}], how_known: "Britannica."}
  major_works:
    - {value: "Walden Two", year: 1948, kind: book, certainty: 0.7, cites: [{source: S1, locator: "Indiana paragraph"}], how_known: "Britannica."}
    - {value: "Science and Human Behavior", year: 1953, kind: book, certainty: 0.7, cites: [{source: S1, locator: "books paragraph"}], how_known: "Britannica."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
  parents_and_household: []
  household_circumstances: {value: TODO}
  schooling:
    - {value: "Harvard University (PhD 1931)", stage: university, years: "–1931", certainty: 0.7, cites: [{source: S1, locator: "Pavlov paragraph"}], how_known: "Britannica."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [English], certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1938–1971", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "Signed: 'Any account of nature should pass the tests of scientific evidence; in our judgment, the dogmas and myths of traditional religions do not do so'", certainty: 0.5, cites: [{source: S2, locator: "First"}], how_known: "Collective manifesto he signed with 'general support' (S2)."}
  primary_system:
    value: SECHUM
    basis: written_profession
    certainty: 0.5
    cites: [{source: S2, locator: "preface; First; signatories"}]
    rationale: "Signed Humanist Manifesto II (1973), listed as 'B. F. Skinner, Prof. of Psychology, Harvard Univ.' It says 'As nontheists, we begin with humans not God, nature not deity' and describes itself as 'naturalistic humanism'. Named alternative: ATHE."
    how_known: "A signed public statement, but collective, and the signers pledge 'general support' 'while not necessarily endorsing every detail' (S2), so 0.5."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: SECHUM, reason: "Signed a humanist manifesto."}
    - {code: ATHE, reason: "'nontheists ... nature not deity'; the manifesto's wording on God is 'insufficient evidence', not a flat denial."}
    - {code: DETERM, reason: "His 1953 determinism (S4) is a working assumption of method about behaviour; it bears on B, not on the system code (coder's call)."}
  lio_axes:
    A_locus:
      value: 4
      basis: written_profession
      certainty: 0.5
      cites: [{source: S2, locator: "First"}]
      rationale: "No God (P38): 'We find insufficient evidence for belief in the existence of a supernatural'; 'As nontheists, we begin with humans not God, nature not deity'; 'No deity will save us; we must save ourselves.' 'Insufficient evidence' is weaker than a flat denial, which is part of why this is 0.5."
      how_known: "Signed collective text with a 'not every detail' clause, so 0.5."
    B_cause:
      value: 4
      basis: written_profession
      certainty: 0.5
      cites: [{source: S4, locator: "p. 6"}, {source: S4, locator: "p. 447"}, {source: S2, locator: "First"}]
      rationale: "v8's ruling on RQ2 of the batch N audit (on the auditor's advice): his own 1953 text says 'If we are to use the methods of science in the field of human affairs, we must assume that behavior is lawful and determined', that science cannot be applied 'to a subject matter which is assumed to move about capriciously' (p. 6), and that 'The hypothesis that man is not free is essential to the application of scientific method to the study of human behavior' (p. 447). That denies the one exception B 3 allows (a free will outside natural law), so B 4 (P40). It is framed as a working assumption of method, not a claim about all of nature, so 0.5 with alternative 3. The manifesto he signed in 1973 (S2) rejects the supernatural in nature, consistent with this."
      how_known: "His own book, read in the B.F. Skinner Foundation PDF; dated 1953, inside the working years. Methodological framing, so 0.5."
      alternatives:
        - {value: 3, note: "The determinism is stated as a working hypothesis of method ('we must assume'); read as such, there is no stated exceptionless law of nature, and working science alone gives B 3 (P35).", cites: [{source: S4, locator: "p. 6"}]}
    C_ledger:
      value: 4
      basis: written_profession
      certainty: 0.5
      cites: [{source: S2, locator: "Second"}]
      rationale: "No ledger: 'Promises of immortal salvation or fear of eternal damnation are both illusory and harmful.'"
      how_known: "Signed collective text, 0.5."
    D_authority:
      value: 4
      basis: written_profession
      certainty: 0.5
      cites: [{source: S2, locator: "First"}]
      rationale: "'Any account of nature should pass the tests of scientific evidence; in our judgment, the dogmas and myths of traditional religions do not do so.'"
      how_known: "Signed collective text, 0.5."
    E_scope: {value: UNKNOWN, how_known: "Nothing read on the world's order as such (P7); P44(c) applies to systems, not people."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A 4 but at 0.5: the A ≥ 3 branch reads A only (P10) and needs 0.7, as for Hawking and Beauvoir."}
  statements:
    - text: "We cannot apply the methods of science to a subject matter which is assumed to move about capriciously. Science not only describes, it predicts. [...] If we are to use the methods of science in the field of human affairs, we must assume that behavior is lawful and determined."
      cites: [{source: S4, locator: "p. 6"}]
      date: "1953"
      context: "Science and Human Behavior, ch. I, 'The threat to freedom' (S4)."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-17
      note: "Foundation PDF of the book; page number from its running head."
    - text: "The hypothesis that man is not free is essential to the application of scientific method to the study of human behavior."
      cites: [{source: S4, locator: "p. 447"}]
      date: "1953"
      context: "Science and Human Behavior, section VI, 'The problem of control' (S4)."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-17
      note: "Foundation PDF; page number from its running head."
    - text: "We find insufficient evidence for belief in the existence of a supernatural; it is either meaningless or irrelevant to the question of survival and fulfillment of the human race. As nontheists, we begin with humans not God, nature not deity. Nature may indeed be broader and deeper than we now know; any new discoveries, however, will but enlarge our knowledge of the natural."
      cites: [{source: S2, locator: "First"}]
      date: "1973"
      context: "Humanist Manifesto II (1973), signed by Skinner among others (S2)."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-17
      note: "Collective text; signers 'not necessarily endorsing every detail'."
    - text: "Promises of immortal salvation or fear of eternal damnation are both illusory and harmful."
      cites: [{source: S2, locator: "Second"}]
      date: "1973"
      context: "Same manifesto."
      axes: [C_ledger]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-17
    - text: "We, the undersigned, while not necessarily endorsing every detail of the above, pledge our general support to Humanist Manifesto II for the future of humankind."
      cites: [{source: S2, locator: "signatories"}]
      date: "1973"
      context: "Signing clause above the list that includes 'B. F. Skinner, Prof. of Psychology, Harvard Univ.'"
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-17
  changes_over_life: []
  coder_notes: "Coder's call. A manifesto signature is his public profession but not his own wording, hence 0.5 throughout. The manifesto is dated 1973, after the working years (1938–1971); B rests on his own Science and Human Behavior (1953), inside them. Leads not read: his autobiography (Particulars of My Life, 1976) on his loss of faith, and the AHA Humanist of the Year award."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "American", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1938–1971", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "First to last dated listed lasting contribution (P29, P30)."}
  age_at_first_lasting_contribution: {value: 34, certainty: 0.5, cites: [{source: S1, locator: "opening; 1938"}], how_known: "1938 − 1904 = 34 (P30)."}
  first_evidence_of_lio_type_views: {value: "1953: behaviour 'lawful and determined'; 'man is not free' (Science and Human Behavior)", year: 1953, certainty: 0.5, cites: [{source: S4, locator: "p. 6; p. 447"}], how_known: "Earlier writings (1938, 1948) not read for this (P30 #7)."}
  lio_views_relative_to_major_work: {value: "during major work", rationale: "1953 falls inside 1938–1971.", certainty: 0.5, cites: [{source: S4, locator: "p. 6"}], how_known: "Dates of what was read."}
  worldview_during_major_work: {value: "Determinist about behaviour as a working assumption of science (1953); nothing read on God from these years", certainty: 0.5, cites: [{source: S4, locator: "p. 6; p. 447"}], how_known: "His own book."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Nothing read.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Nothing read."}
  circle_present: {value: "no", rationale: "'nature not deity'.", certainty: 0.5, cites: [{source: S2, locator: "First"}], how_known: "Coder's reading."}
  reading: "Nontheist naturalistic humanism."
  notes: ""

institutions:
  - {value: "University of Minnesota", role: "faculty", years: "1936–1945", kind: university, certainty: 0.5, cites: [{source: S1, locator: "Minnesota sentence"}], how_known: "Britannica (joined 1936; end year from the Indiana appointment)."}
  - {value: "Indiana University, Bloomington", role: "professor of psychology", years: "1945–1948", kind: university, certainty: 0.7, cites: [{source: S1, locator: "Indiana paragraph"}], how_known: "Britannica."}
  - {value: "Harvard University", role: "professor of psychology", years: "1948–1974", kind: university, certainty: 0.7, cites: [{source: S1, locator: "Harvard paragraph"}], how_known: "Britannica (emeritus 1974)."}
collaborators:
  - {value: "Ivan Pavlov", relation: "influenced by", note: "conditioned reflexes", certainty: 0.7, cites: [{source: S1, locator: "Pavlov paragraph"}], how_known: "Britannica."}
  - {value: "John B. Watson", relation: "influenced by", note: "founder of behaviourism", certainty: 0.7, cites: [{source: S1, locator: "Pavlov paragraph"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 86"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Britannica article is unsigned (Britannica Editors)."
    - "A, C and D rest on one collective manifesto he signed, not on his own wording; B rests on his own 1953 book."
  open_questions:
    - "Read Particulars of My Life (1976) and his own essays for a first-person statement on God and nature."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "Britannica Editors. \"B.F. Skinner.\" Encyclopaedia Britannica. https://www.britannica.com/biography/B-F-Skinner. Read in Wayback snapshot 20261005171724."
    url: "https://www.britannica.com/biography/B-F-Skinner"
    accessed: 2026-10-17
    reliability_note: "Unsigned article. Body only; Top Questions not cited."
    used_for: [identity, basics, contribution, childhood, timing, institutions, collaborators]
  - id: S2
    type: primary
    kind: "institutional page"
    author: "American Humanist Association"
    citation: "Humanist Manifesto II (1973), with signatories. American Humanist Association. https://americanhumanist.org/what-is-humanism/manifesto2/. Read in Wayback snapshot 20261006044056 (live page returned 403)."
    url: "https://americanhumanist.org/what-is-humanism/manifesto2/"
    accessed: 2026-10-17
    reliability_note: "The copyright holder's own text of the manifesto and signer list; quotations checked word for word."
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
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "B. F. Skinner"
    citation: "Skinner, B. F. Science and Human Behavior. New York: Macmillan, 1953. Read in the B. F. Skinner Foundation PDF (copyright 2014): https://www.bfskinner.org/wp-content/uploads/2014/02/ScienceHumanBehavior.pdf"
    url: "https://www.bfskinner.org/wp-content/uploads/2014/02/ScienceHumanBehavior.pdf"
    accessed: 2026-10-17
    reliability_note: "The Foundation's PDF of the book, with the book's page numbers in the running heads; quotations checked word for word."
    used_for: [worldview, timing]
---

# B.F. Skinner

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

B.F. Skinner (1904–1990), American behaviourist psychologist [S1]. Draft: primary_system SECHUM (0.5, alt ATHE); A 4 at 0.5; B 4 at 0.5 (alt 3); C 4 at 0.5; D 4 at 0.5; mid_basin BELOW_THRESHOLD. Plotted (faded).

## Life and work

Harvard PhD 1931; Minnesota, Indiana, Harvard [S1].

## Contribution and impact

The Behavior of Organisms (1938), reinforcement, the Skinner box, Walden Two (1948) [S1].

## Childhood and education

Not read.

## Adult working worldview

Behaviour 'lawful and determined'; 'man is not free' (1953) [S4, p. 6; p. 447]. Signed Humanist Manifesto II (1973) [S2].

## Heritage (context only)

American [S1].

## Timing

First lasting contribution 1938, at 34 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No circle [S2].

## Open questions

- Autobiography for his own words.

## Research log

- 2026-10-17: Read Britannica (Wayback 20261005171724) and Humanist Manifesto II with signers (AHA, Wayback 20261006044056; live page 403); quotations checked word for word.
