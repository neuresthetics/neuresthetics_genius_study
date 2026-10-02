---
record:
  record_type: system
  schema_version: "1.1"
  record_version: 4
  review_status: "example — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, repo setup)"
  model_used: "Grok Bot executor agent; direct reads of the cited encyclopedia entries"
  collected_on: 2026-10-01
  last_updated: 2026-10-01
  change_log:
    - {date: 2026-10-01, by: scripts/make_system_stubs.py, summary: "Stub created from v7.1 data book table 4 and section 7."}
    - {date: 2026-10-01, by: "Grok Bot", summary: "Worked example: sourced fields filled from SEP entries; LIO axes scored on the proposed 0–4 scale; revised rubric left for Jason. Not reviewed."}
    - {date: 2026-10-01, by: "Grok Bot", summary: "Display label set to the full original V6 label, approved by Jason 2026-10-01 (OPEN_DECISIONS S2). Source: V6_(history)/V6/beliefCoherence.json, PANT entry, field belief_system (v7 repo). v7_1_label unchanged."}
    - {date: 2026-10-01, by: "Grok Bot", summary: "Schema 1.1. LIO scale approved (P1); the five scores were rechecked and are valid on it. Coding guidance adds the PANT boundary rules (S6); the two open questions they settle are removed."}
identity:
  id: PANT
  v7_1_number: 6
  v7_1_label: "Pantheism (Spinozistic/naturalistic 'God = Univers…"
  display_label: "Pantheism (Spinozistic/naturalistic 'God = Universe')"
  label_status: "approved"
  aliases: ["Deus sive Natura", "Spinozism (core form)"]
classification:
  kind: {value: "family of positions", certainty: 1.0, cites: [{source: S1, locator: "introduction"}], how_known: "SEP: pantheism 'should not be thought of as a single codifiable position' but as 'a diverse family of distinct doctrines'. The study's code covers the Spinozistic core of that family (see coding_guidance)."}
  family: {value: "Monism: God identified with the cosmos (positively) or not distinct from it (negatively)", certainty: 1.0, cites: [{source: S1, locator: "introduction; §4"}], how_known: "SEP definition; 'practically all pantheists are monists (of some sort)'."}
  parent_traditions:
    value: ["Stoic physicalist pantheism", "Renaissance pantheism (Giordano Bruno)", "Cartesian and Jewish philosophical background of Spinoza"]
    certainty: 0.5
    cites: [{source: S1, locator: "§4 (Bruno), §6 (Stoics)"}, {source: S2, locator: "§1 Biography"}]
    how_known: "S1 names the Stoics and Bruno as earlier pantheists. Reading them as 'parents' of the Spinozistic form is a coder's reconstruction, and the third item is a TODO placeholder until a source on Spinoza's influences is read."
  related_codes:
    - {code: ATHE, relation: "neighbor (easily confused)", note: "shares the no-exemption stance; differs on the entity-term (v7.1 two-lane paper, LIO section)"}
    - {code: PANENT, relation: "neighbor (easily confused)", note: "God includes the world but also exceeds it"}
    - {code: PANDEI, relation: "neighbor (easily confused)"}
    - {code: PANPSY, relation: "neighbor (easily confused)"}
    - {code: STOIC, relation: "parent tradition", note: "SEP treats Stoic physicalism as an ancient form of pantheism"}
    - {code: IDEAL, relation: "overlaps", note: "Absolute Idealist pantheism (Fichte, Schelling, Hegel)"}
    - {code: DETERM, relation: "overlaps", note: "Spinoza's necessitarianism"}
