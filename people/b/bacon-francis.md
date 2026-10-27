---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch E)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to philosophy. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch E, order P32: F 5, rank 26). Basics from Britannica (Urbach et al.). Worldview from The Advancement of Learning (1605), Morley's 1893 Cassell edition as transcribed by Project Gutenberg (#5500), and 'Of Atheism' (Essays, Gutenberg #575). Not a scientist (P30, P33). CHRIST 0.7; A 0 (0.7); B 3 (0.7); D 2 (0.7); mid_basin true (0.7). Draft, not reviewed."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Audit fixes (fallacy_catalog audit of 2332880, run 1): Gutenberg statements relabelled verified_against 'secondary quotation' (web copies); certainties already at the 0.7 web-copy cap, so no change and mid_basin true (0.7) stands. II.XXV.(3) confirmed as D_authority evidence only (it was not cited under B_cause)."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #26, next-50 batch). Need was A single-source. Added Confession of Faith (S5; Spedding Works scholarly edition via Wikisource) as second A stream; Advancement quotes checked against Spedding 1884 Works Vol. 1 (S6 scholarly edition; pp. 291–292, 322–323, 367). SEP Peltonen 2025 (S7) for bio/family. P47 source_quality on every source. A_locus support single→corroborated (S6+S5; value 0 @ 0.7 written_profession unchanged; alt 1). B_cause stays 3 @ 0.7 corroborated (S6+S3; alt 4). CHRIST / D / mid_basin unchanged at 0.7 (named alts / P10). Chart-moving YES: A hollow→filled with B already corroborated → filled mid-basin dark. Family_religion filled (Puritan/Protestant household). No fallacy_catalog (Jason 2026-10-23/24). Draft, not reviewed."}

identity:
  id: bacon-francis
  display_name: "Francis Bacon"
  roster:
    canonical_name: "Francis Bacon"
    rank: 26
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: philosophy
    field_bucket: philosophy
  full_name: {value: "Francis Bacon, Viscount Saint Alban", certainty: 0.7, cites: [{source: S1, locator: "header ('Also known as')"}], how_known: "Britannica alone."}
  native_name: {value: UNKNOWN, how_known: "English; no different native-script name."}
  aliases:
    - {name: "Bacon-Francis", kind: "roster alias"}
    - {name: "Francis-Bacon", kind: "roster alias"}

