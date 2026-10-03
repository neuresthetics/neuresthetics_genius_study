---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 5
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, third batch: physical science 1600–1950)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages and library scans"
  collected_on: 2026-10-02
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (third batch, RUNBOOK §1 order). Basics from Britannica (Bensaude-Vincent, first page) and the Science History Institute. Worldview from two of his own books in Presidential Library scans on the Internet Archive: Materialy dlya suzhdeniya o spiritizme (1876; his April 1876 lectures, pp. 376–377) and Zavetnye mysli (1903–1905; p. 136 note and the Afterword, p. 426), each passage checked on the page images. primary_system BELOW_THRESHOLD (DEISM and CHRIST considered). B 4 (0.7); A, C, D, E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Schema 1.1 → 1.2 (decision P8 adds basis recorded_interview and statement kind 'recorded interview'); no content change."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit, batch 3 (run 2, #81; run 1 noted the same): the p. 426 Afterword quotation stops mid-sentence (it continues ', получится неустойчивая и слащавая шаткость'), so the trailing cut is now marked [...]. No score changed. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Stage 3 lens-audit rulings applied to the batch's other records (OPEN_DECISIONS P14–P28, v8's picks, 2026-10-02). Schema 1.2 → 1.3. One reliable source caps a fact at 0.7; derived fields take the lowest certainty of their inputs; BELOW_THRESHOLD vs UNKNOWN per P19. Full before → after list: reports/stage3_rulings_changes.csv. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Span alignment (P29, P30 and its addendum): timing.major_work_period 1868–1871 → 1869–1871; worldview.working_years 1855–1907 → 1869–1871, equal to the span (P30 addendum f); 1 headline values rest on evidence outside the span and are left unchanged for a ruling (open questions). Listed in reports/p30_span_alignment.csv. Not reviewed."}

identity:
  id: mendeleev-dmitri
  display_name: "Dmitri Mendeleev"
  roster:
    canonical_name: "Dmitri Mendeleev"
    rank: 92
    F: 4
    models: [Claude, DeepSeek, Gemini, Grok]
    band: "core (3–4)"
    status: core
    field: chemistry
    field_bucket: chemistry
  full_name: {value: "Dmitri Ivanovich Mendeleev", certainty: 1.0, cites: [{source: S1, locator: "'Also known as'"}, {source: S2, locator: "opening"}], how_known: "Two sources."}
  native_name: {value: "Дмитрий Иванович Менделеев (pre-1918 spelling Дмитрій Ивановичъ Менделѣевъ)", certainty: 1.0, cites: [{source: S3, locator: "title page; p. 136 running head"}, {source: S4, locator: "p. 377 running head"}], how_known: "His own title pages and running heads (old orthography); modern spelling standard."}
  aliases:
    - {name: "Mendeleev-Dmitri", kind: "roster alias"}
    - {name: "Dmitry Ivanovich Mendeleyev", kind: transliteration}

basics:
  birth:
    date: {value: "1834-02-08", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening ('January 27 (February 8, New Style), 1834')"}], how_known: "Britannica gives both styles; Julian 27 January 1834."}
    place: {value: "Tobolsk", modern_name: "Tobolsk, Tyumen Oblast, Russia", polity_then: "Russian Empire", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "paragraph 3"}], how_known: "Two sources agree."}
  death:
    date: {value: "1907-02-02", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening ('January 20 (February 2), 1907')"}], how_known: "Britannica only (Julian 20 January)."}
    place: {value: "St. Petersburg", modern_name: "Saint Petersburg, Russia", polity_then: "Russian Empire", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1869, certainty: 1.0, cites: [{source: S1, locator: "'Formulation of the periodic law'"}, {source: S2, locator: "'Who Got There First?'"}], how_known: "Periodic law announced 6 March 1869 and first published that year."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "'Formulation of the periodic law'"}], how_known: "From first_lasting_contribution_year (P2)."}
  region_of_birth: {value: "Eastern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Russia is Eastern Europe in data/reference/regions.csv (P3), although Tobolsk is in Siberia (flag)."}
  region_of_work: {value: "Eastern Europe", certainty: 1.0, cites: [{source: S1, locator: "'Early life and education'"}, {source: S2, locator: "'Later Lives'"}], how_known: "St. Petersburg, apart from Heidelberg 1859–61."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "As the sources record it."}
  languages_of_work: {value: [Russian], certainty: 1.0, cites: [{source: S1, locator: "'Formulation of the periodic law' (Osnovy khimii)"}, {source: S3, locator: "title page"}], how_known: "His books are in Russian; translations exist."}
  occupations: {value: [chemist, "university professor", "government official (weights and measures)"], certainty: 1.0, cites: [{source: S1, locator: "'Early life and education'"}, {source: S2, locator: "'Later Lives'"}], how_known: "Two sources."}

