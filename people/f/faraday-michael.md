---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 11
  review_status: "example — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, repo setup)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-01
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-01, by: "Grok Bot", summary: "Worked example created to show the record structure. Only well-sourced fields filled; everything else TODO. Not reviewed."}
    - {date: 2026-10-01, by: "Grok Bot", summary: "1844 exclusion: reason, length and restoration added from Cantor 2020 (S8), Brooke 1991 (S9) and Gladstone 1872/1873 (S10, S11); second eldership after 1860 added. Exact readmission date still a gap."}
    - {date: 2026-10-01, by: "Grok Bot", summary: "Schema 1.1. Era and region notes now cite the decided buckets (P2) and the region table (P3). mid_basin note: the P4 test exists; value stays TODO until A_locus and B_cause are scored."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "All five LIO axes and mid_basin scored from the sources already cited (no new sources): A 0, B 3 (his physics), D 1 at 0.7; C 1 and E 1 at 0.5. mid_basin true at 0.7. Five statements added from Gladstone (S10) and Cantor (S8), checked word for word. Timing fields for LIO-type views filled; changes_over_life changed from an empty list to UNKNOWN. Primary system still TODO. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Primary system coded CHRIST at 0.7 (consistent private letters) from his own writings and the sources already cited; CLTHEI and CLASS_THEISM rejected with reasons. secondary_system UNKNOWN (no second system). B_cause and mid_basin rechecked under decision P6 (B on his account of nature): unchanged, B 3 and mid_basin true at 0.7. No new sources. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit fixes: 1821 membership reworded from both sources (sought membership within days of the wedding, Russell; formal profession of faith a month after it, Gladstone p. 91). D_authority 1 -> 2 at 0.7 (two domains, each with its own authority, as for Maxwell and Newton). Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit, run 2: E_scope how_known now names the domain scored (salvation and church membership) and points to open item P7. Score and certainty unchanged (1 at 0.5). Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "P7 decided by Jason (2026-10-02, option 1): E_scope is scored on the world's order. E_scope 1 -> 3 at 0.5, from his account of nature (God's 'definite laws' for all matter; no favour in events in his own words; biblical miracles accepted). The sect and salvation reading moved to the C_ledger rationale (C unchanged). Statement axis tags updated. P7 interim note removed. No new sources. mid_basin unchanged. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit runs 2–3: (#2) the 'perfect trust and submission' quotation is on Gladstone 2nd ed. p. 36, not p. 37; every S10 p. 37 locator corrected (checked against the archive.org scan). (#10) self_described_science_religion_relation rested on one private letter, which CODING_GUIDE §3 says is not 'consistent private letters'. The 1854 public discourse already in the record (S10, pp. 99–100) says the same thing, so it is now cited, the value says 'a private letter and a public lecture' instead of 'conversation and correspondence', and 0.7 stands. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Schema 1.1 → 1.2 (decision P8 adds basis recorded_interview and statement kind 'recorded interview'); no content change."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Stage 3 lens-audit rulings applied to the batch's other records (OPEN_DECISIONS P14–P28, v8's picks, 2026-10-02). Schema 1.2 → 1.3. One reliable source caps a fact at 0.7; derived fields take the lowest certainty of their inputs; kind lists (P21: research institute, school stage and run_by, scholarly edition). Full before → after list: reports/stage3_rulings_changes.csv. Not reviewed."}

identity:
  id: faraday-michael
  display_name: "Michael Faraday"
  roster:
    canonical_name: "Michael Faraday"
    rank: 58
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: physics
    field_bucket: physics
  full_name: {value: "Michael Faraday", certainty: 1.0, cites: [{source: S1, locator: "opening sentence"}, {source: S2, locator: "Biography"}], how_known: "Both sources use this name; no other given names reported."}
  native_name: {value: "Michael Faraday", certainty: 0.7, cites: [{source: S1, locator: "opening sentence"}], how_known: "English was his language, so the native form is the roster name."}
  aliases:
    - {name: "Faraday-Michael", kind: "roster alias"}
    - {name: "Michael-Faraday", kind: "roster alias"}

basics:
  birth:
    date:
      value: "1791-09-22"
      certainty: 1.0
      cites: [{source: S1, locator: "opening sentence and Quick Facts"}, {source: S4, locator: "letter text: 'next Sabbath day (the 22nd) I shall complete my 70th year'"}]
      how_known: "Encyclopedia date, matched by Faraday's own statement in a letter of 19 Sept 1861."
      alternatives:
        - {value: "1791-09-21", cites: [{source: S5, locator: "p. 4, gravestone transcription"}], note: "Russell's transcription of the gravestone reads 'Born 21 September 1791'. Not checked against the stone or a photograph."}
    place:
      value: "Newington Butts, Surrey, England"
      modern_name: "Southwark, South London"
      polity_then: "Kingdom of Great Britain"
      certainty: 1.0
      cites: [{source: S1, locator: "opening sentence; Early life"}, {source: S2, locator: "Biography"}]
      how_known: "S1 says Newington, Surrey, 'now a part of South London'; S2 says Newington Butts, Southwark."
  death:
    date: {value: "1867-08-25", certainty: 1.0, cites: [{source: S1, locator: "opening sentence"}, {source: S5, locator: "p. 4"}], how_known: "Encyclopedia and a historian's paper agree."}
    place:
      value: "His house at Hampton Court, Surrey, England"
      modern_name: "Hampton Court, London Borough of Richmond upon Thames"
      certainty: 1.0
      cites: [{source: S1, locator: "opening sentence; Later life"}, {source: S2, locator: "Biography: 'a Grace and Favour House at Hampton Court where he died'"}]
      how_known: "Two independent summaries agree."
  first_lasting_contribution_year: {value: 1821, certainty: 1.0, cites: [{source: S1, locator: "Early life (electromagnetic rotation, 'the first electric motor')"}, {source: S2, locator: "Biography: 'electro–magnetic rotations (1821)'"}], how_known: "Both list the 1821 electromagnetic rotations as his first major discovery in electricity."}
  era_bucket: {value: "1750 to 1849", certainty: 1.0, cites: [{source: S1, locator: "Early life"}], how_known: "Derived from first_lasting_contribution_year (1821) under the era buckets (decision P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 1.0, cites: [{source: S1, locator: "opening sentence"}], how_known: "Born in England; the United Kingdom is Northern Europe in data/reference/regions.csv (UN M49 sub-region, decision P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.7, cites: [{source: S2, locator: "Ri positions"}], how_known: "His whole working life was at the Royal Institution in London."}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S2, locator: "Biography: 'the son of a Sandemanian blacksmith'"}, {source: S1, locator: "throughout ('he', 'his')"}], how_known: "As the sources record it."}
  languages_of_work: {value: [English], certainty: 0.7, cites: [{source: S2, locator: "Publications"}], how_known: "All his published books and paper collections are in English."}
  occupations:
    value: ["bookbinder (apprentice)", "chemist", "physicist", "public lecturer", "scientific adviser"]
    certainty: 1.0
    cites: [{source: S2, locator: "Biography and Ri positions"}, {source: S1, locator: "opening sentence"}]
    how_known: "From the Royal Institution's own list of his posts and the encyclopedia summary."

