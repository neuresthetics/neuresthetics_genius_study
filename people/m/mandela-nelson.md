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
    date: {value: "2013-12-05", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "facts box (Died)"}, {source: S3, locator: "facts (Died)"}], how_known: "Britannica and the Nobel facts page."}
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
    certainty: 0.5
    cites: [{source: S5, locator: "Easter section ('Each easter marks...'); opening"}, {source: S4, locator: "'Why the claims...'; 'African Christian humanism'"}]
    how_known: "His own public Easter address (1994, inside the span). Under P42 a speech he gave in person, attributed to him by SAHO and the Nelson Mandela Foundation archive, counts as his own words; no source read names a speechwriter. 'Each easter marks the rebirth of our faith. It marks the victory of our risen saviour over the torture of the cross and the grave.' Forster: 'Mr Mandela regarded himself as a member of that denomination throughout his life' (S4)."
    rationale: "CHRIST at 0.5 with BELOW_THRESHOLD as the named alternative. For: first-person-plural confession of the resurrection in his own address; lifelong self-identification as a Methodist (S4). Against: the address was a campaign speech three weeks before the 1994 election, given on behalf of the ANC to a church audience; Forster finds him 'much more strongly influenced by a form of African humanism than Christian theology' and quotes him as 'just an ordinary person trying to make sense of the mysteries of life' (S4; a secondary quotation: Forster quoting Cracknell and White quoting Mandela, so context only). Contested, so at most 0.7; occasion-bound, so 0.5."
    alternatives:
      - {value: BELOW_THRESHOLD, note: "Occasion-bound public piety; humanism over theology (S4).", cites: [{source: S4, locator: "'African Christian humanism'"}]}
  secondary_system: {value: UNKNOWN, how_known: "One system (P29). Forster's 'African Christian humanism' is a scholar's label, not a code."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Coded at 0.5: own Easter address; Methodist self-identification (S4, S5)."}
    - {code: SECHUM, reason: "Rejected: Forster's 'humanism' is Christian humanism, not the secular movement (S4)."}
    - {code: ISLAM, reason: "Rejected: studied Islam on Robben Island (S4, citing Sampson); no adherence."}
  lio_axes:
    A_locus:
      value: 1
      basis: written_profession
      certainty: 0.5
      cites: [{source: S5, locator: "opening; Easter section; closing"}]
      rationale: "Transcendent personal God: 'give thanks to the Almighty for the bounty he has bestowed upon us'; 'May the Lord Almighty grant Your Grace the wisdom'; a Messiah who 'came to us in the form of a mortal man'. Leans to the interventionist pole without a stated doctrine of God, so 1. Named alternative BELOW_THRESHOLD: liturgical and campaign language (as for primary_system)."
      how_known: "One public address, occasion-bound; 0.5."
      alternatives:
        - {value: BELOW_THRESHOLD, note: "Liturgical language at a campaign event.", cites: [{source: S4, locator: "'African Christian humanism'"}]}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30); no statement on nature (P16). Ruling V1 (v8's call on the auditor's advice, batch V audit at 982cb8e): the RQ-AU1 addendum covers only a person's own prayer for physical protection or healing; a public petition for peace ('We pray with you so that the blessings of peace may descend upon South Africa like a torrent!') is neither and says nothing about nature, so B is UNKNOWN. Leads kept: reading 1 (the communal petitions) and reading 3 ('The coming of the democratic elections to this country is not a miracle. It is the outcome of decades of consistent and unrelenting struggle', a human-causation remark about politics, not a statement about nature)."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing on reward and punishment of persons in his own view read (P19); 'attained immortality' is said of the Messiah."}
    D_authority: {value: UNKNOWN, how_known: "Nothing on revelation against observation read (P19)."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Scored on the world's order (P7). Lead only: prayers for blessings on South Africa; 'the Good News ... who chose all of humankind' is about salvation's scope (C, not E)."}
  mid_basin: {value: UNKNOWN, how_known: "P4/P19: B is UNKNOWN, which takes precedence (batch V audit fix MA6, after ruling V1). A 1 at 0.5."}
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
  changes_over_life:
    - {value: "Regular churchgoer and Sunday school teacher to about 1958; little church practice while underground (1958–1963, none found by Forster); communion in prison; formal Methodist ties again from 1994", certainty: 0.5, cites: [{source: S4, locator: "'Young adulthood...'; 'Imprisonment'; 'Release and president'"}], how_known: "Forster."}
  coder_notes: "Coder's call on the span: 1964 (Rivonia speech) to 1994 (end of the 1990–1994 transition). Alternative start 1955 (Freedom Charter, excluded as collective). The religion code rests on one campaign address plus a scholar's faith biography; Long Walk to Freedom was read only through Forster's quotations. Not a scientist (P30). Leads: his 1994 and 1998 addresses to the Methodist Conference (SAHO); Long Walk to Freedom chs. on Robben Island. Not plotted."

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
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No statement scored at 3 or 4."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S5, locator: "whole"}], how_known: "None scored."}
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
    - "primary_system and A rest on one campaign address to a church audience plus Forster's faith biography."
    - "Definition fit 'arguable' (leader of a collective movement)."
    - "Span is a coder's call with a named alternative start."
  open_questions:
    - "1994 and 1998 addresses to the Methodist Conference; Long Walk to Freedom on faith in prison."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "Britannica Editors. \"Nelson Mandela.\" Encyclopaedia Britannica (updated 14 October 2026). https://www.britannica.com/biography/Nelson-Mandela. Read live 2026-10-19."
    url: "https://www.britannica.com/biography/Nelson-Mandela"
    accessed: 2026-10-19
    reliability_note: "Unsigned editors' article; facts box and body cited; 'Top Questions' boxes not cited (P26)."
    used_for: [identity, basics, contribution, childhood, heritage, timing, institutions, collaborators, review]
  - id: S2
    type: tertiary
    kind: institutional page
    author: "Nobel Foundation"
    citation: "\"Nelson Mandela – Biographical.\" NobelPrize.org, from Les Prix Nobel 1993, ed. Tore Frängsmyr (Stockholm, 1994). https://www.nobelprize.org/prizes/peace/1993/mandela/biographical/"
    url: "https://www.nobelprize.org/prizes/peace/1993/mandela/biographical/"
    accessed: 2026-10-19
    reliability_note: "Biography written at the time of the award; paragraphs cited."
    used_for: [identity, basics, contribution, childhood, institutions, collaborators]
  - id: S3
    type: tertiary
    kind: institutional page
    author: "Nobel Foundation"
    citation: "\"Nelson Mandela – Facts.\" NobelPrize.org. https://www.nobelprize.org/prizes/peace/1993/mandela/facts/"
    url: "https://www.nobelprize.org/prizes/peace/1993/mandela/facts/"
    accessed: 2026-10-19
    reliability_note: "Official facts page with the prize motivation."
    used_for: [basics, contribution, timing, collaborators]
  - id: S4
    type: secondary
    kind: "journal article"
    author: "Dion Forster"
    citation: "Forster, Dion. \"Mandela and the Methodists: Faith, fallacy and fact.\" Studia Historiae Ecclesiasticae 40, no. 2 (2014). https://www.scielo.org.za/scielo.php?pid=S1017-04992014000200007&script=sci_arttext"
    url: "https://www.scielo.org.za/scielo.php?pid=S1017-04992014000200007&script=sci_arttext"
    accessed: 2026-10-19
    reliability_note: "Peer-reviewed faith biography (Stellenbosch), from documents and interviews; cites Long Walk to Freedom by page. Locators by section heading."
    used_for: [identity, childhood, heritage, worldview]
  - id: S5
    type: primary
    kind: "published work by the subject"
    author: "Nelson Mandela"
    citation: "Mandela, Nelson. \"Speech by Nelson Mandela at Zionist Christian Church Easter Conference, Moria, 3 April 1994.\" South African History Online. https://www.sahistory.org.za/archive/speech-nelson-mandela-zionist-christian-church-easter-conference-moria-3-april-1994"
    url: "https://www.sahistory.org.za/archive/speech-nelson-mandela-zionist-christian-church-easter-conference-moria-3-april-1994"
    accessed: 2026-10-19
    reliability_note: "Transcript of the delivered address; the same text is on the South African government's Mandela speeches site and in the Nelson Mandela Foundation archive. Locators by section."
    used_for: [worldview]
  - id: S6
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Nelson Mandela

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Nelson Mandela (1918–2013), anti-apartheid leader and first Black president of South Africa [S1]. Draft: primary_system CHRIST at 0.5; A 1 at 0.5; B UNKNOWN (ruling V1); mid_basin UNKNOWN. Not plotted.

## Life and work

ANC from 1944; law practice with Tambo 1952; Rivonia Trial and life sentence 1964; Robben Island 1964–82; released 1990; president 1994–99 [S1, S2].

## Contribution and impact

The Rivonia speech (1964); the negotiated end of apartheid (1990–1994); Nobel Peace Prize 1993 [S1, S3].

## Childhood and education

Tembu chiefly family; baptised Methodist; Clarkebury, Healdtown, Fort Hare [S1, S4].

## Adult working worldview

"Each easter marks the rebirth of our faith" (1994) [S5]; a lifelong self-described Methodist [S4].

## Heritage (context only)

Methodist and Xhosa [S4].

## Timing

1964–1994, from age 46 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Not assessed.

## Open questions

- Methodist Conference addresses (1994, 1998).

## Research log

- 2026-10-19: Read Britannica, the Nobel biography and facts, Forster (2014) and the Moria address.
