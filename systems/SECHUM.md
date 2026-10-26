---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 5
  review_status: draft — unreviewed
  collected_by: Grok Bot (systems batch S2 for Jason)
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
    summary: 'Draft (systems batch S2): filled from the Council for Secular Humanism page (primary self-definition).
      A, B, C, D 4; E 4 at 0.5. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S2 audit note: Humanist Manifesto II cited as quoted on the Council page.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from Council for Secular Humanism page: metaphysics TODOs, epistemology/ethics/practice/science/origins.
      Axes unchanged.'
identity:
  id: SECHUM
  v7_1_number: 8
  v7_1_label: Secular Humanism
  display_label: Secular Humanism
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: ethical or civic movement
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: "'a comprehensive, non-religious lifestance'. Coder's classification, 0.7."
  family:
    value: Naturalism; secular humanism as comprehensive nonreligious lifestance (eupraxsophy)
    certainty: 1.0
    cites:
    - source: S1
      locator: 'opening; A comprehensive, nonreligious lifestance'
    how_known: Own definition.
  parent_traditions:
    value:
    - Enlightenment freethought
    - American Humanist Association / Humanist Manifestos
    - Council for Secular Humanism (Paul Kurtz)
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; A consequentialist ethical system
    how_known: S1.
  related_codes:
  - code: ATHE
    relation: neighbor (easily confused)
    note: Broader than atheism alone
  - code: AGNOS
    relation: neighbor (easily confused)
    note: Positive lifestance vs suspension
  - code: SUNASM
    relation: overlaps
    note: Secular congregational practice
  - code: ETHCUL
    relation: overlaps
    note: Ethical humanism neighbor
  - code: EMPIR
    relation: overlaps
    note: Science-rooted outlook
origins:
  founding_era:
    value: Mid–late 20th c. institutionalization (Council for Secular Humanism; Humanist Manifesto II
      1973)
    certainty: 1.0
    cites:
    - source: S1
      locator: opening; A consequentialist ethical system
    how_known: S1.
  founding_region:
    value: 'United States (Amherst, NY Council; broader Western freethought)'
    certainty: 0.7
    cites:
    - source: S1
      locator: footer / Center for Inquiry
    how_known: '0.7 — address on page.'
  founders_or_key_figures:
    value:
    - Paul Kurtz
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Named as founder of the Council for Secular Humanism and Free Inquiry.
  key_texts:
  - value: Humanist Manifesto II
    year: 1973
    certainty: 1.0
    cites:
    - source: S1
      locator: A consequentialist ethical system
    how_known: "Quoted on the Council for Secular Humanism page ('No god will save us … we must save ourselves');\
      \ the Manifesto itself was not read."
  - value: A Secular Humanist Declaration
    certainty: 0.7
    cites:
    - source: S1
      locator: Explanations
    how_known: Listed as an explanation on the page; date not given.
