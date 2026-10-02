---
record:
  record_type: system
  schema_version: "1.1"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (overnight systems run for Jason)"
  model_used: "Grok Bot executor agent; direct reads of the cited encyclopedia entries"
  collected_on: 2026-10-01
  last_updated: 2026-10-01
  change_log:
    - {date: 2026-10-01, by: scripts/make_system_stubs.py, summary: "Stub created from v7.1 data book table 4 and section 7."}
    - {date: 2026-10-01, by: "Grok Bot", summary: "Draft: classification, origins, metaphysics, LIO axes (0–4, P1), science, schools and coding guidance filled from seven SEP entries, IEP and the multi-author Britannica article. v7.1 scores and note unchanged. Not reviewed."}
identity:
  id: PLATO
  v7_1_number: 36
  v7_1_label: "Platonism"
  display_label: "Platonism"
  label_status: "as in v7.1"
  aliases: ["Platonic philosophy", "Middle Platonism", "Neoplatonism", "Christian Platonism"]
classification:
  kind: {value: "philosophical school or method", certainty: 0.7, cites: [{source: S1, locator: "introduction"}], how_known: "Britannica: 'any philosophy that derives its ultimate inspiration from Plato', read in many ways. A long tradition rather than one school, so 0.7."}
  family: {value: "Greek philosophy; metaphysics of transcendent forms and an intelligible reality", certainty: 1.0, cites: [{source: S1, locator: "introduction; page 'Evaluation of Platonism'"}, {source: S2, locator: "§1"}], how_known: "Britannica and SEP state the central doctrine directly."}
  parent_traditions: {value: ["Socrates", "Pythagoreanism (mathematical side of the forms)"], certainty: 0.7, cites: [{source: S2, locator: "§4; §11"}, {source: S1, locator: "'Greek Platonism from Aristotle through Middle Platonism'"}], how_known: "SEP on Socrates as Plato's main speaker; Britannica on Pythagorean influence. Calling them parents is the coder's framing, 0.7."}
  related_codes:
    - {code: ARIST, relation: offshoot, note: "Aristotle studied in Plato's Academy and rejected transcendent forms but kept much of Platonism (Britannica)"}
    - {code: PANENT, relation: "neighbor (easily confused)", note: "SEP God and Other Ultimates lists Plato among panentheistic models; Neoplatonic emanation is excluded from the Abrahamic doctrine of creation (SEP Religion and Science)"}
    - {code: STOIC, relation: overlaps, note: "Middle Platonism and Platonized Stoicism (Posidonius)"}
    - {code: CHRIST, relation: overlaps, note: "Augustinian and Christian Platonism; Cambridge Platonists"}
    - {code: IDEAL, relation: overlaps, note: "Neoplatonism influenced Hegel and Schelling; Britannica warns against equating them"}
origins:
  founding_era: {value: "4th century BCE (Plato, c. 427–347 BCE, and his Academy)", certainty: 1.0, cites: [{source: S3, locator: "title; §1.a"}], how_known: "IEP gives Plato's dates."}
  founding_region: {value: "Athens; later Alexandria, Rome, the Byzantine world, the Islamic world, Florence and England", certainty: 0.7, cites: [{source: S1, locator: "introduction; pages 'Neoplatonism: its nature and history', 'Renaissance and later Platonism'"}, {source: S3, locator: "§1.c"}], how_known: "Britannica and IEP; the list of later centres is the coder's selection, 0.7."}
  founders_or_key_figures: {value: ["Plato (founder)", "Speusippus and Xenocrates (Old Academy)", "Arcesilaus (Skeptical Academy)", "Philo of Alexandria (Middle Platonism and Jewish thought)", "Plotinus (3rd century CE, Neoplatonism)", "Porphyry, Iamblichus, Proclus (later Neoplatonists)", "Augustine and Pseudo-Dionysius (Christian Platonism)", "Marsilio Ficino (Florentine Academy)", "Henry More and Ralph Cudworth (Cambridge Platonists)"], certainty: 1.0, cites: [{source: S1, locator: "introduction; pages 'Neoplatonism: its nature and history', 'The later Neoplatonists', 'Augustinian Platonism', 'Renaissance and later Platonism'"}, {source: S6, locator: "introduction"}], how_known: "All named in these roles in Britannica or SEP. A selection, not a ranking."}
  key_texts:
    - {value: "Dialogues, especially Phaedo, Republic, Phaedrus, Timaeus and Laws", author: "Plato", year: "4th century BCE", certainty: 1.0, cites: [{source: S2, locator: "§1; §11"}, {source: S3, locator: "§6"}, {source: S4, locator: "§1"}], how_known: "SEP and IEP. Platonism was based primarily on a reading of the dialogues (Britannica)."}
    - {value: "Enneads", author: "Plotinus", year: "3rd century CE", certainty: 1.0, cites: [{source: S1, locator: "pages 'Plotinus and his philosophy', 'Renaissance and later Platonism'"}, {source: S5, locator: "introduction"}], how_known: "Britannica and SEP."}
