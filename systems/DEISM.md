---
record:
  record_type: system
  schema_version: "1.1"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (overnight systems run for Jason)"
  model_used: "Grok Bot executor agent; direct reads of the cited encyclopedia entries"
  collected_on: 2026-10-01
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-01, by: scripts/make_system_stubs.py, summary: "Stub created from v7.1 data book table 4 and section 7."}
    - {date: 2026-10-01, by: "Grok Bot", summary: "Draft: classification, origins, metaphysics, LIO axes (0–4, P1), science, schools and coding guidance filled from seven SEP entries and the Britannica article. v7.1 scores and note unchanged. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit fix: 'providence' is not in the Britannica text; the intervention field, the B_cause rationale and the data quality flag now quote Britannica on prophetic revelation and cite Clarke's taxonomy (SEP Clarke §4.5) for providential action. No score changed. Not reviewed."}
identity:
  id: DEISM
  v7_1_number: 31
  v7_1_label: "Deism"
  display_label: "Deism"
  label_status: "as in v7.1"
  aliases: ["natural religion (in part)", "rational religion"]
classification:
  kind: {value: "family of positions", certainty: 0.7, cites: [{source: S1, locator: "introduction; 'The English Deists'"}], how_known: "Britannica calls it an unorthodox religious attitude and says there is no single work that can be designated as the quintessential expression of Deism. It had no church or creed, so it is coded as a family of positions; coder's reading, 0.7."}
  family: {value: "Enlightenment natural religion; a theistic dualism of God and world", certainty: 1.0, cites: [{source: S2, locator: "§2.3"}, {source: S4, locator: "§2.2"}], how_known: "SEP: deism is the form of religion most associated with the Enlightenment; SEP God and Other Ultimates files it among theistic dualisms."}
  parent_traditions: {value: ["Christian theology of a perfect creator (perfect being theology)", "Newtonian natural philosophy", "Locke's philosophy (for the English deists)"], certainty: 0.7, cites: [{source: S4, locator: "§2.2"}, {source: S2, locator: "§2.3"}], how_known: "SEP: perfect being theology met Newtonian mechanics and spawned deism; the English deists were influenced by Locke. Listing them as parents is the coder's summary, 0.7."}
  related_codes:
    - {code: CLTHEI, relation: "contrast case", note: "19th–20th-century theologians defined deism against theism as belief in a God who intervenes (Britannica)"}
    - {code: CLASS_THEISM, relation: "neighbor (easily confused)", note: "both reject a God whom prayer changes; CLASS_THEISM keeps revelation and continuous divine causation"}
    - {code: CHRIST, relation: "parent tradition", note: "English deism grew inside and against Christianity; many deists kept Jesus as a moral teacher"}
    - {code: PANDEI, relation: offshoot, note: "Britannica: pandeism tried to unite deism and pantheism"}
    - {code: ATHE, relation: "neighbor (easily confused)", note: "Britannica: among the French philosophes the line between deism and atheism was often blurred"}