origins:
  founding_era: {value: "Ideas ancient; the word 'pantheism' first appears in John Toland (1705); the Spinozistic form the study uses is from Spinoza's Ethics (published 1677).", certainty: 1.0, cites: [{source: S1, locator: "introduction"}, {source: S2, locator: "§1 Biography"}], how_known: "SEP entries."}
  founding_region: {value: "No single origin (pantheist ideas appear in many traditions). The Spinozistic form is from the Dutch Republic (Amsterdam, Voorburg, The Hague).", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "§1 Biography"}], how_known: "SEP entries."}
  founders_or_key_figures: {value: ["Baruch Spinoza", "the Stoics", "Giordano Bruno", "John Toland (coined the term)", "Hegel (Absolute Idealist form)"], certainty: 1.0, cites: [{source: S1, locator: "introduction; §4; §6; §10"}], how_known: "Named as pantheists or pantheist sources in the SEP entry."}
  key_texts:
    - {value: "Ethics, Demonstrated in Geometrical Order", author: "Baruch Spinoza", year: 1677, certainty: 1.0, cites: [{source: S1, locator: "Bibliography"}, {source: S2, locator: "§1, §2"}], how_known: "SEP bibliography and biography."}
    - {value: "Theological-Political Treatise", author: "Baruch Spinoza", year: 1670, certainty: 1.0, cites: [{source: S2, locator: "§1, §3"}], how_known: "SEP: published anonymously in 1670."}
    - {value: "Cause, Principle and Unity", author: "Giordano Bruno", year: 1584, certainty: 1.0, cites: [{source: S1, locator: "§4; Bibliography"}], how_known: "SEP."}
    - {value: "Socinianism truly stated (first use of 'pantheist')", author: "John Toland", year: 1705, certainty: 0.7, cites: [{source: S1, locator: "introduction; Bibliography"}], how_known: "SEP says the term 'possibly' first appears in Toland (1705)."}
metaphysics:
  god_nature_relation: {value: "One substance, 'God, or Nature' (Deus, sive Natura). God is 'the universal, immanent and sustaining cause of all that exists', not a transcendent creator of a world distinct from himself.", stance: identity, certainty: 1.0, cites: [{source: S2, locator: "§2.1 God or Nature"}, {source: S1, locator: "§4 (1) Substance identity; §4 (3)"}], how_known: "Both SEP entries."}
  deity_personal: {value: "In Spinoza, God has infinite intellect but no will or purposes in the ordinary sense, and does not act for ends. Across the pantheist family, whether God is personal is disputed: many pantheists deny it (Einstein among them), others affirm it.", stance: "both / disputed", certainty: 1.0, cites: [{source: S1, locator: "§12 Personal"}, {source: S2, locator: "§2.1"}], how_known: "SEP gives both sides."}
  intervention: {value: "None. There are no departures from the necessary course of nature.", stance: none, certainty: 1.0, cites: [{source: S2, locator: "§2.1"}], how_known: "SEP exposition of Ethics I, Appendix."}
  miracles: {value: "Miracles as divinely caused departures from nature are impossible; belief in them comes from ignorance of natural causes.", stance: denied, certainty: 1.0, cites: [{source: S2, locator: "§2.1; §3.1 (TTP ch. 6)"}], how_known: "SEP exposition of the Ethics and the TTP."}
  petition_and_prayer: {value: "Most pantheists have held that the universe cannot be petitioned. Exceptions such as Fechner treat the cosmos as conscious. For Spinoza, God does not judge, plan or need placating.", stance: "no petition", certainty: 1.0, cites: [{source: S1, locator: "§17"}, {source: S2, locator: "§2.1"}], how_known: "SEP entries."}
  afterlife: {value: "No personal immortality is the common pantheist position. Spinoza's claim that 'something' of the mind 'remains which is eternal' (Ethics 5p23) is disputed.", stance: "impersonal survival or eternity", certainty: 0.5, cites: [{source: S1, locator: "§17"}], how_known: "Contested in the literature.", alternatives: [{value: "Spinoza denies the immortality of the soul.", cites: [{source: S2, locator: "§1 Biography"}]}]}
  moral_ledger: {value: "No judging God who rewards and punishes; Spinoza rejects that picture as anthropomorphic, and SEP's summary says it lets 'opportunistic preachers' play on people's hopes and fears.", stance: none, certainty: 0.7, cites: [{source: S2, locator: "§2.1"}], how_known: "Coder's reading of SEP's exposition of Ethics I, Appendix."}
  authority: {value: "Reason and knowledge of nature. Prophets had vivid imaginations but no privileged knowledge, and their pronouncements set no limits on what reason may believe about nature.", stance: "observation and reason", certainty: 1.0, cites: [{source: S2, locator: "§3.1 On Religion and Scripture"}], how_known: "SEP exposition of the TTP."}
  reserved_exemptions: {value: "None: 'nothing stands outside of nature, not even the human mind'; the same laws hold everywhere.", stance: none, certainty: 1.0, cites: [{source: S2, locator: "§2.4 Passion and Action"}], how_known: "SEP exposition of Ethics III."}
  teleology_in_nature: {value: "None. God or Nature acts for no ends; final causes are a human fiction.", stance: none, certainty: 1.0, cites: [{source: S2, locator: "§2.1"}], how_known: "SEP exposition of Ethics I, Appendix."}
  necessity_and_freedom: {value: "Everything follows from God's nature with necessity, on the model of theorems following from axioms. Critics have long objected that this rules out free will.", certainty: 1.0, cites: [{source: S2, locator: "§2.1"}, {source: S1, locator: "§4 (3)"}], how_known: "SEP entries."}
