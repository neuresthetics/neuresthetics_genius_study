---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 5
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch W)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: '2026-10-25'
  change_log:
    - {date: 2026-10-25, by: "Grok Bot", summary: "Perpetual deepen: family_religion TODO synced from religious_heritage_by_birth (context only). Chart-moving NO. No figures/; no fallacy_catalog."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #122 / F4 rank 123). Goals: raise B if justified; corroborate A (P48); mid if B≥0.7. Re-read De revolutionibus dedication, I.4, I.9, I.10 on Latin Wikisource (S3) against Rosen English (S5, Reed/Octavo PDF of Rosen 1978); Commentariolus uniformity language via Rosen Three Copernican Treatises English on erenow (S6); Wikipedia EN dual bio (S7, P50). A 1 stays @0.7 written_profession; support single→corroborated (S3+S5). B 3 stays @0.5: basis inference_from_work→written_profession (I.4 'certa lege' / constant law; Commentariolus 'rule of absolute motion'); P16 Hilbert / P35 keep 0.5 without a stated no-exception or limited-exception claim (alt 4); support corroborated. mid_basin stays BELOW_THRESHOLD (B under 0.7 bar). primary_system stays BELOW_THRESHOLD, CHRIST lead (ruling W1). Chart-moving NO (still faded). P47 source_quality on S1–S7. No fallacy_catalog. No figures/. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Batch W audit notes tidied (no score change): primary_system how_known now marks the brackets in 'Opt[imi]. Max[imi].' as the Wikisource editor's; A_locus how_known records why the I.10 'Trimegistus visibilem Deum' line is not used (it reports what others call the Sun, not his own profession)."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Audit fixes for batch W (gs_2584730_W run 1): (CO4) dedication locator djvu p. 7 -> p. 8 in all five cites (statement, nominal_affiliations, self_described relation, D and its alternative), and the inflected form 'Reipublicæ ecclesiasticæ conducere' quoted in place of 'Respublica ecclesiastica'. Ruling W1 (v8's call on the auditor's advice): primary_system stays BELOW_THRESHOLD, CHRIST the lead. (Notes) S1 credits Westman and Britannica Editors; Britannica and SEP typed tertiary. No scored value changes."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch W, order P32: F 4, rank 123). Basics from Britannica (Robert S. Westman) and SEP (Sheila Rabin). Own voice read in Latin in the 1543 De revolutionibus on Latin Wikisource (dedication to Paul III, proofread; I.9 proofread; I.10 not yet proofread). Scientist (P30). primary_system BELOW_THRESHOLD (CHRIST lead; generic creator language plus a canon's office, by analogy with ruling U2); A 1 (0.7, alt 0); B 3 (0.5, alt 4); C UNKNOWN; D 2 (0.5, alt 3); E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD (B at 0.5). Span 1514–1543 (0.5). Plotted (faded). Draft, not reviewed."}

identity:
  id: copernicus-nicolaus
  display_name: "Nicolaus Copernicus"
  roster:
    canonical_name: "Nicolaus Copernicus"
    rank: 123
    F: 4
    models: [Claude, DeepSeek, Gemini, Grok]
    band: "core (3–4)"
    status: core
    field: astronomy
    field_bucket: astronomy
  full_name: {value: "Nicolaus Copernicus", certainty: 0.7, cites: [{source: S1, locator: "facts box; opening"}], how_known: "Britannica; Latin form of his name."}
  native_name: {value: "Mikołaj Kopernik (Polish); Nikolaus Kopernikus (German)", certainty: 0.7, cites: [{source: S1, locator: "facts box ('German: Nikolaus Kopernikus'; 'Also known as: Mikołaj Kopernik')"}], how_known: "Britannica gives both forms; SEP: 'the child of a German family was a subject of the Polish crown' (S2, §1)."}
  aliases:
    - {name: "Copernicus-Nicolaus", kind: "roster alias"}
    - {name: "Mikołaj Kopernik", kind: "other"}
    - {name: "Nikolaus Kopernikus", kind: "other"}

basics:
  birth:
    date: {value: "1473-02-19", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "facts box (Born); 'Early life and education'"}, {source: S2, locator: "§1"}], how_known: "Britannica and SEP agree; Britannica notes the date comes 'According to a later horoscope', so 0.7. Julian calendar (before 1582)."}
    place: {value: "Toruń", modern_name: "Toruń, Poland", polity_then: "Royal Prussia, Kingdom of Poland", certainty: 1.0, cites: [{source: S1, locator: "facts box (Born)"}, {source: S2, locator: "§1"}], how_known: "Both sources."}
  death:
    date: {value: "1543-05-24", calendar: julian, certainty: 1.0, cites: [{source: S1, locator: "facts box (Died)"}, {source: S2, locator: "§1 ('on 24 May 1543 Copernicus held a copy of the finished work on his deathbed')"}], how_known: "Britannica; SEP agrees."}
    place: {value: "Frauenburg", modern_name: "Frombork, Poland", polity_then: "Prince-Bishopric of Warmia, Kingdom of Poland", certainty: 0.7, cites: [{source: S1, locator: "facts box (Died: 'Frauenburg, East Prussia [now Frombork, Poland]')"}, {source: S2, locator: "§1"}], how_known: "Britannica; SEP says he lived at Frombork from 1510 'the rest of his life'. polity_then is the coder's (0.7)."}
  first_lasting_contribution_year: {value: 1514, certainty: 0.5, cites: [{source: S1, locator: "opening ('sometime between 1508 and 1514')"}, {source: S2, locator: "§1 ('Sometime between 1510 and 1514')"}], how_known: "The heliocentric theory, first set out in the Commentariolus. The sources date it within a window (Britannica 1508–1514, SEP 1510–1514), not as a work in progress, so the coder takes the latest year both allow (1514). Named alternatives: 1508 and 1510."}
  era_bucket: {value: "1400 to 1599", certainty: 1.0, cites: [{source: S1, locator: "facts box"}], how_known: "Whole working life in the bucket (P2)."}
  region_of_birth: {value: "Eastern Europe", certainty: 1.0, cites: [{source: S1, locator: "facts box"}, {source: S2, locator: "§1"}], how_known: "Poland is Eastern Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Eastern Europe", certainty: 1.0, cites: [{source: S1, locator: "body"}, {source: S2, locator: "§1"}], how_known: "Frombork and Lidzbark (Warmia), Poland; his studies in Italy (1496–1503) came before the span."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "As recorded."}
  languages_of_work: {value: ["Latin"], certainty: 0.7, cites: [{source: S3, locator: "Praefatio; Liber I"}, {source: S2, locator: "§1 (Latin the language of the universities; Greek read)"}], how_known: "De revolutionibus is in Latin; SEP on his Greek."}
  occupations: {value: ["astronomer", "canon of the Warmia cathedral chapter (administrator)", "physician"], certainty: 1.0, cites: [{source: S1, locator: "'What did Nicolaus Copernicus do for a living?'; 'Early life and education'"}, {source: S2, locator: "§1"}], how_known: "Both sources. Britannica: 'Despite serving as a canon, Copernicus did not become a priest.'"}

