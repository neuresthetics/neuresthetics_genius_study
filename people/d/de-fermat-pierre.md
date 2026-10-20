---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA8)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA8, order P32: F 3, rank 210). Source: Britannica, signed by Carl B. Boyer (scholars edition, read in full). Lasting work: his method for tangents and maxima and minima, defended in the 1638 controversy with Descartes through Mersenne and 'fully justified some 30 years later in the calculus of Sir Isaac Newton' (he is 'regarded as the inventor of the differential calculus'); 'Fermat's lesser theorem', announced in letters (1640; 'A more important result'); and the principle of least time for refraction, 'twenty years' after Descartes's 1637 Dioptrique (so about 1657), later 'verified experimentally' by Fizeau (S1). Span 1638–1657 at 0.5 (1657 is inferred from 'twenty years later'), age 37. Scientist (P30): the principle of least time is a law about light; B 3 at 0.5, alternative 4 (P35). Worldview: no own words read; primary education in a Franciscan school (S1). primary_system UNKNOWN; A UNKNOWN; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}

identity:
  id: de-fermat-pierre
  display_name: "Pierre de Fermat"
  roster:
    canonical_name: "Pierre de Fermat"
    rank: 210
    F: 3
    models: [Claude, Gemini, Grok]
    band: "core (3–4)"
    status: "core"
    field: "mathematics"
    field_bucket: "mathematics"
  full_name: {value: "Pierre de Fermat", certainty: 0.7, cites: [{source: S1, locator: "Introduction; Life and early work"}], how_known: "Britannica: 'known as Pierre de Fermat' from before 1638."}
  native_name: {value: "Pierre de Fermat", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  aliases:
    - {name: "Fermat-Pierre de", kind: "roster alias"}

basics:
  birth:
    date: {value: "1601-08-17", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
    place: {value: "Beaumont-de-Lomagne", modern_name: "Beaumont-de-Lomagne, France", polity_then: "Kingdom of France", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  death:
    date: {value: "1665-01-12", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
    place: {value: "Castres", modern_name: "Castres, France", polity_then: "Kingdom of France", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1638, certainty: 0.7, cites: [{source: S1, locator: "Disagreement with other Cartesian views"}], how_known: "1638 controversy with Descartes, through Mersenne, on the validity of their tangent methods (S1): the earliest documented public statement of the method (P30)."}
  era_bucket: {value: "1600 to 1749", certainty: 1.0, cites: [{source: S1, locator: "text"}], how_known: "1638 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "France (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "Life and early work"}], how_known: "Toulouse."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Latin", "French"], certainty: 0.5, cites: [{source: S1, locator: "Analyses of curves"}], how_known: "Latin paper title (S1); letters in French inferred."}
  occupations: {value: ["lawyer", "magistrate", "mathematician"], certainty: 0.7, cites: [{source: S1, locator: "Life and early work"}], how_known: "Britannica: councillor at Toulouse; Criminal Court."}

contribution:
  fields: {value: ["mathematics", "number theory", "optics"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Method of tangents and of maxima and minima (equivalent to differentiation)", year: 1638, kind: "method", lasting: "'led him to be regarded as the inventor of the differential calculus'; 'Fermat's views were fully justified some 30 years later in the calculus of Sir Isaac Newton' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Introduction; Disagreement with other Cartesian views"}], how_known: "Developed in the mid-1630s; first documented public statement the 1638 controversy (S1)."}
    - {value: "Fermat's lesser (little) theorem", year: 1640, kind: "discovery", lasting: "'now known as Fermat's lesser theorem'; he is 'often called the founder of the modern theory of numbers' (S1)", certainty: 0.5, cites: [{source: S1, locator: "Work on theory of numbers"}], how_known: "S1 dates his 1640 letters (on Fermat numbers, to Pascal and others); the lesser theorem's own letter is not dated in S1, so 0.5."}
    - {value: "Principle of least time (law of refraction)", year: 1657, kind: "law or principle", lasting: "'His argument concerning the speed of light was found later to be in agreement with the wave theory of ... Huygens, and in 1849 it was verified experimentally by A.-H.-L. Fizeau' (S1)", certainty: 0.5, cites: [{source: S1, locator: "Disagreement with other Cartesian views"}], how_known: "'Twenty years later' than Descartes's Dioptrique (1637), so about 1657; inferred, 0.5."}
  evidence_of_impact:
    - {value: "'often called the founder of the modern theory of numbers'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
    - {value: "Fermat's last theorem, proved by Wiles (1995)", kind: "named after them", certainty: 0.7, cites: [{source: S1, locator: "Work on theory of numbers"}], how_known: "Britannica."}
  major_works:
    - {value: "'De Linearum Curvarum cum Lineis Rectis Comparatione' (his only mathematical work published in his lifetime)", year: 1660, kind: "paper or paper series", certainty: 0.7, cites: [{source: S1, locator: "Analyses of curves"}], how_known: "Britannica."}
    - {value: "Introduction to Loci (analytic geometry; posthumous 1679)", year: 1679, kind: "paper or paper series", certainty: 0.7, cites: [{source: S1, locator: "Life and early work"}], how_known: "Britannica."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Founder of modern number theory (S1).", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Of Basque origin", role: "family", certainty: 0.7, cites: [{source: S1, locator: "Life and early work"}], how_known: "Britannica."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling:
    - {value: "Local Franciscan school; law probably at Toulouse, perhaps Bordeaux; baccalaureate in law, Orléans (1631)", certainty: 0.7, cites: [{source: S1, locator: "Life and early work"}], how_known: "Britannica."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1638–1657", certainty: 0.5, cites: [{source: S1, locator: "Disagreement with other Cartesian views"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: {value: UNKNOWN, how_known: "No own words on belief read. Franciscan schooling (S1) is context."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Heritage only: Franciscan school (S1)."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing first-hand read (P19)."}
    B_cause: 
      value: 3
      basis: inference_from_work
      certainty: 0.5
      cites: [{source: S1, locator: "Disagreement with other Cartesian views"}]
      how_known: "Scientist (P30): the principle of least time is a law about light, later verified experimentally (S1). B from working science with no statement of his own on law and exception, so 3 at 0.5, alternative 4, never 4 (P35)."
      rationale: "Refraction derived from 'nature always chooses the shortest path' as a principle of least time (S1): lawful nature in his science. Alternative 4."
      alternatives:
        - {value: 4, note: "Working science cannot tell lawful-with-exceptions from exceptionless (P35).", cites: [{source: S1, locator: "Disagreement with other Cartesian views"}]}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, so the P4 test cannot be applied (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "Read Mahoney, The Mathematical Career of Pierre de Fermat (1973), for religion; scientist status rests on the least-time principle (P33 does not apply: a law, not an invention)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated in S1 beyond Franciscan schooling."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1638–1657", certainty: 0.5, cites: [{source: S1, locator: "Disagreement with other Cartesian views"}], how_known: "Tangent-method controversy (1638) to the least-time principle (about 1657), the first and last lasting items (P29, P30); 0.5, following the weakest lasting item."}
  age_at_first_lasting_contribution: {value: 37, certainty: 0.7, cites: [{source: S1, locator: "Introduction; Disagreement with other Cartesian views"}], how_known: "1638 − 1601 = 37 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "Analytic geometry of curves (S1).", certainty: 0.5, cites: [{source: S1, locator: "Analyses of curves"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "Parlement of Toulouse", role: "councillor; Criminal Court", years: "1634–1665", kind: "government or state body", certainty: 0.7, cites: [{source: S1, locator: "Life and early work"}], how_known: "Britannica: councillor 1634; Criminal Court 1638."}
collaborators:
  - {value: "Blaise Pascal", relation: "correspondent", note: "probability (1654)", certainty: 0.7, cites: [{source: S1, locator: "Disagreement with other Cartesian views"}], how_known: "Britannica."}
  - {value: "René Descartes", relation: "rival or critic", note: "tangents; refraction", certainty: 0.7, cites: [{source: S1, locator: "Disagreement with other Cartesian views"}], how_known: "Britannica."}
  - {value: "Marin Mersenne", relation: "correspondent", note: "intermediary", certainty: 0.7, cites: [{source: S1, locator: "Disagreement with other Cartesian views"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 210"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Worldview: no source."
    - "Least-time date inferred (about 1657)."
  open_questions:
    - "Scientist status via the least-time principle; religion (Mahoney)."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Carl B. Boyer"
    citation: "Boyer, Carl B. 'Pierre de Fermat.' Encyclopaedia Britannica (scholars edition). https://kids.britannica.com/scholars/article/Pierre-de-Fermat/34048"
    url: "https://kids.britannica.com/scholars/article/Pierre-de-Fermat/34048"
    accessed: 2026-10-19
    reliability_note: "Signed article, scholars edition, read in full."
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

Pierre de Fermat (1601–1665), mathematician [S1]. Draft: B 3 (0.5); worldview UNKNOWN. Not plotted.

## Life and work

Beaumont-de-Lomagne; Toulouse [S1].

## Contribution and impact

Tangents 1638; lesser theorem 1640; least time c. 1657 [S1].

## Childhood and education

Franciscan school; Orléans [S1].

## Adult working worldview

None read.

## Heritage (context only)

Not stated.

## Timing

1638–1657 (0.5), age 37 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Scientist status.

## Research log

- 2026-10-19: Read Britannica (Boyer, scholars edition).
