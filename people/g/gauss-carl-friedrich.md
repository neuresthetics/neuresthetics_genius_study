---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch B)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (stage 3 batch B). Basics from MacTutor and Britannica (Gray, first page). Worldview from Sartorius von Waltershausen, Gauss zum Gedächtniss (1856), a friend's memoir with reported sayings, read on the Internet Archive scan (pp. 16, 97, 98, 101, 102, 103 checked on the page images; pp. 99–100 in the OCR text only). No writing by Gauss on religion was read. primary_system BELOW_THRESHOLD. A 1 (0.5), B 4 (0.5); C, D, E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. All scores are drafts for v8's review. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit fixes, stage 3 batch B (two blind runs at 3db6511). #156: full_name now cites MacTutor's heading for the order used, with Britannica's 'Johann Friedrich Carl Gauss' as a cited alternative (both reopened); certainty unchanged pending v8's ruling on name-order disputes. #205: the 1795 age note corrected (Sartorius p. 16 puts the least-squares discovery at Göttingen, reached 11 October 1795, so 18). #216: 'Fragen.«' copied as printed (page image). Left for v8 as a method question: #162 (first lasting year 1796 vs the listed least-squares item 1795–1801). Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Stage 3 rulings P14–P28 (v8, main 6aeba87), schema 1.3. first_lasting_contribution_year 1796 → 1795 (P12 start of the 1795–1801 least-squares item) (P17, P23), the 1796 alternative dropped since it needs the item re-dated or split (P23), 1792 kept (P25), era and age unchanged; 17-gon item 1.0 → 0.5 with Britannica's 1792 named (P25); major_work_period how_known cites the sources' dates (P23); A_locus 1 (0.5) → BELOW_THRESHOLD and B_cause 4 (0.5) → BELOW_THRESHOLD (reported speech alone (P18); B needs a statement about nature (P16)); E_scope stays BELOW_THRESHOLD (reported 'Logik' through the universe and working science, P19; the draft's UNKNOWN reverted); mid_basin note rewritten; lio_views_relative_to_major_work unclear → no LIO-type views found (P27); schooling/0 stage dame or charity school → elementary school (P21); single-source 1.0 fields → 0.7 (P15) (definition_fit, working_years, Göttingen observatory, Weber, Riemann); region_of_birth, region_of_work, sex keep 1.0 with a Britannica cite. Not reviewed."}

identity:
  id: gauss-carl-friedrich
  display_name: "Carl Friedrich Gauss"
  roster:
    canonical_name: "Carl Friedrich Gauss"
    rank: 15
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: mathematics
    field_bucket: mathematics
  full_name: {value: "Johann Carl Friedrich Gauss", certainty: 0.7, cites: [{source: S2, locator: "heading ('Johann Carl Friedrich Gauss')"}], alternatives: [{value: "Johann Friedrich Carl Gauss", cites: [{source: S3, locator: "Quick Facts ('Original name: Johann Friedrich Carl Gauss'); 'Also known as' line"}], note: "Britannica's order of the given names."}], how_known: "MacTutor's heading gives this order; Britannica gives Johann Friedrich Carl Gauss (alternative). Both reopened 2026-10-02. The usual form is Carl Friedrich Gauss. Certainty left at 0.7 pending v8's ruling on name-order disagreements."}
  native_name: {value: "Carl Friedrich Gauß (German)", certainty: 0.7, cites: [{source: S2, locator: "heading"}], how_known: "German name; the ß spelling is the usual German form (coder's note)."}
  aliases:
    - {name: "Carl-Friedrich-Gauss", kind: "roster alias"}
    - {name: "Gauss-Carl Friedrich", kind: "roster alias"}
    - {name: "Johann Friedrich Carl Gauss", kind: "birth name"}

