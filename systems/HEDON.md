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
    value: Not addressed.
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: SEP treats hedonism as a theory of value and motivation.
  deity_personal:
    value: Not addressed as cosmology; value/ethics theory only.
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: 'SEP treats hedonism as theories of motivation and value, not cosmology.'
  intervention:
    value: Not addressed as cosmology; value/ethics theory only.
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: 'SEP treats hedonism as theories of motivation and value, not cosmology.'
  miracles:
    value: Not addressed as cosmology; value/ethics theory only.
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: 'SEP treats hedonism as theories of motivation and value, not cosmology.'
  petition_and_prayer:
    value: Not addressed as cosmology; value/ethics theory only.
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: 'SEP treats hedonism as theories of motivation and value, not cosmology.'
  afterlife:
    value: Not addressed as cosmology; value/ethics theory only.
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: 'SEP treats hedonism as theories of motivation and value, not cosmology.'
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
    value: 'Not addressed as cosmology. Ethically, qualitative hedonism (Mill) ranks pleasures but does
      not exempt an in-group from natural law.'
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: §2.1
    how_known: "Coder's reading; metaphysics neglected."
  teleology_in_nature:
    value: "Not addressed as design. Pleasure and pain are treated as natural governors of human conduct\
      \ (Bentham), not as a designer's purposes."
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: introduction
    how_known: "Coder's reading of Bentham opening; teleology stance is a label."
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
    value: 'UNKNOWN'
    how_known: 'SEP: hedonism is a theory of motivation and value, not a cosmology (P44).'
  B_cause:
    value: 'UNKNOWN'
    how_known: 'SEP: hedonism is a theory of motivation and value, not a cosmology (P44).'
  C_ledger:
    value: 'UNKNOWN'
    how_known: 'SEP: hedonism is a theory of motivation and value, not a cosmology (P44).'
  D_authority:
    value: 3
    rationale: "Observation and reason (experience of pleasure/pain, reasoned comparison) rather than\
      \ revelation; not a full natural-science empiricism programme, so not 4. Alt 4 if Bentham's naturalism\
      \ is read as the LIO pole."
    certainty: 0.7
    cites:
    - source: S1
      locator: introduction; §2.1
    how_known: Scored from sourced authority stance; other axes stay UNKNOWN (P44).
    alternatives:
    - value: 4
      cites:
      - source: S1
        locator: introduction
      note: "If Bentham's natural masters claim is read as full observation/reason pole."
  E_scope:
    value: 'UNKNOWN'
    how_known: 'SEP: hedonism is a theory of motivation and value, not a cosmology (P44).'
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
- name: Psychological (motivational) hedonism
  form: scholastic or philosophical
  how_it_differs: 'Only pleasure or pain motivates (or determines action, in stronger forms).'
  lio_difference: Does not fix LIO cosmology axes.
  certainty: 1.0
  cites:
  - source: S1
    locator: §1
- name: Ethical (evaluative) hedonism
  form: scholastic or philosophical
  how_it_differs: Only pleasure has non-instrumental worth; only pain has disvalue. Quantitative (Bentham)
    vs qualitative (Mill) variants.
  lio_difference: Does not fix LIO cosmology axes.
  certainty: 1.0
  cites:
  - source: S1
    locator: §2
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
