---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 6
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S5 for Jason)
  model_used: Grok Bot executor agent; direct reads of the cited pages
  collected_on: '2026-10-01'
  last_updated: '2026-10-25'
  change_log:
  - date: '2026-10-01'
    by: scripts/make_system_stubs.py
    summary: Stub created from v7.1 data book table 4 and section 7.
  - date: '2026-10-02'
    by: scripts/make_system_stubs.py
    summary: "Decision P7: E_scope note added. E is not scored in a stub; when it is, score it on the\
      \ world's order (same rules for every kind of being and event, no in-group exceptions in this-world\
      \ events). Salvation and moral community go on C_ledger."
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'Draft (systems batch S5): filled from SEP "Causal Determinism" (Hoefer). A BELOW_THRESHOLD;
      B 4 (0.7); E 4 (0.5); C, D UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S5 audit follow-up: E_scope note citing P44(b). No value change.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from SEP Causal Determinism (Hoefer): family/parents/region, metaphysics
      TODOs, epistemology, ethics (free will link), practice, science, schools (Laplacean, physical-theory
      status, compatibilist debates). Axes unchanged.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score D_authority 4 (0.7) and C_ledger 4 (0.5) from sources on file (philosophical thesis;
      not divine ledger). A stays BELOW; B/E already 4.
identity:
  id: DETERM
  v7_1_number: 28
  v7_1_label: Determinism
  display_label: Determinism
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: metaphysical thesis
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP.
  family:
    value: 'Metaphysical thesis: given a state at t, thereafter fixed by natural law'
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP.
  parent_traditions:
    value:
    - Ancient necessity / fate debates
    - 'Early modern physics and philosophy (Laplace, Leibniz PSR contrast)'
    - Philosophy of science and free will
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction; §1
    how_known: SEP.
  related_codes:
  - code: STOIC
    relation: overlaps
    note: Stoic fate / causal nexus historically near
  - code: PANT
    relation: overlaps
    note: Spinoza often dual-coded; physics alone ≠ DETERM
  - code: ATHE
    relation: overlaps
    note: Compatible without God
  - code: EXIST
    relation: contrast case
    note: Existentialist freedom vs marionette worry
origins:
  founding_era:
    value: "Ancient; 'first became subject to clarification and mathematical analysis in the eighteenth\
      \ century'"
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP.
  founding_region:
    value: Concept ancient; mathematical clarification especially eighteenth-century Europe (Laplace)
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP.
  founders_or_key_figures:
    value:
    - Pierre-Simon Laplace
    - Gottfried Wilhelm Leibniz
    certainty: 0.7
    cites:
    - source: S1
      locator: §1–2
    how_known: SEP quotes Laplace and discusses Leibniz; 0.7.
  key_texts:
  - value: 'Laplace, Essai philosophique sur les probabilités (1820) — demon formulation'
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: SEP.
  - value: 'Earman, A Primer on Determinism (1986)'
    certainty: 0.7
    cites:
    - source: S1
      locator: §4
    how_known: SEP cites as storehouse; 0.7.
