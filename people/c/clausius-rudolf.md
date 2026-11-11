---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 6
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, fourth batch: physical science 1600–1950)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to physics. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen D1 (queue #203/228, F 3, rank 216). Goals: firm B; seek any A; do not force plot. Read: Clausius 1865 ninth memoir English (Magie/Farber via Lemoyne Giunta; S4) — own-words 'The energy of the universe is constant' / 'The entropy of the universe strives toward a maximum'; Deutsche Biographie NDB Laue + ADB Reinganum (S5) — (evangelisch), Pfarrergeschlecht genealogy; Encyclopedia.com DSB (S6) — father Lutheran pastor; Bonn Rektoratsrede 1884 Über den Zusammenhang zwischen den großen Agentien der Natur (S7, OCR of scan) — physics of light/heat/electricity/ether only, no God/religion. B stays 3 @ 0.5 inference_from_work; support labelled corroborated (S1+S4; P48); alt 4 named (P35 — 1865 cosmic summary is working-science law statement, not a P16 law-and-exception / miracles claim). A stays UNKNOWN (P19): no first-person God/religion; evangelisch / Lutheran pastor line is heritage. primary_system UNKNOWN. mid UNKNOWN. Chart-moving NO. Heritage + childhood confession filled. P47 source_quality on S1–S7. No fallacy_catalog. No figures/. Draft, not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (fourth batch, RUNBOOK §1 order). Basics from Britannica and MacTutor. No writing of his on religion was found; his father was a pastor and school principal (MacTutor). primary_system BELOW_THRESHOLD (no candidate supported). B 4 at 0.5 from his working science (P6); A, C, D, E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. No interview used. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit, batch 4 (two blind runs at b21655b). #124 (run 1): candidate_codes_considered was empty; CHRIST is now listed as considered, not coded (upbringing by a minister father is never a code, §1; CODING_GUIDE §5.3), and the primary_system note updated. #131–132 (minor): birth date and place and death date and place 0.7 → 1.0, now citing MacTutor's Quick Info as well as Britannica (two independent sources agree). No worldview value changed. Decisions P12/P13 recheck: first_lasting_contribution_year 1850 unchanged. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Stage 3 lens-audit rulings applied to the batch's other records (OPEN_DECISIONS P14–P28, v8's picks, 2026-10-02). Schema 1.2 → 1.3. One reliable source caps a fact at 0.7; derived fields take the lowest certainty of their inputs; BELOW_THRESHOLD vs UNKNOWN per P19; kind lists (P21: research institute, school stage and run_by, scholarly edition); basis inference_from_work for 0.5 inference from working science (P24). Full before → after list: reports/stage3_rulings_changes.csv. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Span alignment (P29, P30 and its addendum): timing.major_work_period checked, 1850–1865 unchanged; worldview.working_years 1844–1888 → 1850–1865, equal to the span (P30 addendum f); evidence for every headline value checked against the span; no value or certainty changed. Listed in reports/p30_span_alignment.csv. Not reviewed."}
    - {date: 2026-10-08, by: "Grok Bot", summary: "Lens audit of batch C (dd91009), ruling R1, logged as P35 (v8's pick): B_cause 4 → 3 at 0.5, alternative 4, because B rests on working science only. No other value changes; mid_basin unchanged."}

identity:
  id: clausius-rudolf
  display_name: "Rudolf Clausius"
  roster:
    canonical_name: "Rudolf Clausius"
    rank: 216
    F: 3
    models: [Claude, DeepSeek, Gemini]
    band: "core (3–4)"
    status: core
    field: physics
    field_bucket: physics
  full_name: {value: "Rudolf Julius Emanuel Clausius", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts ('In full')"}], how_known: "Britannica."}
  native_name: {value: "Rudolf Julius Emanuel Clausius (German)", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}], how_known: "Britannica; German name."}
  aliases:
    - {name: "Clausius-Rudolf", kind: "roster alias"}

