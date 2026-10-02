---
record:
  record_type: person
  schema_version: "1.1"
  record_version: 4
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (overnight agent run for Jason, first pool)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages, papers and letter translations"
  collected_on: 2026-10-02
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created. Basics, contribution, childhood and worldview filled from SEP (Kennedy; Oppy et al.), Britannica, MacTutor, the IAS page, Feferman's synopsis of the Collected Works, Todorov's 2007 portrait and the IAS-approved English translations of his letters to his mother and brother. Coded CLASS_THEISM at 0.5 (theist, following Leibniz; mathematical platonism recorded but not coded as PLATO). A, B, D at 0.7; C at 0.5; E TODO. mid_basin true under P4. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "mid_basin rechecked under decision P6 (B_cause scored on the account of nature): B_cause and mid_basin unchanged. Note added to mid_basin how_known. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit fixes: primary_system CLASS_THEISM at 0.5 -> BELOW_THRESHOLD, with CLASS_THEISM and CLTHEI named as candidates in a note (no scholar places him in a theist code; the simple or immutable God test is not shown). mid_basin unchanged (true at 0.7; it uses only A and B). Lutheran baptism (nominal_affiliations) 0.5 -> 0.7, one reliable source; the same Todorov fact in family_religion, religious_heritage_by_birth and baptism_or_initiation also 0.5 -> 0.7. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit, run 2: E_scope note points to open item P7 (which domain E is scored on). Still TODO. Not reviewed."}

identity:
  id: godel-kurt
  display_name: "Kurt Gödel"
  roster:
    canonical_name: "Kurt Gödel"
    rank: 49
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: mathematics
    field_bucket: mathematics
  full_name: {value: "Kurt Friedrich Gödel", certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}], how_known: "SEP gives the full name; Britannica and MacTutor give Kurt Gödel."}
  native_name: {value: "Kurt Gödel (German)", certainty: 1.0, cites: [{source: S2, locator: "Quick Facts ('also spelled: Goedel')"}], how_known: "German was his native language (S7). Britannica gives the spelling Goedel."}
  aliases:
    - {name: "Gödel-Kurt", kind: "roster alias"}
    - {name: "Kurt-Gödel", kind: "roster alias"}
    - {name: "Kurt Goedel", kind: transliteration}
    - {name: "der Herr Warum (Mr. Why)", kind: other}

