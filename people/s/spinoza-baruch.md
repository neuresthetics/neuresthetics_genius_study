---
record:
  record_type: person
  schema_version: "1.2"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (executor agent for v8, RUNBOOK stage 3, batch A: early modern philosophers)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (stage 3, batch A). Basics from Britannica (Popkin, first page) and SEP 'Baruch Spinoza' (Nadler). Worldview from the Ethics and the Theological-Political Treatise in Elwes's translation, read in the Project Gutenberg texts (unofficial web copies, so every field resting on them is capped at 0.7 under CODING_GUIDE §7). The Cambridge edition (ed. Kisner) was not opened. DRAFT SCORES for v8's review: primary_system PANT 0.7; A 4, B 4, C 4, D 3, E 4, all at 0.7; mid_basin false (0.7). Not reviewed."}

identity:
  id: spinoza-baruch
  display_name: "Baruch Spinoza"
  roster:
    canonical_name: "Baruch Spinoza"
    rank: 11
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: philosophy
    field_bucket: philosophy
  full_name: {value: "Bento (Baruch, Benedictus) de Spinoza", certainty: 1.0, cites: [{source: S2, locator: "§1, paragraph 1"}, {source: S1, locator: "heading and 'Also known as'"}], how_known: "SEP gives the three forms of the given name; Britannica titles him Benedict de Spinoza."}
  native_name: {value: "Bento de Espinosa (Portuguese); Baruch (Hebrew); Benedictus de Spinoza (Latin)", certainty: 0.7, cites: [{source: S2, locator: "§1, paragraph 1"}, {source: S1, locator: "'Also known as'"}], how_known: "SEP gives Bento, Baruch, Benedictus; the Portuguese surname form is from Britannica's alias list only."}
  aliases:
    - {name: "Baruch-Spinoza", kind: "roster alias"}
    - {name: "Benedict de Spinoza", kind: "roster alias"}
    - {name: "Spinoza-Baruch", kind: "roster alias"}
    - {name: "Benedictus de Spinoza", kind: latinized}

basics:
  birth:
    date: {value: "1632-11-24", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening sentence"}, {source: S2, locator: "§1, paragraph 1 (year)"}], how_known: "Britannica gives the day; SEP agrees on the year and Amsterdam. Day from one source, so 0.7."}
    place: {value: "Amsterdam", modern_name: "Amsterdam, Netherlands", polity_then: "Dutch Republic", certainty: 1.0, cites: [{source: S1, locator: "opening sentence"}, {source: S2, locator: "§1, paragraph 1"}], how_known: "Two sources agree."}
  death:
    date: {value: "1677-02-21", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening sentence"}, {source: S2, locator: "§1, last paragraph (year)"}], how_known: "Britannica gives the day; SEP agrees on the year and The Hague."}
    place: {value: "The Hague", modern_name: "The Hague, Netherlands", polity_then: "Dutch Republic", certainty: 1.0, cites: [{source: S1, locator: "opening sentence"}, {source: S2, locator: "§1, last paragraph"}], how_known: "Two sources agree."}
  first_lasting_contribution_year: {value: 1670, certainty: 0.7, cites: [{source: S2, locator: "§1, last paragraph; §3"}], how_known: "The Theological-Political Treatise, published anonymously in 1670, is the earliest item in lasting_original_contributions. The Ethics was being written by 1663 but appeared only in 1677; choosing the 1670 publication is the coder's call."}
  era_bucket: {value: "1600 to 1749", certainty: 1.0, cites: [{source: S2, locator: "§1"}], how_known: "From first_lasting_contribution_year (P2). 1663, 1670 and 1677 all fall in the same bucket."}
  region_of_birth: {value: "Western Europe", certainty: 1.0, cites: [{source: S1, locator: "opening sentence"}], how_known: "Netherlands is Western Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Western Europe", certainty: 1.0, cites: [{source: S2, locator: "§1"}], how_known: "Amsterdam, Rijnsburg, Voorburg and The Hague."}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S2, locator: "§1"}], how_known: "As the sources record it."}
  languages_of_work: {value: [Latin, Dutch], certainty: 0.7, cites: [{source: S2, locator: "§2.1 ('Latin (but not the original Dutch) edition of the Ethics')"}], how_known: "The Ethics was published in Latin and in a Dutch version (SEP); which language he wrote other works in was not checked."}
  occupations: {value: [philosopher, "lens grinder", merchant], certainty: 1.0, cites: [{source: S1, locator: "Top Questions; 'Early life and career'"}, {source: S2, locator: "§1, paragraph 1 (family importing business)"}], how_known: "Two sources: family business, then lens grinding while writing philosophy."}

