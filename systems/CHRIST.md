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
    - {date: 2026-10-01, by: "Grok Bot", summary: "Draft: classification, origins, metaphysics, LIO axes (0–4, P1), science, schools, adherents and coding guidance filled from SEP entries, the multi-author Britannica article and a Pew Research Center report. v7.1 scores and note unchanged. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Coding guidance wording: B_cause is scored on the person's account of nature, not their work or creed (decision P6). No scores changed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit, run 2: E_scope how_known names the domain scored and points to open item P7 (which domain E is scored on). Score and certainty unchanged. Not reviewed."}
identity:
  id: CHRIST
  v7_1_number: 68
  v7_1_label: "Christianity"
  display_label: "Christianity"
  label_status: "as in v7.1"
  aliases: ["Christian faith", "the Christian tradition"]
classification:
  kind: {value: religion, certainty: 1.0, cites: [{source: S1, locator: "introduction"}], how_known: "Britannica calls it a 'major religion stemming from the life, teachings, and death of Jesus of Nazareth'."}
  family: {value: "Abrahamic monotheism", certainty: 1.0, cites: [{source: S2, locator: "§2.1"}], how_known: "SEP: 'Christianity is an Abrahamic monotheistic religion'."}
  parent_traditions: {value: ["Judaism"], certainty: 1.0, cites: [{source: S2, locator: "§2.1"}, {source: S1, locator: "page 'The problem of scriptural authority'"}], how_known: "SEP: it 'developed in the first century CE out of Judaism'; Britannica: Christians inherited the Hebrew Bible as the Old Testament."}
  related_codes:
    - {code: CLASS_THEISM, relation: "neighbor (easily confused)", note: "v7.1 coding rule (Split theisms): the Thomist philosophical God is CLASS_THEISM, not generic CHRIST"}
    - {code: CLTHEI, relation: "neighbor (easily confused)", note: "v7.1 coding rule (Split theisms): the popular interventionist God is CLTHEI, not generic CHRIST"}
    - {code: JUDA, relation: "parent tradition"}
    - {code: PLATO, relation: overlaps, note: "Eastern and Western mystical theology drew on Plato and the Neoplatonists (Britannica, mysticism pages)"}
origins:
  founding_era: {value: "1st century CE", certainty: 1.0, cites: [{source: S1, locator: "introduction"}, {source: S2, locator: "§2.1"}], how_known: "Stated in both sources."}
  founding_region: {value: "Roman Judaea and the eastern Mediterranean: the ministry of Jesus of Nazareth, the Jerusalem church and Paul's mission to the Gentiles.", certainty: 0.7, cites: [{source: S1, locator: "pages 'Dogma: the most authoritative teaching' (Acts 15 council in Jerusalem) and 'The problem of scriptural authority' (Paul's Gentile mission)"}], how_known: "Pieced together from the places the article names; no single sentence gives a region, so 0.7."}
  founders_or_key_figures: {value: ["Jesus of Nazareth (the central figure)", "Paul the Apostle (earliest Christian texts, Gentile mission)", "Origen", "Augustine of Hippo", "Thomas Aquinas", "Martin Luther and the Reformation confessions", "Blaise Pascal, Søren Kierkegaard (modern defences of faith)"], certainty: 1.0, cites: [{source: S1, locator: "introduction; pages 'The problem of scriptural authority', 'Eastern Christianity', 'Western Catholic Christianity', 'Faith and reason', 'Protestantism'"}], how_known: "All named in the Britannica article in these roles. The list after Paul is a selection, not a ranking."}
  key_texts:
    - {value: "Old Testament (the Hebrew Bible, inherited from Judaism)", author: "multiple, ancient Israel", year: "before the 1st century CE", certainty: 1.0, cites: [{source: S2, locator: "§2.1"}, {source: S1, locator: "page 'The problem of scriptural authority'"}], how_known: "Both sources."}
    - {value: "New Testament: Gospels of Matthew, Mark, Luke and John; Acts; the letters of Paul and the Catholic Letters; Revelation", author: "Paul and other early Christian writers", year: "c. 50 CE (first letters of Paul) to the late 1st century; Mark near 70 CE", certainty: 1.0, cites: [{source: S1, locator: "page 'The problem of scriptural authority'"}, {source: S2, locator: "§2.1"}], how_known: "Britannica gives the dates for Paul's letters and Mark."}
    - {value: "Nicene Creed and the conciliar definitions of Nicaea and Constantinople (Trinity and Christ)", author: "ecumenical councils", year: "4th–5th century", certainty: 1.0, cites: [{source: S1, locator: "pages 'Dogma: the most authoritative teaching', 'Concepts of life after death'"}, {source: S4, locator: "introduction"}], how_known: "Britannica and SEP Trinity describe these councils as the main source of dogma."}
    - {value: "Augsburg Confession, in the Book of Concord (Lutheran)", author: "Lutheran reformers", year: "16th century", certainty: 0.7, cites: [{source: S1, locator: "page 'Protestantism'"}], how_known: "Britannica names it as the statement of Lutheran doctrine; the date is the coder's general knowledge, so 0.7. Example of a confessional text, one per branch would be needed for full coverage."}
