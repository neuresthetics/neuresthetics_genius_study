---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 5
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch U)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to 20c_late. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #115 / F4 rank 116). Goals: corroborate A and B (hollow→filled); prefer Strength to Love print vs drafts; RQ-KK1 stands unless print differs in substance. Read Suffering and Faith (Christian Century 27 Apr 1960; S8): 'More than ever before I am convinced of the reality of a personal God.' Re-read S5/S6/S7 King Papers drafts with editors' published-version notes: Love in Action fixed-laws paragraph unmarked (note 6 concerns next sentence only); Answer thunderbolt/miracle unmarked; free-will and 'exceedingly abundant' altered in print but same substance (S6 notes 25, 27; STL pp. 123+). Dual bio Wikipedia EN (S9, P50). P47 source_quality on S1–S9. A 1 @0.7 support single→corroborated (S2+S8; alt 0). B 3 @0.7 support single→corroborated (S5+S6+S3+S7+S2; alts 4 and 2; S7 moral/physical-law parallel and absolute moral laws folded into preferred reading; S2 loving-purpose). D labelled support corroborated (S2+S3). mid_basin true @0.7 unchanged. Chart: dark hollow → dark filled (fill cue). Scores unchanged. No fallacy_catalog. No figures/. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z1 audit fixes (blind audit /workspace/genius_study_audit/gs_8813a47_Z1/run1/), leftovers: KK4 credited to the ca27fcf audit in two places (was 'batch Y audit'); 'sent to the publisher' dropped from three reliability_notes (not stated by the King Papers). No score changed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Audit fixes (gs_ca27fcf_KK run 1): (KK4) 'every significant change' replaced by 'the notes mark no change here'; the Strength to Love quotes labelled draft wording, with printed variants where known from secondary quotations (ch. IV 'She must honor everlastingly ...', unconfirmed; ch. XV 'to expect God to do everything', unmarked in the notes). (KK11) Summary now B 3 at 0.7. (Note) the P27 exception named: ch. XV 'He has made us persons with freedom, free to choose the good and therefore free to choose what is not good' (P30 #14). Ruling RQ-KK1 (v8's call on the auditor's advice, consistent with Jason's approval): 0.7 stands for the draft reading, to be revisited only if the print differs in substance. No score changes."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Jason's ruling on RQ U1 (2026-10-19, 'fix them'): B_cause re-based on Strength to Love (1963, in the span), read in the King Papers first typed drafts (new S5 'Love in Action': 'She must do everlasting honor to her fixed, immutable laws'; S6 'The Answer to a Perplexing Question': 'through some breathtaking miracle or a wave of the hand'; S7 'Our God Is Able' for the B 2 alternative): B 3 0.5 -> 0.7, basis consistent_private_letters -> written_profession (fixes KI9), alternatives 4 and 2, the 1949 essay kept as support. mid_basin BELOW_THRESHOLD -> true at 0.7; plotted dot now solid. Three statements added."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Audit fixes for batch U (gs_59bb9fc_U run 1): Britannica byline corrected to Clayborne Carson (KI2); B how_known now says the 1949 essay is one private document, scholar-backed, 0.5 (§3), with the basis label kept pending ruling U1 (KI9, on instruction); 'editors back the reading' narrowed to scriptural literalism (note). B and mid_basin unchanged; U1 (re-basing B on Strength to Love) not applied: waiting on Jason."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch U, order P32: F 4, rank 116). Basics from Britannica (Clayborne Carson; author corrected in the batch U audit fixes). Worldview from two texts in the King Papers online edition (Stanford King Institute): 'Pilgrimage to Nonviolence' (Christian Century, 13 April 1960; in span) and a 1949 Crozer seminary essay (unpublished; before the span, P31). Not a scientist (P30). primary_system CHRIST (0.7, alt CLTHEI); A 1 (0.7, alt 0); B 3 (0.5, alts 4 and 2; P41, from the 1949 essay); C UNKNOWN; D 2 (0.7, alt 3); E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD (B at 0.5). Plotted (faded). Draft, not reviewed."}

identity:
  id: king-martin-luther-jr
  display_name: "Martin Luther King Jr."
  roster:
    canonical_name: "Martin Luther King Jr."
    rank: 116
    F: 4
    models: [DeepSeek, Gemini, GPT, Grok]
    band: "core (3–4)"
    status: core
    field: "social thought"
    field_bucket: "politics / law / military"
  full_name: {value: "Martin Luther King, Jr. (born Michael King, Jr.)", certainty: 0.7, cites: [{source: S1, locator: "facts box (Original name)"}], how_known: "Britannica."}
  native_name: {value: "Martin Luther King, Jr.", certainty: 0.7, cites: [{source: S1, locator: "facts box"}], how_known: "English; same as the full name."}
  aliases:
    - {name: "King Jr-Martin Luther", kind: "roster alias"}
    - {name: "Martin Luther King Jr-", kind: "roster alias"}
    - {name: "Martin-Luther-King-Jr", kind: "roster alias"}
    - {name: "Michael King, Jr.", kind: "birth name"}