metaphysics:
  god_nature_relation: {value: "In the Timaeus the cosmos is the handiwork of a 'supremely good, ungrudging Craftsman' who ordered a disorderly state of affairs, and the cosmos is itself a living thing with a soul. In Neoplatonism each level of being derives from the one above it, not by a process in time. SEP lists Plato among panentheistic models.", stance: "God in Nature and beyond it", certainty: 0.5, cites: [{source: S4, locator: "§1"}, {source: S1, locator: "page 'Neoplatonism: its nature and history'"}, {source: S7, locator: "§2.2"}], how_known: "Sources state the parts; the stance is the coder's reading and could also be read as creator distinct from creation for the Timaeus, so 0.5."}
  deity_personal: {value: "Disputed: the Craftsman 'seems to be an anthropomorphic representation of Intellect', and scholars disagree about what Intellect is (a form, the form of the Good, or something else). The Neoplatonic One is the first principle beyond all multiplicity. In the early dialogues the gods are completely wise and good.", stance: "both / disputed", certainty: 1.0, cites: [{source: S4, locator: "§7"}, {source: S5, locator: "introduction"}, {source: S3, locator: "§5.e"}], how_known: "SEP and IEP state the dispute directly."}
  intervention: {value: "The Craftsman orders the cosmos, but whether the creation story is literal or metaphorical has divided Platonists since the Old Academy; the metaphorical reading prevailed. The Craftsman cannot change what Necessity fixes. Later Neoplatonists held that the gods give help through prayer and the rites of theurgy.", stance: "varies by school", certainty: 0.7, cites: [{source: S4, locator: "§1; §2"}, {source: S1, locator: "page 'The later Neoplatonists'"}], how_known: "SEP and Britannica; 0.7 for the summary."}
  miracles: {value: "Not a topic in the sources read for Plato. Theurgy in later Neoplatonism used rites to reach the divine but was not thought of merely as magic.", stance: "not addressed", certainty: 0.5, cites: [{source: S1, locator: "page 'The later Neoplatonists'"}], how_known: "Absence in the sources read, so 0.5."}
  petition_and_prayer: {value: "Varies. Socrates reports a divine sign that opposes him when he is about to do wrong; later Neoplatonists held that the gods gave all things 'the power of return in prayer' and practised theurgy; Plotinus' way is contemplative return to the One.", stance: "varies by school", certainty: 0.7, cites: [{source: S3, locator: "§5.e"}, {source: S1, locator: "pages 'The later Neoplatonists', 'Neoplatonism: its nature and history'"}], how_known: "IEP and Britannica."}
  afterlife: {value: "The soul is immortal and existed before birth, and souls are reincarnated into different life forms (Phaedo, Meno, Republic X, Phaedrus, Timaeus, Laws). The early dialogues are more tentative: 'there may be an afterlife' with reward for the good and punishment for the wicked.", stance: rebirth, certainty: 0.7, cites: [{source: S3, locator: "§5.e; §6.c"}, {source: S4, locator: "§1"}], how_known: "IEP; 0.7 because the early dialogues are agnostic and the myths are myths."}
  moral_ledger: {value: "In the myths the souls of the good are rewarded and the wicked punished, and later lives follow from earlier ones; justice is also presented as good in itself.", stance: "personal reward and punishment", certainty: 0.5, cites: [{source: S3, locator: "§5.e; §6.c"}], how_known: "IEP; how literally to take the myths is disputed, so 0.5."}
  authority: {value: "Reason, not the senses: the world 'that appears to our senses is in some way defective and filled with error', and the forms are grasped by thought; Socrates argues from recollection. Britannica adds that when Platonism has been strongly held it has rested on 'a faith depending on some sort of experience rather than simply on the conclusion of an argument'.", stance: "observation and reason", certainty: 0.7, cites: [{source: S2, locator: "§1"}, {source: S1, locator: "page 'Evaluation of Platonism'"}, {source: S3, locator: "§6.c"}], how_known: "SEP and Britannica. The enum joins observation and reason; Plato ranks reason far above observation, so 0.7."}
  reserved_exemptions: {value: "None in Plato's own system in the sources read; theurgy in later Neoplatonism is a partial exception.", stance: none, certainty: 0.5, cites: [{source: S1, locator: "page 'The later Neoplatonists'"}], how_known: "Coder's reading, 0.5."}
  teleology_in_nature: {value: "Strong: the Timaeus explains the universe teleologically as the work of a good Craftsman, the fulfilment of the search for teleological explanation in the Phaedo; rational, mathematical order may be the form of the Good.", stance: "designer's purposes", certainty: 1.0, cites: [{source: S4, locator: "§1; §7"}], how_known: "SEP Timaeus."}
  necessity_and_freedom: {value: "Two kinds of cause: Intellect and Necessity. The properties of physical structures are fixed by Necessity, and it is not open to the Craftsman to change them. Neoplatonic derivation from the One is not a process in time.", certainty: 1.0, cites: [{source: S4, locator: "§1"}, {source: S1, locator: "page 'Neoplatonism: its nature and history'"}], how_known: "SEP and Britannica."}
