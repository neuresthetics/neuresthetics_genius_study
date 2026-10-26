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
    summary: 'Draft (systems batch S10): filled from Britannica "Sikhism" (McLeod), introduction and Guru
      Nanak pages. A 2 (0.5, alt 1); D 1 (0.5); B, C, E UNKNOWN. v7.1 scores and note unchanged. Not reviewed.'
  - date: '2026-10-15'
    by: Grok Bot
    summary: 'T1: B_cause searched, still UNKNOWN; search logged.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Deepen qualities from Britannica Sikhism (McLeod): Nanak, ten Gurus, Guru Granth Sahib,
      nirgun God, Khalsa, langar. Keep prior axis scores.'
  - date: '2026-10-25'
    by: Grok Bot
    summary: Fill adherents/estimate gloss from existing sources (order-of-magnitude / qualitative). Axes
      unchanged.
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score C_ledger 3 (0.5) rebirth/consequence (P44d-adjacent); B_cause 1 (0.5) Guru spirit /
      scripture. D already 1.
  - date: '2026-10-25'
    by: Grok Bot
    summary: Score E_scope 3 (0.5) from sources on file. Alternatives named.
  - date: '2026-10-25'
    by: Grok Bot
    summary: 'Fill miracles, exemptions, necessity from Wikipedia Sikhism. No LIO moves.'
identity:
  id: SIKH
  v7_1_number: 62
  v7_1_label: Sikhism
  display_label: Sikhism
  label_status: as in v7.1
  aliases: []
classification:
  kind:
    value: religion
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: 'Britannica: religion and philosophy.'
  family:
    value: "Sikhism / Gurmat ('Way of the Guru'): monotheistic Panth founded by Guru Nanak; ten human\
      \ Gurus then Guru Granth Sahib as eternal Guru"
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  parent_traditions:
    value:
    - Sant tradition of northern India (incl. Kabir milieu)
    - 'Vaishnava bhakti (devotional influence, with differences)'
    - Nath meditation concepts (spiritual ascent; rejected physical Hatha Yoga)
    certainty: 1.0
    cites:
    - source: S1
      locator: history and doctrine
    how_known: Britannica.
  related_codes:
  - code: HINDU
    relation: neighbor (easily confused)
    note: Sikhs claim separate tradition; scholars debate early stage
  - code: ISLAM
    relation: neighbor (easily confused)
    note: little direct Islamic doctrine influence per Britannica
  - code: CLASS_THEISM
    relation: overlaps
    note: nirgun monotheism
origins:
  founding_era:
    value: Late 15th century; Guru Nanak (1469–1539); Khalsa 1699; scripture as Guru after Gobind Singh
      (d. 1708)
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  founding_region:
    value: Punjab; majority in Indian Punjab; ~25 million worldwide
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  founders_or_key_figures:
    value:
    - Guru Nanak
    - Nine successor Gurus through Guru Gobind Singh
    - Guru Granth Sahib as eternal Guru
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  key_texts:
  - value: Adi Granth / Guru Granth Sahib (compiled 1604 by Guru Arjan)
    certainty: 1.0
    cites:
    - source: S1
      locator: holy book FAQ
    how_known: Britannica.
  - value: Dasam Granth (lesser reverence)
    certainty: 1.0
    cites:
    - source: S1
      locator: holy book FAQ
    how_known: Britannica.
