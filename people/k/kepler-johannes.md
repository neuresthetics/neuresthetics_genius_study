---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 8
  review_status: draft — unreviewed
  collected_by: "Grok Bot (agent run for Jason, second batch: physical science 1600–1950)"
  model_used: Grok Bot executor agent; web search plus direct reads of the cited pages
  collected_on: '2026-10-02'
  last_updated: 2026-10-27
  change_log:
  - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to early_modern. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
  - date: '2026-10-02'
    by: Grok Bot
    summary: "Record created (second batch, RUNBOOK §1 order). Basics from Britannica (Westman), MacTutor (J. V. Field) and\
      \ SEP (Di Liscia). Worldview from SEP and MacTutor (scholars' readings) and one letter quoted by the Bodleian's Cultures\
      \ of Knowledge project. No primary text of Kepler's was read. CHRIST (Lutheran, excommunicated 1612) at 0.5; PLATO named.\
      \ A 1, B 4, D 3, E 4, all at 0.5; C BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD (A at 0.5). Not reviewed."
  - date: '2026-10-02'
    by: Grok Bot
    summary: "Lens audit, batch 2 (two blind runs at e648145). Finding #78: B_cause 4 → 3 at 0.5; MacTutor quotes him on the\
      \ 1604 nova allowing a 'special creation' only after trying 'everything else' (De stella nova ch. 22), a stated limited\
      \ exception; statement added. Finding #81: E_scope 4 (0.5) → BELOW_THRESHOLD, the same thin evidence as Fermi, Meitner\
      \ and Curie (§3 same pattern). Finding #83: self_described_science_religion_relation 0.7 → 0.5 (single-letter rule,\
      \ §3). mid_basin unchanged (BELOW_THRESHOLD; A 1 and B 3 both at 0.5). primary_system unchanged (CHRIST 0.5). Not reviewed."
  - date: '2026-10-02'
    by: Grok Bot
    summary: "Schema 1.1 → 1.2 (decision P8 adds basis recorded_interview and statement kind 'recorded interview'); no content\
      \ change."
  - date: '2026-10-02'
    by: Grok Bot
    summary: "Stage 3 lens-audit rulings applied to the batch's other records (OPEN_DECISIONS P14–P28, v8's picks, 2026-10-02).\
      \ Schema 1.2 → 1.3. One reliable source caps a fact at 0.7; derived fields take the lowest certainty of their inputs;\
      \ BELOW_THRESHOLD vs UNKNOWN per P19; kind lists (P21: research institute, school stage and run_by, scholarly edition);\
      \ first lasting year per P13/P23, no coder's-choice wording. Full before → after list: reports/stage3_rulings_changes.csv.\
      \ Not reviewed."
  - date: '2026-10-02'
    by: Grok Bot
    summary: "P30 rule 5 age sweep: ages recomputed as event year − birth year, with no month adjustment (scripts/recompute_ages.py;\
      \ every change is in reports/p30_age_changes.csv). No other value changed."
  - date: '2026-10-02'
    by: Grok Bot
    summary: "Span alignment (P29, P30 and its addendum): timing.major_work_period checked, 1604–1627 unchanged; worldview.working_years\
      \ 1594–1630 → 1604–1627, equal to the span (P30 addendum f); evidence for every headline value checked against the span;\
      \ no value or certainty changed. Listed in reports/p30_span_alignment.csv. Not reviewed."
  - date: '2026-10-24'
    by: Grok Bot
    summary: "Deepen pass D1 (queue #45). Needs: A faded; B faded (both 1/3 @0.5 scholarly_reconstruction). Verified against\
      \ KGW Digital PDFs (BAdW): De stella nova ch. 22 Latin in KGW 1 p. 257 ('Priusquam autem ad creationem… tentanda omnia\
      \ existimo'); Harmonices mundi IV.1 Latin in KGW 6 p. 223 ('Geometria ante rerum ortum Menti divinae coaeterna, Deus\
      \ ipse…'); Maestlin letter 23 Latin in KGW 13 p. 40 ('Theologus esse volebam…'). MacTutor quotations (Field/Aiton/Duncan/Field)\
      \ as English. P47 source_quality on S1–S10. P48 support: corroborated on A/B/D. A 1 @0.5→0.7 written_profession (alt\
      \ 2); B 3 @0.5→0.7 written_profession (alt 4); D 3 @0.5→0.7; CHRIST @0.5→0.7 written_profession; mid_basin BELOW→true\
      \ @0.7. Chart-moving YES (faded filled → dark filled). No fallacy_catalog (Jason). Draft, not reviewed."
identity:
  id: kepler-johannes
  display_name: Johannes Kepler
  roster:
    canonical_name: Johannes Kepler
    rank: 45
    F: 5
    models:
    - Claude
    - DeepSeek
    - Gemini
    - GPT
    - Grok
    band: high (5)
    status: core
    field: astronomy
    field_bucket: astronomy
  full_name:
    value: Johannes Kepler
    certainty: 1.0
    cites:
    - source: S1
      locator: opening paragraph
    - source: S2
      locator: Quick Info
    how_known: Sources agree.
  native_name:
    value: Johannes Kepler (German)
    certainty: 0.7
    cites:
    - source: S1
      locator: opening paragraph
    how_known: German; he wrote mostly in Latin.
  aliases:
  - name: Johannes-Kepler
    kind: roster alias
  - name: Kepler-Johannes
    kind: roster alias
  - name: Ioannes Keplerus
    kind: latinized
