---
record:
  record_type: person
  schema_version: "1.1"
  record_version: 6
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (overnight agent run for Jason, first pool)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages and translations"
  collected_on: 2026-10-02
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created. Basics, contribution, childhood, worldview (CLASS_THEISM at 1.0) and all five LIO axes filled from the Summa theologiae (English Dominican translation) and three reference sources. mid_basin UNKNOWN: B_cause scored 2, which the P4 test does not cover. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "mid_basin changed from UNKNOWN to TODO with a note: the evidence is in, but P4 does not say whether B is scored on his theology or his account of nature (new open item P6). key_early_reading changed from an empty list to UNKNOWN, as the coding guide asks."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "P6 decided by Jason (2026-10-02): B_cause is scored on the account of nature. B_cause changed from 2 to 3 at 1.0, with the theology-wide reading (2) kept in the rationale; added the I q. 105 a. 5 statement. mid_basin changed from TODO to true at 1.0. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit fixes: B_cause certainty 1.0 -> 0.7 (miracles in ST I q. 105 a. 6–8 are part of his account of nature; the theology-wide 2 is a named alternative); mid_basin certainty 1.0 -> 0.7, with a note that the result turns on decision P6. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit, run 2 (claim #23 pattern): E_scope certainty 1.0 -> 0.7, because the score depends on which domain E is scored on (open item P7, PROPOSED). Score unchanged (2). Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "P7 decided by Jason (2026-10-02, option 1): E_scope is scored on the world's order. E_scope 2 -> 3 at 0.7 (universal providence over individual creatures, I q. 22 a. 2; miracles the limited exception; named alternative 2 from I q. 22 a. 2 ad 4). Reprobation and salvation by revealed truth moved to the C_ledger rationale (C unchanged). Two statements added from I q. 22 a. 2 (same source, page already read), checked word for word. P7 interim note removed. mid_basin unchanged. Not reviewed."}

identity:
  id: aquinas-thomas
  display_name: "Thomas Aquinas"
  roster:
    canonical_name: "Thomas Aquinas"
    rank: 135
    F: 4
    models: [Claude, DeepSeek, GPT, Grok]
    band: "core (3–4)"
    status: core
    field: philosophy
    field_bucket: philosophy
  full_name: {value: "Thomas Aquinas (Thomas of Aquino)", certainty: 1.0, cites: [{source: S1, locator: "opening sentence"}, {source: S2, locator: "§1.1"}], how_known: "Named for the family seat near Aquino (S2). 'Saint' from his canonization in 1323 (S1)."}
  native_name: {value: "Tommaso d'Aquino", certainty: 0.5, cites: [{source: S2, locator: "§1.1 (born near Aquino)"}], how_known: "Italian form of the name; not given in the sources read, built by the coder from the place name. He wrote in Latin (Thomas de Aquino)."}
  aliases:
    - {name: "Thomas-Aquinas", kind: "roster alias"}
    - {name: "Saint Thomas Aquinas", kind: "title or honorific"}

