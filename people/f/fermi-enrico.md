---
record:
  record_type: person
  schema_version: "1.2"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, second batch: physical science 1600–1950)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (second batch, RUNBOOK §1 order). Basics, contribution and childhood from Britannica (Badash), MacTutor and the Nobel biography. No writing by Fermi on religion was found; Laura Fermi's Atoms in the Family (p. 52, the usual source for 'agnostic') is lending-only on archive.org and was not read. primary_system BELOW_THRESHOLD (AGNOS candidate, stub). B_cause 4 at 0.5 from his working science (P6); A, C, D, E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit, batch 2 (finding #32): region_of_work locator now paragraphs 2–5, since Florence is in Nobel paragraph 2. Value and certainty unchanged. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Schema 1.1 → 1.2 (decision P8 adds basis recorded_interview and statement kind 'recorded interview'); no content change."}

identity:
  id: fermi-enrico
  display_name: "Enrico Fermi"
  roster:
    canonical_name: "Enrico Fermi"
    rank: 23
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: physics
    field_bucket: physics
  full_name: {value: "Enrico Fermi", certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}, {source: S2, locator: "heading"}], how_known: "Sources agree."}
  native_name: {value: "Enrico Fermi (Italian)", certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}], how_known: "Same spelling in Italian."}
  aliases:
    - {name: "Enrico-Fermi", kind: "roster alias"}
    - {name: "Fermi-Enrico", kind: "roster alias"}

basics:
  birth:
    date: {value: "1901-09-29", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S3, locator: "first paragraph"}], how_known: "Two sources agree."}
    place: {value: "Rome", modern_name: "Rome, Italy", polity_then: "Kingdom of Italy", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S3, locator: "first paragraph"}], how_known: "Two sources agree."}
  death:
    date: {value: "1954-11-28", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S2, locator: "Quick Info"}], how_known: "Two sources agree."}
    place: {value: "Chicago, Illinois", modern_name: "Chicago, Illinois, United States", polity_then: "United States", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}], how_known: "Britannica; MacTutor gives burial in Oak Woods Cemetery, Chicago (S2)."}
  first_lasting_contribution_year: {value: 1926, certainty: 1.0, cites: [{source: S3, locator: "paragraph 3"}, {source: S1, locator: "Fermi-Dirac statistics"}], how_known: "Fermi statistics (Fermi–Dirac statistics), 1926; two sources."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S3, locator: "paragraph 3"}], how_known: "From first_lasting_contribution_year (P2)."}
  region_of_birth: {value: "Southern Europe", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}], how_known: "Italy is Southern Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Southern Europe", certainty: 0.7, cites: [{source: S3, locator: "paragraphs 2–5 (Florence in paragraph 2)"}], how_known: "Fermi statistics, beta-decay theory and slow neutrons (1926–1934) were done in Florence and Rome. The first controlled chain reaction (1942) was in Chicago. Two regions, so 0.7.", alternatives: [{value: "North America", cites: [{source: S3, locator: "paragraphs 6–8"}], note: "Columbia 1939–1942; Chicago 1942–1954."}]}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S3, locator: "first paragraph ('the son of')"}], how_known: "As the sources record it."}
  languages_of_work: {value: [Italian, English], certainty: 1.0, cites: [{source: S2, locator: "Biography (Italian titles of 1921–1935 papers; English papers in Proc. Roy. Soc.)"}], how_known: "MacTutor lists papers in both languages."}
  occupations: {value: [physicist, "university professor"], certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}, {source: S3, locator: "paragraphs 4–8"}], how_known: "Sources agree."}

contribution:
  fields: {value: ["theoretical physics", "nuclear physics", "statistical mechanics", "particle physics"], certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}, {source: S3, locator: "paragraphs 3–8"}], how_known: "Sources agree."}
  lasting_original_contributions:
    - {value: "Fermi(–Dirac) statistics for particles obeying the exclusion principle (fermions)", year: "1926", kind: theory, lasting: "Britannica: 'a contribution of exceptional importance to atomic and nuclear physics'", certainty: 1.0, cites: [{source: S1, locator: "Fermi-Dirac statistics"}, {source: S3, locator: "paragraph 3"}], how_known: "Two sources; developed independently by Dirac (S1)."}
    - {value: "Theory of beta decay", year: "1934", kind: theory, lasting: "standard nuclear physics", certainty: 1.0, cites: [{source: S3, locator: "paragraph 5"}], how_known: "Nobel biography."}
    - {value: "Neutron-induced radioactivity and slow neutrons", year: "1934", kind: discovery, lasting: "Nobel Prize 1938; led to the discovery of fission (S3)", certainty: 1.0, cites: [{source: S2, locator: "Biography"}, {source: S3, locator: "paragraph 5"}], how_known: "Two sources."}
    - {value: "First controlled nuclear chain reaction (Chicago Pile-1)", year: "1942", kind: invention, lasting: "the first nuclear reactor (S1)", certainty: 1.0, cites: [{source: S1, locator: "opening summary"}, {source: S2, locator: "Biography"}, {source: S3, locator: "paragraph 7"}], how_known: "Three sources."}
  evidence_of_impact:
    - {value: "Nobel Prize for Physics 1938", kind: "honours in lifetime", certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}, {source: S2, locator: "Biography"}], how_known: "Two sources."}
    - {value: "Particles named fermions after him", kind: "named after them", certainty: 1.0, cites: [{source: S1, locator: "Fermi-Dirac statistics"}, {source: S3, locator: "paragraph 3"}], how_known: "Two sources."}
  major_works: []
  honours:
    - {value: "Nobel Prize for Physics", year: 1938, certainty: 1.0, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor quotes the citation."}
  definition_fit: {value: "clearly meets", rationale: "Several lasting original contributions in theory and experiment.", certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}], how_known: "Sources agree."}

