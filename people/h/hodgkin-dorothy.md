---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 6
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, fourth batch: physical science 1600–1950; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to chemistry. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (fourth batch, RUNBOOK §1 order). Included by owner decision, borderline on the stage-2 date window (main work 1945–69; Jason, 2026-10-02). Basics from Britannica (Ferry), the Nobel biography and Dodson's Royal Society memoir (2002). No writing of hers on religion was found; the memoir reports Quaker-type values from her mother and Margery Fry and quotes Max Perutz's memorial address ('more Christian in word and deed than many believers I have known'), which is another person's view. primary_system BELOW_THRESHOLD (no candidate supported). B 4 at 0.5 from her working science (P6); A, C, D, E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. No interview used. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit, batch 4 (two blind runs at b21655b). #150 (both runs): the no-code note wrongly cited 'decision P9: paraphrase alone cannot score'; it now cites CODING_GUIDE §1 and §7. #150 (run 1): candidate_codes_considered was empty; CHRIST is now listed as considered, not coded (§5.3). #158 (run 1): death place 'Shipston-on-Stour, Warwickshire' (0.7) → 'Ilmington, Warwickshire (at home, Crab Mill)' (0.5), per Dodson's memoir p. 188, with Britannica's Shipston-on-Stour as the alternative (sources disagree, as for Pasteur). Decision P12: first_lasting_contribution_year 1945 → 1942 (start of the listed 1942–1945 penicillin item; Nobel biography), age 35 → 32; era unchanged. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Stage 3 lens-audit rulings applied to the batch's other records (OPEN_DECISIONS P14–P28, v8's picks, 2026-10-02). Schema 1.2 → 1.3. One reliable source caps a fact at 0.7; derived fields take the lowest certainty of their inputs; BELOW_THRESHOLD vs UNKNOWN per P19; basis inference_from_work for 0.5 inference from working science (P24). Full before → after list: reports/stage3_rulings_changes.csv. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Span alignment (P29, P30 and its addendum): timing.major_work_period checked, 1942–1969 unchanged; worldview.working_years 1932–1994 → 1942–1969, equal to the span (P30 addendum f); evidence for every headline value checked against the span; no value or certainty changed. Listed in reports/p30_span_alignment.csv. Not reviewed."}
    - {date: 2026-10-08, by: "Grok Bot", summary: "Lens audit of batch C (dd91009), ruling R1, logged as P35 (v8's pick): B_cause 4 → 3 at 0.5, alternative 4, because B rests on working science only. No other value changes; mid_basin unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #93, F4 rank 94). Needs: A BELOW (no own-voice; Perutz memorial third-party); B 3 @0.5 alt 4 (P35 working science); primary BELOW; mid_basin BELOW; not plotted. Dual bio: Britannica Ferry (S1) + Wikipedia EN (S5) (P50). P47 source_quality on S1–S10. Read Ferry Dorothy Hodgkin: A Life (Bloomsbury Reader / IA OCR, S6) cover-to-cover search for religion/God/Quaker/atheist/Creator/afterlife — zero hits for religion/atheist/believer/Creator/afterlife as Dorothy's creed; Quaker mentions are husband's family, Kathleen Lonsdale, Hongying Liao, not her membership; church wedding with Communist vicar quoting Marx (ch. 4); biographer: resisted labels / would not have called herself a pacifist (ch. 9). Hektoen/Pearce (S7): Quaker affinities via marriage and pacifism but 'did not formally belong to the Society of Friends'. Nobel lecture PDF (S8) technical crystallography only — no nature-order / miracle / God. Nobel women-story attributed quote 'I believe in perfecting the world…' (S9) is humanitarian/peace, not a place/deny of God; primary interview page unread. NCUACS catalogue (S10): notebook notes on science and religion partly translation exercises / uncertain own theology; Thomas (husband) letter wished 'good old-fashioned Christian burial' — not Dorothy. A stays BELOW_THRESHOLD (Pasteur/Hilbert pattern; third-party eulogies cannot score A alone). B stays 3 @0.5 alt 4 inference_from_work (P35); support corroborated S1+S8 on method (P48); certainty still 0.5 under P35; no P16 explicit nature-order statement found. primary BELOW; mid_basin BELOW (A blocks P4). Chart-moving NO. Filled family_religion @0.5 (mother's strong religious convictions; father less so; not Quaker by birth). No fallacy_catalog. Draft, not reviewed."}

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
  full_name: {value: "Dorothy Mary Crowfoot Hodgkin (née Crowfoot)", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts ('In full'; 'Née')"}, {source: S3, locator: "p. 179, heading"}, {source: S5, locator: "lead"}], how_known: "Britannica, Dodson, Wikipedia (P15)."}
  native_name: {value: "Dorothy Crowfoot Hodgkin (English)", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}], how_known: "English name."}
  aliases:
    - {name: "Dorothy Crowfoot Hodgkin", kind: "roster alias"}
    - {name: "Hodgkin-Dorothy", kind: "roster alias"}
    - {name: "Dorothy Crowfoot", kind: "birth name"}

