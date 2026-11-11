---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch E; deepen D1 queue #28)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to 19c. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch E, order P32: F 5, rank 28). Basics from Britannica (Magnus). Worldview from The Joyful Wisdom (trans. Thomas Common, Levy ed., 1910; Gutenberg #52881) §§108, 109, 343 and Ecce Homo (trans. Anthony M. Ludovici, Levy ed., 1911; Gutenberg #52190). The madman of §125 and Zarathustra are characters and are not used. ATHE 0.7; A 4 (0.7); B 4 (0.7, P40); C 4 (0.5); D 4 (0.7); mid_basin false (0.7). Draft, not reviewed."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Audit fixes (fallacy_catalog audit of 2332880, run 1): B_cause 4 (0.7) kept; rationale ties P40 to the explicit exclusion of exceptions ('no one who transgresses') and chance; added the 'it also knows no law' statement. Gutenberg statements relabelled verified_against 'secondary quotation' (web copies); certainties already at the 0.7 web-copy cap, unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #28, next-50 batch). Need was B single-source. Added Kaufmann Gay Science (S5 scholarly edition; Stanford course PDF of Vintage Kaufmann/Hollingdale) — GS §§108–109 verified_against scholarly edition; Beyond Good and Evil §22 (S6; Zimmern via Gutenberg) and Twilight of the Idols 'Four Great Errors' close (S7; Ludovici via Gutenberg) as second and third B streams (necessary/calculable course without lawgiver; fatality / no causa prima). Wikipedia EN (S8) dual-sources bio. P47 source_quality on every source. A stays 4 @ 0.7 corroborated (S5+S3+S7); B stays 4 @ 0.7 P40, support single→corroborated (S5+S6+S7; alt BELOW_THRESHOLD). Chart-moving YES: hollow→filled (same dark cell). Major-work span end → 1888. No fallacy_catalog (Jason 2026-10-23/24). Draft, not reviewed."}

identity:
  id: nietzsche-friedrich
  display_name: "Friedrich Nietzsche"
  roster:
    canonical_name: "Friedrich Nietzsche"
    rank: 28
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: philosophy
    field_bucket: philosophy
  full_name: {value: "Friedrich Wilhelm Nietzsche", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S8, locator: "infobox; Youth"}], how_known: "Britannica names him after King Friedrich Wilhelm IV; Wikipedia gives full birth name Friedrich Wilhelm Nietzsche (later dropped the middle name). Dual source → 1.0."}
  native_name: {value: UNKNOWN, how_known: "German in Latin script; same as display name."}
  aliases:
    - {name: "Friedrich-Nietzsche", kind: "roster alias"}
    - {name: "Nietzsche-Friedrich", kind: "roster alias"}

basics:
  birth:
    date: {value: "1844-10-15", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "At a Glance; opening"}, {source: S8, locator: "infobox"}], how_known: "Britannica + Wikipedia EN."}
    place: {value: "Röcken, Saxony, Prussia", modern_name: "Röcken, Germany", polity_then: "Kingdom of Prussia", certainty: 1.0, cites: [{source: S1, locator: "At a Glance"}, {source: S8, locator: "infobox; Youth"}], how_known: "Britannica + Wikipedia EN."}
  death:
    date: {value: "1900-08-25", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "At a Glance"}, {source: S8, locator: "infobox"}], how_known: "Britannica + Wikipedia EN."}
    place: {value: "Weimar, Thuringian States", modern_name: "Weimar, Germany", polity_then: "German Empire", certainty: 1.0, cites: [{source: S1, locator: "At a Glance"}, {source: S8, locator: "infobox"}], how_known: "Britannica + Wikipedia EN (Grand Duchy of Saxe-Weimar-Eisenach)."}
  first_lasting_contribution_year: {value: 1872, certainty: 1.0, cites: [{source: S1, locator: "'Basel years' (Die Geburt der Tragödie, 1872)"}, {source: S8, locator: "Works"}], how_known: "Earliest listed lasting contribution (P13); dual source."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "'Basel years'"}, {source: S8, locator: "Works"}], how_known: "From 1872 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 1.0, cites: [{source: S1, locator: "At a Glance"}, {source: S8, locator: "Youth"}], how_known: "Germany (P3)."}
  region_of_work: {value: "Western Europe", certainty: 1.0, cites: [{source: S1, locator: "'Basel years'"}, {source: S8, locator: "Professor at Basel; Independent philosopher"}], how_known: "Basel, Switzerland, and Germany/Italy/France; Western Europe."}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S1, locator: "text"}, {source: S8, locator: "infobox"}], how_known: "As recorded."}
  languages_of_work: {value: [German], certainty: 1.0, cites: [{source: S1, locator: "German titles"}, {source: S8, locator: "Works"}], how_known: "Britannica + Wikipedia."}
  occupations: {value: ["classical philologist (professor at Basel)", "philosopher", "critic of culture"], certainty: 1.0, cites: [{source: S1, locator: "opening; 'Basel years'"}, {source: S8, locator: "lead; Professor at Basel"}], how_known: "Britannica + Wikipedia."}

