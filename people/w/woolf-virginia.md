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
    - {date: 2026-10-17, by: "Grok Bot", summary: "Record created (stage 3 batch M, order P32: F 5, rank 79). Basics from Britannica (Panthea Reid, signed; body only). Worldview from 'A Sketch of the Past' (memoir, 1940–41, published 1976) quoted by Ryan (2012, Glasgow PhD) and the 1928 letter to Vanessa Bell quoted by Tóibín (LRB, 2014): secondary quotations, primary check pending. primary_system ATHE (0.5, alt AGNOS); A 4 (0.7); B UNKNOWN (P16); mid_basin false (0.7, A ≥ 3 branch). Not plotted. Draft, not reviewed."}
    - {date: 2026-10-17, by: "Grok Bot", summary: "Batch M audit fixes (/workspace/genius_study_audit/gs_159d60d_M/run1/, run 1: 16 hold, 3 weaken): memoir dated 1939–40 (date field 1939), MB p. 85 noted as the Pimlico page (Harcourt pp. 71–72); SECHUM named as the better alternative to AGNOS. Values unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #78, F5 rank 79). Needs: B UNKNOWN. Primaries/secondaries: Ryan thesis re-checked (S2, MB 85 quote); LRB Tóibín re-checked (S3, 1928 Eliot letter); Wayback 2020 UAH Sketch quotations page (S5) as independent web transcription of Harcourt pp. 71–72; LitHub Bellot 2017 (S6) long quote of same Sketch passage + diary/letter leads (Einstein 20 Mar 1926; 'Oh, how I loathe religion' to Ethel Smyth 1934; 'anti-religious bias'); Wikipedia EN dual bio (S7, P50); Humanists UK heritage page (S8). P47 on S1–S8. A 4 @0.7 stays; support field added as corroborated (S2+S5 memoir streams; S3+S6 letter streams). B stays UNKNOWN after P16 check: Sketch 'pattern' / 'world is a work of art' is aesthetic-immanent philosophy, not nature's causal order; diary 20 Mar 1926 Einstein/'foretell our own lives' reports a dinner argument 'passing my limits', not her creed; early 'vast living thing' nature notes and fiction 'little miracles' not scored. D UNKNOWN→4 @0.5 corroborated (loathe religion / anti-religious bias / Eliot letter / no-God Sketch). C stays UNKNOWN (no clear own-words afterlife denial; Clarissa Dalloway 'cease completely' is fiction). primary_system ATHE @0.5 alt SECHUM unchanged (naturalism half still unstated; pattern-mysticism softens ATHE). mid_basin false @0.7 (A≥3 branch). Chart-moving NO (B UNKNOWN; still unplottable for A&B fill). Moments of Being print / Letters III scholarly volumes still unread (IA borrow gated). No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: woolf-virginia
  display_name: "Virginia Woolf"
  roster:
    canonical_name: "Virginia Woolf"
    rank: 79
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: literature
    field_bucket: literature
  full_name: {value: "Adeline Virginia Woolf, née Stephen", certainty: 0.7, cites: [{source: S1, locator: "header; 'Early life and influences' ('Born Virginia Stephen')"}, {source: S7, locator: "infobox birth_name Adeline Virginia Stephen"}], how_known: "Britannica + Wikipedia (P50)."}
  native_name: {value: UNKNOWN, how_known: "English."}
  aliases:
    - {name: "Virginia-Woolf", kind: "roster alias"}
    - {name: "Woolf-Virginia", kind: "roster alias"}

basics:
  birth:
    date: {value: "1882-01-25", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "infobox"}], how_known: "Two sources."}
    place: {value: "London, England", modern_name: "London, United Kingdom", polity_then: "United Kingdom", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "infobox (South Kensington / Hyde Park Gate)"}], how_known: "Two sources."}
  death:
    date: {value: "1941-03-28", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "infobox"}], how_known: "Two sources."}
    place: {value: "near Rodmell, Sussex, England", modern_name: "Rodmell, East Sussex, United Kingdom", polity_then: "United Kingdom", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "infobox / death (River Ouse)"}], how_known: "Two sources."}
  first_lasting_contribution_year: {value: 1922, certainty: 0.5, cites: [{source: S1, locator: "'Mrs. Dalloway, To the Lighthouse, ...' (Jacob's Room)"}, {source: S7, locator: "notable works"}], how_known: "In Jacob's Room (1922) 'she achieved such emotion' (S1): the earliest novel the body marks as an achievement (P13). The Voyage Out (1915) is dated but not so marked. 0.5 because the choice is the coder's."}
  era_bucket: {value: "1850 to 1949", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "From 1922 (P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "United Kingdom (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S7, locator: "Life"}], how_known: "London and Sussex."}
  sex_as_recorded: {value: "female", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [English], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
  occupations: {value: ["novelist", "essayist", "publisher (Hogarth Press)"], certainty: 0.7, cites: [{source: S1, locator: "opening; Hogarth Press paragraph"}, {source: S7, locator: "infobox occupations"}], how_known: "Two sources."}

contribution:
  fields: {value: ["fiction", "essays", "literary criticism"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Jacob's Room", year: 1922, kind: work, lasting: "'she achieved such emotion' (S1)", certainty: 0.7, cites: [{source: S1, locator: "major works section"}, {source: S7, locator: "notable works"}], how_known: "Two sources."}
    - {value: "Mrs. Dalloway", year: 1925, kind: work, lasting: "among the novels she 'is best known for' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "notable works"}], how_known: "Two sources."}
    - {value: "To the Lighthouse", year: 1927, kind: work, lasting: "among the novels she 'is best known for' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "notable works"}], how_known: "Two sources."}
    - {value: "Between the Acts", year: 1941, kind: work, lasting: "worked on during the bombing of London, 1940–41 (S1)", certainty: 0.5, cites: [{source: S1, locator: "major works section"}], how_known: "Britannica; published after her death; lasting status is the coder's reading."}
  evidence_of_impact:
    - {value: "Her novels 'exerted a major influence on the genre'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Agnostic / freethinking household (both parents prominent agnostic atheists; father Leslie Stephen public agnostic and ethical-society figure; mother Julia Stephen wrote Agnostic Women)", certainty: 0.7, cites: [{source: S7, locator: "Views / Humanist views"}, {source: S8, locator: "Life (Leslie and Julia Stephen)"}], how_known: "Wikipedia + Humanists UK."}
  family_religious_practice: {value: "No church Christianity as household creed; freethinking / ethical-society milieu (father President, West London Ethical Society; helped found Union of Ethical Societies, 1896)", certainty: 0.7, cites: [{source: S7, locator: "Views / Humanist views"}, {source: S8, locator: "Life"}], how_known: "Two sources."}
  parents_and_household:
    - {value: "Father Leslie Stephen, literary figure, first editor of the Dictionary of National Biography; public agnostic", role: father, certainty: 0.7, cites: [{source: S1, locator: "'Early life and influences'"}, {source: S7, locator: "Early life / Humanist views"}], how_known: "Two sources."}
    - {value: "Mother Julia Jackson (Duckworth / Prinsep); model, philanthropist; wrote Agnostic Women (1880)", role: mother, certainty: 0.7, cites: [{source: S1, locator: "'Early life and influences'"}, {source: S7, locator: "Early life / Humanist views"}, {source: S8, locator: "Life"}], how_known: "Three sources."}
  household_circumstances: {value: "Blended literary upper-middle-class household at 22 Hyde Park Gate, Kensington; summers in Cornwall (Talland House, St Ives)", certainty: 0.7, cites: [{source: S7, locator: "Early life"}, {source: S8, locator: "Life"}], how_known: "Two sources."}
  schooling:
    - {value: "Educated largely at home; attended classes at King's College London (Ladies' Department)", stage: "university", run_by: other, certainty: 0.7, cites: [{source: S7, locator: "infobox Education; Early life"}, {source: S1, locator: "'Early life and influences'"}], how_known: "Wikipedia names King's College London; Britannica home education."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [English], certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  notable_events:
    - {value: "Mother Julia died 1895; father Leslie died 1904; brother Thoby died 1906 — successive family deaths in adolescence/early adulthood", certainty: 0.7, cites: [{source: S7, locator: "Early life"}, {source: S8, locator: "Life"}], how_known: "Two sources."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1922–1941", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Bloomsbury Group (secular / freethinking literary circle; no church membership read)", certainty: 0.7, cites: [{source: S7, locator: "Bloomsbury"}, {source: S8, locator: "Life"}], how_known: "Two sources; affiliation is social, not a creed code."}
  self_described_science_religion_relation: {value: "Interest in contemporary physics (Einstein dinner talk, 1926) with explicit anti-religious bias; 1938 said she 'had not read Einstein; I should not understand it' while discussing his 'extra mundane influence upon fiction' (S6). No systematic science-vs-religion essay read.", certainty: 0.5, cites: [{source: S6, locator: "Einstein diary 1926; Nielsen letter 1938"}], how_known: "LitHub quotation of diary and letter; primary Diary / Letters volumes unread this pass."}
  primary_system:
    value: ATHE
    basis: consistent_private_letters
    certainty: 0.5
    cites: [{source: S2, locator: "Introduction, p. 1 (PDF p. 8), quoting MB 85"}, {source: S5, locator: "UAH Sketch quotations (Harcourt pp. 71–72)"}, {source: S3, locator: "Woolf letter quoted"}, {source: S6, locator: "'anti-religious bias'; 'Oh, how I loathe religion'"}]
    rationale: "'certainly and emphatically there is no God' (memoir) and 'there's something obscene in a living person sitting by the fire and believing in God' (1928 letter); 'Oh, how I loathe religion' / 'anti-religious bias' (S6). Named alternative: SECHUM (denial of God without stated naturalism; no humanist-society membership statement read as her own). ATHE's naturalism half is not stated; the same Sketch passage holds that 'behind the cotton wool is hidden a pattern' and 'the whole world is a work of art' (soft mystic-immanent language)."
    how_known: "Memoir + private letters in working years, now cross-checked across independent secondary streams (Ryan; UAH/LitHub Sketch wording; LRB letter). 0.5: naturalism half of ATHE unstated; SECHUM named; Moments of Being / Letters III print volumes unread (P26)."
    alternatives:
      - {value: SECHUM, note: "Denial of God without stated naturalism; pattern/art mysticism; parents' ethical-society humanism is heritage, not her membership statement.", cites: [{source: S2, locator: "MB 85"}, {source: S8, locator: "Life"}]}
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: ATHE, reason: "Explicit denial of God in memoir and hostile letter on belief."}
    - {code: SECHUM, reason: "Better alternative to ATHE: denial without stated naturalism; no own membership statement read."}
    - {code: AGNOS, reason: "Weak: her own words are a denial, not a suspension of judgement."}
  lio_axes:
    A_locus:
      value: 4
      basis: consistent_private_letters
      certainty: 0.7
      support: corroborated
      cites: [{source: S2, locator: "Introduction quoting MB 85"}, {source: S5, locator: "UAH Sketch quotations, Harcourt pp. 71–72"}, {source: S3, locator: "1928 letter to Vanessa Bell"}, {source: S6, locator: "LitHub long quote of Sketch + Eliot letter"}]
      how_known: "Memoir + private letter in the working years, consistent (0.7 ceiling, §3). Support corroborated (P48): Ryan thesis (S2) + independent UAH/LitHub Sketch wording (S5/S6); LRB (S3) + LitHub (S6) on the Eliot letter. Moments of Being / Letters III print still unread — not above 0.7 (P26)."
      rationale: "No God (A 4 for a denial, P38): 'certainly and emphatically there is no God; we are the words; we are the music; we are the thing itself' (Sketch, 1939–40), and on Eliot's conversion, 'there's something obscene in a living person sitting by the fire and believing in God' (letter, 1928). Immanent 'we are the thing itself' language fits A 4 rather than a transcendent blank."
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30/P33). For a non-scientist, B needs an explicit remark on the order of nature — laws, miracles in nature, chance vs necessity (P16). Checked and left unscored: (1) Sketch 'pattern' behind 'cotton wool' / 'the whole world is a work of art' is aesthetic-immanent philosophy, not causal law vs exception; (2) diary ~20 Mar 1926 records a Clive Bell dinner argument 'passing my limits — how, if Einstein is true, we shall be able to foretell our own lives' (S6) — reporting others' speculation, not her creed; (3) early 'vast living thing' nature notes and fiction 'little daily miracles' (To the Lighthouse characters) are not own-words causal-order professions. Deliberately not scored."}
    C_ledger: {value: UNKNOWN, how_known: "Eliot's belief in 'immortality' is reported with shock, not answered by her own afterlife creed. Clarissa Dalloway's 'cease completely' (S8) is fiction. Nothing read that maps personal reward/punishment."}
    D_authority:
      value: 4
      basis: consistent_private_letters
      certainty: 0.5
      support: corroborated
      cites: [{source: S3, locator: "1928 Eliot letter"}, {source: S6, locator: "'Oh, how I loathe religion' (to Ethel Smyth, 1934); 'anti-religious bias'"}, {source: S2, locator: "MB 85 no God"}]
      how_known: "Private letters + memoir denial. Support corroborated (S3+S6+S2). 0.5: no single sentence that says 'reason outranks revelation' in those words; the score is the coder's reading of hostility to religious authority / belief."
      rationale: "Observation and secular reason over revelation: loathes religion, names an 'anti-religious bias', finds belief in God 'obscene', and denies God. Church and conversion treated as deadening, not authoritative."
    E_scope: {value: UNKNOWN, how_known: "Nothing read on same laws everywhere (P7)."}
  mid_basin: {value: false, certainty: 0.7, cites: [{source: S2, locator: "MB 85"}, {source: S3, locator: "Woolf letter quoted"}, {source: S5, locator: "UAH Sketch quotations"}], how_known: "A 4 at 0.7: the A ≥ 3 branch reads A only (P10), so B UNKNOWN does not block mid_basin false."}
  statements:
    - text: "But there is no Shakespeare, there is no Beethoven; certainly and emphatically there is no God; we are the words; we are the music; we are the thing itself."
      cites: [{source: S2, locator: "Introduction quoting MB 85"}, {source: S5, locator: "UAH Sketch quotations (Harcourt pp. 71–72)"}, {source: S6, locator: "LitHub long quote"}]
      date: "1939"
      context: "'A Sketch of the Past', memoir written 1939–40 (date field = start year), published in Moments of Being (1976). MB p. 85 is the Pimlico edition Ryan cites; Harcourt editions place the passage at pp. 71–72 (S5). Follows 'that behind the cotton wool is hidden a pattern ... that the whole world is a work of art'."
      axes: [A_locus, D_authority]
      kind: "unpublished manuscript"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Wording agreed across Ryan (S2), UAH Wayback transcription (S5), and LitHub (S6). Moments of Being print still unread (IA borrow gated); P26 ceiling holds."
    - text: "I have had a most shameful and distressing interview with poor dear Tom Eliot, who may be called dead to us all from this day forward. He has become an Anglo-Catholic, believes in God and immortality, and goes to church. I was really shocked. A corpse would seem to me more credible than he is. I mean, there’s something obscene in a living person sitting by the fire and believing in God."
      cites: [{source: S3, locator: "Woolf letter quoted"}, {source: S6, locator: "LitHub quotation of same letter"}]
      date: "1928-02-11"
      context: "To her sister Vanessa Bell, on Eliot's conversion. Month/day from secondary leads (Cambridge Companion / Lives of Unbelievers); Letters III: 457–58 unread this pass."
      axes: [A_locus, D_authority]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "LRB (S3) and LitHub (S6) agree on wording. Letters vol. III print unread (P26)."
    - text: "I wanted, like a child, to stay and argue […] how if Einstein is true, we shall be able to foretell our own lives."
      cites: [{source: S6, locator: "diary entry ~20 March 1926 at Clive Bell's (Diary vol. 3, p. 68 in secondary cites)"}]
      date: "1926-03-20"
      context: "Diary: dinner conversation; argument 'passing my limits'. Checked for B and left off B (P16): reports others' speculation about Einstein, not her own profession on nature's causal order."
      axes: [B_cause]
      kind: "notebook or diary"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "LitHub / PhiN / Modernist Review secondary quotes; Diary of Virginia Woolf vol. 3 print unread."
    - text: "Oh, how I loathe religion"
      cites: [{source: S6, locator: "letter to Ethel Smyth, 1934"}]
      date: "1934"
      context: "To Ethel Smyth; LitHub also notes Smyth's diary that Woolf 'has no conception' of religion, and Woolf's own phrase 'an anti-religious bias'."
      axes: [D_authority, A_locus]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Secondary quotation only this pass."
  changes_over_life:
    - {value: "Raised in parents' agnostic/freethinking household; adult working years show explicit no-God memoir language and hostility to Christian conversion (Eliot 1928), with ongoing interest in popular physics talk without a scored B.", year: 1928, certainty: 0.5, cites: [{source: S7, locator: "Humanist views"}, {source: S3, locator: "Eliot letter"}, {source: S2, locator: "MB 85"}], how_known: "Heritage vs working-years documents."}
  coder_notes: "Deepen D1: queue need was B UNKNOWN. B left UNKNOWN after Einstein-diary and Sketch-pattern checks (P16). A support field set corroborated (was already two streams). D newly 4 @0.5. Chart-moving NO. Lane A scores separate from Lane B geometric labels. No fallacy_catalog (Jason)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "English", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "lead"}], how_known: "Two sources."}
  religious_heritage_by_birth: {value: "Agnostic / freethinking (both parents prominent agnostic atheists; father ethical-society president; mother Agnostic Women)", certainty: 0.7, cites: [{source: S7, locator: "Humanist views"}, {source: S8, locator: "Life"}], how_known: "Two sources."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Nothing read that records infant baptism; freethinking household makes it unlikely, but no document read."}
  childhood_catechism: {value: UNKNOWN, how_known: "Nothing read on formal catechism; aunt Caroline Stephen (Quaker) was a later influence per Wikipedia, not a childhood catechism."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1922–1941", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "First to last listed lasting contribution (P29, P30); start and end are the coder's picks."}
  age_at_first_lasting_contribution: {value: 40, certainty: 0.5, cites: [{source: S1, locator: "opening; 1922"}], how_known: "1922 − 1882 = 40 (P30)."}
  first_evidence_of_lio_type_views: {value: "1928: mocks belief in God in a letter on Eliot's conversion", year: 1928, certainty: 0.5, cites: [{source: S3, locator: "Woolf letter quoted"}], how_known: "Earlier letters and diaries not fully read (P30 #7); 1926 Einstein diary is not LIO-scored."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.5, cites: [{source: S3, locator: "Woolf letter quoted"}, {source: S2, locator: "MB 85"}], how_known: "1928 and 1939–40, inside 1922–1941."}
  worldview_during_major_work: {value: "No God; immanent 'we are the thing itself' / pattern behind appearances; hostility to Christian belief and conversion", certainty: 0.5, cites: [{source: S2, locator: "MB 85"}, {source: S3, locator: "Eliot letter"}], how_known: "Memoir + letter."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Modernist form experiments; no Euclidean ideal-geometry theology read.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Nothing read."}
  circle_present: {value: "no", rationale: "No God as source or end; pattern/art is not a return-to-source circle.", certainty: 0.5, cites: [{source: S2, locator: "MB 85"}], how_known: "Coder's reading."}
  reading: "No God; immanent pattern; anti-religious bias. Lane B separate from Lane A axis scores."
  notes: "Einstein interest is literary/cultural (S6), not a Lane A B_cause score."

institutions:
  - {value: "Hogarth Press (co-founder, 1917)", role: founder, years: "1917–1941", kind: other, certainty: 0.7, cites: [{source: S1, locator: "Hogarth Press paragraph"}, {source: S7, locator: "Hogarth Press"}], how_known: "Two sources."}
  - {value: "King's College London (Ladies' Department classes)", role: student, years: "c. 1897–1901", kind: university, certainty: 0.5, cites: [{source: S7, locator: "infobox Education / Early life"}], how_known: "Wikipedia; exact years soft."}
collaborators:
  - {value: "Leonard Woolf", relation: family, note: "husband; co-founder of the Hogarth Press", certainty: 0.7, cites: [{source: S1, locator: "Hogarth Press paragraph"}, {source: S7, locator: "infobox spouse"}], how_known: "Two sources."}
  - {value: "Vanessa Bell", relation: family, note: "sister; recipient of 1928 Eliot letter", certainty: 0.7, cites: [{source: S3, locator: "letter"}, {source: S7, locator: "Early life"}], how_known: "Two sources."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 79"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Moments of Being and Letters vol. III print editions unread (IA borrow / download gated); Sketch and Eliot-letter wording corroborated across secondary streams only (P26)."
    - "B left UNKNOWN after Einstein-diary and Sketch-pattern P16 checks."
  open_questions:
    - "Read Moments of Being (Schulkind) and Letters III: 457–58 against print for primary verified_against upgrade."
    - "Diary vols for any explicit own-words remark on laws of nature / miracles / chance that would score B under P16."
    - "Full Ethel Smyth 1934 letter and Nielsen 1938 Einstein letter in Letters volumes."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Panthea Reid"
    citation: "Reid, Panthea. \"Virginia Woolf.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Virginia-Woolf. Read in Wayback snapshots: main page 2026-09-08 22:14:20 UTC; major works section 20260831164516; 'Legacy' 20250812193713."
    url: "https://www.britannica.com/biography/Virginia-Woolf"
    accessed: 2026-10-17
    source_quality: "reference entry"
    reliability_note: "Signed article (Professor of English Emerita, LSU). Body only; Q&A boxes and Top Questions not cited. Create-pass body retained this deepen (P50 dual with Wikipedia)."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: secondary
    kind: other
    author: "Derek Ryan"
    citation: "Ryan, Derek. Virginia Woolf and the materiality of theory: sex, animal, life. PhD thesis, University of Glasgow, 2012. https://theses.gla.ac.uk/3408/."
    url: "https://theses.gla.ac.uk/3408/1/2012ryanphd.pdf"
    accessed: 2026-10-24
    source_quality: "scholarly edition or monograph"
    reliability_note: "Doctoral thesis, read directly (PDF); quotes 'A Sketch of the Past' from Moments of Being (MB 85) in its introduction. Re-checked 2026-10-24."
    used_for: [worldview, timing, lane_b]
  - id: S3
    type: secondary
    kind: other
    author: "Colm Tóibín"
    citation: "Tóibín, Colm. \"Putting Religion in Its Place.\" London Review of Books 36, no. 20 (23 October 2014). https://www.lrb.co.uk/the-paper/v36/n20/colm-toibin/putting-religion-in-its-place."
    url: "https://www.lrb.co.uk/the-paper/v36/n20/colm-toibin/putting-religion-in-its-place"
    accessed: 2026-10-24
    source_quality: "other"
    reliability_note: "Signed review essay, read directly; quotes the 1928 letter in full and dates it to 1928. Re-checked 2026-10-24."
    used_for: [worldview, timing, collaborators]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-17
    source_quality: "study roster"
    reliability_note: "Study's own roster."
    used_for: [identity, review]
  - id: S5
    type: secondary
    kind: other
    author: "University of Alabama in Huntsville (Woolf course page)"
    citation: "\"Quotations for Discussion from A Sketch of the Past.\" UAH Woolf site (Harcourt Moments of Being pp. 71–72 transcription). https://www.uah.edu/woolf/sketchquotes.html. Live 404 on 2026-10-24; read via Wayback Machine 2020 snapshot."
    url: "https://web.archive.org/web/2020/https://www.uah.edu/woolf/sketchquotes.html"
    accessed: 2026-10-24
    source_quality: "unofficial web copy"
    reliability_note: "Teaching-page transcription of Harcourt edition pages; independent of Ryan's Pimlico MB 85 cite for P48 corroboration of Sketch wording. Not a critical edition."
    used_for: [worldview]
  - id: S6
    type: secondary
    kind: other
    author: "Gabrielle Bellot"
    citation: "Bellot, Gabrielle. \"How Much of Einstein’s Theory of Relativity is in the Writing of Virginia Woolf?\" Literary Hub, 10 August 2017. https://lithub.com/how-much-of-einsteins-theory-of-relativity-is-in-the-writing-of-virginia-woolf/."
    url: "https://lithub.com/how-much-of-einsteins-theory-of-relativity-is-in-the-writing-of-virginia-woolf/"
    accessed: 2026-10-24
    source_quality: "other"
    reliability_note: "Signed essay; long quote of Sketch no-God passage; secondary quotes of diary 20 Mar 1926 Einstein argument, Ethel Smyth 1934 'loathe religion', 'anti-religious bias', and Nielsen 1938 Einstein letter. Used for B-check and D support; Diary/Letters print unread."
    used_for: [worldview, timing]
  - id: S7
    type: secondary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "\"Virginia Woolf.\" Wikipedia. https://en.wikipedia.org/wiki/Virginia_Woolf (infobox; Early life; Humanist views; Hogarth Press)."
    url: "https://en.wikipedia.org/wiki/Virginia_Woolf"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Dual bio with Britannica (P50). Used for Adeline name, dates, parents' agnosticism, King's College, death at Rodmell — not for LIO scores."
    used_for: [identity, basics, contribution, childhood, heritage, timing, institutions, collaborators]
  - id: S8
    type: secondary
    kind: institutional page
    author: "Humanists UK"
    citation: "Humanists UK. \"Virginia Woolf (1882-1941).\" Humanist Heritage. https://heritage.humanists.uk/virginia-woolf/."
    url: "https://heritage.humanists.uk/virginia-woolf/"
    accessed: 2026-10-24
    source_quality: "other"
    reliability_note: "Advocacy/heritage page; useful for Leslie/Julia Stephen freethinking context and Sybil Oldfield bond-in-atheism remark. Fiction (Mrs Dalloway) lines not used for LIO scores."
    used_for: [childhood, heritage, collaborators]
---

# Virginia Woolf

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Virginia Woolf (1882–1941), English novelist and essayist [S1; S7]. Deepen D1: primary_system ATHE (0.5, alt SECHUM); A 4 @0.7 corroborated; B UNKNOWN; D 4 @0.5; mid_basin false (0.7). Chart-moving NO.

## Life and work

Born Adeline Virginia Stephen; Hogarth Press from 1917; died Rodmell 1941 [S1; S7].

## Contribution and impact

Jacob's Room (1922), Mrs. Dalloway (1925), To the Lighthouse (1927) [S1; S7].

## Childhood and education

Daughter of Leslie Stephen and Julia Jackson; agnostic/freethinking household; King's College London classes [S1; S7; S8].

## Adult working worldview

'certainly and emphatically there is no God' (Sketch, 1939–40) [S2; S5; S6]; 1928 Eliot letter [S3; S6]. B left UNKNOWN after Einstein-diary and pattern checks [S6; S2].

## Heritage (context only)

English; parents prominent agnostic atheists [S7; S8].

## Timing

First lasting contribution 1922, at 40 [S1]. LIO-type evidence during major work [S3; S2].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No circle [S2].

## Open questions

- Moments of Being / Letters III print primary check.
- Diary own-words for P16 B.

## Research log

- 2026-10-17: Britannica (Reid); Ryan thesis; Tóibín LRB.
- 2026-10-24: Deepen D1. Ryan re-check; LRB re-check; Wayback UAH Sketch quotations [S5]; LitHub Bellot [S6]; Wikipedia [S7]; Humanists UK [S8]. IA Moments of Being borrow gated. B stays UNKNOWN.