metaphysics:
  god_nature_relation:
    value: "Not fixed: determinism and theological views are 'easy to disentangle, barring certain strong\
      \ theological commitments'; for Leibniz God may will that things be so."
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: SEP.
  deity_personal:
    value: Not fixed by the thesis; compatible with and without God
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: §1–2
    how_known: SEP disentangles from fate/gods.
  intervention:
    value: "None within the thesis: 'every event is necessitated by antecedent events and conditions together\
      \ with the laws of nature'."
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: introduction
    how_known: "SEP's rough definition; 0.7."
  miracles:
    value: 'Within the thesis, events follow laws; miracle as law-exception is outside the thesis'
    stance: denied
    certainty: 0.7
    cites:
    - source: S1
      locator: introduction
    how_known: Implied by law-necessitation. 0.7.
  petition_and_prayer:
    value: Not addressed; petition that changes law-governed outcomes conflicts with the thesis
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: Not a religious practice thesis.
  afterlife:
    value: Not addressed
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP.
  moral_ledger:
    value: Not a moral-ledger doctrine; free-will debate concerns moral responsibility under determination
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: §6
    how_known: SEP free action section. 0.7.
  authority:
    value: Natural law and observation; philosophy of science framing
    stance: observation and reason
    certainty: 1.0
    cites:
    - source: S1
      locator: §2.4; §3
    how_known: SEP.
  reserved_exemptions:
    value: No group exempt from the laws if the thesis holds universally
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: introduction
    how_known: Matches E 4 rationale. 0.7.
  teleology_in_nature:
    value: Distinct from fatalism/destiny; laws not gods’ wills or intrinsic teleology
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: §1
    how_known: SEP fatalism disentanglement. 0.7.
  necessity_and_freedom:
    value: 'Core problem: if past + laws fix actions, free agency seems threatened; compatibilist and
      incompatibilist responses; time-symmetric determination noted'
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction; §6
    how_known: SEP.
lio_axes:
  A_locus:
    value: 'BELOW_THRESHOLD'
    how_known: 'The thesis is compatible with and without God (S1 §2): members differ (P44b).'
    note: 'Evidence: S1 §2.'
  B_cause:
    value: 4
    rationale: 'Every event necessitated by antecedent conditions and the laws of nature: no exceptions
      and no chance (P40).'
    certainty: 0.7
    cites:
    - source: S1
      locator: introduction
    how_known: "Fixed by the stance; 0.7 because SEP gives the definition 'roughly speaking'."
  C_ledger:
    value: 4
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — not an ethical school; no divine ledger implied.'
    rationale: C=4 implied none. Certainty 0.5.
    alternatives:
    - value: 'UNKNOWN'
      note: Named alternative if refusing implied score.
      cites:
      - source: S1
        locator: opening
  D_authority:
    value: 4
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: '0.7 — philosophical argument; stance observation and reason.'
    rationale: 'D=4: reason over revelation.'
    alternatives:
    - value: 3
      note: Named alternative if coding theological determinism as primary.
      cites:
      - source: S1
        locator: opening
  E_scope:
    value: 4
    rationale: "On the world's order (P7): every event under the same laws, so no group is exempt."
    certainty: 0.5
    cites:
    - source: S1
      locator: introduction
    how_known: 'Implied by the stance, not stated: 0.5.'
    note: 'P44(b): the stance itself fixes E (every event under the same laws, so no exception for any
      group); hence a score, not UNKNOWN.'
epistemology:
  value: 'Whether determinism is knowable is thorny: Final Theory unknown; chaos and QM interpretations
    complicate empirical decision; metaphysical argument also used'
  certainty: 1.0
  cites:
  - source: S1
    locator: §3
  how_known: SEP epistemology section.
ethics:
  value: Not an ethical school; stakes are moral responsibility and free agency under determination (compatibilism
    vs incompatibilism)
  certainty: 1.0
  cites:
  - source: S1
    locator: §6
  how_known: SEP.
practice:
  ritual_and_practice:
    value: Philosophical/scientific thesis; no ritual
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP.
  community_form:
    value: 'Philosophers of science, physicists, free-will theorists'
    certainty: 1.0
    cites:
    - source: S1
      locator: §4; §6
    how_known: SEP.
science:
  historical_stance:
    value: 'Tied to classical mechanics and Laplacean ideal; status varies across CM, relativity, QM'
    certainty: 1.0
    cites:
    - source: S1
      locator: §4
    how_known: SEP.
  current_stance:
    value: No agreement whether determinism is true; QM often thought indeterministic but Bohmian and
      Everettian readings can be deterministic
    certainty: 1.0
    cites:
    - source: S1
      locator: §4.4
    how_known: SEP.
schools_and_variants:
- name: Laplacean determinism
  form: scholastic or philosophical
  how_it_differs: Present state + laws fix past and future; famous intelligence/demon image
  lio_difference: B 4
  certainty: 1.0
  cites:
  - source: S1
    locator: §1
