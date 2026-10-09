---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch C)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-08
  last_updated: 2026-10-08
  change_log:
    - {date: 2026-10-08, by: "Grok Bot", summary: "Record created (stage 3 batch C; the last uncoded person in the physical-science 1600–1950 pool with F ≥ 3, taken first under P32). Basics from Britannica (editors), the Linda Hall Library and Yu Shi's 2025 paper; dates of the three listed experiments from the APS journal records. No statement by Wu on religion, God or nature was found. primary_system UNKNOWN; B_cause 4 at 0.5 from working science (P24); A, C, D UNKNOWN; E BELOW_THRESHOLD (P19); mid_basin UNKNOWN. Draft, not reviewed."}

identity:
  id: wu-chien-shiung
  display_name: "Chien-Shiung Wu"
  roster:
    canonical_name: "Chien-Shiung Wu"
    rank: 17
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: physics
    field_bucket: physics
  full_name: {value: "Chien-Shiung Wu", certainty: 1.0, cites: [{source: S1, locator: "heading; opening sentence"}, {source: S2, locator: "opening sentence"}], how_known: "Two sources give the same form."}
  native_name: {value: TODO}
  aliases:
    - {name: "Chien-Shiung-Wu", kind: "roster alias"}
    - {name: "Wu-Chien-Shiung", kind: "roster alias"}

basics:
  birth:
    date:
      value: "1912-05-31"
      calendar: gregorian
      certainty: 0.5
      cites: [{source: S2, locator: "opening sentence ('born May 31, 1912')"}]
      how_known: "The sources read give two different days for the same birth, so 0.5 (real dispute, P25, P30). May 31 is kept as the value because the 110th-anniversary symposium was held on 31 May 2022 (S3, abstract); the year is 1912 in every source."
      alternatives:
        - {value: "1912-05-29", cites: [{source: S1, locator: "Born line; opening sentence"}], note: "Britannica (editors)."}
    place: {value: "Liuhe, Jiangsu province", modern_name: "Liuhe, Jiangsu, China", polity_then: "Republic of China", certainty: 1.0, cites: [{source: S1, locator: "Born line"}, {source: S2, locator: "opening sentence ('Jiangsu province, China')"}], how_known: "Britannica names Liuhe; the Linda Hall page gives the province. Two sources agree on the province; the town is Britannica's."}
  death:
    date: {value: "1997-02-16", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "Died line"}], how_known: "Britannica alone gives the day; the Linda Hall page gives only the year 1997. One source for the day, so 0.7 (P15)."}
    place: {value: "New York, New York", modern_name: "New York City, USA", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "Died line"}], how_known: "Britannica alone, so 0.7 (P15)."}
  first_lasting_contribution_year:
    value: 1949
    certainty: 1.0
    cites: [{source: S4, locator: "APS record: 'Received 21 November 1949'"}, {source: S3, locator: "§2 ('In 1949, Wu and her student Irving Shaknov studied ...')"}]
    how_known: "The Wu–Shaknov annihilation-radiation experiment, the earliest listed lasting contribution, was formally submitted on 21 November 1949 and published on 1 January 1950 (S4). Under P30 a formal submission is a documented public statement, so the year is 1949. Primary journal record plus Shi, so 1.0."
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S4, locator: "APS record (received 1949)"}, {source: S3, locator: "§2"}], how_known: "From 1949 under P2. Note: dating by first publication (1950) would give '1950 on'; P30 dates by the formal submission, so the bucket follows the rule, not a source conflict."}
  region_of_birth: {value: "East Asia", certainty: 1.0, cites: [{source: S1, locator: "Born line"}, {source: S2, locator: "opening sentence"}], how_known: "China is East Asia in data/reference/regions.csv (P3)."}
  region_of_work: {value: "North America", certainty: 1.0, cites: [{source: S1, locator: "paragraph 2 (Berkeley, Smith College, Princeton, Columbia)"}, {source: S3, locator: "§1"}], how_known: "All listed work was done at Columbia University, New York."}
  sex_as_recorded: {value: "female", certainty: 1.0, cites: [{source: S1, locator: "paragraph 2 ('she')"}, {source: S2, locator: "opening"}], how_known: "As the sources record it."}
  languages_of_work: {value: [English], certainty: 1.0, cites: [{source: S4, locator: "paper title"}, {source: S5, locator: "paper title"}], how_known: "Her papers are in English (Physical Review)."}
  occupations: {value: ["experimental physicist", "university professor"], certainty: 1.0, cites: [{source: S1, locator: "opening; paragraph 2 (Pupin professor 1957)"}, {source: S2, locator: "opening"}], how_known: "Two sources."}

