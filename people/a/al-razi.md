---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z2)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z2 audit fixes (blind audit /workspace/genius_study_audit/gs_f70a593_Z2/run1/): the 0.5 ceiling now cites the scholarly-reconstruction ceiling (CODING_GUIDE §3), not P36. No score changed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z2, order P32: F 3, rank 142). Source: SEP 'Abu Bakr al-Razi' (Peter Adamson, rev. 2025). Scholarly reconstruction only: five eternal principles; God's existence 'demonstrated on the basis of the good design of the universe'; 'God intervenes to make the world as good as it can be'; creation ex nihilo impossible. His religion is disputed: the hostile Abū Ḥātim has him reject prophecy and miracles, but Doubts about Galen acknowledges 'books sent by God'. A scientist (P30: medicine; alchemy is described as chemical procedure, so it does not cut the inference). Span UNKNOWN (P12, P39: no lasting work dated in the source); era '500 to 1399'. primary_system BELOW_THRESHOLD (leads PLATO, DEISM, ISLAM); A 1 (0.5, alt 0); B 3 (0.5, alt 4); C UNKNOWN; D BELOW_THRESHOLD; E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Plotted (faded) at the next chart refresh. Draft, not reviewed."}

identity:
  id: al-razi
  display_name: "Al-Razi"
  roster:
    canonical_name: "Al-Razi"
    rank: 142
    F: 3
    models: [Claude, DeepSeek, Grok]
    band: "core (3–4)"
    status: core
    field: medicine
    field_bucket: medicine
  full_name: {value: "Abū Bakr Muḥammad ibn Zakariyyāʾ al-Rāzī", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
  native_name: {value: "Abū Bakr Muḥammad ibn Zakariyyāʾ al-Rāzī", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP (transliterated Arabic)."}
  aliases:
    - {name: "Razi", kind: "roster alias"}

basics:
  birth:
    date: {value: "865", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "heading (865–925 CE, 251–313 AH)"}], how_known: "SEP."}
    place: {value: "Rayy", modern_name: "Rey, near Tehran, Iran", polity_then: "Abbasid caliphate", certainty: 0.5, cites: [{source: S1, locator: "§1"}], how_known: "SEP: he 'hailed from' Rayy; birth there is the coder's reading, so 0.5."}
  death:
    date: {value: "925", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "heading"}], how_known: "SEP."}
    place: {value: UNKNOWN, how_known: "Not stated in the source read."}
  first_lasting_contribution_year: {value: UNKNOWN, how_known: "No lasting work is dated in SEP; the Book for al-Manṣūr is dedicated to a governor who died in 914, so it is before 914 (P12: undated items do not set the year)."}
  era_bucket: {value: "500 to 1399", certainty: 1.0, cites: [{source: S1, locator: "heading"}], how_known: "Every work falls between 865 and 925 (P2, P39)."}
  region_of_birth: {value: "Middle East and North Africa", certainty: 0.5, cites: [{source: S1, locator: "§1"}], how_known: "Iran, placed in MENA (P3)."}
  region_of_work: {value: "Middle East and North Africa", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "Hospitals in Rayy and Baghdad."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "As recorded."}
  languages_of_work: {value: ["Arabic"], certainty: 0.7, cites: [{source: S1, locator: "§1 (Arabic editions)"}], how_known: "SEP."}
  occupations: {value: ["physician and hospital director", "philosopher", "alchemist"], certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}

