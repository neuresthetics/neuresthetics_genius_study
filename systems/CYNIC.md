---
record:
  record_type: system
  schema_version: '1.1'
  record_version: 8
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
    summary: 'Draft (systems batch S3): filled from IEP "Cynics" (Piering). All axes UNKNOWN: an ethics
      and way of life that neglects metaphysics. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities: family, parent traditions, related codes, remaining metaphysics (not addressed
      / nature), epistemology, practice, science, schools, neighbors; D_authority 3 (0.7). Still unscored
      on A/B/C/E (ethics school, no metaphysics). Sources unchanged (IEP Piering).'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Fill adherents/estimate gloss from existing sources (order-of-magnitude / qualitative). Axes
      unchanged.
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score C_ledger 4 (0.7); A_locus 4 (0.5); raise D_authority 3→4 (0.7) from IEP Cynics (nature/reason;
      neglect of gods; no divine ledger).
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Fill implied axes (B=4@0.5, E=4@0.5) from sources on file / P44(c) where naturalistic. Alternatives
      named.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Clarify thin metaphysics (miracles/afterlife/exemptions) from Wikipedia Cynicism; deepen
      practice note. No invented cosmology; no LIO moves.
identity:
  id: CYNIC
  v7_1_number: 15
  v7_1_label: Cynicism
  display_label: Cynicism
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: philosophical school or method
    certainty: 0.7
    cites:
    - source: S1
      locator: introduction
    how_known: "IEP: calling the Cynics a 'school' 'immediately raises a difficulty'. 0.7."
  family:
    value: Hellenistic Socratic ethics; precursor tradition to Stoicism
    certainty: 1.0
    cites:
    - source: S1
      locator: §2; §5
    how_known: IEP traces lineage Antisthenes–Diogenes–Crates–Zeno and names Stoic inheritance of Cynic
      ethics.
  parent_traditions:
    value:
    - Socratic ethics (claimed lineage)
    - Antisthenes (controversial as first Cynic)
    certainty: 0.7
    cites:
    - source: S1
      locator: introduction; §2
    how_known: 'IEP: Socratic lineage claimed; Antisthenes as original Cynic is controversial. 0.7.'
  related_codes:
  - code: STOIC
    relation: offshoot
    note: Zeno studied under Crates; Stoics inherit living in accord with nature and askēsis
  - code: EPICUR
    relation: neighbor (easily confused)
    note: rival Hellenistic ethics; different goods
  - code: SCEPT
    relation: neighbor (easily confused)
    note: shared suspicion of dogmatic metaphysics
  - code: HELLEN
    relation: neighbor (easily confused)
    note: 'modern Hellenismos is reconstructionist religion, not the ancient Cynic school'
origins:
  founding_era:
    value: 'Classical Greece; a lineage from Antisthenes to Diogenes, Crates and Zeno; as a school it
      ends in the sixth century CE'
    certainty: 1.0
    cites:
    - source: S1
      locator: §1–2
    how_known: IEP.
  founding_region:
    value: Athens
    certainty: 0.7
    cites:
    - source: S1
      locator: §1
    how_known: "IEP: 'the streets of Athens' as setting. 0.7."
  founders_or_key_figures:
    value:
    - Antisthenes
    - Diogenes of Sinope
    - Crates
    certainty: 1.0
    cites:
    - source: S1
      locator: §1–2
    how_known: IEP (Antisthenes as original Cynic is controversial).
  key_texts:
  - value: 'No Cynic treatises survive; tradition via Diogenes Laertius, Book 6, and later literary portraits'
    certainty: 1.0
    cites:
    - source: S1
      locator: introduction
    how_known: "IEP: 'none of the many Cynic texts have survived'; tenets via lives."
