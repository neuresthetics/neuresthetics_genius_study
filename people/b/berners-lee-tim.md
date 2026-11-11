---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch L; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to computer_science. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch L, order P32: F 5, rank 77). Basics from Britannica (Michael Aaron Dennis); Top Questions not cited. Worldview from his own essay 'The World Wide Web and the \"Web of Life\"' (1998, w3.org). Not a scientist under P30 (computer science). primary_system BELOW_THRESHOLD (Unitarian Universalist, no study code); A BELOW_THRESHOLD; B UNKNOWN (P16); mid_basin UNKNOWN (P19). Not plotted. Draft, not reviewed."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Audit fixes (fallacy_catalog audit of 2742382, run 1). No change: primary_system stays BELOW_THRESHOLD (no UU code, not mapped to SECHUM); UU recorded under nominal_affiliations."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #76, F5 rank 77). Needs: A BELOW_THRESHOLD; B UNKNOWN. Primaries/own words: 1998 w3.org UU essay (S2) re-read; Business Insider / Die Welt Döpfner interview 7 May 2017 (S4) 'Not in the sense of most people. I'm atheist and Unitarian Universalist.'; UU World Graff 1999 (S5) interview paraphrase on MIT UU / no dogma; w3.org FAQ physics replies (S6); Wikipedia EN dual bio (S7, P50) with Britannica create-pass body retained (S1; live JS-empty this pass). P47 on S1–S8. Not a scientist (P30/P33: Web/HTML/HTTP/URI are inventions, not theories about natural systems) — B stays UNKNOWN (P16); physics 'microscopic rule → macroscopic' remarks are design analogies, not a scored B account. primary_system BELOW→ATHE @0.5 (interview self-label; alt BELOW / SECHUM). A BELOW→4 @0.5 support single (interview; alt BELOW_THRESHOLD for span vacuum / UU without God term, P38). D UNKNOWN→3 @0.5 (essay reject dogma / One True Churches + quest-for-truth skepticism). C/E UNKNOWN. mid_basin stays UNKNOWN (B UNKNOWN, P19). Span stays 1989–1991. Chart-moving NO (still unplottable; B UNKNOWN). No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: berners-lee-tim
  display_name: "Tim Berners-Lee"
  roster:
    canonical_name: "Tim Berners-Lee"
    rank: 77
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: computer science
    field_bucket: "computer science / AI"
  full_name: {value: "Timothy John Berners-Lee", certainty: 1.0, cites: [{source: S7, locator: "infobox birth_name"}, {source: S1, locator: "header (Sir Tim Berners-Lee)"}], how_known: "Wikipedia birth_name; Britannica honorific form."}
  native_name: {value: UNKNOWN, how_known: "English."}
  aliases:
    - {name: "Sir Tim Berners-Lee", kind: "title or honorific"}
    - {name: "TimBL", kind: "other"}
    - {name: "TBL", kind: "other"}

basics:
  birth:
    date: {value: "1955-06-08", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "infobox"}], how_known: "Two sources."}
    place: {value: "London, England", modern_name: "London, United Kingdom", polity_then: "United Kingdom", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "infobox"}], how_known: "Two sources."}
  death:
    date: {value: UNKNOWN, how_known: "Living."}
    place: {value: UNKNOWN, how_known: "Living."}
  first_lasting_contribution_year: {value: 1989, certainty: 0.7, cites: [{source: S1, locator: "CERN paragraph"}, {source: S7, locator: "proposal 12 March 1989"}], how_known: "Proposal for a global hypertext system (1989), the Web's founding document (P30)."}
  era_bucket: {value: "1950 on", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "infobox"}], how_known: "Birth year bucket (P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "infobox"}], how_known: "United Kingdom (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "CERN paragraph"}, {source: S7, locator: "workplaces CERN / MIT"}], how_known: "CERN, Geneva, for the Web's invention; later MIT / Oxford (P3 Western Europe for CERN years)."}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S1, locator: "text"}, {source: S7, locator: "he/him"}], how_known: "As recorded."}
  languages_of_work: {value: [English], certainty: 0.7, cites: [{source: S2, locator: "text"}], how_known: "His own essay and FAQ."}
  occupations: {value: ["computer scientist", "software engineer"], certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "lead"}], how_known: "Two sources."}