metaphysics:
  god_nature_relation:
    value: "'nature (the world of everyday physical experience) is all there is'; 'Naturalism asserts\
      \ that supernatural entities like God do not exist'."
    stance: no God
    certainty: 1.0
    cites:
    - source: S1
      locator: A naturalistic philosophy
    how_known: Own definition.
  deity_personal:
    value: No supernatural beings; nature is all there is
    stance: no deity
    certainty: 1.0
    cites:
    - source: S1
      locator: A naturalistic philosophy
    how_known: S1.
  intervention:
    value: No supernatural intervention; natural world only
    stance: none
    certainty: 1.0
    cites:
    - source: S1
      locator: A naturalistic philosophy
    how_known: S1.
  miracles:
    value: Supernatural entities denied; knowledge without natural appeal unreliable
    stance: denied
    certainty: 1.0
    cites:
    - source: S1
      locator: A naturalistic philosophy
    how_known: S1.
  petition_and_prayer:
    value: Nonreligious lifestance; no petition to gods
    stance: no petition
    certainty: 1.0
    cites:
    - source: S1
      locator: 'A comprehensive, nonreligious lifestance'
    how_known: S1.
  afterlife:
    value: No supernatural realm; undesigned beings via evolution
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: A cosmic outlook rooted in science
    how_known: '0.7 — implied by naturalism.'
  moral_ledger:
    value: "Ethics 'is consequential, to be judged by results', against command ethics 'attributed to\
      \ divine authority'; 'No god will save us … we must save ourselves' (Humanist Manifesto II)."
    stance: none
    certainty: 1.0
    cites:
    - source: S1
      locator: A consequentialist ethical system
    how_known: Own definition.
  authority:
    value: "'reliable knowledge is best obtained when we query nature using the scientific method'."
    stance: observation and reason
    certainty: 1.0
    cites:
    - source: S1
      locator: A naturalistic philosophy
    how_known: Own definition.
  reserved_exemptions:
    value: No reserved supernatural exemptions; same natural methods for all
    stance: none
    certainty: 1.0
    cites:
    - source: S1
      locator: A naturalistic philosophy
    how_known: S1.
  teleology_in_nature:
    value: 'Undesigned, unintended beings through evolution; no designer purposes'
    stance: none
    certainty: 1.0
    cites:
    - source: S1
      locator: A cosmic outlook rooted in science
    how_known: S1.
  necessity_and_freedom:
    value: Moral agency affirmed alongside evolutionary naturalism; not a full free-will treatise
    certainty: 0.7
    cites:
    - source: S1
      locator: A cosmic outlook rooted in science
    how_known: '0.7.'
lio_axes:
  A_locus:
    value: 4
    rationale: Supernatural entities like God do not exist; nature is all there is. A 4 for a no-God system
      (P44a).
    certainty: 1.0
    cites:
    - source: S1
      locator: A naturalistic philosophy
    how_known: Own explicit definition.
  B_cause:
    value: 4
    rationale: 'Nature is all there is, so nothing outside it to make exceptions.'
    certainty: 0.7
    cites:
    - source: S1
      locator: A naturalistic philosophy
    how_known: 'The page states naturalism, not a doctrine of exceptionless law; 0.7.'
  C_ledger:
    value: 4
    rationale: "No divine ledger: ethics judged by results; 'No god will save us'."
    certainty: 0.7
    cites:
    - source: S1
      locator: A consequentialist ethical system
    how_known: "The Council page states it, quoting Humanist Manifesto II (1973) ('No god will save us');\
      \ stated by the system, so 0.7 under P44(c)."
  D_authority:
    value: 4
    rationale: The scientific method; knowledge gained without appeal to the natural world is unreliable.
    certainty: 1.0
    cites:
    - source: S1
      locator: A naturalistic philosophy
    how_known: Own explicit statement.
  E_scope:
    value: 4
    rationale: "On the world's order (P7): nature is all there is, so no agent to exempt a group."
    certainty: 0.5
    cites:
    - source: S1
      locator: A naturalistic philosophy
    how_known: 'Implied by the naturalist stance, not stated: 0.5 under P44(c).'
epistemology:
  value: Reliable knowledge via querying nature with the scientific method; impartial multi-observer review
  certainty: 1.0
  cites:
  - source: S1
    locator: A naturalistic philosophy
  how_known: S1.
ethics:
  value: Consequentialist ethics judged by results; develop principles by examining outcomes in real lives;
    rejects command ethics from divine authority
  certainty: 1.0
  cites:
  - source: S1
    locator: A consequentialist ethical system
  how_known: S1.
