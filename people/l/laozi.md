---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA5)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA5, order P32: F 3, rank 198). Source: Britannica, signed by Max Kaltenmark (revised by Roger T. Ames; read in full). Lasting work: the Daodejing, 'a primary Daoist writing', traditionally his; but 'The Daodejing, as we have it, cannot be the work of a single author', a Guodian version dates 'to before 300 bce', and 'The name Laozi seems to represent a certain type of sage rather than an individual' (S1). The text is therefore context only (P42, Sun Tzu precedent): primary_system UNKNOWN (lead TAO); A, B UNKNOWN; mid_basin UNKNOWN. Life dates UNKNOWN ('flourished 6th century bce' is traditional; some place Lao Dan at the end of the 4th century bce), so first-lasting year, era (P39), span and age are UNKNOWN. Not plotted. Draft, not reviewed."}

identity:
  id: laozi
  display_name: "Laozi"
  roster:
    canonical_name: "Laozi"
    rank: 198
    F: 3
    models: [Claude, DeepSeek, Gemini]
    band: "core (3–4)"
    status: "core"
    field: "philosophy"
    field_bucket: "philosophy"
  full_name: {value: "Laozi", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica; Sima Qian gives family name Li, proper name Er, appellation Dan."}
  native_name: {value: "老子", certainty: 0.5, cites: [{source: S1, locator: "Introduction"}], how_known: "Standard Chinese form (coder's knowledge); not printed in S1."}
  aliases:
    - {name: "Lao Tzu", kind: "roster alias"}
    - {name: "Li Er", kind: "birth name"}
    - {name: "Lao Dan", kind: "other"}
    - {name: "Lao Jun", kind: "title or honorific"}

basics:
  birth:
    date: {value: UNKNOWN, how_known: "Unknown; 'flourished 6th century bce' is traditional (S1)."}
    place: {value: "Quren, Hu district, state of Chu", modern_name: "Luyi, Henan, China", polity_then: "State of Chu", certainty: 0.5, cites: [{source: S1, locator: "The life of Laozi"}], how_known: "Sima Qian, as reported by Britannica, who notes he 'had little solid information'."}
  death:
    date: {value: UNKNOWN, how_known: "Unknown; 'nobody knows what has become of him' (Sima Qian, S1)."}
    place: {value: UNKNOWN, how_known: "Unknown (S1)."}
  first_lasting_contribution_year: {value: UNKNOWN, how_known: "The Daodejing is undated and composite; a Guodian version dates to before 300 BCE (S1) (P39)."}
  era_bucket: {value: UNKNOWN, how_known: "No dated lasting work and no reliable life dates (P39): tradition puts him in the 6th century BCE, others at the end of the 4th (S1), across the -500 edge."}
  region_of_birth: {value: "East Asia", certainty: 0.5, cites: [{source: S1, locator: "The life of Laozi"}], how_known: "China (P3), on the Shiji tradition."}
  region_of_work: {value: "East Asia", certainty: 0.5, cites: [{source: S1, locator: "The life of Laozi"}], how_known: "Zhou court, per tradition."}
  sex_as_recorded: {value: "male", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "As recorded in tradition."}
  languages_of_work: {value: ["Classical Chinese"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "The Daodejing."}
  occupations: {value: ["philosopher", "archivist (shi) at the Zhou court"], certainty: 0.5, cites: [{source: S1, locator: "The life of Laozi"}], how_known: "Sima Qian's account, of doubtful historicity."}

contribution:
  fields: {value: ["philosophy", "Daoism"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Daodejing (attributed)", kind: "work", lasting: "'a primary Daoist writing'; Laozi 'the first philosopher of Chinese Daoism' (S1)", certainty: 0.5, cites: [{source: S1, locator: "Introduction; The life of Laozi"}], how_known: "Britannica: traditionally his, but composite ('cannot be the work of a single author') and undated; 0.5, the floor, for attribution (P42)."}
  evidence_of_impact:
    - {value: "Venerated as a philosopher by Confucians, as a saint or god in popular religion, and by Daoists as an emanation of the Dao", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "Introduction; Hagiographical legends"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "arguable", rationale: "The founding figure of Daoism, but possibly a type of sage rather than an individual (S1).", certainty: 0.5, cites: [{source: S1, locator: "The life of Laozi"}], how_known: "Coder's reading."}

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
  working_years: {value: UNKNOWN, how_known: "Equals timing.major_work_period (UNKNOWN, P39)."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: {value: UNKNOWN, how_known: "Nothing attributable to him (P42): the Daodejing is composite and 'The name Laozi seems to represent a certain type of sage rather than an individual' (S1). Read as context, the text's Dao is 'the immanent and transcendent source of the universe' (S1, Top Questions, not citable under P26). Lead TAO."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: TAO, reason: "Lead: the Daodejing, context only (P42)."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing attributable (P42)."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist; nothing attributable (P42)."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing attributable."}
    D_authority: {value: UNKNOWN, how_known: "Nothing attributable."}
    E_scope: {value: UNKNOWN, how_known: "Nothing attributable."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, so the P4 test cannot be applied (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "If v8 wants the text scored as context, a scholarly translation of the Guodian and Mawangdui versions (e.g. Henricks) would be needed; the attribution ruling would decide."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Unknown."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: UNKNOWN, how_known: "No dated lasting contribution (P39)."}
  age_at_first_lasting_contribution: {value: UNKNOWN, how_known: "No dated lasting contribution and no birth date (P39)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Aphoristic, not geometric (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions: []
collaborators:
  - {value: "Confucius", relation: "other", note: "a celebrated but legendary meeting", certainty: 0.5, cites: [{source: S1, locator: "The life of Laozi"}], how_known: "Britannica: 'the meeting seems a mere legend'."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 198"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Historicity doubtful; text composite (P42)."
  open_questions:
    - "Whether the Daodejing may be scored as context."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Max Kaltenmark (revised by Roger T. Ames)"
    citation: "Kaltenmark, Max, and Roger T. Ames. 'Laozi.' Encyclopaedia Britannica. https://www.britannica.com/biography/Laozi"
    url: "https://www.britannica.com/biography/Laozi"
    accessed: 2026-10-19
    reliability_note: "Signed article, read in full (Top Questions boxes not used, P26)."
    used_for: [identity, basics, contribution, worldview, collaborators]
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

Laozi (traditionally 6th century BCE), Daoist sage [S1]. Draft: all UNKNOWN; text composite (P42). Not plotted.

## Life and work

Chu; Zhou court, per Sima Qian [S1].

## Contribution and impact

Daodejing (attributed) [S1].

## Childhood and education

Unknown.

## Adult working worldview

Nothing attributable.

## Heritage (context only)

Unknown.

## Timing

UNKNOWN (P39).

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Scoring the text as context.

## Research log

- 2026-10-19: Read Britannica (Kaltenmark, Ames).