contribution:
  primary_domain: computer_science
  fields: {value: ["computer science"], certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "lead"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Proposal for a global hypertext document system using the Internet (World Wide Web)", year: 1989, kind: invention, lasting: "the World Wide Web (S1, S7)", certainty: 0.7, cites: [{source: S1, locator: "CERN paragraph"}, {source: S7, locator: "proposal 12 March 1989"}], how_known: "Two sources."}
    - {value: "First Web server and first Web client (browser); HTTP, HTML, URI/URL", year: 1991, kind: invention, lasting: "core Web stack (S1, S7)", certainty: 0.7, cites: [{source: S1, locator: "CERN paragraph"}, {source: S7, locator: "lead / 1990–91"}], how_known: "Written October 1990 to summer 1991; end year used (P12/P30)."}
  evidence_of_impact:
    - {value: "Knighthood and inaugural Millennium Technology Prize (2004); Turing Award (2016)", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "awards"}], how_known: "Two sources."}
  major_works:
    - {value: "Weaving the Web (HarperCollins / Orion)", year: 1999, kind: book, certainty: 0.5, cites: [{source: S6, locator: "FAQ note pointing to the book"}], how_known: "His FAQ points to it; page-check of religion chapters not done this pass."}
  honours:
    - {value: "Millennium Technology Prize", year: 2004, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    - {value: "Turing Award", year: 2016, certainty: 0.7, cites: [{source: S7, locator: "awards"}], how_known: "Wikipedia."}
  definition_fit: {value: "clearly meets", rationale: "Inventor of the World Wide Web (S1, S7).", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "lead"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Church of England (Protestant / Anglican)", certainty: 0.7, cites: [{source: S2, locator: "'Where I'm coming from'"}, {source: S7, locator: "Personal life"}], how_known: "Own essay; Wikipedia Anglican."}
  family_religious_practice: {value: "Religious upbringing; confirmed as a teenager", certainty: 0.7, cites: [{source: S2, locator: "'Where I'm coming from'"}], how_known: "His own essay."}
  parents_and_household:
    - {value: "Conway Berners-Lee and Mary Lee Woods (Berners-Lee); both worked on the Ferranti Mark I", role: parents, certainty: 0.7, cites: [{source: S1, locator: "paragraph 2"}, {source: S7, locator: "Early life"}], how_known: "Two sources."}
  household_circumstances: {value: TODO}
  schooling:
    - {value: "Sheen Mount Primary School", stage: elementary school, run_by: other, certainty: 0.5, cites: [{source: S7, locator: "Early life"}], how_known: "Wikipedia."}
    - {value: "Emanuel School (direct-grant grammar), 1969–1973", stage: "grammar or secondary school", run_by: other, certainty: 0.7, cites: [{source: S7, locator: "Early life"}], how_known: "Wikipedia / Who's Who cite."}
    - {value: "The Queen's College, Oxford; first-class BA in physics (1976)", stage: university, run_by: other, certainty: 0.7, cites: [{source: S1, locator: "paragraph 2"}, {source: S7, locator: "Early life"}], how_known: "Two sources; physics degree from Wikipedia."}
  early_mathematics: {value: "advanced mathematics", certainty: 0.5, cites: [{source: S6, locator: "Physics: why and influence"}], how_known: "Own FAQ: parents mathematicians; childhood maths/paper tape; later Oxford physics (coder maps to advanced mathematics)."}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure:
    - {value: "Electronics hobby; built computers from cardboard / old TV; Oxford physics", certainty: 0.7, cites: [{source: S6, locator: "Physics FAQ"}, {source: S7, locator: "Early life"}], how_known: "Own FAQ and Wikipedia."}
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [English], certainty: 0.5, cites: [{source: S2, locator: "text"}], how_known: "Coder's reading."}
  notable_events:
    - {value: "Rejected his Church of England upbringing as a teenager, just after confirmation", certainty: 0.7, cites: [{source: S2, locator: "'Where I'm coming from'"}], how_known: "His own essay; no year given."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1989–1991", certainty: 0.7, cites: [{source: S1, locator: "CERN paragraph"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Unitarian Universalist congregation (Boston area), joined after having children / after moving to MIT (1994)", years: "by 1998", role: member, certainty: 0.7, cites: [{source: S2, locator: "'Where I'm coming from'"}, {source: S5, locator: "MIT UU parish"}], how_known: "Own essay; UU World interview paraphrase places the UU turn after 1994 MIT arrival."}
  self_described_science_religion_relation: {value: "UUs 'allow or even require their belief to be compatible with reason' (1998); self-label 'atheist and Unitarian Universalist' (2017).", certainty: 0.7, cites: [{source: S2, locator: "'Where I'm coming from'"}, {source: S4, locator: "closing exchange on God"}], how_known: "Own essay and interview."}
  primary_system:
    value: ATHE
    basis: recorded_interview
    certainty: 0.5
    cites: [{source: S4, locator: "Do you believe in God? / I'm atheist and Unitarian Universalist"}]
    rationale: "2017 Döpfner interview: 'Not in the sense of most people. I'm atheist and Unitarian Universalist.' Positive atheist self-label (ATHE). Study has no UU system code; UU kept under nominal_affiliations. Contested: create-pass BELOW (no God statement in 1998 essay; vacuum 'Christian philosophy without dogma'); SECHUM if UU dignity/reason identity were read as humanist movement rather than metaphysics — rejected (SECHUM needs humanist-movement public identity; UU is a denomination). Cap 0.5 (named alternatives + interview after span)."
    how_known: "(interview) Business Insider / Die Welt Döpfner Q&A 7 May 2017 (S4), his own words (P8). Adult-life evidence for the working years under P31: teenage C of E rejection already in place before 1989–91; no sourced conversion to theism between the span and 2017; UU join (after Web) is affiliation/community, not a theistic turn. Retrospective / after-span interview still at most 0.5 with named alt BELOW."
    alternatives:
      - {value: BELOW_THRESHOLD, note: "Create-pass / span vacuum: 1998 essay states no personal God view; 'Christian philosophy without dogma' seeking before UU.", cites: [{source: S2, locator: "'Where I'm coming from'"}]}
      - {value: SECHUM, note: "If UU + human dignity/reason were coded as humanist-movement identity; rejected under SECHUM use_when.", cites: [{source: S2, locator: "fundamental value and dignity"}]}
  secondary_system: {value: UNKNOWN, how_known: "UU affiliation is nominal; no second metaphysical code scored."}
  candidate_codes_considered:
    - {code: ATHE, reason: "Self-described atheist (2017 interview)."}
    - {code: SECHUM, reason: "UU dignity/reason emphasis; rejected — not humanist-movement public identity."}
    - {code: AGNOS, reason: "No explicit suspension; he affirms atheist. Create-pass BELOW (no UU code) is named under primary_system.alternatives, not here."}
    - {code: CHRIST, reason: "Sought 'Christian philosophy without dogma' after rejecting C of E; not a working confession."}
  lio_axes:
    A_locus:
      value: 4
      basis: recorded_interview
      certainty: 0.5
      support: single
      cites: [{source: S4, locator: "I'm atheist and Unitarian Universalist"}]
      rationale: "No God in the ordinary sense: asked 'Do you believe in God?', answers 'Not in the sense of most people. I'm atheist…' (P38). Contested span reading (essay leaves God optional for UUs) named as alt BELOW_THRESHOLD."
      how_known: "(interview) S4 closing exchange; single source for the A 4 value (P48 single). After-span interview + named alt → 0.5."
      alternatives:
        - {value: BELOW_THRESHOLD, note: "1998 essay never states his own denial of God; only UU tolerance 'if they use the term'.", cites: [{source: S2, locator: "'Tolerance'"}]}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist under P30/P33: lasting contributions are the Web proposal, server/browser, and HTTP/HTML/URI — inventions and protocols, not theories or results about physical or natural systems. For a non-scientist, B needs an explicit remark on the order of nature (P16); none scored. FAQ/Bush-talk physics analogies (microscopic rules → macroscopic behaviour; 'laws of physics' for particles vs protocols for web objects) are design metaphors, not a LIO account of law and exception (same pattern as Knuth's discrete-code remark)."}
    C_ledger: {value: UNKNOWN, how_known: "No statement on afterlife, soul, or cosmic justice in S1–S8."}
    D_authority:
      value: 3
      basis: written_profession
      certainty: 0.5
      support: single
      cites: [{source: S2, locator: "'Where I'm coming from'; 'Truth'; Independent Invention"}]
      rationale: "Rejects C of E confirmation of 'unbelievable things'; attacks One True Churches / divine-prophet exclusivism; 'quest for the truth is always accompanied by skepticism of anyone claiming to have found it.' Reason-compatible belief over dogma. Not a full naturalist D 4 (still participates in UU religion). Single essay cluster → 0.5."
      how_known: "Own 1998 w3.org essay (written_profession)."
    E_scope: {value: UNKNOWN, how_known: "Not a scientist; working practice does not score E (P19/P30). No statement on same laws everywhere (P7)."}
  mid_basin: {value: UNKNOWN, how_known: "B is UNKNOWN; UNKNOWN takes precedence (P19). A 4 @0.5 would not clear the A≥3 branch at 0.7 anyway (P10)."}
  statements:
    - text: "Like many people, I had a religious upbringing which I rejected as a teenager: in my case it was a protestant Christian (Church of England) upbringing. I rejected it just after being \"confirmed\" and told how essential it was to believe in all kinds of unbelievable things."
      cites: [{source: S2, locator: "'Where I'm coming from'"}]
      date: "1998"
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "His own page on w3.org; re-verified this deepen."
    - text: "They respect those who believe in some sort of a God different from theirs (if they use the term)."
      cites: [{source: S2, locator: "'Tolerance'"}]
      date: "1998"
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "About UUs in general, not a statement of his own belief; kept as context for alt BELOW."
    - text: "The quest for the truth is always accompanied by skepticism of anyone claiming to have found it."
      cites: [{source: S2, locator: "'Truth'"}]
      date: "1998"
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
    - text: "Not in the sense of most people. I'm atheist and Unitarian Universalist."
      cites: [{source: S4, locator: "closing: Do you believe in God?"}]
      date: "2017-05-07"
      context: "Mathias Döpfner interview, Business Insider / Die Welt; last Q&A exchange."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Live Business Insider page opened this pass; quote matches Wikipedia/FFRF secondary citations."
    - text: "In physics, you learn to think up some simple mathematical rule on a microscopic scale, which when scaled will explain the macroscopic behavior. On the Internet, we try to dream up computer protocols which when extrapolated to the macroscopic will produce an information space with properties we would like."
      cites: [{source: S6, locator: "Physics: why and influence (1997 New Scientist replies)"}]
      date: "1997"
      axes: []
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Design analogy only; not used to score B (P16/P33)."
  changes_over_life:
    - {value: "Rejected Church of England as a teenager (just after confirmation). During/after that rejection he describes a years-long vacuum seeking 'the basis for Christian philosophy but without the dogma.' Joined a Unitarian Universalist congregation after having children / after the 1994 MIT move (essay 1998; UU World). 2017 interview self-labels 'atheist and Unitarian Universalist.' No sourced theistic reconversion between the Web span and 2017.", certainty: 0.7, cites: [{source: S2, locator: "'Where I'm coming from'"}, {source: S5, locator: "MIT UU"}, {source: S4, locator: "atheist and UU"}], how_known: "Own essay + interview; UU World paraphrase for MIT timing."}
  coder_notes: "Deepen D1: ATHE/A4 from S4 interview; B stays UNKNOWN (inventor, P33). No UU system code — UU nominal only. Physics analogies (S6) and Bush Symposium particle/law metaphors deliberately not scored for B. Weaving the Web (1999) unread for worldview this pass. Lane A scores separate from Lane B geometric labels. No fallacy_catalog (Jason)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "English", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "lead"}], how_known: "Two sources."}
  religious_heritage_by_birth: {value: "Church of England (Anglican)", certainty: 0.7, cites: [{source: S2, locator: "'Where I'm coming from'"}, {source: S7, locator: "Personal life"}], how_known: "Own essay; Wikipedia."}
  baptism_or_initiation: {value: "Confirmed in the Church of England as a teenager", certainty: 0.7, cites: [{source: S2, locator: "'Where I'm coming from'"}], how_known: "His own essay."}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1989–1991", certainty: 0.7, cites: [{source: S1, locator: "CERN paragraph"}, {source: S7, locator: "1989–91"}], how_known: "First to last listed lasting contribution (P29, P30)."}
  age_at_first_lasting_contribution: {value: 34, certainty: 0.7, cites: [{source: S1, locator: "opening; CERN paragraph"}, {source: S7, locator: "birth 1955 / proposal 1989"}], how_known: "1989 − 1955 = 34 (P30)."}
  first_evidence_of_lio_type_views: {value: "2017", certainty: 0.5, cites: [{source: S4, locator: "atheist self-label"}], how_known: "First scored A≥3 evidence; 1998 essay bears on D but A was not scored from it. Earlier works not read for God (P30)."}
  lio_views_relative_to_major_work: {value: "after major work", certainty: 0.7, cites: [{source: S4, locator: "2017"}, {source: S2, locator: "1998"}], how_known: "Essay and interview after 1991 span."}
  worldview_during_major_work: {value: "Post–C of E rejection; pre-UU. No God statement from 1989–91 read. Adult-life atheist self-label applied to the span under P31 (no theistic reconversion sourced).", certainty: 0.5, cites: [{source: S2, locator: "Web before UU"}, {source: S4, locator: "atheist"}], how_known: "Essay places UU after Web development."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "No geometric-theology reading attempted; protocols-as-rules metaphors are engineering, not Lane B form.", certainty: 0.5, cites: [{source: S6, locator: "Physics FAQ"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Not read."}
  circle_present: {value: "no", rationale: "Atheist self-label; UU without a stated personal God circle.", certainty: 0.5, cites: [{source: S4, locator: "atheist"}], how_known: "Coder's reading of Lane B labels."}
  reading: "Atheist UU; reason-compatible liberal religion; inventing engineer not natural-philosopher for B."
  notes: "Lane B separate from Lane A axis scores."

institutions:
  - {value: "CERN", role: "software engineer", years: "1980; 1984–1994", kind: "research institute", certainty: 0.7, cites: [{source: S1, locator: "CERN paragraph"}, {source: S7, locator: "workplaces"}], how_known: "Two sources."}
  - {value: "Massachusetts Institute of Technology / W3C", role: "W3C Director; CSAIL", years: "1994–", kind: university, certainty: 0.7, cites: [{source: S7, locator: "workplaces"}, {source: S6, locator: "Roles at MIT"}], how_known: "Wikipedia and own FAQ."}
  - {value: "University of Oxford", role: "professorial research fellow", kind: university, certainty: 0.5, cites: [{source: S7, locator: "lead"}], how_known: "Wikipedia."}
collaborators: []

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 77"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Britannica live page JS-empty this deepen pass; create-pass body retained; Wikipedia dual bio (P50)."
    - "A and primary_system rest on after-span 2017 interview (0.5); 1998 essay alone left A BELOW."
    - "FFRF freethought page is a secondary lead only; Telegraph 2008 unread."
  open_questions:
    - "Weaving the Web (1999) chapter-check for any God/nature statement that could corroborate A or score B."
    - "Telegraph 30 Mar 2008 'relieved a great tension' context (FFRF secondary S8) — full article unread."
    - "Any explicit own-words account of natural law / miracles for B."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Michael Aaron Dennis"
    citation: "Dennis, Michael Aaron. \"Tim Berners-Lee.\" Encyclopaedia Britannica, updated 26 September 2026. https://www.britannica.com/biography/Tim-Berners-Lee."
    url: "https://www.britannica.com/biography/Tim-Berners-Lee"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Signed body (with Britannica Editors); Top Questions not cited. Live page was JS-empty this deepen pass; create-pass reading retained for CERN/honours; Wikipedia dual bio for dates/name (P50)."
    used_for: [identity, basics, contribution, childhood, heritage, timing, lane_b, institutions]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Tim Berners-Lee"
    citation: "Berners-Lee, Tim. \"The World Wide Web and the 'Web of Life'.\" 1998. https://www.w3.org/People/Berners-Lee/UU.html."
    url: "https://www.w3.org/People/Berners-Lee/UU.html"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "His own page on the W3C site; full text re-read this deepen."
    used_for: [basics, childhood, worldview, heritage, timing, lane_b]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    source_quality: "study roster"
    reliability_note: "Study's own roster."
    used_for: [identity, review]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "Tim Berners-Lee; interviewer Mathias Döpfner"
    citation: "Döpfner, Mathias. \"The inventor of the web Tim Berners-Lee on the future of the internet, 'fake news,' and why net neutrality is so important.\" Business Insider / Die Welt, 7 May 2017. https://www.businessinsider.com/mathias-dopfner-tim-berners-lee-world-wide-web-interview-2017-5."
    url: "https://www.businessinsider.com/mathias-dopfner-tim-berners-lee-world-wide-web-interview-2017-5"
    accessed: 2026-10-24
    source_quality: "newspaper interview"
    reliability_note: "Full Q&A opened this pass; closing exchange is first-person. Kind kept as published work by the subject for schema; source_quality newspaper interview (P47)."
    used_for: [worldview, timing, lane_b]
  - id: S5
    type: secondary
    kind: "journal article"
    author: "E. J. Graff"
    citation: "Graff, E. J. \"Keeping cyberspace free: Tim Berners-Lee and the World Wide Web.\" UU World, May/June 1999 (republished 23 August 2016). https://www.uuworld.org/articles/keeping-cyberspace-free."
    url: "https://www.uuworld.org/articles/keeping-cyberspace-free"
    accessed: 2026-10-24
    source_quality: "other"
    reliability_note: "Magazine interview feature; paraphrases his words on MIT UU parish — used for affiliation timing, not to score A alone (reported speech / paraphrase)."
    used_for: [worldview, timing]
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "Tim Berners-Lee"
    citation: "Berners-Lee, Tim. \"Frequently asked questions by the Press.\" W3C. Physics replies based on New Scientist (David Brake), 1997/9. https://www.w3.org/People/Berners-Lee/FAQ.html."
    url: "https://www.w3.org/People/Berners-Lee/FAQ.html"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "Own FAQ page; physics section used only as non-scoring B-blocker context."
    used_for: [basics, childhood, contribution, institutions, worldview]
  - id: S7
    type: secondary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia. \"Tim Berners-Lee.\" English Wikipedia. https://en.wikipedia.org/wiki/Tim_Berners-Lee."
    url: "https://en.wikipedia.org/wiki/Tim_Berners-Lee"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Dual bio with Britannica (P50). Personal life cites S4 for the atheist quote; Early life for parents/Emanuel/Queen's."
    used_for: [identity, basics, contribution, childhood, heritage, timing, institutions, review]
  - id: S8
    type: secondary
    kind: "institutional page"
    author: "Freedom From Religion Foundation"
    citation: "Freedom From Religion Foundation. \"Tim Berners-Lee\" (Freethought of the Day). https://ffrf.org/publications/day/tim-berners-lee/."
    url: "https://ffrf.org/publications/day/tim-berners-lee/"
    accessed: 2026-10-24
    source_quality: "other"
    reliability_note: "Secondary compilation quoting S2 and S4; lead to Telegraph 2008 not opened. Not used alone to score."
    used_for: [review]
---

# Tim Berners-Lee

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Tim Berners-Lee (born 1955), English computer scientist, inventor of the World Wide Web [S1; S7]. Deepen D1: primary_system ATHE @0.5 (interview); A 4 @0.5 single (interview; alt BELOW); B UNKNOWN (inventor, P33/P16); D 3 @0.5; mid_basin UNKNOWN. Chart-moving NO (still unplottable).

## Life and work

Oxford physics (Queen's College, 1976); Plessey; CERN; MIT/W3C [S1; S7].

## Contribution and impact

Web proposal (1989); first server and browser / HTTP–HTML–URI (1990–91) [S1; S7]. Turing Award 2016 [S7].

## Childhood and education

Church of England upbringing, rejected as a teenager after confirmation [S2]. Parents Conway Berners-Lee and Mary Lee Woods on the Ferranti Mark I [S1; S7]. Emanuel School; Queen's College, Oxford [S7].

## Adult working worldview

Working years 1989–1991: post–C of E rejection, pre-UU [S2]. Unitarian Universalist by the late 1990s [S2; S5]. 2017 interview: "I'm atheist and Unitarian Universalist" [S4] — scores ATHE and A 4 @0.5 (interview). B UNKNOWN: Web stack is invention under P33; no scored nature-order remark [S6]. D 3 @0.5 from the 1998 essay's anti-dogma lines [S2].

## Heritage (context only)

Church of England / Anglican [S2; S7].

## Timing

First lasting contribution 1989, at 34 [S1; S7]. LIO A evidence 2017, after major work [S4].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Circle absent under atheist self-label [S4]. Geometric form unclear.

## Open questions

- Weaving the Web (1999) for corroborating A or any B-capable nature remark.
- Telegraph 30 Mar 2008 full text (FFRF lead) [S8].

## Research log

- 2026-10-15: Read Britannica (Dennis) and his 1998 UU essay on w3.org.
- 2026-10-24: Deepen D1 — BI/Die Welt Döpfner interview (S4); UU World Graff (S5); w3.org FAQ (S6); Wikipedia dual bio (S7); FFRF lead (S8). Britannica live JS-empty. No fallacy audit.