origins:
  founding_era: {value: "First half of the 17th century (Herbert of Cherbury) to the middle of the 18th century in England, with a high point from about 1689 to 1742; then France and Germany in the later 18th century and the United States in the late 18th and early 19th centuries.", certainty: 1.0, cites: [{source: S1, locator: "introduction; 'Nature and scope'"}], how_known: "Britannica states the dates."}
  founding_region: {value: "England, then France, Germany and the United States", certainty: 1.0, cites: [{source: S1, locator: "introduction; page 'Deists in other countries'"}, {source: S2, locator: "§2.3"}], how_known: "Britannica and SEP."}
  founders_or_key_figures: {value: ["Edward Herbert, 1st Baron Herbert of Cherbury", "John Toland", "Anthony Collins", "Matthew Tindal", "Thomas Woolston", "Shaftesbury", "Viscount Bolingbroke", "Voltaire", "H. S. Reimarus", "Thomas Paine", "Benjamin Franklin"], certainty: 1.0, cites: [{source: S1, locator: "'The English Deists'; page 'Deists in other countries'"}, {source: S2, locator: "§2.3"}, {source: S6, locator: "§3"}], how_known: "Named as deists in Britannica and SEP. The canon was fixed by an opponent, John Leland, in 1754–56; Herbert was not known as a Deist in his day (Britannica)."}
  key_texts:
    - {value: "Christianity Not Mysterious", author: "John Toland", year: 1696, certainty: 1.0, cites: [{source: S2, locator: "§2.3"}], how_known: "SEP."}
    - {value: "A Discourse of Freethinking", author: "Anthony Collins", year: 1713, certainty: 1.0, cites: [{source: S2, locator: "§2.3"}], how_known: "SEP."}
    - {value: "Christianity as Old as Creation", author: "Matthew Tindal", year: 1730, certainty: 1.0, cites: [{source: S2, locator: "§2.3"}], how_known: "SEP."}
    - {value: "A Letter Concerning Enthusiasm", author: "Shaftesbury", year: 1708, certainty: 1.0, cites: [{source: S1, locator: "'The English Deists'"}], how_known: "Britannica: probably the crucial document in propagating Deist ideas."}
    - {value: "Apologie oder Schutzschrift für die vernünftigen Verehrer Gottes", author: "H. S. Reimarus", year: "published 1774–78 (by Lessing, after Reimarus's death)", certainty: 1.0, cites: [{source: S1, locator: "page 'Deists in other countries'"}], how_known: "Britannica."}
    - {value: "The Age of Reason", author: "Thomas Paine", year: "1790s", certainty: 0.7, cites: [{source: S6, locator: "introduction; §3"}], how_known: "SEP calls it a popular deist text. The page read does not give a single year; 1790s is the coder's, so 0.7."}
metaphysics:
  god_nature_relation: {value: "God is a supreme intelligence who created the world and is distinct from it; SEP files deism as a dualism because it assumes God can leave the world behind.", stance: "creator distinct from creation", certainty: 1.0, cites: [{source: S2, locator: "§2.3"}, {source: S4, locator: "§2.2"}], how_known: "SEP states it directly."}
  deity_personal: {value: "An intelligent creator with a plan, often called the Prime Mover or Original Architect. Deists differed on whether God has moral attributes or cares what happens (Clarke's four categories). Critics called the deist God distant and abstract.", stance: "varies by school", certainty: 0.7, cites: [{source: S2, locator: "§2.3"}, {source: S3, locator: "§4.5"}, {source: S7, locator: "§2.1"}], how_known: "SEP. The stance is the coder's reading of the spread, 0.7."}
  intervention: {value: "Typically none: 'the being does not interfere with creation' (SEP). Britannica warns that the stark version, God withdrawing after creation, 'was accepted by very few Deists' and was often forced on them by opponents, and 'It was possible to believe even in prophetic revelation and still remain a Deist', revelation being taken as a natural historical occurrence. In Clarke's taxonomy, one group of deists 'accept providential action in the world' (S3, §4.5).", stance: none, certainty: 0.7, cites: [{source: S2, locator: "§2.3"}, {source: S1, locator: "'Nature and scope'; 'The English Deists'"}, {source: S3, locator: "§4.5"}], how_known: "SEP and Britannica disagree on how typical the stark view was; 0.7."}
  miracles: {value: "Typically rejected. Deists accepted the moral teachings of the Bible without any commitment to the historical reality of the reported miracles; Woolston read the New Testament allegorically.", stance: denied, certainty: 0.7, cites: [{source: S2, locator: "§2.3"}, {source: S1, locator: "'The English Deists'"}], how_known: "Both sources say typically; 0.7 for the exceptions."}
  petition_and_prayer: {value: "Herbert counted worship among the innate religious ideas and a pious and virtuous life as its most desirable form. A God who does not interfere does not answer petitions; critics said the deist God does not meet the human needs from which religion springs.", stance: "no petition", certainty: 0.5, cites: [{source: S1, locator: "'The English Deists'"}, {source: S2, locator: "§2.3"}], how_known: "Sources do not discuss petition directly; the stance is inferred from non-intervention, so 0.5."}
  afterlife: {value: "Divided. Herbert's five innate ideas include rewards and punishments in the next world, and Franklin's creed reproduced them; Clarke's third category of deists denied the immortality of the soul.", stance: "varies by school", certainty: 1.0, cites: [{source: S1, locator: "'The English Deists'; page 'Deists in other countries'"}, {source: S3, locator: "§4.5"}], how_known: "Stated directly."}
  moral_ledger: {value: "For Herbert-type deists, repentance and future rewards and punishments are part of natural religion; for others, morality stands without a future state, or (Clarke's second category) without moral attributes in God. Kant held that moral principles come from reason, not revelation.", stance: "varies by school", certainty: 1.0, cites: [{source: S1, locator: "'The English Deists'; page 'Deists in other countries'"}, {source: S3, locator: "§4.5"}], how_known: "Stated directly."}
  authority: {value: "Reason and nature only: religious knowledge 'inborn in every person or that can be acquired by the use of reason', and rejection of what comes 'through either revelation or the teaching of any church'. Proofs of God were mostly from design and order.", stance: "observation and reason", certainty: 1.0, cites: [{source: S1, locator: "introduction; 'The English Deists'"}, {source: S2, locator: "§2.3"}], how_known: "Britannica and SEP state it directly."}
  reserved_exemptions: {value: "None in the typical form; moderate deists who kept a place for revelation treated it as a natural event.", stance: none, certainty: 0.7, cites: [{source: S1, locator: "'The English Deists'"}], how_known: "Britannica; 0.7 for the moderate exceptions."}
  teleology_in_nature: {value: "The supreme being has a plan for creation from the beginning; the machine-like order of the cosmos needs God as its author (the design argument).", stance: "designer's purposes", certainty: 1.0, cites: [{source: S2, locator: "§2.3"}, {source: S1, locator: "'The English Deists'"}], how_known: "SEP and Britannica."}
  necessity_and_freedom: {value: "No single view. Collins argued for a compatibilist determinism and rejected free will; questions of materialism, determinism and providential purpose were central to the writings of deists such as Toland and Collins.", certainty: 0.7, cites: [{source: S8, locator: "§1.1"}], how_known: "SEP on Collins; generalising beyond him is the coder's, 0.7."}
