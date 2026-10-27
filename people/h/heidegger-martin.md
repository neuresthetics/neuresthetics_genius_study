---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch U)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to 20c_early. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Batch V audit note (gs_982cb8e_V run 1, UF8 follow-up): S1 now cites all Britannica contributors, Arne D. Naess, Richard Wolin and Britannica Editors. No value changes."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Audit fixes for batch U (gs_59bb9fc_U run 1): HE4, the later essays and lectures listed as one body-of-work contribution (1946–1964; SEP for lasting, IEP for dates), span and working_years 1927 -> 1927–1964; note, the dates of the break with Catholicism (Britannica 1916–17, IEP 9 January 1919) in changes_over_life. No scored value changes."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch U, order P32: F 4, rank 115). Basics from Britannica (Arne D. Naess), SEP (Mark Wrathall) and IEP (W. J. Korab-Karpowicz). No text of his own on God or nature read: Phänomenologie und Theologie (1927) and the 1919 letter are leads only (P26). Not a scientist (P30). primary_system BELOW_THRESHOLD; A BELOW_THRESHOLD; B UNKNOWN; C UNKNOWN; D BELOW_THRESHOLD; E UNKNOWN; mid_basin UNKNOWN. Single-year span 1927 (Being and Time). Not plotted. Draft, not reviewed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #114 / F4 rank 115). Goals: Pathmarks / Phänomenologie und Theologie primary if reachable; keep A/B honest. Read Wegmarken GA 9 (Klostermann; S5 heidegger.ru PDF OCR): Phänomenologie und Theologie (1927) and Brief über den Humanismus (1946). Dual bio Wikipedia EN (S6, P50). P47 source_quality on S1–S6. A stays BELOW (PT characterizes Christian faith's 'gekreuzigte Gott' as theology's positum, not his locus; Humanism: Sein ≠ Gott / Weltgrund; thinking neither theistic nor atheistic — no clear A). B UNKNOWN→BELOW (philosopher, P16/P30: physis essay and Humanism Natur as Seiende in clearing, no own-voice natural-law / exception claim). D BELOW→2 @0.7 written_profession support single (S5): theology 'absolut verschieden' from philosophy; faith Todfeind of free Existenz; no Christian philosophy (GA 9:48–49, 66). C/E UNKNOWN. mid UNKNOWN→BELOW (A and B both BELOW, P19). primary BELOW unchanged. first_evidence LIO 1927 (PT for D). Chart-moving NO. Krebs 1919 letter still secondary-only; Spiegel 1966 after span. No fallacy_catalog. No figures/. Draft, not reviewed."}

identity:
  id: heidegger-martin
  display_name: "Martin Heidegger"
  roster:
    canonical_name: "Martin Heidegger"
    rank: 115
    F: 4
    models: [Claude, DeepSeek, Gemini, Grok]
    band: "core (3–4)"
    status: core
    field: philosophy
    field_bucket: philosophy
  full_name: {value: "Martin Heidegger", certainty: 0.7, cites: [{source: S1, locator: "facts box"}, {source: S2, locator: "§1 Life and Work"}], how_known: "Britannica and SEP."}
  native_name: {value: "Martin Heidegger", certainty: 0.7, cites: [{source: S1, locator: "facts box"}], how_known: "German; same as the full name."}
  aliases:
    - {name: "Heidegger-Martin", kind: "roster alias"}

