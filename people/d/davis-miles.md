---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch V)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Batch W audit note (gs_2584730_W run 1): S3 (Tingen, a music journalist's book) kind 'scholarly book' -> other. No value changes."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Audit fixes for batch V (gs_982cb8e_V run 1): DV4, Tingen's Miles Beyond ch. 1 recorded as S3, an openable secondary quotation of Miles p. 411 (book still unread); ruling V3 (v8's call on the auditor's advice): primary_system stays UNKNOWN. No scored value changes."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch V, order P32: F 4, rank 119). Basics from Britannica (Britannica Editors, 18 October 2026). No statement of his on God, religion or nature read: the autobiography Miles (1989) was not available, and the one article quoting its religion passage could not be opened. Not a scientist (P30). primary_system, A–E and mid_basin UNKNOWN. Span 1949–1970 (0.5). Not plotted. Draft, not reviewed."}

identity:
  id: davis-miles
  display_name: "Miles Davis"
  roster:
    canonical_name: "Miles Davis"
    rank: 119
    F: 4
    models: [Claude, DeepSeek, Gemini, GPT]
    band: "core (3–4)"
    status: core
    field: music
    field_bucket: music
  full_name: {value: "Miles Dewey Davis III", certainty: 0.7, cites: [{source: S1, locator: "'Also known as'; 'Miles Davis at a Glance'"}], how_known: "Britannica."}
  native_name: {value: "Miles Dewey Davis III", certainty: 0.7, cites: [{source: S1, locator: "'Miles Davis at a Glance'"}], how_known: "English; same as the full name."}
  aliases:
    - {name: "Miles-Davis", kind: "roster alias"}

basics:
  birth:
    date: {value: "1926-05-26", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "'Miles Davis at a Glance' (Born)"}], how_known: "Britannica."}
    place: {value: "Alton, Illinois", modern_name: "Alton, Illinois, USA", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "'Miles Davis at a Glance' (Born)"}], how_known: "Britannica."}
  death:
    date: {value: "1991-09-28", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "'Miles Davis at a Glance' (Died)"}], how_known: "Britannica."}
    place: {value: "Santa Monica, California", modern_name: "Santa Monica, USA", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "'Miles Davis at a Glance' (Died)"}], how_known: "Britannica; pneumonia, respiratory failure and stroke (S1, 'Personal Life')."}
  first_lasting_contribution_year: {value: 1949, certainty: 0.7, cites: [{source: S1, locator: "'Cool jazz and modal jazz' ¶1"}], how_known: "The nonet recordings 'originally released as singles (1949–50)', later Birth of the Cool (1957); dated by first release, range start (P12, P30)."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S1, locator: "'Cool jazz and modal jazz' ¶1"}], how_known: "1949 (P2); one year before the edge."}
  region_of_birth: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "'Miles Davis at a Glance'"}], how_known: "USA (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "'Starting out'"}], how_known: "New York from 1944."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "'Personal Life'"}], how_known: "Britannica."}
  languages_of_work: {value: ["English"], certainty: 0.5, cites: [{source: S1, locator: "'Starting out'"}], how_known: "Coder's reading."}
  occupations: {value: ["jazz trumpeter", "bandleader", "composer"], certainty: 0.7, cites: [{source: S1, locator: "opening; 'Miles Davis at a Glance'"}], how_known: "Britannica."}

