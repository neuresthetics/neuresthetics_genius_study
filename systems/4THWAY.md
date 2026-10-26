---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 4
  review_status: draft — unreviewed
  collected_by: Grok Bot
  model_used: Grok Bot (Lane A tertiary fill)
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
    summary: 'S11: P45 search logged; stays a stub.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Lift stub from Wikipedia Fourth Way / George Gurdjieff (tertiary). Fill classification,
      origins, metaphysics, practice, schools; score LIO with 0.5 certainty and alternatives. Prior P45
      Britannica gap noted; Wikipedia now used as encyclopedia source.'
identity:
  id: '4THWAY'
  v7_1_number: 60
  v7_1_label: "Fourth Way (Gurdjieff's teachings)"
  display_label: "Fourth Way (Gurdjieff's teachings)"
  label_status: as in v7.1
  aliases:
  - The Work
  - Gurdjieff Work
  - "Gurdjieff's teaching"
classification:
  kind:
    value: esoteric or occult tradition
    certainty: 0.7
    cites: &id002
    - source: S2
      locator: opening
    how_known: 'Wikipedia: spiritual teacher / esotericist; Work groups as esoteric schools. 0.7 — also
      read as new religious movement.'
  family:
    value: 'Fourth Way / Gurdjieff Work: path of self-remembering and conscious labour alongside ordinary
      life, distinct from fakir/monk/yogi ways'
    certainty: 0.7
    cites: &id001
    - source: S1
      locator: Overview; Teachings
    how_known: Wikipedia Fourth Way.
  parent_traditions:
    value:
    - "Gurdjieff's synthesis (claimed Eastern monastic sources)"
    - "Ouspensky's transmission"
    - possible Tibetan Buddhist contacts (disputed)
    certainty: 0.5
    cites: *id001
    how_known: '0.5 — exact sources unknown per Wikipedia; Tirado/Chatral notes disputed.'
  related_codes:
  - code: THEOS
    relation: neighbor (easily confused)
    note: Overlapping early-20th-c. esoteric milieu; different cosmology and method
  - code: BUDDH
    relation: overlaps
    note: Claimed Tibetan/monastery influences; not Buddhist identity
  - code: ISLAM
    relation: neighbor (easily confused)
    note: Sufi-link speculation in popular literature; not established here
origins:
  founding_era:
    value: Gurdjieff travels c. 1890–1912; teaching in Russia then Europe from 1910s; Institute at Fontainebleau
      1922; dies 1949
    certainty: 0.7
    cites: &id003
    - source: S1
      locator: Overview
    - source: S2
      locator: opening
    how_known: Wikipedia Gurdjieff / Fourth Way.
  founding_region:
    value: 'Russian Empire (Alexandropol / Caucasus origins); teaching centres in Russia, then France
      (Prieuré, Fontainebleau-Avon), later international Foundations'
    certainty: 0.7
    cites: *id002
    how_known: Wikipedia.
  founders_or_key_figures:
    value:
    - George Ivanovich Gurdjieff
    - P. D. Ouspensky
    - Jeanne de Salzmann
    - Thomas de Hartmann
    - John G. Bennett
    certainty: 0.7
    cites: *id003
    how_known: Wikipedia.
  key_texts:
  - value: In Search of the Miraculous (P. D. Ouspensky)
    certainty: 0.7
    cites: &id005
    - source: S1
      locator: Overview; Teachings
    how_known: Wikipedia Fourth Way.
  - value: "Beelzebub's Tales to His Grandson (G. I. Gurdjieff)"
    certainty: 0.7
    cites: &id004
    - source: S2
      locator: opening
    how_known: Wikipedia Gurdjieff.
  - value: Meetings with Remarkable Men (G. I. Gurdjieff)
    certainty: 0.7
    cites: *id004
    how_known: Wikipedia.
  - value: The Fourth Way (Ouspensky lecture compilation)
    certainty: 0.7
    cites: *id005
    how_known: Wikipedia.
