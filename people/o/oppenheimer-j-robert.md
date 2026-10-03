---
record:
  record_type: person
  schema_version: "1.2"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, fourth batch: physical science 1600–1950)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (fourth batch, RUNBOOK §1 order). Basics from Britannica (Rouzé) and the Institute for Advanced Study's page. Worldview: no statement of his on God or religion was read in a checkable source. His Los Alamos farewell speech (2 November 1945, Atomic Heritage Foundation excerpts) states a faith in the value of science; his 1965 televised interview (interview) recalls the Bhagavad Gita line at Trinity. primary_system BELOW_THRESHOLD (ETHCUL candidate, stub; HINDU rejected). B 4 at 0.5 from his working science (P6); A, C, D, E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. His AIP oral-history interviews carry quotation limits and were not used. Not reviewed."}

identity:
  id: oppenheimer-j-robert
  display_name: "J. Robert Oppenheimer"
  roster:
    canonical_name: "J. Robert Oppenheimer"
    rank: 185
    F: 3
    models: [Gemini, GPT, Grok]
    band: "core (3–4)"
    status: core
    field: physics
    field_bucket: physics
  full_name: {value: "J. Robert Oppenheimer", certainty: 1.0, cites: [{source: S1, locator: "heading"}, {source: S2, locator: "heading"}], how_known: "Two sources; the expansion of 'J.' is not given in the sources read."}
  native_name: {value: "J. Robert Oppenheimer (English)", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "English name."}
  aliases:
    - {name: "J-Robert-Oppenheimer", kind: "roster alias"}
    - {name: "Oppenheimer-J-Robert", kind: "roster alias"}
    - {name: "Robert Oppenheimer", kind: "roster alias"}

basics:
  birth:
    date: {value: "1904-04-22", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "New York City", modern_name: "New York, New York, USA", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "1967-02-18", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "closing paragraphs"}], how_known: "Two sources agree."}
    place: {value: "Princeton, New Jersey", modern_name: "Princeton, New Jersey, USA", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1927, certainty: 0.7, cites: [{source: S2, locator: "Göttingen paragraph ('worked with Born on the structure of molecules')"}], how_known: "IAS page: the Born–Oppenheimer work of 1927, the year of his doctorate."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S2, locator: "Göttingen paragraph"}], how_known: "From first_lasting_contribution_year (P2)."}
  region_of_birth: {value: "North America", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "USA is North America in data/reference/regions.csv (P3)."}
  region_of_work: {value: "North America", certainty: 1.0, cites: [{source: S1, locator: "'Early life and education'; Manhattan Project section"}], how_known: "Berkeley, Caltech, Los Alamos, Princeton."}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "As the sources record it."}
  languages_of_work: {value: [English], certainty: 1.0, cites: [{source: S3, locator: "speech"}, {source: S2, locator: "Reith Lectures"}], how_known: "Speeches and lectures in English."}
  occupations: {value: ["theoretical physicist", "science administrator", "university professor"], certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "opening"}], how_known: "Two sources."}

