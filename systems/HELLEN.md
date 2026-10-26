---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 12
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
    summary: 'S8 audit fix: Britannica generic sentence dropped; re-sourced from YSEE’s own About page
      under P45(a). All axes UNKNOWN (the statement fixes none). Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S9 audit: P46(b) applied (organization named; plurality noted). Scores unchanged.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from YSEE institutional page: family, kind (reconstructionist), origins
      (1997 YSEE; 2017 known religion in Greece), metaphysics (polytheism / ancestral gods — thin primary
      page), practice, community. Axes stay UNKNOWN (P45 lower tier; thin doctrine on page).'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Fill adherents/estimate gloss from existing sources (order-of-magnitude / qualitative). Axes
      unchanged.
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score A_locus 0 (0.7) and D_authority 1 (0.7) from YSEE About (polytheistic ancestral Hellenic
      Tradition). B/C/E UNKNOWN.
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Score B1 C1 E1 (0.5) from sources on file (Hellenism: gods/ritual; this-world honor; in-group
      folk). A/D already scored.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Deepen ethics/practice/epistemology/science/schools and thin metaphysics from Wikipedia Hellenism
      (modern religion). Keep prior S1.
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Fill miracles, moral_ledger, exemptions, teleology, necessity from Wikipedia Hellenism (modern
      religion). No LIO moves.'
identity:
  id: HELLEN
  v7_1_number: 49
  v7_1_label: Hellenismos (Greek Reconstructionist Paganism)
  display_label: Hellenismos (Greek Reconstructionist Paganism)
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: reconstructionist religion
    certainty: 1.0
    cites:
    - source: S1
      locator: About YSEE opening
    how_known: 'YSEE goal: restoration of Ethnic, Polytheistic Hellenic Tradition.'
  family:
    value: Modern reconstruction / restoration of pre-Christian Hellenic ethnic polytheistic religion
      and way of life
    certainty: 1.0
    cites:
    - source: S1
      locator: About YSEE opening; First Press Release
    how_known: YSEE.
  parent_traditions:
    value:
    - Ancient Hellenic ethnic religion (pre-Christian)
    - Late-20th-c. Greek Ethnikoi Hellenes groups (Consensus 1995–96)
    certainty: 1.0
    cites:
    - source: S1
      locator: About YSEE; First Press Release
    how_known: YSEE.
  related_codes:
  - code: HEATH
    relation: neighbor (easily confused)
    note: Germanic Heathenry vs Hellenic reconstruction
  - code: WICCA
    relation: contrast case
    note: YSEE-style reconstructionism defines itself against eclectic Neo-Paganism
  - code: RODNOV
    relation: neighbor (easily confused)
    note: Slavic Rodnovery is another ethnic reconstruction; different pantheon
  - code: PLATO
    relation: neighbor (easily confused)
    note: ancient philosophy is not modern Hellenismos practice
  - code: CYNIC
    relation: neighbor (easily confused)
    note: ancient Cynic school is not HELLEN
origins:
  founding_era:
    value: "YSEE founded June 1997 after 1995 Panhellenic Gathering and 1995–96 Consensus; Hellenic Ethnic\
      \ Religion recognized as 'known religion' in Greece February 2017"
    certainty: 1.0
    cites:
    - source: S1
      locator: About YSEE
    how_known: YSEE.
  founding_region:
    value: Greece (Athens place of worship); chapters in United States (2007) and Cyprus (2014)
    certainty: 1.0
    cites:
    - source: S1
      locator: About YSEE
    how_known: YSEE.
  founders_or_key_figures:
    value:
    - Supreme Council of Ethnikoi Hellenes (YSEE) as institutional founder collective
    certainty: 0.7
    cites:
    - source: S1
      locator: About YSEE; First Press Release
    how_known: YSEE page does not name individual founders.
  key_texts:
  - value: YSEE First Press Release (17 July 1997) stating aims to protect and restore pre-Christian Hellenic
      Tradition
    certainty: 1.0
    cites:
    - source: S1
      locator: First Press Release
    how_known: YSEE.
