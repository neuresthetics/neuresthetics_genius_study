---
record:
  record_type: person
  schema_version: "1.2"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, third batch: physical science 1600–1950)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (third batch, RUNBOOK §1 order). Basics from Britannica and MacTutor; her own words from Memoir and Correspondence of Caroline Herschel (John Murray, 1876), page images checked for pp. 17–18, 235–236, 275, 347 and 351. Primary CHRIST at 0.5 (consistent_private_letters, below the ceiling because the evidence is brief devotional phrases: a Nunc dimittis citation, thanksgiving and prayer to 'the Almighty', 'as long as God pleases'); A 0 at 0.5; B, C, D, E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Schema 1.1 → 1.2 (decision P8 adds basis recorded_interview and statement kind 'recorded interview'); no content change."}

identity:
  id: herschel-caroline
  display_name: "Caroline Herschel"
  roster:
    canonical_name: "Caroline Herschel"
    rank: 155
    F: 3
    models: [DeepSeek, GPT, Grok]
    band: "core (3–4)"
    status: core
    field: astronomy
    field_bucket: astronomy
  full_name: {value: "Caroline Lucretia Herschel", certainty: 1.0, cites: [{source: S1, locator: "'Also known as'"}, {source: S2, locator: "heading"}], how_known: "Two sources."}
  native_name: {value: "Carolina Lucretia Herschel (German form on her epitaph: 'Carolina Herschel')", certainty: 0.7, cites: [{source: S3, locator: "p. 351 (epitaph)"}], how_known: "Epitaph as printed; the full German form with 'Lucretia' is not in a source read."}
  aliases:
    - {name: "Caroline Lucretia Herschel", kind: "roster alias"}
    - {name: "Caroline-Herschel", kind: "roster alias"}
    - {name: "Carolina Herschel", kind: other}

