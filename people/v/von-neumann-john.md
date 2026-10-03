---
record:
  record_type: person
  schema_version: "1.2"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch B)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (stage 3 batch B). Basics from MacTutor. Religion from a colleague's recollection, Seeger, 'Von Neumann, Jewish Catholic' (PSCF 40, 1988): nominal Catholic after his first marriage and Catholic instruction in his last illness. No statement of his own on religion was read, and no recorded interview of him on religion was found (the P8 interview route is unavailable). primary_system BELOW_THRESHOLD. B 4 (0.5) from working science; A, C, D, E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. All scores are drafts for v8's review. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit fix, stage 3 batch B (two blind runs at 3db6511). #352: full_name now follows MacTutor ('born János von Neumann'); the earlier 'born János Neumann' is kept only as a marked inference from the 1913 title. Not reviewed."}

identity:
  id: von-neumann-john
  display_name: "John von Neumann"
  roster:
    canonical_name: "John von Neumann"
    rank: 47
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: mathematics
    field_bucket: mathematics
  full_name: {value: "John von Neumann (born János von Neumann)", certainty: 0.7, cites: [{source: S1, locator: "Biography, paragraphs 1–2 ('John von Neumann was born János von Neumann')"}], how_known: "MacTutor's wording, reopened 2026-10-02. MacTutor also says his father bought the title in 1913, ten years after the birth, so his name at birth was probably János Neumann; that is the coder's inference, not stated in the source."}
  native_name: {value: "Neumann János (Hungarian)", certainty: 0.5, cites: [{source: S1, locator: "Biography, paragraph 1"}], how_known: "MacTutor gives János; the Hungarian name order is the coder's rendering."}
  aliases:
    - {name: "John-von-Neumann", kind: "roster alias"}
    - {name: "Von Neumann-John", kind: "roster alias"}
    - {name: "János von Neumann", kind: "birth name"}
    - {name: "Johnny", kind: other}

