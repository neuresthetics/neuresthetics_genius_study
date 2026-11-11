---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 8
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, third batch: physical science 1600–1950)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to physics. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (third batch, RUNBOOK §1 order). Basics from Britannica, MacTutor, his Nobel autobiography (Les Prix Nobel 1983) and Parker's NAS Biographical Memoir (1997). Worldview from his own words in the AIP interview of 6 October 1987 (Krisciunas): 'he knew I was an atheist'. primary_system ATHE at 0.5 (one oral self-description; no basis type fits a recorded interview, so capped by analogy with the single-letter rule; flagged). A 4 (0.5), B 4 (0.5); C, D, E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Rechecked under decision P8 (recorded interviews; schema 1.2). primary_system ATHE: basis scholarly_reconstruction 0.5 → recorded_interview 0.7. A_locus 4: 0.5 → 0.7 (recorded_interview). Self-described relation 0.5 → 0.7. B_cause 4 unchanged at 0.5 (Parker; the interview remark is indirect). mid_basin BELOW_THRESHOLD → false at 0.5 (A ≥ 3 at 0.7; certainty capped by B). Both statements now kind 'recorded interview'. Schema 1.1 → 1.2."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit, batch 3 (both runs, #19, #20, #25). S5 carries AIP's no-quotation notice, so under P8's last sentence only a paraphrase can be published and the interview cannot score an axis or code on its own; the record's earlier reading (quoting verbatim avoids the limit) was circular. Treated like Bohr's S7: S5 is now paraphrased throughout and its two verbatim statements were removed. primary_system ATHE 0.7 → 0.5 and A_locus 4 0.7 → 0.5, both basis recorded_interview → scholarly_reconstruction (as before P8); self-described relation 0.7 → 0.5; B_cause unchanged (4 at 0.5). mid_basin false (0.5) → BELOW_THRESHOLD (A and B both only at 0.5). Stale Wali note reworded. Not reviewed. Interview-based fields (primary_system, A_locus, the self-described relation, lio_views_relative_to_major_work, worldview_during_major_work, circle_present) now start their how_known with '(interview)' (P8 as signed off by Jason, 2026-10-02)."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Stage 3 lens-audit rulings applied to the batch's other records (OPEN_DECISIONS P14–P28, v8's picks, 2026-10-02). Schema 1.2 → 1.3. One reliable source caps a fact at 0.7; derived fields take the lowest certainty of their inputs; BELOW_THRESHOLD vs UNKNOWN per P19. Full before → after list: reports/stage3_rulings_changes.csv. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "P30 rule 5 age sweep: ages recomputed as event year − birth year, with no month adjustment (scripts/recompute_ages.py; every change is in reports/p30_age_changes.csv). No other value changed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Span alignment (P29, P30 and its addendum): timing.major_work_period checked, 1930–1983 unchanged; worldview.working_years 1929–1995 → 1930–1983, equal to the span (P30 addendum f); evidence for every headline value checked against the span; no value or certainty changed. Listed in reports/p30_span_alignment.csv. Not reviewed."}
    - {date: 2026-10-08, by: "Grok Bot", summary: "Lens audit of batch C (dd91009), ruling R1, logged as P35 (v8's pick): B_cause 4 → 3 at 0.5, alternative 4, because B rests on working science only. No other value changes; mid_basin unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #74, F5 rank 75). Needs: A single source; A faded; B faded. Quotable documents beyond S5 (P8): Wali Chandra (1991) p.304 atheist dialogue (S7; secondary quotation via Wikipedia cite-quote + Swarajya long extract); Wali (ed.) Man Behind the Legend (1997) for the 1987 Chicago Colloquium Gita preface 'I consider myself an atheist' (S8; secondary quotation); Free Inquiry 35.5 Haught Speaks block with Gita 'written by man' and 'definitely as an atheist' (S9). Dual bio Wikipedia EN (S10, P50). P47 source_quality on S1–S11. Truth and Beauty Kerr 'shuddering before the beautiful' via MacTutor Kerr biography (S11; secondary quotation) — aesthetic match of mathematics to Nature, not a law/exception claim (P35). primary_system ATHE 0.5→0.7 (written_profession on 1987 colloquium + recorded_interview Wali 1991; S5 paraphrase in support); A 4 0.5→0.7 support single→corroborated (S8+S7+S9; S5 support); drop A alt BELOW_THRESHOLD. B_cause stays 3 @0.5 inference_from_work (P35 alt 4); support labelled corroborated (S4+S5+S11 aesthetic). D UNKNOWN→4 @0.7 support corroborated (Gita not divine / written by man). mid_basin BELOW_THRESHOLD→false @0.7 (A≥3 branch, P10). Chart: faded hollow → faded filled (A corroborated @0.7; B still faded @0.5). Chart-moving YES (fill). Native Tamil name from Wikipedia. No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: chandrasekhar-subrahmanyan
  display_name: "Subrahmanyan Chandrasekhar"
  roster:
    canonical_name: "Subrahmanyan Chandrasekhar"
    rank: 75
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: physics
    field_bucket: physics
  full_name: {value: "Subrahmanyan Chandrasekhar", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "header"}], how_known: "Two sources; the Nobel page spells it 'Subramanyan'."}
  native_name: {value: "சுப்பிரமணியன் சந்திரசேகர்", certainty: 0.7, cites: [{source: S10, locator: "lead / Tamil native-name"}], how_known: "Wikipedia Tamil form (Cuppiramaṇiyaṉ Cantiracēkar); one reference entry (P15)."}
  aliases:
    - {name: "Chandrasekhar-Subrahmanyan", kind: "roster alias"}
    - {name: "Subrahmanyan-Chandrasekhar", kind: "roster alias"}
    - {name: "Chandra", kind: other}
    - {name: "Subramanyan Chandrasekhar", kind: transliteration}

