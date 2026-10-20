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
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z6, order P32: F 3, rank 157). Basics and own words from the INA 'Archives du XXe siècle' interview with Jean-José Marchand (filmed 1972; INA biography and bibliography on the same pages), chapter 2 '...et l'indifférence religieuse': 'jamais dans toute mon enfance, aucun problème, aucune inquiétude religieuse, ne s'est posé à moi'; 'jamais, à aucun moment, enfin, il n'y a jamais eu pour moi aucun problème religieux'. The 1988 Eribon lines ('sourd aux réponses religieuses'; 'un rapport avec un Dieu personnel, jamais') were seen only as second-hand quotations (V3), so leads only. Not a scientist (social science; Sen precedent). Span 1949–1971. primary_system BELOW_THRESHOLD (leads AGNOS, ATHE); A BELOW_THRESHOLD; B UNKNOWN; C, D, E UNKNOWN; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}

identity:
  id: levi-strauss-claude
  display_name: "Claude Lévi-Strauss"
  roster:
    canonical_name: "Claude Levi-Strauss"
    rank: 157
    F: 3
    models: [Claude, DeepSeek, GPT]
    band: "core (3–4)"
    status: "core"
    field: "anthropology"
    field_bucket: "social science"
  full_name: {value: "Claude Lévi-Strauss", certainty: 0.7, cites: [{source: S1, locator: "Biographie"}], how_known: "INA."}
  native_name: {value: "Claude Lévi-Strauss", certainty: 0.7, cites: [{source: S1, locator: "Biographie"}], how_known: "INA."}
  aliases:
    - {name: "Claude Levi-Strauss", kind: "transliteration"}
    - {name: "Claude-Levi-Strauss", kind: "roster alias"}

basics:
  birth:
    date: {value: "1908", certainty: 0.7, cites: [{source: S1, locator: "Biographie"}], how_known: "INA: 'né en 1908 à Bruxelles'."}
    place: {value: "Brussels", modern_name: "Brussels, Belgium", polity_then: "Belgium", certainty: 0.7, cites: [{source: S1, locator: "Biographie"}], how_known: "INA."}
  death:
    date: {value: UNKNOWN, how_known: "Not in the sources read."}
    place: {value: UNKNOWN, how_known: "Not in the sources read."}
  first_lasting_contribution_year: {value: 1949, certainty: 0.7, cites: [{source: S1, locator: "Bibliographie"}], how_known: "Les Structures élémentaires de la parenté, PUF, 1949."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "Bibliographie"}], how_known: "1949 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "Biographie"}], how_known: "Belgium (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "Biographie"}], how_known: "Paris (EPHE, Collège de France) over the span."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["French"], certainty: 0.7, cites: [{source: S1, locator: "Bibliographie"}], how_known: "French titles."}
  occupations: {value: ["anthropologist", "professor (EPHE; Collège de France)"], certainty: 0.7, cites: [{source: S1, locator: "Biographie"}], how_known: "INA."}

contribution:
  fields: {value: ["social anthropology", "structuralism"], certainty: 0.7, cites: [{source: S1, locator: "Biographie"}], how_known: "INA."}
  lasting_original_contributions:
    - {value: "Les Structures élémentaires de la parenté", year: 1949, kind: work, lasting: "his work 'est au fondement du courant de pensée dit structuraliste' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Biographie; Bibliographie"}], how_known: "INA biography and bibliography."}
    - {value: "Mythologiques (4 vols; vol. 4 L'Homme nu)", year: 1971, kind: "body of work", lasting: "structural analysis of myth (S1)", certainty: 0.5, cites: [{source: S1, locator: "Bibliographie"}], how_known: "INA bibliography; lastingness the coder's call, so the span end is 0.5."}
  evidence_of_impact:
    - {value: "Brought anthropology into French social science in the 1960s; founded structuralism", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "Biographie"}], how_known: "INA."}
  major_works:
    - {value: "Tristes Tropiques", year: 1955, kind: book, certainty: 0.7, cites: [{source: S1, locator: "Biographie"}], how_known: "INA."}
  honours:
    - {value: "Elected to the Académie française", year: 1973, certainty: 0.7, cites: [{source: S1, locator: "Biographie"}], how_known: "INA."}
  definition_fit: {value: "clearly meets", rationale: "Founder of structural anthropology (S1).", certainty: 0.7, cites: [{source: S1, locator: "Biographie"}], how_known: "Founder of structuralism."}