basics:
  birth:
    date: {value: "1903-12-28", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "Quick Info"}], how_known: "MacTutor; Seeger gives the year 1903 only (S2)."}
    place: {value: "Budapest", modern_name: "Budapest, Hungary", polity_then: "Austria-Hungary (Kingdom of Hungary)", certainty: 1.0, cites: [{source: S1, locator: "Quick Info"}, {source: S2, locator: "paragraph 2"}], how_known: "Two sources agree."}
  death:
    date: {value: "1957-02-08", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "Quick Info"}], how_known: "MacTutor."}
    place: {value: "Washington, D.C. (Walter Reed Army Hospital)", modern_name: "Washington, D.C., USA", polity_then: "United States", certainty: 1.0, cites: [{source: S1, locator: "Quick Info"}, {source: S2, locator: "last paragraph"}], how_known: "Two sources (Seeger names the hospital)."}
  first_lasting_contribution_year: {value: 1923, certainty: 0.5, cites: [{source: S1, locator: "Biography ('He published a definition of ordinal numbers when he was 20')"}], how_known: "Definition of the ordinal numbers, 'the one used today'; MacTutor gives his age (20), not the year, so 1923 or 1924. Draft judgment (one line): the ordinals are taken as first lasting work rather than the 1922 paper with Fekete."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "Biography"}], how_known: "Any candidate year (1922–1926) falls in 1850–1949 (P2)."}
  region_of_birth: {value: "Eastern Europe", certainty: 1.0, cites: [{source: S1, locator: "Quick Info"}], how_known: "Hungary is Eastern Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "North America", certainty: 1.0, cites: [{source: S1, locator: "Biography (1930–1957)"}], how_known: "Princeton and Washington from 1930; Berlin, Hamburg and Göttingen (Western Europe) 1926–1930."}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S1, locator: "Biography"}], how_known: "As the sources record it."}
  languages_of_work: {value: [German, English], certainty: 0.7, cites: [{source: S1, locator: "Biography (Mathematische Grundlagen der Quantenmechanik, 1932; Theory of Games, 1944)"}], how_known: "Titles of his works in MacTutor."}
  occupations: {value: ["mathematician", "physicist", "computer pioneer", "government scientific adviser"], certainty: 1.0, cites: [{source: S1, locator: "Summary; Biography"}, {source: S2, locator: "paragraphs 4–5"}], how_known: "Two sources."}

contribution:
  fields: {value: ["set theory", "operator theory", "quantum mechanics", "game theory", "hydrodynamics", "computer science"], certainty: 1.0, cites: [{source: S1, locator: "Summary; Biography"}, {source: S2, locator: "paragraphs 7–8"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Definition of the ordinal numbers", year: "1923", kind: "concept or term", lasting: "the definition used today", certainty: 0.7, cites: [{source: S1, locator: "Biography (doctorate paragraph)"}], how_known: "MacTutor."}
    - {value: "Rigorous Hilbert-space framework for quantum mechanics (Mathematische Grundlagen der Quantenmechanik)", year: "1932", kind: theory, lasting: "standard framework", certainty: 1.0, cites: [{source: S1, locator: "Biography (1932)"}, {source: S2, locator: "paragraph 7"}], how_known: "Two sources."}
    - {value: "Rings of operators (von Neumann algebras)", year: "1930s–1940s", kind: theory, lasting: "named after him", certainty: 0.7, cites: [{source: S1, locator: "Biography (operator algebras)"}], how_known: "MacTutor."}
    - {value: "Minimax theorem and the theory of games (with Morgenstern, 1944)", year: "1928", kind: theory, lasting: "foundation of game theory", certainty: 1.0, cites: [{source: S1, locator: "Biography (game theory)"}, {source: S2, locator: "paragraph 8"}], how_known: "Two sources."}
    - {value: "Implosion method for the atomic bomb", year: "1943–1945", kind: method, lasting: "nuclear weapons design", certainty: 1.0, cites: [{source: S1, locator: "Biography (war work)"}, {source: S2, locator: "paragraph 10"}], how_known: "Two sources."}
  evidence_of_impact:
    - {value: "Enrico Fermi Award, 1956", kind: "honours in lifetime", certainty: 1.0, cites: [{source: S1, locator: "Biography (1956)"}, {source: S2, locator: "paragraph 12"}], how_known: "Two sources."}
  major_works:
    - {value: "Mathematische Grundlagen der Quantenmechanik", year: 1932, kind: book, certainty: 1.0, cites: [{source: S1, locator: "Biography (1932)"}, {source: S2, locator: "paragraph 3"}], how_known: "Two sources."}
    - {value: "Theory of Games and Economic Behavior (with Oskar Morgenstern)", year: 1944, kind: book, certainty: 1.0, cites: [{source: S1, locator: "Biography (game theory)"}, {source: S2, locator: "paragraph 4"}], how_known: "Two sources."}
  honours:
    - {value: "Enrico Fermi Award", year: 1956, certainty: 1.0, cites: [{source: S1, locator: "Biography (1956)"}, {source: S2, locator: "paragraph 12"}], how_known: "Two sources."}
    - {value: "Medal for Merit", year: 1947, certainty: 0.7, cites: [{source: S1, locator: "honours paragraph"}], how_known: "MacTutor."}
  definition_fit: {value: "clearly meets", rationale: "Founder of the mathematical framework of quantum mechanics and of game theory; computer architecture pioneer.", certainty: 1.0, cites: [{source: S1, locator: "Summary"}], how_known: "Sources agree."}

childhood:
  family_religion: {value: "Jewish, non-observant; the household 'seemed to mix Jewish and Christian traditions'", certainty: 0.7, cites: [{source: S1, locator: "Biography, paragraph 1"}], how_known: "MacTutor: 'Although the family were Jewish, Max Neumann did not observe the strict practices of that religion and the household seemed to mix Jewish and Christian traditions.'"}
  family_religious_practice: {value: "Non-observant", certainty: 0.7, cites: [{source: S1, locator: "Biography, paragraph 1"}], how_known: "MacTutor."}
  parents_and_household:
    - {value: "Father, Max Neumann, banker, ennobled in 1913", name: "Max Neumann", role: father, certainty: 1.0, cites: [{source: S1, locator: "Biography, paragraphs 1–2"}, {source: S2, locator: "paragraph 2"}], how_known: "Two sources."}
    - {value: "Mother, Margaret Kann", name: "Margaret Neumann (née Kann)", role: mother, certainty: 0.7, cites: [{source: S2, locator: "paragraph 2"}], how_known: "Seeger."}
  household_circumstances: {value: "Wealthy Budapest family; governesses; two younger brothers", certainty: 1.0, cites: [{source: S1, locator: "Biography, paragraph 1"}, {source: S2, locator: "paragraph 2"}], how_known: "Two sources."}
  schooling:
    - {value: "Lutheran Gymnasium, Budapest", stage: "religious school", years: "1911–1921", certainty: 1.0, cites: [{source: S1, locator: "Biography (1911, 1921)"}, {source: S2, locator: "paragraph 2"}], how_known: "Two sources. MacTutor: academic tradition counted for more than religious affiliation."}
    - {value: "University of Budapest (mathematics, examinations only), Berlin (chemistry) and ETH Zürich (chemical engineering diploma 1926); Budapest doctorate in set theory 1926", stage: university, years: "1921–1926", certainty: 1.0, cites: [{source: S1, locator: "Biography (1921–1926)"}, {source: S2, locator: "paragraph 2"}], how_known: "Two sources."}
  early_mathematics: {value: "advanced mathematics", note: "Special tuition at the Gymnasium; first paper with Fekete in 1922 (MacTutor).", certainty: 1.0, cites: [{source: S1, locator: "Biography (1911, 1921–22)"}, {source: S2, locator: "paragraph 2"}], how_known: "Two sources."}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "Michael Fekete, tutor and co-author of his first paper", name: "Michael Fekete", certainty: 0.7, cites: [{source: S1, locator: "Biography (1921–22)"}], how_known: "MacTutor (Seeger names Fejér as tutor instead)."}
  languages_in_childhood: {value: [Hungarian, German, French], certainty: 0.7, cites: [{source: S1, locator: "Biography, paragraph 1"}], how_known: "MacTutor: languages from German and French governesses; Hungarian assumed from Budapest (coder)."}
  notable_events:
    - {value: "Family fled briefly to Austria during Béla Kun's Communist government", year: "1919", age: 15, certainty: 0.7, cites: [{source: S1, locator: "Biography (1919)"}], how_known: "MacTutor."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1926–1957", certainty: 1.0, cites: [{source: S1, locator: "Biography"}], how_known: "From the doctorate to his death."}
  nominal_affiliations:
    - {value: "Roman Catholic, presumably nominal, from about his first marriage to a Catholic wife (Marietta Kövesi)", years: "c. 1930–", certainty: 0.5, cites: [{source: S2, locator: "last paragraph"}, {source: S1, locator: "Biography (marriage before leaving for Princeton, 1930)"}], how_known: "Seeger: 'his first wife had been Catholic. I presume that he was a nominal one in those early days of his marriage.' A colleague's presumption, so 0.5. Seeger dates the marriage to the year of the IAS appointment; MacTutor puts it before the 1930 move to Princeton (flag)."}
    - {value: "Catholic burial service at Walter Reed Army Hospital; buried in Princeton", year: 1957, certainty: 0.7, cites: [{source: S2, locator: "last paragraph"}], how_known: "Seeger attended the service."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No statement of his on science and religion was read. Seeger: 'we never discussed religion' and 'he showed little interest in the philosophical aspects of quantum mechanics' (S2)."}
  primary_system:
    value: BELOW_THRESHOLD
    cites: [{source: S2, locator: "last paragraph"}]
    how_known: "Only a colleague's recollection was read: 'Some people claim that von Neumann was an agnostic', but 'he died a Roman Catholic', having asked for a priest and received instruction in his last illness (S2). Nothing in his own words. The often-quoted 'There probably has to be a God' and Pascal's-wager remarks reach us only through later secondary reports and were not traced to a source read."
    note: "Draft judgment (one line): BELOW_THRESHOLD because there is no first-hand statement and the two candidates point in opposite directions. No recorded interview of von Neumann on religion was found, so the P8 interview route is not available; the oral histories about him (e.g. his daughter Marina Whitman's) are other people's reports and were not opened."
  secondary_system: {value: UNKNOWN, how_known: "No system evidence beyond Seeger."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Considered: nominal Catholic after his first marriage, Catholic instruction (a Benedictine, then a Jesuit) and burial at the end of his life (S2). A deathbed turn reported by a colleague is not the adult working worldview. CHRIST is a draft.", cites: [{source: S2, locator: "last paragraph"}]}
    - {code: AGNOS, reason: "Considered: 'Some people claim that von Neumann was an agnostic' (S2), unattributed. AGNOS is a stub system file (flag).", cites: [{source: S2, locator: "last paragraph"}]}
    - {code: JUDA, reason: "Rejected: Jewish family heritage, non-observant (S1). Heritage is never a code.", cites: [{source: S1, locator: "Biography, paragraph 1"}]}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "Nothing read on God in his own words."}
    B_cause:
      value: 4
      basis: scholarly_reconstruction
      certainty: 0.5
      cites: [{source: S1, locator: "Biography (1932; hydrodynamics; war work)"}, {source: S2, locator: "paragraphs 7–9"}]
      how_known: "Coder's reading of his working science (P6), as for Dirac and Fermi; no statement of his own on miracles, so 0.5."
      rationale: "Scored on his account of nature (P6). He gave quantum mechanics a rigorous Hilbert-space form (S1), worked on the equations of hydrodynamics and shocks, and searched 'how nature itself solves nonlinear equations' (Seeger, S2): mathematical law throughout, with no miracle, petition or exemption in anything read. Named alternative: BELOW_THRESHOLD, since about 130 of his 150 papers were pure mathematics (S2) and no worldview statement was read."
    C_ledger: {value: BELOW_THRESHOLD, how_known: "Nothing in his own words on judgement or afterlife. Wigner's recollection, quoted by MacTutor, that his logic 'forced him to realise that he would cease to exist' (S1) and the deathbed Catholic instruction (S2) are other people's reports and point different ways."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "Nothing read on revelation or scripture. Reciting the Penitential Psalms in Latin (reported by an Air Force chaplain to Seeger, S2) is practice, not a view of authority."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Scored on the world's order (P7). Nothing read addresses favour for a group in events."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD and B_cause is only 0.5."}
  statements: []
  changes_over_life:
    - {value: "From non-observant Jewish upbringing to nominal Catholicism around his first marriage", year: "c. 1930", certainty: 0.5, cites: [{source: S1, locator: "Biography, paragraph 1"}, {source: S2, locator: "last paragraph"}], how_known: "MacTutor for the family; Seeger's presumption for the Catholic affiliation."}
    - {value: "In his last illness he asked for a Roman Catholic priest and received instruction from a Benedictine, then a Jesuit", year: "1956–1957", certainty: 0.5, cites: [{source: S2, locator: "last paragraph"}], how_known: "A colleague's recollection, partly second-hand (the chaplain's report)."}
  coder_notes: "AGNOS is a stub system file (flag); CHRIST and JUDA are drafts or sourced files used only as candidates. Interviews: no recorded interview of von Neumann on religion was found, so decision P8's recorded_interview basis cannot be used; interviews about him (e.g. Marina von Neumann Whitman's oral histories) were not opened (one Atomic Heritage URL returned 404) and would be reported speech in any case. Seeger quotes his essay 'The Mathematician' (1947): 'The most vitally characteristic fact about mathematics is, in my opinion, its quite peculiar relationship to the natural sciences' (secondary quotation; the essay itself was not read). statements is empty because nothing of his own on religion was read. Seeger's article was read through the fetch tool only (direct download blocked by the server)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Hungarian Jewish", certainty: 1.0, cites: [{source: S1, locator: "Biography, paragraph 1; Budapest quota paragraph"}, {source: S2, locator: "paragraphs 1, 6"}], how_known: "Two sources."}
  religious_heritage_by_birth: {value: "Jewish", certainty: 0.7, cites: [{source: S1, locator: "Biography, paragraph 1"}], how_known: "MacTutor."}
  baptism_or_initiation: {value: TODO, note: "A Catholic baptism is implied by Seeger's 'nominal' Catholicism but no date or record was read."}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1923–1955", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "Ordinals to computing and the AEC (coder's span)."}
  age_at_first_lasting_contribution: {value: 20, certainty: 0.7, cites: [{source: S1, locator: "Biography (ordinals 'when he was 20')"}], how_known: "MacTutor gives the age."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No worldview statement found."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", rationale: "Nothing read in his own words.", certainty: 0.5, cites: [{source: S2, locator: "last paragraph"}], how_known: "Absence in what was read; not evidence of absence."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "'His general approach was from the standpoint of axiomatization' (Seeger, S2).", certainty: 0.5, cites: [{source: S2, locator: "paragraph 7"}], how_known: "A colleague's characterisation."}
  form_acquired: {value: "childhood or adolescence", certainty: 0.5, cites: [{source: S1, locator: "Biography (Gymnasium; 1922 paper)"}], how_known: "Advanced mathematics before 18."}
  circle_present: {value: "unclear", rationale: "No God–Nature statement read.", certainty: 0.5, cites: [{source: S2, locator: "last paragraph"}], how_known: "No evidence either way."}
  reading: "As belief, not finding: form present, circle unclear. The record does not test H1."
  notes: ""

institutions:
  - {value: "Institute for Advanced Study, Princeton", role: "one of the original six mathematics professors", years: "1933–1957", kind: university, certainty: 1.0, cites: [{source: S1, locator: "Biography (1933)"}, {source: S2, locator: "paragraph 3"}], how_known: "Two sources."}
  - {value: "Los Alamos Scientific Laboratory", role: consultant, years: "1943–1955", kind: "government or state body", certainty: 0.7, cites: [{source: S1, locator: "Biography (war work)"}], how_known: "MacTutor."}
  - {value: "U.S. Atomic Energy Commission", role: commissioner, years: "1955–1957", kind: "government or state body", certainty: 1.0, cites: [{source: S1, locator: "Biography (1955)"}, {source: S2, locator: "paragraph 5"}], how_known: "Two sources."}
collaborators:
  - {value: "Oskar Morgenstern", relation: collaborator, note: "Theory of Games (1944)", certainty: 1.0, cites: [{source: S1, locator: "Biography (game theory)"}, {source: S2, locator: "paragraph 4"}], how_known: "Two sources."}
  - {value: "David Hilbert", relation: "influenced by", note: "studied under him at Göttingen 1926–27", certainty: 1.0, cites: [{source: S1, locator: "Biography (1926–27)"}, {source: S2, locator: "paragraph 2"}], how_known: "Two sources."}
  - {value: "Raymond J. Seeger", relation: collaborator, note: "shock-wave work; author of S2", certainty: 0.7, cites: [{source: S2, locator: "paragraph 9"}], how_known: "Seeger's own statement."}

review:
  roster_status_reason: {value: "Core in v8 (F 5: Claude, DeepSeek, Gemini, GPT, Grok).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 47"}], how_known: "Study roster."}
  controversies:
    - {value: "Whether he was agnostic or Catholic: Seeger reports both the claim of agnosticism and his Catholic death", certainty: 0.5, cites: [{source: S2, locator: "last paragraph"}], how_known: "One colleague's recollection."}
  data_quality_flags:
    - "First marriage: before the 1930 move to Princeton (MacTutor) vs the year of the IAS appointment (Seeger)."
    - "Tutor: Fekete (MacTutor) vs Fejér (Seeger)."
    - "No primary statement on religion; the famous wager remarks are unsourced in what was read."
    - "Britannica was not read for von Neumann."
  open_questions:
    - "Find a first-hand source for the deathbed conversion (e.g. the priest's or family's written account) and the 1947 essay 'The Mathematician'."
    - "Open Marina von Neumann Whitman's oral histories for reported statements (would stay reported speech)."

sources:
  - id: S1
    type: secondary
    kind: "institutional page"
    author: "J J O'Connor and E F Robertson"
    citation: "O'Connor, J. J., and E. F. Robertson. \"John von Neumann.\" MacTutor History of Mathematics, University of St Andrews. https://mathshistory.st-andrews.ac.uk/Biographies/Von_Neumann/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Von_Neumann/"
    accessed: 2026-10-02
    reliability_note: "Biography; cited by paragraph description."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: secondary
    kind: "journal article"
    author: "Raymond J. Seeger"
    year: 1988
    citation: "Seeger, Raymond J. \"Von Neumann, Jewish Catholic.\" Perspectives on Science and Christian Faith 40 (December 1988): 234–236. https://www.asa3.org/ASA/PSCF/1988/PSCF12-88Seeger.html."
    url: "https://www.asa3.org/ASA/PSCF/1988/PSCF12-88Seeger.html"
    accessed: 2026-10-02
    reliability_note: "Short memoir by a colleague (shock-wave collaborator), on the journal's own site; paragraphs counted from 'John von Neumann's life was a paradox'. His religious information is partly second-hand (the chaplain)."
    used_for: [basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators, review]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
---

# John von Neumann

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

John von Neumann (1903–1957), Hungarian-American mathematician, gave quantum mechanics its Hilbert-space form, founded game theory and helped design the implosion bomb and early computers [S1; S2]. Born into a non-observant Jewish family [S1], he was, according to a colleague, a nominal Catholic after his first marriage and asked for a Catholic priest in his last illness [S2]. No statement of his own on religion was read, and no recorded interview of him on religion exists in what was searched. primary_system BELOW_THRESHOLD; B 4 (0.5) from working science; A, C, D, E below threshold; mid_basin below threshold.

## Life and work

Lutheran Gymnasium in Budapest, chemistry in Berlin and Zürich, a Budapest doctorate in set theory (1926), Göttingen, Berlin and Hamburg, then Princeton from 1930 and the IAS from 1933; Los Alamos consultant and AEC commissioner [S1; S2].

## Contribution and impact

Ordinals, the mathematical foundations of quantum mechanics (1932), operator algebras, the minimax theorem (1928) and game theory (1944), hydrodynamics and computing [S1; S2].

## Childhood and education

Wealthy Budapest banking family; the household "seemed to mix Jewish and Christian traditions" [S1, Biography, paragraph 1].

## Adult working worldview

Not established from his own words. Seeger: "Some people claim that von Neumann was an agnostic. I must confess that we never discussed religion" [S2].

## Heritage (context only)

Hungarian Jewish, non-observant [S1]. Context only.

## Timing

First lasting contribution about 1923 (ordinals, at 20) [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form present (axiomatization [S2]); circle unclear.

## Open questions

- A first-hand account of the deathbed conversion; the 1947 essay 'The Mathematician'.

## Research log

- 2026-10-02: Read MacTutor and Seeger (1988, via the fetch tool; direct download blocked). Searched for recorded interviews of von Neumann on religion: none found. The 'probably has to be a God' and wager quotes were seen only in secondary pages and not used.