basics:
  birth:
    date: {value: "1889-09-26", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "facts box (Born)"}, {source: S2, locator: "§1 Life and Work"}, {source: S3, locator: "§1 Life and Works"}, {source: S6, locator: "lead / Infobox"}], how_known: "Britannica, SEP, IEP and Wikipedia EN (P50 dual bio) agree."}
    place: {value: "Messkirch", modern_name: "Meßkirch, Baden-Württemberg, Germany", polity_then: "Grand Duchy of Baden, German Empire", certainty: 1.0, cites: [{source: S1, locator: "facts box (Born)"}, {source: S2, locator: "§1 Life and Work"}], how_known: "Britannica and SEP; polity the coder's."}
  death:
    date: {value: "1976-05-26", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "facts box (Died)"}, {source: S3, locator: "§1 Life and Works, last paragraph"}, {source: S6, locator: "lead / Infobox"}], how_known: "Britannica, IEP and Wikipedia EN (P50)."}
    place: {value: "Freiburg im Breisgau", modern_name: "Freiburg im Breisgau, Germany", polity_then: "West Germany", certainty: 0.7, cites: [{source: S1, locator: "facts box (Died)"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1927, certainty: 0.7, cites: [{source: S2, locator: "§1 Life and Work"}, {source: S3, locator: "§1 Life and Works"}], how_known: "Being and Time, published February 1927 (S3)."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S3, locator: "§1 Life and Works"}], how_known: "1927 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 1.0, cites: [{source: S1, locator: "facts box"}], how_known: "Germany (P3)."}
  region_of_work: {value: "Western Europe", certainty: 1.0, cites: [{source: S2, locator: "§1 Life and Work"}, {source: S3, locator: "§1 Life and Works"}], how_known: "Freiburg and Marburg."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S2, locator: "§1 Life and Work"}], how_known: "Pronouns in SEP."}
  languages_of_work: {value: ["German"], certainty: 0.7, cites: [{source: S2, locator: "§1 Life and Work"}], how_known: "Coder's reading."}
  occupations: {value: ["philosopher", "university lecturer and professor (Freiburg, Marburg)", "rector of the University of Freiburg (1933–1934)"], certainty: 0.7, cites: [{source: S2, locator: "§1 Life and Work"}, {source: S3, locator: "§1 Life and Works"}], how_known: "SEP and IEP."}

