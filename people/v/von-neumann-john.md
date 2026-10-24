---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 5
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch B)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (stage 3 batch B). Basics from MacTutor. Religion from a colleague's recollection, Seeger, 'Von Neumann, Jewish Catholic' (PSCF 40, 1988): nominal Catholic after his first marriage and Catholic instruction in his last illness. No statement of his own on religion was read, and no recorded interview of him on religion was found (the P8 interview route is unavailable). primary_system BELOW_THRESHOLD. B 4 (0.5) from working science; A, C, D, E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. All scores are drafts for v8's review. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit fix, stage 3 batch B (two blind runs at 3db6511). #352: full_name now follows MacTutor ('born János von Neumann'); the earlier 'born János Neumann' is kept only as a marked inference from the 1913 title. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Stage 3 rulings P14–P28 (v8, main 6aeba87), schema 1.3. B_cause 4 (0.5) → BELOW_THRESHOLD (no remark of his own on natural law) (P16); D_authority BELOW_THRESHOLD → UNKNOWN (the Psalms recitation is practice, off-point) and E_scope stays BELOW_THRESHOLD (working science; the draft's UNKNOWN reverted), A, C notes rewritten (P19); first_lasting_contribution_year how_known and the ordinals item year rewritten without a chosen year, alternative 1924 named (P12, P23, P25); tutor Fekete 0.7 → 0.5 with Fejér named, marriage date alternatives named (P25); Lutheran Gymnasium stage religious school → grammar or secondary school, run_by religious body (P21); major_work_period how_known cites the sources' dates (P23); Seeger's 1947 quotation marked primary check pending (P26); mid_basin note rewritten; IAS kind university → research institute (P21); single-source 1.0 fields → 0.7 (P15) (era_bucket, definition_fit, working_years); region_of_birth, region_of_work, sex keep 1.0 with a Seeger cite. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens run 1 on rulings packet 6155174, sources reopened. Tutor note reworded: MacTutor (Fekete) and Seeger (Fejér) name different tutors but do not exclude each other; certainty left at 0.5 and the P25 question flagged for v8. Not reviewed."}
    - {date: 2026-10-08, by: "Grok Bot", summary: "P30 rule 5 age sweep: ages recomputed as event year − birth year, with no month adjustment (scripts/recompute_ages.py; every change is in reports/p30_age_changes.csv). No other value changed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #47, F5 rank 47). Needs: A BELOW_THRESHOLD; B BELOW_THRESHOLD. P47 source_quality on every source. New: S4 Britannica (Poundstone; dual-source birth/death/basics); S5 Nicholas A. Vonneuman, John von Neumann as Seen by His Brother (OCR §6.3: family converted to Catholicism 1929 'for sake of convenience, not conviction'; deathbed legends 'not quite as simple'); S6 von Neumann, The Mathematician (1947; MacTutor Extras + Works of the Mind; primary / own words on math–natural-science link); S7 Bochner NAS Biographical Memoir 1958 (baptized Roman Catholic 1930; 'died in the faith'). B_cause BELOW_THRESHOLD → 3 @ 0.5 inference_from_work, alt 4 named (P30 scientist + P35; working QM/hydrodynamics); support corroborated (S1+S2+S4; P48). A_locus stays BELOW_THRESHOLD (no adult-working locus of his own; P19; Macrae God/Pascal lines remain secondary/deathbed-adjacent, unread in Macrae). primary_system stays BELOW_THRESHOLD (Nicholas not-conviction + Seeger 'some claim agnostic' + Bochner membership still leave no adult-working code at ≥0.5; AGNOS/CHRIST remain candidates; AGNOS stub flagged). Baptism filled (Bochner 1930; Nicholas 1929 conversion — year alt named P25). working_years synced to major_work_period 1923–1955 (P30 addendum). Chart-moving NO (A BELOW; B faded @0.5). No fallacy_catalog (Jason). Draft, not reviewed."}

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
    date: {value: "1903-12-28", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Quick Info"}, {source: S4, locator: "opening ('born December 28, 1903, Budapest, Hungary')"}], how_known: "MacTutor and Britannica agree. Was 0.7 (MacTutor alone)."}
    place: {value: "Budapest", modern_name: "Budapest, Hungary", polity_then: "Austria-Hungary (Kingdom of Hungary)", certainty: 1.0, cites: [{source: S1, locator: "Quick Info"}, {source: S2, locator: "paragraph 2"}, {source: S4, locator: "opening"}], how_known: "Three sources agree."}
  death:
    date: {value: "1957-02-08", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Quick Info"}, {source: S4, locator: "opening ('died February 8, 1957, Washington, D.C.')"}], how_known: "MacTutor and Britannica agree. Was 0.7 (MacTutor alone)."}
    place: {value: "Washington, D.C. (Walter Reed Army Hospital)", modern_name: "Washington, D.C., USA", polity_then: "United States", certainty: 1.0, cites: [{source: S1, locator: "Quick Info"}, {source: S2, locator: "last paragraph"}, {source: S4, locator: "opening"}], how_known: "MacTutor, Seeger (names the hospital), Britannica."}
  first_lasting_contribution_year: {value: 1923, certainty: 0.5, cites: [{source: S1, locator: "Biography ('He published a definition of ordinal numbers when he was 20')"}], how_known: "Definition of the ordinal numbers, 'the one used today', the earliest listed lasting contribution (P17, P23). MacTutor gives his age (20), not the year; born 28 December 1903 (S1, Quick Info), he was 20 from 28 December 1923 to 27 December 1924, and a range counts from its start year (P12), so 1923, at 0.5 with 1924 named. The 1922 paper with Fekete, his first, is not listed: MacTutor does not call it lasting.", alternatives: [{value: 1924, cites: [{source: S1, locator: "Biography ('when he was 20'); Quick Info (born 28 December 1903)"}], note: "Age 20 covers all of 1924 but only the last four days of 1923."}]}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "Biography"}, {source: S4, locator: "opening / Early life"}], how_known: "Both candidate years (1923, 1924) fall in 1850–1949 (P2). Dual-sourced via MacTutor + Britannica; was 0.7 under P15."}
  region_of_birth: {value: "Eastern Europe", certainty: 1.0, cites: [{source: S1, locator: "Quick Info"}, {source: S2, locator: "paragraph 2 ('He was born in Budapest in 1903')"}], how_known: "Hungary is Eastern Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "North America", certainty: 1.0, cites: [{source: S1, locator: "Biography (1930–1957)"}, {source: S2, locator: "paragraphs 3–5 (Princeton, Los Alamos, the AEC)"}, {source: S4, locator: "Princeton, 1930–42; Later years"}], how_known: "Princeton and Washington from 1930; Berlin, Hamburg and Göttingen (Western Europe) 1926–1930."}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S1, locator: "Biography"}, {source: S2, locator: "paragraph 2"}], how_known: "As the sources record it."}
  languages_of_work: {value: [German, English], certainty: 1.0, cites: [{source: S1, locator: "Biography (Mathematische Grundlagen der Quantenmechanik, 1932; Theory of Games, 1944)"}, {source: S4, locator: "European career / Princeton"}], how_known: "Titles of his works in MacTutor; Britannica concurs on German-to-English shift."}
  occupations: {value: ["mathematician", "physicist", "computer pioneer", "government scientific adviser"], certainty: 1.0, cites: [{source: S1, locator: "Summary; Biography"}, {source: S2, locator: "paragraphs 4–5"}, {source: S4, locator: "opening summary"}], how_known: "Three sources."}

contribution:
  fields: {value: ["set theory", "operator theory", "quantum mechanics", "game theory", "hydrodynamics", "computer science"], certainty: 1.0, cites: [{source: S1, locator: "Summary; Biography"}, {source: S2, locator: "paragraphs 7–8"}, {source: S4, locator: "opening / European career"}], how_known: "Three sources."}
  lasting_original_contributions:
    - {value: "Definition of the ordinal numbers", year: "1923–1924", kind: "concept or term", lasting: "the definition used today", certainty: 0.7, cites: [{source: S1, locator: "Biography (doctorate paragraph)"}], how_known: "MacTutor gives his age (20), not the year, so the item is dated by the age window (P12, P23). Was '1923'."}
    - {value: "Rigorous Hilbert-space framework for quantum mechanics (Mathematische Grundlagen der Quantenmechanik)", year: "1932", kind: theory, lasting: "standard framework", certainty: 1.0, cites: [{source: S1, locator: "Biography (1932)"}, {source: S2, locator: "paragraph 7"}, {source: S4, locator: "European career, 1921–30"}], how_known: "Three sources. Counts as a theory about physical systems under P30 (scientist for B)."}
    - {value: "Rings of operators (von Neumann algebras)", year: "1930s–1940s", kind: theory, lasting: "named after him", certainty: 0.7, cites: [{source: S1, locator: "Biography (operator algebras)"}], how_known: "MacTutor."}
    - {value: "Minimax theorem and the theory of games (with Morgenstern, 1944)", year: "1928", kind: theory, lasting: "foundation of game theory", certainty: 1.0, cites: [{source: S1, locator: "Biography (game theory)"}, {source: S2, locator: "paragraph 8"}, {source: S4, locator: "European career ('Theory of Parlor Games', 1928)"}], how_known: "Three sources."}
    - {value: "Implosion method for the atomic bomb", year: "1943–1945", kind: method, lasting: "nuclear weapons design", certainty: 1.0, cites: [{source: S1, locator: "Biography (war work)"}, {source: S2, locator: "paragraph 10"}, {source: S4, locator: "World War II / hydrodynamics and shock waves"}], how_known: "Three sources. Applied physical science under P30."}
  evidence_of_impact:
    - {value: "Enrico Fermi Award, 1956", kind: "honours in lifetime", certainty: 1.0, cites: [{source: S1, locator: "Biography (1956)"}, {source: S2, locator: "paragraph 12"}], how_known: "Two sources."}
  major_works:
    - {value: "Mathematische Grundlagen der Quantenmechanik", year: 1932, kind: book, certainty: 1.0, cites: [{source: S1, locator: "Biography (1932)"}, {source: S2, locator: "paragraph 3"}, {source: S4, locator: "European career"}], how_known: "Three sources."}
    - {value: "Theory of Games and Economic Behavior (with Oskar Morgenstern)", year: 1944, kind: book, certainty: 1.0, cites: [{source: S1, locator: "Biography (game theory)"}, {source: S2, locator: "paragraph 4"}, {source: S4, locator: "opening"}], how_known: "Three sources."}
    - {value: "The Mathematician (essay)", year: 1947, kind: other, certainty: 1.0, cites: [{source: S6, locator: "title page / Works of the Mind citation"}, {source: S2, locator: "paragraph 9"}], how_known: "Primary essay read (S6); Seeger quotes it."}
  honours:
    - {value: "Enrico Fermi Award", year: 1956, certainty: 1.0, cites: [{source: S1, locator: "Biography (1956)"}, {source: S2, locator: "paragraph 12"}], how_known: "Two sources."}
    - {value: "Medal for Merit", year: 1947, certainty: 0.7, cites: [{source: S1, locator: "honours paragraph"}], how_known: "MacTutor."}
  definition_fit: {value: "clearly meets", rationale: "Founder of the mathematical framework of quantum mechanics and of game theory; computer architecture pioneer.", certainty: 1.0, cites: [{source: S1, locator: "Summary"}, {source: S4, locator: "opening summary"}], how_known: "MacTutor and Britannica; was 0.7 under P15."}

childhood:
  family_religion: {value: "Jewish, non-observant; the household 'seemed to mix Jewish and Christian traditions'", certainty: 0.7, cites: [{source: S1, locator: "Biography, paragraph 1"}, {source: S5, locator: "§6.3 (father not observing Jewish religion strictly)"}], how_known: "MacTutor; Nicholas's brother memoir concurs on non-observant Jewish household."}
  family_religious_practice: {value: "Non-observant", certainty: 0.7, cites: [{source: S1, locator: "Biography, paragraph 1"}, {source: S5, locator: "§6.3"}], how_known: "MacTutor and Nicholas."}
  parents_and_household:
    - {value: "Father, Max Neumann, banker, ennobled in 1913", name: "Max Neumann", role: father, certainty: 1.0, cites: [{source: S1, locator: "Biography, paragraphs 1–2"}, {source: S2, locator: "paragraph 2"}, {source: S4, locator: "Early life and education"}], how_known: "Three sources."}
    - {value: "Mother, Margaret Kann", name: "Margaret Neumann (née Kann)", role: mother, certainty: 1.0, cites: [{source: S2, locator: "paragraph 2"}, {source: S4, locator: "Early life and education"}], how_known: "Seeger and Britannica."}
  household_circumstances: {value: "Wealthy Budapest family; governesses; two younger brothers", certainty: 1.0, cites: [{source: S1, locator: "Biography, paragraph 1"}, {source: S2, locator: "paragraph 2"}], how_known: "Two sources."}
  schooling:
    - {value: "Lutheran Gymnasium, Budapest", stage: "grammar or secondary school", run_by: "religious body", years: "1911–1921", certainty: 1.0, cites: [{source: S1, locator: "Biography (1911, 1921)"}, {source: S2, locator: "paragraph 2"}, {source: S5, locator: "§6.4"}], how_known: "Three sources. Stage is the level and run_by who ran it (P21; was religious school). MacTutor speaks of 'the religious affiliation' of the school, which counted for less than its academic tradition."}
    - {value: "University of Budapest (mathematics, examinations only), Berlin (chemistry) and ETH Zürich (chemical engineering diploma 1926); Budapest doctorate in set theory 1926", stage: university, years: "1921–1926", certainty: 1.0, cites: [{source: S1, locator: "Biography (1921–1926)"}, {source: S2, locator: "paragraph 2"}, {source: S4, locator: "Early life and education"}], how_known: "Three sources."}
  early_mathematics: {value: "advanced mathematics", note: "Special tuition at the Gymnasium; first paper with Fekete in 1922 (MacTutor).", certainty: 1.0, cites: [{source: S1, locator: "Biography (1911, 1921–22)"}, {source: S2, locator: "paragraph 2"}], how_known: "Two sources."}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "Michael Fekete, tutor and co-author of his first paper", name: "Michael Fekete", certainty: 0.5, cites: [{source: S1, locator: "Biography (1921–22)"}], how_known: "MacTutor: 'Fekete the assistant at the University of Budapest who had been tutoring him' (S1). Seeger: 'he was tutored by Leopold Fejer of the University of Budapest' (S2). The two name different tutors but do not strictly exclude each other: both could have tutored him. Left at 0.5 with Fejér named under P25 pending v8; if v8 reads the sources as compatible, P25 does not apply, Fekete returns to 0.7 (MacTutor alone, P15) and Fejér becomes a separate mentor at 0.7 (Seeger alone). Was 0.7.", alternatives: [{value: "Leopold Fejér, tutor", cites: [{source: S2, locator: "paragraph 2 ('he was tutored by Leopold Fejer of the University of Budapest')"}], note: "Seeger's tutor; Seeger spells it Fejer. Possibly a second tutor rather than a rival value (flagged for v8)."}]}
  languages_in_childhood: {value: [Hungarian, German, French], certainty: 0.7, cites: [{source: S1, locator: "Biography, paragraph 1"}], how_known: "MacTutor: languages from German and French governesses; Hungarian assumed from Budapest (coder)."}
  notable_events:
    - {value: "Family fled briefly to Austria during Béla Kun's Communist government", year: "1919", age: 16, certainty: 1.0, cites: [{source: S1, locator: "Biography (1919)"}, {source: S4, locator: "Early life and education"}], how_known: "MacTutor and Britannica."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1923–1955", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "Equal to timing.major_work_period (P30 addendum). Was 1926–1957 (doctorate to death)."}
  nominal_affiliations:
    - {value: "Roman Catholic (family conversion after father's death; convenience not conviction per brother)", years: "c. 1929–", certainty: 0.7, cites: [{source: S5, locator: "§6.3 ('After father's death in 1929 we all converted to Catholicism for sake of convenience, not conviction')"}, {source: S7, locator: "p. baptism paragraph ('baptized a Roman Catholic in 1930')"}, {source: S2, locator: "last paragraph"}], how_known: "Nicholas (brother memoir) for the 1929 family conversion and 'not conviction'; Bochner for baptism 1930; Seeger for nominal-Catholic presumption around first marriage. Year of baptism/conversion: 1929 (Nicholas) vs 1930 (Bochner) — named under P25.", alternatives: [{value: "c. 1930–", cites: [{source: S7, locator: "baptism paragraph"}], note: "Bochner's baptism year 1930; MacTutor/Seeger date the first marriage around the 1930 Princeton move / IAS year."}]}
    - {value: "Catholic burial service at Walter Reed Army Hospital; buried in Princeton", year: 1957, certainty: 0.7, cites: [{source: S2, locator: "last paragraph"}, {source: S7, locator: "baptism paragraph ('died in the faith… buried in Princeton')"}], how_known: "Seeger attended the service; Bochner concurs on burial."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No statement of his on science and religion was read. Seeger: 'we never discussed religion' and 'he showed little interest in the philosophical aspects of quantum mechanics' (S2). The Mathematician (S6) addresses mathematics and the natural/empirical sciences, not religion."}
  primary_system:
    value: BELOW_THRESHOLD
    cites: [{source: S5, locator: "§6.3"}, {source: S2, locator: "last paragraph"}, {source: S7, locator: "baptism paragraph"}]
    how_known: "Adult-working system still not established at ≥0.5. Nicholas (S5): family converted to Catholicism in 1929 'for sake of convenience, not conviction' — affiliation without conviction, not an AGNOS label. Seeger (S2): 'Some people claim that von Neumann was an agnostic' (unattributed) and reports Catholic deathbed instruction. Bochner (S7): baptized 1930 and 'died in the faith' (membership). Nothing in his own words on God. The often-quoted 'There probably has to be a God' and Pascal's-wager remarks reach us only through later secondary reports (Wikipedia citing Macrae); Macrae itself was not read this pass (lending/403). Named alternative: AGNOS @ 0.5 scholarly_reconstruction if v8 treats Nicholas not-conviction + Seeger claim as enough; CHRIST if deathbed/membership is taken as adult-working (against Nicholas and against P20 adult-working unit)."
    note: "Draft judgment (one line): BELOW_THRESHOLD — opposite-direction candidates, no first-hand locus, no scholarly AGNOS label as strong as Segrè-on-Fermi. AGNOS is a stub system file (flag). No recorded interview of von Neumann on religion (P8 unavailable)."
  secondary_system: {value: UNKNOWN, how_known: "No second-system evidence beyond the Catholic membership / AGNOS claim split."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Considered: baptism 1930 (S7), family conversion 1929 (S5), Catholic burial (S2, S7), deathbed priest (S2). Rejected as adult-working code: Nicholas says 'convenience, not conviction' and deathbed legends 'not quite as simple' (S5); deathbed turn is not the adult working worldview. CHRIST remains a candidate, not the code.", cites: [{source: S5, locator: "§6.3"}, {source: S2, locator: "last paragraph"}, {source: S7, locator: "baptism paragraph"}]}
    - {code: AGNOS, reason: "Considered: Seeger's unattributed 'Some people claim…agnostic' (S2) plus Nicholas 'not conviction' (S5). Not coded: no collaborator/scholar label as strong as Segrè-on-Fermi; 'not conviction' ≠ explicit suspension of judgement about God. AGNOS stub flagged. Named alternative if v8 codes it at 0.5.", cites: [{source: S2, locator: "last paragraph"}, {source: S5, locator: "§6.3"}]}
    - {code: JUDA, reason: "Rejected: Jewish family heritage, non-observant (S1, S5). Heritage is never a code.", cites: [{source: S1, locator: "Biography, paragraph 1"}, {source: S5, locator: "§6.3"}]}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, note: "No statement of his own placing or denying God in the adult working years. Seeger's agnostic claim and Catholic death (S2), Nicholas not-conviction (S5), and Bochner 'died in the faith' (S7) are other people's reports and pull opposite ways. Macrae 'There probably has to be a God' / Pascal-wager lines (via Wikipedia) are secondary and deathbed-adjacent; Macrae unread. If AGNOS were coded, P20 would also keep A at BELOW_THRESHOLD.", how_known: "Some evidence, too indirect (§4) (P19). Named alternative: UNKNOWN if v8 reads the reports as saying nothing on locus."}
    B_cause:
      value: 3
      basis: inference_from_work
      certainty: 0.5
      support: corroborated
      cites: [{source: S1, locator: "Biography (Mathematische Grundlagen 1932; war-work hydrodynamics)"}, {source: S2, locator: "paragraphs 7–10"}, {source: S4, locator: "European career / World War II (Hilbert-space QM; hydrodynamics and shock waves)"}, {source: S6, locator: "opening: 'peculiar relationship to the natural sciences' / empirics"}]
      how_known: "Coder's reading of his working science, as P6/P24/P30 direct for a scientist (lasting contributions include the Hilbert-space framework for quantum mechanics and implosion/hydrodynamics — theories/results about physical systems). No statement of his own about miracles or exceptions, so 0.5. Three independent biographical source ids describing the same physical program (MacTutor + Seeger + Britannica) → corroborated (P48); The Mathematician (S6) is his own essay on mathematics' link to empirical natural science, not a no-exception claim. Named alternative 4 (P35). Was BELOW_THRESHOLD under a pre-P30/P35 reading of P16 (pure-mathematics / no remark); restored under P30+P35."
      rationale: "Scored on his account of nature (P6), which for a scientist is the working science. Mathematische Grundlagen der Quantenmechanik (1932) and his hydrodynamics/shock work treat physical systems as mathematically lawful. The Mathematician (1947) stresses mathematics' 'quite peculiar relationship to the natural sciences' and empirical origins (S6) but does not claim nature is exceptionless, so it does not lift the basis to written_profession. P35: B from working science alone is 3 at 0.5 with 4 as the named alternative, never 4. Named alternative: 4, if a statement of his own shows no exception."
    C_ledger: {value: BELOW_THRESHOLD, note: "Nothing in his own words on judgement or afterlife. Wigner's recollection, quoted by MacTutor, that his logic 'forced him to realise that he would cease to exist' (S1) and the deathbed Catholic instruction (S2) are other people's reports and point different ways.", how_known: "Some evidence, too indirect (§4) (P19)."}
    D_authority: {value: UNKNOWN, how_known: "Searched MacTutor, Seeger, Britannica, Nicholas, Bochner, The Mathematician: nothing on revelation, scripture or their authority against observation. Reciting the Penitential Psalms in Latin (reported by an Air Force chaplain to Seeger, S2) is practice, not a view of authority, so it is off-point and counts as nothing; working science does not bear on D (P19)."}
    E_scope: {value: BELOW_THRESHOLD, note: "Scored on the world's order (P7). No statement of his own on favour for a group in events or on the same rules for every kind of being; his working science (quantum mechanics, hydrodynamics and shocks; S1, S2, S4) bears on the first question only.", how_known: "A scientist's working science keeps E at BELOW_THRESHOLD without a statement (P19)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD and B_cause is only 0.5, under the P4 test's 0.7 bar (§6)."}
  statements: []
  changes_over_life:
    - {value: "From non-observant Jewish upbringing to family Catholic conversion after father's death (convenience, not conviction)", year: "1929", certainty: 0.7, cites: [{source: S5, locator: "§6.3"}, {source: S7, locator: "baptism paragraph (1930)"}, {source: S1, locator: "Biography, paragraph 1"}], how_known: "Nicholas for 1929 conversion and motive; Bochner for baptism 1930; MacTutor for Jewish family. Year alt 1930 named (P25).", alternatives: [{value: "1930", cites: [{source: S7, locator: "baptism paragraph"}], note: "Bochner's baptism year."}]}
    - {value: "In his last illness he asked for a Roman Catholic priest and received instruction from a Benedictine (Father Anselm), then a Jesuit (per Seeger)", year: "1956–1957", certainty: 0.5, cites: [{source: S2, locator: "last paragraph"}, {source: S5, locator: "§6.3 (Father Anselm; legends of conversion/second baptism 'not quite as simple')"}], how_known: "Seeger (colleague; partly second-hand via chaplain); Nicholas names Father Anselm and warns against overnight-conversion legends. Not the adult working worldview."}
  coder_notes: "Deepen D1: B restored to 3 @ 0.5 inference_from_work under P30+P35 (was BELOW under early P16); support corroborated (P48). primary_system and A stay BELOW_THRESHOLD — Nicholas 'convenience, not conviction' blocks CHRIST-as-conviction but does not by itself establish AGNOS; Seeger's unattributed agnostic claim is weaker than Segrè-on-Fermi. Macrae (God/Pascal quotes) and Heims (Morgenstern agnostic recollection often cited online) unread this pass (lending/403). The Mathematician read in full (S6); no religion language; empirics remarks support working-science context for B only. statements empty (nothing of his on religion). AGNOS stub flagged. No fallacy_catalog (Jason 2026-10-23)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Hungarian Jewish", certainty: 1.0, cites: [{source: S1, locator: "Biography, paragraph 1; Budapest quota paragraph"}, {source: S2, locator: "paragraphs 1, 6"}, {source: S4, locator: "Early life ('affluent, highly assimilated Jewish family')"}], how_known: "Three sources."}
  religious_heritage_by_birth: {value: "Jewish", certainty: 1.0, cites: [{source: S1, locator: "Biography, paragraph 1"}, {source: S5, locator: "§6.3"}], how_known: "MacTutor and Nicholas."}
  baptism_or_initiation: {value: "Baptized Roman Catholic (1930 per Bochner; family conversion 1929 per Nicholas)", certainty: 0.7, cites: [{source: S7, locator: "baptism paragraph ('baptized a Roman Catholic in 1930')"}, {source: S5, locator: "§6.3 ('converted to Catholicism' 1929)"}], how_known: "Bochner NAS memoir and Nicholas brother memoir. Year 1929 vs 1930 named under P25. Heritage/initiation only — never a worldview code.", note: "Heritage/initiation only — never a worldview code.", alternatives: [{value: "1929 family conversion (baptism date not separately stated by Nicholas)", cites: [{source: S5, locator: "§6.3"}], note: "Nicholas dates the family's conversion to 1929 after the father's death."}]}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1923–1955", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "From the ordinals (age 20, so 1923–24) to the 1955 AEC appointment, both as MacTutor dates them; the ends are the sources' dates, not a chosen span (P23). MacTutor alone, so 0.7 (P15)."}
  age_at_first_lasting_contribution: {value: 20, certainty: 0.7, cites: [{source: S1, locator: "Biography (ordinals 'when he was 20')"}], how_known: "MacTutor gives the age, so it does not depend on the 1923 or 1924 reading."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No LIO-type view (P27) of his own was read; B is inference_from_work only (not an LIO-type view under P27)."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", rationale: "Nothing of his on God or nature at the P27 bar; B is inference_from_work only.", certainty: 0.5, cites: [{source: S6, locator: "whole"}, {source: S2, locator: "last paragraph"}], how_known: "Absence at the P27 bar in sources read."}
  worldview_during_major_work: {value: "primary_system BELOW_THRESHOLD; A BELOW_THRESHOLD; B 3 @ 0.5 from working science; nominal Catholic affiliation without conviction (Nicholas)", certainty: 0.5, cites: [{source: S5, locator: "§6.3"}, {source: S1, locator: "Biography"}, {source: S6, locator: "whole"}], how_known: "Synthesis of D1 sources; not a stronger code."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "'His general approach was from the standpoint of axiomatization' (Seeger, S2); Hilbert-program / set-theory / operator-algebra work (S1, S4).", certainty: 0.5, cites: [{source: S2, locator: "paragraph 7"}, {source: S1, locator: "Biography"}], how_known: "Colleague characterisation plus the listed work."}
  form_acquired: {value: "childhood or adolescence", certainty: 0.5, cites: [{source: S1, locator: "Biography (Gymnasium; 1922 paper)"}], how_known: "Advanced mathematics before 18."}
  circle_present: {value: "unclear", rationale: "No God–Nature identity statement read; The Mathematician links math to natural science without identifying God and Nature.", certainty: 0.5, cites: [{source: S6, locator: "opening"}, {source: S2, locator: "last paragraph"}], how_known: "No evidence either way at the circle bar."}
  reading: "As belief, not finding: form present, circle unclear. The record does not test H1."
  notes: ""

institutions:
  - {value: "Institute for Advanced Study, Princeton", role: "one of the original six mathematics professors", years: "1933–1957", kind: "research institute", certainty: 1.0, cites: [{source: S1, locator: "Biography (1933)"}, {source: S2, locator: "paragraph 3"}, {source: S4, locator: "Princeton, 1930–42"}], how_known: "Three sources. Kind 'research institute' (P21)."}
  - {value: "Los Alamos Scientific Laboratory", role: consultant, years: "1943–1955", kind: "government or state body", certainty: 1.0, cites: [{source: S1, locator: "Biography (war work)"}, {source: S4, locator: "World War II"}], how_known: "MacTutor and Britannica."}
  - {value: "U.S. Atomic Energy Commission", role: commissioner, years: "1955–1957", kind: "government or state body", certainty: 1.0, cites: [{source: S1, locator: "Biography (1955)"}, {source: S2, locator: "paragraph 5"}, {source: S4, locator: "Later years"}], how_known: "Three sources."}
collaborators:
  - {value: "Oskar Morgenstern", relation: collaborator, note: "Theory of Games (1944)", certainty: 1.0, cites: [{source: S1, locator: "Biography (game theory)"}, {source: S2, locator: "paragraph 4"}, {source: S4, locator: "opening"}], how_known: "Three sources."}
  - {value: "David Hilbert", relation: "influenced by", note: "studied under him at Göttingen 1926–27", certainty: 1.0, cites: [{source: S1, locator: "Biography (1926–27)"}, {source: S2, locator: "paragraph 2"}, {source: S4, locator: "European career"}], how_known: "Three sources."}
  - {value: "Raymond J. Seeger", relation: collaborator, note: "shock-wave work; author of S2", certainty: 0.7, cites: [{source: S2, locator: "paragraph 9"}], how_known: "Seeger's own statement."}

review:
  roster_status_reason: {value: "Core in v8 (F 5: Claude, DeepSeek, Gemini, GPT, Grok).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 47"}], how_known: "Study roster."}
  controversies:
    - {value: "Whether he was agnostic or Catholic: Seeger reports both the claim of agnosticism and his Catholic death; Nicholas denies overnight devout conversion", certainty: 0.5, cites: [{source: S2, locator: "last paragraph"}, {source: S5, locator: "§6.3"}], how_known: "Colleague recollection vs brother memoir."}
  data_quality_flags:
    - "First marriage: before the 1930 move to Princeton (MacTutor) vs the year of the IAS appointment (Seeger)."
    - "Tutor: MacTutor names Fekete, Seeger names Fejér. Not strictly a conflict (both may have tutored him); coded 0.5 under P25 pending v8."
    - "Catholic conversion/baptism year: Nicholas 1929 vs Bochner 1930 (P25)."
    - "No primary statement on religion; Macrae God/Pascal quotes and Heims Morgenstern agnostic recollection unread (lending/403)."
    - "AGNOS is a stub system file (flag)."
    - "B restored under P30+P35 from the 2026-10-02 P16 BELOW coding; still faded @0.5."
  open_questions:
    - "Read Norman Macrae, John von Neumann (1992), esp. p. 379 area for the 'There probably has to be a God' / Pascal lines in context (deathbed vs adult-working)."
    - "Read Steve J. Heims, John von Neumann and Norbert Wiener (1980) for the Morgenstern recollection often cited as 'completely agnostic'."
    - "Own-words locus or no-exception claim (Selected Letters, Rédei ed.; Collected Works commentary) to lift A or B above 0.5 / BELOW."