basics:
  birth:
    date:
      value: '1571-12-27'
      calendar: julian
      certainty: 1.0
      cites:
      - source: S1
        locator: Quick Facts
      - source: S2
        locator: Quick Info
      how_known: "Two sources agree on 27 December 1571. Protestant Württemberg still used the Julian calendar; the sources\
        \ do not state the calendar, so the calendar tag is the coder's (flag)."
    place:
      value: "Weil der Stadt, Württemberg"
      modern_name: "Weil der Stadt, Baden-Württemberg, Germany"
      polity_then: Holy Roman Empire
      certainty: 1.0
      cites:
      - source: S1
        locator: Quick Facts
      - source: S2
        locator: Quick Info
      how_known: Two sources agree.
  death:
    date:
      value: '1630-11-15'
      certainty: 1.0
      cites:
      - source: S1
        locator: Quick Facts
      - source: S2
        locator: Quick Info
      how_known: Two sources agree.
    place:
      value: Regensburg
      modern_name: "Regensburg, Germany"
      polity_then: Holy Roman Empire
      certainty: 1.0
      cites:
      - source: S1
        locator: Quick Facts
      - source: S2
        locator: Quick Info
      how_known: Two sources agree.
  first_lasting_contribution_year:
    value: 1604
    certainty: 0.7
    cites:
    - source: S2
      locator: opening paragraph (optics 1604)
    - source: S1
      locator: opening (a new and correct account of how vision occurs)
    how_known: "The earliest listed lasting item (lasting_original_contributions/0): the 1604 optics gave 'a new and correct\
      \ account of how vision occurs' (S1). Rule P13/P23: the year is that of the earliest listed item that is itself lasting.\
      \ Kept at 0.7 until it is checked whether S1–S2 call the Mysterium cosmographicum (1596, a major work, not listed as\
      \ lasting) a lasting contribution (P17)."
  era_bucket:
    value: 1600 to 1749
    certainty: 0.7
    cites:
    - source: S2
      locator: opening paragraph
    how_known: Both candidate years fall in 1600 to 1749 (P2).
  region_of_birth:
    value: Western Europe
    certainty: 1.0
    cites:
    - source: S1
      locator: "Quick Facts ('Württemberg [Germany]')"
    how_known: Germany is Western Europe in data/reference/regions.csv (P3).
  region_of_work:
    value: Eastern Europe
    certainty: 0.7
    cites:
    - source: S2
      locator: "Biography (Prague; Imperial Mathematician after Tycho, 1601)"
    - source: S3
      locator: §1
    how_known: "The optics (1604) and the first two laws (1609) were done in Prague (Czechia is Eastern Europe in regions.csv).\
      \ The third law (Harmonices mundi, 1619) was done in Linz (Austria, Western Europe). Two regions, so 0.7."
    alternatives:
    - value: Western Europe
      cites:
      - source: S2
        locator: Biography (Linz)
      note: Graz 1594–1600 and Linz from 1612 (Austria).
  sex_as_recorded:
    value: male
    certainty: 0.7
    cites:
    - source: S2
      locator: Childhood
    how_known: As the sources record it.
  languages_of_work:
    value:
    - Latin
    - German
    certainty: 0.7
    cites:
    - source: S2
      locator: Biography
    - source: S5
      locator: catalogue note (letters mostly in Latin and German)
    how_known: Latin works; letters in Latin and German.
  occupations:
    value:
    - astronomer
    - mathematician
    - Imperial Mathematician
    - teacher of mathematics
    - astrologer
    certainty: 1.0
    cites:
    - source: S2
      locator: Biography
    - source: S3
      locator: §1
    how_known: Two sources.
