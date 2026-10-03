---
record:
  record_type: person
  schema_version: "1.2"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, third batch: physical science 1600–1950)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (third batch, RUNBOOK §1 order). Basics from Britannica (Kojevnikov, first page), MacTutor and the Nobel biography. No writing by Dirac on religion could be checked: the 1963 Scientific American article is access-restricted on the Internet Archive, the FSU Library scan of his 1976 Lindau lecture notes sits behind a bot challenge, and the 1927 Solvay remarks survive only in Heisenberg's later reconstruction (another person's report). primary_system BELOW_THRESHOLD (ATHE candidate, stub). B 4 at 0.5 from his working science (P6); A, C, D, E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Schema 1.1 → 1.2 (decision P8 adds basis recorded_interview and statement kind 'recorded interview'); no content change."}

identity:
  id: dirac-paul
  display_name: "Paul Dirac"
  roster:
    canonical_name: "Paul Dirac"
    rank: 124
    F: 4
    models: [Claude, DeepSeek, Gemini, GPT]
    band: "core (3–4)"
    status: core
    field: physics
    field_bucket: physics
  full_name: {value: "Paul Adrien Maurice Dirac", certainty: 1.0, cites: [{source: S2, locator: "heading"}, {source: S3, locator: "paragraph 1"}], how_known: "Two sources."}
  native_name: {value: "Paul Adrien Maurice Dirac (English)", certainty: 1.0, cites: [{source: S3, locator: "paragraph 1"}], how_known: "English name."}
  aliases:
    - {name: "Dirac-Paul", kind: "roster alias"}
    - {name: "Paul-Dirac", kind: "roster alias"}
    - {name: "P. A. M. Dirac", kind: other}