lio_axes:
  A_locus: {value: 1, rationale: "A transcendent creator distinct from the world, but a thin or distant person (Prime Mover, Original Architect); some deists denied God moral attributes. METHOD §1.1: a deist God is a transcendent person (A low).", certainty: 0.7, cites: [{source: S2, locator: "§2.3"}, {source: S3, locator: "§4.5"}, {source: S4, locator: "§2.2"}], how_known: "Scored on the 0–4 scale (P1). Coder's reading, 0.7."}
  B_cause: {value: 3, rationale: "God made the world to run by its laws and typically does not interfere; miracles are rejected. Not 4, because Britannica says very few deists held the stark non-interference view and that one could believe in prophetic revelation and remain a deist; Clarke also describes deists who accept providential action in the world (S3, §4.5).", certainty: 0.7, cites: [{source: S2, locator: "§2.3"}, {source: S1, locator: "'Nature and scope'"}, {source: S5, locator: "§3.1"}, {source: S3, locator: "§4.5"}], how_known: "0–4 scale (P1). The stark modern form (God only set the initial conditions) would be 4."}
  C_ledger: {value: 2, rationale: "Split: Herbert-line deists kept rewards and punishments in the next world, earned by virtue and repentance (toward 1); others denied a future state (toward 3–4). No ritual or priestly ledger in any form.", certainty: 0.5, cites: [{source: S1, locator: "'The English Deists'"}, {source: S3, locator: "§4.5"}], how_known: "0–4 scale (P1). 0.5 because deists disagreed."}
  D_authority: {value: 3, rationale: "Revelation and church teaching rejected in favor of reason. Not 4: much of the reasoning is a priori or from innate ideas (Herbert) rather than observation, and moderate deists kept revelation as a natural occurrence.", certainty: 0.7, cites: [{source: S1, locator: "introduction; 'The English Deists'"}, {source: S2, locator: "§2.3"}], how_known: "0–4 scale (P1). Coder's reading, 0.7."}
  E_scope: {value: 3, rationale: "Natural religion is universal: the same truths are inborn in or open to every person, and positive religions are corruptions or partial versions of it (Lessing's three rings: the monotheisms equally true). Some deists still kept a special place for Christianity.", certainty: 0.7, cites: [{source: S1, locator: "'The English Deists'; page 'Deists in other countries'"}], how_known: "0–4 scale (P1). Coder's reading, 0.7."}
