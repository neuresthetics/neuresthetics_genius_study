---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z4)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to 20c_early. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen D1 (queue #143): opened DeVoto full PDF (S4) for in-span Kandinsky letters (Stein Letters pp. 88–93 via DeVoto quotation); Style and Idea 'Composition with Twelve Tones' ch.1 web transcription (S7, 1941 UCLA lecture); ASC reconversion draft 12 Aug 1933 (S8, German). Added statements: Kandinsky 20 Apr 1923 ('I am a Jew' — ethnic identity under antisemitism, not JUDA locus profession); Kandinsky 4 May 1923 ('task that their God has imposed on them' — third-person about Jewry, not first-person profession); Composition with Twelve Tones Divine Model / 'Lord said Let there be Light' (post-span artistic metaphor, after 1933 JUDA return); Aug 1933 reconversion note (Religionswechsel only for religious and national cause — clear own-voice but after coded span). Goldschmied 1890 'unbeliever' remains pre-span. P42: Moses und Aron / Jakobsleiter libretti still do not code the person. primary stays BELOW_THRESHOLD (leads JUDA from 1933 after span; CHRIST nominal); A stays BELOW_THRESHOLD; B UNKNOWN (P30 not scientist); mid UNKNOWN; not plotted. P47 source_quality on all sources. Style and Idea full Stein volume IA borrow-restricted this pass. No figures/; no fallacy_catalog."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z8 audit fix (RQ-Z8-1, v8's call on the auditor's advice): premise corrected. The Dance around the Golden Calf from Moses und Aron premiered in Darmstadt on 2 July 1951 (Scherchen; Schott, Universal Edition), but an excerpt premiere dates only the excerpt, so the work's year and the span end stay UNKNOWN. coder_note added: dated 1951, the span would include the 1933 return to Judaism. Values unchanged."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z7 audit fix (WEAKEN): 'begun in 1930' is a composition start, not a P30 #1 dating event. Moses und Aron was neither staged nor published in his lifetime (unfinished; he died 1951) [premise corrected at Z8: an excerpt premiered in 1951]; item year and span end set to UNKNOWN (Al-Ghazali precedent). Span 1899–1930 -> UNKNOWN (starts 1899)."}
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
  era_bucket: 20c_early
  fields: {value: ["music composition", "music theory"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Verklärte Nacht", year: 1899, kind: work, lasting: "'one of Schoenberg's most-popular compositions' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'First major works'"}], how_known: "Britannica."}
    - {value: "Method of composition with twelve tones", year: 1921, kind: method, lasting: "serialism and the 12-tone row (S1)", certainty: 0.7, cites: [{source: S5, locator: "1921 passage"}], how_known: "Britannica (July 1921, Piano Suite op. 25)."}
    - {value: "Moses und Aron", year: UNKNOWN, kind: work, lasting: "'his greatest work, the opera Moses und Aron (begun in 1930)' (S5, body)", certainty: 0.5, cites: [{source: S5, locator: "'Evolution from tonality' (body)"}], how_known: "Only an excerpt premiered in his lifetime: the Dance around the Golden Calf, Darmstadt, 2 July 1951 (Hermann Scherchen; Schott work page, Universal Edition chronology). An excerpt premiere dates only the excerpt, not the whole work (RQ-Z8-1), so the work's year stays UNKNOWN. Britannica body sentence, seen as excerpted by search (as S5's 1921 passage). 'Begun in 1930' is a composition start, not a P30 #1 dating event; unfinished and not staged or published in his lifetime, so the year is UNKNOWN (Z7 audit). 0.5."}
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
  working_years: {value: UNKNOWN, how_known: "Equals timing.major_work_period (end UNKNOWN)."}
  nominal_affiliations:
    - {value: "Lutheran (baptized 1898)", certainty: 0.7, cites: [{source: S4, locator: "p. 2"}], how_known: "DeVoto."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "Nominal Lutheran over most of the coded span; readmitted to Judaism July 1933, just after it (S3). In-span own voice: Dehmel 1912 is an oratorio plan (P42-adjacent); Kandinsky 1923 affirms Jewish identity under antisemitism, not a JUDA locus/cause profession; May 1923 'their God' is third-person about Jewry. Clear religious own-voice for the return (S8, Aug 1933) and Style and Idea Divine Model (S7, 1941) fall after the coded span. Leads JUDA (1933+) and CHRIST (nominal)."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: JUDA, reason: "Lead: readmission July 1933 (S3) and Aug 1933 own-voice that a Religionswechsel may have only religious and national cause (S8) — both after the coded span end; in-span Kandinsky identity talk does not by itself code JUDA."}
    - {code: CHRIST, reason: "Lead: Lutheran baptism 1898; DeVoto suggests his theology did not match Christian concepts."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "No clear own-voice locus profession inside the coded span. Dehmel 1912 is an oratorio plan; Kandinsky 1923 is ethnic identity / collective 'their God', not 'my God' or a locus doctrine; Moses und Aron / Jakobsleiter are characters' words (P42). Post-span S7 Divine Model and S8 reconversion note do not lift the coded A."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30); nothing read on nature."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: UNKNOWN, how_known: "B_cause is UNKNOWN, which takes precedence (§6, P19)."}
  statements:
    - text: "For a long time I have been wanting to write an oratorio on the following subject: modern man, having passed through materialism, socialism, and anarchy and, despite having been an atheist, still having in him some residue of ancient faith (in the form of superstition), wrestles with God (see also Strindberg's 'Jacob Wrestling') and finally succeeds in finding God and becoming religious. Learning to pray!"
      cites: [{source: S2, locator: "letter 11, p. 35"}, {source: S4, locator: "p. 2–3 (quotes Stein)"}]
      date: "1912-12-13"
      context: "Letter to Richard Dehmel from Berlin-Zehlendorf, in English translation (Stein ed.)."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Private letter printed after his death (Stein ed.); plan for a work's hero, not a first-person profession. Deepen: wording matched in DeVoto (S4)."
    - text: "For I have at last learned the lesson that has been forced upon me during this year, and I shall not ever forget it. It is that I am not a German, not a European, indeed perhaps scarcely even a human being (at least, the Europeans prefer the worst of their race to me), but I am a Jew. I am content that it should be so!"
      cites: [{source: S2, locator: "pp. 88–89 (Stein ed., per DeVoto n.3)"}, {source: S4, locator: "p. 4"}]
      date: "1923-04-20"
      context: "Letter to Wassily Kandinsky declining Bauhaus involvement after reports of antisemitism there; inside the coded span."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Ethnic/peoplehood identity under antisemitism, not a religious locus profession (does not by itself code JUDA). Stein Letters not opened this pass (IA borrow-restricted); quotation from DeVoto citing Stein."
    - text: "...they will not be able to exterminate those much tougher elements thanks to whose endurance Jewry has maintained itself unaided against the whole of mankind for 20 centuries. For these are evidently so constituted that they can accomplish the task that their God has imposed on them: to survive in exile, uncorrupted and unbroken, until the hour of salvation comes!"
      cites: [{source: S2, locator: "pp. 89–93 (Stein ed., per DeVoto n.4)"}, {source: S4, locator: "p. 5"}]
      date: "1923-05-04"
      context: "Second letter to Kandinsky; inside the coded span."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Third-person about Jewry ('their God'), not 'my God' / first-person profession. Identity and peoplehood under threat; does not lift A. Same verification path as the April letter."
    - text: "To understand the very nature of creation one must acknowledge that there was no light before the Lord said: 'Let there be Light.' And since there was not yet light, the Lord's omniscience embraced a vision of it which only His omnipotence could call forth. [...] In fact, the concept of creator and creation should be formed in harmony with the Divine Model; inspiration and perfection, wish and fulfillment, will and accomplishment coincide spontaneously and simultaneously."
      cites: [{source: S7, locator: "Composition with Twelve Tones, ch. 1 (opening)"}]
      date: "1941"
      context: "Style and Idea essay / UCLA lecture 'Composition with Twelve Tones' (1); after the coded span and after the July 1933 return to Judaism."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Artistic creation metaphor (Divine Model vs human composer), not a clear CHRIST or JUDA locus profession for the coded span. Post-span; does not lift coded A."
    - text: "Ein Religionswechsel darf nur religiösen und nationalen Anlass haben. Es wäre schmählich, mit diesem Schritt eine Nebenabsicht zu verbinden."
      cites: [{source: S8, locator: "T56.02 / Rekonversion, 12.VIII.1933"}]
      date: "1933-08-12"
      context: "Draft reply rejecting the claim that his Paris readmission to Judaism was only a protest gesture against Nazi persecution; after the coded span."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Own-voice: a change of religion may have only a religious and national cause. Clear for the 1933 return, but after the coded span end (RQ-Z8-1). English sense from ASC transcription page."
  changes_over_life:
    - {value: "Baptized Lutheran", year: 1898, certainty: 0.7, cites: [{source: S4, locator: "p. 2"}], how_known: "DeVoto."}
    - {value: "Readmitted to Judaism, Liberal synagogue, Paris (witnesses Marianoff and Chagall); own-voice draft 12 Aug 1933: Religionswechsel only for religious and national cause (S8)", year: 1933, certainty: 0.7, cites: [{source: S3, locator: "full report"}, {source: S8, locator: "T56.02"}], how_known: "JTA 25 July 1933; ASC reconversion draft."}
  coder_notes: "RQ-Z8-1 stands: if Moses und Aron or another lasting work were dated after July 1933 (e.g. by the 1951 Darmstadt excerpt premiere — rejected at Z8 for dating only the excerpt), the JUDA readmission and S8 own-voice would fall inside the span and primary_system could change. Deepen D1 read the unused DeVoto leads: Kandinsky 1923 = identity, not profession; Goldschmied 1890 'unbeliever' is pre-span. Style and Idea full Stein/UC Press volume was IA borrow-restricted; opened the 1941 Composition with Twelve Tones opening via ASC/Belmont web (S7) — post-span Divine Model metaphor. Post-span also: Two Speeches on the Jewish Situation (1934–35), Israel Academy letter (DeVoto n.8 / Stein pp. 286–287) with Mosaic monotheism language. P42 unchanged for libretti. Not a scientist (P30) → B UNKNOWN."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Viennese Jewish", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}, {source: S4, locator: "p. 1"}], how_known: "Britannica; DeVoto."}
  religious_heritage_by_birth: {value: "Jewish", certainty: 0.7, cites: [{source: S4, locator: "p. 2"}], how_known: "DeVoto."}
  baptism_or_initiation: {value: "Lutheran baptism 1898", certainty: 0.7, cites: [{source: S4, locator: "p. 2"}], how_known: "DeVoto."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not known (S4)."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: UNKNOWN, how_known: "Starts with Verklärte Nacht (1899); the latest lasting work, Moses und Aron, has no dating event for the whole work in his lifetime (begun 1930, unfinished; only the Golden Calf excerpt premiered, Darmstadt 1951, which dates the excerpt alone, RQ-Z8-1; P30 #1), so the end is UNKNOWN (P29; Al-Ghazali precedent; Z7 audit)."}
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
  - {value: "Wassily Kandinsky", relation: correspondent, note: "1923 letters on Jewish identity and Bauhaus antisemitism", certainty: 0.7, cites: [{source: S4, locator: "p. 4–5"}], how_known: "DeVoto quoting Stein Letters."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S6, locator: "roster.csv, rank 148"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Stein Letters and Style and Idea full volumes were IA borrow-restricted this pass; Kandinsky quotes rest on DeVoto's secondary quotation of Stein (P21)."
    - "Span end UNKNOWN (Moses und Aron); coded worldview still rests on a span ending before July 1933 (RQ-Z8-1)."
  open_questions:
    - "Primary check of Stein Letters pp. 88–93 against an open scan."
    - "In-span Style and Idea essays (e.g. Relationship to the Text 1912; Mahler 1912) if a full volume opens."
    - "Dating event for Moses und Aron that would pull July 1933 inside the span (RQ-Z8-1)."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Dika Newlin"
    citation: "Newlin, Dika. \"Arnold Schoenberg.\" Encyclopaedia Britannica (updated 12 September 2026). https://www.britannica.com/biography/Arnold-Schoenberg"
    url: "https://www.britannica.com/biography/Arnold-Schoenberg"
    accessed: 2026-10-19
    reliability_note: "Signed article; body cited, question boxes flagged (P26)."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, heritage, timing, lane_b, collaborators]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Arnold Schoenberg, ed. Erwin Stein"
    citation: "Schoenberg, Arnold. Letters, ed. Erwin Stein, tr. Eithne Wilkins and Ernst Kaiser (London: Faber, 1964), letter 11, p. 35; scan at https://www.yumpu.com/en/document/view/8232991/arn-ld-schoenberg-letters"
    url: "https://www.yumpu.com/en/document/view/8232991/arn-ld-schoenberg-letters"
    accessed: 2026-10-19
    reliability_note: "Printed edition via an unofficial scan; quoted identically by the Berlin Philharmonic and DeVoto. Full Stein volume not re-opened this pass (IA borrow-restricted)."
    source_quality: "unofficial web copy"
    used_for: [worldview, collaborators]
  - id: S3
    type: secondary
    kind: other
    author: "Jewish Telegraphic Agency"
    citation: "\"Arnold Schoenberg, Composer, is Reconverted to Judaism.\" JTA Daily Bulletin, 25 July 1933. https://www.jta.org/archive/arnold-schoenberg-composer-is-reconverted-to-judaism"
    url: "https://www.jta.org/archive/arnold-schoenberg-composer-is-reconverted-to-judaism"
    accessed: 2026-10-19
    reliability_note: "Contemporary news report (it gives 1921 for his leaving Judaism, against 1898 elsewhere)."
    source_quality: "other"
    used_for: [worldview]
  - id: S4
    type: secondary
    kind: other
    author: "Mark DeVoto"
    citation: "DeVoto, Mark. \"Arnold Schoenberg and Judaism: The Harder Road\" (lecture, 1990). Tufts University. https://bpb-us-e1.wpmucdn.com/sites.tufts.edu/dist/6/2974/files/2015/10/Schoenberg.pdf"
    url: "https://bpb-us-e1.wpmucdn.com/sites.tufts.edu/dist/6/2974/files/2015/10/Schoenberg.pdf"
    accessed: 2026-10-24
    reliability_note: "Signed lecture by a Schoenberg scholar; full lecture PDF read this deepen (quotes Stein Letters for Kandinsky 1923)."
    source_quality: "scholarly edition or monograph"
    used_for: [childhood, worldview, heritage, collaborators]
  - id: S5
    type: tertiary
    kind: encyclopedia
    author: "Dika Newlin"
    citation: "Newlin, Dika. \"Arnold Schoenberg\" (later body sections, as excerpted by search). Encyclopaedia Britannica. https://www.britannica.com/biography/Arnold-Schoenberg"
    url: "https://www.britannica.com/biography/Arnold-Schoenberg"
    accessed: 2026-10-19
    reliability_note: "Same article as S1; the 1921 passage was seen only in a search excerpt."
    source_quality: "reference entry"
    used_for: [contribution]
  - id: S6
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [review]
  - id: S7
    type: primary
    kind: "published work by the subject"
    author: "Arnold Schoenberg"
    citation: 'Schoenberg, Arnold. "Composition with Twelve Tones" (1) (1941 UCLA lecture), in Style and Idea; web transcription ch. 1 at https://eas.schoenbergmusic.com/composition-with-twelve-tones/schoenberg-12-tone-lecture/chapter-1/ (Arnold Schönberg Center & Belmont Music Publishers).'
    url: "https://eas.schoenbergmusic.com/composition-with-twelve-tones/schoenberg-12-tone-lecture/chapter-1/"
    accessed: 2026-10-24
    reliability_note: "Estate/center web transcription of a Style and Idea essay; full Stein volume IA borrow-restricted this pass."
    source_quality: "unofficial web copy"
    used_for: [worldview]
  - id: S8
    type: primary
    kind: "published work by the subject"
    author: "Arnold Schoenberg"
    citation: "Schoenberg, Arnold. Rekonversion draft (T56.02), 12 August 1933. Arnold Schönberg Center writings transcription https://archive.schoenberg.at/writings/transcription.php?action=view&id_transcription=2193 (URN at-asc-T021935)."
    url: "https://archive.schoenberg.at/writings/transcription.php?action=view&id_transcription=2193"
    accessed: 2026-10-24
    reliability_note: "ASC transcription of Schoenberg's German draft reply; live page timed out this pass — German text taken from ASC search/catalog excerpt and matched to the published first line."
    source_quality: "unofficial web copy"
    used_for: [worldview]
---

## Summary

Arnold Schoenberg (1874–1951), composer [S1]. Deepen D1: primary BELOW_THRESHOLD; A BELOW_THRESHOLD; B UNKNOWN. Not plotted.

## Life and work

Vienna, Berlin, Los Angeles [S1].

## Contribution and impact

Verklärte Nacht; twelve-tone method; Moses und Aron [S1].

## Childhood and education

Shopkeeper's son; self-taught with Zemlinsky [S1].

## Adult working worldview

Lutheran 1898, Jewish again 1933 [S3, S4, S8]. In-span own voice: Dehmel oratorio plan 1912 [S2]; Kandinsky identity letters 1923 [S2/S4] — not locus professions. Post-span: Style and Idea Divine Model 1941 [S7]; reconversion note Aug 1933 [S8]. Libretti under P42.

## Heritage (context only)

Viennese Jewish [S1].

## Timing

From 1899 (end UNKNOWN), age 25 [S1, S5].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Primary Stein Letters check for Kandinsky 1923.
- In-span Style and Idea essays if a full volume opens.
- RQ-Z8-1 dating that would bring July 1933 inside the span.

## Research log

- 2026-10-19: Read Britannica (Newlin), JTA 1933, DeVoto excerpt, Dehmel letter.
- 2026-10-24: Deepen D1 — full DeVoto PDF; Kandinsky 1923 via DeVoto/Stein; Composition with Twelve Tones ch.1 (ASC/Belmont web); ASC reconversion draft 12 Aug 1933; Style and Idea IA borrow-restricted. Codes unchanged.
