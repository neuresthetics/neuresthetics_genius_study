---
record:
  record_type: person
  schema_version: "1.2"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, fourth batch: physical science 1600–1950)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (fourth batch, RUNBOOK §1 order). Basics from Britannica (Paradowski, first page) and the Nobel biography. Worldview from his own speech 'Humanism and Peace' (American Humanist Association, 17 March 1961) and his letter of 23 January 1963 to Mrs. Eubert J. Daniel, both in the transcriptions of Oregon State University's Pauling Papers. No interview used. primary_system SECHUM at 0.7 (stub; ATHE named, stub). A 4, B 4, C 4, D 4, E 4, all at 0.7; mid_basin false (0.7). Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Decision P10 (lens audit batch 3, #25): mid_basin how_known reworded; the A ≥ 3 branch reads A only, so certainty is A's (0.7). Value and certainty unchanged. Not reviewed."}

identity:
  id: pauling-linus
  display_name: "Linus Pauling"
  roster:
    canonical_name: "Linus Pauling"
    rank: 200
    F: 3
    models: [Claude, DeepSeek, Gemini]
    band: "core (3–4)"
    status: core
    field: chemistry
    field_bucket: chemistry
  full_name: {value: "Linus Carl Pauling", certainty: 0.7, cites: [{source: S2, locator: "paragraph 1"}], how_known: "Nobel biography."}
  native_name: {value: "Linus Pauling (English)", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "English name."}
  aliases:
    - {name: "Pauling-Linus", kind: "roster alias"}

basics:
  birth:
    date: {value: "1901-02-28", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "paragraph 1"}], how_known: "Two sources agree."}
    place: {value: "Portland, Oregon", modern_name: "Portland, Oregon, USA", polity_then: "United States", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "paragraph 1"}], how_known: "Two sources agree."}
  death:
    date: {value: "1994-08-19", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "closing note"}], how_known: "Two sources agree."}
    place: {value: "Big Sur, California", modern_name: "Big Sur, California, USA", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1925, certainty: 0.5, cites: [{source: S1, locator: "'Early life and education'"}, {source: S2, locator: "paragraph 3"}], how_known: "His X-ray crystal-structure papers, begun with Dickinson in 1922, formed his 1925 PhD; which early paper first lasted is the coder's judgement."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S2, locator: "paragraph 3"}], how_known: "From first_lasting_contribution_year (P2); any candidate year (1922–1931) is in this bucket."}
  region_of_birth: {value: "North America", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "USA is North America in data/reference/regions.csv (P3)."}
  region_of_work: {value: "North America", certainty: 1.0, cites: [{source: S2, locator: "paragraph 4"}], how_known: "Caltech, 1922 on."}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "As the sources record it."}
  languages_of_work: {value: [English], certainty: 1.0, cites: [{source: S2, locator: "paragraph 5"}], how_known: "His books are in English."}
  occupations: {value: ["chemist", "university professor", "peace activist"], certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "paragraphs 4–5"}], how_known: "Two sources."}

