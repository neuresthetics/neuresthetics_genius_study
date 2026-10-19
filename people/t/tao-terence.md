---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Y)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Audit fixes for batch Y (gs_7b46f24_Y run 1): (TA7) Solving mathematical problems dated 1992, its first edition (written 1990; MacTutor). Ruling Y3 (v8's call on the auditor's advice): not a scientist; B stays UNKNOWN (recorded under P30). No score changes."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Y, order P32: F 4, rank 134; roster status provisional). Basics from Britannica (Jeremy John Gray, 18 Oct 2026) and MacTutor (O'Connor and Robertson, December 2023). The Green–Tao theorem dated by its arXiv submission (8 April 2004; Annals of Mathematics 2008). No statement on religion or nature found in a reliable source; web pages offering 'quotes' on his faith are unsourced and not used. Not a scientist (pure mathematics; RQ-Y3). Span 2004 at 0.5. primary_system and all axes UNKNOWN; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}

identity:
  id: tao-terence
  display_name: "Terence Tao"
  roster:
    canonical_name: "Terence Tao"
    rank: 134
    F: 4
    models: [Claude, Gemini, GPT, Grok]
    band: "core (3–4)"
    status: provisional
    field: mathematics
    field_bucket: mathematics
  full_name: {value: "Terence Chi-Shen Tao", certainty: 0.7, cites: [{source: S2, locator: "Quick Info"}], how_known: "MacTutor."}
  native_name: {value: "Terence Chi-Shen Tao", certainty: 0.5, cites: [{source: S2, locator: "Quick Info"}], how_known: "English form; Chinese characters not given in the sources read."}
  aliases:
    - {name: "Tao-Terence", kind: "roster alias"}
    - {name: "Terence-Tao", kind: "roster alias"}
    - {name: "Terry Tao", kind: other}

basics:
  birth:
    date: {value: "1975-07-17", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S2, locator: "Quick Info"}], how_known: "Both sources."}
    place: {value: "Adelaide, South Australia", modern_name: "Adelaide, South Australia, Australia", polity_then: "Australia", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S2, locator: "Quick Info"}], how_known: "Both sources."}
  death:
    date: {value: UNKNOWN, how_known: "Living (Britannica gives his age as 51)."}
    place: {value: UNKNOWN, how_known: "Living."}
  first_lasting_contribution_year: {value: 2004, certainty: 0.5, cites: [{source: S2, locator: "Fields Medal paragraphs ('work with Ben Green on the distribution of prime numbers'; 'This fantastic achievement')"}, {source: S3, locator: "arXiv math/0404188, submitted 8 Apr 2004"}], how_known: "The Green–Tao theorem (the primes contain arbitrarily long arithmetic progressions), dated by its first public statement, the arXiv preprint of 8 April 2004 (S3; P30); published in Annals of Mathematics 167 (2008), 481–547 (Crossref). His earlier work on the Kakeya problem and the nonlinear Schrödinger equation is undated in the sources read and may be earlier (P12), so 0.5."}
  era_bucket: {value: "1950 on", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}], how_known: "Born 1975; every adult year falls in '1950 on' (P2)."}
  region_of_birth: {value: "Oceania", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S2, locator: "Quick Info"}], how_known: "Australia (P3)."}
  region_of_work: {value: "North America", certainty: 1.0, cites: [{source: S1, locator: "body ('joined the faculty at the University of California, Los Angeles')"}, {source: S2, locator: "career paragraphs"}], how_known: "UCLA from 1996."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S2, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S3, locator: "paper"}], how_known: "His papers."}
  occupations: {value: ["mathematician", "professor at the University of California, Los Angeles"], certainty: 1.0, cites: [{source: S1, locator: "body"}, {source: S2, locator: "career paragraphs"}], how_known: "Both sources."}