metaphysics:
  god_nature_relation:
    value: 'Not a constructive theology. Cynics neglect and often ridicule speculative metaphysics; "living
      in accord with nature" is ethical, not a theistic cosmos model. Some later Cynic-Stoic overlap imports
      more cosmology, but classic Cynicism stays practice-first.'
    stance: not addressed
    certainty: 0.7
    cites: &id001
    - source: S2
      locator: opening
    how_known: '0.7 — Wikipedia + prior IEP/SEP-style notes in file.'
  deity_personal:
    value: "Not a stated doctrine. Diogenes rebukes prayers for wealth and fame as mistaking what is 'truly\
      \ good'; religion as convention is mocked rather than theologized."
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S1
      locator: §3.a
    how_known: "Coder's reading of IEP anecdotes on prayer and convention; no positive theology."
  intervention:
    value: "Not addressed as cosmology. Living 'in accord with nature' replaces petitionary religion as\
      \ the ethical standard."
    stance: not addressed
    certainty: 0.7
    cites:
    - source: S1
      locator: §3
    how_known: IEP ethics section; no miracle doctrine.
  miracles:
    value: Not addressed. Cynic sources ridicule speculative metaphysics and conventional religion; no
      miracle doctrine is part of the school.
    stance: not addressed
    certainty: 0.7
    cites: *id001
    how_known: '0.7 — Wikipedia: reject convention including religious prestige; no miracle catechism.'
  petition_and_prayer:
    value: "Diogenes 'would rebuke men in general with regard to their prayers, declaring that they asked\
      \ for things which seemed to them to be good, not for such as are truly good' (via Diogenes Laertius\
      \ in IEP)."
    stance: no petition
    certainty: 1.0
    cites:
    - source: S1
      locator: §3.a
    how_known: IEP quotation.
  afterlife:
    value: Not addressed as doctrine in sources read. Focus is virtue and self-sufficiency in this life;
      Diogenes exemplars do not teach a heaven/hell path.
    stance: not addressed
    certainty: 0.5
    cites: *id001
    how_known: '0.5 — Wikipedia overview is ethics/askēsis-centred.'
  moral_ledger:
    value: 'No divine judge. Virtue is living in accord with nature; shame attaches to failing to live
      well, not to a personal afterlife ledger.'
    stance: none
    certainty: 0.7
    cites:
    - source: S1
      locator: §3
    how_known: "Coder's reading of Cynic ethics in IEP; no reward/punishment theology stated."
  authority:
    value: 'Nature and reason over nomos (convention), including religious and political authority. Parrhēsia
      (frank speech) against rulers and temples.'
    stance: observation and reason
    certainty: 1.0
    cites:
    - source: S1
      locator: §3; §3.a.i
    how_known: IEP on nature vs convention and parrhēsia.
  reserved_exemptions:
    value: None. No clerical or civic rank exempts one from living in accord with nature; kings and beggars
      alike are under the Cynic demand (Diogenes before Alexander motif).
    stance: none
    certainty: 0.7
    cites: *id001
    how_known: '0.7 — Wikipedia ethical egalitarianism of shameless virtue.'
  teleology_in_nature:
    value: "Nature is the ethical standard for the good life (reason, self-sufficiency, freedom), not\
      \ a designer's purposes in the scholastic sense. Stoics later develop physis more systematically."
    stance: immanent ends
    certainty: 0.5
    cites:
    - source: S1
      locator: §3; §4
    how_known: "IEP: virtue as life in accord with nature; teleology wording is a coder's label. Alt:\
      \ not addressed."
    alternatives:
    - value: not addressed as natural teleology; ethical naturalism only
      cites:
      - source: S1
        locator: §1
  necessity_and_freedom:
    value: 'Freedom (eleutheria), self-sufficiency (autarkeia), and frank speech (parrhēsia) are central
      goods; askēsis trains the self for that freedom against convention.'
    certainty: 1.0
    cites:
    - source: S1
      locator: §3.a.i–ii
    how_known: IEP.
