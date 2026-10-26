---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 9
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
    summary: 'Draft (systems batch S12, P45 lower tier): filled from Flaherty, "International Raëlian
      Movement", CDAMM (Cambridge). A 4 (0.5, P44(a)); D 1 (0.5, alt 2); B, C, E UNKNOWN. v7.1 scores
      and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S12 audit fix: CDAMM described as a commissioned, edited scholarly dictionary entry (amended
      P45(b)), not peer-reviewed. Values unchanged.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from Encyclopedia.com Raëlians (Palmer): Vorilhon/Raël 1973, Elohim DNA
      creation, atheistic UFO religion, cloning/embassy aims. Keep A=4 D=1; B C E UNKNOWN.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Fill adherents/estimate gloss from existing sources (order-of-magnitude / qualitative). Axes
      unchanged.
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score C_ledger 4 (0.7) and B_cause 3 (0.5) from sources on file (Elohim as technologically
      advanced beings; this-world ethics). A/D already scored.
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score E_scope 4 (0.5) from sources on file. Alternatives named.
  - date: '2026-10-25'
    by: Grok Bot
    summary: Fill reserved_exemptions from Wikipedia Raëlism. No LIO moves.
identity:
  id: RAEL
  v7_1_number: 76
  v7_1_label: Raëlism (Raëlian Movement)
  display_label: Raëlism (Raëlian Movement)
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: religion
    certainty: 0.7
    cites:
    - source: S2
      locator: opening
    how_known: Demands recognition as religion; atheistic UFO religion — 0.7.
  family:
    value: 'Raëlian Movement: atheistic UFO religion; Elohim as extraterrestrial scientific creators;
      Raël final messenger'
    certainty: 1.0
    cites:
    - source: S2
      locator: opening
    how_known: Encyclopedia.com.
  parent_traditions:
    value:
    - '1970s French UFO milieu'
    - Claims continuity with biblical prophets reinterpreted scientifically
    certainty: 1.0
    cites:
    - source: S2
      locator: opening
    how_known: Encyclopedia.com.
  related_codes:
  - code: ATHE
    relation: overlaps
    note: denies God and soul; still ritual/worship of Elohim
  - code: SCIENT
    relation: neighbor (easily confused)
    note: both science-framed NRMs — different cosmologies
  - code: MORMON
    relation: neighbor (easily confused)
    note: Smith listed among prophets in Raëlian teaching
origins:
  founding_era:
    value: '1973 encounter; Madech 1974; Raëlian Movement 1976; Raëlian Religion name 1998 (US)'
    certainty: 1.0
    cites:
    - source: S2
      locator: opening; Organizational
    how_known: Encyclopedia.com.
  founding_region:
    value: France (Puy de Lassolas); HQ Geneva; international
    certainty: 1.0
    cites:
    - source: S2
      locator: opening
    how_known: Encyclopedia.com.
  founders_or_key_figures:
    value:
    - Claude Vorilhon (Raël)
    - Brigitte Boisselier (Clonaid / named successor)
    certainty: 1.0
    cites:
    - source: S2
      locator: opening; Cloning
    how_known: Encyclopedia.com.
  key_texts:
  - value: Le livre qui dit la vérité (1974)
    certainty: 1.0
    cites:
    - source: S2
      locator: opening
    how_known: Encyclopedia.com.
  - value: "Les extra-terrestres m'ont amené sur leur planète (1975)"
    certainty: 1.0
    cites:
    - source: S2
      locator: opening
    how_known: Encyclopedia.com.
  - value: Sensual Meditation (1980)
    certainty: 1.0
    cites:
    - source: S2
      locator: opening
    how_known: Encyclopedia.com.