contribution:
  fields: {value: ["astronomy", "mathematics"], certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "§2"}], how_known: "Britannica and SEP."}
  lasting_original_contributions:
    - {value: "Heliocentric theory: the planets' motions referred to the Sun; Earth a planet with a daily rotation and annual orbit; slow change of the axis explains precession (first set out in the Commentariolus)", year: 1514, kind: theory, lasting: "'Copernicus's theory had important consequences for later thinkers of the Scientific Revolution, including such major figures as Galileo, Kepler, Descartes, and Newton' (S1); 'Copernicus came to be seen as the initiator of what is commonly known as the Scientific Revolution' (S2, opening)", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "opening; §1; §2.2"}], how_known: "Britannica and SEP. Year: the Commentariolus window (1508–1514 S1, 1510–1514 S2); 1514 taken (see first_lasting_contribution_year)."}
    - {value: "De revolutionibus orbium coelestium libri vi: the full mathematical version of the heliocentric system, ordering the planets by their periods and replacing Ptolemy's equant", year: 1543, kind: work, lasting: "'the book that contains the final version of his theory' (S1); 'the majority of sixteenth-century astronomers thought eliminating the equant was Copernicus' big achievement' (Gingerich, quoted in S2 §2.6)", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "§2.3; §2.6"}], how_known: "Both sources. Published 1543 (Nuremberg)."}
  evidence_of_impact:
    - {value: "Heliocentric system 'usually called' after the Sun; theory shaped Galileo, Kepler, Descartes and Newton", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    - {value: "Prutenic Tables (Reinhold) built on his models were more widely adopted than the Alfonsine Tables", kind: "institutional or technological lineage", certainty: 0.7, cites: [{source: S2, locator: "§2.6"}], how_known: "SEP."}
  major_works:
    - {value: "De revolutionibus orbium coelestium", year: 1543, kind: book, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "§2.3"}], how_known: "Both sources."}
    - {value: "Commentariolus", year: 1514, kind: other, certainty: 0.5, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "§2.2"}], how_known: "Manuscript sent to astronomers, never printed in his lifetime (S2); dated within 1508–1514 (see above)."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Originator of the heliocentric system, the start of the Scientific Revolution (S1, S2).", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "opening"}], how_known: "Coder's reading of both sources."}

