---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 4
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch V)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to economics. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #119 / F4 rank 120). Goals: corroborate AGNOS; hunt locus (A) or P16 (B); keep honest BELOW/UNKNOWN if not found. Re-read LA Times 1986 (S3). Opened Hammond 2021 full PDF (S4, bibliotekanauki / gilsonsociety) — still secondary paraphrase of Two Lucky People ('completely agnostic'; Rose 'fanatically antireligious'); memoir itself unread (IA twoluckypeopleme00frie access-restricted, download 401; Google Books API 429). New primary: Fox News Your World transcript, David Asman interview 15 May 2004 (S6) — 'I would describe myself as an agnostic'; 'Not an atheist. The proposition that there is a God is not capable of being proved either false or true'; faith in people/freedom, not theological. Corroborates S3 AGNOS and rejects ATHE in own voice; after span (P1 cap 0.5). Lofton handwritten-note exchange remains a lead (Daily Hatch / American View; no archival letter). Wikipedia EN (S7, P50) dual bio; Religious views cites Commentary/Ebenstein + Fox. No own-voice locus (P20 → A stays BELOW_THRESHOLD). No P16 nature-order (B stays UNKNOWN; not a scientist P30; Methodology of Positive Economics / Hume causality discussion in Hammond is economics-method, not worldview lawfulness). P47 on S1–S7. Chart-moving NO. No fallacy_catalog. No figures/. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Batch W audit note (gs_2584730_W run 1): 'not reconciled' replaced by the auditor's explanation of the Hammond pages (1183–1217; '1107-1140' is the PDF's file label, where Michaud's article starts). No value changes."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Audit fixes for batch V (gs_982cb8e_V run 1): FR4, family_religion how_known the right way round (the child pushed his parents to be more observant, S3), with the tension against Hammond's 'Orthodox Jewish beliefs' noted; note, Hammond's page range 1183–1217 added to S4. No scored value changes."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch V, order P32: F 4, rank 120). Basics from Britannica (Bruce J. Caldwell; Britannica Editors) and his Nobel autobiography; religion from the 1986 Los Angeles Times profile (his own words, interview) and J. Daniel Hammond's 2021 essay (reporting Two Lucky People). Not a scientist (P30; economics, as for Keynes). primary_system AGNOS at 0.5 (interview); A BELOW_THRESHOLD (P20); B, C, E UNKNOWN; D BELOW_THRESHOLD; mid_basin UNKNOWN. Span 1956–1967 (0.5). Not plotted. Draft, not reviewed."}

identity:
  id: friedman-milton
  display_name: "Milton Friedman"
  roster:
    canonical_name: "Milton Friedman"
    rank: 120
    F: 4
    models: [Claude, DeepSeek, Gemini, GPT]
    band: "core (3–4)"
    status: core
    field: economics
    field_bucket: "social science"
  full_name: {value: "Milton Friedman", certainty: 0.7, cites: [{source: S1, locator: "facts box"}, {source: S2, locator: "¶1"}], how_known: "Britannica and his own Nobel autobiography."}
  native_name: {value: "Milton Friedman", certainty: 0.7, cites: [{source: S1, locator: "facts box"}], how_known: "English; same as the full name."}
  aliases:
    - {name: "Friedman-Milton", kind: "roster alias"}
    - {name: "Milton-Friedman", kind: "roster alias"}

