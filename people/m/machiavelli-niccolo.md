---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch V)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Audit fixes for batch V (gs_982cb8e_V run 1): MC4, Prince ch. 26 locator p. 99 -> p. 100 (scan p. 110); MC8, the three Discorsi statements relabelled from scholarly edition to the web-copy label (primary transcription, unscanned); ruling V2 (v8's call on the auditor's advice): primary_system stays BELOW_THRESHOLD with the Esortazione alla penitenza as a lead; note, SEP dates added to S2. No scored value changes."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch V, order P32: F 4, rank 122). Basics from Britannica (Harvey Mansfield) and SEP (Cary Nederman); own-voice passages read in Italian on Wikisource: Il Principe chs. 25–26 (1814 edition, proofread against scans) and Discorsi I.12, I.56, II.5 (Martelli text). Not a scientist (P30). primary_system BELOW_THRESHOLD (scholars divide: anti-Christian, conventional piety, Christian); A, B, D, E BELOW_THRESHOLD; C UNKNOWN; mid_basin BELOW_THRESHOLD. Span 1513–1519 (0.5). Not plotted. Draft, not reviewed."}

identity:
  id: machiavelli-niccolo
  display_name: "Niccolò Machiavelli"
  roster:
    canonical_name: "Niccolò Machiavelli"
    rank: 122
    F: 4
    models: [DeepSeek, Gemini, GPT, Grok]
    band: "core (3–4)"
    status: core
    field: "political thought"
    field_bucket: "politics / law / military"
  full_name: {value: "Niccolò di Bernardo Machiavelli", certainty: 0.5, cites: [{source: S1, locator: "'Early life and political career'"}], how_known: "Patronymic from his father Bernardo (S1); the form is the coder's."}
  native_name: {value: "Niccolò Machiavelli", certainty: 0.7, cites: [{source: S1, locator: "title"}], how_known: "Italian."}
  aliases:
    - {name: "Machiavelli-Niccolò", kind: "roster alias"}
    - {name: "Niccolo Machiavelli", kind: "roster alias"}
    - {name: "Niccolo-Machiavelli", kind: "roster alias"}

basics:
  birth:
    date: {value: "1469-05-03", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "facts box (Born)"}], how_known: "Britannica; Florence used the Julian calendar."}
    place: {value: "Florence", modern_name: "Florence, Italy", polity_then: "Republic of Florence", certainty: 0.7, cites: [{source: S1, locator: "facts box (Born)"}], how_known: "Britannica."}
  death:
    date: {value: "1527-06-21", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "facts box (Died)"}], how_known: "Britannica."}
    place: {value: "Florence", modern_name: "Florence, Italy", polity_then: "Republic of Florence", certainty: 0.7, cites: [{source: S1, locator: "facts box (Died)"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1513, certainty: 0.7, cites: [{source: S1, locator: "'Writings'"}, {source: S2, locator: "§1 Biography"}], how_known: "The Prince, written 1513 ('end of 1513 (and perhaps early 1514)', S2); published 1532. Dated by documented composition (P30): the letter of 10 December 1513 announces it (S1)."}
  era_bucket: {value: "1400 to 1599", certainty: 0.7, cites: [{source: S2, locator: "§1 Biography"}], how_known: "1513 (P2)."}
  region_of_birth: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "facts box"}], how_known: "Italy (P3)."}
  region_of_work: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "'Early life and political career'"}], how_known: "Florence and San Casciano."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "'Early life and political career'"}], how_known: "Britannica."}
  languages_of_work: {value: ["Italian", "Latin"], certainty: 0.5, cites: [{source: S1, locator: "'Early life and political career'"}], how_known: "Wrote in Italian; 'learned Latin well' (S1)."}
  occupations: {value: ["secretary (head of the second chancery) of the Florentine republic", "diplomat", "political philosopher and historian", "playwright and poet"], certainty: 0.7, cites: [{source: S1, locator: "'Early life and political career'; 'Writings'"}, {source: S2, locator: "§1"}], how_known: "Britannica and SEP."}

