---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 4
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch B)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-08
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (stage 3 batch B). Basics from MacTutor and Britannica (Copeland, first page). Worldview from 'Computing Machinery and Intelligence' (Mind, 1950), read on the offprint scan in the Turing Digital Archive (King's College Cambridge, AMT/B/19; pp. 443, 444 and 453 checked on the page images), and from the 1932 manuscript 'Nature of Spirit' (AMT/C/29, facsimile), with Hodges' SEP entry and Scrapbook page for context. primary_system BELOW_THRESHOLD (ATHE candidate, stub). B 3 (0.7), D 4 (0.7); A, C, E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. All scores are drafts for v8's review. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit fixes, stage 3 batch B (two blind runs at 3db6511). #122: primary_system unchanged (BELOW_THRESHOLD); its reason now rests on the evidence (CODING_GUIDE §3, §4) and no longer cites an unwritten rule; the stub-system question awaits v8's ruling. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Stage 3 rulings P14–P28 (v8, main 6aeba87), schema 1.3. primary_system BELOW_THRESHOLD → ATHE 0.5, scholarly_reconstruction, on Hodges (new sources S8, S9) (P14); Mind p. 443 statement axes [A_locus, E_scope] → [A_locus, C_ledger] (P7); C and E notes rewritten (still BELOW_THRESHOLD), A note gives the evidence (P19); Nature of Spirit kind notebook or diary → unpublished manuscript (P18); single-source 1.0 fields → 0.7 (P15) (native_name, first_lasting_contribution_year, era_bucket, imitation game item, major_works/0, schooling/2, working_years, major_work_period, age_at_first_lasting_contribution, King's and Princeton, Church and Newman); region_of_birth, region_of_work, sex keep 1.0 with a Britannica cite; Hazlehurst stage grammar or secondary school → elementary school (P21); Morcom quotation marked primary check pending (P26); first_evidence_of_lio_type_views checked against the LIO-type view anchor (P27), unchanged. Not reviewed."}
    - {date: 2026-10-08, by: "Grok Bot", summary: "P30 rule 5 age sweep: ages recomputed as event year − birth year, with no month adjustment (scripts/recompute_ages.py; every change is in reports/p30_age_changes.csv). No other value changed."}

identity:
  id: turing-alan
  display_name: "Alan Turing"
  roster:
    canonical_name: "Alan Turing"
    rank: 5
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: mathematics
    field_bucket: mathematics
  full_name: {value: "Alan Mathison Turing", certainty: 1.0, cites: [{source: S4, locator: "'In full' line"}, {source: S3, locator: "heading"}], how_known: "Two sources."}
  native_name: {value: "Alan Mathison Turing (English)", certainty: 0.7, cites: [{source: S4, locator: "'In full' line"}], how_known: "English name. One source cited, so 0.7 under the single-source rule (P15)."}
  aliases:
    - {name: "Alan-Turing", kind: "roster alias"}
    - {name: "Turing-Alan", kind: "roster alias"}

basics:
  birth:
    date: {value: "1912-06-23", calendar: gregorian, certainty: 1.0, cites: [{source: S3, locator: "Quick Info"}, {source: S4, locator: "Born line"}], how_known: "Two sources agree."}
    place: {value: "London (Paddington)", modern_name: "London, England, UK", polity_then: "United Kingdom", certainty: 1.0, cites: [{source: S3, locator: "Quick Info; Biography, paragraph 1"}, {source: S4, locator: "Born line"}], how_known: "Two sources agree."}
  death:
    date: {value: "1954-06-07", calendar: gregorian, certainty: 1.0, cites: [{source: S3, locator: "Quick Info"}, {source: S4, locator: "Died line"}], how_known: "Two sources agree."}
    place: {value: "Wilmslow, Cheshire", modern_name: "Wilmslow, Cheshire, England, UK", polity_then: "United Kingdom", certainty: 1.0, cites: [{source: S3, locator: "Quick Info"}, {source: S4, locator: "Died line"}], how_known: "Two sources agree."}
  first_lasting_contribution_year: {value: 1936, certainty: 0.7, cites: [{source: S3, locator: "Biography ('In 1936 he published On Computable Numbers')"}], how_known: "On Computable Numbers, completed April 1936, revised August 1936, printed 1937 (MacTutor); the year of the work is 1936."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S3, locator: "Biography (1936)"}], how_known: "From first_lasting_contribution_year (P2). Follows that field's 0.7 under the single-source rule (P15)."}
  region_of_birth: {value: "Northern Europe", certainty: 1.0, cites: [{source: S3, locator: "Quick Info"}, {source: S4, locator: "Born line"}], how_known: "UK is Northern Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 1.0, cites: [{source: S3, locator: "Biography"}, {source: S4, locator: "codebreaking section (Bletchley Park)"}], how_known: "Cambridge, Bletchley Park and Manchester; Princeton (North America) only 1936–38."}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S3, locator: "Biography"}, {source: S4, locator: "opening"}], how_known: "As the sources record it."}
  languages_of_work: {value: [English], certainty: 1.0, cites: [{source: S1, locator: "whole paper"}], how_known: "His papers are in English."}
  occupations: {value: ["mathematician", "logician", "cryptanalyst", "computer scientist"], certainty: 1.0, cites: [{source: S3, locator: "Biography"}, {source: S4, locator: "heading; opening"}], how_known: "Two sources."}

contribution:
  fields: {value: ["mathematical logic", "computability", "cryptanalysis", "computer science", "artificial intelligence", "morphogenesis"], certainty: 1.0, cites: [{source: S3, locator: "Biography"}, {source: S4, locator: "opening"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "The Turing machine and the unsolvability of the Entscheidungsproblem (On Computable Numbers)", year: "1936", kind: theory, lasting: "foundation of computability theory and computer science", certainty: 1.0, cites: [{source: S3, locator: "Biography (1936)"}, {source: S4, locator: "opening"}], how_known: "Two sources."}
    - {value: "Methods for breaking German Enigma and Tunny messages at Bletchley Park", year: "1939–1945", kind: method, lasting: "wartime codebreaking", certainty: 1.0, cites: [{source: S3, locator: "Biography (Bletchley Park)"}, {source: S4, locator: "codebreaking section"}], how_known: "Two sources."}
    - {value: "The imitation game (Turing test) as a criterion for machine intelligence", year: "1950", kind: "concept or term", lasting: "standard reference in AI", certainty: 0.7, cites: [{source: S1, locator: "pp. 433–434"}], how_known: "His own paper gives the contribution; no second source is cited for its lasting status, so 0.7 under the single-source rule (P15)."}
    - {value: "Mathematical theory of morphogenesis", year: "1952", kind: theory, lasting: "reaction–diffusion patterns in biology", certainty: 0.7, cites: [{source: S3, locator: "Biography (1952)"}], how_known: "MacTutor."}
  evidence_of_impact:
    - {value: "Fellow of the Royal Society, 1951, mainly for the 1936 work", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S3, locator: "Biography (1951)"}], how_known: "MacTutor."}
  major_works:
    - {value: "On Computable Numbers, with an Application to the Entscheidungsproblem", year: 1936, kind: "paper or paper series", certainty: 0.7, cites: [{source: S3, locator: "Biography (1936)"}], how_known: "MacTutor alone, so 0.7 under the single-source rule (P15)."}
    - {value: "Computing Machinery and Intelligence", year: 1950, kind: "paper or paper series", certainty: 1.0, cites: [{source: S1, locator: "p. 433"}], how_known: "Read on the scan."}
  honours:
    - {value: "Officer of the Order of the British Empire (OBE), for codebreaking", year: "1945–1946", certainty: 0.7, cites: [{source: S4, locator: "codebreaking section ('At the end of the war')"}], how_known: "Britannica gives 'at the end of the war', not a year."}
    - {value: "Fellow of the Royal Society", year: 1951, certainty: 0.7, cites: [{source: S3, locator: "Biography (1951)"}], how_known: "MacTutor."}
  definition_fit: {value: "clearly meets", rationale: "Founder of computability theory and of the theory of the universal computing machine.", certainty: 1.0, cites: [{source: S3, locator: "Biography (1936)"}, {source: S4, locator: "opening"}], how_known: "Sources agree."}

childhood:
  family_religion: {value: TODO, note: "Not stated in the sources read."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father, Julius Mathison Turing, of the Indian Civil Service, often abroad", name: "Julius Mathison Turing", role: father, certainty: 0.7, cites: [{source: S3, locator: "Biography, paragraph 1"}], how_known: "MacTutor."}
    - {value: "Mother, Ethel Sara Stoney, daughter of the chief engineer of the Madras railways", name: "Ethel Sara Turing (née Stoney)", role: mother, certainty: 0.7, cites: [{source: S3, locator: "Biography, paragraph 1"}], how_known: "MacTutor."}
  household_circumstances: {value: "Left in England with family friends from about age one while his parents were in India", certainty: 0.7, cites: [{source: S3, locator: "Biography, paragraph 1"}], how_known: "MacTutor."}
  schooling:
    - {value: "Hazlehurst Preparatory School", stage: "elementary school", years: "–1926", certainty: 0.7, cites: [{source: S3, locator: "Biography, paragraph 2"}], how_known: "MacTutor. A preparatory school, before Sherborne (1926); stage is the level (P21), so elementary school (was grammar or secondary school as the nearest stage). MacTutor does not say who ran it, so no run_by."}
    - {value: "Sherborne School", stage: "grammar or secondary school", years: "1926–1931", certainty: 0.7, cites: [{source: S3, locator: "Biography, paragraphs 2–3"}], how_known: "MacTutor (entered 1926; King's College 1931)."}
    - {value: "King's College, Cambridge, mathematics", stage: university, years: "1931–1934", certainty: 0.7, cites: [{source: S3, locator: "Biography (1931, 1934)"}], how_known: "MacTutor alone, so 0.7 under the single-source rule (P15)."}
  early_mathematics: {value: "advanced mathematics", note: "Won almost every mathematics prize at Sherborne and read Einstein on relativity (MacTutor).", certainty: 0.7, cites: [{source: S3, locator: "Biography, Sherborne paragraph"}], how_known: "MacTutor."}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure:
    - {value: "Chemistry experiments of his own at school; Einstein's relativity papers and Eddington's The Nature of the Physical World", certainty: 0.7, cites: [{source: S3, locator: "Biography, Sherborne paragraph"}], how_known: "MacTutor."}
  key_early_reading:
    - {value: "Eddington, The Nature of the Physical World", certainty: 0.7, cites: [{source: S3, locator: "Biography, Sherborne paragraph"}], how_known: "MacTutor."}
  childhood_mentors: []
  languages_in_childhood: {value: [English], certainty: 0.7, cites: [{source: S3, locator: "Biography, paragraph 1"}], how_known: "English family."}
  notable_events:
    - {value: "Close friendship with Christopher Morcom (1928), who died in February 1930; Turing 'felt that this was something beyond what science could explain' (MacTutor)", year: "1930", age: 18, certainty: 0.7, cites: [{source: S3, locator: "Biography, Morcom paragraph"}], how_known: "MacTutor, which quotes Turing: 'It is not difficult to explain these things away - but, I wonder!' (secondary quotation; primary check pending, P26). Not used for any score."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1934–1954", certainty: 0.7, cites: [{source: S3, locator: "Biography"}], how_known: "From graduation to his death. MacTutor alone, so 0.7 under the single-source rule (P15)."}
  nominal_affiliations: []
  self_described_science_religion_relation:
    value: "In 1950 he answered the 'Theological Objection' to thinking machines by saying 'I am unable to accept any part of this' and 'I am not very impressed with theological arguments whatever they may be used to support', citing the texts once used against Copernicus; he also wrote that the statistical evidence for telepathy was 'overwhelming' and would challenge 'all our usual scientific ideas'."
    certainty: 1.0
    cites: [{source: S1, locator: "pp. 443–444, 453"}]
    how_known: "His own published paper, read on the archive scan."
  primary_system:
    value: ATHE
    basis: scholarly_reconstruction
    certainty: 0.5
    cites: [{source: S8, locator: "§ on the computer after the war ('His later thought was strongly determinist and atheistic in character')"}, {source: S9, locator: "paragraph on Manchester ('a materialist and atheistic exposition'); paragraph on the syllogism ('God-denying 'heretic'')"}, {source: S5, locator: "§ on the 1950 paper ('always committed to materialist explanation')"}, {source: S1, locator: "pp. 443–444"}]
    how_known: "Coded to the evidence under the stub-systems rule (P14). His biographer reconstructs the adult view: 'His later thought was strongly determinist and atheistic in character' (S8, Hodges 1995); the 1950 paper is 'famous as a materialist and atheistic exposition' and he enjoyed 'the status he enjoyed having as a God-denying 'heretic' for proposing Artificial Intelligence' (S9, Hodges 2003); 'always committed to materialist explanation' (S5). His own 1950 words reject the theological objection outright: 'I am unable to accept any part of this' (S1, p. 443). No first-person denial of God was read, so this is a scholar's reconstruction from indirect evidence, 0.5 (CODING_GUIDE §3). ATHE is a stub system file, noted for the sourcing backlog."
    rationale: "Draft judgment (one line): ATHE (positive naturalism) at 0.5 on Hodges' reading, matched by the 1950 paper; the named alternative is AGNOS, since none of his own words read denies God outright. All three Hodges sources are one author, so they count as one scholar's reconstruction."
  secondary_system: {value: UNKNOWN, how_known: "Searched MacTutor, Britannica (first page), Hodges' SEP entry, short biography, IWM talk and Scrapbook page, and the 1950 paper: none names a second system for the working years. The 1932 'Nature of Spirit' (S2) is before them."}
  candidate_codes_considered:
    - {code: ATHE, reason: "Coded at 0.5 (primary_system): Hodges calls his later thought 'atheistic' (S8; S9) and 'always committed to materialist explanation' (S5); the 1950 paper rejects theological arguments (S1). ATHE is a stub system file (flag, sourcing backlog).", cites: [{source: S8, locator: "§ on the computer after the war"}, {source: S9, locator: "paragraph on Manchester"}, {source: S5, locator: "§ on the 1950 paper"}, {source: S1, locator: "pp. 443–444"}]}
    - {code: AGNOS, reason: "Named alternative: none of his own words read denies God; his reply 'in theological terms' (S1, p. 443) is an argument he does not accept, not suspended judgment. AGNOS is a stub system file (flag).", cites: [{source: S1, locator: "p. 443"}]}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, note: "Evidence exists but is indirect: Hodges speaks of his 'God-denying 'heretic'' status (S9) and 'atheistic' later thought (S8), but none of his own words read places or denies God; his 1950 reply 'in theological terms' is offered as an argument he does not accept ('this is mere speculation', S1, p. 443). Draft judgment (one line): not scored, because axes are scored from the person's own words (§6); the alternative v8 may prefer is A 4 at 0.5 on Hodges' reconstruction.", how_known: "Kept BELOW_THRESHOLD under the UNKNOWN/BELOW_THRESHOLD rule (P19): some evidence, too indirect to score."}
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.7
      cites: [{source: S1, locator: "pp. 443–444, 453"}]
      how_known: "His own published paper (archive scan); a named alternative, so 0.7."
      rationale: "Draft judgment (one line): leans LIO, not the pole, because the paper treats nature as lawful but grants that telepathy, if accepted, would overturn 'all our usual scientific ideas'. Scored on his account of nature (P6). He wrote that the statistical evidence 'at least for telepathy, is overwhelming' and that the idea that our bodies move 'simply according to the known laws of physics, together with some others not yet discovered but somewhat similar, would be one of the first to go' (S1, p. 453). Named alternative: 4, since he speaks of laws 'not yet discovered' rather than of miracle, and the 1950 paper never admits petition or exemption."
    C_ledger: {value: BELOW_THRESHOLD, note: "Some indirect evidence: in 1950, against the objection that 'God has given an immortal soul to every man and woman, but not to any other animal or to machines', he wrote 'I am unable to accept any part of this' and that he would find it more convincing 'if animals were classed with men' (S1, p. 443). That concerns the scope of the moral community, which P7 places on C, but it says nothing on reward or punishment of persons. The 1932 survival of the spirit (S2) is before the working years and has no ledger. Draft judgment (one line): too indirect to score; the alternative is C 4 at 0.5.", how_known: "The p. 443 passage moved here from E under rule P7; BELOW_THRESHOLD under P19."}
    D_authority:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S1, locator: "pp. 443–444"}]
      how_known: "His own published paper (archive scan); a named alternative, so 0.7."
      rationale: "Draft judgment (one line): scripture and theology have no authority over questions of fact for him. 'I am not very impressed with theological arguments whatever they may be used to support. Such arguments have often been found unsatisfactory in the past' (p. 443); the Joshua and Psalm texts against Copernicus 'With our present knowledge such an argument appears futile' (p. 444). Named alternative: 3, because he still offers a reply 'in theological terms' (p. 443), though as 'mere speculation'."
    E_scope: {value: BELOW_THRESHOLD, note: "Scored on the world's order (P7). Only indirect evidence: in 1950 he set out, as an objection, 'We like to believe that Man is in some subtle way superior to the rest of creation' and answered that 'Consolation would be more appropriate: perhaps this should be sought in the transmigration of souls' (S1, p. 444), which mocks the in-group view without stating his own account of the world's order. The p. 443 'animals classed with men' passage is scored on C (P7). Draft judgment (one line): too indirect to score.", how_known: "BELOW_THRESHOLD under P19: some evidence, too weak. The earlier alternative (E 4 from p. 443) is dropped because that passage now goes to C (P7)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD, so the P4 test cannot be applied."}
  statements:
    - text: "I am unable to accept any part of this, but will attempt to reply in theological terms. I should find the argument more convincing if animals were classed with men, for there is a greater difference, to my mind, between the typical animate and the inanimate than there is between man and the other animals."
      cites: [{source: S1, locator: "p. 443"}]
      date: "1950-10"
      context: "Reply to '(1) The Theological Objection': that thinking is a function of the immortal soul, which God gave to men and women but not to animals or machines."
      axes: [A_locus, C_ledger]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
    - text: "However, this is mere speculation. I am not very impressed with theological arguments whatever they may be used to support. Such arguments have often been found unsatisfactory in the past."
      cites: [{source: S1, locator: "p. 443"}]
      date: "1950-10"
      context: "Closing his theological reply; he goes on to the texts (Joshua x. 13 and a Psalm) used against Copernicus in Galileo's time."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
    - text: "With our present knowledge such an argument appears futile."
      cites: [{source: S1, locator: "p. 444"}]
      date: "1950-10"
      context: "On the scriptural argument against Copernicus."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
    - text: "These disturbing phenomena seem to deny all our usual scientific ideas. How we should like to discredit them! Unfortunately the statistical evidence, at least for telepathy, is overwhelming."
      cites: [{source: S1, locator: "p. 453"}]
      date: "1950-10"
      context: "'(9) The Argument from Extra-Sensory Perception'."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
    - text: "The idea that our bodies move simply according to the known laws of physics, together with some others not yet discovered but somewhat similar, would be one of the first to go."
      cites: [{source: S1, locator: "p. 453"}]
      date: "1950-10"
      context: "Same section; what ESP would overturn. Read on the 110 dpi page image only."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
    - text: "Personally I think that spirit is really eternally connected with matter but certainly not always by the same kind of body."
      cites: [{source: S2, locator: "sheet 4"}]
      date: "1932"
      context: "'Nature of Spirit', manuscript written at age 19 on a visit to the Morcom family home (Hodges, S6); before the working years."
      axes: [C_ledger]
      kind: "unpublished manuscript"
      note: "Handwriting read by eye on the archive facsimile; date from the archive catalogue."
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
  changes_over_life:
    - {value: "As a 19-year-old student he wrote out a belief in the survival of the spirit after death ('Nature of Spirit'); by 1950 he rejected theological arguments and, as Hodges puts it, enjoyed calling the computability of mind 'heresy' to the believers in souls beyond material description", year: "1932 to late 1940s", certainty: 0.7, cites: [{source: S2, locator: "sheets 4–5"}, {source: S6, locator: "'Nature of Spirit' paragraph"}, {source: S5, locator: "§ on mechanising mind ('heresy')"}, {source: S1, locator: "p. 443"}], how_known: "His own manuscript for the start; Hodges for the later view; the change itself is Hodges' reading."}
  coder_notes: "ATHE and AGNOS are stub system files (flag; ATHE coded under P14, sourcing backlog). Hodges' short biography (S8) and IWM talk (S9) are on his own website; together with S5 and S6 they are one author. Mind 1950 was read on the King's College archive offprint scan (AMT/B/19; PDF page = journal page − 432) because the OUP page was blocked; the scan is the original printing, so this is not an unofficial web copy. The 1932 'Nature of Spirit' sheet 5 also says that when the body dies 'the spirit finds a new body sooner or later perhaps immediately' (handwriting read by eye, not quoted as a statement). The Morcom quotation is MacTutor's secondary quotation. No recorded interview of Turing on religion was found."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "English; father in the Indian Civil Service", certainty: 0.7, cites: [{source: S3, locator: "Biography, paragraph 1"}], how_known: "MacTutor."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1936–1952", certainty: 0.7, cites: [{source: S3, locator: "Biography"}], how_known: "On Computable Numbers to morphogenesis. MacTutor alone, so 0.7 under the single-source rule (P15)."}
  age_at_first_lasting_contribution: {value: 24, certainty: 0.7, cites: [{source: S3, locator: "Quick Info; Biography (April 1936)"}], how_known: "Born June 1912; paper completed April 1936. MacTutor alone for the month, so 0.7 under the single-source rule (P15). P30 (rule 5): 1936 − 1912 = 24, with no month adjustment; was 23 until the P30 age sweep (2026-10-08)."}
  first_evidence_of_lio_type_views: {value: "1950 (rejection of theological arguments in print); Hodges dates the 'heresy' remarks to the late 1940s", certainty: 0.5, cites: [{source: S1, locator: "pp. 443–444"}, {source: S5, locator: "§ on mechanising mind"}], how_known: "Earliest dated text read is 1950; Hodges' dating is secondary. The 1950 statements are scored at 3 or 4 (B_cause 3, D_authority 4), so they meet the LIO-type view anchor (P27)."}
  lio_views_relative_to_major_work: {value: "during major work", rationale: "The 1950 paper falls inside 1936–1952; nothing read dates the views earlier, and the 1932 manuscript points the other way.", certainty: 0.5, cites: [{source: S1, locator: "p. 443"}, {source: S2, locator: "sheet 4"}], how_known: "Dated texts only."}
  worldview_during_major_work: {value: "Materialist and, on Hodges' reading, atheistic; rejection of theological arguments in 1950", certainty: 0.5, cites: [{source: S5, locator: "§ on the 1950 paper"}, {source: S8, locator: "§ on the computer after the war"}, {source: S1, locator: "p. 443"}], how_known: "Secondary characterisation plus one paper."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "His central work is formal: machines defined by a finite table of rules, with theorems derived from the definitions (S3).", certainty: 0.5, cites: [{source: S3, locator: "Biography (1936)"}], how_known: "Coder's reading."}
  form_acquired: {value: "childhood or adolescence", certainty: 0.5, cites: [{source: S3, locator: "Biography, Sherborne paragraph"}], how_known: "Deep mathematics learned on his own at school."}
  circle_present: {value: "unclear", rationale: "No God–Nature statement of his adult years was read.", certainty: 0.5, cites: [{source: S1, locator: "p. 443"}], how_known: "No evidence either way."}
  reading: "As belief, not finding: form present, circle unclear. The record does not test H1."
  notes: ""