basics:
  birth:
    date: {value: "1750-03-16", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "p. 351 (epitaph)"}], how_known: "Two sources agree."}
    place: {value: "Hanover", modern_name: "Hannover, Lower Saxony, Germany", polity_then: "Electorate of Brunswick-Lüneburg (Hanover)", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "p. 351 (epitaph)"}], how_known: "Two sources agree."}
  death:
    date: {value: "1848-01-09", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "p. 351 (epitaph)"}], how_known: "Two sources agree."}
    place: {value: "Hanover", modern_name: "Hannover, Lower Saxony, Germany", polity_then: "Kingdom of Hanover", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "p. 347"}], how_known: "Two sources agree."}
  first_lasting_contribution_year: {value: 1786, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "1786 paragraph"}], how_known: "Her first comet (1 August 1786). She had found three nebulae in 1783 (S1), which would also qualify; both fall in the same era bucket.", alternatives: [{value: 1783, cites: [{source: S1, locator: "opening"}], note: "Three nebulae detected by telescope."}]}
  era_bucket: {value: "1750 to 1849", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "From first_lasting_contribution_year (P2); 1783 gives the same bucket."}
  region_of_birth: {value: "Western Europe", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "Germany is Western Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "paragraphs 2–4"}, {source: S2, locator: "Bath to Slough paragraphs"}], how_known: "Comets and the Flamsteed index were done in England (UK, Northern Europe), 1772–1822; the nebula catalogue was finished in Hanover (Western Europe) after 1822. Two regions, so 0.7.", alternatives: [{value: "Western Europe", cites: [{source: S2, locator: "1822 paragraph"}], note: "Hanover, 1822–1848."}]}
  sex_as_recorded: {value: "female", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "As the sources record it."}
  languages_of_work: {value: [English, German], certainty: 0.7, cites: [{source: S3, locator: "pp. 235–236, 275 (letters in English)"}, {source: S2, locator: "Bath paragraph (William taught her English)"}], how_known: "Letters printed in English; German was her first language."}
  occupations: {value: ["astronomer", "singer", "assistant to William Herschel"], certainty: 1.0, cites: [{source: S1, locator: "paragraphs 1–3"}, {source: S2, locator: "Bath paragraphs"}], how_known: "Two sources."}

contribution:
  fields: {value: ["observational astronomy", "comets", "star and nebula catalogues"], certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "summary"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Discovery of eight comets, the first in 1786 (one periodic: 35P/Herschel–Rigollet)", year: "1786–1797", kind: discovery, lasting: "first comets discovered by a woman", certainty: 1.0, cites: [{source: S1, locator: "opening; paragraph 3"}, {source: S2, locator: "1786 and 1797 paragraphs"}], how_known: "Two sources."}
    - {value: "Index to Flamsteed's Observations of the Fixed Stars, with 560 omitted stars and errata", year: "1798", kind: work, lasting: "published by the Royal Society", certainty: 1.0, cites: [{source: S1, locator: "paragraph 3"}, {source: S2, locator: "Flamsteed paragraph"}], how_known: "Two sources."}
    - {value: "Catalogue of about 2,500 nebulae and star clusters (reduction of William Herschel's sweeps)", year: "1822–1828", kind: work, lasting: "Royal Astronomical Society gold medal, 1828", certainty: 1.0, cites: [{source: S1, locator: "paragraph 4"}, {source: S2, locator: "1822 paragraph"}], how_known: "Two sources."}
    - {value: "Three nebulae detected by telescope", year: "1783", kind: discovery, lasting: "early independent discoveries", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  evidence_of_impact:
    - {value: "Comet 35P/Herschel–Rigollet and the minor planet Lucretia (1889)", kind: "named after them", certainty: 0.7, cites: [{source: S1, locator: "paragraph 3"}, {source: S2, locator: "final paragraph"}], how_known: "One source for each name."}
    - {value: "Royal pension from George III (1787) as William's assistant, which Britannica calls the first salary of a professional female astronomer", kind: "honours in lifetime", certainty: 1.0, cites: [{source: S1, locator: "paragraph 3"}, {source: S2, locator: "1787 paragraph"}], how_known: "Two sources."}
  major_works:
    - {value: "Catalogue of Stars, Taken from Mr. Flamsteed's Observations [...] (Index to Flamsteed)", year: 1798, kind: book, certainty: 0.7, cites: [{source: S2, locator: "Flamsteed paragraph"}], how_known: "MacTutor gives the subject; the printed title was not checked (flag)."}
  honours:
    - {value: "Gold Medal of the (Royal) Astronomical Society", year: 1828, certainty: 1.0, cites: [{source: S1, locator: "paragraph 4"}, {source: S2, locator: "1822 paragraph"}], how_known: "Two sources; they differ on what it was for (see flags)."}
    - {value: "Honorary member of the Royal Astronomical Society (with Mary Somerville, the first women)", year: 1835, certainty: 0.7, cites: [{source: S2, locator: "honours paragraph"}], how_known: "MacTutor; her own letter mentions the choice (S3, p. 276)."}
    - {value: "Member of the Royal Irish Academy", year: 1838, certainty: 1.0, cites: [{source: S2, locator: "honours paragraph"}, {source: S3, locator: "p. 351 (epitaph)"}], how_known: "Two sources (the epitaph gives no year)."}
    - {value: "Gold Medal for Science from the King of Prussia", year: 1846, certainty: 0.7, cites: [{source: S2, locator: "honours paragraph (her 96th birthday)"}], how_known: "MacTutor."}
  definition_fit: {value: "clearly meets", rationale: "Independent discoveries (comets, nebulae) and major catalogues; her largest work reduced her brother's observations.", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "1822 paragraph"}], how_known: "Coder's reading of the two sources."}

childhood:
  family_religion: {value: "Christian; she was christened, confirmed and later buried in the garrison church of Hanover (confession not named in the sources read)", certainty: 1.0, cites: [{source: S3, locator: "pp. 17–18, 347"}], how_known: "Her recollections (pp. 17–18) and the editor's account of the funeral (p. 347), checked on the page images."}
  family_religious_practice: {value: "Church attendance and confirmation instruction as a girl", certainty: 1.0, cites: [{source: S3, locator: "pp. 16–17"}], how_known: "Her own recollection: 'my constant attendance at church and school' (p. 17); her mother released her from housework for the 'necessary preparation for her daughter's confirmation' (p. 16)."}
  parents_and_household:
    - {value: "Father, Isaac Herschel, oboist and later bandmaster in the Hanoverian Foot Guards, with interests in music, philosophy and astronomy", name: "Isaac Herschel", role: father, certainty: 0.7, cites: [{source: S2, locator: "paragraph 1"}], how_known: "MacTutor."}
    - {value: "Mother, Anna Ilse Moritzen, who opposed her daughters' education", name: "Anna Ilse Herschel (née Moritzen)", role: mother, certainty: 1.0, cites: [{source: S2, locator: "paragraph 1"}, {source: S1, locator: "paragraph 2"}], how_known: "Two sources (Britannica on the opposition)."}
  household_circumstances: {value: "Six children; brothers trained as musicians; she was kept to household work, especially after her father's death in 1767; typhus at about ten stunted her growth", certainty: 1.0, cites: [{source: S1, locator: "paragraph 2"}, {source: S2, locator: "paragraphs 1–3"}], how_known: "Two sources."}
  schooling:
    - {value: "School in Hanover alongside confirmation instruction (school not named)", stage: other, years: "–1764", certainty: 0.7, cites: [{source: S3, locator: "p. 17"}], how_known: "Her recollection; the school is not named."}
    - {value: "Lessons in dressmaking; studied to qualify as a governess", stage: other, years: "after 1767", certainty: 0.7, cites: [{source: S2, locator: "paragraph 3"}], how_known: "MacTutor."}
    - {value: "Taught singing, English, algebra, geometry and spherical trigonometry by her brother William in Bath", stage: tutor, years: "1772–1782", certainty: 1.0, cites: [{source: S1, locator: "paragraph 2"}, {source: S2, locator: "Bath paragraphs"}], how_known: "Two sources."}
  early_mathematics: {value: TODO, note: "Her mathematics (algebra, geometry, spherical trigonometry) came from William in Bath, from age 22; childhood mathematics not researched."}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure:
    - {value: "Her father showed her constellations on a frosty night after watching a comet", certainty: 0.7, cites: [{source: S2, locator: "paragraph 2 (quoting the Memoir)"}], how_known: "MacTutor quoting her recollection."}
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [German], certainty: 0.7, cites: [{source: S2, locator: "Bath paragraph"}], how_known: "Born in Hanover; William taught her English after 1772."}
  notable_events:
    - {value: "Confirmed on a Sunday during William's visit, then received first communion the following Sunday, the day he left", year: "1764", certainty: 0.7, cites: [{source: S3, locator: "pp. 17–18"}], how_known: "Her recollection; the year comes from the editor's narrative (William arrived 2 April 1764), so 'Sunday the 8th' is 8 April 1764."}
    - {value: "Typhus at about ten", year: "1760", certainty: 0.7, cites: [{source: S1, locator: "paragraph 2"}], how_known: "Britannica (age 10)."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1772–1848", certainty: 1.0, cites: [{source: S1, locator: "paragraphs 2–4"}], how_known: "From Bath to her death."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Searched the 1876 Memoir's full text (God, Providence, church, prayer, Creator, soul, heaven); no statement relating astronomy and religion was found. 'Minding the heavens' is her phrase for observing."}
  primary_system:
    value: CHRIST
    basis: consistent_private_letters
    certainty: 0.5
    cites: [{source: S3, locator: "pp. 235, 236, 275"}]
    how_known: "Three private letters in her own words (two of 3 March 1829, one of 23 April 1835), checked on the page images of the 1876 edition. Below the 0.7 ceiling because each is a brief devotional phrase of the kind common in letters of the time, not a statement of belief, and the edition is a family selection with marked cuts."
    rationale: "CHRIST guidance: use when the person's own writing shows Christian belief (Christ, scripture, creeds, church). She quotes Simeon's canticle from scripture to express her joy ('See St. Luke, cap. ii., v. 29', p. 236), puts letters by 'under thanksgiving to the Almighty, with a prayer for future protection' (p. 275), and signs off 'as long as God pleases I shall remain' (p. 235). Upbringing and burial in the garrison church (pp. 17–18, 347) do not code her by themselves."
    alternatives:
      - {value: CLTHEI, cites: [{source: S3, locator: "p. 275"}], note: "A prayer for future protection is petition; preferred only if her writing showed God acting in particular events beyond nature's course. None found."}
  secondary_system: {value: UNKNOWN, how_known: "No second system in the sources read."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Chosen at 0.5: scripture, thanksgiving and prayer in her letters (S3, pp. 235–236, 275).", cites: [{source: S3, locator: "pp. 235–236, 275"}]}
    - {code: CLTHEI, reason: "Prayer for protection is petition; not chosen because nothing read shows God expected to act against the course of nature.", cites: [{source: S3, locator: "p. 275"}]}
    - {code: DEISM, reason: "Rejected: she prays to God for protection and treats her lifespan as in God's pleasure (S3, pp. 235, 275).", cites: [{source: S3, locator: "pp. 235, 275"}]}
  lio_axes:
    A_locus:
      value: 0
      basis: consistent_private_letters
      certainty: 0.5
      cites: [{source: S3, locator: "pp. 235, 275"}]
      how_known: "Two private letters (1829, 1835). Below the 0.7 ceiling because the phrases are brief and conventional and speak to the axis only indirectly."
      rationale: "Interventionist pole features: a personal God addressed as 'the Almighty' in thanksgiving and in 'a prayer for future protection' (p. 275), whose pleasure sets how long she lives ('as long as God pleases I shall remain', p. 235). Nothing read places God in the world. Alternative: 1, if the phrases are read as formula rather than belief."
    B_cause: {value: BELOW_THRESHOLD, how_known: "Scored on her account of nature (P6). Nothing read gives her account of why the heavens move as they do: her work was sweeping for comets and nebulae, reducing observations and cataloguing (S1; S2), and her providential phrases concern her own life, not nature. Not reconstructed from observational work alone."}
    C_ledger: {value: BELOW_THRESHOLD, how_known: "No statement on reward, punishment or judgement in her own words read.", note: "Her epitaph, said by the editor to be 'of her own composition' (S3, p. 347), speaks of her father gone before 'zu einem besseren Leben' (p. 351); it was completed after her death (it gives her age at death), so the wording cannot be assigned to her with confidence, and it states hope of an afterlife, not a ledger."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "Nothing read on revelation against observation. Quoting Luke to express joy (p. 236) shows use of scripture, not its authority over natural knowledge."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Scored on the world's order (P7). 'A prayer for future protection' (p. 275, a single letter) asks for protection but says nothing about God answering petition with particular events; not enough to score."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is only 0.5 and B_cause is BELOW_THRESHOLD, under the P4 test's 0.7 bar."}
  statements:
    - text: "But as long as God pleases I shall remain"
      cites: [{source: S3, locator: "p. 235"}]
      date: "1829-03-03"
      context: "Closing line before her signature ('Your most affectionate sister, C. Herschel') in a letter to William's widow, Lady Herschel, on John Herschel's marriage, after arrangements for her belongings at her death."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: 'But I can at this present moment find no words which would better express my happiness than those which escaped in exclamation from my lips, according to Simeon. See St. Luke, cap. ii., v. 29: "Lord, now lettest thou thy servant depart in peace!"'
      cites: [{source: S3, locator: "p. 236"}]
      date: "1829-03-03"
      context: "Letter to her nephew J. F. W. Herschel on news of his engagement."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "Each time after having read them over again they are put by, under thanksgiving to the Almighty, with a prayer for future protection."
      cites: [{source: S3, locator: "p. 275"}]
      date: "1835-04-23"
      context: "Letter to her nephew's wife ('My dearest Niece'), about the five letters received from the family at the Cape."
      axes: [A_locus, E_scope]
      kind: "private letter"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
  changes_over_life: []
  coder_notes: "The 1876 Memoir (ed. Mrs John Herschel) prints her recollections and letters with cuts marked by asterisks and dots; the cuts are the editor's, and quotations here keep them as printed. Devotional phrases in letters ('God bless you', 'thank God') recur across the volume (full-text search), which supports a settled conventional piety, but they were not coded as evidence. Her epitaph (p. 351) is treated as uncertain authorship (see C_ledger). The diary pages from the years after William's marriage were destroyed by her (S2), so a gap in the record there is expected."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Hanoverian German; a musicians' family", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "paragraph 1"}], how_known: "Two sources."}
  religious_heritage_by_birth: {value: "Christian (Hanover garrison church congregation)", certainty: 1.0, cites: [{source: S3, locator: "p. 347"}], how_known: "Editor's account, checked on the page image."}
  baptism_or_initiation: {value: "Christened in the garrison church, Hanover", certainty: 1.0, cites: [{source: S3, locator: "p. 347"}], how_known: "Editor's account, checked on the page image."}
  childhood_catechism: {value: "Confirmation instruction, then confirmation and first communion in 1764", certainty: 1.0, cites: [{source: S3, locator: "pp. 16–18"}], how_known: "Her recollection and the editor's narrative."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1786–1828", certainty: 1.0, cites: [{source: S1, locator: "paragraphs 1–4"}, {source: S2, locator: "1786–1828 paragraphs"}], how_known: "From the first comet to the nebula catalogue."}
  age_at_first_lasting_contribution: {value: 36, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Born March 1750; first comet August 1786. 33 if the 1783 nebulae are counted."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No LIO-type statement found in the Memoir's full text."}
  lio_views_relative_to_major_work: {value: "unclear", rationale: "No LIO-type statement found; not scored from absence.", certainty: 0.5, cites: [{source: S3, locator: "full text searched"}], how_known: "Nothing to date."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Observational and computational work (sweeps, reductions, catalogues); no definition-and-consequence argument read.", certainty: 0.5, cites: [{source: S2, locator: "Bath to 1828 paragraphs"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "Bath paragraphs"}], how_known: "Geometry and spherical trigonometry learned from William; interest only in useful parts (S2)."}
  circle_present: {value: "no", rationale: "Her God language (S3) is personal and petitionary, not a God–Nature identity.", certainty: 0.5, cites: [{source: S3, locator: "pp. 235, 275"}], how_known: "Coder's reading of brief phrases."}
  reading: "As belief, not finding: no geometric form and no circle in what was read. The record does not test H1."
  notes: ""

institutions:
  - {value: "King George III (royal pension as William's assistant)", role: "pensioned assistant astronomer", years: "1787–", kind: "patron or funder", certainty: 1.0, cites: [{source: S1, locator: "paragraph 3"}, {source: S2, locator: "1787 paragraph"}], how_known: "Two sources."}
  - {value: "Royal Astronomical Society", role: "gold medallist (1828); honorary member (1835)", years: "1828–1848", kind: "academy or learned society", certainty: 1.0, cites: [{source: S1, locator: "paragraph 4"}, {source: S2, locator: "honours paragraph"}], how_known: "Two sources."}
  - {value: "Royal Irish Academy", role: member, years: "1838–1848", kind: "academy or learned society", certainty: 0.7, cites: [{source: S2, locator: "honours paragraph"}, {source: S3, locator: "p. 351"}], how_known: "Two sources; year from MacTutor only."}
collaborators:
  - {value: "William Herschel", roster_id: herschel-william, relation: collaborator, note: "brother; she kept house, ground mirrors, recorded and reduced his observations (1772–1822)", certainty: 1.0, cites: [{source: S1, locator: "paragraphs 1–3"}, {source: S2, locator: "Bath to 1822 paragraphs"}], how_known: "Two sources."}
  - {value: "John Herschel", relation: family, note: "nephew; she helped educate him and compiled the nebula catalogue for his work", certainty: 1.0, cites: [{source: S2, locator: "1822 paragraph"}, {source: S3, locator: "p. 236"}], how_known: "Two sources."}
  - {value: "Mary Somerville", roster_id: somerville-mary, relation: correspondent, note: "elected with her as the first women honorary members of the RAS (1835); a letter from Somerville to her is printed", certainty: 0.7, cites: [{source: S2, locator: "honours paragraph"}, {source: S3, locator: "p. 274"}], how_known: "Two sources."}
  - {value: "Carl Friedrich Gauss", roster_id: gauss-carl-friedrich, relation: other, note: "visited her in Hanover", certainty: 0.7, cites: [{source: S2, locator: "Hanover paragraph"}], how_known: "MacTutor."}

review:
  roster_status_reason: {value: "Core in v8 (F 3: DeepSeek, GPT, Grok).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 155"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "What the 1828 gold medal was for: Britannica says an 'unpublished revision and reorganization of their work'; MacTutor says the catalogue of 2,500 nebulae."
    - "Britannica article is signed only 'The Editors'."
    - "The 1876 Memoir is a family edition with editorial cuts; letters were read as printed, not against manuscripts."
    - "Printed title of the 1798 Flamsteed index not checked."
  open_questions:
    - "Read Hoskin's biographies (Caroline Herschel's Autobiographies, 2003; Discoverers of the Universe, 2011) for her religious life in Hanover and any statement on astronomy and God."
    - "Check whether the epitaph text she composed survives in her own hand (Herschel papers, Royal Astronomical Society)."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "The Editors of Encyclopaedia Britannica"
    citation: "\"Caroline Herschel.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Caroline-Lucretia-Herschel."
    url: "https://www.britannica.com/biography/Caroline-Lucretia-Herschel"
    accessed: 2026-10-02
    reliability_note: "Unsigned editors' article, four paragraphs; cited by paragraph."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, institutions, collaborators]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "J J O'Connor and E F Robertson"
    citation: "O'Connor, J. J., and E. F. Robertson. \"Caroline Lucretia Herschel.\" MacTutor History of Mathematics, University of St Andrews. https://mathshistory.st-andrews.ac.uk/Biographies/Herschel_Caroline/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Herschel_Caroline/"
    accessed: 2026-10-02
    reliability_note: "Biography drawing on Hoskin and the Memoir; cited by paragraph subject."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S3
    type: primary
    kind: letter
    author: "Caroline Herschel; ed. Mrs. John Herschel"
    year: 1876
    citation: "Herschel, Mrs. John (ed.). Memoir and Correspondence of Caroline Herschel. London: John Murray, 1876. Internet Archive memoircorrespond00hersiala (University of California Libraries)."
    url: "https://archive.org/details/memoircorrespond00hersiala"
    accessed: 2026-10-02
    reliability_note: "Her recollections and letters as printed by the family, with editorial cuts. Page images checked for pp. 17, 18, 235, 236, 275, 276, 347 and 351 (image n = page + 23 from p. 235 on; p. 18 is n37)."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
---

# Caroline Herschel

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Caroline Lucretia Herschel (1750–1848), Hanover-born astronomer in England, discovered eight comets (1786–1797), indexed Flamsteed's observations (1798) and catalogued about 2,500 nebulae for her nephew John; she won the Astronomical Society's gold medal in 1828 [S1; S2]. Her letters show brief Christian devotion: Simeon's canticle, thanksgiving and prayer to "the Almighty", "as long as God pleases" [S3, pp. 235–236, 275]. Primary CHRIST at 0.5; A 0 at 0.5; B to E below threshold; mid_basin below threshold.

## Life and work

Kept from schooling by her mother, she joined William in Bath in 1772, trained as a singer, and moved with him into astronomy, sweeping for comets and reducing his observations; after his death in 1822 she returned to Hanover [S1; S2].

## Contribution and impact

Comets, the Flamsteed index and the nebula catalogue; a royal pension from 1787 [S1; S2].

## Childhood and education

Christened and confirmed in the Hanover garrison church [S3, pp. 17–18, 347]; household drudgery; William taught her English and mathematics in Bath [S2].

## Adult working worldview

Brief devotional phrases in her letters [S3, pp. 235–236, 275]; no statement on astronomy and religion found.

## Heritage (context only)

Hanoverian musicians' family; christened and confirmed in the garrison church [S3]. Context only.

## Timing

First comet 1786, at 36 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No geometric form; no circle.

## Open questions

- Hoskin's editions and biographies; the epitaph manuscript.

## Research log

- 2026-10-02: Read Britannica and MacTutor; searched the full text of the 1876 Memoir (Internet Archive) and checked the cited pages on the page images.
