---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 11
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (overnight agent run for Jason, first pool)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages and transcriptions"
  collected_on: 2026-10-02
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created. Basics, contribution, childhood, worldview (CHRIST at 0.7), all five LIO axes and mid_basin (true) filled from his published works (General Scholium, Opticks Query 31, Rules of Reasoning), letters to Bentley, three private theological manuscripts and four reference sources. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "key_early_reading changed from an empty list to UNKNOWN with a how_known note, as the coding guide asks. No other change."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "mid_basin rechecked under decision P6 (B_cause scored on the account of nature): B_cause and mid_basin unchanged. Note added to mid_basin how_known. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit fixes: B_cause certainty 1.0 -> 0.7 (the 'Reformation' passage is a named plausible alternative, B = 2); mid_basin certainty 1.0 -> 0.7 (result still true); 'UNKNOWN' wording for a B = 2 result corrected to TODO; 'Church of England' replaced by 'Protestant', as the cited sources say, in nominal_affiliations (certainty 1.0 -> 0.7) and family_religion. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit, run 2 (claim #23): E_scope certainty 1.0 -> 0.7. E is scored on natural philosophy only, while other records score it on salvation scope; the domain is open item P7 (PROPOSED). Score unchanged (3). Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "P7 decided by Jason (2026-10-02, option 1): E_scope is scored on the world's order. Rechecked: E_scope stays 3 at 0.7. The interim P7 cap is gone, but certainty stays 0.7 under CODING_GUIDE §3, because the new rule makes a named alternative (2): his private articles petition the Father for 'blessings of this life' (S9, article 8). Rationale and statement tags updated; P7 interim note removed. No new sources. mid_basin unchanged. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "CODING_GUIDE §7 rule on unofficial web copies: S6 (Project Gutenberg Opticks, 4th ed. 1730) is an unofficial copy. Checked it against S14, the University of California library scan of the 1730 edition (Internet Archive), with a second scan (Oxford copy) to resolve OCR noise. The five Query 31 quotations and the Query 28 passage agree word for word. Added S14 cites with the printed 1730 pages to the four certainty-1.0 fields that cite S6 (languages_of_work, major_works Opticks, self-described relation, A_locus) and to the five quotations, whose verified_against goes from primary transcription to primary facsimile. All stay at 1.0. Noted that S6's page markers run about 24 pages above the 1730 pagination. No value, certainty or mid_basin change."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Schema 1.1 → 1.2 (decision P8 adds basis recorded_interview and statement kind 'recorded interview'); no content change."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Stage 3 lens-audit rulings applied to the batch's other records (OPEN_DECISIONS P14–P28, v8's picks, 2026-10-02). Schema 1.2 → 1.3. One reliable source caps a fact at 0.7; derived fields take the lowest certainty of their inputs; quote kinds relabelled (P18/P28). Full before → after list: reports/stage3_rulings_changes.csv. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "P30 rule 5 age sweep: ages recomputed as event year − birth year, with no month adjustment (scripts/recompute_ages.py; every change is in reports/p30_age_changes.csv). No other value changed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Span alignment (P29, P30 and its addendum): timing.major_work_period 1665–1693 → 1665–1704; worldview.working_years 1665–1727 → 1665–1704, equal to the span (P30 addendum f); lasting item added: Opticks (1704); 6 headline values rest on evidence outside the span and are left unchanged for a ruling (open questions). Listed in reports/p30_span_alignment.csv. Not reviewed."}

identity:
  id: newton-isaac
  display_name: "Isaac Newton"
  roster:
    canonical_name: "Isaac Newton"
    rank: 42
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: physics
    field_bucket: physics
  full_name: {value: "Sir Isaac Newton", certainty: 1.0, cites: [{source: S1, locator: "opening sentence; Leader of English science (knighted 1705)"}, {source: S2, locator: "Biography"}], how_known: "Both sources use this name; 'Sir' from his knighthood in 1705."}
  native_name: {value: "Isaac Newton", certainty: 0.7, cites: [{source: S1, locator: "opening sentence"}], how_known: "English was his language, so the native form is the roster name."}
  aliases:
    - {name: "Isaac-Newton", kind: "roster alias"}
    - {name: "Newton-Isaac", kind: "roster alias"}
    - {name: "Sir Isaac Newton", kind: "title or honorific"}

basics:
  birth:
    date:
      value: "1642-12-25"
      calendar: julian
      certainty: 1.0
      cites: [{source: S1, locator: "opening sentence"}, {source: S2, locator: "Quick Info; Biography (calendar note)"}, {source: S3, locator: "§1.1"}]
      how_known: "Three sources agree. England used the Julian calendar until 1752 (S2), so the source date is kept with calendar julian, as the data dictionary asks."
      alternatives:
        - {value: "1643-01-04", cites: [{source: S1, locator: "opening sentence ('New Style')"}, {source: S2, locator: "Quick Info"}], note: "The same day in the Gregorian calendar. MacTutor uses this date."}
    place:
      value: "Woolsthorpe (manor house), near Grantham, Lincolnshire, England"
      modern_name: "Woolsthorpe-by-Colsterworth, Lincolnshire, England, United Kingdom"
      polity_then: "Kingdom of England"
      certainty: 1.0
      cites: [{source: S1, locator: "opening sentence"}, {source: S2, locator: "Biography, first paragraph"}, {source: S3, locator: "§1.1"}]
      how_known: "Three sources agree; S2 says the manor house. The modern parish name is the coder's addition."
  death:
    date:
      value: "1727-03-20"
      calendar: julian
      certainty: 1.0
      cites: [{source: S1, locator: "opening sentence"}, {source: S2, locator: "Quick Info"}]
      how_known: "Britannica gives 20 March (Julian) and 31 March (Gregorian); MacTutor gives 31 March. Same day."
      alternatives:
        - {value: "1727-03-31", cites: [{source: S1, locator: "opening sentence"}, {source: S2, locator: "Quick Info"}], note: "Gregorian date."}
    place:
      value: "London, England"
      modern_name: "London, England, United Kingdom"
      polity_then: "Kingdom of Great Britain"
      certainty: 1.0
      cites: [{source: S1, locator: "opening sentence"}, {source: S2, locator: "Quick Info"}]
      how_known: "Two sources agree. The district is not given in the sources read."
  first_lasting_contribution_year: {value: 1665, certainty: 1.0, cites: [{source: S2, locator: "Biography (plague years 1665–1667)"}, {source: S1, locator: "Career (experiments of 1665 and 1666); International prominence (calculus before Leibniz)"}], how_known: "Year he began the method of fluxions (calculus) and the prism experiments, during the plague years at Woolsthorpe. Both are listed as lasting contributions below."}
  era_bucket: {value: "1600 to 1749", certainty: 1.0, cites: [{source: S2, locator: "Biography"}], how_known: "Derived from first_lasting_contribution_year (1665) under the era buckets (decision P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 1.0, cites: [{source: S1, locator: "opening sentence"}], how_known: "Born in Lincolnshire, England; the United Kingdom is Northern Europe in data/reference/regions.csv (UN M49 sub-region, decision P3)."}
  region_of_work: {value: "Northern Europe", certainty: 1.0, cites: [{source: S1, locator: "Career; Warden of the mint"}, {source: S2, locator: "Biography"}], how_known: "All his posts were in Cambridge and London."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "throughout ('he', 'his', 'only son')"}], how_known: "As the sources record it."}
  languages_of_work: {value: [Latin, English], certainty: 1.0, cites: [{source: S1, locator: "opening sentence (Philosophiae Naturalis Principia Mathematica, 1687); Final years (Latin and English editions of the Opticks)"}, {source: S6, locator: "title page"}, {source: S14, locator: "title page"}], how_known: "The Principia was in Latin; the Opticks and his theological manuscripts were in English."}
  occupations:
    value: ["Lucasian professor of mathematics", "natural philosopher", "mathematician", "Warden and Master of the Royal Mint", "President of the Royal Society", "Member of Parliament (Convention Parliament)", "theologian and biblical scholar (mostly unpublished)"]
    certainty: 1.0
    cites: [{source: S1, locator: "Career; Warden of the mint; Interest in religion and theology; Leader of English science"}, {source: S2, locator: "Biography"}, {source: S3, locator: "opening section"}]
    how_known: "Posts from S1 and S2. S3 says he put no less effort into theology and biblical studies than into mathematics and physics."