epistemology: {value: "Natural light of reason; innate common notions (Herbert); a priori or empirical arguments for God, mostly from design, drawing on Newton's lawful world; biblical criticism against literal revelation.", certainty: 1.0, cites: [{source: S1, locator: "'The English Deists'"}, {source: S2, locator: "§2.3"}], how_known: "Britannica and SEP."}
ethics: {value: "A pious and virtuous life as the best worship; opposition to fanaticism, enthusiasm and cruel images of God; Jesus as a moral teacher ('The ten commandments and the sermon on the mount contain my religion', John Adams).", certainty: 1.0, cites: [{source: S1, locator: "'The English Deists'; page 'Deists in other countries'"}, {source: S2, locator: "§2.3"}], how_known: "Britannica and SEP."}
practice:
  ritual_and_practice: {value: "Little ritual of its own; worship is a virtuous life. Robespierre's Cult of the Supreme Being was a short-lived state form.", certainty: 0.7, cites: [{source: S1, locator: "'The English Deists'"}, {source: S2, locator: "§2.3"}], how_known: "Coder's summary of the sources, 0.7."}
  community_form: {value: "Writers and readers rather than congregations; today some Unitarian Universalist congregations have deist members and discussion groups.", certainty: 0.7, cites: [{source: S1, locator: "page 'Deists in other countries' ('Influence of Deism since the early 20th century')"}], how_known: "Britannica; generalisation is the coder's, 0.7."}
science:
  historical_stance: {value: "Deism was 'fitted to the new discoveries in natural science' (SEP) and drew on Newton's lawful world, though Newton, Locke and Clarke were not deists. Clarke argued against deists that matter cannot ground its own laws and needs continuous dependence on its Creator.", certainty: 1.0, cites: [{source: S2, locator: "§2.3"}, {source: S3, locator: "§4.5"}, {source: S1, locator: "'The English Deists'"}], how_known: "SEP and Britannica."}
  current_stance: {value: "In science and religion today, some deists hold that there is only general divine action, God letting nature run 'like clockwork without further interference'; SEP notes most authors in the field are not deists.", certainty: 1.0, cites: [{source: S5, locator: "§3.1"}], how_known: "SEP Religion and Science."}
schools_and_variants:
  - {name: "English constructive deism (Herbert of Cherbury)", form: "scholastic or philosophical", how_it_differs: "Five innate religious ideas, including worship, repentance and rewards and punishments in the next world.", lio_difference: "C toward 1.", certainty: 1.0, cites: [{source: S1, locator: "'The English Deists'"}]}
  - {name: "Critical English deism (Toland, Collins, Tindal, Woolston)", form: "scholastic or philosophical", how_it_differs: "Attack on mystery, priestcraft and literal scripture, using biblical criticism.", lio_difference: "D at 3–4.", certainty: 1.0, cites: [{source: S1, locator: "'The English Deists'"}, {source: S2, locator: "§2.3"}]}
  - {name: "French philosophe deism (Voltaire)", form: regional, how_it_differs: "Openly claimed the name; the line with atheism was blurred.", lio_difference: "A toward 2 at the atheist edge.", certainty: 1.0, cites: [{source: S1, locator: "page 'Deists in other countries'"}, {source: S2, locator: "§2.3"}]}
  - {name: "German rational religion (Reimarus, Lessing, Mendelssohn)", form: regional, how_it_differs: "Reason alone reaches a perfect religion; Lessing gave positive religions a teaching role; Mendelssohn applied it to Judaism.", lio_difference: "E at 3–4 (the three rings).", certainty: 1.0, cites: [{source: S1, locator: "page 'Deists in other countries'"}]}
  - {name: "American deism (Franklin, Paine, Jefferson, Adams)", form: regional, how_it_differs: "Creeds close to Herbert's; influence on church and state in the new republic. SEP's Jefferson entry argues that calling Jefferson a deist is a misunderstanding.", lio_difference: "Like the code; check each person.", certainty: 0.7, cites: [{source: S1, locator: "page 'Deists in other countries'"}, {source: S2, locator: "§2.3"}, {source: S7, locator: "§2.1"}, {source: S6, locator: "§3"}]}
  - {name: "Stark modern deism (the clockwork God)", form: modern, how_it_differs: "God only set the initial conditions and then left the world to run; this is mainly how theologians and textbooks defined deism.", lio_difference: "B at 4; C and E at 3–4.", certainty: 0.7, cites: [{source: S4, locator: "§2.2"}, {source: S1, locator: "'Nature and scope'"}, {source: S5, locator: "§3.1"}]}
