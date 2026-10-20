---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z6)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z6, order P32: F 3, rank 159). Basics from NobelPrize.org facts (Chemistry 2024). His words on religion seen only as quoted from Sebastian Mallaby's biography The Infinity Machine (2026) in reviews and an interview with Mallaby: 'doing science is, sort of, like reading the mind of God. Understanding the deep mystery of the universe is my religion, kind of'; Mallaby calls him a Spinozan. Second-hand quotations alone (V3), so UNKNOWN with leads. Scientist status not decided: AlphaFold2 is an AI method for a natural system (protein structure); Knuth/Tao precedent says not, the Chemistry Nobel says yes; B UNKNOWN pending a ruling. Span 2020. primary_system UNKNOWN (leads PANT, DEISM); A UNKNOWN; B UNKNOWN; C, D, E UNKNOWN; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}

identity:
  id: hassabis-demis
  display_name: "Demis Hassabis"
  roster:
    canonical_name: "Demis Hassabis"
    rank: 159
    F: 3
    models: [DeepSeek, GPT, Grok]
    band: "core (3–4)"
    status: "provisional"
    field: "computer science"
    field_bucket: "computer science / AI"
  full_name: {value: "Demis Hassabis", certainty: 0.7, cites: [{source: S1, locator: "heading"}], how_known: "NobelPrize.org."}
  native_name: {value: "Demis Hassabis", certainty: 0.7, cites: [{source: S1, locator: "heading"}], how_known: "NobelPrize.org."}
  aliases:
    - {name: "Demis-Hassabis", kind: "roster alias"}

basics:
  birth:
    date: {value: "1976-07-27", certainty: 0.7, cites: [{source: S1, locator: "Born"}], how_known: "NobelPrize.org."}
    place: {value: "London", modern_name: "London, United Kingdom", polity_then: "United Kingdom", certainty: 0.7, cites: [{source: S1, locator: "Born"}], how_known: "NobelPrize.org."}
  death:
    date: {value: UNKNOWN, how_known: "Living per the sources read."}
    place: {value: UNKNOWN, how_known: "Living."}
  first_lasting_contribution_year: {value: 2020, certainty: 0.5, cites: [{source: S1, locator: "Work"}], how_known: "AlphaFold2 (2020), the prize work; earlier AlphaGo (2016) not in the source read, so 0.5."}
  era_bucket: {value: "1950 on", certainty: 1.0, cites: [{source: S1, locator: "Work"}], how_known: "2020 (P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "Born"}], how_known: "UK (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "Affiliation"}], how_known: "Google DeepMind, London."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Inferred."}
  occupations: {value: ["AI researcher", "co-founder and CEO of DeepMind"], certainty: 0.7, cites: [{source: S1, locator: "Affiliation"}], how_known: "NobelPrize.org."}

