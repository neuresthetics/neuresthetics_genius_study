---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 3
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S1 for Jason)
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
    summary: 'Draft (systems batch S1): filled from SEP ("Atheism and Agnosticism", §2) and Britannica (Nielsen, "Atheism"). A is BELOW_THRESHOLD (explicit suspension); B, C and E UNKNOWN; D 4 at 0.5. v7.1 scores and note unchanged. Not reviewed.'
identity:
  id: AGNOS
  v7_1_number: 2
  v7_1_label: Agnosticism
  display_label: Agnosticism
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: epistemic stance
    certainty: 0.7
    cites:
    - source: S1
      locator: §2
    how_known: SEP defines it as a principle or as the psychological state of being an agnostic; coder's classification, 0.7.
  family:
    value: Non-theism (suspension of judgement)
    certainty: 0.7
    cites:
    - source: S2
      locator: opening
    how_known: 'Britannica: agnosticism ''leaves open the question whether there is a god or not''. 0.7.'
  parent_traditions:
    value: UNKNOWN
    how_known: Not given in the sources read.
  related_codes:
  - code: ATHE
    relation: neighbor (easily confused)
  - code: SECHUM
    relation: neighbor (easily confused)
origins:
  founding_era:
    value: 'Late nineteenth century: the terms were ''famously coined in the late nineteenth century by the English biologist, T.H. Huxley''.'
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: SEP.
  founding_region:
    value: England
    certainty: 0.7
    cites:
    - source: S1
      locator: §2
    how_known: Where Huxley coined the term; coder's inference, 0.7.
  founders_or_key_figures:
    value:
    - T. H. Huxley
    - Leslie Stephen
    - Robin Le Poidevin
    certainty: 0.7
    cites:
    - source: S1
      locator: §2, §4
    - source: S2
      locator: '''Atheism and theism'''
    how_known: Huxley coined the term (SEP); Britannica names Huxley and Leslie Stephen as agnostics; Le Poidevin argues for agnosticism (SEP §4). 0.7.
  key_texts:
  - value: '"Agnosticism: A Symposium"'
    author: T. H. Huxley
    year: 1884
    certainty: 1.0
    cites:
    - source: S1
      locator: §2; Bibliography
    how_known: SEP quotes and cites it.
  - value: '"Agnosticism and Christianity"'
    author: T. H. Huxley
    year: 1889
    certainty: 1.0
    cites:
    - source: S1
      locator: §2; Bibliography
    how_known: SEP cites it.
metaphysics:
  god_nature_relation:
    value: 'Suspended: ''an agnostic is a person who has entertained the proposition that there is a God but believes neither that it is true nor that it is false''.'
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: SEP.
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
    value: 'Huxley''s principle: ''it is wrong to say that one knows or believes that a proposition is true without logically satisfactory evidence''; since neither theism nor atheism is adequately supported, one should suspend judgement.'
    stance: observation and reason
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: SEP paraphrase of Huxley 1884 and 1889.
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
    how_known: 'Explicit suspension on whether God exists (S1, §2), so no locus is held; as for persons (CODING_GUIDE §6, P20: an agnostic with no stated locus view is BELOW_THRESHOLD).'
    note: 'Evidence: the definition of agnosticism (S1 §2; S2 opening).'
  B_cause:
    value: UNKNOWN
    how_known: The sources read say nothing on law, miracle or exception as part of agnosticism.
  C_ledger:
    value: UNKNOWN
    how_known: Not addressed in the sources read.
  D_authority:
    value: 4
    rationale: Huxley's principle makes logically satisfactory evidence the condition for knowing or believing, which leaves no independent authority to revelation.
    certainty: 0.5
    cites:
    - source: S1
      locator: §2
    how_known: 0–4 scale (P1). SEP does not mention revelation; inferred, so 0.5.
  E_scope:
    value: UNKNOWN
    how_known: Not addressed in the sources read.
