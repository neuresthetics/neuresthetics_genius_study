---
# Person record template. Copy to people/<shard>/<id>.md (path from data/roster/person_ids.csv).
# Field meanings: docs/DATA_DICTIONARY.md. Coding rules: docs/CODING_GUIDE.md. Workflow: docs/RUNBOOK.md.
#
# Every factual field is a claim:  {value: ..., certainty: 1.0|0.7|0.5, cites: [{source: S1, locator: "p. 12"}], how_known: "..."}
# Unfilled:                        {value: TODO}
# Researched, nothing reliable:    {value: UNKNOWN, how_known: "checked S1, S2; neither gives it"}
# Evidence under certainty 0.5:    {value: BELOW_THRESHOLD, how_known: "...", note: "what the weak evidence is"}
# Competing sources:               fill value with the best-supported one, certainty 0.5, and list the rest under alternatives.
record:
  record_type: person
  schema_version: "1.1"
  record_version: 1
  review_status: "draft — unreviewed"     # stub | example — unreviewed | draft — unreviewed | in review | reviewed | needs revision; only a named human sets reviewed (P5)
  collected_by: TODO                      # person or agent that ran the collection
  model_used: TODO                        # e.g. "Claude Opus 4.x" or "none (human)"
  collected_on: 2026-01-01
  last_updated: 2026-01-01
  change_log:
    - {date: 2026-01-01, by: TODO, summary: "Record created."}

identity:
  id: family-given                        # replace with the id from data/roster/person_ids.csv; never invent one
  display_name: TODO
  roster:                                 # copy the roster.csv row exactly; the validator compares
    canonical_name: TODO
    rank: 1
    F: 1
    models: [Claude]
    band: TODO
    status: TODO
    field: TODO
    field_bucket: TODO
  full_name: {value: TODO}
  native_name: {value: TODO}              # name in the original script / language, if different
  aliases: []                             # - {name: "...", kind: "roster alias"}

basics:
  birth:
    date: {value: TODO}                   # "1791-09-22", "1791", or "-384" (= 384 BCE); add approx: true if "c."
    place: {value: TODO}                  # as the sources give it; modern_name / polity_then optional
  death:
    date: {value: TODO}
    place: {value: TODO}
  first_lasting_contribution_year: {value: TODO}
  era_bucket: {value: TODO}               # from first_lasting_contribution_year (P2); an edge year goes to the later bucket (1950 -> "1950 on")
  region_of_birth: {value: TODO}          # modern borders; look up the country in data/reference/regions.csv (P3)
  region_of_work: {value: TODO}
  sex_as_recorded: {value: TODO}          # as the sources record it; do not infer
  languages_of_work: {value: TODO}        # list
  occupations: {value: TODO}              # list

contribution:
  fields: {value: TODO}                   # list
  lasting_original_contributions: []      # - {value: "...", year: 1831, kind: discovery, lasting: "...", certainty: 1.0, cites: [...], how_known: "..."}
  evidence_of_impact: []                  # - {value: "...", kind: "named after them", ...}
  major_works: []                         # - {value: "Title", year: 1839, kind: book, ...}
  honours: []                             # - {value: "Copley Medal", year: 1832, ...}
  definition_fit: {value: TODO}           # clearly meets | arguable | does not meet  (+ rationale)

childhood:                                # birth to about 17; give ages where known
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
  parents_and_household: []               # - {value: "Father, James, a blacksmith", name: "James Faraday", role: father, ...}
  household_circumstances: {value: TODO}
  schooling: []                           # - {value: "...", stage: "dame or charity school", years: "...", ages: "...", ...}
  early_mathematics: {value: TODO}        # none known | arithmetic only | basic algebra | geometry (Euclid-style proof) | advanced mathematics | other
  early_geometric_style_reasoning: {value: TODO}   # definition-to-consequence practice before ~17 (Euclid, logic, disputation, catechism as proof ...)
  early_science_exposure: []              # - {value: "...", year: 1810, age: 19, ...}
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: TODO}
  notable_events: []

worldview:                                # the ADULT WORKING worldview (docs/CODING_GUIDE.md part 1)
  unit: "adult working worldview"
  working_years: {value: TODO}            # e.g. "1812–1862"
  nominal_affiliations: []                # church / community membership, offices held. Membership is not ideology.
  self_described_science_religion_relation: {value: TODO}
  primary_system: {value: TODO}           # a code in systems/; needs basis + certainty that match
  secondary_system: {value: TODO}         # only if they published in two systems; else value: UNKNOWN with how_known
  candidate_codes_considered: []          # - {code: CLTHEI, reason: "..."}
  lio_axes:                               # 0–4 scale (P1): 0 interventionist pole, 1 leans interventionist, 2 mixed, 3 leans LIO, 4 LIO pole
    A_locus: {value: TODO}
    B_cause: {value: TODO}
    C_ledger: {value: TODO}
    D_authority: {value: TODO}
    E_scope: {value: TODO}
  mid_basin: {value: TODO}                # P4 test: true if A_locus <= 1 and B_cause (in the work) >= 3, both certainty >= 0.7; see METHOD
  statements: []                          # verbatim quotes only; - {text: "...", cites: [...], date: "1844-10-24", kind: "private letter", verified_against: "primary transcription", verified_on: 2026-01-01}
  changes_over_life: []
  coder_notes: ""

heritage:                                 # context only. Never feeds an outcome table or a worldview code.
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: TODO}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: TODO}
  age_at_first_lasting_contribution: {value: TODO}
  first_evidence_of_lio_type_views: {value: TODO}
  lio_views_relative_to_major_work: {value: TODO}   # held from childhood | before major work | during major work | after major work | no LIO-type views found | unclear
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: TODO}   # yes | partly | no | unclear
  form_acquired: {value: TODO}            # childhood or adolescence | adulthood, before major work | through the profession | unclear
  circle_present: {value: TODO}           # yes | partly | no | unclear
  reading: ""
  notes: ""

institutions: []                          # - {value: "Royal Institution", role: "...", years: "...", kind: employer, ...}
collaborators: []                         # - {value: "Humphry Davy", roster_id: davy-humphry, relation: "mentor or employer", ...}

review:
  roster_status_reason: {value: TODO}
  controversies: []
  data_quality_flags: []
  open_questions: []

sources: []
# - id: S1
#   type: primary | secondary | tertiary
#   kind: letter | scholarly book | encyclopedia | ...
#   citation: "Full citation."
#   url: "https://..."
#   accessed: 2026-01-01
#   reliability_note: "..."
#   used_for: [basics, childhood]
---

# TODO display name

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

TODO: three to six sentences. Who, when, what lasting original contribution, and what is known about the working worldview.

## Life and work

TODO

## Contribution and impact

TODO

## Childhood and education

TODO

## Adult working worldview

TODO

## Heritage (context only)

TODO

## Timing

TODO

## Lane B notes (labeled belief model)

TODO. Everything in this section is Lane B: labeled belief, not a finding.

## Open questions

TODO

## Research log

- YYYY-MM-DD: what was searched, what was found, what was left TODO and why.
