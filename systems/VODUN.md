---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 5
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S9 for Jason)
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
    summary: 'Draft (systems batch S10): filled from Britannica "Vodou" (McAlister). A 1 (0.5, alt 2);
      B 1 (0.5, alt 0); E 1 (0.5); C, D UNKNOWN. Covers Haitian Vodou; West African Vodun not described
      separately. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S10 audit fix: A, B and E scoped to Haitian Vodou; use_when scoped; West African Vodun lead.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from Britannica Vodou (McAlister): Bondye + lwa, serve the spirits, possession,
      manbo/oungan, Rada/Petwo etc. Keep prior axis scores.'
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
      locator: opening
    how_known: Traditional Afro-Haitian religion.
  family:
    value: 'Vodou (Voodoo/Vodun): Afro-Haitian syncretism of West African Vodun with Roman Catholicism;
      everything is spirit; serve the lwa'
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  parent_traditions:
    value:
    - West African Vodun (Fon/Dahomey and related)
    - Kongo, Yoruba and other enslaved ethnic traditions
    - Roman Catholic missionary Christianity in Saint-Domingue
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  related_codes:
  - code: SANTER
    relation: neighbor (easily confused)
    note: Cuban Lucumí; related African-diaspora but distinct
  - code: CHRIST
    relation: overlaps
    note: Bondye as biblical God; saint calendar syncretism
  - code: ANIM
    relation: overlaps
    note: everything is spirit
origins:
  founding_era:
    value: Formed among enslaved Africans in colonial Saint-Domingue (16th–17th c. Christianization context);
      ongoing Haitian tradition
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  founding_region:
    value: Haiti (colonial Saint-Domingue); diaspora communities
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  founders_or_key_figures:
    value:
    - No single founder; manbo and oungan priesthoods; familial inheritance of spirits
    certainty: 1.0
    cites:
    - source: S1
      locator: practice
    how_known: Britannica.
  key_texts:
  - value: Oral tradition; no single scripture in Britannica account
    certainty: 1.0
    cites:
    - source: S1
      locator: practice
    how_known: Oral tradition stated.
metaphysics:
  god_nature_relation:
    value: Biblical God (Bondye) created universe and spirits; lwa help govern humanity and nature. Everything
      is spirit; unseen world of lwa, mysteries, ancestors in Ginen.
    stance: God in Nature and beyond it
    certainty: 0.7
    cites:
    - source: S1
      locator: worldview
    how_known: Creator God + pervasive spirit; 0.7.
  deity_personal:
    value: Personal Bondye and personal lwa who possess devotees and give advice/cures.
    stance: personal
    certainty: 1.0
    cites:
    - source: S1
      locator: worldview; possession
    how_known: Britannica.
  intervention:
    value: 'Regular: possession, healing, advice, protection in return for service.'
    stance: regular
    certainty: 1.0
    cites:
    - source: S1
      locator: sevi lwa; possession
    how_known: Britannica.
  miracles:
    value: Medical cures and special physical feats under possession; not denied.
    stance: affirmed
    certainty: 0.7
    cites:
    - source: S1
      locator: possession
    how_known: Britannica.
  petition_and_prayer:
    value: Prayers and devotional rites to God and particular spirits for health, protection, favour.
    stance: petition answered
    certainty: 1.0
    cites:
    - source: S1
      locator: sevi lwa
    how_known: Britannica.
  afterlife:
    value: Spirits of ancestors and recently deceased populate the unseen world; funerary rituals. Not
      a single heaven doctrine here.
    stance: personal afterlife
    certainty: 0.5
    cites:
    - source: S1
      locator: worldview; calendar
    how_known: Ancestor spirits; 0.5.
  moral_ledger:
    value: Justice is part of the Vodou worldview; secret societies perform religio-juridical function.
      Not a clear afterlife ledger.
    stance: none
    certainty: 0.5
    cites:
    - source: S1
      locator: worldview; Bizango
    how_known: 0.5.
  authority:
    value: Oral/familial inheritance; initiation (kanzo); manbo/oungan; no centralized hierarchy or single
      leader.
    stance: tradition or ancestors
    certainty: 0.7
    cites:
    - source: S1
      locator: practice
    how_known: Britannica.
  reserved_exemptions:
    value: Not addressed.
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: Silence.
  teleology_in_nature:
    value: Spirits help govern the natural world; restore balance and energy in relationships.
    stance: immanent ends
    certainty: 0.5
    cites:
    - source: S1
      locator: worldview; ritual
    how_known: 0.5.
  necessity_and_freedom:
    value: Not addressed.
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Silence.
lio_axes:
  A_locus:
    value: 1
    rationale: A creator God with spirits 'made by God to help him govern humanity and the natural world';
      yet 'Its fundamental principle is that everything is spirit'.
    certainty: 0.5
    cites: &id001
    - source: S1
      locator: article
    how_known: '0.5: the everything-is-spirit principle gives alternative 2. Scope: Haitian Vodou only
      (S1); West African Vodun is not described.'
    alternatives:
    - value: 2
      note: Named alternative.
      cites: *id001
  B_cause:
    value: 1
    rationale: Prayers and rites 'in return for health, protection, and favour'; possessed devotees 'give
      supernaturally inspired advice to people, or perform medical cures or special physical feats'.
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
    rationale: 'On the world''s order (P7): the spirits are served ''in return for health, protection,
      and favour'', and families ''inherit familial spirits''.'
    certainty: 0.5
    cites:
    - source: S1
      locator: article
    how_known: '0.5: favour for those who serve. Scope: Haitian Vodou only (S1); West African Vodun is
      not described.'