adherents:
  use: "context only — never a genius-rate denominator"
  estimate: {value: TODO, note: "Not a census category. Britannica mentions deist members in some Unitarian Universalist congregations but gives no number; no demographic source was read."}
v7_1_rubric:
  label: "authorial v7.1 scores"
  L: 9
  P: 8
  E: 9
  V: 8
  X: 7
  total: 41
  scoring_note: "Deism achieves a high score for its rational reconciliation of a creator with empirical science, avoiding the pitfalls of interventionist theism, though docked slightly for the unprovable deistic assumption."
  source: "v7.1 data book, section 6 table (tables[4]) row 31 and section 7 scoring notes"
revised_rubric:
  status: "not started"
  L: {score: TODO, rationale: ""}
  P: {score: TODO, rationale: ""}
  E: {score: TODO, rationale: ""}
  V: {score: TODO, rationale: ""}
  X: {score: TODO, rationale: ""}
coding_guidance:
  use_when: "The person's own writing affirms a creator known by reason (usually from design or order) and rejects revelation, miracles and church authority as sources of religious knowledge (S1 introduction; S2 §2.3). Under the v8 test deists usually pass: the deist God is a transcendent person (A low) who does not intervene (B high), so DEISM people are mid-basin theists, not an exclusion (METHOD §1.1; CODING_GUIDE)."
  do_not_use_when: "The person accepts revelation and miracles but is mainly working out natural theology (Newton, Clarke, Locke were not deists per S2 §2.3; Britannica calls the 18th-century deist Newton a transmutation contrary to his writings): CHRIST or CLASS_THEISM. God is identified with the universe: PANDEI or PANT. The line with atheism is blurred (French philosophes): check ATHE. The label deist was often applied by opponents (S1), so do not code from a hostile label."
  neighbors:
    - {code: CLTHEI, relation: "contrast case"}
    - {code: CLASS_THEISM, relation: "neighbor (easily confused)"}
    - {code: CHRIST, relation: "parent tradition"}
    - {code: PANDEI, relation: offshoot}
    - {code: ATHE, relation: "neighbor (easily confused)"}
review:
  data_quality_flags:
    - "The v7.1 note credits deism with avoiding 'the pitfalls of interventionist theism'. Britannica (S1, Nature and scope) says the stark non-interfering view 'was accepted by very few Deists' and was largely a picture drawn by opponents and by 19th–20th-century theologians, and that 'It was possible to believe even in prophetic revelation and still remain a Deist'. Clarke's taxonomy (S3, §4.5) adds a group that 'accept providential action in the world'. The note fits the textbook definition better than the historical deists. v7.1 text left unchanged."
    - "The v7.1 note speaks of reconciling a creator 'with empirical science'. The historical deists' main target was revelation and church authority, and much of their reasoning was a priori (Herbert's innate ideas), though SEP calls deism the religion 'fitted to the new discoveries in natural science' (S2 §2.3). Partly consistent; reported, not changed."
    - "SEP's Jefferson entry (S7) disputes calling Jefferson a deist; S2 lists him among founders sympathetic to deism."
  open_questions:
    - "Newton (first pool) must not be coded DEISM from his reputation: SEP says 'Though not a deist himself' and Britannica calls the 18th-century deist Newton contrary to the spirit of his writings."
    - "Adherents are TODO."