contribution:
  fields: {value: [chemistry, metrology, "industrial and economic policy"], certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "'Later Lives'"}], how_known: "Chemistry from both; the rest from SHI."}
  lasting_original_contributions:
    - {value: "Periodic law and periodic table of the elements, with predicted elements (gallium, scandium, germanium) and corrected atomic weights", year: "1869–1871", kind: "law or principle", lasting: "framework of chemistry", certainty: 1.0, cites: [{source: S1, locator: "'Formulation of the periodic law'"}, {source: S2, locator: "'Who Got There First?'"}], how_known: "Two sources."}
  evidence_of_impact:
    - {value: "Periodic table became the framework for much of chemical theory; international recognition in his lifetime", kind: "standard textbook canon", certainty: 1.0, cites: [{source: S1, locator: "'Formulation of the periodic law'"}, {source: S2, locator: "opening"}], how_known: "Two sources."}
  major_works:
    - {value: "Osnovy khimii (The Principles of Chemistry)", year: 1869, kind: book, certainty: 0.7, cites: [{source: S1, locator: "'Formulation of the periodic law' (1868–71)"}, {source: S2, locator: "'Who Got There First?' (first edition 1871)"}], how_known: "Sources differ on the date (issued in parts 1868–71)."}
    - {value: "Zavetnye mysli (Cherished Thoughts)", year: 1905, kind: book, certainty: 1.0, cites: [{source: S3, locator: "title page; colophon note (printing finished 19 Oct 1905)"}], how_known: "Library scan; issued in four parts 1903–1905."}
  honours:
    - {value: "Demidov Prize (for his 1861 organic chemistry textbook)", certainty: 0.7, cites: [{source: S1, locator: "'Formulation of the periodic law'"}], how_known: "Britannica names the prize but not the year of award."}
  definition_fit: {value: "clearly meets", rationale: "Discovered the periodic law.", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Sources agree."}

childhood:
  family_religion: {value: TODO, note: "Russian Orthodox by general report; not stated in the sources read."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father, Ivan Pavlovich Mendeleev, teacher at the Tobolsk gymnasium (Russian literature); blind from 1834, died 1847", name: "Ivan Pavlovich Mendeleev", role: father, certainty: 1.0, cites: [{source: S1, locator: "'Early life and education'"}, {source: S2, locator: "paragraph 3"}], how_known: "Two sources."}
    - {value: "Mother, Mariya Dmitriyevna Kornileva, who ran the family glassworks; died soon after taking him to St. Petersburg", name: "Mariya Dmitriyevna Mendeleeva (née Kornileva)", role: mother, certainty: 1.0, cites: [{source: S1, locator: "'Early life and education'"}, {source: S2, locator: "paragraph 3"}], how_known: "Two sources."}
  household_circumstances: {value: "Last of 13 or 14 surviving children; father blind and then dead; the glassworks burned in December 1848; early contact with political exiles in Tobolsk", certainty: 1.0, cites: [{source: S1, locator: "'Early life and education'"}, {source: S2, locator: "paragraph 3"}], how_known: "Two sources (exiles from SHI)."}
  schooling:
    - {value: "Main Pedagogical Institute, St. Petersburg (graduated 1855)", stage: university, years: "1850–1855", certainty: 0.7, cites: [{source: S1, locator: "'Early life and education'"}, {source: S2, locator: "paragraph 3"}], how_known: "Two sources; start year is the coder's estimate (he arrived aged 15)."}
    - {value: "Master's degree 1856; study at Heidelberg 1859–1861 (in his own laboratory, nominally under Bunsen); doctorate, St. Petersburg, 1865", stage: university, years: "1856–1865", certainty: 0.7, cites: [{source: S1, locator: "'Early life and education'"}, {source: S2, locator: "paragraph 3"}], how_known: "Two sources; Heidelberg years from Britannica's 'two years' before 1861."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure:
    - {value: "Freedom to roam the family glassworks, which stimulated his interest in industrial chemistry", certainty: 0.7, cites: [{source: S2, locator: "paragraph 3"}], how_known: "SHI."}
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [Russian], certainty: 0.7, cites: [{source: S1, locator: "'Early life and education'"}], how_known: "Siberian Russian family."}
  notable_events:
    - {value: "Glassworks fire; his mother took him to St. Petersburg and died soon after", year: "1848–1850", certainty: 1.0, cites: [{source: S1, locator: "'Early life and education'"}, {source: S2, locator: "paragraph 3"}], how_known: "Two sources."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1869–1871", certainty: 0.7, cites: [{source: S1, locator: "'Formulation of the periodic law'"}], how_known: "Equal to timing.major_work_period (P30 addendum f; span check 2026-10-02). Was 1855–1907: From graduation to death."}
  nominal_affiliations: []
  self_described_science_religion_relation:
    value: "Complementary parts of one whole: the 'highest consciousness' of everything is expressed 'въ религіи, искусствѣ и наукѣ', and dropping any member of such a triad leaves 'анализъ безъ полнаго синтеза' (analysis without full synthesis)."
    certainty: 0.7
    cites: [{source: S3, locator: "p. 426"}]
    how_known: "His own published book, checked on the library scan. Below 1.0 because the statement is a single terse sentence and he says he withheld his fuller worldview chapter as incomplete and as revealing 'то, что лучше оставлять про себя'."
  primary_system:
    value: BELOW_THRESHOLD
    cites: [{source: S3, locator: "pp. 136, 426"}]
    how_known: "His published statements read do not speak of God. He calls himself a 'realist', not a materialist, holding that the unity of spirit, force and matter will long remain an 'incomprehensible mystery' (p. 136 note), and names religion with art and science as expressions of the highest consciousness (p. 426); neither places or describes a divine being."
    note: "Candidates: DEISM and CHRIST (drafts). Would need the withheld worldview chapter, his letters, or the family memoirs (son Ivan; niece N. Ya. Kapustina-Gubkina) read in an edition."
  secondary_system: {value: UNKNOWN, how_known: "No system evidence beyond the passages above."}
  candidate_codes_considered:
    - {code: DEISM, reason: "Considered: later scholarship (not read) describes a 'romantic deism'. Not coded: no statement of a creator in what was read. DEISM is a draft system file."}
    - {code: CHRIST, reason: "Considered: Orthodox upbringing by general report (not in a source read) and religion kept among the three highest expressions of consciousness (p. 426). Not coded: nothing specifically Christian is affirmed. CHRIST is a draft system file.", cites: [{source: S3, locator: "p. 426"}]}
    - {code: ATHE, reason: "Rejected: he rejects 'materialism' by name in favour of 'realism' (p. 136 note) and keeps religion in his triad (p. 426). ATHE is a stub system file.", cites: [{source: S3, locator: "pp. 136, 426"}]}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "Nothing read places or denies God. The 'unity of the world' as a lasting mystery (S3, p. 136 note) is about the world's basic concepts, not about a divine locus."}
    B_cause:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S4, locator: "pp. 376–377"}, {source: S1, locator: "'Formulation of the periodic law'"}]
      how_known: "His own published lectures (P6), checked on the library scan. Below 1.0 because the passages concern spiritualist phenomena and superstition, not miracle or providence directly."
      rationale: "Scored on his account of nature (P6). Against the spiritualists he holds that nervous physiology 'разрушитъ суевѣрія' and that people will one day speak of these matters as calmly as of eclipses and comets (p. 376); 'Наука борется съ суевѣріями, какъ свѣтъ съ потемками' (p. 377). Alleged mediumistic forces are referred to physiology or fraud, not admitted as exceptions to natural law. His working science is lawful in the strong sense: he trusted the periodic law enough to correct atomic weights and predict unknown elements (S1)."
    C_ledger: {value: UNKNOWN, how_known: "Nothing read on judgement, afterlife or reward and punishment. 'Долгъ' (duty) to family, homeland and humanity (S3, p. 426) is ethics, not a ledger."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "No statement on revelation or scripture in what was read. 'Суевѣріе есть увѣренность, на знаніи неоснованная' (S4, p. 377) is aimed at spiritualism, not revealed religion, and the triad of religion, art and science (S3, p. 426) does not say which decides.", note: "Not scored by the same-pattern rule: p. 426 names three expressions of one consciousness, not two domains under two authorities."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Scored on the world's order (P7). Nothing read addresses favour for a group in events; not scored from working science alone (same treatment as Fermi and Curie)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD, so the P4 test cannot be applied."}
  statements:
    - text: "Разработка вопросовъ нервной физіологіи не убьетъ нравственныхъ началъ, она только разрушитъ суевѣрія, существующія въ этомъ отношеніи, то есть предвзятыя мысли съ давнихъ поръ на вѣру принимаемыя."
      cites: [{source: S4, locator: "p. 376"}]
      date: "1876-04"
      context: "From his two public lectures on spiritualism (24 and 25 April 1876, Julian), printed in the book he edited. Coder's gloss: the study of nervous physiology will not kill moral principles; it will only destroy the superstitions in this area, that is, preconceived ideas long taken on faith. Old orthography as printed (checked on the page image)."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
    - text: "Суевѣріе есть увѣренность, на знаніи неоснованная. Наука борется съ суевѣріями, какъ свѣтъ съ потемками."
      cites: [{source: S4, locator: "p. 377"}]
      date: "1876-04"
      context: "Same lectures, on popular beliefs about psychic activity. Coder's gloss: superstition is a certainty not founded on knowledge; science fights superstitions as light fights darkness."
      axes: [B_cause, D_authority]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
    - text: "По моему же крайнему разумѣнію, это не матеріализмъ, а реализмъ; [...] искусственный дуализмъ, признающій только духъ и вещество и упускающій третье основное современное понятіе о силѣ или энергіи, сыгралъ уже свою роль въ мірѣ, въ которомъ непостижимою тайною надолго останется единство міра, тройственность исходныхъ понятій (духъ, сила и вещество) и сліяніе ихъ во всемъ томъ, что подлежитъ сужденію или объясненію въ людскихъ отношеніяхъ."
      cites: [{source: S3, locator: "p. 136, note 1"}]
      date: "1903"
      context: "Note to ch. 3 (foreign trade), answering critics who call the link between industry and history 'crude materialism'. Coder's gloss: not materialism but realism; dualism of spirit and matter alone, omitting force or energy, has had its day in a world where the unity of the world, the trinity of spirit, force and matter, will long remain an incomprehensible mystery. Date is the first part's imprint (1903–1904); the volume was completed in 1905."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
    - text: "Хочется-то мнѣ выразить завѣтнѣйшую мысль о нераздѣльности и сочетанности такихъ отдѣльныхъ граней познанія, каковы: вещество, сила и духъ; инстинктъ, разумъ и воля; свобода, трудъ и долгъ. Послѣдній должно признать по отношенію къ семьѣ, родинѣ и человѣчеству, а высшее сознаніе всего этого выраженнымъ въ религіи, искусствѣ и наукѣ. Выкиньте одно изъ каждой троицы — будетъ лишь анализъ безъ полнаго синтеза [...]"
      cites: [{source: S3, locator: "p. 426"}]
      date: "1905"
      context: "Afterword, written after the last chapter dated 27 September 1905, explaining why he did not print his short chapter on his personal worldview. The three triads are set as separate lines in the original. Coder's gloss: I want to express my most cherished thought on the inseparability of matter, force and spirit; instinct, reason and will; freedom, labour and duty, the last owed to family, homeland and humanity, and the highest consciousness of all this expressed in religion, art and science. Throw one out of each triad and there will be only analysis without full synthesis."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
  changes_over_life: []
  coder_notes: "DEISM and CHRIST are drafts; ATHE is a stub system file (flag). Quotations keep the pre-1918 orthography of the scans; English glosses in context are the coder's. Not used: claims about his religion from his son Ivan's and others' memoirs (reported by later writers, not read), and online quotations attributed to him on God (not traced to a scan). The commission's verdict that spiritualism 'is superstition' is a collective conclusion signed by twelve members (S4, first section, commission report; located in the OCR only, page not checked), so his own lecture sentences are used instead. changes_over_life is empty: no dated change in what was read."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Russian (Siberian provincial family)", certainty: 0.7, cites: [{source: S1, locator: "'Early life and education'"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: TODO, note: "Russian Orthodox by general report; not in a source read."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1869–1871", certainty: 0.7, cites: [{source: S1, locator: "'Formulation of the periodic law'"}], how_known: "The periodic law and table (1869–1871), the only listed lasting contribution (P29). Span check 2026-10-02 (P29, P30 and its addendum): was 1868–1871, which started with work on the Osnovy khimii textbook."}
  age_at_first_lasting_contribution: {value: 35, certainty: 0.7, cites: [{source: S1, locator: "opening; 'Formulation of the periodic law'"}], how_known: "Born February 1834; law announced March 1869."}
  first_evidence_of_lio_type_views: {value: "Lectures against spiritualism (lawful nature, superstition)", year: 1876, certainty: 1.0, cites: [{source: S4, locator: "pp. 376–377"}], how_known: "Earliest dated statement read."}
  lio_views_relative_to_major_work: {value: "unclear", rationale: "The earliest statement read (1876) postdates the periodic law (1869), but nothing earlier was read, so the order cannot be fixed from absence.", certainty: 0.5, cites: [{source: S4, locator: "pp. 376–377"}], how_known: "Dates of what was read only."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "The periodic law, once stated, was used deductively to correct atomic weights and predict elements (S1); not a definitional method.", certainty: 0.5, cites: [{source: S1, locator: "'Formulation of the periodic law'"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "'Early life and education'"}], how_known: "Nothing on method in what was read."}
  circle_present: {value: "unclear", rationale: "A 'unity of the world' of spirit, force and matter (S3, p. 136 note), but no identification of God with Nature.", certainty: 0.5, cites: [{source: S3, locator: "p. 136"}], how_known: "Coder's reading."}
  reading: "As belief, not finding: form partly present (predictive law), circle unclear. The record does not test H1."
  notes: ""