basics:
  birth:
    date: {value: "1906-04-28", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "Quick Facts"}, {source: S3, locator: "Quick Info"}], how_known: "Three sources agree."}
    place:
      value: "Brünn (Brno), Moravia"
      modern_name: "Brno, Czech Republic"
      polity_then: "Austria-Hungary"
      certainty: 1.0
      cites: [{source: S1, locator: "§1"}, {source: S2, locator: "Quick Facts"}, {source: S3, locator: "Quick Info"}]
      how_known: "Three sources agree. After 1918 Brno was in Czechoslovakia (S2, Early life and career)."
  death:
    date: {value: "1978-01-14", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "Quick Facts"}, {source: S3, locator: "Quick Info"}], how_known: "Three sources agree."}
    place:
      value: "Princeton, New Jersey"
      modern_name: "Princeton, New Jersey, United States"
      polity_then: "United States"
      certainty: 1.0
      cites: [{source: S1, locator: "§1"}, {source: S3, locator: "Quick Info; Biography (in his hospital room)"}]
      how_known: "Two sources. SEP quotes the death certificate: 'starvation and inanition, due to personality disorder'."
  first_lasting_contribution_year: {value: 1929, certainty: 1.0, cites: [{source: S1, locator: "§1 (completeness theorem, dissertation 1929)"}, {source: S2, locator: "Gödel's theorems"}, {source: S3, locator: "Biography"}], how_known: "The completeness theorem for first-order logic was the main theorem of his 1929 dissertation; it was published in 1930."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "§1"}], how_known: "From first_lasting_contribution_year under the era buckets (decision P2)."}
  region_of_birth: {value: "Eastern Europe", certainty: 1.0, cites: [{source: S1, locator: "§1 ('now Brno in the Czech Republic')"}], how_known: "Czechia is Eastern Europe in data/reference/regions.csv (UN M49 sub-region, decision P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "§1"}, {source: S3, locator: "Biography"}], how_known: "The completeness and incompleteness theorems (1929–1931) and the consistency of the axiom of choice and the continuum hypothesis (1935–1937) were done at the University of Vienna (Austria is Western Europe in regions.csv). From 1940 he worked at the Institute for Advanced Study in Princeton (North America), where the rotating-universe solutions and all the philosophical work were done. Two regions, so 0.7.", alternatives: [{value: "North America", cites: [{source: S1, locator: "§1"}, {source: S4, locator: "Visits"}], note: "Princeton, 1940–1978; also visits in 1933–34, 1935 and 1938."}]}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S1, locator: "§1"}], how_known: "As the sources record it."}
  languages_of_work: {value: [German, English], certainty: 1.0, cites: [{source: S1, locator: "§1; bibliography"}, {source: S3, locator: "Biography"}], how_known: "The 1929–1931 papers are in German; the Princeton papers and lectures in English. His notebooks are in Gabelsberger German shorthand (S7)."}
  occupations:
    value: [mathematician, logician, philosopher, "university lecturer (Privatdozent)", "research professor"]
    certainty: 1.0
    cites: [{source: S1, locator: "§1"}, {source: S2, locator: "heading; Early life and career"}, {source: S4, locator: "Visits"}]
    how_known: "Three sources agree."

contribution:
  fields: {value: ["mathematical logic", "set theory", "philosophy of mathematics", "general relativity (cosmology)", philosophy], certainty: 1.0, cites: [{source: S1, locator: "opening paragraph; §1; §2"}, {source: S2, locator: "Gödel's theorems; Turn to philosophy"}, {source: S3, locator: "Biography"}], how_known: "Three sources agree."}
  lasting_original_contributions:
    - {value: "Completeness theorem for first-order logic", year: "1929", kind: theory, lasting: "a basic theorem of logic, taught everywhere (S2)", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "Gödel's theorems"}, {source: S3, locator: "Biography"}], how_known: "Three sources."}
    - {value: "Incompleteness theorems: any consistent axiomatic system containing arithmetic has propositions it can neither prove nor disprove, and cannot prove its own consistency", year: "1931", kind: theory, lasting: "among the 'landmark theorems in twentieth century mathematics' (S1)", certainty: 1.0, cites: [{source: S1, locator: "opening paragraph; §1"}, {source: S2, locator: "Gödel's theorems"}, {source: S3, locator: "Biography"}, {source: S4, locator: "description"}], how_known: "Four sources."}
    - {value: "Consistency of the axiom of choice and the generalized continuum hypothesis with the axioms of set theory (the constructible universe L)", year: "1935–1940", kind: theory, lasting: "Cohen's 1963 independence proof built on it (S3)", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S3, locator: "Biography"}, {source: S4, locator: "description (1938, 1940)"}], how_known: "Three sources."}
    - {value: "Rotating-universe solutions of Einstein's field equations, allowing closed time-like paths", year: "1949", kind: discovery, lasting: "a standard example in general relativity (S7)", certainty: 0.7, cites: [{source: S1, locator: "§1"}, {source: S7, locator: "Sect. 2"}], how_known: "SEP dates the paper; Todorov describes the result."}
    - {value: "Dialectica interpretation of intuitionistic arithmetic", year: "1958", kind: method, lasting: "named after the journal; used in proof theory (S1)", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "One source."}
  evidence_of_impact:
    - {value: "SEP: one of the principal founders of the modern, metamathematical era in mathematical logic", kind: "scholarly consensus", certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}], how_known: "SEP (Kennedy)."}
    - {value: "IAS calls him the foremost mathematical logician of the twentieth century", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S4, locator: "description"}], how_known: "Institutional page of his own institute."}
    - {value: "Einstein Award (1951) and National Medal of Science (1974)", kind: "honours in lifetime", certainty: 1.0, cites: [{source: S3, locator: "Biography"}, {source: S4, locator: "Honors"}], how_known: "Two sources."}
  major_works:
    - {value: "Über die Vollständigkeit des Logikkalküls (dissertation; completeness theorem)", year: "1929 (published 1930)", kind: "paper or paper series", certainty: 1.0, cites: [{source: S2, locator: "Gödel's theorems"}, {source: S1, locator: "§1"}], how_known: "Two sources."}
    - {value: "Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I", year: "1931", kind: "paper or paper series", certainty: 1.0, cites: [{source: S2, locator: "Gödel's theorems"}, {source: S3, locator: "Biography"}], how_known: "Two sources."}
    - {value: "The Consistency of the Axiom of Choice and of the Generalized Continuum-Hypothesis with the Axioms of Set Theory", year: "1940", kind: book, certainty: 1.0, cites: [{source: S3, locator: "Biography"}, {source: S4, locator: "description"}], how_known: "Two sources."}
    - {value: "What is Cantor's Continuum Problem?", year: "1947 (revised 1964)", kind: "paper or paper series", certainty: 0.7, cites: [{source: S1, locator: "§1 (1947)"}, {source: S2, locator: "Turn to philosophy (1964)"}], how_known: "SEP dates it 1947 and Britannica 1964, with different titles; see flags."}
    - {value: "Some Basic Theorems on the Foundations of Mathematics and Their Philosophical Implications (Gibbs Lecture, Brown University)", year: "1951 (published 1995)", kind: "lecture series", certainty: 1.0, cites: [{source: S1, locator: "§1; §3.1"}, {source: S4, locator: "Honors (AMS Gibbs Lect 1951)"}], how_known: "Two sources."}
    - {value: "Ontological proof (manuscript)", year: "1970 (published 1995)", kind: notebook, certainty: 1.0, cites: [{source: S8, locator: "§9; bibliography (Gödel 1995, 'Ontological Proof')"}, {source: S7, locator: "Sect. 3"}], how_known: "Two sources."}
  honours:
    - {value: "Einstein Award", year: 1951, certainty: 1.0, cites: [{source: S3, locator: "Biography"}, {source: S4, locator: "Honors"}], how_known: "Two sources."}
    - {value: "Honorary degrees from Yale (1951), Harvard (1952), Amherst (1967) and Rockefeller University (1972)", year: "1951–1972", certainty: 0.7, cites: [{source: S4, locator: "Honors"}], how_known: "IAS page only."}
    - {value: "National Medal of Science", year: 1974, certainty: 1.0, cites: [{source: S3, locator: "Biography"}, {source: S4, locator: "Honors"}], how_known: "Two sources."}
    - {value: "Member of the US National Academy of Sciences; Foreign Member of the Royal Society; member of the Institut de France and fellow of the British Academy", certainty: 0.7, cites: [{source: S3, locator: "Biography"}, {source: S4, locator: "Honors"}], how_known: "Two sources, worded differently."}
    - {value: "Refused membership, and later honorary membership, of the Academy of Sciences in Vienna, and refused Austria's highest national medal for science and art", certainty: 0.7, cites: [{source: S3, locator: "Biography"}], how_known: "MacTutor only."}
  definition_fit: {value: "clearly meets", rationale: "The completeness and incompleteness theorems and the consistency proofs in set theory are lasting original results that changed mathematical logic.", certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}, {source: S2, locator: "Gödel's theorems"}], how_known: "Lane A definition applied to the contributions above."}