institutions:
  - {value: "King's College, Cambridge", role: "student; fellow from 1935", years: "1931–", kind: university, certainty: 0.7, cites: [{source: S3, locator: "Biography (1931, 1935)"}], how_known: "MacTutor alone, so 0.7 under the single-source rule (P15)."}
  - {value: "Princeton University", role: "graduate student under Church", years: "1936–1938", kind: university, certainty: 0.7, cites: [{source: S3, locator: "Biography (Princeton)"}], how_known: "MacTutor alone, so 0.7 under the single-source rule (P15)."}
  - {value: "Government Code and Cypher School, Bletchley Park", role: codebreaker, years: "1939–1945", kind: "government or state body", certainty: 1.0, cites: [{source: S3, locator: "Biography (Bletchley Park)"}, {source: S4, locator: "codebreaking section"}], how_known: "Two sources."}
  - {value: "University of Manchester", role: reader, years: "1948–1954", kind: university, certainty: 0.7, cites: [{source: S3, locator: "Biography (1948)"}], how_known: "MacTutor."}
collaborators:
  - {value: "Alonzo Church", relation: teacher, note: "Princeton supervisor", certainty: 0.7, cites: [{source: S3, locator: "Biography (Princeton)"}], how_known: "MacTutor alone, so 0.7 under the single-source rule (P15)."}
  - {value: "Max Newman", relation: "mentor or employer", note: "1935 foundations course; Manchester", certainty: 0.7, cites: [{source: S3, locator: "Biography (1935, 1948)"}], how_known: "MacTutor alone, so 0.7 under the single-source rule (P15)."}

