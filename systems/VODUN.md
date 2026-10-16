---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 4
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S9 for Jason)
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
    summary: 'Draft (systems batch S10): filled from Britannica "Vodou" (McAlister). A 1 (0.5, alt 2); B 1 (0.5, alt 0); E 1 (0.5); C, D UNKNOWN. Covers Haitian Vodou; West African Vodun not described separately. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S10 audit fix: A, B and E scoped to Haitian Vodou; use_when scoped; West African Vodun lead.'
identity:
  id: VODUN
  v7_1_number: 57
  v7_1_label: Vodun (Voodoo/West African Vodun)
  display_label: Vodun (Voodoo/West African Vodun)
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: religion
    certainty: 1.0
    cites:
    - source: S1
      locator: article
    how_known: '''a traditional Afro-Haitian religion''.'
  family:
    value: TODO
  parent_traditions:
    value: TODO
  related_codes: []
origins:
  founding_era:
    value: 16th–17th centuries
    certainty: 0.7
    cites:
    - source: S1
      locator: article
    how_known: 'Britannica: enslaved people Christianized in the 16th and 17th centuries.'
  founding_region:
    value: Saint-Domingue (Haiti), from West and Central African religions
    certainty: 1.0
    cites:
    - source: S1
      locator: article
    how_known: Britannica.
  founders_or_key_figures:
    value: TODO
  key_texts: []
metaphysics:
  god_nature_relation:
    value: '''The God of the Christian Bible is understood to be the creator of both the universe and the spirits; the spirits were made by God to help him govern humanity and the natural world.'''
    stance: creator distinct from creation
    certainty: 1.0
    cites:
    - source: S1
      locator: article
    how_known: Britannica.
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
    value: TODO
    stance: TODO
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
    value: 1
    rationale: A creator God with spirits 'made by God to help him govern humanity and the natural world'; yet 'Its fundamental principle is that everything is spirit'.
    certainty: 0.5
    cites: &id001
    - source: S1
      locator: article
    how_known: '0.5: the everything-is-spirit principle gives alternative 2. Scope: Haitian Vodou only (S1); West African Vodun is not described.'
    alternatives:
    - value: 2
      note: Named alternative.
      cites: *id001
  B_cause:
    value: 1
    rationale: Prayers and rites 'in return for health, protection, and favour'; possessed devotees 'give supernaturally inspired advice to people, or perform medical cures or special physical feats'.
    certainty: 0.5
    cites: &id002
    - source: S1
      locator: article
    how_known: '0.5. Alternative 0. Scope: Haitian Vodou only (S1); West African Vodun is not described.'
    alternatives:
    - value: 0
      note: Named alternative.
      cites: *id002
  C_ledger:
    value: UNKNOWN
    how_known: Not addressed in the sources read.
  D_authority:
    value: UNKNOWN
    how_known: Not addressed in the sources read.
  E_scope:
    value: 1
    rationale: 'On the world''s order (P7): the spirits are served ''in return for health, protection, and favour'', and families ''inherit familial spirits''.'
    certainty: 0.5
    cites:
    - source: S1
      locator: article
    how_known: '0.5: favour for those who serve. Scope: Haitian Vodou only (S1); West African Vodun is not described.'
epistemology:
  value: TODO
ethics:
  value: TODO
practice:
  ritual_and_practice:
    value: TODO
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
  L: 7
  P: 6
  E: 5
  V: 5
  X: 3
  total: 26
  scoring_note: Vodun scores moderately due to its emphasis on spiritual balance and communal practices, offering rich cultural coherence but limited by supernatural elements and lack of empirical rigor.
  source: v7.1 data book, section 6 table (tables[4]) row 57 and section 7 scoring notes
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
  use_when: The person practised Haitian Vodou (the source read). West African Vodun shares the code (single code, as with TAO) but needs its own source.
  do_not_use_when: Haitian heritage alone is not enough; Santería is SANTER.
  neighbors: []
review:
  data_quality_flags:
  - Source covers Haitian Vodou; the Britannica "Vodun" page is an unsigned index stub, so West African Vodun has no separate source.
  open_questions:
  - 'Lead: a signed or peer-reviewed source on West African Vodun (Fon/Ewe, Benin and Togo), to check whether these values hold for it.'
  - A source on West African Vodun.
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Elizabeth A. McAlister; Britannica Editors
  citation: 'McAlister, Elizabeth A., and The Editors of Encyclopaedia Britannica. "Vodou." Encyclopaedia Britannica. https://www.britannica.com/topic/Vodou. Wayback Machine snapshot 2026-10-06 07:22:58 UTC: https://web.archive.org/web/20261006072258/https://www.britannica.com/topic/Vodou.'
  url: https://www.britannica.com/topic/Vodou
  accessed: '2026-10-15'
  reliability_note: 'Signed article (scholar of Haitian Vodou), full short article read. It covers Haitian Vodou; West African Vodun appears only as its source. P44(e): read in the Wayback copy (https://web.archive.org/web/20261006072258/https://www.britannica.com/topic/Vodou); live page not compared (live Britannica times out from the box).'
---

# Vodun (Voodoo/West African Vodun) (VODUN)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

Vodou is 'a traditional Afro-Haitian religion', 'a syncretism of the West African Vodun religion and Roman Catholicism' [S1].

## Core metaphysics

Creator God; lwa and ancestors; 'everything is spirit' [S1].

## Position on the LIO axes

- A 1 (0.5, alt 2); B 1 (0.5, alt 0); E 1 (0.5).
- C, D UNKNOWN.

## Schools and variants

TODO

## Science

TODO

## Coding guidance

Practising Vodou / Vodun.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> VODUN (26/50) — Vodun (Voodoo/West African Vodun). Vodun scores moderately due to its emphasis on spiritual balance and communal practices, offering rich cultural coherence but limited by supernatural elements and lack of empirical rigor.

## Open questions

- West African Vodun source.
- Adherents are TODO.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7 (score E on the world's order when the stub is filled).
- 2026-10-15 (systems batch S10): read the listed sources; quotations checked word for word against the fetched page text. Britannica pages read in Wayback copies under P44(e); AI Top Questions not used.
- 2026-10-15 (S10 audit fix): A, B and E scoped to Haitian Vodou; use_when scoped; West African Vodun lead.
