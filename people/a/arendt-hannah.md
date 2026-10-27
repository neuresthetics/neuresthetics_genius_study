---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch F; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to philosophy. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch F, order P32: F 5, rank 34). Basics from SEP (Tömmel and Passerin d'Entrèves) and Britannica. Worldview evidence: one private letter to Jaspers (4 March 1951) stating a 'trust' in God distinct from faith and no interest in traditional religion, read only as a Spanish quotation in Araos (Humanitas). Single private letter, secondary quotation, and no locus or nature statement: primary_system and A BELOW_THRESHOLD; B, C, D, E UNKNOWN; mid_basin UNKNOWN. Draft, not reviewed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #34, next-50 batch). Needs: A BELOW_THRESHOLD; B UNKNOWN. Re-opened Araos Humanitas full web text (S3; Spanish 1951 letter + Denktagebuch May 1965); Wikipedia EN (S7); JWA Whitfield (S8); Young-Bruehl Spanish Paidós/elboomeran PDF (S9) for Vogelstein childhood and non-religious parents; Zawisza Cryptotheology MDPI 2018 (S10) scholarly reconstruction (not used to lift A). P47 source_quality on every source. A stays BELOW_THRESHOLD: 1951 private letter states trust in God but nothing on where God is (locus); single private letter below 0.5 unless scholar backs a scored locus reading (§3); Araos backs belief, not locus; cryptotheology/Denktagebuch speculative politics not confession. B stays UNKNOWN (P16/P30): not a scientist; lasting contributions are political philosophy, not theories about natural systems; no explicit nature-order remark in S1–S10 (Human Condition earth/labor anthropological; Zawisza Augustine/tzimtzum are scholarly reconstruction, not her B). Childhood/heritage filled. Chart: still unplotted. No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: arendt-hannah
  display_name: "Hannah Arendt"
  roster:
    canonical_name: "Hannah Arendt"
    rank: 34
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: philosophy
    field_bucket: philosophy
  full_name: {value: "Hannah Arendt (born Johanna Arendt)", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "infobox / lead (Johanna Arendt)"}], how_known: "SEP Hannah Arendt; Wikipedia birth name Johanna Arendt."}
  native_name: {value: "Johanna Arendt", certainty: 0.7, cites: [{source: S7, locator: "infobox Other name / Born"}], how_known: "German in Latin script; Wikipedia."}
  aliases:
    - {name: "Arendt-Hannah", kind: "roster alias"}
    - {name: "Hannah-Arendt", kind: "roster alias"}
    - {name: "Hannah Arendt Bluecher", kind: "other"}

basics:
  birth:
    date: {value: "1906-10-14", calendar: gregorian, certainty: 1.0, cites: [{source: S2, locator: "opening"}, {source: S7, locator: "infobox"}, {source: S8, locator: "Early Life"}], how_known: "Britannica, Wikipedia, and JWA agree on the day."}
    place: {value: "Linden (Hannover), Germany", modern_name: "Hanover (Linden district), Lower Saxony, Germany", polity_then: "German Empire (Prussia)", certainty: 1.0, cites: [{source: S7, locator: "Born … Linden, Province of Hanover"}, {source: S8, locator: "born … in Hanover"}, {source: S1, locator: "§1"}], how_known: "Wikipedia Linden; JWA/SEP/Britannica Hanover/Hannover — same city (Linden now a Hanover district)."}
  death:
    date: {value: "1975-12-04", calendar: gregorian, certainty: 1.0, cites: [{source: S2, locator: "opening"}, {source: S7, locator: "infobox"}, {source: S1, locator: "§1 (year)"}], how_known: "Britannica and Wikipedia agree on the day."}
    place: {value: "New York, New York, U.S.", modern_name: "New York City, United States", polity_then: "United States", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "opening"}, {source: S7, locator: "infobox"}], how_known: "Three sources."}
  first_lasting_contribution_year: {value: 1951, certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "Origins paragraph"}], how_known: "Earliest listed lasting contribution, The Origins of Totalitarianism (1951) (P13). The 1929 dissertation (S1 §1) is not listed: SEP treats it as background, not as itself lasting."}
  era_bucket: {value: "1950 on", certainty: 1.0, cites: [{source: S1, locator: "§1"}], how_known: "From 1951 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "opening"}], how_known: "Germany (P3)."}
  region_of_work: {value: "North America", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "text"}], how_known: "New York from 1941; all listed works written in the US."}
  sex_as_recorded: {value: "female", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [English, German], certainty: 0.7, cites: [{source: S1, locator: "§1 (German dissertation; English books)"}], how_known: "SEP."}
  occupations: {value: ["political philosopher", "professor", "editor"], certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "text"}], how_known: "Two sources."}

