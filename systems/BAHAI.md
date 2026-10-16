---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 5
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S7 for Jason)
  model_used: Grok Bot executor agent; direct reads of the cited pages
  collected_on: 2026-10-01
  last_updated: '2026-10-15'
  change_log:
  - date: 2026-10-01
    by: scripts/make_system_stubs.py
    summary: Stub created from v7.1 data book table 4 and section 7.
  - date: 2026-10-02
    by: scripts/make_system_stubs.py
    summary: 'Decision P7: E_scope note added. E is not scored in a stub; when it is, score it on the world''s order (same rules for every kind of being and event, no in-group exceptions in this-world events). Salvation and moral community go on C_ledger.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'Draft (systems batch S7): filled from the Britannica article body ("Bahāʾī Faith", editors, revised by Charles Preston). A 0 (0.5, alt 1); D 1 (0.5, alt 2); B, C, E UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S7 audit fix: Wayback snapshot URL and timestamp cited under P44(e).'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'T1: B_cause searched, still UNKNOWN; search logged.'
identity:
  id: BAHAI
  v7_1_number: 39
  v7_1_label: Bahá’í Faith
  display_label: Bahá’í Faith
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: religion
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: '''universalist religion''.'
  family:
    value: TODO
  parent_traditions:
    value: TODO
  related_codes: []
origins:
  founding_era:
    value: Mid-19th century (the Bāb 1844; Bahāʾu’llāh declared 1863)
    certainty: 1.0
    cites:
    - source: S1
      locator: History
    how_known: Britannica.
  founding_region:
    value: Iran; publicly declared in Iraq
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: Britannica.
  founders_or_key_figures:
    value:
    - The Bāb
    - Bahāʾu’llāh
    - ʿAbd al-Bahāʾ
    - Shoghi Effendi Rabbānī
    certainty: 1.0
    cites:
    - source: S1
      locator: History
    how_known: Britannica.
  key_texts: []
metaphysics:
  god_nature_relation:
    value: Bahāʾu’llāh and the Bāb 'were manifestations of God, who in his essence is unknowable'.
    stance: creator distinct from creation
    certainty: 0.7
    cites:
    - source: S1
      locator: introduction
    how_known: Britannica; creator status is not stated in the article.
  deity_personal:
    value: TODO
    stance: TODO
  intervention:
    value: TODO
    stance: TODO
  miracles:
    value: TODO
    stance: TODO
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
    value: '''The writings and spoken words of the Bāb, Bahāʾu’llāh, and ʿAbd al-Bahāʾ form the sacred literature''; the Universal House of Justice ''applies the laws promulgated by Bahāʾu’llāh and legislates on matters not covered in the sacred texts''.'
    stance: revelation
    certainty: 1.0
    cites:
    - source: S1
      locator: Practices; Organization
    how_known: Britannica.
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
    value: 0
    rationale: God 'in his essence is unknowable' and acts through manifestations, 'agents of a progressive divine plan'.
    certainty: 0.5
    cites: &id001
    - source: S1
      locator: introduction
    how_known: '0.5: transcendence is stated; personhood is the coder’s reading of the divine plan. Alternative 1.'
    alternatives:
    - value: 1
      note: Named alternative.
      cites: *id001
  B_cause:
    value: UNKNOWN
    how_known: Not fixed by the sources read (T1 search logged, 2026-10-15).
  C_ledger:
    value: UNKNOWN
    how_known: Not addressed in the sources read.
  D_authority:
    value: 1
    rationale: Sacred literature from the founders; the Universal House of Justice applies their laws and legislates where the texts are silent.
    certainty: 0.5
    cites: &id002
    - source: S1
      locator: Practices; Organization
    how_known: '0.5: the article does not discuss reason or science. Alternative 2.'
    alternatives:
    - value: 2
      note: Named alternative.
      cites: *id002
  E_scope:
    value: UNKNOWN
    how_known: Not addressed in the sources read.
epistemology:
  value: TODO
ethics:
  value: TODO
practice:
  ritual_and_practice:
    value: '''The faith has no priesthood and does not observe ritual forms in its worship''; daily prayer, a 19-day fast and the Nineteen Day Feast.'
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction; Practices
    how_known: Britannica.
  community_form:
    value: TODO
science:
  historical_stance:
    value: TODO
  current_stance:
    value: TODO
schools_and_variants: []
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: TODO
v7_1_rubric:
  label: authorial v7.1 scores
  L: 8
  P: 8
  E: 7
  V: 6
  X: 5
  total: 34
  scoring_note: Bahá’í Faith scores moderately high due to its innovative emphasis on global unity and progressive revelation, fostering ethical and social coherence, but constrained by revelatory authority over full empirical alignment.
  source: v7.1 data book, section 6 table (tables[4]) row 39 and section 7 scoring notes
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
  use_when: The person self-identifies as Bahāʾī.
  do_not_use_when: Universalist sympathy alone is not BAHAI.
  neighbors: []
review:
  data_quality_flags: []
  open_questions:
  - A source on reason, science and miracles in Bahāʾī teaching (B, D).
  - Adherents are TODO.
  - 'T1 (2026-10-15): B_cause search logged in the research log; still UNKNOWN.'
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Britannica Editors
  citation: 'The Editors of Encyclopaedia Britannica. "Bahāʾī Faith." Encyclopaedia Britannica (most recently revised and updated by Charles Preston). https://www.britannica.com/topic/Bahai-Faith. Wayback Machine snapshot 2026-10-11 10:55:53 UTC: https://web.archive.org/web/20261011105553/https://www.britannica.com/topic/Bahai-Faith.'
  url: https://www.britannica.com/topic/Bahai-Faith
  accessed: '2026-10-15'
  reliability_note: 'Unsigned editors’ article; article body only (AI Top Questions ignored). P44(e): read in the Wayback copy (https://web.archive.org/web/20261011105553/https://www.britannica.com/topic/Bahai-Faith), counted as the full article, no P45 cap. Live page timed out on 2026-10-15, so no live comparison; byline in the copy: Britannica Editors.'
---

# Bahá’í Faith (BAHAI)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

The Bahāʾī Faith is a 'universalist religion founded in the mid-19th century'; its cornerstone is that Bahāʾu’llāh and the Bāb 'were manifestations of God, who in his essence is unknowable' [S1].

## Core metaphysics

Unknowable God; progressive revelation through manifestations [S1].

## Position on the LIO axes

- A 0 (0.5, alt 1); D 1 (0.5, alt 2).
- B, C, E UNKNOWN.

## Schools and variants

TODO

## Science

TODO

## Coding guidance

Self-identified Bahāʾīs.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> BAHAI (34/50) — Bahá’í Faith. Bahá’í Faith scores moderately high due to its innovative emphasis on global unity and progressive revelation, fostering ethical and social coherence, but constrained by revelatory authority over full empirical alignment.

## Open questions

- B and D sources.
- Adherents are TODO.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7 (score E on the world's order when the stub is filled).
- 2026-10-15 (systems batch S7): read the listed sources; quotations checked word for word against the fetched page text. Britannica pages read in their full Wayback Machine copies (curl and WebFetch time out on the live site); Britannica AI Top Questions not used.
- 2026-10-15 (S7 audit fix): P44(e) Wayback citation.
- 2026-10-15 (targeted A/B pass, batch T1): searched the sources below for a statement fixing B_cause; quotations checked word for word against fetched page text. BAHAI: Britannica 'Bahāʾī Faith' (Wayback 20261011105553) read: byline 'Britannica Editors' (unsigned) and no passage on science, reason or miracles. No signed source found; Iranica 'Bahaism' listed as external lead. B stays UNKNOWN.