metaphysics:
  god_nature_relation:
    value: 'Cosmology of the Absolute and Ray of Creation (hierarchical levels Absolute → galaxies → sun
      → earth → moon). Cosmic Law of Three and Law of Seven structure processes. Ordinary humans live
      in "waking sleep"; higher consciousness possible. Exact theism varies by interpreter of Beelzebub
      / oral teaching.'
    certainty: 0.5
    cites:
    - source: S1
      locator: Cosmic Laws; Ray of Creation
    how_known: '0.5 — Wikipedia cosmology sections; stance tentative.'
    stance: God in Nature and beyond it
  deity_personal:
    value: 'Not a simple personal-God devotion system. Teaching centres on self-remembering and development
      of being; Absolute is remote at the top of the Ray. Some readers find a Creator Endlessness in Beelzebub;
      practice is Work, not petitionary theism.'
    certainty: 0.5
    cites: *id001
    how_known: '0.5 — Wikipedia emphasizes awakening over personal deity.'
    stance: both / disputed
  intervention:
    value: Higher influences and cosmic laws shape human possibility; Work is conscious labour against
      automatism rather than waiting for miracle intervention.
    certainty: 0.5
    cites: *id001
    how_known: '0.5 — Wikipedia Teachings.'
    stance: rare
  miracles:
    value: 'Not framed as classical miracle religion. Esoteric claims about consciousness, energy, and
      sacred dances; empirical status contested.'
    certainty: 0.5
    cites: *id001
    how_known: '0.5 — Wikipedia.'
    stance: reinterpreted as natural
  petition_and_prayer:
    value: 'Self-observation, self-remembering, conscious labour, intentional suffering — not petitionary
      prayer as the core method. Groups may include readings and Movements.'
    certainty: 0.7
    cites:
    - source: S1
      locator: Basis of teachings
    how_known: '0.7 — Wikipedia.'
    stance: contemplative only
  afterlife:
    value: 'Soul is a potential seed that must be developed through Work; without it one may "die in sleep."
      Not a simple heaven/hell catechism in the Wikipedia summary.'
    certainty: 0.5
    cites:
    - source: S1
      locator: Overview (soul)
    how_known: '0.5 — Wikipedia soul/waking-sleep material.'
    stance: impersonal survival or eternity
  moral_ledger:
    value: 'Evolution of being via conscious labour and intentional suffering; failure is remaining mechanical/asleep.
      Consequence is qualitative (level of being), not a courtroom afterlife scorecard in sources read.'
    certainty: 0.5
    cites:
    - source: S1
      locator: Basis of teachings
    how_known: '0.5 — Wikipedia.'
    stance: impersonal consequence
  authority:
    value: Gurdjieff as teacher; oral transmission via Ouspensky and direct pupils; Foundations after
      1949 (Jeanne de Salzmann). Esoteric but Gurdjieff claimed it was not veiled secrecy — interest/capability
      limit understanding.
    certainty: 0.7
    cites: *id003
    how_known: '0.7 — Wikipedia.'
    stance: founder
  reserved_exemptions:
    value: 'No ethnic or clerical exemption from mechanical sleep; anyone may Work. Schools warn of fake
      ways; right way recognized by knowing it, per Gurdjieff/Ouspensky.'
    certainty: 0.5
    cites: *id001
    how_known: '0.5 — Wikipedia.'
    stance: none
  teleology_in_nature:
    value: Ray of Creation and cosmic laws imply structured process and purpose in the scale of being;
      humans have a possible place/role if awake. Not designer-watchmaker language in sources read.
    certainty: 0.5
    cites:
    - source: S1
      locator: Cosmic Laws; Ray of Creation
    how_known: '0.5 — Wikipedia.'
    stance: immanent ends
  necessity_and_freedom:
    value: Ordinary life is mechanical automatism; freedom begins with self-remembering and struggle against
      identification. Not libertarian free will as academic thesis — practical freedom through Work.
    certainty: 0.5
    cites:
    - source: S1
      locator: Basis of teachings
    how_known: '0.5 — Wikipedia.'
