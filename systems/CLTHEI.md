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
    - {date: 2026-10-01, by: scripts/make_system_stubs.py, summary: "Display label approved (OPEN_DECISIONS S1); CLASS_THEISM relation changed to 'neighbor (easily confused)' (S5)."}
    - {date: 2026-10-01, by: "Grok Bot", summary: "Draft: classification, origins, metaphysics, LIO axes (0–4, P1), science, schools and coding guidance filled from six SEP entries and two Britannica articles. v7.1 scores and note unchanged. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Coding guidance wording: B_cause is scored on the person's account of nature (decision P6). No scores changed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit fixes: B_cause quote attributed to William Adams (1767), as quoted in SEP Miracles §1.1; E_scope certainty 0.7 -> 0.5 and the Clarke miracle-definition quote dropped (no source addresses scope directly). Not reviewed."}
identity:
  id: CLTHEI
  v7_1_number: 72
  v7_1_label: "Classical Theism (personal, interventionist Creator God)"
  display_label: "Interventionist personal theism"
  label_status: "approved"
  aliases: ["popular interventionist personal God", "theistic personalism (in part)", "interventionist theism", "special divine action theism"]
classification:
  kind: {value: "family of positions", certainty: 0.7, cites: [{source: S1, locator: "§2.2"}, {source: S6, locator: "§3.1"}], how_known: "The code names a picture of God (personal, answers petition, works miracles) found across the Abrahamic religions and in modern positions such as open theism and interventionist creationism. It is not one religion or school. Coder's reading, so 0.7."}
  family: {value: "Abrahamic monotheism, personal and interventionist form: theism as distinct from deism", certainty: 1.0, cites: [{source: S2, locator: "introduction; 'Deism'"}, {source: S8, locator: "Nature and scope"}], how_known: "Britannica: theism speaks of the ultimate reality 'in personal terms'; the deist God 'is not involved in the world in the same personal way'; 19th–20th-century theologians contrasted deism with 'theism, the belief in an immanent God who actively intervenes in the affairs of men'."}
  parent_traditions:
    value: ["the Jewish idea of a single God who acts in history and hears prayer", "Christian and Islamic theism built on it"]
    certainty: 1.0
    cites: [{source: S1, locator: "§2.2"}]
    how_known: "SEP: perfect being theology fused 'the Jewish idea of a single God that acts in history' with Greek perfection; the God 'who hears our prayers and who intervenes in the world' is the Jewish side of that fusion, passed to Christianity and Islam."
  related_codes:
    - {code: CLASS_THEISM, relation: "neighbor (easily confused)", note: "v7.1 coding rule: CLTHEI is not CLASS_THEISM"}
    - {code: CHRIST, relation: "neighbor (easily confused)"}
    - {code: ISLAM, relation: "neighbor (easily confused)"}
    - {code: JUDA, relation: "neighbor (easily confused)"}
    - {code: DEISM, relation: "contrast case", note: "Britannica: the deist God is not involved in the world in the same personal way"}
