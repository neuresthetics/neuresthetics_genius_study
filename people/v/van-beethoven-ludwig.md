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
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch H, order P32: F 5, rank 53). Basics from Britannica (Budden), signed body only (work years given only in the Top Questions box are not used). Worldview from letters in Nohl's collection, Lady Wallace's translation, Gutenberg #13065 (web copy, 0.7 cap): Heiligenstadt document 1802, letter to Zmeskall 1813. Not a scientist (P30). primary_system BELOW_THRESHOLD (candidates CHRIST, CLTHEI, DEISM); A 0 at 0.7 (alt 1); B BELOW_THRESHOLD (Providence statements are about his life, not nature, P16); C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD. Not plotted. No datable lasting contribution in the signed body read (P39). Draft, not reviewed."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Batch H audit (cae9cb2, run 1: hold; note on timing): signed Britannica sections re-checked; no dated lasting work is citable, so the timing fields stay UNKNOWN. No value changes."}

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
  native_name: {value: UNKNOWN, how_known: "German, same Latin-script form."}
  aliases: []

basics:
  birth:
    date: {value: UNKNOWN, how_known: "Only the baptism date is given: 17 December 1770 (S1); the birth year is taken as 1770 for ages."}
    place: {value: "Bonn, archbishopric of Cologne", modern_name: "Bonn, Germany", polity_then: "Electorate of Cologne", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica (place of baptism)."}
  death:
    date: {value: "1827-03-26", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Vienna, Austria", modern_name: "Vienna, Austria", polity_then: "Austrian Empire", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: UNKNOWN, how_known: "The signed body read dates his first extant composition (1783) but calls the Bonn works of more interest to the student than to the ordinary music lover; the dated symphonies appear only in the Top Questions box, which is not cited (P39)."}
  era_bucket: {value: "1750 to 1849", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "His whole life (1770–1827) falls in the bucket (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Germany is Western Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.5, cites: [{source: S1, locator: "'The early years'"}], how_known: "Vienna from 1792; Austria assigned as in regions.csv (coder's reading, 0.5)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [German], certainty: 0.7, cites: [{source: S2, locator: "title page (letters translated from the German)"}], how_known: "Letters."}
  occupations: {value: ["composer", "pianist"], certainty: 0.7, cites: [{source: S1, locator: "opening; 'The early years'"}], how_known: "Britannica."}

contribution:
  fields: {value: ["music"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Widened the scope of sonata, symphony, concerto and quartet; Ninth Symphony combined vocal and instrumental music", kind: work, lasting: "'Widely regarded as the greatest composer who ever lived' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica; no year in the body read (P39)."}
  evidence_of_impact:
    - {value: "'the fountainhead of much that characterized the work of the Romantics who followed him'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
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
  working_years: {value: UNKNOWN, how_known: "No dated major-work period (P39)."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system:
    value: BELOW_THRESHOLD
    basis: consistent_private_letters
    certainty: 0.5
    cites: [{source: S2, locator: "No. 26 (1802); No. 109 (1813)"}]
    rationale: "Theist language (God who 'looks into my heart', 'O Providence!', 'the Almighty') but nothing that picks a system: CHRIST, CLTHEI and DEISM all fit. Bonn's ruler was 'a liberal Roman Catholic' (S1), context only."
    how_known: "Two letters in a web-copy translation."
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Commends correspondents 'to the grace of God' (No. 25); nothing doctrinal read."}
    - {code: CLTHEI, reason: "A providential personal God."}
    - {code: DEISM, reason: "'the temple of Nature'; no rejection of revelation (P27)."}
  lio_axes:
    A_locus:
      value: 0
      basis: consistent_private_letters
      certainty: 0.7
      cites: [{source: S2, locator: "No. 26 (Heiligenstadt, 6 Oct. 1802); No. 109 (to Zmeskall, 26 Apr. 1813)"}]
      how_known: "Consistent across two private documents eleven years apart (0.7 ceiling); web-copy translation; alternative named."
      rationale: "A personal God who 'looks into my heart, He searches it' (1802) and an Almighty who will 'prevent my being utterly ruined' (1813): a God apart from the world who acts in a life. Named alternative: 1 ('the temple of Nature and of man', 1802)."
    B_cause: {value: BELOW_THRESHOLD, how_known: "The Providence statements are about his own life, not the order of nature (P16); no statement on nature's laws read."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read (P7)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "B is BELOW_THRESHOLD."}
  statements:
    - text: "God looks into my heart, He searches it, and knows that love for man and feelings of benevolence have their abode there!"
      cites: [{source: S2, locator: "No. 26, Heiligenstadt, Oct. 6, 1802"}]
      date: "1802-10-06"
      context: "The document to his brothers Carl and Johann (the Heiligenstadt Testament)."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "Lady Wallace's translation via Gutenberg #13065; web copy, 0.7 cap."
    - text: "O Providence! vouchsafe me one day of pure felicity!"
      cites: [{source: S2, locator: "No. 26"}]
      date: "1802-10-06"
      context: "Same document."
      axes: [A_locus, B_cause]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "As above."
    - text: "But the Almighty will no doubt prevent my being utterly ruined."
      cites: [{source: S2, locator: "No. 109, to Zmeskall, April 26, 1813"}]
      date: "1813-04-26"
      context: "On a postponed concert."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "As above."
  changes_over_life: []
  coder_notes: "Coder's call; volume 2 of the letters and the conversation books not read."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Flemish origin (Malines)", certainty: 0.7, cites: [{source: S1, locator: "'The early years'"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: "Baptized 17 December 1770, Bonn", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica; church not named."}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: UNKNOWN, how_known: "No dated lasting work in the signed body read (P39)."}
  age_at_first_lasting_contribution: {value: UNKNOWN, how_known: "As above."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "B is BELOW_THRESHOLD."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S2, locator: "Nos. 26, 109"}], how_known: "No statement on nature's order read."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "No dated period."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Nothing read.", certainty: 0.5, cites: [{source: S1, locator: "'The early years'"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "'The early years'"}], how_known: "Left school by 11."}
  circle_present: {value: "no", rationale: "A personal, providential God; no lawful-order statement.", certainty: 0.5, cites: [{source: S2, locator: "Nos. 26, 109"}], how_known: "Coder's reading."}
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
  data_quality_flags: []
  open_questions:
    - "Date the lasting works from a citable body text; read volume 2 of the letters."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Julian Medforth Budden"
    citation: "Budden, Julian Medforth. \"Ludwig van Beethoven.\" Encyclopaedia Britannica, updated 12 October 2026. https://www.britannica.com/biography/Ludwig-van-Beethoven."
    url: "https://www.britannica.com/biography/Ludwig-van-Beethoven"
    accessed: 2026-10-15
    reliability_note: "Signed article body (opening and 'The early years'); the Top Questions box is not used. Britannica lists several contributors; the byline shown was Julian Medforth Budden in one fetch and Raymond L. Knapp in another on 2026-10-15. Re-checked after the batch H audit: the signed sections the page returns end with 'The early years' and date no lasting work, so the timing fields stay UNKNOWN (P39). Lead, not cited: the Britannica Kids Scholars edition dates the Op. 1 piano trios (published 1795)."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: primary
    kind: letter
    author: "Ludwig van Beethoven"
    citation: "Beethoven, Ludwig van. Beethoven's Letters 1790-1826, Volume 1. From the collection of Dr. Ludwig Nohl. Trans. Lady Grace Wallace. Project Gutenberg eBook #13065."
    url: "https://www.gutenberg.org/ebooks/13065"
    accessed: 2026-10-15
    reliability_note: "Translated letters in an unofficial web copy; §7 cap 0.7."
    used_for: [basics, worldview, timing, lane_b]
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

# Ludwig van Beethoven

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Ludwig van Beethoven (baptized 1770–1827), German composer [S1]. Draft: primary_system BELOW_THRESHOLD; A 0 at 0.7; B BELOW_THRESHOLD; C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD. Not plotted.

## Life and work

Bonn court musician; to Vienna in 1792 [S1].

## Contribution and impact

Widened sonata, symphony, concerto and quartet [S1].

## Childhood and education

Musicians' family; left school by 11; taught by Neefe [S1].

## Adult working worldview

'God looks into my heart' (1802); 'the Almighty will no doubt prevent my being utterly ruined' (1813) [S2].

## Heritage (context only)

Flemish origin [S1].

## Timing

No dated lasting work in the sources read [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No circle [S2].

## Open questions

- Dates of lasting works.

## Research log

- 2026-10-15: Read Britannica (Budden, opening and 'The early years') and letters Nos. 25, 26, 109 (Gutenberg #13065).