childhood:
  family_religion: {value: "Lutheran, his mother's church; the surrounding state and town were Catholic", certainty: 0.7, cites: [{source: S7, locator: "Sect. 1"}], how_known: "One reliable, undisputed source (Todorov, drawing on Dawson's biography), so 0.7."}
  family_religious_practice: {value: TODO, note: "No account of worship at home in the sources read. His 1950 letter says only that his school religion classes were poor (S6). Dawson's biography (1997, ch. 1) is the likely source; it is only on archive.org's restricted lending, so it was not read."}
  parents_and_household:
    - {value: "Father Rudolf August Gödel, from a Viennese family, managing director and part owner of a major textile firm in Brno; died 1929", role: father, certainty: 1.0, cites: [{source: S3, locator: "Biography"}, {source: S1, locator: "§1 ('a businessman')"}], how_known: "Two sources."}
    - {value: "Mother Marianne Gödel, born Handschuh, from the Rhineland; a well-educated woman with a literary education, part of it in France; fourteen years younger than her husband. He stayed close to her all his life and wrote her many letters.", role: mother, certainty: 1.0, cites: [{source: S3, locator: "Biography"}, {source: S1, locator: "§1"}, {source: S6, locator: "letters 1946–1965"}], how_known: "Two reference sources and the letters themselves."}
    - {value: "One older brother, Rudolf (1902–1994), who studied medicine in Vienna and became a radiologist", role: sibling, certainty: 1.0, cites: [{source: S3, locator: "Biography"}, {source: S7, locator: "Sect. 1"}], how_known: "Two sources; dates from Todorov."}
  household_circumstances: {value: "Well-off family of a textile-firm director in Brno; after the father's death in 1929 the mother bought a large flat in Vienna, where both sons lived with her", certainty: 1.0, cites: [{source: S1, locator: "§1 ('The family was well off')"}, {source: S3, locator: "Biography"}], how_known: "Two sources."}
  schooling:
    - {value: "Primary school, Brno", stage: other, institution: "primary school, Brno", years: "c. 1912–1916", ages: "c. 6–10", certainty: 0.5, cites: [{source: S1, locator: "§1 ('an exemplary student at primary school')"}], how_known: "SEP names the stage; the years and ages are the coder's estimate."}
    - {value: "German-language Realgymnasium in Brno; top marks in Latin, excelled in languages and religion (or theology); by the final years he had mastered university mathematics", stage: "grammar or secondary school", institution: "Realgymnasium, Brno", years: "c. 1916–1924", ages: "c. 10–18", certainty: 0.7, cites: [{source: S1, locator: "§1"}, {source: S3, locator: "Biography (brother Rudolf's account)"}, {source: S7, locator: "Sect. 1"}], how_known: "Three sources. SEP and Todorov give 1924 for leaving; MacTutor gives 1923 (see flags)."}
    - {value: "University of Vienna: began in physics, turned to mathematics after Furtwängler's lectures; learned logic from Hahn and Carnap; Dr. phil. in mathematics under Hahn", stage: university, institution: "University of Vienna", years: "1924–1929", ages: "18–23", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S3, locator: "Biography"}, {source: S7, locator: "Sect. 1"}], how_known: "Three sources. Start year 1923 in MacTutor; degree year 1930 on the IAS page (see flags)."}
  early_mathematics: {value: "advanced mathematics", ages: "c. 16–18", description: "His brother Rudolf said that he 'had mastered university mathematics by his final Gymnasium years'. Todorov, citing Dawson, says his only mark below the top one at school was in mathematics.", certainty: 0.7, cites: [{source: S3, locator: "Biography"}, {source: S7, locator: "Sect. 1"}], how_known: "His brother's account through MacTutor; Todorov's detail points the other way on marks (see flags)."}
  early_geometric_style_reasoning: {value: "As a small child he asked so many questions that the family called him 'Mr. Why'; at school he was noted for exact Latin, with no grammatical error, and for teaching himself university mathematics.", certainty: 0.7, cites: [{source: S7, locator: "Sect. 1 ('der Herr Warum')"}, {source: S3, locator: "Biography"}], how_known: "Two secondary sources. Facts only; the Lane B reading is in lane_b."}
  early_science_exposure:
    - {value: "At about 8 he read medical books about the rheumatic fever he had had at 6, and became convinced he had a weak heart", year: "c. 1914", age: "c. 8", certainty: 1.0, cites: [{source: S3, locator: "Biography"}, {source: S7, locator: "Sect. 1"}, {source: S2, locator: "Early life and career"}], how_known: "Three sources (Britannica gives the fever at 6)."}
    - {value: "Became interested in Goethe's colour theory and its dispute with Newton, which he later said led him indirectly to his choice of profession; entered university to study physics", year: "1921–1924", age: "15–18", certainty: 0.7, cites: [{source: S6, locator: "letter of 26 August 1946"}, {source: S1, locator: "§1"}], how_known: "His own letter (in translation) and SEP on physics as his first field."}
  key_early_reading:
    - {value: "Houston Stewart Chamberlain's book 'Goethe', read at Marienbad in 1921", age: "15", certainty: 0.7, cites: [{source: S6, locator: "letter of 26 August 1946"}], how_known: "His own letter, which says he read it 'exactly 25 years ago' and that 'This Goethe book was the beginning of my interest with Goethe's science of colors and his argument with Newton'. One private letter, in translation."}
  childhood_mentors: [{value: UNKNOWN, how_known: "No teacher before university is named in S1–S7. His university teachers (Furtwängler, Hahn, Carnap) are listed under collaborators."}]
  languages_in_childhood: {value: [German, Latin, French, English], certainty: 0.7, cites: [{source: S7, locator: "Sect. 1"}], how_known: "Todorov: German at home; Latin, French and English at school; he neither studied nor spoke Czech."}
  notable_events:
    - {value: "Rheumatic fever at 6, followed by lifelong worry about his health", age: "6", year: "c. 1912", certainty: 1.0, cites: [{source: S2, locator: "Early life and career"}, {source: S3, locator: "Biography"}], how_known: "Two sources."}
    - {value: "Became a citizen of the new Czechoslovakia when Austria-Hungary broke up; he saw himself as an Austrian in exile", age: "12", year: "1918", certainty: 0.7, cites: [{source: S2, locator: "Early life and career"}, {source: S7, locator: "Sect. 1"}], how_known: "Britannica on the change; Todorov on how he saw himself."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1929–1978", certainty: 1.0, cites: [{source: S1, locator: "§1"}], how_known: "From his dissertation to his death."}
  nominal_affiliations:
    - {value: "Baptized in a Lutheran congregation; no church membership is reported for his adult life in the sources read", years: "from birth", role: "baptized member", certainty: 0.7, cites: [{source: S7, locator: "Sect. 1 ('baptised in a Lutheran congregation')"}], how_known: "One reliable, undisputed source for the baptism (Todorov), so 0.7 (raised from 0.5 after the lens audit). The Grandjean questionnaire's answer on religion (Collected Works IV) was not read directly."}
  self_described_science_religion_relation:
    value: "Science and theology are not in conflict. He wrote to his mother that it may already be possible, by reason alone and without faith, to see that the 'theological world view' (that the world and everything in it has a good meaning) fits all known facts, and that the idea that everything has a meaning matches the principle that everything has a cause, on which science rests. He held that there is a scientific, exact philosophy and theology, which is also fruitful for science. Science, he wrote, shows the greatest regularity and order in everything, and order is a form of rationality."
    certainty: 0.7
    cites: [{source: S7, locator: "Sect. 3, note 14 (letter of October 1961)"}, {source: S1, locator: "§3.1 ('My Philosophical Viewpoint', c. 1960)"}, {source: S6, locator: "letter of 23 July 1961"}]
    how_known: "His private letters (one in IAS-approved translation, one through a secondary quotation) and a private list quoted by SEP. Consistent private writing, so 0.7. Quotations are in statements."
  primary_system:
    value: BELOW_THRESHOLD
    cites: [{source: S5, locator: "Vol. IV section ('Grandjean questionnaire')"}, {source: S7, locator: "Sect. 3, note 14"}, {source: S1, locator: "§3.1"}, {source: S8, locator: "§9"}]
    how_known: "His theism is stated in private writing (the Grandjean answer, S5; letters, S6, S7). No scholar read places him in a particular theist code, and one of the CLASS_THEISM tests (a simple or immutable God) is not shown in the sources read, so the choice of code is below 0.5. Changed from CLASS_THEISM at 0.5 after the lens audit (2026-10-02); the CODING_GUIDE (§3) uses 0.5 only when a scholar backs the reading."
    note: "Candidates: CLASS_THEISM (he called his belief 'theistic not pantheistic (following Leibniz rather than Spinoza)', S5; argument to God by reason and nature as an order of causes are met; a simple or immutable God is not shown) and CLTHEI (a personal afterlife, S6, but no petition, miracles or special divine action in what was read). Reading Wang 1987 and 1996 and the Collected Works IV letters could settle it."
    rationale: "In the unsent Grandjean questionnaire (sent to him in 1974) he called his belief 'theistic not pantheistic (following Leibniz rather than Spinoza)' (S5). The v7.1 scoring note for CLASS_THEISM lists Leibniz. The code's use_when asks for (1) an argument to God by reason, (2) a simple or immutable God and (3) nature as an order of causes. (1) is met: the ontological proof (1970, S8) and his letter saying the theological world view can be grasped 'purely rationally' (S7). (3) is met: everything has a cause, and science shows order in everything (S6, S7). (2) is not shown in the sources read. Mathematical platonism is recorded (S1, S2), but the PLATO guidance says that alone does not settle the worldview, and his own writing names Leibniz's theism rather than Plato's forms as its origin. No scholar in S1–S8 names his theism as classical theism, so the code is withheld (BELOW_THRESHOLD) with CLASS_THEISM and CLTHEI as candidates."
  secondary_system: {value: UNKNOWN, how_known: "No second system in S1–S8. His mathematical platonism (S1 opening paragraph; S2 Turn to philosophy) is recorded under self_described_science_religion_relation and coder_notes, not as a code, following the PLATO guidance."}
  candidate_codes_considered:
    - {code: CLASS_THEISM, reason: "Leading candidate, not coded (BELOW_THRESHOLD): no scholar read places him here. Leibnizian theism reached by reason; an ontological proof; the world as an order of causes and meaning. Criterion (2), a simple and immutable God, is not shown in the sources read.", cites: [{source: S5, locator: "Vol. IV section"}, {source: S8, locator: "§9"}, {source: S7, locator: "Sect. 3, note 14"}]}
    - {code: PLATO, reason: "Rejected. He defended mathematical Platonism and held that 'objective reality is beautiful, good, and perfect' (S1, §3.1, from Wang's notes of conversations). But he names Leibniz, not Plato, as his model and calls his belief theistic (S5). The PLATO guidance says mathematical platonism alone does not settle the worldview, and its review note asks whether his writing makes an intelligible reality the origin of existence and values; what was read makes God that origin.", cites: [{source: S1, locator: "§3; §3.1"}, {source: S5, locator: "Vol. IV section"}]}
    - {code: CLTHEI, reason: "Second candidate, not coded. He expected a personal afterlife (S6, 23 July 1961). But nothing read shows petition, miracles or special divine action; he looks to order and reason. Would become the code if Wang's books or the Collected Works show a God who acts in particular events, or rule out a simple, immutable God.", cites: [{source: S6, locator: "letter of 23 July 1961"}]}
    - {code: CHRIST, reason: "Rejected. Baptized Lutheran (S7), but no adult church life is reported, he kept a notebook on 'Fehler in der Bibel' (errors in the Bible) and distrusted papal nuncios (S6, 8 May 1958). Baptism alone is never a code.", cites: [{source: S7, locator: "Sect. 3, note 14"}, {source: S6, locator: "letter of 8 May 1958"}]}
    - {code: PANT, reason: "Rejected by his own words: 'theistic not pantheistic', Leibniz 'rather than Spinoza' (S5).", cites: [{source: S5, locator: "Vol. IV section"}]}
  lio_axes:
    A_locus:
      value: 1
      basis: consistent_private_letters
      certainty: 0.7
      cites: [{source: S5, locator: "Vol. IV section ('Grandjean questionnaire')"}, {source: S8, locator: "§9"}, {source: S6, locator: "letter of 23 July 1961"}]
      how_known: "The unsent questionnaire (through Feferman's quotation), private letters and an unpublished proof all point the same way. Private writing, so 0.7; the key line is a secondary quotation."
      rationale: "Leans to the transcendent pole. He states a theism that is not pantheism and follows Leibniz rather than Spinoza (S5), so God is not the world. The God of the ontological proof is a being whose essential properties are all the positive properties (S8). He also quotes 'And God created a new Heaven and a new Earth' as a future act (S6). Not 0, because nothing read shows a God in a changing give-and-take relationship with people; the God he argues for is known by reason."
    B_cause:
      value: 3
      basis: consistent_private_letters
      certainty: 0.7
      cites: [{source: S6, locator: "letters of 23 July 1961 and 20 September 1952"}, {source: S7, locator: "Sect. 3, note 14 (letter of October 1961)"}, {source: S1, locator: "§3.1"}]
      how_known: "Several private letters over ten years, consistent with each other and with the private list quoted by SEP, so 0.7."
      rationale: "Leans to law. Science shows 'the greatest regularity and order reign in everything. Order is but a form of rationality' (S6, 1961). Everything having a meaning is 'precisely analogous to the principle that everything has a cause on which the whole science rests' (S7, October 1961). Even reported telepathy is treated as a human capacity that science can measure (S6, 1952). There is no miracle or answered petition in what was read. The stated limited exception: he takes the end of the world 'prophesied in the last book of the Bible', and a new heaven and earth after it, as a real future event that science leaves room for (S6, 1961). So 3. His work (logic, set theory, relativity) has no exceptions at all, so scoring on his account of nature or on his work gives the same result."
    C_ledger:
      value: 3
      basis: scholarly_reconstruction
      certainty: 0.5
      cites: [{source: S6, locator: "letters of 27 February 1950 and 23 July 1961"}, {source: S7, locator: "Sect. 3, note 14 (letter of October 1961)"}]
      how_known: "Coder's reading of three letters that discuss the afterlife but not judgement directly, so 0.5."
      rationale: "Leans to consequence. He argues for a next life because a being with so many possibilities should be allowed to fulfil them (S6, 1961), and says earthly life 'can only be a means toward the goal of another existence' (S7, October 1961). The next life is a continuation and completion, not a court; no reward or punishment language appears in what was read. Not 4, because he accepts the Bible's end of the world and new creation (S6, 1961), which carries the judgement tradition, and the letters read are a small selection."
    D_authority:
      value: 3
      basis: consistent_private_letters
      certainty: 0.7
      cites: [{source: S7, locator: "Sect. 3, note 14 (letter of October 1961; notebook 'Fehler in der Bibel')"}, {source: S1, locator: "§3.1 ('My Philosophical Viewpoint')"}, {source: S6, locator: "letters of 23 July 1961 and 8 May 1958"}]
      how_known: "Private letters and notebooks, consistent with each other, so 0.7."
      rationale: "Leans to reason. The theological world view may be grasped 'purely rationally (without the support of faith' (S7). There is 'a scientific (exact) philosophy and theology' (S1). He kept a notebook on errors in the Bible (S7) and had 'very little trust in the love of truth of papal nuncii' (S6, 1958). The stated limited exception: he treats the Bible's prophecy of the end of the world as something science confirms, so scripture keeps a place as a witness that reason can check (S6, 1961). So 3."
    E_scope: {value: TODO, note: "Little in the sources read. His view that religions are mostly bad but religion is not (item 14 of 'My Philosophical Viewpoint') and his remarks on Islam are known only through Wang's books and Engelen's paper on the Max Phil notebooks, which were not read (Wang not online; Engelen's HAL copy blocked by a bot check). His 1952 letter says every human has the same psychic capacities to some degree (S6), which points toward the same rules for everyone but is not about religion. Score after reading Wang 1996 (p. 316) or the Collected Works. Which domain E is scored on is open (OPEN_DECISIONS P7, PROPOSED); score once it is decided."}
  mid_basin:
    value: true
    certainty: 0.7
    cites: [{source: S5, locator: "Vol. IV section"}, {source: S6, locator: "letter of 23 July 1961"}, {source: S7, locator: "Sect. 3, note 14"}]
    how_known: "P4 test applied to the scores above: A_locus = 1 (≤ 1) at 0.7 and B_cause = 3 (≥ 3) at 0.7. Both certainties are at least 0.7, so true. B is the same whether scored on his account of nature or on his work in logic and relativity, so decision P6 (2026-10-02) does not change the result. Certainty 0.7, not higher, because both axes rest on private writing and one secondary quotation. F = 5, so first-rank is met."
  statements:
    - text: "theistic not pantheistic (following Leibniz rather than Spinoza)"
      cites: [{source: S5, locator: "Vol. IV section ('Grandjean questionnaire')"}]
      context: "Answer on religion in the questionnaire the sociologist Burke D. Grandjean sent him in 1974; he filled it in but never returned it. Feferman, editor of the Collected Works, quotes it in indirect form ('he said that his view was …')."
      axes: [A_locus]
      kind: other
      verified_against: "secondary quotation"
      verified_on: 2026-10-02
      note: "Collected Works IV prints the questionnaire; not read directly. Wording elsewhere differs slightly."
    - text: "If the world is set up rationally and has a meaning, then that must be so."
      cites: [{source: S6, locator: "letter to his mother, Princeton, 23 July 1961"}]
      context: "His answer to his mother's question whether they would meet again in the hereafter. Feferman's translation reads 'If the world is rationally organized and has a sense, then that must be so' (S5)."
      axes: [C_ledger]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
      note: "English translation by Marilya Veteto Reese, ed. Stephen Budiansky, reprinted with permission of the IAS; original in the Wienbibliothek im Rathaus."
    - text: "For it is certainly not chaotic and arbitrary, but rather, as science shows, the greatest regularity and order reign in everything. Order is but a form of rationality."
      cites: [{source: S6, locator: "letter to his mother, 23 July 1961"}]
      context: "Same letter, his reason for thinking the world is rationally set up."
      axes: [B_cause]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
      note: "Reese/Budiansky translation. Feferman's version: 'as science shows, the greatest regularity and order prevails in all things' (S5)."
    - text: "Science confirms at any rate the end of the world prophesied in the last book of the Bible and leaves room for that which will then follow"
      cites: [{source: S6, locator: "letter to his mother, 23 July 1961"}]
      context: "Same letter; it goes on to quote 'And God created a new Heaven and a new Earth.'"
      axes: [B_cause, D_authority, A_locus]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
      note: "Reese/Budiansky translation."
    - text: "already today it may be possible purely rationally (without the support of faith [...] to apprehend that the theological world view is thoroughly compatible with all known facts"
      cites: [{source: S7, locator: "Sect. 3, note 14 (letter to his mother, October 1961)"}]
      context: "Letter on the theological world view, which he defines in the same letter as 'the idea that the world and everything in it has a good and indubitable meaning'."
      axes: [D_authority]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-02
      note: "Todorov quotes it from George Dyson's posting of a translation supplied by Feferman. Three steps from the letter; supports D only together with S1 and S6."
    - text: "The idea that everything in the world has a meaning is precisely analogous to the principle that everything has a cause on which the whole science rests."
      cites: [{source: S7, locator: "Sect. 3, note 14 (letter to his mother, October 1961)"}]
      context: "Same letter."
      axes: [B_cause]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-02
      note: "As above."
    - text: "Since our earthly existence has in itself a very doubtful meaning, it follows directly that it can only be a means toward the goal of another existence."
      cites: [{source: S7, locator: "Sect. 3, note 14 (letter to his mother, October 1961)"}]
      context: "Same letter."
      axes: [C_ledger]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-02
      note: "As above."
    - text: "There is a scientific (exact) philosophy and theology, which deals with concepts of the highest abstractness; and this is also most highly fruitful for science."
      cites: [{source: S1, locator: "§3.1 (item of 'My Philosophical Viewpoint', c. 1960)"}]
      context: "One of fourteen points in a list he wrote about 1960, transcribed by Cheryl Dawson and published in Wang 1996, p. 316 (S1)."
      axes: [D_authority]
      kind: "notebook or diary"
      verified_against: "secondary quotation"
      verified_on: 2026-10-02
      note: "SEP's wording; other transcriptions put 'and theology' in braces as a later addition."
    - text: "But I have very little trust in the love of truth of papal nuncii."
      cites: [{source: S6, locator: "letter to his mother, 8 May 1958"}]
      context: "On a claim, credited to a papal nuncio, that Crown Prince Rudolf was murdered."
      axes: [D_authority]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
      note: "Reese/Budiansky translation. About church officials, not doctrine."
    - text: "each human possesses these capacities but in most only to a very minor degree"
      cites: [{source: S6, locator: "letter to his mother, 20 September 1952"}]
      context: "On his test of Adele's knack for guessing numbers and on university studies of 'occult visitations'."
      axes: [B_cause]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
      note: "Reese/Budiansky translation. Shows him treating even the paranormal as a natural capacity open to measurement."
  changes_over_life:
    - {value: "By his own later account he held mathematical realism from 1925; Feferman says this is hard to square with other evidence", year: "1925", certainty: 0.5, cites: [{source: S5, locator: "Vol. IV section"}], how_known: "Questionnaire answer, through Feferman."}
    - {value: "Turned to philosophy almost entirely from about 1943; intensive study of Leibniz, by his own report, 1943–1946; his theist statements read here all date from 1950 on", year: "1943–1946", certainty: 0.7, cites: [{source: S1, locator: "§1"}, {source: S6, locator: "letters 1950–1961"}], how_known: "SEP and the dated letters. Whether his theism began then or only became visible then is not known from the sources read."}
  coder_notes: "All worldview evidence is private: letters to his mother, an unsent questionnaire, notebooks and an unpublished proof. Nothing he published states a religious view, so no axis reaches 1.0. Two key lines (the Grandjean answer and the October 1961 letter) are secondary quotations; the 1961 July letter and others are in an IAS-approved translation. Mathematical platonism is well attested (S1, S2) and is recorded here rather than coded, following the PLATO guidance. Britannica says he 'subscribed to Platonism, theism, and mind-body dualism' (S2). No scholar read places him in CLASS_THEISM or CLTHEI, so primary_system is BELOW_THRESHOLD with both as candidates (lens audit, 2026-10-02); reading Wang 1996 and the Collected Works IV letters could settle it. mid_basin does not depend on the code: it uses only A and B."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "German-speaking Austrian of Moravia; father's family from Vienna, mother from the Rhineland", certainty: 1.0, cites: [{source: S2, locator: "Early life and career ('a German-speaking Austrian')"}, {source: S3, locator: "Biography"}], how_known: "Two sources."}
  religious_heritage_by_birth: {value: "Lutheran (Protestant), his mother's church, in a mainly Catholic setting", certainty: 0.7, cites: [{source: S7, locator: "Sect. 1"}], how_known: "One reliable, undisputed source (Todorov), so 0.7."}
  baptism_or_initiation: {value: "Baptized in a Lutheran congregation", certainty: 0.7, cites: [{source: S7, locator: "Sect. 1"}], how_known: "One reliable, undisputed source (Todorov), so 0.7; no date given."}
  childhood_catechism: {value: "Religion was a school subject; he did very well in it at the Gymnasium, but later wrote that his religion classes were poor", certainty: 0.7, cites: [{source: S1, locator: "§1 ('excelling especially in mathematics, languages and religion')"}, {source: S6, locator: "letter of 27 February 1950"}], how_known: "SEP and his own letter: 'with the kind we had, that would certainly not have been possible'."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1929–1949", certainty: 1.0, cites: [{source: S1, locator: "§1"}], how_known: "From the completeness theorem to the rotating-universe solutions."}
  age_at_first_lasting_contribution: {value: 23, certainty: 1.0, cites: [{source: S1, locator: "§3 ('at the age of twenty-three he opened his doctoral thesis')"}], how_known: "SEP; matches 1929 and a birth in April 1906."}
  first_evidence_of_lio_type_views: {value: "Letter to his mother arguing that no one can know there is no other world, because we do not know why this world exists or why it is as it is", year: 1950, certainty: 0.5, cites: [{source: S6, locator: "letter of 27 February 1950"}, {source: S5, locator: "Vol. IV section"}], how_known: "Earliest dated religious statement in the sources read. Earlier letters exist but were not read, so 0.5."}
  lio_views_relative_to_major_work: {value: "after major work", rationale: "The theist and lawful-order statements read date from 1950 on (the questionnaire from 1974 or later). His mathematical realism is said (by him, late) to date from 1925, but that is not an LIO view.", certainty: 0.5, cites: [{source: S6, locator: "letters 1950–1961"}, {source: S5, locator: "Vol. IV section"}], how_known: "Dated private writing; earlier writing not read."}
  worldview_during_major_work: {value: "Mathematical realism, by his own later account; he attended the Vienna Circle but was 'not himself a logical positivist'. No religious statement from 1929–1949 was found in the sources read.", certainty: 0.5, cites: [{source: S1, locator: "§1"}, {source: S6, locator: "letter of 15 August 1946"}], how_known: "SEP and his 1946 letter: he was 'in some regard even in direct opposition to the predominant views there'."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "His life's work is proof from axioms, and he carried it into philosophy and theology: 'There are systematic methods for the solution of all problems' (S1) and an axiomatic ontological proof (S8).", certainty: 0.5, cites: [{source: S1, locator: "§3.1"}, {source: S8, locator: "§9"}], how_known: "Coder's reading."}
  form_acquired: {value: "childhood or adolescence", rationale: "He had mastered university mathematics by the end of school (S3), before Hahn's logic.", certainty: 0.5, cites: [{source: S3, locator: "Biography"}], how_known: "His brother's account; when the deductive habit formed is not stated."}
  circle_present: {value: "no", rationale: "He rejected the God-equals-Nature identity in so many words: theistic, not pantheistic; Leibniz rather than Spinoza (S5).", certainty: 0.7, cites: [{source: S5, locator: "Vol. IV section"}], how_known: "His own words, through a secondary quotation."}
  reading: "As belief, not finding: the form is present and was acquired by adolescence; the circle is explicitly rejected. The record does not test H1."
  notes: ""

institutions:
  - {value: "University of Vienna", role: "student; Privatdozent", years: "1924–1939", kind: university, certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S3, locator: "Biography"}], how_known: "Two sources. The Privatdozentur (1933) was cancelled under the Nazi regime (S1)."}
  - {value: "Vienna Circle (Schlick's group)", role: "attended meetings", years: "c. 1926–1936", kind: other, certainty: 0.7, cites: [{source: S1, locator: "§1"}, {source: S6, locator: "letter of 15 August 1946"}], how_known: "SEP and his own letter; years approximate."}
  - {value: "Institute for Advanced Study, Princeton", role: "visiting member (1933–34, 1935, 1938); member 1940–1953; professor 1953–1976; emeritus", years: "1933–1978", kind: employer, certainty: 1.0, cites: [{source: S4, locator: "Visits"}, {source: S1, locator: "§1"}, {source: S3, locator: "Biography"}], how_known: "IAS page, with SEP and MacTutor (see flags on the permanent-member date)."}
  - {value: "University of Notre Dame", role: "visiting lecturer (spring term)", years: "1939", kind: university, certainty: 0.7, cites: [{source: S3, locator: "Biography"}], how_known: "MacTutor only."}

