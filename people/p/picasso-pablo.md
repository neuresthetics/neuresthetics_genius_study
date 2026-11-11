---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch J)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to 20c_early. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch J, order P32: F 5, rank 64). Basics from Britannica (McCully), signed body through 1903 (the fetch returned only that part). No worldview statement read. primary_system UNKNOWN; A, B, C, D, E UNKNOWN; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Audit fixes (fallacy_catalog audit of 81b9098, run 1). mid_basin BELOW_THRESHOLD -> UNKNOWN (P19)."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #63, F5 rank 64). Needs: A UNKNOWN; B UNKNOWN; 1 source. Bio/dating: Britannica McCully via Wayback 2015 full body (S1) + Wikipedia EN (S3) — Demoiselles 1907, Analytical Cubism with Braque 1909–12, Guernica 1937; span 1901–1937. Worldview: Gilot Life with Picasso 1964 p.50 God-as-artist (S4; P43 memoir; QI page-check) — style metaphor, not A locus. Zervos 1935 via Chipp/Wikiquote (S5) — 'instrument of nature' / 'cannot go against nature' = art process, not B (P16). Richardson NYRB 1987 (S6): Jacqueline 'Pablo always claims he is not a believer' (reported speech). Wikipedia/Cox Tate secondary 'atheist' label (S3). primary_system BELOW_THRESHOLD (leads ATHE); A BELOW_THRESHOLD (alt 4); B UNKNOWN; C/D/E UNKNOWN; mid_basin BELOW_THRESHOLD. P47 on S1–S6. Chart-moving NO. No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: picasso-pablo
  display_name: "Pablo Picasso"
  roster:
    canonical_name: "Pablo Picasso"
    rank: 64
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: art
    field_bucket: arts
  full_name: {value: "Pablo Diego José Francisco de Paula Juan Nepomuceno Crispín Crispiniano María Remedios de la Santísima Trinidad Ruiz Picasso", certainty: 0.7, cites: [{source: S1, locator: "header ('In full')"}, {source: S3, locator: "Early life — baptism note"}], how_known: "Britannica; Wikipedia baptism record (Crispín/Cipriano and name order variants)."}
  native_name: {value: UNKNOWN, how_known: "Spanish, Latin script."}
  aliases:
    - {name: "Pablo Ruiz", kind: "birth name"}
    - {name: "Pablo Ruiz Picasso", kind: "other"}