basics:
  birth:
    date: {value: "1561-01-22", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "At a Glance; 'Youth and early maturity'"}], how_known: "Britannica alone."}
    place: {value: "York House, London, England", modern_name: "London, United Kingdom", polity_then: "Kingdom of England", certainty: 0.7, cites: [{source: S1, locator: "At a Glance"}], how_known: "Britannica alone."}
  death:
    date: {value: "1626-04-09", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "At a Glance; 'Fall from power'"}], how_known: "Britannica alone."}
    place: {value: "London (the earl of Arundel's house near Highgate)", modern_name: "London, United Kingdom", polity_then: "Kingdom of England", certainty: 0.7, cites: [{source: S1, locator: "'Fall from power', last paragraph"}], how_known: "Britannica alone."}
  first_lasting_contribution_year: {value: 1605, certainty: 0.7, cites: [{source: S1, locator: "'Career in the service of James I' ('In the autumn of 1605 he published his Advancement of Learning')"}], how_known: "Earliest listed lasting contribution (P13). Earlier Essayes editions exist (S1 calls the 1625 edition the 'third and enlarged'), but no source read dates the first, so it does not set the year (P12); the true year may be earlier."}
  era_bucket: {value: "1600 to 1749", certainty: 0.7, cites: [{source: S1, locator: "'Career in the service of James I'"}], how_known: "From 1605 (P2). If the undated first Essayes edition were before 1600 the bucket would be '1400 to 1599'."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "At a Glance"}], how_known: "United Kingdom (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "career sections"}], how_known: "London."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [English, Latin], certainty: 0.7, cites: [{source: S1, locator: "'Fall from power' (De Augmentis, a Latin translation)"}], how_known: "Britannica."}
  occupations: {value: ["lawyer", "statesman (lord chancellor)", "philosopher", "essayist"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

contribution:
  primary_domain: philosophy
  fields: {value: ["philosophy of science (method)", "essays", "political and legal thought"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "The Advancement of Learning: survey and classification of knowledge", year: 1605, kind: work, lasting: "expanded as De Augmentis (1623); d'Alembert's classification drew on it (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Career in the service of James I'"}], how_known: "Britannica."}
    - {value: "Novum Organum: an inductive method for natural knowledge", year: 1620, kind: method, lasting: "revered by Hooke and Boyle and the Royal Society founders; 'a symbol for the idea that science is inductive' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Fall from power' ('the Novum Organum, published in 1620')"}], how_known: "Britannica. A method, not a theory or result about natural systems, so Bacon is not a scientist under P30 #11 and P33."}
    - {value: "Essayes (third, enlarged edition)", year: 1625, kind: work, lasting: "he is 'remembered in literary terms for the sharp worldly wisdom of a few dozen essays' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Fall from power'"}], how_known: "Britannica dates the third edition; earlier editions undated in the source read."}
  evidence_of_impact:
    - {value: "Kant dedicated the Critique of Pure Reason to Bacon; Darwin acknowledged his influence", kind: "assessment by a later major figure", certainty: 0.7, cites: [{source: S1, locator: "body (influence)"}], how_known: "Britannica article body (not the AI boxes)."}
  major_works:
    - {value: "De Sapientia Veterum", year: 1609, kind: book, certainty: 0.7, cites: [{source: S1, locator: "'Career in the service of James I'"}], how_known: "Britannica."}
    - {value: "New Atlantis", year: 1626, kind: book, certainty: 0.7, cites: [{source: S1, locator: "'Career in the service of James I' (written c. 1614, printed 1626)"}], how_known: "Britannica."}
  honours:
    - {value: "Lord chancellor and Baron Verulam (1618); Viscount St. Albans (1620/21)", year: 1618, certainty: 0.7, cites: [{source: S1, locator: "'Career in the service of James I'"}], how_known: "Britannica."}
  definition_fit: {value: "clearly meets", rationale: "Lasting influence on scientific method and English prose.", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "Protestant (Church of England); mother Anne Cooke Bacon of a noted Protestant/Puritan reforming household", certainty: 0.7, cites: [{source: S7, locator: "§1; §8"}, {source: S1, locator: "'Youth and early maturity'"}], how_known: "SEP: second wife Anne, daughter of Sir Anthony Cooke; scholarship notes Puritan background of his mother (S7 §8). Britannica names Sir Nicholas and the Cambridge/Whitgift household."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father, Sir Nicholas Bacon, lord keeper of the great seal; younger of two sons of his second marriage", name: "Nicholas Bacon", role: father, certainty: 0.7, cites: [{source: S1, locator: "'Youth and early maturity'"}], how_known: "Britannica."}
  household_circumstances: {value: "Household of a high officer of state; cousin of Robert Cecil", certainty: 0.7, cites: [{source: S1, locator: "'Youth and early maturity'"}], how_known: "Britannica."}
  schooling:
    - {value: "Trinity College, Cambridge", stage: university, years: "1573–1575", ages: "12–14", certainty: 0.7, cites: [{source: S1, locator: "'Youth and early maturity'"}], how_known: "Britannica; ages = year − 1561 (P30)."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: TODO}
  notable_events:
    - {value: "Distaste for 'unfruitful' Aristotelian philosophy began at Cambridge", year: 1573, age: 12, certainty: 0.7, cites: [{source: S1, locator: "'Youth and early maturity'"}], how_known: "Britannica; year is the start of his Cambridge stay."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1605–1625", certainty: 0.7, cites: [{source: S1, locator: "career sections"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "Two books, 'the book of God's word, or [...] the book of God's works, divinity or philosophy': study both without end, but do not 'unwisely mingle or confound these learnings together' (1605).", certainty: 0.7, cites: [{source: S6, locator: "Book I (1884 Works Vol. 1, p. 292)"}, {source: S2, locator: "Book I, I.(3)"}], how_known: "Published work (written_profession). Wording checked against Spedding/Montagu 1884 Works Vol. 1 p. 292 (S6 scholarly edition); Gutenberg #5500 (S2) agrees. Certainty held at 0.7 by named alternatives on D/CHRIST, not by web-copy."}
  primary_system:
    value: CHRIST
    basis: written_profession
    certainty: 0.7
    cites: [{source: S6, locator: "Book I; Book II, VI.(1); Book II, XXV.(3) (1884 Works Vol. 1)"}, {source: S5, locator: "opening: Trinity; Creator by the Word; Mediator"}]
    rationale: "Revealed theology 'grounded only upon the word and oracle of God' governs faith and morals, beside a natural theology that 'sufficeth to convince atheism, but not to inform religion' (Advancement, S6). Confession of Faith (S5) confesses Trinity, creation by the Word, and the Mediator — same CHRIST pole. Accepts revelation, so not DEISM (P27). Not CLASS_THEISM: he rejects Aristotelian philosophy (S1/S7) and grounds theology in Scripture. Not CLTHEI: God works 'nothing in Nature but by second causes'. Certainty held at 0.7 by the named alternative CLTHEI (P15)."
    how_known: "Advancement checked in Spedding 1884 Works (S6); Confession in Spedding Works Vol. 2 (S5). Named alternative CLTHEI."
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Chosen: revealed divinity as the religion confessed."}
    - {code: CLTHEI, reason: "Alternative: he accepts that God wrought miracles to convert idolaters; rejected as primary because nature runs by second causes."}
    - {code: DEISM, reason: "Rejected: accepts revelation (P27)."}
    - {code: CLASS_THEISM, reason: "Rejected: anti-Aristotelian; theology from Scripture."}
  lio_axes:
    A_locus:
      value: 0
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S6, locator: "Book II, VI.(1) (1884 Works Vol. 1, pp. 322–323)"}, {source: S5, locator: "opening paragraphs: Creator; nature = laws of the creation"}]
      rationale: "God is the Maker set apart from his works: Advancement — the works 'show forth the power and skill of the workman, and not his image', and the heathen error was to suppose 'the world to be the image of God' (S6). Confession of Faith (second stream): 'nothing is without beginning, but God; no nature, no matter, no spirit'; he 'become a Creator' and 'by his eternal Word created all things'; nature is 'nothing but the laws of the creation' (S5). Separate personal creator = Boyle pattern, scored 0. Alternative 1 (no limiting feature named, so 0 kept). Independent works → corroborated (P48)."
      how_known: "Advancement in Spedding 1884 Works (S6 scholarly edition) plus Confession in Spedding Works Vol. 2 (S5). Named alternative 1; certainty 0.7."
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S6, locator: "Book I (1884 Works Vol. 1, pp. 291–292); Book II, VI.(1) (pp. 322–323)"}, {source: S3, locator: "'Of Atheism', first paragraph"}]
      rationale: "Account of nature (P6): 'God worketh nothing in nature but by second causes; and if they would have it otherwise believed, it is mere imposture' (S6). Stated, limited exception: 'miracles have been wrought to convert idolaters and the superstitious' (rare past acts for revelation; B 3 anchor, P27). Confession (S5) agrees: providence works 'by compass; not violating nature', and miracles transcend nature only for redemption. Alternative 4 (the miracles are not placed in nature), so 0.7. Independent source ids → corroborated (P48)."
      how_known: "Advancement in Spedding 1884 Works (S6) plus Essays 'Of Atheism' (S3). Named alternative 4."
    C_ledger: {value: UNKNOWN, how_known: "Passages read do not treat reward and punishment of persons."}
    D_authority:
      value: 2
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S6, locator: "Book I (p. 292); Book II, XXV.(3) (p. 367)"}, {source: S5, locator: "Scriptures shut; Church custody only"}]
      rationale: "Two domains each with its own authority (D 2 anchor, P27): philosophy studies the book of God's works; divinity 'is grounded only upon the word and oracle of God, and not upon the light of nature', and covers the mysteries and 'the law moral'; the two are not to be mingled (S6). Confession: the book of the Scriptures was 'shut and closed' after the apostles; the Church has 'only the custody and delivery over of the Scriptures' (S5). Independent sources → corroborated (P48)."
      how_known: "Advancement in Spedding 1884 Works (S6) plus Confession (S5)."
    E_scope: {value: UNKNOWN, how_known: "Scored on the world's order (P7); nothing read on in-group exceptions in events."}
  mid_basin: {value: true, certainty: 0.7, cites: [{source: S6, locator: "Book I; Book II, VI.(1)"}, {source: S5, locator: "Creator; laws of nature"}], how_known: "A_locus 0 (≤ 1) and B_cause 3 (≥ 3), both at 0.7 (P4, P6), both corroborated (P48). B's alternative 4 is on the same side (P30 #10); A's alternative 1 also. Capped at the lower of the two, 0.7 (P10). F = 5."}
  statements:
    - text: "For certain it is that God worketh nothing in Nature but by second causes; and if they would have it otherwise believed, it is mere imposture, as it were in favour towards God, and nothing else but to offer to the Author of truth the unclean sacrifice of a lie."
      cites: [{source: S6, locator: "Book I (1884 Works Vol. 1, pp. 291–292)"}, {source: S2, locator: "Book I, I.(3)"}]
      date: "1605"
      context: "Answering divines who say knowledge of second causes weakens dependence on God."
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      axes: [B_cause]
      note: "Checked against Spedding/Montagu 1884 Works Vol. 1 pp. 291–292 (S6); Gutenberg #5500 (S2) agrees (modernised spelling). Spedding has 'nature' lowercase."
    - text: "let no man upon a weak conceit of sobriety or an ill-applied moderation think or maintain that a man can search too far, or be too well studied in the book of God's word, or in the book of God's works, divinity or philosophy; but rather let men endeavour an endless progress or proficience in both; [...] and again, that they do not unwisely mingle or confound these learnings together."
      cites: [{source: S6, locator: "Book I (1884 Works Vol. 1, p. 292)"}, {source: S2, locator: "Book I, I.(3)"}]
      date: "1605"
      context: "Close of his answer to the divines."
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      axes: [D_authority]
      note: "Checked against Spedding 1884 Works Vol. 1 p. 292 (S6)."
    - text: "The bounds of this knowledge are, that it sufficeth to convince atheism, but not to inform religion; and therefore there was never miracle wrought by God to convert an atheist, because the light of nature might have led him to confess a God; but miracles have been wrought to convert idolaters and the superstitious, because no light of nature extendeth to declare the will and true worship of God.  For as all works do show forth the power and skill of the workman, and not his image, so it is of the works of God, which do show the omnipotency and wisdom of the Maker, but not His image."
      cites: [{source: S6, locator: "Book II, VI.(1) (1884 Works Vol. 1, pp. 322–323)"}, {source: S2, locator: "Book II, VI.(1)"}]
      date: "1605"
      context: "On natural theology (divine philosophy)."
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      axes: [A_locus, B_cause]
      note: "Checked against Spedding 1884 Works Vol. 1 pp. 322–323 (S6); 'maker' lowercase in Spedding."
    - text: "Wherefore we conclude that sacred theology (which in our idiom we call divinity) is grounded only upon the word and oracle of God, and not upon the light of nature"
      cites: [{source: S6, locator: "Book II, XXV.(3) (1884 Works Vol. 1, p. 367)"}, {source: S2, locator: "Book II, XXV.(3)"}]
      date: "1605"
      context: "On revealed theology."
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      axes: [D_authority]
      note: "Checked against Spedding 1884 Works Vol. 1 p. 367 (S6)."
    - text: "I HAD rather believe all the fables in the Legend, and the Talmud, and the Alcoran, than that this universal frame is without a mind. And therefore, God never wrought miracle, to convince atheism, because his ordinary works convince it."
      cites: [{source: S3, locator: "'Of Atheism', first paragraph"}]
      date: "1625"
      context: "Essay 'Of Atheism', in the 1625 Essayes."
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      axes: [B_cause]
      note: "Gutenberg #575 gives no source edition; primary check pending (EEBO-TCP of the 1625 edition)."
    - text: "I believe that nothing is without beginning, but God; no nature, no matter, no spirit, but one, only, and the same God. That God, as he is eternally almighty, only wise, only good, in his nature; so he is eternally Father, Son, and Spirit, in persons."
      cites: [{source: S5, locator: "opening paragraphs"}]
      date: "1603"
      context: "A Confession of Faith; MS circulated; first printed London 1641; Spedding Works Vol. 2 / VII."
      kind: "unpublished manuscript"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      axes: [A_locus]
      note: "Posthumous print of a finished confession; private-document ceiling would apply if used alone (P18); here corroborates Advancement A 0 (written_profession)."
    - text: "That by the virtue of this his eternal counsel he condescended of his own good pleasure, and according to the times and seasons to himself known, to become a Creator; and by his eternal Word created all things; and by his eternal Spirit doth comfort and preserve them. [...] he created heaven and earth, and all their armies and generations; and gave unto them constant and everlasting laws, which we call nature; which is nothing but the laws of the creation"
      cites: [{source: S5, locator: "Creator / laws of nature paragraphs"}]
      date: "1603"
      context: "Same Confession: Creator distinct from creatures; nature = creation's laws."
      kind: "unpublished manuscript"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      axes: [A_locus, B_cause]
    - text: "That notwithstanding God hath rested and ceased from creating since the first sabbath, yet, nevertheless, he doth accomplish and fulfil his divine will in all things, great and small, singular and general, as fully and exactly by providence, as he could by miracle and new creation, though his working be not immediate and direct, but by compass; not violating nature, which is his own law, upon the creature. [...] whensoever God doth transcend the law of nature by miracles, which may ever seem as new creations, he never cometh to that point or pass, but in regard of the work of redemption"
      cites: [{source: S5, locator: "providence / miracles paragraphs"}]
      date: "1603"
      context: "Providence by second causes; miracles rare and for redemption — supports B 3."
      kind: "unpublished manuscript"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      axes: [B_cause]
  changes_over_life: []
  coder_notes: "Coder's call: A 0, not 1, because Advancement and Confession separate Maker/Creator from works/nature without a limiting immanence feature (Boyle pattern). Deepen D1: A support single→corroborated via Confession (S5) + Advancement Spedding (S6); chart hollow→filled. Long s does not occur in the modernised Spedding/Gutenberg texts quoted."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "English", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "English Protestant (Church of England); mother's household Calvinist/Puritan-leaning", certainty: 0.7, cites: [{source: S7, locator: "§1; §8"}, {source: S1, locator: "'Youth and early maturity'"}], how_known: "SEP + Britannica; Matthews 2008 (cited S7 §8) notes Puritan background of the mother."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1605–1625", certainty: 0.7, cites: [{source: S1, locator: "career sections"}], how_known: "Advancement (1605) to the 1625 Essayes (P29, P30)."}
  age_at_first_lasting_contribution: {value: 44, certainty: 0.7, cites: [{source: S1, locator: "At a Glance; 1605"}], how_known: "1605 − 1561 = 44 (P30)."}
  first_evidence_of_lio_type_views: {value: "1605, age 44: 'God worketh nothing in Nature but by second causes'", year: 1605, age: 44, certainty: 0.5, cites: [{source: S2, locator: "Book I, I.(3)"}], how_known: "Earlier works (Essayes 1597, 1612) not read: 'earlier works not read' (P30 #7)."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.5, cites: [{source: S2, locator: "Book I, I.(3)"}], how_known: "Stated in the first listed work; earlier works not read."}
  worldview_during_major_work: {value: "CHRIST with a lawful nature by second causes", certainty: 0.7, cites: [{source: S2, locator: "Book I–II"}], how_known: "As coded."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "His method is inductive tables, not definition-to-consequence.", certainty: 0.5, cites: [{source: S1, locator: "body (method)"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "'Youth and early maturity'"}], how_known: "Nothing read."}
  circle_present: {value: "no", rationale: "He denies the world is God's image.", certainty: 0.5, cites: [{source: S2, locator: "Book II, VI.(1)"}], how_known: "Coder's reading."}
  reading: "As belief, not finding: a mid-basin case with no geometric form; cuts against H1's form requirement."
  notes: ""

