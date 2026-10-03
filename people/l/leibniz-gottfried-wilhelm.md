---
record:
  record_type: person
  schema_version: "1.2"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (executor agent for v8, RUNBOOK stage 3, batch A: early modern philosophers)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (stage 3, batch A). Basics from SEP 'Gottfried Wilhelm Leibniz' (Look) and Britannica (Belaval, first page); physics from SEP 'Leibniz's Philosophy of Physics' (McDonough). Worldview from the Theodicy (Huggard, Gutenberg) and the Monadology (Latta, Wikisource), both capped at 0.7 (§7), and Leibniz's First Paper to Clarke, read in page images of the 1717 first edition. DRAFT SCORES for v8's review: primary_system CLASS_THEISM 0.7; A 1, B 3, C 2, D 3, E 3, all at 0.7; mid_basin true (0.7). Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit fixes, stage 3 batch A (two blind runs at 59a8371). #287: German removed from languages_of_work (no German work in the sources read). #348: Mainz service 1667–1673 (Britannica: Boyneburg died Dec 1672, the Elector Feb 1673; he stayed in Paris until 1676). #291: how_known now says the 'ancestor' wording is in lasting. Britannica byline now Belaval and Look. #282 (with #341, #372) left: first-lasting year awaits v8 (P13 now in CODING_GUIDE §8). Not reviewed."}

identity:
  id: leibniz-gottfried-wilhelm
  display_name: "Gottfried Wilhelm Leibniz"
  roster:
    canonical_name: "Gottfried Wilhelm Leibniz"
    rank: 32
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: polymath
    field_bucket: polymath
  full_name: {value: "Gottfried Wilhelm Leibniz", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S3, locator: "opening"}], how_known: "Two sources."}
  native_name: {value: "Gottfried Wilhelm Leibniz", certainty: 0.7, cites: [{source: S3, locator: "opening"}], how_known: "German form as given; the 1717 edition spells it 'Leibnitz' (S6, title page)."}
  aliases:
    - {name: "Gottfried Leibniz", kind: "roster alias"}
    - {name: "Gottfried-Wilhelm-Leibniz", kind: "roster alias"}
    - {name: "Leibniz-Gottfried Wilhelm", kind: "roster alias"}
    - {name: "Leibnitz", kind: "other"}

basics:
  birth:
    date: {value: "1646-07-01", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S3, locator: "opening ('June 21 [July 1, New Style], 1646')"}], how_known: "Two sources; Britannica gives 21 June Old Style (Julian), 1 July New Style."}
    place: {value: "Leipzig", modern_name: "Leipzig, Saxony, Germany", polity_then: "Electorate of Saxony (Holy Roman Empire)", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S3, locator: "opening"}], how_known: "Two sources agree; polity is the coder's gloss."}
  death:
    date: {value: "1716-11-14", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S3, locator: "opening"}], how_known: "Two sources agree."}
    place: {value: "Hanover", modern_name: "Hanover, Lower Saxony, Germany", polity_then: "Electorate of Brunswick-Lüneburg (Hanover)", certainty: 1.0, cites: [{source: S3, locator: "opening"}, {source: S1, locator: "§1"}], how_known: "Britannica names Hanover; SEP says he spent his last years there. Polity is the coder's gloss."}
  first_lasting_contribution_year: {value: 1675, certainty: 0.7, cites: [{source: S3, locator: "'Early life and education' ('Late in 1675 Leibniz laid the foundations of both integral and differential calculus')"}], how_known: "Calculus, late 1675 (Britannica). De arte combinatoria (1666) is an earlier candidate; both years give the same era bucket."}
  era_bucket: {value: "1600 to 1749", certainty: 1.0, cites: [{source: S3, locator: "'Early life and education'"}], how_known: "From first_lasting_contribution_year (P2); 1666 gives the same bucket."}
  region_of_birth: {value: "Western Europe", certainty: 1.0, cites: [{source: S1, locator: "§1"}], how_known: "Germany is Western Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Western Europe", certainty: 1.0, cites: [{source: S1, locator: "§1 (Mainz, Paris, Hanover)"}], how_known: "Mainz, Paris (1672–1676) and Hanover."}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S1, locator: "§1"}], how_known: "As the sources record it."}
  languages_of_work: {value: [Latin, French], certainty: 0.7, cites: [{source: S1, locator: "§1; §1.1 (Latin and French titles)"}, {source: S6, locator: "First Paper (French original)"}], how_known: "Latin and French works in the sources. German was removed: no source read shows works by him in German (lens audit #287); add it back only with a source."}
  occupations: {value: [philosopher, mathematician, "political adviser", librarian, historian, "court councillor"], certainty: 1.0, cites: [{source: S3, locator: "opening"}, {source: S1, locator: "§1"}], how_known: "Britannica: 'German philosopher, mathematician, and political adviser'; SEP: librarian, historian and Privy Councillor at Hanover."}

