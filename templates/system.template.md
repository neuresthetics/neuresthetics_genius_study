---
# Belief-system record template. The 77 v7.1 systems already have files in systems/ (stubs made by
# scripts/make_system_stubs.py). Fill those in; use this template only to see every field in one place.
# Field meanings: docs/DATA_DICTIONARY.md part 3. Coding rules: docs/CODING_GUIDE.md part 2. Workflow: docs/RUNBOOK.md part 2.
# Claim form is the same as person files: {value, certainty, cites: [{source, locator}], how_known}; TODO / UNKNOWN / BELOW_THRESHOLD.
record:
  record_type: system
  schema_version: "1.0"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: TODO
  model_used: TODO
  collected_on: 2026-01-01
  last_updated: 2026-01-01
  change_log:
    - {date: 2026-01-01, by: TODO, summary: "Record created."}
identity:
  id: CODE                                # the v7.1 abbr code; never rename
  v7_1_number: 1                          # row number in data book table 4
  v7_1_label: "Label exactly as in the v7.1 data book"
  display_label: "Label used in v8 tables"
  label_status: "as in v7.1"              # as in v7.1 | proposed — pending Jason's OK | approved
  aliases: []
classification:
  kind: {value: TODO}                     # religion | philosophical school or method | metaphysical thesis | ethical or civic movement | epistemic stance | esoteric or occult tradition | new religious movement | indigenous or traditional religion | reconstructionist religion | family of positions
  family: {value: TODO}                   # e.g. "monism", "Abrahamic", "Hellenistic philosophy"
  parent_traditions: {value: TODO}        # list
  related_codes: []                       # - {code: ATHE, relation: "neighbor (easily confused)", note: "..."}
origins:
  founding_era: {value: TODO}
  founding_region: {value: TODO}
  founders_or_key_figures: {value: TODO}  # list
  key_texts: []                           # - {value: "Ethics", author: "Spinoza", year: 1677, certainty: 1.0, cites: [...], how_known: "..."}
metaphysics:                              # each: value = the position in 1–3 sentences; stance = short label from the schema list
  god_nature_relation: {value: TODO, stance: TODO}
  deity_personal: {value: TODO, stance: TODO}
  intervention: {value: TODO, stance: TODO}
  miracles: {value: TODO, stance: TODO}
  petition_and_prayer: {value: TODO, stance: TODO}
  afterlife: {value: TODO, stance: TODO}
  moral_ledger: {value: TODO, stance: TODO}
  authority: {value: TODO, stance: TODO}  # revelation vs observation
  reserved_exemptions: {value: TODO, stance: TODO}
  teleology_in_nature: {value: TODO, stance: TODO}
  necessity_and_freedom: {value: TODO}
lio_axes:                                 # PROPOSED 0–4 per axis, with rationale; score the official or scholarly form
  A_locus: {value: TODO}
  B_cause: {value: TODO}
  C_ledger: {value: TODO}
  D_authority: {value: TODO}
  E_scope: {value: TODO}
epistemology: {value: TODO}
ethics: {value: TODO}
practice:
  ritual_and_practice: {value: TODO}
  community_form: {value: TODO}
science:
  historical_stance: {value: TODO}
  current_stance: {value: TODO}
schools_and_variants: []                  # - {name: "...", code: CLTHEI, form: popular, how_it_differs: "...", lio_difference: "...", certainty: 0.7, cites: [...]}
adherents:
  use: "context only — never a genius-rate denominator"
  estimate: {value: TODO}                 # with year and scope
v7_1_rubric:                              # copied by make_system_stubs.py; validator compares with the data book
  label: "authorial v7.1 scores"
  L: 0
  P: 0
  E: 0
  V: 0
  X: 0
  total: 0
  scoring_note: "verbatim from data book section 7"
  source: "v7.1 data book, section 6 table (tables[4]) row N and section 7 scoring notes"
revised_rubric:
  status: "not started"                   # not started | draft | reviewed
  L: {score: TODO, rationale: ""}
  P: {score: TODO, rationale: ""}
  E: {score: TODO, rationale: ""}
  V: {score: TODO, rationale: ""}
  X: {score: TODO, rationale: ""}
coding_guidance:
  use_when: "TODO"
  do_not_use_when: "TODO"
  neighbors: []
review:
  data_quality_flags: []
  open_questions: []
sources: []
---

# Display label (CODE)

## Summary

## Core metaphysics

## Position on the LIO axes

## Schools and variants

## Science

## Coding guidance

## v7.1 scoring note

## Open questions

## Research log
