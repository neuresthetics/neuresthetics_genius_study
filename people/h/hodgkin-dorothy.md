---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 4
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, fourth batch: physical science 1600–1950)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-08
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (fourth batch, RUNBOOK §1 order). Included by owner decision, borderline on the stage-2 date window (main work 1945–69; Jason, 2026-10-02). Basics from Britannica (Ferry), the Nobel biography and Dodson's Royal Society memoir (2002). No writing of hers on religion was found; the memoir reports Quaker-type values from her mother and Margery Fry and quotes Max Perutz's memorial address ('more Christian in word and deed than many believers I have known'), which is another person's view. primary_system BELOW_THRESHOLD (no candidate supported). B 4 at 0.5 from her working science (P6); A, C, D, E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. No interview used. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit, batch 4 (two blind runs at b21655b). #150 (both runs): the no-code note wrongly cited 'decision P9: paraphrase alone cannot score'; it now cites CODING_GUIDE §1 and §7. #150 (run 1): candidate_codes_considered was empty; CHRIST is now listed as considered, not coded (§5.3). #158 (run 1): death place 'Shipston-on-Stour, Warwickshire' (0.7) → 'Ilmington, Warwickshire (at home, Crab Mill)' (0.5), per Dodson's memoir p. 188, with Britannica's Shipston-on-Stour as the alternative (sources disagree, as for Pasteur). Decision P12: first_lasting_contribution_year 1945 → 1942 (start of the listed 1942–1945 penicillin item; Nobel biography), age 35 → 32; era unchanged. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Stage 3 lens-audit rulings applied to the batch's other records (OPEN_DECISIONS P14–P28, v8's picks, 2026-10-02). Schema 1.2 → 1.3. One reliable source caps a fact at 0.7; derived fields take the lowest certainty of their inputs; BELOW_THRESHOLD vs UNKNOWN per P19; basis inference_from_work for 0.5 inference from working science (P24). Full before → after list: reports/stage3_rulings_changes.csv. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Span alignment (P29, P30 and its addendum): timing.major_work_period checked, 1942–1969 unchanged; worldview.working_years 1932–1994 → 1942–1969, equal to the span (P30 addendum f); evidence for every headline value checked against the span; no value or certainty changed. Listed in reports/p30_span_alignment.csv. Not reviewed."}
    - {date: 2026-10-08, by: "Grok Bot", summary: "Lens audit of batch C (dd91009), ruling R1, logged as P35 (v8's pick): B_cause 4 → 3 at 0.5, alternative 4, because B rests on working science only. No other value changes; mid_basin unchanged."}

identity:
  id: hodgkin-dorothy
  display_name: "Dorothy Hodgkin"
  roster:
    canonical_name: "Dorothy Hodgkin"
    rank: 94
    F: 4
    models: [Claude, DeepSeek, Gemini, Grok]
    band: "core (3–4)"
    status: core
    field: chemistry
    field_bucket: chemistry
  full_name: {value: "Dorothy Mary Crowfoot Hodgkin (née Crowfoot)", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts ('In full'; 'Née')"}, {source: S3, locator: "p. 179, heading"}], how_known: "Two sources."}
  native_name: {value: "Dorothy Crowfoot Hodgkin (English)", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}], how_known: "English name."}
  aliases:
    - {name: "Dorothy Crowfoot Hodgkin", kind: "roster alias"}
    - {name: "Hodgkin-Dorothy", kind: "roster alias"}
    - {name: "Dorothy Crowfoot", kind: "birth name"}

