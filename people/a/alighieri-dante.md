---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch E)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to literature. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch E, order P32: F 5, rank 20). Basics from Britannica (Quinones). Worldview from Monarchia III.xvi in Prue Shaw's edition and English translation (Dante Online, Società Dantesca Italiana). The Commedia's speakers, including the pilgrim, are characters and are not used. Not a scientist. CHRIST 0.7; A 0 (0.7); B 3 (0.5); D 2 (0.7); mid_basin BELOW_THRESHOLD. Draft, not reviewed."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Audit fix (fallacy_catalog audit of 2332880, run 1): B_cause 3 (0.5) -> BELOW_THRESHOLD (alternative 4); Mon. III.xvi.12-13 is political and God acts through the order of the heavens, so no stated exception. mid_basin stays BELOW_THRESHOLD. Drops off the person chart."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #20, F5 rank 20). P47 source_quality on every source. Dual-sourced birth/death/parents (S1 Britannica prior + S4 Wikipedia EN). A_locus 0 @ 0.7: support single → corroborated (S2 Shaw Dante Online + S5 Aurelia Henry 1904 De Monarchia III.xvi — independent English translations of the same chapter: prince of the universe / God alone elects / ruler of all things spiritual and temporal). B_cause stays BELOW_THRESHOLD (alt 4): re-read Mon. I.xii free will (S2) and Convivio IV.4–5 Lansing (S6) — free will is moral/political freedom under monarchy, not a Descartes-style carve-out from natural law; Convivio special providence of Rome is historical election, not an account of physical nature's miracles; Henry corroborates the III.xvi order-without-stated-exception wording. D_authority 2 @ 0.7: support single → corroborated (S2+S5 two-guides passage). mid_basin stays BELOW_THRESHOLD. Chart: still unplotted (B BELOW). No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: alighieri-dante
  display_name: "Dante Alighieri"
  roster:
    canonical_name: "Dante Alighieri"
    rank: 20
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: literature
    field_bucket: literature
  full_name: {value: "Dante Alighieri", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts ('In full')"}, {source: S4, locator: "infobox / lead (Durante di Alighiero degli Alighieri)"}], how_known: "Britannica + Wikipedia EN."}
  native_name: {value: "Durante di Alighiero degli Alighieri", certainty: 0.5, cites: [{source: S4, locator: "infobox birth_name; note on baptismal name"}], how_known: "Wikipedia EN birth_name; certainty 0.5 (baptismal/formal form; everyday 'Dante' is the usual name)."}
  aliases:
    - {name: "Dante-Alighieri", kind: "roster alias"}
    - {name: "Durante degli Alighieri", kind: "other"}

basics:
  birth:
    date: {value: "1265", approx: true, certainty: 1.0, cites: [{source: S1, locator: "Quick Facts ('c. May 21–June 20, 1265')"}, {source: S4, locator: "infobox (c. May 1265)"}], how_known: "Britannica + Wikipedia EN; day uncertain, year agreed."}
    place: {value: "Florence", modern_name: "Florence, Italy", polity_then: "Republic of Florence", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S4, locator: "infobox; Early life"}], how_known: "Britannica + Wikipedia EN."}
  death:
    date: {value: "1321-09-13", approx: true, calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "Quick Facts ('September 13/14, 1321')"}, {source: S4, locator: "infobox (14 September 1321)"}], how_known: "Britannica 13/14; Wikipedia 14 — real day dispute, so 0.7 not 1.0 (P30)."}
    place: {value: "Ravenna", modern_name: "Ravenna, Italy", polity_then: "Ravenna (da Polenta lordship)", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S4, locator: "infobox; Death and burial"}], how_known: "Britannica + Wikipedia EN."}
  first_lasting_contribution_year: {value: 1293, certainty: 0.5, cites: [{source: S1, locator: "'Who was Dante's muse?' ('La vita nuova (c. 1293)')"}, {source: S4, locator: "Works / Vita Nuova"}], how_known: "Earliest listed lasting contribution; Britannica dates it 'c. 1293', so 0.5 (circa date)."}
  era_bucket: {value: "500 to 1399", certainty: 1.0, cites: [{source: S1, locator: "dates"}, {source: S4, locator: "dates"}], how_known: "Every candidate year (c. 1293, 1308) is in '500 to 1399' (derived-field exception, §3); birth dual-sourced."}
  region_of_birth: {value: "Southern Europe", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S4, locator: "Early life"}], how_known: "Italy (P3)."}
  region_of_work: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "exile; Ravenna"}, {source: S4, locator: "Exile from Florence; Death"}], how_known: "Florence, then Italian exile."}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S1, locator: "text"}, {source: S4, locator: "infobox"}], how_known: "As recorded."}
  languages_of_work: {value: [Italian, Latin], certainty: 1.0, cites: [{source: S1, locator: "opening (vernacular rather than Latin; De monarchia)"}, {source: S4, locator: "Works"}], how_known: "Britannica + Wikipedia EN."}
  occupations: {value: ["poet", "prose writer", "political thinker"], certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "infobox occupations"}], how_known: "Britannica + Wikipedia EN."}