basics:
  birth:
    date: {value: "1912-07-31", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "facts box (Born)"}, {source: S2, locator: "¶1"}], how_known: "Britannica and his own autobiography agree."}
    place: {value: "Brooklyn, New York", modern_name: "Brooklyn, New York, USA", polity_then: "United States", certainty: 1.0, cites: [{source: S1, locator: "facts box (Born)"}, {source: S2, locator: "¶1"}], how_known: "Britannica and S2."}
  death:
    date: {value: "2006-11-16", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "facts box (Died)"}, {source: S7, locator: "Death"}], how_known: "Britannica and Wikipedia EN agree (P50); heart failure, San Francisco."}
    place: {value: "San Francisco, California", modern_name: "San Francisco, USA", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "facts box (Died)"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1956, certainty: 0.5, cites: [{source: S1, locator: "'Challenging Keynesian economics'"}], how_known: "Restatement of the quantity theory in his introduction to Studies in the Quantity of Money (1956), the start of monetarism (P13). The permanent income hypothesis (1957, 'One of his earliest' contributions, S1) is the named alternative start."}
  era_bucket: {value: "1950 on", certainty: 0.5, cites: [{source: S1, locator: "'Challenging Keynesian economics'"}], how_known: "1956 (P2); 1957 gives the same bucket."}
  region_of_birth: {value: "North America", certainty: 1.0, cites: [{source: S1, locator: "facts box"}], how_known: "USA (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "'Academic career and key collaborations'"}], how_known: "University of Chicago; later the Hoover Institution, Stanford."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S2, locator: "¶1"}], how_known: "'first son' (S2)."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "Bibliography"}], how_known: "Coder's reading."}
  occupations: {value: ["economist", "professor of economics, University of Chicago", "Newsweek columnist (1966–1984)", "Senior Research Fellow, Hoover Institution"], certainty: 0.7, cites: [{source: S1, locator: "'Academic career and key collaborations'; 'From monetary theory to public policy'"}], how_known: "Britannica."}

contribution:
  primary_domain: economics
  fields: {value: ["economics", "monetary economics", "consumption theory"], certainty: 0.7, cites: [{source: S1, locator: "opening; 'Academic career and key collaborations'"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Restatement of the quantity theory of money (introduction to Studies in the Quantity of Money): changes in the money supply affect real activity in the short run and prices in the long run; the base of monetarism", year: 1956, kind: theory, lasting: "'regarded as the founder of monetarism' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Challenging Keynesian economics'"}], how_known: "Britannica. A theory of the economy, not of natural systems, so not a scientist (P30; as for Keynes)."}
    - {value: "Permanent income hypothesis (A Theory of the Consumption Function)", year: 1957, kind: theory, lasting: "'provided an explanation for some puzzles' in consumption data (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Academic career and key collaborations', last paragraph"}], how_known: "Britannica."}
    - {value: "A Monetary History of the United States, 1867–1960 (with Anna J. Schwartz)", year: 1963, kind: work, lasting: "'has remained a vital resource' (S1); its Federal Reserve account of the Great Depression 'Especially influential' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Challenging Keynesian economics'; 'Milton Friedman's legacy'"}], how_known: "Britannica."}
    - {value: "Natural rate of unemployment and the critique of a stable Phillips curve (AEA presidential address)", year: 1967, kind: theory, lasting: "'another seminal contribution'; stagflation 'seen by many as confirmation' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Challenging Keynesian economics'"}], how_known: "Britannica. Dated by the delivered address, 1967 (P30), not the 1968 printing."}
  evidence_of_impact:
    - {value: "Nobel Prize for Economics, 1976", kind: "honours in lifetime", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "page heading (Sveriges Riksbank Prize 1976)"}], how_known: "Britannica and the Nobel site."}
    - {value: "'one of the leading proponents of monetarism in the second half of the 20th century'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works:
    - {value: "Free to Choose (with Rose D. Friedman; book of the PBS series)", year: 1980, certainty: 0.7, cites: [{source: S1, locator: "'From monetary theory to public policy'"}], how_known: "Britannica."}
    - {value: "Two Lucky People: Memoirs (with Rose D. Friedman)", year: 1998, certainty: 0.7, cites: [{source: S1, locator: "'From monetary theory to public policy'"}, {source: S2, locator: "1998 paragraph"}], how_known: "Britannica and S2."}
  honours:
    - {value: "Nobel Prize for Economics", year: 1976, certainty: 1.0, cites: [{source: S1, locator: "facts box (Awards And Honors)"}, {source: S2, locator: "page heading"}], how_known: "Britannica and the Nobel site; formally the Sveriges Riksbank Prize in Economic Sciences in Memory of Alfred Nobel (S2)."}
  definition_fit: {value: "clearly meets", rationale: "Founder of monetarism; permanent income and natural-rate theories still used (S1).", certainty: 0.7, cites: [{source: S1, locator: "'Milton Friedman's legacy'"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "Orthodox Jewish", certainty: 0.5, cites: [{source: S4, locator: "opening section"}, {source: S3, locator: "¶ on his upbringing"}], how_known: "Hammond, reporting Two Lucky People: neither Milton nor Rose 'adhered to their parents’ Orthodox Jewish beliefs' (S4). The LA Times has it the other way round on practice: 'His parents weren't the most religious of Jews, and Friedman recalls at a very early age pushing them to be more observant' (S3); the child pushed the parents (corrected in the batch V audit fixes, FR4). The two sources are in tension (Orthodox beliefs vs not the most religious), so 0.5."}
  family_religious_practice: {value: "Hebrew school until about 13; Bar-Mitzvahed; by his own account 'fanatically religious' as a child", certainty: 0.5, cites: [{source: S4, locator: "opening section"}], how_known: "Hammond's summary of Two Lucky People (memoir not read)."}
  parents_and_household:
    - {value: "Father: Jeno Saul Friedman, born in Carpatho-Ruthenia; a succession of mostly unsuccessful 'jobbing' ventures; died in Milton's senior year of high school", certainty: 0.7, cites: [{source: S2, locator: "¶1–2"}], how_known: "His own autobiography."}
    - {value: "Mother: Sarah Ethel (Landau) Friedman, born in Carpatho-Ruthenia; ran a small dry-goods store in Rahway", certainty: 0.7, cites: [{source: S2, locator: "¶1"}], how_known: "His own autobiography."}
  household_circumstances: {value: "Immigrant family of small, uncertain income in Rahway, New Jersey; 'warm and supportive'", certainty: 0.7, cites: [{source: S2, locator: "¶1"}], how_known: "His own autobiography."}
  schooling:
    - {value: "Public elementary and secondary schools, Rahway; graduated from Rahway High School 1928", stage: "grammar or secondary school", run_by: "state or municipal", years: "to 1928", certainty: 0.7, cites: [{source: S2, locator: "¶2"}], how_known: "His own autobiography."}
    - {value: "Hebrew school, to about age 13", stage: other, run_by: "religious body", certainty: 0.5, cites: [{source: S4, locator: "opening section"}], how_known: "Hammond, reporting Two Lucky People."}
    - {value: "Rutgers University (scholarship): mathematics and economics; B.A. 1932", stage: university, run_by: other, years: "1928–1932", certainty: 0.7, cites: [{source: S1, locator: "'Early life and education'"}, {source: S2, locator: "¶3"}], how_known: "Britannica and S2; S2 calls Rutgers then 'predominantly private'."}
    - {value: "University of Chicago (A.M. 1933); Columbia University (Ph.D. 1946)", stage: university, run_by: private, years: "1932–1946", certainty: 0.7, cites: [{source: S1, locator: "'Early life and education'"}], how_known: "Britannica."}
  early_mathematics: {value: "advanced mathematics", certainty: 0.5, cites: [{source: S1, locator: "'Early life and education'"}], how_known: "Studied mathematics at Rutgers from age 16; the level before 18 is the coder's reading."}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading:
    - {value: "Alfred Marshall's Principles of Economics, introduced by Arthur Burns at Rutgers", certainty: 0.7, cites: [{source: S1, locator: "'Early life and education'"}], how_known: "Britannica; at university, not childhood."}
  childhood_mentors: []
  languages_in_childhood: {value: ["English"], certainty: 0.5, cites: [{source: S2, locator: "¶1"}], how_known: "Coder's reading."}
  notable_events:
    - {value: "Gave up the Jewish religion around age 13", certainty: 0.5, cites: [{source: S3, locator: "¶ on his upbringing"}, {source: S4, locator: "opening section"}], how_known: "LA Times ('by the time he turned 13, he abandoned Judaism altogether') and Hammond."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1956–1967", certainty: 0.5, cites: [{source: S1, locator: "'Challenging Keynesian economics'"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Married by a rabbi (25 June 1938) as 'pure form, not substance'", certainty: 0.5, cites: [{source: S4, locator: "opening section"}], how_known: "Hammond, quoting Two Lucky People. A ritual for the families' sake; no code (JUDA is heritage here)."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing in his own words read on science and religion."}
  primary_system:
    value: AGNOS
    basis: recorded_interview
    certainty: 0.5
    cites: [{source: S3, locator: "¶ on his upbringing"}, {source: S6, locator: "Faith section"}, {source: S4, locator: "pp. 1183–1184 / opening"}]
    how_known: "(interview) Deepen D1: two independent after-span interviews name AGNOS. (1) LA Times 1986 (S3): 'I've been an agnostic ever since.' (2) Fox News Your World, 15 May 2004 (S6): 'I would describe myself as an agnostic'; 'Not an atheist. The proposition that there is a God is not capable of being proved either false or true.' Both after the working years (P1 cap 0.5); 'ever since' from age 13 covers the span. Hammond full PDF (S4) paraphrases Two Lucky People as 'completely agnostic' — memoir unread (IA 401). Certainty stays 0.5 (interview / after span); corroboration strengthens support, not the P1 cap."
    rationale: "(interview) AGNOS: self-named in S3 and S6; S6 also rejects ATHE in own voice. Rose's 'fanatically antireligious' (via S4) remains reported speech. Lofton handwritten-note exchange (Daily Hatch quoting American View) matches S6 wording closely but is not used as a scored cite (host unverified; archival letter not found). Two Lucky People still unread."
  secondary_system: {value: UNKNOWN, how_known: "One system (P29)."}
  candidate_codes_considered:
    - {code: AGNOS, reason: "Self-description in S3 (1986) and S6 (2004); Hammond paraphrase of Two Lucky People (S4). Coded at 0.5 (interview, after span, P1)."}
    - {code: ATHE, reason: "Rejected in own voice (S6: 'Not an atheist'); Rose's 'fanatically antireligious' is reported speech (S4), not his code."}
    - {code: JUDA, reason: "Rejected: childhood religion and heritage only (S3, S4); wedding 'pure form, not substance'."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "(interview) Deepen D1: S3 and S6 name AGNOS and (S6) the epistemic status of 'There is a God' (not proveable true or false). That is the AGNOS definition, not a locus claim about where God is / acts (P20). No immanence, transcendence, or pantheism statement read → A stays BELOW_THRESHOLD."}
    B_cause: {value: UNKNOWN, how_known: "Deepen D1: not a scientist (P30; economics like Keynes). For a non-scientist B needs an explicit own-voice remark on the order of nature (P16). Checked and off-point (P19): (1) S6 — faith in people/freedom, values; nothing on natural law vs miracle; (2) Hammond (S4) on Methodology of Positive Economics and Hume on causality — economics-method / philosophy-of-science discussion, not a worldview profession that nature is lawful; (3) Lofton lead on evolutionary origin of values — morals/customs, not P16 physical order. Coder's call: UNKNOWN, not BELOW (nothing scored that bears on B)."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing on reward and punishment of persons read (P19)."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "(interview) Lead only: left religion when he 'decided there wasn't any sense to it' (S3); Hammond: faith 'unreasonable' (S4 paraphrase of memoir). S6 contrasts scientific statements (contradictable by experience) with 'There is a God' as a statement of faith — methodological demarcation, not a scored view that revelation is false against observation. Stays BELOW."}
    E_scope: {value: UNKNOWN, how_known: "Nothing on favour for a group in the world's order read (P7, P19)."}
  mid_basin: {value: UNKNOWN, how_known: "B_cause is UNKNOWN, which takes precedence (P19)."}
  statements:
    - text: "When I thought the religion I was brought up in was correct, I was very rigid and strict in observing it. On the day I decided there wasn't any sense to it, I quit. I've been an agnostic ever since."
      cites: [{source: S3, locator: "¶ on his upbringing"}]
      date: "1986-12-14"
      context: "Interview profile by Jonathan Peterson, Los Angeles Times Magazine; the journalist's frame says he abandoned Judaism by 13. The quote is split by the journalist's 'he says' after 'observing it'; the cut is not marked inside quotation marks because no words are dropped."
      axes: [D_authority]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "Read live in the Los Angeles Times archive text (the printed article's web copy). A journalist's direct quotation; no audio or full transcript. Whether a newspaper's direct quote counts as 'recorded or transcribed' under P8 is flagged for the auditor."
    - text: "I would describe myself as an agnostic. … Not an atheist. The proposition that there is a God is not capable of being proved either false or true. And that's what I mean about being an agnostic. … There are statements which are capable of being contradicted by experience. Those are scientific statements. There are statements which can not be contradicted by any experience such as: 'There is a God.' And those are statements of faith. … But my faith is not theological. … my faith is faith in people and faith in the principle of freedom."
      cites: [{source: S6, locator: "Faith section"}]
      date: "2004-05-15"
      context: "Fox News Your World interview with David Asman; full transcript published 16 Nov 2006 (day of death) and archived. Ellipses mark interviewer turns / unrelated sentences dropped; wording inside quotes is continuous within each answer as printed."
      axes: [D_authority]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Broadcast interview transcript on Fox News (and Wayback). After the span (P1). Explicitly rejects ATHE; no locus for A (P20)."
  changes_over_life:
    - {value: "'fanatically religious' child (Hebrew school, Bar Mitzvah); gave up the religion around 13 and stayed agnostic", certainty: 0.5, cites: [{source: S3, locator: "¶ on his upbringing"}, {source: S4, locator: "opening section"}], how_known: "LA Times and Hammond; before the span."}
  coder_notes: "Deepen D1 2026-10-24: AGNOS @0.5 corroborated by Fox 2004 (S6) + LA Times 1986 (S3); A BELOW (P20, no locus); B UNKNOWN (P16/P30). Two Lucky People still unread (IA 401). Lofton note lead only. Chart-moving NO. Not plotted. Span unchanged: 1956–1967 (alt start 1957)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Jewish, of immigrant parents from Carpatho-Ruthenia", certainty: 0.7, cites: [{source: S2, locator: "¶1"}, {source: S4, locator: "opening section"}], how_known: "S2 (origin) and Hammond (Jewish family)."}
  religious_heritage_by_birth: {value: "Orthodox Judaism", certainty: 0.5, cites: [{source: S4, locator: "opening section"}], how_known: "Hammond."}
  baptism_or_initiation: {value: "Bar Mitzvah", certainty: 0.5, cites: [{source: S4, locator: "opening section"}], how_known: "Hammond, reporting Two Lucky People."}
  childhood_catechism: {value: "Hebrew school to about 13", certainty: 0.5, cites: [{source: S4, locator: "opening section"}], how_known: "Hammond."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1956–1967", certainty: 0.5, cites: [{source: S1, locator: "'Academic career and key collaborations'; 'Challenging Keynesian economics'"}], how_known: "From the 1956 restatement to the 1967 AEA address (P12, P30). Coder's call; alternative start 1957 (coder_notes)."}
  age_at_first_lasting_contribution: {value: 44, certainty: 0.5, cites: [{source: S1, locator: "facts box; 'Challenging Keynesian economics'"}], how_known: "1956 − 1912 = 44 (P30); 45 under the 1957 alternative."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "AGNOS self-descriptions after the span; no axis at 3 or 4 (A/D BELOW; B UNKNOWN)."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S3, locator: "¶ on his upbringing"}, {source: S6, locator: "Faith section"}], how_known: "AGNOS named; A BELOW and B UNKNOWN — no plotted LIO-type views."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "'Early life and education'"}], how_known: "Not assessed."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "'Early life and education'"}], how_known: "Not assessed."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "'Early life and education'"}], how_known: "Coder's reading."}
  reading: "Economics as 'an engine for the discovery of concrete truth' (Marshall, quoted approvingly; S1)."
  notes: ""