basics:
  birth:
    date: {value: "1902-08-08", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "paragraph 1"}], how_known: "Two sources agree."}
    place: {value: "Bristol", modern_name: "Bristol, England, UK", polity_then: "United Kingdom", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "paragraph 1"}], how_known: "Two sources agree."}
  death:
    date: {value: "1984-10-20", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Quick Info"}], how_known: "Two sources agree."}
    place: {value: "Tallahassee, Florida", modern_name: "Tallahassee, Florida, USA", polity_then: "United States", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Quick Info"}], how_known: "Two sources agree."}
  first_lasting_contribution_year: {value: 1925, certainty: 1.0, cites: [{source: S3, locator: "paragraph 2"}, {source: S2, locator: "Biography (1925 paragraph)"}], how_known: "His independent algebraic formulation of quantum mechanics after reading Heisenberg's paper in 1925."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S3, locator: "paragraph 2"}], how_known: "From first_lasting_contribution_year (P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "UK is Northern Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 1.0, cites: [{source: S2, locator: "Biography"}, {source: S3, locator: "paragraph 1"}], how_known: "Cambridge 1923–1969; Florida (North America) from 1969."}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S3, locator: "paragraph 1"}], how_known: "As the sources record it."}
  languages_of_work: {value: [English], certainty: 1.0, cites: [{source: S3, locator: "paragraph 2"}], how_known: "Papers in the Proceedings of the Royal Society."}
  occupations: {value: ["theoretical physicist", "university professor"], certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Biography"}], how_known: "Two sources."}

contribution:
  fields: {value: ["quantum mechanics", "quantum electrodynamics", "theoretical physics"], certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Summary"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "General mathematical formulation of quantum mechanics (q-numbers, Poisson-bracket analogy; transformation theory)", year: "1925–1926", kind: theory, lasting: "foundation of quantum mechanics", certainty: 1.0, cites: [{source: S1, locator: "paragraph after 'Physics and Natural Law'"}, {source: S2, locator: "Biography (1925 paragraph)"}], how_known: "Two sources."}
    - {value: "Quantum theory of radiation (second quantization)", year: "1927", kind: theory, lasting: "beginning of quantum electrodynamics", certainty: 0.7, cites: [{source: S1, locator: "paragraph on QED"}], how_known: "Britannica."}
    - {value: "Relativistic wave equation for the electron (Dirac equation)", year: "1928", kind: theory, lasting: "standard physics; Nobel Prize 1933", certainty: 1.0, cites: [{source: S1, locator: "'In 1928 Dirac published'"}, {source: S3, locator: "paragraphs 2–3"}], how_known: "Two sources."}
    - {value: "Prediction of antimatter (the positron)", year: "1930–1931", kind: discovery, lasting: "confirmed 1932; antiparticles a universal property of matter", certainty: 1.0, cites: [{source: S1, locator: "'In 1928 Dirac published', paragraphs 2–3"}, {source: S3, locator: "paragraph 2"}], how_known: "Two sources."}
    - {value: "Fermi–Dirac statistics", year: "1926", kind: "law or principle", lasting: "standard physics", certainty: 0.7, cites: [{source: S1, locator: "paragraph after 'Physics and Natural Law'"}], how_known: "Britannica."}
  evidence_of_impact:
    - {value: "Nobel Prize in Physics 1933 (shared with Schrödinger)", kind: "honours in lifetime", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Biography (1933)"}], how_known: "Two sources."}
  major_works:
    - {value: "The Principles of Quantum Mechanics", year: 1930, kind: book, certainty: 1.0, cites: [{source: S1, locator: "later work paragraph"}, {source: S2, locator: "Biography (1930)"}], how_known: "Two sources."}
  honours:
    - {value: "Nobel Prize in Physics", year: 1933, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Biography"}], how_known: "Two sources."}
    - {value: "Fellow of the Royal Society", year: 1930, certainty: 1.0, cites: [{source: S2, locator: "Biography (1930)"}, {source: S3, locator: "paragraph 4"}], how_known: "Two sources."}
    - {value: "Copley Medal", year: 1952, certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor; Nobel page names the medal without a year."}
    - {value: "Pontifical Academy of Sciences (member)", year: 1961, certainty: 0.5, cites: [{source: S3, locator: "paragraph 4 (1961)"}, {source: S2, locator: "honours paragraph (1958)"}], how_known: "Sources disagree (1961 vs 1958)."}
    - {value: "Order of Merit", year: 1973, certainty: 0.7, cites: [{source: S2, locator: "honours paragraph"}], how_known: "MacTutor."}
  definition_fit: {value: "clearly meets", rationale: "A founder of quantum mechanics and QED.", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "Sources agree."}

childhood:
  family_religion: {value: TODO, note: "Not stated in the sources read."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father, Charles Adrien Ladislas Dirac, Swiss-born French teacher at the Merchant Venturers' school, a strict disciplinarian", name: "Charles Dirac", role: father, certainty: 1.0, cites: [{source: S2, locator: "Biography, paragraph 1"}, {source: S1, locator: "childhood paragraph"}], how_known: "Two sources."}
    - {value: "Mother, Florence Hannah Holten, from Cornwall, working in a Bristol library when she met Charles", name: "Florence Dirac (née Holten)", role: mother, certainty: 1.0, cites: [{source: S2, locator: "Biography, paragraph 1"}, {source: S3, locator: "paragraph 1"}], how_known: "Two sources (English mother)."}
  household_circumstances: {value: "Strict, unhappy home (oppressive paternal discipline); French only at the father's table; an older brother (Reginald, who later took his own life) and a younger sister", certainty: 1.0, cites: [{source: S2, locator: "Biography, paragraphs 2, 7"}, {source: S1, locator: "childhood paragraph"}], how_known: "Two sources."}
  schooling:
    - {value: "Bishop Primary School (as MacTutor names it), Bristol", stage: "dame or charity school", years: "–1914", certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraph 3"}], how_known: "MacTutor; nearest stage."}
    - {value: "Merchant Venturers' Technical College secondary school, Bristol", stage: "grammar or secondary school", years: "1914–1918", certainty: 1.0, cites: [{source: S2, locator: "Biography, paragraph 3"}, {source: S3, locator: "paragraph 1"}], how_known: "Two sources."}
    - {value: "University of Bristol: electrical engineering (BSc 1921), then mathematics (first class, 1923)", stage: university, years: "1918–1923", certainty: 1.0, cites: [{source: S1, locator: "education paragraph"}, {source: S2, locator: "Biography, paragraphs 4–5"}], how_known: "Two sources."}
    - {value: "St John's College, Cambridge, research student under Ralph Fowler (PhD 1926)", stage: university, years: "1923–1926", certainty: 1.0, cites: [{source: S2, locator: "Biography, paragraph 6"}, {source: S3, locator: "paragraph 1"}], how_known: "Two sources."}
  early_mathematics: {value: "advanced mathematics", note: "At school he studied from books ahead of his class (his own account quoted by MacTutor).", certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraph 3"}], how_known: "MacTutor quoting Dirac."}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure:
    - {value: "Early access to the school's science laboratories during World War I", certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraph 3"}], how_known: "MacTutor."}
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [English, French], certainty: 1.0, cites: [{source: S2, locator: "Biography, paragraph 2"}], how_known: "French at his father's table."}
  notable_events:
    - {value: "Elder brother Reginald took his own life while Paul was a research student", year: "1925", certainty: 0.7, cites: [{source: S2, locator: "Biography (research-student paragraph)"}], how_known: "MacTutor; year from the period described."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1923–1984", certainty: 1.0, cites: [{source: S2, locator: "Biography"}], how_known: "From research student to death."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No statement by Dirac on science and religion could be read in a checkable source (see coder_notes)."}
  primary_system:
    value: BELOW_THRESHOLD
    cites: [{source: S2, locator: "Biography"}]
    how_known: "No writing or first-hand reported speech of Dirac on religion was read. The well-known Solvay 1927 outburst against religion is Heisenberg's reconstruction decades later, in his memoir, and so is another person's report, not usable as Dirac's statement; his 1963 'God is a mathematician' passage (Scientific American, May 1963) and his 1976 Lindau lecture notes could not be checked."
    note: "Candidate: ATHE (stub system file, flagged). Would need Kragh's biography (1990), the Scientific American text, or the FSU notes."
  secondary_system: {value: UNKNOWN, how_known: "No system evidence in the sources read."}
  candidate_codes_considered:
    - {code: ATHE, reason: "Leading candidate, not coded (BELOW_THRESHOLD): rests on Heisenberg's reconstruction of the 1927 Solvay conversation and on Pauli's quip, both reports by others. ATHE is a stub system file (flag)."}
    - {code: AGNOS, reason: "Considered: his later writing is reported to treat God as an open hypothesis; not read. AGNOS is a stub system file (flag)."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "No statement placing or denying God was read."}
    B_cause:
      value: 4
      basis: scholarly_reconstruction
      certainty: 0.5
      cites: [{source: S1, locator: "QED and 1928 paragraphs"}, {source: S2, locator: "Biography"}]
      how_known: "Coder's reading of his working science, as P6 directs (same treatment as Fermi). No statement of his own about miracles read, so 0.5."
      rationale: "Scored on his account of nature (P6). He accepted that the fundamental laws of microscopic particles are probabilistic ('nature makes a choice', S1) and trusted mathematical formalism to find new laws, predicting the positron from his equation (S1): statistical and mathematical law throughout, with no miracle, petition or exemption in anything read."
    C_ledger: {value: BELOW_THRESHOLD, how_known: "Nothing on reward, punishment or afterlife in the sources read."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "No statement on revelation in the sources read.", note: "His view that a true theory must be mathematically beautiful (S1) concerns method within physics, not revelation versus observation."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Scored on the world's order (P7). Nothing read addresses favour for a group in events; not scored from working science alone (same treatment as Fermi and Curie)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD and B_cause is only 0.5, under the P4 test's 0.7 bar."}
  statements: []
  changes_over_life: []
  coder_notes: "ATHE and AGNOS are stub system files (flag). Nothing is quoted in statements because no religious statement by Dirac could be checked: (1) Scientific American, May 1963 ('The Evolution of the Physicist's Picture of Nature') is access-restricted on the Internet Archive (sim_scientific-american_1963-05_208_5); (2) the FSU Libraries scan of his handwritten notes for 'Basic Beliefs and Prejudices in Physics' (Lindau, 29 June 1976; fsu:200), which the catalogue says covers whether there is a God, returned an AWS bot challenge to both fetch tools; the Lindau Mediatheque has the audio only; (3) the 1927 Solvay remarks are Heisenberg's reconstruction (Der Teil und das Ganze, 1969) and Pauli's 'There is no God and Dirac is his prophet' is Pauli's line, so neither is scored as Dirac's own words."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "English mother, Swiss father (from Monthey, Valais)", certainty: 1.0, cites: [{source: S2, locator: "Biography, paragraph 1"}, {source: S3, locator: "paragraph 1"}], how_known: "Two sources."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1925–1933", certainty: 1.0, cites: [{source: S1, locator: "opening to 1928 paragraphs"}, {source: S2, locator: "Biography"}], how_known: "Quantum mechanics to the Lagrangian paper and the Nobel Prize."}
  age_at_first_lasting_contribution: {value: 23, certainty: 1.0, cites: [{source: S3, locator: "paragraphs 1–2"}], how_known: "Born August 1902; work of late 1925."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No checkable worldview statement found."}
  lio_views_relative_to_major_work: {value: "unclear", rationale: "No checkable worldview statement found.", certainty: 0.5, cites: [{source: S2, locator: "Biography"}], how_known: "Nothing to date."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "He sought laws through mathematical formalism and beauty and argued 'with unbeatable logic' (S2, quoting Pais et al.), but from equations, not definitions and axioms in the Euclidean manner.", certainty: 0.5, cites: [{source: S1, locator: "1928 paragraphs"}, {source: S2, locator: "Biography (1930)"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "Biography, paragraph 3"}], how_known: "Rapid early mathematics; nothing on method."}
  circle_present: {value: "unclear", rationale: "No God-Nature statement could be read; not scored from absence.", certainty: 0.5, cites: [{source: S2, locator: "Biography"}], how_known: "No evidence either way."}
  reading: "As belief, not finding: form partly present (mathematical beauty as guide), circle unclear. The record does not test H1."
  notes: ""

institutions:
  - {value: "University of Cambridge (St John's College)", role: "fellow (1927); Lucasian Professor of Mathematics (1932–1969)", years: "1923–1969", kind: university, certainty: 1.0, cites: [{source: S2, locator: "Biography"}, {source: S3, locator: "paragraph 1"}], how_known: "Two sources."}
  - {value: "Florida State University", role: "professor of physics", years: "1971–1984", kind: university, certainty: 1.0, cites: [{source: S1, locator: "'Dirac taught at Cambridge' paragraph"}, {source: S2, locator: "Biography (1971)"}], how_known: "Two sources."}
collaborators:
  - {value: "Ralph Fowler", relation: teacher, note: "research adviser at Cambridge (Britannica: Dirac 'had no teacher in the true sense, but his adviser, Ralph Fowler')", certainty: 1.0, cites: [{source: S1, locator: "education paragraph"}, {source: S2, locator: "Biography, paragraph 6"}], how_known: "Two sources."}
  - {value: "Werner Heisenberg", roster_id: heisenberg-werner, relation: "influenced by", note: "the 1925 paper Dirac reworked; travelled together to Japan in 1929", certainty: 1.0, cites: [{source: S1, locator: "'In August 1925 Dirac received through Fowler proofs'"}, {source: S3, locator: "paragraph 5"}], how_known: "Two sources."}
  - {value: "Niels Bohr", roster_id: bohr-niels, relation: "mentor or employer", note: "worked with Bohr in Copenhagen after his 1926 PhD", certainty: 0.7, cites: [{source: S2, locator: "Biography (after the doctorate)"}], how_known: "MacTutor."}
  - {value: "Erwin Schrödinger", roster_id: schrodinger-erwin, relation: other, note: "shared the 1933 Nobel Prize", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Biography (1933)"}], how_known: "Two sources."}
  - {value: "Eugene Wigner", relation: family, note: "brother-in-law: Dirac married Wigner's sister Margit in 1937", certainty: 1.0, cites: [{source: S2, locator: "Biography (1934–35)"}], how_known: "MacTutor."}

review:
  roster_status_reason: {value: "Core in v8 (F 4: Claude, DeepSeek, Gemini, GPT).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 124"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Pontifical Academy of Sciences membership: 1961 (Nobel page) vs 1958 (MacTutor)."
    - "No primary statement on religion could be checked; three leads are listed in coder_notes."
    - "Britannica read as its first page only."
  open_questions:
    - "Get the FSU scan of the 1976 Lindau notes (fsu:200) through a browser session, and the May 1963 Scientific American article through a library."
    - "Read Kragh, Dirac: A Scientific Biography (1990), and Farmelo, The Strangest Man (2009), for documented statements, keeping Heisenberg's reconstruction apart."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Alexei Kojevnikov"
    citation: "Kojevnikov, Alexei. \"P.A.M. Dirac.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Paul-Dirac."
    url: "https://www.britannica.com/biography/Paul-Dirac"
    accessed: 2026-10-02
    reliability_note: "Signed article; first page only. Cited by paragraph description."
    used_for: [basics, contribution, childhood, worldview, timing, lane_b, institutions, collaborators]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "J J O'Connor and E F Robertson"
    citation: "O'Connor, J. J., and E. F. Robertson. \"Paul Adrien Maurice Dirac.\" MacTutor History of Mathematics, University of St Andrews. https://mathshistory.st-andrews.ac.uk/Biographies/Dirac/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Dirac/"
    accessed: 2026-10-02
    reliability_note: "Biography; paragraphs counted from 'Paul Dirac's father'."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S3
    type: tertiary
    kind: "institutional page"
    author: "Nobel Foundation"
    year: 1965
    citation: "\"Paul A.M. Dirac – Biographical.\" From Nobel Lectures, Physics 1922–1941. Amsterdam: Elsevier, 1965. NobelPrize.org. https://www.nobelprize.org/prizes/physics/1933/dirac/biographical/."
    url: "https://www.nobelprize.org/prizes/physics/1933/dirac/biographical/"
    accessed: 2026-10-02
    reliability_note: "Official biography; paragraphs counted from 'Paul Adrien Maurice Dirac was born'."
    used_for: [identity, basics, contribution, childhood, heritage, timing, institutions]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
---

# Paul Dirac

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Paul Adrien Maurice Dirac (1902–1984), English theoretical physicist, gave quantum mechanics its general mathematical form, wrote the relativistic equation of the electron and predicted antimatter; he shared the 1933 Nobel Prize with Schrödinger [S1; S3]. No statement of his on religion could be checked; the famous anti-religious remarks of 1927 are Heisenberg's later reconstruction. primary_system BELOW_THRESHOLD (ATHE candidate, stub). B 4 at 0.5 from the working science; A, C, D, E below threshold; mid_basin below threshold.

## Life and work

Born in Bristol to a Swiss father and an English mother, he studied engineering and mathematics at Bristol and research at Cambridge under Fowler, held the Lucasian chair from 1932 to 1969, and ended his career at Florida State University [S1; S2].

## Contribution and impact

Quantum mechanics (1925–26), quantum theory of radiation (1927), the Dirac equation (1928) and the positron (1930–31) [S1; S2; S3].

## Childhood and education

A strict, unhappy home in which only French was spoken at his father's table [S2, Biography, paragraph 2].

## Adult working worldview

Not established from checkable sources. His working physics is lawful and probabilistic [S1], which gives B 4 at 0.5 only.

## Heritage (context only)

English and Swiss parentage [S2]. Context only.

## Timing

First lasting contribution 1925, at 23 [S3].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form partly present (mathematical beauty); circle unclear.

## Open questions

- The FSU Lindau notes, the 1963 Scientific American article, Kragh (1990).

## Research log

- 2026-10-02: Read Britannica (Kojevnikov, first page), MacTutor and the Nobel biography. The Scientific American scan is lending-only; the FSU repository returned a bot challenge to curl and WebFetch; the Lindau Mediatheque holds audio only.