contribution:
  primary_domain: literature
  fields: {value: ["poetry", "literary theory", "moral and political philosophy"], certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "Works"}], how_known: "Britannica + Wikipedia EN."}
  lasting_original_contributions:
    - {value: "La vita nuova", year: "c. 1293", kind: work, lasting: "chronicle of his love for Beatrice; canon of Italian literature", certainty: 0.5, cites: [{source: S1, locator: "'Who was Dante's muse?'"}, {source: S4, locator: "Works / Vita Nuova"}], how_known: "Britannica + Wikipedia EN; circa date."}
    - {value: "La commedia (The Divine Comedy), in the Tuscan vernacular", year: "c. 1308–1321", kind: work, lasting: "'one of the world's most important and influential works of literature'; made Italian a literary language (S1)", certainty: 0.7, cites: [{source: S1, locator: "intro; opening"}, {source: S4, locator: "Works / Divine Comedy"}], how_known: "Britannica + Wikipedia EN; finished shortly before his death."}
  evidence_of_impact:
    - {value: "'considered the greatest Italian poet'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "intro"}], how_known: "Britannica."}
  major_works:
    - {value: "De monarchia", year: "undated", kind: book, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "title / Book III xvi"}], how_known: "Britannica names it; Shaw edition opened; undated in the texts read."}
    - {value: "Convivio", year: "c. 1304–1307", kind: book, certainty: 0.5, cites: [{source: S4, locator: "Works / Convivio"}, {source: S6, locator: "Book IV (Lansing)"}], how_known: "Wikipedia EN + Lansing text opened; dating conventional/circa."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Commedia; founding influence on literary Italian.", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "Legacy"}], how_known: "Britannica + Wikipedia EN."}

childhood:
  family_religion: {value: "Roman Catholic (Florentine Christian household)", certainty: 0.5, cites: [{source: S4, locator: "Early life; Legacy (Catholic reception)"}, {source: S1, locator: "early life"}], how_known: "Heritage inference from Florentine Christian context and later Catholic reception; household creed not stated in the sources read. Certainty 0.5."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father Alighiero di Bellincione (businessman / moneylender); mother Bella (probably Abati family); mother died before he was ten; father remarried Lapa di Chiarissimo Cialuffi; half-siblings Francesco and Tana; lesser nobility in Florence", certainty: 0.7, cites: [{source: S1, locator: "'early life'"}, {source: S4, locator: "Early life (parents; Lapa; half-siblings)"}], how_known: "Britannica + Wikipedia EN."}
  household_circumstances: {value: "Lesser nobility; father in business/moneylending", certainty: 0.7, cites: [{source: S1, locator: "'early life'"}, {source: S4, locator: "Early life"}], how_known: "Britannica + Wikipedia EN."}
  schooling:
    - {value: "Education and poetry with Brunetto Latini among others (dolce stil nuovo circle)", stage: other, certainty: 0.5, cites: [{source: S4, locator: "Education and poetry"}], how_known: "Wikipedia EN; Britannica early-life section did not name Brunetto in the prior read."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "Brunetto Latini (teacher / poetic mentor)", certainty: 0.5, cites: [{source: S4, locator: "Education and poetry"}], how_known: "Wikipedia EN."}
  languages_in_childhood: {value: [Italian], certainty: 0.7, cites: [{source: S4, locator: "Early life (Florence)"}], how_known: "Florentine household."}
  notable_events:
    - {value: "Met Beatrice Portinari", year: 1274, age: 9, certainty: 0.7, cites: [{source: S1, locator: "'early life'"}, {source: S4, locator: "Early life"}], how_known: "Britannica gives age nine; year = 1265 + 9 (P30)."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1293–1321", certainty: 0.5, cites: [{source: S1, locator: "dates"}, {source: S4, locator: "Works dates"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "Two goals and two means: 'we attain the first through the teachings of philosophy [...] whereas we attain the second through spiritual teachings which transcend human reason' (Monarchia III.xvi.8).", certainty: 1.0, cites: [{source: S2, locator: "Mon. III.xvi.8"}, {source: S5, locator: "Book III ch. XVI (Henry: twofold end; philosophy / revelation)"}], how_known: "His published treatise in two independent scholarly English translations (Shaw; Henry)."}
  primary_system:
    value: CHRIST
    basis: written_profession
    certainty: 0.7
    cites: [{source: S2, locator: "Mon. III.xvi.7–10, 18"}, {source: S5, locator: "Book III ch. XVI (Holy Spirit / Jesus Christ / Pontiff)"}]
    rationale: "The Holy Spirit 'through Jesus Christ the son of God, coeternal with him [...] has revealed to us the transcendent truth we cannot do without', and the Pontiff leads mankind 'in conformity with revealed truth': the religion as confessed. CLASS_THEISM is the named alternative (Aristotle cited, God 'one in the citadel of its own simplicity of nature', III.xvi.15), but the chapter's route is revelation, not an a posteriori argument (P22), so 0.7."
    how_known: "Shaw + Henry independent translations; alternative named, so 0.7."
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Chosen: revelation through Jesus Christ; Pontiff as guide to eternal life (Mon. III.xvi)."}
    - {code: CLASS_THEISM, reason: "Alternative: Aristotelian-scholastic frame; God simple (III.xvi.15)."}
    - {code: CLTHEI, reason: "Rejected as primary: God's choice of the emperor works through the preordained disposition of the heavens; no petition/miracle programme scored from Monarchia."}
  lio_axes:
    A_locus:
      value: 0
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S2, locator: "Mon. III.xvi.2, 12–13, 18"}, {source: S5, locator: "Book III ch. XVI (Prince of the universe; God alone elects; ruler of all things spiritual as well as temporal)"}]
      rationale: "God is 'the prince of the universe', who 'alone chooses' the emperor and is 'ruler over all things spiritual and temporal': a transcendent person outside the world. Alternative 1 (the simple God of III.xvi.15), so 0.7."
      how_known: "Two independent scholarly English translations of Monarchia III.xvi (Shaw Dante Online; Henry 1904) agree on the transcendent-ruler wording; alternative named."
    B_cause:
      value: BELOW_THRESHOLD
      cites: [{source: S2, locator: "Mon. III.xvi.12–13; I.xii.1–6"}, {source: S5, locator: "Book III ch. XVI (order of this world follows the order of the heavens; God alone elects)"}, {source: S6, locator: "Convivio IV.4–5 (divine providence and Rome)"}]
      how_known: "Deepen 2026-10-24: III.xvi order passage corroborated by Henry; I.xii and Convivio IV.4–5 opened. Still too weak/indirect for a scored B (P19)."
      note: "Named alternative 4 (lawful order with no stated exception): III.xvi says the world's disposition follows the circling heavens that God 'preordained' to 'bind all things in due order', and 'God alone chooses' the emperor through that order — politics, not a miracle/exception in nature (prior audit; Henry confirms the same wording). I.xii free will is 'free judgment in matters of volition' and the 'greatest gift given by God to human nature' for political/moral freedom under monarchy — not a Descartes-style carve-out from natural law (distinguish P30 free-will B 3). Convivio IV.4–5 special providence of Rome is historical election for the Incarnation, not an account of physical nature's miracles. Keep 3 only if a stated miracle or clear free-will-vs-nature carve-out is found in a non-fiction treatise."
    C_ledger: {value: UNKNOWN, how_known: "Not treated in the prose chapters read; the Commedia's afterlife is a poem's fiction and is not used."}
    D_authority:
      value: 2
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S2, locator: "Mon. III.xvi.8–10"}, {source: S5, locator: "Book III ch. XVI (two guides: Pontiff and Emperor)"}]
      rationale: "Two domains each with its own authority (P27 anchor): philosophy and the Emperor for 'temporal happiness', revelation and the Pontiff for 'eternal life'. Indirect on observation as such, so 0.7."
      how_known: "Shaw + Henry; two-guides passage dual-translated."
    E_scope: {value: UNKNOWN, how_known: "Scored on the world's order (P7); nothing scored beyond the political/heavens disposition already used under B."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus 0 at 0.7, but B_cause is BELOW_THRESHOLD (P4, §6)."}
  statements:
    - text: "Now these two kinds of happiness must be reached by different means, as representing different ends. For we attain the first through the teachings of philosophy, provided that we follow them putting into practice the moral and intellectual virtues; whereas we attain the second through spiritual teachings which transcend human reason, provided that we follow them putting into practice the theological virtues, i.e. faith, hope and charity."
      cites: [{source: S2, locator: "Mon. III.xvi.8"}, {source: S5, locator: "Book III ch. XVI (Henry parallel: teachings of philosophy / revelation)"}]
      date: "1321"
      context: "Final chapter of Monarchia, on the two ends of man. Undated work; death year used as the evidence date (P39 practice). Henry 1904 independently renders the same argument."
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      axes: [D_authority]
      note: "Shaw's translation; Latin 'per phylosophica documenta [...] per documenta spiritualia que humanam rationem transcendunt'. Monarchia's date is disputed; the death year bounds it (P39 practice)."
    - text: "And since the disposition of this world is a result of the disposition inherent in the circling of the heavens, in order that useful teachings concerning freedom and peace can be applied appropriately to times and places, it is necessary for provision for this protector to be made by Him who takes in at a glance the whole disposition of the heavens. For he alone is the one who preordained this disposition, making provision through it to bind all things in due order."
      cites: [{source: S2, locator: "Mon. III.xvi.12"}, {source: S5, locator: "Book III ch. XVI (Henry: order of this world follows the order of the heavens; preordained)"}]
      date: "1321"
      context: "Argument that the emperor depends directly on God. Henry: 'since the order of this world follows the order of the heavens, as they run their course... He who alone has preordained this... bind all things together, each in their own order.'"
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      axes: [B_cause, A_locus]
    - text: "If this is so, then God alone chooses, he alone confirms, since he has none above him."
      cites: [{source: S2, locator: "Mon. III.xvi.13"}, {source: S5, locator: "Book III ch. XVI (Henry: 'God alone elects, God alone confirms')"}]
      date: "1321"
      context: "Same argument. Henry independent wording confirms the transcendent chooser."
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      axes: [A_locus, B_cause]
    - text: "Therefore it must be borne in mind that the first principle of our freedom is free will, which many people talk about but few understand. For they go so far as to say that free will is free judgment in matters of volition. And what they say is true, but they are very far from understanding what the words mean... Now if judgment controls desire completely and is in no way pre-empted by it, it is free... And that is why the lower animals cannot have free will, because their judgments are always pre-empted by desire... When this has been grasped, it can also be seen that this freedom (or this principle of all our freedom) is the greatest gift given by God to human nature — as I have already said in the Paradiso of the Comedy — since by virtue of it we become happy here as men, by virtue of it we become happy elsewhere as gods."
      cites: [{source: S2, locator: "Mon. I.xii.2–6"}]
      date: "1321"
      context: "Monarchia I.xii on free will as the principle of political freedom under monarchy. Cross-ref to Paradiso is Dante's own; the Commedia's speakers are still not used for axes. Opened this deepen for B; not scored as a nature-exception carve-out."
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      axes: [B_cause]
      note: "Supports researching B; does not by itself raise B above BELOW_THRESHOLD (moral/political freedom, not a stated exception to physical lawfulness)."
  changes_over_life: []
  coder_notes: "Deepen 2026-10-24: Commedia still unused for axes (fictional speakers). A and D now dual-translated (Shaw + Henry). B researched via I.xii and Convivio IV.4–5; stays BELOW (alt 4). Britannica live 403 this pass — S1 claims rest on 2026-10-15 read plus Wikipedia dual-source for basics."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Florentine", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "Early life"}], how_known: "Britannica + Wikipedia EN."}
  religious_heritage_by_birth: {value: "Roman Catholic (Florentine Christian)", certainty: 0.5, cites: [{source: S4, locator: "Early life; Legacy"}, {source: S1, locator: "early life"}], how_known: "Heritage inference; baptism record not opened."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1293–1321", certainty: 0.5, cites: [{source: S1, locator: "dates"}, {source: S4, locator: "Works"}], how_known: "Vita nuova (c. 1293) to the Commedia (range end 1321, his death year) (P29, P30)."}
  age_at_first_lasting_contribution: {value: 28, certainty: 0.5, cites: [{source: S1, locator: "dates"}, {source: S4, locator: "birth c. 1265; Vita Nuova c. 1293"}], how_known: "1293 − 1265 = 28 (P30); circa year, so 0.5."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "B is BELOW_THRESHOLD and Monarchia is undated; A 0 and D 2 are LIO-type but the treatise date is disputed (P27/P39)."}
  lio_views_relative_to_major_work: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "Mon. III.xvi"}], how_known: "Monarchia undated."}
  worldview_during_major_work: {value: "CHRIST", certainty: 0.7, cites: [{source: S2, locator: "Mon. III.xvi"}, {source: S5, locator: "Book III ch. XVI"}], how_known: "As coded."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "Monarchia argues by syllogism and reductio ('a reductio ad absurdum', III.xvi.1).", certainty: 0.5, cites: [{source: S2, locator: "Mon. III.xvi.1"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "opening (scholastic learning)"}, {source: S4, locator: "Education and poetry"}], how_known: "Scholastic frame noted; schooling details thin."}
  circle_present: {value: "no", rationale: "God rules from outside the world ('prince of the universe'; 'ruler over all things spiritual and temporal').", certainty: 0.5, cites: [{source: S2, locator: "Mon. III.xvi.18"}, {source: S5, locator: "Book III ch. XVI close"}], how_known: "Coder's reading of Shaw + Henry."}
  reading: "As belief, not finding: scholastic form with a transcendent God."
  notes: "Lane A and Lane B kept separate (P49). No chart cue from Lane B alone."