basics:
  birth:
    date: {value: "1929-01-15", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "facts box (Born); opening"}, {source: S9, locator: "lead / Infobox"}], how_known: "Britannica and Wikipedia EN (P50)."}
    place: {value: "Atlanta, Georgia", modern_name: "Atlanta, Georgia, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "facts box (Born)"}], how_known: "Britannica."}
  death:
    date: {value: "1968-04-04", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "facts box (Died); opening"}, {source: S9, locator: "lead / Infobox"}], how_known: "Britannica and Wikipedia EN (P50); assassinated."}
    place: {value: "Memphis, Tennessee", modern_name: "Memphis, Tennessee, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "facts box (Died)"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1955, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "part II"}], how_known: "Leadership of the civil rights movement 'from the mid-1950s' (S1), beginning as spokesman of the Montgomery bus boycott (S2). A range date sets the span start (P12)."}
  era_bucket: {value: "1950 on", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "1955 (P2)."}
  region_of_birth: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "facts box"}], how_known: "United States (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "United States."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Pronouns in Britannica."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  occupations: {value: ["Baptist minister", "civil rights leader", "head of the Southern Christian Leadership Conference"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

contribution:
  era_bucket: 20c_late
  fields: {value: ["civil rights", "social ethics", "nonviolent resistance"], certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "part II"}], how_known: "Britannica and his essay."}
  lasting_original_contributions:
    - {value: "Leadership of the US civil rights movement by nonviolent methods, from the Montgomery bus boycott to his death, ending legal segregation in the South", year: 1955, kind: other, lasting: "'His leadership was fundamental to that movement’s success in ending the legal segregation of African Americans in the South and other parts of the United States' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "part II"}], how_known: "Britannica; range 1955–1968 (P12), from the boycott, which began 'about a year' after he came to Montgomery in 1954 (S2), to his death (S1). Not a theory about natural systems, so not a scientist (P30)."}
    - {value: "'I Have a Dream' speech, March on Washington", year: 1963, kind: work, lasting: "'His most famous work' (S1, question box, cited only for the date) and the March on Washington (1963) in the body (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; question box 'What is Martin Luther King, Jr., known for?'"}], how_known: "Britannica. Inside the range above."}
  evidence_of_impact:
    - {value: "Nobel Peace Prize, 1964", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    - {value: "Martin Luther King, Jr., Day, a US federal holiday first observed in 1986", kind: "named after them", certainty: 0.7, cites: [{source: S1, locator: "question box 'How did Martin Luther King, Jr., die?'"}], how_known: "Britannica question box (date only)."}
  major_works: []
  honours:
    - {value: "Nobel Peace Prize", year: 1964, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  definition_fit: {value: "clearly meets", rationale: "Leadership 'fundamental' to ending legal segregation (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "Baptist (Protestant)", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Father and maternal grandfather Baptist preachers (S1)."}
  family_religious_practice: {value: "Father pastor of Ebenezer Baptist Church, Atlanta; raised 'in a rather strict fundamentalistic tradition'", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}, {source: S2, locator: "opening paragraph"}], how_known: "Britannica and his own account (S2)."}
  parents_and_household:
    - {value: "Father: Michael (later Martin Luther) King, Sr., pastor of Ebenezer Baptist Church", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
    - {value: "Mother: Alberta Williams King; her father had been pastor of Ebenezer", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  household_circumstances: {value: "Comfortable, college-educated middle-class family on Auburn Avenue, Atlanta", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  schooling:
    - {value: "Morehouse College, Atlanta (entered at 15 under a wartime program); graduated 1948", stage: university, run_by: private, years: "1944–1948", certainty: 0.5, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica; operator the coder's reading."}
    - {value: "Crozer Theological Seminary, Chester, Pennsylvania; B.D. 1951", stage: university, run_by: other, years: "1948–1951", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica; operator not stated."}
    - {value: "Boston University; Ph.D. 1955 (dissertation comparing the conceptions of God of Tillich and Wieman)", stage: university, run_by: private, years: "1951–1955", certainty: 0.5, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica; start year and operator the coder's."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure:
    - {value: "Favoured medicine and law at Morehouse before choosing the ministry", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  key_early_reading:
    - {value: "Rauschenbusch, Christianity and the Social Crisis (early 1950s); Niebuhr; Gandhi", certainty: 0.7, cites: [{source: S2, locator: "parts I–II"}], how_known: "His own account (1960)."}
  childhood_mentors:
    - {value: "Benjamin Mays, Morehouse president and social-gospel activist", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  languages_in_childhood: {value: ["English"], certainty: 0.5, cites: [{source: S1, locator: "'Early years'"}], how_known: "Coder's reading."}
  notable_events:
    - {value: "At about six, a white playmate was no longer allowed to play with him once schools separated; at 12, after his grandmother's death, he jumped from a second-story window", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1955–1968", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "Liberal theology's 'refusal to abandon the best light of reason' and biblical criticism to be 'defended with religious and scientific passion', but 'Reason, devoid of the purifying power of faith, can never free itself from distortions and rationalizations' (1960)", certainty: 0.7, cites: [{source: S2, locator: "part I"}], how_known: "Published essay in the span; contested reading (D 2 against 3), so 0.7."}
  primary_system:
    value: CHRIST
    basis: written_profession
    certainty: 0.7
    cites: [{source: S2, locator: "parts I–II, closing section"}]
    rationale: "Christian belief in his own published writing: 'Christ furnished the spirit and motivation while Gandhi furnished the method'; 'the ultimate Christian answer'; 'the Christian doctrine of love'; a living, personal God. Baptist minister (S1); branch Protestant (Baptist). Named alternative CLTHEI: 'this God both evokes and answers prayers' stresses petition, but it is one clause, and the essay's theology (a synthesis of liberalism and neo-orthodoxy) is not a popular interventionist theism, so CHRIST at 0.7."
    how_known: "Published essay inside the span (Christian Century, 13 April 1960); 0.7 because an alternative is named (contested readings)."
    alternatives:
      - {value: CLTHEI, note: "'this God both evokes and answers prayers'.", cites: [{source: S2, locator: "closing section"}]}
  secondary_system: {value: UNKNOWN, how_known: "One system (P29)."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Chosen at 0.7."}
    - {code: CLTHEI, reason: "Named alternative: answered prayer."}
    - {code: CLASS_THEISM, reason: "Rejected: no Thomist simple God; his God has 'feeling and will'."}
  lio_axes:
    A_locus:
      value: 1
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S2, locator: "closing section; part I"}, {source: S8, locator: "closing paragraph ('reality of a personal God')"}, {source: S7, locator: "closing: 'great benign Power in the universe whose name is God'"}]
      rationale: "Transcendent-person pole with limits: 'the reality of a personal God'; 'In him there is feeling and will'; but 'To say God is personal is not to make him an object among other objects', and he faults both liberalism's 'overstress of his immanence' and neo-orthodoxy's God 'hidden, unknown and \"wholly other\"', taking a middle course (S2). Corroborated by Suffering and Faith (S8): 'More than ever before I am convinced of the reality of a personal God,' and by Our God Is Able (S7): 'a great benign Power in the universe whose name is God.' Named alternative 0 (a personal God who answers prayer, with no immanence claimed)."
      how_known: "Two independent published essays in the span (Pilgrimage, Christian Century 13 Apr 1960; Suffering and Faith, Christian Century 27 Apr 1960) plus Strength to Love draft sermon (S7). Contested (1 against 0), so 0.7. Distinct source ids → corroborated (P48)."
      alternatives:
        - {value: 0, note: "Personal God with feeling and will; nothing placing God in the world (S2, S8).", cites: [{source: S2, locator: "closing section"}, {source: S8, locator: "closing paragraph"}]}
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S5, locator: "Draft of Chapter IV, 'Love in Action', paragraph 'One can only see the greatness of this prayer by contrast'"}, {source: S6, locator: "Draft of Chapter XV, 'The Answer to a Perplexing Question', text between notes 24–25 and 27–28"}, {source: S3, locator: "virgin-birth and resurrection paragraphs; editors' headnote"}, {source: S7, locator: "Draft of Chapter XIII, 'Our God Is Able': moral law 'akin to the laws in the physical world'; 'absolute moral laws' in the structure of the universe"}, {source: S2, locator: "closing: 'loving purpose' / 'cosmic companionship'"}]
      rationale: "Scored on his account of nature (P6), from Strength to Love (Harper & Row, 1963; published in the span), read in the first typed drafts printed by the King Papers, whose notes mark changes in the published text in detail; the notes mark no change here (they are not a full collation: at least one nearby change is unmarked, ca27fcf audit, KK4). The quotes are draft wording. Nature keeps fixed laws: 'She must do everlasting honor to her fixed, immutable laws. When these laws are violated, she has no alternative but to follow inexorably her path of uniformity. Nature does not and cannot forgive.' ('Love in Action'). God does not act on evil by miracle: 'Therefore we must never feel that God will, through some breathtaking miracle or a wave of the hand, cast evil out of the world. As long as we believe this we will pray unanswerable prayers and ask God to do things that he will never do.' and 'No prodigious thunderbolt will come dashing out of the sky to blast evil away.' ('The Answer to a Perplexing Question'). B 3: a lawful nature, with God working through man and history ('The principle which opens the door for God to work through man is faith'), not by intervention. The one exception (P27; free will under P30 #14) is named in the same chapter: 'He has made us persons with freedom, free to choose the good and therefore free to choose what is not good.' (S6, text before note 27, draft wording). Support (P31): the 1949 seminary essay calls a virgin birth 'downright improbable and even impossible' and says 'No laws were broken because they had no knowledge of the existence of law' (S3). S7 also supports the preferred reading: 'a law in the moral world … akin to the laws in the physical world' and 'absolute moral laws' placed 'in the very structure of this universe' (draft; editors mark nearby wording changes but not these claims as dropped). Named alternatives: 4 ('fixed, immutable laws ... path of uniformity'; but he states no exceptionless order for God's own action), and 2 ('a God of Power in the universe who is able to do exceedingly abundant things in nature and history', S7; 'this God both evokes and answers prayers', S2, 1960)."
      how_known: "Jason's ruling (2026-10-19, RQ U1): re-based on in-span Strength to Love sermons (written_profession), 1949 essay as support; two named alternatives, so 0.7. Deepen D1: King Papers editors' published-version notes confirm RQ-KK1 — Love in Action fixed-laws paragraph unmarked (note 6 is the next sentence only); Answer thunderbolt and 'breathtaking miracle' unmarked; free-will and 'exceedingly abundant' wording change in print but same substance (S6 notes 25, 27; STL pp. 123+). Full Harper 1963 volume still not held. Support single→corroborated (P48): S5+S6+S3 plus S7 (physical/moral-law parallel; absolute moral laws) and S2 (loving purpose); alt-exclusive sources folded into main cites."
      alternatives:
        - {value: 4, note: "Nature's 'fixed, immutable laws' and 'path of uniformity'; rejection of miracle as God's way with evil.", cites: [{source: S5, locator: "'One can only see the greatness of this prayer by contrast' paragraph"}, {source: S3, locator: "virgin-birth paragraph"}]}
        - {value: 2, note: "A God 'able to do exceedingly abundant things in nature and history' (1963) who 'answers prayers' (1960).", cites: [{source: S7, locator: "Draft of Chapter XIII, 'Our God Is Able', opening paragraph"}, {source: S2, locator: "closing section"}]}
    C_ledger: {value: UNKNOWN, how_known: "Nothing on reward and punishment of persons in the texts read; 'salvation or doom' (S2, last paragraph) is said of a historical crisis (P19)."}
    D_authority:
      value: 2
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S2, locator: "part I"}, {source: S3, locator: "opening paragraphs; virgin-birth paragraph"}]
      rationale: "Two domains, each with its own authority (P27 anchor). Reason and historical criticism decide fact: liberalism's 'refusal to abandon the best light of reason' and its 'philological-historical criticism of biblical literature' to be 'defended with religious and scientific passion'; neo-orthodoxy's 'narrow, uncritical biblicism' rejected (1960); in 1949 the evidence for the virgin birth is 'to shallow to convince any objective thinker'. Faith keeps its own say over the human condition: 'reason is darkened by sin'; 'Reason, devoid of the purifying power of faith, can never free itself from distortions and rationalizations'; 'the ultimate Christian answer'. Named alternative 3: religion's say may shrink to the spirit behind doctrines once their literal content is given up (1949: 'What ultimately the creed signifies is not words, but spirit', quoting Hedley)."
      how_known: "Published essay in the span, with the 1949 essay in support (P31); contested (2 against 3), so 0.7."
      alternatives:
        - {value: 3, note: "Faith limited to the spirit of the doctrines.", cites: [{source: S3, locator: "opening paragraphs"}]}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Scored on the world's order (P7). Lead only: 'this God both evokes and answers prayers' and 'resources of strength that only God could give' (S2) concern inner strength, not events changed for an in-group; nothing on the same rules for all beings."}
  mid_basin: {value: true, certainty: 0.7, cites: [{source: S2, locator: "closing section"}, {source: S8, locator: "closing paragraph"}, {source: S5, locator: "'Love in Action'"}, {source: S6, locator: "'The Answer to a Perplexing Question'"}, {source: S7, locator: "'Our God Is Able'"}], how_known: "P4 test: A 1 (0.7) ≤ 1 and B 3 (0.7) ≥ 3, both at ≥ 0.7, so true at 0.7 (Jason's ruling on RQ U1, 2026-10-19). Deepen D1: A and B both corroborated (P48) → chart fill hollow→filled. The B 2 alternative would fall between the branches."}
  statements:
    - text: "I am convinced that the universe is under the control of a loving purpose and that in the struggle for righteousness man has cosmic companionship. Behind the harsh appearances of the world there is a benign power. To say God is personal is not to make him an object among other objects or attribute to him the finiteness and limitations of human personality; it is to take what is finest and noblest in our consciousness and firm its perfect existence in him."
      cites: [{source: S2, locator: "closing section"}]
      date: "1960-04-13"
      context: "'How My Mind Has Changed' series, Christian Century; on his growing conviction of 'the reality of a personal God'."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-19
      note: "King Papers transcription of Christian Century 77 (13 April 1960): 439–441."
    - text: "So in the truest sense of the word, God is a living God. In him there is feeling and will, responsive to the deepest yearnings of the human heart: this God both evokes and answers prayers."
      cites: [{source: S2, locator: "closing section"}]
      date: "1960-04-13"
      context: "Same paragraph."
      axes: [A_locus, B_cause, E_scope]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-19
      note: "Basis of the CLTHEI, A 0 and B 2 alternatives."
    - text: "Liberalism failed to see that reason by itself is little more than an instrument to justify man's defensive ways of thinking. Reason, devoid of the purifying power of faith, can never free itself from distortions and rationalizations."
      cites: [{source: S2, locator: "part I"}]
      date: "1960-04-13"
      context: "On what he came to reject in liberal theology; the same section keeps liberalism's 'refusal to abandon the best light of reason'."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-19
    - text: "Christ furnished the spirit and motivation while Gandhi furnished the method."
      cites: [{source: S2, locator: "part II"}]
      date: "1960-04-13"
      context: "On the Montgomery bus boycott."
      axes: []
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-19
    - text: "They were not unscientific in their approach because they had no knowledge of the scientific. They could only express themselves in terms of the pre-scientific thought patterns of their day. No laws were broken because they had no knowledge of the existence of law. They only knew that they had been with the Jesus of history and that his spiritual life was so far beyond theirs that to explain his biological origin as identical with theirs was quite inadequate. We of this scientific age will not explain the birth of Jesus in such unscientific terms, but we will have to admit with the early Christians that the spiritual uniqueness of Jesus stands as a mystery to man."
      cites: [{source: S3, locator: "virgin-birth paragraph"}]
      date: "1949"
      context: "Seminary essay for George W. Davis's course Christian Theology for Today, Crozer, autumn 1949 (dated 13 September – 23 November 1949 with a query by the editors); follows Hedley's The Symbol of the Faith closely."
      axes: [B_cause]
      kind: "unpublished manuscript"
      verified_against: "scholarly edition"
      verified_on: 2026-10-19
      note: "King Papers transcription from the Boston University archive (MLKP-MBU); before the span (P31)."
    - text: "First we must admit that the evidence for the tenability of this doctrine is to shallow to convince any objective thinker."
      cites: [{source: S3, locator: "virgin-birth paragraph"}]
      date: "1949"
      context: "Same essay; on the virgin birth."
      axes: [B_cause, D_authority]
      kind: "unpublished manuscript"
      verified_against: "scholarly edition"
      verified_on: 2026-10-19
      note: "'to shallow' as in the transcription."
    - text: "She must do everlasting honor to her fixed, immutable laws. When these laws are violated, she has no alternative but to follow inexorably her path of uniformity. Nature does not and cannot forgive."
      cites: [{source: S5, locator: "'One can only see the greatness of this prayer by contrast' paragraph"}]
      date: "1963"
      context: "Strength to Love, ch. IV 'Love in Action', contrasting Jesus' prayer of forgiveness with nature, which 'is caught in the finality of its own impersonal structure'."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-19
      note: "Draft wording: the first typed draft (July 1962 – March 1963) as printed by the King Papers; the notes mark no change here (note 6 concerns the next sentence). Printed variant, unconfirmed: 'She must honor everlastingly her fixed, immutable laws, and when these laws are violated she has no alternative except to follow inexorably her path of uniformity' (as paraphrased in the Valdosta Daily Times, 22 Jan 2020, a secondary quotation)."
    - text: "Therefore we must never feel that God will, through some breathtaking miracle or a wave of the hand, cast evil out of the world. As long as we believe this we will pray unanswerable prayers and ask God to do things that he will never do."
      cites: [{source: S6, locator: "text between notes 27 and 28"}]
      date: "1963"
      context: "Strength to Love, ch. XV 'The Answer to a Perplexing Question': evil is cast out neither by God alone nor by man alone, but by both."
      axes: [B_cause, E_scope]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-19
      note: "Draft wording, as printed by the King Papers; the notes mark no change here. The printed text is quoted word for word in secondary sources (e.g. Glover, 'Give And It Will Be Given To You', revjaystuartglover.com). Two sentences later the print reads 'to expect God to do everything while we do nothing' where the draft has 'to trust God with the expectation that he will do everything while we do nothing', a change the notes do not mark (ca27fcf audit, KK4; secondary quotation)."
    - text: "No prodigious thunderbolt will come dashing out of the sky to blast evil away. No mighty army of angels will decend from heaven and force men to do what their wills have led them not to do."
      cites: [{source: S6, locator: "text between notes 24 and 25"}]
      date: "1963"
      context: "Same chapter, on 'the fallacy of the idea that God alone will rid the earth of evil'."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-19
      note: "Draft wording; 'decend' as in the transcription. The notes mark no change here (note 25 concerns only the later phrase 'stands ever ready to give exceedingly abundant things')."
    - text: "The suffering and agonizing moments through which I have passed over the last few years have also drawn me closer to God. More than ever before I am convinced of the reality of a personal God."
      cites: [{source: S8, locator: "closing paragraph"}]
      date: "1960-04-27"
      context: "'Suffering and Faith,' Christian Century; addendum to Pilgrimage published two weeks later."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "King Papers transcription of Christian Century 77 (27 April 1960): 510."
    - text: "There is a law in the moral world,—a silent, invisible imperative—akin to the laws in the physical world, which reminds us that life will only work a certain way. [...] He has placed in the very structure of this universe certain absolute moral laws. No matter how much we try, we cannot defy or break them; if we disobey them, they end up breaking us."
      cites: [{source: S7, locator: "paragraphs on subduing evil / absolute moral laws"}]
      date: "1963"
      context: "Strength to Love, ch. XIII 'Our God Is Able'; God conquers evil through moral order in history."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Draft wording (King Papers); editors' notes mark nearby wording changes in the published text but do not mark these law sentences as dropped or reversed."
  changes_over_life:
    - {value: "Raised 'in a rather strict fundamentalistic tradition'; a 'thoroughgoing liberal' in seminary; then rejected 'mainly the liberal doctrine of man' (Niebuhr), without accepting neo-orthodoxy", certainty: 0.7, cites: [{source: S2, locator: "opening; part I"}], how_known: "His own retrospective account (1960) of 1949–1959 (P29 cap 0.7)."}
    - {value: "A personal God, once 'little more than a metaphysical category', became 'a living reality ... validated in the experiences of everyday life' during the struggle (to 1960)", certainty: 0.7, cites: [{source: S2, locator: "closing section"}], how_known: "His own account; 'I have always believed in the personality of God', so the content is unchanged."}
  coder_notes: "Deepen D1 2026-10-24: A corroborated via Suffering and Faith (S8) + Pilgrimage (S2) + S7 benign Power. B corroborated by folding S7 (physical/moral-law parallel) and S2 (loving purpose) into main cites with S5/S6/S3; alts 4 and 2 retained. RQ-KK1 confirmed against King Papers published-version notes (not a hand-held Harper 1963). Hamilton/Brooks influence note on drafts unchanged (batch U). Leads still: Stride Toward Freedom (1958) full text; dissertation (1955); hand-held 1963 print."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "African American", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Baptist", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1955–1968", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "From the Montgomery bus boycott to his death: one lasting contribution dated as a range (P12, P30), led 'from the mid-1950s until his death' (S1)."}
  age_at_first_lasting_contribution: {value: 26, certainty: 0.7, cites: [{source: S1, locator: "facts box; opening"}], how_known: "1955 − 1929 = 26 (P30)."}
  first_evidence_of_lio_type_views: {value: "1949 seminary essay: a virgin birth 'downright improbable and even impossible' — B 3", year: 1949, certainty: 0.5, cites: [{source: S3, locator: "virgin-birth paragraph"}], how_known: "Earliest source read (P30 #7)."}
  lio_views_relative_to_major_work: {value: "before major work", certainty: 0.5, cites: [{source: S3, locator: "virgin-birth paragraph"}], how_known: "1949, six years before the span; one unpublished essay."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "part I"}], how_known: "Not assessed."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "part I"}], how_known: "Not assessed."}
  circle_present: {value: "unclear", rationale: "'cosmic companionship' and a 'loving purpose' controlling the universe; not assessed further.", certainty: 0.5, cites: [{source: S2, locator: "closing section"}], how_known: "Coder's reading."}
  reading: "A personal God and a loving purpose in the universe, with Christian love worked through Gandhian nonviolence."
  notes: ""

