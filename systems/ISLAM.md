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
    - {date: 2026-10-01, by: "Grok Bot", summary: "Draft: classification, origins, metaphysics, LIO axes (0–4, P1), science, schools, adherents and coding guidance filled from six SEP entries, the multi-author Britannica article and a Pew Research Center report. v7.1 scores and note unchanged. Not reviewed."}
identity:
  id: ISLAM
  v7_1_number: 69
  v7_1_label: "Islam"
  display_label: "Islam"
  label_status: "as in v7.1"
  aliases: ["the Islamic tradition"]
classification:
  kind: {value: religion, certainty: 1.0, cites: [{source: S1, locator: "introduction"}], how_known: "Britannica: 'major world religion promulgated by the Prophet Muhammad in Arabia in the 7th century'."}
  family: {value: "Abrahamic monotheism", certainty: 1.0, cites: [{source: S2, locator: "§2.2"}, {source: S1, locator: "page 'Doctrines of the Qurʾān'"}], how_known: "SEP calls Islam a monotheistic religion; Britannica says its picture of God is related to the concept of God shared by Judaism and Christianity."}
  parent_traditions: {value: ["the prophetic line the Qurʾān recognises (Adam, Noah, Abraham, Moses, Jesus), shared with Judaism and Christianity"], certainty: 0.7, cites: [{source: S1, locator: "introduction; page 'Doctrines of the Qurʾān'"}], how_known: "Britannica: Muhammad is considered the last of a series of prophets and his message completes earlier revelations. Islam does not see itself as an offshoot, so the parent label is the coder's, 0.7."}
  related_codes:
    - {code: CLASS_THEISM, relation: "neighbor (easily confused)", note: "v7.1 coding rule (Split theisms): falsafa (Avicenna, Averroes) is CLASS_THEISM, not generic ISLAM"}
    - {code: CLTHEI, relation: "neighbor (easily confused)", note: "v7.1 coding rule (Split theisms)"}
    - {code: JUDA, relation: overlaps, note: "shared prophets and concept of God (Britannica)"}
    - {code: CHRIST, relation: overlaps, note: "shared prophets including Jesus; the Trinity is rejected (Britannica)"}
origins:
  founding_era: {value: "7th century CE (Muhammad's migration to Medina in 622; his death in 632)", certainty: 1.0, cites: [{source: S1, locator: "introduction; 'The legacy of Muhammad'"}, {source: S2, locator: "§2.2"}], how_known: "Stated in both sources."}
  founding_region: {value: "Arabia (Mecca and Medina)", certainty: 1.0, cites: [{source: S1, locator: "introduction; 'The legacy of Muhammad'"}], how_known: "Britannica."}
  founders_or_key_figures: {value: ["Muhammad (the Prophet)", "ʿAlī ibn Abī Ṭālib (fourth caliph; the Prophet's designated successor in Shiʿi belief)", "Aḥmad ibn Ḥanbal (d. 855)", "ʿAbd al-Jabbār (935–1025, Muʿtazilite)", "al-Ashʿarī (874–936) and al-Māturīdī (Sunni theology)", "al-Kindī, Avicenna (980–1037), Averroes (1126–1198) (falsafa)", "al-Ghazālī (11th–12th century)", "Ibn ʿArabī and al-Suhrawardī (mysticism and illumination)", "al-Afghānī, Muḥammad ʿAbduh, Muḥammad Iqbāl (modern reform)"], certainty: 1.0, cites: [{source: S1, locator: "introduction; pages 'Theology and sectarianism', 'Sunnism', 'Islamic philosophy', 'Critiques of Aristotle in Islamic theology', 'Impact of modernism'"}, {source: S3, locator: "§1.1; §1.2"}, {source: S2, locator: "§2.2"}], how_known: "All named in these roles in the sources. After Muhammad the list is a selection, not a ranking."}
  key_texts:
    - {value: "Qurʾān", author: "revealed to Muhammad (Muslim belief)", year: "7th century CE", certainty: 1.0, cites: [{source: S1, locator: "introduction"}, {source: S2, locator: "§2.2"}], how_known: "Both sources: the central religious text."}
    - {value: "Ḥadīth (sayings, actions and tacit approvals of the Prophet)", author: "transmitted corpus", year: "collected over the first Islamic centuries", certainty: 0.7, cites: [{source: S2, locator: "§2.2"}], how_known: "SEP calls it an important source of jurisprudence and theology. The dating phrase is the coder's, so 0.7."}
    - {value: "The Incoherence of the Philosophers (Tahāfut al-falāsifa)", author: "al-Ghazālī", year: "11th century", certainty: 1.0, cites: [{source: S2, locator: "§2.2"}, {source: S4, locator: "§3"}], how_known: "SEP: an influential critique of Greek-inspired Muslim philosophy."}
