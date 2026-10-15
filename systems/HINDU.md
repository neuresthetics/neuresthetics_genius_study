---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 3
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S8 for Jason)
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
    summary: 'Draft (systems batch S8): filled from Britannica "Hinduism" (Narayanan) and IEP "Hindu Philosophy" (Ranganathan). A, D BELOW_THRESHOLD; C 3 (0.5, alt 4, P44(d)); B, E UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
identity:
  id: HINDU
  v7_1_number: 47
  v7_1_label: Hinduism (Sanatana Dharma)
  display_label: Hinduism (Sanatana Dharma)
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: religion
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: Britannica.
  family:
    value: TODO
  parent_traditions:
    value: TODO
  related_codes: []
origins:
  founding_era:
    value: Texts and practices from the 2nd millennium BCE or earlier
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: Britannica.
  founding_region:
    value: Indian subcontinent
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: Britannica.
  founders_or_key_figures:
    value: TODO
  key_texts: []
metaphysics:
  god_nature_relation:
    value: TODO
    stance: TODO
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
    value: karma 'denotes the moral, psychological spiritual and physical causal consequences of morally significant past choices'.
    stance: karma-type law
    certainty: 1.0
    cites:
    - source: S2
      locator: §1.a.i
    how_known: IEP.
  authority:
    value: TODO
    stance: TODO
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
    value: BELOW_THRESHOLD
    how_known: 'Members differ: ''it is not true that all Hindus are polytheists''; Vaiṣṇava and Śaiva traditions hold one deity is genuinely God (S2), and Sāṅkhya explains the cosmos by Prakṛti and Puruṣa (S2).'
    note: P44(b).
  B_cause:
    value: UNKNOWN
    how_known: Not addressed in the sources read.
  C_ledger:
    value: 3
    rationale: 'Karma: causal consequences of morally significant past choices.'
    certainty: 0.5
    cites: &id001
    - source: S2
      locator: §1.a.i
    how_known: 'Karma rule (P44(d)): an impersonal moral ledger is C 3 @0.5, alternative 4. Theistic schools may add a divine overseer (alternative not scored).'
    alternatives:
    - value: 4
      note: Named alternative.
      cites: *id001
  D_authority:
    value: BELOW_THRESHOLD
    how_known: Hindu philosophy shares 'a textual connection to certain core Hindu religious texts (the Vedas)', but Sāṅkhya 'does not explicitly attempt to align itself with the authority of the Vedas' (S2).
    note: 'Alternative: 1.'
    alternatives:
    - value: 1
      note: Named alternative.
      cites:
      - source: S2
        locator: §1.b; Sāṅkhya
  E_scope:
    value: UNKNOWN
    how_known: Not addressed in the sources read.
epistemology:
  value: TODO
ethics:
  value: TODO
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
  L: 8
  P: 7
  E: 5
  V: 5
  X: 3
  total: 28
  scoring_note: Hinduism scores moderately due to its profound philosophical depth and ethical systems, accommodating diverse paths to enlightenment, but limited by supernatural claims and scriptural authority over empirical evidence.
  source: v7.1 data book, section 6 table (tables[4]) row 47 and section 7 scoring notes
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
  use_when: The person self-identifies as Hindu or adopts a Hindu school as their framework.
  do_not_use_when: Indian birth alone is not HINDU; yoga practice alone is not enough.
  neighbors: []
review:
  data_quality_flags: []
  open_questions:
  - Per-school variants (Vedānta, Vaiṣṇava, Śaiva) not filled.
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Vasudha Narayanan; Britannica Editors
  citation: Narayanan, Vasudha, and Britannica Editors. "Hinduism." Encyclopaedia Britannica. https://www.britannica.com/topic/Hinduism.
  url: https://www.britannica.com/topic/Hinduism
  accessed: '2026-10-15'
  reliability_note: Signed article; introduction and "The term Hinduism" read. Read in its Wayback Machine copy (snapshot 2026-10-07); the live page timed out.
- id: S2
  type: tertiary
  kind: encyclopedia
  author: Shyam Ranganathan
  citation: Ranganathan, Shyam. "Hindu Philosophy." Internet Encyclopedia of Philosophy. https://iep.utm.edu/hindu-ph/.
  url: https://iep.utm.edu/hindu-ph/
  accessed: '2026-10-15'
  reliability_note: Peer-reviewed; undated page.
---

# Hinduism (Sanatana Dharma) (HINDU)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

Hinduism: 'major world religion originating on the Indian subcontinent and comprising several and varied systems of philosophy, belief, and ritual' [S1]. No 'shared, comprehensive doctrine' identifies it [S2].

## Core metaphysics

Varied; karma common but not unique [S2].

## Position on the LIO axes

- A, D BELOW_THRESHOLD.
- C 3 (0.5, alt 4; P44(d)).
- B, E UNKNOWN.

## Schools and variants

TODO

## Science

TODO

## Coding guidance

Self-identified Hindus.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> HINDU (28/50) — Hinduism (Sanatana Dharma). Hinduism scores moderately due to its profound philosophical depth and ethical systems, accommodating diverse paths to enlightenment, but limited by supernatural claims and scriptural authority over empirical evidence.

## Open questions

- School variants.
- Adherents are TODO.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7 (score E on the world's order when the stub is filled).
- 2026-10-15 (systems batch S8): read the listed sources; quotations checked word for word against the fetched page text. Britannica pages read in full Wayback Machine copies (live site times out); AI Top Questions not used.
