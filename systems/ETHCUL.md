---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 6
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S1 for Jason)
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
    summary: 'Draft (systems batch S1): filled from Britannica "Ethical Culture". D 3 at 0.5; A, B, C
      and E UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S1 audit: Britannica credited as Britannica Editors (unsigned); leads for A noted.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from Britannica + Encyclopedia.com Ethical Culture: metaphysics TODOs,
      epistemology/practice/science/schools; set A=4 (0.7) from Adler’s rejection of theism. Other axes
      unchanged.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score B4 C4 E4 (0.7/0.7/0.5) from Britannica Ethical Culture (this-world ethics; Adler theism
      rejection). A/D already scored.
identity:
  id: ETHCUL
  v7_1_number: 5
  v7_1_label: Ethical Culture (Ethical Humanism)
  display_label: Ethical Culture (Ethical Humanism)
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: ethical or civic movement
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: "Britannica: 'a movement based upon the conviction that moral tenets need not be grounded\
      \ in religious or philosophical dogma'."
  family:
    value: Ethical humanism / Ethical Culture movement; deed over creed
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    - source: S2
      locator: opening
    how_known: Britannica + Encyclopedia.com.
  parent_traditions:
    value:
    - Reform Judaism (Adler’s background)
    - Kantian ethics
    - Free religious / Independent Church lectures
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    - source: S2
      locator: opening
    how_known: S1/S2.
  related_codes:
  - code: SECHUM
    relation: overlaps
    note: Secular ethical humanism neighbor
  - code: KANT
    relation: overlaps
    note: Adler’s Kantian every-person-as-end
  - code: SUNASM
    relation: overlaps
    note: Congregational secular practice
  - code: ATHE
    relation: neighbor (easily confused)
    note: Adler rejected theism but movement embraces diverse meaning-quests
origins:
  founding_era:
    value: '1876'
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  founding_region:
    value: 'New York City, United States'
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  founders_or_key_figures:
    value:
    - Felix Adler
    - W. M. Salter
    - Stanton Coit
    - Walter L. Sheldon
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica names Adler as founder and these other leaders.
  key_texts:
  - value: 'Felix Adler, Creed and Deed (and founding address 1876)'
    year: 1877
    certainty: 0.7
    cites:
    - source: S2
      locator: Bibliography; opening
    how_known: '0.7 — named in literature; texts not fully read.'
metaphysics:
  god_nature_relation:
    value: Adler rejected theism; movement embraces ethical fellowship regardless of diverse approaches
      to meaning
    stance: varies by school
    certainty: 0.7
    cites:
    - source: S2
      locator: opening
    how_known: '0.7 — founder vs openness.'
  deity_personal:
    value: No required theism; Adler rejected theism and finality of Jewish theology
    stance: varies by school
    certainty: 0.7
    cites:
    - source: S2
      locator: opening
    how_known: '0.7.'
  intervention:
    value: Ethics not grounded in divine intervention
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: '0.7.'
  miracles:
    value: Not a miracle religion; ethics independent of religious dogma
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: '0.7.'
  petition_and_prayer:
    value: Sunday services with music/address; not petitionary theism required
    stance: no petition
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    - source: S2
      locator: guise of a religious organization
    how_known: '0.7.'
  afterlife:
    value: Not a required afterlife doctrine; life-cycle rites without supernatural creed
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    - source: S2
      locator: guise
    how_known: '0.7.'
  moral_ledger:
    value: No divine ledger; moral law and social ethics in this life
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    - source: S2
      locator: opening
    how_known: '0.7.'
  authority:
    value: "Ethics independent of dogma: 'Adler contended that Judaism and Christianity were mistaken\
      \ in making ethics dependent on religious dogma'; he started from Kant's principle that every human\
      \ being is an end in himself."
    stance: observation and reason
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  reserved_exemptions:
    value: Universal intrinsic worth; no in-group supernatural exemption
    stance: none
    certainty: 0.7
    cites:
    - source: S2
      locator: ideals
    how_known: '0.7.'
  teleology_in_nature:
    value: Not a designer-teleology doctrine; focus on ethical action
    stance: none
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5.'
  necessity_and_freedom:
    value: Moral agency and duty to apply ethics to society; Kantian end-in-oneself
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    - source: S2
      locator: opening
    how_known: '0.7.'
lio_axes:
  A_locus:
    value: 4
    certainty: 0.7
    cites:
    - source: S2
      locator: opening
    how_known: '0.7 — Encyclopedia.com: Adler rejected theism; movement remains open to diverse meaning-quests.'
    rationale: 'Founder rejects theism; A 4 for no-God grounding under P44a. Alternatives: leave UNKNOWN
      if coding persons who keep private theism inside Ethical Culture.'
    alternatives:
    - value: 'UNKNOWN'
      note: Named alternative if member retains theism under deed-over-creed openness.
      cites:
      - source: S2
        locator: opening
  B_cause:
    value: 4
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: '0.7 — no miracle doctrine; ethical culture this-world.'
    rationale: B=4.
    alternatives:
    - value: 'UNKNOWN'
      note: Named alternative if refusing.
      cites:
      - source: S1
        locator: opening
  C_ledger:
    value: 4
    certainty: 0.7
    cites:
    - source: S1
      locator: ethics
    how_known: '0.7 — this-world ethics; no divine ledger.'
    rationale: C=4.
    alternatives:
    - value: 3
      note: Named alternative if reading deed consequences as impersonal law.
      cites:
      - source: S1
        locator: ethics
  D_authority:
    value: 3
    rationale: 'Moral reason, not religious dogma, grounds ethics (Adler; Kant). 3 not 4: the source speaks
      to ethics only, not to knowledge of the world.'
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0–4 scale (P1). Inferred from the ethics claim, 0.5.'
  E_scope:
    value: 4
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — implied same natural/moral community order.'
    rationale: E=4 at 0.5.
    alternatives:
    - value: 'UNKNOWN'
      note: Named alternative if refusing.
      cites:
      - source: S1
        locator: opening
