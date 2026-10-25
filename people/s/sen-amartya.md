---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z3; deepen D1 catch-up 5/13)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z3, order P32: F 3, rank 146). Basics from Britannica (Editors) and his Nobel autobiography. Own voice: Calcutta Press Club, December 1998, as reported by Rediff: 'Although this is a personal matter... But the answer to your question is: No. I do not believe in god.'; interview with Roy McCloughry (29 July 2009): his grandfather said he had placed himself 'on the atheistic branch of Hinduism'; 'relying on faith goes against reason'. Not a scientist (economist; Keynes precedent), so B UNKNOWN. Span 1970–1999 at 0.5. primary_system ATHE (0.5, alt BELOW_THRESHOLD); A 4 (0.5, alt BELOW_THRESHOLD); B UNKNOWN; C UNKNOWN; D BELOW_THRESHOLD; E UNKNOWN; mid_basin BELOW_THRESHOLD. Not plotted (no B). Draft, not reviewed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (catch-up 5/13; F3 rank 146). Goals: firm A/primary if sources allow; B only with nature-order own words (not economist working science); do not force plot. Opened Forman / Metro Santa Cruz archive at Good Times (S6, 4–11 Oct 2006); NDTV Prannoy Roy full transcript on Home in the World (S7, 2021); Wikipedia EN + bn.wikipedia title (S8, P50). Native name অমর্ত্য সেন; birth name Amartya Kumar Sen confirmed. primary_system stays ATHE @0.5: basis recorded_interview now on S6 own-voice ('I think it's an atheist position') + S4 + S3; alternative BELOW_THRESHOLD → AGNOS (S6 modest-moments hedge). A 4 stays @0.5 under P38 (atheist + would not object to agnostic); support single → corroborated (S6+S4+S3; P48); alt BELOW_THRESHOLD kept (P38). B stays UNKNOWN (P30 economist; Forman objective-truth remarks are social-science epistemology, not P16 nature-order; Newtonian-bullet NDTV anecdote is physics of projectiles, not worldview). C/D/E/mid unchanged. Chart-moving NO. P47 source_quality on S1–S8. No fallacy_catalog. No figures/. Draft, not reviewed."}

identity:
  id: sen-amartya
  display_name: "Amartya Sen"
  roster:
    canonical_name: "Amartya Sen"
    rank: 146
    F: 3
    models: [Claude, DeepSeek, GPT]
    band: "core (3–4)"
    status: provisional
    field: economics
    field_bucket: "social science"
  full_name: {value: "Amartya Kumar Sen", certainty: 0.7, cites: [{source: S8, locator: "infobox birth_name"}, {source: S1, locator: "opening"}], how_known: "Wikipedia birth_name; Britannica."}
  native_name: {value: "অমর্ত্য সেন", certainty: 0.7, cites: [{source: S8, locator: "bn.wikipedia title; EN IPA bn"}], how_known: "Bengali Wikipedia title অমর্ত্য সেন; EN Wikipedia Bengali IPA (P50)."}
  aliases:
    - {name: "Amartya-Sen", kind: "roster alias"}
    - {name: "Amartya Kumar Sen", kind: "birth name", cites: [{source: S8, locator: "infobox birth_name"}]}

basics:
  birth:
    date: {value: "1933-11-03", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "Born"}], how_known: "Britannica."}
    place: {value: "Santiniketan, Bengal", modern_name: "Santiniketan, West Bengal, India", polity_then: "British India", certainty: 0.7, cites: [{source: S1, locator: "Born"}, {source: S2, locator: "opening"}], how_known: "Britannica; Nobel autobiography ('born in a University campus')."}
  death:
    date: {value: UNKNOWN, how_known: "Living per the sources read (2026)."}
    place: {value: UNKNOWN, how_known: "Living."}
  first_lasting_contribution_year: {value: 1970, certainty: 0.7, cites: [{source: S1, locator: "text ('His influential monograph Collective Choice and Social Welfare (1970)')"}], how_known: "Britannica."}
  era_bucket: {value: "1950 on", certainty: 1.0, cites: [{source: S1, locator: "text"}], how_known: "1970 (P2)."}
  region_of_birth: {value: "South Asia", certainty: 0.7, cites: [{source: S1, locator: "Born"}], how_known: "India (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "LSE, London, Oxford 1971–88 hold most of the span; Delhi before and Harvard after, so 0.5."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
  occupations: {value: ["economist", "philosopher", "professor (Delhi, LSE, Oxford, Harvard); Master of Trinity College, Cambridge"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}

contribution:
  fields: {value: ["welfare economics", "social choice theory", "development economics", "philosophy"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Collective Choice and Social Welfare", year: 1970, kind: work, lasting: "'inspired researchers to turn their attention to issues of basic welfare' (S1)", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
    - {value: "Entitlement theory of famine (Poverty and Famines)", year: 1981, kind: theory, lasting: "'Governments and international organizations handling food crises were influenced by Sen's work' (S1)", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
    - {value: "Development as Freedom", year: 1999, kind: work, lasting: "listed among his major works (S1)", certainty: 0.5, cites: [{source: S1, locator: "'What did Amartya Sen write?'; text"}], how_known: "Britannica; lasting is the coder's call, so the span end is 0.5."}
  evidence_of_impact:
    - {value: "Nobel Memorial Prize in Economic Sciences 1998", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works:
    - {value: "The Idea of Justice", year: 2009, kind: book, certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
    - {value: "Home in the World: A Memoir", year: 2021, kind: book, certainty: 0.7, cites: [{source: S7, locator: "title; memoir passages"}], how_known: "NDTV interview on the memoir."}
  honours:
    - {value: "Nobel Memorial Prize in Economic Sciences", year: 1998, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  definition_fit: {value: "clearly meets", rationale: "Called the 'conscience of his profession'; Nobel 1998 (S1).", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Hindu: parents believed in God without institutional practice; grandfather a scholar of Hinduism", certainty: 0.5, cites: [{source: S4, locator: "first answer"}], how_known: "(interview) His own words (2009)."}
  family_religious_practice: {value: "'no particular institutional activity'; reading religious texts encouraged", certainty: 0.5, cites: [{source: S4, locator: "first answer"}], how_known: "(interview) His own words."}
  parents_and_household:
    - {value: "Kshiti Mohan Sen, maternal grandfather, Sanskritist and scholar of Hinduism at Visva-Bharati", role: grandparent, certainty: 0.7, cites: [{source: S2, locator: "opening"}, {source: S4, locator: "first answer"}], how_known: "Nobel autobiography; interview."}
    - {value: "Amita Sen, mother, former Santiniketan student", role: mother, certainty: 0.7, cites: [{source: S2, locator: "opening"}], how_known: "Nobel autobiography."}
  household_circumstances: {value: "University family from Dhaka; childhood in Dhaka, Mandalay and Santiniketan", certainty: 0.7, cites: [{source: S2, locator: "opening"}], how_known: "Nobel autobiography."}
  schooling:
    - {value: "St Gregory's School, Dhaka", stage: "elementary school", run_by: "religious body", years: "1930s", certainty: 0.5, cites: [{source: S2, locator: "opening"}], how_known: "Nobel autobiography; run_by the coder's (a missionary school), so 0.5."}
    - {value: "Tagore's Visva-Bharati school, Santiniketan", stage: "grammar or secondary school", run_by: private, years: "1940s", certainty: 0.7, cites: [{source: S2, locator: "opening"}], how_known: "Nobel autobiography."}
    - {value: "Presidency College, Calcutta; Trinity College, Cambridge (Ph.D. 1959)", stage: university, run_by: other, years: "1951–1959", certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S2, locator: "Presidency College"}], how_known: "Britannica; Nobel autobiography."}
  early_mathematics: {value: "other", certainty: 0.5, cites: [{source: S7, locator: "Calcutta / football anecdote from memoir"}], how_known: "(interview) Memoir: 'quite strongly hooked at that time on mathematics and physics, with only Sanskrit as a possible rival' — level not specified, so other."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "Kshiti Mohan Sen", certainty: 0.7, cites: [{source: S4, locator: "first answer"}], how_known: "(interview) He grew up with him."}
  languages_in_childhood: {value: ["Bengali"], certainty: 0.7, cites: [{source: S8, locator: "bn.wikipedia; EN IPA bn"}, {source: S2, locator: "opening"}], how_known: "Bengali native name and family; Nobel autobiography."}
  notable_events:
    - {value: "Witnessed the Bengal famine of 1943", year: 1943, certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S2, locator: "Presidency College"}], how_known: "Britannica; Nobel autobiography."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1970–1999", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "'relying on faith goes against reason' (2009); ethics not based on religious beliefs (2006)", certainty: 0.5, cites: [{source: S4, locator: "faith schools answer"}, {source: S6, locator: "religious views exchange"}], how_known: "(interview) After the span."}
  primary_system:
    value: ATHE
    basis: recorded_interview
    certainty: 0.5
    cites: [{source: S6, locator: "religious views exchange"}, {source: S4, locator: "first answer"}, {source: S3, locator: "paragraphs 1–3"}]
    how_known: "(interview) Own voice, 2006: 'I think it's an atheist position' (S6); 2009 grandfather placed him on the 'atheistic branch of Hinduism' / Lokayata (S4); 1998 press-club 'No. I do not believe in god' as reported (S3). Certainty held at 0.5 because he also accepts 'agnostic' in modest moments (S6) and names AGNOS as alternative."
    rationale: "ATHE: stated non-belief / atheist position with no suspension of judgment as his preferred label. Alternative AGNOS: S6 'in my modest moments I wouldn't object to being called an agnostic'."
    alternatives:
      - {value: AGNOS, note: "S6 modest-moments hedge; Buddha's unresolved-god point is descriptive of Buddha, not a self-label.", cites: [{source: S6, locator: "Would that make you agnostic or atheist?"}]}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: ATHE, reason: "Coded at 0.5; firmed with S6 own-voice."}
    - {code: AGNOS, reason: "Named alternative only (S6 modest moments); not preferred label."}
    - {code: HINDU, reason: "Rejected: 'atheistic branch of Hinduism' / Lokayata is grandfather's cultural framing and Sen's accepted spectrum placement, not a theistic profession (S4; S7)."}
    - {code: SECHUM, reason: "Not his public identity in what was read."}
  lio_axes:
    A_locus:
      value: 4
      basis: recorded_interview
      certainty: 0.5
      support: corroborated
      cites: [{source: S6, locator: "religious views exchange"}, {source: S4, locator: "first answer"}, {source: S3, locator: "paragraphs 1–3"}]
      how_known: "(interview) S6: no religious views; 'I think it's an atheist position'. S4: atheistic branch / Lokayata. S3: 'No. I do not believe in god' (reported, in span). Certainty capped at 0.5 under P38 because he also would not object to 'agnostic'."
      rationale: "No separate God (A 4). Alternative BELOW_THRESHOLD under P38 (atheist statement + agnostic hedge)."
      alternatives:
        - {value: BELOW_THRESHOLD, note: "P38: published disbelief plus willingness to accept 'agnostic' → A 4 at most 0.5 with BELOW_THRESHOLD as named alternative.", cites: [{source: S6, locator: "Would that make you agnostic or atheist?"}]}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (economist; P30, as Keynes). Deepen D1: no own-voice remark on the order of nature (P16). Checked and off-point (P19): (1) S6 Forman — belief in objective truth / truth and falsity for social-science questions is epistemology of inquiry, not a statement that nature is lawful; (2) S7 NDTV Newtonian-bullet anecdote — corrects a Subedar on projectile mechanics, not a worldview profession about nature's order. Coder's call: UNKNOWN."}
    C_ledger: {value: UNKNOWN, how_known: "Lead only (P19): prefers Lokayata / Akbar that one should do good not to be looked on with favour by an Almighty (S4); S6 ethics not based on religious beliefs. Not scored."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "(interview) Lead toward 4: 'relying on faith goes against reason'; Akbar's argument 'why reason has to have priority over faith' (S4, 2009, after the span). Reason, not observation, is ranked, so not scored."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P19)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A 4 at 0.5: the A ≥ 3 branch needs 0.7 (P10). B UNKNOWN."}
  statements:
    - text: "I think it's an atheist position, but atheism can be seen as involving a bit of arrogance, so in my modest moments I wouldn't object to being called an agnostic."
      cites: [{source: S6, locator: "Would that make you agnostic or atheist?"}]
      date: "2006-10"
      context: "Bill Forman interview, Metro Santa Cruz (Good Times archive), before UCSC Sidhartha Maitra lecture; answer after 'Have you ever talked about your own religious views?' / 'I don't have any!'"
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "After the span (P20). Own-voice A score + P38 hedge."
    - text: "Although this is a personal matter... But the answer to your question is: No. I do not believe in god."
      cites: [{source: S3, locator: "paragraph 2"}]
      date: "1998-12"
      context: "Meet-the-press programme at the Calcutta Press Club, after the Nobel award; Rediff report dated 28 December 1998."
      axes: [A_locus]
      kind: "reported speech"
      verified_against: "secondary quotation"
      verified_on: 2026-10-19
      note: "Journalist's report of a public answer; in the span."
    - text: "He was very confident that I would come to God (as it were) as I grew up. But I didn’t. But then he told me that clearly I had placed myself on the atheistic branch of Hinduism"
      cites: [{source: S4, locator: "first answer"}]
      date: "2009-07-29"
      context: "Interview with Roy McCloughry, London."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "After the span (P20)."
    - text: "Yes, there was no escape from that. To him, there were these different schools of thought, Advaita, Shaivite and so on, and of course atheism or Lokayata is one of them."
      cites: [{source: S7, locator: "grandfather / Lokayata exchange"}]
      date: "2021-07"
      context: "NDTV interview with Prannoy Roy on Home in the World; Sen affirms the memoir passage in which his grandfather placed him in the atheistic Lokayata part of the Hindu spectrum."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "newspaper interview"
      verified_on: 2026-10-24
      note: "After the span (P20). Affirms lifelong non-belief framed as Lokayata; cultural spectrum, not HINDU code."
  changes_over_life: []
  coder_notes: "B UNKNOWN as for Keynes (economics not counted as science under P30). If v8 counts economics as science, B would still need a P16 nature-order remark; none found this pass. Chart needs A&B ≥0.7 — A held at 0.5 by P38; B UNKNOWN."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Bengali (family from Dhaka)", certainty: 0.7, cites: [{source: S2, locator: "opening"}], how_known: "Nobel autobiography."}
  religious_heritage_by_birth: {value: "Hindu", certainty: 0.5, cites: [{source: S4, locator: "first answer"}], how_known: "(interview)"}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "No religious practice expected of him (S4)."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1970–1999", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Collective Choice (1970) to Development as Freedom (1999) (P29, P30); end at 0.5."}
  age_at_first_lasting_contribution: {value: 37, certainty: 0.7, cites: [{source: S1, locator: "Born; text"}], how_known: "1970 − 1933 = 37 (P30)."}
  first_evidence_of_lio_type_views: {value: "1998", certainty: 0.5, cites: [{source: S3, locator: "paragraph 2"}], how_known: "Reported answer; childhood Lokayata placement is earlier but first dated public evidence is 1998."}
  lio_views_relative_to_major_work: {value: "before major work", certainty: 0.5, cites: [{source: S4, locator: "first answer"}, {source: S7, locator: "grandfather / Lokayata exchange"}], how_known: "(interview) Did not 'come to God' as he grew up; scepticism matured with age."}
  worldview_during_major_work: {value: "Non-believer (atheist position)", certainty: 0.5, cites: [{source: S3, locator: "paragraph 2"}, {source: S6, locator: "religious views exchange"}], how_known: "1998 in-span report; 2006 own-voice atheist position consistent."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "Axiomatic social choice theory (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: "adulthood, before major work", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Cambridge."}
  circle_present: {value: "no", rationale: "No God (S3; S6).", certainty: 0.5, cites: [{source: S3, locator: "paragraph 2"}, {source: S6, locator: "religious views exchange"}], how_known: "Coder's reading."}
  reading: "Formal method without God-in-nature belief."
  notes: ""

institutions:
  - {value: "London School of Economics; University of London", role: professor, years: "1971–1977", kind: university, certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
  - {value: "University of Oxford", role: professor, years: "1977–1988", kind: university, certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
  - {value: "Harvard University", role: "professor of economics and philosophy", years: "1988–1998", kind: university, certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
collaborators: []

review:
  roster_status_reason: {value: "Provisional in v8 (F 3).", certainty: 0.7, cites: [{source: S5, locator: "roster.csv, rank 146"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "1998 disbelief remains a journalist's report; firmed by 2006 and 2009 own-voice interviews."
    - "P38 caps A at 0.5 because of the 2006 agnostic hedge."
  open_questions:
    - "Direct check of Home in the World print/ebook for a written_profession A statement (currently affirmed via NDTV quotation)."
    - "Any P16 nature-order remark that would allow B for a non-scientist."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "The Editors of Encyclopaedia Britannica"
    citation: "\"Amartya Sen.\" Encyclopaedia Britannica (updated 5 September 2026). https://www.britannica.com/money/Amartya-Sen"
    url: "https://www.britannica.com/money/Amartya-Sen"
    accessed: 2026-10-19
    reliability_note: "Unsigned editors' article; body cited (P26)."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, timing, lane_b, institutions]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Amartya Sen"
    citation: "Sen, Amartya. \"Biographical.\" NobelPrize.org (1998). https://www.nobelprize.org/prizes/economic-sciences/1998/sen/biographical/"
    url: "https://www.nobelprize.org/prizes/economic-sciences/1998/sen/biographical/"
    accessed: 2026-10-19
    reliability_note: "His own Nobel autobiography."
    source_quality: "primary / own words"
    used_for: [basics, childhood, heritage]
  - id: S3
    type: secondary
    kind: other
    author: "Rediff"
    citation: "\"Market economy not the panacea, says Sen.\" Rediff On The NeT, 28 December 1998. https://www.rediff.com/business/1998/dec/28sen.htm"
    url: "https://www.rediff.com/business/1998/dec/28sen.htm"
    accessed: 2026-10-19
    reliability_note: "News report quoting his answer at a press club."
    source_quality: "newspaper interview"
    used_for: [worldview, timing, lane_b]
  - id: S4
    type: primary
    kind: other
    author: "Amartya Sen, interviewed by Roy McCloughry"
    citation: "McCloughry, Roy. \"Amartya Sen\" (interview, London, 29 July 2009). High Profiles. https://highprofiles.info/interview/amartya-sen/"
    url: "https://highprofiles.info/interview/amartya-sen/"
    accessed: 2026-10-19
    reliability_note: "Published interview transcript (recorded_interview, P8)."
    source_quality: "newspaper interview"
    used_for: [childhood, worldview, heritage, timing]
  - id: S5
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [review]
  - id: S6
    type: primary
    kind: other
    author: "Amartya Sen, interviewed by Bill Forman"
    citation: "Forman, Bill. \"Sen and Sensibility.\" Metro Santa Cruz, 4–11 October 2006 (archived at Good Times). https://www.goodtimes.sc/archives/metro-santa-cruz/10.04.06/amartya-sen-0640.html"
    url: "https://www.goodtimes.sc/archives/metro-santa-cruz/10.04.06/amartya-sen-0640.html"
    accessed: 2026-10-24
    reliability_note: "Published Q&A with own-voice atheist/agnostic exchange (recorded_interview, P8)."
    source_quality: "newspaper interview"
    used_for: [worldview, timing, lane_b]
  - id: S7
    type: primary
    kind: other
    author: "Amartya Sen, interviewed by Prannoy Roy"
    citation: "Roy, Prannoy. \"Prannoy Roy Speaks To Amartya Sen About His New Book Home in the World: A Memoir - Full Transcript.\" NDTV, July 2021. https://www.ndtv.com/india-news/prannoy-roy-speaks-to-amartya-sen-about-his-new-book-home-in-the-world-a-memoir-full-transcript-2493717"
    url: "https://www.ndtv.com/india-news/prannoy-roy-speaks-to-amartya-sen-about-his-new-book-home-in-the-world-a-memoir-full-transcript-2493717"
    accessed: 2026-10-24
    reliability_note: "Full published transcript; host reads memoir passages; Sen affirms Lokayata placement."
    source_quality: "newspaper interview"
    used_for: [contribution, childhood, worldview, timing]
  - id: S8
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "\"Amartya Sen.\" Wikipedia (English); title \"অমর্ত্য সেন\" (Bengali Wikipedia). Accessed via MediaWiki API / page text, 24 October 2026."
    url: "https://en.wikipedia.org/wiki/Amartya_Sen"
    accessed: 2026-10-24
    reliability_note: "Dual bio for P50 identity only; worldview cites elsewhere."
    source_quality: "reference entry"
    used_for: [identity, childhood]
---

# Amartya Sen

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Amartya Sen (born 1933), Indian economist and philosopher [S1]. Deepen D1: primary ATHE (0.5, alt AGNOS); A 4 (0.5, support corroborated, P38); B UNKNOWN; D BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Not plotted.

## Life and work

Santiniketan, Calcutta, Cambridge, Delhi, LSE, Oxford, Harvard [S1; S2]. Living [S1].

## Contribution and impact

Social choice, famine, capability; Nobel 1998 [S1]. Memoir *Home in the World* (2021) [S7].

## Childhood and education

Hindu family without institutional practice; grandfather Kshiti Mohan Sen framed his non-belief as Lokayata [S4; S7].

## Adult working worldview

Own voice (2006): atheist position; would not object to agnostic in modest moments [S6]. 1998 reported: 'No. I do not believe in god' [S3]. No P16 nature-order remark found; B UNKNOWN (economist, P30) [S6; S7].

## Heritage (context only)

Bengali Hindu [S2; S4]. Native name অমর্ত্য সেন [S8].

## Timing

1970–1999 [S1]. Non-belief from youth; public A evidence from 1998 [S3; S4; S7].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No circle [S3; S6].

## Open questions

- Direct *Home in the World* print check for written_profession A.
- Any P16 nature-order remark for B.

## Research log

- 2026-10-19: Read Britannica, the Nobel autobiography, Rediff (1998) and the 2009 High Profiles interview.
- 2026-10-24: Deepen D1 — Forman / Metro Santa Cruz 2006 (Good Times archive); NDTV 2021 memoir transcript; Wikipedia EN + bn title (P50). Nature-order search empty for B.
