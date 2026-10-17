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
    - {date: 2026-10-17, by: "Grok Bot", summary: "Record created (stage 3 batch M, order P32: F 5, rank 79). Basics from Britannica (Panthea Reid, signed; body only). Worldview from 'A Sketch of the Past' (memoir, 1940–41, published 1976) quoted by Ryan (2012, Glasgow PhD) and the 1928 letter to Vanessa Bell quoted by Tóibín (LRB, 2014): secondary quotations, primary check pending. primary_system ATHE (0.5, alt AGNOS); A 4 (0.7); B UNKNOWN (P16); mid_basin false (0.7, A ≥ 3 branch). Not plotted. Draft, not reviewed."}

identity:
  id: woolf-virginia
  display_name: "Virginia Woolf"
  roster:
    canonical_name: "Virginia Woolf"
    rank: 79
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: literature
    field_bucket: literature
  full_name: {value: "Adeline Virginia Woolf, née Stephen", certainty: 0.5, cites: [{source: S1, locator: "header; 'Early life and influences' ('Born Virginia Stephen')"}], how_known: "Britannica gives 'Born Virginia Stephen'; 'Adeline' is from the header only."}
  native_name: {value: UNKNOWN, how_known: "English."}
  aliases:
    - {name: "Virginia-Woolf", kind: "roster alias"}
    - {name: "Woolf-Virginia", kind: "roster alias"}

