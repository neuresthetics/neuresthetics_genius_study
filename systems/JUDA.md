---
record:
  record_type: system
  schema_version: "1.1"
  record_version: 4
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (overnight systems run for Jason)"
  model_used: "Grok Bot executor agent; direct reads of the cited encyclopedia entries"
  collected_on: 2026-10-01
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-01, by: scripts/make_system_stubs.py, summary: "Stub created from v7.1 data book table 4 and section 7."}
    - {date: 2026-10-01, by: "Grok Bot", summary: "Draft: classification, origins, metaphysics, LIO axes (0–4, P1), science, schools, adherents and coding guidance filled from three SEP entries, the multi-author Britannica article and a Pew Research Center report. v7.1 scores and note unchanged. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit, run 2: E_scope how_known names the domain scored and points to open item P7 (which domain E is scored on). Score and certainty unchanged. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "P7 decided (option 1): E_scope rescored on the world's order. Value and certainty unchanged (1 at 0.5); the basis is now God's particular acts in nature and history (revelation, the choice of Israel), not the covenant as a moral community. The covenant noted under C_ledger (C score unchanged). Not reviewed."}
identity:
  id: JUDA
  v7_1_number: 70
  v7_1_label: "Judaism"
  display_label: "Judaism"
  label_status: "as in v7.1"
  aliases: ["the Jewish religion", "Rabbinic Judaism (its main historical form)"]
classification:
  kind: {value: religion, certainty: 1.0, cites: [{source: S1, locator: "introduction"}], how_known: "Britannica: a 'monotheistic religion developed among the ancient Hebrews'."}
  family: {value: "Abrahamic monotheism", certainty: 1.0, cites: [{source: S2, locator: "§2.5"}], how_known: "SEP: 'one of the three major Abrahamic monotheistic traditions'."}
  parent_traditions: {value: ["the religion of ancient Israel (biblical Judaism)"], certainty: 0.7, cites: [{source: S1, locator: "introduction; 'The history of Judaism'"}, {source: S2, locator: "§2.5"}], how_known: "Britannica traces Judaism from the ancient Hebrews; SEP says most contemporary strains are Rabbinic rather than biblical. Treating the biblical religion as a parent is the coder's framing, 0.7."}
  related_codes:
    - {code: CLASS_THEISM, relation: "neighbor (easily confused)", note: "v7.1 coding rule (Split theisms): Maimonides' philosophical God is CLASS_THEISM, not generic JUDA"}
    - {code: CLTHEI, relation: "neighbor (easily confused)"}
    - {code: CHRIST, relation: offshoot, note: "SEP: Christianity developed in the first century CE out of Judaism"}
    - {code: ISLAM, relation: overlaps, note: "shared prophets and concept of God (Britannica, Islam)"}
    - {code: PANENT, relation: "neighbor (easily confused)", note: "decision S6: Kabbalah is coded JUDA by default, PANENT if the writing keeps a God beyond the world"}
origins:
  founding_era: {value: "Ancient Israel (biblical period, 2nd–1st millennium BCE); Rabbinic Judaism from the 1st–2nd centuries CE, after the destruction of the Temple in 70 CE", certainty: 0.7, cites: [{source: S1, locator: "introduction; page 'Basic beliefs and doctrines' (Temple cult ended 70 CE)"}, {source: S2, locator: "§2.5"}], how_known: "Britannica and SEP give the pieces; the summary dating is the coder's, 0.7."}
  founding_region: {value: "Ancient Israel and Judah (the land of Israel); later Babylonia and the diaspora", certainty: 0.7, cites: [{source: S1, locator: "introduction; page 'Humanity's place in the universe' (Babylonian Exile)"}], how_known: "Britannica; region wording is the coder's, 0.7."}
  founders_or_key_figures: {value: ["Abraham, Moses and the Hebrew prophets (in the tradition's own account)", "the rabbis of the Mishna and Talmud", "Philo of Alexandria", "Maimonides (1138–1204)", "Joseph Albo", "Israel Baʿal Shem Tov (Hasidism)", "Moses Mendelssohn", "Hermann Cohen", "Abraham Isaac Kook", "Mordecai Kaplan (Reconstructionism)"], certainty: 1.0, cites: [{source: S1, locator: "introduction; pages 'Jewish philosophy', 'Humanity's place in the universe', 'Religious reform movements', 'Modern Judaism'"}, {source: S2, locator: "§2.5"}, {source: S3, locator: "§1"}], how_known: "All named in these roles in Britannica or SEP. A selection, not a ranking."}
  key_texts:
    - {value: "Tanakh (the written Torah, Hebrew Bible)", author: "multiple, ancient Israel", year: "1st millennium BCE", certainty: 0.7, cites: [{source: S2, locator: "§2.5"}], how_known: "SEP names it as central; the date is the coder's, 0.7."}
    - {value: "Talmud (Mishna and Gemara), the Oral Law of Rabbinic Judaism", author: "the rabbis", year: "c. 2nd–6th century CE", certainty: 0.7, cites: [{source: S2, locator: "§2.5"}, {source: S1, locator: "page 'Humanity's place in the universe'"}], how_known: "SEP and Britannica name it; dating is the coder's, 0.7."}
    - {value: "Siddur (prayer book), including the Shema", author: "liturgical tradition", year: "formulations from the last pre-Christian and first Christian centuries", certainty: 1.0, cites: [{source: S1, locator: "page 'Basic beliefs and doctrines'"}], how_known: "Britannica: the Shema is often regarded as the Jewish confession of faith."}
    - {value: "Guide of the Perplexed", author: "Maimonides", year: 1190, certainty: 1.0, cites: [{source: S3, locator: "§1"}], how_known: "SEP: completed in 1190."}
    - {value: "Sefer ha-ʿiqqarim (Book of Principles)", author: "Joseph Albo", year: 1485, certainty: 1.0, cites: [{source: S1, locator: "page 'Humanity's place in the universe'"}], how_known: "Britannica."}
    - {value: "Pittsburgh Platform (Reform)", author: "Reform rabbinate", year: 1885, certainty: 1.0, cites: [{source: S2, locator: "§2.5"}], how_known: "SEP."}
    - {value: "Zohar and later Kabbalistic literature", author: "various", year: "medieval and early modern", certainty: 0.5, cites: [{source: S1, locator: "page 'Jewish mysticism'"}], how_known: "Britannica's mysticism page describes Kabbala; the Zohar is not named in the paragraphs read, so 0.5."}
metaphysics:
  god_nature_relation: {value: "God relates to the world 'as that of creator to creation', and his activity is ongoing: unlike the Stoic deity 'he remains actively present in nature'. Transcendence (holiness, otherness) is mirrored by immanence.", stance: "creator distinct from creation", certainty: 1.0, cites: [{source: S1, locator: "page 'Basic beliefs and doctrines' ('Creativity'; 'Otherness and nearness')"}], how_known: "Britannica states it directly."}
  deity_personal: {value: "Personal: the community has been confronted by the divine 'as a person', addressed as thou in the blessings. Maimonides' negative theology denies that the qualities named in prayer give knowledge of God's essence.", stance: personal, certainty: 1.0, cites: [{source: S1, locator: "page 'Basic beliefs and doctrines'"}, {source: S3, locator: "§4"}], how_known: "Britannica and SEP."}
  intervention: {value: "God acts in history and renews creation each day; creation, teaching and redemption together disclose 'God’s continual activity in the world'. In eschatology God is pictured as actively intervening. Maimonides' naturalism and Kaplan's process view pull away from this.", stance: regular, certainty: 0.7, cites: [{source: S1, locator: "pages 'Basic beliefs and doctrines', 'Humanity's place in the universe'"}, {source: S3, locator: "§1"}, {source: S2, locator: "§2.5"}], how_known: "Britannica on the liturgical creed; 0.7 because of the naturalist wings."}
  miracles: {value: "The tradition knows the miraculous (for example the possibility of restoring the dead to life), but views differ: Maimonides' naturalism made him suspicious of miracles, and his Messiah is not required to perform them.", stance: "varies by school", certainty: 0.7, cites: [{source: S1, locator: "page 'Humanity' ('The earthly-spiritual creature')"}, {source: S3, locator: "§1"}], how_known: "Britannica and SEP; 0.7 because no source surveys the whole range."}
  petition_and_prayer: {value: "Daily prayer is central; Maimonides insists it is mandatory even though he holds the qualities named in prayer are negations or descriptions of God's effects. SEP lists Judaism among the monotheisms whose petitionary prayer raises the classic puzzles.", stance: "petition answered", certainty: 0.5, cites: [{source: S3, locator: "§4"}, {source: S4, locator: "introduction"}], how_known: "Prayer practice is stated directly; that petition is answered is the coder's reading of SEP's grouping, so 0.5."}
  afterlife: {value: "Mixed. Belief in the resurrection of the body developed after the biblical period; under Greek influence the immortal soul was set beside or in place of it; medieval philosophers tried to reconcile the two; Maimonides' afterlife is 'purely intellectual'. Britannica: in the modern period 'Little or no consensus was evident'.", stance: "varies by school", certainty: 1.0, cites: [{source: S1, locator: "page 'Humanity' ('The earthly-spiritual creature'; 'Medieval and modern views of man')"}, {source: S3, locator: "§1"}], how_known: "Stated directly."}
  moral_ledger: {value: "The community is promised reward for obedience and punishment for disobedience (Deuteronomy 11), and Maimonides' 13 principles include 'divine punishment and reward' and the resurrection of the dead. The ledger is often communal and historical as much as individual.", stance: "personal reward and punishment", certainty: 0.7, cites: [{source: S1, locator: "page 'Basic beliefs and doctrines' ('Activity in the world')"}, {source: S3, locator: "§1"}], how_known: "Britannica and SEP; 0.7 because modern movements differ."}
  authority: {value: "Revelation and its interpretation: the written Torah and the Oral Law, read through rabbinic interpretation that holds Scripture should not be read in a simple literal fashion. Maimonides gave philosophy a large role; Reform declared science not antagonistic to Judaism; Kaplan wanted scientific methods applied to religion.", stance: "both, revelation first", certainty: 0.7, cites: [{source: S2, locator: "§2.5"}, {source: S3, locator: "§1; §2"}], how_known: "SEP. The single stance is the coder's reading of the mainstream, 0.7."}
  reserved_exemptions: {value: "Some: revelation to Moses and the prophets, the choice of Israel and the giving of the Torah are particular acts of God; non-literal rabbinic reading leaves room for science on many questions.", stance: some, certainty: 0.5, cites: [{source: S1, locator: "introduction; page 'Israel: the Jewish people'"}, {source: S2, locator: "§2.5"}], how_known: "Coder's reading, 0.5."}
  teleology_in_nature: {value: "Nature has never been seen as irrelevant to the divine purpose, and its restoration is part of the goal of history. Kook placed evolution within a cosmic evolution toward perfection; Kaplan saw reality as progressive but without a pre-ordained goal.", stance: "designer's purposes", certainty: 0.7, cites: [{source: S1, locator: "page 'Humanity's place in the universe'"}, {source: S2, locator: "§2.5"}], how_known: "Britannica and SEP; 0.7 for the spread."}
  necessity_and_freedom: {value: "God creates by free choice, not necessity: Maimonides rejects the Aristotelian view that the world is governed by necessity, partly because a God without free will could not issue commandments, while admitting that creation cannot be strictly demonstrated.", certainty: 1.0, cites: [{source: S3, locator: "§5"}], how_known: "SEP Maimonides."}
lio_axes:
  A_locus: {value: 0, rationale: "One transcendent, personal creator who acts in history and is addressed as thou. Maimonides' negative theology, Kabbalah and Reconstructionist naturalism move away from the pole.", certainty: 0.7, cites: [{source: S1, locator: "introduction; page 'Basic beliefs and doctrines'"}, {source: S3, locator: "§4"}, {source: S2, locator: "§2.5"}], how_known: "Scored on the 0–4 scale (P1). 0.7 for the philosophical, mystical and naturalist wings."}
  B_cause: {value: 1, rationale: "God is continually active in nature and history and intervenes in the end-time; but rabbinic and philosophical traditions read miracles cautiously (Maimonides' naturalism). Range 0–3.", certainty: 0.5, cites: [{source: S1, locator: "page 'Basic beliefs and doctrines'"}, {source: S3, locator: "§1"}], how_known: "0–4 scale (P1). 0.5 for the spread."}
  C_ledger: {value: 1, rationale: "Reward and punishment are part of the covenant and of Maimonides' principles; the afterlife is disputed and modern movements lack consensus. Under decision P7 the covenant as a moral community is scored here, not on E: God 'has chosen the people of Israel in love', yet is 'the teacher of all humanity' (S1, page 'Basic beliefs and doctrines').", certainty: 0.5, cites: [{source: S1, locator: "pages 'Basic beliefs and doctrines', 'Humanity'"}, {source: S3, locator: "§1"}], how_known: "0–4 scale (P1). 0.5 for the spread."}
  D_authority: {value: 1, rationale: "Revelation and the interpretive tradition first; non-literal reading and a strong philosophical line (Maimonides, Cohen, Kaplan) give reason more room than in scripture-literal traditions. Matches the v7.1 note's 'reliance on revelation'.", certainty: 0.5, cites: [{source: S2, locator: "§2.5"}, {source: S3, locator: "§2"}], how_known: "0–4 scale (P1). 0.5 for the spread; Reform and Reconstructionist forms sit near 2."}
  E_scope: {value: 1, rationale: "Scored on the world's order (decision P7). Leans exception. God 'remains actively present in nature' and acts in history (S1), and some acts are particular: revelation to Moses and the prophets, the choice of Israel and the giving of the Torah (reserved exemptions, S1). The tradition knows the miraculous (S1), and petition is the coder's reading of SEP's grouping (S4). Range 0–3: Maimonides' naturalism, which made him 'suspicious of miracles' (S3, §1), and non-literal rabbinic reading (S2, §2.5) lean toward 3. The covenant as a chosen people with a message for all is a question of moral community, scored on C, not here.", certainty: 0.5, cites: [{source: S1, locator: "pages 'Basic beliefs and doctrines', 'Humanity'; introduction"}, {source: S3, locator: "§1"}, {source: S2, locator: "§2.5"}, {source: S4, locator: "introduction"}], how_known: "0–4 scale (P1). Coder's reading, 0.5. Rescored on the world's order after decision P7 (2026-10-02); the value is unchanged from the earlier score, which rested on the covenant (1 at 0.5)."}
epistemology: {value: "Study and interpretation of texts (Torah, Talmud) as the central religious activity; rabbinic non-literal reading; philosophical theology (Maimonides: logic cannot settle creation versus eternity); mystical knowledge in Kabbalah, which seeks contact with the divine independently of sense perception and intellect.", certainty: 1.0, cites: [{source: S2, locator: "§2.5"}, {source: S3, locator: "§5"}, {source: S1, locator: "page 'Jewish mysticism'"}], how_known: "SEP and Britannica."}
ethics: {value: "Torah as 'a program of human action'; commandments govern relations with God, other people and the natural world (limits on human dominion); a covenant with obligations grounded in God's acts in history.", certainty: 1.0, cites: [{source: S1, locator: "pages 'Basic beliefs and doctrines', 'Humanity's place in the universe', 'Israel: the Jewish people'"}], how_known: "Britannica."}
practice:
  ritual_and_practice: {value: "Daily liturgy (the Shema and blessings), the commandments of Torah, and the religious calendar, including harvest festivals.", certainty: 1.0, cites: [{source: S1, locator: "pages 'Basic beliefs and doctrines', 'Humanity's place in the universe'"}, {source: S3, locator: "§4"}], how_known: "Britannica and SEP."}
  community_form: {value: "The Jewish people as covenant community; synagogues; in modern times Orthodox (including Neo-Orthodoxy and Hasidism), Conservative, Reform and Reconstructionist movements.", certainty: 1.0, cites: [{source: S1, locator: "pages 'Israel: the Jewish people', 'Religious reform movements'"}, {source: S2, locator: "§2.5"}], how_known: "Britannica and SEP."}
science:
  historical_stance: {value: "Maimonides had an enduring influence on Jewish thought and on the science and religion literature; Kabbalah influenced Renaissance Christian authors such as Pico della Mirandola. Early 20th-century Jewish scholars accepted evolution but were hesitant about natural selection as its mechanism.", certainty: 1.0, cites: [{source: S2, locator: "§2.5"}], how_known: "SEP Religion and Science."}
  current_stance: {value: "A spectrum: rabbinic non-literal reading leaves room for theories such as Big Bang cosmology; Reform holds that science is not antagonistic to Judaism (Pittsburgh Platform, 1885); Kook treated religion and science as largely separate domains; Kaplan argued for flow in both directions and an early Jewish process theology.", certainty: 1.0, cites: [{source: S2, locator: "§2.5"}], how_known: "SEP Religion and Science."}
schools_and_variants:
  - {name: "Rabbinic Judaism (Talmudic tradition)", form: other, how_it_differs: "Oral Law and interpretation; most contemporary strains are rabbinic rather than biblical.", lio_difference: "D slightly above scripture-literal traditions.", certainty: 1.0, cites: [{source: S2, locator: "§2.5"}]}
  - {name: "Medieval philosophy (Maimonides and others)", form: "scholastic or philosophical", how_it_differs: "Negative theology; naturalism suspicious of miracles; intellectual afterlife; creation chosen over necessity.", lio_difference: "A, B and D toward 2; if the person's own writing is in this line, code CLASS_THEISM.", certainty: 1.0, cites: [{source: S3, locator: "§1; §4; §5"}]}
  - {name: "Kabbalah and Hasidism", form: mystical, how_it_differs: "Direct contact with the divine beyond sense and intellect; Kabbala is akin to gnosis but almost purged of its dualism; Hasidism as an Orthodox pietist revival from the 18th century.", lio_difference: "A toward 1–2. Under S6, code JUDA by default and PANENT if the writing keeps a God beyond the world.", certainty: 0.7, cites: [{source: S1, locator: "pages 'Jewish mysticism', 'Religious reform movements'"}]}
  - {name: "Orthodox and Neo-Orthodox Judaism", form: other, how_it_differs: "Traditional observance; Neo-Orthodoxy divided religion (Orthodox) from culture (Western).", lio_difference: "As scored, D toward 0–1.", certainty: 1.0, cites: [{source: S1, locator: "page 'Religious reform movements'"}]}
  - {name: "Reform Judaism", form: reform, how_it_differs: "A child of Enlightenment rationalism; messianism turned to social welfare; science not antagonistic to Judaism.", lio_difference: "B and D toward 2.", certainty: 1.0, cites: [{source: S1, locator: "page 'Religious reform movements'"}, {source: S2, locator: "§2.5"}]}
  - {name: "Conservative Judaism", form: modern, how_it_differs: "Judaism as a developing religion guided by tradition and the will of the people; largely traditional observance.", lio_difference: "Between Orthodox and Reform.", certainty: 1.0, cites: [{source: S1, locator: "page 'Religious reform movements'"}]}
  - {name: "Reconstructionism (Kaplan)", form: modern, how_it_differs: "Naturalistic framework; God as the source of a progressive process without a pre-ordained goal.", lio_difference: "A toward 2–3; B and D toward 3.", certainty: 0.7, cites: [{source: S1, locator: "page 'Humanity's place in the universe'"}, {source: S2, locator: "§2.5"}]}
adherents:
  use: "context only — never a genius-rate denominator"
  estimate: {value: "14.8 million (Jews worldwide; up nearly 1 million from 2010)", year: 2020, scope: world, certainty: 0.7, cites: [{source: S5, locator: "key findings"}], how_known: "Pew Research Center demographic estimate. Counts Jews by self-identification, which includes non-religious Jews, so 0.7 as a count of the religion."}
v7_1_rubric:
  label: "authorial v7.1 scores"
  L: 7
  P: 6
  E: 4
  V: 3
  X: 2
  total: 22
  scoring_note: "Judaism provides a rich ethical and covenantal framework with historical depth, but its reliance on revelation over empirical evidence limits its score on scientific metrics."
  source: "v7.1 data book, section 6 table (tables[4]) row 70 and section 7 scoring notes"
revised_rubric:
  status: "not started"
  L: {score: TODO, rationale: ""}
  P: {score: TODO, rationale: ""}
  E: {score: TODO, rationale: ""}
  V: {score: TODO, rationale: ""}
  X: {score: TODO, rationale: ""}
coding_guidance:
  use_when: "v7.1 coding rule (Split theisms): CLASS_THEISM (Aristotelian-Thomistic-Falsafa) is not CLTHEI (popular interventionist personal God) and not generic CHRIST/ISLAM/JUDA. v8 note: use JUDA when the person's own writing shows Jewish religious belief or practice (God, Torah, covenant) without a more specific philosophical position. Record the movement (Orthodox, Conservative, Reform, Reconstructionist, Hasidic) in the person file. Kabbalah is coded JUDA by default (decision S6)."
  do_not_use_when: "Jewish descent or upbringing alone: no code; many Jews are not religious, so descent says nothing about working metaphysics. Writing that works out Maimonides' philosophical God (simple, known by negation, creation chosen over necessity): CLASS_THEISM. Kabbalistic writing that keeps a God beyond the world as well as in it: PANENT (S6). Spinoza's God or Nature: PANT, not JUDA. Popular interventionism beyond the tradition: consider CLTHEI."
  neighbors:
    - {code: CLASS_THEISM, relation: "neighbor (easily confused)"}
    - {code: CLTHEI, relation: "neighbor (easily confused)"}
    - {code: PANENT, relation: "neighbor (easily confused)"}
    - {code: CHRIST, relation: offshoot}
review:
  data_quality_flags:
    - "The v7.1 note cites 'reliance on revelation over empirical evidence'. SEP (S2 §2.5) reports that rabbinic tradition holds Scripture should not be read in a simple literal fashion, which 'opens up more space for accepting scientific theories', and that Reform Judaism takes an explicit anti-conflict view. This fits D_authority 1 with low certainty but is a more open picture than the note's. v7.1 text left unchanged."
    - "Pew's 14.8 million counts Jews, not religious practice; context only."
  open_questions:
    - "None of the first-pool people is likely to be coded JUDA, but Maimonides' line matters for CLASS_THEISM."
sources:
  - {id: S1, type: tertiary, kind: encyclopedia, author: "Louis H. Feldman, Moshe Greenberg, Gerson D. Cohen, Salo Wittmayer Baron and others (multi-author article)", citation: "\"Judaism.\" Encyclopaedia Britannica. Online article, main page and subpages 'Basic beliefs and doctrines', 'Humanity', 'Jewish philosophy', 'Humanity's place in the universe', 'Israel: the Jewish people', 'Jewish mysticism', 'Religious reform movements', 'Modern Judaism (c. 1750 to the present)'. https://www.britannica.com/topic/Judaism.", url: "https://www.britannica.com/topic/Judaism", accessed: 2026-10-01, reliability_note: "Signed reference article. Article paragraphs only; the AI-generated question boxes on Britannica pages were ignored.", used_for: [classification, origins, metaphysics, lio_axes, epistemology, ethics, practice, schools_and_variants]}
  - {id: S2, type: tertiary, kind: encyclopedia, author: "Helen De Cruz", year: 2022, citation: "De Cruz, Helen. \"Religion and Science.\" Stanford Encyclopedia of Philosophy. First published January 17, 2017; substantive revision September 3, 2022. https://plato.stanford.edu/entries/religion-science/.", url: "https://plato.stanford.edu/entries/religion-science/", accessed: 2026-10-01, reliability_note: "Peer-reviewed reference entry.", used_for: [classification, origins, metaphysics, lio_axes, science, schools_and_variants]}
  - {id: S3, type: tertiary, kind: encyclopedia, author: "Kenneth Seeskin", year: 2024, citation: "Seeskin, Kenneth. \"Maimonides.\" Stanford Encyclopedia of Philosophy. First published January 24, 2006; substantive revision November 18, 2024. https://plato.stanford.edu/entries/maimonides/.", url: "https://plato.stanford.edu/entries/maimonides/", accessed: 2026-10-01, reliability_note: "Peer-reviewed reference entry.", used_for: [origins, metaphysics, lio_axes, epistemology, schools_and_variants]}
  - {id: S4, type: tertiary, kind: encyclopedia, author: "Scott A. Davison", year: 2026, citation: "Davison, Scott A. \"Petitionary Prayer.\" Stanford Encyclopedia of Philosophy. First published August 15, 2012; substantive revision May 18, 2026. https://plato.stanford.edu/entries/petitionary-prayer/.", url: "https://plato.stanford.edu/entries/petitionary-prayer/", accessed: 2026-10-01, reliability_note: "Peer-reviewed reference entry.", used_for: [metaphysics]}
  - {id: S5, type: secondary, kind: "institutional page", author: "Pew Research Center", year: 2025, citation: "Pew Research Center. \"How the Global Religious Landscape Changed From 2010 to 2020.\" June 9, 2025. https://www.pewresearch.org/religion/2025/06/09/how-the-global-religious-landscape-changed-from-2010-to-2020/.", url: "https://www.pewresearch.org/religion/2025/06/09/how-the-global-religious-landscape-changed-from-2010-to-2020/", accessed: 2026-10-01, reliability_note: "Demographic estimates from censuses and surveys; context only.", used_for: [adherents]}
---

# Judaism (JUDA)

> Status: draft — unreviewed. Filled from Stanford Encyclopedia of Philosophy entries, the multi-author Britannica article and a Pew Research Center report. LIO axes use the 0–4 scale (P1). The v7.1 scores and note are unchanged.

## Summary

Judaism is the monotheistic religion of the Jewish people. Britannica describes it as belief "in one transcendent God who revealed himself to Abraham, Moses, and the Hebrew prophets" and a life lived by Scripture and rabbinic tradition [S1, introduction]. SEP notes that "Most contemporary strains of Judaism are Rabbinic, rather than biblical" [S2, §2.5]. This record covers the religion as a whole. Under the v7.1 rule, Maimonides' philosophical God is CLASS_THEISM, and under decision S6 Kabbalah stays JUDA by default.

## Core metaphysics

The liturgical creed presents God as creator whose activity "is not in the past but is ongoing and continuous", and who, unlike the Stoic deity, "remains actively present in nature" [S1, Basic beliefs and doctrines]. God is met "as a person" and addressed as thou [S1, Basic beliefs and doctrines]. The covenant promises reward for obedience and punishment for disobedience [S1, Basic beliefs and doctrines]. Views of the afterlife changed over time, from bodily resurrection to the immortal soul to medieval attempts to reconcile the two. In the modern period "Little or no consensus was evident" [S1, Humanity]. Maimonides listed 13 principles, including "divine punishment and reward" and resurrection. His own afterlife is "purely intellectual" and his "naturalism makes him suspicious of miracles" [S3, §1].

## Position on the LIO axes

Scored on the 0–4 scale (P1), for the code as v7.1 defines it (the religion as a whole):

- A locus 0 (0.7): transcendent personal creator [S1].
- B cause 1 (0.5): continual divine activity; cautious about miracles in the philosophical line [S1; S3, §1].
- C ledger 1 (0.5): covenant reward and punishment; afterlife disputed [S1; S3].
- D authority 1 (0.5): revelation and interpretation; non-literal reading [S2, §2.5].
- E scope 1 (0.5): on the world's order (P7), God acts in nature and history, with particular acts such as revelation and the choice of Israel [S1]; Maimonides leans toward 3 [S3, §1]. The covenant as a moral community is scored on C.

## Schools and variants

Rabbinic Judaism is the main historical form [S2, §2.5]. Maimonides represents the medieval philosophical line [S3]. Kabbalah is a mysticism "akin to gnosis" but almost purged of dualism [S1, Jewish mysticism]. In modern times the movements divide: Orthodoxy, including Neo-Orthodoxy and Hasidism; Reform, "a child of Enlightenment rationalism"; Conservative, "a child of historical romanticism"; and Kaplan's Reconstructionism [S1, Religious reform movements; S2, §2.5].

## Science

SEP says rabbinic non-literal reading "opens up more space for accepting scientific theories (e.g., Big Bang cosmology)" [S2, §2.5]. The Reform Pittsburgh Platform of 1885 states: "We hold that the modern discoveries of scientific researches in the domain of nature and history are not antagonistic to the doctrines of Judaism" [S2, §2.5]. Early 20th-century Jewish scholars accepted evolution but hesitated over natural selection. Kook kept science and religion largely separate, and Kaplan argued for a two-way flow [S2, §2.5].

## Coding guidance

Use JUDA when the person's own writing shows Jewish religious belief or practice without a narrower position. Jewish descent alone gives no code. If the writing works out Maimonides' philosophical God, use CLASS_THEISM. If it is Kabbalah that keeps a God beyond the world, use PANENT; otherwise Kabbalah stays JUDA (S6). Spinoza is PANT.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> JUDA (22/50) — Judaism. Judaism provides a rich ethical and covenantal framework with historical depth, but its reliance on revelation over empirical evidence limits its score on scientific metrics.

## Open questions

- SEP gives a more open picture of Judaism and science than the v7.1 note (see review).

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-01 (overnight run): read SEP "Religion and Science", "Maimonides" and "Petitionary Prayer"; Britannica "Judaism" (main page and eight subpages, multi-author); Pew Research Center's 2025 report. SEP has no general Judaism entry. AI-generated question boxes on Britannica pages were not used. All quotations were checked word for word against the fetched page text with a script.