childhood:
  family_religion: {value: "Catholic (Latin Church)", certainty: 0.5, cites: [{source: S2, locator: "§1"}], how_known: "Same as religious_heritage_by_birth (uncle-bishop / church career milieu)."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father: Nicolaus Copernicus Sr., well-to-do merchant (died 1483, or between 1483 and 1485 per S1)", certainty: 0.7, cites: [{source: S2, locator: "§1"}, {source: S1, locator: "'Early life and education'"}], how_known: "SEP gives 1483; Britannica 'sometime between 1483 and 1485'."}
    - {value: "Mother: Barbara Watzenrode, of a leading merchant family", certainty: 1.0, cites: [{source: S1, locator: "'Early life and education'"}, {source: S2, locator: "§1"}], how_known: "Both sources."}
    - {value: "Maternal uncle Lucas Watzenrode (1447–1512), later bishop of Warmia, took the children under his protection and directed his education and church career", certainty: 1.0, cites: [{source: S1, locator: "'Early life and education'"}, {source: S2, locator: "§1"}], how_known: "Both sources."}
  household_circumstances: {value: "Youngest of four children of a merchant family; fatherless from about age 10, raised under a cleric uncle's protection", certainty: 0.7, cites: [{source: S2, locator: "§1"}, {source: S1, locator: "'Early life and education'"}], how_known: "Both sources."}
  schooling:
    - {value: "University of Cracow (liberal arts, including astronomy and astrology); no degree", stage: university, run_by: other, years: "1491–c. 1494", certainty: 1.0, cites: [{source: S1, locator: "'Early life and education'"}, {source: S2, locator: "§1"}], how_known: "Both sources; end year Britannica's 'about 1494'."}
    - {value: "University of Bologna (canon law); lived with the astronomer Domenico Maria Novara", stage: university, run_by: other, years: "1496–1500", certainty: 1.0, cites: [{source: S1, locator: "'Early life and education'"}, {source: S2, locator: "§1"}], how_known: "Both sources."}
    - {value: "University of Padua (medicine); doctorate in canon law from Ferrara, May 1503", stage: university, run_by: other, years: "1501–1503", certainty: 1.0, cites: [{source: S1, locator: "'Early life and education'"}, {source: S2, locator: "§1"}], how_known: "Both sources."}
  early_mathematics: {value: "advanced mathematics", certainty: 0.5, cites: [{source: S2, locator: "§1"}], how_known: "Cracow offered mathematics and astronomy and he bought books on them there (S2); level is the coder's reading."}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure:
    - {value: "Astronomy and astrology at Cracow; assistant to Novara's observations at Bologna (first known observation 9 March 1497)", certainty: 0.7, cites: [{source: S1, locator: "'Early life and education'"}], how_known: "Britannica."}
  key_early_reading:
    - {value: "Regiomontanus, Epitome of Ptolemy's Almagest; Pico della Mirandola, Disputations against Divinatory Astrology ('probably' introduced by Novara)", certainty: 0.5, cites: [{source: S1, locator: "'Early life and education'"}], how_known: "Britannica's 'probably', so 0.5."}
  childhood_mentors:
    - {value: "Lucas Watzenrode (uncle)", certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "SEP."}
  languages_in_childhood: {value: ["German"], certainty: 0.5, cites: [{source: S2, locator: "§1 ('the child of a German family')"}], how_known: "Coder's reading of 'German family'."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1514–1543", certainty: 0.5, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "§1"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Canon of the Frombork (Warmia) cathedral chapter from 1495/1497 to his death; not a priest", certainty: 1.0, cites: [{source: S1, locator: "'Early life and education'"}, {source: S2, locator: "§1"}], how_known: "Both sources. Office at membership level, not a code."}
    - {value: "Dedicated De revolutionibus to Pope Paul III, offering his work as useful to the Church's calendar reform ('Reipublicæ ecclesiasticæ conducere')", certainty: 0.7, cites: [{source: S3, locator: "Praefatio Authoris (djvu p. 8)"}, {source: S2, locator: "§2.5 ('probably for political reasons')"}], how_known: "His dedication; SEP reads the dedication as probably political. Context."}
  self_described_science_religion_relation: {value: "Mathematics is for mathematicians: critics 'ignorant of mathematics' who twist 'some passage of Scripture' against astronomy are to be disregarded, as Lactantius spoke 'childishly' of the Earth's shape (1542)", certainty: 0.7, cites: [{source: S3, locator: "Praefatio Authoris (djvu p. 8)"}, {source: S1, locator: "'Early life and education' (last paragraph)"}, {source: S2, locator: "§2.5"}], how_known: "His dedication, published 1543; Britannica dates its composition to 1542; SEP glosses it as 'theologians should not meddle with it'."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "Coder's call, by analogy with ruling U2 (Cervantes). His own words read name a creator but nothing specifically Christian: the world machine was founded 'propter nos, ab optimo & regularissimo omnium opifice' (dedication), gravity is implanted 'à divina providentia opificis universorum' (I.9), and the cosmos is 'divina haec Opt[imi]. Max[imi]. fabrica' (I.10; brackets are the Wikisource editor's). His church office is membership (CHRIST do_not_use_when), and the dedication to the Pope is 'probably for political reasons' (S2 §2.5). CHRIST is the named lead; a profession of doctrine (Christ, the Church's teaching) in his own words would restore it. Ruling W1 (v8's call on the auditor's advice, batch W audit): stays BELOW_THRESHOLD, CHRIST the lead."}
  secondary_system: {value: UNKNOWN, how_known: "None (P29)."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Named lead: Catholic canon; creator language in his dedication to the Pope. Not chosen: no own-voice doctrinal profession read (ruling U2 by analogy)."}
    - {code: CLASS_THEISM, reason: "Rejected: 'Best and Greatest' maker language is not a stated Thomist doctrine of God."}
    - {code: PLATO, reason: "Rejected: SEP (§2.2) argues against reading Neoplatonism or Hermetism as his motive."}
  lio_axes:
    A_locus:
      value: 1
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S3, locator: "Praefatio Authoris (djvu p. 6); Liber I cap. 9 (fol. 7a); cap. 10 (fol. 10a)"}, {source: S5, locator: "preface 3 (Artisan); I.9 (Creator); I.10 (divine handiwork / Almighty)"}]
      rationale: "Leans to the transcendent pole: the world machine was 'founded for us by the best and most orderly maker of all' ('qui propter nos, ab optimo & regularissimo omnium opifice, conditus esset'); gravity is 'a natural appetency implanted in the parts by the divine providence of the maker of all things'; the cosmos is 'this divine work of the Best and Greatest' / Rosen 'divine handiwork of the most excellent Almighty'. The maker is distinct from the world he made. Not 0: no intervention, miracle, petition or revelation is mentioned; providence acts by an implanted natural tendency. Named alternative 0: a maker who made the world 'propter nos' is the personal creator of the CHRIST pole (Galileo precedent)."
      how_known: "Published book, his own Latin on Wikisource (S3) cross-checked to Rosen English (S5). Independent source ids → corroborated (P48). Capped at 0.7 because 0 is named (Galileo precedent). The dedication's political purpose (S2 §2.5) does not touch I.9 and I.10. Not used: the I.10 line on the Sun, 'Trimegistus visibilem Deum', reports what others call the Sun, not his own profession (batch W audit, RQ-W1)."
      alternatives:
        - {value: 0, note: "Personal creator who made the world for us.", cites: [{source: S3, locator: "Praefatio Authoris (djvu p. 6)"}, {source: S5, locator: "preface 3"}]}
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.5
      support: corroborated
      cites: [{source: S3, locator: "Liber I cap. 4 (djvu pp. 18–19: 'certa lege'); Praefatio (djvu p. 6: 'regularissimo'); Liber I cap. 9"}, {source: S5, locator: "I.4 ('constant law'); preface 3 (systematic Artisan); I.9"}, {source: S6, locator: "Commentariolus opening ('rule of absolute motion' / uniform about proper center)"}, {source: S2, locator: "§2.2; §2.3"}]
      rationale: "Scored on his account of nature (P6). Own published words: celestial inequalities 'observant' a 'certa lege' / Rosen 'constant law' with fixed restorations (I.4); defects are 'indignum' in bodies 'in optima … ordinatione constituta'; the maker is 'regularissimus'; gravity is an implanted natural appetency (I.9). Commentariolus (unpublished in his lifetime) seeks an arrangement where everything moves uniformly about its proper center 'as the rule of absolute motion requires' (S6). No stated miracle, petition, or no-exception claim → B 3 at 0.5, alternative 4 (P16 Hilbert addendum / P35), never 4."
      how_known: "Written profession in De revolutionibus I.4 (S3 Latin proofread level 3; S5 Rosen English). Commentariolus (S6) and SEP (S2) corroborate. Certainty held at 0.5: explicit lawful-order remark without a stated no-exception or limited-exception claim (P16 Hilbert; P35)."
      alternatives:
        - {value: 4, note: "P16 Hilbert / P35: lawful-order remark without a no-exception claim cannot score 4.", cites: [{source: S3, locator: "Liber I cap. 4"}, {source: S5, locator: "I.4"}]}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read on reward and punishment of persons (P19)."}
    D_authority:
      value: 2
      basis: written_profession
      certainty: 0.5
      cites: [{source: S3, locator: "Praefatio Authoris (djvu p. 8)"}, {source: S2, locator: "§2.5"}]
      rationale: "Two domains: in astronomy, mathematics decides, and critics who reach a verdict 'propter aliquem locum scripturae, male ad suum propositum detortum' are to be scorned ('tanquam temerarium contemnam'); 'Mathemata mathematicis scribuntur'. He says the passage is misread, not that Scripture is overruled, and offers the work to the Church's calendar reform, so revelation keeps its own domain (D 2 anchor, P27). Named alternative 3: he states no religious domain beyond leaving theology to theologians."
      how_known: "His dedication (written 1542, printed 1543). 0.5: the other domain is the coder's inference, and SEP reads the dedication as 'probably for political reasons'."
      alternatives:
        - {value: 3, note: "Religion's say not stated at all in the passage.", cites: [{source: S3, locator: "Praefatio Authoris (djvu p. 8)"}]}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Scored on the world's order (P7). Lead toward 3–4: gravity, a natural appetency in Earth's parts, is 'credibile' also in the Sun, Moon and planets (I.9), one rule for Earth and heavens. But it is one property, stated as credible, and says nothing of living beings or humans; working science alone does not score E (P19)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "P4 test: A 1 at 0.7 passes, but B 3 remains at 0.5 under P16 Hilbert / P35 (I.4 'certa lege' states lawfulness without a no-exception or limited-exception claim), under the test's 0.7 bar. Deepen D1 did not darken B."}
  statements:
    - text: "cœpit me tædere, quòd nulla certior ratio motuum machinæ mundi, qui propter nos, ab optimo & regularissimo omnium opifice, conditus esset, philosophis constaret"
      cites: [{source: S3, locator: "Praefatio Authoris (djvu p. 6)"}]
      date: "1542"
      context: "Dedication to Pope Paul III: why he began to doubt the received astronomy."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "Latin Wikisource transcription of the 1543 Nuremberg edition, page proofread (level 4). Composed 1542 (S1), printed 1543."
    - text: "Si fortasse erunt ματαιόλογοι, qui cum omnium Mathematum ignari sint, tamen de illis indicium sibi sumunt, propter aliquem locum scripturæ, male ad suum propositum detortum, ausi fuerint meum hoc institutum reprehendere ас insectari: illos nihil moror, adeo ut etiam illorum iudicium tanquam temerarium contemnam. Non enim obscurum est Lactantium, celebrem alioqui scriptorem, sed Mathematicum parum, admodum pueriliter de forma terræ loqui [...] Mathemata mathematicis scribuntur"
      cites: [{source: S3, locator: "Praefatio Authoris (djvu p. 8)"}]
      date: "1542"
      context: "Same dedication, on critics who might cite Scripture against him; he then offers the work as useful to the Church's calendar reform ('Reipublicæ ecclesiasticæ conducere', same page)."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "Same edition, proofread page (level 4); 'indicium' as transcribed (for 'iudicium'). Britannica and SEP translate the last clause ('mathematics is written for mathematicians')."
    - text: "Equidem existimo, gravitatem non aliud esse, quàm appetentiam quandam naturalem partibus inditam à divina providentia opificis universorum, ut in unitatem integritatemque suam sese conferant in formam globi coëuntes. Quam affectionem credibile est etiam Soli, Lunæ, cæterisque errantium fulgoribus inesse"
      cites: [{source: S3, locator: "Liber I cap. 9 (fol. 7a; djvu p. 27)"}]
      date: "1543"
      context: "Book I, ch. 9, whether the Earth can have several motions, and on the centre of the world."
      axes: [A_locus, B_cause, E_scope]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "Same edition, page proofread (level 3)."
    - text: "Tanta nimirum est divina haec Opt[imi]. Max[imi]. fabrica."
      cites: [{source: S3, locator: "Liber I cap. 10 (fol. 10a; djvu p. 33)"}]
      date: "1543"
      context: "Close of Book I, ch. 10, on the order of the heavenly spheres, after the argument for the immense distance of the fixed stars."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "Same edition; this page is not yet proofread on Wikisource (level 1), so it is supporting only; A rests on the proofread dedication and I.9. Rosen English (S5) agrees on 'divine handiwork of the most excellent Almighty'."
    - text: "Fateri nihilominus oportet circulares esse motus, vel ex pluribus circulis compositos, eo quòd inæqualitates huiusmodi certa lege, statisque observant restitutionibus, quòd fieri non posset, si circulares non essent. [...] Cum vero ab utroque abhorreat intellectus, sitque indignum tale quiddam in illis existimari, quae in optima sunt ordinatione constituta"
      cites: [{source: S3, locator: "Liber I cap. 4 (djvu pp. 18–19)"}, {source: S5, locator: "I.4 ('constant law'; 'best order')"}]
      date: "1543"
      context: "Book I, ch. 4: celestial motions are circular or compounded of circles because inequalities recur by a constant law; defects in the moving force are unworthy of bodies constituted in the best order."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Latin Wikisource pages proofread (level 3). Rosen: 'these nonuniformities recur regularly according to a constant law'; 'It is improper to conceive any such defect in objects constituted in the best order'."
    - text: "Having become aware of these defects, I often considered whether there could perhaps be found a more reasonable arrangement of circles, from which every apparent inequality would be derived and in which everything would move uniformly about its proper center, as the rule of absolute motion requires."
      cites: [{source: S6, locator: "Commentariolus, opening (Rosen English)"}]
      date: "1514"
      context: "Commentariolus preface: motive for the seven postulata — save uniform circular motion without the equant."
      axes: [B_cause]
      kind: "unpublished manuscript"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Never printed in his lifetime (S2 §2.2). English from Rosen Three Copernican Treatises via erenow.org (S6); unofficial web copy → 0.7 field cap if alone; here supporting I.4. Date: Commentariolus window; 1514 taken as elsewhere."
  changes_over_life: []
  coder_notes: "Deepen D1 2026-10-24: A corroborated (S3+S5); B upgraded to written_profession on I.4 'certa lege' but certainty stays 0.5 (P16 Hilbert / P35); mid still BELOW; primary stays BELOW_THRESHOLD / CHRIST lead (W1). Coder's call. Osiander's anonymous preface ('Ad lectorem'), which calls the system a hypothesis, is not Copernicus's (S2 §2.5) and is not used. Span start: the Commentariolus is dated only within a window (1508–1514, S1; 1510–1514, S2); 1514 taken, 1508 and 1510 named. primary_system is BELOW_THRESHOLD with CHRIST as lead (RQ-W1): his own words give a transcendent maker (A 1) but no doctrine, and his office is membership; if the auditor reads the dedication to the Pope plus the creator language as enough, CHRIST at 0.5 is the alternative. Plotted (faded): A 1 at 0.7 (now corroborated) and B 3 at 0.5 (written_profession; P16 Hilbert bar)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "German merchant family, subject of the Polish crown", certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "SEP; Britannica's Researcher's Note on his nationality was not read."}
  religious_heritage_by_birth: {value: "Catholic (Latin Church)", certainty: 0.5, cites: [{source: S2, locator: "§1"}], how_known: "Inferred: his uncle was a bishop and steered him to a church career; baptism not stated."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1514–1543", certainty: 0.5, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "§1; §2.2; §2.3"}], how_known: "From the Commentariolus (window 1508–1514; 1514 taken) to De revolutionibus (1543) (P12, P30). Alternative starts 1508 and 1510."}
  age_at_first_lasting_contribution: {value: 41, certainty: 0.5, cites: [{source: S1, locator: "facts box; opening"}], how_known: "1514 − 1473 = 41 (P30); 35 or 37 on the alternative starts."}
  first_evidence_of_lio_type_views: {value: "c. 1514 Commentariolus: uniform circular motion as the 'rule of absolute motion' (B); 1542–1543 De revolutionibus: 'regularissimus' maker, I.4 'certa lege', I.9 implanted appetency (A+B)", year: 1514, certainty: 0.5, cites: [{source: S6, locator: "Commentariolus opening"}, {source: S3, locator: "Praefatio Authoris; Liber I cap. 4; cap. 9"}], how_known: "Commentariolus supplies the earliest B-type lawfulness read (unpublished manuscript); A statements begin in the 1542 dedication / 1543 books."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.5, cites: [{source: S3, locator: "Praefatio Authoris; Liber I cap. 9"}], how_known: "De revolutionibus closes the span."}
  worldview_during_major_work: {value: "A transcendent, orderly maker of a world made for us; astronomy decided by mathematics, with misread Scripture set aside", certainty: 0.5, cites: [{source: S3, locator: "Praefatio Authoris; Liber I cap. 9–10"}], how_known: "Coder's summary of the statements."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "A geometric model of uniform circular motions ordered around the Sun (S2 §2.2–2.3).", certainty: 0.5, cites: [{source: S2, locator: "§2.2; §2.3"}], how_known: "Coder's reading."}
  form_acquired: {value: "adulthood, before major work", certainty: 0.5, cites: [{source: S1, locator: "'Early life and education'"}], how_known: "Ptolemaic astronomy learned at Cracow and Bologna (Regiomontanus's Epitome)."}
  circle_present: {value: "partly", rationale: "An orderly maker and a harmony of the spheres ('certum harmoniae nexum', I.10) are present, but the maker stays distinct from the world.", certainty: 0.5, cites: [{source: S3, locator: "Liber I cap. 10"}], how_known: "Coder's reading."}
  reading: "A geometrically ordered cosmos made by a best and most orderly maker; mathematics as the judge in astronomy."
  notes: ""

institutions:
  - {value: "Cathedral chapter of Warmia (Frombork)", role: "canon: administration of holdings, finances, defence; physician to the bishop and canons", years: "1497–1543", kind: "religious body", certainty: 1.0, cites: [{source: S1, locator: "'Early life and education'"}, {source: S2, locator: "§1"}], how_known: "Both sources; elected 1495, assumed the post two years later (S2)."}
  - {value: "Fifth Lateran Council (calendar reform)", role: "invited to give an opinion (1514); never attended", years: "1514", kind: "religious body", certainty: 0.7, cites: [{source: S1, locator: "'Early life and education' (last paragraph)"}], how_known: "Britannica."}
collaborators:
  - {value: "Lucas Watzenrode", relation: family, note: "maternal uncle, bishop of Warmia, patron", certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "SEP."}
  - {value: "Domenico Maria Novara", relation: teacher, note: "astronomy professor at Bologna; Copernicus his 'assistant and witness'", certainty: 0.7, cites: [{source: S1, locator: "'Early life and education'"}, {source: S2, locator: "§1"}], how_known: "Both sources."}
  - {value: "Georg Joachim Rheticus", relation: "student or assistant", note: "visited 1539, wrote the Narratio prima, persuaded him to publish and oversaw printing", certainty: 0.7, cites: [{source: S2, locator: "§1; §2.4; §2.5"}], how_known: "SEP."}
  - {value: "Andreas Osiander", relation: other, note: "Lutheran minister who finished seeing the book through the press and added an anonymous preface", certainty: 0.7, cites: [{source: S2, locator: "§2.5"}], how_known: "SEP."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 123"}], how_known: "Study roster."}
  controversies:
    - {value: "Osiander's unsigned preface presented the work as hypothesis only", certainty: 0.7, cites: [{source: S2, locator: "§2.5"}], how_known: "SEP."}
    - {value: "Luther may have spoken against heliocentrism as contrary to the Bible; Bartolomeo Spina intended to condemn the book; no official Catholic position by 1600", certainty: 0.7, cites: [{source: S2, locator: "§2.6"}], how_known: "SEP."}
  data_quality_flags:
    - "Commentariolus date differs by source (1508–1514 vs 1510–1514); span start is the coder's pick."
    - "I.10 page not yet proofread on Wikisource; supporting only (Rosen English agrees)."
    - "Commentariolus English read as unofficial web copy of Rosen (S6); Latin MS not opened."
  open_questions:
    - "Settled (ruling W1): primary_system stays BELOW_THRESHOLD with CHRIST as the lead; an own-voice profession of doctrine would restore CHRIST."
    - "B certainty stays 0.5 under P16 Hilbert / P35 unless a later primary states a limited exception (miracle/creation) or an explicit no-exception claim."
    - "Letter against Werner (1524) not opened this pass (Rosen Three Treatises); may add nature-order language but unlikely to break the Hilbert bar alone."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Robert S. Westman and Britannica Editors"
    citation: "Westman, Robert S., and Britannica Editors. \"Nicolaus Copernicus.\" Encyclopaedia Britannica (updated 15 October 2026). https://www.britannica.com/biography/Nicolaus-Copernicus. Read live 2026-10-19; re-checked 2026-10-24."
    url: "https://www.britannica.com/biography/Nicolaus-Copernicus"
    accessed: 2026-10-24
    reliability_note: "Signed body read through 'Early life and education'; question boxes used only where the body repeats them."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, timing, institutions, collaborators]
  - id: S2
    type: tertiary
    kind: encyclopedia
    author: "Sheila Rabin"
    citation: "Rabin, Sheila. \"Nicolaus Copernicus.\" Stanford Encyclopedia of Philosophy (first published 30 November 2004; substantive revision 29 September 2023). https://plato.stanford.edu/entries/copernicus/"
    url: "https://plato.stanford.edu/entries/copernicus/"
    accessed: 2026-10-24
    reliability_note: "Signed scholarly encyclopedia entry."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, collaborators, review]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "Nicolaus Copernicus"
    citation: "Copernicus, Nicolaus. De revolutionibus orbium coelestium, libri VI. Nuremberg: Johannes Petreius, 1543. Latin Wikisource transcription from the scan 'Nicolai Copernici torinensis De revolutionibus orbium coelestium.djvu' (Praefatio Authoris, djvu pp. 4–8; Liber I cap. 4, djvu pp. 18–19; Liber I, djvu pp. 15–33)."
    url: "https://la.wikisource.org/wiki/De_revolutionibus_orbium_coelestium"
    accessed: 2026-10-24
    reliability_note: "Page-by-page transcription against the scan: dedication pages proofread (level 4), I.4 and I.9 proofread (level 3), I.10 not proofread (level 1). Deepen D1 re-read I.4 for 'certa lege'. Imprint from SEP (S2 §2.5)."
    source_quality: "primary / own words"
    used_for: [basics, worldview, timing, lane_b]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S5
    type: primary
    kind: "published work by the subject"
    author: "Nicolaus Copernicus (trans. Edward Rosen)"
    citation: "Copernicus, Nicolaus. On the Revolutions. Translation and commentary by Edward Rosen (Polish Scientific Publishers / Macmillan, 1978). Read in the Reed College / Octavo digital extract (English translation file): https://www.reed.edu/math-stats/wieting/mathematics537/DeRevolutionibus.pdf. Dedication (preface 1–5), I.4, I.9, I.10. Read 2026-10-24."
    url: "https://www.reed.edu/math-stats/wieting/mathematics537/DeRevolutionibus.pdf"
    accessed: 2026-10-24
    reliability_note: "Scholarly English translation of the 1543 text (Rosen 1978), used here to corroborate the Latin Wikisource readings of the same chapters. Not a second Latin witness."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview, timing]
  - id: S6
    type: primary
    kind: other
    author: "Nicolaus Copernicus (trans. Edward Rosen)"
    citation: "Copernicus, Nicolaus. Commentariolus (c. 1514). English in Edward Rosen, Three Copernican Treatises (Columbia University Press, 1939; later reprints). Read via erenow.org web copy of the Rosen English: https://erenow.org/common/history-philosophy-science-reader/32.php. Opening on uniform circular motion and the seven postulata. Read 2026-10-24."
    url: "https://erenow.org/common/history-philosophy-science-reader/32.php"
    accessed: 2026-10-24
    reliability_note: "Unofficial web copy of Rosen's English; Latin MS not opened this pass. Never printed in Copernicus's lifetime (S2). Used as supporting B evidence beside De revolutionibus I.4."
    source_quality: "unofficial web copy"
    used_for: [worldview, timing, contribution]
  - id: S7
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia. \"Nicolaus Copernicus.\" English Wikipedia. https://en.wikipedia.org/wiki/Nicolaus_Copernicus. Read 2026-10-24 (P50 dual bio with Britannica/SEP)."
    url: "https://en.wikipedia.org/wiki/Nicolaus_Copernicus"
    accessed: 2026-10-24
    reliability_note: "P50 frozen-roster dual biography check; birth/death and Commentariolus window agree with S1/S2. Not used to score axes."
    source_quality: "reference entry"
    used_for: [identity, basics, review]
