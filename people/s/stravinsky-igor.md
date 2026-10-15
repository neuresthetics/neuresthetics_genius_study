---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch G)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-15
  change_log:
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch G, order P32: F 5, rank 40). Basics from Britannica (White). Worldview from Per Dahl (Danish Musicology Online 2016), who quotes Conversations with Igor Stravinsky (with Robert Craft, 1959): belief in 'a personal God, a personal Devil and the miracles of the Church'. Britannica calls the Craft books 'factually unreliable', so every worldview field is capped at 0.5. primary_system CHRIST (Russian Orthodox) 0.5; A 0 at 0.5 (alt 1); B 2 at 0.5 (alt 3); C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD. Plotted. Ruling question raised (RQ1 batch G), since ruled as P43. Draft, not reviewed."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "fallacy_catalog blind audit of 5ff29b4: all claims HOLD. RQ1 ruled by Jason as P43 (interview cap 0.5; plotted faded). CLTHEI added as a named alternative code. No value changes."}

identity:
  id: stravinsky-igor
  display_name: "Igor Stravinsky"
  roster:
    canonical_name: "Igor Stravinsky"
    rank: 40
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: music
    field_bucket: music
  full_name: {value: "Igor Fyodorovich Stravinsky", certainty: 0.7, cites: [{source: S1, locator: "At a Glance"}], how_known: "Britannica."}
  native_name: {value: UNKNOWN, how_known: "Cyrillic form not recorded in the source read."}
  aliases:
    - {name: "Igor-Stravinsky", kind: "roster alias"}
    - {name: "Stravinsky-Igor", kind: "roster alias"}

