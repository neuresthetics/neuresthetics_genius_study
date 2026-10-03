---
record:
  record_type: person
  schema_version: "1.2"
  record_version: 4
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, second batch: physical science 1600–1950)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (second batch, RUNBOOK §1 order). Basics from Britannica (first page), the Nobel biography and the AIP exhibit (Pasachoff). Worldview from her own Pierre Curie with Autobiographical Notes (1923, Kellogg translation, Project Gutenberg) and two 1887 letters quoted in Eve Curie's Madame Curie (1937, Sheean translation, archive.org OCR). Raised Catholic; faith lost after her mother's death; civil wedding. primary_system AGNOS at 0.5 (stub system; ATHE named). B 4 (0.7), D 4 (0.5); A, C, E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit, batch 2 (two blind runs at e648145). Finding #108: primary_system AGNOS (0.5) → BELOW_THRESHOLD, candidates AGNOS and ATHE; the AGNOS choice rested on the absence of a denial of God, and AIP p. 57 ('liberal freethinkers like Marie and her friends') fits either code. Finding #112: D_authority 4 (0.5) → BELOW_THRESHOLD (scored from absence; same as Fermi). Finding #126: the p. 77 'nothingness' line is about obscurity, not death; C_ledger tag and the reliance in primary_system and C removed. Finding #120: 1898 locator AIP p. 36, not p. 22. Eve Curie page numbers confirmed against the scans; the 'one page either way' caveat is removed and the archive.org image-index offset is noted. mid_basin unchanged (BELOW_THRESHOLD). Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "CODING_GUIDE §7 rule on unofficial web copies: S3 (Project Gutenberg text of Pierre Curie, 1923) is an unofficial copy. Checked it against S7, the Phillips Academy library scan of the 1923 Macmillan edition (Internet Archive). Every quotation and every S3 fact used by the eleven certainty-1.0 fields that cite S3 was found word for word: native_name, birth date, family_religion, father, household_circumstances, early_science_exposure, childhood_mentors, notable_events, nominal_affiliations, ethnic_or_communal_heritage, religious_heritage_by_birth. Added S7 cites with printed page numbers to those fields and to the two S3 quotations; the two quotations' verified_against goes from primary transcription to primary facsimile. All stay at 1.0. No value, certainty or mid_basin change."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Schema 1.1 → 1.2 (decision P8 adds basis recorded_interview and statement kind 'recorded interview'); no content change."}

identity:
  id: curie-marie
  display_name: "Marie Curie"
  roster:
    canonical_name: "Marie Curie"
    rank: 56
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: physics
    field_bucket: physics
  full_name: {value: "Marie Skłodowska Curie (née Maria Skłodowska)", certainty: 1.0, cites: [{source: S1, locator: "opening paragraph and 'Early life'"}, {source: S2, locator: "paragraph 1"}], how_known: "Two sources agree."}
  native_name: {value: "Maria Skłodowska (Polish)", certainty: 1.0, cites: [{source: S1, locator: "'Early life'"}, {source: S3, locator: "Autobiographical Notes, ch. I ('my name is Marie Sklodowska')"}, {source: S7, locator: "p. 155; p. 73 n. 1"}], how_known: "Two sources; she used 'Marie' from 1891 in Paris (S1)."}
  aliases:
    - {name: "Curie-Marie", kind: "roster alias"}
    - {name: "Marie-Curie", kind: "roster alias"}
    - {name: "Manya", kind: other}

