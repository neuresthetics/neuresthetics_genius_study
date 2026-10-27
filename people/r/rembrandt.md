---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch K)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to early_modern. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch K, order P32: F 5, rank 67). Basics from Britannica (Ernst van de Wetering), signed body through 'Early years' only; Top Questions not cited. No worldview statement read. primary_system UNKNOWN; A, B, C, D, E UNKNOWN; mid_basin UNKNOWN (P19). Not plotted. Draft, not reviewed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #66, F5 rank 67). Needs: A UNKNOWN; B UNKNOWN; 1 source. Dual bio Wikipedia EN (S3) + retained Britannica van de Wetering (S1; live Cloudflare-blocked; Wayback TOC/early body). Primary: only surviving letters — to Constantijn Huygens c.1636–39 (S4 Hofstede de Groot / Binstock EN; S5 Wikiquote Dutch of 12 Jan 1639) — conventional closings ('commend… to God', 'blessing of salvation') and art goal 'meeste ende… naetuereelste beweechgelickheijt' (greatest and most natural movement) = pictorial emotion/motion, not nature's causal order (P16). Wheelock Leiden Collection (S6): family Remonstrant lean; 'Rembrandt's own religious views are not known'. Mother Catholic / father Dutch Reformed (S3). Biblical history pieces ≠ avowed belief. A stays UNKNOWN (God closings off-point; P19); B stays UNKNOWN (P16). primary_system UNKNOWN (CHRIST/Reformed heritage lead only). mid_basin UNKNOWN. Working years 1632–1669 @0.7. P47 on S1–S6. Chart-moving NO. Thin-source caution — no overclaim. No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: rembrandt
  display_name: "Rembrandt"
  roster:
    canonical_name: "Rembrandt"
    rank: 67
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: art
    field_bucket: arts
  full_name: {value: "Rembrandt Harmenszoon van Rijn", certainty: 0.7, cites: [{source: S1, locator: "header ('In full')"}, {source: S3, locator: "lede"}], how_known: "Britannica and Wikipedia EN."}
  native_name: {value: "Rembrandt Harmenszoon van Rijn", certainty: 0.7, cites: [{source: S3, locator: "lede"}], how_known: "Dutch, Latin script (Wikipedia)."}
  aliases:
    - {name: "Rembrandt van Rijn", kind: "roster alias"}

basics:
  birth:
    date: {value: "1606-07-15", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "infobox"}], how_known: "Britannica and Wikipedia; Holland used Gregorian."}
    place: {value: "Leiden, Dutch Republic", modern_name: "Leiden, Netherlands", polity_then: "Dutch Republic", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "infobox"}], how_known: "Britannica and Wikipedia."}
  death:
    date: {value: "1669-10-04", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "infobox; death"}], how_known: "Britannica and Wikipedia; buried Westerkerk (S3)."}
    place: {value: "Amsterdam, Dutch Republic", modern_name: "Amsterdam, Netherlands", polity_then: "Dutch Republic", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "infobox"}], how_known: "Britannica and Wikipedia."}
  first_lasting_contribution_year: {value: 1632, certainty: 0.7, cites: [{source: S3, locator: "Notable work — Anatomy Lesson of Dr. Nicolaes Tulp (1632)"}, {source: S1, locator: "opening (portrait fame; Night Watch dated)"}], how_known: "Anatomy Lesson (1632) — early public masterpiece; dual with Britannica career framing (P13). Prior collect used Night Watch 1642 only."}
  era_bucket: {value: "1600 to 1749", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "Whole life in the bucket (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Netherlands (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "Career"}], how_known: "Leiden, Amsterdam."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [Dutch], certainty: 0.7, cites: [{source: S4, locator: "letters Dutch originals via Hofstede de Groot"}, {source: S5, locator: "Dutch of 12 Jan 1639 letter"}], how_known: "Surviving letters in Dutch."}
  occupations: {value: ["painter", "printmaker", "draughtsman"], certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "lede"}], how_known: "Britannica and Wikipedia."}

