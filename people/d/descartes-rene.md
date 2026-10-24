---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (executor agent for v8, RUNBOOK stage 3, batch A: early modern philosophers)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (stage 3, batch A). Basics from SEP 'René Descartes' (Hatfield) and Britannica (Watson, first page); physics from SEP 'Descartes' Physics' (Slowik). Worldview from the Discourse (Veitch), the Principles (Veitch's selections) and the Meditations (Molyneux 1680), all read in Project Gutenberg texts, so capped at 0.7 (CODING_GUIDE §7). DRAFT SCORES for v8's review: primary_system CLASS_THEISM 0.5; A 1, B 3, D 1, E 3 at 0.7; C 1 at 0.5; mid_basin true (0.7). Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit fixes, stage 3 batch A (two blind runs at 59a8371). #94: native_name 'René Descartes' (French), 'Renatus Cartesius' dropped. #123: early_mathematics 'other' (curriculum only; no source says advanced). #132: primary_system rationale now quotes the CLASS_THEISM tests and cites Principles I.14–15 (idea of God) and Discourse IV for the attributes; value unchanged. #138: conservation passage is Principles II.42 (SEP physics §4 prints 'Pr II 62'; §6 has II 42). #141: the named alternative score is now in the E rationale; rational soul quoted from Discourse V. #156: first_evidence wording now the 1629 'foundation of physics' letter (AT 1:144); 'all the principles of my physics' is a later letter about the Meditations (AT 3:233). #157, #161, #168: locators and coder note corrected. S5 note lists the parts in the selection. Not reviewed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #67, F5 rank 68). Needs already dark and corroborated on A and B; still deepen gaps (P47/P48, scholarly editions, TODOs). Opened Adam–Tannery Oeuvres vol. VI Discours Part V (French: lois établies; continuous creation / same action; mouches & fourmis) and vol. VIII Principia II.36–37 Latin (God primary cause; conservation by ordinary concurrence; immutability; explicit exception for changes known by experience or divine revelation = miracles). Wikipedia EN dual bio (P50). Charles Adam Vie et œuvres: baptism 3 Apr 1596 Saint-George La Haye. P47 source_quality on every source. support: corroborated on A/B/D/E (P48). Scores unchanged: A 1 @0.7 (alt 0), B 3 @0.7 (alt 4; II.36 miracle exception confirms not 4), C 1 @0.5, D 1 @0.7, E 3 @0.7; CLASS_THEISM @0.5; mid_basin true @0.7. Chart-moving NO. No fallacy_catalog (Jason). Draft, not reviewed."}

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
  family_religious_practice: {value: "Roman Catholic baptism and Jesuit college education", certainty: 0.7, cites: [{source: S10, locator: "baptism Saint-George 3 Apr 1596"}, {source: S1, locator: "§1.1 La Flèche"}], how_known: "Parish baptism (Adam/Baillet) and Jesuit schooling; practice intensity not detailed."}
  parents_and_household:
    - {value: "Father, Joachim, a lawyer and councillor in the Parlement of Brittany at Rennes", name: "Joachim Descartes", role: father, certainty: 1.0, cites: [{source: S1, locator: "§1.1"}, {source: S2, locator: "'Early life and education'"}], how_known: "Two sources."}
    - {value: "Mother, Jeanne Brochard, died in childbirth when he was thirteen and a half months old", name: "Jeanne Brochard", role: mother, certainty: 1.0, cites: [{source: S1, locator: "§1.1"}, {source: S2, locator: "'Early life and education' ('when he was one year old')"}], how_known: "Two sources."}
  household_circumstances: {value: "Raised first by his maternal grandmother at La Haye, then probably by a great-uncle at Châtellerault; family of lawyers with minor nobility", certainty: 0.7, cites: [{source: S1, locator: "§1.1 ('It is likely')"}, {source: S2, locator: "'Early life and education'"}], how_known: "Two sources; SEP hedges the move."}
  schooling:
    - {value: "Jesuit College of La Flèche: grammar school, then three years of Aristotelian philosophy, with mathematics in the final three years", stage: "grammar or secondary school", run_by: "religious body", years: "1606/1607–1614/1615", certainty: 0.7, cites: [{source: S1, locator: "§1.1"}, {source: S2, locator: "'Early life and education' (1606)"}, {source: S9, locator: "education 1607–1614"}], how_known: "Two/three sources; SEP 1606 or 1607, Britannica 1606, Wikipedia 1607–1614. Schema 1.3: Jesuit college = grammar/secondary run_by religious body."}
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
  working_years: {value: "1637–1649", certainty: 0.7, cites: [{source: S1, locator: "§1.3–1.5"}, {source: S9, locator: "major works 1637–1649"}], how_known: "Equal to timing.major_work_period (P30 addendum): Geometry/Discourse 1637 through Passions 1649."}
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
      support: corroborated
      cites: [{source: S6, locator: "Meditation III"}, {source: S4, locator: "Part V"}, {source: S8, locator: "AT VI, Discours Part V — continuous creation French"}]
      how_known: "Own published works; Discourse continuous-creation wording checked against Adam–Tannery French (S8). Certainty 0.7: named alternative 0, and Meditations still read in unofficial EN (S6)."
      rationale: "Leans to the transcendent-person pole: God is 'a certain Infinite Substance, Independent, Omniscient, Almighty, by whom both I my self, and every thing else that is [...] was created' (Meditation III / S6), distinct from the extended world he creates. Not 0, because God sustains the world continuously — AT VI French: the action by which he now conserves it is the same as that by which he created it (S8; matches Veitch S4). Same immanence feature as Aquinas/Newton at 1. Named alternative: 0. Independent source ids → corroborated (P48)."
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S4, locator: "Part V"}, {source: S8, locator: "AT VI Discours lois; AT VIII Principia II.36–37"}, {source: S3, locator: "§4 / §6 Pr II.37 and II.42"}, {source: S1, locator: "§1.5"}]
      how_known: "Discourse laws + Principles II.36 checked in Adam–Tannery (S8). Named alternative 4 (Hatfield)."
      rationale: "Scored on his account of nature (P6/P16). Leans LIO: God established certain laws in nature exactly observed in all that exists or takes place (Discourse V / AT VI French, S8); God is primary cause of motion and conserves the same quantity of motion by ordinary concurrence (Principia II.36 AT VIII Latin, S8). Stated limited exceptions: (1) Principia II.36 itself excepts changes that evident experience or divine revelation make certain — i.e. miracles — from the 'no other changes in His works' rule; (2) free created mind outside mechanical necessity (Principles I.37). Named alternative: 4 (Hatfield: if fully consistent, no miracles — S1 §1.5). Independent source ids → corroborated (P48)."
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
      support: corroborated
      cites: [{source: S5, locator: "Part I, §76"}, {source: S4, locator: "Part I"}]
      how_known: "Own published text (unofficial EN copies, §7); named alternative 2. Two independent work-ids → corroborated (P48)."
      rationale: "DRAFT. Revelation outranks reason when they conflict: 'what God has revealed is incomparably more certain than anything else; and that, we ought to submit our belief to the Divine authority rather than to our own judgment, even although perhaps the light of reason should, with the greatest clearness and evidence, appear to suggest to us something contrary' (Principles I.76). A large domain is left to reason ('in things regarding which there is no revelation'). Same pattern as Aquinas (D 1: when they conflict revelation wins). Named alternative: 2, because in practice his physics is built from reason alone and revelation is silent on it."
    E_scope:
      value: 3
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S5, locator: "Part II, §22–23; Part III, §3"}, {source: S4, locator: "Part V"}]
      how_known: "Own published texts (unofficial EN, §7); named alternative 4. Two independent work-ids → corroborated (P48)."
      rationale: "DRAFT. Scored on the world's order (P7). Leans LIO: 'the earth and heavens are made of the same matter' and 'There is therefore but one kind of matter in the whole universe' (Principles II.22–23); animal and human bodies are machines 'made by the hands of God' (Discourse V); and the supposition that all things were made for us 'would be plainly ridiculous and inept in physical reasoning' (Principles III.3). The stated, limited exception is the human rational soul, which 'could by no means be educed from the power of matter' but 'must be expressly created' (Discourse V). No favour for a group in events in anything read. His hope of heaven is a C matter (P7). Named alternative: 4, if the rational soul is not counted as an exception to the world's order, since it concerns the human mind and grants no group any exception in events."
  mid_basin: {value: true, certainty: 0.7, cites: [{source: S6, locator: "Meditation III"}, {source: S4, locator: "Part V"}, {source: S8, locator: "AT VI / VIII"}], how_known: "P4/P6 test: A_locus 1 (0.7) ≤ 1 and B_cause 3 (0.7) ≥ 3, both at ≥ 0.7 and corroborated (P48), so true. Certainty is the lower of the two (0.7). Named-alternative cases do not change the mid-basin result. Chart already dark filled; deepen did not move the dot."}
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
    - text: "que Dieu a tellement establies en la nature, & dont il a imprimé de telles notions en nos ames, qu apres y avoir fait assez de reflexion, nous ne sçaurions douter qu'elles ne soient exactement observées, en tout ce qui est ou qui se fait dans le monde"
      cites: [{source: S8, locator: "AT VI, Discours de la méthode, Part V (French)"}]
      date: "1637"
      context: "Discourse Part V — laws God established in nature (French original via Adam–Tannery)."
      axes: [B_cause, E_scope]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Spelling normalized from AT OCR long-s/ampersands for readability; sense checked against Veitch S4."
    - text: "il est certain, & c'est une opinion communement receuë entre les Theologiens, que l'action, par laquelle maintenant il le conserve, est toute la mesme que celle par laquelle il l'a creé"
      cites: [{source: S8, locator: "AT VI, Discours Part V (French continuous creation)"}]
      date: "1637"
      context: "Discourse Part V — God sustains the world by the same action as creation."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "AT French; matches Veitch 'action by which he now sustains it' (S4)."
    - text: "Motûs naturâ sic animadversâ, considerare oportet ejus causam, eamque duplicem: primò scilicet universalem & primariam […] Et generalem quod attinet, manifestum mihi videtur illam non aliam esse, quam Deum ipsum, qui materiam simul cum motu & quiete in principio creavit, jamque, per solum suum concursum ordinarium, tantundem motûs & quietis in eâ totâ quantum tunc posuit conservat. […] Intelligimus etiam perfectionem esse in Deo, non solùm quod in se ipso sit immutabilis, sed etiam quod modo quàm maximè constanti & immutabili operetur: adeò ut, iis mutationibus exceptis, quas evidens experientia vel divina revelatio certas reddit […] nullas alias in ejus operibus supponere debeamus"
      cites: [{source: S8, locator: "AT VIII, Principia Philosophiae II.36 (Latin)"}]
      date: "1644"
      context: "Principles II.36 — God primary cause of motion; conserves quantity of motion; immutability; exceptions for changes known by experience or divine revelation (miracles)."
      axes: [B_cause, A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Latin normalized from AT VIII OCR (long-s/ligatures). Confirms B 3 not 4: miracle exceptions are explicit in II.36 itself."
  changes_over_life: []
  coder_notes: "DRAFT SCORES. Deepen D1 2026-10-24: AT VI Discours Part V French and AT VIII Principia II.36–37 Latin opened (S8) — lifts the 'II.36 unread' gap; miracle exception is in II.36 itself. Gutenberg Veitch/Molyneux kept as EN cross-check (S4–S6); worldview certainties stay ≤0.7 (named alternatives + Meditations still unofficial EN). RATN stub flag remains. Rosicrucian/dream material not scored. Chart-moving NO (already dark filled mid-basin)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "French; family of lawyers with minor nobility from Poitou and Touraine", certainty: 1.0, cites: [{source: S1, locator: "§1.1"}, {source: S2, locator: "'Early life and education'"}], how_known: "Two sources."}
  religious_heritage_by_birth: {value: "Roman Catholic", certainty: 1.0, cites: [{source: S2, locator: "'Early life and education'"}, {source: S1, locator: "§1.1"}], how_known: "Two sources."}
  baptism_or_initiation: {value: "Baptized 3 April 1596, église Saint-George, La Haye (curé Grison); godparents René Brochard and Michel Ferrand; godmother Jeanne Proust Sain", certainty: 0.7, cites: [{source: S10, locator: "baptism act; Baillet extract"}, {source: S9, locator: "Early life — Catholic family"}], how_known: "Charles Adam (AT editor) from parish register and Baillet; Wikipedia agrees on Catholic family."}
  childhood_catechism: {value: "Jesuit schooling at La Flèche", certainty: 1.0, cites: [{source: S1, locator: "§1.1"}, {source: S2, locator: "'Early life and education'"}], how_known: "Two sources."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1637–1649", certainty: 0.7, cites: [{source: S1, locator: "§1.3–1.5"}, {source: S4, locator: "Discourse 1637"}, {source: S9, locator: "Passions 1649"}], how_known: "First lasting published (Geometry/Discourse 1637) to last listed major work (Passions 1649) (P29). Discovery of analytic geometry dated 1619/1628 is outside the published-span start."}
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
    - "Date of analytic geometry: 1619 (Britannica) vs 'certainly by 1628' (SEP); published 1637."
    - "Entry to La Flèche: 1606 (Britannica) vs 1606 or 1607 (SEP); Wikipedia 1607–1614."
    - "Meditations still read in Molyneux 1680 Gutenberg EN (S6); Discourse/Principles key A/B passages now also in AT French/Latin (S8)."
    - "Britannica Watson still mainly first-page depth from create pass; Wikipedia added as dual bio."
    - "CLASS_THEISM at 0.5 remains a judgment call (partial fit to Aristotelian label)."
  open_questions:
    - "CSM (Cottingham–Stoothoff–Murdoch) EN cross-check of Meditations III and Principles I.76 with AT page numbers — could firm EN wording; named alternatives still cap A/B at 0.7."
    - "Decide whether CLASS_THEISM is meant to cover Cartesian rational theism; if not, primary_system → BELOW_THRESHOLD (CHRIST lead) or a new Cartesian-theism code."
    - "Fuller Britannica Watson body when live/unblocked."
    - "Private letters on piety (e.g. to Elisabeth / Chanut) for C_ledger beyond Discourse passing remarks."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Gary Hatfield"
    year: 2023
    citation: "Hatfield, Gary. \"René Descartes.\" Stanford Encyclopedia of Philosophy (substantive revision 23 Oct 2023). https://plato.stanford.edu/entries/descartes/."
    url: "https://plato.stanford.edu/entries/descartes/"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Scholarly reference work; §§1.1–1.5 and §2–3 read (create + deepen). Cited by section."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: tertiary
    kind: encyclopedia
    author: "Richard A. Watson"
    citation: "Watson, Richard A. \"René Descartes.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Rene-Descartes."
    url: "https://www.britannica.com/biography/Rene-Descartes"
    accessed: 2026-10-02
    source_quality: "reference entry"
    reliability_note: "Signed article; first page mainly (create pass). Dual-sourced with Wikipedia S10 on deepen."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, lane_b, collaborators]
  - id: S3
    type: secondary
    kind: encyclopedia
    author: "Edward Slowik"
    year: 2025
    citation: "Slowik, Edward. \"Descartes' Physics.\" Stanford Encyclopedia of Philosophy (substantive revision 20 Oct 2025). https://plato.stanford.edu/entries/descartes-physics/."
    url: "https://plato.stanford.edu/entries/descartes-physics/"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Scholarly reference work; opening, §4 and conservation in §6. II.37/II.42 quotes are secondary; deepen now has AT VIII II.36 primary (S8). §4 mislabel 'Pr II 62' noted (lens #138)."
    used_for: [contribution, worldview]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "René Descartes"
    year: 1637
    citation: "Descartes, René. Discourse on the Method of Rightly Conducting the Reason, and Seeking Truth in the Sciences. Translated by John Veitch. Project Gutenberg eBook 59, https://www.gutenberg.org/ebooks/59."
    url: "https://www.gutenberg.org/ebooks/59"
    accessed: 2026-10-02
    source_quality: "unofficial web copy"
    reliability_note: "Unofficial web copy of Veitch EN; key Part V laws/continuous-creation wording cross-checked against AT VI French (S8) on deepen. Cited by Part."
    used_for: [childhood, worldview, timing, lane_b, contribution]
  - id: S5
    type: primary
    kind: "published work by the subject"
    author: "René Descartes"
    year: 1644
    citation: "Descartes, René. Selections from the Principles of Philosophy. Translated by John Veitch. Project Gutenberg eBook 4391, https://www.gutenberg.org/ebooks/4391."
    url: "https://www.gutenberg.org/ebooks/4391"
    accessed: 2026-10-02
    source_quality: "unofficial web copy"
    reliability_note: "Unofficial web copy of Veitch selection (omits II.26–64). II.36 now read in AT Latin (S8); I.76 and II.22–23 / III.3 still from this selection."
    used_for: [worldview, timing, contribution]
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "René Descartes"
    year: 1680
    citation: "Descartes, René. Six Metaphysical Meditations; Wherein It Is Proved That There Is a God [...]. Translated by William Molyneux. London: Benj. Tooke, 1680. Project Gutenberg eBook 70091, https://www.gutenberg.org/ebooks/70091."
    url: "https://www.gutenberg.org/ebooks/70091"
    accessed: 2026-10-02
    source_quality: "unofficial web copy"
    reliability_note: "Gutenberg transcription of Molyneux 1680 EN; still unofficial for Meditations III God definition. Cited by Meditation."
    used_for: [contribution, worldview, lane_b, collaborators]
  - id: S7
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    source_quality: "study roster"
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
  - id: S8
    type: primary
    kind: "scholarly edition"
    author: "René Descartes (ed. Charles Adam and Paul Tannery)"
    year: 1897
    citation: "Descartes, René. Oeuvres de Descartes. Edited by Charles Adam and Paul Tannery. Paris: Léopold Cerf, 1897–1913. Vol. VI (Discours de la méthode) and vol. VIII (Principia philosophiae). Archive.org scans of Fisher/Toronto copies (djvu OCR read 2026-10-24)."
    url: "https://archive.org/details/oeuvresdedescar08desc"
    accessed: 2026-10-24
    source_quality: "scholarly edition or monograph"
    reliability_note: "Standard scholarly collected works (AT). Vol. VI Discours Part V French (laws; continuous creation; mouches & fourmis). Vol. VIII Principia II.36–37 Latin (primary cause; conservation; immutability; revelation/experience exceptions). OCR long-s normalized when quoting."
    used_for: [worldview, contribution, timing]
  - id: S9
    type: secondary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: 'Wikipedia contributors. "René Descartes." Wikipedia, The Free Encyclopedia. https://en.wikipedia.org/wiki/René_Descartes (accessed 24 October 2026).'
    url: "https://en.wikipedia.org/wiki/René_Descartes"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Dual-source bio with Britannica (P50). Early life (Catholic family; La Flèche 1607–1614), career outline, death Stockholm. Not used alone for worldview scores."
    used_for: [identity, basics, childhood, heritage, collaborators, review]
  - id: S10
    type: secondary
    kind: "scholarly book"
    author: "Charles Adam"
    year: 1910
    citation: "Adam, Charles. Vie et œuvres de Descartes. Livre I, chapitre premier. Paris: Léopold Cerf, 1910. French Wikisource transcription."
    url: "https://fr.wikisource.org/wiki/Vie_et_œuvres_de_Descartes/Livre_I/Chapitre_premier"
    accessed: 2026-10-24
    source_quality: "scholarly edition or monograph"
    reliability_note: "Biography by the AT co-editor; cites Baillet and the La Haye baptism register (3 April 1596, Saint-George, curé Grison)."
    used_for: [heritage, childhood, basics]
---

# René Descartes

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

René Descartes (1596–1650), French mathematician and philosopher, founded analytic geometry and gave modern philosophy its starting point in the method of doubt and the cogito [S1; S2; S9]. A Roman Catholic (baptized 3 Apr 1596, La Haye) [S10], he argued to an infinite, immutable God by reason and grounded laws of nature in God's constant action [S6; S4; S8 AT VI/VIII]. Draft CLASS_THEISM at 0.5. Axes A 1 / B 3 at 0.7 corroborated; mid_basin true. Deepen solidify; chart-moving no.

## Life and work

Educated by the Jesuits at La Flèche and in law at Poitiers, he served as a gentleman soldier, worked with Beeckman, lived in the Netherlands from 1628/29 to 1649 and died in Stockholm at Queen Christina's court [S1, §§1.1–1.5; S2].

## Contribution and impact

Analytic geometry (published 1637), the cogito and dualism, and the first modern statement of laws of motion with a conservation principle [S1; S3].

## Childhood and education

His mother died when he was about a year old; he was raised by his grandmother and probably a great-uncle, then schooled at La Flèche, where mathematics was taught in the last three years [S1, §1.1; S2].

## Adult working worldview

God is "a certain Infinite Substance, Independent, Omniscient, Almighty" who created everything [S6, Meditation III] and sustains it by the same action [S4; S8 AT VI French]. Laws God established in nature are exactly observed in all that exists or takes place [S4; S8]. Principia II.36: God is primary cause of motion, conserves quantity of motion by ordinary concurrence; exceptions for changes known by experience or divine revelation (miracles) [S8 AT VIII]. Revelation outranks reason where they conflict [S5, I.76]. Hatfield: metaphysical God "tending toward the deistic"; if fully consistent, no miracles — named alt for B 4 [S1, §1.5]. Scores: A 1 / B 3 @0.7 corroborated; mid_basin true.

## Heritage (context only)

French Catholic family of lawyers; baptized Saint-George La Haye 3 April 1596 [S1; S2; S9; S10]. Context only.

## Timing

First lasting contribution taken as the Geometry of 1637 (discovered 1619 or by 1628) [S1, §1.2; S2]. The lawful physics and its God appear in the Discourse [S4, Part V].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Geometric form present; circle absent [S4; S6].

## Open questions

- CSM EN cross-check of Meditations III / Principles I.76 with AT page numbers.
- Settle whether CLASS_THEISM covers Cartesian rational theism.
- Private letters (Elisabeth / Chanut) for C_ledger.

## Research log

- 2026-10-02: Read SEP Hatfield §§1–2, SEP Slowik physics, Britannica Watson first page; Gutenberg Discourse / Principles selections / Molyneux Meditations.
- 2026-10-02 (lens audit): SEP §3.3; Slowik §6; Principles I.14–15; Discourse IV–V.
- 2026-10-24 (D1): AT VI Discours Part V French; AT VIII Principia II.36–37 Latin; Wikipedia EN; Charles Adam Vie et œuvres (baptism). P47/P48. No fallacy_catalog.