contribution:
  era_bucket: 20c_early
  fields: {value: ["philosophy", "phenomenology", "ontology"], certainty: 0.7, cites: [{source: S2, locator: "opening"}, {source: S3, locator: "opening"}], how_known: "SEP and IEP."}
  lasting_original_contributions:
    - {value: "Being and Time (Sein und Zeit): the question of the meaning of being pursued through a phenomenological analysis of human existence (Dasein) and its temporality", year: 1927, kind: work, lasting: "'his most important work' (S2); 'recognized as a truly epoch-making work of 20th century philosophy' and 'his most influential work' (S3)", certainty: 1.0, cites: [{source: S2, locator: "opening; §1 Life and Work"}, {source: S3, locator: "§1 Life and Works; §3"}], how_known: "SEP and IEP. The first lasting contribution; the later essays and lectures are listed below (HE4). Not a theory about natural systems, so not a scientist (P30)."}
    - {value: "Later essays and lectures on modernity, technology, language and the history of being (among them 'What are Poets for?' 1946, 'Letter on Humanism' 1947, 'The Question Concerning Technology' 1953, 'The Way to Language' 1959, 'Time and Being' 1962, 'The End of Philosophy and the Task of Thinking' 1964)", year: 1946, kind: "body of work", lasting: "'His magnum opus, Being and Time (1927), and his many essays and lectures, profoundly influenced subsequent movements' (S2, opening)", certainty: 0.5, cites: [{source: S2, locator: "opening"}, {source: S3, locator: "§1 Life and Works (last three decades)"}], how_known: "SEP for lasting, IEP for the dates (range 1946–1964; P12 start, P30 end of range). Listed in the batch U audit fixes (HE4, P30 addendum b). 0.5: SEP names the essays as a class, IEP lists the examples."}
  evidence_of_impact:
    - {value: "Being and Time influenced Arendt, Sartre, Beauvoir, Merleau-Ponty, Gadamer, Derrida, Foucault, Deleuze, the Frankfurt School, the Kyoto School and fields from theology to cognitive science", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S2, locator: "opening"}], how_known: "SEP."}
    - {value: "Being and Time 'generated a level of excitement that few other works of philosophy have matched'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "'Being and Time'"}], how_known: "Britannica."}
  major_works:
    - {value: "Sein und Zeit (Being and Time)", year: 1927, certainty: 1.0, cites: [{source: S2, locator: "§1 Life and Work"}, {source: S3, locator: "§1 Life and Works"}], how_known: "SEP and IEP."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Being and Time 'profoundly influenced' twentieth-century philosophy (S2).", certainty: 0.7, cites: [{source: S2, locator: "opening"}], how_known: "SEP."}

childhood:
  family_religion: {value: "Catholic", certainty: 1.0, cites: [{source: S2, locator: "§1 Life and Work"}, {source: S3, locator: "§1 Life and Works"}, {source: S6, locator: "Early years"}], how_known: "Father a sexton in the Catholic Church (S2); 'a Catholic family' (S3); Wikipedia EN concurs (P50)."}
  family_religious_practice: {value: "Father served as sexton of the local church; the son was prepared for the priesthood", certainty: 0.7, cites: [{source: S3, locator: "§1 Life and Works"}], how_known: "IEP."}
  parents_and_household:
    - {value: "Father: Friedrich Heidegger, master cooper and sexton in the Catholic Church", certainty: 1.0, cites: [{source: S2, locator: "§1 Life and Work"}, {source: S3, locator: "§1 Life and Works"}], how_known: "SEP and IEP."}
  household_circumstances: {value: "Provincial craftsman's family in a small rural town; conservative upbringing", certainty: 0.7, cites: [{source: S2, locator: "§1 Life and Work"}], how_known: "SEP."}
  schooling:
    - {value: "High school in Konstanz from 1903, with a church scholarship", stage: "grammar or secondary school", run_by: other, years: "1903–1906", certainty: 0.7, cites: [{source: S3, locator: "§1 Life and Works"}], how_known: "IEP; who ran the school is not stated, the scholarship came from the church."}
    - {value: "High school in Freiburg", stage: "grammar or secondary school", run_by: other, years: "1906–1909", certainty: 0.7, cites: [{source: S3, locator: "§1 Life and Works"}], how_known: "IEP; operator not stated."}
    - {value: "Jesuit novitiate, discharged within a month for health", stage: other, run_by: "religious body", years: "1909", certainty: 0.7, cites: [{source: S3, locator: "§1 Life and Works"}], how_known: "IEP."}
    - {value: "University of Freiburg: Catholic theology (seminary), then philosophy, mathematics and natural sciences; doctorate 1913; habilitation on Duns Scotus 1915", stage: university, run_by: "state or municipal", years: "1909–1915", certainty: 0.7, cites: [{source: S2, locator: "§1 Life and Work"}, {source: S3, locator: "§1 Life and Works"}], how_known: "SEP and IEP; operator the coder's reading (German state university)."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure:
    - {value: "Studied mathematics and natural sciences at Freiburg after leaving the seminary in 1911", certainty: 0.7, cites: [{source: S3, locator: "§1 Life and Works"}], how_known: "IEP."}
  key_early_reading:
    - {value: "Franz Brentano, On the Manifold Meaning of Being according to Aristotle (read at seventeen; 'by his own account' the start of his quest for the meaning of being)", certainty: 0.7, cites: [{source: S3, locator: "§1 Life and Works"}], how_known: "IEP."}
    - {value: "Edmund Husserl, Logical Investigations", certainty: 0.7, cites: [{source: S3, locator: "§1 Life and Works"}], how_known: "IEP."}
  childhood_mentors: []
  languages_in_childhood: {value: ["German"], certainty: 0.5, cites: [{source: S2, locator: "§1 Life and Work"}], how_known: "Coder's reading."}
  notable_events:
    - {value: "Prepared for the priesthood; Jesuit novice in 1909; left the seminary in 1911", certainty: 0.7, cites: [{source: S3, locator: "§1 Life and Works"}], how_known: "IEP."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1927–1964", certainty: 0.5, cites: [{source: S2, locator: "opening; §1 Life and Work"}, {source: S3, locator: "§1 Life and Works"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Raised Catholic; in 1915 'regarded himself as standing in the service of the Catholic world-view'", certainty: 0.7, cites: [{source: S3, locator: "§1 Life and Works"}], how_known: "IEP's report; before the span and before the 1919 break. Context, not a code."}
    - {value: "Buried in the churchyard in Messkirch", certainty: 0.7, cites: [{source: S3, locator: "§1 Life and Works, last paragraph"}], how_known: "IEP. Context only."}
  self_described_science_religion_relation:
    value: "Philosophy and Christian theology (faith) are 'absolut verschieden'; faith as a specific Existenzmöglichkeit remains the 'Todfeind' of philosophy's free self-assumption of Dasein; there is no Christian philosophy ('hölzernes Eisen'). Thinking the truth of Being is neither theistic nor atheistic."
    certainty: 0.7
    cites: [{source: S5, locator: "GA 9:48–49, 66 (Phänomenologie und Theologie); Brief über den Humanismus (neither theistic nor atheistic)"}]
    how_known: "Own words in Wegmarken (GA 9), read this pass (S5)."
  primary_system: {value: BELOW_THRESHOLD, how_known: "Phänomenologie und Theologie (1927) treats 'Christus, der gekreuzigte Gott' as the positum of Christian faith, not as his profession (S5). Brief über den Humanismus: Sein 'ist nicht Gott und nicht ein Weltgrund'; thinking 'kann so wenig … theistisch … wie atheistisch' sein (S5). Break with the 'system of Catholicism' (1919 Krebs letter) remains secondary report (S3). Britannica's 'secularized Protestantism' (S1) is a tone reading. Candidates CHRIST, ATHE and AGNOS all fail a profession in the span."}
  secondary_system: {value: UNKNOWN, how_known: "One system (P29)."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Rejected: broke with the Catholic 'system' (S3, before span); PT characterizes the crucified God as faith's positum, not his own (S5); Humanism refuses theism (S5).", cites: [{source: S5, locator: "GA 9:52–54, Humanismus (neither theistic nor atheistic)"}, {source: S3, locator: "§1 Life and Works"}]}
    - {code: ATHE, reason: "Rejected: Humanism expressly refuses atheism as much as theism (S5); no denial of God.", cites: [{source: S5, locator: "Brief über den Humanismus"}]}
    - {code: AGNOS, reason: "Rejected: no stated suspension of judgment; 'methodological atheism' readings remain secondary leads.", cites: [{source: S5, locator: "Brief über den Humanismus"}]}
    - {code: PANT, reason: "Rejected: Humanism 'Das »Sein« — das ist nicht Gott und nicht ein Weltgrund' undercuts Sein=God (S5).", cites: [{source: S5, locator: "Brief über den Humanismus"}]}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "Primary texts reached (S5) still give no locus. Phänomenologie und Theologie analyzes Christian faith's 'Christus, der gekreuzigte Gott' as theology's positum (GA 9:52–54), not Heidegger's own place for God. Brief über den Humanismus: Sein 'ist nicht Gott und nicht ein Weltgrund'; whether 'der Gott und die Götter' arrive is Geschick, not a scored locus; thinking is neither theistic nor atheistic. Hedged BELOW (task: keep BELOW if still no locus)."}
    B_cause: {value: BELOW_THRESHOLD, how_known: "Not a scientist (P30). Philosopher: score B only from own-voice nature / physical-world claims (P16). Wegmarken read: 'Vom Wesen und Begriff der Φύσις' is Aristotelian ontology of physis, not natural-law vs exception; Humanism treats Natur as Seiende that may enter the clearing of Being. Nothing read states lawful order with or without miracle/exemption → BELOW (P19), was UNKNOWN before the primary read."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing on reward and punishment of persons read (P19). PT's faith-as-Wiedergeburt is theological characterization, not a ledger of personal deserts."}
    D_authority:
      value: 2
      basis: written_profession
      certainty: 0.7
      support: single
      cites: [{source: S5, locator: "GA 9:48–49, 66"}]
      how_known: "Own 1927 lecture text in Wegmarken (GA 9), read this pass. Single source id → single (P48). Named alternative kept below."
      rationale: "Two domains, each with its own authority (same-pattern rule). Theology is a positive science 'absolut verschieden' from philosophy (GA 9:48–49); faith as a specific Existenzmöglichkeit remains philosophy's 'Todfeind' so absolutely that philosophy does not even try to combat it (GA 9:66); 'Es gibt daher nicht so etwas wie eine christliche Philosophie, das ist ein »hölzernes Eisen« schlechthin' (GA 9:66). Named alternative: none strong — the 'Korrektiv' role of philosophy for theological concepts does not collapse the two into one authority (philosophy can be what it is without serving as that corrective)."
    E_scope: {value: UNKNOWN, how_known: "Nothing on favour for a group in the world's order read (P7, P19)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus and B_cause are both BELOW_THRESHOLD (P19; Kafka pattern)."}
  statements:
    - text: "Die Theologie ist eine positive Wissenschaft und als solche daher von der Philosophie absolut verschieden."
      cites: [{source: S5, locator: "GA 9:48–49"}]
      date: "1927"
      context: "Phänomenologie und Theologie (Tübingen 9 Mar 1927; Marburg repeat 14 Feb 1928); thesis on theology vs philosophy."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
    - text: "Dieses eigentümliche Verhältnis schließt nicht aus, sondern eben ein, daß der Glaube in seinem innersten Kern als eine spezifische Existenzmöglichkeit gegenüber der wesenhaft zur Philosophie gehörigen und faktisch höchst veränderlichen Existenzform der Todfeind bleibt. [...] Es gibt daher nicht so etwas wie eine christliche Philosophie, das ist ein »hölzernes Eisen« schlechthin."
      cites: [{source: S5, locator: "GA 9:66"}]
      date: "1927"
      context: "Phänomenologie und Theologie; faith vs free philosophical Existenz."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
    - text: "Das »Sein« — das ist nicht Gott und nicht ein Weltgrund. Das Sein ist wesenhaft weiter denn alles Seiende und ist gleichwohl dem Menschen naher als jedes Seiende, sei dies ein Fels, ein Tier, ein Kunstwerk, eine Maschine, sei es ein Engel oder Gott."
      cites: [{source: S5, locator: "Brief über den Humanismus (GA 9)"}]
      date: "1946"
      context: "Brief über den »Humanismus« to Jean Beaufret; Sein distinguished from God and from any Seiende."
      axes: [A_locus]
      kind: "published letter"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
    - text: "Doch mit diesem Hinweis möchte sich das Denken, das in die Wahrheit des Seins als das zu Denkende vorweist, keineswegs für den Theismus entschieden haben. Theistisch kann es so wenig sein wie atheistisch."
      cites: [{source: S5, locator: "Brief über den Humanismus (GA 9)"}]
      date: "1946"
      context: "Brief über den »Humanismus«; thinking the holy / Godhead does not decide theism."
      axes: [A_locus]
      kind: "published letter"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
  changes_over_life:
    - {value: "Catholic: in 1915 'in the service of the Catholic world-view'; broke with Catholicism between 1916 and 1919 (married the Lutheran Elfride Petri in 1917)", certainty: 0.7, cites: [{source: S3, locator: "§1 Life and Works"}, {source: S1, locator: "'Background and early career'"}], how_known: "Dates differ by source: Britannica puts the 'rejection of the religion of his youth' in a spiritual crisis in 1916 (after his study of Luther and Calvin), 'completed' by the 1917 marriage; IEP gives his announced break with the 'system of Catholicism' on 9 January 1919. Before the 1927 span either way."}
  coder_notes: "Span 1927–1964 (batch U audit fix HE4, P30 addendum b). Deepen D1 reached Wegmarken GA 9 (S5). PT and Humanism in span; Krebs 1919 letter still only secondary quotation (Casper 1980); Spiegel interview 1966 ('nur noch ein Gott kann uns retten') after the working span — not scored. Φύσις essay (1939) read for P16 and does not yield B. Not plotted."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "German (Swabian-Badenese provincial)", certainty: 0.5, cites: [{source: S2, locator: "§1 Life and Work"}], how_known: "Coder's reading of 'southwest Germany'."}
  religious_heritage_by_birth: {value: "Catholic", certainty: 1.0, cites: [{source: S2, locator: "§1 Life and Work"}, {source: S3, locator: "§1 Life and Works"}], how_known: "SEP and IEP."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1927–1964", certainty: 0.5, cites: [{source: S2, locator: "opening; §1 Life and Work"}, {source: S3, locator: "§1 Life and Works"}], how_known: "From Being and Time (1927) to the end of the later essays and lectures listed as one body of work (IEP's latest example, 1964; P12, P30 addendum b). Batch U audit fix (HE4)."}
  age_at_first_lasting_contribution: {value: 38, certainty: 0.7, cites: [{source: S1, locator: "facts box"}, {source: S3, locator: "§1 Life and Works"}], how_known: "1927 − 1889 = 38 (P30); 37 in February 1927."}
  first_evidence_of_lio_type_views: {value: "Phänomenologie und Theologie (faith vs philosophy; D 2)", year: 1927, certainty: 0.7, cites: [{source: S5, locator: "GA 9:48–49, 66"}], how_known: "Earliest dated own-voice statement now used for a scored LIO axis (D_authority)."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.7, cites: [{source: S5, locator: "GA 9:45–78 (1927); Brief über den Humanismus (1946)"}], how_known: "PT is the same year as Being and Time; Humanism falls inside 1927–1964."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "§2"}], how_known: "Not assessed."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S3, locator: "§1 Life and Works"}], how_known: "Not read."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S2, locator: "§2"}], how_known: "Coder's reading."}
  reading: "The question of the meaning of being, approached through temporal human existence."
  notes: ""

