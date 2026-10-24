---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch H)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch H, order P32: F 5, rank 50). Basics from Britannica (Morson). Worldview from The Kingdom of God Is Within You (preface dated 1893), Garnett translation, Gutenberg #4602 (web copy, 0.7 cap). Not a scientist (P30). primary_system CHRIST 0.5 (alt DEISM); A 2 at 0.7 (alt 3); B 3 at 0.5 (alt 4) under P41 by analogy (rejects miracles without stating exceptionless law); C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD. Plotted (faded). Ruling question RQ1 batch H. Draft, not reviewed."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Batch H audit (cae9cb2, run 1: hold): B 3 at 0.5 (alt 4) now cites the P41 extension for miracle rejection instead of an analogy. No value changes."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #50). Needs: A single source; B single source; B faded. Read A Confession (Maude via CCEL, S4) and My Religion / What I Believe (Huntington Smith, S5); dual-sourced bio via Wikipedia EN (S6). P47 source_quality on S1–S6. P48: A support single→corroborated (S2+S4; alt 3); B support single→corroborated (S2+S4+S5; P41, alt 4). Values/certainties unchanged. first_evidence_of_lio_type_views → 1882; lio_views_relative → during major work. Native name filled. Chart-moving YES: faded hollow → faded filled. No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: tolstoy-leo
  display_name: "Leo Tolstoy"
  roster:
    canonical_name: "Leo Tolstoy"
    rank: 50
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: literature
    field_bucket: literature
  full_name: {value: "Count Lev Nikolayevich Tolstoy", certainty: 1.0, cites: [{source: S1, locator: "header ('Also known as')"}, {source: S6, locator: "lead"}], how_known: "Britannica + Wikipedia EN."}
  native_name: {value: "Лев Николаевич Толстой", certainty: 0.7, cites: [{source: S6, locator: "lead"}], how_known: "Wikipedia EN lead (Russian); single non-primary source → 0.7 (P15)."}
  aliases:
    - {name: "Leo Tolstoi", kind: transliteration}

basics:
  birth:
    date: {value: "1828-08-28", calendar: julian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "lead (O.S. 28 August)"}], how_known: "Britannica: 'August 28 [September 9, New Style], 1828'; Wikipedia agrees O.S. 28 August / N.S. 9 September. Russia used the Julian calendar, so the source date is kept as julian. Dual source → 1.0."}
    place: {value: "Yasnaya Polyana, Tula province, Russian Empire", modern_name: "Yasnaya Polyana, Russia", polity_then: "Russian Empire", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "lead; Early life"}], how_known: "Britannica + Wikipedia EN."}
  death:
    date: {value: "1910-11-07", calendar: julian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "lead (O.S. 7 November)"}], how_known: "Britannica: 'November 7 [November 20], 1910'; Wikipedia agrees O.S. 7 November / N.S. 20 November. Dual source → 1.0."}
    place: {value: "Astapovo, Ryazan province", modern_name: "Lev Tolstoy, Lipetsk oblast, Russia", polity_then: "Russian Empire", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "Death"}], how_known: "Britannica and Wikipedia give Astapovo; the modern name Lev Tolstoy (Lipetsk) is the coder's reading of the renamed station town (0.7)."}
  first_lasting_contribution_year: {value: 1852, certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}, {source: S6, locator: "Career and novels"}], how_known: "Childhood (Detstvo), his first published work (P13); Wikipedia agrees."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "From 1852 (P2)."}
  region_of_birth: {value: "Eastern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Russia is Eastern Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Eastern Europe", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Yasnaya Polyana, 'where he was to live the better part of his life and write his most-important works'."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [Russian], certainty: 1.0, cites: [{source: S2, locator: "title page ('Translated from the Russian')"}, {source: S6, locator: "lead"}], how_known: "Gutenberg title page + Wikipedia."}
  occupations: {value: ["novelist", "moral and religious teacher"], certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "lead"}], how_known: "Britannica + Wikipedia."}

