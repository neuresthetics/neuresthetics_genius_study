---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch D)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch D, order P32: F 5, rank 18). Basics and works from Britannica (Lockspeiser). Worldview: the 1911 Excelsior interview with Henry Malherbe, read only as quoted in English in Vallas (1933), pp. 224–225 (archive.org scan). Not a scientist. primary_system BELOW_THRESHOLD (PANT fails the two-part test); A, B, D BELOW_THRESHOLD; C, E UNKNOWN; mid_basin BELOW_THRESHOLD. Draft, not reviewed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #18, F5 rank 18). P47 source_quality on every source. Dual-sourced birth/death (S1+S2) → 1.0. French of Malherbe Excelsior interview corroborated via unofficial web reprint (S4; wording matches Vallas English; Gallica Excelsior still blocked). Added Bizet Comœdia 18 May 1911 line via Lesure Monsieur Croche p. 305 as cited secondhand (S5). Baptism 1864-07-31 and parents filled (S2+S6). A_locus stays BELOW_THRESHOLD: French keeps «près de Dieu» separate from Nature → PANT part 1 still fails; Bizet «pas … catholique ou croyant» rejects practice/belief without locating God. B_cause stays BELOW_THRESHOLD (not a scientist; beauty/spectacle language ≠ law/exception, P16). primary_system stays BELOW_THRESHOLD; AGNOS considered from Bizet, not chosen (no suspension; still speaks of God, prayer, Christian faith in the Martyre mix). Chart: still unplotted. Lockspeiser Life and Mind and Lesure full editions unread. No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: debussy-claude
  display_name: "Claude Debussy"
  roster:
    canonical_name: "Claude Debussy"
    rank: 18
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: music
    field_bucket: music
  full_name: {value: "Achille-Claude Debussy", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts ('In full')"}, {source: S2, locator: "p. 1 (childhood; Achille-Claude)"}], how_known: "Britannica + Vallas (dual-source)."}
  native_name: {value: "Achille-Claude Debussy", certainty: 0.7, cites: [{source: S2, locator: "p. 1"}], how_known: "French birth name as in Vallas; same orthography as English."}
  aliases:
    - {name: "Claude-Debussy", kind: "roster alias"}
    - {name: "Debussy-Claude", kind: "roster alias"}
    - {name: "Claude Achille Debussy", kind: "other"}

basics:
  birth:
    date: {value: "1862-08-22", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Quick Facts; opening sentence"}, {source: S2, locator: "p. 1 (22 August 1862, Saint-Germain-en-Laye)"}], how_known: "Britannica + Vallas (dual-source)."}
    place: {value: "Saint-Germain-en-Laye, France", modern_name: "Saint-Germain-en-Laye, France", polity_then: "Second French Empire", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S2, locator: "p. 1 (38 rue au Pain)"}], how_known: "Britannica + Vallas (dual-source)."}
  death:
    date: {value: "1918-03-25", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S2, locator: "p. (death; 25 March 1918)"}], how_known: "Britannica + Vallas (dual-source)."}
    place: {value: "Paris", modern_name: "Paris, France", polity_then: "French Third Republic", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S6, locator: "death; 16e / Passy"}], how_known: "Britannica + Wikipedia EN (dual-source for place)."}
  first_lasting_contribution_year: {value: 1894, certainty: 0.7, cites: [{source: S1, locator: "opening; Middle period"}], how_known: "Prélude à l'après-midi d'un faune (1894), the earliest listed lasting contribution; Britannica's year, taken as the premiere year (P30). Clair de lune is dated '1890–1905' (published within the suite later), so it is not listed as the earliest dated item."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "p. 1"}], how_known: "From 1894 (P2); birth year dual-sourced."}
  region_of_birth: {value: "Western Europe", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S2, locator: "p. 1"}], how_known: "France (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "Early and Middle period (Paris)"}], how_known: "Britannica."}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S1, locator: "text"}, {source: S2, locator: "p. 1"}], how_known: "As recorded."}
  languages_of_work: {value: [French], certainty: 0.7, cites: [{source: S1, locator: "works"}], how_known: "French titles and texts."}
  occupations: {value: ["composer", "pianist"], certainty: 0.7, cites: [{source: S1, locator: "opening; Early period"}], how_known: "Britannica."}

