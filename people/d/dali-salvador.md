---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch K)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to visual_arts. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch K, order P32: F 5, rank 71). Basics from Britannica (Britannica Editors, unsigned); Top Questions not cited. No worldview statement read; the 1950–70 religious-themed paintings are subjects, not avowed belief. primary_system UNKNOWN; A, B, C, D, E UNKNOWN; mid_basin UNKNOWN (P19). Not plotted. Draft, not reviewed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #70, F5 rank 71). Needs: A UNKNOWN; B UNKNOWN; 1 source. Dual bio: Britannica Editors via Wayback 2015 body (S1; live Cloudflare-blocked) + Wikipedia EN (S3). Primary: The Secret Life of Salvador Dalí 1942 Dial/Chevalier (S4 IA OCR) — end: 'At this moment I do not yet have faith, and I fear I shall die without heaven'; science 'windows open to heaven'; L'Age d'Or collaboration framed as fanatical sacrilege / 'excess of Catholic fanaticism' not naive anticlericalism. Mystical Manifesto 1951 (S8 OCR) — nuclear-mysticism program (post-span). Secondary: NGV Liquid Desire religion + education PDF (S5) — young Dalí shared father's aversion; 1950 'Catholic without faith'; Ateneu lecture title. Living Church Lima 2021 (S6) and Word on Fire (S7) quote Secret Life and the 1950/1970s 'I believe in God but I have no faith' line. P31: lasting contributions = Surrealist 1929–1937 (Britannica best-known window; Soft Construction 1936; Metamorphosis of Narcissus 1937); later Catholic-without-faith / nuclear mysticism in changes_over_life only — do not score axes on post-span phase. A stays UNKNOWN (anti-clerical art and secondary 'atheist' labels under threshold; own film words complicate ATHE; Picasso thin-source pattern). B stays UNKNOWN (not a scientist; Manifesto spirituality-of-substance ≠ P16 nature-order). primary_system UNKNOWN; mid_basin UNKNOWN. P47 on S1–S8. Chart-moving NO. Thin-source caution — no overclaim. No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: dali-salvador
  display_name: "Salvador Dalí"
  roster:
    canonical_name: "Salvador Dalí"
    rank: 71
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: art
    field_bucket: arts
  full_name: {value: "Salvador Felipe Jacinto Dalí y Domenech", certainty: 0.7, cites: [{source: S1, locator: "header ('In full')"}, {source: S3, locator: "lead / infobox"}], how_known: "Britannica; Wikipedia agrees on Spanish form (accent/Domènech variants)."}
  native_name: {value: UNKNOWN, how_known: "Catalan/Spanish, Latin script."}
  aliases:
    - {name: "Salvador Dali", kind: "roster alias"}

basics:
  birth:
    date: {value: "1904-05-11", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "lead"}], how_known: "Britannica and Wikipedia agree (P15)."}
    place: {value: "Figueras, Catalonia, Spain", modern_name: "Figueres, Spain", polity_then: "Kingdom of Spain", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "lead"}], how_known: "Britannica and Wikipedia."}
  death:
    date: {value: "1989-01-23", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "lead"}], how_known: "Britannica and Wikipedia."}
    place: {value: "Figueras, Spain", modern_name: "Figueres, Spain", polity_then: "Spain", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "lead"}], how_known: "Britannica and Wikipedia; last rites noted (S5)."}
  first_lasting_contribution_year: {value: 1929, certainty: 0.7, cites: [{source: S1, locator: "'Surrealism' / 1929–1937 window"}, {source: S3, locator: "Un Chien Andalou"}], how_known: "Mature Surrealist style from 1929 (S1); Un Chien andalou with Buñuel (S1/S3; S1 also dates the film 1928)."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "Birth year bucket (P2)."}
  region_of_birth: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Spain (P3)."}
  region_of_work: {value: "Southern Europe", certainty: 0.5, cites: [{source: S1, locator: "Surrealism / later career"}, {source: S3, locator: "Paris; United States 1940–48"}], how_known: "Spain and Paris for lasting Surrealist work; United States 1940–48/55 (0.5 dual region)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [Spanish, French], certainty: 0.5, cites: [{source: S1, locator: "'Early life'"}, {source: S4, locator: "published EN autobiography (translated)"}], how_known: "Catalan at home; Spanish and French for art/film world (0.5)."}
  occupations: {value: ["painter", "printmaker", "filmmaker", "writer"], certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "lead"}], how_known: "Britannica; Wikipedia; Secret Life (S4)."}
