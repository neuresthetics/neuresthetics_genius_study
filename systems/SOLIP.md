---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 6
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S6 for Jason)
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
    summary: 'Draft (systems batch S6): filled from IEP "Solipsism and the Problem of Other Minds" (Thornton).
      All axes UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities: family, parents, related codes, founders, remaining metaphysics (not addressed
      / none), epistemology, ethics, practice, science, schools. Axes stay UNKNOWN (mind thesis, not God
      cosmology; P44). Source: IEP Thornton.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Fill adherents/estimate gloss from existing sources (order-of-magnitude / qualitative). Axes
      unchanged.
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score A_locus 4 (0.7) and D_authority 4 (0.7) from IEP Solipsism (epistemic thesis; observation
      and reason). B/C/E UNKNOWN.
identity:
  id: SOLIP
  v7_1_number: 38
  v7_1_label: Solipsism
  display_label: Solipsism
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: metaphysical thesis
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: IEP.
  family:
    value: 'Metaphysical and epistemic thesis that existence, for the subject, is exhausted by their own
      mental states; typically treated as a problem to refute rather than a school with adherents'
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction; §1
    how_known: 'IEP: no great philosopher has espoused it; doctrine that existence means my existence
      and my mental states.'
  parent_traditions:
    value:
    - Cartesian egocentric epistemology
    - "British empiricism (Locke) on acquiring psychological concepts from one's own case"
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: IEP historical origins.
  related_codes:
  - code: IDEAL
    relation: neighbor (easily confused)
    note: idealism about mind/matter is not the claim that only one mind exists
  - code: PHENOM
    relation: contrast case
    note: 'phenomenological bracketing is methodological, not solipsism'
  - code: SCEPT
    relation: overlaps
    note: methodic doubt can raise the specter; Descartes escapes via God
  - code: EXIST
    relation: neighbor (easily confused)
    note: existential first-person themes are not SOLIP
origins:
  founding_era:
    value: "Problem crystallizes after Descartes' methodic doubt; discussed through modern empiricism\
      \ and Wittgenstein"
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: IEP.
  founding_region:
    value: 'Early modern European philosophy (France, Britain); later analytic critique (Wittgenstein)'
    certainty: 0.7
    cites:
    - source: S1
      locator: §2; §7
    how_known: "Coder's geographic gloss on IEP cast."
  founders_or_key_figures:
    value:
    - René Descartes (backdrop; escapes via God)
    - John Locke (own-case psychology)
    - Ludwig Wittgenstein (critique)
    - Norman Malcolm
    - P. F. Strawson
    certainty: 1.0
    cites:
    - source: S1
      locator: §2; §5; §7
    how_known: IEP; none is an adherent solipsist.
  key_texts:
  - value: Meditations on First Philosophy (backdrop)
    author: René Descartes
    year: 1641
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: IEP.
  - value: Philosophical Investigations (critique)
    author: Ludwig Wittgenstein
    year: 1953
    certainty: 1.0
    cites:
    - source: S1
      locator: §4; §7
    how_known: IEP.
