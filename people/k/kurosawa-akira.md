---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to visual_arts. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #135, F3 rank 139). Opened Sragow primary: Salon 21 Sep 2000 reprint of Michael Sragow's 1986 Ran interview (S5) — gods/God 'powerlessness' quote in the interviewer's own signed recount. Opened Cineaste text: Hirano, Cineaste XIV.4 (1986) pp. 23–25, 'Making Films for All the People' — 'God and Buddha, if they actually exist' verified in DBU study-guide reprint of the Q&A (S3) and eNotes source citation (S6). Read Something Like an Autobiography (1982 Eng., S7): childhood Buddhist funeral laughter ('absurdly funny'; brother 'Idiotic!'); father-ordered daily Hachiman shrine visits. V3 secondary-quotation bar lifted; content still does not score — primary/A/B restored BELOW_THRESHOLD (AGNOS/BUDDH leads; film-viewpoint conditional ≠ explicit AGNOS suspension; no BUDDH profession; B is human-conduct film viewpoint not nature, P16). C/D/E UNKNOWN; mid BELOW. Still not plotted. P47 on S1–S8; P50 Wikipedia EN (S8) dual bio; parents Isamu/Shima named. No fallacy_catalog; no figures/. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z1 audit fixes (blind audit /workspace/genius_study_audit/gs_8813a47_Z1/run1/): Z1-41 (FAIL): primary_system, A_locus and B_cause BELOW_THRESHOLD -> UNKNOWN, with AGNOS and BUDDH kept as leads (V3: second-hand quotations alone do not move a value off UNKNOWN); mid_basin -> UNKNOWN. Still not plotted."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z1, order P32: F 3, rank 139). Basics from Britannica (Tadao Sato and Britannica Editors, signed). Own voice on religion only in interviews about Ran, both as secondary quotations: to Michael Sragow (1986, reprinted in Sight & Sound, 2010), 'the gods or God or whoever it is observing human events is feeling sadness ... and powerlessness to affect human beings' behaviour'; to Cineaste (quoted in a Dallas Baptist University study guide), 'how God and Buddha, if they actually exist, perceive this human life'. Not a scientist. Span 1950–1985 at 0.7 (Rashomon to Ran). primary_system BELOW_THRESHOLD (leads AGNOS, BUDDH); A, B BELOW_THRESHOLD with readings named; C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD. Not plotted. Draft, not reviewed."}

identity:
  id: kurosawa-akira
  display_name: "Akira Kurosawa"
  roster:
    canonical_name: "Akira Kurosawa"
    rank: 139
    F: 3
    models: [Gemini, GPT, Grok]
    band: "core (3–4)"
    status: core
    field: film
    field_bucket: arts
  full_name: {value: "Kurosawa Akira", certainty: 0.7, cites: [{source: S1, locator: "title; opening"}], how_known: "Britannica (Japanese order)."}
  native_name: {value: "黒澤明", certainty: 0.7, cites: [{source: S1, locator: "title"}, {source: S8, locator: "infobox (黒澤 明)"}], how_known: "Britannica title; Wikipedia EN agrees (P50)."}
  aliases:
    - {name: "Akira-Kurosawa", kind: "roster alias"}
    - {name: "Kurosawa-Akira", kind: "roster alias"}

