---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z6)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to 20c_late. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z6, order P32: F 3, rank 157). Basics and own words from the INA 'Archives du XXe siècle' interview with Jean-José Marchand (filmed 1972; INA biography and bibliography on the same pages), chapter 2 '...et l'indifférence religieuse': 'jamais dans toute mon enfance, aucun problème, aucune inquiétude religieuse, ne s'est posé à moi'; 'jamais, à aucun moment, enfin, il n'y a jamais eu pour moi aucun problème religieux'. The 1988 Eribon lines ('sourd aux réponses religieuses'; 'un rapport avec un Dieu personnel, jamais') were seen only as second-hand quotations (V3), so leads only. Not a scientist (social science; Sen precedent). Span 1949–1971. primary_system BELOW_THRESHOLD (leads AGNOS, ATHE); A BELOW_THRESHOLD; B UNKNOWN; C, D, E UNKNOWN; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen D1 (queue #151, F 3, rank 157). Re-opened INA Marchand 1972 ch. 2 primary. In-span own-voice: Time 'Theology: Toward a Hidden God' (8 Apr 1966) quoted words via CNN AllPolitics 1996 Notebook reprint (S4) — 'Personally, I've never been confronted with the question of God'; 'perfectly possible to spend my life knowing that we will never explain the universe'; Time's 'politely indifferent atheist' is journalist label, not self-ID. Tristes Tropiques (1955) three-religions / Islam chapters read as attributed excerpts (S7): comparative cultural critique, not a personal creed (P42-analogue for ethnographic essay). Eribon De près et de loin (1988) still no free full text (Cairn paywall; IA absent; Google Books no preview) — p.14 'sourd aux réponses religieuses' / 'sens du mystère' and 'Dieu personnel, jamais' remain V3 second-hand (S5 blog cites Odile Jacob p.14; S6 France Catholique paraphrase with quotation marks); after-span P20 leads only. Wikipedia EN + Académie française + NYT obit dual bio (S3/S8/S9; P50): birth 28 Nov 1908 Brussels; death 30 Oct 2009 Paris. Britannica 403. P47 source_quality on S1–S9. primary/A BELOW_THRESHOLD (leads AGNOS, ATHE); B UNKNOWN (not scientist, Sen/P30); mid UNKNOWN. Chart-moving NO. Draft, not reviewed."}

identity:
  id: levi-strauss-claude
  display_name: "Claude Lévi-Strauss"
  roster:
    canonical_name: "Claude Levi-Strauss"
    rank: 157
    F: 3
    models: [Claude, DeepSeek, GPT]
    band: "core (3–4)"
    status: "core"
    field: "anthropology"
    field_bucket: "social science"
  full_name: {value: "Gustave Claude Lévi-Strauss", certainty: 0.7, cites: [{source: S3, locator: "infobox / Early life"}], how_known: "Wikipedia EN gives Gustave Claude Lévi-Strauss; INA and everyday use Claude Lévi-Strauss."}
  native_name: {value: "Claude Lévi-Strauss", certainty: 1.0, cites: [{source: S1, locator: "Biographie"}, {source: S3, locator: "infobox"}], how_known: "INA and Wikipedia."}
  aliases:
    - {name: "Claude Levi-Strauss", kind: "transliteration"}
    - {name: "Claude-Levi-Strauss", kind: "roster alias"}
    - {name: "Gustave Claude Lévi-Strauss", kind: "birth name"}

