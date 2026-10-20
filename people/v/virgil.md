---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
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
    date: {value: "-70-10-15", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "opening ('born October 15, 70 bce')"}], how_known: "Britannica alone (P15); the day is the ancient tradition."}
    place: {value: "Andes, near Mantua", modern_name: "near Mantua, Italy", polity_then: "Cisalpine Gaul (Roman province)", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Political background'"}], how_known: "Britannica; Cisalpine Gaul was incorporated into Italy only in 42 BCE (S1)."}
  death:
    date: {value: "-19-09-21", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "opening ('died September 21, 19 bce')"}], how_known: "Britannica alone."}
    place: {value: "Brundisium", modern_name: "Brindisi, Italy", polity_then: "Roman Italy", certainty: 0.7, cites: [{source: S1, locator: "opening; final paragraph"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: -42, certainty: 0.7, cites: [{source: S1, locator: "'Literary career' ('composed between 42 and 37 bce')"}], how_known: "The Eclogues, his 'earliest certain work', dated as a range 42–37 BCE; the range's start year (P12). The Appendix Vergiliana is excluded: Britannica says 'it is unlikely that many of these are genuine' (P42)."}
  era_bucket: {value: "-500 to 499", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "Every adult year (c. 50–19 BCE) falls in '-500 to 499' (P2)."}
  region_of_birth: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Italy (P3)."}
  region_of_work: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Political background'"}], how_known: "Italy: Rome and Campania; he died on return from a voyage to Greece (S1)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Latin"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
  occupations: {value: ["poet"], certainty: 0.7, cites: [{source: S1, locator: "'Political background' ('His life was devoted entirely to his poetry')"}], how_known: "Britannica."}

contribution:
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
    - {value: "Born 'of peasant stock'", role: family, certainty: 0.7, cites: [{source: S1, locator: "opening paragraphs"}], how_known: "Britannica."}
  household_circumstances: {value: "Peasant family in the Po valley (Cisalpine Gaul)", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Political background'"}], how_known: "Britannica."}
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
  primary_system: {value: BELOW_THRESHOLD, how_known: "Leads EPICUR and STOIC. Britannica (signed, a summary of scholarship): 'the Epicurean philosophy is substantially reflected in his early poetry but gradually gives way to attitudes more akin to Stoicism' (S1). That is a scholar's reading of the poems, not his own profession of a school, and the poems' own voice is mixed: Georgics II.490–492 blesses the one who knew 'the causes of things' and trampled 'all fears and inexorable fate' (the Lucretian ideal), and II.493–494 calls 'fortunate too' the one who knows the country gods (S2). Gods and speeches in the Aeneid are characters' (P42; coder's call, as for Homer). No code reaches 0.5."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: EPICUR, reason: "Teacher Siro; Epicureanism 'substantially reflected in his early poetry' (S1); Georgics II.490–492 (S2). Against: the next lines praise the country gods; a scholar's reading, not his profession."}
    - {code: STOIC, reason: "Later attitudes 'more akin to Stoicism' (S1). Against: Anchises' Stoic-sounding account of the world-soul (Aeneid VI) is a character's speech (P42); no profession of his own."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "Didactic narrator's voice in the Georgics (S2): 'the Father himself willed that the path of tillage should not be easy' and 'put evil venom in black serpents' (I.121–130), and 'the Father himself decreed what the monthly moon should warn' (I.351–353). Reading 1 (Jupiter as a personal maker of the world's order). Against: a poem's mythic idiom, not a profession of belief, and II.490–492 praises the Lucretian release from fear of the gods' underworld. Too indirect to score (P19, coder's call)."}
    B_cause: {value: BELOW_THRESHOLD, how_known: "Not a scientist. Scored on his account of nature (P6), but only through poetic statements: the weather signs were fixed by Jupiter 'so that we might learn by sure signs' (I.351–353), a lawful order set once (reading 3); the same book narrates portents at Caesar's death (I.463 ff., coder's reading, not quoted), and II.490 praises knowing 'the causes of things'. Mixed, and in a poem's idiom: no reading reaches 0.5 (P16, P19)."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read in his own voice on reward and punishment of persons; the Aeneid's underworld (Book VI) is narrative and a character's speech (P42)."}
    D_authority: {value: UNKNOWN, how_known: "Nothing read (P19)."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read on the world's order beyond the above (P7, P19); the Aeneid's divine mission for Rome is narrative and Jupiter's speech (P42)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A and B both BELOW_THRESHOLD (P19)."}
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
  changes_over_life:
    - {value: "Epicurean attitudes in the early poetry 'gradually give way to attitudes more akin to Stoicism'", certainty: 0.5, cites: [{source: S1, locator: "opening paragraphs"}], how_known: "Britannica's reading of the poems (a scholar's summary), not a dated statement of his."}
  coder_notes: "Coder's calls: (1) the Georgics' didactic narrator is read as his own voice, but its mythic idiom keeps A and B BELOW_THRESHOLD, not scored; (2) the Aeneid's gods and speeches (Jupiter I.257 ff., Anchises VI) are characters' and score nothing (P42 by analogy; as for Homer); (3) the Appendix Vergiliana (including the Siro poem) is of doubtful authorship (S1) and not used (P42); (4) span 42–19 BCE: Eclogues start to the unfinished Aeneid at death."

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
    - "Latin read in The Latin Library's web copy, not checked against a critical edition (Mynors OCT); no field rests on it above BELOW_THRESHOLD."
  open_questions:
    - "Read a scholarly study of Virgil's religion and philosophy (e.g. on Epicureanism and Siro) and check the Georgics against the Oxford text."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Robert Deryck Williams"
    citation: "Williams, Robert Deryck. \"Virgil.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Virgil. Read live 2026-10-19."
    url: "https://www.britannica.com/biography/Virgil"
    accessed: 2026-10-19
    reliability_note: "Signed article by a professor of classics; body cited, question boxes not cited (P26)."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, collaborators]
  - id: S2
    type: primary
    kind: other
    author: "Virgil"
    citation: "Vergil. Georgics, books I, II, IV. Latin text, The Latin Library. https://www.thelatinlibrary.com/vergil/geo1.shtml (and geo2, geo4). Read 2026-10-19."
    url: "https://www.thelatinlibrary.com/vergil/geo1.shtml"
    accessed: 2026-10-19
    reliability_note: "Unofficial web copy of the Latin text (P26 cap 0.7); line numbers as printed there."
    used_for: [worldview, timing, lane_b]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Virgil

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Virgil (70–19 BCE), Roman poet of the Eclogues, Georgics and Aeneid [S1]. Draft: primary_system BELOW_THRESHOLD (leads EPICUR, STOIC); A, B BELOW_THRESHOLD; C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD. Not plotted.

## Life and work

Born near Mantua, schooled at Cremona, Milan and Rome; a teacher was the Epicurean Siro [S1].

## Contribution and impact

Eclogues (42–37 BCE), Georgics (37–30 BCE), Aeneid (from c. 30 BCE, unfinished) [S1].

## Childhood and education

Peasant stock; rhetoric and philosophy [S1].

## Adult working worldview

The Georgics name Jupiter as the father who made farming hard and set the weather signs, and praise both the knower of causes and the knower of the country gods [S2, I.121–123, I.351–353, II.490–493]. Britannica reads an Epicurean early phase giving way to Stoic attitudes [S1].

## Heritage (context only)

Provincial from Cisalpine Gaul [S1].

## Timing

42–19 BCE, from age 28 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Not assessed [S1].

## Open questions

- A scholarly study of his religion; the Georgics in a critical edition.

## Research log

- 2026-10-19: Read Britannica (Williams) and Georgics I, II and IV in The Latin Library's text.
