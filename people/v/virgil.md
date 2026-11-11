---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to ancient. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #134, F4 rank 137). Checked Eclogues dedicatory/personal asides (S6: Ecl. 1 Tityrus 'deus' = patron/iuvenis, character speech P42; Ecl. 6.1–12 Varus dedicatory craft aside; Silenus cosmogony 6.31ff character, Lucretian echoes still P42). Ancient Vita Suetonius-Donatus (S4 Wilson-Okamura): §35 planned retirement 'ut reliqua vita tantum philosophiae vacaret' — philosophical interest, not school profession; Siro/Epicurus + Academy/Plato preference sits in interpolated grey block (sigma), carefully labeled not scored as own voice; Horsfall-style bio-allegory caveat noted. Non-poetic association: Philodemus On Vices books address Vergil with Varius, Plotius, Quintilius (SEP Philodemus S7) — circle address ≠ first-person EPICUR profession (membership/association ≠ code). Georgics didactic already read; Aeneid unused (P42). primary/A/B/mid stay BELOW_THRESHOLD. Still not plotted. P47 on S1–S7; P50 Wikipedia EN (S5) dual bio; parents Magia Polla / Magius-employee tradition named from Vita/Wikipedia. No fallacy_catalog; no figures/. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z1 audit fixes (blind audit /workspace/genius_study_audit/gs_8813a47_Z1/run1/): statement kind relabelled from 'written profession (public)' to 'other' (poem's narrator; not scored). RQ-Z1-1 ruled (v8's call on the auditor's advice): the Georgics Jupiter lines are poetic myth, so A stays BELOW_THRESHOLD. No score changed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z1, order P32: F 4, rank 137). Basics from Britannica (Robert Deryck Williams, signed). Own voice read in the Georgics (Latin, The Latin Library web copy): the didactic narrator names Jupiter as the 'father' who made farming hard and set the weather signs (I.121–124, I.351–353), and praises the one who knew 'the causes of things' and trampled fear of fate and Acheron (II.490–492) beside the one who knows the country gods (II.493–494). Not a scientist. Span 42–19 BCE at 0.7 (Eclogues to the unfinished Aeneid). primary_system BELOW_THRESHOLD (leads EPICUR, STOIC); A, B BELOW_THRESHOLD with readings named; C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD. Not plotted. Draft, not reviewed."}

identity:
  id: virgil
  display_name: "Virgil"
  roster:
    canonical_name: "Virgil"
    rank: 137
    F: 4
    models: [Claude, DeepSeek, Gemini, Grok]
    band: "core (3–4)"
    status: core
    field: literature
    field_bucket: literature
  full_name: {value: "Publius Vergilius Maro", certainty: 0.7, cites: [{source: S1, locator: "'Also known as'"}], how_known: "Britannica."}
  native_name: {value: "Publius Vergilius Maro", certainty: 0.7, cites: [{source: S1, locator: "'Also known as'"}], how_known: "Latin name, as in Britannica."}
  aliases:
    - {name: "Vergil", kind: other}
    - {name: "Publius Vergilius Maro", kind: other}

