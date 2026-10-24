---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch E)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch E, order P32: F 5, rank 27). Basics from Britannica (Zelazko). No worldview statement of her own was found: the widely quoted 'I am an atheist' (1948) is Diego Rivera's, not hers. All worldview fields UNKNOWN. Draft, not reviewed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #27, F5 rank 27). P47 source_quality on every source. Dual-sourced basics (S1 Britannica prior + S3 Wikipedia EN). Own words: diary (Abrams 1995 / Lowe; English via Marginalian S4 and Denver Art Museum S5) — disagreement with 'religions' among imperialism/fascism/capitalism; 'everything exists, and moves, under only one law = life' (political-existential, not B). 1948 letter to President Alemán (Zamora Cartas; Marginalian S6) protests mural censorship — anti-sectarian, no God-denial. Scholarly 'avowed'/'adamant' atheist labels (Barnet-Sanchez LARR S7 summarizing Cooey/Lowe) without a Kahlo 'I do not believe in God'. Rivera's 1948 'I am an atheist' remains Rivera's (S6). Mother 'fanatically religious' (Kahlo characterization via S3). primary_system BELOW_THRESHOLD (lead ATHE); A_locus BELOW_THRESHOLD (P38; Joyce/Monet precedent); B_cause UNKNOWN (not a scientist; one-law = life ≠ nature's causal order, P16); C/D/E UNKNOWN; mid_basin UNKNOWN (B UNKNOWN, P19). Chart: still unplotted. No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: kahlo-frida
  display_name: "Frida Kahlo"
  roster:
    canonical_name: "Frida Kahlo"
    rank: 27
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: art
    field_bucket: arts
  full_name: {value: "Magdalena Carmen Frida Kahlo y Calderón", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts ('Original name')"}, {source: S3, locator: "infobox / lead (Magdalena Carmen Frida Kahlo y Calderón)"}], how_known: "Britannica + Wikipedia EN. Married name Frida Kahlo de Rivera also used."}
  native_name: {value: "Magdalena Carmen Frida Kahlo y Calderón", certainty: 0.7, cites: [{source: S3, locator: "lead; Spanish pronunciation"}], how_known: "Spanish in Latin script; Wikipedia EN."}
  aliases:
    - {name: "Frida-Kahlo", kind: "roster alias"}
    - {name: "Kahlo-Frida", kind: "roster alias"}
    - {name: "Frieda Kahlo", kind: "other"}

basics:
  birth:
    date: {value: "1907-07-06", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S3, locator: "infobox; Family and childhood"}], how_known: "Britannica + Wikipedia EN. She later claimed 1910 to align with the Revolution (S3) — not used as birth date."}
    place: {value: "Coyoacán, Mexico", modern_name: "Coyoacán, Mexico City, Mexico", polity_then: "Mexico", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S3, locator: "infobox; Family and childhood (La Casa Azul / grandmother)"}], how_known: "Britannica + Wikipedia EN."}
  death:
    date: {value: "1954-07-13", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S3, locator: "infobox; Last years and death"}], how_known: "Britannica + Wikipedia EN. Official cause pulmonary embolism; no autopsy (S3)."}
    place: {value: "Coyoacán, Mexico", modern_name: "Coyoacán, Mexico City, Mexico", polity_then: "Mexico", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S3, locator: "infobox; Last years and death (Casa Azul)"}], how_known: "Britannica + Wikipedia EN."}
  first_lasting_contribution_year: {value: 1926, certainty: 0.7, cites: [{source: S1, locator: "Key dates; accident section (Self-Portrait Wearing a Velvet Dress, 1926)"}, {source: S3, locator: "Early career / Self-portrait in a Velvet Dress 1926"}], how_known: "Earliest listed lasting contribution (P13)."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "1926"}, {source: S3, locator: "birth 1907; death 1954"}], how_known: "From 1926 (P2); dual-sourced life dates."}
  region_of_birth: {value: "Latin America and Caribbean", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S3, locator: "infobox"}], how_known: "Mexico (P3)."}
  region_of_work: {value: "Latin America and Caribbean", certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S3, locator: "Work in the United States; Return to Mexico City"}], how_known: "Mexico; 1930–33 in the United States (not a second lasting region of work)."}
  sex_as_recorded: {value: "female", certainty: 1.0, cites: [{source: S1, locator: "text"}, {source: S3, locator: "infobox"}], how_known: "As recorded."}
  languages_of_work: {value: [Spanish], certainty: 0.7, cites: [{source: S3, locator: "diary / letters mostly Spanish"}, {source: S4, locator: "diary Spanish with occasional English"}], how_known: "Mexican life; diary mostly Spanish (S3, S4)."}
  occupations: {value: ["painter", "teacher (La Esmeralda)"], certainty: 1.0, cites: [{source: S1, locator: "opening; Key dates 1943–54"}, {source: S3, locator: "opening; La Esmeralda"}], how_known: "Britannica + Wikipedia EN."}

