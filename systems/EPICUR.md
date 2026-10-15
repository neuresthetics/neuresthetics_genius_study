---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 4
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S3 for Jason)
  model_used: Grok Bot executor agent; direct reads of the cited pages
  collected_on: 2026-10-01
  last_updated: '2026-10-15'
  change_log:
  - date: 2026-10-01
    by: scripts/make_system_stubs.py
    summary: Stub created from v7.1 data book table 4 and section 7.
  - date: 2026-10-02
    by: scripts/make_system_stubs.py
    summary: 'Decision P7: E_scope note added. E is not scored in a stub; when it is, score it on the world''s order (same rules for every kind of being and event, no in-group exceptions in this-world events). Salvation and moral community go on C_ledger.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'Draft (systems batch S3): filled from SEP "Epicurus" (Konstan). A 3 (0.5, alt 4), B 3 (0.5), C 4 (0.7), D 4 (0.7), E 4 (0.5). v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S3 audit (WEAKEN #3b): the swerve is Epicurus'' doctrine (known chiefly through Lucretius and Cicero); B alternative 4 named; A reasoning noted. Values unchanged.'
identity:
  id: EPICUR
  v7_1_number: 16
  v7_1_label: Epicureanism
  display_label: Epicureanism
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: philosophical school or method
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: '''a complete and interdependent system''.'
  family:
    value: TODO
  parent_traditions:
    value: TODO
  related_codes: []
origins:
  founding_era:
    value: Hellenistic; Epicurus 341–270 BCE
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP.
  founding_region:
    value: TODO
  founders_or_key_figures:
    value:
    - Epicurus
    - Lucretius
    certainty: 1.0
    cites:
    - source: S1
      locator: §1, §3
    how_known: SEP.
  key_texts: []
metaphysics:
  god_nature_relation:
    value: Gods exist, 'immortal and indestructible', within an atomistic materialist universe; 'do not imagine that they concern themselves about human beings and their behavior'.
    stance: many gods within nature
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction; §4
    how_known: SEP.
  deity_personal:
    value: TODO
    stance: TODO
  intervention:
    value: 'None: the gods do not concern themselves about human beings.'
    stance: none
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP.
  miracles:
    value: TODO
    stance: TODO
  petition_and_prayer:
    value: TODO
    stance: TODO
  afterlife:
    value: 'None: radical materialism disproves ''the possibility of the soul’s survival after death, and hence the prospect of punishment in the afterlife''.'
    stance: none
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP.
  moral_ledger:
    value: TODO
    stance: TODO
  authority:
    value: 'Empiricist: ''sensations, together with the perception of pleasure and pain, are infallible criteria''.'
    stance: observation and reason
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP.
  reserved_exemptions:
    value: TODO
    stance: TODO
  teleology_in_nature:
    value: TODO
    stance: TODO
  necessity_and_freedom:
    value: TODO
lio_axes:
  A_locus:
    value: 3
    rationale: 'Gods exist inside a materialist universe and do not concern themselves with humans: no transcendent person.'
    certainty: 0.5
    cites:
    - source: S1
      locator: introduction; §4
    how_known: 0.5, alternative 4. The gods exist as material beings inside the cosmos, so P44(a) (no God gives 4) does not apply; divine beings located within nature fit 3. Their indifference bears on C and E (both 4), not on locus (S3 audit RQ1).
    alternatives:
    - value: 4
      note: If material gods within nature are read as the immanent pole.
      cites:
      - source: S1
        locator: introduction
  B_cause:
    value: 3
    rationale: No divine intervention and a naturalistic account of nature, but the swerve, Epicurus' doctrine of uncaused atomic deviation (attested chiefly in later sources, including Lucretius and Cicero), is chance within nature, so not exceptionless law (P40).
    certainty: 0.5
    cites:
    - source: S1
      locator: introduction; §3
    how_known: '0.5: the swerve is Epicurus'' doctrine, known chiefly through Lucretius and Cicero (S1); its reading as a bar to B 4 is the coder''s (P40: 4 only where exceptions and chance are both ruled out). Alternative 4.'
    alternatives:
    - value: 4
      note: If the swerve is read as natural indeterminacy compatible with B 4.
      cites:
      - source: S1
        locator: §3
  C_ledger:
    value: 4
    rationale: No afterlife punishment and gods indifferent to human behaviour.
    certainty: 0.7
    cites:
    - source: S1
      locator: introduction
    how_known: Stated by the system (P44c), 0.7.
  D_authority:
    value: 4
    rationale: Sensations are infallible criteria; empiricist theory of knowledge.
    certainty: 0.7
    cites:
    - source: S1
      locator: introduction
    how_known: Stated; revelation not discussed, 0.7.
  E_scope:
    value: 4
    rationale: 'On the world''s order (P7): indifferent gods favour no group.'
    certainty: 0.5
    cites:
    - source: S1
      locator: introduction
    how_known: Implied by the stance (P44c), 0.5.
epistemology:
  value: TODO
ethics:
  value: The goal is 'happiness, resulting from absence of physical pain and mental disturbance'.
  certainty: 1.0
  cites:
  - source: S1
    locator: introduction
  how_known: SEP.
practice:
  ritual_and_practice:
    value: TODO
  community_form:
    value: TODO
science:
  historical_stance:
    value: TODO
  current_stance:
    value: TODO
schools_and_variants: []
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: TODO
v7_1_rubric:
  label: authorial v7.1 scores
  L: 9
  P: 9
  E: 10
  V: 10
  X: 8
  total: 46
  scoring_note: Epicureanism balances pleasure with reason, scoring high for its empirical roots in atomism and ethics.
  source: v7.1 data book, section 6 table (tables[4]) row 16 and section 7 scoring notes
revised_rubric:
  status: not started
  L:
    score: TODO
    rationale: ''
  P:
    score: TODO
    rationale: ''
  E:
    score: TODO
    rationale: ''
  V:
    score: TODO
    rationale: ''
  X:
    score: TODO
    rationale: ''
coding_guidance:
  use_when: The person's own writing adopts Epicurean atomism and its ethics of tranquillity.
  do_not_use_when: Popular "epicure" (pleasure-seeking) is not EPICUR. Atomism alone, without the ethics, is not enough.
  neighbors: []
review:
  data_quality_flags: []
  open_questions:
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: David Konstan
  year: 2022
  citation: David Konstan. "Epicurus." Stanford Encyclopedia of Philosophy. First published January 10, 2005; substantive revision July 8, 2022. https://plato.stanford.edu/entries/epicurus/.
  url: https://plato.stanford.edu/entries/epicurus/
  accessed: '2026-10-15'
  reliability_note: Peer-reviewed reference entry.
---

# Epicureanism (EPICUR)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44. The v7.1 scores and note are unchanged.

## Summary

Epicurus (341–270 BCE) taught 'a complete and interdependent system': happiness as absence of pain and disturbance, an empiricist theory of knowledge, 'atomistic materialism', and a naturalistic account of evolution [S1].

## Core metaphysics

Atoms and void; gods immortal but unconcerned with humans; no survival after death [S1].

## Position on the LIO axes

- A 3 (0.5, alt 4), B 3 (0.5).
- C 4 (0.7), D 4 (0.7), E 4 (0.5).

## Schools and variants

TODO

## Science

Atomism; Epicurus' swerve, known chiefly through Lucretius and Cicero [S1, §3].

## Coding guidance

Ancient and later avowed Epicureans.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> EPICUR (46/50) — Epicureanism. Epicureanism balances pleasure with reason, scoring high for its empirical roots in atomism and ethics.

## Open questions

- Adherents are TODO.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7 (score E on the world's order when the stub is filled).
- 2026-10-15 (systems batch S3): read the listed sources; quotations checked word for word against the fetched page text with a script. Axes under P44.
- 2026-10-15 (S3 audit fixes, run 1: 10 HOLD, 1 WEAKEN): swerve attributed to Epicurus (via Lucretius and Cicero); B alt 4 named; A reasoning noted.
