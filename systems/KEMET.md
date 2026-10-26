---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 11
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S8 for Jason)
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
    summary: 'Draft (systems batch S8, thin): one sentence in Britannica "Modern Paganism" (Doyle White).
      A BELOW_THRESHOLD; rest UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'P44(e) compliance (with the S7 fixes): Wayback snapshot URL and timestamp cited.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S8 audit fix: Britannica generic sentence dropped; re-sourced from kemet.org FAQ (House
      of Netjer) under P45(a). A UNKNOWN; B 1 @0.5 (P45 cap). Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S9 audit: P46(b) applied (organization named; plurality noted). Scores unchanged.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: "Deepen qualities from Kemet.org FAQ: family, kind (reconstructionist), Nisut/kingly ka,\
      \ polytheism, Saq oracles, state vs personal practice, Ma'at. Keep B=1; other axes UNKNOWN (P45\
      \ institutional)."
  - date: '2026-10-25'
    by: Grok Bot
    summary: Fill adherents/estimate gloss from existing sources (order-of-magnitude / qualitative). Axes
      unchanged.
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score D_authority 1 (0.7) and A_locus 0 (0.7) from kemet.org FAQ (polytheist Netjeru; ancient
      texts + Saq oracular). C stays UNKNOWN.
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score C_ledger 1 (0.5) and E_scope 1 (0.5) from sources on file (Maat judgment; temple/reconstruction
      in-group).
  - date: '2026-10-25'
    by: Grok Bot
    summary: Fill reserved_exemptions and necessity_and_freedom; deepen schools (reconstructionist / syncretic
      / Kemetic Orthodoxy) from Wikipedia Kemetism. Keep S1. No LIO moves.
identity:
  id: KEMET
  v7_1_number: 50
  v7_1_label: Kemetism (Kemetic Orthodoxy/Egyptian Reconstructionism)
  display_label: Kemetism (Kemetic Orthodoxy/Egyptian Reconstructionism)
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: reconstructionist religion
    certainty: 1.0
    cites:
    - source: S1
      locator: reintroduction; common/differ FAQ
    how_known: 'Kemetic Orthodoxy: revived ancient Nile Valley religion from source texts.'
  family:
    value: 'Kemetic Orthodoxy: modern reconstruction of ancient Egyptian (Kemetic) polytheistic religion
      with state and personal practice levels; House of Netjer'
    certainty: 1.0
    cites:
    - source: S1
      locator: common/differ FAQ
    how_known: Kemet.org FAQ.
  parent_traditions:
    value:
    - 'Pharaonic Kemetic religion (Pyramid Texts, Coffin Texts, Pert em Hru, temple liturgies)'
    - Founded/led by Rev. Tamara Siuda (Nisut)
    certainty: 1.0
    cites:
    - source: S1
      locator: reintroduction FAQ
    how_known: Kemet.org FAQ.
  related_codes:
  - code: HELLEN
    relation: neighbor (easily confused)
    note: both reconstructionisms; different cultures
  - code: WICCA
    relation: contrast case
    note: FAQ distinguishes from Neo-Pagan/New Age Egyptian paths
  - code: THSAT
    relation: contrast case
    note: Temple of Set is not Kemetic Orthodoxy
  - code: HERMET
    relation: neighbor (easily confused)
    note: Greco-Egyptian Hermetica ≠ Kemetic Orthodoxy
origins:
  founding_era:
    value: Modern Kemetic Orthodoxy under Rev. Tamara Siuda (Nisut); public interfaith presence from 1993
      Parliament of World Religions; ancient religion ~4500–30 BCE
    certainty: 0.7
    cites:
    - source: S1
      locator: reintroduction FAQ
    how_known: FAQ; exact KO founding year not stated on this page.
  founding_region:
    value: Modern organization international (House of Netjer); ancient Kemet = Nile Valley
    certainty: 1.0
    cites:
    - source: S1
      locator: common/differ FAQ
    how_known: FAQ.
  founders_or_key_figures:
    value:
    - Rev. Tamara Siuda (Nisut Hekatawy Alexandros; founder; Egyptology/Coptic studies background)
    certainty: 1.0
    cites:
    - source: S1
      locator: Nisut FAQ; reintroduction
    how_known: FAQ.
  key_texts:
  - value: 'Pyramid Texts, Coffin Texts, Pert em Hru (Book of the Dead), temple liturgies and Wisdom Literature
      — sources for KO liturgy'
    certainty: 1.0
    cites:
    - source: S1
      locator: reintroduction FAQ
    how_known: FAQ.