metaphysics:
  god_nature_relation:
    value: 'One God, nirgun (without form), not incarnated; devotion essential to liberation from rebirth.'
    stance: creator distinct from creation
    certainty: 0.5
    cites:
    - source: S1
      locator: history and doctrine
    how_known: '0.5 vs God-in-all Sant seeing.'
  deity_personal:
    value: One God approached through devotion and Guru; no sagun incarnation.
    stance: personal
    certainty: 0.5
    cites:
    - source: S1
      locator: history and doctrine
    how_known: '0.5.'
  intervention:
    value: Single spirit inhabited ten Gurus; eternal Guru in scripture. Ongoing intervention thin in
      extract.
    stance: not addressed
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: Thin.
  miracles:
    value: 'Emphasis on the Name (Naam) and the Guru Granth Sahib over wonder-working. Sikh tradition
      includes hagiographic miracle stories of the Gurus; mainstream teaching stresses honest work, service,
      and remembrance of the One rather than miracle-seeking.'
    stance: varies by school
    certainty: 0.5
    cites: &id001
    - source: S3
      locator: opening
    how_known: '0.5 — Wikipedia core practices; miracle hagiography not detailed in extract.'
  petition_and_prayer:
    value: 'Bow before Guru Granth Sahib, hymns, ardas prayer.'
    stance: petition answered
    certainty: 0.5
    cites:
    - source: S1
      locator: gurdwara FAQ
    how_known: '0.5.'
  afterlife:
    value: Liberation from cycle of rebirth.
    stance: rebirth
    certainty: 1.0
    cites:
    - source: S1
      locator: history and doctrine
    how_known: Britannica.
  moral_ledger:
    value: Rebirth cycle implies consequence.
    stance: impersonal consequence
    certainty: 0.5
    cites:
    - source: S1
      locator: history and doctrine
    how_known: '0.5.'
  authority:
    value: Guru (human then scripture); Khalsa discipline.
    stance: 'both, revelation first'
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  reserved_exemptions:
    value: 'None ethnic or clerical before Ik Onkar. Equality of humankind is core; rejects monopoly of
      absolute truth by any one tradition. Khalsa discipline is vocation, not cosmic exemption from hukam.'
    stance: none
    certainty: 0.7
    cites: *id001
    how_known: '0.7 — Wikipedia equality / sarbat da bhala.'
  teleology_in_nature:
    value: Sants saw the divine in all things.
    stance: immanent ends
    certainty: 0.5
    cites:
    - source: S1
      locator: history and doctrine
    how_known: '0.5.'
  necessity_and_freedom:
    value: 'Living under hukam (divine order/will) while choosing honest conduct, seva, and Naam. Not
      a Western free-will treatise; moral agency is affirmed in daily discipline.'
    certainty: 0.5
    cites: *id001
    how_known: '0.5 — Wikipedia core beliefs summary.'
lio_axes:
  A_locus:
    value: 2
    rationale: "The Sants held that God is 'nirgun (“without form”)' and 'can be neither incarnated nor\
      \ represented', and saw the divine 'in all things'; for Nanak 'the nam encompasses the whole of\
      \ creation', and grace is 'bestowed by God, or Akal Purakh'."
    certainty: 0.5
    cites: &id002
    - source: S1
      locator: History and doctrine
    - source: S2
      locator: Guru Nanak
    how_known: '0.5: a gracious God beyond form and a divine name in all creation. Alternative 1.'
    alternatives:
    - value: 1
      note: Named alternative.
      cites: *id002
  B_cause:
    value: 1
    certainty: 0.5
    cites:
    - source: S1
      locator: Guru; scripture
    how_known: '0.5 — single spirit inhabited ten Gurus; eternal Guru in scripture; intervention thin.'
    rationale: 'B=1: special revelatory/Guru cases. Not 0: not miracle-centered catalog.'
    alternatives:
    - value: 'UNKNOWN'
      note: Named alternative if intervention evidence too thin.
      cites:
      - source: S1
        locator: opening
  C_ledger:
    value: 3
    certainty: 0.5
    cites:
    - source: S1
      locator: rebirth; liberation
    how_known: '0.5 — rebirth cycle implies impersonal consequence; liberation aim (karma-type).'
    rationale: 'C=3: impersonal. Alternative 1 if personal God as judge primary.'
    alternatives:
    - value: 1
      note: Named alternative if coding personal God judgment as primary.
      cites:
      - source: S1
        locator: God
  D_authority:
    value: 1
    rationale: "The scripture Guru Granth Sahib 'thereafter was regarded as the sole Guru'; the divine\
      \ word (shabad) is heard 'through a grace bestowed by God'."
    certainty: 0.5
    cites:
    - source: S1
      locator: introduction
    - source: S2
      locator: Guru Nanak
    how_known: '0.5: the source does not discuss observation or reason.'
  E_scope:
    value: 3
    certainty: 0.5
    cites:
    - source: S1
      locator: opening
    how_known: '0.5 — Ik Onkar / universal God; langar open'
    rationale: E=3 at 0.5.
    alternatives:
    - value: 4
      note: Named alternative.
      cites:
      - source: S1
        locator: opening
epistemology:
  value: Guidance of the Guru; hymn/scripture; Sikh as learner.
  certainty: 1.0
  cites:
  - source: S1
    locator: opening
  how_known: Britannica.
ethics:
  value: Equality (langar); Khalsa courage/integrity; Five Ks; rejection of caste.
  certainty: 1.0
  cites:
  - source: S1
    locator: practice FAQs
  how_known: Britannica.
practice:
  ritual_and_practice:
    value: 'Gurdwara worship, Adi Granth reverence, langar, Five Ks for Khalsa, ardas.'
    certainty: 1.0
    cites:
    - source: S1
      locator: practice FAQs
    how_known: Britannica.
  community_form:
    value: Panth; gurdwaras; Khalsa; diaspora.
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
science:
  historical_stance:
    value: Not addressed.
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Silence.
  current_stance:
    value: Not addressed.
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    how_known: Silence.
schools_and_variants:
- name: Khalsa / mainstream Gurmat
  form: reform
  how_it_differs: Initiated order 1699; Five Ks.
  lio_difference: Prior SIKH scores.
  certainty: 1.0
  cites:
  - source: S1
    locator: Khalsa FAQ