metaphysics:
  god_nature_relation: {value: "God is one and unique, the sole creator and sustainer, who brought creation into being by the command Be; his presence is everywhere but he is not incarnated in anything. Some Sufi thinkers read God and world more closely (the Oneness of Being associated with Ibn ʿArabī).", stance: "creator distinct from creation", certainty: 1.0, cites: [{source: S1, locator: "page 'Doctrines of the Qurʾān'"}, {source: S6, locator: "§3.1"}], how_known: "Britannica states the Qurʾānic doctrine directly."}
  deity_personal: {value: "Personal: powerful, just, merciful and provident; God's role toward humans is that of the commander. The schools argued about God's attributes (the Muʿtazilah held God to be pure Essence without eternal attributes).", stance: personal, certainty: 1.0, cites: [{source: S1, locator: "pages 'Doctrines of the Qurʾān', 'Eschatology', 'Theology and sectarianism'"}], how_known: "Britannica."}
  intervention: {value: "Classical theologians held that God creates the world of atoms and accidents and recreates it at every moment, as the immediate cause of every change. Ashʿarites limited agency to God alone (occasionalism); Muʿtazilites made an exception for human action; the falāsifa (Avicenna, Averroes) held to causal necessity in nature. The Qurʾān itself stresses that there are no gaps or dislocations in nature.", stance: "varies by school", certainty: 1.0, cites: [{source: S3, locator: "§1.1; §1.2; §3.3"}, {source: S1, locator: "page 'Doctrines of the Qurʾān'"}], how_known: "SEP and Britannica state the positions directly."}
  miracles: {value: "Affirmed. Al-Ghazālī attacked the philosophers' causal necessity to safeguard belief in miracles and divine omnipotence, and also argued that miracles are compatible with bodily natures (God can speed up natural changes).", stance: affirmed, certainty: 1.0, cites: [{source: S3, locator: "§3.3.4; §4.3"}], how_known: "SEP."}
  petition_and_prayer: {value: "Ritual prayer (ṣalāt) five times a day is a pillar of Islam and cannot be waived even for the sick; individual devotional prayers are not obligatory but are common among the pious. SEP lists Islam among the monotheisms whose petitionary prayer raises the classic puzzles. The sources read do not describe personal petition in detail.", stance: "petition answered", certainty: 0.5, cites: [{source: S8, locator: "introduction"}, {source: S1, locator: "page 'Prayer'"}, {source: S7, locator: "introduction"}], how_known: "Ritual prayer is stated directly; that petition is answered is a coder's reading from SEP's grouping, so 0.5."}
  afterlife: {value: "Personal: on the Last Day the dead are resurrected and judged; the condemned burn in hellfire and the saved enjoy paradise, which are both spiritual and corporeal. Al-Ghazālī counted the denial of bodily return (an Avicennan teaching) as unbelief.", stance: "personal afterlife", certainty: 1.0, cites: [{source: S1, locator: "page 'Eschatology'"}, {source: S4, locator: "§3"}], how_known: "Britannica and SEP."}
  moral_ledger: {value: "A judgment 'on every person in accordance with his deeds'; spending for others is described as a credit with God. Most schools accept intercession, and God in his mercy may forgive certain sinners. Muʿtazilites tied the justice of reward and punishment to human agency.", stance: "personal reward and punishment", certainty: 1.0, cites: [{source: S1, locator: "page 'Eschatology'"}, {source: S3, locator: "§1.1"}], how_known: "Stated directly."}
  authority: {value: "Revelation: the Qurʾān, with the ḥadīth as a source of law and theology; Sunnis add the consensus of the community, Shiʿis the infallible imam. On reason the schools split: Muʿtazilites and Shiʿis hold that reason can know good and evil; al-Ashʿarī held that it cannot and that acts are good or evil by God's declaring them so. Averroes held there can be no conflict between God's word and God's work, properly understood.", stance: "both, revelation first", certainty: 0.7, cites: [{source: S2, locator: "§2.2"}, {source: S1, locator: "pages 'Sunnism', 'Shiism'"}], how_known: "Sources state the positions; the single stance is the coder's reading of the mainstream, so 0.7."}
  reserved_exemptions: {value: "Central: revelation to the prophets, miracles, and bodily resurrection are articles of faith; al-Ghazālī treated challenges to monotheism, the prophecy of Muhammad and resurrection after death as apostasy.", stance: central, certainty: 0.7, cites: [{source: S2, locator: "§2.2"}, {source: S3, locator: "§3.3.4"}], how_known: "Coder's reading of what the core doctrines commit to, so 0.7."}
  teleology_in_nature: {value: "The Qurʾān stresses design and order to prove God's unity: every created thing has a definite nature and its own laws of behaviour, endowed by God; nothing was made without a purpose, and humans are God's vice-regents.", stance: "designer's purposes", certainty: 1.0, cites: [{source: S1, locator: "page 'Doctrines of the Qurʾān'"}], how_known: "Britannica."}
  necessity_and_freedom: {value: "A central dispute. Muʿtazilites gave humans power over their own acts, on grounds of divine justice; al-Ashʿarī taught that God creates human acts and humans acquire them; al-Māturīdī held that a human is a real actor though God creates everything; Sunni orthodoxy sought a synthesis of responsibility and omnipotence; Shiʿism adopted the Muʿtazilite view of free will.", certainty: 1.0, cites: [{source: S1, locator: "pages 'Sunnism', 'Shiism'"}, {source: S3, locator: "§1.1; §1.2"}], how_known: "Stated directly."}