basics:
  birth:
    date: {value: "1910-10-19", calendar: gregorian, certainty: 0.7, cites: [{source: S3, locator: "paragraph 1"}, {source: S1, locator: "opening"}, {source: S2, locator: "header"}], how_known: "His own Nobel autobiography, Britannica and MacTutor give 19 October; Parker's NAS memoir heads its text 'October 13, 1910', probably an error. Kept below 1.0 because of the conflict.", alternatives: [{value: "1910-10-13", cites: [{source: S4, locator: "heading"}]}]}
    place: {value: "Lahore", modern_name: "Lahore, Pakistan", polity_then: "British India", certainty: 1.0, cites: [{source: S3, locator: "paragraph 1"}, {source: S1, locator: "opening"}], how_known: "Two sources agree."}
  death:
    date: {value: "1995-08-21", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "header"}, {source: S3, locator: "note at end"}], how_known: "Three sources agree."}
    place: {value: "Chicago", modern_name: "Chicago, Illinois, United States", polity_then: "United States", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "final paragraphs"}], how_known: "Two sources agree."}
  first_lasting_contribution_year: {value: 1930, certainty: 0.7, cites: [{source: S1, locator: "paragraph 3 ('on his voyage to England in 1930')"}, {source: S4, locator: "shipboard paragraph"}, {source: S3, locator: "Nobel-cited papers (1931)"}], how_known: "The white-dwarf mass limit was worked out on the 1930 voyage; the first papers appeared in 1931."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S1, locator: "paragraph 3"}], how_known: "From first_lasting_contribution_year (P2)."}
  region_of_birth: {value: "South Asia", certainty: 1.0, cites: [{source: S1, locator: "opening ('Lahore, India [now in Pakistan]')"}], how_known: "Pakistan (and India) are South Asia in data/reference/regions.csv (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S3, locator: "paragraph 5"}, {source: S4, locator: "Chicago paragraphs"}], how_known: "Chicago from 1937 to his death; the mass limit itself (1930–35) was done in Madras, on the voyage and at Cambridge (Northern Europe)."}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S3, locator: "paragraph 1 ('the first son')"}], how_known: "His own account."}
  languages_of_work: {value: [English], certainty: 1.0, cites: [{source: S3, locator: "list of monographs"}, {source: S4, locator: "selected bibliography"}], how_known: "All monographs listed are in English."}
  occupations: {value: [astrophysicist, "theoretical physicist", "university professor", "journal editor"], certainty: 1.0, cites: [{source: S1, locator: "opening; paragraph 4"}, {source: S4, locator: "editor paragraph"}], how_known: "Two sources."}

contribution:
  primary_domain: physics
  fields: {value: [astrophysics, "theoretical physics", "general relativity"], certainty: 1.0, cites: [{source: S3, locator: "the seven periods"}, {source: S1, locator: "opening"}], how_known: "His own list of periods; Britannica agrees."}
  lasting_original_contributions:
    - {value: "Chandrasekhar limit: the maximum mass of a white dwarf (about 1.4 solar masses)", year: "1930–1935", kind: "law or principle", lasting: "named limit; basis of the theory of stellar collapse", certainty: 1.0, cites: [{source: S1, locator: "paragraph 3"}, {source: S4, locator: "shipboard paragraph"}], how_known: "Two sources."}
    - {value: "Stellar dynamics, including dynamical friction and Brownian-motion methods", year: "1938–1943", kind: theory, lasting: "Principles of Stellar Dynamics; 'Stochastic Problems' (1943)", certainty: 1.0, cites: [{source: S3, locator: "the seven periods"}, {source: S4, locator: "monographs paragraph"}], how_known: "Two sources."}
    - {value: "Radiative transfer, including the negative hydrogen ion and the polarization of the sunlit sky", year: "1943–1950", kind: theory, lasting: "Radiative Transfer (1950)", certainty: 1.0, cites: [{source: S3, locator: "the seven periods"}, {source: S4, locator: "monographs paragraph"}], how_known: "Two sources."}
    - {value: "Mathematical theory of black holes", year: "1974–1983", kind: theory, lasting: "The Mathematical Theory of Black Holes (1983)", certainty: 1.0, cites: [{source: S3, locator: "the seven periods"}, {source: S1, locator: "paragraph 4"}], how_known: "Two sources."}
  evidence_of_impact:
    - {value: "Nobel Prize in Physics (with W. A. Fowler) for theoretical studies of the structure and evolution of stars", kind: "honours in lifetime", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Nobel paragraph"}], how_known: "Two sources."}
    - {value: "Managing editor of the Astrophysical Journal, which he built into the leading journal of the field", kind: "institutional or technological lineage", certainty: 0.7, cites: [{source: S4, locator: "editor paragraph"}, {source: S2, locator: "editor paragraph"}], how_known: "Two sources; the assessment is Parker's."}
  major_works:
    - {value: "An Introduction to the Study of Stellar Structure", year: 1939, kind: book, certainty: 1.0, cites: [{source: S3, locator: "monograph 1"}, {source: S1, locator: "paragraph 5"}], how_known: "Two sources."}
    - {value: "Radiative Transfer", year: 1950, kind: book, certainty: 1.0, cites: [{source: S3, locator: "monograph 3"}, {source: S1, locator: "paragraph 5"}], how_known: "Two sources."}
    - {value: "The Mathematical Theory of Black Holes", year: 1983, kind: book, certainty: 1.0, cites: [{source: S3, locator: "monograph 6"}, {source: S1, locator: "paragraph 4"}], how_known: "Two sources."}
    - {value: "Truth and Beauty: Aesthetics and Motivations in Science", year: 1987, kind: book, certainty: 1.0, cites: [{source: S1, locator: "paragraph 5"}, {source: S4, locator: "Truth and Beauty paragraph"}], how_known: "Two sources; Kerr passage read via secondary quotation (S11), not the book pages."}
  honours:
    - {value: "Fellow of the Royal Society", year: 1944, certainty: 1.0, cites: [{source: S4, locator: "honours paragraph"}, {source: S5, locator: "office-furniture passage"}], how_known: "Two sources."}
    - {value: "Gold Medal of the Royal Astronomical Society", year: 1953, certainty: 1.0, cites: [{source: S1, locator: "paragraph 5"}, {source: S4, locator: "honours paragraph"}], how_known: "Two sources."}
    - {value: "Nobel Prize in Physics", year: 1983, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Nobel paragraph"}], how_known: "Two sources."}
    - {value: "Copley Medal of the Royal Society", year: 1984, certainty: 1.0, cites: [{source: S1, locator: "paragraph 5"}, {source: S2, locator: "Copley paragraph"}], how_known: "Two sources."}
  definition_fit: {value: "clearly meets", rationale: "Founded the theory of white-dwarf collapse and led several branches of theoretical astrophysics.", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Sources agree."}

childhood:
  family_religion: {value: "Hindu by birth (Tamil Brahmin), in a family Parker calls 'free-thinking'", certainty: 0.7, cites: [{source: S4, locator: "opening sentence"}, {source: S2, locator: "Biography, paragraph 1 ('a Brahman family')"}], how_known: "Parker's description; MacTutor gives the Brahmin family. Religious practice at home was not described in what was read."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not described in S1–S11. Wali (1991) covers the family but the book itself was not borrowed this pass (lending-only IA); only quoted passages used."}
  parents_and_household:
    - {value: "Father, C. S. Ayyar (Chandrasekhara Subrahmanya Ayyar), officer in the Indian Audits and Accounts Department", name: "Chandrasekhara Subrahmanya Ayyar", role: father, certainty: 1.0, cites: [{source: S3, locator: "paragraph 1"}, {source: S4, locator: "opening paragraph"}], how_known: "His own account; Parker agrees."}
    - {value: "Mother, Sita (Sitalakshmi, née Balakrishnan), who translated Ibsen's A Doll's House into Tamil", name: "Sitalakshmi", role: mother, certainty: 1.0, cites: [{source: S3, locator: "paragraph 1"}, {source: S4, locator: "opening paragraph"}], how_known: "Two sources."}
  household_circumstances: {value: "Third of ten children in a senior civil servant's family; moved to Madras in 1918; nephew of the physicist C. V. Raman", certainty: 1.0, cites: [{source: S3, locator: "paragraphs 1–2"}, {source: S4, locator: "opening paragraphs"}, {source: S1, locator: "paragraph 2"}], how_known: "Three sources."}
  schooling:
    - {value: "Education at home by his parents and private tutors until about twelve", stage: home, years: "to 1922", certainty: 0.7, cites: [{source: S3, locator: "paragraph 2"}, {source: S4, locator: "education paragraphs"}], how_known: "His own account; Parker says he entered regular school in 1921."}
    - {value: "Hindu High School, Triplicane, Madras", stage: "grammar or secondary school", years: "1922–1925", certainty: 0.7, cites: [{source: S3, locator: "paragraph 3"}], how_known: "His own account; Parker's 1921 start date differs."}
    - {value: "Presidency College, Madras: B.Sc. (Hons.) in physics, 1930", stage: university, years: "1925–1930", certainty: 1.0, cites: [{source: S3, locator: "paragraph 3"}, {source: S4, locator: "Presidency College paragraph"}], how_known: "Two sources."}
    - {value: "Trinity College, Cambridge, under R. H. Fowler (one year in Copenhagen); Ph.D. 1933", stage: university, years: "1930–1933", certainty: 1.0, cites: [{source: S3, locator: "paragraphs 3–4"}, {source: S4, locator: "Cambridge paragraphs"}], how_known: "Two sources."}
  early_mathematics: {value: "other", note: "Algebra and geometry in his second school year, which 'so attracted him that he worked his way through the textbooks the summer before the start of school' (S4).", certainty: 0.7, cites: [{source: S4, locator: "Madras paragraph"}], how_known: "Parker only."}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure:
    - {value: "Read Sommerfeld's Atomic Structure and Spectral Lines on his own; met Sommerfeld (1928) and Heisenberg (1929) when they lectured at Presidency College", certainty: 1.0, cites: [{source: S4, locator: "Sommerfeld and Heisenberg paragraphs"}, {source: S5, locator: "on Heisenberg and others"}], how_known: "Parker; these are college years (17–19)."}
  key_early_reading:
    - {value: "Sommerfeld, Atomic Structure and Spectral Lines", certainty: 0.7, cites: [{source: S4, locator: "Sommerfeld paragraph"}], how_known: "Parker."}
  childhood_mentors:
    - {value: "His parents, who taught him at home", certainty: 1.0, cites: [{source: S3, locator: "paragraph 2"}, {source: S4, locator: "education paragraph"}], how_known: "Two sources."}
    - {value: "His uncle C. V. Raman, as a role model", certainty: 0.7, cites: [{source: S2, locator: "Biography, paragraph 1"}], how_known: "MacTutor."}
  languages_in_childhood: {value: [Tamil, English], certainty: 0.7, cites: [{source: S4, locator: "opening paragraphs"}], how_known: "Parker: a 'Tamil-speaking' family; his mother taught Tamil and English."}
  notable_events:
    - {value: "Family moved from Lahore to Madras", year: "1918", certainty: 1.0, cites: [{source: S3, locator: "paragraph 2"}, {source: S4, locator: "Madras paragraph"}], how_known: "Two sources."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1930–1983", certainty: 1.0, cites: [{source: S3, locator: "the seven periods"}], how_known: "Equal to timing.major_work_period (P30 addendum f; span check 2026-10-02). Was 1929–1995: From his first paper to his death."}
  nominal_affiliations: []
  self_described_science_religion_relation:
    value: "Self-described atheist who still finds Hindu upbringing (tolerance, detachment) easy to live with; treats the Bhagavad Gita as great literature written by man, not divine revelation; takes mathematical beauty matched in Nature (Kerr) as the seal of scientific truth."
    certainty: 0.7
    cites: [{source: S7, locator: "p. 304 (via Wikipedia cite-quote / Swarajya)"}, {source: S9, locator: "Speaks block (Gita; definitely atheist)"}, {source: S11, locator: "Kerr 'shuddering before the beautiful'"}]
    how_known: "Own words in Wali biography dialogue and Free Inquiry Speaks block (secondary quotation); Kerr aesthetic via Truth and Beauty quotation. S5 paraphrase agrees on atheist self-description and 'simple is the seal of the true'."
  primary_system:
    value: ATHE
    basis: written_profession
    certainty: 0.7
    cites: [{source: S8, locator: "1987 Chicago Colloquium Gita preface (via Wikipedia / Swarajya)"}, {source: S7, locator: "p. 304"}, {source: S9, locator: "Speaks block"}, {source: S5, locator: "answer on whether Otto Struve was religious"}]
    how_known: "Public lecture preface (1987 Colloquium on Nuclear Policy, Culture and History, Chicago): 'I consider myself an atheist' (S8; secondary quotation of Wali 1997). Corroborated by Wali 1991 p.304 dialogue 'I am not religious in any sense; in fact, I consider myself an atheist' (S7) and Free Inquiry Speaks 'definitely as an atheist' (S9). S5 AIP paraphrase supports and does not score alone (P8). Secondary quotation keeps ceiling 0.7 not 1.0 (P21). P20: adult-life evidence; Struve retrospective (S5) places the view in the Yerkes years inside the span."
    rationale: "ATHE (positive naturalism: no gods) fits repeated first-person atheist self-descriptions. AGNOS is not a live alternative: he called himself an atheist, not undecided. HINDU heritage and cultural ease with Hindu tolerance are not a code (heritage never a code)."
    note: "IA lending copies of Wali 1991/1997 and Truth and Beauty remain unread as page images this pass; wording rests on secondary quotation (primary check pending)."
  secondary_system: {value: UNKNOWN, how_known: "No second system. Cultural Hindu upbringing is heritage/context, not a coded affiliation."}
  candidate_codes_considered:
    - {code: ATHE, reason: "Coded at 0.7: repeated own-words atheist self-descriptions (1987 colloquium; Wali 1991; Free Inquiry). ATHE is a stub system file (flag).", cites: [{source: S8, locator: "Gita preface"}, {source: S7, locator: "p. 304"}]}
    - {code: AGNOS, reason: "Rejected: he described himself as an atheist / 'definitely as an atheist', not as suspending judgement. AGNOS is a stub system file (flag).", cites: [{source: S9, locator: "Speaks block"}]}
    - {code: HINDU, reason: "Rejected: Hindu Brahmin heritage and ease with Hindu tolerance only; he denies religious belief and rejects the Gita as divine. Heritage is never a code.", cites: [{source: S7, locator: "p. 304"}, {source: S4, locator: "opening sentence"}]}
  lio_axes:
    A_locus:
      value: 4
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S8, locator: "1987 Colloquium Gita preface"}, {source: S7, locator: "p. 304"}, {source: S9, locator: "Speaks block"}]
      how_known: "Own-words denial of gods / religion in a public lecture preface (S8) plus biography interview dialogue (S7) and Free Inquiry Speaks (S9). Independent occasions → corroborated (P48). S5 paraphrase supports (P8) and is not counted as a scoring source alone. Secondary quotation keeps 0.7 not 1.0. Dropped create-pass alt BELOW_THRESHOLD: repeated 'atheist' / 'not religious in any sense' / 'definitely as an atheist' settle that the LIO pole applies."
      rationale: "No transcendent person: he denies any god and any religious sense, so the interventionist pole is absent and whatever order there is lies in the world (LIO pole)."
    B_cause:
      value: 3
      basis: inference_from_work
      certainty: 0.5
      support: corroborated
      cites: [{source: S4, locator: "Copenhagen / Eddington paragraphs"}, {source: S5, locator: "'simple is the seal of the true' passage"}, {source: S11, locator: "Kerr 'exact replica in Nature'"}]
      how_known: "Still scored on working science (P6/P35): Parker on developing implications of basic physical laws with no special cases against Eddington's 'stars do not behave in that way'. S5 paraphrase and Truth and Beauty Kerr aesthetic (S11) support lawfulness/beauty-matched-to-Nature but do not state no-exception. Support labelled corroborated (S4+S5+S11; P48). P35: B from working science only stays 3 @0.5 with named alternative 4."
      rationale: "Scored on his account of nature (P6). His work develops the implications of the basic physical laws with no special cases: a white dwarf above the limit must collapse, against Eddington. Kerr solution as exact representation in Nature (S11) and 'simple is the seal of the true' (S5, paraphrased) are aesthetic/truth remarks, not an explicit no-exception claim. Named alternative: 4, if a statement of his own shows no exception (Truth and Beauty pages still unread)."
    C_ledger: {value: BELOW_THRESHOLD, how_known: "Nothing on judgement, afterlife, karma or moral reckoning in S1–S11. His atheism rules out a divine judge, but not every ledger (for example karma), so C is not inferred from it.", note: "Gap: fuller Wali 1991/1997 pages."}
    D_authority:
      value: 4
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S9, locator: "Speaks block (Bhagvad Gita written by man)"}, {source: S8, locator: "1987 Colloquium Gita discussion (via Swarajya)"}]
      how_known: "(secondary quotation) Free Inquiry Speaks quotes his rejection of the Gita as divine ('written by man… irrational'); Swarajya quotes the same Colloquium's long Gita reading. Primary check of Wali 1997 / lecture text pending. S9 Speaks and S8 Colloquium/Swarajya path agree → corroborated (P48). Secondary quotation keeps 0.7 not 1.0."
      rationale: "Observation and reason outrank revelation: he can read the Gita as literature and 'noble instructions' but 'unable to accept it as divine' because it 'was written by man'."
    E_scope: {value: BELOW_THRESHOLD, how_known: "Scored on the world's order (P7). Nothing read addresses favour for a group in events; not scored from working science alone (same treatment as Fermi and Curie)."}
  mid_basin: {value: false, certainty: 0.7, cites: [{source: S8, locator: "Gita preface"}, {source: S7, locator: "p. 304"}], how_known: "A_locus 4 at 0.7: the A ≥ 3 branch reads A only (P10), so B at 0.5 does not block false."}
  statements:
    - text: "I should like to preface my remarks with a personal statement in order that my later remarks will not be misunderstood. I consider myself an atheist."
      cites: [{source: S8, locator: "1987 Chicago Colloquium Gita session (via Wikipedia / Swarajya)"}, {source: S10, locator: "Personal life / religious views"}]
      date: "1987"
      context: "Colloquium on Nuclear Policy, Culture and History, Chicago, session 'An Ethics for Nuclear Policy: The Bhagavad Gita, or Gandhian Non-violence or the Middle Way?'. Wording as quoted in Wali (ed.) 1997 and reported by Wikipedia and Swarajya."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Primary check pending against Wali 1997 / lecture text."
    - text: "I am not religious in any sense; in fact, I consider myself an atheist. Nonetheless, because the Hindu religion, despite its outward trappings, is an essentially rational way of life, it's easy to live with it. It's so tolerant."
      cites: [{source: S7, locator: "p. 304"}, {source: S9, locator: "Speaks block"}, {source: S10, locator: "cite to Wali 1991 p. 304"}]
      date: "1991"
      context: "Dialogue in Kameshwar C. Wali, Chandra: A Biography of S. Chandrasekhar (University of Chicago Press, 1991), p. 304. Long form also in Free Inquiry Speaks and Swarajya."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Primary check pending against Wali 1991 page images (IA lending-only this pass)."
    - text: "No, I am an atheist."
      cites: [{source: S9, locator: "Speaks block (Would you call yourself a religious person?)"}]
      date: "1991"
      context: "Interview dialogue as printed in Free Inquiry 35.5 Speaks block (James A. Haught). Likely from the Wali interview corpus; treated as secondary quotation."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
    - text: "I can read the Bhagvad Gita, recognize it as great literature, recognize that parts of it are wholly noble instructions to people. But I am unable to accept it as divine and—as one commonly says, a testament directly of God—because I know, at least I think I know, the Bhagvad Gita was written by man, and to attribute it to anything more seems irrational."
      cites: [{source: S9, locator: "Speaks block"}]
      date: "1991"
      context: "Same Free Inquiry Speaks interview block (spelling Bhagvad as printed there)."
      axes: [D_authority, A_locus]
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Primary check pending (Wali 1991/1997)."
    - text: "No. In fact, I can characterize myself definitely as an atheist."
      cites: [{source: S9, locator: "Speaks block (strong convictions of a religious or philosophical nature?)"}]
      date: "1991"
      context: "Same Free Inquiry Speaks block."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
    - text: "In my entire scientific life, extending over forty-five years, the most shattering experience has been the realization that an exact solution of Einstein's equations of general relativity, discovered by the New Zealand mathematician, Roy Kerr, provides the absolutely exact representation of untold numbers of massive black holes that populate the universe. This shuddering before the beautiful, this incredible fact that a discovery motivated by a search after the beautiful in mathematics should find its exact replica in Nature, persuades me to say that beauty is that to which the human mind responds at its deepest and most profound."
      cites: [{source: S11, locator: "MacTutor Kerr biography quotation of Truth and Beauty"}]
      date: "1987"
      context: "Truth and Beauty: Aesthetics and Motivations in Science (University of Chicago Press, 1987); wording as quoted on MacTutor's Roy Kerr biography (and matching New Scientist / Kerr Fest extracts)."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Aesthetic truth/beauty claim; does not by itself lift B past P35 (no explicit no-exception statement). Primary check pending against Truth and Beauty pages."
  changes_over_life: []
  coder_notes: "Deepen D1 2026-10-24. P8 fix path taken: quotable documents other than paraphrase-only S5 now carry ATHE and A (Wali 1991/1997; Free Inquiry Speaks), with S5 in support. ATHE, AGNOS and HINDU remain stub system files (flag). B stays under P35 until Truth and Beauty (or another own-words law/exception statement) is read in a scholarly edition. Free Inquiry Speaks may reprint Wali interview material — counted as access path / secondary quotation, not as an independent primary. nominal_affiliations empty after research. No fallacy_catalog (Jason)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Tamil Brahmin", certainty: 1.0, cites: [{source: S4, locator: "opening sentence"}, {source: S2, locator: "Biography, paragraph 1"}], how_known: "Two sources."}
  religious_heritage_by_birth: {value: "Hindu", certainty: 0.7, cites: [{source: S4, locator: "opening sentence"}], how_known: "From the Brahmin family; Parker calls the family free-thinking."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1930–1983", certainty: 1.0, cites: [{source: S3, locator: "the seven periods"}], how_known: "His own periods, from white dwarfs to black holes."}
  age_at_first_lasting_contribution: {value: 20, certainty: 0.7, cites: [{source: S3, locator: "paragraph 1"}, {source: S4, locator: "shipboard paragraph"}], how_known: "Born October 1910; the limit was worked out on the voyage of July–August 1930. P30 (rule 5): 1930 − 1910 = 20, with no month adjustment; was 19 until the P30 age sweep (2026-10-02)."}
  first_evidence_of_lio_type_views: {value: "1937–1950 (retrospective)", certainty: 0.5, cites: [{source: S5, locator: "answer on whether Struve was religious"}, {source: S7, locator: "p. 304"}], how_known: "(interview) S5 paraphrase: Struve knew during the Yerkes years that he was an atheist. Dated public/interview atheist statements are 1987–1991 (after span end 1983); P20 lets adult-life evidence score the span absent a sourced change."}
  lio_views_relative_to_major_work: {value: "during major work", rationale: "Retrospective remark that Struve knew he was an atheist in the Yerkes years (inside 1930–1983); later 1987–1991 statements continue the same view with no sourced conversion.", certainty: 0.5, cites: [{source: S5, locator: "Struve answer"}, {source: S8, locator: "1987 Colloquium"}], how_known: "(interview) S5 dating is hindsight; 1987 colloquium is just after span end."}
  worldview_during_major_work: {value: "On his own later account, Struve knew during their Yerkes years (1937–1950) that he was an atheist; 1987–1991 statements confirm continuing atheism with no sourced change (P20).", certainty: 0.5, cites: [{source: S5, locator: "answer on whether Struve was religious"}, {source: S7, locator: "p. 304"}, {source: S8, locator: "Gita preface"}], how_known: "(interview) Retrospective S5 plus later quotable atheist statements; dating the view into the span rests partly on hindsight, so 0.5."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", certainty: 0.5, cites: [{source: S3, locator: "paragraph 7"}], how_known: "Coder's reading of his own description of his method: after study he presents his view 'ab initio, in a coherent account with order, form, and structure' (S3)."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S4, locator: "Madras paragraph"}], how_known: "Early attraction to algebra and geometry (S4); nothing on how the method was formed."}
  circle_present: {value: "no", rationale: "Self-described atheist; no God-Nature identity in anything read.", certainty: 0.7, cites: [{source: S8, locator: "Gita preface"}, {source: S7, locator: "p. 304"}], how_known: "Repeated atheist self-descriptions."}
  reading: "As belief, not finding: form present, no circle. The record does not test H1."
  notes: ""

institutions:
  - {value: "Trinity College, Cambridge", role: "Prize Fellow", years: "1933–1937", kind: university, certainty: 1.0, cites: [{source: S3, locator: "paragraph 4"}, {source: S4, locator: "Trinity paragraph"}], how_known: "Two sources (Britannica gives 1933–1936)."}
  - {value: "University of Chicago (Yerkes Observatory to 1964, then the campus)", role: "research associate (1937); Morton D. Hull Distinguished Service Professor (1952)", years: "1937–1995", kind: university, certainty: 1.0, cites: [{source: S3, locator: "paragraph 5"}, {source: S1, locator: "paragraph 4"}, {source: S4, locator: "Chicago paragraphs"}], how_known: "Three sources."}
  - {value: "Ballistic Research Laboratories, Aberdeen Proving Ground", role: "wartime researcher", years: "1943–1945", kind: "government or state body", certainty: 0.7, cites: [{source: S2, locator: "World War II paragraph"}], how_known: "MacTutor."}
  - {value: "Astrophysical Journal", role: "managing editor", years: "1952–1971", kind: other, certainty: 1.0, cites: [{source: S2, locator: "editor paragraph"}, {source: S4, locator: "editor paragraph"}], how_known: "Two sources."}
collaborators:
  - {value: "R. H. Fowler", relation: teacher, note: "Cambridge supervisor; communicated his first paper", certainty: 1.0, cites: [{source: S3, locator: "paragraph 3"}, {source: S4, locator: "Fowler paragraphs"}], how_known: "Two sources."}
  - {value: "Arthur Eddington", roster_id: eddington-arthur, relation: "rival or critic", note: "rejected the mass limit at the RAS in January 1935", certainty: 1.0, cites: [{source: S4, locator: "January 1935 paragraph"}, {source: S1, locator: "paragraph 3"}], how_known: "Two sources."}
  - {value: "Paul Dirac", roster_id: dirac-paul, relation: "influenced by", note: "advised his year in Copenhagen", certainty: 1.0, cites: [{source: S3, locator: "paragraph 3"}, {source: S4, locator: "Cambridge paragraph"}], how_known: "Two sources."}
  - {value: "Otto Struve", relation: "mentor or employer", note: "brought him to Yerkes in 1937", certainty: 1.0, cites: [{source: S3, locator: "paragraph 5"}, {source: S5, locator: "opening answers"}], how_known: "Two sources."}
  - {value: "C. V. Raman", roster_id: raman-c-v, relation: family, note: "paternal uncle; role model", certainty: 1.0, cites: [{source: S1, locator: "paragraph 2"}, {source: S4, locator: "opening paragraph"}], how_known: "Two sources."}

review:
  roster_status_reason: {value: "Core in v8 (F 5, all five models).", certainty: 0.7, cites: [{source: S6, locator: "roster.csv, rank 75"}], how_known: "Study roster."}
  controversies:
    - {value: "Eddington's public rejection of the white-dwarf mass limit (1935) and its effect on his career", certainty: 1.0, cites: [{source: S4, locator: "January 1935 paragraph"}, {source: S1, locator: "paragraph 3"}], how_known: "Two sources."}
  data_quality_flags:
    - "Birth date: 19 October 1910 in his autobiography, Britannica and MacTutor; 13 October in the NAS memoir heading."
    - "School start: his autobiography says home education until twelve and Hindu High School 1922–25; Parker says regular school from 1921."
    - "S5 AIP no-quotation notice: paraphrase-only; cannot score alone (P8). Deepen D1 rests ATHE/A on Wali 1991/1997 and Free Inquiry Speaks (secondary quotation); S5 in support."
    - "Wali 1991, Wali 1997, and Truth and Beauty page images unread this pass (IA lending-restricted); all quoted atheist/Gita/Kerr wording is secondary quotation (primary check pending)."
    - "S5 was read through the Wayback Machine copy of the AIP page (the live page redirects to a repository that refused the fetch); its wording was checked on that rendering, not saved locally."
  open_questions:
    - "Borrow Wali, Chandra (1991) p. 304 and Wali (ed.) 1997 for primary check of atheist and Gita quotations (upgrade verified_against)."
    - "Read Truth and Beauty (1987) pages for any explicit law/exception statement that would lift B past P35."
    - "1977 AIP Weart interviews still unread."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "\"Subrahmanyan Chandrasekhar.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Subrahmanyan-Chandrasekhar."
    url: "https://www.britannica.com/biography/Subrahmanyan-Chandrasekhar"
    accessed: 2026-10-02
    source_quality: "reference entry"
    reliability_note: "Short editorial article; paragraphs counted from the opening."
    used_for: [identity, basics, contribution, childhood, institutions, collaborators, review]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "J J O'Connor and E F Robertson"
    citation: "O'Connor, J. J., and E. F. Robertson. \"Subrahmanyan Chandrasekhar.\" MacTutor History of Mathematics, University of St Andrews. https://mathshistory.st-andrews.ac.uk/Biographies/Chandrasekhar/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Chandrasekhar/"
    accessed: 2026-10-02
    source_quality: "reference entry"
    reliability_note: "Biography; located by topic."
    used_for: [identity, basics, contribution, childhood, heritage, institutions]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "Subrahmanyan Chandrasekhar"
    year: 1984
    citation: "Chandrasekhar, S. \"Subramanyan Chandrasekhar – Biographical.\" In Les Prix Nobel. The Nobel Prizes 1983, ed. Wilhelm Odelberg. Stockholm: Nobel Foundation, 1984. NobelPrize.org. https://www.nobelprize.org/prizes/physics/1983/chandrasekhar/biographical/."
    url: "https://www.nobelprize.org/prizes/physics/1983/chandrasekhar/biographical/"
    accessed: 2026-10-02
    source_quality: "primary / own words"
    reliability_note: "His own autobiography on the Nobel Foundation's official site; paragraphs counted from 'I was born in Lahore'."
    used_for: [identity, basics, contribution, childhood, worldview, timing, lane_b, institutions, collaborators]
  - id: S4
    type: secondary
    kind: "book chapter"
    author: "Eugene N. Parker"
    year: 1997
    citation: "Parker, Eugene N. \"Subrahmanyan Chandrasekhar, October 13, 1910–August 21, 1995.\" Biographical Memoirs, vol. 72. Washington, DC: National Academies Press, 1997. https://www.nationalacademies.org/read/5859/chapter/4."
    url: "https://www.nationalacademies.org/read/5859/chapter/4"
    accessed: 2026-10-02
    source_quality: "scholarly reconstruction"
    reliability_note: "NAS memoir by a colleague, drawing on Wali (1991). Read on the National Academies Press site, which has no page numbers; located by topic."
    used_for: [basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators, review]
  - id: S5
    type: primary
    kind: "archive record"
    author: "Subrahmanyan Chandrasekhar, interviewed by Kevin Krisciunas"
    year: 1987
    citation: "Interview with Dr. S. Chandrasekhar by Kevin Krisciunas, University of Chicago, 6 October 1987. Niels Bohr Library & Archives, American Institute of Physics. Archived copy of the AIP page: https://web.archive.org/web/20150202064758/http://www.aip.org/history/ohilist/4552.html."
    url: "https://web.archive.org/web/20150202064758/http://www.aip.org/history/ohilist/4552.html"
    accessed: 2026-10-02
    source_quality: "primary / own words"
    reliability_note: "Official AIP transcript of a tape-recorded interview (as archived in 2015); mostly about Otto Struve. His own speech, not a written text. AIP restricts quotation without written permission, so the record paraphrases it and, under P8, it scores nothing on its own (same treatment as Bohr's S7). Located by topic. Deepen D1: support only."
    used_for: [basics, childhood, worldview, timing, lane_b, collaborators]
  - id: S6
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    source_quality: "study roster"
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
  - id: S7
    type: secondary
    kind: "scholarly book"
    author: "Kameshwar C. Wali"
    year: 1991
    citation: "Wali, Kameshwar C. Chandra: A Biography of S. Chandrasekhar. Chicago: University of Chicago Press, 1991, p. 304. Quotation reached via Wikipedia cite-quote (SC: 'I am not religious in any sense; in fact, I consider myself an atheist') and Aravindan Neelakandan, Swarajya, 20 October 2017 (long extract)."
    url: "https://archive.org/details/chandrabiography0000wali_a3y2"
    accessed: 2026-10-24
    source_quality: "scholarly edition or monograph"
    reliability_note: "Scholarly biography with interview dialogue. Page images unread this pass (IA access-restricted / lending). Used as secondary quotation only; primary check pending."
    used_for: [worldview, timing, review]
  - id: S8
    type: secondary
    kind: "scholarly book"
    author: "Kameshwar C. Wali (ed.)"
    year: 1997
    citation: "Wali, Kameshwar C., ed. S. Chandrasekhar: The Man Behind the Legend. London: Imperial College Press, 1997. Cited by Wikipedia and Swarajya for the 1987 Chicago Colloquium Gita-session preface 'I consider myself an atheist' and related Gita discussion."
    url: "https://archive.org/details/schandrasekharma0000unse"
    accessed: 2026-10-24
    source_quality: "scholarly edition or monograph"
    reliability_note: "Edited volume; lecture/preface wording used via secondary quotation (Wikipedia; Swarajya). Page images unread (IA lending)."
    used_for: [worldview, timing, review]
  - id: S9
    type: secondary
    kind: "journal article"
    author: "James A. Haught"
    year: 2015
    citation: "Haught, James A. \"Subrahmanyan Chandrasekhar.\" Free Inquiry 35, no. 5 (2015). Speaks block. https://secularhumanism.org/2015/07/cont-subrahmanyan-chandrasekhar/ (read via Wayback Machine)."
    url: "https://web.archive.org/web/2020/https://secularhumanism.org/2015/07/cont-subrahmanyan-chandrasekhar/"
    accessed: 2026-10-24
    source_quality: "newspaper interview"
    reliability_note: "Magazine Speaks block printing interview Q&A (atheist; Gita written by man; definitely an atheist). May reprint Wali interview material; treated as secondary quotation / access path, not an independent primary. Live site Cloudflare-blocked the fetch agent; Wayback used."
    used_for: [worldview]
  - id: S10
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    year: 2026
    citation: "\"Subrahmanyan Chandrasekhar.\" Wikipedia. https://en.wikipedia.org/wiki/Subrahmanyan_Chandrasekhar."
    url: "https://en.wikipedia.org/wiki/Subrahmanyan_Chandrasekhar"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Dual biography with Britannica (P50). Used for Tamil native name and for cite-links to Wali 1991 p.304 and Wali 1997; worldview scores rest on those cited works, not on Wikipedia prose alone."
    used_for: [identity, worldview]
  - id: S11
    type: secondary
    kind: "institutional page"
    author: "J J O'Connor and E F Robertson"
    year: 2003
    citation: "O'Connor, J. J., and E. F. Robertson. \"Roy Kerr.\" MacTutor History of Mathematics, University of St Andrews. Quotation from Chandrasekhar, Truth and Beauty (1987). https://mathshistory.st-andrews.ac.uk/Biographies/Kerr_Roy/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Kerr_Roy/"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Secondary quotation of the Kerr 'shuddering before the beautiful' passage from Truth and Beauty; book pages unread. Cross-checked against matching extracts (New Scientist; Kerr Fest)."
    used_for: [worldview, contribution]
---

# Subrahmanyan Chandrasekhar

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Subrahmanyan Chandrasekhar (1910–1995), Indian-born American astrophysicist, found the mass limit for white dwarfs on his 1930 voyage to England and won the 1983 Nobel Prize in Physics [S1, opening; paragraph 3]. Born into a "free-thinking, Tamil-speaking Brahmin family" [S4, opening sentence], he repeatedly called himself an atheist in quotable documents beyond the paraphrase-only AIP interview: the 1987 Chicago Colloquium Gita preface [S8], Wali 1991 p. 304 [S7], and Free Inquiry Speaks [S9]. Deepen D1: **ATHE at 0.7**; **A 4 at 0.7** (corroborated); **B 3 at 0.5** (alternative 4, P35; support corroborated); **D 4 at 0.7** (corroborated; Gita not divine); C and E below threshold; **mid_basin false** at 0.7. Chart: faded filled (A dark enough alone would be dark, but darkness uses min(A,B); B still faded).

## Life and work

Born in Lahore, educated at home, at the Hindu High School in Madras and at Presidency College, he went to Cambridge in 1930 and took his Ph.D. in 1933 [S3, paragraphs 1–4]. He held a Trinity Prize Fellowship (1933–37) and joined the University of Chicago in January 1937, where he stayed for the rest of his life [S3, paragraphs 4–5].

## Contribution and impact

The white-dwarf mass limit, then stellar dynamics, radiative transfer, hydrodynamic stability, ellipsoidal figures, relativity and black holes, each closed by a monograph [S3, the seven periods]. He edited the Astrophysical Journal from 1952 to 1971 [S2; S4].

## Childhood and education

His parents taught him at home until he was about twelve [S3, paragraph 2]. Algebra and geometry so attracted him that he worked through the textbooks before the school year began [S4]. He read Sommerfeld on his own and met Sommerfeld and Heisenberg in Madras [S4].

## Adult working worldview

Quotable own words (secondary quotation; primary check of Wali / Truth and Beauty pending): public lecture preface "I consider myself an atheist" [S8]; biography dialogue "I am not religious in any sense; in fact, I consider myself an atheist" [S7, p. 304]; Free Inquiry Speaks — "No, I am an atheist", Gita "written by man", "definitely as an atheist" [S9]. S5 AIP interview (paraphrase-only) supports and dates the view into the Struve/Yerkes years [S5]. Scores: **A 4 (0.7, corroborated)**; **B 3 (0.5, inference from work; alternative 4, P35)**; **D 4 (0.7, corroborated)**; C and E below threshold; **mid_basin false (0.7)**.

## Heritage (context only)

Tamil Brahmin, Hindu by birth [S4, opening sentence]. Context only — never a code. He described Hindu upbringing as tolerant and easy to live with while denying religious belief [S7].

## Timing

First lasting contribution 1930, at 20 [S1, paragraph 3; S4]. Earliest in-span pointer is retrospective: Struve knew in 1937–1950 that he was an atheist [S5]. Dated public/interview statements 1987–1991 continue the same view (P20).

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form present (he presents each field "ab initio, in a coherent account with order, form, and structure" [S3, paragraph 7]); no circle.

## Open questions

- Primary check of Wali 1991 p. 304 and Wali 1997 (IA lending).
- Truth and Beauty pages for a B law/exception statement (P35).
- 1977 AIP Weart interviews.

## Research log

- 2026-10-02: Read Britannica, MacTutor, the Nobel autobiography, Parker's NAS memoir (National Academies Press reader; the nasonline PDF returned an HTML block page) and the AIP interview of 1987 (Wayback copy). Wali (1991) and the 1997 volume are lending-only on archive.org and could not be searched. The 1977 AIP interviews (Weart) were not reached.
- 2026-10-24: Deepen D1. Secondary quotations of Wali 1991/1997 via Wikipedia and Swarajya; Free Inquiry 35.5 Speaks via Wayback; Wikipedia dual bio; Kerr/Truth and Beauty passage via MacTutor Kerr. IA borrow of Wali and Truth and Beauty still blocked. A/ATHE/mid_basin raised; B stays P35; D filled. No fallacy_catalog (Jason).