contribution:
  fields: {value: ["political philosophy", "history"], certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "opening"}], how_known: "Britannica and SEP."}
  lasting_original_contributions:
    - {value: "The Prince (Il Principe): worldly success in politics apart from conventional morality", year: 1513, kind: work, lasting: "'arguably the most famous book on politics ever written', giving the name Machiavellian (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Writings'"}, {source: S2, locator: "§1; §2"}], how_known: "Britannica and SEP. Not a theory of natural systems, so not a scientist (P30)."}
    - {value: "Discourses on the First Ten Books of Titus Livy: principles of republican rule, liberty and civic conflict", year: 1514, kind: work, lasting: "his 'other major contribution to political thought' (S2); traced by Pocock and Rahe into the Atlantic republican tradition (S2 §9)", certainty: 0.5, cites: [{source: S2, locator: "§1; §6; §9"}, {source: S1, locator: "'Writings'"}], how_known: "SEP: 'commencing perhaps in 1514 or 1515 and completed in 1518 or 1519'; start year 1514 (P12), end 1519 for the span (P30). Published 1531."}
  evidence_of_impact:
    - {value: "'Machiavellian' as a word for worldly success through scheming deceit", kind: "named after them", certainty: 0.7, cites: [{source: S1, locator: "'Writings'"}], how_known: "Britannica."}
    - {value: "A literature on his originality and place in Western thought 'of truly staggering proportions'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S2, locator: "§9"}], how_known: "SEP."}
  major_works:
    - {value: "The Art of War (Dell'arte della guerra)", year: 1521, certainty: 0.7, cites: [{source: S1, locator: "'Early life and political career'"}], how_known: "Britannica."}
    - {value: "Florentine Histories (Istorie fiorentine), presented to Clement VII", year: 1525, certainty: 0.7, cites: [{source: S1, locator: "'Early life and political career'"}, {source: S2, locator: "§1"}], how_known: "Britannica and SEP. Not listed as lasting from the sources read; it would move the span end to 1525 if listed (coder_notes)."}
    - {value: "The Life of Castruccio Castracani of Lucca", year: 1520, certainty: 0.7, cites: [{source: S1, locator: "'Early life and political career'"}], how_known: "Britannica."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "The Prince and the Discourses remain central texts of political thought (S1, S2).", certainty: 0.7, cites: [{source: S2, locator: "§9"}], how_known: "SEP."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Nothing on the family's religious practice in the sources read beyond the Catholic city."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not in the sources read."}
  parents_and_household:
    - {value: "Father: Bernardo Machiavelli, doctor of laws, barred from office as an insolvent debtor; kept a library", certainty: 0.7, cites: [{source: S1, locator: "'Early life and political career'"}], how_known: "Britannica."}
  household_circumstances: {value: "Poor branch of a wealthy and prominent Florentine family", certainty: 0.7, cites: [{source: S1, locator: "'Early life and political career'"}], how_known: "Britannica."}
  schooling:
    - {value: "Humanist education; attended lectures of Marcello Virgilio Adriani at the Studio Fiorentino", stage: other, run_by: other, certainty: 0.5, cites: [{source: S1, locator: "'Early life and political career'"}], how_known: "Britannica: 'little is known of Niccolò’s education'; years not stated."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["Italian"], certainty: 0.5, cites: [{source: S1, locator: "'Early life and political career'"}], how_known: "Coder's reading."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1513–1519", certainty: 0.5, cites: [{source: S2, locator: "§1 Biography"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Catholic Florence; listened to Savonarola's sermons (1498)", certainty: 0.5, cites: [{source: S1, locator: "'Early life and political career'"}], how_known: "Britannica. Context only."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing read."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "Scholars divide (S2 §4): many read him as 'profoundly anti-Christian, preferring the pagan civil religions'; Parel finds an 'essentially pagan' astral cosmos; others 'a man of conventional, if unenthusiastic, piety'; Grazia, Viroli and Nederman find a Christian, divinely ordered cosmos. Britannica: The Prince 'brought him a reputation as an atheist' (S1). His own texts read are mixed (statements): God 'does not want to do everything' so as not to take away free will (Prince 26), beside a debunking account of miracles 'even in false religions' (Discorsi I.12). Contested readings with no decisive own-voice profession, so below threshold; CHRIST is the named lead. Ruling V2 (v8's call on the auditor's advice, batch V audit): the Esortazione alla penitenza (it.wikisource 'Discorso morale', Opere VI pp. 142–147, 25% transcribed, undated) does not lift CHRIST: it was a confraternity address given on assignment ('per ubbidire a' miei maggiori'), it is undated (P39), and scholars divide on his sincerity (S2 §4). Cited as a lead only (not read in full)."}
  secondary_system: {value: UNKNOWN, how_known: "One system (P29)."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Lead: Grazia, Viroli, Nederman (S2 §4); Prince 26 on God and free will; the Esortazione alla penitenza (‘ogni cosa è creata per onore e per bene dell’uomo’, per the batch V audit; ruling V2: lead only)."}
    - {code: ATHE, reason: "Rejected: a reputation (S1), no stated denial."}
    - {code: HELLEN, reason: "Rejected as a code: his preference for Roman civil religion (S2 §4) is a political judgement about religions, not a stated personal adherence."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "Prince 26 speaks of a God who wills and withholds action ('Dio non vuole far ogni cosa'), a lead toward 1; but it is an exhortation to the Medici wrapped in Exodus figures (the sea opened, manna), and scholars contest his sincerity (S2 §4). Named readings: 1 (Grazia, Nederman) or BELOW_THRESHOLD."}
    B_cause: {value: BELOW_THRESHOLD, how_known: "Mixed own-voice evidence, none a general statement of lawfulness. Toward the LIO pole: nature purges the human race by flood, plague and famine 'come ne’ corpi semplici' (Discorsi II.5), and the prudent spread belief in miracles 'eziandio false' (I.12). Toward the other pole: portents always precede great events, perhaps sent by intelligences in the air 'avendo compassione agli uomini' (I.56), and Prince 26's 'straordinari senza esempio, condutti da Dio'. Prince 25 leaves fortune 'arbitra della metà delle azioni nostre'. Named readings 2 and 3; not a scientist (P30), so no working-science score."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read on reward and punishment of persons in his own view (P19)."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "Lead only: rulers should favour things that support religion 'come che le giudicassono false', the more so 'quanto più conoscitori delle cose naturali' (Discorsi I.12). Religion judged by political use, not a stated rule on revelation against observation."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Scored on the world's order (P7). Lead: Discorsi II.5 puts 'questo corpo misto della umana generazione' under the same purging as simple bodies; but I.56's warning signs out of compassion for men point the other way. Not enough for a score."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A and B are BELOW_THRESHOLD; no branch of the P4 test is met."}
  statements:
    - text: "Nondimanco, perchè il nostro libero arbitrio non sia spento, giudico potere esser vero, che la fortuna sia arbitra della metà delle azioni nostre, ma che ancora ella ne lasci governare l’altra metà, o poco meno, a noi."
      cites: [{source: S3, locator: "cap. XXV, p. 95"}]
      date: "1513"
      context: "The Prince ch. 25, answering the opinion 'che le cose del mondo siano in modo governate dalla fortuna, e da Dio' that men cannot correct them."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "Wikisource proofread transcription (level 4) of the 1814 'Italia' edition (Internet Archive ilprincipedinic00machgoog), printed p. 95. Written 1513, published 1532."
    - text: "Oltre a questo, qui si veggono straordinari senza esempio, condutti da Dio: il mare s’è aperto, una nube vi ha scorto il cammino, la pietra ha versato l’acqua; qui è piovuto la manna, ogni cosa è concorsa nella vostra grandezza; il rimanente dovete far voi. Dio non vuole far ogni cosa, per non ci torre il libero arbitrio, e parte di quella gloria che tocca a noi."
      cites: [{source: S3, locator: "cap. XXVI, p. 100"}]
      date: "1513"
      context: "The Prince ch. 26, the exhortation to the Medici to free Italy; Exodus imagery applied to the present."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "Same edition, printed p. 100 (scan p. 110); printed p. 99 ends '...possa farsi capo di questa' (corrected in the batch V audit fixes, MC4). Rhetorical exhortation; scholars dispute how literally to read it (S2 §4)."
    - text: "E debbono, tutte le cose che nascano in favore di quella, come che le giudicassono false, favorirle e accrescerle; e tanto più lo debbono fare, quanto più prudenti sono, e quanto più conoscitori delle cose naturali. E perché questo modo è stato osservato dagli uomini savi, ne è nato l’opinione dei miracoli, che si celebrano nelle religioni eziandio false"
      cites: [{source: S4, locator: "Libro I, cap. 12"}]
      date: "1514"
      context: "Discorsi I.12, on keeping religion as the foundation of a republic; followed by Livy's miracle of Juno at Veii."
      axes: [B_cause, D_authority]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "Wikisource text of Tutte le opere, ed. Mario Martelli (Sansoni, 1971), via LiberLiber, re-read against the book (talk page); not scan-backed, so a web copy (0.7 cap; nothing scored on it). Labelled as an unscanned keyed transcription, the house label for a web copy (Keynes precedent; batch V audit fix MC8), not as a scholarly edition read in print. Dated by the start of composition (1514 or 1515 to 1518 or 1519, S2)."
    - text: "Donde ei si nasca io non so, ma ei si vede per gli antichi e per gli moderni esempli, che mai non venne alcuno grave accidente in una città o in una provincia, che non sia stato, o da indovini o da rivelazioni o da prodigi o da altri segni celesti, predetto."
      cites: [{source: S4, locator: "Libro I, cap. 56"}]
      date: "1514"
      context: "Discorsi I.56; examples Savonarola, the lightning on the Duomo before Lorenzo's death, Livy's voice to Caedicius. He then leaves the cause to one with 'notizia delle cose naturali e soprannaturali' and offers that the air may be 'pieno di intelligenze' which 'per naturali virtù' foresee and warn men."
      axes: [B_cause, E_scope]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "Martelli text on Wikisource; web copy as above. Dated by the start of composition (1514 or 1515 to 1518 or 1519, S2)."
    - text: "perché la natura, come ne’ corpi semplici, quando e’ vi è ragunato assai materia superflua, muove per sé medesima molte volte, e fa una purgazione, la quale è salute di quel corpo; così interviene in questo corpo misto della umana generazione"
      cites: [{source: S4, locator: "Libro II, cap. 5"}]
      date: "1514"
      context: "Discorsi II.5, on why memory of antiquity is lost: causes from men (new sects and languages) and 'dal cielo' (plague, famine, flood)."
      axes: [B_cause, E_scope]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "Martelli text on Wikisource; web copy as above. Dated by the start of composition (1514 or 1515 to 1518 or 1519, S2)."
  changes_over_life: []
  coder_notes: "Coder's call on the span: 1513 (The Prince) to 1519 (completion of the Discourses, SEP 'completed in 1518 or 1519'; P30 end of range). Florentine Histories (1525) and The Art of War (1521) are major works but not listed as lasting from the sources read; listing the Histories would end the span in 1525. Not a scientist (P30). The religion fields are below threshold because scholars divide (S2 §4) and his own passages pull both ways; the axes name readings rather than score them. Leads: Discorsi I.11–15 and II.2 (Christianity 'ha renduto il mondo debole', not read here); the letter to Guicciardini of 17 May 1521; the 'Esortazione alla penitenza'. Italian quotations kept verbatim; no translation inside quotation marks. Not plotted."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Florentine patrician family (poor branch)", certainty: 0.7, cites: [{source: S1, locator: "'Early life and political career'"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Catholic", certainty: 0.5, cites: [{source: S1, locator: "'Early life and political career'"}], how_known: "Coder's reading of Florence c. 1469."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1513–1519", certainty: 0.5, cites: [{source: S2, locator: "§1 Biography"}], how_known: "From The Prince (1513) to the completion of the Discourses (1518 or 1519; end of range, P30). Coder's call; alternative end 1525 (coder_notes)."}
  age_at_first_lasting_contribution: {value: 44, certainty: 0.7, cites: [{source: S1, locator: "facts box"}, {source: S2, locator: "§1"}], how_known: "1513 − 1469 = 44 (P30)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No axis scored."}
  lio_views_relative_to_major_work: {value: "unclear", certainty: 0.5, cites: [{source: S4, locator: "Libro II, cap. 5"}], how_known: "LIO-leaning passages exist in the Discourses but are not scored."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "§2"}], how_known: "Not assessed."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "§2"}], how_known: "Not assessed."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S2, locator: "§2"}], how_known: "Coder's reading."}
  reading: "Virtù against Fortuna; politics read from ancient and modern examples."
  notes: ""