contribution:
  fields: {value: [chemistry, physics, electromagnetism, electrochemistry], certainty: 0.7, cites: [{source: S1, locator: "opening paragraph"}], how_known: "Encyclopedia summary."}
  lasting_original_contributions:
    - {value: "Electromagnetic rotation: the first electric motor", year: 1821, kind: invention, lasting: "the principle of the electric motor", certainty: 1.0, cites: [{source: S1, locator: "Early life"}, {source: S2, locator: "Biography"}], how_known: "Two summaries agree."}
    - {value: "Isolated and described benzene", year: 1825, kind: discovery, certainty: 1.0, cites: [{source: S1, locator: "Early life"}, {source: S2, locator: "Biography"}], how_known: "Two summaries agree."}
    - {value: "Electromagnetic induction (iron-ring experiment of 29 August 1831), then the first dynamo", year: 1831, kind: discovery, lasting: "generators and transformers rest on induction", certainty: 1.0, cites: [{source: S1, locator: "Early life (end)"}, {source: S2, locator: "Biography"}], how_known: "Two summaries agree; S1 gives the date of the experiment."}
    - {value: "Two laws of electrochemistry (electrolysis), and the words electrode, cathode, ion", year: "early 1830s", kind: "law or principle", certainty: 1.0, cites: [{source: S1, locator: "Theory of electrochemistry"}, {source: S2, locator: "Biography"}], how_known: "Two summaries agree."}
    - {value: "Specific inductive capacity of insulating materials", year: "by 1839", kind: discovery, certainty: 0.7, cites: [{source: S1, locator: "Theory of electrochemistry"}], how_known: "One encyclopedia source."}
    - {value: "Magneto-optical effect (rotation of polarized light by a magnetic field) and diamagnetism", year: 1845, kind: discovery, certainty: 1.0, cites: [{source: S1, locator: "Later life"}, {source: S2, locator: "Biography"}], how_known: "Two summaries agree."}
    - {value: "Field conception of electric and magnetic force: space as a medium carrying the strains of force", year: "by 1850", kind: theory, lasting: "Maxwell built his field equations on it", certainty: 1.0, cites: [{source: S1, locator: "Later life"}, {source: S2, locator: "Biography: 'thereafter formulating the field theory of electro-magnetism'"}], how_known: "Two summaries agree."}
  evidence_of_impact:
    - {value: "Maxwell took the basic ideas for his mathematical field theory from Faraday, and said so", kind: "assessment by a later major figure", certainty: 0.7, cites: [{source: S1, locator: "Later life"}], how_known: "Reported by the encyclopedia article; Maxwell's own words not checked here."}
    - {value: "Effects and laws carry his name: Faraday effect, Faraday's law of induction, Faraday's laws of electrolysis", kind: "named after them", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts: Subjects of study"}], how_known: "Listed by the encyclopedia."}
    - {value: "Founded the Royal Institution's Friday Evening Discourses and Christmas Lectures in the mid-1820s", kind: "institutional or technological lineage", certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "The institution's own record."}
  major_works:
    - {value: "Chemical Manipulation, Being Instructions to Students in Chemistry", year: 1827, kind: book, certainty: 0.7, cites: [{source: S2, locator: "Publications"}], how_known: "Institution's bibliography; his only book."}
    - {value: "Experimental Researches in Electricity, vols I–III", year: "1837, 1844, 1855", kind: "paper or paper series", certainty: 0.7, cites: [{source: S2, locator: "Publications"}], how_known: "Institution's bibliography."}
    - {value: "Experimental Researches in Chemistry and Physics", year: 1859, kind: "paper or paper series", certainty: 0.7, cites: [{source: S2, locator: "Publications"}], how_known: "Institution's bibliography."}
    - {value: "A Course of Six Lectures on the Chemical History of a Candle (ed. W. Crookes)", year: 1861, kind: "lecture series", certainty: 0.7, cites: [{source: S2, locator: "Publications"}], how_known: "Institution's bibliography."}
  honours:
    - {value: "Copley Medal", year: "1832, 1838", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts: Awards and honors"}], how_known: "Encyclopedia fact box."}
    - {value: "Civil List pension", year: 1836, certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "Institution's record."}
    - {value: "Twice offered the Presidency of the Royal Society; declined both times", certainty: 1.0, cites: [{source: S2, locator: "Biography"}, {source: S5, locator: "p. 4"}], how_known: "Two sources agree."}
    - {value: "Use of a Grace and Favour house at Hampton Court from the Queen", year: 1858, certainty: 1.0, cites: [{source: S2, locator: "Biography"}, {source: S1, locator: "Later life"}], how_known: "Two sources agree; S2 gives the year."}
  definition_fit: {value: "clearly meets", rationale: "Several discoveries still in use (induction, electrolysis laws, field concept), named effects, and Maxwell's acknowledged debt.", certainty: 0.7, cites: [{source: S1, locator: "opening paragraph; Later life"}], how_known: "Lane A definition (lasting original impact on documented criteria) applied to the contributions listed above."}

childhood:
  family_religion: {value: "Sandemanian (Glasite) Christian. The family had belonged to this small dissenting sect since his grandfather's generation.", certainty: 1.0, cites: [{source: S1, locator: "Early life"}, {source: S2, locator: "Biography: 'son of a Sandemanian blacksmith'"}, {source: S5, locator: "p. 1, 'The roots of Faraday's beliefs'"}], how_known: "Three sources agree on a Sandemanian family; S5 traces it to his grandfather Robert Faraday."}
  family_religious_practice: {value: "Attended the Sandemanian chapel in Paul's Alley, City of London, as a child (Russell calls it his 'childhood habit').", certainty: 0.7, cites: [{source: S5, locator: "p. 1"}], how_known: "One historian's summary; detail on frequency and form not given."}
  parents_and_household:
    - {value: "Father, James Faraday, a blacksmith who moved to London from the north of England in 1791", name: "James Faraday", role: father, certainty: 1.0, cites: [{source: S1, locator: "Early life"}, {source: S2, locator: "Biography"}, {source: S5, locator: "p. 1"}], how_known: "Three sources agree."}
    - {value: "Mother, Margaret; Michael was named after her father", name: "Margaret Faraday", role: mother, certainty: 0.7, cites: [{source: S5, locator: "p. 1"}], how_known: "One source gives her name and the naming."}
    - {value: "One of four children; the third child", role: sibling position, certainty: 0.7, cites: [{source: S1, locator: "Early life: 'one of four children'"}, {source: S5, locator: "p. 1: 'their third child'"}], how_known: "S1 gives four children; only S5 gives birth order."}
  household_circumstances: {value: "Poor: the father was often ill and unable to work steadily, and the children were often short of food.", certainty: 1.0, cites: [{source: S1, locator: "Early life"}, {source: S5, locator: "p. 1: 'early years of penury'"}], how_known: "Two sources agree."}
  schooling:
    - {value: "Only the rudiments: reading, writing and ciphering, learned in a church Sunday school", stage: "elementary school", certainty: 0.7, cites: [{source: S1, locator: "Early life"}], how_known: "One encyclopedia source gives the content; S5 p. 1 confirms 'limited schooling' without detail.", run_by: "religious body"}
    - {value: "Apprenticed to the bookbinder and bookseller George Riebau", stage: apprenticeship, institution: "George Riebau, bookbinder", years: "1805–1812", ages: "14–21", certainty: 1.0, cites: [{source: S2, locator: "Biography"}, {source: S1, locator: "Early life: 'at the age of 14'"}], how_known: "Two sources agree."}
    - {value: "Educated himself during the apprenticeship by reading books brought in for rebinding", stage: self-directed, years: "1805–1812", certainty: 1.0, cites: [{source: S1, locator: "Early life"}, {source: S5, locator: "p. 1: 'attempts at self-education'"}], how_known: "Two sources agree."}
  early_mathematics: {value: "arithmetic only", description: "'ciphering' at Sunday school; no consulted source reports geometry or algebra teaching in childhood", certainty: 0.7, cites: [{source: S1, locator: "Early life"}], how_known: "Inferred from the only description of his schooling. Later limits on his mathematics are reported elsewhere but not checked here."}
  early_geometric_style_reasoning: {value: TODO, note: "Wikipedia says he read Isaac Watts's The Improvement of the Mind during his apprenticeship. Check that in Cantor 1991 or James 2010 before entering it, and say whether it involved definition-to-consequence practice."}
  early_science_exposure:
    - {value: "Read the article on electricity in the third edition of the Encyclopaedia Britannica", year: "1805–1812", age: "14–21", certainty: 0.7, cites: [{source: S1, locator: "Early life"}], how_known: "One source."}
    - {value: "Built a crude electrostatic generator from old bottles and lumber, and a weak voltaic pile for electrochemistry experiments", year: "1805–1812", age: "14–21", certainty: 0.7, cites: [{source: S1, locator: "Early life"}], how_known: "One source."}
    - {value: "Attended Humphry Davy's chemistry lectures at the Royal Institution, took notes, and sent Davy a bound copy with a request for work", year: 1812, age: "about 20–21", certainty: 0.7, cites: [{source: S1, locator: "Early life"}, {source: S2, locator: "Biography (apprenticeship ended 1812)"}], how_known: "S1 describes the lectures as happening during the apprenticeship, which S2 dates as ending in 1812; the year is therefore inferred."}
  key_early_reading:
    - {value: "Encyclopaedia Britannica, 3rd edition, article 'Electricity'", certainty: 0.7, cites: [{source: S1, locator: "Early life"}], how_known: "One source."}
  childhood_mentors:
    - {value: "George Riebau, the master bookbinder he was apprenticed to, and who first employed him to deliver newspapers", name: "George Riebau", years: "1805–1812", certainty: 0.7, cites: [{source: S2, locator: "Biography"}, {source: S1, locator: "Early life"}], how_known: "S2 names Riebau; S1 says he first delivered newspapers for the book dealer he was later apprenticed to. That this is the same man is read across the two sources."}
  languages_in_childhood: {value: TODO}
  notable_events:
    - {value: "Delivered newspapers for a book dealer and bookbinder before his apprenticeship", age: "before 14", certainty: 0.7, cites: [{source: S1, locator: "Early life"}], how_known: "One source."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1813–1865", certainty: 1.0, cites: [{source: S2, locator: "Ri positions"}, {source: S5, locator: "p. 4: stepped down as Superintendent in 1865"}], how_known: "From his appointment at the Royal Institution in 1813 to his last posts in 1865."}
  nominal_affiliations:
    - {value: "Joined the Sandemanian church in 1821: he sought membership within days of his marriage (12 June 1821) and made his formal profession of faith about a month after it", year: 1821, role: member, certainty: 0.7, cites: [{source: S5, locator: "p. 2"}, {source: S10, locator: "p. 91"}, {source: S8, locator: "section 'Primitive Christianity'"}], how_known: "Russell: 'Within days of the wedding Faraday sought membership of the Sandemanian church' (S5, p. 2). Gladstone, who knew him: 'he did not make any formal profession of his faith till a month after his marriage' (S10, p. 91). Cantor confirms the confession of faith in 1821 (S8). The sources agree on the year; the exact day of the profession is not given, so 0.7."}
    - {value: "Deacon", year: 1832, role: deacon, certainty: 0.7, cites: [{source: S5, locator: "p. 2"}], how_known: "One source."}
    - {value: "Elder; he preached ('exhortations') at Sandemanian meetings", year: 1840, role: elder, certainty: 0.7, cites: [{source: S5, locator: "p. 2"}], how_known: "One source."}
    - {value: "Excluded from the London Sandemanian church in 1844, which also ended his first term as elder", year: 1844, role: elder, certainty: 1.0, cites: [{source: S10, locator: "p. 36"}, {source: S8, locator: "section 'Primitive Christianity', para. 3"}, {source: S6, locator: "article title"}], how_known: "Gladstone, who knew him, says the first eldership ('between 1840 and 1844') 'came to a close through his separation both from his office and from the Church itself'. Cantor (S6 title, S8) agrees. Independent sources, no dispute, so 1.0."}
    - {value: "Restored to membership after a few weeks, in the spring of 1844", year: 1844, certainty: 0.7, cites: [{source: S8, locator: "section 'Primitive Christianity', para. 3"}, {source: S10, locator: "p. 36"}], how_known: "Cantor gives the length and season: 'for a few weeks in the spring of 1844'. Gladstone confirms the restoration ('was after a while restored to the rights of membership') but gives no date. The timing rests on one historian, so 0.7. The exact day of readmission is not in any source read (see open_questions)."}
    - {value: "Reason for the 1844 exclusion: an internal dispute over church discipline", year: 1844, certainty: 0.7, cites: [{source: S8, locator: "section 'Primitive Christianity', para. 3"}, {source: S9, locator: "para. 7"}], how_known: "Cantor writes that they excluded him 'owing to an internal dispute over church discipline' (S8). Brooke's review of Cantor's 1991 book (S9) reports that the Queen story 'is called into question by Cantor’s evidence'. S9 depends on Cantor, so this is one line of evidence: 0.7. The BJHS article itself (S6) was not read, so what the dispute was about is not recorded here.", alternatives: [{value: "He missed a Sunday love feast because he was the Queen's guest, and defended obeying her", cites: [{source: S11, locator: "p. 35"}], note: "Gladstone's first edition (1872) gives this as what the reason 'is said to have been': 'it appeared not only that he had been the guest of the Queen, but that he was ready to justify his own conduct in obeying her commands'. His second edition drops it and says the reason 'is unknown except to the parties immediately concerned' (S10, p. 36). Not preferred."}]}
    - {value: "Elder again after 1860", year: "after 1860", role: elder, certainty: 0.7, cites: [{source: S10, locator: "p. 36"}], how_known: "Gladstone gives his periods of eldership as 'between 1840 and 1844, or after 1860', and says he was restored 'eventually to the office of elder'. One contemporary source; no exact start date."}
    - {value: "Resigned his eldership", year: 1864, certainty: 0.7, cites: [{source: S5, locator: "p. 4"}], how_known: "One source."}
  self_described_science_religion_relation:
    value: "In a private letter and in a public lecture he kept religion and natural philosophy apart ('two distinct things'; 'an absolute distinction between religious and ordinary belief'), while holding that the works of God cannot contradict the higher things of faith."
    certainty: 0.7
    cites: [{source: S3, locator: "final paragraph"}, {source: S10, locator: "pp. 99–100 ('Observations on Mental Education', 1854)"}]
    how_known: "Two consistent documents in his own words: the 1844 letter to Lovelace (S3) and the 1854 Royal Institution discourse, which claims 'an absolute distinction between religious and ordinary belief' and says he has 'never seen anything incompatible' between the two (quoted by Gladstone, S10). A quotation in a secondary source cannot support 1.0, so 0.7. How far the separation went in his scientific thinking is disputed by historians (see alternatives)."
    alternatives:
      - {value: "Convergent reading: his science and faith interacted (vocation, unity of forces, point-centre atoms and fields).", cites: [{source: S5, locator: "pp. 2–3"}], note: "Russell's argument against taking the 'two distinct things' sentence as the whole story."}
  primary_system:
    value: CHRIST
    basis: consistent_private_letters
    certainty: 0.7
    cites: [{source: S3, locator: "final paragraph"}, {source: S4, locator: "first paragraph"}, {source: S10, locator: "pp. 36, 58, 99–100"}, {source: S5, locator: "pp. 1–2"}, {source: S9, locator: "para. on natural theology"}]
    how_known: "His Christian belief is in his own words in private letters (S3, 1844; S4, 1861; the Comte de Paris letter through Gladstone, S10, p. 58), consistent with his public 1854 lecture as quoted by Gladstone (S10, pp. 99–100) and with his profession of faith in 1821 and his offices (S10, p. 91; S5, p. 2). The published lecture was read only as a secondary quotation, which cannot support 1.0, so 0.7."
    rationale: "CHRIST fits 'the religion as practised and confessed' (CODING_GUIDE): his hope is 'founded on the faith that is in Christ' (S3), peace is 'alone in the gift of God', whose 'unspeakable gift in his beloved son' grounds hope (S4), and the truths of the future life are 'received through simple belief of the testimony given' (S10, pp. 99–100). Neither theism split fits better. Not CLASS_THEISM: 'There is no philosophy in my religion' (S3), and he rejected natural theology as 'superfluous and misguided' (S9); no argued simple, immutable God appears. Not CLTHEI: the writing read shows submission, not petition ('perfect trust and submission to God's will', S10, p. 36), and no expected acts of God against the course of nature; in nature God 'governs his material works by definite laws' (S8). CLTHEI's own guidance sends such a case to the host religion. Membership and eldership alone would not code him (CODING_GUIDE); his own writings do. The Sandemanian form is recorded in nominal_affiliations, not as a code."
    alternatives:
      - {value: CLTHEI, cites: [{source: S5, locator: "pp. 1–2"}], note: "Closest alternative. Russell calls the church evangelical and strongly Calvinist, and quotes J. M. Thomas that he accepted 'the literal truth of the Bible' (S5, p. 2), miracles included. Preferred only if his own writing showed petition answered by God or God acting in particular events beyond nature's course; none was found."}
  secondary_system: {value: UNKNOWN, how_known: "No second system; he published in no other system, and he kept religion and natural philosophy as 'two distinct things' (S3) rather than as two systems."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Chosen at 0.7. His own letters profess Christian faith: hope 'founded on the faith that is in Christ' (S3), God's 'unspeakable gift in his beloved son' (S4), and revealed truth 'received through simple belief of the testimony given' (S10, pp. 99–100). Neither theism split fits better.", cites: [{source: S3, locator: "final paragraph"}, {source: S4, locator: "first paragraph"}, {source: S10, locator: "pp. 99–100"}, {source: S5, locator: "p. 2"}]}
    - {code: CLTHEI, reason: "Russell describes the church as evangelical and strongly Calvinist, appealing to biblical authority (p. 1), and quotes J. M. Thomas that Faraday accepted the literal truth of the Bible (p. 2). Rejected: his own writing read shows trust and submission (S10, p. 36), not petition that changes events, and in nature God works by 'definite laws' (S8). CLTHEI's guidance sends a person who accepts scriptural miracles but allows no exceptions in nature to the host religion.", cites: [{source: S5, locator: "pp. 1–2"}, {source: S10, locator: "p. 36"}, {source: S8, locator: "section 'Electric discoveries'"}]}
    - {code: CLASS_THEISM, reason: "Rejected. Nothing consulted shows an Aristotelian-Thomistic or falsafa framework; Russell reads 'no philosophy in my religion' as denying that natural knowledge could lead to God.", cites: [{source: S5, locator: "p. 2, 'Natural theology'"}]}
  lio_axes:
    A_locus:
      value: 0
      basis: consistent_private_letters
      certainty: 0.7
      cites: [{source: S4, locator: "first paragraph"}, {source: S10, locator: "pp. 36, 58"}, {source: S5, locator: "p. 2, 'Romantic idealism'"}]
      how_known: "His own letters (S4 in a scholarly transcription; the Comte de Paris letter through Gladstone's quotation) and two accounts of his worship and beliefs. Consistent private writing, so 0.7."
      rationale: "At the interventionist pole: a transcendent, fully personal God. Peace 'is alone in the gift of God' and his 'unspeakable gift in his beloved son' grounds hope (S4, 1861). He bows 'before Him who is Lord of all' and waits for 'His time and mode of releasing me' (S10, p. 58). His extempore prayers expressed 'perfect trust and submission to God's will' (S10, p. 36). Where unity was applied 'to God and the universe', his faith 'rose up in disbelief' (S5, p. 2), so God is not the world."
    B_cause:
      value: 3
      basis: consistent_private_letters
      certainty: 0.7
      cites: [{source: S8, locator: "section 'Electric discoveries'"}, {source: S9, locator: "paras. on laws of nature and forces"}, {source: S10, locator: "pp. 103, 118"}, {source: S5, locator: "pp. 2–3"}]
      how_known: "His own words through two historians' quotations (S8, S9) and a contemporary biographer (S10), consistent with each other. No direct primary text on the axis was read, so 0.7, not 1.0."
      rationale: "Scored for his physics, as P4 asks. Leans to law. 'the Creator governs his material works by definite laws resulting from the forces impressed on matter' (S8). The beauty of electricity is that it is 'under law' (S9). He spoke of 'the unchangeability of the laws of nature' (S10, p. 103), and as a lecturer did not 'look beyond the natural laws he was describing' (S10, p. 118). He explained table-turning by 'a quasi involuntary muscular action', not a spirit (S8). The stated limited exception: creating or destroying force is 'only within the power of Him', which is why force is conserved (S8, 1857 discourse). So 3, the same as Maxwell's limit at the creation of molecules. Under decision P6 (2026-10-02) B is scored on his account of nature, which for Faraday is his physics, so the score is unchanged. Theology-wide reading: he accepted 'the literal truth of the Bible' (S5, p. 2, quoting J. M. Thomas), with its miracles, which would score lower."
    C_ledger:
      value: 1
      basis: scholarly_reconstruction
      certainty: 0.5
      cites: [{source: S4, locator: "first paragraph"}, {source: S10, locator: "p. 58"}, {source: S9, locator: "para. on Sandeman's doctrine"}]
      how_known: "Coder's reading of his letters and of Brooke's account of Sandemanian teaching. His own words speak of hope and gift, not judgement, so 0.5."
      rationale: "Leans interventionist. The future life is a personal gift and promise of God, not a natural consequence: 'the ground of no doubtful hope' is God's gift in his Son (S4), and he looks to 'the great and precious promises whereby His people are made partakers of the Divine nature' (S10, p. 58). Sandemanian salvation was 'freely available through Christ’s ransom', with 'the imitation of Christ and obedience to his commands' required in return (S9), and the church disciplined its members, as it did him in 1844 (S8). Not 0, because no punishment language appears in his own words read here. Under decision P7 (2026-10-02), the scope of salvation and church membership is recorded here, not on E: he belonged to 'a very small & despised sect of christians' (S3), whose members kept apart from other denominations (S8). This fits a score of 1 and does not change it."
    D_authority:
      value: 2
      basis: consistent_private_letters
      certainty: 0.7
      cites: [{source: S10, locator: "pp. 99–100 ('Observations on Mental Education')"}, {source: S3, locator: "final paragraph"}, {source: S9, locator: "para. on natural theology"}, {source: S5, locator: "p. 2"}]
      how_known: "His own public lecture through Gladstone's quotation, his private letter to Lovelace (scholarly transcription) and two historians, consistent with each other, so 0.7."
      rationale: "Mixed, by domain, as the scale defines 2. Two domains, each with its own authority. For God and the future life, revelation alone: that truth 'cannot be brought to his knowledge by any exertion of his mental powers' and is 'received through simple belief of the testimony given' (S10, pp. 99–100); he refuses to apply his methods 'to the very highest' (S10, p. 100), and knowledge of God came from 'the plain teaching of Scripture', with natural theology 'superfluous and misguided' (S9). For nature, observation and experiment rule, and 'that which is religious & that which is philosophical have ever been two distinct things' (S3); matters like the age of the earth and the Flood are 'studiously avoided' (S5, p. 2). Scripture is never used as evidence in his science, and revelation is not set over observation inside nature, so this is the same two-domain pattern as Maxwell and Newton (both 2). Changed from 1 after the lens audit (2026-10-02). Plausible alternative: 1, if his refusal to apply reason to the highest things is read as revelation outranking reason; so certainty stays at most 0.7 (CODING_GUIDE §3)."
    E_scope:
      value: 3
      basis: scholarly_reconstruction
      certainty: 0.5
      cites: [{source: S8, locator: "section 'Electric discoveries'"}, {source: S10, locator: "pp. 36, 103"}, {source: S5, locator: "p. 2"}]
      how_known: "Coder's reading of his words as quoted by two historians and a contemporary biographer (S8, S10) and of Russell's account (S5). No source addresses the axis directly, so 0.5. Rescored under decision P7 (2026-10-02): before P7 this was 1, scored on the scope of salvation and church membership."
      rationale: "Scored on the world's order (decision P7). Leans LIO. One set of laws for all matter: 'the Creator governs his material works by definite laws resulting from the forces impressed on matter' (S8), and he spoke of 'the unchangeability of the laws of nature' (S10, p. 103). Claimed spirit action among people (table-turning) he put down to 'a quasi involuntary muscular action' (S8), so human events fall under the same rules. No petition for favour and no special acts of God for believers appear in his own words read: his prayers expressed 'perfect trust and submission to God's will' (S10, p. 36). The limited exception: he accepted 'the literal truth of the Bible' (S5, p. 2, quoting J. M. Thomas), with its miracles, some of them done for God's people, though none enters his account of nature. So 3. A reviewer who sets the biblical miracles aside could score 4. The sect ('a very small & despised sect', S3) and the promises to 'His people' (S10, p. 58) used to give 1 here. Under P7 they belong to C (see C_ledger)."
  mid_basin:
    value: true
    certainty: 0.7
    cites: [{source: S4, locator: "first paragraph"}, {source: S10, locator: "pp. 58, 103"}, {source: S8, locator: "section 'Electric discoveries'"}]
    how_known: "P4 test applied to the scores above: A_locus = 0 (≤ 1) at 0.7 and B_cause = 3 (≥ 3) at 0.7, B scored on his account of nature, his physics and chemistry (P4 as amended by P6, 2026-10-02; the result is the same under the old wording). Both certainties are at least 0.7, so true. F = 5, so first-rank is met. This confirms the v7.1 starting label under the study's own test. Certainty 0.7 because the key B evidence is his words quoted by historians, not a primary text read here."
  statements:
    - text: "There is no philosophy in my religion[.] I am of a very small & despised sect of christians known, if known at all, as Sandemanians and our hope is founded on the faith that is in Christ. But though the natural works of God can never by any possibility come in contradiction with the higher things that belong to our future existence, and must with every thing concerning Him ever glorify him still I do not think it at all necessary to tie the study of the natural sciences & religion together and in my intercourse with my fellow creatures that which is religious & that which is philosophical have ever been two distinct things[.]"
      cites: [{source: S3, locator: "final paragraph (from Faraday's own copy, IEE MS SC 3, per the edition's note 4)"}]
      date: "1844-10-24"
      context: "Reply to Ada Lovelace, who had asked about his religion and offered to work through his experiments with him."
      axes: [D_authority, A_locus]
      kind: "private letter"
      verified_against: "primary transcription"
      verified_on: 2026-10-01
    - text: "I am, I hope, very thankful that in the withdrawal of the powers & things of this life,- the good hope is left with me, which makes the contemplation of death a comfort - not a fear. Such peace is alone in the gift of God; and as it is he who gives it, why should we be afraid? His unspeakable gift in his beloved son is the ground of no doubtful hope;- and there is the rest for those who like you & me are drawing near the latter end of our terms here below.-"
      cites: [{source: S4, locator: "first paragraph"}]
      date: "1861-09-19"
      context: "Letter to his friend and fellow physicist Auguste De La Rive, three days before his 70th birthday."
      axes: [C_ledger]
      kind: "private letter"
      verified_against: "primary transcription"
      verified_on: 2026-10-01
    - text: "the Creator governs his material works by definite laws resulting from the forces impressed on matter"
      cites: [{source: S8, locator: "section 'Electric discoveries', para. 2"}]
      context: "Cantor quotes this as Faraday's belief behind his search for the laws linking electricity, magnetism and chemical action. Cantor gives no date or source for the words."
      axes: [B_cause, E_scope]
      kind: other
      verified_against: "secondary quotation"
      verified_on: 2026-10-02
      note: "Short magazine article without notes, by Faraday's main religious biographer. Supports B only together with S9 and S10."
    - text: "I believe that the truth of that future cannot be brought to his knowledge by any exertion of his mental powers, however exalted they may be; that it is made known to him by other teaching than his own, and is received through simple belief of the testimony given."
      cites: [{source: S10, locator: "pp. 99–100"}]
      context: "Opening of his Royal Institution discourse 'Observations on Mental Education', where he limits the range of his remarks to the things of this life."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-02
      note: "Quoted by Gladstone; checked against the Gutenberg text of the 3rd edition and the OCR of the 2nd. The lecture itself (published 1854; reprinted 1859) was not read."
    - text: "I shall be reproached with the weakness of refusing to apply those mental operations which I think good in respect of high things to the very highest. I am content to bear the reproach."
      cites: [{source: S10, locator: "p. 100"}]
      context: "Same discourse, after claiming 'an absolute distinction between religious and ordinary belief'."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-02
      note: "As above."
    - text: "I bow before Him who is Lord of all, and hope to be kept waiting patiently for His time and mode of releasing me according to His Divine Word, and the great and precious promises whereby His people are made partakers of the Divine nature."
      cites: [{source: S10, locator: "p. 58"}]
      context: "Letter to the Comte de Paris in his last years, when 'the dark shadow was creeping over him'."
      axes: [A_locus, C_ledger]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-02
      note: "Quoted by Gladstone, who knew him; undated in the source."
    - text: "when we speak of such things as the conservation of force, the permanency of matter, and the unchangeability of the laws of nature"
      cites: [{source: S10, locator: "p. 103"}]
      context: "On the poor grasp of science among people educated only in literature. Gladstone places it in his section on Faraday's evidence to the Public Schools Commission (18 November 1862) but does not say which text the words come from."
      axes: [B_cause, E_scope]
      kind: other
      verified_against: "secondary quotation"
      verified_on: 2026-10-02
      note: "Quoted by Gladstone."
  changes_over_life: [{value: UNKNOWN, how_known: "No change of worldview is reported in S1–S11. He attended the Sandemanian chapel as a child and made his profession of faith in 1821, about a month after his marriage (S10, p. 91; S5, p. 2); the brief exclusion of 1844 was over church discipline, not belief (S8)."}]
  coder_notes: "Example record. Axes, mid_basin and the primary system (CHRIST at 0.7) coded on 2026-10-02 from the sources already cited. The quotes from S3 and S4 are transcriptions from the edited correspondence (Epsilon), not checked against the manuscripts; the new statements are secondary quotations (Gladstone, Cantor). The weak points: B = 3 rests on his words as quoted by historians, and a reviewer could read the creation-of-force limit as the edge of science and score 4; C and E are coder's readings at 0.5; E is scored on the world's order (decision P7), and the sect and salvation reading is on C. B is scored on his account of nature (decision P6); his acceptance of the literal truth of the Bible would pull a whole-religion score lower. The primary code's weak point is CHRIST versus CLTHEI: no petition or intervention language was found in his own words, but only a few letters were read."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "English", certainty: 0.7, cites: [{source: S1, locator: "opening sentence"}], how_known: "Encyclopedia."}
  religious_heritage_by_birth: {value: "Sandemanian family, from at least his grandfather Robert Faraday; part of a long family tradition of religious dissent from the Church of England", certainty: 0.7, cites: [{source: S5, locator: "p. 1"}], how_known: "One historian's account of the family."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1821–c. 1855", certainty: 0.7, cites: [{source: S1, locator: "Early life (1821); Later life ('About 1855, Faraday's mind began to fail')"}], how_known: "Coder's summary of the dates in S1."}
  age_at_first_lasting_contribution: {value: 29, certainty: 0.7, cites: [{source: S1, locator: "opening sentence; Early life"}], how_known: "1821 minus 1791. The month of the rotation experiment was not checked, so it may be 30."}
  first_evidence_of_lio_type_views: {value: "In 'Observations on Mental Education' he separates the things of this life, open to reason and judgement, from the future life, known only by revelation; his public talk of fixed laws of nature and the conservation of force dates from the same decade.", year: 1854, certainty: 0.5, cites: [{source: S10, locator: "pp. 99–100, 103"}, {source: S8, locator: "section 'Electric discoveries' (1857 discourse)"}], how_known: "Earliest dated statement on the axes in the sources read. His laws of electrolysis (early 1830s) and the undated 'definite laws' remark (S8) suggest earlier views, but no earlier dated statement was read, so 0.5."}
  lio_views_relative_to_major_work: {value: "during major work", rationale: "The dated statements (1844 letter on keeping religion and philosophy apart; 1854 lecture; 1857 discourse) fall inside the major work period (1821–c. 1855). Cantor ties the search for God-given laws to the work itself (S8).", certainty: 0.5, cites: [{source: S3, locator: "final paragraph"}, {source: S10, locator: "pp. 99–100"}, {source: S8, locator: "section 'Electric discoveries'"}], how_known: "Dated statements; the earlier decades are not covered by any statement read."}
  worldview_during_major_work: {value: "A practising Sandemanian throughout: member from 1821, deacon 1832, elder 1840.", certainty: 0.7, cites: [{source: S5, locator: "p. 2"}], how_known: "One historian's account; matches his 1844 and 1861 letters."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: TODO}
  form_acquired: {value: TODO}
  circle_present: {value: TODO}
  reading: "Not assessed. The v7.1 two-lane paper uses Faraday as the case where the no-exemption form is present without the pantheist metaphysics (Lane B, B3 and V7.1-N B5). This record collects the facts that claim would be tested on; it does not test it."
  notes: ""

institutions:
  - {value: "Royal Institution of Great Britain", role: "Laboratory Assistant (1813, 1815–1826); Director of the Laboratory (1825–1867); Fullerian Professor of Chemistry (1833–1867); Superintendent of the House (1852–1867)", years: "1813–1867", kind: "research institute", certainty: 0.7, cites: [{source: S2, locator: "Ri positions"}], how_known: "The institution's own record."}
  - {value: "Royal Military Academy, Woolwich", role: "Professor of Chemistry", years: "1830–1851", kind: employer, certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "Institution's record."}
  - {value: "The Admiralty", role: "Scientific Adviser", years: "from 1829", kind: "government or state body", certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "Institution's record."}
  - {value: "Trinity House (lighthouse authority)", role: "Scientific Adviser", years: "1836–1865", kind: "government or state body", certainty: 1.0, cites: [{source: S2, locator: "Biography"}, {source: S5, locator: "p. 3"}], how_known: "Two sources agree."}
  - {value: "Sandemanian church, London (Paul's Alley meeting house)", role: "member, deacon, elder", years: "1821–1867, with an exclusion of a few weeks in spring 1844", kind: "religious body", certainty: 0.7, cites: [{source: S5, locator: "pp. 1–2, 4"}, {source: S8, locator: "section 'Primitive Christianity', para. 3"}], how_known: "Russell for the span of membership; Cantor for the length of the 1844 exclusion. One historian each."}
  - {value: "The Crown (Queen Victoria): Civil List pension (1836) and a Grace and Favour house at Hampton Court (1858)", kind: "patron or funder", years: "1836–1867", certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "Institution's record."}

collaborators:
  - {value: "Humphry Davy", roster_id: davy-humphry, relation: "mentor or employer", years: "1812–1820", certainty: 0.7, cites: [{source: S1, locator: "Early life"}], how_known: "Encyclopedia; S1 calls 1812–1820 his 'second apprenticeship, under Davy'."}
  - {value: "Charles Wheatstone", relation: collaborator, years: "1831", note: "worked together on the theory of sound", certainty: 0.7, cites: [{source: S1, locator: "Early life"}], how_known: "One source."}
  - {value: "William Thomson (later Lord Kelvin)", roster_id: thomson-william-kelvin, relation: correspondent, years: "1845", note: "suggested the magnetic-field experiment that led to the magneto-optical effect", certainty: 0.7, cites: [{source: S1, locator: "Later life"}], how_known: "One source."}
  - {value: "James Clerk Maxwell", roster_id: maxwell-james-clerk, relation: influenced, certainty: 0.7, cites: [{source: S1, locator: "opening paragraph; Later life"}], how_known: "Encyclopedia."}
  - {value: "John Tyndall", relation: other, note: "Royal Institution colleague and contemporary biographer", certainty: 0.7, cites: [{source: S5, locator: "pp. 2, 4"}], how_known: "One source."}
  - {value: "Ada Lovelace", roster_id: lovelace-ada, relation: correspondent, years: "1844", certainty: 1.0, cites: [{source: S3, locator: "whole letter"}], how_known: "Primary letter."}
  - {value: "Auguste De La Rive", relation: correspondent, years: "to 1861", certainty: 1.0, cites: [{source: S4, locator: "whole letter"}], how_known: "Primary letter."}

review:
  roster_status_reason: {value: "Core in v7.1 (no v7 review note) and carried into v8 unchanged; F rose from 4 to 5 when the Claude list was counted.", certainty: 0.7, cites: [{source: S7, locator: "roster.csv, rank 58"}], how_known: "Study roster."}
  controversies:
    - {value: "Whether he was ever offered a knighthood", certainty: 0.5, cites: [{source: S1, locator: "Later life"}, {source: S2, locator: "Biography"}, {source: S5, locator: "p. 4"}], how_known: "S1 and S5 say he declined one; S2 (summarising the Oxford DNB) says he said publicly he would not accept one but no evidence has been found that one was offered."}
  data_quality_flags:
    - "Start at the Royal Institution: S1 says he 'joined Davy in 1812'; S2 and S5 give 1813. 1813 is used (two sources)."
    - "Birth date: S5's gravestone transcription gives 21 September 1791; S1 and Faraday's own letter (S4) give 22 September."
    - "Second term as elder: Gladstone gives 'after 1860' (S10, p. 36). The often-cited start year 1860 is not confirmed to the year, and the 1864 resignation is from S5 only."
    - "Gladstone changed his account of the 1844 exclusion between editions: the Queen story is in the 1872 first edition (S11, p. 35) and gone from the 1873 second edition (S10, p. 36). Later writers who repeat the Queen story are following the first edition."
  open_questions:
    - "Primary code: CHRIST, CLTHEI, or something else? Needs a reviewed coding pass (docs/CODING_GUIDE.md)."
    - "B_cause 3 or 4: is the creation-of-force limit (S8) an exception or the edge of science? mid_basin is true either way."
    - "Read a primary text on B (the 1857 discourse on the conservation of force, or the 1854 lecture in Experimental Researches in Chemistry and Physics) to raise B above 0.7."
    - "Early reading (Watts, The Improvement of the Mind; Marcet, Conversations on Chemistry) is widely reported; confirm in Cantor 1991 or James 2010."
    - "Exact dates of the 1844 exclusion and readmission. Not in any source read. A search-engine summary of a WikiTree membership page gives 31 March and 5 May 1844, but WikiTree is user-edited and the page could not be opened (bot check), so the dates are not used. Cantor 1989 (S6) or Cantor 1991 (reviewed in S9) should settle it."
    - "What the 1844 discipline dispute was about. Cantor 1989 (S6) is the source; not read (paywalled)."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "L. Pearce Williams"
    citation: "Williams, L. Pearce. \"Michael Faraday.\" Encyclopaedia Britannica. Last updated September 18, 2026. https://www.britannica.com/biography/Michael-Faraday (article pages: main page with Early life; Theory of electrochemistry; Later life)."
    url: "https://www.britannica.com/biography/Michael-Faraday"
    accessed: 2026-10-01
    reliability_note: "Signed article by a Faraday biographer (author of Michael Faraday, 1965), fact-checked by Britannica editors."
    used_for: [identity, basics, contribution, childhood, collaborators, review]
  - id: S2
    type: tertiary
    kind: "institutional page"
    author: "Royal Institution of Great Britain"
    citation: "Royal Institution of Great Britain. \"Michael Faraday (1791-1867).\" Explore biographies. https://www.rigb.org/explore-science/explore/person/michael-faraday-1791-1867."
    url: "https://www.rigb.org/explore-science/explore/person/michael-faraday-1791-1867"
    accessed: 2026-10-01
    reliability_note: "Faraday's own institution, which holds his papers. The page names the Oxford Dictionary of National Biography as its source."
    used_for: [basics, contribution, childhood, institutions, review]
  - id: S3
    type: primary
    kind: letter
    author: "Michael Faraday"
    year: 1844
    citation: "Faraday, Michael. Letter to Augusta Ada Lovelace, 24 October 1844. Record Faraday1631 in Ɛpsilon: The Michael Faraday Collection. https://epsilon.ac.uk/view/faraday/letters/Faraday1631. Source of text: Bodleian Library, MS dep Lovelace-Byron 171, ff. 44–5, and Faraday's copy, IEE MS SC 3. Also published in The Correspondence of Michael Faraday, vol. 3 (1996)."
    url: "https://epsilon.ac.uk/view/faraday/letters/Faraday1631"
    accessed: 2026-10-01
    reliability_note: "Scholarly transcription from the edited correspondence (Faraday Project). Note 4 of the edition says the closing part of the letter, which holds the religion passage, is taken from Faraday's copy."
    used_for: [worldview, collaborators]
  - id: S4
    type: primary
    kind: letter
    author: "Michael Faraday"
    year: 1861
    citation: "Faraday, Michael. Letter to Arthur-Auguste De La Rive, 19 September 1861. Record Faraday4061 in Ɛpsilon: The Michael Faraday Collection. https://epsilon.ac.uk/view/faraday/letters/Faraday4061. Source of text: BPUG MS 2361, ff. 93–4. Also published in The Correspondence of Michael Faraday, vol. 6 (2011)."
    url: "https://epsilon.ac.uk/view/faraday/letters/Faraday4061"
    accessed: 2026-10-01
    reliability_note: "Scholarly transcription from the edited correspondence."
    used_for: [basics, worldview, collaborators]
  - id: S5
    type: secondary
    kind: "journal article"
    author: "Colin Russell"
    year: 2007
    citation: "Russell, Colin. \"Science and Faith in the Life of Michael Faraday.\" The Faraday Papers, no. 13. Cambridge: The Faraday Institute for Science and Religion, April 2007. 4 pp. https://www.faraday.cam.ac.uk/wp-content/uploads/resources/Faraday%20Papers/Faraday%20Paper%2013%20Russell_EN.pdf."
    url: "https://www.faraday.cam.ac.uk/wp-content/uploads/resources/Faraday%20Papers/Faraday%20Paper%2013%20Russell_EN.pdf"
    accessed: 2026-10-01
    reliability_note: "Short paper by a historian of science (Emeritus Professor, Open University; author of Michael Faraday: Physics and Faith, 2000), drawing on Cantor 1991. Published by a science-and-religion institute; the author argues a 'convergent' reading, so treat interpretation as his."
    used_for: [basics, childhood, worldview, heritage, timing, institutions, collaborators]
  - id: S6
    type: secondary
    kind: "journal article"
    author: "Geoffrey Cantor"
    year: 1989
    citation: "Cantor, Geoffrey. \"Why Was Faraday Excluded from the Sandemanians in 1844?\" The British Journal for the History of Science 22, no. 4 (1989): 433–37. https://doi.org/10.1017/S0007087400026388."
    url: "https://doi.org/10.1017/S0007087400026388"
    accessed: 2026-10-01
    reliability_note: "Peer-reviewed. Only the title and bibliographic record were consulted (paywalled); used only for the fact of the 1844 exclusion. Its findings are summarised by the same author in S8."
    used_for: [worldview]
  - id: S7
    type: tertiary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. v8 roster, data/roster/roster.csv, built by scripts/rebuild_roster.py from the five model lists."
    used_for: [review]
  - id: S8
    type: secondary
    kind: other
    author: "Geoffrey Cantor"
    year: 2020
    citation: "Cantor, Geoffrey. \"Drinking from a Fount on Sunday.\" Christian History, no. 134 (2020): How the Church Fostered Science and Technology. https://christianhistoryinstitute.org/magazine/article/drinking-from-a-fount-on-sundays."
    url: "https://christianhistoryinstitute.org/magazine/article/drinking-from-a-fount-on-sundays"
    accessed: 2026-10-01
    reliability_note: "Short magazine article, no footnotes, by the author of S6 and of the book-length study Michael Faraday: Sandemanian and Scientist (1991). Read as his own summary of his research."
    used_for: [worldview, institutions]
  - id: S9
    type: secondary
    kind: other
    author: "John Hedley Brooke"
    year: 1991
    citation: "Brooke, John Hedley. \"Among the Sandemanians.\" Review of Michael Faraday: Sandemanian and Scientist, by Geoffrey Cantor. London Review of Books 13, no. 14 (25 July 1991). https://www.lrb.co.uk/the-paper/v13/n14/john-hedley-brooke/among-the-sandemanians."
    url: "https://www.lrb.co.uk/the-paper/v13/n14/john-hedley-brooke/among-the-sandemanians"
    accessed: 2026-10-01
    reliability_note: "Book review by a historian of science and religion. Reports Cantor's findings, so it is not independent of S8."
    used_for: [worldview]
  - id: S10
    type: secondary
    kind: other
    author: "J. H. Gladstone"
    year: 1873
    citation: "Gladstone, J. H. Michael Faraday. 2nd ed. London: Macmillan, 1873. Scan: https://archive.org/details/michaelfaraday03gladgoog. Same wording in the 3rd ed. (1874), Project Gutenberg eBook 47396, https://www.gutenberg.org/ebooks/47396."
    url: "https://archive.org/details/michaelfaraday03gladgoog"
    accessed: 2026-10-01
    reliability_note: "Biography by a chemist who knew Faraday; the preface calls it 'my own reminiscences of the great philosopher'. Published within six years of his death. The preface to the second edition does not mention the changed passage. Quotes checked against the proofread Gutenberg text of the 3rd edition and the OCR of the 2nd-edition scan, which agree."
    used_for: [worldview, review]
  - id: S11
    type: secondary
    kind: other
    author: "J. H. Gladstone"
    year: 1872
    citation: "Gladstone, J. H. Michael Faraday. London: Macmillan, 1872 (first edition). Scan: https://archive.org/details/michaelfaraday02gladgoog."
    url: "https://archive.org/details/michaelfaraday02gladgoog"
    accessed: 2026-10-01
    reliability_note: "First edition of S10. Used only to record the Queen story that the second edition withdrew. Quote checked against the OCR text of the scan; the 1872 New York (Harper) printing, pp. 52–53, has the same passage."
    used_for: [worldview, review]
---

# Michael Faraday

> Status: example — unreviewed. This file shows the record structure. Primary system CHRIST at 0.7. LIO axes scored (A 0, B 3, D 2 at 0.7; C 1, E 3 at 0.5) and mid_basin true at 0.7 under the P4 test as amended by P6.

## Summary

Michael Faraday (1791–1867) was an English chemist and physicist who spent his working life at the Royal Institution in London [S1; S2]. His lasting work includes the electromagnetic rotation behind the electric motor (1821), electromagnetic induction (1831), the laws of electrolysis, the magneto-optical effect and diamagnetism (1845), and a field conception of force that Maxwell later put into equations [S1, Early life, Later life; S2]. He had almost no formal schooling [S1, Early life]. He was a lifelong Sandemanian, a small Christian sect, and served it as deacon and elder [S5, p. 2]. In a private letter he described his religion and his natural philosophy as "two distinct things" [S3].

## Life and work

Born at Newington Butts, Surrey, the son of a blacksmith who had moved to London from the north of England [S1, Early life; S2]. He was apprenticed to the bookbinder George Riebau from 1805 to 1812 and taught himself from the books that passed through the shop [S2; S1, Early life]. After attending Humphry Davy's lectures he sent Davy his bound notes, and in 1813 he became Davy's assistant at the Royal Institution [S1, Early life; S2; S5, p. 1]. Britannica dates his joining Davy to 1812 [S1, Early life]. That conflict is logged under review.

At the Royal Institution he became Director of the Laboratory (1825), Fullerian Professor of Chemistry (1833) and Superintendent of the House [S2]. He also advised the Admiralty and Trinity House and taught chemistry at Woolwich [S2]. His health broke down in 1839, and he did little creative science until 1845 [S1, Theory of electrochemistry]. From about 1855 his memory and powers declined [S1, Later life]. In 1858 the Queen gave him the use of a house at Hampton Court, where he died on 25 August 1867. He was buried at Highgate [S1, Later life; S2; S5, p. 4].

## Contribution and impact

- 1821: electromagnetic rotation, the first electric motor [S1, Early life; S2].
- 1825: isolated benzene [S1, Early life; S2].
- 1831: electromagnetic induction, then the first dynamo [S1, Early life].
- 1830s: the two laws of electrochemistry, and the terms electrode, cathode and ion [S1, Theory of electrochemistry; S2].
- 1845: rotation of polarized light by magnetism, and diamagnetism [S1, Later life; S2].
- By 1850: space as a medium carrying electric and magnetic strain, which became field theory. Maxwell acknowledged that the basic ideas of his field equations were Faraday's [S1, Later life].

He founded the Friday Evening Discourses and the Christmas Lectures [S2]. His name is on the Faraday effect, Faraday's law of induction and Faraday's laws of electrolysis [S1, Quick Facts].

## Childhood and education

The household was poor. His father was often ill, and the four children went hungry [S1, Early life]. The family was Sandemanian [S1, Early life; S2], a dissenting tradition that went back at least to his grandfather [S5, p. 1]. As a child he went to the Sandemanian chapel in Paul's Alley [S5, p. 1]. His schooling was reading, writing and ciphering at a church Sunday school [S1, Early life]. No consulted source mentions geometry or algebra in childhood, so early mathematics is entered as "arithmetic only" at certainty 0.7. Whether he had any early practice in definition-to-consequence reasoning is still TODO.

From age 14 he was apprenticed to a bookbinder. He read what came in for binding, including the electricity article in the third edition of the Encyclopaedia Britannica, and built a simple electrostatic machine and a voltaic pile [S1, Early life].

## Adult working worldview

He married Sarah Barnard on 12 June 1821 and sought membership of the Sandemanian church within days [S5, p. 2]. Gladstone says "he did not make any formal profession of his faith till a month after his marriage" [S10, p. 91]. He became a deacon in 1832 and an elder in 1840 [S5, p. 2]. In 1844 he was excluded from the church, which also ended his eldership [S10, p. 36; S6]. Cantor says this lasted "a few weeks in the spring of 1844" and was "owing to an internal dispute over church discipline" [S8]. The older story, that he was put out for being the Queen's guest on a Sunday, comes from the first edition of Gladstone's biography [S11, p. 35]. Gladstone dropped it in the second edition, which says the reason "is unknown except to the parties immediately concerned" [S10, p. 36]. He was restored to membership [S8; S10, p. 36], became an elder again after 1860 [S10, p. 36], and resigned his eldership in 1864 [S5, p. 4].

In his own words to Ada Lovelace in 1844: "There is no philosophy in my religion", the works of God "can never by any possibility come in contradiction" with the things of faith, and "that which is religious & that which is philosophical have ever been two distinct things" [S3]. In 1861 he wrote to De La Rive of the "good hope" that made death "a comfort - not a fear" [S4]. Russell argues that despite that separation, his faith shaped his sense of vocation and his search for a unity of forces, and that a private memorandum on atoms and fields invokes God [S5, pp. 2–3]. In his science he looked for laws: Cantor quotes his belief that "the Creator governs his material works by definite laws resulting from the forces impressed on matter" [S8]. He held that force is conserved because creating or destroying it is "only within the power of Him" [S8]. For the future life he relied on revelation alone: its truth "is received through simple belief of the testimony given" [S10, pp. 99–100].

Coding (2026-10-02): CHRIST at 0.7, from his own letters. Not CLASS_THEISM, since he held "no philosophy in my religion" [S3]; not CLTHEI, since no petition or intervention in nature appears in his own words [S10, p. 36; S8]. A 0, B 3 (his account of nature, P6) and D 2 at 0.7; C 1 and E 3 at 0.5. E is scored on the world's order (decision P7): God governs matter "by definite laws" [S8], and no favour in events appears in his own words. The sect and salvation reading is on C. mid_basin true at 0.7.

## Heritage (context only)

English, from a Sandemanian family with a long history of dissent from the Church of England [S1; S5, p. 1]. Heritage is recorded for context only. It is not a worldview code.

## Timing

His first lasting contribution came in 1821, at about age 29 [S1, Early life]. That same year he joined the Sandemanian church [S5, p. 2; S10, p. 91]. Throughout his major work (1821 to about 1855) he was a practising Sandemanian [S5, p. 2; S1, Later life]. The dated statements on the axes (1844, 1854, 1857) fall during the major work [S3; S10; S8].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. The v7.1 papers use Faraday as the test case of the form without the metaphysics: a devout physicist whose working method leaves no reserved clause. This record does not assess that claim yet. The fields `geometric_form_present`, `form_acquired` and `circle_present` are TODO.

## Open questions

- Primary code CHRIST versus CLTHEI: read more of his letters and prayers for petition or expected divine action in events. Would raise or overturn the 0.7.
- B_cause 3 or 4: is the creation-of-force limit an exception or the edge of science? mid_basin is true either way.
- Read a primary text for B (e.g. the 1857 conservation-of-force discourse) to raise its certainty.
- Was a knighthood ever offered? Sources disagree [S1, Later life; S2; S5, p. 4].
- Confirm his early reading (Watts, Marcet) in a full biography.
- Exact dates of the 1844 exclusion and readmission, and what the discipline dispute was about. Needs Cantor 1989 [S6] or Cantor 1991.

## Research log

- 2026-10-01: Read Britannica (S1: main, Theory of electrochemistry, Later life), the Royal Institution biography (S2), two letters in Epsilon (S3, S4), Russell's Faraday Paper 13 (S5), and the bibliographic record of Cantor 1989 (S6). Did not use Wikipedia as a citation. Its leads (Watts, Marcet, second eldership, FRS 1824, farad unit) are recorded as TODO or open questions. No worldview code, axis score or mid-basin value entered.
- 2026-10-01 (second pass): Closed most of the 1844 gap. Read Cantor's 2020 Christian History article (S8), Brooke's 1991 LRB review of Cantor's book (S9), and the first and second editions of Gladstone's biography (S11, S10; archive.org scans, plus the Gutenberg text of the 3rd edition). Cantor 1989 (S6) and Cantor 1991 are paywalled or lending-only and were not read. Every quoted phrase was checked word for word against the source text. Exact readmission date still not found.
- 2026-10-01 (third pass): No new research. Updated for the decisions of 2026-10-01: schema 1.1, era and region notes (P2, P3), and the mid-basin note now points to the P4 test. `mid_basin` stays TODO until the axes are scored.
- 2026-10-02 (fourth pass): Scored A–E and mid_basin from the sources already cited, re-reading S3, S4, S5, S8, S9 and S10 (Gutenberg 3rd edition and the archive.org 2nd-edition OCR). No new sources. Every new quotation was checked word for word with verify_quotes.py. Primary system left TODO.
- 2026-10-02 (fifth pass): Decision P6 approved. Coded the primary system CHRIST at 0.7 from the sources already cited (S3, S4, S5, S8, S9, S10); no new sources. Rechecked B and mid_basin under P6: unchanged.
- 2026-10-02 (sixth pass): Decision P7 approved. Rescored E_scope on the world's order from the sources and quotations already in the record (S3, S5, S8, S10); no new sources or quotations. The sect and salvation reading moved to the C_ledger rationale.
