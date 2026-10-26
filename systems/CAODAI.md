---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 6
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S7 for Jason)
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
    summary: 'Draft (systems batch S7): filled from Britannica "Cao Dai" (editors). A 1 (0.5, alt 0);
      B 1 (0.5); C 3 (0.5, alt 4); D 1 (0.5); E UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S6 audit fix: C cites P44(d).'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S7 audit fix: Wayback snapshot URL and timestamp cited under P44(e); B ceiling note.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from Britannica Cao Dai: Ngo Van Chieu 1919/1926, syncretism Confucian-Taoist-Buddhist-Catholic,
      Divine Eye, Tay Ninh. Axes kept.'
identity:
  id: CAODAI
  v7_1_number: 41
  v7_1_label: Caodaism
  display_label: Caodaism
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: religion
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: 'Britannica: modern Vietnamese religious movement.'
  family:
    value: 'Cao Dai ("High Tower"): syncretist Vietnamese religion drawing Confucian ethics, Taoist occult
      practices, Buddhist karma/rebirth, Catholic hierarchy'
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  parent_traditions:
    value:
    - Vietnamese religious culture
    - Confucianism
    - Taoism
    - Buddhism
    - Roman Catholicism (organizational pattern)
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  related_codes:
  - code: BUDDH
    relation: overlaps
    note: karma and rebirth
  - code: TAO
    relation: overlaps
    note: Taoist epithet/practices
  - code: CONFUC
    relation: overlaps
    note: ethical precepts
  - code: CHRIST
    relation: neighbor (easily confused)
    note: pope/cardinals pattern ≠ Catholic identity
origins:
  founding_era:
    value: 1919 revelation to Ngo Van Chieu; formally established 1926
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  founding_region:
    value: Vietnam (Tay Ninh headquarters near Ho Chi Minh City)
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  founders_or_key_figures:
    value:
    - Ngo Van Chieu (prophet)
    - Pham Cong Tac (pope; later exile)
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  key_texts:
  - value: Séance communications / revealed teachings (Britannica does not name a single scripture)
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: Thin on text list.
metaphysics:
  god_nature_relation:
    value: Supreme deity (Cao Dai); God represented as an eye in a triangle on temples.
    stance: creator distinct from creation
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: 0.5 — epithet/symbol; full cosmology thin in S1.
  deity_personal:
    value: Supreme deity communicates (séance); pantheon of saints includes Buddha, Confucius, Jesus,
      Muhammad, Joan of Arc, Victor Hugo, Sun Yat-sen.
    stance: personal
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  intervention:
    value: Communication from supreme deity via séance; ongoing worship.
    stance: regular
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  miracles:
    value: Not addressed in depth.
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: Silence.
  petition_and_prayer:
    value: Elaborate rituals and festivals; séance origin.
    stance: petition answered
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: 0.5.
  afterlife:
    value: Buddhist theories of karma and rebirth drawn upon.
    stance: rebirth
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  moral_ledger:
    value: Karma/rebirth frame from Buddhism; Confucian ethics.
    stance: karma-type law
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: 0.5.
  authority:
    value: Hierarchical organization patterned after Catholicism (pope, cardinals, archbishops); revealed
      communications.
    stance: revelation
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
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
    value: Not addressed.
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: Silence.
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
    rationale: A supreme god who communicates with humans.
    certainty: 0.5
    cites: &id001
    - source: S1
      locator: introduction; history
    how_known: '0.5: the article does not describe the god’s nature further. Alternative 0.'
    alternatives:
    - value: 0
      note: Named alternative.
      cites: *id001
  B_cause:
    value: 1
    rationale: Chieu 'received a communication from the supreme deity during a table-moving séance'.
    certainty: 0.5
    cites:
    - source: S1
      locator: history
    how_known: '0.5: one founding event; no general doctrine of intervention stated. 0.5 is the ceiling:
      the séance is a communication, not a physical intervention (S7 audit).'
  C_ledger:
    value: 3
    rationale: Karma and rebirth taken from Buddhism.
    certainty: 0.5
    cites: &id002
    - source: S1
      locator: introduction
    how_known: 'Karma rule (P44(d)): an impersonal moral ledger is C 3 @0.5, alternative 4. Karma and
      rebirth from Buddhism.'
    alternatives:
    - value: 4
      note: Named alternative.
      cites: *id002
  D_authority:
    value: 1
    rationale: Founded on séance revelation; a Catholic-style hierarchy with a pope.
    certainty: 0.5
    cites:
    - source: S1
      locator: introduction; history
    how_known: 0.5.
  E_scope:
    value: UNKNOWN
    how_known: Not addressed in the sources read.
