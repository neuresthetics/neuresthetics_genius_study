---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA6)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA6, order P32: F 3, rank 202). Sources: Britannica, signed by B.R. Nanda (scholars edition, read in full), and the Introduction to Gandhi's Autobiography (1927–29, tr. Mahadev Desai), read in full on mkgandhi.org (unofficial web copy). Lasting work: satyagraha, 'born' at the Johannesburg mass meeting of September 1906 (S1); Nanda calls him the 'catalyst' of 'three of the major revolutions of the 20th century'. Span 1906, age 37. Own words: 'to see God face to face, to attain Moksha' and 'He alone is real and all else is unreal' (S2, Introduction signed 26 November 1925); 'I call myself a Sanatani Hindu' (Young India, dated 6 October 1921 in the Truth Is God anthology, S4; date not verified in CWMG); Young India 1924, 'to attain moksha in this very existence' (quoted in S1). All after the span: P20 cap 0.5. primary_system HINDU 0.5 (written_profession, on the explicit 'Sanatani Hindu' self-identification, RQ-AA6-1), alternative BELOW_THRESHOLD (he held all religions 'true' yet 'imperfect', S1). A BELOW_THRESHOLD: 'God as Truth', 'He alone is real' (acosmic, A 4 lead) against 'see God face to face' (personal, A 2 or lower lead); not a scientist, B UNKNOWN; mid_basin BELOW_THRESHOLD. region_of_work Sub-Saharan Africa for the span (South Africa), South Asia afterwards. Not plotted. Draft, not reviewed."}

