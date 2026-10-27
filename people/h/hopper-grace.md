---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch F)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to computer_science. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch F, order P32: F 5, rank 33). Basics from Britannica and Yale News. No statement of hers on religion or on the order of nature was found. Not a scientist under P30/P33 (her lasting contributions are a manual and compilers, not theories about natural systems). All worldview fields UNKNOWN; mid_basin UNKNOWN. Draft, not reviewed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #33, next-50 batch). Needs: A UNKNOWN; B UNKNOWN. Opened Smithsonian Computer Oral History July 1968 (Merzbach; S4) and July 1972 (Luebbert/Tropp; checked for religion terms — none); Computer History Museum 1980 oral history (Pantages; S7); Mitchell 1994 UNT dissertation (S6); Wikipedia EN (S5) citing Williams 2004 for West End Collegiate family church; re-read Britannica and Yale News. P47 source_quality on every source. A stays UNKNOWN (P19): no first-person God/religion statement in S1–S7; family Collegiate Reformed church and Presbyterian girls' schools are heritage/childhood, not A. B stays UNKNOWN (P16/P33): not a scientist (lasting contributions are manual/compilers/FLOW-MATIC — devices and software, not theories about natural systems); no explicit remark on the order of nature. Childhood filled (parents; Graham/Schoonmaker/Hartridge; West End Collegiate marriage 1930). Chart: still unplotted. No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: hopper-grace
  display_name: "Grace Hopper"
  roster:
    canonical_name: "Grace Hopper"
    rank: 33
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: computer science
    field_bucket: "computer science / AI"
  full_name: {value: "Grace Brewster Murray Hopper", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts ('Née: Grace Brewster Murray'; 'Also known as')"}, {source: S5, locator: "lead / born line"}, {source: S2, locator: "title"}], how_known: "Britannica + Wikipedia + Yale News."}
  native_name: {value: UNKNOWN, how_known: "English."}
  aliases:
    - {name: "Grace-Hopper", kind: "roster alias"}
    - {name: "Hopper-Grace", kind: "roster alias"}

basics:
  birth:
    date: {value: "1906-12-09", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "title (year only)"}], how_known: "Day from Britannica alone; Yale News gives the years 1906–1992."}
    place: {value: "New York, New York, U.S.", modern_name: "New York City, United States", polity_then: "United States", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "born line"}, {source: S4, locator: "316 West 95th Street / brownstone birth"}], how_known: "Britannica + Wikipedia; oral history gives street detail."}
  death:
    date: {value: "1992-01-01", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "title (year only)"}], how_known: "Day from Britannica alone."}
    place: {value: "Arlington, Virginia, U.S.", modern_name: "Arlington, Virginia, United States", polity_then: "United States", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "Death"}, {source: S2, locator: "burial Arlington"}], how_known: "Britannica + Wikipedia + Yale News."}
  first_lasting_contribution_year: {value: 1946, certainty: 0.7, cites: [{source: S1, locator: "second paragraph (A Manual of Operation for the Automatic Sequence Controlled Calculator, 1946)"}], how_known: "Earliest listed lasting contribution (P13); Britannica alone."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S1, locator: "1946"}], how_known: "From 1946 (P2)."}
  region_of_birth: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "United States (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "United States."}
  sex_as_recorded: {value: "female", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [English], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica (US career)."}
  occupations: {value: ["mathematician", "naval officer", "computer programmer"], certainty: 0.7, cites: [{source: S1, locator: "opening; third paragraph"}], how_known: "Britannica."}

contribution:
  primary_domain: computer_science
  fields: {value: ["computer programming", "programming languages"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "A Manual of Operation for the Automatic Sequence Controlled Calculator (Harvard Mark I)", year: 1946, kind: work, lasting: "'the first extensive treatment of how to program a computer' (S1)", certainty: 0.7, cites: [{source: S1, locator: "second paragraph"}], how_known: "Britannica alone."}
    - {value: "One of the first compilers; coined the word 'compiler'", year: 1949, kind: invention, lasting: "compilers translate programmer instructions into machine code (S1)", certainty: 0.5, cites: [{source: S1, locator: "third paragraph"}], how_known: "Britannica says she joined Eckert-Mauchly in 1949 'where she designed' it; the start year of the design is not given, so 1949 is the earliest it could be and may be later (§8 undated starts). It does not move the first-lasting year, which is 1946."}
    - {value: "Flow-Matic, the first English-language data-processing compiler (her division)", year: 1957, kind: invention, lasting: "'inspired the development of COBOL' (S1)", certainty: 0.7, cites: [{source: S1, locator: "third paragraph"}], how_known: "Britannica alone."}
  evidence_of_impact:
    - {value: "National Medal of Technology, 1991; USS Hopper commissioned 1996; more than 40 honorary degrees", kind: "other", certainty: 0.7, cites: [{source: S2, locator: "paragraph on honours"}], how_known: "Yale News."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Compilers and English-like languages underlie later programming (S1).", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading. Beyer (2009), per a review, argues her role has been mythologised (not read)."}

childhood:
  family_religion: {value: "Parents attended West End Collegiate Church (Collegiate Reformed Protestant Dutch Church / Reformed Church in America tradition), New York City", certainty: 0.7, cites: [{source: S5, locator: "Early life and education (citing Williams 2004)"}, {source: S6, locator: "marriage at West End Collegiate Church, 15 June 1930"}], how_known: "Wikipedia (Williams) for parents' attendance; Mitchell for her wedding there. Not evidence of adult A (P19)."}
  family_religious_practice: {value: UNKNOWN, how_known: "Attendance named; practice intensity not detailed in S1–S7."}
  parents_and_household:
    - {value: "Walter Fletcher Murray (father; Yale B.A. 1894; insurance)", certainty: 0.7, cites: [{source: S2, locator: "daughter of Walter Fletcher Murray"}, {source: S5, locator: "Early life"}], how_known: "Yale News + Wikipedia."}
    - {value: "Mary Campbell Van Horne (mother; interested in mathematics)", certainty: 0.7, cites: [{source: S2, locator: "Mary Campbell Van Horne"}, {source: S4, locator: "mother's very great interest in mathematics"}], how_known: "Yale News + Smithsonian oral history."}
    - {value: "Sister and brother (Roger F. Murray among siblings)", certainty: 0.7, cites: [{source: S4, locator: "I have a sister and a brother"}, {source: S6, locator: "Dr. Roger Murray interview"}], how_known: "Oral history + Mitchell."}
  household_circumstances: {value: "New York City apartment (316 West 95th Street); summers in Wolfeboro, New Hampshire; house full of books", certainty: 0.7, cites: [{source: S4, locator: "316 West 95th Street; Wolfeboro; house full of books"}, {source: S2, locator: "family summered in Wolfeboro"}], how_known: "Smithsonian oral history + Yale News."}
  schooling:
    - {value: "Graham School (Misses Graham; conservative Presbyterian girls' school), New York", stage: elementary school, run_by: private, years: "1912–1916", ages: "6–10", certainty: 0.7, cites: [{source: S6, locator: "Graham School 1912–1916"}, {source: S4, locator: "Graham's School"}], how_known: "Mitchell + oral history confirmation of Graham."}
    - {value: "Miss Mary Schoonmaker's School for Girls / New York Collegiate Institute (conservative Presbyterian)", stage: "grammar or secondary school", run_by: private, years: "1916–1923", ages: "10–16", certainty: 0.7, cites: [{source: S6, locator: "Schoonmaker / Collegiate Institute"}], how_known: "Mitchell."}
    - {value: "Hartridge School, Plainfield, New Jersey", stage: "grammar or secondary school", run_by: private, years: "1923–1924", ages: "16–17", certainty: 0.7, cites: [{source: S5, locator: "Hartridge School"}, {source: S6, locator: "Hartridge"}], how_known: "Wikipedia + Mitchell."}
    - {value: "Vassar College, B.A. mathematics and physics, Phi Beta Kappa", stage: university, run_by: private, years: "1924–1928", ages: "17–22", certainty: 1.0, cites: [{source: S1, locator: "second paragraph"}, {source: S2, locator: "Vassar 1928"}, {source: S5, locator: "Vassar 1928"}], how_known: "Britannica + Yale News + Wikipedia."}
    - {value: "Yale University, M.A. 1930, Ph.D. 1934 (mathematics; adviser Øystein Ore)", stage: university, run_by: private, years: "1928–1934", ages: "22–28", certainty: 1.0, cites: [{source: S1, locator: "second paragraph"}, {source: S2, locator: "M.A. 1930; Ph.D. 1934"}, {source: S5, locator: "Yale; Ore"}], how_known: "Britannica + Yale News + Wikipedia."}
  early_mathematics: {value: "advanced mathematics", certainty: 0.7, cites: [{source: S4, locator: "mother's very great interest in mathematics; house full of books"}, {source: S1, locator: "Ph.D. mathematics"}], how_known: "Mother's math interest and path to Yale Ph.D.; enum is highest level reached. Alarm-clock curiosity is secondary (S5) — not used for the enum."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Nothing specific on proof-style geometric training in childhood sources read."}
  early_science_exposure:
    - {value: "Ancestors who had been scientists and engineers (her account)", certainty: 0.7, cites: [{source: S4, locator: "ancestors who had been scientists and engineers"}], how_known: "Smithsonian oral history (own words)."}
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [English], certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S4, locator: "later Latin/reading struggle then fluency"}], how_known: "US upbringing; oral history discusses later language learning, not childhood bilingualism."}
  notable_events:
    - {value: "Married Vincent Foster Hopper at West End Collegiate Church, New York City, 15 June 1930; divorced 1945", certainty: 0.7, cites: [{source: S6, locator: "15 June 1930 West End Collegiate"}, {source: S5, locator: "m. 1930; div. 1945"}], how_known: "Mitchell + Wikipedia. Heritage/life event, not A."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1946–1957", certainty: 0.7, cites: [{source: S1, locator: "dates"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Deepen D1: Britannica, Yale News, Wikipedia, Mitchell 1994, Smithsonian July 1968 and July 1972 oral histories, and CHM 1980 oral history (S1–S7) — no statement of hers on science and religion."}
  primary_system:
    value: UNKNOWN
    cites: [{source: S1, locator: "whole article"}, {source: S4, locator: "whole July 1968 transcript"}, {source: S7, locator: "whole 1980 transcript"}, {source: S6, locator: "dissertation (pedagogy/career; silent on personal faith)"}]
    how_known: "Deepen D1 re-read S1–S7 and web-swept for God/religion/faith/atheist/agnostic: no first-person statement. Under P19 the sources say nothing on the point, so UNKNOWN. Beyer (2009) still unread cover-to-cover; Williams 2004 Admiral of the Cyber Sea unread as full text."
    note: "Leads still open: Kurt Beyer, Grace Hopper and the Invention of the Information Age (MIT 2009); Kathleen Broome Williams, Grace Hopper: Admiral of the Cyber Sea (Naval Institute 2004) — Wikipedia cites Williams for parents' West End Collegiate attendance only."
  secondary_system: {value: UNKNOWN, how_known: "No second system in what was read."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Family Collegiate Reformed church and Presbyterian schooling are heritage/childhood, not adult profession (P19); no adult CHRIST evidence; not coded."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing of hers placing or denying God in S1–S7 (P19). Smithsonian 1968 (S4) and 1972: career, family, teaching, Mark I — no religion discussion. CHM 1980 (S7): no God/faith content (rg for religion terms empty except idiomatic 'My God'). Family West End Collegiate (S5/S6) and Presbyterian girls' schools (S6) are heritage/childhood, not A. Wedding at that church (1930) is life event, not a locus claim."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist under P30/P33: lasting contributions are the Mark I manual, early compiler/coining 'compiler', and FLOW-MATIC — devices and software, not theories or results about physical or natural systems. For a non-scientist, B needs an explicit remark on the order of nature (P16); none found in S1–S7. Oral-history remarks on teaching non-Euclidean/Einstein concepts are pedagogy, not a scored account of nature."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing of hers on judgement, reward or afterlife in S1–S7 (P19)."}
    D_authority: {value: UNKNOWN, how_known: "Nothing on revelation or scripture in S1–S7 (P19)."}
    E_scope: {value: UNKNOWN, how_known: "Not a scientist; working practice does not score E (P19/P30). No statement on same laws everywhere (P7)."}
  mid_basin: {value: UNKNOWN, how_known: "A and B are UNKNOWN, so the P4 test cannot be applied; UNKNOWN takes precedence (§6, P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "Deepen D1: A and B stay UNKNOWN after Smithsonian 1968/1972, CHM 1980, Mitchell, Wikipedia, Britannica, Yale News. Compilers remain inventions under P33 — not scientist; no B inference_from_work. Chart still unplotted. Lane B (geometric form) separate from Lane A axis scores."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Scottish and Dutch descent (parents)", certainty: 0.7, cites: [{source: S5, locator: "Early life (Scottish and Dutch descent)"}], how_known: "Wikipedia (citing Williams). Context only."}
  religious_heritage_by_birth: {value: "Collegiate Reformed Protestant (West End Collegiate Church) family attendance; Presbyterian private schooling", certainty: 0.7, cites: [{source: S5, locator: "West End Collegiate Church"}, {source: S6, locator: "conservative Presbyterian schools; wedding at West End Collegiate"}], how_known: "Wikipedia + Mitchell. Context only — not primary_system or A (P19)."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not found in S1–S7."}
  childhood_catechism: {value: UNKNOWN, how_known: "Graham School listed Bible stories in curriculum (S6); not evidence of home catechism."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1946–1957", certainty: 0.7, cites: [{source: S1, locator: "dates"}], how_known: "1946 to 1957, first to last listed lasting contribution (P29, P30). Her COBOL advocacy in the 1960s is described as promotion, not an original contribution, so it is not listed."}
  age_at_first_lasting_contribution: {value: 40, certainty: 0.7, cites: [{source: S1, locator: "opening; 1946"}], how_known: "1946 − 1906 = 40 (P30)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No statement of hers scored at 3 or 4 on A–E (P27); A and B remain UNKNOWN."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", rationale: "Nothing of hers on God or nature at the LIO-type-view bar (P27).", certainty: 0.5, cites: [{source: S1, locator: "whole article"}, {source: S4, locator: "whole July 1968 transcript"}, {source: S7, locator: "whole 1980 transcript"}], how_known: "Absence in the sources read; not evidence of absence."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "A/B UNKNOWN for the working years after deepen D1."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "Doctorate in mathematics (Yale 1934) and Vassar/Yale teaching of proof-heavy courses (finite differences, probability, solid geometry) give documented exposure to proof.", certainty: 0.5, cites: [{source: S1, locator: "second paragraph"}, {source: S4, locator: "teaching finite differences; solid geometry; non-Euclidean"}], how_known: "Coder's reading; Lane B separate from Lane A."}
  form_acquired: {value: "adulthood, before major work", certainty: 0.5, cites: [{source: S4, locator: "Vassar teaching; Yale/Courant study"}, {source: S1, locator: "Ph.D. 1934"}], how_known: "Formal mathematics training before 1946 major work; childhood geometry still thin."}
  circle_present: {value: "unclear", rationale: "No God–Nature identity statement; not a pantheist reading.", certainty: 0.5, cites: [{source: S4, locator: "whole transcript"}, {source: S1, locator: "whole article"}], how_known: "No evidence either way."}
  reading: "As belief, not finding: form partly present via mathematics doctorate; circle unclear. The record does not test H1 while A/B UNKNOWN."
  notes: "Lane B separate from Lane A axis scores (A/B UNKNOWN)."

institutions:
  - {value: "Vassar College", role: "mathematics teacher", years: "to 1943", kind: university, certainty: 0.7, cites: [{source: S1, locator: "second paragraph"}], how_known: "Britannica."}
  - {value: "Harvard University, Bureau of Ordnance Computation Project", role: "naval officer, then civilian research fellow", years: "1944–1949", kind: university, certainty: 0.7, cites: [{source: S1, locator: "second paragraph"}], how_known: "Britannica; end year is when she joined Eckert-Mauchly."}
  - {value: "Eckert-Mauchly Computer Corp. (later Remington Rand, Sperry Rand)", role: "head programmer", years: "1949–", kind: commercial, certainty: 0.7, cites: [{source: S1, locator: "third paragraph"}], how_known: "Britannica."}
collaborators: []

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 33"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "The popular claim that she was the first woman with a Yale mathematics doctorate is disputed: a Technology and Culture review of Beyer (2009) / Yale Alumni Magazine note that Charlotte Barnum and others preceded her. Not used in this record."
    - "Deepen D1: A and B remain UNKNOWN (P19/P16/P33) after Smithsonian 1968/1972, CHM 1980, Mitchell, Wikipedia, Britannica, Yale News."
    - "Beyer (2009) and Williams (2004) full texts still unread; Wikipedia uses Williams only for parents' church attendance."
    - "Yale News still has a factual-error history (Ph.D. field; Engstrom as doctoral adviser — Ore is correct per Wikipedia/AMS); used for biography/honours, not worldview."
  open_questions:
    - "Read Kurt Beyer, Grace Hopper and the Invention of the Information Age (MIT 2009) cover-to-cover for any religion or nature own-words."
    - "Read Kathleen Broome Williams, Grace Hopper: Admiral of the Cyber Sea (Naval Institute 2004) for church/faith detail beyond Wikipedia's citation."
    - "Remaining Smithsonian sessions (Nov 1968; Jan/Feb 1969) if transcripts add private-life material."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "Britannica Editors. \"Grace Hopper.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Grace-Hopper."
    url: "https://www.britannica.com/biography/Grace-Hopper"
    accessed: 2026-10-15
    reliability_note: "Article body only; the AI 'Top Questions' box is not used. Re-read 2026-10-24."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, timing, lane_b, institutions]
  - id: S2
    type: tertiary
    kind: institutional page
    author: "Yale News"
    citation: "\"Grace Murray Hopper (1906-1992): A legacy of innovation and service.\" Yale News, 10 February 2017."
    url: "https://news.yale.edu/2017/02/10/grace-murray-hopper-1906-1992-legacy-innovation-and-service"
    accessed: 2026-10-15
    reliability_note: "University news page; full article re-read 2026-10-24. Corrected Ph.D.-field error noted in page's own correction; Engstrom-as-adviser claim not used (Ore is correct)."
    source_quality: "other"
    used_for: [identity, basics, contribution, childhood]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S4
    type: primary
    kind: "other"
    author: "Grace Murray Hopper; interviewer Uta C. Merzbach"
    year: 1968
    citation: "Hopper, Grace Murray. Computer Oral History Collection interview, July 1968. Archives Center, National Museum of American History. https://www.si.edu/media/NMAH/NMAH-AC0196_hopp680700.pdf. (Related July 1972 session also opened: https://www.si.edu/media/NMAH/NMAH-AC0196_hopp720507.pdf — no religion terms.)"
    url: "https://www.si.edu/media/NMAH/NMAH-AC0196_hopp680700.pdf"
    accessed: 2026-10-24
    reliability_note: "Primary transcription of her own oral history. Used for childhood/family, teaching, Mark I, and A/B-negative (no God/religion discussion)."
    source_quality: "primary / own words"
    used_for: [identity, basics, childhood, worldview, lane_b, institutions]
  - id: S5
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia. Grace Hopper. https://en.wikipedia.org/wiki/Grace_Hopper. (Parents/West End Collegiate cites Kathleen Broome Williams, Grace Hopper: Admiral of the Cyber Sea, 2004.)"
    url: "https://en.wikipedia.org/wiki/Grace_Hopper"
    accessed: 2026-10-24
    reliability_note: "Dual-source bio; West End Collegiate parents' attendance from Williams citation. Worldview not taken from Wikipedia."
    source_quality: "other"
    used_for: [identity, basics, childhood, heritage, contribution]
  - id: S6
    type: secondary
    kind: "scholarly book"
    author: "Carmen Lois Mitchell"
    year: 1994
    citation: "Mitchell, Carmen Lois. The Contributions of Grace Murray Hopper to Computer Science and Computer Education. Ph.D. diss., University of North Texas, 1994. https://digital.library.unt.edu/ark:/67531/metadc278692/m2/1/high_res_d/1002721264-mitchell.pdf."
    url: "https://digital.library.unt.edu/ark:/67531/metadc278692/m2/1/high_res_d/1002721264-mitchell.pdf"
    accessed: 2026-10-24
    reliability_note: "Scholarly dissertation; childhood schools (Graham, Schoonmaker/Collegiate Institute, Hartridge); wedding at West End Collegiate 15 June 1930 (Roger Murray interview). Silent on adult personal faith."
    source_quality: "scholarly edition or monograph"
    used_for: [childhood, heritage, worldview]
  - id: S7
    type: primary
    kind: "other"
    author: "Grace Murray Hopper; interviewer Angeline Pantages"
    year: 1980
    citation: "Oral History of Captain Grace Hopper. Interview by Angeline Pantages, December 1980. Computer History Museum, 102702026. https://archive.computerhistory.org/resources/text/Oral_History/Hopper_Grace/102702026.05.01.pdf."
    url: "https://archive.computerhistory.org/resources/text/Oral_History/Hopper_Grace/102702026.05.01.pdf"
    accessed: 2026-10-24
    reliability_note: "Primary transcription. Career/compilers/user-friendly languages; rg for religion/God/faith terms empty except idiomatic speech. A/B-negative."
    source_quality: "primary / own words"
    used_for: [worldview, contribution]

---

# Grace Hopper

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Grace Hopper (1906–1992), American mathematician and naval officer, wrote the Mark I manual and designed early compilers / FLOW-MATIC [S1; S2; S5]. Deepen D1 (P47–P50): A and B stay UNKNOWN after Smithsonian oral histories [S4], CHM 1980 [S7], Mitchell 1994 [S6], and Wikipedia [S5] — no first-person God/religion or nature-order statements; not a scientist under P33 for B inference. Family West End Collegiate / Presbyterian schooling filled as heritage only. Still unplotted; mid_basin UNKNOWN.

## Life and work

New York childhood; Graham / Schoonmaker / Hartridge schools; Vassar and Yale; Naval Reserve from 1943; Harvard Mark I; Eckert-Mauchly and UNIVAC I; rear admiral [S1; S4; S5; S6].

## Contribution and impact

Mark I manual (1946), early compiler, Flow-Matic (1957) [S1]; National Medal of Technology [S2].

## Childhood and education

Parents Walter Fletcher Murray and Mary Campbell Van Horne; West End Collegiate Church family attendance; Presbyterian private schools; Vassar B.A. 1928; Yale Ph.D. 1934 (Ore) [S2; S4; S5; S6].

## Adult working worldview

Unknown after deepen: no own-words on God or the order of nature in Britannica, Yale News, Wikipedia, Mitchell, or the Smithsonian / CHM oral histories [S1–S7]. Compilers are inventions (P33), so B is not inferred from working practice. A UNKNOWN; B UNKNOWN; mid_basin UNKNOWN.

## Heritage (context only)

Scottish and Dutch descent; Collegiate Reformed family church; Presbyterian schooling — context only, not a worldview code [S5; S6].

## Timing

First lasting contribution 1946, at 40 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Mathematics doctorate and proof-heavy teaching → form partly; circle unclear. Separate from Lane A (A/B UNKNOWN) [S1; S4].

## Open questions

- Beyer (2009) and Williams (2004) full texts; remaining Smithsonian sessions (Nov 1968; Jan/Feb 1969).

## Research log

- 2026-10-15: Read Britannica and Yale News; web search for her religious views found nothing.
- 2026-10-24: Deepen D1 — Smithsonian July 1968 + July 1972 PDFs; CHM 1980 oral history; Mitchell 1994 UNT PDF; Wikipedia EN (Williams cite for West End Collegiate); P47 on all sources. No fallacy_catalog. A/B remain UNKNOWN.
