---
record:
  record_type: system
  schema_version: "1.1"
  record_version: 5
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (overnight systems run for Jason)"
  model_used: "Grok Bot executor agent; direct reads of the cited encyclopedia entries"
  collected_on: 2026-10-01
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-01, by: scripts/make_system_stubs.py, summary: "Stub created from v7.1 data book table 4 and section 7."}
    - {date: 2026-10-01, by: scripts/make_system_stubs.py, summary: "Coding guidance and PANT neighbor from the PANT boundary rules (OPEN_DECISIONS S6)."}
    - {date: 2026-10-01, by: "Grok Bot", summary: "Draft: classification, origins, metaphysics, LIO axes (0–4, P1), science, schools and coding guidance filled from five SEP entries, IEP and the Britannica article. S6 guidance and PANT neighbor kept. v7.1 scores and note unchanged. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit fix: E_scope 4 -> 3 at 0.7. The world is made for gods and humans and animals are outside the moral community (SEP Pantheism §15; SEP Stoicism §5.2), the same feature that holds CLASS_THEISM at 3. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit, run 2: E_scope how_known names the domain scored and points to open item P7 (which domain E is scored on). Score and certainty unchanged. Not reviewed."}
identity:
  id: STOIC
  v7_1_number: 21
  v7_1_label: "Stoicism"
  display_label: "Stoicism"
  label_status: "as in v7.1"
  aliases: ["the Stoa", "Stoic philosophy", "Neo-Stoicism (early modern revival)", "Modern Stoicism"]
classification:
  kind: {value: "philosophical school or method", certainty: 1.0, cites: [{source: S1, locator: "introduction; §1.1"}], how_known: "SEP: one of the dominant philosophical systems of the Hellenistic period, a school founded in Athens."}
  family: {value: "Hellenistic philosophy; materialist and providential pantheism", certainty: 0.7, cites: [{source: S1, locator: "introduction; §2.7"}, {source: S4, locator: "§6; §12"}], how_known: "SEP Stoicism for the period; SEP Pantheism calls Stoic physicalism an ancient form of pantheism, while also reporting the argument that the Stoic God was personal. The combined label is the coder's, 0.7."}
  parent_traditions: {value: ["Socratic philosophy", "Cynicism (Zeno studied under Crates)", "Plato's Academy and the Megarian School"], certainty: 1.0, cites: [{source: S1, locator: "§1.1"}], how_known: "SEP: Zeno was a reader of Socratic dialogues, studied under the Cynic Crates and was influenced by Plato's Academy and the Megarian School."}
  related_codes:
    - {code: PANT, relation: "neighbor (easily confused)", note: "SEP: Stoic physicalism is an ancient form of pantheism; the providential Stoic God is not the PANT circle (S6)"}
    - {code: CYNIC, relation: "parent tradition", note: "Zeno studied under the Cynic Crates (SEP)"}
    - {code: EPICUR, relation: "contrast case", note: "rival Hellenistic school; Marcus Aurelius's providence or atoms"}
    - {code: PLATO, relation: overlaps, note: "Middle Stoics engaged with Platonic doctrine (SEP)"}
    - {code: CHRIST, relation: overlaps, note: "Christian writers assimilated Stoic morality; Lipsius's Christian Neo-Stoicism (Britannica, SEP)"}
