---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch V)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #120 / F4 rank 121). Goals: raise A if corroborating own-voice locus; keep B UNKNOWN unless true P16; open Long Walk / letters / Methodist speeches. Opened Long Walk to Freedom ebook PDF (S7; ACT Rwanda repository of Little, Brown 1994/95): 'Though I am a Methodist, I would attend each different religious service' (Robben Island); 'I told them that I was a Christian and had always been a Christian' + Christ/moneylenders (Pollsmoor, Washington Times editors visit, mid-1980s event). Methodist Conference Umtata 18 Sep 1994 (S8, Wayback ANC): 'personal home-coming, both in the physical and spiritual sense'; spiritual association with Methodist Church. Methodist Triennial Durban 17 Jul 1998 (S9): 'my church'; 'God who did not tolerate oppression' framed as what religious organisations taught (after span). Villa-Vicencio, The Spirit of Freedom (S10; interviews 1992/early 1993, in-span): 'person and his or her God'; 'humankind made in the image of God. This is a God who, if I understand the Bible correctly, requires us…'. CHRIST 0.5→0.7 (written_profession; support corroborated). A 1 0.5→0.7 (support corroborated; Moria S5 + Villa-Vicencio S10 locus; LWTF Christ-as-agent). B stays UNKNOWN (ruling V1; Scheffler science-bolsters-religion appeal ≠ P16; struggle 'not a miracle' remains political lead). Mid UNKNOWN. Chart-moving NO. P47 on S1–S10. Wikipedia EN (S11, P50). No fallacy_catalog. No figures/. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Audit fixes for batch V (gs_982cb8e_V run 1): ruling V1 (v8's call on the auditor's advice; RQ-AU1 does not extend to prayers for peace): MA5, B BELOW_THRESHOLD -> UNKNOWN, readings 1 and 3 kept as leads; MA6, mid_basin BELOW_THRESHOLD -> UNKNOWN. Notes: Forster's 'just an ordinary person' labelled a secondary quotation; primary_system how_known gives the P42 reason the speech counts. Still not plotted."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch V, order P32: F 4, rank 121). Basics from Britannica (Britannica Editors), the Nobel Foundation biography and facts page; religion from Dion Forster's 2014 faith biography and his own Easter address at Moria (3 April 1994, SAHO transcript). Not a scientist (P30). primary_system CHRIST at 0.5 (alt BELOW_THRESHOLD); A 1 at 0.5 (alt BELOW_THRESHOLD); B BELOW_THRESHOLD (readings 1 and 3 named); C, D UNKNOWN; E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Span 1964–1994 (0.5). Not plotted. Draft, not reviewed."}

identity:
  id: mandela-nelson
  display_name: "Nelson Mandela"
  roster:
    canonical_name: "Nelson Mandela"
    rank: 121
    F: 4
    models: [DeepSeek, Gemini, GPT, Grok]
    band: "core (3–4)"
    status: core
    field: "political thought"
    field_bucket: "politics / law / military"
  full_name: {value: "Nelson Rolihlahla Mandela", certainty: 0.7, cites: [{source: S1, locator: "facts box (In full)"}, {source: S2, locator: "¶1"}], how_known: "Britannica and the Nobel biography."}
  native_name: {value: "Rolihlahla Mandela", certainty: 0.5, cites: [{source: S4, locator: "'Birth and schooling'"}], how_known: "Forster: born Rolihlahla; 'Nelson' given by his teacher Miss Mdingane."}
  aliases:
    - {name: "Mandela-Nelson", kind: "roster alias"}
    - {name: "Nelson-Mandela", kind: "roster alias"}
    - {name: "Madiba", kind: "other"}

