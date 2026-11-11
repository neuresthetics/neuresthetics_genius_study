---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 6
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, third batch: physical science 1600–1950)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to physics. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (third batch, RUNBOOK §1 order). Basics from Britannica (Kojevnikov, first page), MacTutor and the Nobel biography. No writing by Dirac on religion could be checked: the 1963 Scientific American article is access-restricted on the Internet Archive, the FSU Library scan of his 1976 Lindau lecture notes sits behind a bot challenge, and the 1927 Solvay remarks survive only in Heisenberg's later reconstruction (another person's report). primary_system BELOW_THRESHOLD (ATHE candidate, stub). B 4 at 0.5 from his working science (P6); A, C, D, E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Schema 1.1 → 1.2 (decision P8 adds basis recorded_interview and statement kind 'recorded interview'); no content change."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Stage 3 lens-audit rulings applied to the batch's other records (OPEN_DECISIONS P14–P28, v8's picks, 2026-10-02). Schema 1.2 → 1.3. One reliable source caps a fact at 0.7; derived fields take the lowest certainty of their inputs; BELOW_THRESHOLD vs UNKNOWN per P19; kind lists (P21: research institute, school stage and run_by, scholarly edition); basis inference_from_work for 0.5 inference from working science (P24). Full before → after list: reports/stage3_rulings_changes.csv. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Span alignment (P29, P30 and its addendum): timing.major_work_period 1925–1933 → 1925–1934; worldview.working_years 1923–1984 → 1925–1934, equal to the span (P30 addendum f); lasting item added: Vacuum polarization (1934); evidence for every headline value checked against the span; no value or certainty changed. Listed in reports/p30_span_alignment.csv. Not reviewed."}
    - {date: 2026-10-08, by: "Grok Bot", summary: "Lens audit of batch C (dd91009), ruling R1, logged as P35 (v8's pick): B_cause 4 → 3 at 0.5, alternative 4, because B rests on working science only. No other value changes; mid_basin unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #123 / F4 rank 124). Goals: open SciAm 1963 / Lindau / Farm Hall or other own-voice on God; lift A/primary if justified; keep honest BELOW if secondary-only. Opened SciAm May 1963 full text via SciAm guest-blog republish (S5); Lindau 1976 Mediatheque English transcript (S7; no God talk in delivered lecture); Wikipedia EN dual bio (S6, P50). Farm Hall not a Dirac source (Solvay misattribution). A stays BELOW_THRESHOLD: SciAm 'God is a mathematician' is hedged metaphor ('One could perhaps describe'); Solvay 1927 still Heisenberg reconstruction (P49, not own voice); 1971 conditional God/life quote only via Wikipedia citing Kragh (secondary). B 3 stays @0.5: basis inference_from_work→written_profession (S5 'fundamental physical laws' / 'nature is so constructed'; S7 math-beauty as guide to laws); P16 Hilbert / P35 keep 0.5 without exception/no-exception claim (alt 4); support corroborated. primary_system / mid_basin stay BELOW_THRESHOLD. Chart-moving NO. P47 source_quality on S1–S7. No fallacy_catalog. No figures/. Draft, not reviewed."}

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
  native_name: {value: "Paul Adrien Maurice Dirac (English)", certainty: 0.7, cites: [{source: S3, locator: "paragraph 1"}], how_known: "English name."}
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
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S3, locator: "paragraph 1"}], how_known: "As the sources record it."}
  languages_of_work: {value: [English], certainty: 0.7, cites: [{source: S3, locator: "paragraph 2"}], how_known: "Papers in the Proceedings of the Royal Society."}
  occupations: {value: ["theoretical physicist", "university professor"], certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Biography"}], how_known: "Two sources."}

contribution:
  primary_domain: physics
  fields: {value: ["quantum mechanics", "quantum electrodynamics", "theoretical physics"], certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Summary"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "General mathematical formulation of quantum mechanics (q-numbers, Poisson-bracket analogy; transformation theory)", year: "1925–1926", kind: theory, lasting: "foundation of quantum mechanics", certainty: 1.0, cites: [{source: S1, locator: "paragraph after 'Physics and Natural Law'"}, {source: S2, locator: "Biography (1925 paragraph)"}], how_known: "Two sources."}
    - {value: "Quantum theory of radiation (second quantization)", year: "1927", kind: theory, lasting: "beginning of quantum electrodynamics", certainty: 0.7, cites: [{source: S1, locator: "paragraph on QED"}], how_known: "Britannica."}
    - {value: "Relativistic wave equation for the electron (Dirac equation)", year: "1928", kind: theory, lasting: "standard physics; Nobel Prize 1933", certainty: 1.0, cites: [{source: S1, locator: "'In 1928 Dirac published'"}, {source: S3, locator: "paragraphs 2–3"}], how_known: "Two sources."}
    - {value: "Prediction of antimatter (the positron)", year: "1930–1931", kind: discovery, lasting: "confirmed 1932; antiparticles a universal property of matter", certainty: 1.0, cites: [{source: S1, locator: "'In 1928 Dirac published', paragraphs 2–3"}, {source: S3, locator: "paragraph 2"}], how_known: "Two sources."}
    - {value: "Fermi–Dirac statistics", year: "1926", kind: "law or principle", lasting: "standard physics", certainty: 0.7, cites: [{source: S1, locator: "paragraph after 'Physics and Natural Law'"}], how_known: "Britannica."}
    - {value: "Vacuum polarization", year: 1934, kind: "concept or term", lasting: "used in the renormalized quantum electrodynamics built after the Second World War", certainty: 0.7, cites: [{source: S1, locator: "paragraph on quantum electrodynamics in the 1930s ('These concepts, and also Dirac’s idea of vacuum polarization (1934), helped a new generation of theorists after World War II invent ways of subtracting infinities')"}], how_known: "One encyclopedia article, so 0.7. Added 2026-10-02 under the P30 addendum (the latest lasting work must be listed). Not added: the 1933 Lagrangian paper (S1; S2), which falls inside the span, and the 1938 classical electron theory (S2, 'famous paper'), which no source read calls lasting."}
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
  definition_fit: {value: "clearly meets", rationale: "A founder of quantum mechanics and QED.", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Sources agree."}

childhood:
  family_religion: {value: "Mother from a Cornish Methodist family; father's religion not stated in sources read", certainty: 0.7, cites: [{source: S6, locator: "Early life"}], how_known: "Wikipedia EN (P50 dual bio); corroborates MacTutor's English mother without naming the Methodist detail."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father, Charles Adrien Ladislas Dirac, Swiss-born French teacher at the Merchant Venturers' school, a strict disciplinarian", name: "Charles Dirac", role: father, certainty: 1.0, cites: [{source: S2, locator: "Biography, paragraph 1"}, {source: S1, locator: "childhood paragraph"}], how_known: "Two sources."}
    - {value: "Mother, Florence Hannah Holten, from Cornwall, working in a Bristol library when she met Charles", name: "Florence Dirac (née Holten)", role: mother, certainty: 1.0, cites: [{source: S2, locator: "Biography, paragraph 1"}, {source: S3, locator: "paragraph 1"}], how_known: "Two sources (English mother)."}
  household_circumstances: {value: "Strict, unhappy home (oppressive paternal discipline); French only at the father's table; an older brother (Reginald, who later took his own life) and a younger sister", certainty: 1.0, cites: [{source: S2, locator: "Biography, paragraphs 2, 7"}, {source: S1, locator: "childhood paragraph"}], how_known: "Two sources."}
  schooling:
    - {value: "Bishop Primary School (as MacTutor names it), Bristol", stage: "elementary school", years: "–1914", certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraph 3"}], how_known: "MacTutor; nearest stage."}
    - {value: "Merchant Venturers' Technical College secondary school, Bristol", stage: "grammar or secondary school", years: "1914–1918", certainty: 1.0, cites: [{source: S2, locator: "Biography, paragraph 3"}, {source: S3, locator: "paragraph 1"}], how_known: "Two sources."}
    - {value: "University of Bristol: electrical engineering (BSc 1921), then mathematics (first class, 1923)", stage: university, years: "1918–1923", certainty: 1.0, cites: [{source: S1, locator: "education paragraph"}, {source: S2, locator: "Biography, paragraphs 4–5"}], how_known: "Two sources."}
    - {value: "St John's College, Cambridge, research student under Ralph Fowler (PhD 1926)", stage: university, years: "1923–1926", certainty: 1.0, cites: [{source: S2, locator: "Biography, paragraph 6"}, {source: S3, locator: "paragraph 1"}], how_known: "Two sources."}
  early_mathematics: {value: "advanced mathematics", note: "At school he studied from books ahead of his class (his own account quoted by MacTutor).", certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraph 3"}], how_known: "MacTutor quoting Dirac."}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure:
    - {value: "Early access to the school's science laboratories during World War I", certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraph 3"}], how_known: "MacTutor."}
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [English, French], certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraph 2"}], how_known: "French at his father's table."}
  notable_events:
    - {value: "Elder brother Reginald took his own life while Paul was a research student", year: "1925", certainty: 0.7, cites: [{source: S2, locator: "Biography (research-student paragraph)"}], how_known: "MacTutor; year from the period described."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1925–1934", certainty: 1.0, cites: [{source: S1, locator: "opening to 1928 paragraphs; paragraph on quantum electrodynamics in the 1930s (vacuum polarization, 1934)"}, {source: S2, locator: "Biography"}], how_known: "Equal to timing.major_work_period (P30 addendum f; span check 2026-10-02). Was 1923–1984: From research student to death."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "SciAm 1963 (S5) uses hedged God-as-mathematician metaphor for nature's mathematical construction; it does not state a relation between science and religion as domains. 1971 conditional (S6 via Kragh) not opened as primary."}
  primary_system:
    value: BELOW_THRESHOLD
    cites: [{source: S5, locator: "May 1963 SciAm, God-as-mathematician paragraph"}, {source: S6, locator: "Views on religion (Solvay; 1971)"}]
    how_known: "Deepen D1 opened SciAm 1963 (S5) and Lindau 1976 transcript (S7). SciAm's God language is hedged metaphor for mathematical nature, not a system profession. Solvay 1927 anti-religion speech remains Heisenberg's reconstruction (P49) and is not scored as own voice. Wikipedia (S6) quotes a 1971 conference conditional on God/life via Kragh 1990 pp. 256–257 — secondary only; Kragh and the FSU 'God and the Big Bang' / Lindau handwritten notes (fsu:198, fsu:200) were not opened. Honest BELOW_THRESHOLD (P19)."
    note: "Lead candidates still ATHE (Solvay tradition, unusable for coding) and AGNOS (1971 conditional; secondary). Both stub system files (flag). No Farm Hall Dirac source."
  secondary_system: {value: UNKNOWN, how_known: "No second system in S1–S7."}
  candidate_codes_considered:
    - {code: ATHE, reason: "Still a lead from the Solvay tradition, not coded: Heisenberg memoir reconstruction and Pauli's quip are other people's reports (P49). SciAm 1963 does not deny God. ATHE is a stub system file (flag).", cites: [{source: S6, locator: "Views on religion"}]}
    - {code: AGNOS, reason: "Stronger lead after deepen: Wikipedia (S6) quotes 1971 conference language that treats God's existence as conditional on whether life requires divine influence — open hypothesis, not commitment. Not coded: quote reaches us only through Wikipedia citing Kragh; primary not opened. AGNOS is a stub system file (flag).", cites: [{source: S6, locator: "Views on religion (1971)"}]}
  lio_axes:
    A_locus:
      value: BELOW_THRESHOLD
      how_known: "SciAm 1963 (S5) uses hedged 'One could perhaps describe… God is a mathematician' metaphor for nature's mathematical construction — not a firm placing of God as transcendent maker (A 1) and not a denial (A 4). Solvay 1927 remains Heisenberg reconstruction (P49). 1971 conditional (S6 via Kragh) is secondary and suspends rather than places. Stays BELOW_THRESHOLD (P19)."
      note: "Gap: FSU DigiNole fsu:198 'God and the Big Bang' (1978) and fsu:200 Lindau handwritten notes (catalogue: theological issues) still behind bot wall; Kragh 1990 / Farmelo 2009 / 1933 notes not opened."
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.5
      support: corroborated
      cites: [{source: S5, locator: "May 1963 SciAm, fundamental physical laws / nature is so constructed"}, {source: S7, locator: "Lindau 1976 transcript, mathematical beauty as basic idea"}, {source: S1, locator: "QED and 1928 paragraphs"}]
      how_known: "Own published words (S5) plus own spoken lecture transcript (S7). Independent source ids → corroborated (P48). Certainty held at 0.5: lawful-order remark without a stated no-exception or limited-exception claim (P16 Hilbert addendum / P35)."
      rationale: "Scored on his account of nature (P6). Written profession: 'fundamental physical laws are described in terms of a mathematical theory of great beauty and power' and 'nature is so constructed' (S5). Lindau 1976: 'physical laws must be based on beautiful equations' / 'The underlying equations should have great mathematical beauty' (S7). Working science (S1) still shows statistical/mathematical law with no miracle read. No stated miracle, petition, or no-exception claim → B 3 at 0.5, alternative 4 (P16 Hilbert / P35), never 4."
      alternatives:
        - {value: 4, note: "P16 Hilbert / P35: lawful-order remark without a no-exception claim cannot score 4.", cites: [{source: S5, locator: "fundamental physical laws paragraph"}]}
    C_ledger: {value: UNKNOWN, how_known: "Nothing on reward, punishment or afterlife in S1–S7."}
    D_authority: {value: UNKNOWN, how_known: "No statement on revelation versus observation in S1–S7.", note: "Mathematical beauty as theory-guide (S5, S7) is method within physics, not D."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Scored on the world's order (P7). Nothing read addresses favour for a group in events; not scored from working science alone (same treatment as Fermi and Curie)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "P4 test: A_locus is BELOW_THRESHOLD and B_cause remains 0.5 under P16 Hilbert / P35, under the test's 0.7 bar. Deepen D1 did not darken B."}
  statements:
    - text: "It seems to be one of the fundamental features of nature that fundamental physical laws are described in terms of a mathematical theory of great beauty and power, needing quite a high standard of mathematics for one to understand it. You may wonder: Why is nature constructed along these lines? One can only answer that our present knowledge seems to show that nature is so constructed. We simply have to accept it. One could perhaps describe the situation by saying that God is a mathematician of a very high order, and He used very advanced mathematics in constructing the universe."
      cites: [{source: S5, locator: "May 1963 SciAm guest-blog republish of the full article"}]
      date: "1963-05"
      context: "Scientific American essay 'The Evolution of the Physicist's Picture of Nature'. The God sentence is hedged ('One could perhaps describe') and is used as metaphor for mathematical construction of nature; scored for B lawfulness, not for A."
      axes: [B_cause, A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Full text read via Scientific American guest-blog republish (2010) of the May 1963 article. IA lending-only scan not required once the publisher republish was opened."
    - text: "it seems to me now that this basic idea one can have in physics is to suppose that physical laws must be based on beautiful equations. That is the only really important requirement. The underlying equations should have great mathematical beauty."
      cites: [{source: S7, locator: "Lindau Mediatheque English transcript, Basic Beliefs and Prejudices in Physics, 29 June 1976"}]
      date: "1976-06-29"
      context: "Lindau Nobel lecture; own voice on method. Delivered lecture has no God/theology content (FSU catalogue note on handwritten notes covering God not confirmed from the spoken transcript)."
      axes: [B_cause]
      kind: other
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Mediatheque English transcript/subtitles opened 2026-10-24. Handwritten notes fsu:200 still unopened."
  changes_over_life: []
  coder_notes: "ATHE and AGNOS are stub system files (flag). Deepen D1 (2026-10-24): SciAm May 1963 blocker cleared via SciAm guest-blog republish (S5); Lindau 1976 spoken transcript opened (S7) — no God talk in the delivered lecture. Remaining blockers: FSU DigiNole fsu:198 ('God and the Big Bang', 1978) and fsu:200 (Lindau handwritten notes; catalogue mentions theological issues) behind bot wall; Kragh Dirac: A Scientific Biography (1990) and Farmelo The Strangest Man (2009) not opened; 1933 notes cited by Kragh not opened. Solvay 1927 remains Heisenberg reconstruction (P49) — another person's report ≠ own voice. Farm Hall is not a Dirac source. SciAm God sentence is metaphorical/hedged → does not lift A. 1971 conditional (S6 via Kragh) kept as AGNOS lead only."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "English mother, Swiss father (from Monthey, Valais)", certainty: 1.0, cites: [{source: S2, locator: "Biography, paragraph 1"}, {source: S3, locator: "paragraph 1"}], how_known: "Two sources."}
  religious_heritage_by_birth: {value: "Maternal Cornish Methodist family; father's affiliation not stated", certainty: 0.7, cites: [{source: S6, locator: "Early life"}], how_known: "Wikipedia EN. Context only — never a worldview code."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1925–1934", certainty: 1.0, cites: [{source: S1, locator: "opening to 1928 paragraphs; paragraph on quantum electrodynamics in the 1930s (vacuum polarization, 1934)"}, {source: S2, locator: "Biography"}], how_known: "From quantum mechanics (1925–1926) to vacuum polarization (1934), the first and last listed lasting contributions (P29). Span check 2026-10-02 (P29, P30 and its addendum): was 1925–1933. S1 names his 1934 vacuum polarization among the ideas that later made the predictions of quantum electrodynamics finite, so it was added as the latest lasting item."}
  age_at_first_lasting_contribution: {value: 23, certainty: 1.0, cites: [{source: S3, locator: "paragraphs 1–2"}], how_known: "Born August 1902; work of late 1925."}
  first_evidence_of_lio_type_views: {value: "1963", certainty: 0.7, cites: [{source: S5, locator: "May 1963 SciAm"}], how_known: "First checkable own-voice LIO-type remark opened this pass: SciAm on fundamental physical laws / nature so constructed (B-type). Major-work span is 1925–1934, so this is after the span."}
  lio_views_relative_to_major_work: {value: "after major work", rationale: "SciAm 1963 is decades after major_work_period 1925–1934. No checkable LIO-type own voice inside the span was opened (Solvay 1927 is Heisenberg reconstruction).", certainty: 0.7, cites: [{source: S5, locator: "May 1963 SciAm"}], how_known: "Date of S5 vs timing.major_work_period."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "He sought laws through mathematical formalism and beauty and argued 'with unbeatable logic' (S2, quoting Pais et al.), but from equations, not definitions and axioms in the Euclidean manner.", certainty: 0.5, cites: [{source: S1, locator: "1928 paragraphs"}, {source: S2, locator: "Biography (1930)"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "Biography, paragraph 3"}], how_known: "Rapid early mathematics; nothing on method."}
  circle_present: {value: "unclear", rationale: "SciAm 1963 uses God-as-mathematician metaphor for nature's math; hedged and conventional, not a circle claim (Deus sive Natura). Not scored from metaphor alone.", certainty: 0.5, cites: [{source: S5, locator: "God is a mathematician paragraph"}], how_known: "Own words opened; still unclear as circle."}
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
  - {value: "Eugene Wigner", relation: family, note: "brother-in-law: Dirac married Wigner's sister Margit in 1937", certainty: 0.7, cites: [{source: S2, locator: "Biography (1934–35)"}], how_known: "MacTutor."}

review:
  roster_status_reason: {value: "Core in v8 (F 4: Claude, DeepSeek, Gemini, GPT).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 124"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Pontifical Academy of Sciences membership: 1961 (Nobel page) vs 1958 (MacTutor)."
    - "Britannica read as its first page only."
    - "1971 God/life conditional reaches the file only via Wikipedia citing Kragh 1990 — secondary; primary not opened."
    - "FSU DigiNole fsu:198 and fsu:200 still behind bot wall this pass."
  open_questions:
    - "Open FSU DigiNole fsu:198 (God and the Big Bang, 1978) and fsu:200 (Lindau handwritten notes) via a browser session that clears the bot wall."
    - "Read Kragh, Dirac: A Scientific Biography (1990), esp. pp. 256–257 (1971) and any 1933 notes quotations; Farmelo, The Strangest Man (2009). Keep Heisenberg Solvay reconstruction labeled P49."
    - "If 1933 notes or FSU texts firmly deny or place God in own words, re-score A and reconsider primary (ATHE vs AGNOS)."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Alexei Kojevnikov"
    citation: "Kojevnikov, Alexei. \"P.A.M. Dirac.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Paul-Dirac."
    url: "https://www.britannica.com/biography/Paul-Dirac"
    accessed: 2026-10-02
    reliability_note: "Signed article; first page only. Cited by paragraph description."
    source_quality: "reference entry"
    used_for: [basics, contribution, childhood, worldview, timing, lane_b, institutions, collaborators]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "J J O'Connor and E F Robertson"
    citation: "O'Connor, J. J., and E. F. Robertson. \"Paul Adrien Maurice Dirac.\" MacTutor History of Mathematics, University of St Andrews. https://mathshistory.st-andrews.ac.uk/Biographies/Dirac/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Dirac/"
    accessed: 2026-10-02
    reliability_note: "Biography; paragraphs counted from 'Paul Dirac's father'."
    source_quality: "reference entry"
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
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, heritage, timing, institutions]
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
    type: primary
    kind: "journal article"
    author: "P. A. M. Dirac"
    year: 1963
    citation: "Dirac, P. A. M. \"The Evolution of the Physicist's Picture of Nature.\" Scientific American 208, no. 5 (May 1963). Full text read via Scientific American guest-blog republish: https://www.scientificamerican.com/blog/guest-blog/the-evolution-of-the-physicists-picture-of-nature/ (also https://www.scientificamerican.com/article/the-evolution-of-the-physicists-pic/)."
    url: "https://www.scientificamerican.com/blog/guest-blog/the-evolution-of-the-physicists-picture-of-nature/"
    accessed: 2026-10-24
    reliability_note: "Publisher republish of Dirac's own May 1963 essay. IA lending-only scan of the print issue not needed once the republish was opened. Key B sentence: fundamental physical laws / nature is so constructed; God-as-mathematician is hedged metaphor."
    source_quality: "primary / own words"
    used_for: [worldview, timing, lane_b]
  - id: S6
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "\"Paul Dirac.\" Wikipedia. https://en.wikipedia.org/wiki/Paul_Dirac."
    url: "https://en.wikipedia.org/wiki/Paul_Dirac"
    accessed: 2026-10-24
    reliability_note: "P50 dual bio: birth 1902-08-08 Bristol and death 1984-10-20 Tallahassee agree with Britannica/MacTutor/Nobel. Used for maternal Methodist heritage; Views on religion section quotes SciAm and cites Kragh 1990 for 1971 conditional (secondary path to that quote)."
    source_quality: "reference entry"
    used_for: [basics, childhood, heritage, worldview, review]
  - id: S7
    type: primary
    kind: other
    author: "P. A. M. Dirac"
    year: 1976
    citation: "Dirac, P. A. M. \"Basic Beliefs and Prejudices in Physics.\" Lindau Nobel Laureate Meeting, 29 June 1976. English transcript/subtitles: https://mediatheque.lindau-nobel.org/recordings/31421/basic-beliefs-and-prejudices-in-physics-1976."
    url: "https://mediatheque.lindau-nobel.org/recordings/31421/basic-beliefs-and-prejudices-in-physics-1976"
    accessed: 2026-10-24
    reliability_note: "Mediatheque English transcript of the delivered lecture. Own voice on mathematical beauty as the basic idea for physical laws. No God/theology in the spoken lecture; FSU handwritten notes (fsu:200) remain unopened."
    source_quality: "primary / own words"
    used_for: [worldview]
---

# Paul Dirac

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Paul Adrien Maurice Dirac (1902–1984), English theoretical physicist, gave quantum mechanics its general mathematical form, wrote the relativistic equation of the electron and predicted antimatter; he shared the 1933 Nobel Prize with Schrödinger [S1; S3]. Deepen D1 opened his May 1963 Scientific American essay [S5] and the 1976 Lindau lecture transcript [S7]. primary_system stays BELOW_THRESHOLD (ATHE and AGNOS leads, both stubs). B 3 at 0.5 written_profession (alternative 4, P16 Hilbert / P35); A and E below threshold, C and D UNKNOWN; mid_basin below threshold. Not plotted.

## Life and work

Born in Bristol to a Swiss father and an English mother from a Cornish Methodist family [S2; S6], he studied engineering and mathematics at Bristol and research at Cambridge under Fowler, held the Lucasian chair from 1932 to 1969, and ended his career at Florida State University [S1; S2].

## Contribution and impact

Quantum mechanics (1925–26), quantum theory of radiation (1927), the Dirac equation (1928) and the positron (1930–31) [S1; S2; S3].

## Childhood and education

A strict, unhappy home in which only French was spoken at his father's table [S2, Biography, paragraph 2]. Maternal Methodist heritage [S6].

## Adult working worldview

Own words on nature's lawfulness: SciAm 1963 states that fundamental physical laws are mathematical and that "nature is so constructed," with a hedged "God is a mathematician" metaphor [S5]; Lindau 1976 states that physical laws must rest on beautiful equations [S7]. That lifts B's basis to written_profession but, under P16 Hilbert / P35, keeps B at 0.5 (no exception / no-exception claim). A stays BELOW_THRESHOLD: the SciAm God sentence is metaphor; Solvay 1927 is Heisenberg's reconstruction, not own voice [S6]; a 1971 conditional on God/life is only secondary via Wikipedia citing Kragh [S6].

## Heritage (context only)

English (maternal Cornish Methodist) and Swiss parentage [S2; S6]. Context only — never a worldview code.

## Timing

First lasting contribution 1925, at 23 [S3]. First checkable LIO-type own voice 1963 (SciAm), after the major-work span [S5].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form partly present (mathematical beauty as guide); circle unclear (SciAm God metaphor is not Deus sive Natura).

## Open questions

- FSU DigiNole fsu:198 / fsu:200 (bot wall).
- Kragh 1990 (1971; 1933 notes); Farmelo 2009. Keep Solvay as P49.

## Research log

- 2026-10-02: Read Britannica (Kojevnikov, first page), MacTutor and the Nobel biography. The Scientific American scan is lending-only; the FSU repository returned a bot challenge to curl and WebFetch; the Lindau Mediatheque holds audio only.
- 2026-10-24: Deepen D1. SciAm 1963 full text via SciAm guest-blog republish [S5]; Lindau 1976 English transcript [S7] (no God in delivered lecture); Wikipedia EN dual bio [S6, P50]. FSU DigiNole still bot-walled. Farm Hall not a Dirac source. Honest BELOW on A/primary; B → written_profession @0.5.
