---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch V)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
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
    date: {value: "2006-11-16", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "facts box (Died)"}], how_known: "Britannica."}
    place: {value: "San Francisco, California", modern_name: "San Francisco, USA", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "facts box (Died)"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1956, certainty: 0.5, cites: [{source: S1, locator: "'Challenging Keynesian economics'"}], how_known: "Restatement of the quantity theory in his introduction to Studies in the Quantity of Money (1956), the start of monetarism (P13). The permanent income hypothesis (1957, 'One of his earliest' contributions, S1) is the named alternative start."}
  era_bucket: {value: "1950 on", certainty: 0.5, cites: [{source: S1, locator: "'Challenging Keynesian economics'"}], how_known: "1956 (P2); 1957 gives the same bucket."}
  region_of_birth: {value: "North America", certainty: 1.0, cites: [{source: S1, locator: "facts box"}], how_known: "USA (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "'Academic career and key collaborations'"}], how_known: "University of Chicago; later the Hoover Institution, Stanford."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S2, locator: "¶1"}], how_known: "'first son' (S2)."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "Bibliography"}], how_known: "Coder's reading."}
  occupations: {value: ["economist", "professor of economics, University of Chicago", "Newsweek columnist (1966–1984)", "Senior Research Fellow, Hoover Institution"], certainty: 0.7, cites: [{source: S1, locator: "'Academic career and key collaborations'; 'From monetary theory to public policy'"}], how_known: "Britannica."}

contribution:
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
    cites: [{source: S3, locator: "¶ on his upbringing"}, {source: S4, locator: "opening section"}]
    how_known: "(interview) His own first-person words in a newspaper interview profile (P8): 'On the day I decided there wasn't any sense to it, I quit. I've been an agnostic ever since.' (S3, 1986). Spoken 19 years after the working years (P1 cap 0.5); 'ever since' (from age 13) covers the span. Hammond, reporting Two Lucky People, has him 'completely agnostic' after childhood (S4)."
    rationale: "(interview) AGNOS: he names himself an agnostic. ATHE is not named as an alternative from what was read: no stated denial. Rose's description 'fanatically antireligious' (via S4) is reported, not his words. A handwritten note quoted on a blog ('I am an agnostic. I do not \"believe in\" God, but I am not an atheist') was not used: unreliable host, not verified."
  secondary_system: {value: UNKNOWN, how_known: "One system (P29)."}
  candidate_codes_considered:
    - {code: AGNOS, reason: "His self-description (S3), backed by Hammond (S4); coded at 0.5 (interview, after the span)."}
    - {code: ATHE, reason: "Rejected: no stated denial read; Rose's 'fanatically antireligious' is reported speech (S4)."}
    - {code: JUDA, reason: "Rejected: childhood religion and heritage only (S3, S4)."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "(interview) An agnostic with no stated locus view (P20)."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30); nothing of his on natural law, miracle or petition read (P16, P19)."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing on reward and punishment of persons read (P19)."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "(interview) Lead only: he left religion when he 'decided there wasn't any sense to it' (S3), and Hammond says he came to think his faith 'unreasonable' (S4). A judgement on one religion, not a stated view on revelation against observation."}
    E_scope: {value: UNKNOWN, how_known: "Nothing on the world's order read (P7, P19)."}
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
  changes_over_life:
    - {value: "'fanatically religious' child (Hebrew school, Bar Mitzvah); gave up the religion around 13 and stayed agnostic", certainty: 0.5, cites: [{source: S3, locator: "¶ on his upbringing"}, {source: S4, locator: "opening section"}], how_known: "LA Times and Hammond; before the span."}
  coder_notes: "Coder's call on the span: start 1956 (quantity-theory restatement; S1 dates monetarism's case to it) with 1957 (permanent income) as the alternative; end 1967 (AEA address on the natural rate). Monetary History (1963) inside. Not a scientist: economics is not a theory of natural systems (P30, Keynes precedent). The interview basis for a newspaper quote is flagged (statement note). Leads: Two Lucky People (1998) chapter on the wedding and his loss of faith, read only through Hammond; the handwritten 'I am an agnostic' note (blog copy only). Not plotted."

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
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No statement scored at 3 or 4 on any axis."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S3, locator: "¶ on his upbringing"}], how_known: "Agnostic self-description only; no axis scored."}
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
    - "The worldview code rests on one newspaper interview quote (after the span) and one scholar's summary of the memoir; the memoir itself was not read."
    - "Whether a newspaper's direct quotation counts as a recorded interview (P8) is flagged for the auditor."
    - "Span is a coder's call with a named alternative start."
  open_questions:
    - "Two Lucky People (1998) on his loss of faith and the 1938 wedding."
    - "The handwritten 'I am an agnostic' note: find an archival copy."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Bruce J. Caldwell; The Editors of Encyclopaedia Britannica"
    citation: "Caldwell, Bruce J., and the Editors of Encyclopaedia Britannica. \"Milton Friedman.\" Encyclopaedia Britannica (updated 29 September 2026). https://www.britannica.com/money/Milton-Friedman. Read live 2026-10-19."
    url: "https://www.britannica.com/money/Milton-Friedman"
    accessed: 2026-10-19
    reliability_note: "Signed article (Caldwell, Duke); facts box and section bodies cited."
    used_for: [identity, basics, contribution, childhood, timing, institutions, collaborators, review]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Milton Friedman"
    citation: "Friedman, Milton. \"Milton Friedman – Biographical.\" NobelPrize.org (from Les Prix Nobel 1976, with a later addendum). https://www.nobelprize.org/prizes/economic-sciences/1976/friedman/biographical/"
    url: "https://www.nobelprize.org/prizes/economic-sciences/1976/friedman/biographical/"
    accessed: 2026-10-19
    reliability_note: "His own autobiographical note for the Nobel Foundation; nothing on religion. Locators by paragraph."
    used_for: [identity, basics, childhood, heritage, institutions, collaborators]
  - id: S3
    type: secondary
    kind: other
    author: "Jonathan Peterson"
    citation: "Peterson, Jonathan. \"The Captain of Capitalism.\" Los Angeles Times (Magazine), 14 December 1986. https://www.latimes.com/archives/la-xpm-1986-12-14-tm-2801-story.html"
    url: "https://www.latimes.com/archives/la-xpm-1986-12-14-tm-2801-story.html"
    accessed: 2026-10-19
    reliability_note: "Newspaper interview profile; his direct quotes are used as his words (P8, flagged), the journalist's narration as context only."
    used_for: [worldview, childhood, heritage]
  - id: S4
    type: secondary
    kind: "journal article"
    author: "J. Daniel Hammond"
    citation: "Hammond, J. Daniel. \"God and Man at the University of Chicago: Religious Commitments of Three Economists.\" Studia Gilsoniana 10, no. 5 (2021): 1183–1217. DOI 10.26385/SG.100446. PDF: http://gilsonsociety.com/files/1107-1140-Hammond-46.pdf"
    url: "http://gilsonsociety.com/files/1107-1140-Hammond-46.pdf"
    accessed: 2026-10-19
    reliability_note: "Scholarly article by an economic historian (Wake Forest) summarising and quoting Two Lucky People; read in the search index extract of the PDF's opening section. Page range 1183–1217 from PhilPapers (batch V audit note); the PDF's file name reads '1107-1140', not reconciled."
    used_for: [worldview, childhood, heritage]
  - id: S5
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Milton Friedman

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Milton Friedman (1912–2006), American economist, founder of monetarism [S1]. Draft: primary_system AGNOS at 0.5 (interview); A BELOW_THRESHOLD; B UNKNOWN; mid_basin UNKNOWN. Not plotted.

## Life and work

Rahway, Rutgers, Chicago, Columbia, the NBER; University of Chicago 1946–1977; Hoover Institution [S1, S2].

## Contribution and impact

The 1956 restatement of the quantity theory, the permanent income hypothesis (1957), A Monetary History (1963, with Schwartz), the natural rate (1967); Nobel Prize 1976 [S1].

## Childhood and education

Orthodox Jewish immigrant family; Hebrew school and Bar Mitzvah; gave up religion around 13 [S3, S4].

## Adult working worldview

"I've been an agnostic ever since" (1986, interview) [S3]. AGNOS at 0.5 (interview).

## Heritage (context only)

Jewish [S2, S4].

## Timing

1956–1967, from age 44 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Not assessed.

## Open questions

- Two Lucky People on his loss of faith.

## Research log

- 2026-10-19: Read Britannica, the Nobel autobiography, the LA Times profile and Hammond's article (search extract).