contribution:
  era_bucket: early_modern
  fields:
    value:
    - astronomy
    - optics
    - mathematics
    - cosmology
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    - source: S2
      locator: opening paragraph
    how_known: Two sources.
  lasting_original_contributions:
  - value: "Optics: a new and correct account of how vision occurs"
    year: '1604'
    kind: theory
    lasting: Britannica calls it correct
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    - source: S2
      locator: opening paragraph
    how_known: Two sources.
  - value: First and second laws of planetary motion (ellipse; area law)
    year: '1609'
    kind: law or principle
    lasting: Newton derived them from gravitation (S1)
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    - source: S2
      locator: opening paragraph
    how_known: Two sources.
  - value: Third (harmonic) law
    year: '1619'
    kind: law or principle
    lasting: standard astronomy
    certainty: 1.0
    cites:
    - source: S1
      locator: opening
    - source: S2
      locator: The Harmony of the World
    how_known: Two sources.
  - value: Rudolphine Tables
    year: '1627'
    kind: work
    lasting: "their accuracy 'did much to establish the truth of heliocentric astronomy' (S2)"
    certainty: 0.7
    cites:
    - source: S2
      locator: opening paragraph
    how_known: MacTutor.
  evidence_of_impact:
  - value: Laws named after him; Newton derived them from his law of gravity
    kind: named after them
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: Britannica.
  major_works:
  - value: Mysterium cosmographicum
    year: 1596
    kind: book
    certainty: 1.0
    cites:
    - source: S2
      locator: first cosmological model
    - source: S3
      locator: §1
    how_known: Two sources.
  - value: Astronomia nova
    year: 1609
    kind: book
    certainty: 0.7
    cites:
    - source: S2
      locator: Biography
    how_known: MacTutor.
  - value: Harmonices mundi
    year: 1619
    kind: book
    certainty: 0.7
    cites:
    - source: S2
      locator: The Harmony of the World
    how_known: MacTutor.
  honours: []
  definition_fit:
    value: clearly meets
    rationale: The three laws of planetary motion.
    certainty: 0.7
    cites:
    - source: S1
      locator: opening
    how_known: Sources agree.
childhood:
  family_religion:
    value: Lutheran
    certainty: 1.0
    cites:
    - source: S2
      locator: "Childhood ('a bastion of Lutheran orthodoxy')"
    - source: S5
      locator: catalogue introduction (the Lutheran Seminary of Adelberg)
    how_known: Two sources.
  family_religious_practice:
    value: TODO
  parents_and_household:
  - value: Father a mercenary soldier who left when Johannes was five and is believed to have died in the Netherlands war
    role: father
    certainty: 0.7
    cites:
    - source: S2
      locator: Childhood
    how_known: MacTutor.
  - value: "Mother, Katharina, daughter of an innkeeper; later tried for witchcraft"
    name: Katharina Kepler
    role: mother
    certainty: 0.7
    cites:
    - source: S2
      locator: Childhood; Witchcraft trial
    how_known: MacTutor.
  household_circumstances:
    value: "Lived with his mother in his grandfather's inn and helped serve; moved to Leonberg in 1576"
    certainty: 0.7
    cites:
    - source: S2
      locator: Childhood
    how_known: MacTutor.
  schooling:
  - value: "Local (Latin) school, Leonberg"
    stage: grammar or secondary school
    certainty: 0.7
    cites:
    - source: S2
      locator: Childhood
    - source: S5
      locator: catalogue introduction
    how_known: Two sources.
  - value: "Lutheran seminary (Adelberg), intending ordination"
    stage: grammar or secondary school
    certainty: 1.0
    cites:
    - source: S2
      locator: Childhood
    - source: S5
      locator: catalogue introduction
    how_known: Two sources.
    run_by: religious body
  - value: "University of Tübingen (Stift): Magister Artium 1591, then theology"
    stage: university
    years: 1589–1594
    certainty: 1.0
    cites:
    - source: S3
      locator: §1
    - source: S5
      locator: catalogue introduction (enrolled 17 September 1589)
    how_known: Two sources.
  early_mathematics:
    value: arithmetic only
    note: "MacTutor mentions his 'unusual competence at arithmetic' as a child at the inn; nothing more before 17 in the sources\
      \ read"
    certainty: 0.5
    cites:
    - source: S2
      locator: Childhood
    how_known: "One source, framed as the author's surmise."
  early_geometric_style_reasoning:
    value: TODO
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood:
    value:
    - German
    - Latin
    certainty: 0.7
    cites:
    - source: S5
      locator: catalogue introduction (Latin school)
    how_known: Latin school; German native.
  notable_events: []
