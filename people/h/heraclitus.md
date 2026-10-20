---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "AA1 audit fix (FAIL, P39 strict reading): era_bucket '-500 to 499' @0.5 -> UNKNOWN; life dates UNKNOWN and the c. 500 BCE floruit sits on the bucket edge. Plot unchanged (A 4 / B 3, faded)."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA1, order P32: F 3, rank 180). Source: SEP 'Heraclitus' (Daniel W. Graham, rev. 2023), a scholar's account with DK fragment numbers; the fragments are quoted in SEP's translation and attributed to him by scholarly agreement (P42), transmitted by later authors. Worldview by scholarly_reconstruction (0.5 cap): 'God is day night, winter summer, war peace ...' (B67) and 'This world-order ... no god nor man did create, but it ever was and is and will be: everliving fire, kindling in measures' (B30); 'all human laws are nourished by the one divine law' (B114). PANT 0.5 (two-part test: the divine identified with the whole of opposites, part 1; one eternal measured order, part 2), alt BELOW_THRESHOLD ('would and would not be called by the name of Zeus', B32). A 4 at 0.5 (alt 3); B 3 at 0.5 (alt 4): lawful measures, no exceptionless claim (P41-style); not counted a scientist (no listed theory about physical systems; the doctrines are metaphysical). C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD (A ≥ 3 only at 0.5, P10). Span UNKNOWN ('active around 500 BCE' is a floruit, not a composition range; P39). Plotted, faded, at A 4 / B 3. Draft, not reviewed."}