metaphysics:
  god_nature_relation: {value: "God created the world from nothing and is distinct from it; the world is not part of God or an emanation of God's being.", stance: "creator distinct from creation", certainty: 1.0, cites: [{source: S2, locator: "§3.1"}], how_known: "SEP's summary of the doctrine of creation, which it says Western cultures had from biblical texts before modern cosmology."}
  deity_personal: {value: "Personal and triune: the one God exists as or in three equally divine Persons, Father, Son and Holy Spirit, and the Son became incarnate as Jesus. Theologians understand the term Person in different ways, and classical theologians also hold God to be simple and unchanging.", stance: personal, certainty: 1.0, cites: [{source: S4, locator: "introduction"}, {source: S1, locator: "page 'Dogma: the most authoritative teaching'"}], how_known: "SEP Trinity and Britannica state the doctrine directly."}
  intervention: {value: "The biblical God is free Creator, Sustainer and Judge and 'could suspend the natural order or break the causal chain through miracles'. The doctrine of creation adds special divine action (miracles, revelation) to general creation and sustenance. Theologians differ on how God acts, from interventionist creationism to non-interventionist quantum or chaos models.", stance: "varies by school", certainty: 0.7, cites: [{source: S1, locator: "page 'God as Creator, Sustainer, and Judge' (E. W. Benz)"}, {source: S2, locator: "§3.1"}], how_known: "Sources state the doctrine; the stance (varies by school) is a coder's reading of the spread, so 0.7."}
  miracles: {value: "Affirmed in the creeds and scripture (the Exodus rescue, the resurrection of Jesus are Britannica's examples); modern apologists argue from miracles and from reported healings, while critics question the reports.", stance: affirmed, certainty: 1.0, cites: [{source: S1, locator: "pages 'God as Creator, Sustainer, and Judge', 'Arguments from religious experience and miracles' (J. Hick)"}], how_known: "Britannica."}
  petition_and_prayer: {value: "Petition is central to practice. Aquinas qualifies it: 'We pray not in order to change the divine disposition' but to obtain what God has disposed to be achieved by prayer. Catholics and Orthodox also pray for the dead; Eastern monasticism stresses contemplative prayer (Hesychasm).", stance: "petition answered", certainty: 0.7, cites: [{source: S5, locator: "§2"}, {source: S1, locator: "pages 'Concepts of life after death', 'Eastern Christianity'"}], how_known: "SEP and Britannica. 0.7 because the classical wing reads answered petition in Aquinas's way."}
  afterlife: {value: "Personal: resurrection of the dead, judgment and eternal life. Britannica: 'Eternal life is personal life'. Views of the interval differ (immediate individual judgment, sleep of the soul, Catholic purgatory; Orthodoxy has no purgatory but prays for the dead).", stance: "personal afterlife", certainty: 1.0, cites: [{source: S1, locator: "page 'Concepts of life after death' (J. J. Pelikan)"}], how_known: "Britannica states it directly."}
  moral_ledger: {value: "Judgment after death with reward or punishment; 'its decision can also mean eternal punishment (Matthew 25:46)'. But salvation rests on grace, and the schools split: Augustinians restrict saving love to a limited elect, Arminians make it resistible, universalists say it cannot be thwarted forever. The Fifth General Council condemned universal reconciliation in 553 CE.", stance: "personal reward and punishment", certainty: 0.7, cites: [{source: S1, locator: "page 'Concepts of life after death'"}, {source: S3, locator: "§1; §2"}], how_known: "Britannica and SEP. 0.7 because grace and universalism make reward and punishment a simplification for many theologians."}
  authority: {value: "Revelation in scripture and in Christ, kept by the church through councils, creeds and (in some branches) bishops. Reason has a place: Aquinas held that reason can prove God and the soul's immortality and that revelation 'supplements, rather than cancels or replaces' philosophy, which Britannica calls the general though not universal Christian view. Kierkegaard's leap of faith is the fideist end; the Wesleyan quadrilateral adds experience, tradition and reason to scripture.", stance: "both, revelation first", certainty: 0.7, cites: [{source: S1, locator: "pages 'Faith and reason', 'Dogma: the most authoritative teaching', 'The problem of scriptural authority'"}, {source: S2, locator: "§2.1"}], how_known: "Sources state the range; the single stance is a coder's reading of the mainstream, so 0.7."}
  reserved_exemptions: {value: "Central: the incarnation, the resurrection and the biblical miracles are articles of faith and cannot be treated as ordinary natural events.", stance: central, certainty: 0.7, cites: [{source: S1, locator: "pages 'Dogma: the most authoritative teaching', 'Arguments from religious experience and miracles'"}, {source: S2, locator: "§3.1"}], how_known: "Coder's reading of what the creeds commit to, so 0.7."}
  teleology_in_nature: {value: "Creation is the orderly, intelligible product of a designer; the design argument has a long Christian history (criticised by Hume, reformulated in the 20th century). Some Christians read evolution as continuing creation (creatio continua).", stance: "designer's purposes", certainty: 1.0, cites: [{source: S2, locator: "§1.3"}, {source: S1, locator: "pages 'Christian philosophy as natural theology', 'God as Creator, Sustainer, and Judge'"}], how_known: "SEP and Britannica."}
  necessity_and_freedom: {value: "God creates freely, not by necessity. How providence and grace fit human freedom divides the schools (Augustinian election, Arminian resistible grace, universalism).", certainty: 0.7, cites: [{source: S2, locator: "§3.1"}, {source: S3, locator: "§1"}], how_known: "SEP. The summary across schools is the coder's, so 0.7."}
