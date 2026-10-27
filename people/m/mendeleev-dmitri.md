---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 8
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, third batch: physical science 1600–1950)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages and library scans"
  collected_on: 2026-10-02
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to 19c. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (third batch, RUNBOOK §1 order). Basics from Britannica (Bensaude-Vincent, first page) and the Science History Institute. Worldview from two of his own books in Presidential Library scans on the Internet Archive: Materialy dlya suzhdeniya o spiritizme (1876; his April 1876 lectures, pp. 376–377) and Zavetnye mysli (1903–1905; p. 136 note and the Afterword, p. 426), each passage checked on the page images. primary_system BELOW_THRESHOLD (DEISM and CHRIST considered). B 4 (0.7); A, C, D, E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Schema 1.1 → 1.2 (decision P8 adds basis recorded_interview and statement kind 'recorded interview'); no content change."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit, batch 3 (run 2, #81; run 1 noted the same): the p. 426 Afterword quotation stops mid-sentence (it continues ', получится неустойчивая и слащавая шаткость'), so the trailing cut is now marked [...]. No score changed. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Stage 3 lens-audit rulings applied to the batch's other records (OPEN_DECISIONS P14–P28, v8's picks, 2026-10-02). Schema 1.2 → 1.3. One reliable source caps a fact at 0.7; derived fields take the lowest certainty of their inputs; BELOW_THRESHOLD vs UNKNOWN per P19. Full before → after list: reports/stage3_rulings_changes.csv. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Span alignment (P29, P30 and its addendum): timing.major_work_period 1868–1871 → 1869–1871; worldview.working_years 1855–1907 → 1869–1871, equal to the span (P30 addendum f); 1 headline values rest on evidence outside the span and are left unchanged for a ruling (open questions). Listed in reports/p30_span_alignment.csv. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "P31 (continuity rule, v8's pick, 2026-10-02): the 1 value the span check flagged as resting on evidence outside the span are resolved, since changes_over_life documents no change of view between the span and that evidence; no value or certainty changed; the Open questions pointer line was removed. Listed in reports/p30_span_alignment.csv. Not reviewed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #91, F4 rank 92). Needs: A BELOW (blocks plot); B 4 @0.7; primary BELOW (DEISM/CHRIST). Dual bio: Britannica Bensaude-Vincent (S1, Wayback 2024) + Wikipedia EN (S6) (P50). P47 source_quality on S1–S8. A stays BELOW_THRESHOLD: checked withheld appendix «Мировоззрение» (written 1905 for Zavetnye mysli, refused print; posthumous Sochineniya XXIV 1954 / Wikisource Ch.11, S7) — affirms abstract unity traditionally «выражено в признании единого Бога» as necessary, rejects realizing that unity as «воображаемом и вечном старике» / matter / energy / church formalism; separates «начало всех начал» (faith/heart) from scientific generalization; does not place or deny a personal intervening God as locus (Pasteur pattern; unpublished MS private ceiling P18). Gordin 2004 pp. 229–230 via Wikipedia cite (S8): son Ivan — practically split from Church from earliest years; Gordin labels «romanticized deism» (not atheism/materialism). primary stays BELOW with DEISM lead strengthened (P27: no clear rejection of revelation as knowledge source in own words; Ivan/Gordin are reported speech + scholarly reconstruction). CHRIST further weakened (left Church per Ivan). B stays 4 @0.7 written_profession; added support corroborated (S4 lectures + S1 periodic-law practice). mid_basin stays BELOW (A blocks). Filled family_religion / heritage Orthodox @0.5; changes_over_life church split. Chart-moving NO. No fallacy_catalog. Draft, not reviewed."}

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
  era_bucket: 19c
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
  family_religion: {value: "Russian Orthodox", certainty: 0.5, cites: [{source: S6, locator: "raised as an Orthodox Christian"}, {source: S8, locator: "pp. 229–230 (mother exceptionally devout)"}], how_known: "Wikipedia; Gordin via Wikipedia cite. Heritage, not adult confession (0.5)."}
  family_religious_practice: {value: "Mother exceptionally devout; sister briefly in a fanatical religious sect (Gordin); adult Mendeleev practically split from the Church (Ivan via Gordin)", certainty: 0.5, cites: [{source: S8, locator: "pp. 229–230"}], how_known: "Gordin quotation via Wikipedia; son's reported speech."}
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
    cites: [{source: S3, locator: "pp. 136, 426"}, {source: S7, locator: "единого Бога / вечном старике passages"}, {source: S8, locator: "pp. 229–230 romanticized deism"}]
    how_known: "Published Zavetnye mysli: realist not materialist; religion–art–science triad (S3). Withheld «Мировоззрение» (S7): affirms abstract unity expressed as recognition of one God, rejects anthropomorphic / material realizations; not a coded system confession. Gordin (S8) labels romanticized deism from Ivan's report he left the Church — scholarly reconstruction + reported speech, not his own system label. P27: DEISM needs rejection of revelation; S7 keeps «начало всех начал» for faith/heart apart from science, without rejecting revelation as a knowledge source. Kept BELOW with DEISM lead."
    note: "Candidates: DEISM (lead) and CHRIST (weakened). Letters and Kapustina-Gubkina memoirs still unread beyond Gordin's Ivan extract."
  secondary_system: {value: UNKNOWN, how_known: "No second system beyond the DEISM lead."}
  candidate_codes_considered:
    - {code: DEISM, reason: "Lead: Gordin «romanticized deism» (S8); S7 rejects «вечном старике» / church formalism as realizations of unity. Not coded: P27 needs rejection of revelation — not clear in own words; Gordin/Ivan are not his system label. DEISM is a draft system file.", cites: [{source: S8, locator: "pp. 229–230"}, {source: S7, locator: "вечном старике / formalism"}]}
    - {code: CHRIST, reason: "Orthodox upbringing (S6/S8); religion in triad (S3 p. 426). Rejected for scoring: Ivan via Gordin — practically split from the Church from earliest years; nothing specifically Christian affirmed as adult confession.", cites: [{source: S3, locator: "p. 426"}, {source: S8, locator: "Ivan quotation"}]}
    - {code: ATHE, reason: "Rejected: rejects materialism for realism (S3 p. 136); keeps religion in triad; Gordin says opposition to Orthodoxy was not atheism (S8).", cites: [{source: S3, locator: "pp. 136, 426"}, {source: S8, locator: "not atheism"}]}
  lio_axes:
    A_locus:
      value: BELOW_THRESHOLD
      cites: [{source: S3, locator: "p. 136 note (unity mystery)"}, {source: S7, locator: "единого Бога / вечном старике / начало всех начал"}, {source: S8, locator: "pp. 229–230 (few theological commitments; left Church)"}]
      note: "Named alternatives if later own-voice place/deny is found: A 2 (abstract unity) or A 4 (reject anthropomorphic God / deism-adjacent) at ≤0.5 with BELOW as alt. Unpublished MS private ceiling (P18) would cap A at 0.5 from S7 alone even if clearer."
      how_known: "Checked: S3 p. 136 unity of spirit/force/matter as mystery (not locus); S7 «Мировоззрение» (withheld 1905; Sochineniya XXIV / Wikisource) — «признании единого Бога» as correct expression of unity, but rejects realizing that unity as «воображаемом и вечном старике», matter, energy, or religious formalism; «начало всех начал» left to faith/heart, not science. Does not place or deny a personal intervening God (Pasteur pattern). S8: Ivan — left Church; Gordin — romanticized deism / few theological commitments. No published «I do not believe in God» / place-deny of intervening God."
    B_cause:
      value: 4
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S4, locator: "pp. 376–377"}, {source: S1, locator: "'Formulation of the periodic law'"}]
      how_known: "His own published lectures (P6), checked on the library scan; corroborated by Britannica's account of predictive periodic law (S1). Below 1.0 because the lecture passages concern spiritualist phenomena and superstition, not miracle or providence directly. Deepen D1: support made explicit (P48); no lift needed."
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
    - text: "Современный научно-философский скептицизм берет свое начало из вековечно существовавшего и долженствующего вечно существовать стремления людей признать единство всего внутреннего и внешнего мира, что и выражено в признании единого Бога и в стремлении это исходное понятие об «едином» по возможности реализовать или узнать ближе. Первое признавать правильным, по мне, совершенно необходимо, а второе во всех отношениях неправильно, недостижимо и к скептицизму-то и приводит. Одни видели это единство в солнце, другие — в самодержавии, воображаемом и вечном старике, третьи — в единоличном людском разуме [...]"
      cites: [{source: S7, locator: "единого Бога / вечном старике paragraph"}]
      date: "1905-09"
      context: "«Мировоззрение», written as intended appendix to Zavetnye mysli; he refused to publish it (Afterword S3; Wikisource note). Dated 27 September 1905 at close. Coder's gloss: recognizing unity of inner and outer world, expressed in recognition of one God, is necessary/correct; trying to realize that «единое» more closely (as sun, autocracy/imagined eternal old man, matter, energy, etc.) is wrong and leads to skepticism."
      axes: [A_locus]
      kind: "unpublished manuscript"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Posthumous print in Sochineniya XXIV (1954) / Wikisource; not in 1905 Zavetnye mysli IA scan (verified OCR). Private ceiling (P18). Documents A lead; A stays BELOW_THRESHOLD."
    - text: "Дело идет о данном времени и лишь о том, до чего может ныне достигать разумное обобщение, на чем должно или может соглашаться, хоть временно успокоиться лично, вовсе помимо «начала всех начал», для которого почва создается не изучением, а тем, что называется верою и определяется инстинктом, волею, чувством и сердцем."
      cites: [{source: S7, locator: "начало всех начал paragraph"}]
      date: "1905-09"
      context: "Same withheld «Мировоззрение». Coder's gloss: rational generalization for the present is apart from the «beginning of all beginnings», whose soil is faith (instinct, will, feeling, heart), not study."
      axes: [A_locus, D_authority]
      kind: "unpublished manuscript"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Keeps a faith domain without placing personal intervening God; not used to score DEISM under P27."
  changes_over_life:
    - {value: "Practically split from the Orthodox Church from earliest years; tolerated simple rites only as national tradition (Ivan via Gordin); wrote then withheld «Мировоззрение» (1905)", year: "c. 1840s–1905", certainty: 0.5, cites: [{source: S8, locator: "Ivan quotation pp. 229–230"}, {source: S7, locator: "withheld chapter note"}], how_known: "Son's reported speech via Gordin; Afterword + Wikisource note on withheld MS."}
  coder_notes: "Coder's call D1. Did not score A 2/4 or DEISM from S7+S8 (overclaim; Pasteur/P27). Ivan quotation used only as reported speech under Gordin. «Мировоззрение» is unpublished MS (private ceiling). DEISM/CHRIST drafts; ATHE stub. Pre-1918 orthography in S3/S4 quotes; S7 modern orthography from Wikisource. Commission spiritualism verdict not used (collective). No fallacy_catalog (Jason). Figures not refreshed."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Russian (Siberian provincial family)", certainty: 0.7, cites: [{source: S1, locator: "'Early life and education'"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Russian Orthodox", certainty: 0.5, cites: [{source: S6, locator: "raised as an Orthodox Christian"}, {source: S8, locator: "heavily religious upbringing"}], how_known: "Wikipedia; Gordin via Wikipedia. Context only."}
  baptism_or_initiation: {value: "Baptized (sibling baptism count in family reports)", certainty: 0.5, cites: [{source: S6, locator: "only 14 stayed alive to be baptized"}], how_known: "Wikipedia citing brother Pavel; implies Orthodox baptism practice. Context only."}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1869–1871", certainty: 0.7, cites: [{source: S1, locator: "'Formulation of the periodic law'"}], how_known: "The periodic law and table (1869–1871), the only listed lasting contribution (P29). Span check 2026-10-02 (P29, P30 and its addendum): was 1868–1871, which started with work on the Osnovy khimii textbook."}
  age_at_first_lasting_contribution: {value: 35, certainty: 0.7, cites: [{source: S1, locator: "opening; 'Formulation of the periodic law'"}], how_known: "Born February 1834; law announced March 1869."}
  first_evidence_of_lio_type_views: {value: "Lectures against spiritualism (lawful nature, superstition)", year: 1876, certainty: 1.0, cites: [{source: S4, locator: "pp. 376–377"}], how_known: "Earliest dated statement read."}
  lio_views_relative_to_major_work: {value: "unclear", rationale: "The earliest statement read (1876) postdates the periodic law (1869), but nothing earlier was read, so the order cannot be fixed from absence.", certainty: 0.5, cites: [{source: S4, locator: "pp. 376–377"}], how_known: "Dates of what was read only."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "primary_system BELOW; A BELOW; earliest LIO statements read are 1876 (after 1869–71). P31: no documented change of view between span and later evidence used for B."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "The periodic law, once stated, was used deductively to correct atomic weights and predict elements (S1); not a definitional method.", certainty: 0.5, cites: [{source: S1, locator: "'Formulation of the periodic law'"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "'Early life and education'"}], how_known: "Nothing on method in what was read."}
  circle_present: {value: "unclear", rationale: "Unity of spirit, force and matter (S3/S7), but S7 rejects realizing «единое» as Nature/matter/energy; no God=Nature identity.", certainty: 0.5, cites: [{source: S3, locator: "p. 136"}, {source: S7, locator: "единое realizations"}], how_known: "Coder's reading."}
  reading: "As belief, not finding: form partly present (predictive law); A BELOW; B 4 @0.7 corroborated; unplotted (A blocks)."
  notes: "Lane B only. Chart-moving NO."

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
    - "S3/S4 quotations from library scans in pre-1918 orthography; transcribed from page images (OCR poor)."
    - "«Мировоззрение» (S7) is a withheld 1905 MS published posthumously (Sochineniya XXIV 1954); private ceiling P18."
    - "Gordin 2004 IA borrow-restricted; Ivan/deism quotations taken from Wikipedia's cited extract (S8)."
    - "Region of birth coded Eastern Europe by country rule although Tobolsk is in Siberia."
    - "Britannica live fetch Cloudflare-blocked 2026-10-24; Wayback 2024 body used for S1 refresh."
  open_questions:
    - "Optional: Gordin 2004 print pp. 229–230 beyond Wikipedia extract; Kapustina-Gubkina / Ivan memoirs in full."
    - "Optional: Sochineniya XXIV facsimile page images of «Мировоззрение» (currently Wikisource scholarly web)."
    - "Settled this pass: withheld worldview chapter located (S7); does not clear A ≥ 0.7."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Bernadette Bensaude-Vincent"
    citation: "Bensaude-Vincent, Bernadette. \"Dmitri Mendeleev.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Dmitri-Mendeleev. Deepen refresh via Wayback 2024 snapshot (live Cloudflare-blocked 2026-10-24)."
    url: "https://www.britannica.com/biography/Dmitri-Mendeleev"
    accessed: 2026-10-24
    reliability_note: "Signed article; create-pass used first page to 'Formulation of the periodic law'. Sections cited by heading."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "Science History Institute"
    citation: "Science History Institute. \"Julius Lothar Meyer and Dmitri Ivanovich Mendeleev.\" Scientific Biographies. https://www.sciencehistory.org/education/scientific-biographies/julius-lothar-meyer-and-dmitri-ivanovich-mendeleev/."
    url: "https://www.sciencehistory.org/education/scientific-biographies/julius-lothar-meyer-and-dmitri-ivanovich-mendeleev/"
    accessed: 2026-10-24
    reliability_note: "Museum and library biography; paragraphs counted from the opening, sections by heading. Silent on religion (checked deepen D1)."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, institutions, collaborators, review]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "Dmitri Ivanovich Mendeleev"
    year: 1905
    citation: "Mendeleev, D. I. Zavetnye mysli D. Mendeleeva [Заветные мысли Д. Менделеева]. St. Petersburg: Tipo-litografiya M. P. Frolovoi, 1903–[1905]. Presidential Library scan on the Internet Archive: https://archive.org/details/zavetnyemyslidmendeleeva4."
    url: "https://archive.org/details/zavetnyemyslidmendeleeva4"
    accessed: 2026-10-24
    reliability_note: "Library scan (Presidential Library collection). Issued in four parts; title page 1903–1904; printing finished 19 Oct 1905. Pages 136 and 426 checked on the page images (leaf = page + 3). Deepen D1: OCR of full volume confirms Afterword withholds worldview chapter; «Мировоззрение» not in this 1905 print."
    source_quality: "primary / own words"
    used_for: [identity, contribution, worldview, lane_b]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "Dmitri Ivanovich Mendeleev (editor and author of the preface and lectures)"
    year: 1876
    citation: "Mendeleev, D. I., ed. Materialy dlya suzhdeniya o spiritizme [Материалы для суждения о спиритизме]. St. Petersburg: Obshchestvennaya pol'za, 1876. Presidential Library scan on the Internet Archive: https://archive.org/details/materialydljasuzhdenijaospiritizme54."
    url: "https://archive.org/details/materialydljasuzhdenijaospiritizme54"
    accessed: 2026-10-24
    reliability_note: "Library scan. Contains the commission's papers and his own lectures of 15 Dec 1875 and 24–25 Apr 1876; only his own lectures and preface are used for his views. Pages 376–377 checked on the page images."
    source_quality: "primary / own words"
    used_for: [identity, worldview, timing, institutions]
  - id: S5
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    reliability_note: "Study's own roster; used only for rank, F and status."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S6
    type: secondary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia. \"Dmitri Mendeleev.\" https://en.wikipedia.org/wiki/Dmitri_Mendeleev. Read 2026-10-24."
    url: "https://en.wikipedia.org/wiki/Dmitri_Mendeleev"
    accessed: 2026-10-24
    reliability_note: "Dual-bio second source (P50) for dates/places; Early life on Orthodox upbringing and Gordin/Ivan deism note."
    source_quality: "reference entry"
    used_for: [identity, basics, childhood, worldview, heritage, review]
  - id: S7
    type: primary
    kind: "published work by the subject"
    author: "Dmitri Ivanovich Mendeleev"
    year: 1905
    citation: "Mendeleev, D. I. Mirovozzrenie (written 1905 as intended appendix to Zavetnye mysli; withheld from the 1905 print). Posthumous: Sochineniya, vol. XXIV (Moscow/Leningrad: AN SSSR, 1954), pp. 455-461; Wikisource Zavetnye mysli / Glava 11 (Prilozhenie)."
    url: "https://ru.wikisource.org/wiki/%D0%97%D0%B0%D0%B2%D0%B5%D1%82%D0%BD%D1%8B%D0%B5_%D0%BC%D1%8B%D1%81%D0%BB%D0%B8_(%D0%94._%D0%98._%D0%9C%D0%B5%D0%BD%D0%B4%D0%B5%D0%BB%D0%B5%D0%B5%D0%B2)/%D0%93%D0%BB%D0%B0%D0%B2%D0%B0_11"
    accessed: 2026-10-24
    reliability_note: "Own words, unpublished in his lifetime (Afterword S3; Wikisource note 1). Scholarly web of posthumous edition; private ceiling P18. Not a second print-check of the 1905 book."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview, review]
  - id: S8
    type: secondary
    kind: "scholarly book"
    author: "Michael D. Gordin"
    citation: "Gordin, Michael D. A Well-Ordered Thing: Dmitrii Mendeleev and the Shadow of the Periodic Table. Basic Books, 2004, pp. 229–230. Quotation as cited on Wikipedia (S6) including Ivan Mendeleev on leaving the Church and Gordin's «romanticized deism» label. IA item wellorderedthing00gord borrow-restricted 2026-10-24."
    url: "https://archive.org/details/wellorderedthing00gord/page/229"
    accessed: 2026-10-24
    reliability_note: "Scholarly monograph. Pages not opened this pass; extract taken from Wikipedia's cited quotation of pp. 229–230 (Ivan reported speech + Gordin reconstruction)."
    source_quality: "scholarly reconstruction"
    used_for: [worldview, childhood, heritage, review]