adherents:
  use: context only — never a genius-rate denominator
  estimate:
    value: 'Sikhism: tens of millions globally (order-of-magnitude; confirm with census when coding persons)'
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: '0.7 — qualitative from listed source; not a genius-rate denominator.'
v7_1_rubric:
  label: authorial v7.1 scores
  L: 8
  P: 7
  E: 4
  V: 4
  X: 2
  total: 25
  scoring_note: 'Sikhism scores moderately due to its strong ethical coherence and emphasis on equality
    and service, which foster social harmony, but its revelatory foundation and supernatural aspects limit
    empirical and predictive alignment.'
  source: 'v7.1 data book, section 6 table (tables[4]) row 62 and section 7 scoring notes'
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
  use_when: Sikh / Gurmat / Khalsa identity.
  do_not_use_when: Generic Sant/bhakti without Sikh Panth identity.
  neighbors:
  - code: HINDU
    relation: neighbor (easily confused)
  - code: ISLAM
    relation: neighbor (easily confused)
review:
  data_quality_flags: []
  open_questions:
  - 'Karma and the moral ledger: not in the pages read.'
  - 'Adherents: Britannica says nearly 25 million (early 21st century); cite a demographic source.'
  - 'T1 (2026-10-15): B_cause search logged in the research log; still UNKNOWN.'
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: William Hewat McLeod
  citation: 'McLeod, William Hewat. "Sikhism." Encyclopaedia Britannica. https://www.britannica.com/topic/Sikhism.
    Wayback Machine snapshot 2026-10-06 08:39:15 UTC: https://web.archive.org/web/20261006083915/https://www.britannica.com/topic/Sikhism.'
  url: 'https://www.britannica.com/topic/Sikhism'
  accessed: '2026-10-25'
  reliability_note: 'Signed article (historian of Sikhism); introduction read. P44(e): read in the Wayback
    copy (https://web.archive.org/web/20261006083915/https://www.britannica.com/topic/Sikhism); live page
    not compared (live Britannica times out from the box).'
- id: S2
  type: tertiary
  kind: encyclopedia
  author: William Hewat McLeod
  citation: 'McLeod, William Hewat. "Sikhism: Guru Nanak." Encyclopaedia Britannica. https://www.britannica.com/topic/Sikhism/Guru-Nanak.
    Wayback Machine snapshot 2026-08-20 15:49:38 UTC: https://web.archive.org/web/20260820154938/https://www.britannica.com/topic/Sikhism/Guru-Nanak.'
  url: 'https://www.britannica.com/topic/Sikhism/Guru-Nanak'
  accessed: '2026-10-25'
  reliability_note: 'Later page of the same signed article. P44(e): read in the Wayback copy (https://web.archive.org/web/20260820154938/https://www.britannica.com/topic/Sikhism/Guru-Nanak);
    live page not compared (live Britannica times out from the box).'
- id: S3
  type: tertiary
  kind: encyclopedia
  citation: 'Wikipedia contributors. "Sikhism." Wikipedia. Accessed 2026-10-25.'
  url: 'https://en.wikipedia.org/wiki/Sikhism'
  accessed: '2026-10-25'
---
# Sikhism (SIKH)

> Status: draft — unreviewed. Filled from the sources listed; LIO axes use the 0–4 scale (P1) under P44 and P45. The v7.1 scores and note are unchanged.

## Summary

Sikhism (Gurmat) is the monotheistic Panth founded by Guru Nanak in late-15th-c. Punjab; ten human Gurus then Guru Granth Sahib as eternal Guru [S1].

## Core metaphysics

Nirgun one God; liberation from rebirth through devotion; Guru authority in person then scripture [S1].

## Position on the LIO axes

Prior scores kept (see YAML).

## Schools and variants

Khalsa; other sects thin in extract [S1].

## Science

Not addressed [S1].

## Coding guidance

Sikh Panth. Not generic HINDU.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> SIKH (25/50) — Sikhism. Sikhism scores moderately due to its strong ethical coherence and emphasis on equality and service, which foster social harmony, but its revelatory foundation and supernatural aspects limit empirical and predictive alignment.

## Open questions

- Fuller doctrine (hukam, maya) for axis refinement.

## Research log

- 2026-10-15 (batch S10): Britannica Sikhism; axes set.
- 2026-10-25: deepened classification, origins, metaphysics, practice. Axes kept.
- 2026-10-25: adherents/estimate filled (qualitative).
- 2026-10-25: C/B scored.
- 2026-10-25: E_scope scored 3 (0.5).
- 2026-10-25: Filled miracles/exemptions/necessity from Wikipedia Sikhism.