institutions:
  - {value: "St. Petersburg Technological Institute", role: professor, years: "1864–1866", kind: university, certainty: 0.7, cites: [{source: S1, locator: "'Early life and education'"}, {source: S2, locator: "'Who Got There First?'"}], how_known: "Two sources; end year is the coder's estimate."}
  - {value: "University of St. Petersburg", role: "professor of chemical technology, then of general chemistry", years: "1865–1890", kind: university, certainty: 1.0, cites: [{source: S1, locator: "'Early life and education'"}, {source: S2, locator: "'Later Lives'"}], how_known: "Two sources; left in 1890 after an official rebuke."}
  - {value: "Central Board (Chief Chamber) of Weights and Measures", role: director, years: "1893–1907", kind: "government or state body", certainty: 0.7, cites: [{source: S2, locator: "'Later Lives'"}], how_known: "SHI; start year from general knowledge, flagged."}
  - {value: "Commission of the Russian Physical Society for the examination of mediumistic phenomena", role: member, years: "1875–1876", kind: "academy or learned society", certainty: 0.7, cites: [{source: S4, locator: "preface, p. x"}], how_known: "His preface; his membership is implied by 'мои почтенные товарищи' in the lectures (OCR), not checked on the image."}
collaborators:
  - {value: "Robert Bunsen", relation: "mentor or employer", note: "Heidelberg; Mendeleev worked mostly in his own laboratory", certainty: 0.7, cites: [{source: S1, locator: "'Early life and education'"}, {source: S2, locator: "paragraph 2"}], how_known: "Two sources, which differ on how closely he worked with Bunsen."}
  - {value: "Julius Lothar Meyer", relation: "rival or critic", note: "independent periodic system; long priority dispute", certainty: 0.7, cites: [{source: S2, locator: "'Who Got There First?'"}], how_known: "SHI."}
  - {value: "Stanislao Cannizzaro", relation: "influenced by", note: "Karlsruhe 1860 paper on atomic weights", certainty: 1.0, cites: [{source: S1, locator: "'Early life and education'"}, {source: S2, locator: "'Karlsruhe'"}], how_known: "Two sources."}