lio_axes:
  A_locus:
    value: 2
    certainty: 0.5
    cites:
    - source: S1
      locator: Ray of Creation; Absolute
    how_known: '0.5 — Absolute remote yet cosmos structured; alternative 1 (more transcendent creator)
      or 3 (law-immanent).'
    rationale: 'Hierarchical Absolute / Ray of Creation: transcendent source with immanent cosmic levels.'
    alternatives:
    - value: 1
      note: Read Absolute/Creator Endlessness as more distinct deity
      cites:
      - source: S1
        locator: Ray of Creation
    - value: 3
      note: Emphasize Law of Three/Seven as immanent process
      cites:
      - source: S1
        locator: Cosmic Laws
  B_cause:
    value: 2
    certainty: 0.5
    cites: *id001
    how_known: '0.5 — higher influences + Work; not pure naturalism. Alternative 3.'
    rationale: 'Change via conscious labour against automatism, within cosmic laws and higher influences
      — not ordinary physicalism, not simple miracle petition.'
    alternatives:
    - value: 3
      note: Stress mechanical laws / psychological technique over higher worlds
      cites: *id001
  C_ledger:
    value: 2
    certainty: 0.5
    cites:
    - source: S1
      locator: Overview (soul)
    how_known: '0.5 — being-evolution ledger; alternative 3 (stronger personal afterlife read).'
    rationale: Soul-development / level-of-being consequences; remain asleep vs awaken.
    alternatives:
    - value: 3
      note: Stronger personal survival/judgment reading of Beelzebub
      cites: *id001
  D_authority:
    value: 1
    certainty: 0.5
    cites: *id003
    how_known: '0.5 — founder/lineage Work schools. Alternative 0 (stricter revelation) or 2.'
    rationale: "Authority in Gurdjieff's teaching and pupil lineages / Foundations; texts mediate."
    alternatives:
    - value: 0
      note: Treat oral esoteric mastership as revelation-like
      cites: *id002
    - value: 2
      note: Emphasize personal verification in the Work
      cites: *id001
  E_scope:
    value: 3
    certainty: 0.5
    cites:
    - source: S1
      locator: Cosmic Laws
    how_known: '0.5 — cosmic laws universal (P7 world-order); Work groups are practice communities not
      cosmic exemptions. Alternative 4 or 2.'
    rationale: 'Law of Three/Seven presented as cosmic; same mechanical sleep for humans generally. In-group
      is school membership for method, not different physics.'
    alternatives:
    - value: 4
      note: 'Fully universal cosmic laws, no school privilege'
      cites:
      - source: S1
        locator: Cosmic Laws
    - value: 2
      note: If fake-schools rhetoric read as strong in-group epistemic privilege
      cites: *id001
    note: "P7: score E on the world's order (same rules for every kind of being and event). Salvation/moral\
      \ community on C. Cosmic laws read as universal; school is method community."
epistemology:
  value: "Self-observation and self-remembering; verify teaching in one's own being. Esoteric knowledge\
    \ claimed practical, not secret for its own sake. Ouspensky documentation of oral teaching."
  certainty: 0.7
  cites: *id001
  how_known: '0.7 — Wikipedia.'
ethics:
  value: "Conscious labour and intentional suffering (including enduring others' displeasing manifestations).\
    \ Aim: awaken from mechanical sleep and develop being. Not a modern progressive social ethics programme\
    \ in sources read."
  certainty: 0.7
  cites:
  - source: S1
    locator: Basis of teachings
  how_known: '0.7 — Wikipedia.'
practice:
  ritual_and_practice:
    value: Self-observation; self-remembering; Gurdjieff Movements (sacred dances); group Work; music
      (de Hartmann collaborations); study of Beelzebub and related texts.
    certainty: 0.7
    cites:
    - source: S1
      locator: Gurdjieff Movements; Basis of teachings
    how_known: '0.7 — Wikipedia.'
  community_form:
    value: "Work groups and Foundations (Gurdjieff Foundation NY 1953; International Association of Gurdjieff\
      \ Foundations — France, USA, UK, Venezuela). Not a mass church; comes and goes without permanent\
      \ institutional form per Ouspensky's report of Gurdjieff."
    certainty: 0.7
    cites: *id003
    how_known: '0.7 — Wikipedia.'
science:
  historical_stance:
    value: Presents cosmic laws and psychological centres as knowledge; not a modern experimental science
      programme. Overlaps early-20th-c. esoteric / occult psychology.
    certainty: 0.5
    cites: *id001
    how_known: '0.5 — Wikipedia.'
  current_stance:
    value: 'Contemporary Foundations continue practical Work. Academic study exists (e.g. Wellbeloved
      Key Concepts — noted prior P45, not re-read here). Not a laboratory science.'
    certainty: 0.5
    cites: *id002
    how_known: '0.5 — Wikipedia + prior open_questions note.'
schools_and_variants:
- name: Gurdjieff Foundations (de Salzmann line)
  form: mystical
  how_it_differs: Direct-pupil lineage after 1949; Jeanne de Salzmann leadership; Movements and group
    Work.
  lio_difference: Axes as scored for the teaching family.
  certainty: 0.7
  cites: *id002
- name: Ouspensky / Fourth Way lecture stream
  form: scholastic or philosophical
  how_it_differs: "Emphasizes Ouspensky's systematic presentation (In Search of the Miraculous; The Fourth\
    \ Way)."
  lio_difference: Little axis change; more didactic.
  certainty: 0.7
  cites: *id001
- name: Independent / Bennett and other lines
  form: modern
  how_it_differs: John G. Bennett and other teachers developed related schools; forms vary.
  lio_difference: May shift D (authority) by lineage.
  certainty: 0.5
  cites: *id002
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Small esoteric networks worldwide via Foundations and independent groups; no reliable mass
      census in sources read
    certainty: 0.5
    cites: *id002
    how_known: '0.5 — Wikipedia describes many groups, no global count.'