basics:
  birth:
    date: {value: "1910-03-23", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "Quick Facts; opening"}, {source: S8, locator: "infobox (March 23, 1910)"}], how_known: "Britannica; Wikipedia EN agrees (P50)."}
    place: {value: "Tokyo", modern_name: "Tokyo, Japan", polity_then: "Empire of Japan", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}, {source: S8, locator: "infobox / Childhood (Ōi / Shinagawa)"}], how_known: "Britannica; Wikipedia EN agrees (P50)."}
  death:
    date: {value: "1998-09-06", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "Quick Facts; opening"}, {source: S8, locator: "infobox (September 6, 1998)"}], how_known: "Britannica; Wikipedia EN agrees (P50)."}
    place: {value: "Tokyo", modern_name: "Tokyo, Japan", polity_then: "Japan", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}, {source: S8, locator: "infobox (Setagaya, Tokyo)"}], how_known: "Britannica; Wikipedia EN agrees (P50)."}
  first_lasting_contribution_year: {value: 1950, certainty: 0.7, cites: [{source: S1, locator: "'Films of the 1950s'"}], how_known: "Rashomon (1950): 'the first time a Japanese film had won such high international acclaim' (S1). Drunken Angel (1948), which 'made Kurosawa's name famous', is listed as a major work, not as lasting (coder's call); taking 1948 would not change any score."}
  era_bucket: {value: "1950 on", certainty: 0.7, cites: [{source: S1, locator: "'Films of the 1950s'"}], how_known: "From 1950 (P2: an edge year goes to the later bucket); 1948 would give '1850 to 1949', so 0.7 rests on the coder's call above."}
  region_of_birth: {value: "East Asia", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}], how_known: "Japan (P3)."}
  region_of_work: {value: "East Asia", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Japan."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Japanese"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
  occupations: {value: ["film director", "screenwriter", "painter (early)"], certainty: 0.7, cites: [{source: S1, locator: "'Early life'; 'First films'"}], how_known: "Britannica."}

contribution:
  primary_domain: visual_arts
  fields: {value: ["film"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Rashomon", year: 1950, kind: work, lasting: "Venice Grand Prix and Academy Award; 'advanced the idea of cinema as a means of probing a metaphysical problem' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Films of the 1950s'"}], how_known: "Britannica."}
    - {value: "Ikiru", year: 1952, kind: work, lasting: "'regarded by many critics as one of the finest works in the history of the cinema' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Films of the 1950s'"}], how_known: "Britannica."}
    - {value: "Seven Samurai", year: 1954, kind: work, lasting: "his 'greatest commercial success'; inspiration for The Magnificent Seven (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Films of the 1950s'"}], how_known: "Britannica."}
    - {value: "Throne of Blood", year: 1957, kind: work, lasting: "'called the best film of all the countless cinematized Shakespearean dramas' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Films of the 1950s'"}], how_known: "Britannica."}
    - {value: "Ran", year: 1985, kind: work, lasting: "named in Britannica's opening among the films that won him 'international acclaim' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica; latest listed, so it ends the span (P30 addendum)."}
  evidence_of_impact:
    - {value: "First Japanese film director to win international acclaim", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works:
    - {value: "Drunken Angel (Yoidore tenshi)", year: 1948, kind: other, certainty: 0.7, cites: [{source: S1, locator: "'First films'"}], how_known: "Britannica: 'made Kurosawa's name famous'."}
    - {value: "Kagemusha", year: 1980, kind: other, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  honours:
    - {value: "Golden Lion (Grand Prix), Venice, for Rashomon", year: 1951, certainty: 0.7, cites: [{source: S1, locator: "'Films of the 1950s'"}], how_known: "Britannica."}
  definition_fit: {value: "clearly meets", rationale: "'The first Japanese film director to win international acclaim' (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Japanese Buddhist and Shinto practice (household)", certainty: 0.5, cites: [{source: S7, locator: "sister's funeral chapter; 'Kendo' chapter (Hachiman shrine)"}], how_known: "Autobiography: sister's funeral at a Buddhist temple with priests, sutras, posthumous Buddhist name; father ordered daily morning visits to a Hachiman shrine with seal diary (Shinto). No single named family creed."}
  family_religious_practice: {value: "Buddhist funerary rites; father-enforced daily Hachiman shrine visits in primary-school years", certainty: 0.5, cites: [{source: S7, locator: "sister's funeral; 'Kendo'"}], how_known: "Autobiography."}
  parents_and_household:
    - {value: "Isamu Kurosawa (1864–1948), former army officer / Toyama Academy graduate, then teacher who helped develop athletics instruction in Japan; samurai-family background (Akita)", role: father, certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}, {source: S8, locator: "Childhood and youth"}], how_known: "Britannica (career); Wikipedia EN names Isamu and dates (P50)."}
    - {value: "Shima Kurosawa (1870–1952), from a merchant family in Osaka", role: mother, certainty: 0.5, cites: [{source: S8, locator: "Childhood and youth"}], how_known: "Wikipedia EN (P50); Britannica does not name her."}
  household_circumstances: {value: "Moderately wealthy; youngest of eight (siblings already grown or deceased); father transferred strict expectations to him after his brother's academic turn", certainty: 0.5, cites: [{source: S7, locator: "early chapters"}, {source: S8, locator: "Childhood and youth"}], how_known: "Autobiography and Wikipedia EN."}
  schooling:
    - {value: "Kuroda Primary School; kendo and calligraphy under father's orders; free-education circle of teacher Mr. Tachikawa", stage: elementary school, run_by: other, years: "c. Taishō era", certainty: 0.5, cites: [{source: S7, locator: "'Kendo'"}], how_known: "Autobiography."}
    - {value: "Art school after secondary school; painting in the Western style", stage: other, run_by: other, years: "c. 1927–1936", certainty: 0.5, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica (undated); years the coder's estimate."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "Older brother Heigo (benshi; guided film/theatre watching; died by suicide 1933)", certainty: 0.7, cites: [{source: S8, locator: "Childhood and youth"}, {source: S7, locator: "'A Story I Don't Want to Tell' (cited via Wikipedia)"}], how_known: "Wikipedia EN; autobiography chapter named there."}
  languages_in_childhood: {value: ["Japanese"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  notable_events:
    - {value: "Laughed through sister's Buddhist funeral as a child; brother called the ceremony 'Idiotic!' — he agreed it was 'absurdly funny'", certainty: 0.5, cites: [{source: S7, locator: "sister's funeral chapter"}], how_known: "Autobiography (childhood skepticism of funerary ritual; not an adult AGNOS profession)."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1950–1985", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Films of the 1950s'"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing read."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "(interview) Deepen D1: V3 secondary bar lifted — Sragow 1986 now read in Salon 2000 (S5, interviewer's signed recount); Cineaste XIV.4 1986 Hirano text verified (S3/S6). Leads AGNOS and BUDDH. Own voice: 'how God and Buddha, if they actually exist, perceive this human life' (S3) is a film-scene conditional ('essential scenes of this film are based on my wondering'), not an explicit personal suspension of belief (AGNOS needs explicit suspension). No BUDDH profession. Sragow 'gods or God or whoever it is' is the film's observing viewpoint for the battle-music cue, not a creed. Autobiography childhood funeral laughter (S7) is childhood, not adult working identity. Not a scientist. Stay BELOW with named leads."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: AGNOS, reason: "Lead: 'if they actually exist' (S3, now primary-verified). Against: film-craft conditional / wondering for Ran scenes, not a stated personal suspension of judgment."}
    - {code: BUDDH, reason: "Lead: 'God and Buddha' as the imagined observers (S3); Japanese Buddhist funerary heritage (S7). Against: no profession; childhood found the funeral 'absurdly funny'."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "(interview) Deepen D1: primary-verified (S3, S5). 'If they actually exist' (S3) states no locus; Sragow's observing 'gods or God or whoever' (S5) is the film's viewpoint for the muted-battle music, not a personal A score. Named reading toward no clear personal God, but film intent ≠ scored locus (P19, P42 for character speech; director's film-viewpoint still not a creed). Stay BELOW."}
    B_cause: {value: BELOW_THRESHOLD, how_known: "(interview) Deepen D1: primary-verified (S5). Observing divinity's 'powerlessness to affect human beings' behaviour' concerns human conduct in Ran's viewpoint, not nature (P6, P16). Cineaste line on 'exorcise the essential evil in human nature' (S3) is likewise human nature / ethics, not physical-world exception. Not a scientist. Stay BELOW."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read on his own deserts/afterlife (P19); characters' words in Ran are not his (P42)."}
    D_authority: {value: UNKNOWN, how_known: "Nothing read (P19)."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read on the world's order (P7, P19)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A and B both BELOW_THRESHOLD — mid-basin needs both at ≥0.7 (P4). Still not plotted."}
  statements:
    - text: "What I was trying to get at in Ran – and this was there from the script stage – was that the gods or God or whoever it is observing human events is feeling sadness about how human beings destroy each other, and powerlessness to affect human beings' behaviour. The music comes up to represent the feelings of the gods."
      cites: [{source: S5, locator: "Salon 2000 recount of 1986 interview"}, {source: S2, locator: "section 13, Ran (Sight & Sound anthology)"}]
      date: "1986"
      context: "Told to Michael Sragow in 1986 during Ran's first run, explaining why battle sound drops to mournful music; Sragow published the exchange in Salon, 21 Sep 2000. Within a year after the span end (Ran, 1985)."
      axes: [A_locus, B_cause]
      kind: "recorded interview"
      verified_against: "newspaper interview"
      verified_on: 2026-10-24
      note: "Primary path opened: Salon is the interviewer's own signed recount. Sight & Sound July 2010 (S2) reprints a shorter form without the music sentence."
    - text: "What I meant was that some of the essential scenes of this film are based on my wondering how God and Buddha, if they actually exist, perceive this human life, this mankind stuck in the same absurd behavior patterns. ... I did not mean that I wanted to see through the eyes of a heavenly being."
      cites: [{source: S3, locator: "opening Cineaste Q&A block"}, {source: S6, locator: "Cineaste XIV.4 (1986) source note"}]
      date: "1986"
      context: "Cineaste interview by Kyoko Hirano (translated from Japanese), New York visit for Ran at the NY Film Festival; correcting a Japanese magazine's 'heavenly viewpoint' report. Title: 'Making Films for All the People.' Within a year after the span end."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Text verified via DBU study-guide reprint of the Cineaste Q&A (S3); bibliographic identity via eNotes (S6: Cineaste Vol. XIV No. 4, 1986, pp. 23–25). Cardullo Interviews reprint (IA) access-restricted (401)."
    - text: "To me, the whole thing was absurdly funny. When I heard my brother's opinion ['Idiotic!'], I felt relieved. I wondered if my sister would be at all consoled by that ceremony in the main hall."
      cites: [{source: S7, locator: "sister's funeral chapter"}]
      date: "1981"
      context: "Something Like an Autobiography: childhood memory of laughing at sister's Buddhist funeral while priests recited sutras with drum and gong. Childhood; not adult working worldview."
      axes: []
      kind: "autobiography"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Heritage/childhood only; does not score adult AGNOS."
  changes_over_life: []
  coder_notes: "Deepen D1 2026-10-24: (1) span still Rashomon 1950–Ran 1985; (2) V3 lifted by Salon Sragow + Cineaste text; (3) content still BELOW — film-viewpoint conditional ≠ AGNOS/BUDDH scores; B fails P16; (4) autobiography fills childhood Buddhist/Shinto practice, not adult code; (5) Chart-moving NO. Not plotted."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Japanese", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Japanese Buddhist funerary and Shinto shrine practice (household)", certainty: 0.5, cites: [{source: S7, locator: "funeral; Hachiman shrine"}], how_known: "Autobiography (practice, not a named exclusive creed)."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated; father enforced shrine-seal piety diary, not doctrinal catechism."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1950–1985", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Films of the 1950s'"}], how_known: "Rashomon (1950) to Ran (1985) (P29, P30)."}
  age_at_first_lasting_contribution: {value: 40, certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}], how_known: "1950 − 1910 = 40 (P30)."}
  first_evidence_of_lio_type_views: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S5, locator: "Salon 2000"}, {source: S3, locator: "Cineaste Q&A"}], how_known: "Primary-verified Ran interviews still do not score any axis at 3 or 4."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S5, locator: "Salon 2000"}, {source: S3, locator: "Cineaste Q&A"}], how_known: "As above; interviews are immediately after span end (1986)."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Ran interviews are 1986 (after 1985 span end); autobiography silent on adult creed."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Not assessed."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Not assessed."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S5, locator: "Salon 2000"}], how_known: "Not assessed."}
  reading: "Not assessed."
  notes: ""

institutions:
  - {value: "PCL (Photo Chemical Laboratories) studio", role: "assistant director", years: "1936–1943", kind: employer, certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica (the PCL expansion is the coder's)."}
collaborators:
  - {value: "Mifune Toshirō", relation: collaborator, note: "lead actor in most of his films from Drunken Angel", certainty: 0.7, cites: [{source: S1, locator: "'First films'"}], how_known: "Britannica."}
  - {value: "Yamamoto Kajirō", relation: "mentor or employer", note: "director he assisted until 1943", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 139"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Cineaste XIV.4 full magazine page images / Cardullo Interviews book still unread (IA 401); DBU reprint + eNotes citation used for the Hirano Q&A."
    - "Autobiography read as unofficial PDF (lenguajecinematografico wordpress OCR); page numbers not mapped to the Vintage print."
  open_questions:
    - "Optional: Cardullo (ed.) Akira Kurosawa: Interviews full Hirano piece, or Cineaste XIV.4 page images."
    - "In-span (pre-1986) interviews that state a personal creed, if any exist."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Tadao Sato; Britannica Editors"
    citation: "Sato, Tadao, and Britannica Editors. \"Kurosawa Akira.\" Encyclopaedia Britannica (15 Oct 2026). https://www.britannica.com/biography/Kurosawa-Akira. Read live 2026-10-19; rechecked 2026-10-24."
    url: "https://www.britannica.com/biography/Kurosawa-Akira"
    accessed: 2026-10-24
    reliability_note: "Signed article; body cited, AI question boxes not cited (P26)."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, institutions, collaborators]
    source_quality: "reference entry"
  - id: S2
    type: secondary
    kind: other
    author: "Sight & Sound (BFI)"
    citation: "\"Kurosawa on Kurosawa.\" Sight & Sound, July 2010 (BFI). Archived https://web.archive.org/web/20190520121122/old.bfi.org.uk/sightandsound/feature/49625"
    url: "https://web.archive.org/web/20190520121122/old.bfi.org.uk/sightandsound/feature/49625"
    accessed: 2026-10-24
    reliability_note: "Magazine anthology of interview remarks (Richie 1964; Rayns 1981; Sragow 1986). Prefer S5 (Salon) for the Ran/Sragow line."
    used_for: [worldview]
    source_quality: "other"
  - id: S3
    type: secondary
    kind: other
    author: "Dallas Baptist University, Mitchell Center (study guide reprinting Cineaste Q&A)"
    citation: "\"Akira Kurosawa's Lear: Ran and the Failure of the Samurai Ethic.\" Global film resources, Dallas Baptist University. Opens with the Cineaste/Hirano Q&A block. https://www.dbu.edu/mitchell/global-film-resources/_documents/ranandthefailureofthesamuraiethic.pdf"
    url: "https://www.dbu.edu/mitchell/global-film-resources/_documents/ranandthefailureofthesamuraiethic.pdf"
    accessed: 2026-10-24
    reliability_note: "Unsigned teaching guide; reprints the Cineaste interview Q&A verbatim with 'Cineaste:' / 'Akira Kurosawa:' labels. Bibliographic identity of the interview from S6. Unofficial web copy of the interview text (P47)."
    used_for: [worldview]
    source_quality: "unofficial web copy"
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [identity, review]
    source_quality: "study roster"
  - id: S5
    type: primary
    kind: published work by the subject
    author: "Michael Sragow"
    citation: "Sragow, Michael. \"Lear meets the energy vampire.\" Salon, 21 September 2000. https://www.salon.com/2000/09/21/kurosawa/ — signed recount of his 1986 interview with Kurosawa during Ran's first run."
    url: "https://www.salon.com/2000/09/21/kurosawa/"
    accessed: 2026-10-24
    reliability_note: "Interviewer publishing his own 1986 exchange; treated as recorded_interview primary for the Ran gods/powerlessness line (V3 path)."
    used_for: [worldview, timing, lane_b]
    source_quality: "newspaper interview"
  - id: S6
    type: secondary
    kind: other
    author: "eNotes / Cineaste bibliographic note"
    citation: "eNotes. \"Akira Kurosawa Criticism: Making Films for All the People.\" SOURCE: \"Making Films for All the People,\" Cineaste, Vol. XIV, No. 4, 1986, pp. 23–25 (Kyoko Hirano interview/translation). https://www.enotes.com/topics/akira-kurosawa/criticism/kurosawa-akira-vol-119/interviews"
    url: "https://www.enotes.com/topics/akira-kurosawa/criticism/kurosawa-akira-vol-119/interviews"
    accessed: 2026-10-24
    reliability_note: "Confirms Cineaste XIV.4 (1986) pp. 23–25 identity and opens the same Hirano Q&A; paywalled after the first sentence of the God/Buddha answer. Used with S3 for the full paragraph."
    used_for: [worldview]
    source_quality: "other"
  - id: S7
    type: primary
    kind: published work by the subject
    author: "Akira Kurosawa; tr. Audie E. Bock"
    citation: "Kurosawa, Akira. Something Like an Autobiography. Trans. Audie E. Bock. Vintage, 1983 (Japanese 1981). Unofficial PDF copy read 2026-10-24 (lenguajecinematografico.wordpress.com upload)."
    url: "https://lenguajecinematografico.wordpress.com/wp-content/uploads/2013/07/kurosawa-akira-something_like_an_autobiography.pdf"
    accessed: 2026-10-24
    reliability_note: "Own words (memoir). Unofficial web PDF / OCR; Vintage page numbers not mapped. Used for childhood religion practice and funeral episode, not adult LIO scores."
    used_for: [childhood, heritage, worldview]
    source_quality: "unofficial web copy"
  - id: S8
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "\"Akira Kurosawa.\" Wikipedia (English). https://en.wikipedia.org/wiki/Akira_Kurosawa. Read 2026-10-24."
    url: "https://en.wikipedia.org/wiki/Akira_Kurosawa"
    accessed: 2026-10-24
    reliability_note: "P50 dual-bio check against Britannica; parents Isamu/Shima and childhood detail. Not used for worldview codes."
    used_for: [identity, basics, childhood, heritage]
    source_quality: "reference entry"
---

# Akira Kurosawa

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Kurosawa Akira (1910–1998), Japanese film director [S1; S8]. Deepen D1: primary_system BELOW_THRESHOLD (leads AGNOS, BUDDH; interview); A, B BELOW_THRESHOLD; C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD. Chart-moving NO. Not plotted.

## Life and work

Painter, then assistant director at PCL from 1936; director from 1943 [S1]. Parents Isamu and Shima [S8].

## Contribution and impact

Rashomon, Ikiru, Seven Samurai, Throne of Blood, Ran [S1].

## Childhood and education

Father an army officer turned teacher; art school [S1]. Autobiography: Buddhist temple funeral for a sister (he laughed; found it "absurdly funny"); father-ordered daily Hachiman shrine visits with a piety seal diary [S7].

## Adult working worldview

Primary-verified Ran interviews (Sragow/Salon 1986 via 2000 [S5]; Cineaste/Hirano 1986 [S3; S6]): film-viewpoint conditional "God and Buddha, if they actually exist" and observing gods' "powerlessness" over human behaviour — leads AGNOS/BUDDH but stay BELOW (not explicit personal suspension; B not about nature, P16). Autobiography childhood funeral skepticism does not score adult AGNOS [S7].

## Heritage (context only)

Japanese [S1]. Household Buddhist funerary and Shinto shrine practice [S7].

## Timing

1950–1985, from age 40 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Not assessed [S1].

## Open questions

- Cardullo Interviews full Hirano piece or Cineaste XIV.4 page images.
- Any in-span personal creed interview (pre-1986).

## Research log

- 2026-10-19: Read Britannica (Sato), the Sight & Sound anthology and a study guide quoting Cineaste.
- 2026-10-24: Deepen D1. Opened Salon Sragow 2000 [S5]; verified Cineaste XIV.4 via DBU + eNotes [S3; S6]; read autobiography PDF [S7]; Wikipedia EN P50 [S8]. V3 lifted; primary/A/B/mid stay or restore BELOW. Chart-moving NO.