contribution:
  fields: {value: ["jazz", "music"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Nonet recordings later collected as Birth of the Cool: bebop improvisation with a thick orchestral texture (cool jazz)", year: 1949, kind: work, lasting: "'changed the course of modern jazz and paved the way for the West Coast styles of the 1950s' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Cool jazz and modal jazz' ¶1"}], how_known: "Britannica; released as singles 1949–50, album 1957. Not a theory of natural systems, so not a scientist (P30)."}
    - {value: "Kind of Blue: modal jazz", year: 1959, kind: work, lasting: "'perhaps the most celebrated album in the history of jazz'; added to the National Recording Registry in 2002 (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Cool jazz and modal jazz' ¶2; 'Honors'"}], how_known: "Britannica."}
    - {value: "In a Silent Way: electric jazz", year: 1969, kind: work, lasting: "'regarded as the seminal album of the jazz fusion movement' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Free jazz and fusion' ¶2"}], how_known: "Britannica."}
    - {value: "Bitches Brew: jazz-rock fusion", year: 1970, kind: work, lasting: "its 'influence was heard in such 1970s fusion groups as Weather Report' and Return to Forever; added to the National Recording Registry in 2025 (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Free jazz and fusion' ¶3; 'Honors'"}], how_known: "Britannica; released 1970."}
  evidence_of_impact:
    - {value: "Regarded, with Armstrong, Ellington and Parker, as 'one of the four most important and influential musicians in jazz history'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "'Personal Life', last paragraph"}], how_known: "Britannica."}
    - {value: "Kind of Blue (2002) and Bitches Brew (2025) added to the Library of Congress National Recording Registry", kind: other, certainty: 0.7, cites: [{source: S1, locator: "'Honors'"}], how_known: "Britannica."}
  major_works:
    - {value: "Miles Ahead; Porgy and Bess; Sketches of Spain (with Gil Evans)", year: 1957, certainty: 0.7, cites: [{source: S1, locator: "'Cool jazz and modal jazz' ¶3"}], how_known: "Britannica: 'monuments of the genre'; years 1957, 1959, 1960."}
    - {value: "Miles: The Autobiography (with Quincy Troupe)", year: 1989, certainty: 0.7, cites: [{source: S1, locator: "'Personal Life', last paragraph"}], how_known: "Britannica."}
  honours:
    - {value: "Grammy Award for lifetime achievement", year: 1990, certainty: 0.7, cites: [{source: S1, locator: "'Honors'"}], how_known: "Britannica."}
    - {value: "Honorary doctorate, New England Conservatory of Music", year: 1986, certainty: 0.7, cites: [{source: S1, locator: "'Honors'"}], how_known: "Britannica."}
  definition_fit: {value: "clearly meets", rationale: "Introduced cool, modal and fusion styles that changed jazz (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not in the sources read."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not in the sources read."}
  parents_and_household:
    - {value: "Father: Miles Davis II, a prosperous dental surgeon in East St. Louis", certainty: 0.7, cites: [{source: S1, locator: "'Starting out' ¶1"}], how_known: "Britannica."}
    - {value: "Mother: Cleota Henry Davis, an accomplished musician", certainty: 0.7, cites: [{source: S1, locator: "'Starting out' ¶1"}], how_known: "Britannica."}
  household_circumstances: {value: "Comfortable, prosperous professional family in East St. Louis, Illinois", certainty: 0.7, cites: [{source: S1, locator: "'Starting out' ¶1"}], how_known: "Britannica: 'his comfortable upbringing'."}
  schooling:
    - {value: "Violin lessons from age 10 (encouraged by his mother); trumpet from his early teens", stage: tutor, run_by: family, certainty: 0.5, cites: [{source: S1, locator: "'Starting out' ¶1"}], how_known: "Britannica; teacher not named, operator the coder's reading."}
    - {value: "Institute of Musical Art (now the Juilliard School), New York; dropped out", stage: university, run_by: private, years: "1944–1945", certainty: 0.7, cites: [{source: S1, locator: "'Starting out' ¶2"}], how_known: "Britannica."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "His first trumpet teacher, who told him to play without vibrato", certainty: 0.7, cites: [{source: S1, locator: "'Starting out' ¶1"}], how_known: "Britannica; unnamed."}
  languages_in_childhood: {value: ["English"], certainty: 0.5, cites: [{source: S1, locator: "'Starting out'"}], how_known: "Coder's reading."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1949–1970", certainty: 0.5, cites: [{source: S1, locator: "'Cool jazz and modal jazz'; 'Free jazz and fusion'"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing read."}
  primary_system: {value: UNKNOWN, how_known: "No statement of his on God or religion read in his own text. Lead: Miles (1989, with Quincy Troupe), p. 411: 'But I do believe in being spiritual and do believe in spirits. I always have. I believe my mother and father come to visit me…' Known from two secondary quotations: Lauren Coyle Rosen's article in The Spiritual Muses (search extract, gives p. 411; the page returns HTTP 500) and Paul Tingen, Miles Beyond ch. 1 (S3, opens; same words, no page), which also reports 'mystery and the supernatural' from the autobiography and Jo Gelbard's 'He was not one for God'. The book itself is unread; the words are after the span (1989, P1 cap 0.5) and from an interview-built autobiography (P42, P43). Ruling V3 (v8's call on the auditor's advice, batch V audit): secondary quotations alone do not move the value, so UNKNOWN stands until p. 411 is read in the book."}
  secondary_system: {value: UNKNOWN, how_known: "One system (P29)."}
  candidate_codes_considered:
    - {code: ANIM, reason: "Not assessed: the 'spirits' lead (Miles p. 411) is known only from secondary quotations (Rosen; Tingen, S3); ruling V3."}
    - {code: AGNOS, reason: "Not assessed: no statement read."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing read (P19)."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30); nothing read (P16, P19)."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read (P19)."}
    D_authority: {value: UNKNOWN, how_known: "Nothing read (P19)."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7, P19)."}
  mid_basin: {value: UNKNOWN, how_known: "A and B are UNKNOWN, which takes precedence (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "Span 1949 (nonet singles, later Birth of the Cool) to 1970 (Bitches Brew); dated by first release. Davis's later work (1980s) is not listed as lasting by S1 ('critics dismissed much of the music Davis released after Bitches Brew'). Lead for the worldview: Miles: The Autobiography (1989, with Quincy Troupe), pp. 148–149 and 411, on spirituality and 'spirits'; written with Troupe from interviews, so if read it may fall under P43's disputed-wording cap and P1 (after the span). Not plotted."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "African American", certainty: 0.5, cites: [{source: S1, locator: "'Personal Life', last paragraph"}], how_known: "Coder's reading of S1 (the racism he faced)."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not in the sources read."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1949–1970", certainty: 0.5, cites: [{source: S1, locator: "'Cool jazz and modal jazz' ¶1; 'Free jazz and fusion' ¶3"}], how_known: "From the nonet singles (1949) to Bitches Brew (1970) (P12, P30). Coder's call on which late album ends the span."}
  age_at_first_lasting_contribution: {value: 23, certainty: 0.7, cites: [{source: S1, locator: "'Miles Davis at a Glance'; 'Cool jazz and modal jazz' ¶1"}], how_known: "1949 − 1926 = 23 (P30)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "Nothing read."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S1, locator: "whole"}], how_known: "None in the source read."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "'Cool jazz and modal jazz'"}], how_known: "Not assessed."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "'Cool jazz and modal jazz'"}], how_known: "Not assessed."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "'Cool jazz and modal jazz'"}], how_known: "Coder's reading."}
  reading: "'Don't play what's there, play what's not there' (image caption, S1)."
  notes: ""

institutions:
  - {value: "Columbia Records", role: "recording artist", kind: commercial, certainty: 0.5, cites: [{source: S1, locator: "'Free jazz and fusion' (memo of 14 November 1969)"}], how_known: "Britannica quotes a Columbia internal memo about the Bitches Brew title; years not stated."}
collaborators:
  - {value: "Charlie Parker", relation: collaborator, note: "recorded together often, 1945–48", certainty: 0.7, cites: [{source: S1, locator: "'Starting out' ¶2"}], how_known: "Britannica."}
  - {value: "Dizzy Gillespie", relation: "mentor or employer", note: "'His mentor Gillespie' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Starting out' ¶2"}], how_known: "Britannica."}
  - {value: "Gil Evans", relation: collaborator, note: "arranger: nonet; Miles Ahead, Porgy and Bess, Sketches of Spain", certainty: 0.7, cites: [{source: S1, locator: "'Cool jazz and modal jazz' ¶1, ¶3"}], how_known: "Britannica."}
  - {value: "John Coltrane", relation: collaborator, note: "saxophonist in his 1950s groups", certainty: 0.7, cites: [{source: S1, locator: "'Cool jazz and modal jazz' ¶2"}], how_known: "Britannica."}
  - {value: "Quincy Troupe", relation: collaborator, note: "co-author of Miles (1989)", certainty: 0.7, cites: [{source: S1, locator: "'Personal Life', last paragraph"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 119"}], how_known: "Study roster."}
  controversies:
    - {value: "Heroin addiction in the early 1950s ('a four-year horror show')", certainty: 0.7, cites: [{source: S1, locator: "'Cool jazz and modal jazz' ¶2"}], how_known: "Britannica."}
  data_quality_flags:
    - "Single tertiary source; no worldview evidence read."
  open_questions:
    - "Miles: The Autobiography (1989), pp. 148–149 and 411, on religion and spirits."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "Britannica Editors. \"Miles Davis.\" Encyclopaedia Britannica (updated 18 October 2026). https://www.britannica.com/biography/Miles-Davis. Read live 2026-10-19."
    url: "https://www.britannica.com/biography/Miles-Davis"
    accessed: 2026-10-19
    reliability_note: "Editors' article; 'at a Glance' box and body sections cited; question boxes not cited (P26)."
    used_for: [identity, basics, contribution, childhood, heritage, timing, institutions, collaborators, review]
  - id: S3
    type: secondary
    kind: other
    author: "Paul Tingen"
    citation: "Tingen, Paul. Miles Beyond: The Electric Explorations of Miles Davis, 1967–1991 (New York: Billboard Books, 2001), ch. 1. Author's web copy: https://tingen.org/miles-beyond-chapter-1/"
    url: "https://tingen.org/miles-beyond-chapter-1/"
    accessed: 2026-10-19
    reliability_note: "Music journalist's book chapter on the author's site (© 2001); quotes the autobiography without page numbers (secondary quotation). Used only for the worldview lead; nothing scored on it."
    used_for: [worldview]
  - id: S2
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Miles Davis

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Miles Davis (1926–1991), American jazz trumpeter, bandleader and composer [S1]. Draft: primary_system and every axis UNKNOWN; mid_basin UNKNOWN. Not plotted.

## Life and work

East St. Louis; New York from 1944; Parker, Gillespie; his own groups from 1948 [S1].

## Contribution and impact

Birth of the Cool (1949–50), Kind of Blue (1959), In a Silent Way (1969), Bitches Brew (1970) [S1].

## Childhood and education

Son of a dental surgeon and a musician mother; Juilliard 1944–45 [S1].

## Adult working worldview

Nothing read; lead in Miles (1989) [S1].

## Heritage (context only)

Not recorded.

## Timing

1949–1970, from age 23 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Not assessed.

## Open questions

- Miles (1989), pp. 148–149, 411 (p. 411 quoted by Rosen and Tingen [S3]; book unread).

## Research log

- 2026-10-19: Read Britannica; The Spiritual Muses article (Rosen) failed to open (HTTP 500 and curl).
- 2026-10-19 (batch V audit fixes): read Tingen, Miles Beyond ch. 1 (tingen.org) for the p. 411 wording [S3].
