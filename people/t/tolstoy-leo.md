---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch H)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-15
  change_log:
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch H, order P32: F 5, rank 50). Basics from Britannica (Morson). Worldview from The Kingdom of God Is Within You (preface dated 1893), Garnett translation, Gutenberg #4602 (web copy, 0.7 cap). Not a scientist (P30). primary_system CHRIST 0.5 (alt DEISM); A 2 at 0.7 (alt 3); B 3 at 0.5 (alt 4) under P41 by analogy (rejects miracles without stating exceptionless law); C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD. Plotted (faded). Ruling question RQ1 batch H. Draft, not reviewed."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Batch H audit (cae9cb2, run 1: hold): B 3 at 0.5 (alt 4) now cites the P41 extension for miracle rejection instead of an analogy. No value changes."}

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
  full_name: {value: "Count Lev Nikolayevich Tolstoy", certainty: 0.7, cites: [{source: S1, locator: "header ('Also known as')"}], how_known: "Britannica."}
  native_name: {value: UNKNOWN, how_known: "Cyrillic form not recorded in the source read."}
  aliases:
    - {name: "Leo Tolstoi", kind: transliteration}

basics:
  birth:
    date: {value: "1828-08-28", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica: 'August 28 [September 9, New Style], 1828'; Russia used the Julian calendar, so the source date is kept as julian."}
    place: {value: "Yasnaya Polyana, Tula province, Russian Empire", modern_name: "Yasnaya Polyana, Russia", polity_then: "Russian Empire", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "1910-11-07", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica: 'November 7 [November 20], 1910'; Julian."}
    place: {value: "Astapovo, Ryazan province", modern_name: "Lev Tolstoy, Lipetsk oblast, Russia", polity_then: "Russian Empire", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Britannica gives Astapovo; the modern name is the coder's (not in the source), so 0.5."}
  first_lasting_contribution_year: {value: 1852, certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Childhood (Detstvo), his first published work (P13)."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "From 1852 (P2)."}
  region_of_birth: {value: "Eastern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Russia is Eastern Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Eastern Europe", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Yasnaya Polyana, 'where he was to live the better part of his life and write his most-important works'."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [Russian], certainty: 0.7, cites: [{source: S2, locator: "title page ('Translated from the Russian')"}], how_known: "Gutenberg title page."}
  occupations: {value: ["novelist", "moral and religious teacher"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

contribution:
  fields: {value: ["literature", "religious and moral thought"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Childhood (Detstvo)", year: 1852, kind: work, lasting: "first published work (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
    - {value: "War and Peace", year: 1869, kind: work, lasting: "'among the finest novels ever written' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica: 1865–69; completion year used."}
    - {value: "Anna Karenina", year: 1877, kind: work, lasting: "(S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica: 1875–77."}
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
  self_described_science_religion_relation: {value: "Christian teaching is 'a guide for the whole of our life'; men of 'what is falsely called science' wrongly reduce it to its dogmas and miracles and think it outgrown.", certainty: 0.7, cites: [{source: S2, locator: "Gutenberg ch. IV (line-free web text; TODO map to a printed edition)"}], how_known: "Published book in a web copy, 0.7 cap."}
  primary_system:
    value: CHRIST
    basis: written_profession
    certainty: 0.5
    cites: [{source: S2, locator: "Gutenberg chs. III–IV"}]
    rationale: "Holds to 'the Christian teaching' as a 'divine view of life', but treats miracles and the dogma that 'Christ was God' as later obscurings of the doctrine, which needs no proof but its truth (S2). A non-church, non-dogmatic Christianity. Named alternative: DEISM (if his reading counts as rejecting revelation, P27); he does not say revelation is rejected, so CHRIST at 0.5."
    how_known: "Gutenberg #4602 (Garnett, 1894); TODO: map to a printed edition (Jubilee edition vol. 28)."
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Chosen at 0.5: 'the Christian teaching' as the divine view of life."}
    - {code: DEISM, reason: "Alternative: rejects miracles and Christ's divinity; P27 needs a stated rejection of revelation, not read."}
  lio_axes:
    A_locus:
      value: 2
      basis: written_profession
      certainty: 0.7
      cites: [{source: S2, locator: "Gutenberg ch. IV (the divine theory of life)"}]
      how_known: "Published book in a web copy, 0.7 cap; alternative named."
      rationale: "Mixed: God is 'the eternal undying source of life' and 'the principle of the whole', in whose life man 'can merge his life' (impersonal, world-pervading), yet God has a 'will' to be fulfilled and is 'the Father' (personal). Named alternative: 3 (leaning to God as the principle of the whole)."
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.5
      cites: [{source: S2, locator: "Gutenberg ch. III (miracles as later additions)"}]
      how_known: "Published book in a web copy; 0.5 under P41 (miracle-rejection extension)."
      rationale: "Scored on his account of nature (P6, P16): miracles are not part of the true doctrine; 'the more the understanding of Christ's teaching was obscured, the more the miraculous was introduced into it'. He rejects miracles but states no exceptionless order of nature, so B 3 at 0.5 with 4 as the named alternative under P41 (extension of 2026-10-15: P41 also covers non-scientists who reject miracles or intervention without stating an exceptionless order)."
    C_ledger: {value: UNKNOWN, how_known: "Not read with this in view; the doctrine's lack of 'threats of punishment' (ch. III) is about the teaching's method, not reward and punishment by God."}
    D_authority: {value: UNKNOWN, how_known: "Nothing read that sets revelation against observation."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A 2 is neither ≤ 1 nor ≥ 3, and B is at 0.5, below the test's 0.7 bar (§6, P19)."}
  statements:
    - text: "The man who holds the divine theory of life recognizes life not in his own individuality, and not in societies of individualities [...] but in the eternal undying source of life--in God; and to fulfill the will of God he is ready to sacrifice his individual and family and social welfare. The motor power of his life is love. And his religion is the worship in deed and in truth of the principle of the whole--God."
      cites: [{source: S2, locator: "Gutenberg ch. IV"}]
      date: "1893"
      context: "On the three conceptions of life (individual, social, divine)."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "Garnett translation (1894) via Gutenberg #4602; web copy, 0.7 cap. TODO: map to a printed edition."
    - text: "The more the understanding of Christ's teaching was obscured, the more the miraculous was introduced into it"
      cites: [{source: S2, locator: "Gutenberg ch. III"}]
      date: "1893"
      context: "After 'the proposition that Christ was God had to be proved by miracles completely beyond our comprehension'."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "Gutenberg #4602; TODO: printed-edition mapping."
  changes_over_life: []
  coder_notes: "Coder's call: one late religious book read; his A Confession and What I Believe were not read. The scored worldview is that of the 1893 book; whether it held during the novels (1852–1877) is not established from the sources read, which is why working_years is at 0.5. RQ1 (batch H) was ruled by the P41 extension; codes unchanged."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Russian aristocracy", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1852–1893", certainty: 0.5, cites: [{source: S1, locator: "opening; 'Early years'"}, {source: S2, locator: "preface date"}], how_known: "1852 to 1893, first to last listed lasting contribution (P29, P30); the 1893 entry is at 0.5."}
  age_at_first_lasting_contribution: {value: 24, certainty: 0.7, cites: [{source: S1, locator: "opening; 'Early years'"}], how_known: "1852 − 1828 = 24 (P30)."}
  first_evidence_of_lio_type_views: {value: "1893", certainty: 0.5, cites: [{source: S2, locator: "Gutenberg ch. III"}], how_known: "Earliest work read; earlier religious works not read."}
  lio_views_relative_to_major_work: {value: "after major work", certainty: 0.5, cites: [{source: S2, locator: "preface date"}], how_known: "Read only in the 1893 book, after the novels; earlier views not read."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Not read for the novel years."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Nothing on mathematics.", certainty: 0.5, cites: [{source: S1, locator: "'Early years'"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "'Early years'"}], how_known: "Nothing read."}
  circle_present: {value: "unclear", rationale: "God as source and principle of the whole; miracles rejected; no statement on natural law.", certainty: 0.5, cites: [{source: S2, locator: "chs. III–IV"}], how_known: "Coder's reading."}
  reading: "A late, non-dogmatic Christianity: God as the source of life, no miracles."
  notes: ""

institutions: []
collaborators: []

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 50"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags: []
  open_questions:
    - "Read A Confession and What I Believe; map the Kingdom of God quotes to the Jubilee edition."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Gary Saul Morson"
    citation: "Morson, Gary Saul. \"Leo Tolstoy.\" Encyclopaedia Britannica, updated 5 September 2026. https://www.britannica.com/biography/Leo-Tolstoy."
    url: "https://www.britannica.com/biography/Leo-Tolstoy"
    accessed: 2026-10-15
    reliability_note: "Signed article body (opening and 'Early years'); the Top Questions box is not used."
    used_for: [identity, basics, contribution, childhood, heritage, timing, lane_b]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Leo Tolstoy"
    year: 1893
    citation: "Tolstoy, Leo. \"The Kingdom of God Is Within You\": Christianity Not as a Mystic Religion but as a New Theory of Life. Trans. Constance Garnett. New York, 1894. Project Gutenberg eBook #4602."
    url: "https://www.gutenberg.org/ebooks/4602"
    accessed: 2026-10-15
    reliability_note: "Translation in an unofficial web copy; §7 cap 0.7."
    used_for: [basics, contribution, worldview, timing, lane_b]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Leo Tolstoy

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Leo Tolstoy (1828–1910), Russian novelist and religious teacher: War and Peace, Anna Karenina [S1]. Draft: primary_system CHRIST 0.5; A 2 at 0.7; B 3 at 0.5 (P41); C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD. Plotted (faded).

## Life and work

Yasnaya Polyana; army in the Caucasus and Crimea; novels; later a moral and religious teacher [S1].

## Contribution and impact

Childhood (1852), War and Peace, Anna Karenina, Ivan Ilyich, nonresistance [S1, S2].

## Childhood and education

Orphaned young; raised by relatives [S1].

## Adult working worldview

God is 'the eternal undying source of life' and 'the principle of the whole'; miracles are later obscurings of Christ's teaching [S2].

## Heritage (context only)

Russian aristocracy [S1].

## Timing

First lasting contribution 1852, at 24 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Unclear [S2].

## Open questions

- A Confession; What I Believe.

## Research log

- 2026-10-15: Read Britannica (Morson) and The Kingdom of God Is Within You (Gutenberg #4602), chs. III–IV.
