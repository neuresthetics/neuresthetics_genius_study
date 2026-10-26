---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 6
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S5 for Jason)
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
    summary: 'Draft (systems batch S5): filled from Britannica "Satanism" (Doyle White). A 4 (0.7, P44a);
      B BELOW_THRESHOLD (alt 2, belief in magic); C, D, E UNKNOWN. v7.1 scores and note unchanged. Not
      reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S5 audit follow-up: kept as is; The Satanic Bible noted as an unverified P45 lead.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from Britannica Satanism: family/parents, metaphysics TODOs, epistemology/ethics/practice/science/schools.
      Axes unchanged (B stays BELOW_THRESHOLD for magic).'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score D_authority 1 (0.7) and C_ledger 4 (0.7) from Britannica Satanism / CoS materials on
      file (LaVey texts; this-world individualism). A already 4.
identity:
  id: LVSAT
  v7_1_number: 29
  v7_1_label: LaVeyan Satanism (Church of Satan)
  display_label: LaVeyan Satanism (Church of Satan)
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: new religious movement
    certainty: 1.0
    cites:
    - source: S1
      locator: Modern religious Satanism
    how_known: Britannica.
  family:
    value: Modern religious Satanism — LaVeyan / Church of Satan (atheistic-symbolic Satan)
    certainty: 1.0
    cites:
    - source: S1
      locator: Modern religious Satanism
    how_known: Britannica.
  parent_traditions:
    value:
    - Romantic reassessment of Satan
    - '20th-c. occult / new religious movements'
    - Right-libertarian individualism (LaVey)
    certainty: 1.0
    cites:
    - source: S1
      locator: Modern religious Satanism
    how_known: Britannica.
  related_codes:
  - code: ATHE
    relation: overlaps
    note: Formally atheistic; Satan as symbol
  - code: OBJCT
    relation: neighbor (easily confused)
    note: Rational egoism / elite individualism adjacent
  - code: HELLEN
    relation: neighbor (easily confused)
    note: Not classical; modern NRM
origins:
  founding_era:
    value: '1966'
    certainty: 1.0
    cites:
    - source: S1
      locator: Modern religious Satanism
    how_known: Britannica.
  founding_region:
    value: 'San Francisco, United States'
    certainty: 1.0
    cites:
    - source: S1
      locator: Modern religious Satanism
    how_known: Britannica.
  founders_or_key_figures:
    value:
    - Anton LaVey
    certainty: 1.0
    cites:
    - source: S1
      locator: Modern religious Satanism
    how_known: Britannica.
  key_texts:
  - value: The Satanic Bible
    author: Anton LaVey
    year: 1969
    certainty: 1.0
    cites:
    - source: S1
      locator: Modern religious Satanism
    how_known: Britannica.
