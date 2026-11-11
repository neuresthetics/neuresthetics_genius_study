---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to 20c_late. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (catch-up 4/13; F3 rank 138). Goals: firm B; any A; do not force plot. Opened WINA Dec 2016 (S5, Pollak); Principia 16 Mar 2016 (S6); Mètode 18 Jun 2018 (S7); Wikipedia EN dual bio (S8, P50). Native name עדה יונת; birth name Ada Esther Lifshitz. A stays BELOW_THRESHOLD (P20): SINC 2010 + WINA 2016 distance science from biblical origin accounts and joke about Vatican/Darwin 'miracles', but no place/deny of a personal God and no explicit AGNOS suspension. primary_system stays BELOW_THRESHOLD (leads AGNOS, JUDA). B 3 stays @0.5 alt 4: basis inference_from_work → recorded_interview (Mètode: 'this is the law in life, in chemistry and in the world: the structure defines the function'; Nobel bio S2 principles of nature / mechanics guiding the process); support single → corroborated (S7+S2; P48). Certainty held at 0.5 under P16 Hilbert / P35 (no exception / no-exception claim). mid_basin BELOW_THRESHOLD. Chart-moving NO (A BELOW; B faded @0.5). Deceased 31 Aug 2026 (not living). P47 source_quality on S1–S8. No fallacy_catalog. No figures/. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z1 audit fixes (blind audit /workspace/genius_study_audit/gs_8813a47_Z1/run1/): Z1-21: context line rewritten; 'Desconozco' is the interviewer's, not hers. No score changed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z1, order P32: F 3, rank 138). Basics from Britannica (Kara Rogers, signed; death 31 August 2026, also in the Nobel Foundation's addendum) and her Nobel autobiography (Les Prix Nobel 2009). Own voice on religion: SINC interview (Enrique Sacristán, 5 Oct 2010, Spanish): asked whether science and religious faith are compatible, 'La respuesta no es nada que pueda saber. Pienso que la definición de Dios es algo tan… (silencio) por encima de mí. Así que no puedo responder.' A scientist (P30: ribosome structures). Span 1980–2001 at 0.7. primary_system BELOW_THRESHOLD (leads AGNOS, JUDA); A BELOW_THRESHOLD; B 3 at 0.5, alt 4 (P35); C, D UNKNOWN; E BELOW_THRESHOLD (P19); mid_basin BELOW_THRESHOLD. Not plotted (no A). Draft, not reviewed."}

identity:
  id: yonath-ada
  display_name: "Ada Yonath"
  roster:
    canonical_name: "Ada Yonath"
    rank: 138
    F: 3
    models: [DeepSeek, Gemini, Grok]
    band: "core (3–4)"
    status: provisional
    field: chemistry
    field_bucket: chemistry
  full_name: {value: "Ada E. Yonath", certainty: 0.7, cites: [{source: S2, locator: "title"}], how_known: "Nobel Foundation page title; the middle name is not expanded in the sources read (Wikipedia gives Esther via birth name)."}
  native_name: {value: "עדה יונת", certainty: 0.7, cites: [{source: S8, locator: "infobox native_name"}], how_known: "Wikipedia Hebrew (P50)."}
  aliases:
    - {name: "Yonath-Ada", kind: "roster alias"}
    - {name: "Ada Esther Lifshitz", kind: "birth name"}
    - {name: "Ada Esther Yonath", kind: "other"}

