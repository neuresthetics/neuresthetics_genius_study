---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA6)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA6, order P32: F 3, rank 203). Source: Britannica, signed by George Duncan Painter (scholars edition, read in full). Lasting work: À la recherche du temps perdu (1913–27); 'The entire climate of the 20th-century novel was affected' by it (S1). First volume November 1913; the last three volumes are posthumous, so the span ends at his death, 1922 (posthumous rule; P29 never past death). Span 1913–1922, age 42. Worldview: no own words on belief read; S1 reads the novel as 'set in the context of human religious experience', its subject 'salvation' (a critic's reading of fiction, not a profession). Catholic father, Jewish mother (S1). primary_system UNKNOWN; A UNKNOWN; not a scientist; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}

identity:
  id: proust-marcel
  display_name: "Marcel Proust"
  roster:
    canonical_name: "Marcel Proust"
    rank: 203
    F: 3
    models: [Claude, Gemini, GPT]
    band: "core (3–4)"
    status: "core"
    field: "literature"
    field_bucket: "literature"
  full_name: {value: "Marcel Proust", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  native_name: {value: "Marcel Proust", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  aliases:
    - {name: "Marcel-Proust", kind: "roster alias"}
    - {name: "Proust-Marcel", kind: "roster alias"}

basics:
  birth:
    date: {value: "1871-07-10", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
    place: {value: "Auteuil, near Paris", modern_name: "Auteuil, Paris, France", polity_then: "France", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  death:
    date: {value: "1922-11-18", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
    place: {value: "Paris", modern_name: "Paris, France", polity_then: "France", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1913, certainty: 0.7, cites: [{source: S1, locator: "Works"}], how_known: "Du côté de chez Swann, November 1913 (S1); publication (P30)."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "Works"}], how_known: "1913 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "France (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "Works"}], how_known: "Paris."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["French"], certainty: 0.7, cites: [{source: S1, locator: "Works"}], how_known: "French titles."}
  occupations: {value: ["novelist", "essayist", "translator"], certainty: 0.7, cites: [{source: S1, locator: "Introduction; Works"}], how_known: "Britannica: translated Ruskin."}

contribution:
  fields: {value: ["literature"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "À la recherche du temps perdu (In Search of Lost Time)", year: 1913, kind: "work", lasting: "'The entire climate of the 20th-century novel was affected by À la recherche du temps perdu, which is one of the supreme achievements of modern fiction' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Works; Legacy"}], how_known: "Britannica: volumes 1913–27; the last three posthumous."}
  evidence_of_impact:
    - {value: "Prix Goncourt (1919) for À l'ombre des jeunes filles en fleurs", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "Works"}], how_known: "Britannica: December 1919."}
  major_works:
    - {value: "Les Plaisirs et les jours", year: 1896, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "Works"}], how_known: "Britannica."}
    - {value: "Contre Sainte-Beuve", year: 1909, kind: "other", certainty: 0.5, cites: [{source: S1, locator: "Works"}], how_known: "Britannica: written c. 1908–09, published 1954."}
  honours:
    - {value: "Prix Goncourt", year: 1919, certainty: 0.7, cites: [{source: S1, locator: "Works"}], how_known: "Britannica."}
  definition_fit: {value: "clearly meets", rationale: "Affected the entire climate of the 20th-century novel (S1).", certainty: 0.7, cites: [{source: S1, locator: "Legacy"}], how_known: "Britannica."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Father Adrien Proust, eminent physician of provincial French Catholic descent; mother Jeanne (Weil), from a wealthy Jewish family", role: "family", certainty: 0.7, cites: [{source: S1, locator: "Early life and education"}], how_known: "Britannica."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling:
    - {value: "Lycée Condorcet (1882–89; philosophy master Alphonse Darlu); School of Political Sciences; licences in law (1893) and literature (1895)", certainty: 0.7, cites: [{source: S1, locator: "Early life and education"}], how_known: "Britannica."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1913–1922", certainty: 0.7, cites: [{source: S1, locator: "Works"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: {value: UNKNOWN, how_known: "No own words on belief read. S1's reading of the novel ('subject being salvation'; 'context of human religious experience') is a critic's account of fiction, not a profession."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Heritage only: Catholic father (S1)."}
    - {code: JUDA, reason: "Heritage only: Jewish mother (S1)."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing first-hand read (P19)."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30); no statement on nature read."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, so the P4 test cannot be applied (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "Own words quoted in S1 ('Suddenly ... the universe regained in my eyes an immeasurable value', on reading Ruskin, c. 1899) are aesthetic, not doctrinal. Read Topping, Proust's Gods (2000), and the correspondence."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: "Catholic father, Jewish mother", certainty: 0.7, cites: [{source: S1, locator: "Early life and education"}], how_known: "Britannica; baptism not stated in S1."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1913–1922", certainty: 0.7, cites: [{source: S1, locator: "Works"}], how_known: "Swann (1913) to his death (1922), his last act on the novel; the volumes of 1923–27 are posthumous (guide: posthumous work dated by the last act in life or the death year)."}
  age_at_first_lasting_contribution: {value: 42, certainty: 0.7, cites: [{source: S1, locator: "Introduction; Works"}], how_known: "1913 − 1871 = 42 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Novel of memory (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions: []
collaborators: []

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 203"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Worldview: no source."
  open_questions:
    - "Religious views (Topping; correspondence)."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "George Duncan Painter"
    citation: "Painter, George Duncan. 'Marcel Proust.' Encyclopaedia Britannica (scholars edition). https://kids.britannica.com/scholars/article/Marcel-Proust/61641"
    url: "https://kids.britannica.com/scholars/article/Marcel-Proust/61641"
    accessed: 2026-10-19
    reliability_note: "Signed article, scholars edition, read in full."
    used_for: [identity, basics, contribution, childhood, heritage, timing]
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

Marcel Proust (1871–1922), novelist [S1]. Draft: worldview UNKNOWN. Not plotted.

## Life and work

Auteuil; Paris [S1].

## Contribution and impact

À la recherche, 1913–27 [S1].

## Childhood and education

Lycée Condorcet [S1].

## Adult working worldview

None read.

## Heritage (context only)

Catholic father, Jewish mother [S1].

## Timing

1913–1922, age 42 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Religious views.

## Research log

- 2026-10-19: Read Britannica (Painter, scholars edition).
