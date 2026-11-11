---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch H)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to 19c. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch H, order P32: F 5, rank 53). Basics from Britannica (Budden), signed body only (work years given only in the Top Questions box are not used). Worldview from letters in Nohl's collection, Lady Wallace's translation, Gutenberg #13065 (web copy, 0.7 cap): Heiligenstadt document 1802, letter to Zmeskall 1813. Not a scientist (P30). primary_system BELOW_THRESHOLD (candidates CHRIST, CLTHEI, DEISM); A 0 at 0.7 (alt 1); B BELOW_THRESHOLD (Providence statements are about his life, not nature, P16); C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD. Not plotted. No datable lasting contribution in the signed body read (P39). Draft, not reviewed."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Batch H audit (cae9cb2, run 1: hold; note on timing): signed Britannica sections re-checked; no dated lasting work is citable, so the timing fields stay UNKNOWN. No value changes."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #53, F5 rank 53). Needs: A single source; B BELOW_THRESHOLD. P47 source_quality on S1–S7. Corroborated A via German Wikisource Heiligenstädter Testament (S4, Gottheit/Vorsehung) and independent EN Wikisource translation (S5) alongside Wallace Gutenberg S2; A stays 0 @ 0.7, support single→corroborated (P48); alt 1 retained. Gutenberg vol. 2 (S6) letter 300 to Archduke Rudolph 18 July 1821 (Providence / humanity, God, and Nature) added as further A stream — still own-life Providence, not nature's order (P16). B stays BELOW_THRESHOLD under P16 (temple of Nature = joy locus; Humanity/God/Nature letter = duties + rescue from tribulations; forest Holy! quotes and Sturm markings unread as law-vs-exception statements). Dual-source bio via Wikipedia EN (S7): Catholic baptism St Remigius; Op. 1 1795; First Symphony 1800; timing filled. Chart-moving NO (B still BELOW; still unplotted). Anderson Letters / Solomon Tagebuch / Sturm annotations unread. No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: van-beethoven-ludwig
  display_name: "Ludwig van Beethoven"
  roster:
    canonical_name: "Ludwig van Beethoven"
    rank: 53
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: music
    field_bucket: music
  full_name: {value: "Ludwig van Beethoven", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  native_name: {value: "Ludwig van Beethoven", certainty: 0.7, cites: [{source: S7, locator: "opening"}], how_known: "German; same Latin-script form (Wikipedia)."}
  aliases: []

basics:
  birth:
    date: {value: UNKNOWN, how_known: "No authentic birth record; baptism 17 December 1770 at Catholic Parish of St Remigius, Bonn (S7; S1). Region custom was baptism within 24 hours; birth year taken as 1770 for ages."}
    place: {value: "Bonn, archbishopric of Cologne", modern_name: "Bonn, Germany", polity_then: "Electorate of Cologne", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica (place of baptism)."}
  death:
    date: {value: "1827-03-26", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Vienna, Austria", modern_name: "Vienna, Austria", polity_then: "Austrian Empire", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1795, certainty: 0.7, cites: [{source: S7, locator: "Vienna / Op. 1 paragraph (Piano Trios Op. 1, 1795)"}], how_known: "Wikipedia: earliest works to which he accorded an opus number, published 1795. Britannica signed body (S1) still gives no dated lasting work (P39 note retained in S1)."}
  era_bucket: {value: "1750 to 1849", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "His whole life (1770–1827) falls in the bucket (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Germany is Western Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.5, cites: [{source: S1, locator: "'The early years'"}], how_known: "Vienna from 1792; Austria assigned as in regions.csv (coder's reading, 0.5)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [German], certainty: 0.7, cites: [{source: S2, locator: "title page (letters translated from the German)"}], how_known: "Letters."}
  occupations: {value: ["composer", "pianist"], certainty: 0.7, cites: [{source: S1, locator: "opening; 'The early years'"}], how_known: "Britannica."}

contribution:
  era_bucket: 19c
  fields: {value: ["music"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Widened the scope of sonata, symphony, concerto and quartet; Ninth Symphony combined vocal and instrumental music", kind: work, lasting: "'Widely regarded as the greatest composer who ever lived' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica; no year in the body read (P39)."}
  evidence_of_impact:
    - {value: "'the fountainhead of much that characterized the work of the Romantics who followed him'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works:
    - {value: "Piano Trios, Op. 1", year: 1795, kind: "composition", certainty: 0.7, cites: [{source: S7, locator: "Op. 1 paragraph"}], how_known: "Wikipedia."}
    - {value: "Symphony No. 1", year: 1800, kind: "composition", certainty: 0.7, cites: [{source: S7, locator: "First Symphony premiered in 1800"}], how_known: "Wikipedia."}
    - {value: "Symphony No. 9 / Missa solemnis", year: 1824, kind: "composition", certainty: 0.7, cites: [{source: S7, locator: "late period paragraph"}], how_known: "Wikipedia."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Catholic (baptized in the Catholic Parish of St Remigius, Bonn)", certainty: 0.7, cites: [{source: S7, locator: "Early life / baptism paragraph"}], how_known: "Wikipedia."}
  family_religious_practice: {value: UNKNOWN, how_known: "Baptism recorded; household practice not detailed in S1/S7."}
  parents_and_household:
    - {value: "Eldest surviving child of Johann and Maria Magdalena van Beethoven; father a singer in the electoral choir", role: parents, certainty: 0.7, cites: [{source: S1, locator: "'The early years'"}], how_known: "Britannica."}
  household_circumstances: {value: "Musicians' family of Flemish origin, growing poorer after 1773 with the father's alcoholism; breadwinner at 18", certainty: 0.7, cites: [{source: S1, locator: "'The early years'"}], how_known: "Britannica."}
  schooling:
    - {value: "School, left by age 11", stage: "elementary school", run_by: other, ages: "–11", certainty: 0.5, cites: [{source: S1, locator: "'The early years'"}], how_known: "Britannica; school not named."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "Christian Gottlob Neefe, court organist, his teacher", certainty: 0.7, cites: [{source: S1, locator: "'The early years'"}], how_known: "Britannica."}
  languages_in_childhood: {value: TODO}
  notable_events:
    - {value: "First extant composition (Nine Variations on a March by Dressler) published at Mannheim", year: 1783, age: 13, certainty: 0.7, cites: [{source: S1, locator: "'The early years'"}], how_known: "Britannica; age from the baptism year."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1795–1824", certainty: 0.7, cites: [{source: S7, locator: "career periods; Op. 1 1795; Ninth / Missa solemnis 1824"}], how_known: "Equal to timing.major_work_period (P30 addendum f)."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system:
    value: BELOW_THRESHOLD
    basis: consistent_private_letters
    certainty: 0.5
    cites: [{source: S2, locator: "No. 26 (1802); No. 109 (1813)"}, {source: S4, locator: "Gottheit / Vorsehung passages"}, {source: S6, locator: "No. 300 (1821)"}]
    rationale: "Theist language (Gottheit who looks into the inner self; Vorsehung; Almighty; Providence who searches the heart) across 1802–1821, but nothing that picks a system: CHRIST, CLTHEI and DEISM all fit. Catholic baptism is heritage only. Bonn's ruler was 'a liberal Roman Catholic' (S1), context only."
    how_known: "Private documents in German Wikisource plus Wallace web translations (vols 1–2)."
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Catholic baptism (S7); grace-of-God closings (S2 No. 25); Missa solemnis later. Nothing doctrinal of his own on Christ or creed read this pass.", cites: [{source: S7, locator: "baptism"}, {source: S2, locator: "No. 25"}]}
    - {code: CLTHEI, reason: "A providential personal Gottheit / Providence across Heiligenstadt and later letters (S2, S4, S6).", cites: [{source: S4, locator: "Gottheit / Vorsehung"}, {source: S6, locator: "No. 300"}]}
    - {code: DEISM, reason: "'Tempel der Natur' (1802) and nature-worship language elsewhere; no rejection of revelation (P27).", cites: [{source: S4, locator: "Tempel der Natur"}]}
  lio_axes:
    A_locus:
      value: 0
      basis: consistent_private_letters
      certainty: 0.7
      support: corroborated
      cites: [{source: S2, locator: "No. 26 (Heiligenstadt, 6 Oct. 1802); No. 109 (to Zmeskall, 26 Apr. 1813)"}, {source: S4, locator: "Gottheit du siehst herab…; o Vorsehung…; o Wann o Gottheit"}, {source: S5, locator: "Divine One thou lookest…; O Providence…; temple of nature"}, {source: S6, locator: "No. 300 (18 July 1821)"}]
      how_known: "Consistent private documents 1802–1821. German Wikisource (S4) plus two independent English web translations (Wallace S2; Wikisource S5) and a further Wallace letter (S6) → corroborated (P48). Private writing / unofficial web copies, 0.7 ceiling; alternative named."
      rationale: "A personal Gottheit who looks into the inner self (1802 German) and Providence/Almighty who acts in a life (1813, 1821): a God apart from the world. Named alternative: 1 ('Tempel der Natur und der Menschen', 1802 addendum) — nature as place of joy, not pantheist identity."
    B_cause: {value: BELOW_THRESHOLD, how_known: "Not a scientist (P16, P30). Providence / Almighty statements (Heiligenstadt; Zmeskall 1813; Rudolph 1821) concern rescue and duties in his own life, not nature's causal order (P16; same as Mozart). 'Tempel der Natur' is a place of joy, not law vs exception. Forest 'Holy! Holy!' and Sturm Betrachtungen markings (reported via secondary sites) unread this pass as own-words law statements. Named reading: still BELOW if those remain aesthetic/devotional nature-talk (Debussy parallel).", note: "Gap: Solomon Tagebuch edition; Beethoven's annotated Sturm; Anderson Letters for any law-of-nature wording."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read (P7)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "B is BELOW_THRESHOLD. P48: A support corroborated at 0.7, but B unscored → still unplotted (need both axes)."}
  statements:
    - text: "Gottheit du siehst herab auf mein inneres, du kennst es, du weist, dasß menschenliebe und neigung zum Wohlthun drin Hausen"
      cites: [{source: S4, locator: "main Testament (6 Oct. 1802)"}]
      date: "1802-10-06"
      context: "Heiligenstadt Testament to his brothers; German Wikisource text of the autograph-based print tradition."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Primary German wording; spelling as in Wikisource. Wallace (S2) and EN Wikisource (S5) are independent English renderings of the same sentence."
    - text: "Divine One thou lookest into my inmost soul, thou knowest it, thou knowest that love of man and desire to do good live therein."
      cites: [{source: S5, locator: "Testament body"}, {source: S2, locator: "No. 26 (Wallace: 'God looks into my heart…')"}]
      date: "1802-10-06"
      context: "Same document; EN Wikisource translation (unknown translator) vs Wallace."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
    - text: "o Vorsehung – laß einmal einen reinen Tag der Freude mir erscheinen … o wann – o Wann o Gottheit – kann ich im Tempel der Natur und der Menschen ihn wider fühlen"
      cites: [{source: S4, locator: "addendum 10 Oct. 1802"}, {source: S5, locator: "Addendum (O Providence… temple of nature)"}]
      date: "1802-10-10"
      context: "Heiligenstadt addendum. Providence petition about his joy; Tempel der Natur is place of joy, not a B law statement (P16)."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
    - text: "But the Almighty will no doubt prevent my being utterly ruined."
      cites: [{source: S2, locator: "No. 109, to Zmeskall, April 26, 1813"}]
      date: "1813-04-26"
      context: "On a postponed concert."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Wallace Gutenberg #13065; web copy, 0.7 cap."
    - text: "That Providence, who searches my inmost heart, and knows that as a man I have striven sacredly to fulfil all the duties imposed on me by humanity, God, and Nature, will no doubt one day extricate me from all these troubles."
      cites: [{source: S6, locator: "No. 300, to Archduke Rudolph, 18 July 1821"}]
      date: "1821-07-18"
      context: "Illness and family troubles; Mass in D delayed. Own-life Providence (P16) — Nature here is a duty-source alongside God/humanity, not nature's causal order."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
  changes_over_life: []
  coder_notes: "Deepen D1: A 0 @ 0.7 support corroborated (German Wikisource + EN Wikisource + Wallace vols 1–2). B stays BELOW_THRESHOLD (P16). Anderson Letters, Solomon Tagebuch, and Sturm annotations unread. Conversation books unread. Chart still unplotted."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Flemish origin (Malines)", certainty: 0.7, cites: [{source: S1, locator: "'The early years'"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Catholic", certainty: 0.7, cites: [{source: S7, locator: "Early life / baptism paragraph"}], how_known: "Baptized Catholic; heritage only."}
  baptism_or_initiation: {value: "Baptized 17 December 1770, Catholic Parish of St Remigius, Bonn", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "Early life / baptism paragraph"}], how_known: "Two sources; church from Wikipedia."}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1795–1824", certainty: 0.7, cites: [{source: S7, locator: "Op. 1 1795; Ninth / Missa solemnis premiered 1824"}], how_known: "Op. 1 piano trios to Ninth Symphony / Missa solemnis (Wikipedia). Britannica signed body (S1) still undates lasting works."}
  age_at_first_lasting_contribution: {value: 25, certainty: 0.7, cites: [{source: S7, locator: "Op. 1 1795"}, {source: S1, locator: "baptism year 1770"}], how_known: "P30 rule 5: 1795 − 1770 = 25, no month adjustment."}
  first_evidence_of_lio_type_views: {value: "Heiligenstadt Testament (Gottheit / Vorsehung)", year: 1802, certainty: 0.7, cites: [{source: S4, locator: "6 and 10 Oct. 1802"}], how_known: "Earliest dated A-bearing private document read; B still BELOW so not a full LIO pair."}
  lio_views_relative_to_major_work: {value: "during major work", rationale: "Heiligenstadt 1802 falls inside 1795–1824; later A letters (1813, 1821) also inside the span. B remains BELOW_THRESHOLD.", certainty: 0.7, cites: [{source: S4, locator: "1802"}, {source: S7, locator: "span"}], how_known: "Dates."}
  worldview_during_major_work: {value: "Personal providential theism in private letters (A 0); no B statement on nature's order", certainty: 0.5, cites: [{source: S4, locator: "1802"}, {source: S6, locator: "1821"}], how_known: "A documented; B BELOW."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Nothing read.", certainty: 0.5, cites: [{source: S1, locator: "'The early years'"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "'The early years'"}], how_known: "Left school by 11."}
  circle_present: {value: "no", rationale: "A personal, providential Gottheit; Tempel der Natur is joy-place, not God=Nature identity; no lawful-order statement.", certainty: 0.5, cites: [{source: S4, locator: "Gottheit / Tempel der Natur"}, {source: S6, locator: "No. 300"}], how_known: "Coder's reading."}
  reading: "Personal providential theism in letters."
  notes: ""

institutions:
  - {value: "Court of the archbishop-elector of Cologne, Bonn", role: "assistant court organist; continuo player; violist", years: "1782–1792", kind: employer, certainty: 0.7, cites: [{source: S1, locator: "'The early years'"}], how_known: "Britannica."}
collaborators:
  - {value: "Christian Gottlob Neefe", relation: teacher, certainty: 0.7, cites: [{source: S1, locator: "'The early years'"}], how_known: "Britannica."}
  - {value: "Joseph Haydn", relation: teacher, note: "offered to take him as a pupil; Beethoven left Bonn for Vienna in 1792", certainty: 0.7, cites: [{source: S1, locator: "'The early years'"}], how_known: "Britannica."}
  - {value: "Ferdinand, Graf von Waldstein", relation: "mentor or employer", note: "patron and admirer from 1788", certainty: 0.7, cites: [{source: S1, locator: "'The early years'"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 53"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "A rests on unofficial web copies of private documents (German Wikisource; Wallace Gutenberg; EN Wikisource), capped at 0.7."
    - "Britannica signed body (S1) still undates lasting works; timing years from Wikipedia (S7)."
  open_questions:
    - "Emily Anderson, The Letters of Beethoven (1961), or BGA / Henle Briefwechsel for scholarly-edition wording of Heiligenstadt and Rudolph 1821."
    - "Maynard Solomon Tagebuch edition for diary prayers; Beethoven's annotated Sturm Betrachtungen for any law-of-nature own words (B)."
    - "Conversation books for late religious remarks."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Julian Medforth Budden"
    citation: "Budden, Julian Medforth. 'Ludwig van Beethoven.' Encyclopaedia Britannica. https://www.britannica.com/biography/Ludwig-van-Beethoven."
    url: "https://www.britannica.com/biography/Ludwig-van-Beethoven"
    accessed: 2026-10-15
    reliability_note: "Signed article body (opening and 'The early years'); the Top Questions box is not used. Britannica lists several contributors; the byline shown was Julian Medforth Budden in one fetch and Raymond L. Knapp in another on 2026-10-15. Signed sections date no lasting work (P39); timing years in this deepen come from Wikipedia (S7). Re-access 403 on 2026-10-24; prior read retained."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: primary
    kind: letter
    author: "Ludwig van Beethoven"
    citation: "Beethoven, Ludwig van. Beethoven's Letters 1790-1826, Volume 1. From the collection of Dr. Ludwig Nohl. Trans. Lady Grace Wallace. Project Gutenberg eBook #13065."
    url: "https://www.gutenberg.org/ebooks/13065"
    accessed: 2026-10-15
    reliability_note: "Translated letters in an unofficial web copy; §7 cap 0.7. Heiligenstadt No. 26 and Zmeskall No. 109 re-checked 2026-10-24."
    source_quality: "unofficial web copy"
    used_for: [basics, worldview, timing, lane_b]
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
    kind: letter
    author: "Ludwig van Beethoven"
    citation: "Beethoven, Ludwig van. 'Heiligenstädter Testament' (6 and 10 Oct. 1802). German text. Wikisource. https://de.wikisource.org/wiki/Heiligenstädter_Testament."
    url: "https://de.wikisource.org/wiki/Heiligenstädter_Testament"
    accessed: 2026-10-24
    reliability_note: "Unofficial web copy of the German Heiligenstadt text (Gottheit / Vorsehung / Tempel der Natur). Primary language for A corroboration; not a critical BGA/Henle edition."
    source_quality: "primary / own words"
    used_for: [worldview, timing]
  - id: S5
    type: primary
    kind: letter
    author: "Ludwig van Beethoven"
    citation: "Beethoven, Ludwig van. 'Heiligenstadt Testament' (1802). English translation (unknown translator). Wikisource. https://en.wikisource.org/wiki/Heiligenstadt_Testament."
    url: "https://en.wikisource.org/wiki/Heiligenstadt_Testament"
    accessed: 2026-10-24
    reliability_note: "Independent English web translation (not Wallace); used with S4/S2 to corroborate A wording."
    source_quality: "unofficial web copy"
    used_for: [worldview]
  - id: S6
    type: primary
    kind: letter
    author: "Ludwig van Beethoven"
    citation: "Beethoven, Ludwig van. Beethoven's Letters 1790-1826, Volume 2. From the collection of Dr. Ludwig Nohl. Trans. Lady Grace Wallace. Project Gutenberg eBook #13272. Letter No. 300 to Archduke Rudolph, 18 July 1821."
    url: "https://www.gutenberg.org/ebooks/13272"
    accessed: 2026-10-24
    reliability_note: "Unofficial web copy; §7 cap 0.7. Letter 300: Providence / humanity, God, and Nature."
    source_quality: "unofficial web copy"
    used_for: [worldview, timing]
  - id: S7
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia contributors. 'Ludwig van Beethoven.' Wikipedia. https://en.wikipedia.org/wiki/Ludwig_van_Beethoven."
    url: "https://en.wikipedia.org/wiki/Ludwig_van_Beethoven"
    accessed: 2026-10-24
    reliability_note: "Dual-source biography and dated works (Op. 1 1795; First Symphony 1800; Ninth / Missa solemnis 1824; Catholic baptism at St Remigius). Not used alone for axis scores."
    source_quality: "other"
    used_for: [identity, basics, contribution, childhood, heritage, timing]
---

# Ludwig van Beethoven

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Ludwig van Beethoven (baptized 1770–1827), German composer [S1; S7]. Deepen D1 (P47–P50): primary_system BELOW_THRESHOLD (candidates CHRIST, CLTHEI, DEISM); A 0 at 0.7 consistent_private_letters, support corroborated (S2+S4+S5+S6; alt 1); B BELOW_THRESHOLD (P16); C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD. Still unplotted (B BELOW).

## Life and work

Bonn court musician; to Vienna in 1792 [S1].

## Contribution and impact

Widened sonata, symphony, concerto and quartet [S1]; Op. 1 (1795), First Symphony (1800), Ninth / Missa solemnis (1824) [S7].

## Childhood and education

Musicians' family; left school by 11; taught by Neefe [S1].

## Adult working worldview

German Heiligenstadt: 'Gottheit du siehst herab auf mein inneres' and 'o Vorsehung… Tempel der Natur' (1802) [S4; S5; S2]. 'The Almighty will no doubt prevent my being utterly ruined' (1813) [S2]. 'Providence, who searches my inmost heart… humanity, God, and Nature' (1821) [S6]. A 0 at 0.7, support corroborated; B BELOW_THRESHOLD (P16).

## Heritage (context only)

Flemish origin; Catholic baptism at St Remigius, Bonn [S1; S7].

## Timing

Op. 1 (1795) to Ninth / Missa solemnis (1824) [S7]; age at first lasting contribution 25. Heiligenstadt 1802 during the span.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No circle [S2].

## Open questions

- Anderson Letters / BGA for scholarly-edition wording.
- Solomon Tagebuch; annotated Sturm for any B nature-order own words.
- Conversation books.

## Research log

- 2026-10-15: Read Britannica (Budden, opening and 'The early years') and letters Nos. 25, 26, 109 (Gutenberg #13065).
- 2026-10-24 (deepen D1, queue #53): German Wikisource Heiligenstädter Testament (S4); EN Wikisource translation (S5); Gutenberg vol. 2 letter 300 (S6); Wikipedia EN dual-source bio and Op. 1 / Ninth dates (S7). Re-checked Wallace Heiligenstadt and Zmeskall. Britannica re-access 403. P47 on S1–S7; A support corroborated; B stays BELOW (P16). Chart-moving NO. No fallacy_catalog (Jason).
