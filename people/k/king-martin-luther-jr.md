---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch U)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch U, order P32: F 4, rank 116). Basics from Britannica (David L. Lewis). Worldview from two texts in the King Papers online edition (Stanford King Institute): 'Pilgrimage to Nonviolence' (Christian Century, 13 April 1960; in span) and a 1949 Crozer seminary essay (unpublished; before the span, P31). Not a scientist (P30). primary_system CHRIST (0.7, alt CLTHEI); A 1 (0.7, alt 0); B 3 (0.5, alts 4 and 2; P41, from the 1949 essay); C UNKNOWN; D 2 (0.7, alt 3); E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD (B at 0.5). Plotted (faded). Draft, not reviewed."}

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
    date: {value: "1929-01-15", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "facts box (Born); opening"}], how_known: "Britannica."}
    place: {value: "Atlanta, Georgia", modern_name: "Atlanta, Georgia, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "facts box (Born)"}], how_known: "Britannica."}
  death:
    date: {value: "1968-04-04", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "facts box (Died); opening"}], how_known: "Britannica; assassinated."}
    place: {value: "Memphis, Tennessee", modern_name: "Memphis, Tennessee, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "facts box (Died)"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1955, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "part II"}], how_known: "Leadership of the civil rights movement 'from the mid-1950s' (S1), beginning as spokesman of the Montgomery bus boycott (S2). A range date sets the span start (P12)."}
  era_bucket: {value: "1950 on", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "1955 (P2)."}
  region_of_birth: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "facts box"}], how_known: "United States (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "United States."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Pronouns in Britannica."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  occupations: {value: ["Baptist minister", "civil rights leader", "head of the Southern Christian Leadership Conference"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

contribution:
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
      cites: [{source: S2, locator: "closing section; part I"}]
      rationale: "Transcendent-person pole with limits: 'the reality of a personal God'; 'In him there is feeling and will'; but 'To say God is personal is not to make him an object among other objects', and he faults both liberalism's 'overstress of his immanence' and neo-orthodoxy's God 'hidden, unknown and \"wholly other\"', taking a middle course. Named alternative 0 (a personal God who answers prayer, with no immanence claimed)."
      how_known: "Published essay in the span; contested (1 against 0), so 0.7."
      alternatives:
        - {value: 0, note: "Personal God with feeling and will; nothing placing God in the world.", cites: [{source: S2, locator: "closing section"}]}
    B_cause:
      value: 3
      basis: consistent_private_letters
      certainty: 0.5
      cites: [{source: S3, locator: "virgin-birth and resurrection paragraphs; editors' headnote"}, {source: S2, locator: "closing section"}]
      rationale: "Scored on his account of nature (P6). A non-scientist who rejects a miracle without stating an exceptionless order: B 3 at 0.5, alternative 4 (P41, Tolstoy precedent). In 1949 he calls a virgin birth 'downright improbable and even impossible', says 'No laws were broken because they had no knowledge of the existence of law' and 'We of this scientific age will not explain the birth of Jesus in such unscientific terms', and finds the external evidence for the bodily resurrection 'wanting'. Named alternative 2: in the span (1960) 'the universe is under the control of a loving purpose' and God 'answers prayers', which could be special providence as a live part of how events go."
      how_known: "One unpublished seminary essay (1949), his own words, before the span: it counts under P31 because the 1960 essay documents a change on the doctrine of man and on how real God felt to him ('a metaphysical category' to 'a living reality'), not on miracles. A single unpublished document takes the private ceiling; the King Papers editors back the reading ('King shows himself willing to abandon scriptural literalism', S3 headnote), so 0.5 (P18). The essay 'follows the book's structure and argument closely' (Hedley's The Symbol of the Faith; S3 headnote)."
      alternatives:
        - {value: 4, note: "P41: rejecting a miracle cannot rule out a no-exception nature.", cites: [{source: S3, locator: "virgin-birth paragraph"}]}
        - {value: 2, note: "Answered prayer and a 'loving purpose' controlling the universe (1960).", cites: [{source: S2, locator: "closing section"}]}
    C_ledger: {value: UNKNOWN, how_known: "Nothing on reward and punishment of persons in the texts read; 'salvation or doom' (S2, last paragraph) is said of a historical crisis (P19)."}
    D_authority:
      value: 2
      basis: written_profession
      certainty: 0.7
      cites: [{source: S2, locator: "part I"}, {source: S3, locator: "opening paragraphs; virgin-birth paragraph"}]
      rationale: "Two domains, each with its own authority (P27 anchor). Reason and historical criticism decide fact: liberalism's 'refusal to abandon the best light of reason' and its 'philological-historical criticism of biblical literature' to be 'defended with religious and scientific passion'; neo-orthodoxy's 'narrow, uncritical biblicism' rejected (1960); in 1949 the evidence for the virgin birth is 'to shallow to convince any objective thinker'. Faith keeps its own say over the human condition: 'reason is darkened by sin'; 'Reason, devoid of the purifying power of faith, can never free itself from distortions and rationalizations'; 'the ultimate Christian answer'. Named alternative 3: religion's say may shrink to the spirit behind doctrines once their literal content is given up (1949: 'What ultimately the creed signifies is not words, but spirit', quoting Hedley)."
      how_known: "Published essay in the span, with the 1949 essay in support (P31); contested (2 against 3), so 0.7."
      alternatives:
        - {value: 3, note: "Faith limited to the spirit of the doctrines.", cites: [{source: S3, locator: "opening paragraphs"}]}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Scored on the world's order (P7). Lead only: 'this God both evokes and answers prayers' and 'resources of strength that only God could give' (S2) concern inner strength, not events changed for an in-group; nothing on the same rules for all beings."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "P4 test: A 1 at 0.7 meets A ≤ 1, but B 3 is at 0.5, under the 0.7 bar (P10); the B 2 alternative would fall between the branches."}
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
  changes_over_life:
    - {value: "Raised 'in a rather strict fundamentalistic tradition'; a 'thoroughgoing liberal' in seminary; then rejected 'mainly the liberal doctrine of man' (Niebuhr), without accepting neo-orthodoxy", certainty: 0.7, cites: [{source: S2, locator: "opening; part I"}], how_known: "His own retrospective account (1960) of 1949–1959 (P29 cap 0.7)."}
    - {value: "A personal God, once 'little more than a metaphysical category', became 'a living reality ... validated in the experiences of everyday life' during the struggle (to 1960)", certainty: 0.7, cites: [{source: S2, locator: "closing section"}], how_known: "His own account; 'I have always believed in the personality of God', so the content is unchanged."}
  coder_notes: "Coder's call. The plotted B rests on one pre-span unpublished seminary essay (P31, P41) that follows a textbook closely; the in-span essay gives answered prayer and a 'loving purpose', named as the B 2 alternative. If the 1949 essay is ruled not to count (a documented change under P31, or a course paraphrase), B becomes BELOW_THRESHOLD and he leaves the chart. Leads: Stride Toward Freedom (1958); Strength to Love (1963); the dissertation (1955); his sermons on science and religion. Not read."

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
    - "The plotted B rests on one unpublished pre-span seminary essay that follows Hedley closely (P31, P41); in-span answered prayer is the B 2 alternative."
    - "Britannica's body text was read through 'Early years'; later sections not fetched. Question-box items are cited only for dates."
  open_questions:
    - "Read Strength to Love (1963) and Stride Toward Freedom (1958) for in-span statements on miracles and providence."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "David L. Lewis (Britannica)"
    citation: "Lewis, David L. \"Martin Luther King, Jr.\" Encyclopaedia Britannica (updated 18 October 2026). https://www.britannica.com/biography/Martin-Luther-King-Jr. Read live 2026-10-19."
    url: "https://www.britannica.com/biography/Martin-Luther-King-Jr"
    accessed: 2026-10-19
    reliability_note: "Signed article; fetched text ran through 'Early years'. Question boxes cited for dates only."
    used_for: [identity, basics, contribution, childhood, heritage, timing, institutions, collaborators]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Martin Luther King, Jr."
    citation: "King, Martin Luther, Jr. \"Pilgrimage to Nonviolence.\" Christian Century 77 (13 April 1960): 439–441. Transcribed in The Papers of Martin Luther King, Jr. (King Papers Project, Stanford King Institute), online edition."
    url: "https://kinginstitute.stanford.edu/king-papers/documents/pilgrimage-nonviolence"
    accessed: 2026-10-19
    reliability_note: "Scholarly edition transcription with editors' notes; locators by the essay's parts I–III and closing section."
    used_for: [worldview, childhood, contribution, timing, lane_b, institutions]
  - id: S3
    type: primary
    kind: "scholarly edition"
    author: "Martin Luther King, Jr.; King Papers Project editors"
    citation: "King, Martin Luther, Jr. \"What Experiences of Christians Living in the Early Christian Century Led to the Christian Doctrines of the Divine Sonship of Jesus, the Virgin Birth, and the Bodily Resurrection.\" Essay, Crozer Theological Seminary, 13 September – 23 November 1949 (queried). MLKP-MBU, Boston University. The Papers of Martin Luther King, Jr., online edition, with editors' headnote and notes."
    url: "https://kinginstitute.stanford.edu/king-papers/documents/what-experiences-christians-living-early-christian-century-led-christian"
    accessed: 2026-10-19
    reliability_note: "Unpublished student essay; the editors note it follows Hedley's The Symbol of the Faith closely and quote Hedley's parallel passages."
    used_for: [worldview, timing, collaborators]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Martin Luther King Jr.

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Martin Luther King Jr. (1929–1968), Baptist minister who led the US civil rights movement from the mid-1950s until his death [S1]. Draft: primary_system CHRIST (0.7, alt CLTHEI); A 1 (0.7); B 3 (0.5, alts 4 and 2); D 2 (0.7); mid_basin BELOW_THRESHOLD. Plotted (faded).

## Life and work

Morehouse, Crozer, Boston University; Montgomery, the SCLC, the March on Washington; Nobel Peace Prize 1964 [S1].

## Contribution and impact

Leadership 'fundamental' to ending legal segregation [S1].

## Childhood and education

Son and grandson of Baptist preachers, raised in 'a rather strict fundamentalistic tradition' [S1, S2].

## Adult working worldview

'this God both evokes and answers prayers' [S2]; in 1949, 'No laws were broken because they had no knowledge of the existence of law' [S3].

## Heritage (context only)

Baptist, African American [S1].

## Timing

1955–1968, from age 26 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. 'cosmic companionship' [S2].

## Open questions

- Strength to Love (1963), Stride Toward Freedom (1958).

## Research log

- 2026-10-19: Read Britannica (to 'Early years') and two King Papers documents.
