---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch E)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-15
  change_log:
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch E, order P32: F 5, rank 26). Basics from Britannica (Urbach et al.). Worldview from The Advancement of Learning (1605), Morley's 1893 Cassell edition as transcribed by Project Gutenberg (#5500), and 'Of Atheism' (Essays, Gutenberg #575). Not a scientist (P30, P33). CHRIST 0.7; A 0 (0.7); B 3 (0.7); D 2 (0.7); mid_basin true (0.7). Draft, not reviewed."}

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
  family_religion: {value: TODO}
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
  self_described_science_religion_relation: {value: "Two books, 'the book of God's word, or [...] the book of God's works, divinity or philosophy': study both without end, but do not 'unwisely mingle or confound these learnings together' (1605).", certainty: 0.7, cites: [{source: S2, locator: "Book I, I.(3)"}], how_known: "Published work (written_profession), read in a Gutenberg transcription of Morley's 1893 edition, so capped at 0.7 under the §7 web-copy rule. TODO: check against a scholarly edition (Kiernan, Oxford Francis Bacon IV)."}
  primary_system:
    value: CHRIST
    basis: written_profession
    certainty: 0.7
    cites: [{source: S2, locator: "Book I, I.(3); Book II, VI.(1); Book II, XXV.(3)"}]
    rationale: "Revealed theology 'grounded only upon the word and oracle of God' governs faith and morals, beside a natural theology that 'sufficeth to convince atheism, but not to inform religion'. Accepts revelation, so not DEISM (P27). Not CLASS_THEISM: he rejects Aristotelian philosophy (S1) and grounds theology in Scripture, not in a simple immutable God of the schools. Not CLTHEI: God works 'nothing in Nature but by second causes'. Capped at 0.7 by the web-copy rule and by the named alternative CLTHEI."
    how_known: "Gutenberg #5500 (Morley 1893 text); 0.7 cap pending a scholarly-edition check."
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
      cites: [{source: S2, locator: "Book II, VI.(1)"}]
      rationale: "God is the Maker set apart from his works: the works 'show forth the power and skill of the workman, and not his image', and the heathen error was to suppose 'the world to be the image of God'. A separate personal creator is the Boyle pattern, scored 0. Alternative 1 (no limiting feature named, so 0 kept)."
      how_known: "Gutenberg web copy, 0.7 cap; alternative named."
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.7
      cites: [{source: S2, locator: "Book I, I.(3); Book II, VI.(1)"}, {source: S3, locator: "'Of Atheism', first paragraph"}]
      rationale: "Account of nature (P6): 'God worketh nothing in Nature but by second causes; and if they would have it otherwise believed, it is mere imposture'. Stated, limited exception: 'miracles have been wrought to convert idolaters and the superstitious' (rare past acts for revelation; B 3 anchor, P27). Alternative 4 (the miracles are not placed in nature), so 0.7."
      how_known: "Published work in a Gutenberg web copy, 0.7 cap; alternative named."
    C_ledger: {value: UNKNOWN, how_known: "Passages read do not treat reward and punishment of persons."}
    D_authority:
      value: 2
      basis: written_profession
      certainty: 0.7
      cites: [{source: S2, locator: "Book I, I.(3); Book II, XXV.(3)"}]
      rationale: "Two domains each with its own authority (D 2 anchor, P27): philosophy studies the book of God's works; divinity 'is grounded only upon the word and oracle of God, and not upon the light of nature', and covers the mysteries and 'the law moral'; the two are not to be mingled."
      how_known: "Gutenberg web copy, 0.7 cap."
    E_scope: {value: UNKNOWN, how_known: "Scored on the world's order (P7); nothing read on in-group exceptions in events."}
  mid_basin: {value: true, certainty: 0.7, cites: [{source: S2, locator: "Book I, I.(3); Book II, VI.(1)"}], how_known: "A_locus 0 (≤ 1) and B_cause 3 (≥ 3), both at 0.7 (P4, P6). B's alternative 4 is on the same side (P30 #10); A's alternative 1 also. Capped at the lower of the two, 0.7 (P10). F = 5."}
  statements:
    - text: "For certain it is that God worketh nothing in Nature but by second causes; and if they would have it otherwise believed, it is mere imposture, as it were in favour towards God, and nothing else but to offer to the Author of truth the unclean sacrifice of a lie."
      cites: [{source: S2, locator: "Book I, I.(3)"}]
      date: "1605"
      context: "Answering divines who say knowledge of second causes weakens dependence on God."
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-15
      axes: [B_cause]
      note: "Morley's edited text (Cassell 1893) via Gutenberg #5500; modernised spelling; web copy, 0.7 cap."
    - text: "let no man upon a weak conceit of sobriety or an ill-applied moderation think or maintain that a man can search too far, or be too well studied in the book of God's word, or in the book of God's works, divinity or philosophy; but rather let men endeavour an endless progress or proficience in both; [...] and again, that they do not unwisely mingle or confound these learnings together."
      cites: [{source: S2, locator: "Book I, I.(3)"}]
      date: "1605"
      context: "Close of his answer to the divines."
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-15
      axes: [D_authority]
    - text: "The bounds of this knowledge are, that it sufficeth to convince atheism, but not to inform religion; and therefore there was never miracle wrought by God to convert an atheist, because the light of nature might have led him to confess a God; but miracles have been wrought to convert idolaters and the superstitious, because no light of nature extendeth to declare the will and true worship of God.  For as all works do show forth the power and skill of the workman, and not his image, so it is of the works of God, which do show the omnipotency and wisdom of the Maker, but not His image."
      cites: [{source: S2, locator: "Book II, VI.(1)"}]
      date: "1605"
      context: "On natural theology (divine philosophy)."
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-15
      axes: [A_locus, B_cause]
    - text: "Wherefore we conclude that sacred theology (which in our idiom we call divinity) is grounded only upon the word and oracle of God, and not upon the light of nature"
      cites: [{source: S2, locator: "Book II, XXV.(3)"}]
      date: "1605"
      context: "On revealed theology."
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-15
      axes: [D_authority]
    - text: "I HAD rather believe all the fables in the Legend, and the Talmud, and the Alcoran, than that this universal frame is without a mind. And therefore, God never wrought miracle, to convince atheism, because his ordinary works convince it."
      cites: [{source: S3, locator: "'Of Atheism', first paragraph"}]
      date: "1625"
      context: "Essay 'Of Atheism', in the 1625 Essayes."
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      axes: [B_cause]
      note: "Gutenberg #575 gives no source edition; primary check pending (EEBO-TCP of the 1625 edition)."
  changes_over_life: []
  coder_notes: "Coder's call: A 0, not 1, because the passage separates Maker and works without a limiting feature (lens's Boyle pattern). Long s does not occur (modernised text)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "English", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: TODO}
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
    - "Advancement and Essays read only in Gutenberg web copies; fields capped at 0.7."
  open_questions:
    - "Check quotes against the Oxford Francis Bacon edition and EEBO-TCP for the 1605 and 1625 printings; read the Confession of Faith for A."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Peter Michael Urbach; Kathleen Marguerite Lea; Anthony M. Quinton"
    citation: "\"Francis Bacon.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Francis-Bacon-Viscount-Saint-Alban."
    url: "https://www.britannica.com/biography/Francis-Bacon-Viscount-Saint-Alban"
    accessed: 2026-10-15
    reliability_note: "Signed article body; AI 'Top Questions' not used (P26)."
    used_for: [identity, basics, contribution, childhood, heritage, timing, institutions, review]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Francis Bacon"
    year: 1605
    citation: "Bacon, Francis. The Advancement of Learning (1605). Ed. Henry Morley. London: Cassell, 1893. Project Gutenberg eBook #5500."
    url: "https://www.gutenberg.org/ebooks/5500"
    accessed: 2026-10-15
    reliability_note: "Edited, modernised text in an unofficial web copy; §7 cap 0.7."
    used_for: [worldview, timing, lane_b]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "Francis Bacon"
    year: 1625
    citation: "Bacon, Francis. The Essays or Counsels, Civil and Moral. Project Gutenberg eBook #575."
    url: "https://www.gutenberg.org/ebooks/575"
    accessed: 2026-10-15
    reliability_note: "Source edition not named in the eBook; supporting use only."
    used_for: [worldview]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Francis Bacon

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Francis Bacon (1561–1626), English lawyer, lord chancellor and philosopher of inductive method: Advancement of Learning (1605), Novum Organum (1620), Essayes (1625) [S1]. He held that 'God worketh nothing in Nature but by second causes', while miracles were wrought to convert idolaters [S2, Book I, I.(3); Book II, VI.(1)]. Draft: CHRIST 0.7; A 0 at 0.7; B 3 at 0.7; D 2 at 0.7; mid_basin true at 0.7.

## Life and work

Trinity College, Cambridge; Gray's Inn; lord chancellor 1618–21; fell for bribery in 1621 [S1].

## Contribution and impact

Advancement, Novum Organum, Essays [S1].

## Childhood and education

Son of Sir Nicholas Bacon; Cambridge 1573–75 [S1].

## Adult working worldview

Two books, of God's word and God's works, not to be mingled; nature runs by second causes [S2].

## Heritage (context only)

English [S1].

## Timing

First lasting contribution 1605, at 44 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No geometric form; no circle [S1, S2].

## Open questions

- Scholarly-edition check of quotes.

## Research log

- 2026-10-15: Read Britannica; searched Gutenberg #5500 and #575 for the passages quoted.
