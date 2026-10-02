---
record:
  record_type: system
  schema_version: "1.1"
  record_version: 3
  review_status: stub
  collected_by: scripts/make_system_stubs.py
  model_used: none (ported from the v7.1 data book)
  collected_on: 2026-10-01
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-01, by: scripts/make_system_stubs.py, summary: "Stub created from v7.1 data book table 4 and section 7."}
    - {date: 2026-10-01, by: scripts/make_system_stubs.py, summary: "Coding guidance from the PANT boundary rules (OPEN_DECISIONS S6)."}
    - {date: 2026-10-02, by: scripts/make_system_stubs.py, summary: "Decision P7: E_scope note added. E is not scored in a stub; when it is, score it on the world's order (same rules for every kind of being and event, no in-group exceptions in this-world events). Salvation and moral community go on C_ledger."}
identity:
  id: ATHE
  v7_1_number: 1
  v7_1_label: "Atheism (naturalistic/materialistic – no gods + philosophical naturalism)"
  display_label: "Atheism (naturalistic/materialistic – no gods + philosophical naturalism)"
  label_status: "as in v7.1"
  aliases: []
classification:
  kind: {value: TODO}
  family: {value: TODO}
  parent_traditions: {value: TODO}
  related_codes:
    - {code: AGNOS, relation: "neighbor (easily confused)", note: "explicit suspension rather than positive naturalism"}
    - {code: SECHUM, relation: "neighbor (easily confused)", note: "public identity is the humanist movement"}
    - {code: PANT, relation: "neighbor (easily confused)", note: "shares the no-exemption stance; differs on the entity-term"}
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
  E_scope: {value: TODO, note: "Not scored (stub). When filled, score on the world's order (decision P7, 2026-10-02): the same rules for every kind of being and event, and no in-group exceptions in this-world events (fortune, protection, answered petition, miracles for the favoured). Salvation, reward and punishment, and moral community go on C_ledger. The v7.1 rubric's E column (direct empirical compatibility) is a different axis; the v7.1 scoring note below may mix domains, so recheck it against this rule."}
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
  L: 10
  P: 10
  E: 10
  V: 10
  X: 10
  total: 50
  scoring_note: "Atheism achieves a perfect score as the most parsimonious system, fully embracing naturalism and science without unnecessary metaphysical additions, making it highly coherent and empirically robust."
  source: "v7.1 data book, section 6 table (tables[4]) row 1 and section 7 scoring notes"
revised_rubric:
  status: "not started"
  L: {score: TODO, rationale: ""}
  P: {score: TODO, rationale: ""}
  E: {score: TODO, rationale: ""}
  V: {score: TODO, rationale: ""}
  X: {score: TODO, rationale: ""}
coding_guidance:
  use_when: "v7.1 coding rule (Atheism vs Agnosticism): ATHE = positive naturalism. AGNOS = explicit suspension. SECHUM if the public identity is humanist movement rather than metaphysics. v8 rule (decision S6, 2026-10-01): reverent language about nature that fails the two-part PANT test is ATHE (or SECHUM if the public identity is the humanist movement). See systems/PANT.md and docs/CODING_GUIDE.md section 5."
  do_not_use_when: "The person's own writing identifies God or the divine with Nature as a whole and gives the whole a mark beyond feeling (unity, necessity or eternity, something mind-like, or value): PANT. Explicit suspension: AGNOS. Public identity is the humanist movement: SECHUM."
  neighbors:
    - {code: AGNOS, relation: "neighbor (easily confused)"}
    - {code: SECHUM, relation: "neighbor (easily confused)"}
    - {code: PANT, relation: "neighbor (easily confused)"}
review:
  data_quality_flags:
    - "v7.1 table 4 label is truncated; v7_1_label is taken from the section 7 scoring note."
  open_questions: []
sources: []
---

# Atheism (naturalistic/materialistic – no gods + philosophical naturalism) (ATHE)

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

> ATHE (50/50) — Atheism (naturalistic/materialistic – no gods + philosophical naturalism). Atheism achieves a perfect score as the most parsimonious system, fully embracing naturalism and science without unnecessary metaphysical additions, making it highly coherent and empirically robust.

## Open questions

None yet.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7 (score E on the world's order when the stub is filled).