basics:
  birth:
    date: {value: "1939-06-22", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "Quick Facts; opening"}, {source: S2, locator: "paragraph 1 ('born in Jerusalem in 1939')"}], how_known: "Britannica gives the day; her autobiography gives the year and place."}
    place: {value: "Jerusalem", modern_name: "Jerusalem", polity_then: "Mandatory Palestine (British mandate)", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S2, locator: "paragraph 1"}], how_known: "Britannica and her own autobiography agree; polity_then is the coder's."}
  death:
    date: {value: "2026-08-31", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Quick Facts; opening"}, {source: S2, locator: "closing addendum ('Ada Yonath died on 31 August 2026')"}, {source: S8, locator: "Personal life and death"}], how_known: "Britannica, the Nobel Foundation, and Wikipedia agree."}
    place: {value: UNKNOWN, how_known: "Not stated in the sources read."}
  first_lasting_contribution_year: {value: 1980, certainty: 0.7, cites: [{source: S1, locator: "paragraph 4 ('In 1980 Yonath became the first person to determine the three-dimensional ... arrangement of a large ribosomal subunit')"}, {source: S2, locator: "paragraph 8 ('At the start of the 1980s ... we created the first ribosome micro crystals')"}], how_known: "Britannica dates the first large-subunit result to 1980; her own account says 'the start of the 1980s', which agrees but is less exact."}
  era_bucket: {value: "1950 on", certainty: 1.0, cites: [{source: S1, locator: "paragraph 4"}], how_known: "From 1980 (P2); every candidate year falls in the bucket."}
  region_of_birth: {value: "Middle East and North Africa", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}], how_known: "Israel (Western Asia → MENA, P3)."}
  region_of_work: {value: "Middle East and North Africa", certainty: 0.7, cites: [{source: S1, locator: "paragraph 3"}], how_known: "Weizmann Institute, Rehovot; also the Max Planck unit in Hamburg (1986–2004)."}
  sex_as_recorded: {value: "female", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English", "Hebrew"], certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading (publishes in English; Israeli institution)."}
  occupations: {value: ["protein crystallographer", "director, Kimmelman Center (Weizmann Institute)"], certainty: 0.7, cites: [{source: S1, locator: "paragraphs 1, 3"}], how_known: "Britannica."}