lio_axes:
  A_locus: {value: 4, rationale: "LIO pole: God is identical with Nature, not a person outside it.", certainty: 1.0, cites: [{source: S2, locator: "§2.1"}], how_known: "Scored on the 0–4 scale (decision P1) from the sourced metaphysics above."}
  B_cause: {value: 4, rationale: "LIO pole: no miracles, no petition, no departures from law.", certainty: 1.0, cites: [{source: S2, locator: "§2.1; §3.1"}], how_known: "0–4 scale (P1)."}
  C_ledger: {value: 4, rationale: "LIO pole: no personal reward and punishment by God. Scored on the Spinozistic form; the afterlife question is contested (see metaphysics/afterlife).", certainty: 0.7, cites: [{source: S2, locator: "§2.1"}], how_known: "0–4 scale (P1); certainty follows the moral_ledger reading."}
  D_authority: {value: 4, rationale: "LIO pole: prophecy gives no privileged knowledge of nature; reason decides.", certainty: 1.0, cites: [{source: S2, locator: "§3.1"}], how_known: "0–4 scale (P1)."}
  E_scope: {value: 4, rationale: "LIO pole: the same laws for everything, human emotions included ('as if it were a Question of lines, planes, and bodies').", certainty: 1.0, cites: [{source: S2, locator: "§2.4"}], how_known: "0–4 scale (P1)."}
epistemology: {value: "Knowledge is of adequate ideas, which grasp the necessity of things 'under a species of eternity'. The Ethics is set out in geometrical order: definitions, axioms, propositions, demonstrations.", certainty: 1.0, cites: [{source: S2, locator: "§2.3 Knowledge"}, {source: S1, locator: "Bibliography (full title of the Ethics); §4 (3)"}], how_known: "SEP entries."}
ethics: {value: "A wider concern in place of selfishness. For Spinoza the highest human happiness is the intellectual love of God.", certainty: 1.0, cites: [{source: S1, locator: "§16; §17"}], how_known: "SEP."}
practice:
  ritual_and_practice: {value: "No ritual is required. Whether worship, love and gratitude can properly be directed at the cosmos is debated; petition is mostly rejected.", certainty: 0.7, cites: [{source: S1, locator: "§17"}], how_known: "SEP treats this as an open philosophical question rather than describing an organised practice."}
  community_form: {value: TODO, note: "Check whether any organised modern pantheist body exists and is documented in a reliable source; do not use self-description alone."}
