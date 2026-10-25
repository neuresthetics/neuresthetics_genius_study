---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA6)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen D1 (queue #190/228, F 3, rank 202): firm A if a clear reading reaches ≥0.5 over the mixed lines; leave BELOW if still mixed; do not force B or plot. Re-read Autobiography Introduction (S2); Truth Is God anthology / Mind of Mahatma Gandhi God chapters (S4, S6); Hind Swaraj ch. 8/10 near-span God/Maker lines (S7); Young India 5 Mar 1925 personal-and-impersonal both; YI 11 Oct 1928 pervading Power / 'He alone is'; YI 31 Dec 1931 'Truth is God'. A stays BELOW_THRESHOLD: acosmic/Truth/He-alone-is-real (A 4 lead) against face-to-face / personal God for those who need presence / prayer language (A 0–2 lead); Gandhi himself affirms both registers in one paragraph (YI 5-3-1925). No reading reaches 0.5 over the other (Plotinus pattern). B stays UNKNOWN (not a scientist, P30; no nature-law profession). primary HINDU 0.5 written_profession unchanged — Sanatani Hindu self-identification dated Young India 6 Oct 1921 (CPS secondary corroborates anthology date; P20 post-span cap). Mid BELOW. Dual bio P50 (Britannica + Wikipedia EN); P47 on all. Not plotted. Fallacy audit none; figures not refreshed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA6, order P32: F 3, rank 202). Sources: Britannica, signed by B.R. Nanda (scholars edition, read in full), and the Introduction to Gandhi's Autobiography (1927–29, tr. Mahadev Desai), read in full on mkgandhi.org (unofficial web copy). Lasting work: satyagraha, 'born' at the Johannesburg mass meeting of September 1906 (S1); Nanda calls him the 'catalyst' of 'three of the major revolutions of the 20th century'. Span 1906, age 37. Own words: 'to see God face to face, to attain Moksha' and 'He alone is real and all else is unreal' (S2, Introduction signed 26 November 1925); 'I call myself a Sanatani Hindu' (Young India, dated 6 October 1921 in the Truth Is God anthology, S4; date not verified in CWMG); Young India 1924, 'to attain moksha in this very existence' (quoted in S1). All after the span: P20 cap 0.5. primary_system HINDU 0.5 (written_profession, on the explicit 'Sanatani Hindu' self-identification, RQ-AA6-1), alternative BELOW_THRESHOLD (he held all religions 'true' yet 'imperfect', S1). A BELOW_THRESHOLD: 'God as Truth', 'He alone is real' (acosmic, A 4 lead) against 'see God face to face' (personal, A 2 or lower lead); not a scientist, B UNKNOWN; mid_basin BELOW_THRESHOLD. region_of_work Sub-Saharan Africa for the span (South Africa), South Asia afterwards. Not plotted. Draft, not reviewed."}

identity:
  id: gandhi-mahatma
  display_name: "Mahatma Gandhi"
  roster:
    canonical_name: "Mahatma Gandhi"
    rank: 202
    F: 3
    models: [DeepSeek, Gemini, Grok]
    band: "core (3–4)"
    status: "core"
    field: "political thought"
    field_bucket: "politics / law / military"
  full_name: {value: "Mohandas Karamchand Gandhi", certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S5, locator: "infobox / Born"}], how_known: "Britannica and Wikipedia EN agree (P50)."}
  native_name: {value: "મોહનદાસ કરમચંદ ગાંધી", certainty: 0.7, cites: [{source: S5, locator: "lede / Gujarati"}], how_known: "Wikipedia EN Gujarati form; not printed in Britannica scholars page read."}
  aliases:
    - {name: "Gandhi-Mahatma", kind: "roster alias"}
    - {name: "Mohandas Karamchand Gandhi", kind: "birth name"}
    - {name: "Mahatma", kind: "title or honorific"}
    - {name: "Bapu", kind: "other"}