collaborators:
  - {value: "Hans Hahn", relation: teacher, note: "doctoral adviser; a leader of the Vienna Circle", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "Early life and career"}, {source: S3, locator: "Biography"}], how_known: "Three sources."}
  - {value: "Philipp Furtwängler", relation: teacher, note: "number theory lectures that turned him to mathematics", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S3, locator: "Biography"}], how_known: "Two sources."}
  - {value: "Rudolf Carnap", relation: teacher, note: "taught him logic", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "One source."}
  - {value: "Moritz Schlick", relation: "mentor or employer", note: "his seminar first drew Gödel to logic; Schlick's murder in 1936 led to a breakdown", certainty: 0.7, cites: [{source: S3, locator: "Biography"}, {source: S1, locator: "§1"}], how_known: "Two sources."}
  - {value: "Albert Einstein", roster_id: einstein-albert, relation: other, note: "close friend and daily walking partner at Princeton", years: "1940–1955", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S3, locator: "Biography"}, {source: S6, locator: "letter of 25 April 1955"}], how_known: "Three sources."}
  - {value: "John von Neumann", roster_id: von-neumann-john, relation: other, note: "friend at Princeton", certainty: 0.7, cites: [{source: S3, locator: "Biography"}], how_known: "One source."}
  - {value: "Oskar Morgenstern", relation: other, note: "friend at Princeton; diarist of his later years", certainty: 0.7, cites: [{source: S3, locator: "Biography"}, {source: S7, locator: "Sect. 3"}], how_known: "Two sources."}
  - {value: "Gottfried Wilhelm Leibniz", roster_id: leibniz-gottfried-wilhelm, relation: "influenced by", note: "his principal philosophical model; studied intensively 1943–1946", certainty: 1.0, cites: [{source: S1, locator: "§1; §3"}, {source: S5, locator: "Vol. IV section"}], how_known: "Two sources."}
  - {value: "Edmund Husserl", roster_id: husserl-edmund, relation: "influenced by", note: "phenomenology as a method for exact philosophy", certainty: 1.0, cites: [{source: S1, locator: "§3"}], how_known: "SEP."}
  - {value: "Immanuel Kant", roster_id: kant-immanuel, relation: "influenced by", note: "relativity and Kant's idea of time (1949 paper)", certainty: 0.7, cites: [{source: S1, locator: "§3"}, {source: S6, locator: "letter of 7 November 1947"}], how_known: "Two sources."}
  - {value: "Ernst Zermelo", relation: "rival or critic", note: "met at Bad Elster in 1931; felt he had already reached Gödel's result", certainty: 0.7, cites: [{source: S3, locator: "Biography"}], how_known: "MacTutor, quoting Taussky-Todd."}
  - {value: "Paul Cohen", relation: influenced, note: "built on Gödel's set-theory work to prove independence in 1963", certainty: 0.7, cites: [{source: S3, locator: "Biography"}], how_known: "MacTutor."}