metaphysics:
  god_nature_relation:
    value: Deny God; Elohim are extraterrestrial scientists who created life via DNA — not supernatural
      God.
    stance: no God
    certainty: 1.0
    cites:
    - source: S2
      locator: opening
    how_known: Encyclopedia.com — A=4 kept.
  deity_personal:
    value: Elohim as personal (loving creators) but material beings; no transcendental God/soul.
    stance: personal
    certainty: 0.5
    cites:
    - source: S2
      locator: opening
    how_known: '0.5 — personal ETs, not deity in theistic sense.'
  intervention:
    value: Past creation and prophetic contacts; expected return by ~2035 if humanity peaceful/scientific.
    stance: rare
    certainty: 0.5
    cites:
    - source: S2
      locator: opening
    how_known: '0.5.'
  miracles:
    value: 'Founding UFO encounters framed as physical events, not supernatural miracles.'
    stance: denied
    certainty: 0.5
    cites:
    - source: S2
      locator: opening
    how_known: '0.5.'
  petition_and_prayer:
    value: Rituals link humans to creators/infinity; not classical petitionary theism.
    stance: no petition
    certainty: 0.5
    cites:
    - source: S2
      locator: opening
    how_known: '0.5.'
  afterlife:
    value: Deny human soul; aspire to physical immortality via cloning; bone sample bank for re-creation
      hope.
    stance: none
    certainty: 0.7
    cites:
    - source: S2
      locator: Organizational
    how_known: Encyclopedia.com.
  moral_ledger:
    value: Ethical system enforced in Structure; not afterlife reward ledger.
    stance: none
    certainty: 0.7
    cites:
    - source: S2
      locator: Practices
    how_known: Encyclopedia.com.
  authority:
    value: Raël as final messenger / guide of guides; Structure hierarchy; ongoing revelations.
    stance: founder
    certainty: 0.7
    cites:
    - source: S2
      locator: Organizational
    how_known: Encyclopedia.com — D=1 kept.
  reserved_exemptions:
    value: "Founder/prophet role (Raël) is unique as messenger; members pursue levels in the structure.\
      \ Not an ethnic exemption from the teaching's ethics."
    stance: some
    certainty: 0.5
    cites:
    - source: S3
      locator: opening
    how_known: '0.5–0.7 — Wikipedia Raëlism.'
  teleology_in_nature:
    value: Scientific creation by Elohim; Age of Apocalypse since Hiroshima; embassy for return.
    stance: "designer's purposes"
    certainty: 0.5
    cites:
    - source: S2
      locator: opening
    how_known: '0.5 — designers are ETs.'
  necessity_and_freedom:
    value: Free choice emphasized in sexual ethics; geniocracy abandoned as political project.
    certainty: 0.5
    cites:
    - source: S2
      locator: Practices; opening
    how_known: Thin.
lio_axes:
  A_locus:
    value: 4
    rationale: "'There is no ‘God’, Raël teaches'; the Elohim are 'an ET race of space-faring bioengineers'\
      \ who 'are not gods, but human beings'."
    certainty: 0.5
    cites:
    - source: S1
      locator: article
    how_known: 'P44(a): no God gives A 4. Capped at 0.5 (P45).'
  B_cause:
    value: 3
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — Elohim as advanced scientists; message via founder; framed as tech not classical
      miracle.'
    rationale: 'B=3: lawlike advanced tech / regularity-leaning. Not 4: special contact events. Not 0:
      not supernatural miracle doctrine in self-description.'
    alternatives:
    - value: 1
      note: Named alternative if coding UFO contact as miracle-class special case.
      cites:
      - source: S1
        locator: opening
    - value: 4
      note: Named alternative if coding full naturalistic reading.
      cites:
      - source: S1
        locator: opening
  C_ledger:
    value: 4
    certainty: 0.7
    cites:
    - source: S1
      locator: ethics
    how_known: '0.7 — pacifism/tolerance ethics; not a divine afterlife ledger as primary.'
    rationale: 'C=4: none as divine personal ledger.'
    alternatives:
    - value: 1
      note: Named alternative if coding Elohim judgment/cloning immortality as personal ledger.
      cites:
      - source: S1
        locator: opening
  D_authority:
    value: 1
    rationale: "Raël 'has been chosen by the Elohim as the Prophet of the Age of Apocalypse'; the message\
      \ rests on his reported encounters with the Elohim."
    certainty: 0.5
    cites: &id001
    - source: S1
      locator: article
    how_known: '0.5: a prophet’s received message is the authority; science is also invoked (‘scientific
      creationism’). Alternative 2.'
    alternatives:
    - value: 2
      note: Named alternative.
      cites: *id001
  E_scope:
    value: 4
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — same physical universe; Elohim as extraterrestrials'
    rationale: 'E=4 at 0.5: same physical laws; UFO contact as naturalized.'
    alternatives:
    - value: 1
      note: Named alternative if coding Elohim contact as in-group miracle.
      cites:
      - source: S1
        locator: opening
epistemology:
  value: "Raël's claimed contacts and books as scientific reinterpretation of Bible; embrace science/tech;\
    \ sensual meditation."
  certainty: 1.0
  cites:
  - source: S2
    locator: opening; Practices
  how_known: Encyclopedia.com.
ethics:
  value: 'Respect for life, pacifism, tolerance, democracy, birth control, sharing resources; Structure
    drug/alcohol abstinence; libertine reputation with enforced Structure ethics.'
  certainty: 1.0
  cites:
  - source: S2
    locator: Practices
  how_known: Encyclopedia.com.
practice:
  ritual_and_practice:
    value: Baptism/transmission of cellular plan; sensual meditation; four festivals; Awakening seminars;
      apostasy act from prior religion.
    certainty: 1.0
    cites:
    - source: S2
      locator: Organizational; Practices
    how_known: Encyclopedia.com.
  community_form:
    value: Structure hierarchy (guides); loose members; Clonaid associated; embassy project (Israel preferred).
    certainty: 1.0
    cites:
    - source: S2
      locator: Organizational; Embassy
    how_known: Encyclopedia.com.