basics:
  birth:
    date: {value: "1910-05-12", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "paragraph 1"}, {source: S5, locator: "infobox / lead"}], how_known: "Three sources agree."}
    place: {value: "Cairo", modern_name: "Cairo, Egypt", polity_then: "Khedivate of Egypt (under British occupation)", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "paragraph 1"}, {source: S5, locator: "Early life"}], how_known: "Sources agree; polity is the coder's description."}
  death:
    date: {value: "1994-07-29", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "p. 179, heading"}, {source: S5, locator: "Disability and death"}], how_known: "Sources agree on July 1994; day from S1/S3."}
    place: {value: "Ilmington, Warwickshire (at home, Crab Mill)", modern_name: "Ilmington, Warwickshire, England, UK", polity_then: "United Kingdom", certainty: 0.5, cites: [{source: S3, locator: "p. 188 ('Crab Mill, his parents' house in the village of Ilmington'; 'Dorothy spent her time at Crab Mill [...] After a fall, she died at home with her family on 29 July 1994')"}, {source: S5, locator: "Disability and death (Ilmington, near Shipston-on-Stour)"}], how_known: "Dodson's Royal Society memoir, the fuller source, puts her death at home at Crab Mill in Ilmington; Britannica gives Shipston-on-Stour and does not say why. Reliable sources disagree, so 0.5 (CODING_GUIDE §3, §8), as for Pasteur. Was 'Shipston-on-Stour, Warwickshire' at 0.7 until the batch 4 lens audit (#158).", alternatives: [{value: "Shipston-on-Stour, Warwickshire", cites: [{source: S1, locator: "opening"}], note: "Britannica's form. That it names the nearby market town rather than the village is the coder's inference, not a sourced fact."}]}
  first_lasting_contribution_year: {value: 1942, certainty: 0.7, cites: [{source: S2, locator: "paragraph 7 ('researches on penicillin began in 1942')"}, {source: S1, locator: "'Scientific achievements', paragraph 1 ('By 1945 she had succeeded')"}], how_known: "Start year of the earliest listed contribution, the penicillin structure (1942–1945), under decision P12. Her 1930s X-ray work on sterols and pepsin with Bernal is not a listed contribution, so it does not set the year (P13). Was 1945 (the year the structure was solved) until the batch 4 lens audit."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S1, locator: "'Scientific achievements', paragraph 1"}], how_known: "From first_lasting_contribution_year 1942 (P2); her vitamin B12 and insulin structures fall in 1950 on."}
  region_of_birth: {value: "Middle East and North Africa", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "Egypt is Middle East and North Africa in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 1.0, cites: [{source: S1, locator: "'Education and marriage'"}, {source: S2, locator: "paragraph 6"}], how_known: "Oxford, 1934–1977."}
  sex_as_recorded: {value: "female", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "As the sources record it."}
  languages_of_work: {value: [English], certainty: 0.7, cites: [{source: S3, locator: "bibliography"}], how_known: "Papers in English."}
  occupations: {value: ["chemist", "X-ray crystallographer", "university teacher"], certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "paragraph 6"}], how_known: "Two sources."}

