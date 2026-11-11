---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z7; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to medieval. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #154, F3 rank 162). Opened Ordinatio I (Peter Simpson EN, aristotelophile PDF) d.2 nn.74–88 (first efficient cause has intelligence and will; natural agents act of necessity; contingent causation from first will) and d.42 nn.8–9 (theological omnipotence — immediate without co-agent — believed, not demonstrated); Wolter Nelson 1962 Philosophical Writings §V experimental knowledge (IA OCR). Lifted CLASS_THEISM, A 1, B 3 from scholarly_reconstruction @0.5 to written_profession @0.7 (alts kept: A alt 0; B alt 2). P48 support corroborated on A and B. mid_basin BELOW_THRESHOLD → true @0.7. Chart-moving YES (faded→dark; hollow→filled). P47 source_quality; P50 Wikipedia dual bio (birth-year range differs from SEP). No fallacy_catalog; no figures/. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z7 audit fix: change_log cap label corrected; scholarly_reconstruction caps at 0.5, not 0.7. No value changed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z7, order P32: F 3, rank 162). Source: SEP 'John Duns Scotus' (Thomas Williams, rev. 2025), a scholar's account of his works with Ordinatio and Lectura locators. No Latin or translated primary text read, so the worldview rests on scholarly_reconstruction (0.5 cap). Franciscan friar, priest (1291) and master of theology at Paris. primary_system CLASS_THEISM (0.5, scholarly_reconstruction cap). A 1 (0.5, alt 0): first agent with intellect and will, infinite being; univocity makes the God–creature difference 'one of degree'. B 3 (0.5, alt 2): certainty about 'causal judgments derived from experience', but God 'can cause immediately ... whatever he ordinarily causes through a secondary cause' and all contingent truth hangs on his free will. C, D, E UNKNOWN. mid_basin BELOW_THRESHOLD (A and B at 0.5). Plotted (A 1, B 3). Span 1298–1308. Draft, not reviewed."}

identity:
  id: scotus-duns
  display_name: "John Duns Scotus"
  roster:
    canonical_name: "Duns Scotus"
    rank: 162
    F: 3
    models: [Claude, DeepSeek, Grok]
    band: "core (3–4)"
    status: "core"
    field: "philosophy"
    field_bucket: "philosophy"
  full_name: {value: "John Duns Scotus", certainty: 0.7, cites: [{source: S1, locator: "§1.1"}, {source: S5, locator: "lead"}], how_known: "SEP and Wikipedia agree."}
  native_name: {value: "Iohannes Duns Scotus", certainty: 0.5, cites: [{source: S1, locator: "§1.1"}], how_known: "SEP gives the family name Duns; the Latin form is the coder's."}
  aliases:
    - {name: "John Duns Scotus", kind: "roster alias"}
    - {name: "the Subtle Doctor", kind: "title or honorific"}
    - {name: "Doctor Subtilis", kind: "title or honorific"}