origins:
  founding_era: {value: "No founding event. The God who acts in history and hears prayer is the biblical idea (SEP). As named modern positions: 'theistic personalism' against classical theism (a split SEP dates perhaps as early as 1644), open theism (1994 onward) and interventionist creationism and Intelligent Design (late 20th century).", certainty: 0.7, cites: [{source: S1, locator: "§2.2; bibliography (Pinnock et al. 1994, Sanders 1998)"}, {source: S6, locator: "§3.1"}], how_known: "Dates from SEP. Treating these as the code's origins is a coder's summary, so 0.7."}
  founding_region: {value: "Ancient Israel for the root idea; the modern named positions are mainly Anglo-American (open theism, Intelligent Design).", certainty: 0.5, cites: [{source: S1, locator: "§2.2"}, {source: S6, locator: "§3.1 (US constitutional context of Intelligent Design)"}], how_known: "Inferred from where the cited works and debates are placed; no source states a region for the code. Reconstruction, so 0.5."}
  founders_or_key_figures: {value: ["no founder", "open theists Clark Pinnock, Richard Rice, John Sanders, William Hasker and David Basinger", "Intelligent Design creationist William Dembski", "Alvin Plantinga (God may have guided each mutation)"], certainty: 0.7, cites: [{source: S1, locator: "§2.2; bibliography"}, {source: S6, locator: "§3.1"}], how_known: "Named in SEP as holding open-theist or interventionist views. They are examples, not founders."}
  key_texts:
    - {value: "The Openness of God: a Biblical Challenge to the Traditional Understanding of God", author: "Clark H. Pinnock, Richard Rice, John Sanders, William Hasker and David Basinger", year: 1994, certainty: 1.0, cites: [{source: S1, locator: "§2.2; bibliography"}], how_known: "Cited in SEP as a statement of open theism."}
    - {value: "The God Who Risks: A Theology of Providence", author: "John Sanders", year: 1998, certainty: 1.0, cites: [{source: S1, locator: "§2.2; bibliography"}], how_known: "Cited in SEP for open theism."}
    - {value: "The Design Inference: Eliminating Chance through Small Probabilities", author: "William A. Dembski", year: 1998, certainty: 1.0, cites: [{source: S6, locator: "§3.1; bibliography"}], how_known: "Cited in SEP for Intelligent Design, which 'affirms divine intervention in natural processes'."}
metaphysics:
  god_nature_relation: {value: "God created the world and is distinct from it; the world depends on God, who also acts within it.", stance: "creator distinct from creation", certainty: 1.0, cites: [{source: S6, locator: "§3.1"}, {source: S2, locator: "introduction"}], how_known: "SEP's summary of the doctrine of creation; Britannica on theism."}
  deity_personal: {value: "Personal, and fully so. Theistic personalists 'deny or weaken the Greek perfections to save God’s personhood'; open theists drop immutability and impassibility so that God can be 'in an ongoing, dynamic relationship with us'.", stance: personal, certainty: 1.0, cites: [{source: S1, locator: "§2.2"}], how_known: "SEP states it directly."}
  intervention: {value: "God acts in particular events as well as sustaining the world: 'special divine actions (e.g., miracles and revelations)' in addition to general creation and sustenance. Creationists hold that God 'occasionally performs special divine actions (miracles) that intervene in the fabric of those laws'.", stance: regular, certainty: 0.7, cites: [{source: S6, locator: "§3.1"}], how_known: "SEP. The stance 'regular' is a coder's reading for the popular form, where God answers prayer in ordinary life; creationists say 'occasionally'."}
  miracles: {value: "Affirmed, often defined as a violation of the laws of nature by a god (Hume's and Swinburne's definitions) or as an event beyond the productive power of nature. Samuel Clarke ties the miracle to proof of a doctrine or of a person's authority.", stance: affirmed, certainty: 1.0, cites: [{source: S4, locator: "§1.1; §1.2; §1.3"}, {source: S6, locator: "§3.1"}], how_known: "SEP entries."}
  petition_and_prayer: {value: "Petition is effective: God brings about what was asked 'at least in part because of' the prayer. This is the sense of answered prayer that the philosophical puzzles about immutability and impassibility are about.", stance: "petition answered", certainty: 1.0, cites: [{source: S3, locator: "§1; §2"}], how_known: "SEP Petitionary Prayer."}
  afterlife: {value: "Personal survival beyond the grave, with heaven and hell in the Christian forms.", stance: "personal afterlife", certainty: 0.7, cites: [{source: S7, locator: "introduction"}], how_known: "SEP Heaven and Hell in Christian Thought; generalising it to the whole code is a coder's reading, so 0.7."}
  moral_ledger: {value: "In the popular form, 'heaven and hell are essentially deserved compensations for the kind of earthly lives we live'. SEP adds that virtually all Christian theologians call that view 'overly simplistic and unsophisticated'.", stance: "personal reward and punishment", certainty: 0.7, cites: [{source: S7, locator: "introduction"}], how_known: "SEP describes the popular view directly; applying it to the code is a coder's reading."}
  authority: {value: "Knowledge of God comes through revelation, sacred authority and religious experience, which matter most 'for those who stress the personal involvement of God in the lives of human beings'. Miracles are treated as evidence for doctrine.", stance: "both, revelation first", certainty: 0.7, cites: [{source: S2, locator: "The problem of particular knowledge of God: 'Theism and religious experience'"}, {source: S4, locator: "§1.3"}], how_known: "Britannica and SEP; the stance is a coder's reading."}
  reserved_exemptions: {value: "Central: particular acts of God that break or go beyond the regular course of nature (miracles, answered prayer, revelations).", stance: central, certainty: 1.0, cites: [{source: S6, locator: "§3.1"}, {source: S4, locator: "§1.2"}], how_known: "SEP: this concept of divine action is 'commonly labeled interventionist'."}
  teleology_in_nature: {value: "Providence: 'God governs creation as a loving father, working all things for good'. Intelligent Design infers 'design and purposiveness' in organisms.", stance: "designer's purposes", certainty: 1.0, cites: [{source: S5, locator: "introduction"}, {source: S6, locator: "§3.1"}], how_known: "SEP entries."}
  necessity_and_freedom: {value: "Creatures have libertarian free will in most modern forms. Open theism makes God temporal: God 'must await the actions of free creatures in order to know with certainty what they will be'. Traditional theism keeps everything under God's providence, which raises the problem of evil.", certainty: 1.0, cites: [{source: S5, locator: "introduction; §3"}], how_known: "SEP Divine Providence."}
