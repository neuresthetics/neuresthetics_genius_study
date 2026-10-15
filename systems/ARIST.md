---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 3
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S2 for Jason)
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
    summary: 'Draft (systems batch S2): filled from SEP "Aristotle", "Aristotle''s Natural Philosophy" and "Aristotle''s Ethics". A 1 at 0.5; B BELOW_THRESHOLD (alt 3); C, D, E UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
identity:
  id: ARIST
  v7_1_number: 11
  v7_1_label: Aristotelianism
  display_label: Aristotelianism
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: philosophical school or method
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: 'SEP: the Lyceum; its members later called Peripatetics.'
  family:
    value: TODO
  parent_traditions:
    value: TODO
  related_codes: []
origins:
  founding_era:
    value: 4th century BCE (Aristotle, 384–322 BCE; Lyceum set up on his return to Athens in 335)
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: SEP.
  founding_region:
    value: Athens
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: SEP.
  founders_or_key_figures:
    value:
    - Aristotle
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: SEP.
  key_texts:
  - value: Physics
    author: Aristotle
    certainty: 1.0
    cites:
    - source: S2
      locator: introduction
    how_known: 'SEP: bk. 8 establishes the unmoved mover.'
  - value: Metaphysics
    author: Aristotle
    certainty: 1.0
    cites:
    - source: S1
      locator: §4
    - source: S2
      locator: introduction
    how_known: SEP.
  - value: Nicomachean Ethics
    author: Aristotle
    certainty: 1.0
    cites:
    - source: S3
      locator: §1
    how_known: SEP.
metaphysics:
  god_nature_relation:
    value: '''the unmoved mover of the universe, a supra-physical entity, without which the physical domain could not remain in existence''; ''the first and final cause of all motion''.'
    stance: creator distinct from creation
    certainty: 1.0
    cites:
    - source: S2
      locator: introduction
    - source: S1
      locator: §3
    how_known: SEP.
    note: '''creator distinct from creation'' is the nearest schema stance; SEP gives an eternal universe, not creation.'
  deity_personal:
    value: TODO
    stance: TODO
  intervention:
    value: TODO
    stance: TODO
  miracles:
    value: TODO
    stance: TODO
  petition_and_prayer:
    value: TODO
    stance: TODO
  afterlife:
    value: TODO
    stance: TODO
  moral_ledger:
    value: TODO
    stance: TODO
  authority:
    value: TODO
    stance: TODO
  reserved_exemptions:
    value: TODO
    stance: TODO
  teleology_in_nature:
    value: Nature is 'an inner principle of change and being at rest' (Physics 2.1); final causes are 'what these processes and entities are for'.
    stance: immanent ends
    certainty: 1.0
    cites:
    - source: S2
      locator: §1
    how_known: SEP.
  necessity_and_freedom:
    value: TODO
lio_axes:
  A_locus:
    value: 1
    rationale: A separate, supra-physical unmoved mover on which the physical domain depends; not a creator in time (an 'eternal chain of motions').
    certainty: 0.5
    cites:
    - source: S2
      locator: introduction
    how_known: 0–4 scale (P1). Transcendent is fixed by the stance; personhood is not addressed in the sources read, so 0.5 (alternative 2).
  B_cause:
    value: BELOW_THRESHOLD
    how_known: Natures are inner principles of change and the chain of motions is eternal (S2), but the sources read do not address exceptions or miracles.
    note: 'Alternative: 3. Evidence: S2 §1, §4.'
  C_ledger:
    value: UNKNOWN
    how_known: Not addressed in the sources read (S3 treats eudaimonia, not a divine ledger).
  D_authority:
    value: UNKNOWN
    how_known: Revelation not addressed in the sources read.
  E_scope:
    value: UNKNOWN
    how_known: Not addressed in the sources read.
epistemology:
  value: TODO
ethics:
  value: Eudaimonia ('happiness', 'flourishing') and aretê ('virtue', 'excellence').
  certainty: 1.0
  cites:
  - source: S3
    locator: §1
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
  X: 9
  total: 47
  scoring_note: Aristotelianism lays foundational empirical and logical groundwork, scoring high despite historical limitations.
  source: v7.1 data book, section 6 table (tables[4]) row 11 and section 7 scoring notes
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
  use_when: Aristotle (founders rule), or a person whose own writing adopts Aristotle's natures, four causes and unmoved mover without the Christian or Islamic creator.
  do_not_use_when: A posteriori arguments to the simple, immutable creator God (Aquinas, Falsafa) are CLASS_THEISM (P22).
  neighbors: []
review:
  data_quality_flags: []
  open_questions:
  - Personhood of the unmoved mover (SEP entry on Aristotle's theology not available; 404).
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Christopher Shields
  year: 2020
  citation: Shields, Christopher. "Aristotle." Stanford Encyclopedia of Philosophy. First published September 25, 2008; substantive revision August 25, 2020. https://plato.stanford.edu/entries/aristotle/.
  url: https://plato.stanford.edu/entries/aristotle/
  accessed: '2026-10-15'
  reliability_note: Peer-reviewed reference entry.
- id: S2
  type: tertiary
  kind: encyclopedia
  author: Istvan Bodnar
  year: 2023
  citation: Bodnar, Istvan. "Aristotle's Natural Philosophy." Stanford Encyclopedia of Philosophy. First published May 26, 2006; substantive revision April 24, 2023. https://plato.stanford.edu/entries/aristotle-natphil/.
  url: https://plato.stanford.edu/entries/aristotle-natphil/
  accessed: '2026-10-15'
  reliability_note: Peer-reviewed reference entry.
- id: S3
  type: tertiary
  kind: encyclopedia
  author: Richard Kraut
  year: 2026
  citation: Kraut, Richard. "Aristotle's Ethics." Stanford Encyclopedia of Philosophy. First published May 1, 2001; substantive revision August 11, 2026. https://plato.stanford.edu/entries/aristotle-ethics/.
  url: https://plato.stanford.edu/entries/aristotle-ethics/
  accessed: '2026-10-15'
  reliability_note: Peer-reviewed reference entry.
---

# Aristotelianism (ARIST)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1). The v7.1 scores and note are unchanged.

## Summary

Aristotelianism is the school of Aristotle (384–322 BCE), whose Lyceum members 'later came to be called Peripatetics' [S1]. Aristotle's Physics 'establishes in bk. 8 the existence of the unmoved mover of the universe, a supra-physical entity' [S2].

## Core metaphysics

Nature is 'an inner principle of change and being at rest' [S2, §1]; an eternal chain of motions dependent on an unmoved mover [S2].

## Position on the LIO axes

- A 1 (0.5, alt 2) [S2].
- B BELOW_THRESHOLD (alt 3).
- C, D, E UNKNOWN.

## Schools and variants

TODO

## Science

Physics 'tends in Aristotle’s hands to concentrate on conceptual puzzles pertaining to nature rather than on empirical research' [S1].

## Coding guidance

Aristotle by the founders rule; Thomists are CLASS_THEISM.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> ARIST (47/50) — Aristotelianism. Aristotelianism lays foundational empirical and logical groundwork, scoring high despite historical limitations.

## Open questions

- Personhood of the unmoved mover.
- Adherents are TODO.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7 (score E on the world's order when the stub is filled).
- 2026-10-15 (systems batch S2): read the listed sources; quotations checked against the fetched page text. Axes follow P44(b): a value only where the stance itself fixes it; UNKNOWN where the source is silent; BELOW_THRESHOLD where members differ.