metaphysics:
  god_nature_relation:
    value: "'LaVeyan Satanism was formally atheistic, presenting Satan not as a real being but as a symbol\
      \ of humanity’s animal nature.'"
    stance: no God
    certainty: 1.0
    cites:
    - source: S1
      locator: Modern religious Satanism
    how_known: Britannica.
  deity_personal:
    value: 'Satan presented as symbol of humanity’s animal nature, not a literal being (Church of Satan)'
    stance: no deity
    certainty: 1.0
    cites:
    - source: S1
      locator: Modern religious Satanism
    how_known: Britannica.
  intervention:
    value: No intervening personal Satan-god; magic/ritual intent still affirmed in LaVeyan practice
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: Modern religious Satanism
    how_known: '0.7 — magic complicates clean naturalism.'
  miracles:
    value: "'It nevertheless accepted certain supernaturalist ideas, namely a belief in magic, with LaVeyan\
      \ Satanists performing rituals with magical intent.'"
    stance: affirmed
    certainty: 1.0
    cites:
    - source: S1
      locator: Modern religious Satanism
    how_known: Britannica.
  petition_and_prayer:
    value: Rituals with magical intent; not petition to a literal Satan as deity
    stance: varies by school
    certainty: 0.7
    cites:
    - source: S1
      locator: Modern religious Satanism
    how_known: '0.7 — CoS vs theistic Satanists.'
  afterlife:
    value: Not a central Church of Satan doctrine in Britannica overview
    stance: not addressed
    certainty: 0.5
    cites:
    - source: S1
      locator: Modern religious Satanism
    how_known: '0.5.'
  moral_ledger:
    value: No divine reward/punishment ledger; elite individualism vs “herd”
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: Modern religious Satanism
    how_known: '0.7.'
  authority:
    value: LaVey’s writings and Church of Satan; reason/individual will over Christian dogma
    stance: founder
    certainty: 0.7
    cites:
    - source: S1
      locator: Modern religious Satanism
    how_known: '0.7.'
  reserved_exemptions:
    value: Satanists as elite set apart from the “herd”; magical ritual as special practice
    stance: some
    certainty: 0.7
    cites:
    - source: S1
      locator: Modern religious Satanism
    how_known: '0.7.'
  teleology_in_nature:
    value: No designer teleology; animal nature symbolism
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: Modern religious Satanism
    how_known: '0.7.'
  necessity_and_freedom:
    value: Strong individualism / libertarian emphasis; not a full free-will treatise
    certainty: 0.7
    cites:
    - source: S1
      locator: Modern religious Satanism
    how_known: '0.7.'
lio_axes:
  A_locus:
    value: 4
    rationale: 'Formally atheistic: Satan a symbol, not a real being. A 4 for a no-God system (P44a).'
    certainty: 0.7
    cites:
    - source: S1
      locator: Modern religious Satanism
    how_known: Stated by Britannica; 0.7 because magic keeps a supernaturalist element.
  B_cause:
    value: 'BELOW_THRESHOLD'
    how_known: 'Belief in magic and rituals with magical intent (S1) mean nature is not exceptionless,
      but the source does not say how far magic departs from law.'
    note: 'Alternative: 2.'
    alternatives:
    - value: 2
      note: Named alternative.
      cites:
      - source: S1
        locator: Modern religious Satanism
  C_ledger:
    value: 4
    certainty: 0.7
    cites:
    - source: S1
      locator: ethics
    how_known: '0.7 — this-world individualism; no divine reward ledger.'
    rationale: 'C=4: none.'
    alternatives:
    - value: 3
      note: Named alternative if reading Lex Talionis as impersonal law.
      cites:
      - source: S1
        locator: ethics
  D_authority:
    value: 1
    certainty: 0.7
    cites:
    - source: S1
      locator: Church of Satan; LaVey
    how_known: '0.7 — founder texts (Satanic Bible); stance founder.'
    rationale: 'D=1: founder writings as primary. Not 0: atheistic Satanism is not revelation-of-Satan;
      texts are human.'
    alternatives:
    - value: 0
      note: Named alternative if coding Satanic Bible as revelation-like closed canon.
      cites:
      - source: S1
        locator: opening
    - value: 4
      note: Named alternative if coding only the atheistic naturalism without founder authority.
      cites:
      - source: S1
        locator: opening
  E_scope:
    value: 'UNKNOWN'
    how_known: Not addressed in the sources read.
epistemology:
  value: Formally atheistic / rationalist camp; Satan as symbol; magic still practiced with intent
  certainty: 1.0
  cites:
  - source: S1
    locator: Modern religious Satanism
  how_known: Britannica.
ethics:
  value: Right-wing libertarian principles; individualism; elite apart from ordinary humanity (LaVey);
    contrast TST progressive line as neighbor not this code
  certainty: 1.0
  cites:
  - source: S1
    locator: Modern religious Satanism
  how_known: Britannica.
practice:
  ritual_and_practice:
    value: Rituals with magical intent; ceremonial Church of Satan practice
    certainty: 1.0
    cites:
    - source: S1
      locator: Modern religious Satanism
    how_known: Britannica.
  community_form:
    value: 'Church of Satan (1966, San Francisco); organized NRM'
    certainty: 1.0
    cites:
    - source: S1
      locator: Modern religious Satanism
    how_known: Britannica.
