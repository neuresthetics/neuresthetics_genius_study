---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 6
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
    summary: "Decision P7: E_scope note added. E is not scored in a stub; when it is, score it on the\
      \ world's order (same rules for every kind of being and event, no in-group exceptions in this-world\
      \ events). Salvation and moral community go on C_ledger."
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'Draft (systems batch S9, thin): filled from Britannica "Bon" (editors, one paragraph). A
      3 (0.5, alt 2); B 1 (0.5); C, D, E UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S9 audit fix: A 3 and B 1 -> UNKNOWN for Bon as a whole; early-Bon reading kept as a lead.
      P45(b) search found Kværne leads; none read in full, so nothing scored. Sourced, unscored (P46(a)).'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from Britannica: family, parents, related codes, origins, metaphysics (many
      gods / propitiation / oracular priests), practice, science, schools (early magic Bon vs later systematized).
      Axes stay UNKNOWN (thin Britannica; P46(a)).'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Fill adherents/estimate gloss from existing sources (order-of-magnitude / qualitative). Axes
      unchanged.
identity:
  id: BON
  v7_1_number: 54
  v7_1_label: Bön (Tibetan indigenous religion)
  display_label: Bön (Tibetan indigenous religion)
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: indigenous or traditional religion
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: 'Britannica: indigenous religion of Tibet.'
  family:
    value: Indigenous Tibetan religion; later systematized in interaction with Buddhism; survives as a
      living faith and in Tibetan Buddhist features
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; closing
    how_known: Britannica.
  parent_traditions:
    value:
    - 'Pre-Buddhist Tibetan cults (magic, divine kingship, atmospheric/earth/subterranean gods)'
    - Buddhist literary and doctrinal models (from the 8th century systematization)
    certainty: 0.7
    cites:
    - source: S1
      locator: paragraphs 1–3
    how_known: "Coder's reading of Britannica's early features and 8th-c. systematization."
  related_codes:
  - code: BUDDH
    relation: overlaps
    note: Bon absorbed into and gave character to Tibetan Buddhism; living Bon remains distinct
  - code: ANIM
    relation: neighbor (easily confused)
    note: early Bon magic/propitiation is not automatic ANIM
  - code: SHINTO
    relation: neighbor (easily confused)
    note: both have indigenous-plus-Buddhist histories; different regions
origins:
  founding_era:
    value: Pre-Buddhist Tibet; systematized with sacred literature in the 8th–9th centuries under Buddhist
      literary influence; persecuted under King Khrisong Detsen
    certainty: 1.0
    cites:
    - source: S1
      locator: paragraphs 2–3
    how_known: Britannica.
  founding_region:
    value: Tibet; surviving communities on the northern and eastern frontiers of Tibet
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; closing
    how_known: Britannica.
  founders_or_key_figures:
    value:
    - 'King Khrisong Detsen (persecutor of Bon claims to supremacy, late 8th century)'
    certainty: 0.7
    cites:
    - source: S1
      locator: paragraph 3
    how_known: Britannica names the king; Bon founding figures not named in this article.
  key_texts:
  - value: Bon sacred literature developed when Bon was systematized (enabled by Buddhist concern for
      written works)
    certainty: 0.7
    cites:
    - source: S1
      locator: paragraph 3
    how_known: Britannica mentions sacred literature without naming titles.