basics:
  birth:
    date: {value: "1869-10-02", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S5, locator: "infobox"}], how_known: "Britannica and Wikipedia EN agree (P50)."}
    place: {value: "Porbandar", modern_name: "Porbandar, Gujarat, India", polity_then: "Porbandar State, Kathiawar Agency, British India", certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S5, locator: "infobox / Born"}], how_known: "Two sources (P50)."}
  death:
    date: {value: "1948-01-30", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S5, locator: "infobox"}], how_known: "Two sources (P50); assassinated."}
    place: {value: "Delhi", modern_name: "New Delhi, India", polity_then: "Dominion of India", certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S5, locator: "infobox"}], how_known: "Two sources (P50)."}
  first_lasting_contribution_year: {value: 1906, certainty: 0.7, cites: [{source: S1, locator: "Emergence as a political and social activist"}, {source: S5, locator: "Civil rights activist in South Africa"}], how_known: "Satyagraha 'born' at the Johannesburg mass meeting, September 1906 (S1; S5 11 September): a documented public statement (P30)."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "text"}], how_known: "1906 (P2)."}
  region_of_birth: {value: "South Asia", certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S5, locator: "infobox"}], how_known: "India (P3); two sources."}
  region_of_work: {value: "Sub-Saharan Africa", certainty: 0.5, cites: [{source: S1, locator: "Emergence as a political and social activist"}, {source: S5, locator: "Civil rights activist in South Africa"}], how_known: "Johannesburg during the 1906 span (region of work follows where the span took place, v8's call on the AA6 audit); alternative South Asia, the home region, where his campaigns from 1915 took place.", alternatives: [{value: "South Asia", note: "India campaigns from 1915 (S1; S5).", cites: [{source: S1, locator: "text"}, {source: S5, locator: "Struggle for Indian independence"}]}]}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Gujarati", "English"], certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S5, locator: "Literary works"}], how_known: "Hind Swaraj and the autobiography in Gujarati; Young India in English (S1; S5)."}
  occupations: {value: ["lawyer", "political leader", "writer"], certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S5, locator: "infobox"}], how_known: "Two sources (P50)."}