basics:
  birth:
    date: {value: "-70-10-15", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "opening ('born October 15, 70 bce')"}, {source: S5, locator: "infobox (15 October 70 BC)"}, {source: S4, locator: "§2 (Ides of October, Pompey and Crassus consuls)"}], how_known: "Britannica; Wikipedia EN agrees (P50); ancient Vita tradition (S4). Day is traditional."}
    place: {value: "Andes, near Mantua", modern_name: "near Mantua, Italy", polity_then: "Cisalpine Gaul (Roman province)", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Political background'"}, {source: S5, locator: "Family and birth"}], how_known: "Britannica; Wikipedia EN agrees (P50). Cisalpine Gaul incorporated into Italy 42 BCE (S1). Exact Andes site contested (Pietole vs Calvisano tradition) — place kept as 'near Mantua'."}
  death:
    date: {value: "-19-09-21", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "opening ('died September 21, 19 bce')"}, {source: S5, locator: "infobox (21 September 19 BC)"}, {source: S4, locator: "§35 (XI Kal. Oct.; Sentius and Lucretius consuls)"}], how_known: "Britannica; Wikipedia EN agrees (P50); Vita (S4)."}
    place: {value: "Brundisium", modern_name: "Brindisi, Italy", polity_then: "Roman Italy", certainty: 0.7, cites: [{source: S1, locator: "opening; final paragraph"}, {source: S5, locator: "Poetic career / death"}, {source: S4, locator: "§35"}], how_known: "Britannica; Wikipedia EN and Vita agree Brundisium (Servius late MSS Taranto noted as minority; not used)."}
  first_lasting_contribution_year: {value: -42, certainty: 0.7, cites: [{source: S1, locator: "'Literary career' ('composed between 42 and 37 bce')"}], how_known: "The Eclogues, his 'earliest certain work', dated as a range 42–37 BCE; the range's start year (P12). The Appendix Vergiliana is excluded: Britannica says 'it is unlikely that many of these are genuine' (P42)."}
  era_bucket: {value: "-500 to 499", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "Every adult year (c. 50–19 BCE) falls in '-500 to 499' (P2)."}
  region_of_birth: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Italy (P3)."}
  region_of_work: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Political background'"}], how_known: "Italy: Rome and Campania; he died on return from a voyage to Greece (S1)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Latin"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
  occupations: {value: ["poet"], certainty: 0.7, cites: [{source: S1, locator: "'Political background' ('His life was devoted entirely to his poetry')"}], how_known: "Britannica."}