science:
  historical_stance:
    value: '20th-c. new religion after Romantic Satan reassessment; distinct from medieval devil-worship
      accusations'
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; Modern religious Satanism
    how_known: Britannica.
  current_stance:
    value: Small organized presence; culturally visible; distinct from Satanic panic myths
    certainty: 1.0
    cites:
    - source: S1
      locator: Satanic panic; Modern religious Satanism
    how_known: Britannica.
schools_and_variants:
- name: Church of Satan / LaVeyan
  form: modern
  how_it_differs: Atheistic-symbolic Satan; magic; libertarian elite ethos
  lio_difference: Primary for LVSAT scores
  certainty: 1.0
  cites:
  - source: S1
    locator: Modern religious Satanism
- name: 'The Satanic Temple (neighbor, not this code)'
  form: modern
  how_it_differs: Also atheistic-symbolic but progressive politics
  lio_difference: Do not merge into LVSAT
  certainty: 1.0
  cites:
  - source: S1
    locator: Modern religious Satanism
- name: Temple of Set / theistic Satanism
  form: modern
  how_it_differs: Literal Set/Satan; not LaVeyan atheism
  lio_difference: Would move A — keep out of LVSAT
  certainty: 1.0
  cites:
  - source: S1
    locator: Modern religious Satanism
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Small organized NRM; Britannica gives no global census
    certainty: 0.5
    cites:
    - source: S1
      locator: Modern religious Satanism
    how_known: '0.5.'
v7_1_rubric:
  label: authorial v7.1 scores
  L: 9
  P: 9
  E: 9
  V: 9
  X: 7
  total: 43
  scoring_note: 'LaVeyan Satanism scores relatively high as an atheistic philosophy promoting rational
    individualism, with strong empirical and logical alignment, though its symbolic elements slightly
    limit predictive scope.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 29 and section 7 scoring notes'
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
  use_when: Person’s primary identity is Church of Satan / LaVeyan Satanism.
  do_not_use_when: The Satanic Temple progressive activism as primary; theistic Satanism; mere “devil
    worship” moral-panic labels.
  neighbors:
  - code: ATHE
    relation: overlaps
    note: Symbolic atheism
  - code: OBJCT
    relation: neighbor (easily confused)
    note: Egoism adjacent
review:
  data_quality_flags: []
  open_questions:
  - Rescore B if Satanic Bible clarifies magic vs law?
  - Keep TST strictly out of LVSAT?
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Ethan Doyle White; Britannica Editors
  citation: 'Doyle White, Ethan, and Britannica Editors. "Satanism." Encyclopaedia Britannica, updated
    15 October 2026. https://www.britannica.com/topic/Satanism.'
  url: 'https://www.britannica.com/topic/Satanism'
  accessed: '2026-10-25'
  reliability_note: Signed article (historian of religion). Article text only; AI-generated Top Questions
    ignored.
---
# LaVeyan Satanism / Church of Satan (LVSAT)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44. Prior scores unchanged this pass.

## Summary

Church of Satan (Anton LaVey, 1966): Satan as symbol of animal nature; atheistic; rituals with magical intent; libertarian individualism [S1].

## Core metaphysics

No literal Satan-god; magic affirmed; elite-vs-herd ethos [S1].

## Position on the LIO axes

Prior: A4; B BELOW_THRESHOLD (magic); C/D/E UNKNOWN — unchanged.

## Schools and variants

LaVeyan CoS (this code); TST and Temple of Set as neighbors [S1].

## Science

Modern NRM; distinct from historical devil-worship accusations and Satanic panic [S1].

## Coding guidance

LaVeyan / Church of Satan → LVSAT. TST or theistic Satanism → other codes.

## v7.1 scoring note

Authorial v7.1 note unchanged (see front matter).

## Open questions

- Firmer B from primary LaVey texts?
- TST coding separation?

## Research log

- Prior god/miracles fills.
- 2026-10-25: deepened TODOs from Britannica; axes unchanged.
- 2026-10-25: D/C scored.
