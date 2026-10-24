---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch M; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-17
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-17, by: "Grok Bot", summary: "Record created (stage 3 batch M, order P32: F 5, rank 78). Basics from Britannica (Britannica Editors, unsigned; body only, Q&A boxes not cited). Worldview from letters 155 (1880), 613, 632 and 691 (1888) in the Van Gogh Museum / Huygens ING edition. primary_system BELOW_THRESHOLD; A 0 (0.5, alt 1); B UNKNOWN (P16); mid_basin UNKNOWN (P19). Not plotted. Draft, not reviewed."}
    - {date: 2026-10-17, by: "Grok Bot", summary: "Batch M audit fixes (/workspace/genius_study_audit/gs_159d60d_M/run1/, run 1: 16 hold, 3 weaken): letter 632 added to A's cites; the irony in letter 613 marked plainly as the coder's reading. Value unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #77, F5 rank 78). Needs: A single source; A faded; B UNKNOWN. Primaries: Van Gogh Museum / Huygens ING letters re-verified via Wayback 2020 snapshots of translation pages (S2: 574, 613, 632, 673, 691); Complete Letters / webexhibits older EN of CL 490 (=613) and W01 (=574) as independent translation stream (S5); Patrick Grant Reading Vincent van Gogh (AU Press) scholarly monograph quoting Jansen edition (S4); Wikipedia EN dual bio (S6, P50) with Britannica create-pass body retained (S1). P47 on S1–S7. A 0 @0.5 support single→corroborated (S2+S5 on letter 613; alt 1 kept and strengthened by letter 673 'do without the dear Lord' + 691 religion/stars). Cert stays 0.5 (contested: legend/irony framing of 613 + 673 + named alt 1) — faded not cleared. B stays UNKNOWN (P16/P33: not a scientist; letter 574 providence agnosticism is about personal help/consolation, not nature's causal order; 'wrestle with nature' / beauties-of-nature lines are artistic method). C UNKNOWN→1 @0.5 corroborated (632 eternal life as principal certainty + 613 hope of another life; alt UNKNOWN). D UNKNOWN→3 @0.5 single (632 Bible pettiness / Christ-as-kernel; 574 reject sentimental providence tales; 673 do without dear Lord). primary_system stays BELOW (CHRIST/CLTHEI/DEISM still partly fit; churchless; 673 loosens conventional theism). mid_basin UNKNOWN (B UNKNOWN, P19). Span stays 1888–1890. Chart-moving NO (still unplottable; B UNKNOWN). No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: van-gogh-vincent
  display_name: "Vincent van Gogh"
  roster:
    canonical_name: "Vincent van Gogh"
    rank: 78
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: art
    field_bucket: arts
  full_name: {value: "Vincent Willem van Gogh", certainty: 0.7, cites: [{source: S1, locator: "header / opening"}, {source: S6, locator: "infobox birth_name"}], how_known: "Britannica and Wikipedia (P50)."}
  native_name: {value: UNKNOWN, how_known: "Dutch in Latin script."}
  aliases:
    - {name: "Van Gogh-Vincent", kind: "roster alias"}
    - {name: "Vincent-van-Gogh", kind: "roster alias"}

basics:
  birth:
    date: {value: "1853-03-30", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "infobox"}], how_known: "Two sources."}
    place: {value: "Zundert, Netherlands", modern_name: "Zundert, Netherlands", polity_then: "Netherlands", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "Early years (Groot-Zundert)"}], how_known: "Two sources."}
  death:
    date: {value: "1890-07-29", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "infobox"}], how_known: "Two sources."}
    place: {value: "Auvers-sur-Oise, near Paris, France", modern_name: "Auvers-sur-Oise, France", polity_then: "France", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "infobox"}], how_known: "Two sources."}
  first_lasting_contribution_year: {value: 1888, certainty: 0.5, cites: [{source: S1, locator: "'The productive decade' (Arles)"}, {source: S6, locator: "Arles (1888–89)"}], how_known: "The Arles works of 1888 'marked his first great period' (S1): the earliest work the body marks as lasting (P13). Weavers (1884) and The Potato Eaters (1885) are dated but not marked lasting. 0.5 because the choice is the coder's."}
  era_bucket: {value: "1850 to 1949", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "From 1888 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Netherlands (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S6, locator: "Life"}], how_known: "Netherlands, Belgium, France."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [Dutch, French], certainty: 0.7, cites: [{source: S2, locator: "letters 613, 632, 673"}, {source: S6, locator: "Letters"}], how_known: "Letters to Theo (Dutch and French) and Bernard (French)."}
  occupations: {value: ["painter", "art dealer's employee (Goupil)", "lay preacher and evangelist"], certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}, {source: S6, locator: "Early years / Emerging artist"}], how_known: "Two sources."}