lio_axes:
  A_locus: {value: 0, rationale: "One transcendent, personal creator, not incarnated in anything, who commands and judges. Sufi and philosophical strands (Ibn ʿArabī's school; the falāsifa) move away from the pole.", certainty: 0.7, cites: [{source: S1, locator: "page 'Doctrines of the Qurʾān'"}, {source: S6, locator: "§3.1"}], how_known: "Scored on the 0–4 scale (P1). 0.7 for the mystical and philosophical wings."}
  B_cause: {value: 1, rationale: "Nature has fixed, God-given patterns with no gaps, but the dominant Ashʿarite theology makes God the immediate cause of every change (occasionalism) and defends miracles; falsafa holds causal necessity. Spread from 0 to 3.", certainty: 0.5, cites: [{source: S1, locator: "page 'Doctrines of the Qurʾān'"}, {source: S3, locator: "§1.2; §3.3"}], how_known: "0–4 scale (P1). 0.5 because the schools are far apart; where occasionalism counts on this axis is itself a judgement call."}
  C_ledger: {value: 0, rationale: "Every person is judged by their deeds and rewarded or punished in a bodily and spiritual afterlife; mercy and intercession qualify it but do not remove the ledger.", certainty: 0.7, cites: [{source: S1, locator: "page 'Eschatology'"}], how_known: "0–4 scale (P1). 0.7: stated directly, but falsafa and some Sufis read it differently."}
  D_authority: {value: 1, rationale: "Revelation and prophetic tradition first; rational theology (kalām) and philosophy work within it. Ashʿarites deny that reason alone finds good and evil (toward 0); Muʿtazilites and Averroes give reason more room (toward 2). Matches the v7.1 note's 'reliance on revelation'.", certainty: 0.5, cites: [{source: S1, locator: "pages 'Sunnism', 'Shiism'"}, {source: S2, locator: "§2.2"}], how_known: "0–4 scale (P1). 0.5 for the spread."}
  E_scope: {value: 1, rationale: "God's will governs all creation, but revelation, prophecy and community are particular: Muslims are the best community, and Jews and Christians had a special status as people of the Book. Judgment is for every individual.", certainty: 0.5, cites: [{source: S1, locator: "introduction; page 'Eschatology'"}], how_known: "0–4 scale (P1). Coder's reading, so 0.5."}
