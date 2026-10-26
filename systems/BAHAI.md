---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 10
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
    summary: "Decision P7: E_scope note added. E is not scored in a stub; when it is, score it on the\
      \ world's order (same rules for every kind of being and event, no in-group exceptions in this-world\
      \ events). Salvation and moral community go on C_ledger."
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'Draft (systems batch S7): filled from the Britannica article body ("Bahāʾī Faith", editors,
      revised by Charles Preston). A 0 (0.5, alt 1); D 1 (0.5, alt 2); B, C, E UNKNOWN. v7.1 scores and
      note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S7 audit fix: Wayback snapshot URL and timestamp cited under P44(e).'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'T1: B_cause searched, still UNKNOWN; search logged.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from Britannica Bahāʾī Faith: Báb/Bahā�Deepen qualities from Britannica
      Bahāʾī Faith: Báb/Bahāʾu’llāh, progressive revelation, unity of religions/humanity, no clergy, Universal
      House of Justice. Keep A=0; B C D E UNKNOWN.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Fill adherents/estimate gloss from existing sources (order-of-magnitude / qualitative). Axes
      unchanged.
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score B_cause 2 (0.7) progressive revelation rare; C_ledger 4 (0.5) social ethics emphasis.
      A/D already scored.
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score E_scope 3 (0.5) from sources on file. Alternatives named.
  - date: '2026-10-25'
    by: Grok Bot
    summary: Fill reserved_exemptions and necessity_and_freedom from Wikipedia Baháʼí Faith. No LIO moves.
identity:
  id: BAHAI
  v7_1_number: 39
  v7_1_label: Bahá’í Faith
  display_label: Bahá’í Faith
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: religion
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: 'Britannica: universalist religion.'
  family:
    value: 'Bahāʾī Faith: universalist religion; unity of religions and humanity; progressive divine plan
      via manifestations of God'
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  parent_traditions:
    value:
    - Bābī faith (1844)
    - Twelver Shiʿi Islamic milieu (historical origin)
    - Independent religion after Bahāʾu’llāh
    certainty: 1.0
    cites:
    - source: S1
      locator: history
    how_known: Britannica.
  related_codes:
  - code: ISLAM
    relation: offshoot
    note: historical Bābī/Shiʿi milieu; now independent
  - code: CHRIST
    relation: overlaps
    note: Jesus among prior manifestations
  - code: BUDDH
    relation: overlaps
    note: Buddha among prior manifestations in Bahāʾī teaching
origins:
  founding_era:
    value: Báb 1844; Bahāʾu’llāh declaration 1863; mid-19th century
    certainty: 1.0
    cites:
    - source: S1
      locator: history; opening
    how_known: Britannica.
  founding_region:
    value: Iran / Iraq (declaration); shrines Haifa/Acre (Israel)
    certainty: 1.0
    cites:
    - source: S1
      locator: history; organization
    how_known: Britannica.
  founders_or_key_figures:
    value:
    - The Báb (Mīrzā ʿAlī Moḥammad)
    - Bahāʾu’llāh (Mīrzā Ḥosayn ʿAlī Nūrī)
    - ʿAbd al-Bahā�Ḥosayn ʿAlī Nūrī)
    - ʿAbd al-Bahāʾ
    - Shoghi Effendi Rabbānī
    certainty: 1.0
    cites:
    - source: S1
      locator: history
    how_known: Britannica.
  key_texts:
  - value: 'Writings and spoken words of the Báb, Bahāʾu’llāh, and ʿAbd al-Bahāʾ (sacred literature)'
    certainty: 1.0
    cites:
    - source: S1
      locator: practices
    how_known: Britannica.