contribution:
  primary_domain: visual_arts
  fields: {value: ["painting", "film"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Un Chien andalou (with Luis Buñuel)", year: 1929, kind: work, lasting: "Surrealist film (S1; S3)", certainty: 0.7, cites: [{source: S1, locator: "Surrealism paragraph"}, {source: S3, locator: "Un Chien Andalou"}], how_known: "Dual-sourced; S1 also gives 1928."}
    - {value: "The Persistence of Memory", year: 1931, kind: work, lasting: "'Perhaps the most famous of those enigmatic images' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Surrealism paragraph"}, {source: S3, locator: "Notable works"}], how_known: "Britannica and Wikipedia."}
    - {value: "Soft Construction with Boiled Beans (Premonition of Civil War)", year: 1936, kind: work, lasting: "Major Surrealist political allegory in the 1929–37 peak window (S1; S3)", certainty: 0.7, cites: [{source: S3, locator: "Notable works (1936)"}, {source: S1, locator: "1929 to 1937 best-known Surrealist paintings"}], how_known: "Wikipedia dating; falls inside Britannica's 1929–37 window."}
    - {value: "The Metamorphosis of Narcissus", year: 1937, kind: work, lasting: "Enduring Surrealist icon under Edward James patronage (S3); closes Britannica 1929–37 window", certainty: 0.7, cites: [{source: S3, locator: "Metamorphosis of Narcissus (1937)"}, {source: S1, locator: "1929 to 1937"}], how_known: "Wikipedia; end of Britannica best-known span."}
  evidence_of_impact:
    - {value: "'the world’s best-known Surrealist artist' for paintings produced 1929–1937", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "Surrealism paragraph"}], how_known: "Britannica."}
    - {value: "Later (1950–70) religious-themed paintings 'not as highly regarded as the artist’s earlier works'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "later career paragraph"}], how_known: "Britannica — supports P31 choice of Surrealist span over nuclear-mysticism phase."}
  major_works:
    - {value: "The Persistence of Memory", year: 1931, certainty: 0.7, cites: [{source: S1, locator: "Surrealism"}, {source: S3, locator: "Notable works"}], how_known: "Dual-sourced."}
    - {value: "Soft Construction with Boiled Beans (Premonition of Civil War)", year: 1936, certainty: 0.7, cites: [{source: S3, locator: "Notable works"}], how_known: "Wikipedia."}
    - {value: "Christ of Saint John of the Cross", year: 1951, certainty: 0.7, cites: [{source: S3, locator: "Notable works"}, {source: S5, locator: "Christ in perspective / Glasgow note"}], how_known: "Post-span nuclear-mysticism period; listed for contribution context, not to extend major_work_period (P30/P31)."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Atheist father; Roman Catholic mother", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}, {source: S5, locator: "Dalí and Religion"}, {source: S3, locator: "Early life — father anti-clerical atheist"}], how_known: "Britannica; NGV; Wikipedia."}
  family_religious_practice: {value: "Father sent him to local state school to spare a Catholic education; mother's family devout Catholic", certainty: 0.7, cites: [{source: S5, locator: "Dalí and Religion opening"}], how_known: "NGV education resource."}
  parents_and_household:
    - {value: "Father Salvador Dalí Cusí, notary, anti-clerical atheist and Republican; mother Felipa Domènech Ferrés (d. 1921), Roman Catholic", role: parents, certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}, {source: S3, locator: "Early life"}], how_known: "Britannica; Wikipedia."}
  household_circumstances: {value: "An elder brother, also named Salvador, died nine months before his birth; sister Ana María born 1908", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}, {source: S3, locator: "Early life"}], how_known: "Britannica; Wikipedia."}
  schooling:
    - {value: "Local state school (father avoiding Catholic education)", stage: "elementary school", run_by: "state or municipal", certainty: 0.7, cites: [{source: S5, locator: "Dalí and Religion"}], how_known: "NGV."}
    - {value: "Real Academia de Bellas Artes de San Fernando, Madrid (from c. 1921)", stage: "other", run_by: "state or municipal", certainty: 0.5, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica; art academy (0.5)."}
  early_mathematics: {value: UNKNOWN, how_known: "Not read; later amateur interest in physics/math is adult (S7, S8)."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not read as childhood training."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [Catalan], certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}
  notable_events:
    - {value: "Death of his mother", year: 1921, certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}, {source: S7, locator: "mother's death"}], how_known: "Britannica; Word on Fire."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1929–1937", certainty: 0.7, cites: [{source: S1, locator: "1929 to 1937 best-known Surrealist paintings"}, {source: S3, locator: "Persistence 1931; Soft Construction 1936; Metamorphosis 1937"}], how_known: "Equals timing.major_work_period (P30). Britannica: paintings that made him the world's best-known Surrealist artist were produced 1929–1937; later religious canvases less highly regarded (S1)."}
  nominal_affiliations:
    - {value: "Paris Surrealist group (joined 1929; expelled late 1930s — artistic/political, not a scored metaphysical system)", certainty: 0.7, cites: [{source: S1, locator: "Surrealism / expulsion"}, {source: S3, locator: "Surrealist group; Politics and religion"}], how_known: "Britannica and Wikipedia."}
  self_described_science_religion_relation: {value: "Post-span (1942+): special sciences do not deny religion — 'windows open to heaven' (S4); nuclear mysticism fuses Catholic mysticism with quantum/atomic physics (S7, S8). Not a during-span science–religion profession.", certainty: 0.5, cites: [{source: S4, locator: "closing pages (~pp. 399–400 Dial 1942)"}, {source: S8, locator: "Mystical Manifesto 1951"}, {source: S7, locator: "Nuclear Mystic"}], how_known: "Own words after the Surrealist peak; kept out of A/B scoring for 1929–1937 (P31)."}
  primary_system: {value: UNKNOWN, how_known: "No scorable adult profession during 1929–1937. Checked and rejected as scored codes: (1) ATHE — Word on Fire secondary 'identified as an atheist' (S7) and NGV 'shared his father's aversion' (S5) are under 0.5 and about clergy/Catholic education more than God-locus; Secret Life own account of L'Age d'Or wants 'authentic sacrilege' / 'excess of Catholic fanaticism' not 'naive anticlericalism' (S4) — complicates a clean ATHE reading. (2) CHRIST — baptism/heritage only for the span; 1950 'Catholic without faith' and Secret Life 1942 return-to-Catholicism language are post-span (P31). Religious paintings 1950–70 are subjects (create-pass rule; S1)."}
  secondary_system: {value: UNKNOWN, how_known: "None scored for the working span."}
  candidate_codes_considered:
    - {code: ATHE, reason: "Lead only from secondary 'atheist' / shared-father-aversion labels (S5, S7) and Surrealist anti-clerical films/drawings. Own Secret Life film account (S4) and thinness → not scored as primary. Named alt if a during-span own-word disbelief of God appears: ATHE / A 4."}
    - {code: CHRIST, reason: "Rejected as working code for 1929–1937. Baptism/first communion = heritage (S3). Post-span 'Catholic without faith' (S5) and nuclear mysticism (S7, S8) belong in changes_over_life, not the Surrealist axes."}
    - {code: AGNOS, reason: "Wikipedia later-years 'Catholic and an agnostic' (S3) and the 1950/1970s 'believe in God but I have no faith' paradox (S5, S6, S7) are post-span; not used to score the Surrealist unit."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "No during-span own-word locus of the divine at ≥0.5 (P19). Checked off-point: (1) Un Chien andalou / L'Age d'Or and 1929 Sacred Heart drawing — anti-clerical/blasphemous art and provocation, not a profession of disbelief (S5; Picasso pattern); Secret Life even frames the film as fanatical sacrilege rather than naive anticlericalism (S4). (2) Secondary 'identified as an atheist' (S7) / shared father's aversion (S5) — scholarly reconstruction under 0.5; aversion is to Catholic education/clergy. (3) Secret Life 1942 'I do not yet have faith' and 1950 'I believe in God but I have no faith' (S4, S5, S6, S7) are after the Surrealist peak (P31) — recorded in statements/changes_over_life, not scored on the working-years axis. Named alternative if a Surrealist-period own-word denial of God appears: A 4."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30/P33). No statement of his own on nature's causal order during 1929–1937 (P16). Soft watches / paranoiac-critical method are art process. Post-span Mystical Manifesto 'spirituality of all substance' / quantum dematerialization (S8) and Anti-Matter 'My father today is Dr. Heisenberg' are about mysticism/physics-as-inspiration, not exceptionless natural law — and fall after the lasting-contribution span."}
    C_ledger: {value: UNKNOWN, how_known: "Not read for the working span."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read (P7)."}
  mid_basin: {value: UNKNOWN, how_known: "A and B UNKNOWN (P19)."}
  statements:
    - text: "At this moment I do not yet have faith, and I fear I shall die without heaven."
      cites: [{source: S4, locator: "closing page after 'THE END' (Dial Press 1942; Hampton Manor)"}, {source: S6, locator: "quotes Secret Life 1942"}]
      date: "1942"
      context: "Final sentence of The Secret Life of Salvador Dalí, after affirming that the special sciences' temple has 'windows open to heaven' and that heaven is in the bosom of the man who has faith."
      axes: [A_locus]
      kind: "autobiography"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Published autobiography (written_profession ceiling available) but post-dates major_work_period 1929–1937 — P31: do not score working-years A from this. Documents the 1942 'return' as still without faith. Living Church (S6) corroborates the wording."
    - text: "One thing is certain: nothing, absolutely nothing, in the philosophic, esthetic, morphological, biological or moral discoveries of our epoch denies religion. On the contrary, the architecture of the temple of the special sciences has all its windows open to heaven."
      cites: [{source: S4, locator: "closing pages (~p. 400 Dial 1942)"}, {source: S7, locator: "quotes Secret Life"}]
      date: "1942"
      context: "Secret Life epilogue: after claiming to have studied the special sciences since 1929; announces seeking heaven / Gala as reality."
      axes: []
      kind: "autobiography"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Science–religion relation (post-span). Not an A locus denial or affirmation of God; not B (no nature-causal claim)."
    - text: "No, no! No comedy. I like all this business of the archbishops; in fact, I like it enormously. Let's have a few blasphematory scenes, if you will, but it must be done with the utmost fanaticism to achieve the grandeur of a true and authentic sacrilege!"
      cites: [{source: S4, locator: "L'Age d'Or collaboration chapter (Dial 1942 OCR)"}]
      date: "1942"
      context: "Retrospective account of collaborating with Buñuel on L'Age d'Or; Dalí contrasts his desired fanatical sacrilege with Buñuel's 'elementary anti-clericalism' / later calls the finished film 'crudely anticlerical' and 'subversive rather through excess of Catholic fanaticism than through naive anticlericalism.'"
      axes: [A_locus]
      kind: "autobiography"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Own words about Surrealist-period film practice — undercuts coding A 4 / ATHE from the films alone. Blasphemy as aesthetic/fanatical gesture, not a scored disbelief profession."
    - text: "I believe in God, but I have no faith. Mathematics and Science tell me that God must exist, but I don't believe it."
      cites: [{source: S5, locator: "NGV PDF epigraph / Ateneu 1950 lecture context"}, {source: S7, locator: "quotes 1950 Barcelona lecture"}, {source: S6, locator: "1970s parallel wording"}]
      date: "1950"
      context: "NGV and Word on Fire attribute the line to the 1950 Ateneu Barcelona lecture 'Why I was Sacrilegious. Why I Am a Mystic' (and/or Dalí Dimension DVD); Living Church gives a close 1970s parallel. Post-span nuclear-mysticism phase."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "P43/secondary quotation of lecture — not checked against a primary transcript this pass. Post-span (P31). Paradoxical 'believe… but don't believe' — would at most be AGNOS/CHRIST tension at 0.5 if the later phase were the coding unit; not used to score 1929–1937 A."
    - text: "Ever since the theory of relativity substituted the substratum of the universe for the ether… since the explosive equivalence of mass-energy — all those who think, apart from the Marxist inertia, know that it is up to the metaphysicians to work precisely on the question of matter. … matter is in a constant and accelerated process of dematerialization, of disintegration, slipping out of the hands of scientists and thus proving to us the spirituality of all substance."
      cites: [{source: S8, locator: "Mystical Manifesto (1951), Collected Writings OCR pp. 364–365"}]
      date: "1951-04-15"
      context: "Mystical Manifesto, Neuilly, 15 April 1951 — program for mystical painting after Surrealism."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Post-span. Spirituality-of-substance / anti-materialism — not a P16 statement of exceptionless natural law; do not score B. Soft-watches allusion is autobiographical art history, not B."
  changes_over_life:
    - {value: "Surrealist years: anti-clerical films and blasphemous Sacred Heart drawing (1929–30); youth identified as communist/anti-clerical (S3). Own Secret Life account stresses fanatical sacrilege over naive anticlericalism (S4).", year: "1929–1937", certainty: 0.7, cites: [{source: S5, locator: "films and Sacred Heart"}, {source: S3, locator: "Politics and religion — youth anti-clerical"}, {source: S4, locator: "L'Age d'Or collaboration"}], how_known: "NGV, Wikipedia, Secret Life."}
    - {value: "1940s United States: Secret Life (1942) announces seeking heaven / Catholicism of love for Gala while still 'I do not yet have faith'; science windows open to heaven (S4). Shift from Surrealist provocation toward classicism and religion.", year: 1942, certainty: 0.7, cites: [{source: S4, locator: "closing pages"}, {source: S5, locator: "attitude began shifting in America in the 1940s"}, {source: S6, locator: "Secret Life return to Catholicism"}], how_known: "Primary autobiography; NGV; Living Church."}
    - {value: "1949 audience with Pius XII; 1950 announces himself 'Catholic without faith'; Ateneu lecture 'Why I was Sacrilegious. Why I Am a Mystic'; nuclear mysticism and Mystical Manifesto 1951. Later years: Wikipedia 'Catholic and an agnostic'; 1970s repeat of believe-God-no-faith line. Died with last rites 1989.", year: "1949–1989", certainty: 0.7, cites: [{source: S5, locator: "Catholic without faith; last rites"}, {source: S3, locator: "return to Catholic faith; Catholic and an agnostic"}, {source: S7, locator: "1950 lecture quotation"}, {source: S8, locator: "Mystical Manifesto"}], how_known: "NGV, Wikipedia, Word on Fire, Manifesto. Post-span — not the coding unit (P31; S1 rates later religious paintings below Surrealist peak)."}
  coder_notes: "Deepen D1 2026-10-24 (queue #70): Thin prior source count (1). Do not score A 4 or primary ATHE from Surrealist blasphemy or secondary atheist labels — Secret Life own film words cut the other way. Do not score later 'Catholic without faith' / 'I believe in God but I have no faith' on the Surrealist axes (P31). B permanently likely UNKNOWN unless a nature-causal profession appears. Chart-moving NO. No fallacy_catalog (Jason)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Catalan", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}, {source: S3, locator: "Figueres / Catalonia"}], how_known: "Britannica; Wikipedia."}
  religious_heritage_by_birth: {value: "Catholic mother, atheist father", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}, {source: S5, locator: "Dalí and Religion"}], how_known: "Britannica; NGV."}
  baptism_or_initiation: {value: "Baptized at Church of Sant Pere, Figueres (also first communion and funeral site)", certainty: 0.7, cites: [{source: S3, locator: "Sant Pere caption / baptism"}, {source: S7, locator: "baptized in the Church of Sant Pere"}], how_known: "Wikipedia; Word on Fire."}
  childhood_catechism: {value: UNKNOWN, how_known: "Father avoided Catholic schooling (S5); Christian Brothers winter-evening memory appears in Living Church via Secret Life (S6) — not enough to code formal catechism."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1929–1937", certainty: 0.7, cites: [{source: S1, locator: "1929 to 1937"}, {source: S3, locator: "Persistence 1931; Soft Construction 1936; Metamorphosis 1937"}], how_known: "First to last dated lasting Surrealist contribution in the Britannica best-known window (P29, P30). Christ of St John of the Cross (1951) not used to extend the span — S1 rates later religious work lower; P31 phase with most lasting contributions = Surrealism."}
  age_at_first_lasting_contribution: {value: 25, certainty: 0.7, cites: [{source: S1, locator: "opening; Surrealism"}, {source: S3, locator: "lead"}], how_known: "1929 − 1904 = 25 (P30); birth year dual-sourced."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No LIO-type view scored at ≥0.5 for the working span. 1942 Secret Life faith/heaven language and 1950 lecture are post-span and not scored."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S4, locator: "closing pages"}, {source: S5, locator: "Catholic without faith"}], how_known: "Nothing LIO-type at ≥0.5 during 1929–1937; later statements recorded but not scored on axes."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Axes UNKNOWN for 1929–1937; Surrealist anti-clerical practice documented without a scorable A/B profession."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Meticulous realist technique inside dream juxtapositions; later nuclear-mysticism uses classical geometry — pictorial, not a worldview circle claim.", certainty: 0.5, cites: [{source: S1, locator: "Surrealism paragraph"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "academy / Surrealism"}], how_known: "Art-academy training; no mathematics-to-form path read for the Surrealist span."}
  circle_present: {value: "no", rationale: "No lawful-order-of-nature belief statement in the working span; post-span Manifesto spirituality-of-substance is mysticism, not H1 circle.", certainty: 0.5, cites: [{source: S8, locator: "spirituality of all substance"}], how_known: "Coder's reading."}
  reading: "Lane B only: no H1 circle from Surrealist worldview. Soft watches / paranoiac-critical ≠ Lane A B_cause."
  notes: "Do not treat melting clocks or nuclear-mysticism geometry as evidence for A/B scores."

institutions: []
collaborators:
  - {value: "Luis Buñuel", relation: collaborator, certainty: 0.7, cites: [{source: S1, locator: "Surrealism"}, {source: S4, locator: "Chien Andalou / L'Age d'Or chapters"}], how_known: "Two films."}
  - {value: "Gala (Elena Ivanovna Diakonova)", relation: other, certainty: 0.7, cites: [{source: S1, locator: "later career"}, {source: S4, locator: "Gala passages"}], how_known: "Wife/muse; Secret Life addresses her as 'reality'."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 71"}], how_known: "Study roster."}
  controversies:
    - {value: "Adult religion: Surrealist anti-clerical provocateur vs later 'Catholic without faith' / nuclear mystic. Sincerity of the Catholic turn long disputed (Living Church summarizes Protestant skepticism vs Catholic willingness to place him in a mystical tradition). Axes left UNKNOWN for the Surrealist coding unit.", certainty: 0.5, cites: [{source: S6, locator: "Paradise: Opposition"}, {source: S5, locator: "Catholic without faith"}, {source: S3, locator: "Catholic and an agnostic"}], how_known: "Secondary debate; not resolved by scoring."}
  data_quality_flags:
    - "Secret Life and Mystical Manifesto read as archive OCR only (page images not viewed)."
    - "1950 Ateneu lecture and 1970s 'believe in God but no faith' line via secondary quotation (S5–S7); primary lecture transcript unread."
    - "Thin create-pass source count; do not overclaim A/B."
  open_questions:
    - "Primary transcript or contemporary print of the 19 Oct 1950 Ateneu lecture 'Why I was Sacrilegious. Why I Am a Mystic'."
    - "Secret Life Dial Press 1942 page images (IA borrow often 401) to replace OCR for the faith/heaven closing."
    - "During-span (1929–1937) own-word letter or interview denying or affirming God — would reopen A."
    - "Elliott King / Descharnes scholarly pages on nuclear mysticism for any P16-grade nature statement (unlikely to move Surrealist-span B)."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "Britannica Editors. \"Salvador Dalí.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Salvador-Dali. Surrealism 1929–1937 body and later-career judgment also checked via Wayback Machine snapshot 2015-09-05."
    url: "https://www.britannica.com/biography/Salvador-Dali"
    archive_url: "https://web.archive.org/web/20150905102646/http://www.britannica.com/biography/Salvador-Dali"
    accessed: 2026-10-24
    reliability_note: "Unsigned editors' body. Live fetch Cloudflare-blocked; 1929–37 / later-career wording from Wayback 20150905102646. Top Questions not cited."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, collaborators, review]
  - id: S2
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S3
    type: secondary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia contributors. \"Salvador Dalí.\" Wikipedia. https://en.wikipedia.org/wiki/Salvador_Dal%C3%AD."
    url: "https://en.wikipedia.org/wiki/Salvador_Dal%C3%AD"
    accessed: 2026-10-24
    reliability_note: "P50 dual bio with Britannica. Used for dating Soft Construction / Metamorphosis, Sant Pere baptism, Politics and religion (youth anti-clerical; later Catholic and agnostic). Not sole warrant for worldview scores."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, collaborators, review]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "Dalí, Salvador"
    year: 1942
    citation: "Dalí, Salvador. The Secret Life of Salvador Dalí. Translated by Haakon M. Chevalier. New York: Dial Press, 1942. Read via Internet Archive OCR (in.ernet.dli.2015.76092)."
    url: "https://archive.org/details/in.ernet.dli.2015.76092"
    accessed: 2026-10-24
    reliability_note: "Primary published autobiography. Verified as archive OCR only this pass (page images not viewed); OCR typos normalized in quotation where obvious."
    source_quality: "primary / own words"
    used_for: [worldview, timing, collaborators, review]
  - id: S5
    type: secondary
    kind: "institutional page"
    author: "National Gallery of Victoria"
    citation: "National Gallery of Victoria. \"Dalí and Religion.\" Salvador Dalí: Liquid Desire exhibition education pages, and \"Dalí and Religion\" education PDF. https://www.ngv.vic.gov.au/dali/salvador/religion.html ; https://www.ngv.vic.gov.au/dali/salvador/resources/DaliandReligion.pdf."
    url: "https://www.ngv.vic.gov.au/dali/salvador/religion.html"
    accessed: 2026-10-24
    reliability_note: "Museum education resource for the Liquid Desire exhibition. Strong on chronology of anti-clerical Surrealism → Catholic without faith; epigraph quotes the believe-God-no-faith line (DVD / lecture)."
    source_quality: "scholarly reconstruction"
    used_for: [childhood, worldview, heritage, contribution, review]
  - id: S6
    type: secondary
    kind: "journal article"
    author: "Lima, Ben"
    year: 2021
    citation: "Lima, Ben. \"Dalí and the Psychology of Sin.\" The Living Church, 11 January 2021. https://livingchurch.org/church-life/dali-and-the-psychology-of-sin/."
    url: "https://livingchurch.org/church-life/dali-and-the-psychology-of-sin/"
    accessed: 2026-10-24
    reliability_note: "Art-historian review essay; useful secondary quotation of Secret Life faith line and 1970s believe-God-no-faith parallel; summarizes critical debate on sincerity of the Catholic turn."
    source_quality: "scholarly reconstruction"
    used_for: [worldview, review]
  - id: S7
    type: secondary
    kind: other
    author: "Word on Fire"
    citation: "Word on Fire. \"Salvador Dalí, the Nuclear Mystic.\" https://www.wordonfire.org/articles/salvador-dali-the-nuclear-mystic/."
    url: "https://www.wordonfire.org/articles/salvador-dali-the-nuclear-mystic/"
    accessed: 2026-10-24
    reliability_note: "Popular Catholic essay; cites Secret Life windows-open passage and 1950 lecture 'I believe in God, but I have no faith.' Secondary 'identified as an atheist' for Surrealist period used only as thin lead, not as scored A."
    source_quality: "scholarly reconstruction"
    used_for: [worldview, childhood, heritage, review]
  - id: S8
    type: primary
    kind: "published work by the subject"
    author: "Dalí, Salvador"
    year: 1951
    citation: "Dalí, Salvador. \"Mystical Manifesto\" (Manifeste mystique). Paris: Robert J. Godet, 1951. English text read from Collected Writings OCR (anthology pages headed Mystical Manifesto; dated Neuilly 15 April 1951)."
    url: "https://digginganddeepening.com/texts/ESSAYS/S_Dali/1951_Mystical%20Manifesto.pdf"
    accessed: 2026-10-24
    reliability_note: "Primary 1951 manifesto; this pass via OCR of a 4-page anthology PDF (tesseract), not the 1951 Godet printing. Post-span nuclear-mysticism program."
    source_quality: "primary / own words"
    used_for: [worldview, review]
---

# Salvador Dalí

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Salvador Dalí (1904–1989), Spanish Surrealist painter and filmmaker [S1, S3]. Deepen D1: lasting contributions in the Britannica 1929–1937 Surrealist window [S1]; Soft Construction (1936) and Metamorphosis of Narcissus (1937) added [S3]. Primary Secret Life (1942) and Mystical Manifesto (1951) read [S4, S8]. Working-years A UNKNOWN; B UNKNOWN; primary_system UNKNOWN; mid_basin UNKNOWN. Later 'Catholic without faith' / nuclear mysticism documented in changes_over_life only (P31). Not plotted. Chart-moving no.

## Life and work

Figueres; Madrid academy; Paris Surrealists; United States 1940–48/55; return to Catalonia [S1, S3]. Best-known Surrealist paintings 1929–1937 [S1]. Expulsion from Surrealists late 1930s; later classicism and religious subjects [S1, S3].

## Contribution and impact

Un Chien andalou (1929); The Persistence of Memory (1931); Soft Construction with Boiled Beans (1936); The Metamorphosis of Narcissus (1937) [S1, S3]. Britannica: later 1950–70 religious paintings not as highly regarded as the earlier Surrealist work [S1].

## Childhood and education

Atheist, anti-clerical father; Catholic mother; state school to avoid Catholic education [S1, S5, S3]. Baptized at Sant Pere, Figueres [S3, S7]. Mother died 1921 [S1, S7].

## Adult working worldview

Coding unit = Surrealist peak 1929–1937 [S1]. No scorable A or B own-word locus in that span. Anti-clerical films and the 1929 Sacred Heart drawing are provocation/subjects, not disbelief professions [S5]; Secret Life retrospectively wants 'authentic sacrilege' / 'excess of Catholic fanaticism' rather than naive anticlericalism for L'Age d'Or [S4]. Secondary 'identified as an atheist' [S7] left under threshold.

Post-span (not scored on axes): Secret Life closes 'At this moment I do not yet have faith, and I fear I shall die without heaven' and says the special sciences have 'windows open to heaven' [S4]. 1950: 'Catholic without faith'; 'I believe in God, but I have no faith…' [S5, S7, S6]. Mystical Manifesto 1951: spirituality of substance / quantum mysticism [S8]. Wikipedia later years: 'Catholic and an agnostic' [S3]. Died with last rites [S5].

## Heritage (context only)

Catalan; Catholic mother / atheist father; Sant Pere baptism [S1, S3, S5, S7].

## Timing

First lasting contribution 1929, at 25 [S1, S3]. Major work period 1929–1937 [S1, S3]. LIO-type views relative to major work: none found at ≥0.5 [S4, S5].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No H1 circle from Surrealist worldview. Soft watches and nuclear-mysticism geometry ≠ A/B [S1, S8].

## Open questions

- Primary Ateneu 1950 lecture transcript.
- Secret Life page images (replace OCR).
- During-span own-word God denial/affirmation.

## Research log

- 2026-10-15: Read Britannica (Editors) full body.
- 2026-10-24: Deepen D1. Wayback Britannica Surrealism body; Wikipedia dual bio; Secret Life IA OCR; NGV religion page + PDF; Living Church; Word on Fire Nuclear Mystic; Mystical Manifesto OCR. No fallacy_catalog (Jason).