lio_axes:
  A_locus:
    value: 4
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — Cynics neglect/mock religious convention; not a stated atheism (P44a at low certainty).'
    rationale: 'A=4 at 0.5: no personal God doctrine; mockery of prayer for wealth. Alternative UNKNOWN.'
    alternatives:
    - value: 'UNKNOWN'
      note: 'Named alternative: sources do not state a positive atheism.'
      cites:
      - source: S1
        locator: opening
  B_cause:
    value: 4
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — neglect of gods/prayer; nature/reason.'
    rationale: B=4 at 0.5.
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
      locator: ethics
    how_known: '0.7 — virtue with nature; shame for failing to live well; no personal afterlife ledger.'
    rationale: 'C=4: none. Not 3: not karma.'
    alternatives:
    - value: 3
      note: Named alternative if reading living-with-nature as impersonal law.
      cites:
      - source: S1
        locator: ethics
  D_authority:
    value: 4
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: '0.7 — nature and reason over nomos including religion.'
    rationale: 'D=4: reason/nature over revelation. Raised from 3.'
    alternatives:
    - value: 3
      note: Named alternative if weighting askēsis lineage as tradition.
      cites:
      - source: S1
        locator: opening
  E_scope:
    value: 4
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — virtue with nature generally.'
    rationale: E=4 at 0.5.
    alternatives:
    - value: 'UNKNOWN'
      note: Named alternative if refusing P44(c) implied score.
      cites:
      - source: S1
        locator: opening
epistemology:
  value: Practice (askēsis) over theory. Dogmatic and speculative philosophy is ridiculed; living examples
    and parrhēsia carry the teaching. No surviving technical epistemology.
  certainty: 1.0
  cites:
  - source: S1
    locator: introduction; §1
  how_known: IEP.
ethics:
  value: "'virtue is a life lived in accord with nature'; a 'shortcut to virtue'; rejection of nomos (convention)."
  certainty: 1.0
  cites:
  - source: S1
    locator: '§1, §3'
  how_known: IEP.
practice:
  ritual_and_practice:
    value: 'Askēsis: voluntary poverty, public shamelessness, frank speech (parrhēsia), living outdoors/simple.
      Not temple ritual. Exemplars over treatises.'
    certainty: 0.7
    cites: *id001
    how_known: '0.7 — Wikipedia.'
  community_form:
    value: 'Loose school of exemplary teachers (Antisthenes, Diogenes, Crates) rather than a church; later
      Roman Imperial Cynic preachers.'
    certainty: 0.7
    cites: *id001
    how_known: '0.7 — Wikipedia.'
science:
  historical_stance:
    value: No positive natural science programme. Speculative physics and metaphysics are mocked; nature
      is an ethical guide. Stoic physics later develops related themes.
    certainty: 0.7
    cites:
    - source: S1
      locator: §1; §5
    how_known: "Coder's reading of IEP on neglect of speculative philosophy and Stoic legacy."
  current_stance:
    value: "Ancient school ended by the sixth century CE; modern 'cynicism' as distrust is not the school.\
      \ Legacy in philosophy and literature, not a scientific stance."
    certainty: 1.0
    cites:
    - source: S1
      locator: §2; §5
    how_known: IEP.
schools_and_variants:
- name: Classical Cynicism (Diogenes–Crates line)
  form: scholastic or philosophical
  how_it_differs: Way of life and askēsis; virtue as life in accord with nature; anti-convention.
  lio_difference: D scored 3; other axes UNKNOWN for the school as metaphysics.
  certainty: 1.0
  cites:
  - source: S1
    locator: §2–3
- name: Stoic inheritance
  code: STOIC
  form: scholastic or philosophical
  how_it_differs: 'Takes over primacy of ethics, virtue sufficiency, living in accord with nature, askēsis;
    adds systematic physics and a providential logos.'
  lio_difference: 'Stoic God is argued personal/providential; use STOIC, not CYNIC.'
  certainty: 1.0
  cites:
  - source: S1
    locator: §5
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: Historical school (Antiquity); no modern mass membership; philosophical legacy via Stoicism
    certainty: 0.7
    cites:
    - source: S1
      locator: opening; Cynic Legacy
    how_known: '0.7 — qualitative from listed source; not a genius-rate denominator.'