origins:
  founding_era: {value: "around 300 BCE", certainty: 1.0, cites: [{source: S1, locator: "§1.1"}], how_known: "SEP states it."}
  founding_region: {value: "Athens (the Painted Porch, stoa poikilê, in the Agora); later Rome", certainty: 1.0, cites: [{source: S1, locator: "introduction; §1.1"}], how_known: "SEP."}
  founders_or_key_figures: {value: ["Zeno of Citium (founder)", "Cleanthes of Assos", "Chrysippus of Soli (head c. 230–206 BCE, chief systematizer)", "Diogenes of Babylon, Antipater of Tarsus", "Panaetius, Posidonius (Middle Stoicism)", "Seneca", "Epictetus", "Marcus Aurelius", "Hierocles", "Justus Lipsius (Neo-Stoicism, late 16th century)"], certainty: 1.0, cites: [{source: S1, locator: "§1.1; §5.3"}], how_known: "SEP."}
  key_texts:
    - {value: "Discourses and Encheiridion (Manual)", author: "Epictetus, as recorded by Arrian", year: "early 2nd century CE", certainty: 0.7, cites: [{source: S6, locator: "§1"}, {source: S3, locator: "page 'Later Roman Stoicism'"}], how_known: "SEP and Britannica name them; the date is the coder's from Epictetus's dates in SEP Stoicism (expelled from Rome in 93 CE), so 0.7."}
    - {value: "Meditations", author: "Marcus Aurelius", year: "2nd century CE (emperor 161–180)", certainty: 1.0, cites: [{source: S1, locator: "§1.1"}, {source: S7, locator: "§4.1"}], how_known: "SEP."}
    - {value: "Moral Letters to Lucilius; Natural Questions", author: "Seneca", year: "1st century CE", certainty: 1.0, cites: [{source: S5, locator: "§1"}, {source: S2, locator: "1.c"}], how_known: "SEP Seneca and IEP."}
    - {value: "The Elements of Ethics (partially extant)", author: "Hierocles", year: "2nd century CE", certainty: 1.0, cites: [{source: S1, locator: "§1.1"}], how_known: "SEP. The works of the early Stoics survive only in fragments; the complete surviving works are Imperial (SEP §1.3)."}
metaphysics:
  god_nature_relation: {value: "God is corporeal and identical with the active principle, which acts on passive matter and is blended with it through and through; God is immanent throughout the cosmos, which is a living thing.", stance: identity, certainty: 0.7, cites: [{source: S1, locator: "§2.3; §2.7"}, {source: S4, locator: "§6"}], how_known: "SEP states it directly. Stance 0.7 because God is the active principle, not passive matter, so identity holds for the cosmos as a whole rather than every part."}
  deity_personal: {value: "Disputed. God is eternal reason (logos) and intelligent designing fire, orderly and providential; Baltzly has argued the Stoics believed in a personal deity, a conscious rational being exercising providence and approached in prayer.", stance: "both / disputed", certainty: 1.0, cites: [{source: S1, locator: "§2.7"}, {source: S4, locator: "§12"}], how_known: "SEP Pantheism reports the dispute directly."}
  intervention: {value: "No intervention from outside: God directs the cosmos 'down to the smallest detail' through the causal order itself, and divine actions are not random and unpredictable but 'orderly, rational, and providential'.", stance: none, certainty: 0.7, cites: [{source: S1, locator: "§2.7"}], how_known: "SEP. Mapping immanent providence to the stance none is the coder's, 0.7."}
  miracles: {value: "No miracles as exceptions to nature in the sources read. Divination was accepted, but 'as a branch of physics, not a superstition': predicting the future by exploiting the laws of physics, not going outside them.", stance: "reinterpreted as natural", certainty: 0.5, cites: [{source: S2, locator: "2.b"}], how_known: "IEP on divination. The sources read do not discuss miracles directly, so 0.5."}
  petition_and_prayer: {value: "Mixed. Seneca argued that praying would be insane without a caring God and that, though prayer cannot change fate, it can be effective because the gods left some things unresolved. Epictetus mocked praying for what one can do oneself. SEP Pantheism reports the view that the Stoic God was approached in prayer.", stance: "varies by school", certainty: 0.7, cites: [{source: S5, locator: "§5.3"}, {source: S6, locator: "§5"}, {source: S4, locator: "§12"}], how_known: "SEP entries; 0.7 because three authors are not a full survey."}
  afterlife: {value: "The sources read say little. The soul is a body (pneuma) that is separated from the body at death (Chrysippus); Seneca took seriously both a better afterlife and a genuine end; the cosmos goes through endless cycles of conflagration and recurrence.", stance: "varies by school", certainty: 0.5, cites: [{source: S1, locator: "§2.5; §2.9"}, {source: S5, locator: "§3.3"}], how_known: "Partial evidence only, so 0.5. A source on the orthodox Stoic view of survival was not read."}
  moral_ledger: {value: "Virtue is the only good and is necessary and sufficient for happiness, which is fully in our power; no divine reward or punishment appears in the sources read.", stance: "impersonal consequence", certainty: 0.5, cites: [{source: S1, locator: "§3.7; §4.3"}], how_known: "SEP on Stoic ethics. The stance is the coder's reading, and afterlife sources are thin, so 0.5."}
  authority: {value: "Reason and perception: knowledge rests on cognitive impressions, which have 'a peculiar power of revealing their objects'; physics grounds ethics; no revealed text.", stance: "observation and reason", certainty: 1.0, cites: [{source: S1, locator: "§3.7"}, {source: S3, locator: "page 'Ancient Stoicism'"}], how_known: "SEP and Britannica (perception as the basis of certain knowledge)."}
  reserved_exemptions: {value: "None: every event is the result of a cause or chain of causes; fate is an inviolable ordering.", stance: none, certainty: 1.0, cites: [{source: S1, locator: "§2.8"}], how_known: "SEP states it directly."}
  teleology_in_nature: {value: "God is intelligent designing fire that structures matter according to its plan, like a seed containing the directions of all that will develop; the cosmos is providentially ordered.", stance: "immanent ends", certainty: 1.0, cites: [{source: S1, locator: "§2.7"}], how_known: "SEP. The designer is inside nature, so immanent ends rather than an external designer's purposes."}
  necessity_and_freedom: {value: "Causal determinism with compatibilism: fate is the working out of the rational will of Zeus and everything is determined by preceding causes (though not logically necessary); Chrysippus's cylinder and cone keep assent 'in our power'.", certainty: 1.0, cites: [{source: S1, locator: "§2.8"}], how_known: "SEP."}
