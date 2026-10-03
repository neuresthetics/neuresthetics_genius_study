---
record:
  record_type: person
  schema_version: "1.2"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, second batch: physical science 1600–1950)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (second batch, RUNBOOK §1 order). Basics from Britannica (Westman), MacTutor (J. V. Field) and SEP (Di Liscia). Worldview from SEP and MacTutor (scholars' readings) and one letter quoted by the Bodleian's Cultures of Knowledge project. No primary text of Kepler's was read. CHRIST (Lutheran, excommunicated 1612) at 0.5; PLATO named. A 1, B 4, D 3, E 4, all at 0.5; C BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD (A at 0.5). Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit, batch 2 (two blind runs at e648145). Finding #78: B_cause 4 → 3 at 0.5; MacTutor quotes him on the 1604 nova allowing a 'special creation' only after trying 'everything else' (De stella nova ch. 22), a stated limited exception; statement added. Finding #81: E_scope 4 (0.5) → BELOW_THRESHOLD, the same thin evidence as Fermi, Meitner and Curie (§3 same pattern). Finding #83: self_described_science_religion_relation 0.7 → 0.5 (single-letter rule, §3). mid_basin unchanged (BELOW_THRESHOLD; A 1 and B 3 both at 0.5). primary_system unchanged (CHRIST 0.5). Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Schema 1.1 → 1.2 (decision P8 adds basis recorded_interview and statement kind 'recorded interview'); no content change."}

identity:
  id: kepler-johannes
  display_name: "Johannes Kepler"
  roster:
    canonical_name: "Johannes Kepler"
    rank: 45
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: astronomy
    field_bucket: astronomy
  full_name: {value: "Johannes Kepler", certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}, {source: S2, locator: "Quick Info"}], how_known: "Sources agree."}
  native_name: {value: "Johannes Kepler (German)", certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}], how_known: "German; he wrote mostly in Latin."}
  aliases:
    - {name: "Johannes-Kepler", kind: "roster alias"}
    - {name: "Kepler-Johannes", kind: "roster alias"}
    - {name: "Ioannes Keplerus", kind: latinized}

basics:
  birth:
    date: {value: "1571-12-27", calendar: julian, certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S2, locator: "Quick Info"}], how_known: "Two sources agree on 27 December 1571. Protestant Württemberg still used the Julian calendar; the sources do not state the calendar, so the calendar tag is the coder's (flag)."}
    place: {value: "Weil der Stadt, Württemberg", modern_name: "Weil der Stadt, Baden-Württemberg, Germany", polity_then: "Holy Roman Empire", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S2, locator: "Quick Info"}], how_known: "Two sources agree."}
  death:
    date: {value: "1630-11-15", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S2, locator: "Quick Info"}], how_known: "Two sources agree."}
    place: {value: "Regensburg", modern_name: "Regensburg, Germany", polity_then: "Holy Roman Empire", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S2, locator: "Quick Info"}], how_known: "Two sources agree."}
  first_lasting_contribution_year: {value: 1604, certainty: 0.7, cites: [{source: S2, locator: "opening paragraph (optics 1604)"}, {source: S1, locator: "opening (a new and correct account of how vision occurs)"}], how_known: "The 1604 optics gave 'a new and correct account of how vision occurs' (S1). If the planetary laws are taken as the first lasting contribution, the year is 1609, so 0.7.", alternatives: [{value: 1609, cites: [{source: S2, locator: "opening paragraph"}], note: "First two laws, Astronomia nova."}]}
  era_bucket: {value: "1600 to 1749", certainty: 1.0, cites: [{source: S2, locator: "opening paragraph"}], how_known: "Both candidate years fall in 1600 to 1749 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts ('Württemberg [Germany]')"}], how_known: "Germany is Western Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Eastern Europe", certainty: 0.7, cites: [{source: S2, locator: "Biography (Prague; Imperial Mathematician after Tycho, 1601)"}, {source: S3, locator: "§1"}], how_known: "The optics (1604) and the first two laws (1609) were done in Prague (Czechia is Eastern Europe in regions.csv). The third law (Harmonices mundi, 1619) was done in Linz (Austria, Western Europe). Two regions, so 0.7.", alternatives: [{value: "Western Europe", cites: [{source: S2, locator: "Biography (Linz)"}], note: "Graz 1594–1600 and Linz from 1612 (Austria)."}]}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S2, locator: "Childhood"}], how_known: "As the sources record it."}
  languages_of_work: {value: [Latin, German], certainty: 0.7, cites: [{source: S2, locator: "Biography"}, {source: S5, locator: "catalogue note (letters mostly in Latin and German)"}], how_known: "Latin works; letters in Latin and German."}
  occupations: {value: [astronomer, mathematician, "Imperial Mathematician", "teacher of mathematics", astrologer], certainty: 1.0, cites: [{source: S2, locator: "Biography"}, {source: S3, locator: "§1"}], how_known: "Two sources."}

