---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA7)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA7, order P32: F 3, rank 207). Sources: SEP 'Parmenides' (John Palmer, read in full) and Britannica 'Eleaticism' (signed by Starkey and Calogero, scholars edition, read in part). Born about 515 BCE, inferred from Plato's Parmenides (S1); 'active during the early to mid-fifth century BCE' (S1). Lasting work: the poem On Nature, 'founder of metaphysics or ontology' (S1); undated, so first-lasting year, span and age UNKNOWN (P39). Era UNKNOWN, candidate -500 to 499 (AA7 audit, v8's call on the auditor's advice): Diogenes Laertius 9.23 (S4) says 'He flourished in the 69th Olympiad' (504–501 BCE), which implies birth about 540 BCE and an adult life across the -500 edge (P39 strict; Pythagoras and Heraclitus precedent). Worldview: the goddess of the proem is the poem's narrator-device; SEP: 'Parmenides himself never in the extant fragments calls What Is divine or otherwise suggests that it is a god'. primary_system UNKNOWN; A UNKNOWN; not a scientist; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}

identity:
  id: parmenides
  display_name: "Parmenides"
  roster:
    canonical_name: "Parmenides"
    rank: 207
    F: 3
    models: [Claude, DeepSeek, Grok]
    band: "core (3–4)"
    status: "core"
    field: "philosophy"
    field_bucket: "philosophy"
  full_name: {value: "Parmenides of Elea", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Writings"}], how_known: "SEP."}
  native_name: {value: UNKNOWN, how_known: "Greek form not printed in the sources read."}
  aliases: []

basics:
  birth:
    date: {value: "-515", certainty: 0.5, cites: [{source: S1, locator: "1. Life and Writings"}, {source: S4, locator: "IX.23"}], how_known: "SEP: 'born about 515 BCE', inferred from the dramatic date of Plato's Parmenides. Competing date: about 540 BCE, implied by Apollodorus's floruit in the 69th Olympiad (504–501 BCE) as reported by Diogenes Laertius 9.23 (S4)."}
    place: {value: "Elea", modern_name: "Velia, Campania, Italy", polity_then: "Elea (Greek colony)", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Writings"}, {source: S2, locator: "Introduction"}], how_known: "SEP; Britannica."}
  death:
    date: {value: UNKNOWN, how_known: "Death date not given."}
    place: {value: UNKNOWN, how_known: "Death place not given."}
  first_lasting_contribution_year: {value: UNKNOWN, how_known: "On Nature is undated; 'active during the early to mid-fifth century BCE' (S1) is a floruit, not a composition range (P39; RQ-Z9-N1)."}
  era_bucket: {value: UNKNOWN, how_known: "P39 strict (AA7 audit): on Plato's chronology (born about 515 BCE, S1) every adult year falls in -500 to 499, but Diogenes Laertius's floruit in the 69th Olympiad, 504–501 BCE (S4), puts his adult life across the -500 edge. Candidate: -500 to 499."}
  region_of_birth: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Writings"}], how_known: "Elea, southern Italy (P3)."}
  region_of_work: {value: "Southern Europe", certainty: 0.7, cites: [{source: S2, locator: "Introduction"}], how_known: "Elea."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Ancient Greek"], certainty: 0.7, cites: [{source: S1, locator: "2. Overview of Parmenides' Poem"}], how_known: "Hexameter poem."}
  occupations: {value: ["philosopher", "poet", "lawgiver"], certainty: 0.5, cites: [{source: S1, locator: "1. Life and Writings"}], how_known: "SEP: Speusippus reportedly said he established Elea's laws."}

contribution:
  fields: {value: ["philosophy", "metaphysics"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "SEP."}
  lasting_original_contributions:
    - {value: "On Nature (Way of Truth; Way of Opinion): the ontology of What Is", year: UNKNOWN, kind: "work", lasting: "SEP: his derivation of the attributes of what must be qualifies him 'to be seen as the founder of metaphysics or ontology as a domain of inquiry distinct from theology'; Britannica: Eleaticism 'one of the principal schools' of pre-Socratic philosophy", certainty: 0.7, cites: [{source: S1, locator: "closing section"}, {source: S2, locator: "Introduction"}], how_known: "SEP; Britannica. Undated."}
  evidence_of_impact:
    - {value: "Plato's dialogue Parmenides; reception by Plato and Aristotle", kind: "assessment by a later major figure", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Writings"}], how_known: "SEP."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Founder of metaphysics or ontology (S1).", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "SEP."}

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
  working_years: {value: UNKNOWN, how_known: "Undated (P39)."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: {value: UNKNOWN, how_known: "No system professed in the fragments as SEP reads them; the goddess of the proem is the poem's device, and What Is is never called divine (S1)."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: HELLEN, reason: "Lead only: the proem's goddess, Justice and the daughters of Helios (S1); literary frame, not a profession."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "SEP: 'Parmenides himself never in the extant fragments calls What Is divine or otherwise suggests that it is a god' (S1); no locus view to score."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30); the Way of Opinion's cosmology is not scored."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, so the P4 test cannot be applied (P19)."}
  statements:
    - text: "Although What Is in Parmenides has its nearest analogue in these divine principles, Parmenides himself never in the extant fragments calls What Is divine or otherwise suggests that it is a god."
      cites: [{source: S1, locator: "closing section"}]
      context: "Palmer's reading of the extant fragments."
      axes: [A_locus]
      kind: "other"
      verified_against: "scholarly edition"
      verified_on: 2026-10-19
      note: "Scholar's statement, recorded because it settles why A is not scored."
  changes_over_life: []
  coder_notes: "Fr. 12's daimōn 'who steers all things' sits in the Way of Opinion; not scored."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: UNKNOWN, how_known: "Undated (P39)."}
  age_at_first_lasting_contribution: {value: UNKNOWN, how_known: "Undated (P39)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "What Is as a well-rounded sphere (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions: []
collaborators:
  - {value: "Zeno of Elea", relation: "student or assistant", note: "younger associate", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Writings"}, {source: S2, locator: "Introduction"}], how_known: "SEP; Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 207"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Era UNKNOWN: 515 vs 540 BCE birth (P39)."
  open_questions:
    - "Poem date (Wheelwright's 470–460 BCE is a lead only)."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "John Palmer"
    citation: "Palmer, John. 'Parmenides.' Stanford Encyclopedia of Philosophy. https://plato.stanford.edu/entries/parmenides/"
    url: "https://plato.stanford.edu/entries/parmenides/"
    accessed: 2026-10-19
    reliability_note: "Signed entry, read in full."
    used_for: [identity, basics, contribution, worldview, collaborators]
  - id: S2
    type: tertiary
    kind: "encyclopedia"
    author: "Lawrence H. Starkey; Guido Calogero"
    citation: "Starkey, Lawrence H., and Guido Calogero. 'Eleaticism.' Encyclopaedia Britannica (scholars edition). https://kids.britannica.com/scholars/article/Eleaticism/108668"
    url: "https://kids.britannica.com/scholars/article/Eleaticism/108668"
    accessed: 2026-10-19
    reliability_note: "Signed article; introduction and Parmenides sections read."
    used_for: [identity, contribution]
  - id: S3
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [review]
  - id: S4
    type: primary
    kind: "other"
    author: "Diogenes Laertius, tr. R.D. Hicks"
    citation: "Diogenes Laertius. Lives of the Eminent Philosophers, Book IX, tr. R.D. Hicks (1925). Wikisource. https://en.wikisource.org/wiki/Lives_of_the_Eminent_Philosophers/Book_IX"
    url: "https://en.wikisource.org/wiki/Lives_of_the_Eminent_Philosophers/Book_IX"
    accessed: 2026-10-19
    reliability_note: "Ancient biography in translation; the Parmenides chapter (IX.21–23) read."
    used_for: [identity, basics]
---

## Summary

Parmenides (born c. 515 BCE), founder of Eleaticism [S1]. Draft: worldview UNKNOWN. Not plotted.

## Life and work

Elea [S1].

## Contribution and impact

On Nature, undated [S1].

## Childhood and education

Unknown.

## Adult working worldview

Never calls What Is divine [S1].

## Heritage (context only)

Not stated.

## Timing

Undated (P39); era UNKNOWN.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Poem date.

## Research log

- 2026-10-19: Read SEP (Palmer); Britannica Eleaticism; D.L. IX.23.
