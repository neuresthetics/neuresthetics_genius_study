---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 8
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
    summary: 'Draft (systems batch S5): filled from SEP "Hedonism" (Moore). All axes UNKNOWN: a theory
      of value and motivation. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities: family, parents, related codes, remaining metaphysics (not addressed),
      epistemology, practice, science, schools (psychological vs ethical; Bentham/Mill). Axes stay UNKNOWN
      (value theory). Source: SEP Moore.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Fill adherents/estimate gloss from existing sources (order-of-magnitude / qualitative). Axes
      unchanged.
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score A_locus 4 and C_ledger 4 (0.7); raise D_authority 3→4 (0.7) from SEP Hedonism (value
      theory; no deity/ledger; experience).
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Fill implied axes (B=4@0.5, E=4@0.5) from sources on file / P44(c) where naturalistic. Alternatives
      named.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Clarify cosmology silence and teleology/exemptions from Wikipedia Hedonism; note Epicurean
      cousin ≠ the label. No LIO moves.
identity:
  id: HEDON
  v7_1_number: 32
  v7_1_label: Hedonism
  display_label: Hedonism
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: family of positions
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: Psychological and ethical hedonism (SEP).
  family:
    value: Theories of motivation and of value centered on pleasure and pain
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP introduction.
  parent_traditions:
    value:
    - Ancient Greek ethics (Epicurus)
    - 'British moral philosophy (Bentham, Mill, Sidgwick)'
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP lists key contributors across those lines.
  related_codes:
  - code: EPICUR
    relation: neighbor (easily confused)
    note: ancient school with a full physics; HEDON is the value thesis alone
  - code: UTIL
    relation: overlaps
    note: classical utilitarianism is often hedonistic; code UTIL when maximizing aggregate welfare is
      the frame
  - code: CYNIC
    relation: contrast case
    note: virtue/askēsis vs pleasure as sole value
origins:
  founding_era:
    value: Debate runs from ancient Greece through Bentham; modern analytic formulations continue after
      Mill and Sidgwick
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP.
  founding_region:
    value: Greek Mediterranean; later Britain and analytic philosophy broadly
    certainty: 0.7
    cites:
    - source: S1
      locator: introduction
    how_known: "Coder's geographic gloss on SEP's cast of contributors."
  founders_or_key_figures:
    value:
    - Epicurus
    - Jeremy Bentham
    - John Stuart Mill
    - Henry Sidgwick
    certainty: 0.7
    cites:
    - source: S1
      locator: introduction; §1
    how_known: SEP lists contributors to the debate; 0.7.
  key_texts:
  - value: An Introduction to the Principles of Morals and Legislation
    author: Jeremy Bentham
    year: 1789
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: "SEP opens with Bentham's two sentences."
  - value: Utilitarianism
    author: John Stuart Mill
    year: 1863
    certainty: 1.0
    cites:
    - source: S1
      locator: §2.1
    how_known: SEP on qualitative hedonism.
metaphysics:
  god_nature_relation:
    value: 'Not addressed. Hedonism is a family of value/psychology/ethics theses about pleasure and pain,
      not a theology of God and Nature. (Epicureanism is a related but distinct code with atomist cosmology.)'
    stance: not addressed
    certainty: 0.7
    cites: &id001
    - source: S2
      locator: opening; Ethical hedonism
    how_known: '0.7 — Wikipedia treats hedonism as pleasure theory, not religion.'
  deity_personal:
    value: 'Not addressed as cosmology; hedonism is a value/ethics (and sometimes psychology) theory.
      Distinct from Epicurean physics, which denies afterlife anxiety.'
    stance: not addressed
    certainty: 0.7
    cites: *id001
    how_known: '0.7 — Wikipedia scope of hedonism.'
  intervention:
    value: 'Not addressed as cosmology; hedonism is a value/ethics (and sometimes psychology) theory.
      Distinct from Epicurean physics, which denies afterlife anxiety.'
    stance: not addressed
    certainty: 0.7
    cites: *id001
    how_known: '0.7 — Wikipedia scope of hedonism.'
  miracles:
    value: 'Not addressed as cosmology; hedonism is a value/ethics (and sometimes psychology) theory.
      Distinct from Epicurean physics, which denies afterlife anxiety.'
    stance: not addressed
    certainty: 0.7
    cites: *id001
    how_known: '0.7 — Wikipedia scope of hedonism.'
  petition_and_prayer:
    value: 'Not addressed as cosmology; hedonism is a value/ethics (and sometimes psychology) theory.
      Distinct from Epicurean physics, which denies afterlife anxiety.'
    stance: not addressed
    certainty: 0.7
    cites: *id001
    how_known: '0.7 — Wikipedia scope of hedonism.'
  afterlife:
    value: 'Not addressed as cosmology; hedonism is a value/ethics (and sometimes psychology) theory.
      Distinct from Epicurean physics, which denies afterlife anxiety.'
    stance: not addressed
    certainty: 0.7
    cites: *id001
    how_known: '0.7 — Wikipedia scope of hedonism.'
  moral_ledger:
    value: No divine judge. Value is pleasure and disvalue is pain; no personal afterlife ledger is part
      of the thesis.
    stance: none
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction; §2
    how_known: 'SEP ethical hedonism is about value, not reward theology.'
  authority:
    value: 'Not a theory of revelation or tradition. Bentham and Mill argue from nature, experience, and
      reasoned comparison of pleasures; no sacred text is the authority.'
    stance: observation and reason
    certainty: 0.7
    cites:
    - source: S1
      locator: introduction; §2.1
    how_known: "Coder's reading of Bentham/Mill material in SEP; certainty 0.7 because authority is not\
      \ SEP's topic."
  reserved_exemptions:
    value: 'None as cosmology. Ethically, qualitative hedonism (Mill) ranks kinds of pleasure but does
      not exempt an in-group from the pleasure/pain standard.'
    stance: none
    certainty: 0.7
    cites: *id001
    how_known: '0.7 — Wikipedia qualitative vs quantitative.'
  teleology_in_nature:
    value: 'Not designer teleology. Bentham treats pleasure and pain as natural governors of conduct;
      that is motivational psychology, not cosmic purpose.'
    stance: none
    certainty: 0.7
    cites: *id001
    how_known: '0.7 — Wikipedia / Bentham framing in sources.'
  necessity_and_freedom:
    value: "Not a free-will doctrine. Psychological hedonism is a claim about what motivates; ethical\
      \ hedonism is about value. Agency weaknesses and the 'paradox of hedonism' are discussed without\
      \ a metaphysics of freedom."
    certainty: 0.7
    cites:
    - source: S1
      locator: §1
    how_known: SEP §1.
