---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA10; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to astronomy. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA10, order P32: F 3, rank 220). Source: Britannica scholars edition, signed by Olin Jeuck Eggen (read in full). Lasting: his body of accurate naked-eye observations, 'the most accurate possible before the invention of the telescope', which 'paved the way for future discoveries'; 'What Tycho accomplished ... remains an outstanding accomplishment of the Renaissance'; with his data 'Kepler laid the groundwork for the work of Sir Isaac Newton' (S1). Dated from De nova stella (1573), the first published result of the programme, to his leaving Uraniborg (1597), where 'The major portion of Tycho's lifework ... had already been done'. Span 1573–1597 at 0.5 (alternative start 1576, the Ven grant), age 27. Scientist: B 3 at 0.5, alt 4 (P35). Worldview UNKNOWN. Not plotted. Draft, not reviewed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen D1 (queue #207/228, F 3, rank 220): firm B; seek any A from De nova stella / letters; do not force plot. Read De nova stella 1573 in McLaughlin English from Dreyer Opera Omnia (S3) cross-checked to tekstnet Latin (S4); Håkansson 2004 quoting same (S5); Wikipedia EN (S6); Encyclopedia.com / Complete Dictionary of Scientific Biography Melanchthonian curriculum (S7). primary UNKNOWN→CHRIST @0.7 written_profession (Savior, Son as sacrifice, Moses, Magi; Lutheran/Philippist affiliation). A UNKNOWN→0 @0.7 written_profession, support corroborated (S3+S4): God author of the universe / artificer of the worldly machine; divine majesty not bound by nature's bonds; fabricates the nova as portent. B 3@0.5 inference_from_work (P35)→3 @0.7 written_profession, support corroborated (S3+S4+S5): ordinary heavens without generation/corruption; stated limited exception — nova praeter omnem naturae ordinem; when God wills He halts rivers and turns stars back. Mid UNKNOWN→true @0.7 (P4). Chart-moving YES: not plotted → dark filled when figures next refresh. C/D/E left UNKNOWN. P47 source_quality on all. No fallacy_catalog; figures not refreshed. Draft, not reviewed."}

identity:
  id: brahe-tycho
  display_name: "Tycho Brahe"
  roster:
    canonical_name: "Tycho Brahe"
    rank: 220
    F: 3
    models: [Claude, DeepSeek, Gemini]
    band: "core (3–4)"
    status: "core"
    field: "astronomy"
    field_bucket: "astronomy"
  full_name: {value: "Tycho Brahe", certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S6, locator: "lead"}], how_known: "Britannica and Wikipedia agree."}
  native_name: {value: "Tyge Ottesen Brahe", certainty: 0.7, cites: [{source: S6, locator: "lead"}], how_known: "Wikipedia: Danish form Tyge Ottesen Brahe."}
  aliases:
    - {name: "Tyge Brahe", kind: "birth name"}

basics:
  birth:
    date: {value: "1546-12-14", certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S6, locator: "lead"}], how_known: "Britannica and Wikipedia agree."}
    place: {value: "Knudstrup, Scania", modern_name: "Knudstrup, Scania (now in Sweden)", polity_then: "Kingdom of Denmark", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S6, locator: "Early years"}], how_known: "Britannica: 'Knudstrup, Scania, Denmark'; Wikipedia agrees Scania then Denmark, now Sweden."}
  death:
    date: {value: "1601-10-24", certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S6, locator: "lead"}], how_known: "Britannica and Wikipedia agree."}
    place: {value: "Prague", modern_name: "Prague, Czech Republic", polity_then: "Kingdom of Bohemia (Holy Roman Empire)", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S6, locator: "Death"}], how_known: "Britannica and Wikipedia agree."}
  first_lasting_contribution_year: {value: 1573, certainty: 0.5, cites: [{source: S1, locator: "Youth and education"}, {source: S6, locator: "Nova of 1572"}], how_known: "'his publication of his observations of it in De nova stella in 1573' (S1): first public statement of the observing programme (P30). 0.5: the lasting claim is for the whole body of observations; alternative 1576 (Uraniborg)."}
  era_bucket: {value: "1400 to 1599", certainty: 1.0, cites: [{source: S1, locator: "Youth and education"}], how_known: "1573 (P2); the 1576 alternative is in the same bucket."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Scania (now Sweden; then Denmark): Northern Europe either way (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "Mature career"}], how_known: "Ven (Uraniborg), where the span took place (AA6 rule)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Latin"], certainty: 0.7, cites: [{source: S1, locator: "Youth and education"}, {source: S4, locator: "title page / body"}], how_known: "De nova stella published in Latin (S4); Britannica names the Latin title."}
  occupations: {value: ["astronomer", "instrument maker"], certainty: 0.7, cites: [{source: S1, locator: "Introduction; Mature career"}], how_known: "Britannica."}

