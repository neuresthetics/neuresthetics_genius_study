---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 9
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (overnight agent run for Jason, first pool)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages and scans"
  collected_on: 2026-10-01
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created. Basics, contribution, childhood, worldview (CHRIST at 0.7), A_locus, B_cause, C_ledger, D_authority and mid_basin (true) filled from his own letters, lecture and essays and three reference sources; E_scope left TODO. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "mid_basin rechecked under decision P6 (B_cause scored on the account of nature): B_cause and mid_basin unchanged. Note added to mid_basin how_known. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit fixes: C_ledger certainty 0.7 -> 0.5 (prayers have no judgement or reward language). Consistency pass (CODING_GUIDE §3 cap): B_cause certainty 1.0 -> 0.7, because the coder notes name B = 4 as plausible; mid_basin certainty 1.0 -> 0.7 (result still true). Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit, run 2: E_scope note points to open item P7 (which domain E is scored on). Still TODO. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "P7 decided by Jason (2026-10-02, option 1): E_scope is scored on the world's order. E_scope TODO -> 3 at 0.5, from the sources already cited (S8 the same molecular laws in Sirius and on earth; S9 human will acting within law; S7 prayers that ask for understanding, not favour in events). No text read addresses favour in events directly, so 0.5, with a gap note. No new sources. mid_basin unchanged. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "CODING_GUIDE §7 rule on unofficial web copies: the letters, essays and prayers S4–S7 and S9 were read in the Gutenberg text of Campbell and Garnett 1882 (S3), an unofficial copy. Checked them against S13, the University of Toronto library scan of the 1882 edition (Internet Archive). All seven quotations match word for word except one Gutenberg error: the 1876 letter to Ellicott (p. 394) reads 'founded on a most conjectural scientific hypothesis', not 'almost' (checked on the page image); quotation corrected. The two prayers (S7) are in a footnote on p. 323, not p. 347; locator corrected everywhere. Added S13 cites to the three certainty-1.0 fields that rest on these texts (A_locus, Lewis Campbell and C. J. Ellicott collaborator entries) and to the seven quotations. All stay at 1.0. No value, certainty or mid_basin change."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "S13 scan verification follow-up: the seven quotations checked against the University of Toronto library scan are now marked verified_against primary facsimile; the four S8 lecture quotations and the S3 reported speech remain unchanged. S13 citations were already present. No quotation text or score changed. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Schema 1.1 → 1.2 (decision P8 adds basis recorded_interview and statement kind 'recorded interview'); no content change."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Stage 3 lens-audit rulings applied to the batch's other records (OPEN_DECISIONS P14–P28, v8's picks, 2026-10-02). Schema 1.2 → 1.3. One reliable source caps a fact at 0.7; derived fields take the lowest certainty of their inputs; quote kinds relabelled (P18/P28); kind lists (P21: research institute, school stage and run_by, scholarly edition). Full before → after list: reports/stage3_rulings_changes.csv. Not reviewed."}

identity:
  id: maxwell-james-clerk
  display_name: "James Clerk Maxwell"
  roster:
    canonical_name: "James Clerk Maxwell"
    rank: 43
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: physics
    field_bucket: physics
  full_name: {value: "James Clerk Maxwell", certainty: 1.0, cites: [{source: S1, locator: "opening sentence"}, {source: S3, locator: "p. 2"}], how_known: "Both sources use this name. S1 explains that 'Maxwell' was added to the family name Clerk by his father."}
  native_name: {value: "James Clerk Maxwell", certainty: 0.7, cites: [{source: S1, locator: "opening sentence"}], how_known: "English was his language, so the native form is the roster name."}
  aliases:
    - {name: "James-Clerk-Maxwell", kind: "roster alias"}
    - {name: "Maxwell-James Clerk", kind: "roster alias"}

basics:
  birth:
    date:
      value: "1831-06-13"
      certainty: 1.0
      cites: [{source: S1, locator: "opening sentence; Researcher's Note 'Maxwell's date of birth' (additional-info page)"}, {source: S2, locator: "Quick Info"}, {source: S3, locator: "p. 2"}]
      how_known: "Three sources agree, including his first biographers. Britannica's researcher's note says the date is well grounded and that the November 13 date in some older reference works is an error."
      alternatives:
        - {value: "1831-11-13", cites: [{source: S1, locator: "Researcher's Note 'Maxwell's date of birth'"}], note: "Britannica reports that many printed sources give 13 November, probably spread by its own 11th edition (1910–11) and the Dictionary of National Biography. Not preferred."}
    place:
      value: "No. 14 India Street, Edinburgh, Scotland"
      modern_name: "Edinburgh, Scotland, United Kingdom"
      polity_then: "United Kingdom of Great Britain and Ireland"
      certainty: 1.0
      cites: [{source: S3, locator: "p. 2"}, {source: S2, locator: "Biography, first sentence"}, {source: S1, locator: "opening sentence"}]
      how_known: "Three sources agree; S2 and S3 give the street address."
  death:
    date: {value: "1879-11-05", certainty: 1.0, cites: [{source: S1, locator: "opening sentence; Later life (last paragraph)"}, {source: S2, locator: "Quick Info"}], how_known: "Two independent reference sources agree."}
    place:
      value: "Cambridge, England"
      modern_name: "Cambridge, Cambridgeshire, England, United Kingdom"
      polity_then: "United Kingdom of Great Britain and Ireland"
      certainty: 1.0
      cites: [{source: S1, locator: "opening sentence"}, {source: S2, locator: "Quick Info"}]
      how_known: "Two sources agree. S1 says he was buried at Parton, Scotland."
  first_lasting_contribution_year: {value: 1855, certainty: 0.7, cites: [{source: S3, locator: "p. 517 (Garnett's sketch): 'On Faraday's Lines of Force' read 10 December 1855 and 11 February 1856"}, {source: S3, locator: "p. 221, letter to his father, 3 December 1855"}], how_known: "Year the first part of 'On Faraday's Lines of Force' was read. It is the start of the field work that led to his equations (S1, Later life). His 1846 paper on ovals (age 14) is earlier but is not listed as lasting."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S3, locator: "p. 517"}], how_known: "Derived from first_lasting_contribution_year (1855) under the era buckets (decision P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 1.0, cites: [{source: S1, locator: "opening sentence"}], how_known: "Born in Edinburgh; the United Kingdom is Northern Europe in data/reference/regions.csv (UN M49 sub-region, decision P3)."}
  region_of_work: {value: "Northern Europe", certainty: 1.0, cites: [{source: S1, locator: "Early life; Later life"}, {source: S2, locator: "Biography"}], how_known: "All his posts were in Aberdeen, London and Cambridge, plus his estate at Glenlair (all United Kingdom)."}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S1, locator: "throughout ('he', 'his')"}, {source: S3, locator: "p. 2 ('his parents')"}], how_known: "As the sources record it."}
  languages_of_work: {value: [English], certainty: 1.0, cites: [{source: S8, locator: "whole lecture"}, {source: S1, locator: "Later life (Treatise, 1873)"}], how_known: "His papers, lectures and books were in English."}
  occupations:
    value: ["professor of natural philosophy", "physicist", "laboratory director", "laird of the Glenlair estate"]
    certainty: 1.0
    cites: [{source: S1, locator: "Early life; Later life"}, {source: S2, locator: "Biography"}, {source: S3, locator: "p. 371"}]
    how_known: "Chairs at Aberdeen, London and Cambridge and the Cavendish Laboratory from S1 and S2; the estate from S1 (Early life) and S3."