sources:
  - id: S1
    type: secondary
    kind: "institutional page"
    author: "J J O'Connor and E F Robertson"
    citation: "O'Connor, J. J., and E. F. Robertson. \"John von Neumann.\" MacTutor History of Mathematics, University of St Andrews. https://mathshistory.st-andrews.ac.uk/Biographies/Von_Neumann/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Von_Neumann/"
    accessed: 2026-10-24
    reliability_note: "Biography; cited by paragraph description."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: secondary
    kind: "journal article"
    author: "Raymond J. Seeger"
    year: 1988
    citation: "Seeger, Raymond J. \"Von Neumann, Jewish Catholic.\" Perspectives on Science and Christian Faith 40 (December 1988): 234–236. https://www.asa3.org/ASA/PSCF/1988/PSCF12-88Seeger.html."
    url: "https://www.asa3.org/ASA/PSCF/1988/PSCF12-88Seeger.html"
    accessed: 2026-10-24
    reliability_note: "Short memoir by a colleague (shock-wave collaborator), on the journal's own site; paragraphs counted from 'John von Neumann's life was a paradox'. His religious information is partly second-hand (the chaplain)."
    source_quality: "scholarly edition or monograph"
    used_for: [basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators, review]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    reliability_note: "Study's own roster; used only for rank, F and status."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S4
    type: tertiary
    kind: encyclopedia
    author: "William Poundstone"
    citation: "Poundstone, William. \"John von Neumann.\" Encyclopaedia Britannica. https://www.britannica.com/biography/John-von-Neumann."
    url: "https://www.britannica.com/biography/John-von-Neumann"
    accessed: 2026-10-24
    reliability_note: "Signed Britannica article by the author of Prisoner's Dilemma; used for dual-source basics and working-science corroboration. Religion not treated in the pages read."
    source_quality: "reference entry"
    used_for: [basics, contribution, childhood, worldview, heritage, institutions, collaborators]
  - id: S5
    type: secondary
    kind: "scholarly book"
    author: "Nicholas A. Vonneuman"
    year: 1987
    citation: "Vonneuman, Nicholas A. John von Neumann as Seen by His Brother. Privately circulated memoir (Meadowbrook, PA). §6.3 'The religious milieu' (OCR from scanned pages)."
    accessed: 2026-10-24
    reliability_note: "Brother's privately circulated memoir; primary family testimony on household religion and the 1929 conversion. Image-only PDF; text via tesseract OCR of §6.3–§6.4. Not a critical edition."
    source_quality: "other"
    used_for: [childhood, worldview, heritage, review]
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "John von Neumann"
    year: 1947
    citation: "von Neumann, John. \"The Mathematician.\" In The Works of the Mind, ed. Robert B. Heywood, vol. 1, no. 1, 180–196. Chicago: University of Chicago Press, 1947. Read via MacTutor Extras transcription (Parts 1–2) and a matching PDF of the essay text."
    url: "https://mathshistory.st-andrews.ac.uk/Extras/Von_Neumann_Part_1/"
    accessed: 2026-10-24
    reliability_note: "Own words on mathematics and the natural/empirical sciences; no religion language. Also at Extras/Von_Neumann_Part_2/."
    source_quality: "primary / own words"
    used_for: [contribution, worldview, timing, lane_b]
  - id: S7
    type: secondary
    kind: "scholarly book"
    author: "S. Bochner"
    year: 1958
    citation: "Bochner, S. \"John von Neumann, 1903–1957.\" Biographical Memoirs of the National Academy of Sciences. Washington, D.C.: National Academy of Sciences, 1958. https://www.nasonline.org/wp-content/uploads/2024/06/von-neumann-john.pdf (also Wayback)."
    url: "https://www.nasonline.org/wp-content/uploads/2024/06/von-neumann-john.pdf"
    accessed: 2026-10-24
    reliability_note: "NAS biographical memoir by a mathematical colleague; used for baptism 1930 and 'died in the faith'. Membership, not adult-working belief."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview, heritage]