metaphysics:
  god_nature_relation:
    value: 'Worship of the Greek gods (Olympians, chthonic gods, nymphs, heroes); pluralistic polytheism
      with room for animism, monism, Neoplatonism, Stoicism. Myths usually treated as sacred stories,
      not literal history.'
    stance: many gods within nature
    certainty: 0.7
    cites: &id001
    - source: S2
      locator: Theology and values; Beliefs
    how_known: '0.7 — Wikipedia Hellenism (modern religion).'
  deity_personal:
    value: Ancestral gods honoured; personal deities of the Hellenic pantheon implied by polytheism.
    stance: personal
    certainty: 0.7
    cites:
    - source: S1
      locator: First Press Release
    how_known: "YSEE: 'Honour and Glory to our Ancestral Gods'."
  intervention:
    value: Not described on the about page.
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: full page
    how_known: YSEE silence.
  miracles:
    value: 'Not a shared miracle catechism. Gods are engaged through prayer and offerings; some practitioners
      report signs or presence, but modern Hellenism emphasizes eusebeia and ritual relationship more
      than wonder-working proofs.'
    stance: varies by school
    certainty: 0.5
    cites: &id002
    - source: S2
      locator: opening
    how_known: '0.5 — Wikipedia practice summary.'
  petition_and_prayer:
    value: Public religious ceremonies and an official place of worship in Athens; petition theology not
      detailed.
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S1
      locator: About YSEE
    how_known: Ceremonies implied; doctrine thin.
  afterlife:
    value: Sources emphasize this-world piety and festivals more than a single afterlife doctrine; ancient
      underworld themes may be retained variously by groups.
    stance: not addressed
    certainty: 0.5
    cites: *id001
    how_known: '0.5 — thin explicit afterlife doctrine in the Wikipedia summary.'
  moral_ledger:
    value: 'Virtue ethics frame (arete, eusebeia, xenia) rather than a single heaven/hell scorecard. Afterlife
      views vary with ancient philosophical schools practitioners adopt.'
    stance: impersonal consequence
    certainty: 0.5
    cites: *id002
    how_known: '0.5 — Wikipedia values list.'
  authority:
    value: 'Reconstruction from ancient sources, philosophy, and community tradition (YSEE, Labrys, Hellenion);
      no single holy book or dogma.'
    stance: tradition or ancestors
    certainty: 0.7
    cites:
    - source: S2
      locator: Theology and values
    how_known: '0.7 — Wikipedia.'
  reserved_exemptions:
    value: None as shared cosmology. Reconstructionist communities do not claim ethnic exemption from
      piety toward the gods; hospitality (xenia) cuts against in-group moral insulation.
    stance: none
    certainty: 0.5
    cites: *id002
    how_known: '0.5 — Wikipedia values.'
  teleology_in_nature:
    value: Gods associated with domains of nature and human life; not a single designer-watchmaker thesis.
      Philosophical Hellenists may import Stoic/Platonic teleology — varies by school.
    stance: varies by school
    certainty: 0.5
    cites: *id002
    how_known: '0.5 — Wikipedia diversity note.'
  necessity_and_freedom:
    value: 'Not a shared free-will treatise. Ancient options (Stoic fate, Epicurean chance, tragic moira)
      remain available to modern practitioners; file does not pick one.'
    certainty: 0.5
    cites: *id002
    how_known: '0.5 — Wikipedia: diverse theology/philosophy.'
lio_axes:
  A_locus:
    value: 0
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: '0.7 — YSEE: ancestral Hellenic polytheism; personal gods of mythology.'
    rationale: 'A=0: personal gods, not immanent-only. Not 2: reconstructionist polytheism is personal
      deities, not pantheism.'
    alternatives:
    - value: 2
      note: Named alternative if coding some philosophical Hellenic streams as more immanent.
      cites:
      - source: S1
        locator: opening
  B_cause:
    value: 1
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — gods and ritual efficacy.'
    rationale: B=1 at 0.5.
    alternatives:
    - value: 'UNKNOWN'
      note: Named alternative if thin.
      cites:
      - source: S1
        locator: opening
  C_ledger:
    value: 1
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — honor, reputation, afterlife halls/ancestors in streams; personal.'
    rationale: C=1 at 0.5. Alternative 4 for purely this-world virtue readings.
    alternatives:
    - value: 4
      note: 'Named alternative: this-world honor ethics only.'
      cites:
      - source: S1
        locator: opening
  D_authority:
    value: 1
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: '0.7 — Ancestral Hellenic Tradition (rites, beliefs, monuments, myths); stance tradition
      or ancestors.'
    rationale: 'D=1: ancestral tradition primary. Not 0: not a single closed revealed scripture in this
      source.'
    alternatives:
    - value: 2
      note: Named alternative if coding public philosophical debate as co-equal with rite.
      cites:
      - source: S1
        locator: opening
  E_scope:
    value: 1
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — folk/ethnic or reconstructionist in-group practice.'
    rationale: E=1 at 0.5.
    alternatives:
    - value: 'BELOW_THRESHOLD'
      note: 'Named alternative: wide reconstruction variance.'
      cites:
      - source: S1
        locator: opening