sources:
  - {id: S1, type: tertiary, kind: encyclopedia, author: "David A. Pailin", citation: "Pailin, David A. \"Deism.\" Encyclopaedia Britannica. Online article, main page and page 'Deists in other countries'. https://www.britannica.com/topic/Deism.", url: "https://www.britannica.com/topic/Deism", accessed: 2026-10-01, reliability_note: "Signed reference article. Article paragraphs only; the AI-generated question boxes on Britannica pages were ignored.", used_for: [classification, origins, metaphysics, lio_axes, epistemology, ethics, practice, science, schools_and_variants]}
  - {id: S2, type: tertiary, kind: encyclopedia, author: "William Bristow", year: 2017, citation: "Bristow, William. \"Enlightenment.\" Stanford Encyclopedia of Philosophy. First published August 20, 2010; substantive revision August 29, 2017. https://plato.stanford.edu/entries/enlightenment/.", url: "https://plato.stanford.edu/entries/enlightenment/", accessed: 2026-10-01, reliability_note: "Peer-reviewed reference entry.", used_for: [classification, origins, metaphysics, lio_axes, epistemology, science, schools_and_variants]}
  - {id: S3, type: tertiary, kind: encyclopedia, author: "Timothy Yenter; Ezio Vailati", year: 2024, citation: "Yenter, Timothy, and Ezio Vailati. \"Samuel Clarke.\" Stanford Encyclopedia of Philosophy. First published April 5, 2003; substantive revision July 29, 2024. https://plato.stanford.edu/entries/clarke/.", url: "https://plato.stanford.edu/entries/clarke/", accessed: 2026-10-01, reliability_note: "Peer-reviewed reference entry. Clarke was an opponent of deism; his four categories are a hostile but detailed taxonomy.", used_for: [metaphysics, lio_axes, science]}
  - {id: S4, type: tertiary, kind: encyclopedia, author: "Jeanine Diller", year: 2021, citation: "Diller, Jeanine. \"God and Other Ultimates.\" Stanford Encyclopedia of Philosophy. First published December 17, 2021. https://plato.stanford.edu/entries/god-ultimates/.", url: "https://plato.stanford.edu/entries/god-ultimates/", accessed: 2026-10-01, reliability_note: "Peer-reviewed reference entry.", used_for: [classification, metaphysics, lio_axes, schools_and_variants]}
  - {id: S5, type: tertiary, kind: encyclopedia, author: "Helen De Cruz", year: 2022, citation: "De Cruz, Helen. \"Religion and Science.\" Stanford Encyclopedia of Philosophy. First published January 17, 2017; substantive revision September 3, 2022. https://plato.stanford.edu/entries/religion-science/.", url: "https://plato.stanford.edu/entries/religion-science/", accessed: 2026-10-01, reliability_note: "Peer-reviewed reference entry.", used_for: [lio_axes, science, schools_and_variants]}
  - {id: S6, type: tertiary, kind: encyclopedia, author: "Mark Philp", year: 2025, citation: "Philp, Mark. \"Thomas Paine.\" Stanford Encyclopedia of Philosophy. First published July 18, 2013; substantive revision August 27, 2025. https://plato.stanford.edu/entries/paine/.", url: "https://plato.stanford.edu/entries/paine/", accessed: 2026-10-01, reliability_note: "Peer-reviewed reference entry.", used_for: [origins, schools_and_variants]}
  - {id: S7, type: tertiary, kind: encyclopedia, author: "M. Andrew Holowchak", year: 2025, citation: "Holowchak, M. Andrew. \"Thomas Jefferson.\" Stanford Encyclopedia of Philosophy. First published November 17, 2015; substantive revision March 28, 2025. https://plato.stanford.edu/entries/jefferson/.", url: "https://plato.stanford.edu/entries/jefferson/", accessed: 2026-10-01, reliability_note: "Peer-reviewed reference entry; argues against the deist reading of Jefferson.", used_for: [metaphysics, schools_and_variants, review]}
  - {id: S8, type: tertiary, kind: encyclopedia, author: "William Uzgalis", year: 2025, citation: "Uzgalis, William. \"Anthony Collins.\" Stanford Encyclopedia of Philosophy. First published August 25, 2003; substantive revision September 4, 2025. https://plato.stanford.edu/entries/collins/.", url: "https://plato.stanford.edu/entries/collins/", accessed: 2026-10-01, reliability_note: "Peer-reviewed reference entry.", used_for: [metaphysics]}
---

# Deism (DEISM)

> Status: draft — unreviewed. Filled from Stanford Encyclopedia of Philosophy entries and the signed Britannica article. LIO axes use the 0–4 scale (P1). The v7.1 scores and note are unchanged. Adherents are TODO.

## Summary