contribution:
  fields: {value: ["painting"], certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "opening"}], how_known: "Britannica + Wikipedia EN."}
  lasting_original_contributions:
    - {value: "Self-Portrait Wearing a Velvet Dress (first known work)", year: 1926, kind: work, lasting: "start of the self-portraits she is best known for (S1)", certainty: 0.7, cites: [{source: S1, locator: "accident section"}, {source: S3, locator: "Early career"}], how_known: "Britannica + Wikipedia EN."}
    - {value: "Henry Ford Hospital and My Birth", year: 1932, kind: work, lasting: "'some of her most harrowing works' (S1); retablo manner (S3)", certainty: 0.7, cites: [{source: S1, locator: "'Marriage to Diego Rivera'"}, {source: S3, locator: "Work in the United States"}], how_known: "Britannica + Wikipedia EN."}
    - {value: "The Two Fridas", year: 1939, kind: work, lasting: "among her most famous double self-portraits; purchased by Museo de Arte Moderno 1947 (S3)", certainty: 0.7, cites: [{source: S1, locator: "intro Q&A on gender (signed page)"}, {source: S3, locator: "Return to Mexico City; Self-portraits"}], how_known: "Britannica + Wikipedia EN."}
    - {value: "Self-Portrait with Cropped Hair", year: 1940, kind: work, lasting: "cited for her rejection of gender restrictions, which 'continues to inspire artists' (S1)", certainty: 0.7, cites: [{source: S1, locator: "intro Q&A on gender (signed page)"}, {source: S3, locator: "Self-portraits"}], how_known: "Britannica + Wikipedia EN."}
    - {value: "The Broken Column", year: 1944, kind: work, lasting: "iconic spinal-pain self-portrait of the mid-1940s decline period (S3)", certainty: 0.7, cites: [{source: S3, locator: "Later years; Style"}], how_known: "Wikipedia EN (Britannica prior read did not date it)."}
  evidence_of_impact:
    - {value: "First 20th-century Mexican artist in the French national collection (The Frame, 1939)", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "Key dates 1939"}, {source: S3, locator: "Paris exhibition / Louvre"}], how_known: "Britannica + Wikipedia EN."}
  major_works: []
  honours: []
  definition_fit: {value: "arguable", rationale: "Lasting fame mostly posthumous ('Fridamania'); originality of the self-portraits widely recognised.", certainty: 0.5, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "Posthumous recognition"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Roman Catholic (mother devout / 'fanatically religious'; father not practicing Catholic in the sources read)", certainty: 0.7, cites: [{source: S3, locator: "Family and childhood (mother 'fanatically religious'; baptism for Catholic traditions)"}, {source: S7, locator: "mother a devout Catholic"}], how_known: "Wikipedia EN quotes her characterization of her mother; Barnet-Sanchez LARR review states mother was a devout Catholic."}
  family_religious_practice: {value: "Mother ran a devout Catholic household; half-sisters from father's first marriage raised in a convent (S3, S7)", certainty: 0.5, cites: [{source: S3, locator: "Family and childhood"}, {source: S7, locator: "mother a devout Catholic; half-sisters in convent"}], how_known: "Secondary biographical consensus; not a household diary."}
  parents_and_household:
    - {value: "Father Guillermo Kahlo, German photographer (Hungarian descent; Jewish ancestry claimed by Frida, challenged by 2006 German genealogists who found Lutheran)", role: father, certainty: 0.7, cites: [{source: S1, locator: "early life"}, {source: S3, locator: "Family and childhood"}], how_known: "Britannica + Wikipedia EN."}
    - {value: "Mother Matilde Calderón y González, Mexican, of Spanish and Indigenous (Purépecha/Oaxaca) descent; devout Catholic", role: mother, certainty: 0.7, cites: [{source: S1, locator: "early life"}, {source: S3, locator: "Family and childhood"}, {source: S7, locator: "Matilde Calderon"}], how_known: "Britannica + Wikipedia EN + Barnet-Sanchez."}
  household_circumstances: {value: "La Casa Azul, Coyoacán; father often ill (epilepsy); mother's ailments; marriage described as loveless; atmosphere 'very, very sad' (Kahlo, via S3)", certainty: 0.5, cites: [{source: S3, locator: "Family and childhood"}], how_known: "Wikipedia EN summarizing Herrera/Ankori."}
  schooling:
    - {value: "National Preparatory School, Mexico City, aiming at medicine", stage: "grammar or secondary school", run_by: "state or municipal", years: "1922–1925", ages: "15–18", certainty: 0.7, cites: [{source: S1, locator: "early life"}, {source: S3, locator: "Family and childhood"}], how_known: "Britannica + Wikipedia EN; run_by is the coder's reading of a national school."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure:
    - {value: "More interested in science than drawing; planned to study medicine", year: 1922, age: 15, certainty: 0.7, cites: [{source: S1, locator: "early life"}, {source: S3, locator: "Family and childhood (natural sciences / physician)"}], how_known: "Britannica + Wikipedia EN."}
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [Spanish], certainty: 0.7, cites: [{source: S3, locator: "Coyoacán household"}], how_known: "Mexican Spanish household; father also spoke German (not scored as childhood language of hers)."}
  notable_events:
    - {value: "Polio, leaving a slight limp / thinner right leg", year: 1913, age: 6, certainty: 1.0, cites: [{source: S1, locator: "Key dates 1913"}, {source: S3, locator: "Family and childhood"}], how_known: "Britannica + Wikipedia EN."}
    - {value: "Baptized under Catholic tradition (given Magdalena Carmen so she could be baptized Catholic; always called Frida)", year: 1907, age: 0, certainty: 0.5, cites: [{source: S3, locator: "Notes [a]"}], how_known: "Wikipedia EN note; parish register not opened."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1926–1944", certainty: 0.7, cites: [{source: S1, locator: "dates"}, {source: S3, locator: "Broken Column 1944; lasting list"}], how_known: "Equals timing.major_work_period (extended to Broken Column 1944)."}
  nominal_affiliations:
    - {value: "Mexican Communist Party (PCM)", certainty: 0.7, cites: [{source: S1, locator: "accident section"}, {source: S3, locator: "joined PCM 1927; rejoined 1948"}], how_known: "Britannica + Wikipedia EN. Political membership, not by itself a worldview code."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No first-person statement equating or opposing science and religion read. Diary and 1948 letter opened for politics/religion; nothing on science–religion."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "Scholarly 'avowed'/'adamant' atheist labels (S7) plus diary disagreement with 'religions' (S4) and anti-sectarian 1948 letter (S6), without a Kahlo-authored 'I do not believe in God' or equivalent.", note: "Lead ATHE from Barnet-Sanchez/Cooey/Lowe (S7) and from diary list placing 'religions' with imperialism/fascism/capitalism (S4). Not scored ATHE: P38 needs published/own disbelief in God for A 4 even at 0.5; Joyce/Monet precedent — rejecting religions/practice without a God-view stays BELOW. Rivera's 1948 'I am an atheist' is Rivera's (S6), not Kahlo's. Fuentes's 'natural pantheism' reading of the diary (via S3 summary) is a competing scholarly lens, not her code. Baptism/mother's Catholicism is heritage, not adult CHRIST."}
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: ATHE, reason: "Lead: Barnet-Sanchez LARR ('adamant atheism'); Cooey via S7 ('avowed atheist'); Lowe situates her 'as an atheist' (S7); diary rejects 'religions' (S4). Rejected as scored code: no Kahlo own-words denial of God's existence read; the famous atheist quote is Rivera's (S6)."}
    - {code: CHRIST, reason: "Rejected for adult working years: Catholic baptism and devout mother are heritage; adult PCM membership, diary rejection of religions, and anti-clerical 1948 letter contradict practicing CHRIST. Religious imagery in paintings is desacralized use (S7), not coded as belief."}
    - {code: PANT, reason: "Fuentes introduction to the diary (summarized S3) posits 'natural pantheism' under the politics. Rejected: not her word; diary 'one law = life' is revolutionary-process language, not God-as-Nature (contrast Wright)."}
    - {code: AGNOS, reason: "No suspension-of-judgment language from Kahlo read; scholars use atheist, not agnostic."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, note: "Diary rejects 'religions' as a political/bourgeois item (S4) and the 1948 letter attacks sectarian/clerical censorship (S6) without locating God (in / above / as Nature) or denying God's existence. Scholarly 'atheist' labels (S7) are reconstruction. Named reading: 4 (ATHE locus) if a letter, interview, or diary line with explicit disbelief is opened; Joyce/Monet precedent (church/religions rejection without God-view → BELOW).", how_known: "BELOW_THRESHOLD under P19 (weak/indirect; private diary list + scholarly reconstruction; no P38 denial)."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P16). Researched: Britannica, Wikipedia, diary English via S4/S5 — 'everything exists, and moves, under only one law = life' equates law with life/revolutionary process, not nature's causal order (law vs exception). 'Nothing is absolute. Everything changes…' is flux language, not a B claim. Painting method and dialectical-materialism profession (1952 diary, S4) are not scored as B."}
    C_ledger: {value: UNKNOWN, how_known: "Last diary line hopes never to return (S3); not scored as afterlife/ledger claim. Nothing else on reward or afterlife in sources read."}
    D_authority: {value: UNKNOWN, how_known: "Nothing on revelation vs observation as authority (P19). Anti-clerical politics is not a D score."}
    E_scope: {value: UNKNOWN, how_known: "Nothing on the world's order as one/many (P7). 'Everything is all and one' in the revolution passage (S5) is political-existential, not scored as E."}
  mid_basin: {value: UNKNOWN, how_known: "B_cause is UNKNOWN, which takes precedence (§6, P19); A_locus is BELOW_THRESHOLD."}
  statements:
    - text: "1st. I'm convinced of my disagreement with the counterrevolution — imperialism — fascism — religions — stupidity — capitalism — and the whole gamut of bourgeois tricks — I wish to cooperate with the Revolution in transforming the world into a class-less one so that we can attain a better rhythm for the oppressed classes"
      cites: [{source: S4, locator: "diary politics excerpt (English translation)"}, {source: S5, locator: "Quotes about revolution (parallel paraphrase)"}]
      date: "1950"
      context: "Diary entry (Abrams facsimile / Lowe commentary), last decade of life (diary 1944–1954). English via Marginalian quoting The Diary of Frida Kahlo: An Intimate Self-Portrait. Private notebook; after most of the major-work span. Date approximate (S4 places the cluster 1950–1951 / revolutionary pages)."
      kind: "notebook or diary"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Own words rejecting 'religions' as a political category. Underwrites BELOW lead ATHE; not a P38 God-denial. Private ceiling; single passage — not consistent_private_letters 0.7."
    - text: "Revolution is the harmony of form and color and everything exists, and moves, under only one law = life. Nobody is separate from anybody else – nobody fights for [themselves]. Everything is all and one, Anguish and pain – pleasure and death are no more than a process of existence."
      cites: [{source: S5, locator: "Quotes about revolution"}]
      date: "1944"
      context: "Diary (1944–1954). English via Denver Art Museum curatorial blog quoting the diary. Exact diary page/date not opened this pass."
      kind: "notebook or diary"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "'One law = life' is revolutionary/existential process language, not a statement about nature's causal order (P16). Not scored for B. Date year is diary-span start placeholder; page undated in S5."
    - text: "Nothing is absolute. Everything changes, everything moves, everything revolves, everything flies and goes away."
      cites: [{source: S5, locator: "Quotes about life"}]
      date: "1944"
      context: "Diary (1944–1954). English via Denver Art Museum. Page/date not opened."
      kind: "notebook or diary"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Flux language; does not score B (and if anything cuts against exceptionless law). Date year is diary-span start placeholder."
    - text: "I want to communicate to you the tremendous historical responsibility that your government is assuming by letting a Mexican painter's work… be covered up… because of SECTARIAN, DEMAGOGIC, AND MERCENARY reasons. … those criminal attacks against freedom have only been committed in regimes like Hitler's and are still being committed under Francisco Franco, and in the past, during the dark and negative age of the 'Holy' Inquisition."
      cites: [{source: S6, locator: "letter body (English translation from Zamora)"}]
      date: "1948-10-20"
      context: "Letter to President Miguel Alemán Valdés protesting the boarding-over of Rivera's Hotel del Prado mural (Dios no existe). Printed in Martha Zamora, The Letters of Frida Kahlo: Cartas Apasionadas. English via Marginalian. Written for the president (published-letter / written_profession ceiling if treated as public protest); does not deny God."
      kind: "published letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Anti-sectarian / anti-Inquisition; supports BELOW lead against CHRIST practice, not ATHE/A4."
    - text: "To affirm 'God does not exist,' I do not have to hide behind Don Ignacio Ramírez; I am an atheist and I consider religions to be a form of collective neurosis."
      cites: [{source: S6, locator: "Rivera to a reporter (quoted after Kahlo letter narrative)"}]
      date: "1948"
      context: "Diego Rivera speaking to a reporter during the Hotel del Prado mural controversy — NOT Kahlo. Kept here as a data-quality / misattribution control (create pass and deepen both confirm)."
      kind: "reported speech"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Do not score Kahlo from this. Widely misattributed online to Kahlo."
    - text: "Frida Kahlo has come to represent… her adamant atheism combined with her desacralized use of religious imagery and symbolism…"
      cites: [{source: S7, locator: "p. 246 (opening synthesis)"}]
      date: "1997"
      context: "Holly Barnet-Sanchez, Latin American Research Review 32(3), review essay synthesizing recent Kahlo scholarship (incl. Cooey 1994; Lowe 1991)."
      kind: "other"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Scholarly synthesis asserting 'adamant atheism' without quoting a Kahlo denial of God. Ceiling scholarly_reconstruction 0.5; does not by itself score ATHE/A4."
    - text: "Cooey argues that although Frida was an avowed atheist, her use of religious symbolism—even if desacralized—posits a religious sensibility as a 'ritualistic transvaluing of the ordinary that reflects a deeply held faith' (p. 108)."
      cites: [{source: S7, locator: "p. 256 (on Cooey 1994)"}]
      date: "1997"
      context: "Barnet-Sanchez summarizing Paula M. Cooey, Religious Imagination and the Body (Oxford, 1994). Cooey's book page not opened this pass."
      kind: "other"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Second scholarly 'avowed atheist' label; Cooey also posits a residual religious sensibility — named tension, not a scored code."
  changes_over_life:
    - {value: "Late diary (1950–52) intensifies Marxist / 'Revolutionary Realism' profession and Party utility of painting (S4); PCM rejoined 1948 (S3). No documented change from disbelief-in-religions to theism, or the reverse, between the 1926–1944 span and the diary — adult anti-clerical / Communist stance treated as continuous for coding (P31).", certainty: 0.5, cites: [{source: S4, locator: "1952 'I am a self and a Communist'"}, {source: S3, locator: "rejoined PCM 1948"}], how_known: "Coder's reading of continuity; not a scored axis change."}
  coder_notes: "Deepen 2026-10-24: Abrams diary facsimile not opened page-by-page; English via Marginalian + DAM. Zamora letters via Marginalian. Cooey 1994 / Lowe 1991 / Herrera biography pages not opened beyond Barnet-Sanchez summary. Chart stays unplotted (A BELOW, B UNKNOWN). Religious imagery in paintings remains uncoded (create-pass call kept)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Mexican; German father (Hungarian descent; Jewish claim contested), Mexican mother of Spanish and Indigenous descent", certainty: 0.7, cites: [{source: S1, locator: "early life"}, {source: S3, locator: "Family and childhood"}], how_known: "Britannica + Wikipedia EN."}
  religious_heritage_by_birth: {value: "Roman Catholic (baptized for Catholic tradition; devout Catholic mother)", certainty: 0.5, cites: [{source: S3, locator: "Notes [a]; Family and childhood"}, {source: S7, locator: "mother a devout Catholic"}], how_known: "Baptism note + mother's devotion; family creed not a separate primary document (0.5)."}
  baptism_or_initiation: {value: "Baptized under Catholic tradition (names Magdalena Carmen for baptism; always called Frida)", certainty: 0.5, cites: [{source: S3, locator: "Notes [a]"}], how_known: "Wikipedia EN note; parish register not opened."}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1926–1944", certainty: 0.7, cites: [{source: S1, locator: "1926; 1940"}, {source: S3, locator: "Broken Column 1944"}], how_known: "First listed lasting contribution 1926 to Broken Column 1944 (P29, P30). Later still lifes / Marxism Will Give Health (c. 1954) not listed as lasting originals this pass."}
  age_at_first_lasting_contribution: {value: 19, certainty: 0.7, cites: [{source: S1, locator: "Quick Facts; 1926"}, {source: S3, locator: "birth 1907; 1926"}], how_known: "1926 − 1907 = 19 (P30)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No statement scored at 3 or 4 (P27); A and B not plottable."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", rationale: "A BELOW_THRESHOLD and B UNKNOWN — nothing scored as a LIO-type view at plottable certainty.", certainty: 0.5, cites: [{source: S4, locator: "religions list"}, {source: S7, locator: "adamant atheism"}], how_known: "Absence of scored axes."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Nothing read on childhood geometry or mathematical form beyond ordinary schooling.", certainty: 0.5, cites: [{source: S1, locator: "early life"}, {source: S3, locator: "Family and childhood"}], how_known: "No evidence."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "early life"}], how_known: "No evidence."}
  circle_present: {value: "unclear", rationale: "Cachuchas / PCM / muralist circle are political-artistic, not a geometric-form belief circle.", certainty: 0.5, cites: [{source: S3, locator: "Cachuchas; PCM"}], how_known: "No Lane B circle evidence."}
  reading: "As belief, not finding: unclear. Does not test H1."
  notes: "Lane A worldview deepen does not supply Lane B geometric-form evidence."