contribution:
  fields: {value: [mathematics, physics, optics, astronomy, "chemistry and alchemy", "theology and chronology"], certainty: 1.0, cites: [{source: S1, locator: "opening paragraph; Influence of the Hermetic tradition"}, {source: S3, locator: "opening section"}], how_known: "Two reference sources agree."}
  lasting_original_contributions:
    - {value: "The method of fluxions (the infinitesimal calculus), developed before Leibniz's independent work", year: 1665, kind: method, lasting: "the calculus", certainty: 1.0, cites: [{source: S1, locator: "opening paragraph ('original discoverer of the infinitesimal calculus'); International prominence"}, {source: S2, locator: "Biography (plague years)"}], how_known: "Two sources agree on the discovery and the plague-years date. Published only in 1704 (S1)."}
    - {value: "Composition of white light: sunlight is a mixture of rays with different refrangibility and colour (prism experiments)", year: "1665–1666; published 1672", kind: discovery, lasting: "foundation of physical optics", certainty: 1.0, cites: [{source: S1, locator: "opening paragraph; Career (experiments of 1665 and 1666)"}, {source: S2, locator: "Biography (1672 paper in the Philosophical Transactions)"}], how_known: "Two sources agree."}
    - {value: "The reflecting telescope", year: "by 1671", kind: invention, lasting: "reflecting telescopes", certainty: 1.0, cites: [{source: S1, locator: "Career ('he constructed the first ever built'; the Royal Society heard of it in 1671)"}, {source: S2, locator: "Biography (elected FRS in 1672 after donating one)"}], how_known: "Two sources agree. The build year itself is not given in the sources read."}
    - {value: "The three laws of motion and the law of universal gravitation (Principia)", year: 1687, kind: "law or principle", lasting: "the basic principles of classical mechanics", certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}, {source: S2, locator: "Biography"}], how_known: "Two sources agree."}
    - {value: "Opticks: the experiments on light and colours in book form, with the first printed account of his calculus in two appended papers", year: 1704, kind: "work", lasting: "the experimental theory of light and colours; the calculus in print", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts (Notable Works: 'Opticks'); International prominence ('he did not really publish it until he appended two papers to the Opticks in 1704'); Final years ('the first edition of the Opticks in 1704')"}], how_known: "One encyclopedia article, read on three of its pages, so 0.7. S1 adds that the book 'merely published work done 30 years before'. Added 2026-10-02 under the P30 addendum (the latest lasting work must be listed)."}
  evidence_of_impact:
    - {value: "Britannica calls his three laws of motion 'the basic principles of modern physics' and the Principia one of the most important single works in the history of modern science", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening paragraph"}], how_known: "Signed reference article."}
    - {value: "Young British scientists took him as their model, and within a generation the salaried science chairs in England were held by Newtonians", kind: "institutional or technological lineage", certainty: 0.7, cites: [{source: S1, locator: "International prominence"}], how_known: "One source."}
    - {value: "Newton's laws of motion and the Newton–Raphson method carry his name", kind: "named after them", certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}, {source: S2, locator: "Other pages about Isaac Newton (Newton-Raphson method)"}], how_known: "Named in both sources."}
  major_works:
    - {value: "Philosophiae Naturalis Principia Mathematica (2nd ed. 1713 with the General Scholium; 3rd ed. 1726)", year: 1687, kind: book, certainty: 1.0, cites: [{source: S1, locator: "opening paragraph; Final years"}, {source: S4, locator: "General Scholium 'added to the second edition of the text in 1713'"}], how_known: "Two sources."}
    - {value: "Opticks (Latin edition 1706; English editions 1717–18 and later, with the expanded Queries)", year: 1704, kind: book, certainty: 1.0, cites: [{source: S1, locator: "Final years"}, {source: S6, locator: "title page (4th edition, 1730)"}, {source: S14, locator: "title page (fourth edition, corrected, 1730)"}], how_known: "Encyclopedia and the text itself."}
    - {value: "Theological and chronological works on the prophecies of Daniel and St John and on ancient chronology, published after his death", year: "later years; posthumous", kind: other, certainty: 0.7, cites: [{source: S1, locator: "Interest in religion and theology"}], how_known: "Encyclopedia."}
  honours:
    - {value: "Fellow of the Royal Society", year: 1672, certainty: 1.0, cites: [{source: S2, locator: "Biography"}, {source: S1, locator: "Career (election after the telescope)"}], how_known: "Two sources."}
    - {value: "One of eight foreign associates of the French Académie des Sciences", year: 1699, certainty: 0.7, cites: [{source: S1, locator: "Leader of English science ('Four years earlier' than 1703)"}], how_known: "One source; year computed from its wording."}
    - {value: "President of the Royal Society, re-elected each year until his death", year: 1703, certainty: 1.0, cites: [{source: S1, locator: "Leader of English science"}, {source: S2, locator: "Biography"}], how_known: "Two sources."}
    - {value: "Knighted by Queen Anne, the first scientist so honoured for his work", year: 1705, certainty: 1.0, cites: [{source: S1, locator: "Leader of English science"}, {source: S2, locator: "Biography"}], how_known: "Two sources."}
  definition_fit: {value: "clearly meets", rationale: "Calculus, the laws of motion, universal gravitation and the analysis of white light are still standard; named laws; reference works call the Principia one of the most important works in the history of science.", certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}, {source: S2, locator: "Biography"}], how_known: "Lane A definition (lasting original impact on documented criteria) applied to the contributions listed above."}