contribution:
  fields: {value: ["painting", "drawing"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Arles paintings (orchards, sunflowers, portraits of Roulin, the house)", year: 1888, kind: work, lasting: "'marked his first great period' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'The productive decade'"}, {source: S6, locator: "Arles (1888–89)"}], how_known: "Two sources."}
    - {value: "The Starry Night", year: 1889, kind: work, lasting: "in the Museum of Modern Art, New York (S1)", certainty: 0.7, cites: [{source: S1, locator: "'The productive decade' (Saint-Rémy; image caption)"}, {source: S6, locator: "notable_works"}], how_known: "Two sources."}
  evidence_of_impact:
    - {value: "'a powerful influence on the Expressionist movement in modern art'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "'generally considered one of the greatest of the Post-Impressionists' (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Dutch Reformed (father a minister of the Dutch Reformed Church)", certainty: 0.7, cites: [{source: S6, locator: "Early years"}, {source: S1, locator: "'Early life' (Protestant pastor)"}], how_known: "Wikipedia names the denomination; Britannica 'Protestant pastor'."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Eldest surviving of six children of Theodorus van Gogh, Dutch Reformed minister, and Anna Cornelia Carbentus", role: father, certainty: 0.7, cites: [{source: S6, locator: "Early years"}, {source: S1, locator: "'Early life'"}], how_known: "Two sources."}
  household_circumstances: {value: TODO}
  schooling:
    - {value: "Village school; boarding school Zevenbergen (1864); middle school Tilburg (1866–1868)", stage: "grammar or secondary school", run_by: other, certainty: 0.7, cites: [{source: S6, locator: "Early years"}], how_known: "Wikipedia."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [Dutch], certainty: 0.5, cites: [{source: S1, locator: "'Early life'"}], how_known: "Coder's reading (Brabant village)."}
  notable_events:
    - {value: "Apprenticed at 16 to Goupil and Co., The Hague", age: 16, certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}, {source: S6, locator: "Early years"}], how_known: "Two sources."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1888–1890", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Dutch Reformed upbringing; trained as an evangelist, dismissed by church authorities (1879–80)", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}, {source: S6, locator: "Early years"}], how_known: "Britannica: dismissed 'for a too-literal interpretation of Christian teaching'. Context, not a code."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing read that sets science against religion as such."}
  primary_system:
    value: BELOW_THRESHOLD
    basis: consistent_private_letters
    certainty: 0.5
    cites: [{source: S2, locator: "letters 613, 632, 673, 691"}, {source: S4, locator: "Ch. 1 quotes of 613, 632, 673"}, {source: S5, locator: "CL 490 / W01"}]
    rationale: "Churchless theist language in the Arles letters without a system that fits cleanly: God as 'Good Lord' / 'creative hand' (613), Christ as 'principal certainty' of eternal life (632), yet 'I can easily do without the dear Lord' while needing 'something greater… the power to create' (673) and a 'tremendous need… for religion' expressed by painting stars (691). CHRIST, CLTHEI and DEISM all partly fit; the church had dismissed him (S1). Cap 0.5 (named alternatives + contested conventional-theism reading)."
    how_known: "Several private letters in the working years (consistent_private_letters). Scholarly monograph (S4) and older Complete Letters stream (S5) agree on the same passages."
    alternatives:
      - {value: CHRIST, note: "Christ-centred 632; no church after 1880.", cites: [{source: S2, locator: "letter 632"}]}
      - {value: CLTHEI, note: "God as creative hand who may take 'revenge' (613).", cites: [{source: S2, locator: "letter 613"}]}
      - {value: DEISM, note: "A God judged by his botched world-study (613); no P27 revelation rejection read.", cites: [{source: S2, locator: "letter 613"}]}
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Christ as the 'principal certainty' of eternal life (632); but outside any church after 1880, and 673 loosens 'dear Lord'."}
    - {code: CLTHEI, reason: "God as 'the same creative hand' who may take 'revenge' (613)."}
    - {code: DEISM, reason: "A God who made the world and then is judged by it (613); no rejection of revelation read (P27)."}
    - {code: AGNOS, reason: "574 'I definitely don't know what to make of' providence — suspension about intervention, not about God-as-author; not chosen as primary."}
  lio_axes:
    A_locus:
      value: 0
      basis: consistent_private_letters
      certainty: 0.5
      support: corroborated
      cites: [{source: S2, locator: "letter 613 (Arles, 26 May 1888)"}, {source: S5, locator: "CL 490 / webexhibits 18/490.htm (same letter, older EN)"}, {source: S2, locator: "letter 632"}]
      how_known: "Private letters in the working years; letter 632 backs letter 613 as earnest theist language. Support corroborated (P48): Jansen edition (S2) + independent Complete Letters / webexhibits EN (S5) agree on the God-as-author reading of 613. Held at 0.5 (not 0.7): (a) 613 is framed as 'legend' and can read as ironic (coder's reading; edition does not flag irony); (b) letter 673 same span 'I can easily do without the dear Lord' contests conventional personal theism; (c) named alt 1. Faded cue unchanged."
      rationale: "God as the world's author, apart from it: 'we shouldn't judge the Good Lord by this world, because it's one of his studies that turned out badly' and 'the same creative hand' (1888). Named alternative: 1 — knowing God by love (155, before span), 'something greater than myself, which is my life, the power to create' (673), and painting stars from a 'tremendous need… for religion' (691)."
      alternatives:
        - {value: 1, note: "Immanent / creative-power reading of 673+691+155; God known by love or as 'something on high' rather than a separate judge.", cites: [{source: S2, locator: "letters 673, 691, 155"}]}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist under P30/P33: lasting contributions are paintings, not theories about natural systems. For a non-scientist, B needs an explicit remark on the order of nature (P16). Letter 574 (Paris, late 1887) refuses the belief that 'powers above us intervene personally to help us or to comfort us' and calls providence 'such a strange thing' he does not know what to make of it — about personal consolation, not nature's causal law (same caution as Austen's petitionary-prayer addendum in reverse). Letter 613's 'world… cobbled together in haste' judges the world's quality, not law vs exception. 'Wrestle with nature' / beauties-of-nature lines are pictorial method (Rembrandt/Picasso pattern). Deliberately not scored."}
    C_ledger:
      value: 1
      basis: consistent_private_letters
      certainty: 0.5
      support: corroborated
      cites: [{source: S2, locator: "letter 632"}, {source: S2, locator: "letter 613"}, {source: S4, locator: "Ch. 1 quotes of 632 and 613"}]
      how_known: "Two Arles letters + scholarly monograph quotation. 0.5: hope and Christ's 'principal certainty' of eternal life, not a detailed personal judgment schedule; named alt UNKNOWN (create-pass left C unscored as hope only)."
      rationale: "Christ 'declared eternal life – the endlessness of time, the non-existence of death – to be the principal certainty' (632); 'hope of seeing better than that in another life' (613). Personal continuity / afterlife lean without a mapped heaven–hell ledger (same direction as CHRIST system C 1; thinner than Dostoevsky's immortality-for-virtue argument)."
      alternatives:
        - {value: UNKNOWN, note: "If hope-without-judgment is left unscored (create-pass reading).", cites: [{source: S2, locator: "letter 613"}]}
    D_authority:
      value: 3
      basis: consistent_private_letters
      certainty: 0.5
      support: single
      cites: [{source: S2, locator: "letters 632, 574, 673"}]
      how_known: "Private letters cluster (single edition stream for the D value → support single). 0.5: still finds Christ as the Bible's consoling kernel; not a full naturalist D 4."
      rationale: "Rejects sentimental providence tales and personal intervention-to-console (574); the Bible 'stirs up our despair' by its 'pettiness and its contagious folly' yet the kernel is Christ (632); 'I can easily do without the dear Lord' (673). Reason/experience over dogmatic consolation. Still participates in religious need (691)."
    E_scope: {value: UNKNOWN, how_known: "Not a scientist; no statement on same laws everywhere (P7)."}
  mid_basin: {value: UNKNOWN, how_known: "B is UNKNOWN; UNKNOWN takes precedence (P19). A 0 @0.5 would not clear the mid-basin ≥0.7 bar anyway (P10)."}
  statements:
    - text: "I'm thinking more and more that we shouldn't judge the Good Lord by this world, because it's one of his studies that turned out badly."
      cites: [{source: S2, locator: "letter 613, to Theo van Gogh, Arles, 26 May 1888"}, {source: S5, locator: "CL 490 / webexhibits 18/490.htm"}]
      date: "1888-05-26"
      context: "To Theo; the letter goes on: 'What legend tells us about the Good Lord is that he went to enormous trouble over this study of his for a world. I'm inclined to believe that the legend tells the truth' and hopes for 'revenge taken by the same creative hand' / 'better than that in another life'."
      axes: [A_locus, C_ledger]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Jansen/Luijten/Bakker English via Wayback 2020 snapshot of vangoghletters.org translation page; wording cross-checked against Complete Letters / webexhibits older EN (S5)."
    - text: "Christ — alone — among all the philosophers, magicians, &c. declared eternal life – the endlessness of time, the non-existence of death – to be the principal certainty."
      cites: [{source: S2, locator: "letter 632, to Emile Bernard, Arles, 26 June 1888"}, {source: S4, locator: "Ch. 1 (27)"}]
      date: "1888-06-26"
      context: "To Bernard; follows a critique of the Bible's 'pettiness' with Christ as the consoling kernel. 'That's serious, you know, especially because it's the truth.'"
      axes: [A_locus, C_ledger, D_authority]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Wayback 2020 of vangoghletters.org; AU Press quotes the same Jansen wording."
    - text: "In life and in painting too, I can easily do without the dear Lord, but I can't, suffering as I do, do without something greater than myself, which is my life, the power to create."
      cites: [{source: S2, locator: "letter 673, to Theo van Gogh, Arles, 3 September 1888"}, {source: S4, locator: "Ch. 1 (21)"}, {source: S5, locator: "CL 531 / webexhibits 18/531.htm"}]
      date: "1888-09-03"
      context: "To Theo; continues that he wants to paint consoling portraits with 'that je ne sais quoi of the eternal' once symbolized by the halo."
      axes: [A_locus, D_authority]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Named as the main contest to A 0 / conventional theism; supports alt 1."
    - text: "That doesn't stop me having a tremendous need for, shall I say the word — for religion — so I go outside at night to paint the stars"
      cites: [{source: S2, locator: "letter 691, to Theo van Gogh, Arles, on or about 29 September 1888"}]
      date: "1888-09-29"
      context: "To Theo."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "As above."
    - text: "I feel uneasy about assuming for my own use or recommending to others for theirs the belief that powers above us intervene personally to help us or to comfort us. Providence is such a strange thing, and I tell you that I definitely don't know what to make of it."
      cites: [{source: S2, locator: "letter 574, to Willemien van Gogh, Paris, late October 1887"}, {source: S5, locator: "webexhibits letter/17/W01.htm"}, {source: S4, locator: "Ch. 1 (19)"}]
      date: "1887-10"
      context: "To sister Willemien, shortly before the Arles span; about her literary piece on plants and rain / providence tales."
      axes: [D_authority]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Checked for B and left off B (P16): about personal help/consolation, not nature's causal order. Adult-life evidence near the span (P31)."
    - text: "But without intending it, I'm always inclined to believe that the best way of knowing God is to love a great deal."
      cites: [{source: S2, locator: "letter 155, to Theo van Gogh, Cuesmes, c. 22–24 June 1880"}]
      date: "1880-06"
      context: "To Theo, after his dismissal as an evangelist; before the working years (P20)."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-17
      note: "Kept as alt-1 context; create-pass verification retained."
  changes_over_life:
    - {value: "Dismissed as an evangelist; Britannica: 'feeling that his faith was destroyed' (winter 1879–80). Early letters (e.g. 117, 1877) affirm living God; post-Borinage conventional Christian citations drop (S4). Arles 1888: churchless theist/Christ language with 'do without the dear Lord' (673) and religion-as-painting-stars (691).", year: 1880, age: 27, certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}, {source: S4, locator: "Ch. 1 religion section"}, {source: S2, locator: "letters 673, 691"}], how_known: "Britannica + Grant synthesis + own letters."}
  coder_notes: "Deepen D1: A support single→corroborated (S2+S5); cert stays 0.5 (faded not cleared — 613 irony + 673 contest + alt 1). B deliberately UNKNOWN (574 providence ≠ P16 nature order). C newly 1 @0.5; D newly 3 @0.5 single. Chart-moving NO. Lane A scores separate from Lane B geometric labels. No fallacy_catalog (Jason)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Dutch", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "lead"}], how_known: "Two sources."}
  religious_heritage_by_birth: {value: "Dutch Reformed (son of a Dutch Reformed minister)", certainty: 0.7, cites: [{source: S6, locator: "Early years"}, {source: S1, locator: "'Early life'"}], how_known: "Wikipedia names the denomination."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1888–1890", certainty: 0.5, cites: [{source: S1, locator: "'The productive decade'"}, {source: S6, locator: "Arles through Auvers"}], how_known: "First listed lasting contribution (1888) to his death (P29, P30); start is the coder's pick."}
  age_at_first_lasting_contribution: {value: 35, certainty: 0.5, cites: [{source: S1, locator: "opening; Arles 1888"}], how_known: "1888 − 1853 = 35 (P30)."}
  first_evidence_of_lio_type_views: {value: "1888", certainty: 0.5, cites: [{source: S2, locator: "letters 613, 632"}], how_known: "First scored A≤1 evidence in the working years; earlier theist letters (1877–80) are before the span and after the evangelist crisis (P20/P31)."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.7, cites: [{source: S2, locator: "letters 613, 632, 673, 691"}], how_known: "Arles letters 1888 inside 1888–90 span."}
  worldview_during_major_work: {value: "Churchless theist / Christ-centred language with contested conventional 'dear Lord': God as world's author (613), Christ as certainty of eternal life (632), yet can 'do without the dear Lord' for creative power (673) and seeks religion in painting stars (691).", certainty: 0.5, cites: [{source: S2, locator: "letters 613, 632, 673, 691"}], how_known: "Private letters, 1888."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "Post-Impressionist colour/contour structure; not a Euclidean ideal geometry as worldview.", certainty: 0.5, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "Style and works"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Nothing read that dates a geometric theology."}
  circle_present: {value: "unclear", rationale: "God as maker / creative hand; hope of another life; no clear return-to-source circle.", certainty: 0.5, cites: [{source: S2, locator: "letter 613"}], how_known: "Coder's reading."}
  reading: "Churchless theist in the Arles letters; religion relocated into painting and 'something greater' (creative power)."
  notes: "Lane B separate from Lane A axis scores."

institutions:
  - {value: "Goupil and Co. (The Hague, London, Paris)", role: employee, years: "1869–1876", kind: other, certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}, {source: S6, locator: "Early years"}], how_known: "Two sources."}
