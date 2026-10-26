---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 5
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
    summary: 'Draft (systems batch S5): filled from SEP "Idealism" (Guyer and Horstmann). A BELOW_THRESHOLD;
      others UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S10 audit fix: A how_known repeats the source quote.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities: family, parents, related codes, founders/texts, remaining metaphysics
      (varies/not addressed), epistemology, ethics, practice, science, schools (Berkeley, Kant, German/British
      absolute). A stays BELOW_THRESHOLD; B–E UNKNOWN. Re-read SEP Idealism (Guyer/Horstmann).'
identity:
  id: IDEAL
  v7_1_number: 34
  v7_1_label: Idealism
  display_label: Idealism
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: family of positions
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: Epistemological and ontological idealism (SEP).
  family:
    value: Modern philosophical idealisms (ontological and epistemologically argued)
    certainty: 1.0
    cites: &id001
    - source: S1
      locator: introduction
    how_known: 'SEP: movement chiefly 18th–19th c.; mental foundational or knowledge permeated by mind.'
  parent_traditions:
    value:
    - 'Early modern rationalism (Malebranche, Leibnizian readings)'
    - British empiricism (Berkeley)
    - Kantian critical philosophy
    - German and British absolute idealism
    certainty: 1.0
    cites: *id001
    how_known: SEP section map.
  related_codes:
  - code: SOLIP
    relation: neighbor (easily confused)
    note: Solipsism is egoistic idealism; not all idealism is solipsism (Wolff taxonomy in SEP)
  - code: PANENT
    relation: neighbor (easily confused)
    note: Some absolute idealisms shade toward God-world identity talk
  - code: PLATO
    relation: neighbor (easily confused)
    note: SEP largely sets pre-modern Platonism aside; Forms are not this code’s focus
  - code: KANT
    relation: offshoot
    note: 'If KANT is coded separately: transcendental idealism is one major strand inside the family'
origins:
  founding_era:
    value: Chiefly the eighteenth and nineteenth centuries
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP.
  founding_region:
    value: Britain and Germany (chief modern centers); precursors across early modern Europe
    certainty: 1.0
    cites: *id001
    how_known: 'SEP focuses Berkeley/Hume/Kant, German idealism, British/American idealism.'
  founders_or_key_figures:
    value:
    - George Berkeley
    - Immanuel Kant
    - 'German Idealists (Fichte, Schelling, Hegel — as treated in SEP)'
    - 'British/American absolute idealists (e.g. Bradley, Royce)'
    - Brand Blanshard (late defense)
    certainty: 1.0
    cites: *id001
    how_known: SEP introduction and section plan.
  key_texts:
  - value: 'Berkeley, Principles / Three Dialogues (immaterialism)'
    certainty: 1.0
    cites:
    - source: S1
      locator: §3
    how_known: SEP.
  - value: 'Kant, Critique of Pure Reason; Prolegomena'
    certainty: 1.0
    cites:
    - source: S1
      locator: §4
    how_known: SEP.
  - value: 'German Idealism corpus; British/American absolute idealism (Bradley, Royce, et al.)'
    certainty: 0.7
    cites:
    - source: S1
      locator: §5; §8
    how_known: SEP section titles. 0.7.
