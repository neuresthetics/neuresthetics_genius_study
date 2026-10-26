---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 8
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
    summary: 'Draft (systems batch S9, thin): Britannica "Modern Paganism" (one sentence) and the abstract
      of Aitamurto & Simpson, Slavic Native Faith (P45). A BELOW_THRESHOLD; rest UNKNOWN. v7.1 scores
      and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S9 audit fix: A BELOW_THRESHOLD -> UNKNOWN. All axes UNKNOWN: sourced, unscored (P46(a)).'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S11 audit fix: publisher summary moved from sources to leads (summary or abstract is a lead,
      not a source).'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from Britannica Neo-Paganism: Rodnovery as Slavic-oriented modern Paganism
      in Poland/Russia/Ukraine; reconstructionist ethnic framing; polytheism varies. Axes stay UNKNOWN
      (umbrella article; P46(a)).'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Fill adherents/estimate gloss from existing sources (order-of-magnitude / qualitative). Axes
      unchanged.
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score A_locus 0 (0.7) and D_authority 1 (0.7) from Britannica Neo-Paganism (reconstructionist
      Slavic gods; historical/archaeological tradition). B/C/E UNKNOWN.
identity:
  id: RODNOV
  v7_1_number: 51
  v7_1_label: Rodnovery (Slavic Native Faith)
  display_label: Rodnovery (Slavic Native Faith)
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: reconstructionist religion
    certainty: 0.7
    cites:
    - source: S1
      locator: History of modern Paganism (1990s Eastern bloc); Beliefs
    how_known: 'Britannica: Slavic-oriented Rodnovery; reconstructionists emphasize fidelity to sources.
      0.7.'
  family:
    value: 'Modern Pagan Rodnovery (Native Faith): Slavic-oriented religions venerating pre-Christian
      Slavic deities; emerged strongly after 1990s collapse of Marxist-Leninist governments'
    certainty: 1.0
    cites:
    - source: S1
      locator: History of modern Paganism
    how_known: 'Britannica names Rodnovery in Poland, Russia, Ukraine.'
  parent_traditions:
    value:
    - Pre-Christian Slavic religions
    - '20th-c. modern Paganism / ethnic nationalist reconstruction currents in Eastern Europe'
    certainty: 0.7
    cites:
    - source: S1
      locator: History of modern Paganism; Beliefs and practices
    how_known: "Coder's reading of Britannica."
  related_codes:
  - code: HEATH
    relation: neighbor (easily confused)
    note: Germanic Heathenry vs Slavic Rodnovery
  - code: HELLEN
    relation: neighbor (easily confused)
    note: both ethnic reconstructionisms; different pantheons
  - code: WICCA
    relation: contrast case
    note: 'Britannica: reconstructionists often define against Wiccan eclecticism'
  - code: ANIM
    relation: neighbor (easily confused)
    note: not automatic ANIM
origins:
  founding_era:
    value: Rapid emergence in the 1990s after collapse of Marxist-Leninist governments in the Eastern
      bloc; broader modern Pagan roots in 20th century
    certainty: 1.0
    cites:
    - source: S1
      locator: History of modern Paganism
    how_known: Britannica.
  founding_region:
    value: 'Linguistically Slavic countries such as Poland, Russia, and Ukraine'
    certainty: 1.0
    cites:
    - source: S1
      locator: History of modern Paganism
    how_known: Britannica.
  founders_or_key_figures:
    value:
    - Not named as individuals in the Britannica Neo-Paganism article
    certainty: 1.0
    cites:
    - source: S1
      locator: History of modern Paganism
    how_known: Britannica silence on Rodnover founders.
  key_texts:
  - value: No Rodnover canon named in the Britannica Neo-Paganism article
    certainty: 1.0
    cites:
    - source: S1
      locator: full article
    how_known: Britannica silence.