contribution:
  era_bucket: ancient
  fields: {value: ["pastoral poetry", "didactic poetry", "epic poetry"], certainty: 0.7, cites: [{source: S1, locator: "'Literary career'"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Eclogues", year: -42, kind: work, lasting: "'gave a new direction to the genre' of pastoral (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Literary career'"}], how_known: "Britannica: composed 42–37 BCE; the start year (P12)."}
    - {value: "Georgics", year: -37, kind: work, lasting: "'a superb plea for the restoration of the traditional agricultural life of Italy' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Literary career'"}], how_known: "Britannica: composed 37–30 BCE."}
    - {value: "Aeneid", year: -30, kind: work, lasting: "his fame 'rests chiefly upon the Aeneid'; Dido 'the only character to be created by a Roman poet that has passed into world literature' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Literary career'"}], how_known: "Britannica: 'from c. 30 bce; unfinished at his death' (19 BCE), so it ends the span (P12 range end, P30 death cap)."}
  evidence_of_impact:
    - {value: "Regarded by the Romans as their greatest poet; Dante makes him his guide in the Divine Comedy; influence on Spenser and Milton", kind: "assessment by a later major figure", certainty: 0.7, cites: [{source: S1, locator: "opening; 'How did Virgil influence the world?' (body paragraph: Ovid to Dante)"}], how_known: "Britannica body ('regarded by the Romans as their greatest poet'); the Dante, Spenser and Milton line is from the summary panel, kept here as context (P26)."}
  major_works:
    - {value: "Eclogues", year: -42, kind: book, certainty: 0.7, cites: [{source: S1, locator: "'Literary career'"}], how_known: "Britannica."}
    - {value: "Georgics", year: -37, kind: book, certainty: 0.7, cites: [{source: S1, locator: "'Literary career'"}], how_known: "Britannica."}
    - {value: "Aeneid", year: -30, kind: book, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "'Regarded by the Romans as their greatest poet, an estimation that subsequent generations have upheld' (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated in Britannica."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Born 'of peasant stock' / humble parents (Britannica); Vita: father variously a potter or employee of a summoner Magius who married Magius's daughter", role: family, certainty: 0.5, cites: [{source: S1, locator: "opening paragraphs"}, {source: S4, locator: "§1"}, {source: S5, locator: "Family and birth"}], how_known: "Britannica peasant stock; Donatus Vita and Wikipedia name Magius / Magia Polla traditions — ancient biographical tradition, partly contested (education suggests more means). Certainty 0.5."}
    - {value: "Mother Magia Polla (named in Phocas and Probus lives; Wikipedia)", role: mother, certainty: 0.5, cites: [{source: S5, locator: "Family and birth (Magia Polla)"}, {source: S4, locator: "§1 (daughter of Magius)"}], how_known: "Later Vitae / Wikipedia; Donatus implies Magius's daughter without naming Polla."}
  household_circumstances: {value: "Provincial household in the Po valley (Cisalpine Gaul); Vita adds woodlands and bees as the father's later substance", certainty: 0.5, cites: [{source: S1, locator: "opening; 'Political background'"}, {source: S4, locator: "§1"}], how_known: "Britannica + Vita tradition."}
  schooling:
    - {value: "Cremona, Milan, then Rome: Greek and Roman authors, rhetoric and philosophy", stage: "grammar or secondary school", run_by: other, years: UNKNOWN, certainty: 0.7, cites: [{source: S1, locator: "opening paragraphs"}], how_known: "Britannica; stage and run_by the coder's reading."}
    - {value: "Taught by the Epicurean Siro", stage: tutor, run_by: private, years: UNKNOWN, certainty: 0.7, cites: [{source: S1, locator: "opening paragraphs"}], how_known: "Britannica ('It is known that one of his teachers was the Epicurean Siro')."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["Latin"], certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading; Greek learned at school (S1)."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "42–19 BCE", certainty: 0.7, cites: [{source: S1, locator: "'Literary career'; final paragraph"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing read in his own voice on the relation, beyond Georgics II.490–494 (see A and B)."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "Leads EPICUR and STOIC — still below 0.5 after deepen. Britannica: Epicurean early poetry giving way to Stoic-akin attitudes (S1) is a scholar's reading of poems, not his profession. Non-poetic association strengthens the EPICUR lead without unlocking a code: Siro teacher (S1); Philodemus On Vices addresses Vergil with Varius, Plotius, Quintilius (S7) — circle address / pupilship ≠ first-person school profession. Donatus Vita §35 planned 'philosophiae' retirement (S4) shows philosophical intent, not a named school; the interpolated Siro+Academy/Plato block (S4 grey) is carefully labeled and not scored. Poems remain mixed and P42-bound: Georgics II.490–494 Lucretian knower of causes beside knower of country gods (S2); Ecl. 1 'deus' is Tityrus on a patron (S6); Ecl. 6 Silenus cosmogony is character song (S6); Aeneid gods/speeches unused (P42). No code reaches 0.5."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: EPICUR, reason: "Lead: Siro (S1); Philodemus circle address (S7); Georgics II.490–492 Lucretian praise (S2). Against: no first-person profession; next Georgics lines praise country gods; association ≠ code."}
    - {code: STOIC, reason: "Lead: later attitudes 'more akin to Stoicism' (S1). Against: Anchises' world-soul (Aeneid VI) is character speech (P42); no own profession."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "Deepen D1 reaffirms BELOW. Georgics didactic (S2): Jupiter as Father who made farming hard and set weather signs — reading 1 in mythic idiom; II.490–492 Lucretian release from fear of Acheron pulls the other way. Eclogues: Ecl. 1.6–10 'deus nobis haec otia fecit' is Tityrus on a patron iuvenis (political-poetic convention), not theological profession (P42, S6); Ecl. 6.31–40 Silenus cosmogony (seeds in the void) is character song with Lucretian echoes, still P42 (S6). Poetic mythic idiom alone too indirect (P19; RQ-Z1-1). No non-poetic own-voice locus in Vita or Philodemus address."}
    B_cause: {value: BELOW_THRESHOLD, how_known: "Not a scientist. Deepen D1: still only poetic statements about nature (P6/P16). Georgics I.351–353 weather signs fixed once (reading 3) mixed with portents and II.490 causes-of-things praise — poem's idiom, no exception claim. Ecl. 6 Silenus cosmogony unused as author belief (P42). No reading reaches 0.5."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read in his own voice on reward and punishment of persons; the Aeneid's underworld (Book VI) is narrative and a character's speech (P42)."}
    D_authority: {value: UNKNOWN, how_known: "Nothing read (P19). Vita §35 philosophy retirement and Philodemus association do not state revelation vs observation (S4, S7)."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read on the world's order beyond the above (P7, P19); the Aeneid's divine mission for Rome is narrative and Jupiter's speech (P42)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A and B both BELOW_THRESHOLD (P19). Still not plotted."}
  statements:
    - text: "pater ipse colendi / haud facilem esse uiam uoluit, primusque per artem / mouit agros, curis acuens mortalia corda"
      cites: [{source: S2, locator: "Georgics I.121–123"}]
      date: "-37"
      context: "Georgics I, the didactic narrator on why farming is hard: Jupiter ended the Golden Age."
      axes: [A_locus]
      kind: "other"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "Poem's narrator; not scored. Georgics composed 37–30 BCE (S1); date is the start year. The Latin Library web copy (P26 web-copy cap 0.7); the Father here is Jupiter. Poem's voice, not a profession of belief (coder's call)."
    - text: "Atque haec ut certis possemus discere signis, / aestusque pluuiasque et agentis frigora uentos, / ipse pater statuit quid menstrua luna moneret"
      cites: [{source: S2, locator: "Georgics I.351–353"}]
      date: "-37"
      context: "Georgics I, on weather signs."
      axes: [A_locus, B_cause]
      kind: "other"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "Poem's narrator; not scored. As above."
    - text: "felix qui potuit rerum cognoscere causas / atque metus omnis et inexorabile fatum / subiecit pedibus strepitumque Acherontis auari: / fortunatus et ille deos qui nouit agrestis"
      cites: [{source: S2, locator: "Georgics II.490–493"}]
      date: "-37"
      context: "Georgics II, praise of country life; generally read as about Lucretius (coder's note, not from a source read)."
      axes: [A_locus, B_cause]
      kind: "other"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "Poem's narrator; not scored. As above."
    - text: "O Meliboee, deus nobis haec otia fecit. / namque erit ille mihi semper deus"
      cites: [{source: S6, locator: "Eclogues 1.6–7"}]
      date: "-42"
      context: "Eclogue 1: Tityrus answers Meliboeus on why he keeps his land and leisure; the 'deus' is the unnamed iuvenis at Rome (lines 42–45), conventionally Octavian."
      axes: [A_locus]
      kind: "other"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Character speech (Tityrus), not author profession (P42). Political-poetic patron-as-god idiom. Not scored. Date = Eclogues span start (P12)."
    - text: "Cum canerem reges et proelia, Cynthius aurem / uellit, et admonuit: 'Pastorem, Tityre, pinguis / pascere oportet ouis, deductum dicere carmen.'"
      cites: [{source: S6, locator: "Eclogues 6.3–5"}]
      date: "-42"
      context: "Eclogue 6 opening dedicatory aside to Varus: the speaker's poetic choice of slender pastoral over epic."
      axes: []
      kind: "other"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "First-person poetic craft aside (Apollo cuffing the ear). Not a LIO/worldview profession. Not scored."
    - text: "Anno aetatis quinquagesimo secundo ... statuit in Graeciam et in Asiam secedere ... ut reliqua vita tantum philosophiae vacaret."
      cites: [{source: S4, locator: "§35 (Wilson-Okamura; Brugnoli–Stok numbering)"}]
      date: "-19"
      context: "Donatus Vita (Suetonian core): Virgil's planned three-year Aeneid revision in Greece/Asia so the rest of life would be free for philosophy; trip cut short by illness and death at Brundisium."
      axes: []
      kind: "reported speech"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Ancient biography, not own words. Shows philosophical intent without naming a school. Not scored as primary_system (association/intent ≠ profession). Bio-allegory caveat on Vita as a whole (Horsfall; S4 note)."
  changes_over_life:
    - {value: "Epicurean attitudes in the early poetry 'gradually give way to attitudes more akin to Stoicism'", certainty: 0.5, cites: [{source: S1, locator: "opening paragraphs"}], how_known: "Britannica's reading of the poems (a scholar's summary), not a dated statement of his. Deepen D1: Philodemus circle address (S7) is association evidence for the early Epicurean milieu, not a dated conversion."}
  coder_notes: "Deepen D1 2026-10-24: Eclogues asides checked (S6) — still P42 / poetic craft; Vita (S4) carefully labeled (interpolation + Horsfall bio-allegory); Philodemus address (S7) strengthens EPICUR lead without unlocking a code. Keep BELOW. Prior calls stand: Georgics mythic idiom; Aeneid unused; Appendix Vergiliana unused (P42); span 42–19 BCE."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Provincial from Cisalpine Gaul, of peasant stock", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Political background'"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "42–19 BCE", certainty: 0.7, cites: [{source: S1, locator: "'Literary career'; final paragraph"}], how_known: "Eclogues (42–37 BCE, start year, P12) to the Aeneid, unfinished at his death in 19 BCE (P30)."}
  age_at_first_lasting_contribution: {value: 28, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "70 − 42 = 28 (BCE years; event year − birth year, P30)."}
  first_evidence_of_lio_type_views: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S2, locator: "Georgics I–II"}], how_known: "Nothing scored at 3 or 4."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S2, locator: "Georgics I–II"}], how_known: "As above."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Only Britannica's Epicurean-to-Stoic reading (S1)."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Not assessed."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Not assessed."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S2, locator: "Georgics II.490–493"}], how_known: "Not assessed."}
  reading: "Not assessed."
  notes: ""