metaphysics:
  god_nature_relation:
    value: "Not addressed; Descartes escapes solipsism 'by the desperate expedient of appealing to the\
      \ benevolence of God'."
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: IEP.
  deity_personal:
    value: "Not part of the solipsist doctrine. Descartes uses God's benevolence to escape solipsism;\
      \ the thesis itself is about minds, not theology."
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: IEP.
  intervention:
    value: "Not part of the solipsist doctrine. Descartes uses God's benevolence to escape solipsism;\
      \ the thesis itself is about minds, not theology."
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: IEP.
  miracles:
    value: "Not part of the solipsist doctrine. Descartes uses God's benevolence to escape solipsism;\
      \ the thesis itself is about minds, not theology."
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: IEP.
  petition_and_prayer:
    value: "Not part of the solipsist doctrine. Descartes uses God's benevolence to escape solipsism;\
      \ the thesis itself is about minds, not theology."
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: IEP.
  afterlife:
    value: "Not part of the solipsist doctrine. Descartes uses God's benevolence to escape solipsism;\
      \ the thesis itself is about minds, not theology."
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: IEP.
  moral_ledger:
    value: 'Not addressed. If only one mind is intelligible, a interpersonal divine judge is not in view.'
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: introduction
    how_known: "Coder's reading; ethics largely absent from IEP entry."
  authority:
    value: "Privileged access to one's own mental states is the epistemic starting point that makes solipsism\
      \ seem threatening; Wittgensteinian critique rejects that picture. Not revelation."
    stance: observation and reason
    certainty: 0.5
    cites:
    - source: S1
      locator: §1; §7
    how_known: "Borderline: 'observation' here is inner experience on the Cartesian picture. Certainty\
      \ 0.5."
  reserved_exemptions:
    value: Not addressed as cosmology.
    stance: none
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: 'IEP is about other minds, not exemptions from natural law.'
  teleology_in_nature:
    value: Not addressed.
    stance: none
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: IEP.
  necessity_and_freedom:
    value: Not a free-will doctrine. Concern is intelligibility of other minds and privacy of experience.
    certainty: 1.0
    cites:
    - source: S1
      locator: §6
    how_known: IEP.
lio_axes:
  A_locus:
    value: 4
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: '0.7 — solipsism as metaphysical/epistemic thesis about minds/world; no God or spiritual
      being required (P44a).'
    rationale: 'A=4: no transcendent personal God in the thesis. Not BELOW: the position itself fixes
      absence of deity.'
    alternatives:
    - value: 'UNKNOWN'
      note: Named alternative if coding only the problem-statement form without ontological commitment.
      cites:
      - source: S1
        locator: opening
  B_cause:
    value: 'UNKNOWN'
    how_known: "Thesis about minds/existence-for-me, not a God cosmology or a public science of authority\
      \ (P44). Descartes' God escape is not part of SOLIP."
  C_ledger:
    value: 'UNKNOWN'
    how_known: "Thesis about minds/existence-for-me, not a God cosmology or a public science of authority\
      \ (P44). Descartes' God escape is not part of SOLIP."
  D_authority:
    value: 4
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: '0.7 — IEP frames privileged access / Cartesian argument; stance already observation and
      reason.'
    rationale: 'D=4: reason and first-person argument outrank revelation. Not 3: no church or scripture
      as primary.'
    alternatives:
    - value: 3
      note: Named alternative if coding common-sense rebuttals as co-equal method.
      cites:
      - source: S1
        locator: opening
  E_scope:
    value: 'UNKNOWN'
    how_known: "Thesis about minds/existence-for-me, not a God cosmology or a public science of authority\
      \ (P44). Descartes' God escape is not part of SOLIP."
epistemology:
  value: "On the Cartesian picture: what is known most certainly are the contents of one's own mind; other\
    \ minds only by analogy (then argued to fail). Wittgensteinian critique: psychological concepts are\
    \ learned in public language-games; private-language and privacy-of-experience theses are rejected;\
    \ solipsism is incoherent because it requires public language."
  certainty: 1.0
  cites:
  - source: S1
    locator: §1; §3; §7
  how_known: IEP.
ethics:
  value: Not developed as an ethics. The problem is metaphysical/epistemic; IEP does not state a solipsist
    moral theory.
  certainty: 1.0
  cites:
  - source: S1
    locator: introduction
  how_known: IEP silence.
practice:
  ritual_and_practice:
    value: "None as a lived school. 'No great philosopher has espoused solipsism' [S1]."
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: IEP.
  community_form:
    value: Not a community; a philosophical problem. A nuclear-holocaust sole survivor believing they
      are alone is still not a solipsist in the IEP sense.
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: IEP.
science:
  historical_stance:
    value: 'Threat arises inside modern epistemology, not as a scientific research programme. Empiricist
      psychology-from-own-case feeds the problem.'
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: IEP.
  current_stance:
    value: Treated as incoherent or foundationless in the Wittgensteinian line; remains a teaching problem
      in philosophy of mind. Not a scientific stance.
    certainty: 1.0
    cites:
    - source: S1
      locator: §7
    how_known: IEP.