review:
  roster_status_reason: {value: "Core in v7.1 (F 4) and v8 (F 5, all five models).", certainty: 0.7, cites: [{source: S9, locator: "roster.csv, rank 49"}], how_known: "Study roster (F_change_vs_v7 = +1)."}
  controversies:
    - {value: "Late-life paranoia: he believed he was being poisoned, ate only food his wife had tasted, and starved to death when she was in hospital", certainty: 1.0, cites: [{source: S2, locator: "Turn to philosophy"}, {source: S3, locator: "Biography"}, {source: S1, locator: "§1 (death certificate)"}], how_known: "Three sources."}
    - {value: "He believed Leibniz's writings had been systematically suppressed by his editors; Morgenstern could not explain the gaps Gödel showed him in the library", certainty: 0.7, cites: [{source: S7, locator: "Sect. 3"}], how_known: "Todorov, drawing on Dawson."}
  data_quality_flags:
    - "School leaving and university entry: MacTutor says he completed school in 1923 and entered Vienna in 1923; SEP and Todorov say 1924, and Britannica's 'Six years later' after 1918 also gives 1924."
    - "Doctorate: SEP, Britannica and MacTutor give 1929; the IAS page lists 'Ph.D. 1930'. The dissertation was published in 1930 (S2)."
    - "School marks: SEP says he excelled 'especially in mathematics'; Todorov (citing Dawson) says his only less-than-top mark was in mathematics. Both may hold."
    - "IAS posts: SEP says permanent member from 1946 and professor from 1953; the IAS page lists him as 'Member' from 1940 to 1953 without the 1946 change; MacTutor says he held a Princeton chair 'from 1953 until his death', while IAS and SEP give retirement in 1976."
    - "Continuum paper: SEP dates 'What is Cantor's Continuum Hypothesis?' to 1947; Britannica dates 'What Is Cantor's Continuum Problem?' to 1964. Probably the original and the revised version under one title; not settled from the sources read."
    - "Britannica's AI-generated 'Top Questions' box says he obtained the incompleteness theorem at the Institute for Advanced Study; the article body and every other source place it in Vienna (1931). The box is not used."
    - "Two English translations of the 23 July 1961 letter differ in wording (Feferman in S5 vs Reese/Budiansky in S6); statements use S6."
    - "The October 1961 letter reaches this record through three steps (Feferman's translation, posted by George Dyson, quoted by Todorov)."
    - "His questionnaire claim to have held mathematical realism since 1925 is, Feferman says, 'difficult to square with other evidence'."
  open_questions:
    - "Read the Grandjean questionnaire and the letters to his mother in Collected Works IV (2003) directly, to raise A and B above secondary quotation."
    - "Read Wang's Reflections on Kurt Gödel (1987) and A Logical Journey (1996) on whether his God is personal, and on religions versus religion (item 14), to score E and to settle CLASS_THEISM vs CLTHEI."
    - "Read Dawson's Logical Dilemmas (1997) for household religion in Brno."
    - "Read Engelen's paper on the Max Phil notebooks (HAL copy blocked by a bot check)."
    - "Check whether his theism appears in anything written before 1943."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Juliette Kennedy"
    year: 2025
    citation: "Kennedy, Juliette. \"Kurt Gödel.\" Stanford Encyclopedia of Philosophy, first published 13 February 2007, substantive revision 10 September 2025. https://plato.stanford.edu/entries/goedel/."
    url: "https://plato.stanford.edu/entries/goedel/"
    accessed: 2026-10-02
    reliability_note: "Peer-reviewed entry by a Gödel scholar. Quotes Wang's notes of conversations and the Nachlass list 'My Philosophical Viewpoint'."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators, review]
  - id: S2
    type: tertiary
    kind: encyclopedia
    author: "Mark Balaguer"
    citation: "Balaguer, Mark. \"Kurt Gödel.\" Encyclopaedia Britannica. Last updated September 17, 2026. https://www.britannica.com/biography/Kurt-Godel."
    url: "https://www.britannica.com/biography/Kurt-Godel"
    accessed: 2026-10-02
    reliability_note: "Signed article by a philosopher of mathematics; fact-checked. Its 'Top Questions' box is AI-generated and contains an error; it is not used."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, collaborators, review]
  - id: S3
    type: tertiary
    kind: encyclopedia
    author: "J. J. O'Connor and E. F. Robertson"
    year: 2003
    citation: "O'Connor, J. J., and E. F. Robertson. \"Kurt Gödel.\" MacTutor History of Mathematics Archive, University of St Andrews, last update October 2003. https://mathshistory.st-andrews.ac.uk/Biographies/Godel/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Godel/"
    accessed: 2026-10-02
    reliability_note: "University reference archive; quotes his brother Rudolf and Olga Taussky-Todd."
    used_for: [basics, contribution, childhood, heritage, lane_b, institutions, collaborators, review]
  - id: S4
    type: tertiary
    kind: "institutional page"
    author: "Institute for Advanced Study"
    citation: "Institute for Advanced Study. \"Kurt Gödel.\" Scholars. https://www.ias.edu/scholars/kurt-godel."
    url: "https://www.ias.edu/scholars/kurt-godel"
    accessed: 2026-10-02
    reliability_note: "His institute's own record of appointments, degrees and honours."
    used_for: [basics, contribution, institutions, review]
  - id: S5
    type: secondary
    kind: "journal article"
    author: "Solomon Feferman"
    year: 2004
    citation: "Feferman, Solomon. \"The Gödel Editorial Project: A synopsis.\" Paper, Stanford University (on completion of Kurt Gödel, Collected Works, vols. IV–V, Oxford University Press, 2003). http://math.stanford.edu/~feferman/papers/Goedel-Project-Synopsis.pdf."
    url: "http://math.stanford.edu/~feferman/papers/Goedel-Project-Synopsis.pdf"
    accessed: 2026-10-02
    reliability_note: "By the editor-in-chief of the Collected Works; quotes the letters to his mother and the Grandjean questionnaire from the edition. Year of the paper inferred from its text ('completion last year')."
    used_for: [worldview, timing, lane_b, collaborators, review]
  - id: S6
    type: primary
    kind: letter
    author: "Kurt Gödel (trans. Marilya Veteto Reese, ed. Stephen Budiansky)"
    citation: "Gödel, Kurt. Selected letters of Kurt Gödel to his mother (Marianne) and brother (Rudolf), 1940–1965. Translated by Marilya Veteto Reese, edited by Stephen Budiansky; reprinted with permission of the Institute for Advanced Study. Originals in the Wienbibliothek im Rathaus, Vienna. https://www.budiansky.com/LETTS.pdf."
    url: "https://www.budiansky.com/LETTS.pdf"
    accessed: 2026-10-02
    reliability_note: "English translations of his own private letters, published by his biographer with IAS permission. Excerpts only; ellipses are the editor's."
    used_for: [childhood, worldview, heritage, timing, institutions, collaborators]
  - id: S7
    type: secondary
    kind: "journal article"
    author: "Ivan Todorov"
    year: 2007
    citation: "Todorov, Ivan. Kurt Gödel and his universe. Talk at the IV International Conference 'Gravity, Astrophysics & Strings @ the Black Sea', Primorsko, June 2007. arXiv:0709.1387. https://arxiv.org/abs/0709.1387."
    url: "https://arxiv.org/pdf/0709.1387"
    accessed: 2026-10-02
    reliability_note: "Biographical portrait by a physicist, drawing on Dawson, Wang and Kreisel. Useful for details and one secondary quotation of the October 1961 letter; not peer-reviewed as history."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, review, collaborators]
  - id: S8
    type: tertiary
    kind: encyclopedia
    author: "Graham Oppy, Joshua Rasmussen and Joseph Schmid"
    year: 2024
    citation: "Oppy, Graham, Joshua Rasmussen and Joseph Schmid. \"Ontological Arguments.\" Stanford Encyclopedia of Philosophy, first published 8 February 1996, substantive revision 3 June 2024. https://plato.stanford.edu/entries/ontological-arguments/."
    url: "https://plato.stanford.edu/entries/ontological-arguments/"
    accessed: 2026-10-02
    reliability_note: "Peer-reviewed entry; §9 sets out a Gödelian ontological argument."
    used_for: [contribution, worldview, lane_b]
  - id: S9
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv and data/roster/person_ids.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
---