Deism is the natural religion of a group of English writers from Herbert of Cherbury (early 17th century) to Bolingbroke (mid 18th century). It then spread to France, Germany and America [S1, introduction]. Britannica defines it as "the acceptance of a certain body of religious knowledge that is inborn in every person or that can be acquired by the use of reason", together with the rejection of knowledge from revelation or church teaching [S1, introduction]. SEP calls it "the form of religion most associated with the Enlightenment" [S2, §2.3]. Under the v8 test, deists usually pass: the deist God is a transcendent person who does not intervene (METHOD §1.1).

## Core metaphysics

SEP: "we can know by the natural light of reason that the universe is created and governed by a supreme intelligence", and that being "does not interfere with creation" [S2, §2.3]. Deists typically reject miracles and special revelation, and treat Jesus as a moral teacher [S2, §2.3]. Britannica adds an important warning. The textbook picture, God withdrawing after creation, "was accepted by very few Deists during the flowering of the doctrine", and opponents often pushed them into it [S1, Nature and scope]. Deists also disagreed with each other. Samuel Clarke, an opponent, sorted them into four categories [S3, §4.5]: some denied providence, some denied God moral attributes, some denied a future state, and some held orthodox doctrine but based it only on reason. Herbert's five innate ideas include "rewards and punishments in the next world" [S1, The English Deists].

## Position on the LIO axes

Scored on the 0–4 scale (P1):

- A locus 1 (0.7): a transcendent creator, thinly personal [S2, §2.3; S4, §2.2].
- B cause 3 (0.7): typically no intervention and no miracles; the stark form would be 4 [S2, §2.3; S1].
- C ledger 2 (0.5): some keep future rewards and punishments, others deny a future state [S1; S3, §4.5].
- D authority 3 (0.7): reason against revelation, much of it a priori [S1, introduction].
- E scope 3 (0.7): universal natural religion [S1].

## Schools and variants

English deism had a constructive side (Herbert's common notions) and a critical side: Toland, Collins, Tindal and Woolston attacked mystery, priestcraft and literal scripture [S1, The English Deists; S2, §2.3]. Voltaire carried deism to France, where the line with atheism was "often rather blurred" [S1, Deists in other countries]. Reimarus and Lessing developed a German rational religion, and Mendelssohn applied it to Judaism [S1]. In America, Franklin's creed "almost literally reproduced Herbert's five fundamental beliefs" [S1, Deists in other countries]. SEP's Jefferson entry argues that calling Jefferson a deist is a misunderstanding [S7, §2.1]. The stark clockwork version is what SEP describes as "the idea that God set the initial conditions of the universe and then left it to play out on its own" [S4, §2.2].

## Science

SEP calls deism "the form of religion fitted to the new discoveries in natural science" [S2, §2.3]. Newton gave it fuel with the design argument in the Opticks, "Though not a deist himself" [S2, §2.3]. Britannica says the 18th-century tendency to turn Newton into a deist was "contrary to the spirit of both his philosophical and his theological writings" [S1, The English Deists]. In current science and religion, some deists hold that God lets nature "run like clockwork without further interference", but most authors in the field are not deists [S5, §3.1].

## Coding guidance

Use DEISM when the person's own writing affirms a creator known by reason and rejects revelation, miracles and church authority. Such people usually pass the v8 test (METHOD §1.1). Do not code from the label alone: opponents applied it freely [S1]. Newton, Locke and Clarke were not deists [S2, §2.3]. If God is identified with the universe, use PANDEI or PANT. If the person is a French philosophe, check ATHE.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> DEISM (41/50) — Deism. Deism achieves a high score for its rational reconciliation of a creator with empirical science, avoiding the pitfalls of interventionist theism, though docked slightly for the unprovable deistic assumption.

## Open questions

- The v7.1 note assumes the stark non-interventionist deism that Britannica says few deists held (see review).
- Newton's person file must not take DEISM from his reputation.
- Adherents are TODO.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-01 (overnight run): read Britannica "Deism" (D. A. Pailin; two pages) and SEP "Enlightenment", "Samuel Clarke", "God and Other Ultimates", "Religion and Science", "Thomas Paine", "Thomas Jefferson" and "Anthony Collins". SEP has no general Deism entry and IEP's deism page returned 404. AI-generated question boxes on Britannica pages were not used. All quotations were checked word for word against the fetched page text with a script.