lio_axes:
  A_locus: {value: 0, rationale: "At the interventionist pole: a transcendent creator, distinct from the world, who is a full person in relationship with us.", certainty: 1.0, cites: [{source: S1, locator: "§2.2"}, {source: S6, locator: "§3.1"}], how_known: "Scored on the 0–4 scale (P1). The sources state the pole features directly."}
  B_cause: {value: 1, rationale: "Leans interventionist: miracles, answered petition and special divine action are central, but they are exceptions against a regular course of nature that the position also affirms: as William Adams (1767) put it, as quoted in SEP Miracles (S4, §1.1), 'There must be an ordinary regular course of nature, before there can be any thing extraordinary'.", certainty: 0.7, cites: [{source: S6, locator: "§3.1"}, {source: S3, locator: "§1"}, {source: S4, locator: "§1.1"}], how_known: "0–4 scale (P1). 1 rather than 0 because creationists say God acts 'occasionally'; popular piety may sit at 0."}
  C_ledger: {value: 1, rationale: "Leans interventionist: the popular form treats heaven and hell as deserved reward and punishment; theologians nuance this, and the code does not require it.", certainty: 0.5, cites: [{source: S7, locator: "introduction"}], how_known: "0–4 scale (P1). 0.5: one source, on Christian thought only."}
  D_authority: {value: 1, rationale: "Leans interventionist: revelation, sacred authority, religious experience and miracles as evidence for doctrine; some defenders also argue from evidence (Intelligent Design claims to infer design).", certainty: 0.5, cites: [{source: S2, locator: "'Theism and religious experience'"}, {source: S4, locator: "§1.3"}, {source: S6, locator: "§3.1"}], how_known: "0–4 scale (P1). 0.5 because the forms differ."}
  E_scope: {value: 1, rationale: "Leans interventionist: God acts for particular people in answer to their prayers (S3, §1); the laws of nature still hold for everything else.", certainty: 0.5, cites: [{source: S3, locator: "§1"}], how_known: "0–4 scale (P1). Coder's reading: no source addresses scope directly, so 0.5, as for CLASS_THEISM. The Clarke quote on miracles attesting a particular person's authority was dropped after the lens audit (2026-10-02): it is a definition of a miracle, not evidence about in-group exceptions."}
