---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 6
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, third batch: physical science 1600–1950)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (third batch, RUNBOOK §1 order). Basics from Britannica, MacTutor, his Nobel autobiography (Les Prix Nobel 1983) and Parker's NAS Biographical Memoir (1997). Worldview from his own words in the AIP interview of 6 October 1987 (Krisciunas): 'he knew I was an atheist'. primary_system ATHE at 0.5 (one oral self-description; no basis type fits a recorded interview, so capped by analogy with the single-letter rule; flagged). A 4 (0.5), B 4 (0.5); C, D, E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Rechecked under decision P8 (recorded interviews; schema 1.2). primary_system ATHE: basis scholarly_reconstruction 0.5 → recorded_interview 0.7. A_locus 4: 0.5 → 0.7 (recorded_interview). Self-described relation 0.5 → 0.7. B_cause 4 unchanged at 0.5 (Parker; the interview remark is indirect). mid_basin BELOW_THRESHOLD → false at 0.5 (A ≥ 3 at 0.7; certainty capped by B). Both statements now kind 'recorded interview'. Schema 1.1 → 1.2."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit, batch 3 (both runs, #19, #20, #25). S5 carries AIP's no-quotation notice, so under P8's last sentence only a paraphrase can be published and the interview cannot score an axis or code on its own; the record's earlier reading (quoting verbatim avoids the limit) was circular. Treated like Bohr's S7: S5 is now paraphrased throughout and its two verbatim statements were removed. primary_system ATHE 0.7 → 0.5 and A_locus 4 0.7 → 0.5, both basis recorded_interview → scholarly_reconstruction (as before P8); self-described relation 0.7 → 0.5; B_cause unchanged (4 at 0.5). mid_basin false (0.5) → BELOW_THRESHOLD (A and B both only at 0.5). Stale Wali note reworded. Not reviewed. Interview-based fields (primary_system, A_locus, the self-described relation, lio_views_relative_to_major_work, worldview_during_major_work, circle_present) now start their how_known with '(interview)' (P8 as signed off by Jason, 2026-10-02)."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Stage 3 lens-audit rulings applied to the batch's other records (OPEN_DECISIONS P14–P28, v8's picks, 2026-10-02). Schema 1.2 → 1.3. One reliable source caps a fact at 0.7; derived fields take the lowest certainty of their inputs; BELOW_THRESHOLD vs UNKNOWN per P19. Full before → after list: reports/stage3_rulings_changes.csv. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "P30 rule 5 age sweep: ages recomputed as event year − birth year, with no month adjustment (scripts/recompute_ages.py; every change is in reports/p30_age_changes.csv). No other value changed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Span alignment (P29, P30 and its addendum): timing.major_work_period checked, 1930–1983 unchanged; worldview.working_years 1929–1995 → 1930–1983, equal to the span (P30 addendum f); evidence for every headline value checked against the span; no value or certainty changed. Listed in reports/p30_span_alignment.csv. Not reviewed."}

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
  native_name: {value: UNKNOWN, how_known: "The Tamil-script form is not given in S1–S5."}
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
    - {value: "Truth and Beauty: Aesthetics and Motivations in Science", year: 1987, kind: book, certainty: 1.0, cites: [{source: S1, locator: "paragraph 5"}, {source: S4, locator: "Truth and Beauty paragraph"}], how_known: "Two sources; not read."}
  honours:
    - {value: "Fellow of the Royal Society", year: 1944, certainty: 1.0, cites: [{source: S4, locator: "honours paragraph"}, {source: S5, locator: "office-furniture passage"}], how_known: "Two sources."}
    - {value: "Gold Medal of the Royal Astronomical Society", year: 1953, certainty: 1.0, cites: [{source: S1, locator: "paragraph 5"}, {source: S4, locator: "honours paragraph"}], how_known: "Two sources."}
    - {value: "Nobel Prize in Physics", year: 1983, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Nobel paragraph"}], how_known: "Two sources."}
    - {value: "Copley Medal of the Royal Society", year: 1984, certainty: 1.0, cites: [{source: S1, locator: "paragraph 5"}, {source: S2, locator: "Copley paragraph"}], how_known: "Two sources."}
  definition_fit: {value: "clearly meets", rationale: "Founded the theory of white-dwarf collapse and led several branches of theoretical astrophysics.", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Sources agree."}

childhood:
  family_religion: {value: "Hindu by birth (Tamil Brahmin), in a family Parker calls 'free-thinking'", certainty: 0.7, cites: [{source: S4, locator: "opening sentence"}, {source: S2, locator: "Biography, paragraph 1 ('a Brahman family')"}], how_known: "Parker's description; MacTutor gives the Brahmin family. Religious practice at home was not described in what was read."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not described in S1–S5. Wali's biography (1991) covers the family but is a lending-only scan."}
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
    value: "None stated as such in what was read. In a 1987 interview (paraphrased here) he called himself an atheist in passing, and described the maxim that the simple is the seal of the true as a description of the fundamental truths of science, giving the Kerr solution, where a search for abstract beauty is matched exactly in nature, as his example."
    certainty: 0.5
    cites: [{source: S5, locator: "answer on whether Otto Struve was religious; answer on 'the simple is the seal of the true'"}]
    how_known: "(interview) His own words in one recorded interview (S5). AIP's notice restricts quotation, so S5 is paraphrased (same treatment as Bohr's S7). One paraphrase-only interview, so 0.5 (lens audit batch 3: back from 0.7 to the pre-P8 value)."
  primary_system:
    value: ATHE
    basis: scholarly_reconstruction
    certainty: 0.5
    cites: [{source: S5, locator: "answer on whether Otto Struve was religious"}, {source: S4, locator: "opening sentence"}]
    how_known: "(interview) His own self-description in a tape-recorded AIP interview (S5, 6 October 1987): asked whether Otto Struve was religious, he said in passing that Struve knew he was an atheist and never raised the subject with him (paraphrased; AIP's notice restricts quotation). Under decision P8 a paraphrase-only interview cannot score a code on its own, so basis recorded_interview (0.7) does not apply (lens audit batch 3, #19). Kept at the 0.5 floor with basis scholarly_reconstruction, as before P8, by v8's pick on the lens fix (2026-10-02); Parker's 'free-thinking' family (S4) is consistent with it. A strict reading of P8 would withhold the code (BELOW_THRESHOLD) until a second, quotable document is read."
    rationale: "ATHE (positive naturalism: no gods) fits a self-described atheist, and the code does not rest on the absence of belief. AGNOS is not a live alternative: he called himself an atheist, not undecided. The certainty is limited by the evidence type, not by a rival code."
    note: "Wali, Chandra (1991), p. 304, reportedly quotes him: 'I am not religious in any sense; in fact, I consider myself an atheist'. Seen only via a secondary summary (lending-only scan), so not used. Reading it, or Wali (ed.), S. Chandrasekhar: The Man Behind the Legend (1997), would give a quotable document other than S5; the code would then rest on that document, with S5 in support (P8), and could be reconsidered at 0.7."
  secondary_system: {value: UNKNOWN, how_known: "No second system in S1–S5."}
  candidate_codes_considered:
    - {code: ATHE, reason: "Coded at 0.5: his own self-description as an atheist in a paraphrase-only interview (S5). ATHE is a stub system file (flag).", cites: [{source: S5, locator: "answer on whether Struve was religious"}]}
    - {code: AGNOS, reason: "Rejected: he described himself as an atheist, not as suspending judgement. AGNOS is a stub system file (flag).", cites: [{source: S5, locator: "answer on whether Struve was religious"}]}
    - {code: HINDU, reason: "Rejected: Hindu Brahmin heritage only; no adult practice or belief recorded. Heritage is never a code.", cites: [{source: S4, locator: "opening sentence"}]}
  lio_axes:
    A_locus:
      value: 4
      basis: scholarly_reconstruction
      certainty: 0.5
      cites: [{source: S5, locator: "answer on whether Struve was religious"}]
      how_known: "(interview) Read from his self-description as an atheist in one paraphrase-only interview (S5). P8 does not let such an interview score an axis on its own, so not recorded_interview (lens audit batch 3, #20); kept at 0.5, the same level as primary_system, as before P8. The coder's step from a passing 'atheist' label to the LIO pole is itself indirect, which also points to 0.5; the named alternative below would cap it at 0.7 in any case (CODING_GUIDE §3)."
      rationale: "No transcendent person: he denied any god, so the interventionist pole is absent and whatever order there is lies in the world (LIO pole). Alternative named: the axis may be read as not applying to someone who denies the divine altogether, which would make it BELOW_THRESHOLD as for Fermi, Curie and Bohr, who made no such denial in what was read."
    B_cause:
      value: 4
      basis: scholarly_reconstruction
      certainty: 0.5
      cites: [{source: S4, locator: "Copenhagen paragraph"}, {source: S5, locator: "'simple is the seal of the true' passage"}]
      how_known: "Scored on his working science (P6), mainly from Parker's account (scholarly reconstruction, 0.5). The interview remark (S5) is paraphrase-only and speaks to beauty and truth, not to law against exception, so it only supports the score (P8). Unchanged by the batch 3 audit."
      rationale: "Scored on his account of nature (P6). His work develops 'the implications of the basic physical laws of nature' (Parker, S4) with no special cases: a white dwarf above the limit must collapse whatever the expectations, against Eddington's insistence that 'stars do not behave in that way' (S4). In 1987 he gave the Kerr solution as an example of a search for abstract beauty matched exactly in nature (S5, paraphrased). No miracle, petition or exemption appears."
    C_ledger: {value: BELOW_THRESHOLD, how_known: "Nothing on judgement, afterlife, karma or moral reckoning in S1–S5. His atheism rules out a divine judge, but not every ledger (for example karma), so C is not inferred from it.", note: "Gap: Wali (1991, 1997)."}
    D_authority: {value: UNKNOWN, how_known: "No statement on revelation or scripture in S1–S5.", note: "A widely quoted remark that he could not accept the Bhagavad Gita as divine because it 'was written by man' comes through secondary web pages citing Wali (1997); not read, so not used."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Scored on the world's order (P7). Nothing read addresses favour for a group in events; not scored from working science alone (same treatment as Fermi and Curie)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus (4) and B_cause (4) are both only at 0.5, under the test's 0.7 bar (CODING_GUIDE §6). If A reached 0.7 from a quotable document, the test would give false (A ≥ 3), with certainty set by A alone (decision P10).", note: "Was false at 0.5 from P8 (2026-10-02) until the lens audit batch 3 fix the same day."}
  statements: []
  changes_over_life: []
  coder_notes: "ATHE, AGNOS and HINDU are stub system files (flag). Basis: decision P8 (2026-10-02) added basis recorded_interview (ceiling 0.7) for the person's own words in a recorded interview, but its last sentence says an interview that may only be paraphrased (an AIP no-quotation notice) cannot score an axis or code on its own. S5 carries that notice (header of the transcript: no quotation, reproduction or redistribution, in whole or in part, without AIP's written permission), and no permission is recorded, so S5 is treated as paraphrase-only, as Bohr's S7 is (lens audit batch 3, #19–#20). The two verbatim statements it once supplied (his remark on Struve and himself, and the 'simple is the seal of the true' answer) were removed; both can be read at the S5 locators. statements is empty after research: no quotable written or published statement of his on religion was read. nominal_affiliations and changes_over_life are empty after research: no adult membership or practice, and no dated change of belief, is recorded in S1–S5."

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
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "The only dated statement is from 1987 (S5); no earlier evidence read."}
  lio_views_relative_to_major_work: {value: "unclear", rationale: "The atheist self-description is late (1987) and undated as to origin.", certainty: 0.5, cites: [{source: S5, locator: "answer on whether Struve was religious"}], how_known: "(interview) Dates."}
  worldview_during_major_work: {value: "On his own later account, Struve knew during their Yerkes years (1937–1950) that he was an atheist", certainty: 0.5, cites: [{source: S5, locator: "answer on whether Struve was religious"}], how_known: "(interview) One retrospective remark (1987) about 1937–1950, paraphrased (AIP restricts quotation); dating his view to those years rests on hindsight, so 0.5."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", certainty: 0.5, cites: [{source: S3, locator: "paragraph 7"}], how_known: "Coder's reading of his own description of his method: after study he presents his view 'ab initio, in a coherent account with order, form, and structure' (S3)."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S4, locator: "Madras paragraph"}], how_known: "Early attraction to algebra and geometry (S4); nothing on how the method was formed."}
  circle_present: {value: "no", rationale: "A self-described atheist; no God-Nature identity in anything read.", certainty: 0.5, cites: [{source: S5, locator: "answer on whether Struve was religious"}], how_known: "(interview) One self-description."}
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
    - "Decision P8 (2026-10-02) first raised primary_system and A_locus to 0.7 (recorded_interview) and gave mid_basin false (0.5); the lens audit (batch 3, #19, #20, #25) showed that S5's AIP no-quotation notice brings it under P8's paraphrase limit, so both are back at 0.5 (scholarly_reconstruction) and mid_basin is BELOW_THRESHOLD. AIP's written permission, or a second quotable document (Wali 1991, 1997), would reopen this."
    - "S5 was read through the Wayback Machine copy of the AIP page (the live page redirects to a repository that refused the fetch); its wording was checked on that rendering, not saved locally."
  open_questions:
    - "Read Wali, Chandra (1991), p. 304, and Wali (ed.), S. Chandrasekhar: The Man Behind the Legend (1997), for the atheist statements and the Bhagavad Gita remarks."
    - "Read Truth and Beauty (1987) for any written statement on law, beauty and nature."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "\"Subrahmanyan Chandrasekhar.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Subrahmanyan-Chandrasekhar."
    url: "https://www.britannica.com/biography/Subrahmanyan-Chandrasekhar"
    accessed: 2026-10-02
    reliability_note: "Short editorial article; paragraphs counted from the opening."
    used_for: [identity, basics, contribution, childhood, institutions, collaborators, review]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "J J O'Connor and E F Robertson"
    citation: "O'Connor, J. J., and E. F. Robertson. \"Subrahmanyan Chandrasekhar.\" MacTutor History of Mathematics, University of St Andrews. https://mathshistory.st-andrews.ac.uk/Biographies/Chandrasekhar/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Chandrasekhar/"
    accessed: 2026-10-02
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
    reliability_note: "Official AIP transcript of a tape-recorded interview (as archived in 2015); mostly about Otto Struve. His own speech, not a written text. AIP restricts quotation without written permission, so the record paraphrases it and, under P8, it scores nothing on its own (same treatment as Bohr's S7). Located by topic."
    used_for: [basics, childhood, worldview, timing, lane_b, collaborators]
  - id: S6
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
---

# Subrahmanyan Chandrasekhar

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Subrahmanyan Chandrasekhar (1910–1995), Indian-born American astrophysicist, found the mass limit for white dwarfs on his 1930 voyage to England and won the 1983 Nobel Prize in Physics [S1, opening; paragraph 3]. Born into a "free-thinking, Tamil-speaking Brahmin family" [S4, opening sentence], he said in a 1987 interview, in passing, that Otto Struve knew he was an atheist [S5, paraphrased]. ATHE at 0.5 (interview; one paraphrase-only interview, decision P8); A 4 at 0.5 (interview) and B 4 at 0.5; C and E below threshold, D UNKNOWN; mid_basin below threshold.

## Life and work

Born in Lahore, educated at home, at the Hindu High School in Madras and at Presidency College, he went to Cambridge in 1930 and took his Ph.D. in 1933 [S3, paragraphs 1–4]. He held a Trinity Prize Fellowship (1933–37) and joined the University of Chicago in January 1937, where he stayed for the rest of his life [S3, paragraphs 4–5].

## Contribution and impact

The white-dwarf mass limit, then stellar dynamics, radiative transfer, hydrodynamic stability, ellipsoidal figures, relativity and black holes, each closed by a monograph [S3, the seven periods]. He edited the Astrophysical Journal from 1952 to 1971 [S2; S4].

## Childhood and education

His parents taught him at home until he was about twelve [S3, paragraph 2]. Algebra and geometry so attracted him that he worked through the textbooks before the school year began [S4]. He read Sommerfeld on his own and met Sommerfeld and Heisenberg in Madras [S4].

## Adult working worldview

The only statement of his own read is from a 1987 AIP interview, which AIP's notice lets the record paraphrase but not quote: asked whether Struve was religious, he said that Struve knew he was an atheist and never raised the subject with him [S5]. In the same interview he called the maxim that the simple is the seal of the true a description of the fundamental truths of science [S5]. Under decision P8 a paraphrase-only interview cannot score an axis or code on its own, so the code and A stay at 0.5. Scores: A 4 (0.5, interview), B 4 (0.5, mainly Parker's reconstruction); C and E below threshold, D UNKNOWN.

## Heritage (context only)

Tamil Brahmin, Hindu by birth [S4, opening sentence]. Context only.

## Timing

First lasting contribution 1930, at 20 [S1, paragraph 3; S4]. The dated evidence of his atheism is late (1987) [S5].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form present (he presents each field "ab initio, in a coherent account with order, form, and structure" [S3, paragraph 7]); no circle.

## Open questions

- Wali's biography (1991) and edited volume (1997); Truth and Beauty (1987).

## Research log

- 2026-10-02: Read Britannica, MacTutor, the Nobel autobiography, Parker's NAS memoir (National Academies Press reader; the nasonline PDF returned an HTML block page) and the AIP interview of 1987 (Wayback copy). Wali (1991) and the 1997 volume are lending-only on archive.org and could not be searched. The 1977 AIP interviews (Weart) were not reached.
