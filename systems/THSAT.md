---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 7
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
    summary: 'Draft (systems batch S12, thin): Britannica "Satanism" (Doyle White) describes theistic
      Satanists only briefly. All axes UNKNOWN: sourced, unscored (P46(a)). v7.1 scores and note unchanged.
      Not reviewed.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from Britannica Satanism: family, kind, contrast with atheistic LaVeyan/TST,
      Temple of Set and solitary theistic practitioners, metaphysics (literal Satan/Lucifer/Set), practice.
      Axes stay UNKNOWN — no shared cosmology across theistic groups (P46(a)).'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Fill adherents/estimate gloss from existing sources (order-of-magnitude / qualitative). Axes
      unchanged.
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score A_locus 0 (0.7) from Britannica Satanism (literal Satan/Lucifer/Set as personal being).
      D stays UNKNOWN (varies by school). B/C/E UNKNOWN.
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Score B1 C1 D2 E1 (0.5) from sources on file (theistic Satanism: personal Satan; occult;
      mixed authority). A already scored.'
identity:
  id: THSAT
  v7_1_number: 73
  v7_1_label: Theistic Satanism (Joy of Satan or similar)
  display_label: Theistic Satanism (Joy of Satan or similar)
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: new religious movement
    certainty: 0.7
    cites:
    - source: S1
      locator: Modern religious Satanism
    how_known: 'Britannica: 20th-c. new religions; theistic camp often solitary. 0.7.'
  family:
    value: 'Modern religious Satanism in the supernaturalist/theistic camp: Satan or Lucifer (sometimes
      Set) is a literal being to be worshipped, not merely a symbol'
    certainty: 1.0
    cites:
    - source: S1
      locator: Modern religious Satanism
    how_known: Britannica divides atheist/rationalist vs supernaturalist camps.
  parent_traditions:
    value:
    - Christian Devil mythology (inverted)
    - Romantic reassessment of Satan as rebel
    - '20th-c. occult milieu; Temple of Set from Church of Satan split'
    certainty: 0.7
    cites:
    - source: S1
      locator: Satan as a character; Modern religious Satanism
    how_known: "Coder's reading of Britannica history."
  related_codes:
  - code: THELEM
    relation: neighbor (easily confused)
    note: Crowleyan Thelema is not THSAT
  - code: CHAOSM
    relation: neighbor (easily confused)
    note: chaos magic ≠ theistic Satan worship
  - code: KEMET
    relation: neighbor (easily confused)
    note: Temple of Set equates Satan with Egyptian Set but is not Kemetic Orthodoxy
  - code: ATHE
    relation: contrast case
    note: LaVeyan Church of Satan and The Satanic Temple are atheistic — not THSAT
origins:
  founding_era:
    value: Organized theistic forms from mid–late 20th century (Temple of Set 1975); solitary theistic
      Satanists proliferated via the Internet by end of 20th century
    certainty: 1.0
    cites:
    - source: S1
      locator: Modern religious Satanism
    how_known: Britannica.
  founding_region:
    value: United States (Temple of Set); international solitary practice via Internet; earlier marginal
      Luciferian groups in first half of 20th century
    certainty: 0.7
    cites:
    - source: S1
      locator: Modern religious Satanism
    how_known: Britannica.
  founders_or_key_figures:
    value:
    - 'Michael Aquino (Temple of Set, 1975)'
    - 'Anton LaVey (Church of Satan founder — atheistic contrast, not THSAT)'
    certainty: 1.0
    cites:
    - source: S1
      locator: Modern religious Satanism
    how_known: Britannica. Joy of Satan named in v7.1 label but not in this Britannica article.
  key_texts:
  - value: "No single canon for theistic Satanism as a whole; LaVey's Satanic Bible (1969) is atheistic\
      \ and not THSAT doctrine"
    certainty: 0.7
    cites:
    - source: S1
      locator: Modern religious Satanism
    how_known: Britannica emphasizes variety; no Joy of Satan text cited.