basics:
  birth:
    date: {value: "1908-11-28", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Biographie"}, {source: S3, locator: "infobox"}], how_known: "INA year 1908; Wikipedia day 28 November 1908 (dual, P50)."}
    place: {value: "Brussels", modern_name: "Brussels, Belgium", polity_then: "Belgium", certainty: 1.0, cites: [{source: S1, locator: "Biographie"}, {source: S3, locator: "infobox"}], how_known: "INA and Wikipedia."}
  death:
    date: {value: "2009-10-30", calendar: gregorian, certainty: 1.0, cites: [{source: S3, locator: "infobox / Later life and death"}, {source: S8, locator: "announcement"}, {source: S9, locator: "lead"}], how_known: "Académie française (30 octobre 2009, Paris); NYT and Wikipedia agree (P50)."}
    place: {value: "Paris", modern_name: "Paris, France", polity_then: "France", certainty: 1.0, cites: [{source: S8, locator: "announcement"}, {source: S9, locator: "lead"}, {source: S3, locator: "infobox"}], how_known: "Académie française and NYT (son Laurent: home in Paris); Wikipedia."}
  first_lasting_contribution_year: {value: 1949, certainty: 0.7, cites: [{source: S1, locator: "Bibliographie"}, {source: S3, locator: "Career"}], how_known: "Les Structures élémentaires de la parenté, PUF, 1949; Wikipedia concurs."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "Bibliographie"}], how_known: "1949 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 1.0, cites: [{source: S1, locator: "Biographie"}, {source: S3, locator: "infobox"}], how_known: "Belgium (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "Biographie"}, {source: S3, locator: "Career"}], how_known: "Paris (EPHE, Collège de France) over the span; Brazil fieldwork and NY wartime years are formative but outside the coded major_work_period.", alternatives: [{value: "Latin America", cites: [{source: S1, locator: "Biographie"}], note: "São Paulo / Mato Grosso fieldwork 1935–39, before span."}, {value: "North America", cites: [{source: S3, locator: "Expatriation"}], note: "New School / cultural attaché WWII–1947, before span."}]}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["French"], certainty: 0.7, cites: [{source: S1, locator: "Bibliographie"}], how_known: "French titles; English translations secondary."}
  occupations: {value: ["anthropologist", "ethnologist", "professor (EPHE; Collège de France)"], certainty: 1.0, cites: [{source: S1, locator: "Biographie"}, {source: S3, locator: "lead"}], how_known: "INA and Wikipedia."}

contribution:
  era_bucket: 20c_late
  fields: {value: ["social anthropology", "structuralism", "mythology"], certainty: 0.7, cites: [{source: S1, locator: "Biographie"}, {source: S3, locator: "lead"}], how_known: "INA; Wikipedia."}
  lasting_original_contributions:
    - {value: "Les Structures élémentaires de la parenté", year: 1949, kind: work, lasting: "his work 'est au fondement du courant de pensée dit structuraliste' (S1); Wikipedia: key kinship/structural anthropology work", certainty: 0.7, cites: [{source: S1, locator: "Biographie; Bibliographie"}, {source: S3, locator: "Career"}], how_known: "INA and Wikipedia."}
    - {value: "Mythologiques (4 vols; vol. 4 L'Homme nu)", year: 1971, kind: "body of work", lasting: "structural analysis of myth (S1; S3)", certainty: 0.5, cites: [{source: S1, locator: "Bibliographie"}, {source: S3, locator: "Mythologiques"}], how_known: "INA bibliography; Wikipedia; lastingness the coder's call, so the span end is 0.5."}
  evidence_of_impact:
    - {value: "Brought anthropology into French social science in the 1960s; founded structuralism", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "Biographie"}, {source: S3, locator: "lead"}], how_known: "INA; Wikipedia."}
    - {value: "Académie française (1973); Erasmus Prize (1973); Pléiade living author", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "Biographie"}, {source: S3, locator: "Later life"}, {source: S8, locator: "notice"}], how_known: "INA; Wikipedia; Académie."}
  major_works:
    - {value: "Tristes Tropiques", year: 1955, kind: book, certainty: 1.0, cites: [{source: S1, locator: "Biographie"}, {source: S3, locator: "Career"}], how_known: "INA and Wikipedia."}
    - {value: "Anthropologie structurale", year: 1958, kind: book, certainty: 0.7, cites: [{source: S1, locator: "Bibliographie"}, {source: S3, locator: "Works"}], how_known: "INA; Wikipedia."}
    - {value: "La Pensée sauvage", year: 1962, kind: book, certainty: 0.7, cites: [{source: S1, locator: "Bibliographie"}, {source: S3, locator: "The Savage Mind"}], how_known: "INA; Wikipedia."}
  honours:
    - {value: "Elected to the Académie française", year: 1973, certainty: 1.0, cites: [{source: S1, locator: "Biographie"}, {source: S8, locator: "notice"}], how_known: "INA; Académie française."}
    - {value: "Erasmus Prize", year: 1973, certainty: 0.7, cites: [{source: S3, locator: "Later life"}], how_known: "Wikipedia."}
  definition_fit: {value: "clearly meets", rationale: "Founder of structural anthropology (S1; S3).", certainty: 0.7, cites: [{source: S1, locator: "Biographie"}, {source: S3, locator: "lead"}], how_known: "Two sources."}

