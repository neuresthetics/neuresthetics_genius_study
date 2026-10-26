---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 5
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S4 for Jason)
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
    summary: 'Draft (systems batch S4): filled from SEP "Immanuel Kant" (Rohlf) and "Kant’s Philosophy
      of Religion" (Pasternack and Fugate). A 1 (0.5), B 3 (0.5), C BELOW_THRESHOLD (alt 1), D 3 (0.5),
      E UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: "S4 audit (WEAKEN #2): A_locus 1 (0.5) → 0 (0.5), alternative 1; miracle quote labelled 'SEP,\
      \ reporting AK 6:52'; note that the architect limit is on theoretical proof only. Stance kept."
  - date: '2026-10-25'
    by: Grok Bot
    summary: "Deepen qualities from SEP Kant's Philosophy of Religion + SEP Kant: family/parents, metaphysics\
      \ TODOs, epistemology/ethics/practice/science. Axes unchanged."
identity:
  id: KANT
  v7_1_number: 22
  v7_1_label: Kantianism
  display_label: Kantianism
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: philosophical school or method
    certainty: 0.7
    cites:
    - source: S2
      locator: introduction
    how_known: "Kant 'is the central figure in modern philosophy'. Coder's classification, 0.7."
  family:
    value: Critical / transcendental idealism; moral theology grounded in practical reason; pure rational
      religion
    certainty: 1.0
    cites:
    - source: S1
      locator: §1; §3
    - source: S2
      locator: introduction
    how_known: SEP.
  parent_traditions:
    value:
    - Lutheran Pietism
    - Leibnizian–Wolffian school
    - Newtonian science
    - Rousseau
    certainty: 1.0
    cites:
    - source: S1
      locator: §2.1
    how_known: SEP.
  related_codes:
  - code: DEISM
    relation: neighbor (easily confused)
    note: Kant’s “Deism” = thin transcendental theology; British deism closer to his Theism
  - code: RATN
    relation: overlaps
    note: Reason-first; moral postulates
  - code: AGNOS
    relation: neighbor (easily confused)
    note: Limits knowledge to make room for faith — not mere suspension
origins:
  founding_era:
    value: 'Late eighteenth century (Kant, 1724–1804)'
    certainty: 1.0
    cites:
    - source: S2
      locator: introduction
    how_known: SEP.
  founding_region:
    value: 'Königsberg, Prussia'
    certainty: 0.7
    cites:
    - source: S2
      locator: §1
    how_known: SEP life section; 0.7.
  founders_or_key_figures:
    value:
    - Immanuel Kant
    certainty: 1.0
    cites:
    - source: S2
      locator: introduction
    how_known: SEP.
  key_texts:
  - value: Critique of Pure Reason
    author: Immanuel Kant
    certainty: 1.0
    cites:
    - source: S1
      locator: §3
    how_known: SEP.
  - value: Religion within the Boundaries of Mere Reason
    author: Immanuel Kant
    certainty: 1.0
    cites:
    - source: S1
      locator: overview
    how_known: SEP.
