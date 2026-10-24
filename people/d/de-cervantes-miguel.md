---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch U)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #117 / F4 rank 118). Goals: hunt prologues/dedications/letters for A/B; keep honest BELOW if only fiction (P42). Read in-span: Don Quixote I Prólogo 1605 (S5) — 'orden de naturaleza' as literary generation analogy, closing 'Dios te dé salud' formula; Novelas ejemplares Prólogo and Dedicatoria 1613 (S6) — love scenes 'medidos con la razón y discurso cristiano'; 'mi edad no está ya para burlarse con la otra vida'; closing 'Dios te guarde'; Guarde nuestro Señor. Don Quixote II Prólogo and Dedicatoria 1615 (S7) — '¡Válame Dios!', 'tentaciones del demonio', 'Cristo con todos', Lemos's 'cristiandad', 'Deo volente' (P42 formula). Wikipedia EN (S8, P50): birth/death align; Third Order Franciscans ~1613 noted as membership. P47 on S1–S8. A stays BELOW (formulas + Christian literary measure ≠ A1–A4 locus). B stays BELOW (orden de naturaleza / milagro not P16 law-vs-exception; not scientist P30). C stays BELOW (otra vida hope, no deserts). primary BELOW, CHRIST lead strengthened by in-span Novelas but still short of a code under ruling U2. mid BELOW. Chart-moving NO. No fallacy_catalog. No figures/. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Audit fixes for batch U (gs_59bb9fc_U run 1): Britannica byline corrected to Edward C. Riley (CE2). Ruling U2 (v8's call on the auditor's advice): primary_system CHRIST 0.5 -> BELOW_THRESHOLD, CHRIST the named lead; the last rites recorded in nominal_affiliations as practice; the dedication formulas treated as context (P42 will-preamble addendum, by analogy). Still not plotted."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch U, order P32: F 4, rank 118; taken in place of Louis Pasteur, already coded). Basics from Britannica (Edward C. Riley; author corrected in the batch U audit fixes). Worldview from his own dedication (19 April 1616) and prologue to Los trabajos de Persiles y Sigismunda (published 1617), read in the Calpe 1920 edition on Wikisource; after the span (P1 cap 0.5). Characters' words in the novels are not his (P42). Not a scientist (P30). primary_system CHRIST (0.5, alt BELOW_THRESHOLD); A BELOW_THRESHOLD; B BELOW_THRESHOLD; C BELOW_THRESHOLD; D UNKNOWN; E UNKNOWN; mid_basin BELOW_THRESHOLD. Not plotted. Draft, not reviewed."}

identity:
  id: de-cervantes-miguel
  display_name: "Miguel de Cervantes"
  roster:
    canonical_name: "Miguel de Cervantes"
    rank: 118
    F: 4
    models: [Claude, DeepSeek, Gemini, Grok]
    band: "core (3–4)"
    status: core
    field: literature
    field_bucket: literature
  full_name: {value: "Miguel de Cervantes Saavedra", certainty: 0.7, cites: [{source: S1, locator: "facts box (In full)"}], how_known: "Britannica."}
  native_name: {value: "Miguel de Cervantes Saavedra", certainty: 0.7, cites: [{source: S1, locator: "facts box"}], how_known: "Spanish; same as the full name."}
  aliases:
    - {name: "Cervantes-Miguel de", kind: "roster alias"}

