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
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (stage 3 batch B). Basics from MacTutor and Dedekind's 'Bernhard Riemann's Lebenslauf'. Worldview from Riemann's own unpublished philosophical fragments and Dedekind's Lebenslauf, both in the Gesammelte mathematische Werke (2nd ed., 1892; University of Toronto scan on the Internet Archive; pp. 518, 519, 521, 541, 557 and 558 checked on the page images). primary_system BELOW_THRESHOLD (CHRIST and CLTHEI candidates). A 1 (0.5), B 4 (0.5); C, D, E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. All scores are drafts for v8's review. Not reviewed."}

identity:
  id: riemann-bernhard
  display_name: "Bernhard Riemann"
  roster:
    canonical_name: "Bernhard Riemann"
    rank: 12
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: mathematics
    field_bucket: mathematics
  full_name: {value: "Georg Friedrich Bernhard Riemann", certainty: 1.0, cites: [{source: S1, locator: "p. 541 (Lebenslauf)"}, {source: S2, locator: "heading"}], how_known: "Two sources."}
  native_name: {value: "Georg Friedrich Bernhard Riemann (German)", certainty: 1.0, cites: [{source: S1, locator: "p. 541"}], how_known: "German name."}
  aliases:
    - {name: "Bernhard-Riemann", kind: "roster alias"}
    - {name: "Riemann-Bernhard", kind: "roster alias"}