lio_axes:
  A_locus: {value: 3, rationale: "God is immanent in and identical with the active principle of the cosmos, an ancient form of pantheism; held back from 4 by the providential, possibly personal God whom Stoics prayed to.", certainty: 0.5, cites: [{source: S1, locator: "§2.7"}, {source: S4, locator: "§6; §12"}], how_known: "Scored on the 0–4 scale (P1). 0.5 because scholars disagree on whether the Stoic God is personal."}
  B_cause: {value: 4, rationale: "Strict causal determinism: every event follows from a chain of causes and fate is inviolable; even divination works within the laws of physics.", certainty: 0.7, cites: [{source: S1, locator: "§2.8"}, {source: S2, locator: "2.b"}], how_known: "0–4 scale (P1). Not 1.0 because the inviolable order is also called providence and the will of Zeus."}
  C_ledger: {value: 3, rationale: "Virtue is its own good and sufficient for happiness; no judge rewards or punishes in the sources read. Not 4 because the afterlife evidence is thin and Seneca allowed a better afterlife.", certainty: 0.5, cites: [{source: S1, locator: "§4.3"}, {source: S5, locator: "§3.3"}], how_known: "0–4 scale (P1). 0.5 for the thin afterlife evidence."}
  D_authority: {value: 3, rationale: "Knowledge from cognitive impressions and reason; no revelation. Not 4 because natural study was subordinate to living well and divination was accepted as a science.", certainty: 0.7, cites: [{source: S1, locator: "§3.7"}, {source: S2, locator: "2.b"}], how_known: "0–4 scale (P1). Coder's reading, 0.7."}
  E_scope: {value: 3, rationale: "Leans LIO: one causal order for everything, with no exemptions, and all human beings together with Zeus are citizens of one universal city (cosmopolis) (S1, §2.8; §4.5). The limited exception is a ranking of beings: Cicero's 'all things were made for either Gods or men' (S4, §15), and animals stand outside the moral community (Augustine followed the Stoics rather than the Platonists 'on the question of animals’ membership in the moral community', S1, §5.2). The same feature (the rest of creation ordered for the sake of rational beings) holds CLASS_THEISM at 3. 4 is the named alternative if only the causal order is counted.", certainty: 0.7, cites: [{source: S1, locator: "§2.8; §4.5; §5.2"}, {source: S4, locator: "§15"}], how_known: "0–4 scale (P1). Changed from 4 after the lens audit (2026-10-02) for consistency with CLASS_THEISM. Coder's reading with a named alternative, so 0.7 (CODING_GUIDE §3). The domain is open (OPEN_DECISIONS P7, PROPOSED): on the world's order alone the moral-community limit drops out and the named alternative 4 applies."}