basics:
  birth:
    date: {value: "1822-01-02", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Quick Info"}, {source: S5, locator: "Lebensdaten / NDB (* 2.1.1822)"}], how_known: "Britannica, MacTutor, and Deutsche Biographie agree."}
    place: {value: "Köslin, Prussia", modern_name: "Koszalin, Poland", polity_then: "Kingdom of Prussia", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Quick Info ('Koslin, Prussia (now Koszalin, Poland)')"}, {source: S5, locator: "Geburtsort Köslin (Pommern)"}], how_known: "Three sources."}
  death:
    date: {value: "1888-08-24", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Quick Info"}, {source: S5, locator: "† 24.8.1888"}], how_known: "Three sources."}
    place: {value: "Bonn", modern_name: "Bonn, Germany", polity_then: "German Empire", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Quick Info"}, {source: S5, locator: "Sterbeort Bonn"}], how_known: "Three sources."}
  first_lasting_contribution_year: {value: 1850, certainty: 1.0, cites: [{source: S1, locator: "paragraph 2"}, {source: S2, locator: "Biography (1850 paper)"}], how_known: "Über die bewegende Kraft der Wärme, read to the Berlin Academy and published in Annalen der Physik in 1850; the second law."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "paragraph 2"}], how_known: "From first_lasting_contribution_year (P2)."}
  region_of_birth: {value: "Eastern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening ('Köslin, Prussia [Poland]')"}], how_known: "Modern Poland is Eastern Europe in data/reference/regions.csv (P3); then Prussia."}
  region_of_work: {value: "Western Europe", certainty: 1.0, cites: [{source: S1, locator: "paragraphs 2–3"}, {source: S2, locator: "Biography"}], how_known: "Berlin, Zürich, Würzburg, Bonn."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "As the sources record it."}
  languages_of_work: {value: [German], certainty: 0.7, cites: [{source: S2, locator: "Biography (1850 paper title)"}, {source: S4, locator: "German Annalen original"}], how_known: "Papers in Annalen der Physik in German; English translations secondary."}
  occupations: {value: ["mathematical physicist", "university professor"], certainty: 1.0, cites: [{source: S1, locator: "opening; paragraphs 2–3"}, {source: S2, locator: "Biography"}], how_known: "Two sources."}

