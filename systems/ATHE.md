---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 5
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S1 for Jason)
  model_used: Grok Bot executor agent; direct reads of the cited pages
  collected_on: 2026-10-01
  last_updated: '2026-10-15'
  change_log:
  - date: 2026-10-01
    by: scripts/make_system_stubs.py
    summary: Stub created from v7.1 data book table 4 and section 7.
  - date: 2026-10-01
    by: scripts/make_system_stubs.py
    summary: Coding guidance from the PANT boundary rules (OPEN_DECISIONS S6).
  - date: 2026-10-02
    by: scripts/make_system_stubs.py
    summary: 'Decision P7: E_scope note added. E is not scored in a stub; when it is, score it on the world''s order (same rules for every kind of being and event, no in-group exceptions in this-world events). Salvation and moral community go on C_ledger.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'Draft (systems batch S1): classification, origins, metaphysics, LIO axes (0–4, P1), epistemology, science, schools and coding guidance filled from Britannica (Nielsen, "Atheism") and SEP ("Atheism and Agnosticism", "Naturalism"). v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S1 audit: A cites P44(a); open question closed.'
identity:
  id: ATHE
  v7_1_number: 1
  v7_1_label: Atheism (naturalistic/materialistic – no gods + philosophical naturalism)
  display_label: Atheism (naturalistic/materialistic – no gods + philosophical naturalism)
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: metaphysical thesis
    certainty: 0.7
    cites:
    - source: S2
      locator: §1
    how_known: 'SEP: in philosophy ''atheism'' standardly names the proposition that God does not exist; a position, not an organised religion. Coder''s classification, 0.7.'
  family:
    value: Non-theism; in the v7.1 label, atheism joined to philosophical naturalism
    certainty: 0.7
    cites:
    - source: S2
      locator: §1
    - source: S3
      locator: introduction
    how_known: SEP notes that some writers identify atheism with a positive metaphysical theory like naturalism or materialism; the v7.1 label takes that form. 0.7.
  parent_traditions:
    value: UNKNOWN
    how_known: The sources read do not give a lineage for atheism as such.
  related_codes:
  - code: AGNOS
    relation: neighbor (easily confused)
    note: explicit suspension rather than positive naturalism
  - code: SECHUM
    relation: neighbor (easily confused)
    note: public identity is the humanist movement
  - code: PANT
    relation: neighbor (easily confused)
    note: shares the no-exemption stance; differs on the entity-term
origins:
  founding_era:
    value: UNKNOWN
    how_known: 'No founding date: Britannica treats atheism as a standing position, not a founded movement.'
  founding_region:
    value: UNKNOWN
    how_known: 'Not founded in one region (Britannica: atheism rejects the beliefs of African, classical, Hindu and Buddhist religions as well as the Abrahamic ones).'
  founders_or_key_figures:
    value:
    - Baron d'Holbach
    certainty: 0.7
    cites:
    - source: S1
      locator: '''Atheism and theism'''
    how_known: Britannica's example of an atheist; the list is not exhaustive, so 0.7.
  key_texts: []
