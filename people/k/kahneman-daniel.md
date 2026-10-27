---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z6)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to 20c_late. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen D1 (queue #152, F 3, rank 158). Re-opened Nobel autobiography (S1) and Raskin 2022 (S2). Nobel teen line: existence of God among questions, but 'more interested in what made people believe in God than … whether God existed' — AGNOS-leaning curiosity, not ATHE profession; childhood Pascal/faith essay before age 11. On Being (S6) Tippett quotes that Nobel line; Kahneman affirms ('I couldn't say it better') — after-span, does not lift A/ATHE past P20. Thinking, Fast and Slow (S5, IA OCR): Bloom origins-of-religion as System-1 psychology (not a personal creed); 'underestimate the role of chance in events' + Nobel flight-instructor 'important truth about the world' / regression — B 3 corroboration of probabilistic regularity, but P16 Hilbert addendum / P35 keep B 3 @ 0.5 alt 4 (no no-exception claim). No second 'stopped believing' stream. Dual bio (P50): birth 5 Mar 1934 (Guardian S7 + Wikipedia S4); death 27 Mar 2024 Nunningen SO (Guardian date; Nau.ch S8 + Wikipedia place; assisted suicide via Pegasos reported 2025). P47 source_quality on S1–S8. primary ATHE @0.5 (alt AGNOS); A 4 @0.5 (alts BELOW, 3); B 3 @0.5 (alt 4); mid BELOW. Chart-moving NO. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z7 audit fix (P10): mid_basin false 0.5 -> BELOW_THRESHOLD; A 4 is only at 0.5, under the 0.7 bar."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z6 audit fixes (blind audit at 85859f0, run 1; Z6-21, Z6-22 FAIL; v8's call on the auditor's advice): 'I remember very precisely the moment at which I stopped believing in God' is stated non-belief, not suspension (P38 reasoning; CODING_GUIDE §1), so primary_system AGNOS -> ATHE 0.5, alt AGNOS; A BELOW_THRESHOLD -> 4 at 0.5, alts BELOW_THRESHOLD and 3 (P20 explicit denial of a God that cares; Chomsky, Penrose, Sen precedents); mid_basin BELOW_THRESHOLD -> false at 0.5 (A 4 >= 3). Raskin page dated 2022-03-01 (page metadata datePublished), as Chomsky's in Z2. Now plotted, faded, at A 4 / B 3."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z6, order P32: F 3, rank 158). Basics from his Nobel autobiography (2002). Own voice: interview with Max Raskin (undated web page; after the span): never religious as an adult; lost his faith at about 15: 'maybe I could believe in God, but I could not believe in a God that cared whether or not I masturbate ... if I can't imagine God caring about me, then we were irrelevant to each other, and it really didn't matter whether he existed or not'; no afterlife; 'There's nothing mystical'. A scientist (P30, P35 addendum: experimental claims about human judgment, as Skinner). Span 1974–1979. primary_system AGNOS (0.5, alt BELOW_THRESHOLD); A BELOW_THRESHOLD; B 3 (0.5, alt 4; P35); C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD. Not plotted (no A). Draft, not reviewed."}

identity:
  id: kahneman-daniel
  display_name: "Daniel Kahneman"
  roster:
    canonical_name: "Daniel Kahneman"
    rank: 158
    F: 3
    models: [Claude, DeepSeek, GPT]
    band: "core (3–4)"
    status: "core"
    field: "psychology"
    field_bucket: "psychology / neuroscience"
  full_name: {value: "Daniel Kahneman", certainty: 1.0, cites: [{source: S1, locator: "Early years"}, {source: S4, locator: "infobox"}], how_known: "Nobel autobiography and Wikipedia (P50)."}
  native_name: {value: "דניאל כהנמן", certainty: 0.7, cites: [{source: S4, locator: "infobox"}], how_known: "Wikipedia Hebrew form."}
  aliases:
    - {name: "Daniel-Kahneman", kind: "roster alias"}

basics:
  birth:
    date: {value: "1934-03-05", calendar: gregorian, certainty: 1.0, cites: [{source: S7, locator: "closing life dates"}, {source: S4, locator: "infobox"}], how_known: "Guardian obituary and Wikipedia agree (P50); Nobel autobiography confirms year 1934."}
    place: {value: "Tel Aviv", modern_name: "Tel Aviv, Israel", polity_then: "Mandatory Palestine", certainty: 1.0, cites: [{source: S1, locator: "Early years"}, {source: S4, locator: "infobox"}], how_known: "Nobel autobiography (family domiciled in Paris) and Wikipedia."}
  death:
    date: {value: "2024-03-27", calendar: gregorian, certainty: 1.0, cites: [{source: S7, locator: "closing life dates"}, {source: S8, locator: "lead"}, {source: S4, locator: "infobox / Death"}], how_known: "Guardian 'died 27 March 2024'; Nau.ch 'am 27. März 2024'; Wikipedia (P50)."}
    place: {value: "Nunningen", modern_name: "Nunningen, Solothurn, Switzerland", polity_then: "Switzerland", certainty: 1.0, cites: [{source: S8, locator: "lead"}, {source: S4, locator: "infobox / Death"}], how_known: "Nau.ch (assisted suicide via Pegasos in Nunningen SO) and Wikipedia; manner publicised March 2025."}
  first_lasting_contribution_year: {value: 1974, certainty: 1.0, cites: [{source: S1, locator: "references"}, {source: S4, locator: "Judgment and decision-making"}], how_known: "Tversky and Kahneman, 'Judgment under uncertainty: Heuristics and biases', Science (1974); Wikipedia concurs."}
  era_bucket: {value: "1950 on", certainty: 1.0, cites: [{source: S1, locator: "references"}], how_known: "1974 (P2)."}
  region_of_birth: {value: "Middle East and North Africa", certainty: 1.0, cites: [{source: S1, locator: "Early years"}, {source: S4, locator: "infobox"}], how_known: "Israel / Mandatory Palestine (P3; regions.csv)."}
  region_of_work: {value: "Middle East and North Africa", certainty: 0.5, cites: [{source: S1, locator: "text"}, {source: S4, locator: "Career"}], how_known: "Hebrew University and the Van Leer Institute, Jerusalem, for most of 1974–78; then North America, so 0.5.", alternatives: [{value: "North America", cites: [{source: S4, locator: "Career"}], note: "UBC / Berkeley / Princeton after 1978; outside coded major_work_period 1974–1979."}]}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English", "Hebrew"], certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S4, locator: "lead"}], how_known: "Nobel English autobiography; Hebrew University career; Israeli-American."}
  occupations: {value: ["psychologist", "professor"], certainty: 1.0, cites: [{source: S1, locator: "text"}, {source: S4, locator: "lead"}], how_known: "Nobel autobiography and Wikipedia."}

contribution:
  era_bucket: 20c_late
  fields: {value: ["psychology of judgment and decision-making", "behavioral economics"], certainty: 1.0, cites: [{source: S1, locator: "text"}, {source: S4, locator: "lead"}], how_known: "Nobel and Wikipedia."}
  lasting_original_contributions:
    - {value: "Heuristics and biases (with Amos Tversky)", year: 1974, kind: theory, lasting: "Nobel Prize 2002 (S1)", certainty: 1.0, cites: [{source: S1, locator: "references; text"}, {source: S4, locator: "Judgment and decision-making"}], how_known: "Nobel autobiography; Wikipedia."}
    - {value: "Prospect theory (with Amos Tversky)", year: 1979, kind: theory, lasting: "'prospect theory undoubtedly afforded some legitimacy' to behavioral economics (S1)", certainty: 1.0, cites: [{source: S1, locator: "text"}, {source: S4, locator: "Prospect theory"}], how_known: "Nobel autobiography (Kahneman and Tversky, 1979); Wikipedia."}
  evidence_of_impact:
    - {value: "Nobel Memorial Prize in Economic Sciences 2002", kind: "honours in lifetime", certainty: 1.0, cites: [{source: S1, locator: "heading"}, {source: S4, locator: "Awards"}], how_known: "NobelPrize.org; Wikipedia."}
  major_works:
    - {value: "Thinking, Fast and Slow", year: 2011, kind: book, certainty: 1.0, cites: [{source: S5, locator: "title page / text"}, {source: S4, locator: "Books"}], how_known: "His own book; Wikipedia."}
    - {value: "Judgment Under Uncertainty: Heuristics and Biases (ed. with Slovic and Tversky)", year: 1982, kind: book, certainty: 0.7, cites: [{source: S4, locator: "Books"}], how_known: "Wikipedia bibliography."}
  honours:
    - {value: "Nobel Memorial Prize in Economic Sciences", year: 2002, certainty: 1.0, cites: [{source: S1, locator: "heading"}, {source: S4, locator: "Awards"}], how_known: "NobelPrize.org; Wikipedia."}
    - {value: "Presidential Medal of Freedom", year: 2013, certainty: 0.7, cites: [{source: S4, locator: "Awards"}, {source: S8, locator: "lead"}], how_known: "Wikipedia; Nau.ch."}
  definition_fit: {value: "clearly meets", rationale: "Founded the heuristics-and-biases programme and prospect theory (S1).", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Nobel."}

childhood:
  family_religion: {value: "Jewish (Lithuanian Jews in Paris); mother's family moderately religious", certainty: 0.7, cites: [{source: S1, locator: "Early years"}, {source: S2, locator: "Rabbi Kahaneman"}], how_known: "Nobel autobiography; (interview)."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated beyond a moderately religious maternal family."}
  parents_and_household:
    - {value: "Father, chief of research at a chemical factory", role: father, certainty: 0.7, cites: [{source: S1, locator: "Early years"}], how_known: "Nobel autobiography."}
    - {value: "Rabbi Kahaneman of the Ponevezh Yeshiva, paternal uncle", role: other, certainty: 0.7, cites: [{source: S2, locator: "Rabbi Kahaneman"}], how_known: "(interview)."}
  household_circumstances: {value: "Jewish family in occupied France 1940–44; emigrated to Palestine 1946", certainty: 0.7, cites: [{source: S1, locator: "Early years"}, {source: S2, locator: "Rabbi Kahaneman"}], how_known: "Nobel autobiography; interview."}
  schooling:
    - {value: "Religious school, Jerusalem and Tel Aviv", stage: "elementary school", run_by: "religious body", years: "1946–1949", certainty: 0.5, cites: [{source: S2, locator: "Rabbi Kahaneman"}], how_known: "(interview); years approximate."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading:
    - {value: "Childhood essay on faith quoting Pascal ('Faith is God made perceptible to the heart') before age 11", certainty: 0.7, cites: [{source: S1, locator: "Early years"}], how_known: "Nobel autobiography; juvenile, not adult creed."}
  childhood_mentors: []
  languages_in_childhood: {value: ["French", "Hebrew"], certainty: 0.5, cites: [{source: S1, locator: "Early years"}], how_known: "Inferred."}
  notable_events:
    - {value: "Lost his religious faith at about 15", year: 1949, certainty: 0.5, cites: [{source: S2, locator: "Rabbi Kahaneman"}], how_known: "(interview); year from his age; after-span retrospective (P20)."}
    - {value: "Teen interest shifted from whether God exists to what makes people believe in God", year: 1950, certainty: 0.5, cites: [{source: S1, locator: "Early years"}, {source: S6, locator: "Tippett opening"}], how_known: "Nobel autobiography; affirmed in On Being; year approximate (teens)."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1974–1979", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nobel and TFAS frame religion as a psychological object (why people believe); no scored science–religion relation statement for his own creed."}
  primary_system:
    value: ATHE
    basis: recorded_interview
    certainty: 0.5
    cites: [{source: S2, locator: "Rabbi Kahaneman"}]
    how_known: "(interview) 2022; After the span, so capped at 0.5 (P20). Stated non-belief: 'I remember very precisely the moment at which I stopped believing in God'; never religious as an adult; no afterlife; 'There's nothing mystical'. Nobel (S1) and On Being (S6) corroborate teen curiosity about belief-formation, not a second ATHE profession — A/ATHE support remains single (P48)."
    rationale: "ATHE: stated non-belief is more than suspension (P38 reasoning; AGNOS is explicit suspension, CODING_GUIDE §1). v8's call on the auditor's advice (Z6 audit, Z6-21). Alternative AGNOS: 'maybe I could believe in God'; 'it really didn't matter whether he existed or not'; Nobel 'more interested in what made people believe in God than … whether God existed'."
    alternatives:
      - {value: AGNOS, note: "'maybe I could believe in God ... it really didn't matter whether he existed or not'; Nobel teen line affirmed in On Being.", cites: [{source: S2, locator: "Rabbi Kahaneman"}, {source: S1, locator: "Early years"}, {source: S6, locator: "Tippett opening"}]}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: ATHE, reason: "Coded at 0.5: 'stopped believing in God' (Z6 audit); deepen found no second stream to lift past P20."}
    - {code: AGNOS, reason: "Alternative: 'maybe I could believe in God'; existence 'didn't matter'; Nobel/On Being belief-formation curiosity."}
  lio_axes:
    A_locus:
      value: 4
      basis: recorded_interview
      certainty: 0.5
      support: single
      cites: [{source: S2, locator: "Rabbi Kahaneman"}]
      how_known: "(interview) 2022; Explicit denial of a personal, intervening God is scored (CODING_GUIDE §6, P20): 'I could not believe in a God that cared'; 'I stopped believing in God'. The retrospective covers his whole adult life, span included; after the span, so 0.5. Nobel/On Being do not restate the personal-God denial — support single (P48)."
      rationale: "By analogy with P38 and the Sen, Chomsky and Penrose precedents. v8's call on the auditor's advice (Z6 audit, Z6-22). Deepen D1: keep; no in-span lift."
      alternatives:
        - {value: BELOW_THRESHOLD, note: "Indifference ('irrelevant to each other') rather than a locus view.", cites: [{source: S2, locator: "Rabbi Kahaneman"}]}
        - {value: 3, note: "Denies only a caring God ('maybe I could believe in God').", cites: [{source: S2, locator: "Rabbi Kahaneman"}]}
    B_cause:
      value: 3
      basis: inference_from_work
      certainty: 0.5
      support: corroborated
      cites: [{source: S1, locator: "flight-instructor / regression passage"}, {source: S5, locator: "Part 3 theme / role of chance"}]
      how_known: "Scientist (P30; P35 addendum: testable claims about human judgment). Working science alone → B 3 @ 0.5 alt 4 (P35). Deepen: Nobel 'important truth about the world' via regression to the mean; TFAS 'underestimate the role of chance in events' — probabilistic regularity, not a no-exception claim. P16 Hilbert addendum: explicit lawful-order remark without no-exception claim stays B 3 @ 0.5 alt 4. Two source ids → corroborated (P48). Not lifted to 0.7."
      rationale: "Scored on his account of nature (P6) via working experimental psychology plus own remarks on chance/regression as features of the world. No miracle, petition, or exceptionless-determinism profession read. Named alternative 4 under P35."
      alternatives:
        - {value: 4, note: "P35 alternative if a no-exception claim of his own were read.", cites: [{source: S1, locator: "text"}, {source: S5, locator: "text"}]}
    C_ledger: {value: UNKNOWN, how_known: "'Do you believe in an afterlife? No.' (interview S2) not scored as ledger (coder's call, unchanged); TFAS Bloom on immortal souls is Bloom's claim, not Kahneman's profession."}
    D_authority: {value: UNKNOWN, how_known: "Nothing scored on revelation vs observation (P19)."}
    E_scope: {value: BELOW_THRESHOLD, note: "Working science assumes regularities of judgment across people, which bears on E's first question, but E is not scored from working science alone (P19, P30 addendum).", how_known: "BELOW_THRESHOLD under P19."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is at least 3 only at 0.5; P10 caps mid_basin by the certainty of the tested condition, below the 0.7 bar, so BELOW_THRESHOLD (Chomsky, Sen, Russell, Franklin precedents; Z7 audit). Chart-moving NO (deepen 2026-10-24)."}
  statements:
    - text: "I was walking home, and I had the insight that maybe I could believe in God, but I could not believe in a God that cared whether or not I masturbate. That was a very sudden insight. That if I can't imagine God caring about me, then we were irrelevant to each other, and it really didn't matter whether he existed or not. And that was the end of the religion for me."
      cites: [{source: S2, locator: "Rabbi Kahaneman"}]
      context: "Interview with Max Raskin; recalling age about 15; after the span."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "Page dated 2022-03-01 (page metadata). Re-confirmed deepen 2026-10-24."
    - text: "The questions that interested me in my teens were philosophical – the meaning of life, the existence of God, and the reasons not to misbehave. But I was discovering that I was more interested in what made people believe in God than I was in whether God existed, and I was more curious about the origins of people's peculiar convictions about right and wrong than I was about ethics."
      cites: [{source: S1, locator: "Early years"}]
      context: "Nobel autobiography (2002); teen years before the span; AGNOS-leaning curiosity, not an ATHE profession."
      axes: [A_locus]
      kind: "autobiography"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Affirmed in On Being (S6) when Tippett read the line back; after-span affirmation."
    - text: "We are prone to overestimate how much we understand about the world and to underestimate the role of chance in events."
      cites: [{source: S5, locator: "introduction / Part 3 theme"}]
      context: "Thinking, Fast and Slow (2011), after the span; own framing of uncertainty and chance."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Read in Internet Archive DJVU OCR of the book; not checked against a publisher facsimile this pass."
    - text: "This was a joyous moment, in which I understood an important truth about the world: because we tend to reward others when they do well and punish them when they do badly, and because there is regression to the mean, it is part of the human condition that we are statistically punished for rewarding others and rewarded for punishing them."
      cites: [{source: S1, locator: "flight-instructor / regression passage"}]
      context: "Nobel autobiography recalling an Israeli Air Force flight-instructor demonstration; statistical regularity as a truth about the world."
      axes: [B_cause]
      kind: "autobiography"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
  changes_over_life:
    - {value: "Childhood religious schooling and a pre-teen Pascal/faith essay; loss of faith ~age 15 (Raskin retrospective); adult working years with no recovered theism in sources read.", certainty: 0.5, cites: [{source: S1, locator: "Early years"}, {source: S2, locator: "Rabbi Kahaneman"}], how_known: "Nobel + Raskin; timing of adult non-belief during 1974–79 still rests on after-span retrospective (P20)."}
  coder_notes: "Psychology counts as science here under the P35 addendum (Skinner); flag if the auditor reads him as social science. Deepen D1: ATHE/A stay 0.5 (P20/P38); B stays 3 @ 0.5 (P35/P16); chart-moving NO."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Lithuanian Jewish", certainty: 0.7, cites: [{source: S1, locator: "Early years"}], how_known: "Nobel autobiography."}
  religious_heritage_by_birth: {value: "Jewish", certainty: 0.7, cites: [{source: S1, locator: "Early years"}], how_known: "Nobel autobiography."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Religious school (S2); content not detailed."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1974–1979", certainty: 0.7, cites: [{source: S1, locator: "text; references"}], how_known: "Heuristics and biases (1974) to prospect theory (1979) (P29, P30)."}
  age_at_first_lasting_contribution: {value: 40, certainty: 0.7, cites: [{source: S1, locator: "Early years; references"}, {source: S7, locator: "closing life dates"}], how_known: "1974 − 1934 = 40 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: "c. 1949 (loss of faith at about 15)", certainty: 0.5, cites: [{source: S2, locator: "Rabbi Kahaneman"}], how_known: "(interview); after-span retrospective."}
  lio_views_relative_to_major_work: {value: "before major work", certainty: 0.5, cites: [{source: S2, locator: "Rabbi Kahaneman"}], how_known: "(interview); loss of faith ~1949 vs span 1974–79."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "No in-span creed statement; adult ATHE/A rest on after-span retrospective (P20)."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Experimental psychology (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "Hebrew University of Jerusalem", role: professor, years: "1961–1978", kind: university, certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S4, locator: "Career"}], how_known: "Nobel autobiography; Wikipedia."}
  - {value: "Princeton University", role: "professor emeritus of psychology and public affairs", years: "1993–2024", kind: university, certainty: 0.7, cites: [{source: S4, locator: "infobox / Career"}], how_known: "Wikipedia; after the coded span."}
collaborators:
  - {value: "Amos Tversky", relation: collaborator, note: "heuristics and biases; prospect theory", certainty: 1.0, cites: [{source: S1, locator: "text"}, {source: S4, locator: "Partnership with Amos Tversky"}], how_known: "Nobel autobiography; Wikipedia."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 158"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Only own words stating ATHE/A 4 are the 2022 Raskin interview after the span (P20)."
    - "TFAS chance quote read in IA OCR only (archive scan OCR); not publisher-facsimile checked."
  open_questions:
    - "In-span or near-span own-voice creed statement that would lift ATHE/A past P20 0.5."
    - "Own-voice no-exception / exceptionless nature-order claim that would lift B past P35/P16 0.5."

sources:
  - id: S1
    type: primary
    kind: "published work by the subject"
    author: "Daniel Kahneman"
    citation: "Kahneman, Daniel. 'Biographical.' NobelPrize.org (2002). https://www.nobelprize.org/prizes/economic-sciences/2002/kahneman/biographical/"
    url: "https://www.nobelprize.org/prizes/economic-sciences/2002/kahneman/biographical/"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "His own Nobel autobiography."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: primary
    kind: "other"
    author: "Daniel Kahneman, interviewed by Max Raskin"
    citation: "Raskin, Max. 'Interview with Daniel Kahneman.' maxraskin.com (2022-03-01). https://www.maxraskin.com/interviews/daniel-kahneman"
    url: "https://www.maxraskin.com/interviews/daniel-kahneman"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "Published interview transcript (recorded_interview, P8); dated 2022-03-01 in the page metadata (datePublished)."
    used_for: [childhood, worldview, timing]
  - id: S3
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    source_quality: "study roster"
    reliability_note: "Study's own roster."
    used_for: [review]
  - id: S4
    type: secondary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia. 'Daniel Kahneman.' https://en.wikipedia.org/wiki/Daniel_Kahneman"
    url: "https://en.wikipedia.org/wiki/Daniel_Kahneman"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Tertiary; used for dual bio (P50) and career cross-check, not for worldview scoring alone."
    used_for: [identity, basics, contribution, institutions, collaborators]
  - id: S5
    type: primary
    kind: "published work by the subject"
    author: "Daniel Kahneman"
    citation: "Kahneman, Daniel. Thinking, Fast and Slow. Farrar, Straus and Giroux, 2011. (Internet Archive DJVU OCR)"
    url: "https://archive.org/details/DanielKahnemanThinkingFastAndSlow"
    accessed: 2026-10-24
    source_quality: "archive scan (OCR only)"
    reliability_note: "Own book; quotations verified against IA OCR only this pass (P21 archive scan OCR)."
    used_for: [contribution, worldview]
  - id: S6
    type: primary
    kind: "other"
    author: "Daniel Kahneman, interviewed by Krista Tippett"
    citation: "Tippett, Krista. 'Daniel Kahneman — Why We Contradict Ourselves and Confound Each Other.' On Being. https://onbeing.org/programs/daniel-kahneman-why-we-contradict-ourselves-and-confound-each-other/"
    url: "https://onbeing.org/programs/daniel-kahneman-why-we-contradict-ourselves-and-confound-each-other/"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "Published interview transcript; after the span; affirms Nobel teen line on belief-formation."
    used_for: [worldview, childhood]
  - id: S7
    type: secondary
    kind: "other"
    author: "Georgina Ferry"
    citation: "Ferry, Georgina. 'Daniel Kahneman obituary.' The Guardian (2024-04-04). https://www.theguardian.com/science/2024/apr/04/daniel-kahneman-obituary"
    url: "https://www.theguardian.com/science/2024/apr/04/daniel-kahneman-obituary"
    accessed: 2026-10-24
    source_quality: "other"
    reliability_note: "Obituary; dual bio for birth/death dates (P50)."
    used_for: [basics, timing]
  - id: S8
    type: secondary
    kind: "other"
    author: "Antun Boskovic"
    citation: "Boskovic, Antun. 'Nunningen SO: Nobelpreisträger kam für Sterbehilfe in die Schweiz.' Nau.ch (2025-03-25). https://www.nau.ch/news/schweiz/nunningen-so-nobelpreistrager-kam-fur-sterbehilfe-in-die-schweiz-66943858"
    url: "https://www.nau.ch/news/schweiz/nunningen-so-nobelpreistrager-kam-fur-sterbehilfe-in-die-schweiz-66943858"
    accessed: 2026-10-24
    source_quality: "other"
    reliability_note: "Swiss news report of assisted death in Nunningen; dual with Wikipedia for death place (P50)."
    used_for: [basics, contribution]
---

## Summary

Daniel Kahneman (1934–2024), psychologist [S1; S4; S7]. Draft deepen: ATHE (0.5, alt AGNOS); A 4 (0.5); B 3 (0.5, alt 4). Plotted, faded. Chart-moving NO.

## Life and work

Paris (occupied France), Jerusalem, North America; died Nunningen, Switzerland, 27 March 2024 [S1; S4; S7; S8].

## Contribution and impact

Heuristics and biases; prospect theory; Thinking, Fast and Slow [S1; S4; S5].

## Childhood and education

Religious schooling; childhood Pascal/faith essay; faith lost at about 15 [S1; S2].

## Adult working worldview

Stopped believing in God at about 15 (Raskin 2022, after span) [S2]. Nobel/On Being: more interested in belief-formation than God's existence [S1; S6]. Chance/regression as features of the world [S1; S5]; B stays P35/P16 @ 0.5.

## Heritage (context only)

Lithuanian Jewish [S1].

## Timing

1974–1979, age 40 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- In-span creed statement to lift ATHE/A past P20.
- Own-voice no-exception nature-order claim to lift B past P35/P16.

## Research log

- 2026-10-19: Read Nobel autobiography; Raskin interview.
- 2026-10-19: Z6 audit fixes: ATHE, A 4; Raskin page date from metadata.
- 2026-10-24: Deepen D1 — Nobel re-open; TFAS OCR; On Being; Wikipedia; Guardian; Nau.ch; no chart-moving lift.