institutions:
  - {value: "National Resources Committee, Washington", role: "consumer budget study", years: "1935–1937", kind: "government or state body", certainty: 0.7, cites: [{source: S1, locator: "'Early life and education'"}], how_known: "Britannica."}
  - {value: "National Bureau of Economic Research", role: "research staff (with Simon Kuznets)", years: "from 1937", kind: "research institute", certainty: 0.7, cites: [{source: S1, locator: "'Early life and education'"}, {source: S2, locator: "NBER paragraph"}], how_known: "Britannica and S2."}
  - {value: "University of Chicago", role: "professor of economics", years: "1946–1977", kind: university, certainty: 0.7, cites: [{source: S1, locator: "'Academic career and key collaborations'"}, {source: S2, locator: "1977 paragraph"}], how_known: "Britannica (from 1946; retired 1976 per Britannica, 1977 per S2)."}
  - {value: "Hoover Institution, Stanford University", role: "Senior Research Fellow", years: "from 1977", kind: "research institute", certainty: 0.7, cites: [{source: S1, locator: "'From monetary theory to public policy'"}, {source: S2, locator: "1977 paragraph"}], how_known: "Britannica and S2."}
collaborators:
  - {value: "Arthur F. Burns", relation: "mentor or employer", note: "'his mentor and most important influence' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Early life and education'"}, {source: S2, locator: "Rutgers paragraph"}], how_known: "Britannica and S2."}
  - {value: "Anna J. Schwartz", relation: collaborator, note: "A Monetary History (1963) and two later books", certainty: 0.7, cites: [{source: S1, locator: "'Challenging Keynesian economics'"}], how_known: "Britannica."}
  - {value: "Simon Kuznets", relation: collaborator, note: "Incomes from Independent Professional Practice", certainty: 0.7, cites: [{source: S1, locator: "'Early life and education'"}, {source: S2, locator: "NBER paragraph"}], how_known: "Britannica and S2."}
  - {value: "Rose Director Friedman", relation: family, note: "wife and co-author (Free to Choose; Two Lucky People)", certainty: 0.7, cites: [{source: S1, locator: "'Early life and education'; 'From monetary theory to public policy'"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S5, locator: "roster.csv, rank 120"}], how_known: "Study roster."}
  controversies:
    - {value: "Criticized for appearing to support the Pinochet dictatorship after his 1975 Chile visit and letter", certainty: 0.7, cites: [{source: S1, locator: "'From monetary theory to public policy'"}], how_known: "Britannica."}
  data_quality_flags:
    - "AGNOS @0.5 rests on after-span interviews (S3 1986; S6 2004); P1 cap holds. Two Lucky People (1998) still unread in primary (IA 401)."
    - "Whether a newspaper's direct quotation (S3) counts as recorded interview (P8) remains flagged; S6 is a broadcast transcript."
    - "Span is a coder's call with a named alternative start (1957)."
  open_questions:
    - "Read Two Lucky People (1998), Early Years—Milton / wedding chapters, in a primary copy (IA borrow or print)."
    - "Lofton–Friedman handwritten notes: archival scan (Hoover / American View original), not Daily Hatch alone."
    - "Any in-span (1956–1967) written profession on God/locus or P16 nature-order (low prior)."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Bruce J. Caldwell; The Editors of Encyclopaedia Britannica"
    citation: "Caldwell, Bruce J., and the Editors of Encyclopaedia Britannica. \"Milton Friedman.\" Encyclopaedia Britannica (updated 29 September 2026). https://www.britannica.com/money/Milton-Friedman. Read live 2026-10-19."
    url: "https://www.britannica.com/money/Milton-Friedman"
    accessed: 2026-10-19
    reliability_note: "Signed article (Caldwell, Duke); facts box and section bodies cited."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, timing, institutions, collaborators, review]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Milton Friedman"
    citation: "Friedman, Milton. \"Milton Friedman – Biographical.\" NobelPrize.org (from Les Prix Nobel 1976, with a later addendum). https://www.nobelprize.org/prizes/economic-sciences/1976/friedman/biographical/"
    url: "https://www.nobelprize.org/prizes/economic-sciences/1976/friedman/biographical/"
    accessed: 2026-10-19
    reliability_note: "His own autobiographical note for the Nobel Foundation; nothing on religion. Locators by paragraph."
    source_quality: "primary / own words"
    used_for: [identity, basics, childhood, heritage, institutions, collaborators]
  - id: S3
    type: secondary
    kind: other
    author: "Jonathan Peterson"
    citation: "Peterson, Jonathan. \"The Captain of Capitalism.\" Los Angeles Times (Magazine), 14 December 1986. https://www.latimes.com/archives/la-xpm-1986-12-14-tm-2801-story.html"
    url: "https://www.latimes.com/archives/la-xpm-1986-12-14-tm-2801-story.html"
    accessed: 2026-10-19
    reliability_note: "Newspaper interview profile; his direct quotes are used as his words (P8, flagged), the journalist's narration as context only."
    source_quality: "newspaper interview"
    used_for: [worldview, childhood, heritage]
  - id: S4
    type: secondary
    kind: "journal article"
    author: "J. Daniel Hammond"
    citation: "Hammond, J. Daniel. \"God and Man at the University of Chicago: Religious Commitments of Three Economists.\" Studia Gilsoniana 10, no. 5 (2021): 1183–1217. DOI 10.26385/SG.100446. PDF: http://gilsonsociety.com/files/1107-1140-Hammond-46.pdf"
    url: "http://gilsonsociety.com/files/1107-1140-Hammond-46.pdf"
    accessed: 2026-10-19
    reliability_note: "Scholarly article by an economic historian (Wake Forest) summarising and quoting Two Lucky People. Deepen D1: full PDF read 2026-10-24 via bibliotekanauki.pl and gilsonsociety.com (Studia Gilsoniana 10, no. 5: 1183–1217). Still secondary paraphrase for Friedman's faith (memoir unread). File-name '1107-1140' is the site's label, not the page range (batch W note)."
    source_quality: "other"
    used_for: [worldview, childhood, heritage]
  - id: S5
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "Milton Friedman; interviewed by David Asman"
    citation: "Asman, David. \"'Your World' Interview With Economist Milton Friedman.\" Fox News (transcript of interview 15 May 2004; published 16 November 2006). https://www.foxnews.com/story/your-world-interview-with-economist-milton-friedman. Wayback: https://web.archive.org/web/20110206063810/http://www.foxnews.com/story/0,2933,230045,00.html. Read live 2026-10-24."
    url: "https://www.foxnews.com/story/your-world-interview-with-economist-milton-friedman"
    accessed: 2026-10-24
    reliability_note: "Broadcast interview transcript (Fox News Your World). Own spoken words as printed. After the span (2004; P1). Kind = published work by the subject; source_quality newspaper interview (P47 nearest for broadcast Q&A)."
    source_quality: "newspaper interview"
    used_for: [worldview, review]
  - id: S7
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia. \"Milton Friedman.\" English Wikipedia. https://en.wikipedia.org/wiki/Milton_Friedman. Religious views section and death facts read 2026-10-24."
    url: "https://en.wikipedia.org/wiki/Milton_Friedman"
    accessed: 2026-10-24
    reliability_note: "Crowdsourced; dual bio (P50) against Britannica. Religious views cites Commentary/Ebenstein and the Fox interview (S6); Christmas-tree anecdote from Two Lucky People p.129 (practice, not scored)."
    source_quality: "reference entry"
    used_for: [basics, heritage, review]