contribution:
  fields: {value: ["medicine", "philosophy", "alchemy"], certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
  lasting_original_contributions:
    - {value: "Doubts about Galen", year: UNKNOWN, kind: work, lasting: "his critique of Galen, 'the most significant surviving work for his philosophy' (S1)", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP; undated."}
    - {value: "The Book for al-Manṣūr", year: UNKNOWN, kind: work, lasting: "'a substantial medical treatise' (S1)", certainty: 0.5, cites: [{source: S1, locator: "§1"}], how_known: "SEP; before 914; lasting is the coder's call."}
  evidence_of_impact:
    - {value: "Made his fame mostly as a doctor", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
  major_works:
    - {value: "The Spiritual Medicine", year: UNKNOWN, kind: book, certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
    - {value: "The Philosophical Way of Life", year: UNKNOWN, kind: book, certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "A leading physician whose medical and philosophical works survive and are studied (S1).", certainty: 0.7, cites: [{source: S1, locator: "§1; §6"}], how_known: "Coder's reading."}

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
  working_years: {value: UNKNOWN, how_known: "Equals timing.major_work_period (UNKNOWN)."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "A revealed text's truth must accord with the truth found by reason (Adamson: 'At a minimum')", certainty: 0.5, cites: [{source: S1, locator: "§5"}], how_known: "Scholarly reconstruction (CODING_GUIDE §3 ceiling)."}
  primary_system:
    value: BELOW_THRESHOLD
    how_known: "Disputed in S1 §5: Abū Ḥātim (hostile) reports a rejection of prophecy and miracles; Fakhr al-Dīn reports Qurʾān interpretations in agreement with his philosophy; Doubts about Galen acknowledges 'books sent by God'. Leads: PLATO (five eternal principles, God and Soul), DEISM (God known by design, revelation possibly rejected; P27 fails if he accepted revelation), ISLAM."
  secondary_system: {value: UNKNOWN, how_known: "See primary."}
  candidate_codes_considered:
    - {code: DEISM, reason: "Lead only: P27 requires rejecting revelation, which is disputed (S1 §5)."}
    - {code: PLATO, reason: "Lead only: five eternals with Soul; no source calls him a Platonist outright."}
    - {code: ISLAM, reason: "Lead only: 'books sent by God' (S1 §5)."}
  lio_axes:
    A_locus:
      value: 1
      basis: scholarly_reconstruction
      certainty: 0.5
      cites: [{source: S1, locator: "§2"}]
      how_known: "Adamson: God is one of five eternal principles; God's existence is 'demonstrated on the basis of the good design of the universe'; the world was not created directly by God but begun by the Soul's desire, and 'God intervenes to make the world as good as it can be'; creation ex nihilo is impossible. Scholarly reconstruction, so at most 0.5 (CODING_GUIDE §3, scholarly-reconstruction ceiling)."
      rationale: "A separate, wise God who orders a world he did not create from nothing (co-eternal matter, time, place): 1. Alternative 0: a separate personal God who intervenes."
      alternatives:
        - {value: 0, note: "Personal intervening God.", cites: [{source: S1, locator: "§2"}]}
    B_cause:
      value: 3
      basis: scholarly_reconstruction
      certainty: 0.5
      cites: [{source: S1, locator: "§1; §5"}]
      how_known: "A scientist (P30: physician whose medical theory works within the Galenic framework of humours and natural powers; his alchemy describes 'a wide variety of chemical procedures' explained by atomist matter theory, S1), so working science gives B 3 at 0.5, alternative 4 (P35). Abū Ḥātim's report that he rejected the possibility of miracles points to 4 but is hostile and unverified (S1 §5)."
      rationale: "P35."
      alternatives:
        - {value: 4, note: "P35 alternative; Abū Ḥātim's report.", cites: [{source: S1, locator: "§5"}]}
    C_ledger: {value: UNKNOWN, how_known: "The Soul's liberation through reason is described, not a ledger (P19)."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "Leads toward 4 (reason suffices; critique of taqlīd) but reported by a hostile source and contested (S1 §5)."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Not scored from science alone (P19)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A 1 and B 3 at 0.5: both need 0.7 (P10)."}
  statements: []
  changes_over_life: []
  coder_notes: "No own-voice text read; everything rests on Adamson (scholarly-reconstruction ceiling, CODING_GUIDE §3). Span UNKNOWN; era filled from life dates (P39)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Persian (Rayy)", certainty: 0.5, cites: [{source: S1, locator: "§1 ('the Persian city of Rayy')"}], how_known: "SEP."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: UNKNOWN, how_known: "No lasting work is dated in the source read (P12, P29, P39)."}
  age_at_first_lasting_contribution: {value: UNKNOWN, how_known: "First-lasting year UNKNOWN (P12)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "Works undated."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "Works undated."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Works undated."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Wrote on mathematics and logic (S1); nothing on method.", certainty: 0.5, cites: [{source: S1, locator: "§1"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not stated."}
  circle_present: {value: "no", rationale: "God is one of five distinct eternals, not identified with nature (S1 §2).", certainty: 0.5, cites: [{source: S1, locator: "§2"}], how_known: "Coder's reading."}
  reading: "No circle."
  notes: ""

institutions:
  - {value: "Hospital in Rayy", role: "director (per biographers)", years: UNKNOWN, kind: other, certainty: 0.5, cites: [{source: S1, locator: "§1"}], how_known: "SEP: 'His biographers report'."}
  - {value: "Hospital in Baghdad", role: "director (per biographers)", years: UNKNOWN, kind: other, certainty: 0.5, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
collaborators:
  - {value: "Abū Ṣāliḥ al-Manṣūr", relation: "mentor or employer", note: "governor of Rayy, patron", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
  - {value: "Abū Ḥātim al-Rāzī", relation: "rival or critic", note: "Ismāʿīlī opponent, The Proofs of Prophecy", certainty: 0.7, cites: [{source: S1, locator: "§1; §5"}], how_known: "SEP."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 142"}], how_known: "Study roster."}
  controversies:
    - {value: "Whether he rejected prophecy and revelation", certainty: 0.7, cites: [{source: S1, locator: "§5"}], how_known: "SEP."}
  data_quality_flags:
    - "No own-voice text read."
  open_questions:
    - "Read Doubts about Galen §2.1 and the Spiritual Medicine in translation."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Peter Adamson"
    citation: "Adamson, Peter. \"Abu Bakr al-Razi.\" Stanford Encyclopedia of Philosophy (first published 2021; revised 14 May 2025). https://plato.stanford.edu/entries/abu-bakr-al-razi/"
    url: "https://plato.stanford.edu/entries/abu-bakr-al-razi/"
    accessed: 2026-10-19
    reliability_note: "Signed scholarly reference by the author of the standard monograph (Adamson 2021)."
    used_for: [identity, basics, contribution, worldview, heritage, lane_b, institutions, collaborators, review]
  - id: S2
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [review]
---

# Al-Razi

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Abū Bakr al-Rāzī (865–925), physician and philosopher of Rayy [S1]. Draft: primary_system BELOW_THRESHOLD; A 1 (0.5, alt 0); B 3 (0.5, alt 4); C UNKNOWN; D, E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Plotted (faded) at the next chart refresh.

## Life and work

Hospitals in Rayy and Baghdad [S1].

## Contribution and impact

Doubts about Galen; the Book for al-Manṣūr [S1].

## Childhood and education

Not recorded in the source read.

## Adult working worldview

Five eternals; God known from design; religion disputed [S1].

## Heritage (context only)

Persian [S1].

## Timing

UNKNOWN (works undated) [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No circle [S1].

## Open questions

- Own-voice reading.

## Research log

- 2026-10-19: Read SEP (Adamson) in full.