metaphysics:
  god_nature_relation:
    value: God in essence unknowable; acts through manifestations; progressive divine plan.
    stance: creator distinct from creation
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: "0.5 — transcendence clear; 'beyond nature' wording not used."
  deity_personal:
    value: 'Manifestations of God (Báb, Bahāʾu’llāh, founders of prior religions) as agents of divine
      plan.'
    stance: personal
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — manifestations personal; essence unknowable.'
  intervention:
    value: Progressive revelation through successive manifestations.
    stance: rare
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5.'
  miracles:
    value: Not a focus of Britannica article.
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: Silence.
  petition_and_prayer:
    value: Daily prayer obligatory; Nineteen Day Feast with prayer and scripture.
    stance: petition answered
    certainty: 0.5
    cites:
    - source: S1
      locator: practices
    how_known: '0.5 — prayer required; answeredness not fixed.'
  afterlife:
    value: Not detailed in S1.
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: Silence in article read.
  moral_ledger:
    value: Social ethics emphasized; not a classic afterlife ledger in S1.
    stance: none
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5.'
  authority:
    value: Sacred writings of Báb/Bahāʾu’llāh/ʿAbd al-Bahāʾ; Universal House of Justice applies laws and
      legislates gaps; no priesthood.
    stance: revelation
    certainty: 0.7
    cites:
    - source: S1
      locator: organization; practices
    how_known: Britannica — D left UNKNOWN per prior coding.
  reserved_exemptions:
    value: 'No clergy caste exemption. Progressive revelation and independent investigation of truth;
      all souls accountable. Administrative order is organizational, not a moral free pass.'
    stance: none
    certainty: 0.5
    cites: &id001
    - source: S2
      locator: opening; Beliefs
    how_known: '0.5 — Wikipedia Baháʼí Faith.'
  teleology_in_nature:
    value: Progressive divine plan for education of humanity — teleology of history more than nature design.
    stance: "designer's purposes"
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5.'
  necessity_and_freedom:
    value: Free will affirmed in Baháʼí teaching alongside divine will; humans choose to turn toward God.
      Not identical to Western libertarian debates.
    certainty: 0.5
    cites: *id001
    how_known: '0.5 — Wikipedia Baháʼí Faith.'
lio_axes:
  A_locus:
    value: 0
    rationale: "God 'in his essence is unknowable' and acts through manifestations, 'agents of a progressive\
      \ divine plan'."
    certainty: 0.5
    cites: &id002
    - source: S1
      locator: introduction
    how_known: '0.5: transcendence is stated; personhood is the coder’s reading of the divine plan. Alternative
      1.'
    alternatives:
    - value: 1
      note: Named alternative.
      cites: *id002
  B_cause:
    value: 2
    certainty: 0.7
    cites:
    - source: S1
      locator: progressive revelation
    how_known: '0.7 — progressive revelation through successive manifestations; intervention rare.'
    rationale: 'B=2: rare special revelation events, not constant miracle regime.'
    alternatives:
    - value: 1
      note: Named alternative if weighting manifestation events as stronger special cases.
      cites:
      - source: S1
        locator: opening
    - value: 3
      note: Named alternative if reading post-manifestation order as lawlike.
      cites:
      - source: S1
        locator: opening
  C_ledger:
    value: 4
    certainty: 0.5
    cites:
    - source: S1
      locator: ethics
    how_known: '0.5 — social ethics emphasized; not a classic afterlife ledger in S1.'
    rationale: C=4 at 0.5. Alternative 1 if personal judgment detailed elsewhere.
    alternatives:
    - value: 1
      note: Named alternative if coding personal afterlife judgment from other sources.
      cites:
      - source: S1
        locator: opening
  D_authority:
    value: 1
    rationale: Sacred literature from the founders; the Universal House of Justice applies their laws
      and legislates where the texts are silent.
    certainty: 0.5
    cites: &id003
    - source: S1
      locator: Practices; Organization
    how_known: '0.5: the article does not discuss reason or science. Alternative 2.'
    alternatives:
    - value: 2
      note: Named alternative.
      cites: *id003
  E_scope:
    value: 3
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — progressive revelation / unity of religions; universalist'
    rationale: 'E=3 at 0.5: same moral order across faiths; not miracle-free naturalism.'
    alternatives:
    - value: 4
      note: Named alternative if reading scientific religion as E=4.
      cites:
      - source: S1
        locator: opening
epistemology:
  value: Progressive revelation; identical truth taught by religions; scripture of all religions recited
    in temples.
  certainty: 1.0
  cites:
  - source: S1
    locator: opening; practices
  how_known: Britannica.
ethics:
  value: 'Unity of humanity; abolish racial, class, religious prejudice; social ethics bulk of teachings;
    monogamy, parental consent, substance abstinence.'
  certainty: 1.0
  cites:
  - source: S1
    locator: opening; practices
  how_known: Britannica.