practice:
  ritual_and_practice:
    value: Lifestance / eupraxsophy orienting a complete life; free inquiry; no sacred supernatural ritual
      required
    certainty: 1.0
    cites:
    - source: S1
      locator: 'A comprehensive, nonreligious lifestance'
    how_known: S1.
  community_form:
    value: Council for Secular Humanism / Free Inquiry network; freethinker and humanist associations
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: S1.
science:
  historical_stance:
    value: Rooted in Enlightenment science and modern evolutionary outlook
    certainty: 1.0
    cites:
    - source: S1
      locator: A cosmic outlook rooted in science
    how_known: S1.
  current_stance:
    value: 'Commitment to science, democracy, and freedom as stated principles'
    certainty: 1.0
    cites:
    - source: S1
      locator: Kurtz quote
    how_known: S1.
schools_and_variants:
- name: Council for Secular Humanism / Kurtz line
  form: modern
  how_it_differs: Eupraxsophy; Free Inquiry institutional home
  lio_difference: Not rescored
  certainty: 1.0
  cites:
  - source: S1
    locator: opening
- name: Broader secular humanist / Manifesto tradition
  form: popular
  how_it_differs: Overlaps AHA and Manifesto readers without Council membership
  lio_difference: Not rescored
  certainty: 0.7
  cites:
  - source: S1
    locator: A consequentialist ethical system
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Organizational network and self-identifiers; not a global census religion
    certainty: 0.5
    cites:
    - source: S1
      locator: Kurtz quote
    how_known: '0.5 — no count on page.'
v7_1_rubric:
  label: authorial v7.1 scores
  L: 10
  P: 10
  E: 10
  V: 10
  X: 9
  total: 49
  scoring_note: 'Secular Humanism scores near-perfect by integrating rational ethics with empirical science,
    promoting human flourishing without dogma, though its focus on welfare adds a minor subjective layer.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 8 and section 7 scoring notes'
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
  use_when: 'v7.1 coding rule (Atheism vs Agnosticism): ATHE = positive naturalism. AGNOS = explicit suspension.
    SECHUM if the public identity is humanist movement rather than metaphysics.'
  do_not_use_when: Do not use for a person whose only stated view is disbelief in God (ATHE) or suspension
    (AGNOS); SECHUM needs a humanist public identity or the lifestance (S1).
  neighbors:
  - code: ATHE
    relation: neighbor (easily confused)
    note: Metaphysics alone ≠ SECHUM
  - code: AGNOS
    relation: neighbor (easily confused)
    note: Suspension ≠ lifestance
  - code: SUNASM
    relation: overlaps
    note: Congregational secular
review:
  data_quality_flags: []
  open_questions:
  - Score E (agency) more firmly from moral-agency language?
  - Manifesto II full text vs page paraphrase
sources:
- id: S1
  type: primary
  kind: institutional page
  author: Council for Secular Humanism (Free Inquiry)
  citation: 'Council for Secular Humanism. "What is Secular Humanism?" Free Inquiry. https://secularhumanism.org/what-is-secular-humanism/.'
  url: 'https://secularhumanism.org/what-is-secular-humanism/'
  accessed: '2026-10-25'
  reliability_note: "The movement's own page (primary for self-definition); undated. Britannica has no\
    \ 'secular humanism' article (404)."
---
# Secular humanism (SECHUM)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44. Prior axis scores unchanged this pass.

## Summary

Comprehensive nonreligious lifestance: naturalistic philosophy, science-rooted cosmic outlook, consequentialist ethics [S1].

## Core metaphysics

Nature is all there is; no supernatural God or realm [S1].

## Position on the LIO axes

Prior scores unchanged (naturalism → high A/B; no divine ledger).

## Schools and variants

Council / Kurtz institutional line; broader Manifesto humanism [S1].

## Science

Science as method and cosmic outlook [S1].

## Coding guidance

Humanist public identity / lifestance → SECHUM. Mere disbelief → ATHE. Suspension → AGNOS.

## v7.1 scoring note

Authorial v7.1 note unchanged (see front matter).

## Open questions

- Score E (agency) more firmly from moral-agency language?
- Manifesto II full text vs page paraphrase?

## Research log

- Prior partial naturalism/ethics fills.
- 2026-10-25: deepened TODOs from Council page; axes unchanged.