metaphysics:
  god_nature_relation:
    value: 'Cult of gods of the atmosphere, the earth, and subterranean regions; sky divinity linked to
      divine kingship; demonic forces propitiated.'
    stance: many gods within nature
    certainty: 0.7
    cites:
    - source: S1
      locator: paragraph 2
    how_known: Britannica early features; later Bon doctrine not detailed here.
  deity_personal:
    value: Personal gods and demonic forces addressed in cult and propitiation; sky divinity manifested
      in kings.
    stance: personal
    certainty: 0.7
    cites:
    - source: S1
      locator: paragraph 2
    how_known: Britannica.
  intervention:
    value: 'Magic-related practice and propitiation of demonic forces; oracular priests. Intervention
      assumed in cult, not denied.'
    stance: regular
    certainty: 0.5
    cites:
    - source: S1
      locator: paragraph 2
    how_known: "Coder's reading of early Bon features; thin source; certainty 0.5."
  miracles:
    value: Magic and oracular practice imply supernatural efficacy; Britannica does not state a miracle
      doctrine in Christian terms.
    stance: affirmed
    certainty: 0.5
    cites:
    - source: S1
      locator: paragraph 2
    how_known: "Thin; alternative 'not addressed' if magic ≠ miracles."
  petition_and_prayer:
    value: Propitiation of demonic forces; blood sacrifices in early Bon; oracular priesthood.
    stance: petition answered
    certainty: 0.7
    cites:
    - source: S1
      locator: paragraph 2
    how_known: Britannica.
  afterlife:
    value: Not described in the Britannica article read. Divine kingship and sky-divinity manifestations
      are noted without a general afterlife doctrine.
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: full article
    how_known: Britannica silence.
  moral_ledger:
    value: Not described in the source read.
    stance: none
    certainty: 0.5
    cites:
    - source: S1
      locator: full article
    how_known: "Silence; stance 'none' as placeholder for no ledger doctrine stated (not a positive claim\
      \ of no karma)."
  authority:
    value: Oracular priests; later sacred literature; tradition continuous with pre-Buddhist practice.
      Not observation-and-reason natural science.
    stance: tradition or ancestors
    certainty: 0.7
    cites:
    - source: S1
      locator: paragraphs 2–3
    how_known: "Coder's reading of Britannica."
  reserved_exemptions:
    value: Not addressed as cosmology of exemptions from natural law.
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: full article
    how_known: Britannica silence.
  teleology_in_nature:
    value: Not addressed.
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: full article
    how_known: Britannica silence.
  necessity_and_freedom:
    value: Not addressed in the source read.
    certainty: 1.0
    cites:
    - source: S1
      locator: full article
    how_known: Britannica silence.
lio_axes:
  A_locus:
    value: 'UNKNOWN'
    how_known: Britannica article is short on doctrine; early features suggest gods and magic but do not
      fix LIO scores under P44/P46(a). Fuller Bon literature needed.
  B_cause:
    value: 'UNKNOWN'
    how_known: Britannica article is short on doctrine; early features suggest gods and magic but do not
      fix LIO scores under P44/P46(a). Fuller Bon literature needed.
  C_ledger:
    value: 'UNKNOWN'
    how_known: Britannica article is short on doctrine; early features suggest gods and magic but do not
      fix LIO scores under P44/P46(a). Fuller Bon literature needed.
  D_authority:
    value: 'UNKNOWN'
    how_known: Britannica article is short on doctrine; early features suggest gods and magic but do not
      fix LIO scores under P44/P46(a). Fuller Bon literature needed.
  E_scope:
    value: 'UNKNOWN'
    how_known: Britannica article is short on doctrine; early features suggest gods and magic but do not
      fix LIO scores under P44/P46(a). Fuller Bon literature needed.
epistemology:
  value: Oracular priests and later sacred literature. Britannica does not state a formal epistemology.
  certainty: 0.7
  cites:
  - source: S1
    locator: paragraphs 2–3
  how_known: "Coder's reading."
ethics:
  value: Not described in the Britannica article (ritual and political struggle dominate the summary).
  certainty: 1.0
  cites:
  - source: S1
    locator: full article
  how_known: Britannica silence.
practice:
  ritual_and_practice:
    value: 'Early: magic, propitiation of demonic forces, blood sacrifices; oracular priests; cult of
      atmospheric, earth, and subterranean gods; divine kingship. Later: systematized religion with sacred
      literature.'
    certainty: 1.0
    cites:
    - source: S1
      locator: paragraphs 2–3
    how_known: Britannica.
  community_form:
    value: "Living religion on Tibet's northern and eastern frontiers; historically tied to noble families\
      \ vs Buddhist ruling house; features absorbed into Tibetan Buddhism."
    certainty: 1.0
    cites:
    - source: S1
      locator: paragraphs 2–3
    how_known: Britannica.
science:
  historical_stance:
    value: 'Magic and oracular practice, not a natural-science programme. Systematization borrowed Buddhist
      written-culture habits.'
    certainty: 0.7
    cites:
    - source: S1
      locator: paragraphs 2–3
    how_known: "Coder's reading."
  current_stance:
    value: Continues as a living religion; Britannica does not state a modern science stance.
    certainty: 1.0
    cites:
    - source: S1
      locator: closing
    how_known: Britannica.
schools_and_variants:
- name: Early / pre-systematized Bon
  form: popular
  how_it_differs: 'Magic, propitiation, blood sacrifice, oracular priests, divine kingship, three-realm
    gods.'
  lio_difference: Axes UNKNOWN on thin source.
  certainty: 0.7
  cites:
  - source: S1
    locator: paragraph 2