lio_axes:
  A_locus: {value: 0, rationale: "A transcendent, personal, triune creator distinct from the world, who became incarnate and acts in history. Mystical and apophatic strands (Origen, Pseudo-Dionysius, Erigena) and the classical simple God pull away from the pole without leaving the interventionist half.", certainty: 0.7, cites: [{source: S2, locator: "§3.1"}, {source: S4, locator: "introduction"}, {source: S1, locator: "pages 'Eastern Christianity', 'Western Catholic Christianity'"}], how_known: "Scored on the 0–4 scale (P1). 0.7 rather than 1.0 because of the classical and mystical wings."}
  B_cause: {value: 1, rationale: "Miracles, the resurrection and answered prayer are confessed, but against a created order that Christians also treat as lawful and intelligible ('Book of Nature'). Range: popular piety and creationism near 0, Thomist and non-interventionist models near 2.", certainty: 0.5, cites: [{source: S1, locator: "page 'God as Creator, Sustainer, and Judge'"}, {source: S2, locator: "§2.1; §3.1"}], how_known: "0–4 scale (P1). 0.5 because the schools spread across 0–2."}
  C_ledger: {value: 1, rationale: "Personal judgment with heaven, hell and (for Catholics) purgatory, so there is a personal ledger; but grace, not merit, decides salvation in most theology, and universalists deny a final division.", certainty: 0.5, cites: [{source: S1, locator: "page 'Concepts of life after death'"}, {source: S3, locator: "§1"}], how_known: "0–4 scale (P1). 0.5: Augustinian, Arminian and universalist theologies disagree."}
  D_authority: {value: 1, rationale: "Revelation first: scripture, creeds and church teaching, with reason as a partner in the Thomist line and experience and science added in Wesleyan and integration approaches. Fideists and fundamentalists sit at 0. Matches the v7.1 note's 'reliance on supernatural revelation'.", certainty: 0.5, cites: [{source: S1, locator: "page 'Faith and reason'"}, {source: S2, locator: "§2.1"}], how_known: "0–4 scale (P1). 0.5 for the spread."}
  E_scope: {value: 1, rationale: "Salvation is offered to all but runs through Christ and, for many, the church; God acts for particular people in answer to prayer and in particular events (incarnation, resurrection). Universalists and Arminians widen it; the Augustinian elect narrows it.", certainty: 0.5, cites: [{source: S3, locator: "§1"}, {source: S1, locator: "page 'Concepts of life after death'"}], how_known: "0–4 scale (P1). Coder's reading; schools disagree. Scored mainly on the scope of salvation, plus particular divine acts; the domain is open (OPEN_DECISIONS P7, PROPOSED), and on the world's order alone it would need a rescore. Already below the 0.7 cap."}