childhood:
  family_religion: {value: "Protestant. SEP says he was born into a Puritan family; his stepfather Barnabas Smith was the minister of the church at North Witham.", certainty: 0.7, cites: [{source: S3, locator: "§1.1 ('born into a Puritan family')"}, {source: S2, locator: "Biography (Smith 'the minister of the church at North Witham')"}, {source: S1, locator: "Formative influences ('the well-to-do minister Barnabas Smith')"}], how_known: "Only one source (SEP) names the family's religious leaning; the stepfather's office is in two."}
  family_religious_practice: {value: TODO, note: "No account of the household's worship was found in the sources read. Westfall's Never at Rest or the Newton Project biography may have it."}
  parents_and_household:
    - {value: "Father, Isaac Newton, a yeoman farmer who owned property and animals but could not sign his name; he died in October 1642, before his son was born", name: "Isaac Newton (senior)", role: father, certainty: 1.0, cites: [{source: S2, locator: "Biography"}, {source: S1, locator: "Formative influences"}], how_known: "Two sources agree that he died before the birth (they differ on two or three months; see data_quality_flags)."}
    - {value: "Mother, Hannah Ayscough. She remarried Barnabas Smith and moved to his village, leaving Isaac with her parents; she returned to Woolsthorpe after Smith died in 1653", name: "Hannah Ayscough (later Smith)", role: mother, certainty: 1.0, cites: [{source: S1, locator: "Formative influences"}, {source: S2, locator: "Biography"}, {source: S3, locator: "§1.1"}], how_known: "Three sources agree on the facts; they differ on when she remarried (see data_quality_flags)."}
    - {value: "Raised from about age two or three by his maternal grandmother Margery Ayscough at Woolsthorpe", name: "Margery Ayscough", role: grandmother, certainty: 1.0, cites: [{source: S2, locator: "Biography"}, {source: S1, locator: "Formative influences"}], how_known: "Two sources."}
    - {value: "Stepfather Barnabas Smith (d. 1653); three half-siblings from that marriage (one half-brother, two half-sisters)", name: "Barnabas Smith", role: stepfather, certainty: 1.0, cites: [{source: S2, locator: "Biography"}, {source: S1, locator: "Formative influences ('a son and two daughters')"}], how_known: "Two sources."}
  household_circumstances: {value: "Landed yeoman family; his mother became 'a lady of reasonable wealth and property' after her second marriage. He was the only son of the first marriage.", certainty: 1.0, cites: [{source: S2, locator: "Biography"}, {source: S1, locator: "Formative influences ('her now considerable property')"}], how_known: "Two sources agree."}
  schooling:
    - {value: "Learned to read and write from his grandmother and mother", stage: home, certainty: 0.7, cites: [{source: S3, locator: "§1.1"}], how_known: "One source."}
    - {value: "Free Grammar School, Grantham, lodging with the Clark family; taken out about 1659 to run the farm, then sent back in 1660 to prepare for the university, lodging with the headmaster, Stokes", stage: "grammar or secondary school", institution: "Free Grammar School, Grantham", years: "c. 1655–1661 (interrupted c. 1659–1660)", ages: "c. 13–19", certainty: 1.0, cites: [{source: S2, locator: "Biography"}, {source: S3, locator: "§1.1 (boarding school from 1655; farm 1659)"}, {source: S1, locator: "Formative influences"}], how_known: "Three sources agree on the school and the interruption. Start year from S3; S2 says 'shortly after' 1653."}
    - {value: "Trinity College, Cambridge: entered as a sizar on 5 June 1661; scholar 1664; BA April 1665", stage: university, institution: "Trinity College, Cambridge", years: "1661–1665", ages: "19–23", certainty: 1.0, cites: [{source: S2, locator: "Biography"}, {source: S1, locator: "Formative influences (matriculated June 1661)"}], how_known: "Two sources agree."}
  early_mathematics: {value: "arithmetic only", ages: "to 18", description: "At Grantham he 'probably received no more than a smattering of arithmetic' (S1). MacTutor: 'There is no evidence that he learnt any mathematics' before university, and he did not read Euclid before 1663 (S2).", certainty: 0.7, cites: [{source: S1, locator: "Formative influences"}, {source: S2, locator: "Biography"}], how_known: "Two sources agree that there is little or no evidence of school mathematics; both hedge ('probably'), so 0.7."}
  early_geometric_style_reasoning: {value: "None documented before 18. He first read Euclid's Elements (Barrow's edition) in autumn 1663, at 20, after failing to follow the mathematics in an astrology book; he then read the whole book.", certainty: 0.7, cites: [{source: S2, locator: "Biography (de Moivre's account)"}], how_known: "MacTutor reports de Moivre's account. One line of evidence."}
  early_science_exposure:
    - {value: "Built model machines such as clocks and windmills at Grantham", age: "c. 12–18", certainty: 0.5, cites: [{source: S1, locator: "Formative influences ('anecdotes')"}, {source: S2, locator: "Biography"}], how_known: "Both sources call these anecdotes; S2 warns they may have been made up later."}
  key_early_reading: [{value: UNKNOWN, how_known: "None documented in S1–S3. MacTutor (S2) says 'We know nothing about what Isaac learnt in preparation for university'. See open_questions."}]
  childhood_mentors:
    - {value: "His uncle William Ayscough (Cambridge MA), who persuaded his mother to send him back to school and to the university", name: "William Ayscough", role: uncle, certainty: 1.0, cites: [{source: S2, locator: "Biography"}, {source: S3, locator: "§1.1 ('Hannah's brother')"}], how_known: "Two sources."}
    - {value: "Stokes, headmaster at Grantham, with whom he lodged in 1660–61", name: "Stokes (headmaster)", years: "1660–1661", certainty: 1.0, cites: [{source: S2, locator: "Biography"}, {source: S3, locator: "§1.1"}], how_known: "Two sources."}
  languages_in_childhood: {value: [English, Latin], certainty: 0.7, cites: [{source: S1, locator: "Formative influences ('a firm command of Latin')"}], how_known: "English as his first language; Latin learned at Grantham. One source for the Latin."}
  notable_events:
    - {value: "Father died before his birth", year: 1642, age: 0, certainty: 1.0, cites: [{source: S1, locator: "Formative influences"}, {source: S2, locator: "Biography"}], how_known: "Two sources."}
    - {value: "Mother remarried and left him with his grandmother", year: "1645 or 1646", age: "3–4", certainty: 1.0, cites: [{source: S2, locator: "Biography"}, {source: S1, locator: "Formative influences"}, {source: S3, locator: "§1.1"}], how_known: "Three sources agree on the event; the year differs by source."}
    - {value: "Death of his stepfather; mother returned to Woolsthorpe with three young children", year: 1653, age: 11, certainty: 1.0, cites: [{source: S1, locator: "Formative influences"}, {source: S2, locator: "Biography"}, {source: S3, locator: "§1.1"}], how_known: "Three sources."}
    - {value: "Wrote a list of his sins in shorthand at 19, including threatening to burn his mother and stepfather 'and the house over them', and setting his heart on learning more than on God", year: 1662, age: 20, certainty: 1.0, cites: [{source: S1, locator: "Formative influences"}, {source: S2, locator: "Biography"}], how_known: "Both sources quote the list."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1665–1704", certainty: 1.0, cites: [{source: S2, locator: "Biography (plague years)"}, {source: S1, locator: "International prominence; Final years ('the first edition of the Opticks in 1704')"}], how_known: "Equal to timing.major_work_period (P30 addendum f; span check 2026-10-02). Was 1665–1727: From the plague years to his death. His creative science was mostly done by 1693 (S1); theology continued to the end."}
  nominal_affiliations:
    - {value: "Protestant ('a fervent if unorthodox Protestant'). He was a Fellow of Trinity College, helped lead Cambridge's resistance to James II's attempt to Catholicize it, and sat for the university in the Convention Parliament (1689)", years: "1661–1727", certainty: 0.7, cites: [{source: S1, locator: "Warden of the mint ('a fervent if unorthodox Protestant')"}, {source: S2, locator: "Biography (Convention Parliament, 15 January 1689)"}], how_known: "Britannica gives the label 'Protestant'; MacTutor confirms the Convention Parliament. Neither names the Church of England, so the label is 'Protestant' (lens audit, 2026-10-02). One source for the label, so 0.7. His London parish priest was Samuel Clarke (next entry, S4)."}
    - {value: "In London, Samuel Clarke was his parish priest", certainty: 0.7, cites: [{source: S4, locator: "§7 (Leibniz–Clarke correspondence)"}], how_known: "One source."}
  self_described_science_religion_relation:
    value: "Natural philosophy reasons from phenomena up to a first cause that is not mechanical, and talking about God from the appearances of things belongs to natural philosophy. He wrote the Principia partly to support belief in a Deity. Natural philosophy, if perfected, would also widen moral philosophy by showing our duty to the first cause."
    certainty: 1.0
    cites: [{source: S5, locator: "p. 392"}, {source: S6, locator: "pp. 369, 405"}, {source: S14, locator: "pp. 344, 381"}, {source: S7, locator: "letter of 10 Dec. 1692, f. 4r"}]
    how_known: "His own words in the General Scholium and Opticks (public) and a letter to Bentley (private) that agree. Paraphrase; quotations are in statements."
  primary_system:
    value: CHRIST
    basis: consistent_private_letters
    certainty: 0.7
    cites: [{source: S9, locator: "f. 1r"}, {source: S10, locator: "MS pp. 35–36"}, {source: S11, locator: "ff. 1r–2r"}, {source: S1, locator: "Interest in religion and theology"}, {source: S3, locator: "opening section"}]
    how_known: "His public writings (S5, S6) are theistic but not specifically Christian. His Christian belief, including Christ as the one mediator, the resurrection and the judgement, is in three private manuscripts that agree (S9–S11), and reference sources describe decades of biblical study. So 0.7, not 1.0."
    rationale: "CHRIST fits 'the religion as practised and confessed', in a heterodox form: a biblical, anti-Trinitarian Protestant (S1: 'a fervent if unorthodox Protestant'; S12: an Arian from about 1672) whose private creed names 'one God the Father' and 'one Mediator between God & Man' (S9) and who spent years on the prophecies of Daniel and John (S1). Under the coding rule the question is whether a theism split fits better. CLTHEI is the close second (see candidate_codes_considered). CHRIST is chosen because his religion is a specific scriptural Christianity, not a general picture of God, and the CLTHEI features he shows (petition, God reforming the solar system) sit inside that Christianity."
  secondary_system: {value: UNKNOWN, how_known: "No second system; he published in no other system."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Chosen. Scripture-centred, anti-Trinitarian Protestant; Christ as mediator and judge in his private creeds (S9, S10); decades of biblical study (S1, S3).", cites: [{source: S9, locator: "f. 1r"}, {source: S10, locator: "MS p. 36"}, {source: S1, locator: "Interest in religion and theology"}]}
    - {code: CLTHEI, reason: "Close second; a reviewer could choose it. For: his God is a governing Lord who can 'form and reform the Parts of the Universe' and whose system 'wants a Reformation' (S6), and his private articles direct petition to the Father (S9). Against: these features are part of his scriptural Christianity, nothing read shows popular miracle piety, and in his physics he says gravity works 'without a miracle' (S4).", cites: [{source: S6, locator: "pp. 402–403"}, {source: S9, locator: "f. 1r, articles 7–8"}, {source: S4, locator: "§7, quoting Newton's draft reply to Leibniz"}]}
    - {code: DEISM, reason: "Rejected. He says 'a God without dominion, providence, and final causes, is nothing else but Fate and Nature' (S5) and that the system may need reforming by God (S6). A creator who is not involved does not fit. Under P4 a deist would also pass, so this choice does not change mid_basin.", cites: [{source: S5, locator: "p. 391"}, {source: S6, locator: "p. 402"}]}
    - {code: CLASS_THEISM, reason: "Rejected. His God is defined by dominion and will ('Deity is the dominion of God') and is present in space substantially, not the simple, immutable God known through Aristotelian metaphysics. SEP describes him holding that even the divine being has spatial location, which his Cartesian and Leibnizian contemporaries rejected.", cites: [{source: S5, locator: "pp. 389–390"}, {source: S4, locator: "§3 (space and the divine)"}]}
    - {code: PANT, reason: "Rejected. He denies that God is 'the soul of the world' and says 'we are not to consider the World as the Body of God'.", cites: [{source: S5, locator: "p. 389"}, {source: S6, locator: "p. 403"}]}
  lio_axes:
    A_locus:
      value: 1
      basis: written_profession
      certainty: 1.0
      cites: [{source: S5, locator: "pp. 389–390"}, {source: S6, locator: "p. 403"}, {source: S14, locator: "p. 379"}, {source: S4, locator: "§3"}]
      how_known: "Published texts (General Scholium 1713, Opticks Query 31); written profession, so 1.0."
      rationale: "Leans to the transcendent-person pole. God governs 'not as the soul of the world, but as Lord over all', and the world is not 'the Body of God' (S5, S6): a person who rules his creatures. But some immanence features are present: God is omnipresent 'not virtually only, but also substantially', and moves bodies 'within his boundless uniform Sensorium' (S5, S6). SEP notes he held that even the divine being has spatial location (S4). So 1, not 0."
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.7
      cites: [{source: S8, locator: "pp. 384–385"}, {source: S6, locator: "pp. 402–404"}, {source: S5, locator: "pp. 388, 392"}]
      how_known: "Published texts (Principia Rules, General Scholium, Opticks Query 31), so written profession; certainty capped at 0.7 because the record names a plausible alternative score (CODING_GUIDE §3): the Opticks 'Reformation' passage has God repairing the system from time to time inside his physics, which could score 2. Lowered from 1.0 after the lens audit (2026-10-02)."
      rationale: "Scored for his natural philosophy. Law and induction rule: the same effects get the same causes, and qualities found in all bodies within reach of experiment are taken as universal (S8); gravity acts according to the laws he has explained (S5). He states limited exceptions. (1) The origin: the system 'could only proceed from the counsel and dominion of an intelligent and powerful being', and it is 'unphilosophical' to derive the world from chaos 'by the mere Laws of Nature' (S5, S6; also the letters to Bentley, S7). (2) Upkeep: small irregularities 'will be apt to increase, till this System wants a Reformation', and God can 'form and reform the Parts of the Universe' (S6). Once formed, the world 'may continue by those Laws for many Ages' (S6). These are stated and limited, so 3. A reviewer who reads the reformation as ongoing intervention inside his physics could score 2, which would leave mid_basin TODO under P4 (the test has no branch for A = 1 with B = 2). Outside his science his private articles direct petition to God (S9); that is not scored here."
    C_ledger:
      value: 0
      basis: consistent_private_letters
      certainty: 0.7
      cites: [{source: S10, locator: "MS p. 36"}, {source: S11, locator: "f. 2r"}, {source: S9, locator: "f. 1r, article 12"}]
      how_known: "Three private theological manuscripts that agree; so 0.7."
      rationale: "At the personal reward-and-punishment pole: God 'will at length raise all men from the dead to be judged by him & rewarded according to their deeds' (S10); the gentiles are to be judged 'in the last day' by the law written in their hearts (S11); Christ 'hath redeemed us with his blood' (S9). Private manuscripts, so 0.7."
    D_authority:
      value: 2
      basis: consistent_private_letters
      certainty: 0.7
      cites: [{source: S5, locator: "p. 392"}, {source: S6, locator: "pp. 404–405"}, {source: S9, locator: "f. 1r"}, {source: S10, locator: "MS pp. 2–3"}, {source: S1, locator: "Interest in religion and theology"}]
      how_known: "The observation side is in published texts; the scripture side is in private manuscripts and the reference sources' account of his biblical work. The weaker basis sets the certainty: 0.7."
      rationale: "Holds both, in different domains. In natural philosophy observation and induction outrank hypothesis ('I frame no hypothesis'), and he says natural philosophy can show our duty to God 'by the Light of Nature' (S5, S6). In religion scripture is the authority: his creeds are built from biblical texts, and he treated the Trinity as a later corruption of scripture, found by textual study (S9, S10; S1; S12). Neither ranks over the other in the texts read."
    E_scope:
      value: 3
      basis: written_profession
      certainty: 0.7
      cites: [{source: S8, locator: "p. 384"}, {source: S5, locator: "p. 389"}, {source: S6, locator: "pp. 403–404"}, {source: S9, locator: "f. 1r, article 8"}]
      how_known: "Published texts (Principia Rules, General Scholium, Opticks Query 31), so written profession (ceiling 1.0). Certainty 0.7 because the record names a plausible alternative score, 2, from a private manuscript (CODING_GUIDE §3; see the rationale). Rechecked under decision P7 (2026-10-02). The score was already on the world's order and is unchanged; the interim P7 cap no longer applies."
      rationale: "Scored on the world's order (decision P7). Near the LIO pole. The same rules hold for every kind of thing: 'to the same natural effects we must, as far as possible, assign the same causes', for 'respiration in a man and in a beast', for stones 'in Europe and in America' and for 'our culinary fire and of the sun' (S8, Rule II). Qualities found in all bodies within reach of experiment are 'the universal qualities of all bodies whatsoever' (S8, Rule III). The light of the fixed stars is 'of the same nature with the light of the Sun' (S5). One stated, limited exception: God could 'vary the Laws of Nature, and make Worlds of several sorts in several Parts of the Universe' (S6), offered as a possibility, not a finding. So 3. Named alternative 2: his private 'Twelve articles' thank the Father for 'other blessings of this life' and say that whatever we 'desire that he would do for us we ask of him' (S9, article 8). That is petition for this-world favour, which P7 counts against E if it is answered. The text does not say that petition changes events in nature, and it is private, so 3 is kept. His judgement and reward of all the dead (S10, S11) are scored on C, not here."
  mid_basin:
    value: true
    certainty: 0.7
    cites: [{source: S5, locator: "pp. 388–389"}, {source: S6, locator: "pp. 402–403"}, {source: S8, locator: "pp. 384–385"}]
    how_known: "Applied the P4 test to the axis scores above: A_locus = 1 at 1.0 and B_cause = 3 at 0.7, so true. Certainty 0.7: mid_basin is no surer than the less certain of A and B (CODING_GUIDE §3; lens audit, 2026-10-02). Rechecked under decision P6 (2026-10-02): B is scored on his account of nature, which is his natural philosophy, so the result is unchanged. The 'Reformation' passage stays a stated, limited exception inside that account (see the B_cause rationale)."
    rationale: "P4 test (METHOD §1.1): A_locus = 1 (≤ 1) at certainty 1.0, and B_cause = 3 (≥ 3) scored for his natural philosophy at certainty 0.7. Both at ≥ 0.7, so true. F = 5, so 'first-rank' is also met (applied separately). The B score is the weak point: if a reviewer scores B = 2 for the 'Reformation' passage, the test has no branch, so mid_basin would be TODO, not false."
  statements:
    - text: "This most beautiful System of the Sun, Planets and Comets, could only proceed from the counsel and dominion of an intelligent and powerful being."
      cites: [{source: S5, locator: "p. 388"}]
      date: "1713"
      context: "General Scholium, added to the second edition of the Principia (1713); Motte's English translation (1729)."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
      note: "Newton Project transcription of Motte 1729, vol. 2. Motte's English for Newton's Latin."
    - text: "This Being governs all things, not as the soul of the world, but as Lord over all"
      cites: [{source: S5, locator: "p. 389"}]
      date: "1713"
      context: "General Scholium, opening the discussion of God's dominion."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "not virtually only, but also substantially; for virtue cannot subsist without substance."
      cites: [{source: S5, locator: "p. 390"}]
      date: "1713"
      context: "General Scholium, on what God's omnipresence means. The words before it (he is omnipresent) are split across a line in the transcription and are not quoted."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "God suffers nothing from the motion of bodies; bodies find no resistance from the omnipresence of God."
      cites: [{source: S5, locator: "p. 390"}]
      date: "1713"
      context: "General Scholium, same passage."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "a God without dominion, providence, and final causes, is nothing else but Fate and Nature."
      cites: [{source: S5, locator: "p. 391"}]
      date: "1713"
      context: "General Scholium."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "I have not been able to discover the cause of those properties of gravity from phænomena, and I frame no hypothesis."
      cites: [{source: S5, locator: "p. 392"}]
      date: "1713"
      context: "General Scholium, on the cause of gravity ('hypotheses non fingo')."
      axes: [D_authority, B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "the light of the fixed Stars is of the same nature with the light of the Sun, and from every system light passes into all the other systems."
      cites: [{source: S5, locator: "p. 389"}]
      date: "1713"
      context: "General Scholium, arguing that all star systems are under the dominion of One."
      axes: [E_scope]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "Therefore to the same natural effects we must, as far as possible, assign the same causes. As to respiration in a man and in a beast; the descent of stones in Europe and in America; the light of our culinary fire and of the sun"
      cites: [{source: S8, locator: "p. 384, Rule II"}]
      date: "1687"
      context: "Rules of Reasoning in Philosophy, Principia Book III, in Motte's translation. The year is the first edition's; the wording of the rules changed between editions (S4 §4), and the edition history of this rule was not checked."
      axes: [E_scope, B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
      note: "Checked against the OCR of the 1846 American edition of Motte's translation. Spaces before punctuation in the OCR were ignored."
    - text: "The qualities of bodies, which admit neither intension nor remission [...] are to be esteemed the universal qualities of all bodies whatsoever."
      cites: [{source: S8, locator: "p. 384, Rule III"}]
      context: "Rule III, which SEP calls a rare public statement of what Newton took as the 'foundation' of natural philosophy (S4 §4). The omitted words include an OCR error."
      axes: [B_cause, E_scope]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
      note: "Rule III is usually dated to the second edition (1713); that date was not confirmed in the sources read, so no date is given."
    - text: "it's unphilosophical to seek for any other Origin of the World, or to pretend that it might arise out of a Chaos by the mere Laws of Nature; though being once form'd, it may continue by those Laws for many Ages."
      cites: [{source: S6, locator: "p. 402, Query 31"}, {source: S14, locator: "p. 378"}]
      date: "1717"
      context: "Opticks, Query 31 (Queries expanded in the 1706 Latin and 1717–18 English editions; text of the 4th edition, 1730)."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
      note: "Project Gutenberg transcription of the 1730 edition. The date is the English edition's; the sentence may first appear in the 1706 Latin Queries."
    - text: "some inconsiderable Irregularities excepted, which may have risen from the mutual Actions of Comets and Planets upon one another, and which will be apt to increase, till this System wants a Reformation."
      cites: [{source: S6, locator: "p. 402, Query 31"}, {source: S14, locator: "p. 378"}]
      date: "1717"
      context: "Same passage: the planets' common direction of motion is the effect of choice."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
    - text: "a powerful ever-living Agent, who being in all Places, is more able by his Will to move the Bodies within his boundless uniform Sensorium, and thereby to form and reform the Parts of the Universe, than we are by our Will to move the Parts of our own Bodies. And yet we are not to consider the World as the Body of God, or the several Parts thereof, as the Parts of God."
      cites: [{source: S6, locator: "p. 403, Query 31"}, {source: S14, locator: "p. 379"}]
      date: "1717"
      context: "Same Query, on the design of animal bodies and the instinct of insects."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
    - text: "God is able to create Particles of Matter of several Sizes and Figures, and in several Proportions to Space, and perhaps of different Densities and Forces, and thereby to vary the Laws of Nature, and make Worlds of several sorts in several Parts of the Universe. At least, I see nothing of Contradiction in all this."
      cites: [{source: S6, locator: "pp. 403–404, Query 31"}, {source: S14, locator: "pp. 379–380"}]
      date: "1717"
      context: "Same Query; introduced by 'it may be also allow'd that'."
      axes: [B_cause, E_scope]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
    - text: "For so far as we can know by natural Philosophy what is the first Cause, what Power he has over us, and what Benefits we receive from him, so far our Duty towards him, as well as that towards one another, will appear to us by the Light of Nature."
      cites: [{source: S6, locator: "p. 405, end of Query 31"}, {source: S14, locator: "p. 381"}]
      date: "1717"
      context: "Closing paragraph of the Opticks."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
    - text: "When I wrote my treatise about our Systeme I had an eye upon such Principles as might work with considering men for the beleife of a Deity & nothing can rejoyce me more then to find it usefull for that purpose"
      cites: [{source: S7, locator: "letter of 10 Dec. 1692, f. 4r"}]
      date: "1692-12-10"
      context: "Letter to Richard Bentley, who was preparing his Boyle lectures against atheism for print."
      axes: [D_authority, A_locus]
      kind: "private letter"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
      note: "Newton Project normalized transcription of the original letter (Trinity College Library 189.R.4.47)."
    - text: "I do not think explicable by mere natural causes but am forced to ascribe it to the counsel & contrivance of a voluntary Agent."
      cites: [{source: S7, locator: "letter of 10 Dec. 1692, f. 4r"}]
      date: "1692-12-10"
      context: "Same letter, on why one body in the solar system (the Sun) gives light and heat and the planets do not."
      axes: [B_cause]
      kind: "private letter"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "the growth of new systems out of old ones without the mediation of a divine power seems to me apparently absurd."
      cites: [{source: S7, locator: "letter of 25 Feb. 1692/3, f. 7r"}]
      date: "1693-02-25"
      context: "Letter to Bentley. In the same letter he says gravity must be caused by an agent acting constantly according to certain laws, and leaves open whether that agent is material or immaterial (paraphrased, because the transcription has editorial braces inside those words)."
      axes: [B_cause]
      kind: "private letter"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
      note: "Dated 25 February 1692/3 in the Newton Project catalogue; given here with the year starting 1 January."
    - text: "But certainly God could create planets that should move round of themselves without any other cause than gravity that should prevent their removing through the tangent. For gravity without a miracle may keep the planets in."
      cites: [{source: S4, locator: "§7, quoting Newton 2004: 117"}]
      context: "Draft rebuttal of Leibniz's charge that the Principia makes gravity a 'perpetual miracle'; published only after Newton's death. Undated in the source read."
      axes: [B_cause]
      kind: "unpublished manuscript"
      verified_against: "secondary quotation"
      verified_on: 2026-10-02
      note: "Quoted in SEP from Janiak's edition of Newton's Philosophical Writings (2004). The draft itself was not read."
    - text: "There is one God the Father everliving, omnipresent, omniscient, almighty, the maker of heaven & earth, & one Mediator between God & Man the Man Christ Iesus."
      cites: [{source: S9, locator: "f. 1r, article 1"}]
      context: "'Twelve articles on religion', a one-page private manuscript (Keynes MS 8). The Newton Project dates it post-1710."
      axes: [A_locus]
      kind: "unpublished manuscript"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
      note: "Normalized transcription, checked against the original by the Newton Project editors."
    - text: "We are to return thanks to the father alone for creating us & giving us food & raiment & other blessings of this life & whatsover we are to thank him for or desire that he would do for us we ask of him immediately in the name of Christ"
      cites: [{source: S9, locator: "f. 1r, article 8"}]
      context: "Same manuscript. Article 7 says prayers are 'most prevalent when directed to the father in the name of the son'."
      axes: [B_cause, C_ledger, E_scope]
      kind: "unpublished manuscript"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
      note: "Petitionary prayer, outside his science; bears on the CHRIST/CLTHEI choice, not on B for his work. Under P7 it bears on E: it is the basis of the named alternative E = 2."
    - text: "will at length raise all men from the dead to be judged by him & rewarded according to their deeds"
      cites: [{source: S10, locator: "MS p. 36"}]
      context: "'Irenicum, or Ecclesiastical Polyty tending to Peace' (Keynes MS 3), on the duty, after Christ's resurrection, to believe in God's government of the world; 'him' is Jesus Christ."
      axes: [C_ledger]
      kind: "unpublished manuscript"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "Atheism is so senseless & odious to mankind that it never had many professors."
      cites: [{source: S11, locator: "f. 1r"}]
      context: "'A short Schem of the true Religion' (Keynes MS 7), section 'Of Atheism'. It goes on to argue from the matched left and right sides of animal bodies."
      axes: [D_authority, A_locus]
      kind: "unpublished manuscript"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
  changes_over_life:
    - {value: "Became an Arian (rejected the Trinity) around 1672, after studying the Bible in its original languages; he kept the view largely secret", year: 1672, age: 30, certainty: 0.7, cites: [{source: S12, locator: "first paragraph"}, {source: S4, locator: "§7 ('a committed anti-Trinitarian')"}, {source: S1, locator: "Interest in religion and theology"}], how_known: "The year is from one source (MacTutor, 'around 1672'); the anti-Trinitarian view itself is in three sources."}
  coder_notes: "The code is the hardest call. CHRIST (0.7) rests on private manuscripts; the published texts are theistic only. CLTHEI is a close second. The axes rest on his own words. B = 3 is the weak point for mid_basin: the 'Reformation' passage could be read as B = 2, so B and mid_basin are held at 0.7 (CODING_GUIDE §3). A = 1 rather than 0 because of the substantial omnipresence and the sensorium. C rests on private manuscripts, all post-1710 and so after the major work. E (3) is scored on the world's order (decision P7). It is held at 0.7 because the petition in his private articles (S9) is a named alternative (2)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "English; a family of Lincolnshire yeoman farmers on his father's side, the Ayscoughs on his mother's", certainty: 1.0, cites: [{source: S2, locator: "Biography"}, {source: S1, locator: "Formative influences"}], how_known: "Two sources."}
  religious_heritage_by_birth: {value: "English Protestant; SEP calls the family Puritan", certainty: 0.7, cites: [{source: S3, locator: "§1.1"}], how_known: "One source names the leaning."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1665–1704", certainty: 1.0, cites: [{source: S2, locator: "Biography (plague years)"}, {source: S1, locator: "International prominence; Final years ('the first edition of the Opticks in 1704')"}], how_known: "From the plague-years calculus (1665) to the Opticks (1704), the first and last listed lasting contributions (P29). Span check 2026-10-02 (P29, P30 and its addendum): was 1665–1693, which ended at his breakdown and move to London. The Opticks (1704) was in major_works but not on the list. S1 names it among his notable works and says the calculus first appeared in print in its two appended papers, so it was added and the span ends there. Later editions (1706, 1713, 1717–18, 1726) revise earlier work and are not separate items."}
  age_at_first_lasting_contribution: {value: 23, certainty: 1.0, cites: [{source: S2, locator: "Quick Info; Biography"}], how_known: "Born 4 January 1643 (Gregorian); the plague-years work began in 1665. P30 (rule 5): 1665 − 1642 = 23, with no month adjustment; was 22 until the P30 age sweep (2026-10-02)."}
  first_evidence_of_lio_type_views: {value: "The Principia (1687) treats gravitation as universal, and its rules assign the same causes to the same effects on earth and in the heavens.", year: 1687, age: 45, certainty: 0.7, cites: [{source: S8, locator: "pp. 384–385"}, {source: S1, locator: "opening paragraph"}], how_known: "Earliest dated public statement found. His student notebook (Quaestiones, 1664) and De gravitatione were not read, so an earlier statement may exist."}
  lio_views_relative_to_major_work: {value: "during major work", rationale: "The earliest dated lawful-order statement found is in the Principia itself (1687). The theistic framing in print (General Scholium 1713, Opticks Queries 1717) comes after the major work; the Bentley letters (1692–93) fall at its end. Span check 2026-10-02: against the new 1665–1704 span the Bentley letters are inside and the 1713 and 1717 texts are still after it; the label is unchanged.", certainty: 0.7, cites: [{source: S8, locator: "p. 384"}, {source: S7, locator: "letters of 1692–93"}, {source: S5, locator: "p. 388"}], how_known: "Dated documents; search not exhaustive."}
  worldview_during_major_work: {value: "An anti-Trinitarian Protestant from about 1672 (privately), who in 1692 said he wrote the Principia with an eye to belief in a Deity. The fullest statements of his theism (1713, 1717) and his private creeds (after 1710) are later than the major work.", certainty: 0.7, cites: [{source: S12, locator: "first paragraph"}, {source: S7, locator: "letter of 10 Dec. 1692"}, {source: S5, locator: "p. 388"}], how_known: "Dated documents; the creeds are dated only as after 1710."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "He cast Principia Book III 'into the form of Propositions (in the mathematical way)', and derives the system of the world from definitions, laws and rules; inside nature he allows no exemptions beyond the stated origin and reformation (S6, S8).", certainty: 0.7, cites: [{source: S8, locator: "pp. 383–385"}, {source: S6, locator: "p. 402"}], how_known: "Coder's reading of the Principia's form and his own statement of it."}
  form_acquired: {value: "adulthood, before major work", rationale: "No mathematics is documented before university; he read Euclid in 1663, at 20, two years before the plague-years work (S2).", certainty: 0.7, cites: [{source: S2, locator: "Biography"}, {source: S1, locator: "Formative influences"}], how_known: "Two sources, both hedged."}
  circle_present: {value: "no", rationale: "He denies that God is the soul of the world or that the world is God's body, in his own published words.", certainty: 0.7, cites: [{source: S5, locator: "p. 389"}, {source: S6, locator: "p. 403"}], how_known: "His own texts."}
  reading: "As belief, not finding: Newton has the geometric form, acquired at about 20 rather than in childhood, without the circle. His God is a ruler distinct from the world, though present in space. The record does not test H1, which is about the circle; here the circle is absent. It is a case of form acquired in early adulthood, before the major work."
  notes: ""

institutions:
  - {value: "Trinity College, Cambridge", role: "scholar (1664), minor fellow (1667), major fellow (1668)", years: "1661–1701", kind: university, certainty: 1.0, cites: [{source: S2, locator: "Biography"}, {source: S1, locator: "Career (fellowship 1667)"}], how_known: "Two sources; he resigned his Cambridge posts in 1701."}
  - {value: "University of Cambridge", role: "Lucasian Professor of Mathematics", years: "1669–1701", kind: university, certainty: 1.0, cites: [{source: S1, locator: "Career"}, {source: S2, locator: "Biography"}], how_known: "Two sources."}
  - {value: "Royal Society of London", role: "Fellow (1672); President (1703–1727)", years: "1672–1727", kind: "academy or learned society", certainty: 1.0, cites: [{source: S2, locator: "Biography"}, {source: S1, locator: "Leader of English science; Final years"}], how_known: "Two sources."}
  - {value: "Royal Mint", role: "Warden (1696), Master (1699)", years: "1696–1727", kind: "government or state body", certainty: 1.0, cites: [{source: S2, locator: "Biography"}, {source: S1, locator: "Warden of the mint; Final years"}], how_known: "Two sources."}
  - {value: "Convention Parliament", role: "Member for the University of Cambridge", years: "1689", kind: "government or state body", certainty: 1.0, cites: [{source: S2, locator: "Biography"}, {source: S1, locator: "Warden of the mint"}], how_known: "Two sources."}

collaborators:
  - {value: "Isaac Barrow", relation: "mentor or employer", note: "Lucasian professor who passed Newton's De Analysi to Collins and recommended him as his successor in 1669", certainty: 1.0, cites: [{source: S1, locator: "Career"}, {source: S2, locator: "Biography"}], how_known: "Two sources."}
  - {value: "Edmond Halley", roster_id: halley-edmund, relation: collaborator, note: "asked the 1684 question on orbits and persuaded Newton to write the Principia", years: "1684–1687", certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor."}
  - {value: "Robert Hooke", roster_id: hooke-robert, relation: "rival or critic", note: "disputes over light (from 1672) and over priority", certainty: 1.0, cites: [{source: S1, locator: "Controversy; The Principia"}, {source: S2, locator: "Biography"}], how_known: "Two sources."}
  - {value: "Gottfried Wilhelm Leibniz", roster_id: leibniz-gottfried-wilhelm, relation: "rival or critic", note: "priority dispute over the calculus; criticism of gravity as a 'perpetual miracle'", certainty: 1.0, cites: [{source: S1, locator: "International prominence"}, {source: S4, locator: "§7"}], how_known: "Two sources."}
  - {value: "Christiaan Huygens", roster_id: huygens-christiaan, relation: "rival or critic", note: "objected to his 1672 paper on light", certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "One source."}
  - {value: "John Locke", roster_id: locke-john, relation: correspondent, note: "close friend from 1689; Newton sent him 'Two Notable Corruptions of Scripture'", certainty: 1.0, cites: [{source: S4, locator: "§7"}, {source: S1, locator: "Warden of the mint; Interest in religion and theology"}], how_known: "Two sources."}
  - {value: "Richard Bentley", relation: correspondent, note: "first Boyle lecturer, later Master of Trinity; Newton's 1692–93 letters on God and gravity", years: "1692–1693", certainty: 1.0, cites: [{source: S7, locator: "letters"}, {source: S4, locator: "§7"}], how_known: "Primary letters."}
  - {value: "Samuel Clarke", relation: other, note: "his parish priest in London, who answered Leibniz in the Leibniz–Clarke correspondence", certainty: 0.7, cites: [{source: S4, locator: "§7"}], how_known: "One source."}
  - {value: "Nicolas Fatio de Duillier", relation: other, note: "close friend; the relationship broke off in 1693", years: "to 1693", certainty: 1.0, cites: [{source: S1, locator: "International prominence; Warden of the mint"}, {source: S2, locator: "Biography"}], how_known: "Two sources."}
  - {value: "Roger Cotes", relation: "student or assistant", note: "editor of the second edition of the Principia (1713)", certainty: 1.0, cites: [{source: S1, locator: "Final years"}, {source: S4, locator: "§7"}], how_known: "Two sources."}
  - {value: "René Descartes", roster_id: descartes-rene, relation: "influenced by", note: "his Géométrie and mechanical philosophy, read as an undergraduate", certainty: 1.0, cites: [{source: S1, locator: "Influence of the Scientific Revolution"}, {source: S3, locator: "§1.2"}], how_known: "Two sources."}
  - {value: "Robert Boyle", roster_id: boyle-robert, relation: "influenced by", note: "the foundation for Newton's chemistry", certainty: 1.0, cites: [{source: S1, locator: "Influence of the Scientific Revolution"}, {source: S2, locator: "Biography"}], how_known: "Two sources."}

review:
  roster_status_reason: {value: "Core in v7.1 (no v7 review note) and carried into v8 unchanged; F rose from 4 (v7) to 5 (v8 roster).", certainty: 0.7, cites: [{source: S13, locator: "roster.csv, rank 42"}], how_known: "Study roster."}
  controversies:
    - {value: "Calculus priority dispute with Leibniz; Newton, as President of the Royal Society, appointed the committee and wrote its report", certainty: 1.0, cites: [{source: S1, locator: "International prominence"}, {source: S2, locator: "Biography"}], how_known: "Two sources."}
  data_quality_flags:
    - "Father's death: Britannica and MacTutor say three months before the birth (MacTutor: October 1642); SEP says two months."
    - "Mother's remarriage: MacTutor says when Isaac was two, Britannica 'within two years', SEP 'three years later'. Given as 1645 or 1646."
    - "Calendar: dates are Julian (Old Style) as in the sources; MacTutor converts to Gregorian (4 January 1643, 31 March 1727)."
    - "Grantham schooling start: SEP says 1655; MacTutor says 'shortly after' 1653."
    - "Label for his theology: MacTutor says 'Arian'; SEP says 'anti-Trinitarian' and 'mild heretic'; Britannica 'a fervent if unorthodox Protestant'. The record uses anti-Trinitarian."
    - "The 1662 list of sins is quoted in old spelling by Britannica and in modern spelling by MacTutor."
    - "S8 quotations come from OCR of the 1846 American edition of Motte's translation; an OCR error inside Rule III was left out with [...]."
    - "The General Scholium transcription (S5) splits some words across lines; quotations avoid those spots."
  open_questions:
    - "Read the Quaestiones quaedam philosophicae (1664) and De gravitatione for an earlier dated lawful-order statement (timing)."
    - "Find the household's religious practice and Newton's baptism record."
    - "Key early reading: none documented before university in the sources read; Westfall's Never at Rest may list his Grantham reading."
    - "Date the Twelve Articles, Irenicum and Short Schem more closely (the Newton Project says only post-1710)."
    - "Check whether the Query 31 sentences on 'Reformation' first appeared in the 1706 Latin Queries, and which edition first had Rule III."
    - "CHRIST vs CLTHEI: a reviewer should decide whether the petition articles and the reforming God make CLTHEI the better fit."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Richard S. Westfall"
    citation: "Westfall, Richard S. \"Isaac Newton.\" Encyclopaedia Britannica. Last updated September 26, 2026. https://www.britannica.com/biography/Isaac-Newton (pages: main page with Formative influences and Influence of the Scientific Revolution; Career; The Principia; International prominence, with Warden of the mint, Interest in religion and theology and Leader of English science; Final years)."
    url: "https://www.britannica.com/biography/Isaac-Newton"
    accessed: 2026-10-02
    reliability_note: "Signed article by the author of the standard biography (Never at Rest); fact-checked by Britannica editors."
    used_for: [identity, basics, contribution, childhood, worldview, institutions, collaborators, review]
  - id: S2
    type: tertiary
    kind: encyclopedia
    author: "J. J. O'Connor and E. F. Robertson"
    year: 2000
    citation: "O'Connor, J. J., and E. F. Robertson. \"Isaac Newton.\" MacTutor History of Mathematics Archive, University of St Andrews, last update January 2000. https://mathshistory.st-andrews.ac.uk/Biographies/Newton/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Newton/"
    accessed: 2026-10-02
    reliability_note: "University reference archive; signed; draws on Westfall and reports de Moivre's account."
    used_for: [identity, basics, contribution, childhood, institutions, collaborators, timing, lane_b, heritage]
  - id: S3
    type: tertiary
    kind: encyclopedia
    author: "George Smith"
    year: 2007
    citation: "Smith, George. \"Isaac Newton.\" Stanford Encyclopedia of Philosophy, first published 19 December 2007. https://plato.stanford.edu/entries/newton/."
    url: "https://plato.stanford.edu/entries/newton/"
    accessed: 2026-10-02
    reliability_note: "Peer-reviewed reference entry by a Newton scholar."
    used_for: [basics, contribution, childhood, worldview, heritage]
  - id: S4
    type: tertiary
    kind: encyclopedia
    author: "Andrew Janiak"
    year: 2021
    citation: "Janiak, Andrew. \"Newton's Philosophy.\" Stanford Encyclopedia of Philosophy, first published 13 October 2006, substantive revision 14 July 2021. https://plato.stanford.edu/entries/newton-philosophy/."
    url: "https://plato.stanford.edu/entries/newton-philosophy/"
    accessed: 2026-10-02
    reliability_note: "Peer-reviewed reference entry by the editor of Newton's Philosophical Writings (2004). Section numbers are the coder's reading (§3 space and the divine; §4 rules of reasoning; §7 Locke, Leibniz and Clarke); check against the live entry."
    used_for: [contribution, worldview, collaborators]
  - id: S5
    type: primary
    kind: "published work by the subject"
    author: "Isaac Newton"
    year: 1729
    citation: "Newton, Isaac. \"General Scholium.\" In The Mathematical Principles of Natural Philosophy, trans. Andrew Motte, vol. 2, pp. 387–393. London: Benjamin Motte, 1729. Latin original added to the 2nd edition of the Principia (1713). Transcription: The Newton Project, NATP00056, https://www.newtonproject.ox.ac.uk/view/texts/normalized/NATP00056."
    url: "https://www.newtonproject.ox.ac.uk/view/texts/normalized/NATP00056"
    accessed: 2026-10-02
    reliability_note: "Public text, published in Latin in his lifetime. The English is Motte's translation, two years after Newton's death. Page numbers from the transcription's page markers."
    used_for: [worldview, timing, lane_b]
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "Isaac Newton"
    year: 1730
    citation: "Newton, Isaac. Opticks: or, a Treatise of the Reflections, Refractions, Inflections and Colours of Light. 4th ed., corrected. London, 1730. Project Gutenberg eBook 33504, https://www.gutenberg.org/ebooks/33504. Query 31 near the end of Book III."
    url: "https://www.gutenberg.org/ebooks/33504"
    accessed: 2026-10-02
    reliability_note: "Public text; the Queries were expanded in the Latin (1706) and English (1717–18) editions in his lifetime (S1). Page numbers from the transcription's [Pg] markers, which do not match the 1730 printing (see S14). Project Gutenberg is an unofficial web copy, so under CODING_GUIDE §7 it cannot by itself support certainty 1.0. Its wording was checked against the library scan S14, so every field that cites S6 at 1.0 also cites S14 with the 1730 page."
    used_for: [basics, contribution, worldview, lane_b]
  - id: S7
    type: primary
    kind: letter
    author: "Isaac Newton"
    year: 1692
    citation: "Newton, Isaac. Letters to Richard Bentley, 10 December 1692 (Trinity College Library, Cambridge, 189.R.4.47, ff. 4A–5; Newton Project THEM00254) and 25 February 1692/3 (same volume, ff. 7–8; Newton Project THEM00258). https://www.newtonproject.ox.ac.uk/view/texts/normalized/THEM00254 and https://www.newtonproject.ox.ac.uk/view/texts/normalized/THEM00258."
    url: "https://www.newtonproject.ox.ac.uk/view/texts/normalized/THEM00254"
    accessed: 2026-10-02
    reliability_note: "Original letters, transcribed and tagged by the Newton Project. Private when written."
    used_for: [worldview, timing, collaborators]
  - id: S8
    type: primary
    kind: "published work by the subject"
    author: "Isaac Newton"
    year: 1846
    citation: "Newton, Isaac. The Mathematical Principles of Natural Philosophy, trans. Andrew Motte. First American edition, carefully revised and corrected, with a life of the author by N. W. Chittenden. New York: Daniel Adee, 1846. Book III, 'Rules of Reasoning in Philosophy', pp. 384–385. Scan and OCR: https://archive.org/details/newtonspmathema00newtrich."
    url: "https://archive.org/details/newtonspmathema00newtrich"
    accessed: 2026-10-02
    reliability_note: "Motte's 1729 translation as revised in 1846. Read in OCR; quotations limited to clean passages."
    used_for: [worldview, timing, lane_b]
  - id: S9
    type: primary
    kind: "diary or notebook"
    author: "Isaac Newton"
    citation: "Newton, Isaac. 'Twelve articles on religion'. Keynes MS 8, King's College, Cambridge, post-1710, 1 p. Newton Project THEM00008 (transcribed by Stephen Snobelen; checked against the original by John Young), https://www.newtonproject.ox.ac.uk/view/texts/normalized/THEM00008."
    url: "https://www.newtonproject.ox.ac.uk/view/texts/normalized/THEM00008"
    accessed: 2026-10-02
    reliability_note: "Private manuscript, unpublished in his lifetime (printed by Brewster in 1855, per the Newton Project catalogue). Dated only as post-1710."
    used_for: [worldview]
  - id: S10
    type: primary
    kind: "diary or notebook"
    author: "Isaac Newton"
    citation: "Newton, Isaac. 'Irenicum, or Ecclesiastical Polyty tending to Peace'. Keynes MS 3, King's College, Cambridge, post-1710, 40 pp. Newton Project THEM00003, https://www.newtonproject.ox.ac.uk/view/texts/normalized/THEM00003."
    url: "https://www.newtonproject.ox.ac.uk/view/texts/normalized/THEM00003"
    accessed: 2026-10-02
    reliability_note: "Private manuscript with several drafts; page numbers are the manuscript pages marked in the transcription. Read by keyword search, not in full."
    used_for: [worldview]
  - id: S11
    type: primary
    kind: "diary or notebook"
    author: "Isaac Newton"
    citation: "Newton, Isaac. 'A short Schem of the true Religion'. Keynes MS 7, King's College, Cambridge, post-1710, 4 pp. Newton Project THEM00007, https://www.newtonproject.ox.ac.uk/view/texts/normalized/THEM00007."
    url: "https://www.newtonproject.ox.ac.uk/view/texts/normalized/THEM00007"
    accessed: 2026-10-02
    reliability_note: "Private manuscript (extracts printed by Brewster in 1855, per the Newton Project catalogue)."
    used_for: [worldview]
  - id: S12
    type: tertiary
    kind: encyclopedia
    author: "MacTutor History of Mathematics Archive"
    year: 2006
    citation: "MacTutor History of Mathematics Archive. \"Newton's Arian beliefs.\" University of St Andrews, last updated March 2006. https://mathshistory.st-andrews.ac.uk/Extras/Newton_Arian/."
    url: "https://mathshistory.st-andrews.ac.uk/Extras/Newton_Arian/"
    accessed: 2026-10-02
    reliability_note: "Short reference page; prints Newton's twelve points on why he was an Arian, without a manuscript reference."
    used_for: [worldview, timing]
  - id: S13
    type: tertiary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. v8 roster, data/roster/roster.csv, built by scripts/rebuild_roster.py from the five model lists."
    used_for: [review]
  - id: S14
    type: primary
    kind: "published work by the subject"
    author: "Isaac Newton"
    year: 1730
    citation: "Newton, Isaac. Opticks: or, a Treatise of the Reflections, Refractions, Inflections and Colours of Light. The Fourth Edition, corrected. London: Printed for William Innys, 1730. University of California Libraries copy, Internet Archive scan, https://archive.org/details/opticksortreatis1730newt."
    url: "https://archive.org/details/opticksortreatis1730newt"
    accessed: 2026-10-02
    reliability_note: "Library scan of the edition that S6 transcribes. Used to check S6 wherever a quotation or a certainty-1.0 field rests on it. The five Query 31 quotations and the Query 28 passage on the 'very first Cause' agree word for word, apart from long-s and other OCR noise; a second scan (Oxford copy, https://archive.org/details/opticksoratreat00newtgoog) has its OCR noise in different places, and the two together leave no word in doubt. Page numbers are the printed 1730 ones: Query 28 is on p. 344 and the cited Query 31 passages on pp. 378–381. S6's [Pg] markers are about 24 pages higher, so they do not follow the 1730 pagination."
    used_for: [basics, contribution, worldview]
---

# Isaac Newton

> Status: draft — unreviewed. Worldview coded CHRIST at 0.7 (CLTHEI a close second); all five LIO axes scored; mid_basin true under the P4 test. A few childhood facts are TODO.

## Summary

Isaac Newton (1642–1727, Old Style dates) was an English mathematician and natural philosopher. He was Lucasian Professor at Cambridge, then Master of the Mint and President of the Royal Society [S1; S2]. He found the calculus, the composition of white light, the laws of motion and universal gravitation [S1, opening paragraph]. He spent as much effort on theology and biblical study as on physics [S3]. Privately he rejected the Trinity [S1; S4; S12]. In print he argued that the solar system came from "the counsel and dominion of an intelligent and powerful being" [S5, p. 388].

## Life and work

He was born at Woolsthorpe, Lincolnshire, after his father's death. His mother remarried and left him with his grandmother until 1653 [S1; S2; S3]. He went to the grammar school at Grantham, was taken out to run the farm, and was sent back to prepare for Cambridge [S2; S3]. He entered Trinity College in 1661 [S2].

During the plague years (1665–67) at Woolsthorpe he began the calculus, the optics and the work on gravity [S2]. He became a fellow of Trinity in 1667 and Lucasian Professor in 1669 [S1, Career; S2]. The Principia appeared in 1687 [S1]. After a breakdown in 1693 he moved to London as Warden (1696) and then Master (1699) of the Mint. He became President of the Royal Society in 1703 and was knighted in 1705 [S1; S2]. He brought out the Opticks (1704) and new editions of the Principia (1713, 1726) [S1, Final years].

## Contribution and impact

- 1665–66: method of fluxions (calculus) and the prism experiments [S2; S1, Career].
- 1672: paper on light and colours; Fellow of the Royal Society after giving a reflecting telescope [S2].
- 1687: Principia, with the three laws of motion and universal gravitation [S1; S2].
- 1704: Opticks, with the calculus papers appended [S1, International prominence].

Britannica calls the laws of motion "the basic principles of modern physics" [S1, opening paragraph].

## Childhood and education

His father was a yeoman farmer who could not sign his name [S2]. SEP calls the family Puritan; his stepfather was a minister [S3; S2]. He learned to read and write from his grandmother and mother [S3]. At Grantham he gained Latin but "probably received no more than a smattering of arithmetic" [S1, Formative influences]. MacTutor finds no evidence of school mathematics; he first read Euclid in 1663, at 20 [S2]. At 19 he wrote a list of his sins that included threatening his mother and stepfather [S1; S2].

## Adult working worldview

In print his God is a ruler. He "governs all things, not as the soul of the world, but as Lord over all", and "a God without dominion, providence, and final causes, is nothing else but Fate and Nature" [S5, pp. 389, 391]. God is present everywhere, "not virtually only, but also substantially" [S5, p. 390]. The world is not God's body [S6, p. 403].

His science runs on law. The same effects get the same causes [S8, p. 384]. But the origin of the system needs a choosing agent, and the system may in time need "a Reformation" [S6, p. 402]. In a draft reply to Leibniz he wrote that "gravity without a miracle may keep the planets in" [S4, §7].

His private manuscripts show a scriptural, anti-Trinitarian Christianity: one God the Father and one mediator, Christ; prayer to the Father in the name of Christ; and a final judgement of all people [S9; S10]. MacTutor dates his Arian view to about 1672 [S12].

Coding: CHRIST at 0.7, with CLTHEI as a close second. A_locus 1 at 1.0; B_cause 3 (natural philosophy), C_ledger 0, D_authority 2 and E_scope 3 at 0.7. E is scored on the world's order (decision P7): the same causes for man and beast, Europe and America [S8, p. 384]. The petition in his private articles is the named alternative (2) [S9]. mid_basin is true at 0.7 under P4.

## Heritage (context only)

English, from Lincolnshire yeoman farmers and the Ayscough family [S2; S1]. Heritage is recorded for context only. It is not a worldview code.

## Timing

His first lasting work began in 1665, at 23 [S2]. The earliest dated lawful-order statement found is in the Principia (1687) [S8]. His theism is stated most fully after the major work (1713, 1717), and his private creeds are post-1710 [S5; S6; S9].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Newton shows the geometric form, acquired at about 20 (Euclid in 1663), without the circle: God rules the world and is not its soul [S2; S5, p. 389; S6, p. 403].

## Open questions

- Span check (2026-10-02, P29/P30): primary_system (CHRIST 0.7), A_locus (1 at 1.0), C_ledger (0 at 0.7), D_authority (2 at 0.7), E_scope (3 at 0.7), mid_basin (true at 0.7 (pass)) rest on evidence outside the new span 1665–1704. Values left unchanged pending a ruling; details in reports/p30_span_alignment.csv.
- Earlier dated lawful-order statements (Quaestiones 1664, De gravitatione).
- Household religious practice and baptism record.
- Closer dates for the theological manuscripts.
- Whether the "Reformation" sentence first appeared in the 1706 Latin Queries.
- CHRIST vs CLTHEI: reviewer's call.

## Research log

- 2026-10-02: Read Britannica (S1: main page and four subpages), MacTutor (S2 and the Arian page S12), SEP "Isaac Newton" (S3) and "Newton's Philosophy" (S4). Read the General Scholium (S5) and two Bentley letters (S7) in Newton Project transcriptions, Query 31 of the Opticks (S6, Gutenberg), the Rules of Reasoning (S8, archive.org OCR), and three private theological manuscripts (S9–S11, Newton Project). Wikipedia not used. Every quotation was checked word for word against the fetched text with a script (verify_quotes.py) before commit. Westfall's Never at Rest, the Oxford DNB and the Newton Project's own biography were not read. Baptism, household practice and key early reading left TODO.
- 2026-10-02 (P7): E_scope rechecked on the world's order from the texts already cited (S5, S6, S8, S9); no new sources or quotations. The score stays 3 at 0.7.