contribution:
  era_bucket: 20c_late
  fields: {value: ["X-ray crystallography", "structural biology", "ribosome structure"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "First three-dimensional arrangement of a large ribosomal subunit (Bacillus stearothermophilus)", year: 1980, kind: discovery, lasting: "began the ribosome crystallography that led to the 2009 Nobel Prize (S1)", certainty: 0.7, cites: [{source: S1, locator: "paragraph 4"}], how_known: "Britannica."}
    - {value: "Cryo-bio-crystallography (rapid cooling of protein crystals)", year: UNKNOWN, kind: method, lasting: "'techniques that are today widely used in structural biology labs around the world' (S2)", certainty: 0.7, cites: [{source: S1, locator: "paragraph 5"}, {source: S2, locator: "paragraph 9"}], how_known: "Britannica (undated) and her own account (between the mid-1980s and the late 1990s)."}
    - {value: "First complete three-dimensional structures of both bacterial ribosomal subunits", year: 2000, kind: discovery, lasting: "basis of the 2009 Nobel Prize in Chemistry (S1)", certainty: 0.7, cites: [{source: S2, locator: "paragraph 10 ('in 2000 and 2001, we published')"}, {source: S1, locator: "paragraph 5 (small subunit at 3.3 Å)"}], how_known: "Her own account; range 2000–2001, start year (P12)."}
    - {value: "Binding pockets of antibiotics on the bacterial ribosome", year: 2001, kind: discovery, lasting: "'we have revealed the means of action of almost all of the antibiotics that target the ribosome' (S2)", certainty: 0.7, cites: [{source: S2, locator: "paragraph 11 ('published in Nature, in 2001')"}, {source: S1, locator: "paragraph 5"}], how_known: "Her own account; latest dated lasting item, so it ends the span (P30 addendum)."}
  evidence_of_impact:
    - {value: "Nobel Prize in Chemistry 2009 (with Ramakrishnan and Steitz)", kind: "honours in lifetime", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "page"}], how_known: "Britannica and the Nobel Foundation."}
  major_works: []
  honours:
    - {value: "Louisa Gross Horwitz Prize", year: 2005, certainty: 0.7, cites: [{source: S1, locator: "final paragraph"}], how_known: "Britannica."}
    - {value: "Nobel Prize in Chemistry", year: 2009, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "page"}], how_known: "Two sources."}
  definition_fit: {value: "clearly meets", rationale: "Ribosome structure work recognised by the 2009 Nobel Prize (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Jewish (religious families)", certainty: 0.7, cites: [{source: S2, locator: "paragraph 2 ('My parents were raised in religious families, being educated mainly in Judaism (my father)')"}], how_known: "Her own autobiography."}
  family_religious_practice: {value: "The neighbourhood schools followed her parents' religious principles", certainty: 0.7, cites: [{source: S2, locator: "paragraph 2"}], how_known: "Her autobiography: 'All of the schools in my immediate neighborhood were based on the same principles as those of my parents'."}
  parents_and_household:
    - {value: "Father educated mainly in Judaism, often hospitalized; died when she was 11", role: father, certainty: 0.7, cites: [{source: S2, locator: "paragraphs 2–3"}], how_known: "Her own account."}
    - {value: "Mother, who moved the family to Tel Aviv a year later", role: mother, certainty: 0.7, cites: [{source: S2, locator: "paragraph 3"}], how_known: "Her own account."}
  household_circumstances: {value: "Poor; a rented four-room apartment shared with two other families", certainty: 0.7, cites: [{source: S2, locator: "paragraph 1"}], how_known: "Her own account."}
  schooling:
    - {value: "Beit Hakerem, 'a very prestigious secular grammar school', Jerusalem", stage: "grammar or secondary school", run_by: "state or municipal", years: "to c. 1951", certainty: 0.7, cites: [{source: S2, locator: "paragraph 2"}], how_known: "Her own account; run_by the coder's reading."}
    - {value: "Hebrew University of Jerusalem (BSc chemistry 1962, MSc biochemistry 1964)", stage: university, run_by: "state or municipal", years: "to 1964", certainty: 0.7, cites: [{source: S1, locator: "paragraph 2"}], how_known: "Britannica."}
    - {value: "Weizmann Institute of Science (PhD 1968)", stage: university, run_by: private, years: "to 1968", certainty: 0.7, cites: [{source: S1, locator: "paragraph 2"}], how_known: "Britannica."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure:
    - {value: "At five, a balcony-measuring 'experiment' with stacked furniture", certainty: 0.7, cites: [{source: S2, locator: "paragraph 1"}], how_known: "Her own account."}
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["Hebrew"], certainty: 0.5, cites: [{source: S2, locator: "paragraph 1"}], how_known: "Coder's reading."}
  notable_events:
    - {value: "Father's death when she was 11", year: 1950, certainty: 0.7, cites: [{source: S2, locator: "paragraph 3"}], how_known: "Her own account; year is 1939 + 11, the coder's."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1980–2001", certainty: 0.7, cites: [{source: S1, locator: "paragraph 4"}, {source: S2, locator: "paragraphs 10–11"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "(interview) Can't say whether science and religious faith are compatible: definition of God 'above me' (SINC 2010). WINA 2016: religious people 'don't think about the origin of life' because 'it is all in the Bible'; some scientists are religious and some religious people fight science; Vatican/Darwin anecdote ending 'Es geschehen noch Wunder!' (ironic).", certainty: 0.5, cites: [{source: S3, locator: "question on science and faith"}, {source: S5, locator: "Glauben und Wissen / Ursprünge des Lebens"}], how_known: "(interview) Two recorded interviews after the span (P20), so 0.5."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "(interview) Leads AGNOS and JUDA. SINC 2010: she has asked herself 'many times' whether science and faith are compatible, 'the answer is nothing I can know', 'the definition of God is something so ... above me' (S3). WINA 2016 distances biblical origin accounts from scientific inquiry and jokes about Church miracles (S5), but still does not state an explicit suspension of belief in God (AGNOS needs one) nor a profession of Judaism (JUDA). Family was religious, school secular (S2). Below 0.5."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: AGNOS, reason: "'La respuesta no es nada que pueda saber' (S3); WINA distances religion from origins science (S5). Against: about compatibility / God's definition / biblical vs scientific origins, not a stated suspension of belief in God."}
    - {code: JUDA, reason: "Religious Jewish family (S2). Against: heritage, not her view; nothing read professes it."}
    - {code: ATHE, reason: "Rejected: nothing read denies God; WINA joke about miracles is irony about the Church, not a denial."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "(interview) The definition of God is 'above me' (S3, 2010); WINA 2016 does not place or deny a personal intervening God (S5). No locus stated (P20 agnostic rule)."}
    B_cause:
      value: 3
      basis: recorded_interview
      certainty: 0.5
      support: corroborated
      cites: [{source: S7, locator: "structure defines the function"}, {source: S2, locator: "paragraphs 1, 5 ('principles of the nature'; 'mechanics guiding the process')"}, {source: S6, locator: "'bases of natural processes'"}]
      rationale: "Scored on her account of nature (P6). Own-voice (Mètode 2018): structure must be found because 'this is the law in life, in chemistry and in the world: the structure defines the function' (S7). Nobel autobiography: childhood desire to understand 'the principles of the nature around me' and aim 'to reveal the mechanics guiding the process' of protein biosynthesis (S2). Principia 2016: crystallography is 'the only way to understand the bases of natural processes' (S6). Lawful-order remarks without a stated exception or no-exception claim → B 3 at 0.5, alternative 4 (P16 Hilbert addendum / P35). Scientist (P30)."
      how_known: "(interview) Mètode 2018 (S7) plus written autobiography (S2); independent source ids → corroborated (P48). Certainty held at 0.5: lawful-order remark without a stated no-exception or limited-exception claim (P16 Hilbert / P35). After span for the interview (P20)."
      alternatives:
        - {value: 4, note: "P16 / P35 alternative: if an own-voice statement showed exceptionless law.", cites: [{source: S7, locator: "structure defines the function"}, {source: S2, locator: "paragraphs 1, 5"}]}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read (P19)."}
    D_authority: {value: UNKNOWN, how_known: "Nothing scored on revelation against observation (P19). WINA's biblical-origins vs science contrast (S5) is a lead for D 3/4 but does not state which authority decides which domain; left unscored."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Not scored from working science alone (P19). Her remarks that the ribosome core 'se conserva en todos los ribosomas, desde los de una bacteria hasta los de un elefante o los que hay en los humanos' (S3) and that the protoribosome is in bacteria, lions, elephants (S7) are findings about biology, not statements on favour in the world's order (P7)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A BELOW_THRESHOLD and B only at 0.5 (P19 / P4). Deepen D1 did not darken B past 0.5."}
  statements:
    - text: "Esta pregunta me la he hecho yo misma muchas veces. La respuesta no es nada que pueda saber. Pienso que la definición de Dios es algo tan… (silencio) por encima de mí. Así que no puedo responder."
      cites: [{source: S3, locator: "question on science and faith"}]
      date: "2010-10-05"
      context: "SINC interview at the Passion for Knowledge festival, San Sebastián; the interviewer, saying he does not know ('Desconozco si usted es judía y cree en Dios'), asks instead whether being a scientist and having religious faith are compatible."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "newspaper interview"
      verified_on: 2026-10-19
      note: "Agency's published text in Spanish; the language spoken is not stated. After the span (P20). verified_against corrected from 'primary transcription' on deepen re-check (published newspaper/agency interview)."
    - text: "Die Religiösen denken nicht über den Ursprung des Lebens nach. Es steht alles in der Bibel, man braucht nicht darüber nachzudenken. Es gibt einige Wissenschaftler, die religiös sind, und es gibt religiöse Menschen, die die Wissenschaft bekämpfen, wo immer sie können. … Als ich später Mitglied der Päpstlichen Akademie wurde, sagte der Papst in seiner Ansprache: Wir wissen nun, dass die Kirche sich mit der Evolution anfreunden kann. Es geschehen noch Wunder!"
      cites: [{source: S5, locator: "Glauben und Wissen / Ursprünge des Lebens"}]
      date: "2016-12"
      context: "WINA (Vienna Jewish city magazine) interview with Anita Pollak after a Vienna talk on biochemical origins of life; interviewer pressed philosophical and religious aspects she had left out."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "newspaper interview"
      verified_on: 2026-10-24
      note: "Published German interview text. Distances biblical origin accounts from scientific inquiry; ironic 'miracles' about the Church accepting evolution. Does not place or deny God. After the span (P20)."
    - text: "Ribosomes perform, in my opinion, one of the key vital functions of life, and I wanted to understand how they did it. And for understanding how, I needed to find their structure because this is the law in life, in chemistry and in the world: the structure defines the function."
      cites: [{source: S7, locator: "What brought you to the study of ribosomes?"}]
      date: "2018-06-18"
      context: "Mètode interview (University of Valencia), Susanna Ligero and Lucía Sapiña, on Darwin Day / Biology Studies anniversary visit."
      axes: [B_cause]
      kind: "recorded interview"
      verified_against: "newspaper interview"
      verified_on: 2026-10-24
      note: "Published interview text (English). Lawful-order remark about life, chemistry and the world; no exception / no-exception claim. After the span (P20)."
    - text: "My memories from my childhood are centered on my father's medical conditions alongside my constant desire to understand the principles of the nature around me."
      cites: [{source: S2, locator: "paragraph 1"}]
      date: "2010"
      context: "Nobel autobiography (Les Prix Nobel 2009), opening paragraph."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Own published autobiography on the Nobel Foundation site. Principles-of-nature line; corroborates S7 for B (P48)."
  changes_over_life: []
  coder_notes: "Deepen D1 (2026-10-24). B lifted to recorded_interview @0.5 corroborated via Mètode 2018 (S7) + Nobel bio (S2); Principia 2016 (S6) supports. P16 Hilbert / P35 hold certainty at 0.5. A stays BELOW (P20): SINC + WINA give no place/deny of God. primary BELOW (AGNOS lead strengthened by WINA biblical-origins distance, still not explicit suspension). Deceased 31 Aug 2026 — catch-up brief said living; corrected from sources. Chart-moving NO. No fallacy_catalog. No figures/."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Israeli Jewish", certainty: 0.7, cites: [{source: S2, locator: "paragraphs 1–2"}], how_known: "Her autobiography."}
  religious_heritage_by_birth: {value: "Jewish (religious families)", certainty: 0.7, cites: [{source: S2, locator: "paragraph 2"}], how_known: "Her autobiography."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated; she attended a secular school (S2)."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1980–2001", certainty: 0.7, cites: [{source: S1, locator: "paragraph 4"}, {source: S2, locator: "paragraphs 10–11"}], how_known: "First large-subunit result (1980) to the antibiotic-binding paper (2001) (P29, P30)."}
  age_at_first_lasting_contribution: {value: 41, certainty: 0.7, cites: [{source: S1, locator: "Quick Facts; paragraph 4"}], how_known: "1980 − 1939 = 41 (P30)."}
  first_evidence_of_lio_type_views: {value: "2018 (Mètode law-in-the-world remark), after the span", certainty: 0.5, cites: [{source: S7, locator: "structure defines the function"}], how_known: "Own-voice B remark is after the span; earlier B rested on working science only (§8)."}
  lio_views_relative_to_major_work: {value: "after major work", certainty: 0.5, cites: [{source: S7, locator: "structure defines the function"}], how_known: "Scored own-voice B is 2018; span ends 2001."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "primary_system BELOW; A BELOW; scored B own-voice is after span; working-science B at 0.5 does not alone set the working worldview."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S2, locator: "text"}], how_known: "Not assessed."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "text"}], how_known: "Not assessed."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S3, locator: "text"}], how_known: "Not assessed."}
  reading: "Not assessed."
  notes: ""