metaphysics:
  god_nature_relation:
    value: Satan/Lucifer (or Set) literally exists as a being to be worshipped. Relationship to a creator
      God varies by practitioner; often inverted or opposed to Christian God.
    stance: varies by school
    certainty: 0.7
    cites:
    - source: S1
      locator: Modern religious Satanism
    how_known: Britannica stresses variety among theistic Satanists.
  deity_personal:
    value: Satan or Lucifer as a literal personal being; Temple of Set identifies the being with Egyptian
      Set.
    stance: personal
    certainty: 1.0
    cites:
    - source: S1
      locator: Modern religious Satanism
    how_known: Britannica definition of the supernaturalist camp.
  intervention:
    value: Worship implies a being who can be related to; specific intervention doctrines vary and are
      not fixed in Britannica.
    stance: varies by school
    certainty: 0.7
    cites:
    - source: S1
      locator: Modern religious Satanism
    how_known: Britannica.
  miracles:
    value: Not fixed across groups. Some occult Satanic currents accept magic; not universal.
    stance: varies by school
    certainty: 0.7
    cites:
    - source: S1
      locator: 'Modern religious Satanism; occult Q&A material'
    how_known: Britannica notes magic in some groups.
  petition_and_prayer:
    value: Worship of a literal Satan/Lucifer/Set; forms vary. Not described as a single petition theology.
    stance: varies by school
    certainty: 0.7
    cites:
    - source: S1
      locator: Modern religious Satanism
    how_known: Britannica.
  afterlife:
    value: Not described as shared doctrine in Britannica.
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: Modern religious Satanism
    how_known: Britannica silence.
  moral_ledger:
    value: Not a shared ledger doctrine. Groups range from ritual magicians to Order of Nine Angles extremism;
      no single moral cosmology.
    stance: none
    certainty: 0.5
    cites:
    - source: S1
      locator: Modern religious Satanism
    how_known: "Coder's reading; 'none' = no shared ledger, not ethical nihilism claim."
  authority:
    value: 'Varies: founder teachings (Aquino), personal gnosis, occult texts. Not public science. Revelation/founder
      mix; score as varies.'
    stance: varies by school
    certainty: 0.7
    cites:
    - source: S1
      locator: Modern religious Satanism
    how_known: Britannica emphasizes variety and solitude of many practitioners.
  reserved_exemptions:
    value: Not addressed as shared cosmology.
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: Modern religious Satanism
    how_known: Britannica silence.
  teleology_in_nature:
    value: Not addressed as shared doctrine.
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: Modern religious Satanism
    how_known: Britannica silence.
  necessity_and_freedom:
    value: Romantic rebel-Satan theme (challenge to arbitrary authority) informs some currents; not a
      shared free-will metaphysics.
    certainty: 0.7
    cites:
    - source: S1
      locator: Modern religious Satanism
    how_known: "Coder's reading of Britannica on Romantic reassessment."
lio_axes:
  A_locus:
    value: 0
    certainty: 0.7
    cites:
    - source: S1
      locator: opening; theistic forms
    how_known: '0.7 — Satan/Lucifer (or Set) literally exists as a personal being.'
    rationale: 'A=0: transcendent personal being. Not 1: theistic Satanism is not mid-basin deism.'
    alternatives:
    - value: 1
      note: Named alternative if coding some Luciferian streams as more immanent.
      cites:
      - source: S1
        locator: opening
  B_cause:
    value: 1
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — supernatural Satan / magic.'
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
    how_known: '0.5 — personal spiritual consequences / pact themes in streams.'
    rationale: C=1 at 0.5.
    alternatives:
    - value: 'UNKNOWN'
      note: Named alternative if thin.
      cites:
      - source: S1
        locator: opening
  D_authority:
    value: 2
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — mixed: grimoires, gnosis, founder texts; not single closed revelation.'
    rationale: D=2 at 0.5.
    alternatives:
    - value: 1
      note: Named alternative for tradition-heavy streams.
      cites:
      - source: S1
        locator: opening
    - value: 0
      note: Named alternative if coding revelation from Satan as outranks.
      cites:
      - source: S1
        locator: opening
  E_scope:
    value: 1
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — occult in-group / left-hand path exceptions.'
    rationale: E=1 at 0.5.
    alternatives:
    - value: 2
      note: Named alternative.
      cites:
      - source: S1
        locator: opening
epistemology:
  value: 'Varies by group: occult teaching, personal experience of a literal Satan/Set, founder revelations
    (e.g. Aquino). No shared public method.'
  certainty: 0.7
  cites:
  - source: S1
    locator: Modern religious Satanism
  how_known: "Coder's reading."
ethics:
  value: 'No shared ethics. Church of Satan / TST (atheistic) are out of scope. Order of Nine Angles endorses
    violence including human sacrifice — extreme fringe, not representative of all theistic Satanists
    [S1].'
  certainty: 1.0
  cites:
  - source: S1
    locator: Modern religious Satanism
  how_known: Britannica.
practice:
  ritual_and_practice:
    value: Worship of literal Satan/Lucifer/Set; often solitary via Internet. Temple of Set as an organized
      theistic body. Ritual details vary widely.
    certainty: 1.0
    cites:
    - source: S1
      locator: Modern religious Satanism
    how_known: Britannica.
  community_form:
    value: Typically solitary practitioners communicating online; Temple of Set is an organized exception.
      Not one church.
    certainty: 1.0
    cites:
    - source: S1
      locator: Modern religious Satanism
    how_known: Britannica.
science:
  historical_stance:
    value: Occult / supernaturalist; not a natural-science tradition. Distinct from atheistic Satanisms
      that reject a literal Devil.
    certainty: 0.7
    cites:
    - source: S1
      locator: Modern religious Satanism
    how_known: "Coder's reading."
  current_stance:
    value: Not a science stance; supernaturalist self-identification.
    certainty: 1.0
    cites:
    - source: S1
      locator: Modern religious Satanism
    how_known: Britannica.