institutions:
  - {value: "La Esmeralda (Ministry of Public Education's School of Painting and Sculpture)", role: teacher, years: "1943–1954", kind: other, certainty: 0.7, cites: [{source: S1, locator: "Key dates 1943–54"}, {source: S3, locator: "La Esmeralda"}], how_known: "Britannica + Wikipedia EN."}
collaborators:
  - {value: "Diego Rivera", relation: family, note: "husband (married 1929, divorced 1939, remarried 1940)", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "infobox; marriage"}], how_known: "Britannica + Wikipedia EN."}
  - {value: "Tina Modotti", relation: other, note: "introduced Kahlo into communist / artist circle; reintroduced her to Rivera", certainty: 0.7, cites: [{source: S3, locator: "Bus accident and marriage"}], how_known: "Wikipedia EN."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 27"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "A widely shared 'I am an atheist' quote attributed to Kahlo online is Diego Rivera's (1948 reporter interview; S6)."
    - "Abrams diary facsimile pages not opened this pass; English diary quotes via Marginalian (S4) and Denver Art Museum (S5) secondary quotations."
    - "Cooey 1994 and Lowe 1991 known via Barnet-Sanchez LARR summary (S7), not full-page opens."
    - "Britannica live fetch not re-opened this deepen; S1 claims rest on the 2026-10-15 read plus dual-sourcing from Wikipedia for basics."
  open_questions:
    - "Open Abrams 1995 diary facsimile (Spanish + Lowe translation) for exact page/date of the religions list and any God/atheist line."
    - "Open Zamora Cartas Apasionadas and Herrera Frida for any Kahlo-authored denial of God."
    - "Open Cooey 1994 p.108 and Lowe 1991 for the primary citations behind 'avowed'/'as an atheist'."
    - "Parish baptism register for Magdalena Carmen."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Alicja Zelazko"
    citation: "Zelazko, Alicja. \"Frida Kahlo.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Frida-Kahlo."
    url: "https://www.britannica.com/biography/Frida-Kahlo"
    accessed: 2026-10-15
    reliability_note: "Signed encyclopedia article; create-pass read. Live re-fetch not required this deepen — basics dual-sourced from Wikipedia EN."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, institutions, collaborators]
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
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia. \"Frida Kahlo.\" https://en.wikipedia.org/wiki/Frida_Kahlo (accessed 2026-10-24)."
    url: "https://en.wikipedia.org/wiki/Frida_Kahlo"
    accessed: 2026-10-24
    reliability_note: "Used for dual-source basics, mother 'fanatically religious', baptism note, PCM dates, Broken Column 1944, lasting works. Atheism not taken from Wikipedia alone — followed to scholarly review (S7) and own-words sources (S4–S6)."
    source_quality: "other"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, institutions, collaborators, review]
  - id: S4
    type: primary
    kind: other
    author: "Frida Kahlo (diary); Sarah M. Lowe (commentary); Carlos Fuentes (introduction)"
    citation: "Kahlo, Frida. The Diary of Frida Kahlo: An Intimate Self-Portrait. Introduction by Carlos Fuentes; commentaries by Sarah M. Lowe. New York: Harry N. Abrams / Mexico City: La Vaca Independiente, 1995. English excerpts via Popova, Maria. \"Frida Kahlo's Politics.\" The Marginalian, 2 Aug 2013. https://www.themarginalian.org/2013/08/02/frida-kahlos-politics/."
    url: "https://www.themarginalian.org/2013/08/02/frida-kahlos-politics/"
    accessed: 2026-10-24
    reliability_note: "Primary diary text in scholarly facsimile edition; this pass used Marginalian's English quotation of the Abrams translation (secondary quotation of primary). Facsimile pages not opened."
    source_quality: "primary / own words"
    used_for: [worldview]
  - id: S5
    type: secondary
    kind: other
    author: "Laura Almeida (Denver Art Museum)"
    citation: "Almeida, Laura. \"Quotes from Frida Kahlo.\" Denver Art Museum blog, 28 Dec 2020. https://www.denverartmuseum.org/en/blog/quotes-frida-kahlo."
    url: "https://www.denverartmuseum.org/en/blog/quotes-frida-kahlo"
    accessed: 2026-10-24
    reliability_note: "Museum curatorial blog quoting diary/letters; English only; page/date of diary originals not given."
    source_quality: "other"
    used_for: [worldview]
  - id: S6
    type: primary
    kind: letter
    author: "Frida Kahlo (letter); Diego Rivera (reporter quote); Martha Zamora (editor)"
    citation: "Kahlo, Frida. Letter to Miguel Alemán Valdés, 20 Oct 1948, in Zamora, Martha. The Letters of Frida Kahlo: Cartas Apasionadas. English narrative and excerpts via Popova, Maria. \"Art, Atheism, and the Freedom of Expression: Frida Kahlo's Searing Protest Letter to the President of Mexico.\" The Marginalian, 3 Sep 2019. https://www.themarginalian.org/2019/09/03/frida-kahlo-miguel-aleman-letter/."
    url: "https://www.themarginalian.org/2019/09/03/frida-kahlo-miguel-aleman-letter/"
    accessed: 2026-10-24
    reliability_note: "Kahlo letter is primary (Zamora edition); Rivera atheist quote is Rivera's to a reporter, included as misattribution control. English via Marginalian."
    source_quality: "primary / own words"
    used_for: [worldview, review]
  - id: S7
    type: secondary
    kind: journal article
    author: "Holly Barnet-Sanchez"
    citation: "Barnet-Sanchez, Holly. \"Frida Kahlo: Her Life and Art Revisited.\" Latin American Research Review 32, no. 3 (1997): 243–257. https://doi.org/10.1017/S0023879100038152. PDF: Cambridge Core."
    url: "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/D9BCF0640DA98B7115154BD3E24D6DED/S0023879100038152a.pdf/frida-kahlo-her-life-and-art-revisited.pdf"
    accessed: 2026-10-24
    reliability_note: "Peer-reviewed review essay; read in full (PDF). Synthesizes Cooey 1994 and Lowe 1991 atheist labels; mother devout Catholic."
    source_quality: "scholarly edition or monograph"
    used_for: [childhood, worldview, heritage, review]