contribution:
  fields: {value: ["literature", "religious and moral thought"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Childhood (Detstvo)", year: 1852, kind: work, lasting: "first published work (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
    - {value: "War and Peace", year: 1869, kind: work, lasting: "'among the finest novels ever written' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica: 1865–69; completion year used."}
    - {value: "Anna Karenina", year: 1877, kind: work, lasting: "(S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica: 1875–77."}
    - {value: "A Confession", year: 1882, kind: work, lasting: "account of the crisis and return to faith that opens the late religious period (S4)", certainty: 0.7, cites: [{source: S4, locator: "title page / ch. I; front matter ('First distributed in Russia in 1882')"}], how_known: "Maude Confession via CCEL; front matter dates first Russian distribution 1882."}
    - {value: "The Death of Ivan Ilyich", year: 1886, kind: work, lasting: "'among the best examples of the novella' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    - {value: "The Kingdom of God Is Within You (doctrine of nonresistance)", year: 1893, kind: work, lasting: "influenced Gandhi (S1)", certainty: 0.5, cites: [{source: S2, locator: "preface, dated 'May 14/26, 1893'"}, {source: S1, locator: "opening (nonresistance; Gandhi)"}], how_known: "The preface date is from the Gutenberg text; Britannica names the doctrine, not this book (0.5)."}
  evidence_of_impact:
    - {value: "'one of the world's greatest novelists'; nonresistance influenced Gandhi", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Mother Mariya Nikolayevna, née Princess Volkonskaya (d. before he was two); father Count Nikolay Ilich Tolstoy (d. 1837)", role: parents, certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  household_circumstances: {value: "Aristocratic estate; orphaned young and raised by relatives, later an aunt in Kazan", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  schooling:
    - {value: "University (left in 1847 without a degree)", stage: university, run_by: "state or municipal", years: "–1847", ages: "–19", certainty: 0.5, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica names no university in the passage read; run_by is the coder's reading (0.5)."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "Cousin Tatyana Aleksandrovna Yergolskaya ('Aunt Toinette'), remembered as the greatest influence on his childhood", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica (his own recollection)."}
  languages_in_childhood: {value: TODO}
  notable_events:
    - {value: "Father died", year: 1837, age: 9, certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1852–1893", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "Christian teaching is 'a guide for the whole of our life'; men of 'what is falsely called science' wrongly reduce it to its dogmas and miracles and think it outgrown.", certainty: 0.7, cites: [{source: S2, locator: "Gutenberg ch. IV"}], how_known: "Published book in a web copy, 0.7 cap."}
  primary_system:
    value: CHRIST
    basis: written_profession
    certainty: 0.5
    cites: [{source: S2, locator: "Gutenberg chs. III–IV"}, {source: S4, locator: "chs. IX, XI–XII"}, {source: S5, locator: "chs. I–II"}]
    rationale: "Holds to 'the Christian teaching' as a 'divine view of life' (S2) and lives only when he 'believed in God' (S4), but treats miracles and the dogma that 'Christ was God' as later obscurings (S2) and sets church miracle-holidays and literal Eucharist aside (S4). A non-church, non-dogmatic Christianity. Named alternative: DEISM (if his reading counts as rejecting revelation, P27); he does not say revelation is rejected, so CHRIST at 0.5."
    how_known: "Kingdom (Garnett, Gutenberg #4602); Confession (Maude, CCEL); My Religion (Huntington Smith). TODO: Jubilee edition mapping."
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Chosen at 0.5: 'the Christian teaching' as the divine view of life; Confession seeks God and Christ's teaching."}
    - {code: DEISM, reason: "Alternative: rejects miracles and Christ's divinity; P27 needs a stated rejection of revelation, not read."}
  lio_axes:
    A_locus:
      value: 2
      basis: written_profession
      certainty: 0.7
      cites: [{source: S2, locator: "Gutenberg ch. IV (the divine theory of life)"}, {source: S4, locator: "ch. IX ('infinite god… divinity of the soul… connexion of human affairs with God'); ch. XI (seeking God)"}]
      support: corroborated
      how_known: "Two independent published works in web translations (Kingdom S2; Confession S4). Published writing, 0.7 cap. P48 corroborated."
      rationale: "Mixed: God is 'the eternal undying source of life' and 'the principle of the whole', in whose life man can merge his life (impersonal, world-pervading), yet God has a 'will' to be fulfilled and is 'the Father' (personal) (S2). Confession names 'an infinite god, the divinity of the soul, the connexion of human affairs with God' and that he 'only lived at those times when I believed in God' (S4). Named alternative: 3 (leaning to God as the principle of the whole)."
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.5
      cites: [{source: S2, locator: "Gutenberg ch. III (miracles as later additions)"}, {source: S4, locator: "ch. XI ('no miracles can prove His existence'); ch. XIV (miracles as fables)"}, {source: S5, locator: "chs. VIII–IX (resurrection as superstition; demand for miracles)"}]
      support: corroborated
      how_known: "Three independent published works (Kingdom S2; Confession S4; My Religion S5). Not a scientist (P30). 0.5 under P41 (miracle-rejection extension). P48 corroborated."
      rationale: "Scored on his account of nature (P6, P16): miracles are not part of the true doctrine; 'the more the understanding of Christ's teaching was obscured, the more the miraculous was introduced into it' and 'Christ was God had to be proved by miracles completely beyond our comprehension' (S2). Confession: God 'does not exist, and no miracles can prove His existence, because the miracles would be my imagination, besides being irrational'; later 'Putting aside the miracles and regarding them as fables' (S4). My Religion: those who 'demand of Jesus that he shall work miracles' never realize faith in life; personal resurrection is a 'superstition' he denies (S5). He rejects miracles but states no exceptionless order of nature, so B 3 at 0.5 with 4 as the named alternative under P41 (extension of 2026-10-15: P41 also covers non-scientists who reject miracles or intervention without stating an exceptionless order)."
    C_ledger: {value: UNKNOWN, how_known: "Not read with this in view; the doctrine's lack of 'threats of punishment' (Kingdom ch. III) is about the teaching's method, not reward and punishment by God."}
    D_authority: {value: UNKNOWN, how_known: "Nothing read that sets revelation against observation."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A 2 is neither ≤ 1 nor ≥ 3, and B is at 0.5, below the test's 0.7 bar (§6, P19). P48: both A and B corroborated → filled; darkness faded (min cert 0.5)."}
  statements:
    - text: "The man who holds the divine theory of life recognizes life not in his own individuality, and not in societies of individualities [...] but in the eternal undying source of life--in God; and to fulfill the will of God he is ready to sacrifice his individual and family and social welfare. The motor power of his life is love. And his religion is the worship in deed and in truth of the principle of the whole--God."
      cites: [{source: S2, locator: "Gutenberg ch. IV"}]
      date: "1893"
      context: "On the three conceptions of life (individual, social, divine)."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Garnett translation (1894) via Gutenberg #4602; web copy, 0.7 cap. Re-checked 2026-10-24 against Gutenberg plain text. TODO: Jubilee edition mapping."
    - text: "The conception of an infinite god, the divinity of the soul, the connexion of human affairs with God, the unity and existence of the soul, man's conception of moral goodness and evil — are conceptions formulated in the hidden infinity of human thought, they are those conceptions without which neither life nor I should exist"
      cites: [{source: S4, locator: "ch. IX"}]
      date: "1882"
      context: "On the answers given by faith after the crisis."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Aylmer Maude translation via CCEL PDF; web copy, 0.7 cap."
    - text: "I remembered that I only lived at those times when I believed in God. As it was before, so it was now; I need only be aware of God to live; I need only forget Him, or disbelieve Him, and I died."
      cites: [{source: S4, locator: "ch. XI"}]
      date: "1882"
      context: "Wood in early spring; seeking God after despair."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Maude via CCEL."
    - text: "The more the understanding of Christ's teaching was obscured, the more the miraculous was introduced into it"
      cites: [{source: S2, locator: "Gutenberg ch. III"}]
      date: "1893"
      context: "After 'the proposition that Christ was God had to be proved by miracles completely beyond our comprehension'."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Gutenberg #4602; re-checked 2026-10-24. TODO: printed-edition mapping."
    - text: "He does not exist, and no miracles can prove His existence, because the miracles would be my imagination, besides being irrational."
      cites: [{source: S4, locator: "ch. XI"}]
      date: "1882"
      context: "Interior dialogue while seeking God; rejects miracle-proofs of God's existence."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Maude via CCEL."
    - text: "Putting aside the miracles and regarding them as fables illustrating thoughts, this reading revealed to me life's meaning."
      cites: [{source: S4, locator: "ch. XIV"}]
      date: "1882"
      context: "Reading Lives of holy men after church rites (including miracle-holidays) had become a stumbling-block."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Maude via CCEL."
    - text: "In men who demand of Jesus that he shall work miracles we may recognize a desire to believe in his doctrine; but this desire never can be realized in life, however arduous the efforts to obtain it."
      cites: [{source: S5, locator: "ch. IX"}]
      date: "1884"
      context: "On faith vs. miracle-seeking; ch. VIII treats personal resurrection as a superstition foreign to Jesus' teaching."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Huntington Smith translation (My Religion = What I Believe) via theanarchistlibrary.org web copy."
  changes_over_life: []
  coder_notes: "Deepen D1 (queue #50): A support single→corroborated (S2 Kingdom + S4 Confession); B support single→corroborated (S2+S4+S5 My Religion; P41 keeps 0.5, alt 4). Not a scientist (P30). No exceptionless natural-law wording found for B 4. primary_system stays CHRIST 0.5 (alt DEISM). first_evidence_of_lio → 1882 (Confession). Chart: faded hollow → faded filled (fill cue; darkness min(A,B)=0.5). C/D/E still UNKNOWN. Jubilee Russian edition unread. No fallacy_catalog (Jason 2026-10-24)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Russian aristocracy", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1852–1893", certainty: 0.5, cites: [{source: S1, locator: "opening; 'Early years'"}, {source: S2, locator: "preface date"}, {source: S4, locator: "front matter 1882"}], how_known: "1852 to 1893, first to last listed lasting contribution (P29, P30); the 1893 entry is at 0.5."}
  age_at_first_lasting_contribution: {value: 24, certainty: 0.7, cites: [{source: S1, locator: "opening; 'Early years'"}], how_known: "1852 − 1828 = 24 (P30)."}
  first_evidence_of_lio_type_views: {value: "1882", certainty: 0.7, cites: [{source: S4, locator: "chs. IX, XI (God; miracles)"}], how_known: "A Confession (first Russian distribution 1882) states infinite God and rejects miracle-proofs; earlier novels not scored for LIO."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.7, cites: [{source: S4, locator: "1882"}, {source: S2, locator: "1893"}], how_known: "1882 and 1893 fall inside 1852–1893."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Not read for the novel years (1852–1877); scored texts are the late religious works."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Nothing on mathematics.", certainty: 0.5, cites: [{source: S1, locator: "'Early years'"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "'Early years'"}], how_known: "Nothing read."}
  circle_present: {value: "unclear", rationale: "God as source and principle of the whole; miracles rejected; no statement on natural law.", certainty: 0.5, cites: [{source: S2, locator: "chs. III–IV"}, {source: S4, locator: "chs. IX, XI"}], how_known: "Coder's reading."}
  reading: "A late, non-dogmatic Christianity: God as the source of life, no miracles."
  notes: "Belief model only. Chart cue after D1: faded filled (A 2 @ 0.7 corr; B 3 @ 0.5 corr)."

institutions: []
collaborators: []

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 50"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags: []
  open_questions:
    - "Map Kingdom / Confession / My Religion quotes to the Jubilee (Polnoe sobranie sochinenii) Russian edition."
    - "No explicit no-exception / miracle-denial-of-nature wording found for B 4; P41 keeps B at 0.5."
    - "Family religion / Orthodox baptism details still TODO."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Gary Saul Morson"
    citation: "Morson, Gary Saul. \"Leo Tolstoy.\" Encyclopaedia Britannica, updated 5 September 2026. https://www.britannica.com/biography/Leo-Tolstoy."
    url: "https://www.britannica.com/biography/Leo-Tolstoy"
    accessed: 2026-10-24
    reliability_note: "Signed article body (opening and 'Early years'); the Top Questions box is not used."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, heritage, timing, lane_b]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Leo Tolstoy"
    year: 1893
    citation: "Tolstoy, Leo. \"The Kingdom of God Is Within You\": Christianity Not as a Mystic Religion but as a New Theory of Life. Trans. Constance Garnett. New York, 1894. Project Gutenberg eBook #4602."
    url: "https://www.gutenberg.org/ebooks/4602"
    accessed: 2026-10-24
    reliability_note: "Translation in an unofficial web copy; §7 cap 0.7. Re-checked 2026-10-24."
    source_quality: "unofficial web copy"
    used_for: [basics, contribution, worldview, timing, lane_b]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "Leo Tolstoy"
    year: 1882
    citation: "Tolstoy, Leo. A Confession. Trans. Aylmer Maude. First distributed in Russia in 1882. Christian Classics Ethereal Library (CCEL) text/PDF."
    url: "https://www.ccel.org/ccel/tolstoy/confession.html"
    accessed: 2026-10-24
    reliability_note: "Standard Maude English translation in an unofficial web copy; §7 cap 0.7. Front matter dates first Russian distribution 1882."
    source_quality: "unofficial web copy"
    used_for: [contribution, worldview, timing, lane_b]
  - id: S5
    type: primary
    kind: "published work by the subject"
    author: "Leo Tolstoy"
    year: 1884
    citation: "Tolstoy, Leo. My Religion (What I Believe). Trans. Huntington Smith. New York: Thomas Y. Crowell & Co., 1885. Text via theanarchistlibrary.org."
    url: "https://theanarchistlibrary.org/library/leo-tolstoy-my-religion"
    accessed: 2026-10-24
    reliability_note: "Huntington Smith translation in an unofficial web copy; §7 cap 0.7. Alternate title What I Believe (В чём моя вера?)."
    source_quality: "unofficial web copy"
    used_for: [worldview]
  - id: S6
    type: secondary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "\"Leo Tolstoy.\" Wikipedia, The Free Encyclopedia. https://en.wikipedia.org/wiki/Leo_Tolstoy."
    url: "https://en.wikipedia.org/wiki/Leo_Tolstoy"
    accessed: 2026-10-24
    reliability_note: "Used only to dual-source identity/basics (native name, O.S./N.S. birth and death) already in Britannica; not used for worldview coding."
    source_quality: "other"
    used_for: [identity, basics]
---

# Leo Tolstoy

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`. Worldview CHRIST 0.5; A 2 @ 0.7 corroborated; B 3 @ 0.5 corroborated (P41); C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD. Chart: faded filled (D1 2026-10-24).

## Summary

Leo Tolstoy (1828–1910), Russian novelist and religious teacher: War and Peace, Anna Karenina, A Confession, The Kingdom of God Is Within You [S1; S4; S2]. Deepen D1 (P47–P50): primary_system CHRIST 0.5 (alt DEISM); A 2 @ 0.7 written_profession, support corroborated (S2+S4; alt 3); B 3 @ 0.5 written_profession, support corroborated (S2+S4+S5; P16/P41, alt 4); C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD. Chart: faded hollow → faded filled (fill cue; darkness min(A,B)=0.5).

## Life and work

Yasnaya Polyana; army in the Caucasus and Crimea; novels; later a moral and religious teacher [S1; S6]. Native name Лев Николаевич Толстой [S6].

## Contribution and impact

Childhood (1852), War and Peace, Anna Karenina, A Confession (1882), Ivan Ilyich, nonresistance / Kingdom of God (1893) [S1; S4; S2].

## Childhood and education

Orphaned young; raised by relatives [S1].

## Adult working worldview

God is 'the eternal undying source of life' and 'the principle of the whole' [S2]; Confession names an 'infinite god' and the 'connexion of human affairs with God' [S4]. Miracles are later obscurings of Christ's teaching [S2]; Confession rejects miracle-proofs of God and treats miracle stories as fables [S4]; My Religion rejects miracle-seeking and personal-resurrection superstition [S5]. No exceptionless natural-law wording read (P41 → B 3 @ 0.5).

## Heritage (context only)

Russian aristocracy [S1].

## Timing

First lasting contribution 1852, at 24 [S1]. First LIO-type evidence read: A Confession, 1882 (during major work) [S4].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Unclear geometric form; circle unclear (God as source/principle; miracles rejected; no natural-law statement) [S2; S4].

## Open questions

- Jubilee Russian edition mapping for Kingdom / Confession / My Religion.
- No explicit no-exception claim for B 4 (P41 keeps 0.5).
- Family religion / baptism still TODO.

## Research log

- 2026-10-15: Read Britannica (Morson) and The Kingdom of God Is Within You (Gutenberg #4602), chs. III–IV.
- 2026-10-24 (deepen D1, queue #50): Re-checked Kingdom Gutenberg plain text (chs. III–IV). Read A Confession (Maude, CCEL PDF) chs. IX, XI, XIV. Read My Religion / What I Believe (Huntington Smith) for miracle-seeking and resurrection passages. Dual-sourced bio via Wikipedia EN (native name; O.S./N.S. dates). P47 source_quality on S1–S6. P48 A and B support single→corroborated. Chart-moving YES: faded hollow → faded filled. Jubilee edition still unread. No fallacy_catalog (Jason).