epistemology:
  value: Huxley's evidentialist principle, applied to theistic and atheistic belief (SEP); in the 'psychological' sense, the state of being an agnostic.
  certainty: 1.0
  cites:
  - source: S1
    locator: §2
  how_known: SEP.
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
schools_and_variants:
- name: Huxley's principled agnosticism
  form: scholastic or philosophical
  how_it_differs: A normative principle (weaker than evidentialism) rather than a belief state.
  lio_difference: D at 4 (0.5).
  certainty: 1.0
  cites:
  - source: S1
    locator: §2
- name: Modest agnosticism (Le Poidevin)
  form: scholastic or philosophical
  how_it_differs: Neither versatile theism nor global atheism is known to be true.
  lio_difference: None on the axes read.
  certainty: 1.0
  cites:
  - source: S1
    locator: §4
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: TODO
v7_1_rubric:
  label: authorial v7.1 scores
  L: 10
  P: 10
  E: 10
  V: 10
  X: 9
  total: 49
  scoring_note: Agnosticism promotes intellectual humility, scoring near-perfect for its evidence-based skepticism and avoidance of unsubstantiated commitments.
  source: v7.1 data book, section 6 table (tables[4]) row 2 and section 7 scoring notes
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
  use_when: 'v7.1 coding rule (Atheism vs Agnosticism): ATHE = positive naturalism. AGNOS = explicit suspension. SECHUM if the public identity is humanist movement rather than metaphysics.'
  do_not_use_when: 'A stated denial of God ("I do not believe in God") is ATHE or, for a self-described agnostic, A 4 at most 0.5 with BELOW_THRESHOLD as the alternative (P38). Positive naturalism: ATHE. Humanist public identity: SECHUM.'
  neighbors:
  - code: ATHE
    relation: neighbor (easily confused)
  - code: SECHUM
    relation: neighbor (easily confused)
review:
  data_quality_flags: []
  open_questions:
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Paul Draper
  year: 2022
  citation: Draper, Paul. "Atheism and Agnosticism." Stanford Encyclopedia of Philosophy. First published August 2, 2017; substantive revision March 22, 2022. https://plato.stanford.edu/entries/atheism-agnosticism/.
  url: https://plato.stanford.edu/entries/atheism-agnosticism/
  accessed: '2026-10-15'
  reliability_note: Peer-reviewed reference entry.
- id: S2
  type: tertiary
  kind: encyclopedia
  author: Kai E. Nielsen
  citation: Nielsen, Kai E. "Atheism." Encyclopaedia Britannica, updated 16 September 2026. https://www.britannica.com/topic/atheism.
  url: https://www.britannica.com/topic/atheism
  accessed: '2026-10-15'
  reliability_note: Signed reference article (with Britannica Editors). Article paragraphs only; the AI-generated Top Questions boxes were ignored.
---

# Agnosticism (AGNOS)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1). The v7.1 scores and note are unchanged.

## Summary

Agnosticism was coined by T. H. Huxley in the late nineteenth century [S1, §2]. An agnostic 'has entertained the proposition that there is a God but believes neither that it is true nor that it is false' [S1, §2]; Britannica: it 'leaves open the question whether there is a god or not' [S2, opening].

## Core metaphysics

Suspension on God [S1, §2].

## Position on the LIO axes

- A BELOW_THRESHOLD: explicit suspension (P20 logic) [S1].
- B, C, E UNKNOWN: not addressed.
- D 4 (0.5): Huxley's evidence principle [S1, §2].

## Schools and variants

Huxley's principle; Le Poidevin's modest agnosticism [S1, §2, §4].

## Science

TODO

## Coding guidance

AGNOS = explicit suspension (v7.1 rule). A stated disbelief is scored on A under P38.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> AGNOS (49/50) — Agnosticism. Agnosticism promotes intellectual humility, scoring near-perfect for its evidence-based skepticism and avoidance of unsubstantiated commitments.

## Open questions

- Adherents are TODO.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7 (score E on the world's order when the stub is filled).
- 2026-10-15 (systems batch S1): read the listed sources; quotations checked word for word against the fetched page text with a script. Britannica Top Questions boxes (AI-generated) not used.
