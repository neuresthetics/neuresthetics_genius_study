---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 8
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
    summary: 'Draft (systems batch S4): filled from SEP "The History of Utilitarianism" (Driver). A BELOW_THRESHOLD
      (theological and secular utilitarians); others UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S10 audit fix: A how_known repeats the source quote.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities: family/parents/related codes, origins era/region, metaphysics TODOs, epistemology,
      practice, science, schools (classical, theological, ideal). LIO axes unchanged. Re-read SEP History
      of Utilitarianism.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score D_authority 3 (0.7) from SEP History of Utilitarianism (secular classical reason/reform).
      Enrich related codes (EFFALT). Axes A stays BELOW_THRESHOLD; B/C/E UNKNOWN.
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Fill implied axes (C=4@0.5, E=4@0.5, B=4@0.5) from sources on file / P44(c) where naturalistic.
      Alternatives named.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Fill miracles from Wikipedia Utilitarianism. No LIO moves.
identity:
  id: UTIL
  v7_1_number: 24
  v7_1_label: Utilitarianism
  display_label: Utilitarianism
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: philosophical school or method
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: "An approach to normative ethics, 'a species of consequentialism'."
  family:
    value: Consequentialist normative ethics (utilitarian species)
    certainty: 1.0
    cites: &id001
    - source: S1
      locator: introduction
    how_known: 'SEP: species of consequentialism.'
  parent_traditions:
    value:
    - British moralists / theological utilitarians
    - 'Classical secular utilitarianism (Bentham, Mill, Sidgwick)'
    - Later ideal utilitarianism (Moore)
    certainty: 1.0
    cites:
    - source: S1
      locator: §1–4
    how_known: SEP structure.
  related_codes:
  - code: EPICUR
    relation: neighbor (easily confused)
    note: Hedonism about pleasure vs utilitarian moral decision procedure
  - code: PRAG
    relation: neighbor (easily confused)
    note: Pragmatism is not the same as maximizing utility
  - code: HEDON
    relation: overlaps
    note: Classical utilitarianism is hedonistic about value; not all hedonism is utilitarian
  - code: EFFALT
    relation: overlaps
    note: Effective altruism as evidence-based utilitarian-adjacent movement
  - code: SECHUM
    relation: overlaps
    note: Secular humanist consequentialism neighbor
origins:
  founding_era:
    value: 'Classical form late 18th–19th c. (Godwin, Bentham, Mill, Sidgwick); precursors earlier (Hutcheson,
      theological utilitarians, Mozi noted)'
    certainty: 1.0
    cites: *id001
    how_known: SEP.
  founding_region:
    value: Britain (classical core); precursors noted in China and India in SEP
    certainty: 1.0
    cites: *id001
    how_known: SEP.
  founders_or_key_figures:
    value:
    - Jeremy Bentham
    - John Stuart Mill
    - Henry Sidgwick
    - William Paley
    certainty: 1.0
    cites:
    - source: S1
      locator: §1–3
    how_known: SEP.
  key_texts:
  - value: 'Bentham, Introduction to the Principles of Morals and Legislation'
    certainty: 1.0
    cites:
    - source: S1
      locator: §2.2
    how_known: SEP.
  - value: 'Mill, Utilitarianism'
    certainty: 1.0
    cites:
    - source: S1
      locator: §2.3
    how_known: SEP.
  - value: 'Sidgwick, The Methods of Ethics'
    certainty: 1.0
    cites:
    - source: S1
      locator: §3
    how_known: SEP.
