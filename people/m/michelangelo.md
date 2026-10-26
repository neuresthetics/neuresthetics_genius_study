---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch I)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: '2026-10-25'
  change_log:
    - {date: 2026-10-25, by: "Grok Bot", summary: "Perpetual deepen: family_religion TODO synced from religious_heritage_by_birth (context only). Chart-moving NO. No figures/; no fallacy_catalog."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch I, order P32: F 5, rank 59). Basics from Britannica (Gilbert), signed body through the early works only (the fetch returned only that part). Worldview from Sonnet LXV (dated 19 September 1554, sent to Vasari), Symonds's translation, Gutenberg #10314 (web copy). Not a scientist. primary_system CHRIST 0.5; A 0 at 0.5 (alt 1); B UNKNOWN (P16); C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD. Not plotted. Draft, not reviewed."}

    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #59, F5 rank 59). Needs: A single source; A faded; B UNKNOWN. Primary Italian of late spiritual sonnets from Guasti 1863 (S4, IA OCR) and Girardi/Wikisource (S5): G 285 Giunto è già, G 288 Le favole del mondo, G 289 Non è più bassa, G 290 Scarco d'un'importuna — personal Christ who opens arms on the cross, faith as gift, blood that washes sins. Eisenbichler 1987 (S6) adds Carteggio letters on sacraments (1516, 1548). A 0 0.5 single → 0 @0.7 corroborated; primary_system CHRIST 0.5 → 0.7; C 1 @0.5 and D 1 @0.5 newly scored; B stays UNKNOWN (P16: not a scientist; no statement on nature's causal order — 'natura' poems are beauty/love, not physics). mid_basin BELOW_THRESHOLD. Wikipedia EN (S7) dual-sources bio dates and Catholic faith. P47 on S1–S7. Chart-moving NO (B UNKNOWN, unplotted). No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: michelangelo
  display_name: "Michelangelo"
  roster:
    canonical_name: "Michelangelo"
    rank: 59
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: art
    field_bucket: arts
  full_name: {value: "Michelangelo di Lodovico Buonarroti Simoni", certainty: 0.7, cites: [{source: S1, locator: "header ('In full')"}], how_known: "Britannica."}
  native_name: {value: UNKNOWN, how_known: "Italian, Latin script."}
  aliases:
    - {name: "Michelangelo Buonarroti", kind: "roster alias"}
    - {name: "Michael Angelo", kind: other}