basics:
  birth:
    date: {value: "1918-07-18", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "facts box (Born)"}, {source: S3, locator: "facts (Born)"}], how_known: "Britannica and the Nobel facts page agree."}
    place: {value: "Mvezo", modern_name: "Mvezo, Eastern Cape, South Africa", polity_then: "Union of South Africa", certainty: 1.0, cites: [{source: S1, locator: "facts box (Born)"}, {source: S3, locator: "facts (Born)"}], how_known: "Britannica and the Nobel facts page; S2 says Transkei."}
  death:
    date: {value: "2013-12-05", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "facts box (Died)"}, {source: S3, locator: "facts (Died)"}, {source: S11, locator: "Death"}], how_known: "Britannica, Nobel facts, and Wikipedia EN agree (P50)."}
    place: {value: "Johannesburg", modern_name: "Johannesburg, South Africa", polity_then: "South Africa", certainty: 1.0, cites: [{source: S1, locator: "facts box (Died)"}, {source: S3, locator: "facts (Died)"}], how_known: "Britannica and the Nobel facts page."}
  first_lasting_contribution_year: {value: 1964, certainty: 0.5, cites: [{source: S1, locator: "'Underground activity and the Rivonia Trial'"}], how_known: "The speech from the dock at the Rivonia Trial, published as I Am Prepared to Die (1964): 'a classic defense of liberty and defiance of tyranny' (S1). The Freedom Charter (1955) is excluded: a collective document he was 'involved in drafting' (S1); 1955 is the named alternative start."}
  era_bucket: {value: "1950 on", certainty: 0.5, cites: [{source: S1, locator: "'Underground activity and the Rivonia Trial'"}], how_known: "1964 (P2); 1955 gives the same bucket."}
  region_of_birth: {value: "Sub-Saharan Africa", certainty: 1.0, cites: [{source: S1, locator: "facts box"}, {source: S3, locator: "facts"}], how_known: "South Africa (P3)."}
  region_of_work: {value: "Sub-Saharan Africa", certainty: 0.7, cites: [{source: S1, locator: "'Early life and work'"}], how_known: "South Africa."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "'Early life and work'"}], how_known: "'the son of Chief Henry Mandela' (S1)."}
  languages_of_work: {value: ["English", "isiXhosa"], certainty: 0.5, cites: [{source: S1, locator: "'Early life and work'"}], how_known: "Coder's reading: Xhosa-speaking Tembu family; English writings."}
  occupations: {value: ["lawyer", "ANC leader", "political prisoner", "president of South Africa (1994–1999)"], certainty: 0.7, cites: [{source: S1, locator: "opening; 'Early life and work'"}, {source: S2, locator: "¶1–3"}], how_known: "Britannica and the Nobel biography."}