institutions:
  - {value: "Weizmann Institute of Science", role: "scientist to director of the Mazer and Kimmelman centers", years: "1970–2026", kind: "research institute", certainty: 0.7, cites: [{source: S1, locator: "paragraph 3"}], how_known: "Britannica; end year the coder's (her death)."}
  - {value: "Max Planck Research Unit for Ribosomal Structure, Hamburg", role: "head", years: "1986–2004", kind: "research institute", certainty: 0.7, cites: [{source: S1, locator: "paragraph 3"}], how_known: "Britannica."}
collaborators:
  - {value: "Heinz-Günter Wittmann", relation: collaborator, note: "Max Planck Institute for Molecular Genetics, Berlin; co-initiated the ribosome project", certainty: 0.7, cites: [{source: S2, locator: "paragraph 6"}], how_known: "Her own account ('Prof. H.G. Wittmann'); the first name is the coder's expansion."}

review:
  roster_status_reason: {value: "Provisional in v8 (F 3).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 138"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Britannica says 'three-dimensional atomic arrangement' for the 1980 work; her own account speaks of the first micro crystals at the start of the 1980s and the high-resolution structures only in 2000–2001. The year 1980 is kept from Britannica."
    - "Own-voice religion statements are post-span interviews (SINC 2010 Spanish; WINA 2016 German)."
    - "Catch-up brief said living; she died 31 August 2026 (S1, S2, S8)."
  open_questions:
    - "Hebrew/Israeli long-form interview that places or denies God, or states AGNOS suspension explicitly."
    - "Any own-voice no-exception claim that would lift B certainty past 0.5 (P16 / P35)."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Kara Rogers"
    citation: "Rogers, Kara. \"Ada Yonath.\" Encyclopaedia Britannica (14 Oct 2026). https://www.britannica.com/biography/Ada-Yonath. Read live 2026-10-19; re-checked 2026-10-24."
    url: "https://www.britannica.com/biography/Ada-Yonath"
    accessed: 2026-10-24
    reliability_note: "Signed article; body cited, AI question boxes not cited (P26)."
    source_quality: "reference entry"
    used_for: [basics, contribution, childhood, worldview, timing, institutions]
  - id: S2
    type: primary
    kind: other
    author: "Ada E. Yonath"
    citation: "Yonath, Ada E. \"Biographical.\" In Les Prix Nobel. The Nobel Prizes 2009, ed. Karl Grandin. Stockholm: Nobel Foundation, 2010. https://www.nobelprize.org/prizes/chemistry/2009/yonath/biographical/"
    url: "https://www.nobelprize.org/prizes/chemistry/2009/yonath/biographical/"
    accessed: 2026-10-24
    reliability_note: "Her own autobiography, on the publisher's official site (Nobel Foundation), with a later death addendum."
    source_quality: "primary / own words"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, collaborators]
  - id: S3
    type: primary
    kind: other
    author: "Ada Yonath, interviewed by Enrique Sacristán (SINC)"
    citation: "Sacristán, Enrique. \"Ada Yonath: La ciencia es la fuerza para el futuro.\" Tendencias21 / SINC, 5 Oct 2010. https://www.tendencias21.es/Ada-Yonath-La-ciencia-es-la-fuerza-para-el-futuro_a4918.html"
    url: "https://www.tendencias21.es/Ada-Yonath-La-ciencia-es-la-fuerza-para-el-futuro_a4918.html"
    accessed: 2026-10-24
    reliability_note: "Published interview text (recorded_interview, P8), Spanish."
    source_quality: "newspaper interview"
    used_for: [worldview, timing, lane_b]
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
    kind: other
    author: "Ada Yonath, interviewed by Anita Pollak (WINA)"
    citation: "Pollak, Anita / WINA. \"Ich bin sicherlich kein Start-up.\" Wina — Das jüdische Stadtmagazin, December 2016. https://www.wina-magazin.at/ich-bin-sicherlich-kein-start-up/"
    url: "https://www.wina-magazin.at/ich-bin-sicherlich-kein-start-up/"
    accessed: 2026-10-24
    reliability_note: "Published German interview text (recorded_interview, P8). Page byline also names Julia Kaldori; interview voice is Pollak/Yonath."
    source_quality: "newspaper interview"
    used_for: [worldview]
  - id: S6
    type: primary
    kind: other
    author: "Ada Yonath, interviewed by Cristina Escandón (Principia)"
    citation: "Escandón, Cristina. \"Interview with Ada Yonath.\" Principia, 16 March 2016. https://principia.io/2016/03/16/interview-ada-yonath.IjI1MSI/"
    url: "https://principia.io/2016/03/16/interview-ada-yonath.IjI1MSI/"
    accessed: 2026-10-24
    reliability_note: "Published interview text (English). Used for B corroboration (bases of natural processes)."
    source_quality: "newspaper interview"
    used_for: [worldview]
  - id: S7
    type: primary
    kind: other
    author: "Ada Yonath, interviewed by Susanna Ligero and Lucía Sapiña (Mètode)"
    citation: "Ligero, Susanna, and Lucía Sapiña. \"Interview with Ada Yonath.\" Mètode, 18 June 2018. https://metode.org/issues/entrevista-revistes/interview-with-ada-yonath.html"
    url: "https://metode.org/issues/entrevista-revistes/interview-with-ada-yonath.html"
    accessed: 2026-10-24
    reliability_note: "Published interview text (English). Primary for B recorded_interview ('law in life, in chemistry and in the world')."
    source_quality: "newspaper interview"
    used_for: [worldview, timing]
  - id: S8
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia. \"Ada Yonath.\" English Wikipedia. https://en.wikipedia.org/wiki/Ada_Yonath. Wikitext via API 2026-10-24 (P50 dual bio)."
    url: "https://en.wikipedia.org/wiki/Ada_Yonath"
    accessed: 2026-10-24
    reliability_note: "Used for native_name, birth name, death corroboration; Personal life silent on religion. Not used alone for worldview scores."
    source_quality: "reference entry"
    used_for: [identity, basics]
