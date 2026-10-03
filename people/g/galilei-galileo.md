---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 5
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, second batch: physical science 1600–1950)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages and translations"
  collected_on: 2026-10-02
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (second batch, RUNBOOK §1 order). Basics from SEP (Miller, after Machamer), Britannica (Van Helden) and MacTutor. Worldview from the Letter to the Grand Duchess Christina (1615) in Drake's translation, read in two copies (Fordham excerpt; a course selection with the Joshua section). Coded CHRIST (Catholic) at 0.7. A 1 (0.7), B 3 (0.7), C 1 (0.5), D 2 (0.7), E 3 (0.7). mid_basin true. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit, batch 2 (two blind runs at e648145). Findings #69 (and #55, #57, #60): the 'inexorable and immutable' sentence is in the Fordham paragraph beginning 'This being granted…', not 'With regard to this argument…'; locators fixed in the statement, B_cause and E_scope (S5 p. 4 was already right). S4 is no longer described as Drake's translation: its translator and provenance are unknown and its wording differs from S5 in places (finding #70 note). Finding #62: self_described_science_religion_relation certainty 1.0 → 0.7 (secondary quotations cannot by themselves support 1.0, §7). Axis scores, primary_system and mid_basin unchanged. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Schema 1.1 → 1.2 (decision P8 adds basis recorded_interview and statement kind 'recorded interview'); no content change."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit, batch 4 (two blind runs at b21655b). Decision P12 recheck: first_lasting_contribution_year 1610 → 1609 (start year of the listed 1609–1610 telescopic discoveries), age 46 → 45; the 1604 alternative is kept (P13 note added). Era unchanged. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Stage 3 lens-audit rulings applied to the batch's other records (OPEN_DECISIONS P14–P28, v8's picks, 2026-10-02). Schema 1.2 → 1.3. One reliable source caps a fact at 0.7; derived fields take the lowest certainty of their inputs; kind lists (P21: research institute, school stage and run_by, scholarly edition). Full before → after list: reports/stage3_rulings_changes.csv. Not reviewed."}

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
  full_name: {value: "Galileo Galilei", certainty: 1.0, cites: [{source: S1, locator: "§2"}, {source: S2, locator: "heading"}], how_known: "Sources agree."}
  native_name: {value: "Galileo Galilei (Italian)", certainty: 0.7, cites: [{source: S2, locator: "Quick Facts"}], how_known: "Same in Italian."}
  aliases:
    - {name: "Galilei-Galileo", kind: "roster alias"}
    - {name: "Galileo-Galilei", kind: "roster alias"}
    - {name: "Galileo", kind: other}

basics:
  birth:
    date: {value: "1564-02-15", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "§2"}, {source: S2, locator: "Quick Facts"}], how_known: "Two sources agree."}
    place: {value: "Pisa", modern_name: "Pisa, Italy", polity_then: "Duchy of Florence", certainty: 1.0, cites: [{source: S1, locator: "§2"}, {source: S2, locator: "Quick Facts"}], how_known: "Two sources agree."}
  death:
    date: {value: "1642-01-08", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "§2 ('but for problems with the date, see Machamer 1998b')"}, {source: S2, locator: "Quick Facts"}], how_known: "Two sources give 8 January 1642; SEP notes problems with the date, so 0.7."}
    place: {value: "Arcetri, near Florence", modern_name: "Arcetri, Florence, Italy", polity_then: "Grand Duchy of Tuscany", certainty: 1.0, cites: [{source: S2, locator: "Quick Facts"}, {source: S1, locator: "§2 (house arrest at his villa in Arcetri)"}], how_known: "Two sources."}
  first_lasting_contribution_year: {value: 1609, certainty: 0.7, cites: [{source: S1, locator: "§2 (telescope and discoveries, 1609; Sidereus nuncius, March 1610)"}, {source: S2, locator: "opening summary"}], how_known: "Start year of the earliest listed contribution, the telescopic discoveries (1609–1610), under decision P12; they were published in Sidereus nuncius (March 1610). Was 1610 until the batch 4 lens audit. SEP says the mechanics worked out earlier in Padua is his 'primary lasting contribution', but it was published only in 1638, so 0.7.", alternatives: [{value: 1604, cites: [{source: S1, locator: "§2; §3.1"}], note: "Mechanics worked out in Padua (from 1592), published 1638; the year of the law of fall is approximate. Under decision P13 the listed mechanics item is dated 1638, so 1604 stays an alternative (age 40)."}]}
  era_bucket: {value: "1600 to 1749", certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "Both candidate years fall in 1600 to 1749 (P2)."}
  region_of_birth: {value: "Southern Europe", certainty: 1.0, cites: [{source: S2, locator: "Quick Facts ('Pisa [Italy]')"}], how_known: "Italy is Southern Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "Pisa, Padua, Florence and Arcetri."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "As the sources record it."}
  languages_of_work: {value: [Italian, Latin], certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "Sidereus nuncius in Latin; the Dialogue and Two New Sciences in Italian."}
  occupations: {value: [mathematician, "natural philosopher", astronomer, "university lecturer", "court mathematician and philosopher"], certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "SEP."}

contribution:
  fields: {value: [mechanics, astronomy, "natural philosophy", "instrument making"], certainty: 1.0, cites: [{source: S1, locator: "§3"}, {source: S2, locator: "opening summary"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Telescopic discoveries (moons of Jupiter and others) and an improved telescope", year: "1609–1610", kind: discovery, lasting: "Britannica: they 'revolutionized astronomy'", certainty: 1.0, cites: [{source: S1, locator: "§2; §3.2"}, {source: S2, locator: "opening summary"}], how_known: "Two sources."}
    - {value: "New science of motion: the law of fall and projectile motion (Two New Sciences)", year: "1638", kind: theory, lasting: "SEP: 'his primary lasting contribution to physical science'", certainty: 0.7, cites: [{source: S1, locator: "§2; §3.3"}], how_known: "SEP."}
    - {value: "Mathematical natural philosophy: the book of nature written in the language of mathematics", year: "1623", kind: method, lasting: "Britannica: changed natural philosophy 'from a verbal, qualitative account to a mathematical one'", certainty: 1.0, cites: [{source: S1, locator: "§2; §4.1"}, {source: S2, locator: "opening summary"}], how_known: "Two sources."}
  evidence_of_impact:
    - {value: "Kepler 'lauded the work' (Sidereus nuncius) and the Collegio Romano confirmed its results", kind: "assessment by a later major figure", certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "SEP."}
  major_works:
    - {value: "Sidereus nuncius", year: 1610, kind: book, certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "SEP."}
    - {value: "Dialogue Concerning the Two Chief World Systems", year: 1632, kind: book, certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "SEP."}
    - {value: "Discourses and Mathematical Demonstrations Concerning Two New Sciences", year: 1638, kind: book, certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "SEP."}
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
  working_years: {value: "1589–1642", certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "Lecturer at Pisa (1589) to death."}
  nominal_affiliations:
    - {value: "Catholic; his daughters became nuns at the convent of St Matthew, Arcetri", role: member, certainty: 1.0, cites: [{source: S1, locator: "§2"}, {source: S3, locator: "Biography"}], how_known: "Two sources."}
  self_described_science_religion_relation:
    value: "Scripture and nature both come from God and cannot truly conflict; Scripture teaches salvation, 'how one goes to heaven, not how heaven goes'; sense experience and demonstrations decide physical questions, and Scripture is then read in their light."
    certainty: 0.7
    cites: [{source: S4, locator: "paragraphs 'With regard to this argument…' to 'But I do not feel obliged…'"}, {source: S5, locator: "pp. 4–6"}]
    how_known: "His own Letter to the Grand Duchess Christina, written to circulate, but read only in English translation in two web copies, so every quotation is a secondary quotation and cannot by itself support 1.0 (§7). 0.7, as for Schrödinger's comparable relation."
  primary_system:
    value: CHRIST
    basis: written_profession
    certainty: 0.7
    cites: [{source: S4, locator: "letter, 1615"}, {source: S5, locator: "pp. 3–6"}, {source: S1, locator: "§2; §5"}]
    how_known: "The Letter to Christina professes Catholic belief: the Bible 'can never speak untruth', the Holy Spirit teaches salvation, and his aim is nothing 'that is not pious and Catholic'. Written for circulation (SEP: 'widely circulated'), so written_profession. 0.7, not 1.0: one work read, a letter in manuscript rather than a book he published, and the abjuration of 1633 (S1 §5) is coerced and not used."
    rationale: "CHRIST use_when: the person's writing shows Christian belief (scripture, church) without a more specific philosophical position. Branch: Catholic. Not CLASS_THEISM: the letter does not work out the simple God of Aquinas. Not CLTHEI: no stress on petition beyond the creeds."
  secondary_system: {value: UNKNOWN, how_known: "No second system in S1–S5."}
  candidate_codes_considered:
    - {code: CLASS_THEISM, reason: "Rejected: no classical metaphysics of God in what was read."}
    - {code: DEISM, reason: "Rejected: he accepts revelation for salvation and the Joshua miracle.", cites: [{source: S5, locator: "p. 10"}]}
  lio_axes:
    A_locus:
      value: 1
      basis: written_profession
      certainty: 0.7
      cites: [{source: S4, locator: "letter"}, {source: S5, locator: "pp. 4–5"}]
      how_known: "His circulated letter; capped at 0.7 because 0 is named below."
      rationale: "Leans to the transcendent pole: God is the author of both Scripture and Nature ('the holy Bible and the phenomena of nature proceed alike from the divine Word'), gives us 'senses, reason and intellect', and imposes laws on Nature. God is not the world. Not 0: the letter stresses God 'excellently revealed in Nature's actions' and does not describe a give-and-take relationship. Named alternative 0 (a personal God of the creeds, as Faraday and Maxwell are coded)."
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.7
      cites: [{source: S4, locator: "paragraph 'This being granted…'"}, {source: S5, locator: "pp. 4, 10"}]
      how_known: "His circulated letter; one work, so 0.7."
      rationale: "Scored on his account of nature (P6). Leans to law: 'Nature, on the other hand, is inexorable and immutable; she never transgresses the laws imposed upon her'. The stated limited exception: the miracle of Joshua is real; 'when God willed that at Joshua's command the whole system of the world should rest', 'day was miraculously prolonged', and he works out how it fits the Copernican system."
    C_ledger:
      value: 1
      basis: written_profession
      certainty: 0.5
      cites: [{source: S5, locator: "p. 6"}]
      how_known: "The letter refers to salvation of souls only in passing, so 0.5."
      rationale: "Leans to the personal ledger: Scripture's aim is 'our salvation', 'how one goes to heaven'. The judgement of persons is assumed, not discussed."
    D_authority:
      value: 2
      basis: written_profession
      certainty: 0.7
      cites: [{source: S4, locator: "paragraphs 'With regard to this argument…' to 'But I do not feel obliged…'"}]
      how_known: "His circulated letter; same pattern as Faraday, Maxwell and Newton (two domains), so 2 (§3 consistency)."
      rationale: "Mixed, two domains. Sense experience and necessary demonstrations decide physics, and Scripture must be read to agree with them. But the Bible's authority covers articles 'surpassing all human reasoning', and even outside faith 'this authority ought to be preferred over that of all human writings which are supported only by bare assertions or probable arguments'."
    E_scope:
      value: 3
      basis: written_profession
      certainty: 0.7
      cites: [{source: S4, locator: "paragraph 'This being granted…'"}, {source: S5, locator: "p. 10"}, {source: S1, locator: "§3.2"}]
      how_known: "His circulated letter and SEP on his celestial physics; one work, so 0.7."
      rationale: "Scored on the world's order (P7). Leans LIO: one immutable Nature, and his astronomy treats heavens and earth by the same mathematics. The stated limited exception: he accepts the Joshua miracle, a lengthened day granted 'at Joshua's command' during Israel's battle, a favour in events for a people. Salvation is scored on C, not here."
  mid_basin:
    value: true
    certainty: 0.7
    cites: [{source: S4, locator: "letter"}, {source: S5, locator: "pp. 4, 10"}]
    how_known: "P4 test: A_locus = 1 (≤ 1) at 0.7 and B_cause = 3 (≥ 3) at 0.7, so true. Certainty is the lower of the two. F = 5."
  statements:
    - text: "But Nature, on the other hand, is inexorable and immutable; she never transgresses the laws imposed upon her, or cares a whit whether her abstruse reasons and methods of operation are understandable to men."
      cites: [{source: S4, locator: "paragraph 'This being granted…'"}, {source: S5, locator: "p. 4"}]
      date: "1615"
      context: "Letter to the Grand Duchess Christina, in English translation; S4 and S5 (Drake) agree on this sentence (S5's line break splits 'in exorable')."
      axes: [B_cause, E_scope]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-02
      note: "English translation read in two web copies (S5 is Drake 1957; S4's translator is not named); the Italian original was not checked."
    - text: "But I do not feel obliged to believe that the same God who has endowed us with senses, reason and intellect has intended us to forego their use and by some other means to give us knowledge which we can attain by them."
      cites: [{source: S4, locator: "paragraph 'But I do not feel obliged…'"}]
      date: "1615"
      axes: [D_authority, A_locus]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-02
      note: "S5 has a variant ('that that same God … has intended to forgo their use'); S4's wording is used."
    - text: "I should judge that the authority of the Bible was designed to persuade men of those articles and propositions which, surpassing all human reasoning could not be made credible by science, or by any other means than through the very mouth of the Holy Spirit."
      cites: [{source: S4, locator: "paragraph 'From this I do not mean to infer…'"}]
      date: "1615"
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-02
    - text: "That the intention of the Holy Ghost is to teach us how one goes to heaven, not how heaven goes."
      cites: [{source: S5, locator: "p. 6"}]
      date: "1615"
      context: "Galileo quotes 'an ecclesiastic of the most eminent degree' with approval."
      axes: [C_ledger, D_authority]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-02
      note: "S4 has a typo ('heaven. not how')."
    - text: "the holy Bible and the phenomena of nature proceed alike from the divine Word"
      cites: [{source: S5, locator: "p. 4"}, {source: S4, locator: "letter"}]
      date: "1615"
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-02
    - text: "when God willed that at Joshua's command the whole system of the world should rest and should remain for many hours in the same state, it sufficed to make the sun stand still."
      cites: [{source: S5, locator: "p. 10"}]
      date: "1615"
      axes: [B_cause, E_scope]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-02
    - text: "nor in all that time did day decline towards night, for day was miraculously prolonged."
      cites: [{source: S5, locator: "p. 10"}]
      date: "1615"
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-02
  changes_over_life:
    - {value: "Abjured Copernicanism under sentence of the Inquisition (22 June 1633); coerced, not used as evidence of belief", year: "1633", certainty: 0.7, cites: [{source: S1, locator: "§5"}], how_known: "SEP."}
  coder_notes: "CHRIST is a sourced system file. All statements are English translations in web copies, so 'secondary quotation': S5 is Drake's 1957 translation; S4 (Fordham) names no translator and its wording is close to Drake's but not identical. The Letter to Castelli and the Dialogue were not read."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Tuscan; father of noble heritage", certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "SEP."}
  religious_heritage_by_birth: {value: "Catholic", certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "Undisputed."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: "Monastic schooling with the Camaldolese at Vallombrosa and Florence", certainty: 1.0, cites: [{source: S1, locator: "§2"}, {source: S3, locator: "Biography"}], how_known: "Two sources."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1604–1638", certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "From the Padua mechanics to Two New Sciences; start year approximate."}
  age_at_first_lasting_contribution: {value: 45, certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "Born 15 February 1564; telescopic work from 1609, so 45. 40 if the 1604 mechanics is used. Was 46 (Sidereus nuncius, 1610) until the batch 4 lens audit."}
  first_evidence_of_lio_type_views: {value: "Letter to Castelli, then Letter to Christina: Nature immutable under laws", year: 1615, certainty: 0.7, cites: [{source: S1, locator: "§2"}, {source: S4, locator: "letter"}], how_known: "The 1613–14 Letter to Castelli was not read; the 1615 letter is the earliest read."}
  lio_views_relative_to_major_work: {value: "during major work", rationale: "1615 falls between Sidereus nuncius and the Dialogue.", certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "Dates."}
  worldview_during_major_work: {value: "Catholic, defending Copernicanism as compatible with Scripture", certainty: 0.7, cites: [{source: S4, locator: "letter"}, {source: S1, locator: "§2"}], how_known: "His letter and SEP."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "Necessary demonstrations from geometry; the universe 'written in the language of mathematics' with 'triangles, circles, and other geometric figures' (S3, The Assayer, as quoted).", certainty: 0.7, cites: [{source: S3, locator: "Biography (The Assayer quotation)"}, {source: S1, locator: "§4.1"}], how_known: "His own words via MacTutor; SEP."}
  form_acquired: {value: "adulthood, before major work", rationale: "Euclid with Ricci at 18–19 (S3).", certainty: 0.5, cites: [{source: S3, locator: "Biography"}], how_known: "Coder's reading."}
  circle_present: {value: "no", rationale: "God imposes laws on Nature; God is not Nature.", certainty: 0.7, cites: [{source: S4, locator: "letter"}], how_known: "His own words."}
  reading: "As belief, not finding: form present, acquired at 18–19; no circle. The record does not test H1."
  notes: ""

institutions:
  - {value: "University of Pisa", role: "lecturer in mathematics", years: "1589–1592", kind: university, certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "SEP."}
  - {value: "University of Padua", role: "chair of mathematics", years: "1592–1610", kind: university, certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "SEP."}
  - {value: "Medici court, Florence", role: "Chief Mathematician and Philosopher to the Grand Duke", years: "1610–1642", kind: "patron or funder", certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "SEP."}
  - {value: "Accademia dei Lincei", role: member, years: "1611–1642", kind: "academy or learned society", certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "SEP."}
collaborators:
  - {value: "Ostilio Ricci", relation: teacher, certainty: 1.0, cites: [{source: S1, locator: "§2"}, {source: S3, locator: "Biography"}], how_known: "Two sources."}
  - {value: "Benedetto Castelli", relation: "student or assistant", certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "SEP."}
  - {value: "Johannes Kepler", roster_id: kepler-johannes, relation: correspondent, note: "praised Sidereus nuncius", certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "SEP."}
  - {value: "Robert Bellarmine", relation: "rival or critic", note: "the 1616 admonition", certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "SEP."}

review:
  roster_status_reason: {value: "Core in v7.1 (F 4) and v8 (F 5, all five models).", certainty: 0.7, cites: [{source: S6, locator: "roster.csv, rank 31"}], how_known: "Study roster."}
  controversies:
    - {value: "Convicted of 'vehement suspicion of heresy' in 1633 and kept under house arrest", certainty: 0.7, cites: [{source: S1, locator: "§2; §5"}], how_known: "SEP."}
  data_quality_flags:
    - "Death date: SEP flags 'problems with the date' (Machamer 1998b), unread."
    - "Novitiate: MacTutor says he became a novice; SEP is unsure."
    - "S4 does not name its translator: its note says the text 'was sent to me by a now misplaced correspondent, so its copyright status is uncertain'. Its wording is close to Drake 1957 (S5) but differs in places (e.g. 'the same God … has intended us to forego' vs S5 'that that same God … has intended to forgo'), so it is not treated as Drake's translation (lens audit, batch 2)."
  open_questions:
    - "Read the Letter to Castelli and the full Letter to Christina (Drake pp. 173–216) to check the Joshua passage against the book's pages."
    - "Read Heilbron, Galileo (2010), for his private piety (letters to Maria Celeste)."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "David Marshall Miller (after Peter Machamer)"
    year: 2025
    citation: "Miller, David Marshall. \"Galileo Galilei.\" Stanford Encyclopedia of Philosophy, first published 4 March 2005 (Machamer), substantive revision 17 December 2025. https://plato.stanford.edu/entries/galileo/."
    url: "https://plato.stanford.edu/entries/galileo/"
    accessed: 2026-10-02
    reliability_note: "Peer-reviewed entry."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators, review]
  - id: S2
    type: tertiary
    kind: encyclopedia
    author: "Albert Van Helden"
    citation: "Van Helden, Albert. \"Galileo.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Galileo-Galilei."
    url: "https://www.britannica.com/biography/Galileo-Galilei"
    accessed: 2026-10-02
    reliability_note: "Signed article by a historian of astronomy; first page read."
    used_for: [identity, basics, contribution]
  - id: S3
    type: tertiary
    kind: encyclopedia
    author: "J. J. O'Connor and E. F. Robertson"
    citation: "O'Connor, J. J. and E. F. Robertson. \"Galileo Galilei.\" MacTutor History of Mathematics Archive. https://mathshistory.st-andrews.ac.uk/Biographies/Galileo/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Galileo/"
    accessed: 2026-10-02
    reliability_note: "Standard biographical archive; quotes The Assayer in translation."
    used_for: [childhood, worldview, heritage, lane_b, collaborators]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "Galileo Galilei"
    year: 1615
    citation: "Galilei, Galileo. Letter to the Grand Duchess Christina of Tuscany, 1615 (excerpt, English translation). Internet Modern History Sourcebook, Fordham University."
    url: "https://sourcebooks.fordham.edu/mod/galileo-tuscany.asp"
    accessed: 2026-10-02
    reliability_note: "Excerpt; translator and provenance unknown ('sent to me by a now misplaced correspondent'). Wording close to Drake 1957 (S5) but not identical, so not cited as Drake. No page numbers, so paragraphs are located by their opening words."
    used_for: [worldview, timing, lane_b]
  - id: S5
    type: primary
    kind: "published work by the subject"
    author: "Galileo Galilei"
    year: 1615
    citation: "Galilei, Galileo. Letter to Madame Christina of Lorraine, Grand Duchess of Tuscany (selections). Trans. Stillman Drake, Discoveries and Opinions of Galileo, New York: Anchor-Doubleday, 1957, pp. 173–216. Course selection PDF, 'Galileo, Selections from Letter to the Grand Duchess'."
    url: "https://core1section11.files.wordpress.com/2013/01/galileo-lettertothegrandduchessselections.pdf"
    accessed: 2026-10-02
    reliability_note: "Course copy of Drake's translation with a few typos; page numbers are the PDF's own (pp. 1–11), not Drake's."
    used_for: [worldview]
  - id: S6
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
---

# Galileo Galilei

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Galileo Galilei (1564–1642), Tuscan mathematician and natural philosopher, made the telescopic discoveries of 1609–1610 and founded the new science of motion published in Two New Sciences (1638) [S1, §2]. His Letter to the Grand Duchess Christina (1615) holds that Nature "never transgresses the laws imposed upon her" while Scripture teaches salvation, and accepts the miracle of Joshua [S4, letter; S5, p. 10]. Coded CHRIST (Catholic) at 0.7; mid-basin true.

## Life and work

Born in Pisa, schooled by Camaldolese monks, he left medicine for mathematics, held chairs at Pisa and Padua, and from 1610 served the Medici [S1, §2; S3, Biography]. He was condemned in 1633 and lived under house arrest at Arcetri [S1, §5].

## Contribution and impact

Telescopic astronomy, the law of fall and projectile motion, and mathematical natural philosophy [S1, §2–§4; S2, opening summary].

## Childhood and education

Son of the musician Vincenzo Galilei [S1, §2]. He was taught by Camaldolese monks at Vallombrosa and was drawn to the religious life [S3, Biography; S1, §2]. Euclid came with Ricci at 18–19 [S3, Biography].

## Adult working worldview

"Nature, on the other hand, is inexorable and immutable; she never transgresses the laws imposed upon her" [S4]. God gave "senses, reason and intellect" and does not ask us to forgo them [S4]. Scripture teaches "how one goes to heaven, not how heaven goes" [S5, p. 6]. At Joshua's command God made the world rest and "day was miraculously prolonged" [S5, p. 10]. Scores: A 1 (0.7), B 3 (0.7), C 1 (0.5), D 2 (0.7), E 3 (0.7); mid_basin true.

## Heritage (context only)

Tuscan Catholic [S1, §2]. Context only.

## Timing

First lasting contribution 1609, the telescopic discoveries (published 1610), at 45 [S1, §2]. The 1615 letter falls during the major work.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Geometric form is present ("written in the language of mathematics") [S3, Biography]; no circle.

## Open questions

- Letter to Castelli; full Drake text; Heilbron on private piety.

## Research log

- 2026-10-02: Read SEP (Miller), Britannica (Van Helden, first page), MacTutor, the Fordham excerpt of the Letter to Christina and a course PDF of Drake's selections with the Joshua section. Quotations checked word for word against S4 or S5 as cited.