contribution:
  fields: {value: [metaphysics, ethics, "political philosophy", "biblical criticism"], certainty: 1.0, cites: [{source: S2, locator: "opening; §§2–3"}, {source: S1, locator: "opening"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Theological-Political Treatise: historical and critical reading of Scripture, the separation of philosophy from theology, and a case for toleration and freedom of thought", year: "1670", kind: work, lasting: "founding text of modern biblical criticism and of the liberal argument for free philosophizing", certainty: 0.7, cites: [{source: S2, locator: "§3, §3.1, §3.2"}], how_known: "SEP; 'lasting' wording is the coder's summary of SEP's account."}
    - {value: "Ethics: a monist metaphysics of one substance, God or Nature, with a naturalistic psychology and ethics set out in geometrical order", year: "1677", kind: work, lasting: "canonical text of early modern rationalism and of pantheism", certainty: 1.0, cites: [{source: S2, locator: "§2, §2.1"}, {source: S1, locator: "opening"}], how_known: "Two sources."}
  evidence_of_impact:
    - {value: "Called 'one of the most important philosophers—and certainly the most radical—of the early modern period' and 'among the most relevant today'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S2, locator: "opening paragraph"}], how_known: "SEP, one scholarly reference work."}
  major_works:
    - {value: "Renati des Cartes Principiorum Philosophiae (Descartes's Principles of Philosophy)", year: 1663, kind: book, certainty: 1.0, cites: [{source: S2, locator: "§1"}, {source: S1, locator: "Top Questions"}], how_known: "Two sources; the only work published under his name in his lifetime (SEP)."}
    - {value: "Tractatus Theologico-Politicus", year: 1670, kind: book, certainty: 1.0, cites: [{source: S2, locator: "§1"}, {source: S1, locator: "Top Questions"}], how_known: "Two sources."}
    - {value: "Ethica, ordine geometrico demonstrata (in the Opera posthuma)", year: 1677, kind: book, certainty: 1.0, cites: [{source: S2, locator: "§1; §2"}, {source: S1, locator: "opening"}], how_known: "Two sources."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Lasting original system in metaphysics, ethics and political thought.", certainty: 1.0, cites: [{source: S2, locator: "opening"}], how_known: "Sources agree."}

childhood:
  family_religion: {value: "Jewish (Amsterdam's Portuguese-Jewish community; the parents had been forcibly converted in Portugal and practised Judaism in secret before escaping)", certainty: 1.0, cites: [{source: S1, locator: "'Early life and career', paragraph 1"}, {source: S2, locator: "§1, paragraph 1"}], how_known: "Two sources."}
  family_religious_practice: {value: "Practising: the father served as one of the directors of the city's synagogue", certainty: 0.7, cites: [{source: S1, locator: "'Early life and career', paragraph 1"}], how_known: "Britannica."}
  parents_and_household:
    - {value: "Father, Michael, an important merchant and a director of the Amsterdam synagogue (died 1654)", name: "Michael Spinoza", role: father, certainty: 0.7, cites: [{source: S1, locator: "'Early life and career', paragraph 1; 'Excommunication' paragraph"}], how_known: "Britannica."}
    - {value: "Mother, Hannah, died in 1638, shortly before his sixth birthday", name: "Hannah Spinoza", role: mother, certainty: 0.7, cites: [{source: S1, locator: "'Early life and career', paragraph 1"}], how_known: "Britannica."}
  household_circumstances: {value: "Middle son of a prominent family of moderate means in the Portuguese-Jewish community", certainty: 0.7, cites: [{source: S2, locator: "§1, paragraph 1"}], how_known: "SEP."}
  schooling:
    - {value: "Talmud Torah school of the Amsterdam congregation; did not reach the upper levels (advanced Talmud); studies cut short at seventeen for the family business", stage: "religious school", years: "–c. 1649", ages: "to 17", certainty: 1.0, cites: [{source: S2, locator: "§1, paragraph 1"}, {source: S1, locator: "'Early life and career', paragraph 3"}], how_known: "Two sources."}
  early_mathematics: {value: TODO, note: "Not in the sources read."}
  early_geometric_style_reasoning: {value: TODO, note: "Not in the sources read; his geometrical method is documented only for the adult Ethics."}
  early_science_exposure: []
  key_early_reading:
    - {value: "Probably Hebrew and some Jewish philosophy, including Maimonides, at the Talmud-Torah school", certainty: 0.5, cites: [{source: S1, locator: "'Early life and career', paragraph 3 ('probably learned')"}], how_known: "Britannica hedges it ('probably')."}
  childhood_mentors: []
  languages_in_childhood: {value: TODO, note: "Portuguese and Hebrew are likely but not stated in the sources read."}
  notable_events:
    - {value: "Mother's death", year: "1638", age: 5, certainty: 0.7, cites: [{source: S1, locator: "'Early life and career', paragraph 1"}], how_known: "Britannica."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1656–1677", certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "From the herem of 1656 to his death; the coder's span."}
  nominal_affiliations:
    - {value: "Member of the Amsterdam Portuguese-Jewish congregation until his herem (excommunication) of 27 July 1656, never rescinded", certainty: 1.0, cites: [{source: S2, locator: "§1, paragraph 2"}, {source: S1, locator: "'Excommunication'"}], how_known: "Two sources (SEP gives the day)."}
  self_described_science_religion_relation:
    value: "Philosophy and theology each have their own domain: 'The sphere of reason is, as we have said, truth and wisdom; the sphere of theology, is piety and obedience' (TTP ch. 15). Knowledge of nature and of God comes from reason, not from prophecy or miracles: 'we cannot gain knowledge of the existence and providence of God by means of miracles, but [...] we can far better infer them from the fixed and immutable order of nature' (TTP ch. 6)."
    certainty: 0.7
    cites: [{source: S5, locator: "TTP ch. 15, sentences (52)–(53)"}, {source: S4, locator: "TTP ch. 6, sentence (40)"}]
    how_known: "His own published treatise, read in an unofficial web copy of Elwes's translation; capped at 0.7 (CODING_GUIDE §7)."
  primary_system:
    value: PANT
    basis: written_profession
    certainty: 0.7
    cites: [{source: S3, locator: "E1P15; E1P18; E1P29; E4 Preface"}, {source: S2, locator: "§2.1"}]
    how_known: "His own published Ethics. Capped at 0.7 twice over: the text was read in an unofficial web copy (CODING_GUIDE §7), and the record names a plausible alternative code (ATHE; contested-readings rule, §3)."
    rationale: "DRAFT for v8's review. Passes the S6 two-part test in his own words: (1) God is identified with Nature as a claim about what exists ('the eternal and infinite Being, which we call God or Nature', E4 Preface; 'Whatsoever is, is in God', E1P15; God 'the indwelling and not the transient cause of all things', E1P18); (2) the whole has marks beyond feeling: one substance (E1P14–15), necessity (E1P29, E1P33) and eternity (E1P19). PANT's v7.1 rule is defined by his phrase 'Deus sive Natura', and the founders rule points the same way. Named alternative: ATHE, because SEP (Nadler) argues that he is not a pantheist in the religious sense, since 'even the atheist can, without too much difficulty, admit that God is nothing but Nature' and worshipful awe is foreign to his philosophy (S2, §2.1)."
  secondary_system: {value: UNKNOWN, how_known: "He published in one system; the TTP's account of Scripture is a reading of JUDA/CHRIST texts, not a second system."}
  candidate_codes_considered:
    - {code: PANT, reason: "Coded (DRAFT): passes both parts of the S6 test from the Ethics; PANT is the sourced worked-example system file and is built on his texts.", cites: [{source: S3, locator: "E1P15; E4 Preface"}]}
    - {code: ATHE, reason: "Named alternative: SEP (Nadler) argues his God or Nature is naturalistic and reductive and that he rejects the religious attitudes that separate pantheism from atheism. Not coded because his own text keeps the term God with marks (one substance, necessity, eternity) that pass the S6 test. ATHE is a stub system file (flag).", cites: [{source: S2, locator: "§2.1"}]}
    - {code: DETERM, reason: "Considered: 'Nothing in the universe is contingent' (E1P29). Rejected as primary: determinism is one consequence of his God-Nature monism, not the whole working metaphysics. DETERM is a stub system file.", cites: [{source: S3, locator: "E1P29"}]}
    - {code: JUDA, reason: "Rejected: heritage and childhood community only; excommunicated in 1656 and denies that the Law was given by God (S2, §1). Heritage is never a code.", cites: [{source: S2, locator: "§1"}]}
  lio_axes:
    A_locus:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S3, locator: "E1P15; E1P18; E4 Preface"}]
      how_known: "His own published text in an unofficial web copy; capped at 0.7 (§7)."
      rationale: "DRAFT. At the LIO pole: God is immanent in or identical with the world. 'Whatsoever is, is in God, and without God nothing can be, or be conceived' (E1P15); God is 'the indwelling and not the transient cause of all things' (E1P18); 'God or Nature' (E4 Preface). The scholarly dispute over whether God is all of Nature or only natura naturans (S2, §2.1) does not move the score: both readings are immanent."
    B_cause:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S3, locator: "E1P29; E1 Appendix"}, {source: S4, locator: "TTP ch. 6, sentences (17), (19)"}]
      how_known: "His own published texts in unofficial web copies; capped at 0.7 (§7)."
      rationale: "DRAFT. Scored on his account of nature (P6); at the LIO pole. 'Nothing in the universe is contingent' (E1P29); an event against nature's universal laws would mean 'that God acted against His own nature - an evident absurdity' (TTP ch. 6, (17)); appeal to God's will for an event is 'the sanctuary of ignorance' (E1 Appendix). No miracle, petition or exemption anywhere in nature."
    C_ledger:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S3, locator: "E5P17 and Corollary; E5P19; E5P42"}]
      how_known: "His own published text in an unofficial web copy; capped at 0.7 (§7). Also a named alternative (the eternity of the mind)."
      rationale: "DRAFT. At the impersonal-consequence pole: 'Strictly speaking, God does not love or hate anyone' (E5P17 Corollary); 'He, who loves God, cannot endeavour that God should love him in return' (E5P19); 'Blessedness is not the reward of virtue, but virtue itself' (E5P42). E1 Appendix traces 'praise and blame, sin and merit' to the false belief that we are free agents. Named alternative: 3, because 'there remains of it something which is eternal' (E5P23) is read by some as a form of survival; SEP and Britannica differ on how far he discusses immortality (see flags)."
    D_authority:
      value: 3
      basis: written_profession
      certainty: 0.7
      cites: [{source: S5, locator: "TTP ch. 15, sentences (52)–(55), (64), (94)"}, {source: S2, locator: "§3.1"}]
      how_known: "His own published treatise in an unofficial web copy; capped at 0.7 (§7) and a named alternative."
      rationale: "DRAFT. Leans LIO with one stated, limited exception. Prophecy 'does not provide privileged knowledge of natural or spiritual phenomena' (SEP §3.1), and theology 'has neither the will nor the power to oppose reason' and 'leaves reason to determine their precise truth' (TTP ch. 15, (55)). The exception: the one dogma that 'simple obedience is the path of salvation' cannot be reached 'by the natural light of reason', so 'revelation was necessary' (ch. 15, (64), (94)). Named alternative: 2, since he says theology and reason each have 'her own domain' (ch. 15, (52)), which under the same-pattern rule can read as two domains each with its own authority; not taken because revelation never outranks reason on any question of truth."
    E_scope:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S3, locator: "E1 Appendix; E3 Preface"}, {source: S6, locator: "TTP ch. 3, sentences (10), (13)–(14)"}]
      how_known: "His own published texts in unofficial web copies; capped at 0.7 (§7)."
      rationale: "DRAFT. Scored on the world's order (P7); at the LIO pole. Human actions are to be treated 'as though I were concerned with lines, planes, and solids' (E3 Preface); the belief 'that everything which is created is created for their sake' is the root error he attacks (E1 Appendix); 'the help of God' means 'the fixed and unchangeable order of nature' (TTP ch. 3, (13)), and 'the Hebrews did not surpass other nations in knowledge, or in piety' (ch. 3, (10)). No favour for any group in events. Election and salvation readings are not scored here (P7); his denial of a personal reward is on C."
  mid_basin: {value: false, certainty: 0.7, cites: [{source: S3, locator: "E1P15; E4 Preface"}], how_known: "P4 test: A_locus is 4 (at 0.7), so A ≥ 3 gives false. Certainty is capped by A_locus alone, the only axis this branch reads (decision P10): 0.7."}
  statements:
    - text: "Whatsoever is, is in God, and without God nothing can be, or be conceived."
      cites: [{source: S3, locator: "E1P15"}]
      date: "1677"
      context: "Ethics, Part I, Proposition 15, following the proof that God is the only substance (E1P14)."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "God is the indwelling and not the transient cause of all things."
      cites: [{source: S3, locator: "E1P18"}]
      date: "1677"
      context: "Ethics, Part I, Proposition 18."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "Nothing in the universe is contingent, but all things are conditioned to exist and operate in a particular manner by the necessity of the divine nature."
      cites: [{source: S3, locator: "E1P29"}]
      date: "1677"
      context: "Ethics, Part I, Proposition 29."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "So they will pursue their questions from cause to cause, till at last you take refuge in the will of God--in other words, the sanctuary of ignorance."
      cites: [{source: S3, locator: "E1 Appendix"}]
      date: "1677"
      context: "On people who explain a fatal accident by God's purpose. The double hyphen is the Gutenberg text's."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "For the eternal and infinite Being, which we call God or Nature, acts by the same necessity as that whereby it exists."
      cites: [{source: S3, locator: "E4 Preface"}, {source: S2, locator: "§2.1 (Latin 'Deus, sive Natura')"}]
      date: "1677"
      context: "Ethics, Part IV, Preface, on final causes. SEP notes the 'or Nature' clause is in the Latin but not the Dutch edition."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "I shall consider human actions and desires in exactly the same manner, as though I were concerned with lines, planes, and solids."
      cites: [{source: S3, locator: "E3 Preface"}]
      date: "1677"
      context: "Ethics, Part III, Preface, on method for the emotions."
      axes: [E_scope]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "Corollary.--Strictly speaking, God does not love or hate anyone."
      cites: [{source: S3, locator: "E5P17 Corollary"}]
      date: "1677"
      context: "Ethics, Part V, after Proposition 17 ('God is without passions')."
      axes: [C_ledger]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "Blessedness is not the reward of virtue, but virtue itself; neither do we rejoice therein, because we control our lusts, but, contrariwise, because we rejoice therein, we are able to control our lusts."
      cites: [{source: S3, locator: "E5P42"}]
      date: "1677"
      context: "Last proposition of the Ethics."
      axes: [C_ledger]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "Hence, any event happening in nature which contravened nature's universal laws, would necessarily also contravene the Divine decree, nature, and understanding; or if anyone asserted that God acts in contravention to the laws of nature, he, ipso facto, would be compelled to assert that God acted against His own nature - an evident absurdity."
      cites: [{source: S4, locator: "TTP ch. 6, sentence (17)"}]
      date: "1670"
      context: "Theological-Political Treatise, chapter 6, 'Of Miracles'. Sentence numbers are the Gutenberg volunteer's."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "We may conclude, then, that we cannot gain knowledge of the existence and providence of God by means of miracles, but that we can far better infer them from the fixed and immutable order of nature."
      cites: [{source: S4, locator: "TTP ch. 6, sentence (40)"}]
      date: "1670"
      context: "Same chapter, on what miracles can teach."
      axes: [B_cause, D_authority]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "By the help of God, I mean the fixed and unchangeable order of nature or the chain of natural events"
      cites: [{source: S6, locator: "TTP ch. 3, sentence (13)"}]
      date: "1670"
      context: "Chapter 3, 'Of the Vocation of the Hebrews', defining divine help and fortune before discussing election."
      axes: [E_scope]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "The sphere of reason is, as we have said, truth and wisdom; the sphere of theology, is piety and obedience."
      cites: [{source: S5, locator: "TTP ch. 15, sentence (53)"}]
      date: "1670"
      context: "Chapter 15, 'Theology is shown not to be subservient to Reason, nor Reason to Theology'."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "For as we cannot perceive by the natural light of reason that simple obedience is the path of salvation [Endnote 25], and are taught by revelation only that it is so by the special grace of God, which our reason cannot attain, it follows that the Bible has brought a very great consolation to mankind."
      cites: [{source: S5, locator: "TTP ch. 15, sentence (94)"}]
      date: "1670"
      context: "End of chapter 15: the one dogma he says only revelation teaches. '[Endnote 25]' is the Gutenberg text's marker."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
  changes_over_life:
    - {value: "Left Judaism: excommunicated from the Amsterdam congregation in 1656; SEP judges that his faith and religious commitment were 'by this point, gone'", year: "1656", certainty: 0.7, cites: [{source: S2, locator: "§1, paragraphs 2–3"}], how_known: "SEP's reading; the herem itself is documented."}
  coder_notes: "DRAFT SCORES for v8's review. All worldview fields rest on Project Gutenberg texts of Elwes's 1883 translation (S3–S6), unofficial web copies, so nothing worldview-related exceeds 0.7 (CODING_GUIDE §7). The Cambridge Texts edition (ed. Kisner), which v8 asked for, was not opened in this run; locators are by part and proposition (E1P15 etc.) and, for the TTP, by chapter and the Gutenberg volunteer's sentence numbers, which are not in any printed edition. No page numbers are given. Copy error noted: the Gutenberg TTP ch. 6, sentence (19), reads 'a fixed and mutable order', which is probably a dropped 'im-'; that sentence is not quoted. ATHE and DETERM are stub system files (flag). The 1650s report that he held that God exists, but only 'philosophically' (Britannica, an Augustinian friar's account) is reported speech and not used."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Portuguese-Jewish (Sephardic) community of Amsterdam; parents were Marranos (forcibly converted, secretly practising Jews) who escaped from Portugal", certainty: 1.0, cites: [{source: S1, locator: "'Early life and career', paragraph 1"}, {source: S2, locator: "§1, paragraph 1"}], how_known: "Two sources."}
  religious_heritage_by_birth: {value: "Jewish", certainty: 1.0, cites: [{source: S1, locator: "'Early life and career'"}, {source: S2, locator: "§1"}], how_known: "Two sources."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: "Talmud Torah school of the congregation", certainty: 1.0, cites: [{source: S2, locator: "§1, paragraph 1"}, {source: S1, locator: "'Early life and career', paragraph 3"}], how_known: "Two sources."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1661–1677", certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "From the Rijnsburg writings (correspondence begins 1661) to the posthumous works."}
  age_at_first_lasting_contribution: {value: 37, certainty: 0.7, cites: [{source: S1, locator: "opening (birth 1632)"}, {source: S2, locator: "§1 (TTP 1670)"}], how_known: "Born November 1632; TTP 1670. Follows the coder's choice of year."}
  first_evidence_of_lio_type_views: {value: "Herem of 1656, which SEP links to the ideas of his later treatises (denial of a transcendent, providential God)", year: 1656, age: 23, certainty: 0.5, cites: [{source: S2, locator: "§1, paragraph 2"}], how_known: "SEP calls this 'an educated guess'; the content of the 'abominable heresies' is not recorded. His own first dated texts on the question are the 1660s writings."}
  lio_views_relative_to_major_work: {value: "before major work", rationale: "Whatever the herem was for, the immanent God of the Short Treatise and the Ethics is present in the Rijnsburg writings of the early 1660s (S2, §1), before the TTP (1670) and the Ethics (1677).", certainty: 0.5, cites: [{source: S2, locator: "§1"}], how_known: "SEP dating of the works; the Short Treatise was not read."}
  worldview_during_major_work: {value: "PANT throughout (draft code)", certainty: 0.5, cites: [{source: S3, locator: "E1P15"}, {source: S4, locator: "TTP ch. 6"}], how_known: "The TTP and the Ethics, written in the major-work period, agree."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "The Ethics is set out in geometrical order (its title in S3: 'Ethica Ordine Geometrico Demonstrata'): definitions, axioms, propositions, demonstrations, with every proposition demonstrated from what precedes it (S2, §2.1; S3, title and Part I).", certainty: 1.0, cites: [{source: S2, locator: "§2.1"}, {source: S3, locator: "title; Part I definitions and axioms"}], how_known: "The text's own form."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "§1"}], how_known: "No source read says where he learned geometrical method; his Descartes exposition (1663) is also in geometrical form (not read)."}
  circle_present: {value: "yes", rationale: "God or Nature (E4 Preface), all things in God (E1P15), and human beings treated by the same method as lines and planes (E3 Preface): the entity applied to Nature and Nature rendered in the entity.", certainty: 0.7, cites: [{source: S3, locator: "E1P15; E3 Preface; E4 Preface"}], how_known: "His own text in an unofficial web copy; Nadler's ATHE-type reading is the named alternative."}
  reading: "As belief, not finding: form present (geometrical order), circle present (Deus sive Natura). Spinoza is the case the circle is named after, so the record cannot test H1; it only confirms the definition."
  notes: ""