---

# Milton Friedman

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Milton Friedman (1912–2006), American economist, founder of monetarism [S1; S7]. Deepen D1: primary_system AGNOS at 0.5 (interview; corroborated S3+S6); A BELOW_THRESHOLD (P20); B UNKNOWN (P16/P30); mid_basin UNKNOWN. Chart-moving NO. Not plotted.

## Life and work

Rahway, Rutgers, Chicago, Columbia, the NBER; University of Chicago 1946–1977; Hoover Institution [S1, S2].

## Contribution and impact

The 1956 restatement of the quantity theory, the permanent income hypothesis (1957), A Monetary History (1963, with Schwartz), the natural rate (1967); Nobel Prize 1976 [S1].

## Childhood and education

Orthodox Jewish immigrant family; Hebrew school and Bar Mitzvah; gave up religion around 13 [S3, S4].

## Adult working worldview

"I've been an agnostic ever since" (1986) [S3]; "I would describe myself as an agnostic" / not an atheist (2004) [S6]. AGNOS at 0.5 (interview, after span). Two Lucky People unread [S4].

## Heritage (context only)

Jewish [S2, S4].

## Timing

1956–1967, from age 44 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Not assessed.

## Open questions

- Two Lucky People (1998) primary pages on loss of faith; Lofton archival notes; any in-span God/locus or P16 claim.

## Research log

- 2026-10-19: Read Britannica, the Nobel autobiography, the LA Times profile and Hammond's article (search extract).
- 2026-10-24: Deepen D1. Hammond full PDF [S4]; Fox Your World 2004 transcript [S6]; Wikipedia EN [S7]. IA Two Lucky People 401. AGNOS @0.5 kept; A BELOW; B UNKNOWN. Chart-moving NO.