lio_axes:
  A_locus:
    value: 4
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: '0.7 — value/ethics theory; no cosmology of God; P44a.'
    rationale: 'A=4: no God in the thesis. Not UNKNOWN: silence on deity plus value-only scope fixes absence
      for the system-as-such.'
    alternatives:
    - value: 'UNKNOWN'
      note: Named alternative if coding only as silent on God.
      cites:
      - source: S1
        locator: opening
  B_cause:
    value: 4
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — value theory; no miracle doctrine.'
    rationale: B=4 at 0.5.
    alternatives:
    - value: 'UNKNOWN'
      note: Named alternative if refusing P44(c) implied score.
      cites:
      - source: S1
        locator: opening
  C_ledger:
    value: 4
    certainty: 0.7
    cites:
    - source: S1
      locator: Ethical hedonism
    how_known: '0.7 — value is pleasure/pain; no personal afterlife ledger.'
    rationale: 'C=4: none. Not 3: not karma.'
    alternatives:
    - value: 3
      note: Named alternative if reading pleasure/pain as impersonal moral law.
      cites:
      - source: S1
        locator: Ethical hedonism
  D_authority:
    value: 4
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: '0.7 — experience of pleasure/pain; Bentham/Mill; stance observation and reason.'
    rationale: 'D=4: experience over revelation. Raised from 3.'
    alternatives:
    - value: 3
      note: Named alternative if weighting Aristippus/Epicurus school variance.
      cites:
      - source: S1
        locator: opening
  E_scope:
    value: 4
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — pleasure/pain as general value facts.'
    rationale: E=4 at 0.5.
    alternatives:
    - value: 'UNKNOWN'
      note: Named alternative if refusing P44(c) implied score.
      cites:
      - source: S1
        locator: opening
epistemology:
  value: 'Pleasure and pain are known in experience; debates turn on whether pleasure is phenomenal, intentional,
    or both. Empirical psychology is invited for motivational claims; ethical claims use philosophical
    argument.'
  certainty: 0.7
  cites:
  - source: S1
    locator: §1; §2.1
  how_known: "Coder's reading of SEP on nature of pleasure and appraisal methods."
ethics:
  value: "'Ethical or evaluative hedonism claims that only pleasure has worth or value and only pain or\
    \ displeasure has disvalue'."
  certainty: 1.0
  cites:
  - source: S1
    locator: introduction
  how_known: SEP.
practice:
  ritual_and_practice:
    value: 'No ritual. Lived as a guide to choice: seek pleasure, avoid pain; Mill adds cultivation of
      higher pleasures. Not a church practice.'
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction; §2.1
    how_known: SEP.
  community_form:
    value: 'Philosophical position and ethical debate, not a membership community. Overlaps with utilitarian
      and Epicurean communities when those are the vehicle.'
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: 'SEP presents a family of theses, not a sect.'
science:
  historical_stance:
    value: Motivational hedonism is framed as an empirical psychological thesis that should face meta-analyses
      and specialist science; ethical hedonism is philosophical.
    certainty: 1.0
    cites:
    - source: S1
      locator: §1.2 (closing)
    how_known: SEP.
  current_stance:
    value: Ongoing debate in philosophy of value and well-being; empirical psychology continues to test
      motivational claims. Not a scientific school.
    certainty: 0.7
    cites:
    - source: S1
      locator: §3
    how_known: "Coder's reading of SEP concluding remarks."