contribution:
  fields: {value: [mathematics, metaphysics, logic, "natural philosophy", theology, law], certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S3, locator: "opening"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Differential and integral calculus, invented independently of Newton; first to publish", year: "1675", kind: method, lasting: "standard mathematics and notation", certainty: 1.0, cites: [{source: S3, locator: "opening; 'Early life and education'"}, {source: S1, locator: "§1"}], how_known: "Two sources."}
    - {value: "Dynamics: vis viva (mv²) as the measure of force, against the Cartesian quantity of motion (Brief Demonstration, 1686)", year: "1686", kind: concept or term, lasting: "ancestor of the conservation of kinetic energy", certainty: 0.7, cites: [{source: S2, locator: "§3.1"}], how_known: "SEP physics; the 'ancestor' wording in lasting is the coder's (flag)."}
    - {value: "Plan for a universal characteristic and logical calculus (De arte combinatoria)", year: "1666", kind: concept or term, lasting: "ancestor of symbolic logic and computing", certainty: 0.7, cites: [{source: S1, locator: "§1"}, {source: S3, locator: "'Early life and education'"}], how_known: "Two sources; Britannica calls it 'the theoretical ancestor of some modern computers'."}
    - {value: "Calculating machine performing the four arithmetic operations", year: "1673", kind: invention, lasting: "mechanical calculation", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S3, locator: "'Early life and education'"}], how_known: "Two sources."}
    - {value: "Monadology, pre-established harmony and the principle of sufficient reason", year: "1686–1714", kind: theory, lasting: "a main system of early modern rationalism", certainty: 1.0, cites: [{source: S1, locator: "§§3–5"}, {source: S3, locator: "opening"}], how_known: "Two sources."}
  evidence_of_impact:
    - {value: "One of the three great representatives of early modern rationalism, with Descartes and Spinoza", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S3, locator: "opening"}], how_known: "Britannica."}
  major_works:
    - {value: "Discourse on Metaphysics", year: 1686, kind: other, certainty: 1.0, cites: [{source: S1, locator: "§1.1"}], how_known: "SEP chronology."}
    - {value: "New Essays on Human Understanding (finished 1704, published 1765)", year: 1704, kind: book, certainty: 1.0, cites: [{source: S1, locator: "§1.1; §2"}], how_known: "SEP."}
    - {value: "Theodicy", year: 1710, kind: book, certainty: 1.0, cites: [{source: S1, locator: "§1.1; §2"}, {source: S4, locator: "title"}], how_known: "SEP and the text."}
    - {value: "Monadology", year: 1714, kind: other, certainty: 1.0, cites: [{source: S1, locator: "§1.1"}, {source: S5, locator: "title"}], how_known: "SEP and the text."}
    - {value: "Correspondence with Clarke (published by Clarke, 1717)", year: 1715, kind: other, certainty: 1.0, cites: [{source: S1, locator: "§1.1"}, {source: S6, locator: "title page"}], how_known: "SEP and the 1717 edition."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Co-inventor of the calculus; major metaphysician and logician.", certainty: 1.0, cites: [{source: S3, locator: "opening"}, {source: S1, locator: "§1"}], how_known: "Sources agree."}

childhood:
  family_religion: {value: "Lutheran", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S3, locator: "'Early life and education' ('a pious Lutheran family')"}], how_known: "Two sources."}
  family_religious_practice: {value: "Pious Lutheran", certainty: 0.7, cites: [{source: S3, locator: "'Early life and education'"}], how_known: "Britannica only."}
  parents_and_household:
    - {value: "Father, Friedrich Leibniz, jurist and professor of moral philosophy at Leipzig; died 1652", name: "Friedrich Leibniz", role: father, certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S3, locator: "'Early life and education'"}], how_known: "Two sources."}
    - {value: "Mother, Catharina Schmuck, daughter of a professor of law; directed his education after 1652", name: "Catharina Schmuck", role: mother, certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
  household_circumstances: {value: "Educated elite family on both sides; after his father's death in 1652 his education was directed by his mother, an uncle and himself, with free use of his father's library", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S3, locator: "'Early life and education'"}], how_known: "Two sources."}
  schooling:
    - {value: "Nicolai School, Leipzig", stage: "grammar or secondary school", years: "before 1661", certainty: 0.7, cites: [{source: S3, locator: "'Early life and education'"}], how_known: "Britannica only."}
    - {value: "Largely self-taught in his father's library (ancient history, Church Fathers)", stage: "self-directed", years: "1650s", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S3, locator: "'Early life and education'"}], how_known: "Two sources."}
    - {value: "University of Leipzig (law; chiefly Scholastic philosophy), baccalaureate thesis De principio individui (1663)", stage: university, years: "1661–1666", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S3, locator: "'Early life and education'"}], how_known: "Two sources."}
    - {value: "University of Altdorf, doctorate of law", stage: university, years: "1666–1667", certainty: 0.7, cites: [{source: S1, locator: "§1 (1667)"}, {source: S3, locator: "'Early life and education'"}], how_known: "SEP dates the doctorate 1667; Britannica says he finished legal studies in 1666 and took the Altdorf degree 'at once'."}
  early_mathematics: {value: UNKNOWN, how_known: "Checked SEP §1 and Britannica's first page: neither says what mathematics he learned as a child; SEP says he studied the moderns' mathematics properly only in Paris with Huygens (1672–1676)."}
  early_geometric_style_reasoning: {value: "Scholastic logic at Leipzig; De arte combinatoria (1666) at twenty", certainty: 0.5, cites: [{source: S1, locator: "§1"}], how_known: "SEP; the link to geometric-style reasoning is the coder's reading."}
  early_science_exposure:
    - {value: "Contact at Leipzig with the thought of Galileo, Bacon, Hobbes and Descartes", year: "1661–1666", age: "15–20", certainty: 0.5, cites: [{source: S3, locator: "'Early life and education'"}, {source: S1, locator: "§1"}], how_known: "Britannica says he came into contact with them; SEP says the moderns had not yet made a great impact in German lands, so 0.5."}
  key_early_reading:
    - {value: "Ancient history and the Church Fathers in his father's library", certainty: 1.0, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
  childhood_mentors: []
  languages_in_childhood: {value: [German, Latin], certainty: 0.5, cites: [{source: S3, locator: "'Early life and education'"}], how_known: "German home and Latin schooling are the coder's inference from the Nicolai School and the library; not stated."}
  notable_events:
    - {value: "Father's death", year: "1652", age: 6, certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S3, locator: "'Early life and education'"}], how_known: "Two sources."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1666–1716", certainty: 1.0, cites: [{source: S1, locator: "§1"}], how_known: "De arte combinatoria to his death."}
  nominal_affiliations:
    - {value: "Lutheran (worked for Protestant–Catholic reunion)", certainty: 0.7, cites: [{source: S1, locator: "§1 ('lifelong irenicism')"}, {source: S3, locator: "'Early life and education'"}], how_known: "Lutheran family; SEP and Britannica on his reunion work. His own adult confession is not stated in the pages read."}
  self_described_science_religion_relation:
    value: "Faith and reason cannot conflict: 'two truths cannot contradict each other' (Theodicy, Preliminary Dissertation §1). The laws of nature are positive truths God chose and can dispense with by a miracle, but the eternal truths 'admit no dispensation, and faith cannot contradict them' (§3). Mysteries are above reason, never against it, and a dogma refuted by reason is absurd (§23). God works miracles 'not [...] to supply the Wants of Nature, but those of Grace' (First Paper to Clarke, §4)."
    certainty: 0.7
    cites: [{source: S4, locator: "Preliminary Dissertation §§1, 3, 23"}, {source: S6, locator: "First Paper §4, p. 7"}]
    how_known: "His own published text in an unofficial copy (§7 cap) and the 1717 edition."
  primary_system:
    value: CLASS_THEISM
    basis: written_profession
    certainty: 0.7
    cites: [{source: S5, locator: "§§38, 45, 47"}, {source: S4, locator: "Preliminary Dissertation §§2–3"}, {source: S1, locator: "§7.1"}]
    how_known: "His own published and finished texts in unofficial web copies (§7) and SEP; capped at 0.7 by §7 and by a named alternative."
    rationale: "DRAFT. Meets the three CLASS_THEISM use_when tests in his own words: (1) argues to God by reason, a posteriori from contingent beings ('the final reason of things must be in a necessary substance [...] and this substance we call God', Monadology §38) and a priori (§45; SEP §7.1 on his ontological argument); (2) God simple: 'God alone is the primary unity or original simple substance' (§47); (3) nature a lawful order God chose ('the laws which it has pleased God to give to Nature', Theodicy PD §2). The v7.1 scoring note on CLASS_THEISM names Leibniz. Differences flagged in the system file: he affirms a best possible world, which Aquinas denies. Named alternative: CHRIST (Lutheran family; accepts revelation founded on miracles, PD §1). DEISM, which the system file asks to check, is ruled out by DEISM's own do_not_use_when: he accepts revelation and miracles (PD §§1, 3)."
  secondary_system: {value: UNKNOWN, how_known: "No second system in the sources read."}
  candidate_codes_considered:
    - {code: CLASS_THEISM, reason: "Coded (DRAFT, 0.7): God reached by reason, simple, choosing a lawful order. The v7.1 note names him.", cites: [{source: S5, locator: "§§38, 47"}, {source: S4, locator: "Preliminary Dissertation §2"}]}
    - {code: CHRIST, reason: "Named alternative: Lutheran; revelation rests on witnessed miracles (PD §1); worked for church reunion (S1 §1). Not coded: the CHRIST file's own guidance sends a philosophical God of reason to CLASS_THEISM.", cites: [{source: S4, locator: "Preliminary Dissertation §1"}, {source: S1, locator: "§1"}]}
    - {code: DEISM, reason: "Considered (asked by the CLASS_THEISM file) and rejected: a clockwork-like God who does not intervene in nature, but he accepts revelation and miracles for grace (PD §3; First Paper §4), which DEISM's do_not_use_when excludes.", cites: [{source: S4, locator: "Preliminary Dissertation §3"}, {source: S6, locator: "First Paper §4"}]}
    - {code: RATN, reason: "Considered: Britannica calls him a great representative of rationalism. Not coded: RATN is a stub system file and names an epistemology, not a God-world metaphysics (same flag as Descartes).", cites: [{source: S3, locator: "opening"}]}
  lio_axes:
    A_locus:
      value: 1
      basis: written_profession
      certainty: 0.7
      cites: [{source: S5, locator: "§§38, 47, 85"}]
      how_known: "His own text in an unofficial copy (§7); a named alternative (0)."
      rationale: "DRAFT. Leans to the transcendent-person pole: God is a necessary substance outside the series of contingent things (Monadology §38), with power, knowledge and will (§48), 'the most perfect of Monarchs' of the City of God (§85). The immanence feature: all created monads 'have their birth, so to speak, through continual fulgurations of the Divinity from moment to moment' (§47). Same pattern as Aquinas and Newton (1). Named alternative: 0."
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.7
      cites: [{source: S6, locator: "First Paper §4, pp. 5–7"}, {source: S4, locator: "Preliminary Dissertation §§2–3"}, {source: S5, locator: "§§79–81"}, {source: S1, locator: "§4.5"}]
      how_known: "His own texts: the 1717 edition read in page images, the Theodicy and Monadology in unofficial copies (§7); a named alternative (4)."
      rationale: "DRAFT. Scored on his account of nature (P6). Leans LIO: 'the same Force and Vigour remains always in the World, and only passes from one part of Matter to another, agreeably to the Laws of Nature, and the beautiful pre-established Order' (First Paper §4), and he mocks the view that God must 'wind up his Watch from Time to Time'; bodies act by efficient causes 'as if there were no souls' (Monadology §§79–81; SEP §4.5: 'all corporeal phenomena can be derived from efficient and mechanical causes'). The stated, limited exception: God 'can exempt creatures from the laws he has prescribed for them [...] by performing a miracle' (PD §3), but only for grace, not nature (First Paper §4). Same pattern as Aquinas (B 3). Named alternative: 4, since miracles never serve nature's needs."
    C_ledger:
      value: 2
      basis: written_profession
      certainty: 0.7
      cites: [{source: S5, locator: "§§88–90"}, {source: S4, locator: "Preface"}]
      how_known: "His own texts in unofficial copies (§7); named alternatives (1 and 3)."
      rationale: "DRAFT, judgment call. Both features at once. Consequence: 'sins must bear their penalty with them, through the order of nature, and even in virtue of the mechanical structure of things' (Monadology §89). Personal: God as Lawgiver and Monarch sees that 'no good action would be unrewarded and no bad one unpunished' (§90), the globe is renewed 'for the punishment of some and the reward of others' (§88), and the Theodicy's Preface weighs 'the glory of all the saved' against 'the misery of all the damned'. A personal ledger delivered through natural means, so 2. Named alternatives: 3 (penalty by the order of nature) and 1 (damnation affirmed)."
    D_authority:
      value: 3
      basis: written_profession
      certainty: 0.7
      cites: [{source: S4, locator: "Preliminary Dissertation §§1, 3, 23, 25"}]
      how_known: "His own published text in an unofficial copy (§7); a named alternative (2)."
      rationale: "DRAFT. Leans to reason: faith cannot contradict the eternal truths (PD §3); 'a truth can never be contrary to reason, and once a dogma has been disputed and refuted by reason, [...] nothing is easier to understand, nor more obvious, than its absurdity' (§23); a truly irrefutable objection would show 'that the falsity of this thesis is demonstrated' (§25). The stated exception: mysteries 'above reason' (the Trinity, creation, the choice of the best order, §23) are held on revelation, which rests on witnessed miracles and tradition (§1). Same pattern as Ibn Sina (D 3: demonstration decides; some articles on authority). Named alternative: 2 (two sources, each with its domain)."
    E_scope:
      value: 3
      basis: written_profession
      certainty: 0.7
      cites: [{source: S5, locator: "§§79, 87–88"}, {source: S6, locator: "First Paper §4, p. 7"}]
      how_known: "His own texts (§7 cap on the Monadology; page images for the 1717 edition); a named alternative (4)."
      rationale: "DRAFT. Scored on the world's order (P7). Leans LIO: one pre-established harmony covers every body and soul (Monadology §§79–81), and the realm of grace runs 'by the very ways of nature' (§88). The stated, limited exception: miracles worked for 'the Wants [...] of Grace' (First Paper §4), i.e. events for the sake of spirits. The City of God as a moral community is a C matter (P7). Named alternative: 4."
  mid_basin: {value: true, certainty: 0.7, cites: [{source: S5, locator: "§§38, 47"}, {source: S6, locator: "First Paper §4"}], how_known: "P4/P6 test: A_locus 1 (0.7) ≤ 1 and B_cause 3 (0.7) ≥ 3, both at ≥ 0.7, so true. Certainty is the lower of the two (0.7). DRAFT: A 0 or B 4 (the named alternatives) would not change the result."}
  statements:
    - text: "According to their Doctrine, God Almighty wants to wind up his Watch from Time to Time : Otherwise it would cease to move."
      cites: [{source: S6, locator: "First Paper §4, p. 5"}]
      date: "1715"
      context: "Leibniz's First Paper (the exchange is dated 1715–1716 on the title page), on Newton and his followers; Clarke's English, read in the page image of the 1717 edition. Long s printed as s, italics dropped and the line-end hyphen in Other-wise joined; spacing as printed."
      axes: [B_cause]
      kind: "other"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
    - text: "According to My Opinion, the same Force and Vigour remains always in the World, and only passes from one part of Matter to another, agreeably to the Laws of Nature, and the beautiful pre-established Order. And I hold, that when God works Miracles, he does not do it in order to supply the Wants of Nature, but those of Grace. Whoever thinks otherwise, must needs have a very mean Notion of the Wisdom and Power of God."
      cites: [{source: S6, locator: "First Paper §4, pp. 5–7"}]
      date: "1715"
      context: "Same paragraph; English on pp. 5 and 7, the French original on p. 6 ('Et je tiens, quand Dieu fait des Miracles, que ce n'est pas pour soutenir les besoins de la Nature, mais pour ceux de la Grace'). Long s printed as s; footnote marks dropped."
      axes: [B_cause, E_scope]
      kind: "other"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
    - text: "Thus it is made clear that God can exempt creatures from the laws he has prescribed for them, and produce in them that which their nature does not bear by performing a miracle."
      cites: [{source: S4, locator: "Preliminary Dissertation §3"}]
      date: "1710"
      context: "Theodicy, Preliminary Dissertation on the Conformity of Faith with Reason."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "Nevertheless it still remains true that the laws of Nature are subject to be dispensed from by the Law-giver; whereas the eternal verities, as for instance those of geometry, admit no dispensation, and faith cannot contradict them."
      cites: [{source: S4, locator: "Preliminary Dissertation §3"}]
      date: "1710"
      context: "Same section."
      axes: [B_cause, D_authority]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "But a truth can never be contrary to reason, and once a dogma has been disputed and refuted by reason, instead of its being incomprehensible, one may say that nothing is easier to understand, nor more obvious, than its absurdity."
      cites: [{source: S4, locator: "Preliminary Dissertation §23"}]
      date: "1710"
      context: "After distinguishing what is above reason (the Trinity, creation) from what is against it."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "Thus God alone is the primary unity or original simple substance, of which all created or derivative Monads are products and have their birth, so to speak, through continual fulgurations of the Divinity from moment to moment, limited by the receptivity of the created being, of whose essence it is to have limits."
      cites: [{source: S5, locator: "§47"}]
      date: "1714"
      context: "Monadology, Latta's 1898 translation. Written 1714, published after his death; the date is of writing (S1 §1.1)."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "It may also be said that God as Architect satisfies in all respects God as Lawgiver, and thus that sins must bear their penalty with them, through the order of nature, and even in virtue of the mechanical structure of things"
      cites: [{source: S5, locator: "§89"}]
      date: "1714"
      context: "Monadology, on the harmony of the realms of nature and grace."
      axes: [C_ledger]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "Finally, under this perfect government no good action would be unrewarded and no bad one unpunished"
      cites: [{source: S5, locator: "§90"}]
      date: "1714"
      context: "Monadology, the City of God."
      axes: [C_ledger]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
  changes_over_life: []
  coder_notes: "DRAFT SCORES for v8's review. The Theodicy (Huggard) and the Monadology (Latta) were read in unofficial web copies, so §7 caps them at 0.7. Leibniz's First Paper to Clarke was read in page images of the 1717 first edition (Internet Archive, Wellcome Library copy b30520022), in Clarke's English with the French facing; that is a primary facsimile, but the axes it supports also rest on the capped texts. The Monadology was not published in his lifetime; kind 'written profession (public)' is used because it was a finished treatise written for others (flag). The Gutenberg Theodicy carries page markers from the Open Court edition; they are not used as locators."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "German; Leipzig academic and legal elite", certainty: 1.0, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
  religious_heritage_by_birth: {value: "Lutheran", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S3, locator: "'Early life and education'"}], how_known: "Two sources."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1666–1716", certainty: 1.0, cites: [{source: S1, locator: "§1; §1.1"}], how_known: "SEP chronology."}
  age_at_first_lasting_contribution: {value: 29, certainty: 0.7, cites: [{source: S3, locator: "'Early life and education'"}], how_known: "Born July 1646; calculus late 1675. If De arte combinatoria (1666) is used, 19 or 20."}
  first_evidence_of_lio_type_views: {value: "Principle of sufficient reason ('nothing exists or occurs without a reason') developed while working on the Demonstrationes Catholicae at Mainz", year: 1668, age: 22, certainty: 0.5, cites: [{source: S3, locator: "'Early life and education'"}], how_known: "Britannica dates the Mainz work to before the 1671 Hypothesis physica nova; the year 1668 is the coder's estimate from the start of his Mainz service (flag)."}
  lio_views_relative_to_major_work: {value: "during major work", rationale: "The principle of sufficient reason appears at Mainz (late 1660s); the lawful order is fully stated in 1686–1714.", certainty: 0.5, cites: [{source: S3, locator: "'Early life and education'"}, {source: S1, locator: "§1.1"}], how_known: "Dates of what was read."}
  worldview_during_major_work: {value: "CLASS_THEISM throughout (draft code)", certainty: 0.5, cites: [{source: S4, locator: "Preliminary Dissertation"}, {source: S5, locator: "§§38–47"}], how_known: "Theodicy (1710) and Monadology (1714) agree; earlier works not read."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "Reason is 'the linking together of truths' and the eternal verities 'of geometry, admit no dispensation' (PD §§1, 3); a calculus of reasoning from De arte combinatoria on (S1 §1).", certainty: 0.7, cites: [{source: S4, locator: "Preliminary Dissertation §§1, 3"}, {source: S1, locator: "§1"}], how_known: "His own text in an unofficial copy, and SEP."}
  form_acquired: {value: "adulthood, before major work", certainty: 0.5, cites: [{source: S1, locator: "§1"}], how_known: "Scholastic logic at university and De arte combinatoria at twenty; no source on childhood mathematics."}
  circle_present: {value: "partly", rationale: "One harmonious order with nature and grace in step (Monadology §§87–88), but God is a monarch outside the series of things (§38), not identified with Nature.", certainty: 0.5, cites: [{source: S5, locator: "§§38, 87–88"}], how_known: "Coder's reading."}
  reading: "As belief, not finding: form present, circle partial (one order, transcendent author). He met Spinoza in 1676 and discussed the Ethics, then built a system that keeps God outside nature."
  notes: ""