basics:
  birth:
    date: {value: "1475-03-06", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica; before 1582, so Julian."}
    place: {value: "Caprese, Republic of Florence", modern_name: "Caprese Michelangelo, Italy", polity_then: "Republic of Florence", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "Early life, 1475–1488"}], how_known: "Britannica and Wikipedia EN (modern name Caprese Michelangelo)."}
  death:
    date: {value: "1564-02-18", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica; Julian."}
    place: {value: "Rome, Papal States", modern_name: "Rome, Italy", polity_then: "Papal States", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1498, certainty: 0.5, cites: [{source: S1, locator: "'Early life and works' (Pietà commission, 1498)"}], how_known: "The Pietà, 'today the most famous example' of its type, commissioned 1498 (P13); completion year not in the body read, so 0.5."}
  era_bucket: {value: "1400 to 1599", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "His whole life (1475–1564) falls in the bucket (P2)."}
  region_of_birth: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Italy is Southern Europe in regions.csv (P3)."}
  region_of_work: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "'Early life and works'"}], how_known: "Florence, Bologna, Rome."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [Italian], certainty: 0.7, cites: [{source: S2, locator: "notes (Italian originals)"}], how_known: "Poems and letters in Italian."}
  occupations: {value: ["sculptor", "painter", "architect", "poet"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

contribution:
  fields: {value: ["sculpture", "painting", "architecture"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Pietà (St. Peter's Basilica)", year: 1499, kind: work, lasting: "Signed masterpiece; among the most famous sculptures in Western art (S1, S7)", certainty: 0.7, cites: [{source: S1, locator: "'Early life and works'"}, {source: S7, locator: "Notable work (1498–1499)"}], how_known: "Commission 1497–98; completion 1499 (Wikipedia EN dual-source with Britannica)."}
    - {value: "David", year: 1504, kind: work, lasting: "Prime Renaissance nude; defining Florentine civic symbol (S1, S7)", certainty: 0.7, cites: [{source: S1, locator: "'Early life and works'"}, {source: S7, locator: "Notable work (1501–1504)"}], how_known: "Completed 1504."}
    - {value: "Sistine Chapel ceiling frescoes", year: 1512, kind: work, lasting: "Genesis cycle including Creation of Adam; among the most influential frescoes in Western art (S1, S7)", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "Sistine Chapel ceiling, 1508–1512"}], how_known: "Painted 1508–1512."}
    - {value: "The Last Judgment (Sistine Chapel altar wall)", year: 1541, kind: work, lasting: "Second Coming and judgement of souls; widely imitated and later censored (S7)", certainty: 0.7, cites: [{source: S7, locator: "Rome, 1534–1546; Notable work (1536–1541)"}], how_known: "Painted 1536–1541."}
  evidence_of_impact:
    - {value: "First Western artist whose biography was published in his lifetime (Vasari 1550; Condivi 1553)", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "opening section"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Roman Catholic (Florentine)", certainty: 0.5, cites: [{source: S7, locator: "Early life"}, {source: S6, locator: "p. 123"}], how_known: "Same as religious_heritage_by_birth; baptism record not read."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father held occasional government posts; administrator of Caprese at the birth", role: father, certainty: 0.7, cites: [{source: S1, locator: "'Early life and works'"}], how_known: "Britannica."}
  household_circumstances: {value: "Minor Florentine nobility that had lost its patrimony and status", certainty: 0.7, cites: [{source: S1, locator: "'Early life and works'"}], how_known: "Britannica."}
  schooling:
    - {value: "Apprenticed to Domenico Ghirlandaio (left after one year)", stage: apprenticeship, run_by: private, ages: "13–14", certainty: 0.7, cites: [{source: S1, locator: "'Early life and works'"}], how_known: "Britannica."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "Lorenzo de' Medici took him under his wing; Bertoldo di Giovanni 'the nearest... to a teacher of sculpture'", certainty: 0.7, cites: [{source: S1, locator: "'Early life and works'"}], how_known: "Britannica."}
  languages_in_childhood: {value: TODO}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1498–1541", certainty: 0.5, cites: [{source: S1, locator: "'Early life and works'"}, {source: S7, locator: "Notable work dates"}], how_known: "Equals timing.major_work_period (first lasting to Last Judgment)."}
  nominal_affiliations:
    - {value: "Roman Catholic", role: member, certainty: 0.7, cites: [{source: S6, locator: "pp. 123–124 (Mass, sacraments)"}, {source: S7, locator: "Personal life — Faith"}], how_known: "Practicing Catholic in letters and biographies; Wikipedia EN agrees (dual-source)."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not a scientist; no science–religion remark read."}
  primary_system:
    value: CHRIST
    basis: consistent_private_letters
    certainty: 0.7
    cites: [{source: S4, locator: "pp. 230–232 (G 285, G 288; letters to Vasari)"}, {source: S5, locator: "G 285, G 288, G 289, G 290"}, {source: S6, locator: "pp. 123–124, 130–133"}, {source: S2, locator: "Sonnets LXV–LXVII, LXXIII (Symonds EN)"}]
    rationale: "Late spiritual sonnets turn to Christ on the cross ('Amor divino / Ch'aperse, a prender noi, in croce le braccia', G 285), beg for faith as God's gift (G 289), and ask that 'Tuo sangue sol mie colpe lavi' (G 290). Covering letters to Vasari (1554, 1555) say the poems show 'dove io tengo i mie' pensieri'. Letters urge sacraments for dying kin (S6). Multiple consistent private documents, so 0.7. Named alternative: PLATO for earlier Cavalieri/Colonna Neoplatonic ascent poetry (Eisenbichler; not the adult working code here)."
    how_known: "Italian primary in Guasti 1863 (S4) and Girardi/Wikisource (S5); letters via Eisenbichler (S6); Symonds EN cross-check (S2)."
  secondary_system: {value: UNKNOWN, how_known: "Neoplatonism of the 1530s love poetry is a live lead (PLATO), not coded as a second system here."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Chosen: cross, blood, faith, sacraments, final reckoning."}
    - {code: PLATO, reason: "Not chosen for adult working worldview; earlier love poetry uses Neoplatonic ascent (Eisenbichler on G 83, G 151)."}
    - {code: CLTHEI, reason: "Not chosen; prayers ask for grace and faith, not intervention in physical events."}
  lio_axes:
    A_locus:
      value: 0
      basis: consistent_private_letters
      certainty: 0.7
      support: corroborated
      cites: [{source: S4, locator: "p. 230 (G 285)"}, {source: S5, locator: "G 285, G 288, G 290"}, {source: S6, locator: "pp. 130–133 (cross, blood, grace)"}, {source: S2, locator: "Sonnets LXV, LXXIII"}]
      how_known: "Multiple late spiritual sonnets in Italian primary (S4, S5) plus letters on Christian practice (S6). Independent poem corpus and letter evidence → corroborated (P48). Named alternative keeps certainty at 0.7."
      rationale: "Personal redeeming God: soul 'volta a quell'amor divino / c'aperse, a prender noi, 'n croce le braccia' (G 285); addresses 'Signor mie caro'; asks that Christ's blood alone wash his sins (G 290). Not identity with nature or impersonal order. Named alternative: 1, if the Neoplatonic 'forma universale' of earlier love poetry is read as the adult locus."
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30/P33). No statement of his own on nature's causal order was found (P16). Poems that mention 'natura' (e.g. G 69 Ben provvide natura) treat nature as provider of beauty in love, not physical law. Anatomy practice and Genesis frescoes are work, not a B statement (P24 inference not applied: he is not a scientist)."}
    C_ledger:
      value: 1
      basis: consistent_private_letters
      certainty: 0.5
      support: corroborated
      cites: [{source: S4, locator: "p. 230 (G 285, 'conto e ragion d'ogn' opra trista e pia')"}, {source: S5, locator: "G 290 ('Tuo sangue sol mie colpe lavi')"}, {source: S6, locator: "p. 133"}]
      how_known: "Final reckoning of every deed and blood that washes sins, in more than one poem. Certainty 0.5: poems are penitential prayer, not a full doctrine of desert; named alternative 0 (grace alone without ledger)."
      rationale: "Leans interventionist ledger: at death one 'render[s] conto e ragion d'ogni opra trista e pia' (G 285); yet he also begs that justice not look on his past and that blood alone cleanse him (G 290). Named alternative: 0."
    D_authority:
      value: 1
      basis: consistent_private_letters
      certainty: 0.5
      support: corroborated
      cites: [{source: S5, locator: "G 289 (faith as 'don de' doni')"}, {source: S4, locator: "p. 232 (G 288)"}, {source: S6, locator: "pp. 131–133"}]
      how_known: "Faith is a gift God must give; contemplation of God displaced by worldly 'favole'. Two poems plus scholarly reading. Certainty 0.5: no explicit ranking of reason vs revelation for knowledge of nature; named alternative 2 (art/intelletto as a second domain in the concetto sonnets)."
      rationale: "Revelation/grace outranks: he cannot rise halfway to heaven without God's help (G 288); faith is the chain of every celestial gift (G 289); blood opens heaven. Named alternative: 2, if the earlier 'man that obeys the intellect' art theory (G 151) is read as a second authority domain."
    E_scope: {value: UNKNOWN, how_known: "No statement on the scope of God's governance of the world's order (P7). Last Judgment is a painted subject, not a verbal account of nature."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "B_cause is UNKNOWN (P16); A is 0 @0.7 corroborated. Unplotted."}
  statements:
    - text: "Né pinger né scolpir fie più che quieti / l'anima, volta a quell'amor divino / c'aperse, a prender noi, 'n croce le braccia."
      cites: [{source: S4, locator: "p. 230"}, {source: S5, locator: "G 285"}, {source: S2, locator: "Sonnet LXV (Symonds EN)"}]
      date: "1554-09-19"
      context: "Sonnet G 285 ('Giunto è già 'l corso della vita mia') sent to Giorgio Vasari with a letter dated 19 September 1554 (Guasti prints the letter under the poem)."
      axes: [A_locus, C_ledger]
      kind: "private letter"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Guasti 1863 p. 230 OCR; Wikisource/Girardi 1960 agrees. Symonds rhymed EN: 'Painting nor sculpture now can lull to rest / My soul that turns to His great love on high, / Whose arms to clasp us on the cross were spread.'"
    - text: "Le favole del mondo m'hanno tolto / il tempo dato a contemplare Iddio."
      cites: [{source: S4, locator: "p. 232"}, {source: S5, locator: "G 288"}]
      date: "1555"
      context: "Sonnet G 288 sent to Vasari with G 289; covering letter says the poems show where he keeps his thoughts (Guasti p. 232)."
      axes: [A_locus, D_authority]
      kind: "private letter"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Guasti OCR; Wikisource/Girardi agrees. Symonds LXVI."
    - text: "Tuo sangue sol mie colpe lavi e tocchi, / e più abondi, quant'i' son più vecchio, / di pronta aita e di perdono intero."
      cites: [{source: S5, locator: "G 290"}, {source: S6, locator: "p. 133"}, {source: S2, locator: "Sonnet LXXIII (Symonds EN)"}]
      context: "Late penitential sonnet G 290 ('Scarco d'un'importuna e greve salma'); address to Christ."
      axes: [A_locus, C_ledger, D_authority]
      kind: "unpublished manuscript"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Wikisource/Girardi 1960 Italian; Eisenbichler quotes the same closing. Symonds LXXIII."
  changes_over_life: []
  coder_notes: "Deepen D1 (2026-10-24): A raised on multiple Italian spiritual sonnets + letters; B left UNKNOWN under P16 after checking 'natura' poems and art-theory sonnets. C and D newly at 0.5. Neoplatonic earlier phase noted under candidates, not scored as adult working code. Chart-moving NO."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Florentine", certainty: 0.7, cites: [{source: S1, locator: "'Early life and works'"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Roman Catholic (Florentine)", certainty: 0.5, cites: [{source: S7, locator: "Early life"}, {source: S6, locator: "p. 123"}], how_known: "Florentine Catholic milieu; baptism record not read (0.5)."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1498–1541", certainty: 0.5, cites: [{source: S1, locator: "'Early life and works'"}, {source: S7, locator: "Notable work dates"}], how_known: "First lasting (Pietà commission/completion) to Last Judgment (P29, P30). St Peter's architects' work after 1546 not used as end year here."}
  age_at_first_lasting_contribution: {value: 23, certainty: 0.5, cites: [{source: S1, locator: "opening; 'Early life and works'"}], how_known: "1498 − 1475 = 23 (P30)."}
  first_evidence_of_lio_type_views: {value: "1554", certainty: 0.5, cites: [{source: S4, locator: "p. 230 (G 285 letter 19 Sep 1554)"}], how_known: "Earliest dated LIO-type statement scored (G 285). Earlier religious practice in letters (1516) is not an axis statement."}
  lio_views_relative_to_major_work: {value: "after major work", certainty: 0.5, cites: [{source: S4, locator: "p. 230"}, {source: S7, locator: "Notable work dates"}], how_known: "G 285 is 1554; major-work span ends 1541."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Scored spiritual poems are after the listed major-work span; earlier Neoplatonic love poetry not used for LIO axes."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Art-theory 'concetto' sonnets (G 151) are Neoplatonic form-in-marble, not scored as geometric form for H1.", certainty: 0.5, cites: [{source: S6, locator: "pp. 119–120"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S7, locator: "Apprenticeships (Platonic Academy)"}], how_known: "Medici Academy / Ficino circle contact reported; not traced to a belief model here."}
  circle_present: {value: "no", rationale: "Personal redeeming Christ; B UNKNOWN — no lawful-order statement.", certainty: 0.5, cites: [{source: S4, locator: "p. 230"}, {source: S5, locator: "G 285"}], how_known: "Coder's reading of scored poems."}
  reading: "Late Christian devotion (cross, blood, faith-as-gift); earlier Neoplatonic ascent in love poetry noted but not the LIO score."
  notes: "Belief model only; H1 not tested. B UNKNOWN under P16."

institutions:
  - {value: "Medici household of Lorenzo de' Medici", role: protégé, kind: "patron or funder", certainty: 0.7, cites: [{source: S1, locator: "'Early life and works'"}], how_known: "Britannica."}
collaborators:
  - {value: "Domenico Ghirlandaio", relation: teacher, certainty: 0.7, cites: [{source: S1, locator: "'Early life and works'"}], how_known: "Britannica."}
  - {value: "Giorgio Vasari", relation: correspondent, certainty: 0.7, cites: [{source: S2, locator: "note to Sonnet LXV"}, {source: S1, locator: "opening section"}], how_known: "Biographer (S1) and recipient of Sonnet LXV (S2)."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 59"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags: []
  open_questions:
    - "B_cause: any statement of his own on nature's causal order (creation, miracles in nature, anatomy-as-science)? None found in poems read; Condivi/Vasari and the full Carteggio still largely unread on that point."
    - "Baptism / Secular Franciscan enrollment: Wikipedia alleges Secular Franciscan with 'better source needed'; not entered."
    - "Score PLATO as secondary_system if the Cavalieri/Colonna corpus is treated as a second adult system."
    - "Ramsden Letters of Michelangelo or Carteggio critical edition — check devotion language beyond Eisenbichler's quotations."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Creighton E. Gilbert"
    citation: "Gilbert, Creighton E. \"Michelangelo.\" Encyclopaedia Britannica, updated 15 October 2026. https://www.britannica.com/biography/Michelangelo."
    url: "https://www.britannica.com/biography/Michelangelo"
    accessed: 2026-10-15
    reliability_note: "Signed body (opening and 'Early life and works'); Top Questions not cited. Full later-life body not re-fetched this pass (Cloudflare 403 on 2026-10-24); Wikipedia EN used for later dates."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: primary
    kind: "scholarly edition"
    author: "Michelangelo Buonarroti; trans. John Addington Symonds"
    year: 1878
    citation: "The Sonnets of Michael Angelo Buonarroti and Tommaso Campanella. Trans. John Addington Symonds. 1878. Project Gutenberg eBook #10314."
    url: "https://www.gutenberg.org/ebooks/10314"
    accessed: 2026-10-15
    reliability_note: "Rhymed English from Guasti's autograph-based text. Used only as EN cross-check after Italian primary (S4/S5); wording of LXV checked against Guasti OCR. Unofficial web copy."
    source_quality: "unofficial web copy"
    used_for: [basics, worldview, timing, lane_b, collaborators]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    reliability_note: "Study's own roster."
    used_for: [identity, review]

  - id: S4
    type: primary
    kind: "scholarly edition"
    author: "Michelangelo Buonarroti; ed. Cesare Guasti"
    year: 1863
    citation: "Buonarroti, Michelangelo. Le Rime di Michelangelo Buonarroti, pittore scultore e architetto, cavate dagli autografi e pubblicate da Cesare Guasti. Florence: Felice Le Monnier, 1863. Internet Archive OCR: https://archive.org/details/bub_gb_S6-0x834F-EC (bub_gb_S6-0x834F-EC_djvu.txt). Sonnets to Vasari at printed pp. 230–232 (Giunto è già; Le favole del mondo), with covering letters of 19 September 1554 and the 1555 pair."
    url: "https://archive.org/details/bub_gb_S6-0x834F-EC"
    accessed: 2026-10-24
    reliability_note: "Standard 19th-c. edition from the autographs. Read in IA OCR only; page numbers from OCR running headers (pp. 230–232). Italian wording of G 285/288 checked against Wikisource/Girardi (S5)."
    source_quality: "archive scan (OCR only)"
    used_for: [worldview, timing, collaborators]

  - id: S5
    type: primary
    kind: "scholarly edition"
    author: "Michelangelo Buonarroti; ed. Enzo Noè Girardi (via Wikisource)"
    year: 1960
    citation: "Buonarroti, Michelangelo. Rime. Ed. Enzo Noè Girardi. Bari: Laterza, 1960 (BEIC). Italian Wikisource transcription: G 285 Giunto è già 'l corso della vita mia; G 288 Le favole del mondo m'hanno tolto; G 289 Non è più bassa o vil cosa terrena; G 290 Scarco d'un'importuna e greve salma. https://it.wikisource.org/wiki/Rime_(Michelangelo)"
    url: "https://it.wikisource.org/wiki/Rime_(Michelangelo)/285._Giunto_%C3%A8_gi%C3%A0_%27l_corso_della_vita_mia"
    accessed: 2026-10-24
    reliability_note: "Modern critical numbering (Girardi). Wikisource transcription of the 1960 BEIC text; used to confirm Guasti Italian and to quote G 289–290. Not a facsimile of the autograph."
    source_quality: "primary / own words"
    used_for: [worldview]

  - id: S6
    type: secondary
    kind: "journal article"
    author: "Konrad Eisenbichler"
    year: 1987
    citation: "Eisenbichler, Konrad. The Religious Poetry of Michelangelo: The Mystical Sublimation. Renaissance and Reformation / Renaissance et Réforme 23, no. 1 (1987): 123–136. https://jps.library.utoronto.ca/index.php/renref/article/download/11976/8857/24081"
    url: "https://jps.library.utoronto.ca/index.php/renref/article/download/11976/8857/24081"
    accessed: 2026-10-24
    reliability_note: "Peer-reviewed article. Quotes Carteggio letters (1516 on father's sacraments; 1548 on Giovansimone) and Italian lines of G 285 and G 290. Letter locators are the article's; manuscripts not checked here."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview, heritage, lane_b]

  - id: S7
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Michelangelo. Wikipedia. https://en.wikipedia.org/wiki/Michelangelo (Early life; Notable work dates; Personal life — Faith; Relationships and poetry)."
    url: "https://en.wikipedia.org/wiki/Michelangelo"
    accessed: 2026-10-24
    reliability_note: "Used for dual-source bio dates (with S1) and Catholic-faith summary (with S6). Poem 285 EN paraphrase not used alone for LIO. Secular Franciscan claim marked 'better source needed' there — not entered."
    source_quality: "reference entry"
    used_for: [basics, contribution, timing, worldview, heritage, lane_b]

---
# Michelangelo

> Status: draft — unreviewed. Deepen D1 (2026-10-24). Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Michelangelo (1475–1564), Italian sculptor, painter, architect and poet [S1; S7]. Primary system CHRIST at 0.7; A 0 @0.7 corroborated; B UNKNOWN (P16); C 1 and D 1 at 0.5 corroborated; mid_basin BELOW_THRESHOLD. Unplotted.

## Life and work

Born Caprese (Republic of Florence); worked in Florence, Bologna and Rome [S1; S7]. Apprenticed to Ghirlandaio; under Lorenzo de' Medici [S1; S7]. First Western artist with a biography published in his lifetime (Vasari 1550; Condivi 1553) [S1; S7].

## Contribution and impact

Pietà (completed 1499), David (1504), Sistine Chapel ceiling (1508–1512), Last Judgment (1536–1541) [S1; S7].

## Childhood and education

Apprenticed to Ghirlandaio at 13; briefly at the Medici household / Platonic Academy circle [S1; S7].

## Adult working worldview

Late spiritual sonnets (Italian primary): the soul turns to the divine love that opened its arms on the cross (G 285, 1554) [S4; S5]; worldly fables stole time given to contemplate God (G 288) [S4; S5]; Christ's blood alone washes his sins (G 290) [S5; S6]. Letters urge the sacraments for dying kin [S6]. No statement found on nature's causal order for B [P16].

## Heritage (context only)

Florentine; Catholic milieu [S1; S6; S7].

## Timing

First lasting contribution 1498/99 (Pietà), age about 23–24 [S1; S7]. Major-work span coded 1498–1541; scored LIO poems after that span [S4; S7].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No circle; B UNKNOWN [S4; S5].

## Open questions

- Any B-capable statement on nature in the full Carteggio or Condivi/Vasari?
- Baptism / alleged Secular Franciscan enrollment.
- Whether to code PLATO as secondary_system for the Cavalieri/Colonna phase.

## Research log

- 2026-10-15: Read Britannica (Gilbert, opening and early works) and Symonds's Sonnet LXV with note (Gutenberg #10314).
- 2026-10-24 (deepen D1, queue #59): Guasti 1863 IA OCR (S4) pp. 230–232; Wikisource/Girardi G 285, 288, 289, 290 (S5); Eisenbichler 1987 PDF (S6); Symonds LXV–LXXIII re-check (S2); Wikipedia EN (S7). Britannica re-fetch 403. Searched 'natura' poems (G 69, G 19) — beauty/love, not B. No fallacy_catalog (Jason).