epistemology: {value: "Revealed knowledge (Qurʾān, ḥadīth) alongside the human knowledge of the ancients, which al-Kindī began to reconcile through rational and metaphorical exegesis. Kalām argues rationally inside revealed premises; falsafa follows Greek demonstration; mystics claim a higher knowledge in experience; Shiʿism holds that sure knowledge comes only through the infallible imam.", certainty: 1.0, cites: [{source: S1, locator: "pages 'Islamic philosophy', 'Shiism', 'Critiques of Aristotle in Islamic theology'"}, {source: S5, locator: "introduction"}], how_known: "Britannica and SEP."}
ethics: {value: "Submission to the divine will; moral struggle against pride and narrowness; social service to the needy as part of religion; equality of believers before God, with distinction only by piety and good acts.", certainty: 1.0, cites: [{source: S1, locator: "pages 'Doctrines of the Qurʾān', 'Eschatology' (sections 'Social service')"}], how_known: "Britannica."}
practice:
  ritual_and_practice: {value: "The five Pillars, including five daily ritual prayers with ablution, congregational Friday prayer, the fast of Ramadan and the hajj.", certainty: 1.0, cites: [{source: S8, locator: "introduction"}, {source: S1, locator: "page 'Prayer'"}], how_known: "Britannica."}
  community_form: {value: "One community of the faithful (umma) bound by a common faith, with sects and law schools; Sunnis are the majority, Shiʿis the main other branch; Sufi orders spread Islam widely after the 12th century.", certainty: 1.0, cites: [{source: S1, locator: "introduction; pages 'Theology and sectarianism', 'Shiism'"}], how_known: "Britannica."}
science:
  historical_stance: {value: "Between about the ninth and fifteenth centuries the Islamic world far exceeded Europe in mathematics, astronomy, optics and medicine, with Abbasid patronage and the House of Wisdom translating Greek, Persian and Indian works. Liberal authors blame later decline on conservative theology after al-Ghazālī; SEP says that narrative has problems and points instead to law (fiqh) and to apostasy rules from the eleventh century.", certainty: 1.0, cites: [{source: S2, locator: "§2.2"}], how_known: "SEP Religion and Science."}
  current_stance: {value: "Mixed. Old Earth creationism is more influential than Young Earth creationism, and most Muslims reject human evolution because of the special creation of Adam; Muslim scientists such as Nidhal Guessoum and Rana Dajani accept evolution, and Guessoum follows Averroes's no-possible-conflict principle.", certainty: 1.0, cites: [{source: S2, locator: "§2.2"}], how_known: "SEP Religion and Science."}