metaphysics:
  god_nature_relation:
    value: 'No God or gods: ''atheism, in general, the critique and denial of metaphysical beliefs in God or spiritual beings''; on the v7.1 label, nature is all there is (''reality is exhausted by nature, containing nothing "supernatural"'').'
    stance: no God
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    - source: S3
      locator: introduction
    how_known: Britannica and SEP state it directly.
  deity_personal:
    value: 'No deity, personal or impersonal: atheism rejects all belief in "spiritual beings".'
    stance: no deity
    certainty: 1.0
    cites:
    - source: S1
      locator: '''Atheism as rejection of religious beliefs'''
    how_known: Britannica.
  intervention:
    value: None. Ontological naturalism holds that all physical effects have fully physical causes (causal closure).
    stance: none
    certainty: 0.7
    cites:
    - source: S3
      locator: §1.2
    how_known: SEP Naturalism; atheism alone does not entail it (SEP Atheism §1), the v7.1 label adds it, so 0.7.
  miracles:
    value: 'Denied on the naturalistic form: nothing supernatural.'
    stance: denied
    certainty: 0.7
    cites:
    - source: S3
      locator: introduction
    how_known: Follows from the naturalism in the v7.1 label; 0.7.
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
    value: 'Evidence: ''The empirical method, and the empirical method alone, such an atheist asserts, affords a reliable method for establishing what is in fact the case''; the fallibilist atheist stays open to evidence.'
    stance: observation and reason
    certainty: 0.7
    cites:
    - source: S1
      locator: '''Atheism and theism'''
    how_known: Britannica describes this as one form of atheist argument ('such an atheist'), so 0.7.
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
    value: 4
    rationale: 'No God outside or inside the world: the denial that God exists (SEP) and of all spiritual beings (Britannica). Scored at the LIO pole as for a person''s stated disbelief (P38 logic).'
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    - source: S2
      locator: §1
    how_known: 0–4 scale (P1). A 4 for a system with no God, under P44(a) (extends P38). 0.7.
  B_cause:
    value: 4
    rationale: 'Philosophical naturalism (in the v7.1 label): reality contains nothing supernatural, and all physical effects have fully physical causes, so no miracle, petition or exemption.'
    certainty: 0.7
    cites:
    - source: S3
      locator: introduction; §1.2
    how_known: '0–4 scale (P1). 0.7: minimal atheism (SEP §1) does not entail naturalism; the v7.1 label does.'
  C_ledger:
    value: 4
    rationale: 'No divine reward or punishment of persons: atheism rejects belief in God or spiritual beings who could keep one.'
    certainty: 0.5
    cites:
    - source: S1
      locator: '''Atheism as rejection of religious beliefs'''
    how_known: 0–4 scale (P1). Inferred from the denial, not stated in the sources, so 0.5.
  D_authority:
    value: 4
    rationale: 'Observation outranks revelation: ''The empirical method, and the empirical method alone ... affords a reliable method for establishing what is in fact the case''; claimed ''spiritual facts'' or ''transcendent facts'' ''have not been shown''.'
    certainty: 0.7
    cites:
    - source: S1
      locator: '''Atheism and theism'''
    how_known: 0–4 scale (P1). Britannica gives this as one atheist's argument, so 0.7.
  E_scope:
    value: 4
    rationale: 'Scored on the world''s order (P7): the same physical causes for every effect, and no supernatural agent to favour a group in events.'
    certainty: 0.5
    cites:
    - source: S3
      locator: §1.2
    how_known: 0–4 scale (P1). Inferred from causal closure, so 0.5.
epistemology:
  value: 'Evidence and the burden of proof: the theist ''needs to present the evidence''; the atheist should be ''a thorough and consistent fallibilist''.'
  certainty: 1.0
  cites:
  - source: S1
    locator: '''Atheism and theism'''
  how_known: Britannica.
ethics:
  value: UNKNOWN
  how_known: The sources read do not set out an atheist ethics.
practice:
  ritual_and_practice:
    value: TODO
  community_form:
    value: TODO
science:
  historical_stance:
    value: 'Ontological naturalism grew with science: the doctrine of the ''causal closure'' or ''causal completeness of the physical'', ''according to which all physical effects have fully physical causes'', became widely accepted.'
    certainty: 1.0
    cites:
    - source: S3
      locator: §1.2
    how_known: SEP Naturalism.
  current_stance:
    value: Most contemporary philosophers 'would both reject "supernatural" entities, and allow that science is a possible route ... to important truths'.
    certainty: 1.0
    cites:
    - source: S3
      locator: introduction
    how_known: SEP Naturalism.
schools_and_variants:
- name: Local and global atheism (Diller)
  form: scholastic or philosophical
  how_it_differs: Local atheism denies one sort of God; global atheism holds that there are no Gods of any sort.
  lio_difference: A at 4 only for global atheism; a local atheist may hold another God-concept.
  certainty: 1.0
  cites:
  - source: S2
    locator: §3
- name: Psychological (lack of belief) versus propositional atheism
  form: scholastic or philosophical
  how_it_differs: The psychological sense is 'lacking the belief that God exists'; in philosophy, atheism is the proposition that God does not exist.
  lio_difference: The lack-of-belief sense overlaps AGNOS; A may be BELOW_THRESHOLD.
  certainty: 1.0
  cites:
  - source: S2
    locator: §1
- name: Fallibilist atheism
  form: scholastic or philosophical
  how_it_differs: Denies God on present evidence while staying open to evidence, as against a priori atheism.
  lio_difference: Same axes; D at 4.
  certainty: 1.0
  cites:
  - source: S1
    locator: '''Atheism and theism'''
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
  X: 10
  total: 50
  scoring_note: Atheism achieves a perfect score as the most parsimonious system, fully embracing naturalism and science without unnecessary metaphysical additions, making it highly coherent and empirically robust.
  source: v7.1 data book, section 6 table (tables[4]) row 1 and section 7 scoring notes
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
  use_when: 'v7.1 coding rule (Atheism vs Agnosticism): ATHE = positive naturalism. AGNOS = explicit suspension. SECHUM if the public identity is humanist movement rather than metaphysics. v8 rule (decision S6, 2026-10-01): reverent language about nature that fails the two-part PANT test is ATHE (or SECHUM if the public identity is the humanist movement). See systems/PANT.md and docs/CODING_GUIDE.md section 5.'
  do_not_use_when: 'The person''s own writing identifies God or the divine with Nature as a whole and gives the whole a mark beyond feeling (unity, necessity or eternity, something mind-like, or value): PANT. Explicit suspension: AGNOS. Public identity is the humanist movement: SECHUM.'
  neighbors:
  - code: AGNOS
    relation: neighbor (easily confused)
  - code: SECHUM
    relation: neighbor (easily confused)
  - code: PANT
    relation: neighbor (easily confused)
