---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 6
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch B)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to mathematics. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-25, by: "Grok Bot", summary: "Perpetual deepen: religious_heritage_by_birth / family_religion TODO→Lutheran (Brunswick) @0.7 from new Wikipedia S8 + Britannica birthplace. Baptism/catechism UNKNOWN. Chart-moving NO. No figures/; no fallacy_catalog."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (stage 3 batch B). Basics from MacTutor and Britannica (Gray, first page). Worldview from Sartorius von Waltershausen, Gauss zum Gedächtniss (1856), a friend's memoir with reported sayings, read on the Internet Archive scan (pp. 16, 97, 98, 101, 102, 103 checked on the page images; pp. 99–100 in the OCR text only). No writing by Gauss on religion was read. primary_system BELOW_THRESHOLD. A 1 (0.5), B 4 (0.5); C, D, E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. All scores are drafts for v8's review. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit fixes, stage 3 batch B (two blind runs at 3db6511). #156: full_name now cites MacTutor's heading for the order used, with Britannica's 'Johann Friedrich Carl Gauss' as a cited alternative (both reopened); certainty unchanged pending v8's ruling on name-order disputes. #205: the 1795 age note corrected (Sartorius p. 16 puts the least-squares discovery at Göttingen, reached 11 October 1795, so 18). #216: 'Fragen.«' copied as printed (page image). Left for v8 as a method question: #162 (first lasting year 1796 vs the listed least-squares item 1795–1801). Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Stage 3 rulings P14–P28 (v8, main 6aeba87), schema 1.3. first_lasting_contribution_year 1796 → 1795 (P12 start of the 1795–1801 least-squares item) (P17, P23), the 1796 alternative dropped since it needs the item re-dated or split (P23), 1792 kept (P25), era and age unchanged; 17-gon item 1.0 → 0.5 with Britannica's 1792 named (P25); major_work_period how_known cites the sources' dates (P23); A_locus 1 (0.5) → BELOW_THRESHOLD and B_cause 4 (0.5) → BELOW_THRESHOLD (reported speech alone (P18); B needs a statement about nature (P16)); E_scope stays BELOW_THRESHOLD (reported 'Logik' through the universe and working science, P19; the draft's UNKNOWN reverted); mid_basin note rewritten; lio_views_relative_to_major_work unclear → no LIO-type views found (P27); schooling/0 stage dame or charity school → elementary school (P21); single-source 1.0 fields → 0.7 (P15) (definition_fit, working_years, Göttingen observatory, Weber, Riemann); region_of_birth, region_of_work, sex keep 1.0 with a Britannica cite. Not reviewed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #15). P47 source_quality on every source. Own-word letters: S5 Schmidt–Stäckel Briefwechsel Gauss–Bolyai (1899; archive.org OCR) — 1799.I.9 hope of better future; 1802.XII.3 true life in eigentliche Heimat; 1848.IV.20 Schöpfer unsrer Existenz / schönere Metamorphose; S6 Schilling Wilhelm Olbers Bd. 2.1 (1900) Brief 1805.IX.3 'bloss durch die Gnade Gottes'; S7 Kneller Christianity and the leaders of modern science (1911) scholarly digest of those letters. A_locus BELOW_THRESHOLD → 1 @ 0.5 consistent_private_letters, support corroborated (S5+S6); named alt 2 (deist reading, Bühler). B_cause BELOW_THRESHOLD → 3 @ 0.5 inference_from_work, support corroborated (S2+S3; P30/P35 scientist: least squares/Ceres, least constraint, magnetism/potential theory); named alt 4. C stays BELOW_THRESHOLD (immortality without reward/punishment language). D stays BELOW_THRESHOLD (reported speech on science/religion). E stays BELOW_THRESHOLD (scientist, no statement; P19). mid_basin still BELOW_THRESHOLD (A and B only at 0.5). primary_system stays BELOW_THRESHOLD (confession still open). Chart: unplotted → faded filled. No fallacy_catalog (Jason 2026-10-23). Draft, not reviewed."}

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
  primary_domain: mathematics
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
  family_religion: {value: "Lutheran", certainty: 0.7, cites: [{source: S8, locator: "Religious views: member of the Lutheran church, like most of the population in northern Germany"}], how_known: "Wikipedia: Lutheran church membership typical of northern German / Brunswick milieu. Context only."}
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
  working_years: {value: "1795–1840", certainty: 0.7, cites: [{source: S1, locator: "p. 16"}, {source: S2, locator: "Biography ('by 1840 he had written three important papers on the subject')"}], how_known: "Equals timing.major_work_period (P30 addendum): least squares 1795 to magnetism papers with Weber through 1840 (S1, S2). Was 1795–1855 (death); tightened on deepen."}
  nominal_affiliations: []
  self_described_science_religion_relation:
    value: "Reported by a friend: questions of ethics, of 'unser Verhältniss zu Gott', of our destiny and future mattered to him more than mathematics, but 'ihre Lösung liegt ganz unerreichbar über uns und ganz ausserhalb des Gebietes der Wissenschaft'; he held philosophical ideas to be subjective and kept them strictly apart from science."
    certainty: 0.5
    cites: [{source: S1, locator: "pp. 97–98"}]
    how_known: "Reported speech in a friend's memoir (Sartorius knew him for many years); not Gauss's own writing, so 0.5."
  primary_system:
    value: BELOW_THRESHOLD
    cites: [{source: S1, locator: "pp. 99–103"}, {source: S5, locator: "pp. 40–47, 132–133"}, {source: S6, locator: "Brief 133, pp. 267–269"}]
    how_known: "Sartorius still leaves confession aside (pp. 99–100). Own letters name Gott / Schöpfer and a better life after death (S5, S6) but do not fix a confession or reject revelation, so no system file fits at 0.5 (P19; DEISM needs rejection of revelation, P27)."
    note: "Draft judgment (one line): BELOW_THRESHOLD — confession still open. Candidates: CLASS_THEISM, DEISM, CHRIST (all drafts). Letters strengthen personal-Creator language but do not settle the code."
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: CLASS_THEISM, reason: "Considered: Sartorius's 'ewigen, gerechten, allweisen, allmächtigen Gott' (S1, p. 103) and Gauss's own 'Schöpfer unsrer Existenz' (S5, 1848.IV.20) fit personal Creator theism, but nothing on divine simplicity or the classical school; confession still open.", cites: [{source: S1, locator: "p. 103"}, {source: S5, locator: "Letter XLI, Göttingen 1848.IV.20, pp. 132–133"}]}
    - {code: DEISM, reason: "Considered (and named as A alternative): a last Ordner and science kept apart from God-questions (S1); Bühler and others read Gauss as deist. Against: personal Schöpfer / Gnade Gottes language and afterlife hope in his own letters; revelation not rejected (P27).", cites: [{source: S1, locator: "pp. 97–98, 103"}, {source: S5, locator: "pp. 40–47, 132–133"}, {source: S6, locator: "Brief 133, p. 269"}]}
    - {code: CHRIST, reason: "Considered: Lutheran upbringing is often asserted in secondary literature, but nothing read here on Christ, church or scripture in his own hand; Sartorius leaves confession aside.", cites: [{source: S1, locator: "pp. 99–100"}]}
  lio_axes:
    A_locus:
      value: 1
      basis: consistent_private_letters
      certainty: 0.5
      support: corroborated
      cites: [{source: S5, locator: "Letter XXI, Braunschweig 1802.XII.3, pp. 40–47 ('wahren Lebens in unsrer eigentlichen Heymath')"}, {source: S5, locator: "Letter XLI, Göttingen 1848.IV.20, pp. 132–133 ('Schöpfer unsrer Existenz'; 'schöneren Metamorphose')"}, {source: S6, locator: "Brief 133, Braunschweig 1805.IX.3, p. 269 ('bloss durch die Gnade Gottes')"}, {source: S1, locator: "p. 103 ('letzten Ordner der Dinge'; 'ewigen, gerechten, allweisen, allmächtigen Gott')"}, {source: S7, locator: "pp. 44–46 (English digest of the Bolyai/Olbers letters)"}]
      how_known: "Was BELOW_THRESHOLD under P18 (Sartorius only). Deepen: two independent scholarly letter editions give Gauss's own words naming Gott's grace (1805, during major work) and a Schöpfer (1848, after major_work_period end 1840 — cited for consistency of Creator language, not as the sole during-span A anchor). During-span afterlife letter 1802 speaks of true life in a spiritual home. Held at 0.5: (a) contested deist reading (named alt 2); (b) during-span A language is thinner than the 1848 Schöpfer line; (c) private letters, more than one document → consistent_private_letters ceiling 0.7, capped by contest and indirectness. Support corroborated (S5+S6; S1 friend-report of personal God kept as corroborating context, also cited on the named alt)."
      rationale: "Draft judgment (one line): personal transcendent Creator — 'bloss durch die Gnade Gottes' (S6, 1805) and 'der Schöpfer unsrer Existenz' (S5, 1848), with during-span hope of a true life in our eigentliche Heimat (S5, 1802). Named alternative: 2 (impersonal Ordner / deist reading)."
      alternatives:
        - {value: 2, note: "Deist / impersonal last Ordner reading (Sartorius's 'letzten Ordner der Dinge'; Bühler and others).", cites: [{source: S1, locator: "p. 103"}]}
    B_cause:
      value: 3
      basis: inference_from_work
      certainty: 0.5
      support: corroborated
      cites: [{source: S2, locator: "Biography (Ceres orbit; least squares; principle of least constraint; magnetism / potential theory)"}, {source: S3, locator: "opening; Hanover survey / theorema egregium; astronomy paragraphs"}]
      how_known: "Was BELOW_THRESHOLD under a stricter P16 reading that demanded an explicit nature statement. Deepen under P30/P35 (scientist with lasting physical/natural contributions → B 3 @ 0.5 inference_from_work, never 4; named alt 4): least-squares orbit of Ceres, least constraint, magnetism and potential theory are lasting results on natural regularity (S2, S3). No statement of his own on law and exception, so 0.5. Sartorius's reported 'Logik' through the universe remains support-only (P18). Support corroborated (S2+S3)."
      rationale: "Draft judgment (one line): working mathematical astronomy and physics — Ceres orbit by least squares, least constraint, geomagnetism and potential theory (S2; S3) — imply a lawful natural order with no stated exception in what was read, so B 3 at 0.5. Named alternative: 4 (P35: working science cannot tell lawful-with-exceptions from exceptionless)."
      alternatives:
        - {value: 4, note: "P35 default alternative for inference_from_work.", cites: [{source: S2, locator: "Biography (Ceres; least squares; least constraint)"}, {source: S3, locator: "astronomy / magnetism paragraphs"}]}
    C_ledger: {value: BELOW_THRESHOLD, note: "Own letters affirm survival / a better life after death (S5 1799, 1802, 1848) but say nothing on reward, punishment or judgement. Sartorius's 'Rechtsverhältniss' remains reported speech. Draft judgment (one line): immortality without a moral ledger — not scored on C.", how_known: "Some evidence, too weak for C (§4) (P19). Deepen 2026-10-24."}
    D_authority: {value: BELOW_THRESHOLD, note: "Reported: questions of God lie 'ausserhalb des Gebietes der Wissenschaft' (S1, p. 97); nothing in the letters read speaks of revelation or scripture against reason.", how_known: "Some evidence, too indirect (§4) (P19)."}
    E_scope: {value: BELOW_THRESHOLD, note: "Scientist under P30; working science bears on E's first question but E is not scored from working science alone (P19). No statement of his own on one world / one order.", how_known: "BELOW_THRESHOLD under P19 (scientist, no statement; deepen 2026-10-24)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus 1 ≤ 1 and B_cause 3 ≥ 3 would pass P4's shape test, but both are only at 0.5, under the test's 0.7 bar (§6, P19)."}
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
    - text: "Was sind wir ohne die Hoffnung einer bessern Zukunft? Lass uns die Freiheit unsers Herzens behaupten, so lange es gehen will u. unser Glück vorzüglich in uns selbst suchen."
      cites: [{source: S5, locator: "Letter VII, Braunschweig 1799.I.9, pp. 29–30"}]
      date: "1799-01-09"
      context: "Private letter to Wolfgang Bolyai, mourning a friend's wife's death; during major work."
      axes: [C_ledger]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Schmidt–Stäckel 1899 OCR (archive.org); wording checked in the OCR against the page header. Used for C context; C still BELOW_THRESHOLD (no reward/punishment language)."
    - text: "Nun lebe wohl Du Guter. Möge der Traum den wir das Leben nennen dir ein süsser seyn, ein Vorschmack des wahren Lebens in unsrer eigentlichen Heymath, wo den erwachten Geist nicht mehr die Ketten des trägen Leibes, die Schranken des Raums, die Geissel der irdischen Leiden und das Necken unserer kleinlichen Bedürfnisse und Wünsche drückt. Lass uns muthig und ohne Murren die Bürde bis ans Ende tragen, aber nie jenes höhere Ziel aus den Augen verlieren."
      cites: [{source: S5, locator: "Letter XXI, Braunschweig 1802.XII.3, pp. 40–47"}]
      date: "1802-12-03"
      context: "Close of a private letter to Bolyai; during major work. Spelling Heymath as in the edition."
      axes: [A_locus, C_ledger]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Schmidt–Stäckel 1899. Spiritual-home / true-life language; does not by itself name a personal Creator (paired with 1805 Gnade Gottes and 1848 Schöpfer)."
    - text: "Endlich vor ein paar Tagen ist's gelungen — aber nicht meinem mühseligen Suchen, sondern bloss durch die Gnade Gottes möchte ich sagen. Wie der Blitz einschlägt, hat sich das Räthsel gelöst."
      cites: [{source: S6, locator: "Brief 133, Braunschweig 1805.IX.3, pp. 267–269"}]
      date: "1805-09-03"
      context: "Private letter to Wilhelm Olbers on finding the proof of the sign of the Gaussian sum (Disquisitiones Arithmeticae follow-on); during major work."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Schilling 1900 OCR (archive.org). OCR garbles Gnade; wording restored from the standard reading of this famous letter (also in Kneller S7). Conventional grace formula — scored with the Bolyai Creator/afterlife letters, not alone."
    - text: "Ich will gern zugeben, dass dieselben Schicksale, die zu tragen mir so schwer geworden ist, und noch ist, manchem andern viel leichter gewesen wären, aber die Gemüthsverfassung gehört zu unserm Ich, der Schöpfer unsrer Existenz hat sie uns mitgegeben, und wir vermögen wenig daran zu ändern. Ich finde dagegen in diesem Bewusstsein der Nichtigkeit des Lebens, was doch jedenfalls der grössere Theil der Menschheit beim Annähern des Ziels aussprechen muss, mir die stärkste Bürgschaft für das Nachfolgen einer schöneren Metamorphose darbietet."
      cites: [{source: S5, locator: "Letter XLI, Göttingen 1848.IV.20, pp. 132–133"}]
      date: "1848-04-20"
      context: "Private letter to Bolyai late in life; after major_work_period end (1840). Cited for consistency of Creator / afterlife language (P20 / changes_over_life), not as the sole during-span A anchor."
      axes: [A_locus, C_ledger]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Schmidt–Stäckel 1899. Strongest personal-Creator wording in what was read; outside the 1795–1840 major-work window."
  changes_over_life:
    - {value: "Same personal-Creator / afterlife conviction made more explicit late (1848 Schöpfer unsrer Existenz / schönere Metamorphose) than in the during-span letters (1799 hope; 1802 spiritual Heimat; 1805 Gnade Gottes); not a reversal. A uses during-span letters as the primary anchor.", year: 1848, age: 71, certainty: 0.7, cites: [{source: S5, locator: "Letters VII, XXI, XLI"}, {source: S6, locator: "Brief 133"}], how_known: "Dated Bolyai letter after major_work_period end (1840); wording checked in Schmidt–Stäckel OCR."}
  coder_notes: "Deepen 2026-10-24 (queue #15): A and B lifted on own-word letters (S5, S6) and scientist inference_from_work (P30/P35). CLASS_THEISM, DEISM and CHRIST remain draft candidates; confession still open. Sartorius (S1) kept as support/context only for axes (P18). Religious notes Sartorius says survive (p. 100) still unread. Greek motto Ὁ Θεὸς ἀριθμητίζει (S1 p. 97) not scored. Chart-moving: unplotted → faded filled (A and B both scored at 0.5, both corroborated; mid_basin still BELOW)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "German (Brunswick)", certainty: 1.0, cites: [{source: S2, locator: "Quick Info"}, {source: S3, locator: "Born line"}], how_known: "Two sources."}
  religious_heritage_by_birth: {value: "Lutheran (Brunswick / northern German)", certainty: 0.7, cites: [{source: S8, locator: "Religious views: member of the Lutheran church, like most of the population in northern Germany"}, {source: S1, locator: "opening / Early life (Brunswick)"}], how_known: "Wikipedia states Lutheran church membership as the regional default; birth in Brunswick (Protestant north Germany). Adult belief nuances (not all dogma) do not erase birth-heritage. Context only (P19)."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Lutheran infant baptism expected but no baptism record opened."}
  childhood_catechism: {value: UNKNOWN, how_known: "No childhood catechism curriculum named in sources read."}

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
    - "A and B now rest on own-word letter editions (S5, S6) and scientist inference_from_work (P30/P35); Sartorius reported speech kept as support only (P18)."
    - "A at 0.5: contested deist reading; strongest Schöpfer wording is 1848 (after major_work end 1840)."
    - "Letter editions read as archive.org OCR; Gnade Gottes line restored from the standard reading of Schilling Brief 133 (also Kneller)."
    - "Britannica read as its first page only."
  open_questions:
    - "Gauss's religious notes in his own hand, which Sartorius says survive (S1, p. 100), still unread."
    - "A full re-read of Schilling/Bolyai page images (not OCR) for the Gnade Gottes and Schöpfer lines."
    - "Whether a confession code (CLASS_THEISM vs DEISM vs CHRIST) can be fixed without those notes."

sources:
  - id: S1
    type: primary
    kind: "scholarly book"
    author: "Wolfgang Sartorius von Waltershausen"
    year: 1856
    citation: "Sartorius von Waltershausen, Wolfgang. Gauss zum Gedächtniss. Leipzig: S. Hirzel, 1856. Internet Archive, bub_gb_h_Q5AAAAcAAJ (Google library scan). https://archive.org/details/bub_gb_h_Q5AAAAcAAJ."
    url: "https://archive.org/details/bub_gb_h_Q5AAAAcAAJ"
    accessed: 2026-10-02
    source_quality: "scholarly edition or monograph"
    reliability_note: "Contemporary memoir by a friend; reported speech, not Gauss's own writing. Quoted pages checked on the page images (leaf = page + 2); pp. 99–100 read in the OCR text only. Axis scores no longer rest on this alone (P18)."
    used_for: [basics, contribution, worldview, timing, lane_b, collaborators]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "J J O'Connor and E F Robertson"
    citation: "O'Connor, J. J., and E. F. Robertson. \"Johann Carl Friedrich Gauss.\" MacTutor History of Mathematics, University of St Andrews. https://mathshistory.st-andrews.ac.uk/Biographies/Gauss/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Gauss/"
    accessed: 2026-10-02
    source_quality: "reference entry"
    reliability_note: "Biography; cited by paragraph description. Used for B inference_from_work (lasting contributions)."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S3
    type: tertiary
    kind: encyclopedia
    author: "Jeremy John Gray"
    citation: "Gray, Jeremy John. \"Carl Friedrich Gauss.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Carl-Friedrich-Gauss."
    url: "https://www.britannica.com/biography/Carl-Friedrich-Gauss"
    accessed: 2026-10-02
    source_quality: "reference entry"
    reliability_note: "Signed article; first page only. Used for B inference_from_work (lasting contributions)."
    used_for: [identity, basics, contribution, childhood, heritage, institutions, worldview]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    source_quality: "study roster"
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
  - id: S5
    type: primary
    kind: "scholarly book"
    author: "Franz Schmidt and Paul Stäckel (eds.)"
    year: 1899
    citation: "Schmidt, Franz, and Paul Stäckel, eds. Briefwechsel zwischen Carl Friedrich Gauss und Wolfgang Bolyai. Leipzig: B. G. Teubner, 1899. Internet Archive, briefwechselzwi00gausgoog. https://archive.org/details/briefwechselzwi00gausgoog."
    url: "https://archive.org/details/briefwechselzwi00gausgoog"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "Scholarly edition of Gauss's private letters to Bolyai. Read as archive.org OCR (Google scan); letter numbers and dates from page headers. Letters VII (1799.I.9), XXI (1802.XII.3), XLI (1848.IV.20) used for A/C."
    used_for: [worldview]
  - id: S6
    type: primary
    kind: "scholarly book"
    author: "C. Schilling (ed.)"
    year: 1900
    citation: "Schilling, C., ed. Wilhelm Olbers, sein Leben und seine Werke. Band 2, Abtheilung 1: Briefwechsel zwischen Olbers und Gauss. Berlin: Julius Springer, 1900. Internet Archive, p1wilhelmolberss02olbeuoft. https://archive.org/details/p1wilhelmolberss02olbeuoft."
    url: "https://archive.org/details/p1wilhelmolberss02olbeuoft"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "Scholarly edition of Gauss–Olbers letters. Brief 133 (Braunschweig 1805.IX.3, printed pp. 267–269) for Gnade Gottes. Read as archive.org OCR; wording of the grace clause restored from the standard reading of this letter."
    used_for: [worldview]
  - id: S7
    type: secondary
    kind: "scholarly book"
    author: "Karl Alois Kneller"
    year: 1911
    citation: "Kneller, Karl Alois. Christianity and the Leaders of Modern Science: A Contribution to the History of Culture in the Nineteenth Century. Trans. T. M. Kettle. Freiburg im Breisgau / St. Louis: B. Herder, 1911. Internet Archive scan used 2026-10-24."
    url: "https://archive.org/details/christianityandle00kneluoft"
    accessed: 2026-10-24
    source_quality: "scholarly edition or monograph"
    reliability_note: "Secondary digest of Gauss's religious letters (Bolyai/Olbers); used to corroborate the standard reading of the Gnade Gottes and afterlife passages, not as primary wording."
    used_for: [worldview]
  - id: S8
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia. \"Carl Friedrich Gauss.\" English Wikipedia. https://en.wikipedia.org/wiki/Carl_Friedrich_Gauss. Read 2026-10-25 (Religious views: Lutheran church membership)."
    url: "https://en.wikipedia.org/wiki/Carl_Friedrich_Gauss"
    accessed: 2026-10-25
    reliability_note: "Used for heritage/context (Lutheran membership line) and dual bio only; worldview scores not taken from Wikipedia."
    source_quality: "reference entry"
    used_for: [heritage, basics]

---

# Carl Friedrich Gauss

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Carl Friedrich Gauss (1777–1855), German mathematician and astronomer, proved the 17-gon constructible, wrote the Disquisitiones Arithmeticae (1801), developed least squares and the intrinsic geometry of surfaces [S1, p. 16; S2; S3]. Deepen (2026-10-24): his own letters name God's grace in discovery ("bloss durch die Gnade Gottes", to Olbers 1805) and a Creator / afterlife hope (to Bolyai 1799, 1802, 1848) [S5; S6]. Sartorius's memoir remains the fullest friend-report on science kept apart from God-questions [S1, pp. 97, 103]. primary_system still BELOW_THRESHOLD (confession open). A_locus 1 @ 0.5 (consistent private letters; named alt 2); B_cause 3 @ 0.5 (inference from lasting work; named alt 4); C, D, E and mid_basin below threshold. Chart: unplotted → faded filled.

## Life and work

Born poor in Brunswick and supported by the duke, he studied at the Collegium Carolinum and Göttingen, took his degree at Helmstedt (1799), directed the Göttingen observatory from 1807, led the Hanover survey (1818–32) and worked on magnetism with Weber [S2; S3].

## Contribution and impact

Number theory, least squares and the orbit of Ceres, differential geometry (theorema egregium), potential theory and magnetism [S2; S3].

## Childhood and education

Only child of poor parents; a calculating prodigy noticed at elementary school by Büttner and Bartels [S2; S3].

## Adult working worldview

Own letters: hope of a better future (Bolyai 1799) and of true life in a spiritual Heimat (Bolyai 1802); discovery credited to "die Gnade Gottes" (Olbers 1805); late letter names "der Schöpfer unsrer Existenz" and a "schöneren Metamorphose" (Bolyai 1848) [S5; S6]. Sartorius still the fullest friend-report that science and religion were kept apart [S1, pp. 97–98] and that confession was left aside [S1, pp. 99–100]. A scored 1 @ 0.5 from the letters; B scored 3 @ 0.5 from lasting astronomy/physics work (P30/P35) [S2; S3].

## Heritage (context only)

German, from Brunswick [S2]. Context only.

## Timing

First lasting contribution 1795, least squares, the start of the listed 1795–1801 item [S1, p. 16] (P12, P13, P17, P23), at 18. The 17-gon is dated 1796 by his own note [S1, p. 16]; Britannica says 1792 [S3], which would make it the earliest item, so the year is held at 0.5 (P25).

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form present (science as a closed logical building [S1, p. 97]); circle partly present.

## Open questions

- Gauss's religious notes in his own hand (Sartorius p. 100).
- Page-image re-check of Schilling Brief 133 and Bolyai XLI (OCR used).
- Confession code still open (CLASS_THEISM / DEISM / CHRIST).

## Research log

- 2026-10-02: Read MacTutor, Britannica (Gray, first page) and Sartorius (1856) on the Internet Archive scan; checked pp. 16, 97, 98, 101, 102 and 103 on the page images.
- 2026-10-02 (v8 method rulings): Reopened Sartorius p. 16 on the page image (1795, least squares, 'hier' = Göttingen) and pp. 97–103 for the axes.
- 2026-10-02 (stage 3 rulings P14–P28): Reopened MacTutor's biography for the magnetism papers ('by 1840') and the potential-theory remark.
- 2026-10-24 (deepen D1, queue #15): Read Schmidt–Stäckel Briefwechsel Gauss–Bolyai (1899) and Schilling Olbers–Gauss Bd. 2.1 (1900) on archive.org OCR; Kneller 1911 digest. A and B scored; person-file commit only.