childhood:
  family_religion: {value: "Nominally Catholic family background, but his own household was not religious; his father's relatives were devout Catholics", certainty: 0.7, cites: [{source: S2, locator: "Biography ('the family were not religious')"}], how_known: "MacTutor (one source). The baptism usually reported (in accordance with his grandparents' wishes) was not confirmed in a source read; see open questions."}
  family_religious_practice: {value: "Not religious; his elementary school was chosen because it was secular", certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor."}
  parents_and_household:
    - {value: "Father, Alberto Fermi, a railway official (chief inspector)", name: "Alberto Fermi", role: father, certainty: 1.0, cites: [{source: S1, locator: "early life"}, {source: S2, locator: "Biography"}, {source: S3, locator: "first paragraph"}], how_known: "Three sources (S3 says Ministry of Communications)."}
    - {value: "Mother, Ida de Gattis, an elementary schoolteacher", name: "Ida de Gattis", role: mother, certainty: 1.0, cites: [{source: S1, locator: "early life"}, {source: S2, locator: "Biography"}], how_known: "Two sources."}
  household_circumstances: {value: "Civil-service family in Rome; brother Giulio died in 1915, when Enrico was 14", certainty: 1.0, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor."}
  schooling:
    - {value: "Secular elementary school, from age six", stage: "other", ages: "6–10", certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor."}
    - {value: "Ginnasio (five years) and liceo (three years), Rome", stage: "grammar or secondary school", certainty: 0.7, cites: [{source: S2, locator: "Biography"}, {source: S3, locator: "first paragraph"}], how_known: "Two sources."}
    - {value: "Scuola Normale Superiore and University of Pisa; doctorate 1922", stage: university, years: "1918–1922", certainty: 1.0, cites: [{source: S1, locator: "early life"}, {source: S2, locator: "Biography"}, {source: S3, locator: "first paragraph"}], how_known: "Three sources."}
  early_mathematics: {value: "advanced mathematics", note: "Puzzling out the equation of a circle by about age ten; his 1918 entrance essay used partial differential equations and Fourier analysis", certainty: 1.0, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor."}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure:
    - {value: "Built electric motors and mechanical toys with his brother and sister; mathematics and physics encouraged by his father's colleague A. Amidei", certainty: 1.0, cites: [{source: S2, locator: "Biography"}, {source: S3, locator: "first paragraph"}], how_known: "Two sources."}
  key_early_reading: []
  childhood_mentors:
    - {value: "A. Amidei, a colleague of his father", certainty: 0.7, cites: [{source: S3, locator: "first paragraph"}], how_known: "Nobel biography."}
  languages_in_childhood: {value: [Italian], certainty: 1.0, cites: [{source: S2, locator: "Biography"}], how_known: "Born and schooled in Rome."}
  notable_events:
    - {value: "Death of his brother Giulio", year: 1915, age: 14, certainty: 1.0, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1921–1954", certainty: 1.0, cites: [{source: S2, locator: "Biography"}], how_known: "First paper 1921 to death."}
  nominal_affiliations:
    - {value: "No church membership reported for his adult life in the sources read; his two children were Roman Catholics", role: other, certainty: 0.7, cites: [{source: S2, locator: "Biography (1938)"}], how_known: "MacTutor (one source)."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No statement by Fermi on science and religion in S1–S3."}
  primary_system:
    value: BELOW_THRESHOLD
    cites: [{source: S2, locator: "Biography"}]
    how_known: "No writing or reported speech of Fermi on religion was found in the sources read. The usual claim that he was an agnostic throughout adult life cites Laura Fermi, Atoms in the Family (1954), p. 52, which could not be read (lending-only scan)."
    note: "Candidate: AGNOS (stub system file, flagged). Would need Laura Fermi p. 52 or Segrè's biography to reach 0.5."
  secondary_system: {value: UNKNOWN, how_known: "No system evidence at all in S1–S3."}
  candidate_codes_considered:
    - {code: AGNOS, reason: "Leading candidate, not coded (BELOW_THRESHOLD): the agnostic description comes through a source not read. AGNOS is a stub system file (flag)."}
    - {code: CHRIST, reason: "Rejected: a non-religious household (S2) and no adult practice reported. Heritage is never a code.", cites: [{source: S2, locator: "Biography"}]}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "No statement about God or the divine in the sources read.", note: "Gap: Laura Fermi 1954; Segrè 1970."}
    B_cause:
      value: 4
      basis: scholarly_reconstruction
      certainty: 0.5
      cites: [{source: S3, locator: "paragraphs 3–7"}, {source: S2, locator: "Biography"}]
      how_known: "Coder's reading of his working science, as P6 directs for a scientist. No statement of his own about miracles or exceptions, so 0.5."
      rationale: "Scored on his account of nature (P6), which for a scientist is the working science. Statistical laws for fermions, beta decay, neutron reactions and the chain reaction all treat nature as governed by law with no special cases. No miracle, petition or exemption appears anywhere in the sources read."
    C_ledger: {value: BELOW_THRESHOLD, how_known: "Nothing on reward, punishment or afterlife in the sources read."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "No statement on revelation in the sources read.", note: "His practice is wholly empirical, but D asks about revelation versus observation, which needs a statement."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Scored on the world's order (P7). His physics applies the same laws everywhere, but whether his account of events keeps any exception for a group is not addressed in any source read, so below 0.5.", note: "Not scored from the working science alone, unlike B, because P7 asks a second question (in-group exceptions) that needs a statement."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD and B_cause is only 0.5, under the P4 test's 0.7 bar."}
  statements: []
  changes_over_life: []
  coder_notes: "No verifiable quotation on religion was found; nothing is quoted in statements. Two Fermi religion anecdotes often repeated online (an agnostic self-description; a remark about the stars) were not traced to an accessible source and are not used."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Italian", certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}], how_known: "Sources agree."}
  religious_heritage_by_birth: {value: "Catholic family background (his father's relatives devout Catholics)", certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor."}
  baptism_or_initiation: {value: TODO, note: "Commonly reported as Catholic baptism at his grandparents' wish; not confirmed in a source read."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not mentioned in S1–S3; his elementary school was secular (S2)."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1926–1942", certainty: 1.0, cites: [{source: S3, locator: "paragraphs 3–7"}], how_known: "From Fermi statistics to the chain reaction."}
  age_at_first_lasting_contribution: {value: 24, certainty: 0.7, cites: [{source: S3, locator: "paragraph 3"}], how_known: "Born September 1901; the 1926 statistics paper. 24 or 25 depending on the month of the paper, which S3 does not give."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No worldview statement in S1–S3."}
  lio_views_relative_to_major_work: {value: "unclear", rationale: "No worldview statement found.", certainty: 0.5, cites: [{source: S2, locator: "Biography"}], how_known: "Absence in the sources read."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "A friend recalled that for him 'to know a theorem or law meant chiefly to know how to use it' (S2): a practical rather than axiomatic style.", certainty: 0.5, cites: [{source: S2, locator: "Biography (Persico)"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "Biography"}], how_known: "Coder's reading."}
  circle_present: {value: "no", rationale: "No God-Nature identity in anything read.", certainty: 0.5, cites: [{source: S2, locator: "Biography"}], how_known: "Absence in the sources read."}
  reading: "As belief, not finding: form unclear (practical style), circle absent. The record does not test H1."
  notes: ""

institutions:
  - {value: "University of Rome", role: "professor of theoretical physics", years: "1927–1938", kind: university, certainty: 1.0, cites: [{source: S3, locator: "paragraph 4"}, {source: S2, locator: "Biography"}], how_known: "Two sources."}
  - {value: "Columbia University", role: "professor of physics", years: "1939–1942", kind: university, certainty: 1.0, cites: [{source: S1, locator: "opening summary"}, {source: S3, locator: "paragraph 6"}], how_known: "Two sources."}
  - {value: "University of Chicago (Manhattan Project; Institute for Nuclear Studies)", role: "group leader; professor", years: "1942–1954", kind: university, certainty: 1.0, cites: [{source: S1, locator: "opening summary"}, {source: S3, locator: "paragraphs 7–8"}], how_known: "Two sources."}
collaborators:
  - {value: "Max Born", relation: teacher, note: "Göttingen, 1923", certainty: 1.0, cites: [{source: S1, locator: "early life"}, {source: S3, locator: "paragraph 2"}], how_known: "Two sources."}
  - {value: "Paul Ehrenfest", relation: teacher, note: "Leiden, 1924", certainty: 1.0, cites: [{source: S1, locator: "early life"}, {source: S3, locator: "paragraph 2"}], how_known: "Two sources."}
  - {value: "Paul Dirac", roster_id: dirac-paul, relation: other, note: "developed the same statistics independently", certainty: 1.0, cites: [{source: S1, locator: "Fermi-Dirac statistics"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v7.1 (F 4) and v8 (F 5, all five models).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 23"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Academy of 1929: MacTutor says Mussolini appointed him to the Accademia dei Lincei; Britannica says the new Accademia d'Italia. Britannica's version is probably right; not settled from the sources read."
    - "Chicago professorship: MacTutor says the offer came in 1945; the Nobel biography and Britannica say 1946."
  open_questions:
    - "Read Laura Fermi, Atoms in the Family (1954), p. 52, and Segrè, Enrico Fermi, Physicist (1970), for any statement on religion; until then A, C, D, E and primary_system stay below threshold."
    - "Confirm the Catholic baptism."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Lawrence Badash"
    citation: "Badash, Lawrence. \"Enrico Fermi.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Enrico-Fermi."
    url: "https://www.britannica.com/biography/Enrico-Fermi"
    accessed: 2026-10-02
    reliability_note: "Signed article by a historian of science."
    used_for: [identity, basics, contribution, childhood, heritage, institutions, collaborators]
  - id: S2
    type: tertiary
    kind: encyclopedia
    author: "J. J. O'Connor and E. F. Robertson"
    citation: "O'Connor, J. J. and E. F. Robertson. \"Enrico Fermi.\" MacTutor History of Mathematics Archive, University of St Andrews. https://mathshistory.st-andrews.ac.uk/Biographies/Fermi/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Fermi/"
    accessed: 2026-10-02
    reliability_note: "Standard biographical archive; quotes Persico, Segrè and Laura Fermi."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions]
  - id: S3
    type: tertiary
    kind: "institutional page"
    author: "Nobel Foundation"
    citation: "\"Enrico Fermi – Biographical.\" NobelPrize.org (from Nobel Lectures, Physics 1922–1941, Elsevier, 1965). https://www.nobelprize.org/prizes/physics/1938/fermi/biographical/."
    url: "https://www.nobelprize.org/prizes/physics/1938/fermi/biographical/"
    accessed: 2026-10-02
    reliability_note: "Official biography; paragraphs counted from the top of the text."
    used_for: [basics, contribution, childhood, timing, institutions, collaborators]
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

# Enrico Fermi

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Enrico Fermi (1901–1954), Italian-born physicist, developed Fermi statistics (1926), the theory of beta decay and neutron-induced radioactivity (1934), and directed the first controlled chain reaction (1942) [S1, opening paragraph; S3, paragraphs 3–7]. Nobel Prize 1938 [S2, Biography]. No statement of his on religion was found in accessible sources, so his worldview is below threshold; B_cause is 4 at 0.5 from his working science.

## Life and work

Born in Rome, he studied at the Scuola Normale in Pisa, worked with Born and Ehrenfest, held the Rome chair of theoretical physics from 1927, and left Italy in 1938 for Columbia and then Chicago [S3, paragraphs 1–8; S2, Biography].

## Contribution and impact

Fermi statistics, beta-decay theory, slow neutrons and the first reactor [S3, paragraphs 3–7]. Britannica calls him "one of the chief architects of the nuclear age" [S1, opening paragraph].

## Childhood and education

His household was not religious, which upset his father's devout Catholic relatives, and his elementary school was chosen because it was secular [S2, Biography]. By about ten he was working out why x² + y² = r² is a circle [S2, Biography].

## Adult working worldview

No writing or reported speech on religion was found in the sources read [S1; S2; S3]. The common report that he was agnostic traces to Laura Fermi's 1954 memoir, which could not be read. primary_system BELOW_THRESHOLD (AGNOS candidate, stub). B 4 at 0.5 from the working science; A, C, D, E below threshold; mid_basin below threshold.

## Heritage (context only)

Italian, Catholic family background [S2, Biography]. Context only.

## Timing

First lasting contribution 1926, at about 24 [S3, paragraph 3]. No worldview statement to time.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. A practical, use-oriented style of knowing laws is reported [S2, Biography]; no circle.

## Open questions

- Laura Fermi p. 52 and Segrè 1970 on religion.

## Research log

- 2026-10-02: Read Britannica (Badash), MacTutor and the Nobel biography. Searched for Fermi on religion; the agnostic claim traces (via Wikipedia's footnote) to Laura Fermi, Atoms in the Family, p. 52; archive.org copies are lending-only. Nothing quoted on religion.