contribution:
  era_bucket: 19c
  fields: {value: ["philosophy", "classical philology", "aesthetics"], certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S8, locator: "lead; Philosophy"}], how_known: "Britannica + Wikipedia."}
  lasting_original_contributions:
    - {value: "The Birth of Tragedy: the Apollonian and Dionysian account of Greek tragedy", year: 1872, kind: work, lasting: "'remains a classic in the history of aesthetics to this day' (S1)", certainty: 1.0, cites: [{source: S1, locator: "'Basel years'"}, {source: S8, locator: "Works"}], how_known: "Britannica + Wikipedia."}
    - {value: "Thus Spake Zarathustra", year: "1883–1885", kind: work, lasting: "'the first thorough statement of [his] mature philosophy'; influence 'considerable in the arts as well as philosophy' (S1)", certainty: 1.0, cites: [{source: S1, locator: "intro ('What did Friedrich Nietzsche write?', signed text)"}, {source: S8, locator: "Works"}], how_known: "Britannica + Wikipedia."}
    - {value: "Beyond Good and Evil; On the Genealogy of Morality; Twilight of the Idols; The Antichrist; Ecce Homo (late mature books)", year: "1886–1888", kind: work, lasting: "Core of the late published corpus; Genealogy and Twilight widely cited in the secondary literature (S8)", certainty: 0.7, cites: [{source: S8, locator: "Works; Independent philosopher"}], how_known: "Wikipedia Works list; Britannica names later works without dating them in the create-pass text."}
  evidence_of_impact:
    - {value: "'one of the most influential of all modern thinkers'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    - {value: "Wide impact on continental philosophy (existentialism, postmodernism, post-structuralism), arts and popular culture after the Kaufmann/Hollingdale rehabilitation", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S8, locator: "lead; Reception and legacy"}], how_known: "Wikipedia EN."}
  major_works:
    - {value: "Human, All-Too-Human", year: 1878, kind: book, certainty: 1.0, cites: [{source: S1, locator: "'Basel years'"}, {source: S8, locator: "Works"}], how_known: "Britannica + Wikipedia."}
    - {value: "The Gay Science (Die fröhliche Wissenschaft)", year: 1882, kind: book, certainty: 1.0, cites: [{source: S5, locator: "title page / Book III"}, {source: S8, locator: "Works"}], how_known: "Kaufmann edition + Wikipedia; Book V (§343) added in the second edition (1887)."}
    - {value: "Beyond Good and Evil", year: 1886, kind: book, certainty: 1.0, cites: [{source: S6, locator: "title"}, {source: S8, locator: "Works"}], how_known: "Primary text + Wikipedia."}
    - {value: "Twilight of the Idols", year: 1888, kind: book, certainty: 1.0, cites: [{source: S7, locator: "title; translator preface"}, {source: S8, locator: "Works"}], how_known: "Primary text + Wikipedia (written 1888; published early 1889)."}
  honours:
    - {value: "Doctorate conferred by Leipzig without examination", year: 1869, certainty: 0.7, cites: [{source: S1, locator: "'Basel years'"}], how_known: "Britannica; Wikipedia says honorary doctorate March 1869."}
  definition_fit: {value: "clearly meets", rationale: "Among the most influential modern thinkers.", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "Lutheran", certainty: 1.0, cites: [{source: S1, locator: "'Early years'"}, {source: S8, locator: "Youth"}], how_known: "Britannica: 'a stronghold of Lutheran piety'; Wikipedia: father a Lutheran pastor; long line of Lutheran clergy (Oehler genealogy note)."}
  family_religious_practice: {value: "Pious; father a pastor, both grandfathers clergy or Protestant writers", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}, {source: S8, locator: "Youth"}], how_known: "Britannica + Wikipedia."}
  parents_and_household:
    - {value: "Father, Carl Ludwig Nietzsche, pastor at Röcken; died 1849", name: "Carl Ludwig Nietzsche", role: father, certainty: 1.0, cites: [{source: S1, locator: "'Early years'"}, {source: S8, locator: "Youth"}], how_known: "Britannica + Wikipedia."}
    - {value: "Mother, Franziska (née Oehler)", name: "Franziska Nietzsche", role: mother, certainty: 1.0, cites: [{source: S1, locator: "'Early years'"}, {source: S8, locator: "Youth"}], how_known: "Britannica + Wikipedia."}
  household_circumstances: {value: "After 1849 a household of five women (mother, sister, grandmother, two aunts); moved to Naumburg 1850", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}, {source: S8, locator: "Youth"}], how_known: "Britannica + Wikipedia."}
  schooling:
    - {value: "Domgymnasium, Naumburg (private preparatory school)", stage: "grammar or secondary school", run_by: private, years: "1850–", ages: "6–", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
    - {value: "Schulpforta, Protestant boarding school", stage: "grammar or secondary school", run_by: "religious body", years: "1858–1864", ages: "14–20", certainty: 1.0, cites: [{source: S1, locator: "'Early years'"}, {source: S8, locator: "Youth"}], how_known: "Britannica + Wikipedia."}
    - {value: "Universities of Bonn (theology, philology) and Leipzig", stage: university, years: "1864–1869", ages: "20–25", certainty: 1.0, cites: [{source: S1, locator: "'Early years'"}, {source: S8, locator: "Youth; Education"}], how_known: "Britannica + Wikipedia; abandoned theology after one semester."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: TODO}
  notable_events:
    - {value: "Death of his father", year: 1849, age: 5, certainty: 1.0, cites: [{source: S1, locator: "'Early years'"}, {source: S8, locator: "Youth"}], how_known: "Britannica + Wikipedia."}
    - {value: "Loss of Christian faith while a student; letter to sister Elisabeth (June 1865) preferring inquiry to belief", year: 1865, age: 20, certainty: 0.7, cites: [{source: S8, locator: "Youth"}], how_known: "Wikipedia quotes the letter; off-point for adult axes (P29) but fills childhood/early adult religion."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1872–1888", certainty: 1.0, cites: [{source: S1, locator: "'Basel years'; intro"}, {source: S8, locator: "Works"}], how_known: "Equals timing.major_work_period (Birth of Tragedy through Twilight / Ecce Homo / Antichrist)."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "'I am quite unacquainted with atheism as a result, and still less as an event in my life: in me it is inborn, instinctive.' God is 'a coarse and rude prohibition of us: ye shall not think!' (Ecce Homo, 1888). De-deification of nature (GS §109).", certainty: 0.7, cites: [{source: S3, locator: "'Why I am so clever', §1"}, {source: S5, locator: "§109"}], how_known: "Own texts written for publication; EH in Ludovici via Gutenberg (0.7 web-copy); GS in Kaufmann scholarly edition."}
  primary_system:
    value: ATHE
    basis: written_profession
    certainty: 0.7
    cites: [{source: S5, locator: "§§108, 109"}, {source: S3, locator: "'Why I am so clever', §1"}, {source: S7, locator: "'The Four Great Errors' close"}]
    rationale: "Positive naturalism: 'God is dead' in his own voice (GS §108), atheism 'inborn, instinctive' (EH), call to complete the de-deification of nature (GS §109), and 'We deny God, we deny responsibility in God' (TI Four Great Errors). Not AGNOS (no suspension). Not PANT: he warns against thinking the world a living being and wants nature undeified (fails S6 part 1). NIHIL was considered; ATHE fits the metaphysics. Contested reception (Kaufmann and others read 'God is dead' culturally), so 0.7."
    how_known: "Kaufmann GS (S5) + EH Gutenberg (S3) + Twilight Gutenberg (S7). Madman §125 and Zarathustra not used (characters)."
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: ATHE, reason: "Chosen."}
    - {code: NIHIL, reason: "He diagnoses nihilism; his own metaphysics is naturalist, so not primary."}
    - {code: PANT, reason: "Rejected: 'nature entirely undeified' / de-deification of nature."}
  lio_axes:
    A_locus:
      value: 4
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S5, locator: "§108"}, {source: S3, locator: "'Why I am so clever', §1"}, {source: S7, locator: "'The Four Great Errors' close"}]
      rationale: "No separate God: 'God is dead' (GS §108, own voice); atheism as instinct (EH); 'We deny God' (TI). Scored as an explicit denial (§6). Contested cultural reading of 'God is dead' keeps 0.7."
      how_known: "Kaufmann GS + EH + Twilight. Madman (§125) is a character and is not used."
    B_cause:
      value: 4
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S5, locator: "§109"}, {source: S6, locator: "§22"}, {source: S7, locator: "'The Four Great Errors' close"}]
      rationale: "Account of nature (P6): GS §109 — 'There are only necessities: there is nobody who commands, nobody who obeys, nobody who trespasses'; no design and so no accident; chaos 'not of a lack of necessity but of a lack of order'. Explicitly rules out exceptions and chance (P40). BGE §22 agrees in a second work: the world has a 'necessary' and 'calculable' course 'NOT… because laws obtain in it, but because they are absolutely LACKING, and every power effects its ultimate consequences every moment'. Twilight Four Great Errors closes with fatality / piece of fate / no causa prima / innocence of Becoming. He rejects the word 'law' only as a lawgiver's command. Named alternative: BELOW_THRESHOLD if 'knows no law' / BGE §21's denial of necessity in being-in-itself is read as rejecting the lawful pole (P40). Contested, so 0.7. Three independent source ids → corroborated (P48)."
      how_known: "Kaufmann GS §109 (S5) + BGE §22 Zimmern (S6) + Twilight Ludovici (S7). Named alternative BELOW_THRESHOLD (P40)."
    C_ledger:
      value: 4
      basis: written_profession
      certainty: 0.5
      support: corroborated
      cites: [{source: S3, locator: "'Why I am so clever', §1"}, {source: S7, locator: "'The Four Great Errors' — free will / hangman metaphysics"}]
      rationale: "'\"God,\" \"the immortality of the soul,\" \"salvation,\" a \"beyond\"' are notions he 'never paid any attention' to (EH): no personal ledger. Twilight rejects guilt/punishment / 'metaphysics of the hangman'. Indirect on reward and punishment as a scored ledger, so 0.5. Two source ids → corroborated (P48)."
      how_known: "EH + Twilight; indirect."
    D_authority:
      value: 4
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S3, locator: "'Why I am so clever', §1"}, {source: S7, locator: "'The Four Great Errors' close"}]
      rationale: "God is 'a coarse and rude prohibition of us: ye shall not think!' (EH): religion keeps no domain of its own. Twilight: denying God / responsibility in God is 'the great deliverance'."
      how_known: "EH + Twilight, 0.7 web-copy / translation cap."
    E_scope: {value: UNKNOWN, how_known: "Scored on the world's order (P7); GS §109's 'exception' is astronomical, not an in-group exception; nothing else read."}
  mid_basin: {value: false, certainty: 0.7, cites: [{source: S5, locator: "§108"}], how_known: "A_locus 4 (≥ 3) at 0.7; this branch reads A only (P10)."}
  statements:
    - text: "God is dead; but given the way of men, there may still be caves for thousands of years in which his shadow will be shown. —And we—we still have to vanquish his shadow, too."
      cites: [{source: S5, locator: "§108"}, {source: S2, locator: "§108"}]
      date: "1882"
      context: "Aphorism 'New struggles', author's own voice (Kaufmann)."
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      axes: [A_locus]
      note: "Kaufmann translation (Vintage / Portable Nietzsche lineage) via Stanford course PDF of The Gay Science. Madman §125 not used."
    - text: "Let us beware of saying that there are laws in nature. There are only necessities: there is nobody who commands, nobody who obeys, nobody who trespasses. Once you know that there are no purposes, you also know that there is no accident; for it is only beside a world of purposes that the word 'accident' has meaning."
      cites: [{source: S5, locator: "§109"}]
      date: "1882"
      context: "Aphorism 'Let us beware', against anthropomorphising nature (Kaufmann)."
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      axes: [B_cause]
    - text: "The total character of the world, however, is in all eternity chaos—in the sense not of a lack of necessity but of a lack of order, arrangement, form, beauty, wisdom, and whatever other names there are for our aesthetic anthropomorphisms."
      cites: [{source: S5, locator: "§109"}]
      date: "1882"
      context: "Same aphorism (Kaufmann)."
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      axes: [B_cause]
    - text: "When will we complete our de-deification of nature? When may we begin to \"naturalize\" humanity in terms of a pure, newly discovered, newly redeemed nature?"
      cites: [{source: S5, locator: "§109"}]
      date: "1882"
      context: "Close of the same aphorism (Kaufmann)."
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      axes: [A_locus, B_cause]
    - text: "somebody might come along, who, with opposite intentions and modes of interpretation, could read out of the same \"Nature,\" and with regard to the same phenomena, just the tyrannically inconsiderate and relentless enforcement of the claims of power… and who should, nevertheless, end by asserting the same about this world as you do, namely, that it has a \"necessary\" and \"calculable\" course, NOT, however, because laws obtain in it, but because they are absolutely LACKING, and every power effects its ultimate consequences every moment."
      cites: [{source: S6, locator: "§22"}]
      date: "1886"
      context: "Beyond Good and Evil, 'Prejudices of Philosophers' §22, against physicists' 'Nature's conformity to law'."
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      axes: [B_cause]
      note: "Helen Zimmern translation, Complete Works (Levy) via Gutenberg #4363. Second independent B stream (different work from GS §109)."
    - text: "One is necessary, one is a piece of fate, one belongs to the whole, one is in the whole,—there is nothing that could judge, measure, compare, and condemn our existence, for that would mean judging, measuring, comparing and condemning the whole. But there is nothing outside the whole! … The concept \"God\" has been the greatest objection to existence hitherto.… We deny God, we deny responsibility in God: thus alone do we save the world."
      cites: [{source: S7, locator: "'The Four Great Errors' close"}]
      date: "1888"
      context: "Twilight of the Idols, end of 'The Four Great Errors' (free-will / innocence of Becoming)."
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      axes: [A_locus, B_cause, D_authority]
      note: "Ludovici translation, Levy Complete Works vol. 16, via Gutenberg #52263. Third B stream + A/D."
    - text: "I am quite unacquainted with atheism as a result, and still less as an event in my life: in me it is inborn, instinctive."
      cites: [{source: S3, locator: "'Why I am so clever', §1"}]
      date: "1888"
      context: "Ecce Homo, written 1888 for publication, published 1908."
      kind: "unpublished manuscript"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      axes: [A_locus, D_authority]
      note: "Ludovici translation, Levy edition 1911, via Gutenberg #52190. Supports A alongside the published GS §108 and TI."
  changes_over_life:
    - {value: "Lutheran household and theology study at Bonn (1864) before the working years; faith dropped by 1865 (letter to Elisabeth)", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}, {source: S8, locator: "Youth"}], how_known: "Childhood and student years; off-point for the axes (P29). EH says he never attended to God 'even as a child'."}
  coder_notes: "Coder's call: Zarathustra's and the madman's words are characters' words and are not used (task rule). B 4 rests on P40 (v8's pick); deepen adds BGE §22 and TI Four Great Errors as independent agreeing sources so support → corroborated. BGE §21 (denies necessity in being-in-itself) is the pressure behind the named BELOW_THRESHOLD alternative."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "German", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S8, locator: "Citizenship, nationality and ethnicity"}], how_known: "Britannica; Wikipedia notes later Polish-ancestry claims are rejected by modern scholars."}
  religious_heritage_by_birth: {value: "Lutheran", certainty: 1.0, cites: [{source: S1, locator: "'Early years'"}, {source: S8, locator: "Youth"}], how_known: "Britannica + Wikipedia."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1872–1888", certainty: 1.0, cites: [{source: S1, locator: "'Basel years'; intro"}, {source: S8, locator: "Works"}], how_known: "Birth of Tragedy (1872) through Twilight / Antichrist / Ecce Homo (1888) (P29, P30 #4)."}
  age_at_first_lasting_contribution: {value: 28, certainty: 1.0, cites: [{source: S1, locator: "At a Glance; 'Basel years'"}, {source: S8, locator: "infobox; Works"}], how_known: "1872 − 1844 = 28 (P30)."}
  first_evidence_of_lio_type_views: {value: "1882, age 38: 'God is dead' (§108) and 'There are only necessities' (§109)", year: 1882, age: 38, certainty: 0.7, cites: [{source: S5, locator: "§§108–109"}], how_known: "Kaufmann GS; earlier works (Birth of Tragedy, Human, All-Too-Human) not read for LIO in this pass — year now from the edition itself, 0.7."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.7, cites: [{source: S5, locator: "§§108–109"}, {source: S7, locator: "1888"}], how_known: "Within 1872–1888; reinforced in 1886–88 books."}
  worldview_during_major_work: {value: "ATHE", certainty: 0.7, cites: [{source: S5, locator: "§108"}, {source: S7, locator: "'We deny God'"}], how_known: "As coded."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Aphoristic, not definition-to-consequence.", certainty: 0.5, cites: [{source: S5, locator: "form of the work"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "'Early years'"}], how_known: "Classical schooling; nothing on proof."}
  circle_present: {value: "no", rationale: "Rejects the world as living being and wants nature undeified / de-deified.", certainty: 0.5, cites: [{source: S5, locator: "§109"}], how_known: "Coder's reading."}
  reading: "As belief, not finding: necessity-without-commander naturalism (P40) without geometric form or circle; BGE §22 and TI reinforce."
  notes: ""

institutions:
  - {value: "University of Basel", role: "professor of classical philology", years: "1869–1879", kind: university, certainty: 1.0, cites: [{source: S1, locator: "'Basel years'"}, {source: S8, locator: "Professor at Basel"}], how_known: "Britannica + Wikipedia."}
collaborators:
  - {value: "Richard Wagner", relation: other, note: "friend; friendship broken by 1878", certainty: 1.0, cites: [{source: S1, locator: "'Basel years'"}, {source: S8, locator: "Professor at Basel"}], how_known: "Britannica + Wikipedia."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 28"}], how_known: "Study roster."}
  controversies:
    - {value: "His name was later invoked by fascists for aims he loathed; sister Elisabeth's editions associated him with nationalism/antisemitism he opposed", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S8, locator: "lead; Reception"}], how_known: "Britannica + Wikipedia."}
  data_quality_flags:
    - "GS §§108–109 now checked against Kaufmann scholarly edition (S5); BGE and Twilight still Levy-era translations via Gutenberg (0.7 cap)."
    - "BGE §21 (denies necessity in being-in-itself) is the pressure behind B's named BELOW_THRESHOLD alternative; value kept at 4 under P40."
  open_questions:
    - "Optional: check BGE §22 and TI Four Great Errors against Kaufmann/Hollingdale or KSA for page numbers; Antichrist for further A statements."
    - "C_ledger still 0.5 / effectively single — EH + TI hangman metaphysics could be deepened later."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Bernd Magnus"
    citation: "Magnus, Bernd. \"Friedrich Nietzsche.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Friedrich-Nietzsche."
    url: "https://www.britannica.com/biography/Friedrich-Nietzsche"
    accessed: 2026-10-15
    reliability_note: "Signed article body."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, heritage, timing, institutions, collaborators, review]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Friedrich Nietzsche"
    year: 1882
    citation: "Nietzsche, Friedrich. The Joyful Wisdom (La Gaya Scienza). Trans. Thomas Common. Complete Works, vol. 10, ed. Oscar Levy. 1910. Project Gutenberg eBook #52881."
    url: "https://www.gutenberg.org/ebooks/52881"
    accessed: 2026-10-15
    reliability_note: "Older authorised translation, web copy; create-pass quotes. Deepen re-checked §§108–109 against Kaufmann (S5); S2 kept as concordant unofficial web copy."
    source_quality: "unofficial web copy"
    used_for: [worldview]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "Friedrich Nietzsche"
    year: 1888
    citation: "Nietzsche, Friedrich. Ecce Homo. Trans. Anthony M. Ludovici. Complete Works, vol. 17, ed. Oscar Levy. 1911. Project Gutenberg eBook #52190."
    url: "https://www.gutenberg.org/ebooks/52190"
    accessed: 2026-10-15
    reliability_note: "Web copy; 0.7 cap."
    source_quality: "unofficial web copy"
    used_for: [worldview]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S5
    type: primary
    kind: "scholarly edition"
    author: "Friedrich Nietzsche; Walter Kaufmann (trans./ed.)"
    year: 1974
    citation: "Nietzsche, Friedrich. The Gay Science. Trans. Walter Kaufmann with Bernard Guingand Hollingdale notes lineage. Vintage / Portable Nietzsche text as reproduced in Stanford University course PDF (jsabol/existentialism materials)."
    url: "https://web.stanford.edu/~jsabol/existentialism/materials/nietzsche-gay-science-hurry.pdf"
    accessed: 2026-10-24
    reliability_note: "Kaufmann scholarly translation; PDF is a course scan of the published edition pages. Used to lift GS §§108–109 to verified_against scholarly edition."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview, contribution, timing, lane_b]
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "Friedrich Nietzsche"
    year: 1886
    citation: "Nietzsche, Friedrich. Beyond Good and Evil. Trans. Helen Zimmern. Complete Works, ed. Oscar Levy. Project Gutenberg eBook #4363."
    url: "https://www.gutenberg.org/ebooks/4363"
    accessed: 2026-10-24
    reliability_note: "Older authorised translation, web copy; 0.7 cap. §22 used as second independent B stream."
    source_quality: "unofficial web copy"
    used_for: [worldview, contribution]
  - id: S7
    type: primary
    kind: "published work by the subject"
    author: "Friedrich Nietzsche"
    year: 1888
    citation: "Nietzsche, Friedrich. The Twilight of the Idols (with The Antichrist). Trans. Anthony M. Ludovici. Complete Works, vol. 16, ed. Oscar Levy. 1911. Project Gutenberg eBook #52263."
    url: "https://www.gutenberg.org/ebooks/52263"
    accessed: 2026-10-24
    reliability_note: "Web copy; 0.7 cap. 'Four Great Errors' close used for A/B/D."
    source_quality: "unofficial web copy"
    used_for: [worldview, contribution, timing]
  - id: S8
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "\"Friedrich Nietzsche.\" Wikipedia, The Free Encyclopedia. https://en.wikipedia.org/wiki/Friedrich_Nietzsche."
    url: "https://en.wikipedia.org/wiki/Friedrich_Nietzsche"
    accessed: 2026-10-24
    reliability_note: "Used for dual-source bio, Works list, sister-edition controversy; not for LIO scores."
    source_quality: "other"
    used_for: [identity, basics, contribution, childhood, heritage, timing, institutions, collaborators, review]