metaphysics:
  god_nature_relation:
    value: "God as a postulate of practical reason, rooted in the highest good; theoretically, the design\
      \ argument reaches 'an architect of the world' but not an infinite creator."
    stance: creator distinct from creation
    certainty: 1.0
    cites:
    - source: S1
      locator: §3.4–3.5
    how_known: SEP.
    note: "The 'architect of the world' limit applies to the theoretical proof only (Kant rejects the\
      \ step from a 'Wise Author of Nature' to an infinite creator); the practical postulate is of a moral\
      \ author of the world (S4 audit RQ2)."
  deity_personal:
    value: 'Moral theism: God as wise author / judge postulated for highest good; not mere ens realissimum
      abstraction'
    stance: personal
    certainty: 0.7
    cites:
    - source: S1
      locator: §3.2; §3.5
    how_known: '0.7 — interpretive disputes.'
  intervention:
    value: Theoretical reason cannot establish intervention; practical faith does not require ongoing
      miracles; Opus Postumum readings vary
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S1
      locator: §3.7.6; §4
    how_known: '0.7.'
  miracles:
    value: "SEP, reporting AK 6:52: reason 'does not contest the possibility or actuality' of miracles\
      \ (and grace, mysteries); 'it just cannot incorporate them into its maxims of thought or action'."
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: 'Religion, part 1'
    how_known: SEP.
  petition_and_prayer:
    value: Prayer and ritual can be reconstituted for moral religion; petition for favors risks counterfeit
      service
    stance: contemplative only
    certainty: 0.7
    cites:
    - source: S1
      locator: §3.7.5
    how_known: '0.7.'
  afterlife:
    value: Immortality postulated for highest good / moral striving; revisions across Critiques and Religion
    stance: personal afterlife
    certainty: 1.0
    cites:
    - source: S1
      locator: §3.5.2
    how_known: SEP.
  moral_ledger:
    value: 'Highest good: happiness proportioned to moral worth; God as distributor; not karma-type impersonal
      law'
    stance: personal reward and punishment
    certainty: 1.0
    cites:
    - source: S1
      locator: §3.4–3.5
    how_known: SEP.
  authority:
    value: "'human reason gives itself the moral law, which is our basis for belief in God, freedom, and\
      \ immortality'."
    stance: 'both, reason first'
    certainty: 1.0
    cites:
    - source: S2
      locator: introduction
    how_known: SEP.
  reserved_exemptions:
    value: Same moral law for all finite rational beings; no in-group exemption from duty
    stance: none
    certainty: 1.0
    cites:
    - source: S1
      locator: §3.7
    how_known: SEP.
  teleology_in_nature:
    value: Wise Author of nature as regulative idea; Critique of Judgment purposiveness; not a theoretical
      proof of designer
    stance: "designer's purposes"
    certainty: 0.7
    cites:
    - source: S1
      locator: §3.1.2.3; §3.2
    how_known: '0.7 — regulative vs constitutive debate.'
  necessity_and_freedom:
    value: Freedom as practical postulate / condition of moral law; causality of nature vs causality of
      freedom
    certainty: 1.0
    cites:
    - source: S1
      locator: §3.5
    - source: S2
      locator: introduction
    how_known: SEP.
lio_axes:
  A_locus:
    value: 0
    rationale: 'God postulated by practical reason as a transcendent, personal moral author of the world;
      the study scores that pattern A 0 (as Locke, Bacon, Boyle).'
    certainty: 0.5
    cites:
    - source: S1
      locator: §3.5.1
    - source: S2
      locator: introduction
    how_known: "0.5: God here is a practical postulate, not knowledge, and personhood is the coder's reading.\
      \ Alternative 1. Changed from 1 (0.5) after the S4 audit."
    alternatives:
    - value: 1
      note: Thinly personal moral author.
      cites:
      - source: S1
        locator: §3.5.1
  B_cause:
    value: 3
    rationale: 'Miracles are not contested but cannot enter the maxims of thought or action: nature is
      treated as lawful.'
    certainty: 0.5
    cites:
    - source: S1
      locator: 'Religion, part 1'
    how_known: '0.5: inferred from SEP, reporting AK 6:52.'
  C_ledger:
    value: 'BELOW_THRESHOLD'
    how_known: The postulates of God and immortality are rooted in the highest good (S1 §3.4–3.5); SEP
      excerpts read do not state the proportion of happiness to virtue.
    note: 'Alternative: 1 (God secures the highest good).'
    alternatives:
    - value: 1
      note: Named alternative.
      cites:
      - source: S1
        locator: §3.4
  D_authority:
    value: 3
    rationale: 'Reason first: religion within the boundaries of mere reason; revelation treated, but reason
      gives the moral law that grounds belief in God.'
    certainty: 0.5
    cites:
    - source: S2
      locator: introduction
    - source: S1
      locator: overview
    how_known: 'Stance label both, reason first; 0.5.'
  E_scope:
    value: 'UNKNOWN'
    how_known: Not addressed in the sources read.
epistemology:
  value: Limits of theoretical knowledge of supersensible; practical cognition and moral faith (Glaube);
    hope; analogy for religious concepts
  certainty: 1.0
  cites:
  - source: S1
    locator: §3.3
  how_known: SEP.
ethics:
  value: Autonomy; categorical imperative; radical evil and change of heart in Religion; highest good
    as morality + proportionate happiness
  certainty: 1.0
  cites:
  - source: S1
    locator: §3.4; §3.7
  - source: S2
    locator: introduction
  how_known: SEP.