lio_axes:
  A_locus: {value: 2, rationale: "Mid-basin: an intelligible reality and a good Craftsman (or Intellect) apart from the sensible world, with a world-soul inside it; SEP lists Plato among panentheistic models; the Neoplatonic One is beyond personhood.", certainty: 0.5, cites: [{source: S4, locator: "§1; §7"}, {source: S7, locator: "§2.2"}, {source: S5, locator: "introduction"}], how_known: "Scored on the 0–4 scale (P1). 0.5: readings differ (literal Craftsman toward 1, Neoplatonic One toward 2–3)."}
  B_cause: {value: 3, rationale: "The cosmos is ordered by Intellect working with Necessity, which even the Craftsman cannot change; no miracles in Plato. Not 4: explanation is teleological, and later Neoplatonists used theurgy.", certainty: 0.7, cites: [{source: S4, locator: "§1; §7"}, {source: S1, locator: "page 'The later Neoplatonists'"}], how_known: "0–4 scale (P1). Coder's reading, 0.7."}
  C_ledger: {value: 2, rationale: "Myths of judgment and reincarnation give a moral ledger across lives, but it is presented in myth and the early dialogues are agnostic; no personal judge who can be swayed is required.", certainty: 0.5, cites: [{source: S3, locator: "§5.e; §6.c"}], how_known: "0–4 scale (P1). 0.5 for the interpretive dispute."}
  D_authority: {value: 2, rationale: "No revelation in Plato, and reason is the authority; but it is a priori reason that distrusts the senses, and strong Platonism rests on a kind of experience as much as argument. Later Neoplatonism and Christian Platonism added revealed or ritual sources.", certainty: 0.5, cites: [{source: S2, locator: "§1"}, {source: S1, locator: "page 'Evaluation of Platonism'"}], how_known: "0–4 scale (P1). 0.5 because how to place a priori reason on this axis is itself a judgement call."}
  E_scope: {value: 3, rationale: "The forms and the order of the cosmos hold universally, with no in-group exemptions in Plato; later theurgy and the gods' help are partial exceptions.", certainty: 0.7, cites: [{source: S2, locator: "§1"}, {source: S1, locator: "page 'The later Neoplatonists'"}], how_known: "0–4 scale (P1). Coder's reading, 0.7."}