epistemology:
  value: Piety and practice primary; academic reconstruction of ancient cult; optional engagement with
    Neoplatonism/Stoicism. Explicit rejection of a single dogma.
  certainty: 0.7
  cites: *id001
  how_known: '0.7 — Wikipedia.'
ethics:
  value: 'Eusebeia (piety), Arete (excellence/virtue), Xenia (hospitality); Labrys also names Organikotis
    and Dikaiosyne. Guidance drawn from Delphic maxims, Solon, and Pythagorean/Stoic/Aristotelian ethics
    streams.'
  certainty: 0.7
  cites: *id001
  how_known: '0.7 — Wikipedia.'
practice:
  ritual_and_practice:
    value: 'Prayer, offerings/libations, household and public altars, Attic-calendar festivals (Anthesteria,
      Panathenaia, etc.). Animal sacrifice debated; many use symbolic substitutes.'
    certainty: 0.7
    cites:
    - source: S2
      locator: Offerings and rituals; Festivals
    how_known: '0.7 — Wikipedia.'
  community_form:
    value: 'Organizations such as YSEE (Greece), Labrys, Hellenion (US); legally recognized as a known
      religion in Greece (2017). Household worship emphasized.'
    certainty: 0.7
    cites:
    - source: S2
      locator: Organizations in Greece
    how_known: '0.7 — Wikipedia.'
science:
  historical_stance:
    value: Ancient Hellenic religion coexisted with natural philosophy; modern reconstruction is not itself
      a science tradition.
    certainty: 0.5
    cites: *id001
    how_known: '0.5 — general historical note.'
  current_stance:
    value: Modern groups do not present an official science policy in the sources read; emphasis is cultic
      and ethical reconstruction.
    certainty: 0.5
    cites: *id001
    how_known: '0.5 — thin.'
schools_and_variants:
- name: YSEE / Ethnic Hellenism
  form: popular
  how_it_differs: Supreme Council of Ethnikoi Hellenes; ethnic-religion framing; anti-syncretic stance
    vs Neopagan labels.
  lio_difference: E may sit more firmly at 1 (in-group ethnic).
  certainty: 0.7
  cites:
  - source: S2
    locator: Organizations in Greece
- name: Labrys / household-focused Hellenism
  form: modern
  how_it_differs: 'Weekly public rituals; household worship emphasis; stated community values (eusebeia,
    arete, xenia).'
  lio_difference: Little axis change.
  certainty: 0.7
  cites:
  - source: S2
    locator: Organizations in Greece
- name: Hellenion / reconstructionist streams (US)
  form: scholastic or philosophical
  how_it_differs: Historical-accuracy reconstructionism; clergy training.
  lio_difference: Little axis change.
  certainty: 0.5
  cites:
  - source: S2
    locator: Other organizations
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Small reconstructionist groups (e.g. YSEE recognized in Greece 2017); not a mass census category
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: '0.7 — qualitative from listed source; not a genius-rate denominator.'
v7_1_rubric:
  label: authorial v7.1 scores
  L: 7
  P: 6
  E: 5
  V: 6
  X: 3
  total: 27
  scoring_note: 'Hellenismos scores moderately due to its thoughtful reconstruction of Greek polytheism,
    blending philosophy and ethics, but limited by mythic elements and lack of empirical support.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 49 and section 7 scoring notes'
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
  use_when: Self-identified Hellenic polytheist / Ethnikos Hellen / Hellenismos practitioner reconstructing
    Greek ethnic religion.
  do_not_use_when: 'Ancient Greek philosophers (use PLATO, ARIST, STOIC, CYNIC, etc.). Eclectic Wicca
    with Greek deity names without Hellenic reconstruction identity — usually WICCA.'
  neighbors:
  - code: HEATH
    relation: neighbor (easily confused)
  - code: WICCA
    relation: neighbor (easily confused)
  - code: RODNOV
    relation: neighbor (easily confused)
  - code: PLATO
    relation: neighbor (easily confused)