contribution:
  fields: {value: ["nuclear physics", "beta decay", "weak interaction", "experimental physics"], certainty: 1.0, cites: [{source: S1, locator: "Subjects of study; opening"}, {source: S2, locator: "beta-decay paragraph"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Wu–Shaknov experiment: precise measurement of the angular correlation of scattered annihilation radiation, confirming the QED prediction that the two photons are polarized at right angles; later recognised as the first controlled production of spatially separated entangled photons", year: "1949", kind: discovery, lasting: "standard test of QED; Bohm and Aharonov (1957) used it as the experimental case of entanglement (S3, §4)", certainty: 1.0, cites: [{source: S4, locator: "APS record (title, received 21 November 1949)"}, {source: S3, locator: "§§2–4"}], how_known: "Primary journal record for the date; Shi for the content and the later reading."}
    - {value: "Experimental proof that parity is not conserved in the weak interaction (cobalt-60 beta decay, with the National Bureau of Standards group)", year: "1957", kind: discovery, lasting: "overturned parity conservation; basis of the modern theory of the weak interaction", certainty: 1.0, cites: [{source: S5, locator: "APS record (received 15 January 1957; published 15 February 1957)"}, {source: S1, locator: "paragraph 3"}, {source: S2, locator: "parity paragraphs"}], how_known: "The experiment ran in late 1956 (S1, S2); the earliest documented public statement read is the formal submission of 15 January 1957 (S5), so 1957 under P30."}
    - {value: "Experimental confirmation of the conserved vector current (CVC) theory in nuclear beta decay (beta spectra of B-12 and N-12, with Y. K. Lee and L. W. Mo)", year: "1963", kind: discovery, lasting: "confirmed the Feynman–Gell-Mann CVC hypothesis, part of the V−A theory", certainty: 1.0, cites: [{source: S6, locator: "APS record (received 4 February 1963)"}, {source: S1, locator: "paragraph 3 ('experimentally confirmed in 1963 by Wu')"}], how_known: "Primary journal record and Britannica."}
  evidence_of_impact:
    - {value: "Lee and Yang won the 1957 Nobel Prize for Physics after her experiment and similar ones confirmed their proposal", kind: "other", certainty: 0.7, cites: [{source: S1, locator: "paragraph 3"}], how_known: "Britannica."}
    - {value: "The cobalt-60 test is known as 'the Wu experiment'", kind: "named after them", certainty: 0.7, cites: [{source: S2, locator: "parity paragraph ('the Wu experiment of 1956, as it is still called')"}], how_known: "Linda Hall page."}
  major_works:
    - {value: "Experimental Test of Parity Conservation in Beta Decay (with E. Ambler, R. W. Hayward, D. D. Hoppes and R. P. Hudson), Physical Review 105, 1413", year: 1957, kind: "paper or paper series", certainty: 1.0, cites: [{source: S5, locator: "APS record"}], how_known: "Primary journal record."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "First experimental proof of parity violation in the weak interaction; earlier precise test of QED with entangled photons.", certainty: 1.0, cites: [{source: S1, locator: "opening sentence"}, {source: S3, locator: "§§2–3"}], how_known: "Two sources."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Britannica, the Linda Hall page and Shi's two papers say nothing on the family's religion."}
  family_religious_practice: {value: UNKNOWN, how_known: "Same sources; nothing found."}
  parents_and_household:
    - {value: "Father founded the first school she attended and believed strongly that women deserved equal opportunities for education", role: father, certainty: 0.7, cites: [{source: S2, locator: "opening paragraph"}], how_known: "Linda Hall page alone, so 0.7 (P15); the father's name is not given there."}
  household_circumstances: {value: TODO}
  schooling:
    - {value: "A school founded by her father", stage: "elementary school", run_by: family, certainty: 0.7, cites: [{source: S2, locator: "opening paragraph"}], how_known: "Linda Hall page; the school's name and level are not given there, so stage is the coder's reading of 'the first school she attended'."}
    - {value: "National Central University, Nanjing; graduated 1934; thesis on the Bragg equation under Shih-Yuan Sze", stage: university, run_by: "state or municipal", years: "1930–1934", ages: "18–22", certainty: 0.7, cites: [{source: S1, locator: "paragraph 2 (graduated 1934)"}, {source: S3, locator: "§1 (1930 to 1934; thesis)"}], how_known: "Two sources agree on 1934; the start year and the thesis are Shi's alone, so 0.7 for the entry. 'State' for the run_by is the coder's reading of a national university."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: TODO}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1949–1963", certainty: 1.0, cites: [{source: S4, locator: "APS record (1949)"}, {source: S6, locator: "APS record (1963)"}], how_known: "Equals timing.major_work_period: first to last listed lasting contribution (P29, P30)."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No statement of hers on science and religion was found in Britannica, the Linda Hall page, Shi's two papers or a web search for her religious views (2026-10-08)."}
  primary_system:
    value: UNKNOWN
    cites: [{source: S1, locator: "whole article"}, {source: S2, locator: "whole page"}, {source: S3, locator: "whole paper"}]
    how_known: "Searched Britannica, the Linda Hall page, Shi (MPLA 2025) and the web for any statement of hers on religion, God or nature; none found. Under P19 the sources say nothing on the point, so UNKNOWN."
    note: "Leads: Chiang Tsai-Chien, Madame Wu Chien-Shiung (World Scientific, 2014), based on interviews with her from 1989; the NAS Biographical Memoir by Noémie Benczer-Koller (2009; the PDF was blocked to the fetch on 2026-10-08)."
  secondary_system: {value: UNKNOWN, how_known: "No system evidence in what was read."}
  candidate_codes_considered: []
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing of hers on God or the divine in the sources read (P19)."}
    B_cause:
      value: 4
      basis: inference_from_work
      certainty: 0.5
      cites: [{source: S5, locator: "APS record (parity test)"}, {source: S3, locator: "§2 (precision test of a theoretical prediction)"}, {source: S2, locator: "parity paragraphs"}]
      how_known: "Coder's reading of her working science, as P24 and P30 direct for a scientist (same treatment as Fermi and Libby). No statement of her own about miracles or exceptions was read, so 0.5."
      rationale: "Scored on her account of nature (P6), which for a scientist is the working science. Her experiments test whether nature follows stated laws without exception: QED's polarization prediction (S3) and parity symmetry, which she found violated in the weak interaction (S2, S5). Finding that a symmetry fails is a finding about which law holds, not an exception to lawfulness. No miracle, petition or exemption appears in anything read."
    C_ledger: {value: UNKNOWN, how_known: "Nothing of hers on judgement, reward or afterlife in the sources read (P19)."}
    D_authority: {value: UNKNOWN, how_known: "Nothing on revelation or scripture. Working science does not bear on D (P19), so UNKNOWN."}
    E_scope: {value: BELOW_THRESHOLD, note: "Scored on the world's order (P7). Her working science assumes the same laws for every nucleus, which bears on E's first question, but E is not scored from working science alone (P19, P30 addendum).", how_known: "BELOW_THRESHOLD under P19: not scored from working science alone."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, so the P4 test cannot be applied; UNKNOWN takes precedence (§6, P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "statements is empty because no religious or metaphysical statement of hers was found. Her 1964 MIT remark on whether atoms and nuclei 'have any preference for either masculine or feminine treatment' was seen only on Wikipedia (a lead, not citable) and is about gender, not God or nature. Shi's two papers are by one author, so they count as one source. The APS records (S4–S6) were read as record pages (title, authors, received and published dates); the full texts were not read. Coder's call (CODING_GUIDE §8): the first-lasting year is the 1949 submission date under P30, not the 1950 publication; this moves the era bucket from '1950 on' to '1850 to 1949'."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Han Chinese", certainty: 0.5, cites: [{source: S1, locator: "opening ('Chinese-born American physicist')"}, {source: S2, locator: "opening ('Chinese-American')"}], how_known: "The sources say Chinese-born and Chinese-American; 'Han' is the coder's inference, so 0.5 (P24)."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not in the sources read."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not in the sources read."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not in the sources read."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1949–1963", certainty: 1.0, cites: [{source: S4, locator: "APS record (received 1949)"}, {source: S6, locator: "APS record (received 1963)"}], how_known: "First to last listed lasting contribution (P29, P30): the Wu–Shaknov submission (1949) to the CVC test (1963)."}
  age_at_first_lasting_contribution: {value: 37, certainty: 1.0, cites: [{source: S4, locator: "APS record (1949)"}, {source: S1, locator: "Born line (1912)"}], how_known: "1949 − 1912 = 37 (P30, no month adjustment); the birth-day dispute does not change the year."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No statement of hers scored at 3 or 4; B rests on working science, which is not an LIO-type view (P27)."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", rationale: "Nothing of hers on God or nature was read.", certainty: 0.5, cites: [{source: S1, locator: "whole article"}, {source: S3, locator: "whole paper"}], how_known: "Absence in the sources read; not evidence of absence."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Her work was precision experiment testing theoretical predictions (S3); nothing read on proof-style training.", certainty: 0.5, cites: [{source: S3, locator: "§§1–2"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S3, locator: "§1"}], how_known: "Nothing read on early mathematics."}
  circle_present: {value: "unclear", rationale: "No God–Nature statement read.", certainty: 0.5, cites: [{source: S1, locator: "whole article"}], how_known: "No evidence either way."}
  reading: "As belief, not finding: form and circle unclear. The record does not test H1."
  notes: ""

institutions:
  - {value: "University of California, Berkeley", role: "graduate student (Ph.D. 1940) and postdoc", years: "1936–1942", kind: university, certainty: 0.7, cites: [{source: S1, locator: "paragraph 2 (Ph.D. 1940)"}, {source: S3, locator: "§1 (1936 to 1940; postdoc to 1942)"}], how_known: "Two sources agree on the Ph.D.; the years are Shi's, so 0.7."}
  - {value: "Columbia University", role: "Division of War Research from 1944; research scientist; Pupin professor of physics from 1957", years: "1944–", kind: university, certainty: 1.0, cites: [{source: S1, locator: "paragraph 2"}, {source: S3, locator: "§1"}], how_known: "Two sources."}
collaborators:
  - {value: "Emilio Segrè", relation: "mentor or employer", note: "doctoral adviser at Berkeley", certainty: 0.7, cites: [{source: S3, locator: "§1"}], how_known: "Shi alone; the Linda Hall page names him as an expert on beta decay at Berkeley."}
  - {value: "Ernest O. Lawrence", relation: teacher, note: "Berkeley adviser", certainty: 1.0, cites: [{source: S1, locator: "paragraph 2"}, {source: S3, locator: "§1"}], how_known: "Two sources."}
  - {value: "Tsung-Dao Lee and Chen Ning Yang", relation: collaborator, note: "proposed parity non-conservation; asked her to run the test", certainty: 1.0, cites: [{source: S1, locator: "paragraph 3"}, {source: S2, locator: "parity paragraphs"}], how_known: "Two sources."}
  - {value: "Irving Shaknov", relation: "student or assistant", note: "co-author of the 1949 annihilation-radiation experiment", certainty: 1.0, cites: [{source: S4, locator: "APS record (authors)"}, {source: S3, locator: "§2"}], how_known: "Primary record and Shi."}

review:
  roster_status_reason: {value: "Core in v8 (F 5: Claude, DeepSeek, Gemini, GPT, Grok).", certainty: 0.7, cites: [{source: S7, locator: "roster.csv, rank 17"}], how_known: "Study roster."}
  controversies:
    - {value: "She was not included in the 1957 Nobel Prize given to Lee and Yang; the Linda Hall essay calls this an injustice that many feel was done", certainty: 0.7, cites: [{source: S2, locator: "paragraph 6 ('many feel that a great injustice was done')"}], how_known: "Linda Hall page alone."}
  data_quality_flags:
    - "Birth day: 29 May (Britannica) vs 31 May (Linda Hall); 0.5 with the alternative (P25)."
    - "Columbia start: 1944 (Britannica, Shi: Division of War Research) vs 1945 (Linda Hall). Not used for any computed field."
    - "Arrival in the US: Britannica and Shi imply 1936 (Berkeley 1936–1940); the Linda Hall page says she landed in San Francisco in 1937. Not used for any field."
    - "No worldview evidence found; worldview fields are UNKNOWN (P19), except B (working science, 0.5) and E (BELOW_THRESHOLD, P19)."
  open_questions:
    - "Read Chiang's biography (2014) and the NAS memoir (2009) for any statement on religion or nature."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "Britannica Editors. \"Chien-Shiung Wu.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Chien-Shiung-Wu."
    url: "https://www.britannica.com/biography/Chien-Shiung-Wu"
    accessed: 2026-10-08
    reliability_note: "Unsigned editors' article; whole article read (four paragraphs and Quick Facts)."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "William B. Ashworth, Jr."
    year: 2022
    citation: "Ashworth, William B., Jr. \"Chien-Shiung Wu.\" Scientist of the Day, Linda Hall Library, 31 May 2022. https://www.lindahall.org/about/news/scientist-of-the-day/chien-shiung-wu/."
    url: "https://www.lindahall.org/about/news/scientist-of-the-day/chien-shiung-wu/"
    accessed: 2026-10-08
    reliability_note: "Signed short essay by a historian of science at a research library."
    used_for: [identity, basics, contribution, childhood, worldview, heritage]
  - id: S3
    type: secondary
    kind: "journal article"
    author: "Yu Shi"
    year: 2025
    citation: "Shi, Yu. \"Chien-Shiung Wu as the Experimental Pioneer in Quantum Entanglement: A 2022 Note.\" Modern Physics Letters A (2025). https://doi.org/10.1142/S0217732325300010. Read as arXiv:2502.06458v1 (HTML)."
    url: "https://arxiv.org/html/2502.06458v1"
    accessed: 2026-10-08
    reliability_note: "Physicist's historical review, published in MPLA; read in the arXiv version. Sections numbered as in the paper."
    used_for: [basics, contribution, childhood, worldview, timing, lane_b, institutions, collaborators]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "C. S. Wu and I. Shaknov"
    year: 1950
    citation: "Wu, C. S., and I. Shaknov. \"The Angular Correlation of Scattered Annihilation Radiation.\" Physical Review 77, no. 1 (1950): 136. Received 21 November 1949. https://doi.org/10.1103/PhysRev.77.136."
    url: "https://journals.aps.org/pr/abstract/10.1103/PhysRev.77.136"
    accessed: 2026-10-08
    reliability_note: "Record page read (title, authors, received and published dates); full text behind a paywall, not read."
    used_for: [basics, contribution, worldview, timing, collaborators]
  - id: S5
    type: primary
    kind: "published work by the subject"
    author: "C. S. Wu, E. Ambler, R. W. Hayward, D. D. Hoppes and R. P. Hudson"
    year: 1957
    citation: "Wu, C. S., E. Ambler, R. W. Hayward, D. D. Hoppes, and R. P. Hudson. \"Experimental Test of Parity Conservation in Beta Decay.\" Physical Review 105, no. 4 (1957): 1413–1415. Received 15 January 1957. https://doi.org/10.1103/PhysRev.105.1413."
    url: "https://journals.aps.org/pr/abstract/10.1103/PhysRev.105.1413"
    accessed: 2026-10-08
    reliability_note: "Record page read (title, authors, received and published dates); the paper text was not read."
    used_for: [basics, contribution, worldview]
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "Y. K. Lee, L. W. Mo and C. S. Wu"
    year: 1963
    citation: "Lee, Y. K., L. W. Mo, and C. S. Wu. \"Experimental Test of the Conserved Vector Current Theory on the Beta Spectra of B12 and N12.\" Physical Review Letters 10, no. 6 (1963): 253. Received 4 February 1963. https://doi.org/10.1103/PhysRevLett.10.253."
    url: "https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.10.253"
    accessed: 2026-10-08
    reliability_note: "Record page read (title, authors, received and published dates); full text not read."
    used_for: [contribution, worldview, timing]
  - id: S7
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-08
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
---

# Chien-Shiung Wu

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Chien-Shiung Wu (1912–1997), Chinese-born American experimental physicist, gave the first experimental proof that parity is not conserved in the weak interaction (1957) [S1; S5]. Earlier, with Irving Shaknov, she measured the polarization correlation of annihilation photons (submitted 1949), later read as the first controlled entangled state [S3; S4], and in 1963 she confirmed the conserved vector current theory [S1; S6]. No statement of hers on religion, God or nature was found. Draft: primary_system UNKNOWN; B_cause 4 at 0.5 from working science; A UNKNOWN; mid_basin UNKNOWN.

## Life and work

Born in Jiangsu province, she studied at the National Central University in Nanjing (graduated 1934), took her Ph.D. at Berkeley in 1940, taught at Smith College and Princeton, and joined Columbia's Division of War Research in 1944, where she stayed and became Pupin professor in 1957 [S1; S3].

## Contribution and impact

The 1949 Wu–Shaknov experiment [S4; S3], the 1957 parity test [S5; S1; S2] and the 1963 CVC test [S6; S1]. Lee and Yang received the 1957 Nobel Prize after her result and similar experiments confirmed their proposal [S1].

## Childhood and education

Her father founded the first school she attended and held that girls deserved equal education [S2]. She graduated from the National Central University in 1934 [S1; S3].

## Adult working worldview

Not established. No statement of hers on religion, God or nature was found. B is scored 4 at 0.5 from her working science, as the rules direct for a scientist (P24) [S5; S3].

## Heritage (context only)

Chinese-born [S1; S2]. Context only.

## Timing

First lasting contribution 1949, at 37 [S4]. No LIO-type views found.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form and circle unclear [S3; S1].

## Open questions

- Chiang's biography (2014) and the NAS memoir (2009) for any worldview statement.

## Research log

- 2026-10-08: Read Britannica (editors), the Linda Hall Library page (Ashworth 2022), Shi's MPLA paper (arXiv HTML), and the APS record pages of the 1950, 1957 and 1963 papers (dates only). Web search for her religious views found nothing citable. The NAS memoir PDF was blocked to the fetch. Worldview left UNKNOWN except B (working science) and E (BELOW_THRESHOLD).
