---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch G)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to ancient. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch G, order P32: F 5, rank 38). Basics from Britannica (Deakin) and MacTutor (O'Connor and Robertson). All her works are lost (S1, S2); her Neoplatonism is known only from later reports, which are reported speech (§7, P42). Not a scientist under P30: no original result is known (S2). Birth year disputed (c. 355 vs c. 370). Undated works (P39). primary_system BELOW_THRESHOLD (candidate PLATO, as Neoplatonism); A BELOW_THRESHOLD; B, C, D, E UNKNOWN; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #38, F5 rank 38). Needs: A BELOW_THRESHOLD; B UNKNOWN; 2 sources. Re-opened Britannica Deakin via Wayback (S1) and MacTutor (S2). New: Socrates Scholasticus HE 7.15 NPNF (S4); Synesius Ep. 15 Fitzgerald via Livius (S5) — his words, not hers; Suda On Line upsilon 166 (S6) for lost-work titles and Damascius/Hesychius testimonia. P47 source_quality on every source. Sparse own words / ancient testimonia: no letter or treatise of hers survives; Synesius's seven letters are to her; Neoplatonism and 'the One' remain reported speech / reference paraphrase (P42). MacTutor's pairing with Iamblichus is not followed: Socrates names Plato and Plotinus only; later scholarship stresses a Plotinian (not Iamblichean) line. Not a scientist under P30; no nature statement in her voice (P16). A stays BELOW_THRESHOLD; B stays UNKNOWN. Chart: still unplotted. No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: hypatia
  display_name: "Hypatia"
  roster:
    canonical_name: "Hypatia"
    rank: 38
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: mathematics
    field_bucket: mathematics
  full_name: {value: "Hypatia of Alexandria", certainty: 0.7, cites: [{source: S2, locator: "Biography, first sentence"}, {source: S6, locator: "SOL upsilon 166 (born and educated in Alexandria)"}], how_known: "MacTutor; Suda."}
  native_name: {value: "Ὑπατία (Hypatia)", certainty: 0.7, cites: [{source: S6, locator: "SOL headword *(upati/a / Hypatia)"}], how_known: "Standard Greek form in the Suda headword."}
  aliases:
    - {name: "Hypatia of Alexandria", kind: "other"}

basics:
  birth:
    date:
      value: "355"
      approx: true
      calendar: julian
      certainty: 0.5
      cites: [{source: S1, locator: "opening ('c. 355 ce')"}]
      how_known: "Real dispute (P25): Britannica (Deakin) c. 355; MacTutor about 370; Suda floruit under Arcadius only."
      alternatives:
        - {value: "370", cites: [{source: S2, locator: "Quick Info ('Born about 370')"}], note: "MacTutor (1999); Britannica's later article (Deakin) prefers c. 355."}
    place: {value: "Alexandria, Egypt", modern_name: "Alexandria, Egypt", polity_then: "Roman Empire (Egypt)", certainty: 0.7, cites: [{source: S2, locator: "Quick Info"}, {source: S6, locator: "SOL ('born and raised and educated in Alexandria')"}], how_known: "MacTutor Quick Info; Suda."}
  death:
    date: {value: "0415-03", calendar: julian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Quick Info"}, {source: S4, locator: "HE 7.15 (March, Lent, fourth year of Cyril)"}], how_known: "Britannica, MacTutor, and Socrates agree on March 415."}
    place: {value: "Alexandria, Egypt", modern_name: "Alexandria, Egypt", polity_then: "Roman Empire (Egypt)", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Quick Info"}, {source: S4, locator: "HE 7.15"}], how_known: "All agree."}
  first_lasting_contribution_year: {value: UNKNOWN, how_known: "No listed contribution can be dated (P39); commentaries and tables are undated."}
  era_bucket: {value: "-500 to 499", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Quick Info"}, {source: S4, locator: "HE 7.15 (death 415)"}], how_known: "Every adult year on either birth date (c. 355 or c. 370) to 415 falls in '-500 to 499' (P39)."}
  region_of_birth: {value: "Middle East and North Africa", certainty: 0.7, cites: [{source: S2, locator: "Quick Info"}, {source: S6, locator: "SOL"}], how_known: "Egypt (P3); Alexandria (MacTutor + Suda)."}
  region_of_work: {value: "Middle East and North Africa", certainty: 1.0, cites: [{source: S1, locator: "text"}, {source: S2, locator: "Biography"}, {source: S4, locator: "HE 7.15"}], how_known: "Alexandria, all sources."}
  sex_as_recorded: {value: "female", certainty: 1.0, cites: [{source: S1, locator: "text"}, {source: S2, locator: "Biography"}, {source: S4, locator: "HE 7.15 ('woman at Alexandria')"}], how_known: "All sources."}
  languages_of_work: {value: [Greek], certainty: 0.7, cites: [{source: S1, locator: "text ('the Greek mathematical and astronomical heritage')"}, {source: S6, locator: "SOL (Plato, Aristotle, mathematical titles in Greek tradition)"}], how_known: "Greek mathematical heritage; Suda titles and Damascius report of lecturing on Plato and Aristotle."}
  occupations: {value: ["mathematician", "astronomer", "philosopher", "teacher"], certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Biography"}, {source: S4, locator: "HE 7.15"}, {source: S6, locator: "SOL"}], how_known: "Britannica, MacTutor, Socrates, Suda."}

contribution:
  era_bucket: ancient
  fields: {value: ["mathematics", "astronomy", "philosophy"], certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Biography"}, {source: S6, locator: "SOL (commentaries; Plato/Aristotle teaching)"}], how_known: "All major sources."}
  lasting_original_contributions:
    - {value: "Commentaries on Apollonius's Conics and Diophantus's Arithmetica, and an Astronomical Canon / table (all lost as independent texts)", kind: work, lasting: "attempts to reconstruct aspects of them (S1); Deakin via MacTutor: excellent compiler, editor and preserver (S2); Suda lists the three titles (S6)", certainty: 0.7, cites: [{source: S1, locator: "text, third paragraph"}, {source: S2, locator: "Biography (Suidas)"}, {source: S6, locator: "SOL upsilon 166 (Diophantos; Astronomical Canon; Conics of Apollonios)"}], how_known: "Britannica and MacTutor report the Suda attribution; Suda text checked this pass. Undated (P39). No evidence of original mathematical research (S2)."}
    - {value: "Assisted Theon's commentary on the Almagest and edition of Euclid's Elements", kind: work, lasting: "Theon's Elements 'became the basis for all later editions' (S2)", certainty: 0.5, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor: 'It is also thought'; one source, hedged (0.5). Undated."}
  evidence_of_impact:
    - {value: "Head of a Platonist / Plotinian teaching circle at Alexandria; later a symbol of learning", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S2, locator: "Biography"}, {source: S4, locator: "HE 7.15 ('succeeded to the school of Plato and Plotinus')"}], how_known: "Socrates; Britannica; MacTutor dates the headship to about 400."}
    - {value: "Synesius of Cyrene (later bishop of Ptolemais) was her pupil and correspondent", kind: "assessment by a later major figure", certainty: 1.0, cites: [{source: S1, locator: "text"}, {source: S2, locator: "Biography"}, {source: S5, locator: "Ep. 15 address / Livius note"}], how_known: "Britannica, MacTutor; surviving Synesius letters to her."}
  major_works: []
  honours: []
  definition_fit: {value: "arguable", rationale: "Leading mathematician of her time (S1), but 'no evidence that Hypatia undertook original mathematical research' (S2) and all independent work is lost (S1, S6).", certainty: 0.5, cites: [{source: S1, locator: "text"}, {source: S2, locator: "Biography"}], how_known: "Coder's reading; the sources differ in emphasis."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Adult sources treat her as a pagan philosopher (S1: Neoplatonism seen as 'pagan'); household cult practice and mother's affiliation are not documented. Mother never named (S1, S2, S6)."}
  family_religious_practice: {value: UNKNOWN, how_known: "Nothing on household rites or attendance."}
  parents_and_household:
    - {value: "Father Theon of Alexandria, mathematician and astronomer (last attested member of the Alexandrian Museum / Mouseion tradition)", role: parents, certainty: 1.0, cites: [{source: S1, locator: "text"}, {source: S2, locator: "Biography"}, {source: S4, locator: "HE 7.15 ('daughter of the philosopher Theon')"}, {source: S6, locator: "SOL ('daughter of Theon the geometer')"}], how_known: "All major sources."}
  household_circumstances: {value: "Scholarly mathematical household in Alexandria; Theon edited Euclid and commented on Ptolemy", certainty: 0.7, cites: [{source: S1, locator: "text (Theon; Museum)"}, {source: S2, locator: "Biography"}], how_known: "Britannica and MacTutor on Theon's program."}
  schooling: []
  early_mathematics: {value: "geometry (Euclid-style proof)", certainty: 0.5, cites: [{source: S2, locator: "Biography ('fairly certain that she studied mathematics under ... her father')"}, {source: S1, locator: "text (Theon's Euclid / Ptolemy program)"}], how_known: "MacTutor, hedged; father's Euclid edition is the natural early exposure."}
  early_geometric_style_reasoning: {value: "Exposed via Theon's Euclid edition and the family's mathematical program (inferred; not a dated childhood episode)", certainty: 0.5, cites: [{source: S1, locator: "text"}, {source: S2, locator: "Biography"}], how_known: "Inferred from Theon's work and MacTutor's study-under-father claim."}
  early_science_exposure:
    - {value: "Raised in Theon's mathematical and astronomical teaching household in Alexandria", certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S2, locator: "Biography"}, {source: S6, locator: "SOL"}], how_known: "Britannica, MacTutor, Suda."}
  key_early_reading: []
  childhood_mentors:
    - {value: "Theon of Alexandria (father)", certainty: 0.5, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor, hedged."}
  languages_in_childhood: {value: [Greek], certainty: 0.5, cites: [{source: S1, locator: "text"}, {source: S6, locator: "SOL (Alexandria)"}], how_known: "Inferred for a Greek-speaking Alexandrian scholarly household."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: UNKNOWN, how_known: "No dated work (P39); headship c. 400–415 is institutional, not a dated composition span."}
  nominal_affiliations:
    - {value: "Platonist / Plotinian teaching circle at Alexandria (reported headship)", role: other, certainty: 0.7, cites: [{source: S2, locator: "Biography ('head of the Platonist school… about 400')"}, {source: S4, locator: "HE 7.15 ('succeeded to the school of Plato and Plotinus')"}], how_known: "Socrates and MacTutor; affiliation/role, not a scored profession of belief."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No writing of hers survives (S1, S2, S6). Synesius's letters are his words (S5)."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "Socrates reports she succeeded to the school of Plato and Plotinus (S4); Britannica: her philosophy was Neoplatonist, concerned with the approach to the One (S1); MacTutor adds Iamblichus (S2) — that pairing is not followed here (Socrates names Plotinus only). No text of hers survives: later report and reference paraphrase cannot score alone (§7, P42). Candidate PLATO (Neoplatonism; no separate code).", note: "Would be PLATO at low certainty if a scholarly reconstruction of her Plotinian teaching were taken under P49; deepen leaves the axis/system at BELOW because the Cambridge-style caution (Socrates alone for 'from Plotinus'; Synesius→teacher inference) still applies and no own words exist."}
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: PLATO, reason: "Socrates: school of Plato and Plotinus (S4); Britannica Neoplatonism / approach to the One (S1). No separate Neoplatonism code; PLATO is the nearest. Report only — not coded as primary_system.", cites: [{source: S4, locator: "HE 7.15"}, {source: S1, locator: "text ('Neoplatonist'; 'the One')"}]}
    - {code: HELLEN, reason: "Rejected: modern reconstructionist code; not for ancient pagans by default.", cites: [{source: S1, locator: "text"}]}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "Britannica describes her Neoplatonism as 'concerned with the approach to the One, an underlying reality' (S1) — reference paraphrase of a reported doctrine, not her own words (P42). Socrates places her in the school of Plato and Plotinus without stating a locus in her voice (S4). Named alternative: A pointing to a non-personal One @ ≤0.5 under P49 if a monograph reconstruction were locked as scholarly_reconstruction; deepen does not lift.", note: "Would point to a non-personal One if her own text existed."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist under P30 (no known original mathematical or physical result; S2: 'no evidence that Hypatia undertook original mathematical research'; commentaries/editorial work on Euclid, Apollonius, Diophantus, Ptolemy). No statement on nature survives in her voice (P16). Synesius Ep. 15 (hydroscope) is his request and description, not hers (S5). Researched silent (P19) — not BELOW_THRESHOLD."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing of hers survives."}
    D_authority: {value: UNKNOWN, how_known: "Nothing of hers survives."}
    E_scope: {value: UNKNOWN, how_known: "Nothing of hers survives (P7)."}
  mid_basin: {value: UNKNOWN, how_known: "B_cause is UNKNOWN, which takes precedence (§6, P19)."}
  statements:
    - text: "Having succeeded to the school of Plato and Plotinus, she explained the principles of philosophy to her auditors, many of whom came from a distance to receive her instructions."
      cites: [{source: S4, locator: "HE 7.15 (NPNF)"}]
      date: "400"
      context: "Socrates Scholasticus, Ecclesiastical History 7.15 — contemporary Christian historian on Hypatia's teaching succession. Reported speech about her school, not a profession in her voice. Context only; not used to score."
      axes: [A_locus]
      kind: "reported speech"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "NPNF English via New Advent / earlychurchtexts this pass. Date '400' is conventional for the reported headship (MacTutor c. 400), not a dated composition of hers. P42: scores nothing."
  changes_over_life: []
  coder_notes: "Deepen D1: sparse own words / ancient testimonia. Synesius's seven letters to Hypatia survive; none from her (S2, S5). Socrates HE 7.15 is the best near-contemporary narrative (S4). Suda preserves Hesychius/Damascius material and the lost-work titles (S6). MacTutor's Iamblichus claim (S2) is set aside against Socrates' Plato-and-Plotinus wording. Nothing scores under P42. A BELOW_THRESHOLD; B UNKNOWN. Chart unplotted."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Greek-speaking Alexandrian", certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S6, locator: "SOL (Alexandria)"}], how_known: "Britannica + Suda."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Adult pagan philosophical identity is reported (S1); birth-household religion and any initiation are not documented. Heritage only — never a worldview code."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "No Christian baptism attested; pagan initiation not documented."}
  childhood_catechism: {value: UNKNOWN, how_known: "Nothing."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: UNKNOWN, how_known: "No dated work (P39)."}
  age_at_first_lasting_contribution: {value: UNKNOWN, how_known: "No dated work (P39)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "Nothing of hers survives; Socrates/Britannica reports are not her words."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S1, locator: "text"}, {source: S4, locator: "HE 7.15"}], how_known: "Nothing scores under P42."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Nothing of hers survives."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "Commentary on Apollonius's Conics; Euclid program with Theon (S1, S2, S6).", certainty: 0.5, cites: [{source: S1, locator: "text"}, {source: S6, locator: "SOL (Conics)"}], how_known: "Coder's reading of attributed mathematical work."}
  form_acquired: {value: "childhood or adolescence", certainty: 0.5, cites: [{source: S2, locator: "Biography"}], how_known: "Taught by her father (hedged)."}
  circle_present: {value: "unclear", rationale: "Reported Plotinian Neoplatonism only; no text of hers for circle geometry as belief (S1, S4).", certainty: 0.5, cites: [{source: S1, locator: "text"}, {source: S4, locator: "HE 7.15"}], how_known: "Coder's reading."}
  reading: "No reading possible as finding: no text of hers survives. As belief model only: geometry present in attributed work; circle unclear; H1 not tested. Worldview unplottable (A BELOW; B UNKNOWN)."
  notes: "P42 ancient-testimonia case (with Homer / Hippocrates)."

institutions:
  - {value: "Platonist school at Alexandria", role: head, years: "c. 400–415", kind: "other", certainty: 0.5, cites: [{source: S2, locator: "Biography"}, {source: S4, locator: "HE 7.15"}], how_known: "MacTutor 'in about 400 AD'; Socrates succession wording."}
collaborators:
  - {value: "Theon of Alexandria", relation: family, note: "father; joint work on Ptolemy and Euclid (hedged)", certainty: 0.5, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor."}
  - {value: "Synesius of Cyrene", relation: "student or assistant", note: "pupil and correspondent; seven letters of his to her survive", certainty: 1.0, cites: [{source: S1, locator: "text"}, {source: S2, locator: "Biography"}, {source: S5, locator: "Ep. 15"}], how_known: "Britannica, MacTutor, Synesius corpus."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 38"}], how_known: "Study roster."}
  controversies:
    - {value: "Birth year c. 355 vs c. 370; how much original work is hers vs editorial/commentary; Plotinian vs (outdated) Iamblichean framing; Cyril's responsibility for the murder", certainty: 0.7, cites: [{source: S1, locator: "opening; text"}, {source: S2, locator: "Quick Info; Biography"}, {source: S4, locator: "HE 7.15"}, {source: S6, locator: "SOL (Cyril vs Alexandrian insolence)"}], how_known: "Sources differ."}
  data_quality_flags:
    - "No writing of hers survives; Synesius letters are his words (S5)."
    - "P42: Socrates, Suda/Damascius, and Britannica Neoplatonism paraphrase cannot score axes alone."
    - "MacTutor pairs her teaching with Iamblichus (S2); Socrates names Plato and Plotinus only (S4) — Iamblichus not followed."
  open_questions:
    - "Page-check Watts, Hypatia (OUP 2017) and City and School (2006/2008) for the Plotinian-not-Iamblichean reconstruction and any passage that would meet P49 scholarly_reconstruction for A."
    - "Page-check Dzielska, Hypatia of Alexandria (Harvard 1995) for Synesius-derived teaching content vs her own voice."
    - "Cameron on the Almagest Book III title / possible Diophantus interpolations — still editorial, not a B-scoring nature result."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Michael Deakin"
    citation: "Deakin, Michael. \"Hypatia.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Hypatia."
    url: "https://www.britannica.com/biography/Hypatia"
    accessed: 2026-10-24
    reliability_note: "Signed article body by the author of Hypatia of Alexandria: Mathematician and Martyr; Top Questions box not used. Live page JS-walled this pass; full text from Wayback capture."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, collaborators, review]
  - id: S2
    type: secondary
    kind: encyclopedia
    author: "J. J. O'Connor and E. F. Robertson"
    year: 1999
    citation: "O'Connor, J. J., and E. F. Robertson. \"Hypatia of Alexandria.\" MacTutor History of Mathematics, University of St Andrews, last update April 1999. https://mathshistory.st-andrews.ac.uk/Biographies/Hypatia/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Hypatia/"
    accessed: 2026-10-24
    reliability_note: "Signed biography. Useful on mathematics and Synesius; the claim that she based teaching on Plotinus and Iamblichus is not followed for coding (conflicts with Socrates HE 7.15 naming Plato and Plotinus only)."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, lane_b, institutions, collaborators, review]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S4
    type: primary
    kind: other
    author: "Socrates Scholasticus (Socrates of Constantinople); NPNF translation"
    year: 440
    citation: "Socrates Scholasticus. Ecclesiastical History 7.15. Trans. in Nicene and Post-Nicene Fathers (NPNF). English via New Advent / earlychurchtexts.com this pass."
    url: "https://www.newadvent.org/fathers/26017.htm"
    accessed: 2026-10-24
    reliability_note: "Near-contemporary Christian church history (written within decades of 415). Best narrative source for her public role and murder; the Plato-and-Plotinus succession is his report, not her words (P42)."
    source_quality: "unofficial web copy"
    used_for: [basics, contribution, worldview, timing, lane_b, institutions, collaborators, review]
  - id: S5
    type: primary
    kind: letter
    author: "Synesius of Cyrene; trans. A. Fitzgerald (improved Livius text)"
    year: 402
    citation: "Synesius of Cyrene. Letter 15 (to Hypatia), on a hydroscope/densimeter. Trans. A. Fitzgerald, Livius.org improved text. https://www.livius.org/sources/content/synesius/synesius-letter-015/."
    url: "https://www.livius.org/sources/content/synesius/synesius-letter-015/"
    accessed: 2026-10-24
    reliability_note: "Primary letter of her pupil; his words and instrument description, not hers. Used to document the correspondence and that no reply of hers survives. Livius notes letters 10, 16, 33, 81, 124, 154 also to her."
    source_quality: "unofficial web copy"
    used_for: [contribution, worldview, collaborators, review]
  - id: S6
    type: secondary
    kind: encyclopedia
    author: "Suda (Byzantine encyclopedia); Suda On Line translation (upsilon 166)"
    year: 1000
    citation: "Suda On Line, Adler upsilon 166 \"Hypatia\" (trans. and vetted SOL entry; incorporates Hesychius and Damascius Life of Isidore material). https://www.cs.uky.edu/~raphael/sol/sol-entries/upsilon/166."
    url: "https://www.cs.uky.edu/~raphael/sol/sol-entries/upsilon/166"
    accessed: 2026-10-24
    reliability_note: "Medieval compilation; high-vetted SOL English. Primary for the traditional work titles (Diophantus, Astronomical Canon, Apollonius Conics) and Damascius anecdotes; not her own voice. 'Wife of Isidore' line is chronologically impossible and set aside."
    source_quality: "scholarly edition or monograph"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, lane_b, review]
---

# Hypatia

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Hypatia of Alexandria (c. 355 or c. 370–415), mathematician, astronomer and teacher in a Platonist circle [S1, S2, S4]. All her independent works are lost; no letter of hers survives [S1, S2, S5, S6]. Deepen D1: primary_system and A BELOW_THRESHOLD; B, C, D, E UNKNOWN; mid_basin UNKNOWN. Chart still unplotted.

## Life and work

Daughter of Theon; taught philosophy and mathematics at Alexandria; murdered by a Christian mob in March 415 [S1, S2, S4]. Socrates says she succeeded to the school of Plato and Plotinus [S4]. Synesius of Cyrene, later a bishop, was her pupil; seven of his letters to her survive, none from her [S2, S5].

## Contribution and impact

Suda attributes commentaries on Diophantus and Apollonius's Conics and an Astronomical Canon — all lost as independent texts [S1, S2, S6]. MacTutor: no evidence of original mathematical research; compiler/editor/preserver [S2]. Assisted Theon's Euclid/Ptolemy program (hedged) [S2].

## Childhood and education

Raised in Theon's Alexandrian mathematical household; probably studied under him [S1, S2, S6]. Mother unknown. Family religion and household cult practice not documented.

## Adult working worldview

**Lane A.** Reported Neoplatonism / approach to the One [S1] and Socrates' Plato-and-Plotinus succession [S4] are later report and reference paraphrase — not her own words (P42). A BELOW_THRESHOLD.

**Lane B (separate).** Not a scientist under P30; no nature statement in her voice. Synesius Ep. 15 (hydroscope) is his words [S5]. B UNKNOWN.

## Heritage (context only)

Greek-speaking Alexandria [S1, S6]. Adult pagan philosophical identity reported; birth-household religion UNKNOWN.

## Timing

No dated work (P39) [S1, S2].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Geometry present in attributed work; circle unclear [S1, S4, S6]. H1 not tested.

## Open questions

- Watts OUP 2017 / City and School page-check for P49 A reconstruction.
- Dzielska 1995 page-check.
- Cameron on Almagest / Diophantus interpolations (editorial, not B).

## Research log

- 2026-10-15: Read Britannica (Deakin) and MacTutor.
- 2026-10-24 (D1): Britannica via Wayback; MacTutor re-read; Socrates HE 7.15 NPNF; Synesius Ep. 15 Livius/Fitzgerald; Suda On Line upsilon 166. P42 reaffirmed. A BELOW→BELOW; B UNKNOWN→UNKNOWN. Chart-moving no.