science:
  historical_stance: {value: "Spinoza explains every event, including miracles and prophecy, through natural causes and universal laws, which put him at odds with the religious authorities of his day.", certainty: 1.0, cites: [{source: S2, locator: "§2.1; §2.4; §3.1"}], how_known: "SEP."}
  current_stance: {value: "Scientific or naturalistic pantheism makes no ontological commitments beyond those of empirical science, and some forms deny nature any intrinsic value.", certainty: 1.0, cites: [{source: S1, locator: "§6 (1); §13"}], how_known: "SEP."}
schools_and_variants:
  - {name: "Spinozistic substance monism (the study's core form)", form: "scholastic or philosophical", how_it_differs: "One substance, God or Nature, known under infinite attributes; strict necessity; no teleology.", lio_difference: "All five axes at the LIO pole.", certainty: 1.0, cites: [{source: S2, locator: "§2.1"}, {source: S1, locator: "§4 (1)"}]}
  - {name: "Stoic physicalist pantheism", code: STOIC, form: "scholastic or philosophical", how_it_differs: "Only bodies exist; the divine is the active pneuma or logos. It has been argued that the Stoics believed in a personal deity and prayed.", lio_difference: "If the Stoic deity was personal, A and B may sit below the pole. TODO.", certainty: 0.7, cites: [{source: S1, locator: "§6 (1); §12"}]}
  - {name: "Scientific or naturalistic pantheism (modern)", form: modern, how_it_differs: "Drops infinity, necessity and other classical divine attributes; nothing beyond empirical science; sometimes no intrinsic value in nature.", lio_difference: "Close to ATHE on exemptions. Whether the entity-term (the circle) survives is the coding question.", certainty: 1.0, cites: [{source: S1, locator: "§6 (1); §10; §13"}]}
  - {name: "Absolute Idealist pantheism (Fichte, Schelling, Hegel, British Idealists)", code: IDEAL, form: "scholastic or philosophical", how_it_differs: "One spiritual reality; the physical world is its partial manifestation; often teleological, with God fully realised at the end of history.", lio_difference: "Teleology moves away from the LIO pole on B/C. TODO.", certainty: 1.0, cites: [{source: S1, locator: "§4 (4); §6 (2)"}]}
  - {name: "Pantheist strands in religious traditions (Advaita Vedanta, some Kabbalah, Sufi mysticism, Celtic spirituality)", form: mystical, how_it_differs: "Pantheist ideas inside a wider religion, e.g. Ibn 'Arabi's unity of being.", lio_difference: "Depends on the host tradition. v7.1's PANENT label also names 'some Kabbalah/Advaita forms', so coders must decide which code a given person fits.", certainty: 1.0, cites: [{source: S1, locator: "§1; §4 (2)"}]}
adherents:
  use: "context only — never a genius-rate denominator"
  estimate: {value: TODO, note: "Pantheism is not a standard census category; any figure would come from self-identification surveys."}
v7_1_rubric:
  label: "authorial v7.1 scores"
  L: 10
  P: 10
  E: 10
  V: 10
  X: 9
  total: 49
  scoring_note: "Pantheism as the circle: entity applied to Nature and Nature rendered in entity. Not God deleted. Petition splits mapping from mapped. Scores near-perfect for a no-exemption cosmos."
  source: "v7.1 data book, section 6 table (tables[4]) row 6 and section 7 scoring notes"
revised_rubric:
  status: "not started"
  L: {score: TODO, rationale: ""}
  P: {score: TODO, rationale: ""}
  E: {score: TODO, rationale: ""}
  V: {score: TODO, rationale: ""}
  X: {score: TODO, rationale: ""}