institutions:
  - {value: "Pastorate in Montgomery, Alabama", role: "pastor", years: "1954–", kind: "religious body", certainty: 0.7, cites: [{source: S2, locator: "part II"}], how_known: "'When I went to Montgomery, Alabama, as a pastor in 1954' (S2); the church is not named in the sources read."}
  - {value: "Southern Christian Leadership Conference", role: "head", kind: other, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  - {value: "Ebenezer Baptist Church, Atlanta", role: "minister (his father's church)", kind: "religious body", certainty: 0.5, cites: [{source: S1, locator: "question box 'What was Martin Luther King’s family life like?'"}], how_known: "Britannica question box only; years not stated."}
collaborators:
  - {value: "Benjamin Mays", relation: teacher, note: "Morehouse president and mentor", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  - {value: "George W. Davis", relation: teacher, note: "Crozer professor of Christian theology; set and graded the 1949 essay", certainty: 0.7, cites: [{source: S3, locator: "editors' headnote and note 1"}], how_known: "King Papers editors."}
  - {value: "Mohandas Gandhi", relation: "influenced by", note: "the method of nonviolent resistance", certainty: 1.0, cites: [{source: S1, locator: "'Early years'"}, {source: S2, locator: "part II"}], how_known: "Britannica and his own account."}
  - {value: "Coretta Scott King", relation: family, note: "wife, married 1953", certainty: 0.7, cites: [{source: S1, locator: "question box 'family life'"}], how_known: "Britannica question box."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 116"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "B still quoted from King Papers first typed drafts; RQ-KK1 confirmed via editors' published-version notes (scored loci unmarked or same substance). Full Harper 1963 / Fortress reprint not held in hand."
    - "Britannica's body text was read through 'Early years'; later sections not fetched. Question-box items are cited only for dates."
  open_questions:
    - "Hand-check Love in Action / Answer / Our God Is Able against a physical or borrowable 1963 Harper or Fortress Strength to Love."
    - "Read Stride Toward Freedom (1958) ch. 6 for any A/B wording independent of the Pilgrimage family."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Clayborne Carson (Britannica)"
    citation: "Carson, Clayborne. \"Martin Luther King, Jr.\" Encyclopaedia Britannica (updated 18 October 2026). https://www.britannica.com/biography/Martin-Luther-King-Jr. Read live 2026-10-19."
    url: "https://www.britannica.com/biography/Martin-Luther-King-Jr"
    accessed: 2026-10-19
    reliability_note: "Signed article; fetched text ran through 'Early years'. Question boxes cited for dates only."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, heritage, timing, institutions, collaborators]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Martin Luther King, Jr."
    citation: "King, Martin Luther, Jr. \"Pilgrimage to Nonviolence.\" Christian Century 77 (13 April 1960): 439–441. Transcribed in The Papers of Martin Luther King, Jr. (King Papers Project, Stanford King Institute), online edition."
    url: "https://kinginstitute.stanford.edu/king-papers/documents/pilgrimage-nonviolence"
    accessed: 2026-10-19
    reliability_note: "Scholarly edition transcription with editors' notes; locators by the essay's parts I–III and closing section."
    source_quality: "primary / own words"
    used_for: [worldview, childhood, contribution, timing, lane_b, institutions]
  - id: S3
    type: primary
    kind: "scholarly edition"
    author: "Martin Luther King, Jr.; King Papers Project editors"
    citation: "King, Martin Luther, Jr. \"What Experiences of Christians Living in the Early Christian Century Led to the Christian Doctrines of the Divine Sonship of Jesus, the Virgin Birth, and the Bodily Resurrection.\" Essay, Crozer Theological Seminary, 13 September – 23 November 1949 (queried). MLKP-MBU, Boston University. The Papers of Martin Luther King, Jr., online edition, with editors' headnote and notes."
    url: "https://kinginstitute.stanford.edu/king-papers/documents/what-experiences-christians-living-early-christian-century-led-christian"
    accessed: 2026-10-19
    reliability_note: "Unpublished student essay; the editors note it follows Hedley's The Symbol of the Faith closely and quote Hedley's parallel passages."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview, timing, collaborators]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S5
    type: primary
    kind: "scholarly edition"
    author: "Martin Luther King, Jr.; King Papers Project editors"
    citation: "King, Martin Luther, Jr. \"Draft of Chapter IV, 'Love in Action'.\" July 1962 – March 1963. For Strength to Love (New York: Harper & Row, 1963). MLKP-MBU, Boston University. The Papers of Martin Luther King, Jr., vol. 6, online edition, with editors' notes."
    url: "https://kinginstitute.stanford.edu/king-papers/documents/draft-chapter-iv-love-action"
    accessed: 2026-10-19
    reliability_note: "First typed draft (draft wording); the editors' notes mark changes in the published text in detail but not exhaustively."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview]
  - id: S6
    type: primary
    kind: "scholarly edition"
    author: "Martin Luther King, Jr.; King Papers Project editors"
    citation: "King, Martin Luther, Jr. \"Draft of Chapter XV, 'The Answer to a Perplexing Question'.\" July 1962 – March 1963. For Strength to Love (New York: Harper & Row, 1963). Morehouse College Martin Luther King, Jr. Collection, Robert W. Woodruff Library, Atlanta University Center. The Papers of Martin Luther King, Jr., vol. 6, online edition, with editors' notes."
    url: "https://kinginstitute.stanford.edu/king-papers/documents/draft-chapter-xv-answer-perplexing-question"
    accessed: 2026-10-19
    reliability_note: "First typed draft (draft wording); the editors' notes mark changes in the published text in detail but not exhaustively."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview]
  - id: S7
    type: primary
    kind: "scholarly edition"
    author: "Martin Luther King, Jr.; King Papers Project editors"
    citation: "King, Martin Luther, Jr. \"Draft of Chapter XIII, 'Our God Is Able'.\" July 1962 – March 1963. For Strength to Love (New York: Harper & Row, 1963). The Papers of Martin Luther King, Jr., vol. 6, online edition, with editors' notes."
    url: "https://kinginstitute.stanford.edu/king-papers/documents/draft-chapter-xiii-our-god-able"
    accessed: 2026-10-19
    reliability_note: "First typed draft; used only for the B 2 alternative."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview]
  - id: S8
    type: primary
    kind: "published work by the subject"
    author: "Martin Luther King, Jr."
    citation: "King, Martin Luther, Jr. \"Suffering and Faith.\" Christian Century 77 (27 April 1960): 510. Transcribed in The Papers of Martin Luther King, Jr. (King Papers Project, Stanford King Institute), online edition."
    url: "https://kinginstitute.stanford.edu/king-papers/documents/suffering-and-faith"
    accessed: 2026-10-24
    reliability_note: "Published addendum to Pilgrimage (arrived too late for the 13 April issue); independent Christian Century printing two weeks later. Scholarly edition transcription."
    source_quality: "primary / own words"
    used_for: [worldview, review]
  - id: S9
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia. \"Martin Luther King Jr.\" English Wikipedia. https://en.wikipedia.org/wiki/Martin_Luther_King_Jr. Read live 2026-10-24."
    url: "https://en.wikipedia.org/wiki/Martin_Luther_King_Jr."
    accessed: 2026-10-24
    reliability_note: "Crowdsourced; dual bio (P50) against Britannica. Birth/death and Baptist family align with S1."
    source_quality: "reference entry"
    used_for: [identity, basics, childhood, heritage, review]

