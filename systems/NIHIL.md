---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 6
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
    summary: 'Draft (systems batch S3): filled from IEP "Nihilism" (Pratt). A BELOW_THRESHOLD (alt 4);
      others UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'S3 audit RQ3: D_authority UNKNOWN → BELOW_THRESHOLD under P44(b).'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities: family/parents/related codes, origins, metaphysics TODOs, epistemology,
      ethics, practice, science, schools (political, ethical, existential, antifoundational). Axes unchanged.
      Re-read IEP Nihilism (Pratt).'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Score C_ledger 4 (0.7) from IEP Nihilism (moral nihilism: no absolute values / no divine
      ledger). A/D stay BELOW_THRESHOLD; B/E UNKNOWN.'
identity:
  id: NIHIL
  v7_1_number: 18
  v7_1_label: Nihilism
  display_label: Nihilism
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: family of positions
    certainty: 0.7
    cites:
    - source: S1
      locator: introduction
    how_known: "'few philosophers would claim to be nihilists'. 0.7."
  family:
    value: 'Family of views that values/knowledge/purpose lack foundation (ethical, existential, epistemic,
      political senses)'
    certainty: 1.0
    cites: &id001
    - source: S1
      locator: opening
    how_known: IEP definition.
  parent_traditions:
    value:
    - Russian political nihilism (Turgenev/Bakunin era)
    - Nietzschean diagnosis of European nihilism
    - Existential confrontation with meaninglessness
    - Late antifoundational / postmodern receptions
    certainty: 1.0
    cites:
    - source: S1
      locator: §1–4
    how_known: IEP structure.
  related_codes:
  - code: EXIST
    relation: neighbor (easily confused)
    note: Existentialists often answer nihilism rather than affirm it
  - code: ABSURD
    relation: neighbor (easily confused)
    note: Camus fights nihilism’s victory via revolt/limits
  - code: SCEPT
    relation: overlaps
    note: Epistemological nihilism linked to extreme skepticism
  - code: ATHE
    relation: neighbor (easily confused)
    note: 'Death of God is a path, not identical to atheism alone'
origins:
  founding_era:
    value: Term popularized mid-19th c. (Jacobi; Turgenev 1862); Nietzschean crisis diagnosis late 19th
      c.
    certainty: 1.0
    cites:
    - source: S1
      locator: §1–2
    how_known: IEP.
  founding_region:
    value: Europe (Russia political sense; German philosophical diagnosis)
    certainty: 1.0
    cites:
    - source: S1
      locator: §1–2
    how_known: IEP.
  founders_or_key_figures:
    value:
    - Friedrich Nietzsche (central association)
    - Ivan Turgenev (popularization)
    - Max Stirner (often placed among early philosophical nihilists)
    - Russian political nihilists / Bakunin (destruction motif)
    certainty: 1.0
    cites:
    - source: S1
      locator: §1–2
    how_known: IEP.
  key_texts:
  - value: 'Nietzsche, Will to Power notes; Gay Science (death of God context)'
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: IEP.
  - value: 'Turgenev, Fathers and Sons'
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: IEP.
metaphysics:
  god_nature_relation:
    value: "Not addressed directly: 'A true nihilist would believe in nothing'; Nietzsche argued its effects\
      \ would 'destroy all moral, religious, and metaphysical convictions'."
    stance: not addressed
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: IEP.
  deity_personal:
    value: Often tied to death of God / rejection of religious authority; not a positive theology
    stance: no deity
    certainty: 0.7
    cites:
    - source: S1
      locator: §1–2
    how_known: Russian nihilists denounce God; Nietzschean crisis. 0.7 as family tendency.
  intervention:
    value: No divine order assumed
    stance: none
    certainty: 0.7
    cites: *id001
    how_known: '0.7.'
  miracles:
    value: Not a miracle religion
    stance: denied
    certainty: 0.7
    cites: *id001
    how_known: '0.7.'
  petition_and_prayer:
    value: Not a petitionary religion
    stance: no petition
    certainty: 0.7
    cites: *id001
    how_known: '0.7.'
  afterlife:
    value: Not affirmed; cosmic purposelessness themes
    stance: none
    certainty: 0.7
    cites: *id001
    how_known: IEP themes. 0.7.
  moral_ledger:
    value: Ethical nihilism rejects absolute moral values; good/evil as social/emotive products
    stance: none
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: IEP ethical nihilism definition.
  authority:
    value: 'Varies: political nihilism rejects state/church/family authority; epistemic forms deny knowledge
      foundations'
    stance: varies by school
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: IEP.
  reserved_exemptions:
    value: Not a supernatural in-group doctrine; political forms may exempt revolutionary destruction
      as prerequisite
    stance: varies by school
    certainty: 0.5
    cites:
    - source: S1
      locator: §1
    how_known: '0.5.'
  teleology_in_nature:
    value: Cosmic purposelessness; aim lacking
    stance: none
    certainty: 1.0
    cites:
    - source: S1
      locator: §2
    how_known: Nietzsche quote in IEP.
  necessity_and_freedom:
    value: 'Existential nihilism: invent meaning under nothingness; political forms emphasize destruction
      as creative'
    certainty: 0.7
    cites:
    - source: S1
      locator: §1; §3
    how_known: '0.7.'