practice:
  ritual_and_practice:
    value: Good life-conduct as genuine religion; church attendance/prayer reconstituted; rejects counterfeit
      service
    certainty: 1.0
    cites:
    - source: S1
      locator: §3.7.5
    how_known: SEP.
  community_form:
    value: Ethical community / universal church as social dimension of highest good
    certainty: 1.0
    cites:
    - source: S1
      locator: §3.7.4
    how_known: SEP.
science:
  historical_stance:
    value: Newtonian cosmology informs pre-Critical physico-theology; Critical limits theoretical theology
    certainty: 1.0
    cites:
    - source: S1
      locator: §2.1.2
    how_known: SEP.
  current_stance:
    value: Central modern figure; philosophy of religion actively debated
    certainty: 1.0
    cites:
    - source: S2
      locator: introduction
    how_known: SEP.
schools_and_variants:
- name: Kantian moral theology (Critical)
  form: scholastic or philosophical
  how_it_differs: Practical postulates of God and immortality
  lio_difference: Not rescored
  certainty: 1.0
  cites:
  - source: S1
    locator: §3.5
- name: Religion within Boundaries readings
  form: scholastic or philosophical
  how_it_differs: Apologetic vs pure-rational-system vs non-doxic interpretations
  lio_difference: May affect B/D — keep prior scores
  certainty: 0.7
  cites:
  - source: S1
    locator: §3.6
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Historical school; lasting influence in philosophy of religion (not a mass religion census)
    certainty: 0.7
    cites:
    - source: S2
      locator: introduction
    how_known: '0.7.'
v7_1_rubric:
  label: authorial v7.1 scores
  L: 9
  P: 9
  E: 9
  V: 10
  X: 8
  total: 45
  scoring_note: 'Kantianism scores high for its logical rigor and emphasis on universal duty, providing
    a foundational deontological framework, though slightly limited by abstraction from real-world variability.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 22 and section 7 scoring notes'
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
  use_when: Person’s primary philosophy is Kantian Critical philosophy / moral theology.
  do_not_use_when: Mere “limits of knowledge” slogans without Kantian practical faith; British deism alone.
  neighbors:
  - code: DEISM
    relation: neighbor (easily confused)
    note: Thin vs moral theism
  - code: AGNOS
    relation: neighbor (easily confused)
    note: Faith ≠ suspension
review:
  data_quality_flags: []
  open_questions:
  - Opus Postumum break vs continuity for A?
  - Score C from highest-good ledger more firmly?
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Lawrence Pasternack; Courtney Fugate
  year: 2025
  citation: 'Lawrence Pasternack and Courtney Fugate. "Kant’s Philosophy of Religion." Stanford Encyclopedia
    of Philosophy. First published June 22, 2004; substantive revision October 13, 2025. https://plato.stanford.edu/entries/kant-religion/.'
  url: 'https://plato.stanford.edu/entries/kant-religion/'
  accessed: '2026-10-25'
  reliability_note: Peer-reviewed reference entry.
- id: S2
  type: tertiary
  kind: encyclopedia
  author: Michael Rohlf
  year: 2024
  citation: 'Michael Rohlf. "Immanuel Kant." Stanford Encyclopedia of Philosophy. First published May
    20, 2010; substantive revision July 31, 2024. https://plato.stanford.edu/entries/kant/.'
  url: 'https://plato.stanford.edu/entries/kant/'
  accessed: '2026-10-25'
  reliability_note: Peer-reviewed reference entry.
---
# Kantianism / Kant’s philosophy of religion (KANT)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44. The v7.1 scores and note are unchanged.

## Summary

Critical philosophy: limits of theoretical knowledge to make room for moral faith; God and immortality as practical postulates for the highest good [S1][S2].

## Core metaphysics

Ens realissimum critiqued as theoretical proof; moral theism; immortality; regulative Wise Author [S1].

## Position on the LIO axes

Prior scores (A0 B3 C BELOW_THRESHOLD D3 E UNKNOWN) unchanged this pass.

## Schools and variants

Critical moral theology; contested Religion readings [S1].

## Science

Newtonian backdrop; Critical limits on theoretical theology [S1].

## Coding guidance

Kantian Critical / moral theology → KANT.

## v7.1 scoring note

Authorial v7.1 note unchanged (see front matter).

## Open questions

- Opus Postumum for A?
- Firmer C from highest good?

## Research log

- Prior partial fills (god, miracles, authority).
- 2026-10-25: deepened TODOs from SEP; axes unchanged.