basics:
  birth:
    date: {value: "1867-11-07", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S2, locator: "paragraph 1"}, {source: S3, locator: "Autobiographical Notes, ch. I"}, {source: S7, locator: "p. 157"}], how_known: "Three sources agree."}
    place: {value: "Warsaw", modern_name: "Warsaw, Poland", polity_then: "Congress Kingdom of Poland, Russian Empire", certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}, {source: S2, locator: "paragraph 1"}], how_known: "Two sources agree."}
  death:
    date: {value: "1934-07-04", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S2, locator: "final paragraph"}], how_known: "Two sources agree."}
    place: {value: "near Sallanches, Savoy", modern_name: "Sallanches area, Haute-Savoie, France", polity_then: "France", certainty: 0.7, cites: [{source: S1, locator: "opening paragraph"}, {source: S2, locator: "final paragraph ('in Savoy')"}], how_known: "Britannica says near Sallanches; the Nobel biography says only Savoy. The sanatorium was not named in the sources read."}
  first_lasting_contribution_year: {value: 1898, certainty: 1.0, cites: [{source: S1, locator: "'Move to Paris, Pierre Curie, and first Nobel Prize'"}, {source: S5, locator: "p. 36"}], how_known: "Polonium (summer 1898) and radium (late 1898)."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "'Move to Paris'"}], how_known: "From first_lasting_contribution_year (P2)."}
  region_of_birth: {value: "Eastern Europe", certainty: 1.0, cites: [{source: S1, locator: "opening paragraph ('Warsaw, Congress Kingdom of Poland')"}], how_known: "Poland is Eastern Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Western Europe", certainty: 1.0, cites: [{source: S1, locator: "'Move to Paris'"}, {source: S2, locator: "paragraphs 1–2"}], how_known: "All the lasting work was done in Paris (France, Western Europe)."}
  sex_as_recorded: {value: "female", certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}], how_known: "As the sources record it."}
  languages_of_work: {value: [French, Polish], certainty: 0.7, cites: [{source: S2, locator: "paragraph 5 (French titles of her books)"}, {source: S1, locator: "'Early life'"}], how_known: "She published in French; Polish was her first language. Her own Autobiographical Notes appeared in English (S3), possibly through a translator."}
  occupations: {value: [physicist, chemist, "university professor", "laboratory director"], certainty: 1.0, cites: [{source: S2, locator: "paragraph 1"}, {source: S1, locator: "opening paragraph"}], how_known: "Two sources."}

contribution:
  fields: {value: [radioactivity, physics, chemistry], certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}, {source: S2, locator: "paragraphs 2, 6"}], how_known: "Nobel Prizes in physics (1903) and chemistry (1911)."}
  lasting_original_contributions:
    - {value: "Discovery of the elements polonium and radium (with Pierre Curie)", year: "1898", kind: discovery, lasting: "two named elements; founding of radiochemistry", certainty: 1.0, cites: [{source: S1, locator: "'Move to Paris'"}, {source: S2, locator: "paragraph 2"}], how_known: "Two sources."}
    - {value: "Showed that radioactivity is an atomic property (thorium also radioactive; activity of pitchblende above that of its uranium) and named it 'radioactivity'", year: "1898", kind: discovery, lasting: "the concept and the term", certainty: 0.7, cites: [{source: S1, locator: "'Move to Paris'"}], how_known: "Britannica; the atomic-property framing is in S5 but was not quote-checked here."}
    - {value: "Isolation of radium and methods for separating it from residues", year: "1902–1910", kind: method, lasting: "1911 Nobel Prize in Chemistry; medical radium supply", certainty: 1.0, cites: [{source: S1, locator: "'Move to Paris'"}, {source: S2, locator: "paragraphs 2, 6"}], how_known: "Two sources."}
  evidence_of_impact:
    - {value: "First woman to win a Nobel Prize and only woman to win in two different fields", kind: "honours in lifetime", certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}], how_known: "Britannica."}
  major_works:
    - {value: "Recherches sur les substances radioactives (doctoral thesis)", year: 1903, kind: book, certainty: 0.7, cites: [{source: S2, locator: "paragraph 5 (dated 1904)"}, {source: S1, locator: "'Move to Paris' (doctorate June 1903)"}], how_known: "S2 gives 1904 for the published book; S1 gives the June 1903 doctorate."}
    - {value: "Traité de radioactivité", year: 1910, kind: book, certainty: 1.0, cites: [{source: S2, locator: "paragraph 5"}], how_known: "Nobel biography."}
  honours:
    - {value: "Nobel Prize in Physics (shared with Pierre Curie and Henri Becquerel)", year: 1903, certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}, {source: S2, locator: "paragraph 6"}], how_known: "Two sources."}
    - {value: "Davy Medal of the Royal Society (with Pierre Curie)", year: 1903, certainty: 1.0, cites: [{source: S1, locator: "'Move to Paris'"}, {source: S2, locator: "paragraph 6"}], how_known: "Two sources."}
    - {value: "Nobel Prize in Chemistry", year: 1911, certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}, {source: S2, locator: "paragraph 6"}], how_known: "Two sources."}
  definition_fit: {value: "clearly meets", rationale: "Discovered two elements and founded the study of radioactivity.", certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}], how_known: "Sources agree."}

