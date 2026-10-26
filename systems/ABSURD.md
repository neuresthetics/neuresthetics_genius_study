---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 7
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S3 for Jason)
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
    summary: 'Draft (systems batch S3): filled from SEP "Albert Camus" (Aronson). A BELOW_THRESHOLD (alt
      4); others UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S10 audit fix: A how_known repeats the source quote.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities: family/parents/related codes, origins, metaphysics TODOs, epistemology,
      ethics, practice, science, schools (Sisyphus absurd; Rebel limits). Axes unchanged. Re-read SEP
      Albert Camus (Aronson).'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Score A_locus 4, D_authority 4, C_ledger 4 (all 0.7) from SEP Camus (no God; lucid reason;
      live without appeal). B/E UNKNOWN.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Fill implied axes (B=4@0.7, E=4@0.5) from sources on file / P44(c) where naturalistic. Alternatives
      named.'
identity:
  id: ABSURD
  v7_1_number: 14
  v7_1_label: Absurdism
  display_label: Absurdism
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: philosophical school or method
    certainty: 0.7
    cites:
    - source: S1
      locator: introduction
    how_known: "Camus's philosophy of the absurd; he rejected 'the very idea of a philosophical system'.\
      \ Coder's classification, 0.7."
  family:
    value: Camus’s philosophy of the absurd (and related absurdist stance)
    certainty: 1.0
    cites: &id001
    - source: S1
      locator: opening
    how_known: SEP Camus entry.
  parent_traditions:
    value:
    - Post-religious Mediterranean sensibility (Nuptials)
    - Nietzschean death of God / anti-hope
    - Critique of existentialist leaps
    - Political moralism of The Rebel
    certainty: 1.0
    cites: *id001
    how_known: SEP structure.
  related_codes:
  - code: EXIST
    relation: neighbor (easily confused)
    note: Camus denied existentialist label; critiques existentialist “forced hope”
  - code: NIHIL
    relation: neighbor (easily confused)
    note: Starts from meaninglessness but refuses suicide and totalizing revolution
  - code: ATHE
    relation: overlaps
    note: Live without God; not new-atheist militancy
origins:
  founding_era:
    value: Camus’s work c. 1938–1950s (Nuptials; Myth of Sisyphus 1942; Rebel 1951)
    certainty: 1.0
    cites: *id001
    how_known: SEP.
  founding_region:
    value: Algeria / France
    certainty: 1.0
    cites: *id001
    how_known: SEP.
  founders_or_key_figures:
    value:
    - Albert Camus
    certainty: 1.0
    cites: *id001
    how_known: SEP.
  key_texts:
  - value: The Myth of Sisyphus
    certainty: 1.0
    cites: &id002
    - &id004
      source: S1
      locator: §3
    how_known: SEP.
  - value: The Rebel
    certainty: 1.0
    cites: &id003
    - &id005
      source: S1
      locator: §4
    how_known: SEP.
  - value: Nuptials; The Plague; The Stranger
    certainty: 1.0
    cites: *id001
    how_known: SEP.