metaphysics:
  god_nature_relation:
    value: Modern Pagan theologies range from pantheism and monotheism to polytheism and atheism; Rodnovery
      is Slavic deity-veneration. Exact Rodnover consensus not fixed in this umbrella article.
    stance: varies by school
    certainty: 0.7
    cites:
    - source: S1
      locator: Beliefs and practices
    how_known: "Britannica on modern Pagan diversity; Rodnovery specifically 'venerating the pre-Christian\
      \ deities'."
  deity_personal:
    value: 'Veneration of pre-Christian Slavic deities; some practitioners take deities as literal, others
      as symbolic/archetypal (Britannica on modern Pagans generally).'
    stance: varies by school
    certainty: 0.7
    cites:
    - source: S1
      locator: History; Beliefs and practices
    how_known: Britannica.
  intervention:
    value: 'Ritual offerings to deities, spirits, or ancestors imply relational engagement; not a fixed
      intervention doctrine for Rodnovery alone.'
    stance: varies by school
    certainty: 0.5
    cites:
    - source: S1
      locator: Beliefs and practices
    how_known: Umbrella modern Pagan practice; certainty 0.5 for RODNOV.
  miracles:
    value: Not fixed.
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S1
      locator: Beliefs and practices
    how_known: Britannica silence for Rodnovery specifically.
  petition_and_prayer:
    value: 'Offerings of food, drink, poetry, or performance to deities, spirits, or ancestors are common
      in modern Pagan ritual (umbrella).'
    stance: varies by school
    certainty: 0.5
    cites:
    - source: S1
      locator: Beliefs and practices
    how_known: Umbrella; not Rodnover-specific.
  afterlife:
    value: Some modern Pagans deny a soul; others affirm afterlife or reincarnation. Rodnover consensus
      not stated.
    stance: varies by school
    certainty: 0.7
    cites:
    - source: S1
      locator: Beliefs and practices
    how_known: Britannica umbrella.
  moral_ledger:
    value: Not described for Rodnovery.
    stance: none
    certainty: 0.5
    cites:
    - source: S1
      locator: Beliefs and practices
    how_known: Silence.
  authority:
    value: Reconstructionist emphasis on historical and archaeological source material; ethnic/national
      identity framing common in Eastern European forms. Tradition and ancestors over Abrahamic revelation.
    stance: tradition or ancestors
    certainty: 0.7
    cites:
    - source: S1
      locator: History of modern Paganism; Beliefs
    how_known: "Coder's reading of Britannica on reconstructionists and Eastern ethnic forms."
  reserved_exemptions:
    value: Not addressed.
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: full article
    how_known: Silence.
  teleology_in_nature:
    value: Modern Pagans often view traditions as nature/Earth religions; not a scholastic teleology doctrine.
    stance: immanent ends
    certainty: 0.5
    cites:
    - source: S1
      locator: Beliefs and practices
    how_known: Umbrella gloss at 0.5.
  necessity_and_freedom:
    value: Not addressed for Rodnovery.
    certainty: 1.0
    cites:
    - source: S1
      locator: full article
    how_known: Silence.
lio_axes:
  A_locus:
    value: 0
    certainty: 0.7
    cites:
    - source: S1
      locator: opening; Eastern Europe
    how_known: '0.7 — reconstructionist Slavic polytheism; personal gods.'
    rationale: 'A=0: personal deities. Not 2: ethnic reconstructionist Rodnoverie is not pantheism in
      this source.'
    alternatives:
    - value: 'BELOW_THRESHOLD'
      note: Named alternative if coding wide Neo-Pagan variance under this code.
      cites:
      - source: S1
        locator: opening
  B_cause:
    value: 'UNKNOWN'
    how_known: 'Britannica Neo-Paganism umbrella mentions Rodnovery but does not fix a Slavic cosmogony.
      P44/P46(a): UNKNOWN.'
  C_ledger:
    value: 'UNKNOWN'
    how_known: 'Britannica Neo-Paganism umbrella mentions Rodnovery but does not fix a Slavic cosmogony.
      P44/P46(a): UNKNOWN.'
  D_authority:
    value: 1
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: '0.7 — reconstruction from historical and archaeological sources; stance tradition or ancestors.'
    rationale: 'D=1: ancestral/historical reconstruction primary. Not 4: not observation-first science;
      not 0: no single closed revelation.'
    alternatives:
    - value: 2
      note: Named alternative if coding nationalist ideology as co-equal authority with rite.
      cites:
      - source: S1
        locator: opening
  E_scope:
    value: 'UNKNOWN'
    how_known: 'Britannica Neo-Paganism umbrella mentions Rodnovery but does not fix a Slavic cosmogony.
      P44/P46(a): UNKNOWN.'
epistemology:
  value: Reconstruction from historical and archaeological sources (as reconstructionists define themselves);
    ritual practice often prioritized over belief across modern Paganism.
  certainty: 0.7
  cites:
  - source: S1
    locator: History; Beliefs and practices
  how_known: "Coder's reading."
ethics:
  value: Eastern European ethnic-nationalist modern Paganisms tend to be more socially conservative; progressive
    forms predominate in North America/Britain. Rodnover ethics not separately stated.
  certainty: 0.5
  cites:
  - source: S1
    locator: Beliefs and practices
  how_known: Umbrella political contrast; thin for RODNOV.
practice:
  ritual_and_practice:
    value: Offerings; seasonal/astronomical festivals; outdoor or home ceremonies typical of modern Paganism.
      Rodnover-specific calendar not detailed in Britannica.
    certainty: 0.7
    cites:
    - source: S1
      locator: Beliefs and practices
    how_known: Umbrella applied cautiously.
  community_form:
    value: Homegrown groups in Slavic countries emphasizing national identity; some collaboration via
      bodies like the European Congress of Ethnic Religions; ethnic-nationalist strands often excluded
      from Western Pagan umbrella orgs.
    certainty: 0.7
    cites:
    - source: S1
      locator: History of modern Paganism
    how_known: "Coder's reading of Britannica."