epistemology: {value: "Empiricist foundation: cognitive (kataleptic) impressions, assent and cognition; logic as an instrument; physics, logic and ethics form one interlocking system.", certainty: 1.0, cites: [{source: S1, locator: "introduction; §1.2; §3.7"}, {source: S3, locator: "page 'Ancient Stoicism'"}], how_known: "SEP and Britannica."}
ethics: {value: "The end is 'living in agreement with nature' (Cleanthes); virtue is the only good and sufficient for happiness; externals are indifferents; passions are to be removed (apatheia); cosmopolitanism.", certainty: 1.0, cites: [{source: S1, locator: "§4.1; §4.3; §4.5; §4.7"}, {source: S2, locator: "3; 4"}], how_known: "SEP and IEP."}
practice:
  ritual_and_practice: {value: "Philosophy as a way of life: the system was meant primarily as guidance for everyday life (IEP), with therapy of the emotions in Seneca; the modern movement traces roots to logotherapy and cognitive behavioral therapy.", certainty: 0.7, cites: [{source: S2, locator: "6"}, {source: S5, locator: "§3.3"}], how_known: "IEP and SEP; the summary is the coder's, 0.7."}
  community_form: {value: "A school with a line of heads (scholarchs) in Athens; later individual teachers and their students; today a Modern Stoicism movement and a steady flow of scholarship and translations.", certainty: 0.7, cites: [{source: S1, locator: "§1.1"}, {source: S2, locator: "6"}], how_known: "SEP and IEP; 0.7 for the modern part."}
science:
  historical_stance: {value: "Stoic physics is a full natural philosophy (bodies and incorporeals, pneuma, mixture, the elements, cosmic cycles), and Stoic logic was a major achievement. But for the Stoics the study of nature is 'not an end in itself, but rather subordinate to help us live a eudaimonic life' (IEP), and they treated divination as part of physics.", certainty: 1.0, cites: [{source: S1, locator: "§2; §3"}, {source: S2, locator: "2.b; 6"}], how_known: "SEP and IEP."}
  current_stance: {value: "Modern Stoicism (Irvine, Sellars, Becker) presents Stoicism again as practical philosophy. IEP notes that modern recurring-universe models do away with providence. The sources read do not say how much of the physics modern Stoics keep.", certainty: 0.7, cites: [{source: S2, locator: "2.b; 6"}], how_known: "IEP; the summary is the coder's, 0.7."}
schools_and_variants:
  - {name: "Old Stoa (Zeno, Cleanthes, Chrysippus)", form: "scholastic or philosophical", how_it_differs: "The full system: physics, logic and ethics; conflagration and recurrence.", lio_difference: "As scored.", certainty: 1.0, cites: [{source: S1, locator: "§1.1; §2.5"}]}
  - {name: "Middle Stoicism (Panaetius, Posidonius)", form: "scholastic or philosophical", how_it_differs: "More engagement with Plato and Aristotle; Panaetius rejected the conflagration.", lio_difference: "Little change on the axes.", certainty: 0.7, cites: [{source: S1, locator: "§1.1; §2.5"}]}
  - {name: "Roman Imperial Stoicism (Seneca, Epictetus, Marcus Aurelius)", form: "scholastic or philosophical", how_it_differs: "Practical ethics and consolation; more prayer and piety language; Marcus keeps the providence or atoms alternative open.", lio_difference: "A may sit lower (more personal God); C less certain (Seneca on afterlife).", certainty: 0.7, cites: [{source: S1, locator: "§1.1"}, {source: S5, locator: "§3.3; §5.3"}, {source: S7, locator: "§4.1"}]}
  - {name: "Christian Neo-Stoicism (Lipsius) and Renaissance Stoic pantheism (Patrizi, Bruno)", form: reform, how_it_differs: "Lipsius synthesised Stoicism with Christianity; Patrizi and Bruno drew a pantheistic naturalism from Stoic sources; Britannica calls the debatably pantheist side of Spinoza essentially Stoic.", lio_difference: "Lipsius: toward CHRIST. Bruno and Spinoza: test against PANT (S6).", certainty: 1.0, cites: [{source: S1, locator: "§5.3"}, {source: S3, locator: "page 'Revival of Stoicism in modern times'"}]}
  - {name: "Modern Stoicism (Irvine, Sellars, Becker; CBT links)", form: modern, how_it_differs: "Practical philosophy for everyday life; the sources read do not say how much of the Stoic God modern Stoics keep.", lio_difference: "A toward 4 or out of the theist frame; check ATHE or SECHUM for the person's working worldview.", certainty: 0.7, cites: [{source: S2, locator: "6"}]}