epistemology: {value: "Knowledge is of forms, reached by reason and dialectic; recollection (learning as drawing on what the soul already knows); the senses give only defective images. Mathematical method is the model.", certainty: 1.0, cites: [{source: S2, locator: "§1"}, {source: S3, locator: "§6.c"}], how_known: "SEP and IEP."}
ethics: {value: "An intense concern for the quality of human life, 'always ethical, often religious, and sometimes political', grounded in unchanging forms that give value and meaning; the Good as the highest form.", certainty: 1.0, cites: [{source: S1, locator: "introduction"}, {source: S4, locator: "§7"}], how_known: "Britannica and SEP."}
practice:
  ritual_and_practice: {value: "Dialectic and contemplation; in later Neoplatonism, prayer and theurgic rites; in the Academies, teaching and commentary.", certainty: 0.7, cites: [{source: S1, locator: "pages 'Neoplatonism: its nature and history', 'The later Neoplatonists'"}], how_known: "Coder's summary of Britannica, 0.7."}
  community_form: {value: "The Academy and its successors; Neoplatonic schools until pagan teaching of philosophy ended in the 6th century CE; the Florentine Academy; the Cambridge Platonists; no modern organised body.", certainty: 0.7, cites: [{source: S1, locator: "pages 'Neoplatonism: its nature and history', 'Renaissance and later Platonism'"}], how_known: "Britannica; the absence of a modern body is the coder's statement, 0.7."}
science:
  historical_stance: {value: "The Timaeus gives a mathematical physics: the four kinds are made of geometrical bodies (fire of tetrahedra, air of octahedra, water of icosahedra). Plato's forms were, according to Aristotle, highly mathematical. Aristotle rejected the Timaeus cosmology because it required a beginning of time.", certainty: 1.0, cites: [{source: S4, locator: "§1; §2"}, {source: S1, locator: "'Greek Platonism from Aristotle through Middle Platonism'"}], how_known: "SEP and Britannica."}
  current_stance: {value: "No single stance. In current philosophy, platonism (lowercase) usually names the view that abstract objects exist; SEP calls this 'a contemporary view' and says it is not entirely clear that Plato held it.", certainty: 1.0, cites: [{source: S8, locator: "introduction"}], how_known: "SEP Platonism in Metaphysics."}
schools_and_variants:
  - {name: "Old Academy (Speusippus, Xenocrates)", form: "scholastic or philosophical", how_it_differs: "Mathematical metaphysics; Speusippus replaced forms with numbers.", lio_difference: "Little change.", certainty: 1.0, cites: [{source: S1, locator: "'Greek Platonism from Aristotle through Middle Platonism'"}]}
  - {name: "Skeptical Academy", form: "scholastic or philosophical", how_it_differs: "Britannica says the central doctrine of an independent intelligible reality does not apply to it.", lio_difference: "Code SCEPT if the person's own writing is in this line.", certainty: 0.7, cites: [{source: S1, locator: "page 'Evaluation of Platonism'"}]}
  - {name: "Middle Platonism (1st century CE; Philo)", form: "scholastic or philosophical", how_it_differs: "Linked with revived Pythagoreanism; philosophical background for Philo's biblical philosophy.", lio_difference: "A toward 1 in the Jewish and Christian uses.", certainty: 0.7, cites: [{source: S1, locator: "'Greek Platonism from Aristotle through Middle Platonism'"}]}
  - {name: "Neoplatonism (Plotinus, Porphyry, Iamblichus, Proclus)", form: mystical, how_it_differs: "Hierarchy of levels of being derived from the One, with outgoing and return; later theurgy.", lio_difference: "A 2–3 (emanation); B and E slightly lower where theurgy is used.", certainty: 1.0, cites: [{source: S1, locator: "pages 'Neoplatonism: its nature and history', 'The later Neoplatonists'"}, {source: S5, locator: "introduction"}]}
  - {name: "Christian, Jewish and Islamic Platonism (Augustine, Pseudo-Dionysius; Ficino; Cambridge Platonists)", form: "scholastic or philosophical", how_it_differs: "Platonism inside a revealed religion.", lio_difference: "A and D lower; usually code the host religion or CLASS_THEISM from the person's own writing.", certainty: 0.7, cites: [{source: S1, locator: "pages 'Augustinian Platonism', 'Platonism in the world of revealed religions', 'Renaissance and later Platonism'"}, {source: S6, locator: "introduction"}]}
  - {name: "Contemporary platonism about abstract objects", form: modern, how_it_differs: "A view in metaphysics and the philosophy of mathematics, not a worldview or school.", lio_difference: "Says nothing about A–C by itself.", certainty: 1.0, cites: [{source: S8, locator: "introduction"}]}