contribution:
  fields: {value: ["politics", "law", "anti-apartheid movement"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Speech from the dock at the Rivonia Trial (published as I Am Prepared to Die)", year: 1964, kind: work, lasting: "'a classic defense of liberty and defiance of tyranny'; 'garnered international attention and acclaim' (S1)", certainty: 0.5, cites: [{source: S1, locator: "'Underground activity and the Rivonia Trial'"}, {source: S2, locator: "¶2"}], how_known: "Britannica; the Nobel biography notes its 'considerable international publicity'. Year from S1 ('published later that year', the trial ending June 1964). Whether a speech counts as a lasting original contribution is the coder's call (0.5)."}
    - {value: "Negotiated end of apartheid and the peaceful transition to majority rule (with F. W. de Klerk)", year: 1990, kind: other, lasting: "Nobel motivation: 'for laying the foundations for a new democratic South Africa' (S3); 'helped end the country’s apartheid system' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "prize motivation"}, {source: S2, locator: "¶4"}], how_known: "Britannica ('negotiations in the early 1990s'), Nobel facts and biography (release 11 February 1990). Range 1990–1994: start year 1990 (P12); the period ends in 1994 with the first democratic election and his presidency (P30, end of range)."}
  evidence_of_impact:
    - {value: "Nobel Peace Prize 1993 (with F. W. de Klerk)", kind: "honours in lifetime", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "facts"}], how_known: "Britannica and the Nobel site."}
    - {value: "'the world's most famous political prisoner'; 'Africa's Greatest Freedom Symbol'", kind: other, certainty: 0.7, cites: [{source: S3, locator: "summary"}], how_known: "Nobel Foundation."}
  major_works:
    - {value: "Long Walk to Freedom (autobiography)", year: 1994, certainty: 0.7, cites: [{source: S2, locator: "Selected Bibliography"}], how_known: "Nobel bibliography (Little, Brown, 1994)."}
    - {value: "The Struggle Is My Life", year: 1978, certainty: 0.7, cites: [{source: S2, locator: "Selected Bibliography"}], how_known: "Nobel bibliography: first published 1978, revised 1986."}
  honours:
    - {value: "Nobel Peace Prize", year: 1993, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "facts"}], how_known: "Britannica and the Nobel site."}
  definition_fit: {value: "arguable", rationale: "Lasting impact is political leadership of a collective movement; his original written contribution is the Rivonia speech. The Lane A definition excludes collectives, so fit is arguable.", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading; roster status is Jason's."}

childhood:
  family_religion: {value: "Mother Christian (Methodist)", certainty: 0.5, cites: [{source: S4, locator: "'Birth and schooling'"}], how_known: "Forster, citing Long Walk to Freedom p. 11: his mother became a Christian through George and Ben Mbekela. The father's religion is not stated in the sources read (a heritage page seen only in search says he followed Xhosa belief; not used)."}
  family_religious_practice: {value: "Baptised in the Wesleyan (Methodist) church at about 7; regular church attender at Mqhekezweni under Rev. Matyholo; Methodist class-meeting cards 1929–1931", certainty: 0.5, cites: [{source: S4, locator: "'Birth and schooling'"}], how_known: "Forster, from Long Walk to Freedom pp. 18–19 and the Mandela archives."}
  parents_and_household:
    - {value: "Father: Chief Henry (Gadla) Mandela of the Madiba clan of the Tembu; died when Nelson was young", certainty: 0.7, cites: [{source: S1, locator: "'Early life and work'"}, {source: S4, locator: "'Birth and schooling'"}], how_known: "Britannica; Forster gives Mphakanyiswa Gadla Mandela, deposed as chief."}
    - {value: "Mother: Nosekeni (Nogaphi Nosekeni)", certainty: 0.5, cites: [{source: S4, locator: "'Birth and schooling'"}], how_known: "Forster."}
    - {value: "Guardian: Jongintaba (Dalindyebo), regent of the Tembu", certainty: 0.7, cites: [{source: S1, locator: "'Early life and work'"}, {source: S4, locator: "'Birth and schooling'"}], how_known: "Britannica and Forster."}
  household_circumstances: {value: "Chiefly Tembu family; after his father's death raised at the regent's court at Mqhekezweni", certainty: 0.7, cites: [{source: S1, locator: "'Early life and work'"}, {source: S4, locator: "'Birth and schooling'"}], how_known: "Britannica and Forster."}
  schooling:
    - {value: "Wesleyan mission schools at Qunu and Mqhekezweni", stage: "elementary school", run_by: "religious body", certainty: 0.5, cites: [{source: S4, locator: "'Birth and schooling'"}], how_known: "Forster; years not stated."}
    - {value: "Clarkebury Institute, Engcobo (Methodist)", stage: "grammar or secondary school", run_by: "religious body", years: "from 1935", certainty: 0.5, cites: [{source: S4, locator: "'Birth and schooling'"}], how_known: "Forster."}
    - {value: "Healdtown, Fort Beaufort (Methodist)", stage: "grammar or secondary school", run_by: "religious body", years: "from 1937", certainty: 0.5, cites: [{source: S4, locator: "'Birth and schooling'"}], how_known: "Forster."}
    - {value: "South African Native College (University of Fort Hare); expelled 1940", stage: university, run_by: other, years: "1939–1940", certainty: 0.5, cites: [{source: S1, locator: "'Early life and work'"}, {source: S4, locator: "'Birth and schooling'"}], how_known: "Britannica and Forster; operator not stated."}
    - {value: "University of the Witwatersrand (law)", stage: university, run_by: other, certainty: 0.7, cites: [{source: S1, locator: "'Early life and work'"}, {source: S2, locator: "¶1"}], how_known: "Britannica and the Nobel biography; years not stated."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "Rev. Matyholo, Wesleyan minister at Mqhekezweni", certainty: 0.5, cites: [{source: S4, locator: "'Birth and schooling'"}], how_known: "Forster, quoting Long Walk to Freedom."}
    - {value: "Rev. Seth Mokitimi, boarding master at Healdtown", certainty: 0.5, cites: [{source: S4, locator: "'Birth and schooling'"}], how_known: "Forster."}
  languages_in_childhood: {value: ["isiXhosa"], certainty: 0.5, cites: [{source: S1, locator: "'Early life and work'"}], how_known: "Coder's reading of 'Xhosa-speaking Tembu people'."}
  notable_events:
    - {value: "Member of the Students Christian Association and Sunday school teacher at Fort Hare", certainty: 0.5, cites: [{source: S4, locator: "'Birth and schooling'"}], how_known: "Forster, citing his 1977 letter to his daughter Maki ('At Fort Hare I even became a Sunday School teacher')."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1964–1994", certainty: 0.5, cites: [{source: S1, locator: "opening; 'Underground activity and the Rivonia Trial'"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Methodist Church of Southern Africa: self-described member throughout life; communion from Methodist chaplains on Robben Island; membership recorded at Mqhekezweni circuit (1998)", certainty: 0.5, cites: [{source: S4, locator: "'Imprisonment'; 'Release and president'; 'Why the claims...'"}], how_known: "Forster's faith biography, from documents and interviews with Storey, Gribble and Dandala."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing read."}
  primary_system:
    value: CHRIST
    basis: written_profession
    certainty: 0.7
    cites: [{source: S7, locator: "Pollsmoor visitors / Washington Times editors"}, {source: S7, locator: "Robben Island Sunday services"}, {source: S5, locator: "Easter section ('Each easter marks...'); opening"}, {source: S8, locator: "opening / spiritual home-coming"}, {source: S4, locator: "'Why the claims...'; 'African Christian humanism'"}]
    how_known: "Deepen D1: Long Walk to Freedom (S7, written profession, published 1994 at end of span) — 'I told them that I was a Christian and had always been a Christian' (recounting mid-1980s Pollsmoor interview, in-span event); 'Though I am a Methodist, I would attend each different religious service' (Robben Island). Corroborated by Moria Easter 1994 resurrection confession (S5, P42 speech); Methodist Conference Umtata 18 Sep 1994 'personal home-coming, both in the physical and spiritual sense' (S8, in-span). Forster: lifelong Methodist self-regard (S4). Distinct source ids → corroborated (P48)."
    rationale: "CHRIST at 0.7 with BELOW_THRESHOLD as named alternative. For: explicit own-voice Christian and Methodist self-IDs in the autobiography covering in-span years, plus in-span Methodist homecoming and Easter confession. Against: Forster's African-Christian-humanism reading and secondary 'ordinary person… mysteries of life' quotation (S4); collaborative autobiography (Stengel) and public/political speech occasions. Contested enough to stop at 0.7, not 1.0."
    alternatives:
      - {value: BELOW_THRESHOLD, note: "Humanism over theology (S4); public piety / collaborative memoir caveats.", cites: [{source: S4, locator: "'African Christian humanism'"}]}
  secondary_system: {value: UNKNOWN, how_known: "One system (P29). Forster's 'African Christian humanism' is a scholar's label, not a code."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Coded at 0.7: LWTF Christian/Methodist self-IDs (S7); Moria Easter (S5); Methodist 1994 homecoming (S8); Forster membership (S4)."}
    - {code: SECHUM, reason: "Rejected: Forster's 'humanism' is Christian humanism, not the secular movement (S4)."}
    - {code: ISLAM, reason: "Rejected: studied Islam on Robben Island (S4, citing Sampson); no adherence."}
  lio_axes:
    A_locus:
      value: 1
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S5, locator: "opening; Easter section; closing"}, {source: S10, locator: "Religion section (image of God / God who requires)"}, {source: S7, locator: "Pollsmoor / Washington Times: Christ and the moneylenders"}, {source: S4, locator: "'African Christian humanism'"}]
      rationale: "Transcendent personal God (pole 1). Moria 1994 (S5): 'the Almighty'; risen Christ / Messiah 'came to us in the form of a mortal man'. Villa-Vicencio interview 1992/early 1993 (S10, in-span): 'the relationship between a person and his or her God'; 'humankind made in the image of God. This is a God who, if I understand the Bible correctly, requires us to be engaged in the actual fight against evil…'. LWTF (S7): affirms Christ as real agent who 'used force to expel the moneylenders'. Leans interventionist without a full doctrine of God → 1. Named alternative BELOW_THRESHOLD (liturgical / political God-talk)."
      how_known: "Deepen D1: two independent in-span own-voice locus sources (S5 written profession; S10 recorded interview) plus LWTF Christ-as-agent. Distinct source ids → corroborated (P48). Contested (campaign speech + interview-book framing), so 0.7 not 1.0."
      alternatives:
        - {value: BELOW_THRESHOLD, note: "Liturgical / campaign God-talk; humanism reading (S4).", cites: [{source: S4, locator: "'African Christian humanism'"}]}
    B_cause: {value: UNKNOWN, how_known: "Deepen D1: not a scientist (P30); no own-voice P16 nature-order claim found. Ruling V1 stands: peace prayers ≠ B. Checked and off-point: (1) Moria 'not a miracle' / struggle outcome (S5) — politics, not nature; (2) LWTF Scheffler 'enlisted science to bolster his beliefs' — Mandela found the approach appealing, not a profession that nature is lawful; (3) Villa-Vicencio peace/religion remarks (S10) — morals and struggle, not physical order. Leads unchanged. Coder's call: UNKNOWN."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing on reward and punishment of persons in his own view read (P19); 'attained immortality' is said of the Messiah."}
    D_authority: {value: UNKNOWN, how_known: "Nothing on revelation against observation read (P19)."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Scored on the world's order (P7). Lead only: prayers for blessings on South Africa; 'the Good News ... who chose all of humankind' is about salvation's scope (C, not E)."}
  mid_basin: {value: UNKNOWN, how_known: "P4/P19: B is UNKNOWN, which takes precedence (ruling V1). A 1 at 0.7 after deepen; still not plotted."}
  statements:
    - text: "We bow our heads in worship on this day and give thanks to the Almighty for the bounty he has bestowed upon us over the past year. We raise our voices in holy gladness to celebrate the victory of the risen Christ over the terrible forces of death."
      cites: [{source: S5, locator: "opening, after the greetings"}]
      date: "1994-04-03"
      context: "Address to the Zionist Christian Church Easter Conference, Moria, three weeks before the first democratic election; he brings 'the heartfelt greetings of the entire membership of the ANC'."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "SAHO transcript (also held by the Nelson Mandela Foundation archive, item ZA COM MR-S-171, seen in search, not read). A prepared address delivered in person; drafting help not known."
    - text: "The coming of the democratic elections to this country is not a miracle. It is the outcome of decades of consistent and unrelenting struggle by millions of ordinary South Africans"
      cites: [{source: S5, locator: "section on South Africa's past"}]
      date: "1994-04-03"
      context: "Same address, on the history of the struggle."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
    - text: "Each easter marks the rebirth of our faith. It marks the victory of our risen saviour over the torture of the cross and the grave. Our Messiah, who came to us in the form of a mortal man, but who by his suffering and crucifixion attained immortality."
      cites: [{source: S5, locator: "Easter section"}]
      date: "1994-04-03"
      context: "Same address; leads into the Messiah's life as testimony against oppression."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
    - text: "Though I am a Methodist, I would attend each different religious service."
      cites: [{source: S7, locator: "Robben Island Sunday services"}]
      date: "1994"
      context: "Long Walk to Freedom, recounting Robben Island years (in-span). Ebook PDF pagination (calibre) ~p.472 of this file; print Little Brown page not marked in the ebook."
      axes: [A_locus]
      kind: "autobiography"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Adult working-years self-identification as Methodist; not itself a locus claim, but anchors CHRIST."
    - text: "I told them that I was a Christian and had always been a Christian. Even Christ, I said, when he was left with no alternative, used force to expel the moneylenders from the temple. He was not a man of violence, but had no choice but to use force against evil."
      cites: [{source: S7, locator: "Pollsmoor visitors / Washington Times editors"}]
      date: "1994"
      context: "Long Walk to Freedom, recounting a mid-1980s Pollsmoor visit by Washington Times editors (in-span event). Ebook ~p.545 of this file."
      axes: [A_locus]
      kind: "autobiography"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Explicit CHRIST self-ID; treats Christ as real historical/agent figure (supports A1). Collaborative autobiography (Stengel) flagged in data_quality_flags."
    - text: "My joy at being in this conference is multiplied many-fold by the fact that this is for me also a personal home-coming, both in the physical and spiritual sense. The environs of Umtata are not only my humble origins. It is here that my spiritual association with this great Church started. And I cannot over-emphasise the role that the Methodist Church has played in my own life."
      cites: [{source: S8, locator: "opening after greetings"}]
      date: "1994-09-18"
      context: "Address to Annual Conference of the Methodist Church, Umtata; inside the span (end)."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Membership/formation claim; little locus content. P42 speech."
    - text: "The relationship between a person and his or her God is a deeply intimate and private matter. … Yes, I certainly recognise the importance of the religious dimension of my own life. … Religion is about mutual love and respect for one another and for life itself. It is about the dignity and equality of humankind made in the image of God. This is a God who, if I understand the Bible correctly, requires us to be engaged in the actual fight against evil, poverty, disease, illiteracy, the lack of housing and other social ills in society."
      cites: [{source: S10, locator: "Religion section"}]
      date: "1992"
      context: "Interview with Charles Villa-Vicencio for The Spirit of Freedom (book 1996). Book preface: interviewees spoken with in 1992 or early 1993 — inside the span. Ellipses mark interviewer turns / bridging narration dropped; wording inside continuous answers as printed."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Strongest A locus corroboration this pass: personal God; image of God; God who requires engagement. Interview-book format (quoted speech woven with narration)."
  changes_over_life:
    - {value: "Regular churchgoer and Sunday school teacher to about 1958; little church practice while underground (1958–1963, none found by Forster); communion in prison; formal Methodist ties again from 1994", certainty: 0.5, cites: [{source: S4, locator: "'Young adulthood...'; 'Imprisonment'; 'Release and president'"}], how_known: "Forster."}
  coder_notes: "Deepen D1 2026-10-24: CHRIST @0.7 (LWTF + Methodist 1994 + Moria); A 1 @0.7 corroborated (Moria + Villa-Vicencio + LWTF Christ); B UNKNOWN (ruling V1; no P16). Long Walk ebook opened; Methodist 1994/1998 opened; Villa-Vicencio 1992/93 interview opened. Chart-moving NO. Not plotted. Span unchanged 1964–1994."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Xhosa-speaking Tembu, Madiba clan", certainty: 0.7, cites: [{source: S1, locator: "'Early life and work'"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Methodist (mother) and Xhosa tradition", certainty: 0.5, cites: [{source: S4, locator: "'Birth and schooling'"}], how_known: "Forster."}
  baptism_or_initiation: {value: "Baptised in the Wesleyan (Methodist) church at about 7", certainty: 0.5, cites: [{source: S4, locator: "'Birth and schooling'"}], how_known: "Forster, from Long Walk to Freedom."}
  childhood_catechism: {value: "Methodist class meetings (cards 1929–1931)", certainty: 0.5, cites: [{source: S4, locator: "'Birth and schooling'"}], how_known: "Forster."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1964–1994", certainty: 0.5, cites: [{source: S1, locator: "opening; 'Underground activity and the Rivonia Trial'"}, {source: S3, locator: "prize motivation"}], how_known: "From the Rivonia speech (1964) to the end of the transition (1994) (P12, P30). Coder's call; alternative start 1955."}
  age_at_first_lasting_contribution: {value: 46, certainty: 0.5, cites: [{source: S1, locator: "facts box; 'Underground activity and the Rivonia Trial'"}], how_known: "1964 − 1918 = 46 (P30); 37 under the 1955 alternative."}
  first_evidence_of_lio_type_views: {value: "1992", certainty: 0.5, cites: [{source: S10, locator: "Religion section"}, {source: S5, locator: "opening"}], how_known: "Earliest in-span scored A locus in own voice this pass: Villa-Vicencio interview (1992/early 1993). Moria Easter 3 Apr 1994 also in-span. Certainty 0.5 (interview-book date band)."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.5, cites: [{source: S5, locator: "whole"}, {source: S10, locator: "Religion section"}, {source: S7, locator: "Pollsmoor / Washington Times"}], how_known: "A 1 @0.7 from in-span own voice (Moria 1994; Villa-Vicencio 1992/93; LWTF recounting 1980s). B UNKNOWN → not plotted."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Not assessed."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Not assessed."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  reading: "Law and negotiation in the service of liberation."
  notes: ""

institutions:
  - {value: "African National Congress", role: "member from 1944; Youth League leader; president from 1991", years: "1944–", kind: other, certainty: 0.7, cites: [{source: S1, locator: "'Early life and work'"}, {source: S2, locator: "¶1; ¶4"}], how_known: "Britannica (1944) and the Nobel biography (1944; president 1991)."}
  - {value: "Mandela and Tambo law practice, Johannesburg", role: "partner (South Africa's first Black law practice)", years: "from 1952", kind: commercial, certainty: 0.7, cites: [{source: S1, locator: "'Early life and work'"}], how_known: "Britannica."}
  - {value: "Umkhonto we Sizwe", role: "co-founder", years: "1961", kind: other, certainty: 0.7, cites: [{source: S1, locator: "'Underground activity and the Rivonia Trial'"}, {source: S2, locator: "¶2"}], how_known: "Britannica and the Nobel biography."}
  - {value: "Government of South Africa", role: "president", years: "1994–1999", kind: "government or state body", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
collaborators:
  - {value: "Oliver Tambo", relation: collaborator, note: "law partner and ANC colleague; 'lifelong friend' (S2)", certainty: 0.7, cites: [{source: S1, locator: "'Early life and work'"}, {source: S2, locator: "¶4"}], how_known: "Britannica and the Nobel biography."}
  - {value: "F. W. de Klerk", relation: other, note: "negotiating counterpart; shared the 1993 Nobel Peace Prize", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "summary"}], how_known: "Britannica and the Nobel site."}
  - {value: "Jongintaba Dalindyebo", relation: family, note: "regent of the Tembu; guardian", certainty: 0.7, cites: [{source: S1, locator: "'Early life and work'"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S6, locator: "roster.csv, rank 121"}], how_known: "Study roster; definition fit arguable (collective movement), a matter for Jason."}
  controversies:
    - {value: "Abandoned nonviolence after Sharpeville and co-founded the ANC's armed wing", certainty: 0.7, cites: [{source: S1, locator: "'Underground activity and the Rivonia Trial'"}], how_known: "Britannica."}
  data_quality_flags:
    - "Long Walk to Freedom is a collaborative autobiography (Richard Stengel); Mandela attributed as author; P42/P43 noted."
    - "Villa-Vicencio interview book weaves quoted speech with narration; date band 1992/early 1993 from book preface."
    - "Definition fit 'arguable' (leader of a collective movement)."
    - "Span is a coder's call with a named alternative start (1955)."
  open_questions:
    - "Print Little, Brown page numbers for the Robben Island / Pollsmoor faith passages (ebook lacks print pagination)."
    - "Archival prison letters with theological locus (Prison Letters volume skimmed in search only)."
    - "Any explicit P16 nature-order remark (low prior; not a scientist)."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "Britannica Editors. \"Nelson Mandela.\" Encyclopaedia Britannica (updated 14 October 2026). https://www.britannica.com/biography/Nelson-Mandela. Read live 2026-10-19."
    url: "https://www.britannica.com/biography/Nelson-Mandela"
    accessed: 2026-10-19
    reliability_note: "Unsigned editors' article; facts box and body cited; 'Top Questions' boxes not cited (P26)."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, heritage, timing, institutions, collaborators, review]
  - id: S2
    type: tertiary
    kind: institutional page
    author: "Nobel Foundation"
    citation: "\"Nelson Mandela – Biographical.\" NobelPrize.org, from Les Prix Nobel 1993, ed. Tore Frängsmyr (Stockholm, 1994). https://www.nobelprize.org/prizes/peace/1993/mandela/biographical/"
    url: "https://www.nobelprize.org/prizes/peace/1993/mandela/biographical/"
    accessed: 2026-10-19
    reliability_note: "Biography written at the time of the award; paragraphs cited."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, institutions, collaborators]
  - id: S3
    type: tertiary
    kind: institutional page
    author: "Nobel Foundation"
    citation: "\"Nelson Mandela – Facts.\" NobelPrize.org. https://www.nobelprize.org/prizes/peace/1993/mandela/facts/"
    url: "https://www.nobelprize.org/prizes/peace/1993/mandela/facts/"
    accessed: 2026-10-19
    reliability_note: "Official facts page with the prize motivation."
    source_quality: "reference entry"
    used_for: [basics, contribution, timing, collaborators]
  - id: S4
    type: secondary
    kind: "journal article"
    author: "Dion Forster"
    citation: "Forster, Dion. \"Mandela and the Methodists: Faith, fallacy and fact.\" Studia Historiae Ecclesiasticae 40, no. 2 (2014). https://www.scielo.org.za/scielo.php?pid=S1017-04992014000200007&script=sci_arttext"
    url: "https://www.scielo.org.za/scielo.php?pid=S1017-04992014000200007&script=sci_arttext"
    accessed: 2026-10-19
    reliability_note: "Peer-reviewed faith biography (Stellenbosch), from documents and interviews; cites Long Walk to Freedom by page. Locators by section heading."
    source_quality: "other"
    used_for: [identity, childhood, heritage, worldview]
  - id: S5
    type: primary
    kind: "published work by the subject"
    author: "Nelson Mandela"
    citation: "Mandela, Nelson. \"Speech by Nelson Mandela at Zionist Christian Church Easter Conference, Moria, 3 April 1994.\" South African History Online. https://www.sahistory.org.za/archive/speech-nelson-mandela-zionist-christian-church-easter-conference-moria-3-april-1994"
    url: "https://www.sahistory.org.za/archive/speech-nelson-mandela-zionist-christian-church-easter-conference-moria-3-april-1994"
    accessed: 2026-10-19
    reliability_note: "Transcript of the delivered address; the same text is on the South African government's Mandela speeches site and in the Nelson Mandela Foundation archive. Locators by section."
    source_quality: "unofficial web copy"
    used_for: [worldview]
  - id: S6
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S7
    type: primary
    kind: "published work by the subject"
    author: "Nelson Mandela"
    citation: "Mandela, Nelson. Long Walk to Freedom: The Autobiography of Nelson Mandela. Boston: Little, Brown, 1994/1995. Ebook PDF (calibre) read 2026-10-24 via African Centre of Excellence in Data Science repository, https://repository.act.ac.rw/server/api/core/bitstreams/1781d4c1-64c6-4fa2-87e7-b693e01b24d4/content. Locators by episode (ebook lacks Little Brown print page numbers)."
    url: "https://repository.act.ac.rw/server/api/core/bitstreams/1781d4c1-64c6-4fa2-87e7-b693e01b24d4/content"
    accessed: 2026-10-24
    reliability_note: "Autobiography attributed to Mandela; collaborative with Richard Stengel (P42/P43 noted). Primary for self-IDs and recounted in-span speech. Print pagination not available in this ebook."
    source_quality: "primary / own words"
    used_for: [worldview, childhood, review]
  - id: S8
    type: primary
    kind: "published work by the subject"
    author: "Nelson Mandela"
    citation: "Mandela, Nelson. \"Address to the Annual Conference of the Methodist Church,\" Umtata, 18 September 1994. ANC historical documents (Wayback): https://web.archive.org/web/20060519000000/http://www.anc.org.za/ancdocs/history/mandela/1994/sp940918.html. Also NMF ZA COM MR-S-201. Read 2026-10-24."
    url: "https://web.archive.org/web/20060519000000/http://www.anc.org.za/ancdocs/history/mandela/1994/sp940918.html"
    accessed: 2026-10-24
    reliability_note: "Official ANC transcript of delivered presidential address; inside the span (end). P42 speech."
    source_quality: "unofficial web copy"
    used_for: [worldview]
  - id: S9
    type: primary
    kind: "published work by the subject"
    author: "Nelson Mandela"
    citation: "Mandela, Nelson. \"Address at the first Triennial Conference of the Methodist Church of South Africa,\" Durban, 17 July 1998. South African History Online. https://sahistory.org.za/archive/address-president-nelson-mandela-first-triennial-conference-methodist-church-south-africa. Also NMF ZA COM MR-S-603. Read 2026-10-24."
    url: "https://sahistory.org.za/archive/address-president-nelson-mandela-first-triennial-conference-methodist-church-south-africa"
    accessed: 2026-10-24
    reliability_note: "After the span (1998; P1 if scored for certainty). Used for 'my church' membership corroboration and the reported 'God who… stood with the oppressed' line (framed as what churches taught)."
    source_quality: "unofficial web copy"
    used_for: [worldview, review]
  - id: S10
    type: primary
    kind: "published work by the subject"
    author: "Nelson Mandela; interviewed by Charles Villa-Vicencio"
    citation: "Villa-Vicencio, Charles. The Spirit of Freedom: South African Leaders on Religion and Politics. Berkeley: University of California Press, 1996. Mandela chapter, Religion section. UC Press E-Books: https://publishing.cdlib.org/ucpressebooks/view?chunk.id=d0e3720&doc.view=print&docId=ft4p3006kc. Interviews dated by the book to 1992 or early 1993. Read 2026-10-24."
    url: "https://publishing.cdlib.org/ucpressebooks/view?chunk.id=d0e3720&doc.view=print&docId=ft4p3006kc"
    accessed: 2026-10-24
    reliability_note: "Published interview book; Mandela's answers appear in quotation. In-span (1992/early 1993). Kind = published work by the subject; source_quality nearest newspaper interview for Q&A."
    source_quality: "newspaper interview"
    used_for: [worldview]
  - id: S11
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia. \"Nelson Mandela.\" English Wikipedia. https://en.wikipedia.org/wiki/Nelson_Mandela. Birth/death and Methodist categories read 2026-10-24."
    url: "https://en.wikipedia.org/wiki/Nelson_Mandela"
    accessed: 2026-10-24
    reliability_note: "Crowdsourced; dual bio (P50) against Britannica/Nobel for birth and death. Religious affiliation categories cite Forster."
    source_quality: "reference entry"
    used_for: [basics, heritage, review]

---

# Nelson Mandela

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Nelson Mandela (1918–2013), anti-apartheid leader and first Black president of South Africa [S1; S11]. Deepen D1: primary_system CHRIST at 0.7; A 1 at 0.7 (corroborated); B UNKNOWN (ruling V1); mid_basin UNKNOWN. Chart-moving NO. Not plotted.

## Life and work

ANC from 1944; law practice with Tambo 1952; Rivonia Trial and life sentence 1964; Robben Island 1964–82; released 1990; president 1994–99 [S1, S2].

## Contribution and impact

The Rivonia speech (1964); the negotiated end of apartheid (1990–1994); Nobel Peace Prize 1993 [S1, S3].

## Childhood and education

Tembu chiefly family; baptised Methodist; Clarkebury, Healdtown, Fort Hare [S1, S4].

## Adult working worldview

"I was a Christian and had always been a Christian" / "Though I am a Methodist" (LWTF) [S7]; Moria Easter 1994 [S5]; Methodist homecoming 1994 [S8]; Villa-Vicencio personal God / image of God [S10]. CHRIST @0.7; A 1 @0.7.

## Heritage (context only)

Methodist and Xhosa [S4].

## Timing

1964–1994, from age 46 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Not assessed.

## Open questions

- Print LWTF page numbers; archival prison letters with locus; any P16 (low prior).

## Research log

- 2026-10-19: Read Britannica, the Nobel biography and facts, Forster (2014) and the Moria address.
- 2026-10-24: Deepen D1. Long Walk ebook [S7]; Methodist 1994 [S8] and 1998 [S9]; Villa-Vicencio Spirit of Freedom [S10]; Wikipedia EN [S11]. CHRIST 0.5→0.7; A 1 0.5→0.7; B UNKNOWN. Chart-moving NO.