metaphysics:
  god_nature_relation:
    value: "Varies: theological utilitarians (Paley; Newcome: 'divine beneficence consists in God’s promotion\
      \ of happiness') and classical secular forms."
    stance: varies by school
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: SEP.
  deity_personal:
    value: 'Varies: theological utilitarians ground duty in God; classical forms are secular.'
    stance: varies by school
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: SEP.
  intervention:
    value: Not a shared miracle doctrine; ethical theory about consequences.
    stance: not addressed
    certainty: 1.0
    cites: *id001
    how_known: SEP.
  miracles:
    value: Not addressed. Utilitarianism is a consequentialist ethics about welfare; it has no miracle
      doctrine.
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S2
      locator: opening
    how_known: '0.5–0.7 — Wikipedia Utilitarianism.'
  petition_and_prayer:
    value: 'Not a cult; theological forms may pray, classical secular forms do not require it.'
    stance: not addressed
    certainty: 1.0
    cites: *id001
    how_known: SEP.
  afterlife:
    value: Theological utilitarians may tie salvation to conformity with God’s will; classical secular
      forms do not require afterlife.
    stance: varies by school
    certainty: 0.7
    cites:
    - source: S1
      locator: §1
    how_known: SEP on Gay/theological. 0.7.
  moral_ledger:
    value: This-world consequences of actions/policies; not a divine hell ledger as the defining idea
      (though theological forms add God).
    stance: impersonal consequence
    certainty: 0.7
    cites: *id001
    how_known: "Coder's reading of consequentialist core. 0.7."
  authority:
    value: Reasoned calculation of consequences (utility); Mill adds internal sanctions/conscience.
    stance: observation and reason
    certainty: 0.7
    cites:
    - source: S1
      locator: §2
    how_known: SEP classical approach. 0.7.
  reserved_exemptions:
    value: Impartiality and agent-neutrality are core; everyone’s happiness counts the same.
    stance: none
    certainty: 0.7
    cites: *id001
    how_known: SEP introduction on impartiality. 0.7.
  teleology_in_nature:
    value: Not required; theological forms may read divine ends into happiness promotion.
    stance: varies by school
    certainty: 0.7
    cites:
    - source: S1
      locator: §1
    how_known: '0.7.'
  necessity_and_freedom:
    value: Not a shared free-will metaphysics; practical deliberation and sanctions matter in Mill/Sidgwick.
    certainty: 0.7
    cites:
    - source: S1
      locator: §2.3; §3
    how_known: '0.7.'
lio_axes:
  A_locus:
    value: 'BELOW_THRESHOLD'
    how_known: "Theological and secular utilitarians differ (S1): P44(b). Quote (S1, §1): Varies: theological\
      \ utilitarians (Paley; Newcome: 'divine beneficence consists in God’s promotion of happiness') and\
      \ classical secular forms."
    note: 'Evidence: S1 §1.'
  B_cause:
    value: 4
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — secular classical: no miracle doctrine.'
    rationale: B=4 at 0.5; theological util alt.
    alternatives:
    - value: 'BELOW_THRESHOLD'
      note: 'Named alternative: theological utilitarianism (Paley).'
      cites:
      - source: S1
        locator: §1
  C_ledger:
    value: 4
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — secular classical: consequences, not divine ledger.'
    rationale: C=4 at 0.5; Paley alt.
    alternatives:
    - value: 'BELOW_THRESHOLD'
      note: 'Named alternative: theological utilitarianism (Paley).'
      cites:
      - source: S1
        locator: §1
  D_authority:
    value: 3
    certainty: 0.7
    cites:
    - source: S1
      locator: §2; conclusion
    how_known: '0.7 — classical secular utilitarianism uses reason and consequences for law/policy; theological
      utilitarians add God’s will.'
    rationale: 'Observation and reason as moral decision method (Bentham/Mill); not revelation-first.
      3 not 4: theological utilitarians and internal sanctions complicate a clean 4.'
    alternatives:
    - value: 4
      note: Named alternative if coding only secular classical act-utilitarianism.
      cites:
      - source: S1
        locator: §2.2–2.3
    - value: 'UNKNOWN'
      note: Named alternative if coding Paley-style theological utilitarianism as primary.
      cites:
      - source: S1
        locator: §1
  E_scope:
    value: 4
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — impartiality; same rules for moral patients.'
    rationale: 'E=4 at 0.5 (careful: E is world order).'
    alternatives:
    - value: 'UNKNOWN'
      note: Named alternative if refusing P44(c) implied score.
      cites:
      - source: S1
        locator: opening
epistemology:
  value: Moral evaluation via expected or actual consequences for happiness/utility; Bentham’s felicific
    calculus parameters; experience and rules of thumb for efficiency.
  certainty: 1.0
  cites:
  - source: S1
    locator: §2.2
  how_known: SEP Bentham.
ethics:
  value: "'the moral quality of an action or policy is entirely a function of its consequences'."
  certainty: 1.0
  cites:
  - source: S1
    locator: introduction
  how_known: SEP.
practice:
  ritual_and_practice:
    value: 'Ethical and political method, not a church ritual system; aimed at law and social reform.'
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: SEP.
  community_form:
    value: Philosophical and reform movements; no single denomination.
    certainty: 1.0
    cites: *id001
    how_known: SEP.
science:
  historical_stance:
    value: 'Secular, forward-looking policy question “What use is it?”; influence on law and social policy.'
    certainty: 1.0
    cites:
    - source: S1
      locator: Conclusion
    how_known: SEP.
  current_stance:
    value: Ancestor of contemporary consequentialism; classical hedonism often refined or replaced.
    certainty: 1.0
    cites:
    - source: S1
      locator: Conclusion
    how_known: SEP.