review:
  roster_status_reason: {value: "Core in v8 (F 4: Claude, DeepSeek, Gemini, Grok).", certainty: 0.7, cites: [{source: S5, locator: "roster.csv, rank 92"}], how_known: "Study roster."}
  controversies:
    - {value: "Priority dispute with Lothar Meyer over the periodic system", certainty: 0.7, cites: [{source: S2, locator: "'Who Got There First?'"}], how_known: "SHI."}
  data_quality_flags:
    - "Quotations are from library scans in the pre-1918 orthography; the OCR is poor, so every quoted passage was transcribed from the page images."
    - "His religious heritage (Orthodox) and the family's clerical background are general report, not in the sources read; left TODO."
    - "Region of birth is coded Eastern Europe by the country rule although Tobolsk is in Siberia."
    - "Britannica read as its first page only."
  open_questions:
    - "Read the family memoirs (Ivan Mendeleev; Kapustina-Gubkina) and Gordin, A Well-Ordered Thing (2004), keeping reported speech apart from his own words."
    - "Look for the withheld worldview chapter mentioned in the Afterword of Zavetnye mysli (S3, p. 426) in the Sochineniya."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Bernadette Bensaude-Vincent"
    citation: "Bensaude-Vincent, Bernadette. \"Dmitri Mendeleev.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Dmitri-Mendeleev."
    url: "https://www.britannica.com/biography/Dmitri-Mendeleev"
    accessed: 2026-10-02
    reliability_note: "Signed article; first page only (to 'Formulation of the periodic law'). Sections cited by heading."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "Science History Institute"
    citation: "Science History Institute. \"Julius Lothar Meyer and Dmitri Ivanovich Mendeleev.\" Scientific Biographies. https://www.sciencehistory.org/education/scientific-biographies/julius-lothar-meyer-and-dmitri-ivanovich-mendeleev/."
    url: "https://www.sciencehistory.org/education/scientific-biographies/julius-lothar-meyer-and-dmitri-ivanovich-mendeleev/"
    accessed: 2026-10-02
    reliability_note: "Museum and library biography; paragraphs counted from the opening, sections by heading."
    used_for: [identity, basics, contribution, childhood, institutions, collaborators, review]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "Dmitri Ivanovich Mendeleev"
    year: 1905
    citation: "Mendeleev, D. I. Zavetnye mysli D. Mendeleeva [Заветные мысли Д. Менделеева]. St. Petersburg: Tipo-litografiya M. P. Frolovoi, 1903–[1905]. Presidential Library scan on the Internet Archive: https://archive.org/details/zavetnyemyslidmendeleeva4."
    url: "https://archive.org/details/zavetnyemyslidmendeleeva4"
    accessed: 2026-10-02
    reliability_note: "Library scan (Presidential Library collection). Issued in four parts; title page 1903–1904; printing finished 19 Oct 1905. Pages 136 and 426 checked on the page images (leaf = page + 3)."
    used_for: [identity, contribution, worldview, lane_b]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "Dmitri Ivanovich Mendeleev (editor and author of the preface and lectures)"
    year: 1876
    citation: "Mendeleev, D. I., ed. Materialy dlya suzhdeniya o spiritizme [Материалы для суждения о спиритизме]. St. Petersburg: Obshchestvennaya pol'za, 1876. Presidential Library scan on the Internet Archive: https://archive.org/details/materialydljasuzhdenijaospiritizme54."
    url: "https://archive.org/details/materialydljasuzhdenijaospiritizme54"
    accessed: 2026-10-02
    reliability_note: "Library scan. Contains the commission's papers and his own lectures of 15 Dec 1875 and 24–25 Apr 1876; only his own lectures and preface are used for his views. Pages 376–377 checked on the page images."
    used_for: [identity, worldview, timing, institutions]
  - id: S5
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
---