institutions: []
collaborators:
  - {value: "Maecenas", relation: other, note: "patron; dedicatee of the Georgics", certainty: 0.7, cites: [{source: S1, locator: "'Literary career'"}], how_known: "Britannica."}
  - {value: "Augustus", relation: other, note: "patron; countermanded the burning of the Aeneid, by the story Britannica reports", certainty: 0.7, cites: [{source: S1, locator: "final paragraph"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 137"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Latin (Georgics S2, Eclogues S6) read in The Latin Library web copy, not checked against a critical edition (Mynors OCT); no field rests on it above BELOW_THRESHOLD."
    - "Donatus Vita mixes Suetonian core with commentary-preface bio-allegory and later interpolations (S4); philosophy-of-life Siro+Academy block is interpolated (grey in Wilson-Okamura)."
    - "Philodemus Herculaneum address is association/circle evidence, not Virgil's own profession (S7)."
  open_questions:
    - "Optional: full Horsfall Companion chapter + critical OCT for Georgics/Eclogues — unlikely to unlock A/B without non-poetic own-voice."
    - "Optional: direct PHerc editions naming Vergil (beyond SEP summary) — still association, not profession."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Robert Deryck Williams"
    citation: "Williams, Robert Deryck. \"Virgil.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Virgil. Read live 2026-10-19."
    url: "https://www.britannica.com/biography/Virgil"
    accessed: 2026-10-19
    reliability_note: "Signed article by a professor of classics; body cited, question boxes not cited (P26)."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, collaborators]
  - id: S2
    type: primary
    kind: other
    author: "Virgil"
    citation: "Vergil. Georgics, books I, II, IV. Latin text, The Latin Library. https://www.thelatinlibrary.com/vergil/geo1.shtml (and geo2, geo4). Read 2026-10-19."
    url: "https://www.thelatinlibrary.com/vergil/geo1.shtml"
    accessed: 2026-10-19
    reliability_note: "Unofficial web copy of the Latin text (P26 cap 0.7); line numbers as printed there."
    source_quality: "unofficial web copy"
    used_for: [worldview, timing, lane_b]
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
  - id: S4
    type: secondary
    kind: other
    author: "Aelius Donatus (after Suetonius); tr. David Scott Wilson-Okamura"
    citation: "Donatus, Aelius. Life of Virgil. Trans. David Scott Wilson-Okamura. 1996; rev. 2005, 2008, 2014. http://virgil.org/vitae/. Read live 2026-10-24. (Brugnoli–Stok numbering; grey angle-bracket passages = Bodleian sigma interpolations.)"
    url: "http://virgil.org/vitae/"
    accessed: 2026-10-24
    reliability_note: "Ancient vita prefixed to Donatus's commentary; Suetonian core mixed with bio-allegory of the poems (Horsfall 1995 skepticism noted on the translator's page). Interpolations marked grey — Siro+Academy 'philosophy of life' block not treated as core. Used for biography/tradition only; never to score LIO as own voice."
    source_quality: "other"
    used_for: [basics, childhood, worldview, review]
  - id: S5
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia contributors. \"Virgil.\" Wikipedia, The Free Encyclopedia. https://en.wikipedia.org/wiki/Virgil. Read live 2026-10-24."
    url: "https://en.wikipedia.org/wiki/Virgil"
    accessed: 2026-10-24
    reliability_note: "P50 dual bio with Britannica (S1): birth Andes near Mantua 15 Oct 70 BCE and death Brundisium 21 Sep 19 BCE agree. Parents Magia Polla / Magius traditions summarized. Worldview scores do not rest on Wikipedia. Notes Vita bio-allegory and land-confiscation inference problems."
    source_quality: "reference entry"
    used_for: [basics, childhood, heritage, review]
  - id: S6
    type: primary
    kind: other
    author: "Virgil"
    citation: "Vergil. Eclogues 1 and 6. Latin text, The Latin Library. https://www.thelatinlibrary.com/vergil/ec1.shtml ; https://www.thelatinlibrary.com/vergil/ec6.shtml. Read 2026-10-24."
    url: "https://www.thelatinlibrary.com/vergil/ec1.shtml"
    accessed: 2026-10-24
    reliability_note: "Unofficial web copy (P26 cap 0.7). Used for dedicatory/personal asides check; character speech and poetic craft remain P42 / not scored."
    source_quality: "unofficial web copy"
    used_for: [worldview]
  - id: S7
    type: secondary
    kind: encyclopedia
    author: "David Blank (SEP)"
    citation: "Blank, David. \"Philodemus.\" Stanford Encyclopedia of Philosophy (Summer 2025 Edition), ed. Edward N. Zalta and Uri Nodelman. https://plato.stanford.edu/archives/sum2025/entries/philodemus/. Read live 2026-10-24. (§1.4 Naples / On Vices addresses; §2.2.4.4.2 On Flattery / greed / slander books naming Plotius, Varius, Vergil, Quintilius.)"
    url: "https://plato.stanford.edu/archives/sum2025/entries/philodemus/"
    accessed: 2026-10-24
    reliability_note: "Peer-reviewed encyclopedia. Documents Philodemus addressing Vergil in Epicurean ethical treatises — association/circle evidence, not Virgil's own profession of Epicureanism."
    source_quality: "reference entry"
    used_for: [worldview, review]
---

# Virgil

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`. Deepen D1: still BELOW on primary/A/B/mid; not plotted.

## Summary

Virgil (70–19 BCE), Roman poet of the Eclogues, Georgics and Aeneid [S1; S5]. Deepen D1 (queue #134): primary_system BELOW_THRESHOLD (EPICUR/STOIC leads; Philodemus association S7 does not unlock a code); A, B BELOW (Eclogues asides P42; Georgics mythic idiom); mid BELOW. Still not plotted.

## Life and work

Born near Mantua, schooled at Cremona, Milan and Rome; a teacher was the Epicurean Siro [S1].

## Contribution and impact

Eclogues (42–37 BCE), Georgics (37–30 BCE), Aeneid (from c. 30 BCE, unfinished) [S1].

## Childhood and education

Peasant stock; rhetoric and philosophy [S1].

## Adult working worldview

Georgics didactic naming Jupiter and praising knower of causes / country gods [S2] — poetic idiom, not scored. Eclogues: Tityrus's patron-as-god [S6 Ecl. 1] and Varus dedicatory craft aside [S6 Ecl. 6] — P42 / not LIO. Vita plans philosophy retirement [S4 §35]; Philodemus addresses Vergil in On Vices [S7] — association, not profession. Still BELOW [S1].

## Heritage (context only)

Provincial from Cisalpine Gaul [S1].

## Timing

42–19 BCE, from age 28 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Not assessed [S1].

## Open questions

- Optional Horsfall + OCT; direct PHerc editions — unlikely to unlock own-voice A/B.

## Research log

- 2026-10-19: Read Britannica (Williams) and Georgics I, II and IV in The Latin Library's text.
- 2026-10-24 (D1): Donatus Vita (S4); Wikipedia EN dual bio (S5); Eclogues 1 and 6 (S6); SEP Philodemus circle address (S7). Keep BELOW. Chart-moving NO. No fallacy_catalog; no figures/.