institutions:
  - {value: "Court of the Elector of Mainz", role: "legal and political adviser; diplomat to Paris", years: "1667–1673", kind: "government or state body", certainty: 0.7, cites: [{source: S1, locator: "§1"}, {source: S3, locator: "'Early life and education'"}], how_known: "Start: SEP (Boineburg secured the post in 1667). End: Britannica says he was 'left without protectors by the deaths of Freiherr von Boyneburg in December 1672 and of the prince elector in February 1673'; SEP says only that his employer died while he was in Paris. He stayed in Paris, looking for another post, until 1676, when he went to Hanover (S1 §1). Lens audit #348: was 1667–1676."}
  - {value: "Court of Hanover (House of Brunswick)", role: "librarian, historian, Privy Councillor", years: "1676–1716", kind: employer, certainty: 1.0, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
collaborators:
  - {value: "Christiaan Huygens", roster_id: huygens-christiaan, relation: "mentor or employer", note: "tutored him in philosophy, physics and mathematics in Paris", certainty: 1.0, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
  - {value: "Baruch Spinoza", roster_id: spinoza-baruch, relation: other, note: "met him in Amsterdam, 18–21 November 1676; discussed the Ethics", certainty: 1.0, cites: [{source: S1, locator: "§1; §7.1"}], how_known: "SEP."}
  - {value: "Antoine Arnauld", relation: correspondent, note: "met in Paris 1672; correspondence from 1686", certainty: 1.0, cites: [{source: S1, locator: "§1; §1.1"}, {source: S3, locator: "'Early life and education'"}], how_known: "Two sources."}
  - {value: "Isaac Newton", roster_id: newton-isaac, relation: "rival or critic", note: "calculus priority dispute; natural theology dispute through Clarke", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S6, locator: "First Paper §4"}], how_known: "SEP and the 1717 edition."}
  - {value: "Samuel Clarke", relation: "rival or critic", note: "exchange of papers 1715–1716", certainty: 1.0, cites: [{source: S6, locator: "title page"}, {source: S1, locator: "§1.1"}], how_known: "The 1717 edition and SEP."}
  - {value: "Jacob Thomasius", relation: teacher, note: "supervised De principio individui at Leipzig", certainty: 1.0, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
  - {value: "Blaise Pascal", roster_id: pascal-blaise, relation: "influenced by", note: "reading Pascal's mathematical manuscripts in Paris led him toward the differential calculus (his own account)", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP, reporting Leibniz's account."}

review:
  roster_status_reason: {value: "Core in v8 (F 5: all five models); field tie across models.", certainty: 0.7, cites: [{source: S7, locator: "roster.csv, rank 32"}], how_known: "Study roster."}
  controversies:
    - {value: "Calculus priority dispute with Newton", certainty: 1.0, cites: [{source: S1, locator: "§1"}], how_known: "SEP: most historians hold the two developed it independently, Newton first, Leibniz first to publish."}
  data_quality_flags:
    - "Birth date: 21 June Old Style / 1 July New Style 1646 (Britannica); SEP gives July 1."
    - "Altdorf doctorate: 1667 (SEP) vs 1666 (Britannica)."
    - "Theodicy and Monadology read only in Gutenberg and Wikisource copies."
    - "Britannica read as its first page only."
  open_questions:
    - "Check the Theodicy and Monadology quotations against Gerhardt (G VI) and give page numbers; that would lift the §7 cap."
    - "Settle whether CLASS_THEISM covers a best-possible-world rational theism (the CLASS_THEISM file's own open item)."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Brandon C. Look"
    year: 2013
    citation: "Look, Brandon C. \"Gottfried Wilhelm Leibniz.\" Stanford Encyclopedia of Philosophy (substantive revision 24 Jul 2013). https://plato.stanford.edu/entries/leibniz/."
    url: "https://plato.stanford.edu/entries/leibniz/"
    accessed: 2026-10-02
    reliability_note: "Scholarly reference work; §1, §4.5 and §7.1 read closely. Cited by section."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators, review]
  - id: S2
    type: secondary
    kind: encyclopedia
    author: "Jeffrey K. McDonough"
    year: 2024
    citation: "McDonough, Jeffrey K. \"Leibniz's Philosophy of Physics.\" Stanford Encyclopedia of Philosophy (substantive revision 26 Jul 2024). https://plato.stanford.edu/entries/leibniz-physics/."
    url: "https://plato.stanford.edu/entries/leibniz-physics/"
    accessed: 2026-10-02
    reliability_note: "Scholarly reference work; §3 read. Cited by section."
    used_for: [contribution]
  - id: S3
    type: tertiary
    kind: encyclopedia
    author: "Yvon Belaval and Brandon C. Look"
    citation: "Belaval, Yvon, and Brandon C. Look. \"Gottfried Wilhelm Leibniz.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Gottfried-Wilhelm-Leibniz."
    url: "https://www.britannica.com/biography/Gottfried-Wilhelm-Leibniz"
    accessed: 2026-10-02
    reliability_note: "Signed article; first page only. Cited by section heading."
    used_for: [identity, basics, contribution, childhood, worldview, timing, institutions, collaborators]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "Gottfried Wilhelm Leibniz"
    year: 1710
    citation: "Leibniz, G. W. Theodicy: Essays on the Goodness of God, the Freedom of Man and the Origin of Evil. Edited by Austin Farrer, translated by E. M. Huggard from Gerhardt's edition. La Salle, IL: Open Court. Project Gutenberg eBook 17147, https://www.gutenberg.org/ebooks/17147."
    url: "https://www.gutenberg.org/ebooks/17147"
    accessed: 2026-10-02
    reliability_note: "Unofficial web copy of a modern translation; capped at 0.7 under CODING_GUIDE §7. Cited by section of the Preliminary Dissertation."
    used_for: [worldview, timing, lane_b]
  - id: S5
    type: primary
    kind: "published work by the subject"
    author: "Gottfried Wilhelm Leibniz"
    year: 1714
    citation: "Leibniz, G. W. The Monadology. Translated by Robert Latta (1898). Wikisource, https://en.wikisource.org/wiki/Monadology_(Leibniz,_tr._Latta)."
    url: "https://en.wikisource.org/wiki/Monadology_(Leibniz,_tr._Latta)"
    accessed: 2026-10-02
    reliability_note: "Wikisource transcription without page scans; capped at 0.7 under §7. Cited by section number."
    used_for: [worldview, timing, lane_b]
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "Gottfried Wilhelm Leibniz and Samuel Clarke"
    year: 1717
    citation: "A Collection of Papers, Which passed between the late Learned Mr. Leibnitz, and Dr. Clarke, In the Years 1715 and 1716. Relating to the Principles of Natural Philosophy and Religion. London: Printed for J. Knapton, 1717. Internet Archive scan (Wellcome Library), https://archive.org/details/b30520022."
    url: "https://archive.org/details/b30520022"
    accessed: 2026-10-02
    reliability_note: "First edition, French with Clarke's English facing; quotations read in the page images of pp. 5–7 (leaves n24–n26). Cited by paper, section and printed page."
    used_for: [identity, basics, worldview, collaborators]
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

# Gottfried Wilhelm Leibniz

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Gottfried Wilhelm Leibniz (1646–1716), German philosopher, mathematician and court adviser, invented the calculus independently of Newton and built one of the main rationalist systems [S1; S3]. His God is a necessary, simple substance reached by reason, who chose a lawful order and works miracles only for grace [S5, §§38, 47; S6, First Paper §4]. Draft code CLASS_THEISM at 0.7. Axes A 1, B 3, C 2, D 3, E 3, all at 0.7; mid_basin true at 0.7 (draft).

## Life and work

Leipzig and Altdorf (law), Mainz, Paris (1672–1676, with Huygens), then Hanover as librarian, historian and councillor until his death [S1, §1; S3].

## Contribution and impact

Calculus, dynamics (vis viva), logic and the calculating machine; the Monadology and the Theodicy [S1; S2, §3; S3].

## Childhood and education

His father died when he was six; he taught himself in his father's library, then studied law at Leipzig and Altdorf [S1, §1; S3].

## Adult working worldview

Faith and reason cannot conflict; the laws of nature are chosen by God and dispensable by miracle, but the eternal truths are not [S4, PD §§1–3, 23]. He rejected the view that God must "wind up his Watch from Time to Time" [S6, p. 5].

## Heritage (context only)

Pious Lutheran academic family in Leipzig [S1; S3]. Context only.

## Timing

First lasting contribution taken as the calculus of 1675 [S3].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form present; circle partial [S4; S5].

## Open questions

- Check Theodicy and Monadology against Gerhardt.

## Research log

- 2026-10-02: Read SEP "Gottfried Wilhelm Leibniz" (Look, §§1, 4.5, 7.1), SEP "Leibniz's Philosophy of Physics" (McDonough, §3), Britannica (Belaval, first page), the Theodicy (Gutenberg 17147, Preface and Preliminary Dissertation), the Monadology (Latta, Wikisource), and the 1717 Clarke edition (IA b30520022, page images of pp. 5–7). Wikipedia not used.
- 2026-10-02 (lens audit fixes): Re-read Britannica "Early life and education" for the end of the Mainz service (#348).