adherents:
  use: "context only — never a genius-rate denominator"
  estimate: {value: TODO, note: "Ancient school; no census category. Modern Stoicism has no membership count in the sources read."}
v7_1_rubric:
  label: "authorial v7.1 scores"
  L: 9
  P: 9
  E: 10
  V: 10
  X: 8
  total: 46
  scoring_note: "Stoicism provides practical wisdom with strong rational and empirical ties, ideal for personal coherence."
  source: "v7.1 data book, section 6 table (tables[4]) row 21 and section 7 scoring notes"
revised_rubric:
  status: "not started"
  L: {score: TODO, rationale: ""}
  P: {score: TODO, rationale: ""}
  E: {score: TODO, rationale: ""}
  V: {score: TODO, rationale: ""}
  X: {score: TODO, rationale: ""}
coding_guidance:
  use_when: "v8 rule (decision S6, 2026-10-01): ancient Stoics, and anyone whose avowed school is Stoicism (founders rule; 'Primary = dominant working metaphysics'). SEP 'Pantheism' (Mander, rev. 2023) treats Stoic physicalism as an ancient form of pantheism, but the Stoic God is argued to be personal and providential, one 'to whom we might approach in prayer', which is not the PANT circle."
  do_not_use_when: "A later thinker who takes the Stoic or Spinozist identity of God and Nature without the providential, prayer-hearing deity, and who passes the two-part PANT test: PANT. A Christian Neo-Stoic whose working metaphysics is Christian (Lipsius): CHRIST. A modern practitioner who keeps Stoic ethics but not the Stoic God: code the working worldview (ATHE, SECHUM or AGNOS), not STOIC, unless they avow the school."
  neighbors:
    - {code: PANT, relation: "neighbor (easily confused)"}
    - {code: EPICUR, relation: "contrast case"}
    - {code: CHRIST, relation: overlaps}
review:
  data_quality_flags:
    - "The v7.1 note claims 'strong rational and empirical ties'. The sources support the rational side and an empiricist theory of knowledge (cognitive impressions), but IEP says Stoic natural study was subordinate to living well and that the Stoics accepted divination as a branch of physics (S2, 2.b; 6). That is a weaker empirical tie than the note suggests. v7.1 text left unchanged."
    - "PANT lists STOIC as a parent tradition, while this file and the S6 rule list PANT as a neighbor. Both are true in different directions (Stoic sources of later pantheism; boundary for coding). Not changed."
  open_questions:
    - "Afterlife: the orthodox Stoic view of how long souls survive was not found in the sources read. Needs a source before C_ledger certainty can rise."
    - "Adherents are TODO."