lio_axes:
  A_locus:
    value: 'BELOW_THRESHOLD'
    how_known: "'A true nihilist would believe in nothing' (S1) implies no God, but the source states\
      \ no position on God (P44b)."
    note: 'Evidence: S1.'
    alternatives:
    - value: 4
      note: Named alternative.
      cites:
      - source: S1
        locator: introduction
  B_cause:
    value: 'UNKNOWN'
    how_known: Not addressed in the sources read.
  C_ledger:
    value: 4
    certainty: 0.7
    cites:
    - source: S1
      locator: Moral Nihilism
    how_known: '0.7 — IEP: moral nihilism denies absolute values; no personal divine reward/punishment
      as family stance.'
    rationale: 'C=4: none / impersonal absence of absolute moral ledger. Not 3: not a karma-type impersonal
      law.'
    alternatives:
    - value: 'BELOW_THRESHOLD'
      note: Named alternative if coding only political nihilism without a moral thesis.
      cites:
      - source: S1
        locator: opening
  D_authority:
    value: 'BELOW_THRESHOLD'
    how_known: "The source addresses knowledge ('nothing can be known'), so it is not silent; IEP separates\
      \ epistemological, moral, existential and cosmic nihilism, which differ here, so members differ\
      \ (P44b)."
    note: "Changed from UNKNOWN after the S3 audit (coder's conservative call)."
  E_scope:
    value: 'UNKNOWN'
    how_known: Not addressed in the sources read.
epistemology:
  value: Epistemological nihilism denies possibility of knowledge/truth; linked to extreme skepticism
    and later antifoundationalism
  certainty: 1.0
  cites:
  - source: S1
    locator: §1; §4
  how_known: IEP.
ethics:
  value: 'Moral nihilism: no absolute values; existential forms face meaninglessness; Nietzsche: highest
    values devalue themselves'
  certainty: 1.0
  cites:
  - source: S1
    locator: §1–2
  how_known: IEP.
practice:
  ritual_and_practice:
    value: Not a church; political terrorism association historically; literary/philosophical diagnosis
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: IEP.
  community_form:
    value: Loose Russian revolutionary identification; later academic/cultural themes
    certainty: 1.0
    cites:
    - source: S1
      locator: §1
    how_known: IEP.
science:
  historical_stance:
    value: Russian nihilism tied to scientism/materialism as sole knowledge source (Bazarov caricature)
    certainty: 0.7
    cites:
    - source: S1
      locator: §1
    how_known: IEP. 0.7.
  current_stance:
    value: Cultural diagnosis more than research programme; antifoundational receptions
    certainty: 0.7
    cites:
    - source: S1
      locator: §4
    how_known: '0.7.'