basics:
  birth:
    date: {value: "1777-04-30", calendar: gregorian, certainty: 1.0, cites: [{source: S2, locator: "Quick Info"}, {source: S3, locator: "Born line"}], how_known: "Two sources agree."}
    place: {value: "Brunswick", modern_name: "Braunschweig, Lower Saxony, Germany", polity_then: "Duchy of Brunswick", certainty: 1.0, cites: [{source: S2, locator: "Quick Info"}, {source: S3, locator: "Born line"}], how_known: "Two sources agree."}
  death:
    date: {value: "1855-02-23", calendar: gregorian, certainty: 1.0, cites: [{source: S2, locator: "Quick Info"}, {source: S3, locator: "Died line"}], how_known: "Two sources agree."}
    place: {value: "Göttingen", modern_name: "Göttingen, Lower Saxony, Germany", polity_then: "Kingdom of Hanover", certainty: 1.0, cites: [{source: S2, locator: "Quick Info"}, {source: S3, locator: "Died line"}], how_known: "Two sources agree."}
  first_lasting_contribution_year:
    value: 1795
    certainty: 0.5
    cites: [{source: S1, locator: "p. 16 ('Schon 1795 entdeckte er hier die Methode der kleinsten Quadrate')"}, {source: S2, locator: "Biography (Ceres)"}]
    how_known: "Under P12 and P13 read literally, with P17 and P23: the earliest listed lasting contribution is 'Method of least squares; orbit of Ceres', dated as the range 1795–1801, and a range counts from its start year, so 1795 (Sartorius dates the discovery of least squares to 1795, at Göttingen; S1, p. 16, checked on the page image). Was 1796 (the 17-gon). Reliable sources disagree: Britannica dates the 17-gon to 1792, which would make it the earliest listed item, so 0.5 with that alternative named (P25). The 1796 alternative is dropped: it was reachable only by re-dating or splitting the least-squares item, and P23 does not allow choosing the year that way."
    alternatives:
      - {value: 1792, cites: [{source: S3, locator: "'Gauss's first significant discovery, in 1792'"}], note: "Britannica dates the 17-gon discovery to 1792; the listed 17-gon item follows Sartorius's 1796."}
  era_bucket: {value: "1750 to 1849", certainty: 1.0, cites: [{source: S1, locator: "p. 16"}, {source: S3, locator: "17-gon paragraph"}], how_known: "Every candidate year (1795, 1792) falls in 1750–1849 (P2); two independent sources, so 1.0 stands under P15."}
  region_of_birth: {value: "Western Europe", certainty: 1.0, cites: [{source: S2, locator: "Quick Info"}, {source: S3, locator: "Born line"}], how_known: "Germany is Western Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Western Europe", certainty: 1.0, cites: [{source: S2, locator: "Biography"}, {source: S3, locator: "'Göttingen from 1795 to 1798'; Hanover survey paragraph"}], how_known: "Brunswick and Göttingen."}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S2, locator: "Biography"}, {source: S3, locator: "opening"}], how_known: "As the sources record it."}
  languages_of_work: {value: [Latin, German], certainty: 0.7, cites: [{source: S2, locator: "Biography (Disquisitiones Arithmeticae; Über ein neues allgemeines Grundgesetz der Mechanik)"}], how_known: "Titles of his works in MacTutor."}
  occupations: {value: ["mathematician", "astronomer", "physicist", "geodesist", "observatory director"], certainty: 1.0, cites: [{source: S2, locator: "Biography"}, {source: S3, locator: "opening"}], how_known: "Two sources."}