epistemology: {value: "God is known by revelation and authority, by religious experience, and by evidence such as miracles or design. Analogy (from Aquinas) is also used, but Britannica notes it leaves faith 'very thin and remote, far from the warm fellowship' that personal theism wants.", certainty: 1.0, cites: [{source: S2, locator: "The problem of particular knowledge of God"}, {source: S4, locator: "§1.3; §4"}], how_known: "Britannica and SEP."}
ethics: {value: TODO, note: "The code has no ethics of its own; it inherits the host religion's. Not researched for the code as such."}
practice:
  ritual_and_practice: {value: "Petitionary prayer is central: people ask God for things and expect God to act on the request.", certainty: 1.0, cites: [{source: S3, locator: "introduction; §1"}], how_known: "SEP Petitionary Prayer."}
  community_form: {value: "No body of its own; it is found inside churches, synagogues and mosques and in movements such as creationism and Intelligent Design.", certainty: 0.7, cites: [{source: S6, locator: "§3.1"}, {source: S3, locator: "introduction"}], how_known: "Coder's reading of SEP."}
science:
  historical_stance: {value: "From the seventeenth century, 'scientific laws' in physics 'seemed to leave no room for special divine action', and geology and evolution challenged the biblical accounts of creation. Newton, in a 1713 addendum to the Principia, held that the positions of the planets' orbits and of the stars required a divine explanation.", certainty: 1.0, cites: [{source: S6, locator: "§3.1"}], how_known: "SEP Religion and Science."}
  current_stance: {value: "Ranges from conflict to accommodation. Creationists deny any role of natural selection in the origin of species (Young Earth creationists also reject geology), and Intelligent Design 'affirms divine intervention in natural processes'. Others look for 'non-interventionist' special action in quantum or chaotic indeterminacy (Russell, Murphy, Polkinghorne).", certainty: 1.0, cites: [{source: S6, locator: "§3.1"}], how_known: "SEP Religion and Science."}
schools_and_variants:
  - {name: "Popular petitionary and miracle piety (Christian, Jewish, Muslim)", form: popular, how_it_differs: "God answers everyday prayer and rewards and punishes; theologians call the reward-and-punishment picture overly simple.", lio_difference: "B and C at or near 0.", certainty: 0.7, cites: [{source: S3, locator: "§1"}, {source: S7, locator: "introduction"}]}
  - {name: "Open theism", form: modern, how_it_differs: "God is temporal and learns free creatures' choices as they happen; immutability and impassibility are dropped for a 'dynamic relationship'.", lio_difference: "A at 0 (strongly personal). B stays low: God responds to events.", certainty: 1.0, cites: [{source: S1, locator: "§2.2"}, {source: S5, locator: "§3"}]}
  - {name: "Creationism (Young Earth and Old Earth) and Intelligent Design", form: modern, how_it_differs: "God created the laws and occasionally intervenes in them; natural selection is denied a significant role.", lio_difference: "B low in biology and geology; E low.", certainty: 1.0, cites: [{source: S6, locator: "§3.1"}]}
  - {name: "Non-interventionist special divine action (quantum and chaos models)", form: modern, how_it_differs: "God acts specially in nature without suspending laws, in the openness of quantum events or chaotic systems.", lio_difference: "B moves up toward 2–3; A stays 0. Borderline with CLASS_THEISM.", certainty: 1.0, cites: [{source: S6, locator: "§3.1"}]}
adherents:
  use: "context only — never a genius-rate denominator"
  estimate: {value: TODO, note: "Not a census category. Survey data on belief in a personal God or answered prayer could give context; none was read in this run."}
v7_1_rubric:
  label: "authorial v7.1 scores"
  L: 7
  P: 5
  E: 3
  V: 3
  X: 2
  total: 20
  scoring_note: "Classical Theism scores low due to persistent logical paradoxes like the problem of evil and reliance on revelation over empirical evidence, though it provides a foundational framework for many Abrahamic religions."
  source: "v7.1 data book, section 6 table (tables[4]) row 72 and section 7 scoring notes"
