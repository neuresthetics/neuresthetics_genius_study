---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch G; deepen D1 queue #44)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch G, order P32: F 5, rank 44). Basics from Britannica (Emery). Worldview evidence: one marginal note in his Calov Bible (2 Chronicles 5:13), read only as quoted on the Bach studies site (bach-studies.wursten.be); his lifelong Lutheran church posts (S1). primary_system CHRIST at 0.5 (inferred from work and conduct, P24); A BELOW_THRESHOLD; B, C, D, E UNKNOWN; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #44). Need was A BELOW_THRESHOLD; B UNKNOWN. P47 source_quality on S1–S7. Calov 2 Chr 5:13 note verified against Wikimedia Commons facsimile of Concordia Seminary page (S4); wording matches (Bey einer andächtigen Musiq… Gnaden Gegenwart). Baptism 1685-03-23 OS Georgenkirche Eisenach from Bach-Dokumente II Nr. 1 via jsbach.de (S5). Wikipedia (S6) dual-sources birth/death and reports Small Catechism teaching + Calov. Concordia Seminary Bach Bible page (S7) authenticates ownership/ink. A stays BELOW_THRESHOLD (names personal God of grace; does not place God in/above/as Nature — Debussy parallel). B stays UNKNOWN after research (not a scientist, P16; no own-words law/exception statement; cantata nature-Ordnung lines are Franck libretti, P42). mid_basin UNKNOWN. CHRIST @ 0.5 unchanged. Chart-moving NO — still unplotted. Thoroughbass precepts left unused (P42 disputed authorship). No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: bach-johann-sebastian
  display_name: "Johann Sebastian Bach"
  roster:
    canonical_name: "Johann Sebastian Bach"
    rank: 44
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: music
    field_bucket: music
  full_name: {value: "Johann Sebastian Bach", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "lead"}], how_known: "Britannica and Wikipedia agree."}
  native_name: {value: "Johann Sebastian Bach", certainty: 0.7, cites: [{source: S6, locator: "lead"}], how_known: "German in Latin script; Wikipedia lead form."}
  aliases:
    - {name: "Bach-Johann Sebastian", kind: "roster alias"}
    - {name: "Johann-Sebastian-Bach", kind: "roster alias"}

basics:
  birth:
    date: {value: "1685-03-21", calendar: julian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "infobox; Youth and education"}], how_known: "Britannica and Wikipedia agree: 21 March 1685 O.S. / 31 March N.S. Protestant Thuringia used Julian until 1700, so source date kept as julian (data dictionary)."}
    place: {value: "Eisenach, Thuringia", modern_name: "Eisenach, Germany", polity_then: "Ernestine Saxon Duchies (Saxe-Eisenach)", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "infobox"}], how_known: "Two sources agree."}
  death:
    date: {value: "1750-07-28", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening; 'Last years'"}, {source: S6, locator: "infobox; Death and burial"}], how_known: "Two sources agree."}
    place: {value: "Leipzig", modern_name: "Leipzig, Germany", polity_then: "Electorate of Saxony", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "infobox"}], how_known: "Two sources agree."}
  first_lasting_contribution_year: {value: 1708, certainty: 0.5, cites: [{source: S1, locator: "'The Mühlhausen period'"}, {source: S6, locator: "Weimar, Arnstadt, and Mühlhausen"}], how_known: "Cantata No. 71, Gott ist mein König, 1708, first published composition (S1); Wikipedia: only extant Bach cantata published in his lifetime. Earlier works dated only by ascription with less certainty (S1), so year might be earlier (0.5)."}
  era_bucket: {value: "1600 to 1749", certainty: 0.7, cites: [{source: S1, locator: "'The Mühlhausen period'"}], how_known: "From 1708 (P2); any earlier work also falls in the bucket."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Germany is Western Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "career sections"}, {source: S6, locator: "career sections"}], how_known: "Arnstadt, Mühlhausen, Weimar, Köthen, Leipzig."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [German, Latin], certainty: 0.5, cites: [{source: S1, locator: "text"}, {source: S6, locator: "Music (Latin church music)"}], how_known: "German posts and texts; Latin church music (Mass in B minor, Magnificat). Not a self-report (0.5)."}
  occupations: {value: ["composer", "organist", "Kapellmeister", "cantor"], certainty: 0.7, cites: [{source: S1, locator: "career sections"}, {source: S6, locator: "infobox"}], how_known: "Britannica and Wikipedia."}

