---
record:
  record_type: person
  schema_version: "1.2"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch B)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (stage 3 batch B). Basics from MacTutor and Britannica (Gray, first page). Worldview from Sartorius von Waltershausen, Gauss zum Gedächtniss (1856), a friend's memoir with reported sayings, read on the Internet Archive scan (pp. 16, 97, 98, 101, 102, 103 checked on the page images; pp. 99–100 in the OCR text only). No writing by Gauss on religion was read. primary_system BELOW_THRESHOLD. A 1 (0.5), B 4 (0.5); C, D, E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. All scores are drafts for v8's review. Not reviewed."}

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
  full_name: {value: "Johann Carl Friedrich Gauss", certainty: 0.7, cites: [{source: S3, locator: "Quick Facts ('Original name: Johann Friedrich Carl Gauss')"}], how_known: "Britannica gives the original name as Johann Friedrich Carl Gauss; the usual form is Carl Friedrich Gauss (S2)."}
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
    value: 1796
    certainty: 0.5
    cites: [{source: S1, locator: "p. 16"}, {source: S2, locator: "Biography (Göttingen paragraph)"}]
    how_known: "The theory of cyclotomy with the 17-gon construction, dated 30 March 1796 by Sartorius from Gauss's own note in his copy of the Disquisitiones (S1, p. 16). Sources disagree, so 0.5. Draft judgment (one line): the dated note is preferred to the round dates."
    alternatives:
      - {value: 1795, cites: [{source: S1, locator: "p. 16"}], note: "Method of least squares, found 1795 (Sartorius) but published only in 1809."}
      - {value: 1792, cites: [{source: S3, locator: "'Gauss's first significant discovery, in 1792'"}], note: "Britannica dates the 17-gon discovery to 1792."}
  era_bucket: {value: "1750 to 1849", certainty: 1.0, cites: [{source: S1, locator: "p. 16"}, {source: S3, locator: "17-gon paragraph"}], how_known: "Every candidate year falls in 1750–1849 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 1.0, cites: [{source: S2, locator: "Quick Info"}], how_known: "Germany is Western Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Western Europe", certainty: 1.0, cites: [{source: S2, locator: "Biography"}], how_known: "Brunswick and Göttingen."}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S2, locator: "Biography"}], how_known: "As the sources record it."}
  languages_of_work: {value: [Latin, German], certainty: 0.7, cites: [{source: S2, locator: "Biography (Disquisitiones Arithmeticae; Über ein neues allgemeines Grundgesetz der Mechanik)"}], how_known: "Titles of his works in MacTutor."}
  occupations: {value: ["mathematician", "astronomer", "physicist", "geodesist", "observatory director"], certainty: 1.0, cites: [{source: S2, locator: "Biography"}, {source: S3, locator: "opening"}], how_known: "Two sources."}

contribution:
  fields: {value: ["number theory", "geometry", "probability theory", "geodesy", "astronomy", "potential theory", "magnetism"], certainty: 1.0, cites: [{source: S3, locator: "opening"}, {source: S2, locator: "Biography"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Constructibility of the regular 17-gon (theory of cyclotomy)", year: "1796", kind: discovery, lasting: "opened the way to later Galois theory (Britannica)", certainty: 1.0, cites: [{source: S1, locator: "p. 16"}, {source: S2, locator: "Biography"}, {source: S3, locator: "17-gon paragraph"}], how_known: "Three sources (the year differs; see basics)."}
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
  definition_fit: {value: "clearly meets", rationale: "Founder of modern number theory and of differential geometry of surfaces.", certainty: 1.0, cites: [{source: S3, locator: "opening"}], how_known: "Sources agree."}

childhood:
  family_religion: {value: TODO, note: "Not stated in the sources read."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Only child of poor parents; a 'devoted mother' who with his teachers recommended him to the duke", role: "parents", certainty: 0.7, cites: [{source: S3, locator: "childhood paragraph"}], how_known: "Britannica."}
  household_circumstances: {value: "Poor family; ducal stipend from 1791", certainty: 0.7, cites: [{source: S3, locator: "childhood paragraph"}], how_known: "Britannica (MacTutor mentions the stipend before 1792)."}
  schooling:
    - {value: "Elementary school in Brunswick (teacher Büttner, assistant Martin Bartels)", stage: "dame or charity school", years: "from age 7", certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraph 1"}], how_known: "MacTutor; nearest stage."}
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
  working_years: {value: "1795–1855", certainty: 1.0, cites: [{source: S2, locator: "Biography"}], how_known: "From Göttingen to his death."}
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
    A_locus:
      value: 1
      basis: scholarly_reconstruction
      certainty: 0.5
      cites: [{source: S1, locator: "pp. 101–103"}]
      how_known: "A friend's memoir (reported views and sayings), so 0.5."
      rationale: "Draft judgment (one line): leans interventionist because the God reported is personal and transcendent: 'der feste Glaube an einen letzten Ordner der Dinge, an einen ewigen, gerechten, allweisen, allmächtigen Gott' (p. 103), with a second 'rein geistige Weltordnung' beside the material one (p. 103). Named alternative: 2, because the God is also described as an 'alles durchdringenden Intelligenz, die von einem Sonnensystem zum andern im Weltall wiederklingt' (p. 102), which leans toward an order in the world."
    B_cause:
      value: 4
      basis: scholarly_reconstruction
      certainty: 0.5
      cites: [{source: S1, locator: "pp. 97–98"}, {source: S2, locator: "Biography"}]
      how_known: "Coder's reading of his working science (P6) plus a friend's memoir, so 0.5 (same treatment as Fermi and Dirac)."
      rationale: "Scored on his account of nature (P6). Astronomy, geodesy and mechanics by exact law and least squares (S2); for Sartorius the principle of least constraint was 'die mathematische Verkörperung jenes ethischen Grundgedankens, den er für das Universum als bindend erkannte' (p. 97), and Gauss recognised 'die durchs ganze Weltall gehende Logik' even where our minds cannot enter (pp. 97–98). No miracle, petition or exemption in anything read."
    C_ledger: {value: BELOW_THRESHOLD, how_known: "Survival after death is affirmed (S1, pp. 101, 103) and Sartorius calls the spiritual life of the universe a 'grosses von ewiger Wahrheit durchdrungenes Rechtsverhältniss' (p. 101), but nothing read speaks of reward, punishment or judgement. Draft judgment (one line): not scored from the memoirist's phrase."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "Questions of God lie 'ausserhalb des Gebietes der Wissenschaft' (S1, p. 97), but nothing read speaks of revelation or scripture."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Scored on the world's order (P7). Nothing read addresses favour for a group in events; not scored from working science alone (same treatment as Fermi and Dirac)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus = 1 but only at 0.5, and B_cause is only 0.5; the P4 test needs both at 0.7 or more."}
  statements:
    - text: "»Es gibt Fragen,« sagte er ein Mal, »auf deren Beantwortung ich einen unendlich viel höhern Werth legen würde als auf die mathematischen z. B. über Ethik, über unser Verhältniss zu Gott, über unsere Bestimmung und über unsere Zukunft; allein ihre Lösung liegt ganz unerreichbar über uns und ganz ausserhalb des Gebietes der Wissenschaft.«"
      cites: [{source: S1, locator: "p. 97"}]
      date: "1856"
      context: "Sartorius reporting a remark of Gauss; date is the memoir's publication, the remark is undated."
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
  major_work_period: {value: "1795–1840", certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "From least squares and the 17-gon to the magnetism work with Weber (coder's span)."}
  age_at_first_lasting_contribution: {value: 18, certainty: 0.5, cites: [{source: S1, locator: "p. 16"}], how_known: "Born 30 April 1777; 17-gon on 30 March 1796, so 18. Other dates give 15 (1792) or 18 (1795)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "The memoir gives no dates for his views."}
  lio_views_relative_to_major_work: {value: "unclear", rationale: "No dated statement.", certainty: 0.5, cites: [{source: S1, locator: "pp. 97–103"}], how_known: "Undated memoir."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "Sartorius: by science he understood only the 'streng in sich abgeschlossene logische Gebäude' built on generally recognised truths by 'eine eiserne Gedankenkette' (p. 97).", certainty: 0.5, cites: [{source: S1, locator: "p. 97"}], how_known: "Memoir plus coder's reading."}
  form_acquired: {value: "childhood or adolescence", certainty: 0.5, cites: [{source: S2, locator: "Biography, paragraph 1"}], how_known: "Advanced mathematics before 18."}
  circle_present: {value: "partly", rationale: "Least constraint as the mathematical embodiment of an ethical idea binding on the universe (p. 97), and logic through the whole universe (pp. 97–98), but a second, purely spiritual world order beside the material (p. 103).", certainty: 0.5, cites: [{source: S1, locator: "pp. 97–98, 103"}], how_known: "Memoir plus coder's reading."}
  reading: "As belief, not finding: form present, circle partly present on a friend's report. The record does not test H1."
  notes: ""

institutions:
  - {value: "Göttingen Observatory and University of Göttingen", role: "director of the observatory", years: "1807–1855", kind: university, certainty: 1.0, cites: [{source: S2, locator: "Biography (1807)"}], how_known: "MacTutor."}
  - {value: "Survey of the Kingdom of Hanover", role: "in charge of observations", years: "1818–1832", kind: "government or state body", certainty: 0.7, cites: [{source: S3, locator: "Hanover survey paragraph"}], how_known: "Britannica."}
collaborators:
  - {value: "Wilhelm Weber", relation: collaborator, note: "physics professor at Göttingen from 1831", certainty: 1.0, cites: [{source: S2, locator: "Biography (1831)"}], how_known: "MacTutor."}
  - {value: "Bernhard Riemann", roster_id: riemann-bernhard, relation: "influenced", note: "approved his doctoral thesis and heard his probationary lecture", certainty: 1.0, cites: [{source: S2, locator: "Biography (1850 onward)"}], how_known: "MacTutor."}
  - {value: "Wolfgang Sartorius von Waltershausen", relation: other, note: "friend and memoirist", certainty: 0.7, cites: [{source: S1, locator: "pp. 99–100"}], how_known: "His own account of many years' friendship."}

review:
  roster_status_reason: {value: "Core in v8 (F 5: Claude, DeepSeek, Gemini, GPT, Grok).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 15"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "17-gon date: 30 March 1796 (Sartorius, from Gauss's own note) vs 1792 (Britannica)."
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

Carl Friedrich Gauss (1777–1855), German mathematician and astronomer, proved the 17-gon constructible, wrote the Disquisitiones Arithmeticae (1801), developed least squares and the intrinsic geometry of surfaces [S1, p. 16; S2; S3]. His friend Sartorius reports a firm belief in a personal, just, almighty God and in survival after death, and his view that questions about God lie "ganz ausserhalb des Gebietes der Wissenschaft" [S1, pp. 97, 103]. No writing of his own on religion was read. primary_system BELOW_THRESHOLD. Draft scores: A 1 (0.5), B 4 (0.5); C, D, E below threshold; mid_basin below threshold.

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

First lasting contribution 1796 (17-gon, dated by his own note [S1, p. 16]); Britannica says 1792 [S3].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form present (science as a closed logical building [S1, p. 97]); circle partly present.

## Open questions

- Gauss's own religious notes and letters.

## Research log

- 2026-10-02: Read MacTutor, Britannica (Gray, first page) and Sartorius (1856) on the Internet Archive scan; checked pp. 16, 97, 98, 101, 102 and 103 on the page images.