contribution:
  fields: {value: ["artificial intelligence", "protein structure prediction"], certainty: 0.7, cites: [{source: S1, locator: "Prize motivation"}], how_known: "NobelPrize.org."}
  lasting_original_contributions:
    - {value: "AlphaFold2 (with John Jumper)", year: 2020, kind: method, lasting: "Nobel Prize in Chemistry 2024 'for protein structure prediction'; 'widely used' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Work"}], how_known: "NobelPrize.org."}
  evidence_of_impact:
    - {value: "Nobel Prize in Chemistry 2024 (1/4)", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "Prize share"}], how_known: "NobelPrize.org."}
  major_works: []
  honours:
    - {value: "Nobel Prize in Chemistry", year: 2024, certainty: 0.7, cites: [{source: S1, locator: "heading"}], how_known: "NobelPrize.org."}
  definition_fit: {value: "arguable", rationale: "Provisional in v8; AlphaFold2 is team work (with Jumper) at a firm (S1).", certainty: 0.5, cites: [{source: S1, locator: "Work"}], how_known: "Coder's reading."}

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
  languages_in_childhood: {value: ["English"], certainty: 0.5, cites: [{source: S1, locator: "Born"}], how_known: "Inferred."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "2020", certainty: 0.5, cites: [{source: S1, locator: "Work"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: {value: UNKNOWN, how_known: "His words seen only second-hand (V3): as quoted from Mallaby's The Infinity Machine (2026), 'doing science is, sort of, like reading the mind of God ... my religion, kind of'; Mallaby calls him a Spinozan, with 'some sort of intelligent design behind it, or at least there might be' (Mallaby's paraphrase). Leads PANT (Spinoza) and DEISM (design)."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: PANT, reason: "Lead: Spinozan, per Mallaby."}
    - {code: DEISM, reason: "Lead: design, per Mallaby's paraphrase."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Second-hand only (V3)."}
    B_cause: {value: UNKNOWN, how_known: "Scientist status unruled: AlphaFold2 is an AI method applied to a natural system; Knuth/Tao say not a scientist, the Chemistry Nobel suggests science. Nothing first-hand on nature."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: UNKNOWN, how_known: "A and B are UNKNOWN (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "Read The Infinity Machine itself (or a first-hand interview) for his words; scientist status under P30 #11 is a ruling question (RQ-Z6-1)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "2020", certainty: 0.5, cites: [{source: S1, locator: "Work"}], how_known: "AlphaFold2 (P29, P30); other lasting work not in the source read."}
  age_at_first_lasting_contribution: {value: 44, certainty: 0.5, cites: [{source: S1, locator: "Born; Work"}], how_known: "2020 − 1976 = 44 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Machine learning (S1).", certainty: 0.5, cites: [{source: S1, locator: "Work"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "Google DeepMind", role: "co-founder; CEO", years: UNKNOWN, kind: commercial, certainty: 0.7, cites: [{source: S1, locator: "Affiliation"}], how_known: "NobelPrize.org."}
collaborators:
  - {value: "John Jumper", relation: collaborator, note: "AlphaFold2", certainty: 0.7, cites: [{source: S1, locator: "Work"}], how_known: "NobelPrize.org."}

review:
  roster_status_reason: {value: "Provisional in v8 (F 3).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 159"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Religious views only second-hand (Mallaby, via reviews)."
  open_questions:
    - "The Infinity Machine; first-hand interviews."

sources:
  - id: S1
    type: tertiary
    kind: "institutional page"
    author: "Nobel Prize Outreach"
    citation: "'Demis Hassabis – Facts – 2024.' NobelPrize.org. https://www.nobelprize.org/prizes/chemistry/2024/hassabis/facts/"
    url: "https://www.nobelprize.org/prizes/chemistry/2024/hassabis/facts/"
    accessed: 2026-10-19
    reliability_note: "Official prize facts page."
    used_for: [identity, basics, contribution, timing, lane_b, institutions, collaborators]
  - id: S2
    type: secondary
    kind: "other"
    author: "Andrew Keen and Sebastian Mallaby"
    citation: "Keen, Andrew. 'The Many Faces of AI: Sebastian Mallaby on Demis Hassabis and the Quest to Read God's Mind.' Keen On (2026). https://www.keenon.tv/the-many-faces-of-ai-sebastian-mallaby-on-demis-hassabis-and-the-quest-to-read-gods-mind/"
    url: "https://www.keenon.tv/the-many-faces-of-ai-sebastian-mallaby-on-demis-hassabis-and-the-quest-to-read-gods-mind/"
    accessed: 2026-10-19
    reliability_note: "Interview with his biographer; Hassabis's words second-hand (V3)."
    used_for: [worldview]
  - id: S3
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

Demis Hassabis (b. 1976), AI researcher [S1]. Draft: all worldview fields UNKNOWN (leads PANT, DEISM). Not plotted.

## Life and work

London; DeepMind [S1].

## Contribution and impact

AlphaFold2 [S1].

## Childhood and education

Not read.

## Adult working worldview

Spinozan by his biographer's account; second-hand only [S2].

## Heritage (context only)

Not read.

## Timing

2020, age 44 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- First-hand words.

## Research log

- 2026-10-19: Read NobelPrize.org facts; Mallaby coverage.
