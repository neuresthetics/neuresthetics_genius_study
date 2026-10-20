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
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA7, order P32: F 3, rank 208). Source: Britannica, signed by René Huyghe (scholars edition, read in full). Lasting work: the last Bathers (1900–05), 'groundbreaking'; identified as Bathers (Les Grandes Baigneuses), National Gallery, London, NG6359, which the Gallery says 'was finished in 1905' and calls 'hugely influential on early twentieth-century modern art, particularly Cubism' (S3; the Barnes and Philadelphia versions run to 1906), which clearly inspired Picasso's Les Demoiselles d'Avignon (1907); his approach 'laid the foundation for Picasso and other artists' subsequent explorations with Cubism' (S1). Not exhibited in his life (the 1907 retrospective was posthumous), so dated by the last documented act, completion 1905 (posthumous rule), at 0.5; alternatives 1906 (death) and 1907 (first showing). Span 1905, age 66. 'Most significant precursor of 20th-century formal abstraction' is body-of-work praise, undated, not used to extend the span. Worldview: no own words on belief read. primary_system UNKNOWN; A UNKNOWN; not a scientist; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}

identity:
  id: cezanne-paul
  display_name: "Paul Cézanne"
  roster:
    canonical_name: "Paul Cézanne"
    rank: 208
    F: 3
    models: [Claude, Gemini, GPT]
    band: "core (3–4)"
    status: "core"
    field: "art"
    field_bucket: "arts"
  full_name: {value: "Paul Cézanne", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  native_name: {value: "Paul Cézanne", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  aliases:
    - {name: "Cézanne-Paul", kind: "roster alias"}
    - {name: "Paul-Cezanne", kind: "roster alias"}

basics:
  birth:
    date: {value: "1839-01-19", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
    place: {value: "Aix-en-Provence", modern_name: "Aix-en-Provence, France", polity_then: "France", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  death:
    date: {value: "1906-10-22", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
    place: {value: "Aix-en-Provence", modern_name: "Aix-en-Provence, France", polity_then: "France", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1905, certainty: 0.5, cites: [{source: S1, locator: "Final years; Legacy"}, {source: S3, locator: "Overview"}], how_known: "Bathers NG6359, 'finished in 1905' (S3), not shown in his life; dated by completion (posthumous rule). Alternatives 1906 (death year) and 1907 (Salon d'Automne retrospective)."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "Final years"}], how_known: "1905 and each alternative (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "France (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "Final years"}], how_known: "Aix-en-Provence."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["French"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "French."}
  occupations: {value: ["painter"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}

contribution:
  fields: {value: ["painting"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Bathers (Les Grandes Baigneuses), National Gallery, London, NG6359", year: 1905, kind: "work", lasting: "'Picasso created his seminal Les Demoiselles d'Avignon ... clearly inspired by Cézanne's groundbreaking Bathers of 1900–05'; his approach 'laid the foundation for ... Cubism' (S1)", certainty: 0.5, cites: [{source: S1, locator: "Final years; Legacy"}, {source: S3, locator: "Overview"}], how_known: "Britannica; National Gallery: 'may date from 1898–9 and was finished in 1905'; 'had a lasting impact on Picasso and Matisse' (S3). Dated by completion (posthumous rule), alternatives 1906 and 1907."}
  evidence_of_impact:
    - {value: "Picasso: 'the father of us all'", kind: "assessment by a later major figure", certainty: 0.7, cites: [{source: S1, locator: "Legacy"}], how_known: "Britannica."}
    - {value: "'the most significant precursor of 20th-century formal abstraction in painting'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "Legacy"}], how_known: "Britannica."}
  major_works:
    - {value: "The House of the Suicide", year: 1873, kind: "artwork", certainty: 0.7, cites: [{source: S1, locator: "Impressionist years"}], how_known: "Britannica."}
    - {value: "The Card Players", year: 1892, kind: "artwork", certainty: 0.7, cites: [{source: S1, locator: "Development of his mature style"}], how_known: "Britannica: 1890–92."}
    - {value: "Mont Sainte-Victoire paintings", year: 1902, kind: "artwork", certainty: 0.7, cites: [{source: S1, locator: "Final years"}], how_known: "Britannica: 1898–1902."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Foundation for Cubism (S1).", certainty: 0.7, cites: [{source: S1, locator: "Legacy"}], how_known: "Britannica."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Well-to-do bourgeois family; father a successful banker", role: "family", certainty: 0.7, cites: [{source: S1, locator: "Early life and work"}], how_known: "Britannica."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling:
    - {value: "Collège Bourbon, Aix (classical education); law school, Aix (two years); Académie Suisse, Paris", certainty: 0.7, cites: [{source: S1, locator: "Early life and work"}], how_known: "Britannica."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1905", certainty: 0.5, cites: [{source: S1, locator: "Final years"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: {value: UNKNOWN, how_known: "No own words on belief read."}
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
  coder_notes: "Own words quoted in S1 ('The landscape ... becomes a thinking, living being within me. I become one with my picture') are aesthetic, not doctrinal. Read Rewald (ed.), Letters, and Gasquet's or Vollard's conversations for religion."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated in S1."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1905", certainty: 0.5, cites: [{source: S1, locator: "Final years; Legacy"}], how_known: "The one listed lasting item, dated by completion (posthumous rule); 0.5."}
  age_at_first_lasting_contribution: {value: 66, certainty: 0.5, cites: [{source: S1, locator: "Introduction"}], how_known: "1905 − 1839 = 66 (P30 year difference); alternatives 67 (1906) and 68 (1907)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "'Everything in Nature is modeled after the sphere, the cone, and the cylinder' (S1).", certainty: 0.5, cites: [{source: S1, locator: "Development of his mature style"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions: []
collaborators:
  - {value: "Camille Pissarro", relation: "teacher", note: "taught him Impressionist technique", certainty: 0.7, cites: [{source: S1, locator: "Impressionist years"}], how_known: "Britannica."}
  - {value: "Émile Zola", relation: "other", note: "school friend; friendship ended", certainty: 0.7, cites: [{source: S1, locator: "Early life and work"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 208"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Worldview: no source."
    - "Lasting item posthumous; dated 1905 at 0.5."
  open_questions:
    - "Religious views (Letters; Gasquet)."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "René Huyghe"
    citation: "Huyghe, René. 'Paul Cézanne.' Encyclopaedia Britannica (scholars edition). https://kids.britannica.com/scholars/article/Paul-C%C3%A9zanne/22192"
    url: "https://kids.britannica.com/scholars/article/Paul-C%C3%A9zanne/22192"
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
  - id: S3
    type: secondary
    kind: "institutional page"
    author: "The National Gallery, London"
    citation: "'Paul Cezanne, Bathers (Les Grandes Baigneuses), about 1894–1905.' National Gallery, London, NG6359. https://www.nationalgallery.org.uk/paintings/paul-cezanne-bathers-les-grandes-baigneuses"
    url: "https://www.nationalgallery.org.uk/paintings/paul-cezanne-bathers-les-grandes-baigneuses"
    accessed: 2026-10-19
    reliability_note: "Holder of the painting; collection page read."
    used_for: [basics, contribution, timing]
---

## Summary

Paul Cézanne (1839–1906), painter [S1]. Draft: worldview UNKNOWN. Not plotted.

## Life and work

Aix-en-Provence; Paris [S1].

## Contribution and impact

Bathers 1900–05 [S1].

## Childhood and education

Collège Bourbon [S1].

## Adult working worldview

None read.

## Heritage (context only)

Not stated.

## Timing

1905 (0.5), age 66 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Religious views.

## Research log

- 2026-10-19: Read Britannica (Huyghe, scholars edition).