epistemology:
  value: Oral tradition; initiation transforms the body as site of knowledge; possession as incarnate
    presence of lwa.
  certainty: 1.0
  cites:
  - source: S1
    locator: practice; possession
  how_known: Britannica.
ethics:
  value: Serve the spirits; restore balance in relationships; justice as part of worldview; details vary
    by sosyete.
  certainty: 0.7
  cites:
  - source: S1
    locator: sevi lwa; worldview
  how_known: Britannica.
practice:
  ritual_and_practice:
    value: Prayer, song, dance, gesture, possession; kanzo initiation; feast calendar syncretized with
      Catholic saints’ days; funerary rites; Bizango/Sanpwèl secret societies.
    certainty: 1.0
    cites:
    - source: S1
      locator: practice; calendar
    how_known: Britannica.
  community_form:
    value: Extended families inheriting spirits; urban sosyete under manbo/oungan; branches Rada, Petwo,
      Kongo, etc.; no single leader.
    certainty: 1.0
    cites:
    - source: S1
      locator: practice
    how_known: Britannica.
science:
  historical_stance:
    value: Worldview encompassing medicine and justice alongside religion; not a science–religion dualism
      statement.
    certainty: 0.7
    cites:
    - source: S1
      locator: worldview
    how_known: Britannica.
  current_stance:
    value: Not addressed.
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Silence.
schools_and_variants:
- name: Rada / Petwo / Kongo and other branches
  form: regional
  how_it_differs: Regional and lineage ritual differences across Haiti.
  lio_difference: Same umbrella scores.
  certainty: 1.0
  cites:
  - source: S1
    locator: practice
- name: Diaspora Vodou
  form: modern
  how_it_differs: Practiced beyond Haiti (article focuses on Haiti).
  lio_difference: Same.
  certainty: 0.7
  cites:
  - source: S1
    locator: opening
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
  scoring_note: Vodun scores moderately due to its emphasis on spiritual balance and communal practices,
    offering rich cultural coherence but limited by supernatural elements and lack of empirical rigor.
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
  use_when: Haitian Vodou / Vodun / Voodoo as Afro-Haitian religion.
  do_not_use_when: Santería/Lucumí (SANTER). Pop-culture 'voodoo' caricature without Vodou identity.
  neighbors:
  - code: SANTER
    relation: neighbor (easily confused)
  - code: CHRIST
    relation: neighbor (easily confused)
review:
  data_quality_flags:
  - Source covers Haitian Vodou; the Britannica "Vodun" page is an unsigned index stub, so West African
    Vodun has no separate source.
  open_questions:
  - 'Lead: a signed or peer-reviewed source on West African Vodun (Fon/Ewe, Benin and Togo), to check
    whether these values hold for it.'
  - A source on West African Vodun.
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Elizabeth A. McAlister; Britannica Editors
  citation: 'McAlister, Elizabeth A., and The Editors of Encyclopaedia Britannica. "Vodou." Encyclopaedia
    Britannica. https://www.britannica.com/topic/Vodou. Wayback Machine snapshot 2026-10-06 07:22:58 UTC:
    https://web.archive.org/web/20261006072258/https://www.britannica.com/topic/Vodou.'
  url: https://www.britannica.com/topic/Vodou
  accessed: '2026-10-25'
  reliability_note: 'Signed article (scholar of Haitian Vodou), full short article read. It covers Haitian
    Vodou; West African Vodun appears only as its source. P44(e): read in the Wayback copy (https://web.archive.org/web/20261006072258/https://www.britannica.com/topic/Vodou);
    live page not compared (live Britannica times out from the box).'
---
# Vodou / Vodun (VODUN)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

Vodou is a traditional Afro-Haitian religion syncretizing West African Vodun with Roman Catholicism; everything is spirit; primary activity is to serve the lwa [S1].

## Core metaphysics

Bondye (biblical God) creates; lwa help govern; possession embodies lwa; Ginen as cosmic Africa [S1].

## Position on the LIO axes

Prior scores kept (see YAML). Deepening did not change axes.

## Schools and variants

Rada, Petwo, Kongo and other branches; familial and sosyete forms [S1].

## Science

Worldview includes medicine and justice [S1].

## Coding guidance

Haitian Vodou. Not SANTER.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> VODUN (26/50) — Vodun (Voodoo/West African Vodun). Vodun scores moderately due to its emphasis on spiritual balance and communal practices, offering rich cultural coherence but limited by supernatural elements and lack of empirical rigor.

## Open questions

- Axis certainties could be revisited with a longer source; left unchanged this pass.

## Research log

- 2026-10-15 (batch S10): Britannica Vodou; axes set.
- 2026-10-25: deepened classification, origins, metaphysics, practice. Axes kept.