institutions: []
collaborators:
  - {value: "Brunetto Latini", relation: teacher, certainty: 0.5, cites: [{source: S4, locator: "Education and poetry"}], how_known: "Wikipedia EN."}
  - {value: "Beatrice Portinari", relation: other, note: "muse of Vita Nuova / Commedia; not a collaborator", certainty: 0.7, cites: [{source: S1, locator: "'early life'; muse Q&A"}, {source: S4, locator: "Early life"}], how_known: "Britannica + Wikipedia EN."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 20"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Britannica gives birth as a range of dates and death as 13/14 September; Wikipedia death 14 September — day left approx."
    - "Britannica live fetch 403 this deepen; S1 rests on 2026-10-15 partial read plus Wikipedia dual-source for basics."
    - "Commedia unused for LIO axes (fictional speakers, including the narrator-pilgrim)."
  open_questions:
    - "Date Monarchia more tightly (scholarly debate)."
    - "Open a baptism / parish record if available for religious_heritage certainty."
    - "If a non-fiction treatise states miracles in nature or a clear free-will-vs-celestial-necessitation carve-out, reopen B."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Ricardo J. Quinones"
    citation: "Quinones, Ricardo J. \"Dante.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Dante-Alighieri."
    url: "https://www.britannica.com/biography/Dante-Alighieri"
    accessed: 2026-10-15
    source_quality: "reference entry"
    reliability_note: "Signed article; the intro Q&A blocks are part of the article page and were used only for dates also in the body. Live fetch 403 on 2026-10-24 deepen; prior 2026-10-15 read stands for claims not dual-sourced elsewhere."
    used_for: [identity, basics, contribution, childhood, heritage, timing]
  - id: S2
    type: primary
    kind: "scholarly edition"
    author: "Dante Alighieri; ed. and trans. Prue Shaw"
    citation: "Dante Alighieri. Monarchia. Ed. and trans. Prue Shaw. Società Dantesca Italiana digital edition (2nd ed., 2019), Book I ch. xii; Book III ch. xvi."
    url: "https://www.danteonline.it/monarchia/"
    accessed: 2026-10-24
    source_quality: "scholarly edition or monograph"
    reliability_note: "Critical edition on the official site of the Società Dantesca Italiana. III.xvi re-confirmed 2026-10-24; I.xii opened this deepen for free will / B."
    used_for: [worldview, timing, lane_b, contribution]
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
    type: tertiary
    kind: other
    author: "Wikipedia contributors"
    citation: "Wikipedia. \"Dante Alighieri.\" https://en.wikipedia.org/wiki/Dante_Alighieri (accessed 2026-10-24)."
    url: "https://en.wikipedia.org/wiki/Dante_Alighieri"
    accessed: 2026-10-24
    source_quality: "other"
    reliability_note: "Used for dual-source basics (birth/death/place), parents, Brunetto, Convivio dating pointer; not used alone for worldview axes."
    used_for: [identity, basics, contribution, childhood, heritage, timing, collaborators]
  - id: S5
    type: primary
    kind: "scholarly edition"
    author: "Dante Alighieri; ed. and trans. Aurelia Henry"
    citation: "Dante Alighieri. The De Monarchia of Dante Alighieri. Ed. with translation and notes by Aurelia Henry. Boston and New York: Houghton, Mifflin and Company, 1904. Book III, chapter XVI. Project Gutenberg HTML (ebook 33896); also Online Library of Liberty PDF."
    url: "https://www.gutenberg.org/files/33896/33896-h/33896-h.htm"
    accessed: 2026-10-24
    source_quality: "scholarly edition or monograph"
    reliability_note: "Independent 1904 English translation (not Shaw). Used to corroborate Monarchia III.xvi A/D wording and the heavens-order B passage. Gutenberg HTML opened this pass."
    used_for: [worldview]
  - id: S6
    type: primary
    kind: "scholarly edition"
    author: "Dante Alighieri; trans. Richard Lansing"
    citation: "Dante Alighieri. The Convivio. Trans. Richard Lansing. Book IV, chapters 4–5 (divine providence and Rome), via Digital Dante / Lansing text reprint opened 2026-10-24."
    url: "https://digitaldante.columbia.edu/text/library/the-convivio/"
    accessed: 2026-10-24
    source_quality: "scholarly edition or monograph"
    reliability_note: "Standard modern English translation; Digital Dante chapter pages were thin/JS shells this pass — IV.4–5 wording taken from the Lansing text as reprinted at rapeutation.com/cult.danteconvivio4.htm (unofficial mirror of the same translation). Used only to research B (special providence of Rome); not scored for axes."
    used_for: [worldview, contribution]
---

# Dante Alighieri

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Dante (c. 1265–1321), Florentine poet of *La vita nuova* (c. 1293) and the *Commedia* (c. 1308–21) [S1; S4]. In *Monarchia* he sets two ends, reached by philosophy and by revelation [S2; S5]. Draft deepen: CHRIST 0.7; A 0 at 0.7 **corroborated** (Shaw + Henry); B BELOW_THRESHOLD (alt 4); D 2 at 0.7 corroborated; mid_basin BELOW_THRESHOLD; chart unplotted.

## Life and work

Exiled from Florence in 1302; died at Ravenna [S1; S4].

## Contribution and impact

*Vita nuova*; *Commedia* in the vernacular [S1; S4]. *Monarchia*; *Convivio* [S2; S5; S6].

## Childhood and education

Lesser nobility; parents Alighiero and Bella; met Beatrice at nine [S1; S4]. Brunetto Latini among early mentors [S4].

## Adult working worldview

Two ends, two guides; God as prince of the universe chooses the emperor through the preordained order of the heavens [S2; S5]. Free will is the principle of political freedom (*Mon.* I.xii) [S2]. *Commedia* unused for axes.

## Heritage (context only)

Florentine; Catholic Christian heritage at 0.5 [S1; S4].

## Timing

First lasting contribution c. 1293, at about 28 [S1; S4].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Scholastic form partly; no circle [S2; S5].

## Open questions

- Date *Monarchia*; baptism record; non-fiction miracle / free-will-vs-nature carve-out for B.

## Research log

- 2026-10-15: Read Britannica and *Monarchia* III.xvi (Shaw, Dante Online).
- 2026-10-24: Deepen — re-read Shaw III.xvi; opened Shaw I.xii; Henry 1904 III.xvi (Gutenberg); Convivio IV.4–5 Lansing; Wikipedia EN dual-source. Britannica 403.