schools_and_variants:
  - {name: "Sunni Islam (Ashʿarite and Māturīdite theology; four law schools)", form: "scholastic or philosophical", how_it_differs: "Majority branch; follows the consensus of the community; Ashʿarites hold occasionalism and that God's command makes acts good or evil.", lio_difference: "B toward 0 in Ashʿarite occasionalism; D toward 0.", certainty: 1.0, cites: [{source: S1, locator: "page 'Sunnism'"}, {source: S3, locator: "§1.2"}]}
  - {name: "Shiʿi Islam (Twelvers and others)", form: other, how_it_differs: "Leadership through ʿAlī's line; the infallible imam as source of true knowledge; adopted Muʿtazilite free will and reason's capacity to know good and evil.", lio_difference: "D: authority runs through the imam; reason given more room than in Ashʿarism.", certainty: 1.0, cites: [{source: S1, locator: "page 'Shiism'"}]}
  - {name: "Muʿtazilite theology", form: "scholastic or philosophical", how_it_differs: "God's unity and justice; humans cause their own acts; God without eternal attributes; once the state creed under al-Maʾmūn, later eclipsed.", lio_difference: "B and D up by about one step.", certainty: 1.0, cites: [{source: S1, locator: "page 'Theology and sectarianism'"}, {source: S3, locator: "§1.1"}, {source: S2, locator: "§2.2"}]}
  - {name: "Falsafa (al-Kindī, al-Fārābī, Avicenna, Averroes)", form: "scholastic or philosophical", how_it_differs: "Greek-inspired philosophy; causal necessity in nature; al-Ghazālī judged three Avicennan teachings (eternal world, God's knowledge of universals only, no bodily return) to be unbelief.", lio_difference: "B and D at 2–3; code CLASS_THEISM when the person's own writing is in this line.", certainty: 1.0, cites: [{source: S4, locator: "§3"}, {source: S3, locator: "§2; §3"}]}
  - {name: "Sufism and philosophical mysticism (Ibn ʿArabī, al-Suhrawardī, Mullā Ṣadrā)", form: mystical, how_it_differs: "The esoteric dimension of Islam; knowledge by experience; the Oneness of Being associated with Ibn ʿArabī, illumination in al-Suhrawardī.", lio_difference: "A toward 1–2.", certainty: 0.7, cites: [{source: S5, locator: "introduction"}, {source: S6, locator: "§3.1"}, {source: S1, locator: "page 'Critiques of Aristotle in Islamic theology'"}]}
  - {name: "Modern reform (al-Afghānī, ʿAbduh, Iqbāl) and science-and-religion writers", form: reform, how_it_differs: "Rebelled against the late medieval synthesis and called for reform; some current Muslim scientists argue science and religion are in harmony.", lio_difference: "D toward 2 in the science-friendly wing.", certainty: 0.7, cites: [{source: S1, locator: "page 'Impact of modernism'"}, {source: S2, locator: "§2.2"}]}
adherents:
  use: "context only — never a genius-rate denominator"
  estimate: {value: "25.6% of the world population; up 347 million from 2010", year: 2020, scope: world, certainty: 0.7, cites: [{source: S9, locator: "key findings"}], how_known: "Pew Research Center demographic estimate. Self-identification based and differs by source, so 0.7.", alternatives: [{value: "more than 1.5 billion (early 21st century)", cites: [{source: S1, locator: "introduction"}]}]}
v7_1_rubric:
  label: "authorial v7.1 scores"
  L: 7
  P: 6
  E: 4
  V: 3
  X: 2
  total: 22
  scoring_note: "Islam provides a comprehensive monotheistic framework emphasizing submission and ethics, but its reliance on revelation over empirical evidence limits its alignment with scientific metrics."
  source: "v7.1 data book, section 6 table (tables[4]) row 69 and section 7 scoring notes"
revised_rubric:
  status: "not started"
  L: {score: TODO, rationale: ""}
  P: {score: TODO, rationale: ""}
  E: {score: TODO, rationale: ""}
  V: {score: TODO, rationale: ""}
  X: {score: TODO, rationale: ""}