revised_rubric:
  status: "not started"
  L: {score: TODO, rationale: ""}
  P: {score: TODO, rationale: ""}
  E: {score: TODO, rationale: ""}
  V: {score: TODO, rationale: ""}
  X: {score: TODO, rationale: ""}
coding_guidance:
  use_when: "v7.1 coding rule (Split theisms): CLASS_THEISM (Aristotelian-Thomistic-Falsafa) is not CLTHEI (popular interventionist personal God) and not generic CHRIST/ISLAM/JUDA. v8 coding guide: CLTHEI is the popular interventionist personal God who answers petition and works miracles. Use it when the person's own writing (1) treats God as a person who responds to requests or to events, and (2) expects God to act in particular events, against or beyond the regular course of nature (S3 §1; S6 §3.1). Interventionist creationism and open theism fall here."
  do_not_use_when: "God is simple and immutable and prayer does not change God (Aquinas, Avicenna, Maimonides): CLASS_THEISM. The working view is the confessed religion and the writing does not show an interventionist God more than its creeds do: CHRIST, ISLAM or JUDA. God made the world and its laws and then does not intervene: DEISM. Accepts scriptural miracles but allows no exceptions in their account of nature: still score B_cause on their account of nature (CODING_GUIDE §6; decision P6), and consider the host religion or CLASS_THEISM before CLTHEI. Church membership or upbringing alone: never a code."
  neighbors:
    - {code: CLASS_THEISM, relation: "neighbor (easily confused)"}
    - {code: CHRIST, relation: "neighbor (easily confused)"}
    - {code: ISLAM, relation: "neighbor (easily confused)"}
    - {code: JUDA, relation: "neighbor (easily confused)"}
    - {code: DEISM, relation: "contrast case"}
review:
  data_quality_flags:
    - "v7.1 used 'Classical Theism' for both CLASS_THEISM and CLTHEI. The display label keeps the code and separates the names (approved 2026-10-01, OPEN_DECISIONS S1)."
    - "v7.1 table 4 label is truncated; v7_1_label is taken from the section 7 scoring note."
    - "The v7.1 scoring note for CLTHEI says 'Classical Theism scores low due to persistent logical paradoxes like the problem of evil'. In SEP the problem of evil arises for 'traditional theism' as a whole, including the classical God of CLASS_THEISM (S5 introduction), which v7.1 scores 43. So the problem of evil does not by itself separate the two codes; intervention and petition do. v7.1 text left unchanged."
    - "Britannica (S8) calls the theist's God 'immanent' in the sense of actively present. On the LIO A axis this is still a transcendent person outside the world, not identity with it."
  open_questions:
    - "Newton (first pool): S6 §3.1 reports his 1713 view that orbit positions need a divine explanation. Read his own words before coding him; that is a person-file question, not settled here."
    - "Ethics and adherents are TODO for the code."