epistemology: {value: "Faith as assent to revealed truths on God's authority (Aquinas), supported but not replaced by reason; natural theology (design and cosmological arguments) and arguments from religious experience and miracles; voluntarist defences (Pascal's wager, James) and Kierkegaard's leap of faith; in science and religion, critical realism is the dominant outlook.", certainty: 1.0, cites: [{source: S1, locator: "pages 'Faith and reason', 'Christian philosophy as natural theology', 'Arguments from religious experience and miracles'"}, {source: S2, locator: "§2.1"}], how_known: "Britannica and SEP."}
ethics: {value: TODO, note: "Not researched in this run. The v7.1 note calls it a framework for 'salvation and ethics'; the content (love commands, natural law, Reformation ethics) would need its own sources."}
practice:
  ritual_and_practice: {value: "Baptism in the name of Father, Son and Holy Spirit; worship and prayer, including intercession for the dead in Catholic and Orthodox practice; monastic contemplative prayer.", certainty: 1.0, cites: [{source: S1, locator: "pages 'Dogma: the most authoritative teaching', 'Concepts of life after death', 'Eastern Christianity'"}], how_known: "Britannica."}
  community_form: {value: "The church, 'the community of people who make up the body of believers', divided into thousands of churches and denominations; the largest groups are Roman Catholic, Eastern Orthodox and Protestant, with the Oriental Orthodox as one of the oldest branches.", certainty: 1.0, cites: [{source: S1, locator: "introduction; 'The essence and identity of Christianity'"}], how_known: "Britannica."}
science:
  historical_stance: {value: "The two books metaphor (nature and scripture both reveal God) goes back to Augustine. Historians such as Hooykaas and Harrison argue Christian doctrine (creation as orderly; the Fall as a reason to rely on instruments and experiment) helped early modern science; SEP says claims that Christianity was uniquely responsible ignore Islamic and Greek contributions. The 1277 Condemnation of Paris opened room beyond Aristotle's physics.", certainty: 1.0, cites: [{source: S2, locator: "§1.3; §2.1"}], how_known: "SEP Religion and Science."}
  current_stance: {value: "Mostly integration and critical realism in the scholarly literature (Barbour, Peacocke, van Huyssteen, Murphy, Haught); 'vocal opposition to the theory of evolution among Christian fundamentalists' persists, and the conflict view dominates in public. Some Christians read evolution as continuing creation.", certainty: 1.0, cites: [{source: S2, locator: "§2.1"}, {source: S1, locator: "page 'God as Creator, Sustainer, and Judge'"}], how_known: "SEP and Britannica."}
schools_and_variants:
  - {name: "Roman Catholic (Thomist philosophical theology)", form: "scholastic or philosophical", how_it_differs: "Faith and reason as partners; purgatory; magisterium and councils. Aquinas's God is the classical simple God.", lio_difference: "B and D toward 2 in the philosophical wing; if a person's own writing is Thomist, code CLASS_THEISM.", certainty: 0.7, cites: [{source: S1, locator: "pages 'Faith and reason', 'Concepts of life after death'"}]}
  - {name: "Eastern Orthodox and Oriental Orthodox", form: regional, how_it_differs: "No purgatory but prayer for the dead; divinization through contemplative prayer (Hesychasm); Oriental Orthodox split over Christology in the 5th century.", lio_difference: "A slightly less stark (mystical union); otherwise like the code.", certainty: 0.7, cites: [{source: S1, locator: "introduction; pages 'Concepts of life after death', 'Eastern Christianity'"}]}
  - {name: "Protestant confessions (Lutheran, Anglican, Reformed, Free Church)", form: reform, how_it_differs: "Scripture as the main authority; great internal diversity (Britannica: greater than between some Protestant and non-Protestant forms).", lio_difference: "D near 0–1 in scripture-first wings; wide spread elsewhere.", certainty: 0.7, cites: [{source: S1, locator: "page 'Protestantism' (P. A. Crow)"}]}
  - {name: "Mystical theology (Origen, Evagrius, Pseudo-Dionysius, Erigena, Bernard)", form: mystical, how_it_differs: "Union with God; strong negative theology; draws on Plato and Plotinus.", lio_difference: "A moves toward 1; check PLATO if the person's thought is mainly Neoplatonic.", certainty: 0.7, cites: [{source: S1, locator: "pages 'Eastern Christianity', 'Western Catholic Christianity'"}]}
  - {name: "Fundamentalist and creationist Christianity", form: modern, how_it_differs: "Literal scripture; opposition to evolution.", lio_difference: "B and D at 0; close to CLTHEI.", certainty: 1.0, cites: [{source: S2, locator: "§2.1; §3.1"}]}
  - {name: "Integration and liberal theology (critical realism, kenosis, continuing creation)", form: modern, how_it_differs: "Reads science in a theological light and accepts evolution.", lio_difference: "B toward 2; D toward 2.", certainty: 0.7, cites: [{source: S2, locator: "§2.1"}, {source: S1, locator: "page 'God as Creator, Sustainer, and Judge'"}]}