contribution:
  fields: {value: ["political thought", "nonviolent resistance"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Satyagraha (nonviolent resistance)", year: 1906, kind: "method", lasting: "Nanda: he became 'the catalyst if not the initiator of three of the major revolutions of the 20th century' (S1); his method influenced Martin Luther King, Jr. (S1; S5)", certainty: 0.7, cites: [{source: S1, locator: "Emergence as a political and social activist; Place in history"}, {source: S5, locator: "lede"}], how_known: "Britannica; Wikipedia corroborates influence."}
  evidence_of_impact:
    - {value: "Influence on Martin Luther King, Jr., and the civil-rights movement", kind: "assessment by a later major figure", certainty: 0.7, cites: [{source: S1, locator: "Place in history"}, {source: S5, locator: "lede"}], how_known: "Britannica and Wikipedia."}
  major_works:
    - {value: "Hind Swaraj", year: 1909, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S5, locator: "Literary works"}], how_known: "Britannica and Wikipedia."}
    - {value: "Salt March", year: 1930, kind: "other", certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S5, locator: "Salt Satyagraha"}], how_known: "Britannica and Wikipedia."}
    - {value: "An Autobiography: The Story of My Experiments with Truth", year: 1927, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S5, locator: "Literary works"}], how_known: "Britannica: 1927–29; Wikipedia."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Originator of satyagraha (S1).", certainty: 0.7, cites: [{source: S1, locator: "Place in history"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "Hindu (Vaishnava / Pranami Vaishnava on mother's side; Jain tinge in the home)", certainty: 0.7, cites: [{source: S1, locator: "Early years"}, {source: S5, locator: "Parents; Childhood"}], how_known: "Britannica Vaishnava with Jain tinge; Wikipedia: Putlibai from a Pranami Vaishnava family. Heritage context only."}
  family_religious_practice: {value: "Mother Putlibai deeply pious — daily prayers and hard vows / fasts (S5)", certainty: 0.7, cites: [{source: S5, locator: "Childhood"}, {source: S1, locator: "Early years"}], how_known: "Wikipedia quoting childhood piety; Britannica 'deeply religious'."}
  parents_and_household:
    - {value: "Father Karamchand Gandhi, dewan (chief minister) of Porbandar then Rajkot; mother Putlibai, deeply religious (Pranami Vaishnava)", role: "family", certainty: 0.7, cites: [{source: S1, locator: "Early years"}, {source: S5, locator: "Parents"}], how_known: "Britannica and Wikipedia."}
  household_circumstances: {value: "Modh Bania (Vaishya) Gujarati merchant-caste household; father in princely-state service", certainty: 0.7, cites: [{source: S5, locator: "Parents; Childhood"}], how_known: "Wikipedia."}
  schooling:
    - {value: "Local school and Alfred High School, Rajkot; brief Samaldas College, Bhavnagar; law at the Inner Temple, London (called to the bar 1891)", certainty: 0.7, cites: [{source: S1, locator: "Early years"}, {source: S5, locator: "Childhood; Student of law"}], how_known: "Britannica and Wikipedia."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading:
    - {value: "Stories of Shravana and king Harishchandra (Indian classics); later, in London, Bhagavad Gita with Theosophical Society members", certainty: 0.7, cites: [{source: S5, locator: "Childhood; Vegetarianism and committee work"}], how_known: "Wikipedia summarizing Autobiography."}
  childhood_mentors: []
  languages_in_childhood: {value: ["Gujarati"], certainty: 0.7, cites: [{source: S5, locator: "Childhood"}], how_known: "Gujarati home; Wikipedia."}
  notable_events:
    - {value: "Arranged marriage to Kasturba Kapadia, 1883 (age 13)", certainty: 0.7, cites: [{source: S5, locator: "Marriage"}, {source: S1, locator: "Early years"}], how_known: "Wikipedia; Britannica."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1906", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Sanatani Hindu (self-described)", years: "1921 (public profession)", certainty: 0.5, cites: [{source: S4, locator: "Why I Am A Hindu"}, {source: S8, locator: "Young India 6 Oct 1921 citation"}], how_known: "Young India 6 Oct 1921 (S4; S8); after the 1906 span (P20 cap 0.5)."}
  self_described_science_religion_relation: {value: "Compares his moral/spiritual experiments to a scientist's open-minded experiments (Autobiography Introduction); not a statement on nature's laws", certainty: 0.5, cites: [{source: S2, locator: "Introduction"}], how_known: "Autobiography Introduction metaphor; after span; does not score B (not a scientist; P30)."}
  primary_system:
    value: HINDU
    basis: written_profession
    certainty: 0.5
    cites: [{source: S4, locator: "Why I Am A Hindu"}, {source: S2, locator: "Introduction"}, {source: S1, locator: "Religious quest"}, {source: S8, locator: "Young India 6 Oct 1921"}]
    how_known: "Young India, 6 October 1921 (S4 anthology; CPS secondary S8 corroborates the date; CWMG volume not opened this pass). Autobiography Introduction (1925). All after the 1906 span (P20 cap 0.5)."
    rationale: "Explicit self-identification: 'I call myself a Sanatani Hindu, because ... I believe in the Vedas, the Upanishads, the Puranas' (S4). Supporting: aim 'to see God face to face, to attain Moksha' (S2); the Gita his 'spiritual dictionary' (S1). RQ-AA6-1. Named alternative BELOW_THRESHOLD: he held all religions 'true' yet 'imperfect' (S1), affirms Bible/Koran/Zend Avesta as divinely inspired alongside the Vedas (S4), and names no exclusive tradition in S2."
  secondary_system: {value: UNKNOWN, how_known: "None coded; Jain influence is heritage/mentor, not profession."}
  candidate_codes_considered:
    - {code: HINDU, reason: "Coded at 0.5 (S4, S2, S1, S8)."}
    - {code: JAIN, reason: "Lead: Jain tinge of the Vaishnava home; mentor Shrimad Rajchandra (S1); heritage, not profession."}
    - {code: PANT, reason: "Lead only, rejected: 'Truth is God' / pervading Power / God in everyone can be read as immanent identity, but he also keeps personal-God and prayer language and never equates God with Nature as such; standing rule and mixed A block a pantheism code."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "Deepen D1 re-check of Autobiography Introduction (S2), Young India God essays (S6), Hind Swaraj near-span Maker lines (S7): still mixed. A 4 lead — 'I worship God as Truth only'; 'He alone is real and all else is unreal' (S2); 'indefinable mysterious Power that pervades everything' / 'He alone is' (YI 11-10-1928, S6); 'Truth is God' (YI 31-12-1931, S6); 'God is neither in heaven, nor down below, but in every one' (S6). Personal / A 0–2 lead — 'to see God face to face' (S2); 'He is a personal God to those who need His personal presence' and prayer/Maker language (YI 5-3-1925, S6; Hind Swaraj, S7); 'whose offspring I am' (S2). In one paragraph he affirms both registers (YI 5-3-1925). No reading reaches 0.5 over the other (Plotinus pattern; deepen standing rule). Do not force plot.", note: "All scored own words are after the 1906 span (P20); mix itself, not the date, blocks the score."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30); no statement on nature's law and exception read. Autobiography's scientist-of-experiments metaphor is about moral method, not physical order. Do not force B."}
    C_ledger: {value: UNKNOWN, how_known: "Not scored this pass; karma/rebirth affirmed as Hindu belief (S4) but ledger axis not opened."}
    D_authority: {value: UNKNOWN, how_known: "Not scored this pass; he subordinates scripture to reason and moral sense (S4) but axis not opened."}
    E_scope: {value: UNKNOWN, how_known: "Not scored this pass."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD, so the P4 test cannot be applied (Pavlov pattern / P19)."}
  statements:
    - text: "What I want to achieve - what I have been striving and pining to achieve these thirty years - is self-realization, to see God face to face, to attain Moksha. I live and move and have my being in pursuit of this goal."
      cites: [{source: S2, locator: "Introduction"}]
      date: "1925-11-26"
      context: "Introduction to the Autobiography, signed 26 November 1925 (tr. Desai); after the span."
      axes: [A_locus]
      kind: "autobiography"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Personal / face-to-face lead. mkgandhi.org transcription of the Desai translation."
    - text: "Often in my progress I have had faint glimpses of the Absolute Truth, God, and daily the conviction is growing upon me that He alone is real and all else is unreal."
      cites: [{source: S2, locator: "Introduction"}]
      date: "1925-11-26"
      context: "Same Introduction."
      axes: [A_locus]
      kind: "autobiography"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Acosmic / A 4 lead. Same Introduction also: 'I worship God as Truth only'."
    - text: "I call myself a Sanatani Hindu, because, 1. I believe in the Vedas, the Upanishads, the Puranas and all that goes by the name of Hindu scriptures, and therefore in Avataras and rebirth;"
      cites: [{source: S4, locator: "Why I Am A Hindu"}, {source: S8, locator: "Young India 6 Oct 1921"}]
      date: "1921-10-06"
      context: "Young India, 6 October 1921 (CPS S8 and Truth Is God anthology agree on 6 Oct 1921; the same page on mkgandhi.org also prints a 20 Oct 1927 Young India piece above it — the Sanatani list is the 1921 article). After the span. CWMG volume not opened this pass."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Primary-system profession; not a locus score by itself."
    - text: "He is a personal God to those who need His personal presence. He is embodied to those who need His touch. He is the purest essence. He simply is to those who have faith. He is all things to all men. He is in us and yet above and beyond us."
      cites: [{source: S6, locator: "Nature of God; Young India 5-3-1925, p. 81"}]
      date: "1925-03-05"
      context: "Young India, 5 March 1925, as compiled in Mind of Mahatma Gandhi ch. 'Truth is God' (S6). After the span."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Same essay continues 'We are not, He alone Is' — both personal and acosmic registers in one piece; the mix that keeps A BELOW."
    - text: "THERE IS an indefinable mysterious Power that pervades everything. I feel it, though I do not see it. ... That informing Power or Spirit is God. And since nothing else I see merely through the senses can or will persist, He alone is."
      cites: [{source: S6, locator: "God Is; Young India 11-10-1928, pp. 340–1"}]
      date: "1928-10-11"
      context: "Young India, 11 October 1928 (S6). After the span."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Pervading-Power / He-alone-is lead (A 4); still opposed by personal/prayer language elsewhere."
    - text: "But two years ago I went a step further and said that Truth is God. You will see the fine distinction between the two statements, viz., that God is Truth and Truth is God."
      cites: [{source: S6, locator: "Nature of God; Young India 31-12-1931, pp. 427–8"}]
      date: "1931-12-31"
      context: "Young India, 31 December 1931, Switzerland meeting reply on the way from the Round Table Conference (S6). After the span."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Truth-is-God formulation; strengthens acosmic/order lead without cancelling personal language."
    - text: "Religion is dear to me, and my first complaint is that India is becoming irreligious. Here I am not thinking of the Hindu and Mahomedan or the Zoroastrian religion, but of the religion which underlies all religions. We are turning away from God."
      cites: [{source: S7, locator: "ch. 8 The Condition of India"}]
      date: "1909"
      context: "Hind Swaraj / Indian Home Rule (1909), Editor voice. Near-span (span 1906); shows theist framing in the political programme years. Not used alone to score A (no locus)."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Near-span God affirmation; same book: 'God gifted man with intellect that he might know his Maker' (ch. 10). Supports continuity of theism into the working years without resolving personal vs acosmic."
  changes_over_life:
    - {value: "Shifts public formula from 'God is Truth' to 'Truth is God' (YI 31-12-1931); still keeps personal-God and prayer language. Recorded; does not unlock A.", year: "c. 1929–1931", certainty: 0.5, cites: [{source: S6, locator: "YI 31-12-1931"}], how_known: "His own Young India statement of the shift."}
  coder_notes: "Deepen D1 2026-10-24: A left BELOW — Gandhi's own YI 5-3-1925 paragraph affirms personal and impersonal registers together; standing rule requires ≥0.5 over the mixed lines before scoring. B not forced (not a scientist). CWMG print check of the 6 Oct 1921 Sanatani article and of Hind Swaraj Gujarati still optional. systems/HINDU.md not re-audited this pass."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Gujarati Modh Bania (Vaishya)", certainty: 0.7, cites: [{source: S5, locator: "Parents; Childhood"}], how_known: "Wikipedia."}
  religious_heritage_by_birth: {value: "Hindu (Vaishnava, with a Jain tinge; mother Pranami Vaishnava)", certainty: 0.7, cites: [{source: S1, locator: "Early years"}, {source: S5, locator: "Parents"}], how_known: "Britannica and Wikipedia."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated beyond mother's piety and Rama-name nurse teaching (S6 / Autobiography)."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1906", certainty: 0.7, cites: [{source: S1, locator: "Emergence as a political and social activist"}], how_known: "The one listed lasting item (P29, P30)."}
  age_at_first_lasting_contribution: {value: 37, certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "1906 − 1869 = 37 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: "1909 (Hind Swaraj God/Maker lines); fuller locus mix from 1921–1931 Young India / Autobiography", certainty: 0.5, cites: [{source: S7, locator: "ch. 8"}, {source: S2, locator: "Introduction"}, {source: S6, locator: "YI essays"}], how_known: "Near-span Hind Swaraj names God/Maker; scored A-mix statements are post-span."}
  lio_views_relative_to_major_work: {value: "after major work", rationale: "Hind Swaraj 1909 is near-span theist framing; the detailed personal/acosmic A-mix (Autobiography 1925; YI 1925–1931) is after the 1906 span (P20).", certainty: 0.5, cites: [{source: S7, locator: "ch. 8"}, {source: S2, locator: "Introduction"}, {source: S6, locator: "YI essays"}], how_known: "Dates of the sources vs span."}
  worldview_during_major_work: {value: "Hindu theist working programme (satyagraha / Truth); locus not resolved for scoring", certainty: 0.5, cites: [{source: S7, locator: "ch. 8"}, {source: S1, locator: "Emergence as a political and social activist"}], how_known: "Near-span Hind Swaraj plus the 1906 method; A stays BELOW."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Ethical and political method (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: "Lane B unused for Gandhi; B_cause UNKNOWN because he is not a scientist and no nature-law profession was read."

institutions:
  - {value: "Natal Indian Congress", role: "founder", years: "1894", kind: "other", certainty: 0.7, cites: [{source: S1, locator: "Emergence as a political and social activist"}, {source: S5, locator: "Civil rights activist in South Africa"}], how_known: "Britannica and Wikipedia."}
  - {value: "Indian National Congress", role: "leader", years: "1920s–1940s", kind: "other", certainty: 0.5, cites: [{source: S1, locator: "text"}, {source: S5, locator: "Struggle for Indian independence"}], how_known: "Britannica and Wikipedia."}
collaborators:
  - {value: "Shrimad Rajchandra", relation: "teacher", note: "Jain mentor", certainty: 0.7, cites: [{source: S1, locator: "Religious quest"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 202"}], how_known: "Study roster."}
  controversies:
    - {value: "Early South Africa racial attitudes and later brahmacharya experiments are debated in the secondary literature (S5); not used for worldview coding.", certainty: 0.5, cites: [{source: S5, locator: "Europeans, Indians and Africans; Brahmacharya"}], how_known: "Wikipedia summary of scholarly debate."}
  data_quality_flags:
    - "Profession and A-mix statements after the span (P20)."
    - "mkgandhi.org copies are unofficial web transcriptions (verified_against)."
  open_questions:
    - "CWMG print check of Young India 6 Oct 1921 Sanatani article and of Hind Swaraj Gujarati/English."
    - "Whether a scholar's Advaita-Vedanta reconstruction (Richards / Gier via S5) should ever lift A under P49 — standing deepen rule here keeps BELOW unless own words resolve the mix."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "B.R. Nanda"
    citation: "Nanda, B.R. 'Mahatma Gandhi.' Encyclopaedia Britannica (scholars edition). https://kids.britannica.com/scholars/article/Mahatma-Gandhi/109421"
    url: "https://kids.britannica.com/scholars/article/Mahatma-Gandhi/109421"
    accessed: 2026-10-24
    reliability_note: "Signed article, scholars edition, read in full (creation pass); re-used for basics on deepen."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "M.K. Gandhi"
    citation: "Gandhi, M.K. An Autobiography or The Story of My Experiments with Truth, tr. Mahadev Desai. Introduction. mkgandhi.org. https://www.mkgandhi.org/autobio/intro.php"
    url: "https://www.mkgandhi.org/autobio/intro.php"
    accessed: 2026-10-24
    reliability_note: "Unofficial web copy of the Desai translation; Introduction re-read in full on deepen."
    source_quality: "unofficial web copy"
    used_for: [worldview]
  - id: S3
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [review]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "M.K. Gandhi, comp. R.K. Prabhu"
    citation: "Gandhi, M.K. Truth Is God, comp. R.K. Prabhu, ch. 22 'Why I Am A Hindu' (from Young India). mkgandhi.org. https://www.mkgandhi.org/truthisgod/22hindu.php"
    url: "https://www.mkgandhi.org/truthisgod/22hindu.php"
    accessed: 2026-10-24
    reliability_note: "Unofficial web copy of an anthology; chapter re-read in full. Page also prints a 20 Oct 1927 Young India piece above the Sanatani list; date of the Sanatani list corroborated as 6 Oct 1921 by S8."
    source_quality: "unofficial web copy"
    used_for: [worldview]
  - id: S5
    type: tertiary
    kind: "encyclopedia"
    author: "Wikipedia contributors"
    citation: "Wikipedia. 'Mahatma Gandhi.' https://en.wikipedia.org/wiki/Mahatma_Gandhi"
    url: "https://en.wikipedia.org/wiki/Mahatma_Gandhi"
    accessed: 2026-10-24
    reliability_note: "English Wikipedia; used for dual-bio P50 (dates/places/names) and childhood/heritage detail. Scholarly Advaita readings cited there (Richards, Gier) noted but not used to lift A."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, heritage, review]
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "M.K. Gandhi (comp. R.K. Prabhu / U.R. Rao)"
    citation: "Mind of Mahatma Gandhi, ch. 'Truth is God' (Young India / Harijan extracts). mkgandhi.org. https://mkgandhi.org/momgandhi/chap10.htm"
    url: "https://mkgandhi.org/momgandhi/chap10.htm"
    accessed: 2026-10-24
    reliability_note: "Unofficial web compilation of dated Young India / Harijan pieces; YI 5-3-1925, 11-10-1928, 31-12-1931 passages used. CWMG not opened."
    source_quality: "unofficial web copy"
    used_for: [worldview]
  - id: S7
    type: primary
    kind: "published work by the subject"
    author: "M.K. Gandhi"
    citation: "Gandhi, M.K. Hind Swaraj or Indian Home Rule (1909). Ch. 8 Condition of India; ch. 10 Hindus and Mahomedans. mkgandhi.org."
    url: "https://www.mkgandhi.org/hindswaraj/chap10_hindumahomedans.php"
    accessed: 2026-10-24
    reliability_note: "Unofficial web copy of the English Hind Swaraj; near-span God/Maker lines. Gujarati original not compared."
    source_quality: "unofficial web copy"
    used_for: [worldview, timing]
  - id: S8
    type: secondary
    kind: "other"
    author: "J.K. Bajaj and M.D. Srinivas / Centre for Policy Studies"
    citation: "Bajaj, J.K. and Srinivas, M.D. 'Relevance of Mahatma Gandhi and His Thought in Modern Times' (CPS); blog reprint 'Mahatma Gandhi and the World III' citing Young India 6.10.1921 for the Sanatani Hindu definition. https://blog.cpsindia.org/2024/06/mahatma-gandhi-and-world-iii.html"
    url: "https://blog.cpsindia.org/2024/06/mahatma-gandhi-and-world-iii.html"
    accessed: 2026-10-24
    reliability_note: "Secondary citation of the Young India date; used only to corroborate 6 Oct 1921 against anthology day-dispute. Not a CWMG substitute."
    source_quality: "other"
    used_for: [worldview]
---

## Summary

Mahatma Gandhi (1869–1948), originator of satyagraha [S1; S5]. Deepen D1: HINDU 0.5 (written_profession, Sanatani self-identification); A BELOW_THRESHOLD (personal vs acosmic mix; no reading ≥0.5 over the other); B UNKNOWN (not a scientist); mid BELOW_THRESHOLD. Not plotted.

## Life and work

Porbandar; London; South Africa (satyagraha 1906); India [S1; S5].

## Contribution and impact

Satyagraha, 1906 [S1; S5].

## Childhood and education

Vaishnava / Pranami home with Jain tinge; Rajkot schools; Inner Temple [S1; S5].

## Adult working worldview

'I call myself a Sanatani Hindu' (Young India, 6 Oct 1921) [S4; S8]. Autobiography Introduction: face-to-face Moksha aim beside 'He alone is real' [S2]. Young India: personal God for those who need presence and pervading Power / Truth is God in the same corpus [S6]. Mix keeps A BELOW. Hind Swaraj 1909 near-span God/Maker framing [S7].

## Heritage (context only)

Gujarati Modh Bania; Vaishnava with Jain tinge; mother Pranami Vaishnava [S1; S5].

## Timing

1906, age 37 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. B_cause UNKNOWN — not a scientist; no nature-law profession.

## Open questions

- CWMG print check of Young India 6 Oct 1921 and Hind Swaraj.
- Whether P49 Advaita reconstruction should ever lift A (standing rule this pass: no).

## Research log

- 2026-10-19: Read Britannica (Nanda, scholars edition); autobiography Introduction; Truth Is God ch. 22.
- 2026-10-24: Deepen D1. Re-read S2; added Wikipedia (S5), Mind of Mahatma Gandhi God chapter (S6), Hind Swaraj (S7), CPS date corroboration (S8). A stays BELOW; B UNKNOWN; primary HINDU 0.5. Wrote drafts/deepen_gandhi-mahatma.md (untracked). Person-file-only commit. No figures/.