collaborators:
  - {value: "Theo van Gogh", relation: family, note: "brother and main correspondent", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "Letters"}], how_known: "Two sources."}
  - {value: "Émile Bernard", relation: correspondent, note: "painter; letter 632 on Christ/eternal life", certainty: 0.7, cites: [{source: S2, locator: "letter 632"}, {source: S6, locator: "Letters"}], how_known: "Two sources."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 78"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "vangoghletters.org live pages require JavaScript; S2 translations re-verified from Wayback Machine 2020 snapshots of the official translation URLs (2026-10-24)."
    - "A stays faded (0.5): letter 613 legend/irony contest + letter 673 'do without the dear Lord' + named alt 1."
    - "B left UNKNOWN after checking letter 574 providence and nature-as-art letters (P16)."
  open_questions:
    - "Morgan Library Bernard letter facsimiles / full Strauss-style print volumes for independent transcription of 632 beyond Wayback HTML."
    - "Any explicit own-words remark on nature's causal order (laws, miracles in nature) that would score B under P16."
    - "Baptism / Dutch Reformed membership records."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "Britannica Editors. \"Vincent van Gogh.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Vincent-van-Gogh. Read in Wayback snapshots: main page 2026-09-22 02:13:55 UTC; 'The productive decade' 20260217004628; 'Legacy' 20260922021354."
    url: "https://www.britannica.com/biography/Vincent-van-Gogh"
    accessed: 2026-10-17
    source_quality: "reference entry"
    reliability_note: "Unsigned editors' article (JSON-LD author 'Britannica Editors'). Body only; Q&A boxes and Top Questions not cited. Create-pass body retained this deepen (P50 dual with Wikipedia)."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: primary
    kind: scholarly edition
    author: "Vincent van Gogh"
    citation: "Van Gogh, Vincent. Vincent van Gogh – The Letters, ed. Leo Jansen, Hans Luijten and Nienke Bakker. Amsterdam and The Hague: Van Gogh Museum and Huygens ING. https://vangoghletters.org/vg/ (letters 155, 574, 613, 632, 673, 691). Deepen re-verify: Wayback Machine 2020 snapshots of /vg/letters/letNNN/translation.html for 574, 613, 632, 673, 691 (live site JS-gated 2026-10-24)."
    url: "https://vangoghletters.org/vg/"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "Critical edition with the editors' English translation; letter numbers are the edition's. Live pages require JS; English checked against Wayback HTML of the official translation URLs."
    used_for: [basics, worldview, timing, lane_b, collaborators]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-17
    source_quality: "study roster"
    reliability_note: "Study's own roster."
    used_for: [identity, review]
  - id: S4
    type: secondary
    kind: "scholarly book"
    author: "Patrick Grant"
    citation: "Grant, Patrick. Reading Vincent van Gogh: A Thematic Guide to the Letters. Edmonton: Athabasca University Press. Chapter One: Shaping Commitments (Religion), quoting Jansen edition letters 574, 613, 632, 673, 691. https://read.aupress.ca/read/reading-vincent-van-gogh/section/3eec3b0d-f538-42d4-b08e-bcdefdda89f1"
    url: "https://read.aupress.ca/read/reading-vincent-van-gogh/section/3eec3b0d-f538-42d4-b08e-bcdefdda89f1"
    accessed: 2026-10-24
    source_quality: "scholarly edition or monograph"
    reliability_note: "Scholarly monograph; long quotations of the Jansen English with letter numbers. Used to corroborate wording and for Grant's synthesis of the post-Borinage shift."
    used_for: [worldview, timing]
  - id: S5
    type: primary
    kind: scholarly edition
    author: "Vincent van Gogh"
    citation: "Van Gogh, Vincent. The Complete Letters of Vincent van Gogh (older English tradition), via WebExhibits. Letter CL 490 = Jansen 613 (https://www.webexhibits.org/vangogh/letter/18/490.htm); CL 531 = Jansen 673 (https://www.webexhibits.org/vangogh/letter/18/531.htm); W01 = Jansen 574 (https://www.webexhibits.org/vangogh/letter/17/W01.htm)."
    url: "https://www.webexhibits.org/vangogh/"
    accessed: 2026-10-24
    source_quality: "unofficial web copy"
    reliability_note: "Older Complete Letters English (van Gogh-Bonger / related tradition), not the Jansen critical translation. Independent translation stream for P48 corroboration of A (613/490) and cross-check of 574/673. Capped as unofficial web copy."
    used_for: [worldview]
  - id: S6
    type: secondary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "\"Vincent van Gogh.\" Wikipedia. https://en.wikipedia.org/wiki/Vincent_van_Gogh (lead/infobox; Early years; Letters; Arles)."
    url: "https://en.wikipedia.org/wiki/Vincent_van_Gogh"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Featured article; dual bio with Britannica (P50). Used for full name, Dutch Reformed father, schooling, dates — not for LIO scores."
    used_for: [identity, basics, contribution, childhood, heritage, timing, lane_b, institutions, collaborators]
  - id: S7
    type: secondary
    kind: other
    author: "Steven Naifeh and Gregory White Smith"
    citation: "Naifeh, Steven, and Gregory White Smith. Van Gogh: The Life. New York: Random House, 2011. Secondary quotation of letter 613 via While Reading and Walking / review excerpts; full volume unread this pass."
    url: "https://en.wikipedia.org/wiki/Van_Gogh:_The_Life"
    accessed: 2026-10-24
    source_quality: "scholarly edition or monograph"
    reliability_note: "Major biography; used only as a lead. Full text unread; letter wording taken from S2/S5 instead."
    used_for: [review]
---

# Vincent van Gogh

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Vincent van Gogh (1853–1890), Dutch Post-Impressionist painter [S1; S6]. Deepen D1: primary_system BELOW_THRESHOLD; A 0 @0.5 corroborated (alt 1); B UNKNOWN; C 1 @0.5; D 3 @0.5 single; mid_basin UNKNOWN. Chart-moving NO (still unplottable).

## Life and work

Goupil; lay preacher and evangelist; painter from ~1880; Arles 1888; Saint-Rémy 1889; Auvers 1890 [S1; S6].

## Contribution and impact

Arles works of 1888, his 'first great period'; The Starry Night (1889) [S1; S6].

## Childhood and education

Son of Dutch Reformed minister Theodorus van Gogh, Brabant; Zevenbergen / Tilburg schooling [S6; S1].

## Adult working worldview

'we shouldn't judge the Good Lord by this world, because it's one of his studies that turned out badly' (1888) [S2; S5]. 'I can easily do without the dear Lord…' (1888) [S2; S5]. Christ as 'principal certainty' of eternal life (1888) [S2; S4].

## Heritage (context only)

Dutch, Dutch Reformed pastor's family [S1; S6].

## Timing

First lasting contribution 1888, at 35 [S1]. LIO-type letters during major work (Arles 1888) [S2].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Partly geometric (colour/contour); circle unclear.

## Open questions

- Explicit P16 nature-order own words for B (Naifeh & Smith *Van Gogh: The Life* unread cover-to-cover) [S7].
- Morgan / print critical transcriptions beyond Wayback HTML.
- Baptism / membership records.

## Research log

- 2026-10-17: Read Britannica (Editors) in Wayback copies; read letters 155, 613, 632 and 691 on vangoghletters.org.
- 2026-10-24: Deepen D1. Live vangoghletters.org JS-gated; re-verified 574/613/632/673/691 via Wayback 2020 translation pages [S2]. Webexhibits Complete Letters 490/531/W01 [S5]. AU Press Grant Ch. 1 [S4]. Wikipedia EN dual bio [S6]. Naifeh/Smith lead only [S7].