adherents:
  use: "context only — never a genius-rate denominator"
  estimate: {value: "about 2.3 billion (28.8% of the world population)", year: 2020, scope: world, certainty: 0.7, cites: [{source: S6, locator: "key findings"}], how_known: "Pew Research Center demographic estimate. Survey-based estimates count self-identification and differ by source, so 0.7.", alternatives: [{value: "more than two billion", cites: [{source: S1, locator: "introduction"}]}]}
v7_1_rubric:
  label: "authorial v7.1 scores"
  L: 7
  P: 6
  E: 4
  V: 3
  X: 2
  total: 22
  scoring_note: "Christianity provides a comprehensive faith-based framework for salvation and ethics, but its reliance on supernatural revelation over empirical evidence limits its scientific alignment."
  source: "v7.1 data book, section 6 table (tables[4]) row 68 and section 7 scoring notes"
revised_rubric:
  status: "not started"
  L: {score: TODO, rationale: ""}
  P: {score: TODO, rationale: ""}
  E: {score: TODO, rationale: ""}
  V: {score: TODO, rationale: ""}
  X: {score: TODO, rationale: ""}
coding_guidance:
  use_when: "v7.1 coding rule (Split theisms): CLASS_THEISM (Aristotelian-Thomistic-Falsafa) is not CLTHEI (popular interventionist personal God) and not generic CHRIST/ISLAM/JUDA. Also (Scientists with church membership): Church tax / baptism ≠ ideology. Need writings. Faraday and Maxwell pass; many 19th-c names will be CHRIST-nominal / AGNOS-working. v8 note: use CHRIST when the person's own writing shows Christian belief (Christ, scripture, creeds, church) but not a more specific philosophical position. Record the branch (Catholic, Orthodox, Protestant confession, sect) in the person file; the code covers all of them."
  do_not_use_when: "Membership, baptism, church tax or upbringing only: no code from that (CODING_GUIDE; v7.1 rule). The writing works out the classical simple God of Aquinas: CLASS_THEISM. The writing stresses a God who intervenes and answers petition beyond what the creeds say: consider CLTHEI. God made the world and does not intervene, and revelation is rejected: DEISM. Mainly Neoplatonic metaphysics with little that is specifically Christian: consider PLATO. Score B_cause on the person's account of nature, not their creed (CODING_GUIDE §6; decision P6)."
  neighbors:
    - {code: CLASS_THEISM, relation: "neighbor (easily confused)"}
    - {code: CLTHEI, relation: "neighbor (easily confused)"}
    - {code: JUDA, relation: "parent tradition"}
    - {code: PLATO, relation: overlaps}
review:
  data_quality_flags:
    - "The v7.1 note attributes low scientific alignment to 'reliance on supernatural revelation over empirical evidence'. SEP (S2 §2.1) reports that the scholarly literature mostly sees integration, not conflict, between Christianity and science, and that historians credit Christian doctrine with some role in early modern science; conflict dominates mainly in public debate. This does not contradict the claim that revelation comes first (D_authority 1), but it is a different picture of the science stance. v7.1 text left unchanged."
    - "Adherent count (S6) is for context only."
  open_questions:
    - "Ethics is TODO."
    - "Faraday (Sandemanian) and Maxwell are in the first pool. The v7.1 rule says they pass the membership test; their person files decide CHRIST versus a narrower code from their own writings."