adherents:
  use: "context only — never a genius-rate denominator"
  estimate: {value: TODO, note: "A philosophical tradition with no membership; no demographic source applies."}
v7_1_rubric:
  label: "authorial v7.1 scores"
  L: 8
  P: 8
  E: 7
  V: 8
  X: 6
  total: 37
  scoring_note: "Platonism scores moderately high due to its influential theory of ideal forms, providing philosophical depth for reality and ethics, but limited by abstract nature and modest empirical alignment."
  source: "v7.1 data book, section 6 table (tables[4]) row 36 and section 7 scoring notes"
revised_rubric:
  status: "not started"
  L: {score: TODO, rationale: ""}
  P: {score: TODO, rationale: ""}
  E: {score: TODO, rationale: ""}
  V: {score: TODO, rationale: ""}
  X: {score: TODO, rationale: ""}
coding_guidance:
  use_when: "The person's own writing holds that a spiritual or intelligible reality independent of the world (forms, the Good, the One, Intellect) is the ultimate origin of both existence and values, and this is their working metaphysics (S1, Evaluation of Platonism). Avowed Platonists and Neoplatonists outside a revealed religion are the clear cases."
  do_not_use_when: "Mathematical platonism alone (abstract objects exist): it is a contemporary view in metaphysics (S8) and does not by itself settle the worldview. Record it in the person file and code from the rest of their writing. Platonism inside Christianity, Judaism or Islam: code the host religion or CLASS_THEISM unless the Platonism clearly dominates. Skeptical Academy: SCEPT. Aristotle's immanent forms: ARIST. A God both in and beyond the world without the forms: PANENT."
  neighbors:
    - {code: ARIST, relation: offshoot}
    - {code: PANENT, relation: "neighbor (easily confused)"}
    - {code: CHRIST, relation: overlaps}
    - {code: STOIC, relation: overlaps}
review:
  data_quality_flags:
    - "The v7.1 note credits Platonism's 'theory of ideal forms' and docks it for 'modest empirical alignment'. Consistent with the sources: SEP says the world that appears to our senses is in some way defective, and Britannica says strong Platonism has rested on a kind of faith from experience. But the Timaeus also offers a mathematical physics (S4), which the note does not mention. Not a contradiction; reported only. v7.1 text left unchanged."
    - "The v7.1 coding rule names CLASS_THEISM as Aristotelian-Thomistic-Falsafa; Christian and Islamic Platonists (Augustine, Pseudo-Dionysius, Avicenna's Neoplatonic elements) sit between PLATO, the host religion and CLASS_THEISM. Code from the person's writing."
  open_questions:
    - "Gödel (first pool): his mathematical platonism is the contemporary abstract-objects view (S8), which alone does not give PLATO. His person file should check whether his own writing goes further (an intelligible reality as the origin of existence and values) before choosing PLATO over a theist code."
    - "Adherents: not applicable (TODO)."