---

# Martin Luther King Jr.

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Martin Luther King Jr. (1929–1968), Baptist minister who led the US civil rights movement from the mid-1950s until his death [S1; S9]. Deepen D1: primary_system CHRIST (0.7, alt CLTHEI); A 1 (0.7, corroborated); B 3 (0.7, corroborated; alts 4 and 2); D 2 (0.7, corroborated); mid_basin true (0.7). Chart: dark filled (was dark hollow).

## Life and work

Morehouse, Crozer, Boston University; Montgomery, the SCLC, the March on Washington; Nobel Peace Prize 1964 [S1].

## Contribution and impact

Leadership 'fundamental' to ending legal segregation [S1].

## Childhood and education

Son and grandson of Baptist preachers, raised in 'a rather strict fundamentalistic tradition' [S1, S2].

## Adult working worldview

'More than ever before I am convinced of the reality of a personal God' [S8]; 'this God both evokes and answers prayers' [S2]; nature 'must do everlasting honor to her fixed, immutable laws' [S5]; God will not 'through some breathtaking miracle or a wave of the hand, cast evil out of the world' [S6]; moral laws 'akin to the laws in the physical world' [S7]; in 1949, 'No laws were broken because they had no knowledge of the existence of law' [S3]. A and B both corroborated (P48).

## Heritage (context only)

Baptist, African American [S1].

## Timing

1955–1968, from age 26 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. 'cosmic companionship' [S2].

## Open questions

- Hand-held Strength to Love 1963/Fortress; Stride Toward Freedom (1958) full text.

## Research log

- 2026-10-19: Read Britannica (to 'Early years') and two King Papers documents.
- 2026-10-19: Read the King Papers drafts of Strength to Love chapters IV, XIII and XV (Jason's ruling on RQ U1).
- 2026-10-24: Deepen D1. Suffering and Faith (S8); re-read S5–S7 with published-version notes (RQ-KK1 holds); Wikipedia EN (S9). A/B support single→corroborated; chart hollow→filled.