# Kurt Gödel

> Status: draft — unreviewed. Worldview BELOW_THRESHOLD (theist, following Leibniz; CLASS_THEISM and CLTHEI are candidates, no scholar places him in either). A, B, D scored at 0.7, C at 0.5, E TODO. mid_basin true under the P4 test.

## Summary

Kurt Gödel (1906–1978) was a logician from Brno who worked in Vienna and, from 1940, at the Institute for Advanced Study in Princeton [S1, §1]. He proved the completeness theorem (1929), the incompleteness theorems (1931) and the consistency of the axiom of choice and the continuum hypothesis with set theory [S1; S3]. SEP calls him one of the principal founders of the modern era in mathematical logic [S1].

## Life and work

He grew up in a well-off German-speaking family in Brno [S1; S3]. He studied physics, then mathematics, at the University of Vienna and took his doctorate under Hans Hahn in 1929 [S1]. He attended the Vienna Circle but was not a logical positivist [S1; S6]. After the Nazi takeover he lost his post and emigrated with his wife Adele in 1940 [S1]. At Princeton he was a close friend of Einstein, found rotating-universe solutions in relativity (1949) and turned mainly to philosophy [S1]. He died in 1978 after refusing to eat out of fear of poisoning [S1; S2; S3].

## Contribution and impact