sources:
  - {id: S1, type: tertiary, kind: encyclopedia, author: "Henry J. Blumenthal, A. Hilary Armstrong and others (multi-author article)", citation: "\"Platonism.\" Encyclopaedia Britannica. Online article, main page and subpages 'Neoplatonism: its nature and history', 'Plotinus and his philosophy', 'The later Neoplatonists', 'Augustinian Platonism', 'Medieval Platonism', 'Platonism in the world of revealed religions', 'Renaissance and later Platonism', 'Evaluation of Platonism'. https://www.britannica.com/topic/Platonism.", url: "https://www.britannica.com/topic/Platonism", accessed: 2026-10-01, reliability_note: "Signed reference article. Article paragraphs only; the AI-generated question boxes on Britannica pages were ignored.", used_for: [classification, origins, metaphysics, lio_axes, ethics, practice, science, schools_and_variants]}
  - {id: S2, type: tertiary, kind: encyclopedia, author: "Richard Kraut", year: 2026, citation: "Kraut, Richard. \"Plato.\" Stanford Encyclopedia of Philosophy. First published March 20, 2004; substantive revision April 24, 2026. https://plato.stanford.edu/entries/plato/.", url: "https://plato.stanford.edu/entries/plato/", accessed: 2026-10-01, reliability_note: "Peer-reviewed reference entry.", used_for: [classification, origins, metaphysics, lio_axes, epistemology]}
  - {id: S3, type: tertiary, kind: encyclopedia, author: "Thomas Brickhouse; Nicholas D. Smith", citation: "Brickhouse, Thomas, and Nicholas D. Smith. \"Plato (427–347 B.C.E.).\" Internet Encyclopedia of Philosophy. https://iep.utm.edu/plato/.", url: "https://iep.utm.edu/plato/", accessed: 2026-10-01, reliability_note: "Peer-reviewed reference entry. Locators are the IEP's numbered sections.", used_for: [origins, metaphysics, lio_axes, epistemology]}
  - {id: S4, type: tertiary, kind: encyclopedia, author: "Donald Zeyl; Barbara Sattler", year: 2022, citation: "Zeyl, Donald, and Barbara Sattler. \"Plato's Timaeus.\" Stanford Encyclopedia of Philosophy. First published October 25, 2005; substantive revision May 13, 2022. https://plato.stanford.edu/entries/plato-timaeus/.", url: "https://plato.stanford.edu/entries/plato-timaeus/", accessed: 2026-10-01, reliability_note: "Peer-reviewed reference entry.", used_for: [metaphysics, lio_axes, ethics, science]}
  - {id: S5, type: tertiary, kind: encyclopedia, author: "Paul Kalligas", year: 2024, citation: "Kalligas, Paul. \"Plotinus.\" Stanford Encyclopedia of Philosophy. First published September 25, 2024. https://plato.stanford.edu/entries/plotinus/.", url: "https://plato.stanford.edu/entries/plotinus/", accessed: 2026-10-01, reliability_note: "Peer-reviewed reference entry.", used_for: [origins, metaphysics, lio_axes, schools_and_variants]}
  - {id: S6, type: tertiary, kind: encyclopedia, author: "Sarah Hutton", year: 2020, citation: "Hutton, Sarah. \"The Cambridge Platonists.\" Stanford Encyclopedia of Philosophy. First published October 3, 2001; substantive revision June 29, 2020. https://plato.stanford.edu/entries/cambridge-platonists/.", url: "https://plato.stanford.edu/entries/cambridge-platonists/", accessed: 2026-10-01, reliability_note: "Peer-reviewed reference entry.", used_for: [origins, schools_and_variants]}
  - {id: S7, type: tertiary, kind: encyclopedia, author: "Jeanine Diller", year: 2021, citation: "Diller, Jeanine. \"God and Other Ultimates.\" Stanford Encyclopedia of Philosophy. First published December 17, 2021. https://plato.stanford.edu/entries/god-ultimates/.", url: "https://plato.stanford.edu/entries/god-ultimates/", accessed: 2026-10-01, reliability_note: "Peer-reviewed reference entry.", used_for: [metaphysics, lio_axes]}
  - {id: S8, type: tertiary, kind: encyclopedia, author: "Mark Balaguer", year: 2024, citation: "Balaguer, Mark. \"Platonism in Metaphysics.\" Stanford Encyclopedia of Philosophy. First published May 12, 2004; substantive revision December 24, 2024. https://plato.stanford.edu/entries/platonism/.", url: "https://plato.stanford.edu/entries/platonism/", accessed: 2026-10-01, reliability_note: "Peer-reviewed reference entry; about the contemporary abstract-objects view, not the historical school.", used_for: [science, schools_and_variants, coding_guidance]}
---

# Platonism (PLATO)

