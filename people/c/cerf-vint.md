---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA10; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to 20c_late. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-20, by: "Grok Bot", summary: "AA10 audit fix: span 1973 (INWG Note 39, Sussex, September 1973; S3, S4), age 30; 1974 as the alternative."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA10, order P32: F 3, rank 222). Source: Britannica scholars edition, signed by Michael Aaron Dennis (read in full). Lasting: the ARPA Internet design and TCP/IP with Robert Kahn; he 'is considered one of the founders, along with Robert Kahn, of the Internet' (S1). Dated by the earliest public statement (P30): 'HOST and PROCESS Level Protocols for Internetwork Communication', INWG Note 39 (NIC 18764), September 1973, presented at the INWG meeting at the University of Sussex (S3, S4); alternative 1974 (IEEE Transactions on Communications, May 1974). Span 1973, age 30. Not a scientist (McCarthy precedent, RQ-AA3-1; P33: protocol design is engineering). Worldview UNKNOWN. Living. Not plotted. Draft, not reviewed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen D1 (queue #209/228, F 3, rank 222): any firm A and B; do not force plot. Read Senate written testimony 17 Jul 2014 / SciAm republication (S5); FCC FIRSTS podcast transcript Apr 2024 (S6); Commonweal Spadaro interview (S7); Wikipedia EN (S8); Gizmodo 2013 interview (context). B UNKNOWN→3 @0.5 written_profession, support single, alt 4 (P16 Hilbert addendum for non-scientist nature-order remark; engineer not P35). A stays UNKNOWN: Moscow 2010 'Do you believe in God?' answered 'I'm geek orthodox' (= technology is our friend; S6) — witty deflection, not ATHE/AGNOS/locus. primary UNKNOWN (Geek Orthodoxy not a code). Mid UNKNOWN. Not plotted. P47 on all. No fallacy_catalog; figures not refreshed. Draft, not reviewed."}

identity:
  id: cerf-vint
  display_name: "Vint Cerf"
  roster:
    canonical_name: "Vint Cerf"
    rank: 222
    F: 3
    models: [Claude, DeepSeek, GPT]
    band: "core (3–4)"
    status: "core"
    field: "computer science"
    field_bucket: "computer science / AI"
  full_name: {value: "Vinton Gray Cerf", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S8, locator: "lead"}], how_known: "Britannica and Wikipedia agree."}
  native_name: {value: "Vinton Cerf", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  aliases:
    - {name: "Vinton Cerf", kind: "roster alias"}
    - {name: "Vint Cerf", kind: "other"}

basics:
  birth:
    date: {value: "1943-06-23", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S8, locator: "lead"}], how_known: "Britannica and Wikipedia agree."}
    place: {value: "New Haven, Connecticut", modern_name: "New Haven, Connecticut, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S8, locator: "lead"}], how_known: "Britannica and Wikipedia agree."}
  death:
    date: {value: UNKNOWN, how_known: "Living."}
    place: {value: UNKNOWN, how_known: "Living."}
  first_lasting_contribution_year: {value: 1973, certainty: 0.7, cites: [{source: S1, locator: "para. 4"}, {source: S3, locator: "title page"}, {source: S4, locator: "references, note 8"}], how_known: "INWG Note 39, September 1973 (S3; cited as such in S4), presented at the INWG meeting at Sussex: earliest public statement (P30). Alternative 1974, the joint paper (S1)."}
  era_bucket: {value: "1950 on", certainty: 1.0, cites: [{source: S1, locator: "para. 4"}], how_known: "1973 (P2); the 1974 alternative is in the same bucket."}
  region_of_birth: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "United States (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "para. 3–4"}], how_known: "Stanford; DARPA; Google."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "English."}
  occupations: {value: ["computer scientist", "engineer", "executive"], certainty: 0.7, cites: [{source: S1, locator: "opening; para. 5"}], how_known: "Britannica."}

contribution:
  era_bucket: 20c_late
  fields: {value: ["computer science", "networking"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Internet architecture and the TCP/IP protocols (with Robert Kahn)", year: 1973, kind: "invention", lasting: "'considered one of the founders, along with Robert Kahn, of the Internet' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; para. 4"}, {source: S3, locator: "title page"}], how_known: "INWG Note 39, September 1973 (S3); joint paper 1974 (S1, alternative); TCP/IP produced later at DARPA IPTO (from 1976) (S1)."}
  evidence_of_impact:
    - {value: "A.M. Turing Award (2004, with Kahn) 'for pioneering work on internetworking ... TCP/IP'", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works:
    - {value: "Network Control Program for the ARPANET (with Crocker, Kleinrock lab, UCLA)", year: UNKNOWN, kind: "other", certainty: 0.7, cites: [{source: S1, locator: "para. 3"}], how_known: "Britannica; undated."}
    - {value: "MCI Mail, first commercial e-mail service connected to the Internet", year: UNKNOWN, kind: "other", certainty: 0.7, cites: [{source: S1, locator: "para. 5"}], how_known: "Britannica."}
  honours:
    - {value: "A.M. Turing Award", year: 2004, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    - {value: "Presidential Medal of Freedom", year: 2005, certainty: 0.7, cites: [{source: S1, locator: "para. 6"}], how_known: "Britannica."}
    - {value: "Queen Elizabeth Prize for Engineering", year: 2013, certainty: 0.7, cites: [{source: S1, locator: "para. 6"}], how_known: "Britannica."}
  definition_fit: {value: "clearly meets", rationale: "Co-founder of the Internet (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated in sources opened this pass (S1, S8)."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Son of Muriel (née Gray) and Vinton Thruston Cerf; mother Canadian-born (British, Irish, French Canadian descent); paternal line from Alsace–Lorraine to Kentucky", role: "family", certainty: 0.7, cites: [{source: S8, locator: "Life and career (parents; ancestry)"}], how_known: "Wikipedia (Stanford oral history and related cites)."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling:
    - {value: "Van Nuys High School; Stanford (B.S. mathematics 1965); UCLA (M.S. 1970, Ph.D. computer science 1972)", certainty: 0.7, cites: [{source: S1, locator: "para. 2"}, {source: S8, locator: "Life and career"}], how_known: "Britannica and Wikipedia."}
  early_mathematics: {value: "basic algebra", certainty: 0.7, cites: [{source: S6, locator: "FCC FIRSTS interview (fifth-grade math teacher)"}], how_known: "Own words: fifth-grade teacher handed him a seventh-grade algebra book after he complained math was boring; he worked all the problems (S6)."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure:
    - {value: "High-school chemistry enthusiasm; programming access at UCLA (Bendix G15, IBM 7094) with Steve Crocker; Rocketdyne Apollo F-1 statistical software", certainty: 0.7, cites: [{source: S6, locator: "FCC FIRSTS"}, {source: S8, locator: "Life and career (Rocketdyne)"}], how_known: "Own words; Wikipedia."}
  key_early_reading: []
  childhood_mentors:
    - {value: "Fifth-grade math teacher (Mr. Tomaszewski)", certainty: 0.7, cites: [{source: S6, locator: "closing mentor answer"}], how_known: "Own words."}
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1973", certainty: 0.7, cites: [{source: S1, locator: "para. 4"}, {source: S3, locator: "title page"}], how_known: "Equals timing.major_work_period; alternative 1974."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No scored science–religion relation statement. 'Geek orthodox' is a joke about his Google title and technology advocacy (S6), not a religion–science claim."}
  primary_system: {value: UNKNOWN, how_known: "Repeated audience question 'Do you believe in God?' (Moscow 2010 lectures) answered 'I'm geek orthodox' — defined as believing technology is our friend (S6). Witty deflection, not ATHE, AGNOS, CHRIST, or JUDA. Commonweal talk of transcendence/digital artifacts (S7) is philosophical, not a system self-label. No force."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: ATHE, reason: "Rejected: asked whether he believes in God, he answered with a technology joke, not a denial of God (S6).", cites: [{source: S6, locator: "geek orthodox answer"}]}
    - {code: AGNOS, reason: "Rejected: no stated suspension of judgement on God (S6).", cites: [{source: S6, locator: "geek orthodox answer"}]}
  lio_axes:
    A_locus: {value: UNKNOWN, cites: [{source: S6, locator: "geek orthodox / Do you believe in God?"}, {source: S7, locator: "space for transcendence exchange"}], how_known: "Sought own words on God/divine locus (P19). Direct 'Do you believe in God?' (Moscow 2010) answered 'I'm geek orthodox' (= technology advocacy; S6) — no transcendent, immanent, or denial locus. Commonweal Spadaro exchange on 'space for transcendence' (S7) discusses artifact vs natural/digital processes, not a personal God claim. Do not force plot."}
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.5
      support: single
      cites: [{source: S5, locator: "'Laws of Physics' / approximations of reality; Newtonian model incomplete; theories revised by experiment"}]
      how_known: "Own written Senate testimony 17 July 2014 (S5; SciAm is the same text, not an independent corroborating source). Engineer not scientist (P30/P33; RQ-AA3-1): B needs an explicit nature-order remark (P16). Hilbert addendum: lawful-order remark with no no-exception claim → B 3 @0.5, alt 4. Support single."
      rationale: "Scored on his account of nature (P6), not on protocol engineering. Senate testimony: theories explain observations of natural (and artificial) phenomena; experiments validate or refute; 'Laws of Physics' are so-called laws that 'may be only approximations of reality' limited by measurement; every scientist must revise a pet theory when observation contradicts it; Newtonian notions were inadequate; Einstein and quantum models replaced complacency. That is a stated general lawfulness of nature (models of orderly reality we keep testing), with no miracle, petition, or reserved exemption, and no explicit no-exception claim (he softens inviolability). Named alternative 4 (P16 Hilbert / P40). Not B 4: he treats laws as revisable approximations. Not BELOW: the paradigm is still predictive lawfulness of nature."
      alternatives:
        - {value: 4, note: "A reviewer who reads the 'Laws of Physics' framing without the approximation caveat as exceptionless could score 4; the text itself undercuts inviolability.", cites: [{source: S5, locator: "Laws of Physics / approximations"}]}
    C_ledger: {value: UNKNOWN, how_known: "Nothing on personal reward/punishment read this pass (P19)."}
    D_authority: {value: UNKNOWN, how_known: "Scientific method vs revelation not scored as a clean D statement this pass (P19)."}
    E_scope: {value: UNKNOWN, how_known: "Nothing on in-group favour vs one order for all events scored this pass (P7/P19)."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, so the P4 test cannot be applied (P19). B 3 @0.5 alone cannot decide mid_basin."}
  statements:
    - text: "Humility is called for in this space. One hears the term \"Laws of Physics\" as if punishment awaits anyone or anything that dares to break them. And, yet, we know these so-called laws may be only approximations of reality – limited by the accuracy of our measurement tools and experimental capacity to validate their predictions. Every scientist must be prepared to cast aside or revise a pet theory if measurement and observation contradict it."
      cites: [{source: S5, locator: "Senate written testimony, 17 July 2014 (also SciAm republication)"}]
      date: "2014-07-17"
      context: "Written testimony before the U.S. Senate Committee on Commerce, Science and Transportation on federal research investment."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-24
    - text: "I am sure every member of this committee is well aware of the fundamental scientific paradigm: Theories are developed to explain observations or to speculate on how and why things might work. Experiments are undertaken to validate or refute the predictions of the theory. Theories are revised based on experimental results."
      cites: [{source: S5, locator: "opening scientific-paradigm paragraph"}]
      date: "2014-07-17"
      context: "Same Senate written testimony."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-24
    - text: "I'm geek orthodox. ... geek orthodoxy basically says, I really believe that technology is our friend here. Even when it doesn't seem to be, it can and should be."
      cites: [{source: S6, locator: "FCC FIRSTS podcast transcript, answer to 'Do you believe in God?'"}]
      date: "2024-04-02"
      context: "FCC FIRSTS conversation with Jessica Rosenworcel; recounts Moscow 2010 audience questions prompted by his 'Chief Internet Evangelist' title."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "primary facsimile"
      verified_on: 2026-10-24
      note: "Not scored as A or primary: deflection into technology advocacy, not a God/denial/suspension claim."
  changes_over_life: []
  coder_notes: "Living engineer (not scientist for B per McCarthy/RQ-AA3-1 / P33). B opened only because Senate testimony is explicit P16 nature-order talk (Hilbert pattern @0.5). Leads still useful: Stanford oral history full text; CHM oral history PDF; Bright Galaxies-style belief interviews if any surface. Do not code Geek Orthodoxy as a system."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Maternal: British, Irish, and French Canadian (mother born in Canada); paternal: Alsace–Lorraine to Kentucky", certainty: 0.7, cites: [{source: S8, locator: "Life and career"}], how_known: "Wikipedia."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated in S1 or S8."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1973", certainty: 0.7, cites: [{source: S1, locator: "para. 4"}, {source: S3, locator: "title page"}], how_known: "The one lasting item, dated by INWG Note 39 (P29, P30); alternative 1974."}
  age_at_first_lasting_contribution: {value: 30, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "title page"}], how_known: "1973 − 1943 = 30 (P30 year difference); alternative 31 (1974)."}
  first_evidence_of_lio_type_views: {value: "2014", certainty: 0.5, cites: [{source: S5, locator: "Laws of Physics passage"}], how_known: "Clearest B statement is 2014 Senate testimony (after span; no change of view documented — P31)."}
  lio_views_relative_to_major_work: {value: "after major work", certainty: 0.7, cites: [{source: S5, locator: "2014"}], how_known: "B evidence is 2014; no in-span nature-order profession found."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "No in-span (1973) own words on belief or nature-order read; B continuity under P31 rests on later testimony with no documented change."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Networking (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "Lane B only: geek-orthodox joke and Senate lawfulness talk do not decide mid_basin; A stays UNKNOWN."
  notes: "Do not treat technology advocacy as a worldview code."

institutions:
  - {value: "DARPA Information Processing Techniques Office", role: "program manager for networking", years: "1976–1982", kind: "government or state body", certainty: 0.7, cites: [{source: S1, locator: "para. 4–5"}], how_known: "Britannica."}
  - {value: "Stanford University", role: "faculty", years: "1972–1976", kind: "university", certainty: 0.7, cites: [{source: S1, locator: "para. 2"}, {source: S8, locator: "Life and career"}], how_known: "Britannica; Wikipedia."}
  - {value: "Google", role: "vice president and chief Internet evangelist", years: "2005–2026", kind: "commercial", certainty: 0.7, cites: [{source: S1, locator: "para. 5"}, {source: S8, locator: "Life and career (retired July 2026)"}], how_known: "Britannica; Wikipedia retirement note."}
collaborators:
  - {value: "Robert Kahn", relation: "collaborator", note: "co-designer of TCP/IP", certainty: 0.7, cites: [{source: S1, locator: "para. 3–4"}], how_known: "Britannica."}
  - {value: "Leonard Kleinrock", relation: "mentor or employer", note: "UCLA laboratory", certainty: 0.7, cites: [{source: S1, locator: "para. 3"}], how_known: "Britannica."}
  - {value: "Steve Crocker", relation: "collaborator", note: "Van Nuys High / UCLA ARPANET", certainty: 0.7, cites: [{source: S6, locator: "mentor answer"}, {source: S8, locator: "Life and career"}], how_known: "Own words; Wikipedia."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 222"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Not a scientist (P30/P33; RQ-AA3-1 open): B scored only from explicit P16 nature-order testimony, Hilbert-style @0.5."
    - "SciAm 2014 page is republication of the same Senate text — not a second independent B source (support stays single)."
    - "A and primary still UNKNOWN after deepen (do not force plot)."
    - "Living."
  open_questions:
    - "Stanford oral history (Gwiazda) and CHM oral history full text for any quieter A."
    - "Any in-span (c. 1973) nature-order or belief statement."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Michael Aaron Dennis"
    citation: "Dennis, Michael Aaron. 'Vinton Cerf.' Encyclopaedia Britannica (scholars edition). https://kids.britannica.com/scholars/article/Vinton-Cerf/389928"
    url: "https://kids.britannica.com/scholars/article/Vinton-Cerf/389928"
    accessed: 2026-10-19
    reliability_note: "Signed article, scholars edition, read in full at creation."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, timing, institutions, collaborators]
  - id: S2
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [review]
  - id: S3
    type: primary
    kind: "archive record"
    author: "Vinton Cerf; Robert Kahn"
    citation: "Cerf, V., and R. Kahn. 'HOST and PROCESS Level Protocols for Internetwork Communication.' INWG Note 39, NIC 18764, September 1973. Scan at Internet Archive: https://archive.org/details/HostAndProcessLevelProtocolsForInternetworkCommunication"
    url: "https://archive.org/details/HostAndProcessLevelProtocolsForInternetworkCommunication"
    accessed: 2026-10-19
    reliability_note: "Archive item record (title, authors, 1973) read; scan not read in full. The Sussex venue is from the AA10 audit (INWG records), not verified here."
    source_quality: "archive scan (OCR only)"
    used_for: [contribution, timing]
  - id: S4
    type: secondary
    kind: "journal article"
    author: "UNKNOWN"
    citation: "'Some computer network interconnection issues.' AFIPS National Computer Conference proceedings (1974). doi:10.1145/1500175.1500335"
    url: "https://doi.org/10.1145/1500175.1500335"
    accessed: 2026-10-19
    reliability_note: "Reference list read: cites Cerf and Kahn, INWG Note #39, NIC #18764, September 1973."
    source_quality: "scholarly edition or monograph"
    used_for: [timing]
  - id: S5
    type: primary
    kind: "published work by the subject"
    author: "Vinton G. Cerf"
    year: 2014
    citation: "Cerf, Vinton G. Written testimony before the U.S. Senate Committee on Commerce, Science and Transportation, hearing 'The Federal Research Portfolio: Capitalizing on Investments in R&D,' 17 July 2014. PDF: https://www.commerce.senate.gov/wp-content/uploads/media/doc/Cerf%20Testimony.pdf ; also Scientific American republication 22 July 2014: https://www.scientificamerican.com/article/vinton-g-cerf-the-value-of-investment-by-the-u-s-government-cannot-be-overstated/"
    url: "https://www.commerce.senate.gov/wp-content/uploads/media/doc/Cerf%20Testimony.pdf"
    accessed: 2026-10-24
    reliability_note: "Own written testimony; SciAm page read in full this pass (same text)."
    source_quality: "primary / own words"
    used_for: [worldview, timing]
  - id: S6
    type: primary
    kind: "other"
    author: "Vint Cerf; Jessica Rosenworcel (interviewer)"
    year: 2024
    citation: "Rosenworcel, Jessica. 'FIRSTS Conversation with One of the Father's of the Internet.' Federal Communications Commission podcast / speaker series #6, recorded April 2024; transcript published at https://www.fcc.gov/news-events/podcast/firsts-conversation-one-fathers-internet"
    url: "https://www.fcc.gov/news-events/podcast/firsts-conversation-one-fathers-internet"
    accessed: 2026-10-24
    reliability_note: "Official FCC transcript read in full this pass; geek-orthodox / God-question passage."
    source_quality: "primary / own words"
    used_for: [worldview, childhood, collaborators]
  - id: S7
    type: secondary
    kind: "other"
    author: "Antonio Spadaro (interviewing Vint G. Cerf)"
    year: 2026
    citation: "Spadaro, Antonio. 'Memory in the Digital Age: A conversation with Vint G. Cerf.' Commonweal Magazine, 8 October 2026. https://www.commonwealmagazine.org/vint-cerf-spadaro-interview-digital-memory"
    url: "https://www.commonwealmagazine.org/vint-cerf-spadaro-interview-digital-memory"
    accessed: 2026-10-24
    reliability_note: "Interview page read in full; transcendence/artifact exchange unused for A (no locus profession)."
    source_quality: "newspaper interview"
    used_for: [worldview]
  - id: S8
    type: tertiary
    kind: "encyclopedia"
    author: "Wikipedia contributors"
    citation: "Wikipedia. 'Vint Cerf.' https://en.wikipedia.org/wiki/Vint_Cerf"
    url: "https://en.wikipedia.org/wiki/Vint_Cerf"
    accessed: 2026-10-24
    reliability_note: "P50 dual bio with Britannica; used for parents/ancestry and career dates — not alone for axis values. No religion section."
    source_quality: "reference entry"
    used_for: [identity, basics, childhood, heritage, institutions, collaborators]
---

## Summary

Vint Cerf (born 1943), Internet co-designer [S1]. Deepen D1: B 3 @ 0.5 (P16 Hilbert); A UNKNOWN; primary UNKNOWN. Mid UNKNOWN. Not plotted.

## Life and work

New Haven; Stanford; UCLA; DARPA; Google (Chief Internet Evangelist) [S1, S8].

## Contribution and impact

INWG Note 39, 1973; TCP/IP with Kahn [S1, S3].

## Childhood and education

Fifth-grade algebra push; Van Nuys High with Crocker; Stanford; UCLA [S1, S6, S8].

## Adult working worldview

Senate 2014: 'Laws of Physics' as revisable approximations of reality; scientific paradigm of theory and experiment [S5]. Asked whether he believes in God (Moscow 2010), answered 'I'm geek orthodox' (= technology is our friend) [S6] — not scored as A or primary. Lane A public record only.

## Heritage (context only)

Maternal British/Irish/French Canadian; paternal Alsace–Lorraine [S8]. Family religion UNKNOWN. Context only — never an outcome.

## Timing

1973, age 30 [S3]. Clearest B statement 2014 (after major work; P31 continuity).

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Geek-orthodox joke is not a code; B alone does not decide mid_basin.

## Open questions

- Stanford and CHM oral histories for any quieter A.
- Any in-span (c. 1973) nature-order or belief statement.

## Research log

- 2026-10-20: AA10 audit fix: span 1973 (INWG Note 39, Sussex, September 1973; S3, S4), age 30; 1974 as the alternative.
- 2026-10-20: Read Britannica (Dennis, scholars edition).
- 2026-10-24: Deepen D1 — Senate/SciAm 2014 (S5); FCC FIRSTS 2024 (S6); Commonweal Spadaro (S7); Wikipedia (S8). Person-file only commit; drafts/ and reports/ left uncommitted; figures/ untouched.