contribution:
  fields: {value: ["structural chemistry", "quantum chemistry", "molecular biology"], certainty: 1.0, cites: [{source: S1, locator: "'Elucidation of molecular structures'"}, {source: S2, locator: "paragraph 6"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Nature of the chemical bond: valence-bond theory with resonance and hybrid bonds; electronegativity scale", year: "1930s", kind: theory, lasting: "Nobel Prize in Chemistry 1954", certainty: 1.0, cites: [{source: S1, locator: "'Elucidation of molecular structures', paragraphs 1–2"}, {source: S2, locator: "paragraphs 3, 6"}], how_known: "Two sources."}
    - {value: "Sickle-cell anemia as the first 'molecular disease'", year: "1949", kind: discovery, lasting: "founding case of molecular medicine", certainty: 1.0, cites: [{source: S1, locator: "sickle-cell paragraph"}], how_known: "Britannica."}
    - {value: "Alpha helix of proteins", year: "1948–1951", kind: discovery, lasting: "standard protein structure", certainty: 0.7, cites: [{source: S1, locator: "Oxford 1948 paragraph"}], how_known: "Britannica gives the 1948 discovery; publication year not on the page read."}
  evidence_of_impact:
    - {value: "Only person to have won two unshared Nobel Prizes", kind: "honours in lifetime", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works:
    - {value: "The Nature of the Chemical Bond, and the Structure of Molecules and Crystals", year: 1939, kind: book, certainty: 1.0, cites: [{source: S1, locator: "'Elucidation of molecular structures', paragraph 2"}, {source: S2, locator: "paragraph 5"}], how_known: "Two sources."}
    - {value: "General Chemistry", year: 1947, kind: book, certainty: 0.7, cites: [{source: S2, locator: "paragraph 5"}], how_known: "Nobel biography."}
    - {value: "No More War!", year: 1958, kind: book, certainty: 0.7, cites: [{source: S2, locator: "paragraph 5"}], how_known: "Nobel biography."}
  honours:
    - {value: "Nobel Prize in Chemistry", year: 1954, certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    - {value: "Nobel Peace Prize (for 1962)", year: 1962, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "paragraph 4 ('In 1963, he was awarded the Nobel Peace Prize')"}], how_known: "Two sources: the prize for 1962 was awarded in 1963."}
    - {value: "Humanist of the Year (American Humanist Association)", year: 1961, certainty: 1.0, cites: [{source: S2, locator: "paragraph 5"}, {source: S3, locator: "itinerary entry"}], how_known: "Two sources."}
    - {value: "Rationalist of the Year", year: 1960, certainty: 0.7, cites: [{source: S2, locator: "paragraph 5"}], how_known: "Nobel biography."}
  definition_fit: {value: "clearly meets", rationale: "Founder of modern structural chemistry; two unshared Nobel Prizes.", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "Protestant: paternal grandparents Lutheran; he believed he was baptized in the Congregational Church", certainty: 0.7, cites: [{source: S4, locator: "letter, paragraph 1"}], how_known: "His own letter (one source; 'I believe that I was baptized')."}
  family_religious_practice: {value: "He attended various Sunday schools as a boy", certainty: 0.7, cites: [{source: S4, locator: "letter, paragraph 1"}], how_known: "His own letter."}
  parents_and_household:
    - {value: "Father, Herman Henry William Pauling, a druggist born in Missouri, of German descent", name: "Herman Pauling", role: father, certainty: 1.0, cites: [{source: S2, locator: "paragraph 1"}, {source: S1, locator: "'Early life and education'"}], how_known: "Two sources."}
    - {value: "Mother, Lucy Isabelle Darling, born in Oregon of English-Scottish ancestry, a pharmacist's daughter", name: "Lucy Isabelle Pauling (née Darling)", role: mother, certainty: 1.0, cites: [{source: S2, locator: "paragraph 1"}, {source: S1, locator: "'Early life and education'"}], how_known: "Two sources."}
  household_circumstances: {value: "First of three children and only son", certainty: 0.7, cites: [{source: S1, locator: "'Early life and education'"}], how_known: "Britannica."}
  schooling:
    - {value: "Public elementary and high schools in Condon and Portland, Oregon", stage: "grammar or secondary school", years: "–1917", certainty: 1.0, cites: [{source: S2, locator: "paragraph 2"}, {source: S1, locator: "'Early life and education'"}], how_known: "Two sources."}
    - {value: "Oregon Agricultural (State) College: BSc in chemical engineering 1922; full-time teacher of quantitative analysis 1919–20", stage: university, years: "1917–1922", certainty: 1.0, cites: [{source: S2, locator: "paragraph 2"}, {source: S1, locator: "'Early life and education'"}], how_known: "Two sources."}
    - {value: "California Institute of Technology: PhD 1925 under Roscoe G. Dickinson and Richard C. Tolman", stage: university, years: "1922–1925", certainty: 1.0, cites: [{source: S2, locator: "paragraph 2"}, {source: S1, locator: "'Early life and education'"}], how_known: "Two sources."}
  early_mathematics: {value: TODO, note: "PhD minors in physics and mathematics (S2); earlier mathematics not stated."}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure:
    - {value: "From 1919, papers by Irving Langmuir on the Lewis electron-pair bond", certainty: 1.0, cites: [{source: S2, locator: "paragraph 3"}], how_known: "Nobel biography."}
  key_early_reading:
    - {value: "Irving Langmuir's papers on the shared electron pair", certainty: 1.0, cites: [{source: S2, locator: "paragraph 3"}], how_known: "Nobel biography."}
  childhood_mentors: []
  languages_in_childhood: {value: [English], certainty: 1.0, cites: [{source: S2, locator: "paragraph 1"}], how_known: "Born in Oregon."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1922–1994", certainty: 1.0, cites: [{source: S2, locator: "paragraphs 2–4"}], how_known: "Caltech graduate work to death."}
  nominal_affiliations:
    - {value: "American Humanist Association (member)", years: "–1963", role: "member", certainty: 1.0, cites: [{source: S4, locator: "letter, paragraph 1"}, {source: S3, locator: "speech heading and itinerary"}], how_known: "His own letter; his 1961 speech to the AHA, where he received its Humanist of the Year award."}
    - {value: "First Unitarian Church of Los Angeles ('accepts atheists as members'; joined 'to help with' its support of morality and ethics)", years: "1962–", role: "member", certainty: 0.7, cites: [{source: S4, locator: "letter, paragraph 1"}], how_known: "His own letter (one source)."}
  self_described_science_religion_relation:
    value: "Humanism as 'a rational philosophy' that rejects 'the mysticism and supernaturalism of the revealed religions', life after death, and a god who interferes 'with the ordered regularity of events as determined by natural laws'; he broke away from church affiliation when he 'began to think for myself and to become skeptical about dogmatic statements'."
    certainty: 0.7
    cites: [{source: S3, locator: "speech, paragraph on humanism"}, {source: S4, locator: "letter, paragraph 1"}]
    how_known: "His own speech and letter; 0.7 because the speech states what humanism 'as I understand it' holds, which he endorses but phrases through the movement."
  primary_system:
    value: SECHUM
    basis: written_profession
    certainty: 0.7
    cites: [{source: S3, locator: "speech, paragraph on humanism"}, {source: S4, locator: "letter, paragraph 1"}]
    how_known: "His own words: 'I believe that there is great value in the philosophy of humanism' (S3); 'I am a Humanist—a member of the American Humanist Association' (S4); speech given to the AHA on receiving its Humanist of the Year award."
    rationale: "SECHUM: v7.1's rule sends a person to SECHUM 'if the public identity is humanist movement rather than metaphysics' (CODING_GUIDE §1). His public identity is the humanist movement (AHA member, Humanist of the Year, 'Humanism and Peace'). Named alternative: ATHE, since he also writes 'I do not believe in God' (S4) and his humanism rejects the supernatural outright (S3), which is positive naturalism. SECHUM and ATHE are stub system files (flag)."
  secondary_system: {value: UNKNOWN, how_known: "No second system; Unitarian membership is an affiliation, not a second published system."}
  candidate_codes_considered:
    - {code: SECHUM, reason: "Coded at 0.7: self-described Humanist, AHA member and award winner; speech on humanism. Stub system file (flag).", cites: [{source: S3, locator: "speech"}, {source: S4, locator: "letter"}]}
    - {code: ATHE, reason: "Named alternative: 'I do not believe in God'; rejection of the supernatural. Stub system file (flag).", cites: [{source: S4, locator: "letter, paragraph 1"}, {source: S3, locator: "speech, paragraph on humanism"}]}
    - {code: CHRIST, reason: "Rejected: childhood Sunday schools and a probable Congregational baptism are upbringing; he 'broke away from church affiliation', and he states the Unitarian church he joined is 'not Christian'.", cites: [{source: S4, locator: "letter, paragraph 1"}]}
  lio_axes:
    A_locus:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S4, locator: "letter, paragraph 1"}, {source: S3, locator: "speech, paragraph on humanism"}]
      how_known: "His own letter and speech; the denial of God is in a letter signed for him by his secretary (S4), so 0.7."
      rationale: "No God beyond the world, so at the LIO pole as for other atheist and humanist records (Chandrasekhar): 'I do not believe in God' (S4); humanism rejects 'a belief in an omniscient, omnipotent, and omnipresent god who watches over and cares for human beings' (S3)."
    B_cause:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S3, locator: "speech, paragraph on humanism"}]
      how_known: "His own speech, phrased as what humanism holds; 0.7 (indirect)."
      rationale: "Scored on his account of nature (P6). He rejects a god 'interfering, sometimes in response to prayer, with the ordered regularity of events as determined by natural laws'. Law and regularity, no miracle or petition; his working chemistry is lawful structural science (S1)."
    C_ledger:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S3, locator: "speech, paragraph on humanism"}]
      how_known: "His own speech, phrased as what humanism holds; 0.7."
      rationale: "No ledger: humanism 'rejects life after death and the idea that suffering in this world may, for the righteous, be compensated for by the bliss of an after-life'. The moral community is 'all humanity' (scored here, not on E)."
    D_authority:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S3, locator: "speech, paragraph on humanism"}, {source: S4, locator: "letter, paragraph 1"}]
      how_known: "His own speech and letter; 0.7."
      rationale: "Observation and reason outrank revelation: humanism 'is a rational philosophy' that 'rejects the mysticism and supernaturalism of the revealed religions' (S3); he left the church when he became 'skeptical about dogmatic statements' (S4)."
    E_scope:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S3, locator: "speech, paragraph on humanism"}]
      how_known: "His own speech; 0.7."
      rationale: "Scored on the world's order (P7). No hidden exceptions: he rejects a god who intervenes in events 'in response to prayer'; events follow 'the ordered regularity [...] determined by natural laws' for all. The scope of the moral community ('all humanity') is scored on C."
  mid_basin:
    value: false
    certainty: 0.7
    cites: [{source: S4, locator: "letter, paragraph 1"}, {source: S3, locator: "speech, paragraph on humanism"}]
    how_known: "P4 test: A_locus = 4 (≥ 3) at 0.7, so false. Certainty is A's (0.7): the A ≥ 3 branch reads A only (decision P10)."
  statements:
    - text: "I believe that there is great value in the philosophy of humanism -- that the chief end of human life is to work for the happiness of man upon this earth (and we might soon have to add the moon and then Venus and other planets)."
      cites: [{source: S3, locator: "speech, paragraph on humanism"}]
      date: "1961-03-17"
      context: "'Humanism and Peace', speech to the annual meeting of the American Humanist Association, Cleveland, Ohio, on receiving its Humanist of the Year award."
      axes: [C_ledger]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "Humanism, as I understand it, is a rational philosophy. It rejects the mysticism and supernaturalism of the revealed religions. It rejects life after death and the idea that suffering in this world may, for the righteous, be compensated for by the bliss of an after-life. Included in this rejection of the supernatural is the rejection of a belief in an omniscient, omnipotent, and omnipresent god who watches over and cares for human beings, interfering, sometimes in response to prayer, with the ordered regularity of events as determined by natural laws."
      cites: [{source: S3, locator: "speech, paragraph on humanism"}]
      date: "1961-03-17"
      context: "Same speech, the next sentences."
      axes: [A_locus, B_cause, C_ledger, D_authority, E_scope]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "My paternal grandparents were Lutherans. I believe that I was baptized in the Congregational Church—I attended various Sunday schools when X was a boy, but I broke away from church affiliation when I began to think for myself and to become skeptical about dogmatic statements. I do not believe in God."
      cites: [{source: S4, locator: "letter, paragraph 1"}]
      date: "1963-01-23"
      context: "Letter to Mrs. Eubert J. Daniel (Duke University Medical Center), answering her inquiry (her letter of 18 January 1963); signed for him by his secretary Linda Hopkins. 'X' is as in the archive's transcription."
      axes: [A_locus, D_authority]
      kind: "private letter"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "I am a Humanist—a member of the American Humanist Association."
      cites: [{source: S4, locator: "letter, paragraph 1"}]
      date: "1963-01-23"
      context: "Same letter; he encloses 'Humanism and Peace' as 'a statement of my beliefs'."
      axes: []
      kind: "private letter"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
  changes_over_life:
    - {value: "Sunday schools as a boy; broke away from church affiliation as he became skeptical of dogma; humanist by 1961; joined the First Unitarian Church of Los Angeles in summer 1962", year: "1910s–1962", certainty: 0.7, cites: [{source: S4, locator: "letter, paragraph 1"}, {source: S3, locator: "speech"}], how_known: "His own letter; the date of the break is not given."}
  coder_notes: "SECHUM and ATHE are stub system files (flag). S3 and S4 are read in Oregon State University Special Collections' own transcriptions of documents in the Ava Helen and Linus Pauling Papers (the archive that holds them), so they are treated as authoritative copies under §7, not unofficial web copies; the printed version of the speech (The Humanist, 1961) was not compared. S4 is signed for him by his secretary Linda Hopkins ('Linus Pauling:lh'), so it is his letter in his name but possibly not typed or signed by him; fields resting mainly on it are at 0.7. The essay 'Why I am a Unitarian' on the Pauling Blog is by Ava Helen Pauling and is not used. No interview is used in this record."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "German (father's side) and English-Scottish (mother's side) American", certainty: 1.0, cites: [{source: S2, locator: "paragraph 1"}], how_known: "Nobel biography."}
  religious_heritage_by_birth: {value: "Protestant (Lutheran grandparents; probable Congregational baptism)", certainty: 0.7, cites: [{source: S4, locator: "letter, paragraph 1"}], how_known: "His own letter."}
  baptism_or_initiation: {value: "Probably baptized in the Congregational Church ('I believe that I was baptized')", certainty: 0.5, cites: [{source: S4, locator: "letter, paragraph 1"}], how_known: "His own uncertain recollection."}
  childhood_catechism: {value: "Various Sunday schools", certainty: 0.7, cites: [{source: S4, locator: "letter, paragraph 1"}], how_known: "His own letter."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1927–1954", certainty: 0.7, cites: [{source: S1, locator: "'Elucidation of molecular structures'"}, {source: S2, locator: "paragraphs 3–4"}], how_known: "Return to Caltech to the chemistry Nobel; coder's reading."}
  age_at_first_lasting_contribution: {value: 24, certainty: 0.5, cites: [{source: S1, locator: "opening; 'Early life and education'"}], how_known: "Born February 1901; PhD papers 1925; same caveat as the year."}
  first_evidence_of_lio_type_views: {value: "'Humanism and Peace' speech", year: 1961, certainty: 1.0, cites: [{source: S3, locator: "speech heading"}], how_known: "Earliest dated statement read (Rationalist of the Year 1960 suggests earlier views, not read)."}
  lio_views_relative_to_major_work: {value: "unclear", rationale: "The statements read are from 1961 and 1963, after the main work; the letter says he broke with the church when he began to think for himself, without a date.", certainty: 0.5, cites: [{source: S4, locator: "letter, paragraph 1"}], how_known: "Dates of the sources."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "He reasoned from structural rules (atomic radii, bond strengths, electronegativity) to molecular structures, and built the alpha helix by folding a paper model (S1); rule-based but empirical, not a definitional method.", certainty: 0.5, cites: [{source: S1, locator: "'Elucidation of molecular structures'; 1948 paragraph"}], how_known: "Coder's reading."}
  form_acquired: {value: "through the profession", certainty: 0.5, cites: [{source: S2, locator: "paragraph 3"}], how_known: "Crystal-structure work from 1922 with Dickinson; coder's reading."}
  circle_present: {value: "no", rationale: "He denies God; nothing identifies God with Nature.", certainty: 0.7, cites: [{source: S4, locator: "letter, paragraph 1"}], how_known: "His own letter."}
  reading: "As belief, not finding: form partly present (structural rules), circle absent. The record does not test H1."
  notes: ""

institutions:
  - {value: "California Institute of Technology", role: "professor; chairman of the Division of Chemistry and Chemical Engineering and director of the Gates and Crellin laboratories (1936–1958)", years: "1922–1963", kind: university, certainty: 0.7, cites: [{source: S2, locator: "paragraph 4"}, {source: S1, locator: "'Elucidation of molecular structures'"}], how_known: "Two sources; the end year is not on the pages read."}
  - {value: "American Humanist Association", role: "member; Humanist of the Year 1961", years: "1961–", kind: other, certainty: 1.0, cites: [{source: S4, locator: "letter"}, {source: S2, locator: "paragraph 5"}], how_known: "Two sources."}
collaborators:
  - {value: "Roscoe G. Dickinson", relation: teacher, note: "taught him X-ray crystal-structure determination", certainty: 1.0, cites: [{source: S1, locator: "'Early life and education'"}, {source: S2, locator: "paragraph 2"}], how_known: "Two sources."}
  - {value: "Arnold Sommerfeld", relation: "mentor or employer", note: "most of his 1926–27 Guggenheim year in Munich", certainty: 1.0, cites: [{source: S1, locator: "'Early life and education'"}, {source: S2, locator: "paragraph 4"}], how_known: "Two sources."}
  - {value: "Niels Bohr", roster_id: bohr-niels, relation: "mentor or employer", note: "worked with him in Europe in 1926–27", certainty: 0.7, cites: [{source: S2, locator: "paragraph 4"}], how_known: "Nobel biography."}
  - {value: "Robert Corey", relation: collaborator, note: "DNA triple-helix proposal (1953) and protein structures", certainty: 1.0, cites: [{source: S1, locator: "1948 paragraph"}], how_known: "Britannica."}
  - {value: "J. Robert Oppenheimer", roster_id: oppenheimer-j-robert, relation: other, note: "asked him to head the Manhattan Project's chemistry section; he declined for illness", certainty: 1.0, cites: [{source: S1, locator: "World War II sentence"}], how_known: "Britannica."}
  - {value: "Ava Helen Miller", relation: family, note: "wife (married 1923)", certainty: 1.0, cites: [{source: S2, locator: "paragraph 7"}, {source: S1, locator: "'Early life and education'"}], how_known: "Two sources."}

review:
  roster_status_reason: {value: "Core in v8 (F 3: Claude, DeepSeek, Gemini).", certainty: 0.7, cites: [{source: S5, locator: "roster.csv, rank 200"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "S4 is signed for him by his secretary."
    - "S3 read in the archive's transcription of the speech typescript; the printed version in The Humanist was not compared."
    - "Britannica read as its first page only."
  open_questions:
    - "Read the printed 'Humanism and Peace' (The Humanist, 1961) and any statement behind the 1960 Rationalist of the Year award."
    - "Decision question: SECHUM or ATHE for a self-described Humanist who also says 'I do not believe in God' (see CHANGELOG, batch 4)."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Robert J. Paradowski"
    citation: "Paradowski, Robert J. \"Linus Pauling.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Linus-Pauling."
    url: "https://www.britannica.com/biography/Linus-Pauling"
    accessed: 2026-10-02
    reliability_note: "Signed article; first page only. Sections cited by heading."
    used_for: [identity, basics, contribution, childhood, worldview, timing, lane_b, institutions, collaborators]
  - id: S2
    type: tertiary
    kind: "institutional page"
    author: "Nobel Foundation"
    year: 1964
    citation: "\"Linus Pauling – Biographical.\" From Nobel Lectures, Chemistry 1942–1962. Amsterdam: Elsevier, 1964. NobelPrize.org. https://www.nobelprize.org/prizes/chemistry/1954/pauling/biographical/."
    url: "https://www.nobelprize.org/prizes/chemistry/1954/pauling/biographical/"
    accessed: 2026-10-02
    reliability_note: "Official biography; paragraphs counted from 'Linus Carl Pauling was born'."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S3
    type: primary
    kind: "archive record"
    author: "Linus Pauling"
    year: 1961
    citation: "Pauling, Linus. \"Humanism and Peace.\" Speech to the American Humanist Association, Cleveland, Ohio, 17 March 1961. Ava Helen and Linus Pauling Papers, Speeches 1961s.9; transcription in Linus Pauling Day-by-Day, Oregon State University Special Collections, https://scarc.library.oregonstate.edu/coll/pauling/calendar/1961/03/17.html."
    url: "https://scarc.library.oregonstate.edu/coll/pauling/calendar/1961/03/17.html"
    accessed: 2026-10-02
    reliability_note: "His own speech, transcribed by the archive that holds the typescript. No page numbers; the humanism paragraph begins 'I believe that there is great value in the philosophy of humanism'."
    used_for: [contribution, worldview, timing]
  - id: S4
    type: primary
    kind: letter
    author: "Linus Pauling"
    year: 1963
    citation: "Pauling, Linus, to Mrs. Eubert J. Daniel, 23 January 1963 (signed by Linda Hopkins). Ava Helen and Linus Pauling Papers, Correspondence D, #99.4; transcription in Linus Pauling Day-by-Day, Oregon State University Special Collections, https://scarc.library.oregonstate.edu/coll/pauling/calendar/1963/01/23.html."
    url: "https://scarc.library.oregonstate.edu/coll/pauling/calendar/1963/01/23.html"
    accessed: 2026-10-02
    reliability_note: "His letter, transcribed by the archive that holds it; one page, one main paragraph."
    used_for: [childhood, worldview, heritage, timing, lane_b, institutions]
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

# Linus Pauling

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Linus Pauling (1901–1994), American chemist, explained the chemical bond in quantum terms, found the first molecular disease and the alpha helix, and won two unshared Nobel Prizes (Chemistry 1954, Peace 1962) [S1]. He called himself "a Humanist—a member of the American Humanist Association" and wrote "I do not believe in God" [S4]; his 1961 speech to the AHA rejects the supernatural, the afterlife and a god who answers prayer [S3]. primary_system SECHUM at 0.7 (stub; ATHE named). A, B, C, D and E all 4 at 0.7; mid_basin false (0.7).

## Life and work

Oregon Agricultural College (BSc 1922), Caltech (PhD 1925), a Guggenheim year with Sommerfeld, then Caltech for decades; peace campaigning from the 1950s [S1; S2].

## Contribution and impact

Crystal structures, valence-bond theory and resonance, electronegativity, The Nature of the Chemical Bond (1939), sickle-cell anemia (1949), the alpha helix [S1; S2].

## Childhood and education

A druggist's son in Oregon; Sunday schools as a boy; probably baptized Congregational [S2; S4].

## Adult working worldview

A humanist who rejects the supernatural and revealed religion [S3]; he joined the First Unitarian Church of Los Angeles in 1962 because it supports morality and ethics and "accepts atheists as members" [S4].

## Heritage (context only)

German and English-Scottish American [S2]. Context only.

## Timing

First lasting contribution about 1925 [S1; S2]. The worldview statements read are from 1961 and 1963.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form partly present (structural rules); circle absent.

## Open questions

- The printed speech in The Humanist; SECHUM or ATHE.

## Research log

- 2026-10-02: Read Britannica (Paradowski, first page), the Nobel biography, and OSU's Day-by-Day transcriptions for 17 March 1961 and 23 January 1963. The Pauling Blog post on Unitarianism was read for context only; its 'Why I am a Unitarian' is Ava Helen Pauling's. No interview used.