sources:
  - {id: S1, type: tertiary, kind: encyclopedia, author: "Jeanine Diller", year: 2021, citation: "Diller, Jeanine. \"God and Other Ultimates.\" Stanford Encyclopedia of Philosophy. First published December 17, 2021. https://plato.stanford.edu/entries/god-ultimates/.", url: "https://plato.stanford.edu/entries/god-ultimates/", accessed: 2026-10-01, reliability_note: "Peer-reviewed reference entry.", used_for: [classification, origins, metaphysics, lio_axes, schools_and_variants]}
  - {id: S2, type: tertiary, kind: encyclopedia, author: "Hywel David Lewis", citation: "Lewis, Hywel David. \"Theism.\" Encyclopaedia Britannica. Online article, pages 'theism' and 'The problem of particular knowledge of God'. https://www.britannica.com/topic/theism.", url: "https://www.britannica.com/topic/theism", accessed: 2026-10-01, reliability_note: "Signed reference article. Only the article paragraphs were used; the AI-generated question boxes at the top of the Britannica page were ignored.", used_for: [classification, metaphysics, lio_axes, epistemology]}
  - {id: S3, type: tertiary, kind: encyclopedia, author: "Scott A. Davison", year: 2026, citation: "Davison, Scott A. \"Petitionary Prayer.\" Stanford Encyclopedia of Philosophy. First published August 15, 2012; substantive revision May 18, 2026. https://plato.stanford.edu/entries/petitionary-prayer/.", url: "https://plato.stanford.edu/entries/petitionary-prayer/", accessed: 2026-10-01, reliability_note: "Peer-reviewed reference entry.", used_for: [metaphysics, lio_axes, practice]}
  - {id: S4, type: tertiary, kind: encyclopedia, author: "Timothy McGrew; Robert Larmer", year: 2024, citation: "McGrew, Timothy, and Robert Larmer. \"Miracles.\" Stanford Encyclopedia of Philosophy. First published October 11, 2010; substantive revision May 7, 2024. https://plato.stanford.edu/entries/miracles/.", url: "https://plato.stanford.edu/entries/miracles/", accessed: 2026-10-01, reliability_note: "Peer-reviewed reference entry. Clarke and Adams are quoted as given there.", used_for: [metaphysics, lio_axes, epistemology]}
  - {id: S5, type: tertiary, kind: encyclopedia, author: "Hugh J. McCann; Daniel M. Johnson", year: 2022, citation: "McCann, Hugh J., and Daniel M. Johnson. \"Divine Providence.\" Stanford Encyclopedia of Philosophy. First published August 1, 2001; substantive revision December 9, 2022. https://plato.stanford.edu/entries/providence-divine/.", url: "https://plato.stanford.edu/entries/providence-divine/", accessed: 2026-10-01, reliability_note: "Peer-reviewed reference entry.", used_for: [metaphysics, schools_and_variants, review]}
  - {id: S6, type: tertiary, kind: encyclopedia, author: "Helen De Cruz", year: 2022, citation: "De Cruz, Helen. \"Religion and Science.\" Stanford Encyclopedia of Philosophy. First published January 17, 2017; substantive revision September 3, 2022. https://plato.stanford.edu/entries/religion-science/.", url: "https://plato.stanford.edu/entries/religion-science/", accessed: 2026-10-01, reliability_note: "Peer-reviewed reference entry.", used_for: [classification, origins, metaphysics, lio_axes, science, schools_and_variants]}
  - {id: S7, type: tertiary, kind: encyclopedia, author: "Thomas Talbott", year: 2025, citation: "Talbott, Thomas. \"Heaven and Hell in Christian Thought.\" Stanford Encyclopedia of Philosophy. First published April 23, 2013; substantive revision May 10, 2025. https://plato.stanford.edu/entries/heaven-hell/.", url: "https://plato.stanford.edu/entries/heaven-hell/", accessed: 2026-10-01, reliability_note: "Peer-reviewed reference entry; covers Christian thought only.", used_for: [metaphysics, lio_axes, schools_and_variants]}
  - {id: S8, type: tertiary, kind: encyclopedia, author: "David A. Pailin", citation: "Pailin, David A. \"Deism.\" Encyclopaedia Britannica. Online article. https://www.britannica.com/topic/Deism.", url: "https://www.britannica.com/topic/Deism", accessed: 2026-10-01, reliability_note: "Signed reference article. Article paragraphs only, not the AI question boxes.", used_for: [classification]}
---

# Interventionist personal theism (CLTHEI)

> Status: draft — unreviewed. Filled from Stanford Encyclopedia of Philosophy entries and two signed Britannica articles. LIO axes use the 0–4 scale (P1). The v7.1 scores and note are unchanged. Ethics and adherents are TODO.

## Summary