basics:
  birth:
    date: {value: "1826-09-17", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "p. 541"}, {source: S2, locator: "Quick Info"}], how_known: "Two sources agree."}
    place: {value: "Breselenz, near Dannenberg", modern_name: "Breselenz, Lower Saxony, Germany", polity_then: "Kingdom of Hanover", certainty: 1.0, cites: [{source: S1, locator: "p. 541"}, {source: S2, locator: "Quick Info"}], how_known: "Two sources agree."}
  death:
    date: {value: "1866-07-20", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "p. 558 (grave inscription)"}, {source: S2, locator: "Quick Info"}], how_known: "Two sources agree."}
    place: {value: "Selasca, near Intra, Lago Maggiore", modern_name: "Selasca (Verbania), Piedmont, Italy", polity_then: "Kingdom of Italy", certainty: 1.0, cites: [{source: S1, locator: "pp. 557–558"}, {source: S2, locator: "Quick Info"}], how_known: "Two sources agree."}
  first_lasting_contribution_year: {value: 1851, certainty: 0.7, cites: [{source: S2, locator: "Biography (thesis examined 16 December 1851)"}], how_known: "His doctoral thesis on complex functions, 'one of the most remarkable pieces of original work to appear in a doctoral thesis' (MacTutor). One source."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S2, locator: "Biography (1851)"}], how_known: "From first_lasting_contribution_year (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 1.0, cites: [{source: S2, locator: "Quick Info"}], how_known: "Germany is Western Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Western Europe", certainty: 1.0, cites: [{source: S2, locator: "Biography"}], how_known: "Göttingen (and Berlin as a student); Italy only for his health."}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S2, locator: "Biography"}], how_known: "As the sources record it."}
  languages_of_work: {value: [German], certainty: 1.0, cites: [{source: S1, locator: "whole volume"}], how_known: "His works are in German."}
  occupations: {value: ["mathematician", "university professor"], certainty: 1.0, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor."}

contribution:
  fields: {value: ["complex analysis", "differential geometry", "number theory", "real analysis", "mathematical physics"], certainty: 0.7, cites: [{source: S2, locator: "Summary; Biography"}], how_known: "MacTutor."}
  lasting_original_contributions:
    - {value: "Doctoral thesis on complex functions (Riemann surfaces, Dirichlet principle)", year: "1851", kind: theory, lasting: "foundation of geometric function theory", certainty: 0.7, cites: [{source: S2, locator: "Biography (1851)"}], how_known: "MacTutor."}
    - {value: "Riemann integral and trigonometric series (Habilitation dissertation)", year: "1854", kind: "concept or term", lasting: "standard analysis", certainty: 0.7, cites: [{source: S2, locator: "Biography (Habilitation)"}], how_known: "MacTutor."}
    - {value: "Über die Hypothesen, welche der Geometrie zu Grunde liegen (Riemannian geometry)", year: "1854", kind: theory, lasting: "geometry of general relativity", certainty: 0.7, cites: [{source: S2, locator: "Biography (10 June 1854)"}], how_known: "MacTutor (delivered 1854, published 1868)."}
    - {value: "Zeta function in the complex plane and the Riemann hypothesis", year: "1859", kind: theory, lasting: "central unsolved problem of mathematics", certainty: 0.7, cites: [{source: S2, locator: "Biography (1859)"}], how_known: "MacTutor."}
  evidence_of_impact:
    - {value: "Elected to the Berlin Academy of Sciences, 1859", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S2, locator: "Biography (1859)"}], how_known: "MacTutor."}
  major_works:
    - {value: "Über die Anzahl der Primzahlen unter einer gegebenen Grösse", year: 1859, kind: "paper or paper series", certainty: 0.7, cites: [{source: S2, locator: "Biography (1859)"}], how_known: "MacTutor."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Founder of Riemannian geometry and Riemann surfaces; author of the Riemann hypothesis.", certainty: 1.0, cites: [{source: S2, locator: "Summary; Biography"}], how_known: "Sources agree."}

childhood:
  family_religion: {value: "Lutheran (father a Lutheran minister)", certainty: 1.0, cites: [{source: S2, locator: "Biography, paragraph 1"}, {source: S1, locator: "p. 541 ('Prediger')"}], how_known: "Two sources."}
  family_religious_practice: {value: "Pastor's household; confirmed by his father at thirteen and a half", certainty: 1.0, cites: [{source: S1, locator: "p. 541"}], how_known: "Dedekind's Lebenslauf (checked on the page image)."}
  parents_and_household:
    - {value: "Father, Friedrich Bernhard Riemann, former lieutenant under Wallmoden in the Wars of Liberation, then pastor (Prediger) at Breselenz and later Quickborn; taught Bernhard almost alone until the Gymnasium", name: "Friedrich Bernhard Riemann", role: father, certainty: 1.0, cites: [{source: S1, locator: "p. 541"}, {source: S2, locator: "Biography, paragraph 1"}], how_known: "Two sources."}
    - {value: "Mother, Charlotte Ebell, daughter of Hofrath Ebell of Hanover", name: "Charlotte Riemann (née Ebell)", role: mother, certainty: 1.0, cites: [{source: S1, locator: "p. 541"}, {source: S2, locator: "Biography, paragraph 1"}], how_known: "Two sources."}
  household_circumstances: {value: "Second of six children in a country parsonage", certainty: 1.0, cites: [{source: S1, locator: "p. 541"}, {source: S2, locator: "Biography, paragraph 1"}], how_known: "Two sources."}
  schooling:
    - {value: "Taught at home by his father, helped from about age ten by the teacher Schulz (arithmetic and geometry)", stage: home, years: "–1840", certainty: 1.0, cites: [{source: S1, locator: "p. 541"}, {source: S2, locator: "Biography, paragraph 1"}], how_known: "Two sources."}
    - {value: "Lyceum, Hanover", stage: "grammar or secondary school", years: "1840–1842", certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraph 2"}], how_known: "MacTutor."}
    - {value: "Johanneum Gymnasium, Lüneburg (classics, Hebrew, theology; mathematics books from the director's library)", stage: "grammar or secondary school", years: "1842–1846", certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraph 2"}], how_known: "MacTutor."}
    - {value: "University of Göttingen, entered in theology, then mathematics; Berlin 1847–1849", stage: university, years: "1846–1851", certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraphs 3–6"}], how_known: "MacTutor."}
  early_mathematics: {value: "advanced mathematics", note: "Read Legendre's number theory in six days at the Gymnasium (MacTutor).", certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraph 2"}], how_known: "MacTutor."}
  early_geometric_style_reasoning: {value: "Geometry with the teacher Schulz from about age ten", certainty: 0.7, cites: [{source: S1, locator: "p. 541"}], how_known: "Dedekind ('guten Unterricht im Rechnen und in der Geometrie'); nothing on proof style."}
  early_science_exposure: []
  key_early_reading:
    - {value: "Legendre, Théorie des nombres", certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraph 2"}], how_known: "MacTutor."}
  childhood_mentors:
    - {value: "His father, his first teacher", name: "Friedrich Bernhard Riemann", certainty: 1.0, cites: [{source: S1, locator: "p. 541"}], how_known: "Dedekind."}
  languages_in_childhood: {value: [German], certainty: 1.0, cites: [{source: S1, locator: "p. 541"}], how_known: "German family."}
  notable_events:
    - {value: "Confirmed by his father, then left home for school", year: "1840", age: 13, certainty: 0.7, cites: [{source: S1, locator: "p. 541"}], how_known: "Dedekind gives the age (thirteen and a half); the year follows from his birth date."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1849–1866", certainty: 1.0, cites: [{source: S2, locator: "Biography"}], how_known: "From his return to Göttingen to his death."}
  nominal_affiliations: []
  self_described_science_religion_relation:
    value: "In an unpublished fragment he wrote that freedom 'ist sehr wohl vereinbar mit strenger Gesetzmässigkeit des Naturlaufs', and that the concept of providence must be supplemented by that of a time-acting God, 'eines Lenkers der Herzen und Geschicke der Menschen'; the passage stands in the Thesis column of a table of antinomies, so it may set out a position rather than state his settled view."
    certainty: 0.5
    cites: [{source: S1, locator: "pp. 518–519"}]
    how_known: "His own unpublished notes, printed in the Nachlass; one fragment, laid out as an antinomy, so 0.5."
  primary_system:
    value: BELOW_THRESHOLD
    cites: [{source: S1, locator: "pp. 557–558 (Lebenslauf)"}, {source: S1, locator: "pp. 518–519 (fragment)"}]
    how_known: "Dedekind, his friend and editor, writes that the piety planted in his father's house stayed with him all his life and that he served his God faithfully, 'wenn auch nicht in derselben Form'; daily self-examination before God was, 'nach seinem eigenen Ausspruche', the main thing in religion for him; he died while his wife prayed the Lord's Prayer with him (pp. 557–558). But his own writing read speaks only of God, not of Christ, scripture, creed or church (CHRIST use_when), and the God of his fragment, who steers 'Herzen und Geschicke der Menschen' (p. 519), points rather to CLTHEI (CHRIST do_not_use_when). A Lutheran upbringing alone gives no code."
    note: "Draft judgment (one line): BELOW_THRESHOLD because no own writing shows specifically Christian belief, as the batch 3 audit required for Gödel and Heisenberg. Leading candidate CHRIST (Dedekind's testimony); CLTHEI second (the fragment). Riemann's letters to his family would decide it."
  secondary_system: {value: UNKNOWN, how_known: "No second system in what was read."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Leading candidate, not coded: Dedekind's testimony of lifelong piety and the Lord's Prayer at his death (S1, pp. 557–558), but no writing of his own read names Christ, scripture or creed, and Dedekind says his service of God was not in the same form as his father's. CHRIST is a draft system file.", cites: [{source: S1, locator: "pp. 557–558"}]}
    - {code: CLTHEI, reason: "Considered: a time-acting God, 'Lenker der Herzen und Geschicke der Menschen', in place of a timeless providence (S1, p. 519); not coded because the fragment is an antinomy table (the Thesis column may not be his settled view). CLTHEI is a draft system file.", cites: [{source: S1, locator: "pp. 518–519"}]}
    - {code: PANPSY, reason: "Considered and rejected: the fragments discuss Fechner's 'Erdseele' and the souls of dead creatures as elements of the earth's soul-life (S1, p. 518), but in a form that reports Fechner ('sollen'), not as his own view. PANPSY is a stub system file (flag).", cites: [{source: S1, locator: "p. 518"}]}
  lio_axes:
    A_locus:
      value: 1
      basis: scholarly_reconstruction
      certainty: 0.5
      cites: [{source: S1, locator: "pp. 518–519"}, {source: S1, locator: "pp. 557–558"}]
      how_known: "One fragment of his own plus a friend's report, so 0.5."
      rationale: "Draft judgment (one line): leans interventionist because the God of the fragment acts in time and steers 'Herzen und Geschicke der Menschen' (p. 519), and Dedekind reports prayer and daily self-examination before God (pp. 557–558). Named alternative: BELOW_THRESHOLD, because the passage stands in the Thesis column of an antinomy table and may not state his own view."
    B_cause:
      value: 4
      basis: consistent_private_letters
      certainty: 0.5
      cites: [{source: S1, locator: "p. 521"}, {source: S1, locator: "p. 519"}]
      how_known: "His own unpublished notes (private writing). One fragment states it plainly (p. 521); the second sentence (p. 519) sits in an antinomy column, so the evidence counts as one document: 0.5 (single-document rule)."
      rationale: "Scored on his account of nature (P6). 'Naturwissenschaft ist der Versuch, die Natur durch genaue Begriffe aufzufassen'; when something happens that the concepts did not expect, the task is to complete or rework them until the observation 'aufhört, unmöglich oder unwahrscheinlich zu sein' (p. 521). Anomalies are met by better concepts, never by exceptions; freedom 'ist sehr wohl vereinbar mit strenger Gesetzmässigkeit des Naturlaufs' (p. 519). Named alternative: 3, since the same passage asks for a God who steers the fates of men, which could allow guidance in events."
    C_ledger: {value: BELOW_THRESHOLD, how_known: "Nothing read on judgement, reward or punishment. Daily self-examination before God (S1, p. 558) is a practice, not a doctrine of reckoning; the fourth antinomy names 'Unsterblichkeit' (p. 519) without saying what follows."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "Nothing read on revelation or scripture as a source of knowledge."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Scored on the world's order (P7). Nothing read addresses favour for a group in events."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus = 1 but only at 0.5, and B_cause is only 0.5; the P4 test needs both at 0.7 or more."}
  statements:
    - text: "Freiheit ist sehr wohl vereinbar mit strenger Gesetzmässigkeit des Naturlaufs. Aber der Begriff eines zeitlosen Gottes ist daneben nicht haltbar. Es muss vielmehr die Beschränkung, welche Allmacht und Allwissenheit durch die Freiheit der Geschöpfe in der oben festgestellten Bedeutung erleiden, aufgehoben werden durch die Annahme eines zeitlich wirkenden Gottes, eines Lenkers der Herzen und Geschicke der Menschen, der Begriff der Vorsehung muss ergänzt und zum Theil ersetzt werden durch den Begriff der Weltregierung."
      cites: [{source: S1, locator: "p. 519 (Antinomien, IV, Thesis column)"}]
      date: "1892"
      context: "Unpublished fragment 'Zur Psychologie und Metaphysik', table of 'Antinomien'; under IV, Thesis 'Unsterblichkeit'. Undated; the date given is the edition's. Row III reads Thesis 'Ein zeitlich wirkender Gott (Weltregierung)', Antithesis 'Ein zeitloser, persönlicher, allwissender, allmächtiger, allgütiger Gott (Vorsehung)' (p. 518)."
      axes: [A_locus, B_cause]
      kind: "notebook or diary"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "Naturwissenschaft ist der Versuch, die Natur durch genaue Begriffe aufzufassen."
      cites: [{source: S1, locator: "p. 521"}]
      date: "1892"
      context: "Opening of the fragment 'Versuch einer Lehre von den Grundbegriffen der Mathematik und Physik als Grundlage für die Naturerklärung' (section II, 'Erkenntnisstheoretisches'). Undated; edition date given."
      axes: [B_cause]
      kind: "notebook or diary"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "Geschieht aber Etwas, was nach ihnen nicht erwartet wird, also nach ihnen unmöglich oder unwahrscheinlich ist, so entsteht die Aufgabe, sie so zu ergänzen oder, wenn nöthig, umzuarbeiten, dass nach dem vervollständigten oder verbesserten Begriffssystem das Wahrgenommene aufhört, unmöglich oder unwahrscheinlich zu sein."
      cites: [{source: S1, locator: "p. 521"}]
      date: "1892"
      context: "Same fragment; 'ihnen' are the concepts through which we grasp nature."
      axes: [B_cause]
      kind: "notebook or diary"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "Der fromme Sinn, der im Vaterhaus gepflanzt war, blieb ihm durch das ganze Leben, und er diente, wenn auch nicht in derselben Form, treu seinem Gott; mit der grössten Pietät vermied er, Andere in ihrem Glauben zu stören; die tägliche Selbstprüfung vor dem Angesichte Gottes war, nach seinem eigenen Ausspruche, für ihn eine Hauptsache in der Religion."
      cites: [{source: S1, locator: "pp. 557–558 (Lebenslauf)"}]
      date: "1892"
      context: "Dedekind's account of Riemann's death and character, closing the Lebenslauf; Dedekind reports a saying of Riemann's in the last clause. The Lebenslauf first appeared in the 1876 first edition (not checked)."
      axes: [A_locus]
      kind: "reported speech"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
  changes_over_life: []
  coder_notes: "CHRIST and CLTHEI are drafts; PANPSY is a stub system file (flag). The 1892 Werke is a scholarly edition (Weber with Dedekind) of his published works and Nachlass, read on the University of Toronto scan (archive.org page n-index = printed page + 15). The philosophical fragments are undated, so statement dates are the edition's. The antinomy layout (Thesis and Antithesis columns) was checked on the page images: the long passage is in the Thesis column under IV. Fechner material on p. 518 is reported with 'sollen' and is not scored. The grave inscription (Romans 8:28, p. 558) was chosen by his Italian friends (footnote), so it is not his act. changes_over_life is empty: Dedekind's 'not in the same form' suggests a change from his father's church form but gives no date."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "German (Kingdom of Hanover)", certainty: 1.0, cites: [{source: S1, locator: "p. 541"}, {source: S2, locator: "Quick Info"}], how_known: "Two sources."}
  religious_heritage_by_birth: {value: "Lutheran", certainty: 1.0, cites: [{source: S2, locator: "Biography, paragraph 1"}, {source: S1, locator: "p. 541"}], how_known: "Father a Lutheran pastor."}
  baptism_or_initiation: {value: "Confirmed by his father at thirteen and a half", certainty: 1.0, cites: [{source: S1, locator: "p. 541"}], how_known: "Dedekind (page image)."}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1851–1859", certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "Thesis to the zeta paper."}
  age_at_first_lasting_contribution: {value: 25, certainty: 0.7, cites: [{source: S2, locator: "Quick Info; Biography (16 December 1851)"}], how_known: "Born September 1826; thesis examined December 1851."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "The fragments are undated."}
  lio_views_relative_to_major_work: {value: "unclear", rationale: "Undated fragments.", certainty: 0.5, cites: [{source: S1, locator: "pp. 518–521"}], how_known: "No dates."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "He wrote of concept systems (Begriffssysteme) refined against experience (p. 521) and of the limit method (p. 519); conceptual rather than axiomatic.", certainty: 0.5, cites: [{source: S1, locator: "pp. 519, 521"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "p. 541"}], how_known: "Early arithmetic and geometry; nothing on method."}
  circle_present: {value: "partly", rationale: "Strict natural law together with a time-acting God who governs the world (p. 519), in an antinomy table.", certainty: 0.5, cites: [{source: S1, locator: "p. 519"}], how_known: "Coder's reading."}
  reading: "As belief, not finding: form partly present, circle partly present. The record does not test H1."
  notes: ""

institutions:
  - {value: "University of Göttingen", role: "Privatdozent (1854), professor (1857), chair of mathematics (1859)", years: "1849–1866", kind: university, certainty: 0.7, cites: [{source: S2, locator: "Biography (1854, 1857, 1859)"}], how_known: "MacTutor."}
  - {value: "Berlin Academy of Sciences", role: "member", years: "1859–1866", kind: "academy or learned society", certainty: 0.7, cites: [{source: S2, locator: "Biography (1859)"}], how_known: "MacTutor."}
collaborators:
  - {value: "Carl Friedrich Gauss", roster_id: gauss-carl-friedrich, relation: teacher, note: "supervised the thesis; chose the 1854 lecture", certainty: 1.0, cites: [{source: S2, locator: "Biography (1851, 1854)"}], how_known: "MacTutor."}
  - {value: "Peter Gustav Lejeune Dirichlet", relation: "influenced by", note: "main influence in Berlin", certainty: 0.7, cites: [{source: S2, locator: "Biography (Berlin)"}], how_known: "MacTutor."}
  - {value: "Wilhelm Weber", relation: "mentor or employer", note: "Riemann was his assistant for 18 months", certainty: 0.7, cites: [{source: S2, locator: "Biography (1849)"}], how_known: "MacTutor."}
  - {value: "Richard Dedekind", relation: collaborator, note: "friend; wrote the Lebenslauf and co-edited the Werke", certainty: 1.0, cites: [{source: S1, locator: "title page; p. 541"}, {source: S2, locator: "Biography (1857)"}], how_known: "Two sources."}

review:
  roster_status_reason: {value: "Core in v8 (F 5: Claude, DeepSeek, Gemini, GPT, Grok).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 12"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Worldview rests on one undated fragment laid out as an antinomy and on Dedekind's memoir."
    - "Britannica was not read for Riemann; basics are MacTutor and Dedekind."
  open_questions:
    - "Read the first edition (1876) of the Werke and Riemann's letters (e.g. to his family) for direct religious statements."
    - "Is the Thesis column of the antinomy table Riemann's own view? A scholarly study of the fragments would settle A."

sources:
  - id: S1
    type: primary
    kind: "scholarly edition"
    author: "Bernhard Riemann; ed. Heinrich Weber with Richard Dedekind"
    year: 1892
    citation: "Riemann, Bernhard. Gesammelte mathematische Werke und wissenschaftlicher Nachlass. Edited by Heinrich Weber with Richard Dedekind. 2nd ed. Leipzig: B. G. Teubner, 1892. Includes 'Fragmente philosophischen Inhalts' (from p. 509; section II 'Erkenntnisstheoretisches' from p. 521) and Dedekind, 'Bernhard Riemann's Lebenslauf' (from p. 539; text from p. 541 to p. 558). Internet Archive, gesammeltemathem00riemuoft (University of Toronto). https://archive.org/details/gesammeltemathem00riemuoft."
    url: "https://archive.org/details/gesammeltemathem00riemuoft"
    accessed: 2026-10-02
    reliability_note: "Scholarly edition; library scan. pp. 518, 519, 521, 541, 557 and 558 checked on the page images. Section start pages (509, 521, 539) are from the table of contents in the OCR text; only 521 and 541 were seen on images."
    used_for: [identity, basics, childhood, worldview, heritage, timing, lane_b, collaborators]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "J J O'Connor and E F Robertson"
    citation: "O'Connor, J. J., and E. F. Robertson. \"Georg Friedrich Bernhard Riemann.\" MacTutor History of Mathematics, University of St Andrews. https://mathshistory.st-andrews.ac.uk/Biographies/Riemann/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Riemann/"
    accessed: 2026-10-02
    reliability_note: "Biography; cited by paragraph description."
    used_for: [identity, basics, contribution, childhood, heritage, timing, institutions, collaborators]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
---

# Bernhard Riemann

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Georg Friedrich Bernhard Riemann (1826–1866), German mathematician, founded the theory of Riemann surfaces and Riemannian geometry and posed the Riemann hypothesis [S2]. The son of a Lutheran pastor, he kept a pious outlook all his life, serving his God "wenn auch nicht in derselben Form" (Dedekind) [S1, pp. 557–558]; in an unpublished fragment he argued for a time-acting God who steers "Herzen und Geschicke der Menschen" alongside strict natural law [S1, p. 519]. Draft codes: primary_system BELOW_THRESHOLD (candidates CHRIST, CLTHEI); A 1 (0.5), B 4 (0.5); C, D, E below threshold; mid_basin below threshold.

## Life and work

Taught at home by his father, he went to school in Hanover and Lüneburg, entered Göttingen in theology in 1846, switched to mathematics, studied in Berlin, and returned to Göttingen, where he held Gauss's old chair from 1859 [S1, p. 541; S2]. He died of tuberculosis at Selasca on Lago Maggiore in 1866 [S1, pp. 557–558; S2].

## Contribution and impact

Thesis on complex functions (1851), the Riemann integral and the 1854 lecture on the foundations of geometry, abelian functions (1857) and the zeta paper (1859) [S2].

## Childhood and education

Second of six children in a parsonage; his father taught him almost alone and confirmed him at thirteen and a half [S1, p. 541].

## Adult working worldview

His notes treat natural science as grasping nature "durch genaue Begriffe", reworked whenever something unexpected occurs [S1, p. 521]. A table of antinomies sets a time-acting God against a timeless providence [S1, pp. 518–519]. Dedekind reports lifelong piety and daily self-examination before God [S1, pp. 557–558].

## Heritage (context only)

Lutheran pastor's family in the Kingdom of Hanover [S1, p. 541; S2]. Context only.

## Timing

First lasting contribution 1851, at 25 [S2].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form partly present (concept systems [S1, p. 521]); circle partly present [S1, p. 519].

## Open questions

- Whether the Thesis column states his own view; Riemann's letters.

## Research log

- 2026-10-02: Read MacTutor and the 1892 Werke on the Internet Archive (Toronto scan); checked pp. 518, 519, 521, 541, 557 and 558 on the page images (n-index = page + 15).
