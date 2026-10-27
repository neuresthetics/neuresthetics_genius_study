---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch G; deepen D1 queue #40)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to 20c_early. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch G, order P32: F 5, rank 40). Basics from Britannica (White). Worldview from Per Dahl (Danish Musicology Online 2016), who quotes Conversations with Igor Stravinsky (with Robert Craft, 1959): belief in 'a personal God, a personal Devil and the miracles of the Church'. Britannica calls the Craft books 'factually unreliable', so every worldview field is capped at 0.5. primary_system CHRIST (Russian Orthodox) 0.5; A 0 at 0.5 (alt 1); B 2 at 0.5 (alt 3); C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD. Plotted. Ruling question raised (RQ1 batch G), since ruled as P43. Draft, not reviewed."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "fallacy_catalog blind audit of 5ff29b4: all claims HOLD. RQ1 ruled by Jason as P43 (interview cap 0.5; plotted faded). CLTHEI added as a named alternative code. No value changes."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #40). P47 source_quality on S1–S8. Primary-checked Conversations (Doubleday 1959, IA OCR S4) p. 143: 'Person of the Lord, the Person of the Devil, and the Miracles of the Church' (Dahl's Faber p. 104 paraphrase 'personal God…' corrected). Added Dialogues and a Diary (1963, IA OCR S5): 'I do, of course, believe in a system beyond Nature' plus Venetian finger taken as miracle during 'strictest… Christian Orthodoxy'. Christoforidis 2016 (S6) for 1936 Góngora / La Noche interview ('I am an Orthodox Christian…'; God creates). Wikipedia (S7) native name + baptism; Walsh Catholic Herald (S8) for 6 Apr 1926 communion date vs Dahl's 9 Apr. A_locus 0 @ 0.5 and B_cause 2 @ 0.5 unchanged (P43 Craft cap; no own-hand confirmation). support: corroborated on A and B (P48) via S4+S5 — chart fill hollow→filled; darkness still faded. mid_basin stays BELOW_THRESHOLD. Expositions and Developments primary unread (IA 401). No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: stravinsky-igor
  display_name: "Igor Stravinsky"
  roster:
    canonical_name: "Igor Stravinsky"
    rank: 40
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: music
    field_bucket: music
  full_name: {value: "Igor Fyodorovich Stravinsky", certainty: 1.0, cites: [{source: S1, locator: "At a Glance"}, {source: S7, locator: "lead"}], how_known: "Britannica and Wikipedia agree."}
  native_name: {value: "Игорь Фёдорович Стравинский", certainty: 0.7, cites: [{source: S7, locator: "lead / native name"}], how_known: "Wikipedia Cyrillic form."}
  aliases:
    - {name: "Igor-Stravinsky", kind: "roster alias"}
    - {name: "Stravinsky-Igor", kind: "roster alias"}

basics:
  birth:
    date: {value: "1882-06-17", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "lead"}], how_known: "Britannica and Wikipedia: 17 June [O.S. 5 June] 1882; Gregorian kept."}
    place: {value: "Oranienbaum, near St. Petersburg, Russia", modern_name: "Lomonosov, Russia", polity_then: "Russian Empire", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "lead"}], how_known: "Britannica and Wikipedia."}
  death:
    date: {value: "1971-04-06", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "lead"}, {source: S8, locator: "opening"}], how_known: "Britannica, Wikipedia, and Walsh (Holy Week Tuesday)."}
    place: {value: "New York, New York, U.S.", modern_name: "New York, United States", polity_then: "United States", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "lead"}], how_known: "Britannica and Wikipedia."}
  first_lasting_contribution_year: {value: 1910, certainty: 0.7, cites: [{source: S1, locator: "'Life and career'"}], how_known: "The Firebird, premiered 25 June 1910, 'made Stravinsky known overnight' (P13). Earlier student works were performed but are not listed as lasting."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S1, locator: "'Life and career'"}], how_known: "From 1910 (P2)."}
  region_of_birth: {value: "Eastern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Russia is Eastern Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.5, cites: [{source: S1, locator: "'Life and career'"}], how_known: "Switzerland and France 1910–1939, then the United States from 1940; the main works through 1939 were in Western Europe (0.5)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [Russian, French, English], certainty: 0.5, cites: [{source: S1, locator: "'Life and career'"}, {source: S7, locator: "Life"}], how_known: "Inferred from residence, texts set, and later U.S. career; not a single explicit list."}
  occupations: {value: ["composer", "pianist", "conductor"], certainty: 0.7, cites: [{source: S1, locator: "'Life and career'"}], how_known: "Britannica."}

