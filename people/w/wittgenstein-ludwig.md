---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch I)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch I, order P32: F 5, rank 54). Basics from Britannica (Monk), signed body only. Worldview from the Tractatus Logico-Philosophicus (1921; Ogden translation, 1922), read in the Gutenberg #5740 PDF (web copy, 0.7 cap). Not a scientist (P30). primary_system BELOW_THRESHOLD (candidates CHRIST, AGNOS); A 0 at 0.5 (alt BELOW_THRESHOLD); B BELOW_THRESHOLD (6.37 and 6.371–6.372 deny natural necessity and that laws of nature explain, which fits no B anchor; RQ1 batch I); C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD. Not plotted. Draft, not reviewed."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Audit fixes (fallacy_catalog audit of bbb26f8, run 1). B_cause BELOW_THRESHOLD -> 3 (0.5, alternative BELOW_THRESHOLD) under P41, the laws-only-describe view as for Russell; now plotted (faded) at A 0 / B 3, mid_basin BELOW_THRESHOLD. S2 cited as the Gutenberg #5740 PDF; the plain-text file returns 404."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #54, F5 rank 54). Needs: A single source + faded; B single source + faded. P47 source_quality on S1–S7. Corroborated A via German Tractatus (S4, Wittgenstein Project reproduction of 1922 bilingual: Gott offenbart sich nicht in der Welt / Sinn der Welt ausserhalb) + Ogden EN (S2 / S5 Wikisource) + Lecture on Ethics 1929 (S6: God allegory; Ethics supernatural; wonder at world existence). A stays 0 @ 0.5 written_profession, support single→corroborated (P48); alt BELOW retained (saying vs locus). Corroborated B via German 6.37 / 6.371–6.372 / 5.1361 (S4) + Ogden (S2/S5); B stays 3 @ 0.5 under P41 (alt 4 / BELOW); support single→corroborated. Dual-source bio Wikipedia (S7): Catholic infant baptism; birth/death confirm. Britannica S1 403 this pass — prior Monk read retained. Notebooks 1914–16 scholarly edition unread. Chart-moving YES on fill cue only (faded hollow → faded filled); darkness still faded (both @ 0.5). No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: wittgenstein-ludwig
  display_name: "Ludwig Wittgenstein"
  roster:
    canonical_name: "Ludwig Wittgenstein"
    rank: 54
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: philosophy
    field_bucket: philosophy
  full_name: {value: "Ludwig Josef Johann Wittgenstein", certainty: 0.7, cites: [{source: S1, locator: "header ('Also known as')"}], how_known: "Britannica."}
  native_name: {value: "Ludwig Wittgenstein", certainty: 0.7, cites: [{source: S7, locator: "opening (Austrian German pronunciation)"}], how_known: "German; same Latin-script form (Wikipedia)."}
  aliases: []