contribution:
  fields: {value: ["music"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Cantata No. 71, Gott ist mein König, his first published composition", year: 1708, kind: work, lasting: "first of the cantata output (S1)", certainty: 0.7, cites: [{source: S1, locator: "'The Mühlhausen period'"}, {source: S6, locator: "Weimar, Arnstadt, and Mühlhausen"}], how_known: "Two sources."}
    - {value: "Brandenburg Concertos", year: 1721, kind: work, lasting: "among the works he is 'celebrated as the creator of' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; 'The Köthen period'"}, {source: S6, locator: "lead"}], how_known: "Finished by 24 March 1721 (S1)."}
    - {value: "The Well-Tempered Clavier, Book 1", year: 1722, kind: work, lasting: "named in Britannica's lead (S1)", certainty: 0.7, cites: [{source: S1, locator: "'The Köthen period'"}, {source: S6, locator: "lead"}], how_known: "Two sources."}
    - {value: "St. Matthew Passion", year: 1729, kind: work, lasting: "(S1)", certainty: 0.7, cites: [{source: S1, locator: "'Symbolism'"}, {source: S6, locator: "Cantata cycle years"}], how_known: "Wikipedia notes first performance Good Friday 11 April 1727 in recent research; Britannica 1729 retained as listed lasting year with note."}
    - {value: "The Musical Offering", year: 1747, kind: work, lasting: "(S1)", certainty: 0.7, cites: [{source: S1, locator: "'Last years'"}, {source: S6, locator: "Final years"}], how_known: "Two sources; The Art of the Fugue unfinished/posthumous (1751), so period ends at 1747 (P30)."}
  evidence_of_impact:
    - {value: "'generally regarded as one of the greatest composers of all time'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    - {value: "Acclaimed as one of the greatest composers in the history of Western music", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S6, locator: "lead"}], how_known: "Wikipedia lead."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Canonical composer (S1, S6).", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "lead"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Lutheran", certainty: 0.7, cites: [{source: S1, locator: "opening (Veit Bach, 'a Lutheran baker'); 'Early years'"}, {source: S5, locator: "Georgenkirche baptism entry"}, {source: S6, locator: "Youth and education"}], how_known: "Ancestor Veit Bach Lutheran (S1); infant baptism in Eisenach Georgenkirche (S5); Protestant church posts in family (S6)."}
  family_religious_practice: {value: "Lutheran parish worship at Eisenach Georgenkirche; father city and court musician there; great-uncle Johann Christoph Bach organist", certainty: 0.7, cites: [{source: S5, locator: "Georgenkirche page context"}, {source: S1, locator: "'Early years'"}, {source: S6, locator: "Youth and education"}], how_known: "Baptism and family posts at St George's; Britannica on early church context."}
  parents_and_household:
    - {value: "Father Johann Ambrosius Bach, string player for the town council and ducal court; mother Elisabeth (Maria Elisabeth) Lämmerhirt; both dead by 1695", role: parents, certainty: 1.0, cites: [{source: S1, locator: "'Early years'"}, {source: S6, locator: "Youth and education"}], how_known: "Two sources agree (Wikipedia names Maria Elisabeth née Lämmerhirt)."}
    - {value: "Eldest brother Johann Christoph, organist at Ohrdruf, took him in", role: guardian, certainty: 1.0, cites: [{source: S1, locator: "'Early years'"}, {source: S6, locator: "Youth and education"}], how_known: "Two sources agree."}
  household_circumstances: {value: "Orphaned by 1695 (age 10)", certainty: 1.0, cites: [{source: S1, locator: "'Early years'"}, {source: S6, locator: "Youth and education"}], how_known: "Two sources agree."}
  schooling:
    - {value: "School at Eisenach (Lateinschule)", stage: "grammar or secondary school", run_by: "state or municipal", years: "1692 or 1693–1695", ages: "7–10", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}, {source: S6, locator: "Youth and education"}], how_known: "Britannica; Wikipedia Lateinschule / Gymnasium."}
    - {value: "Lyceum / Gymnasium at Ohrdruf with brother Johann Christoph", stage: "grammar or secondary school", run_by: "state or municipal", years: "1695–1700", ages: "10–15", certainty: 0.7, cites: [{source: S6, locator: "Youth and education"}], how_known: "Wikipedia: theology, Latin, Greek at local Gymnasium; Bach-Dokumente school years (via secondary)."}
    - {value: "School at the Michaelskirche, Lüneburg (choir of poor boys)", stage: "grammar or secondary school", run_by: "religious body", years: "1700–1702", ages: "15–17", certainty: 1.0, cites: [{source: S1, locator: "'Early years'"}, {source: S6, locator: "Youth and education (St Michael's School from 3 April 1700)"}], how_known: "Two sources agree."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "Johann Christoph Bach (brother), first formal keyboard lessons", certainty: 1.0, cites: [{source: S1, locator: "'Early years'"}, {source: S6, locator: "Youth and education"}], how_known: "Two sources agree."}
  languages_in_childhood: {value: [German, Latin], certainty: 0.5, cites: [{source: S6, locator: "Youth and education (Latin and Greek at Gymnasium)"}], how_known: "Inferred from Gymnasium curriculum (S6); Greek not listed as work language."}
  notable_events:
    - {value: "Both parents dead", year: 1695, age: 10, certainty: 1.0, cites: [{source: S1, locator: "'Early years'"}, {source: S6, locator: "Youth and education"}], how_known: "Two sources agree."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1708–1747", certainty: 0.5, cites: [{source: S1, locator: "career sections"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Lutheran church (official posts as organist and cantor; taught Luther's Small Catechism as Thomaskantor)", certainty: 0.7, cites: [{source: S1, locator: "'The Arnstadt period'; 'Years at Leipzig'"}, {source: S6, locator: "Creative range (Small Catechism)"}], how_known: "Britannica church posts; Wikipedia on teaching Luther's Small Catechism in Leipzig."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing read on science and religion."}
  primary_system:
    value: CHRIST
    basis: inference_from_work
    certainty: 0.5
    cites: [{source: S1, locator: "'The Arnstadt period'; 'Years at Leipzig'"}, {source: S4, locator: "2 Chronicles 5:13 marginal note (facsimile)"}, {source: S2, locator: "four music annotations summary"}, {source: S6, locator: "Creative range (Calov; Small Catechism)"}, {source: S7, locator: "ownership and ink analysis"}]
    rationale: "Lifelong Lutheran church musician (S1, S6); own-hand Calov note that God is always present with his grace in devotional music (S4, verified facsimile); further Calov music glosses treat church music as God-pleasing and Spirit-ordered (S2). Conduct and private notes, so inference_from_work at 0.5 (P24). No statement on revelation, so DEISM is not in play (P27). Named alternative BELOW_THRESHOLD if private notes are treated as too weak for a system code."
    how_known: "Inferred from posts and verified Calov annotations; facsimile S4 upgrades S2's secondary quotation for the 2 Chronicles note."
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Chosen at 0.5: Lutheran posts, Calov Gnadengegenwart note, Spirit-ordered music gloss."}
    - {code: CLTHEI, reason: "Not chosen: the annotations speak of God's gracious presence and ordering of worship music, not intervention in worldly events."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, note: "Calov note (S4/S2) names Gott and Gnadengegenwart in devotion music — a personal God of grace — but does not place God relative to the world (in / above / as Nature). Other Calov music glosses (God-pleasing church music; music ordered by God's Spirit) likewise assume a personal God without a locus claim. Debussy parallel: naming God without locating → BELOW_THRESHOLD. Named reading: 0 (transcendent person) if a scholar's reconstruction of Lutheran locus is accepted as backing (P18 private + scholar → 0.5).", how_known: "BELOW_THRESHOLD under P19 (implication / indirect). Facsimile verification does not change the axis gap."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P16, P30). Researched 2026-10-24: Britannica, Wikipedia, Calov music annotations, Bach studies pages — no Bach own-words statement on nature's causal order (law vs exception). Cantata lines on Natur/Ordnung (e.g. BWV 17) are librettist Salomo Franck's text, not Bach's voice (P42). Thoroughbass 'glory of God' precepts unused (P42 disputed authorship / Niedt)."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read that scores C."}
    D_authority: {value: UNKNOWN, how_known: "Nothing read that scores D; Small Catechism teaching is office duty, not a revelation-vs-observation claim."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7)."}
  mid_basin: {value: UNKNOWN, how_known: "B_cause is UNKNOWN, which takes precedence (§6, P19); A_locus is BELOW_THRESHOLD."}
  statements:
    - text: "NB. Bey einer andächtigen Musiq ist allzeit Gott mit seiner Gnaden Gegenwart."
      cites: [{source: S4, locator: "Wikimedia Commons facsimile of Concordia Seminary Calov page, 2 Chr 5:13 margin"}, {source: S2, locator: "'II Chron 5:13' entry"}, {source: S7, locator: "handwriting and ink analysis"}]
      context: "Marginal note in his copy of Abraham Calov's Bible commentary, beside 2 Chronicles 5:13 (the cloud filling the temple as the priests make music). English sense: when devout/devotional music is performed, God is always present with his gracious presence."
      axes: [A_locus]
      kind: "document in own hand"
      verified_against: "primary facsimile"
      verified_on: 2026-10-24
      note: "Verified 2026-10-24 against Wikimedia Commons File:Bach_Calov-Bibel_2_Chr_5,13.jpg (source Concordia Seminary). Spelling on the page image: Musiq, allzeit, Gnaden Gegenwart (hyphenated line break). S2 and Wikipedia use allezeit / Gnadengegenwart variants; sense identical. Date of the note not established. Authenticity of Bach's hand/ink: Concordia Seminary (S7)."
    - text: "NB. Dieses Capitel ist das wahre Fundament aller Gottgefälligen Kirchen Music. etc."
      cites: [{source: S2, locator: "1 Chronicles 25[26] entry"}]
      context: "Calov marginal gloss at 1 Chronicles 25: this chapter is the true foundation of all church music that pleases God."
      axes: [A_locus]
      kind: "document in own hand"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Secondary quotation only (S2); facsimile not opened for this page. Supports personal God who can be pleased; not a locus placement."
    - text: "Ein herrlicher Beweiß, daß neben anderen Anstalten des Gottesdienstes, besonders auch die Musica von Gottes Geist durch David mit angeordnet worden."
      cites: [{source: S2, locator: "1 Chronicles 28[29] entry"}]
      context: "Calov gloss: splendid proof that music too was specially ordered by God's Spirit through David."
      axes: [A_locus]
      kind: "document in own hand"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Secondary quotation only (S2). Personal God / Spirit ordering worship; not a nature-order (B) claim."
  changes_over_life: []
  coder_notes: "Deepen D1 2026-10-24: A stays BELOW_THRESHOLD despite facsimile-verified Calov note — names personal God, does not locate (Debussy parallel). B UNKNOWN after failed nature-statement search. CHRIST at 0.5 from posts + notes. Thoroughbass precepts (Niedt/P42) and SDG manuscript headings left unused for axes (formula / disputed authorship). Still unplotted; not chart-moving."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "German (Thuringian musical family)", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "Youth and education"}], how_known: "Two sources."}
  religious_heritage_by_birth: {value: "Lutheran", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "baptism entry"}], how_known: "Lutheran family context and infant baptism in Georgenkirche."}
  baptism_or_initiation: {value: "Baptized 1685-03-23 (Julian) at Georgenkirche (St George's), Eisenach — church-book entry 'G. Sebastian' son of Johann Ambrosius Bach; sponsors Nagel and Johann Georg Koch", certainty: 0.7, cites: [{source: S5, locator: "Bach-Dokumente II Nr. 1 (transcription)"}, {source: S6, locator: "Youth and education (Eisenach birth)"}], how_known: "jsbach.de prints BD II Nr. 1 church-book text; Wikipedia confirms Eisenach birth two days earlier. Register image not fetched."}
  childhood_catechism: {value: TODO, how_known: "Adult teaching of Luther's Small Catechism as Thomaskantor is documented (S6) but is not childhood catechism."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1708–1747", certainty: 0.5, cites: [{source: S1, locator: "'The Mühlhausen period'; 'Last years'"}], how_known: "1708 to 1747, first to last listed lasting contribution (P29, P30); the start year might be earlier (0.5)."}
  age_at_first_lasting_contribution: {value: 23, certainty: 0.5, cites: [{source: S1, locator: "opening; 'The Mühlhausen period'"}], how_known: "1708 − 1685 = 23 (P30); start year at 0.5."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "Calov notes assume a personal God but do not score A/B; no dated LIO-type locus/cause claim."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S4, locator: "2 Chr 5:13 note"}], how_known: "Calov notes are devotion/music theology, not LIO axis placements."}
  worldview_during_major_work: {value: "CHRIST", certainty: 0.5, cites: [{source: S1, locator: "'Years at Leipzig'"}, {source: S4, locator: "Calov note"}], how_known: "As primary_system."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Fugue and canon are rule-governed forms (S1, S6), but that is music, not geometry.", certainty: 0.5, cites: [{source: S1, locator: "'The Köthen period'"}, {source: S6, locator: "Counterpoint"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "'Early years'"}], how_known: "Nothing on mathematics."}
  circle_present: {value: "unclear", rationale: "No statement locating God relative to nature.", certainty: 0.5, cites: [{source: S4, locator: "Calov note"}], how_known: "Coder's reading."}
  reading: "No mid-basin reading possible: A BELOW_THRESHOLD, B UNKNOWN. Lutheran church musician with private notes on God's gracious presence in music; no account of nature's causal order."
  notes: "Lane B only. Do not treat fugue craft as geometric-form evidence for H1."

institutions:
  - {value: "Thomaskirche and Thomasschule, Leipzig", role: "cantor and director of church music", years: "1723–1750", kind: "religious body", certainty: 1.0, cites: [{source: S1, locator: "'Years at Leipzig'"}, {source: S6, locator: "Appointment"}], how_known: "Two sources agree."}
  - {value: "Court of Prince Leopold of Anhalt-Köthen", role: "Kapellmeister / musical director", years: "1717–1723", kind: "employer", certainty: 1.0, cites: [{source: S1, locator: "'The Köthen period'"}, {source: S6, locator: "Köthen"}], how_known: "Two sources agree."}
collaborators:
  - {value: "Johann Matthias Gesner", relation: other, note: "rector of the Thomasschule, an admirer", certainty: 0.7, cites: [{source: S1, locator: "'Nonmusical duties'"}], how_known: "Britannica."}
  - {value: "Picander (Christian Friedrich Henrici)", relation: collaborator, note: "librettist, St Matthew Passion", certainty: 0.7, cites: [{source: S6, locator: "Structure and lyrics"}], how_known: "Wikipedia."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 44"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags: []
  open_questions:
    - "Read Leaver (ed.), J. S. Bach and Scripture (Concordia, 1985) or Van Wijnen 2017 facsimile set for all Calov glosses in scholarly apparatus; Steiger on Gnadengegenwart."
    - "Wolff, Johann Sebastian Bach: The Learned Musician — second biography for basics and any locus/cause statements."
    - "New Bach Reader (David/Mendel/Wolff) for SDG/JJ headings in citable transcription; keep P42 in view for thoroughbass precepts."
    - "Any Bach own-words remark on nature, Ordnung of the physical world, miracle, or providence (would open B / CLTHEI)."
    - "Childhood catechism practice (as distinct from adult Small Catechism teaching)."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Walter Emery"
    citation: "Emery, Walter. \"Johann Sebastian Bach.\" Encyclopaedia Britannica, updated 25 August 2026. https://www.britannica.com/biography/Johann-Sebastian-Bach."
    url: "https://www.britannica.com/biography/Johann-Sebastian-Bach"
    accessed: 2026-10-15
    source_quality: "reference entry"
    reliability_note: "Signed article body; the Top Questions box is not used. Not re-fetched 2026-10-24 (Britannica often Cloudflare-blocked); prior read retained."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "Bach studies (bach-studies.wursten.be)"
    citation: "\"Bach's annotations in Calov's Bible commentary.\" Bach studies. https://bach-studies.wursten.be/bachs-annotations/."
    url: "https://bach-studies.wursten.be/bachs-annotations/"
    accessed: 2026-10-24
    source_quality: "other"
    reliability_note: "Personal research site collecting Calov markings with translations; not peer-reviewed. Used for the three other music glosses (1 Chron 25, 1 Chron 28, Exodus 15) in secondary quotation. The 2 Chronicles note is now also verified on facsimile S4."
    used_for: [worldview]
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
    type: primary
    kind: "archive record"
    author: "Johann Sebastian Bach"
    citation: "Bach, Johann Sebastian. Marginal note at 2 Chronicles 5:13 in his copy of Abraham Calov, Die heilige Bibel… (Wittenberg, 1681–82). Concordia Seminary Library, St. Louis. Facsimile image: Wikimedia Commons File:Bach_Calov-Bibel_2_Chr_5,13.jpg (from http://bach.csl.edu/media/calov)."
    url: "https://commons.wikimedia.org/wiki/File:Bach_Calov-Bibel_2_Chr_5,13.jpg"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "Photographic facsimile of the Concordia Seminary page. Handwriting/ink authenticity established by Concordia analysis (S7). Page image read 2026-10-24; transcription checked against the visible margin note."
    used_for: [worldview]
  - id: S5
    type: secondary
    kind: "scholarly book"
    author: "Werner Neumann and Hans-Joachim Schulze (eds.)"
    year: 1969
    citation: "Neumann, Werner, and Hans-Joachim Schulze, eds. Bach-Dokumente, Band 2: Fremdschriftliche und gedruckte Dokumente zur Lebensgeschichte Johann Sebastian Bachs, 1685–1750. Kassel: Bärenreiter, 1969, Nr. 1 (Taufe, Eisenach Georgenkirche, 23.3.1685). Transcription quoted at https://jsbach.de/bachs-welt/dokumente/1685-23-maerz-eisenach-taufe-johann-sebastian-bachs-der-georgenkirche."
    url: "https://jsbach.de/bachs-welt/dokumente/1685-23-maerz-eisenach-taufe-johann-sebastian-bachs-der-georgenkirche"
    accessed: 2026-10-24
    source_quality: "scholarly edition or monograph"
    reliability_note: "Critical edition of documents; jsbach.de reprints BD II Nr. 1 church-book text. Register image not fetched; citation follows the printed BD number."
    used_for: [heritage, childhood]
  - id: S6
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "\"Johann Sebastian Bach.\" Wikipedia. https://en.wikipedia.org/wiki/Johann_Sebastian_Bach (accessed 2026-10-24)."
    url: "https://en.wikipedia.org/wiki/Johann_Sebastian_Bach"
    accessed: 2026-10-24
    source_quality: "other"
    reliability_note: "Used for dual-sourcing basics, Calov caption quote, Small Catechism teaching, career outline. Not used alone for worldview axis scores."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S7
    type: secondary
    kind: "institutional page"
    author: "Concordia Seminary Library"
    citation: "\"Bach Bible.\" Kristine Kay Hasse Memorial Library, Concordia Seminary, St. Louis. https://library.csl.edu/rare-and-special-collections/bach-bible/."
    url: "https://library.csl.edu/rare-and-special-collections/bach-bible/"
    accessed: 2026-10-24
    source_quality: "other"
    reliability_note: "Holding library: ~25 marginal annotations; handwriting and 1980s ink analysis establish Bach ownership. Supports authenticity of S4."
    used_for: [worldview]
---

# Johann Sebastian Bach

> Status: draft — unreviewed. primary_system CHRIST at 0.5; A BELOW_THRESHOLD; B UNKNOWN; mid_basin UNKNOWN. Not plotted.

## Summary

Johann Sebastian Bach (1685–1750), German Baroque composer and organist: Brandenburg Concertos, The Well-Tempered Clavier, St. Matthew Passion, Mass in B Minor [S1; S6]. Lifelong Lutheran church musician [S1; S6]. Own-hand Calov Bible note: God is always present with his grace in devout music [S4]. Draft: CHRIST at 0.5; A BELOW_THRESHOLD (names God, does not locate); B UNKNOWN (no nature statement); mid_basin UNKNOWN. Not plotted.

## Life and work

Born Eisenach 21 March 1685 O.S.; baptized Georgenkirche 23 March [S5; S6]. Arnstadt, Mühlhausen, Weimar, Köthen; Thomaskantor at Leipzig from 1723 [S1; S6]. Died Leipzig 28 July 1750 [S1; S6].

## Contribution and impact

Cantatas, Passions, keyboard and orchestral works; among the greatest Western composers [S1; S6].

## Childhood and education

Eisenach Lateinschule; orphaned 1695; Ohrdruf with brother Johann Christoph; Lüneburg Michaelskirche school from 1700 [S1; S6]. Lutheran parish household at Georgenkirche [S5].

## Adult working worldview

Lutheran posts as organist and cantor; taught Luther's Small Catechism in Leipzig [S1; S6]. In his Calov Bible he wrote that when devout music is performed God is always present with his gracious presence [S4]. Further Calov glosses call a Chronicles chapter the foundation of God-pleasing church music and say music was ordered by God's Spirit through David [S2]. Coding: CHRIST at 0.5 (inference from posts and notes, P24). A BELOW_THRESHOLD — the notes name a personal God of grace but do not place God relative to the world. B UNKNOWN — not a scientist; no own-words account of nature's law vs exception found (librettist lines and disputed thoroughbass precepts excluded, P42). mid_basin UNKNOWN.

## Heritage (context only)

Thuringian Lutheran musical family [S1; S6]. Baptized Georgenkirche Eisenach 23 March 1685 O.S. [S5].

## Timing

First lasting contribution 1708 (first published cantata), at 23 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Fugue/canon craft is music, not geometric-form evidence. No circle statement (God vs nature). No mid-basin reading while A is BELOW_THRESHOLD and B is UNKNOWN [S1; S4].

## Open questions

- Leaver / Van Wijnen facsimile apparatus for all Calov glosses; Steiger on Gnadengegenwart.
- Wolff *Learned Musician*; New Bach Reader for SDG/JJ in citable form.
- Any own-words nature / providence / miracle statement (would open B / CLTHEI).
- Childhood catechism (vs adult Small Catechism teaching).

## Research log

- 2026-10-15: Read Britannica (Emery); the Bach studies annotation page; search excerpts on the Calov note (not cited).
- 2026-10-24 (deepen D1, queue #44): Verified 2 Chr 5:13 note on Wikimedia Commons Concordia facsimile (S4); Concordia ownership page (S7); Bach-Dokumente baptism via jsbach.de (S5); Wikipedia dual-source (S6); re-read Bach studies four music annotations (S2). Searched for nature/law/miracle own words — none found usable under P16/P42. P47 on S1–S7. A/B/mid_basin status unchanged; not chart-moving. No fallacy_catalog.