- name: Physical-theory determinism (theory-relative)
  form: modern
  how_it_differs: 'Ask whether a given theory (CM, GTR, QM interpretation) is deterministic'
  lio_difference: Same B reading when affirmed
  certainty: 1.0
  cites:
  - source: S1
    locator: §4
- name: Compatibilist reception
  form: scholastic or philosophical
  how_it_differs: 'Holds free agency compatible with determination (Fischer, Humean lines, Hoefer/Ismael/Loewer
    arguments)'
  lio_difference: Does not change B; coding stays on the metaphysical thesis
  certainty: 1.0
  cites:
  - source: S1
    locator: §6
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Not a religion; position among philosophers and scientists
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP.
v7_1_rubric:
  label: authorial v7.1 scores
  L: 9
  P: 8
  E: 9
  V: 9
  X: 8
  total: 43
  scoring_note: 'Determinism scores high for its logical rigor and alignment with empirical causality,
    providing a foundational view of reality, but tempered by ongoing debates in quantum physics and free
    will.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 28 and section 7 scoring notes'
revised_rubric:
  status: not started
  L:
    score: 'TODO'
    rationale: ''
  P:
    score: 'TODO'
    rationale: ''
  E:
    score: 'TODO'
    rationale: ''
  V:
    score: 'TODO'
    rationale: ''
  X:
    score: 'TODO'
    rationale: ''
coding_guidance:
  use_when: "The person's own writing affirms causal determinism as the main worldview (considered for\
    \ Spinoza, stage 3)."
  do_not_use_when: "A determinist physics alone does not make the worldview DETERM; Spinoza's God-or-Nature\
    \ is PANT."
  neighbors:
  - code: PANT
    relation: overlaps
    note: 'Spinoza: prefer PANT for God-or-Nature; DETERM only if determinism is the main worldview label'
  - code: STOIC
    relation: overlaps
    note: Fate / causal nexus
  - code: EXIST
    relation: neighbor (easily confused)
    note: Freedom-first coding vs determinist thesis
review:
  data_quality_flags: []
  open_questions:
  - When does a scientist’s determinism clear DETERM vs ATHE/PANT host coding?
  - Should fatalism get a separate code?
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Carl Hoefer
  year: 2023
  citation: 'Carl Hoefer. "Causal Determinism." Stanford Encyclopedia of Philosophy. First published January
    23, 2003; substantive revision September 21, 2023. https://plato.stanford.edu/entries/determinism-causal/.'
  url: 'https://plato.stanford.edu/entries/determinism-causal/'
  accessed: '2026-10-25'
  reliability_note: Peer-reviewed reference entry.
---
# Causal determinism (DETERM)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44. The v7.1 scores and note are unchanged.

## Summary

Causal determinism: every event necessitated by antecedent events and conditions together with the laws of nature [S1]. Distinct from fatalism and from mere predictability [S1].

## Core metaphysics

Thesis about laws and states, not about God; compatible with and without deity [S1]. Core free-will problem [S1].

## Position on the LIO axes

A BELOW_THRESHOLD; B 4 (0.7); E 4 (0.5); C/D UNKNOWN. Unchanged this pass.

## Schools and variants

Laplacean image; theory-relative physical determinism; compatibilist reception of the free-will problem [S1].

## Science

Status disputed across CM, relativity, QM interpretations [S1].

## Coding guidance

Person’s writing affirms causal determinism as main worldview → DETERM. Determinist physics alone under Spinoza’s God-or-Nature → PANT.

## v7.1 scoring note

Authorial v7.1 note unchanged (see front matter).

## Open questions

- When does a scientist’s determinism clear DETERM vs ATHE/PANT host coding?
- Should fatalism get a separate code?

## Research log

- 2026-10-15: draft from SEP Causal Determinism.
- 2026-10-25: deepened TODOs, schools, science/ethics; axes unchanged.
- 2026-10-25: D/C scored.