schools_and_variants:
- name: Temple of Set
  form: modern
  how_it_differs: "Aquino 1975; Satan's real identity is Set; shifts toward modern Paganism."
  lio_difference: Person-level; axes UNKNOWN for THSAT umbrella.
  certainty: 1.0
  cites:
  - source: S1
    locator: Modern religious Satanism
- name: Solitary theistic Satanists / Luciferians
  form: modern
  how_it_differs: Internet-era solitary worship of literal Satan or Lucifer (sometimes distinguished).
  lio_difference: Score the person; umbrella UNKNOWN.
  certainty: 1.0
  cites:
  - source: S1
    locator: Modern religious Satanism
- name: Order of Nine Angles (fringe)
  form: other
  how_it_differs: "Self-described 'traditional Satanism'; little emphasis on Satan; endorses human sacrifice\
    \ and extreme politics."
  lio_difference: Do not treat as typical THSAT ethics.
  certainty: 1.0
  cites:
  - source: S1
    locator: Modern religious Satanism
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Small theistic Satanist / Temple of Set / solitary practitioners; Britannica no census
    certainty: 0.5
    cites:
    - source: S1
      locator: Modern religious Satanism
    how_known: '0.5 — qualitative from listed source; not a genius-rate denominator.'
v7_1_rubric:
  label: authorial v7.1 scores
  L: 6
  P: 5
  E: 3
  V: 4
  X: 2
  total: 20
  scoring_note: 'Theistic Satanism scores low due to its supernatural focus and reliance on revelation,
    though it provides a rebellious framework for some adherents.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 73 and section 7 scoring notes'
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
  use_when: Person affirms Satan/Lucifer (or Set-as-Satan) as a literal being they worship.
  do_not_use_when: 'Church of Satan, The Satanic Temple, or other atheistic/symbolic Satanism — not THSAT
    (contrast ATHE / ethical movements). Accusations of Devil worship without self-identification — not
    THSAT.'
  neighbors:
  - code: THELEM
    relation: neighbor (easily confused)
  - code: KEMET
    relation: neighbor (easily confused)
  - code: CHAOSM
    relation: neighbor (easily confused)
review:
  data_quality_flags:
  - 'Thin: a few sentences on theistic Satanism in a general article; Joy of Satan not named.'
  open_questions:
  - 'Lead: the Temple of Set (1975) held that Satan’s real identity was the Egyptian god Set (S1). A peer-reviewed
    source on theistic Satanism (e.g. Joy of Satan) is needed.'
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Ethan Doyle White
  citation: 'Doyle White, Ethan. "Satanism." Encyclopaedia Britannica. https://www.britannica.com/topic/Satanism.
    Wayback Machine snapshot 2026-10-12 04:17:08 UTC: https://web.archive.org/web/20261012041708/https://www.britannica.com/topic/Satanism.'
  url: 'https://www.britannica.com/topic/Satanism'
  accessed: '2026-10-25'
  reliability_note: 'Signed article (historian of modern Paganism and Satanism); the modern religious
    Satanism section read. P44(e): read in the Wayback copy (https://web.archive.org/web/20261012041708/https://www.britannica.com/topic/Satanism);
    live page not compared (live Britannica times out from the box).'
---
# Theistic Satanism (Joy of Satan or similar) (THSAT)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

Modern religious Satanists divide into atheists/rationalists (Satan as symbol) and supernaturalists who 'perceive Satan/Lucifer as a being that literally exists and whom they wish to worship' [S1]. THSAT is the latter camp. Joy of Satan is named in the v7.1 label but not covered in the Britannica article used here.

## Core metaphysics

Literal personal Satan/Lucifer; Temple of Set equates the being with Egyptian Set [S1]. Broader god–nature and afterlife doctrines vary and are not fixed for the umbrella code.

## Position on the LIO axes

All UNKNOWN (sourced, unscored; P46(a)). Beliefs 'vary considerably' [S1] — score the person's specific group when evidence allows.

## Schools and variants

Temple of Set; solitary theistic Satanists/Luciferians; fringe Order of Nine Angles (not typical) [S1]. Atheistic Church of Satan and The Satanic Temple are out of scope.

## Science

Supernaturalist; not a science tradition [S1].

## Coding guidance

Literal worship only. Symbolic/atheistic Satanism is not THSAT.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> THSAT (20/50) — Theistic Satanism (Joy of Satan or similar). Theistic Satanism scores low due to its supernatural focus and reliance on revelation, though it provides a rebellious framework for some adherents.

## Open questions

- Joy of Satan–specific doctrine source (not in Britannica).
- Adherents are TODO.

## Research log

- 2026-10-15 (batch S12): Britannica Satanism; axes UNKNOWN.
- 2026-10-25: deepened classification, origins, metaphysics, practice, schools from re-read Britannica. Axes still UNKNOWN.
- 2026-10-25: adherents/estimate filled (qualitative).
- 2026-10-25: A_locus scored 0 (0.7).
- 2026-10-25: B/C/D/E scored.