schools_and_variants:
- name: Metaphysical solipsism (only my mind exists)
  form: scholastic or philosophical
  how_it_differs: Ontological claim; rarely if ever sincerely held.
  lio_difference: Does not fix God axes; all UNKNOWN.
  certainty: 1.0
  cites:
  - source: S1
    locator: introduction
- name: Methodological / implicit solipsism in egocentric epistemologies
  form: scholastic or philosophical
  how_it_differs: "IEP: many post-Cartesian theories of knowledge are 'inherently solipsistic' in starting\
    \ from own case without affirming the doctrine."
  lio_difference: "Code the person's actual system (e.g. SCEPT), not SOLIP, unless they affirm the doctrine."
  certainty: 1.0
  cites:
  - source: S1
    locator: §1
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Philosophical problem/thesis; essentially no organized adherent body
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: '0.7 — qualitative from listed source; not a genius-rate denominator.'
v7_1_rubric:
  label: authorial v7.1 scores
  L: 9
  P: 9
  E: 5
  V: 8
  X: 4
  total: 35
  scoring_note: 'Solipsism scores moderately high for its radical logical purity and focus on personal
    certainty, but is limited by its dismissal of empirical intersubjectivity and practical applicability.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 38 and section 7 scoring notes'
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
  use_when: "The person's own writing affirms that only their own mind exists (rare)."
  do_not_use_when: Methodological doubt (Descartes) is not SOLIP. Phenomenological bracketing is not SOLIP.
    Idealism is not SOLIP.
  neighbors:
  - code: IDEAL
    relation: neighbor (easily confused)
  - code: PHENOM
    relation: neighbor (easily confused)
  - code: SCEPT
    relation: neighbor (easily confused)
review:
  data_quality_flags: []
  open_questions:
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Stephen P. Thornton
  citation: 'Thornton, Stephen P. "Solipsism and the Problem of Other Minds." Internet Encyclopedia of
    Philosophy. https://iep.utm.edu/solipsis/.'
  url: 'https://iep.utm.edu/solipsis/'
  accessed: '2026-10-25'
  reliability_note: Peer-reviewed reference entry; undated page.
---
# Solipsism (SOLIP)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44. The v7.1 scores and note are unchanged.

## Summary

Solipsism is 'the doctrine that, in principle, “existence” means for me my existence and that of my mental states' [S1]. 'No great philosopher has espoused solipsism' [S1]; it is examined as a threat arising from Cartesian egocentric epistemology and as incoherent once public language is taken seriously [S1].

## Core metaphysics

Only my mind / mental states are intelligible as existent in the strong doctrine [S1]. Theology is not part of the thesis; Descartes escapes via God's benevolence [S1].

## Position on the LIO axes

All UNKNOWN — mind thesis, not a God cosmology; Descartes' God is an escape from SOLIP, not SOLIP (P44).

## Schools and variants

Metaphysical solipsism (rare); methodological/implicit solipsism in egocentric epistemologies [S1].

## Science

Not a scientific programme; a problem in philosophy of mind and language [S1].

## Coding guidance

Only when the person's own writing affirms that only their mind exists. Methodic doubt and bracketing are not SOLIP.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> SOLIP (35/50) — Solipsism. Solipsism scores moderately high for its radical logical purity and focus on personal certainty, but is limited by its dismissal of empirical intersubjectivity and practical applicability.

## Open questions

- Adherents are TODO (effectively none as a lived school).

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7.
- 2026-10-15 (systems batch S6): IEP Thornton; axes under P44.
- 2026-10-25: deepened classification, origins, metaphysics, epistemology, practice, science, schools. Re-read IEP.
- 2026-10-25: adherents/estimate filled (qualitative).
- 2026-10-25: A=4 and D=4 scored from IEP.