basics:
  birth:
    date: {value: "1910-05-12", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "paragraph 1"}], how_known: "Two sources agree."}
    place: {value: "Cairo", modern_name: "Cairo, Egypt", polity_then: "Khedivate of Egypt (under British occupation)", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "paragraph 1"}], how_known: "Two sources agree; polity is the coder's description."}
  death:
    date: {value: "1994-07-29", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "p. 179, heading"}], how_known: "Two sources agree."}
    place: {value: "Ilmington, Warwickshire (at home, Crab Mill)", modern_name: "Ilmington, Warwickshire, England, UK", polity_then: "United Kingdom", certainty: 0.5, cites: [{source: S3, locator: "p. 188 ('Crab Mill, his parents' house in the village of Ilmington'; 'Dorothy spent her time at Crab Mill [...] After a fall, she died at home with her family on 29 July 1994')"}], how_known: "Dodson's Royal Society memoir, the fuller source, puts her death at home at Crab Mill in Ilmington; Britannica gives Shipston-on-Stour and does not say why. Reliable sources disagree, so 0.5 (CODING_GUIDE §3, §8), as for Pasteur. Was 'Shipston-on-Stour, Warwickshire' at 0.7 until the batch 4 lens audit (#158).", alternatives: [{value: "Shipston-on-Stour, Warwickshire", cites: [{source: S1, locator: "opening"}], note: "Britannica's form. That it names the nearby market town rather than the village is the coder's inference, not a sourced fact."}]}
  first_lasting_contribution_year: {value: 1942, certainty: 0.7, cites: [{source: S2, locator: "paragraph 7 ('researches on penicillin began in 1942')"}, {source: S1, locator: "'Scientific achievements', paragraph 1 ('By 1945 she had succeeded')"}], how_known: "Start year of the earliest listed contribution, the penicillin structure (1942–1945), under decision P12. Her 1930s X-ray work on sterols and pepsin with Bernal is not a listed contribution, so it does not set the year (P13). Was 1945 (the year the structure was solved) until the batch 4 lens audit."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S1, locator: "'Scientific achievements', paragraph 1"}], how_known: "From first_lasting_contribution_year 1942 (P2); her vitamin B12 and insulin structures fall in 1950 on."}
  region_of_birth: {value: "Middle East and North Africa", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "Egypt is Middle East and North Africa in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 1.0, cites: [{source: S1, locator: "'Education and marriage'"}, {source: S2, locator: "paragraph 6"}], how_known: "Oxford, 1934–1977."}
  sex_as_recorded: {value: "female", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "As the sources record it."}
  languages_of_work: {value: [English], certainty: 0.7, cites: [{source: S3, locator: "bibliography"}], how_known: "Papers in English."}
  occupations: {value: ["chemist", "X-ray crystallographer", "university teacher"], certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "paragraph 6"}], how_known: "Two sources."}