metaphysics:
  god_nature_relation:
    value: "Varies: idealism commits to 'the primacy or at least the unavoidability and irreducibility\
      \ of mental items in the constitution and order of things'; some forms rest on 'a God such as Berkeley\
      \ postulates'."
    stance: varies by school
    certainty: 0.7
    cites:
    - source: S1
      locator: introduction; §1
    how_known: SEP.
  deity_personal:
    value: 'Varies: Berkeley’s God; absolute idealisms often impersonal Absolute; Kant denies theoretical
      knowledge of God as thing-in-itself while allowing practical postulates.'
    stance: varies by school
    certainty: 0.7
    cites: &id002
    - source: S1
      locator: introduction; §1
    how_known: SEP introduction and Kant/Berkeley discussions. 0.7.
  intervention:
    value: Not a shared doctrine of the family. Berkeley’s God sustains ideas; many later idealisms are
      not miracle religions.
    stance: varies by school
    certainty: 0.7
    cites: *id002
    how_known: Coder reading of SEP range. 0.7.
  miracles:
    value: Not addressed as a shared thesis across idealism.
    stance: not addressed
    certainty: 1.0
    cites: *id001
    how_known: 'SEP is metaphysics/epistemology history, not miracle doctrine.'
  petition_and_prayer:
    value: Not a shared cult practice of the philosophical family.
    stance: not addressed
    certainty: 1.0
    cites: *id001
    how_known: SEP.
  afterlife:
    value: Not fixed across schools; not the defining issue in SEP’s survey.
    stance: not addressed
    certainty: 1.0
    cites: *id001
    how_known: SEP.
  moral_ledger:
    value: 'Not a shared afterlife ledger doctrine. Some idealists (Green, Royce) connected idealism to
      progressive social ethics; that is not a divine judge schema.'
    stance: none
    certainty: 0.7
    cites: *id001
    how_known: SEP notes social-philosophy idealism but does not define a moral ledger. 0.7.
  authority:
    value: Philosophical argument (metaphysical and/or epistemological). No shared revealed scripture
      for the family as such.
    stance: observation and reason
    certainty: 0.7
    cites: *id001
    how_known: SEP frames idealism as philosophical theories and arguments. 0.7.
  reserved_exemptions:
    value: Not addressed as a shared doctrine.
    stance: none
    certainty: 1.0
    cites: *id001
    how_known: SEP.
  teleology_in_nature:
    value: Varies; absolute idealisms often read nature as expression of mind/Absolute; Kant’s theoretical
      philosophy restricts teleology.
    stance: varies by school
    certainty: 0.7
    cites:
    - source: S1
      locator: §4; §5
    how_known: '0.7.'
  necessity_and_freedom:
    value: 'SEP notes freedom motives for some idealisms (mental causation, autonomy) alongside world-constitution
      motives; no single free-will doctrine for the family.'
    certainty: 0.7
    cites: *id001
    how_known: SEP §1 motives discussion. 0.7.
lio_axes:
  A_locus:
    value: 'BELOW_THRESHOLD'
    how_known: "Idealists differ on God (Berkeley versus others) (S1): P44(b). Quote (S1, introduction;\
      \ §1): Varies: idealism commits to 'the primacy or at least the unavoidability and irreducibility\
      \ of mental items in the constitution and order of things'; some forms rest on 'a God such as Berkeley\
      \ postulates'."
    note: 'Evidence: S1 §1.'
  B_cause:
    value: 'UNKNOWN'
    how_known: Not addressed in the sources read.
  C_ledger:
    value: 'UNKNOWN'
    how_known: Not addressed in the sources read.
  D_authority:
    value: 'UNKNOWN'
    how_known: Not addressed in the sources read.
  E_scope:
    value: 'UNKNOWN'
    how_known: Not addressed in the sources read.
epistemology:
  value: 'SEP distinguishes metaphysical vs epistemological *arguments* for idealism as a metaphysical
    thesis that reality is in some way mental. Epistemological route: conditions of knowledge force the
    known to be mental (isomorphism). Not the weaker claim that we always know from a point of view.'
  certainty: 1.0
  cites: *id001
  how_known: SEP introduction (Ewing / deVries framing).
ethics:
  value: 'No single ethics for the family. SEP notes British/American university idealism often linked
    to progressive social thought (Green, Bosanquet, Royce) without making that definitional.'
  certainty: 1.0
  cites:
  - source: S1
    locator: introduction
  how_known: SEP.
practice:
  ritual_and_practice:
    value: 'Philosophical movement, not a church ritual system.'
    certainty: 1.0
    cites: *id001
    how_known: SEP.
  community_form:
    value: Academic and literary schools (German Idealism; British/American absolute idealism as university
      movement).
    certainty: 1.0
    cites: *id001
    how_known: SEP.
science:
  historical_stance:
    value: 'Engages laws of nature, representation, and the status of the physical; Kant’s empirical realism
      aims to secure ordinary science while denying space/time of things in themselves.'
    certainty: 0.7
    cites:
    - source: S1
      locator: §4
    how_known: SEP Kant section. 0.7.
  current_stance:
    value: 'Historical movement; SEP tracks 20th-c. attack (Moore, Russell) and late defenses (Blanshard).
      Not a scientific research programme.'
    certainty: 1.0
    cites:
    - source: S1
      locator: §9
    how_known: SEP.
schools_and_variants:
- name: Berkeleyan immaterialism
  form: scholastic or philosophical
  how_it_differs: Esse is percipi; minds and ideas (plus God); ontological idealism
  lio_difference: Would move A toward theism — still BELOW_THRESHOLD for the family
  certainty: 1.0
  cites:
  - source: S1
    locator: §3
- name: Kantian transcendental / critical idealism
  form: scholastic or philosophical
  how_it_differs: Space/time forms of intuition; empirical realism + transcendental idealism; things in
    themselves affirmed
  lio_difference: Does not reduce to Berkeleian immaterialism — A still BELOW_THRESHOLD for family
  certainty: 1.0
  cites:
  - source: S1
    locator: §4