childhood:
  family_religion: {value: "Catholic", certainty: 1.0, cites: [{source: S3, locator: "ch. IV, footnote 6; Autobiographical Notes, ch. I"}, {source: S7, locator: "p. 73 n. 1; p. 157"}, {source: S4, locator: "p. 51"}], how_known: "Her own statement ('my parents were both Catholics') and her daughter's biography."}
  family_religious_practice: {value: "Mother devout ('an ardent piety'); father 'a lukewarm Catholic, a freethinker without acknowledging it'", certainty: 0.7, cites: [{source: S3, locator: "Autobiographical Notes, ch. I"}, {source: S4, locator: "p. 51"}], how_known: "The mother's piety is in her own words (S3); the father's description is Eve Curie's (S4), so 0.7."}
  parents_and_household:
    - {value: "Father, Władysław Skłodowski, teacher of physics and mathematics at a Warsaw lycée", name: "Władysław Skłodowski", role: father, certainty: 1.0, cites: [{source: S3, locator: "Autobiographical Notes, ch. I"}, {source: S7, locator: "p. 156"}, {source: S4, locator: "p. 3 ('Vladislav Sklodovski, professor of physics')"}, {source: S1, locator: "'Early life'"}], how_known: "Three sources; S4 spells the name 'Vladislav Sklodovski'."}
    - {value: "Mother, director of a Warsaw girls' school; died of tuberculosis when Marie was about ten (S3 says nine)", name: "Bronisława Skłodowska", role: mother, certainty: 0.7, cites: [{source: S3, locator: "Autobiographical Notes, ch. I"}, {source: S5, locator: "pp. 3, 5"}], how_known: "S3 says she was 'only nine years old'; S5 says ten (May 1878). Mother's given name from S5; not quote-checked."}
  household_circumstances: {value: "Five children; the eldest daughter Zosia died at fourteen and the mother soon after; the father lost his savings", certainty: 1.0, cites: [{source: S3, locator: "Autobiographical Notes, ch. I"}, {source: S7, locator: "p. 157"}, {source: S1, locator: "'Early life'"}], how_known: "Two sources."}
  schooling:
    - {value: "Warsaw schools, including Mlle Sikorska's private school; gold medal at the Russian lycée at 16", stage: "grammar or secondary school", certainty: 1.0, cites: [{source: S1, locator: "'Early life'"}, {source: S4, locator: "p. 16"}], how_known: "Two sources."}
    - {value: "Clandestine Polish 'free university'", stage: other, certainty: 1.0, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}
    - {value: "Sorbonne: licence in physical sciences (1893, first) and mathematical sciences (1894, second)", stage: university, years: "1891–1894", certainty: 1.0, cites: [{source: S1, locator: "'Move to Paris'"}, {source: S2, locator: "paragraph 1"}], how_known: "Two sources."}
  early_mathematics: {value: "other", note: "'I learned easily mathematics and physics, as far as these sciences were taken in consideration in the school' (S3)", certainty: 0.7, cites: [{source: S3, locator: "Autobiographical Notes, ch. I"}], how_known: "Her own account; level not stated."}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure:
    - {value: "Her father taught physics and 'enjoyed any explanation he could give us about Nature and her ways'", certainty: 1.0, cites: [{source: S3, locator: "Autobiographical Notes, ch. I"}, {source: S7, locator: "p. 161"}], how_known: "Her own account."}
  key_early_reading: []
  childhood_mentors:
    - {value: "Her father", certainty: 1.0, cites: [{source: S3, locator: "Autobiographical Notes, ch. I"}, {source: S7, locator: "p. 161"}], how_known: "Her own account."}
  languages_in_childhood: {value: [Polish, Russian], certainty: 0.7, cites: [{source: S1, locator: "'Early life' (Russian lycée)"}, {source: S3, locator: "Autobiographical Notes, ch. I"}], how_known: "Polish home; Russian-language schooling under Russian rule."}
  notable_events:
    - {value: "Deaths of her eldest sister and then her mother; 'the first great sorrow of my life'", year: "1876–1878", certainty: 1.0, cites: [{source: S3, locator: "Autobiographical Notes, ch. I"}, {source: S7, locator: "p. 157"}, {source: S5, locator: "p. 5"}], how_known: "Her own account; S5 dates the mother's death May 1878."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1894–1934", certainty: 1.0, cites: [{source: S1, locator: "'Move to Paris'"}, {source: S2, locator: "paragraphs 1–7"}], how_known: "From laboratory work in Paris to her death."}
  nominal_affiliations:
    - {value: "Raised Catholic; no practice in adult life; civil wedding (1895)", years: "1867–1934", role: "former member", certainty: 1.0, cites: [{source: S3, locator: "ch. IV (marriage)"}, {source: S7, locator: "p. 80"}, {source: S4, locator: "p. 137"}, {source: S5, locator: "p. 18"}], how_known: "Her own statement that she 'did not practice any' religion, and two other sources on the civil ceremony."}
  self_described_science_religion_relation:
    value: "None stated as such. As a young woman she wrote that the consolation of 'God willed it' 'is not for everybody' and that she could not share believers' faith, while respecting sincere faith; her published account of radioactive decay calls its causes 'a mystery to us'."
    certainty: 0.5
    cites: [{source: S4, locator: "p. 76"}, {source: S3, locator: "ch. VI"}]
    how_known: "One 1887 letter in translation, quoted by her daughter, plus her 1923 book; none addresses science and religion directly."
  primary_system:
    value: BELOW_THRESHOLD
    cites: [{source: S4, locator: "pp. 29, 51, 76"}, {source: S5, locator: "pp. 18, 57"}, {source: S3, locator: "ch. IV (marriage)"}]
    how_known: "Direct evidence shows loss of faith and no practice, but not which non-theist position she held. Her own words: she 'did not practice any' religion (S3, 1923) and in 1887 could not understand or share believers' faith (S4, p. 76). Two biographers say her faith was lost after her mother's death (S4, pp. 29, 51; S5, p. 18), and S5 groups her with the 'liberal freethinkers like Marie and her friends' against conservative Catholics (S5, p. 57). AGNOS needs 'explicit suspension' and ATHE 'positive naturalism' (v7.1 rule in both system files); nothing read gives either, and the earlier AGNOS choice rested on the absence of a denial of God. So no code reaches 0.5."
    note: "Was AGNOS at 0.5 (lens audit, batch 2, finding #108; treated like Fermi). Candidates: AGNOS or ATHE. 'Freethinker' (S5, p. 57) fits either. Needs her French correspondence, the 1906–07 mourning journal, or a biographer's report of her own words (Goldsmith 2005; Reid)."
  secondary_system: {value: UNKNOWN, how_known: "No second system in S1–S5."}
  candidate_codes_considered:
    - {code: AGNOS, reason: "Candidate, not coded (BELOW_THRESHOLD): no explicit suspension of judgement in anything read; the earlier choice rested on the absence of a denial of God. AGNOS is a stub system file (flag).", cites: [{source: S4, locator: "pp. 51, 76"}]}
    - {code: ATHE, reason: "Candidate, not coded (BELOW_THRESHOLD): a freethinker by S5's description ('liberal freethinkers like Marie and her friends') and no God-term in her adult writing read, but no positive statement of naturalism. ATHE is a stub system file (flag).", cites: [{source: S5, locator: "p. 57"}, {source: S4, locator: "p. 137"}]}
    - {code: CHRIST, reason: "Rejected for the adult unit: Catholic upbringing only; she 'did not practice any' religion. Heritage and upbringing are never a code.", cites: [{source: S3, locator: "ch. IV (marriage)"}]}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "No statement placing or denying God was found; she speaks only of others' faith.", note: "Gap: her French correspondence and 1906–07 mourning journal (published in Polish and French) were not read."}
    B_cause:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S3, locator: "ch. VI (exponential law)"}, {source: S4, locator: "p. 76 (letter of 1887-04-04)"}]
      how_known: "Her published 1923 account of nature (P6), read in the 1923 English translation; supported by a single private letter. Below the 1.0 ceiling because neither passage speaks to miracle directly."
      rationale: "Scored on her account of nature (P6). She describes radioactive transformation as following 'the laws of probability', with causes 'a mystery to us' and no outside action shown to affect it: lawful, with an open question, not an exemption. In 1887 she wrote that she could not take the consolation of 'God willed it' for a stillbirth. No miracle, providence or petition appears in anything read."
    C_ledger: {value: BELOW_THRESHOLD, how_known: "Nothing on judgement, afterlife or moral reckoning in what was read. The 1887 line about not disappearing 'into nothingness' (S4, p. 77) is about sinking into obscurity as a governess, not about death, so it is not evidence for C (lens audit, batch 2, finding #126).", note: "Gap: her mourning journal after Pierre's death (1906)."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "No statement on revelation, scripture or church authority in anything read. The earlier score (4 at 0.5) came from that absence; 'for us it has become incomprehensible' (S4, p. 76) is about believers' faith and the religious conservatism around her, not about which authority decides; her daughter's 'by tradition and convention' (S4, p. 51) is about practice.", note: "Was 4 at 0.5 (lens audit, batch 2, finding #112). Same treatment as Fermi: D asks about revelation versus observation, which needs a statement."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Scored on the world's order (P7). Nothing read addresses favour for a group in events; not scored from working science alone (same treatment as Fermi and Meitner)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD, so the P4 test cannot be applied."}
  statements:
    - text: "a civil ceremony, for Pierre Curie professed no religion, and I myself did not practice any."
      cites: [{source: S3, locator: "ch. IV, 'Marriage and Organization of Family Life'"}, {source: S7, locator: "p. 80"}]
      date: "1923"
      context: "Her account of the July 1895 wedding, in her published life of Pierre Curie (English translation by Charlotte Kellogg)."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
    - text: "The exponential law has a profound philosophic bearing; it indicates that the transformation is produced according to the laws of probability. The causes that determine the transformation are a mystery to us"
      cites: [{source: S3, locator: "ch. VI"}, {source: S7, locator: "p. 123"}]
      date: "1923"
      context: "On radioactive decay; she goes on: 'no exterior action has shown itself effective in influencing the transformation'."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
    - text: "If one could only say, with Christian resignation, “God willed it and his will be done!” half of the terrible bitterness would be gone. Alas, that consolation is not for everybody."
      cites: [{source: S4, locator: "p. 76"}]
      date: "1887-04-04"
      context: "Letter to her cousin Henrietta, who had just given birth to a dead child. The OCR prints the year as 'i88y'."
      axes: [B_cause, D_authority]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-02
    - text: "the more I recognize how lucky they are the less I can understand their faith, and the less I feel capable of sharing their happiness."
      cites: [{source: S4, locator: "p. 76"}]
      date: "1887-04-04"
      context: "Same letter; she adds: 'Let everybody keep his own faith, so long as it is sincere.'"
      axes: [D_authority]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-02
    - text: "I, even I, keep a sort of hope that I shall not disappear completely into nothingness."
      cites: [{source: S4, locator: "p. 77"}]
      date: "1887-05-20"
      context: "Letter to her brother Joseph, on her work as a governess, her fear of 'getting terribly stupid' and her wish to be 'of some use'; it follows 'petty annoyances with the babas'."
      note: "About sinking into obscurity, not survival after death, so no axis is tagged (lens audit, batch 2, finding #126)."
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-02
  changes_over_life:
    - {value: "Lost her childhood Catholic faith after the deaths of her sister and mother; kept outward practice 'by tradition and convention' for some years", year: "c. 1878–1885", certainty: 0.7, cites: [{source: S4, locator: "pp. 29, 51"}, {source: S5, locator: "p. 18"}], how_known: "Two biographers; dates approximate."}
  coder_notes: "AGNOS and ATHE are stub system files (flag). The 1887 letters are Sheean's English translation of Polish letters, quoted by Eve Curie; page numbers are the printed pages, confirmed against the page scans (lens audit, batch 2). Pierre Curie (1923) is read in the Kellogg translation on Project Gutenberg; the book gives no page numbers there, so locators are chapters."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Polish, from small landed gentry families", certainty: 1.0, cites: [{source: S3, locator: "Autobiographical Notes, ch. I"}, {source: S7, locator: "pp. 155–156"}], how_known: "Her own account."}
  religious_heritage_by_birth: {value: "Catholic", certainty: 1.0, cites: [{source: S3, locator: "ch. IV, footnote 6"}, {source: S7, locator: "p. 73 n. 1"}], how_known: "Her own statement."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated in S1–S5."}
  childhood_catechism: {value: "Catholic prayers taught at school (in Russian, under Russian rule)", certainty: 0.5, cites: [{source: S4, locator: "p. 20"}], how_known: "Eve Curie's narrative only."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1898–1911", certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}, {source: S2, locator: "paragraphs 2, 6"}], how_known: "Polonium and radium to the second Nobel Prize."}
  age_at_first_lasting_contribution: {value: 30, certainty: 1.0, cites: [{source: S1, locator: "Quick Facts; 'Move to Paris'"}], how_known: "Born November 1867; polonium in summer 1898."}
  first_evidence_of_lio_type_views: {value: "Letter declining the consolation of 'God willed it'", year: 1887, certainty: 0.5, cites: [{source: S4, locator: "p. 76"}], how_known: "Earliest dated statement read; a lapse of faith, not an LIO view as such."}
  lio_views_relative_to_major_work: {value: "before major work", rationale: "Her loss of faith (1887 letters) predates the 1898 work; the lawful account of decay is in the 1923 book.", certainty: 0.5, cites: [{source: S4, locator: "pp. 76–77"}, {source: S3, locator: "ch. VI"}], how_known: "Dates."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "'Move to Paris'"}], how_known: "Experimental physicist and chemist; nothing on deductive form read."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S3, locator: "Autobiographical Notes, ch. I"}], how_known: "Nothing read."}
  circle_present: {value: "no", rationale: "No God-Nature identity in anything read.", certainty: 0.5, cites: [{source: S4, locator: "pp. 51, 76"}], how_known: "Absence in the sources read."}
  reading: "As belief, not finding: form unclear, no circle. The record does not test H1."
  notes: ""

