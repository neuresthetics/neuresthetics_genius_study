---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z8)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
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
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
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
    basis: recorded_interview
    certainty: 0.5
    cites: [{source: S2, locator: "Part 1, opening questions; Part 2"}]
    how_known: "(interview) 1957, after the span (P20), so 0.5. Wording checked against the Harry Ransom Center's own transcript in its CONTENTdm digital collection (S2; RQ-Z8-2), so it is a primary recorded interview (P8, up to 0.7), capped at 0.5 after the span (P20)."
    rationale: "God named as Nature: 'You spell God with a G, don't you? [...] I spell Nature with an N, capital'; 'I put a capital N on Nature, and call it my Church'; 'I've always considered myself deeply religious'. Alternative BELOW_THRESHOLD: a rhetorical line about churches and architecture rather than a doctrine."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: PANT, reason: "Coded: God spelled as Nature."}
    - {code: CHRIST, reason: "Rejected: quotes Jesus ('The Kingdom of God is within you') but attends no church and rejects organised Christianity."}
  lio_axes:
    A_locus: 
      value: 4
      basis: recorded_interview
      certainty: 0.5
      cites: [{source: S2, locator: "Part 1, opening questions"}]
      how_known: "(interview) 1957, after the span; P20 cap 0.5."
      rationale: "The divine is Nature itself ('I spell Nature with an N, capital' for God): the order of nature itself, 4. Alternatives 3 (mostly nature, with 'the Kingdom of God is within you') and BELOW_THRESHOLD (rhetoric)."
      alternatives:
        - {value: 3, note: "'The Kingdom of God is within you' keeps a God beyond nature.", cites: [{source: S2, locator: "Part 2"}]}
        - {value: BELOW_THRESHOLD, note: "Rhetorical, not a locus view.", cites: [{source: S2, locator: "Part 1"}]}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30). 'Nature' in his words is a church and a design standard, not a claim about how events happen (P16, P19)."}
    C_ledger: {value: UNKNOWN, how_known: "'Do you believe [...] in your personal immortality? Yes [...] when they put you into the box that's your immortality' (S2) is ambiguous between survival and legacy; not scored."}
    D_authority: {value: UNKNOWN, how_known: "Not scored."}
    E_scope: {value: UNKNOWN, how_known: "Not scored."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is at least 3 only at 0.5; P10 caps mid_basin by the certainty of the tested condition, below the 0.7 bar, so BELOW_THRESHOLD (Z7 audit precedent)."}
  statements:
    - text: "WALLACE: Are you a religious man yourself? WRIGHT: I've always considered myself deeply... [...] ...religious. WALLACE: Do you go to any specific church? WRIGHT: Yes, I go occasionally to this one, and then sometimes to that one, but my church I put a capital N on Nature and go there. [...] You spell God with a G, don't you? WALLACE: I spell God with a G, you will spell it with...? WRIGHT: I spell Nature with an N, capital."
      cites: [{source: S2, locator: "Part 1, opening questions"}]
      date: "1957-09"
      context: "The Mike Wallace Interview; after the span."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-19
      note: "Husseini's posting of the Ransom Center transcript, 'making a few corrections'; not checked against the video."
  changes_over_life: []
  coder_notes: "Check the wording against the Ransom Center video; A Testament (1957) and An Autobiography (1932, within reach of the span) for written words on God and Nature."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Father a preacher (S1); denomination not stated in the sources read."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1902–1937", certainty: 0.5, cites: [{source: S1, locator: "The early Chicago years"}, {source: S3, locator: "opening"}], how_known: "Willits House (1902) to Fallingwater (designed 1935, completed 1937; P29, P30 rule 4). Later works (Guggenheim) not called lasting in a body read."}
  age_at_first_lasting_contribution: {value: 35, certainty: 0.5, cites: [{source: S1, locator: "opening; The early Chicago years"}], how_known: "1902 − 1867 = 35 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

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
    - "Own words from a 1957 TV interview after the span, checked against the Ransom Center transcript."
  open_questions:
    - "Ransom Center video check; A Testament; An Autobiography."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Edgar Kaufmann"
    citation: "Kaufmann, Edgar. 'Frank Lloyd Wright.' Encyclopaedia Britannica. https://www.britannica.com/biography/Frank-Lloyd-Wright"
    url: "https://www.britannica.com/biography/Frank-Lloyd-Wright"
    accessed: 2026-10-19
    reliability_note: "Signed article; body cited, Top Questions not used (P26)."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, collaborators]
  - id: S2
    type: primary
    kind: "other"
    author: "Frank Lloyd Wright, interviewed by Mike Wallace"
    citation: "Interview with Frank Lloyd Wright. The Mike Wallace Interview (1 and 28 September 1957), Harry Ransom Center, University of Texas at Austin, HRC_WAL0115, transcript in the CONTENTdm digital collection. https://hrc.contentdm.oclc.org/digital/collection/p15878coll90/id/81 (earlier read in Usamah Husseini's web copy, https://husseini.posthaven.com/radical-frank-lloyd-wright-interviewed-by-mike-wallace)"
    url: "https://hrc.contentdm.oclc.org/digital/collection/p15878coll90/id/81"
    accessed: 2026-10-19
    reliability_note: "Recorded TV interview (recorded_interview, P8). The quoted lines were checked word for word against the institution's own transcript (HRC CONTENTdm item 81, fetched 2026-10-19), not only the third-party web copy (RQ-Z8-2). Video not viewed."
    used_for: [worldview]
  - id: S3
    type: tertiary
    kind: "encyclopedia"
    author: "Alicja Zelazko"
    citation: "Zelazko, Alicja. 'Fallingwater.' Encyclopaedia Britannica (Scholars edition). https://kids.britannica.com/scholars/article/Fallingwater/629390"
    url: "https://kids.britannica.com/scholars/article/Fallingwater/629390"
    accessed: 2026-10-19
    reliability_note: "Topic article body (seen as a search excerpt); not a question box."
    used_for: [contribution, worldview, timing, institutions, collaborators]
  - id: S4
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [review]
---

## Summary

Frank Lloyd Wright (1867–1959), architect [S1]. Draft: PANT (0.5); A 4 (0.5); B UNKNOWN. Not plotted.

## Life and work

Wisconsin, Chicago, Taliesin, Arizona [S1].

## Contribution and impact

Prairie style; Unity Temple; Fallingwater [S1, S3].

## Childhood and education

Preacher father, schoolteacher mother; engineering at Madison [S1].

## Adult working worldview

'I put a capital N on Nature, and call it my Church' [S2].

## Heritage (context only)

Not stated.

## Timing

1902–1937, age 35 [S1, S3].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Ransom Center video; A Testament.

## Research log

- 2026-10-19: Read Britannica (Kaufmann), Britannica 'Fallingwater', Wallace interview transcription; 2026-10-19 (Z8 fixes): checked against the HRC CONTENTdm transcript.
