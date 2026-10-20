---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z8)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z8, order P32: F 3, rank 166). Source: MacTutor biography (O'Connor and Robertson, signed). No own words on religion found; MacTutor says his mother taught him religion and 'imparted her own scepticism to her son' (the biographers' words, not his). Not a scientist (pure algebra; Knuth, Tao, Noether-algebra precedents; P30). primary_system UNKNOWN (lead AGNOS from the mother's scepticism); A, B, C, D, E UNKNOWN; mid_basin UNKNOWN. Span 1829–1832, age 18. Not plotted. Draft, not reviewed."}

identity:
  id: galois-evariste
  display_name: "Évariste Galois"
  roster:
    canonical_name: "Évariste Galois"
    rank: 166
    F: 3
    models: [Claude, Gemini, Grok]
    band: "core (3–4)"
    status: "core"
    field: "mathematics"
    field_bucket: "mathematics"
  full_name: {value: "Évariste Galois", certainty: 0.7, cites: [{source: S1, locator: "Quick Info"}], how_known: "MacTutor."}
  native_name: {value: "Évariste Galois", certainty: 0.7, cites: [{source: S1, locator: "Quick Info"}], how_known: "MacTutor."}
  aliases:
    - {name: "Galois-Évariste", kind: "roster alias"}

basics:
  birth:
    date: {value: "1811-10-25", certainty: 0.7, cites: [{source: S1, locator: "Quick Info"}], how_known: "MacTutor."}
    place: {value: "Bourg-la-Reine", modern_name: "Bourg-la-Reine, France", polity_then: "Kingdom of France", certainty: 0.7, cites: [{source: S1, locator: "Quick Info"}], how_known: "MacTutor."}
  death:
    date: {value: "1832-05-31", certainty: 0.7, cites: [{source: S1, locator: "Quick Info"}], how_known: "MacTutor."}
    place: {value: "Paris", modern_name: "Paris, France", polity_then: "Kingdom of France", certainty: 0.7, cites: [{source: S1, locator: "Quick Info; Biography"}], how_known: "Cochin hospital, after a duel."}
  first_lasting_contribution_year: {value: 1829, certainty: 0.5, cites: [{source: S1, locator: "Biography"}], how_known: "Articles on the algebraic solution of equations submitted to the Académie on 25 May and 1 June 1829; those versions are lost, later versions 1830 and 1831, so 0.5."}
  era_bucket: {value: "1750 to 1849", certainty: 1.0, cites: [{source: S1, locator: "Biography"}], how_known: "1829 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "Quick Info"}], how_known: "France (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "Paris."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["French"], certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "French papers."}
  occupations: {value: ["mathematician"], certainty: 0.7, cites: [{source: S1, locator: "Summary"}], how_known: "MacTutor."}

contribution:
  fields: {value: ["algebra", "group theory"], certainty: 0.7, cites: [{source: S1, locator: "Summary"}], how_known: "MacTutor."}
  lasting_original_contributions:
    - {value: "Galois theory: solubility of equations by radicals, early group theory", year: 1829, kind: "theory", lasting: "'The theory that Galois outlined in these papers is now called Galois theory'; Liouville: 'as correct as it is deep' (S1)", certainty: 0.5, cites: [{source: S1, locator: "Biography (Liouville, 1843–46)"}], how_known: "MacTutor; worked on from 1829 to the letter of 29 May 1832 (range 1829–1832; P12 start). Published by Liouville in 1846."}
  evidence_of_impact:
    - {value: "Famous for his development of early group theory", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "Summary"}], how_known: "MacTutor."}
  major_works:
    - {value: "Mémoire sur les conditions de résolubilité des équations par radicaux (third version)", year: 1831, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "Submitted 17 January 1831; rejected by Poisson."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Founder of Galois theory and early group theory (S1).", certainty: 0.7, cites: [{source: S1, locator: "Summary"}], how_known: "MacTutor."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated; parents 'well educated in philosophy, classical literature and religion' (S1)."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household: []
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling:
    - {value: "Lycée Louis-le-Grand", stage: "grammar or secondary school", years: "1823–1829", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "Adelaide Marie Demante, mother, his sole teacher to age 12", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor: taught him Greek, Latin and religion, 'where she imparted her own scepticism to her son'."}
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events:
    - {value: "Father's suicide after a forged-epigram scandal involving the village priest", year: 1829, certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1829–1832", certainty: 0.5, cites: [{source: S1, locator: "Biography"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: {value: UNKNOWN, how_known: "No own words on religion found. Lead AGNOS: his mother 'imparted her own scepticism to her son' (S1, the biographers' words). Ardent republican; anticlerical context (the priest's forgeries) is not a stance."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: AGNOS, reason: "Lead: inherited scepticism (S1), second-hand."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing found (P19)."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (pure algebra; P30, Noether and Tao precedents), and no statement on nature found (P16, P19)."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing found."}
    D_authority: {value: UNKNOWN, how_known: "Nothing found."}
    E_scope: {value: UNKNOWN, how_known: "Nothing found."}
  mid_basin: {value: UNKNOWN, how_known: "A and B are UNKNOWN (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "Dupuy (1896) and the Bourgne–Azra Écrits et mémoires may report deathbed words or letters on religion; not read."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "French", certainty: 0.7, cites: [{source: S1, locator: "Quick Info"}], how_known: "MacTutor."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1829–1832", certainty: 0.5, cites: [{source: S1, locator: "Biography"}], how_known: "Galois theory, first submitted 1829, to the letter and marginal notes of 29 May 1832 (P29, P30; range end)."}
  age_at_first_lasting_contribution: {value: 18, certainty: 0.5, cites: [{source: S1, locator: "Quick Info; Biography"}], how_known: "1829 − 1811 = 18 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "Abstract algebraic proof; studied Legendre's Géométrie (S1).", certainty: 0.5, cites: [{source: S1, locator: "Biography"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "École Normale (préparatoire)", role: "student", years: "1829–1830", kind: "university", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor; expelled 1830."}
collaborators:
  - {value: "Auguste Chevalier", relation: "other", note: "copied and circulated his papers", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
  - {value: "Augustin-Louis Cauchy", relation: "rival or critic", note: "referee of the 1829 paper", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 166"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "No own words on religion found."
  open_questions:
    - "Dupuy 1896; Écrits et mémoires."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "J. J. O'Connor and E. F. Robertson"
    citation: "O'Connor, J. J., and E. F. Robertson. 'Évariste Galois.' MacTutor History of Mathematics, University of St Andrews. https://mathshistory.st-andrews.ac.uk/Biographies/Galois/"
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Galois/"
    accessed: 2026-10-19
    reliability_note: "Signed reference biography with references."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
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

Évariste Galois (1811–1832), mathematician [S1]. Draft: all worldview fields UNKNOWN (lead AGNOS). Not plotted.

## Life and work

Bourg-la-Reine, Paris; prison 1831–32; killed in a duel [S1].

## Contribution and impact

Galois theory; early group theory [S1].

## Childhood and education

Taught by his mother to 12; Louis-le-Grand [S1].

## Adult working worldview

Not known from his words.

## Heritage (context only)

French [S1].

## Timing

1829–1832, age 18 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Dupuy 1896 and his collected writings.

## Research log

- 2026-10-19: Read MacTutor.