- name: Later systematized Bon (8th–9th c. onward)
  form: other
  how_it_differs: Doctrine and sacred literature under Buddhist literary influence; survived persecution;
    living frontier communities.
  lio_difference: Still UNKNOWN pending fuller doctrine sources.
  certainty: 0.7
  cites:
  - source: S1
    locator: paragraph 3
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Living Tibetan Bon communities and Bon features inside Tibetan Buddhism; no single global census
      in Britannica
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — qualitative from listed source; not a genius-rate denominator.'
v7_1_rubric:
  label: authorial v7.1 scores
  L: 7
  P: 6
  E: 5
  V: 5
  X: 3
  total: 26
  scoring_note: 'Bön scores moderately due to its ancient shamanistic roots and focus on natural harmony,
    offering cultural and spiritual coherence but limited by revelatory elements and lack of empirical
    rigor.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 54 and section 7 scoring notes'
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
  use_when: 'Person practices or identifies with Bon as a living Tibetan religion, or historical Bon priesthood/nobility
    context.'
  do_not_use_when: "Tibetan Buddhist practice that merely inherits Bon-derived features — use BUDDH. Generic\
    \ 'shamanism' without Bon identity — not BON."
  neighbors:
  - code: BUDDH
    relation: neighbor (easily confused)
  - code: ANIM
    relation: neighbor (easily confused)
review:
  data_quality_flags:
  - 'Thin: one-paragraph editors’ article; later systematized Bon not described.'
  open_questions:
  - 'Early-Bon lead (S1, hedged): "a cult of the gods of the atmosphere, the earth, and subterranean regions";
    kings as "manifestations of the sky divinity" (would suggest A 3, alt 2); "The original features of
    Bon seem to have been largely magic-related" (would suggest B 1). Not scored: early Bon only.'
  - 'P45(b) leads, not read in full: Kværne, "The study of Bon in the West: Past, present, and future",
    Senri Ethnological Reports 15 (2000), doi 10.15021/00002196, which separates pre-Buddhist religion,
    popular "nameless religion" and Yungdrung Bon; Kværne, The Bon Religion of Tibet (1995), intro pp.
    9–10.'
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Britannica Editors
  citation: 'The Editors of Encyclopaedia Britannica. "Bon." Encyclopaedia Britannica. https://www.britannica.com/topic/Bon-Tibetan-religion.
    Wayback Machine snapshot 2026-09-11 19:57:27 UTC: https://web.archive.org/web/20260911195727/https://www.britannica.com/topic/Bon-Tibetan-religion.'
  url: 'https://www.britannica.com/topic/Bon-Tibetan-religion'
  accessed: '2026-10-25'
  reliability_note: 'Short unsigned editors’ article (one paragraph). P44(e): read in the Wayback copy
    (https://web.archive.org/web/20260911195727/https://www.britannica.com/topic/Bon-Tibetan-religion);
    live page timed out on 2026-10-15, so no live comparison.'
---
# Bön (Tibetan indigenous religion) (BON)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

Bon is the 'indigenous religion of Tibet' that, 'when absorbed by the Buddhist traditions introduced from India in the 8th century, gave Tibetan Buddhism much of its distinctive character' [S1]. It 'continues to survive both in the aspects of Tibetan Buddhism … and as a living religion on the northern and eastern frontiers of Tibet' [S1].

## Core metaphysics

Early features: magic and propitiation of demonic forces (including blood sacrifices); divine kingship as manifestation of the sky divinity; oracular priests; gods of atmosphere, earth, and subterranean regions [S1]. Later Bon developed 'specific doctrine and a sacred literature' under Buddhist written-culture influence [S1]. Afterlife and moral ledger are not described in this Britannica article.

## Position on the LIO axes

All UNKNOWN (sourced, unscored; P46(a)). Britannica is too thin on later Bon doctrine to score under P44.

## Schools and variants

Early magic/propitiatory Bon; later systematized Bon (8th–9th c.) [S1].

## Science

Magic and oracular practice, not a natural-science programme [S1].

## Coding guidance

Living or historical Bon identity. Tibetan Buddhism that only inherits Bon features → BUDDH.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> BON (26/50) — Bön (Tibetan indigenous religion). Bön scores moderately due to its ancient shamanistic roots and focus on natural harmony, offering cultural and spiritual coherence but limited by revelatory elements and lack of empirical rigor.

## Open questions

- Later Bon doctrine (afterlife, karma, cosmology) needs a fuller source (e.g. Snellgrove / Encyclopedia.com Bon entry).
- Adherents are TODO.

## Research log

- 2026-10-15 (batch S9): Britannica Bon; axes UNKNOWN under P46(a).
- 2026-10-25: deepened classification, origins, metaphysics, practice, science, schools from re-read Britannica. Axes still UNKNOWN.
- 2026-10-25: adherents/estimate filled (qualitative).