coding_guidance:
  use_when: "v7.1 coding rule (Split theisms): CLASS_THEISM (Aristotelian-Thomistic-Falsafa) is not CLTHEI (popular interventionist personal God) and not generic CHRIST/ISLAM/JUDA. v8 note: use ISLAM when the person's own writing shows Muslim belief (God's unity, the Qurʾān, the Prophet, the last judgment) without a more specific philosophical position. Kalām theologians (Ashʿarite, Māturīdite, Muʿtazilite) stay under ISLAM; record the school in the person file."
  do_not_use_when: "The person's own writing is falsafa: a necessary first cause, causal necessity in nature, demonstration first (Avicenna, Averroes): CLASS_THEISM. Popular interventionism beyond what the confession teaches: consider CLTHEI. Mainly Sufi metaphysics of the Oneness of Being: still ISLAM by default, but check PANT/PANENT neighbours and note it. Birth into a Muslim society alone: no code."
  neighbors:
    - {code: CLASS_THEISM, relation: "neighbor (easily confused)"}
    - {code: CLTHEI, relation: "neighbor (easily confused)"}
    - {code: JUDA, relation: overlaps}
    - {code: CHRIST, relation: overlaps}
review:
  data_quality_flags:
    - "The v7.1 note cites 'reliance on revelation over empirical evidence'. SEP (S2 §2.2) records that the Islamic world led European science from about the ninth to the fifteenth century, and that the usual story blaming theology for the later decline has problems. This does not contradict D_authority 1 but gives a fuller picture of the science record. v7.1 text left unchanged."
    - "Britannica's adherent figure (more than 1.5 billion) is older than Pew's 2020 estimate; Pew is used."
  open_questions:
    - "Ibn Sina (first pool): the v7.1 split puts falsafa under CLASS_THEISM, and al-Ghazālī judged three of Avicenna's teachings to be unbelief (S4 §3). His person file should code from his writings, which most likely means CLASS_THEISM rather than ISLAM."
    - "How Ashʿarite occasionalism should score on B_cause is unclear: every event is God's act, yet nature is regular by God's custom. Scored 1 with 0.5 certainty."