basics:
  birth:
    date:
      value: "1225"
      approx: true
      calendar: julian
      certainty: 0.7
      cites: [{source: S2, locator: "§1.1 ('around the year 1225')"}, {source: S1, locator: "opening sentence ('1224/25')"}, {source: S3, locator: "§1.a ('between 1224 and 1226')"}]
      how_known: "Three sources agree on about 1225 but none gives a day; so 0.7."
      alternatives:
        - {value: "1224", cites: [{source: S1, locator: "opening sentence"}, {source: S3, locator: "§1.a"}], note: "Britannica gives 1224/25; IEP gives a range 1224–1226."}
    place:
      value: "Roccasecca, near Aquino, Kingdom of Sicily"
      modern_name: "Roccasecca, Lazio, Italy"
      polity_then: "Kingdom of Sicily"
      certainty: 1.0
      cites: [{source: S1, locator: "opening sentence"}, {source: S3, locator: "§1.a"}, {source: S2, locator: "§1.1 (family castle at Roccasecca)"}]
      how_known: "Three sources agree."
  death:
    date: {value: "1274-03-07", calendar: julian, certainty: 1.0, cites: [{source: S1, locator: "opening sentence; Last years at Naples"}, {source: S2, locator: "§1.1"}, {source: S3, locator: "§1.a"}], how_known: "Three sources agree."}
    place:
      value: "Cistercian abbey of Fossanova, near Terracina"
      modern_name: "Fossanova, Priverno, Lazio, Italy"
      polity_then: "Papal States"
      certainty: 1.0
      cites: [{source: S1, locator: "opening sentence"}, {source: S2, locator: "§1.1"}]
      how_known: "Two sources agree; he fell ill on his way to the Second Council of Lyon (S1, S3)."
  first_lasting_contribution_year: {value: 1252, approx: true, certainty: 0.7, cites: [{source: S3, locator: "References: Thomas' Works (De ente et essentia, 1252–1253)"}, {source: S2, locator: "§1.2; §4 (essence and existence)"}], how_known: "Year On Being and Essence was begun, per IEP's work list. Its account of essence and existence is listed as a lasting contribution below. Dated only to a range, so 0.7."}
  era_bucket: {value: "500 to 1399", certainty: 1.0, cites: [{source: S3, locator: "References: Thomas' Works"}], how_known: "Derived from first_lasting_contribution_year (1252) under the era buckets (decision P2). Any date in his career gives the same bucket."}
  region_of_birth: {value: "Southern Europe", certainty: 1.0, cites: [{source: S1, locator: "opening sentence"}], how_known: "Born in what is now Italy; Italy is Southern Europe in data/reference/regions.csv (UN M49 sub-region, decision P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S2, locator: "§1.1"}, {source: S3, locator: "§1.a"}], how_known: "He taught in Paris (1252–1259, 1268–1272) and Cologne (1248–1252) and in Italy (1259–1268, 1272–1273). His two Paris regencies and the Summa contra gentiles years split between France and Italy; Western Europe is chosen because his university career centred on Paris. Southern Europe is a close alternative, so 0.7."}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S2, locator: "§1.1"}], how_known: "As the sources record it."}
  languages_of_work: {value: [Latin], certainty: 1.0, cites: [{source: S4, locator: "edition note (Fathers of the English Dominican Province, 2nd rev. ed., 1920, translated from the Latin)"}, {source: S1, locator: "Years at the papal Curia (works and literary forms)"}], how_known: "He wrote in Latin, the language of the universities."}
  occupations:
    value: ["Dominican friar and priest", "master (professor) of theology", "papal theological adviser", "commentator on Aristotle and the Bible"]
    certainty: 1.0
    cites: [{source: S1, locator: "opening sentence; Years at the papal Curia"}, {source: S2, locator: "§1.1"}, {source: S3, locator: "§1.a"}]
    how_known: "Three sources agree."

contribution:
  fields: {value: [philosophy, theology, metaphysics, ethics, "natural law", "philosophy of mind"], certainty: 1.0, cites: [{source: S2, locator: "contents; §8"}, {source: S3, locator: "introduction"}], how_known: "Two reference sources agree."}
  lasting_original_contributions:
    - {value: "The distinction between essence and existence in all created things, with God as the one being whose essence is to exist (On Being and Essence; developed in the Summa)", year: 1252, kind: "concept or term", lasting: "a core doctrine of Thomist metaphysics", certainty: 0.7, cites: [{source: S2, locator: "§4 ('God's perfect simplicity precludes even the composition of essence and existence, which is found in all created substances')"}, {source: S3, locator: "References (De ente et essentia, 1252–1253)"}], how_known: "SEP states the doctrine; the year is IEP's date for the treatise. That the doctrine is original to this treatise is the coder's reading, so 0.7."}
    - {value: "The Summa contra gentiles: a work of natural theology arguing to God and providence from premises open to reason", year: "1259–1265", kind: work, lasting: "standard text of natural theology", certainty: 1.0, cites: [{source: S3, locator: "§1.b; References"}, {source: S1, locator: "opening sentence"}], how_known: "Two sources."}
    - {value: "The Summa theologiae, with the 'five ways' of proving that God exists; the classical systematization of Latin theology", year: "1265–1273", kind: work, lasting: "Thomism; the Catholic Church's reference theology", certainty: 1.0, cites: [{source: S1, locator: "opening sentence"}, {source: S2, locator: "§2"}, {source: S3, locator: "References (dates by part)"}], how_known: "Three sources."}
    - {value: "A theory of natural law grounding moral law in human nature and reason", year: "1271", kind: theory, lasting: "natural law theory in ethics and law", certainty: 0.7, cites: [{source: S2, locator: "§8.2"}, {source: S4, locator: "I-II q. 94"}], how_known: "SEP section and the text itself; the year is the IEP date for the Prima Secundae, where the treatise sits."}
  evidence_of_impact:
    - {value: "Recognized by the Roman Catholic Church as its foremost Western philosopher and theologian (S1); named a Doctor of the Church in 1567; Leo XIII's encyclical Aeterni Patris (1879) held him up as a model for Christian philosophy (S3, S2)", kind: "institutional or technological lineage", certainty: 1.0, cites: [{source: S1, locator: "opening paragraph; Legacy"}, {source: S3, locator: "§1.a"}, {source: S2, locator: "§9"}], how_known: "Three sources."}
    - {value: "Thomism, the school named after him, from the 15th century (Capreolus) to the present; adopted as the official philosophy of the Church in 1917", kind: "named after them", certainty: 1.0, cites: [{source: S1, locator: "Introduction & Top Questions"}, {source: S2, locator: "§9"}], how_known: "Two sources."}
    - {value: "Almost everything he wrote survives, more than eight million words, edited and translated into many languages", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S2, locator: "§1.2"}], how_known: "One source."}
  major_works:
    - {value: "Commentary on the Sentences of Peter Lombard", year: "1252–1256", kind: book, certainty: 1.0, cites: [{source: S3, locator: "References"}, {source: S2, locator: "§1.1"}], how_known: "Two sources."}
    - {value: "Summa contra gentiles", year: "1259–1265", kind: book, certainty: 1.0, cites: [{source: S3, locator: "References"}, {source: S2, locator: "§1.1"}], how_known: "Two sources."}
    - {value: "Summa theologiae (unfinished)", year: "1265–1273", kind: book, certainty: 1.0, cites: [{source: S3, locator: "References"}, {source: S1, locator: "opening sentence"}], how_known: "Two sources."}
    - {value: "Commentaries on Aristotle's principal works", year: "chiefly 1268–1273", kind: "other", certainty: 0.7, cites: [{source: S2, locator: "§1.1"}], how_known: "One source for the dating."}
  honours:
    - {value: "Master of theology at Paris below the statutory age", year: 1256, certainty: 1.0, cites: [{source: S2, locator: "§1.1"}, {source: S1, locator: "Studies in Paris"}], how_known: "Two sources."}
    - {value: "Canonized", year: 1323, certainty: 1.0, cites: [{source: S1, locator: "opening sentence"}, {source: S2, locator: "§9"}, {source: S3, locator: "§1.a"}], how_known: "Three sources (S2 gives 18 July 1323)."}
    - {value: "Doctor of the Church", year: 1567, certainty: 1.0, cites: [{source: S1, locator: "Legacy"}, {source: S3, locator: "§1.a"}, {source: S2, locator: "§9"}], how_known: "Three sources."}
  definition_fit: {value: "clearly meets", rationale: "Founder of a school that has lasted 750 years; the Catholic Church's reference theologian; natural law theory and his arguments for God are still taught.", certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}, {source: S2, locator: "introduction; §9"}], how_known: "Lane A definition (lasting original impact on documented criteria) applied to the contributions above."}

