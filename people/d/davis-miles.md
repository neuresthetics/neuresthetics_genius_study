---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 4
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch V)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to music. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #118 / F4 rank 119). Goals: open Miles (1989) p.411 or in-span interviews on God/spirits; keep UNKNOWN if still secondary-only (ruling V3). Tried Internet Archive borrow copies (milesautobiograp0000davi et al.): access-restricted, download 401; Rosen The Spiritual Muses still HTTP 500. Read in-span: Alex Haley Playboy interview Sept 1962 (S5) — race, music, public persona; no God/religion/spirits. Don DeMicheal Rolling Stone interview 13 Dec 1969 (S6) — music direction, race, rock; no God/religion/spirits. Wikipedia EN (S4, P50): birth/death align Britannica; brief Catholic elementary; gospel as early taste; funeral St. Peter's Lutheran 1991 (after span, practice). Secondary leads unchanged (Tingen S3; Rosen search-snippet p.411; Hollowverse cites autobiography Islam/per se — still unread book). P47 on S1–S6. primary/A–E/mid stay UNKNOWN under V3. Chart-moving NO. No fallacy_catalog. No figures/. Draft, not reviewed."}
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
    date: {value: "1926-05-26", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "'Miles Davis at a Glance' (Born)"}, {source: S4, locator: "Infobox / Early life"}], how_known: "Britannica and Wikipedia EN agree (P50)."}
    place: {value: "Alton, Illinois", modern_name: "Alton, Illinois, USA", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "'Miles Davis at a Glance' (Born)"}], how_known: "Britannica."}
  death:
    date: {value: "1991-09-28", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "'Miles Davis at a Glance' (Died)"}, {source: S4, locator: "Infobox / Death"}], how_known: "Britannica and Wikipedia EN agree (P50); pneumonia, respiratory failure and stroke."}
    place: {value: "Santa Monica, California", modern_name: "Santa Monica, USA", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "'Miles Davis at a Glance' (Died)"}], how_known: "Britannica; pneumonia, respiratory failure and stroke (S1, 'Personal Life')."}
  first_lasting_contribution_year: {value: 1949, certainty: 0.7, cites: [{source: S1, locator: "'Cool jazz and modal jazz' ¶1"}], how_known: "The nonet recordings 'originally released as singles (1949–50)', later Birth of the Cool (1957); dated by first release, range start (P12, P30)."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S1, locator: "'Cool jazz and modal jazz' ¶1"}], how_known: "1949 (P2); one year before the edge."}
  region_of_birth: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "'Miles Davis at a Glance'"}], how_known: "USA (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "'Starting out'"}], how_known: "New York from 1944."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "'Personal Life'"}], how_known: "Britannica."}
  languages_of_work: {value: ["English"], certainty: 0.5, cites: [{source: S1, locator: "'Starting out'"}], how_known: "Coder's reading."}
  occupations: {value: ["jazz trumpeter", "bandleader", "composer"], certainty: 0.7, cites: [{source: S1, locator: "opening; 'Miles Davis at a Glance'"}], how_known: "Britannica."}

