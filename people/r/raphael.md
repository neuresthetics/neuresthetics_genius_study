---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch J)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to visual_arts. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch J, order P32: F 5, rank 66). Basics from Britannica (Britannica Editors, unsigned; body through the Perugia years) and the School of Athens date from Britannica's Plato article (Meinwald). No worldview statement read. primary_system UNKNOWN; A, B, C, D, E UNKNOWN; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Audit fixes (fallacy_catalog audit of 81b9098, run 1). mid_basin BELOW_THRESHOLD -> UNKNOWN (P19)."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #65, F5 rank 66). Needs: A UNKNOWN; B UNKNOWN. Dual bio Wikipedia EN (S4) + retained Britannica Editors (S1; live Cloudflare-blocked, Wayback Top Questions/facts). Primary letters: IRDS/Shearman 1 Jul 1514 to uncle Simone Ciarla (S5) — 'ringratione Dio del continuo' (conventional thanksgiving for not marrying) and St Peter's as 'primo tempio del mondo' (career/architecture); Wikisource Visconti Letter to Leo X c.1519 (S6; co-draft with Castiglione debated) — antiquities survey, 'patria universale di tutti li cristiani' (civic address to the Pope), not a creed. IRDS/Shearman sonnet draft c.1509–10 (S7) — 'arcana Dei' = Paul's ineffability as Petrarchan love metaphor, not theology. Vasari last rites / Pantheon burial via Wikipedia (S4) = practice report, not own-word A. A stays UNKNOWN (checked items off-point for locus; P19); B stays UNKNOWN (P16 — not a scientist; no nature-causal statement). primary_system UNKNOWN (CHRIST = heritage/milieu lead only; religious commissions ≠ avowed belief). mid_basin UNKNOWN. Working years 1504–1520 @0.7. P47 on S1–S7. Chart-moving NO. No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: raphael
  display_name: "Raphael"
  roster:
    canonical_name: "Raphael"
    rank: 66
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: art
    field_bucket: arts
  full_name: {value: "Raffaello Sanzio da Urbino", certainty: 0.7, cites: [{source: S1, locator: "header ('Also known as')"}, {source: S4, locator: "lede (Raffaello Sanzio da Urbino)"}], how_known: "Britannica Raffaello Sanzio/Santi; Wikipedia full form with da Urbino (dual-source)."}
  native_name: {value: "Raffaello Sanzio", certainty: 0.7, cites: [{source: S4, locator: "lede"}], how_known: "Italian, Latin script (Wikipedia)."}
  aliases:
    - {name: "Raffaello Santi", kind: other}
    - {name: "Raffaello Sanzio", kind: other}

basics:
  birth:
    date: {value: "1483-04-06", calendar: julian, certainty: 0.5, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "infobox; Private life and death (Good Friday / Vasari)"}], how_known: "Britannica gives 6 April 1483; Wikipedia notes 28 March or 6 April (Vasari: both birth and death on Good Friday; 1483 Good Friday = 28 March). Contested day — 0.5 (P25). Julian."}
    place: {value: "Urbino, Duchy of Urbino", modern_name: "Urbino, Italy", polity_then: "Duchy of Urbino", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "infobox"}], how_known: "Britannica and Wikipedia EN."}
  death:
    date: {value: "1520-04-06", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "Private life and death"}], how_known: "Britannica and Wikipedia; Good Friday 6 April 1520. Julian."}
    place: {value: "Rome, Papal States", modern_name: "Rome, Italy", polity_then: "Papal States", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "infobox"}], how_known: "Britannica and Wikipedia."}
  first_lasting_contribution_year: {value: 1504, certainty: 0.7, cites: [{source: S1, locator: "'Apprenticeship at Perugia'"}, {source: S4, locator: "Early life — Marriage of the Virgin (1504)"}], how_known: "The Marriage of the Virgin (1504), Britannica 'first major work' / Wikipedia dual (P13)."}
  era_bucket: {value: "1400 to 1599", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "Whole life in the bucket (P2)."}
  region_of_birth: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Italy (P3)."}
  region_of_work: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "Early life; Roman period"}], how_known: "Urbino, Perugia, Florence, Rome."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [Italian], certainty: 0.7, cites: [{source: S5, locator: "letter Italian"}, {source: S6, locator: "letter Italian"}], how_known: "Surviving letters and sonnet draft in Italian."}
  occupations: {value: ["painter", "architect"], certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "lede"}], how_known: "Britannica and Wikipedia."}