contribution:
  primary_domain: astronomy
  fields: {value: ["astronomy"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Body of naked-eye astronomical observations (new star of 1572 beyond the Moon; comet of 1577 beyond the Moon; positions of more than 777 fixed stars; planetary observations used by Kepler)", year: 1573, kind: "body of work", lasting: "'paved the way for future discoveries'; 'remains an outstanding accomplishment of the Renaissance'; with those data 'Kepler laid the groundwork for the work of Sir Isaac Newton' (S1)", certainty: 0.5, cites: [{source: S1, locator: "Introduction; Youth and education; Mature career"}], how_known: "From De nova stella (1573) through Uraniborg (1576–1597) (S1); 0.5 on the start year."}
  evidence_of_impact:
    - {value: "Kepler built on his data", kind: "institutional or technological lineage", certainty: 0.7, cites: [{source: S1, locator: "Mature career"}], how_known: "Britannica."}
  major_works:
    - {value: "De nova stella", year: 1573, kind: "book", certainty: 1.0, cites: [{source: S1, locator: "Youth and education"}, {source: S4, locator: "title"}], how_known: "Britannica and the Latin text itself."}
    - {value: "Geo-heliocentric (Tychonic) system", year: UNKNOWN, kind: "other", certainty: 0.7, cites: [{source: S1, locator: "Mature career"}], how_known: "Britannica; undated; not lasting."}
  honours:
    - {value: "Island of Ven and observatory funding from Frederick II", year: 1576, certainty: 0.7, cites: [{source: S1, locator: "Mature career"}], how_known: "Britannica."}
  definition_fit: {value: "clearly meets", rationale: "Most accurate pre-telescope observations; Kepler's data (S1).", certainty: 0.7, cites: [{source: S1, locator: "Mature career"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "Lutheran", certainty: 0.7, cites: [{source: S6, locator: "Early years; Education"}, {source: S7, locator: "Humanist Influence / Lutheran University of Copenhagen"}], how_known: "Danish Reformation nobility; Copenhagen Lutheran University with Melanchthonian curriculum and Sunday Lutheran catechism (S7); Wikipedia Philippist/Lutheran context."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated beyond confessional setting."}
  parents_and_household:
    - {value: "Father a privy councillor and governor of Helsingborg castle; raised by his childless uncle Jørgen at Tostrup", role: "family", certainty: 0.7, cites: [{source: S1, locator: "Youth and education"}], how_known: "Britannica."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling:
    - {value: "Universities of Copenhagen (law, 1559–62) and Leipzig (1562–65); then Wittenberg, Rostock, Basel, Augsburg", certainty: 0.7, cites: [{source: S1, locator: "Youth and education"}], how_known: "Britannica."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1573–1597", certainty: 0.5, cites: [{source: S1, locator: "Youth and education; Mature career"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Lutheran (Philippist)", certainty: 0.7, cites: [{source: S6, locator: "Life at Uraniborg (Philippists; gnesio-Lutheran bishops)"}, {source: S7, locator: "Humanist Influence"}], how_known: "Wikipedia: known Philippist sympathies under Melanchthon's followers; Encyclopedia.com: Lutheran University of Copenhagen Melanchthonian curriculum and Lutheran catechism."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "De nova stella treats the nova as a divine portent outside natural order and then restricts his own claims to mathematical consideration (S3/S4); no separate science–religion relation statement scored this pass."}
  primary_system:
    value: CHRIST
    basis: written_profession
    certainty: 0.7
    cites: [{source: S3, locator: "McLaughlin English: Moses; God author of the universe; Magi / Savior of the world; Son as sacrifice; Joshua"}, {source: S4, locator: "Deum autorem Vniuersi; Saluator mundj; Gnatus / victima; Iosue"}, {source: S6, locator: "Religion; Philippists"}, {source: S7, locator: "Humanist Influence"}]
    how_known: "Own published Latin of 1573 (S4) with matching English (S3): Moses' creation history; God as author of the universe; Magi and the Savior of the world; the Son made a sacrifice; Joshua. Lutheran/Philippist affiliation in S6–S7. Named alternatives CLASS_THEISM and Hermetic/Paracelsian interests; 0.7."
    rationale: "CHRIST use_when: Christian belief (Scripture, Savior/Christ, church setting) without a more specific philosophical position as the frame. Branch: Danish Lutheran, Philippist. Named alternative CLASS_THEISM rejected: the scored voice is biblical Christian, not Aristotelian-Thomistic or falsafa. Hermetic/Paracelsian interests (S6) are noted as context, not a second scored primary."
  secondary_system: {value: UNKNOWN, how_known: "Paracelsian/Hermetic interests appear in secondary literature (S6) but no dual profession of a second system is scored this pass."}
  candidate_codes_considered:
    - {code: CLASS_THEISM, reason: "Rejected as primary: De nova stella's own voice is biblical Christian (Moses, Savior, Son as sacrifice), not classical metaphysics of a simple God.", cites: [{source: S3, locator: "McLaughlin English (Moses; Savior; Son)"}, {source: S4, locator: "Deum autorem Vniuersi; Saluator mundj"}]}
    - {code: CHRIST, reason: "Chosen: own published Christian language plus Lutheran/Philippist affiliation.", cites: [{source: S3, locator: "McLaughlin English"}, {source: S6, locator: "Philippists"}]}
  lio_axes:
    A_locus:
      value: 0
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S3, locator: "McLaughlin English: 'God, the author of the universe'; 'God, the artificer of the entire worldly machine'; divine majesty 'not bound by any bonds of nature'"}, {source: S4, locator: "Deum autorem Vniuersi; Dei totius Machinae mundanae opificis; Diuina enim maiestas liberrime agit, nec vllis obstricta est Naturae vinculis"}]
      how_known: "Own public words in De nova stella 1573: Latin (S4) cross-checked to McLaughlin English from Dreyer (S3). Named alt 1; certainty 0.7. Independent source ids → corroborated (P48)."
      rationale: "Leans to the interventionist personal-Creator pole: God is 'author of the universe' who finished creation and rested (Moses); the nova is a marvelous portent 'fabricated by God, the artificer of the entire worldly machine'; 'divine majesty acts very freely and is not bound by any bonds of nature but, when it wills, it halts the water of the rivers and makes the stars go backward'; Joshua and the Son as sacrifice are named. God is distinct from the world he made and intervenes. Named alternative 1: opifex / worldly-machine language alone could be read as craftsman without petition (Copernicus precedent); not chosen because the same pages state free divine action against nature's bonds."
      alternatives:
        - {value: 1, note: "Opifex of the worldly machine without reading the free-action / miracle lines as personal intervention.", cites: [{source: S3, locator: "artificer of the entire worldly machine"}, {source: S4, locator: "Machinae mundanae opificis"}]}
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S3, locator: "McLaughlin English: heavens without generation/corruption; portent 'distinct from the natural order'; divine majesty not bound by bonds of nature"}, {source: S4, locator: "nullam fierj alterationem generationis vel corruptionis; praeter omnem naturae ordinem; nec vllis obstricta est Naturae vinculis"}, {source: S5, locator: "pp. quoting Opera Omnia: praeter Naturae ordinis; stops the rivers / stars recede"}, {source: S1, locator: "Mature career"}]
      how_known: "Own public words: De nova stella Latin (S4) + McLaughlin English (S3); Håkansson quotes the same Opera Omnia lines (S5). Working science (systematic celestial measurement) in S1. Named alt 4; certainty 0.7. Independent source ids → corroborated (P48)."
      rationale: "Scored on his account of nature (P6). Leans to law: he affirms the ordinary celestial order — no generation or corruption in the ethereal heavens, stars keeping number, place, light (S3/S4); his life's work is lawful measurement of positions (S1). Stated limited exception: the 1572 star is a marvelous portent 'praeter omnem naturae ordinem' / 'distinct from the natural order', fabricated by God; divine majesty 'is not bound by any bonds of nature' and can halt rivers and turn stars back (Joshua). So 3. Named alternative 4 if the special-creation lines are read as the edge of what mathematics can say rather than an exception inside nature (P35 leftover). Independent source ids → corroborated (P48)."
      alternatives:
        - {value: 4, note: "If 'I cannot affirm anything about its generation' is read as leaving special creation outside his account of nature rather than a stated exception inside it (P35).", cites: [{source: S3, locator: "confess that I cannot affirm anything about its generation"}, {source: S4, locator: "de eius generatione ... me nihil affirmare posse"}]}
    C_ledger: {value: UNKNOWN, how_known: "Nothing on personal reward/punishment read this pass (P19)."}
    D_authority: {value: UNKNOWN, how_known: "Wikipedia notes he cited Scripture against a moving Earth as a secondary objection (S6); De nova stella treats Moses and mathematicians in one discussion of the nova. Not scored as a clean two-domain statement this pass (P19)."}
    E_scope: {value: UNKNOWN, how_known: "Nothing on in-group favour vs one order for all events scored this pass (P7/P19)."}
  mid_basin:
    value: true
    certainty: 0.7
    cites: [{source: S3, locator: "McLaughlin English (author of the universe; praeter / natural order)"}, {source: S4, locator: "Deum autorem Vniuersi; praeter omnem naturae ordinem"}]
    how_known: "P4 test: A_locus = 0 (≤ 1) at 0.7 corroborated and B_cause = 3 (≥ 3) at 0.7 corroborated, B scored on his account of nature (P6). Both ≥ 0.7, so true. Certainty 0.7 because both axes still name an alternative. F = 3 (first-rank not met; mid_basin itself does not require F = 5). Chart-moving: not plotted → dark filled when figures next refresh."
  statements:
    - text: "Consequently, we are left to conclude that this marvelous portent, distinct from the natural order, was fabricated by God, the artificer of the entire worldly machine, from the very beginning and now, at last, exhibited to the world as evening approached. For the divine majesty acts very freely and is not bound by any bonds of nature but, when it wills, it halts the water of the rivers and makes the stars go backward."
      cites: [{source: S3, locator: "McLaughlin English (from Dreyer Opera Omnia text)"}, {source: S4, locator: "Reliquum igitur est, vt statuamus Dei totius Machinae mundanae opificis ... sistit aquam fluuijs et vertit sidera retro"}]
      date: "1573"
      context: "De nova stella: on the generation of the 1572 new star, after rejecting ordinary philosophical and theological explanations."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
    - text: "For through Moses' history of the creation of the world, it was discovered that God, the author of the universe, having finished preparing the details of the heavens and the elements, had rested from all work and had not afterwards created any new species in the world."
      cites: [{source: S3, locator: "McLaughlin English"}, {source: S4, locator: "per Mosis de mundi fabrica historiam ... Deum autorem Vniuersi"}]
      date: "1573"
      context: "De nova stella: why ordinary theological appeals to creation history cannot explain the nova as a new species under the usual order."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
  changes_over_life: []
  coder_notes: "Leads still useful: Thoren, The Lord of Uraniborg (1990); Christianson, On Tycho's Island (2000); Mechanica / Uraniborg inscription not verified this pass (cabinet.ox.ac.uk fetch failed). Wittendorff-style claims of weak personal piety are secondary contest and do not erase the 1573 published Christian language. Hermetic/Paracelsian interests noted in S6 remain secondary context."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Danish noble (Scanian)", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S6, locator: "Early years"}], how_known: "Britannica and Wikipedia."}
  religious_heritage_by_birth: {value: "Lutheran", certainty: 0.7, cites: [{source: S6, locator: "Early years; Education"}, {source: S7, locator: "Lutheran University of Copenhagen; Lutheran catechism"}], how_known: "Post-Reformation Danish setting; Lutheran university and catechism (S7)."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: "Lutheran catechism (Sunday instruction at Copenhagen)", certainty: 0.5, cites: [{source: S7, locator: "Humanist Influence"}], how_known: "Encyclopedia.com: 'No doubt he received instruction in the articles of faith from the Lutheran catechism on Sunday mornings.' Single secondary; 0.5."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1573–1597", certainty: 0.5, cites: [{source: S1, locator: "Youth and education; Mature career"}], how_known: "De nova stella (1573) to leaving Uraniborg (1597), where 'the major portion' of the lifework was done (P29, P30); 0.5 following the item. Alternatives 1576–1597 and 1573–1601 (data left at death)."}
  age_at_first_lasting_contribution: {value: 27, certainty: 0.5, cites: [{source: S1, locator: "Introduction; Youth and education"}], how_known: "1573 − 1546 = 27 (P30 year difference); alternative 30 (1576)."}
  first_evidence_of_lio_type_views: {value: "1573 (De nova stella: God as artificer; nova outside the natural order)", certainty: 0.7, cites: [{source: S3, locator: "McLaughlin English"}, {source: S4, locator: "praeter omnem naturae ordinem; Machinae mundanae opificis"}], how_known: "Published book at the start of the span."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.7, cites: [{source: S3, locator: "1573"}, {source: S1, locator: "Youth and education"}], how_known: "Stated in the first lasting publication (same year as span start)."}
  worldview_during_major_work: {value: "Lutheran Christian natural philosophy: lawful celestial order with stated divine exceptions (nova as portent)", certainty: 0.7, cites: [{source: S3, locator: "McLaughlin English"}, {source: S4, locator: "praeter omnem naturae ordinem"}, {source: S6, locator: "Philippists"}], how_known: "From De nova stella plus affiliation sources."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Observational astronomy; no geometric-form claim scored for Lane B this pass (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "Lane B only: childhood Melanchthonian / Lutheran university setting (S7) is consistent with later published Christian natural philosophy in De nova stella (S3/S4), but Lane B does not decide mid_basin."
  notes: "Do not treat Philippist curriculum as an outcome."

institutions:
  - {value: "Uraniborg observatory, Ven", role: "founder and director", years: "1576–1597", kind: "research institute", certainty: 0.7, cites: [{source: S1, locator: "Mature career"}], how_known: "Britannica."}
  - {value: "Court of Emperor Rudolf II, Prague", role: "imperial patronage", years: "1599–1601", kind: "patron or funder", certainty: 0.7, cites: [{source: S1, locator: "Mature career"}], how_known: "Britannica."}
collaborators:
  - {value: "Johannes Kepler", relation: "student or assistant", note: "pupil and assistant in his final years; inherited the data", certainty: 0.7, cites: [{source: S1, locator: "Mature career"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 220"}], how_known: "Study roster."}
  controversies:
    - {value: "Philippist sympathies vs gnesio-Lutheran bishops; later secondary claims about personal piety", certainty: 0.5, cites: [{source: S6, locator: "Life at Uraniborg"}], how_known: "Wikipedia; does not erase 1573 published Christian language."}
  data_quality_flags:
    - "De nova stella English is an unofficial web translation (McLaughlin 2023) of Dreyer; Latin tekstnet used as cross-check (P47)."
    - "Span start 1573 vs 1576."
    - "Uraniborg / Mechanica inscription not verified this pass."
  open_questions:
    - "Letters and Mechanica / Uraniborg inscription for further A corroboration."
    - "D_authority from Scripture-vs-Earth-motion passages (De mundi aetherei; correspondence with Rothmann)."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Olin Jeuck Eggen"
    citation: "Eggen, Olin Jeuck. 'Tycho Brahe.' Encyclopaedia Britannica (scholars edition). https://kids.britannica.com/scholars/article/Tycho-Brahe/16148"
    url: "https://kids.britannica.com/scholars/article/Tycho-Brahe/16148"
    accessed: 2026-10-19
    reliability_note: "Signed article, scholars edition, read in full."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, timing, institutions, collaborators, worldview]
  - id: S2
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [review]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "Tycho Brahe (trans. Michael P. McLaughlin)"
    year: 1573
    citation: "Brahe, Tycho. De Nova Stella (1573). English translation by Michael P. McLaughlin (2023) from I. L. E. Dreyer, ed., Opera Omnia. https://causascientia.org/science/Tycho/DeNova.pdf"
    url: "https://causascientia.org/science/Tycho/DeNova.pdf"
    accessed: 2026-10-24
    reliability_note: "Unofficial web English of Dreyer's Latin text; key A/B passages cross-checked to tekstnet Latin (S4) this pass (CODING_GUIDE §7)."
    source_quality: "unofficial web copy"
    used_for: [worldview, timing]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "Tycho Brahe"
    year: 1573
    citation: "Brahe, Tycho. De nova stella (1573), Latin text. Tekstnet / DSL digital edition. https://tekstnet.dk/books/brahe-t_de-nova-stella/005/"
    url: "https://tekstnet.dk/books/brahe-t_de-nova-stella/005/"
    accessed: 2026-10-24
    reliability_note: "Scholarly digital Latin edition of the 1573 work; used to verify McLaughlin English."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview, timing, basics]
  - id: S5
    type: secondary
    kind: "journal article"
    author: "Håkan Håkansson"
    year: 2004
    citation: "Håkansson, Håkan. Essay quoting Tycho's De nova stella / Opera Omnia (Dreyer) on the nova as sign of God 'outside the order of nature' (praeter Naturae ordinis). Lund University PDF. https://lucris.lub.lu.se/ws/files/5734223/3807277.pdf"
    url: "https://lucris.lub.lu.se/ws/files/5734223/3807277.pdf"
    accessed: 2026-10-24
    reliability_note: "Scholarly secondary quoting Dreyer Opera Omnia; corroborates B exception language."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview]
  - id: S6
    type: tertiary
    kind: "encyclopedia"
    author: "Wikipedia contributors"
    citation: "Wikipedia. 'Tycho Brahe.' https://en.wikipedia.org/wiki/Tycho_Brahe"
    url: "https://en.wikipedia.org/wiki/Tycho_Brahe"
    accessed: 2026-10-24
    reliability_note: "P50 dual bio with Britannica; used for native name, Philippist affiliation, Scripture-and-geocentrism note — not alone for axis values."
    source_quality: "reference entry"
    used_for: [identity, childhood, heritage, worldview, review]
  - id: S7
    type: secondary
    kind: "encyclopedia"
    author: "Complete Dictionary of Scientific Biography (via Encyclopedia.com)"
    citation: "Complete Dictionary of Scientific Biography. 'Tycho Brahe.' Encyclopedia.com. https://www.encyclopedia.com/people/science-and-technology/astronomy-biographies/tycho-brahe"
    url: "https://www.encyclopedia.com/people/science-and-technology/astronomy-biographies/tycho-brahe"
    accessed: 2026-10-24
    reliability_note: "Dictionary of Scientific Biography entry: Melanchthonian / Philippist curriculum and Lutheran catechism at Copenhagen."
    source_quality: "reference entry"
    used_for: [childhood, heritage, worldview]
---

## Summary

Tycho Brahe (1546–1601), Danish astronomer [S1]. Deepen D1: primary CHRIST @ 0.7; A 0 @ 0.7 corroborated; B 3 @ 0.7 corroborated; mid_basin true @ 0.7. Chart cue: dark filled (figures not refreshed this pass).

## Life and work

Scania; Copenhagen; Leipzig; Ven (Uraniborg); Prague [S1]. Lutheran / Philippist setting [S6, S7].

## Contribution and impact

Naked-eye observations 1573–1597; data used by Kepler [S1].

## Childhood and education

Copenhagen Lutheran University under Melanchthonian influence; Leipzig and other Lutheran universities [S1, S7].

## Adult working worldview

In *De nova stella* (1573) he calls God the author of the universe and artificer of the worldly machine, treats the 1572 star as a portent outside the natural order, and says divine majesty is not bound by nature's bonds [S3, S4]. Ordinary heavens remain without generation and corruption [S3, S4]. Lane A public record only.

## Heritage (context only)

Danish noble; Lutheran by birth and schooling [S6, S7]. Context only — never an outcome.

## Timing

1573–1597, age 27 at first lasting item [S1]. LIO-type views first evidenced in the same 1573 book [S3, S4].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Melanchthonian curriculum is consistent with later published Christian natural philosophy; it does not decide mid_basin.

## Open questions

- Letters; Mechanica / Uraniborg inscription.
- D_authority from Scripture-and-cosmology passages.

## Research log

- 2026-10-20: Read Britannica (Eggen, scholars edition).
- 2026-10-24: Deepen D1 — De nova stella McLaughlin English (S3) + tekstnet Latin (S4); Håkansson (S5); Wikipedia (S6); Encyclopedia.com / DSB (S7). Person-file only commit; drafts/ and reports/ left uncommitted; figures/ untouched.