contribution:
  fields: {value: ["partial differential equations", "combinatorics", "harmonic analysis", "additive number theory"], certainty: 1.0, cites: [{source: S1, locator: "opening (Fields Medal citation)"}, {source: S2, locator: "Summary"}], how_known: "Fields Medal citation in both sources."}
  lasting_original_contributions:
    - {value: "Green–Tao theorem: the primes contain arbitrarily long arithmetic progressions (with Ben Green)", year: 2004, kind: "law or principle", lasting: "'This fantastic achievement' (S2); cited in the 2006 Fields Medal press release (S2)", certainty: 0.5, cites: [{source: S2, locator: "Fields Medal paragraphs"}, {source: S3, locator: "arXiv math/0404188"}], how_known: "MacTutor for lasting; date from arXiv (P30). Pure mathematics (P30), so not a scientist."}
    - {value: "Existence theorems for the nonlinear Schrödinger equation (with collaborators)", year: UNKNOWN, kind: "law or principle", lasting: "'established crucial existence theorems' (S1); 'giving the subject a whole new look' (S2)", certainty: 0.7, cites: [{source: S1, locator: "body"}, {source: S2, locator: "Schrödinger paragraph"}], how_known: "Both sources; undated in the sources read, so it sets no span (P12). Theorems about an equation used in physics; the coder reads this as mathematics, not a theory of a physical system (RQ-Y3)."}
    - {value: "Contributions to the Kakeya problem", year: UNKNOWN, kind: "body of work", lasting: "'a great resurgence of interest' (S2)", certainty: 0.7, cites: [{source: S2, locator: "Kakeya paragraph"}], how_known: "MacTutor; undated (P12)."}
  evidence_of_impact:
    - {value: "Fields Medal (2006)", kind: "honours in lifetime", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Summary; honours"}], how_known: "Both sources."}
    - {value: "Fellow of the Royal Society (2007); Crafoord Prize (2012); Breakthrough Prize in Mathematics (2014)", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S2, locator: "honours paragraph"}], how_known: "MacTutor."}
  major_works:
    - {value: "Solving mathematical problems: A personal perspective", year: 1992, kind: book, certainty: 0.7, cites: [{source: S2, locator: "1989–1990 paragraph ('The first edition was published in 1992')"}], how_known: "MacTutor: written in 1990, at 15; first edition 1992 (batch Y audit, TA7)."}
  honours:
    - {value: "Salem Prize", year: 2000, certainty: 1.0, cites: [{source: S1, locator: "last paragraph"}, {source: S2, locator: "honours paragraph"}], how_known: "Both sources."}
    - {value: "Fields Medal", year: 2006, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "honours paragraph"}], how_known: "Both sources."}
  definition_fit: {value: "clearly meets", rationale: "'a supreme problem-solver whose spectacular work has had an impact across several mathematical areas' (Fields citation, quoted in S2).", certainty: 0.7, cites: [{source: S2, locator: "Fields Medal paragraphs"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated in the sources read."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Father Billy Tao, a Chinese-born paediatrician; mother Grace, born in Hong Kong, with a degree in physics and mathematics; they emigrated to Australia in 1972", role: family, certainty: 0.7, cites: [{source: S2, locator: "opening of Biography"}], how_known: "MacTutor."}
  household_circumstances: {value: "Eldest of three brothers, all later PhDs", certainty: 0.7, cites: [{source: S2, locator: "opening of Biography"}], how_known: "MacTutor."}
  schooling:
    - {value: "Blackwood High School, Adelaide", stage: "grammar or secondary school", run_by: "state or municipal", years: "1983–1988", certainty: 0.5, cites: [{source: S2, locator: "Blackwood paragraph"}], how_known: "MacTutor gives the school and years; run_by is the coder's reading (an Adelaide public high school), so 0.5."}
    - {value: "Flinders University (B.Sc. Honours 1991; master's 1992)", stage: university, run_by: "state or municipal", years: "1989–1992", certainty: 0.7, cites: [{source: S2, locator: "Flinders paragraphs"}, {source: S1, locator: "body"}], how_known: "Both sources; classes there from age about 11 (S2)."}
    - {value: "Princeton University (PhD 1996)", stage: university, run_by: private, years: "1992–1996", certainty: 1.0, cites: [{source: S1, locator: "body"}, {source: S2, locator: "graduate school paragraphs"}], how_known: "Both sources."}
  early_mathematics: {value: "advanced mathematics", certainty: 0.7, cites: [{source: S2, locator: "Clements paragraph ('reading a hardback book with the title Calculus' at seven)"}], how_known: "MacTutor."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "Garth Gaudry (Flinders University)", certainty: 0.7, cites: [{source: S2, locator: "Flinders paragraphs"}], how_known: "MacTutor."}
  languages_in_childhood: {value: ["English"], certainty: 0.5, cites: [{source: S2, locator: "text"}], how_known: "Coder's reading."}
  notable_events:
    - {value: "International Mathematical Olympiad medals from age ten", year: 1986, certainty: 0.5, cites: [{source: S2, locator: "Olympiad paragraph"}], how_known: "MacTutor: 'at the age of ten'; year the coder's."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "2004", certainty: 0.5, cites: [{source: S3, locator: "arXiv math/0404188"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing found."}
  primary_system: {value: UNKNOWN, how_known: "Searched: Britannica and MacTutor say nothing on religion; a web search found only unsourced pages (some with invented-looking 'quotes' on his faith), which are not used (P19)."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered: []
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing found (P19)."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (pure mathematics; ruling Y3: existence and well-posedness theorems are mathematical results about equations physics uses, the Hilbert case), and no statement on nature found (P16, P19). If his PDE work counts as a result about a physical system (P30), B would be 3 at 0.5 from working science (P24, P35)."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing found (P19)."}
    D_authority: {value: UNKNOWN, how_known: "Nothing found (P19)."}
    E_scope: {value: UNKNOWN, how_known: "Nothing found (P7, P19)."}
  mid_basin: {value: UNKNOWN, how_known: "A and B are UNKNOWN (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "Coder's call on the span: only the Green–Tao theorem is both called lasting and datable from the sources read (arXiv 2004); the NLS and Kakeya work is undated, and later results (Collatz progress 2019, the 2022 tiling counterexample with Greenfeld, S2) are recent and not called lasting. Not a scientist (ruling Y3). Leads for worldview: his blog and long-form interviews (MacTutor's references list several); none read."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Chinese (father Chinese-born; mother from Hong Kong)", certainty: 0.7, cites: [{source: S2, locator: "opening of Biography"}], how_known: "MacTutor."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "2004", certainty: 0.5, cites: [{source: S3, locator: "arXiv math/0404188"}, {source: S2, locator: "Fields Medal paragraphs"}], how_known: "Only one dated lasting contribution (P29, P30)."}
  age_at_first_lasting_contribution: {value: 29, certainty: 0.5, cites: [{source: S1, locator: "Quick Facts"}], how_known: "2004 − 1975 = 29 (P30); 28 by month."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "Nothing found."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "Nothing found."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Nothing found."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S2, locator: "text"}], how_known: "Not assessed."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "text"}], how_known: "Not assessed."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S2, locator: "text"}], how_known: "Not assessed."}
  reading: ""
  notes: ""

institutions:
  - {value: "University of California, Los Angeles", role: "faculty", years: "from 1996", kind: university, certainty: 1.0, cites: [{source: S1, locator: "body"}, {source: S2, locator: "career paragraphs"}], how_known: "Both sources."}
collaborators:
  - {value: "Ben Green", relation: collaborator, note: "Green–Tao theorem", certainty: 0.7, cites: [{source: S2, locator: "Fields Medal paragraphs"}], how_known: "MacTutor."}
  - {value: "Elias Stein", relation: teacher, note: "doctoral adviser at Princeton", certainty: 0.7, cites: [{source: S2, locator: "graduate school paragraph ('advised by Elias Stein')"}], how_known: "MacTutor."}

review:
  roster_status_reason: {value: "Provisional in v8 (F 4; four models).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 134"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "No worldview evidence in reliable sources; search results with 'quotes' are unsourced and not used."
    - "Contribution year taken from arXiv, not from S1 or S2."
  open_questions:
    - "Settled by ruling Y3: not a scientist."
    - "Read his blog and long-form interviews for statements on religion or nature."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Jeremy John Gray (Britannica)"
    citation: "Gray, Jeremy John. \"Terence Tao.\" Encyclopaedia Britannica (18 Oct 2026). https://www.britannica.com/biography/Terence-Tao. Read live 2026-10-19."
    url: "https://www.britannica.com/biography/Terence-Tao"
    accessed: 2026-10-19
    reliability_note: "Signed short article."
    used_for: [identity, basics, contribution, childhood, timing, institutions]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "J. J. O'Connor and E. F. Robertson (MacTutor)"
    citation: "O'Connor, J. J., and E. F. Robertson. \"Terence Chi-Shen Tao.\" MacTutor History of Mathematics, University of St Andrews (last update December 2023). https://mathshistory.st-andrews.ac.uk/Biographies/Tao/"
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Tao/"
    accessed: 2026-10-19
    reliability_note: "Signed biography."
    used_for: [identity, basics, contribution, childhood, heritage, timing, institutions, collaborators]
  - id: S3
    type: primary
    kind: "journal article"
    author: "Ben Green and Terence Tao"
    citation: "Green, Ben, and Terence Tao. \"The primes contain arbitrarily long arithmetic progressions.\" arXiv:math/0404188 (submitted 8 April 2004); Annals of Mathematics 167 (2008): 481–547."
    url: "https://arxiv.org/abs/math/0404188"
    accessed: 2026-10-19
    reliability_note: "Abstract page read for the submission date; journal details from the Crossref record (doi:10.4007/annals.2008.167.481)."
    used_for: [basics, contribution, worldview, timing]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Terence Tao

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Terence Tao (born 1975), Australian-American mathematician, Fields Medal 2006 [S1; S2]. Draft: no worldview evidence found; everything UNKNOWN. Not plotted.

## Life and work

Adelaide, Flinders, Princeton, UCLA [S1; S2].

## Contribution and impact

Green–Tao theorem; nonlinear Schrödinger equations; Kakeya [S1; S2; S3].

## Childhood and education

Prodigy; Flinders University from age 14 [S2].

## Adult working worldview

Nothing found.

## Heritage (context only)

Chinese [S2].

## Timing

2004, at 29 [S1; S3].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Not assessed [S2].

## Open questions

- RQ-Y3, settled by ruling Y3 (not a scientist).

## Research log

- 2026-10-19: Read Britannica (Gray), MacTutor and the Green–Tao arXiv record; searched for statements on religion.