identity:
  id: gandhi-mahatma
  display_name: "Mahatma Gandhi"
  roster:
    canonical_name: "Mahatma Gandhi"
    rank: 202
    F: 3
    models: [DeepSeek, Gemini, Grok]
    band: "core (3–4)"
    status: "core"
    field: "political thought"
    field_bucket: "politics / law / military"
  full_name: {value: "Mohandas Karamchand Gandhi", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  native_name: {value: UNKNOWN, how_known: "Gujarati script form not printed in the sources read."}
  aliases:
    - {name: "Gandhi-Mahatma", kind: "roster alias"}
    - {name: "Mohandas Karamchand Gandhi", kind: "birth name"}
    - {name: "Mahatma", kind: "title or honorific"}

basics:
  birth:
    date: {value: "1869-10-02", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
    place: {value: "Porbandar", modern_name: "Porbandar, Gujarat, India", polity_then: "Porbandar State, British India", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  death:
    date: {value: "1948-01-30", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica: assassinated."}
    place: {value: "Delhi", modern_name: "New Delhi, India", polity_then: "Dominion of India", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1906, certainty: 0.7, cites: [{source: S1, locator: "Emergence as a political and social activist"}], how_known: "Satyagraha 'born' at the Johannesburg mass meeting, September 1906 (S1): a documented public statement (P30)."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "text"}], how_known: "1906 (P2)."}
  region_of_birth: {value: "South Asia", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "India (P3)."}
  region_of_work: {value: "Sub-Saharan Africa", certainty: 0.5, cites: [{source: S1, locator: "Emergence as a political and social activist"}], how_known: "Johannesburg during the 1906 span (region of work follows where the span took place, v8's call on the AA6 audit); alternative South Asia, the home region, where his campaigns from 1915 took place."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Gujarati", "English"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Hind Swaraj and the autobiography in Gujarati; Young India in English (S1)."}
  occupations: {value: ["lawyer", "political leader", "writer"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}

contribution:
  fields: {value: ["political thought", "nonviolent resistance"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Satyagraha (nonviolent resistance)", year: 1906, kind: "method", lasting: "Nanda: he became 'the catalyst if not the initiator of three of the major revolutions of the 20th century' (S1); his method influenced Martin Luther King, Jr. (S1)", certainty: 0.7, cites: [{source: S1, locator: "Emergence as a political and social activist; Place in history"}], how_known: "Britannica."}
  evidence_of_impact:
    - {value: "Influence on Martin Luther King, Jr., and the civil-rights movement", kind: "assessment by a later major figure", certainty: 0.7, cites: [{source: S1, locator: "Place in history"}], how_known: "Britannica."}
  major_works:
    - {value: "Hind Swaraj", year: 1909, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
    - {value: "Salt March", year: 1930, kind: "other", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
    - {value: "An Autobiography: The Story of My Experiments with Truth", year: 1927, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica: 1927–29."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Originator of satyagraha (S1).", certainty: 0.7, cites: [{source: S1, locator: "Place in history"}], how_known: "Britannica."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Father Karamchand Gandhi, dewan (chief minister) of Porbandar; mother Putlibai, deeply religious", role: "family", certainty: 0.7, cites: [{source: S1, locator: "Early years"}], how_known: "Britannica."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling:
    - {value: "Schools in Rajkot; law at the Inner Temple, London (called to the bar 1891)", certainty: 0.7, cites: [{source: S1, locator: "Early years"}], how_known: "Britannica."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1906", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: 
    value: HINDU
    basis: written_profession
    certainty: 0.5
    cites: [{source: S4, locator: "Why I Am A Hindu"}, {source: S2, locator: "Introduction"}, {source: S1, locator: "Religious quest"}]
    how_known: "Young India, 1921 (S4; date as the anthology gives it, not verified in CWMG; other copies give 10 June 1921), and the Autobiography Introduction (1925); all after the 1906 span (P20 cap 0.5)."
    rationale: "Explicit self-identification: 'I call myself a Sanatani Hindu, because ... I believe in the Vedas, the Upanishads, the Puranas' (S4). Supporting: aim 'to see God face to face, to attain Moksha' (S2); the Gita his 'spiritual dictionary' (S1). RQ-AA6-1 (v8's call on the auditor's advice). Alternative BELOW_THRESHOLD: he held all religions 'true' yet 'imperfect' (S1) and names no tradition in S2."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: HINDU, reason: "Coded at 0.5 (S4, S2, S1)."}
    - {code: JAIN, reason: "Lead: Jain tinge of the Vaishnava home; mentor Shrimad Rajchandra (S1); heritage, not profession."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "Mixed: 'He alone is real and all else is unreal' and 'I worship God as Truth only' (S2) lean to A 4; 'to see God face to face' leans personal (A 2 or lower). No reading reaches 0.5 over the other."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30); no statement on nature read."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD, so the P4 test cannot be applied (Pavlov pattern)."}
  statements:
    - text: "What I want to achieve - what I have been striving and pining to achieve these thirty years - is self-realization, to see God face to face, to attain Moksha. I live and move and have my being in pursuit of this goal."
      cites: [{source: S2, locator: "Introduction"}]
      date: "1925-11-26"
      context: "Introduction to the Autobiography, signed 26 November 1925 (tr. Desai); after the span."
      axes: [A_locus]
      kind: "autobiography"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-19
      note: "mkgandhi.org transcription of the Desai translation."
    - text: "Often in my progress I have had faint glimpses of the Absolute Truth, God, and daily the conviction is growing upon me that He alone is real and all else is unreal."
      cites: [{source: S2, locator: "Introduction"}]
      date: "1925-11-26"
      context: "Same Introduction."
      axes: [A_locus]
      kind: "autobiography"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-19
      note: "Acosmic reading: the A 4 lead."
    - text: "I call myself a Sanatani Hindu, because, 1. I believe in the Vedas, the Upanishads, the Puranas and all that goes by the name of Hindu scriptures, and therefore in Avataras and rebirth;"
      cites: [{source: S4, locator: "Why I Am A Hindu"}]
      context: "Young India; the Truth Is God anthology dates it 6 October 1921 (other copies give 10 June 1921); date not verified in CWMG, so left undated here; after the span."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-19
      note: "mkgandhi.org transcription of the anthology (comp. R.K. Prabhu)."
    - text: "I am impatient to realize myself, to attain moksha in this very existence."
      cites: [{source: S1, locator: "Religious quest"}]
      date: "1924"
      context: "Young India, 1924, as quoted by Nanda; after the span."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-19
      note: "Quoted in S1."
  changes_over_life: []
  coder_notes: "Hind Swaraj (1909) and the Natal-era writings would give within-span own words; not read."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: "Hindu (Vaishnava, with a Jain tinge)", certainty: 0.7, cites: [{source: S1, locator: "Early years"}], how_known: "Britannica."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1906", certainty: 0.7, cites: [{source: S1, locator: "Emergence as a political and social activist"}], how_known: "The one listed lasting item (P29, P30)."}
  age_at_first_lasting_contribution: {value: 37, certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "1906 − 1869 = 37 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Ethical and political method (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "Natal Indian Congress", role: "founder", years: "1894", kind: "other", certainty: 0.7, cites: [{source: S1, locator: "Emergence as a political and social activist"}], how_known: "Britannica."}
  - {value: "Indian National Congress", role: "leader", years: "1920s–1940s", kind: "other", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
collaborators:
  - {value: "Shrimad Rajchandra", relation: "teacher", note: "Jain mentor", certainty: 0.7, cites: [{source: S1, locator: "Religious quest"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 202"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Profession after the span (P20)."
  open_questions:
    - "Within-span own words (Hind Swaraj 1909); CWMG date of the Sanatani Hindu passage."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "B.R. Nanda"
    citation: "Nanda, B.R. 'Mahatma Gandhi.' Encyclopaedia Britannica (scholars edition). https://kids.britannica.com/scholars/article/Mahatma-Gandhi/109421"
    url: "https://kids.britannica.com/scholars/article/Mahatma-Gandhi/109421"
    accessed: 2026-10-19
    reliability_note: "Signed article, scholars edition, read in full."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "M.K. Gandhi"
    citation: "Gandhi, M.K. An Autobiography or The Story of My Experiments with Truth, tr. Mahadev Desai. Introduction. mkgandhi.org. https://www.mkgandhi.org/autobio/intro.php"
    url: "https://www.mkgandhi.org/autobio/intro.php"
    accessed: 2026-10-19
    reliability_note: "Unofficial web copy of the Desai translation; Introduction read in full."
    used_for: [worldview]
  - id: S3
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [review]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "M.K. Gandhi, comp. R.K. Prabhu"
    citation: "Gandhi, M.K. Truth Is God, comp. R.K. Prabhu, ch. 22 'Why I Am A Hindu' (from Young India). mkgandhi.org. https://www.mkgandhi.org/truthisgod/22hindu.php"
    url: "https://www.mkgandhi.org/truthisgod/22hindu.php"
    accessed: 2026-10-19
    reliability_note: "Unofficial web copy of an anthology of his writings; chapter read in full."
    used_for: [worldview]
---

## Summary

Mahatma Gandhi (1869–1948), originator of satyagraha [S1]. Draft: HINDU (0.5). Not plotted.

## Life and work

Porbandar; London; South Africa; India [S1].

## Contribution and impact

Satyagraha, 1906 [S1].

## Childhood and education

Rajkot; Inner Temple [S1].

## Adult working worldview

'I call myself a Sanatani Hindu' (Young India, 1921) [S4]; 'to see God face to face' (1925) [S2].

## Heritage (context only)

Vaishnava, Jain tinge [S1].

## Timing

1906, age 37 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Within-span own words.

## Research log

- 2026-10-19: Read Britannica (Nanda, scholars edition); autobiography Introduction.