basics:
  birth:
    date: {value: "1889-04-26", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "infobox / opening"}], how_known: "Two sources."}
    place: {value: "Vienna, Austria-Hungary", modern_name: "Vienna, Austria", polity_then: "Austria-Hungary", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "1951-04-29", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening; last paragraph"}, {source: S7, locator: "infobox / death"}], how_known: "Two sources."}
    place: {value: "Cambridge, Cambridgeshire, England", modern_name: "Cambridge, United Kingdom", polity_then: "United Kingdom", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1921, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Logisch-philosophische Abhandlung (1921; Tractatus Logico-Philosophicus, 1922) (P13)."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "From 1921 (P2); the later work runs to 1951, in the same bucket."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Austria is Western Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.5, cites: [{source: S1, locator: "Cambridge from 1929"}], how_known: "Tractatus finished in Austria (Western Europe); later work at Cambridge (Northern Europe); coder's reading, 0.5."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [German], certainty: 0.7, cites: [{source: S1, locator: "opening (German titles)"}], how_known: "Britannica."}
  occupations: {value: ["philosopher", "elementary school teacher"], certainty: 0.7, cites: [{source: S1, locator: "opening; post-war years"}], how_known: "Britannica."}

contribution:
  fields: {value: ["logic", "philosophy of language", "philosophy of mathematics", "philosophy of mind"], certainty: 0.7, cites: [{source: S1, locator: "later-work paragraphs"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Tractatus Logico-Philosophicus (picture theory of meaning)", year: 1921, kind: work, lasting: "'inspired a vast secondary literature' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    - {value: "Philosophical Investigations (language games; private language argument)", year: 1953, kind: work, lasting: "(S1)", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Published posthumously in 1953; worked on for his last 20 years (S1), so the end year is uncertain (0.5)."}
  evidence_of_impact:
    - {value: "'regarded by many as the greatest philosopher of the 20th century'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works:
    - {value: "Tractatus Logico-Philosophicus (Logisch-philosophische Abhandlung)", year: 1921, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "publication"}], how_known: "Two sources."}
    - {value: "Philosophical Investigations", year: 1953, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "1953 publication"}], how_known: "Two sources; worked on in lifetime."}
    - {value: "A Lecture on Ethics", year: 1929, kind: "lecture series", certainty: 0.7, cites: [{source: S6, locator: "Heretics Society, Cambridge, 17 Nov. 1929"}, {source: S7, locator: "PhD and fellowship"}], how_known: "Delivered 1929; Philosophical Review 1965."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Family originally Jewish; father raised Protestant, mother raised Catholic", certainty: 0.7, cites: [{source: S1, locator: "family paragraph"}], how_known: "Britannica."}
  family_religious_practice: {value: "Raised in the Roman Catholic faith of their mother", certainty: 0.7, cites: [{source: S7, locator: "Early life / Faith"}], how_known: "Wikipedia."}
  parents_and_household:
    - {value: "Father Karl Wittgenstein, steel industrialist; mother Leopoldine; youngest of eight children", role: parents, certainty: 0.7, cites: [{source: S1, locator: "family paragraph"}], how_known: "Britannica."}
  household_circumstances: {value: "One of the wealthiest families of Habsburg Vienna; a centre of Viennese cultural life", certainty: 0.7, cites: [{source: S1, locator: "family paragraph"}], how_known: "Britannica."}
  schooling: []
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading:
    - {value: "Otto Weininger, Sex and Character (1903)", certainty: 0.7, cites: [{source: S1, locator: "Weininger paragraph"}], how_known: "Britannica: 'one of the earliest and deepest influences'."}
  childhood_mentors: []
  languages_in_childhood: {value: TODO}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1921–1953", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "Even if all possible scientific questions are answered, 'the problems of life have still not been touched at all' (Tractatus 6.52).", certainty: 0.7, cites: [{source: S2, locator: "6.52"}], how_known: "Published book, web copy of the Ogden translation, 0.7 cap."}
  primary_system:
    value: BELOW_THRESHOLD
    basis: written_profession
    certainty: 0.5
    cites: [{source: S4, locator: "6.432, 6.44, 6.522"}, {source: S6, locator: "God allegory; Ethics supernatural"}, {source: S1, locator: "war paragraph (religious conversion)"}]
    rationale: "Tractatus places Gott and das Mystische outside what can be said (6.432, 6.44, 6.522 German); Lecture on Ethics treats God-talk as allegory for experiences beyond significant language. Britannica wartime 'religious conversion' via Tolstoy Gospel (S1). Nothing read picks a system. Candidates CHRIST (Tolstoyan Gospel; Catholic baptism = heritage) and AGNOS (God beyond propositions)."
    how_known: "German Tractatus + Lecture on Ethics + Britannica."
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Catholic infant baptism (S7); Tolstoy Gospel in Brief in war (S1); Lecture on Ethics uses Christian God-allegory language without creed.", cites: [{source: S7, locator: "Faith"}, {source: S6, locator: "God allegory"}]}
    - {code: AGNOS, reason: "Gott / das Mystische cannot be put into propositions (6.432, 6.522); Lecture: tendency to run against language boundaries — not a suspension of belief as such.", cites: [{source: S4, locator: "6.432, 6.522"}, {source: S6, locator: "closing"}]}
  lio_axes:
    A_locus:
      value: 0
      basis: written_profession
      certainty: 0.5
      support: corroborated
      cites: [{source: S4, locator: "6.41; 6.432 (Gott offenbart sich nicht in der Welt)"}, {source: S2, locator: "6.41, 6.432 (Ogden)"}, {source: S5, locator: "6.41, 6.432 (Wikisource Ogden)"}, {source: S6, locator: "God allegory; Ethics supernatural; wonder at existence"}]
      how_known: "Published Tractatus in German (S4) plus Ogden EN (S2/S5) and Lecture on Ethics (S6). Contested reading + aphoristic → 0.5 (alt named). Independent streams → support corroborated (P48)."
      rationale: "German 6.432: 'Gott offenbart sich nicht in der Welt'; 6.41: sense of the world must lie outside it — what is higher is outside the world (A 0). Lecture on Ethics (1929): God-talk as allegory for wonder at the world's existence and absolute safety; Ethics 'supernatural' and beyond significant language — same outside-the-world placement. Named alternative: BELOW_THRESHOLD, since 6.432 may be a remark about what can be said rather than a claim about where God is."
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.5
      support: corroborated
      cites: [{source: S4, locator: "6.37; 6.371–6.372; 5.1361"}, {source: S2, locator: "6.37, 6.371, 6.372 (Ogden)"}, {source: S5, locator: "6.37–6.372 (Wikisource Ogden)"}]
      how_known: "German Tractatus (S4) plus Ogden EN (S2/S5). P41 caps at 0.5 without a stated no-exception claim; alt named. Independent streams → support corroborated (P48)."
      rationale: "P41 (as for Russell): laws of nature only describe and do not explain or necessitate. German 6.37: only logical necessity; 6.371: Täuschung that Naturgesetze are Erklärungen; 5.1361: belief in the Kausalnexus is Aberglaube. No exceptionless order stated (P40) → not 4; no intervention accepted. B 3. Named alternatives: 4 (if denial of natural necessity is read as exceptionless law-talk) and BELOW_THRESHOLD (if the remarks are only about logic/explanation, not how nature runs)."
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read (P7)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A 0 and B 3 both at 0.5: mid-basin test needs ≥ 0.7 (P10). Support now corroborated on both axes (P48 fill cue), but darkness stays faded."}
  statements:
    - text: "Gott offenbart sich nicht in der Welt."
      cites: [{source: S4, locator: "6.432"}, {source: S2, locator: "6.432 (Ogden: 'God does not reveal himself in the world')"}, {source: S5, locator: "6.432"}]
      date: "1921"
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "German primary via Wittgenstein Project (1922 bilingual reproduction). Ogden EN corroborates."
    - text: "Der Sinn der Welt muss ausserhalb ihrer liegen."
      cites: [{source: S4, locator: "6.41"}, {source: S5, locator: "6.41 (Ogden: 'The sense of the world must lie outside the world')"}]
      date: "1921"
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
    - text: "Einen Zwang, nach dem Eines geschehen müsste, weil etwas anderes geschehen ist, gibt es nicht. Es gibt nur eine logische Notwendigkeit."
      cites: [{source: S4, locator: "6.37"}, {source: S5, locator: "6.37 (Ogden)"}]
      date: "1921"
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
    - text: "Der ganzen modernen Weltanschauung liegt die Täuschung zugrunde, dass die sogenannten Naturgesetze die Erklärungen der Naturerscheinungen seien."
      cites: [{source: S4, locator: "6.371"}, {source: S5, locator: "6.371 (Ogden)"}]
      date: "1921"
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
    - text: "Der Glaube an den Kausalnexus ist der Aberglaube."
      cites: [{source: S4, locator: "5.1361"}]
      date: "1921"
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Supports B as denial of natural causal necessity; not a no-exception claim (P41)."
    - text: "For when we speak of God and that he sees everything and when we kneel and pray to him all our terms and actions seem to be parts of a great and elaborate allegory which represents him as a human being of great power whose grace we try to win, etc., etc. … the first of them is, I believe, exactly what people were referring to when they said that God had created the world; and the experience of absolute safety has been described by saying that we feel safe in the hands of God."
      cites: [{source: S6, locator: "Lecture on Ethics (Heretics Society, 17 Nov. 1929; Phil. Review 1965)"}]
      date: "1929-11-17"
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Public lecture text; God as allegory for experiences beyond significant language — A-adjacent (outside-the-world), not a creed."
    - text: "Ethics, if it is anything, is supernatural and our words will only express facts."
      cites: [{source: S6, locator: "Lecture on Ethics"}]
      date: "1929-11-17"
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
  changes_over_life:
    - {value: "Religious conversion on the Eastern front, inspired in part by Tolstoy's The Gospel in Brief", year: 1914, certainty: 0.5, cites: [{source: S1, locator: "war paragraph"}, {source: S7, locator: "Military service / Faith"}], how_known: "Britannica and Wikipedia; year approximate (war start)."}
  coder_notes: "Deepen D1: A 0 @ 0.5 support corroborated (S4 German + S2/S5 Ogden + S6 Lecture); B 3 @ 0.5 support corroborated (S4+S2/S5; P41). Both stay faded. Chart fill hollow→filled. Notebooks 1914–16 scholarly edition unread. No fallacy_catalog."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Viennese family of Jewish origin", certainty: 0.7, cites: [{source: S1, locator: "family paragraph"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Catholic mother, Protestant-raised father (family Jewish in origin)", certainty: 0.7, cites: [{source: S1, locator: "family paragraph"}], how_known: "Britannica."}
  baptism_or_initiation: {value: "Baptized as an infant by a Catholic priest", certainty: 0.7, cites: [{source: S7, locator: "Faith section"}], how_known: "Wikipedia."}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1921–1953", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "First to last listed lasting contribution (P29, P30); 1953 is posthumous publication."}
  age_at_first_lasting_contribution: {value: 32, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "1921 − 1889 = 32 (P30)."}
  first_evidence_of_lio_type_views: {value: "Tractatus 6.37–6.432 (Gott outside world; laws do not explain)", year: 1921, certainty: 0.5, cites: [{source: S4, locator: "6.37–6.432"}], how_known: "Published Tractatus; A and B both scored (faded)."}
  lio_views_relative_to_major_work: {value: "during major work", rationale: "Tractatus (1921) is the first lasting contribution; Lecture on Ethics 1929 inside the span.", certainty: 0.7, cites: [{source: S4, locator: "1921"}, {source: S6, locator: "1929"}], how_known: "Dates."}
  worldview_during_major_work: {value: "A 0 / B 3 (faded); primary_system BELOW_THRESHOLD", certainty: 0.5, cites: [{source: S4, locator: "6.37–6.432"}, {source: S6, locator: "1929"}], how_known: "As axes."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "The Tractatus is a numbered, deductively arranged treatise on logic.", certainty: 0.5, cites: [{source: S2, locator: "structure"}], how_known: "Coder's reading."}
  form_acquired: {value: "adulthood, before major work", certainty: 0.5, cites: [{source: S1, locator: "Cambridge and Russell"}], how_known: "Logic with Russell before the war."}
  circle_present: {value: "no", rationale: "Denies that Naturgesetze explain or that a Kausalnexus exists (5.1361, 6.37–6.372).", certainty: 0.5, cites: [{source: S4, locator: "5.1361; 6.37–6.372"}], how_known: "Coder's reading."}
  reading: "God outside the world and beyond saying; no lawful-order circle."
  notes: ""

institutions:
  - {value: "Trinity College, Cambridge", role: "lecturer, then professor of philosophy (from 1939)", years: "1929–1947", kind: university, certainty: 0.7, cites: [{source: S1, locator: "1929 paragraph; later years"}], how_known: "Britannica."}
collaborators:
  - {value: "Bertrand Russell", relation: teacher, certainty: 0.7, cites: [{source: S1, locator: "logic paragraph"}], how_known: "Britannica."}
  - {value: "Frank Ramsey", relation: collaborator, certainty: 0.7, cites: [{source: S1, locator: "1929 paragraph"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 54"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "A and B rest on unofficial web copies of the Tractatus (German Wittgenstein Project; Ogden Wikisource/Gutenberg) and Lecture on Ethics; axis certainties capped at 0.5 by contested readings and P41."
    - "Britannica S1 re-access Cloudflare/403 on 2026-10-24; prior Monk signed-body read retained."
  open_questions:
    - "Notebooks 1914–16 (Anscombe/von Wright scholarly edition) for wartime God / meaning-of-life remarks as private corroboration."
    - "Pears–McGuinness Tractatus translation as a third EN stream."
    - "Culture and Value / later remarks for any shift after the Tractatus phase (P20)."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Ray Monk"
    citation: "Monk, Ray. 'Ludwig Wittgenstein.' Encyclopaedia Britannica. https://www.britannica.com/biography/Ludwig-Wittgenstein."
    url: "https://www.britannica.com/biography/Ludwig-Wittgenstein"
    accessed: 2026-10-15
    reliability_note: "Signed article body; Top Questions (AI-generated) not used. Re-access Cloudflare/403 on 2026-10-24; prior Monk read retained."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Ludwig Wittgenstein"
    year: 1922
    citation: "Wittgenstein, Ludwig. Tractatus Logico-Philosophicus. Trans. C. K. Ogden. 1922. Project Gutenberg eBook #5740 (PDF)."
    url: "https://www.gutenberg.org/ebooks/5740"
    accessed: 2026-10-15
    reliability_note: "Unofficial web copy of the published Ogden translation; §7 cap 0.7. Plain-text file 404; PDF used. Rechecked via Wikisource S5 this pass."
    source_quality: "unofficial web copy"
    used_for: [worldview, timing, lane_b]
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
    author: "Ludwig Wittgenstein"
    year: 1922
    citation: "Wittgenstein, Ludwig. Logisch-philosophische Abhandlung (Tractatus Logico-Philosophicus). German text. Ludwig Wittgenstein Project reproduction of the 1922 Ogden bilingual edition (Kegan Paul). https://raw.githubusercontent.com/wittgenstein-project/wittgenstein-published-works/main/markdown/german/Logisch-philosophische%20Abhandlung/Logisch-philosophische%20Abhandlung.md"
    url: "https://www.wittgensteinproject.org/"
    accessed: 2026-10-24
    reliability_note: "Primary German wording of 6.37–6.432 and 5.1361; unofficial web reproduction of the 1922 print, not a critical Suhrkamp/BGM edition."
    source_quality: "primary / own words"
    used_for: [worldview, timing, lane_b]
  - id: S5
    type: primary
    kind: "published work by the subject"
    author: "Ludwig Wittgenstein"
    year: 1922
    citation: "Wittgenstein, Ludwig. Tractatus Logico-Philosophicus. Trans. C. K. Ogden. Wikisource, section 6. https://en.wikisource.org/wiki/Tractatus_Logico-Philosophicus/6"
    url: "https://en.wikisource.org/wiki/Tractatus_Logico-Philosophicus/6"
    accessed: 2026-10-24
    reliability_note: "Unofficial web copy of Ogden EN; used with S2/S4 to corroborate English wording against German."
    source_quality: "unofficial web copy"
    used_for: [worldview]
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "Ludwig Wittgenstein"
    year: 1929
    citation: "Wittgenstein, Ludwig. 'A Lecture on Ethics.' Delivered to the Heretics Society, Cambridge, 17 November 1929. The Philosophical Review 74, no. 1 (Jan. 1965): 3–12. Ludwig Wittgenstein Project digital edition. https://www.wittgensteinproject.org/w/index.php/Lecture_on_Ethics"
    url: "https://www.wittgensteinproject.org/w/index.php/Lecture_on_Ethics"
    accessed: 2026-10-24
    reliability_note: "Public lecture text (English as delivered); CC BY-NC digital edition of the 1965 Philosophical Review printing. Own words for A (God allegory; Ethics supernatural)."
    source_quality: "primary / own words"
    used_for: [worldview, contribution, timing]
  - id: S7
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia contributors. 'Ludwig Wittgenstein.' Wikipedia. https://en.wikipedia.org/wiki/Ludwig_Wittgenstein."
    url: "https://en.wikipedia.org/wiki/Ludwig_Wittgenstein"
    accessed: 2026-10-24
    reliability_note: "Dual-source biography: birth/death; Catholic infant baptism; Lecture on Ethics date; family Catholic upbringing. Not used alone for axis scores."
    source_quality: "other"
    used_for: [identity, basics, contribution, childhood, heritage, timing]
---

# Ludwig Wittgenstein

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Ludwig Wittgenstein (1889–1951), Austrian-born British philosopher [S1; S7]. Deepen D1 (P47–P50): primary_system BELOW_THRESHOLD (CHRIST / AGNOS); A 0 at 0.5 written_profession, support corroborated (S4+S2/S5+S6; alt BELOW); B 3 at 0.5 written_profession, support corroborated (S4+S2/S5; P41); mid_basin BELOW_THRESHOLD. Chart: faded hollow → faded filled (fill cue).

## Life and work

Vienna; Cambridge with Russell; war service; schoolteacher; Cambridge from 1929 [S1].

## Contribution and impact

Tractatus (1921); Philosophical Investigations (1953) [S1].

## Childhood and education

Youngest of eight in a wealthy Viennese family [S1].

## Adult working worldview

German Tractatus: 'Gott offenbart sich nicht in der Welt' (6.432); 'Es gibt nur eine logische Notwendigkeit' (6.37); Naturgesetze as Täuschung (6.371) [S4; S5]. Lecture on Ethics (1929): God as allegory; Ethics supernatural [S6]. A 0 / B 3 at 0.5, both support corroborated.

## Heritage (context only)

Jewish origin; Catholic infant baptism; raised in mother’s Roman Catholic faith; Protestant-raised father [S1; S7].

## Timing

First lasting contribution 1921, at 32 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No circle [S2].

## Open questions

- Notebooks 1914–16 scholarly edition.
- Pears–McGuinness Tractatus; Culture and Value for later-phase shifts.

## Research log

- 2026-10-15: Read Britannica (Monk) and Tractatus 6.37–6.522 (Gutenberg #5740 PDF).
- 2026-10-15: Batch I audit fixes: B 3 under P41; source cited as the #5740 PDF (the plain-text file returns 404).
- 2026-10-24 (deepen D1, queue #54): German Tractatus via Wittgenstein Project (S4); Ogden Wikisource §6 (S5); Lecture on Ethics (S6); Wikipedia dual-source bio (S7). Britannica 403. P47 on S1–S7; A and B support single→corroborated; values stay 0.5. Chart-moving YES (fill only). No fallacy_catalog (Jason).