identity:
  id: heraclitus
  display_name: "Heraclitus"
  roster:
    canonical_name: "Heraclitus"
    rank: 180
    F: 3
    models: [Claude, DeepSeek, Grok]
    band: "core (3–4)"
    status: "core"
    field: "philosophy"
    field_bucket: "philosophy"
  full_name: {value: "Heraclitus of Ephesus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}
  native_name: {value: "Ἡράκλειτος", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Greek spelling the coder's."}
  aliases:
    - {name: "Heraclitus", kind: "roster alias"}

basics:
  birth:
    date: {value: UNKNOWN, how_known: "SEP: 'active around 500 BCE'; no birth year."}
    place: {value: "Ephesus", modern_name: "near Kuşadası, Turkey", polity_then: "Ionia (Persian Empire)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}
  death:
    date: {value: UNKNOWN, how_known: "Not stated in the source read."}
    place: {value: UNKNOWN, how_known: "Not stated."}
  first_lasting_contribution_year: {value: UNKNOWN, how_known: "Undated: 'active around 500 BCE' (S1) is a floruit, not a composition range or dating event (P39; RQ-Z9-N1 needs a composition range)."}
  era_bucket: {value: UNKNOWN, how_known: "P39 (strict reading, XW3): life dates UNKNOWN and the floruit 'around 500 BCE' (S1) sits on the -500 bucket edge, so no single bucket holds every adult year (AA1 audit)."}
  region_of_birth: {value: "Middle East and North Africa", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Ephesus, modern Turkey (P3)."}
  region_of_work: {value: "Middle East and North Africa", certainty: 0.5, cites: [{source: S1, locator: "1. Life and Work"}], how_known: "Ephesus."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Ancient Greek"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "SEP."}
  occupations: {value: ["philosopher"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}

contribution:
  fields: {value: ["philosophy", "cosmology"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}
  lasting_original_contributions:
    - {value: "Doctrines of flux and the unity of opposites; the Logos", year: UNKNOWN, kind: "body of work", lasting: "'Already in antiquity he was famous for advocating the coincidence of opposites, the flux doctrine' (S1); influence section", certainty: 0.7, cites: [{source: S1, locator: "opening; 3; 7. Influence"}], how_known: "SEP; a single book, undated."}
  evidence_of_impact:
    - {value: "Influence on Plato, Aristotle, the Stoics and Hegel", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "7. Influence"}], how_known: "SEP."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Founding Presocratic (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}

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
  primary_system: 
    value: PANT
    basis: scholarly_reconstruction
    certainty: 0.5
    cites: [{source: S1, locator: "4. Cosmology; 5. Theology"}]
    how_known: "SEP's reconstruction with fragment numbers (P42: fragments attributed by scholarly agreement); scholar's account, so 0.5."
    rationale: "Part 1: the divine is identified with the whole of opposites ('God is day night, winter summer, war peace, satiety hunger', B67; 'Divine power is manifest in all phenomena', S1). Part 2: one eternal, measured order ('ever was and is and will be: everliving fire, kindling in measures', B30) and 'the one divine law' (B114). Alternative BELOW_THRESHOLD: the 'only wise one, would and would not be called by the name of Zeus' (B32) keeps a ruling mind the reconstruction does not settle (S1)."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: PANT, reason: "Coded at 0.5: god is the whole of opposites; eternal measured fire."}
    - {code: STOIC, reason: "Not used: Stoicism is later; the Stoics drew on him (S1)."}
  lio_axes:
    A_locus: 
      value: 4
      basis: scholarly_reconstruction
      certainty: 0.5
      cites: [{source: S1, locator: "4. Cosmology; 5. Theology"}]
      how_known: "SEP reconstruction; 0.5 cap."
      rationale: "The divine is the world-order itself ('God is day night ...', B67), and 'no god nor man did create' the kosmos (B30): God as the order of nature, 4. Alternative 3: a governing 'wise one' (B32) and the thunderbolt that 'steers all things' read as a mind over the order."
      alternatives:
        - {value: 3, note: "Governing wise one (B32, B64).", cites: [{source: S1, locator: "4. Cosmology"}]}
    B_cause: 
      value: 3
      basis: scholarly_reconstruction
      certainty: 0.5
      cites: [{source: S1, locator: "4. Cosmology; 6"}]
      how_known: "SEP reconstruction; 0.5 cap. Not a scientist, so B rests on his statements about nature (P16)."
      rationale: "Everliving fire 'kindling in measures and being quenched in measures' (B30); human laws 'nourished by the one divine law' (B114): lawful order, with no explicit no-exception claim, so 3 (P41-style). Alternative 4: an uncreated world under fixed measures read as exceptionless."
      alternatives:
        - {value: 4, note: "Fixed measures read as exceptionless.", cites: [{source: S1, locator: "4. Cosmology"}]}
    C_ledger: {value: UNKNOWN, how_known: "Soul fragments (B36) concern transformation, not reward; not scored."}
    D_authority: {value: UNKNOWN, how_known: "Not scored: 'Having harkened not to me but to the Word (Logos)' (B50) is a lead for reason over authority."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is at least 3 only at 0.5; P10 caps mid_basin below the 0.7 bar."}
  statements:
    - text: "This world-order [kosmos], the same of all, no god nor man did create, but it ever was and is and will be: everliving fire, kindling in measures and being quenched in measures."
      cites: [{source: S1, locator: "4. Cosmology (B30)"}]
      date: "-500"
      context: "Fragment B30 (DK), from his book; transmitted by Clement of Alexandria; date is the floruit."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-19
      note: "SEP's translation of the fragment; attributed by scholarly agreement (P42). Scores rest on SEP's reconstruction (scholarly_reconstruction), not on the quotation alone."
  changes_over_life: []
  coder_notes: "Kahn (1979) and Graham's Texts of Early Greek Philosophy would firm up B32, B64 and B67 and test the PANT reading against a cosmic-mind (Logos) reading."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Ionian Greek (Ephesian aristocracy)", certainty: 0.5, cites: [{source: S1, locator: "1. Life and Work"}], how_known: "SEP."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: UNKNOWN, how_known: "Undated: floruit around 500 BCE only (P39)."}
  age_at_first_lasting_contribution: {value: UNKNOWN, how_known: "Undated (P39)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Oracular aphorisms, not geometric argument (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions: []
collaborators: []

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 180"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Fragments known only through later authors."
  open_questions:
    - "Kahn 1979; B32/B64."

sources:
  - id: S1
    type: secondary
    kind: "encyclopedia"
    author: "Daniel W. Graham"
    citation: "Graham, Daniel W. 'Heraclitus.' Stanford Encyclopedia of Philosophy (rev. 8 December 2023). https://plato.stanford.edu/entries/heraclitus/"
    url: "https://plato.stanford.edu/entries/heraclitus/"
    accessed: 2026-10-19
    reliability_note: "Signed scholarly reference article, read in full; fragment numbers (DK) and translations."
    used_for: [identity, basics, contribution, worldview, heritage, lane_b]
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

Heraclitus of Ephesus (fl. c. 500 BCE), philosopher [S1]. Draft: PANT (0.5); A 4, B 3 at 0.5. Plotted (faded).

## Life and work

Ephesus [S1].

## Contribution and impact

Flux; unity of opposites; Logos [S1].

## Childhood and education

Self-taught (B101) [S1].

## Adult working worldview

'God is day night ...' (B67); everliving fire in measures (B30) [S1].

## Heritage (context only)

Ephesian aristocracy [S1].

## Timing

Undated (P39).

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- B32 reading.

## Research log

- 2026-10-19: AA1 audit fix (FAIL, P39 strict reading): era_bucket '-500 to 499' @0.5 -> UNKNOWN; life dates UNKNOWN and the c. 500 BCE floruit sits on the bucket edge. Plot unchanged (A 4 / B 3, faded).
- 2026-10-19: Read SEP (Graham).
