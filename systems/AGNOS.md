---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 6
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S1 for Jason)
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
    summary: 'Draft (systems batch S1): filled from SEP ("Atheism and Agnosticism", §2) and Britannica
      (Nielsen, "Atheism"). A is BELOW_THRESHOLD (explicit suspension); B, C and E UNKNOWN; D 4 at 0.5.
      v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'T2: B_cause searched, unchanged; search logged.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from SEP Atheism and Agnosticism (Draper) + Britannica atheism: family/parents,
      metaphysics TODOs as not addressed/none, epistemology/ethics/practice. Axes unchanged.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Review B/C/E: keep UNKNOWN (agnosticism does not affirm naturalism, ledger, or world-scope).
      Do not invent P44(c) fills.'
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
    how_known: "SEP defines it as a principle or as the psychological state of being an agnostic; coder's\
      \ classification, 0.7."
  family:
    value: 'Epistemological family: neither theism nor atheism is known (or lacks positive epistemic status);
      psychological sense = suspend judgment on God'
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: SEP.
  parent_traditions:
    value:
    - T.H. Huxley’s coinage (evidentialist principle)
    - Philosophy of religion epistemology
    - Psychological nontheism / theological skepticism
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: SEP.
  related_codes:
  - code: ATHE
    relation: neighbor (easily confused)
    note: Denial vs suspension; SEP prefers metaphysical ATHE
  - code: SCEPT
    relation: overlaps
    note: Broader skepticism
  - code: SECHUM
    relation: neighbor (easily confused)
    note: Secular life without God-claim
origins:
  founding_era:
    value: Term coined late 19th c. by T.H. Huxley; older skeptical practice
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: SEP.
  founding_region:
    value: Britain (Huxley); global philosophical use
    certainty: 0.7
    cites:
    - source: S1
      locator: §2
    how_known: '0.7.'
  founders_or_key_figures:
    value:
    - T.H. Huxley
    - Anthony Kenny
    - Robin Le Poidevin
    - J.L. Schellenberg (related skepticism)
    certainty: 1.0
    cites:
    - source: S1
      locator: §2; §4
    how_known: SEP.
  key_texts:
  - value: Huxley on agnosticism (1884/1889); Kenny Faith and Reason; Le Poidevin Agnosticism
    certainty: 1.0
    cites:
    - source: S1
      locator: §2; §4
    how_known: SEP.
metaphysics:
  god_nature_relation:
    value: "Suspended: 'an agnostic is a person who has entertained the proposition that there is a God\
      \ but believes neither that it is true nor that it is false'."
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: SEP.
  deity_personal:
    value: Not affirmed; question left open
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: SEP.
  intervention:
    value: Not affirmed or denied as a package; open
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: SEP.
  miracles:
    value: Not a required doctrine; evidential standards apply if claimed
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: SEP.
  petition_and_prayer:
    value: Not required by agnosticism as such
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: SEP.
  afterlife:
    value: Not settled by agnosticism about God
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: SEP.
  moral_ledger:
    value: Not a metaphysical commitment of agnosticism
    stance: none
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: SEP.
  authority:
    value: "Huxley's principle: 'it is wrong to say that one knows or believes that a proposition is true\
      \ without logically satisfactory evidence'; since neither theism nor atheism is adequately supported,\
      \ one should suspend judgement."
    stance: observation and reason
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: SEP paraphrase of Huxley 1884 and 1889.
  reserved_exemptions:
    value: No in-group exemption from evidence standards
    stance: none
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: SEP.
  teleology_in_nature:
    value: Not settled; open between design and non-design
    stance: none
    certainty: 1.0
    cites:
    - source: S1
      locator: §4
    how_known: SEP.
  necessity_and_freedom:
    value: Not a core agnostic commitment
    certainty: 0.7
    cites:
    - source: S1
      locator: §2
    how_known: '0.7.'
lio_axes:
  A_locus:
    value: 'BELOW_THRESHOLD'
    how_known: 'Explicit suspension on whether God exists (S1, §2), so no locus is held; as for persons
      (CODING_GUIDE §6, P20: an agnostic with no stated locus view is BELOW_THRESHOLD).'
    note: 'Evidence: the definition of agnosticism (S1 §2; S2 opening).'
  B_cause:
    value: 'UNKNOWN'
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: '0.7 — agnosticism withholds commitment; does not fix miracle doctrine, afterlife ledger,
      or world-scope.'
    rationale: Keep UNKNOWN. Not inventing naturalistic B4/C4/E4 from silence. Alternative BELOW if treating
      agnosticism as a family with theist/atheist members.
    alternatives:
    - value: 'BELOW_THRESHOLD'
      note: 'Named alternative: agnostic theists vs agnostic atheists disagree on B/C/E.'
      cites:
      - source: S1
        locator: opening
  C_ledger:
    value: 'UNKNOWN'
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: '0.7 — agnosticism withholds commitment; does not fix miracle doctrine, afterlife ledger,
      or world-scope.'
    rationale: Keep UNKNOWN. Not inventing naturalistic B4/C4/E4 from silence. Alternative BELOW if treating
      agnosticism as a family with theist/atheist members.
    alternatives:
    - value: 'BELOW_THRESHOLD'
      note: 'Named alternative: agnostic theists vs agnostic atheists disagree on B/C/E.'
      cites:
      - source: S1
        locator: opening
  D_authority:
    value: 4
    rationale: "Huxley's principle makes logically satisfactory evidence the condition for knowing or\
      \ believing, which leaves no independent authority to revelation."
    certainty: 0.5
    cites:
    - source: S1
      locator: §2
    how_known: '0–4 scale (P1). SEP does not mention revelation; inferred, so 0.5.'
  E_scope:
    value: 'UNKNOWN'
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: '0.7 — agnosticism withholds commitment; does not fix miracle doctrine, afterlife ledger,
      or world-scope.'
    rationale: Keep UNKNOWN. Not inventing naturalistic B4/C4/E4 from silence. Alternative BELOW if treating
      agnosticism as a family with theist/atheist members.
    alternatives:
    - value: 'BELOW_THRESHOLD'
      note: 'Named alternative: agnostic theists vs agnostic atheists disagree on B/C/E.'
      cites:
      - source: S1
        locator: opening