contribution:
  primary_domain: chemistry
  fields: {value: ["X-ray crystallography", "structural chemistry", "structural biology"], certainty: 1.0, cites: [{source: S1, locator: "'Scientific achievements'"}, {source: S2, locator: "paragraph 7"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Three-dimensional structure of penicillin", year: "1942–1945", kind: discovery, lasting: "largest molecule then solved by X-rays; settled a dispute among organic chemists", certainty: 1.0, cites: [{source: S1, locator: "'Scientific achievements', paragraph 1"}, {source: S2, locator: "paragraph 7 (research from 1942)"}], how_known: "Two sources."}
    - {value: "Structure of vitamin B12, with extensive use of computers", year: "1948–1950s", kind: discovery, lasting: "Nobel Prize 1964", certainty: 1.0, cites: [{source: S1, locator: "'Scientific achievements', paragraph 2"}, {source: S2, locator: "paragraph 7 (research from 1948)"}], how_known: "Two sources."}
    - {value: "Structure of insulin, 34 years after her first X-ray photograph of it", year: "1969", kind: discovery, lasting: "protein structure of medical importance", certainty: 0.7, cites: [{source: S1, locator: "'Scientific achievements', paragraph 3"}, {source: S5, locator: "Scientific career / insulin"}], how_known: "Britannica; Wikipedia."}
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
  family_religion: {value: "English Christian milieu (mother with strong religious convictions; father less so); not Quaker by birth", certainty: 0.5, cites: [{source: S6, locator: "ch. 1 (Mary Crowfoot: John 'probably did not share Molly's strong religious convictions')"}, {source: S7, locator: "not formally Society of Friends"}, {source: S3, locator: "p. 184 (Quaker values influence — values, not family denomination)"}], how_known: "Ferry: Molly's strong religious convictions; John's mother warned he probably did not share them. Quaker link is later via marriage/affinities (Hektoen), not birth denomination. 0.5: biographer paraphrase of a private letter, not a church register."}
  family_religious_practice: {value: UNKNOWN, how_known: "No regular practice (church attendance, Meeting) for the Crowfoot household stated in the sources read; Molly's wartime church experience (Ferry ch. 1) is hers, not a household rule for the children."}
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
  key_early_reading:
    - {value: "W. H. Bragg, Concerning the Nature of Things (and related RI Christmas Lectures) — X-rays as a way to 'see' atoms in crystals", certainty: 0.7, cites: [{source: S6, locator: "ch. 1 (Bragg books; Dorothy recalls fascination with atomic arrangement)"}, {source: S8, locator: "opening (credits Bragg 1925 for first meeting X-ray diffraction)"}, {source: S2, locator: "paragraph 3"}], how_known: "Ferry and Nobel bio; she opens the Nobel lecture by naming Bragg's school book."}
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
  self_described_science_religion_relation: {value: UNKNOWN, cites: [{source: S10, locator: "notebook notes on science and religion (translation vs own work)"}], how_known: "No published statement of hers on science and religion was found. NCUACS catalogue (S10) notes notebook pages 'on science and religion, European religious factions, intolerance etc, some possibly part of a translation exercise, others Hodgkin's own work' — contents unread; not scored."}
  primary_system:
    value: BELOW_THRESHOLD
    cites: [{source: S3, locator: "pp. 184, 193, 213"}, {source: S6, locator: "ch. 4 wedding; ch. 9 resisted labels"}, {source: S7, locator: "not formally Society of Friends"}]
    how_known: "No own-voice system confession. Dodson: Quaker-type values from mother and Margery Fry (p. 184); Perutz memorial 'more Christian in word and deed than many believers I have known' (p. 193) — third-party eulogy, cannot score a code alone (CODING_GUIDE §1, §7). Ferry (S6): Quakerism is the Hodgkin (husband's) family tradition; she resisted rigid ideological labels; church wedding conducted by a Communist vicar who quoted Marx. Hektoen/Pearce (S7): Quaker affinities via marriage and pacifism but did not formally belong. Wikipedia category '20th-century Quakers' (S5) is unsupported by body text and contradicted by S7 — not used to code CHRIST."
    note: "Candidates considered: CHRIST (Quaker affinities / Perutz Christian-deed remark) — not coded. No ATHE/AGNOS own-voice. Would still need Bodleian papers, Wolpert Passion for Science interview primary, or SHI 1990 video transcript for a scored system."
  secondary_system: {value: UNKNOWN, how_known: "No second system evidence."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Considered, not coded: Quaker-type values (S3 p. 184), Perutz 'more Christian… than many believers' (S3 p. 193), church wedding (S6 ch. 4), Wikipedia Quaker category (S5). All third-party, ceremonial, or category-only; Hektoen (S7) denies formal Society of Friends membership; no own-voice theism or Quaker confession (CODING_GUIDE §1, §7).", cites: [{source: S3, locator: "pp. 184, 193"}, {source: S6, locator: "ch. 4"}, {source: S7, locator: "not formally"}, {source: S5, locator: "category 20th-century Quakers"}]}
    - {code: ATHE, reason: "Rejected: Perutz's contrast with 'believers' is another person's implication, not her denial of God; Ferry has no atheist self-label.", cites: [{source: S3, locator: "p. 193"}, {source: S6, locator: "religion/atheist search (none)"}]}
    - {code: AGNOS, reason: "Lead only if a later own-voice suspension of judgment appears. Nothing read states agnosticism.", cites: [{source: S6, locator: "full-text religion search"}]}
  lio_axes:
    A_locus:
      value: BELOW_THRESHOLD
      cites: [{source: S3, locator: "p. 193 (Perutz memorial)"}, {source: S6, locator: "full-text: no God/religion creed of hers"}, {source: S7, locator: "Quaker affinities, not membership"}, {source: S9, locator: "'perfecting the world' attributed quote"}]
      how_known: "Deepen D1: Ferry (S6) searched — no place or deny of a personal God in her words; Perutz (S3) remains third-party; Nobel-attributed 'I believe in perfecting the world… not because I know what's to come of it' (S9) is peace/humanitarian, not locus. Stays BELOW_THRESHOLD (P19; Pasteur/Hilbert pattern)."
      note: "Named alternative if later own-voice denial is found: A 4 at ≤0.5 with BELOW as alt (P38), reading Perutz's 'believers' contrast as non-belief — not scored from eulogy alone."
    B_cause:
      value: 3
      basis: inference_from_work
      certainty: 0.5
      support: corroborated
      cites: [{source: S1, locator: "'Scientific achievements'"}, {source: S8, locator: "Nobel lecture (method: diffraction → electron density; technical only)"}]
      how_known: "Coder's reading of her working science, as P6 directs (same treatment as Fermi and Dirac). Nobel lecture (S8) describes crystallographic method without stating law-vs-exception or miracles. No statement of hers about miracles or nature's exceptions read, so 0.5. Deepen D1: support corroborated across S1+S8 on lawful method (P48); certainty stays 0.5 under P35 (still inference_from_work, not a P16 creed)."
      rationale: "Scored on her account of nature (P6). Her work found the arrangement of atoms in molecules from X-ray diffraction and computation, and the structure of insulin once 'the techniques of X-ray diffraction and high-speed computing were sufficiently advanced' (S1): lawful physical method throughout. No miracle, petition or exemption in anything read. P35 (v8's pick, 2026-10-08, lens audit of batch C ruling R1): B inferred only from a scientist's working science, with no statement of their own on law and exception, is B 3 at 0.5 with 4 as the named alternative, never 4, because working science cannot tell a lawful nature with one stated exception from one with none (Faraday, Maxwell and Newton did the same kind of science and are B 3 from their own statements). Named alternative: 4, if a statement of their own shows no exception."
      alternatives:
        - {value: 4, note: "If an own-voice statement shows no exception to natural law (P16 / P35).", cites: [{source: S1, locator: "'Scientific achievements'"}, {source: S8, locator: "Nobel lecture"}]}
    C_ledger: {value: UNKNOWN, how_known: "Nothing on judgement, afterlife or reward in the sources read. S9 'not because I know what's to come of it' is about outcomes of peace work, not afterlife."}
    D_authority: {value: UNKNOWN, how_known: "No statement on revelation in the sources read."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Scored on the world's order (P7). Nothing read addresses favour for a group in events. Working science bears on the first question (same laws everywhere) but not on favour for a group in events, so E stays BELOW_THRESHOLD; not scored from working science alone (P19)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD, so the P4 test cannot be applied (Sagan/Jung/Curie/Hilbert pattern). B is scored (3 @0.5) but cannot alone decide mid_basin."}
  statements: []
  changes_over_life: []
  coder_notes: "Deepen D1 2026-10-24: Ferry biography (S6) and Nobel lecture (S8) checked; still no own-voice religion for A. Perutz quotation remains reported speech about her. Political views (socialism, Pugwash, peace) are not coded as systems. No interview primary used (Wolpert Passion for Science IA borrow-restricted; SHI 1990 video InC, no transcript). No fallacy_catalog."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "English (family in colonial education and archaeology in Egypt, the Sudan and Palestine)", certainty: 1.0, cites: [{source: S1, locator: "'Education and marriage'"}, {source: S2, locator: "paragraph 1"}], how_known: "Two sources."}
  religious_heritage_by_birth: {value: "English Christian (mother religious; father less so); Quaker connection by marriage later, not birth", certainty: 0.5, cites: [{source: S6, locator: "ch. 1 (Molly's convictions; John's)"}, {source: S7, locator: "Quaker affinities through marriage"}], how_known: "Ferry + Hektoen; context only."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Church wedding (S6 ch. 4) does not establish childhood baptism; no register read."}
  childhood_catechism: {value: UNKNOWN, how_known: "School 'scripture' excellence (Ferry / Perutz report cards) is curriculum, not catechism evidence."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1942–1969", certainty: 1.0, cites: [{source: S1, locator: "'Scientific achievements'"}, {source: S2, locator: "paragraph 7"}], how_known: "Penicillin research to insulin."}
  age_at_first_lasting_contribution: {value: 32, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "paragraph 7"}], how_known: "Born 12 May 1910; penicillin research began in 1942 (month not given), so 32 (31 before 12 May). Was 35 (from 1945) until the batch 4 lens audit."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No worldview statement of hers found that scores A/B."}
  lio_views_relative_to_major_work: {value: "unclear", rationale: "No scored worldview statement of hers found.", certainty: 0.5, cites: [{source: S3, locator: "p. 193"}], how_known: "Nothing to date."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "primary_system BELOW_THRESHOLD; A BELOW; no locus statement from 1942–1969 read."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "Crystallography infers three-dimensional atomic arrangement from diffraction patterns by computation (S1; S8); geometric in subject, empirical in method.", certainty: 0.5, cites: [{source: S1, locator: "'Scientific achievements'"}, {source: S8, locator: "Fourier / electron-density method"}], how_known: "Coder's reading."}
  form_acquired: {value: "childhood or adolescence", rationale: "Her interest in crystals began at about 10 with crystal-growing experiments (S3, p. 182); Bragg's school book (S6; S8).", certainty: 0.5, cites: [{source: S3, locator: "p. 182"}, {source: S6, locator: "ch. 1 Bragg"}], how_known: "Coder's reading of the early crystal interest."}
  circle_present: {value: "unclear", rationale: "No God-Nature statement found; A BELOW; not scored from absence.", certainty: 0.5, cites: [{source: S3, locator: "p. 193"}, {source: S6, locator: "religion search"}], how_known: "No evidence either way."}
  reading: "As belief, not finding: form partly present, circle unclear, A BELOW, B 3 @0.5. The record does not test H1; unplotted."
  notes: "Chart-moving NO this pass (need A≥0.7 and B≥0.7)."

institutions:
  - {value: "Somerville College, Oxford", role: "research fellow, then Official Fellow and Tutor in Natural Science", years: "1934–1977", kind: university, certainty: 1.0, cites: [{source: S1, locator: "'Education and marriage', paragraph 2"}, {source: S2, locator: "paragraph 6"}], how_known: "Two sources."}
  - {value: "University of Oxford (Chemical Crystallography)", role: "lecturer and demonstrator (1946), Reader in X-ray Crystallography (1956)", years: "1946–1977", kind: university, certainty: 0.7, cites: [{source: S2, locator: "paragraph 6"}], how_known: "Nobel biography."}
  - {value: "Pugwash Conferences on Science and World Affairs", role: president, years: "1975–1988", kind: other, certainty: 0.7, cites: [{source: S1, locator: "'Social activism'"}, {source: S5, locator: "Political views and activities"}], how_known: "Britannica; Wikipedia."}
  - {value: "University of Bristol", role: chancellor, years: "1970–1988", kind: university, certainty: 0.7, cites: [{source: S1, locator: "'Social activism'"}], how_known: "Britannica."}
collaborators:
  - {value: "J. D. Bernal", relation: teacher, note: "doctoral supervisor at Cambridge and 'a lifelong influence'; she was receptive to his pro-Soviet views and belief in the social function of science", certainty: 1.0, cites: [{source: S1, locator: "'Education and marriage', paragraph 2"}, {source: S2, locator: "paragraph 5"}], how_known: "Two sources."}
  - {value: "H. M. Powell", relation: teacher, note: "her first research supervisor at Oxford", certainty: 0.7, cites: [{source: S2, locator: "paragraph 4"}], how_known: "Nobel biography."}
  - {value: "Max Perutz", relation: collaborator, note: "she supported his haemoglobin work; he gave the address at her memorial service", certainty: 0.7, cites: [{source: S3, locator: "p. 193"}], how_known: "Dodson."}
  - {value: "Margaret Thatcher", roster_id: thatcher-margaret, relation: "student or assistant", note: "one of her students in the late 1940s", certainty: 0.7, cites: [{source: S1, locator: "'Education and marriage', paragraph 2"}], how_known: "Britannica."}
  - {value: "Thomas Hodgkin", relation: family, note: "husband (married 1937), Quaker family background, left-wing historian, later of West Africa", certainty: 0.7, cites: [{source: S1, locator: "'Education and marriage', paragraph 3"}, {source: S6, locator: "ch. 4 (Society of Friends Hodgkin family)"}, {source: S7, locator: "husband Quaker"}], how_known: "Britannica; Ferry; Hektoen."}

review:
  roster_status_reason: {value: "Core in v8 (F 4: Claude, DeepSeek, Gemini, Grok). Included in the fourth batch by owner decision, borderline on the stage-2 date window (1600–1950).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 94"}], how_known: "Study roster; batch inclusion by Jason, 2026-10-02."}
  controversies: []
  data_quality_flags:
    - "Borderline on the stage-2 date window: main work 1945–69; included by owner decision (2026-10-02)."
    - "No first-hand worldview source scoring A; Perutz memorial and Quaker affinities remain third-party."
    - "Wikipedia category '20th-century Quakers' conflicts with Hektoen formal non-membership — category ignored for coding."
  open_questions:
    - "Optional: Bodleian DMCH papers / letters for any own-voice place/deny of God."
    - "Optional: Wolpert & Richards, A Passion for Science (1988) Hodgkin interview primary (IA borrow-restricted this pass)."
    - "Optional: Science History Institute 1990 video interview (InC; no public transcript this pass)."
    - "Optional: NCUACS notebook pages on science and religion (catalogue B.18 area) — unread beyond catalogue description."
    - "Settled this pass: Ferry A Life OCR searched; Nobel lecture PDF read; Hektoen Quaker non-membership noted."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Georgina Ferry"
    citation: "Ferry, Georgina. \"Dorothy Hodgkin.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Dorothy-Hodgkin."
    url: "https://www.britannica.com/biography/Dorothy-Hodgkin"
    accessed: 2026-10-24
    reliability_note: "Signed article by her biographer. Sections cited by heading. Live deepen fetch thin/Cloudflare; create-pass body retained."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: tertiary
    kind: "institutional page"
    author: "Nobel Foundation"
    year: 1972
    citation: "\"Dorothy Crowfoot Hodgkin – Biographical.\" From Nobel Lectures, Chemistry 1963–1970. Amsterdam: Elsevier, 1972. NobelPrize.org. https://www.nobelprize.org/prizes/chemistry/1964/hodgkin/biographical/."
    url: "https://www.nobelprize.org/prizes/chemistry/1964/hodgkin/biographical/"
    accessed: 2026-10-24
    reliability_note: "Official biography; paragraphs counted from 'Dorothy Crowfoot was born'."
    source_quality: "reference entry"
    used_for: [basics, contribution, childhood, heritage, timing, lane_b, institutions, collaborators]
  - id: S3
    type: secondary
    kind: "journal article"
    author: "Guy Dodson"
    year: 2002
    citation: "Dodson, Guy. \"Dorothy Mary Crowfoot Hodgkin, O.M. 12 May 1910 – 29 July 1994.\" Biographical Memoirs of Fellows of the Royal Society 48 (2002): 179–219. https://doi.org/10.1098/rsbm.2002.0011."
    url: "https://royalsocietypublishing.org/doi/10.1098/rsbm.2002.0011"
    accessed: 2026-10-24
    reliability_note: "Royal Society memoir by a long-time colleague; create-pass read in the publisher's PDF (live deepen PDF Cloudflare-blocked). Printed page numbers from create-pass."
    source_quality: "scholarly edition or monograph"
    used_for: [identity, basics, contribution, childhood, worldview, timing, lane_b, collaborators]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    reliability_note: "Study's own roster; used only for rank, F and status."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S5
    type: secondary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia. \"Dorothy Hodgkin.\" https://en.wikipedia.org/wiki/Dorothy_Hodgkin. Read 2026-10-24."
    url: "https://en.wikipedia.org/wiki/Dorothy_Hodgkin"
    accessed: 2026-10-24
    reliability_note: "Dual-bio second source (P50) for dates/places. Body silent on personal creed; category '20th-century Quakers' not used to code (conflicts with S7)."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, worldview, institutions, review]
  - id: S6
    type: secondary
    kind: "scholarly book"
    author: "Georgina Ferry"
    year: 1998
    citation: "Ferry, Georgina. Dorothy Hodgkin: A Life. London: Granta, 1998; Bloomsbury Reader reprint. Full-text OCR via Internet Archive item dorothy-hodgkin-a-life-by-ferry-georgina-hodgkin-dorothy-z-lib.org.epub (djvu.txt), read 2026-10-24."
    url: "https://archive.org/details/dorothy-hodgkin-a-life-by-ferry-georgina-hodgkin-dorothy-z-lib.org.epub"
    accessed: 2026-10-24
    reliability_note: "Standard biography. OCR searched for religion/God/Quaker/atheist/Creator/afterlife; locators by chapter/episode (page numbers unreliable in OCR)."
    source_quality: "scholarly edition or monograph"
    used_for: [childhood, worldview, heritage, collaborators, review]
  - id: S7
    type: secondary
    kind: other
    author: "J. M. S. Pearce"
    year: 2020
    citation: "Pearce, J. M. S. \"Dorothy Crowfoot Hodgkin OM, FRS (1910–1994).\" Hektoen International, 4 November 2020. https://hekint.org/2020/11/04/dorothy-crowfoot-hodgkin-om-frs-1910-1994/. Based on Pearce, Quakers in Medicine (Sessions of York)."
    url: "https://hekint.org/2020/11/04/dorothy-crowfoot-hodgkin-om-frs-1910-1994/"
    accessed: 2026-10-24
    reliability_note: "States Quaker affinities via marriage and pacifism but 'did not formally belong to the Society of Friends'."
    source_quality: "scholarly reconstruction"
    used_for: [worldview, childhood, heritage, collaborators, review]
  - id: S8
    type: primary
    kind: "published work by the subject"
    author: "Dorothy Crowfoot Hodgkin"
    year: 1964
    citation: "Hodgkin, Dorothy Crowfoot. \"The X-ray Analysis of Complicated Molecules.\" Nobel Lecture, 11 December 1964. NobelPrize.org PDF https://www.nobelprize.org/uploads/2018/06/hodgkin-lecture-1.pdf."
    url: "https://www.nobelprize.org/uploads/2018/06/hodgkin-lecture-1.pdf"
    accessed: 2026-10-24
    reliability_note: "Primary Nobel lecture; technical method only — no religion or explicit nature-order creed."
    source_quality: "primary / own words"
    used_for: [childhood, worldview, lane_b]
  - id: S9
    type: secondary
    kind: "institutional page"
    author: "Nobel Foundation"
    citation: "\"Dorothy Crowfoot Hodgkin.\" Nobel Prize / Women who changed science. https://www.nobelprize.org/stories/women-who-changed-science/dorothy-hodgkin/. Attributes: 'I believe in perfecting the world and trying to do everything to improve things, but not because I know what's to come of it.'"
    url: "https://www.nobelprize.org/stories/women-who-changed-science/dorothy-hodgkin/"
    accessed: 2026-10-24
    reliability_note: "Attributed quote without primary citation on the page; used only as humanitarian/peace voice, not for A. Primary interview unread."
    source_quality: "reference entry"
    used_for: [worldview]
  - id: S10
    type: secondary
    kind: other
    author: "NCUACS / Centre for Scientific Archives"
    year: 2004
    citation: "\"Catalogue of the papers and correspondence of Dorothy Mary Crowfoot Hodgkin OM FRS (1910–1994)\" supplementary catalogue (NCUACS 135/8/04). https://centreforscientificarchives.co.uk/wp-content/uploads/2024/01/HODGKIN_DOROTHY_MARY_CROWFOOT_SUPPLEMENTARY_v2.pdf."
    url: "https://centreforscientificarchives.co.uk/wp-content/uploads/2024/01/HODGKIN_DOROTHY_MARY_CROWFOOT_SUPPLEMENTARY_v2.pdf"
    accessed: 2026-10-24
    reliability_note: "Archive catalogue only. Notes notebook material on science and religion (possibly translation); Thomas Hodgkin 1959 letter wishing 'good old-fashioned Christian burial' (Ferry p. 387) — husband's wish, not Dorothy's."
    source_quality: "other"
    used_for: [worldview, review]
---

# Dorothy Hodgkin

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Dorothy Crowfoot Hodgkin (1910–1994), English chemist, solved the structures of penicillin (1945), vitamin B12 and insulin (1969) by X-ray crystallography and won the 1964 Nobel Prize in Chemistry [S1; S5]. Deepen D1: Ferry biography and Nobel lecture checked — still no own-voice place/deny of God; Perutz's "more Christian… than many believers" remains third-party [S3, p. 193; S6; S7]. primary_system BELOW_THRESHOLD. A BELOW_THRESHOLD; B 3 @0.5 alt 4 (P35, support corroborated on method); mid_basin BELOW_THRESHOLD. Not plotted. Chart-moving NO.

## Life and work

Born in Cairo; Sir John Leman School, Beccles; Somerville, Oxford; doctoral work with Bernal in Cambridge; Oxford from 1934 until 1977; Pugwash president 1975–88 [S1; S2; S5].

## Contribution and impact

Penicillin, vitamin B12 and insulin structures; first Wolfson Research Professor [S1; S2].

## Childhood and education

Eldest of four daughters of colonial educators and archaeologists, largely apart from her parents; crystals from about 10; Bragg's school book on seeing atoms [S1; S2; S3, p. 182; S6; S8]. Family religion: English Christian milieu (mother strong convictions; father less so); not Quaker by birth [S6; S7].

## Adult working worldview

Not established from her own words. Quaker affinities via marriage and pacifism, but she did not formally join the Society of Friends [S7]; Ferry: resisted rigid ideological labels [S6, ch. 9]. Dodson describes belief in social justice, hatred of militarism and socialist sympathies [S3, p. 213]; these are political views, not coded. Nobel-attributed "perfecting the world" line is humanitarian, not locus [S9].

## Heritage (context only)

English [S1]. Religious heritage by birth: English Christian milieu; Quaker connection by marriage later [S6; S7]. Context only.

## Timing

First lasting contribution 1942, the start of the penicillin structure work (solved by 1945), at 32 [S1; S2].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form partly present; circle unclear; A BELOW; B 3 @0.5; unplotted.

## Open questions

- Bodleian papers; Wolpert Passion for Science interview primary; SHI 1990 video transcript; NCUACS science-and-religion notebook pages.
- Settled this pass: Ferry OCR searched; Nobel lecture read; formal Quaker non-membership noted [S7].

## Research log

- 2026-10-02: Read Britannica (Ferry), the Nobel biography and Dodson's Royal Society memoir (publisher's PDF).
- 2026-10-24: Deepen D1. Ferry A Life (IA OCR); Nobel lecture PDF; Wikipedia dual bio; Hektoen/Pearce; NCUACS catalogue; Nobel women-story page. Wrote drafts/deepen_hodgkin-dorothy.md (untracked). No figures refresh. No fallacy_catalog.