science:
  historical_stance:
    value: Strong pro-science/tech/cloning rhetoric; Clonaid claims unverified publicly.
    certainty: 1.0
    cites:
    - source: S2
      locator: Cloning; opening
    how_known: Encyclopedia.com.
  current_stance:
    value: Science and new technologies liberate from myth of god (Raël quoted).
    certainty: 1.0
    cites:
    - source: S2
      locator: Practices quote
    how_known: Encyclopedia.com.
schools_and_variants:
- name: International Raëlian Movement / Raëlian Religion
  form: modern
  how_it_differs: Mainline Structure under Raël.
  lio_difference: A=4 D=1 kept.
  certainty: 1.0
  cites:
  - source: S2
    locator: opening
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Raëlian movement; small UFO religion; self-reported figures unreliable
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — qualitative from listed source; not a genius-rate denominator.'
v7_1_rubric:
  label: authorial v7.1 scores
  L: 6
  P: 5
  E: 2
  V: 3
  X: 1
  total: 17
  scoring_note: 'Raëlism scores low due to its reliance on unverified extraterrestrial claims and revelation
    over evidence, positioning it as a modern UFO-based movement with limited empirical grounding.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 76 and section 7 scoring notes'
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
  use_when: Raëlian / International Raëlian Movement identity.
  do_not_use_when: Generic UFO interest or cloning advocacy without Raëlian membership. Scientology.
  neighbors:
  - code: ATHE
    relation: neighbor (easily confused)
  - code: SCIENT
    relation: neighbor (easily confused)
  - code: MORMON
    relation: neighbor (easily confused)
review:
  data_quality_flags:
  - 'P45 lower tier only: one signed, editor-commissioned CDAMM dictionary entry (not peer-reviewed).
    Capped at 0.5.'
  open_questions:
  - 'Leads (not read in full): Chryssides, "Is God a Space Alien? The Cosmology of the Raëlian Church",
    Culture and Cosmos (doi 10.46472/cc.0104.0207); Palmer & Sentes, Cambridge Companion chapter (doi
    10.1017/ccol9780521196505.012).'
  - Adherents are TODO.
sources:
- id: S1
  type: secondary
  kind: encyclopedia
  author: Robert Pearson Flaherty
  citation: 'Flaherty, Robert Pearson. "International Raëlian Movement." In James Crossley and Alastair
    Lockhart (eds.), Critical Dictionary of Apocalyptic and Millenarian Movements (CDAMM), Centre for
    the Critical Study of Apocalyptic and Millenarian Movements, University of Cambridge, 15 January 2021.
    https://doi.org/10.17863/CAM.121515. Read in Wayback snapshot 2026-03-07 18:06:21 UTC: https://web.archive.org/web/20260307180621/https://www.cdamm.org/articles/international-raelian-movement.'
  url: 'https://www.cdamm.org/articles/international-raelian-movement'
  accessed: '2026-10-25'
  reliability_note: 'P45 lower tier (b), as amended 2026-10-15: a signed, editor-commissioned scholarly
    reference entry (commissioned and edited by CenSAMM, Cambridge; editors James Crossley and Alastair
    Lockhart). Not described as peer-reviewed. No Britannica, SEP or IEP entry found. Claims capped at
    0.5.'
- id: S2
  type: secondary
  kind: encyclopedia
  citation: 'Susan J. Palmer, "Raëlians," Encyclopedia of Religion (Encyclopedia.com).'
  url: 'https://www.encyclopedia.com/environment/encyclopedias-almanacs-transcripts-and-maps/raelians'
  accessed: '2026-10-25'
- id: S3
  type: tertiary
  kind: encyclopedia
  citation: 'Wikipedia contributors. "Raëlism." Wikipedia. Accessed 2026-10-25.'
  url: 'https://en.wikipedia.org/wiki/Ra%C3%ABlism'
  accessed: '2026-10-25'
---
# Raëlian Movement (RAEL)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

Raëlian Movement: atheistic UFO religion founded by Claude Vorilhon (Raël) after 1973 encounter; Elohim as DNA creators; embassy and cloning aims [S2].

## Core metaphysics

No God/soul; material Elohim creators; physical immortality hope via cloning [S2].

## Position on the LIO axes

- **A: 4, D: 1** kept.
- **B, C, E:** UNKNOWN.

## Schools and variants

Mainline Structure [S2].

## Science

Pro-science/cloning platform; Clonaid claims unverified [S2].

## Coding guidance

Raëlian identity only.

## v7.1 scoring note

> RAEL (17/50) — Raëlism (Raëlian Movement). Raëlism scores low due to its reliance on unverified extraterrestrial claims and revelation over evidence, positioning it as a modern UFO-based movement with limited empirical grounding.

## Open questions

- Whether B (cause) should move given DNA-creation cosmology.

## Research log

- Prior: A=4 D=1; P45.
- 2026-10-25: deepened from Encyclopedia.com Raëlians (Palmer 2005). Axes kept.
- 2026-10-25: adherents/estimate filled (qualitative).
- 2026-10-25: C/B scored.
- 2026-10-25: E_scope scored 4 (0.5).
- 2026-10-25: Filled reserved_exemptions from Wikipedia Raëlism.
