---
record:
  record_type: system
  schema_version: "1.1"
  record_version: 2
  review_status: stub
  collected_by: scripts/make_system_stubs.py
  model_used: none (ported from the v7.1 data book)
  collected_on: 2026-10-01
  last_updated: 2026-10-01
  change_log:
    - {date: 2026-10-01, by: scripts/make_system_stubs.py, summary: "Stub created from v7.1 data book table 4 and section 7."}
    - {date: 2026-10-01, by: scripts/make_system_stubs.py, summary: "Display label approved (OPEN_DECISIONS S1); CLASS_THEISM relation changed to 'neighbor (easily confused)' (S5)."}
identity:
  id: CLTHEI
  v7_1_number: 72
  v7_1_label: "Classical Theism (personal, interventionist Creator God)"
  display_label: "Interventionist personal theism"
  label_status: "approved"
  aliases: []
classification:
  kind: {value: TODO}
  family: {value: TODO}
  parent_traditions: {value: TODO}
  related_codes:
    - {code: CLASS_THEISM, relation: "neighbor (easily confused)", note: "v7.1 coding rule: CLTHEI is not CLASS_THEISM"}
    - {code: CHRIST, relation: "neighbor (easily confused)"}
    - {code: ISLAM, relation: "neighbor (easily confused)"}
    - {code: JUDA, relation: "neighbor (easily confused)"}
origins:
  founding_era: {value: TODO}
  founding_region: {value: TODO}
  founders_or_key_figures: {value: TODO}
  key_texts: []
metaphysics:
  god_nature_relation: {value: TODO, stance: TODO}
  deity_personal: {value: TODO, stance: TODO}
  intervention: {value: TODO, stance: TODO}
  miracles: {value: TODO, stance: TODO}
  petition_and_prayer: {value: TODO, stance: TODO}
  afterlife: {value: TODO, stance: TODO}
  moral_ledger: {value: TODO, stance: TODO}
  authority: {value: TODO, stance: TODO}
  reserved_exemptions: {value: TODO, stance: TODO}
  teleology_in_nature: {value: TODO, stance: TODO}
  necessity_and_freedom: {value: TODO}
lio_axes:
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
schools_and_variants: []
adherents:
  use: "context only — never a genius-rate denominator"
  estimate: {value: TODO}
v7_1_rubric:
  label: "authorial v7.1 scores"
  L: 7
  P: 5
  E: 3
  V: 3
  X: 2
  total: 20
  scoring_note: "Classical Theism scores low due to persistent logical paradoxes like the problem of evil and reliance on revelation over empirical evidence, though it provides a foundational framework for many Abrahamic religions."
  source: "v7.1 data book, section 6 table (tables[4]) row 72 and section 7 scoring notes"
revised_rubric:
  status: "not started"
  L: {score: TODO, rationale: ""}
  P: {score: TODO, rationale: ""}
  E: {score: TODO, rationale: ""}
  V: {score: TODO, rationale: ""}
  X: {score: TODO, rationale: ""}
coding_guidance:
  use_when: "v7.1 coding rule (Split theisms): CLASS_THEISM (Aristotelian-Thomistic-Falsafa) is not CLTHEI (popular interventionist personal God) and not generic CHRIST/ISLAM/JUDA."
  do_not_use_when: "TODO"
  neighbors:
    - {code: CLASS_THEISM, relation: "neighbor (easily confused)"}
    - {code: CHRIST, relation: "neighbor (easily confused)"}
    - {code: ISLAM, relation: "neighbor (easily confused)"}
    - {code: JUDA, relation: "neighbor (easily confused)"}
review:
  data_quality_flags:
    - "v7.1 used 'Classical Theism' for both CLASS_THEISM and CLTHEI. The display label keeps the code and separates the names (approved 2026-10-01, OPEN_DECISIONS S1)."
    - "v7.1 table 4 label is truncated; v7_1_label is taken from the section 7 scoring note."
  open_questions: []
sources: []
---

# Interventionist personal theism (CLTHEI)

> Stub. Only the v7.1 scores and scoring note are filled in, copied from the data book. Everything else is TODO. See `docs/RUNBOOK.md` (systems) for how to fill it in.

## Summary

TODO

## Core metaphysics

TODO

## Position on the LIO axes

TODO

## Schools and variants

TODO

## Science

TODO

## Coding guidance

TODO

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> CLTHEI (20/50) — Classical Theism (personal, interventionist Creator God). Classical Theism scores low due to persistent logical paradoxes like the problem of evil and reliance on revelation over empirical evidence, though it provides a foundational framework for many Abrahamic religions.

## Open questions

None yet.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