contribution:
  fields: {value: [physics, "electromagnetism", "kinetic theory of gases", "colour vision", mathematics], certainty: 1.0, cites: [{source: S1, locator: "opening paragraph; Later life"}, {source: S2, locator: "Summary"}], how_known: "Two reference summaries agree."}
  lasting_original_contributions:
    - {value: "'On Faraday's Lines of Force': a mathematical treatment of Faraday's lines of force", year: 1855, kind: theory, lasting: "first step to his field equations", certainty: 1.0, cites: [{source: S3, locator: "p. 517"}, {source: S1, locator: "Later life (preface to the Treatise: to convert Faraday's ideas into mathematical form)"}], how_known: "Read 10 Dec 1855 and 11 Feb 1856 (S3); S1 describes the programme."}
    - {value: "Colour vision measurements with the colour top and colour box, and the three-colour method of colour photography (tartan ribbon, Royal Institution, 1861)", year: "1855–1861", kind: discovery, lasting: "the three-colour method of colour reproduction", certainty: 1.0, cites: [{source: S1, locator: "Later life (colour top, colour box, 1861 lecture)"}, {source: S3, locator: "p. 482 (Rumford Medal 1860 for these researches)"}], how_known: "Two sources agree; years from S1 and S3."}
    - {value: "Saturn's rings must consist of many masses of matter not mutually coherent (Adams Prize essay)", year: 1857, kind: theory, lasting: "confirmed by the Voyager probes more than 100 years later", certainty: 1.0, cites: [{source: S1, locator: "Later life"}, {source: S2, locator: "Biography (Adams Prize of 1857)"}], how_known: "Two sources agree."}
    - {value: "Statistical distribution of molecular velocities in a gas (Maxwell–Boltzmann distribution); kinetic theory of viscosity, conduction and diffusion", year: 1859, kind: "law or principle", lasting: "standard in statistical mechanics", certainty: 1.0, cites: [{source: S1, locator: "Later life"}, {source: S3, locator: "p. 561 ('Illustrations of the Dynamical Theory of Gases', British Association, Aberdeen, 1859)"}], how_known: "Two sources agree; year from S3."}
    - {value: "Electromagnetic field theory: displacement current, electromagnetic waves, and light as an electromagnetic wave ('A Dynamical Theory of the Electro-magnetic Field', read 8 December 1864)", year: 1864, kind: theory, lasting: "Maxwell's equations; radio, which S1 traces to Hertz's 1887 test of the theory", certainty: 1.0, cites: [{source: S3, locator: "p. 550"}, {source: S1, locator: "opening paragraph; Later life"}, {source: S2, locator: "Biography"}], how_known: "Three sources agree; date from S3."}
    - {value: "Maxwell relations of thermodynamics; Maxwell's demon; analysis of speed governors", year: "1860s–1871", kind: "body of work", lasting: "textbook thermodynamics; information theory; control theory", certainty: 0.7, cites: [{source: S1, locator: "Later life"}], how_known: "One reference source; years not given there, so given as a range."}
  evidence_of_impact:
    - {value: "Einstein, in 1931, described the change in physics' conception of reality that came from Maxwell's work as the most profound and fruitful since Newton", kind: "assessment by a later major figure", certainty: 0.7, cites: [{source: S1, locator: "opening paragraph"}], how_known: "Reported by the encyclopedia; Einstein's essay (listed in S2's references) not read."}
    - {value: "Maxwell's equations, the Maxwell–Boltzmann distribution, the Maxwell relations and Maxwell's demon carry his name", kind: "named after them", certainty: 1.0, cites: [{source: S1, locator: "Later life"}, {source: S2, locator: "Biography"}], how_known: "Named in both sources."}
    - {value: "First Cavendish Professor; designed and set up the Cavendish Laboratory (opened 16 June 1874)", kind: "institutional or technological lineage", certainty: 1.0, cites: [{source: S1, locator: "Later life"}, {source: S2, locator: "Biography"}], how_known: "Two sources agree; S2 gives the opening date."}
  major_works:
    - {value: "On Faraday's Lines of Force", year: "1855–1856", kind: "paper or paper series", certainty: 0.7, cites: [{source: S3, locator: "p. 517"}], how_known: "Read before the Cambridge Philosophical Society."}
    - {value: "A Dynamical Theory of the Electro-magnetic Field", year: 1864, kind: "paper or paper series", certainty: 0.7, cites: [{source: S3, locator: "p. 550"}], how_known: "Read before the Royal Society, 8 December 1864."}
    - {value: "A Treatise on Electricity and Magnetism", year: 1873, kind: book, certainty: 1.0, cites: [{source: S1, locator: "Later life"}, {source: S3, locator: "p. 498"}], how_known: "Two sources."}
    - {value: "Molecules (lecture to the British Association at Bradford)", year: 1873, kind: other, certainty: 1.0, cites: [{source: S8, locator: "p. 361 and the edition's source note (From Nature, vol. VIII; the OCR reads 'Till.')"}], how_known: "The lecture text itself."}
  honours:
    - {value: "Second Wrangler, and equal Smith's Prizeman with E. J. Routh, Cambridge", year: 1854, certainty: 1.0, cites: [{source: S3, locator: "p. 176"}, {source: S2, locator: "Biography (Tait: 'bracketed equal with the Senior Wrangler')"}], how_known: "Two sources agree that the Smith's Prize was shared.", alternatives: [{value: "first Smith's prizeman", cites: [{source: S1, locator: "Early life"}], note: "Britannica's wording; it does not mention the tie."}]}
    - {value: "Adams Prize (Cambridge), for the essay on Saturn's rings", year: 1857, certainty: 1.0, cites: [{source: S2, locator: "Biography"}, {source: S1, locator: "Later life ('prizewinning essay')"}], how_known: "Two sources."}
    - {value: "Rumford Medal of the Royal Society, for the colour researches", year: 1860, certainty: 0.7, cites: [{source: S3, locator: "pp. 431, 482"}], how_known: "Stated twice in the biography; S3 p. 431 calls it the first of a long list of honours."}
    - {value: "Fellow of the Royal Society of Edinburgh (1856) and of the Royal Society (1861); Bakerian lecturer (1866)", year: "1856–1866", certainty: 1.0, cites: [{source: S2, locator: "Honours"}, {source: S1, locator: "Early life (Royal Society 1861)"}], how_known: "S2's honours list; S1 confirms 1861."}
  definition_fit: {value: "clearly meets", rationale: "Field equations, kinetic theory and colour work still in use, named laws, and assessments by Einstein and others.", certainty: 0.7, cites: [{source: S1, locator: "opening paragraph; Later life"}], how_known: "Lane A definition (lasting original impact on documented criteria) applied to the contributions listed above."}