contribution:
  fields: {value: ["quantum theory", "nuclear and particle physics", "astrophysics"], certainty: 1.0, cites: [{source: S1, locator: "'Early life and education', paragraph 3"}, {source: S2, locator: "Berkeley paragraphs"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Born–Oppenheimer treatment of molecular structure, with Max Born", year: "1927", kind: method, lasting: "standard approximation in molecular physics", certainty: 0.7, cites: [{source: S2, locator: "Göttingen paragraph"}], how_known: "IAS page."}
    - {value: "Work on neutron stars and black holes", year: "1930s", kind: theory, lasting: "described as 'groundbreaking' by Britannica", certainty: 0.7, cites: [{source: S1, locator: "'Early life and education', paragraph 3"}], how_known: "Britannica; years not given on the page."}
    - {value: "Direction of the Los Alamos Laboratory, which built the first atomic bombs (Trinity test, 16 July 1945)", year: "1943–1945", kind: institution, lasting: "nuclear weapons and the national-laboratory model", certainty: 1.0, cites: [{source: S1, locator: "opening; Manhattan Project section"}], how_known: "Britannica."}
  evidence_of_impact:
    - {value: "Trained 'a whole generation of U.S. physicists'", kind: "institutional or technological lineage", certainty: 0.7, cites: [{source: S1, locator: "'Early life and education', paragraph 3"}], how_known: "Britannica."}
  major_works:
    - {value: "Science and the Common Understanding (BBC Reith Lectures)", year: 1953, kind: "lecture series", certainty: 1.0, cites: [{source: S2, locator: "Reith Lectures sentence"}], how_known: "IAS page."}
  honours:
    - {value: "Enrico Fermi Award of the Atomic Energy Commission", year: 1963, certainty: 1.0, cites: [{source: S1, locator: "'Oppenheimer's legacy'"}, {source: S2, locator: "closing paragraphs"}], how_known: "Two sources."}
  definition_fit: {value: "arguable", rationale: "A leading theorist (Born–Oppenheimer, neutron stars and black holes) and teacher; his fame rests mostly on directing Los Alamos, an administrative role.", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Early life and education'"}], how_known: "Coder's judgement from Britannica."}

childhood:
  family_religion: {value: TODO, note: "Not stated in the sources read. He attended the Ethical Culture School (S2), whose religious or non-religious character for the family is not described there."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father, a German immigrant who made his fortune importing textiles in New York; died 1937, leaving Robert a fortune", role: father, certainty: 1.0, cites: [{source: S1, locator: "'Early life and education'; Manhattan Project section, paragraph 1"}], how_known: "Britannica (his name is not given on the page read)."}
  household_circumstances: {value: "Wealthy New York family", certainty: 0.7, cites: [{source: S1, locator: "'Early life and education'"}], how_known: "Britannica."}
  schooling:
    - {value: "Ethical Culture School of New York (graduated top of his class, 1921)", stage: "grammar or secondary school", years: "–1921", certainty: 0.7, cites: [{source: S2, locator: "education paragraph"}], how_known: "IAS page."}
    - {value: "Harvard University: Latin, Greek, physics and chemistry, Eastern philosophy; summa cum laude 1925", stage: university, years: "1922–1925", certainty: 1.0, cites: [{source: S1, locator: "'Early life and education'"}, {source: S2, locator: "education paragraph"}], how_known: "Two sources; start year is the coder's reading."}
    - {value: "Cavendish Laboratory, Cambridge; then University of Göttingen (PhD 1927 with Max Born)", stage: university, years: "1925–1927", certainty: 1.0, cites: [{source: S1, locator: "'Early life and education', paragraphs 1–2"}, {source: S2, locator: "Göttingen paragraph"}], how_known: "Two sources."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [English], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Born in New York; other childhood languages not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1925–1967", certainty: 1.0, cites: [{source: S1, locator: "'Early life and education' to 'Oppenheimer's legacy'"}], how_known: "Research from 1925 to death."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No statement by him on science and religion was read in a checkable source. The 1945 farewell speech speaks of 'our faith' in the value of science (S3), which is about the worth of knowledge, not about religion."}
  primary_system:
    value: BELOW_THRESHOLD
    cites: [{source: S2, locator: "education paragraph"}, {source: S3, locator: "speech"}, {source: S4, locator: "clip transcript (interview)"}]
    how_known: "No first-hand statement of his on God, religion or ethics as a system was read. His schooling (Ethical Culture School) and his study of Eastern philosophy and use of the Bhagavad Gita (interview, S4) are upbringing and literary reference, not a profession."
    note: "Candidate: ETHCUL (stub system file, flagged). Would need his own statements (letters in Smith and Weiner, Letters and Recollections, 1980, in a library copy) or a biography such as Bird and Sherwin (2005)."
  secondary_system: {value: UNKNOWN, how_known: "No system evidence in the sources read."}
  candidate_codes_considered:
    - {code: ETHCUL, reason: "Leading candidate, not coded (BELOW_THRESHOLD): schooled at the Ethical Culture School (S2); his adult adherence to Ethical Culture is not shown in what was read. Stub system file (flag).", cites: [{source: S2, locator: "education paragraph"}]}
    - {code: HINDU, reason: "Rejected: he studied Eastern philosophy at Harvard (S1) and in a 1965 interview (interview) recalled 'the line from the Hindu scripture, the Bhagavad-Gita' at the Trinity test (S4); a literary recollection, not a profession of Hindu belief. Stub system file (flag).", cites: [{source: S1, locator: "'Early life and education'"}, {source: S4, locator: "clip transcript (interview)"}]}
    - {code: SCIENT, reason: "Considered: the farewell speech's 'belief in the value of science' and 'faith in this' (S3). Not coded: a professional ethic of knowledge is not a metaphysics. Stub system file (flag).", cites: [{source: S3, locator: "speech, 'organic necessity' and closing paragraphs"}]}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "No statement placing or denying God was read."}
    B_cause:
      value: 4
      basis: scholarly_reconstruction
      certainty: 0.5
      cites: [{source: S1, locator: "'Early life and education', paragraph 3"}, {source: S3, locator: "speech, 'organic necessity' paragraph"}]
      how_known: "Coder's reading of his working science, as P6 directs (same treatment as Fermi and Dirac). No statement of his own about miracles read, so 0.5."
      rationale: "Scored on his account of nature (P6). His physics (energy processes of subatomic particles, neutron stars and black holes, S1) is lawful quantum and relativistic theory, and he describes the scientist's belief 'that it is good to find out how the world works' (S3). No miracle, petition or exemption in anything read."
    C_ledger: {value: BELOW_THRESHOLD, how_known: "Nothing on judgement, afterlife or reward and punishment in the sources read."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "No statement on revelation in the sources read.", note: "The farewell speech's 'faith' in science (S3) is about the value of knowledge, not observation against revelation."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Scored on the world's order (P7). Nothing read addresses favour for a group in events."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD and B_cause is only 0.5, under the P4 test's 0.7 bar."}
  statements:
    - text: "If you are a scientist you believe that it is good to find out how the world works; that it is good to find out what the realities are; that it is good to turn over to mankind at large the greatest possible power to control the world and to deal with it according to its lights and its values."
      cites: [{source: S3, locator: "speech, 'organic necessity' paragraph"}]
      date: "1945-11-02"
      context: "Farewell speech to the Association of Los Alamos Scientists, on why the scientists built the bomb; AHF excerpts."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-02
    - text: "I remembered the line from the Hindu scripture, the Bhagavad-Gita. Vishnu is trying to persuade the Prince that he should do his duty and to impress him takes on his multi-armed form and says, “Now, I am become Death, the destroyer of worlds.” I suppose we all thought that one way or another."
      cites: [{source: S4, locator: "clip transcript (interview)"}]
      date: "1965"
      context: "(interview) Recorded television interview for the NBC documentary The Decision to Drop the Bomb (1965), recalling the Trinity test; transcript on the Atomic Archive. Published broadcast, so quotation is permitted; scores nothing (P8: a passing recollection, not a statement of belief)."
      axes: []
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-02
  changes_over_life: []
  coder_notes: "ETHCUL, HINDU and SCIENT are stub system files (flag). Interview-based content (marked '(interview)'): only the 1965 NBC clip (S4), a published broadcast, used in one statement and in the HINDU rejection; it scores no axis or code. His AIP oral-history interviews carry AIP quotation limits and were not used or quoted. S3 is the Atomic Heritage Foundation's excerpt of the farewell speech and S4 the Atomic Archive's transcript of the film clip; both are unofficial web copies (§7), marked secondary quotation. A copy of Smith and Weiner, Letters and Recollections, seen on the Internet Archive has unclear provenance and was not used. changes_over_life is empty after research."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "German immigrant father (New York textile importer)", certainty: 0.7, cites: [{source: S1, locator: "'Early life and education'"}], how_known: "Britannica; the family's Jewish background is widely reported but not stated in the sources read."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO, note: "Ethical Culture School (S2); its moral instruction is not described in the source."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1927–1945", certainty: 0.7, cites: [{source: S1, locator: "'Early life and education' to Manhattan Project section"}, {source: S2, locator: "Göttingen paragraph"}], how_known: "Born–Oppenheimer work to Trinity; coder's reading."}
  age_at_first_lasting_contribution: {value: 23, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Göttingen paragraph"}], how_known: "Born April 1904; 1927 work."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No checkable worldview statement found."}
  lio_views_relative_to_major_work: {value: "unclear", rationale: "No checkable worldview statement found.", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Nothing to date."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Nothing read on his method beyond theoretical physics in general.", certainty: 0.5, cites: [{source: S1, locator: "'Early life and education', paragraph 3"}], how_known: "No evidence."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "education paragraph"}], how_known: "Classics, chemistry and physics at Harvard; nothing on method."}
  circle_present: {value: "unclear", rationale: "No God-Nature statement read; not scored from absence.", certainty: 0.5, cites: [{source: S3, locator: "speech"}], how_known: "No evidence either way."}
  reading: "As belief, not finding: form unclear, circle unclear. The record does not test H1."
  notes: ""

institutions:
  - {value: "University of California, Berkeley, and California Institute of Technology", role: "professor of physics", years: "1929–1943", kind: university, certainty: 0.7, cites: [{source: S1, locator: "'Early life and education', paragraph 2"}], how_known: "Britannica; years are the coder's reading (after 1927 visits to Leiden and Zürich; to Los Alamos 1943)."}
  - {value: "Los Alamos Laboratory (Manhattan Project)", role: director, years: "1943–1945", kind: "government or state body", certainty: 1.0, cites: [{source: S1, locator: "opening; Manhattan Project section"}], how_known: "Britannica."}
  - {value: "General Advisory Committee of the Atomic Energy Commission", role: chairman, years: "1947–1952", kind: "government or state body", certainty: 1.0, cites: [{source: S1, locator: "Manhattan Project section, last paragraph"}], how_known: "Britannica."}
  - {value: "Institute for Advanced Study, Princeton", role: director, years: "1947–1966", kind: employer, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "opening"}], how_known: "Two sources."}
collaborators:
  - {value: "Max Born", roster_id: born-max, relation: teacher, note: "doctoral work at Göttingen; Born–Oppenheimer (1927)", certainty: 1.0, cites: [{source: S1, locator: "'Early life and education', paragraph 2"}, {source: S2, locator: "Göttingen paragraph"}], how_known: "Two sources."}
  - {value: "Niels Bohr", roster_id: bohr-niels, relation: "influenced by", note: "met and studied with him in Göttingen", certainty: 0.7, cites: [{source: S2, locator: "Göttingen paragraph"}, {source: S1, locator: "'Early life and education', paragraph 2"}], how_known: "Two sources (Britannica: 'met')."}
  - {value: "Ernest Rutherford", roster_id: rutherford-ernest, relation: other, note: "research at the Cavendish Laboratory, then under Rutherford's leadership (IAS: research assistant to J. J. Thomson)", certainty: 0.7, cites: [{source: S1, locator: "'Early life and education', paragraph 1"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3: Gemini, GPT, Grok).", certainty: 0.7, cites: [{source: S5, locator: "roster.csv, rank 185"}], how_known: "Study roster."}
  controversies:
    - {value: "1954 security hearing: clearance withdrawn after accusations of past communist associations and opposition to the hydrogen bomb", certainty: 1.0, cites: [{source: S1, locator: "'Security hearing and later years'"}, {source: S2, locator: "later paragraphs"}], how_known: "Two sources."}
  data_quality_flags:
    - "No checkable statement on religion; primary_system rests on nothing first-hand."
    - "S3 and S4 are unofficial web copies (§7)."
  open_questions:
    - "Read Smith and Weiner, Robert Oppenheimer: Letters and Recollections (1980), in a library copy, for letters on the Gita, Ethical Culture and religion."
    - "Read Bird and Sherwin, American Prometheus (2005), on the Ethical Culture School and his adult views."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Michel Rouzé"
    citation: "Rouzé, Michel. \"J. Robert Oppenheimer.\" Encyclopaedia Britannica. https://www.britannica.com/biography/J-Robert-Oppenheimer."
    url: "https://www.britannica.com/biography/J-Robert-Oppenheimer"
    accessed: 2026-10-02
    reliability_note: "Signed article. Sections cited by heading."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators, review]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "Institute for Advanced Study"
    citation: "Institute for Advanced Study. \"J. Robert Oppenheimer.\" https://www.ias.edu/oppenheimer-legacy."
    url: "https://www.ias.edu/oppenheimer-legacy"
    accessed: 2026-10-02
    reliability_note: "Institutional biography by his employer of 1947–66. Cited by paragraph description."
    used_for: [identity, basics, contribution, childhood, worldview, timing, lane_b, institutions, collaborators, review]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "J. Robert Oppenheimer"
    year: 1945
    citation: "Oppenheimer, J. Robert. Speech to the Association of Los Alamos Scientists, Los Alamos, 2 November 1945. Excerpts as 'Oppenheimer's Farewell Speech', Atomic Heritage Foundation / National Museum of Nuclear Science & History, https://ahf.nuclearmuseum.org/ahf/key-documents/oppenheimers-farewell-speech/."
    url: "https://ahf.nuclearmuseum.org/ahf/key-documents/oppenheimers-farewell-speech/"
    accessed: 2026-10-02
    reliability_note: "His own speech in a museum's excerpt; the copy-text is not named on the page, so it is treated as an unofficial web copy (§7). Cited by paragraph."
    used_for: [basics, worldview, lane_b]
  - id: S4
    type: primary
    kind: other
    author: "J. Robert Oppenheimer"
    year: 1965
    citation: "Oppenheimer, J. Robert. Recorded interview in the NBC documentary The Decision to Drop the Bomb (1965). Clip and transcript: \"J. Robert Oppenheimer 'Now I am become death...'\", Atomic Archive, https://www.atomicarchive.com/media/videos/oppenheimer.html."
    url: "https://www.atomicarchive.com/media/videos/oppenheimer.html"
    accessed: 2026-10-02
    reliability_note: "(interview) His own words in a published broadcast; transcript by the Atomic Archive (unofficial web copy). Used for one recollection only; scores nothing."
    used_for: [worldview]
  - id: S5
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
---

# J. Robert Oppenheimer

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

J. Robert Oppenheimer (1904–1967), American theoretical physicist, worked with Born on molecular structure, did early work on neutron stars and black holes, directed Los Alamos (1943–45) and then the Institute for Advanced Study (1947–66) [S1; S2]. No statement of his on God or religion was read in a checkable source. primary_system BELOW_THRESHOLD (ETHCUL candidate, stub). B 4 at 0.5 from the working science; A, C, D, E below threshold; mid_basin below threshold.

## Life and work

Ethical Culture School (1921), Harvard (1925), Cavendish, Göttingen (PhD 1927), Berkeley and Caltech, Los Alamos, IAS; security hearing 1954; Fermi Award 1963 [S1; S2].

## Contribution and impact

Born–Oppenheimer (1927), neutron stars and black holes, a generation of American physicists, and the Los Alamos laboratory [S1; S2].

## Childhood and education

Son of a wealthy German-immigrant textile importer; Ethical Culture School; classics and Eastern philosophy at Harvard [S1; S2].

## Adult working worldview

Not established from checkable sources. In 1945 he spoke of the scientist's belief "that it is good to find out how the world works" [S3]. In a 1965 interview (interview) he recalled a line of the Bhagavad Gita at Trinity [S4]; that is a recollection, not a profession, and scores nothing.

## Heritage (context only)

German-immigrant father [S1]. Context only.

## Timing

First lasting contribution 1927, at 23 [S2].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form unclear; circle unclear.

## Open questions

- Letters and Recollections (1980) in a library copy; Bird and Sherwin (2005).

## Research log

- 2026-10-02: Read Britannica (Rouzé), the IAS page, the AHF excerpts of the farewell speech, the AHF 1965 Groueff interview (Manhattan Project organisation only; nothing on religion) and the Atomic Archive's 1965 NBC clip transcript. The AIP oral history was not used (quotation limits).
