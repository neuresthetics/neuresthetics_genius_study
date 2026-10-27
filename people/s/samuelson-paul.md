---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA8; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to 20c_early. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA8, order P32: F 3, rank 209). Sources: Britannica (scholars edition, unsigned, read in full) and NobelPrize.org facts page (read in full). Lasting work: the textbook Economics (1948), 'considered a classic' (S1) and 'the world's best selling economic textbook' (S2). Span 1948, age 33. Foundations of Economic Analysis (1947), the multiplier–accelerator model and revealed preference are 'of particular influence' (S1) but undated in the sources read or not called lasting; recorded as major works. Economist, not a scientist (Friedman precedent). Worldview: no own words read; born into a Jewish family that emigrated from Poland (S2). primary_system UNKNOWN; A UNKNOWN; B UNKNOWN; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #196/228, F3 rank 209). Goals: any first-person religion/nature statements; keep silence if none; do not force plot. Dual bio Wikipedia EN (S4, P50). Opened My Life Philosophy / policy credos (S5, USP reprint of Szenberg Eminent Economists 1992 / American Economist 1983): ethics of underdog / 'easy faith' = liberal Weltanschauung; Machian HOW as only WHY = scientific methodology (thermodynamics), not a theistic creed or P16 nature-order profession. Atlantic 2009 interview (S6): 'cafeteria Keynesian' explained via cafeteria-Catholic metaphor — economics doctrine pick-and-choose, not personal Catholicism. Chicago School conversation (Hammond 1997/2010, S7): Knight 'flaming atheist' is about Knight; 'I can't say my old religion, although I was trained by the Jesuits' = Chicago-economics metaphor. Infinite MIT oral history: Saint Peter / heaven joke about making economics mathematical — joke only. Own words on family as 'upwardly mobile Jewish immigrants from Poland' (S4 quoting him; S2). No adult ATHE/AGNOS/JUDA/CHRIST self-description found. primary/A stay UNKNOWN (researched silence; metaphors and heritage rejected as codes, P19). B UNKNOWN (not a scientist, P30/Friedman; economics ≠ natural science for B unless clear P16 line — none). mid UNKNOWN. Not plotted. Chart-moving NO. P47 on S1–S7. No fallacy_catalog. No figures/. Draft, not reviewed."}

identity:
  id: samuelson-paul
  display_name: "Paul Samuelson"
  roster:
    canonical_name: "Paul Samuelson"
    rank: 209
    F: 3
    models: [Claude, Gemini, GPT]
    band: "core (3–4)"
    status: "core"
    field: "economics"
    field_bucket: "social science"
  full_name: {value: "Paul Anthony Samuelson", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "lead / infobox"}], how_known: "Britannica; Wikipedia EN."}
  native_name: {value: "Paul Samuelson", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  aliases:
    - {name: "Paul-Samuelson", kind: "roster alias"}
    - {name: "Samuelson-Paul", kind: "roster alias"}
    - {name: "Paul A. Samuelson", kind: "other"}

basics:
  birth:
    date: {value: "1915-05-15", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Born"}, {source: S4, locator: "infobox"}], how_known: "Britannica; Nobel; Wikipedia."}
    place: {value: "Gary, Indiana", modern_name: "Gary, Indiana, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "Biography"}], how_known: "Britannica; Wikipedia."}
  death:
    date: {value: "2009-12-13", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "Death"}], how_known: "Britannica; Wikipedia."}
    place: {value: "Belmont, Massachusetts", modern_name: "Belmont, Massachusetts, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Died"}], how_known: "Britannica; Nobel."}
  first_lasting_contribution_year: {value: 1948, certainty: 0.7, cites: [{source: S1, locator: "para. 4"}, {source: S2, locator: "Life"}], how_known: "Economics (1948), 'considered a classic' (S1); publication (P30)."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "para. 4"}], how_known: "1948 (P2)."}
  region_of_birth: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "USA (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "para. 2"}, {source: S4, locator: "Biography (MIT from 1940)"}], how_known: "MIT."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "English."}
  occupations: {value: ["economist", "professor", "columnist"], certainty: 0.7, cites: [{source: S1, locator: "para. 2, 4"}], how_known: "Britannica."}

