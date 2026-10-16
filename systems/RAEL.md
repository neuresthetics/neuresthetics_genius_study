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
    summary: 'Draft (systems batch S12, P45 lower tier): filled from Flaherty, "International Raëlian Movement", CDAMM (Cambridge). A 4 (0.5, P44(a)); D 1 (0.5, alt 2); B, C, E UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S12 audit fix: CDAMM described as a commissioned, edited scholarly dictionary entry (amended P45(b)), not peer-reviewed. Values unchanged.'
identity:
  id: RAEL
  v7_1_number: 76
  v7_1_label: Raëlism (Raëlian Movement)
  display_label: Raëlism (Raëlian Movement)
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: new religious movement
    certainty: 0.5
    cites:
    - source: S1
      locator: article
    how_known: UFO religion founded by Raël (Claude Vorilhon). P45 lower tier.
  family:
    value: TODO
  parent_traditions:
    value: TODO
  related_codes: []
origins:
  founding_era:
    value: 1973–74 (reported encounter, December 1973)
    certainty: 0.5
    cites:
    - source: S1
      locator: article
    how_known: P45 lower tier.
  founding_region:
    value: TODO
  founders_or_key_figures:
    value:
    - Raël (Claude Vorilhon)
    certainty: 0.5
    cites:
    - source: S1
      locator: article
    how_known: P45 lower tier.
  key_texts: []
metaphysics:
  god_nature_relation:
    value: '''There is no ‘God’, Raël teaches. Nor is there a soul that survives the body’s death.'' The Elohim are ''the ET scientists who created humanity and all life on Earth''.'
    stance: no God
    certainty: 0.5
    cites:
    - source: S1
      locator: article
    how_known: P45 lower tier.
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
    value: 4
    rationale: '''There is no ‘God’, Raël teaches''; the Elohim are ''an ET race of space-faring bioengineers'' who ''are not gods, but human beings''.'
    certainty: 0.5
    cites:
    - source: S1
      locator: article
    how_known: 'P44(a): no God gives A 4. Capped at 0.5 (P45).'
  B_cause:
    value: UNKNOWN
    how_known: Not addressed in the sources read.
  C_ledger:
    value: UNKNOWN
    how_known: Not addressed in the sources read.
  D_authority:
    value: 1
    rationale: Raël 'has been chosen by the Elohim as the Prophet of the Age of Apocalypse'; the message rests on his reported encounters with the Elohim.
    certainty: 0.5
    cites: &id001
    - source: S1
      locator: article
    how_known: '0.5: a prophet’s received message is the authority; science is also invoked (‘scientific creationism’). Alternative 2.'
    alternatives:
    - value: 2
      note: Named alternative.
      cites: *id001
  E_scope:
    value: UNKNOWN
    how_known: Not addressed in the sources read.
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
  L: 6
  P: 5
  E: 2
  V: 3
  X: 1
  total: 17
  scoring_note: Raëlism scores low due to its reliance on unverified extraterrestrial claims and revelation over evidence, positioning it as a modern UFO-based movement with limited empirical grounding.
  source: v7.1 data book, section 6 table (tables[4]) row 76 and section 7 scoring notes
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
  use_when: The person self-identifies as a Raëlian.
  do_not_use_when: General UFO belief is not RAEL.
  neighbors: []
review:
  data_quality_flags:
  - 'P45 lower tier only: one signed, editor-commissioned CDAMM dictionary entry (not peer-reviewed). Capped at 0.5.'
  open_questions:
  - 'Leads (not read in full): Chryssides, "Is God a Space Alien? The Cosmology of the Raëlian Church", Culture and Cosmos (doi 10.46472/cc.0104.0207); Palmer & Sentes, Cambridge Companion chapter (doi 10.1017/ccol9780521196505.012).'
  - Adherents are TODO.
sources:
- id: S1
  type: secondary
  kind: encyclopedia
  author: Robert Pearson Flaherty
  citation: 'Flaherty, Robert Pearson. "International Raëlian Movement." In James Crossley and Alastair Lockhart (eds.), Critical Dictionary of Apocalyptic and Millenarian Movements (CDAMM), Centre for the Critical Study of Apocalyptic and Millenarian Movements, University of Cambridge, 15 January 2021. https://doi.org/10.17863/CAM.121515. Read in Wayback snapshot 2026-03-07 18:06:21 UTC: https://web.archive.org/web/20260307180621/https://www.cdamm.org/articles/international-raelian-movement.'
  url: https://www.cdamm.org/articles/international-raelian-movement
  accessed: '2026-10-15'
  reliability_note: 'P45 lower tier (b), as amended 2026-10-15: a signed, editor-commissioned scholarly reference entry (commissioned and edited by CenSAMM, Cambridge; editors James Crossley and Alastair Lockhart). Not described as peer-reviewed. No Britannica, SEP or IEP entry found. Claims capped at 0.5.'
---

# Raëlism (Raëlian Movement) (RAEL)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

The Raëlian movement holds that the Elohim are 'the ET scientists who created humanity and all life on Earth'; 'There is no ‘God’, Raël teaches' [S1]. P45 lower tier.

## Core metaphysics

No God, no surviving soul; extraterrestrial creators; re-creation by cloning [S1].

## Position on the LIO axes

- A 4 (0.5, P44(a)); D 1 (0.5, alt 2).
- B, C, E UNKNOWN.

## Schools and variants

TODO

## Science

TODO

## Coding guidance

Raëlians.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> RAEL (17/50) — Raëlism (Raëlian Movement). Raëlism scores low due to its reliance on unverified extraterrestrial claims and revelation over evidence, positioning it as a modern UFO-based movement with limited empirical grounding.

## Open questions

- Leads.
- Adherents.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7 (score E on the world's order when the stub is filled).
- 2026-10-15 (systems batch S12): read the listed sources; quotations checked word for word against the fetched page text. Britannica pages read in Wayback copies under P44(e); AI Top Questions not used.
- 2026-10-15 (S12 audit fix): source description corrected under amended P45(b).