v7_1_rubric:
  label: authorial v7.1 scores
  L: 9
  P: 9
  E: 10
  V: 10
  X: 8
  total: 46
  scoring_note: 'Cynicism scores high for its empirical naturalism and practical virtue ethics, promoting
    self-sufficiency and critiquing conventions, making it a robust philosophy for personal coherence
    despite its ancient origins.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 15 and section 7 scoring notes'
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
  use_when: "The person's own writing or life adopts the Cynic programme: virtue as life in accord with\
    \ nature, against convention."
  do_not_use_when: Modern cynicism (distrust) is not CYNIC. Stoics who followed the Cynics are STOIC.
  neighbors:
  - code: STOIC
    relation: neighbor (easily confused)
  - code: EPICUR
    relation: neighbor (easily confused)
  - code: HELLEN
    relation: neighbor (easily confused)
review:
  data_quality_flags: []
  open_questions:
  - 'Whether any LIO A/B/C/E score can be fixed without reading Diogenes Laertius Book 6 or Branham &
    Goulet-Cazé 1996 in full.'
  - Adherents are TODO (ancient school; not a census category).
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Julie Piering
  citation: 'Julie Piering. "Cynics." Internet Encyclopedia of Philosophy. https://iep.utm.edu/cynics/.'
  url: 'https://iep.utm.edu/cynics/'
  accessed: '2026-10-25'
  reliability_note: Peer-reviewed reference entry; undated page.
- id: S2
  type: tertiary
  kind: encyclopedia
  citation: 'Wikipedia contributors. "Cynicism (philosophy)." Wikipedia. Accessed 2026-10-25.'
  url: 'https://en.wikipedia.org/wiki/Cynicism_(philosophy)'
  accessed: '2026-10-25'
---
# Cynicism (CYNIC)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44. The v7.1 scores and note are unchanged.

## Summary

Cynicism 'originates in the philosophical schools of ancient Greece that claim a Socratic lineage'; its interests are ethical, conceived 'more as a way of living than as a doctrine' [S1]. Diogenes of Sinope 'fervently rejects nomos, or convention' [S1]. Virtue is 'a life lived in accord with nature'; the path is askēsis, a 'shortcut to virtue' [S1].

## Core metaphysics

Speculative philosophy and 'metaphysical essences' are neglected and often ridiculed [S1]. Nature, not convention or petitionary religion, is the ethical standard: Diogenes rebukes prayers for seeming goods rather than true goods [S1]. Freedom, self-sufficiency, and parrhēsia are central [S1].

## Position on the LIO axes

- **A, B, C, E:** UNKNOWN — the school does not fix a cosmology (P44).
- **D_authority: 3** (certainty 0.7; alternative 4) — nature and reason over nomos and religious/political authority [S1].

## Schools and variants

Classical Cynic way of life; Stoicism as successor school that systematizes related ethics [S1]. Modern everyday 'cynicism' is not CYNIC.

## Science

No positive science programme; speculative physics mocked [S1]. Legacy is ethical and literary.

## Coding guidance

The ancient school only. Stoics who followed Cynics are STOIC. Modern distrust is not CYNIC.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> CYNIC (46/50) — Cynicism. Cynicism scores high for its empirical naturalism and practical virtue ethics, promoting self-sufficiency and critiquing conventions, making it a robust philosophy for personal coherence despite its ancient origins.

## Open questions

- Can A/B/C/E be scored from Diogenes Laertius or Branham & Goulet-Cazé without inventing a cosmology?
- Adherents are TODO.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-02: E_scope note added for decision P7 (score E on the world's order when the stub is filled).
- 2026-10-15 (systems batch S3): read the listed sources; quotations checked word for word against the fetched page text with a script. Axes under P44.
- 2026-10-25: deepened classification, metaphysics TODOs, epistemology, practice, science, schools; D_authority 3 (0.7). Re-read IEP Piering.
- 2026-10-25: adherents/estimate filled (qualitative).
- 2026-10-25: A/C scored; D raised to 4.
- 2026-10-25: implied axis fill: B=4@0.5, E=4@0.5.
- 2026-10-25: Clarified miracles/afterlife/exemptions; practice from Wikipedia Cynicism.
