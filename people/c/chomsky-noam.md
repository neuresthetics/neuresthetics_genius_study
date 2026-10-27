---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z2)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to 20c_late. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (catch-up 1/13; never on the 215-row queue; F 5, rank 62). Own-voice A/B pass. A stays 4 @0.5 recorded_interview alt BELOW_THRESHOLD (P38 / RQ-Z2-1 held; refuses 'atheist' label S4; ignostic S3); support single→corroborated (S2 Raskin + S3 God reply + S6 Barsamian Chronicles 1992: religion 'not' a factor, 'child of the Enlightenment', avoid irrational belief; S9 Spiritual Human: does not use 'spiritual forces' himself). primary_system ATHE @0.5 unchanged (same hedge). B: drop P30/P35 scientist-from-linguistics route (standing rule: linguistics alone ≠ natural scientist for B). Own nature-order: Reddit AMA 2010 (S7) 'laws of nature enter … overwhelmingly' / physical-chemical channel for evolution; New Horizons ch.4 (S8; IJPS 1994 / CUP 2000) methodological naturalism hoping for 'eventual integration with the \"core\" natural sciences' and 'search for laws of nature'. B stays 3 @0.5 alt 4 (P16 Hilbert); basis scholarly_reconstruction→written_profession; support corroborated (S7+S8). McGilvray 'creative principle' (S1) kept as note only. mid_basin stays BELOW_THRESHOLD (A@0.5, P10). P47 source_quality on all sources. P50 dual bio: Britannica (S1) + Wikipedia EN Living people (S10); living after June 2023 stroke. Chart-moving: hollow→filled (both axes corroborated); faded stays (min=B@0.5). Do not force plot. No fallacy_catalog; no figures/. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z2 audit fixes (blind audit /workspace/genius_study_audit/gs_f70a593_Z2/run1/): Raskin interview dated 2022 (page metadata, 15 January 2022); 'Remarks on Religion' statement date UNKNOWN (the page says no date; '1990' is the URL slug); the ATHE rationale says the refusal of the 'atheist' label is why it is 0.5. RQ-Z2-1 answered: A 4 at 0.5 holds; plotted faded. No score changed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z2, order P32: F 5, rank 62; the gap found in batch Z1, filled on Jason's call that P32 governs). Basics from Britannica (James A. McGilvray, signed). Own voice: Max Raskin interview (2022): 'Do you believe in God?' 'For about a year.' 'But now you don't?' 'No.'; and his undated reply on chomsky.info: 'Do I believe in God? Can't answer, I'm afraid ... I don't understand the question.' Span 1955–1986 at 0.7. primary_system ATHE (0.5, alt BELOW_THRESHOLD); A 4 (0.5, alt BELOW_THRESHOLD; interview; P38 by analogy; RQ-Z2-1); B 3 (0.5, alt 4); C UNKNOWN; D BELOW_THRESHOLD; E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Plotted (faded) at the next chart refresh. Draft, not reviewed."}

identity:
  id: chomsky-noam
  display_name: "Noam Chomsky"
  roster:
    canonical_name: "Noam Chomsky"
    rank: 62
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: provisional
    field: linguistics
    field_bucket: linguistics
  full_name: {value: "Avram Noam Chomsky", certainty: 0.7, cites: [{source: S1, locator: "'In full'"}, {source: S10, locator: "infobox / Born"}], how_known: "Britannica; Wikipedia EN dual bio (P50)."}
  native_name: {value: "Avram Noam Chomsky", certainty: 0.7, cites: [{source: S1, locator: "'In full'"}], how_known: "Britannica."}
  aliases:
    - {name: "Chomsky-Noam", kind: "roster alias"}
    - {name: "Noam-Chomsky", kind: "roster alias"}