contribution:
  primary_domain: visual_arts
  fields: {value: ["painting", "architecture"], certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "lede"}], how_known: "Britannica and Wikipedia."}
  lasting_original_contributions:
    - {value: "The Marriage of the Virgin", year: 1504, kind: work, lasting: "Britannica 'first major work' (S1); early large altarpiece (S4)", certainty: 0.7, cites: [{source: S1, locator: "'Apprenticeship at Perugia'"}, {source: S4, locator: "Early life — Brera Marriage of the Virgin"}], how_known: "Dual-sourced."}
    - {value: "School of Athens (Stanza della Segnatura)", year: 1511, kind: work, lasting: "Among the most famous High Renaissance frescoes (S1, S4)", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "'Life' ('School of Athens (1508–11)')"}, {source: S4, locator: "Vatican Raphael Rooms"}], how_known: "End year 1511 from Meinwald/Britannica and Wikipedia."}
    - {value: "The Transfiguration", year: 1520, kind: work, lasting: "Last major painting; unfinished at death (S1 Top Questions; S4)", certainty: 0.7, cites: [{source: S1, locator: "Top Questions / notable works (1516–20)"}, {source: S4, locator: "Notable work; Private life and death"}], how_known: "Britannica Top Questions dates 1516–20; Wikipedia agrees — death-year end used."}
  evidence_of_impact:
    - {value: "School of Athens among the most famous of Raphael's paintings; High Renaissance 'trinity' with Leonardo and Michelangelo", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "lede"}], how_known: "Britannica and Wikipedia."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1, S4).", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "lede"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Roman Catholic (milieu)", certainty: 0.5, cites: [{source: S4, locator: "Early life — uncle Bartolomeo a priest; categories Italian Roman Catholics"}], how_known: "Priest paternal uncle as guardian; Urbino Catholic court culture. No baptism record read — 0.5."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not read beyond uncle's clerical status."}
  parents_and_household:
    - {value: "Father Giovanni Santi, painter (d. 1494); mother Magia di Battista Ciarla (d. 1491); formal guardian paternal uncle Bartolomeo, a priest", role: parents, certainty: 0.7, cites: [{source: S1, locator: "'Early years at Urbino'"}, {source: S4, locator: "Early life and work"}], how_known: "Britannica and Wikipedia."}
  household_circumstances: {value: "Orphaned by 11; father connected with the court of Urbino; stepmother and father's workshop continued", certainty: 0.7, cites: [{source: S1, locator: "'Early years at Urbino'"}, {source: S4, locator: "Early life and work"}], how_known: "Britannica and Wikipedia."}
  schooling:
    - {value: "First painting instruction from his father", stage: home, run_by: family, certainty: 0.7, cites: [{source: S1, locator: "'Early years at Urbino'"}, {source: S4, locator: "Early life"}], how_known: "Britannica and Wikipedia."}
    - {value: "Workshop of Pietro Perugino, Perugia (pupil vs assistant debated)", stage: apprenticeship, run_by: private, certainty: 0.5, cites: [{source: S1, locator: "'Apprenticeship at Perugia'"}, {source: S4, locator: "Early life — Perugino"}], how_known: "Vasari apprenticeship disputed; influence clear by c.1500; 0.5."}
  early_mathematics: {value: UNKNOWN, how_known: "Not read."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not read."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "Pietro Perugino (workshop influence)", certainty: 0.5, cites: [{source: S1, locator: "'Apprenticeship at Perugia'"}, {source: S4, locator: "Early life"}], how_known: "Dual-sourced; exact pupil status debated."}
  languages_in_childhood: {value: UNKNOWN, how_known: "Italian assumed; not sourced."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1504–1520", certainty: 0.7, cites: [{source: S1, locator: "Marriage of the Virgin; Transfiguration 1516–20"}, {source: S4, locator: "Early life; Private life and death"}], how_known: "Equals timing.major_work_period (P30): first lasting 1504 through Transfiguration unfinished at death 1520."}
  nominal_affiliations:
    - {value: "Roman Catholic (papal court painter/architect; Groom of the Chamber; burial with last rites)", role: member, certainty: 0.5, cites: [{source: S4, locator: "Private life and death — last rites, Pantheon; Golden Spur"}, {source: S5, locator: "Santità di N. S.; fabrica de Santo Petro"}], how_known: "Lifelong papal employment and Vasari/Wikipedia death rites — institutional/milieu membership, not a scored creed profession."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not a scientist; no science–religion remark read."}
  primary_system: {value: UNKNOWN, how_known: "No scorable adult profession of CHRIST (or any other system) in own words. Checked and off-point for creed: (1) S5 'ringratione Dio del continuo' — conventional thanksgiving for avoiding marriage; (2) S5/S6 St Peter's / 'patria universale di tutti li cristiani' — career and civic address to Leo X; (3) S7 'arcana Dei' — love-sonnet metaphor from Paul, not theology; (4) religious commissions and Vasari last rites (S4) ≠ avowed belief. CHRIST remains heritage/milieu lead only."}
  secondary_system: {value: UNKNOWN, how_known: "Britannica/Wikipedia 'Neoplatonic ideal of human grandeur' describes the art, not an avowed PLATO system."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Lead only: Catholic milieu, papal patronage, formulaic 'ringratione Dio', deathbed confession/last rites (S4). Not scored — no own-word redeeming/personal God statement of Michelangelo type."}
    - {code: PLATO, reason: "Rejected: 'Neoplatonic ideal' is art-historical description of form (S1/S4), not his philosophical profession."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Sources read say nothing on locus of the divine (P19). Checked off-point: S5 'ringratione Dio' (conventional thanks); S6 'divinità di quegli animi antichi' / 'simile a Dio' (excellence/flattery metaphors); S7 'arcana Dei' (Petrarchan love); Vasari last rites (S4) = practice report, not A statement. Named alternative if a personal God profession appears in full Shearman REMS: A 0."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30/P33). No statement of his own on nature's causal order (P16). Leo X letter on ruins and 'corso naturale' is about Rome's historical fate, not physical law. Vitruvius margin notes unread this pass."}
    C_ledger: {value: UNKNOWN, how_known: "Deathbed confession (S4 Vasari/Wikipedia) is practice report, not his ledger statement; no poem or letter on sin/grace of Michelangelo type."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read (P7)."}
  mid_basin: {value: UNKNOWN, how_known: "A is UNKNOWN; UNKNOWN takes precedence (P19)."}
  statements:
    - text: "Prima circa a tor don[n]a, ve rispondo che quella che voi mi volisti dare prima, ne son contentissimo, e ringratione Dio del continuo, di non haver tolta né quella né altra, et in questo son stato più savio di voi, che me la volevi dare."
      cites: [{source: S5, locator: "IRDS #2490 / Shearman REMS transcription — letter 1 July 1514"}]
      date: "1514-07-01"
      context: "Private letter to uncle Simone Ciarla in Urbino: refuses an earlier match, reports Roman income and St Peter's fabric post under Leo X."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Formulaic thanksgiving ('ringratione Dio del continuo') for not marrying — social/conventional, not a locus profession. Not used to score A."
    - text: "Ma quallocho è più degno al mondo che Roma, qual impresa è più degna di Santo Petro, ch'è il primo tempio del mondo, e che questa è la più gran fabrica che sia mai vista, ché montarà più d'un millione d'oro?"
      cites: [{source: S5, locator: "IRDS #2490 — same letter 1 July 1514"}]
      date: "1514-07-01"
      context: "Same letter: career pride in succeeding Bramante on St Peter's."
      axes: []
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "'Primo tempio del mondo' = architectural/prestige ranking of the building project, not a creed statement."
    - text: "Onde, se ad ognuno è debito la pietà verso i parenti e la patria, tengomi obbligato di esporre tutte le piccole forze mie, acciocché più che si può resti viva un poco dell'immagine, e quasi l'ombra di questa, che in vero è patria universale di tutti li cristiani…"
      cites: [{source: S6, locator: "Wikisource Visconti 1840 ed. — Lettera a Leone X; cf. Hart & Hicks EN in S8"}]
      date: "1519"
      context: "Letter to Pope Leo X (Mantua/Munich MSS; co-authorship with Baldassare Castiglione debated) urging a survey to halt destruction of Roman antiquities."
      axes: []
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "'Patria universale di tutti li cristiani' addresses the Pope in civic/heritage rhetoric. Not a personal CHRIST profession. Collaborative drafting caveat (Castiglione)."
    - text: "Como non podde dir d'arcana Dei / Paul como diseso fu dal cello / così el mi[o] cor d'uno amoroso vello / a ricoperto tuti i penser mei"
      cites: [{source: S7, locator: "IRDS #2029 / Shearman REMS pp. 132–34 — Ashmolean Parker 547v"}]
      date: "1509"
      context: "Draft sonnet c.1509–10: compares the lover's silence to St Paul's inability to speak of God's secrets after the third heaven."
      axes: [A_locus]
      kind: "unpublished manuscript"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Biblical allusion as Petrarchan love conceit — not theology. Off-point for A."
  changes_over_life: []
  coder_notes: "Deepen D1 2026-10-24 (queue #65): Thin own-word corpus — do not code CHRIST/A 0 from papal patronage, formulaic Dio, or Vasari last rites. Pattern closer to Picasso thin-source caution than Michelangelo sonnet depth. B permanently likely UNKNOWN unless Vitruvius notes or a nature remark surfaces in full Shearman REMS. Chart-moving NO. No fallacy_catalog (Jason)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Urbinate (central Italian)", certainty: 0.7, cites: [{source: S1, locator: "'Early years at Urbino'"}, {source: S4, locator: "Early life"}], how_known: "Britannica and Wikipedia."}
  religious_heritage_by_birth: {value: "Roman Catholic", certainty: 0.5, cites: [{source: S4, locator: "Early life — priest uncle guardian; categories"}], how_known: "Milieu inference; baptism record not read."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "No baptism record read this pass."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not read."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1504–1520", certainty: 0.7, cites: [{source: S1, locator: "Marriage of the Virgin; Transfiguration 1516–20"}, {source: S4, locator: "Early life; Notable works"}], how_known: "First to last dated listed contribution (P29, P30)."}
  age_at_first_lasting_contribution: {value: 21, certainty: 0.5, cites: [{source: S1, locator: "opening; 'Apprenticeship at Perugia'"}, {source: S4, locator: "birth-date ambiguity"}], how_known: "1504 − 1483 = 21; birth day contested so 0.5."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No LIO-scorable statement; letters checked off-point."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S5, locator: "letter"}, {source: S6, locator: "letter"}, {source: S7, locator: "sonnet"}], how_known: "Own words in working years checked; none score A/B."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Axes UNKNOWN."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "High Renaissance clarity of form, pyramidal Holy Families, architectural perspective in School of Athens and St Peter's work (S1, S4) — form in the art, not a worldview score.", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "lede; Architecture"}], how_known: "Coder's reading of dual bio."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Training path clear; H1 acquisition not tested."}
  circle_present: {value: "unclear", rationale: "No worldview statement that would feed H1 circle.", certainty: 0.5, cites: [{source: S5, locator: "letters checked"}], how_known: "Coder's reading."}
  reading: "Lane B only: geometric form present in the work; no H1 circle from worldview. Form ≠ A/B score."
  notes: "Do not treat Neoplatonic art description as PLATO worldview."

institutions:
  - {value: "Pope Julius II / Leo X (Vatican Stanze; St Peter's fabric)", role: painter and architect, kind: "patron or funder", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "Roman period"}, {source: S5, locator: "fabrica de Santo Petro"}], how_known: "Britannica, Wikipedia, Simone letter."}
collaborators:
  - {value: "Pietro Perugino", relation: teacher, certainty: 0.5, cites: [{source: S1, locator: "'Apprenticeship at Perugia'"}, {source: S4, locator: "Early life"}], how_known: "Workshop influence; pupil status debated."}
  - {value: "Donato Bramante", relation: other, certainty: 0.7, cites: [{source: S4, locator: "Architecture — succeeded Bramante 1514"}, {source: S5, locator: "in locho di Bramante"}], how_known: "Wikipedia and Simone letter."}
  - {value: "Baldassare Castiglione", relation: collaborator, certainty: 0.5, cites: [{source: S6, locator: "Letter to Leo X co-draft debate"}, {source: S8, locator: "Hart & Hicks attribution"}], how_known: "Letter to Leo X often ascribed jointly; 0.5."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 66"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Birth day contested (28 March vs 6 April 1483)."
    - "Letter to Leo X may be co-drafted with Castiglione — not treated as pure solo creed evidence."
  open_questions:
    - "Full Shearman REMS 2003 corpus for any non-formulaic religious own-word beyond S5–S7."
    - "Vitruvius (Munich) margin notes — any nature-causal remark for B?"
    - "Baptism / parish record at Urbino."
    - "Golzio / Camesasca scritti editions cross-check of Simone and Leo X texts."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "Britannica Editors. \"Raphael.\" Encyclopaedia Britannica, updated 11 September 2026. https://www.britannica.com/biography/Raphael-Italian-painter-and-architect."
    url: "https://www.britannica.com/biography/Raphael-Italian-painter-and-architect"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Unsigned editors' body (original collect through Perugia); live 2026-10-24 Cloudflare-blocked; Wayback used for Top Questions (Transfiguration 1516–20, family). Top Questions cited only where dual-checked with Wikipedia."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: secondary
    kind: encyclopedia
    author: "Constance C. Meinwald"
    citation: "Meinwald, Constance C. \"Plato.\" Encyclopaedia Britannica, updated 28 August 2026. https://www.britannica.com/biography/Plato."
    url: "https://www.britannica.com/biography/Plato"
    accessed: 2026-10-15
    source_quality: "reference entry"
    reliability_note: "Signed body; dates the School of Athens 1508–11."
    used_for: [contribution, timing]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    source_quality: "study roster"
    reliability_note: "Study's own roster."
    used_for: [identity, review]
  - id: S4
    type: secondary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia contributors. \"Raphael.\" Wikipedia, The Free Encyclopedia. https://en.wikipedia.org/wiki/Raphael (accessed 24 October 2026)."
    url: "https://en.wikipedia.org/wiki/Raphael"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Dual-source bio with Britannica (P50). Early life, Roman period, Private life and death (last rites, Pantheon, engagement). Not used alone for worldview scores."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators, review]
  - id: S5
    type: primary
    kind: letter
    author: "Raffaello Sanzio (transcr. John Shearman)"
    citation: "Raphael to Simone di Battista Ciarla, Rome, 1 July 1514. Italian Renaissance Document Site #2490, transcription from John Shearman, Raphael in Early Modern Sources (1483–1602) (Yale / Bibliotheca Hertziana, 2003), via Pungileoni."
    url: "https://irds-project.org/doc/2490/"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "Scholarly transcription (Shearman REMS) of personal letter. Primary for own words; Italian text read in full."
    used_for: [worldview, basics, institutions, collaborators, timing]
  - id: S6
    type: primary
    kind: letter
    author: "Raffaello Sanzio (ed. Visconti 1840; cf. Shearman / Di Teodoro)"
    citation: "Raffaello Sanzio. Lettera di Raffaello d'Urbino a papa Leone X. Ed. Visconti, 1840. Italian Wikisource. Cf. Shearman REMS; Hart & Hicks translation in Palladio's Rome (Yale, 2006)."
    url: "https://it.wikisource.org/wiki/Lettera_di_Raffaello_d%27Urbino_a_papa_Leone_X_(ed._Visconti)/Lettera_di_Raffaello_d%27Urbino_a_papa_Leone_X"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "19th-c. Visconti edition on Wikisource; co-authorship with Castiglione debated (Hart & Hicks; Di Teodoro). Used for antiquities/civic phrasing only, not creed."
    used_for: [worldview, collaborators]
  - id: S7
    type: primary
    kind: "other"
    author: "Raffaello Sanzio (transcr. John Shearman)"
    citation: "Raphael, draft sonnet ('Como non podde dir d'arcana Dei…'), c.1509–10. Ashmolean Parker 547v. IRDS #2029 from Shearman, Raphael in Early Modern Sources, pp. 132–34."
    url: "https://irds-project.org/doc/2029/"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "Scholarly transcription of autograph draft; heavily revised Petrarchan love poem."
    used_for: [worldview]
  - id: S8
    type: secondary
    kind: "book chapter"
    author: "Vaughan Hart and Peter Hicks"
    citation: "Hart, Vaughan, and Peter Hicks. \"The Letter to Leo X by Raphael and Baldassare Castiglione, c.1519.\" In Palladio's Rome: A Translation of Andrea Palladio's Two Guidebooks to Rome, 179–92. New Haven: Yale University Press, 2006."
    url: "https://en.wikiquote.org/wiki/Raphael"
    accessed: 2026-10-24
    source_quality: "scholarly edition or monograph"
    reliability_note: "EN translation excerpt via Wikiquote pointing to Hart & Hicks; used only to note Castiglione co-attribution and confirm opening lines. Full book unread."
    used_for: [worldview, collaborators]
---

# Raphael

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Raphael (Raffaello Sanzio da Urbino, 1483–1520), Italian High Renaissance painter and architect [S1, S4]. Deepen D1: surviving letters and a love-sonnet draft checked; no scorable A or B statement. A UNKNOWN; B UNKNOWN; primary_system UNKNOWN; mid_basin UNKNOWN. Not plotted.

## Life and work

Born Urbino (day contested: 28 March or 6 April 1483) [S1, S4]. Orphaned young; Perugino workshop influence; Florence years; from 1508 Rome under Julius II and Leo X — Vatican Stanze, St Peter's fabric after Bramante [S1, S4, S5]. Died Rome 6 April 1520; buried in the Pantheon after confession and last rites (Vasari via S4).

## Contribution and impact

Marriage of the Virgin (1504); School of Athens (by 1511); Transfiguration (unfinished, 1520) [S1, S2, S4]. Traditional High Renaissance trinity with Leonardo and Michelangelo [S1, S4].

## Childhood and education

Father Giovanni Santi; mother Magia Ciarla; priest uncle Bartolomeo as guardian [S1, S4]. First lessons at home; Perugino workshop (pupil vs assistant debated) [S1, S4].

## Adult working worldview

Own words in the working years do not score LIO axes [S5, S6, S7]. Letter to Simone Ciarla (1 July 1514): conventional "ringratione Dio" for not marrying; St Peter's as career "primo tempio del mondo" [S5]. Letter to Leo X (c.1519): antiquities preservation; "patria universale di tutti li cristiani" as civic address — Castiglione co-draft debated [S6, S8]. Sonnet draft c.1509–10: "arcana Dei" as love metaphor from Paul, not theology [S7]. Religious commissions and deathbed rites are not avowed belief [S4]. A UNKNOWN; B UNKNOWN (P16); CHRIST heritage/milieu lead only.

## Heritage (context only)

Urbinate Italian; Roman Catholic milieu (priest uncle; papal court) [S1, S4]. Baptism record not read.

## Timing

Major work period 1504–1520 [S1, S4]. No LIO-type views found in own words checked.

## Lane B notes (labeled belief model)

Geometric form present in the paintings and architecture [S1, S4]. No H1 circle from worldview. Form ≠ A/B score. "Neoplatonic ideal" is art description, not PLATO system.

## Open questions

- Full Shearman REMS 2003 for any non-formulaic religious own-word.
- Vitruvius Munich margin notes for any B-capable nature remark.
- Urbino baptism record.
- Golzio / Camesasca cross-check of letter texts.

## Research log

- 2026-10-15: Read Britannica (Editors) body through Perugia, and the Plato article for the School of Athens date.
- 2026-10-24 (D1): Wikipedia EN dual bio; IRDS Shearman Simone letter #2490 and sonnet #2029; Wikisource Visconti Leo X letter; Wikiquote/Hart & Hicks attribution note; Britannica live Cloudflare-blocked (Wayback Top Questions). No fallacy_catalog.