institutions:
  - {value: "Gray's Inn", role: "member, reader, bencher", years: "1576–", kind: other, certainty: 0.7, cites: [{source: S1, locator: "'Early legal career'"}], how_known: "Britannica."}
collaborators: []

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 26"}], how_known: "Study roster."}
  controversies:
    - {value: "Convicted of taking bribes, 1621", certainty: 0.7, cites: [{source: S1, locator: "'Fall from power'"}], how_known: "Britannica."}
  data_quality_flags:
    - "Essays 'Of Atheism' (S3) still Gutenberg #575 without a named source edition; B also rests on S6 Advancement, so axis certainty is not limited by S3 alone."
    - "Oxford Francis Bacon IV (Kiernan) Advancement and OFB XV Essays not opened this pass; Spedding 1884 used as scholarly edition."
  open_questions:
    - "Optional: check Advancement against OFB IV (Kiernan) and Essays against OFB XV / EEBO-TCP 1625 for spelling and page numbers."
    - "Optional: C_ledger / E_scope still UNKNOWN — Confession has personal judgment and elect flock (C/E leads) if a later pass wants them."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Peter Michael Urbach; Kathleen Marguerite Lea; Anthony M. Quinton"
    citation: "\"Francis Bacon.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Francis-Bacon-Viscount-Saint-Alban."
    url: "https://www.britannica.com/biography/Francis-Bacon-Viscount-Saint-Alban"
    accessed: 2026-10-15
    reliability_note: "Signed article body; AI 'Top Questions' not used (P26)."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, heritage, timing, institutions, review]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Francis Bacon"
    year: 1605
    citation: "Bacon, Francis. The Advancement of Learning (1605). Ed. Henry Morley. London: Cassell, 1893. Project Gutenberg eBook #5500."
    url: "https://www.gutenberg.org/ebooks/5500"
    accessed: 2026-10-15
    reliability_note: "Edited, modernised Morley 1893 text via Gutenberg; Advancement quotes re-checked against Spedding 1884 (S6) on deepen D1. Kept as concordant unofficial web copy."
    source_quality: "unofficial web copy"
    used_for: [worldview, timing, lane_b]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "Francis Bacon"
    year: 1625
    citation: "Bacon, Francis. The Essays or Counsels, Civil and Moral. Project Gutenberg eBook #575."
    url: "https://www.gutenberg.org/ebooks/575"
    accessed: 2026-10-15
    reliability_note: "Source edition not named in the eBook; supporting use only for B (paired with S6)."
    source_quality: "unofficial web copy"
    used_for: [worldview]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S5
    type: primary
    kind: "scholarly edition"
    author: "Francis Bacon; James Spedding, Robert Leslie Ellis, Douglas Denon Heath (eds.)"
    year: 1641
    citation: 'Bacon, Francis. A Confession of Faith. In The Works of Francis Bacon, ed. Spedding, Ellis & Heath (London, 1857–74), literary works volume (Wikisource Volume 2). First printed London 1641; composition before 1603 (CELM; Spedding VII, 217–26).'
    url: "https://en.wikisource.org/wiki/The_Works_of_Francis_Bacon/Volume_2/A_Confession_of_Faith"
    accessed: 2026-10-24
    reliability_note: "Standard Spedding collected-works text of a finished confession printed posthumously 1641; authorship well attested (Wing/BM; CELM BcF 165). Second independent A stream from Advancement."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview, childhood, heritage]
  - id: S6
    type: primary
    kind: "scholarly edition"
    author: "Francis Bacon; Spedding / Montagu tradition (1884 Works Vol. 1)"
    year: 1605
    citation: "Bacon, Francis. The Advancement of Learning (1605), in The Works of Francis Bacon (1884) Volume 1 (Wikisource page-image transcription). Book I second-causes and two-books passages pp. 291–292; Book II natural theology VI.(1) pp. 322–323; Book II XXV.(3) p. 367."
    url: "https://en.wikisource.org/wiki/Page:The_Works_of_Francis_Bacon_(1884)_Volume_1.djvu/322"
    accessed: 2026-10-24
    reliability_note: "Scholarly collected-works text (Spedding/Montagu line) read as Wikisource proofread page transcription of the 1884 printing. Used to lift Advancement quotes off the §7 web-copy footing; OFB IV (Kiernan) not opened this pass."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview, timing, lane_b]
  - id: S7
    type: secondary
    kind: encyclopedia
    author: "Markku Peltonen"
    year: 2025
    citation: 'Peltonen, Markku. Francis Bacon. Stanford Encyclopedia of Philosophy (Winter 2025 Edition), ed. Edward N. Zalta and Uri Nodelman. First published 2 Dec 2025. https://plato.stanford.edu/entries/francis-bacon/.'
    url: "https://plato.stanford.edu/entries/francis-bacon/"
    accessed: 2026-10-24
    reliability_note: "Signed SEP reference entry; §1 life (Anne Cooke, York House, dates); §8 natural philosophy and religion (separation; Puritan mother background via Matthews 2008)."
    source_quality: "reference entry"
    used_for: [identity, basics, childhood, heritage, worldview, review]