childhood:
  family_religion: {value: "Jewish by descent; parents without religious feeling", certainty: 0.7, cites: [{source: S1, locator: "ch. 2"}], how_known: "(interview) 'ni mes parents, ni mes oncles et tantes n'avaient le moindre sentiment religieux'."}
  family_religious_practice: {value: "Formal observances only, out of regard for his grandfather", certainty: 0.7, cites: [{source: S1, locator: "ch. 2"}], how_known: "(interview)."}
  parents_and_household:
    - {value: "Maternal grandfather, grand rabbin of Versailles (household during 1914–18)", role: grandparent, certainty: 0.7, cites: [{source: S1, locator: "ch. 2"}], how_known: "(interview)."}
  household_circumstances: {value: "Family of artists", certainty: 0.7, cites: [{source: S1, locator: "Biographie"}], how_known: "INA."}
  schooling: []
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["French"], certainty: 0.5, cites: [{source: S1, locator: "Biographie"}], how_known: "Inferred."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1949–1971", certainty: 0.5, cites: [{source: S1, locator: "Bibliographie"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "(interview, 1972, one year after the span) Lifelong religious indifference: 'il n'y a jamais eu pour moi aucun problème religieux'. Indifference names no position. Leads AGNOS and ATHE; the 1988 Eribon lines ('sourd aux réponses religieuses'; no 'rapport avec un Dieu personnel, jamais'; believers have 'le sens du mystère') were seen only second-hand (V3)."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: AGNOS, reason: "Lead: indifference; 'mystery' of the cosmos (second-hand, 1988)."}
    - {code: ATHE, reason: "Lead: no personal God ever (second-hand, 1988)."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "(interview) Indifference; no locus stated."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30: social anthropology, as Sen); nothing read on nature."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: UNKNOWN, how_known: "B_cause is UNKNOWN, which takes precedence (§6, P19)."}
  statements:
    - text: "Non, jamais, à aucun moment, enfin, il n'y a jamais eu pour moi aucun problème religieux, je puis dire."
      cites: [{source: S1, locator: "ch. 2"}]
      date: "1972"
      context: "INA interview with Jean-José Marchand, answer on adolescent religious crisis."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
  changes_over_life: []
  coder_notes: "Read De près et de loin (1988), p. 14 and the religion passage, in the book itself to lift V3."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "French Jewish", certainty: 0.7, cites: [{source: S1, locator: "ch. 2"}], how_known: "(interview)."}
  religious_heritage_by_birth: {value: "Jewish", certainty: 0.7, cites: [{source: S1, locator: "ch. 2"}], how_known: "(interview)."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1949–1971", certainty: 0.5, cites: [{source: S1, locator: "Bibliographie"}], how_known: "Structures élémentaires (1949) to L'Homme nu (1971) (P29, P30); end is the coder's call on lastingness."}
  age_at_first_lasting_contribution: {value: 41, certainty: 0.7, cites: [{source: S1, locator: "Biographie; Bibliographie"}], how_known: "1949 − 1908 = 41 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Structural method modelled on linguistics, not proof (S1).", certainty: 0.5, cites: [{source: S1, locator: "ch. 35"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "Collège de France", role: "chair of social anthropology", years: "1959–", kind: university, certainty: 0.7, cites: [{source: S1, locator: "Biographie"}], how_known: "INA."}
collaborators: []

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 157"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Britannica would not load; basics from INA's own biography."
    - "Adult views seen first-hand only as indifference (1972)."
  open_questions:
    - "De près et de loin (1988) read first-hand."

sources:
  - id: S1
    type: primary
    kind: "other"
    author: "Claude Lévi-Strauss, interviewed by Jean-José Marchand"
    citation: "Marchand, Jean-José. 'Claude Lévi-Strauss.' Archives du XXe siècle (filmed 1972), INA Entretiens patrimoniaux, transcription. https://entretiens.ina.fr/entretien/38/claude-levi-strauss/transcription/2"
    url: "https://entretiens.ina.fr/entretien/38/claude-levi-strauss/transcription/2"
    accessed: 2026-10-19
    reliability_note: "Filmed interview, INA transcription (recorded_interview, P8), with an INA biography and bibliography."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions]
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

Claude Lévi-Strauss (b. 1908), anthropologist [S1]. Draft: primary and A BELOW_THRESHOLD (leads AGNOS, ATHE); B UNKNOWN. Not plotted.

## Life and work

Brussels, Paris, Brazil, New York, Paris [S1].

## Contribution and impact

Structuralism; Mythologiques [S1].

## Childhood and education

Rabbi grandfather; unbelieving parents [S1].

## Adult working worldview

Lifelong religious indifference, by his 1972 account [S1].

## Heritage (context only)

French Jewish [S1].

## Timing

1949–1971, age 41 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- De près et de loin first-hand.

## Research log

- 2026-10-19: Read the INA interview pages.
