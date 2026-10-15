---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch I)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-15
  change_log:
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch I, order P32: F 5, rank 54). Basics from Britannica (Monk), signed body only. Worldview from the Tractatus Logico-Philosophicus (1921; Ogden translation, 1922), read in the Gutenberg #5740 PDF (web copy, 0.7 cap). Not a scientist (P30). primary_system BELOW_THRESHOLD (candidates CHRIST, AGNOS); A 0 at 0.5 (alt BELOW_THRESHOLD); B BELOW_THRESHOLD (6.37 and 6.371–6.372 deny natural necessity and that laws of nature explain, which fits no B anchor; RQ1 batch I); C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD. Not plotted. Draft, not reviewed."}

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
  native_name: {value: UNKNOWN, how_known: "German, same Latin-script form."}
  aliases: []

basics:
  birth:
    date: {value: "1889-04-26", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Vienna, Austria-Hungary", modern_name: "Vienna, Austria", polity_then: "Austria-Hungary", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "1951-04-29", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening; last paragraph"}], how_known: "Britannica."}
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
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Family originally Jewish; father raised Protestant, mother raised Catholic", certainty: 0.7, cites: [{source: S1, locator: "family paragraph"}], how_known: "Britannica."}
  family_religious_practice: {value: TODO}
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
    cites: [{source: S2, locator: "6.432, 6.44, 6.522"}, {source: S1, locator: "war paragraph (religious conversion)"}]
    rationale: "The Tractatus places God and 'the mystical' outside what can be said (6.432, 6.44, 6.522); Britannica reports a wartime 'religious conversion' inspired partly by Tolstoy's Gospel in Brief (S1). Nothing read fixes a system. Candidates CHRIST (Tolstoyan Gospel) and AGNOS (God beyond what can be said)."
    how_known: "Published book in a web copy plus Britannica."
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Tolstoy's Gospel in Brief carried through the war (S1); no creed stated in the Tractatus."}
    - {code: AGNOS, reason: "God and the mystical cannot be put into propositions (6.432, 6.522); not a suspension of belief as such."}
  lio_axes:
    A_locus:
      value: 0
      basis: written_profession
      certainty: 0.5
      cites: [{source: S2, locator: "6.41, 6.432"}]
      how_known: "Published book, web copy; aphoristic, so 0.5; alternative named."
      rationale: "'God does not reveal himself in the world' (6.432) and 'The sense of the world must lie outside the world' (6.41): what is higher is outside the world. Named alternative: BELOW_THRESHOLD, since 6.432 may be a remark about what can be said rather than a claim about where God is."
    B_cause:
      value: BELOW_THRESHOLD
      how_known: "6.37: 'A necessity for one thing to happen because another has happened does not exist. There is only logical necessity.' 6.371–6.372: the 'illusion' that laws of nature explain phenomena; people 'stop short at natural laws as at something unassailable, as did the ancients at God and Fate'. This denies causal necessity in nature but neither affirms exceptionless law (B 4) nor accepts intervention (B ≤ 3). No anchor fits. RQ1 (batch I)."
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read (P7)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "B is BELOW_THRESHOLD."}
  statements:
    - text: "How the world is, is completely indifferent for what is higher. God does not reveal himself in the world."
      cites: [{source: S2, locator: "6.432"}]
      date: "1921"
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "Ogden translation (1922) via the Gutenberg #5740 PDF; 'indifferent' restored where the text extraction dropped the 'ff' ligature. Web copy, 0.7 cap."
    - text: "A necessity for one thing to happen because another has happened does not exist. There is only logical necessity."
      cites: [{source: S2, locator: "6.37"}]
      date: "1921"
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "As above."
    - text: "At the basis of the whole modern view of the world lies the illusion that the so-called laws of nature are the explanations of natural phenomena."
      cites: [{source: S2, locator: "6.371"}]
      date: "1921"
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "As above."
  changes_over_life:
    - {value: "Religious conversion on the Eastern front, inspired in part by Tolstoy's The Gospel in Brief", year: 1914, certainty: 0.5, cites: [{source: S1, locator: "war paragraph"}], how_known: "Britannica gives the war years (1914–18), not the year of the conversion; 1914 is the start of the war (0.5)."}
  coder_notes: "Coder's call; the Tractatus only. Notebooks 1914–16 and the 'Lecture on Ethics' not read. RQ1 (batch I): B for a denial of causal necessity."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Viennese family of Jewish origin", certainty: 0.7, cites: [{source: S1, locator: "family paragraph"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Catholic mother, Protestant-raised father (family Jewish in origin)", certainty: 0.7, cites: [{source: S1, locator: "family paragraph"}], how_known: "Britannica."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1921–1953", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "First to last listed lasting contribution (P29, P30); 1953 is posthumous publication."}
  age_at_first_lasting_contribution: {value: 32, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "1921 − 1889 = 32 (P30)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "B is BELOW_THRESHOLD."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S2, locator: "6.37–6.372"}], how_known: "Denies natural necessity."}
  worldview_during_major_work: {value: BELOW_THRESHOLD, how_known: "As primary_system."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "The Tractatus is a numbered, deductively arranged treatise on logic.", certainty: 0.5, cites: [{source: S2, locator: "structure"}], how_known: "Coder's reading."}
  form_acquired: {value: "adulthood, before major work", certainty: 0.5, cites: [{source: S1, locator: "Cambridge and Russell"}], how_known: "Logic with Russell before the war."}
  circle_present: {value: "no", rationale: "Denies that natural laws explain or that causal necessity exists.", certainty: 0.5, cites: [{source: S2, locator: "6.37–6.372"}], how_known: "Coder's reading."}
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
  data_quality_flags: []
  open_questions:
    - "Read Notebooks 1914–16 and the Lecture on Ethics; RQ1 batch I."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Ray Monk"
    citation: "Monk, Ray. \"Ludwig Wittgenstein.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Ludwig-Wittgenstein."
    url: "https://www.britannica.com/biography/Ludwig-Wittgenstein"
    accessed: 2026-10-15
    reliability_note: "Signed article body; Top Questions (AI-generated) not used."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Ludwig Wittgenstein"
    year: 1922
    citation: "Wittgenstein, Ludwig. Tractatus Logico-Philosophicus. Trans. C. K. Ogden. 1922. Project Gutenberg eBook #5740 (PDF)."
    url: "https://www.gutenberg.org/ebooks/5740"
    accessed: 2026-10-15
    reliability_note: "Unofficial web copy of the published translation; §7 cap 0.7."
    used_for: [worldview, timing, lane_b]
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

# Ludwig Wittgenstein

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Ludwig Wittgenstein (1889–1951), Austrian-born British philosopher [S1]. Draft: primary_system BELOW_THRESHOLD; A 0 at 0.5; B BELOW_THRESHOLD (RQ1); mid_basin BELOW_THRESHOLD. Not plotted.

## Life and work

Vienna; Cambridge with Russell; war service; schoolteacher; Cambridge from 1929 [S1].

## Contribution and impact

Tractatus (1921); Philosophical Investigations (1953) [S1].

## Childhood and education

Youngest of eight in a wealthy Viennese family [S1].

## Adult working worldview

'God does not reveal himself in the world' (6.432); 'There is only logical necessity' (6.37) [S2].

## Heritage (context only)

Jewish origin; Protestant and Catholic parents [S1].

## Timing

First lasting contribution 1921, at 32 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No circle [S2].

## Open questions

- Notebooks 1914–16; RQ1.

## Research log

- 2026-10-15: Read Britannica (Monk) and Tractatus 6.37–6.522 (Gutenberg #5740 PDF).