contribution:
  primary_domain: philosophy
  fields: {value: ["political philosophy"], certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "opening"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "The Origins of Totalitarianism", year: 1951, kind: work, lasting: "'generated a wide-ranging debate on the nature and historical antecedents of the totalitarian phenomenon' (S1)", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Origins paragraph"}], how_known: "Two sources."}
    - {value: "The Human Condition (vita activa: labor, work, action)", year: 1958, kind: work, lasting: "'an original philosophical study' (S1)", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Human Condition paragraph"}], how_known: "Two sources."}
    - {value: "Eichmann in Jerusalem; the 'banality of evil'", year: 1963, kind: work, lasting: "coined 'banality of evil' (S1)", certainty: 1.0, cites: [{source: S1, locator: "opening; §6.1"}, {source: S2, locator: "Eichmann paragraph"}], how_known: "Two sources."}
    - {value: "The Life of the Mind (thinking, willing, judging), unfinished, published 1978", year: 1975, kind: work, lasting: "'her last major philosophical work' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "last paragraph"}], how_known: "Posthumous: dated by the death year, as no later documented act in life was read (P30). Two volumes complete at her death (S1)."}
  evidence_of_impact:
    - {value: "Origins became 'a classic' (SEP)", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "SEP: 'one of the most influential political philosophers of the twentieth century'.", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}

childhood:
  family_religion: {value: "Assimilated German-Jewish; grandparents Reform synagogue (Königsberg); parents non-religious Social Democrats", certainty: 1.0, cites: [{source: S7, locator: "Family: parents non-religious; Max Arendt Reform synagogue"}, {source: S9, locator: "Ni el padre ni la madre … eran religiosos, pero enviaron a su hija a la sinagoga"}, {source: S1, locator: "opening"}], how_known: "Wikipedia + Young-Bruehl (Spanish) + SEP. Heritage only — not adult A."}
  family_religious_practice: {value: "Parents non-religious; child taken to Reform synagogue with paternal grandparents; rabbi Hermann Vogelstein gave religious instruction at home / school from about age seven", certainty: 1.0, cites: [{source: S7, locator: "Although Hannah's parents were non-religious… Vogelstein"}, {source: S9, locator: "Vogelstein … educación religiosa … siete años"}], how_known: "Wikipedia + Young-Bruehl. Practice is childhood/heritage, not adult A (P19)."}
  parents_and_household:
    - {value: "Paul Arendt (father; engineer; Classics library; died 30 Oct 1913 of syphilis/paresis when Hannah was seven)", certainty: 1.0, cites: [{source: S7, locator: "Parents; died 30 October 1913"}, {source: S8, locator: "father, an engineer, died of paresis"}, {source: S9, locator: "Paul … ingeniero"}], how_known: "Wikipedia + JWA + Young-Bruehl."}
    - {value: "Martha Cohn Arendt (later Beerwald; mother; musician; Social Democrat; studied music/French in Paris)", certainty: 1.0, cites: [{source: S7, locator: "Martha Cohn"}, {source: S9, locator: "Martha … París tres años"}], how_known: "Wikipedia + Young-Bruehl."}
    - {value: "Paternal grandfather Max Arendt (Königsberg Jewish community leader, Centralverein)", certainty: 0.7, cites: [{source: S7, locator: "Max Arendt"}], how_known: "Wikipedia."}
    - {value: "Stepfather Martin Beerwald (married Martha 1920); stepsisters Clara and Eva Beerwald", certainty: 0.7, cites: [{source: S7, locator: "Beerwald"}, {source: S8, locator: "Martin Beerwald … Eva and Clara"}], how_known: "Wikipedia + JWA."}
  household_circumstances: {value: "Born Linden; family returned to Königsberg 1909 (Paul's health); Tiergartenstraße / Hufen Jewish neighborhood; father's Classics library; temporary Berlin flight Aug 1914 (WWI)", certainty: 0.7, cites: [{source: S7, locator: "Family; Early education"}, {source: S9, locator: "biblioteca … clásicos"}], how_known: "Wikipedia + Young-Bruehl."}
  schooling:
    - {value: "Szittnich School / Hufen-Oberlyzeum, Königsberg (Bahnstraße); interrupted by WWI Berlin stay", stage: elementary school, run_by: "state or municipal", years: "1913–", ages: "6–", certainty: 0.7, cites: [{source: S7, locator: "enrolled in the Szittnich School … August 1913"}], how_known: "Wikipedia."}
    - {value: "Königin-Luise-Schule (girls' Gymnasium), Königsberg; expelled 1922 (age 15) for leading a teacher boycott", stage: "grammar or secondary school", run_by: "state or municipal", years: "–1922", ages: "–15", certainty: 0.7, cites: [{source: S7, locator: "Königin-Luise-Schule; expelled … 1922"}], how_known: "Wikipedia."}
    - {value: "Audited University of Berlin (classics; Christian theology under Romano Guardini); Abitur for Marburg", stage: university, run_by: "state or municipal", years: "1922–1924", ages: "15–17", certainty: 0.7, cites: [{source: S7, locator: "Berlin (1922–1924); Guardini"}], how_known: "Wikipedia."}
    - {value: "Universities of Marburg (Heidegger), Freiburg (Husserl), Heidelberg (Jaspers); doctorate Der Liebesbegriff bei Augustin", stage: university, run_by: "state or municipal", years: "1924–1929", ages: "18–23", certainty: 0.5, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "second paragraph"}, {source: S7, locator: "doctorate … 1929"}], how_known: "Start 1924 from Britannica/Wikipedia. End year: SEP/Wikipedia 1929 dissertation; Britannica has also given 1928 for the degree (P25: 0.5)."}
  early_mathematics: {value: "none known", certainty: 0.7, cites: [{source: S7, locator: "Early education (Greek, literature, philosophy; no mathematics named)"}, {source: S1, locator: "§1"}], how_known: "Childhood sources emphasize Greek, literature, Kierkegaard/Kant/Jaspers by 14; no mathematics level named before 18."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Nothing on Euclid-style proof training in childhood sources read (S1, S7, S9)."}
  early_science_exposure: []
  key_early_reading:
    - {value: "Greek and Latin classics from father's library; Goethe (mother's Bildung program)", certainty: 0.7, cites: [{source: S9, locator: "biblioteca … clásicos griegos y latinos"}, {source: S7, locator: "Goethean lines; Unser Kind"}], how_known: "Young-Bruehl + Wikipedia."}
    - {value: "By age 14: Kierkegaard; Jaspers' Psychologie der Weltanschauungen; Kant's Kritik der reinen Vernunft", certainty: 0.7, cites: [{source: S7, locator: "By the age of 14, she had read Kierkegaard…"}], how_known: "Wikipedia."}
  childhood_mentors:
    - {value: "Rabbi Hermann Vogelstein (Reform; home/school religious instruction from ~age 7)", certainty: 0.7, cites: [{source: S7, locator: "Vogelstein"}, {source: S9, locator: "Vogelstein … siete años"}], how_known: "Wikipedia + Young-Bruehl. Heritage/instruction, not adult A."}
  languages_in_childhood: {value: [German, Greek], certainty: 0.7, cites: [{source: S7, locator: "learning ancient Greek as a child; Muttersprache"}, {source: S9, locator: "clásicos griegos"}], how_known: "German mother tongue; Wikipedia ancient Greek as a child. French/Hebrew later (Paris), not childhood."}
  notable_events:
    - {value: "Told Vogelstein she had stopped believing in God; he replied (YB): who asked you to believe in Him?", certainty: 0.7, cites: [{source: S9, locator: "había dejado de creer en Dios … ¿Y quién te pidió"}, {source: S3, locator: "Young-Bruehl episode (secondary pointer)"}], how_known: "Young-Bruehl (Spanish); Araos also summarizes. Childhood declaration — not scored as adult A (P19/P20)."}
    - {value: "Father died 30 Oct 1913 (age 7); later recalled thinking of God from that age and not wanting to bother God with prayers", certainty: 0.5, cites: [{source: S3, locator: "Denktagebuch May 1965 quotation; 'no hay que molestar a Dios con oraciones'"}], how_known: "Araos quoting Denktagebuch / mother notes; scholarly secondary. Retrospective, not a locus score."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1951–1975", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: BELOW_THRESHOLD, how_known: "1951 private letter to Jaspers (S5 via S3/S6) addresses God and traditional religion, not science-and-religion as such.", note: "Single private letter; no science-religion statement."}
  primary_system:
    value: BELOW_THRESHOLD
    how_known: "Deepen D1: still one private letter to Jaspers (4 March 1951), to be cited from Briefwechsel (Piper 1985) or Kimber English Correspondence (Harcourt 1992) (S5); wording verified here from Araos's full Spanish quotation (S3, Humanitas web text now opened) and a German excerpt (S6): a 'trust' in God, with childish/unquestioned character, and traditional religion, Jewish or Christian, means nothing to her as such. Single private letter is below 0.5 unless a scholar backs a scored system reading (§3); Araos backs 'creía en Dios' (belief), which names no system. Zawisza (S10) cryptotheology is scholarly reconstruction of political theology / Augustine reception, not a codeable affiliation. Young-Bruehl childhood 'stopped believing' is childhood, not adult working worldview (P20)."
    note: "The letter supports belief in God of some kind but excludes practised JUDA and CHRIST, and says nothing on revelation, creation, or intervention as a system. No code fits without a guess. Coder's call: BELOW_THRESHOLD."
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: JUDA, reason: "Jewish identity is central to her writing and heritage (grandparents Reform; Vogelstein instruction), but the 1951 letter says traditional Jewish religion no longer means anything to her as such. Rejected (heritage, not worldview)."}
    - {code: CHRIST, reason: "Same letter; Augustine dissertation and later Christian-motif politics (natality, Christ in Human Condition) are scholarship/political theory, not profession of CHRIST. Rejected."}
    - {code: DEISM, reason: "Would need a stated rejection of revelation (P27). Not found. Rejected."}
    - {code: CLTHEI, reason: "No statement on intervention or petition as adult doctrine. Childhood 'do not bother God with prayers' (via S3) is retrospective and not a system. Rejected."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "Deepen D1 re-check (S3 full Araos page; S6 German line; S7–S10): 1951 letter states trust in God but nothing on where God is (immanent vs transcendent locus). Single private letter stays under 0.5 unless a scholar backs a scored locus reading (§3); Araos affirms belief, not locus; Zawisza cryptotheology / withdrawn-God (tzimtzum) and Denktagebuch God-man-men politics are scholarly reconstruction or speculative notebook, not a confession of locus. Childhood Vogelstein disbelief (S9) and Denktagebuch 'thought about God … never reflected on God' (S3) do not place God. Named alternatives not scored.", note: "Evidence bears on God-belief but not on A_locus at ≥0.5 (P19)."}
    B_cause: {value: UNKNOWN, how_known: "Deepen D1: not a scientist under P30/P33 — lasting contributions are political philosophy (totalitarianism, vita activa, banality of evil, Life of the Mind), not theories or results about physical or natural systems. For a non-scientist, B needs an explicit remark on the order of nature (P16). None found in SEP, Britannica, Wikipedia, JWA, Young-Bruehl childhood chapters, Araos, or Zawisza Cryptotheology (S1–S10). Human Condition earth/labor/natality is anthropological-political, not a scored account of natural law vs exception. Zawisza's 'de-divinization of nature' is about Augustine reception / cryptotheology, not her B statement."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing of hers on judgement, reward or afterlife scored from S1–S10 (P19)."}
    D_authority: {value: UNKNOWN, how_known: "The 1951 letter says traditional religion cannot ground (political) law — about politics, not revelation against observation. Nothing else read that scores D (P19)."}
    E_scope: {value: UNKNOWN, how_known: "Not a scientist; no statement on same laws everywhere (P7/P19)."}
  mid_basin: {value: UNKNOWN, how_known: "B_cause is UNKNOWN, which takes precedence for the P4 test (§6, P19); A is also BELOW_THRESHOLD."}
  statements:
    - text: "Abro mi camino en la vida con una especie de confianza (¿infantil? Porque es incuestionada) en Dios"
      cites: [{source: S5, locator: "letter of 4 March 1951 (Kimber English / Piper German pages unread this pass)"}, {source: S3, locator: "opening; Spanish quotation of the letter"}]
      date: "1951-03-04"
      context: "Letter to Karl Jaspers, answering whether Yahweh had not vanished too far from view, after he received The Origins of Totalitarianism. Araos: trust almost childlike; does not resolve the philosophical problem but allows happiness."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Spanish rendering as printed in Araos (Humanitas web text, opened in full D1). Primary check still pending against Kimber Correspondence 1926–1969 (letter of 4 March 1951; search indexes place English on pp. 165–168, often p. 166 — pages not opened). German 'trust' clause not seen in S6 (S6 starts after it). Scores belief, not locus — keeps A BELOW_THRESHOLD."
    - text: "Alle überlieferte Religion, jüdische oder christliche, sagt mir als solche gar nichts mehr"
      cites: [{source: S5, locator: "letter of 4 March 1951"}, {source: S6, locator: "German quotation of the letter"}]
      date: "1951-03-04"
      context: "Same letter to Jaspers. Supporting context: all traditional religion, Jewish or Christian, means nothing to her any more as such."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "German original as quoted on diemorgengab.at (TzN, June 2021); not checked against the printed Briefwechsel; page not verified. Supporting context only; scores nothing on locus."
    - text: "Desde mis siete años propiamente he pensado siempre en Dios, pero nunca he reflexionado sobre Dios"
      cites: [{source: S3, locator: "Denktagebuch / Diario Filosófico, May 1965 quotation"}]
      date: "1965-05"
      context: "Denktagebuch entry (via Araos). Retrospective: thinking about God from age seven without reflecting on God. Supporting context for lifelong God-thought, not a locus claim."
      axes: [A_locus]
      kind: "other"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Spanish via Araos; printed Denktagebuch (Ludz/Nordmann) unread cover-to-cover. Does not place God; does not lift A."
  changes_over_life:
    - {value: "Childhood: Vogelstein episode of declaring she no longer believed in God (Young-Bruehl); adult 1951 letter states unquestioned trust in God while rejecting traditional religion as such.", certainty: 0.5, cites: [{source: S9, locator: "dejado de creer"}, {source: S3, locator: "1951 letter quotation"}], how_known: "Childhood vs adult private letter; neither yields a scored adult A locus. Recorded under P20 as change context only."}
  coder_notes: "Deepen D1: A stays BELOW_THRESHOLD (trust without locus; single private letter; cryptotheology does not score locus). B stays UNKNOWN (not scientist; no nature-order statement). Chart still unplotted. Kimber English pages and full Denktagebuch / Young-Bruehl English still open. Lane B (geometric form) separate from Lane A axis scores."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "German-Jewish (assimilated; Königsberg / Russian-Jewish entrepreneurial grandparents)", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "Family"}, {source: S8, locator: "Russian-Jewish homes"}], how_known: "SEP + Wikipedia + JWA."}
  religious_heritage_by_birth: {value: "Jewish (Reform grandparents; parents non-religious; Vogelstein religious instruction)", certainty: 1.0, cites: [{source: S7, locator: "Reform synagogue; Vogelstein"}, {source: S9, locator: "padres … no … religiosos; sinagoga; Vogelstein"}], how_known: "Wikipedia + Young-Bruehl. Context only — not primary_system or A (P19)."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "No Jewish initiation rite named in S1–S10; Christian catechesis was school-mandatory for pupils (S9) — heritage context only."}
  childhood_catechism: {value: "Vogelstein Jewish religious instruction from ~age 7 (only religious formation she ever received, per YB); mandatory Christian catechesis at school; Christian servant's practices in household", certainty: 0.7, cites: [{source: S9, locator: "única formación … religiosa … catequesis cristiana … sirvienta cristiana"}], how_known: "Young-Bruehl (Spanish). Context only."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1951–1975", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "1951 to 1975, first to last listed lasting contribution; the last is posthumous and dated by death (P29, P30), so 0.7."}
  age_at_first_lasting_contribution: {value: 45, certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "opening"}], how_known: "1951 − 1906 = 45 (P30)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No scored statement at the LIO-type-view bar (P27); A BELOW_THRESHOLD, B UNKNOWN."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S3, locator: "opening paragraph"}, {source: S5, locator: "letter of 4 March 1951"}], how_known: "Only the 1951 letter and Denktagebuch God-thought, unscored for locus/nature."}
  worldview_during_major_work: {value: BELOW_THRESHOLD, how_known: "The 1951 letter falls in the span but is below 0.5 for system and A.", note: "S3, S5."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Philosophy doctorate; Greek/Latin and Kant early; no documented Euclid-style proof exposure read.", certainty: 0.5, cites: [{source: S1, locator: "§1"}, {source: S7, locator: "Early education"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "§1"}], how_known: "Nothing that pins acquisition timing."}
  circle_present: {value: "unclear", rationale: "Trust in God stated; nothing on God and the order of nature.", certainty: 0.5, cites: [{source: S3, locator: "opening paragraph"}], how_known: "Coder's reading."}
  reading: "No reading possible while A is BELOW_THRESHOLD and B is UNKNOWN."
  notes: "Lane B is separate from Lane A axis scores (P47–P50 framing)."

institutions:
  - {value: "University of Chicago", role: professor, years: "1963–1967", kind: university, certainty: 0.7, cites: [{source: S2, locator: "third paragraph"}, {source: S7, locator: "Teaching"}], how_known: "Britannica + Wikipedia."}
  - {value: "New School for Social Research", role: professor, years: "1967–1975", kind: university, certainty: 0.7, cites: [{source: S2, locator: "third paragraph"}, {source: S1, locator: "§1"}, {source: S7, locator: "Teaching"}], how_known: "Britannica + SEP + Wikipedia."}
collaborators:
  - {value: "Karl Jaspers", relation: teacher, note: "dissertation supervisor and lifelong correspondent", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "second paragraph"}], how_known: "Two sources."}
  - {value: "Martin Heidegger", relation: teacher, note: "teacher at Marburg; relationship", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "second paragraph"}], how_known: "Two sources."}
  - {value: "Heinrich Blücher", relation: family, note: "second husband; political interlocutor", certainty: 0.7, cites: [{source: S7, locator: "Blücher"}, {source: S8, locator: "married Blücher"}], how_known: "Wikipedia + JWA."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 34"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Doctorate year: SEP/Wikipedia 1929 (dissertation); Britannica has also given 1928 (degree)."
    - "Arendt 1951 letter English Kimber pages unread; Spanish via Araos full page; German religion-line via S6."
    - "Young-Bruehl read in Spanish elboomeran/Paidós PDF, not English Yale UP pages."
  open_questions:
    - "Open Kimber Correspondence (1992) letter of 4 March 1951 at the cited pages (~165–168) for English primary wording and exact page."
    - "Read Denktagebuch (Ludz/Nordmann) cover-to-cover for any locus or nature-order statement beyond Araos excerpts."
    - "English Young-Bruehl For Love of the World for page-anchored Vogelstein episode."
    - "Ruling question remains: can stated 'trust in God' with no tradition, locus or revelation statement support any code or A value? Coder's call for now: no (BELOW_THRESHOLD)."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Tatjana Tömmel and Maurizio Passerin d'Entrèves"
    year: 2024
    citation: "Tömmel, Tatjana, and Maurizio Passerin d'Entrèves. \"Hannah Arendt.\" Stanford Encyclopedia of Philosophy, first published 27 July 2006, substantive revision 12 February 2024. https://plato.stanford.edu/entries/arendt/."
    url: "https://plato.stanford.edu/entries/arendt/"
    accessed: 2026-10-24
    reliability_note: "Peer-reviewed reference article."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: tertiary
    kind: encyclopedia
    author: "Britannica Editors (revised by Mindy Johnston)"
    citation: "Britannica Editors. \"Hannah Arendt.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Hannah-Arendt."
    url: "https://www.britannica.com/biography/Hannah-Arendt"
    accessed: 2026-10-24
    reliability_note: "Article body only; the AI 'Top Questions' box is not used. Direct fetch hit a JS challenge this pass; prior create-pass body and Wikipedia dual-source used for dates."
    source_quality: "reference entry"
    used_for: [basics, contribution, childhood, heritage, timing, institutions, collaborators]
  - id: S3
    type: secondary
    kind: journal article
    author: "Josefina Araos"
    citation: "Araos, Josefina. \"Esbozos sobre la presencia de Dios en Hannah Arendt.\" Humanitas (Pontificia Universidad Católica de Chile), no. 109 (Humanitas 2025, CIX, pp. 36–43)."
    url: "https://humanitas.cl/revistas/humanitas-109/esbozos-sobre-la-presencia-de-dios-en-hannah-arendt/"
    accessed: 2026-10-24
    reliability_note: "Scholarly essay; full web text opened D1 (Spanish quotation of 1951 letter; Denktagebuch May 1965; Young-Bruehl Vogelstein summary). PDF image path previously 404/HTML; web article used."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview, timing, lane_b, childhood]
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
    kind: scholarly edition
    author: "Hannah Arendt and Karl Jaspers"
    citation: "Arendt, Hannah, and Karl Jaspers. Briefwechsel 1926–1969. Ed. Lotte Köhler and Hans Saner. Munich: Piper, 1985. English: Correspondence 1926–1969, trans. Robert and Rita Kimber. New York: Harcourt Brace Jovanovich, 1992. Letter of 4 March 1951."
    accessed: 2026-10-24
    reliability_note: "Not read directly this pass; cited by letter date. Wording known through S3 (Spanish, full Araos page) and S6 (German excerpt). Search indexes place Kimber English on pp. 165–168."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview]
  - id: S6
    type: secondary
    kind: other
    author: "diemorgengab.at"
    citation: "diemorgengab.at, TzN (Juni 2021), quoting Arendt's letter to Jaspers of 4 March 1951 in German."
    accessed: 2026-10-15
    reliability_note: "Unofficial web quotation; excerpt starts after the 'trust in God' clause; religion-line used as supporting German."
    source_quality: "unofficial web copy"
    used_for: [worldview]
  - id: S7
    type: secondary
    kind: encyclopedia
    author: "Wikipedia contributors"
    year: 2026
    citation: "Wikipedia. \"Hannah Arendt.\" https://en.wikipedia.org/wiki/Hannah_Arendt."
    url: "https://en.wikipedia.org/wiki/Hannah_Arendt"
    accessed: 2026-10-24
    reliability_note: "Dual-source bio for childhood (Linden; parents non-religious; Vogelstein; schools). Cross-checked with JWA and Young-Bruehl."
    source_quality: "other"
    used_for: [identity, basics, childhood, heritage, institutions, collaborators]
  - id: S8
    type: secondary
    kind: encyclopedia
    author: "Stephen J. Whitfield"
    citation: "Whitfield, Stephen J. \"Hannah Arendt.\" Shalvi/Hyman Encyclopedia of Jewish Women (Jewish Women's Archive), 27 February 2009 (updated). https://jwa.org/encyclopedia/article/arendt-hannah."
    url: "https://jwa.org/encyclopedia/article/arendt-hannah"
    accessed: 2026-10-24
    reliability_note: "Signed encyclopedia article; Early Life for parents and Beerwald household."
    source_quality: "reference entry"
    used_for: [identity, basics, childhood, heritage, collaborators]
  - id: S9
    type: secondary
    kind: scholarly book
    author: "Elisabeth Young-Bruehl"
    citation: "Young-Bruehl, Elisabeth. Hannah Arendt: For Love of the World. New Haven: Yale University Press, 1982. Spanish edition PDF via elboomeran.com (Paidós pagination around pp. 71–72 for Vogelstein / non-religious parents)."
    url: "https://www.elboomeran.com/upload/ficheros/obras/hannah_arendt.pdf"
    accessed: 2026-10-24
    reliability_note: "Standard scholarly biography; English Yale pages not opened (IA print-disabled); Spanish Paidós/elboomeran PDF used for childhood religion block."
    source_quality: "scholarly edition or monograph"
    used_for: [childhood, heritage, worldview]
  - id: S10
    type: secondary
    kind: journal article
    author: "Rafał Zawisza"
    year: 2018
    citation: "Zawisza, Rafał. \"Thank God We Are Creatures: Hannah Arendt's Cryptotheology.\" Religions 9(11): 371. https://doi.org/10.3390/rel9110371."
    url: "https://www.mdpi.com/2077-1444/9/11/371"
    accessed: 2026-10-24
    reliability_note: "Peer-reviewed OA; scholarly reconstruction of cryptotheology / Augustine / withdrawn God. Used as negative check — does not supply a scored personal A locus or B nature-order statement."
    source_quality: "scholarly reconstruction"
    used_for: [worldview]