sources:
  - {id: S1, type: tertiary, kind: encyclopedia, author: "Martin E. Marty and others (multi-author article; page authors as listed by Britannica: E. W. Benz, J. J. Pelikan, J. Hick, P. A. Crow, G. Wainwright, L. Fredericksen)", citation: "\"Christianity.\" Encyclopaedia Britannica. Online article, main page and subpages 'The problem of scriptural authority', 'Dogma: the most authoritative teaching', 'God as Creator, Sustainer, and Judge', 'Concepts of life after death', 'Faith and reason', 'Christian philosophy as natural theology', 'Arguments from religious experience and miracles', 'Eastern Christianity', 'Western Catholic Christianity', 'Protestantism'. https://www.britannica.com/topic/Christianity.", url: "https://www.britannica.com/topic/Christianity", accessed: 2026-10-01, reliability_note: "Signed reference article. Only the article paragraphs were used; the AI-generated question boxes on Britannica pages were ignored.", used_for: [classification, origins, metaphysics, lio_axes, epistemology, practice, science, schools_and_variants]}
  - {id: S2, type: tertiary, kind: encyclopedia, author: "Helen De Cruz", year: 2022, citation: "De Cruz, Helen. \"Religion and Science.\" Stanford Encyclopedia of Philosophy. First published January 17, 2017; substantive revision September 3, 2022. https://plato.stanford.edu/entries/religion-science/.", url: "https://plato.stanford.edu/entries/religion-science/", accessed: 2026-10-01, reliability_note: "Peer-reviewed reference entry.", used_for: [classification, origins, metaphysics, lio_axes, science, schools_and_variants]}
  - {id: S3, type: tertiary, kind: encyclopedia, author: "Thomas Talbott", year: 2025, citation: "Talbott, Thomas. \"Heaven and Hell in Christian Thought.\" Stanford Encyclopedia of Philosophy. First published April 23, 2013; substantive revision May 10, 2025. https://plato.stanford.edu/entries/heaven-hell/.", url: "https://plato.stanford.edu/entries/heaven-hell/", accessed: 2026-10-01, reliability_note: "Peer-reviewed reference entry; the author defends universalism elsewhere, but the entry sets out all three positions.", used_for: [metaphysics, lio_axes]}
  - {id: S4, type: tertiary, kind: encyclopedia, author: "Dale Tuggy", year: 2025, citation: "Tuggy, Dale. \"Trinity.\" Stanford Encyclopedia of Philosophy. First published July 23, 2009; substantive revision August 14, 2025. https://plato.stanford.edu/entries/trinity/.", url: "https://plato.stanford.edu/entries/trinity/", accessed: 2026-10-01, reliability_note: "Peer-reviewed reference entry.", used_for: [origins, metaphysics, lio_axes]}
  - {id: S5, type: tertiary, kind: encyclopedia, author: "Scott A. Davison", year: 2026, citation: "Davison, Scott A. \"Petitionary Prayer.\" Stanford Encyclopedia of Philosophy. First published August 15, 2012; substantive revision May 18, 2026. https://plato.stanford.edu/entries/petitionary-prayer/.", url: "https://plato.stanford.edu/entries/petitionary-prayer/", accessed: 2026-10-01, reliability_note: "Peer-reviewed reference entry.", used_for: [metaphysics]}
  - {id: S6, type: secondary, kind: "institutional page", author: "Pew Research Center", year: 2025, citation: "Pew Research Center. \"How the Global Religious Landscape Changed From 2010 to 2020.\" June 9, 2025. https://www.pewresearch.org/religion/2025/06/09/how-the-global-religious-landscape-changed-from-2010-to-2020/.", url: "https://www.pewresearch.org/religion/2025/06/09/how-the-global-religious-landscape-changed-from-2010-to-2020/", accessed: 2026-10-01, reliability_note: "Demographic estimates from censuses and surveys; context only.", used_for: [adherents]}
---

# Christianity (CHRIST)

> Status: draft — unreviewed. Filled from Stanford Encyclopedia of Philosophy entries, the multi-author Britannica article and a Pew Research Center report. LIO axes use the 0–4 scale (P1). The v7.1 scores and note are unchanged. Ethics is TODO.

## Summary

Christianity is a religion that grew out of Judaism in the 1st century CE around Jesus of Nazareth [S2, §2.1; S1, introduction]. It is a broad tradition with thousands of churches; the largest groups are Roman Catholic, Eastern Orthodox and Protestant [S1, introduction]. This record covers the confessed religion as a whole. Two narrower codes split off parts of it under the v7.1 rule: CLASS_THEISM for the philosophical God of Aquinas, and CLTHEI for the popular interventionist God.

