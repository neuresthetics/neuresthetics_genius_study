---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch I)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to 19c. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch I, order P32: F 5, rank 61). Basics from Britannica (Hunt). Worldview from My Inventions (Electrical Experimenter, 1919), ch. VI, Wikisource transcription (web copy, 0.7 cap). Scientist/engineer under P30. primary_system BELOW_THRESHOLD (candidates DETERM, AGNOS); A BELOW_THRESHOLD (only 'faith in a supreme power of some kind' as a general human trait); B 4 at 0.5 (alt 3): 'We are automata entirely controlled by the forces of the medium' and no foundation for spiritual phenomena (near P40; RQ2 batch I); C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD. Not plotted. Draft, not reviewed."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Audit fixes (fallacy_catalog audit of bbb26f8, run 1). B rationale and C_ledger note reworded: the automata line is his mechanical explanation of the cosmic law, not a counter-sign. B stays 4 (0.5, alternative 3)."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #61, F5 rank 61). Needs: A BELOW_THRESHOLD; B single source; B faded. Primaries: Human Energy 1900 (S4) corroborates automata B; Liberty 1935 'A Machine to End War' as told to Viereck (S5) scores A 4@0.5 recorded_interview support single (alt BELOW) and extends B to universe-as-machine; EE 1919 IA DjVuTXT OCR (S6) verifies My Inventions ch. VI wording (no 'gift of mental power' / 'Divine Being' — rejected as non-primary). B 4@0.5 single → B 4@0.7 written_profession, support corroborated (P48); alt 3. D 4@0.5 recorded_interview, support single (new). primary_system stays BELOW (DETERM leading; ATHE/AGNOS named). P47 source_quality on S1–S6. mid_basin BELOW (A≥3 branch needs 0.7). Chart-moving NO (faded; A single → hollow). No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: tesla-nikola
  display_name: "Nikola Tesla"
  roster:
    canonical_name: "Nikola Tesla"
    rank: 61
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: invention
    field_bucket: "invention / engineering"
  full_name: {value: "Nikola Tesla", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  native_name: {value: UNKNOWN, how_known: "Cyrillic form not in the sources read."}
  aliases: []

basics:
  birth:
    date: {value: "1856-07", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica gives 'July 9/10, 1856', so only the month is recorded."}
    place: {value: "Smiljan, Austrian Empire", modern_name: "Smiljan, Croatia", polity_then: "Austrian Empire", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "1943-01-07", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "New York, New York, U.S.", modern_name: "New York City, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1883, certainty: 0.5, cites: [{source: S1, locator: "training paragraph"}], how_known: "First induction motor built at Strassburg in 1883, embodying the rotating-magnetic-field principle he had visualized earlier at Budapest (no year given) (P13); 0.5."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "His whole adult life falls in the bucket (P2)."}
  region_of_birth: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Croatia is Southern Europe in regions.csv (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "from 1884"}], how_known: "United States from 1884."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [English], certainty: 0.5, cites: [{source: S2, locator: "text"}, {source: S4, locator: "text"}], how_known: "Wrote in English in the US; earlier languages not given (0.5)."}
  occupations: {value: ["inventor", "electrical engineer"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

contribution:
  era_bucket: 19c
  fields: {value: ["electrical engineering"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Rotating magnetic field and induction motor (basis of most alternating-current machinery)", year: 1883, kind: discovery, lasting: "'the basis of most alternating-current machinery' (S1)", certainty: 0.5, cites: [{source: S1, locator: "opening; training paragraph"}], how_known: "Year of the first induction motor."}
    - {value: "Tesla coil", year: 1891, kind: invention, lasting: "'widely used today in radio and television sets' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; 1891 paragraph"}], how_known: "Britannica."}
    - {value: "Teleautomatic (remote-controlled) boat", year: 1898, kind: invention, lasting: "(S1)", certainty: 0.5, cites: [{source: S1, locator: "1898 paragraph"}], how_known: "Britannica; lasting status the coder's reading (0.5)."}
  evidence_of_impact:
    - {value: "Tesla Inc. named in his honour (2003)", kind: "named after them", certainty: 0.7, cites: [{source: S1, locator: "last paragraph"}], how_known: "Britannica."}
    - {value: "Edison Medal, 1917", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "turbines paragraph"}], how_known: "Britannica."}
  major_works:
    - {value: "The Problem of Increasing Human Energy", year: 1900, kind: other, certainty: 0.7, cites: [{source: S4, locator: "header (Century Illustrated Magazine, June 1900)"}], how_known: "Published Century essay."}
    - {value: "My Inventions", year: 1919, kind: other, certainty: 0.7, cites: [{source: S2, locator: "header"}, {source: S6, locator: "Electrical Experimenter 1919 installments"}], how_known: "Serialized autobiography."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Serbian Orthodox (father an Orthodox priest)", certainty: 0.7, cites: [{source: S1, locator: "family paragraph"}], how_known: "Britannica."}
  family_religious_practice: {value: "Intended 'from my very birth for the clerical profession'", certainty: 0.7, cites: [{source: S2, locator: "ch. I"}], how_known: "Autobiography; wording checked against EE OCR (S6)."}
  parents_and_household:
    - {value: "Father an Orthodox priest; mother 'unschooled but highly intelligent'", role: parents, certainty: 0.7, cites: [{source: S1, locator: "family paragraph"}], how_known: "Britannica."}
  household_circumstances: {value: TODO}
  schooling:
    - {value: "Technical University at Graz; University of Prague", stage: university, run_by: "state or municipal", certainty: 0.7, cites: [{source: S1, locator: "training paragraph"}], how_known: "Britannica; run_by the coder's reading."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: TODO}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1883–1898", certainty: 0.5, cites: [{source: S1, locator: "career paragraphs"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation:
    value: "Religious dogmas are no longer accepted in their orthodox meaning, but every individual clings to faith in a supreme power of some kind (any source of ideal may serve). 'There is no conflict between the ideal of religion and the ideal of science, but science is opposed to theological dogmas because science is founded on fact.' Commends religion for ideals and conduct while denying he is a believer 'in the orthodox sense'; praises the practicality of Christian religion (food, peace, work) in Human Energy."
    certainty: 0.7
    cites: [{source: S2, locator: "ch. VI"}, {source: S6, locator: "OCR of ch. VI installment"}, {source: S5, locator: "religion / science paragraphs"}, {source: S4, locator: "Christian religion / food-peace-work"}]
    how_known: "Own published essays (S2/S6, S4) and a recorded interview (S5); named alternative on A keeps related scores ≤0.7."
  primary_system:
    value: BELOW_THRESHOLD
    basis: written_profession
    certainty: 0.5
    cites: [{source: S2, locator: "ch. VI"}, {source: S4, locator: "automaton / self-acting-engine"}, {source: S5, locator: "not a believer; great machine; soul"}]
    rationale: "Strict mechanical automatism of life and of the universe, denial of foundation for psychical/spiritual phenomena, and 'not a believer in the orthodox sense', but no self-label and no positive naturalism phrase that would code ATHE; no explicit suspension for AGNOS. Candidates DETERM (leading), ATHE, AGNOS."
    how_known: "Own essays plus recorded interview; codes need a firmer self-placement than this pass gives."
    note: "Stub system files for DETERM / ATHE / AGNOS (flag)."
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: DETERM, reason: "Leading candidate, not coded at ≥0.5 as primary_system: 'We are automata entirely controlled by the forces of the medium' (S2/S6); 'I am an automaton… which merely responds to external stimuli' (S4); 'Man, like the universe, is a machine' (S5). Mechanist determinism is clear for B; DETERM as a system code still wants a labeled stance. Stub system file (flag).", cites: [{source: S2, locator: "ch. VI"}, {source: S4, locator: "automaton passage"}, {source: S5, locator: "Man, like the universe, is a machine"}]}
    - {code: ATHE, reason: "Candidate, not coded: 'not a believer in the orthodox sense'; universe 'never came into being'; soul/spirit = body functionings (S5). Not coded: no 'I do not believe in God' / positive naturalism self-label (v7.1; Curie/Turing pattern). Stub system file (flag).", cites: [{source: S5, locator: "believer / great machine / soul paragraphs"}]}
    - {code: AGNOS, reason: "Candidate, not coded: 'not a believer in the orthodox sense' leaves a non-orthodox possibility; he still commends religion and speaks of ideals. No explicit suspension. Stub system file (flag).", cites: [{source: S5, locator: "believer paragraph"}]}
  lio_axes:
    A_locus:
      value: 4
      basis: recorded_interview
      certainty: 0.5
      support: single
      cites: [{source: S5, locator: "believer / great machine / soul paragraphs"}]
      how_known: "(interview) One recorded interview ('as told to' Viereck), read in an unofficial web transcription of Liberty (not the magazine scan); 0.5 for the named BELOW alternative and for editorial 'as told to' shaping. Single source (P48). S2/S4 'supreme power' / Christian-practicality lines do not place or deny God and are not used for the value."
      rationale: "No Creator / no personal God-bond (P20/P38 logic): 'While I am not a believer in the orthodox sense' and 'To me, the universe is simply a great machine which never came into being and never will end'; soul/spirit 'is nothing more than the sum of the functionings of the body' and ceases with it (S5). Theology-practice or general 'supreme power' about people (S2) would not score A (Curie/Turing). Named alternative: BELOW_THRESHOLD — 'orthodox sense' hedges; he commends religion and ideals; interview is as-told-to, not a Liberty facsimile."
      alternatives:
        - {value: BELOW_THRESHOLD, note: "Orthodox-sense hedge; religion-commendation; as-told-to editorial shaping; no Liberty page images this pass.", cites: [{source: S5, locator: "believer / commend religion paragraphs"}]}
    B_cause:
      value: 4
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S2, locator: "ch. VI"}, {source: S6, locator: "OCR of automata / psychical passages"}, {source: S4, locator: "I am an automaton…; living being is only an automaton / self-acting-engine"}, {source: S5, locator: "universe… great machine; Man, like the universe, is a machine"}]
      how_known: "Two independent published essays of his own (S4 1900; S2/S6 1919), plus a consistent recorded interview (S5). Named alternative keeps certainty at 0.7. Independent source ids → corroborated (P48). Was B 4@0.5 single (S2 only) until this pass."
      rationale: "Scored on his account of nature (P6). Strict mechanism with no spiritual exception: 'We are automata entirely controlled by the forces of the medium' and 'absolutely no foundation' for psychical and spiritual phenomena (S2/S6); earlier, 'I am an automaton endowed with power of movement, which merely responds to external stimuli' and 'a living being is only an automaton, or… a \"self-acting-engine\"' (S4). S5 extends the claim beyond organisms: 'the universe is simply a great machine which never came into being and never will end' and 'Man, like the universe, is a machine.' Named alternative: 3 — if the necessity is read as limited to living beings / behavior (P40 caution) and the universe-machine line as metaphor."
      alternatives:
        - {value: 3, note: "P40-style: automata necessity stated for living beings / response to stimuli; universe-as-machine may be figurative.", cites: [{source: S2, locator: "ch. VI"}, {source: S4, locator: "automaton passage"}]}
    C_ledger: {value: UNKNOWN, how_known: "The 'cosmic' law that wrongdoers 'came to grief' (S2/S6) is explained mechanically by the automata line, with no agent and no moral reckoning; not scored. S5 soul-ceases language is about immortality of soul, not a ledger of reward/punishment."}
    D_authority:
      value: 4
      basis: recorded_interview
      certainty: 0.5
      support: single
      cites: [{source: S5, locator: "science opposed to theological dogmas"}]
      how_known: "(interview) One recorded interview (S5), unofficial web copy; single source (P48)."
      rationale: "Observation/fact outranks theological dogma: 'There is no conflict between the ideal of religion and the ideal of science, but science is opposed to theological dogmas because science is founded on fact' (S5). Named alternative: BELOW_THRESHOLD — as-told-to shaping; no second source."
      alternatives:
        - {value: BELOW_THRESHOLD, note: "Single as-told-to interview; no Liberty facsimile.", cites: [{source: S5, locator: "science / dogmas sentence"}]}
    E_scope: {value: UNKNOWN, how_known: "Not read (P7)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus ≥ 3 (value 4) but only at 0.5: the A ≥ 3 branch reads A only (P10) and needs 0.7. B is 4 at 0.7 and does not lift the branch."}
  statements:
    - text: "We are automata entirely controlled by the forces of the medium, being tossed about like corks on the surface of the water, but mistaking the resultant of the impulses from the outside for free will."
      cites: [{source: S2, locator: "ch. VI"}, {source: S6, locator: "OCR matching Wikisource ch. VI"}]
      date: "1919"
      axes: [B_cause]
      kind: "autobiography"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Wikisource My Inventions checked against Internet Archive Electrical Experimenter 1919 DjVuTXT (S6)."
    - text: "I have never had the faintest reason since to change my views on psychical and spiritual phenomena, for which there is absolutely no foundation."
      cites: [{source: S2, locator: "ch. VI"}, {source: S6, locator: "OCR matching Wikisource ch. VI"}]
      date: "1919"
      axes: [B_cause]
      kind: "autobiography"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "As above."
    - text: "Religious dogmas are no longer accepted in their orthodox meaning, but every individual clings to faith in a supreme power of some kind."
      cites: [{source: S2, locator: "ch. VI"}, {source: S6, locator: "OCR matching Wikisource ch. VI"}]
      date: "1919"
      axes: [A_locus]
      kind: "autobiography"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "General human trait — not used alone to score A (see A_locus how_known)."
    - text: "I have, by every thought and every act of mine, demonstrated, and do so daily, to my absolute satisfaction, that I am an automaton endowed with power of movement, which merely responds to external stimuli beating upon my sense organs, and thinks and acts and moves accordingly."
      cites: [{source: S4, locator: "telautomatics / automaton passage"}]
      date: "1900-06"
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Wikisource of Century Illustrated Magazine, June 1900; Century PDF blocked this pass (403)."
    - text: "While I am not a believer in the orthodox sense, I commend religion, first, because every individual should have some ideal — religious, artistic, scientific, or humanitarian — to give significance to his life."
      cites: [{source: S5, locator: "believer paragraph"}]
      date: "1935-02-09"
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Liberty, 9 Feb 1935, as told to George Sylvester Viereck; Tesla Universe transcription (PBS/tfcbooks misdate as 1937; contemporary Liberty issue list confirms 1935)."
    - text: "To me, the universe is simply a great machine which never came into being and never will end. The human being is no exception to the natural order. Man, like the universe, is a machine."
      cites: [{source: S5, locator: "great machine paragraph"}]
      date: "1935-02-09"
      axes: [A_locus, B_cause]
      kind: "recorded interview"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "As above."
    - text: "what we call \"soul\" or \"spirit,\" is nothing more than the sum of the functionings of the body. When this functioning ceases, the \"soul\" or the \"spirit\" ceases likewise."
      cites: [{source: S5, locator: "soul/spirit paragraph"}]
      date: "1935-02-09"
      axes: [A_locus, C_ledger]
      kind: "recorded interview"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Tagged C only as context; C stays UNKNOWN (no ledger of reward/punishment)."
    - text: "There is no conflict between the ideal of religion and the ideal of science, but science is opposed to theological dogmas because science is founded on fact."
      cites: [{source: S5, locator: "science / dogmas sentence"}]
      date: "1935-02-09"
      axes: [D_authority]
      kind: "recorded interview"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "As above."
  changes_over_life: []
  coder_notes: "Deepen D1: rejected circulating non-primaries (teslainfo.org quote-checker and EE OCR): 'gift of mental power comes from God' absent from Electrical Experimenter 1919; purported 1899 'Immortality' interview is a later play, not used. S5 Liberty date: 9 Feb 1935 (issue lists / Tesla Universe), not the 1937 misdate on some PBS/tfcbooks pages. Century Magazine PDF of Human Energy was 403 this pass. No fallacy_catalog (Jason)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Serbian", certainty: 0.7, cites: [{source: S1, locator: "family paragraph"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Serbian Orthodox", certainty: 0.7, cites: [{source: S1, locator: "family paragraph"}], how_known: "Britannica (father an Orthodox priest)."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1883–1898", certainty: 0.5, cites: [{source: S1, locator: "career paragraphs"}], how_known: "First to last listed contribution (P29, P30)."}
  age_at_first_lasting_contribution: {value: 27, certainty: 0.5, cites: [{source: S1, locator: "opening; training paragraph"}], how_known: "1883 − 1856 = 27 (P30)."}
  first_evidence_of_lio_type_views: {value: "1900", certainty: 0.7, cites: [{source: S4, locator: "automaton / self-acting-engine"}], how_known: "Human Energy states the automata thesis; My Inventions 1919 says the psychical views were held 'long ago' (undated)."}
  lio_views_relative_to_major_work: {value: "unclear", certainty: 0.5, cites: [{source: S4, locator: "automaton passage"}, {source: S2, locator: "ch. VI"}], how_known: "Published from 1900 on, after the 1883–1898 span; he presents the views as long-held (undated)."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "No dated God/nature statement inside 1883–1898 read this pass."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Not read.", certainty: 0.5, cites: [{source: S1, locator: "training paragraph"}], how_known: "Coder's reading."}
  form_acquired: {value: "through the profession", certainty: 0.5, cites: [{source: S1, locator: "training paragraph"}], how_known: "Engineering training."}
  circle_present: {value: "no", rationale: "Mechanism; universe as machine without a stated God identical with it.", certainty: 0.5, cites: [{source: S2, locator: "ch. VI"}, {source: S5, locator: "great machine"}], how_known: "Coder's reading."}
  reading: "Mechanist automatism; A scored only from the 1935 interview (single, 0.5)."
  notes: "Lane B belief model only; no H1 test this pass."

institutions:
  - {value: "Continental Edison Company, Paris", role: engineer, years: "1882–1884", kind: commercial, certainty: 0.5, cites: [{source: S1, locator: "training paragraph"}], how_known: "From 1882; end year inferred from his sailing in 1884 (0.5)."}
collaborators:
  - {value: "George Westinghouse", relation: "mentor or employer", note: "bought the AC patents", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  - {value: "Thomas Edison", relation: "mentor or employer", note: "first US employer; later separation", certainty: 0.7, cites: [{source: S1, locator: "training paragraph"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 61"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags: []
  open_questions:
    - "Liberty Magazine 9 Feb 1935 page images (facsimile) for S5 — would firm A/D verification and may lift as-told-to caution."
    - "Century Illustrated Magazine June 1900 scan for Human Energy (S4) — PDF 403 this pass."
    - "Any first-person 'I do not believe in God' / positive naturalism label for ATHE ≥0.5 — none found; misattributed God-gift and Immortality-interview quotes rejected."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Inez Whitaker Hunt"
    citation: "Hunt, Inez Whitaker. \"Nikola Tesla.\" Encyclopaedia Britannica, updated 15 October 2026. https://www.britannica.com/biography/Nikola-Tesla."
    url: "https://www.britannica.com/biography/Nikola-Tesla"
    accessed: 2026-10-15
    source_quality: "reference entry"
    reliability_note: "Signed body; Top Questions not cited."
    used_for: [identity, basics, contribution, childhood, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Nikola Tesla"
    year: 1919
    citation: "Tesla, Nikola. \"My Inventions.\" Electrical Experimenter, 1919. Wikisource transcription; automata / supreme-power / psychical passages verified against Internet Archive DjVuTXT (S6)."
    url: "https://en.wikisource.org/wiki/My_Inventions"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "Wikisource transcription of the Electrical Experimenter text; key worldview sentences checked against S6 OCR (archive scan). Used for B_cause and self-described relation."
    used_for: [basics, childhood, worldview, timing, lane_b]
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
    kind: "published work by the subject"
    author: "Nikola Tesla"
    year: 1900
    citation: "Tesla, Nikola. \"The Problem of Increasing Human Energy with special references to the harnessing of the Sun's energy.\" Century Illustrated Magazine, June 1900. Wikisource transcription. https://en.wikisource.org/wiki/The_Problem_of_Increasing_Human_Energy."
    url: "https://en.wikisource.org/wiki/The_Problem_of_Increasing_Human_Energy"
    accessed: 2026-10-24
    source_quality: "unofficial web copy"
    reliability_note: "Wikisource of the Century essay; Century PDF blocked (403) this pass — not checked against a facsimile. Used for B_cause corroboration (automaton / self-acting-engine)."
    used_for: [contribution, worldview, timing]
  - id: S5
    type: primary
    kind: other
    author: "Nikola Tesla (as told to George Sylvester Viereck)"
    year: 1935
    citation: "Tesla, Nikola. \"A Machine to End War.\" Liberty, 9 February 1935, as told to George Sylvester Viereck. Transcription at Tesla Universe. https://teslauniverse.com/nikola-tesla/articles/machine-end-war."
    url: "https://teslauniverse.com/nikola-tesla/articles/machine-end-war"
    accessed: 2026-10-24
    source_quality: "newspaper interview"
    reliability_note: "As-told-to interview in Liberty; date 9 Feb 1935 confirmed by contemporary issue lists (PBS/tfcbooks misdate Feb 1937). Read in Tesla Universe unofficial transcription, not Liberty page images. Used for A_locus, B_cause extension, D_authority."
    used_for: [worldview, lane_b]
  - id: S6
    type: primary
    kind: "archive record"
    author: "Nikola Tesla"
    year: 1919
    citation: "Tesla, Nikola. My Inventions and Other Works, Jan.–Oct. 1919 (Electrical Experimenter). Internet Archive item my-inventions-and-other-works-jan.-oct.-1919-nikola-tesla, DjVuTXT OCR."
    url: "https://archive.org/details/my-inventions-and-other-works-jan.-oct.-1919-nikola-tesla"
    accessed: 2026-10-24
    source_quality: "archive scan (OCR only)"
    reliability_note: "OCR only; page images not viewed. Confirms S2 automata / psychical / supreme-power wording; confirms absence of circulating 'gift of mental power' / 'Divine Being' interpolations in this OCR."
    used_for: [worldview]
---

# Nikola Tesla

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Nikola Tesla (1856–1943), Serbian American inventor [S1]. Deepen D1: primary_system BELOW_THRESHOLD; A 4 at 0.5 (single); B 4 at 0.7 corroborated; D 4 at 0.5 (single); mid_basin BELOW_THRESHOLD. Chart: faded hollow if plotted (A single, A cert 0.5).

## Life and work

Graz, Prague, Budapest, Paris; New York from 1884 [S1].

## Contribution and impact

Rotating magnetic field, AC system, Tesla coil [S1]. Human Energy (1900); My Inventions (1919) [S4, S2].

## Childhood and education

Son of an Orthodox priest; intended for the clergy [S1, S2].

## Adult working worldview

'We are automata entirely controlled by the forces of the medium' [S2, S6]; earlier automaton / self-acting-engine [S4]. 1935: not a believer in the orthodox sense; universe a great machine that never came into being [S5].

## Heritage (context only)

Serbian Orthodox [S1].

## Timing

First lasting contribution 1883, at 27 [S1]. First LIO-type evidence read: 1900 [S4].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No circle [S2, S5].

## Open questions

Liberty 1935 facsimile; Century 1900 facsimile; ATHE self-label if any.

## Research log

- 2026-10-15: Read Britannica (Hunt) and My Inventions ch. VI (Wikisource).
- 2026-10-24: Deepen D1 — Human Energy (Wikisource); EE 1919 IA OCR; Liberty 1935 Viereck via Tesla Universe; rejected fake God-gift / Immortality-interview quotes.