---

# Hannah Arendt

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Hannah Arendt (1906–1975), German-born American political philosopher, author of *The Origins of Totalitarianism*, *The Human Condition* and *Eichmann in Jerusalem* [S1, S2, S7]. Deepen D1: the only adult worldview evidence that bears on God is still one private letter to Jaspers (4 March 1951) [S5], read in Spanish via Araos [S3] and a German excerpt [S6], plus Denktagebuch God-thought via Araos and cryptotheology scholarship [S10] that does not score locus. Draft: primary_system and A BELOW_THRESHOLD; B, C, D, E UNKNOWN; mid_basin UNKNOWN.

## Life and work

Studied with Heidegger and Jaspers; fled Germany in 1933 and France in 1941; taught in Chicago and at the New School [S1, S2, S7].

## Contribution and impact

*Origins* (1951), *The Human Condition* (1958), *Eichmann in Jerusalem* (1963), *The Life of the Mind* (unfinished at death) [S1, S2].

## Childhood and education

Assimilated German-Jewish family; parents non-religious Social Democrats; Reform synagogue with grandparents; Vogelstein religious instruction from about age seven [S7, S9]. Linden birth; Königsberg childhood; Gymnasium then Marburg/Freiburg/Heidelberg; doctorate on Augustine [S1, S7]. Childhood Vogelstein declaration of no longer believing in God [S9] is heritage/childhood, not adult A.