schools_and_variants:
- name: Psychological hedonism
  form: scholastic or philosophical
  how_it_differs: Descriptive claim that motivation is pleasure/pain maximization (egoistic reading common).
  lio_difference: Axes as scored for the label; not a religion.
  certainty: 0.7
  cites: *id001
- name: Ethical / axiological hedonism (Bentham quantitative; Mill qualitative)
  form: scholastic or philosophical
  how_it_differs: 'Normative: only pleasure has intrinsic value; Mill adds quality ranking.'
  lio_difference: Little axis change.
  certainty: 0.7
  cites: *id001
- name: Utilitarian vs egoistic ethical hedonism
  form: scholastic or philosophical
  how_it_differs: 'Whose pleasure counts: everyone (utilitarian) vs agent only (egoistic).'
  lio_difference: E-scope ethical read may shift; LIO kept for label.
  certainty: 0.7
  cites: *id001
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: 'Philosophical position, not a membership body; debated across history (Bentham, Mill, etc.)'
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: '0.7 — qualitative from listed source; not a genius-rate denominator.'
v7_1_rubric:
  label: authorial v7.1 scores
  L: 8
  P: 8
  E: 9
  V: 9
  X: 7
  total: 41
  scoring_note: 'Hedonism scores relatively high for its empirical ties to human psychology and consistent
    pleasure-based ethics, offering practical guidance for well-being, but limited by potential oversimplification
    of complex motivations.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 32 and section 7 scoring notes'
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
  use_when: "The person's own writing makes pleasure the only intrinsic value as the main worldview."
  do_not_use_when: Ancient Epicureans are EPICUR; utilitarians are UTIL. HEDON sets no axes.
  neighbors:
  - code: EPICUR
    relation: neighbor (easily confused)
  - code: UTIL
    relation: neighbor (easily confused)
review:
  data_quality_flags: []
  open_questions:
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Andrew Moore
  year: 2013
  citation: 'Andrew Moore. "Hedonism." Stanford Encyclopedia of Philosophy. First published April 20,
    2004; substantive revision October 17, 2013. https://plato.stanford.edu/entries/hedonism/.'
  url: 'https://plato.stanford.edu/entries/hedonism/'
  accessed: '2026-10-25'
  reliability_note: Peer-reviewed reference entry.
- id: S2
  type: tertiary
  kind: encyclopedia
  citation: 'Wikipedia contributors. "Hedonism." Wikipedia. Accessed 2026-10-25.'
  url: 'https://en.wikipedia.org/wiki/Hedonism'
  accessed: '2026-10-25'
---
# Hedonism (HEDON)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44. The v7.1 scores and note are unchanged.

## Summary

'Psychological or motivational hedonism claims that only pleasure or pain motivates us. Ethical or evaluative hedonism claims that only pleasure has worth or value and only pain or displeasure has disvalue' [S1]. Bentham asserted both in the opening of *Principles of Morals and Legislation* [S1].

## Core metaphysics

Not a cosmology. Pleasure and pain are natural governors of conduct for Bentham; no God, miracle, or afterlife doctrine is part of the thesis [S1]. Authority is observation and reason rather than revelation [S1].

## Position on the LIO axes

- **A, B, C, E:** UNKNOWN — value/motivation theory, not cosmology (P44).
- **D_authority: 3** (certainty 0.7; alternative 4) — experience and reasoned comparison of pleasures [S1].

## Schools and variants

Psychological vs ethical hedonism; quantitative (Bentham) vs qualitative (Mill) within ethical hedonism [S1].

## Science

Motivational claims invite empirical psychology; ethical claims remain philosophical [S1].

## Coding guidance

EPICUR and UTIL first when those schools are the person's frame. HEDON is the pleasure-as-sole-value thesis.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> HEDON (41/50) — Hedonism. Hedonism scores relatively high for its empirical ties to human psychology and consistent pleasure-based ethics, offering practical guidance for well-being, but limited by potential oversimplification of complex motivations.

## Open questions

- Adherents are TODO (philosophical thesis, not a census religion).

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7 (score E on the world's order when the stub is filled).
- 2026-10-15 (systems batch S5): read the listed sources; quotations checked word for word against the fetched page text with a script. Britannica Top Questions (AI-generated) not used. Axes under P44.
- 2026-10-25: deepened classification, metaphysics TODOs, epistemology, practice, science, schools; D_authority 3 (0.7). Re-read SEP Moore.
- 2026-10-25: adherents/estimate filled (qualitative).
- 2026-10-25: A/C scored; D raised to 4.
- 2026-10-25: implied axis fill: B=4@0.5, E=4@0.5.
- 2026-10-25: Clarified cosmology silence; schools from Wikipedia Hedonism.