coding_guidance:
  use_when: "v7.1 coding rule (Pantheism): Use PANT only for the circle: Deus sive Natura, entity-in-Nature and Nature-in-entity. Not atheism-plus-poetry. Not every nature-mystic. v8 two-part test (decision S6, 2026-10-01): the person's own writing (1) identifies God or the divine with Nature as a whole, as a claim about what exists and not a figure of speech, and (2) gives the whole at least one mark beyond feeling: unity as one substance or order, necessity or eternity, something mind-like, or value (S1 §5, §10, §12, §13). Both parts are needed."
  do_not_use_when: "Naturalism that drops the entity-term, or reverent language that fails the two-part test (code ATHE; SECHUM if the public identity is the humanist movement; AGNOS for explicit suspension). God includes the world but also exceeds it (PANENT). Advaita Vedanta or Kabbalah by membership alone (code the host tradition, HINDU or JUDA; PANENT if the writing keeps a God beyond the world). Ancient Stoics and avowed Stoics (STOIC: the Stoic God is providential and can be prayed to). Nature-feeling without a stated metaphysics (leave blank, or BELOW_THRESHOLD). Heritage or childhood upbringing alone (never a code)."
  neighbors:
    - {code: ATHE, relation: "neighbor (easily confused)"}
    - {code: PANENT, relation: "neighbor (easily confused)"}
    - {code: PANDEI, relation: "neighbor (easily confused)"}
    - {code: PANPSY, relation: "neighbor (easily confused)"}
    - {code: STOIC, relation: "neighbor (easily confused)"}
review:
  data_quality_flags:
    - "The v7.1 label is cut off mid-word in both the data book table and the Word file. The display label is the full original from V6_(history)/V6/beliefCoherence.json (PANT entry, belief_system), approved 2026-10-01 (OPEN_DECISIONS S2). v7_1_label is kept verbatim, truncated."
    - "v7.1's PANENT label includes 'some Kabbalah/Advaita forms', while SEP lists Advaita Vedanta and some Kabbalah as pantheist. Settled by decision S6: host tradition by default, PANENT for a God beyond the world, PANT only if the two-part test is passed."
  open_questions:
    - "S2 (§2.1) discusses whether identifying God with Nature makes Spinoza a pantheist or an atheist. The PANT/ATHE boundary for Spinoza himself is a scholarly dispute, not just a coding issue."
sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "William Mander"
    year: 2023
    citation: "Mander, William. \"Pantheism.\" Stanford Encyclopedia of Philosophy. First published October 1, 2012; substantive revision August 17, 2023. https://plato.stanford.edu/entries/pantheism/."
    url: "https://plato.stanford.edu/entries/pantheism/"
    accessed: 2026-10-01
    reliability_note: "Peer-reviewed reference entry by a specialist in the philosophy of religion."
    used_for: [classification, origins, metaphysics, epistemology, ethics, practice, science, schools_and_variants]
  - id: S2
    type: tertiary
    kind: encyclopedia
    author: "Steven Nadler"
    year: 2023
    citation: "Nadler, Steven. \"Baruch Spinoza.\" Stanford Encyclopedia of Philosophy. First published June 29, 2001; substantive revision November 8, 2023. https://plato.stanford.edu/entries/spinoza/."
    url: "https://plato.stanford.edu/entries/spinoza/"
    accessed: 2026-10-01
    reliability_note: "Peer-reviewed reference entry by a leading Spinoza scholar. Quotations of Spinoza in this file are taken from it (secondary quotation)."
    used_for: [origins, metaphysics, lio_axes, epistemology, science, schools_and_variants]
---

# Pantheism (Spinozistic/naturalistic 'God = Universe') (PANT)

> Status: example — unreviewed. This file shows the system-record structure. Sourced fields are filled from two Stanford Encyclopedia of Philosophy entries. The LIO axes use the 0–4 scale (P1). The revised rubric, adherents and community form are TODO. The display label is the full V6 label, approved 2026-10-01.

## Summary