schools_and_variants:
- name: Classical hedonistic utilitarianism
  form: scholastic or philosophical
  how_it_differs: Bentham/Mill/Sidgwick; maximize pleasure/happiness impartially
  lio_difference: Not rescored this pass
  certainty: 1.0
  cites:
  - source: S1
    locator: §2
- name: Theological utilitarianism
  form: scholastic or philosophical
  how_it_differs: Duty via God’s will/happiness of mankind
  lio_difference: May move A — family still varies
  certainty: 1.0
  cites:
  - source: S1
    locator: §1
- name: Ideal utilitarianism (Moore)
  form: scholastic or philosophical
  how_it_differs: Plural intrinsic goods beyond pleasure (e.g. beauty)
  lio_difference: Value theory shift — not LIO rescored
  certainty: 1.0
  cites:
  - source: S1
    locator: §4
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Not a census religion; ethical theory and policy influence
    certainty: 1.0
    cites: *id001
    how_known: SEP.
v7_1_rubric:
  label: authorial v7.1 scores
  L: 9
  P: 9
  E: 9
  V: 10
  X: 8
  total: 45
  scoring_note: 'Utilitarianism scores high for its empirical and rational approach to ethics, optimizing
    for collective good with practical applications, though slightly limited by measurement abstractions
    and potential oversimplification.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 24 and section 7 scoring notes'
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
  use_when: "The person's own writing adopts utilitarian ethics as the main worldview (Bentham, Mill)."
  do_not_use_when: UTIL sets no God-view; score axes from the person. Effective altruism members are EFFALT.
  neighbors:
  - code: HEDON
    relation: neighbor (easily confused)
    note: Pleasure as value ≠ full utilitarian decision theory
  - code: EPICUR
    relation: neighbor (easily confused)
    note: Ancient hedonist school vs modern utilitarianism
review:
  data_quality_flags: []
  open_questions:
  - Act vs rule utilitarianism coding for persons — same UTIL code?
  - Should theological utilitarians sometimes be dual-coded with a theism code?
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Julia Driver
  year: 2025
  citation: 'Julia Driver. "The History of Utilitarianism." Stanford Encyclopedia of Philosophy. First
    published March 27, 2009; substantive revision July 31, 2025. https://plato.stanford.edu/entries/utilitarianism-history/.'
  url: 'https://plato.stanford.edu/entries/utilitarianism-history/'
  accessed: '2026-10-25'
  reliability_note: Peer-reviewed reference entry.
- id: S2
  type: tertiary
  kind: encyclopedia
  citation: 'Wikipedia contributors. "Utilitarianism." Wikipedia. Accessed 2026-10-25.'
  url: 'https://en.wikipedia.org/wiki/Utilitarianism'
  accessed: '2026-10-25'
---
# Utilitarianism (UTIL)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44. The v7.1 scores and note are unchanged.

## Summary

Utilitarianism is a species of consequentialism: the moral quality of an action or policy is a function of its consequences [S1]. Classical forms maximize overall good impartially; for Bentham and Mill the value is pleasure/happiness [S1]. SEP also tracks theological precursors and Moore’s ideal utilitarianism [S1].

## Core metaphysics

Not a shared cosmology. Theological utilitarians ground duty in God; classical forms are secular [S1]. Moral evaluation runs through consequences (impersonal in structure), not a hell-court ledger as the defining idea.

## Position on the LIO axes

Axes left as previously coded (see front matter); this pass fills qualities/properties without rescoring.

## Schools and variants

Classical hedonistic utilitarianism; theological utilitarianism; ideal utilitarianism (Moore) [S1].

## Science

Forward-looking secular policy question “What use is it?” [S1].

## Coding guidance

Use for utilitarian / maximizing-consequentialist ethics. Mere hedonism about value may be HEDON; Epicurean school is EPICUR.

## v7.1 scoring note

Authorial v7.1 note unchanged (see front matter).

## Open questions

- Act vs rule utilitarianism coding for persons — same UTIL code?
- Should theological utilitarians sometimes be dual-coded with a theism code?

## Research log

- Prior fill from SEP History of Utilitarianism.
- 2026-10-25: deepened TODOs; re-read SEP.
- 2026-10-25: D_authority scored; EFFALT/SECHUM related; authority stance varies by school.
- 2026-10-25: implied axis fill: C=4@0.5, E=4@0.5, B=4@0.5.
- 2026-10-25: Filled miracles from Wikipedia Utilitarianism.