contribution:
  primary_domain: music
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
    - {value: "Brief Catholic elementary school before John Robinson Elementary (all-black), East St. Louis", stage: "elementary school", run_by: "religious body", certainty: 0.5, cites: [{source: S4, locator: "Early life"}], how_known: "Wikipedia EN; duration not stated. Context only — not a worldview code."}
    - {value: "Violin lessons from age 10 (encouraged by his mother); trumpet from his early teens", stage: tutor, run_by: family, certainty: 0.5, cites: [{source: S1, locator: "'Starting out' ¶1"}], how_known: "Britannica; teacher not named, operator the coder's reading."}
    - {value: "Institute of Musical Art (now the Juilliard School), New York; dropped out", stage: university, run_by: private, years: "1944–1945", certainty: 0.7, cites: [{source: S1, locator: "'Starting out' ¶2"}, {source: S4, locator: "1944–1948: New York City"}], how_known: "Britannica; Wikipedia EN concurs."}
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
  primary_system: {value: UNKNOWN, how_known: "Deepen D1: still no own-voice text of Miles (1989) p. 411 (Internet Archive copies access-restricted, download 401; Rosen Spiritual Muses still HTTP 500). In-span interviews read — Playboy Sept 1962 (S5) and Rolling Stone 13 Dec 1969 (S6) — contain no statement on God, religion, or spirits (race, music, public persona). Secondary lead unchanged: p. 411 'I do believe in being spiritual and do believe in spirits…' (Rosen search-snippet with page; Tingen S3 without page); also Hollowverse citing the autobiography on not practicing a religion 'per se' / Islam affinity — book unread. After the span (1989, P1 cap 0.5); interview-built with Troupe (P42, P43). Ruling V3 stands: secondary quotations alone do not move the value → UNKNOWN until the book page is read."}
  secondary_system: {value: UNKNOWN, how_known: "One system (P29)."}
  candidate_codes_considered:
    - {code: ANIM, reason: "Named lead only: 'spirits' / deceased musicians visiting (Miles p. 411) still secondary-only (Rosen snippet; Tingen S3); V3 — not assessed until book read. After span (P1)."}
    - {code: AGNOS, reason: "Named lead only: Hollowverse quotes autobiography 'I don't really practice a religion, per se' — secondary, book unread; V3."}
    - {code: ATHE, reason: "Rejected: in-span interviews (S5, S6) are silent on God; silence ≠ atheism (P20)."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "In-span Playboy 1962 (S5) and Rolling Stone 1969 (S6) have no God/locus claim. Autobiography p. 411 spirits / non-practice of religion remain secondary-only under V3 (P19). After span if ever scored (P1)."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30). No P16 nature-order profession in sources read; musician (P19)."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing on reward/punishment or afterlife deserts in own text read (P19). Spirits lead is secondary-only (V3)."}
    D_authority: {value: UNKNOWN, how_known: "Nothing on revelation against observation in own voice read (P19)."}
    E_scope: {value: UNKNOWN, how_known: "Nothing on favour for a group in the world's order read (P7, P19)."}
  mid_basin: {value: UNKNOWN, how_known: "A and B are UNKNOWN, which takes precedence (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "Deepen D1 2026-10-24: Miles (1989) p.411 still unread (IA 401; Rosen 500). In-span Haley Playboy 1962 and DeMicheal Rolling Stone 1969 read — silent on God/spirits. V3 → primary/A–E/mid UNKNOWN. Not a scientist (P30). Chart-moving NO. Not plotted."

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
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No LIO-type own-voice text read. Autobiography leads are after the span (1989) and secondary-only under V3."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S5, locator: "whole"}, {source: S6, locator: "whole"}], how_known: "In-span interviews silent on God/spirits; autobiography unread (V3)."}
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
    - "Ruling V3: Miles (1989) p.411 still unread in primary; secondary quotations (Rosen, Tingen) do not move values."
    - "Internet Archive borrow copies access-restricted (download 401) this pass; Rosen Spiritual Muses still HTTP 500."
    - "In-span interviews (Playboy 1962; Rolling Stone 1969) silent on God/spirits — absence ≠ ATHE/NONE (P20)."
  open_questions:
    - "Read Miles: The Autobiography (1989) p.411 (and pp.148–149 if present) in a primary copy; then reassess ANIM/AGNOS under P1/P42/P43."
    - "Any other in-span interview (DownBeat, radio) with explicit God/spirits talk (low prior after S5/S6)."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "Britannica Editors. \"Miles Davis.\" Encyclopaedia Britannica (updated 18 October 2026). https://www.britannica.com/biography/Miles-Davis. Read live 2026-10-19."
    url: "https://www.britannica.com/biography/Miles-Davis"
    accessed: 2026-10-19
    reliability_note: "Editors' article; 'at a Glance' box and body sections cited; question boxes not cited (P26)."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, heritage, timing, institutions, collaborators, review]
  - id: S3
    type: secondary
    kind: other
    author: "Paul Tingen"
    citation: "Tingen, Paul. Miles Beyond: The Electric Explorations of Miles Davis, 1967–1991 (New York: Billboard Books, 2001), ch. 1. Author's web copy: https://tingen.org/miles-beyond-chapter-1/"
    url: "https://tingen.org/miles-beyond-chapter-1/"
    accessed: 2026-10-19
    reliability_note: "Music journalist's book chapter on the author's site (© 2001); quotes the autobiography without page numbers (secondary quotation). Used only for the worldview lead; nothing scored on it (ruling V3)."
    source_quality: "other"
    used_for: [worldview]
  - id: S2
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S4
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia. \"Miles Davis.\" English Wikipedia. https://en.wikipedia.org/wiki/Miles_Davis. Read live 2026-10-24."
    url: "https://en.wikipedia.org/wiki/Miles_Davis"
    accessed: 2026-10-24
    reliability_note: "Crowdsourced; dual bio (P50) against Britannica. Used for birth/death alignment, brief Catholic elementary, funeral location (after span)."
    source_quality: "reference entry"
    used_for: [identity, basics, childhood, heritage, review]
  - id: S5
    type: primary
    kind: "published work by the subject"
    author: "Miles Davis; interviewed by Alex Haley"
    citation: "Haley, Alex. \"Miles Davis: a candid conversation with the jazz world's premier iconoclast.\" Playboy (September 1962). Full text read via plosin.com / erenkrantz mirrors, 2026-10-24."
    url: "https://www.plosin.com/beatbegins/archive/miles.htm"
    accessed: 2026-10-24
    reliability_note: "Contemporaneous in-span interview (1962 within 1949–1970). Own spoken words as printed; mirrors of the published Playboy text. No God/religion/spirits content. Kind = published work by the subject; source_quality newspaper interview (P47)."
    source_quality: "newspaper interview"
    used_for: [worldview, review]
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "Miles Davis; interviewed by Don DeMicheal"
    citation: "DeMicheal, Don. \"Miles Davis: The Rolling Stone Interview.\" Rolling Stone (13 December 1969). Full text read via beatpatrol.wordpress.com republication, 2026-10-24."
    url: "https://beatpatrol.wordpress.com/2008/09/23/don-demicheal-miles-davis-the-rolling-stone-interview-1969/"
    accessed: 2026-10-24
    reliability_note: "Contemporaneous in-span interview (1969 within span). Own spoken words as printed; fan-site republication of the RS text. Music, race, rock; no God/religion/spirits content. Kind = published work by the subject; source_quality newspaper interview (P47)."
    source_quality: "newspaper interview"
    used_for: [worldview, review]