childhood:
  family_religion: {value: "Scottish Presbyterian (Church of Scotland) through his father, who was an elder of the parish kirk at Parton; his mother was an Episcopalian.", certainty: 1.0, cites: [{source: S3, locator: "p. 26 (father an elder at Parton); p. 12 (mother 'a good and pious (not bigoted) Episcopalian'); p. 196"}, {source: S11, locator: "section 3 (Presbyterianism of his father's tradition, Anglicanism of his mother)"}], how_known: "The 1882 biography by his friend Campbell, matched by Hutchinson's later summary."}
  family_religious_practice: {value: "In Edinburgh, on Sundays he went with his father to St Andrew's Church in the morning and, at his aunt Jane Cay's wish, to St John's Episcopal Chapel in the afternoon, where he was for a time in Dean Ramsay's catechism class. His mother encouraged him to 'look up through Nature to Nature's God'.", certainty: 0.7, cites: [{source: S3, locator: "pp. 55–56; p. 32"}], how_known: "One contemporary biography, written by a school friend (Campbell)."}
  parents_and_household:
    - {value: "Father, John Clerk Maxwell, of the Clerks of Penicuik; a lawyer (advocate) who inherited the Middlebie estate and took the name Maxwell", name: "John Clerk Maxwell", role: father, certainty: 1.0, cites: [{source: S1, locator: "Early life"}, {source: S3, locator: "p. 2"}], how_known: "Two sources agree."}
    - {value: "Mother, Frances, daughter of R. H. Cay; she was 40 at his birth and died of abdominal cancer in 1839", name: "Frances Clerk Maxwell (née Cay)", role: mother, certainty: 1.0, cites: [{source: S3, locator: "p. 2"}, {source: S1, locator: "Early life"}], how_known: "S3 gives her name; S1 gives her age and death."}
    - {value: "An only child", role: "sibling position", certainty: 1.0, cites: [{source: S1, locator: "Early life"}, {source: S11, locator: "section 2"}], how_known: "Two sources."}
  household_circumstances: {value: "Comfortable: a landed family. The family lived at Glenlair, the house on the Middlebie estate in Kirkcudbrightshire, and stayed with his father's sister in Edinburgh during his school years.", certainty: 1.0, cites: [{source: S1, locator: "Early life ('a comfortable middle-class background')"}, {source: S2, locator: "Biography (Glenlair; 31 Heriot Row)"}], how_known: "Two sources agree."}
  schooling:
    - {value: "Taught at home by his mother until her last illness in 1839", stage: home, years: "to 1839", ages: "to 8", certainty: 0.7, cites: [{source: S3, locator: "p. 32"}], how_known: "One contemporary biography."}
    - {value: "A private tutor at Glenlair; the arrangement failed", stage: tutor, years: "c. 1839–1841", certainty: 1.0, cites: [{source: S1, locator: "Early life ('a dull and uninspired tutor')"}, {source: S2, locator: "Biography ('A 16 year old boy was hired to act as tutor')"}], how_known: "Two sources agree that a tutor was tried and did not work."}
    - {value: "Edinburgh Academy", stage: "grammar or secondary school", institution: "Edinburgh Academy", years: "1841–1847", ages: "10–16", certainty: 1.0, cites: [{source: S1, locator: "Early life"}, {source: S2, locator: "Biography (arrived 18 November 1841)"}], how_known: "Two sources agree on the start; the end is his entry to the university in November 1847 (S2)."}
    - {value: "University of Edinburgh: mathematics (Kelland), natural philosophy (J. D. Forbes) and logic (William Hamilton)", stage: university, institution: "University of Edinburgh", years: "1847–1850", ages: "16–19", certainty: 1.0, cites: [{source: S2, locator: "Biography (November 1847)"}, {source: S1, locator: "Early life (entered at 16)"}], how_known: "Two sources agree."}
    - {value: "University of Cambridge: Peterhouse for one term, then Trinity College; Second Wrangler in 1854", stage: university, institution: "Peterhouse and Trinity College, Cambridge", years: "1850–1854", ages: "19–22", certainty: 1.0, cites: [{source: S2, locator: "Biography (October 1850)"}, {source: S3, locator: "pp. 134, 176"}], how_known: "Two sources agree."}
  early_mathematics: {value: "advanced mathematics", ages: "by 14 to 18", description: "By the time of his 1846 ovals paper (age 14) he had had 'no instruction in mathematics beyond a few books of Euclid and the merest elements of Algebra' (Tait, quoted in S3 p. 87). From 16 he studied university mathematics under Kelland at Edinburgh (S2).", certainty: 1.0, cites: [{source: S3, locator: "p. 87"}, {source: S2, locator: "Biography (ovals paper at 14; Kelland's class from November 1847)"}, {source: S1, locator: "Early life (first paper at 14)"}], how_known: "Three sources agree on the ovals paper at 14 and university mathematics from 16."}
  early_geometric_style_reasoning: {value: "Yes, documented. Euclid at the Edinburgh Academy before age 14. His school manuscripts of 1846–47 (on ovals, meloids and trifocal curves) were, in his schoolfellow Tait's words, 'drawn up in strict geometrical form, and divided into consecutive propositions'. At 16 he took William Hamilton's logic class.", certainty: 1.0, cites: [{source: S3, locator: "p. 87 (Tait's recollection)"}, {source: S2, locator: "Biography (logic class taught by William Hamilton)"}], how_known: "Tait saw and kept the manuscripts; S2 confirms the logic class. Facts only; Lane B reading is in lane_b."}
  early_science_exposure:
    - {value: "Taken 'to see electro-magnetic machines'", year: 1842, age: 10, certainty: 0.7, cites: [{source: S3, locator: "pp. 52–53 (12 February 1842)"}], how_known: "One source, quoting a family diary."}
    - {value: "First scientific paper, 'On the description of Oval Curves, and those having a plurality of Foci', communicated by J. D. Forbes to the Royal Society of Edinburgh", year: 1846, age: 14, certainty: 1.0, cites: [{source: S3, locator: "p. 87"}, {source: S1, locator: "Early life"}, {source: S2, locator: "Biography"}], how_known: "Three sources agree."}
    - {value: "Free use of J. D. Forbes's class apparatus at the University of Edinburgh", year: "1847–1850", age: "16–19", certainty: 0.7, cites: [{source: S2, locator: "Biography (Tait's account of the winter of 1847)"}], how_known: "One source quoting Tait."}
  key_early_reading:
    - {value: "The Bible, especially the Psalms: at eight he is said to have repeated the whole of Psalm 119", age: 8, certainty: 0.7, cites: [{source: S3, locator: "p. 32"}], how_known: "One source; the biographer writes 'it is said'."}
    - {value: "Milton, known from very early", certainty: 0.7, cites: [{source: S3, locator: "p. 32"}], how_known: "One source."}
  childhood_mentors:
    - {value: "His aunt Jane Cay, who had him sent to the Edinburgh Academy and wanted him at the Episcopal chapel", name: "Jane Cay", role: aunt, certainty: 1.0, cites: [{source: S1, locator: "Early life"}, {source: S3, locator: "p. 55"}], how_known: "Two sources."}
    - {value: "James David Forbes, professor of natural philosophy at Edinburgh, who communicated his first paper", name: "J. D. Forbes", years: "1846–1850", certainty: 1.0, cites: [{source: S3, locator: "p. 87"}, {source: S2, locator: "Biography"}], how_known: "Two sources."}
    - {value: "Dean (Edward) Ramsay of St John's Episcopal Chapel, Edinburgh, whose catechism class he attended", name: "Dean Ramsay", certainty: 0.7, cites: [{source: S3, locator: "pp. 55–56"}], how_known: "One source."}
  languages_in_childhood: {value: [English, "Scots (Galloway speech)"], certainty: 0.7, cites: [{source: S3, locator: "p. 49 ('his Corsock patois')"}], how_known: "Campbell describes his country accent at school. One source."}
  notable_events:
    - {value: "Death of his mother", year: 1839, age: 8, certainty: 1.0, cites: [{source: S1, locator: "Early life"}, {source: S3, locator: "p. 32"}], how_known: "Two sources."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1855–1879", certainty: 1.0, cites: [{source: S3, locator: "p. 517"}, {source: S1, locator: "Later life"}], how_known: "From the Lines of Force paper (1855) to his death."}
  nominal_affiliations:
    - {value: "Elder of the Church of Scotland parish kirk at Parton; he arranged to leave Cambridge each summer to help at the midsummer communion there", years: "Cambridge years (1871–1879) at least", role: elder, certainty: 0.7, cites: [{source: S3, locator: "p. 371"}], how_known: "One contemporary biography. The start of the eldership is not given."}
    - {value: "Endowed the church and built the manse at Corsock, near Glenlair", certainty: 0.7, cites: [{source: S3, locator: "p. 371"}], how_known: "One source. S3 p. 26 dates the church to 1838 and full endowment to 1862."}
    - {value: "Attended a Baptist chapel when in London", years: "1860–1865 (London years)", certainty: 0.7, cites: [{source: S11, locator: "section 3, quoting a letter to the Rev. C. B. Tayler"}], how_known: "Hutchinson quotes his letter; the letter itself was not found in the 1882 edition read (it may be in the 1884 edition)."}
  self_described_science_religion_relation:
    value: "Christians with scientific minds should study science to widen their view of God's glory, but each person's attempts to harmonise science with Christianity matter only to that person, and only for a time. Interpretations of scripture should not be tied to scientific hypotheses, which change faster than interpretations do."
    certainty: 0.7
    cites: [{source: S6, locator: "draft reply, pp. 404–405"}, {source: S5, locator: "letter of Nov. 1876, p. 394"}]
    how_known: "His own words in two private documents written a year apart that agree (see statements). Paraphrase; quotations are in statements."
  primary_system:
    value: CHRIST
    basis: consistent_private_letters
    certainty: 0.7
    cites: [{source: S4, locator: "pp. 178–180"}, {source: S6, locator: "pp. 404–405"}, {source: S7, locator: "p. 323 n. 1"}, {source: S3, locator: "p. 371"}]
    how_known: "His Christian belief is in his own words across private documents from 1852 to the 1870s (letters, a draft reply, prayers among his papers). His only public statement read (S8) is theistic but not specifically Christian, so 1.0 is not reached."
    rationale: "CHRIST fits 'the religion as practised and confessed': a Bible-centred Presbyterian elder who calls Christianity 'the only scheme or form of belief' that keeps nothing off-limits to inquiry (S4). Neither theism split fits better: no Aristotelian-Thomistic framework (not CLASS_THEISM), and no claims of intervention or miracle in nature were found (not CLTHEI). The v7.1 rule 'Faraday and Maxwell pass' (church members whose writings show the belief) is met here by his writings, not by his eldership."
  secondary_system: {value: UNKNOWN, how_known: "No second system; he published in no other system."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Chosen. Elder of the kirk; Bible-centred faith in letters and prayers; 'no God but the Author of Salvation' (S4).", cites: [{source: S4, locator: "p. 179"}, {source: S3, locator: "p. 371"}]}
    - {code: CLTHEI, reason: "Rejected for now. His prayers ask God to teach and bless (petition), but nothing read claims God intervenes in physical events, and his science treats molecules as unchanged since creation. Would need texts on providence or miracle.", cites: [{source: S7, locator: "p. 323 n. 1"}, {source: S8, locator: "pp. 376–377"}]}
    - {code: CLASS_THEISM, reason: "Rejected. No Aristotelian-Thomistic or falsafa framework found. His design argument from molecules rests on Herschel, not on scholastic metaphysics.", cites: [{source: S5, locator: "p. 393"}]}
    - {code: DEISM, reason: "Rejected. He prays to a personal God who is 'mindful of us', and his faith is centred on Christ.", cites: [{source: S7, locator: "p. 323 n. 1"}]}
    - {code: PANT, reason: "Rejected. He lists the 'Pantheist' among those who keep forbidden ground, and contrasts the pantheist's God of Nature with the God of the Bible.", cites: [{source: S4, locator: "p. 179"}]}
  lio_axes:
    A_locus:
      value: 0
      basis: written_profession
      certainty: 1.0
      cites: [{source: S8, locator: "pp. 376–377"}, {source: S4, locator: "p. 179"}, {source: S13, locator: "p. 179"}]
      how_known: "Public lecture text (1873), consistent with his 1852 letter; written profession, so 1.0."
      rationale: "Transcendent person outside the world. In a public lecture (1873) he argues that molecules cannot be eternal and self-existent and 'must have been created', and closes on 'Him who in the beginning created, not only the heaven and the earth, but the materials of which heaven and earth consist'. The creator is distinct from what he made. In 1852 he rejects the pantheist's God of Nature. No immanence or world-soul language was found in the texts read."
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.7
      cites: [{source: S8, locator: "p. 376"}, {source: S9, locator: "pp. 443–444"}]
      how_known: "Public lecture text (1873) for the law and the stated limit; the Eranus essay agrees. Written profession; certainty capped at 0.7 because the record names a plausible alternative score (CODING_GUIDE §3): the coder notes say the creation limit could be read as the edge of science, scoring 4. Lowered from 1.0 in the consistency pass after the lens audit (2026-10-02)."
      rationale: "Scored for his physics. Laws hold without exception everywhere: a hydrogen molecule in Sirius or Arcturus 'executes its vibrations in precisely the same time' (S8). One stated, limited exception: the existence and identical properties of molecules cannot be ascribed to 'any of the causes which we call natural', so science stops at their creation (S8, p. 376). In his 1873 Eranus essay, free will acts at 'singular points' inside physical law, not as an exemption from it (S9). Outside his science his prayers include petition (S7); that is not scored here."
    C_ledger:
      value: 1
      basis: consistent_private_letters
      certainty: 0.5
      cites: [{source: S7, locator: "p. 323 n. 1"}, {source: S4, locator: "p. 179"}]
      how_known: "Two prayers and a letter, all private, that agree. They speak to the axis only indirectly: liturgical, psalm-like phrasing, with no judgement or reward after death. So 0.5, the coder's inference (lens audit, 2026-10-02; CODING_GUIDE §3)."
      rationale: "Leans to personal reward and punishment: two prayers among his papers ask for 'the remission of our sins' and that 'the wicked be no more', and the 1852 letter names God 'the Author of Salvation'. Private writings that agree, but the reading is an inference from liturgical phrasing, so 0.5. No text read on punishment after death, so not scored 0."
    D_authority:
      value: 2
      basis: consistent_private_letters
      certainty: 0.7
      cites: [{source: S5, locator: "p. 394"}, {source: S6, locator: "pp. 404–405"}, {source: S4, locator: "p. 178"}]
      how_known: "Two private letters and a draft reply (1852, 1875, 1876) that agree; so 0.7."
      rationale: "Holds both, in different domains. In science, observation and hypothesis rule, and he refuses to fix scripture to scientific theories (S5) or to give harmonising efforts a society's stamp (S6). In faith, scripture is the authority, and he regards Christianity as the one belief that can be examined without limit (S4). Neither ranks over the other in the texts read. Private letters and a draft that agree, so 0.7."
    E_scope:
      value: 3
      basis: scholarly_reconstruction
      certainty: 0.5
      cites: [{source: S8, locator: "pp. 376–377"}, {source: S9, locator: "p. 443"}, {source: S7, locator: "p. 323 n. 1"}]
      how_known: "Coder's reading of his public lecture (S8), an essay for a private club (S9) and private prayers (S7). They show one order for stars, earth and humans, but none addresses favour for a group in events directly, so 0.5. Scored under decision P7 (2026-10-02); it was TODO before. Gap: Theerman 1986 and the 1884 edition of the Life, on providence and prayer, were not read and could raise or lower this."
      rationale: "Scored on the world's order (decision P7). Leans LIO. The same laws hold for stars and earth: a hydrogen molecule 'whether in Sirius or in Arcturus, executes its vibrations in precisely the same time' (S8, p. 376), and molecules 'continue this day as they were created' (S8, p. 377). Humans are inside the same order. 'Every existence above a certain rank has its singular points', where small influences such as the will can produce large results (S9, p. 443). That is a ranking of beings within physical law, not an exemption from it, and it is why the score is 3 rather than 4. His private prayers petition God to 'teach us to study the works of Thy hands' and to 'strengthen our reason' (S7). They ask for understanding and service, not for favour in events. No text read says God favours believers in what happens. The creation of molecules (S8) is a limit on B, not a favour to a group. Named alternative 4, if the singular points are read as plain physics. The 'knowledge of salvation' in the same prayer (S7) is scored on C, not here."
  mid_basin:
    value: true
    certainty: 0.7
    cites: [{source: S8, locator: "pp. 376–377"}]
    how_known: "Applied the P4 test to the axis scores above: A_locus = 0 at 1.0 and B_cause = 3 at 0.7, so true. Certainty 0.7: mid_basin is no surer than the less certain of A and B (CODING_GUIDE §3). B = 4, the named alternative, also gives true. Rechecked under decision P6 (2026-10-02): B is scored on his account of nature, which is his physics, so the result is unchanged."
    rationale: "P4 test (METHOD §1.1): A_locus = 0 (≤ 1) at certainty 1.0, and B_cause = 3 (≥ 3) scored for his physics at certainty 0.7. Both at ≥ 0.7, so true. F = 5, so 'first-rank' is also met (applied separately)."
  statements:
    - text: "Nothing is to be holy ground consecrated to Stationary Faith, whether positive or negative."
      cites: [{source: S4, locator: "p. 178"}, {source: S13, locator: "p. 178"}]
      date: "1852-03-07"
      context: "Letter from Cambridge to his school friend Lewis Campbell, describing his 'great plan' of letting nothing be left unexamined."
      axes: [D_authority]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
      note: "Transcription as printed in the 1882 Life (Gutenberg text of the 1882 edition)."
    - text: "Christianity—that is, the religion of the Bible—is the only scheme or form of belief which disavows any possessions on such a tenure. Here alone all is free. You may fly to the ends of the world and find no God but the Author of Salvation. You may search the Scriptures and not find a text to stop you in your explorations."
      cites: [{source: S4, locator: "p. 179"}, {source: S13, locator: "p. 179"}]
      date: "1852-03-07"
      context: "Same letter. 'Such a tenure' refers to ground kept 'Tabooed' from inquiry, which he says the Scoffer, the Pantheist and others hold."
      axes: [D_authority, A_locus, C_ledger]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "the exact equality of each molecule to all others of the same kind gives it, as Sir John Herschel has well said, the essential character of a manufactured article, and precludes the idea of its being eternal and self-existent."
      cites: [{source: S8, locator: "p. 376"}]
      date: "1873"
      context: "Evening lecture 'Molecules' to the British Association at Bradford, printed in Nature."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
      note: "Checked against the OCR of the 1890 Scientific Papers (Niven ed.), vol. 2. OCR is faulty in nearby sentences ('hn produced'), so only clean passages are quoted."
    - text: "Science is arrested when she assures herself, on the one hand, that the molecule has been made, and on the other, that it has not been made by any of the processes we call natural"
      cites: [{source: S8, locator: "p. 376"}]
      date: "1873"
      context: "Same lecture, a few sentences later."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "They continue this day as they were created—perfect in number and measure and weight, and from the ineffaceable characters impressed on them we may learn that those aspirations after accuracy in measurement, truth in statement, and justice in action, which we reckon among our noblest attributes as men, are ours because they are essential constituents of the image of Him who in the beginning created, not only the heaven and the earth, but the materials of which heaven and earth consist."
      cites: [{source: S8, locator: "p. 377 (closing sentence)"}]
      date: "1873"
      context: "Closing sentence of the lecture; 'They' are the molecules."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "A molecule of hydrogen, for example, whether in Sirius or in Arcturus, executes its vibrations in precisely the same time."
      cites: [{source: S8, locator: "p. 376"}]
      date: "1873"
      context: "Same lecture, on spectroscopic evidence that distant stars are made of the same molecules as the earth."
      axes: [B_cause, E_scope]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "Every existence above a certain rank has its singular points: the higher the rank, the more of them. At these points, influences whose physical magnitude is too small to be taken account of by a finite being, may produce results of the greatest importance."
      cites: [{source: S9, locator: "p. 443"}, {source: S13, locator: "p. 443"}]
      date: "1873-02-11"
      context: "Essay read to the Eranus club in Cambridge on whether physical science favours determinism over free will."
      axes: [B_cause, E_scope]
      kind: "unpublished manuscript"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
      note: "A paper written for a private discussion club of senior colleagues; printed entire in the 1882 Life."
    - text: "What I thought of was not so much that uniformity of result which is due to uniformity in the process of formation, as a uniformity intended and accomplished by the same wisdom and power of which uniformity, accuracy, symmetry, consistency, and continuity of plan are as important attributes as the contrivance of the special utility of each individual thing."
      cites: [{source: S5, locator: "p. 393"}, {source: S13, locator: "p. 393"}]
      date: "1876-11"
      context: "Reply by return of post to C. J. Ellicott, Bishop of Gloucester and Bristol, who had asked where the phrase 'manufactured articles' came from."
      axes: [A_locus, B_cause]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "But I should be very sorry if an interpretation founded on a most conjectural scientific hypothesis were to get fastened to the text in Genesis, even if by so doing it got rid of the old statement of the commentators which has long ceased to be intelligible. The rate of change of scientific hypothesis is naturally much more rapid than that of Biblical interpretations, so that if an interpretation is founded on such an hypothesis, it may help to keep the hypothesis above ground long after it ought to be buried and forgotten."
      cites: [{source: S5, locator: "p. 394"}, {source: S13, locator: "p. 394"}]
      date: "1876-11"
      context: "Same letter, answering the bishop's question whether light created before the sun (Genesis 1) could be squared with science."
      axes: [D_authority]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "I think men of science as well as other men need to learn from Christ, and I think Christians whose minds are scientific are bound to study science that their view of the glory of God may be as extensive as their being is capable of. But I think that the results which each man arrives at in his attempts to harmonise his science with his Christianity ought not to be regarded as having any significance except to the man himself, and to him only for a time, and should not receive the stamp of a society."
      cites: [{source: S6, locator: "pp. 404–405"}, {source: S13, locator: "pp. 404–405"}]
      date: "1875"
      context: "Rough draft of his reply declining an invitation (March 1875) to join the Victoria Institute, a society for relating science and Christian faith. The draft breaks off; S3 prints 'all that has been found'."
      axes: [D_authority]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "Almighty God, who hast created man in Thine own image, and made him a living soul that he might seek after Thee and have dominion over Thy creatures, teach us to study the works of Thy hands that we may subdue the earth to our use, and strengthen our reason for Thy service; and so to receive Thy blessed Word, that we may believe on Him whom Thou hast sent to give us the knowledge of salvation and the remission of our sins."
      cites: [{source: S7, locator: "p. 323 n. 1"}, {source: S13, locator: "p. 323 n. 1"}]
      context: "One of two undated prayer fragments 'found amongst his papers', printed by Campbell."
      axes: [C_ledger, A_locus, E_scope]
      kind: "document in own hand"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "I have looked into most philosophical systems, and I have seen that none will work without a God."
      cites: [{source: S3, locator: "p. 426"}]
      date: "1879"
      context: "Said in his last days; repeated by Colin Mackenzie to Campbell."
      axes: [A_locus]
      kind: "reported speech"
      verified_against: "secondary quotation"
      verified_on: 2026-10-02
      note: "Reported speech: never a written profession. Not used for any score."
  changes_over_life:
    - {value: "A deepening of religious conviction after an illness in 1853 while staying with the Rev. C. B. Tayler's family in Suffolk; he later said it gave him a new perception of the love of God", year: 1853, age: 22, certainty: 0.7, cites: [{source: S3, locator: "pp. 169–170"}, {source: S11, locator: "section 3"}], how_known: "Campbell's account, repeated by Hutchinson from it, so one line of evidence."}
  coder_notes: "Code and four axes rest on his own words. The two weakest points: (1) CHRIST is 0.7 because the specifically Christian statements are private; (2) B = 3 rather than 4 because of the stated limit at the creation of molecules. A reviewer who reads that limit as the edge of science rather than an exception could score B = 4; mid_basin is true either way. E_scope is 3 at 0.5 on the world's order (decision P7); no text read addresses favour for a group in events directly."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Scottish; the Clerk family of Penicuik on his father's side, the Cay family on his mother's", certainty: 1.0, cites: [{source: S3, locator: "p. 2"}, {source: S1, locator: "opening sentence"}], how_known: "Two sources."}
  religious_heritage_by_birth: {value: "Church of Scotland (father) and Scottish Episcopal (mother)", certainty: 1.0, cites: [{source: S3, locator: "pp. 12, 26"}, {source: S11, locator: "section 3"}], how_known: "Two sources agree."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: "Learned 'his questions' (the Presbyterian catechism) as a child, and the Episcopal catechism in Dean Ramsay's class, so he 'became equally acquainted with the catechisms both of the Scotch and of the English Church'", certainty: 0.7, cites: [{source: S3, locator: "pp. 55–56"}], how_known: "One contemporary source."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1855–1879", certainty: 1.0, cites: [{source: S3, locator: "p. 517"}, {source: S1, locator: "Later life"}], how_known: "From the Lines of Force paper to his death; the Treatise appeared in 1873."}
  age_at_first_lasting_contribution: {value: 24, certainty: 0.7, cites: [{source: S3, locator: "pp. 2, 517"}], how_known: "Born 13 June 1831; first part of the Lines of Force paper read 10 December 1855."}
  first_evidence_of_lio_type_views: {value: "In a February 1856 essay he wrote that interference with the laws of thought by organic laws or physical disturbances is 'no doubt' regulated by the laws of the brain: law without exemption, even for thought.", year: 1856, age: 24, certainty: 0.7, cites: [{source: S10, locator: "p. 240"}], how_known: "His own essay. Earliest dated statement of this kind found in a keyword search of the 1882 Life; earlier letters were not read in full, so an earlier statement may exist."}
  lio_views_relative_to_major_work: {value: "during major work", rationale: "The earliest dated lawful-order statement found (February 1856) falls two months after the first Lines of Force reading (December 1855). The geometric training is earlier (see childhood), but that is form, not a stated view.", certainty: 0.7, cites: [{source: S10, locator: "p. 240"}, {source: S3, locator: "p. 517"}], how_known: "Dated documents; search not exhaustive."}
  worldview_during_major_work: {value: "A practising Presbyterian and elder who believed molecules were created and that science stops at their origin (1873), while keeping science and scripture interpretation apart (1875–76).", certainty: 0.7, cites: [{source: S8, locator: "pp. 376–377"}, {source: S5, locator: "p. 394"}, {source: S3, locator: "p. 371"}], how_known: "His own public lecture and private letters, plus one biographer for the eldership."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "His physics derives consequences from stated principles with no exemption inside nature; the one limit he states (the creation of molecules) is placed at the edge of science, not inside it (S8).", certainty: 0.7, cites: [{source: S8, locator: "pp. 376–377"}, {source: S3, locator: "p. 87"}], how_known: "Coder's reading of his own lecture and the record of his early work."}
  form_acquired: {value: "childhood or adolescence", rationale: "Euclid before 14 and school papers 'drawn up in strict geometrical form, and divided into consecutive propositions' at 14–15; logic at 16.", certainty: 0.7, cites: [{source: S3, locator: "p. 87"}, {source: S2, locator: "Biography"}], how_known: "Tait's recollection and the university record."}
  circle_present: {value: "no", rationale: "God is a creator distinct from nature, and he rejects the pantheist's God of Nature in his own words.", certainty: 0.7, cites: [{source: S4, locator: "p. 179"}, {source: S8, locator: "p. 377"}], how_known: "His own letter and lecture."}
  reading: "As belief, not finding: Maxwell is a case of early geometric form without the circle, in a devout Christian whose physics allows no exemptions inside nature. The v7.1 papers say a devout lawful physicist 'is predicted, not forbidden', and list as damaging 'Faraday/Maxwell look like late professional lawfulness only'. For Maxwell the form is documented from age 14, before any professional training, so this record does not support the 'late professional lawfulness only' reading. It also does not test H1, which is about the circle; here the circle is absent."
  notes: ""

institutions:
  - {value: "Trinity College, Cambridge", role: "Fellow", years: "1855–1856", kind: university, certainty: 0.7, cites: [{source: S1, locator: "Early life ('elected to a fellowship at Trinity')"}], how_known: "One source; years inferred from his move to Aberdeen in 1856."}
  - {value: "Marischal College, Aberdeen", role: "Professor of Natural Philosophy", years: "1856–1860", kind: university, certainty: 1.0, cites: [{source: S1, locator: "Early life"}, {source: S2, locator: "Biography"}], how_known: "Two sources agree."}
  - {value: "King's College, London", role: "Professor of Natural Philosophy", years: "1860–1865", kind: university, certainty: 1.0, cites: [{source: S1, locator: "Early life; Later life"}, {source: S2, locator: "Biography"}], how_known: "Two sources agree."}
  - {value: "University of Cambridge, Cavendish Laboratory", role: "first Cavendish Professor of Physics", years: "1871–1879", kind: university, certainty: 1.0, cites: [{source: S1, locator: "Later life"}, {source: S2, locator: "Biography"}], how_known: "Two sources agree."}
  - {value: "British Association for the Advancement of Science, committee on electrical standards", role: "supervised the determination of electrical units", years: "1860s", kind: "academy or learned society", certainty: 0.7, cites: [{source: S1, locator: "Early life (last paragraph)"}], how_known: "One source."}
  - {value: "Royal Society of London", role: "Fellow", years: "1861–1879", kind: "academy or learned society", certainty: 1.0, cites: [{source: S1, locator: "Early life"}, {source: S2, locator: "Honours"}], how_known: "Two sources."}
  - {value: "Parish kirk of Parton (Church of Scotland)", role: elder, kind: "religious body", certainty: 0.7, cites: [{source: S3, locator: "p. 371"}], how_known: "One source."}

collaborators:
  - {value: "Michael Faraday", roster_id: faraday-michael, relation: "influenced by", certainty: 1.0, cites: [{source: S1, locator: "opening paragraph; Later life"}, {source: S3, locator: "p. 517"}], how_known: "His field theory set out to put Faraday's lines of force into mathematical form."}
  - {value: "Peter Guthrie Tait", relation: other, note: "schoolfellow at the Edinburgh Academy and lifelong friend", years: "1841–1879", certainty: 1.0, cites: [{source: S1, locator: "Early life"}, {source: S2, locator: "Biography"}], how_known: "Two sources."}
  - {value: "Lewis Campbell", relation: correspondent, note: "school friend, main correspondent, and first biographer (S3)", years: "1841–1879", certainty: 1.0, cites: [{source: S1, locator: "Early life"}, {source: S4, locator: "whole letter"}, {source: S13, locator: "pp. 178–180"}], how_known: "Primary letters and an encyclopedia."}
  - {value: "William Hopkins", relation: teacher, years: "1850–1854", note: "Cambridge mathematics coach", certainty: 0.7, cites: [{source: S1, locator: "Early life"}], how_known: "Encyclopedia."}
  - {value: "Ludwig Boltzmann", roster_id: boltzmann-ludwig, relation: other, note: "co-founder of the kinetic theory of gases; the velocity law carries both names", certainty: 0.7, cites: [{source: S3, locator: "p. 561"}, {source: S1, locator: "Later life"}], how_known: "Named together in both sources; no direct collaboration documented."}
  - {value: "Albert Einstein", roster_id: einstein-albert, relation: influenced, certainty: 0.7, cites: [{source: S1, locator: "opening paragraph"}], how_known: "Encyclopedia, citing Einstein's 1931 assessment."}
  - {value: "Max Planck", roster_id: planck-max, relation: influenced, certainty: 0.7, cites: [{source: S1, locator: "opening paragraph"}], how_known: "S1 links Planck's quantum hypothesis to the radiation law derived from Maxwell's theory. One source."}
  - {value: "C. J. Ellicott, Bishop of Gloucester and Bristol", relation: correspondent, years: "1876", certainty: 1.0, cites: [{source: S5, locator: "whole exchange"}, {source: S13, locator: "pp. 392–395"}], how_known: "Primary letters."}
  - {value: "John Ambrose Fleming, Richard Tetley Glazebrook, John Henry Poynting, Arthur Schuster, William D. Niven", relation: "student or assistant", years: "1871–1879", certainty: 0.7, cites: [{source: S1, locator: "Later life"}], how_known: "Listed as his students at the Cavendish by one source."}

review:
  roster_status_reason: {value: "Core in v7.1 (no v7 review note) and carried into v8 unchanged; F rose from 4 to 5 when the Claude list was counted.", certainty: 0.7, cites: [{source: S12, locator: "roster.csv, rank 43"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Birth date: older reference works (Britannica 11th ed., DNB 1921) give 13 November 1831; 13 June is correct per S1's researcher's note and S2, S3."
    - "Smith's Prize 1854: S1 says 'first Smith's prizeman'; S2 and S3 say he and Routh were declared equal. The tie is used."
    - "S1 says he 'received no public honours', while S3 (p. 431) lists many academic honours from 1860 on. S1 probably means state honours; not a real conflict, but worded loosely."
    - "S2 says he spent six years at King's College London, but gives 1860 to spring 1865. Five years is used."
    - "The Baptist-chapel letter to C. B. Tayler is quoted by S11 but was not found in the 1882 edition of the Life (S3); it may be in the 1884 edition."
    - "S8 quotations come from OCR of the 1890 Scientific Papers; some nearby sentences have OCR errors and were not quoted."
  open_questions:
    - "E_scope (3 at 0.5, decision P7): does he anywhere expect God to favour believers in events (providence, answered petition)? Read Theerman 1986 (Am. J. Phys. 54: 312–317), the 1884 edition of the Life and Stanley, Huxley's Church and Maxwell's Demon (2015) to raise or revise it."
    - "Find and read the Tayler letter on the London Baptist chapel (1884 edition of the Life) and quote it from the primary text."
    - "When did he become an elder at Parton? S3 gives no start year."
    - "Baptism: no record found in S3; check parish records or Harman's Scientific Letters and Papers."
    - "Year of Theory of Heat (first edition) not checked."
    - "CLTHEI check: any statement on providence, answered prayer or miracle in nature would bear on the code and on B outside his science."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Cyril Domb"
    citation: "Domb, Cyril. \"James Clerk Maxwell.\" Encyclopaedia Britannica. Last updated August 13, 2026. https://www.britannica.com/biography/James-Clerk-Maxwell (pages: main page with Early life; Later life; additional info with Researcher's Note)."
    url: "https://www.britannica.com/biography/James-Clerk-Maxwell"
    accessed: 2026-10-02
    reliability_note: "Signed article by a physicist who edited Clerk Maxwell and Modern Science; fact-checked by Britannica editors."
    used_for: [identity, basics, contribution, childhood, institutions, collaborators, review]
  - id: S2
    type: tertiary
    kind: encyclopedia
    author: "J. J. O'Connor and E. F. Robertson"
    year: 1997
    citation: "O'Connor, J. J., and E. F. Robertson. \"James Clerk Maxwell.\" MacTutor History of Mathematics Archive, University of St Andrews, last update November 1997. https://mathshistory.st-andrews.ac.uk/Biographies/Maxwell/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Maxwell/"
    accessed: 2026-10-02
    reliability_note: "University reference archive; signed; draws on Campbell and Garnett and on Tait's obituary, which it quotes."
    used_for: [basics, contribution, childhood, institutions, collaborators]
  - id: S3
    type: secondary
    kind: "scholarly book"
    author: "Lewis Campbell and William Garnett"
    year: 1882
    citation: "Campbell, Lewis, and William Garnett. The Life of James Clerk Maxwell, with a Selection from His Correspondence and Occasional Writings and a Sketch of His Contributions to Science. London: Macmillan, 1882. Project Gutenberg eBook 79044 (2026), https://www.gutenberg.org/ebooks/79044, transcribed from the Internet Archive scan https://archive.org/details/lifeofjamesclerk00camprich."
    url: "https://www.gutenberg.org/ebooks/79044"
    accessed: 2026-10-02
    reliability_note: "Biography by his school friend Campbell (Part I) and his Cavendish demonstrator Garnett (Part II), published three years after his death; prints letters and essays in full. Page numbers are the 1882 edition's, from the page markers in the Gutenberg text. Project Gutenberg is an unofficial web copy, so under CODING_GUIDE §7 it cannot by itself support certainty 1.0. The quoted texts were checked against the library scan S13, so fields that rest on S4–S7 or S9 at 1.0 also cite S13. Gutenberg moves footnotes to the end of the chapter, so its page markers do not give a footnote's printed page. Friendly to its subject; treat interpretation as the authors'."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, institutions, collaborators]
  - id: S4
    type: primary
    kind: letter
    author: "James Clerk Maxwell"
    year: 1852
    citation: "Maxwell, James Clerk. Letter to Lewis Campbell, 8 King's Parade, Cambridge, 7 March 1852. Printed in Campbell and Garnett 1882 (S3), pp. 178–180."
    url: "https://www.gutenberg.org/cache/epub/79044/pg79044-images.html"
    accessed: 2026-10-02
    reliability_note: "Printed by the addressee himself. Not checked against the manuscript."
    used_for: [worldview, lane_b, collaborators]
  - id: S5
    type: primary
    kind: letter
    author: "James Clerk Maxwell"
    year: 1876
    citation: "Maxwell, James Clerk. Letter to C. J. Ellicott, Bishop of Gloucester and Bristol, 11 Scroope Terrace, Cambridge, November 1876, replying to Ellicott's letter of 21 November 1876. Both printed in Campbell and Garnett 1882 (S3), pp. 392–395."
    url: "https://www.gutenberg.org/cache/epub/79044/pg79044-images.html"
    accessed: 2026-10-02
    reliability_note: "Printed in full with the bishop's letters. Not checked against the manuscript."
    used_for: [worldview, timing, collaborators]
  - id: S6
    type: primary
    kind: letter
    author: "James Clerk Maxwell"
    year: 1875
    citation: "Maxwell, James Clerk. Rough draft of a reply to the Secretary of the Victoria Institute, declining the invitation of March 1875. Printed in Campbell and Garnett 1882 (S3), pp. 404–405 ('all that has been found of a rough draft')."
    url: "https://www.gutenberg.org/cache/epub/79044/pg79044-images.html"
    accessed: 2026-10-02
    reliability_note: "Incomplete draft; whether a reply was sent is not stated. Printed by his biographers."
    used_for: [worldview]
  - id: S7
    type: primary
    kind: "diary or notebook"
    author: "James Clerk Maxwell"
    citation: "Maxwell, James Clerk. Two undated prayers 'found amongst his papers'. Printed in Campbell and Garnett 1882 (S3), p. 323, footnote 1."
    url: "https://www.gutenberg.org/cache/epub/79044/pg79044-images.html"
    accessed: 2026-10-02
    reliability_note: "Private papers; undated; printed by his biographers without a date or occasion."
    used_for: [worldview]
  - id: S8
    type: primary
    kind: "published work by the subject"
    author: "James Clerk Maxwell"
    year: 1873
    citation: "Maxwell, James Clerk. \"Molecules.\" Lecture delivered before the British Association at Bradford, 1873. Printed in Nature, vol. 8 (1873). Reprinted in The Scientific Papers of James Clerk Maxwell, ed. W. D. Niven, vol. 2, pp. 361–378. Cambridge: Cambridge University Press, 1890. Scan and OCR: https://archive.org/details/scientificpapers02maxwuoft."
    url: "https://archive.org/details/scientificpapers02maxwuoft"
    accessed: 2026-10-02
    reliability_note: "Public lecture, printed in his lifetime. Read in the OCR text of the 1890 edition; quotations limited to passages where the OCR is clean. The Nature volume is from the edition's source note; Nature page numbers and the exact date of the lecture were not checked."
    used_for: [basics, contribution, worldview, timing, lane_b]
  - id: S9
    type: primary
    kind: "published work by the subject"
    author: "James Clerk Maxwell"
    year: 1873
    citation: "Maxwell, James Clerk. \"Does the Progress of Physical Science Tend to Give Any Advantage to the Opinion of Necessity (or Determinism) over That of the Contingency of Events and the Freedom of the Will?\" Essay dated 11 February 1873, read to the Eranus club, Cambridge. Printed in Campbell and Garnett 1882 (S3), pp. 434–444."
    url: "https://www.gutenberg.org/cache/epub/79044/pg79044-images.html"
    accessed: 2026-10-02
    reliability_note: "Written for a private club of senior colleagues; published only after his death. Dated by Maxwell himself (S3, p. 434)."
    used_for: [worldview]
  - id: S10
    type: primary
    kind: "published work by the subject"
    author: "James Clerk Maxwell"
    year: 1856
    citation: "Maxwell, James Clerk. \"Are There Real Analogies in Nature?\" Essay, February 1856. Printed in Campbell and Garnett 1882 (S3), pp. 235–244."
    url: "https://www.gutenberg.org/cache/epub/79044/pg79044-images.html"
    accessed: 2026-10-02
    reliability_note: "Essay read to a Cambridge discussion society; printed entire by his biographers, who call it 'a serious exposition of Maxwell's deliberate views on philosophical questions'."
    used_for: [timing]
  - id: S11
    type: secondary
    kind: other
    author: "Ian Hutchinson"
    year: 2006
    citation: "Hutchinson, Ian. \"James Clerk Maxwell and the Christian Proposition.\" MIT IAP Seminar 'The Faith of Great Scientists', January 1998, revised 2006. http://silas.psfc.mit.edu/Maxwell/."
    url: "http://silas.psfc.mit.edu/Maxwell/"
    accessed: 2026-10-02
    reliability_note: "Seminar paper by an MIT professor of nuclear science, written for a Christian faculty seminar; argues that faith and science were joined in Maxwell. Draws mostly on Campbell and Garnett. Used for facts only."
    used_for: [childhood, worldview, heritage]
  - id: S12
    type: tertiary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. v8 roster, data/roster/roster.csv, built by scripts/rebuild_roster.py from the five model lists."
    used_for: [review]
  - id: S13
    type: secondary
    kind: "scholarly book"
    author: "Lewis Campbell and William Garnett"
    year: 1882
    citation: "Campbell, Lewis, and William Garnett. The Life of James Clerk Maxwell, with a Selection from His Correspondence and Occasional Writings and a Sketch of His Contributions to Science. London: Macmillan, 1882. University of Toronto (Gerstein) library copy, Internet Archive scan, https://archive.org/details/lifeofjamesclerk00campuoft."
    url: "https://archive.org/details/lifeofjamesclerk00campuoft"
    accessed: 2026-10-02
    reliability_note: "Library scan of the 1882 edition that S3 transcribes; a different copy from the one Gutenberg used. Used to check the wording of the letters, essays and prayers printed there (S4–S7, S9) wherever a quotation or a certainty-1.0 field rests on them. All seven quotations were found word for word in the scan's OCR text, except one word checked on the page image (p. 394: the print reads 'a most conjectural', where S3 has 'almost'). The prayers are in a footnote on p. 323; S3's p. 347 was the page where Gutenberg placed the chapter's footnotes."
    used_for: [worldview, collaborators]
---

# James Clerk Maxwell

> Status: draft — unreviewed. Worldview coded CHRIST at 0.7; all five LIO axes scored (E_scope at 0.5); mid_basin true under the P4 test. A few facts are TODO.

## Summary

James Clerk Maxwell (1831–1879) was a Scottish physicist. He held chairs at Aberdeen, London and Cambridge, where he was the first Cavendish Professor [S1, Early life, Later life; S2]. His lasting work includes the electromagnetic field theory that showed light to be an electromagnetic wave, the statistical law of molecular speeds in a gas, and the three-colour method of colour photography [S1, Later life; S3, pp. 517, 550, 561]. He was a practising Presbyterian and an elder of his parish kirk [S3, p. 371]. In a public lecture of 1873 he argued that molecules must have been created and that science stops at that point [S8, pp. 376–377].

## Life and work

He was born at 14 India Street, Edinburgh, and grew up at Glenlair, the family estate in Kirkcudbrightshire [S3, p. 2; S2]. His mother died in 1839 [S1, Early life]. He went to the Edinburgh Academy from 1841, the University of Edinburgh from 1847, and Cambridge from 1850, where he was Second Wrangler in 1854 and shared the Smith's Prize with Routh [S1, Early life; S2; S3, p. 176].

He was professor at Marischal College, Aberdeen (1856–1860), and at King's College London (1860–1865) [S1; S2]. He then lived at Glenlair, where he worked on the Treatise on Electricity and Magnetism (published 1873). In 1871 he became the first Cavendish Professor at Cambridge [S1, Later life; S2]. He died in Cambridge on 5 November 1879 and was buried at Parton [S1, Later life].

## Contribution and impact

- 1855–56: "On Faraday's Lines of Force" [S3, p. 517].
- 1855–61: colour vision experiments and the three-colour photograph of a tartan ribbon (1861); Rumford Medal 1860 [S1, Later life; S3, p. 482].
- 1857: Adams Prize essay showing Saturn's rings must be made of separate masses [S1, Later life; S2].
- 1859 on: kinetic theory of gases and the velocity distribution [S3, p. 561; S1, Later life].
- 1864: "A Dynamical Theory of the Electro-magnetic Field", with light as an electromagnetic wave [S3, p. 550; S1, Later life].
- Also: Maxwell relations, Maxwell's demon, and the theory of governors [S1, Later life].

Einstein in 1931 called the change in physics brought by Maxwell's work the most profound and fruitful since Newton [S1, opening paragraph]. He designed the Cavendish Laboratory, opened in 1874 [S2].

## Childhood and education

His father was a lawyer and landowner and an elder of the Church of Scotland at Parton. His mother was an Episcopalian [S3, pp. 12, 26; S11]. She taught him at home until 1839 and encouraged him to "look up through Nature to Nature's God" [S3, p. 32]. He is said to have known Psalm 119 by heart at eight [S3, p. 32]. In Edinburgh he went to a Presbyterian church in the morning and an Episcopal chapel in the afternoon, and learned both catechisms [S3, pp. 55–56].

At the Edinburgh Academy he learned Euclid. At 14 he wrote his first paper, on oval curves, which Forbes communicated to the Royal Society of Edinburgh. Tait, his schoolfellow, kept his school manuscripts and said they were "drawn up in strict geometrical form, and divided into consecutive propositions" [S3, p. 87]. At 16 he studied mathematics, natural philosophy and logic at Edinburgh [S2].

## Adult working worldview

His own letters show a Bible-centred Christian faith from his student years. In 1852 he wrote to Campbell that "Nothing is to be holy ground consecrated to Stationary Faith" and that Christianity is "the only scheme or form of belief" with no ground kept off-limits to inquiry [S4, pp. 178–179]. After an illness in 1853 at the Taylers' house his faith deepened [S3, p. 170]. He became an elder at Parton and endowed the church at Corsock [S3, p. 371].

On science and faith he kept two things apart. He would not let scripture be tied to a scientific hypothesis, since hypotheses change faster than interpretations [S5, p. 394]. He declined to join the Victoria Institute, saying that each man's attempts to harmonise science with Christianity matter only to himself, and only for a time [S6, pp. 404–405]. In public, though, he drew a theistic conclusion from physics: molecules are identical everywhere, so they have "the essential character of a manufactured article" and must have been created [S8, p. 376].

Coding: CHRIST at 0.7. A_locus 0 at 1.0 and B_cause 3 (for his physics) at 0.7, from the 1873 lecture, so mid_basin is true at 0.7 under P4. D_authority 2 at 0.7; C_ledger 1 at 0.5. E_scope 3 at 0.5, scored on the world's order (decision P7): the same molecular laws in Sirius and on earth [S8, p. 376], and human will acting within law [S9, p. 443]. No text read addresses favour for a group in events.

## Heritage (context only)

Scottish, of the Clerks of Penicuik, with a Presbyterian father and an Episcopalian mother [S3, pp. 2, 12, 26]. Heritage is recorded for context only. It is not a worldview code.

## Timing

His first lasting work was read in December 1855, at 24 [S3, p. 517]. The earliest dated lawful-order statement found is in a February 1856 essay [S10, p. 240], so it is coded "during major work". His geometric training is documented from age 14 [S3, p. 87]. He was a practising Christian throughout [S3, p. 371].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Maxwell shows the geometric form early (Euclid and propositional school papers at 14) without the circle: God is a creator distinct from nature, and he rejects the pantheist's God [S3, p. 87; S4, p. 179; S8, p. 377]. The v7.1 papers would be hurt if Maxwell looked like "late professional lawfulness only". In this record the form is documented before any professional training.

## Open questions

- E_scope (3 at 0.5): read Theerman 1986, the 1884 Life and Stanley 2015 for any expectation of favour for believers in events.
- Find the Tayler letter on the London Baptist chapel in the 1884 edition and quote it from the source.
- Start year of his eldership at Parton; baptism record.
- Any text on providence, answered prayer or miracle in nature (bears on CLTHEI).

## Research log

- 2026-10-02: Read Britannica (S1: main, Later life, Researcher's Note), MacTutor (S2), and the Gutenberg text of Campbell and Garnett 1882 (S3), including the letters, essays and prayers printed there (S4–S7, S9, S10). Read the 1873 "Molecules" lecture in the OCR of the 1890 Scientific Papers (S8) and Hutchinson's seminar paper (S11). Wikipedia not used. Every quotation was checked word for word against the fetched text with a script (verify_quotes.py) before commit. Theerman 1986, the Oxford DNB and Harman's edition of the Scientific Letters and Papers were not read (paywalled or not online). E_scope and baptism left TODO.
- 2026-10-02 (P7): E_scope scored on the world's order (3 at 0.5) from the texts already cited (S7, S8, S9); no new sources or quotations.