worldview:
  unit: adult working worldview
  working_years:
    value: 1604–1627
    certainty: 0.7
    cites:
    - source: S2
      locator: opening paragraph
    how_known: "Equal to timing.major_work_period (P30 addendum f; span check 2026-10-02). Was 1594–1630: Graz post to death."
  nominal_affiliations:
  - value: "Lutheran; excommunicated in 1612 and never reinstated, over the Eucharist"
    years: to 1612
    role: member
    certainty: 0.7
    cites:
    - source: S2
      locator: University education
    how_known: MacTutor (one source).
  self_described_science_religion_relation:
    value: "Astronomy as a way to celebrate God: he had wanted to be a theologian, and wrote in 1595 that through his work\
      \ God is celebrated in astronomy; he also wrote that God wants to be known from the book of Nature."
    certainty: 0.7
    cites:
    - source: S9
      locator: "letter 23, KGW 13 p. 40 (Latin)"
    - source: S4
      locator: paragraph 1 (English)
    - source: S10
      locator: Maestlin 1595 quotation
    how_known: "KGW 13 letter 23 Latin verified (S9): 'Theologus esse volebam: diu angebar: Deus ecce mea opera etiam in astronomia\
      \ celebratur' and 'haec ad Dej gloriam, qui vult ex libro Naturae agnoscj'. English matches Bodleian/MacTutor (S4, S10).\
      \ Private letter plus matching public theme in Harmonices; 0.7 (KGW verification + public corroboration)."
  primary_system:
    value: CHRIST
    basis: written_profession
    certainty: 0.7
    cites:
    - source: S8
      locator: "Harmonices IV.1, KGW 6 p. 223 (Creator; image of God; Trinity symbolism)"
    - source: S9
      locator: "letter 23, KGW 13 p. 40"
    - source: S2
      locator: "Kepler's opinions; University education"
    - source: S3
      locator: §2
    how_known: "Public written profession: Harmonices IV.1 names God the Creator who used geometric exemplars and passed them\
      \ to man with the image of God; same chapter marks the Trinity in the sphere (KGW 6 Latin, S8). Letter 23: wanted to\
      \ be a theologian; God celebrated in astronomy (S9). Lutheran affiliation and excommunication (S2). Named alt PLATO;\
      \ 0.7."
    rationale: "CHRIST use_when: Christian belief (Trinity, scripture, church) without a more specific philosophical position.\
      \ Branch: Lutheran, nonconforming on the Eucharist. Named alternative: PLATO (Neoplatonic geometric archetypes, S3);\
      \ not chosen because the framework pictures the Christian Creator and Trinity, which CHRIST's do_not_use_when allows."
  secondary_system:
    value: UNKNOWN
    how_known: "PLATO is a named alternative, but no source read says he professed two systems."
  candidate_codes_considered:
  - code: PLATO
    reason: "Named alternative: Neoplatonic geometric archetypes (S3 §2). PLATO is sourced."
    cites:
    - source: S3
      locator: §2
  - code: CLASS_THEISM
    reason: "Rejected: no classical metaphysics of a simple God in the sources read."
  lio_axes:
    A_locus:
      value: 1
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites:
      - source: S8
        locator: "Harmonices mundi IV.1, KGW 6 p. 223"
      - source: S10
        locator: Harmony of the World IV.1 (Aiton/Duncan/Field trans.)
      - source: S3
        locator: §2 (Creator; polyhedra; Trinity-sphere)
      how_known: "Own public words in Harmonices IV.1, Latin verified in KGW 6 (S8); English Aiton/Duncan/Field via MacTutor\
        \ quotations (S10); SEP reading agrees (S3). Named alt 2; certainty 0.7."
      rationale: "Leans to the transcendent pole: Geometry coeternal with the divine mind supplied God with patterns for creating\
        \ the world and passed to Man with the image of God (Harmonices IV.1). God the Creator is distinct from the world.\
        \ Not 0: the sphere images the Trinity and Geometry is called 'Deus ipse' as divine archetype, so the world mirrors\
        \ God closely. Alternative 2 possible on that image-reading; not chosen. Independent source ids → corroborated (P48)."
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites:
      - source: S7
        locator: "De stella nova ch. 22, KGW 1 p. 257 lines 23–24"
      - source: S10
        locator: De stella nova ch. 22 quotation (Field trans.)
      - source: S2
        locator: "Observational error (New Star of 1604); Kepler's opinions"
      - source: S1
        locator: opening
      how_known: "Own public words: De stella nova ch. 22 Latin verified in KGW 1 (S7); Field English (S10/S2). Working science\
        \ (laws, solar forces) in S1–S2. Named alt 4; certainty 0.7."
      rationale: "Scored on his account of nature (P6). Leans to the law pole: mathematical plan, planetary laws, forces from\
        \ the Sun (S2); astrology restricted to reliable natural influence (S1). Stated limited exception: on the 1604 nova,\
        \ before coming to special creation (finem omnis disputationis) he holds 'tentanda omnia existimo' — try everything\
        \ else first (KGW 1 257). A special creation in nature is kept as a last resort, so 3. Named alternative 4 (natural\
        \ explanation first, special creation not asserted). Independent source ids → corroborated (P48)."
    C_ledger:
      value: UNKNOWN
      how_known: "Nothing on judgement, reward or afterlife in S1–S5."
      note: "Gap: his letters on the Eucharist dispute and his theological writings were not read."
    D_authority:
      value: 3
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites:
      - source: S9
        locator: "letter 23, KGW 13 p. 40 (book of Nature)"
      - source: S8
        locator: Harmonices IV.1 (geometry known to mind; Creator)
      - source: S3
        locator: §2 (Scripture and arrangement of the universe)
      - source: S2
        locator: "Kepler's opinions"
      how_known: "Letter 23: God wants to be known from the book of Nature (S9 Latin). Harmonices presents geometric insights\
        \ as rational (S8). SEP: God in Scripture and in the arrangement of the universe (S3). Named alt 2; 0.7."
      rationale: "Leans to reason: insights are presented as rational demonstration (Harmonices; S2). Stated limited exception:\
        \ God is known from Scripture and from Nature's arrangement (S3; letter 23 book of Nature). Alternative 2 (two domains)\
        \ possible if Astronomia nova introduction on Scripture is read fully; not fully read this pass. Independent source\
        \ ids → corroborated (P48)."
    E_scope:
      value: BELOW_THRESHOLD
      how_known: "Scored on the world's order (P7). Scholars describe one geometric plan for the whole universe, which humans\
        \ 'made in the image of God' can understand (S2, Kepler's opinions; S3, §2), but nothing read addresses favour or\
        \ exceptions for a group in events, and his writing on providence was not read."
      note: "Same treatment as Fermi, Meitner and Curie: not scored from the working science or the cosmology alone, because\
        \ P7's second question (in-group exceptions) needs a statement (§3 same pattern, lens audit batch 2). Was 4 at 0.5."
  mid_basin:
    value: true
    certainty: 0.7
    cites:
    - source: S8
      locator: Harmonices IV.1
    - source: S7
      locator: De stella nova ch. 22
    how_known: "P4 test: A_locus = 1 (≤ 1) at 0.7 and B_cause = 3 (≥ 3) at 0.7, both corroborated (P48), so true. Certainty\
      \ is the lower of the two (P10). F = 5. Chart-moving: faded filled → dark filled."
  statements:
  - text: "Ego verò studeo, ut haec ad Dej gloriam, qui vult ex libro Naturae agnoscj, quam maturrimè vulgentur: […] Sic vovj\
      \ Deo, sic stat sententia. Theologus esse volebam: diu angebar: Deus ecce mea opera etiam in astronomia celebratur."
    cites:
    - source: S9
      locator: "letter 23, KGW 13 p. 40"
    - source: S10
      locator: Maestlin 1595 English
    - source: S4
      locator: paragraph 1
    date: '1595-10-03'
    context: "Letter to Michael Maestlin, 3 October 1595 (KGW 13, letter 23). English (Field): 'I wanted to be a theologian;\
      \ for a long time I was unhappy. Now, behold, God is praised by my work even in astronomy.'"
    axes:
    - D_authority
    - A_locus
    kind: private letter
    verified_against: scholarly edition
    verified_on: '2026-10-24'
    note: Latin verified in BAdW KGW 13 PDF; English matches S4/S10.
  - text: "Priusquam autem ad creationem, hoc est ad finem omnis disputationis, veniamus: tentanda omnia existimo."
    cites:
    - source: S7
      locator: "De stella nova ch. 22, KGW 1 p. 257 lines 23–24"
    - source: S10
      locator: De stella nova ch. 22 (Field trans.)
    - source: S2
      locator: Observational error (New Star of 1604)
    date: '1606'
    context: "De stella nova (Prague, 1606), ch. 22, on the new star of 1604. Field: 'However, before we come to special creation,\
      \ which puts an end to all discussion: I think we should try everything else.'"
    axes:
    - B_cause
    kind: written profession (public)
    verified_against: scholarly edition
    verified_on: '2026-10-24'
    note: Latin verified in BAdW KGW 1 PDF (Caput XXII).
  - text: "Geometria ante rerum ortum Menti divinae coaeterna, Deus ipse (quid enim in Deo, quod non sit Ipse Deus) exempla\
      \ Deo creandi mundi suppeditavit, et cum imagine Dei transivit in hominem: non demum per oculos introrsum est recepta."
    cites:
    - source: S8
      locator: "Harmonices mundi IV.1, KGW 6 p. 223"
    - source: S10
      locator: Harmony of the World IV.1 (Aiton/Duncan/Field p. 304)
    date: '1619'
    context: "Harmonices mundi Book IV, ch. 1. English (Aiton/Duncan/Field): 'Geometry, which before the origin of things\
      \ was coeternal with the divine mind and is God himself (for what could there be in God which would not be God himself?),\
      \ supplied God with patterns for the creation of the world, and passed over to Man along with the image of God.'"
    axes:
    - A_locus
    - D_authority
    kind: written profession (public)
    verified_against: scholarly edition
    verified_on: '2026-10-24'
    note: "Latin verified in BAdW KGW 6 PDF. OCR has spaced letters; wording normalized to standard orthography in the quote\
      \ ('Menti divinae coaeterna')."
  changes_over_life:
  - value: "Gave up ordination for a mathematics post in Graz, perhaps because of doubts about his orthodoxy"
    year: '1594'
    certainty: 0.5
    cites:
    - source: S2
      locator: "University education ('These may explain')"
    how_known: MacTutor offers it as a likely explanation.
  coder_notes: "CHRIST and PLATO are sourced system files. D1 (2026-10-24): KGW 1, 6, 13 PDFs from BAdW publikationen.badw.de\
    \ read for De stella nova, Harmonices IV.1, and Maestlin letter 23. Astronomia nova introduction on Scripture and Methuen\
    \ 1998 still unread (C, D alt 2)."