# Dmitri Mendeleev

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Dmitri Ivanovich Mendeleev (1834–1907), Russian chemist, discovered the periodic law in 1869 and predicted unknown elements [S1, opening]. Against the spiritualists in 1876 he wrote "Наука борется съ суевѣріями, какъ свѣтъ съ потемками" [S4, p. 377]; in 1905 he named religion, art and science together as the expression of the highest consciousness [S3, p. 426]. He calls his view "реализмъ", not materialism [S3, p. 136]. primary_system BELOW_THRESHOLD; B 4 (0.7); A, D, E below threshold, C UNKNOWN; mid_basin below threshold.

## Life and work

Born in Tobolsk, he studied at the Main Pedagogical Institute in St. Petersburg and in Heidelberg, taught at the University of St. Petersburg from 1865 to 1890, and then directed the Central Board of Weights and Measures [S1; S2, 'Later Lives'].

## Contribution and impact

The periodic law and table (1869–71), with predicted elements later found [S1, 'Formulation of the periodic law'].

## Childhood and education

His father, a gymnasium teacher, went blind the year he was born; his mother ran a glassworks and took him to St. Petersburg after it burned [S1; S2].

## Adult working worldview

Nervous physiology "разрушитъ суевѣрія" [S4, p. 376]. He is a realist: the unity of spirit, force and matter will long remain an "непостижимою тайною" [S3, p. 136]. Religion, art and science together express the highest consciousness [S3, p. 426]. Scores: B 4 (0.7); A, D, E below threshold, C UNKNOWN.

## Heritage (context only)

Russian; religious heritage not stated in the sources read. Context only.

## Timing

First lasting contribution 1869, at 35 [S1]. The worldview evidence read dates from 1876 and 1903–1905.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form partly present (predictive law); circle unclear.

## Open questions

- Span check (2026-10-02, P29/P30): B_cause (4 at 0.7) rest on evidence outside the new span 1869–1871. Values left unchanged pending a ruling; details in reports/p30_span_alignment.csv.
- Family memoirs and Gordin (2004); the withheld worldview chapter.

## Research log

- 2026-10-02: Read Britannica (Bensaude-Vincent, first page), the Science History Institute biography, and two Presidential Library scans on the Internet Archive (Materialy dlya suzhdeniya o spiritizme, 1876, pp. 376–377; Zavetnye mysli, 1903–1905, pp. 136, 426), transcribing from the page images because the OCR is poor. MacTutor has no Mendeleev page (404).