sources:
  - {id: S1, type: tertiary, kind: encyclopedia, author: "Marion Durand; Simon Shogry; Dirk Baltzly", year: 2023, citation: "Durand, Marion, Simon Shogry, and Dirk Baltzly. \"Stoicism.\" Stanford Encyclopedia of Philosophy. First published January 20, 2023. https://plato.stanford.edu/entries/stoicism/.", url: "https://plato.stanford.edu/entries/stoicism/", accessed: 2026-10-01, reliability_note: "Peer-reviewed reference entry. Baltzly is also the author of the personal-deity argument reported in S4.", used_for: [classification, origins, metaphysics, lio_axes, epistemology, ethics, science, schools_and_variants]}
  - {id: S2, type: tertiary, kind: encyclopedia, author: "Massimo Pigliucci", citation: "Pigliucci, Massimo. \"Stoicism.\" Internet Encyclopedia of Philosophy. https://iep.utm.edu/stoicism/.", url: "https://iep.utm.edu/stoicism/", accessed: 2026-10-01, reliability_note: "Peer-reviewed reference entry. The author is an advocate of modern Stoicism; used for divination, science and the modern movement. Locators are the IEP's numbered sections.", used_for: [metaphysics, lio_axes, ethics, practice, science, schools_and_variants]}
  - {id: S3, type: tertiary, kind: encyclopedia, author: "Jason Lewis Saunders", citation: "Saunders, Jason Lewis. \"Stoicism.\" Encyclopaedia Britannica. Online article, pages 'Ancient Stoicism', 'Later Roman Stoicism' and 'Revival of Stoicism in modern times'. https://www.britannica.com/topic/Stoicism.", url: "https://www.britannica.com/topic/Stoicism", accessed: 2026-10-01, reliability_note: "Signed reference article. Article paragraphs only; the AI-generated question boxes on Britannica pages were ignored.", used_for: [origins, metaphysics, epistemology, schools_and_variants]}
  - {id: S4, type: tertiary, kind: encyclopedia, author: "William Mander", year: 2023, citation: "Mander, William. \"Pantheism.\" Stanford Encyclopedia of Philosophy. First published October 1, 2012; substantive revision August 17, 2023. https://plato.stanford.edu/entries/pantheism/.", url: "https://plato.stanford.edu/entries/pantheism/", accessed: 2026-10-01, reliability_note: "Peer-reviewed reference entry.", used_for: [classification, metaphysics, lio_axes, coding_guidance]}
  - {id: S5, type: tertiary, kind: encyclopedia, author: "Katja Vogt", year: 2024, citation: "Vogt, Katja. \"Seneca.\" Stanford Encyclopedia of Philosophy. First published October 17, 2007; substantive revision February 13, 2024. https://plato.stanford.edu/entries/seneca/.", url: "https://plato.stanford.edu/entries/seneca/", accessed: 2026-10-01, reliability_note: "Peer-reviewed reference entry.", used_for: [origins, metaphysics, lio_axes, practice, schools_and_variants]}
  - {id: S6, type: tertiary, kind: encyclopedia, author: "Margaret Graver", year: 2025, citation: "Graver, Margaret. \"Epictetus.\" Stanford Encyclopedia of Philosophy. First published December 23, 2008; substantive revision July 16, 2025. https://plato.stanford.edu/entries/epictetus/.", url: "https://plato.stanford.edu/entries/epictetus/", accessed: 2026-10-01, reliability_note: "Peer-reviewed reference entry.", used_for: [origins, metaphysics]}
  - {id: S7, type: tertiary, kind: encyclopedia, author: "Rachana Kamtekar", year: 2025, citation: "Kamtekar, Rachana. \"Marcus Aurelius.\" Stanford Encyclopedia of Philosophy. First published November 29, 2010; substantive revision March 31, 2025. https://plato.stanford.edu/entries/marcus-aurelius/.", url: "https://plato.stanford.edu/entries/marcus-aurelius/", accessed: 2026-10-01, reliability_note: "Peer-reviewed reference entry.", used_for: [origins, schools_and_variants]}
---

# Stoicism (STOIC)

> Status: draft — unreviewed. Filled from Stanford Encyclopedia of Philosophy entries, IEP and the signed Britannica article. LIO axes use the 0–4 scale (P1). The S6 coding rule and the v7.1 scores and note are unchanged. Adherents are TODO.

## Summary

