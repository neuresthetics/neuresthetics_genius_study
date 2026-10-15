---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch E)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-15
  change_log:
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch E, order P32: F 5, rank 29). Basics from Britannica (Morson) and the chronology in Mayne's 1914 translation of his letters. Worldview: the March 1854 letter to N. D. Fonvisin (Mayne, Letter XXII, pp. 70–71, archive.org scan). Characters (Zosima, Ivan, Shatov) not used. CHRIST 0.5; A BELOW_THRESHOLD; B UNKNOWN; D BELOW_THRESHOLD; mid_basin UNKNOWN. Draft, not reviewed."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Audit fixes (fallacy_catalog audit of 2332880, run 1): primary_system basis scholarly_reconstruction -> consistent_private_letters (his own letter; single letter, so 0.5 kept); locators standardised to Letter 22, begins p. 69, quote pp. 70-71."}

identity:
  id: dostoevsky-fyodor
  display_name: "Fyodor Dostoevsky"
  roster:
    canonical_name: "Fyodor Dostoevsky"
    rank: 29
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: literature
    field_bucket: literature
  full_name: {value: "Fyodor Mikhaylovich Dostoyevsky", certainty: 0.7, cites: [{source: S1, locator: "header ('Also known as')"}], how_known: "Britannica; transliteration varies (Dostoevsky, Dostoyevsky), so 0.7."}
  native_name: {value: "Фёдор Михайлович Достоевский", certainty: 0.5, cites: [{source: S1, locator: "header"}], how_known: "Coder's rendering of the Cyrillic; Britannica gives only transliterations."}
  aliases:
    - {name: "Dostoevsky-Fyodor", kind: "roster alias"}
    - {name: "Fyodor-Dostoevsky", kind: "roster alias"}