contribution:
  era_bucket: 20c_early
  fields: {value: ["music"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "The Firebird", year: 1910, kind: work, lasting: "made him known overnight (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Life and career'"}], how_known: "Britannica."}
    - {value: "The Rite of Spring", year: 1913, kind: work, lasting: "'an early modernist landmark' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Life and career'"}], how_known: "Britannica."}
    - {value: "Symphony of Psalms", year: 1930, kind: work, lasting: "(S1)", certainty: 0.7, cites: [{source: S1, locator: "'Life and career'"}], how_known: "Britannica."}
    - {value: "The Rake's Progress", year: 1951, kind: work, lasting: "his only full-length opera (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Life and career'"}], how_known: "Britannica (worked on 1948–51)."}
    - {value: "Requiem Canticles", year: 1966, kind: work, lasting: "'his last major work' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Life and career'"}], how_known: "Britannica."}
  evidence_of_impact:
    - {value: "Royal Philharmonic Society Gold Medal (1954); Wihuri Sibelius Prize (1963)", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "'Revolutionary impact on musical thought' (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Russian Orthodox", certainty: 0.7, cites: [{source: S2, locator: "p. 61"}, {source: S7, locator: "Early life"}], how_known: "Baptized into Russian Orthodoxy (S7); Dahl: christened Orthodox in Oranienbaum; he later 'rejoined' (S2)."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father Fyodor Ignatievich Stravinsky, one of the leading Russian operatic basses of his day", role: parents, certainty: 0.7, cites: [{source: S1, locator: "'Life and career'"}, {source: S7, locator: "Early life"}], how_known: "Britannica body; Wikipedia names Fyodor."}
    - {value: "Mother Anna Kirillovna Stravinskaya (née Kholodovskaya)", role: parents, certainty: 0.5, cites: [{source: S7, locator: "Early life"}], how_known: "Wikipedia only (Britannica Top Questions box not used)."}
  household_circumstances: {value: "Musical, theatrical and literary household", certainty: 0.7, cites: [{source: S1, locator: "'Life and career'"}], how_known: "Britannica."}
  schooling:
    - {value: "St. Petersburg University (law and philosophy)", stage: university, run_by: "state or municipal", years: "–1905", ages: "–23", certainty: 0.7, cites: [{source: S1, locator: "'Life and career'"}], how_known: "Britannica: graduated 1905."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "Nikolay Rimsky-Korsakov, private teacher from 1902", certainty: 0.7, cites: [{source: S1, locator: "'Life and career'"}], how_known: "Britannica."}
  languages_in_childhood: {value: TODO}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1910–1966", certainty: 0.7, cites: [{source: S1, locator: "'Life and career'"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Russian Orthodox Church (rejoined 1926; first Communion reported 6 or 9 April 1926)", certainty: 0.7, cites: [{source: S2, locator: "p. 61"}, {source: S1, locator: "'Life and career' ('In 1926 Stravinsky experienced a religious conversion')"}, {source: S8, locator: "opening (6 April 1926)"}], how_known: "Dahl and Britannica agree on the 1926 conversion; Dahl gives first communion 9 April 1926, Walsh (S8) 6 April 1926 — date open."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing read on science and religion as a pair; 1936 interview contrasts 'musical chemist' Schoenberg with Christian dialectic (S6) but does not state a science–religion relation."}
  primary_system:
    value: CHRIST
    basis: recorded_interview
    certainty: 0.5
    cites: [{source: S4, locator: "Doubleday 1959, p. 143 (Music and the Church)"}, {source: S2, locator: "p. 64 and note 20"}, {source: S1, locator: "'Life and career'"}, {source: S6, locator: "p. 64 (Góngora / La Noche 12 Mar 1936)"}]
    rationale: "Rejoined the Russian Orthodox Church in 1926 (S1, S2) and, in Conversations, says composing in the old church forms needs belief 'in the Person of the Lord, the Person of the Devil, and the Miracles of the Church' (S4; Dahl S2 paraphrased 'personal God'). 1936 La Noche interview via Christoforidis: 'I am an Orthodox Christian, sympathetic to Catholicism' (S6). Under P42/P43 the Craft books count as his words with basis recorded_interview, capped at 0.5 until a document in his own hand confirms the view. Chroniques / Autobiography (own hand) read; it does not state personal God or Church miracles."
    how_known: "(interview) Conversations primary (S4) plus Dahl; 1936 newspaper interview only via scholarly secondary (S6)."
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Chosen: Orthodox communion from 1926; Person of the Lord and Church miracles (S4); self-described Orthodox Christian (S6)."}
    - {code: CLTHEI, reason: "Named alternative (fallacy_catalog audit of 5ff29b4): a personal God with live Church miracles fits interventionist personal theism; not chosen as primary because the profession is confessional (Orthodox). Not result-changing: A and B decide the plot."}
  lio_axes:
    A_locus:
      value: 0
      basis: recorded_interview
      certainty: 0.5
      support: corroborated
      cites: [{source: S4, locator: "Doubleday 1959, p. 143"}, {source: S5, locator: "Dialogues, pp. 9–10 (OCR; 'system beyond Nature')"}]
      how_known: "(interview) Conversations (S4) and Dialogues (S5), both Craft books; P43 caps at 0.5."
      rationale: "'Person of the Lord' set against mere 'symbolic figures' (S4): a personal God, not the world. Independently, Dialogues: 'I do, of course, believe in a system beyond Nature' (S5). Scored 0 (transcendent person). Named alternative: 1 (nothing on God being outside the world as such beyond the Dialogues line)."
    B_cause:
      value: 2
      basis: recorded_interview
      certainty: 0.5
      support: corroborated
      cites: [{source: S4, locator: "Doubleday 1959, p. 143"}, {source: S5, locator: "Dialogues, pp. 9–10 (Venetian finger taken as miracle)"}]
      how_known: "(interview) Same Craft books; P43 caps at 0.5."
      rationale: "Scored on his account of nature (P6, P16): belief in 'the Miracles of the Church' (S4) is a stated acceptance of miracles. Dialogues recounts a 1925 Venetian finger-healing he 'took… for a miracle' while affirming a system beyond Nature (S5). The Church's miracles are not stated to be rare or past, and nothing states a lawful general order, so the B 2 anchor (miracles as a live part of how events go, P27) fits better than B 3. Named alternative: 3 (if read as accepted past miracles within a lawful order)."
    C_ledger: {value: UNKNOWN, how_known: "Nothing read on reward and punishment."}
    D_authority: {value: UNKNOWN, how_known: "Nothing read on revelation against observation."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A 0 and B 2 at 0.5: A ≤ 1 with B 2 would have no branch at ≥ 0.7 (§6), and both axes are below the test's 0.7 bar, so BELOW_THRESHOLD (P19). Dialogues 'system beyond Nature' (S5) would support a mid_basin reading if certainty reached 0.7."}
  statements:
    - text: "Certainly, and not merely a believer in \"symbolic figures,\" but in the Person of the Lord, the Person of the Devil, and the Miracles of the Church."
      cites: [{source: S4, locator: "Doubleday 1959, p. 143"}, {source: S2, locator: "p. 64; note 20 (Faber 1959, p. 104) — Dahl paraphrase"}]
      date: "1959"
      context: "Answer, in Conversations with Robert Craft, to 'Must one be a believer to compose in these forms?' (Music and the Church)."
      axes: [A_locus, B_cause]
      kind: "recorded interview"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Primary Doubleday 1959 OCR (S4). Dahl's Faber wording ('a personal God, a personal Devil…') is a close paraphrase; Person of the Lord is the printed form. Craft books' first-person wording disputed (S1: 'factually unreliable'); P43."
    - text: "I do, of course, believe in a system beyond Nature."
      cites: [{source: S5, locator: "Dialogues and a Diary, pp. 9–10 (OCR; after Venetian finger episode)"}]
      date: "1963"
      context: "After recounting the Sept 1925 Venetian concert finger-healing he took for a miracle, during his 'strictest and most earnest period of Christian Orthodoxy'."
      axes: [A_locus, B_cause]
      kind: "recorded interview"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Craft book (Dialogues); P43 cap. Independent of the Conversations believer-forms answer."
    - text: "For some years before my actual \"conversion\", a mood of acceptance had been cultivated in me by a reading of the Gospels and by other religious literature"
      cites: [{source: S2, locator: "p. 64; note 16 cites Expositions and Developments (1962), pp. 63–64"}]
      date: "1962"
      context: "On his 1926 return to the Church. Context only; not used to score."
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "Dahl's quotation; Expositions primary unread (IA borrow/401). Craft book; P43."
    - text: "I am an Orthodox Christian, sympathetic to Catholicism."
      cites: [{source: S6, locator: "p. 64, quoting Luis de Góngora, 'Igor Strawinsky y el Surrealismo,' La Noche, 12 March 1936"}]
      date: "1936-03-12"
      context: "Spanish newspaper interview (Barcelona), rejecting Surrealism and communism; also 'I believe in the object because God makes me create it, just as he created me' and 'my religious faith has made me a dualist…'."
      axes: []
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Primary La Noche unread; wording via Christoforidis. Not a Craft book — newspaper interview — but secondary quotation only; used to corroborate Orthodox identity, not to raise A/B above P43."
  changes_over_life:
    - {value: "Return to the Russian Orthodox Church", year: 1926, certainty: 0.7, cites: [{source: S1, locator: "'Life and career'"}, {source: S2, locator: "p. 61"}, {source: S8, locator: "opening"}], how_known: "Two scholarly streams (Britannica/Dahl; Walsh). The scored axes describe the worldview from 1926; the Firebird-to-Rite years (1910–1913) are before it, and nothing is read on them."}
  coder_notes: "Deepen D1: Conversations and Dialogues primary-checked via IA OCR (S4, S5). A 0 and B 2 stay at 0.5 under P43 — no document in his own hand confirms personal God / Church miracles / system beyond Nature (Autobiography Chroniques read; silent on those claims). support corroborated (S4+S5) → chart fill hollow→filled; darkness still faded. First Communion date 6 Apr (Walsh S8) vs 9 Apr (Dahl S2) unresolved. Expositions primary still unread."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Russian", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Russian Orthodox", certainty: 0.7, cites: [{source: S2, locator: "p. 61"}, {source: S7, locator: "Early life"}], how_known: "Baptized Orthodox (S7); Dahl 'rejoined' implies prior membership (S2)."}
  baptism_or_initiation: {value: "Baptized into the Russian Orthodox Church shortly after birth (hours after birth at St. Nicholas Cathedral per S7; Oranienbaum christening 'some days after' per S2) — place/timing details conflict", certainty: 0.5, cites: [{source: S7, locator: "Early life"}, {source: S2, locator: "p. 61"}], how_known: "Wikipedia vs Dahl disagree on hours vs days and cathedral vs Oranienbaum; fact of Orthodox baptism agreed."}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1910–1966", certainty: 0.7, cites: [{source: S1, locator: "'Life and career'"}], how_known: "1910 to 1966, first to last listed lasting contribution (P29, P30)."}
  age_at_first_lasting_contribution: {value: 28, certainty: 1.0, cites: [{source: S1, locator: "opening; 'Life and career'"}, {source: S7, locator: "lead"}], how_known: "1910 − 1882 = 28 (P30); birth year dual-sourced."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "B 2 is not an LIO-type view (P27); none read."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S4, locator: "p. 143"}], how_known: "Nothing LIO-type read."}
  worldview_during_major_work: {value: "CHRIST", certainty: 0.5, cites: [{source: S2, locator: "p. 61, p. 64"}, {source: S4, locator: "p. 143"}], how_known: "From 1926; before then not documented."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Serial technique and Neoclassical form are musical, not geometric (S1).", certainty: 0.5, cites: [{source: S1, locator: "'Life and career'"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "'Life and career'"}], how_known: "Nothing on mathematics."}
  circle_present: {value: "no", rationale: "Personal God and Church miracles; no lawful-order statement.", certainty: 0.5, cites: [{source: S4, locator: "p. 143"}], how_known: "Coder's reading."}
  reading: "Confessional Orthodox belief in a personal God and Church miracles; no LIO circle read."
  notes: ""

institutions:
  - {value: "Ballets Russes (Serge Diaghilev)", role: "commissioned composer", years: "1910–1928", kind: "patron or funder", certainty: 0.7, cites: [{source: S1, locator: "'Life and career'"}], how_known: "Britannica."}
  - {value: "Harvard University (Charles Eliot Norton Lectures)", role: lecturer, years: "1939–1940", kind: university, certainty: 0.7, cites: [{source: S1, locator: "'Life and career'"}], how_known: "Britannica."}
collaborators:
  - {value: "Robert Craft", relation: collaborator, note: "assistant and co-author of six books from 1948", certainty: 0.7, cites: [{source: S1, locator: "'Life and career'"}], how_known: "Britannica."}
  - {value: "Nikolay Rimsky-Korsakov", relation: teacher, note: "private pupil from 1902", certainty: 0.7, cites: [{source: S1, locator: "'Life and career'"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 40"}], how_known: "Study roster."}
  controversies:
    - {value: "Reliability of the Craft books as his own words", certainty: 0.7, cites: [{source: S1, locator: "'Life and career' ('factually unreliable')"}, {source: S7, locator: "notes on Craft memoirs"}], how_known: "Britannica; Wikipedia notes Craft books unreliable/factually inaccurate; Dahl notes Taruskin and Walsh revisit the Craft portrayal (S2, p. 61)."}
  data_quality_flags: []
  open_questions:
    - "Own-hand document confirming Person of the Lord / Miracles of the Church / system beyond Nature would be needed to raise A or B above 0.5 (P43)."
    - "Expositions and Developments (1962) pp. 63–64 primary unread (IA 401)."
    - "First Communion date: Walsh 6 April 1926 vs Dahl 9 April 1926."
    - "Baptism place/timing: Wikipedia St. Nicholas Cathedral hours after birth vs Dahl Oranienbaum some days after."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Eric Walter White"
    citation: "White, Eric Walter. \"Igor Stravinsky.\" Encyclopaedia Britannica, updated 11 September 2026. https://www.britannica.com/biography/Igor-Stravinsky."
    url: "https://www.britannica.com/biography/Igor-Stravinsky"
    accessed: 2026-10-15
    source_quality: "reference entry"
    reliability_note: "Signed article body; the Top Questions box is not used. Re-fetch 2026-10-24 hit Cloudflare challenge; prior read retained."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators, review]
  - id: S2
    type: secondary
    kind: "journal article"
    author: "Per Dahl"
    year: 2016
    citation: "Dahl, Per. \"Text, Identity and Belief in Stravinsky's Symphony of Psalms.\" Danish Musicology Online, Special Edition 2016 (17th Nordic Musicological Congress), pp. 61–80. ISSN 1904-237X."
    url: "https://www.danishmusicologyonline.dk/arkiv/arkiv_dmo/dmo_saernummer_2016/dmo_saernummer_2016_NMC_04.pdf"
    accessed: 2026-10-15
    source_quality: "scholarly edition or monograph"
    reliability_note: "Scholarly article (congress proceedings), re-read in full as PDF 2026-10-24; page numbers as printed. Faber Conversations p. 104 citation cross-checked against Doubleday primary (S4)."
    used_for: [childhood, worldview, heritage, timing, lane_b, review]
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
    kind: "other"
    author: "Igor Stravinsky and Robert Craft"
    year: 1959
    citation: "Stravinsky, Igor, and Robert Craft. Conversations with Igor Stravinsky. Garden City, N.Y.: Doubleday, 1959. Internet Archive OCR (conversationswit00stra)."
    url: "https://archive.org/details/conversationswit00stra"
    accessed: 2026-10-24
    source_quality: "archive scan (OCR only)"
    reliability_note: "Craft interview book; Britannica calls Craft books factually unreliable (S1). P43: scores as recorded_interview, capped at 0.5. Doubleday pagination: believer-forms answer on p. 143 (Music and the Church); Dahl cites Faber 1959 p. 104 for the same exchange."
    used_for: [worldview, timing, lane_b]
  - id: S5
    type: primary
    kind: "other"
    author: "Igor Stravinsky and Robert Craft"
    year: 1963
    citation: "Stravinsky, Igor, and Robert Craft. Dialogues and a Diary. New York: Doubleday, 1963. Internet Archive OCR (dialoguesanddiar00stra)."
    url: "https://archive.org/details/dialoguesanddiar00stra"
    accessed: 2026-10-24
    source_quality: "archive scan (OCR only)"
    reliability_note: "Craft interview book; P43. Pages ~9–10 (OCR): Venetian miracle episode and 'system beyond Nature'. Distinct from Conversations (S4)."
    used_for: [worldview]
  - id: S6
    type: secondary
    kind: "journal article"
    author: "Michael Christoforidis"
    year: 2016
    citation: "Christoforidis, Michael. \"Igor Stravinsky, Spanish Catholicism and Generalísimo Franco.\" In Context: Journal of Music Research (University of Melbourne), no. 22 (or as paginated in hosted PDF), quoting Luis de Góngora, La Noche, 12 March 1936."
    url: "https://bpb-ap-se2.wpmucdn.com/blogs.unimelb.edu.au/dist/6/184/files/2016/11/22_Christoforidis-1w526od.pdf"
    accessed: 2026-10-24
    source_quality: "scholarly edition or monograph"
    reliability_note: "Scholarly article; 1936 interview wording only via this secondary quotation. Primary La Noche unread."
    used_for: [worldview]
  - id: S7
    type: secondary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia. \"Igor Stravinsky.\" English Wikipedia. https://en.wikipedia.org/wiki/Igor_Stravinsky."
    url: "https://en.wikipedia.org/wiki/Igor_Stravinsky"
    accessed: 2026-10-24
    source_quality: "other"
    reliability_note: "Used for Cyrillic native name, parents' names, baptism claim, and dual-source birth/death with S1. Craft-reliability note cross-check only."
    used_for: [identity, basics, childhood, heritage, review]
  - id: S8
    type: secondary
    kind: "other"
    author: "Stephen Walsh"
    year: 2021
    citation: "Walsh, Stephen. \"Composer at the crossroads.\" The Catholic Herald, 1 April 2021. https://thecatholicherald.com/article/composer-at-the-crossroads."
    url: "https://thecatholicherald.com/article/composer-at-the-crossroads"
    accessed: 2026-10-24
    source_quality: "other"
    reliability_note: "Popular-press piece by Stravinsky's scholarly biographer; used for death/Holy Week note and first Confession/Communion dated 6 April 1926 (vs Dahl 9 April)."
    used_for: [basics, worldview, review]
---

# Igor Stravinsky

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Igor Stravinsky (1882–1971), Russian-born composer: The Firebird, The Rite of Spring, Symphony of Psalms, The Rake's Progress [S1]. Draft: primary_system CHRIST 0.5 (interview); A 0 and B 2 at 0.5 (interview), support corroborated; C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD. Plotted faded, now filled (P48).

## Life and work

St. Petersburg; Ballets Russes in Paris; Switzerland, France, then Hollywood from 1940 [S1]. Returned to Russian Orthodoxy in 1926 [S1, S2]; first Communion dated 6 Apr (Walsh) or 9 Apr (Dahl) [S8, S2].

## Contribution and impact

Firebird (1910), Rite (1913), Neoclassical and late serial works to Requiem Canticles (1966) [S1].

## Childhood and education

Son of bass Fyodor Stravinsky; baptized Orthodox (details conflict) [S1, S7, S2]; law at St. Petersburg; private pupil of Rimsky-Korsakov [S1].

## Adult working worldview

In Conversations (Doubleday 1959, p. 143) he says sacred composition needs belief 'in the Person of the Lord, the Person of the Devil, and the Miracles of the Church' [S4]. Dialogues: 'I do, of course, believe in a system beyond Nature' [S5]. 1936 La Noche: 'I am an Orthodox Christian…' [S6]. Craft books 'factually unreliable' [S1] → P43 cap 0.5; no own-hand lift. A/B support corroborated via S4+S5.

## Heritage (context only)

Russian, Orthodox by birth [S1, S2, S7].

## Timing

First lasting contribution 1910, at 28 [S1, S7].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No LIO circle read [S4].

## Open questions

- Own-hand confirmation needed to raise A/B above 0.5 (P43).
- Expositions 1962 primary unread; Communion date 6 vs 9 Apr; baptism place/timing conflict.

## Research log

- 2026-10-15: Read Britannica (White) and Dahl (2016, full PDF). Search excerpts (Sydney Undergraduate journal on Maritain; NYRB 'Obiter Dicta') seen but not cited.
- 2026-10-24 (deepen D1, queue #40): P47 on S1–S8. Primary OCR: Conversations Doubleday 1959 (S4), Dialogues 1963 (S5). Christoforidis/Góngora 1936 (S6). Wikipedia (S7), Walsh Catholic Herald (S8). Autobiography Chroniques OCR scanned for own-hand A/B — none. Expositions IA 401. Britannica re-fetch Cloudflare. A/B values unchanged; support corroborated. No fallacy_catalog.