- Completeness theorem for first-order logic (1929) [S1].
- Incompleteness theorems (1931) [S1; S2; S3].
- Consistency of the axiom of choice and the generalized continuum hypothesis (1935–1940) [S1; S4].
- Rotating universes in general relativity (1949) [S1; S7].

## Childhood and education

His father ran a textile firm; his mother was from the Rhineland and well educated [S3]. He was baptized Lutheran, his mother's church, in a Catholic setting [S7]. The family called him "Mr. Why" [S7]. He had rheumatic fever at 6 and read medical books at 8 [S3]. At the Brno Gymnasium he did best in mathematics, languages and religion [S1]. A book on Goethe, read at 15, led him to Goethe's colour theory and, he later wrote, indirectly to his profession [S6, 1946].

## Adult working worldview

He called his belief "theistic not pantheistic (following Leibniz rather than Spinoza)" [S5]. He wrote that science shows "the greatest regularity and order reign in everything" [S6, 1961], that the theological world view may be grasped by reason without faith [S7], and that there is an exact philosophy and theology [S1]. He argued for an afterlife as the completion of human possibilities [S6]. He wrote an ontological proof of God (1970) [S8]. His mathematical platonism is recorded but not coded as PLATO.

Coding: BELOW_THRESHOLD, with CLASS_THEISM and CLTHEI as candidates; no scholar read places him in either. A 1, B 3, D 3 at 0.7; C 3 at 0.5; E TODO. mid_basin true at 0.7; it uses only A and B, so it does not change.