practice:
  ritual_and_practice:
    value: Daily prayer; Nineteen Day Feast; 19-day fast; no priesthood/ritual forms in worship; houses
      of worship with multi-scripture reading.
    certainty: 1.0
    cites:
    - source: S1
      locator: practices
    how_known: Britannica.
  community_form:
    value: Elected local/national spiritual assemblies; Universal House of Justice (Haifa); no clergy.
    certainty: 1.0
    cites:
    - source: S1
      locator: organization
    how_known: Britannica.
science:
  historical_stance:
    value: Not a science-conflict focus in S1.
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
- name: Mainstream Bahāʾī (Universal House of Justice)
  form: modern
  how_it_differs: Post-Shoghi Effendi elected UHJ governance.
  lio_difference: A=0 kept.
  certainty: 1.0
  cites:
  - source: S1
    locator: organization
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: 'Baháʼí Faith: millions claimed globally (order-of-magnitude; verify when coding)'
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: '0.7 — qualitative from listed source; not a genius-rate denominator.'
v7_1_rubric:
  label: authorial v7.1 scores
  L: 8
  P: 8
  E: 7
  V: 6
  X: 5
  total: 34
  scoring_note: 'Bahá’í Faith scores moderately high due to its innovative emphasis on global unity and
    progressive revelation, fostering ethical and social coherence, but constrained by revelatory authority
    over full empirical alignment.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 39 and section 7 scoring notes'
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
  use_when: "Bahāʾī / Baha'i Faith identity."
  do_not_use_when: Generic progressive Islam or Unitarian-leaning Christianity without Bahāʾī membership.
  neighbors:
  - code: ISLAM
    relation: neighbor (easily confused)
  - code: CHRIST
    relation: neighbor (easily confused)
review:
  data_quality_flags: []
  open_questions:
  - 'A source on reason, science and miracles in Bahāʾī teaching (B, D).'
  - Adherents are TODO.
  - 'T1 (2026-10-15): B_cause search logged in the research log; still UNKNOWN.'
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Britannica Editors
  citation: 'The Editors of Encyclopaedia Britannica. "Bahāʾī Faith." Encyclopaedia Britannica (most recently
    revised and updated by Charles Preston). https://www.britannica.com/topic/Bahai-Faith. Wayback Machine
    snapshot 2026-10-11 10:55:53 UTC: https://web.archive.org/web/20261011105553/https://www.britannica.com/topic/Bahai-Faith.'
  url: 'https://www.britannica.com/topic/Bahai-Faith'
  accessed: '2026-10-25'
  reliability_note: 'Unsigned editors’ article; article body only (AI Top Questions ignored). P44(e):
    read in the Wayback copy (https://web.archive.org/web/20261011105553/https://www.britannica.com/topic/Bahai-Faith),
    counted as the full article, no P45 cap. Live page timed out on 2026-10-15, so no live comparison;
    byline in the copy: Britannica Editors.'
- id: S2
  type: tertiary
  kind: encyclopedia
  citation: 'Wikipedia contributors. "Baháʼí Faith." Wikipedia. Accessed 2026-10-25.'
  url: 'https://en.wikipedia.org/wiki/Bah%C3%A1%CA%BC%C3%AD_Faith'
  accessed: '2026-10-25'
---
# Bahāʾī Faith (BAHAI)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

Bahāʾī Faith: mid-19th-century universalist religion; Báb and Bahāʾu’llāh as manifestations of unknowable God; unity of religions and humanity; social ethics; elected assemblies and Universal House of Justice [S1].

## Core metaphysics

Unknowable God; progressive revelation through manifestations [S1].

## Position on the LIO axes

- **A: 0** — essence unknowable [S1].
- **B, C, D, E:** UNKNOWN (kept).

## Schools and variants

Mainstream UHJ governance [S1].

## Science

Not a focus of S1 [S1].

## Coding guidance

Bahāʾī identity.

## v7.1 scoring note

> BAHAI (34/50) — Bahá’í Faith. Bahá’í Faith scores moderately high due to its innovative emphasis on global unity and progressive revelation, fostering ethical and social coherence, but constrained by revelatory authority over full empirical alignment.

## Open questions

- Afterlife detail and D (revelation) score when Jason wants a rescore.

## Research log

- Prior: A=0 from Britannica.
- 2026-10-25: deepened practices/organization/history. Axes kept.
- 2026-10-25: adherents/estimate filled (qualitative).
- 2026-10-25: B/C scored.
- 2026-10-25: E_scope scored 3 (0.5).
- 2026-10-25: Filled exemptions/necessity from Wikipedia Baháʼí Faith.