metaphysics:
  god_nature_relation:
    value: Polytheists who acknowledge and worship many gods (Netjeru). Not self-classified as Neo-Pagan.
    stance: many gods within nature
    certainty: 0.5
    cites:
    - source: S1
      locator: common/differ FAQ
    how_known: "Polytheism clear; 'within nature' gloss at 0.5."
  deity_personal:
    value: Many personal gods and goddesses; Saq oracular full trance possessions as intimate face-to-face
      interaction with Netjer.
    stance: personal
    certainty: 1.0
    cites:
    - source: S1
      locator: common/differ FAQ
    how_known: FAQ.
  intervention:
    value: Saq oracular possessions; spiritual consultations and divinations by oracle; gods interact
      in ritual.
    stance: regular
    certainty: 0.7
    cites:
    - source: S1
      locator: worship services; common/differ FAQ
    how_known: FAQ.
  miracles:
    value: "Oracular possession and divination affirmed as religious practice; not framed as 'miracles'\
      \ in Christian sense."
    stance: affirmed
    certainty: 0.5
    cites:
    - source: S1
      locator: common/differ FAQ
    how_known: '0.5.'
  petition_and_prayer:
    value: 'Prayer, offerings, sacrifices, purifications, meditations in personal shrines; formal liturgies
      three times daily.'
    stance: petition answered
    certainty: 0.5
    cites:
    - source: S1
      locator: worship services FAQ
    how_known: Practice clear; answered-petition doctrine thin — 0.5.
  afterlife:
    value: "Dead (royal or not) take on identity/power of Wesir; FAQ rejects 'death-cult' caricature.\
      \ Detailed afterlife doctrine not fully on this FAQ page."
    stance: personal afterlife
    certainty: 0.5
    cites:
    - source: S1
      locator: Nisut FAQ
    how_known: Wesir identity for the dead; thin — 0.5.
  moral_ledger:
    value: "Ma'at as ethical/cosmic order to further in the world; not a detailed heaven/hell ledger on\
      \ this page."
    stance: impersonal consequence
    certainty: 0.5
    cites:
    - source: S1
      locator: other religions FAQ; interreligious work
    how_known: "Ma'at mentioned; ledger type thin."
  authority:
    value: Ancient source texts translated by Nisut; divine guidance in formulating canon; Nisut as teacher
      and vessel of kingly ka (not worshipped as a goddess).
    stance: 'both, revelation first'
    certainty: 0.5
    cites:
    - source: S1
      locator: reintroduction; Nisut FAQ
    how_known: Texts + divine guidance + academic Egyptology — 0.5.
  reserved_exemptions:
    value: "No blanket in-group exemption from Ma'at. Pharaoh (ancient) / Nisut (Kemetic Orthodoxy) mediate\
      \ gods and people; clergy by vocation. Chaos (Isfet) is the opposing force, not a privileged class\
      \ exemption."
    stance: none
    certainty: 0.5
    cites:
    - source: S3
      locator: Overview (pharaoh as intermediary)
    how_known: '0.5 — Wikipedia Ancient Egyptian religion + Kemetism; modern groups vary.'
  teleology_in_nature:
    value: "Ma'at as order to uphold; not scholastic designer teleology."
    stance: immanent ends
    certainty: 0.5
    cites:
    - source: S1
      locator: "interreligious work mention of Ma'at"
    how_known: Thin.
  necessity_and_freedom:
    value: "Upholding Ma'at against Isfet frames human duty; gods govern nature but humans choose offerings,\
      \ ritual, and ethical action. Not a scholastic free-will treatise."
    certainty: 0.5
    cites:
    - source: S3
      locator: Overview
    how_known: "0.5 — Wikipedia summarizing Ma'at/Isfet polarity."
