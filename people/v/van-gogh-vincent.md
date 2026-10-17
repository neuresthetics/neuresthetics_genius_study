---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch M)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-17
  last_updated: 2026-10-17
  change_log:
    - {date: 2026-10-17, by: "Grok Bot", summary: "Record created (stage 3 batch M, order P32: F 5, rank 78). Basics from Britannica (Britannica Editors, unsigned; body only, Q&A boxes not cited). Worldview from letters 155 (1880), 613, 632 and 691 (1888) in the Van Gogh Museum / Huygens ING edition. primary_system BELOW_THRESHOLD; A 0 (0.5, alt 1); B UNKNOWN (P16); mid_basin UNKNOWN (P19). Not plotted. Draft, not reviewed."}

identity:
  id: van-gogh-vincent
  display_name: "Vincent van Gogh"
  roster:
    canonical_name: "Vincent van Gogh"
    rank: 78
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: art
    field_bucket: arts
  full_name: {value: "Vincent Willem van Gogh", certainty: 0.5, cites: [{source: S1, locator: "header"}], how_known: "Britannica header; not repeated in the body read."}
  native_name: {value: UNKNOWN, how_known: "Dutch in Latin script."}
  aliases:
    - {name: "Van Gogh-Vincent", kind: "roster alias"}
    - {name: "Vincent-van-Gogh", kind: "roster alias"}

basics:
  birth:
    date: {value: "1853-03-30", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Zundert, Netherlands", modern_name: "Zundert, Netherlands", polity_then: "Netherlands", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "1890-07-29", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Auvers-sur-Oise, near Paris, France", modern_name: "Auvers-sur-Oise, France", polity_then: "France", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1888, certainty: 0.5, cites: [{source: S1, locator: "'The productive decade' (Arles)"}], how_known: "The Arles works of 1888 'marked his first great period' (S1): the earliest work the body marks as lasting (P13). Weavers (1884) and The Potato Eaters (1885) are dated but not marked lasting. 0.5 because the choice is the coder's."}
  era_bucket: {value: "1850 to 1949", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "From 1888 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Netherlands (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Netherlands, Belgium, France."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [Dutch, French], certainty: 0.5, cites: [{source: S2, locator: "letters 613, 632"}], how_known: "Letters to Theo (Dutch and French) and Bernard (French); coder's summary."}
  occupations: {value: ["painter", "art dealer's employee (Goupil)", "lay preacher and evangelist"], certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}

