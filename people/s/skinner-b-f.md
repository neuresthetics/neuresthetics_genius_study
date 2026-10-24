---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch N)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-17
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-17, by: "Grok Bot", summary: "Record created (stage 3 batch N, order P32: F 4, rank 86). Basics from Britannica (Britannica Editors, unsigned; body only). Worldview from his signature on Humanist Manifesto II (1973), read on the American Humanist Association page (Wayback 20261006044056), whose signers pledge 'general support' 'while not necessarily endorsing every detail'. primary_system SECHUM (0.5, alt ATHE); A 4 (0.5); B 3 (0.5, alt 4; P41 and P35); C 4 (0.5); D 4 (0.5); mid_basin BELOW_THRESHOLD (A at 0.5). Plotted (faded). Draft, not reviewed."}
    - {date: 2026-10-17, by: "Grok Bot", summary: "Batch N audit fix (#15, v8's ruling on RQ2): added his own working-years text, Science and Human Behavior (1953; B.F. Skinner Foundation PDF, read directly): 'we must assume that behavior is lawful and determined' (p. 6) and 'The hypothesis that man is not free is essential to the application of scientific method to the study of human behavior' (p. 447). B 3 → 4 at 0.5, alternative 3. Timing fields now date the first LIO-type evidence to 1953, during the major work."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #85, F4 rank 86). Needs: lift A and/or B to ≥0.7 corroborated if own-voice exists; manifesto as support not sole locus. Reconcile queue 'B 3 @0.5 alt 4' with file: keep audit RQ2 value B 4 @0.5 alt 3. Own-voice: 1967 Boring–Lindzey autobiography ('I no longer believed in God'; S9 web copy of published chapter); Free Inquiry Spring 1987 'What Religion Means to Me' (S6, scientificmindfulness reprint); Beyond Freedom and Dignity 1971 (S5, IA djvu.txt + Foundation quote pages) 'Personal exemption from a complete determinism is revoked' / strip autonomous man to environment; re-checked SHB 1953 Foundation PDF (S4); SEP Behaviorism Graham 2023 (S7) aversions to free will + BFAD p.198 quote; Britannica Wayback 20261005171724 (S1, 'In full: Burrhus Frederic'); Wikipedia EN (S8, P50 dual-bio). P47 source_quality on S1–S9. A 4 @0.5 single (manifesto-only) → 4 @0.7 corroborated (S9+S6; manifesto S2 support only). B 4 @0.5 → 4 @0.7 corroborated alt 3 (S4+S5+S7). C/D 4 @0.5 → 4 @0.7 corroborated (S6+S2). E UNKNOWN. primary_system SECHUM @0.5 alt ATHE unchanged (manifesto general-support clause). mid_basin BELOW_THRESHOLD → false @0.7 (A ≥ 3 at 0.7). Chart-moving YES: faded→dark and hollow→filled. No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: skinner-b-f
  display_name: "B.F. Skinner"
  roster:
    canonical_name: "B.F. Skinner"
    rank: 86
    F: 4
    models: [Claude, DeepSeek, Gemini, GPT]
    band: "core (3–4)"
    status: core
    field: psychology
    field_bucket: "psychology / neuroscience"
  full_name: {value: "Burrhus Frederic Skinner", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts / 'In full'"}], how_known: "Britannica Quick Facts: 'In full: Burrhus Frederic Skinner'."}
  native_name: {value: UNKNOWN, how_known: "English."}
  aliases:
    - {name: "B-F-Skinner", kind: "roster alias"}

basics:
  birth:
    date: {value: "1904-03-20", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Susquehanna, Pennsylvania, U.S.", modern_name: "Susquehanna, Pennsylvania, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "1990-08-18", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Cambridge, Massachusetts", modern_name: "Cambridge, Massachusetts, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1938, certainty: 0.5, cites: [{source: S1, locator: "Minnesota sentence"}], how_known: "The Behavior of Organisms (1938), the first dated work in the body of the 'influential exponent of behaviourism' (S1). The Skinner box is undated. 1938 is the coder's pick (P13)."}
  era_bucket: {value: "1850 to 1949", certainty: 0.5, cites: [{source: S1, locator: "Minnesota sentence"}], how_known: "From 1938 (P2)."}
  region_of_birth: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "United States (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Harvard, Minnesota, Indiana."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [English], certainty: 0.7, cites: [{source: S1, locator: "titles"}], how_known: "Britannica."}
  occupations: {value: ["psychologist", "professor", "author"], certainty: 0.7, cites: [{source: S1, locator: "opening; Harvard paragraph"}], how_known: "Britannica."}

contribution:
  fields: {value: ["behaviourism", "experimental psychology"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "The Behavior of Organisms: operant behaviour and reinforcement", year: 1938, kind: theory, lasting: "'Central to his approach is the concept of reinforcement'; 'influenced a generation of psychologists' (S1)", certainty: 0.5, cites: [{source: S1, locator: "Minnesota sentence; Harvard paragraph"}], how_known: "Britannica; pairing the 1938 book with reinforcement is the coder's reading."}
    - {value: "Skinner box", year: UNKNOWN, kind: invention, lasting: "'has been adopted in pharmaceutical research' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Harvard paragraph"}], how_known: "Britannica; undated."}
    - {value: "Beyond Freedom and Dignity", year: 1971, kind: work, lasting: "'generated considerable controversy' (S1)", certainty: 0.5, cites: [{source: S1, locator: "books paragraph"}], how_known: "Britannica; lasting status is the coder's reading."}
  evidence_of_impact:
    - {value: "'influenced a generation of psychologists'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "Harvard paragraph"}], how_known: "Britannica."}
  major_works:
    - {value: "Walden Two", year: 1948, kind: book, certainty: 0.7, cites: [{source: S1, locator: "Indiana paragraph"}], how_known: "Britannica."}
    - {value: "Science and Human Behavior", year: 1953, kind: book, certainty: 0.7, cites: [{source: S1, locator: "books paragraph"}], how_known: "Britannica."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Presbyterian / Protestant Christian culture", certainty: 0.7, cites: [{source: S9, locator: "Miss Graves / Sunday School passage"}, {source: S6, locator: "opening"}], how_known: "1967 autobiography: Presbyterian Sunday School with Miss Graves; Free Inquiry: 'moderately religious culture' / Presbyterian Sunday school."}
  family_religious_practice: {value: "Presbyterian Sunday school (Pentateuch lessons); grandmother taught hell via stove coals", certainty: 0.7, cites: [{source: S9, locator: "Grandmother Skinner / Miss Graves"}], how_known: "1967 autobiography."}
  parents_and_household:
    - {value: "Father William Skinner (lawyer); mother Grace Burrhus; younger brother Edward (d. age 16)", role: parents, certainty: 0.7, cites: [{source: S9, locator: "opening family paragraphs"}, {source: S8, locator: "Early life"}], how_known: "1967 autobiography; Wikipedia."}
  household_circumstances: {value: TODO}
  schooling:
    - {value: "Harvard University (PhD 1931)", stage: university, years: "–1931", certainty: 0.7, cites: [{source: S1, locator: "Pavlov paragraph"}], how_known: "Britannica."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [English], certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1938–1971", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "Own words: 'Science, not religion, has taught me my most useful values, among them intellectual honesty' (S6); manifesto he signed: accounts of nature must pass scientific evidence (S2, general support).", certainty: 0.7, cites: [{source: S6, locator: "Science, not religion..."}, {source: S2, locator: "First"}], how_known: "Free Inquiry essay (own wording) plus manifesto signature."}
  primary_system:
    value: SECHUM
    basis: written_profession
    certainty: 0.5
    cites: [{source: S2, locator: "preface; First; signatories"}]
    rationale: "Signed Humanist Manifesto II (1973), listed as 'B. F. Skinner, Prof. of Psychology, Harvard Univ.'; AHA Humanist of the Year 1972 (S8). Manifesto: 'As nontheists, we begin with humans not God, nature not deity' / 'naturalistic humanism'. Named alternative ATHE: Free Inquiry 1987 own words reject creator / prayer / supernatural rewards (S6), and 1967 autobiography denies God (S9) — but those score A; the SECHUM label still rests on the humanist signature (manifesto 'general support' 'not every detail' → 0.5)."
    how_known: "Manifesto signature with not-every-detail clause, so 0.5. Own-voice atheism (S6, S9) strengthens alt ATHE and A, not a higher SECHUM certainty."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: SECHUM, reason: "Signed a humanist manifesto."}
    - {code: ATHE, reason: "'nontheists ... nature not deity'; the manifesto's wording on God is 'insufficient evidence', not a flat denial."}
    - {code: DETERM, reason: "His 1953 determinism (S4) is a working assumption of method about behaviour; it bears on B, not on the system code (coder's call)."}
  lio_axes:
    A_locus:
      value: 4
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S9, locator: "Miss Graves / 'I no longer believed in God'"}, {source: S6, locator: "creator / prayer / supernatural passages"}]
      rationale: "No God (P38). Own published autobiography (1967, during working years): after a brief adolescent 'Sign', 'Within a year I had gone to Miss Graves to tell her that I no longer believed in God. ... I never went through it' (S9). Free Inquiry Spring 1987 (own essay): 'what we have found is more credible than the hypothesis that the world is the handiwork of a creator'; 'I no longer believe that I can call upon a god as father'; 'Nature is marvelous but not, I think, miraculous. We began to learn more about it as soon as we stopped regarding it as the work of a god'; 'I have no fear of supernatural punishments' (S6). Manifesto (S2) 'insufficient evidence' / nontheist wording is supporting only (general-support clause) — not the sole locus."
      how_known: "Two independent own-voice publications (1967 autobiography chapter; 1987 Free Inquiry essay). No documented reverse change of view → adult evidence counts for the working-years span at normal certainty (CODING_GUIDE Changes over life). Independent source ids S9+S6 → corroborated (P48)."
    B_cause:
      value: 4
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S4, locator: "p. 6; p. 447"}, {source: S5, locator: "ch. 1 p. 21; closing 'strip away' passage (~p. 198)"}, {source: S7, locator: "§6"}]
      rationale: "Account of nature / behaviour as natural system (P6, P16, P35 scientist-of-behaviour). Audit RQ2 kept: B 4 (not queue's stale B 3). SHB 1953: 'we must assume that behavior is lawful and determined' (p. 6); 'The hypothesis that man is not free is essential...' (p. 447); drops 'free will as an inner causal agent' (p. 116). BFAD 1971 (end of major-work span) goes beyond method-only wording: 'Personal exemption from a complete determinism is revoked as a scientific analysis progresses' (ch. 1); 'it should strip away the functions previously assigned to a free or autonomous person and transfer them one by one to the controlling environment' (~p. 198). SEP: aversions to free will / dualism; quotes the strip-away sentence (S7 §6). Denies B 3's free-will exception → B 4 (P40). Named alternative 3: if SHB's 'we must assume' is read as method-only without a claim about nature (P35)."
      how_known: "Own books 1953+1971 inside/at end of working years, plus SEP. Named alternative (3) → 0.7 ceiling. Independent source ids S4+S5+S7 → corroborated (P48)."
      alternatives:
        - {value: 3, note: "If SHB's 'we must assume' is read as method-only (P35) and BFAD's 'complete determinism' is limited to behaviour-science practice rather than nature's order.", cites: [{source: S4, locator: "p. 6"}]}
    C_ledger:
      value: 4
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S6, locator: "Death / supernatural punishments"}, {source: S2, locator: "Second"}]
      rationale: "No ledger. Own words: 'I have no fear of supernatural punishments, of course nor could I enjoy an eternal life in which there would be nothing left for me to do' (S6). Manifesto he signed: 'Promises of immortal salvation or fear of eternal damnation are both illusory and harmful' (S2; general-support)."
      how_known: "Own Free Inquiry essay plus manifesto signature. Independent source ids S6+S2 → corroborated (P48)."
    D_authority:
      value: 4
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S6, locator: "Science, not religion..."}, {source: S2, locator: "First"}]
      rationale: "Science over religious dogma. Own words: 'Science, not religion, has taught me my most useful values, among them intellectual honesty. It is better to go without answers than to accept those that merely resolve puzzlement' (S6). Manifesto: 'Any account of nature should pass the tests of scientific evidence; in our judgment, the dogmas and myths of traditional religions do not do so' (S2; general-support)."
      how_known: "Own Free Inquiry essay plus manifesto. Independent source ids S6+S2 → corroborated (P48)."
    E_scope: {value: UNKNOWN, how_known: "Nothing read on the world's order as such (P7); P44(c) applies to systems, not people."}
  mid_basin: {value: false, certainty: 0.7, cites: [{source: S9, locator: "'I no longer believed in God'"}, {source: S6, locator: "creator / god as father"}], how_known: "A 4 at 0.7: the A ≥ 3 branch reads A only (P10). Deepen D1 lifted A past the 0.5 BELOW_THRESHOLD that matched pre-deepen Hawking/Beauvoir."}
  statements:
    - text: "We cannot apply the methods of science to a subject matter which is assumed to move about capriciously. Science not only describes, it predicts. [...] If we are to use the methods of science in the field of human affairs, we must assume that behavior is lawful and determined."
      cites: [{source: S4, locator: "p. 6"}]
      date: "1953"
      context: "Science and Human Behavior, ch. I, 'The threat to freedom' (S4)."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-17
      note: "Foundation PDF of the book; page number from its running head."
    - text: "The hypothesis that man is not free is essential to the application of scientific method to the study of human behavior."
      cites: [{source: S4, locator: "p. 447"}]
      date: "1953"
      context: "Science and Human Behavior, section VI, 'The problem of control' (S4)."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-17
      note: "Foundation PDF; page number from its running head."
    - text: "We find insufficient evidence for belief in the existence of a supernatural; it is either meaningless or irrelevant to the question of survival and fulfillment of the human race. As nontheists, we begin with humans not God, nature not deity. Nature may indeed be broader and deeper than we now know; any new discoveries, however, will but enlarge our knowledge of the natural."
      cites: [{source: S2, locator: "First"}]
      date: "1973"
      context: "Humanist Manifesto II (1973), signed by Skinner among others (S2)."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-17
      note: "Collective text; signers 'not necessarily endorsing every detail'."
    - text: "Promises of immortal salvation or fear of eternal damnation are both illusory and harmful."
      cites: [{source: S2, locator: "Second"}]
      date: "1973"
      context: "Same manifesto."
      axes: [C_ledger]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-17
    - text: "We, the undersigned, while not necessarily endorsing every detail of the above, pledge our general support to Humanist Manifesto II for the future of humankind."
      cites: [{source: S2, locator: "signatories"}]
      date: "1973"
      context: "Signing clause above the list that includes 'B. F. Skinner, Prof. of Psychology, Harvard Univ.'"
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-17
    - text: "Within a year I had gone to Miss Graves to tell her that I no longer believed in God. 'I know,' she said, 'I have been through that myself.' But her strategy misfired: I never went through it."
      cites: [{source: S9, locator: "end of (1904–1922) section"}]
      date: "1967"
      context: "A History of Psychology in Autobiography, Vol. 5 (Boring & Lindzey), published during working years (S9)."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Web copy of the published 1967 chapter (skeptically.org / Lafayette mirror); wording checked against Wikipedia quotation of the same chapter."
    - text: "We have yet to find many answers, but what we have found is more credible than the hypothesis that the world is the handiwork of a creator. ... I no longer believe that I can call upon a god as father (or mother). ... Nature is marvelous but not, I think, miraculous. We began to learn more about it as soon as we stopped regarding it as the work of a god. ... I have no fear of supernatural punishments, of course nor could I enjoy an eternal life in which there would be nothing left for me to do."
      cites: [{source: S6, locator: "creator / prayer / Nature / Death passages"}]
      date: "1987"
      context: "What Religion Means to Me, Free Inquiry Spring 1987 (S6). After major-work span; no documented reverse change of view from the 1967 denial."
      axes: [A_locus, C_ledger, D_authority]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Read via scientificmindfulness.com full reprint of the Free Inquiry essay; wording checked."
    - text: "Personal exemption from a complete determinism is revoked as a scientific analysis progresses, particularly in accounting for the behavior of the individual."
      cites: [{source: S5, locator: "ch. 1 (~p. 21)"}]
      date: "1971"
      context: "Beyond Freedom and Dignity, ch. 1 'A Technology of Behavior' (S5)."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "IA djvu.txt of the book; Foundation Quote of the Day page agrees (p. 21)."
    - text: "It is in the nature of an experimental analysis of human behaviour that it should strip away the functions previously assigned to autonomous man and transfer them one by one to the controlling environment."
      cites: [{source: S5, locator: "~p. 198"}, {source: S7, locator: "§6"}]
      date: "1971"
      context: "Beyond Freedom and Dignity (S5); SEP Behaviorism quotes the Knopf wording with 'free or autonomous person' (S7)."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
  changes_over_life:
    - {value: "Lost adolescent faith within a year of a 'Sign' experience; told Miss Graves he no longer believed in God and 'never went through' return to faith", year: "c. 1918–1922", certainty: 0.7, cites: [{source: S9, locator: "Miss Graves passage"}, {source: S6, locator: "I soon lost my faith"}], how_known: "Childhood/adolescence before working years; A scored on adult profession (1967, 1987), not this event alone."}
  coder_notes: "Deepen D1 (2026-10-24): manifesto kept as support, not sole A/C/D locus. Queue line 'B 3 @0.5 alt 4' was stale — file correctly had B 4 @0.5 alt 3 after audit RQ2; D1 lifts certainty to 0.7 with BFAD+SEP. Free Inquiry 1987 is after 1938–1971 span but consistent with 1967 denial (no reverse change) → counts at normal written_profession certainty. Particulars of My Life (1976) full text not re-read (1967 chapter covers the loss-of-faith episode)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "American (English paternal grandfather; Susquehanna PA family)", certainty: 0.7, cites: [{source: S9, locator: "opening family paragraphs"}, {source: S1, locator: "opening"}], how_known: "1967 autobiography: English grandfather; Britannica birthplace."}
  religious_heritage_by_birth: {value: "Presbyterian / Protestant", certainty: 0.7, cites: [{source: S9, locator: "Miss Graves Sunday School"}, {source: S6, locator: "opening"}], how_known: "Own autobiography and Free Inquiry essay."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not read."}
  childhood_catechism: {value: "Presbyterian Sunday school under Miss Graves (Old Testament / Pentateuch)", certainty: 0.7, cites: [{source: S9, locator: "Miss Graves"}, {source: S6, locator: "opening"}], how_known: "Own words."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1938–1971", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "First to last dated listed lasting contribution (P29, P30)."}
  age_at_first_lasting_contribution: {value: 34, certainty: 0.5, cites: [{source: S1, locator: "opening; 1938"}], how_known: "1938 − 1904 = 34 (P30)."}
  first_evidence_of_lio_type_views: {value: "1953: behaviour 'lawful and determined'; 'man is not free' (Science and Human Behavior)", year: 1953, certainty: 0.5, cites: [{source: S4, locator: "p. 6; p. 447"}], how_known: "Earlier writings (1938, 1948) not read for this (P30 #7)."}
  lio_views_relative_to_major_work: {value: "during major work", rationale: "1953 falls inside 1938–1971.", certainty: 0.5, cites: [{source: S4, locator: "p. 6"}], how_known: "Dates of what was read."}
  worldview_during_major_work: {value: "Determinist about behaviour (SHB 1953; BFAD 1971 complete-determinism / autonomous-man denial); atheist by published 1967 autobiography (denial since adolescence)", certainty: 0.7, cites: [{source: S4, locator: "p. 6; p. 447"}, {source: S5, locator: "ch. 1; ~p. 198"}, {source: S9, locator: "'I no longer believed in God'"}], how_known: "Own books and 1967 autobiography inside the span."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Nothing read on geometric form.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Nothing read."}
  circle_present: {value: "no", rationale: "Own denial of creator God; nature not miraculous (S6); manifesto 'nature not deity' (S2).", certainty: 0.7, cites: [{source: S6, locator: "Nature...not miraculous"}, {source: S9, locator: "'I no longer believed in God'"}], how_known: "Own words."}
  reading: "Atheist radical behaviorist; signed naturalistic humanism (SECHUM)."
  notes: "Lane B only — labeled belief model."

institutions:
  - {value: "University of Minnesota", role: "faculty", years: "1936–1945", kind: university, certainty: 0.5, cites: [{source: S1, locator: "Minnesota sentence"}], how_known: "Britannica (joined 1936; end year from the Indiana appointment)."}
  - {value: "Indiana University, Bloomington", role: "professor of psychology", years: "1945–1948", kind: university, certainty: 0.7, cites: [{source: S1, locator: "Indiana paragraph"}], how_known: "Britannica."}
  - {value: "Harvard University", role: "professor of psychology", years: "1948–1974", kind: university, certainty: 0.7, cites: [{source: S1, locator: "Harvard paragraph"}], how_known: "Britannica (emeritus 1974)."}
collaborators:
  - {value: "Ivan Pavlov", relation: "influenced by", note: "conditioned reflexes", certainty: 0.7, cites: [{source: S1, locator: "Pavlov paragraph"}], how_known: "Britannica."}
  - {value: "John B. Watson", relation: "influenced by", note: "founder of behaviourism", certainty: 0.7, cites: [{source: S1, locator: "Pavlov paragraph"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 86"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Britannica article is unsigned (Britannica Editors)."
    - "Free Inquiry 1987 essay read via third-party full reprint (scientificmindfulness.com), not the Free Inquiry page image."
    - "1967 autobiography chapter read via web mirror of the published chapter (skeptically.org), not a library PDF of Boring & Lindzey vol. 5."
    - "BFAD read via Internet Archive djvu.txt OCR plus Foundation quote pages; Knopf page images not opened."
  open_questions:
    - "Particulars of My Life (1976) full text for any nuance beyond the 1967 chapter."
    - "About Behaviorism (1974) primary for further B/E if a later deepen needs E."
    - "Free Inquiry Spring 1987 page images / DOI for archival cite."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "Britannica Editors. \"B.F. Skinner.\" Encyclopaedia Britannica. https://www.britannica.com/biography/B-F-Skinner. Read in Wayback snapshot 20261005171724 (re-opened 2026-10-24)."
    url: "https://www.britannica.com/biography/B-F-Skinner"
    accessed: 2026-10-24
    reliability_note: "Unsigned article. Body and Quick Facts ('In full: Burrhus Frederic Skinner'); Top Questions not cited for worldview."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, timing, institutions, collaborators]
  - id: S2
    type: primary
    kind: "institutional page"
    author: "American Humanist Association"
    citation: "Humanist Manifesto II (1973), with signatories. American Humanist Association. https://americanhumanist.org/what-is-humanism/manifesto2/. Read in Wayback snapshot 20261006044056 (live page returned 403)."
    url: "https://americanhumanist.org/what-is-humanism/manifesto2/"
    accessed: 2026-10-17
    reliability_note: "Copyright holder's text; signers pledge 'general support' 'while not necessarily endorsing every detail'. Treated as support, not sole locus for A/C/D after deepen D1."
    source_quality: "primary / own words"
    used_for: [worldview, timing, lane_b]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-17
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "B. F. Skinner"
    citation: "Skinner, B. F. Science and Human Behavior. New York: Macmillan, 1953. B. F. Skinner Foundation PDF (copyright 2014): https://www.bfskinner.org/wp-content/uploads/2014/02/ScienceHumanBehavior.pdf"
    url: "https://www.bfskinner.org/wp-content/uploads/2014/02/ScienceHumanBehavior.pdf"
    accessed: 2026-10-24
    reliability_note: "Foundation PDF with book page numbers in running heads; p. 6, p. 116, p. 447 re-checked D1."
    source_quality: "primary / own words"
    used_for: [worldview, timing]
  - id: S5
    type: primary
    kind: "published work by the subject"
    author: "B. F. Skinner"
    citation: "Skinner, B. F. Beyond Freedom and Dignity. New York: Knopf, 1971. Internet Archive djvu.txt: https://archive.org/stream/Beyond_Freedom_and_Dignity/Beyond%20Freedom%20%26%20Dignity%20-%20Skinner_djvu.txt ; Foundation Quote of the Day (ch. 1 quote 29, p. 21)."
    url: "https://archive.org/details/Beyond_Freedom_and_Dignity"
    accessed: 2026-10-24
    reliability_note: "OCR text of the published book plus Foundation excerpt pages; quotations checked. Pelican/IA lineation may hyphenate words."
    source_quality: "primary / own words"
    used_for: [worldview, timing, lane_b]
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "B. F. Skinner"
    citation: "Skinner, B. F. \"What Religion Means to Me.\" Free Inquiry 7, no. 2 (Spring 1987). Full text read via Brian Thompson reprint: http://www.scientificmindfulness.com/2010/03/skinner-on-religion.html"
    url: "http://www.scientificmindfulness.com/2010/03/skinner-on-religion.html"
    accessed: 2026-10-24
    reliability_note: "Third-party full reprint of the Free Inquiry essay; commenters treat it as complete. Not the magazine page image."
    source_quality: "primary / own words"
    used_for: [worldview, heritage, childhood, lane_b]
  - id: S7
    type: tertiary
    kind: encyclopedia
    author: "George Graham"
    citation: "Graham, George. \"Behaviorism.\" Stanford Encyclopedia of Philosophy (substantive revision 13 January 2023). https://plato.stanford.edu/entries/behaviorism/"
    url: "https://plato.stanford.edu/entries/behaviorism/"
    accessed: 2026-10-24
    reliability_note: "Signed SEP entry, read directly. §6 quotes BFAD on stripping the free/autonomous person; aversions to free will / dualism."
    source_quality: "reference entry"
    used_for: [worldview, lane_b]
  - id: S8
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia contributors. \"B. F. Skinner.\" Wikipedia, The Free Encyclopedia. https://en.wikipedia.org/wiki/B._F._Skinner. Dual biography with S1 Britannica under P50 (frozen roster)."
    url: "https://en.wikipedia.org/wiki/B._F._Skinner"
    accessed: 2026-10-24
    reliability_note: "P50 dual-bio. Used for parents/brother, Humanist of the Year 1972, Manifesto II signer note, and categories 'American atheists'. Quotes 1967 autobiography on atheism — A scored from S9 primary, not from this paraphrase alone."
    source_quality: "reference entry"
    used_for: [basics, heritage, childhood, review]
  - id: S9
    type: primary
    kind: "published work by the subject"
    author: "B. F. Skinner"
    citation: "Skinner, B. F. \"B. F. Skinner.\" In A History of Psychology in Autobiography, Vol. 5, edited by E. G. Boring and Gardner Lindzey, 387–413. New York: Appleton-Century-Crofts, 1967. Web copy of the chapter: http://skeptically.org/skinner/id2.html (from Lafayette early.html mirror)."
    url: "http://skeptically.org/skinner/id2.html"
    accessed: 2026-10-24
    reliability_note: "Web mirror of the published 1967 chapter (also reprinted in Dews Festschrift 1970). Miss Graves / 'I no longer believed in God' wording matches Wikipedia's quotation of the same chapter."
    source_quality: "primary / own words"
    used_for: [worldview, heritage, childhood, timing]
---

# B.F. Skinner

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

B.F. Skinner (1904–1990), American behaviourist psychologist [S1]. Deepen D1: primary_system SECHUM (0.5, alt ATHE); A 4 @0.7 corroborated; B 4 @0.7 corroborated (alt 3); C 4 @0.7 corroborated; D 4 @0.7 corroborated; E UNKNOWN; mid_basin false @0.7. Plotted (now dark filled — chart-moving).

## Life and work

Harvard PhD 1931; Minnesota, Indiana, Harvard [S1].

## Contribution and impact

The Behavior of Organisms (1938), reinforcement, the Skinner box, Walden Two (1948) [S1].

## Childhood and education

Susquehanna PA; Presbyterian Sunday school (Miss Graves); lost faith in adolescence [S9; S6]. Harvard PhD 1931 [S1].

## Adult working worldview

Atheist by own published words: 'I no longer believed in God' (1967) [S9]; Free Inquiry 1987 rejects creator / supernatural ledger [S6]. Behaviour under complete determinism / no autonomous free agent (SHB 1953; BFAD 1971) [S4; S5; S7]. Signed Humanist Manifesto II (1973) as general support [S2] — not sole A locus.

## Heritage (context only)

American; Presbyterian/Protestant upbringing [S1; S9; S6].

## Timing

First lasting contribution 1938, at 34 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No circle [S6; S9].

## Open questions

- Particulars of My Life (1976) full text; About Behaviorism (1974) for E; Free Inquiry page images.

## Research log

- 2026-10-17: Read Britannica (Wayback 20261005171724) and Humanist Manifesto II with signers (AHA, Wayback 20261006044056; live page 403); quotations checked word for word. Batch N audit added SHB 1953 (S4).
- 2026-10-24 (D1): Own-voice A from 1967 autobiography (S9) + Free Inquiry 1987 (S6); B corroborated via BFAD 1971 (S5) + SEP (S7); P47 on S1–S9; manifesto demoted to support. A/B/C/D → 0.7 corroborated; mid_basin false @0.7. Chart-moving YES (faded→dark, hollow→filled).