childhood:
  family_religion: {value: "Jewish by descent; parents without religious feeling (agnostic in secondary bio)", certainty: 0.7, cites: [{source: S1, locator: "ch. 2"}, {source: S3, locator: "Early life"}], how_known: "(INA interview) 'ni mes parents, ni mes oncles et tantes n'avaient le moindre sentiment religieux'; Wikipedia: French-Jewish parents turned agnostic."}
  family_religious_practice: {value: "Formal observances only, out of regard for his grandfather (incl. bar mitzvah to spare him, per secondary)", certainty: 0.7, cites: [{source: S1, locator: "ch. 2"}, {source: S6, locator: "Eribon paraphrase"}], how_known: "INA interview; France Catholique paraphrase of Eribon on bar mitzvah."}
  parents_and_household:
    - {value: "Maternal grandfather, grand rabbin of Versailles (household during 1914–18)", role: grandparent, certainty: 0.7, cites: [{source: S1, locator: "ch. 2"}, {source: S3, locator: "Early life"}], how_known: "INA interview; Wikipedia."}
    - {value: "Father, portrait painter (artist household)", role: father, certainty: 0.7, cites: [{source: S1, locator: "Biographie; ch. 2"}, {source: S3, locator: "Early life"}], how_known: "INA; Wikipedia."}
  household_circumstances: {value: "Family of artists; wartime years in rabbi grandfather's house attached to Versailles synagogue", certainty: 0.7, cites: [{source: S1, locator: "Biographie; ch. 2"}, {source: S3, locator: "Early life"}], how_known: "INA; Wikipedia (Tristes Tropiques passage cited there)."}
  schooling:
    - {value: "Lycée Janson de Sailly", stage: "grammar or secondary school", run_by: "state or municipal", years: "1918–1925", certainty: 0.7, cites: [{source: S3, locator: "Early life and education"}], how_known: "Wikipedia."}
    - {value: "Lycée Condorcet (prépa; did not sit ENS exam)", stage: "grammar or secondary school", run_by: "state or municipal", years: "1925–1926", certainty: 0.7, cites: [{source: S3, locator: "Early life and education"}], how_known: "Wikipedia."}
    - {value: "University of Paris (Sorbonne): law then philosophy; agrégation 1931; doctorat ès lettres 1948", stage: university, run_by: "state or municipal", years: "1926–1931; 1948", certainty: 0.7, cites: [{source: S1, locator: "Biographie"}, {source: S3, locator: "Education / Early career"}], how_known: "INA; Wikipedia."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading:
    - {value: "Marx and Kant in late lycée / prépa years (secondary)", certainty: 0.5, cites: [{source: S3, locator: "Early life"}], how_known: "Wikipedia (Loyer biography via tertiary)."}
  childhood_mentors: []
  languages_in_childhood: {value: ["French"], certainty: 0.7, cites: [{source: S1, locator: "Biographie"}], how_known: "Parisian from age two months (INA)."}
  notable_events:
    - {value: "Raised 1914–18 in maternal grandfather's rabbinical household at Versailles while parents remained unbelieving", certainty: 0.7, cites: [{source: S1, locator: "ch. 2"}], how_known: "(interview)."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1949–1971", certainty: 0.5, cites: [{source: S1, locator: "Bibliographie"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not a natural scientist; no science–religion profession read as his own creed."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "Lifelong religious indifference in own voice: in-span Time 1966 (S4) never confronted with the question of God / universe never to be explained; INA 1972 (S1, one year after span) 'aucun problème religieux'. Indifference names no scored system. Leads AGNOS (mystery / never explain; Eribon 1988 'sens du mystère' V3) and ATHE (Time's journalist label 'politely indifferent atheist'; Eribon V3 'Dieu personnel, jamais'). Tristes Tropiques (1955) religion passages are comparative cultural critique, not a personal profession. Do not force plot."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: AGNOS, reason: "Lead: in-span 'never explain the universe' (S4); after-span Eribon V3 'sourd aux réponses religieuses' + 'sens du mystère' (S5/S6). No clear AGNOS self-label."}
    - {code: ATHE, reason: "Lead only: Time 1966 journalist tag 'politely indifferent atheist' (S4); Eribon V3 no personal God (S6). Own words are indifference, not an ATHE profession."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "In-span (S4) and near-span (S1) indifference: no locus of God/ultimate for his own belief. 'Never confronted with the question of God' names no position. Too thin to score (P19)."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30: social anthropology, as Sen); structural method is linguistic/cultural, not a scored claim about nature's causal order (P16)."}
    C_ledger: {value: UNKNOWN, how_known: "Not read as a scored own-voice claim."}
    D_authority: {value: UNKNOWN, how_known: "Indifference and comparative critique of religions; no scored revelation-vs-observation profession."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: UNKNOWN, how_known: "B_cause is UNKNOWN, which takes precedence (§6, P19). Chart-moving NO (deepen 2026-10-24)."}
  statements:
    - text: "Personally, I've never been confronted with the question of God … I find it's perfectly possible to spend my life knowing that we will never explain the universe."
      cites: [{source: S4, locator: "The Missing God / April 8, 1966 reprint"}]
      date: "1966-04-08"
      context: "Time magazine 'Theology: Toward a Hidden God' (8 Apr 1966), in-span; words as reprinted in CNN/Time Notebook 8 Apr 1996 (S4). Time's surrounding tag 'politely indifferent atheist' is the magazine's label, not his self-description. Original Time page paywalled this pass."
      axes: [A_locus]
      kind: "reported speech"
      verified_against: "newspaper interview"
      verified_on: 2026-10-24
    - text: "Non, jamais, à aucun moment, enfin, il n'y a jamais eu pour moi aucun problème religieux, je puis dire."
      cites: [{source: S1, locator: "ch. 2"}]
      date: "1972"
      context: "INA interview with Jean-José Marchand, answer on adolescent religious crisis; one year after span end (P20 near-span lead)."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
    - text: "jamais dans toute mon enfance, aucun problème, aucune inquiétude religieuse, ne s'est posé à moi"
      cites: [{source: S1, locator: "ch. 2"}]
      date: "1972"
      context: "INA Marchand interview; childhood indifference; near-span (P20)."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
    - text: "…même si je reste sourd aux réponses religieuses, je suis de plus en plus pénétré du sentiment que le cosmos, et la place de l'homme dans l'univers, dépassent et dépasseront toujours notre compréhension. Il arrive que je m'entende mieux avec des croyants qu'avec des rationalistes à tous crins. Au moins les premiers ont le sens du mystère."
      cites: [{source: S5, locator: "quotes De près et de loin, Odile Jacob 1988, p.14"}]
      date: "1988"
      context: "Eribon Conversations / De près et de loin — after span (P20). Seen only as second-hand quotation citing p.14 (S5); full book not opened (Cairn/IA/Books blocked). Lead AGNOS only."
      axes: [A_locus]
      kind: "reported speech"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
    - text: "si par religion vous entendez un rapport avec un Dieu personnel, jamais."
      cites: [{source: S6, locator: "Eribon paraphrase with quotation marks"}]
      date: "1988"
      context: "France Catholique paraphrase of Eribon Conversations — after span (P20). V3; book not opened. Lead ATHE only; not a scored profession."
      axes: [A_locus]
      kind: "reported speech"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
    - text: "Les hommes ont fait trois grandes tentatives religieuses pour se libérer de la persécution des morts, de la malfaisance de l'au-delà et des angoisses de la magie. … chaque étape, loin de marquer un progrès sur la précédente, témoigne plutôt d'un recul."
      cites: [{source: S7, locator: "Le retour excerpt"}]
      date: "1955"
      context: "Tristes Tropiques (1955), in-span. Comparative cultural ranking of Buddhism/Christianity/Islam — ethnographic/philosophical essay voice, not a first-person creed. Not scored as ATHE/AGNOS profession."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
  changes_over_life: []
  coder_notes: "Deepen D1 2026-10-24: INA re-opened; Time 1966 in-span via CNN reprint; TT 1955 attributed excerpt; Eribon still V3 (no free full text). Indifference may stay BELOW — names no position. Not a scientist (Sen/P30). Keep BELOW/UNKNOWN; do not force plot. Chart-moving NO. Full De près et de loin and full Tristes Tropiques (Plon) remain open if a free primary becomes available."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "French Jewish", certainty: 1.0, cites: [{source: S1, locator: "ch. 2"}, {source: S3, locator: "Early life"}], how_known: "INA interview; Wikipedia."}
  religious_heritage_by_birth: {value: "Jewish", certainty: 1.0, cites: [{source: S1, locator: "ch. 2"}, {source: S3, locator: "Early life"}], how_known: "INA; Wikipedia."}
  baptism_or_initiation: {value: "Bar mitzvah performed to spare grandfather (secondary, Eribon via S6)", certainty: 0.5, cites: [{source: S6, locator: "Eribon paraphrase"}], how_known: "France Catholique paraphrase of Eribon; not confirmed in INA pages read."}
  childhood_catechism: {value: "Formal observances for grandfather only; ham sandwiches behind his back (own words)", certainty: 0.7, cites: [{source: S1, locator: "ch. 2"}], how_known: "(interview)."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1949–1971", certainty: 0.5, cites: [{source: S1, locator: "Bibliographie"}, {source: S3, locator: "Mythologiques"}], how_known: "Structures élémentaires (1949) to L'Homme nu (1971) (P29, P30); end is the coder's call on lastingness."}
  age_at_first_lasting_contribution: {value: 41, certainty: 1.0, cites: [{source: S1, locator: "Biographie; Bibliographie"}, {source: S3, locator: "infobox"}], how_known: "1949 − 1908 = 41 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: "1966 Time interview words (indifference; never explain universe)", certainty: 0.5, cites: [{source: S4, locator: "1966 reprint"}], how_known: "In-span reported speech via secondary reprint; still BELOW for coding."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.5, cites: [{source: S4, locator: "1966"}, {source: S7, locator: "1955 TT"}], how_known: "In-span indifference / comparative critique only; not a scored profession."}
  worldview_during_major_work: {value: "religious indifference (unnamed system)", certainty: 0.5, cites: [{source: S4, locator: "1966"}, {source: S1, locator: "1972 near-span"}], how_known: "Consistent indifference; BELOW_THRESHOLD for primary_system."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Structural method modelled on linguistics and binary oppositions (S1; S3), not a scored geometric cosmology of nature.", certainty: 0.5, cites: [{source: S1, locator: "Biographie"}, {source: S3, locator: "Anthropological theories"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No Lane B finding. Structuralism is method for kinship/myth, not a coded personal belief model about physical nature."
  notes: "P30: social anthropology → B not from working science (Sen precedent)."

institutions:
  - {value: "École pratique des hautes études", role: "directeur d'études (comparative religion of non-literate peoples)", years: "1950s–", kind: university, certainty: 0.7, cites: [{source: S1, locator: "Biographie"}, {source: S3, locator: "Career"}], how_known: "INA; Wikipedia."}
  - {value: "Collège de France", role: "chair of social anthropology", years: "1959–1982", kind: university, certainty: 1.0, cites: [{source: S1, locator: "Biographie"}, {source: S3, locator: "lead"}], how_known: "INA; Wikipedia."}
  - {value: "Académie française", role: "member (fauteuil 29)", years: "1973–2009", kind: "academy or learned society", certainty: 1.0, cites: [{source: S8, locator: "notice"}, {source: S1, locator: "Biographie"}], how_known: "Académie française; INA."}
  - {value: "University of São Paulo", role: "visiting professor of sociology", years: "1935–1938", kind: university, certainty: 0.7, cites: [{source: S1, locator: "Biographie"}, {source: S3, locator: "Early career"}], how_known: "INA; Wikipedia."}
collaborators:
  - {value: "Roman Jakobson", relation: "influenced by", certainty: 0.7, cites: [{source: S3, locator: "Expatriation"}], how_known: "Wikipedia."}
  - {value: "Didier Eribon", relation: correspondent, certainty: 0.7, cites: [{source: S5, locator: "citation"}, {source: S1, locator: "Bibliographie"}], how_known: "INA bibliography lists De près et de loin."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 157"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Britannica 403 this deepen; basics dualled INA + Wikipedia; death dualled Académie française + NYT + Wikipedia."
    - "Eribon De près et de loin (1988) still unread in the book itself — V3 second-hand for 'sourd' / 'Dieu personnel' lines."
    - "Time 1966 own words via 1996 CNN reprint only; original Time page paywalled."
    - "Tristes Tropiques religion chapters via attributed web excerpt, not full Plon OCR."
  open_questions:
    - "Full primary text of De près et de loin (Odile Jacob 1988 / Conversations with Claude Lévi-Strauss 1991) to lift V3."
    - "Full Tristes Tropiques (Plon) religion chapters beyond attributed excerpts."
    - "Original Time 8 Apr 1966 page (not only 1996 Notebook reprint)."

sources:
  - id: S1
    type: primary
    kind: "other"
    author: "Claude Lévi-Strauss, interviewed by Jean-José Marchand"
    citation: "Marchand, Jean-José. 'Claude Lévi-Strauss.' Archives du XXe siècle (filmed 1972), INA Entretiens patrimoniaux, transcription. https://entretiens.ina.fr/entretien/38/claude-levi-strauss/transcription/2"
    url: "https://entretiens.ina.fr/entretien/38/claude-levi-strauss/transcription/2"
    accessed: 2026-10-24
    reliability_note: "Filmed interview, INA transcription (recorded_interview, P8), with an INA biography and bibliography."
    source_quality: "primary / own words"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions]
  - id: S2
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [review]
  - id: S3
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia. 'Claude Lévi-Strauss.' https://en.wikipedia.org/wiki/Claude_Lévi-Strauss"
    url: "https://en.wikipedia.org/wiki/Claude_Lévi-Strauss"
    accessed: 2026-10-24
    reliability_note: "Tertiary dual-bio partner (P50) for birth/death/career; not used alone for worldview codes."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, heritage, timing, institutions, collaborators]
  - id: S4
    type: secondary
    kind: "other"
    author: "Time magazine (via CNN AllPolitics Notebook reprint)"
    citation: "Time. 'Theology: Toward a Hidden God.' 8 April 1966; words reprinted in CNN AllPolitics / TIME Notebook, 8 April 1996, section 'The Missing God'. https://www.cnn.com/ALLPOLITICS/1996/analysis/time/9604/08/misc.shtml"
    url: "https://www.cnn.com/ALLPOLITICS/1996/analysis/time/9604/08/misc.shtml"
    accessed: 2026-10-24
    reliability_note: "In-span reported speech; secondary reprint of Time 1966. Magazine's 'politely indifferent atheist' tag is not his self-label. Original Time page paywalled."
    source_quality: "newspaper interview"
    used_for: [worldview, timing]
  - id: S5
    type: secondary
    kind: "other"
    author: "Alkaly Cissé (blog quoting Eribon)"
    citation: "Cissé, Alkaly. 'Claude Lévi-Strauss.' Blog post, 6 December 2009, quoting Lévi-Strauss & Eribon, De près et de loin, Odile Jacob, 1988, p. 14. https://alkalycisse.blogspot.com/2009/12/claude-levi-strauss.html"
    url: "https://alkalycisse.blogspot.com/2009/12/claude-levi-strauss.html"
    accessed: 2026-10-24
    reliability_note: "Second-hand quotation with page cite; book itself not opened (V3)."
    source_quality: "unofficial web copy"
    used_for: [worldview]
  - id: S6
    type: secondary
    kind: "other"
    author: "France Catholique (paraphrase of Eribon)"
    citation: "France Catholique. '3130-L'humanisme de Lévi-Strauss.' Paraphrase of Didier Eribon conversations, including quoted 'si par religion vous entendez un rapport avec un Dieu personnel, jamais.' https://www.france-catholique.fr/3130-l-humanisme-de-levi-strauss.html"
    url: "https://www.france-catholique.fr/3130-l-humanisme-de-levi-strauss.html"
    accessed: 2026-10-24
    reliability_note: "Secondary paraphrase with quotation marks; Eribon book not opened (V3)."
    source_quality: "unofficial web copy"
    used_for: [worldview, heritage]
  - id: S7
    type: primary
    kind: "published work by the subject"
    author: "Claude Lévi-Strauss"
    citation: "Lévi-Strauss, Claude. Tristes Tropiques. Plon, 1955; 'Le retour' religion passage as attributed at https://echange-spirituel.kazeo.com/le-retour-extrait-tristes-tropiques-claude-levi-strauss-a120435594 (excerpt host)."
    url: "https://echange-spirituel.kazeo.com/le-retour-extrait-tristes-tropiques-claude-levi-strauss-a120435594"
    accessed: 2026-10-24
    reliability_note: "In-span published work; this pass used an attributed web excerpt, not a full Plon/OCR primary. Comparative religion critique only."
    source_quality: "unofficial web copy"
    used_for: [worldview, contribution]
  - id: S8
    type: primary
    kind: "institutional page"
    author: "Académie française"
    citation: "Académie française. 'Décès de M. Claude Lévi-Strauss (F29).' 30 October 2009. https://www.academie-francaise.fr/actualites/deces-de-m-claude-levi-strauss-f29"
    url: "https://www.academie-francaise.fr/actualites/deces-de-m-claude-levi-strauss-f29"
    accessed: 2026-10-24
    reliability_note: "Institutional death notice: 30 Oct 2009, Paris."
    source_quality: "reference entry"
    used_for: [basics, contribution, institutions]
  - id: S9
    type: secondary
    kind: "other"
    author: "Edward Rothstein / New York Times"
    citation: "Rothstein, Edward. 'Claude Lévi-Strauss, 100, Dies; Altered Western Views of the “Primitive”.' New York Times, 4 November 2009. https://www.nytimes.com/2009/11/04/world/europe/04levistrauss.html"
    url: "https://www.nytimes.com/2009/11/04/world/europe/04levistrauss.html"
    accessed: 2026-10-24
    reliability_note: "Obituary; son Laurent: cardiac arrest Friday at home in Paris (death 30 Oct 2009)."
    source_quality: "newspaper interview"
    used_for: [basics]
---

## Summary

Claude Lévi-Strauss (1908–2009), anthropologist [S1; S3]. Deepen D1: primary and A BELOW_THRESHOLD (leads AGNOS, ATHE); B UNKNOWN; mid UNKNOWN. Not plotted. Chart-moving NO.

## Life and work

Brussels birth; Paris upbringing; Brazil fieldwork; New York wartime; Paris EPHE and Collège de France [S1; S3]. Died Paris 30 October 2009 [S8; S9].

## Contribution and impact

Structural anthropology; Structures élémentaires (1949); Tristes Tropiques (1955); Mythologiques through L'Homme nu (1971) [S1; S3].

## Childhood and education

Rabbi grandfather at Versailles; unbelieving parents; lycée then Sorbonne agrégation [S1; S3].

## Adult working worldview

Lifelong religious indifference in own voice (Time 1966 in-span; INA 1972 near-span) [S4; S1]. Eribon 1988 lines still second-hand [S5; S6]. Tristes Tropiques religion passages are comparative critique, not a creed [S7]. No scored profession — BELOW_THRESHOLD.

## Heritage (context only)

French Jewish by descent; non-practicing parental household [S1; S3].

## Timing

1949–1971, age 41 at first lasting work [S1; S3]. In-span indifference (1966) does not name a system.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Structural method ≠ scored physics. B UNKNOWN (not a scientist).

## Open questions

- Full De près et de loin / Conversations (1988/1991) primary.
- Full Tristes Tropiques Plon religion chapters.
- Original Time 8 Apr 1966 page.

## Research log

- 2026-10-19: Read the INA interview pages.
- 2026-10-24: Deepen D1 — INA re-open; Time 1966 via CNN reprint; TT attributed excerpt; Eribon still V3; Wiki + Académie + NYT dual bio; Britannica 403; keep BELOW/UNKNOWN; chart NO.