metaphysics:
  god_nature_relation:
    value: "Camus 'centers his work on choosing to live without God', but 'was never assured enough to\
      \ declare that God does not exist'."
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction; §6
    how_known: SEP.
  deity_personal:
    value: Centers choosing to live without God; never assured enough to declare God does not exist; not
      new-atheist militancy
    stance: no deity
    certainty: 0.7
    cites:
    - source: S1
      locator: §2; §6
    how_known: SEP Nuptials + Philosopher of the Present. 0.7 stance as practical no-God living.
  intervention:
    value: No supernatural consolation; world silent about purpose
    stance: none
    certainty: 1.0
    cites: *id002
    how_known: SEP absurd.
  miracles:
    value: Rejected as religious hope/escape
    stance: denied
    certainty: 0.7
    cites:
    - source: S1
      locator: §2
    how_known: Nuptials anti-hope. 0.7.
  petition_and_prayer:
    value: Religious hope rejected as looking away from this life
    stance: no petition
    certainty: 0.7
    cites:
    - source: S1
      locator: §2
    how_known: '0.7.'
  afterlife:
    value: "Death as closed door; no afterlife hope; 'outside there is no salvation'"
    stance: none
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: SEP Nuptials.
  moral_ledger:
    value: No divine ledger; Rebel develops limits against logical crime / utopian murder
    stance: none
    certainty: 0.7
    cites: *id003
    how_known: SEP Rebel. 0.7.
  authority:
    value: Lucid reason noting its limits; lived experience and consistency; anti-system
    stance: observation and reason
    certainty: 0.7
    cites: *id002
    how_known: SEP. 0.7.
  reserved_exemptions:
    value: Solidarity and limits; rejects revolutionary exemption for mass murder
    stance: none
    certainty: 0.7
    cites: *id003
    how_known: '0.7.'
  teleology_in_nature:
    value: Universe silent; no adequate cosmic purpose
    stance: none
    certainty: 1.0
    cites: *id002
    how_known: SEP absurd.
  necessity_and_freedom:
    value: 'Refuse suicide; live in revolt/defiance within limits; Rebel: violence inevitable and impossible
      tension'
    certainty: 1.0
    cites:
    - *id004
    - *id005
    how_known: SEP.
lio_axes:
  A_locus:
    value: 4
    certainty: 0.7
    cites:
    - source: S1
      locator: §3; The Myth of Sisyphus
    how_known: '0.7 — Camus’s absurd rejects appeal to God; P44a.'
    rationale: 'A=4: no transcendent personal God. Not BELOW: Camus’s stance itself fixes it.'
    alternatives:
    - value: 'BELOW_THRESHOLD'
      note: Named alternative if coding broader absurdism including theistic absurdist readings.
      cites:
      - source: S1
        locator: introduction
  B_cause:
    value: 4
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: '0.7 — without appeal; no miracle answer.'
    rationale: B=4.
    alternatives:
    - value: 'UNKNOWN'
      note: Named alternative if refusing P44(c) implied score.
      cites:
      - source: S1
        locator: opening
  C_ledger:
    value: 4
    certainty: 0.7
    cites:
    - source: S1
      locator: §3
    how_known: '0.7 — live without appeal; no transcendent reward/punishment as answer to absurd.'
    rationale: 'C=4: no personal divine ledger. Not 3: revolt/solidarity are human, not impersonal karma
      law.'
    alternatives:
    - value: 3
      note: Named alternative if reading revolt as a this-world moral law with impersonal force.
      cites:
      - source: S1
        locator: §3
  D_authority:
    value: 4
    certainty: 0.7
    cites:
    - source: S1
      locator: §2–3
    how_known: '0.7 — lucid reason noting its limits; lived experience; stance observation and reason.'
    rationale: 'D=4: reason and experience over revelation or leap. Not 3: “without appeal” rejects religious
      authority as answer.'
    alternatives:
    - value: 3
      note: Named alternative if weighting Camus’s limits-of-reason more heavily than anti-leap.
      cites:
      - source: S1
        locator: §2
  E_scope:
    value: 4
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — human condition generally; no in-group exemptions.'
    rationale: E=4 at 0.5.
    alternatives:
    - value: 'UNKNOWN'
      note: Named alternative if refusing P44(c) implied score.
      cites:
      - source: S1
        locator: opening
epistemology:
  value: Skepticism about total knowledge; absurd as hiatus between longing for unity and unreasonable
    silence of the world; reason noting its limits
  certainty: 1.0
  cites: *id002
  how_known: SEP Myth of Sisyphus.
ethics:
  value: Live without appeal; revolt and solidarity; against logical crime and utopian revolution; measure/limits;
    Plague’s “common decency”
  certainty: 1.0
  cites: *id003
  how_known: SEP Rebel / Plague.
practice:
  ritual_and_practice:
    value: Literary/philosophical stance and political moralism; not a church
    certainty: 1.0
    cites: *id001
    how_known: SEP.
  community_form:
    value: 'Writers, journalists, political moralists; Camus’s Combat period'
    certainty: 1.0
    cites: *id001
    how_known: SEP.