contribution:
  fields: {value: ["painting", "drawing"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Arles paintings (orchards, sunflowers, portraits of Roulin, the house)", year: 1888, kind: work, lasting: "'marked his first great period' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'The productive decade'"}], how_known: "Britannica."}
    - {value: "The Starry Night", year: 1889, kind: work, lasting: "in the Museum of Modern Art, New York (S1)", certainty: 0.7, cites: [{source: S1, locator: "'The productive decade' (Saint-Rémy; image caption)"}], how_known: "Britannica."}
  evidence_of_impact:
    - {value: "'a powerful influence on the Expressionist movement in modern art'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "'generally considered one of the greatest of the Post-Impressionists' (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Eldest of six children of a Protestant pastor", role: father, certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}
  household_circumstances: {value: TODO}
  schooling: []
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [Dutch], certainty: 0.5, cites: [{source: S1, locator: "'Early life'"}], how_known: "Coder's reading (Brabant village)."}
  notable_events:
    - {value: "Apprenticed at 16 to Goupil and Co., The Hague", age: 16, certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1888–1890", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Protestant upbringing; trained as an evangelist, dismissed by church authorities (1880)", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica: dismissed 'for a too-literal interpretation of Christian teaching'. Context, not a code."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing read on science."}
  primary_system:
    value: BELOW_THRESHOLD
    basis: consistent_private_letters
    certainty: 0.5
    cites: [{source: S2, locator: "letters 613, 632, 691"}]
    rationale: "Theist and Christ-centred language without a church: Christ 'declared eternal life ... to be the principal certainty' (632), 'a tremendous need for ... religion' (691), and a God whose world is 'one of his studies that turned out badly' (613). CHRIST, CLTHEI and DEISM all partly fit; the church had dismissed him (S1)."
    how_known: "Several private letters; nothing picks a system."
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Christ as the 'principal certainty' of eternal life (632); but outside any church after 1880 (S1)."}
    - {code: CLTHEI, reason: "God as 'the same creative hand' who may take 'revenge' (613)."}
    - {code: DEISM, reason: "A God who made the world and then is judged by it (613); no rejection of revelation read (P27)."}
  lio_axes:
    A_locus:
      value: 0
      basis: consistent_private_letters
      certainty: 0.5
      cites: [{source: S2, locator: "letter 613 (Arles, 26 May 1888); letter 155 (Cuesmes, June 1880)"}]
      how_known: "Private letters in the working years and before; 0.5 because the 1888 passage is ironic and framed as 'legend', and an alternative is named."
      rationale: "God as the world's author, apart from it: 'we shouldn't judge the Good Lord by this world, because it's one of his studies that turned out badly' and 'the same creative hand' (1888). Named alternative: 1 ('the best way of knowing God is to love a great deal', 1880, and the stars painted from a need for religion, 1888)."
    B_cause: {value: UNKNOWN, how_known: "Not a scientist; 'This world was clearly cobbled together in haste' (613) judges the world's quality, not law or exception (P16). Nothing read on nature's order."}
    C_ledger: {value: UNKNOWN, how_known: "'the hope of seeing better than that in another life' (613) is a hope, with no judgement of persons; not scored."}
    D_authority: {value: UNKNOWN, how_known: "Nothing read."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7)."}
  mid_basin: {value: UNKNOWN, how_known: "B is UNKNOWN (P19)."}
  statements:
    - text: "I’m thinking more and more that we shouldn’t judge the Good Lord by this world, because it’s one of his studies that turned out badly."
      cites: [{source: S2, locator: "letter 613, to Theo van Gogh, Arles, 26 May 1888"}]
      date: "1888-05-26"
      context: "To Theo; the letter goes on: 'What legend tells us about the Good Lord is that he went to enormous trouble over this study of his for a world. I’m inclined to believe that the legend tells the truth'."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-17
      note: "English translation of the edition, checked word for word against the edition's web page."
    - text: "That doesn’t stop me having a tremendous need for, shall I say the word — for religion — so I go outside at night to paint the stars"
      cites: [{source: S2, locator: "letter 691, to Theo van Gogh, Arles, on or about 29 September 1888"}]
      date: "1888-09-29"
      context: "To Theo."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-17
      note: "As above."
    - text: "Christ — alone — among all the philosophers, magicians, &c. declared eternal life – the endlessness of time, the non-existence of death – to be the principal certainty."
      cites: [{source: S2, locator: "letter 632, to Emile Bernard, Arles, 26 June 1888"}]
      date: "1888-06-26"
      context: "To Bernard."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-17
      note: "As above."
    - text: "But without intending it, I’m always inclined to believe that the best way of knowing God is to love a great deal."
      cites: [{source: S2, locator: "letter 155, to Theo van Gogh, Cuesmes, c. 22–24 June 1880"}]
      date: "1880-06"
      context: "To Theo, after his dismissal as an evangelist; before the working years (P20)."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-17
      note: "As above."
  changes_over_life:
    - {value: "Dismissed as an evangelist; 'feeling that his faith was destroyed'", year: 1880, age: 27, certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica (winter 1879–80)."}
  coder_notes: "Coder's call. The letters are rich, and only four were read. Letter 613's 'study that turned out badly' is ironic, which is why A is 0.5. A search of the edition for nature, laws and miracles is the lead for B."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Dutch", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Protestant (son of a Protestant pastor)", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica; denomination not named."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1888–1890", certainty: 0.5, cites: [{source: S1, locator: "'The productive decade'"}], how_known: "First listed lasting contribution (1888) to his death (P29, P30); start is the coder's pick."}
  age_at_first_lasting_contribution: {value: 35, certainty: 0.5, cites: [{source: S1, locator: "opening; Arles 1888"}], how_known: "1888 − 1853 = 35 (P30)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No LIO-type view found."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S2, locator: "letters read"}], how_known: "Four letters read."}
  worldview_during_major_work: {value: "Theist without a church: God as the world's author, Christ as the certainty of eternal life (1888)", certainty: 0.5, cites: [{source: S2, locator: "letters 613, 632"}], how_known: "Private letters, 1888."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Nothing read.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Nothing read."}
  circle_present: {value: "unclear", rationale: "God as maker of the world; nothing on return or end.", certainty: 0.5, cites: [{source: S2, locator: "letter 613"}], how_known: "Coder's reading."}
  reading: "Churchless theist in the Arles letters."
  notes: ""

institutions:
  - {value: "Goupil and Co. (The Hague, London, Paris)", role: employee, years: "1869–1876", kind: other, certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica; start year from 'At 16'."}
collaborators:
  - {value: "Theo van Gogh", relation: family, note: "brother and main correspondent", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 78"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags: []
  open_questions:
    - "Search the letters edition for nature, law, miracle and providence for B."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "Britannica Editors. \"Vincent van Gogh.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Vincent-van-Gogh. Read in Wayback snapshots: main page 2026-09-22 02:13:55 UTC; 'The productive decade' 20260217004628; 'Legacy' 20260922021354."
    url: "https://www.britannica.com/biography/Vincent-van-Gogh"
    accessed: 2026-10-17
    reliability_note: "Unsigned editors' article (JSON-LD author 'Britannica Editors'). Body only; Q&A boxes and Top Questions not cited. Live page not compared."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: primary
    kind: scholarly edition
    author: "Vincent van Gogh"
    citation: "Van Gogh, Vincent. Vincent van Gogh – The Letters, ed. Leo Jansen, Hans Luijten and Nienke Bakker. Amsterdam and The Hague: Van Gogh Museum and Huygens ING. https://vangoghletters.org/vg/ (letters 155, 613, 632, 691)."
    url: "https://vangoghletters.org/vg/"
    accessed: 2026-10-17
    reliability_note: "Critical edition with the editors' English translation; letter numbers are the edition's."
    used_for: [basics, worldview, timing, lane_b]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-17
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Vincent van Gogh

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Vincent van Gogh (1853–1890), Dutch Post-Impressionist painter [S1]. Draft: primary_system BELOW_THRESHOLD; A 0 at 0.5 (alt 1); B UNKNOWN; mid_basin UNKNOWN. Not plotted.

## Life and work

Goupil; lay preacher and evangelist; painter from 1880; Arles 1888; Saint-Rémy 1889; Auvers 1890 [S1].

## Contribution and impact

Arles works of 1888, his 'first great period'; The Starry Night (1889) [S1].

## Childhood and education

Son of a Protestant pastor, Brabant [S1].

## Adult working worldview

'we shouldn’t judge the Good Lord by this world, because it’s one of his studies that turned out badly' (1888) [S2].

## Heritage (context only)

Dutch, Protestant pastor's family [S1].

## Timing

First lasting contribution 1888, at 35 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Unclear.

## Open questions

- Letters on nature for B.

## Research log

- 2026-10-17: Read Britannica (Editors) in Wayback copies; read letters 155, 613, 632 and 691 on vangoghletters.org.