epistemology:
  value: Neither theism nor atheism known (modest); or neither has positive epistemic status (ambitious);
    psychological sense = suspend judgment; global vs local scopes
  certainty: 1.0
  cites:
  - source: S1
    locator: §2–4
  how_known: SEP.
ethics:
  value: No single ethics; Huxley’s principle is epistemic; living without dogmatic God-claims compatible
    with many moral views
  certainty: 0.7
  cites:
  - source: S1
    locator: §2
  how_known: '0.7.'
practice:
  ritual_and_practice:
    value: No required ritual; may include religious practice with suspended belief (fideism contrast)
    certainty: 0.7
    cites:
    - source: S1
      locator: §2
    how_known: '0.7.'
  community_form:
    value: No single community; overlapping secular and religious-skeptical milieux
    certainty: 0.7
    cites:
    - source: S1
      locator: §2
    how_known: '0.7.'
science:
  historical_stance:
    value: Huxley tied agnosticism to scientific evidential norms
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: SEP.
  current_stance:
    value: Common default in surveys of belief; philosophical debate continues
    certainty: 0.7
    cites:
    - source: S1
      locator: §2
    - source: S2
      locator: introduction
    how_known: '0.7.'
schools_and_variants:
- name: Psychological agnosticism
  form: popular
  how_it_differs: Suspend judgment on God; neither theist nor atheist
  lio_difference: Not rescored
  certainty: 1.0
  cites:
  - source: S1
    locator: §2
- name: Epistemological agnosticism
  form: scholastic or philosophical
  how_it_differs: Claim that neither theism nor atheism is known / justified
  lio_difference: Not rescored
  certainty: 1.0
  cites:
  - source: S1
    locator: §2
- name: Strong / weak variants
  form: scholastic or philosophical
  how_it_differs: From modest “not known” to “no positive epistemic status”
  lio_difference: Not rescored
  certainty: 1.0
  cites:
  - source: S1
    locator: §2; §7
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Common survey category; share varies by country (not a single census figure in S1)
    certainty: 0.5
    cites:
    - source: S1
      locator: §2
    how_known: Coder gloss. 0.5.
v7_1_rubric:
  label: authorial v7.1 scores
  L: 10
  P: 10
  E: 10
  V: 10
  X: 9
  total: 49
  scoring_note: 'Agnosticism promotes intellectual humility, scoring near-perfect for its evidence-based
    skepticism and avoidance of unsubstantiated commitments.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 2 and section 7 scoring notes'
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
  use_when: 'Person suspends judgment on God, or holds that neither theism nor atheism is known/justified.'
  do_not_use_when: Positive denial of God (→ ATHE); confident theism; mere “spiritual but not religious”
    without God-question stance.
  neighbors:
  - code: ATHE
    relation: neighbor (easily confused)
    note: Denial vs suspension
  - code: SCEPT
    relation: overlaps
    note: Broader
  - code: SECHUM
    relation: neighbor (easily confused)
    note: Life stance may differ
review:
  data_quality_flags: []
  open_questions:
  - Keep psychological vs epistemological AGNOS as one code?
  - Score A/B as BELOW_THRESHOLD for suspension?
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Paul Draper
  year: 2022
  citation: 'Draper, Paul. "Atheism and Agnosticism." Stanford Encyclopedia of Philosophy. First published
    August 2, 2017; substantive revision March 22, 2022. https://plato.stanford.edu/entries/atheism-agnosticism/.'
  url: 'https://plato.stanford.edu/entries/atheism-agnosticism/'
  accessed: '2026-10-25'
  reliability_note: Peer-reviewed reference entry.
- id: S2
  type: tertiary
  kind: encyclopedia
  author: Kai E. Nielsen
  citation: 'Nielsen, Kai E. "Atheism." Encyclopaedia Britannica, updated 16 September 2026. https://www.britannica.com/topic/atheism.'
  url: 'https://www.britannica.com/topic/atheism'
  accessed: '2026-10-25'
  reliability_note: Signed reference article (with Britannica Editors). Article paragraphs only; the AI-generated
    Top Questions boxes were ignored.
---
# Agnosticism (AGNOS)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44. The v7.1 scores and note are unchanged.

## Summary

Huxley’s term: evidential restraint on God-claims; psychological suspension of judgment; epistemological claim that neither theism nor atheism is known [S1].

## Core metaphysics

Not a positive metaphysics; leaves God-nature, afterlife, teleology open [S1].

## Position on the LIO axes

Prior scores unchanged this pass.

## Schools and variants

Psychological vs epistemological; strong vs weak [S1].

## Science

Tied to evidential / scientific norms in Huxley’s usage [S1].

## Coding guidance

Suspend judgment / “not known” → AGNOS. Denial → ATHE.

## v7.1 scoring note

Authorial v7.1 note unchanged (see front matter).

## Open questions

- One code for psych + epistemic senses?
- A/B BELOW_THRESHOLD for suspension?

## Research log

- Prior partial fills.
- 2026-10-25: deepened from SEP Atheism and Agnosticism; axes unchanged.
- B_cause / C_ledger / E_scope intentionally UNKNOWN (2026-10-25): do not invent naturalism from silence.
