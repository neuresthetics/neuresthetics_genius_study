---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA5; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to 20c_late. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #185, F3 rank 197). Opened own-voice autobiographies: Reaching for the Moon ch.1 via Simon & Schuster publisher excerpt (S5) — 'There was only one God... We let God be the judge of that'; georgia preach sermon quotation of RFTM (S6, secondary) — 'God gives us no guarantees that our road will be easy'; My Remarkable Journey via Bookey quote page (S7, secondary) — 'my foundation—my faith, my family, and my friends'; Oprah Daily / LitHub MRJ excerpts (S8–S9); AARP 2018 interview (S10); Blount funeral eulogy PDF (S3 full text). A_locus UNKNOWN → 0 @0.5 written_profession (support single on S5; S6 secondary corroborates providence language). primary_system stays BELOW_THRESHOLD CHRIST lead (Y2 not met: no 'I am a Christian/Presbyterian' or Christ/creed profession in published own words; Blount Jesus/resurrection report is pastor paraphrase of conversation — reported speech). B stays UNKNOWN (RQ-AA5-1 not a scientist; no nature-law statement). mid stays UNKNOWN. Childhood Methodist (St. James) and parents Joshua/Joylette Coleman filled from S5. major_work_period stays UNKNOWN (P13/Lamarr). Still not plotted. P47 on S1–S10. No fallacy_catalog; no figures/. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "AA5 audit fix (v8's call on the auditor's advice): first-lasting year, span, working years, age and era set to UNKNOWN (P13, Lamarr precedent), with 1960 and 1962 as candidates; church roles not in S2 (choir, church officer, ruling elder) dropped. RQ-AA5-1 and RQ-AA5-2 recorded as coded."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA5, order P32: F 3, rank 197). Sources: NASA biography by Margot Lee Shetterly (2016, read in full) and Presbyterian Church (U.S.A.) news (2017, read in full); Blount's statement (Union Presbyterian Seminary, 2020) seen as a search excerpt only. Lasting work: the orbital-flight equations of 'Determination of Azimuth Angle at Burnout for Placing a Satellite Over a Selected Earth Position' (1960, with Ted Skopinski), and the 1962 hand verification of John Glenn's orbital trajectory, 'the work that she would become most known for' (S1). No source calls a result lasting ('pioneering legacy', S1), so first-lasting year, span, age and era are UNKNOWN (P13, Lamarr precedent; AA5 audit), with 1960 and 1962 as candidates. Not a scientist: trajectory computation applies known laws rather than stating a new result about nature (P30, by analogy with P33); ruling question RQ-AA5-1. Worldview: decades of church leadership ('several leadership roles including ... its finance chair', S2) and her pastor's report of 'deep' Christian faith, but no profession of her own read, so BELOW_THRESHOLD with lead CHRIST (Toni Morrison precedent, RQ-Y2); ruling question RQ-AA5-2. A UNKNOWN; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}

identity:
  id: johnson-katherine
  display_name: "Katherine Johnson"
  roster:
    canonical_name: "Katherine Johnson"
    rank: 197
    F: 3
    models: [DeepSeek, GPT, Grok]
    band: "core (3–4)"
    status: "core"
    field: "mathematics"
    field_bucket: "mathematics"
  full_name: {value: "Katherine G. Johnson", certainty: 0.7, cites: [{source: S2, locator: "headline"}], how_known: "PC(USA)."}
  native_name: {value: "Katherine Johnson", certainty: 0.7, cites: [{source: S1, locator: "title"}], how_known: "NASA."}
  aliases:
    - {name: "Katherine-Johnson", kind: "roster alias"}
    - {name: "Katherine Goble Johnson", kind: "other"}