basics:
  birth:
    date: {value: "1882-06-17", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica: 'June 5 [June 17, New Style], 1882'; Gregorian (New Style) date kept."}
    place: {value: "Oranienbaum, near St. Petersburg, Russia", modern_name: "Lomonosov, Russia", polity_then: "Russian Empire", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "1971-04-06", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "New York, New York, U.S.", modern_name: "New York, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1910, certainty: 0.7, cites: [{source: S1, locator: "'Life and career'"}], how_known: "The Firebird, premiered 25 June 1910, 'made Stravinsky known overnight' (P13). Earlier student works were performed but are not listed as lasting."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S1, locator: "'Life and career'"}], how_known: "From 1910 (P2)."}
  region_of_birth: {value: "Eastern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Russia is Eastern Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.5, cites: [{source: S1, locator: "'Life and career'"}], how_known: "Switzerland and France 1910–1939, then the United States from 1940; the main works through 1939 were in Western Europe (0.5)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [Russian, French], certainty: 0.5, cites: [{source: S1, locator: "'Life and career'"}], how_known: "Inferred from his residence and texts set; not stated."}
  occupations: {value: ["composer", "pianist", "conductor"], certainty: 0.7, cites: [{source: S1, locator: "'Life and career'"}], how_known: "Britannica."}

contribution:
  fields: {value: ["music"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "The Firebird", year: 1910, kind: work, lasting: "made him known overnight (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Life and career'"}], how_known: "Britannica."}
    - {value: "The Rite of Spring", year: 1913, kind: work, lasting: "'an early modernist landmark' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Life and career'"}], how_known: "Britannica."}
    - {value: "Symphony of Psalms", year: 1930, kind: work, lasting: "(S1)", certainty: 0.7, cites: [{source: S1, locator: "'Life and career'"}], how_known: "Britannica."}
    - {value: "The Rake's Progress", year: 1951, kind: work, lasting: "his only full-length opera (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Life and career'"}], how_known: "Britannica (worked on 1948–51)."}
    - {value: "Requiem Canticles", year: 1966, kind: work, lasting: "'his last major work' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Life and career'"}], how_known: "Britannica."}
  evidence_of_impact:
    - {value: "Royal Philharmonic Society Gold Medal (1954); Wihuri Sibelius Prize (1963)", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "'Revolutionary impact on musical thought' (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Russian Orthodox (nominal)", certainty: 0.5, cites: [{source: S2, locator: "p. 61"}], how_known: "Inferred: he 'rejoined' the Russian Orthodox Church in 1926 (S2), implying an earlier membership; the parents' practice is not stated."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father one of the leading Russian operatic basses of his day", role: parents, certainty: 0.7, cites: [{source: S1, locator: "'Life and career'"}], how_known: "Britannica body. The mother is named only in the Top Questions box, which is not cited."}
  household_circumstances: {value: "Musical, theatrical and literary household", certainty: 0.7, cites: [{source: S1, locator: "'Life and career'"}], how_known: "Britannica."}
  schooling:
    - {value: "St. Petersburg University (law and philosophy)", stage: university, run_by: "state or municipal", years: "–1905", ages: "–23", certainty: 0.7, cites: [{source: S1, locator: "'Life and career'"}], how_known: "Britannica: graduated 1905."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "Nikolay Rimsky-Korsakov, private teacher from 1902", certainty: 0.7, cites: [{source: S1, locator: "'Life and career'"}], how_known: "Britannica."}
  languages_in_childhood: {value: TODO}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1910–1966", certainty: 0.7, cites: [{source: S1, locator: "'Life and career'"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Russian Orthodox Church (rejoined 1926; first communion 9 April 1926)", certainty: 0.7, cites: [{source: S2, locator: "p. 61"}, {source: S1, locator: "'Life and career' ('In 1926 Stravinsky experienced a religious conversion')"}], how_known: "Dahl and Britannica agree on the 1926 conversion; the communion date is Dahl's."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing read on science and religion."}
  primary_system:
    value: CHRIST
    basis: recorded_interview
    certainty: 0.5
    cites: [{source: S2, locator: "p. 64 and note 20 (Conversations, 1959, p. 104)"}, {source: S1, locator: "'Life and career'"}]
    rationale: "Rejoined the Russian Orthodox Church in 1926 (S1, S2) and, in Conversations, says composing in the old church forms needs belief 'in a personal God, a personal Devil and the miracles of the Church' (S2). Under P42 the Craft book counts as his words because Dahl attributes this answer to him ('the composer responds', S2). Capped at 0.5 because Britannica calls the Craft books 'factually unreliable' (S1) and the text is read only in Dahl's quotation."
    how_known: "(interview) Dahl's quotation of Conversations; Conversations not read."
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Chosen: Orthodox communion from 1926; personal God and Church miracles."}
    - {code: CLTHEI, reason: "Named alternative (fallacy_catalog audit of 5ff29b4): a personal God with live Church miracles fits interventionist personal theism; not chosen as primary because the profession is confessional (Orthodox). Not result-changing: A and B decide the plot."}
  lio_axes:
    A_locus:
      value: 0
      basis: recorded_interview
      certainty: 0.5
      cites: [{source: S2, locator: "p. 64 and note 20"}]
      how_known: "(interview) Conversations (with Craft), read in Dahl's quotation; 0.5 for the disputed voice of the Craft books (S1)."
      rationale: "'A personal God', set against belief in mere 'symbolic figures': a personal God, not the world. Scored 0 (transcendent person). Named alternative: 1 (nothing on God being outside the world as such)."
    B_cause:
      value: 2
      basis: recorded_interview
      certainty: 0.5
      cites: [{source: S2, locator: "p. 64 and note 20"}]
      how_known: "(interview) Same passage; 0.5 for the disputed voice and secondary quotation."
      rationale: "Scored on his account of nature (P6, P16): belief in 'the miracles of the Church' is a stated acceptance of miracles. The Church's miracles are not stated to be rare or past, and nothing states a lawful general order, so the B 2 anchor (miracles as a live part of how events go, P27) fits better than B 3. Named alternative: 3 (if read as accepted past miracles within a lawful order)."
    C_ledger: {value: UNKNOWN, how_known: "Nothing read on reward and punishment."}
    D_authority: {value: UNKNOWN, how_known: "Nothing read on revelation against observation."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A 0 and B 2 at 0.5: A ≤ 1 with B 2 would have no branch at ≥ 0.7 (§6), and both axes are below the test's 0.7 bar, so BELOW_THRESHOLD (P19)."}
  statements:
    - text: "Of course. And not simply be one who believes in symbolic figures, but in a personal God, a personal Devil and the miracles of the Church"
      cites: [{source: S2, locator: "p. 64; note 20 cites Stravinsky and Craft, Conversations with Igor Stravinsky (London: Faber & Faber, 1959), p. 104"}]
      date: "1959"
      context: "Answer, in Conversations with Robert Craft, to whether one must be a believer to compose in the old church forms."
      axes: [A_locus, B_cause]
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "Dahl's wording. Primary check pending against Conversations (1959). A search-engine summary gave a different English wording ('in the Person of the Lord, the Person of the Devil, and the Miracles of the Church'), unverified; the printed text must decide. The Craft books' first-person wording is disputed (S1: 'factually unreliable')."
    - text: "For some years before my actual “conversion”, a mood of acceptance had been cultivated in me by a reading of the Gospels and by other religious literature"
      cites: [{source: S2, locator: "p. 64; note 16 cites Expositions and Developments (1962), pp. 63–64"}]
      date: "1962"
      context: "On his 1926 return to the Church. Context only; not used to score."
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "Dahl's quotation; primary check pending."
  changes_over_life:
    - {value: "Return to the Russian Orthodox Church", year: 1926, certainty: 0.7, cites: [{source: S1, locator: "'Life and career'"}, {source: S2, locator: "p. 61"}], how_known: "Two sources. The scored axes describe the worldview from 1926; the Firebird-to-Rite years (1910–1913) are before it, and nothing is read on them."}
  coder_notes: "Coder's call: the only first-person evidence is from the Craft books, read in Dahl's quotation, so everything is at 0.5. A reported Venetian prayer-healing (1925) and a 1936 'I happen to be a believer' line were seen only in search excerpts and are not used. RQ1 (batch G) was ruled by Jason as P43 (2026-10-15): Craft-book statements score, flagged as interview, capped at 0.5, and go no higher without a document in his own hand; B 2 (alternative 3) is kept. He is plotted faded; with Pascal he is one of two people plotted left of B 3, and the only one resting on a disputed interview voice."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Russian", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Russian Orthodox", certainty: 0.5, cites: [{source: S2, locator: "p. 61"}], how_known: "Inferred from 'rejoined' (S2)."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1910–1966", certainty: 0.7, cites: [{source: S1, locator: "'Life and career'"}], how_known: "1910 to 1966, first to last listed lasting contribution (P29, P30)."}
  age_at_first_lasting_contribution: {value: 28, certainty: 0.7, cites: [{source: S1, locator: "opening; 'Life and career'"}], how_known: "1910 − 1882 = 28 (P30)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "B 2 is not an LIO-type view (P27); none read."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S2, locator: "p. 64"}], how_known: "Nothing LIO-type read."}
  worldview_during_major_work: {value: "CHRIST", certainty: 0.5, cites: [{source: S2, locator: "p. 61, p. 64"}], how_known: "From 1926; before then not documented."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Serial technique and Neoclassical form are musical, not geometric (S1).", certainty: 0.5, cites: [{source: S1, locator: "'Life and career'"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "'Life and career'"}], how_known: "Nothing on mathematics."}
  circle_present: {value: "no", rationale: "Personal God and Church miracles; no lawful-order statement.", certainty: 0.5, cites: [{source: S2, locator: "p. 64"}], how_known: "Coder's reading."}
  reading: "Confessional Orthodox belief in a personal God and Church miracles; no LIO circle read."
  notes: ""

institutions:
  - {value: "Ballets Russes (Serge Diaghilev)", role: "commissioned composer", years: "1910–1928", kind: "patron or funder", certainty: 0.7, cites: [{source: S1, locator: "'Life and career'"}], how_known: "Britannica."}
  - {value: "Harvard University (Charles Eliot Norton Lectures)", role: lecturer, years: "1939–1940", kind: university, certainty: 0.7, cites: [{source: S1, locator: "'Life and career'"}], how_known: "Britannica."}
collaborators:
  - {value: "Robert Craft", relation: collaborator, note: "assistant and co-author of six books from 1948", certainty: 0.7, cites: [{source: S1, locator: "'Life and career'"}], how_known: "Britannica."}
  - {value: "Nikolay Rimsky-Korsakov", relation: teacher, note: "private pupil from 1902", certainty: 0.7, cites: [{source: S1, locator: "'Life and career'"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 40"}], how_known: "Study roster."}
  controversies:
    - {value: "Reliability of the Craft books as his own words", certainty: 0.7, cites: [{source: S1, locator: "'Life and career' ('factually unreliable')"}], how_known: "Britannica; Dahl also notes Taruskin and Walsh revisit the Craft portrayal (S2, p. 61)."}
  data_quality_flags: []
  open_questions:
    - "Check Conversations (1959), p. 104, for the exact wording; read Walsh or Taruskin on his religion; P43 cap."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Eric Walter White"
    citation: "White, Eric Walter. \"Igor Stravinsky.\" Encyclopaedia Britannica, updated 11 September 2026. https://www.britannica.com/biography/Igor-Stravinsky."
    url: "https://www.britannica.com/biography/Igor-Stravinsky"
    accessed: 2026-10-15
    reliability_note: "Signed article body; the Top Questions box is not used."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators, review]
  - id: S2
    type: secondary
    kind: "journal article"
    author: "Per Dahl"
    year: 2016
    citation: "Dahl, Per. \"Text, Identity and Belief in Stravinsky's Symphony of Psalms.\" Danish Musicology Online, Special Edition 2016 (17th Nordic Musicological Congress), pp. 61–80. ISSN 1904-237X."
    url: "https://www.danishmusicologyonline.dk/arkiv/arkiv_dmo/dmo_saernummer_2016/dmo_saernummer_2016_NMC_04.pdf"
    accessed: 2026-10-15
    reliability_note: "Scholarly article (congress proceedings), read in full as PDF; page numbers as printed."
    used_for: [childhood, worldview, heritage, timing, lane_b, review]
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

# Igor Stravinsky

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Igor Stravinsky (1882–1971), Russian-born composer: The Firebird, The Rite of Spring, Symphony of Psalms, The Rake's Progress [S1]. Draft: primary_system CHRIST 0.5; A 0 and B 2 at 0.5; C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD. Plotted.

## Life and work

St. Petersburg; Ballets Russes in Paris; Switzerland, France, then Hollywood from 1940 [S1].

## Contribution and impact

Firebird (1910), Rite (1913), Neoclassical and late serial works to Requiem Canticles (1966) [S1].

## Childhood and education

Son of a leading operatic bass; law at St. Petersburg; private pupil of Rimsky-Korsakov [S1].

## Adult working worldview

Returned to the Russian Orthodox Church in 1926 [S1, S2]. In Conversations he says sacred composition needs belief 'in a personal God, a personal Devil and the miracles of the Church' [S2, p. 64]. The Craft books are 'factually unreliable' [S1], so this is held at 0.5.

## Heritage (context only)

Russian, Orthodox by birth [S1, S2].

## Timing

First lasting contribution 1910, at 28 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No LIO circle read [S2].

## Open questions

- Conversations p. 104; Walsh; Taruskin. A document in his own hand would be needed to raise any score above 0.5 (P43).

## Research log

- 2026-10-15: Read Britannica (White) and Dahl (2016, full PDF). Search excerpts (Sydney Undergraduate journal on Maritain; NYRB 'Obiter Dicta') seen but not cited.