- name: German Idealism
  form: scholastic or philosophical
  how_it_differs: Post-Kantian absolute/subjective developments (SEP §5)
  lio_difference: May move A/B — not rescored for family label
  certainty: 1.0
  cites:
  - source: S1
    locator: §5
- name: British and American absolute idealism
  form: scholastic or philosophical
  how_it_differs: 'Bradley, Royce et al.; often linked to social philosophy'
  lio_difference: May move A — not rescored for family label
  certainty: 1.0
  cites:
  - source: S1
    locator: §8
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Not a census religion; historical philosophical movement
    certainty: 1.0
    cites: *id001
    how_known: 'SEP presents philosophical history, not membership.'
v7_1_rubric:
  label: authorial v7.1 scores
  L: 8
  P: 8
  E: 7
  V: 9
  X: 6
  total: 38
  scoring_note: 'Idealism scores moderately due to its innovative mind-centered view of reality, providing
    philosophical depth but constrained by challenges in empirical verification and material compatibility.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 34 and section 7 scoring notes'
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
  use_when: "The person's own writing holds that reality is mental or thought-like (candidate for Pasteur)."
  do_not_use_when: "French spiritualism (Pasteur's 'doctrine spiritualiste') is only a partial fit (S7);\
    \ Kant is KANT; Platonism is PLATO."
  neighbors:
  - code: SOLIP
    relation: neighbor (easily confused)
    note: 'Egoism/solipsism is one Wolffian subtype, not the whole'
  - code: PLATO
    relation: neighbor (easily confused)
    note: Pre-modern Forms not this code’s SEP focus
review:
  data_quality_flags: []
  open_questions:
  - Should Kantian transcendental idealism be forced into IDEAL or kept only under KANT when that code
    is used?
  - Can B_cause be scored for Berkeley (God sustains ideas) without breaking P44(b) for the family?
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Paul Guyer; Rolf-Peter Horstmann
  year: 2026
  citation: 'Paul Guyer and Rolf-Peter Horstmann. "Idealism." Stanford Encyclopedia of Philosophy. First
    published August 30, 2015; substantive revision May 5, 2026. https://plato.stanford.edu/entries/idealism/.'
  url: 'https://plato.stanford.edu/entries/idealism/'
  accessed: '2026-10-25'
  reliability_note: Peer-reviewed reference entry.
---
# Idealism (IDEAL)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44. The v7.1 scores and note are unchanged.

## Summary

SEP treats idealism as a movement chiefly in the eighteenth and nineteenth centuries, anticipated earlier and continuing into the twentieth [S1]. The shared metaphysical claim (following Ewing/deVries in SEP) is that reality is in some way mental — either ontologically foundational mind, or knowable only as permeated by mind — rather than everyday optimism called “idealism” [S1].

## Core metaphysics

Mind (or the mental) has primacy or irreducibility in the constitution of reality [S1]. Schools diverge: Berkeley’s immaterialism (ideas and minds, including God); Kant’s transcendental idealism with empirical realism and things in themselves; German Idealism; British/American absolute idealism [S1]. God, afterlife, and miracle doctrines are not shared across the family.

## Position on the LIO axes

- **A_locus:** BELOW_THRESHOLD — idealists differ on God (Berkeley vs others) [S1] (P44(b)).
- **B, C, D, E:** UNKNOWN — not fixed for the family in the sources read.

## Schools and variants

Berkeleyan immaterialism; Kantian critical idealism; German Idealism; British/American absolute idealism [S1].

## Epistemology

SEP separates metaphysical arguments (only minds satisfy existence constraints) from epistemological arguments (knowledge requires the known to be mental) for idealism as a metaphysical thesis [S1].

## Science

Engages representation and the status of the physical; Kant’s empirical realism aims to secure ordinary science while denying space/time of things in themselves [S1]. SEP tracks twentieth-century attack (Moore, Russell) and late defenses (Blanshard) [S1].

## Coding guidance

Use when the person’s own writing holds that reality is mental or thought-like. Kant-only coding may prefer KANT if that code is in play; Platonism is PLATO.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> Idealism scores moderately due to its innovative mind-centered view of reality, providing philosophical depth but constrained by challenges in empirical verification and material compatibility.

## Open questions

- Should Kantian transcendental idealism be forced into IDEAL or kept only under KANT when that code is used?
- Can B_cause be scored for Berkeley without breaking P44(b) for the family?

## Research log

- 2026-10-01: stub created.
- 2026-10-15 (systems batch S5): filled from SEP; A BELOW_THRESHOLD.
- 2026-10-25: deepened classification, origins, metaphysics TODOs, epistemology, ethics, practice, science, schools; re-read SEP Idealism (Guyer/Horstmann, rev. 2026-05-05).
