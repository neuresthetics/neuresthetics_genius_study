---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z8)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to architecture. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #160, F3 rank 168). Hunt: An Autobiography read in Faber & Faber London 1945 OCR (S5; archive scan OCR only; Book Two Fellowship: Wasn't nature in this sense the very nature of God?); US 1932 Longmans not separately collated — sentence sits in the four-book Fellowship narrative shared with the 1932 structure; no changes_over_life documented (P31). Wallace 1957 (S2) kept as corroboration. Taliesin Fellowship talk 1956 body of God (secondary via Hierotopy thesis) named as PANENT lead only, not scored. Grasping the laws of nature / Her equilibrium ... is probably God / book of creation in S5 are organic-architecture / Code talk, not P16 cause-order — B stays UNKNOWN. primary_system PANT 0.5→0.7 (written_profession; alt PANENT); A 4 0.5→0.7 support corroborated (S5+S2; alt 3 only, BELOW dropped); mid_basin BELOW_THRESHOLD→false @0.7 (A≥3 branch, P10). Still not plotted (no B). P47 source_quality on S1–S6; Wikipedia EN S6 (P50 dual-bio). No fallacy_catalog; figures/ untouched. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z10 audit fix (WEAKEN; v8's call on the auditor's advice): Fallingwater how_known no longer says 'P12 start 1935'; dated by completion, 1937. Span unchanged."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z8 audit fixes (v8's calls on the auditor's advice). RQ-Z8-2: a third party's web copy of a transcript is a secondary quotation (V3) unless checked; the lines were checked word for word against the Harry Ransom Center's own transcript in CONTENTdm (HRC_WAL0115), now S2, so PANT 0.5 and A 4 at 0.5 hold (P8, P20 cap). Quote cuts now [...]. Fallingwater item year 1935 -> 1937 (completion), S3 author Alicja Zelazko. Unity Temple 1906 is a start date: item year UNKNOWN. Span 1902–1937 unchanged."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z8, order P32: F 3, rank 168). Basics from Britannica (Edgar Kaufmann, signed) and Britannica 'Fallingwater'. Own words: The Mike Wallace Interview (1957, two parts; Harry Ransom Center video, read in a published transcription), after the span: 'I've always considered myself deeply religious'; 'my church I put a capital N on Nature and go there ... You spell God with a G ... I spell Nature with an N, capital'; 'I put a capital N on Nature, and call it my Church'. Not a scientist. primary_system PANT (0.5, alt BELOW_THRESHOLD); A 4 (0.5, alts 3 and BELOW_THRESHOLD); B UNKNOWN (no statement on nature's order); C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD (P10; A ≥ 3 only at 0.5). Span 1902–1937, age 35. Not plotted (no B). Draft, not reviewed."}