institutions:
  - {value: "University of Freiburg", role: "Privatdozent, then Husserl's assistant (1919)", years: "1915–1923", kind: university, certainty: 0.7, cites: [{source: S2, locator: "§1 Life and Work"}, {source: S3, locator: "§1 Life and Works"}], how_known: "SEP and IEP."}
  - {value: "University of Marburg", role: "associate professor, full professor 1927", years: "1923–1928", kind: university, certainty: 1.0, cites: [{source: S2, locator: "§1 Life and Work"}, {source: S3, locator: "§1 Life and Works"}], how_known: "SEP and IEP."}
  - {value: "University of Freiburg", role: "chair of philosophy (succeeding Husserl); rector April 1933 – April 1934; dismissed 1946, ban lifted 1949", years: "1928–1946", kind: university, certainty: 0.7, cites: [{source: S2, locator: "§1 Life and Work"}, {source: S3, locator: "§1 Life and Works"}], how_known: "SEP and IEP."}
collaborators:
  - {value: "Edmund Husserl", relation: "mentor or employer", note: "Heidegger was his assistant from 1919; Being and Time is dedicated to him", certainty: 1.0, cites: [{source: S2, locator: "§1 Life and Work"}, {source: S3, locator: "§1 Life and Works"}], how_known: "SEP and IEP."}
  - {value: "Heinrich Rickert", relation: teacher, note: "directed the doctorate (IEP) and the habilitation (SEP)", certainty: 0.7, cites: [{source: S2, locator: "§1 Life and Work"}, {source: S3, locator: "§1 Life and Works"}], how_known: "SEP and IEP."}
  - {value: "Hannah Arendt", relation: "student or assistant", note: "student at Marburg; long relationship", certainty: 0.7, cites: [{source: S2, locator: "§1 Life and Work"}], how_known: "SEP."}
  - {value: "Ernst Cassirer", relation: "rival or critic", note: "Davos disputation, 1929", certainty: 0.7, cites: [{source: S2, locator: "§1 Life and Work"}], how_known: "SEP."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 115"}], how_known: "Study roster."}
  controversies:
    - {value: "Nazi Party member from May 1933; rector of Freiburg 1933–34; dismissed from his chair in 1946", certainty: 1.0, cites: [{source: S2, locator: "§1 Life and Work; §3"}, {source: S3, locator: "§1 Life and Works"}], how_known: "SEP and IEP."}
  data_quality_flags:
    - "Worldview scores now rest on Wegmarken GA 9 OCR (S5); A and B remain BELOW after the primary read."
    - "Span end rests on IEP's examples of the later essays (to 1964); later writings may extend it."
  open_questions:
    - "Primary print of the 9 January 1919 letter to Engelbert Krebs (Casper 1980) for the Catholicism break in his own hand."
    - "Beiträge zur Philosophie (GA 65) 'letzter Gott' for any A-locus candidate (may still stay BELOW)."
    - "Die Technik und die Kehre / Question Concerning Technology for any P16 natural-order claim (unlikely)."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Arne D. Naess, Richard Wolin and Britannica Editors"
    citation: "Naess, Arne D., Richard Wolin and Britannica Editors. \"Martin Heidegger.\" Encyclopaedia Britannica (updated 22 September 2026). https://www.britannica.com/biography/Martin-Heidegger-German-philosopher. Read live 2026-10-19."
    url: "https://www.britannica.com/biography/Martin-Heidegger-German-philosopher"
    accessed: 2026-10-19
    reliability_note: "Signed article with several contributors: the main page reads 'Written by Arne D. Naess', the 'Later philosophy' subpage 'Written by Richard Wolin' with Britannica Editors (batch V audit note); the fetched text stopped after the 'Being and Time' section; facts box and body cited, question boxes not."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, worldview]
  - id: S2
    type: tertiary
    kind: encyclopedia
    author: "Mark Wrathall"
    citation: "Wrathall, Mark. \"Martin Heidegger.\" Stanford Encyclopedia of Philosophy (2025 revision). https://plato.stanford.edu/entries/heidegger/"
    url: "https://plato.stanford.edu/entries/heidegger/"
    accessed: 2026-10-19
    reliability_note: "Signed scholarly encyclopedia; opening and §1 used, §2.6 checked."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, heritage, timing, institutions, collaborators, review]
  - id: S3
    type: tertiary
    kind: encyclopedia
    author: "W. J. Korab-Karpowicz"
    citation: "Korab-Karpowicz, W. J. \"Martin Heidegger (1889–1976).\" Internet Encyclopedia of Philosophy. https://iep.utm.edu/heidegge/"
    url: "https://iep.utm.edu/heidegge/"
    accessed: 2026-10-19
    reliability_note: "Signed scholarly encyclopedia; §1 Life and Works and the bibliography used."
    source_quality: "reference entry"
    used_for: [basics, contribution, childhood, worldview, heritage, timing, institutions, collaborators, review]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S5
    type: primary
    kind: "published work by the subject"
    author: "Martin Heidegger"
    year: 1976
    citation: "Heidegger, Martin. Wegmarken. Gesamtausgabe Band 9. Ed. Friedrich-Wilhelm von Herrmann. Frankfurt am Main: Vittorio Klostermann, 1976 (unveränderter Text). PDF consulted via heidegger.ru mirror of GA 9, 2026-10-24. Key loci: Phänomenologie und Theologie (1927), GA 9:45–78 (absolut verschieden, Todfeind, gekreuzigte Gott as faith's positum); Brief über den »Humanismus« (1946), GA 9:313–364 (Sein ≠ Gott / Weltgrund; neither theistic nor atheistic); Vom Wesen und Begriff der Φύσις (1939), GA 9:239–301 (checked for P16, not used for a score)."
    url: "https://heidegger.ru/wp-content/uploads/2025/06/9-Wegmarken.pdf"
    accessed: 2026-10-24
    reliability_note: "Posthumous Gesamtausgabe of texts Heidegger published or authorized; Phänomenologie und Theologie first printed Archives de Philosophie 1969, then Klostermann 1970 pamphlet, collected in Wegmarken. OCR from the GA 9 PDF; German quotes checked against the OCR pages cited (running heads for PT; Humanism running heads in this PDF are sticky/wrong — essay title used as locator). Bard digital-commons scan was 403 this pass; IA Pathmarks print-disabled."
    source_quality: "primary / own words"
    used_for: [worldview, timing, lane_b, review]
  - id: S6
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia. \"Martin Heidegger.\" English Wikipedia. https://en.wikipedia.org/wiki/Martin_Heidegger. Read live 2026-10-24."
    url: "https://en.wikipedia.org/wiki/Martin_Heidegger"
    accessed: 2026-10-24
    reliability_note: "Crowdsourced; dual bio (P50) against Britannica/SEP/IEP. Birth/death and Catholic family align with S1–S3. Spiegel interview pointer ('Only a God Can Save Us') noted as after the working span — not scored."
    source_quality: "reference entry"
    used_for: [identity, basics, childhood, heritage, review]