---

# Dmitri Mendeleev

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Dmitri Ivanovich Mendeleev (1834–1907), Russian chemist, discovered the periodic law in 1869 and predicted unknown elements [S1; S6]. Deepen D1: primary_system BELOW_THRESHOLD (DEISM lead); A BELOW_THRESHOLD; B 4 @0.7 corroborated; mid_basin BELOW_THRESHOLD. Not plotted (A blocks). Chart-moving NO.

## Life and work

Born in Tobolsk, he studied at the Main Pedagogical Institute in St. Petersburg and in Heidelberg, taught at the University of St. Petersburg from 1865 to 1890, and then directed the Central Board of Weights and Measures [S1; S2, 'Later Lives'].

## Contribution and impact

The periodic law and table (1869–71), with predicted elements later found [S1, 'Formulation of the periodic law'].

## Childhood and education

His father, a gymnasium teacher, went blind the year he was born; his mother ran a glassworks and took him to St. Petersburg after it burned [S1; S2].

## Adult working worldview

Nervous physiology "разрушитъ суевѣрія" [S4, p. 376]. Realist triad [S3, p. 136]; religion–art–science [S3, p. 426]. Withheld «Мировоззрение»: abstract «единый Бог» / reject «вечный старик» [S7]. Ivan/Gordin: left Church; romanticized deism label [S8]. Scores: A BELOW; B 4 @0.7 corroborated.

## Heritage (context only)

Russian; Orthodox heritage [S6; S8]. Context only.

## Timing

First lasting contribution 1869, at 35 [S1]. The worldview evidence read dates from 1876 and 1903–1905.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form partly present; A BELOW; B 4 @0.7; unplotted.

## Open questions

- Gordin print; Kapustina-Gubkina; Sochineniya XXIV facsimile of «Мировоззрение».

## Research log

- 2026-10-02: Britannica (first page), SHI, Materialy (pp. 376–377), Zavetnye mysli (pp. 136, 426).
- 2026-10-24: Deepen D1. Wikipedia dual bio; Wikisource/Sochineniya «Мировоззрение» (withheld MS); Gordin via Wikipedia cite; IA Zavetnye OCR confirms chapter absent from 1905 print; Britannica live blocked (Wayback used); SHI silent on religion. Wrote drafts/deepen_mendeleev-dmitri.md (untracked). No figures refresh. No fallacy_catalog.