basics:
  birth:
    date: {value: "1882-01-25", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "London, England", modern_name: "London, United Kingdom", polity_then: "United Kingdom", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "1941-03-28", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "near Rodmell, Sussex, England", modern_name: "Rodmell, East Sussex, United Kingdom", polity_then: "United Kingdom", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1922, certainty: 0.5, cites: [{source: S1, locator: "'Mrs. Dalloway, To the Lighthouse, ...' (Jacob's Room)"}], how_known: "In Jacob's Room (1922) 'she achieved such emotion' (S1): the earliest novel the body marks as an achievement (P13). The Voyage Out (1915) is dated but not so marked. 0.5 because the choice is the coder's."}
  era_bucket: {value: "1850 to 1949", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "From 1922 (P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "United Kingdom (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "London and Sussex."}
  sex_as_recorded: {value: "female", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [English], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
  occupations: {value: ["novelist", "essayist", "publisher (Hogarth Press)"], certainty: 0.7, cites: [{source: S1, locator: "opening; Hogarth Press paragraph"}], how_known: "Britannica."}

contribution:
  fields: {value: ["fiction", "essays", "literary criticism"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Jacob's Room", year: 1922, kind: work, lasting: "'she achieved such emotion' (S1)", certainty: 0.7, cites: [{source: S1, locator: "major works section"}], how_known: "Britannica."}
    - {value: "Mrs. Dalloway", year: 1925, kind: work, lasting: "among the novels she 'is best known for' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    - {value: "To the Lighthouse", year: 1927, kind: work, lasting: "among the novels she 'is best known for' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    - {value: "Between the Acts", year: 1941, kind: work, lasting: "worked on during the bombing of London, 1940–41 (S1)", certainty: 0.5, cites: [{source: S1, locator: "major works section"}], how_known: "Britannica; published after her death; lasting status is the coder's reading."}
  evidence_of_impact:
    - {value: "Her novels 'exerted a major influence on the genre'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father Leslie Stephen, literary figure, first editor of the Dictionary of National Biography", role: father, certainty: 0.7, cites: [{source: S1, locator: "'Early life and influences'"}], how_known: "Britannica."}
    - {value: "Mother Julia Jackson (Duckworth)", role: mother, certainty: 0.7, cites: [{source: S1, locator: "'Early life and influences'"}], how_known: "Britannica."}
  household_circumstances: {value: TODO}
  schooling: []
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [English], certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1922–1941", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing read on science."}
  primary_system:
    value: ATHE
    basis: consistent_private_letters
    certainty: 0.5
    cites: [{source: S2, locator: "Introduction, p. 1 (PDF p. 8), quoting MB 85"}, {source: S3, locator: "Woolf letter quoted"}]
    rationale: "'certainly and emphatically there is no God' (memoir) and 'there's something obscene in a living person sitting by the fire and believing in God' (1928 letter). Named alternative: AGNOS or SECHUM; ATHE's naturalism is not stated, and the same passage holds that 'behind the cotton wool is hidden a pattern' and 'the whole world is a work of art'."
    how_known: "Unpublished memoir and a private letter, both secondary quotations (primary check pending); 0.5 because the naturalism half of ATHE is not stated and alternatives are named."
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: ATHE, reason: "Explicit denial of God."}
    - {code: AGNOS, reason: "Her own words are a denial, not a suspension of judgement."}
    - {code: SECHUM, reason: "No membership or humanist statement read."}
  lio_axes:
    A_locus:
      value: 4
      basis: consistent_private_letters
      certainty: 0.7
      cites: [{source: S2, locator: "Introduction, p. 1 (PDF p. 8), quoting MB 85"}, {source: S3, locator: "Woolf letter quoted"}]
      how_known: "Two private documents in the working years, consistent (0.7 ceiling, §3); both secondary quotations, primary check pending, so not above 0.7 (P26)."
      rationale: "No God (A 4 for a denial, P38): 'certainly and emphatically there is no God; we are the words; we are the music; we are the thing itself' (memoir, 1940–41), and on Eliot's conversion, 'A corpse would seem to me more credible than he is. I mean, there's something obscene in a living person sitting by the fire and believing in God' (letter, 1928)."
    B_cause: {value: UNKNOWN, how_known: "Not a scientist. The memoir's 'pattern' behind 'the cotton wool' and 'the whole world is a work of art' is not a statement on law and exception in nature (P16). Nothing read on nature's order."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read on reward or punishment; Eliot's belief in 'immortality' is reported, not judged in her own terms."}
    D_authority: {value: UNKNOWN, how_known: "Nothing read."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7)."}
  mid_basin: {value: false, certainty: 0.7, cites: [{source: S2, locator: "Introduction, p. 1 (PDF p. 8), quoting MB 85"}, {source: S3, locator: "Woolf letter quoted"}], how_known: "A 4 at 0.7: the A ≥ 3 branch reads A only (P10), so B UNKNOWN does not block it."}
  statements:
    - text: "But there is no Shakespeare, there is no Beethoven; certainly and emphatically there is no God; we are the words; we are the music; we are the thing itself."
      cites: [{source: S2, locator: "Introduction, p. 1 (PDF p. 8), quoting MB 85"}]
      date: "1940"
      context: "'A Sketch of the Past', the memoir she worked on during the bombing of London (S1), published in Moments of Being (1976; Ryan cites the Pimlico edition, p. 85). The sentence follows 'that behind the cotton wool is hidden a pattern ... that the whole world is a work of art'."
      axes: [A_locus]
      kind: "unpublished manuscript"
      verified_against: "secondary quotation"
      verified_on: 2026-10-17
      note: "Primary check pending (P26): Moments of Being not read. The same wording appears in Garrity (Edinburgh UP chapter) and the UAH Woolf page, seen in search text only."
    - text: "I have had a most shameful and distressing interview with poor dear Tom Eliot, who may be called dead to us all from this day forward. He has become an Anglo-Catholic, believes in God and immortality, and goes to church. I was really shocked. A corpse would seem to me more credible than he is. I mean, there’s something obscene in a living person sitting by the fire and believing in God."
      cites: [{source: S3, locator: "Woolf letter quoted"}]
      date: "1928"
      context: "To her sister Vanessa Bell, 1928, on Eliot's conversion (S3). Leads only: the month (February) in the summary on the Cambridge chapter page (Lewis 2011), and the locator Letters III: 457–58 in a journal article seen only in search text."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-17
      note: "Primary check pending (P26): The Letters of Virginia Woolf, vol. III, not read."
  changes_over_life: []
  coder_notes: "Coder's call. The letter mocks belief rather than stating her own creed, so it supports the memoir's denial instead of standing alone. The Cambridge chapter page (Lewis 2011) labels its opening a 'Summary', so it is a lead only and is not cited."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "English", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1922–1941", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "First to last listed lasting contribution (P29, P30); start and end are the coder's picks."}
  age_at_first_lasting_contribution: {value: 40, certainty: 0.5, cites: [{source: S1, locator: "opening; 1922"}], how_known: "1922 − 1882 = 40 (P30)."}
  first_evidence_of_lio_type_views: {value: "1928: mocks belief in God in a letter on Eliot's conversion", year: 1928, certainty: 0.5, cites: [{source: S3, locator: "Woolf letter quoted"}], how_known: "Earlier letters and diaries not read (P30 #7)."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.5, cites: [{source: S3, locator: "Woolf letter quoted"}, {source: S2, locator: "Introduction, p. 1 (PDF p. 8)"}], how_known: "1928 and 1940–41, inside 1922–1941; earlier writings not read."}
  worldview_during_major_work: {value: "No God; a 'pattern' behind appearances in which 'we are the thing itself'", certainty: 0.5, cites: [{source: S2, locator: "Introduction, p. 1 (PDF p. 8)"}], how_known: "Secondary quotation of the memoir."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Nothing read.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Nothing read."}
  circle_present: {value: "no", rationale: "No God as source or end.", certainty: 0.5, cites: [{source: S2, locator: "Introduction, p. 1 (PDF p. 8)"}], how_known: "Coder's reading."}
  reading: "No God; immanent pattern."
  notes: ""

institutions:
  - {value: "Hogarth Press (co-founder, 1917)", role: founder, years: "1917–1941", kind: other, certainty: 0.7, cites: [{source: S1, locator: "Hogarth Press paragraph"}], how_known: "Britannica."}
collaborators:
  - {value: "Leonard Woolf", relation: family, note: "husband; co-founder of the Hogarth Press", certainty: 0.7, cites: [{source: S1, locator: "Hogarth Press paragraph"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 79"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Both worldview quotations are secondary; primary check pending."
  open_questions:
    - "Check the memoir against Moments of Being and the letter against Letters vol. III; read the diaries for nature or chance (B)."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Panthea Reid"
    citation: "Reid, Panthea. \"Virginia Woolf.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Virginia-Woolf. Read in Wayback snapshots: main page 2026-09-08 22:14:20 UTC; major works section 20260831164516; 'Legacy' 20250812193713."
    url: "https://www.britannica.com/biography/Virginia-Woolf"
    accessed: 2026-10-17
    reliability_note: "Signed article (Professor of English Emerita, LSU). Body only; Q&A boxes and Top Questions not cited. Live page not compared."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: secondary
    kind: other
    author: "Derek Ryan"
    citation: "Ryan, Derek. Virginia Woolf and the materiality of theory: sex, animal, life. PhD thesis, University of Glasgow, 2012. https://theses.gla.ac.uk/3408/."
    url: "https://theses.gla.ac.uk/3408/1/2012ryanphd.pdf"
    accessed: 2026-10-17
    reliability_note: "Doctoral thesis, read directly (PDF); quotes 'A Sketch of the Past' from Moments of Being (MB 85) in its introduction."
    used_for: [worldview, timing, lane_b]
  - id: S3
    type: secondary
    kind: other
    author: "Colm Tóibín"
    citation: "Tóibín, Colm. \"Putting Religion in Its Place.\" London Review of Books 36, no. 20 (23 October 2014). https://www.lrb.co.uk/the-paper/v36/n20/colm-toibin/putting-religion-in-its-place."
    url: "https://www.lrb.co.uk/the-paper/v36/n20/colm-toibin/putting-religion-in-its-place"
    accessed: 2026-10-17
    reliability_note: "Signed review essay, read directly; quotes the 1928 letter in full and dates it to 1928."
    used_for: [worldview, timing]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-17
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Virginia Woolf

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Virginia Woolf (1882–1941), English novelist and essayist [S1]. Draft: primary_system ATHE (0.5, alt AGNOS); A 4 at 0.7; B UNKNOWN; mid_basin false (0.7). Not plotted.

## Life and work

Born Virginia Stephen; Hogarth Press from 1917 [S1].

## Contribution and impact

Jacob's Room (1922), Mrs. Dalloway (1925), To the Lighthouse (1927) [S1].

## Childhood and education

Daughter of Leslie Stephen and Julia Jackson [S1].

## Adult working worldview

'certainly and emphatically there is no God' (memoir, 1940–41) [S2]; the 1928 letter on Eliot [S3].

## Heritage (context only)

English [S1].

## Timing

First lasting contribution 1922, at 40 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No circle [S2].

## Open questions

- Primary checks; diaries for B.

## Research log

- 2026-10-17: Read Britannica (Reid) in Wayback copies; Ryan's thesis (PDF) and Tóibín (LRB) read directly; Cambridge chapter page (Lewis) seen as a summary only.