---

# John von Neumann

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

John von Neumann (1903–1957), Hungarian-American mathematician, gave quantum mechanics its Hilbert-space form, founded game theory and helped design the implosion bomb and early computers [S1; S2; S4]. Born into a non-observant Jewish family [S1; S5], the family converted to Catholicism in 1929 "for sake of convenience, not conviction" [S5]; Bochner records baptism in 1930 and that he "died in the faith" [S7]. No statement of his own on religion was read. Draft deepen D1: primary_system BELOW_THRESHOLD; A BELOW_THRESHOLD; B 3 @ 0.5 inference_from_work (P30 scientist + P35; support corroborated); C and E BELOW_THRESHOLD; D UNKNOWN; mid_basin BELOW_THRESHOLD. Still unplotted (A BELOW; B faded).

## Life and work

Lutheran Gymnasium in Budapest, chemistry in Berlin and Zürich, a Budapest doctorate in set theory (1926), Göttingen, Berlin and Hamburg, then Princeton from 1930 and the IAS from 1933; Los Alamos consultant and AEC commissioner [S1; S2; S4].

## Contribution and impact

Ordinals, the mathematical foundations of quantum mechanics (1932), operator algebras, the minimax theorem (1928) and game theory (1944), hydrodynamics and computing [S1; S2; S4]. Essay *The Mathematician* (1947) on mathematics and the natural sciences [S6].