---

# Frida Kahlo

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Frida Kahlo (1907–1954), Mexican painter of self-portraits [S1][S3]. Deepen: primary_system BELOW_THRESHOLD (lead ATHE); A_locus BELOW_THRESHOLD; B_cause UNKNOWN; mid_basin UNKNOWN. Not plotted. The circulating "I am an atheist" line is Diego Rivera's [S6].

## Life and work

Bus accident 1925; taught herself to paint; married Rivera 1929 (divorced 1939, remarried 1940); taught at La Esmeralda 1943–54 [S1][S3].

## Contribution and impact

Self-portraits from 1926; Henry Ford Hospital / My Birth 1932; The Two Fridas 1939; Self-Portrait with Cropped Hair 1940; The Broken Column 1944 [S1][S3]. Louvre purchased The Frame (1939) [S1][S3].

## Childhood and education

Polio at six; National Preparatory School; mother devout Catholic ("fanatically religious" in Kahlo's characterization) [S1][S3][S7].

## Adult working worldview

Lane A (descriptive): no Kahlo-authored denial of God opened. Diary lists disagreement with "religions" among imperialism/fascism/capitalism [S4]. 1948 letter to Alemán is anti-sectarian, not a creed [S6]. Scholars call her an avowed/adamant atheist without quoting a God-denial [S7]. Rivera's 1948 atheist quote is his [S6]. A BELOW_THRESHOLD; B UNKNOWN (not a scientist; "one law = life" is not nature's causal order) [S4][S5]. mid_basin UNKNOWN.

## Heritage (context only)

German father; Mexican mother of Spanish and Indigenous descent; Catholic baptism/heritage [S1][S3][S7].

## Timing

First lasting contribution 1926, at 19; major-work period 1926–1944 (through Broken Column) [S1][S3].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Unclear; no geometric-form evidence.

## Open questions

- Abrams diary facsimile page/date for religions list and any God line.
- Zamora / Herrera for a Kahlo-authored denial of God.
- Cooey 1994 p.108 and Lowe 1991 primary citations behind "avowed"/"as an atheist".

## Research log

- 2026-10-15: Read Britannica; web search for her religious statements found only Rivera's quote.
- 2026-10-24: Deepen D1. Wikipedia EN; Marginalian diary politics + Alemán letter; DAM diary quotes; Barnet-Sanchez LARR PDF. A UNKNOWN→BELOW_THRESHOLD; B stays UNKNOWN; primary BELOW_THRESHOLD (lead ATHE). Chart still unplotted. No fallacy_catalog.
