---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch X)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Audit fixes for batch X (gs_a1ff932_X run 1): (RA2) the partition formula dated by its first printed notice, the Comptes rendus note of 2 January 1917 (new S5; P30 #1, the Gauss example): first lasting year 1918 -> 1917, span 1918–1920 -> 1917–1920 (still 0.5), age 31 -> 30 (P30 rule 5, event year − birth year; the audit's 29 is the age in completed years). Ruling X4 (v8's call on the auditor's advice): kept as coded (recorded under P42). No scored worldview value changes."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch X, order P32: F 4, rank 131). Basics from Britannica (Britannica Editors) and MacTutor (O'Connor and Robertson). Worldview only from others' reports: G. H. Hardy's Ramanujan (1940), lecture I, which quotes the Seshu Aiyar and Ramachandra Rao memoir and gives his own conflicting memory; Britannica's quotation from Kanigel. All reported speech (§7), so nothing scores. Not a scientist (P30: pure mathematics). primary_system BELOW_THRESHOLD (HINDU and AGNOS leads; RQ-X4); A, B BELOW_THRESHOLD; C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD. Span 1918–1920 (0.5). Not plotted. Draft, not reviewed."}

identity:
  id: ramanujan-srinivasa
  display_name: "Srinivasa Ramanujan"
  roster:
    canonical_name: "Srinivasa Ramanujan"
    rank: 131
    F: 4
    models: [Claude, Gemini, GPT, Grok]
    band: "core (3–4)"
    status: core
    field: mathematics
    field_bucket: mathematics
  full_name: {value: "Srinivasa Ramanujan", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Quick Info"}], how_known: "Both sources."}
  native_name: {value: "Srinivasa Ramanujan", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Tamil name in the sources' romanization; the Tamil script is not given."}
  aliases:
    - {name: "Ramanujan-Srinivasa", kind: "roster alias"}
    - {name: "Srinivasa-Ramanujan", kind: "roster alias"}

basics:
  birth:
    date: {value: "1887-12-22", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Quick Facts (Born)"}, {source: S2, locator: "Quick Info"}], how_known: "Both sources."}
    place: {value: "Erode", modern_name: "Erode, Tamil Nadu, India", polity_then: "British India (Madras Presidency)", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts (Born)"}, {source: S2, locator: "Quick Info; opening ('in his grandmother's house in Erode')"}], how_known: "Both sources; polity the coder's reading."}
  death:
    date: {value: "1920-04-26", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Quick Facts (Died)"}, {source: S2, locator: "Quick Info"}], how_known: "Both sources."}
    place: {value: "Kumbakonam", modern_name: "Kumbakonam, Tamil Nadu, India", polity_then: "British India (Madras Presidency)", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts (Died)"}, {source: S2, locator: "Quick Info"}], how_known: "Both sources."}
  first_lasting_contribution_year: {value: 1917, certainty: 0.5, cites: [{source: S5, locator: "séance du 2 janvier 1917, pp. 35–38"}, {source: S2, locator: "partition paragraph ('Perhaps his most famous work was on the number p(n)... In a joint paper with Hardy, Ramanujan gave an asymptotic formula')"}, {source: S1, locator: "opening; 'Further advances'"}], how_known: "The Hardy–Ramanujan asymptotic formula for p(n), first stated in print in their Comptes rendus note of 2 January 1917 (S5), which the Proc. London Math. Soc. paper of 1918 footnotes; dated by that printed notice under P30 #1 (the Gauss example; batch X audit, RA2). Neither MacTutor nor Britannica gives a year, so 0.5. Earlier work (the 1911 Bernoulli paper, MacTutor: 'he gained recognition') is not called lasting; Ramanujan summation is undated in the sources (P39)."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S2, locator: "Quick Info"}], how_known: "His whole adult life (1905–1920) falls in this bucket (P2, P39)."}
  region_of_birth: {value: "South Asia", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S2, locator: "Quick Info"}], how_known: "India (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.5, cites: [{source: S2, locator: "Cambridge paragraphs"}, {source: S1, locator: "'The Hardy–Ramanujan collaboration'"}], how_known: "The lasting work was done at Cambridge, 1914–1919 (coder's call); earlier and last-year work in India (South Asia)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S2, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S2, locator: "letters quoted"}], how_known: "His letters and papers are in English."}
  occupations: {value: ["mathematician", "clerk, Madras Port Trust (1912–1914)", "Fellow of Trinity College, Cambridge (1918)"], certainty: 0.7, cites: [{source: S2, locator: "Port Trust and Royal Society paragraphs"}], how_known: "MacTutor."}

contribution:
  fields: {value: ["number theory", "infinite series", "continued fractions", "elliptic functions"], certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Summary"}], how_known: "Both sources."}
  lasting_original_contributions:
    - {value: "Asymptotic formula for the partition function p(n) (with G. H. Hardy), and properties of p(n)", year: 1917, kind: "law or principle", lasting: "'Perhaps his most famous work was on the number p(n)'; the formula 'was later proved by Rademacher' (S2); 'pioneering discoveries of the properties of the partition function' (S1)", certainty: 0.5, cites: [{source: S2, locator: "partition paragraph"}, {source: S1, locator: "Top Questions; 'Further advances'"}, {source: S5, locator: "séance du 2 janvier 1917, pp. 35–38"}], how_known: "Both sources; the year is from the first printed notice, the Comptes rendus note of 2 January 1917 (S5; P30 #1; batch X audit, RA2), not given in either. Pure mathematics, so not a scientist (P30)."}
    - {value: "Mock theta (mock modular) functions, described in his last letter to Hardy", year: 1920, kind: discovery, lasting: "theory confirmed in 2012 by researchers led by Ken Ono (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Health struggles, legacy, and posthumous discoveries'"}], how_known: "Britannica. Latest dated item, so it ends the span (P30 addendum b)."}
    - {value: "Notebooks and the 'lost notebook' of unpublished results", kind: "body of work", lasting: "results 'that mathematicians continued to verify long after his death' (S1); G. N. Watson published nearly 30 papers inspired by them (S2)", certainty: 0.7, cites: [{source: S1, locator: "legacy paragraph"}, {source: S2, locator: "closing paragraph"}], how_known: "Both sources; undated as a body, so it sets no span (P39)."}
  evidence_of_impact:
    - {value: "Compared with Euler and Jacobi as 'a phenomenal genius'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "Top Questions; legacy paragraph"}], how_known: "Britannica."}
    - {value: "Fellow of the Royal Society (1918)", kind: "honours in lifetime", certainty: 1.0, cites: [{source: S1, locator: "'Further advances'"}, {source: S2, locator: "Royal Society paragraph"}], how_known: "Both sources."}
  major_works:
    - {value: "Paper on Bernoulli numbers, Journal of the Indian Mathematical Society", year: 1911, kind: "paper or paper series", certainty: 1.0, cites: [{source: S1, locator: "'Foundational work'"}, {source: S2, locator: "1911 paragraph"}], how_known: "Both sources."}
    - {value: "Highly composite numbers (Cambridge BA by research dissertation)", year: 1916, kind: "paper or paper series", certainty: 0.7, cites: [{source: S2, locator: "1916 paragraph"}], how_known: "MacTutor."}
  honours:
    - {value: "Fellow of the Royal Society", year: 1918, certainty: 1.0, cites: [{source: S1, locator: "'Further advances'"}, {source: S2, locator: "Royal Society paragraph"}], how_known: "Both sources."}
    - {value: "Fellow of Trinity College, Cambridge", year: 1918, certainty: 0.7, cites: [{source: S2, locator: "Royal Society paragraph"}], how_known: "MacTutor."}
  definition_fit: {value: "clearly meets", rationale: "'without peer since Leonhard Euler... and Carl Jacobi' (S1).", certainty: 0.7, cites: [{source: S1, locator: "Top Questions"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Hindu (Brahmin)", certainty: 1.0, cites: [{source: S1, locator: "'Early life' ('a poor Brahmin family')"}, {source: S3, locator: "lecture I, p. 2 ('in a Brahmin family')"}], how_known: "Britannica and Hardy."}
  family_religious_practice: {value: "Orthodox Brahmin observance; he promised his parents to keep the observances of his caste in England", certainty: 0.5, cites: [{source: S3, locator: "lecture I, p. 4"}], how_known: "Hardy's account."}
  parents_and_household:
    - {value: "Father: a clerk in a cloth merchant's shop in Kumbakonam", certainty: 0.7, cites: [{source: S2, locator: "opening"}], how_known: "MacTutor."}
    - {value: "Mother took him to Kumbakonam at age one; arranged his marriage (1909) to S. Janaki Ammal", certainty: 0.7, cites: [{source: S2, locator: "opening; 1909 paragraph"}], how_known: "MacTutor."}
  household_circumstances: {value: "Poor Brahmin family in Kumbakonam", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}, {source: S2, locator: "opening"}], how_known: "Both sources."}
  schooling:
    - {value: "Primary schools in Kumbakonam", stage: "elementary school", run_by: other, years: "from c. 1892", certainty: 0.7, cites: [{source: S2, locator: "opening ('nearly five years old')"}], how_known: "MacTutor; several schools, names not given."}
    - {value: "Town High School, Kumbakonam", stage: "grammar or secondary school", run_by: other, years: "1898–1904", certainty: 0.7, cites: [{source: S2, locator: "opening"}], how_known: "MacTutor; end year from the 1904 scholarship."}
    - {value: "Government College, Kumbakonam (scholarship lost after a year)", stage: university, run_by: "state or municipal", years: "1904–1905", certainty: 0.5, cites: [{source: S2, locator: "1904 paragraph"}, {source: S1, locator: "'Early life' (scholarship 1903, 'University of Madras')"}], how_known: "MacTutor; Britannica dates the scholarship 1903 and names the University of Madras (conflict, so 0.5)."}
    - {value: "Pachaiyappa's College, Madras (left after illness; failed the First Arts examination)", stage: university, run_by: other, years: "1906", certainty: 0.7, cites: [{source: S2, locator: "1906 paragraph"}], how_known: "MacTutor."}
    - {value: "Trinity College, Cambridge (BA by research, 1916)", stage: university, run_by: other, years: "1914–1916", certainty: 0.7, cites: [{source: S2, locator: "Cambridge paragraphs"}], how_known: "MacTutor."}
  early_mathematics: {value: "advanced mathematics", certainty: 0.7, cites: [{source: S2, locator: "opening (quartic, Carr's Synopsis, Euler's constant by 1904)"}, {source: S1, locator: "'Early life'"}], how_known: "Both sources."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading:
    - {value: "G. S. Carr, Synopsis of Elementary Results in Pure and Applied Mathematics (2 vols., 1880–86)", certainty: 1.0, cites: [{source: S1, locator: "'Early life'"}, {source: S2, locator: "opening"}], how_known: "Both sources."}
  childhood_mentors: []
  languages_in_childhood: {value: ["Tamil"], certainty: 0.5, cites: [{source: S2, locator: "opening"}], how_known: "Coder's reading (Tamil Nadu); not stated."}
  notable_events:
    - {value: "Smallpox", year: 1889, certainty: 0.7, cites: [{source: S2, locator: "opening"}], how_known: "MacTutor."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1917–1920", certainty: 0.5, cites: [{source: S2, locator: "partition paragraph"}, {source: S1, locator: "legacy paragraph"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Orthodox high-caste Hindu observance: 'always adhered ... to all the observances of his caste'; strict vegetarian", certainty: 0.7, cites: [{source: S3, locator: "lecture I, p. 4"}, {source: S2, locator: "Cambridge paragraph ('an orthodox Brahmin')"}], how_known: "Hardy and MacTutor; practice at membership level, not a profession."}
  self_described_science_religion_relation: {value: BELOW_THRESHOLD, how_known: "Only reported: 'An equation for me has no meaning unless it expresses a thought of God', quoted by Britannica from Kanigel's 1991 biography (S1), whose own source was not read (§7)."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "Reported speech only, and the two witnesses Hardy quotes 'contradict one another flatly' (S3). Seshu Aiyar and Ramachandra Rao: 'Ramanujan had definite religious views. He had a special veneration for the Namakkal goddess. He believed in the existence of a Supreme being and in the attainment of Godhead by men'. Hardy (pp. 4–5): 'his religion was a matter of observance and not of intellectual conviction, and I remember well his telling me (much to my surprise) that all religions seemed to him more or less equally true', calling him an 'agnostic' in its strict sense. Observance is membership level (nominal_affiliations). Leads HINDU and AGNOS (RQ-X4)."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: HINDU, reason: "Lead: observance and the Namakkal goddess (Seshu Aiyar and Rao, via S3, p. 3); reported."}
    - {code: AGNOS, reason: "Lead: Hardy's memory that he 'had no definite beliefs' (S3, p. 4); reported."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "Reported speech only (§7): belief 'in the existence of a Supreme being' (Seshu Aiyar and Rao) against 'no definite beliefs' (Hardy) (S3). Neither scores alone."}
    B_cause: {value: BELOW_THRESHOLD, how_known: "Not a scientist (P30: pure mathematics), so B needs a statement on nature (P16). Only a view on mathematical truth is reported ('An equation for me has no meaning unless it expresses a thought of God', S1 quoting Kanigel; 'the goddess of Namakkal inspired him with the formulae in dreams', Seshu Aiyar and Rao via S3), which gives BELOW_THRESHOLD under P16, and it is reported speech in any case."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read; 'settled convictions about the problem of life and after' (S3) names no content (P19)."}
    D_authority: {value: UNKNOWN, how_known: "Nothing read (P19)."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7, P19)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A and B both BELOW_THRESHOLD (P19)."}
  statements:
    - text: "his religion was a matter of observance and not of intellectual conviction, and I remember well his telling me (much to my surprise) that all religions seemed to him more or less equally true"
      cites: [{source: S3, locator: "lecture I, p. 4 (quoting his own memoir in the Collected Papers)"}]
      date: "1940"
      context: "Hardy sets his memory against the memoir by Seshu Aiyar and Ramachandra Rao in the Collected Papers and concludes he was 'not a reasoned infidel, but an \"agnostic\" in its strict sense'."
      axes: [A_locus]
      kind: "reported speech"
      verified_against: "secondary quotation"
      verified_on: 2026-10-19
      note: "Read in the Digital Library of India scan's OCR on archive.org; wording checked against the OCR, which is noisy. Hardy's report of a conversation (§7)."
    - text: "Ramanujan had definite religious views. He had a special veneration for the Namakkal goddess. He believed in the existence of a Supreme being and in the attainment of Godhead by men."
      cites: [{source: S3, locator: "lecture I, p. 4 (quoting Seshu Aiyar and Ramachandra Rao)"}]
      date: "1940"
      context: "The Indian memoir (Collected Papers, 1927) as Hardy quotes it, with an ellipsis after 'goddess'."
      axes: [A_locus]
      kind: "reported speech"
      verified_against: "secondary quotation"
      verified_on: 2026-10-19
      note: "As above; the ellipsis in Hardy's quotation is not marked here beyond this note."
    - text: "An equation for me has no meaning unless it expresses a thought of God."
      cites: [{source: S1, locator: "'Further advances and philosophical reflections'"}]
      context: "Quoted by Britannica from Robert Kanigel, The Man Who Knew Infinity (1991); Kanigel's source not read."
      axes: [B_cause]
      kind: "reported speech"
      verified_against: "secondary quotation"
      verified_on: 2026-10-19
      note: "Undated; a lead only."
  changes_over_life: []
  coder_notes: "Coder's call on the span: 1917 (Hardy–Ramanujan asymptotic formula, MacTutor's 'most famous work'; dated by the Comptes rendus note of 2 January 1917, P30 #1, batch X audit RA2; the full paper is Proc. LMS 1918) to 1920 (mock theta functions, Britannica). Both sources leave earlier items undated or not called lasting. Not a scientist (P30): partitions, series and modular forms are pure mathematics; Ono's black-hole remark (S1) is about later uses. His own letters (Berndt and Rankin 1995) and Kanigel's biography were not read; all religious evidence is reported, and Hardy and the Indian memoirists disagree (RQ-X4; ruling X4 keeps the record as coded)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Tamil Brahmin", certainty: 0.5, cites: [{source: S1, locator: "'Early life'"}, {source: S2, locator: "opening"}], how_known: "Brahmin from both sources; 'Tamil' from the birthplace (coder's reading)."}
  religious_heritage_by_birth: {value: "Hinduism (Brahmin)", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}, {source: S3, locator: "lecture I, p. 2"}], how_known: "Britannica and Hardy."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1917–1920", certainty: 0.5, cites: [{source: S2, locator: "partition paragraph"}, {source: S5, locator: "séance du 2 janvier 1917, pp. 35–38"}, {source: S1, locator: "legacy paragraph"}], how_known: "From the partition formula (1917, Comptes rendus note; P30 #1) to the mock theta functions (1920) (P12, P30)."}
  age_at_first_lasting_contribution: {value: 30, certainty: 0.5, cites: [{source: S1, locator: "Quick Facts"}, {source: S5, locator: "séance du 2 janvier 1917, pp. 35–38"}], how_known: "1917 − 1887 = 30 (P30 rule 5: event year − birth year, no month adjustment). The batch X audit's '29' is his age in completed years on 2 January 1917 (born 22 December 1887); P30 gives 30."}
  first_evidence_of_lio_type_views: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S3, locator: "lecture I, pp. 4–5"}], how_known: "Nothing scored."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S3, locator: "lecture I, pp. 4–5"}], how_known: "As above."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Only reported, conflicting accounts."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S2, locator: "text"}], how_known: "Not assessed."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "text"}], how_known: "Not assessed."}
  circle_present: {value: "unclear", rationale: "Britannica reports a 'personal theory of reality centered on zero and infinity' (unsourced in the article).", certainty: 0.5, cites: [{source: S1, locator: "'Further advances and philosophical reflections'"}], how_known: "Coder's reading."}
  reading: "Formulae as gifts of the goddess, in reported accounts."
  notes: ""

institutions:
  - {value: "Madras Port Trust", role: "clerk in the accounts section", years: "1912–1914", kind: employer, certainty: 0.7, cites: [{source: S2, locator: "Port Trust paragraph"}], how_known: "MacTutor; end year from his departure in 1914."}
  - {value: "University of Madras", role: "research scholarship", years: "1913–1914", kind: university, certainty: 0.7, cites: [{source: S2, locator: "1913 paragraph"}], how_known: "MacTutor."}
  - {value: "Trinity College, Cambridge", role: "research student; Fellow from 1918", years: "1914–1919", kind: university, certainty: 0.7, cites: [{source: S2, locator: "Cambridge paragraphs"}], how_known: "MacTutor."}
collaborators:
  - {value: "G. H. Hardy", relation: collaborator, note: "brought him to Cambridge; joint work on partitions", certainty: 1.0, cites: [{source: S1, locator: "'The Hardy–Ramanujan collaboration'"}, {source: S2, locator: "Hardy paragraphs"}], how_known: "Both sources."}
  - {value: "J. E. Littlewood", relation: collaborator, note: "asked to teach him rigorous methods", certainty: 0.7, cites: [{source: S2, locator: "Littlewood paragraph"}], how_known: "MacTutor."}
  - {value: "E. H. Neville", relation: other, note: "helped arrange his travel and hosted him in Cambridge", certainty: 0.7, cites: [{source: S2, locator: "1914 paragraph"}], how_known: "MacTutor."}
  - {value: "R. Ramachandra Rao", relation: "mentor or employer", note: "patron; supported his research for a time", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}, {source: S2, locator: "Ramachandra Rao paragraph"}], how_known: "Both sources."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 131"}], how_known: "Study roster."}
  controversies:
    - {value: "Hardy and the Indian memoirists disagree on his religious beliefs", certainty: 0.7, cites: [{source: S3, locator: "lecture I, pp. 4–5"}], how_known: "Hardy."}
  data_quality_flags:
    - "All worldview evidence is reported speech; Hardy read in a noisy OCR."
    - "The partition formula is dated 1917 from the Comptes rendus note (S5); neither biography dates it."
  open_questions:
    - "Ruling X4: kept as coded (HINDU and AGNOS leads). Open lead: his own letters (Berndt and Rankin) and Kanigel."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Britannica Editors (revised by Anoushka Pant)"
    citation: "Britannica Editors. \"Srinivasa Ramanujan.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Srinivasa-Ramanujan. Read live 2026-10-19."
    url: "https://www.britannica.com/biography/Srinivasa-Ramanujan"
    accessed: 2026-10-19
    reliability_note: "Editors' article, most recently revised by Anoushka Pant; no update date shown. Body cited; Top Questions used only where the body or MacTutor agrees."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, collaborators]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "J. J. O'Connor and E. F. Robertson (MacTutor)"
    citation: "O'Connor, J. J., and E. F. Robertson. \"Srinivasa Ramanujan.\" MacTutor History of Mathematics, University of St Andrews (last update June 1998). https://mathshistory.st-andrews.ac.uk/Biographies/Ramanujan/"
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Ramanujan/"
    accessed: 2026-10-19
    reliability_note: "Signed biography."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, institutions, collaborators, lane_b]
  - id: S3
    type: secondary
    kind: "scholarly book"
    author: "G. H. Hardy"
    citation: "Hardy, G. H. Ramanujan: Twelve Lectures on Subjects Suggested by His Life and Work. Cambridge: Cambridge University Press, 1940. Lecture I, 'The Indian mathematician Ramanujan'. Digital Library of India scan, Internet Archive in.ernet.dli.2015.212059."
    url: "https://archive.org/details/in.ernet.dli.2015.212059"
    accessed: 2026-10-19
    reliability_note: "His collaborator's memoir; his reports of Ramanujan's words are reported speech (§7). Read in a noisy OCR; page numbers from the printed headers."
    used_for: [childhood, worldview, heritage, timing, review]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [identity, review]
  - id: S5
    type: primary
    kind: "journal article"
    author: "G. H. Hardy and S. Ramanujan"
    citation: "Hardy, G. H., and S. Ramanujan. \"Une formule asymptotique pour le nombre des partitions de n.\" Comptes rendus hebdomadaires des séances de l'Académie des sciences 164 (séance du 2 janvier 1917): 35–38. Read on French Wikisource (tome 164, djvu p. 35) and in the Ramanujan Papers web edition (ram31)."
    url: "https://fr.wikisource.org/wiki/Page:Comptes_rendus_hebdomadaires_des_s%C3%A9ances_de_l%E2%80%99Acad%C3%A9mie_des_sciences,_tome_164,_1917.djvu/35"
    accessed: 2026-10-19
    reliability_note: "The printed note itself (web transcription); used only to date the partition formula (batch X audit, RA2)."
    used_for: [basics, contribution, timing]
---

# Srinivasa Ramanujan

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Srinivasa Ramanujan (1887–1920), Indian mathematician [S1, S2]. Draft: primary_system BELOW_THRESHOLD; A and B BELOW_THRESHOLD (reported speech only); mid_basin BELOW_THRESHOLD. Not plotted.

## Life and work

Kumbakonam and Madras; Cambridge with Hardy, 1914–1919 [S2].

## Contribution and impact

Partition function, mock theta functions, notebooks [S1, S2].

## Childhood and education

Poor Brahmin family; Carr's Synopsis [S1, S2].

## Adult working worldview

Reported only, and the witnesses disagree [S3].

## Heritage (context only)

Brahmin [S1].

## Timing

1917–1920, from age 30 [S1, S2, S5].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Not assessed [S1].

## Open questions

- RQ-X4, settled by ruling X4 (kept as coded).

## Research log

- 2026-10-19: Read Britannica, MacTutor and Hardy's Ramanujan (1940), lecture I.