review:
  data_quality_flags:
  - v7.1 table 4 label is truncated; v7_1_label is taken from the section 7 scoring note.
  - The v7.1 label joins atheism to philosophical naturalism; SEP (S2, §1) treats atheism as the denial of God, with naturalism a separate positive theory some writers identify with it. B, C and E are scored on the label's naturalistic form.
  open_questions:
  - Adherents are TODO.
  - Bare atheism (without naturalism) would leave B BELOW_THRESHOLD; a person coded ATHE keeps B from their own evidence.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Kai E. Nielsen
  citation: Nielsen, Kai E. "Atheism." Encyclopaedia Britannica, updated 16 September 2026. https://www.britannica.com/topic/atheism.
  url: https://www.britannica.com/topic/atheism
  accessed: '2026-10-15'
  reliability_note: Signed reference article (with Britannica Editors). Article paragraphs only; the AI-generated Top Questions boxes were ignored.
- id: S2
  type: tertiary
  kind: encyclopedia
  author: Paul Draper
  year: 2022
  citation: Draper, Paul. "Atheism and Agnosticism." Stanford Encyclopedia of Philosophy. First published August 2, 2017; substantive revision March 22, 2022. https://plato.stanford.edu/entries/atheism-agnosticism/.
  url: https://plato.stanford.edu/entries/atheism-agnosticism/
  accessed: '2026-10-15'
  reliability_note: Peer-reviewed reference entry.
- id: S3
  type: tertiary
  kind: encyclopedia
  author: David Papineau
  year: 2020
  citation: Papineau, David. "Naturalism." Stanford Encyclopedia of Philosophy. First published February 22, 2007; substantive revision March 31, 2020. https://plato.stanford.edu/entries/naturalism/.
  url: https://plato.stanford.edu/entries/naturalism/
  accessed: '2026-10-15'
  reliability_note: Peer-reviewed reference entry.
---

# Atheism (naturalistic/materialistic – no gods + philosophical naturalism) (ATHE)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1). The v7.1 scores and note are unchanged.

## Summary

Atheism is 'the critique and denial of metaphysical beliefs in God or spiritual beings' [S1, opening]. In philosophy the term standardly names 'the proposition that God does not exist' [S2, §1]. The v7.1 label adds philosophical naturalism: 'reality is exhausted by nature, containing nothing "supernatural"' [S3, introduction].

## Core metaphysics

No God or spiritual beings [S1]. On the naturalistic form, all physical effects have fully physical causes [S3, §1.2].

## Position on the LIO axes

- A 4 (0.7): no God [S1; S2, §1].
- B 4 (0.7): naturalism, causal closure [S3].
- C 4 (0.5): no divine ledger (inferred) [S1].
- D 4 (0.7): the empirical method alone [S1].
- E 4 (0.5): same causes everywhere (inferred) [S3].

## Schools and variants

Local versus global atheism [S2, §3]; psychological versus propositional atheism [S2, §1]; fallibilist versus a priori atheism [S1].

## Science

Naturalism's causal closure grew out of physics [S3, §1.2]; most philosophers now reject supernatural entities [S3].

## Coding guidance

Use ATHE for positive naturalism (v7.1 rule). Explicit suspension is AGNOS; a humanist public identity is SECHUM; reverent nature language that fails the PANT test is ATHE (S6).

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> ATHE (50/50) — Atheism (naturalistic/materialistic – no gods + philosophical naturalism). Atheism achieves a perfect score as the most parsimonious system, fully embracing naturalism and science without unnecessary metaphysical additions, making it highly coherent and empirically robust.

## Open questions

- A 4 ruled under P44(a).
- Adherents are TODO.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7 (score E on the world's order when the stub is filled).
- 2026-10-15 (systems batch S1): read the listed sources; quotations checked word for word against the fetched page text with a script. Britannica Top Questions boxes (AI-generated) not used.
- 2026-10-15 (S1 audit fixes, run 1: 5 HOLD, 2 WEAKEN): A under P44(a); note that a person coded ATHE keeps B from their own evidence (checked: Chandrasekhar, Hawking, Marx, Nietzsche, Turing all do).
