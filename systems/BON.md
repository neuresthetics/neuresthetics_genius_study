---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 9
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
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score D_authority 1 (0.7) from Britannica Bon (oracular priests; tradition/ancestors). A/B/C/E
      UNKNOWN — article thin on locus/ledger.
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score A1 B1 C3 E1 (0.5) from Britannica Bon (spirits/ritual; Yungdrung Bon; karma-adjacent
      Tibetan context). D already 1.
  - date: '2026-10-25'
    by: Grok Bot
    summary: Deepen ethics/practice/epistemology/science/schools and thin metaphysics claims from Wikipedia
      Bon (tertiary). Keep Britannica S1.
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
    value: Ultimate principle with male Kuntuzangpo and female Kuntuzangmo; bon sku / bon nyid as true
      nature of phenomena (parallel to dharmakaya). Tonpa Shenrab as present teacher-Buddha; worldly spirits
      retained in lower Ways.
    stance: many gods within nature
    certainty: 0.7
    cites: &id001
    - source: S2
      locator: Teachings; Types
    how_known: '0.7 — Wikipedia Bon summarizing Powers/Samuel/Kvaerne.'
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
    value: Karma and rebirth across six realms; funerary guidance; liberation and rainbow-body themes
      in Dzogchen streams of the higher Ways.
    stance: not addressed
    certainty: 0.7
    cites: *id001
    how_known: '0.7 — Wikipedia Bon (Nine Ways / Teachings).'
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
    value: 'Terma rediscoveries, Zhangzhung aural lineage, Menri monastic curriculum, and Dzogchen oral
      instructions; Bon Kanjur/Tenjur rather than Indian Buddhist canon as primary.'
    stance: tradition or ancestors
    certainty: 0.7
    cites: *id001
    how_known: '0.7 — Wikipedia Bon.'
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
    value: 1
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — deities/spirits; not clear classical monotheism.'
    rationale: A=1 at 0.5.
    alternatives:
    - value: 0
      note: Named alternative if coding Bon pantheon as personal gods A=0.
      cites:
      - source: S1
        locator: opening
  B_cause:
    value: 1
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — ritual efficacy / spirits.'
    rationale: B=1 at 0.5.
    alternatives:
    - value: 'UNKNOWN'
      note: Named alternative if thin.
      cites:
      - source: S1
        locator: opening
  C_ledger:
    value: 3
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — Tibetan Bon/Buddhist karma adjacency; impersonal rebirth law reading.'
    rationale: C=3 at 0.5.
    alternatives:
    - value: 1
      note: Named alternative for personal spirit ledger.
      cites:
      - source: S1
        locator: opening
  D_authority:
    value: 1
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: '0.7 — Britannica: oracular priests and later sacred literature; stance tradition or ancestors.'
    rationale: 'D=1: tradition/oracular authority over observation-first. Not 0: not a single closed revelation
      ranking above all observation in the short article.'
    alternatives:
    - value: 0
      note: Named alternative if coding later Bon sacred literature as revelation-outranks.
      cites:
      - source: S1
        locator: opening
    - value: 2
      note: Named alternative if coding modern Bon–Buddhist synthesis as mixed authority.
      cites:
      - source: S1
        locator: opening
  E_scope:
    value: 1
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — ritual and lineage in-group.'
    rationale: E=1 at 0.5.
    alternatives:
    - value: 'BELOW_THRESHOLD'
      note: 'Named alternative: Yungdrung vs folk Bon variance.'
      cites:
      - source: S1
        locator: opening
epistemology:
  value: 'Canonical Bon Kanjur/Tenjur, terma revelations, Gelug-style monastic debate, and Dzogchen direct
    introduction to the natural state.'
  certainty: 0.7
  cites: *id001
  how_known: '0.7 — Wikipedia Bon.'
ethics:
  value: 'Liberation from suffering under karma; lay ten wholesome activities (Way of a Lay Follower);
    monastic vinaya-like discipline in higher Ways; pragmatic worldly rites (divination, ransom) alongside
    path ethics.'
  certainty: 0.7
  cites: *id001
  how_known: '0.7 — Wikipedia Bon (Nine Ways).'
practice:
  ritual_and_practice:
    value: 'Nine Ways: divination, local gods, magic/exorcism, funerary rites, lay morality, ascetic/monastic
      path, tantra/mantra, Anuyoga-like methods, Dzogchen. Offerings often use symbolic substitutes for
      animal sacrifice; ransom rituals common.'
    certainty: 0.7
    cites: *id001
    how_known: '0.7 — Wikipedia Bon.'
  community_form:
    value: 'Monasteries (Menri lineage; diaspora India/Nepal), lay yogis, and village ritual specialists.
      Recognized among Tibetan exile institutions since 1979.'
    certainty: 0.7
    cites:
    - source: S2
      locator: Present situation
    how_known: '0.7 — Wikipedia Bon.'
science:
  historical_stance:
    value: 'Not a modern natural-science tradition; medicine and astrology appear among lower Ways; cosmology
      of elements, eggs, and light/dark dualism.'
    certainty: 0.5
    cites: *id001
    how_known: '0.5 — inferred from Nine Ways classification on Wikipedia.'
  current_stance:
    value: 'Contemporary Bon centers teach philosophy, Dzogchen, and ritual; engagement with Western scholarship
      since Snellgrove. Sources read do not state an official science policy.'
    certainty: 0.5
    cites:
    - source: S2
      locator: Present situation
    how_known: '0.5 — thin on science policy.'
schools_and_variants:
- name: Yungdrung Bon (Eternal Bon)
  form: scholastic or philosophical
  how_it_differs: Classical organized Bon from 10th–11th c.; Tonpa Shenrab; Nine Ways; Menri orthodoxy.
  lio_difference: Axes as scored; A/B/C/E at 0.5.
  certainty: 0.7
  cites:
  - source: S2
    locator: Types
- name: New Bon (Bon Sar)
  form: mystical
  how_it_differs: Syncretic with Nyingma/Padmasambhava streams from 14th c. eastern Tibet.
  lio_difference: Little axis change; more Buddhist overlap.
  certainty: 0.7
  cites:
  - source: S2
    locator: Types
- name: Prehistoric / folk Bon streams
  form: popular
  how_it_differs: 'Earlier court/village ritual, divination, ransom; relationship to Yungdrung Bon debated.'
  lio_difference: May push B/E toward stronger spirit-efficacy / local in-group.
  certainty: 0.5
  cites:
  - source: S2
    locator: Types
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
- id: S2
  type: tertiary
  kind: encyclopedia
  citation: 'Wikipedia contributors. "Bon." Wikipedia. Accessed 2026-10-25.'
  url: 'https://en.wikipedia.org/wiki/Bon'
  accessed: '2026-10-25'
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
- 2026-10-25: D_authority scored 1 (0.7).
- 2026-10-25: A/B/C/E scored at 0.5.
- 2026-10-25: Deepened qualities from Wikipedia Bon (tertiary).