lio_axes:
  A_locus:
    value: 0
    certainty: 0.7
    cites:
    - source: S1
      locator: polytheists; Netjeru
    how_known: '0.7 — many personal gods and goddesses; Saq oracular possession.'
    rationale: 'A=0: personal Netjeru. Not 2: not pantheism in this source.'
    alternatives:
    - value: 1
      note: Named alternative if weighting Maat-as-order over personal gods.
      cites:
      - source: S1
        locator: Maat
  B_cause:
    value: 1
    rationale: Saq oracular possessions and divination; gods interact in ritual (leans interventionist).
    certainty: 0.5
    cites:
    - source: S1
      locator: common/differ FAQ; worship services
    how_known: Prior score kept; reinforced from FAQ.
  C_ledger:
    value: 1
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — weighing of the heart / Maat; personal afterlife judgment theme.'
    rationale: C=1 at 0.5.
    alternatives:
    - value: 3
      note: Named alternative if reading Maat as impersonal cosmic law.
      cites:
      - source: S1
        locator: opening
  D_authority:
    value: 1
    certainty: 0.7
    cites:
    - source: S1
      locator: ancient source texts; Saq
    how_known: '0.7 — ancient liturgies/texts; Nisut translations; Saq oracular revelation.'
    rationale: 'D=1: tradition + oracular. Not 0: not a single closed new revelation ranking alone.'
    alternatives:
    - value: 0
      note: Named alternative if coding Saq as revelation-outranks.
      cites:
      - source: S1
        locator: Saq
  E_scope:
    value: 1
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — reconstructionist / temple practice; ancient Egyptian in-group frame.'
    rationale: E=1 at 0.5.
    alternatives:
    - value: 2
      note: Named alternative.
      cites:
      - source: S1
        locator: opening
epistemology:
  value: Reconstruction from ancient liturgies and texts; Nisut translations; Saq oracular revelation
    in ritual; academic Egyptology credentials of founder.
  certainty: 0.7
  cites:
  - source: S1
    locator: reintroduction; common/differ FAQ
  how_known: "Coder's reading."
ethics:
  value: "Further Ma'at in the world; interreligious charity required of priests; multicultural membership;\
    \ rejects racial gatekeeping."
  certainty: 0.7
  cites:
  - source: S1
    locator: reintroduction; race FAQ
  how_known: FAQ.
practice:
  ritual_and_practice:
    value: 'Formal state liturgies (often 3× daily), festival calendar (Sirius-calibrated), personal home
      shrines, Saq oracles, processions, communal meals.'
    certainty: 1.0
    cites:
    - source: S1
      locator: holidays; worship services
    how_known: FAQ.
  community_form:
    value: House of Netjer; clergy by vocation not self-declaration; Nisut as institutional kingship vessel;
      members may practice other religions privately.
    certainty: 1.0
    cites:
    - source: S1
      locator: other religions; common/differ FAQ
    how_known: FAQ.
science:
  historical_stance:
    value: Uses Egyptological source scholarship; distinguishes academic reconstruction from New Age.
    certainty: 0.7
    cites:
    - source: S1
      locator: reintroduction FAQ
    how_known: "Coder's reading."
  current_stance:
    value: Not a natural-science programme; engages academic Egyptology.
    certainty: 0.7
    cites:
    - source: S1
      locator: reintroduction FAQ
    how_known: "Coder's reading."
schools_and_variants:
- name: Kemetic Orthodoxy (House of Netjer)
  form: modern
  how_it_differs: More monotheistic/henotheistic framing under Nisut; structured clergy and oracular practice
    (Saq). Primary file focus.
  lio_difference: Axes as scored; D may sit more hierarchical than loose reconstructionists.
  certainty: 0.7
  cites:
  - source: S2
    locator: Overview (three types)
- name: Reconstructionist Kemetism
  form: reform
  how_it_differs: Aims closer to historical ancient Egyptian polytheism; less centralized authority than
    Orthodoxy.
  lio_difference: D may sit higher (less clerical hierarchy); A firmly many gods.
  certainty: 0.5
  cites:
  - source: S2
    locator: Overview
- name: Syncretic / eclectic Kemetic paganism
  form: popular
  how_it_differs: Mixes Netjeru with other neopagan streams; looser canon.
  lio_difference: Little axis change; E often more universalist/eclectic.
  certainty: 0.5
  cites:
  - source: S2
    locator: Overview
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Kemetic Orthodoxy and related reconstructionists; small organized presence per institutional
      sources
    certainty: 0.5
    cites:
    - source: S1
      locator: FAQ
    how_known: '0.5 — qualitative from listed source; not a genius-rate denominator.'