basics:
  birth:
    date: {value: "1263", certainty: 0.5, cites: [{source: S1, locator: "§1.1"}, {source: S5, locator: "Life"}], how_known: "SEP: 'a birth year of 1263 or 1264 is therefore likely' (Dumont 2023). Wikipedia dual bio (P50) gives c. 1265/66 from the 1291 ordination age rule. Ranges disagree; keep SEP figure at 0.5."}
    place: {value: "Duns", modern_name: "Duns, Scotland, United Kingdom", polity_then: "Kingdom of Scotland", certainty: 0.7, cites: [{source: S1, locator: "§1.1"}, {source: S5, locator: "Life"}], how_known: "SEP and Wikipedia agree on Duns, Berwickshire."}
  death:
    date: {value: "1308-11-08", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "§1.1"}, {source: S5, locator: "Life"}], how_known: "SEP and Wikipedia: traditional date 8 November 1308, Cologne."}
    place: {value: "Cologne", modern_name: "Cologne, Germany", polity_then: "Holy Roman Empire", certainty: 0.7, cites: [{source: S1, locator: "§1.1"}, {source: S5, locator: "Life"}], how_known: "SEP and Wikipedia."}
  first_lasting_contribution_year: {value: 1298, certainty: 0.7, cites: [{source: S1, locator: "§1.1; §2.2"}], how_known: "Lectura (Oxford lectures 1298–99), with his proof of God (Lectura 1 d. 2 q. 1), 'one of the most outstanding contributions ever made to natural theology'."}
  era_bucket: {value: "500 to 1399", certainty: 1.0, cites: [{source: S1, locator: "§1.1"}], how_known: "1298 (P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "§1.1"}], how_known: "Scotland, UK (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.5, cites: [{source: S1, locator: "§1.1"}], how_known: "Oxford 1298–1302 and 1303–04; Paris 1302–03 and 1304–07 (Western Europe). Coder's call on a near-even split, 0.5."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Latin"], certainty: 0.7, cites: [{source: S1, locator: "Bibliography"}, {source: S3, locator: "title page"}], how_known: "Latin works; English translations used for deepen."}
  occupations: {value: ["Franciscan friar", "priest", "master of theology"], certainty: 0.7, cites: [{source: S1, locator: "§1.1"}, {source: S5, locator: "lead"}], how_known: "SEP and Wikipedia."}

contribution:
  era_bucket: medieval
  fields: {value: ["philosophy", "theology", "metaphysics"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}
  lasting_original_contributions:
    - {value: "Proof of the existence of God (triple primacy)", year: 1298, kind: "concept or term", lasting: "'one of the most outstanding contributions ever made to natural theology' (S1)", certainty: 0.7, cites: [{source: S1, locator: "§2.2"}, {source: S3, locator: "Ordinatio I d.2"}], how_known: "SEP; first version in the Lectura, 1298–99; Ordinatio I d.2 primary-checked this pass."}
    - {value: "Univocity of being; haecceity; formal distinction (Ordinatio)", year: 1308, kind: "body of work", lasting: "'left a mark' on religious language, universals, freedom (S1)", certainty: 0.5, cites: [{source: S1, locator: "opening; §1.2; §3.3"}], how_known: "SEP; the Ordinatio was revised until his death, so the span end is 0.5."}
  evidence_of_impact:
    - {value: "One of the most important and influential philosopher-theologians of the High Middle Ages", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "lead"}], how_known: "SEP and Wikipedia."}
  major_works:
    - {value: "Ordinatio", year: 1308, kind: "book", certainty: 0.5, cites: [{source: S1, locator: "§1.2"}, {source: S3, locator: "title"}], how_known: "SEP: begun by June 1300, unfinished at death; Book I translation read this pass."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Among the most influential medieval philosophers (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household: []
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling: []
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1298–1308", certainty: 0.5, cites: [{source: S1, locator: "§1.1; §1.2"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Franciscan (Order of Friars Minor); Roman Catholic priest", years: "–1308", role: "friar; priest (ordained 1291); master of theology", certainty: 0.7, cites: [{source: S1, locator: "§1.1"}, {source: S5, locator: "Life"}], how_known: "SEP and Wikipedia."}
  self_described_science_religion_relation:
    value: "Natural reason can prove a first efficient cause with intellect and will, and much about God, but some truths (including properly theological omnipotence) are believed rather than demonstrated; revealed doctrine is necessary for the wayfarer."
    certainty: 0.7
    cites: [{source: S3, locator: "Ordinatio I Prologue; I d.42 n.9"}, {source: S1, locator: "§2.2; §3.2"}]
    how_known: "Own teaching in the Ordinatio (translated); paraphrase. Written profession, 0.7."
  primary_system:
    value: CLASS_THEISM
    basis: written_profession
    certainty: 0.7
    cites: [{source: S3, locator: "Ordinatio I d.2 nn.74–88; d.42 nn.8–9"}, {source: S1, locator: "§1.1; §2.2; §2.3"}]
    how_known: "His own Ordinatio (translated teaching work) plus SEP. Written profession ceiling 1.0; held at 0.7 because he is not the namesake founder of the coded tradition (Aquinas is), and CHRIST remains a considered broader label."
    rationale: "Natural theology proving a first efficient cause with intelligence and will, infinite and unique (Ordinatio I d.2), within Catholic theology: CLASS_THEISM, as for Aquinas. Classical Theism label already split historically — keep CLASS_THEISM as coded."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CLASS_THEISM, reason: "Coded. Own-voice proof of infinite first agent with intellect and will; nature ordered through secondary causes with a stated theological exception (S3, S1).", cites: [{source: S3, locator: "Ordinatio I d.2; d.42"}, {source: S1, locator: "§2.2"}]}
    - {code: CHRIST, reason: "Rejected as primary. He was a Franciscan priest whose theology serves the Catholic faith, but CLASS_THEISM is the closer system (as Aquinas); the coding guide reserves CHRIST when neither theism split fits better.", cites: [{source: S1, locator: "§1.1"}]}
    - {code: CLTHEI, reason: "Rejected. Divine will is free and contingent causation hangs on it, but nature's order runs by secondary causes acting from the necessity of nature; proper omnipotence (immediate without co-agent) is believed, not the ordinary course (S3 d.42).", cites: [{source: S3, locator: "Ordinatio I d.2 n.81; d.42 n.9"}]}
  lio_axes:
    A_locus:
      value: 1
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S3, locator: "Ordinatio I d.2 nn.74–88"}, {source: S1, locator: "§2.2; §2.3"}]
      how_known: "Ordinatio I d.2 in Simpson translation (own teaching work) plus SEP. Written profession; certainty 0.7 because the record names a plausible alternative score (CODING_GUIDE §3). P48: corroborated (S3+S1)."
      rationale: "Leans to the transcendent-person pole. 'the first efficient cause has intelligence and will' (Ord. I d.2 n.74); shown 'in a triple way that the first agent has intelligence and will' (n.88). Infinite and one (S1 §2.2). Univocity makes the God–creature difference 'ultimately one of degree' (Cross, quoted in S1), which weakens transcendence less than it strengthens personhood. So 1, as CLASS_THEISM; alternative 0."
      alternatives:
        - {value: 0, note: "Infinite will and intellect, univocally personal — if univocity is read as collapsing transcendence into degree.", cites: [{source: S1, locator: "§2.3"}]}
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S3, locator: "Ordinatio I d.2 nn.76–81; d.42 nn.8–9"}, {source: S4, locator: "§V Experimental Knowledge"}, {source: S1, locator: "§3.2; §4.3; §5.1"}]
      how_known: "Ordinatio I (Simpson) plus Wolter §V on experimental causal certainty, plus SEP. Account of nature (P6). Written profession; certainty 0.7 because the record names a plausible alternative score (CODING_GUIDE §3). P48: corroborated (S3+S4+S1)."
      rationale: "Scored on his account of nature (P6). Leans LIO with a stated, limited exception. Natural agents 'act of necessity' (Ord. I d.2 n.76); 'any other thing acts from the necessity of nature' (n.81); second causes cause as moved by the first (n.80). We know causal regularities from experience: 'Whatever occurs in a great many instances by a cause that is not free, is the natural effect of that cause' (S4 §V). The stated exception is properly theological omnipotence — power 'immediately … without the co-operation of any other agent cause' — which 'is a thing believed about the first efficient cause, and not something demonstrated' (Ord. I d.42 n.9). So 3, as CLASS_THEISM. Alternative 2 if absolute power / strong voluntarism is read as reaching ordinarily into nature (S1 §5.1)."
      alternatives:
        - {value: 2, note: "Strong voluntarism: nature's order wholly contingent on divine will, absolute power read as ordinary.", cites: [{source: S1, locator: "§5.1"}]}
    C_ledger: {value: UNKNOWN, how_known: "Not scored from the sections read (soul's survival known 'only through faith', S1 §3.2)."}
    D_authority: {value: UNKNOWN, how_known: "Prologue on necessity of revealed doctrine read in outline; not scored as a full axis this pass."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin:
    value: true
    certainty: 0.7
    cites: [{source: S3, locator: "Ordinatio I d.2 nn.74–88; d.42 nn.8–9"}, {source: S4, locator: "§V"}, {source: S1, locator: "§2.2; §3.2; §4.3"}]
    how_known: "P4 test as amended by P6: A_locus = 1 at 0.7 and B_cause = 3 at 0.7, B scored on his account of nature. Both at certainty >= 0.7, so true. Certainty 0.7: mid_basin is no surer than the less certain of A and B (CODING_GUIDE §3). F = 3, so first-rank is met."
  statements:
    - text: "first I show that the first efficient cause has intelligence and will such that its intelligence is of infinites distinctly and that its essence is representative of infinites (which essence indeed is its intelligence)"
      cites: [{source: S3, locator: "Ordinatio I d.2 n.74"}]
      context: "Ordinatio I, distinction 2: proof of the infinity of the first being. Teaching work; English of Peter L.P. Simpson."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Translated wording (Simpson). Unofficial web copy of the translation PDF; cannot alone support certainty 1.0 (CODING_GUIDE §7)."
    - text: "every natural agent, precisely considered, would act of necessity"
      cites: [{source: S3, locator: "Ordinatio I d.2 n.76"}]
      context: "Argument that the first being has intelligence and will, from natural agents acting for an end only as dependent on a knower."
      axes: [B_cause, A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
    - text: "there is no principle of contingent operation save the will or something concomitant to will, because any other thing acts from the necessity of nature, and so not contingently"
      cites: [{source: S3, locator: "Ordinatio I d.2 n.81"}]
      context: "Proof that if the first cause causes contingently, it causes willingly."
      axes: [B_cause, A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
    - text: "he is called omnipotent who has power for all effects and for everything possible … and thus immediately – I say – because without the co-operation of any other agent cause; and in this way it seems that omnipotence is a thing believed about the first efficient cause, and not something demonstrated"
      cites: [{source: S3, locator: "Ordinatio I d.42 n.9"}]
      context: "Properly theological sense of omnipotence, distinguished from the weaker mediate/immediate sense demonstrable by natural reason (n.8)."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
    - text: "Whatever occurs in a great many instances by a cause that is not free, is the natural effect of that cause."
      cites: [{source: S4, locator: "Philosophical Writings §V, Experimental Knowledge"}]
      context: "Ordinatio I d.3 q.4 material as in Wolter's selection: rejection of scepticism; certainty of experimental causal judgments."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Wolter's English; Nelson 1962 IA OCR (identifier philosophicalwritings)."
  changes_over_life: []
  coder_notes: "D1 2026-10-24: Ordinatio I d.2 and d.42 (Simpson) and Wolter §V primary-checked. Lectura 2 d.12 and Vatican critical Latin not opened. C/D/E still UNKNOWN."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Scottish", certainty: 0.7, cites: [{source: S1, locator: "§1.1"}, {source: S5, locator: "lead"}], how_known: "SEP and Wikipedia."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated; ordained priest 17 March 1291 (S1, S5) is adult initiation into orders, not childhood baptism."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1298–1308", certainty: 0.5, cites: [{source: S1, locator: "§1.1; §1.2"}], how_known: "Lectura (1298–99) to his death with the Ordinatio unfinished (P29, P30)."}
  age_at_first_lasting_contribution: {value: 35, certainty: 0.5, cites: [{source: S1, locator: "§1.1"}], how_known: "1298 − 1263 = 35 (P30 year difference); birth year disputed (SEP 1263/64 vs Wikipedia 1265/66)."}
  first_evidence_of_lio_type_views: {value: "1298", certainty: 0.7, cites: [{source: S1, locator: "§2.2"}, {source: S3, locator: "Ordinatio I d.2"}], how_known: "Lectura/Ordinatio proof of God with intellect and will and ordered secondary causes."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.7, cites: [{source: S3, locator: "Ordinatio I d.2; d.42"}], how_known: "The scored views are in the major teaching work itself."}
  worldview_during_major_work: {value: "same as adult working worldview", certainty: 0.7, cites: [{source: S3, locator: "Ordinatio I"}], how_known: "Adult working unit is the Ordinatio/Lectura span."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "Metaphysics as a science from self-evident principles by deduction; stepwise proof of God (S1, S3).", certainty: 0.5, cites: [{source: S1, locator: "§2.2; §3.1"}, {source: S3, locator: "Ordinatio I d.2"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data beyond the stepwise natural-theology proof."
  notes: ""

institutions:
  - {value: "University of Paris (Franciscan chair)", role: "master of theology", years: "1305–1307", kind: "university", certainty: 0.7, cites: [{source: S1, locator: "§1.1"}], how_known: "SEP."}
  - {value: "Order of Friars Minor (Franciscans)", role: "friar; priest from 1291", years: "–1308", kind: "religious body", certainty: 0.7, cites: [{source: S1, locator: "§1.1"}, {source: S5, locator: "Life"}], how_known: "SEP and Wikipedia."}
collaborators:
  - {value: "Thomas Aquinas", relation: "rival or critic", note: "Scotus argues against analogy and Aquinas's view of freedom", certainty: 0.7, cites: [{source: S1, locator: "§2.1; §5.2"}], how_known: "SEP."}
  - {value: "Henry of Ghent", relation: "rival or critic", note: "illuminationism", certainty: 0.7, cites: [{source: S1, locator: "§4.3"}, {source: S4, locator: "§V"}], how_known: "SEP; Wolter §V is Scotus against Henry."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 162"}], how_known: "Study roster."}
  controversies:
    - {value: "Birth year: SEP (Dumont) favors 1263 or 1264; Wikipedia gives c. 1265/66 from the 1291 ordination canonical-age rule.", certainty: 0.7, cites: [{source: S1, locator: "§1.1"}, {source: S5, locator: "Life"}], how_known: "P50 dual-bio disagreement."}
  data_quality_flags:
    - "Ordinatio Book I read in Simpson unofficial web PDF and Wolter Nelson OCR selection; Vatican critical Latin and Lectura 2 d.12 not opened this pass."
  open_questions:
    - "Vatican critical Latin for Ord. I d.2 / d.42; Lectura 2 d.12 on secondary causes."
    - "Score C, D, E from Ord. Prologue and later distinctions."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Thomas Williams"
    citation: "Williams, Thomas. 'John Duns Scotus.' Stanford Encyclopedia of Philosophy (rev. 15 Dec 2025). https://plato.stanford.edu/entries/duns-scotus/"
    url: "https://plato.stanford.edu/entries/duns-scotus/"
    accessed: 2026-10-19
    reliability_note: "Peer-reviewed reference entry by a Scotus scholar."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, worldview, heritage, timing, lane_b, institutions, collaborators, review]
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
    author: "John Duns Scotus"
    year: 2016
    citation: "John Duns Scotus. The Ordinatio of Blessed John Duns Scotus. Book One. Translated by Peter L.P. Simpson. PDF at aristotelophile.com (Scotus All Book 1; PDF metadata author 'peter simpson', created 2016-03-25). Pages/sections read: Prologue outline; I d.2 nn.74–88; I d.42 nn.8–13. https://www.aristotelophile.com/Books/Translations/Ordinatio%20I.pdf"
    url: "https://www.aristotelophile.com/Books/Translations/Ordinatio%20I.pdf"
    accessed: 2026-10-24
    reliability_note: "His own teaching work in a scholar's English translation. Dist 3 is not in this PDF (translator notes Van der Bercken forthcoming). Unofficial web copy: under CODING_GUIDE §7 it cannot by itself support certainty 1.0; A/B held at 0.7 with named alternatives and SEP/Wolter corroboration."
    source_quality: "unofficial web copy"
    used_for: [contribution, worldview, timing, lane_b, collaborators]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "John Duns Scotus"
    year: 1962
    citation: "John Duns Scotus. Philosophical Writings: A Selection. Edited and translated by Allan B. Wolter, O.F.M. Edinburgh: Thomas Nelson and Sons, 1962 (repr. 1963). Internet Archive scan, identifier philosophicalwritings. Section read: V. Concerning Human Knowledge — Experimental Knowledge (certitude of causal judgments from experience)."
    url: "https://archive.org/details/philosophicalwritings"
    accessed: 2026-10-24
    reliability_note: "Published scholarly bilingual selection of Ordinatio material. IA OCR used; wording of the experimental-knowledge principle checked in the OCR text."
    source_quality: "archive scan (OCR only)"
    used_for: [worldview, collaborators]
  - id: S5
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia contributors. 'Duns Scotus.' Wikipedia, The Free Encyclopedia. https://en.wikipedia.org/wiki/Duns_Scotus. Read live 2026-10-24."
    url: "https://en.wikipedia.org/wiki/Duns_Scotus"
    accessed: 2026-10-24
    reliability_note: "P50 dual bio with SEP (S1): death Cologne 8 November 1308 and birthplace Duns agree; birth-year range differs (Wiki c. 1265/66 vs SEP 1263/64). Worldview scores do not rest on Wikipedia."
    source_quality: "reference entry"
    used_for: [identity, basics, heritage, institutions, review]
---

## Summary

John Duns Scotus (c. 1263–1308), Franciscan philosopher-theologian [S1]. CLASS_THEISM (0.7, written_profession); A 1 and B 3 at 0.7, corroborated; mid_basin true. Plotted dark filled.

## Life and work

Franciscan friar and priest (ordained 1291); Oxford, Paris, Cologne [S1, S5].

## Contribution and impact

Proof of God (triple primacy); univocity; haecceity; formal distinction [S1, S3].

## Childhood and education

Not read in detail.

## Adult working worldview

Classical theism: first efficient cause with intelligence and will; natural agents act of necessity through secondary causes; properly theological omnipotence (immediate without co-agent) believed, not demonstrated [S3, S4, S1].

## Heritage (context only)

Scottish [S1, S5].

## Timing

1298–1308; LIO-type views in the major teaching work itself [S3].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Stepwise natural-theology proof; geometric form partly present.

## Open questions

- Vatican critical Latin; Lectura 2 d.12.
- Score C, D, E.

## Research log

- 2026-10-19: Read SEP.
- 2026-10-24: Deepen D1 — Ordinatio I (Simpson aristotelophile) d.2 nn.74–88 and d.42 nn.8–9; Wolter Nelson 1962 §V Experimental Knowledge (IA OCR); Wikipedia dual bio. Lifted A/B/primary to written_profession @0.7; mid true; chart-moving YES. No figures/.