heritage:
  use: context only — never an outcome and never a worldview code
  ethnic_or_communal_heritage:
    value: Swabian (Württemberg)
    certainty: 0.7
    cites:
    - source: S2
      locator: Childhood
    how_known: MacTutor.
  religious_heritage_by_birth:
    value: Lutheran
    certainty: 1.0
    cites:
    - source: S2
      locator: Childhood
    - source: S5
      locator: catalogue introduction
    how_known: Two sources.
  baptism_or_initiation:
    value: TODO
  childhood_catechism:
    value: Lutheran seminary training for the ministry
    certainty: 1.0
    cites:
    - source: S5
      locator: catalogue introduction
    - source: S2
      locator: Childhood
    how_known: Two sources.
timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period:
    value: 1604–1627
    certainty: 0.7
    cites:
    - source: S2
      locator: opening paragraph
    how_known: Optics to the Rudolphine Tables.
  age_at_first_lasting_contribution:
    value: 33
    certainty: 0.7
    cites:
    - source: S1
      locator: Quick Facts
    how_known: "Born December 1571; 1604 optics. 37 if the 1609 laws are used. P30 (rule 5): 1604 − 1571 = 33, with no month\
      \ adjustment; was 32 until the P30 age sweep (2026-10-02)."
  first_evidence_of_lio_type_views:
    value: "God made the universe by a mathematical plan (Mysterium cosmographicum); geometry coeternal with divine mind (Harmonices\
      \ IV.1, 1619)"
    year: 1596
    certainty: 0.7
    cites:
    - source: S3
      locator: §2
    - source: S2
      locator: first cosmological model
    - source: S8
      locator: Harmonices IV.1 (1619 confirmation)
    how_known: Mysterium 1596 per S2/S3; Harmonices IV.1 (S8) restates Creator-geometry in own words.
  lio_views_relative_to_major_work:
    value: before major work
    rationale: The geometric-plan cosmology of 1596 precedes the 1604 optics and 1609 laws.
    certainty: 0.7
    cites:
    - source: S3
      locator: §2
    how_known: Dates.
  worldview_during_major_work:
    value: Lutheran Christian natural philosophy with a Neoplatonic geometric cosmology
    certainty: 0.7
    cites:
    - source: S8
      locator: Harmonices IV.1
    - source: S7
      locator: De stella nova ch. 22
    - source: S2
      locator: "Kepler's opinions"
    - source: S3
      locator: §2
    how_known: Own words in Harmonices and De stella nova within the working span; scholars agree.
lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present:
    value: 'yes'
    rationale: "Euclid's postulates 'regarded as actually true' as a method for the universe (S2); Euclid XIII's five solids\
      \ drive the 1596 model."
    certainty: 0.7
    cites:
    - source: S2
      locator: "Kepler's opinions; first cosmological model"
    how_known: MacTutor.
  form_acquired:
    value: unclear
    certainty: 0.5
    cites:
    - source: S2
      locator: University education
    how_known: Mathematics at Tübingen; childhood exposure not stated.
  circle_present:
    value: 'no'
    rationale: "God the Creator is the efficient cause, distinct from the world (Harmonices IV.1; S3)."
    certainty: 0.7
    cites:
    - source: S8
      locator: Harmonices IV.1
    - source: S3
      locator: §2
    how_known: Own words (Creator) plus SEP.
  reading: "As belief, not finding: form present, acquisition unclear, no circle. The record does not test H1."
  notes: ''
institutions:
- value: "Protestant school, Graz"
  role: teacher of mathematics
  years: 1594–1600
  kind: employer
  certainty: 0.7
  cites:
  - source: S3
    locator: §1
  how_known: SEP.
- value: "Imperial court, Prague"
  role: "assistant to Tycho, then Imperial Mathematician"
  years: 1600–1612
  kind: patron or funder
  certainty: 1.0
  cites:
  - source: S3
    locator: §1
  - source: S2
    locator: Biography
  how_known: Two sources.
collaborators:
- value: Michael Maestlin
  relation: teacher
  note: introduced him to Copernicus
  certainty: 1.0
  cites:
  - source: S3
    locator: §1
  - source: S2
    locator: University education
  how_known: Two sources.
- value: Tycho Brahe
  relation: mentor or employer
  certainty: 0.7
  cites:
  - source: S3
    locator: §1
  how_known: SEP.
- value: Galileo Galilei
  roster_id: galilei-galileo
  relation: correspondent
  note: "coined 'satellite' in 1610 for the moons Galileo found orbiting Jupiter"
  certainty: 0.7
  cites:
  - source: S2
    locator: "first cosmological model ('satellite')"
  how_known: MacTutor.
- value: Isaac Newton
  roster_id: newton-isaac
  relation: influenced
  note: "derived Kepler's laws from gravitation"
  certainty: 0.7
  cites:
  - source: S1
    locator: opening
  how_known: Britannica.
review:
  roster_status_reason:
    value: "Core in v7.1 (F 4) and v8 (F 5, all five models)."
    certainty: 0.7
    cites:
    - source: S6
      locator: "roster.csv, rank 45"
    how_known: Study roster.
  controversies:
  - value: His mother was tried for witchcraft; he defended her
    certainty: 0.7
    cites:
    - source: S2
      locator: Witchcraft trial
    how_known: MacTutor.
  data_quality_flags:
  - Calendar of the birth date not stated in the sources; tagged julian by the coder.
  - Axis certainties capped at 0.7 by named alternatives (A alt 2; B alt 4; D alt 2) and English translations alongside Latin.
  open_questions:
  - Read Astronomia nova introduction on Scripture (may firm D alt 2 / two domains).
  - "Read Methuen, Kepler's Tübingen (1998), for theology and C_ledger / E_scope."
  - "Herwart von Hohenburg 16 Feb 1605 clockwork letter (KGW 15, 146) for B mechanism wording — English on MacTutor quotations;\
    \ Latin not opened this pass."
  - Baptism / family_religious_practice still TODO.