## Core metaphysics

God created the world from nothing and is distinct from it [S2, §3.1]. God is one God in three Persons, Father, Son and Holy Spirit, and the Son became incarnate as Jesus; the councils of the 4th and 5th centuries fixed this as dogma [S4, introduction; S1, Dogma]. Britannica says the biblical idea of God "included the concept that God could suspend the natural order or break the causal chain through miracles" [S1, God as Creator, Sustainer, and Judge]. The dead are raised and judged; "Eternal life is personal life" [S1, Concepts of life after death]. The schools differ on who is saved: SEP sets out "three quite different systems of theology", Augustinian, Arminian and universalist [S3, §1]. On prayer, Aquinas held that "We pray not in order to change the divine disposition" [S5, §2], while popular practice asks God to act.

## Position on the LIO axes

Scored on the 0–4 scale (P1), for the code as v7.1 defines it (the confessed religion as a whole). Certainty is lowered where the schools spread.

- A locus 0 (0.7): transcendent, personal, triune creator [S2, §3.1; S4]. The mystical and classical wings soften this.
- B cause 1 (0.5): confessed miracles and answered prayer within a lawful created order [S1; S2, §2.1]. Range 0–2.
- C ledger 1 (0.5): personal judgment, heaven and hell, but grace over merit; universalists deny a final split [S1; S3, §1].
- D authority 1 (0.5): revelation first, reason as a partner in the Thomist line, fideism at one end [S1, Faith and reason].
- E scope 1 (0.5): salvation through Christ; God acts for particular people and in particular events [S1; S3].

## Schools and variants

Roman Catholic theology treats faith and reason as partners and teaches purgatory [S1, Faith and reason; Concepts of life after death]. Eastern Orthodoxy has no purgatory but prays for the dead and stresses contemplative prayer [S1]. Protestantism divides into Lutheran, Anglican, Reformed and Free Church families, and Britannica says it is more diverse within itself than it is compared with some non-Protestant forms [S1, Protestantism]. The mystical theology of Origen, Pseudo-Dionysius and Erigena drew on Plato and Plotinus [S1, Eastern Christianity; Western Catholic Christianity]. In modern times, fundamentalists oppose evolution, while integration authors read science in a theological light [S2, §2.1].

## Science

SEP uses the two books metaphor as its starting point: God revealed Godself through the "Book of Nature" and the "Book of Scripture" [S2, §2.1]. Some historians argue Christian doctrine helped early modern science, for example through the idea of an orderly creation or the Fall as a reason to trust instruments over unaided reason. SEP adds that claims of a unique Christian role overlook Islamic and Greek scholars [S2, §2.1]. Today, critical realism is "the dominant epistemological outlook" in Christian science and religion. There is still "vocal opposition to the theory of evolution among Christian fundamentalists", and the conflict view prevails in public debate [S2, §2.1].

## Coding guidance

Membership, baptism or church tax is not ideology: the person needs writings (v7.1 rule). Use CHRIST when the person's own writing shows Christian belief but not a narrower position. If they work out Aquinas's simple God, use CLASS_THEISM. If they stress intervention and answered petition beyond the creeds, consider CLTHEI. If they reject revelation and keep a non-intervening creator, use DEISM. Score B_cause on the person's account of nature, not their creed (CODING_GUIDE §6; decision P6). Record the branch in the person file.

## v7.1 scoring note

Verbatim from the v7.1 data book, section 7 (authorial; not a finding):

> CHRIST (22/50) — Christianity. Christianity provides a comprehensive faith-based framework for salvation and ethics, but its reliance on supernatural revelation over empirical evidence limits its scientific alignment.

## Open questions

- The v7.1 note and SEP give different pictures of Christianity's relation to science (see review flags).
- Ethics is TODO.

## Research log

- 2026-10-01: stub created by `scripts/make_system_stubs.py`.
- 2026-10-01 (overnight run): read SEP "Religion and Science", "Heaven and Hell in Christian Thought", "Trinity" and "Petitionary Prayer"; Britannica "Christianity" (main page and ten subpages, signed by several authors); Pew Research Center's 2025 report on the global religious landscape. The Britannica pages carry AI-generated question boxes above the article; those were not used. All quotations were checked word for word against the fetched page text with a script. Not read: IEP, the SEP entries on Augustine and Aquinas for this record.