---

# Friedrich Nietzsche

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Friedrich Nietzsche (1844–1900), German philologist and philosopher; The Birth of Tragedy (1872), Thus Spake Zarathustra (1883–85), Beyond Good and Evil (1886), Twilight of the Idols (1888) [S1, S8]. In his own voice: 'God is dead' [S5, §108]; 'There are only necessities' [S5, §109]; necessary/calculable course without laws [S6, §22]; 'We deny God' [S7]; atheism 'inborn, instinctive' [S3]. Draft: ATHE 0.7 corroborated; A 4 at 0.7 corroborated; B 4 at 0.7 corroborated (P40); D 4 at 0.7; mid_basin false at 0.7.

## Life and work

Schulpforta, Bonn, Leipzig; professor at Basel 1869–79; independent writer to 1888; collapse 1889 [S1, S8].

## Contribution and impact

Birth of Tragedy; Zarathustra; late books through 1888 [S1, S8].

## Childhood and education

Pastor's son in a pious Lutheran home; dropped theology/faith by 1865 [S1, S8].

## Adult working worldview

Atheist naturalism; necessity without a commander (GS §109; BGE §22; TI) [S5, S6, S7, S3].

## Heritage (context only)

German Lutheran [S1, S8].

## Timing

First lasting contribution 1872, at 28; major work through 1888 [S1, S8].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No form, no circle [S5].

## Open questions

- Kaufmann/KSA page-check for BGE §22 and TI; optional Antichrist A deepen.
- C_ledger still soft at 0.5.

## Research log

- 2026-10-15: Read Britannica; searched Gutenberg #52881 and #52190.
- 2026-10-24: Deepen D1 — Kaufmann GS PDF (Stanford); Gutenberg BGE #4363 §22; Gutenberg Twilight #52263 Four Great Errors; Wikipedia EN dual-source bio. B support single→corroborated. No fallacy_catalog.