basics:
  birth:
    date: {value: "1918-08-26", certainty: 0.7, cites: [{source: S1, locator: "facts box"}], how_known: "NASA."}
    place: {value: "White Sulphur Springs, West Virginia", modern_name: "White Sulphur Springs, West Virginia, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "facts box; para. 1"}], how_known: "NASA."}
  death:
    date: {value: "2020-02-24", certainty: 0.7, cites: [{source: S1, locator: "final paragraph"}], how_known: "NASA."}
    place: {value: UNKNOWN, how_known: "Not stated in the sources read."}
  first_lasting_contribution_year: {value: UNKNOWN, how_known: "No source read calls any of her results lasting (P13; Lamarr precedent, Z10). Candidates: 1960, the report with Ted Skopinski 'laying out the equations describing an orbital spaceflight in which the landing position of the spacecraft is specified' (S1); 1962, the Glenn verification (S1). v8's call on the auditor's advice (AA5)."}
  era_bucket: {value: UNKNOWN, how_known: "No dated lasting contribution; her adult life (1936 on) crosses the 1950 edge (P39)."}
  region_of_birth: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "para. 1"}], how_known: "USA (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "para. 2"}], how_known: "Langley, Virginia."}
  sex_as_recorded: {value: "female", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "para. 4"}], how_known: "English reports."}
  occupations: {value: ["mathematician", "aerospace technologist"], certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S2, locator: "text"}], how_known: "NASA; PC(USA)."}

contribution:
  era_bucket: 20c_late
  fields: {value: ["orbital mechanics", "spaceflight trajectory analysis"], certainty: 0.7, cites: [{source: S1, locator: "para. 3–5"}], how_known: "NASA."}
  lasting_original_contributions:
    - {value: "Equations for placing a satellite over a selected Earth position (report with Ted Skopinski)", year: 1960, kind: "method", lasting: "'equations describing an orbital spaceflight in which the landing position of the spacecraft is specified' (S1); no source calls them lasting; her 'pioneering legacy' (S1)", certainty: 0.5, cites: [{source: S1, locator: "para. 4"}], how_known: "NASA biography."}
    - {value: "Hand verification of John Glenn's orbital trajectory (Friendship 7)", year: 1962, kind: "other", lasting: "'the work that she would become most known for' (S1)", certainty: 0.5, cites: [{source: S1, locator: "para. 5"}, {source: S2, locator: "text"}], how_known: "NASA; PC(USA); fame rather than a stated lasting result."}
  evidence_of_impact:
    - {value: "Presidential Medal of Freedom (2015)", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "para. 6"}], how_known: "NASA."}
  major_works:
    - {value: "Trajectory analysis for Alan Shepard's Freedom 7", year: 1961, kind: "other", certainty: 0.7, cites: [{source: S1, locator: "para. 3"}], how_known: "NASA."}
  honours: []
  definition_fit: {value: "arguable", rationale: "Credited authorship and celebrated verification; no source names a lasting original result (S1, S2).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Methodist (St. James United Methodist Church, White Sulphur Springs); family also attended the Colored Baptist church on alternate Sundays under shared preaching schedule", certainty: 0.7, cites: [{source: S5, locator: "Ch. 1: St. James; Baptist/Methodist alternating Sundays"}], how_known: "Her own autobiography (RFTM)."}
  family_religious_practice: {value: "Sunday worship (family sat second row right); Daddy taught Sunday school and she helped; evening service; combined vacation Bible school with Baptists; Daddy blessed food at Sunday dinner when the preacher visited", certainty: 0.7, cites: [{source: S5, locator: "Ch. 1 church and Sunday dinner"}], how_known: "Her own autobiography (RFTM)."}
  parents_and_household:
    - {value: "Joylette Coleman — mother; former teacher; orderly; cooked, washed, sewed; took in laundry including that of a White Episcopal priest", role: mother, certainty: 0.7, cites: [{source: S5, locator: "Ch. 1: Mama / Joylette"}], how_known: "Her own autobiography (RFTM)."}
    - {value: "Joshua (Josh) Coleman — father; farmer, logger, handyman, Greenbrier bellman; sixth-grade education; taught Sunday school; 'You are no better than anyone else, but nobody else is better than you'", role: father, certainty: 0.7, cites: [{source: S5, locator: "Ch. 1: Daddy / Josh"}, {source: S8, locator: "Obama excerpt: Joshua McKinley Coleman room"}], how_known: "Her own autobiographies."}
  household_circumstances: {value: "Colored Church Street neighborhood, White Sulphur Springs; house Daddy built ('Big House'); earlier Dutch Run farm outside town; segregation's daily rules", certainty: 0.7, cites: [{source: S5, locator: "Ch. 1"}], how_known: "RFTM."}
  schooling:
    - {value: "Mary McLeod Bethune Grade School (Colored), White Sulphur Springs; kindergarten then skipped into second grade; later skipped fifth", stage: "elementary school", run_by: "state or municipal", certainty: 0.7, cites: [{source: S5, locator: "Ch. 1 Bethune school"}], how_known: "RFTM."}
    - {value: "West Virginia State College (B.S. mathematics and French, 1937); first black graduate students at West Virginia University (1939)", certainty: 0.7, cites: [{source: S1, locator: "facts box; para. 1–2"}], how_known: "NASA."}
  early_mathematics: {value: "advanced mathematics", certainty: 0.7, cites: [{source: S5, locator: "Ch. 1 counting / Charlie / grade skips"}, {source: S10, locator: "love for math answer"}], how_known: "RFTM: counted everything, helped brother with math before school, grade-skipped; AARP interview confirms childhood counting."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["English"], certainty: 0.7, cites: [{source: S5, locator: "Ch. 1"}], how_known: "RFTM."}
  notable_events:
    - {value: "Family sat second row at St. James; Daddy taught Sunday school", year: UNKNOWN, certainty: 0.7, cites: [{source: S5, locator: "Ch. 1"}], how_known: "RFTM."}