identity:
  id: wright-frank-lloyd
  display_name: "Frank Lloyd Wright"
  roster:
    canonical_name: "Frank Lloyd Wright"
    rank: 168
    F: 3
    models: [Claude, DeepSeek, Gemini]
    band: "core (3–4)"
    status: "core"
    field: "architecture"
    field_bucket: "arts"
  full_name: {value: "Frank Lloyd Wright", certainty: 0.7, cites: [{source: S1, locator: "At a Glance; Early life"}], how_known: "Britannica; born Frank Wright, later adopted Lloyd."}
  native_name: {value: "Frank Lloyd Wright", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  aliases:
    - {name: "Frank Wright", kind: "birth name"}
    - {name: "Wright-Frank Lloyd", kind: "roster alias"}

basics:
  birth:
    date: {value: "1867-06-08", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Richland Center, Wisconsin", modern_name: "Richland Center, Wisconsin, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "1959-04-09", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Phoenix, Arizona", modern_name: "Phoenix, Arizona, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1902, certainty: 0.5, cites: [{source: S1, locator: "The early Chicago years"}], how_known: "W.W. Willits House (1902), 'the first masterwork of the Prairie school'; Prairie style 'mature' by 1900, so the start could be earlier."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "The early Chicago years"}], how_known: "1902 (P2)."}
  region_of_birth: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "USA (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Chicago, Wisconsin, Arizona."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Inferred."}
  occupations: {value: ["architect", "writer"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

contribution:
  primary_domain: architecture
  fields: {value: ["architecture"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Prairie style (W.W. Willits House, first masterwork)", year: 1902, kind: "method", lasting: "'His “Prairie style” became the basis of 20th-century residential design in the United States' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; The early Chicago years"}], how_known: "Britannica."}
    - {value: "Unity Temple, Oak Park", year: UNKNOWN, kind: "work", lasting: "'achieved timeless monumentality' (S1)", certainty: 0.5, cites: [{source: S1, locator: "The early Chicago years"}], how_known: "Britannica: 'under way' 1906, a start date, not a P30 #1 dating event (RQ-Z7-N1); no completion or dedication year read, so UNKNOWN. Span unaffected (starts 1902, ends 1937)."}
    - {value: "Fallingwater", year: 1937, kind: "work", lasting: "'became one of the most famous 20th-century buildings' (S3)", certainty: 0.7, cites: [{source: S3, locator: "opening"}], how_known: "Britannica 'Fallingwater': designed 1935, completed 1937; dated by completion, 1937 (RQ-Z7-N1; private building with no unveiling), which is also the span end."}
  evidence_of_impact:
    - {value: "An abundantly creative master of American architecture", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works:
    - {value: "Larkin Administration Building", year: 1904, kind: "artwork", certainty: 0.7, cites: [{source: S1, locator: "The early Chicago years"}], how_known: "Britannica."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Master of American architecture (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "Unitarian (Lloyd-Jones maternal clan)", certainty: 0.7, cites: [{source: S5, locator: "Book One, Family — Richard Jones / Unity"}, {source: S6, locator: "Early life"}], how_known: "Autobiography: maternal Lloyd-Jones Unitarian Unity of all things; Wikipedia and Britannica note Unitarian / Lloyd-Jones heritage. Heritage only — not a worldview code."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "William C. Wright, itinerant musician and preacher", role: "father", certainty: 0.7, cites: [{source: S1, locator: "Early life"}], how_known: "Britannica."}
    - {value: "Anna Lloyd-Jones, schoolteacher", role: "mother", certainty: 0.7, cites: [{source: S1, locator: "Early life"}], how_known: "Britannica."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling:
    - {value: "University of Wisconsin (special student, engineering)", stage: "university", years: "1885–1886", certainty: 0.7, cites: [{source: S1, locator: "Early life"}], how_known: "Britannica."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1902–1937", certainty: 0.5, cites: [{source: S1, locator: "The early Chicago years"}, {source: S3, locator: "opening"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system:
    value: PANT
    basis: written_profession
    certainty: 0.7
    cites: [{source: S5, locator: "Book Two, Fellowship — nature of wood, glass and iron / 'very nature of God'"}, {source: S2, locator: "Part 1, opening questions; Part 2"}]
    how_known: "Own published Autobiography (S5, Faber 1945 OCR of the four-book text; Nature-of-God sentence in Book Two Fellowship / early-career narrative; US 1932 Longmans not separately collated). Wallace 1957 (S2) corroborates the God=Nature identification. No change of view in changes_over_life (P31). Contested-readings cap 0.7 for named PANENT alternative (§3)."
    rationale: "S6 two-part: (1) identifies God with Nature as what exists — Wallace 'I spell Nature with an N, capital' for God; Autobio 'Wasn't nature in this sense the very nature of God?'; (2) mark beyond feeling — Autobio interior order in Nature 'like a religion'; Wallace 'deeply religious' with capital-N Nature as church. Named alternative PANENT: Taliesin Fellowship talk 1956 (secondary) that Nature is 'all the body of God' by which we become aware of Him keeps a God Nature manifests rather than equals; Autobio 'nature of God' can be read as essence-of. BELOW_THRESHOLD (mere church rhetoric) dropped after Autobio."
    alternatives:
      - {value: PANENT, note: "Nature as body/means of God (1956 Taliesin, secondary); Autobio essence-of reading.", cites: [{source: S5, locator: "Book Two, Fellowship"}]}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: PANT, reason: "Coded: God spelled as / identified with Nature (S2, S5); passes S6 on the identity reading."}
    - {code: PANENT, reason: "Named alternative: Nature as body/means of God (1956 Taliesin, secondary); Autobio 'nature of God' as essence-of rather than Deus sive Natura."}
    - {code: CHRIST, reason: "Rejected as primary: Unitarian heritage and Unity Temple practice; quotes Jesus ('The Kingdom of God is within you') but attends no church as doctrine and rejects organised Christianity (S2). Heritage ≠ code."}
  lio_axes:
    A_locus:
      value: 4
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S5, locator: "Book Two, Fellowship — 'very nature of God'"}, {source: S2, locator: "Part 1, opening questions"}]
      how_known: "Autobiography (S5) plus Wallace interview (S2). Contested-readings cap 0.7 for named A 3 alternative. Independent sources → corroborated (P48)."
      rationale: "Divine is Nature itself (Wallace spells God as Nature; Autobio Nature as the very nature of God): locus 4. Alternative 3: 'The Kingdom of God is within you' (S2) and PANENT-leaning body-of-God talk keep a God not exhausted by Nature. Create's BELOW (rhetoric) dropped after Autobio."
      alternatives:
        - {value: 3, note: "'The Kingdom of God is within you' and body-of-God language keep a God beyond or including Nature.", cites: [{source: S2, locator: "Part 2"}]}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30). Autobio 'grasping the laws of nature' / Nature's equilibrium 'probably God' / 'reading mostly in the book of creation' (S5) are organic-architecture and building-Code talk, not claims about how events happen (P16, P19). Wallace Nature-as-church is design/worship, not cause-order. Do not invent B."}
    C_ledger: {value: UNKNOWN, how_known: "'Do you believe [...] in your personal immortality? Yes [...] when they put you into the box that's your immortality' (S2) is ambiguous between survival and legacy; not scored."}
    D_authority: {value: UNKNOWN, how_known: "Not scored."}
    E_scope: {value: UNKNOWN, how_known: "Not scored."}
  mid_basin: {value: false, certainty: 0.7, cites: [{source: S5, locator: "Book Two, Fellowship — 'very nature of God'"}, {source: S2, locator: "Part 1"}], how_known: "A 4 at 0.7 with named alternative 3 (both A ≥ 3); A ≥ 3 branch reads A only (P10). Still not plotted: B UNKNOWN."}
  statements:
    - text: "What did they mean when 'they' used the word nature? Just some sentimental feeling about animals, grass and trees. The out-of-doors? But how about the nature of wood, glass and iron — internal nature? The nature of boys and girls. The nature of law? Wasn't that Nature? Wasn't nature in this sense the very nature of God?"
      cites: [{source: S5, locator: "Book Two, Fellowship (near Silsbee / Oak Park narrative; Larkin plates in this edition)"}]
      date: "1932"
      context: "An Autobiography; sentence in Book Two Fellowship. Copy read: Faber & Faber London 1945 OCR (S5). US 1932 Longmans not separately collated."
      axes: [A_locus]
      kind: "autobiography"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "OCR of Faber 1945; page images not viewed. Hierotopy thesis (Pfeiffer / Pomegranate tradition) also quotes this sentence from An Autobiography."
    - text: "WALLACE: Are you a religious man yourself? WRIGHT: I've always considered myself deeply... [...] ...religious. WALLACE: Do you go to any specific church? WRIGHT: Yes, I go occasionally to this one, and then sometimes to that one, but my church I put a capital N on Nature and go there. [...] You spell God with a G, don't you? WALLACE: I spell God with a G, you will spell it with...? WRIGHT: I spell Nature with an N, capital."
      cites: [{source: S2, locator: "Part 1, opening questions"}]
      date: "1957-09"
      context: "The Mike Wallace Interview; after the span; corroborates Autobio Nature–God identification (P31, no change documented)."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "Checked word for word against HRC CONTENTdm transcript (RQ-Z8-2). Video not viewed."
  changes_over_life: []
  coder_notes: "Deepen D1: Autobio (S5) lifts PANT/A to 0.7; B left UNKNOWN (P16). A Testament (1957) and Ransom Center video still unread. 1932 Longmans page for the Nature-of-God sentence not collated. Taliesin 1956 body-of-God kept as PANENT lead only (secondary). Coder's call: date Autobio statement 1932 (US first edition year) while citing the 1945 Faber OCR as the copy read."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: "Unitarian (maternal Lloyd-Jones; father later Unitarian via wife's family)", certainty: 0.7, cites: [{source: S5, locator: "Book One, Family"}, {source: S6, locator: "Early life"}, {source: S1, locator: "Early life"}], how_known: "Autobiography and Wikipedia: Lloyd-Jones Unitarians; father William joined Unitarian faith through wife's family (S6). Heritage only."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1902–1937", certainty: 0.5, cites: [{source: S1, locator: "The early Chicago years"}, {source: S3, locator: "opening"}], how_known: "Willits House (1902) to Fallingwater (designed 1935, completed 1937; P29, P30 rule 4). Later works (Guggenheim) not called lasting in a body read."}
  age_at_first_lasting_contribution: {value: 35, certainty: 0.5, cites: [{source: S1, locator: "opening; The early Chicago years"}], how_known: "1902 − 1867 = 35 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: "1932 (An Autobiography, Book Two Nature-of-God sentence; copy read Faber 1945)", certainty: 0.5, cites: [{source: S5, locator: "Book Two, Fellowship"}], how_known: "Earliest own published Nature–God identification read; 1932 Longmans not collated."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.5, cites: [{source: S5, locator: "Book Two"}, {source: S2, locator: "Part 1"}], how_known: "Autobiography 1932 within 1902–1937; Wallace 1957 after with same identification, no change documented (P31)."}
  worldview_during_major_work: {value: "PANT / A 4 — Nature identified with God (Autobiography); design-church Nature talk, not cause-order", certainty: 0.7, cites: [{source: S5, locator: "Book Two"}, {source: S2, locator: "Part 1"}], how_known: "Coded axes."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "Geometric plan and structure, no proof (S1).", certainty: 0.5, cites: [{source: S1, locator: "The early Chicago years"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "Taliesin Fellowship", role: "founder", years: "1932–1959", kind: "other", certainty: 0.7, cites: [{source: S3, locator: "text"}], how_known: "Britannica 'Fallingwater'; end year his death."}
collaborators:
  - {value: "Louis Sullivan", relation: "mentor or employer", note: "chief assistant to 1893", certainty: 0.7, cites: [{source: S1, locator: "The early Chicago years"}], how_known: "Britannica."}
  - {value: "Edgar J. Kaufmann", relation: "other", note: "Fallingwater", certainty: 0.7, cites: [{source: S3, locator: "text"}], how_known: "Britannica 'Fallingwater'."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 168"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Autobiography read only as Faber 1945 OCR (archive scan OCR only); 1932 Longmans page not collated."
    - "Wallace 1957 checked against HRC CONTENTdm transcript; video not viewed."
    - "Taliesin 1956 body-of-God known only via secondary quotation (Hierotopy thesis / Pfeiffer)."
  open_questions:
    - "Collate 1932 Longmans An Autobiography for the Nature-of-God sentence."
    - "A Testament (1957); Ransom Center video."
    - "Primary text of Taliesin Fellowship talk 30 Dec 1956 (Collected Writings) for PANENT vs PANT."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Edgar Kaufmann"
    citation: "Kaufmann, Edgar. 'Frank Lloyd Wright.' Encyclopaedia Britannica. https://www.britannica.com/biography/Frank-Lloyd-Wright"
    url: "https://www.britannica.com/biography/Frank-Lloyd-Wright"
    accessed: 2026-10-19
    source_quality: "reference entry"
    reliability_note: "Signed article; body cited, Top Questions not used (P26)."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, collaborators]
  - id: S2
    type: primary
    kind: "other"
    author: "Frank Lloyd Wright, interviewed by Mike Wallace"
    citation: "Interview with Frank Lloyd Wright. The Mike Wallace Interview (1 and 28 September 1957), Harry Ransom Center, University of Texas at Austin, HRC_WAL0115, transcript in the CONTENTdm digital collection. https://hrc.contentdm.oclc.org/digital/collection/p15878coll90/id/81 (earlier read in Usamah Husseini's web copy, https://husseini.posthaven.com/radical-frank-lloyd-wright-interviewed-by-mike-wallace)"
    url: "https://hrc.contentdm.oclc.org/digital/collection/p15878coll90/id/81"
    accessed: 2026-10-19
    source_quality: "primary / own words"
    reliability_note: "Recorded TV interview (recorded_interview, P8). The quoted lines were checked word for word against the institution's own transcript (HRC CONTENTdm item 81, fetched 2026-10-19), not only the third-party web copy (RQ-Z8-2). Video not viewed."
    used_for: [worldview]
  - id: S3
    type: tertiary
    kind: "encyclopedia"
    author: "Alicja Zelazko"
    citation: "Zelazko, Alicja. 'Fallingwater.' Encyclopaedia Britannica (Scholars edition). https://kids.britannica.com/scholars/article/Fallingwater/629390"
    url: "https://kids.britannica.com/scholars/article/Fallingwater/629390"
    accessed: 2026-10-19
    source_quality: "reference entry"
    reliability_note: "Topic article body (seen as a search excerpt); not a question box."
    used_for: [contribution, worldview, timing, institutions, collaborators]
  - id: S4
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    source_quality: "study roster"
    reliability_note: "Study's own roster."
    used_for: [review]
  - id: S5
    type: primary
    kind: "published work by the subject"
    author: "Frank Lloyd Wright"
    citation: "Wright, Frank Lloyd. An Autobiography. London: Faber & Faber, 1945 (first published MCMXLV; OCR of archive.org item in.ernet.dli.2015.61386 / DLI scan). US first edition Longmans 1932; expanded US Duell, Sloan and Pearce 1943. Nature-of-God sentence read in Book Two: Fellowship."
    url: "https://archive.org/details/in.ernet.dli.2015.61386"
    accessed: 2026-10-24
    source_quality: "archive scan (OCR only)"
    reliability_note: "Own published autobiography; copy read is Faber 1945 OCR only (page images not viewed). 1932 Longmans not collated. 'Probably God' / laws-of-nature / book-of-creation lines in the same OCR are design/Code context, not scored for B."
    used_for: [childhood, worldview, heritage, timing]
  - id: S6
    type: tertiary
    kind: "encyclopedia"
    author: "Wikipedia contributors"
    citation: "Wikipedia. 'Frank Lloyd Wright.' English Wikipedia, revision 1379912762 (2026-10-12 UTC). https://en.wikipedia.org/wiki/Frank_Lloyd_Wright"
    url: "https://en.wikipedia.org/wiki/Frank_Lloyd_Wright"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "P50 dual-bio with Britannica (S1). Used for Unitarian / Lloyd-Jones heritage and birthplace corroboration; not for worldview scores."
    used_for: [childhood, heritage, review]
---

## Summary

Frank Lloyd Wright (1867–1959), architect [S1]. Deepen D1: PANT (0.7, alt PANENT); A 4 (0.7, corroborated); B UNKNOWN; mid_basin false (0.7). Not plotted (no B).

## Life and work

Wisconsin, Chicago, Taliesin, Arizona [S1].

## Contribution and impact

Prairie style; Unity Temple; Fallingwater [S1, S3].

## Childhood and education

Preacher father, schoolteacher mother; engineering at Madison [S1].

## Adult working worldview

Autobiography: Nature as 'the very nature of God' [S5]; Wallace: capital-N Nature as church / God spelled Nature [S2]. Design-church Nature talk, not cause-order (B UNKNOWN).

## Heritage (context only)

Unitarian Lloyd-Jones maternal clan; father joined via wife's family [S5, S6, S1]. Heritage only.

## Timing

1902–1937, age 35 [S1, S3].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Collate 1932 Longmans Autobio; A Testament; Ransom Center video; primary Taliesin 1956 body-of-God text.

## Research log

- 2026-10-19: Read Britannica (Kaufmann), Britannica 'Fallingwater', Wallace interview transcription; 2026-10-19 (Z8 fixes): checked against the HRC CONTENTdm transcript.
- 2026-10-24 (D1): Faber 1945 Autobio OCR (S5); Wikipedia EN rev 1379912762 (S6, P50); Hierotopy thesis secondary for Taliesin 1956 (not scored).