contribution:
  fields: {value: ["X-ray crystallography", "structural chemistry", "structural biology"], certainty: 1.0, cites: [{source: S1, locator: "'Scientific achievements'"}, {source: S2, locator: "paragraph 7"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Three-dimensional structure of penicillin", year: "1942–1945", kind: discovery, lasting: "largest molecule then solved by X-rays; settled a dispute among organic chemists", certainty: 1.0, cites: [{source: S1, locator: "'Scientific achievements', paragraph 1"}, {source: S2, locator: "paragraph 7 (research from 1942)"}], how_known: "Two sources."}
    - {value: "Structure of vitamin B12, with extensive use of computers", year: "1948–1950s", kind: discovery, lasting: "Nobel Prize 1964", certainty: 1.0, cites: [{source: S1, locator: "'Scientific achievements', paragraph 2"}, {source: S2, locator: "paragraph 7 (research from 1948)"}], how_known: "Two sources."}
    - {value: "Structure of insulin, 34 years after her first X-ray photograph of it", year: "1969", kind: discovery, lasting: "protein structure of medical importance", certainty: 0.7, cites: [{source: S1, locator: "'Scientific achievements', paragraph 3"}], how_known: "Britannica."}
  evidence_of_impact:
    - {value: "Her structural studies 'set standards for a field that was very much in development'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "last paragraph"}], how_known: "Britannica (her biographer)."}
  major_works: []
  honours:
    - {value: "Fellow of the Royal Society", year: 1947, certainty: 1.0, cites: [{source: S1, locator: "'Scientific achievements', paragraph 1"}, {source: S2, locator: "paragraph 8"}], how_known: "Two sources."}
    - {value: "Wolfson Research Professor of the Royal Society (first holder)", year: 1960, certainty: 1.0, cites: [{source: S1, locator: "'Scientific achievements', paragraph 2"}, {source: S2, locator: "paragraph 6"}], how_known: "Two sources."}
    - {value: "Nobel Prize in Chemistry", year: 1964, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    - {value: "Order of Merit", year: 1965, certainty: 0.7, cites: [{source: S1, locator: "'Scientific achievements', paragraph 2"}], how_known: "Britannica."}
    - {value: "Copley Medal", year: 1976, certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}], how_known: "Britannica."}
  definition_fit: {value: "clearly meets", rationale: "Solved penicillin, vitamin B12 and insulin by X-ray crystallography.", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: TODO, note: "Not stated in the sources read. S3 (p. 184) says Margery Fry's ideas 'coincided with those of Dorothy's mother, and these Quaker values too had a long-lasting influence'; that describes values, not a family religion."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father, John Winter Crowfoot, in the Egyptian Education Service, later Director of Education and of Antiquities in the Sudan, then an archaeologist (British School of Archaeology in Jerusalem)", name: "John Winter Crowfoot", role: father, certainty: 1.0, cites: [{source: S2, locator: "paragraph 1"}, {source: S3, locator: "p. 182"}], how_known: "Two sources."}
    - {value: "Mother, Grace Mary (Molly) Crowfoot, née Hood, botanist and authority on ancient weaving, who encouraged Dorothy's interest in crystals", name: "Grace Mary Crowfoot (née Hood)", role: mother, certainty: 1.0, cites: [{source: S2, locator: "paragraph 2"}, {source: S1, locator: "'Education and marriage'"}, {source: S3, locator: "p. 182"}], how_known: "Three sources."}
  household_circumstances: {value: "Eldest of four sisters, sent to England for schooling and much of the time apart from their parents (at Geldeston, Norfolk, near Beccles)", certainty: 1.0, cites: [{source: S1, locator: "'Education and marriage'"}, {source: S2, locator: "paragraph 3"}], how_known: "Two sources."}
  schooling:
    - {value: "Taught at home by her mother for a year after World War I; then a Parents National Educational Union class near Beccles", stage: home, years: "1919–1921", certainty: 0.7, cites: [{source: S3, locator: "p. 182"}], how_known: "Dodson; years are the coder's reading ('one year after the war'; 'now aged 10')."}
    - {value: "Sir John Leman School, Beccles, where she and one other girl were allowed to join the boys' chemistry class", stage: "grammar or secondary school", years: "1921–1928", certainty: 1.0, cites: [{source: S2, locator: "paragraph 3"}, {source: S1, locator: "'Education and marriage'"}], how_known: "Two sources."}
    - {value: "Somerville College, Oxford: chemistry; first X-ray work as an undergraduate with H. M. Powell", stage: university, years: "1928–1932", certainty: 1.0, cites: [{source: S2, locator: "paragraph 4"}, {source: S1, locator: "'Education and marriage'"}], how_known: "Two sources."}
    - {value: "Cambridge, doctoral research with J. D. Bernal (sterols)", stage: university, years: "1932–1934", certainty: 1.0, cites: [{source: S1, locator: "'Education and marriage', paragraph 2"}, {source: S2, locator: "paragraphs 5–6"}], how_known: "Two sources."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure:
    - {value: "Crystal-growing experiments in her PNEU chemistry book at about 10; analysis of ilmenite with Dr A. F. Joseph in the Sudan", certainty: 1.0, cites: [{source: S3, locator: "p. 182"}, {source: S2, locator: "paragraph 3"}], how_known: "Two sources."}
  key_early_reading: []
  childhood_mentors:
    - {value: "Dr A. F. Joseph, government chemist in Khartoum, a friend of her father", certainty: 1.0, cites: [{source: S2, locator: "paragraph 3"}, {source: S3, locator: "p. 182"}], how_known: "Two sources."}
    - {value: "Her mother, Molly Crowfoot", certainty: 0.7, cites: [{source: S1, locator: "'Education and marriage'"}], how_known: "Britannica ('it was their mother who especially encouraged Dorothy')."}
  languages_in_childhood: {value: [English], certainty: 0.7, cites: [{source: S3, locator: "p. 182"}], how_known: "English family."}
  notable_events:
    - {value: "Visit to her parents in the Sudan, first direct experience of foreign peoples and of colonial poverty", year: "1922", certainty: 0.7, cites: [{source: S3, locator: "p. 182"}], how_known: "Dodson (the Nobel biography gives 1923)."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1942–1969", certainty: 1.0, cites: [{source: S1, locator: "'Scientific achievements'"}, {source: S2, locator: "paragraph 7"}], how_known: "Equal to timing.major_work_period (P30 addendum f; span check 2026-10-02). Was 1932–1994: Doctoral research to death."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No statement by her on science and religion was found in the sources read."}
  primary_system:
    value: BELOW_THRESHOLD
    cites: [{source: S3, locator: "pp. 184, 193, 213"}]
    how_known: "No writing of hers on religion was read. Dodson reports values (Quaker-type values from her mother and Margery Fry, p. 184; 'belief in social justice and her uncompromising hatred of militarism', p. 213), and quotes Max Perutz's memorial address: 'Dorothy was more Christian in word and deed than many believers I have known' (p. 193). Perutz's remark implies she was not a believer, but it is another person's description, not her words, so it cannot score a code (CODING_GUIDE §1, §7)."
    note: "No candidate is supported by her own words. Would need Ferry's biography (Dorothy Hodgkin: A Life, 1998) and her papers (Bodleian Library)."
  secondary_system: {value: UNKNOWN, how_known: "No system evidence in the sources read."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Considered, not coded: the Quaker values from her mother and Margery Fry (p. 184) and Perutz's 'more Christian in word and deed than many believers' (p. 193) are other people's descriptions, not her words (CODING_GUIDE §1, §7); Quakers would fall under CHRIST, and no statement of hers on religion was read.", cites: [{source: S3, locator: "pp. 184, 193"}]}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "No statement placing or denying God was read.", note: "Stays BELOW_THRESHOLD (P19): Perutz's remark that she was 'more Christian in word and deed than many believers' (S3, p. 193) is another person's description, which bears on the point but cannot score it."}
    B_cause:
      value: 3
      basis: inference_from_work
      certainty: 0.5
      cites: [{source: S1, locator: "'Scientific achievements'"}]
      how_known: "Coder's reading of her working science, as P6 directs (same treatment as Fermi and Dirac). No statement of hers about miracles read, so 0.5."
      rationale: "Scored on her account of nature (P6). Her work found the arrangement of atoms in molecules from X-ray diffraction and computation, and the structure of insulin once 'the techniques of X-ray diffraction and high-speed computing were sufficiently advanced' (S1): lawful physical method throughout. No miracle, petition or exemption in anything read. P35 (v8's pick, 2026-10-08, lens audit of batch C ruling R1): B inferred only from a scientist's working science, with no statement of their own on law and exception, is B 3 at 0.5 with 4 as the named alternative, never 4, because working science cannot tell a lawful nature with one stated exception from one with none (Faraday, Maxwell and Newton did the same kind of science and are B 3 from their own statements). Named alternative: 4, if a statement of their own shows no exception."
    C_ledger: {value: UNKNOWN, how_known: "Nothing on judgement, afterlife or reward in the sources read."}
    D_authority: {value: UNKNOWN, how_known: "No statement on revelation in the sources read."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Scored on the world's order (P7). Nothing read addresses favour for a group in events. Working science bears on the first question (same laws everywhere) but not on favour for a group in events, so E stays BELOW_THRESHOLD; not scored from working science alone (P19)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD and B_cause is only 0.5, under the P4 test's 0.7 bar."}
  statements: []
  changes_over_life: []
  coder_notes: "No writing of hers on religion was found, so statements is empty. S3 is the Royal Society's memoir (Dodson 2002), read in the publisher's PDF; page numbers are the journal's printed numbers. Its descriptions of her values and politics (socialist sympathies, Pugwash, peace work, pp. 213–215) are Dodson's; none of the 77 codes is a political creed, and political views are not coded. The Perutz quotation is reported speech about her. No interview used."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "English (family in colonial education and archaeology in Egypt, the Sudan and Palestine)", certainty: 1.0, cites: [{source: S1, locator: "'Education and marriage'"}, {source: S2, locator: "paragraph 1"}], how_known: "Two sources."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1942–1969", certainty: 1.0, cites: [{source: S1, locator: "'Scientific achievements'"}, {source: S2, locator: "paragraph 7"}], how_known: "Penicillin research to insulin."}
  age_at_first_lasting_contribution: {value: 32, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "paragraph 7"}], how_known: "Born 12 May 1910; penicillin research began in 1942 (month not given), so 32 (31 before 12 May). Was 35 (from 1945) until the batch 4 lens audit."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No worldview statement of hers found."}
  lio_views_relative_to_major_work: {value: "unclear", rationale: "No worldview statement of hers found.", certainty: 0.5, cites: [{source: S3, locator: "p. 193"}], how_known: "Nothing to date."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "Crystallography infers three-dimensional atomic arrangement from diffraction patterns by computation (S1); geometric in subject, empirical in method.", certainty: 0.5, cites: [{source: S1, locator: "'Scientific achievements'"}], how_known: "Coder's reading."}
  form_acquired: {value: "childhood or adolescence", rationale: "Her interest in crystals began at about 10 with crystal-growing experiments (S3, p. 182).", certainty: 0.5, cites: [{source: S3, locator: "p. 182"}, {source: S2, locator: "paragraph 3"}], how_known: "Coder's reading of the early crystal interest."}
  circle_present: {value: "unclear", rationale: "No God-Nature statement found; not scored from absence.", certainty: 0.5, cites: [{source: S3, locator: "p. 193"}], how_known: "No evidence either way."}
  reading: "As belief, not finding: form partly present, circle unclear. The record does not test H1."
  notes: ""

institutions:
  - {value: "Somerville College, Oxford", role: "research fellow, then Official Fellow and Tutor in Natural Science", years: "1934–1977", kind: university, certainty: 1.0, cites: [{source: S1, locator: "'Education and marriage', paragraph 2"}, {source: S2, locator: "paragraph 6"}], how_known: "Two sources."}
  - {value: "University of Oxford (Chemical Crystallography)", role: "lecturer and demonstrator (1946), Reader in X-ray Crystallography (1956)", years: "1946–1977", kind: university, certainty: 0.7, cites: [{source: S2, locator: "paragraph 6"}], how_known: "Nobel biography."}
  - {value: "Pugwash Conferences on Science and World Affairs", role: president, years: "1975–1988", kind: other, certainty: 0.7, cites: [{source: S1, locator: "'Social activism'"}], how_known: "Britannica."}
  - {value: "University of Bristol", role: chancellor, years: "1970–1988", kind: university, certainty: 0.7, cites: [{source: S1, locator: "'Social activism'"}], how_known: "Britannica."}
collaborators:
  - {value: "J. D. Bernal", relation: teacher, note: "doctoral supervisor at Cambridge and 'a lifelong influence'; she was receptive to his pro-Soviet views and belief in the social function of science", certainty: 1.0, cites: [{source: S1, locator: "'Education and marriage', paragraph 2"}, {source: S2, locator: "paragraph 5"}], how_known: "Two sources."}
  - {value: "H. M. Powell", relation: teacher, note: "her first research supervisor at Oxford", certainty: 0.7, cites: [{source: S2, locator: "paragraph 4"}], how_known: "Nobel biography."}
  - {value: "Max Perutz", relation: collaborator, note: "she supported his haemoglobin work; he gave the address at her memorial service", certainty: 0.7, cites: [{source: S3, locator: "p. 193"}], how_known: "Dodson."}
  - {value: "Margaret Thatcher", roster_id: thatcher-margaret, relation: "student or assistant", note: "one of her students in the late 1940s", certainty: 0.7, cites: [{source: S1, locator: "'Education and marriage', paragraph 2"}], how_known: "Britannica."}
  - {value: "Thomas Hodgkin", relation: family, note: "husband (married 1937), left-wing historian, later of West Africa", certainty: 0.7, cites: [{source: S1, locator: "'Education and marriage', paragraph 3"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 4: Claude, DeepSeek, Gemini, Grok). Included in the fourth batch by owner decision, borderline on the stage-2 date window (1600–1950).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 94"}], how_known: "Study roster; batch inclusion by Jason, 2026-10-02."}
  controversies: []
  data_quality_flags:
    - "Borderline on the stage-2 date window: main work 1945–69; included by owner decision (2026-10-02)."
    - "No first-hand worldview source; only values and politics as described by Dodson and Perutz."
  open_questions:
    - "Read Ferry, Dorothy Hodgkin: A Life (1998), and her papers at the Bodleian Library, for any statement of her own on religion."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Georgina Ferry"
    citation: "Ferry, Georgina. \"Dorothy Hodgkin.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Dorothy-Hodgkin."
    url: "https://www.britannica.com/biography/Dorothy-Hodgkin"
    accessed: 2026-10-02
    reliability_note: "Signed article by her biographer. Sections cited by heading."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: tertiary
    kind: "institutional page"
    author: "Nobel Foundation"
    year: 1972
    citation: "\"Dorothy Crowfoot Hodgkin – Biographical.\" From Nobel Lectures, Chemistry 1963–1970. Amsterdam: Elsevier, 1972. NobelPrize.org. https://www.nobelprize.org/prizes/chemistry/1964/hodgkin/biographical/."
    url: "https://www.nobelprize.org/prizes/chemistry/1964/hodgkin/biographical/"
    accessed: 2026-10-02
    reliability_note: "Official biography; paragraphs counted from 'Dorothy Crowfoot was born'."
    used_for: [basics, contribution, childhood, heritage, timing, lane_b, institutions, collaborators]
  - id: S3
    type: secondary
    kind: "journal article"
    author: "Guy Dodson"
    year: 2002
    citation: "Dodson, Guy. \"Dorothy Mary Crowfoot Hodgkin, O.M. 12 May 1910 – 29 July 1994.\" Biographical Memoirs of Fellows of the Royal Society 48 (2002): 179–219. https://doi.org/10.1098/rsbm.2002.0011."
    url: "https://royalsocietypublishing.org/doi/10.1098/rsbm.2002.0011"
    accessed: 2026-10-02
    reliability_note: "Royal Society memoir by a long-time colleague; read in the publisher's PDF. Printed page numbers."
    used_for: [identity, basics, contribution, childhood, worldview, timing, lane_b, collaborators]
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

# Dorothy Hodgkin

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Dorothy Crowfoot Hodgkin (1910–1994), English chemist, solved the structures of penicillin (1945), vitamin B12 and insulin (1969) by X-ray crystallography and won the 1964 Nobel Prize in Chemistry [S1]. No writing of hers on religion was found; her memoir records Quaker-type values from her mother and Perutz's remark that she was "more Christian in word and deed than many believers" [S3, pp. 184, 193], which is another person's view. primary_system BELOW_THRESHOLD. B 3 at 0.5 from the working science (alternative 4, P35); A and E below threshold, C and D UNKNOWN; mid_basin below threshold. Included in this batch by owner decision, borderline on the stage-2 date window.

## Life and work

Born in Cairo; Sir John Leman School, Beccles; Somerville, Oxford; doctoral work with Bernal in Cambridge; Oxford from 1934 until 1977; Pugwash president 1975–88 [S1; S2].

## Contribution and impact

Penicillin, vitamin B12 and insulin structures; first Wolfson Research Professor [S1; S2].

## Childhood and education

Eldest of four daughters of colonial educators and archaeologists, largely apart from her parents; crystals from about 10 [S1; S2; S3, p. 182].

## Adult working worldview

Not established from her own words. Dodson describes her belief in social justice, hatred of militarism and socialist sympathies [S3, p. 213]; these are political views, not coded.

## Heritage (context only)

English [S1]. Context only.

## Timing

First lasting contribution 1942, the start of the penicillin structure work (solved by 1945), at 32 [S1; S2].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form partly present; circle unclear.

## Open questions

- Ferry's biography; her papers at the Bodleian.

## Research log

- 2026-10-02: Read Britannica (Ferry), the Nobel biography and Dodson's Royal Society memoir (publisher's PDF).