basics:
  birth:
    date: {value: "1881-10-25", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "infobox / lead"}], how_known: "Britannica and Wikipedia agree (P15)."}
    place: {value: "Málaga, Spain", modern_name: "Málaga, Spain", polity_then: "Kingdom of Spain", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "lead"}], how_known: "Britannica and Wikipedia."}
  death:
    date: {value: "1973-04-08", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "lead"}], how_known: "Britannica and Wikipedia."}
    place: {value: "Mougins, France", modern_name: "Mougins, France", polity_then: "France", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "lead"}], how_known: "Britannica and Wikipedia."}
  first_lasting_contribution_year: {value: 1901, certainty: 0.7, cites: [{source: S1, locator: "'Blue Period' (1901–mid-1904)"}, {source: S3, locator: "Blue Period"}], how_known: "Blue Period dated from 1901 in Britannica and Wikipedia (P13); Cubism/Demoiselles later."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S1, locator: "'Blue Period'"}], how_known: "From 1901 (P2)."}
  region_of_birth: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Spain is Southern Europe in regions.csv (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "opening ('Spanish expatriate'); Cubism / Paris paragraphs"}, {source: S3, locator: "Career in France"}], how_known: "Main lasting work in France (Paris); dual-sourced."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [Spanish, French], certainty: 0.5, cites: [{source: S1, locator: "'Early years' (Catalan; Spanish)"}, {source: S3, locator: "Career in France"}], how_known: "Coder's reading (0.5); Spanish native; long Paris career implies French; Catalan learned (S1)."}
  occupations: {value: ["painter", "sculptor", "printmaker", "ceramicist", "stage designer"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
contribution:
  era_bucket: 20c_early
  fields: {value: ["painting", "sculpture"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Blue Period paintings", year: 1901, kind: work, lasting: "(S1; S3)", certainty: 0.7, cites: [{source: S1, locator: "'Blue Period'"}, {source: S3, locator: "Blue Period"}], how_known: "1901–mid-1904; dual-sourced."}
    - {value: "Les Demoiselles d'Avignon", year: 1907, kind: work, lasting: "cornerstone toward Cubism (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Les Demoiselles d'Avignon' (1907)"}, {source: S3, locator: "Les Demoiselles d'Avignon"}], how_known: "Britannica: begun late 1906, dated 1907; Wikipedia agrees."}
    - {value: "Cubism (with Georges Braque)", year: 1909, kind: theory, lasting: "(S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; Analytical Cubism 1909–12"}, {source: S3, locator: "Cubism"}], how_known: "Britannica: worked with Braque 1909–12 developing Analytical Cubism; creator with Braque (opening)."}
    - {value: "Guernica", year: 1937, kind: work, lasting: "major anti-fascist mural (S1)", certainty: 0.7, cites: [{source: S1, locator: "Guernica paragraph"}, {source: S3, locator: "Guernica"}], how_known: "Britannica: commissioned for 1937 Spanish pavilion; Wikipedia agrees."}
  evidence_of_impact:
    - {value: "'one of the greatest and most-influential artists of the 20th century'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works:
    - {value: "Les Demoiselles d'Avignon", year: 1907, certainty: 0.7, cites: [{source: S1, locator: "'Les Demoiselles d'Avignon'"}, {source: S3, locator: "Notable works"}], how_known: "Britannica; Wikipedia."}
    - {value: "Guernica", year: 1937, certainty: 0.7, cites: [{source: S1, locator: "Guernica paragraph"}, {source: S3, locator: "Notable works"}], how_known: "Britannica; Wikipedia."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Roman Catholic (nominal heritage)", certainty: 0.5, cites: [{source: S3, locator: "efn: baptised a Catholic"}, {source: S6, locator: "family piety / uncle canon paragraph"}], how_known: "Baptized Catholic (S3); Richardson notes clerical uncles and Sacred Heart student work — family Catholic milieu, not adult belief (0.5)."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not read beyond baptism and Richardson's family-piety sketch."}
  parents_and_household:
    - {value: "Father José Ruiz Blasco, professor of drawing; mother Maria Picasso López", role: parents, certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}, {source: S3, locator: "Early life"}], how_known: "Britannica; Wikipedia."}
  household_circumstances: {value: "Moved A Coruña 1891; Barcelona autumn 1895; father taught drawing and supported early exhibition at 13", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  schooling:
    - {value: "Father's pupil in A Coruña (drawing)", stage: other, run_by: other, years: "c. 1891–1895", ages: "c. 10–14", certainty: 0.5, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica; years the coder's reading (0.5)."}
    - {value: "La Llotja art academy, Barcelona", stage: "grammar or secondary school", run_by: other, years: "1895–1897", ages: "14–16", certainty: 0.5, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica; stage and end year the coder's reading (0.5)."}
    - {value: "Royal Academy of San Fernando, Madrid", stage: other, run_by: other, years: "1897", ages: "16", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica; he found the teaching stupid and spent time in the Prado."}
  early_mathematics: {value: UNKNOWN, how_known: "Not read."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Cubism is later adult work, not childhood training."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "José Ruiz Blasco (father)", role: "drawing teacher", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  languages_in_childhood: {value: [Spanish], certainty: 0.5, cites: [{source: S1, locator: "'Early years'"}], how_known: "Coder's reading; later Catalan (S1)."}
  notable_events:
    - {value: "Science and Charity awarded honourable mention, Madrid Fine Arts Exhibition 1897", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
    - {value: "Illness 1898; convalescence Horta de Ebro with Manuel Pallarès; break with academic path on return 1899", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1901–1937", certainty: 0.7, cites: [{source: S1, locator: "'Blue Period'; Demoiselles; Analytical Cubism; Guernica"}, {source: S3, locator: "Blue Period; Cubism; Guernica"}], how_known: "Equals timing.major_work_period (P30). First dated lasting Blue Period 1901 through Guernica 1937; later ceramics/late work not used to extend the span this pass."}
  nominal_affiliations:
    - {value: "French Communist Party (joined after WWII; politics, not metaphysics)", certainty: 0.7, cites: [{source: S1, locator: "World War II and after — joined the Communist Party"}, {source: S3, locator: "French Communist Party"}], how_known: "Britannica and Wikipedia; not coded as primary_system."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "No first-person profession of ATHE naturalism or of CHRIST in the sources read. Leads ATHE: Jacqueline reported that he 'always claims he is not a believer' (S6); Wikipedia/Cox Tate secondary labels him 'atheist' (S3). Gilot God-as-artist (S4) is a style metaphor, not a creed. Bare atheism without a nature statement would leave B open (systems/ATHE.md). CHRIST rejected as working code (anti-clerical reported speech; no confessional adult profession)."}
  secondary_system: {value: UNKNOWN, how_known: "None scored."}
  candidate_codes_considered:
    - {code: ATHE, reason: "Lead: secondary 'atheist' (S3/Cox); Jacqueline 'not a believer' (S6). No own-hand denial of God or naturalism statement — not scored as primary."}
    - {code: CHRIST, reason: "Rejected as adult working code: baptized Catholic (heritage only); Richardson notes residual Catholic imagery/obsession, not belief."}
    - {code: AGNOS, reason: "Lead only if 'not a believer' is read as suspension; no explicit agnostic profession read."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "Bearing evidence under 0.5 (P19): (1) Jacqueline reported speech that he 'always claims he is not a believer' (S6) — reported speech, not his hand; (2) secondary scholarly 'atheist' labels (S3 citing Cox Tate p.124) without first-person disbelief; (3) Gilot P43 memoir God-as-artist (S4) treats God as a metaphor for stylistic variety, not a locus claim. Named alternative if stronger own words of disbelief appear: A 4. Do not overclaim ATHEISM/A4 from thin sources."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30/P33). No statement of his own on nature's causal order (P16). Zervos 1935 'man is the instrument of nature' / 'You cannot go against nature' (S5) is about painting process and form, not physical law or miracles — same pattern as Michelangelo 'natura' poems."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read (P7)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD, so the P4 test cannot be applied; B is UNKNOWN."}
  statements:
    - text: "God is really only another artist. He invented the giraffe, the elephant, and the cat. He has no real style. He just keeps on trying other things."
      cites: [{source: S4, locator: "Part I, p. 50 (McGraw-Hill 1964; QI verified scans)"}, {source: S3, locator: "not used — Wikiquote/TIME parallel only"}]
      date: "1964"
      context: "Gilot memoir: Picasso comparing a sculptor's shifting styles to God's variety of animals (Vollard Suite / album of prints). After much of the working span."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "P43 (interview/memoir book; Gilot+Lake claim total recall in foreword — still disputed-wording class like Craft). QI 2019 page-checks p.50. Style metaphor — not used to score A (does not deny or locate God). TIME/Atlantic 1964 parallel wording not treated as independent primary."
    - text: "Whether he wants it or not, man is the instrument of nature; she imposes on him character and appearance. … You cannot go against nature. She is stronger than the strongest of men. We can permit ourselves some liberties, but in details only."
      cites: [{source: S5, locator: "Zervos Conversation 1935 / Chipp 1968 pp. 266–273; Wikiquote 'Conversations avec Picasso' (Boisgeloup, winter 1934)"}]
      date: "1935"
      context: "Zervos Cahiers d'Art interview on abstract vs figurative painting — 'instrument of nature' in the art-making sense."
      axes: [B_cause]
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Primary Cahiers d'Art / Barr / Chipp pages unread this pass (IA/library blocked). Art-process claim — not scored for B under P16."
    - text: "They make everything, from God to a picture, in their own image."
      cites: [{source: S5, locator: "Zervos / Futurism Ottinger quotation (Boisgeloup, winter 1934)"}]
      date: "1935"
      context: "Same Zervos conversation: viewers cut art to their ignorance; God mentioned as analogy for projection, not theology."
      axes: []
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Context only; not an A statement."
    - text: "Pablo always claims he is not a believer… but if you ask me, he is more Catholic than the Pope."
      cites: [{source: S6, locator: "NYRB 23 Apr 1987 — Jacqueline Picasso reported speech"}]
      date: "1987"
      context: "Richardson on Picasso's resentful obsession with Catholic imagery vs claimed unbelief."
      axes: [A_locus]
      kind: "reported speech"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Jacqueline's report of Pablo's claim — reported speech (P8/P19). Supports BELOW_THRESHOLD on A, not a scored 4. Her 'more Catholic than the Pope' is her opinion, not his profession."
  changes_over_life:
    - {value: "Baptized Roman Catholic; adult self-description as unbeliever reported (Jacqueline); joined French Communist Party after WWII (political, not worldview code)", year: "post-1944", certainty: 0.5, cites: [{source: S3, locator: "baptism efn; French Communist Party"}, {source: S6, locator: "not a believer"}, {source: S1, locator: "joined the Communist Party"}], how_known: "Heritage vs adult reported unbelief; politics separate from A/B."}
  coder_notes: "Deepen D1 2026-10-24 (queue #63): Thin prior source count — do not score A 4 or primary ATHE from secondary 'atheist' labels or Gilot metaphor. P43 on Gilot; Zervos nature quotes ≠ B (P16). Chart-moving NO (A BELOW_THRESHOLD, B UNKNOWN). No fallacy_catalog (Jason)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Andalusian / Spanish (paternal Ruiz; maternal Picasso with Ligurian surname origin noted)", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "Early life — surname"}], how_known: "Britannica Andalusian/Málaga; Wikipedia surname note."}
  religious_heritage_by_birth: {value: "Roman Catholic", certainty: 0.7, cites: [{source: S3, locator: "efn: Though baptised a Catholic…"}], how_known: "Wikipedia baptism note; dual with name from baptismal record."}
  baptism_or_initiation: {value: "Baptized Roman Catholic (baptismal name record)", certainty: 0.7, cites: [{source: S3, locator: "Early life — baptism name"}], how_known: "Wikipedia cites baptism record for full name."}
  childhood_catechism: {value: UNKNOWN, how_known: "Richardson (S6) notes student Sacred Heart altar projects under his father — not enough to code catechism practice."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1901–1937", certainty: 0.7, cites: [{source: S1, locator: "Blue Period; Demoiselles; Cubism; Guernica"}, {source: S3, locator: "same spans"}], how_known: "First to last dated listed lasting contribution (P29, P30): Blue Period 1901 through Guernica 1937."}
  age_at_first_lasting_contribution: {value: 20, certainty: 0.7, cites: [{source: S1, locator: "opening; Blue Period"}, {source: S3, locator: "lead / Blue Period"}], how_known: "1901 − 1881 = 20 (P30); birth year dual-sourced."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No LIO-type view scored; A is BELOW_THRESHOLD only."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S4, locator: "p. 50"}, {source: S6, locator: "not a believer"}], how_known: "Nothing LIO-type at ≥0.5."}
  worldview_during_major_work: {value: "BELOW_THRESHOLD (leads ATHE / reported unbelief); no scored system during 1901–1937", certainty: 0.5, cites: [{source: S6, locator: "not a believer"}, {source: S3, locator: "atheist efn"}], how_known: "Same thin evidence as primary_system; Gilot and Jacqueline reports post-date much of Cubism."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "Cubism fractures form into geometric planes (Analytical Cubism); pictorial geometry, not a worldview circle claim.", certainty: 0.7, cites: [{source: S1, locator: "Analytical Cubism paragraph"}], how_known: "Coder's reading of Britannica's Cubism account."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "Cubism"}], how_known: "No mathematics training read; form from painting practice."}
  circle_present: {value: "no", rationale: "No lawful-order-of-nature belief statement; Zervos nature language is art process (S5).", certainty: 0.5, cites: [{source: S5, locator: "instrument of nature"}], how_known: "Coder's reading."}
  reading: "Lane B only: Cubist geometric form in the work; no H1 circle. Lane A worldview stays BELOW_THRESHOLD / B UNKNOWN."
  notes: "Do not treat Cubist geometry as evidence for A/B scores."

institutions:
  []
collaborators:
  - {value: "Georges Braque", relation: collaborator, certainty: 0.7, cites: [{source: S1, locator: "opening; Analytical Cubism 1909–12"}], how_known: "Britannica."}
  - {value: "Françoise Gilot", relation: other, certainty: 0.7, cites: [{source: S1, locator: "World War II and after"}, {source: S4, locator: "memoir"}], how_known: "Partner/memoirist 1943–53; source of S4, not a collaborative lasting work."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 64"}], how_known: "Study roster."}
  controversies:
    - {value: "Adult religion: secondary sources call him atheist (Cox Tate via S3); Jacqueline reports he claimed unbelief while remaining 'more Catholic than the Pope' in her view (S6). No first-person 'I am an atheist' found this pass — left BELOW_THRESHOLD.", certainty: 0.5, cites: [{source: S3, locator: "atheist efn / Cox p.124"}, {source: S6, locator: "not a believer"}], how_known: "Disagreement is about strength of evidence, not about Cubism."}
  data_quality_flags:
    - "Thin worldview primary: Gilot P43; Zervos via secondary quotation; no letters/autobiography on God read."
  open_questions:
    - "Own-hand letter or published profession of atheism / disbelief (to raise A above BELOW_THRESHOLD or score ATHE)."
    - "Full Chipp/Barr pages of Zervos 1935 for any nature-causal remark beyond art process (unlikely B)."
    - "Dillenberger & Handley The Religious Art of Pablo Picasso (UC Press) — scholarly 'avowed atheist' framing; page-check."
    - "Cox An Interview with Pablo Picasso / NCR 'I hate the Catholic Church' wording — institutional hostility vs A locus."
    - "Parmelin / Brassai interview books under P43."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Marilyn McCully"
    citation: "McCully, Marilyn. \"Pablo Picasso.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Pablo-Picasso. Full article body also checked via Wayback Machine snapshot 2015-08-21 (Analytical Cubism, Demoiselles, Guernica)."
    url: "https://www.britannica.com/biography/Pablo-Picasso"
    accessed: 2026-10-24
    reliability_note: "Signed McCully article. Live fetch often Cloudflare-blocked; Cubism/Guernica dating from Wayback 20150821232830 full body. Top Questions not cited."
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
    year: 2026
    citation: "Wikipedia contributors. \"Pablo Picasso.\" Wikipedia, The Free Encyclopedia. https://en.wikipedia.org/wiki/Pablo_Picasso. Dual-source bio (P50); atheism efn cites Neil Cox, The Picasso Book (Tate Publishing, 2010), p. 124."
    url: "https://en.wikipedia.org/wiki/Pablo_Picasso"
    accessed: 2026-10-24
    reliability_note: "Used for baptism, dates, Communist Party, and Cox secondary 'atheist' label only — not for A/B scores. Cox monograph itself unread."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, review]
  - id: S4
    type: primary
    kind: "other"
    author: "Françoise Gilot and Carlton Lake (reporting Pablo Picasso)"
    year: 1964
    citation: "Gilot, Françoise, and Carlton Lake. Life with Picasso. New York: McGraw-Hill, 1964. Part I, p. 50 (God-as-artist). Attribution and page verified via Quote Investigator (26 May 2019; scans). Full OCR borrow blocked this pass."
    url: "https://quoteinvestigator.com/2019/05/26/giraffe/"
    accessed: 2026-10-24
    reliability_note: "P43: memoir of conversations; Lake foreword claims total recall — still interview-book class, cap 0.5 if scored. Used as statement record only; not used to score A."
    source_quality: "primary / own words"
    used_for: [worldview, collaborators, review]
  - id: S5
    type: primary
    kind: "other"
    author: "Pablo Picasso (interviewed by Christian Zervos)"
    year: 1935
    citation: "Zervos, Christian. \"Conversation avec Picasso.\" Cahiers d'Art 10, nos. 7–10 (1935): 173–178. English in Alfred H. Barr, Jr., Picasso: Fifty Years of His Art (1946) and Herschel B. Chipp, Theories of Modern Art (1968), pp. 266–273. Quotations here via English Wikiquote 'Pablo Picasso' (Zervos / Futurism Ottinger)."
    url: "https://en.wikiquote.org/wiki/Pablo_Picasso"
    accessed: 2026-10-24
    reliability_note: "Primary Cahiers/Barr/Chipp pages unread (library/IA blocked). Wikiquote secondary quotation only — art-theory context; not scored for B."
    source_quality: "unofficial web copy"
    used_for: [worldview, lane_b, review]
  - id: S6
    type: secondary
    kind: "journal article"
    author: "John Richardson"
    year: 1987
    citation: "Richardson, John. \"Picasso's Apocalyptic Whorehouse.\" The New York Review of Books, 23 April 1987. https://www.nybooks.com/articles/1987/04/23/picassos-apocalyptic-whorehouse/."
    url: "https://www.nybooks.com/articles/1987/04/23/picassos-apocalyptic-whorehouse/"
    accessed: 2026-10-24
    reliability_note: "Leading Picasso biographer. Jacqueline 'not a believer' is reported speech. Family piety/Sacred Heart context used for heritage only."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview, childhood, heritage, review]
---

# Pablo Picasso

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`. Deepen D1 2026-10-24: primary_system BELOW_THRESHOLD (leads ATHE); A BELOW_THRESHOLD (alt 4); B UNKNOWN (P16); mid_basin BELOW_THRESHOLD. Unplotted. No fallacy_catalog.

## Summary

Pablo Picasso (1881–1973), Spanish painter and sculptor, co-creator of Cubism with Georges Braque [S1; S3]. Working span coded 1901–1937 (Blue Period through Guernica) [S1; S3]. **Lane A:** primary_system BELOW_THRESHOLD (leads ATHE); A BELOW_THRESHOLD (alt 4); B UNKNOWN; C/D/E UNKNOWN; mid_basin BELOW_THRESHOLD. Not plotted.

## Life and work

Born Málaga; trained under his father and at La Llotja (Barcelona) and briefly San Fernando (Madrid); long career in Paris and France; died Mougins [S1; S3]. Joined the French Communist Party after World War II [S1; S3].

## Contribution and impact

Blue Period from 1901; *Les Demoiselles d'Avignon* (1907); Analytical Cubism with Braque (1909–12); *Guernica* (1937) [S1; S3]. Britannica: one of the most influential artists of the 20th century [S1].

## Childhood and education

Catholic baptism (heritage) [S3]. Father José Ruiz Blasco, drawing professor; Science and Charity honourable mention 1897; break with academic path after Horta 1898–99 [S1].

## Adult working worldview

**Lane A (separate from Lane B).** No first-person profession strong enough to score a system or A/B at ≥0.5.

- **primary_system BELOW_THRESHOLD** (leads ATHE). Jacqueline reported he “always claims he is not a believer” [S6]. Secondary sources label him atheist [S3, citing Cox Tate]. Gilot’s God-as-artist remark is a style metaphor [S4, p. 50; P43]. CHRIST not coded as adult working system.
- **A BELOW_THRESHOLD** (named alt 4). Reported speech + secondary labels + metaphor — under the 0.5 bar (P19). Do not overclaim A 4.
- **B UNKNOWN.** Not a scientist. Zervos “instrument of nature” / “cannot go against nature” is painting process, not nature’s causal order [S5; P16].
- **C, D, E UNKNOWN. mid_basin BELOW_THRESHOLD.**

## Heritage (context only)

Roman Catholic by baptism [S3]. Andalusian/Spanish [S1; S3]. Not an outcome and not a worldview code.

## Timing

Major work period 1901–1937; age at first lasting contribution 20 [S1; S3].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Cubism supplies geometric form in the work [S1]; no lawful-order circle claim; Zervos nature language is art process [S5].

## Open questions

- Own-hand disbelief / atheism profession (letters; non-P43 interview).
- Full Chipp/Barr Zervos pages; Dillenberger & Handley *Religious Art*; Cox interview / NCR church quote.
- Parmelin / Brassaï interview books (P43).

## Research log

- 2026-10-15: Read Britannica (McCully) body through 1903.
- 2026-10-24 (D1): Wayback Britannica full McCully (Demoiselles, Cubism, Guernica); Wikipedia EN dual bio; QI + Gilot p.50 God-as-artist (P43); Wikiquote/Zervos nature quotes (not B); Richardson NYRB Jacqueline “not a believer”; Cox Tate “atheist” via Wikipedia only. IA Gilot/Chipp borrow blocked. A/B left BELOW_THRESHOLD / UNKNOWN — thin sources, no overclaim. No fallacy_catalog.
