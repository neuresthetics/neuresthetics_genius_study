---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA4)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA4, order P32: F 3, rank 195). Source: Britannica, signed by Dirk Jan Struik (scholars edition, read in full). Lasting work: the equations that bear his name, first used in his prize essay on the libration of the Moon (1764, French Academy prize), and Mécanique analytique (1788), 'the basis for all later work in this field'; span 1764–1788 by the prize award and publication (P30 #1), age 28. His earlier calculus of variations (praised by Euler) is undated in the source; 0.5 on the first year, alternative earlier. Scientist (P30): analytic and celestial mechanics are results about physical systems; no statement of his own, so B 3 at 0.5, alt 4 (P35). No worldview source: primary_system UNKNOWN; A UNKNOWN; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}

identity:
  id: lagrange-joseph-louis
  display_name: "Joseph-Louis Lagrange"
  roster:
    canonical_name: "Joseph-Louis Lagrange"
    rank: 195
    F: 3
    models: [Claude, Gemini, Grok]
    band: "core (3–4)"
    status: "core"
    field: "mathematics"
    field_bucket: "mathematics"
  full_name: {value: "Joseph-Louis Lagrange, comte de l'Empire", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  native_name: {value: "Giuseppe Luigi Lagrangia", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica: original Italian."}
  aliases:
    - {name: "Lagrange-Joseph-Louis", kind: "roster alias"}
    - {name: "Giuseppe Luigi Lagrangia", kind: "birth name"}

basics:
  birth:
    date: {value: "1736-01-25", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
    place: {value: "Turin", modern_name: "Turin, Italy", polity_then: "Kingdom of Sardinia (Sardinia-Piedmont)", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  death:
    date: {value: "1813-04-10", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
    place: {value: "Paris", modern_name: "Paris, France", polity_then: "French Empire", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1764, certainty: 0.5, cites: [{source: S1, locator: "para. 3"}], how_known: "Prize essay on the libration of the Moon, 1764, in which 'he used the equations that now bear his name' (S1); the award year stands for the essay's submission (P30 #1). 0.5: his calculus of variations, praised by Euler, is earlier but undated in S1; alternative an earlier year for that."}
  era_bucket: {value: "1750 to 1849", certainty: 0.7, cites: [{source: S1, locator: "para. 3"}, {source: S1, locator: "Introduction"}], how_known: "1764–1788 (P2); an earlier alternative stays after 1750 (he was born 1736 and taught from about age 19)."}
  region_of_birth: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Italy (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "para. 4–5"}], how_known: "Berlin 1766–1787; Paris."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["French", "Latin"], certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "French titles; Latin early papers (coder's reading)."}
  occupations: {value: ["mathematician", "professor"], certainty: 0.7, cites: [{source: S1, locator: "Introduction; para. 6"}], how_known: "Britannica."}

contribution:
  fields: {value: ["analytic mechanics", "celestial mechanics", "number theory", "algebra"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Lagrange's equations (libration of the Moon essay)", year: 1764, kind: "law or principle", lasting: "'the equations that now bear his name' (S1)", certainty: 0.5, cites: [{source: S1, locator: "para. 3"}], how_known: "Britannica; French Academy prize 1764 (0.5, see first-lasting year)."}
    - {value: "Réflexions sur la résolution algébrique des équations", year: 1770, kind: "work", lasting: "'inaugurated a new period in algebra and inspired Évariste Galois to his group theory' (S1)", certainty: 0.7, cites: [{source: S1, locator: "para. 4"}], how_known: "Britannica."}
    - {value: "Mécanique analytique", year: 1788, kind: "work", lasting: "'the basis for all later work in this field' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  evidence_of_impact:
    - {value: "Lagrangian equations; generalized coordinates", kind: "named after them", certainty: 0.7, cites: [{source: S1, locator: "para. 5"}], how_known: "Britannica."}
  major_works:
    - {value: "Théorie des fonctions analytiques", year: 1797, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "para. 6"}], how_known: "Britannica."}
  honours:
    - {value: "Senator and count of the empire (Napoleon)", kind: "other", certainty: 0.7, cites: [{source: S1, locator: "para. 7"}], how_known: "Britannica; year not given."}
  definition_fit: {value: "clearly meets", rationale: "Mécanique analytique the basis for all later work (S1).", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Father treasurer to the king of Sardinia, who lost his fortune in speculation", role: "father", certainty: 0.7, cites: [{source: S1, locator: "para. 2"}], how_known: "Britannica."}
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
  working_years: {value: "1764–1788", certainty: 0.5, cites: [{source: S1, locator: "para. 3"}, {source: S1, locator: "Introduction"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: {value: UNKNOWN, how_known: "No source on his beliefs read. Struik: 'A kind and quiet man, living only for science' (S1)."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered: []
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing first-hand read (P19)."}
    B_cause: 
      value: 3
      basis: inference_from_work
      certainty: 0.5
      cites: [{source: S1, locator: "para. 4–5"}]
      how_known: "Scientist (P30): analytic and celestial mechanics are results about physical systems. B from working science with no statement of his own on law and exception, so 3 at 0.5, alternative 4, never 4 (P35)."
      rationale: "Mechanics as 'a lucid synthesis of the hundred years of research in mechanics since Newton'; the stability of the solar system (S1): lawful nature in his science. Alternative 4."
      alternatives:
        - {value: 4, note: "Working science cannot tell lawful-with-exceptions from exceptionless (P35).", cites: [{source: S1, locator: "para. 5"}]}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, and B 3 is only at 0.5, so the P4 test cannot be applied (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "Look for a scholar's account of his religious views (Delambre's 1816 éloge; a history of mathematics biography); the reported 'je n'ai pas eu besoin de cette hypothèse' belongs to Laplace, not him."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated in the source read."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1764–1788", certainty: 0.5, cites: [{source: S1, locator: "para. 3"}, {source: S1, locator: "Introduction"}], how_known: "From the libration essay (1764) to Mécanique analytique (1788), the listed lasting works (P29, P30 #1); start at 0.5."}
  age_at_first_lasting_contribution: {value: 28, certainty: 0.5, cites: [{source: S1, locator: "Introduction; para. 3"}], how_known: "1764 − 1736 = 28 (P30 year difference); younger on an earlier alternative."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "'one cannot find any figures in this work' (S1): analytic, not geometric.", certainty: 0.5, cites: [{source: S1, locator: "para. 5"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "Prussian Academy of Sciences, Berlin", role: "director of mathematics (post vacated by Euler)", years: "1766–1787", kind: "academy or learned society", certainty: 0.7, cites: [{source: S1, locator: "para. 3–4"}], how_known: "Britannica."}
  - {value: "École Polytechnique", role: "professor of mathematics", years: "1794", kind: "university", certainty: 0.5, cites: [{source: S1, locator: "para. 6"}], how_known: "Britannica: from its opening in 1794; end year not given."}
collaborators:
  - {value: "Leonhard Euler", relation: "correspondent", note: "praised his theory of variations; recommended him to Berlin", certainty: 0.5, cites: [{source: S1, locator: "para. 2–3"}], how_known: "Britannica; correspondence not stated as such."}
  - {value: "Gaspard Monge", relation: "collaborator", note: "fellow leading professor at the École Polytechnique", certainty: 0.7, cites: [{source: S1, locator: "para. 6"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 195"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "No worldview source."
  open_questions:
    - "Religious views (Delambre's éloge)."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Dirk Jan Struik"
    citation: "Struik, Dirk Jan. 'Joseph-Louis Lagrange, comte de l'Empire.' Encyclopaedia Britannica (scholars edition). https://kids.britannica.com/scholars/article/Joseph-Louis-Lagrange-comte-de-lEmpire/46837"
    url: "https://kids.britannica.com/scholars/article/Joseph-Louis-Lagrange-comte-de-lEmpire/46837"
    accessed: 2026-10-19
    reliability_note: "Signed article, read in full."
    used_for: [identity, basics, contribution, childhood, worldview, timing, institutions, collaborators]
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

Joseph-Louis Lagrange (1736–1813), mathematician [S1]. Draft: UNKNOWN; scientist, B 3 at 0.5. Not plotted.

## Life and work

Turin; Berlin; Paris [S1].

## Contribution and impact

Lagrange's equations (1764); Mécanique analytique (1788) [S1].

## Childhood and education

Not stated.

## Adult working worldview

None read.

## Heritage (context only)

Not stated.

## Timing

1764–1788, age 28 (0.5) [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Religious views.

## Research log

- 2026-10-19: Read Britannica (Struik).