worldview:
  unit: "adult working worldview"
  working_years: {value: UNKNOWN, how_known: "Equals timing.major_work_period (UNKNOWN, P13)."}
  nominal_affiliations:
    - {value: "Carver Memorial Presbyterian Church (Newport News / Hampton area), member more than 50 years; finance chair; choir; commissioner to the 187th General Assembly (1975, finance committee)", certainty: 0.7, cites: [{source: S2, locator: "text"}, {source: S3, locator: "finance chair; choir"}, {source: S8, locator: "my church members at Carver Memorial Presbyterian"}], how_known: "PC(USA); Blount eulogy; her own MRJ names the congregation."}
    - {value: "Childhood: St. James United Methodist Church, White Sulphur Springs", certainty: 0.7, cites: [{source: S5, locator: "Ch. 1 St. James"}], how_known: "RFTM."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No own statement pairing science and religion read. Blount eulogy speaks of her 'commitment to her faith, amidst her simultaneous faith in her science' (S3) — pastor's framing, not her words. LitHub MRJ excerpt (S9) has family prayer during Jimmie's illness — practice, not a science-religion relation."}
  primary_system:
    value: BELOW_THRESHOLD
    how_known: "Y2 path not met. Own published words name God and 'my faith' and her Presbyterian congregation (S5, S7, S8) and describe lifelong church practice, but no first-person self-label ('I am a Christian' / 'I am a Presbyterian') and no Christ/scripture/creed profession in the autobiographies and interview opened this pass. Blount (S3): 'I know from conversation with her that Katherine believed that Jesus' promise of this new, resurrected life would one day... be extended to her' — reported speech of a private conversation; cannot score CHRIST alone (P18 reported speech; RQ-Y2 / Morrison needed 'I'm a Catholic'). Lead remains CHRIST from practice + God-talk + pastor report. Named path if primary memoir OCR later yields a creed/self-label."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Lead only: Carver Memorial Presbyterian practice and office (S2, S3); childhood Methodist worship in own autobiography (S5); 'my faith' (S7 secondary); Blount's conversation report of Jesus/resurrection belief (S3, reported speech). Not scored: Y2 self-label / Christ-creed profession absent from published own words opened this pass."}
    - {code: DEISM, reason: "Rejected: no P27 rejection of revelation; church practice and petition/prayer in family narrative (S9 LitHub MRJ excerpt: 'We prayed') cut against DEISM."}
  lio_axes:
    A_locus:
      value: 0
      basis: written_profession
      certainty: 0.5
      support: single
      rationale: "Transcendent personal pole. RFTM Ch.1 (S5 publisher excerpt): 'There was only one God, but segregation meant that White people and Colored people couldn't worship Him in the same place. We let God be the judge of that' — one God, personal ('Him'), judge. Named alternative 1: childhood segregation narrative might be cultural/communal God-talk without an adult locus profession. S6 ('God gives us no guarantees that our road will be easy') is secondary quotation of the same autobiography and would corroborate providence language if checked against primary pages; not used to lift support past single (P26/P48). Late memoirs (2019/2021) vs UNKNOWN major_work_period / after 1960–1962 candidates → 0.5."
      cites: [{source: S5, locator: "Ch. 1: only one God / God be the judge"}]
      how_known: "Published autobiography via Simon & Schuster publisher excerpt (unofficial web copy of her own published text). Support single (P48)."
      alternatives:
        - {value: 1, note: "If 'Him'/'judge' in a childhood segregation anecdote is read as communal idiom rather than personal transcendent locus.", cites: [{source: S5, locator: "Ch. 1 God sentence"}]}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (RQ-AA5-1): trajectory computation applies known laws rather than stating a new result about nature. No first-person statement on nature's lawfulness or exceptions read (P16, P19). Silence kept."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read on reward and punishment of persons in her own view (P19). Blount's Jesus/resurrection conversation report is reported speech and not used to score C."}
    D_authority: {value: UNKNOWN, how_known: "Nothing read on scripture vs observation as authority (P19). Ecclesiastes 3:1 appears as a chapter epigraph in MRJ (S7 Bookey) — framing, not a D statement."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7, P19)."}
  mid_basin: {value: UNKNOWN, how_known: "B_cause is UNKNOWN, so the P4 test cannot be applied (P19; UNKNOWN takes precedence). A at 0.5 would in any case sit under the 0.7 bar. Still not plotted."}
  statements:
    - text: "There was only one God, but segregation meant that White people and Colored people couldn't worship Him in the same place. We let God be the judge of that."
      cites: [{source: S5, locator: "Ch. 1: St. Thomas Episcopal / one God paragraph"}]
      date: "2019"
      context: "Reaching for the Moon autobiography, childhood White Sulphur Springs; contrasting segregated churches with one God"
      axes: [A_locus]
      kind: autobiography
      verified_against: unofficial web copy
      verified_on: 2026-10-24
      note: "Publisher excerpt of published autobiography (Simon & Schuster). Scores A 0 @0.5."
    - text: "At some point or other, every single person will have to scale the rough side of life's mountain. God gives us no guarantees that our road will be easy. Over time that difficulty can help you build strength and a sense of purpose. But until then you hurt."
      cites: [{source: S6, locator: "RFTM quotation in sermon footnote [5]"}]
      date: "2019"
      context: "Reaching for the Moon, on grief and segregation's weight (via georgia preach sermon)"
      axes: [A_locus]
      kind: autobiography
      verified_against: secondary quotation
      verified_on: 2026-10-24
      note: "Secondary quotation of RFTM; primary page images not opened this pass (P26). Corroborates personal-God/providence language; not used to lift A support past single."
    - text: "I may not have known exactly what lay ahead, but I knew that my foundation—my faith, my family, and my friends—would remain solid the rest of the way. And that was enough."
      cites: [{source: S7, locator: "Ch. 11 quote"}]
      date: "2021"
      context: "My Remarkable Journey, late-life reflection"
      kind: autobiography
      verified_against: secondary quotation
      verified_on: 2026-10-24
      note: "Bookey quote page of MRJ; primary OCR borrow-walled on Internet Archive this pass. 'My faith' names faith as foundation but is not a CHRIST self-label or creed profession (Y2)."
    - text: "I've also been active in my church and my sorority [Alpha Kappa Alpha]."
      cites: [{source: S10, locator: "How have you stayed active answer"}]
      date: "2018"
      context: "AARP Bulletin interview on post-retirement life"
      kind: recorded interview
      verified_against: newspaper interview
      verified_on: 2026-10-24
      note: "Church activity, not a creed self-label."
    - text: "Jimmie and I slept little the night before his operation but by morning we were calm and resolute. We prayed and drove with his parents just a few minutes away to Riverside Hospital in Newport News."
      cites: [{source: S9, locator: "Jimmie surgery night"}]
      date: "2021"
      context: "My Remarkable Journey, night before Jimmie's brain surgery (1955)"
      kind: autobiography
      verified_against: unofficial web copy
      verified_on: 2026-10-24
      note: "Family petition/prayer practice; not a locus or creed statement. Cuts against DEISM."
    - text: "I will remember her telling me that she didn't mind saying that her life was filled with grace."
      cites: [{source: S3, locator: "eulogy: filled with grace"}]
      date: "2020"
      context: "Pastor Brian Blount funeral eulogy, reporting her words to him"
      kind: reported speech
      verified_against: secondary quotation
      verified_on: 2026-10-24
      note: "Reported speech; cannot score an axis alone. Grace language strengthens CHRIST lead only as context."
  changes_over_life:
    - {value: "Childhood Methodist worship (St. James) → adult decades at Carver Memorial Presbyterian (PCUSA); late memoirs affirm 'my faith' and a personal God without a published creed self-label", certainty: 0.5, cites: [{source: S5, locator: "St. James"}, {source: S2, locator: "Carver Memorial"}, {source: S7, locator: "my faith"}], how_known: "Own autobiographies and PC(USA); stage years undated."}
  coder_notes: "Deepen D1 2026-10-24: A 0 @0.5 from RFTM S5; primary stays BELOW CHRIST lead (Y2 not met — Morrison needed 'I'm a Catholic'; Johnson has God-talk + 'my faith' + church membership without Christ/creed self-label). B/C/D/E/mid unchanged in plot status (B UNKNOWN). IA myremarkablejour0000john borrow/401; RFTM full PDF not opened. Prefer S5 publisher excerpt over sermon paraphrase for the scoring line. Span still UNKNOWN (P13). No fallacy_catalog; figures not refreshed."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "African American (then Colored / Negro); fair-skinned family in segregated West Virginia", certainty: 0.7, cites: [{source: S5, locator: "Ch. 1 Colored / segregation"}, {source: S1, locator: "text"}], how_known: "Own autobiography; NASA."}
  religious_heritage_by_birth: {value: "Methodist (St. James United Methodist; Colored Methodist/Baptist shared Sundays)", certainty: 0.7, cites: [{source: S5, locator: "Ch. 1"}], how_known: "RFTM."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: "Vacation Bible school (combined Methodist/Baptist); Sunday school with Daddy", certainty: 0.5, cites: [{source: S5, locator: "Ch. 1 Bible school / Sunday school"}], how_known: "RFTM practice description; not a formal catechism name."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: UNKNOWN, how_known: "No contribution sourced as lasting (P13, Lamarr precedent); candidates 1960–1962 (S1)."}
  age_at_first_lasting_contribution: {value: UNKNOWN, how_known: "No dated lasting contribution (P13); 42 on the 1960 candidate."}
  first_evidence_of_lio_type_views: {value: "2019", certainty: 0.5, cites: [{source: S5, locator: "Ch. 1 one God"}], how_known: "Earliest dated own published locus language opened this pass (RFTM); childhood scene, late autobiography. No in-span (1960–62 candidate) locus statement found."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "Major work period UNKNOWN; locus evidence is late memoir."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "No in-span worldview profession read."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "Analytic geometry of orbits (S1).", certainty: 0.5, cites: [{source: S1, locator: "para. 4"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data for a Lane B nature claim; RQ-AA5-1 not a scientist."
  notes: "Lane B silence on nature; do not infer B from orbital computation."

institutions:
  - {value: "NACA / NASA Langley Research Center", role: "mathematician (computer); aerospace technologist", years: "1953–1986", kind: "government or state body", certainty: 0.7, cites: [{source: S1, locator: "facts box"}], how_known: "NASA."}
collaborators:
  - {value: "Ted Skopinski", relation: "collaborator", note: "co-author of the 1960 report", certainty: 0.7, cites: [{source: S1, locator: "para. 4"}], how_known: "NASA."}
  - {value: "Dorothy Vaughan", relation: "mentor or employer", note: "head of West Area Computing", certainty: 0.7, cites: [{source: S1, locator: "para. 2"}], how_known: "NASA."}
  - {value: "W. W. Schieffelin Claytor", relation: "mentor or employer", note: "college mathematics mentor", certainty: 0.7, cites: [{source: S1, locator: "para. 1"}], how_known: "NASA."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 197"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Lasting status arguable (P13)."
    - "Primary_system still practice-led BELOW (Y2); A from late autobiography only."
    - "S6/S7 secondary quotations of memoirs; IA borrow wall on MRJ OCR."
  open_questions:
    - "RQ-AA5-1 scientist status; RQ-AA5-2 practice without profession (still open for primary — Y2 not met)."
    - "Optional: primary page check of RFTM 'God gives us no guarantees' and MRJ Ch.11 'my faith' (lift A support; still would not clear Y2 without a self-label)."
    - "Optional: in-span (1960–1962 candidate) faith statement — none found this pass."

sources:
  - id: S1
    type: secondary
    kind: "institutional page"
    author: "Margot Lee Shetterly"
    citation: "Shetterly, Margot Lee. 'Katherine Johnson Biography.' NASA (22 November 2016). https://www.nasa.gov/centers-and-facilities/langley/katherine-johnson-biography/"
    url: "https://www.nasa.gov/centers-and-facilities/langley/katherine-johnson-biography/"
    accessed: 2026-10-19
    source_quality: "other"
    reliability_note: "Signed NASA biography by the author of Hidden Figures, read in full."
    used_for: [identity, basics, contribution, childhood, timing, institutions, collaborators]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "Presbyterian Church (U.S.A.)"
    citation: "'Real-life \"Hidden Figures\" mathematician Katherine G. Johnson is longtime Presbyterian.' PC(USA) News (26 January 2017). https://pcusa.org/news-storytelling/news/2017/1/26/real-life-hidden-figures-mathematician-katherine-g-johnson-longtime"
    url: "https://pcusa.org/news-storytelling/news/2017/1/26/real-life-hidden-figures-mathematician-katherine-g-johnson-longtime"
    accessed: 2026-10-19
    source_quality: "other"
    reliability_note: "Denominational news article, read in full."
    used_for: [identity, contribution, worldview]
  - id: S3
    type: secondary
    kind: "other"
    author: "Brian K. Blount"
    citation: "Blount, Brian K. 'Eulogy for Katherine Goble Johnson.' Delivered 7 March 2020; PDF hosted by Katherine Johnson Foundation. https://www.katherinejohnsonfoundation.org/wp-content/uploads/2022/03/Katherines-Eulogy-2022a.pdf"
    url: "https://www.katherinejohnsonfoundation.org/wp-content/uploads/2022/03/Katherines-Eulogy-2022a.pdf"
    accessed: 2026-10-24
    source_quality: "other"
    reliability_note: "Full eulogy PDF read 2026-10-24 (UPSEM newsroom URL had drifted). Practice detail and conversation reports; reported speech cannot score axes alone."
    used_for: [worldview, identity]
  - id: S4
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    source_quality: "study roster"
    reliability_note: "Study's own roster."
    used_for: [review]
  - id: S5
    type: primary
    kind: "published work by the subject"
    author: "Katherine Johnson"
    citation: "Johnson, Katherine. Reaching for the Moon: The Autobiography of NASA Mathematician Katherine Johnson. Atheneum Books for Young Readers, 2019. Chapter 1 excerpt via Simon & Schuster. https://www.simonandschuster.net/books/Reaching-for-the-Moon/Katherine-Johnson/9781534440845"
    url: "https://www.simonandschuster.net/books/Reaching-for-the-Moon/Katherine-Johnson/9781534440845"
    accessed: 2026-10-24
    source_quality: "unofficial web copy"
    reliability_note: "Publisher excerpt of her published autobiography, read in full on the S&S page. Scores the one-God A line. Full book PDF not opened."
    used_for: [childhood, worldview, heritage, statements]
  - id: S6
    type: secondary
    kind: "other"
    author: "georgia preach (Emory Presbyterian sermon)"
    citation: "'Summer Saints, Part 2: Science and the Heavens (Madeline L'Engle and Katherine Johnson).' georgia preach (20 June 2021). Quotes Reaching for the Moon. https://georgiapreach.wordpress.com/2021/06/20/summer-saints-part-two-science-and-the-heavens/"
    url: "https://georgiapreach.wordpress.com/2021/06/20/summer-saints-part-two-science-and-the-heavens/"
    accessed: 2026-10-24
    source_quality: "other"
    reliability_note: "Secondary quotation of RFTM 'God gives us no guarantees...'; P26 — not used as sole A support."
    used_for: [worldview, statements]
  - id: S7
    type: secondary
    kind: "other"
    author: "Bookey (quote compilation of Johnson, Hylick, Moore)"
    citation: "'Best Quotes Of My Remarkable Journey With Page Numbers By Katherine G. Johnson.' Bookey. https://www.bookey.app/book/my-remarkable-journey/quote"
    url: "https://www.bookey.app/book/my-remarkable-journey/quote"
    accessed: 2026-10-24
    source_quality: "other"
    reliability_note: "Secondary quotation of MRJ Ch.11 'my foundation—my faith...'; primary pages not opened."
    used_for: [worldview, statements]
  - id: S8
    type: primary
    kind: "published work by the subject"
    author: "Katherine Johnson, Joylette Hylick, and Katherine Moore"
    citation: "Johnson, Katherine, with Joylette Hylick and Katherine Moore. My Remarkable Journey: A Memoir. Amistad, 2021. Excerpt: Oprah Daily / Joshunda Sanders (24 May 2021). https://www.oprahdaily.com/entertainment/books/a36178863/katherine-johnson-memoir-my-remarkable-journey-president-obama/"
    url: "https://www.oprahdaily.com/entertainment/books/a36178863/katherine-johnson-memoir-my-remarkable-journey-president-obama/"
    accessed: 2026-10-24
    source_quality: "unofficial web copy"
    reliability_note: "Long excerpt read in full; affiliation and life narrative; no creed self-label in the excerpt."
    used_for: [worldview, childhood, statements]
  - id: S9
    type: primary
    kind: "published work by the subject"
    author: "Katherine Johnson, Joylette Hylick, and Katherine Moore"
    citation: "Johnson et al. My Remarkable Journey. LitHub excerpt on Jimmie's illness (26 May 2021). https://lithub.com/how-a-pioneering-mathematician-held-her-family-together-in-the-wake-of-her-husbans-medical-emergency/"
    url: "https://lithub.com/how-a-pioneering-mathematician-held-her-family-together-in-the-wake-of-her-husbans-medical-emergency/"
    accessed: 2026-10-24
    source_quality: "unofficial web copy"
    reliability_note: "'We prayed' practice detail; not a locus or creed statement."
    used_for: [worldview]
  - id: S10
    type: primary
    kind: "other"
    author: "Katherine Johnson (interviewed by Sue Lindsey)"
    citation: "Lindsey, Sue. 'NASA Pioneer Katherine Johnson Q&A.' AARP Bulletin (19 February 2018). https://www.aarp.org/events-history/katherine-johnson-q-and-a-2018/"
    url: "https://www.aarp.org/events-history/katherine-johnson-q-and-a-2018/"
    accessed: 2026-10-24
    source_quality: "newspaper interview"
    reliability_note: "Own words on church activity, math, work; no creed self-label."
    used_for: [worldview, childhood, statements]
---

## Summary

Katherine Johnson (1918–2020), NASA mathematician [S1]. Deepen D1: A_locus 0 @0.5 (RFTM one-God line); primary_system BELOW_THRESHOLD (CHRIST lead; Y2 not met). B UNKNOWN. Not plotted.

## Life and work

White Sulphur Springs; Langley [S1]. Childhood Methodist (St. James); adult Carver Memorial Presbyterian [S5, S2].

## Contribution and impact

Orbital equations (1960); Glenn verification (1962) [S1]. Lasting status still unsourced (P13).

## Childhood and education

Counted everything; Bethune Grade School; West Virginia State; WVU [S5, S1]. Parents Joshua and Joylette Coleman [S5].

## Adult working worldview

Own autobiographies: personal God and 'my faith' as foundation [S5, S7]; no published Christian self-label. Practice and pastor report keep CHRIST as lead under BELOW_THRESHOLD [S2, S3]. A 0 @0.5; B UNKNOWN (not a scientist).

## Heritage (context only)

African American; Methodist by upbringing [S5].

## Timing

UNKNOWN (P13); candidates 1960–1962 [S1]. Locus evidence late (2019–2021).

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No nature claim.

## Open questions

- RQ-AA5-1; RQ-AA5-2 / Y2 (still open for primary).
- Primary page check of S6/S7 memoir lines.

## Research log

- 2026-10-24: Deepen D1. Opened RFTM Ch.1 (S&S), georgia preach RFTM quote, Bookey MRJ quotes, Oprah/LitHub MRJ excerpts, AARP 2018, Blount eulogy PDF. A UNKNOWN→0 @0.5; primary stays BELOW CHRIST lead; B/mid UNKNOWN. IA MRJ OCR 401/borrow. No fallacy_catalog; figures not touched. Person-file-only commit.
- 2026-10-19: AA5 audit fix (v8's call on the auditor's advice): first-lasting year, span, working years, age and era set to UNKNOWN (P13, Lamarr precedent), with 1960 and 1962 as candidates; church roles not in S2 (choir, church officer, ruling elder) dropped. RQ-AA5-1 and RQ-AA5-2 recorded as coded.
- 2026-10-19: Read NASA (Shetterly); PC(USA) 2017; Blount excerpt.
