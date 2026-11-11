---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 8
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, second batch: physical science 1600–1950)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages and translations"
  collected_on: 2026-10-02
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to physics. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (second batch, RUNBOOK §1 order). Basics from SEP (Miller, after Machamer), Britannica (Van Helden) and MacTutor. Worldview from the Letter to the Grand Duchess Christina (1615) in Drake's translation, read in two copies (Fordham excerpt; a course selection with the Joshua section). Coded CHRIST (Catholic) at 0.7. A 1 (0.7), B 3 (0.7), C 1 (0.5), D 2 (0.7), E 3 (0.7). mid_basin true. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit, batch 2 (two blind runs at e648145). Findings #69 (and #55, #57, #60): the 'inexorable and immutable' sentence is in the Fordham paragraph beginning 'This being granted…', not 'With regard to this argument…'; locators fixed in the statement, B_cause and E_scope (S5 p. 4 was already right). S4 is no longer described as Drake's translation: its translator and provenance are unknown and its wording differs from S5 in places (finding #70 note). Finding #62: self_described_science_religion_relation certainty 1.0 → 0.7 (secondary quotations cannot by themselves support 1.0, §7). Axis scores, primary_system and mid_basin unchanged. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Schema 1.1 → 1.2 (decision P8 adds basis recorded_interview and statement kind 'recorded interview'); no content change."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit, batch 4 (two blind runs at b21655b). Decision P12 recheck: first_lasting_contribution_year 1610 → 1609 (start year of the listed 1609–1610 telescopic discoveries), age 46 → 45; the 1604 alternative is kept (P13 note added). Era unchanged. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Stage 3 lens-audit rulings applied to the batch's other records (OPEN_DECISIONS P14–P28, v8's picks, 2026-10-02). Schema 1.2 → 1.3. One reliable source caps a fact at 0.7; derived fields take the lowest certainty of their inputs; kind lists (P21: research institute, school stage and run_by, scholarly edition). Full before → after list: reports/stage3_rulings_changes.csv. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Span alignment (P29, P30 and its addendum): timing.major_work_period 1604–1638 → 1609–1638; worldview.working_years 1589–1642 → 1609–1638, equal to the span (P30 addendum f); evidence for every headline value checked against the span; no value or certainty changed. Listed in reports/p30_span_alignment.csv. Not reviewed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #31, next-50 batch). Needs were already dark and corroborated on A and B; still deepen for P47, gaps, solidify. Opened Finocchiaro The Essential Galileo (Hackett 2008) scholarly edition: Letter to Castelli (1613) §4.1, Letter to Christina (1615) §4.2, Assayer (1623) book-of-nature passage. Re-verified inexorable/immutable Nature, divine Word, senses/intellect, heaven-goes, Joshua miracle against Finocchiaro; Castelli is the earlier independent letter with the same Nature-laws wording. Wikipedia EN dual-sources bio. P47 source_quality on every source. support: corroborated on A/B/D/E (P48). Scores unchanged: A 1 @0.7 (alt 0), B 3 @0.7 (alt 4), C 1 @0.5, D 2 @0.7, E 3 @0.7; CHRIST @0.7; mid_basin true @0.7. Chart-moving NO (already dark filled mid-basin). No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: galilei-galileo
  display_name: "Galileo Galilei"
  roster:
    canonical_name: "Galileo Galilei"
    rank: 31
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: physics
    field_bucket: physics
  full_name: {value: "Galileo Galilei", certainty: 1.0, cites: [{source: S1, locator: "§2"}, {source: S2, locator: "heading"}, {source: S8, locator: "lead (Galileo di Vincenzo Bonaiuti de' Galilei)"}], how_known: "SEP + Britannica short form; Wikipedia EN gives the longer birth form as lead."}
  native_name: {value: "Galileo Galilei (Italian)", certainty: 0.7, cites: [{source: S2, locator: "Quick Facts"}], how_known: "Same in Italian."}
  aliases:
    - {name: "Galilei-Galileo", kind: "roster alias"}
    - {name: "Galileo-Galilei", kind: "roster alias"}
    - {name: "Galileo", kind: other}

basics:
  birth:
    date: {value: "1564-02-15", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "§2"}, {source: S2, locator: "Quick Facts"}, {source: S8, locator: "infobox"}], how_known: "Three sources agree."}
    place: {value: "Pisa", modern_name: "Pisa, Italy", polity_then: "Duchy of Florence", certainty: 1.0, cites: [{source: S1, locator: "§2"}, {source: S2, locator: "Quick Facts"}, {source: S8, locator: "infobox"}], how_known: "Three sources agree."}
  death:
    date: {value: "1642-01-08", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "§2 ('but for problems with the date, see Machamer 1998b')"}, {source: S2, locator: "Quick Facts"}, {source: S8, locator: "infobox"}], how_known: "Three sources give 8 January 1642; SEP notes problems with the date, so 0.7."}
    place: {value: "Arcetri, near Florence", modern_name: "Arcetri, Florence, Italy", polity_then: "Grand Duchy of Tuscany", certainty: 1.0, cites: [{source: S2, locator: "Quick Facts"}, {source: S1, locator: "§2 (house arrest at his villa in Arcetri)"}, {source: S8, locator: "infobox"}], how_known: "Three sources."}
  first_lasting_contribution_year: {value: 1609, certainty: 0.7, cites: [{source: S1, locator: "§2 (telescope and discoveries, 1609; Sidereus nuncius, March 1610)"}, {source: S2, locator: "opening summary"}], how_known: "Start year of the earliest listed contribution, the telescopic discoveries (1609–1610), under decision P12; they were published in Sidereus nuncius (March 1610). Was 1610 until the batch 4 lens audit. SEP says the mechanics worked out earlier in Padua is his 'primary lasting contribution', but it was published only in 1638, so 0.7.", alternatives: [{value: 1604, cites: [{source: S1, locator: "§2; §3.1"}], note: "Mechanics worked out in Padua (from 1592), published 1638; the year of the law of fall is approximate. Under decision P13 the listed mechanics item is dated 1638, so 1604 stays an alternative (age 40)."}]}
  era_bucket: {value: "1600 to 1749", certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "Both candidate years fall in 1600 to 1749 (P2)."}
  region_of_birth: {value: "Southern Europe", certainty: 1.0, cites: [{source: S2, locator: "Quick Facts ('Pisa [Italy]')"}], how_known: "Italy is Southern Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "Pisa, Padua, Florence and Arcetri."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "As the sources record it."}
  languages_of_work: {value: [Italian, Latin], certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "Sidereus nuncius in Latin; the Dialogue and Two New Sciences in Italian."}
  occupations: {value: [mathematician, "natural philosopher", astronomer, "university lecturer", "court mathematician and philosopher"], certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "SEP."}

contribution:
  primary_domain: physics
  fields: {value: [mechanics, astronomy, "natural philosophy", "instrument making"], certainty: 1.0, cites: [{source: S1, locator: "§3"}, {source: S2, locator: "opening summary"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Telescopic discoveries (moons of Jupiter and others) and an improved telescope", year: "1609–1610", kind: discovery, lasting: "Britannica: they 'revolutionized astronomy'", certainty: 1.0, cites: [{source: S1, locator: "§2; §3.2"}, {source: S2, locator: "opening summary"}], how_known: "Two sources."}
    - {value: "New science of motion: the law of fall and projectile motion (Two New Sciences)", year: "1638", kind: theory, lasting: "SEP: 'his primary lasting contribution to physical science'", certainty: 0.7, cites: [{source: S1, locator: "§2; §3.3"}], how_known: "SEP."}
    - {value: "Mathematical natural philosophy: the book of nature written in the language of mathematics", year: "1623", kind: method, lasting: "Britannica: changed natural philosophy 'from a verbal, qualitative account to a mathematical one'", certainty: 1.0, cites: [{source: S1, locator: "§2; §4.1"}, {source: S2, locator: "opening summary"}, {source: S7, locator: "Assayer, Hackett pp. 183–184"}], how_known: "SEP + Britannica + Assayer in Finocchiaro."}
  evidence_of_impact:
    - {value: "Kepler 'lauded the work' (Sidereus nuncius) and the Collegio Romano confirmed its results", kind: "assessment by a later major figure", certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "SEP."}
  major_works:
    - {value: "Sidereus nuncius", year: 1610, kind: book, certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "SEP."}
    - {value: "Dialogue Concerning the Two Chief World Systems", year: 1632, kind: book, certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "SEP."}
    - {value: "Discourses and Mathematical Demonstrations Concerning Two New Sciences", year: 1638, kind: book, certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "SEP."}
    - {value: "Letter to Castelli (21 December 1613)", year: 1613, kind: other, certainty: 1.0, cites: [{source: S7, locator: "§4.1"}, {source: S1, locator: "§2"}], how_known: "Finocchiaro + SEP; circulated letter expanded into Christina."}
    - {value: "Letter to the Grand Duchess Christina (1615)", year: 1615, kind: other, certainty: 1.0, cites: [{source: S7, locator: "§4.2"}, {source: S1, locator: "§2"}], how_known: "Finocchiaro + SEP."}
    - {value: "The Assayer (Il Saggiatore)", year: 1623, kind: book, certainty: 1.0, cites: [{source: S7, locator: "Ch. 7"}, {source: S1, locator: "§2"}], how_known: "Finocchiaro + SEP."}
  honours:
    - {value: "Member of the Accademia dei Lincei", year: 1611, certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "SEP."}
  definition_fit: {value: "clearly meets", rationale: "Founding work in mechanics and telescopic astronomy.", certainty: 0.7, cites: [{source: S1, locator: "§2; §3"}], how_known: "Sources agree."}

childhood:
  family_religion: {value: "Catholic", certainty: 1.0, cites: [{source: S1, locator: "§2"}, {source: S3, locator: "Biography (Vallombrosa)"}], how_known: "Catholic Tuscany; schooled by Camaldolese monks. Not disputed."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father, Vincenzo Galilei, of noble heritage, a court musician, composer and music theorist of modest means", name: "Vincenzo Galilei", role: father, certainty: 1.0, cites: [{source: S1, locator: "§2"}, {source: S3, locator: "Biography"}], how_known: "Two sources."}
    - {value: "Mother, Giulia Ammannati, from Pisan cloth merchants", name: "Giulia Ammannati", role: mother, certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "SEP."}
  household_circumstances: {value: "Modest means; the family moved to Florence in 1572", certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "SEP."}
  schooling:
    - {value: "Private tutoring", stage: tutor, certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "SEP."}
    - {value: "Camaldolese monastery at Vallombrosa, then a Camaldolese school in Florence", stage: "grammar or secondary school", certainty: 1.0, cites: [{source: S1, locator: "§2"}, {source: S3, locator: "Biography"}], how_known: "Two sources.", run_by: "religious body"}
    - {value: "University of Pisa, medicine (not completed); Euclid with Ostilio Ricci", stage: university, years: "1580–1585", certainty: 0.7, cites: [{source: S1, locator: "§2"}, {source: S3, locator: "Biography (Ricci's Euclid course 1582–83)"}], how_known: "Two sources; the leaving year is not given in the text read."}
  early_mathematics: {value: TODO, note: "Euclid's Elements came in 1582–83, at 18–19, just past the childhood window (S3)."}
  early_geometric_style_reasoning: {value: "Euclid's Elements with Ricci at 18–19, after the childhood window", certainty: 0.7, cites: [{source: S3, locator: "Biography"}], how_known: "MacTutor."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [Italian, Latin], certainty: 0.7, cites: [{source: S3, locator: "Biography"}], how_known: "Monastic schooling implies Latin; not stated."}
  notable_events:
    - {value: "Became a novice at Vallombrosa, intending to join the Order; his father brought him home", certainty: 0.5, cites: [{source: S3, locator: "Biography"}], how_known: "MacTutor says he became a novice; SEP says he 'considered a religious vocation and may have started a novitiate'. Sources differ in confidence, so 0.5.", alternatives: [{value: "Considered a religious vocation; a novitiate is uncertain", cites: [{source: S1, locator: "§2"}], note: "SEP."}]}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1609–1638", certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "Equal to timing.major_work_period (P30 addendum f; span check 2026-10-02)."}
  nominal_affiliations:
    - {value: "Catholic; his daughters became nuns at the convent of St Matthew, Arcetri", role: member, certainty: 1.0, cites: [{source: S1, locator: "§2"}, {source: S3, locator: "Biography"}], how_known: "Two sources."}
  self_described_science_religion_relation:
    value: "Scripture and nature both come from God and cannot truly conflict; Scripture teaches salvation, 'how one goes to heaven, not how heaven goes'; sense experience and demonstrations decide physical questions, and Scripture is then read in their light."
    certainty: 0.7
    cites: [{source: S7, locator: "§4.1 Castelli; §4.2 Christina"}, {source: S4, locator: "letter"}, {source: S5, locator: "pp. 4–6"}]
    how_known: "Own circulated letters (Castelli 1613; Christina 1615) in Finocchiaro scholarly English (S7); web copies S4/S5 agree. English translation, so 0.7 not 1.0 (§7)."
  primary_system:
    value: CHRIST
    basis: written_profession
    certainty: 0.7
    cites: [{source: S7, locator: "§4.1 Castelli; §4.2 Christina"}, {source: S4, locator: "letter, 1615"}, {source: S1, locator: "§2; §5"}]
    how_known: "Castelli and Christina profess Catholic belief: Scripture can never lie or err; Holy Spirit teaches salvation; aim pious and Catholic (Christina). Written for circulation, so written_profession. 0.7: English translation; letters circulated in manuscript; 1633 abjuration coerced and unused (S1 §5)."
    rationale: "CHRIST use_when: writing shows Christian belief (scripture, church) without a more specific philosophical position. Branch: Catholic. Not CLASS_THEISM: no Thomist metaphysics of God. Not CLTHEI: no stress on petition beyond accepting scriptural miracles (Joshua)."
  secondary_system: {value: UNKNOWN, how_known: "No second system in sources read."}
  candidate_codes_considered:
    - {code: CLASS_THEISM, reason: "Rejected: no classical metaphysics of God in what was read."}
    - {code: DEISM, reason: "Rejected: he accepts revelation for salvation and the Joshua miracle.", cites: [{source: S7, locator: "§4.2 Joshua section"}]}
    - {code: CLTHEI, reason: "Rejected as primary: accepts Joshua miracle but does not stress ongoing petitionary religion beyond the creeds."}
  lio_axes:
    A_locus:
      value: 1
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S7, locator: "§4.1 Castelli; §4.2 Christina (Hackett pp. 104–117)"}, {source: S4, locator: "letter (Drake-family English)"}]
      how_known: "Castelli 1613 + Christina 1615 in Finocchiaro scholarly edition (S7), cross-checked to Fordham (S4). Named alternative 0; certainty 0.7."
      rationale: "Leans to the transcendent pole: Scripture and nature both derive from the divine Word / Godhead; God gives senses, language and intellect and imposes laws on Nature. God is not the world. Not 0: God is revealed in Nature's effects (Tertullian in Christina) without a give-and-take personalism. Named alternative 0 (creedal personal God, Faraday/Maxwell pattern). Independent source ids → corroborated (P48)."
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S7, locator: "§4.1 Castelli pp. 104–105; §4.2 Christina pp. 116–117, 142–143 (Joshua)"}, {source: S5, locator: "pp. 4, 10 (Drake selections)"}]
      how_known: "Castelli + Christina in Finocchiaro (S7); Drake selections (S5) agree on inexorable Nature and Joshua miracle. Named alternative 4; certainty 0.7."
      rationale: "Scored on his account of nature (P6). Leans to law: nature is 'inexorable and immutable' and never transgresses the laws imposed on her (Castelli; Christina). Stated limited exception: Joshua miracle is real — God willed the whole world system to remain motionless so 'the day miraculously got longer' (Christina §4.2). Alternative 4 (miracle read as outside ordinary nature so exceptionless law remains), so 0.7. Independent source ids → corroborated (P48)."
    C_ledger:
      value: 1
      basis: written_profession
      certainty: 0.5
      cites: [{source: S7, locator: "§4.2 Christina (salvation of souls; 'how one goes to heaven')"}, {source: S5, locator: "p. 6"}]
      how_known: "Christina treats salvation of souls only in passing, so 0.5."
      rationale: "Leans to the personal ledger: Scripture's primary purpose is the worship of God and the salvation of souls; Baronius line 'how one goes to heaven'. Judgement of persons assumed, not argued."
    D_authority:
      value: 2
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S7, locator: "§4.1 Castelli; §4.2 Christina (sense/demonstrations vs articles of faith)"}, {source: S4, locator: "paragraphs on Bible authority and senses"}]
      how_known: "Castelli + Christina (S7) and Fordham (S4). Two domains → D 2 (§3)."
      rationale: "Mixed, two domains. Sense experience and necessary demonstrations decide physics; Scripture is reserved for articles necessary for salvation that surpass all human reason. Even outside articles of faith, scriptural authority outranks mere probable human writings. Same pattern as Faraday, Maxwell and Newton."
    E_scope:
      value: 3
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S7, locator: "§4.1–§4.2 (one Nature under laws); Assayer Ch. 7 (mathematical universe)"}, {source: S1, locator: "§3.2; §4.1"}]
      how_known: "Letters + Assayer in Finocchiaro (S7) and SEP. Certainty 0.7 (Joshua favour as limited exception)."
      rationale: "Scored on the world's order (P7). Leans LIO: one immutable Nature under laws; Assayer — the universe is a book written in mathematical language. Stated limited exception: Joshua miracle lengthens a day for Israel's battle. Salvation scored on C, not here."
  mid_basin:
    value: true
    certainty: 0.7
    cites: [{source: S7, locator: "§4.1 Castelli; §4.2 Christina"}, {source: S5, locator: "pp. 4, 10"}]
    how_known: "P4 test: A_locus = 1 (≤ 1) at 0.7 and B_cause = 3 (≥ 3) at 0.7, both corroborated (P48), so true. Certainty is the lower of the two (P10). F = 5. Chart already dark filled; deepen did not move the dot."
  statements:
    - text: "For the Holy Scripture and nature both equally derive from the divine Word, the former as the dictation of the Holy Spirit, the latter as the most obedient executrix of God's commands; moreover, in order to adapt itself to the understanding of all people, it was appropriate for Scripture to say many things which are different from absolute truth in appearance and in regard to the meaning of the words; on the other hand, nature is inexorable and immutable, and she does not care at all whether or not her recondite reasons and modes of operations are revealed to human understanding, and so she never transgresses the terms of the laws imposed on her."
      cites: [{source: S7, locator: "§4.1 Letter to Castelli (1613), Hackett pp. 104–105"}]
      date: "1613-12-21"
      context: "Letter to Benedetto Castelli after the Medici-table dispute over Joshua; earlier independent statement of the Nature-laws claim later expanded in the Letter to Christina."
      axes: [B_cause, A_locus, D_authority]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Finocchiaro 2008 from National Edition 5:281–88."
    - text: "Therefore, I think that in disputes about natural phenomena one must begin not with the authority of scriptural passages, but with sense experiences and necessary demonstrations. For the Holy Scripture and nature derive equally from the Godhead, the former as the dictation of the Holy Spirit and the latter as the most obedient executrix of God's orders; moreover, to accommodate the understanding of the common people it is appropriate for Scripture to say many things that are different (in appearance and in regard to the literal meaning of the words) from the absolute truth; on the other hand, nature is inexorable and immutable, never violates the terms of the laws imposed upon her, and does not care whether or not her recondite reasons and ways of operating are disclosed to human understanding."
      cites: [{source: S7, locator: "§4.2 Letter to Christina (1615), Hackett pp. 116–117"}, {source: S4, locator: "Nature inexorable paragraph"}, {source: S5, locator: "p. 4"}]
      date: "1615"
      context: "Letter to the Grand Duchess Christina; expands Castelli. Drake (S4/S5) wording is close."
      axes: [B_cause, A_locus, D_authority]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Finocchiaro primary; S4/S5 Drake-family cross-check (S4 translator unnamed)."
    - text: "However, I do not think one has to believe that the same God who has given us senses, language, and intellect would want to set aside the use of these and give us by other means the information we can acquire with them."
      cites: [{source: S7, locator: "§4.2 Christina, Hackett p. 117"}, {source: S4, locator: "paragraph 'But I do not feel obliged…'"}]
      date: "1615"
      axes: [D_authority, A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Castelli parallel at S7 §4.1 p. 106 ('senses, language, and intellect')."
    - text: "That the intention of the Holy Spirit is to teach us how one goes to heaven and not how heaven goes."
      cites: [{source: S7, locator: "§4.2 Christina, Hackett p. 119"}, {source: S5, locator: "p. 6"}]
      date: "1615"
      context: "Christina quotes a person of the most eminent degree (Baronius tradition) with approval."
      axes: [C_ledger, D_authority]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
    - text: "Therefore, given that the sun is both the source of light and the origin of motion, and given that God wanted the whole world system to remain motionless for several hours as a result of Joshua's order, it was sufficient to stop the sun, and then its immobility stopped all the other turnings, so that the earth as well as the moon and the sun (and all the other planets) remained in the same arrangement; and during that whole time the night did not approach, and the day miraculously got longer."
      cites: [{source: S7, locator: "§4.2 Christina, Hackett pp. 142–143"}, {source: S5, locator: "p. 10"}]
      date: "1615"
      context: "Christina's Copernican reading of Joshua 10:12–13; accepts the miracle as real."
      axes: [B_cause, E_scope]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Stated limited exception under B 3 / E 3."
    - text: "Philosophy is written in this all-encompassing book that is constantly open before our eyes, that is the universe; but it cannot be understood unless one first learns to understand the language and knows the characters in which it is written. It is written in mathematical language, and its characters are triangles, circles, and other geometrical figures; without these it is humanly impossible to understand a word of it, and one wanders around pointlessly in a dark labyrinth."
      cites: [{source: S7, locator: "Ch. 7 From The Assayer (1623), Hackett pp. 183–184"}, {source: S3, locator: "Biography (Assayer quotation)"}]
      date: "1623"
      context: "Il Saggiatore, published letter to Virginio Cesarini; mathematical natural philosophy credo."
      axes: [E_scope]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Underwrites Lane B geometric_form_present and contribution method claim; not a God-locus score."
  changes_over_life:
    - {value: "Abjured Copernicanism under sentence of the Inquisition (22 June 1633); coerced, not used as evidence of belief", year: "1633", certainty: 0.7, cites: [{source: S1, locator: "§5"}], how_known: "SEP."}
  coder_notes: "CHRIST is a sourced system file. Deepen 2026-10-24: Finocchiaro Essential Galileo (S7) is the scholarly English for Castelli, Christina and Assayer; S4/S5 kept as Drake-family web cross-checks. Italian National Edition not page-checked. Dialogue not read for worldview. Chart-moving NO."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Tuscan; father of noble heritage", certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "SEP."}
  religious_heritage_by_birth: {value: "Catholic", certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "Undisputed."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: "Monastic schooling with the Camaldolese at Vallombrosa and Florence", certainty: 1.0, cites: [{source: S1, locator: "§2"}, {source: S3, locator: "Biography"}], how_known: "Two sources."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1609–1638", certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "From the telescopic discoveries (1609–1610; a range gives its start year, P12) to Two New Sciences (1638), the first and last listed lasting contributions (P29)."}
  age_at_first_lasting_contribution: {value: 45, certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "Born 15 February 1564; telescopic work from 1609, so 45. 40 if the 1604 mechanics is used."}
  first_evidence_of_lio_type_views: {value: "Letter to Castelli: Nature immutable under laws (expanded in Letter to Christina, 1615)", year: 1613, certainty: 0.7, cites: [{source: S7, locator: "§4.1 Castelli (21 Dec 1613)"}, {source: S1, locator: "§2"}], how_known: "Castelli opened this deepen (S7); Christina 1615 expands it."}
  lio_views_relative_to_major_work: {value: "during major work", rationale: "1613–1615 falls between Sidereus nuncius and the Dialogue.", certainty: 0.7, cites: [{source: S1, locator: "§2"}, {source: S7, locator: "§4.1–§4.2"}], how_known: "Dates."}
  worldview_during_major_work: {value: "Catholic, defending Copernicanism as compatible with Scripture", certainty: 0.7, cites: [{source: S7, locator: "§4.1–§4.2"}, {source: S1, locator: "§2"}], how_known: "His letters and SEP."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "Necessary demonstrations from geometry; Assayer: the universe is a book 'written in mathematical language' whose characters are 'triangles, circles, and other geometrical figures' (S7).", certainty: 0.7, cites: [{source: S7, locator: "Assayer, Hackett pp. 183–184"}, {source: S3, locator: "Biography (Assayer quotation)"}, {source: S1, locator: "§4.1"}], how_known: "Finocchiaro scholarly edition + MacTutor + SEP."}
  form_acquired: {value: "adulthood, before major work", rationale: "Euclid with Ricci at 18–19 (S3).", certainty: 0.5, cites: [{source: S3, locator: "Biography"}], how_known: "Coder's reading."}
  circle_present: {value: "no", rationale: "God imposes laws on Nature; God is not Nature.", certainty: 0.7, cites: [{source: S7, locator: "§4.1–§4.2"}, {source: S4, locator: "letter"}], how_known: "His own words."}
  reading: "As belief, not finding: form present, acquired at 18–19; no circle. The record does not test H1."
  notes: "Lane B separate from Lane A axis scores."

institutions:
  - {value: "University of Pisa", role: "lecturer in mathematics", years: "1589–1592", kind: university, certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "SEP."}
  - {value: "University of Padua", role: "chair of mathematics", years: "1592–1610", kind: university, certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "SEP."}
  - {value: "Medici court, Florence", role: "Chief Mathematician and Philosopher to the Grand Duke", years: "1610–1642", kind: "patron or funder", certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "SEP."}
  - {value: "Accademia dei Lincei", role: member, years: "1611–1642", kind: "academy or learned society", certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "SEP."}
collaborators:
  - {value: "Ostilio Ricci", relation: teacher, certainty: 1.0, cites: [{source: S1, locator: "§2"}, {source: S3, locator: "Biography"}], how_known: "Two sources."}
  - {value: "Benedetto Castelli", relation: "student or assistant", certainty: 0.7, cites: [{source: S1, locator: "§2"}, {source: S7, locator: "§4.1"}], how_known: "SEP + letter."}
  - {value: "Johannes Kepler", roster_id: kepler-johannes, relation: correspondent, note: "praised Sidereus nuncius", certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "SEP."}
  - {value: "Robert Bellarmine", relation: "rival or critic", note: "the 1616 admonition", certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "SEP."}

review:
  roster_status_reason: {value: "Core in v7.1 (F 4) and v8 (F 5, all five models).", certainty: 0.7, cites: [{source: S6, locator: "roster.csv, rank 31"}], how_known: "Study roster."}
  controversies:
    - {value: "Convicted of 'vehement suspicion of heresy' in 1633 and kept under house arrest", certainty: 0.7, cites: [{source: S1, locator: "§2; §5"}], how_known: "SEP."}
  data_quality_flags:
    - "Deepen 2026-10-24: worldview quotations re-verified against Finocchiaro Essential Galileo (S7); S4/S5 retained as Drake-family web cross-checks only."
    - "Death date: SEP flags 'problems with the date' (Machamer 1998b), unread."
    - "Novitiate: MacTutor says he became a novice; SEP is unsure."
    - "S4 does not name its translator: wording close to Drake 1957 (S5) but differs in places (lens audit, batch 2)."
  open_questions:
    - "Italian National Edition (Favaro) page-check of Castelli and Christina against Finocchiaro."
    - "Heilbron, Galileo (2010), for private piety (letters to Maria Celeste)."
    - "Dialogue (1632) for any shift in A/B wording during major work."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "David Marshall Miller (after Peter Machamer)"
    year: 2025
    citation: "Miller, David Marshall. \"Galileo Galilei.\" Stanford Encyclopedia of Philosophy, first published 4 March 2005 (Machamer), substantive revision 17 December 2025. https://plato.stanford.edu/entries/galileo/."
    url: "https://plato.stanford.edu/entries/galileo/"
    accessed: 2026-10-24
    reliability_note: "Peer-reviewed entry."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators, review]
  - id: S2
    type: tertiary
    kind: encyclopedia
    author: "Albert Van Helden"
    citation: "Van Helden, Albert. \"Galileo.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Galileo-Galilei."
    url: "https://www.britannica.com/biography/Galileo-Galilei"
    accessed: 2026-10-24
    reliability_note: "Signed article by a historian of astronomy."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution]
  - id: S3
    type: tertiary
    kind: encyclopedia
    author: "J. J. O'Connor and E. F. Robertson"
    citation: "O'Connor, J. J. and E. F. Robertson. \"Galileo Galilei.\" MacTutor History of Mathematics Archive. https://mathshistory.st-andrews.ac.uk/Biographies/Galileo/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Galileo/"
    accessed: 2026-10-24
    reliability_note: "Standard biographical archive; quotes The Assayer in translation."
    source_quality: "reference entry"
    used_for: [childhood, worldview, heritage, lane_b, collaborators]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "Galileo Galilei"
    year: 1615
    citation: "Galilei, Galileo. Letter to the Grand Duchess Christina of Tuscany, 1615 (excerpt, English translation). Internet Modern History Sourcebook, Fordham University."
    url: "https://sourcebooks.fordham.edu/mod/galileo-tuscany.asp"
    accessed: 2026-10-24
    reliability_note: "Excerpt; translator and provenance unknown. Drake-family English; wording close to S5 but not identical (lens audit batch 2). Kept as cross-check; Finocchiaro (S7) is the scholarly edition."
    source_quality: "unofficial web copy"
    used_for: [worldview, timing, lane_b]
  - id: S5
    type: primary
    kind: "published work by the subject"
    author: "Galileo Galilei"
    year: 1615
    citation: "Galilei, Galileo. Letter to Madame Christina of Lorraine, Grand Duchess of Tuscany (selections). Trans. Stillman Drake, Discoveries and Opinions of Galileo, New York: Anchor-Doubleday, 1957, pp. 173–216. Course selection PDF."
    url: "https://core1section11.files.wordpress.com/2013/01/galileo-lettertothegrandduchessselections.pdf"
    accessed: 2026-10-24
    reliability_note: "Course copy of Drake 1957 with typos; PDF page numbers not Drake's. Cross-check only; S7 Finocchiaro preferred."
    source_quality: "unofficial web copy"
    used_for: [worldview]
  - id: S6
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    reliability_note: "Study's own roster; used only for rank, F and status."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S7
    type: primary
    kind: "published work by the subject"
    author: "Galileo Galilei; ed. and trans. Maurice A. Finocchiaro"
    year: 2008
    citation: "Finocchiaro, Maurice A., ed. and trans. The Essential Galileo. Indianapolis: Hackett, 2008. §4.1 Letter to Castelli (1613), pp. 103–109; §4.2 Letter to the Grand Duchess Christina (1615), pp. 109–145; Ch. 7 From The Assayer (1623), pp. 179–189. Translations from Finocchiaro, The Galileo Affair (University of California Press, 1989) where noted."
    url: "https://hackettpublishing.com/the-essential-galileo"
    accessed: 2026-10-24
    reliability_note: "Scholarly edition from Italian National Edition (Favaro). Page numbers are Hackett 2008. Read Castelli, Christina (incl. Joshua), and Assayer book-of-nature passage."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview, timing, lane_b, contribution]
  - id: S8
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia. \"Galileo Galilei.\" https://en.wikipedia.org/wiki/Galileo_Galilei."
    url: "https://en.wikipedia.org/wiki/Galileo_Galilei"
    accessed: 2026-10-24
    reliability_note: "Dual-source for bio (full birth form; dates). Worldview not taken from Wikipedia."
    source_quality: "other"
    used_for: [identity, basics]