basics:
  birth:
    date: {value: "1821-11-11", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "At a Glance ('November 11 [October 30, Old Style], 1821')"}], how_known: "Britannica alone."}
    place: {value: "Moscow", modern_name: "Moscow, Russia", polity_then: "Russian Empire", certainty: 0.7, cites: [{source: S1, locator: "At a Glance"}], how_known: "Britannica alone."}
  death:
    date: {value: "1881-02-09", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "At a Glance"}], how_known: "Britannica alone."}
    place: {value: "St. Petersburg", modern_name: "Saint Petersburg, Russia", polity_then: "Russian Empire", certainty: 0.7, cites: [{source: S1, locator: "At a Glance"}], how_known: "Britannica alone."}
  first_lasting_contribution_year: {value: 1846, certainty: 0.7, cites: [{source: S2, locator: "chronological table, 1846 ('Nekrassov's Petersburg Almanac appears, with Dostoevsky's first book, \"Poor Folk\"')"}], how_known: "Poor Folk, published 15 January 1846; Mayne's chronology alone."}
  era_bucket: {value: "1750 to 1849", certainty: 0.7, cites: [{source: S2, locator: "chronological table, 1846"}], how_known: "From 1846 (P2)."}
  region_of_birth: {value: "Eastern Europe", certainty: 0.7, cites: [{source: S1, locator: "At a Glance"}], how_known: "Russia (P3)."}
  region_of_work: {value: "Eastern Europe", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "St. Petersburg and Siberia; Russia."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [Russian], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
  occupations: {value: ["novelist", "short-story writer", "journalist"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

contribution:
  fields: {value: ["fiction"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Poor Folk", year: 1846, kind: work, lasting: "his first book (S2); acclaimed debut", certainty: 0.7, cites: [{source: S2, locator: "chronological table, 1846"}], how_known: "Mayne chronology."}
    - {value: "The Brothers Karamazov", year: "1879–1880", kind: work, lasting: "one of the four long novels he is best known for (S1)", certainty: 0.7, cites: [{source: S2, locator: "chronological table, 1879–80 ('Appearance of \"The Brothers Karamazov\"')"}, {source: S1, locator: "'Major works'"}], how_known: "Serialised 1879–80 in Russky Vestnik (S2)."}
  evidence_of_impact:
    - {value: "Literary modernism, existentialism and schools of psychology and theology 'profoundly shaped by his ideas'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica body."}
  major_works:
    - {value: "Diary of a Writer", year: "1876–1877", kind: other, certainty: 0.7, cites: [{source: S2, locator: "chronological table, 1876–77"}], how_known: "Mayne chronology; not read for the worldview."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "One of the finest novelists; wide influence.", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "Russian Orthodox (old-fashioned family piety)", certainty: 0.5, cites: [{source: S1, locator: "'Background and early life' ('the old-fashioned piety of his family')"}], how_known: "Britannica says 'piety' without naming the church; Orthodox is the coder's inference, so 0.5."}
  family_religious_practice: {value: "Old-fashioned piety", certainty: 0.7, cites: [{source: S1, locator: "'Background and early life'"}], how_known: "Britannica."}
  parents_and_household:
    - {value: "Father, a retired military surgeon at the Mariinsky Hospital for the Poor, Moscow", role: father, certainty: 0.7, cites: [{source: S1, locator: "'Background and early life'"}], how_known: "Britannica."}
    - {value: "Mother, a cultured woman from a merchant family; died 1837", role: mother, certainty: 0.7, cites: [{source: S1, locator: "'Background and early life'"}], how_known: "Britannica."}
  household_circumstances: {value: "Not landed gentry; father ennobled 1828, bought an estate 1831", certainty: 0.7, cites: [{source: S1, locator: "'Background and early life'"}], how_known: "Britannica."}
  schooling:
    - {value: "Educated at home until 1833", stage: home, years: "–1833", ages: "–12", certainty: 0.7, cites: [{source: S1, locator: "'Background and early life'"}], how_known: "Britannica."}
    - {value: "Day school, then boarding school", stage: "grammar or secondary school", years: "1833–", ages: "12–", certainty: 0.7, cites: [{source: S1, locator: "'Background and early life'"}], how_known: "Britannica."}
    - {value: "Academy of Military Engineering, St. Petersburg (degree 1843)", stage: university, years: "–1843", certainty: 0.7, cites: [{source: S1, locator: "'Background and early life'"}], how_known: "Britannica."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading:
    - {value: "Scott, Radcliffe, Karamzin, Schiller, Pushkin", certainty: 0.7, cites: [{source: S1, locator: "'Background and early life'"}], how_known: "Britannica."}
  childhood_mentors: []
  languages_in_childhood: {value: TODO}
  notable_events:
    - {value: "Death of his mother", year: 1837, age: 16, certainty: 0.7, cites: [{source: S1, locator: "'Background and early life'"}], how_known: "Britannica."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1846–1880", certainty: 0.7, cites: [{source: S2, locator: "chronological table"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "'I am a child of this age, a child of unfaith and scepticism'; yet 'If anyone could prove to me that Christ is outside the truth, and if the truth really did exclude Christ, I should prefer to stay with Christ and not with truth.' (1854)", certainty: 0.5, cites: [{source: S2, locator: "Letter 22 to N. D. Fonvisin, beginning of March 1854 (begins p. 69), quote pp. 70–71"}], how_known: "One private letter, in translation (single-letter rule: 0.5 with a scholar's backing; Britannica's 'lifelong attachment to religion' supports it)."}
  primary_system:
    value: CHRIST
    basis: consistent_private_letters
    certainty: 0.5
    cites: [{source: S1, locator: "'Background and early life' ('Dostoyevsky's lifelong attachment to religion')"}, {source: S2, locator: "Letter 22 (begins p. 69), p. 71"}]
    rationale: "A credo centred on Christ ('nothing lovelier, deeper [...] than the Saviour') in one private letter, plus Morson's account of a lifelong religious attachment. Published nonfiction (Diary of a Writer) not read, so 0.5."
    how_known: "His own private letter (basis consistent_private_letters), but only one letter, so 0.5 with a scholar backing the reading (§3)."
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Chosen at 0.5."}
    - {code: AGNOS, reason: "'child of unfaith and scepticism' — rejected: the same letter states a creed."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "One private letter; it names God and Christ but says nothing on where God is.", note: "'God gives me sometimes moments of perfect peace' implies a personal God; implication only (P19)."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist; the letter and the Britannica article say nothing about nature's order."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read on reward and punishment in his own voice."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "One private letter.", note: "He would 'stay with Christ and not with truth' if they conflicted: a hypothetical preference of faith over proof, in a single letter."}
    E_scope: {value: UNKNOWN, how_known: "Scored on the world's order (P7); nothing read."}
  mid_basin: {value: UNKNOWN, how_known: "B_cause is UNKNOWN, which takes precedence (P19)."}
  statements:
    - text: "I want to say to you, about myself, that I am a child of this age, a child of unfaith and scepticism, and probably (indeed I know it) shall remain so to the end of my life."
      cites: [{source: S2, locator: "Letter 22 to N. D. Fonvisin, beginning of March 1854 (begins p. 69), quote pp. 70–71"}]
      date: "1854-03"
      context: "Letter from Omsk to N. D. Fonvisin, beginning of March 1854, after release from the prison camp."
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-15
      note: "Mayne translation (1914), archive.org scan lettersoffyodorm00dostuoft, OCR checked; Wikiquote's 'Letter XXI, p. 71' is wrong: it is Letter XXII."
    - text: "If anyone could prove to me that Christ is outside the truth, and if the truth really did exclude Christ, I should prefer to stay with Christ and not with truth."
      cites: [{source: S2, locator: "Letter 22 (begins p. 69), p. 71"}]
      date: "1854-03"
      context: "Same letter, after his 'creed'."
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-15
      axes: [D_authority]
  changes_over_life:
    - {value: "Arrest in 1849 (Petrashevsky circle) and Siberian imprisonment", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica; whether it changed his religious view is not documented in the sources read (Britannica's AI box says so, not citable)."}
  coder_notes: "Coder's call: no novel character's words used. Diary of a Writer is the best next source."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Russian", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1846–1880", certainty: 0.7, cites: [{source: S2, locator: "chronological table"}], how_known: "Poor Folk (1846) to Karamazov (range end 1880) (P29, P30 #4)."}
  age_at_first_lasting_contribution: {value: 25, certainty: 0.7, cites: [{source: S1, locator: "At a Glance"}, {source: S2, locator: "chronological table, 1846"}], how_known: "1846 − 1821 = 25 (P30)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No statement scored at 3 or 4."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S2, locator: "Letter 22 (pp. 69–71)"}], how_known: "Only one letter read."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Engineering academy; nothing read on proof training.", certainty: 0.5, cites: [{source: S1, locator: "'Background and early life'"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "'Background and early life'"}], how_known: "Nothing read."}
  circle_present: {value: "no", rationale: "Christ preferred even over truth.", certainty: 0.5, cites: [{source: S2, locator: "Letter 22 (begins p. 69), p. 71"}], how_known: "Coder's reading."}
  reading: "As belief, not finding: no circle."
  notes: ""

institutions:
  - {value: "Academy of Military Engineering, St. Petersburg", role: student, years: "–1843", kind: university, certainty: 0.7, cites: [{source: S1, locator: "'Background and early life'"}], how_known: "Britannica."}
collaborators:
  - {value: "Mikhail Dostoyevsky", relation: family, note: "brother; co-publisher of journals", certainty: 0.7, cites: [{source: S1, locator: "'Background and early life'"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 29"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Wikiquote cites the Fonvisin letter as Letter XXI; the scan shows Letter XXII."
    - "Mayne gives the letter as 'Beginning of March, 1854'; secondary sources say February or March."
  open_questions:
    - "Read Diary of a Writer for published statements on God, miracles and nature."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Gary Saul Morson"
    citation: "Morson, Gary Saul. \"Fyodor Dostoyevsky.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Fyodor-Dostoyevsky."
    url: "https://www.britannica.com/biography/Fyodor-Dostoyevsky"
    accessed: 2026-10-15
    reliability_note: "Signed article body; AI boxes not used (P26)."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, institutions, collaborators]
  - id: S2
    type: primary
    kind: "scholarly edition"
    author: "Fyodor Dostoevsky; trans. Ethel Colburn Mayne"
    year: 1914
    citation: "Letters of Fyodor Michailovitch Dostoevsky to His Family and Friends. Trans. Ethel Colburn Mayne. London: Chatto & Windus, 1914. Scan: archive.org, lettersoffyodorm00dostuoft."
    url: "https://archive.org/details/lettersoffyodorm00dostuoft"
    accessed: 2026-10-15
    reliability_note: "Edited translation with chronology; library scan."
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

# Fyodor Dostoevsky

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Fyodor Dostoevsky (1821–1881), Russian novelist: Poor Folk (1846) to The Brothers Karamazov (1879–80) [S1, S2]. In an 1854 letter he called himself 'a child of unfaith and scepticism' who would 'stay with Christ and not with truth' [S2, Letter XXII]. Draft: CHRIST 0.5; A BELOW_THRESHOLD; B UNKNOWN; mid_basin UNKNOWN.

## Life and work

Engineering academy; arrest 1849 and Siberia; novels and journalism [S1].

## Contribution and impact

Four long novels and Notes from the Underground [S1].

## Childhood and education

Doctor's son; home schooling, then boarding school [S1].

## Adult working worldview

Christ-centred creed in one private letter [S2].

## Heritage (context only)

Russian [S1].

## Timing

First lasting contribution 1846, at 25 [S2].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No circle [S2].

## Open questions

- Diary of a Writer.

## Research log

- 2026-10-15: Read Britannica and Mayne 1914 (archive.org OCR).
