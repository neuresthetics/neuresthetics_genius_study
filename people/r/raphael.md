---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch J)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-15
  change_log:
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch J, order P32: F 5, rank 66). Basics from Britannica (Britannica Editors, unsigned; body through the Perugia years) and the School of Athens date from Britannica's Plato article (Meinwald). No worldview statement read. primary_system UNKNOWN; A, B, C, D, E UNKNOWN; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Audit fixes (fallacy_catalog audit of 81b9098, run 1). mid_basin BELOW_THRESHOLD -> UNKNOWN (P19)."}

identity:
  id: raphael
  display_name: "Raphael"
  roster:
    canonical_name: "Raphael"
    rank: 66
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: art
    field_bucket: arts
  full_name: {value: "Raffaello Sanzio", certainty: 0.7, cites: [{source: S1, locator: "header ('Also known as')"}], how_known: "Britannica (also Raffaello Santi)."}
  native_name: {value: UNKNOWN, how_known: "Italian, Latin script."}
  aliases:
    - {name: "Raffaello Santi", kind: other}

basics:
  birth:
    date: {value: "1483-04-06", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica; Julian."}
    place: {value: "Urbino, Duchy of Urbino", modern_name: "Urbino, Italy", polity_then: "Duchy of Urbino", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "1520-04-06", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Rome, Papal States", modern_name: "Rome, Italy", polity_then: "Papal States", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1504, certainty: 0.7, cites: [{source: S1, locator: "'Apprenticeship at Perugia'"}], how_known: "The Marriage of the Virgin (1504), 'Raphael's first major work' (P13)."}
  era_bucket: {value: "1400 to 1599", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "Whole life in the bucket (P2)."}
  region_of_birth: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Italy (P3)."}
  region_of_work: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Urbino, Perugia, Rome."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [Italian], certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading (0.5)."}
  occupations: {value: ["painter", "architect"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
contribution:
  fields: {value: ["painting", "architecture"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "The Marriage of the Virgin", year: 1504, kind: work, lasting: "'first major work' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Apprenticeship at Perugia'"}], how_known: "Britannica."}
    - {value: "School of Athens (Stanza della Segnatura)", year: 1511, kind: work, lasting: "'one of the most significant artworks of the Renaissance' (S1)", certainty: 0.5, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "'Life' ('School of Athens (1508–11)')"}], how_known: "Date from Britannica's Plato article; end year used (0.5)."}
  evidence_of_impact:
    - {value: "School of Athens 'perhaps the most famous of Raphael's paintings'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father Giovanni Santi, painter (d. 1494); mother Magia di Battista Ciarla (d. 1491)", role: parents, certainty: 0.7, cites: [{source: S1, locator: "'Early years at Urbino'"}], how_known: "Britannica."}
  household_circumstances: {value: "Orphaned by 11; father connected with the court of Urbino", certainty: 0.7, cites: [{source: S1, locator: "'Early years at Urbino'"}], how_known: "Britannica."}
  schooling:
    - {value: "First painting instruction from his father", stage: home, run_by: family, certainty: 0.7, cites: [{source: S1, locator: "'Early years at Urbino'"}], how_known: "Britannica."}
    - {value: "Workshop of Pietro Perugino, Perugia", stage: apprenticeship, run_by: private, certainty: 0.5, cites: [{source: S1, locator: "'Apprenticeship at Perugia'"}], how_known: "Arrival date unknown ('several scholars' say 1495); 0.5."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: TODO}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1504–1511", certainty: 0.5, cites: [{source: S1, locator: "'Apprenticeship at Perugia'"}, {source: S2, locator: "'Life'"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: {value: UNKNOWN, how_known: "No statement read; Britannica's 'Neoplatonic ideal of human grandeur' describes his art, not his avowed belief."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered: []
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "No statement read."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist; nothing read (P16)."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read (P7)."}
  mid_basin: {value: UNKNOWN, how_known: "A is UNKNOWN; UNKNOWN takes precedence (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "Coder's call; few writings of his survive in the sources read. Religious commissions are not avowed belief."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Urbinate (central Italian)", certainty: 0.7, cites: [{source: S1, locator: "'Early years at Urbino'"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1504–1511", certainty: 0.5, cites: [{source: S1, locator: "'Apprenticeship at Perugia'"}, {source: S2, locator: "'Life'"}], how_known: "First to last dated listed contribution (P29, P30)."}
  age_at_first_lasting_contribution: {value: 21, certainty: 0.7, cites: [{source: S1, locator: "opening; 'Apprenticeship at Perugia'"}], how_known: "1504 − 1483 = 21 (P30)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None read."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "None read."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Not read."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Not read.", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Not read."}
  circle_present: {value: "unclear", rationale: "No worldview statement read.", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  reading: "No scorable worldview statement."
  notes: ""

institutions:
  - {value: "Pope Julius II (Vatican apartments)", role: painter, kind: "patron or funder", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
collaborators:
  - {value: "Pietro Perugino", relation: teacher, certainty: 0.5, cites: [{source: S1, locator: "'Apprenticeship at Perugia'"}], how_known: "Member of his workshop."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 66"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags: []
  open_questions:
    - "Find any surviving letters or poems by Raphael on religion."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "Britannica Editors. \"Raphael.\" Encyclopaedia Britannica, updated 11 September 2026. https://www.britannica.com/biography/Raphael-Italian-painter-and-architect."
    url: "https://www.britannica.com/biography/Raphael-Italian-painter-and-architect"
    accessed: 2026-10-15
    reliability_note: "Unsigned editors' body; Top Questions not cited."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: secondary
    kind: encyclopedia
    author: "Constance C. Meinwald"
    citation: "Meinwald, Constance C. \"Plato.\" Encyclopaedia Britannica, updated 28 August 2026. https://www.britannica.com/biography/Plato."
    url: "https://www.britannica.com/biography/Plato"
    accessed: 2026-10-15
    reliability_note: "Signed body; dates the School of Athens."
    used_for: [contribution, timing]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Raphael

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Raphael (1483–1520), Italian High Renaissance painter and architect [S1]. Draft: all worldview fields UNKNOWN. Not plotted.

## Life and work

Urbino; Perugino's workshop; Rome [S1].

## Contribution and impact

See front matter [S1].

## Childhood and education

See front matter [S1].

## Adult working worldview

No statement read [S1].

## Heritage (context only)

See front matter [S1].

## Timing

See front matter [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Unclear [S1].

## Open questions

- Find any surviving letters or poems by Raphael on religion.

## Research log

- 2026-10-15: Read Britannica (Editors) body through Perugia, and the Plato article for the School of Athens date.