---

# Ada Yonath

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Ada Yonath (1939–2026), Israeli protein crystallographer, Nobel Prize in Chemistry 2009 for ribosome structure [S1]. Deepen D1: primary_system BELOW_THRESHOLD (leads AGNOS, JUDA); A BELOW_THRESHOLD; B 3 (0.5, alt 4; recorded_interview, support corroborated); C, D UNKNOWN; E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Not plotted. Chart-moving NO.

## Life and work

Jerusalem, Hebrew University, Weizmann Institute, Max Planck unit in Hamburg [S1; S2]. Native name עדה יונת; born Ada Esther Lifshitz [S8]. Died 31 August 2026 [S1; S2; S8].

## Contribution and impact

Ribosome crystallography from 1980; full subunit structures in 2000–2001; antibiotic binding (2001) [S1; S2].

## Childhood and education

Religious Jewish family, secular school [S2].

## Adult working worldview

In 2010 she said whether science and faith are compatible is "nothing I can know" (interview) [S3]. In 2016 she said religious people do not inquire into life's origins because "it is all in the Bible" (interview) [S5]. For B: "this is the law in life, in chemistry and in the world: the structure defines the function" (Mètode 2018) [S7], with Nobel autobiography principles-of-nature / mechanics lines [S2].

## Heritage (context only)

Jewish [S2].

## Timing

1980–2001, from age 41 [S1; S2]. Own-voice B remark 2018, after the span [S7].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Not assessed [S2].

## Open questions

- Hebrew/Israeli long-form that places or denies God, or states AGNOS explicitly.
- Own-voice no-exception claim for B certainty > 0.5.

## Research log

- 2026-10-19: Read Britannica (Rogers), the Nobel autobiography and the 2010 SINC interview.
- 2026-10-24: Deepen D1 — WINA Dec 2016, Principia Mar 2016, Mètode Jun 2018, Wikipedia EN (P50). B basis → recorded_interview, support corroborated; A/primary stay BELOW. No figures/.
