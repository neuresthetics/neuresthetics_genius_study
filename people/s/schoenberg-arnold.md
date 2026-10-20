---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z4)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z5 audit fix (Z5-08, P26): question-box cite for Moses und Aron and the 1932 span end removed. Re-sourced to the Britannica body ('Evolution from tonality': 'his greatest work, the opera Moses und Aron (begun in 1930)', as excerpted by search, like S5's 1921 passage). Span 1899–1932 -> 1899–1930 (0.5). Worldview unchanged; readmission to Judaism (July 1933) still just after the span. Not plotted."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z4 audit fixes (blind audit /workspace/genius_study_audit/gs_a19c474_Z4/run1/): Z4-11: Dehmel letter kind now 'private letter' (printed posthumously). S4 (DeVoto) note: full lecture read. coder_notes add the 1923 Kandinsky and 1890 Goldschmied leads. Values unchanged."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z4, order P32: F 3, rank 148). Basics from Britannica (Dika Newlin, signed). Religion facts: Lutheran baptism 1898 (DeVoto, Tufts); readmitted to Judaism at the Liberal synagogue, Paris, July 1933 (JTA, 25 July 1933). Own words: letter to Richard Dehmel, 13 December 1912 (Arnold Schoenberg Letters, ed. Erwin Stein, scan): oratorio plan on 'modern man ... despite having been an atheist ... wrestles with God ... and finally succeeds in finding God and becoming religious. Learning to pray!' A plan for a work, not a profession; libretto characters not counted (P42). Not a scientist (P30), so B UNKNOWN. Span 1899–1932. primary_system BELOW_THRESHOLD (leads JUDA from 1933, CHRIST nominal 1898–1933); A BELOW_THRESHOLD; B UNKNOWN; C, D, E UNKNOWN; mid_basin UNKNOWN. Not plotted (no B). Draft, not reviewed."}

identity:
  id: schoenberg-arnold
  display_name: "Arnold Schoenberg"
  roster:
    canonical_name: "Arnold Schoenberg"
    rank: 148
    F: 3
    models: [Claude, Gemini, Grok]
    band: "core (3–4)"
    status: core
    field: music
    field_bucket: music
  full_name: {value: "Arnold Franz Walter Schoenberg", certainty: 0.7, cites: [{source: S1, locator: "In full"}], how_known: "Britannica."}
  native_name: {value: "Arnold Schönberg", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  aliases:
    - {name: "Schoenberg-Arnold", kind: "roster alias"}
    - {name: "Arnold Schönberg", kind: "transliteration"}

basics:
  birth:
    date: {value: "1874-09-13", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "Born"}], how_known: "Britannica."}
    place: {value: "Vienna", modern_name: "Vienna, Austria", polity_then: "Austria-Hungary", certainty: 0.7, cites: [{source: S1, locator: "Born"}], how_known: "Britannica."}
  death:
    date: {value: "1951-07-13", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "Died"}], how_known: "Britannica."}
    place: {value: "Los Angeles, California", modern_name: "Los Angeles, California, USA", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "Died"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1899, certainty: 0.7, cites: [{source: S1, locator: "'First major works'"}], how_known: "Verklärte Nacht (1899), 'one of Schoenberg's most-popular compositions'."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "'First major works'"}], how_known: "1899 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "Born"}], how_known: "Austria (P3; regions.csv)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Vienna and Berlin over the span."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["German"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "German titles."}
  occupations: {value: ["composer", "teacher of composition", "theorist", "painter"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

contribution:
  fields: {value: ["music composition", "music theory"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Verklärte Nacht", year: 1899, kind: work, lasting: "'one of Schoenberg's most-popular compositions' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'First major works'"}], how_known: "Britannica."}
    - {value: "Method of composition with twelve tones", year: 1921, kind: method, lasting: "serialism and the 12-tone row (S1)", certainty: 0.7, cites: [{source: S5, locator: "1921 passage"}], how_known: "Britannica (July 1921, Piano Suite op. 25)."}
    - {value: "Moses und Aron", year: 1930, kind: work, lasting: "'his greatest work, the opera Moses und Aron (begun in 1930)' (S5, body)", certainty: 0.5, cites: [{source: S5, locator: "'Evolution from tonality' (body)"}], how_known: "Britannica body sentence, seen as excerpted by search (as S5's 1921 passage); the body dates only the start, 1930. 0.5."}
  evidence_of_impact:
    - {value: "Teacher of Berg and Webern; central figure of the Second Viennese School", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works:
    - {value: "Harmonielehre", year: 1911, kind: book, certainty: 0.7, cites: [{source: S1, locator: "'First major works'"}], how_known: "Britannica."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Created atonal and twelve-tone methods (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Jewish", certainty: 0.5, cites: [{source: S1, locator: "'Early life'"}, {source: S4, locator: "p. 1–2"}], how_known: "Family in the 'then predominantly Jewish' Second District; DeVoto: no clear picture of his religious training. 0.5."}
  family_religious_practice: {value: UNKNOWN, how_known: "DeVoto: 'nor ... do we have any clear picture of his religious training as a youth'."}
  parents_and_household:
    - {value: "Samuel Schoenberg, father, shoe-shop owner (d. 1890)", role: father, certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}
    - {value: "Pauline Schoenberg (née Nachod), mother", role: mother, certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}
  household_circumstances: {value: "Small shopkeeper's family; worked as a bank clerk 1890–1895 after his father's death", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}
  schooling: []
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading:
    - {value: "Meyers Konversations-Lexikon (sonata form)", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}
  childhood_mentors:
    - {value: "Oskar Adler", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}
  languages_in_childhood: {value: ["German"], certainty: 0.5, cites: [{source: S1, locator: "'Early life'"}], how_known: "Inferred."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1899–1930", certainty: 0.5, cites: [{source: S1, locator: "'First major works'"}, {source: S5, locator: "'Evolution from tonality'"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Lutheran (baptized 1898)", certainty: 0.7, cites: [{source: S4, locator: "p. 2"}], how_known: "DeVoto."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "Nominal Lutheran over most of the span (1898–1933), readmitted to Judaism July 1933, just after it (S3). The 1912 Dehmel letter is a plan for an oratorio, not a profession. Leads JUDA (late span, Moses und Aron) and CHRIST (nominal)."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: JUDA, reason: "Lead: readmission 1933 (S3), after the span's end."}
    - {code: CHRIST, reason: "Lead: Lutheran baptism 1898; DeVoto suggests his theology did not match Christian concepts."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "Own words read (Dehmel letter 1912) concern an oratorio's hero 'finding God'; no locus stated. Libretti (Jakobsleiter, Moses und Aron) are characters' words (P42)."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30); nothing read on nature."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: UNKNOWN, how_known: "B_cause is UNKNOWN, which takes precedence (§6, P19)."}
  statements:
    - text: "For a long time I have been wanting to write an oratorio on the following subject: modern man, having passed through materialism, socialism, and anarchy and, despite having been an atheist, still having in him some residue of ancient faith (in the form of superstition), wrestles with God (see also Strindberg's 'Jacob Wrestling') and finally succeeds in finding God and becoming religious. Learning to pray!"
      cites: [{source: S2, locator: "letter 11, p. 35"}]
      date: "1912-12-13"
      context: "Letter to Richard Dehmel from Berlin-Zehlendorf, in English translation (Stein ed.)."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-19
      note: "Private letter printed after his death (Stein ed.); scan on a document-sharing site; plan for a work, read by many as autobiographical."
  changes_over_life:
    - {value: "Baptized Lutheran", year: 1898, certainty: 0.7, cites: [{source: S4, locator: "p. 2"}], how_known: "DeVoto."}
    - {value: "Readmitted to Judaism, Liberal synagogue, Paris (witnesses Marianoff and Chagall)", year: 1933, certainty: 0.7, cites: [{source: S3, locator: "full report"}], how_known: "JTA report of 25 July 1933."}
  coder_notes: "Unused own-voice leads in DeVoto (S4): the 1923 letters to Kandinsky, inside the span ('but I am a Jew'; the Jews' 'task that their God has imposed on them'), about identity rather than profession; and the 1890 letter to Malvina Goldschmied, before the span ('as an unbeliever myself'). Read these and later essays for A."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Viennese Jewish", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}, {source: S4, locator: "p. 1"}], how_known: "Britannica; DeVoto."}
  religious_heritage_by_birth: {value: "Jewish", certainty: 0.7, cites: [{source: S4, locator: "p. 2"}], how_known: "DeVoto."}
  baptism_or_initiation: {value: "Lutheran baptism 1898", certainty: 0.7, cites: [{source: S4, locator: "p. 2"}], how_known: "DeVoto."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not known (S4)."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1899–1930", certainty: 0.5, cites: [{source: S1, locator: "'First major works'"}, {source: S5, locator: "'Evolution from tonality' (body)"}], how_known: "Verklärte Nacht (1899) to Moses und Aron (P29, P30). The body gives only 'begun in 1930'; the 1930–1932 dating was in a question box (P26), which is no longer cited, so the end is 1930 at 0.5."}
  age_at_first_lasting_contribution: {value: 25, certainty: 0.7, cites: [{source: S1, locator: "Born; 'First major works'"}], how_known: "1899 − 1874 = 25 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Not scored."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Twelve-tone rows are combinatorial, not proof (S1).", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not stated."}
  circle_present: {value: "unclear", rationale: "No views scored.", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions: []
collaborators:
  - {value: "Alexander von Zemlinsky", relation: teacher, note: "harmony, counterpoint, composition", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}
  - {value: "Richard Dehmel", relation: correspondent, note: "poet of Verklärte Nacht", certainty: 0.7, cites: [{source: S2, locator: "letter 11"}], how_known: "Letters."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S6, locator: "roster.csv, rank 148"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Only own words read are an oratorio plan; the Britannica body was read only through 'First major works' plus a search excerpt on 1921."
  open_questions:
    - "Own prose on God (Kandinsky letters 1922–23; 'Composition with Twelve Tones')."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Dika Newlin"
    citation: "Newlin, Dika. \"Arnold Schoenberg.\" Encyclopaedia Britannica (updated 12 September 2026). https://www.britannica.com/biography/Arnold-Schoenberg"
    url: "https://www.britannica.com/biography/Arnold-Schoenberg"
    accessed: 2026-10-19
    reliability_note: "Signed article; body cited, question boxes flagged (P26)."
    used_for: [identity, basics, contribution, childhood, heritage, timing, lane_b, collaborators]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Arnold Schoenberg, ed. Erwin Stein"
    citation: "Schoenberg, Arnold. Letters, ed. Erwin Stein, tr. Eithne Wilkins and Ernst Kaiser (London: Faber, 1964), letter 11, p. 35; scan at https://www.yumpu.com/en/document/view/8232991/arn-ld-schoenberg-letters"
    url: "https://www.yumpu.com/en/document/view/8232991/arn-ld-schoenberg-letters"
    accessed: 2026-10-19
    reliability_note: "Printed edition via an unofficial scan; quoted identically by the Berlin Philharmonic and DeVoto."
    used_for: [worldview, collaborators]
  - id: S3
    type: secondary
    kind: other
    author: "Jewish Telegraphic Agency"
    citation: "\"Arnold Schoenberg, Composer, is Reconverted to Judaism.\" JTA Daily Bulletin, 25 July 1933. https://www.jta.org/archive/arnold-schoenberg-composer-is-reconverted-to-judaism"
    url: "https://www.jta.org/archive/arnold-schoenberg-composer-is-reconverted-to-judaism"
    accessed: 2026-10-19
    reliability_note: "Contemporary news report (it gives 1921 for his leaving Judaism, against 1898 elsewhere)."
    used_for: [worldview]
  - id: S4
    type: secondary
    kind: other
    author: "Mark DeVoto"
    citation: "DeVoto, Mark. \"Arnold Schoenberg and Judaism: The Harder Road\" (lecture, 1990). Tufts University. https://bpb-us-e1.wpmucdn.com/sites.tufts.edu/dist/6/2974/files/2015/10/Schoenberg.pdf"
    url: "https://bpb-us-e1.wpmucdn.com/sites.tufts.edu/dist/6/2974/files/2015/10/Schoenberg.pdf"
    accessed: 2026-10-19
    reliability_note: "Signed lecture by a Schoenberg scholar; full lecture read (PDF)."
    used_for: [childhood, worldview, heritage]
  - id: S5
    type: tertiary
    kind: encyclopedia
    author: "Dika Newlin"
    citation: "Newlin, Dika. \"Arnold Schoenberg\" (later body sections, as excerpted by search). Encyclopaedia Britannica. https://www.britannica.com/biography/Arnold-Schoenberg"
    url: "https://www.britannica.com/biography/Arnold-Schoenberg"
    accessed: 2026-10-19
    reliability_note: "Same article as S1; the 1921 passage was seen only in a search excerpt."
    used_for: [contribution]
  - id: S6
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [review]
---

## Summary

Arnold Schoenberg (1874–1951), composer [S1]. Draft: primary BELOW_THRESHOLD; A BELOW_THRESHOLD; B UNKNOWN. Not plotted.

## Life and work

Vienna, Berlin, Los Angeles [S1].

## Contribution and impact

Verklärte Nacht; twelve-tone method; Moses und Aron [S1].

## Childhood and education

Shopkeeper's son; self-taught with Zemlinsky [S1].

## Adult working worldview

Lutheran 1898, Jewish again 1933 [S3, S4]; oratorio plan of 1912 [S2].

## Heritage (context only)

Viennese Jewish [S1].

## Timing

1899–1930, age 25 [S1, S5].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Own prose on God.

## Research log

- 2026-10-19: Read Britannica (Newlin), JTA 1933, DeVoto excerpt, Dehmel letter.