---

# Martin Heidegger

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Martin Heidegger (1889–1976), German philosopher, author of Being and Time (1927) [S2, S3]. Deepen D1: Wegmarken GA 9 read [S5]. primary_system BELOW_THRESHOLD; A BELOW_THRESHOLD; B BELOW_THRESHOLD; D 2 (0.7); mid_basin BELOW_THRESHOLD. Not plotted.

## Life and work

Freiburg, Marburg, Freiburg; rector 1933–34 and Nazi Party member [S2, S3].

## Contribution and impact

Being and Time, 'a truly epoch-making work' [S3].

## Childhood and education

Son of a Catholic sexton, prepared for the priesthood; Jesuit novice in 1909 [S2, S3].

## Adult working worldview

Broke with the 'system of Catholicism' in 1919 [S3, secondary]. Phänomenologie und Theologie: theology 'absolut verschieden' from philosophy; faith the 'Todfeind' of free Existenz [S5, GA 9:48–49, 66]. Humanism: Sein is not God; thinking neither theistic nor atheistic [S5]. A and B stay BELOW; D 2 @ 0.7.

## Heritage (context only)

Catholic [S2, S3].

## Timing

1927–1964, from age 38 [S2, S3].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Not assessed.

## Open questions

- Krebs 1919 letter primary; Beiträge 'letzter Gott'; Technik essay for any P16 (unlikely).

## Research log

- 2026-10-19: Read Britannica (to the Being and Time section), SEP and IEP. Primary texts behind Cloudflare or access-restricted.
- 2026-10-24: Deepen D1. Read Wegmarken GA 9 (S5 PDF OCR): Phänomenologie und Theologie; Brief über den Humanismus; Φύσις essay checked for P16. Wikipedia EN dual bio (S6). A BELOW; B UNKNOWN→BELOW; D 2 @0.7. Chart-moving NO.