Pantheism identifies God with the cosmos, or denies that God is distinct from it [S1, introduction]. SEP treats it as a family of doctrines, not one position [S1, introduction]. The study's code PANT is narrower. It means the Spinozistic circle, Deus sive Natura: one substance that is both God and Nature, acting from necessity with no purposes, miracles or exemptions [S2, §2.1]. The v7.1 coding rule says to use PANT "only for the circle" and not for "atheism-plus-poetry" or "every nature-mystic".

## Core metaphysics

For Spinoza, God is "the universal, immanent and sustaining cause of all that exists", not a transcendent creator [S2, §2.1]. God does not act for ends. Talk of divine purposes is "an anthropomorphizing fiction" [S2, §2.1]. Miracles are impossible: "Nothing happens in nature that does not follow from her laws" (TTP ch. 6, quoted in [S2, §3.1]). Most pantheists deny that the universe can be petitioned [S1, §17]. Whether God is personal [S1, §12] and whether anything of the mind is eternal [S1, §17; S2, §1] are disputed.

## Position on the LIO axes

Scored on the 0–4 scale (decision P1). All five axes are at the LIO pole (4) for the Spinozistic form: identity of God and Nature (A), no miracles or petition (B), no judging God (C, certainty 0.7), reason over prophecy (D), and the same laws for everything, human emotions included (E) [S2, §2.1, §2.4, §3.1]. The variants below would score differently. They are TODO.

## Schools and variants

Spinozistic substance monism (the study's core form); Stoic physicalist pantheism; modern scientific or naturalistic pantheism; Absolute Idealist pantheism; and pantheist strands inside religious traditions such as Advaita Vedanta, some Kabbalah and Sufism [S1, §1, §4, §6]. These are listed in `schools_and_variants` with how each moves on the axes.

## Science

Spinoza explains everything, miracles and prophecy included, through natural causes and laws [S2, §2.1, §3.1]. Modern scientific pantheism commits to nothing beyond empirical science [S1, §6]. The Ethics is written "in geometrical order" [S1, Bibliography], which matters for Lane B's geometric-method claim.

## Coding guidance

Use PANT only when a person's adult working worldview identifies God and Nature in the Spinozistic sense, not merely reverent naturalism. The two-part test (decision S6) makes this checkable: the person's own writing must (1) identify God or the divine with Nature as a whole, as a claim about what exists, and (2) give the whole a mark beyond feeling, such as unity, necessity, something mind-like or value [S1, §5, §10, §12, §13]. Code reverent naturalism that fails the test ATHE (or SECHUM), explicit suspension AGNOS, and "God beyond the world too" PANENT. Advaita Vedanta and Kabbalah default to the host tradition (HINDU, JUDA). Ancient and avowed Stoics are STOIC. Never code from heritage. See `docs/CODING_GUIDE.md` §5.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> PANT (49/50) — Pantheism as the circle: entity applied to Nature and Nature rendered in entity. Not God deleted. Petition splits mapping from mapped. Scores near-perfect for a no-exemption cosmos.

## Open questions

- Whether Spinoza himself is better read as a pantheist or an atheist is a scholarly dispute [S2, §2.1]. The study codes his system as PANT.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-01: filled from SEP "Pantheism" (Mander, rev. 2023) and SEP "Baruch Spinoza" (Nadler, rev. 2023). Did not consult primary texts directly. Spinoza quotations are as given in S2. Adherent numbers and organised community are left TODO.
- 2026-10-01: display label set to the full original label found in V6 (`V6_(history)/V6/beliefCoherence.json`, PANT entry, `belief_system`, in the v7 repo). Approved by Jason 2026-10-01 (OPEN_DECISIONS S2). `v7_1_label` unchanged.
- 2026-10-01: decisions P1 and S6 applied. Rechecked the five LIO scores on the approved 0–4 scale (all 4, each rationale names the LIO pole, so they stand). Added the two-part PANT test and the Advaita/Kabbalah and Stoic rules to the coding guidance.