contribution:
  era_bucket: 20c_early
  fields: {value: ["economics"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Economics: An Introductory Analysis (textbook)", year: 1948, kind: "work", lasting: "'considered a classic' (S1); 'has become the world's best selling economic textbook' (S2)", certainty: 0.7, cites: [{source: S1, locator: "para. 4"}, {source: S2, locator: "Life"}], how_known: "Britannica; Nobel."}
  evidence_of_impact:
    - {value: "Nobel Prize in Economic Sciences 1970, 'for his fundamental contributions to nearly all branches of economic theory'", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Prize motivation"}], how_known: "Britannica; Nobel."}
  major_works:
    - {value: "Foundations of Economic Analysis", year: 1947, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "para. 3"}], how_known: "Britannica: 'provides the basic theme of his work'."}
    - {value: "Multiplier–accelerator model; theory of revealed preference", year: UNKNOWN, kind: "paper or paper series", certainty: 0.7, cites: [{source: S1, locator: "para. 3"}], how_known: "Britannica: 'Of particular influence'; undated in S1."}
  honours:
    - {value: "Nobel Prize in Economic Sciences", year: 1970, certainty: 0.7, cites: [{source: S2, locator: "Prize motivation"}], how_known: "Nobel."}
  definition_fit: {value: "clearly meets", rationale: "Nobel laureate; classic textbook (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated as practice; Jewish family heritage only (S2, S4)."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Frank Samuelson (pharmacist) and Ella née Lipton; family he later called 'upwardly mobile Jewish immigrants from Poland'", role: "parents / family", certainty: 0.7, cites: [{source: S4, locator: "Biography"}, {source: S2, locator: "Life"}], how_known: "Wikipedia (his quoted words); Nobel."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated beyond Gary/Chicago moves (S4)."}
  schooling:
    - {value: "University of Chicago (BA 1935); Harvard (MA 1936, PhD 1941)", certainty: 0.7, cites: [{source: S1, locator: "para. 2"}, {source: S4, locator: "Biography"}], how_known: "Britannica; Wikipedia."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1948", certainty: 0.7, cites: [{source: S1, locator: "para. 4"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "My Life Philosophy (S5) discusses methodology and ethics, not a scored science–religion equation."}
  primary_system: {value: UNKNOWN, how_known: "Deepen D1: researched; no adult first-person creed on God's existence or a named religious system (P19). Checked and off-point: (1) S5 My Life Philosophy — 'easy faith' / liberal Weltanschauung from parents = ethical ideology, not JUDA/CHRIST/ATHE; (2) S6 Atlantic — 'cafeteria Keynesian' explained by cafeteria-Catholic metaphor (mass / family size) = how he picks Keynesian doctrine, not personal Catholicism; (3) S7 Chicago School talk — Knight as 'flaming atheist' describes Knight; 'old religion' / Jesuits line is Chicago-economics metaphor; (4) Infinite MIT oral history — Saint Peter admits-me-to-heaven joke about mathematizing economics (joke only); (5) S2/S4 Jewish family heritage — context only, never a code. No ATHE/AGNOS self-description found (contrast Friedman). Silence kept."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: JUDA, reason: "Rejected: Jewish family heritage and his own 'Jewish immigrants from Poland' family description (S2, S4) are heritage/context only, never a worldview code."}
    - {code: CHRIST, reason: "Rejected: cafeteria-Catholic metaphor (S6) and Jesuits/'old religion' Chicago metaphor (S7) are about economics schools, not personal Catholicism."}
    - {code: ATHE, reason: "Rejected: no denial of God in own words. Knight 'flaming atheist' (S7) is about Knight. No secondary label found that quotes him denying God."}
    - {code: AGNOS, reason: "Rejected: no suspension/self-description as agnostic read (Friedman contrast)."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Deepen D1: nothing first-hand on where God is / acts, or on denial of a personal God (P19). Metaphors in S6/S7 and the Saint Peter joke do not state a locus. Heritage (S2/S4) is not A."}
    B_cause: {value: UNKNOWN, how_known: "Deepen D1: not a scientist (P30; Friedman/Keynes precedent). Economics is not natural science for B unless a clear P16 nature-order line. Checked and off-point: S5 Machian 'HOW … only approach to WHY' is scientific methodology (thermodynamics as archetype), not a worldview profession that nature is lawful vs exception-bearing; Foundations thermodynamics analogy (S4) is method for economic theory, not P16. Silence on B kept."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing on reward and punishment of persons / afterlife ledger (P19). Saint Peter joke unused."}
    D_authority: {value: UNKNOWN, how_known: "Nothing on revelation against observation (P19). Logical-positivism / Mach remarks in S5 are methodology of economics/science, not a scored D creed."}
    E_scope: {value: UNKNOWN, how_known: "Not a scientist; nothing on same laws everywhere / in-group exceptions (P7, P19)."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus and B_cause are UNKNOWN; UNKNOWN takes precedence for the P4 test (P19)."}
  statements:
    - text: "made up of upwardly mobile Jewish immigrants from Poland who had prospered considerably in World War I, because Gary was a brand new steel-town when my family went there"
      cites: [{source: S4, locator: "Biography (his later words)"}]
      context: "Wikipedia EN attributes this family description to him ('he later said'). Heritage/context only — unused for JUDA or any worldview code."
      axes: []
      kind: "other"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Primary print locus (NYT obituary / interview) not re-opened this pass; Wikipedia attribution accepted for heritage context only."
    - text: "I am a cafeteria Keynesian. You know what a cafeteria catholic is? … I might go to mass every week, so I'm a good catholic, but I don't regulate my family size the way the Pope would like to."
      cites: [{source: S6, locator: "cafeteria Keynesian exchange"}]
      date: "2009-06-16"
      context: "Atlantic interview with Conor Clarke (published 17 June 2009). Explains picking Keynesian doctrine by analogy to cafeteria Catholicism. After span (P1). UNUSED for CHRIST or A — metaphor about economics, not personal creed."
      axes: []
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Ellipsis marks interviewer acknowledgment dropped; wording inside each turn as printed."
    - text: "When we are able to give a pleasingly satisfactory 'HOW' for the way of the world, that gives the only approach to 'WHY' that we shall ever attain."
      cites: [{source: S5, locator: "My methodology (Mach / thermodynamics)"}]
      date: "1983"
      context: "My Life Philosophy (American Economist 1983; Szenberg reprint). After span. Scientific methodology (classical thermodynamics as archetype) — UNUSED for B (P16) and unused as a theistic/atheistic creed."
      axes: []
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Read in USP Economia Aplicada reprint of the Szenberg Eminent Economists chapter."
  changes_over_life: []
  coder_notes: "Deepen D1 2026-10-24: silence kept. primary/A/B/mid UNKNOWN. Chart-moving NO. Not plotted. Span unchanged 1948. Collected Scientific Papers / Backhouse Founder of Modern Economics vol. 1 unread end-to-end (anti-Semitism at Harvard noted via S4 only)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Polish Jewish immigrant family (his description)", certainty: 0.7, cites: [{source: S4, locator: "Biography"}, {source: S2, locator: "Life"}], how_known: "Own words via Wikipedia; Nobel."}
  religious_heritage_by_birth: {value: "Jewish", certainty: 0.7, cites: [{source: S2, locator: "Life"}, {source: S4, locator: "Biography"}], how_known: "Nobel; Wikipedia quoting him."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1948", certainty: 0.7, cites: [{source: S1, locator: "para. 4"}], how_known: "The one listed lasting item (P29, P30)."}
  age_at_first_lasting_contribution: {value: 33, certainty: 0.7, cites: [{source: S1, locator: "opening; para. 4"}], how_known: "1948 − 1915 = 33 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None scored."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None scored."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Silence after deepen (P19)."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Mathematical economics (S1); no geometric cosmology claim.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data for Lane B cosmology."
  notes: "Economics mathematization ≠ geometric form of the cosmos."

institutions:
  - {value: "Massachusetts Institute of Technology", role: "professor of economics", years: "1940–2009", kind: "university", certainty: 0.7, cites: [{source: S1, locator: "para. 2"}, {source: S4, locator: "Biography"}], how_known: "Britannica; Wikipedia."}
collaborators: []

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 209"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Worldview: researched silence — no adult creed own words; metaphors/heritage logged and rejected."
  open_questions:
    - "A dated lasting source for Foundations (1947) or revealed preference would widen the span."
    - "Backhouse Founder of Modern Economics and Collected Scientific Papers unread end-to-end for any missed creed line."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "The Editors of Encyclopaedia Britannica"
    citation: "'Paul Samuelson.' Encyclopaedia Britannica (scholars edition). https://kids.britannica.com/scholars/article/Paul-Samuelson/65248"
    url: "https://kids.britannica.com/scholars/article/Paul-Samuelson/65248"
    accessed: 2026-10-24
    reliability_note: "Unsigned article, read in full (deepen re-open)."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, timing, institutions]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "Nobel Prize Outreach"
    citation: "'Paul A. Samuelson – Facts.' NobelPrize.org. https://www.nobelprize.org/prizes/economic-sciences/1970/samuelson/facts/"
    url: "https://www.nobelprize.org/prizes/economic-sciences/1970/samuelson/facts/"
    accessed: 2026-10-24
    reliability_note: "Facts page, read in full (deepen re-open)."
    source_quality: "other"
    used_for: [identity, contribution, childhood, heritage]
  - id: S3
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [review]
  - id: S4
    type: tertiary
    kind: "encyclopedia"
    author: "Wikipedia contributors"
    citation: 'Wikipedia. "Paul Samuelson." English Wikipedia. https://en.wikipedia.org/wiki/Paul_Samuelson. Biography and death sections read 2026-10-24 (dual bio, P50).'
    url: "https://en.wikipedia.org/wiki/Paul_Samuelson"
    accessed: 2026-10-24
    reliability_note: "Crowdsourced; dual bio against Britannica. Carries his Jewish-immigrants family quote and cafeteria-Keynesian self-description; primary print loci (NYT) not re-opened."
    source_quality: "reference entry"
    used_for: [identity, basics, childhood, heritage, worldview, institutions]
  - id: S5
    type: primary
    kind: "published work by the subject"
    author: "Paul A. Samuelson"
    citation: 'Samuelson, Paul A. "My Life Philosophy" / "My life philosophy: policy credos and working ways." The American Economist 27(2) (1983): 5-12; reprinted in Michael Szenberg (ed.), Eminent Economists: Their Life Philosophies (Cambridge University Press, 1992); Portuguese/English reprint Economia Aplicada 3(2) (1999). Read via https://www.revistas.usp.br/ecoa/article/download/218529/199662/660596 (2026-10-24).'
    url: "https://www.revistas.usp.br/ecoa/article/download/218529/199662/660596"
    accessed: 2026-10-24
    reliability_note: "His published life-philosophy essay; USP reprint authorized by author and CUP. Ethics and methodology only — no theistic creed."
    source_quality: "primary / own words"
    used_for: [worldview]
  - id: S6
    type: primary
    kind: "other"
    author: "Paul A. Samuelson (interviewed by Conor Clarke)"
    citation: 'Clarke, Conor. "An Interview With Paul Samuelson, Part One." The Atlantic, 17 June 2009. https://www.theatlantic.com/politics/archive/2009/06/an-interview-with-paul-samuelson-part-one/19572/'
    url: "https://www.theatlantic.com/politics/archive/2009/06/an-interview-with-paul-samuelson-part-one/19572/"
    accessed: 2026-10-24
    reliability_note: "Published interview transcript; cafeteria-Keynesian / cafeteria-Catholic exchange read in full. After span."
    source_quality: "newspaper interview"
    used_for: [worldview]
  - id: S7
    type: secondary
    kind: "journal article"
    author: "Paul A. Samuelson (interviewed; Chicago School conversation)"
    citation: 'The Chicago School: A conversation with Paul Samuelson (interview held October 1997). History of Economic Ideas / cooperative-individualism.org PDF reprint. https://cooperative-individualism.org/samuelson-paul_the-chicago-school-2010.pdf. Knight atheist and Jesuits/old-religion lines from search-indexed excerpts (full PDF fetch hung this pass).'
    url: "https://cooperative-individualism.org/samuelson-paul_the-chicago-school-2010.pdf"
    accessed: 2026-10-24
    reliability_note: "Interview transcript reprint; used only for off-point metaphor / Knight-description lines. Full local PDF not completed this pass — excerpts from search index; treat as secondary quotation strength for those lines."
    source_quality: "unofficial web copy"
    used_for: [worldview]
---

## Summary

Paul Samuelson (1915–2009), economist [S1; S4]. Deepen D1: primary_system UNKNOWN; A UNKNOWN; B UNKNOWN; mid_basin UNKNOWN. Not plotted. Chart-moving NO.

## Life and work

Gary; Chicago; Harvard; MIT from 1940 [S1; S4].

## Contribution and impact

Economics (1948) textbook; Foundations (1947); Nobel 1970 [S1; S2].

## Childhood and education

Jewish immigrant family (his words) [S2; S4]. Chicago BA; Harvard PhD [S1].

## Adult working worldview

Researched silence. No adult creed own words. Cafeteria-Catholic and Jesuits metaphors are about economics schools [S6; S7]. My Life Philosophy is ethics + methodology [S5]. Heritage only for Jewish family [S2; S4].

## Heritage (context only)

Jewish [S2; S4].

## Timing

1948, age 33 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Mathematical economics ≠ cosmic geometric form.

## Open questions

- Wider span if Foundations/revealed preference get a dated lasting tag.
- Backhouse biography / Collected Scientific Papers unread end-to-end.

## Research log

- 2026-10-19: Read Britannica (scholars edition); Nobel facts.
- 2026-10-24: Deepen D1. Wikipedia EN dual bio; My Life Philosophy (USP); Atlantic interview; Chicago School conversation excerpts; Infinite MIT Saint Peter joke (unused). Silence kept. No figures/. No fallacy_catalog.
