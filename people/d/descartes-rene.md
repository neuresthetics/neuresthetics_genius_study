---
record:
  record_type: person
  schema_version: "1.2"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (executor agent for v8, RUNBOOK stage 3, batch A: early modern philosophers)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (stage 3, batch A). Basics from SEP 'René Descartes' (Hatfield) and Britannica (Watson, first page); physics from SEP 'Descartes' Physics' (Slowik). Worldview from the Discourse (Veitch), the Principles (Veitch's selections) and the Meditations (Molyneux 1680), all read in Project Gutenberg texts, so capped at 0.7 (CODING_GUIDE §7). DRAFT SCORES for v8's review: primary_system CLASS_THEISM 0.5; A 1, B 3, D 1, E 3 at 0.7; C 1 at 0.5; mid_basin true (0.7). Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit fixes, stage 3 batch A (two blind runs at 59a8371). #94: native_name 'René Descartes' (French), 'Renatus Cartesius' dropped. #123: early_mathematics 'other' (curriculum only; no source says advanced). #132: primary_system rationale now quotes the CLASS_THEISM tests and cites Principles I.14–15 (idea of God) and Discourse IV for the attributes; value unchanged. #138: conservation passage is Principles II.42 (SEP physics §4 prints 'Pr II 62'; §6 has II 42). #141: the named alternative score is now in the E rationale; rational soul quoted from Discourse V. #156: first_evidence wording now the 1629 'foundation of physics' letter (AT 1:144); 'all the principles of my physics' is a later letter about the Meditations (AT 3:233). #157, #161, #168: locators and coder note corrected. S5 note lists the parts in the selection. Not reviewed."}

identity:
  id: descartes-rene
  display_name: "René Descartes"
  roster:
    canonical_name: "René Descartes"
    rank: 68
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: philosophy
    field_bucket: philosophy
  full_name: {value: "René Descartes", certainty: 1.0, cites: [{source: S1, locator: "§1.1"}, {source: S2, locator: "opening"}], how_known: "Two sources."}
  native_name: {value: "René Descartes", certainty: 1.0, cites: [{source: S1, locator: "§1.1 (signed 'du Perron')"}, {source: S2, locator: "opening"}], how_known: "French form, as both sources give it. A Latin form of the name is not given in any source read, so none is recorded (lens audit #94: 'Renatus Cartesius' and the title-page claim had no source and were removed)."}
  aliases:
    - {name: "Descartes-René", kind: "roster alias"}
    - {name: "Rene Descartes", kind: "roster alias"}
    - {name: "René-Descartes", kind: "roster alias"}
    - {name: "sieur du Perron", kind: "title or honorific"}

basics:
  birth:
    date: {value: "1596-03-31", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "§1.1"}, {source: S2, locator: "opening"}], how_known: "Two sources agree."}
    place: {value: "La Haye, Touraine (now Descartes)", modern_name: "Descartes, Indre-et-Loire, France", polity_then: "Kingdom of France", certainty: 1.0, cites: [{source: S1, locator: "§1.1"}, {source: S2, locator: "opening; 'Early life and education'"}], how_known: "Two sources agree; the town has been renamed Descartes."}
  death:
    date: {value: "1650-02-11", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "§1.5"}, {source: S2, locator: "opening"}], how_known: "Two sources agree."}
    place: {value: "Stockholm", modern_name: "Stockholm, Sweden", polity_then: "Kingdom of Sweden", certainty: 1.0, cites: [{source: S2, locator: "opening"}, {source: S1, locator: "§1.5 (court of Queen Christina)"}], how_known: "Britannica names Stockholm; SEP places his death at Queen Christina's court."}
  first_lasting_contribution_year: {value: 1637, certainty: 0.7, cites: [{source: S1, locator: "§1.2; §1.3"}, {source: S2, locator: "'Early life and education' (1619)"}], how_known: "Year the Geometry (analytic geometry) was published with the Discourse. The discovery itself is dated 1619 by Britannica and 'certainly by 1628' by SEP; all three years give the same era bucket."}
  era_bucket: {value: "1600 to 1749", certainty: 1.0, cites: [{source: S1, locator: "§1.2–1.3"}], how_known: "From first_lasting_contribution_year (P2); 1619, 1628 and 1637 fall in the same bucket."}
  region_of_birth: {value: "Western Europe", certainty: 1.0, cites: [{source: S1, locator: "§1.1"}], how_known: "France is Western Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Western Europe", certainty: 1.0, cites: [{source: S1, locator: "§1.2 ('He moved to the Dutch Netherlands')"}, {source: S2, locator: "'22 years in the Netherlands'"}], how_known: "Paris and, from 1628/29 to 1649, the Netherlands (both Western Europe); Sweden only in his last months."}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S1, locator: "§1.1"}], how_known: "As the sources record it."}
  languages_of_work: {value: [French, Latin], certainty: 1.0, cites: [{source: S1, locator: "§1 (Discourse in French, 1637; Meditations in Latin, 1641; Principles in Latin, 1644)"}], how_known: "SEP lists the language of each major work."}
  occupations: {value: [philosopher, mathematician, "natural philosopher", "gentleman soldier"], certainty: 1.0, cites: [{source: S1, locator: "opening; §1.1"}, {source: S2, locator: "opening"}], how_known: "Two sources."}