sources:
  - {id: S1, type: tertiary, kind: encyclopedia, author: "Fazlur Rahman, Muhsin S. Mahdi, Annemarie Schimmel and others (multi-author article)", citation: "\"Islam.\" Encyclopaedia Britannica. Online article, main page and subpages 'Doctrines of the Qurʾān', 'Eschatology: doctrine of last things', 'Prayer', 'Theology and sectarianism', 'Sunnism', 'Shiism', 'Islamic thought', 'Islamic philosophy', 'Critiques of Aristotle in Islamic theology', 'Impact of modernism'. https://www.britannica.com/topic/Islam.", url: "https://www.britannica.com/topic/Islam", accessed: 2026-10-01, reliability_note: "Signed reference article. Article paragraphs only; the AI-generated question boxes on Britannica pages were ignored. Some sections are older (adherent figure of 1.5 billion).", used_for: [classification, origins, metaphysics, lio_axes, epistemology, ethics, practice, schools_and_variants]}
  - {id: S2, type: tertiary, kind: encyclopedia, author: "Helen De Cruz", year: 2022, citation: "De Cruz, Helen. \"Religion and Science.\" Stanford Encyclopedia of Philosophy. First published January 17, 2017; substantive revision September 3, 2022. https://plato.stanford.edu/entries/religion-science/.", url: "https://plato.stanford.edu/entries/religion-science/", accessed: 2026-10-01, reliability_note: "Peer-reviewed reference entry.", used_for: [classification, origins, metaphysics, lio_axes, science, schools_and_variants]}
  - {id: S3, type: tertiary, kind: encyclopedia, author: "Kara Richardson", year: 2025, citation: "Richardson, Kara. \"Causation in Arabic and Islamic Thought.\" Stanford Encyclopedia of Philosophy. First published October 26, 2015; substantive revision August 15, 2025. https://plato.stanford.edu/entries/arabic-islamic-causation/.", url: "https://plato.stanford.edu/entries/arabic-islamic-causation/", accessed: 2026-10-01, reliability_note: "Peer-reviewed reference entry.", used_for: [metaphysics, lio_axes, schools_and_variants]}
  - {id: S4, type: tertiary, kind: encyclopedia, author: "Frank Griffel", year: 2026, citation: "Griffel, Frank. \"Al-Ghazali.\" Stanford Encyclopedia of Philosophy. First published August 14, 2007; substantive revision January 15, 2026. https://plato.stanford.edu/entries/al-ghazali/.", url: "https://plato.stanford.edu/entries/al-ghazali/", accessed: 2026-10-01, reliability_note: "Peer-reviewed reference entry.", used_for: [origins, metaphysics, schools_and_variants, review]}
  - {id: S5, type: tertiary, kind: encyclopedia, author: "Mehdi Aminrazavi", year: 2021, citation: "Aminrazavi, Mehdi. \"Mysticism in Arabic and Islamic Philosophy.\" Stanford Encyclopedia of Philosophy. First published March 7, 2009; substantive revision January 19, 2021. https://plato.stanford.edu/entries/arabic-islamic-mysticism/.", url: "https://plato.stanford.edu/entries/arabic-islamic-mysticism/", accessed: 2026-10-01, reliability_note: "Peer-reviewed reference entry.", used_for: [epistemology, schools_and_variants]}
  - {id: S6, type: tertiary, kind: encyclopedia, author: "William Chittick", year: 2025, citation: "Chittick, William. \"Ibn Arabi.\" Stanford Encyclopedia of Philosophy. First published August 5, 2008; substantive revision December 5, 2025. https://plato.stanford.edu/entries/ibn-arabi/.", url: "https://plato.stanford.edu/entries/ibn-arabi/", accessed: 2026-10-01, reliability_note: "Peer-reviewed reference entry. Chittick notes that calling Ibn ʿArabī the founder of the Oneness of Being doctrine is misleading.", used_for: [metaphysics, lio_axes, schools_and_variants]}
  - {id: S7, type: tertiary, kind: encyclopedia, author: "Scott A. Davison", year: 2026, citation: "Davison, Scott A. \"Petitionary Prayer.\" Stanford Encyclopedia of Philosophy. First published August 15, 2012; substantive revision May 18, 2026. https://plato.stanford.edu/entries/petitionary-prayer/.", url: "https://plato.stanford.edu/entries/petitionary-prayer/", accessed: 2026-10-01, reliability_note: "Peer-reviewed reference entry.", used_for: [metaphysics]}
  - {id: S8, type: tertiary, kind: encyclopedia, author: "Britannica Editors", citation: "\"Salat.\" Encyclopaedia Britannica. https://www.britannica.com/topic/salat.", url: "https://www.britannica.com/topic/salat", accessed: 2026-10-01, reliability_note: "Editor-written reference article; article paragraphs only.", used_for: [metaphysics, practice]}
  - {id: S9, type: secondary, kind: "institutional page", author: "Pew Research Center", year: 2025, citation: "Pew Research Center. \"How the Global Religious Landscape Changed From 2010 to 2020.\" June 9, 2025. https://www.pewresearch.org/religion/2025/06/09/how-the-global-religious-landscape-changed-from-2010-to-2020/.", url: "https://www.pewresearch.org/religion/2025/06/09/how-the-global-religious-landscape-changed-from-2010-to-2020/", accessed: 2026-10-01, reliability_note: "Demographic estimates from censuses and surveys; context only.", used_for: [adherents]}
---

# Islam (ISLAM)

> Status: draft — unreviewed. Filled from Stanford Encyclopedia of Philosophy entries, the multi-author Britannica article and a Pew Research Center report. LIO axes use the 0–4 scale (P1). The v7.1 scores and note are unchanged.

## Summary

Islam is the religion taught by the Prophet Muhammad in Arabia in the 7th century CE [S1, introduction]. Its center is the belief in one God who reveals his will through prophets, ending with Muhammad, and through the Qurʾān [S2, §2.2]. The two main branches, Sunni and Shiʿi, go back to a dispute over who should lead after Muhammad [S2, §2.2; S1, Theology and sectarianism]. This record covers the confessed religion as a whole. Under the v7.1 rule, falsafa (Avicenna, Averroes) is coded CLASS_THEISM.

## Core metaphysics