science:
  historical_stance:
    value: "Appeals to historical/archaeological reconstruction; often skeptical of Christian missions;\
      \ some modern Pagans oppose science-fostered 'alienation from nature' (umbrella)."
    certainty: 0.5
    cites:
    - source: S1
      locator: Beliefs and practices
    how_known: Umbrella; thin for RODNOV.
  current_stance:
    value: Not a science programme.
    certainty: 0.7
    cites:
    - source: S1
      locator: Beliefs and practices
    how_known: "Coder's reading."
schools_and_variants:
- name: Rodnovery in Russia / Ukraine / Poland (national variants)
  form: regional
  how_it_differs: Homegrown Slavic Native Faith emphasizing national identity; details vary by country.
  lio_difference: Axes UNKNOWN for umbrella RODNOV.
  certainty: 0.7
  cites:
  - source: S1
    locator: History of modern Paganism
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Modern Pagan Rodnovery communities in Slavic countries after 1990s; Britannica gives no headcount
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
  V: 6
  X: 3
  total: 27
  scoring_note: 'Rodnovery scores moderately due to its cultural revival of Slavic traditions, emphasizing
    nature and ancestry, but limited by mythic elements and lack of empirical rigor.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 51 and section 7 scoring notes'
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
  use_when: Self-identified Rodnover / Slavic Native Faith practitioner.
  do_not_use_when: "Germanic Heathenry (HEATH). Wicca. Generic 'pagan' without Slavic Native Faith identity."
  neighbors:
  - code: HEATH
    relation: neighbor (easily confused)
  - code: HELLEN
    relation: neighbor (easily confused)
  - code: WICCA
    relation: neighbor (easily confused)
review:
  data_quality_flags:
  - 'Thin: one sentence in a general Britannica article (S1). The Aitamurto & Simpson Element is a lead
    only (summary read).'
  open_questions:
  - "Lead (summary only, not a source, per the S11 convention): Aitamurto, Kaarina, and Scott Simpson.\
    \ Slavic Native Faith. Cambridge Elements. Cambridge: Cambridge University Press. https://doi.org/10.1017/9781009436953.\
    \ The publisher summary says the movement 'is comprised of many local and national forms' sharing\
    \ 'a primary emphasis on Slavic identity'. Read the full text."
  - 'Lead for A: Britannica on modern Paganism in general says some take deities as literal and others
    as symbolic (S1); check in Aitamurto & Simpson whether this holds for Rodnovery.'
  - 'Read Aitamurto & Simpson in full.'
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Ethan Doyle White
  citation: 'Doyle White, Ethan. "Modern Paganism." Encyclopaedia Britannica. https://www.britannica.com/topic/Neo-Paganism.
    Wayback Machine snapshot 2026-10-10 14:10:40 UTC: https://web.archive.org/web/20261010141040/https://www.britannica.com/topic/Neo-Paganism.'
  url: 'https://www.britannica.com/topic/Neo-Paganism'
  accessed: '2026-10-25'
  reliability_note: 'Signed article on modern Paganism in general; Rodnovery named in one sentence. P44(e):
    read in the Wayback copy (https://web.archive.org/web/20261010141040/https://www.britannica.com/topic/Neo-Paganism);
    live page timed out on 2026-10-15, so no live comparison.'
---
# Rodnovery / Slavic Native Faith (RODNOV)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

In linguistically Slavic countries such as Poland, Russia, and Ukraine, 'forms of a Slavic-oriented religion called Rodnovery appeared' after the 1990s, as homegrown modern Pagan traditions emphasizing national identity [S1].

## Core metaphysics

Veneration of pre-Christian Slavic deities [S1]. Modern Pagan theology otherwise varies widely (pantheism to atheism; literal vs symbolic deities) [S1] — Rodnover consensus not fixed in this umbrella article.

## Position on the LIO axes

All UNKNOWN (sourced, unscored; P46(a)). Need a Rodnover-specific doctrine source.

## Schools and variants

National variants in Russia, Ukraine, Poland [S1].

## Science

Reconstructionist appeal to history/archaeology; not a science programme [S1].

## Coding guidance

Slavic Native Faith identity only.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> RODNOV (27/50) — Rodnovery (Slavic Native Faith). Rodnovery scores moderately due to its cultural revival of Slavic traditions, emphasizing nature and ancestry, but limited by mythic elements and lack of empirical rigor.

## Open questions

- Rodnover-specific doctrine source (Britannica is umbrella Neo-Paganism).
- Adherents are TODO.

## Research log

- 2026-10-15 (batch S9): Britannica Neo-Paganism; axes UNKNOWN.
- 2026-10-25: deepened classification, origins, metaphysics, practice, schools from re-read Britannica. Axes still UNKNOWN.
- 2026-10-25: adherents/estimate filled (qualitative).
- 2026-10-25: A=0 and D=1 scored from Britannica Neo-Paganism.