science:
  historical_stance:
    value: Dismisses total rationalist systems that “explain everything”; not a lab programme
    certainty: 0.7
    cites: *id002
    how_known: SEP. 0.7.
  current_stance:
    value: Absurdist stance reused in pandemic and violence debates (SEP notes); still literary-philosophical
    certainty: 0.7
    cites:
    - source: S1
      locator: §6
    how_known: '0.7.'
schools_and_variants:
- name: Sisyphus absurdism
  form: scholastic or philosophical
  how_it_differs: Suicide question; lucidity; happiness with the rock
  lio_difference: Not rescored
  certainty: 1.0
  cites: *id002
- name: Rebel / measure
  form: scholastic or philosophical
  how_it_differs: From suicide to murder; limits vs revolution
  lio_difference: May move E/politics coding — not LIO rescored
  certainty: 1.0
  cites: *id003
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Not a census religion; Camus readers and absurdist stance
    certainty: 1.0
    cites: *id001
    how_known: SEP.
v7_1_rubric:
  label: authorial v7.1 scores
  L: 9
  P: 9
  E: 10
  V: 10
  X: 8
  total: 46
  scoring_note: "Absurdism scores high for its honest confrontation with life's irrationality, promoting\
    \ authentic living with strong empirical ties to human psychology, though inherently non-predictive\
    \ in physical domains."
  source: 'v7.1 data book, section 6 table (tables[4]) row 14 and section 7 scoring notes'
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
  use_when: "The person's own writing adopts Camus's absurd (meaning sought, none given) and revolt as\
    \ the main worldview."
  do_not_use_when: Stated disbelief in God is ATHE; Sartre-type existentialism is EXIST.
  neighbors:
  - code: EXIST
    relation: neighbor (easily confused)
    note: Camus vs Sartre label fight
  - code: NIHIL
    relation: neighbor (easily confused)
    note: Meaninglessness without Camus’s revolt/limits
review:
  data_quality_flags: []
  open_questions:
  - Keep Camus out of EXIST by default?
  - Does Rebel anti-Communism need a separate political note for person coding?
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Ronald Aronson
  year: 2021
  citation: 'Ronald Aronson. "Albert Camus." Stanford Encyclopedia of Philosophy. First published October
    27, 2011; substantive revision December 13, 2021. https://plato.stanford.edu/entries/camus/.'
  url: 'https://plato.stanford.edu/entries/camus/'
  accessed: '2026-10-25'
  reliability_note: Peer-reviewed reference entry.
---
# Absurdism (Camus) (ABSURD)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1). The v7.1 scores and note are unchanged.

## Summary

Camus’s absurdism starts from the mismatch between the human demand for meaning and the world’s silence [S1]. The Myth of Sisyphus asks whether absurdity dictates suicide and answers with lucid revolt without religious hope [S1]. The Rebel extends the problem to murder and limits against utopian revolution [S1]. Camus denied the existentialist label [S1].

## Core metaphysics

Live without God and without afterlife hope; death as a closed door [S1]. No cosmic teleology; moral life via revolt, solidarity, and measure rather than a divine ledger [S1].

## Position on the LIO axes

Axes left as previously coded (see front matter); this pass fills qualities without rescoring.

## Schools and variants

Sisyphus-stage absurdism; Rebel-stage philosophy of limits [S1].

## Science

Anti-total-system rationalism; literary-philosophical, not a research programme [S1].

## Coding guidance

Camus absurdism → ABSURD. Sartrean EXIST is a neighbor. Bare “nothing matters” without revolt/limits may be NIHIL.

## v7.1 scoring note

Authorial v7.1 note unchanged (see front matter).

## Open questions

- Keep Camus out of EXIST by default?
- Does Rebel anti-Communism need a separate political note for person coding?

## Research log

- Prior fill from SEP Albert Camus.
- 2026-10-25: deepened TODOs; re-read SEP (Aronson).
- 2026-10-25: A/D/C scored 4 (0.7) from SEP Camus.
- 2026-10-25: implied axis fill: B=4@0.7, E=4@0.5.