epistemology:
  value: Séance communication from supreme deity; syncretic drawing on multiple traditions.
  certainty: 1.0
  cites:
  - source: S1
    locator: opening
  how_known: Britannica.
ethics:
  value: Ethical precepts from Confucianism; karma/rebirth from Buddhism.
  certainty: 0.7
  cites:
  - source: S1
    locator: opening
  how_known: Britannica.
practice:
  ritual_and_practice:
    value: Elaborate rituals and festivals; Divine Eye symbol; occult practices from Taoism.
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  community_form:
    value: Catholic-pattern hierarchy; Tay Ninh HQ; diaspora centres; historically political/military
      role in Vietnam.
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
science:
  historical_stance:
    value: Not a science program.
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: Coder reading.
  current_stance:
    value: Not addressed.
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: Silence.
schools_and_variants:
- name: Cao Dai (Tay Ninh mainstream)
  form: modern
  how_it_differs: HQ Tay Ninh; diaspora after 1975.
  lio_difference: Axes kept from prior coding.
  certainty: 1.0
  cites:
  - source: S1
    locator: opening
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: TODO
v7_1_rubric:
  label: authorial v7.1 scores
  L: 8
  P: 8
  E: 6
  V: 6
  X: 4
  total: 32
  scoring_note: Caodaism scores moderately due to its innovative syncretism promoting religious unity,
    offering ethical and spiritual coherence but limited by revelatory elements and modest empirical alignment.
  source: v7.1 data book, section 6 table (tables[4]) row 41 and section 7 scoring notes
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
  use_when: Cao Dai / Caodaist identity.
  do_not_use_when: Generic Vietnamese Buddhism, Catholicism, or Taoism without Cao Dai identity.
  neighbors:
  - code: BUDDH
    relation: neighbor (easily confused)
  - code: CHRIST
    relation: neighbor (easily confused)
  - code: TAO
    relation: neighbor (easily confused)
review:
  data_quality_flags: []
  open_questions:
  - A fuller source on Cao Dai doctrine.
  - Adherents are TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Britannica Editors
  citation: 'The Editors of Encyclopaedia Britannica. "Cao Dai." Encyclopaedia Britannica. https://www.britannica.com/topic/Cao-Dai.
    Wayback Machine snapshot 2026-05-04 19:37:58 UTC: https://web.archive.org/web/20260504193758/https://www.britannica.com/topic/Cao-Dai.'
  url: https://www.britannica.com/topic/Cao-Dai
  accessed: '2026-10-25'
  reliability_note: 'Short unsigned editors’ article. P44(e): read in the Wayback copy (https://web.archive.org/web/20260504193758/https://www.britannica.com/topic/Cao-Dai),
    counted as the full article, no P45 cap. Live page timed out on 2026-10-15, so no live comparison;
    byline in the copy: Britannica Editors.'
---
# Cao Dai (CAODAI)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

Cao Dai is a syncretist Vietnamese religion (formally 1926) combining Confucian ethics, Taoist practices, Buddhist karma/rebirth, and a Catholic-style hierarchy; Divine Eye symbol; Tay Ninh HQ [S1].

## Core metaphysics

Supreme deity (eye in triangle); saint pantheon spanning Buddha to Victor Hugo; karma/rebirth [S1].

## Position on the LIO axes

Axes kept from prior coding (not re-scored this pass).

## Schools and variants

Tay Ninh mainstream; diaspora [S1].

## Science

Not a science program [S1].

## Coding guidance

Cao Dai identity only.

## v7.1 scoring note

> CAODAI (32/50) — Caodaism. Caodaism scores moderately due to its innovative syncretism promoting religious unity, offering ethical and spiritual coherence but limited by revelatory elements and modest empirical alignment.

## Open questions

- Full scripture list and axis re-score when more sources available.

## Research log

- Prior batch: thin fill.
- 2026-10-25: deepened from Britannica Cao Dai. Axes kept.