v7_1_rubric:
  label: authorial v7.1 scores
  L: 7
  P: 6
  E: 5
  V: 6
  X: 3
  total: 27
  scoring_note: 'Kemetism scores moderately due to its revival of ancient Egyptian balance and justice
    principles, offering ethical coherence but limited by mythic reconstruction and lack of empirical
    rigor.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 50 and section 7 scoring notes'
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
  use_when: Kemetic Orthodox / House of Netjer / self-identified Kemetic reconstructionist practicing
    ancient Egyptian polytheism.
  do_not_use_when: Eclectic Wicca with Egyptian deity names only. Temple of Set. Hermeticism alone.
  neighbors:
  - code: HELLEN
    relation: neighbor (easily confused)
  - code: WICCA
    relation: neighbor (easily confused)
  - code: HERMET
    relation: neighbor (easily confused)
review:
  data_quality_flags:
  - 'P45 lower tier only: the House of Netjer’s own FAQ (Kemetic Orthodoxy, one organization; the FAQ
    says it is not a Neo-Pagan group). Capped at 0.5.'
  - 'P46(b): one organization (the House of Netjer (Kemetic Orthodoxy)); Kemetism is plural: Kemetic Orthodoxy
    is one organization among several Kemetic groups and solitary practitioners.'
  open_questions:
  - 'Leads: Krogh & Pillifant 2004, Sociology of Religion 65(2) (abstract: Kemetic Orthodoxy "is monistic
    ... based on ritual authority"); Harrison 2017 chapter. Not read in full.'
  - Adherents are TODO.
sources:
- id: S1
  type: primary
  kind: institutional page
  author: The House of Netjer
  citation: 'The House of Netjer. "Frequently Asked Questions." Kemet.org (Kemetic Orthodoxy). https://www.kemet.org/faq.'
  url: 'https://www.kemet.org/faq'
  accessed: '2026-10-25'
  reliability_note: 'P45 lower tier (a): the movement’s own published statement; claims capped at 0.5.
    Site copyright 1993–2020; undated page. P46(b): stands for the House of Netjer (Kemetic Orthodoxy)
    only. Kemetism is plural: Kemetic Orthodoxy is one organization among several Kemetic groups and solitary
    practitioners. A peer-reviewed source on the whole movement would take precedence.'
- id: S2
  type: tertiary
  kind: encyclopedia
  citation: 'Wikipedia contributors. "Kemetism." Wikipedia. Accessed 2026-10-25.'
  url: 'https://en.wikipedia.org/wiki/Kemetism'
  accessed: '2026-10-25'
- id: S3
  type: tertiary
  kind: encyclopedia
  citation: 'Wikipedia contributors. "Ancient Egyptian religion." Wikipedia. Accessed 2026-10-25.'
  url: 'https://en.wikipedia.org/wiki/Ancient_Egyptian_religion'
  accessed: '2026-10-25'
---
# Kemetic Orthodoxy / Kemetism (KEMET)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

Kemetic Orthodoxy is a revived practice of ancient Nile Valley religion focusing on liturgy and rites from pharaonic sources; it 'acknowledge[s] the existence of, and worship, many gods' [S1]. Led by Nisut Rev. Tamara Siuda; House of Netjer [S1]. P45 institutional page.

## Core metaphysics

Polytheism; Saq oracular trance possessions; Nisut bears kingly ka but is not worshipped as a goddess [S1]. Ma'at to further in the world [S1].

## Position on the LIO axes

- **A, C, D, E:** UNKNOWN.
- **B_cause: 1** (0.5) — oracular possession and divine ritual interaction [S1].

## Schools and variants

Kemetic Orthodoxy vs other Egyptian Neo-Pagan paths [S1].

## Science

Engages Egyptology; not a natural-science programme [S1].

## Coding guidance

Kemetic reconstruction identity. Not WICCA-with-Egyptian-names.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> KEMET (27/50) — Kemetism (Kemetic Orthodoxy/Egyptian Reconstructionism). Kemetism scores moderately due to its revival of ancient Egyptian balance and justice principles, offering ethical coherence but limited by mythic reconstruction and lack of empirical rigor.

## Open questions

- Adherents.

## Research log

- 2026-10-15 (batch S8): kemet.org FAQ; B scored.
- 2026-10-25: deepened classification, origins, metaphysics, practice, schools from re-read FAQ. B kept.
- 2026-10-25: adherents/estimate filled (qualitative).
- 2026-10-25: A=0 and D=1 scored from kemet.org.
- 2026-10-25: C/E scored.
- 2026-10-25: Filled reserved_exemptions / necessity_and_freedom; schools from Wikipedia Kemetism.