contribution:
  fields: {value: [mathematics, metaphysics, "natural philosophy", epistemology], certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "opening"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Analytic (algebraic) geometry: describing curves by equations relative to coordinate lines ('Cartesian coordinates')", year: "1637", kind: method, lasting: "standard mathematics", certainty: 1.0, cites: [{source: S1, locator: "§1.2"}, {source: S2, locator: "'Early life and education' (1619)"}], how_known: "Two sources; the date of discovery differs (see first_lasting_contribution_year)."}
    - {value: "Method of doubt and the cogito as a foundation for knowledge; mind–body dualism", year: "1637–1641", kind: "concept or term", lasting: "starting point of modern philosophy; the mind–body problem", certainty: 1.0, cites: [{source: S2, locator: "opening"}, {source: S1, locator: "§7"}], how_known: "Two sources."}
    - {value: "Laws of nature (inertial motion in straight lines) and a conservation principle of quantity of motion", year: "1644", kind: "law or principle", lasting: "model for Newton's first law", certainty: 0.7, cites: [{source: S3, locator: "opening; §4"}], how_known: "SEP 'Descartes' Physics'."}
  evidence_of_impact:
    - {value: "Generally regarded as the founder of modern philosophy", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S2, locator: "opening"}], how_known: "Britannica."}
    - {value: "Cartesian coordinates named after him", kind: "named after them", certainty: 1.0, cites: [{source: S1, locator: "§1.2"}], how_known: "SEP."}
  major_works:
    - {value: "Discourse on the Method, with the Dioptrics, Meteorology and Geometry", year: 1637, kind: book, certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S4, locator: "title"}], how_known: "SEP and the text."}
    - {value: "Meditations on First Philosophy, with Objections and Replies", year: 1641, kind: book, certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S6, locator: "title page"}], how_known: "SEP and the text."}
    - {value: "Principles of Philosophy", year: 1644, kind: book, certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S5, locator: "title"}], how_known: "SEP and the text."}
    - {value: "Passions of the Soul", year: 1649, kind: book, certainty: 1.0, cites: [{source: S1, locator: "§1; §1.5"}], how_known: "SEP."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Analytic geometry and the foundations of modern philosophy.", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "opening"}], how_known: "Sources agree."}

childhood:
  family_religion: {value: "Roman Catholic", certainty: 1.0, cites: [{source: S2, locator: "'Early life and education'"}, {source: S1, locator: "§1.1 ('Descartes, a Roman Catholic')"}], how_known: "Two sources."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father, Joachim, a lawyer and councillor in the Parlement of Brittany at Rennes", name: "Joachim Descartes", role: father, certainty: 1.0, cites: [{source: S1, locator: "§1.1"}, {source: S2, locator: "'Early life and education'"}], how_known: "Two sources."}
    - {value: "Mother, Jeanne Brochard, died in childbirth when he was thirteen and a half months old", name: "Jeanne Brochard", role: mother, certainty: 1.0, cites: [{source: S1, locator: "§1.1"}, {source: S2, locator: "'Early life and education' ('when he was one year old')"}], how_known: "Two sources."}
  household_circumstances: {value: "Raised first by his maternal grandmother at La Haye, then probably by a great-uncle at Châtellerault; family of lawyers with minor nobility", certainty: 0.7, cites: [{source: S1, locator: "§1.1 ('It is likely')"}, {source: S2, locator: "'Early life and education'"}], how_known: "Two sources; SEP hedges the move."}
  schooling:
    - {value: "Jesuit College of La Flèche: grammar school, then three years of Aristotelian philosophy, with mathematics in the final three years", stage: "religious school", years: "1606/1607–1614/1615", certainty: 0.7, cites: [{source: S1, locator: "§1.1"}, {source: S2, locator: "'Early life and education' (1606)"}], how_known: "Two sources; SEP gives 1606 or 1607, Britannica 1606."}
    - {value: "University of Poitiers, law degree", stage: university, years: "1614–1616", certainty: 1.0, cites: [{source: S1, locator: "§1.1"}, {source: S2, locator: "'Early life and education'"}], how_known: "Two sources."}
  early_mathematics: {value: "other", note: "Mathematics in the final three years at La Flèche: 'The Jesuits also included mathematics in the final three years' (SEP); the level he reached is not stated.", certainty: 0.7, cites: [{source: S1, locator: "§1.1"}], how_known: "SEP only; it describes the curriculum, not his attainment, so the value is 'other' with the curriculum as description (as in the Bohr record), not a level (lens audit #123)."}
  early_geometric_style_reasoning: {value: "Jesuit curriculum in logic and mathematics; he later wrote that he was 'especially delighted with the mathematics, on account of the certitude and evidence of their reasonings'", certainty: 0.7, cites: [{source: S1, locator: "§1.1"}, {source: S4, locator: "Part I"}], how_known: "SEP on the curriculum; his own later account (Discourse, Part I) of his school years."}
  early_science_exposure:
    - {value: "Galileo's discovery of the moons of Jupiter celebrated at La Flèche", year: "1610", age: 14, certainty: 0.7, cites: [{source: S1, locator: "§1.1"}], how_known: "SEP."}
  key_early_reading:
    - {value: "Aristotle through scholastic textbooks and commentaries; Cicero", certainty: 0.7, cites: [{source: S1, locator: "§1.1"}], how_known: "SEP on the curriculum."}
  childhood_mentors: []
  languages_in_childhood: {value: [French, Latin], certainty: 0.7, cites: [{source: S1, locator: "§1.1 (Latin and Greek grammar)"}], how_known: "French home; Latin at school."}
  notable_events:
    - {value: "Took part in the ceremony placing Henry IV's heart in the La Flèche cathedral", year: "1610", age: 14, certainty: 0.7, cites: [{source: S2, locator: "'Early life and education'"}], how_known: "Britannica."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1618–1650", certainty: 1.0, cites: [{source: S1, locator: "§1.2–1.5"}], how_known: "From the Beeckman years to his death."}
  nominal_affiliations:
    - {value: "Roman Catholic", certainty: 1.0, cites: [{source: S1, locator: "§1.1; §1.5"}], how_known: "SEP, twice."}
  self_described_science_religion_relation:
    value: "Revealed theology is above reason and he did not 'presume to subject them to the impotency of my reason' (Discourse I); where reason and revelation seem to conflict, 'what God has revealed is incomparably more certain than anything else', but 'in things regarding which there is no revelation' a philosopher accepts only what he has ascertained (Principles I.76). God established laws in nature that 'are accurately observed in all that exists or takes place in the world' (Discourse V)."
    certainty: 0.7
    cites: [{source: S4, locator: "Part I; Part V"}, {source: S5, locator: "Part I, §76"}]
    how_known: "His own published works, read in unofficial web copies of Veitch's translations; capped at 0.7 (CODING_GUIDE §7)."
  primary_system:
    value: CLASS_THEISM
    basis: written_profession
    certainty: 0.5
    cites: [{source: S6, locator: "Meditation III"}, {source: S5, locator: "Part I, §§14–15; §76"}, {source: S4, locator: "Part IV; Part V"}, {source: S1, locator: "§1.5"}]
    how_known: "His own published works. Below the 0.7 that the text alone would allow, because the fit to the code is partial (see rationale) and two alternatives are named."
    rationale: "DRAFT, judgment call. The CLASS_THEISM use_when tests, as written, are only partly met in his own words. (1) 'argues to God from the world by reason (first cause, necessary existent, prime mover)': partly. He argues to God by reason, but from the idea of God rather than from the world: the idea of an 'all-perfect Being' (Principles I.14) does not represent 'a chimera, but a true and immutable nature' (Principles I.15; Meditation III). (2) 'holds God simple, immutable or impassible': met; God is 'infinite, eternal, immutable, omniscient, all-powerful' (Discourse IV). (3) 'treats nature as an order of secondary causes': partly; nature is an order of laws that God established and sustains by his 'concurrence' (Discourse V). But the code's label is Aristotelian-Thomistic-Falsafa and Descartes rejected scholastic Aristotelianism (S2, opening), so the fit is to the rational God, not the tradition; hence 0.5. Named alternatives: CHRIST (Catholic, and he submits to revelation, Principles I.76) and DEISM (Hatfield: his metaphysical God is 'nondenominational, tending toward the deistic', S1 §1.5). DEISM is ruled out by its own do_not_use_when (he accepts revelation). RATN (stub) is the epistemological label Britannica uses ('Descartes’s metaphysics is rationalist'), but it names a method, not a God-world metaphysics."
  secondary_system: {value: UNKNOWN, how_known: "No second system: he kept faith doctrines (the Trinity) apart from his claims about God from reason (S1 §1.5) but did not publish a second system."}
  candidate_codes_considered:
    - {code: CLASS_THEISM, reason: "Coded (DRAFT, 0.5): God known by reason, immutable, sustaining a lawful nature. Partial fit: not Aristotelian. CLASS_THEISM is a sourced draft system file.", cites: [{source: S6, locator: "Meditation III"}, {source: S4, locator: "Part V"}]}
    - {code: CHRIST, reason: "Named alternative: Roman Catholic; 'I revered our theology, and aspired as much as any one to reach heaven' (Discourse I); revelation outranks reason (Principles I.76). Not coded because his published work develops the God of reason, not doctrine; CHRIST's own guidance sends a classical God of reason to CLASS_THEISM.", cites: [{source: S4, locator: "Part I"}, {source: S5, locator: "Part I, §76"}]}
    - {code: DEISM, reason: "Named alternative (Hatfield, S1 §1.5: 'tending toward the deistic'). Rejected: DEISM requires rejecting revelation, and he accepts it (Principles I.76).", cites: [{source: S1, locator: "§1.5"}]}
    - {code: RATN, reason: "Considered: a rationalist metaphysics (S2, opening). Not coded: RATN is a stub system file and names an epistemology rather than a God-world metaphysics (flag; see report method question).", cites: [{source: S2, locator: "opening"}]}
  lio_axes:
    A_locus:
      value: 1
      basis: written_profession
      certainty: 0.7
      cites: [{source: S6, locator: "Meditation III"}, {source: S4, locator: "Part V"}]
      how_known: "His own published text in an unofficial web copy; capped at 0.7 (§7). A named alternative (0)."
      rationale: "DRAFT. Leans to the transcendent-person pole: God is 'a certain Infinite Substance, Independent, Omniscient, Almighty, by whom both I my self, and every thing else that is [...] was created' (Meditation III), distinct from the extended world he creates. Not 0, because God sustains the world continuously, 'the action by which he now sustains it is the same with that by which he originally created it' (Discourse V), the same kind of immanence feature that gave Aquinas and Newton 1 (same-pattern rule). Named alternative: 0."
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.7
      cites: [{source: S4, locator: "Part V"}, {source: S3, locator: "§4 (Pr II 37; the conservation passage, labelled 'Pr II 62' there); §6 (same passage, labelled 'Pr II 42')"}, {source: S1, locator: "§1.5"}]
      how_known: "His own published text (unofficial copy, §7) and SEP; a named alternative (4)."
      rationale: "DRAFT. Scored on his account of nature (P6). Leans LIO: God established 'certain laws' in nature that 'are accurately observed in all that exists or takes place in the world' (Discourse V), and maintains the world 'by the same action and with the same laws with which He created it' (Principles II.42, quoted in S3 §4, which mislabels it 'Pr II 62'; S3 §6 gives Pr II 42). The stated, limited exception is the created human mind, which acts freely and is 'master of his own actions' (Principles I.37), outside mechanical necessity; and he does not deny miracles. Named alternative: 4, since Hatfield writes that 'If Descartes were fully consistent [...] there would be no miracles in his world' (S1 §1.5)."
    C_ledger:
      value: 1
      basis: written_profession
      certainty: 0.5
      cites: [{source: S4, locator: "Part I; Part V"}, {source: S5, locator: "Part I, §37"}]
      how_known: "His own published text, but the evidence is indirect (passing remarks, no doctrine of judgement), so 0.5, below the 0.7 the copy allows."
      rationale: "DRAFT, judgment call. Leans to personal reward and punishment: he 'aspired as much as any one to reach heaven' (Discourse I); he holds that the error of thinking animal and human souls alike leads to the view that 'after this life we have nothing to hope for or fear, more than flies and ants' (Discourse V), which implies hope and fear after death; free action 'renders him worthy of praise or blame' (Principles I.37). He gives no account of judgement, so the features are present but limited. Named alternative: BELOW_THRESHOLD, if passing remarks are judged too indirect."
    D_authority:
      value: 1
      basis: written_profession
      certainty: 0.7
      cites: [{source: S5, locator: "Part I, §76"}, {source: S4, locator: "Part I"}]
      how_known: "His own published text (unofficial copy, §7); a named alternative (2)."
      rationale: "DRAFT. Revelation outranks reason when they conflict: 'what God has revealed is incomparably more certain than anything else; and that, we ought to submit our belief to the Divine authority rather than to our own judgment, even although perhaps the light of reason should, with the greatest clearness and evidence, appear to suggest to us something contrary' (Principles I.76). A large domain is left to reason ('in things regarding which there is no revelation'). Same pattern as Aquinas (D 1: when they conflict revelation wins). Named alternative: 2, because in practice his physics is built from reason alone and revelation is silent on it."
    E_scope:
      value: 3
      basis: written_profession
      certainty: 0.7
      cites: [{source: S5, locator: "Part II, §22–23; Part III, §3"}, {source: S4, locator: "Part V"}]
      how_known: "His own published texts (unofficial copies, §7); a named alternative (4)."
      rationale: "DRAFT. Scored on the world's order (P7). Leans LIO: 'the earth and heavens are made of the same matter' and 'There is therefore but one kind of matter in the whole universe' (Principles II.22–23); animal and human bodies are machines 'made by the hands of God' (Discourse V); and the supposition that all things were made for us 'would be plainly ridiculous and inept in physical reasoning' (Principles III.3). The stated, limited exception is the human rational soul, which 'could by no means be educed from the power of matter' but 'must be expressly created' (Discourse V). No favour for a group in events in anything read. His hope of heaven is a C matter (P7). Named alternative: 4, if the rational soul is not counted as an exception to the world's order, since it concerns the human mind and grants no group any exception in events."
  mid_basin: {value: true, certainty: 0.7, cites: [{source: S6, locator: "Meditation III"}, {source: S4, locator: "Part V"}], how_known: "P4/P6 test: A_locus 1 (0.7) ≤ 1 and B_cause 3 (0.7) ≥ 3, both at ≥ 0.7, so true. Certainty is the lower of the two (0.7). DRAFT: both axes are named-alternative cases, and B scored 4 or A scored 0 would not change the result."}
  statements:
    - text: "I revered our theology, and aspired as much as any one to reach heaven: but being given assuredly to understand that the way is not less open to the most ignorant than to the most learned, and that the revealed truths which lead to heaven are above our comprehension, I did not presume to subject them to the impotency of my reason"
      cites: [{source: S4, locator: "Part I"}]
      date: "1637"
      context: "Discourse, Part I, reviewing the subjects he studied at school."
      axes: [C_ledger, D_authority]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "I have also observed certain laws established in nature by God in such a manner, and of which he has impressed on our minds such notions, that after we have reflected sufficiently upon these, we cannot doubt that they are accurately observed in all that exists or takes place in the world"
      cites: [{source: S4, locator: "Part V, opening paragraph"}]
      date: "1637"
      context: "Discourse, Part V, introducing his physics."
      axes: [B_cause, E_scope]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "But this is certain, and an opinion commonly received among theologians, that the action by which he now sustains it is the same with that by which he originally created it"
      cites: [{source: S4, locator: "Part V"}]
      date: "1637"
      context: "Discourse, Part V, on whether the world could have developed from chaos under laws."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "after this life we have nothing to hope for or fear, more than flies and ants"
      cites: [{source: S4, locator: "Part V, last paragraph"}]
      date: "1637"
      context: "The view he rejects: that animal and human souls are of one nature, from which this would follow."
      axes: [C_ledger]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "Above all, we must impress on our memory the infallible rule, that what God has revealed is incomparably more certain than anything else; and that, we ought to submit our belief to the Divine authority rather than to our own judgment, even although perhaps the light of reason should, with the greatest clearness and evidence, appear to suggest to us something contrary to what is revealed. But in things regarding which there is no revelation, it is by no means consistent with the character of a philosopher to accept as true what he has not ascertained to be such"
      cites: [{source: S5, locator: "Part I, §76"}]
      date: "1644"
      context: "Principles of Philosophy, Part I, last article."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "There is therefore but one kind of matter in the whole universe, and this we know only by its being extended."
      cites: [{source: S5, locator: "Part II, §23"}]
      date: "1644"
      context: "Principles, Part II, after §22 'that the matter of the heavens and earth is the same'."
      axes: [E_scope]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "it is yet by no means probable that all things were created for us in this way that God had no other end in their creation; and this supposition would be plainly ridiculous and inept in physical reasoning"
      cites: [{source: S5, locator: "Part III, §3"}]
      date: "1644"
      context: "Principles, Part III, §3, 'In what sense it may be said that all things were created for the sake of man'; he allows it as 'a pious thought' in morals."
      axes: [E_scope]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "By the word God, I mean a certain Infinite Substance, Independent, Omniscient, Almighty, by whom both I my self, and every thing else that is (if any thing do Actualy exist) was created."
      cites: [{source: S6, locator: "Meditation III"}]
      date: "1641"
      context: "Meditation III, the causal argument from the idea of God. Molyneux's 1680 English; the Gutenberg text marks italics with underscores, removed here; spelling as in the text."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
  changes_over_life: []
  coder_notes: "DRAFT SCORES for v8's review. All own-word evidence was read in Project Gutenberg copies (Veitch's Discourse and Principles selections; Molyneux's 1680 Meditations), unofficial web copies, so no worldview field exceeds 0.7 (§7). Veitch's Principles is a selection: Part II stops at §25, so II.37 (the first law) and II.42 (conservation) were read only as quoted in SEP 'Descartes' Physics' (S3). II.36 (God's immutability as the cause of motion) was not read; S3 does not quote it (lens audit #168). No page numbers. RATN is a stub system file (flag). The Rosicrucian and dream material (S1 §1.2; S2) is biography, not his metaphysics, and is not scored."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "French; family of lawyers with minor nobility from Poitou and Touraine", certainty: 1.0, cites: [{source: S1, locator: "§1.1"}, {source: S2, locator: "'Early life and education'"}], how_known: "Two sources."}
  religious_heritage_by_birth: {value: "Roman Catholic", certainty: 1.0, cites: [{source: S2, locator: "'Early life and education'"}, {source: S1, locator: "§1.1"}], how_known: "Two sources."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: "Jesuit schooling at La Flèche", certainty: 1.0, cites: [{source: S1, locator: "§1.1"}, {source: S2, locator: "'Early life and education'"}], how_known: "Two sources."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1619–1649", certainty: 0.7, cites: [{source: S1, locator: "§1.2–1.5"}], how_known: "From the 1619 dreams and early mathematics to the Passions."}
  age_at_first_lasting_contribution: {value: 41, certainty: 0.7, cites: [{source: S1, locator: "§1.1; §1.3"}], how_known: "Born 1596; Geometry published 1637. If the 1619 discovery is used, 23."}
  first_evidence_of_lio_type_views: {value: "The 'metaphysical turn' of his first months in the Netherlands: through his investigations into God and the self he was able 'to discover the foundation of physics' (SEP §1.3, citing AT 1:144). His later remark to Mersenne that the metaphysics of the Meditations contained 'all the principles of my physics' (AT 3:233) is about the Meditations, not 1629 (lens audit #156)", year: 1629, age: 33, certainty: 0.5, cites: [{source: S1, locator: "§1.3"}], how_known: "SEP dates a little metaphysical treatise to his first year in the Netherlands; the text is lost or survives only as the later Meditations."}
  lio_views_relative_to_major_work: {value: "during major work", rationale: "The lawful physics and the God that grounds it were first published in the Discourse (1637), in the middle of the major-work period; they were already in the suppressed World, begun after 1629, whose laws of motion are 'formulated and sustained by God' (S1 §1.3).", certainty: 0.5, cites: [{source: S4, locator: "Part V"}, {source: S1, locator: "§1.3"}], how_known: "Dates of what was read."}
  worldview_during_major_work: {value: "CLASS_THEISM throughout (draft code)", certainty: 0.5, cites: [{source: S4, locator: "Parts I, V"}, {source: S5, locator: "Part I"}], how_known: "Discourse (1637) and Principles (1644) agree."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "He resolved 'to accept as true nothing that did not appear to me more clear and certain than the demonstrations of the geometers' (Discourse V), and his four rules of method are 'a direct application of mathematical procedures' (Britannica).", certainty: 0.7, cites: [{source: S4, locator: "Part V, opening"}, {source: S2, locator: "'Early life and education' (four rules)"}], how_known: "His own text in an unofficial copy, and Britannica."}
  form_acquired: {value: "childhood or adolescence", certainty: 0.5, cites: [{source: S1, locator: "§1.1"}, {source: S4, locator: "Part I"}], how_known: "Mathematics at La Flèche, which he says delighted him by 'the certitude and evidence of their reasonings'; the method itself dates from 1619–1628."}
  circle_present: {value: "no", rationale: "God is an infinite substance distinct from extended matter (Meditation III); of three substances, 'The first and primary substance is God' (S1 §3.3). Not identified with Nature.", certainty: 0.7, cites: [{source: S6, locator: "Meditation III"}, {source: S1, locator: "§3.3"}], how_known: "His own text and SEP."}
  reading: "As belief, not finding: form present (geometrical demonstration as the standard), circle absent (a transcendent creator). A lawful-nature theist with early mathematical form: the pattern H1 says can occur, but it does not test the circle."
  notes: ""

institutions:
  - {value: "University of Franeker", role: "registered student", years: "1629", kind: university, certainty: 0.7, cites: [{source: S1, locator: "§1.3"}], how_known: "SEP."}
  - {value: "Court of Queen Christina of Sweden", role: "philosopher at court; wrote statutes for a Swedish royal academy", years: "1649–1650", kind: "patron or funder", certainty: 0.7, cites: [{source: S1, locator: "§1.5"}], how_known: "SEP."}
collaborators:
  - {value: "Isaac Beeckman", relation: "mentor or employer", note: "set him problems in physico-mathematics at Breda, 1618", certainty: 1.0, cites: [{source: S1, locator: "§1.2"}, {source: S2, locator: "'Early life and education'"}], how_known: "Two sources."}
  - {value: "Marin Mersenne", relation: correspondent, note: "long-time friend and main correspondent", certainty: 1.0, cites: [{source: S1, locator: "§1.2; §1.3"}, {source: S2, locator: "1622 paragraph"}], how_known: "Two sources."}
  - {value: "Thomas Hobbes", roster_id: hobbes-thomas, relation: "rival or critic", note: "wrote objections to the Meditations, printed with Descartes's answers", certainty: 1.0, cites: [{source: S6, locator: "title page"}, {source: S1, locator: "Bibliography (1680 Molyneux entry)"}], how_known: "The 1680 edition and SEP."}

review:
  roster_status_reason: {value: "Core in v8 (F 5: all five models); field tie across models.", certainty: 0.7, cites: [{source: S7, locator: "roster.csv, rank 68"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Date of analytic geometry: 1619 (Britannica, 'While in Bohemia in 1619, he invented analytic geometry') vs 'certainly by 1628' (SEP); published 1637."
    - "Entry to La Flèche: 1606 (Britannica) vs 1606 or 1607 (SEP)."
    - "Worldview texts read only in Project Gutenberg copies; Veitch's Principles is a selection that omits II.26–64."
    - "Britannica read as its first page only."
  open_questions:
    - "Check the quotations against the Adam–Tannery edition or Cottingham–Stoothoff–Murdoch (CSM) and give AT page numbers; that would lift the §7 cap."
    - "Decide whether CLASS_THEISM is meant to cover Cartesian rational theism (see report method question); if not, primary_system becomes BELOW_THRESHOLD with RATN as a stub candidate."
    - "Read Principles II.36 directly (laws from God's immutability)."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Gary Hatfield"
    year: 2023
    citation: "Hatfield, Gary. \"René Descartes.\" Stanford Encyclopedia of Philosophy (substantive revision 23 Oct 2023). https://plato.stanford.edu/entries/descartes/."
    url: "https://plato.stanford.edu/entries/descartes/"
    accessed: 2026-10-02
    reliability_note: "Scholarly reference work; §§1.1–1.5 and §2 read. Cited by section."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: tertiary
    kind: encyclopedia
    author: "Richard A. Watson"
    citation: "Watson, Richard A. \"René Descartes.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Rene-Descartes."
    url: "https://www.britannica.com/biography/Rene-Descartes"
    accessed: 2026-10-02
    reliability_note: "Signed article; first page only. Cited by section heading."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, lane_b, collaborators]
  - id: S3
    type: secondary
    kind: encyclopedia
    author: "Edward Slowik"
    year: 2025
    citation: "Slowik, Edward. \"Descartes' Physics.\" Stanford Encyclopedia of Philosophy (substantive revision 20 Oct 2025). https://plato.stanford.edu/entries/descartes-physics/."
    url: "https://plato.stanford.edu/entries/descartes-physics/"
    accessed: 2026-10-02
    reliability_note: "Scholarly reference work; opening, §4 and the conservation passage in §6 read. Its quotations of Principles II.37 and II.42 are secondary quotations. §4 labels the II.42 passage 'Pr II 62'; §6 labels it 'Pr II 42', which is the correct article (lens audit #138)."
    used_for: [contribution, worldview]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "René Descartes"
    year: 1637
    citation: "Descartes, René. Discourse on the Method of Rightly Conducting the Reason, and Seeking Truth in the Sciences. Translated by John Veitch. Project Gutenberg eBook 59, https://www.gutenberg.org/ebooks/59."
    url: "https://www.gutenberg.org/ebooks/59"
    accessed: 2026-10-02
    reliability_note: "Unofficial web copy of a 19th-century translation; capped at 0.7 under CODING_GUIDE §7. Cited by Part; no page numbers."
    used_for: [childhood, worldview, timing, lane_b, contribution]
  - id: S5
    type: primary
    kind: "published work by the subject"
    author: "René Descartes"
    year: 1644
    citation: "Descartes, René. Selections from the Principles of Philosophy. Translated by John Veitch. Project Gutenberg eBook 4391, https://www.gutenberg.org/ebooks/4391."
    url: "https://www.gutenberg.org/ebooks/4391"
    accessed: 2026-10-02
    reliability_note: "Unofficial web copy (§7 cap 0.7) of a selection: Part I, Part II §§1–25, Part III §§1–3 and Part IV from §188. Cited by Part and article number."
    used_for: [worldview, timing, contribution]
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "René Descartes"
    year: 1680
    citation: "Descartes, René. Six Metaphysical Meditations; Wherein It Is Proved That There Is a God [...]. Translated by William Molyneux. London: Benj. Tooke, 1680. Project Gutenberg eBook 70091, https://www.gutenberg.org/ebooks/70091."
    url: "https://www.gutenberg.org/ebooks/70091"
    accessed: 2026-10-02
    reliability_note: "Gutenberg transcription of the 1680 English translation (made from library images, per its credits line); still an unofficial web copy, so §7 cap 0.7. Cited by Meditation."
    used_for: [contribution, worldview, lane_b, collaborators]
  - id: S7
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
---

# René Descartes

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

René Descartes (1596–1650), French mathematician and philosopher, founded analytic geometry and gave modern philosophy its starting point in the method of doubt and the cogito [S1; S2]. A Roman Catholic, he argued to an infinite, immutable God by reason and grounded laws of nature in God's constant action [S6, Meditation III; S4, Part V; S3, §4]. Draft code CLASS_THEISM at 0.5 (partial fit; CHRIST and DEISM named). Axes A 1, B 3, D 1, E 3 at 0.7 and C 1 at 0.5; mid_basin true at 0.7 (draft).

## Life and work

Educated by the Jesuits at La Flèche and in law at Poitiers, he served as a gentleman soldier, worked with Beeckman, lived in the Netherlands from 1628/29 to 1649 and died in Stockholm at Queen Christina's court [S1, §§1.1–1.5; S2].

## Contribution and impact

Analytic geometry (published 1637), the cogito and dualism, and the first modern statement of laws of motion with a conservation principle [S1; S3].

## Childhood and education

His mother died when he was about a year old; he was raised by his grandmother and probably a great-uncle, then schooled at La Flèche, where mathematics was taught in the last three years [S1, §1.1; S2].

## Adult working worldview

God is "a certain Infinite Substance, Independent, Omniscient, Almighty" who created everything [S6, Meditation III] and sustains it by the same action [S4, Part V]. The laws God set "are accurately observed in all that exists or takes place in the world" [S4, Part V]. Revelation outranks reason where they conflict, but where there is no revelation the philosopher accepts only what he has ascertained [S5, I.76]. Hatfield calls his metaphysical God "tending toward the deistic" [S1, §1.5].

## Heritage (context only)

French Catholic family of lawyers [S1; S2]. Context only.

## Timing

First lasting contribution taken as the Geometry of 1637 (discovered 1619 or by 1628) [S1, §1.2; S2]. The lawful physics and its God appear in the Discourse [S4, Part V].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Geometric form present; circle absent [S4; S6].

## Open questions

- Check quotations against Adam–Tannery or CSM; read Principles II.36.
- Settle whether CLASS_THEISM covers Cartesian rational theism.

## Research log

- 2026-10-02: Read SEP "René Descartes" (Hatfield, §§1–2), SEP "Descartes' Physics" (Slowik, opening and §4), Britannica (Watson, first page). Read the Discourse (Gutenberg 59), Veitch's Principles selections (Gutenberg 4391) and Molyneux's Meditations (Gutenberg 70091) and copied the quotations from those files. No Adam–Tannery or CSM text opened. Wikipedia not used.
- 2026-10-02 (lens audit fixes): Read SEP "René Descartes" §3.3 and SEP "Descartes' Physics" §6, and re-read Principles I.14–15 and Discourse IV–V (Gutenberg) for items #94–#168.