The Qurʾān's doctrine of God is "rigorously monotheistic": God has no partner, and the Trinity is rejected [S1, Doctrines of the Qurʾān]. God is creator and sustainer and is "not incarnated in anything" [S1, Doctrines of the Qurʾān]. Nature has a fixed order: "There are no gaps or dislocations in nature" [S1, Doctrines of the Qurʾān]. The theologians explained that order in different ways. Many classical theologians held that God recreates the world at every moment and "identified God as the immediate cause of every change in the created world" [S3, §1.1]. Ashʿarites "seem to endorse occasionalism, the view that God is the only true cause" [S3, §1.2]. On the Last Day the dead are raised and judged "in accordance with his deeds", and paradise and hell are both spiritual and corporeal [S1, Eschatology].

## Position on the LIO axes

Scored on the 0–4 scale (P1), for the code as v7.1 defines it (the confessed religion as a whole):

- A locus 0 (0.7): one transcendent, personal creator, not incarnate [S1]. Sufi and philosophical wings move up.
- B cause 1 (0.5): a lawful created order, but Ashʿarite occasionalism and miracles; falsafa holds necessity [S1; S3, §1.2; §3.3].
- C ledger 0 (0.7): judgment by deeds, bodily and spiritual reward and punishment [S1, Eschatology].
- D authority 1 (0.5): revelation first; schools differ on what reason can know [S1, Sunnism; Shiism].
- E scope 1 (0.5): universal divine will with a particular revelation and community [S1].

## Schools and variants

Sunni theology took shape in the 10th century in reaction to the Muʿtazilah, with al-Ashʿarī and al-Māturīdī as its main figures [S1, Sunnism]. Shiʿism holds that true knowledge comes through the infallible imam and adopted the Muʿtazilite view of free will [S1, Shiism]. The Muʿtazilites stressed God's justice and gave humans the power to produce their own actions [S3, §1.1]. The falāsifa followed Greek philosophy; al-Ghazālī judged three of Avicenna's teachings to be unbelief [S4, §3]. Sufism "represents the esoteric dimension of Islam" [S5, introduction]. Modern reformers such as al-Afghānī, ʿAbduh and Iqbāl called for radical reform [S1, Impact of modernism].

## Science

SEP says the Islamic world "far exceeded European cultures in the range and quality of its scientific knowledge between approximately the ninth and the fifteenth century" [S2, §2.2]. It describes the view that conservative theology after al-Ghazālī caused the later decline and then says "The problem with this narrative" is that orthodox worries came before and after him, and that law (fiqh) did more to stifle science [S2, §2.2]. Today Old Earth creationism is more influential than Young Earth creationism. Most Muslims reject human evolution, while scientists such as Guessoum and Dajani accept it [S2, §2.2].

## Coding guidance

Use ISLAM when the person's own writing shows Muslim belief without a more specific philosophical position. Kalām theologians stay under ISLAM, with the school recorded. Use CLASS_THEISM for falsafa in the person's own writing (necessary first cause, causal necessity in nature). Consider CLTHEI only for interventionism beyond the confession. Being born into a Muslim society gives no code.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> ISLAM (22/50) — Islam. Islam provides a comprehensive monotheistic framework emphasizing submission and ethics, but its reliance on revelation over empirical evidence limits its alignment with scientific metrics.

## Open questions

- Ibn Sina: CLASS_THEISM or ISLAM. His person file decides, from his writings (see review).
- Where occasionalism belongs on B_cause.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-01 (overnight run): read SEP "Religion and Science", "Causation in Arabic and Islamic Thought", "Al-Ghazali", "Mysticism in Arabic and Islamic Philosophy", "Ibn Arabi" and "Petitionary Prayer"; Britannica "Islam" (main page and ten subpages, multi-author) and "Salat"; Pew Research Center's 2025 report. AI-generated question boxes on Britannica pages were not used. All quotations were checked word for word against the fetched page text with a script. Not read: IEP; a source on personal petition (duʿāʾ), as Britannica has no entry under that name.