v7_1_rubric:
  label: authorial v7.1 scores
  L: 7
  P: 6
  E: 4
  V: 5
  X: 3
  total: 25
  scoring_note: 'Fourth Way scores moderately due to its integrative spiritual approach and focus on self-awakening,
    balanced by esoteric elements that reduce empirical alignment.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 60 and section 7 scoring notes'
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
  use_when: 'Person explicitly in Gurdjieff Work / Fourth Way / Ouspensky line, or primary self-description
    is Gurdjieff pupil.'
  do_not_use_when: 'Generic "esoteric" or Theosophy/Anthroposophy without Gurdjieff link; New Age self-help
    borrowing vocabulary only.'
  neighbors:
  - code: THEOS
    relation: neighbor (easily confused)
  - code: ANTHRO
    relation: neighbor (easily confused)
review:
  data_quality_flags:
  - tertiary_wikipedia_only
  - prior_P45_britannica_gap
  open_questions:
  - 'Prior P45 (2026-10-15): Britannica Gurdjieff bio lacked metaphysics; Wellbeloved 1998/2003 not read
    in full. This fill uses Wikipedia Fourth Way / George Gurdjieff as tertiary encyclopedia — upgrade
    if Wellbeloved or peer-reviewed cosmology is read.'
  - LIO axes at 0.5 with alternatives — Jason may tighten after reading Beelzebub / In Search of the Miraculous
    primary excerpts.
  - SUFI/Islam link remains popular speculation; not coded as parent tradition.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  citation: 'Wikipedia contributors. "Fourth Way." Wikipedia. Accessed 2026-10-25.'
  url: 'https://en.wikipedia.org/wiki/Fourth_Way'
  accessed: '2026-10-25'
- id: S2
  type: tertiary
  kind: encyclopedia
  citation: 'Wikipedia contributors. "George Gurdjieff." Wikipedia. Accessed 2026-10-25.'
  url: 'https://en.wikipedia.org/wiki/George_Gurdjieff'
  accessed: '2026-10-25'
---
# Fourth Way (Gurdjieff's teachings) (4THWAY)

> Status: draft — unreviewed. Lifted from stub 2026-10-25 using Wikipedia *Fourth Way* and *George Gurdjieff* (tertiary). LIO axes scored at 0.5 with alternatives. Prior P45 Britannica gap remains noted under open questions.

## Summary

The Fourth Way (also "the Work") is G. I. Gurdjieff's path of awakening from ordinary "waking sleep" through self-remembering, conscious labour, intentional suffering, and sacred Movements, practised alongside ordinary life rather than in fakir, monk, or yogi withdrawal. P. D. Ouspensky transmitted much of the early oral teaching; Foundations continue group Work after Gurdjieff's death in 1949.

## Core metaphysics

Cosmology includes the Absolute, Ray of Creation, Law of Three, and Law of Seven. Humans are born with a soul-seed that stays dormant under personality unless developed through Work. Authority is the teaching lineage; method is self-observation rather than petitionary prayer.

## Position on the LIO axes

Scored tentatively (0.5) from Wikipedia cosmology/practice summaries: A≈2 (Absolute + immanent levels), B≈2 (Work + higher influences), C≈2 (being/soul development), D≈1 (founder/lineage), E≈3 (cosmic laws universal under P7). Alternatives listed in front matter.

## Schools and variants

Foundations (de Salzmann), Ouspensky lecture stream, and independent lines (e.g. Bennett).

## Science

Not a laboratory science programme; presents cosmic laws and centres as practical esoteric knowledge. Academic secondary literature exists (Wellbeloved et al.) but was not re-read for this fill.

## Coding guidance

Use for explicit Gurdjieff/Fourth Way/Ouspensky affiliation. Do not use for generic esotericism, Theosophy, or Anthroposophy alone.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> 4THWAY (25/50) — Fourth Way (Gurdjieff's teachings). Fourth Way scores moderately due to its integrative spiritual approach and focus on self-awakening, balanced by esoteric elements that reduce empirical alignment.

## Open questions

See front-matter `review.open_questions` (Britannica P45 gap; LIO 0.5; Sufi speculation).

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7.
- 2026-10-15 (S11): P45 search logged; stayed stub (Britannica thin; Wellbeloved unread).
- 2026-10-25: Lifted stub from Wikipedia Fourth Way / George Gurdjieff (tertiary encyclopedia). LIO scored at 0.5 with alternatives. review_status → draft — unreviewed.