contribution:
  primary_domain: physics
  fields: {value: ["thermodynamics", "kinetic theory of gases", "mathematical physics"], certainty: 1.0, cites: [{source: S1, locator: "opening; paragraph 2"}, {source: S2, locator: "Biography"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Second law of thermodynamics ('Heat cannot of itself pass from a colder to a hotter body')", year: "1850", kind: "law or principle", lasting: "foundation of thermodynamics", certainty: 1.0, cites: [{source: S1, locator: "paragraph 2"}, {source: S2, locator: "Biography (1850 paper)"}], how_known: "Two sources."}
    - {value: "Concept of entropy, applied to the theory of the steam engine; 1865 cosmic summary of the two laws", year: "1865", kind: "concept or term", lasting: "standard physics", certainty: 1.0, cites: [{source: S1, locator: "paragraph 2"}, {source: S4, locator: "closing (energy constant; entropy maximum)"}], how_known: "Britannica plus the 1865 ninth-memoir English (S4); name 'entropy' coined in that paper."}
    - {value: "Idea that molecules continually exchange atoms, later the basis of electrolytic dissociation", year: "1857", kind: theory, lasting: "precursor of ionic theory", certainty: 0.7, cites: [{source: S1, locator: "paragraph 2"}], how_known: "Britannica."}
  evidence_of_impact:
    - {value: "Credited with 'making thermodynamics a science'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works:
    - {value: "Über die bewegende Kraft der Wärme", year: 1850, kind: "paper or paper series", certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor."}
    - {value: "Ueber verschiedene für die Anwendung bequeme Formen der Hauptgleichungen der mechanischen Wärmetheorie (entropy; cosmic summary)", year: 1865, kind: "paper or paper series", certainty: 1.0, cites: [{source: S4, locator: "title and closing"}], how_known: "English excerpt of Annalen 125 (1865), S4."}
  honours:
    - {value: "Copley Medal", year: 1879, certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}], how_known: "Britannica."}
    - {value: "Iron Cross (for leading an ambulance corps in the Franco-Prussian War)", year: 1871, certainty: 0.7, cites: [{source: S2, locator: "Biography (1870–71)"}], how_known: "MacTutor."}
  definition_fit: {value: "clearly meets", rationale: "Formulated the second law and the concept of entropy.", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "Evangelical Lutheran / Protestant (evangelisch); father a Lutheran pastor; family of pastors on both sides", certainty: 1.0, cites: [{source: S2, locator: "Biography, paragraph 1"}, {source: S5, locator: "Genealogie (Pfarrergeschlecht); NDB (evangelisch)"}, {source: S6, locator: "opening (Lutheran pastor)"}], how_known: "MacTutor pastor father; DSB Lutheran pastor; NDB evangelisch + Pfarrergeschlecht. Heritage / baptismal affiliation — not adult worldview."}
  family_religious_practice: {value: UNKNOWN, how_known: "Father was pastor of his private school; household piety / attendance detail not stated beyond the office."}
  parents_and_household:
    - {value: "Father Carl Ernst Gottlieb Clausius, theologian, government school councillor, who founded and led a small private school and served as its pastor (later Pfarrer und Superintendent in Ueckermünde)", name: "Carl Ernst Gottlieb Clausius", role: father, certainty: 1.0, cites: [{source: S2, locator: "Biography, paragraph 1"}, {source: S5, locator: "Genealogie (V Carl Ernst Gottlieb)"}, {source: S6, locator: "opening"}], how_known: "MacTutor, NDB, DSB."}
    - {value: "Mother Charlotte Wilhelmine (née Schultze), daughter of Pastor Gottfried Immanuel Schultze", name: "Charlotte Wilhelmine Clausius (née Schultze)", role: mother, certainty: 0.7, cites: [{source: S5, locator: "Genealogie (M Charl. Wilh.)"}], how_known: "NDB genealogy."}
  household_circumstances: {value: "Large family; Rudolf the sixth of eighteen children (many reached adulthood)", certainty: 1.0, cites: [{source: S2, locator: "Biography, paragraph 1"}, {source: S5, locator: "sechste unter achtzehn Kindern"}, {source: S6, locator: "sixth son of the 18 children"}], how_known: "Three sources."}
  schooling:
    - {value: "His father's private school (Ueckermünde)", stage: "elementary school", years: "1820s–1830s", certainty: 0.5, cites: [{source: S2, locator: "Biography, paragraph 1"}, {source: S5, locator: "ADB (Privatschule … Uckermünde)"}], how_known: "MacTutor ('a few years'); ADB places the school at Ueckermünde.", run_by: "private"}
    - {value: "Gymnasium in Stettin (Szczecin)", stage: "grammar or secondary school", years: "–1840", certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraph 1"}], how_known: "MacTutor."}
    - {value: "University of Berlin: mathematics and physics (degree 1844); probationary year teaching at the Frederic-Werder Gymnasium", stage: university, years: "1840–1845", certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraph 2"}], how_known: "MacTutor."}
    - {value: "Boeck's Royal Seminary (1846); doctorate from Halle on the colours of the sky (1848)", stage: university, years: "1846–1848", certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraph 3"}], how_known: "MacTutor."}
  early_mathematics: {value: "advanced mathematics", note: "University mathematics and physics in Berlin; earlier mathematics not stated.", certainty: 0.5, cites: [{source: S2, locator: "Biography, paragraph 2"}], how_known: "MacTutor; university level only."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "His father, as principal of the school he attended", certainty: 0.5, cites: [{source: S2, locator: "Biography, paragraph 1"}], how_known: "MacTutor; mentorship is the coder's reading."}
  languages_in_childhood: {value: [German], certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraph 1"}], how_known: "Prussian family."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1850–1865", certainty: 0.7, cites: [{source: S1, locator: "paragraphs 2–3"}, {source: S2, locator: "Biography"}, {source: S4, locator: "1865 closing"}], how_known: "Equal to timing.major_work_period (P30 addendum f; span check 2026-10-02); 1865 paper closes the entropy span."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No statement by him on science and religion in S1–S7 (2026-10-24 deepen). Bonn rectorial address (S7) is unity of natural agents, not religion."}
  primary_system:
    value: UNKNOWN
    cites: [{source: S2, locator: "Biography"}, {source: S4, locator: "whole excerpt (thermodynamics only)"}, {source: S5, locator: "NDB (evangelisch); Genealogie"}, {source: S6, locator: "opening (Lutheran pastor father)"}, {source: S7, locator: "whole address (OCR; no God/religion)"}]
    how_known: "Deepen D1: no first-person belief profession. NDB (evangelisch) and Lutheran pastor family are heritage (S5, S6), not adult system (P19). Bonn Rektoratsrede (S7) silent on God. Under P19: UNKNOWN."
    note: "Lead open: Folie 1890 'portée métaphysique' is a scholar's metaphysical reading of the thermodynamics, not Clausius own-words religion; not opened in full this pass. Cropper Great Physicists chapter skimmed via secondary citations only."
  secondary_system: {value: UNKNOWN, how_known: "No system evidence in the sources read."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Considered, not coded: no statement of his on religion was read; being brought up by a Lutheran pastor father / NDB evangelisch is upbringing and heritage, never a code (CODING_GUIDE §1; P19).", cites: [{source: S2, locator: "Biography, paragraph 1"}, {source: S5, locator: "evangelisch; Pfarrergeschlecht"}, {source: S6, locator: "Lutheran pastor"}]}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing of his on God or the divine in S1–S7 (P19). Evangelisch / Lutheran parents are heritage, not A. Bonn rectorial address (S7) discusses Naturagentien only."}
    B_cause:
      value: 3
      basis: inference_from_work
      certainty: 0.5
      support: corroborated
      cites: [{source: S1, locator: "paragraphs 2–3 (second law; entropy)"}, {source: S4, locator: "closing (energy of the universe constant; entropy strives toward a maximum)"}]
      how_known: "Scientist (P30). B from working science with no statement of his own on law and exception / miracles, so 3 at 0.5, alternative 4, never 4 (P35). Two independent source ids (Britannica synthesis + Clausius 1865 own-words cosmic summary) → corroborated (P48). Named alternative 4 kept under P35."
      rationale: "Thermodynamics as general laws of nature: second law / entropy. Britannica (S1): second law and entropy. Clausius 1865 own words (S4): 'The energy of the universe is constant. The entropy of the universe strives toward a maximum' — universal lawful statements about heat/energy. No miracle, petition, or exception-to-law claim in anything read (including the 1884 Bonn address, S7). P35 bars lifting to 4 (or to written_profession certainty ≥0.7) without his own statement on law-and-exception. Named alternative: 4."
      alternatives:
        - {value: 4, note: "Working science cannot tell lawful-with-exceptions from exceptionless (P35). Would need an own-words no-exception / miracles claim (Pasteur/Wilson pattern). The 1865 cosmic summary states universal heat laws, not that nature admits no divine exception.", cites: [{source: S1, locator: "paragraphs 2–3"}, {source: S4, locator: "closing"}]}
    C_ledger: {value: UNKNOWN, how_known: "Nothing on judgement, afterlife or reward in the sources read (P19)."}
    D_authority: {value: UNKNOWN, how_known: "No statement on revelation in the sources read (P19)."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Scored on the world's order (P7). Nothing read addresses favour for a group in events. Working science (including the 1865 'laws of the universe') bears on the first question (same laws everywhere) but not on favour for a group in events, so E stays BELOW_THRESHOLD; not scored from working science alone (P19)."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, so mid_basin is UNKNOWN (§6 precedence, decision P19)."}
  statements:
    - text: "The energy of the universe is constant."
      cites: [{source: S4, locator: "closing summary, thesis 1"}]
      date: "1865"
      context: "Ninth memoir (Annalen der Physik 125, 1865); English Magie/Farber via Lemoyne Giunta. Own-words cosmic statement of the first law. Used to corroborate B inference_from_work (P48); not a P16 law-and-exception / miracles statement, so does not lift P35 certainty (P49)."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
    - text: "The entropy of the universe strives toward a maximum."
      cites: [{source: S4, locator: "closing summary, thesis 2"}]
      date: "1865"
      context: "Same closing of the 1865 ninth memoir. Companion to the energy thesis; B corroboration only under P35."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
  changes_over_life: []
  coder_notes: "Deepen D1 verified the widely quoted 1865 energy/entropy summary against Magie/Farber English (S4). Bonn Rektoratsrede 1884 (S7) OCR'd in full for God/religion language — none. Folie 1890 metaphysical essay not used to score A (scholar's reading)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Prussian (Pomeranian) German; a German patriot", certainty: 0.7, cites: [{source: S2, locator: "Biography (Zürich and 1870 paragraphs)"}], how_known: "MacTutor ('a country he deeply loved'; 'a German patriot')."}
  religious_heritage_by_birth: {value: "Evangelical Lutheran / Protestant (evangelisch); pastor family both sides", certainty: 1.0, cites: [{source: S5, locator: "NDB (evangelisch); Genealogie (Pfarrergeschlecht)"}, {source: S6, locator: "Lutheran pastor father"}], how_known: "NDB confession field + DSB Lutheran pastor + pastor genealogy. Context only — not coded as adult primary_system."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated; evangelisch affiliation implies baptismal belonging but no rite record read."}
  childhood_catechism: {value: UNKNOWN, how_known: "Father's school was pastor-led; catechism detail not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1850–1865", certainty: 0.7, cites: [{source: S1, locator: "paragraphs 2–3"}, {source: S2, locator: "Biography"}, {source: S4, locator: "1865"}], how_known: "Second law to entropy paper; coder's reading."}
  age_at_first_lasting_contribution: {value: 28, certainty: 1.0, cites: [{source: S1, locator: "opening; paragraph 2"}, {source: S2, locator: "Biography (read 18 February 1850)"}], how_known: "Born 2 January 1822; paper read 18 February 1850."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "B inferred from working science with no LIO-type own statement is not an LIO-type view (P27); A/C/D empty."}
  lio_views_relative_to_major_work: {value: "unclear", rationale: "No worldview statement found for A/C/D; B is working-science inference only.", certainty: 0.5, cites: [{source: S2, locator: "Biography"}, {source: S4, locator: "closing"}], how_known: "Nothing dated as LIO-type view."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "No adult belief profession dated to the span."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "He built thermodynamics from two stated principles and worked out their mathematical consequences (S1; S2; S4), an axiomatic style within physics.", certainty: 0.5, cites: [{source: S2, locator: "Biography (1850 paper)"}, {source: S4, locator: "opening (two main theses)"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "Biography, paragraphs 1–2"}], how_known: "Nothing on method in his schooling."}
  circle_present: {value: "unclear", rationale: "No God-Nature statement found; not scored from absence.", certainty: 0.5, cites: [{source: S2, locator: "Biography"}, {source: S7, locator: "whole address"}], how_known: "No evidence either way."}
  reading: "As belief, not finding: form partly present (principles and consequences), circle unclear. The record does not test H1."
  notes: ""

institutions:
  - {value: "Royal Artillery and Engineering School, Berlin; Docent at the University of Berlin", role: "professor of physics", years: "1850–1855", kind: university, certainty: 1.0, cites: [{source: S1, locator: "paragraph 2"}, {source: S2, locator: "Biography (1850)"}], how_known: "Two sources."}
  - {value: "Polytechnikum and University of Zürich", role: "professor of mathematical physics", years: "1855–1867", kind: university, certainty: 1.0, cites: [{source: S1, locator: "paragraph 2"}, {source: S2, locator: "Biography (1855)"}], how_known: "Two sources."}
  - {value: "University of Würzburg", role: "professor of physics", years: "1867–1869", kind: university, certainty: 0.7, cites: [{source: S1, locator: "paragraph 3"}], how_known: "Britannica."}
  - {value: "University of Bonn", role: "professor of physics; rector 1884–85", years: "1869–1888", kind: university, certainty: 1.0, cites: [{source: S1, locator: "paragraph 3"}, {source: S2, locator: "Biography (1884)"}, {source: S7, locator: "title page (Rektoratsantritt 18 Oct 1884)"}], how_known: "Three sources."}
collaborators:
  - {value: "Sadi Carnot", roster_id: carnot-sadi, relation: "influenced by", note: "he restated Carnot's principle on the efficiency of heat engines", certainty: 0.7, cites: [{source: S1, locator: "paragraph 3"}], how_known: "Britannica."}
  - {value: "Adelheid Rimpau", relation: family, note: "first wife (married 1859; died 1875)", certainty: 0.7, cites: [{source: S2, locator: "Biography (1859, 1875)"}, {source: S5, locator: "Genealogie"}], how_known: "MacTutor and NDB."}

review:
  roster_status_reason: {value: "Core in v8 (F 3: Claude, DeepSeek, Gemini).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 216"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "A and primary_system UNKNOWN: no own-words belief; evangelisch is heritage."
    - "B faded (0.5) under P35; support now corroborated (S1+S4)."
    - "Bonn Rektoratsrede OCR'd; image PDF — OCR imperfect but no God/religion terms found."
  open_questions:
    - "Open Folie 1890 (portée métaphysique) only if it quotes Clausius on God/religion; unused as scholar metaphysics."
    - "Cropper Great Physicists ch. on Clausius — full chapter for any private remark."
    - "Own-words laws-of-nature / exception claim that would lift B past P35 (1865 cosmic summary does not)."
    - "German original Annalen 125 closing for locator precision (English Magie/Farber used)."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "The Editors of Encyclopaedia Britannica"
    citation: "The Editors of Encyclopaedia Britannica. \"Rudolf Clausius.\" Encyclopaedia Britannica (last updated 20 August 2026). https://www.britannica.com/biography/Rudolf-Clausius."
    url: "https://www.britannica.com/biography/Rudolf-Clausius"
    accessed: 2026-10-02
    source_quality: "reference entry"
    reliability_note: "Unsigned short article. Paragraphs counted from the opening '(born January 2, 1822'. Not re-fetched 2026-10-24 (timeout); prior read retained."
    used_for: [identity, basics, contribution, worldview, timing, institutions, collaborators]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "J J O'Connor and E F Robertson"
    citation: "O'Connor, J. J., and E. F. Robertson. \"Rudolf Julius Emmanuel Clausius.\" MacTutor History of Mathematics, University of St Andrews. https://mathshistory.st-andrews.ac.uk/Biographies/Clausius/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Clausius/"
    accessed: 2026-10-02
    source_quality: "other"
    reliability_note: "Biography quoting his brother Robert's memoir; paragraphs counted from 'Rudolf Clausius's father'."
    used_for: [basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    source_quality: "study roster"
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "Rudolf Clausius"
    citation: "Clausius, Rudolf. 'Ueber verschiedene für die Anwendung bequeme Formen der Hauptgleichungen der mechanischen Wärmetheorie.' Annalen der Physik 125 (1865): 353–400. English excerpts (Magie, A Source Book in Physics, 1935; Farber, Milestones of Modern Chemistry, 1966) at https://web.lemoyne.edu/giunta/Clausius1865.pdf."
    url: "https://web.lemoyne.edu/giunta/Clausius1865.pdf"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "Authoritative English of the 1865 ninth memoir closing (energy/entropy of the universe). Whole Lemoyne excerpt read; German Annalen not opened this pass."
    used_for: [contribution, worldview, statements, timing]
  - id: S5
    type: secondary
    kind: encyclopedia
    author: "Max von Laue (NDB); Max Reinganum (ADB)"
    citation: "Laue, Max von. 'Clausius, Rudolf Julius Emanuel.' Neue Deutsche Biographie 3 (1957): 276–278; plus ADB 55 (1910): 720–729 (Reinganum). Deutsche Biographie online. https://www.deutsche-biographie.de/gnd116540486.html."
    url: "https://www.deutsche-biographie.de/gnd116540486.html"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "NDB signed article: (evangelisch), Pfarrergeschlecht genealogy, career. ADB long scientific life. Index Konfession 'evangelisch?' — NDB body says evangelisch without '?'. Confession = heritage, not adult primary_system."
    used_for: [basics, childhood, worldview, heritage, institutions, collaborators]
  - id: S6
    type: secondary
    kind: encyclopedia
    author: "Dictionary of Scientific Biography (via Encyclopedia.com)"
    citation: "'Rudolf Julius Emanuel Clausius.' Encyclopedia.com (DSB text). https://www.encyclopedia.com/people/science-and-technology/physics-biographies/rudolf-julius-emanuel-clausius."
    url: "https://www.encyclopedia.com/people/science-and-technology/physics-biographies/rudolf-julius-emanuel-clausius"
    accessed: 2026-10-24
    source_quality: "scholarly edition or monograph"
    reliability_note: "DSB-derived biography; whole article read. Opening: father 'a Lutheran pastor'. Also quotes the 1865 energy/entropy summary (used as cross-check; B cites go to S4 primary)."
    used_for: [childhood, worldview, heritage]
  - id: S7
    type: primary
    kind: "published work by the subject"
    author: "Rudolf Clausius"
    citation: "Clausius, Rudolf. Über den Zusammenhang zwischen den großen Agentien der Natur. Rede gehalten beim Antritt des Rectorats der Rheinischen Friedrich-Wilhelms-Universität am 18. October 1884. Bonn: Max Cohen & Sohn, 1885. Scan: https://www.historische-kommission-muenchen-editionen.de/rektoratsreden/pdf/Bonn_1884_Clausius_Zusammenhang_Agentien_Natur.pdf."
    url: "https://www.historische-kommission-muenchen-editionen.de/rektoratsreden/pdf/Bonn_1884_Clausius_Zusammenhang_Agentien_Natur.pdf"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "Image PDF OCR'd (tesseract eng; 14 pages). Physics of light, heat, magnetism, electricity, ether — unity of Naturagentien. No God, religion, Schöpfung, or Kirche language found. Used as A-negative primary read, not to lift B."
    used_for: [worldview, institutions, lane_b]
---

# Rudolf Clausius

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Rudolf Clausius (1822–1888), German mathematical physicist, stated the second law of thermodynamics (1850) and developed entropy (1865) [S1; S2; S4]. Deepen D1: primary_system UNKNOWN; A UNKNOWN; B 3 @ 0.5 inference_from_work, support corroborated (S1+S4), alt 4 (P35); mid_basin UNKNOWN. Not plotted. Evangelical Lutheran heritage (pastor family) is context only [S5; S6].

## Life and work

Stettin Gymnasium, Berlin, Halle doctorate (1848); professor at Berlin, Zürich, Würzburg and Bonn; led a student ambulance corps in 1870–71; Bonn rector 1884–85 [S1; S2; S7].

## Contribution and impact

Second law (1850), entropy and the 1865 cosmic summary of the two laws, kinetic theory, molecular exchange in electrolysis [S1; S4].

## Childhood and education

Sixth of eighteen children of Lutheran pastor Carl Ernst Gottlieb Clausius; father's school then Stettin Gymnasium; Berlin and Halle [S2; S5; S6].

## Adult working worldview

No first-person God or religion statement in sources read. NDB evangelisch / Lutheran pastor line is heritage [S5; S6]. Bonn Rektoratsrede 1884 is Naturagentien physics only [S7]. B from working science at 3 @ 0.5, corroborated by Britannica and the 1865 own-words energy/entropy summary; P35 keeps alt 4 [S1; S4].

## Heritage (context only)

Evangelical Lutheran / Protestant (evangelisch); pastor family both sides [S5; S6]. Context only.

## Timing

First lasting contribution 1850, at 28; entropy paper 1865 closes the span [S1; S2; S4].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form partly present; circle unclear.

## Open questions

- Folie 1890 only if it quotes Clausius on God/religion.
- Cropper chapter; German Annalen 125 locator check.
- Own-words law-and-exception claim for B lift.

## Research log

- 2026-10-24: Deepen D1. Primary 1865 (S4); Deutsche Biographie NDB/ADB (S5); Encyclopedia.com DSB (S6); Bonn Rektoratsrede OCR (S7). B support corroborated; A/primary/mid UNKNOWN; evangelisch heritage filled. Person-file-only local commit. No fallacy_catalog. No figures/.
- 2026-10-08: P35 lens audit: B 4 → 3 @ 0.5, alt 4.
- 2026-10-02: Britannica and MacTutor; stage-3 / span alignment.