> Status: draft — unreviewed. Filled from Stanford Encyclopedia of Philosophy entries, IEP and the multi-author Britannica article. LIO axes use the 0–4 scale (P1). The v7.1 scores and note are unchanged. Adherents are TODO (not applicable).

## Summary

Britannica defines Platonism as "any philosophy that derives its ultimate inspiration from Plato" [S1, introduction]. What the many kinds share is a concern for the quality of human life based on "unchanging and eternal realities, which Plato called forms, independent of the changing things of the world perceived by the senses" [S1, introduction]. The tradition runs from Plato's Academy (4th century BCE) through Middle Platonism and Plotinus' Neoplatonism to Christian, Renaissance and Cambridge Platonism [S1]. Britannica puts the central issue as "the existence (in some sense) of a spiritual or intelligible reality that is independent of the world, and is the ultimate origin of both existence and values" [S1, Evaluation of Platonism].

## Core metaphysics

SEP sums up Plato's central doctrine: the world "that appears to our senses is in some way defective and filled with error", and a more real realm of forms is "eternal, changeless, and in some sense paradigmatic" [S2, §1]. In the Timaeus the universe is "the handiwork of a supremely good, ungrudging Craftsman", and is itself a living thing [S4, §1]. The Craftsman works with Necessity and cannot change what it fixes [S4, §1]. Whether the creation story is literal has divided Platonists since the Old Academy [S4, §2]. Neoplatonism arranges reality in levels of being, each "derived from its superior", with a movement of outgoing and return [S1, Neoplatonism: its nature and history]. Plato argues for an immortal soul and reincarnation [S3, §6.c].

## Position on the LIO axes

Scored on the 0–4 scale (P1):

- A locus 2 (0.5): an intelligible reality and Craftsman apart from the world, plus a world-soul; read by some as panentheism [S4; S7, §2.2].
- B cause 3 (0.7): Intellect and Necessity; no miracles [S4, §1].
- C ledger 2 (0.5): myths of judgment and rebirth [S3].
- D authority 2 (0.5): reason without revelation, but a priori and distrustful of the senses [S2, §1; S1].
- E scope 3 (0.7): universal forms and order [S2, §1].

## Schools and variants

The Old Academy made the forms mathematical, and Speusippus replaced them with numbers [S1]. The Skeptical Academy falls outside the central doctrine [S1, Evaluation of Platonism]. Middle Platonism supplied the Greek background to Philo [S1]. Neoplatonism (Plotinus, Porphyry, Iamblichus, Proclus) later added theurgy [S1, The later Neoplatonists]. Christian Platonism runs through Augustine and Pseudo-Dionysius to Ficino and the Cambridge Platonists [S1; S6]. The contemporary "platonism" about abstract objects is a separate, narrower view [S8].

## Science

The Timaeus gives a mathematical physics in which "fire of tetrahedra, air of octahedra" and water of icosahedra make up the elements [S4, §1]. Aristotle rejected its cosmology because it required "a beginning of time itself" [S4, §2]. SEP notes that the modern abstract-objects view "is a contemporary view" and that "it is not entirely clear that Plato endorsed this view" [S8, introduction].

## Coding guidance

Use PLATO when the person's own working metaphysics is an intelligible reality, independent of the world, that is the source of existence and values [S1, Evaluation of Platonism]. Mathematical platonism alone does not decide the code; record it and code from the rest of the writing [S8]. Platonism inside a revealed religion usually goes to the host religion or CLASS_THEISM. Use ARIST for immanent forms, SCEPT for the Skeptical Academy, and PANENT for a God in and beyond the world without the forms.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> PLATO (37/50) — Platonism. Platonism scores moderately high due to its influential theory of ideal forms, providing philosophical depth for reality and ethics, but limited by abstract nature and modest empirical alignment.

## Open questions

- Gödel's mathematical platonism and this code (see review).
- How to place a priori reason on D_authority.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-01 (overnight run): read SEP "Plato", "Plato's Timaeus", "Plotinus", "The Cambridge Platonists", "God and Other Ultimates" and "Platonism in Metaphysics"; IEP "Plato"; Britannica "Platonism" (main page and eight subpages, multi-author). AI-generated question boxes on Britannica pages were not used. All quotations were checked word for word against the fetched page text with a script.
