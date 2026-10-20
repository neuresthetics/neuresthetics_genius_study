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
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA7, order P32: F 3, rank 205). Source: Britannica, signed by René Ostberg and Kathleen Kuiper (scholars edition, read in full). Lasting work: Frankenstein; or, The Modern Prometheus (January 1818), 'a seminal work of Romanticism and a Gothic horror classic that is also considered to be one of the first science-fiction novels'; its 'subsequent influence on literature and popular culture cannot be overstated' (S1). Span 1818, age 20. Worldview: no own words on belief read; daughter of the radical philosopher William Godwin and Mary Wollstonecraft (S1); her husband was expelled from Oxford over a pamphlet 'endorsing atheism' (S1), a fact about him, not her. primary_system UNKNOWN; A UNKNOWN; not a scientist; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}

identity:
  id: shelley-mary
  display_name: "Mary Shelley"
  roster:
    canonical_name: "Mary Shelley"
    rank: 205
    F: 3
    models: [Gemini, GPT, Grok]
    band: "core (3–4)"
    status: "core"
    field: "literature"
    field_bucket: "literature"
  full_name: {value: "Mary Wollstonecraft Shelley", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica; née Mary Wollstonecraft Godwin."}
  native_name: {value: "Mary Wollstonecraft Shelley", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  aliases:
    - {name: "Mary-Shelley", kind: "roster alias"}
    - {name: "Shelley-Mary", kind: "roster alias"}
    - {name: "Mary Wollstonecraft Godwin", kind: "birth name"}

basics:
  birth:
    date: {value: "1797-08-30", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
    place: {value: "London", modern_name: "London, United Kingdom", polity_then: "Kingdom of Great Britain", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  death:
    date: {value: "1851-02-01", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
    place: {value: "London", modern_name: "London, United Kingdom", polity_then: "United Kingdom", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1818, certainty: 0.7, cites: [{source: S1, locator: "Publishing Frankenstein"}], how_known: "Frankenstein published January 1818 (S1); publication (P30)."}
  era_bucket: {value: "1750 to 1849", certainty: 1.0, cites: [{source: S1, locator: "Publishing Frankenstein"}], how_known: "1818 (P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "United Kingdom (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.5, cites: [{source: S1, locator: "The 'haunted summer' of 1816; Publishing Frankenstein"}], how_known: "Begun at Cologny near Geneva (1816), finished and published in England (1817–18), so the span's place is England; alternative Western Europe (Switzerland)."}
  sex_as_recorded: {value: "female", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "English novels."}
  occupations: {value: ["novelist", "editor", "travel writer"], certainty: 0.7, cites: [{source: S1, locator: "Introduction; Later life and other works"}], how_known: "Britannica."}

contribution:
  fields: {value: ["literature"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Frankenstein; or, The Modern Prometheus", year: 1818, kind: "work", lasting: "'a seminal work of Romanticism and a Gothic horror classic that is also considered to be one of the first science-fiction novels'; 'Frankenstein's subsequent influence on literature and popular culture cannot be overstated' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Introduction; Death and legacy"}], how_known: "Britannica."}
  evidence_of_impact:
    - {value: "Influence of Frankenstein on literature, film and popular culture", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "Death and legacy"}], how_known: "Britannica."}
  major_works:
    - {value: "History of a Six Weeks' Tour (with Percy Shelley)", year: 1817, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "The 'haunted summer' of 1816"}], how_known: "Britannica."}
    - {value: "The Last Man", year: 1826, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "Later life and other works"}], how_known: "Britannica: 'often ranked as her best work'."}
    - {value: "Percy Bysshe Shelley, Poetical Works (editor)", year: 1839, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "Later life and other works"}], how_known: "Britannica."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Author of a seminal Romantic novel and early science fiction (S1).", certainty: 0.7, cites: [{source: S1, locator: "Death and legacy"}], how_known: "Britannica."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Father William Godwin, radical philosopher; mother Mary Wollstonecraft, feminist writer, who died 11 days after her birth; stepmother Mary Jane Clairmont from 1801", role: "family", certainty: 0.7, cites: [{source: S1, locator: "Early life and intellectual upbringing"}], how_known: "Britannica."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling:
    - {value: "No formal education; raised among her father's intellectual visitors; two years in Dundee, Scotland (1812–14)", certainty: 0.7, cites: [{source: S1, locator: "Early life and intellectual upbringing"}], how_known: "Britannica."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1818", certainty: 0.7, cites: [{source: S1, locator: "Publishing Frankenstein"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: {value: UNKNOWN, how_known: "No own words on belief read. Her parents' radicalism and her husband's atheist pamphlet (S1) are context, not her profession."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered: []
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing first-hand read (P19)."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30); no statement on nature read."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, so the P4 test cannot be applied (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "Read The Journals of Mary Shelley (Feldman and Scott-Kilvert, 1987) or Selected Letters (Bennett, 1995) for own words."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated in S1."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1818", certainty: 0.7, cites: [{source: S1, locator: "Publishing Frankenstein"}], how_known: "The one listed lasting item (P29, P30)."}
  age_at_first_lasting_contribution: {value: 21, certainty: 0.7, cites: [{source: S1, locator: "Introduction; Publishing Frankenstein"}], how_known: "1818 − 1797 = 21 (P30 year difference); S1 notes she was 20 at publication in January 1818."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Gothic novel (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions: []
collaborators:
  - {value: "Percy Bysshe Shelley", relation: "family", note: "husband; collaborator on History of a Six Weeks' Tour; edited his works", certainty: 0.7, cites: [{source: S1, locator: "Relationship with Percy Bysshe Shelley; Later life and other works"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 205"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Worldview: no source."
  open_questions:
    - "Own words on religion (Journals; Letters)."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "René Ostberg; Kathleen Kuiper"
    citation: "Ostberg, René, and Kathleen Kuiper. 'Mary Wollstonecraft Shelley.' Encyclopaedia Britannica (scholars edition). https://kids.britannica.com/scholars/article/Mary-Wollstonecraft-Shelley/67263"
    url: "https://kids.britannica.com/scholars/article/Mary-Wollstonecraft-Shelley/67263"
    accessed: 2026-10-19
    reliability_note: "Signed article, scholars edition, read in full."
    used_for: [identity, basics, contribution, childhood, timing, collaborators]
  - id: S2
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [review]
---

## Summary

Mary Shelley (1797–1851), novelist [S1]. Draft: worldview UNKNOWN. Not plotted.

## Life and work

London; Geneva; Italy [S1].

## Contribution and impact

Frankenstein (1818) [S1].

## Childhood and education

No formal education [S1].

## Adult working worldview

None read.

## Heritage (context only)

Not stated.

## Timing

1818, age 21 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Own words.

## Research log

- 2026-10-19: Read Britannica (Ostberg and Kuiper, scholars edition).