---

# Galileo Galilei

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Galileo Galilei (1564–1642), Tuscan mathematician and natural philosopher; telescopic discoveries 1609–1610; Two New Sciences 1638 [S1, S2]. Letter to Castelli (1613) and Letter to Christina (1615): nature "inexorable and immutable" under God's laws; Scripture teaches salvation; Joshua miracle accepted [S7]. Assayer: universe "written in mathematical language" [S7]. CHRIST (Catholic) at 0.7; A 1 / B 3 at 0.7 corroborated; mid_basin true. Deepen solidify; chart-moving no.

## Life and work

Born in Pisa, schooled by Camaldolese monks, left medicine for mathematics, chairs at Pisa and Padua, Medici court from 1610 [S1, S3, S8]. Condemned 1633; house arrest at Arcetri [S1].

## Contribution and impact

Telescopic astronomy, law of fall and projectile motion, mathematical natural philosophy [S1, S2, S7].

## Childhood and education

Son of Vincenzo Galilei [S1]. Camaldolese schooling; drawn to religious life [S3, S1]. Euclid with Ricci at 18–19 [S3].

## Adult working worldview

Castelli/Christina (Finocchiaro): nature inexorable and immutable under imposed laws; Scripture and nature from the divine Word; senses/intellect not set aside; Scripture teaches how one goes to heaven; Joshua miracle lengthens the day [S7; S4/S5 cross-check]. Assayer mathematical book of the universe [S7]. Scores: A 1 (0.7, corroborated), B 3 (0.7, corroborated), C 1 (0.5), D 2 (0.7), E 3 (0.7); mid_basin true.

## Heritage (context only)

Tuscan Catholic [S1]. Context only.

## Timing

First lasting contribution 1609 at 45 [S1]. LIO evidence from Castelli 1613 during major work [S7].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Geometric form present (Assayer) [S7, S3]; no circle.

## Open questions

- Favaro National Edition page-check; Heilbron private piety; Dialogue worldview lines.

## Research log

- 2026-10-02: SEP (Miller), Britannica (Van Helden), MacTutor, Fordham Christina excerpt, Drake course PDF with Joshua section.
- 2026-10-24: Deepen D1 — Finocchiaro *Essential Galileo* (Castelli, Christina, Assayer); Wikipedia EN dual-source; P47 on all sources; support fields. No fallacy_catalog.