contribution:
  fields: {value: ["number theory", "geometry", "probability theory", "geodesy", "astronomy", "potential theory", "magnetism"], certainty: 1.0, cites: [{source: S3, locator: "opening"}, {source: S2, locator: "Biography"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Constructibility of the regular 17-gon (theory of cyclotomy)", year: "1796", kind: discovery, lasting: "opened the way to later Galois theory (Britannica)", certainty: 0.5, cites: [{source: S1, locator: "p. 16"}, {source: S2, locator: "Biography"}, {source: S3, locator: "17-gon paragraph"}], how_known: "Three sources agree on the discovery; they disagree on the year: 30 March 1796 (Sartorius, from Gauss's own note, S1, p. 16) vs 1792 (Britannica), so 0.5 with the alternative named (P25). Was 1.0.", alternatives: [{value: "1792", cites: [{source: S3, locator: "'Gauss's first significant discovery, in 1792'"}], note: "Britannica's year for the 17-gon discovery."}]}
    - {value: "Disquisitiones Arithmeticae", year: "1801", kind: work, lasting: "foundation of modern number theory", certainty: 1.0, cites: [{source: S2, locator: "Biography (1801)"}, {source: S3, locator: "Quick Facts, Notable Works"}], how_known: "Two sources."}
    - {value: "Method of least squares; orbit of Ceres", year: "1795–1801", kind: method, lasting: "standard statistics and astronomy", certainty: 1.0, cites: [{source: S1, locator: "p. 16"}, {source: S2, locator: "Biography (Ceres)"}], how_known: "Two sources."}
    - {value: "Intrinsic curvature of surfaces (theorema egregium)", year: "1828", kind: theory, lasting: "differential geometry", certainty: 1.0, cites: [{source: S2, locator: "Biography (1828)"}, {source: S3, locator: "Hanover survey paragraph"}], how_known: "Two sources."}
    - {value: "Principle of least constraint", year: "before 1831", kind: "law or principle", lasting: "analytical mechanics", certainty: 0.7, cites: [{source: S2, locator: "Biography (Weber paragraph)"}], how_known: "MacTutor."}
  evidence_of_impact:
    - {value: "Copley Medal 1838", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S3, locator: "Quick Facts; awards answer"}], how_known: "Britannica."}
  major_works:
    - {value: "Disquisitiones Arithmeticae", year: 1801, kind: book, certainty: 1.0, cites: [{source: S2, locator: "Biography (1801)"}, {source: S3, locator: "Quick Facts"}], how_known: "Two sources."}
  honours:
    - {value: "Copley Medal", year: 1838, certainty: 0.7, cites: [{source: S3, locator: "awards answer"}], how_known: "Britannica."}
  definition_fit: {value: "clearly meets", rationale: "Founder of modern number theory and of differential geometry of surfaces.", certainty: 0.7, cites: [{source: S3, locator: "opening"}], how_known: "One source cited, so 0.7 under the single-source rule (P15)."}

childhood:
  family_religion: {value: TODO, note: "Not stated in the sources read."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Only child of poor parents; a 'devoted mother' who with his teachers recommended him to the duke", role: "parents", certainty: 0.7, cites: [{source: S3, locator: "childhood paragraph"}], how_known: "Britannica."}
  household_circumstances: {value: "Poor family; ducal stipend from 1791", certainty: 0.7, cites: [{source: S3, locator: "childhood paragraph"}], how_known: "Britannica (MacTutor mentions the stipend before 1792)."}
  schooling:
    - {value: "Elementary school in Brunswick (teacher Büttner, assistant Martin Bartels)", stage: "elementary school", years: "from age 7", certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraph 1"}], how_known: "MacTutor. Stage is the level (P21), so elementary school (was dame or charity school as the nearest stage); MacTutor does not say who ran it, so no run_by."}
    - {value: "Gymnasium, Brunswick (High German and Latin)", stage: "grammar or secondary school", years: "1788–1792", certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraph 1"}], how_known: "MacTutor."}
    - {value: "Collegium Carolinum, Brunswick", stage: university, years: "1792–1795", certainty: 1.0, cites: [{source: S2, locator: "Biography, paragraph 1"}, {source: S1, locator: "p. 16"}], how_known: "Two sources."}
    - {value: "University of Göttingen", stage: university, years: "1795–1798", certainty: 1.0, cites: [{source: S2, locator: "Biography"}, {source: S3, locator: "'Göttingen from 1795 to 1798'"}], how_known: "Two sources."}
  early_mathematics: {value: "advanced mathematics", note: "At the Collegium Carolinum he independently found the binomial theorem, the arithmetic-geometric mean and quadratic reciprocity (MacTutor).", certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraph 1"}], how_known: "MacTutor."}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "Martin Bartels, assistant teacher", name: "Martin Bartels", certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraph 1"}], how_known: "MacTutor."}
  languages_in_childhood: {value: [German, Latin], certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraph 1"}], how_known: "Learned High German and Latin at the Gymnasium."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1795–1855", certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "From Göttingen to his death. MacTutor alone, so 0.7 under the single-source rule (P15)."}
  nominal_affiliations: []
  self_described_science_religion_relation:
    value: "Reported by a friend: questions of ethics, of 'unser Verhältniss zu Gott', of our destiny and future mattered to him more than mathematics, but 'ihre Lösung liegt ganz unerreichbar über uns und ganz ausserhalb des Gebietes der Wissenschaft'; he held philosophical ideas to be subjective and kept them strictly apart from science."
    certainty: 0.5
    cites: [{source: S1, locator: "pp. 97–98"}]
    how_known: "Reported speech in a friend's memoir (Sartorius knew him for many years); not Gauss's own writing, so 0.5."
  primary_system:
    value: BELOW_THRESHOLD
    cites: [{source: S1, locator: "pp. 99–103"}]
    how_known: "Only a friend's report was read. Sartorius affirms a personal, eternal, just, all-wise, almighty God and personal survival (p. 103), but says he will not give a full picture of Gauss's religious views and will touch only sides 'unabhängig von allen confessionellen Fragen' (pp. 99–100, OCR text only). Without his confession or his own notes (which Sartorius says survive, p. 100) no system file fits at 0.5."
    note: "Draft judgment (one line): BELOW_THRESHOLD because the only source deliberately leaves out confession. Candidates: CLASS_THEISM, DEISM, CHRIST (all drafts). Would need his letters or his religious notes."
  secondary_system: {value: UNKNOWN, how_known: "No system evidence beyond the memoir."}
  candidate_codes_considered:
    - {code: CLASS_THEISM, reason: "Considered: 'ewigen, gerechten, allweisen, allmächtigen Gott' (S1, p. 103) fits perfect-being theism, but nothing on divine simplicity or the classical school.", cites: [{source: S1, locator: "p. 103"}]}
    - {code: DEISM, reason: "Considered: a 'letzten Ordner der Dinge' and logic running through the whole universe (S1, pp. 97–98, 103), with God outside science; but survival and a personal God are affirmed and revelation is not discussed.", cites: [{source: S1, locator: "pp. 97–98, 103"}]}
    - {code: CHRIST, reason: "Considered: nothing read on Christ, church or scripture; Sartorius leaves confession aside (pp. 99–100).", cites: [{source: S1, locator: "pp. 99–100"}]}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, note: "Evidence exists only as reported speech: Sartorius reports 'der feste Glaube an einen letzten Ordner der Dinge, an einen ewigen, gerechten, allweisen, allmächtigen Gott' (S1, p. 103) and an 'alles durchdringenden Intelligenz, die von einem Sonnensystem zum andern im Weltall wiederklingt' (p. 102). Read alone, that leaned to 1 (named alternative 2).", how_known: "Was 1 at 0.5. Reported speech cannot score an axis on its own (P18), and nothing else read bears on A, so BELOW_THRESHOLD (P19)."}
    B_cause: {value: BELOW_THRESHOLD, note: "Scored on his account of nature (P6). The only remarks about nature are reported: for Sartorius the principle of least constraint was 'die mathematische Verkörperung jenes ethischen Grundgedankens, den er für das Universum als bindend erkannte' (S1, p. 97), and Gauss recognised 'die durchs ganze Weltall gehende Logik' (pp. 97–98). MacTutor paraphrases: 'He later came to believe his potential theory and his method of least squares provided vital links between science and nature' (S2, Biography), a paraphrase, not his words. His exact astronomy, geodesy and least squares (S2) are physics-facing work with no remark of his own on natural law, which a mathematician needs for B (P16).", how_known: "Was 4 at 0.5. B needs a statement about nature (P16); working science alone does not count, and reported speech cannot score an axis on its own (P18); some evidence exists, so BELOW_THRESHOLD (P19)."}
    C_ledger: {value: BELOW_THRESHOLD, note: "Survival after death is affirmed (S1, pp. 101, 103) and Sartorius calls the spiritual life of the universe a 'grosses von ewiger Wahrheit durchdrungenes Rechtsverhältniss' (p. 101), but nothing read speaks of reward, punishment or judgement, and the evidence is reported speech. Draft judgment (one line): not scored from the memoirist's phrase.", how_known: "Some evidence, too weak (§4) (P19)."}
    D_authority: {value: BELOW_THRESHOLD, note: "Reported: questions of God lie 'ausserhalb des Gebietes der Wissenschaft' (S1, p. 97); nothing read speaks of revelation or scripture.", how_known: "Some evidence, too indirect (§4) (P19)."}
    E_scope: {value: BELOW_THRESHOLD, note: "Scored on the world's order (P7). Only indirect evidence on the first question (the same rules everywhere): Sartorius reports that Gauss recognised 'die durchs ganze Weltall gehende Logik' (S1, pp. 97–98), and his astronomy (the orbit of Ceres, S2) is working science. Nothing read on favour for a group in events.", how_known: "Reported speech cannot score an axis on its own (P18), and working science without a statement keeps E at BELOW_THRESHOLD (P19). The draft had re-sorted it as UNKNOWN; P19's working-science clause keeps it BELOW_THRESHOLD."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus and B_cause are both BELOW_THRESHOLD (reported speech only, P18; B needs a statement about nature, P16), so the P4 test cannot be applied (§6)."}
  statements:
    - text: "»Es gibt Fragen.« sagte er ein Mal, »auf deren Beantwortung ich einen unendlich viel höhern Werth legen würde als auf die mathematischen z. B. über Ethik, über unser Verhältniss zu Gott, über unsere Bestimmung und über unsere Zukunft; allein ihre Lösung liegt ganz unerreichbar über uns und ganz ausserhalb des Gebietes der Wissenschaft.«"
      cites: [{source: S1, locator: "p. 97"}]
      date: "1856"
      context: "Sartorius reporting a remark of Gauss; date is the memoir's publication, the remark is undated. The print has a full stop after 'Fragen' (checked on the page image; possibly a damaged comma), copied as printed."
      axes: [D_authority]
      kind: "reported speech"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
    - text: "Das Princip des kleinsten Zwanges war gleichsam die mathematische Verkörperung jenes ethischen Grundgedankens, den er für das Universum als bindend erkannte."
      cites: [{source: S1, locator: "p. 97"}]
      date: "1856"
      context: "Sartorius's own summary, not a quotation of Gauss."
      axes: [B_cause]
      kind: "reported speech"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
    - text: "So erfasste er das geistige Leben im ganzen Weltall als ein grosses von ewiger Wahrheit durchdrungenes Rechtsverhältniss und aus dieser Quelle schöpfte er vornehmlich die Zuversicht, das unerschütterliche Vertrauen, dass mit dem Tode unsere Laufbahn nicht geschlossen sei."
      cites: [{source: S1, locator: "p. 101"}]
      date: "1856"
      context: "Sartorius's summary of Gauss's religious outlook."
      axes: [C_ledger]
      kind: "reported speech"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
    - text: "Die unerschütterliche Idee von einer persönlichen Fortdauer nach dem Tode, der feste Glaube an einen letzten Ordner der Dinge, an einen ewigen, gerechten, allweisen, allmächtigen Gott, bildete das Fundament seines religiösen Lebens"
      cites: [{source: S1, locator: "p. 103"}]
      date: "1856"
      context: "Sartorius's summary."
      axes: [A_locus]
      kind: "reported speech"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
    - text: "Man wird daher zu der Ansicht gedrängt, für die ohne eine streng wissenschaftliche Begründung so Vieles andere spricht, dass neben dieser materiellen Welt noch eine andere zweite, rein geistige Weltordnung existirt, mit ebenso viel Mannigfaltigkeiten als die, in der wir leben — ihr sollen wir theilhaftig werden."
      cites: [{source: S1, locator: "p. 103"}]
      date: "1856"
      context: "End of a saying Sartorius reports in Gauss's words ('Er selbst sprach sich so eines Tages aus')."
      axes: [A_locus]
      kind: "reported speech"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
  changes_over_life: []
  coder_notes: "CLASS_THEISM, DEISM and CHRIST are drafts. Everything on worldview rests on one friend's memoir (Sartorius von Waltershausen 1856), read on a Google library scan at the Internet Archive; quoted passages were checked on the page images (leaf = page + 2). Sartorius says Gauss left religious notes in his own hand (p. 100, OCR text) and that a paper on the metaphysics of mathematics had not been found (p. 98 footnote); neither was read. The Greek motto he used, Ὁ Θεὸς ἀριθμητίζει (p. 97), is about questions science cannot settle and is not scored. changes_over_life is empty: no dated change in what was read."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "German (Brunswick)", certainty: 1.0, cites: [{source: S2, locator: "Quick Info"}, {source: S3, locator: "Born line"}], how_known: "Two sources."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1795–1840", certainty: 0.7, cites: [{source: S1, locator: "p. 16"}, {source: S2, locator: "Biography ('by 1840 he had written three important papers on the subject')"}], how_known: "From least squares (1795; S1, p. 16) to the magnetism papers with Weber, which MacTutor dates up to 1840 (S2). Both ends are the sources' dates, not a chosen span (P23); 0.7, as the end rests on MacTutor alone (P15)."}
  age_at_first_lasting_contribution: {value: 18, certainty: 0.5, cites: [{source: S1, locator: "p. 16"}], how_known: "Born 30 April 1777. Least squares 1795: Sartorius places the discovery 'hier', at Göttingen, which Gauss reached on 11 October 1795, after his 18th birthday (S1, p. 16, checked on the page image), so 18; recomputed for the new year (P17, P23), value unchanged. The 1792 alternative gives 15, so 0.5, the certainty of the year (P15)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No statement of his own is scored at 3 or 4, so there is no LIO-type view under the anchor (P27); the memoir's reports are reported speech and give no dates."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", rationale: "No statement of his own scored at 3 or 4 (P27 anchor); Sartorius's reports are reported speech and cannot score an axis (P18).", certainty: 0.5, cites: [{source: S1, locator: "pp. 97–103"}], how_known: "Was unclear. Absence in what was read; not evidence of absence."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "Sartorius: by science he understood only the 'streng in sich abgeschlossene logische Gebäude' built on generally recognised truths by 'eine eiserne Gedankenkette' (p. 97).", certainty: 0.5, cites: [{source: S1, locator: "p. 97"}], how_known: "Memoir plus coder's reading."}
  form_acquired: {value: "childhood or adolescence", certainty: 0.5, cites: [{source: S2, locator: "Biography, paragraph 1"}], how_known: "Advanced mathematics before 18."}
  circle_present: {value: "partly", rationale: "Least constraint as the mathematical embodiment of an ethical idea binding on the universe (p. 97), and logic through the whole universe (pp. 97–98), but a second, purely spiritual world order beside the material (p. 103).", certainty: 0.5, cites: [{source: S1, locator: "pp. 97–98, 103"}], how_known: "Memoir plus coder's reading."}
  reading: "As belief, not finding: form present, circle partly present on a friend's report. The record does not test H1."
  notes: ""

institutions:
  - {value: "Göttingen Observatory and University of Göttingen", role: "director of the observatory", years: "1807–1855", kind: university, certainty: 0.7, cites: [{source: S2, locator: "Biography (1807)"}], how_known: "MacTutor alone, so 0.7 under the single-source rule (P15)."}
  - {value: "Survey of the Kingdom of Hanover", role: "in charge of observations", years: "1818–1832", kind: "government or state body", certainty: 0.7, cites: [{source: S3, locator: "Hanover survey paragraph"}], how_known: "Britannica."}
collaborators:
  - {value: "Wilhelm Weber", relation: collaborator, note: "physics professor at Göttingen from 1831", certainty: 0.7, cites: [{source: S2, locator: "Biography (1831)"}], how_known: "MacTutor alone, so 0.7 under the single-source rule (P15)."}
  - {value: "Bernhard Riemann", roster_id: riemann-bernhard, relation: "influenced", note: "approved his doctoral thesis and heard his probationary lecture", certainty: 0.7, cites: [{source: S2, locator: "Biography (1850 onward)"}], how_known: "MacTutor alone, so 0.7 under the single-source rule (P15)."}
  - {value: "Wolfgang Sartorius von Waltershausen", relation: other, note: "friend and memoirist", certainty: 0.7, cites: [{source: S1, locator: "pp. 99–100"}], how_known: "His own account of many years' friendship."}

review:
  roster_status_reason: {value: "Core in v8 (F 5: Claude, DeepSeek, Gemini, GPT, Grok).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 15"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "First lasting year now 1795 (least squares, start of the 1795–1801 item, P12) (P17, P23); 17-gon date: 30 March 1796 (Sartorius, from Gauss's own note) vs 1792 (Britannica)."
    - "All A and B evidence is reported speech, which cannot score an axis on its own (P18); A and B moved to BELOW_THRESHOLD."
    - "All worldview evidence is one friend's memoir; Sartorius warns he may be suspected of mixing in his own views (pp. 99–100, OCR text)."
    - "Britannica read as its first page only."
  open_questions:
    - "Find Gauss's own religious notes, which Sartorius says survive (p. 100), and his letters (e.g. to Bolyai or Olbers) for direct statements."

sources:
  - id: S1
    type: primary
    kind: "scholarly book"
    author: "Wolfgang Sartorius von Waltershausen"
    year: 1856
    citation: "Sartorius von Waltershausen, Wolfgang. Gauss zum Gedächtniss. Leipzig: S. Hirzel, 1856. Internet Archive, bub_gb_h_Q5AAAAcAAJ (Google library scan). https://archive.org/details/bub_gb_h_Q5AAAAcAAJ."
    url: "https://archive.org/details/bub_gb_h_Q5AAAAcAAJ"
    accessed: 2026-10-02
    reliability_note: "Contemporary memoir by a friend; reported speech, not Gauss's own writing. Quoted pages checked on the page images (leaf = page + 2); pp. 99–100 read in the OCR text only. Author, publisher and date as in the Internet Archive record."
    used_for: [basics, contribution, worldview, timing, lane_b, collaborators]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "J J O'Connor and E F Robertson"
    citation: "O'Connor, J. J., and E. F. Robertson. \"Johann Carl Friedrich Gauss.\" MacTutor History of Mathematics, University of St Andrews. https://mathshistory.st-andrews.ac.uk/Biographies/Gauss/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Gauss/"
    accessed: 2026-10-02
    reliability_note: "Biography; cited by paragraph description."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S3
    type: tertiary
    kind: encyclopedia
    author: "Jeremy John Gray"
    citation: "Gray, Jeremy John. \"Carl Friedrich Gauss.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Carl-Friedrich-Gauss."
    url: "https://www.britannica.com/biography/Carl-Friedrich-Gauss"
    accessed: 2026-10-02
    reliability_note: "Signed article; first page only."
    used_for: [identity, basics, contribution, childhood, heritage, institutions]
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

# Carl Friedrich Gauss

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Carl Friedrich Gauss (1777–1855), German mathematician and astronomer, proved the 17-gon constructible, wrote the Disquisitiones Arithmeticae (1801), developed least squares and the intrinsic geometry of surfaces [S1, p. 16; S2; S3]. His friend Sartorius reports a firm belief in a personal, just, almighty God and in survival after death, and his view that questions about God lie "ganz ausserhalb des Gebietes der Wissenschaft" [S1, pp. 97, 103]. No writing of his own on religion was read. Draft under v8's stage 3 rulings (P14–P28): primary_system BELOW_THRESHOLD. A, B, C, D and E below threshold (reported speech only, P18; B needs a statement about nature, P16; E from reported speech and working science, P19); mid_basin below threshold.

## Life and work

Born poor in Brunswick and supported by the duke, he studied at the Collegium Carolinum and Göttingen, took his degree at Helmstedt (1799), directed the Göttingen observatory from 1807, led the Hanover survey (1818–32) and worked on magnetism with Weber [S2; S3].

## Contribution and impact

Number theory, least squares and the orbit of Ceres, differential geometry (theorema egregium), potential theory and magnetism [S2; S3].

## Childhood and education

Only child of poor parents; a calculating prodigy noticed at elementary school by Büttner and Bartels [S2; S3].

## Adult working worldview

Known only through Sartorius's memoir: science and religion kept apart [S1, pp. 97–98], a personal God and a second spiritual world order [S1, p. 103]. Sartorius left out confessional questions on purpose [S1, pp. 99–100].

## Heritage (context only)

German, from Brunswick [S2]. Context only.

## Timing

First lasting contribution 1795, least squares, the start of the listed 1795–1801 item [S1, p. 16] (P12, P13, P17, P23), at 18. The 17-gon is dated 1796 by his own note [S1, p. 16]; Britannica says 1792 [S3], which would make it the earliest item, so the year is held at 0.5 (P25).

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form present (science as a closed logical building [S1, p. 97]); circle partly present.

## Open questions

- Gauss's own religious notes and letters.

## Research log

- 2026-10-02: Read MacTutor, Britannica (Gray, first page) and Sartorius (1856) on the Internet Archive scan; checked pp. 16, 97, 98, 101, 102 and 103 on the page images.
- 2026-10-02 (v8 method rulings): Reopened Sartorius p. 16 on the page image (1795, least squares, 'hier' = Göttingen) and pp. 97–103 for the axes.
- 2026-10-02 (stage 3 rulings P14–P28): Reopened MacTutor's biography for the magnetism papers ('by 1840') and the potential-theory remark.