sources:
- id: S1
  type: tertiary
  kind: encyclopedia
  author: Robert S. Westman
  citation: "Westman, Robert S. \"Johannes Kepler.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Johannes-Kepler."
  url: "https://www.britannica.com/biography/Johannes-Kepler"
  accessed: '2026-10-02'
  reliability_note: Signed article by a historian of astronomy; first page read.
  used_for:
  - identity
  - basics
  - contribution
  - worldview
  - timing
  - collaborators
  source_quality: reference entry
- id: S2
  type: tertiary
  kind: encyclopedia
  author: J. V. Field
  year: 1999
  citation: "Field, J. V. \"Johannes Kepler.\" MacTutor History of Mathematics Archive, University of St Andrews, last updated\
    \ April 1999. https://mathshistory.st-andrews.ac.uk/Biographies/Kepler/."
  url: "https://mathshistory.st-andrews.ac.uk/Biographies/Kepler/"
  accessed: '2026-10-02'
  reliability_note: By a Kepler scholar (translator of Harmonices mundi).
  used_for:
  - identity
  - basics
  - contribution
  - childhood
  - worldview
  - heritage
  - timing
  - lane_b
  - institutions
  - collaborators
  - review
  source_quality: reference entry
- id: S3
  type: tertiary
  kind: encyclopedia
  author: Daniel A. Di Liscia
  year: 2025
  citation: "Di Liscia, Daniel A. \"Johannes Kepler.\" Stanford Encyclopedia of Philosophy, first published 2 May 2011, substantive\
    \ revision 14 September 2025. https://plato.stanford.edu/entries/kepler/."
  url: "https://plato.stanford.edu/entries/kepler/"
  accessed: '2026-10-02'
  reliability_note: Peer-reviewed entry.
  used_for:
  - basics
  - contribution
  - worldview
  - timing
  - lane_b
  - institutions
  - collaborators
  source_quality: reference entry
- id: S4
  type: secondary
  kind: institutional page
  author: Cultures of Knowledge (University of Oxford)
  year: 2016
  citation: "\"'Skybound was the mind': Johannes Kepler.\" Cultures of Knowledge blog, Bodleian Libraries, on the EMLO Kepler\
    \ catalogue. https://www.culturesofknowledge.org/?p=6561."
  url: "https://www.culturesofknowledge.org/?p=6561"
  accessed: '2026-10-02'
  reliability_note: Scholarly project page; quotes the 1595 letter in English.
  used_for:
  - worldview
  source_quality: other
- id: S5
  type: secondary
  kind: database
  author: Early Modern Letters Online (Bodleian Libraries)
  citation: "\"The Correspondence of Johannes Kepler.\" EMLO catalogue introduction. http://emlo-portal.bodleian.ox.ac.uk/collections/?catalogue=johannes-kepler."
  url: "http://emlo-portal.bodleian.ox.ac.uk/collections/?catalogue=johannes-kepler"
  accessed: '2026-10-02'
  reliability_note: "Catalogue introduction; used for Latin school, Adelberg seminary, Tübingen enrolment. Page re-checked\
    \ via prior extract; flag if fuller fetch needed."
  used_for:
  - basics
  - childhood
  - heritage
  source_quality: other
- id: S6
  type: secondary
  kind: database
  author: Neuresthetics Genius Study
  citation: Neuresthetics Genius Study. data/roster/roster.csv (v8 roster).
  url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
  accessed: '2026-10-02'
  reliability_note: "Study's own roster; used only for rank, F and status."
  used_for:
  - identity
  - review
  source_quality: study roster
- id: S7
  type: primary
  kind: scholarly edition
  author: Johannes Kepler; ed. Max Caspar et al.
  year: 1938
  citation: "Kepler, Johannes. Gesammelte Werke, Band I: Mysterium cosmographicum; De stella nova. Ed. Max Caspar. Munich:\
    \ C. H. Beck, 1938 (BAdW digital PDF). De stella nova ch. 22, p. 257. https://publikationen.badw.de/en/002334737/002334737.pdf"
  url: "https://publikationen.badw.de/en/002334737/002334737.pdf"
  accessed: '2026-10-24'
  reliability_note: Critical edition (KGW); Latin of Caput XXII verified in the BAdW PDF this pass.
  source_quality: scholarly edition or monograph
  used_for:
  - worldview