institutions:
  - {value: "Second chancery of the Florentine republic", role: "head (secretary)", years: "1498–1512", kind: "government or state body", certainty: 0.7, cites: [{source: S1, locator: "'Early life and political career'"}], how_known: "Britannica."}
  - {value: "Florentine militia", role: "organizer", years: "from 1505", kind: "government or state body", certainty: 0.7, cites: [{source: S1, locator: "'Early life and political career'"}], how_known: "Britannica."}
  - {value: "Medici papacy (Cardinal Giulio de' Medici / Clement VII)", role: "official historian of Florence", years: "1520–1525", kind: "patron or funder", certainty: 0.7, cites: [{source: S1, locator: "'Early life and political career'"}], how_known: "Britannica."}
  - {value: "Procuratori delle Mura, Florence", role: "chancellor", years: "1526", kind: "government or state body", certainty: 0.7, cites: [{source: S1, locator: "'Early life and political career'"}], how_known: "Britannica."}
collaborators:
  - {value: "Piero Soderini", relation: "mentor or employer", note: "gonfalonier for life; Machiavelli's patron in office", certainty: 0.7, cites: [{source: S1, locator: "'Early life and political career'"}], how_known: "Britannica."}
  - {value: "Francesco Guicciardini", relation: correspondent, note: "friend; with him in the war of the League of Cognac", certainty: 0.7, cites: [{source: S1, locator: "'Early life and political career'"}], how_known: "Britannica."}
  - {value: "Girolamo Savonarola", relation: other, note: "heard his sermons in 1498; 'unarmed prophet' in The Prince", certainty: 0.7, cites: [{source: S1, locator: "'Early life and political career'"}], how_known: "Britannica."}
  - {value: "Marcello Virgilio Adriani", relation: teacher, note: "lectures at the Studio Fiorentino", certainty: 0.5, cites: [{source: S1, locator: "'Early life and political career'"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S5, locator: "roster.csv, rank 122"}], how_known: "Study roster."}
  controversies:
    - {value: "Reputation as 'an atheist and an immoral cynic'", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  data_quality_flags:
    - "Religion fields rest on contested readings; the own-voice passages read pull both ways."
    - "Discorsi quotations are from a Wikisource text of the Martelli edition without scans (web copy)."
    - "Span end is a coder's call (1519 vs 1525)."
  open_questions:
    - "Discorsi I.11–15, II.2; letter to Guicciardini, 17 May 1521; Esortazione alla penitenza (it.wikisource 'Discorso morale', Opere VI pp. 142–147; a lead under ruling V2, not read)."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Harvey Mansfield"
    citation: "Mansfield, Harvey. \"Niccolò Machiavelli.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Niccolo-Machiavelli. Read live 2026-10-19."
    url: "https://www.britannica.com/biography/Niccolo-Machiavelli"
    accessed: 2026-10-19
    reliability_note: "Signed article (Mansfield, Harvard); facts box, 'Early life and political career' and 'Writings' cited; question boxes not cited."
    used_for: [identity, basics, contribution, childhood, heritage, institutions, collaborators, review, worldview]
  - id: S2
    type: tertiary
    kind: encyclopedia
    author: "Cary Nederman"
    citation: "Nederman, Cary. \"Niccolò Machiavelli.\" Stanford Encyclopedia of Philosophy. First published 13 Sep 2005; substantive revision 6 Dec 2023. https://plato.stanford.edu/entries/machiavelli/"
    url: "https://plato.stanford.edu/entries/machiavelli/"
    accessed: 2026-10-19
    reliability_note: "Signed scholarly encyclopedia (first published 13 Sep 2005; substantive revision 6 Dec 2023); §1, §2, §4, §6 and §9 used."
    used_for: [basics, contribution, worldview, timing]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "Niccolò Machiavelli"
    citation: "Machiavelli, Niccolò. Il Principe. Italia, 1814. Wikisource transcription (Indice:Il Principe.djvu, from Internet Archive ilprincipedinic00machgoog). https://it.wikisource.org/wiki/Il_Principe"
    url: "https://it.wikisource.org/wiki/Il_Principe"
    accessed: 2026-10-19
    reliability_note: "Proofread (level 4) transcription tied to page scans of a named printed edition; printed page numbers cited."
    used_for: [worldview]
  - id: S4
    type: primary
    kind: "scholarly edition"
    author: "Niccolò Machiavelli; ed. Mario Martelli"
    citation: "Machiavelli, Niccolò. Discorsi sopra la prima Deca di Tito Livio. In Tutte le opere, ed. Mario Martelli (Firenze: Sansoni, 1971). Wikisource text. https://it.wikisource.org/wiki/Discorsi_sopra_la_prima_Deca_di_Tito_Livio"
    url: "https://it.wikisource.org/wiki/Discorsi_sopra_la_prima_Deca_di_Tito_Livio"
    accessed: 2026-10-19
    reliability_note: "Web copy of the Martelli text (via LiberLiber/Einaudi), marked 75% and re-read against the book per the talk page; no scans. Cited by book and chapter."
    used_for: [worldview, timing]
  - id: S5
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Niccolò Machiavelli

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Niccolò Machiavelli (1469–1527), Florentine secretary and political philosopher [S1]. Draft: primary_system BELOW_THRESHOLD (CHRIST lead); A, B BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Not plotted.

## Life and work

Second chancery 1498–1512; exile at San Casciano from 1513; official historian from 1520 [S1, S2].

## Contribution and impact

The Prince (1513) and the Discourses on Livy (1514–1519) [S1, S2].

## Childhood and education

Son of Bernardo, a doctor of laws; humanist education [S1].

## Adult working worldview

Scholars divide on his religion [S2]. His own passages: God leaves room for free will (Prince 26) [S3]; miracles spread by the prudent even in false religions (Discorsi I.12); portents precede great events (I.56); nature purges the human race (II.5) [S4].

## Heritage (context only)

Catholic Florence [S1].

## Timing

1513–1519, from age 44 [S2].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Not assessed.

## Open questions

- Discorsi I.11–15 and II.2; letters.

## Research log

- 2026-10-19: Read Britannica, SEP, Il Principe chs. 25–26 and Discorsi I.12, I.56, II.5 on Wikisource.