---

# Francis Bacon

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Francis Bacon (1561–1626), English lawyer, lord chancellor and philosopher of inductive method: Advancement of Learning (1605), Novum Organum (1620), Essayes (1625) [S1, S7]. He held that 'God worketh nothing in nature but by second causes', while miracles were wrought to convert idolaters [S6]; Confession of Faith separates Creator from creatures and equates nature with the laws of creation [S5]. Draft: CHRIST 0.7; A 0 at 0.7 corroborated; B 3 at 0.7 corroborated; D 2 at 0.7 corroborated; mid_basin true at 0.7.

## Life and work

Trinity College, Cambridge; Gray's Inn; lord chancellor 1618–21; fell for bribery in 1621 [S1].

## Contribution and impact

Advancement, Novum Organum, Essays [S1].

## Childhood and education

Son of Sir Nicholas Bacon and Anne Cooke Bacon (Protestant/Puritan-leaning household); Cambridge 1573–75 under Whitgift [S1, S7].

## Adult working worldview

Two books, of God's word and God's works, not to be mingled; nature runs by second causes [S6]. Confession: Creator by the Word; nature = laws of creation; providence by compass [S5].

## Heritage (context only)

English Protestant; mother's Puritan/Calvinist reforming background [S1, S7].

## Timing

First lasting contribution 1605, at 44 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No geometric form; no circle [S1, S2].

## Open questions

- Optional OFB IV / OFB XV / EEBO-TCP page-number check.
- C_ledger and E_scope still UNKNOWN (Confession has elect/judgment leads).

## Research log

- 2026-10-15: Read Britannica; searched Gutenberg #5500 and #575 for the passages quoted.
- 2026-10-24: Deepen D1 — Spedding 1884 Advancement pages for A/B/D quotes; Confession of Faith (Spedding/Wikisource) as A second stream; SEP Peltonen 2025 for family religion; P47 labels; A support corroborated (chart-moving hollow→filled).