- id: S8
  type: primary
  kind: scholarly edition
  author: Johannes Kepler; ed. Max Caspar
  year: 1940
  citation: "Kepler, Johannes. Gesammelte Werke, Band VI: Harmonices mundi. Ed. Max Caspar. Munich: C. H. Beck, 1940 (BAdW\
    \ digital PDF). Liber IV, Caput I, p. 223. https://publikationen.badw.de/de/002334742/002334742.pdf"
  url: "https://publikationen.badw.de/de/002334742/002334742.pdf"
  accessed: '2026-10-24'
  reliability_note: Critical edition (KGW); Geometry/Creator sentence verified in the BAdW PDF this pass.
  source_quality: scholarly edition or monograph
  used_for:
  - worldview
  - timing
  - lane_b
- id: S9
  type: primary
  kind: scholarly edition
  author: Johannes Kepler; ed. Max Caspar
  year: 1945
  citation: "Kepler, Johannes. Gesammelte Werke, Band XIII: Briefe 1590–1599. Ed. Max Caspar. Munich: C. H. Beck, 1945 (BAdW\
    \ digital PDF). Letter 23 to Maestlin, 3 Oct. 1595, p. 40. https://publikationen.badw.de/en/002334747/002334747.pdf"
  url: "https://publikationen.badw.de/en/002334747/002334747.pdf"
  accessed: '2026-10-24'
  reliability_note: Critical edition of letters; Latin of letter 23 verified in the BAdW PDF this pass.
  source_quality: scholarly edition or monograph
  used_for:
  - worldview
- id: S10
  type: secondary
  kind: institutional page
  author: J. V. Field
  citation: "Field, J. V. \"Quotations by Johannes Kepler.\" MacTutor History of Mathematics Archive, University of St Andrews.\
    \ Translations by J. V. Field unless otherwise attributed; Harmonices IV.1 also Aiton/Duncan/Field 1997. https://mathshistory.st-andrews.ac.uk/Biographies/Kepler/quotations/"
  url: "https://mathshistory.st-andrews.ac.uk/Biographies/Kepler/quotations/"
  accessed: '2026-10-24'
  reliability_note: "Scholar-translator's quotation page with KGW locators; used for English of passages whose Latin was verified\
    \ in S7–S9."
  source_quality: reference entry
  used_for:
  - worldview
---

# Johannes Kepler

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Johannes Kepler (1571–1630), German astronomer, gave the three laws of planetary motion (1609, 1619) and a correct account of vision (1604) [S1, opening; S2, opening paragraph]. Own words (KGW): Geometry coeternal with the divine mind supplied God with patterns for creating the world [S8, Harmonices IV.1]; on the 1604 nova, try everything before special creation [S7, De stella nova ch. 22]; 1595 letter — wanted to be a theologian, God celebrated in astronomy [S9]. CHRIST at 0.7 (PLATO named); A 1 / B 3 at 0.7 corroborated; mid_basin true. Deepen D1 chart-moving yes (faded filled → dark filled).

## Life and work

Born at Weil der Stadt, schooled at a Lutheran seminary and Tübingen, he taught in Graz, succeeded Tycho as Imperial Mathematician in Prague, and later worked in Linz [S2, Childhood; Biography; S3, §1].

## Contribution and impact

Optics (1604), the ellipse and area laws (1609), the harmonic law (1619) and the Rudolphine Tables (1627) [S2, opening paragraph].

## Childhood and education

His father was a mercenary and his mother an innkeeper's daughter; he trained for the Lutheran ministry [S2, Childhood; S5, catalogue introduction].

## Adult working worldview

Letter to Maestlin (1595): "Theologus esse volebam… Deus ecce mea opera etiam in astronomia celebratur"; God wants to be known from the book of Nature [S9, KGW 13 p. 40]. Harmonices IV.1: Geometry coeternal with the divine mind, God himself as archetype, supplied patterns for creating the world [S8, KGW 6 p. 223; S10]. De stella nova ch. 22: before special creation, "tentanda omnia existimo" [S7, KGW 1 p. 257]. Excommunicated in 1612 over the Eucharist [S2, University education]. Scores: A 1 (0.7, corroborated), B 3 (0.7, corroborated), D 3 (0.7, corroborated); C UNKNOWN, E below threshold; mid_basin true @ 0.7.

## Heritage (context only)

Swabian Lutheran [S2, Childhood]. Context only.

## Timing

First lasting contribution 1604, at 33 [S1, Quick Facts]. The God-made geometric plan of 1596 comes before it [S3, §2]; restated in Harmonices 1619 [S8].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Euclidean form is central [S2, Kepler's opinions]; no circle — Creator distinct from the world [S8; S3].

## Open questions

- Astronomia nova introduction on Scripture; Methuen 1998; Herwart 1605 clockwork letter Latin; baptism / family practice.

## Research log

- 2026-10-02: Read Britannica (Westman, first page), MacTutor (Field), SEP (Kepler) and the Cultures of Knowledge post. EMLO's catalogue text came only through a search extract. No primary text read.
- 2026-10-24: Deepen D1. Opened BAdW KGW PDFs: Band I (De stella nova ch. 22), Band VI (Harmonices IV.1), Band XIII (letter 23). MacTutor quotations for Field/Aiton English. P47/P48. No fallacy_catalog.