contribution:
  fields: {value: [astronomy, optics, mathematics, cosmology], certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "opening paragraph"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Optics: a new and correct account of how vision occurs", year: "1604", kind: theory, lasting: "Britannica calls it correct", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "opening paragraph"}], how_known: "Two sources."}
    - {value: "First and second laws of planetary motion (ellipse; area law)", year: "1609", kind: "law or principle", lasting: "Newton derived them from gravitation (S1)", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "opening paragraph"}], how_known: "Two sources."}
    - {value: "Third (harmonic) law", year: "1619", kind: "law or principle", lasting: "standard astronomy", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "The Harmony of the World"}], how_known: "Two sources."}
    - {value: "Rudolphine Tables", year: "1627", kind: work, lasting: "their accuracy 'did much to establish the truth of heliocentric astronomy' (S2)", certainty: 1.0, cites: [{source: S2, locator: "opening paragraph"}], how_known: "MacTutor."}
  evidence_of_impact:
    - {value: "Laws named after him; Newton derived them from his law of gravity", kind: "named after them", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works:
    - {value: "Mysterium cosmographicum", year: 1596, kind: book, certainty: 1.0, cites: [{source: S2, locator: "first cosmological model"}, {source: S3, locator: "§1"}], how_known: "Two sources."}
    - {value: "Astronomia nova", year: 1609, kind: book, certainty: 1.0, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor."}
    - {value: "Harmonices mundi", year: 1619, kind: book, certainty: 1.0, cites: [{source: S2, locator: "The Harmony of the World"}], how_known: "MacTutor."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "The three laws of planetary motion.", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "Sources agree."}

childhood:
  family_religion: {value: "Lutheran", certainty: 1.0, cites: [{source: S2, locator: "Childhood ('a bastion of Lutheran orthodoxy')"}, {source: S5, locator: "catalogue introduction (the Lutheran Seminary of Adelberg)"}], how_known: "Two sources."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father a mercenary soldier who left when Johannes was five and is believed to have died in the Netherlands war", role: father, certainty: 0.7, cites: [{source: S2, locator: "Childhood"}], how_known: "MacTutor."}
    - {value: "Mother, Katharina, daughter of an innkeeper; later tried for witchcraft", name: "Katharina Kepler", role: mother, certainty: 1.0, cites: [{source: S2, locator: "Childhood; Witchcraft trial"}], how_known: "MacTutor."}
  household_circumstances: {value: "Lived with his mother in his grandfather's inn and helped serve; moved to Leonberg in 1576", certainty: 0.7, cites: [{source: S2, locator: "Childhood"}], how_known: "MacTutor."}
  schooling:
    - {value: "Local (Latin) school, Leonberg", stage: "grammar or secondary school", certainty: 0.7, cites: [{source: S2, locator: "Childhood"}, {source: S5, locator: "catalogue introduction"}], how_known: "Two sources."}
    - {value: "Lutheran seminary (Adelberg), intending ordination", stage: "religious school", certainty: 1.0, cites: [{source: S2, locator: "Childhood"}, {source: S5, locator: "catalogue introduction"}], how_known: "Two sources."}
    - {value: "University of Tübingen (Stift): Magister Artium 1591, then theology", stage: university, years: "1589–1594", certainty: 1.0, cites: [{source: S3, locator: "§1"}, {source: S5, locator: "catalogue introduction (enrolled 17 September 1589)"}], how_known: "Two sources."}
  early_mathematics: {value: "arithmetic only", note: "MacTutor mentions his 'unusual competence at arithmetic' as a child at the inn; nothing more before 17 in the sources read", certainty: 0.5, cites: [{source: S2, locator: "Childhood"}], how_known: "One source, framed as the author's surmise."}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [German, Latin], certainty: 0.7, cites: [{source: S5, locator: "catalogue introduction (Latin school)"}], how_known: "Latin school; German native."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1594–1630", certainty: 1.0, cites: [{source: S3, locator: "§1"}], how_known: "Graz post to death."}
  nominal_affiliations:
    - {value: "Lutheran; excommunicated in 1612 and never reinstated, over the Eucharist", years: "to 1612", role: member, certainty: 0.7, cites: [{source: S2, locator: "University education"}], how_known: "MacTutor (one source)."}
  self_described_science_religion_relation:
    value: "Astronomy as a way to celebrate God: he had wanted to be a theologian, and wrote in 1595 that through his work God is celebrated in astronomy."
    certainty: 0.5
    cites: [{source: S4, locator: "paragraph 1"}, {source: S3, locator: "§2"}]
    how_known: "One letter, through an English translation quoted by the Bodleian project. A single private letter is not 'consistent private letters'; with a scholar's backing it is 0.5 (§3), as for Meitner and Curie. SEP's reading agrees ('astronomy represents for Kepler, if done philosophically, the best path to God')."
  primary_system:
    value: CHRIST
    basis: scholarly_reconstruction
    certainty: 0.5
    cites: [{source: S2, locator: "Kepler's opinions; University education"}, {source: S3, locator: "§2"}]
    how_known: "No work of Kepler's was read. Two scholars describe a 'profoundly religious' Lutheran, 'a Christian Natural Philosopher' (S2), whose cosmology maps the Trinity onto the sphere (S3). Scholarly reconstruction, so 0.5."
    rationale: "CHRIST use_when: Christian belief (Trinity, scripture, church) without a more specific philosophical position. Branch: Lutheran, nonconforming on the Eucharist. Named alternative: PLATO, since 'he always returns to his Platonic and Neoplatonic framework of thought' (S3); not chosen because the framework is used to picture the Christian Creator and Trinity, which CHRIST's do_not_use_when allows."
  secondary_system: {value: UNKNOWN, how_known: "PLATO is a named alternative, but no source read says he professed two systems."}
  candidate_codes_considered:
    - {code: PLATO, reason: "Named alternative: Neoplatonic geometric archetypes (S3 §2). PLATO is sourced.", cites: [{source: S3, locator: "§2"}]}
    - {code: CLASS_THEISM, reason: "Rejected: no classical metaphysics of a simple God in the sources read."}
  lio_axes:
    A_locus:
      value: 1
      basis: scholarly_reconstruction
      certainty: 0.5
      cites: [{source: S3, locator: "§2"}, {source: S2, locator: "Kepler's opinions"}]
      how_known: "Scholars' readings, no primary text read, so 0.5."
      rationale: "Leans to the transcendent pole: 'God the Creator, who accomplished His work according to the model of the five regular polyhedra' (S3) and made the universe by 'a mathematical plan' (S2); God is not the world. Not 0: the sphere is read as an image of the Trinity (S3), so the world mirrors God closely. Alternative 2 is possible on that image-reading; not chosen."
    B_cause:
      value: 3
      basis: scholarly_reconstruction
      certainty: 0.5
      cites: [{source: S2, locator: "Kepler's opinions; University education; Observational error (New Star of 1604)"}, {source: S1, locator: "opening"}]
      how_known: "Scholars' readings of his working science (P6), plus one short phrase of his on the 1604 nova quoted in translation by MacTutor, so 0.5."
      rationale: "Scored on his account of nature (P6). Leans to the law pole: one mathematical plan, laws of planetary motion, forces from the Sun acting on the planets (S2), and an astrology restricted in 'the domain in which its predictions could be considered reliable' (S1), treated as natural influence. The stated limited exception: on the new star of 1604 he rejected numerous explanations and allowed that it 'could just be a special creation', 'but before we come to [that] I think we should try everything else' (S2, quoting De stella nova, 1606, ch. 22). A special creation in nature is kept as a last resort, so 3. Named alternative 4, since he puts natural explanation first and does not assert the special creation."
    C_ledger: {value: BELOW_THRESHOLD, how_known: "Nothing on judgement, reward or afterlife in S1–S5.", note: "Gap: his letters on the Eucharist dispute and his theological writings were not read."}
    D_authority:
      value: 3
      basis: scholarly_reconstruction
      certainty: 0.5
      cites: [{source: S3, locator: "§2"}, {source: S2, locator: "Kepler's opinions"}]
      how_known: "Scholars' readings, so 0.5."
      rationale: "Leans to reason: 'Kepler does indeed repeatedly thank God for granting him insights, but the insights are presented as rational' (S2). The stated limited exception: God manifests himself 'not only in the words of the Scriptures but also in the wonderful arrangement of the universe' (S3), so Scripture keeps a place beside nature. Alternative 2 (two domains) is possible if his Astronomia nova introduction on Scripture is read; not read."
    E_scope: {value: BELOW_THRESHOLD, how_known: "Scored on the world's order (P7). Scholars describe one geometric plan for the whole universe, which humans 'made in the image of God' can understand (S2, Kepler's opinions; S3, §2), but nothing read addresses favour or exceptions for a group in events, and his writing on providence was not read.", note: "Same treatment as Fermi, Meitner and Curie: not scored from the working science or the cosmology alone, because P7's second question (in-group exceptions) needs a statement (§3 same pattern, lens audit batch 2). Was 4 at 0.5."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus = 1 and B_cause = 3 would pass, but both are only at 0.5, under the P4 test's 0.7 bar."}
  statements:
    - text: "'I wanted to become a theologian', he explained in 1595 to Michael Maestlin, the Tübingen professor of mathematics who had first introduced him to Copernicanism, 'and for a long time I was restless. Now however, behold how God is being celebrated in astronomy.'"
      cites: [{source: S4, locator: "paragraph 1"}]
      date: "1595"
      context: "Letter to Maestlin, 3 October 1595 (KGW 13, letter 23, not read)."
      axes: [D_authority]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-02
      note: "The quotation includes the Bodleian writer's framing words; Kepler's words are the two quoted pieces."
    - text: "but before we come to [that] I think we should try everything else"
      cites: [{source: S2, locator: "Observational error (New Star of 1604)"}]
      date: "1606"
      context: "De stella nova (Prague, 1606), ch. 22 (KGW 1, p. 257, line 23, as cited by MacTutor), on the new star of 1604. MacTutor's lead-in: 'remarking at one point that of course this star could just be a special creation'. English translation in S2; bracket as printed there."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-02
  changes_over_life:
    - {value: "Gave up ordination for a mathematics post in Graz, perhaps because of doubts about his orthodoxy", year: "1594", certainty: 0.5, cites: [{source: S2, locator: "University education ('These may explain')"}], how_known: "MacTutor offers it as a likely explanation."}
  coder_notes: "CHRIST and PLATO are sourced system files. No Kepler text was read directly; KGW Digital (searchable PDFs, linked from EMLO) would let the 1595 letter and the Astronomia nova introduction be checked in the original."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Swabian (Württemberg)", certainty: 1.0, cites: [{source: S2, locator: "Childhood"}], how_known: "MacTutor."}
  religious_heritage_by_birth: {value: "Lutheran", certainty: 1.0, cites: [{source: S2, locator: "Childhood"}, {source: S5, locator: "catalogue introduction"}], how_known: "Two sources."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: "Lutheran seminary training for the ministry", certainty: 1.0, cites: [{source: S5, locator: "catalogue introduction"}, {source: S2, locator: "Childhood"}], how_known: "Two sources."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1604–1627", certainty: 1.0, cites: [{source: S2, locator: "opening paragraph"}], how_known: "Optics to the Rudolphine Tables."}
  age_at_first_lasting_contribution: {value: 32, certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}], how_known: "Born December 1571; 1604 optics. 37 if the 1609 laws are used."}
  first_evidence_of_lio_type_views: {value: "God made the universe by a mathematical plan (Mysterium cosmographicum)", year: 1596, certainty: 0.5, cites: [{source: S3, locator: "§2"}, {source: S2, locator: "first cosmological model"}], how_known: "Scholars' readings."}
  lio_views_relative_to_major_work: {value: "before major work", rationale: "The geometric-plan cosmology of 1596 precedes the 1604 optics and 1609 laws.", certainty: 0.5, cites: [{source: S3, locator: "§2"}], how_known: "Dates."}
  worldview_during_major_work: {value: "Lutheran Christian natural philosophy with a Neoplatonic geometric cosmology", certainty: 0.5, cites: [{source: S2, locator: "Kepler's opinions"}, {source: S3, locator: "§2"}], how_known: "Scholars' readings."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "Euclid's postulates 'regarded as actually true' as a method for the universe (S2); Euclid XIII's five solids drive the 1596 model.", certainty: 0.7, cites: [{source: S2, locator: "Kepler's opinions; first cosmological model"}], how_known: "MacTutor."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "University education"}], how_known: "Mathematics at Tübingen; childhood exposure not stated."}
  circle_present: {value: "no", rationale: "God the Creator is the efficient cause, distinct from the world (S3).", certainty: 0.5, cites: [{source: S3, locator: "§2"}], how_known: "Scholar's reading."}
  reading: "As belief, not finding: form present, acquisition unclear, no circle. The record does not test H1."
  notes: ""

institutions:
  - {value: "Protestant school, Graz", role: "teacher of mathematics", years: "1594–1600", kind: employer, certainty: 1.0, cites: [{source: S3, locator: "§1"}], how_known: "SEP."}
  - {value: "Imperial court, Prague", role: "assistant to Tycho, then Imperial Mathematician", years: "1600–1612", kind: "patron or funder", certainty: 1.0, cites: [{source: S3, locator: "§1"}, {source: S2, locator: "Biography"}], how_known: "Two sources."}
collaborators:
  - {value: "Michael Maestlin", relation: teacher, note: "introduced him to Copernicus", certainty: 1.0, cites: [{source: S3, locator: "§1"}, {source: S2, locator: "University education"}], how_known: "Two sources."}
  - {value: "Tycho Brahe", relation: "mentor or employer", certainty: 1.0, cites: [{source: S3, locator: "§1"}], how_known: "SEP."}
  - {value: "Galileo Galilei", roster_id: galilei-galileo, relation: correspondent, note: "coined 'satellite' in 1610 for the moons Galileo found orbiting Jupiter", certainty: 0.7, cites: [{source: S2, locator: "first cosmological model ('satellite')"}], how_known: "MacTutor."}
  - {value: "Isaac Newton", roster_id: newton-isaac, relation: influenced, note: "derived Kepler's laws from gravitation", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v7.1 (F 4) and v8 (F 5, all five models).", certainty: 0.7, cites: [{source: S6, locator: "roster.csv, rank 45"}], how_known: "Study roster."}
  controversies:
    - {value: "His mother was tried for witchcraft; he defended her", certainty: 1.0, cites: [{source: S2, locator: "Witchcraft trial"}], how_known: "MacTutor."}
  data_quality_flags:
    - "Calendar of the birth date not stated in the sources; tagged julian by the coder."
    - "Every worldview claim rests on scholars' readings or a secondary quotation; nothing at 0.7 or above on the axes."
  open_questions:
    - "Read KGW 13 letter 23 (1595), the Astronomia nova introduction on Scripture, and the Harmonices mundi V closing prayer, to raise A, B, D and test C."
    - "Read Methuen, Kepler's Tübingen (1998), for his theology."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Robert S. Westman"
    citation: "Westman, Robert S. \"Johannes Kepler.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Johannes-Kepler."
    url: "https://www.britannica.com/biography/Johannes-Kepler"
    accessed: 2026-10-02
    reliability_note: "Signed article by a historian of astronomy; first page read."
    used_for: [identity, basics, contribution, worldview, timing, collaborators]
  - id: S2
    type: tertiary
    kind: encyclopedia
    author: "J. V. Field"
    year: 1999
    citation: "Field, J. V. \"Johannes Kepler.\" MacTutor History of Mathematics Archive, University of St Andrews, last updated April 1999. https://mathshistory.st-andrews.ac.uk/Biographies/Kepler/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Kepler/"
    accessed: 2026-10-02
    reliability_note: "By a Kepler scholar (translator of Harmonices mundi)."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators, review]
  - id: S3
    type: tertiary
    kind: encyclopedia
    author: "Daniel A. Di Liscia"
    year: 2025
    citation: "Di Liscia, Daniel A. \"Johannes Kepler.\" Stanford Encyclopedia of Philosophy, first published 2 May 2011, substantive revision 14 September 2025. https://plato.stanford.edu/entries/kepler/."
    url: "https://plato.stanford.edu/entries/kepler/"
    accessed: 2026-10-02
    reliability_note: "Peer-reviewed entry."
    used_for: [basics, contribution, worldview, timing, lane_b, institutions, collaborators]
  - id: S4
    type: secondary
    kind: "institutional page"
    author: "Cultures of Knowledge (University of Oxford)"
    year: 2016
    citation: "\"'Skybound was the mind': Johannes Kepler.\" Cultures of Knowledge blog, Bodleian Libraries, on the EMLO Kepler catalogue. https://www.culturesofknowledge.org/?p=6561."
    url: "https://www.culturesofknowledge.org/?p=6561"
    accessed: 2026-10-02
    reliability_note: "Scholarly project page; quotes the 1595 letter in English."
    used_for: [worldview]
  - id: S5
    type: secondary
    kind: database
    author: "Early Modern Letters Online (Bodleian Libraries)"
    citation: "\"The Correspondence of Johannes Kepler.\" EMLO catalogue introduction. http://emlo-portal.bodleian.ox.ac.uk/collections/?catalogue=johannes-kepler."
    url: "http://emlo-portal.bodleian.ox.ac.uk/collections/?catalogue=johannes-kepler"
    accessed: 2026-10-02
    reliability_note: "Read through a search-result extract only (Latin school, Adelberg seminary, Tübingen enrolment date); the page itself was not fetched. Flag."
    used_for: [basics, childhood, heritage]
  - id: S6
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
---

# Johannes Kepler

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Johannes Kepler (1571–1630), German astronomer, gave the three laws of planetary motion (1609, 1619) and a correct account of vision (1604) [S1, opening; S2, opening paragraph]. Scholars describe him as "a profoundly religious man" and "a Christian Natural Philosopher" who saw God's mathematical plan in the cosmos [S2, Kepler's opinions]. No Kepler text was read, so the record stays at 0.5: CHRIST at 0.5 (PLATO named); mid_basin below threshold.