## Childhood and education

Wealthy Budapest banking family; the household "seemed to mix Jewish and Christian traditions" [S1, Biography, paragraph 1]. Brother Nicholas: after the father's death in 1929 "we all converted to Catholicism for sake of convenience, not conviction" [S5, §6.3].

## Adult working worldview

Not established from his own words as a coded system. Seeger: "Some people claim that von Neumann was an agnostic. I must confess that we never discussed religion" [S2]. Nicholas warns that deathbed "conversion and second baptism" legends are "not quite as simple" [S5]. B scored from working science (QM, hydrodynamics) at 3 @ 0.5 under P35 [S1; S2; S4], with *The Mathematician* as own-words empirics context [S6].

## Heritage (context only)

Hungarian Jewish, non-observant; baptized Roman Catholic 1930 [S1; S5; S7]. Context only — never a worldview code.

## Timing

First lasting contribution 1923 or 1924 (ordinals, at 20) [S1]; major work period 1923–1955 [S1]. No LIO-type view (P27) of his own found.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form present (axiomatization [S2; S1]); circle unclear. H1 not tested.

## Open questions

- Macrae (1992) for the God / Pascal lines in context; Heims (1980) for Morgenstern's agnostic recollection.
- Own-words locus or no-exception claim to lift A or B.

## Research log

- 2026-10-02: Read MacTutor and Seeger (1988, via the fetch tool; direct download blocked). Searched for recorded interviews of von Neumann on religion: none found. The 'probably has to be a God' and wager quotes were seen only in secondary pages and not used.
- 2026-10-02 (v8 method rulings): Reopened Seeger (fetch tool) for the 1947 quotation and the nature remark; MacTutor rechecked for any remark on natural law (none).
- 2026-10-02 (stage 3 rulings P14–P28): Reopened MacTutor (Lutheran Gymnasium, Fekete, marriage, ordinals) and Seeger (paragraphs 2–3: Fejér, marriage) for the P21 and P25 checks.
- 2026-10-02 (lens run 1): Reopened MacTutor (Fekete, 1921–22) and Seeger (paragraph 2, Fejér) for the tutor note.
- 2026-10-24 (deepen D1, queue #47): Read Britannica Poundstone (S4); Nicholas brother memoir §6.3–§6.4 via OCR (S5); *The Mathematician* 1947 full essay (S6; MacTutor Extras Parts 1–2 + PDF); Bochner NAS memoir 1958 (S7; Wayback/NAS PDF). Macrae and Heims remain lending/403 blockers. No fallacy audit.