review:
  roster_status_reason: {value: "Core in v8 (F 5: Claude, DeepSeek, Gemini, GPT, Grok).", certainty: 0.7, cites: [{source: S7, locator: "roster.csv, rank 5"}], how_known: "Study roster."}
  controversies:
    - {value: "Cause of death: the inquest found cyanide self-administered; his mother held it was an accident", certainty: 0.7, cites: [{source: S3, locator: "Biography, last paragraph"}], how_known: "MacTutor."}
  data_quality_flags:
    - "Britannica read as its first page only."
    - "p. 453 of Mind 1950 read on the 110 dpi image only (not zoomed)."
  open_questions:
    - "Hodges, Alan Turing: The Enigma (1983), for later statements on religion; Turing's letters in the King's archive."
    - "ATHE is a stub system file; coded under P14 and noted for the sourcing backlog."

sources:
  - id: S1
    type: primary
    kind: "published work by the subject"
    author: "A. M. Turing"
    year: 1950
    citation: "Turing, A. M. \"Computing Machinery and Intelligence.\" Mind 59, no. 236 (October 1950): 433–460. Offprint scan, Turing Digital Archive, King's College Cambridge, AMT/B/19. https://turingarchive.kings.cam.ac.uk/publications-lectures-and-talks-amtb/amt-b-19."
    url: "https://turingarchive.kings.cam.ac.uk/publications-lectures-and-talks-amtb/amt-b-19"
    accessed: 2026-10-02
    reliability_note: "Archive scan of the original printing; pp. 443, 444 and 453 checked on the page images (PDF page = journal page − 432)."
    used_for: [basics, contribution, worldview, timing, lane_b]
  - id: S2
    type: primary
    kind: "archive record"
    author: "A. M. Turing"
    year: 1932
    citation: "Turing, A. M. \"Nature of Spirit.\" Manuscript, [1932]. Xerox copy, Turing Digital Archive, King's College Cambridge, AMT/C/29. https://turingarchive.kings.cam.ac.uk/unpublished-manuscripts-and-drafts-amtc/amt-c-29."
    url: "https://turingarchive.kings.cam.ac.uk/unpublished-manuscripts-and-drafts-amtc/amt-c-29"
    accessed: 2026-10-02
    reliability_note: "Facsimile of the handwriting; read by eye. Date from the archive catalogue."
    used_for: [worldview, timing]
  - id: S3
    type: secondary
    kind: "institutional page"
    author: "J J O'Connor and E F Robertson"
    citation: "O'Connor, J. J., and E. F. Robertson. \"Alan Mathison Turing.\" MacTutor History of Mathematics, University of St Andrews. https://mathshistory.st-andrews.ac.uk/Biographies/Turing/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Turing/"
    accessed: 2026-10-02
    reliability_note: "Biography; cited by paragraph description."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators, review]
  - id: S4
    type: tertiary
    kind: encyclopedia
    author: "B. J. Copeland"
    citation: "Copeland, B. J. \"Alan Turing.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Alan-Turing."
    url: "https://www.britannica.com/biography/Alan-Turing"
    accessed: 2026-10-02
    reliability_note: "Signed article; first page only."
    used_for: [identity, basics, contribution, institutions]
  - id: S5
    type: secondary
    kind: encyclopedia
    author: "Andrew Hodges"
    year: 2013
    citation: "Hodges, Andrew. \"Alan Turing.\" Stanford Encyclopedia of Philosophy (revised 2013). https://plato.stanford.edu/entries/turing/."
    url: "https://plato.stanford.edu/entries/turing/"
    accessed: 2026-10-02
    reliability_note: "Scholarly encyclopedia entry by his biographer."
    used_for: [worldview, timing]
  - id: S6
    type: secondary
    kind: other
    author: "Andrew Hodges"
    citation: "Hodges, Andrew. \"The Alan Turing Scrapbook: Nature of Spirit.\" https://www.turing.org.uk/scrapbook/spirit.html."
    url: "https://www.turing.org.uk/scrapbook/spirit.html"
    accessed: 2026-10-02
    reliability_note: "Biographer's website; used for the context of the 1932 manuscript only."
    used_for: [worldview]
  - id: S7
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
  - id: S8
    type: secondary
    kind: other
    author: "Andrew Hodges"
    year: 1995
    citation: "Hodges, Andrew. \"Alan Turing — a short biography.\" Based on his 1995 entry for the Oxford Dictionary of Scientific Biography. https://www.turing.org.uk/publications/dnb.html."
    url: "https://www.turing.org.uk/publications/dnb.html"
    accessed: 2026-10-02
    reliability_note: "His biographer's own summary of Alan Turing: The Enigma, on his website (© Andrew Hodges, 1995)."
    used_for: [worldview, timing]
  - id: S9
    type: secondary
    kind: other
    author: "Andrew Hodges"
    year: 2003
    citation: "Hodges, Andrew. \"Alan Turing at the Imperial War Museum and Europride.\" Published talk, 21 August 2003. https://www.turing.org.uk/publications/iwm.html."
    url: "https://www.turing.org.uk/publications/iwm.html"
    accessed: 2026-10-02
    reliability_note: "Published talk by his biographer on his website; same author as S5, S6 and S8."
    used_for: [worldview]