## Life and work

Born at Weil der Stadt, schooled at a Lutheran seminary and Tübingen, he taught in Graz, succeeded Tycho as Imperial Mathematician in Prague, and later worked in Linz [S2, Childhood; Biography; S3, §1].

## Contribution and impact

Optics (1604), the ellipse and area laws (1609), the harmonic law (1619) and the Rudolphine Tables (1627) [S2, opening paragraph].

## Childhood and education

His father was a mercenary and his mother an innkeeper's daughter; he trained for the Lutheran ministry [S2, Childhood; S5, catalogue introduction].

## Adult working worldview

He wrote in 1595 that he had wanted to be a theologian and now "God is being celebrated in astronomy" [S4, paragraph 1]. SEP: God the Creator built the world on the five regular solids, and the Trinity maps onto the sphere [S3, §2]. Excommunicated in 1612 over the Eucharist [S2, University education]. Scores: A 1, B 3, D 3 (all 0.5); C and E below threshold; mid_basin below threshold. On the 1604 nova he allowed a "special creation" only after trying "everything else" [S2, Observational error].

## Heritage (context only)

Swabian Lutheran [S2, Childhood]. Context only.

## Timing

First lasting contribution 1604, at 32 [S1, Quick Facts]. The God-made geometric plan of 1596 comes before it [S3, §2].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Euclidean form is central [S2, Kepler's opinions]; no circle.

## Open questions

- KGW 13 letter 23; Astronomia nova introduction; Methuen 1998.

## Research log

- 2026-10-02: Read Britannica (Westman, first page), MacTutor (Field), SEP (Kepler) and the Cultures of Knowledge post. EMLO's catalogue text came only through a search extract. No primary text read.
