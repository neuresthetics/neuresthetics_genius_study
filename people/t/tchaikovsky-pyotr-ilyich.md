---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA8; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen D1 (queue #199/228, F 3, rank 212). Goals: letters own words if any; keep silence if none; do not force plot. Music/liturgy subject alone does not score A or religion. Read: Tchaikovsky Research Letter 633 (30 Oct/11 Nov 1877 von Meck — reason rejects Orthodox/Christian dogmas; pantheistic future life; still turns to Christ in prayer); Letter 659 (23 Nov/5 Dec 1877 von Meck — poetic church bonds / Liturgy & Vigil as artistic delight; lost dogmas; pantheistic eternity of nature; convinced no eternal life vs instinct for mother); Letter 5046 (26 Sept/8 Oct 1893 to K.R. — rejects God the Judge/Avenger; still 'creator and source of all blessings'; dreams of Gospel 'Come unto me'). Wikipedia EN bio (P50 dual bio; Cyrillic native name) + Religious views page (secondary; scholars disagree Sizko vs Zakharova — not used to force a code). P47 source_quality on S1–S7. primary_system UNKNOWN → BELOW_THRESHOLD (leads CHRIST, PANT; no listed code fits; Liturgy Op.41 / Vigil Op.52 are works not profession). A UNKNOWN → BELOW_THRESHOLD (mixed A 0–1 Christ-prayer/creator vs A 4 pantheistic nature; neither ≥0.5). B stays UNKNOWN (not a scientist, P30; pantheistic eternity remark is afterlife/locus, not P16 nature-law). C/D BELOW_THRESHOLD leads only; E UNKNOWN; mid BELOW. first_evidence 1877. Chart-moving NO (still unplotted). No fallacy_catalog. No figures/. Draft, not reviewed."}
    - {date: 2026-10-20, by: "Grok Bot", summary: "AA8 audit fixes: premiere days labelled Old Style (4 March 1877 and 28 October 1893 New Style); 1880 revision of Romeo and Juliet noted."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA8, order P32: F 3, rank 212). Source: Britannica, signed by Alexander Poznansky (scholars edition, read in full). Lasting work: Romeo and Juliet (completed 1869; first performed 1870), 'the first of Tchaikovsky's compositions eventually to enter the standard international classical repertoire'; his ballets, beginning with Swan Lake (premiere 20 February 1877 Old Style, 4 March New Style), with which 'he revolutionized the genre'; and the Symphony No. 6 (Pathétique; premiere 16 October 1893 Old Style, 28 October New Style), 'his most celebrated masterpiece' (S1). Dated by first performance (RQ-Z7-N1 analogue); S1's day dates are Old Style (Russian calendar); years are unaffected (P12). Romeo and Juliet's repertoire version is the 1880 revision; the 1870 premiere is still the first public statement of the work. Span 1870–1893, age 30. Worldview: S1 says the von Meck correspondence discussed 'religious faith', but no own words on belief are quoted. primary_system UNKNOWN; A UNKNOWN; not a scientist; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}

identity:
  id: tchaikovsky-pyotr-ilyich
  display_name: "Pyotr Ilyich Tchaikovsky"
  roster:
    canonical_name: "Pyotr Ilyich Tchaikovsky"
    rank: 212
    F: 3
    models: [Claude, DeepSeek, Grok]
    band: "core (3–4)"
    status: "core"
    field: "music"
    field_bucket: "music"
  full_name: {value: "Pyotr Ilyich Tchaikovsky", certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S3, locator: "lead"}], how_known: "Britannica + Wikipedia EN (P50 dual bio)."}
  native_name: {value: "Пётр Ильич Чайковский", certainty: 0.7, cites: [{source: S3, locator: "infobox / note 1"}], how_known: "Wikipedia EN Cyrillic; Britannica (S1) prints Latin forms only."}
  aliases:
    - {name: "Peter Ilich Tchaikovsky", kind: "transliteration"}
    - {name: "Chaikovsky", kind: "transliteration"}