contribution:
  fields: {value: ["composition"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Prélude à l'après-midi d'un faune", year: 1894, kind: work, lasting: "a 'seminal force' in 20th-century music (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; Middle period"}], how_known: "Britannica."}
    - {value: "Pelléas et Mélisande (opera)", year: 1902, kind: work, lasting: "his single completed opera; standard repertory", certainty: 0.7, cites: [{source: S1, locator: "Middle period ('first performed in 1902')"}], how_known: "Britannica."}
    - {value: "La Mer", year: 1905, kind: work, lasting: "orchestral repertory", certainty: 0.7, cites: [{source: S1, locator: "opening; Middle period"}], how_known: "Britannica."}
    - {value: "Douze Préludes, 2 books", year: "1910–1913", kind: work, lasting: "piano repertory", certainty: 0.7, cites: [{source: S1, locator: "Late period"}], how_known: "Britannica."}
  evidence_of_impact:
    - {value: "Developed 'a highly original system of harmony and musical structure'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works: []
  honours:
    - {value: "Grand Prix de Rome (L'Enfant prodigue)", year: 1884, certainty: 0.7, cites: [{source: S1, locator: "Early period"}], how_known: "Britannica."}
  definition_fit: {value: "clearly meets", rationale: "Original harmonic system; seminal for 20th-century music.", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "Roman Catholic (baptized)", certainty: 0.5, cites: [{source: S2, locator: "pp. 2–3 (baptismal certificate; godparents)"}, {source: S6, locator: "baptism 31 July 1864, Église Saint-Germain"}], how_known: "Baptism in a Catholic church is recorded; household practice not described. Certainty 0.5 (heritage inference from baptism, not a family creed statement)."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father Manuel-Achille Debussy (china/pottery merchant; later various work); mother Victorine-Joséphine-Sophie Manoury", certainty: 0.7, cites: [{source: S2, locator: "pp. 1–2"}, {source: S6, locator: "Early life"}], how_known: "Vallas + Wikipedia EN."}
  household_circumstances: {value: "Born at 38 rue au Pain, Saint-Germain-en-Laye; family later in modest Paris circumstances", certainty: 0.7, cites: [{source: S1, locator: "Early period"}, {source: S2, locator: "p. 1"}], how_known: "Britannica + Vallas."}
  schooling:
    - {value: "Paris Conservatory (piano and composition)", stage: university, run_by: "state or municipal", years: "1873–", ages: "11–", certainty: 0.7, cites: [{source: S1, locator: "Early period"}], how_known: "Britannica; 'university' is the nearest stage for a conservatory. Wikipedia EN/FR give admission autumn 1872 — not dual-sourced here."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "Madame Mauté de Fleurville, associated with Chopin", certainty: 0.7, cites: [{source: S1, locator: "Early period"}], how_known: "Britannica."}
  languages_in_childhood: {value: [French], certainty: 0.7, cites: [{source: S2, locator: "p. 1"}], how_known: "French household."}
  notable_events:
    - {value: "Baptized 31 July 1864 at Église Saint-Germain, Saint-Germain-en-Laye; godfather Achille-Antoine Arosa; godmother (aunt) signed as Octavie de la Ferronnière", certainty: 0.7, cites: [{source: S2, locator: "pp. 2–3"}, {source: S6, locator: "baptism"}], how_known: "Vallas (godparents) + Wikipedia EN (date, church)."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1894–1913", certainty: 0.7, cites: [{source: S1, locator: "opening; Late period"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "(interview) French: «Je me suis fait une religion de la mystérieuse nature» / English via Vallas: 'I have made mysterious Nature my religion.' (Malherbe/Excelsior, 1911). Parallel: Bizet/Comœdia 1911 — «si je ne suis pas de pratique catholique ou croyant».", certainty: 0.5, cites: [{source: S2, locator: "p. 225"}, {source: S4, locator: "French reprint of the nature-religion paragraph"}, {source: S5, locator: "Bizet line via Lesure p. 305 citation"}], how_known: "(interview) Own words in newspaper interviews, known in French only through secondary reprints/citations and in English through Vallas translation — secondary quotation → 0.5."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "(interview) Malherbe + Bizet passages (S2, S4, S5), all secondary quotation of French or English translation.", note: "Vallas and some secondaries call the Malherbe text pantheistic, but under S6 PANT needs (1) God identified with Nature as a claim about what exists, plus (2) a further mark. French keeps God separate («plus près de Dieu» / 'nearer to God'); Nature-as-religion and prayer-as-contemplation are reverent language, not an identity claim — part 1 fails. Bizet rejects Catholic practice and being «croyant» without locating God or suspending judgment, so neither CHRIST nor clean AGNOS/ATHE. Nothing else read scores a system at plottable certainty."}
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: PANT, reason: "Vallas/'pantheistic eulogy' label; fails two-part test — God named separately from Nature (French «près de Dieu»)."}
    - {code: CHRIST, reason: "Rejected: Malherbe «Je ne pratique pas selon les rites consacrés»; Bizet «pas de pratique catholique ou croyant». Martyre attraction to «foi chrétienne» is aesthetic/subject mix, not affiliation."}
    - {code: AGNOS, reason: "Considered from Bizet «pas … croyant»; not chosen — no suspension-of-judgment language; he still speaks of God, prayer, and adoration poses."}
    - {code: ATHE, reason: "Rejected: still names God and describes prayer; not a denial of God."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, note: "(interview) French «Je ne pense pas qu'un homme revêtu d'une robe abbatiale soit plus près de Dieu» names God but does not place God (in / above / as Nature). Nature-as-religion fails PANT part 1, so cannot underwrite A=4 pantheist locus. Bizet non-croyant does not locate God either.", how_known: "(interview) BELOW_THRESHOLD under P19."}
    B_cause: {value: BELOW_THRESHOLD, note: "Not a scientist (P16). Interview praises nature's beauty and 'spectacles' as prayer; Monsieur Croche prefers sunrise to the Pastoral Symphony — aesthetic/pedagogical nature talk, not law vs exception.", how_known: "BELOW_THRESHOLD under P19."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing scored on reward or afterlife in the passages read (Martyre paradise is dramatic subject, not a ledger claim)."}
    D_authority: {value: BELOW_THRESHOLD, note: "(interview) Rejects priestly garments and sacred rites as bringing one nearer to God, but does not set revelation against observation.", how_known: "(interview) BELOW_THRESHOLD under P19."}
    E_scope: {value: UNKNOWN, how_known: "Nothing on the world's order as one/many (P7)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus and B_cause are BELOW_THRESHOLD."}
  statements:
    - text: "Je me suis fait une religion de la mystérieuse nature. Je ne pense pas qu'un homme revêtu d'une robe abbatiale soit plus près de Dieu, ni qu'un lieu dans la ville soit plus favorable à la méditation. Devant un ciel mouvant, en contemplant, de longues heures, ses beautés magnifiques et incessamment renouvelées, une incomparable émotion m'étreint. … Sentir à quels spectacles troublants et souverains la nature convie ses éphémères et tremblants passagers, voilà ce que j'appelle prier."
      cites: [{source: S4, locator: "French paragraph (nature-religion)"}, {source: S2, locator: "p. 225 (English parallel)"}]
      date: "1911-02-11"
      context: "Interview by Henry Malherbe for Excelsior, 11 February 1911, while writing Le Martyre de saint Sébastien. S4 reprints the French (misattributes venue as Comoedia January 1911); wording matches Vallas's English of the Excelsior Malherbe interview. Gallica Excelsior page not opened this pass."
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "French via S4 unofficial web reprint; English via Vallas 1933 translation (S2). Prefer French for coding. Key for PANT: «près de Dieu» keeps God distinct from Nature."
    - text: "I do not practise religion in accordance with the sacred rites. I have made mysterious Nature my religion. I do not believe that a man is any nearer to God for being clad in priestly garments, nor that one place in a town is better adapted to meditation than another."
      cites: [{source: S2, locator: "p. 225"}]
      date: "1911-02-11"
      context: "Same Malherbe/Excelsior interview; English as printed in Vallas 1933 (tr. Maire and Grace O'Brien)."
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "Kept as the English parallel to the French statement above; OCR of archive.org scan (in.ernet.dli.2015.57948), pp. 224–225."
    - text: "Je n'ai pas de profession de foi à vous faire, mais si je ne suis pas de pratique catholique ou croyant, je n'ai pas eu grand effort à faire pour m'élever à la hauteur du mysticisme qu'atteint le drame du poète."
      cites: [{source: S5, locator: "Bizet/Comœdia 1911 via Lesure Monsieur Croche p. 305 citation"}]
      date: "1911-05-18"
      context: "Interview with René Bizet, Comœdia, 18 May 1911, around the Martyre premiere. French as given in Lesure's critical edition (p. 305) and cited in later scholarly literature; Lesure volume and Gallica Comœdia not opened this pass."
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Secondary quotation of a scholarly edition → 0.5. Strengthens non-CHRIST; does not by itself score AGNOS or locate God for A."
  changes_over_life: []
  coder_notes: "Deepen 2026-10-24: French Malherbe confirms the English Vallas reading and the separate naming of God — PANT still fails. Bizet adds explicit non-practice / non-croyant without a locus claim. Gallica Excelsior and Lesure/Lockspeiser full books remain blockers. Chart stays unplotted (A and B BELOW_THRESHOLD)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "French", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Roman Catholic (baptized)", certainty: 0.5, cites: [{source: S2, locator: "pp. 2–3"}, {source: S6, locator: "baptism"}], how_known: "Baptism recorded; family creed not stated."}
  baptism_or_initiation: {value: "Baptized 1864-07-31, Église Saint-Germain, Saint-Germain-en-Laye (Catholic)", certainty: 0.7, cites: [{source: S6, locator: "baptism 31 July 1864"}, {source: S2, locator: "pp. 2–3 (baptismal certificate / godparents)"}], how_known: "Wikipedia EN date + Vallas certificate/godparents."}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1894–1913", certainty: 0.7, cites: [{source: S1, locator: "opening; Late period"}], how_known: "Prélude (1894) to Préludes book 2 (1913) (P29, P30). The Cello Sonata (1915) is named by Britannica but not listed; listing it would move the end to 1915."}
  age_at_first_lasting_contribution: {value: 32, certainty: 1.0, cites: [{source: S1, locator: "Quick Facts; opening"}, {source: S2, locator: "p. 1"}], how_known: "1894 − 1862 = 32 (P30); birth year dual-sourced."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No statement scored at 3 or 4 (P27)."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", rationale: "The nature-religion and Bizet passages are not scored at 3 or 4 on A–E.", certainty: 0.5, cites: [{source: S2, locator: "p. 225"}, {source: S4, locator: "French paragraph"}, {source: S5, locator: "Bizet line"}], how_known: "Coder's reading."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Nothing read on proof-style training.", certainty: 0.5, cites: [{source: S1, locator: "Early period"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "Early period"}], how_known: "Nothing read."}
  circle_present: {value: "partly", rationale: "(interview) Nature reflected in the soul / hands in adoration maps nature into the self, without identifying God and Nature.", certainty: 0.5, cites: [{source: S2, locator: "p. 225"}, {source: S4, locator: "French paragraph"}], how_known: "(interview) Coder's reading of secondary quotation."}
  reading: "As belief, not finding: form unclear, circle partly present."
  notes: "Lane A and Lane B kept separate (P49). No chart cue from Lane B alone."

institutions:
  - {value: "Paris Conservatory", role: student, years: "1873–1884", kind: university, certainty: 0.7, cites: [{source: S1, locator: "Early period"}], how_known: "Britannica."}
collaborators:
  - {value: "Maurice Maeterlinck", relation: collaborator, note: "librettist of Pelléas", certainty: 0.7, cites: [{source: S1, locator: "Middle period"}], how_known: "Britannica."}
  - {value: "Nadezhda von Meck", relation: "mentor or employer", note: "patron", certainty: 0.7, cites: [{source: S1, locator: "Early period"}], how_known: "Britannica."}
  - {value: "Gabriele D'Annunzio", relation: collaborator, note: "librettist/poet of Le Martyre de saint Sébastien (1911)", certainty: 0.7, cites: [{source: S1, locator: "Late period"}, {source: S6, locator: "Martyre"}], how_known: "Britannica + Wikipedia EN."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 18"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Worldview interviews known only as secondary quotation (Vallas English; web French reprint; Lesure p. 305 via later citation). Gallica Excelsior/Comœdia and Lesure/Lockspeiser full volumes not opened."
    - "S4 misattributes the Malherbe nature-religion interview to Comoedia January 1911; venue/date follow Vallas/Excelsior 11 February 1911."
  open_questions:
    - "Open Gallica Excelsior 11 February 1911 (Malherbe) and Comœdia 18 May 1911 (Bizet) for primary French — Cloudflare 403 from this network."
    - "Read Lockspeiser, Debussy: His Life and Mind, and Lesure (ed.), Monsieur Croche et autres écrits / Correspondance 1872–1918, in full."
    - "Conservatory admission year: Britannica 1873 vs Wikipedia 1872 — resolve from Lesure or Conservatoire archives."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Edward Lockspeiser"
    citation: "Lockspeiser, Edward. \"Claude Debussy.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Claude-Debussy."
    url: "https://www.britannica.com/biography/Claude-Debussy"
    accessed: 2026-10-15
    source_quality: "reference entry"
    reliability_note: "Signed encyclopedia article; the AI 'Top Questions' box was not used (P26). Re-confirmed for deepen 2026-10-24 (live fetch briefly 403; prior read stands)."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: secondary
    kind: "scholarly book"
    author: "Léon Vallas"
    year: 1933
    citation: "Vallas, Léon. Claude Debussy: His Life and Works. Translated by Maire and Grace O'Brien. London: Oxford University Press, 1933. Scan: archive.org, in.ernet.dli.2015.57948."
    url: "https://archive.org/details/in.ernet.dli.2015.57948"
    accessed: 2026-10-15
    source_quality: "scholarly edition or monograph"
    reliability_note: "Standard early biography; quotes the 1911 Malherbe interview in English translation; birth, parents, baptismal godparents, death date checked in OCR."
    used_for: [identity, basics, childhood, worldview, heritage, timing, lane_b]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    source_quality: "study roster"
    reliability_note: "Study's own roster."
    used_for: [identity, review]
  - id: S4
    type: secondary
    kind: other
    author: "4'33 magazine"
    year: 2020
    citation: "4'33 magazine. \"Debussy et la « religion de la mystérieuse nature ».\" 9 May 2020. https://www.4-33mag.com/debussy-et-la-religion-de-la-mysterieuse-nature/."
    url: "https://www.4-33mag.com/debussy-et-la-religion-de-la-mysterieuse-nature/"
    accessed: 2026-10-24
    source_quality: "unofficial web copy"
    reliability_note: "French reprint of the nature-religion paragraph; misattributes venue to Comoedia January 1911. Used only to corroborate French wording against Vallas English of the Excelsior/Malherbe interview; not treated as primary."
    used_for: [worldview, lane_b]
  - id: S5
    type: secondary
    kind: "scholarly edition"
    author: "François Lesure (ed.); interview René Bizet"
    year: 1971
    citation: "Debussy, Claude. Interview with René Bizet, Comœdia, 18 May 1911. French text in François Lesure, ed., Monsieur Croche et autres écrits (Paris: Gallimard, 1971), p. 305; wording as cited in later scholarly literature (e.g. Journal of Musicological Research 37, no. 4 [2018] abstract/synthesis)."
    url: "https://www.tandfonline.com/doi/abs/10.1080/01411896.2018.1484997"
    accessed: 2026-10-24
    source_quality: "scholarly edition or monograph"
    reliability_note: "Lesure critical edition not opened this pass; Bizet French taken from secondary citation of Lesure p. 305. Treated as secondary quotation → 0.5."
    used_for: [worldview]
  - id: S6
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia contributors. \"Claude Debussy.\" Wikipedia, The Free Encyclopedia. https://en.wikipedia.org/wiki/Claude_Debussy (and French article for baptism cross-check)."
    url: "https://en.wikipedia.org/wiki/Claude_Debussy"
    accessed: 2026-10-24
    source_quality: "other"
    reliability_note: "Used for dual-source basics (with S1/S2), baptism date, Martyre collaborator, and as a lead to Vallas/Lesure. Not used alone to score worldview axes."
    used_for: [basics, childhood, heritage, collaborators, review]
---

# Claude Debussy

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Claude Debussy (1862–1918), French composer of the Prélude à l'après-midi d'un faune (1894), Pelléas et Mélisande (1902) and La Mer (1905) [S1][S2]. In 1911 interviews he said he had made «une religion de la mystérieuse nature» and that he was not of Catholic practice or a believer, while still speaking of God and prayer [S2][S4][S5]. Draft deepen: primary_system BELOW_THRESHOLD (PANT fails part 1); A, B, D BELOW_THRESHOLD; C, E UNKNOWN; mid_basin BELOW_THRESHOLD — still unplotted.

## Life and work

Paris Conservatory from the early 1870s; Prix de Rome 1884 [S1]. Collaborations include Maeterlinck (Pelléas) and D'Annunzio (Martyre, 1911) [S1][S6].

## Contribution and impact

Faune, Pelléas, La Mer, Préludes [S1].

## Childhood and education

Born Saint-Germain-en-Laye to Manuel-Achille Debussy and Victorine Manoury; baptized Catholic 31 July 1864 [S2][S6]. Conservatory training [S1].

## Adult working worldview

Nature-as-religion (Malherbe/Excelsior, Feb 1911) and non-croyant / non-Catholic-practice (Bizet/Comœdia, May 1911), both secondary quotation at 0.5 [S2][S4][S5]. French keeps God separate from Nature («près de Dieu») — not PANT under the two-part test. Not a scientist; no law/exception claim for B [P16]. A and B remain BELOW_THRESHOLD.

## Heritage (context only)

French; baptized Roman Catholic (context only) [S1][S2][S6].

## Timing

First lasting contribution 1894, at 32 [S1][S2]. No LIO-type views scored at 3 or 4.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form unclear; circle partly (nature reflected in the soul) [S2][S4]. Kept separate from Lane A.

## Open questions

- Gallica Excelsior 11 Feb 1911 and Comœdia 18 May 1911 (primary French).
- Lockspeiser *Life and Mind*; Lesure *Monsieur Croche* / *Correspondance* in full.
- Conservatory admission 1872 vs 1873.

## Research log

- 2026-10-15: Read Britannica (Lockspeiser) and Vallas 1933 (archive.org OCR, pp. 224–225). Wikiquote used only as a lead.
- 2026-10-24: Deepen D1. Re-read Vallas OCR (birth, parents, baptismal godparents, death). French Malherbe paragraph via 4'33 magazine (S4). Bizet line via Lesure p. 305 as cited in scholarly literature (S5). Wikipedia EN/FR for baptism date and dual-source place of death. Gallica Cloudflare 403; Lockspeiser IA borrow-only / 401. Validated; person-file commit only.