institutions: []
collaborators:
  - {value: "René Descartes", roster_id: descartes-rene, relation: "influenced by", note: "Spinoza's only book under his own name was an exposition of Descartes's Principles (1663); his thought combines Cartesian principles with other sources (SEP)", certainty: 1.0, cites: [{source: S2, locator: "opening; §1"}], how_known: "SEP."}

review:
  roster_status_reason: {value: "Core in v8 (F 5: all five models).", certainty: 0.7, cites: [{source: S7, locator: "roster.csv, rank 11"}], how_known: "Study roster."}
  controversies:
    - {value: "Whether he is a pantheist or, in effect, an atheist: SEP (Nadler) argues against the pantheist label", certainty: 1.0, cites: [{source: S2, locator: "§2.1"}], how_known: "SEP sets out both sides."}
  data_quality_flags:
    - "Immortality: SEP says his treatises deny the immortality of the soul (§1); Britannica says he 'did not directly discuss the issue' and that his disbelief in individual immortality is clear only by implication. E5P23 ('something which is eternal') is the text both readings argue over."
    - "Worldview text read only in Project Gutenberg copies (unofficial); the Gutenberg TTP has at least one copy error (ch. 6, (19), 'fixed and mutable order')."
    - "Britannica read as its first page only."
  open_questions:
    - "Check the quoted Ethics and TTP passages against the Cambridge edition (Kisner) or a library scan of Elwes 1883 (Bohn's Chief Works) to lift the §7 cap on A, B, E; give printed page numbers."
    - "Read the Short Treatise and Letter 73 (to Oldenburg) for the date of his immanent God."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Richard H. Popkin"
    citation: "Popkin, Richard H. \"Benedict de Spinoza.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Benedict-de-Spinoza."
    url: "https://www.britannica.com/biography/Benedict-de-Spinoza"
    accessed: 2026-10-02
    reliability_note: "Signed article; first page only (to 'Excommunication'). Cited by section heading."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing]
  - id: S2
    type: secondary
    kind: encyclopedia
    author: "Steven Nadler"
    year: 2023
    citation: "Nadler, Steven. \"Baruch Spinoza.\" Stanford Encyclopedia of Philosophy (Fall 2023 ed.; substantive revision 8 Nov 2023). https://plato.stanford.edu/entries/spinoza/."
    url: "https://plato.stanford.edu/entries/spinoza/"
    accessed: 2026-10-02
    reliability_note: "Scholarly reference work by a leading Spinoza biographer; whole entry read. Cited by section."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, collaborators, review]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "Baruch Spinoza"
    year: 1677
    citation: "Spinoza, Benedict de. The Ethics (Ethica Ordine Geometrico Demonstrata). Translated by R. H. M. Elwes (1883). Project Gutenberg eBook 3800, https://www.gutenberg.org/ebooks/3800 (text read: https://www.gutenberg.org/cache/epub/3800/pg3800.txt)."
    url: "https://www.gutenberg.org/ebooks/3800"
    accessed: 2026-10-02
    reliability_note: "Public-domain translation in an unofficial web copy; under CODING_GUIDE §7 no field resting on it exceeds 0.7 until checked against the Cambridge edition (Kisner) or a library scan. Cited by part and proposition (E1P15 = Part I, Proposition 15); no page numbers."
    used_for: [worldview, timing, lane_b]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "Baruch Spinoza"
    year: 1670
    citation: "Spinoza, Benedict de. A Theologico-Political Treatise, Part 2 (chapters VI–X). Translated by R. H. M. Elwes (1883). Project Gutenberg eBook 990, https://www.gutenberg.org/ebooks/990."
    url: "https://www.gutenberg.org/ebooks/990"
    accessed: 2026-10-02
    reliability_note: "Unofficial web copy (§7 cap 0.7). Sentence numbers in parentheses were 'added by volunteer' (the file's own note) and are not in printed editions. Contains at least one copy error (ch. 6, (19))."
    used_for: [worldview, timing]
  - id: S5
    type: primary
    kind: "published work by the subject"
    author: "Baruch Spinoza"
    year: 1670
    citation: "Spinoza, Benedict de. A Theologico-Political Treatise, Part 3 (chapters XI–XV). Translated by R. H. M. Elwes (1883). Project Gutenberg eBook 991, https://www.gutenberg.org/ebooks/991."
    url: "https://www.gutenberg.org/ebooks/991"
    accessed: 2026-10-02
    reliability_note: "Unofficial web copy (§7 cap 0.7); volunteer sentence numbers."
    used_for: [worldview]
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "Baruch Spinoza"
    year: 1670
    citation: "Spinoza, Benedict de. A Theologico-Political Treatise, Part 1 (preface and chapters I–V). Translated by R. H. M. Elwes (1883). Project Gutenberg eBook 989, https://www.gutenberg.org/ebooks/989."
    url: "https://www.gutenberg.org/ebooks/989"
    accessed: 2026-10-02
    reliability_note: "Unofficial web copy (§7 cap 0.7); volunteer sentence numbers."
    used_for: [worldview]
  - id: S7
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
---