---

# Nicolaus Copernicus

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Nicolaus Copernicus (1473–1543), astronomer of Royal Prussia who proposed the heliocentric system [S1, S2, S7]. Draft: primary_system BELOW_THRESHOLD (CHRIST lead; ruling W1); A 1 (0.7, alt 0, support corroborated); B 3 (0.5, alt 4, written_profession; P16 Hilbert); D 2 (0.5, alt 3); mid_basin BELOW_THRESHOLD. Plotted (faded).

## Life and work

Studied at Cracow, Bologna, Padua and Ferrara; canon of Frombork from 1497 to his death [S1, S2].

## Contribution and impact

The Commentariolus (1508–1514) and De revolutionibus (1543) [S1, S2].

## Childhood and education

Youngest child of a Toruń merchant; raised under his uncle Lucas Watzenrode [S2].

## Adult working worldview

'ab optimo & regularissimo omnium opifice'; I.4 'certa lege'; 'Mathemata mathematicis scribuntur' [S3, S5]. Commentariolus: 'rule of absolute motion' [S6].

## Heritage (context only)

German family, Polish crown [S2].

## Timing

1514–1543, from age 41 [S1, S2].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. A geometric cosmos by an orderly maker; celestial inequalities under a constant law [S3, S5, S6].

## Open questions

- Settled W1: primary stays BELOW_THRESHOLD (CHRIST lead).
- B stays 0.5 under P16 Hilbert / P35 unless a later primary states exception / no-exception.
- Letter against Werner unread.

## Research log

- 2026-10-24: Deepen D1 — Rosen English (S5) + Commentariolus (S6) + Wikipedia (S7); I.4 'certa lege' added; A corroborated; B written_profession @0.5. Wrote drafts/deepen_copernicus-nicolaus.md (untracked).
- 2026-10-19: Read Britannica, SEP and the 1543 text (dedication, I.9, I.10) on Latin Wikisource.