institutions:
  - {value: "École Normale Supérieure for girls, Sèvres", role: "lecturer in physics", years: "1900–", kind: employer, certainty: 1.0, cites: [{source: S1, locator: "'Move to Paris' (last paragraph)"}], how_known: "Britannica."}
  - {value: "Faculty of Sciences, University of Paris (Sorbonne)", role: "professor of general physics (first woman in the post)", years: "1906–1934", kind: employer, certainty: 1.0, cites: [{source: S2, locator: "paragraph 1"}], how_known: "Nobel biography."}
  - {value: "Radium Institute, University of Paris (Curie Laboratory)", role: director, years: "1914–1934", kind: employer, certainty: 1.0, cites: [{source: S2, locator: "paragraph 1"}], how_known: "Nobel biography."}
collaborators:
  - {value: "Pierre Curie", roster_id: curie-pierre, relation: family, note: "husband and co-discoverer of polonium and radium", certainty: 1.0, cites: [{source: S1, locator: "'Move to Paris'"}, {source: S2, locator: "paragraphs 1–2"}], how_known: "Two sources."}
  - {value: "Henri Becquerel", roster_id: becquerel-henri, relation: "influenced by", note: "his 1896 discovery started her thesis; shared the 1903 prize", certainty: 1.0, cites: [{source: S1, locator: "'Move to Paris'"}, {source: S2, locator: "paragraphs 2, 6"}], how_known: "Two sources."}
  - {value: "André-Louis Debierne", relation: collaborator, note: "helped obtain metallic radium", certainty: 1.0, cites: [{source: S1, locator: "'Move to Paris'"}], how_known: "Britannica."}
  - {value: "Irène Joliot-Curie", roster_id: joliot-curie-irene, relation: family, note: "daughter; assisted her with wartime radiology", certainty: 1.0, cites: [{source: S2, locator: "paragraph 3"}], how_known: "Nobel biography."}
  - {value: "Gabriel Lippmann", relation: teacher, note: "lecturer at the Sorbonne; she worked in his laboratory", certainty: 1.0, cites: [{source: S1, locator: "'Move to Paris'"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v7.1 (F 4) and v8 (F 5, all five models).", certainty: 0.7, cites: [{source: S6, locator: "roster.csv, rank 56"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Field split across models: physics (Claude, Grok), physics-chemistry (DeepSeek), chemistry-physics (Gemini), chemistry (GPT); the roster keeps physics."
    - "Age at her mother's death: nine in her own notes (S3), ten in S5."
    - "The 1887 letters are English translations (Sheean) quoted by her daughter; the archive.org OCR misreads the year as 'i88y'."
    - "Britannica was read as its first page only."
  open_questions:
    - "Read her 1906–07 mourning journal and her French and Polish letters for any later statement on God or survival."
    - "Check Goldsmith, Obsessive Genius (2005), and Reid (1974/1978) for a direct 'agnostic' self-description."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "\"Marie Curie.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Marie-Curie."
    url: "https://www.britannica.com/biography/Marie-Curie"
    accessed: 2026-10-02
    reliability_note: "Editorial article; first page only (Quick Facts, opening, 'Early life', 'Move to Paris, Pierre Curie, and first Nobel Prize'). Sections cited by heading."
    used_for: [identity, basics, contribution, childhood, worldview, timing, lane_b, institutions, collaborators]
  - id: S2
    type: tertiary
    kind: "institutional page"
    author: "Nobel Foundation"
    year: 1967
    citation: "\"Marie Curie – Biographical.\" From Nobel Lectures, Physics 1901–1921. Amsterdam: Elsevier, 1967. NobelPrize.org. https://www.nobelprize.org/prizes/physics/1903/marie-curie/biographical/."
    url: "https://www.nobelprize.org/prizes/physics/1903/marie-curie/biographical/"
    accessed: 2026-10-02
    reliability_note: "Short official biography; paragraphs counted from the start of the text."
    used_for: [identity, basics, contribution, childhood, worldview, timing, institutions, collaborators]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "Marie Curie"
    year: 1923
    citation: "Curie, Marie. Pierre Curie, with Autobiographical Notes. Translated by Charlotte and Vernon Kellogg. New York: Macmillan, 1923. Project Gutenberg eBook #69617. https://www.gutenberg.org/ebooks/69617."
    url: "https://www.gutenberg.org/cache/epub/69617/pg69617.txt"
    accessed: 2026-10-02
    reliability_note: "Her own book in its 1923 English edition; the Gutenberg text has no page numbers, so locators are chapters (the Autobiographical Notes have their own chapters I–IV). Project Gutenberg is an unofficial web copy, so under CODING_GUIDE §7 it cannot by itself support certainty 1.0. Its wording was checked against the library scan S7, so every field that cites S3 at 1.0 also cites S7 with a page."
    used_for: [identity, basics, childhood, worldview, heritage, timing, lane_b]
  - id: S4
    type: secondary
    kind: "scholarly book"
    author: "Eve Curie"
    year: 1937
    citation: "Curie, Eve. Madame Curie: A Biography. Translated by Vincent Sheean. Garden City, NY: Doubleday, Doran, 1937 (1938 printing). Internet Archive OCR text. https://archive.org/details/madamecuriebiogr00evec_0."
    url: "https://archive.org/stream/madamecuriebiogr00evec_0/madamecuriebiogr00evec_0_djvu.txt"
    accessed: 2026-10-02
    reliability_note: "Biography by her daughter, quoting family letters in translation. Read as OCR text; page numbers are the printed pages from the running heads, confirmed against the page scans. archive.org's /page/nN image index is not the printed page: n48 = p. 29, n72 = p. 51, n97 = p. 76, n98 = p. 77, n162 = p. 137 (one lower than the hOCR leaf number)."
    used_for: [identity, childhood, worldview, heritage, timing, lane_b]
  - id: S5
    type: secondary
    kind: "institutional page"
    author: "Naomi Pasachoff"
    year: 2005
    citation: "Pasachoff, Naomi. \"Marie Curie and the Science of Radioactivity.\" American Institute of Physics web exhibit (PDF of the exhibit text, site created 2000, revised 2005). https://history.aip.org/exhibits/curie/curie.pdf."
    url: "https://history.aip.org/exhibits/curie/curie.pdf"
    accessed: 2026-10-02
    reliability_note: "AIP exhibit based on Pasachoff's 1996 Oxford University Press book. Page numbers are the PDF's 'Page n of 79' footers."
    used_for: [basics, childhood, worldview]
  - id: S6
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
  - id: S7
    type: primary
    kind: "published work by the subject"
    author: "Marie Curie"
    year: 1923
    citation: "Curie, Marie. Pierre Curie. Translated by Charlotte and Vernon Kellogg, with an introduction by Mrs. William Brown Meloney and Autobiographical Notes by Marie Curie. New York: The Macmillan Company, 1923. Phillips Academy, Oliver Wendell Holmes Library copy, Internet Archive scan, https://archive.org/details/pierrecurie0000curi."
    url: "https://archive.org/details/pierrecurie0000curi"
    accessed: 2026-10-02
    reliability_note: "Library scan of the 1923 Macmillan edition that S3 transcribes. Used to check S3: every quotation and every S3 fact used by a certainty-1.0 field was found word for word in the scan's OCR text. Page numbers are the printed ones. S3's 'ch. IV, footnote 6' is p. 73 n. 1 here; the Autobiographical Notes are pp. 155 ff."
    used_for: [identity, basics, childhood, worldview, heritage]
---

# Marie Curie

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Marie Curie (1867–1934), Polish-born French physicist and chemist, discovered polonium and radium with Pierre Curie in 1898 and won Nobel Prizes in physics (1903) and chemistry (1911) [S1, opening paragraph; S2, paragraph 6]. Raised Catholic, she lost her faith after her mother's death and "did not practice any" religion as an adult [S3, ch. IV; S5, p. 18]. Her system is below threshold (AGNOS or ATHE; a "liberal freethinker" in S5, p. 57); B 4 (0.7); A, C, D, E below threshold; mid_basin below threshold.

## Life and work

Born in Warsaw under Russian rule, she worked as a governess, attended the clandestine "free university", and went to Paris in 1891 [S1, 'Early life'; 'Move to Paris']. She succeeded Pierre Curie as professor in 1906 and directed the Curie Laboratory of the Radium Institute from 1914 [S2, paragraph 1].

## Contribution and impact

Polonium and radium (1898), the term "radioactivity", and the isolation of radium [S1, 'Move to Paris'; S2, paragraph 2].

## Childhood and education

Her mother "had an ardent piety (my parents were both Catholics), but she was never intolerant" [S3, Autobiographical Notes, ch. I]. Her eldest sister and then her mother died when she was a child; she called it "the first great sorrow of my life" [S3, Autobiographical Notes, ch. I].

## Adult working worldview

Her daughter writes that "her faith had been shaken by Mme Sklodovska's death; little by little it had now evaporated" [S4, p. 51]. In 1887 she wrote that the consolation of "God willed it" "is not for everybody" and that she could not share believers' faith [S4, p. 76]. AIP's exhibit places her among the "liberal freethinkers" of French politics [S5, p. 57]. She married in a civil ceremony [S3, ch. IV]. In 1923 she described radioactive decay as following "the laws of probability", with causes "a mystery to us" [S3, ch. VI]. Scores: B 4 (0.7); A, C, D, E below threshold.

## Heritage (context only)

Polish Catholic gentry family [S3, Autobiographical Notes, ch. I]. Context only.

## Timing

First lasting contribution 1898, at 30 [S1]. Her loss of faith predates the major work [S4, pp. 51, 76].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form unclear; no circle.

## Open questions

- Her 1906–07 mourning journal and French or Polish letters; Goldsmith (2005) and Reid for any self-description as agnostic.

## Research log

- 2026-10-02: Read Britannica (first page), the Nobel biography, the AIP exhibit PDF (Pasachoff), Pierre Curie with Autobiographical Notes (Gutenberg #69617) and Eve Curie's Madame Curie (archive.org OCR). MacTutor has no Curie biography (short page). Quotations checked against the downloaded texts.