# Baruch Spinoza

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Bento (Baruch, Benedictus) Spinoza (1632–1677), Dutch philosopher of the Amsterdam Portuguese-Jewish community, wrote the Theological-Political Treatise (1670) and the Ethics (1677) [S1; S2]. In the Ethics God is the one substance, "God or Nature", in which everything is [S3, E1P15; E4 Preface]. Draft code PANT at 0.7, with ATHE as the named alternative [S2, §2.1]; all five axes are scored at or near the LIO pole, each at 0.7 because the texts were read in unofficial web copies. mid_basin false.

## Life and work

Born in Amsterdam to a merchant family; studies cut short at seventeen for the family business; excommunicated by the congregation in July 1656 [S2, §1; S1]. He lived at Rijnsburg, Voorburg and The Hague, grinding lenses, published his exposition of Descartes in 1663 and the Treatise anonymously in 1670, and died in The Hague in 1677 [S1; S2, §1].

## Contribution and impact

A monist metaphysics with a naturalistic psychology and ethics, set out in geometrical order [S2, §2], and a historical-critical reading of Scripture with an argument for freedom of thought [S2, §3].

## Childhood and education

His parents had been forcibly converted in Portugal and practised Judaism in secret before reaching Amsterdam, where his father became a director of the synagogue; his mother died in 1638 [S1, 'Early life and career']. He attended the congregation's Talmud Torah school but not its advanced levels [S2, §1].