basics:
  birth:
    date: {value: "1547-09-29", calendar: julian, certainty: 0.5, cites: [{source: S1, locator: "facts box (Born); body, first paragraph after the opening"}, {source: S8, locator: "Infobox / Biography"}], how_known: "Britannica: 'probably on September 29 (the day of San Miguel)'; baptized 9 October 1547 ('certainly'). Wikipedia EN assumes the same day (P50). Before the 1582 Gregorian reform in Spain, so Julian."}
    place: {value: "Alcalá de Henares", modern_name: "Alcalá de Henares, Madrid, Spain", polity_then: "Crown of Castile (Spain)", certainty: 0.7, cites: [{source: S1, locator: "facts box (Born)"}], how_known: "Britannica."}
  death:
    date: {value: "1616-04-22", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "facts box (Died)"}, {source: S8, locator: "Infobox / Later life and death"}], how_known: "Britannica and Wikipedia EN agree on 22 April 1616 NS (burial long misdated 23 April; P50)."}
    place: {value: "Madrid", modern_name: "Madrid, Spain", polity_then: "Crown of Castile (Spain)", certainty: 0.7, cites: [{source: S1, locator: "facts box (Died)"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1605, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Don Quixote, Part I (1605)."}
  era_bucket: {value: "1600 to 1749", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "1605 (P2)."}
  region_of_birth: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "facts box"}], how_known: "Spain (P3)."}
  region_of_work: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "body"}], how_known: "Spain (Madrid)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "body"}], how_known: "Pronouns in Britannica."}
  languages_of_work: {value: ["Spanish"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  occupations: {value: ["novelist, playwright and poet", "soldier", "royal messenger, commissary of provisions for the Armada, tax collector"], certainty: 0.7, cites: [{source: S1, locator: "opening; 'Soldier and slave'; question box on his living"}], how_known: "Britannica; the later posts from the question box only."}

contribution:
  fields: {value: ["novel", "short story", "drama", "poetry"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Don Quixote, Part I (El ingenioso hidalgo don Quijote de la Mancha)", year: 1605, kind: work, lasting: "translated into 'more than 60 languages'; critical discussion 'unabated since the 18th century' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    - {value: "Novelas ejemplares (Exemplary Stories)", year: 1613, kind: work, lasting: "'a few ... attain a level close to that of Don Quixote' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    - {value: "Don Quixote, Part II", year: 1615, kind: work, lasting: "as Part I (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica dates Don Quixote '(1605, 1615)'. Fiction, so not a scientist (P30)."}
  evidence_of_impact:
    - {value: "'the most important and celebrated figure in Spanish literature'; Don Quixote and Sancho Panza 'probably familiar visually to more people than any other imaginary characters in world literature'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works:
    - {value: "Los trabajos de Persiles y Sigismunda", year: 1617, certainty: 0.7, cites: [{source: S2, locator: "Dedicatorias, pp. 9–10"}], how_known: "Posthumous; dedication dated 19 April 1616. Not listed as lasting in the sources read."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "'the most important and celebrated figure in Spanish literature' (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father: a barber-surgeon who set bones and performed bloodlettings", certainty: 0.7, cites: [{source: S1, locator: "body, first paragraph after the opening"}], how_known: "Britannica."}
  household_circumstances: {value: "Fourth of seven children of a family of minor gentry origins 'come down in the world'; moved from town to town; may have been converso", certainty: 0.7, cites: [{source: S1, locator: "body, first paragraph after the opening"}], how_known: "Britannica."}
  schooling:
    - {value: "Possibly a pupil (or pupil-teacher) of Juan López de Hoyos, head of a municipal school in Madrid, who in 1569 called a Miguel de Cervantes his 'beloved pupil'; no university", stage: "grammar or secondary school", run_by: "state or municipal", years: "by 1569", certainty: 0.5, cites: [{source: S1, locator: "body, first paragraph after the opening"}], how_known: "Britannica; identity of the pupil not certain. Jesuit schooling is 'conjectural' (S1)."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "Juan López de Hoyos (if the same Cervantes), a man 'with Erasmist intellectual leanings'", certainty: 0.5, cites: [{source: S1, locator: "body, first paragraph after the opening"}], how_known: "Britannica."}
  languages_in_childhood: {value: ["Spanish"], certainty: 0.5, cites: [{source: S1, locator: "body"}], how_known: "Coder's reading."}
  notable_events:
    - {value: "Baptized 9 October 1547", certainty: 0.7, cites: [{source: S1, locator: "body, first paragraph after the opening"}], how_known: "Britannica ('certainly')."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1605–1615", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Baptized Catholic; ransomed from Algiers in 1580 with the aid of the Trinitarian friars", certainty: 0.7, cites: [{source: S1, locator: "body; 'Soldier and slave'"}, {source: S8, locator: "Military service and captivity"}], how_known: "Britannica and Wikipedia EN. Context, not a code."}
    - {value: "Joined the Franciscan Third Order (lay tertiary), about July 1613; professed in his house while ill, 2 April 1616 (secondary; membership)", certainty: 0.5, cites: [{source: S8, locator: "Later life and death"}], how_known: "Wikipedia EN (via Fitzmaurice-Kelly / standard biography). Membership/practice only; not a worldview code (CHRIST do_not_use_when)."}
    - {value: "Received extreme unction on 18 April 1616 ('Ayer me dieron la extremaunción, y hoy escribo ésta')", certainty: 0.7, cites: [{source: S2, locator: "Dedicatorias, p. 9"}], how_known: "His own dated dedication (19 April 1616). Practice at membership level, not a code (ruling U2; CHRIST do_not_use_when)."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing in his own voice read on the topic."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "Deepen D1: in-span Novelas ejemplares Prólogo (1613, S6) adds that his love scenes are 'medidos con la razón y discurso cristiano' and that at his age he is not one to 'burlarse con la otra vida'; DQ II (1615, S7) has conventional '¡Válame Dios!', 'Deo volente', praise of a patron's 'cristiandad'. These strengthen the CHRIST lead (Christian moral measure + seriousness about the afterlife) but still fall short of a scored profession of Christian doctrine: 'discurso cristiano' is literary propriety, not A1–A4 or creed; afterlife seriousness without Christ/salvation claim matches the Persiles generic 'otra vida' already ruled insufficient under U2. Sacraments, Third Order, and dedication formulas remain membership/practice/context (P42). Fiction and character speech stay out (P42). CHRIST remains the named lead."}
  secondary_system: {value: UNKNOWN, how_known: "One system (P29)."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Named lead strengthened (D1): in-span 'discurso cristiano' (S6), seriousness about 'la otra vida' (S6; Persiles S2), Third Order membership (S8), last rites (S2). Still not enough for a code under U2: no own-voice creed/locus profession."}
    - {code: CLTHEI, reason: "Rejected: 'milagro' (Persiles) and 'Deo volente' (DQ II) are figures/formulas, not stressed petition (P16 Austen addendum N/A)."}
  lio_axes:
    A_locus:
      value: BELOW_THRESHOLD
      cites: [{source: S6, locator: "Prólogo: 'discurso cristiano'; 'Dios te guarde'"}, {source: S5, locator: "Prólogo close: 'Dios te dé salud'"}, {source: S7, locator: "Prólogo / Dedicatoria: '¡Válame Dios!', 'Deo volente'"}, {source: S2, locator: "Dedicatorias: 'voluntad de los cielos'"}]
      how_known: "In-span and post-span own-voice God-talk checked. 'Discurso cristiano' (S6) measures the moral tone of his fiction, not a personal locus (A1–A4). Closing blessings and 'Deo volente' / 'voluntad de los cielos' are dedication/prologue formulas (P42 will-preamble analogy). Friend's counsel in DQ I Prólogo is framed dialogue, not his creed (P42). Evidence bears weakly toward a theistic cultural idiom but under 0.5 for scored locus → BELOW (P19)."
    B_cause:
      value: BELOW_THRESHOLD
      cites: [{source: S5, locator: "Prólogo open: 'orden de naturaleza… cada cosa engendra su semejante'"}, {source: S2, locator: "Dedicatorias, p. 10: 'milagro'"}]
      how_known: "Not a scientist (P30). DQ I 'orden de naturaleza' is a literary analogy (sterile ingenio begets a dry book), not a P16 claim that the physical world is lawful with or without miraculous exceptions. Persiles 'milagro' remains a figure for unlikely recovery (after span). No own-voice non-fiction nature-order profession found → BELOW (P19)."
    C_ledger:
      value: BELOW_THRESHOLD
      cites: [{source: S6, locator: "Prólogo: 'no… burlarse con la otra vida'"}, {source: S2, locator: "Prólogo, p. 13: 'contentos en la otra vida'"}]
      how_known: "In-span Novelas (S6) and Persiles (S2) take the afterlife seriously as hope/farewell, but say nothing of personal reward or punishment → BELOW."
    D_authority: {value: UNKNOWN, how_known: "Nothing on revelation against observation in his own voice read (P19). Friend's jest about padding margins with Scripture (DQ I) is framed dialogue (P42)."}
    E_scope: {value: UNKNOWN, how_known: "Nothing on favour for a group in the world's order read (P7, P19)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "P4 test: A and B are BELOW_THRESHOLD; neither is UNKNOWN."}
  statements:
    - text: "Ayer me dieron la extremaunción, y hoy escribo ésta; el tiempo es breve, las ansias crecen, las esperanzas menguan, y, con todo esto, llevo la vida sobre el deseo que tengo de vivir"
      cites: [{source: S2, locator: "Dedicatorias, p. 9"}]
      date: "1616-04-19"
      context: "Dedication of Persiles to the Conde de Lemos, opening with the old couplet 'Puesto ya el pie en el estribo'; dated Madrid, 19 April 1616, three days before his death."
      axes: []
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "Wikisource proofread transcription of the Calpe (Colección Universal) 1920 edition, vol. 1; printed page 9 (scan page 11)."
    - text: "Pero si está decretado que la haya de perder, cúmplase la voluntad de los cielos"
      cites: [{source: S2, locator: "Dedicatorias, pp. 9–10"}]
      date: "1616-04-19"
      context: "Same dedication; 'la' is his life."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "Across the page break (scan pages 11–12)."
    - text: "Si a dicha, por buena ventura mía, que ya no sería ventura, sino milagro, me diese el cielo vida, las verá"
      cites: [{source: S2, locator: "Dedicatorias, p. 10"}]
      date: "1616-04-19"
      context: "Same dedication, on works he hopes to finish (Semanas del jardín, Bernardo, the end of La Galatea)."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
    - text: "¡A Dios, gracias; a Dios, donaires; a Dios, regocijados amigos; que yo me voy muriendo, y deseando veros presto contentos en la otra vida!"
      cites: [{source: S2, locator: "Prólogo, p. 13"}]
      context: "Close of the Persiles prologue, after his account of meeting a student on the road from Esquivias; written in his last days."
      axes: [C_ledger]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "'A Dios' as spelled in this edition (adiós). Undated; written by April 1616."
    - text: "pero no he podido yo contravenir al orden de naturaleza, que en ella cada cosa engendra su semejante. Y así, ¿qué podía engendrar el estéril y mal cultivado ingenio mío, sino la historia de un hijo seco…"
      cites: [{source: S5, locator: "Prólogo, opening"}]
      date: "1605"
      context: "Authorial prologue to Don Quixote Part I; literary analogy for why the book is imperfect."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Wikisource 1905 edition. Not scored as P16: generation-of-like-from-like applied to books, not law-vs-miracle about nature."
    - text: "Y con esto, Dios te dé salud, y a mí no olvide. Vale."
      cites: [{source: S5, locator: "Prólogo, close"}]
      date: "1605"
      context: "Close of DQ I authorial prologue."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Courtesy blessing; formula, not locus (P42 by analogy)."
    - text: "los requiebros amorosos que en algunas hallarás, son tan honestos y tan medidos con la razón y discurso cristiano, que no podrán mover a mal pensamiento al descuidado o cuidadoso que las leyere."
      cites: [{source: S6, locator: "Prólogo"}]
      date: "1613"
      context: "Authorial prologue to Novelas ejemplares; literary-moral claim about his fiction."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "In-span. Christian measure of the tales, not a personal locus profession."
    - text: "si por algún modo alcanzara que la lección de estas novelas pudiera inducir a quien las leyera a algún mal deseo o pensamiento, antes me cortara la mano con que las escribí, que sacarlas en público: mi edad no está ya para burlarse con la otra vida, que al cincuenta y cinco de los años gano por nueve más, y por la mano."
      cites: [{source: S6, locator: "Prólogo"}]
      date: "1613"
      context: "Same Novelas prologue; seriousness about the afterlife at age ~64."
      axes: [C_ledger]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "In-span. Afterlife taken as real/serious; no deserts claim."
    - text: "libro a quien daré fin dentro de cuatro meses, Deo volente"
      cites: [{source: S7, locator: "Dedicatoria al Conde de Lemos"}]
      date: "1615-10-31"
      context: "Dedication of Don Quixote Part II, promising Persiles."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Set formula (God willing); P42 will-preamble analogy — context, not locus."
  changes_over_life: []
  coder_notes: "Deepen D1 2026-10-24: DQ I Prólogo (1605), Novelas ejemplares Prólogo/Dedicatoria (1613), DQ II Prólogo/Dedicatoria (1615) read in full for own-voice A/B. A and B stay BELOW (formulas + literary 'discurso cristiano' + 'orden de naturaleza' analogy ≠ locus / P16). CHRIST lead strengthened but primary stays BELOW under U2. Third Order (S8) logged as membership. Fiction/character speech excluded (P42). Not plotted."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Castilian; family possibly converso (of Jewish descent)", certainty: 0.5, cites: [{source: S1, locator: "question box 'early life'"}], how_known: "Britannica: 'may have been converso'."}
  religious_heritage_by_birth: {value: "Catholic", certainty: 0.7, cites: [{source: S1, locator: "body, first paragraph after the opening"}], how_known: "Baptized 1547."}
  baptism_or_initiation: {value: "Baptized 9 October 1547", certainty: 0.7, cites: [{source: S1, locator: "body, first paragraph after the opening"}], how_known: "Britannica."}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1605–1615", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "From Don Quixote Part I (1605) to Part II (1615) (P30)."}
  age_at_first_lasting_contribution: {value: 58, certainty: 0.7, cites: [{source: S1, locator: "facts box; opening"}], how_known: "1605 − 1547 = 58 (P30); 57 if Part I appeared before his birthday."}
  first_evidence_of_lio_type_views: {value: "Don Quixote I Prólogo (orden de naturaleza; Dios te dé salud)", year: 1605, certainty: 0.5, cites: [{source: S5, locator: "Prólogo"}], how_known: "Earliest own-voice nature/God talk in the prologues read; still below threshold for scored A/B."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.5, cites: [{source: S5, locator: "1605"}, {source: S6, locator: "1613"}, {source: S7, locator: "1615"}], how_known: "In-span prologues carry Christian-measure and formula God-talk; still BELOW for scoring. Persiles 1616 is after the span (P1)."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Not assessed."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Not assessed."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  reading: "Not assessed."
  notes: ""

institutions:
  - {value: "Household of Cardinal Giulio Acquaviva, Rome", role: "chamberlain ('It seems')", kind: employer, certainty: 0.5, cites: [{source: S1, locator: "'Soldier and slave'"}], how_known: "Britannica, hedged."}
  - {value: "Spanish infantry regiment, Naples", role: "soldier; wounded at Lepanto (7 October 1571), losing the use of his left hand", years: "1570–1575", kind: "government or state body", certainty: 0.7, cites: [{source: S1, locator: "'Soldier and slave'"}], how_known: "Britannica."}
  - {value: "Trinitarian friars", role: "helped raise his ransom from Algiers", years: "1580", kind: "religious body", certainty: 0.7, cites: [{source: S1, locator: "'Soldier and slave'"}], how_known: "Britannica."}
  - {value: "Conde de Lemos", role: "patron; dedicatee of Persiles", kind: "patron or funder", certainty: 0.7, cites: [{source: S2, locator: "Dedicatorias, pp. 9–10"}], how_known: "The dedication."}
collaborators:
  - {value: "Rodrigo de Cervantes", relation: family, note: "brother, captive with him in Algiers, freed 1577", certainty: 0.7, cites: [{source: S1, locator: "'Soldier and slave'"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 118"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "A/B still BELOW after in-span prologues: Christian literary measure and nature-as-literary-analogy do not settle locus or P16."
    - "Third Order dates rest on secondary biography (Wikipedia / Fitzmaurice-Kelly tradition), not a document in his hand."
    - "No private letters with non-formula God/nature professions found this pass."
  open_questions:
    - "Any surviving non-formula private letter on God or nature (unlikely to move A/B under P42)."
    - "Viaje del Parnaso (1614) authorial asides for overlooked A/B (low prior)."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Edward C. Riley (Britannica)"
    citation: "Riley, Edward C. \"Miguel de Cervantes.\" Encyclopaedia Britannica (updated 2 October 2026). https://www.britannica.com/biography/Miguel-de-Cervantes. Read live 2026-10-19."
    url: "https://www.britannica.com/biography/Miguel-de-Cervantes"
    accessed: 2026-10-19
    reliability_note: "Signed article; fetched text ran through 'Soldier and slave'. Question boxes cited only where marked."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, institutions, collaborators]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Miguel de Cervantes"
    citation: "Cervantes Saavedra, Miguel de. Los trabajos de Persiles y Sigismunda, tomo I. Madrid: Calpe (Colección Universal 237–240), 1920. Dedicatoria al Conde de Lemos (dated 19 April 1616), pp. 9–10; Prólogo, pp. 11–13. Wikisource (es) proofread transcription of the Google Books scan Ws44AAAAYAAJ, pages 11–15 of the scan. First published Madrid, 1617."
    url: "https://es.wikisource.org/wiki/Los_trabajos_de_Persiles_y_Sigismunda_(1920)/Tomo_I/Dedicatorias"
    accessed: 2026-10-19
    reliability_note: "Popular edition of the text; Wikisource page quality 3 (proofread). Pages from the printed numbers in the transcription."
    source_quality: "primary / own words"
    used_for: [worldview, contribution, institutions, timing]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S5
    type: primary
    kind: "published work by the subject"
    author: "Miguel de Cervantes"
    citation: "Cervantes Saavedra, Miguel de. El ingenioso hidalgo Don Quijote de la Mancha, Parte I (1605), Prólogo. Spanish text read in the Wikisource transcription of the 1905 Luis Tasso / Doré edition (es.wikisource.org), 2026-10-24."
    url: "https://es.wikisource.org/wiki/El_ingenioso_hidalgo_Don_Quijote_de_la_Mancha_(1905)/Tomo_I/Pr%C3%B3logo"
    accessed: 2026-10-24
    reliability_note: "Authorial prologue; popular edition transcription. Locators by topic (open: orden de naturaleza; close: Dios te dé salud)."
    source_quality: "primary / own words"
    used_for: [worldview, review]
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "Miguel de Cervantes"
    citation: "Cervantes Saavedra, Miguel de. Novelas ejemplares (Madrid, 1613), Dedicatoria al Conde de Lemos (13 July 1613) and Prólogo al lector. Spanish text read in Project Gutenberg ebook #61202 (Brockhaus 1883 reprint), 2026-10-24."
    url: "https://www.gutenberg.org/files/61202/61202-h/61202-h.htm"
    accessed: 2026-10-24
    reliability_note: "Authorial dedication and prologue; public-domain reprint. Orthography modernized in places in this edition."
    source_quality: "primary / own words"
    used_for: [worldview, review]
  - id: S7
    type: primary
    kind: "published work by the subject"
    author: "Miguel de Cervantes"
    citation: "Cervantes Saavedra, Miguel de. Segunda parte del ingenioso caballero don Quijote de la Mancha (1615), Prólogo al lector and Dedicatoria al Conde de Lemos (Madrid, 31 October 1615). Text from Sevilla Arroyo / Rey Hazas electronic edition at Proyecto Cervantes (Texas A&M), read 2026-10-24."
    url: "https://cervantes.library.tamu.edu/V2/CPI/textos/fsevilla/Quijote1615_prelim.htm"
    accessed: 2026-10-24
    reliability_note: "Scholarly electronic text of the Part II preliminaries; authorial prologue and dedication."
    source_quality: "primary / own words"
    used_for: [worldview, review]
  - id: S8
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia. \"Miguel de Cervantes.\" English Wikipedia. https://en.wikipedia.org/wiki/Miguel_de_Cervantes. Read live 2026-10-24."
    url: "https://en.wikipedia.org/wiki/Miguel_de_Cervantes"
    accessed: 2026-10-24
    reliability_note: "Crowdsourced; dual bio (P50) against Britannica. Used for birth/death alignment and Third Order membership note (secondary)."
    source_quality: "reference entry"
    used_for: [identity, basics, childhood, heritage, worldview, review]

---

# Miguel de Cervantes

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Miguel de Cervantes (1547–1616), Spanish novelist, playwright and poet, creator of Don Quixote [S1; S8]. Deepen D1: primary_system BELOW_THRESHOLD (CHRIST lead); A, B and C BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Not plotted (chart-moving NO).

## Life and work

Soldier at Lepanto, captive in Algiers 1575–1580 [S1].

## Contribution and impact

Don Quixote (1605, 1615) and the Novelas ejemplares (1613) [S1].

## Childhood and education

Son of a barber-surgeon; schooling little known [S1].

## Adult working worldview

In-span Novelas prólogo: 'discurso cristiano' and seriousness about 'la otra vida' [S6]; DQ I 'orden de naturaleza' is literary analogy [S5]; Persiles last rites [S2]. A and B stay BELOW (P42/P16).

## Heritage (context only)

Catholic; family possibly converso [S1].

## Timing

1605–1615, from age 58 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Not assessed.

## Open questions

- Any non-formula private letter; Viaje del Parnaso asides (low prior).

## Research log

- 2026-10-19: Read Britannica (through 'Soldier and slave') and the Persiles dedication and prologue on Wikisource.
- 2026-10-24: Deepen D1. DQ I Prólogo (S5), Novelas ejemplares Dedicatoria/Prólogo (S6), DQ II Prólogo/Dedicatoria (S7), Wikipedia EN (S8). A/B stay BELOW; CHRIST lead strengthened; chart-moving NO.