CLTHEI is the popular picture of a personal God who hears prayer and acts in the world. SEP traces it to "the Jewish idea of a single God that acts in history" [S1, §2.2]. In modern philosophy its nearest named form is "theistic personalism", which gives up divine simplicity and immutability to keep God fully personal; open theism is one example [S1, §2.2]. Britannica describes the older contrast with deism: theism as "the belief in an immanent God who actively intervenes in the affairs of men" [S8, Nature and scope]. The v7.1 rule calls it the "popular interventionist personal God" and keeps it apart from CLASS_THEISM.

## Core metaphysics

God created the world, is distinct from it, and acts in it through "special divine actions (e.g., miracles and revelations)" as well as by sustaining it [S6, §3.1]. Prayer is effective: God brings about what was asked "at least in part because of" the prayer [S3, §1]. Miracles are affirmed, and Hume's and Swinburne's definitions make them violations of natural law [S4, §1.2; S6, §3.1]. In the popular Christian form, heaven and hell are deserved reward and punishment, a view theologians call "overly simplistic and unsophisticated" [S7, introduction]. Open theism makes God temporal, so that God "must await the actions of free creatures" [S5, §3].

## Position on the LIO axes

Scored on the 0–4 scale (P1):

- A locus 0 (1.0): a transcendent, fully personal creator [S1, §2.2].
- B cause 1 (0.7): miracles and answered petition against a regular course of nature [S6, §3.1; S4, §1.1].
- C ledger 1 (0.5): popular heaven and hell as deserved compensation [S7].
- D authority 1 (0.5): revelation, authority and religious experience [S2].
- E scope 1 (0.5): God acts for particular people in answer to prayer [S3, §1]; no source addresses scope directly.

## Schools and variants

Popular petitionary and miracle piety; open theism [S1, §2.2; S5, §3]; creationism and Intelligent Design, which "affirms divine intervention in natural processes" [S6, §3.1]; and non-interventionist models of special divine action, which place God's action in quantum or chaotic openness [S6, §3.1]. The last of these moves B up and borders on CLASS_THEISM.

## Science

SEP says the law-based physics of the seventeenth and eighteenth centuries "seemed to leave no room for special divine action" [S6, §3.1]. Newton answered in 1713 that orbit positions needed a divine explanation [S6, §3.1]. Today creationists reject natural selection's role in the origin of species, Intelligent Design argues for intervention, and quantum and chaos models try to keep special action without breaking laws [S6, §3.1].

## Coding guidance

Use CLTHEI when the person's own writing treats God as a person who responds to requests or events and acts in particular events beyond the regular course of nature [S3, §1; S6, §3.1]. Use CLASS_THEISM for a simple, immutable God whom prayer does not change, DEISM for a God who does not intervene, and CHRIST, ISLAM or JUDA for the confessed religion when the writing shows nothing more specific. Score B_cause on the person's account of nature: someone can accept scriptural miracles and allow no exceptions in nature (CODING_GUIDE §6; decision P6).

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> CLTHEI (20/50) — Classical Theism (personal, interventionist Creator God). Classical Theism scores low due to persistent logical paradoxes like the problem of evil and reliance on revelation over empirical evidence, though it provides a foundational framework for many Abrahamic religions.

## Open questions

- The v7.1 note blames the problem of evil, which SEP treats as a problem for traditional theism as a whole [S5, introduction]. See review flags.
- Newton's 1713 remark [S6, §3.1] is relevant to his person file. It does not decide his code.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-01 (overnight run): read SEP "God and Other Ultimates", "Petitionary Prayer", "Miracles", "Divine Providence", "Religion and Science" and "Heaven and Hell in Christian Thought", and Britannica "Theism" (H. D. Lewis; two pages) and "Deism" (D. A. Pailin). The Britannica pages carry AI-generated question boxes above the article; those were not used. All quotations were checked word for word against the fetched page text with a script. Not read: survey data on belief in answered prayer, IEP.