epistemology:
  value: Ethics independent of religious dogma; Kantian every person as end; deed over creed
  certainty: 1.0
  cites:
  - source: S1
    locator: opening
  - source: S2
    locator: 'Not the creed, but the deed'
  how_known: S1/S2.
ethics:
  value: Intrinsic worth of each person; seek ethical principles as guide; work for material and spiritual
    betterment of society; applied social ethics
  certainty: 1.0
  cites:
  - source: S1
    locator: opening
  - source: S2
    locator: ideals
  how_known: S1/S2.
practice:
  ritual_and_practice:
    value: 'Sunday services (music, reading, address); marriages and funerals; Adler promoted as a religion
      with services'
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    - source: S2
      locator: guise
    how_known: S1/S2.
  community_form:
    value: 'Societies (NY 1876; Chicago, Philadelphia, St. Louis…); American Ethical Union; international
      Ethical/Humanist unions'
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    - source: S2
      locator: national; international
    how_known: S1/S2.
science:
  historical_stance:
    value: Adler’s German university exposure to 19th-c. science and historical criticism shaped rejection
      of theism
    certainty: 1.0
    cites:
    - source: S2
      locator: opening
    how_known: Encyclopedia.com.
  current_stance:
    value: Ongoing Ethical societies; social-reform legacy; liberal social causes
    certainty: 1.0
    cites:
    - source: S2
      locator: applied social ethics
    how_known: Encyclopedia.com.
schools_and_variants:
- name: New York Society for Ethical Culture / Adler
  form: modern
  how_it_differs: Founding society; Adler’s Kantian ethical religion
  lio_difference: Primary for ETHCUL
  certainty: 1.0
  cites:
  - source: S1
    locator: opening
- name: American Ethical Union societies
  form: modern
  how_it_differs: Federated US societies
  lio_difference: Not rescored
  certainty: 1.0
  cites:
  - source: S2
    locator: national
- name: International Ethical / Humanist unions
  form: modern
  how_it_differs: Broader humanist confederation overlap
  lio_difference: May overlap SECHUM
  certainty: 0.7
  cites:
  - source: S2
    locator: international
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: 'Historically a few thousand in US societies (mid-1980s ~5,000 per Encyclopedia.com); small
      movement'
    certainty: 0.7
    cites:
    - source: S2
      locator: membership figures
    how_known: '0.7 — dated census.'
v7_1_rubric:
  label: authorial v7.1 scores
  L: 10
  P: 10
  E: 10
  V: 10
  X: 9
  total: 49
  scoring_note: 'Ethical Culture scores highly for its rational, action-oriented ethics, serving as a
    secular moral framework with excellent coherence.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 5 and section 7 scoring notes'
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
  use_when: Person’s primary identity is Ethical Culture / Ethical Humanism / AEU society.
  do_not_use_when: Generic secular humanism without Ethical Culture → SECHUM; mere Kantianism → KANT.
  neighbors:
  - code: SECHUM
    relation: overlaps
    note: Humanist neighbor
  - code: KANT
    relation: overlaps
    note: Kantian ethics root
  - code: SUNASM
    relation: overlaps
    note: Secular congregation
review:
  data_quality_flags: []
  open_questions:
  - Keep A=4 vs UNKNOWN given openness?
  - Read Adler Creed and Deed for B/C?
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Britannica Editors
  citation: 'Britannica Editors. "Ethical Culture." Encyclopaedia Britannica. https://www.britannica.com/topic/Ethical-Culture.'
  url: 'https://www.britannica.com/topic/Ethical-Culture'
  accessed: '2026-10-25'
  reliability_note: Unsigned article credited to Britannica Editors; read in full.
- id: S2
  type: tertiary
  kind: encyclopedia
  citation: 'Benny Kraut, “Ethical Culture,” Encyclopedia of Religion (via Encyclopedia.com)'
  url: 'https://www.encyclopedia.com/environment/encyclopedias-almanacs-transcripts-and-maps/ethical-culture'
  accessed: '2026-10-25'
---
# Ethical Culture / Ethical Humanism (ETHCUL)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44.

## Summary

Felix Adler’s 1876 New York movement: ethics need not rest on religious dogma; deed over creed; social welfare [S1][S2].

## Core metaphysics

Founder rejected theism; movement open to diverse meaning-quests; no required afterlife or miracle doctrine [S1][S2].

## Position on the LIO axes

A set to 4 (0.7) from Adler’s rejection of theism [S2]; D remains 3; B/C/E UNKNOWN.

## Schools and variants

NY Society; AEU; international Ethical/Humanist unions [S1][S2].

## Science

19th-c. science and criticism in Adler’s formation; reformist practice [S2].

## Coding guidance

Ethical Culture identity → ETHCUL. Broader secular humanism → SECHUM.

## v7.1 scoring note

Authorial v7.1 note unchanged (see front matter).

## Open questions

- A=4 vs UNKNOWN under openness?
- Primary Adler texts for B/C?

## Research log

- Prior family/authority/ethics fills.
- 2026-10-25: deepened TODOs; A scored; axes otherwise unchanged.
- 2026-10-25: B/C/E scored.