## Adult working worldview

God is the only substance and "the indwelling and not the transient cause of all things" [S3, E1P14–E1P18]. Nothing is contingent [S3, E1P29], and a miracle against nature's laws would make God act against his own nature [S4, ch. 6]. God loves and hates no one, and blessedness is virtue itself, not its reward [S3, E5P17 Cor., E5P42]. Reason has the domain of truth; theology only that of obedience, with the one dogma that obedience saves learned from revelation [S5, ch. 15]. Nadler argues that this is naturalism rather than religious pantheism [S2, §2.1]; the record codes PANT on the S6 test and names ATHE as the alternative.

## Heritage (context only)

Portuguese-Jewish (Sephardic) Amsterdam [S1; S2]. Context only.

## Timing

First lasting contribution taken as the Treatise of 1670, at 37 [S2, §1]. The immanent God appears in the writings of the early 1660s [S2, §1]; the content of the 1656 heresies is not recorded.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Geometric form present (the Ethics) and the circle present (Deus sive Natura) [S2, §2.1; S3, E4 Preface]. Spinoza defines the circle, so he cannot test H1.

## Open questions

- Check the quotations against the Cambridge edition (Kisner) or a library scan of Elwes 1883 and add pages.
- Short Treatise and Letter 73 for the dating of his views.

## Research log

- 2026-10-02: Read SEP "Baruch Spinoza" (Nadler, whole entry) and Britannica (Popkin, first page). Read the Ethics (Gutenberg 3800) and the Theological-Political Treatise (Gutenberg 989, 990, 991) and copied quotations from those files. The Cambridge edition (Kisner) was not opened; no page numbers are given. Wikipedia not used.
