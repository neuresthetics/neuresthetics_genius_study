---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 4
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S2 for Jason)
  model_used: Grok Bot executor agent; direct reads of the cited pages
  collected_on: '2026-10-01'
  last_updated: '2026-10-25'
  change_log:
  - date: '2026-10-01'
    by: scripts/make_system_stubs.py
    summary: Stub created from v7.1 data book table 4 and section 7.
  - date: '2026-10-02'
    by: scripts/make_system_stubs.py
    summary: 'Decision P7: E_scope note added. E is not scored in a stub; when it is, score it on the
      world''s order (same rules for every kind of being and event, no in-group exceptions in this-world
      events). Salvation and moral community go on C_ledger.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'Draft (systems batch S2): filled from Britannica "Effective altruism" (Brodsky). Every axis
      UNKNOWN: an ethics and movement with no stated metaphysics. v7.1 scores and note unchanged. Not
      reviewed.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities: family, parents, related codes, metaphysics TODOs, epistemology, practice,
      science, schools (earning to give; longtermism). Add SEP Philanthropy (S2). Score D_authority 3
      (0.7) from evidence-and-reason framing. A/B/C/E stay UNKNOWN. Sources: Britannica Brodsky; SEP Philanthropy
      §3.2.'
identity:
  id: EFFALT
  v7_1_number: 12
  v7_1_label: Effective Altruism
  display_label: Effective Altruism
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: ethical or civic movement
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: '''in ethics, a theory of conduct and a movement''.'
  family:
    value: Consequentialist-leaning ethics of giving and a social movement that uses evidence to maximize
      benefits to others
    certainty: 1.0
    cites:
    - source: S2
      locator: §3.2
    - source: S1
      locator: opening
    how_known: 'SEP: EA ''use[s] evidence and reason to determine how to benefit others as much as possible'';
      Britannica: theory of conduct and movement.'
  parent_traditions:
    value:
    - Peter Singer's arguments on famine and obligation
    - Utilitarian / consequentialist ethics
    - Evidence-based charity evaluation
    certainty: 1.0
    cites:
    - source: S2
      locator: §3.2
    - source: S1
      locator: Historical developments
    how_known: SEP traces roots to Singer 1972; Britannica names Singer, MacAskill, Ord.
  related_codes:
  - code: UTIL
    relation: neighbor (easily confused)
    note: EA often consequentialist but Britannica separates it from utilitarianism as such
  - code: SECHUM
    relation: overlaps
    note: shared secular benevolence; EFFALT is the evidence-maximizing movement
  - code: HEDON
    relation: overlaps
    note: welfarist pleasure/pain metrics sometimes used; not required
origins:
  founding_era:
    value: 1972 roots (Singer); Giving What We Can 2009
    certainty: 1.0
    cites:
    - source: S1
      locator: Historical developments
    how_known: Britannica.
  founding_region:
    value: Anglophone academic and philanthropic networks (UK/US); Giving What We Can founded 2009
    certainty: 0.7
    cites:
    - source: S1
      locator: Historical developments
    how_known: Coder's geographic gloss on Britannica's founding figures and orgs.
  founders_or_key_figures:
    value:
    - Peter Singer
    - William MacAskill
    - Toby Ord
    certainty: 1.0
    cites:
    - source: S1
      locator: Historical developments
    how_known: Britannica.
  key_texts:
  - value: '"Famine, Affluence, and Morality"'
    author: Peter Singer
    year: 1972
    certainty: 1.0
    cites:
    - source: S1
      locator: Historical developments
    how_known: Britannica.
  - value: Doing Good Better
    author: William MacAskill
    year: 2015
    certainty: 1.0
    cites:
    - source: S1
      locator: Historical developments
    how_known: Britannica.
  - value: What We Owe the Future
    author: William MacAskill
    year: 2022
    certainty: 1.0
    cites:
    - source: S1
      locator: Historical developments
    how_known: Britannica.
metaphysics:
  god_nature_relation:
    value: Not addressed.
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: Britannica describes an ethics and movement only.
  deity_personal:
    value: Not addressed as doctrine. Members may hold any God-view; the movement itself is silent.
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    - source: S2
      locator: §3.2
    how_known: Britannica and SEP describe an ethics and movement; no theology.
  intervention:
    value: Not addressed as doctrine. Members may hold any God-view; the movement itself is silent.
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    - source: S2
      locator: §3.2
    how_known: Britannica and SEP describe an ethics and movement; no theology.
  miracles:
    value: Not addressed as doctrine. Members may hold any God-view; the movement itself is silent.
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    - source: S2
      locator: §3.2
    how_known: Britannica and SEP describe an ethics and movement; no theology.
  petition_and_prayer:
    value: Not addressed as doctrine. Members may hold any God-view; the movement itself is silent.
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    - source: S2
      locator: §3.2
    how_known: Britannica and SEP describe an ethics and movement; no theology.
  afterlife:
    value: Not addressed as doctrine. Members may hold any God-view; the movement itself is silent.
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    - source: S2
      locator: §3.2
    how_known: Britannica and SEP describe an ethics and movement; no theology.
  moral_ledger:
    value: No divine judge. Moral weight is on benefits to others (often impartial and welfarist); longtermism
      extends concern to future generations. Not a personal afterlife ledger.
    stance: none
    certainty: 0.7
    cites:
    - source: S2
      locator: §3.2
    how_known: Coder's reading of SEP EA section.
  authority:
    value: 'Evidence and reason: identify interventions that help most, then mobilize resources. Charity
      evaluators and expected-value reasoning over tradition or revelation.'
    stance: observation and reason
    certainty: 1.0
    cites:
    - source: S2
      locator: §3.2
    how_known: SEP quotation of MacAskill definition.
  reserved_exemptions:
    value: Not addressed as cosmology. Ethically, impartial concern (distance and nationality not morally
      relevant in the Singer/EA line) pushes against in-group exemptions.
    stance: none
    certainty: 0.7
    cites:
    - source: S2
      locator: §3.2
    how_known: Coder's reading of SEP on equal moral worth / distance.
  teleology_in_nature:
    value: Not addressed.
    stance: none
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica and SEP describe an ethics and movement; no theology.
  necessity_and_freedom:
    value: Not a free-will doctrine. Stresses individual agency to give, earn-to-give, and choose careers;
      critics note the individualist framing versus institutional change.
    certainty: 0.7
    cites:
    - source: S2
      locator: §3.2
    how_known: SEP on earning to give and institutional critique.
lio_axes:
  A_locus:
    value: UNKNOWN
    how_known: Movement states no cosmology; members differ (P44).
  B_cause:
    value: UNKNOWN
    how_known: Movement states no cosmology; members differ (P44).
  C_ledger:
    value: UNKNOWN
    how_known: Movement states no cosmology; members differ (P44).
  D_authority:
    value: 3
    rationale: Evidence and reason to maximize benefits; strong empiricism about interventions, but not
      a full natural-science cosmology, so not 4. Alt 4 if 'evidence and reason' is read as the LIO pole.
    certainty: 0.7
    cites:
    - source: S2
      locator: §3.2
    how_known: Scored from sourced authority stance (P44).
    alternatives:
    - value: 4
      cites:
      - source: S2
        locator: §3.2
      note: If evidence-and-reason definition counts as full observation/reason pole.
  E_scope:
    value: UNKNOWN
    how_known: Movement states no cosmology; members differ (P44).
epistemology:
  value: Use evidence and reason; charity evaluators (e.g. GiveWell), randomized trials and cost-effectiveness
    where available; expected-value reasoning under uncertainty (including longtermist risk).
  certainty: 1.0
  cites:
  - source: S2
    locator: §3.2
  how_known: SEP.
ethics:
  value: 'Maximize benefits to others on impartial, typically welfarist grounds. Britannica: identifying
    ways to benefit others and mobilizing resources; Giving What We Can urges ≥10% of income. SEP: Singer
    pond argument and equal moral worth across distance.'
  certainty: 1.0
  cites:
  - source: S1
    locator: opening; Historical developments
  - source: S2
    locator: §3.2
  how_known: Britannica and SEP.
practice:
  ritual_and_practice:
    value: Pledging (e.g. 10% of income), career choice including earning-to-give, donating to highly
      rated charities, cause prioritization. No religious ritual.
    certainty: 1.0
    cites:
    - source: S1
      locator: Historical developments
    - source: S2
      locator: §3.2
    how_known: Britannica and SEP.
  community_form:
    value: Movement with organizations (Giving What We Can, 80,000 Hours, Centre for Effective Altruism,
      GiveWell, Open Philanthropy) rather than a church. Academic and philanthropic networks.
    certainty: 1.0
    cites:
    - source: S2
      locator: §3.2
    how_known: SEP.
science:
  historical_stance:
    value: From the start, appeals to evidence about which interventions save or improve lives most; allied
      with development economics and charity evaluation.
    certainty: 1.0
    cites:
    - source: S2
      locator: §3.2
    how_known: SEP.
  current_stance:
    value: Continues evidence-based evaluation; longtermism shifts some attention to existential risk
      and future generations, with contested prediction problems. Not a natural-science research school.
    certainty: 0.7
    cites:
    - source: S2
      locator: §3.2
    how_known: SEP on longtermism and critics.
schools_and_variants:
- name: Global poverty / near-term EA
  form: modern
  how_it_differs: Focus on highly effective aid for currently living people (and often animals).
  lio_difference: Does not fix cosmology axes.
  certainty: 1.0
  cites:
  - source: S2
    locator: §3.2
- name: Earning to give
  form: modern
  how_it_differs: High-earning careers chosen to donate more to effective charities.
  lio_difference: Practice variant; axes unchanged.
  certainty: 1.0
  cites:
  - source: S2
    locator: §3.2
- name: Longtermism
  form: modern
  how_it_differs: Priority on influencing the far future and reducing existential risk (MacAskill 2022;
    Ord).
  lio_difference: Still no cosmology; shifts cause area.
  certainty: 1.0
  cites:
  - source: S1
    locator: Historical developments
  - source: S2
    locator: §3.2
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: TODO
v7_1_rubric:
  label: authorial v7.1 scores
  L: 10
  P: 10
  E: 9
  V: 10
  X: 8
  total: 47
  scoring_note: Effective Altruism is highly coherent, focusing on rational benevolence with strong empirical
    backing.
  source: v7.1 data book, section 6 table (tables[4]) row 12 and section 7 scoring notes
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
  use_when: The person was a founder, leader or committed member of the effective altruism movement.
  do_not_use_when: Charitable giving or utilitarian ethics alone is not EFFALT (Britannica separates it
    from utilitarianism); EFFALT sets no axes.
  neighbors:
  - code: UTIL
    relation: neighbor (easily confused)
  - code: SECHUM
    relation: neighbor (easily confused)
review:
  data_quality_flags: []
  open_questions:
  - Members' personal metaphysics still vary; axes stay UNKNOWN for the movement.
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Isabel Brodsky; Britannica Editors
  citation: Brodsky, Isabel, and the Editors of Encyclopaedia Britannica. "Effective altruism." Encyclopaedia
    Britannica. https://www.britannica.com/topic/effective-altruism.
  url: https://www.britannica.com/topic/effective-altruism
  accessed: '2026-10-25'
  reliability_note: Signed short article (author is a journalist). Article text only; AI-generated Top
    Questions ignored. SEP has no entry (404).
- id: S2
  type: tertiary
  kind: encyclopedia
  author: Theodore Lechterman; Emma Saunders-Hastings; Rob Reich
  year: 2024
  citation: Lechterman, Theodore, Emma Saunders-Hastings, and Rob Reich. "Philanthropy." Stanford Encyclopedia
    of Philosophy. First published November 12, 2024. https://plato.stanford.edu/entries/philanthropy/.
  url: https://plato.stanford.edu/entries/philanthropy/
  accessed: '2026-10-25'
  reliability_note: Peer-reviewed reference entry; EA treated in §3.2 Effective Altruism and Other Consequentialist
    Views.
---
# Effective Altruism (EFFALT)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44. The v7.1 scores and note are unchanged.

## Summary

Effective altruism is 'in ethics, a theory of conduct and a movement that centers on identifying ways to benefit others' [S1]. SEP: it 'invite[s] people to use evidence and reason to determine how to benefit others as much as possible' [S2]. Roots in Singer; MacAskill and Ord founded Giving What We Can in 2009 [S1].

## Core metaphysics

Not a theology. Authority is evidence and reason about interventions [S2]. Members may hold any God-view; the movement is silent [S1; S2].

## Position on the LIO axes

- **A, B, C, E:** UNKNOWN — no movement cosmology (P44).
- **D_authority: 3** (certainty 0.7; alternative 4) — evidence and reason [S2].

## Schools and variants

Near-term global poverty focus; earning to give; longtermism [S1; S2].

## Science

Evidence-based charity evaluation and expected-value reasoning; not a natural-science school [S2].

## Coding guidance

Movement members and founders. Charitable giving or utilitarian ethics alone is not EFFALT. Axes from the person when they state a metaphysics.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> EFFALT (47/50) — Effective Altruism. Effective Altruism is highly coherent, focusing on rational benevolence with strong empirical backing.

## Open questions

- Members' metaphysics.
- Adherents are TODO.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7 (score E on the world's order when the stub is filled).
- 2026-10-15 (systems batch S2): read Britannica; axes under P44.
- 2026-10-25: deepened from Britannica plus SEP Philanthropy §3.2; D_authority 3 (0.7); schools and practice filled.