contribution:
  era_bucket: early_modern
  fields: {value: ["painting", "printmaking", "drawing"], certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "lede"}], how_known: "Britannica and Wikipedia."}
  lasting_original_contributions:
    - {value: "The Anatomy Lesson of Dr. Nicolaes Tulp", year: 1632, kind: work, lasting: "Early Amsterdam group portrait masterpiece (S3)", certainty: 0.7, cites: [{source: S3, locator: "Notable work (1632)"}], how_known: "Wikipedia; career breakthrough as portraitist."}
    - {value: "Night Watch (Militia Company of District II under Frans Banninck Cocq)", year: 1642, kind: work, lasting: "Britannica: 'clearly a turning point in his stylistic development' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening section"}, {source: S3, locator: "Notable work (1642)"}], how_known: "Dual-sourced; end of 1640/42 range."}
    - {value: "Hundred Guilder Print (Christ Preaching)", year: 1649, kind: work, lasting: "Major etching summarizing Matthew 19 (S3)", certainty: 0.5, cites: [{source: S3, locator: "Notable work (c. 1647–1649)"}], how_known: "Wikipedia date range; end year used (0.5)."}
    - {value: "The Return of the Prodigal Son", year: 1669, kind: work, lasting: "Late biblical masterpiece (S3)", certainty: 0.5, cites: [{source: S3, locator: "Notable work (1661–1669)"}], how_known: "Wikipedia range; death-year end (0.5)."}
  evidence_of_impact:
    - {value: "From the Romantic era regarded as one of the greatest figures in art history; generally considered among the greatest visual artists in Western art", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening section"}, {source: S3, locator: "lede"}], how_known: "Britannica and Wikipedia."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1, S3).", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "lede"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Mixed: father Dutch Reformed; mother Catholic; family Remonstrant lean (secondary)", certainty: 0.5, cites: [{source: S3, locator: "Early life — mother Catholic, father Dutch Reformed"}, {source: S6, locator: "raised Protestant; Remonstrant sympathies"}], how_known: "Wikipedia parents' churches; Wheelock: family sympathies with Remonstrants vs Orthodox Calvinists — 0.5 (own views unknown)."}
  family_religious_practice: {value: UNKNOWN, how_known: "Denomination labels only; practice not detailed."}
  parents_and_household:
    - {value: "Father Harmen Gerritszoon van Rijn, miller (Dutch Reformed); mother Neeltgen Willemsdochter van Zuytbrouck, from a family of bakers (Catholic)", role: parents, certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}, {source: S3, locator: "Early life and education"}], how_known: "Britannica and Wikipedia."}
  household_circumstances: {value: "Well-to-do miller's family; fourth/ninth of several children (sources differ on birth order count); not from a family of artists", certainty: 0.5, cites: [{source: S1, locator: "'Early years' (fourth of six surviving of ten)"}, {source: S3, locator: "Early life (ninth child)"}], how_known: "Britannica vs Wikipedia birth-order wording differs — 0.5."}
  schooling:
    - {value: "Elementary school (c. 1612–16)", stage: "elementary school", run_by: other, certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
    - {value: "Latin School, Leiden (c. 1616–20): biblical studies and classics", stage: "grammar or secondary school", run_by: other, certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}, {source: S3, locator: "Early life — Latin school"}], how_known: "Britannica and Wikipedia."}
    - {value: "Enrolled at Leiden University, 20 May 1620, probably without attending", stage: university, run_by: other, certainty: 0.5, cites: [{source: S1, locator: "'Early years'"}, {source: S3, locator: "Early life"}], how_known: "Britannica: enrolment did not imply attendance."}
    - {value: "Trained with Jacob van Swanenburgh (Leiden, about three years), then Pieter Lastman (Amsterdam, six months)", stage: apprenticeship, run_by: private, certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}, {source: S3, locator: "Early life"}], how_known: "Britannica after Orlers; Wikipedia agrees."}
  early_mathematics: {value: UNKNOWN, how_known: "Not read."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not read."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "Jacob van Swanenburgh; Pieter Lastman (history painting)", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}, {source: S3, locator: "Early life"}], how_known: "Dual-sourced."}
  languages_in_childhood: {value: UNKNOWN, how_known: "Dutch assumed; Latin school implies Latin — not separately sourced as childhood languages field."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1632–1669", certainty: 0.7, cites: [{source: S3, locator: "Notable works 1632–1669"}, {source: S1, locator: "Night Watch turning point"}], how_known: "Equals timing.major_work_period (P30): Anatomy Lesson through late biblical/portrait work to death year."}
  nominal_affiliations:
    - {value: "Dutch Reformed / Protestant milieu (not a scored confessional profession)", role: member, certainty: 0.5, cites: [{source: S3, locator: "Early life — father Reformed; marriage church"}, {source: S6, locator: "raised as a Protestant; own views not known"}], how_known: "Family and civic Protestant context; Wheelock: own religious views unknown. Not coded as primary_system."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not a scientist; no science–religion remark read."}
  primary_system: {value: UNKNOWN, how_known: "No scorable adult profession of CHRIST or any other system in own words. Wheelock (S6): 'Rembrandt's own religious views are not known.' Checked off-point: (1) Huygens-letter closings invoking God/salvation (S4) — conventional epistolary formulas; (2) biblical history pieces and Passion commissions — subjects/commissions, not avowed belief (S1, S3); (3) Mennonite/Jewish/Remonstrant contacts (S6) — social/professional, not creed. CHRIST/Reformed = heritage lead only."}
  secondary_system: {value: UNKNOWN, how_known: "Remonstrant family lean (S6) is heritage context, not a scored second system."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Lead only: Protestant Reformed upbringing, Remonstrant family lean (S6), biblical oeuvre, letter formulas naming God/salvation. Not scored — no own-word redeeming/personal God statement; Wheelock states views unknown. Reformed/Remonstrant = heritage, not a separate systems/ code."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Sources read say nothing on locus of the divine (P19). Checked off-point: S4 letter closings ('commend… to God in health'; 'blessing of salvation, Amen'; 'God keep your lordship… and bless you') — conventional courtesy, not a locus profession. Biblical paintings are commissions/subjects. Named alternative if a personal God profession appears in fuller Urkunden: A 0."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30/P33). No statement of his own on nature's causal order (P16). Letter claim of 'meeste ende… naetuereelste beweechgelickheijt' (S4, S5) = greatest and most natural movement in the Passion paintings (emotional/physical motion in art) — same pattern as Picasso Zervos 'nature' / Michelangelo natura poems. Not B."}
    C_ledger: {value: UNKNOWN, how_known: "'Blessing of salvation' letter closing (S4) is formula, not a ledger statement."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read (P7)."}
  mid_basin: {value: UNKNOWN, how_known: "A and B UNKNOWN (P19)."}
  statements:
    - text: "want deesen twee sijnt daer die meeste ende die naetuereelste beweechgelickheijt in geopserveert is dat oock de grooste oorsaeck is dat die selvijge soo lang onder handen sij geweest."
      cites: [{source: S5, locator: "Wikiquote Dutch of letter 12 January 1639"}, {source: S4, locator: "Binstock EN: 'greatest and most natural movement'"}]
      date: "1639-01-12"
      context: "Letter to Constantijn Huygens delivering Entombment and Resurrection for Prince Frederik Hendrik's Passion series — explaining delay by the artistic goal of natural movement."
      axes: [B_cause]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Art-process claim (pictorial motion/emotion). Not scored for B under P16. EN from Binstock/Hofstede de Groot; Dutch from Wikiquote citing Strauss & van der Meulen Rembrandt Documents."
    - text: "I wish you all happiness and the blessing of salvation, Amen."
      cites: [{source: S4, locator: "Binstock EN — letter 12 January 1639 closing"}]
      date: "1639-01-12"
      context: "Same Huygens letter closing formula."
      axes: [A_locus, C_ledger]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Conventional epistolary blessing — off-point for A/C. EN only this pass (Dutch closing not separately pulled); not used to score."
    - text: "Along with my greetings [I] commend all of yours to God in health."
      cites: [{source: S4, locator: "Binstock EN — earlier Huygens letter closing"}]
      date: "1636"
      context: "Huygens correspondence on Passion commissions — closing courtesy."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Formulaic commendation to God. Off-point for A. Exact year of this letter in the Columbia set is early in the series (c.1636–39)."
    - text: "all are commended to God in long-lasting health… wishes God keep your lordship in good health and bless you"
      cites: [{source: S4, locator: "Binstock EN — later Huygens letters on payment"}]
      date: "1639"
      context: "Payment-chasing letters to Huygens, January 1639."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Same conventional pattern. Not used to score A."
  changes_over_life: []
  coder_notes: "Deepen D1 2026-10-24 (queue #66): Thin prior source count (1 bio) — only ~7 letters survive, all to Huygens. Do not code CHRIST/A 0 from formulaic God/salvation closings or biblical subjects. Wheelock explicitly: own religious views unknown. B permanently likely UNKNOWN unless a nature-causal remark surfaces. Chart-moving NO. No fallacy_catalog (Jason)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Dutch (Leiden)", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}, {source: S3, locator: "Early life"}], how_known: "Britannica and Wikipedia."}
  religious_heritage_by_birth: {value: "Dutch Reformed (father) with Catholic mother; Remonstrant family lean reported", certainty: 0.5, cites: [{source: S3, locator: "Early life"}, {source: S6, locator: "Remonstrant sympathies"}], how_known: "Mixed parental churches (S3); Wheelock Remonstrant lean (S6)."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Baptism record not read this pass."}
  childhood_catechism: {value: UNKNOWN, how_known: "Latin-school biblical studies noted (S1); not coded as catechism practice."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1632–1669", certainty: 0.7, cites: [{source: S3, locator: "Notable works"}, {source: S1, locator: "Night Watch"}], how_known: "First to last dated listed contribution (P29, P30)."}
  age_at_first_lasting_contribution: {value: 26, certainty: 0.7, cites: [{source: S3, locator: "Anatomy Lesson 1632; birth 1606"}], how_known: "1632 − 1606 = 26 (P30)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No LIO-scorable statement; Huygens letters checked off-point."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S4, locator: "letters"}, {source: S5, locator: "Dutch beweechgelickheijt"}], how_known: "Own words in working years checked; none score A/B."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Axes UNKNOWN."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "Strong chiaroscuro, compositional grouping (Anatomy Lesson, Night Watch) and late loose handling — pictorial structure present, but not Euclidean/geometric form emphasis of High Renaissance ideal (S1, S3).", certainty: 0.5, cites: [{source: S1, locator: "opening — light and shade; Night Watch"}, {source: S3, locator: "lede"}], how_known: "Coder's reading of dual bio."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Not tested for H1."}
  circle_present: {value: "unclear", rationale: "No worldview statement that would feed H1 circle.", certainty: 0.5, cites: [{source: S4, locator: "letters checked"}], how_known: "Coder's reading."}
  reading: "Lane B only: pictorial form partly present; no H1 circle from worldview. Form ≠ A/B score. 'Natural movement' is art technique, not Lane A B_cause."
  notes: "Do not treat biblical subject matter as CHRIST worldview."

institutions:
  - {value: "Court of Frederik Hendrik / Constantijn Huygens (Passion series)", role: painter, kind: "patron or funder", certainty: 0.7, cites: [{source: S3, locator: "Career — Huygens"}, {source: S4, locator: "letters"}], how_known: "Wikipedia and Huygens letters."}
  - {value: "Amsterdam Guild of St Luke", role: member, kind: "other", certainty: 0.7, cites: [{source: S3, locator: "Career — guild 1634"}], how_known: "Wikipedia."}
collaborators:
  - {value: "Pieter Lastman", relation: teacher, certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}, {source: S3, locator: "Early life"}], how_known: "Dual-sourced."}
  - {value: "Jacob van Swanenburgh", relation: teacher, certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}, {source: S3, locator: "Early life"}], how_known: "Dual-sourced."}
  - {value: "Jan Lievens", relation: collaborator, certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}, {source: S3, locator: "Career — shared Leiden studio"}], how_known: "Dual-sourced."}
  - {value: "Hendrick van Uylenburgh", relation: mentor or employer, certainty: 0.7, cites: [{source: S3, locator: "Career — stayed with Uylenburgh"}, {source: S6, locator: "Mennonite art dealer"}], how_known: "Wikipedia and Wheelock."}
  - {value: "Constantijn Huygens", relation: other, certainty: 0.7, cites: [{source: S3, locator: "Career"}, {source: S4, locator: "letters"}], how_known: "Court intermediary / correspondent."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 67"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Only about seven letters survive, all to Huygens; God/salvation language is formulaic."
    - "Britannica 'Rembrandt and religion' section Cloudflare-blocked this pass; Wheelock used for scholarly 'views unknown'."
    - "Birth-order count differs slightly Britannica vs Wikipedia."
  open_questions:
    - "Full Strauss & van der Meulen Rembrandt Documents / Hofstede de Groot Urkunden Dutch of all letter closings."
    - "Britannica van de Wetering 'Rembrandt and religion' body when unblocked."
    - "Baptism / membership records (Reformed vs Remonstrant)."
    - "Any inventory notes or reported speech with a locus claim (unlikely)."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Ernst van de Wetering"
    citation: "van de Wetering, Ernst. \"Rembrandt.\" Encyclopaedia Britannica, updated 30 September 2026. https://www.britannica.com/biography/Rembrandt-van-Rijn."
    url: "https://www.britannica.com/biography/Rembrandt-van-Rijn"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Signed body through 'Early years' from original collect; live 2026-10-24 Cloudflare-blocked including 'Rembrandt and religion' subsection; Wayback used for TOC/opening. Top Questions not cited alone."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, collaborators]
  - id: S2
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    source_quality: "study roster"
    reliability_note: "Study's own roster."
    used_for: [identity, review]
  - id: S3
    type: secondary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia contributors. \"Rembrandt.\" Wikipedia, The Free Encyclopedia. https://en.wikipedia.org/wiki/Rembrandt (accessed 24 October 2026)."
    url: "https://en.wikipedia.org/wiki/Rembrandt"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Dual-source bio with Britannica (P50). Early life (parental religions), Career, Notable works, death/Westerkerk. Not used alone for worldview scores."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators, review]
  - id: S4
    type: primary
    kind: letter
    author: "Rembrandt van Rijn (trans. Benjamin Binstock from Hofstede de Groot)"
    citation: "Rembrandt to Constantijn Huygens, c.1636–1639. English translation by Benjamin Binstock from C. Hofstede de Groot, Die Urkunden über Rembrandt (The Hague, 1906). Columbia Art Humanities reading PDF."
    url: "https://projects.mcah.columbia.edu/arthumanities/websites/remmon/pdf/art_hum_reading_30.pdf"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "EN teaching translation of the only surviving Rembrandt letters. Closings and payment content read in full; Dutch closings not independently verified this pass (see S5 for one Dutch body)."
    used_for: [worldview, basics, institutions, collaborators, timing]
  - id: S5
    type: primary
    kind: letter
    author: "Rembrandt van Rijn (Dutch text via Wikiquote / Strauss & van der Meulen)"
    citation: "Rembrandt to Constantijn Huygens, Amsterdam, 12 January 1639 (Dutch). Wikiquote 'Rembrandt' citing The Rembrandt Documents (Strauss & van der Meulen) / Painters on Painting (Protter)."
    url: "https://en.wikiquote.org/wiki/Rembrandt"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "Dutch of beweechgelickheijt passage; Wikiquote path to Rembrandt Documents — treated as scholarly transcription pointer, not a facsimile."
    used_for: [worldview, basics, timing]
  - id: S6
    type: secondary
    kind: "book chapter"
    author: "Arthur K. Wheelock Jr."
    citation: "Wheelock, Arthur K., Jr. \"Rembrandt as Universal Artist\" (2020). In The Leiden Collection Catalogue, 4th ed., edited by Arthur K. Wheelock Jr. and Elizabeth Nogrady with Caroline Van Cauwenberge. New York, 2023–. https://theleidencollection.com/essays/rembrandt-as-universal-artist/."
    url: "https://www.theleidencollection.com/essays/rembrandt-as-universal-artist/"
    accessed: 2026-10-24
    source_quality: "scholarly edition or monograph"
    reliability_note: "Signed scholarly catalogue essay. States family Remonstrant lean and that Rembrandt's own religious views are not known; notes Mennonite/Jewish contacts."
    used_for: [worldview, childhood, heritage, collaborators]
---

# Rembrandt

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Rembrandt Harmenszoon van Rijn (1606–1669), Dutch Golden Age painter and printmaker [S1, S3]. Deepen D1: only surviving letters (to Huygens) checked; formulaic God/salvation closings and "natural movement" art goal do not score A or B. Wheelock: own religious views unknown [S6]. A UNKNOWN; B UNKNOWN; primary_system UNKNOWN; mid_basin UNKNOWN. Not plotted.

## Life and work

Born Leiden; Latin school; apprenticeships with van Swanenburgh and Lastman; Leiden studio with Lievens; from 1631/32 Amsterdam [S1, S3]. Married Saskia van Uylenburgh 1634; insolvency 1656; died Amsterdam 4 October 1669, buried Westerkerk [S3].

## Contribution and impact

Anatomy Lesson (1632); Night Watch (1642); Hundred Guilder Print (c.1649); late Return of the Prodigal Son [S1, S3]. International fame for etchings in his lifetime [S1].

## Childhood and education

Father Reformed miller; mother Catholic baker's daughter; Remonstrant family lean reported [S3, S6]. Latin School biblical/classics; brief Leiden University enrolment; Lastman for history painting [S1, S3].

## Adult working worldview

Few writings survive — letters to Huygens only [S4]. Closings commend addressees to God and wish the "blessing of salvation" — conventional formulas, not locus professions [S4]. Artistic aim: "meeste ende… naetuereelste beweechgelickheijt" (greatest and most natural movement) in Passion paintings — art process, not B under P16 [S4, S5]. Biblical subjects and Passion commissions ≠ avowed belief [S1, S3]. Wheelock: own religious views not known [S6]. A UNKNOWN; B UNKNOWN; CHRIST/Reformed heritage lead only.

## Heritage (context only)

Dutch Leiden; mixed parental churches; Remonstrant lean [S3, S6]. Baptism record not read.

## Timing

Major work period 1632–1669 [S3]. No LIO-type views found in own words checked.

## Lane B notes (labeled belief model)

Pictorial form partly present (chiaroscuro, group composition) [S1, S3]. No H1 circle from worldview. "Natural movement" ≠ Lane A B_cause.

## Open questions

- Full Dutch Urkunden / Rembrandt Documents for all letter closings.
- Britannica "Rembrandt and religion" when unblocked.
- Baptism / church membership records.
- Any non-formulaic locus statement (unlikely).

## Research log

- 2026-10-15: Read Britannica (van de Wetering) opening and 'Early years'.
- 2026-10-24 (D1): Wikipedia EN dual bio; Huygens letters (Binstock/Hofstede de Groot PDF + Wikiquote Dutch); Wheelock Leiden Collection essay; Britannica live Cloudflare-blocked. No fallacy_catalog.