basics:
  birth:
    date: {value: "1928-12-07", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S10, locator: "infobox / Born"}], how_known: "Britannica; Wikipedia EN (P50)."}
    place: {value: "Philadelphia, Pennsylvania", modern_name: "Philadelphia, Pennsylvania, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S10, locator: "infobox / Born"}], how_known: "Britannica; Wikipedia EN (P50)."}
  death:
    date: {value: UNKNOWN, how_known: "Living as of Wikipedia EN 'Living people' and age-97 infobox read 2026-10-24 (S10); Britannica article still treats him as living (S1, prior read). Severe stroke June 2023; moved to Brazil full-time (S10)."}
    place: {value: UNKNOWN, how_known: "Living, per the sources read."}
  first_lasting_contribution_year: {value: 1955, certainty: 0.5, cites: [{source: S1, locator: "'Life and basic ideas' (LSLT; one chapter submitted as his Ph.D. dissertation, 1955)"}], how_known: "The Logical Structure of Linguistic Theory, written 1951–55, transformed Harris's and Goodman's ideas 'into something novel' (S1); dated by its formal submission, a chapter as his dissertation in 1955 (P30). Coder's call that LSLT is itself lasting; the alternative is Syntactic Structures (1957), so 0.5.", alternatives: [{value: 1957, note: "Syntactic Structures, the first published book.", cites: [{source: S1, locator: "'Life and basic ideas'"}]}]}
  era_bucket: {value: "1950 on", certainty: 1.0, cites: [{source: S1, locator: "'Life and basic ideas'"}], how_known: "Either candidate year falls in '1950 on' (P2)."}
  region_of_birth: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "United States (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "'Life and basic ideas'"}], how_known: "MIT; University of Arizona."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
  occupations: {value: ["theoretical linguist", "professor (MIT; University of Arizona)", "political writer and activist"], certainty: 0.7, cites: [{source: S1, locator: "opening; 'Life and basic ideas'"}], how_known: "Britannica."}

contribution:
  era_bucket: 20c_late
  fields: {value: ["linguistics", "cognitive science", "philosophy of mind and language", "political criticism"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "The Logical Structure of Linguistic Theory (generative grammar)", year: 1955, kind: theory, lasting: "transformed his teachers' approaches 'into something novel'; the 'fundamental problem' of linguistics it named became 'Plato's problem' (S1)", certainty: 0.5, cites: [{source: S1, locator: "'Life and basic ideas'; 'Plato's problem'"}], how_known: "Britannica; dated by the 1955 dissertation submission (P30); lasting is the coder's call."}
    - {value: "Syntactic Structures", year: 1957, kind: work, lasting: "led MIT to found its linguistics graduate program (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Life and basic ideas'"}], how_known: "Britannica."}
    - {value: "Review of Skinner's Verbal Behavior", year: 1959, kind: work, lasting: "'came to be regarded as the definitive refutation of behaviourist accounts of language learning' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Life and basic ideas'"}], how_known: "Britannica."}
    - {value: "Principles and parameters (Lectures on Government and Binding, 1981; Knowledge of Language, 1986)", year: 1981, kind: theory, lasting: "'offering what appears to be the best solution to Plato's problem yet proposed'; the parameter hypothesis 'supported by empirical evidence' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Principles and parameters'"}], how_known: "Britannica; range 1981–1986, so the span ends in 1986 (P30 addendum)."}
  evidence_of_impact:
    - {value: "Helped initiate and sustain the 'cognitive revolution'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works:
    - {value: "Aspects of the Theory of Syntax", year: 1965, kind: book, certainty: 0.7, cites: [{source: S1, locator: "'Life and basic ideas'"}], how_known: "Britannica."}
    - {value: "Cartesian Linguistics", year: 1966, kind: book, certainty: 0.7, cites: [{source: S1, locator: "'Life and basic ideas'"}], how_known: "Britannica."}
    - {value: "New Horizons in the Study of Language and Mind", year: 2000, kind: book, certainty: 0.7, cites: [{source: S8, locator: "title page / contents"}], how_known: "Cambridge University Press collection; ch. 4 used for B (own nature-order / methodological naturalism)."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "His work 'revolutionized the field of linguistics' (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Jewish (Hebraist; father a Hebrew educator)", certainty: 0.7, cites: [{source: S1, locator: "'Life and basic ideas' ('a middle-class Jewish family')"}, {source: S2, locator: "Yiddishists and Hebraists; Kibbutznik"}], how_known: "Britannica and his own words (interview)."}
  family_religious_practice: {value: "Kept the practices as a child ('I did what my parents did'); read Hebrew with his father every Friday night", certainty: 0.7, cites: [{source: S2, locator: "Kibbutznik; Yiddishists and Hebraists"}], how_known: "(interview) His own words."}
  parents_and_household:
    - {value: "Father a Hebrew educator who ran Philadelphia's Hebrew education programs and wrote a dissertation on David Kimhi", role: father, certainty: 0.7, cites: [{source: S2, locator: "early exposure answer; Hebraists answer"}], how_known: "(interview) His own words."}
  household_circumstances: {value: "Middle-class Jewish family in a Hebraist community", certainty: 0.7, cites: [{source: S1, locator: "'Life and basic ideas'"}], how_known: "Britannica."}
  schooling:
    - {value: "Experimental elementary school with self-directed learning", stage: "elementary school", run_by: other, years: "1930s", certainty: 0.7, cites: [{source: S1, locator: "'Life and basic ideas'"}], how_known: "Britannica; run_by not stated."}
    - {value: "University of Pennsylvania (Ph.D. linguistics 1955)", stage: university, run_by: private, years: "1945–1955", certainty: 0.7, cites: [{source: S1, locator: "'Life and basic ideas'"}], how_known: "Britannica."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated before 18; he later studied mathematics with Nathan Fine (S1)."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading:
    - {value: "His father's dissertation on David Kimhi, at about 10 or 11; Ahad Ha'am", certainty: 0.7, cites: [{source: S2, locator: "early exposure answer"}], how_known: "(interview) His own words."}
  childhood_mentors: []
  languages_in_childhood: {value: ["English", "Hebrew"], certainty: 0.7, cites: [{source: S2, locator: "Hebraists answer"}], how_known: "(interview) His own words."}
  notable_events:
    - {value: "At about 11 or 12 wanted to be 'more religious than my father'; it lasted 'about a year or two'", year: 1940, certainty: 0.5, cites: [{source: S2, locator: "Kibbutznik"}], how_known: "(interview) His own retrospective; year the coder's (age 11–12)."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1955–1986", certainty: 0.7, cites: [{source: S1, locator: "'Life and basic ideas'; 'Principles and parameters'"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "'Science and religion are just incommensurable'; disagrees with Gould's 'non-overlapping magisteria' (2006)", certainty: 0.5, cites: [{source: S4, locator: "'On Stephen Jay Gould'"}], how_known: "(interview) Published conversation with Lawrence Krauss (web copy, after the span), so 0.5."}
  primary_system:
    value: ATHE
    basis: recorded_interview
    certainty: 0.5
    cites: [{source: S2, locator: "Kibbutznik"}, {source: S3, locator: "reply on belief in God"}, {source: S6, locator: "Barsamian / Chronicles of Dissent (religion not a factor; Enlightenment)"}]
    how_known: "(interview) 'Do you believe in God?' 'For about a year.' 'But now you don't?' 'No.' No afterlife; not thought about it 'since I was a teenager' (S2, after the span). Barsamian (1992): religion 'For me, it's not' a factor; 'I am a child of the Enlightenment'; 'irrational belief is a dangerous phenomenon, and I try to consciously avoid irrational belief' (S6). He rejects both labels when the term is undefined: 'I don't even know what an atheist is' and 'I don't see how one can be an agnostic' (S4); of something that 'stands above' the universe, 'I've never heard of any reason for believing that' (S3). Named alternative BELOW_THRESHOLD, so 0.5."
    rationale: "ATHE: no God and no religious belief, with no stated suspension (AGNOS needs explicit suspension; he rejects agnosticism, S4). The alternative is BELOW_THRESHOLD, since his main public answer is that the question is unclear (S3). Consistent with Penrose (P38 ruling W3): a hedged first-person position gives 0.5; his refusal of the 'atheist' label (S4) is why it is 0.5 and not 0.7. Deepen adds Barsamian and Spiritual Human corroboration; certainty unchanged."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: ATHE, reason: "Coded at 0.5 (S2, S3, S6)."}
    - {code: AGNOS, reason: "Rejected: he rejects agnosticism as a coherent position for an undefined term (S4)."}
    - {code: JUDA, reason: "Rejected: heritage and childhood practice only; symbolic observance as an adult (S2)."}
  lio_axes:
    A_locus:
      value: 4
      basis: recorded_interview
      certainty: 0.5
      support: corroborated
      cites: [{source: S2, locator: "Kibbutznik"}, {source: S3, locator: "reply on belief in God"}, {source: S6, locator: "Barsamian / Chronicles of Dissent"}, {source: S4, locator: "atheist / agnostic exchange"}, {source: S9, locator: "spiritual forces / I don't use the concept myself"}]
      how_known: "(interview) A stated non-belief ('No', S2), held since his teens by his own retrospective account, so it covers the span (P20 retrospective cap 0.7). Barsamian (S6): religion not a factor; Enlightenment; avoids irrational belief. Spiritual Human (S9): 'I don't use the concept [spiritual forces] myself.' With his 'Can't answer ... I don't understand the question' (S3) and atheist-label refusal (S4) as the named alternative, 0.5 (P38 by analogy; RQ-Z2-1 held on deepen). Support corroborated: S2+S3+S6 (+S4,S9); alt sources ⊆ main."
      rationale: "No separate God: he does not believe in God and sees no reason to believe in something that 'stands above' the universe (S3); religion is not a factor in who he is (S6). Named alternative BELOW_THRESHOLD: he declines to answer the question as posed and refuses the atheist label when undefined (S3, S4)."
      alternatives:
        - {value: BELOW_THRESHOLD, note: "Ignostic answer: 'I don't know whether I believe or don't believe in whatever a questioner has in mind' (S3); 'I don't even know what an atheist is' (S4).", cites: [{source: S3, locator: "reply on belief in God"}, {source: S4, locator: "atheist / agnostic exchange"}]}
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.5
      support: corroborated
      cites: [{source: S8, locator: "ch. 4 pp. 76–77 (methodological naturalism; core natural sciences)"}, {source: S7, locator: "laws of nature enter … overwhelmingly; physical, chemical channel"}]
      how_known: "Deepen drops the prior P30/P35 scientist-from-linguistics route (standing rule: linguistics alone is not enough for scientist-B). Own nature-order statements: (1) New Horizons ch. 4 (written_profession; Howison/Agnes Cuming lecture 1993, IJPS 1994, CUP 2000): a naturalistic approach 'investigates mental aspects of the world as we do any others, seeking to construct intelligible explanatory theories, with the hope of eventual integration with the \"core\" natural sciences' (S8 pp. 76–77); related ch. 2 places serious realism 'in the context of the search for laws of nature' (S8 p. 21). (2) Reddit AMA 2010 (recorded_interview, chomsky.info): 'how do laws of nature enter into the growth and development of the system? Which of course they do, overwhelmingly' — cells split into spheres by minimization of energy / other laws of nature; 'Evolution takes place with a specific physical, chemical channel of options and possibilities, and physical laws enter all the time' (S7). After the span (P20) and no stated no-exception claim → 0.5 with alt 4 (P16 Hilbert). Support corroborated: S8+S7. McGilvray's 'creative principle' / uncaused language-use reconstruction (S1) is no longer the scoring route."
      rationale: "Scored on his account of nature (P6), not on scientist status. Lawful nature: laws of nature enter development and evolution overwhelmingly (S7); mental/linguistic inquiry aims at unification with the core natural sciences in the search for laws of nature (S8). No stated exceptionless order or miracle-denial (P40) → B 3 at 0.5, alternative 4 (P16 Hilbert addendum)."
      alternatives:
        - {value: 4, note: "P16 Hilbert / P40: lawful-order remarks without a no-exception claim cannot tell lawful-with-exceptions from exceptionless.", cites: [{source: S7, locator: "laws of nature enter … overwhelmingly"}, {source: S8, locator: "pp. 76–77"}]}
    C_ledger: {value: UNKNOWN, how_known: "No afterlife ('No', S2; 'I know of no reason to believe in an afterlife or divine justice' via S9 compilation 2020), but nothing read on reward and punishment of persons (P19)."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "(interview) Leads toward 4: the Bible 'is not a historical text' (S3), and authority 'that cannot meet a strong test of rational justification is illegitimate', 'political, economic, or religious' (S1, Britannica's summary of his beliefs). But he calls science and religion 'incommensurable' (S4), and nothing read ranks revelation against observation in his own words."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Not scored from working science or methodological naturalism alone (P19); 'physical laws enter all the time' (S7) and hope of unification with core natural sciences (S8) are leads, not a same-laws-everywhere claim (P7)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A 4 at 0.5: the A ≥ 3 branch reads A only and needs 0.7 (P10), as for Russell and Crick. Deepen did not lift A past 0.5 (P38 / RQ-Z2-1)."}
  statements:
    - text: "MR: Do you believe in God? NC: For about a year. MR: But now you don't? NC: No. MR: Do you believe in an afterlife? NC: No."
      cites: [{source: S2, locator: "Kibbutznik"}]
      date: "2022"
      context: "Max Raskin's interview, published 15 January 2022 (the page's datePublished metadata)."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "Interviewer's published transcript. After the span (P20)."
    - text: "Do I believe in God? Can’t answer, I’m afraid. I’m not being flippant, but I don’t understand the question. What is it that I am supposed to believe or not believe in? Are you asking whether I believe there is something not in the universe (or the universes, if there are (maybe infinitely) many of them), and that somehow stands above them? I’ve never heard of any reason for believing that."
      cites: [{source: S3, locator: "reply on belief in God"}]
      context: "Reply to a forum query, collected on chomsky.info as 'Remarks on Religion'; the page says '[No date available]' (the URL's 1990 is only the site's filing slug)."
      axes: [A_locus]
      kind: "other"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "Web copy on his authorised archive site; date unknown."
    - text: "For me, it's not. I am a child of the Enlightenment. I think irrational belief is a dangerous phenomenon, and I try to consciously avoid irrational belief."
      cites: [{source: S6, locator: "Barsamian / Chronicles of Dissent"}]
      date: "1992"
      context: "David Barsamian interview in Chronicles of Dissent (Common Courage, 1992), collected on chomsky.info 'Remarks on Religion'. Reply to whether the spiritual dimension in terms of religion is a factor in who he is."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Web copy of print interview (P26 cap 0.7)."
    - text: "Science and religion are just incommensurable."
      cites: [{source: S4, locator: "'On Stephen Jay Gould'"}]
      date: "2006-03-01"
      context: "Conversation with Lawrence Krauss, 'Science in the Dock' (Discover, March 2006), on chomsky.info."
      axes: [D_authority]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "Web copy (P26 cap 0.7)."
    - text: "And the third is: how do laws of nature enter into the growth and development of the system? Which of course they do, overwhelmingly. I mean, nobody, for example, assumes that you have a particular genetic program to determine that cells split into spheres, not cubes, let's say — that's due to, you know, minimization of energy, other laws of nature. And the same holds throughout the course of development. Of course, the same is true for evolution. Evolution takes place with a specific physical, chemical channel of options and possibilities, and physical laws enter all the time into determining what goes on."
      cites: [{source: S7, locator: "laws of nature / physical, chemical channel"}]
      date: "2010-03-12"
      context: "Reddit Blog AMA, 'Chomsky on Cognitive Science, and Anarchism', 12 March 2010; web copy on chomsky.info."
      axes: [B_cause]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "After the span (P20). Own nature-order statement for B (standing rule: not scientist-B from linguistics alone)."
    - text: "Let us also understand the term \"naturalism\" without metaphysical connotations: a \"naturalistic approach\" to the mind investigates mental aspects of the world as we do any others, seeking to construct intelligible explanatory theories, with the hope of eventual integration with the \"core\" natural sciences."
      cites: [{source: S8, locator: "ch. 4 pp. 76–77"}]
      date: "2000"
      context: "New Horizons in the Study of Language and Mind, ch. 4 'Naturalism and dualism in the study of language and mind' (CUP 2000); edited from Agnes Cuming Lectures (UCD, April 1993); first published IJPS 1994, 2: 181–200."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "After the span (P20). Corroborates Reddit laws-of-nature line for B."
  changes_over_life:
    - {value: "A religious phase at about 11–12 ('more religious than my father'; believed in God 'for about a year'), then non-belief from his teens", certainty: 0.5, cites: [{source: S2, locator: "Kibbutznik"}], how_known: "(interview) His own retrospective."}
  coder_notes: "Deepen D1 coder's calls: (1) NOT a natural scientist for B from linguistics alone (standing catch-up rule); B rests on own nature-order statements (S7, S8), Hilbert/P16 path, not P30/P35; (2) span 1955–1986 unchanged; (3) RQ-Z2-1 held: A 4 @0.5 with alt BELOW, not lifted to 0.7 despite corroboration (P38 / atheist-label refusal); (4) McGilvray creative-use exception (S1) demoted from scoring route to context; (5) chart fill may go hollow→filled at next refresh; darkness stays faded."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "American Jewish (Hebraist family of Eastern European origin)", certainty: 0.7, cites: [{source: S1, locator: "'Life and basic ideas'"}, {source: S2, locator: "Roosevelt and Trump"}], how_known: "Britannica and his own words."}
  religious_heritage_by_birth: {value: "Jewish", certainty: 0.7, cites: [{source: S1, locator: "'Life and basic ideas'"}], how_known: "Britannica."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: "Hebrew education in his parents' Hebraist community", certainty: 0.5, cites: [{source: S2, locator: "Hebraists answer"}], how_known: "(interview) Coder's reading of his account."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1955–1986", certainty: 0.7, cites: [{source: S1, locator: "'Life and basic ideas'; 'Principles and parameters'"}], how_known: "LSLT (1955) to Knowledge of Language (1986) (P29, P30); the start year is at 0.5 in basics."}
  age_at_first_lasting_contribution: {value: 27, certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "1955 − 1928 = 27 (P30); 29 under the 1957 alternative."}
  first_evidence_of_lio_type_views: {value: "c. 1992 Barsamian interview (non-belief / Enlightenment); teen onset by 2022 retrospective", certainty: 0.5, cites: [{source: S6, locator: "Barsamian"}, {source: S2, locator: "Kibbutznik"}], how_known: "(interview) Deepen adds dated Barsamian; Raskin still the teen-onset retrospective."}
  lio_views_relative_to_major_work: {value: "before major work", certainty: 0.5, cites: [{source: S2, locator: "Kibbutznik"}], how_known: "(interview) By his own retrospective, non-belief from his teens."}
  worldview_during_major_work: {value: "Non-believer by his own retrospective account", certainty: 0.5, cites: [{source: S2, locator: "Kibbutznik"}], how_known: "(interview) Retrospective."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "Studied formal systems with Goodman and mathematics with Fine; LSLT applies formal systems (S1).", certainty: 0.5, cites: [{source: S1, locator: "'Life and basic ideas'"}], how_known: "Coder's reading."}
  form_acquired: {value: "adulthood, before major work", certainty: 0.5, cites: [{source: S1, locator: "'Life and basic ideas'"}], how_known: "Graduate study."}
  circle_present: {value: "no", rationale: "Nothing read identifies the divine with nature.", certainty: 0.5, cites: [{source: S3, locator: "reply on belief in God"}], how_known: "Coder's reading."}
  reading: "Formal method without any God-in-nature belief: a case against H1 as belief. Own nature-order statements (laws of nature; methodological naturalism) score B on Lane A without implying pantheism."
  notes: ""

institutions:
  - {value: "Massachusetts Institute of Technology", role: "from 1956; Institute Professor 1976; emeritus 2002", years: "1956–2002", kind: university, certainty: 0.7, cites: [{source: S1, locator: "'Life and basic ideas'"}], how_known: "Britannica."}
  - {value: "University of Arizona", role: "laureate professor of linguistics", years: "2017–", kind: university, certainty: 0.7, cites: [{source: S1, locator: "'Life and basic ideas'"}], how_known: "Britannica."}
collaborators:
  - {value: "Zellig S. Harris", relation: teacher, note: "mentor at Penn", certainty: 0.7, cites: [{source: S1, locator: "'Life and basic ideas'"}], how_known: "Britannica."}
  - {value: "Morris Halle", relation: collaborator, note: "co-founded MIT's linguistics graduate program", certainty: 0.7, cites: [{source: S1, locator: "'Life and basic ideas'"}], how_known: "Britannica."}
  - {value: "B.F. Skinner", roster_id: skinner-b-f, relation: "rival or critic", note: "Chomsky's 1959 review of Verbal Behavior", certainty: 0.7, cites: [{source: S1, locator: "'Life and basic ideas'"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Provisional in v8 (F 5).", certainty: 0.7, cites: [{source: S5, locator: "roster.csv, rank 62"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "The record was missing until batch Z2 although P32 put him first among the uncoded; filled on Jason's call (2026-10-19)."
    - "The chomsky.info undated God reply remains undated; Barsamian 1992 on the same Remarks page is dated."
    - "B nature-order evidence is post-span (1993/94 essay; 2010 AMA); certainty already capped 0.5 by P16 alt 4."
  open_questions:
    - "RQ-Z2-1 held on deepen: A 4 @0.5 (P38), not BELOW_THRESHOLD and not 0.7."
    - "Optional: print check Chronicles of Dissent Barsamian pages; in-span (1955–1986) nature-order essay if any (unlikely to lift B above 0.5 under P16)."
    - "C still UNKNOWN (no afterlife ≠ ledger)."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "James A. McGilvray"
    citation: "McGilvray, James A. \"Noam Chomsky.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Noam-Chomsky (and /Linguistics). Read live 2026-10-19; living status re-checked 2026-10-24."
    url: "https://www.britannica.com/biography/Noam-Chomsky"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Signed article by a Chomsky scholar; body cited, question boxes not cited (P26). Creative-use / 'uncaused' language-use lines are McGilvray's reconstruction — not used for B on deepen."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: primary
    kind: other
    author: "Noam Chomsky, interviewed by Max Raskin"
    citation: "Raskin, Max. \"Interview with Noam Chomsky.\" maxraskin.com, 15 January 2022. https://www.maxraskin.com/interviews/noam-chomsky"
    url: "https://www.maxraskin.com/interviews/noam-chomsky"
    accessed: 2026-10-19
    source_quality: "primary / own words"
    reliability_note: "Interviewer's published transcript (recorded_interview, P8)."
    used_for: [childhood, worldview, heritage, timing]
  - id: S3
    type: primary
    kind: other
    author: "Noam Chomsky"
    citation: "Chomsky, Noam. \"Remarks on Religion\" (reply to a forum query; no date available). chomsky.info. https://chomsky.info/1990____/"
    url: "https://chomsky.info/1990____/"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "His own written reply, on the archive site; date unknown; web copy. Same page also hosts Barsamian and Jones excerpts (cited as S6)."
    used_for: [worldview, lane_b]
  - id: S4
    type: primary
    kind: other
    author: "Noam Chomsky and Lawrence Krauss"
    citation: "\"Science in the Dock.\" Discussion with Lawrence Krauss, Discover, March 2006; chomsky.info. https://chomsky.info/20060301/"
    url: "https://chomsky.info/20060301/"
    accessed: 2026-10-19
    source_quality: "primary / own words"
    reliability_note: "Published conversation (recorded_interview), web copy."
    used_for: [worldview]
  - id: S5
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    source_quality: "study roster"
    reliability_note: "Study's own roster."
    used_for: [identity, review]
  - id: S6
    type: primary
    kind: other
    author: "Noam Chomsky, interviewed by David Barsamian"
    citation: "Barsamian, David. Interview in Chronicles of Dissent (Common Courage, 1992); excerpted on chomsky.info \"Remarks on Religion\". https://chomsky.info/1990____/"
    url: "https://chomsky.info/1990____/"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "Print interview, web copy on authorised archive (recorded_interview, P8; P26 cap 0.7)."
    used_for: [worldview, timing]
  - id: S7
    type: primary
    kind: other
    author: "Noam Chomsky"
    citation: "\"Chomsky on Cognitive Science, and Anarchism.\" Reddit Blog AMA, 12 March 2010; chomsky.info. https://chomsky.info/20100312/"
    url: "https://chomsky.info/20100312/"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "Authorised archive transcript of Reddit AMA (recorded_interview, P8)."
    used_for: [worldview]
  - id: S8
    type: primary
    kind: published work by the subject
    author: "Noam Chomsky"
    citation: "Chomsky, Noam. New Horizons in the Study of Language and Mind. Cambridge: Cambridge University Press, 2000. Ch. 4 \"Naturalism and dualism in the study of language and mind\" (pp. 75ff.; from Agnes Cuming Lectures 1993; IJPS 1994, 2: 181–200). Also ch. 2 p. 21 ('search for laws of nature'). PDF read 2026-10-24."
    url: "https://doi.org/10.1017/CBO9780511811937"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "His CUP essay collection; ch. 4 is own professional writing (written_profession)."
    used_for: [contribution, worldview]
  - id: S9
    type: primary
    kind: other
    author: "Noam Chomsky, interviewed by Musa Askari"
    citation: "Askari, Musa. \"Noam Chomsky interviewed by Musa Askari.\" Spiritual Human, 2011. https://spiritualhuman.wordpress.com/ (quote also in In-Sight Publishing compilation \"Noam Chomsky on God\")."
    url: "https://spiritualhuman.wordpress.com/"
    accessed: 2026-10-24
    source_quality: "unofficial web copy"
    reliability_note: "Interview on a personal site; used as corroboration that he does not use 'spiritual forces' himself, not as sole A evidence."
    used_for: [worldview]
  - id: S10
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "\"Noam Chomsky.\" Wikipedia EN. https://en.wikipedia.org/wiki/Noam_Chomsky . Read live 2026-10-24 (Living people; born 1928-12-07 Philadelphia; stroke June 2023)."
    url: "https://en.wikipedia.org/wiki/Noam_Chomsky"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "P50 dual bio with Britannica for living status and birth facts."
    used_for: [identity, basics]

---

# Noam Chomsky

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Noam Chomsky (born 1928), American theoretical linguist [S1; S10]. Deepen D1: primary_system ATHE (0.5, alt BELOW_THRESHOLD; interview); A 4 (0.5, alt BELOW_THRESHOLD; interview; corroborated; RQ-Z2-1 held); B 3 (0.5, alt 4; written_profession; corroborated; own nature-order, not scientist-from-linguistics); C UNKNOWN; D, E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Plotted faded; fill may become filled at next refresh (both axes corroborated).

## Life and work

Philadelphia, Penn, Harvard, MIT from 1956 [S1]. Living after a June 2023 stroke; moved to Brazil full-time [S10].

## Contribution and impact

LSLT (1955), Syntactic Structures (1957), the Skinner review (1959), principles and parameters (1981–1986) [S1]. New Horizons (2000) for methodological naturalism [S8].

## Childhood and education

Hebraist Jewish family; a religious phase at 11–12 (interview) [S1; S2].

## Adult working worldview

Does not believe in God (interview), while calling the question unclear; religion not a factor; child of the Enlightenment [S2; S3; S6]. Laws of nature enter development and evolution overwhelmingly; naturalistic inquiry aims at integration with the core natural sciences [S7; S8].

## Heritage (context only)

Jewish [S1].

## Timing

1955–1986, from age 27 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Formal method, no God-in-nature belief [S1; S3]. Own nature-order statements score B on Lane A without pantheism.

## Open questions

- RQ-Z2-1 held (A 4 @0.5).
- C still UNKNOWN.

## Research log

- 2026-10-19: Read Britannica (McGilvray; two sections), the Raskin interview, and two chomsky.info texts.
- 2026-10-24: Deepen D1 (catch-up 1/13). Barsamian Chronicles 1992 (S6); Reddit AMA 2010 (S7); New Horizons ch. 4 PDF (S8); Spiritual Human 2011 (S9); Wikipedia EN dual bio (S10). B re-based on own nature-order; A/B support corroborated; P47 labels. No fallacy_catalog; no figures/.