---

# Alan Turing

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Alan Mathison Turing (1912–1954), English mathematician, defined the Turing machine and proved the Entscheidungsproblem unsolvable (1936), broke German ciphers at Bletchley Park, and proposed the imitation game for machine intelligence [S3; S4; S1]. In 1950 he wrote "I am not very impressed with theological arguments whatever they may be used to support" [S1, p. 443]; his biographer calls his later thought "strongly determinist and atheistic in character" [S8]. Draft under v8's stage 3 rulings (P14–P28): primary_system ATHE (0.5, scholarly reconstruction) (P14). Draft scores: B 3 (0.7), D 4 (0.7); A, C, E below threshold; mid_basin below threshold.

## Life and work

Sherborne School, King's College Cambridge (1931), Princeton under Church (1936–38), Bletchley Park (1939–45), Manchester (1948) [S3]. Convicted in 1952 under the homosexuality laws; died of cyanide poisoning in 1954 [S3].

## Contribution and impact

Computability (1936), codebreaking, the imitation game (1950) and morphogenesis (1952) [S3; S1].

## Childhood and education

His parents were often in India and he was left with family friends in England [S3]. At Sherborne he read Einstein and Eddington; the death of his friend Christopher Morcom in 1930 shook him [S3].

## Adult working worldview

He rejected the theological objection to thinking machines and the scriptural case against Copernicus [S1, pp. 443–444], but granted that the evidence for telepathy was "overwhelming" [S1, p. 453]. Hodges calls him "always committed to materialist explanation" [S5] and his later thought "strongly determinist and atheistic in character" [S8]. In 1932, before his working years, he had written that the spirit survives the body [S2, sheet 4; S6].

## Heritage (context only)

English family; father in the Indian Civil Service [S3]. Context only.

## Timing

First lasting contribution 1936, at 24 [S3].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form present (formal machines and proofs [S3]); circle unclear.

## Open questions

- Hodges' biography and the King's archive letters for later statements on religion.
- ATHE is a stub system file; coded under P14 (sourcing backlog).

## Research log

- 2026-10-02: Read MacTutor, Britannica (Copeland, first page), Hodges' SEP entry and Scrapbook page; read Mind 1950 on the King's College archive scan (OUP page blocked) and the 'Nature of Spirit' facsimile.
- 2026-10-02 (v8 method rulings): Reopened Hodges' SEP entry; read Hodges' short biography (1995) and IWM talk (2003) on turing.org.uk; reopened Mind 1950 pp. 443–444 on the scan.