basics:
  birth:
    date: {value: "1840-05-07", certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S3, locator: "infobox"}], how_known: "Britannica: April 25 Old Style, May 7 New Style; Wikipedia EN agrees (P50)."}
    place: {value: "Votkinsk", modern_name: "Votkinsk, Russia", polity_then: "Russian Empire", certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S3, locator: "infobox"}], how_known: "Britannica + Wikipedia EN (P50)."}
  death:
    date: {value: "1893-11-06", certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S3, locator: "infobox"}], how_known: "Britannica: October 25 Old Style, November 6 New Style; Wikipedia EN agrees (P50)."}
    place: {value: "St. Petersburg", modern_name: "Saint Petersburg, Russia", polity_then: "Russian Empire", certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S3, locator: "infobox"}], how_known: "Britannica + Wikipedia EN (P50)."}
  first_lasting_contribution_year: {value: 1870, certainty: 0.7, cites: [{source: S1, locator: "Middle years"}], how_known: "Romeo and Juliet completed 1869; 'Nikolay Rubinstein conducted a successful performance of this work the following year' (S1): first performance 1870 (P30)."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "Middle years"}], how_known: "1870 (P2)."}
  region_of_birth: {value: "Eastern Europe", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Russia (P3)."}
  region_of_work: {value: "Eastern Europe", certainty: 0.7, cites: [{source: S1, locator: "Middle years; Final years"}], how_known: "Moscow, Klin, St. Petersburg."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Russian"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Russian letters and operas."}
  occupations: {value: ["composer", "conductor", "teacher"], certainty: 0.7, cites: [{source: S1, locator: "Middle years; Final years"}], how_known: "Britannica."}

contribution:
  fields: {value: ["music"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Romeo and Juliet (fantasy overture)", year: 1870, kind: "work", lasting: "'the first of Tchaikovsky's compositions eventually to enter the standard international classical repertoire' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Middle years"}], how_known: "Completed 1869; first performed 1870 (S1; 4/16 March 1870, Old/New Style). The version in the repertoire is the 1880 revision."}
    - {value: "Ballets (Swan Lake, The Sleeping Beauty, The Nutcracker)", year: 1877, kind: "body of work", lasting: "'he revolutionized the genre'; 'The influence of his experimentation is evident in the ballets of Sergey Prokofiev and Aram Khachaturian' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Years of fame; Legacy"}], how_known: "Swan Lake premiere 20 February 1877 Old Style = 4 March 1877 New Style (S1)."}
    - {value: "Symphony No. 6 in B Minor (Pathétique)", year: 1893, kind: "work", lasting: "'his most celebrated masterpiece'; his last three symphonies 'would influence Gustav Mahler, Sergey Rachmaninoff, and Dmitry Shostakovich' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Final years; Legacy"}], how_known: "Premiere 16 October 1893 Old Style = 28 October 1893 New Style (S1)."}
  evidence_of_impact:
    - {value: "Honorary doctorate, University of Cambridge (1893)", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "Final years"}], how_known: "Britannica."}
    - {value: "Stravinsky: 'Tchaikovsky drew unconsciously from the true, popular sources of our race'", kind: "assessment by a later major figure", certainty: 0.7, cites: [{source: S1, locator: "Legacy"}], how_known: "Britannica."}
  major_works:
    - {value: "Piano Concerto No. 1", year: 1875, kind: "composition", certainty: 0.7, cites: [{source: S1, locator: "Middle years"}], how_known: "Britannica: Boston premiere October 1875."}
    - {value: "Eugene Onegin", year: 1878, kind: "composition", certainty: 0.7, cites: [{source: S1, locator: "Years of fame"}], how_known: "Britannica."}
    - {value: "The Queen of Spades", year: 1890, kind: "composition", certainty: 0.7, cites: [{source: S1, locator: "Final years"}], how_known: "Britannica."}
    - {value: "Liturgy of St John Chrysostom, Op. 41", year: 1878, kind: "composition", certainty: 0.7, cites: [{source: S5, locator: "note 2"}, {source: S7, locator: "Liturgy of St. John Chrysostom"}], how_known: "Sacred work; standing rule: music/liturgy subject alone does not score A or religion."}
    - {value: "All-Night Vigil, Op. 52", year: 1882, kind: "composition", certainty: 0.7, cites: [{source: S5, locator: "note 2"}, {source: S7, locator: "All-Night Vigil"}], how_known: "Sacred work; not an A/religion score (standing rule)."}
  honours:
    - {value: "Honorary doctorate, University of Cambridge", year: 1893, certainty: 0.7, cites: [{source: S1, locator: "Final years"}], how_known: "Britannica."}
  definition_fit: {value: "clearly meets", rationale: "Revolutionized ballet; first great Russian symphonist (S1).", certainty: 0.7, cites: [{source: S1, locator: "Legacy"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "Russian Orthodox", certainty: 0.7, cites: [{source: S7, locator: "Childhood"}], how_known: "Raised Orthodox; clergy ancestors; godfather archpriest (S7). Heritage only."}
  family_religious_practice: {value: "Orthodox household; icons; childhood poems to God; sang in altar trio at episcopal services", certainty: 0.5, cites: [{source: S7, locator: "Childhood"}], how_known: "Secondary (Religious views wiki); heritage context."}
  parents_and_household:
    - {value: "Father Ilya Tchaikovsky, manager of the Kamsko-Votkinsk metal works; mother Alexandra Assier, of French émigré descent", role: "family", certainty: 0.7, cites: [{source: S1, locator: "Early years"}], how_known: "Britannica."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated beyond S1 family sketch."}
  schooling:
    - {value: "Imperial School of Jurisprudence, St. Petersburg (1850–59); St. Petersburg Conservatory (1862–65, under Zaremba and Anton Rubinstein)", certainty: 0.7, cites: [{source: S1, locator: "Early years"}], how_known: "Britannica."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["Russian", "French", "German"], certainty: 0.5, cites: [{source: S3, locator: "Early life and education"}], how_known: "Wikipedia: fluent French and German by age six (Dürbach)."}
  notable_events:
    - {value: "Mother Alexandra died of cholera, 1854", certainty: 0.7, cites: [{source: S1, locator: "Early years"}, {source: S5, locator: "family section"}], how_known: "Britannica; own Letter 659."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1870–1893", certainty: 0.7, cites: [{source: S1, locator: "Middle years; Final years"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Russian Orthodox Church", years: "birth–1893", certainty: 0.5, cites: [{source: S7, locator: "Childhood; Last decade"}, {source: S4, locator: "church / Christ prayer"}, {source: S5, locator: "church bonds"}], how_known: "Heritage and continued attendance/poetic attachment; not coded as primary_system (dogmas rejected in own letters)."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing read on science and religion as such."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "Three private letters in the span (S4 1877, S5 1877, S6 1893) consistently reject Christian dogmas of retribution / God the Judge, lean pantheistic on immortality in 1877, yet keep prayer to Christ, poetic Orthodox bonds, and 1893 veneration of a 'creator and source of all blessings' plus desire to set Gospel texts. Self-describes as 'full of contradictions' (S5). No listed code fits: CHRIST blocked by dogma loss and pantheistic afterlife lean; PANT blocked by Christ-prayer / creator language and failure of S6 Deus sive Natura test (pantheism here is about future life, not God=Nature substance). Liturgy Op.41 / Vigil Op.52 are works, not profession (standing rule; P16). Secondary scholars disagree (S7: Sizko vs Zakharova) — not used to force 0.5. Leads: CHRIST, PANT."}
  secondary_system: {value: UNKNOWN, how_known: "None (P29)."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Lead: turns to Christ in prayer (S4); Gospel texts dreamed for music (S6); Orthodox poetic bonds (S5). Not coded: reason rejects Orthodox and all Christian dogmas (S4); lost faith in dogmas (S5); rejects God Judge/Avenger (S6)."}
    - {code: PANT, reason: "Lead: 'completely enthralled by the pantheistic view of future life and immortality' (S4); future life only as matter preserved / pantheistic eternity of nature (S5). Not coded: does not pass S6 (no Deus sive Natura / one-substance claim); 1893 still speaks of a creator (S6); self-contradiction with Christ-prayer."}
    - {code: ATHE, reason: "Weak lead only: 'convinced that there is no eternal life' (S5). Cancelled by Christ-prayer, creator language, and instinct for reunion with the dead."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "Mixed in the same span: A 0–1 lead — involuntary prayer to Christ (S4); 'creator and source of all blessings' and Gospel 'Come unto me' (S6); strong poetic bonds to Orthodox worship (S5). A 4 lead — pantheistic eternity of nature / 'one microscopic phenomena' and matter preserved (S4, S5). Neither reading reaches 0.5 over the other (Wagner/Plotinus pattern). Liturgy/Vigil attendance and composition are aesthetic/work, not a locus score (standing rule). Do not force plot."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30). Pantheistic eternity-of-nature language in S4/S5 is about immortality / afterlife locus, not nature's causal order or laws vs exceptions (P16). No Naturgesetze / law-vs-exception statement read."}
    C_ledger: {value: BELOW_THRESHOLD, how_known: "Lead toward 4: rejects dogma of retribution (S4, S5) and 'God the Judge, God the Chastiser, God the Avenger' (S6). Counter-lead: instinct refuses never seeing mother again (S5); 1893 still venerates a blessing-source creator. Not enough for a scored value."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "Lead toward 3: reason 'stubbornly refuses to accept the truth of dogma' of Orthodoxy and all Christian denominations (S4); lost faith in dogmas (S5). Counter: still turns to Christ in prayer and wants Gospel texts (S4, S6). Mixed."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read on the world's universal order as such (P7, P19)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD, so the P4 test cannot be applied. B is UNKNOWN."}
  statements:
    - text: "On the one hand, my reason stubbornly refuses to accept the truth of dogma, whether from the Orthodox church or any other Christian denomination. For example, however much I might think about the doctrine of retribution and rewards, I can never discover the slightest sense in this belief. … My mind finds a firm belief in eternal life equally elusive. In this respect, I am completely enthralled by the pantheistic view of future life and immortality. On the other hand, my education, my habits from childhood, my poetic received ideas about Christ and his teaching — all this makes me involuntarily turn to him in prayer at times of grief and with gratitude in times of joy."
      cites: [{source: S4, locator: "Letter 633, Clarens, 30 October/11 November 1877 (EN Winter)"}]
      date: "1877-11-11"
      language: "English translation of Russian"
      axes: [A_locus, C_ledger, D_authority]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
    - text: "And so on the one hand I still have strong bonds which tie me to the church, on the other I, like you, have long since lost faith in the dogmas. The dogma of retribution in particular seems to me terribly unfair and unreasonable. I, like you, have come to believe that if there is a future life, it is only in the sense that matter is preserved, and that in a pantheistic view of the eternity of nature I am merely one microscopic phenomena. In short, I cannot comprehend individual immortality. … And so as a result of all my reasoning, I became convinced that there is no eternal life. But conviction is one thing, and instinctive feelings another. … So you see, my dear friend, that I am full of contradictions, and although I continue to mature in years, neither religion nor philosophy has yet to soothe my restless spirit."
      cites: [{source: S5, locator: "Letter 659, Vienna, 23 November/5 December 1877 (EN Langston)"}]
      date: "1877-12-05"
      language: "English translation of Russian"
      axes: [A_locus, C_ledger]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
    - text: "In the Requiem a lot is said about God the Judge, God the Chastiser, God the Avenger (!!!). Forgive me, Your Highness — but I shall venture to point out that I do not believe in such a God, or at least that such a God could not elicit from me those tears, that rapture, that veneration before the creator and source of all blessings, which would inspire me. If it were possible, I would be extremely delighted to attempt to set to music some Gospel texts. For instance, how many times have I dreamt of illustrating through music these words of Christ: 'Come unto me all ye that labour and are heavy laden' and then: 'For my yoke is easy and my burden is light'."
      cites: [{source: S6, locator: "Letter 5046, Klin, 26 September/8 October 1893 (EN Sundkvist)"}]
      date: "1893-10-08"
      language: "English translation of Russian"
      axes: [A_locus, C_ledger]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
  changes_over_life:
    - {from: "childhood Orthodox piety (heritage; secondary)", to: "1877 crisis: dogmas rejected, pantheistic immortality lean, Christ-prayer retained (S4, S5)", when: "1877", certainty: 0.7, cites: [{source: S4, locator: "Letter 633"}, {source: S5, locator: "Letter 659"}], how_known: "Own letters in the marriage-crisis year."}
    - {from: "1877 mixed private profession", to: "1893: still rejects Judge/Avenger God; still wants Gospel Christ texts and a blessing-source creator (S6)", when: "1893", certainty: 0.7, cites: [{source: S6, locator: "Letter 5046"}], how_known: "Own letter a month before death; contradiction pattern persists — no clean shift to a single scored code."}
  coder_notes: "Deepen D1. Own voice: Letters 633, 659, 5046 on Tchaikovsky Research (EN translations; Russian also printed). Standing rule applied: Liturgy Op.41 / Vigil Op.52 / loving Orthodox services as poetic art do NOT score A or CHRIST. Secondary Religious views wiki (S7) documents scholar disagreement (Sizko Orthodox path vs Zakharova Renan/Spinoza lean) — used for heritage and open questions only, not to force 0.5. 1887 diary entry on doubting Christ's divinity (quoted in S7) not fetched as a primary diary page (site 500/404); left open. Britannica S1 Cloudflare-blocked this pass; kept as prior full read; dual bio via Wikipedia EN (P50). Chart still unplotted (A BELOW; B UNKNOWN)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Russian (with French/German maternal descent)", certainty: 0.5, cites: [{source: S3, locator: "Early life and education"}], how_known: "Wikipedia EN."}
  religious_heritage_by_birth: {value: "Russian Orthodox", certainty: 0.7, cites: [{source: S7, locator: "Childhood"}], how_known: "Raised Orthodox; clergy ancestors (S7). Heritage only — not a worldview code."}
  baptism_or_initiation: {value: "Baptized in the Orthodox Church (family icons; godfather archpriest Vasily Blinov)", certainty: 0.5, cites: [{source: S7, locator: "Childhood"}], how_known: "Secondary (Religious views wiki)."}
  childhood_catechism: {value: "Catechism among subjects at Imperial School of Jurisprudence", certainty: 0.5, cites: [{source: S7, locator: "Youth and maturity"}], how_known: "Secondary; struggled with Catechism among other subjects."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1870–1893", certainty: 0.7, cites: [{source: S1, locator: "Middle years; Final years"}], how_known: "Romeo and Juliet (1870) to the Pathétique (1893), the first and last lasting items, dated by first performance (P29, P30)."}
  age_at_first_lasting_contribution: {value: 30, certainty: 0.7, cites: [{source: S1, locator: "Introduction; Middle years"}], how_known: "1870 − 1840 = 30 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: 1877, certainty: 0.7, cites: [{source: S4, locator: "Letter 633"}, {source: S5, locator: "Letter 659"}], how_known: "Private letters on dogma, pantheism, Christ-prayer (within span)."}
  lio_views_relative_to_major_work: {value: "during major work", rationale: "Letters 633/659 (1877) and 5046 (1893) fall inside 1870–1893; A remains BELOW_THRESHOLD.", certainty: 0.7, cites: [{source: S4, locator: "1877"}, {source: S6, locator: "1893"}], how_known: "Dates."}
  worldview_during_major_work: {value: "Mixed private letters: dogmas and Judge-God rejected; pantheistic lean on immortality (1877); Christ-prayer and creator/Gospel attraction retained (1877, 1893); self-described contradictions. primary_system and A BELOW_THRESHOLD; B UNKNOWN.", certainty: 0.7, cites: [{source: S4, locator: "Letter 633"}, {source: S5, locator: "Letter 659"}, {source: S6, locator: "Letter 5046"}], how_known: "Own letters in span."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Romantic music (S1); no geometrical demonstration form.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Pantheistic eternity-of-nature language (S4/S5) is a thin circle lead; Christ-prayer / creator language cuts against a clean circle. Not assessed as present.", certainty: 0.5, cites: [{source: S4, locator: "pantheistic view"}, {source: S5, locator: "pantheistic eternity of nature"}], how_known: "Coder's reading of private letters."}
  reading: "Lane B separate. No H1 test (A BELOW; B UNKNOWN)."
  notes: "Sacred compositions and church attendance are not Lane A scores (standing rule)."

institutions:
  - {value: "Moscow Conservatory", role: "teacher of music theory", years: "1866–1878", kind: "university", certainty: 0.7, cites: [{source: S1, locator: "Middle years; Years of fame"}], how_known: "Britannica."}
collaborators:
  - {value: "Nadezhda von Meck", relation: "correspondent", note: "patroness and correspondent, 1876–1890; Letters 633 and 659", certainty: 0.7, cites: [{source: S1, locator: "Years of fame"}, {source: S4, locator: "addressee"}, {source: S5, locator: "addressee"}], how_known: "Britannica; letters."}
  - {value: "Nikolay Rubinstein", relation: "mentor or employer", note: "Moscow Conservatory director", certainty: 0.7, cites: [{source: S1, locator: "Middle years"}], how_known: "Britannica."}
  - {value: "Grand Duke Konstantin Konstantinovich (K.R.)", relation: "correspondent", note: "Letter 5046 (1893) on Requiem / God the Judge", certainty: 0.7, cites: [{source: S6, locator: "addressee"}], how_known: "Letter 5046."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 212"}], how_known: "Study roster."}
  controversies:
    - {value: "Scholarly disagreement on late religiosity (Orthodox return vs Renan/Spinoza lean); death cholera vs suicide theories — neither used to score A/B", certainty: 0.5, cites: [{source: S7, locator: "Changes in views; Post-1887"}, {source: S3, locator: "Death"}], how_known: "Secondary; left open."}
  data_quality_flags:
    - "Worldview from English translations of Russian private letters (Tchaikovsky Research); Russian also printed on-site."
    - "Britannica S1 Cloudflare-blocked on deepen pass; prior full read retained; dual bio via Wikipedia EN (P50)."
  open_questions:
    - "1887 diary entry on doubting Christ's divinity (quoted in S7) — primary diary page not fetched (site errors); optional for a future pass."
    - "Whether a Loeb-style Russian edition page-check could lift translation ceiling (already 0.7 on private letters)."
    - "Settled this deepen: primary and A → BELOW_THRESHOLD; B stays UNKNOWN; do not force plot."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Alexander Poznansky"
    citation: "Poznansky, Alexander. 'Pyotr Ilyich Tchaikovsky.' Encyclopaedia Britannica (scholars edition). https://kids.britannica.com/scholars/article/Pyotr-Ilyich-Tchaikovsky/71483"
    url: "https://kids.britannica.com/scholars/article/Pyotr-Ilyich-Tchaikovsky/71483"
    accessed: 2026-10-19
    reliability_note: "Signed article, scholars edition, read in full on create pass. Cloudflare 403 on deepen D1; retained as prior read."
    used_for: [identity, basics, contribution, childhood, timing, institutions, collaborators]
    source_quality: "reference entry"
  - id: S2
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [review]
    source_quality: "study roster"
  - id: S3
    type: tertiary
    kind: "encyclopedia"
    author: "Wikipedia contributors"
    citation: "Wikipedia. 'Pyotr Ilyich Tchaikovsky.' https://en.wikipedia.org/wiki/Pyotr_Ilyich_Tchaikovsky"
    url: "https://en.wikipedia.org/wiki/Pyotr_Ilyich_Tchaikovsky"
    accessed: 2026-10-24
    reliability_note: "P50 dual bio with S1; Cyrillic native name; birth/death agree with Britannica."
    used_for: [identity, basics, childhood]
    source_quality: "reference entry"
  - id: S4
    type: primary
    kind: "letter"
    author: "Pyotr Ilyich Tchaikovsky"
    citation: "Tchaikovsky, P. I. Letter 633 to Nadezhda von Meck, Clarens, 30 October/11 November 1877. English translation by Nick Winter. Tchaikovsky Research. https://en.tchaikovsky-research.net/pages/Letter_633"
    url: "https://en.tchaikovsky-research.net/pages/Letter_633"
    accessed: 2026-10-24
    reliability_note: "Scholarly site; Russian + EN; also in PSS vol. VI and Garden/Gotteri 1993."
    used_for: [worldview]
    source_quality: "scholarly edition or monograph"
  - id: S5
    type: primary
    kind: "letter"
    author: "Pyotr Ilyich Tchaikovsky"
    citation: "Tchaikovsky, P. I. Letter 659 to Nadezhda von Meck, Vienna, 23 November/5 December 1877. English translation by Brett Langston. Tchaikovsky Research. https://en.tchaikovsky-research.net/pages/Letter_659"
    url: "https://en.tchaikovsky-research.net/pages/Letter_659"
    accessed: 2026-10-24
    reliability_note: "Scholarly site; Russian + EN; also in PSS vol. VI and Garden/Gotteri 1993."
    used_for: [worldview, contribution]
    source_quality: "scholarly edition or monograph"
  - id: S6
    type: primary
    kind: "letter"
    author: "Pyotr Ilyich Tchaikovsky"
    citation: "Tchaikovsky, P. I. Letter 5046 to Grand Duke Konstantin Konstantinovich, Klin, 26 September/8 October 1893. English translation by Luis Sundkvist. Tchaikovsky Research. https://en.tchaikovsky-research.net/pages/Letter_5046"
    url: "https://en.tchaikovsky-research.net/pages/Letter_5046"
    accessed: 2026-10-24
    reliability_note: "Scholarly site; Russian + EN; also in PSS vol. XVII (1981)."
    used_for: [worldview, collaborators]
    source_quality: "scholarly edition or monograph"
  - id: S7
    type: secondary
    kind: "encyclopedia"
    author: "Wikipedia contributors"
    citation: "Wikipedia. 'Religious views of Pyotr Ilyich Tchaikovsky.' https://en.wikipedia.org/wiki/Religious_views_of_Pyotr_Ilyich_Tchaikovsky"
    url: "https://en.wikipedia.org/wiki/Religious_views_of_Pyotr_Ilyich_Tchaikovsky"
    accessed: 2026-10-24
    reliability_note: "Secondary survey of scholars (Sizko, Zakharova, Makarova, etc.); used for heritage and open questions only — not to force primary_system or A."
    used_for: [heritage, childhood, contribution, review]
    source_quality: "reference entry"
---

## Summary

Pyotr Ilyich Tchaikovsky (1840–1893), Russian composer [S1, S3]. Deepen D1: primary_system BELOW_THRESHOLD (leads CHRIST, PANT); A BELOW_THRESHOLD; B UNKNOWN; mid_basin BELOW_THRESHOLD. Not plotted.

## Life and work

Votkinsk; St. Petersburg; Moscow; Klin [S1, S3]. Patroness Nadezhda von Meck; correspondent Grand Duke Konstantin (K.R.) [S1, S4–S6].

## Contribution and impact

Romeo and Juliet 1870; ballets; Pathétique 1893 [S1]. Sacred works Liturgy Op. 41 and Vigil Op. 52 are compositions, not worldview scores (standing rule).

## Childhood and education

Russian Orthodox household (heritage) [S7]. School of Jurisprudence; Conservatory [S1].

## Adult working worldview

Own private letters (S4, S5, S6): reason rejects Orthodox and other Christian dogmas and God the Judge/Avenger; 1877 pantheistic lean on immortality / eternity of nature; retained involuntary prayer to Christ and 1893 desire to set Gospel texts while venerating a creator as source of blessings; self-described contradictions. primary_system and A BELOW_THRESHOLD. B UNKNOWN (not a scientist; no P16 nature-law statement). Liturgy/Vigil and church-as-poetry do not score A or religion.

## Heritage (context only)

Russian Orthodox by birth [S7]. Not a worldview code.

## Timing

1870–1893, age 30 [S1]. First LIO-type evidence 1877 (during major work) [S4, S5].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Geometric form no; circle unclear. H1 not tested (A BELOW; B UNKNOWN).

## Open questions

- 1887 diary divinity entry (secondary quote in S7) — primary page not fetched.
- Settled D1: primary/A → BELOW; B UNKNOWN; do not force plot.

## Research log

- 2026-10-24: Deepen D1 — Letters 633, 659, 5046 (Tchaikovsky Research); Wikipedia EN bio + Religious views; P47 on S1–S7; P50 dual bio. primary/A UNKNOWN → BELOW_THRESHOLD; B stays UNKNOWN. Chart-moving NO. No fallacy_catalog. No figures/.
- 2026-10-20: AA8 audit fixes: premiere days labelled Old Style (4 March 1877 and 28 October 1893 New Style); 1880 revision of Romeo and Juliet noted.
- 2026-10-19: Read Britannica (Poznansky, scholars edition).