## Heritage (context only)

German-speaking Austrian of Moravia; Lutheran by baptism [S2; S3; S7]. Heritage is recorded for context only. It is not a worldview code.

## Timing

First lasting contribution in 1929, at 23 [S1]. The religious and lawful-order statements read all date from 1950 or later, after the major work [S6; S5].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. The form (proof from axioms) is present and was acquired by adolescence [S3]. The circle is rejected in his own words: theistic, not pantheistic [S5].

## Open questions

- Read the Grandjean questionnaire and the mother letters in Collected Works IV.
- Read Wang 1987 and 1996 to score E and settle CLASS_THEISM vs CLTHEI.
- Read Dawson 1997 on household religion.
- Read Engelen on the Max Phil notebooks.

## Research log

- 2026-10-02: Read SEP (Kennedy, S1), Britannica (Balaguer, S2), MacTutor (S3), the IAS page (S4), Feferman's synopsis of the Collected Works (S5), the IAS-approved translations of his letters to his mother and brother (S6), Todorov's 2007 portrait (S7) and SEP Ontological Arguments §9 (S8). Wikipedia not used. Every quotation was checked word for word against the fetched text with a script (verify_quotes.py) before commit. Not read: Collected Works IV (print), Wang 1987 and 1996, Dawson 1997 (restricted lending only), Engelen's Max Phil paper (HAL bot check).