---

# Miles Davis

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Miles Davis (1926–1991), American jazz trumpeter, bandleader and composer [S1; S4]. Deepen D1: primary_system and every axis UNKNOWN (ruling V3; Miles 1989 unread); mid_basin UNKNOWN. Chart-moving NO. Not plotted.

## Life and work

East St. Louis; New York from 1944; Parker, Gillespie; his own groups from 1948 [S1].

## Contribution and impact

Birth of the Cool (1949–50), Kind of Blue (1959), In a Silent Way (1969), Bitches Brew (1970) [S1].

## Childhood and education

Son of a dental surgeon and a musician mother; Juilliard 1944–45 [S1].

## Adult working worldview

In-span Playboy 1962 [S5] and Rolling Stone 1969 [S6] silent on God/spirits. Miles (1989) p.411 still unread (V3); secondary lead only [S3].

## Heritage (context only)

Not recorded.

## Timing

1949–1970, from age 23 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Not assessed.

## Open questions

- Miles (1989) p.411 in a primary copy (V3 blocker); other in-span interviews if any.

## Research log

- 2026-10-19: Read Britannica; The Spiritual Muses article (Rosen) failed to open (HTTP 500 and curl).
- 2026-10-19 (batch V audit fixes): read Tingen, Miles Beyond ch. 1 (tingen.org) for the p. 411 wording [S3].
- 2026-10-24: Deepen D1. IA Miles autobiography download 401; Rosen still 500. Read Playboy 1962 [S5], Rolling Stone 1969 [S6], Wikipedia EN [S4]. Values stay UNKNOWN under V3. Chart-moving NO.