Stoicism is a Hellenistic school founded in Athens around 300 BCE by Zeno of Citium. Chrysippus was its main systematizer, and in the Roman period Seneca, Epictetus and Marcus Aurelius made it popular [S1, §1.1]. Its philosophy has three parts, physics, logic and ethics, which are meant to fit together [S1, introduction]. The divine is the rational active principle inside the cosmos. SEP Pantheism calls this "an ancient form of pantheism" and also reports the argument that the Stoic God was personal [S4, §6; §12]. Under decision S6, ancient and avowed Stoics are coded STOIC, not PANT.

## Core metaphysics

The Stoics make God "a corporeal entity, identical with the active principle", which acts on passive matter [S1, §2.7; §2.3]. God is immanent throughout the cosmos and "directs its development down to the smallest detail", and divine action is "orderly, rational, and providential" [S1, §2.7]. They are "determinists about causation" and defend compatibilism [S1, §2.8]. Fate is "a certain natural everlasting ordering of the whole" [S1, §2.8]. The cosmos passes through "a cycle of endless recurrence" with conflagrations [S1, §2.5]. Divination was accepted "as a branch of physics, not a superstition" [S2, 2.b]. On prayer, Seneca held that "Prayer cannot change fate" but can still be effective [S5, §5.3].

## Position on the LIO axes

Scored on the 0–4 scale (P1):

- A locus 3 (0.5): God is the immanent active principle; the personal reading pulls it down [S1, §2.7; S4, §12].
- B cause 4 (0.7): strict causal determinism [S1, §2.8].
- C ledger 3 (0.5): virtue is the only good; thin evidence on the afterlife [S1, §4.3; S5, §3.3].
- D authority 3 (0.7): cognitive impressions and reason; divination counted as science [S1, §3.7; S2, 2.b].
- E scope 3 (0.7): one causal order and one cosmopolis for all, but the world is made for gods and humans and animals are outside the moral community [S1, §2.8; §4.5; §5.2; S4, §15].

## Schools and variants

The Old Stoa built the full system. Middle Stoics engaged more with Plato, and Panaetius rejected the conflagration [S1, §1.1; §2.5]. The Roman Stoics focused on practical ethics; Marcus repeatedly sets out the alternatives "providence or atoms" [S7, §4.1]. In the late 16th century Lipsius led a Christian Neo-Stoicism [S1, §5.3]. Britannica says the pantheistic naturalism of Patrizi and Bruno was Stoic at its source, and that the debatably pantheist side of Spinoza "is essentially Stoic in character" [S3, Revival of Stoicism in modern times]. Modern Stoicism presents the school again as practical philosophy [S2, 6].

## Science

Stoic physics is a full natural philosophy and Stoic logic a major achievement [S1, §2; §3]. IEP adds that for the Stoics the study of nature was "not an end in itself, but rather subordinate to help us live a eudaimonic life" [S2, 6]. The universal causality that underwrites their determinism also led them to treat divination as physics [S2, 2.b].

## Coding guidance

Code STOIC for ancient Stoics and for anyone whose avowed school is Stoicism (decision S6). A later thinker who takes the Stoic or Spinozist identity of God and Nature without the providential, prayer-hearing God, and passes the two-part test, is PANT. A Christian Neo-Stoic is coded by the working metaphysics, usually CHRIST. A modern practitioner who uses Stoic ethics without the Stoic God is coded by their working worldview unless they avow the school.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> STOIC (46/50) — Stoicism. Stoicism provides practical wisdom with strong rational and empirical ties, ideal for personal coherence.

## Open questions

- The empirical side of the v7.1 note is weaker in the sources than the note suggests (see review).
- The orthodox Stoic view of the soul's survival needs a source.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`; S6 coding rule and PANT neighbor added.
- 2026-10-01 (overnight run): read SEP "Stoicism", "Pantheism", "Seneca", "Epictetus" and "Marcus Aurelius"; IEP "Stoicism" (Pigliucci); Britannica "Stoicism" (J. L. Saunders; five pages). AI-generated question boxes on Britannica pages were not used. All quotations were checked word for word against the fetched page text with a script.