## Adult working worldview

To Jaspers in 1951 she wrote of a trust in God (Spanish via Araos: 'confianza … en Dios'), and said traditional religion, Jewish or Christian, no longer meant anything to her as such [S5, S3, S6]. Denktagebuch (May 1965, via Araos): she had thought about God since age seven but never reflected on God [S3]. One private letter naming no locus, plus scholarly cryptotheology that does not confess locus: A stays BELOW_THRESHOLD. Not a scientist; no nature-order statement: B stays UNKNOWN.

## Heritage (context only)

German-Jewish; Reform grandparents; non-religious parents; Vogelstein instruction [S1, S7, S9].

## Timing

First lasting contribution 1951, at 45 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Unclear geometric form and circle [S1, S7].

## Open questions

- Kimber English pages for the 1951 letter; full Denktagebuch; English Young-Bruehl pages.

## Research log

- 2026-10-15: Read SEP and Britannica; web search found the 1951 Jaspers letter via Araos (Spanish). The Araos page and PDF did not load directly; excerpts only.
- 2026-10-15: fallacy_catalog audit of 64605bd (HOLD): primary cite moved to the Briefwechsel / Kimber (S5, by date); German line added from S6; Araos kept as secondary pointer. Code stays BELOW_THRESHOLD.
- 2026-10-24: Deepen D1 (queue #34). Araos Humanitas web text opened in full; Wikipedia, JWA Whitfield, Young-Bruehl Spanish PDF, Zawisza Cryptotheology PDF. P47 on all sources. Childhood/heritage filled. A BELOW→BELOW; B UNKNOWN→UNKNOWN. Chart-moving NO. No fallacy_catalog (Jason).