schools_and_variants:
- name: Political nihilism
  form: modern
  how_it_differs: Destroy existing order as prerequisite for improvement
  lio_difference: May move D/E — not rescored
  certainty: 1.0
  cites:
  - source: S1
    locator: §1
- name: Ethical / moral nihilism
  form: scholastic or philosophical
  how_it_differs: No absolute moral values
  lio_difference: Supports C none reading
  certainty: 1.0
  cites:
  - source: S1
    locator: §1
- name: Existential nihilism
  form: scholastic or philosophical
  how_it_differs: Life has no intrinsic meaning
  lio_difference: Neighbor to EXIST/ABSURD answers
  certainty: 1.0
  cites:
  - source: S1
    locator: §3
- name: Antifoundational / cheerful nihilism
  form: modern
  how_it_differs: Mild acceptance of meaninglessness (Carr/Lyotard/Rorty discussion in IEP)
  lio_difference: Not rescored
  certainty: 1.0
  cites:
  - source: S1
    locator: §4
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Few self-identify; diagnostic/cultural category
    certainty: 1.0
    cites: *id001
    how_known: 'IEP: few claim to be nihilists.'
v7_1_rubric:
  label: authorial v7.1 scores
  L: 9
  P: 9
  E: 10
  V: 10
  X: 8
  total: 46
  scoring_note: 'Nihilism provides a stark, evidence-based critique of meaning, with high coherence in
    its rejection.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 18 and section 7 scoring notes'
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
  use_when: "The person's own writing affirms that all values are baseless (nihilism as held, not diagnosed)."
  do_not_use_when: Do not code Nietzsche or others who diagnose nihilism as NIHIL.
  neighbors:
  - code: EXIST
    relation: neighbor (easily confused)
    note: Answer vs affirmation
  - code: ABSURD
    relation: neighbor (easily confused)
    note: Camus vs nihilism’s victory
  - code: SCEPT
    relation: overlaps
    note: Epistemic branch
review:
  data_quality_flags: []
  open_questions:
  - Should political terrorism-era “nihilist” persons be dual-coded?
  - 'Cheerful antifoundationalism: still NIHIL or a different code?'
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Alan Pratt
  citation: 'Alan Pratt. "Nihilism." Internet Encyclopedia of Philosophy. https://iep.utm.edu/nihilism/.'
  url: 'https://iep.utm.edu/nihilism/'
  accessed: '2026-10-25'
  reliability_note: Peer-reviewed reference entry; undated page.
---
# Nihilism (NIHIL)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44. The v7.1 scores and note are unchanged.

## Summary

Nihilism is the belief that all values are baseless and that nothing can be known or communicated; a true nihilist would believe in nothing [S1]. Senses include political, ethical, existential, and epistemological [S1]. Nietzsche is the central philosophical association; Russian political nihilism popularized the term [S1].

## Core metaphysics

Often post-theistic (death of God / rejection of religious authority) [S1]. Cosmic purposelessness; no absolute moral ledger [S1]. Not a cult religion.

## Position on the LIO axes

Axes left as previously coded (see front matter); this pass fills qualities without rescoring.

## Schools and variants

Political; ethical/moral; existential; antifoundational “cheerful” receptions [S1].

## Science

Historical link to crude scientism in Russian literary caricature; not a research lab [S1].

## Coding guidance

Affirmation of baseless values/meaning → NIHIL. Existentialist answers → EXIST. Camus revolt → ABSURD. Extreme knowledge denial may also touch SCEPT.

## v7.1 scoring note

Authorial v7.1 note unchanged (see front matter).

## Open questions

- Should political terrorism-era “nihilist” persons be dual-coded?
- Cheerful antifoundationalism: still NIHIL or a different code?

## Research log

- Prior fill from IEP Nihilism.
- 2026-10-25: deepened TODOs; re-read IEP (Pratt).
- 2026-10-25: C_ledger scored 4 (0.7).