childhood:
  family_religion: {value: "Latin (Roman) Catholic. His family gave him as a boy to the Benedictine abbey of Monte Cassino as an oblate, hoping he would one day become its abbot.", certainty: 1.0, cites: [{source: S1, locator: "Early years"}, {source: S3, locator: "§1.a"}, {source: S2, locator: "§1.1"}], how_known: "Three sources agree on the oblation and the family's hopes. 'Catholic' is implied by the oblation rather than stated."}
  family_religious_practice: {value: TODO, note: "No account of the household's worship in the sources read. Torrell's biography (S2's main reference) may have it."}
  parents_and_household:
    - {value: "Father of Lombard origin, mother of Norman descent; the family held a modest feudal domain on the disputed border between the emperor and the pope and served Emperor Frederick II", role: parents, certainty: 1.0, cites: [{source: S1, locator: "Early years"}], how_known: "One signed reference source; consistent with S2 and S3 on the family castle. The parents' names are not given in the sources read."}
    - {value: "Youngest of at least nine children; the youngest of four boys", role: "sibling position", certainty: 1.0, cites: [{source: S2, locator: "§1.1"}, {source: S3, locator: "§1.a"}], how_known: "Two sources."}
  household_circumstances: {value: "A wealthy family that presided over a prominent castle at Roccasecca, held by the Aquino family for over a century", certainty: 1.0, cites: [{source: S2, locator: "§1.1"}, {source: S3, locator: "§1.a"}], how_known: "Two sources agree."}
  schooling:
    - {value: "Oblate at the Benedictine abbey of Monte Cassino, where he received his early education; he left in 1239 when the emperor expelled the monks", stage: "religious school", institution: "Abbey of Monte Cassino", years: "c. 1230–1239", ages: "c. 5–14", certainty: 1.0, cites: [{source: S1, locator: "Early years ('after nine years')"}, {source: S3, locator: "§1.a ('from approximately 5 to 15 years of age')"}, {source: S2, locator: "§1.1"}], how_known: "Three sources agree on the abbey; S1's nine years ending 1239 and S3's ages 5 to 15 agree roughly."}
    - {value: "University of Naples: the liberal arts and philosophy, including newly translated works of Aristotle, perhaps introduced by Peter of Ireland", stage: university, institution: "University of Naples", years: "1239–1244", ages: "c. 14–19", certainty: 1.0, cites: [{source: S3, locator: "§1.a"}, {source: S1, locator: "Early years"}], how_known: "Two sources agree on Naples and Aristotle; S3 hedges on Peter of Ireland."}
    - {value: "Dominican studies at Paris (1245–1248) and Cologne (1248–1252) under Albert the Great; then bachelor of the Sentences at Paris (1252–1256)", stage: university, institution: "Dominican studium, Paris; Cologne", years: "1245–1256", ages: "c. 20–31", certainty: 1.0, cites: [{source: S2, locator: "§1.1"}, {source: S3, locator: "§1.a"}, {source: S1, locator: "Studies in Paris"}], how_known: "Three sources agree."}
  early_mathematics: {value: "other", ages: "c. 14–19", description: "IEP says theology training at a 13th-century university began with the seven liberal arts, including the quadrivium (arithmetic, geometry, music, astronomy), and places this at Naples from 1239. No record of what mathematics he actually studied was found.", certainty: 0.5, cites: [{source: S3, locator: "§1.a"}], how_known: "A scholarly account of the usual curriculum, not of his own record: scholarly reconstruction, 0.5."}
  early_geometric_style_reasoning: {value: "Aristotelian logic (the 'old' and 'new' logic of the Organon) as part of the arts course at Naples from about age 14; no specific record of his own logic study was found.", certainty: 0.5, cites: [{source: S3, locator: "§1.a"}], how_known: "IEP describes the logic then taught and says he read Aristotle at Naples. Reconstruction, 0.5. Facts only; the Lane B reading is in lane_b."}
  early_science_exposure:
    - {value: "Met the scientific and philosophical works newly translated from Greek and Arabic at the University of Naples", year: "1239–1244", age: "c. 14–19", certainty: 1.0, cites: [{source: S1, locator: "Early years"}, {source: S3, locator: "§1.a"}], how_known: "Two sources."}
  key_early_reading: [{value: UNKNOWN, how_known: "No named early book in S1–S3. Aristotle at Naples is recorded under schooling."}]
  childhood_mentors:
    - {value: "Peter of Ireland, who may have introduced him to Aristotle at Naples", name: "Peter of Ireland", years: "1239–1244", certainty: 0.5, cites: [{source: S3, locator: "§1.a ('perhaps introduced to him by Peter of Ireland')"}], how_known: "One source, hedged."}
  languages_in_childhood: {value: [Italian vernacular, Latin], certainty: 0.5, cites: [{source: S3, locator: "§1.a (education at Monte Cassino)"}], how_known: "Latin from his monastic schooling; the local vernacular is assumed, not stated. Reconstruction."}
  notable_events:
    - {value: "Left Monte Cassino when Frederick II expelled the monks", year: 1239, age: "c. 14", certainty: 1.0, cites: [{source: S1, locator: "Early years"}, {source: S3, locator: "§1.a"}], how_known: "Two sources (S3 gives the Naples start in 1239)."}
    - {value: "Joined the Dominicans (habit received April 1244); his family seized him and held him at the family castle for about a year before letting him go", year: "1244–1245", age: "c. 19–20", certainty: 1.0, cites: [{source: S3, locator: "§1.a"}, {source: S1, locator: "Early years; Studies in Paris"}, {source: S2, locator: "§1.1"}], how_known: "Three sources agree."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1252–1273", certainty: 1.0, cites: [{source: S3, locator: "§1.a; §1.b"}, {source: S2, locator: "§1.1"}], how_known: "From his Paris bachelorship to December 1273, when he stopped writing."}
  nominal_affiliations:
    - {value: "Dominican friar (Order of Preachers) and priest", years: "1244–1274", role: "friar; master of theology", certainty: 1.0, cites: [{source: S3, locator: "§1.a"}, {source: S2, locator: "§1.1"}, {source: S1, locator: "Early years"}], how_known: "Three sources."}
  self_described_science_religion_relation:
    value: "Philosophy built up by human reason is real knowledge, but salvation also needs truths revealed by God, some of which exceed reason. Revealed theology judges the other sciences: anything in them contrary to its truths is false. Reason serves faith, because grace does not destroy nature but perfects it."
    certainty: 1.0
    cites: [{source: S4, locator: "I q. 1 a. 1; a. 6 ad 2; a. 8 ad 2"}]
    how_known: "His own words in the Summa theologiae, a work written for teaching. Paraphrase; quotations are in statements."
  primary_system:
    value: CLASS_THEISM
    basis: written_profession
    certainty: 1.0
    cites: [{source: S4, locator: "I q. 2 a. 3; q. 3 a. 8; q. 8 a. 1; q. 9 a. 1"}, {source: S2, locator: "§2"}, {source: S1, locator: "opening paragraph"}]
    how_known: "His own published teaching works; written profession, so 1.0."
    rationale: "The coding guide defines CLASS_THEISM as the 'Aristotelian-Thomistic-Falsafa God: simple, immutable, known through reason'. Aquinas argues to God by reason (the five ways), and proves God 'entirely simple' and 'completely unchangeable' (S2, citing ST I q. 3 a. 7 and q. 9 a. 1). He is a founder of the tradition the code names, and the founders rule applies. The CLASS_THEISM system record lists Thomism as its reference form."
  secondary_system: {value: UNKNOWN, how_known: "No second system; his theology and philosophy are one system."}
  candidate_codes_considered:
    - {code: CLASS_THEISM, reason: "Chosen. God proved by reason, simple and immutable; nature an order of secondary causes; Aristotelian framework (S2, S4).", cites: [{source: S4, locator: "I q. 2 a. 3; q. 22 a. 3"}, {source: S2, locator: "§2"}]}
    - {code: CHRIST, reason: "Rejected as primary. He was a Dominican friar whose theology serves the Catholic faith, but the coding guide reserves CHRIST for when neither theism split fits better, and CLASS_THEISM is defined by his own system.", cites: [{source: S3, locator: "§1.a"}, {source: S4, locator: "I q. 1 a. 1"}]}
    - {code: CLTHEI, reason: "Rejected. He affirms miracles, but prayer does not change God: 'we pray not that we may change the Divine disposition' (S4, II-II q. 83 a. 2), and God is altogether immutable (I q. 9 a. 1). The CLTHEI God changes course in answer to petition.", cites: [{source: S4, locator: "II-II q. 83 a. 2; I q. 9 a. 1"}]}
    - {code: ARIST, reason: "Rejected. He builds on Aristotle, but adds creation and providence over every individual thing, which IEP notes Aristotle seemed to deny.", cites: [{source: S4, locator: "I q. 22 a. 2"}, {source: S3, locator: "§1.a"}]}
    - {code: PANT, reason: "Rejected. He calls the view that God is the world-soul, or the formal principle of all things, 'manifest untruth'.", cites: [{source: S4, locator: "I q. 3 a. 8"}]}
  lio_axes:
    A_locus:
      value: 1
      basis: written_profession
      certainty: 1.0
      cites: [{source: S4, locator: "I q. 3 a. 8; q. 8 a. 1"}, {source: S2, locator: "§2"}]
      how_known: "Summa theologiae; written profession, so 1.0."
      rationale: "Leans to the transcendent-person pole. God is the first efficient cause, not the world-soul and not the form or matter of anything (I q. 3 a. 8), and has intellect and will. But he is in all things, 'as an agent is present to that upon which it works' (I q. 8 a. 1), and his personhood is spoken of by analogy. So 1, not 0. This matches the CLASS_THEISM system record (A 1)."
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.7
      cites: [{source: S4, locator: "I q. 22 a. 3; q. 105 a. 5–7; II-II q. 83 a. 2"}, {source: S1, locator: "Years at the papal Curia"}, {source: S3, locator: "§2 (SCG I.6 on miracles)"}]
      how_known: "Summa theologiae, so written profession; certainty capped at 0.7 because the record names a plausible alternative score (CODING_GUIDE §3): God acting outside the order of nature (ST I q. 105 a. 6–8) is part of his own account of how God governs nature, and the theology-wide reading scores 2. Lowered from 1.0 after the lens audit (2026-10-02)."
      rationale: "Scored on his account of nature, as decision P6 asks. Leans LIO with a stated, limited exception. Nature runs by created causes with real powers of their own: he rejects the view that 'it is not fire that gives heat, but God in the fire', and holds that 'God works in things in such a manner that things have their proper operation' (I q. 105 a. 5). God governs lower things through higher ones so that 'the dignity of causality is imparted even to creatures' (I q. 22 a. 3), and petition does not change God (II-II q. 83 a. 2). Britannica says he held that nature 'has necessary laws' and avoided 'a naive recourse to the miraculous' (S1). The exception is the miracle: God 'can do something outside this order created by Him, when He chooses' (I q. 105 a. 6), and such works are miracles (a. 7). So 3, the score the CLASS_THEISM system record gives Thomism. Theology-wide reading (recorded as P6 asks): in his theology the biblical miracles are a working part of the case for the faith (S3, SCG I.6), which would score 2; that was this record's score before P6."
    C_ledger:
      value: 1
      basis: written_profession
      certainty: 1.0
      cites: [{source: S4, locator: "I-II q. 87 a. 1, 3; q. 114 a. 3; I q. 23 a. 3"}]
      how_known: "Summa theologiae; written profession, so 1.0."
      rationale: "Leans to personal reward and punishment: sins that destroy charity 'incur a debt of eternal punishment' (I-II q. 87 a. 3), and work done in grace merits eternal life 'condignly' (I-II q. 114 a. 3). The account is limited by its form: punishment follows because sin disturbs an order and 'the effect remains so long as the cause remains' (q. 87 a. 3), which is close to consequence. So 1, not 0. Under decision P7 (2026-10-02), the scope of salvation is recorded here, not on E: 'God does reprobate some' (I q. 23 a. 3), and salvation needs revealed truths (I q. 1 a. 1). Both fit a score of 1 and do not change it."
    D_authority:
      value: 1
      basis: written_profession
      certainty: 1.0
      cites: [{source: S4, locator: "I q. 1 a. 1, 6, 8"}, {source: S2, locator: "§2"}, {source: S1, locator: "Years at the papal Curia"}]
      how_known: "Summa theologiae; written profession, so 1.0."
      rationale: "Revelation outranks reason, with a large domain left to reason. Natural reason proves that God exists and much of what God is (S2), and 'grace does not destroy nature but perfects it' (I q. 1 a. 8). But some truths needed for salvation exceed reason and come only by revelation (I q. 1 a. 1), and 'Whatsoever is found in other sciences contrary to any truth of this science must be condemned as false' (I q. 1 a. 6). When they conflict revelation wins, so 1. The CLASS_THEISM system record scores the code 2; for Aquinas himself the stated ranking points to 1."
    E_scope:
      value: 3
      basis: written_profession
      certainty: 0.7
      cites: [{source: S4, locator: "I q. 22 a. 2 and ad 4, ad 5; q. 105 a. 5–7; II-II q. 83 a. 2"}]
      how_known: "Summa theologiae, so written profession (ceiling 1.0). Certainty 0.7 because the record names a plausible alternative score, 2 (CODING_GUIDE §3; see the rationale). Rescored under decision P7 (2026-10-02): before P7 this was 2, scored on the natural order and the scope of salvation together."
      rationale: "Scored on the world's order (decision P7). Leans LIO with a stated, limited exception. One providence covers every kind of thing: 'all things are subject to divine providence, not only in general, but even in their own individual selves' (I q. 22 a. 2), and individual irrational creatures do not 'escape the care of divine providence' (ad 5). Created causes keep 'their proper operation' (I q. 105 a. 5), and prayer does not change God's disposition (II-II q. 83 a. 2). The limited exception is the miracle: God 'can do something outside this order created by Him, when He chooses' (I q. 105 a. 6–7). So 3, the score CLASS_THEISM gives the code. Named alternative 2: providence covers the just 'in a certain more excellent way than over the wicked', since God 'prevents anything happening which would impede their final salvation' (I q. 22 a. 2 ad 4). That is a favour in this-world providence for a group, though it is aimed at salvation. Reprobation ('God does reprobate some', I q. 23 a. 3) and salvation needing revealed truths (I q. 1 a. 1) used to pull this score to 2. Under P7 they are scored on C (see C_ledger)."
  mid_basin:
    value: true
    certainty: 0.7
    cites: [{source: S4, locator: "I q. 3 a. 8; q. 8 a. 1; q. 22 a. 3; q. 105 a. 5–7"}]
    how_known: "P4 test as amended by P6 (2026-10-02): A_locus = 1 at 1.0 and B_cause = 3 at 0.7, B scored on his account of nature. Both at certainty >= 0.7, so true. The result turns on decision P6: before P6, B was scored on his whole theology (2), and the test had no branch (TODO). Certainty 0.7: mid_basin is no surer than the less certain of A and B (CODING_GUIDE §3; lens audit, 2026-10-02). F = 4, so first-rank is met. On his whole theology B would be 2, and the test would have no branch (see the B_cause rationale)."
  statements:
    - text: "Therefore some intelligent being exists by whom all natural things are directed to their end; and this being we call God."
      cites: [{source: S4, locator: "I q. 2 a. 3 (fifth way)"}]
      context: "Summa theologiae, First Part (written c. 1265–1268 per S3), the fifth of the five ways."
      axes: [A_locus, D_authority]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
      note: "English Dominican translation (2nd rev. ed., 1920) as transcribed by New Advent. Translated wording."
    - text: "Some have affirmed that God is the world-soul [...] Now all these contain manifest untruth; since it is not possible for God to enter into the composition of anything, either as a formal or a material principle."
      cites: [{source: S4, locator: "I q. 3 a. 8"}]
      context: "Whether God enters into the composition of other things. The omitted words list two further errors (God as the formal principle of all things; God as primary matter)."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "God is in all things; not, indeed, as part of their essence, nor as an accident, but as an agent is present to that upon which it works."
      cites: [{source: S4, locator: "I q. 8 a. 1"}]
      context: "Whether God is in all things."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "He governs things inferior by superior, not on account of any defect in His power, but by reason of the abundance of His goodness; so that the dignity of causality is imparted even to creatures."
      cites: [{source: S4, locator: "I q. 22 a. 3"}]
      context: "Whether God has immediate providence over everything."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "We must say, however, that all things are subject to divine providence, not only in general, but even in their own individual selves."
      cites: [{source: S4, locator: "I q. 22 a. 2"}]
      context: "Whether everything is subject to the providence of God. Just before, he rejects the views that corruptible things fall under providence only as species, and that humans are excepted from the generality of corruptible things (which he attributes to Rabbi Moses)."
      axes: [E_scope]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "God, however, extends His providence over the just in a certain more excellent way than over the wicked; inasmuch as He prevents anything happening which would impede their final salvation."
      cites: [{source: S4, locator: "I q. 22 a. 2 ad 4"}]
      context: "Same article, reply to the objection that God leaves humans to their own counsel. Ad 5 adds that 'individual irrational creatures' do not 'escape the care of divine providence'."
      axes: [E_scope, C_ledger]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
      note: "Basis of the named alternative E = 2."
    - text: "We must therefore understand that God works in things in such a manner that things have their proper operation."
      cites: [{source: S4, locator: "I q. 105 a. 5"}]
      context: "Whether God works in every agent. Just before, he rejects the view that 'it is not fire that gives heat, but God in the fire'."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "Wherefore God can do something outside this order created by Him, when He chooses, for instance by producing the effects of secondary causes without them, or by producing certain effects to which secondary causes do not extend."
      cites: [{source: S4, locator: "I q. 105 a. 6"}]
      context: "Whether God can do anything outside the established order of nature. Just before, he says God cannot act against the order that depends on the first cause, only outside the order of secondary causes."
      axes: [B_cause, E_scope]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "Wherefore those things which God does outside those causes which we know, are called miracles."
      cites: [{source: S4, locator: "I q. 105 a. 7"}]
      context: "Whether whatever God does outside the natural order is miraculous."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "For we pray not that we may change the Divine disposition, but that we may impetrate that which God has disposed to be fulfilled by our prayers"
      cites: [{source: S4, locator: "II-II q. 83 a. 2"}]
      context: "Second Part of the Second Part (c. 1271–1272 per S3), on whether it is becoming to pray."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "It was necessary for man's salvation that there should be a knowledge revealed by God besides philosophical science built up by human reason."
      cites: [{source: S4, locator: "I q. 1 a. 1"}]
      context: "Opening article of the Summa theologiae."
      axes: [D_authority, C_ledger]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "Whatsoever is found in other sciences contrary to any truth of this science must be condemned as false"
      cites: [{source: S4, locator: "I q. 1 a. 6 ad 2"}]
      context: "On whether sacred doctrine is wisdom; 'this science' is revealed theology."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "Since therefore grace does not destroy nature but perfects it, natural reason should minister to faith as the natural bent of the will ministers to charity."
      cites: [{source: S4, locator: "I q. 1 a. 8 ad 2"}]
      context: "On whether sacred doctrine is a matter of argument."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "Therefore whatever sins turn man away from God, so as to destroy charity, considered in themselves, incur a debt of eternal punishment."
      cites: [{source: S4, locator: "I-II q. 87 a. 3"}]
      context: "First Part of the Second Part (1271 per S3). The argument opens: 'sin incurs a debt of punishment through disturbing an order. But the effect remains so long as the cause remains.'"
      axes: [C_ledger]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "it is meritorious of life everlasting condignly"
      cites: [{source: S4, locator: "I-II q. 114 a. 3"}]
      context: "On whether a man in grace can merit eternal life condignly; 'it' is a meritorious work as it proceeds from the grace of the Holy Ghost."
      axes: [C_ledger]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "God does reprobate some."
      cites: [{source: S4, locator: "I q. 23 a. 3"}]
      context: "Whether God reprobates any man. Reprobation is God permitting some to fall away from eternal life, as part of providence."
      axes: [C_ledger]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "as regards the general principles whether of speculative or of practical reason, truth or rectitude is the same for all, and is equally known by all."
      cites: [{source: S4, locator: "I-II q. 94 a. 4"}]
      context: "Whether the natural law is the same in all men."
      axes: [E_scope]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "All that I have written seems to me like straw compared with what has now been revealed to me."
      cites: [{source: S2, locator: "§1.1"}]
      date: "1273"
      context: "Reported explanation for why he stopped writing in Naples, around December 1273."
      axes: [D_authority]
      kind: "reported speech"
      verified_against: "secondary quotation"
      verified_on: 2026-10-02
      note: "Reported speech: never a written profession. Not used for any score."
  changes_over_life:
    - {value: "Stopped writing, leaving the Summa theologiae unfinished, after a powerful religious experience while writing on the sacraments", year: 1273, age: "c. 48", certainty: 1.0, cites: [{source: S3, locator: "§1.a"}, {source: S2, locator: "§1.1"}], how_known: "Two sources agree. It ends his writing; it is not a change of system."}
  coder_notes: "Code and axes rest on his own published teaching, so certainties are high. The judgement calls are B, D and E. B is 3 on his account of nature (decision P6, 2026-10-02), matching the CLASS_THEISM system record; on his whole theology it would be 2, so B and mid_basin are held at 0.7 (CODING_GUIDE §3). D = 1, where the system record has 2 for the code as a whole (between Thomism and falsafa); that 2 is not a reading of Aquinas, whose stated ranking (I q. 1 a. 6) is explicit, so D stays at 1.0. mid_basin is true under the P4 test as amended by P6. E = 3 on the world's order (decision P7); the salvation reading that gave 2 is now on C, and the ad 4 favour to the just keeps E at 0.7. Translation: all quotations are from the 1920 English Dominican translation, not the Latin."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Southern Italian minor nobility; father of Lombard origin, mother of Norman heritage", certainty: 1.0, cites: [{source: S1, locator: "Early years"}], how_known: "One signed reference source."}
  religious_heritage_by_birth: {value: "Latin (Roman) Catholic", certainty: 0.7, cites: [{source: S1, locator: "Early years"}, {source: S3, locator: "§1.a"}], how_known: "Implied by his oblation at Monte Cassino; not stated in those words."}
  baptism_or_initiation: {value: TODO, note: "No baptism record in the sources read. Oblation at Monte Cassino (c. 1230) is recorded under childhood.schooling."}
  childhood_catechism: {value: TODO, note: "Not described in the sources read; Torrell's Saint Thomas Aquinas, vol. 1, ch. 1 is the place to look."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1252–1273", certainty: 1.0, cites: [{source: S3, locator: "§1.a; §1.b"}, {source: S2, locator: "§1.1; §1.2"}], how_known: "From the Sentences commentary to the break-off of the Summa theologiae in December 1273."}
  age_at_first_lasting_contribution: {value: 27, certainty: 0.7, cites: [{source: S3, locator: "References: Thomas' Works"}, {source: S2, locator: "§1.1"}], how_known: "On Being and Essence dated 1252–1253 (S3), with birth about 1225 (S2). Both ends are approximate, so the age may be off by a year or two."}
  first_evidence_of_lio_type_views: {value: "Summa theologiae, First Part: God governs lower things through higher ones and imparts 'the dignity of causality' to creatures; petition does not change God (II-II).", year: 1266, age: 41, certainty: 0.5, cites: [{source: S4, locator: "I q. 22 a. 3"}, {source: S3, locator: "References (ST I, 1265–1268)"}], how_known: "Year is the midpoint of 1265–1268 (S3), age approximate. Earliest work read for this record. The Sentences commentary (1252–1256) and the Summa contra gentiles (1259–1265) were not read and probably state the same views earlier, so 0.5."}
  lio_views_relative_to_major_work: {value: "during major work", rationale: "His order of secondary causes is set out inside the major works themselves; no earlier writings exist, since his writing career is the major-work period.", certainty: 0.7, cites: [{source: S4, locator: "I q. 22 a. 3"}, {source: S2, locator: "§1.2"}], how_known: "Dated works; earlier works not read."}
  worldview_during_major_work: {value: "A Dominican friar and master of theology throughout; the Summa theologiae states the same theism from start to finish. No change of view is recorded.", certainty: 1.0, cites: [{source: S3, locator: "§1.a"}, {source: S2, locator: "§1.1"}], how_known: "Three sources agree on his career; the texts read are consistent."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "His theology is set out as a science in Aristotle's sense, reasoning from principles (I q. 1 a. 2), in the fixed question–objection–reply form of the schools (S1). The form is logical and deductive, not geometrical, and his nature has a stated exception for miracles (I q. 105 a. 6), so 'partly'.", certainty: 0.5, cites: [{source: S4, locator: "I q. 1 a. 2; q. 105 a. 6"}, {source: S1, locator: "Years at the papal Curia (literary forms)"}], how_known: "Coder's reading of the form of the Summa."}
  form_acquired: {value: "through the profession", rationale: "The question-and-disputation form is the method of the 13th-century university, learned at Paris and Cologne from about age 20. He met Aristotle's logic at Naples at about 14 to 19 (S3), which would support 'childhood or adolescence' instead.", certainty: 0.5, cites: [{source: S3, locator: "§1.a"}, {source: S1, locator: "Years at the papal Curia"}], how_known: "Reconstruction; no record of his own logic study."}
  circle_present: {value: "no", rationale: "He calls the world-soul view 'manifest untruth' and denies that God enters into the composition of anything; God is in things as an agent, not as part of their essence.", certainty: 0.7, cites: [{source: S4, locator: "I q. 3 a. 8; q. 8 a. 1"}], how_known: "His own text."}
  reading: "As belief, not finding: the form is present in part (a deductive, Aristotelian science of theology) and was learned through the university, with no circle. The record does not test H1."
  notes: ""

institutions:
  - {value: "Abbey of Monte Cassino (Benedictine)", role: oblate, years: "c. 1230–1239", kind: "religious body", certainty: 1.0, cites: [{source: S1, locator: "Early years"}, {source: S3, locator: "§1.a"}], how_known: "Two sources."}
  - {value: "Order of Preachers (Dominicans)", role: "friar and priest", years: "1244–1274", kind: "religious body", certainty: 1.0, cites: [{source: S3, locator: "§1.a"}, {source: S2, locator: "§1.1"}], how_known: "Three sources."}
  - {value: "University of Paris", role: "student; bachelor of the Sentences (1252–1256); regent master in theology (1256–1259, 1268–1272)", years: "1245–1272", kind: university, certainty: 1.0, cites: [{source: S2, locator: "§1.1"}, {source: S3, locator: "§1.a"}, {source: S1, locator: "Studies in Paris"}], how_known: "Three sources."}
  - {value: "Dominican studium, Cologne", role: "student and assistant to Albert the Great", years: "1248–1252", kind: university, certainty: 1.0, cites: [{source: S2, locator: "§1.1"}, {source: S1, locator: "Studies in Paris"}], how_known: "Two sources; IEP calls it the University of Cologne."}
  - {value: "Papal Curia", role: "theological adviser and lecturer", years: "1259–1268", kind: "religious body", certainty: 0.7, cites: [{source: S1, locator: "Years at the papal Curia"}], how_known: "One source for the role; S3 lists his Italian posts (Naples, Orvieto, Rome)."}
  - {value: "Dominican studium, Naples", role: "teacher", years: "1272–1273", kind: university, certainty: 1.0, cites: [{source: S3, locator: "§1.a"}, {source: S2, locator: "§1.1"}], how_known: "Two sources."}

collaborators:
  - {value: "Albert the Great (Albertus Magnus)", relation: teacher, note: "Dominican master; Thomas studied under him and went with him to Cologne as his assistant. Not on the roster.", years: "1245–1252", certainty: 1.0, cites: [{source: S1, locator: "Studies in Paris"}, {source: S2, locator: "§1.1"}, {source: S3, locator: "§1.a"}], how_known: "Three sources; they differ on whether he studied under Albert in Paris (S1, S3) or only from Cologne (S2)."}
  - {value: "Peter of Ireland", relation: teacher, note: "may have introduced him to Aristotle at Naples", years: "1239–1244", certainty: 0.5, cites: [{source: S3, locator: "§1.a"}], how_known: "One source, hedged."}
  - {value: "Aristotle", roster_id: aristotle, relation: "influenced by", note: "he wrote commentaries on Aristotle's main works and reworked his philosophy within Christian theology", certainty: 1.0, cites: [{source: S2, locator: "introduction; §1.1"}, {source: S1, locator: "opening paragraph"}], how_known: "Three sources."}
  - {value: "Augustine of Hippo", roster_id: augustine-of-hippo, relation: "influenced by", note: "an authority cited throughout; SEP places him at the summit of the tradition running back to Augustine", certainty: 1.0, cites: [{source: S2, locator: "introduction"}, {source: S3, locator: "§1.b"}], how_known: "Two sources."}
  - {value: "Ibn Sina (Avicenna)", roster_id: ibn-sina, relation: "influenced by", note: "followed Ibn Sina's account of the internal senses", certainty: 1.0, cites: [{source: S2, locator: "§6"}, {source: S3, locator: "§1.a"}], how_known: "Two sources."}
  - {value: "Ibn Rushd (Averroes)", roster_id: ibn-rushd, relation: "rival or critic", note: "Thomas opposed the reading of Averroes taken up at Paris, including a single intellect for all humans", certainty: 1.0, cites: [{source: S2, locator: "§6"}, {source: S1, locator: "Years at the papal Curia"}], how_known: "Two sources."}
  - {value: "Siger of Brabant", relation: "rival or critic", note: "leader of the Paris Averroists from 1266", years: "1266–1272", certainty: 0.7, cites: [{source: S1, locator: "Years at the papal Curia"}], how_known: "One source read for the dispute."}
  - {value: "Bonaventure", relation: "rival or critic", note: "Franciscan colleague at Paris; in 1273 criticized philosophy as distinct from theology and 'the notion of a physical nature that has determined laws'", years: "1273", certainty: 1.0, cites: [{source: S1, locator: "Last years at Naples"}, {source: S3, locator: "§5"}], how_known: "Two sources (S3 on angels and spiritual matter)."}
  - {value: "Moses Maimonides", roster_id: maimonides, relation: other, note: "cited as 'Rabbi Moses' on providence (I q. 22 a. 2); Thomas disagrees with his view of names for God", certainty: 1.0, cites: [{source: S4, locator: "I q. 22 a. 2"}, {source: S3, locator: "§6"}], how_known: "His own text and one reference source."}
  - {value: "Reginald of Piperno", relation: "student or assistant", note: "his confessor and assistant, who urged him to keep writing after December 1273", certainty: 1.0, cites: [{source: S3, locator: "§1.a"}], how_known: "One source."}

review:
  roster_status_reason: {value: "Core in v7.1 and carried into v8; F = 4 (named by Claude, DeepSeek, GPT and Grok).", certainty: 1.0, cites: [{source: S5, locator: "roster.csv, rank 135"}], how_known: "Study roster."}
  controversies:
    - {value: "Some of his views were controversial in his lifetime and after: some of the 219 propositions condemned at Paris in 1277 touched his teaching", certainty: 1.0, cites: [{source: S1, locator: "Last years at Naples"}, {source: S2, locator: "§9"}], how_known: "Two sources."}
  data_quality_flags:
    - "Birth year: Britannica 1224/25, SEP 'around the year 1225', IEP 1224/6 and 'between 1224 and 1226'. The record uses 1225, approximate."
    - "Paris 1245–1248: Britannica and IEP say he studied under Albert in Paris; SEP says three years in Paris studying philosophy, then Cologne under Albert from 1248."
    - "Monte Cassino: IEP gives ages about 5 to 15; Britannica 'nine years' ending 1239 (about ages 5–14)."
    - "Siblings: SEP 'youngest of at least nine children'; IEP 'one of nine children' and 'youngest of four boys'."
    - "IEP gives Ibn Sina's dates as 'c. 980-1087'; he died in 1037. Likely a typo in IEP."
    - "Parents' names are not given in the sources read."
    - "All quotations are from the 1920 English Dominican translation (New Advent), not the Latin; SEP §1.1's 'straw' remark is reported speech and is not scored."
    - "Section numbers for S2 and S3 are the coder's reading of the fetched page headings."
  open_questions:
    - "Read the Summa contra gentiles III (providence, miracles) and the Sentences commentary to date his views earlier and to check B_cause."
    - "Torrell's biography for household practice, baptism and childhood instruction."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Marie-Dominique Chenu"
    citation: "Chenu, Marie-Dominique. \"St. Thomas Aquinas.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Saint-Thomas-Aquinas (pages: main page with Early years and Studies in Paris; Years at the papal Curia and return to Paris; Last years at Naples; Legacy)."
    url: "https://www.britannica.com/biography/Saint-Thomas-Aquinas"
    accessed: 2026-10-02
    reliability_note: "Signed article by a leading 20th-century Thomist historian; fact-checked by Britannica editors."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, lane_b, institutions, collaborators, review]
  - id: S2
    type: tertiary
    kind: encyclopedia
    author: "Robert Pasnau"
    year: 2022
    citation: "Pasnau, Robert. \"Thomas Aquinas.\" Stanford Encyclopedia of Philosophy, first published 7 December 2022. https://plato.stanford.edu/entries/aquinas/."
    url: "https://plato.stanford.edu/entries/aquinas/"
    accessed: 2026-10-02
    reliability_note: "Peer-reviewed reference entry by a specialist in medieval philosophy."
    used_for: [identity, basics, contribution, childhood, worldview, timing, institutions, collaborators, review]
  - id: S3
    type: tertiary
    kind: encyclopedia
    author: "Christopher M. Brown"
    citation: "Brown, Christopher M. \"Thomas Aquinas.\" Internet Encyclopedia of Philosophy. https://iep.utm.edu/thomas-aquinas/."
    url: "https://iep.utm.edu/thomas-aquinas/"
    accessed: 2026-10-02
    reliability_note: "Peer-reviewed reference entry. Its list of works with dates is used for the dating of the Summa parts. It has at least one date error (Ibn Sina)."
    used_for: [basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "Thomas Aquinas"
    year: 1920
    citation: "Thomas Aquinas. Summa Theologiae (Summa Theologica). Trans. Fathers of the English Dominican Province, 2nd and revised ed., 1920. Online edition by Kevin Knight, New Advent, https://www.newadvent.org/summa/. Pages read: I q. 1, 2, 3, 8, 9, 22, 23, 105, 115; I-II q. 87, 94, 114; II-II q. 83."
    url: "https://www.newadvent.org/summa/"
    accessed: 2026-10-02
    reliability_note: "His own teaching work, in a standard English translation. Written c. 1265–1273 in Latin. Quotations are the translators' English."
    used_for: [basics, contribution, worldview, timing, lane_b, collaborators]
  - id: S5
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv and data/roster/person_ids.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
---

# Thomas Aquinas

> Status: draft — unreviewed. Worldview coded CLASS_THEISM at 1.0; LIO axes A 1, C 1, D 1 at 1.0, and B 3 and E 3 at 0.7; mid_basin true at 0.7, a result that turns on decision P6 (B_cause scored on his account of nature).

## Summary

Thomas Aquinas (about 1225–1274) was an Italian Dominican friar and master of theology at Paris. He wrote the Summa contra gentiles and the Summa theologiae, the "classical systematization of Latin theology" [S1, opening paragraph]. He was canonized in 1323 and named a Doctor of the Church in 1567 [S1, Legacy]. Thomism is named after him [S2, §9].

## Life and work

He was born at the family castle of Roccasecca, near Aquino, the youngest of at least nine children [S2, §1.1; S1]. From about age 5 he was an oblate at Monte Cassino, until the monks were expelled in 1239 [S3, §1.a; S1, Early years]. At Naples he studied the arts and read Aristotle [S3, §1.a]. He joined the Dominicans in 1244. His family held him at home for about a year before letting him go [S3, §1.a]. He studied at Paris and then at Cologne under Albert the Great (1245–1252). He became a bachelor at Paris in 1252 and a master in 1256 [S2, §1.1; S1, Studies in Paris]. He taught in Italy from 1259 to 1268, at Paris again from 1268 to 1272, and at Naples from 1272 [S3, §1.a]. He stopped writing around December 1273 after a religious experience. He died at Fossanova on 7 March 1274, on his way to the Second Council of Lyon [S3, §1.a; S1, Last years at Naples].

## Contribution and impact

- 1252–1253: On Being and Essence; the distinction of essence and existence [S3; S2, §4].
- 1259–1265: Summa contra gentiles [S3].
- 1265–1273: Summa theologiae, with the five ways and the treatise on law [S3; S2, §2, §8].
- Commentaries on Aristotle, chiefly 1268–1273 [S2, §1.1].

He left more than eight million words [S2, §1.2]. Leo XIII's Aeterni Patris (1879) held him up as "the supreme model of the Christian philosopher" [S3, §1.a].

## Childhood and education

The family held a modest feudal domain and served Emperor Frederick II. His father was of Lombard origin, his mother of Norman heritage [S1, Early years]. His family hoped he would become abbot of Monte Cassino [S1; S3]. The arts course at Naples included the quadrivium and Aristotle's logic, but no record of his own mathematics was found [S3, §1.a].

## Adult working worldview

Reason can prove that God exists and much of what God is: simple, unchanging, eternal [S4, I q. 2–9; S2, §2]. God is not the world-soul or any part of things. He is in all things "as an agent is present to that upon which it works" [S4, I q. 3 a. 8; q. 8 a. 1]. God governs lower things through higher ones, so that "the dignity of causality is imparted even to creatures" [S4, I q. 22 a. 3]. Prayer does not change God's plan [S4, II-II q. 83 a. 2]. But Created things have "their proper operation" [S4, I q. 105 a. 5]. But God "can do something outside this order created by Him, when He chooses", and such works are miracles [S4, I q. 105 a. 6–7]. Revealed theology judges the other sciences [S4, I q. 1 a. 6]. Grave sin incurs eternal punishment, and grace merits eternal life [S4, I-II q. 87 a. 3; q. 114 a. 3]. Natural law is the same for all [S4, I-II q. 94 a. 4], but "God does reprobate some" [S4, I q. 23 a. 3].

Coding: CLASS_THEISM at 1.0. A 1, C 1, D 1 at 1.0 from written profession. E 3 at 0.7: scored on the world's order (decision P7). All things, individual creatures included, are under one providence, with the miracle as the limited exception [S4, I q. 22 a. 2; q. 105 a. 6]. The named alternative is 2, because providence favours the just [S4, I q. 22 a. 2 ad 4]. Reprobation is scored on C. B 3 at 0.7: it is scored on his account of nature (decision P6), and on his whole theology it would be 2, so certainty is capped. mid_basin true at 0.7; the result turns on P6.

## Heritage (context only)

Southern Italian minor nobility, Lombard and Norman by descent; Catholic by birth [S1, Early years]. Heritage is recorded for context only. It is not a worldview code.

## Timing

His writing career (1252–1273) is his major-work period. The earliest statement of his order of secondary causes read here is in the First Part of the Summa (1265–1268) [S4; S3]. Earlier works were not read.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. The form is present in part: theology is set out as a deductive science in the question-and-reply method of the universities. It was learned through the profession. There is no circle: he rejects the world-soul [S4, I q. 1 a. 2; q. 3 a. 8].

## Open questions

- Read the Summa contra gentiles III and the Sentences commentary for earlier dates and a check on B.
- Torrell's biography for household practice, baptism and early instruction.

## Research log

- 2026-10-02: Read Britannica (S1: main page and three subpages), SEP "Thomas Aquinas" (S2) and IEP "Thomas Aquinas" (S3). Read thirteen questions of the Summa theologiae in the New Advent transcription of the 1920 English Dominican translation (S4). Wikipedia not used. Every quotation was checked word for word against the fetched text with a script (verify_quotes.py) before commit. Torrell, the Leonine edition and the Latin text were not read.
- 2026-10-02 (P7): E_scope rescored on the world's order. Re-fetched I q. 22 (New Advent, S4) and checked the two new I q. 22 a. 2 quotations word for word against the page text. No new sources.