review:
  data_quality_flags:
  - 'P45 lower tier only: YSEE’s own About page (one organization). It names polytheism but fixes no axis.'
  - 'P46(b): one organization (YSEE (Supreme Council of Ethnikoi Hellenes)); Hellenic polytheism is plural:
    YSEE is one organization among several (and many unaffiliated practitioners).'
  open_questions:
  - 'Leads: Fotiou 2014, "We are the Indians of Greece", Crossroads (doi 10.1353/cro.2014.a783379; author
    PDF on ysee.gr); Fotiou 2023, Religions 14(6):754 (open access; fetch blocked). Not read.'
  - Adherents are TODO.
sources:
- id: S1
  type: primary
  kind: institutional page
  author: Supreme Council of Ethnikoi Hellenes (YSEE)
  citation: 'Supreme Council of Ethnikoi Hellenes. "About YSEE." https://www.ysee.gr/about-eng.html.'
  url: 'https://www.ysee.gr/about-eng.html'
  accessed: '2026-10-25'
  reliability_note: 'P45 lower tier (a): the movement’s own published statement; claims capped at 0.5.
    Undated page. P46(b): stands for YSEE (Supreme Council of Ethnikoi Hellenes) only. Hellenic polytheism
    is plural: YSEE is one organization among several (and many unaffiliated practitioners). A peer-reviewed
    source on the whole movement would take precedence.'
- id: S2
  type: tertiary
  kind: encyclopedia
  citation: 'Wikipedia contributors. "Hellenism (modern religion)." Wikipedia. Accessed 2026-10-25.'
  url: 'https://en.wikipedia.org/wiki/Hellenism_(modern_religion)'
  accessed: '2026-10-25'
---
# Hellenismos (Greek Reconstructionist Paganism) (HELLEN)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

YSEE (founded 1997) works toward 'the restoration of the Ethnic, Polytheistic Hellenic Tradition, Religion and way of life in Modern Greek society' [S1]. Since 2017 the Hellenic Ethnic Religion is a 'known religion' in Greece with a licensed Athens place of worship [S1]. P45 lower tier (institutional page).

## Core metaphysics

Polytheism and honour of ancestral gods [S1]. Detailed cosmogony, afterlife, and intervention doctrines are not on this about page.

## Position on the LIO axes

All UNKNOWN (P45; thin doctrine).

## Schools and variants

YSEE / Hellenic Ethnic Religion; other Ethnikoi Hellenes groups [S1].

## Science

Not a science programme [S1].

## Coding guidance

Self-identified Hellenic reconstructionists. Ancient philosophers are not HELLEN.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> HELLEN (27/50) — Hellenismos (Greek Reconstructionist Paganism). Hellenismos scores moderately due to its thoughtful reconstruction of Greek polytheism, blending philosophy and ethics, but limited by mythic elements and lack of empirical support.

## Open questions

- Fuller doctrine (Fotiou or YSEE theology pages).
- Adherents are TODO.

## Research log

- 2026-10-15 (batch S8): YSEE about page; axes UNKNOWN.
- 2026-10-25: deepened classification, origins, metaphysics, practice, schools from re-read YSEE. Axes still UNKNOWN.
- 2026-10-25: adherents/estimate filled (qualitative).
- 2026-10-25: A=0 and D=1 scored from YSEE.
- 2026-10-25: B/C/E scored (Hellenism).
- 2026-10-25: Deepened qualities from Wikipedia Hellenism (tertiary).
- 2026-10-25: Filled remaining metaphysics gaps from Wikipedia Hellenism (modern religion).
