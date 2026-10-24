---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 7
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, third batch: physical science 1600–1950)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (third batch, RUNBOOK §1 order). Basics from Britannica (Aaserud, first page), MacTutor and the Nobel biography. Worldview from J. L. Heilbron, 'The Mind that Created the Bohr Atom' (Séminaire Poincaré 2013), which quotes Bohr's 1911–12 letters from Aaserud & Heilbron (2013), and from the AIP interview with Margrethe Bohr (1963, session I; reported speech). Rejected Christian theology in adolescence; left the Danish State Church in April 1912. primary_system BELOW_THRESHOLD (ATHE leading candidate, AGNOS named; both stub files). B 4, C 4, D 4, all at 0.5 (scholarly reconstruction); A, E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Rechecked under decision P8 (recorded interviews; schema 1.2): the AIP interview is Margrethe Bohr's reported speech and paraphrase only, so it scores nothing on its own; it only supports C_ledger, which rests on Heilbron. No score changed. Schema 1.1 → 1.2."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit, batch 3 (two blind runs at d9903b7). #1: primary_system how_known no longer quotes S7 (AIP no-quotation notice); it now paraphrases Margrethe Bohr and says the 'did not think of himself as anything' answer was to Kuhn's question whether he thought of himself as a Jew, not a question about religion; the 'not true' wording is Heilbron's (S4, p. 24). #5: D_authority 4 at 0.5 kept; the 'warn people that it was not true' item is now labelled Margrethe Bohr's 1963 account as reported by Heilbron (S4, p. 24, n. 30), not Bohr's words; p. 34 (truth in literature and science) dropped as D support and its statement untagged from D. D already at the 0.5 floor, so no certainty change; nothing downstream changes (mid_basin BELOW_THRESHOLD, A not scored). Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Stage 3 lens-audit rulings applied to the batch's other records (OPEN_DECISIONS P14–P28, v8's picks, 2026-10-02). Schema 1.2 → 1.3. One reliable source caps a fact at 0.7; derived fields take the lowest certainty of their inputs; kind lists (P21: research institute, school stage and run_by, scholarly edition); first lasting year per P13/P23, no coder's-choice wording. Full before → after list: reports/stage3_rulings_changes.csv. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "P30 rule 5 age sweep: ages recomputed as event year − birth year, with no month adjustment (scripts/recompute_ages.py; every change is in reports/p30_age_changes.csv). No other value changed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Span alignment (P29, P30 and its addendum): timing.major_work_period checked, 1913–1939 unchanged; worldview.working_years 1906–1962 → 1913–1939, equal to the span (P30 addendum f); evidence for every headline value checked against the span; no value or certainty changed. Listed in reports/p30_span_alignment.csv. Not reviewed."}
    - {date: 2026-10-08, by: "Grok Bot", summary: "Lens audit of batch C (dd91009), ruling R1, logged as P35 (v8's pick): B_cause 4 → 3 at 0.5, alternative 4, because B rests on Heilbron's reconstruction of his working science only. No other value changes; mid_basin unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #60, F5 rank 60). Needs: A BELOW_THRESHOLD; B faded. Primary Causality and Complementarity (Phil. Sci. 1937, S9) and Atomic Physics and Human Knowledge Discussion with Einstein (1958, S10) raise B 3@0.5 scholarly_reconstruction → B 4@0.7 written_profession, support corroborated (P48); alt 3. Aaserud & Heilbron 2013 Kierkegaard notes (S8, secondary quotation via Wikipedia S11) plus Witham 2006 fiancée-letter quotation (S12) score A 4@0.5 consistent_private_letters, support corroborated; alt BELOW (P38-style / Aaserud ajar-door). primary_system stays BELOW (ATHE leading; no positive naturalism in own words; Ingeniøren S13). P47 source_quality on S1–S13. mid_basin BELOW (A≥3 branch needs 0.7). Chart-moving NO. No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: bohr-niels
  display_name: "Niels Bohr"
  roster:
    canonical_name: "Niels Bohr"
    rank: 60
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: physics
    field_bucket: physics
  full_name: {value: "Niels Henrik David Bohr", certainty: 1.0, cites: [{source: S3, locator: "paragraph 1"}, {source: S1, locator: "opening"}], how_known: "Nobel biography; Britannica agrees."}
  native_name: {value: "Niels Henrik David Bohr (Danish)", certainty: 0.7, cites: [{source: S3, locator: "paragraph 1"}], how_known: "Danish name; same spelling."}
  aliases:
    - {name: "Bohr-Niels", kind: "roster alias"}
    - {name: "Niels-Bohr", kind: "roster alias"}

basics:
  birth:
    date: {value: "1885-10-07", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S2, locator: "header"}, {source: S3, locator: "paragraph 1"}], how_known: "Three sources agree."}
    place: {value: "Copenhagen", modern_name: "Copenhagen, Denmark", polity_then: "Denmark", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S3, locator: "paragraph 1"}], how_known: "Two sources agree; born in his grandmother Adler's house (S2, paragraph 1; S4, p. 20)."}
  death:
    date: {value: "1962-11-18", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S2, locator: "header"}, {source: S3, locator: "final paragraph"}], how_known: "Three sources agree."}
    place: {value: "Copenhagen", modern_name: "Copenhagen, Denmark", polity_then: "Denmark", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S3, locator: "final paragraph"}], how_known: "Two sources agree; MacTutor says at home, of a heart attack."}
  first_lasting_contribution_year: {value: 1913, certainty: 1.0, cites: [{source: S1, locator: "'Bohr model of the atom' paragraph"}, {source: S2, locator: "1913 papers"}], how_known: "The 1913 trilogy on atomic constitution (Philosophical Magazine)."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "'Bohr model of the atom' paragraph"}], how_known: "From first_lasting_contribution_year (P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}], how_known: "Denmark is Northern Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.7, cites: [{source: S3, locator: "paragraphs 4–6"}], how_known: "Copenhagen, with formative stays in Cambridge and Manchester (both Northern Europe)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S3, locator: "paragraph 1"}], how_known: "As the sources record it."}
  languages_of_work: {value: [Danish, English, German], certainty: 0.7, cites: [{source: S3, locator: "paragraph 9 (English books)"}, {source: S2, locator: "1913 papers in the Philosophical Magazine"}], how_known: "English publications are documented; Danish was his language at home and at the institute. German is the usual language of the 1920s physics community but was not checked here."}
  occupations: {value: [physicist, "university professor", "institute director"], certainty: 1.0, cites: [{source: S3, locator: "paragraphs 6, 12"}, {source: S1, locator: "opening"}], how_known: "Two sources."}

contribution:
  fields: {value: ["atomic physics", "quantum theory", "nuclear physics"], certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "paragraphs 5–8"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Quantum model of the atom (stationary states; radiation only in transitions between them)", year: "1913", kind: theory, lasting: "the Bohr model; Nobel Prize 1922", certainty: 1.0, cites: [{source: S1, locator: "'Bohr model of the atom' paragraph"}, {source: S2, locator: "1913 papers"}], how_known: "Two sources."}
    - {value: "Complementarity as an interpretation of quantum mechanics (Como, September 1927)", year: "1927", kind: "concept or term", lasting: "the Copenhagen interpretation", certainty: 1.0, cites: [{source: S2, locator: "Como 1927 paragraph"}, {source: S3, locator: "paragraph 8"}], how_known: "Two sources."}
    - {value: "Compound-nucleus (liquid-drop) model, and fission explained by uranium-235", year: "1936–1939", kind: theory, lasting: "nuclear fission theory", certainty: 1.0, cites: [{source: S3, locator: "paragraph 7"}, {source: S2, locator: "'other major contributions'"}], how_known: "Two sources."}
    - {value: "Institute for Theoretical Physics, Copenhagen (now the Niels Bohr Institute)", year: "1921", kind: institution, lasting: "centre of 1920s quantum physics", certainty: 0.7, cites: [{source: S1, locator: "'Bohr's Institute for Theoretical Physics' (inauguration 3 March 1921)"}, {source: S2, locator: "opening in 1921"}, {source: S3, locator: "paragraph 6 ('since 1920')"}], how_known: "Britannica and MacTutor give 1921; the Nobel biography says he headed it 'since 1920'."}
  evidence_of_impact:
    - {value: "Nobel Prize in Physics for work on atomic structure", kind: "honours in lifetime", certainty: 1.0, cites: [{source: S3, locator: "paragraph 6"}, {source: S2, locator: "Nobel paragraph"}], how_known: "Two sources."}
    - {value: "Element 72 (hafnium, after Copenhagen) found at his institute as his theory predicted", kind: "other", certainty: 0.7, cites: [{source: S1, locator: "'Nobel Prize' section"}], how_known: "Britannica."}
  major_works:
    - {value: "On the Constitution of Atoms and Molecules (three papers, Philosophical Magazine)", year: 1913, kind: "paper or paper series", certainty: 1.0, cites: [{source: S1, locator: "'Bohr model of the atom' paragraph"}, {source: S2, locator: "1913 papers"}], how_known: "Two sources."}
    - {value: "Atomic Theory and the Description of Nature", year: 1934, kind: book, certainty: 0.7, cites: [{source: S3, locator: "paragraph 9"}], how_known: "Nobel biography."}
    - {value: "Atomic Physics and Human Knowledge (essays 1933–1957)", year: 1958, kind: book, certainty: 0.7, cites: [{source: S3, locator: "paragraph 8"}], how_known: "Nobel biography."}
  honours:
    - {value: "Gold medal of the Royal Danish Academy of Sciences (prize essay on surface tension of water jets)", year: 1906, certainty: 0.7, cites: [{source: S2, locator: "first paper"}, {source: S3, locator: "paragraph 3"}], how_known: "MacTutor dates the medal 1906; the Nobel biography gives the publication (1908) but no award year."}
    - {value: "Nobel Prize in Physics", year: 1922, certainty: 1.0, cites: [{source: S3, locator: "paragraph 6"}, {source: S2, locator: "Nobel paragraph"}], how_known: "Two sources."}
    - {value: "First U.S. Atoms for Peace Award", year: 1957, certainty: 0.7, cites: [{source: S2, locator: "final paragraphs"}], how_known: "MacTutor."}
  definition_fit: {value: "clearly meets", rationale: "Founded the quantum theory of the atom and led its interpretation.", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Sources agree."}

childhood:
  family_religion: {value: "Lutheran state church by upbringing in a non-religious home: father an atheist; mother from a Jewish family, not religious", certainty: 0.7, cites: [{source: S4, locator: "p. 20"}, {source: S7, locator: "Session I (religious training)"}, {source: S2, locator: "'christened in the Christian Church'"}], how_known: "Heilbron (from Aaserud & Heilbron) and Margrethe Bohr's 1963 recollection agree that neither parent was religious; the father's atheism is Heilbron's word. Not 1.0 because both depend on family sources."}
  family_religious_practice: {value: "No religious training at home; the father took him to church on Christmas Eve so he would not feel different from other boys, and said nothing about religion", certainty: 0.7, cites: [{source: S4, locator: "p. 20"}, {source: S7, locator: "Session I (religious training)"}], how_known: "Heilbron says the father 'exposed his son to the state religion so that he would not feel himself different from other boys'; Margrethe Bohr recalled a 1911 Christmas letter from Cambridge saying the same."}
  parents_and_household:
    - {value: "Father, Christian Bohr, professor of physiology at the University of Copenhagen", name: "Christian Bohr", role: father, certainty: 1.0, cites: [{source: S3, locator: "paragraph 1"}, {source: S2, locator: "paragraph 1"}], how_known: "Two sources."}
    - {value: "Mother, Ellen Adler, daughter of the Jewish banker and politician David (Baruch) Adler", name: "Ellen Bohr (née Adler)", role: mother, certainty: 1.0, cites: [{source: S2, locator: "paragraph 1"}, {source: S4, locator: "p. 20"}], how_known: "Two sources."}
  household_circumstances: {value: "Professor's household in Copenhagen with an older sister (Jenny) and a younger brother (the mathematician Harald Bohr); his father's circle (Høffding, Christiansen, Thomsen) met for discussions the boys listened to", certainty: 1.0, cites: [{source: S2, locator: "paragraphs 1–4"}, {source: S4, locator: "p. 32"}], how_known: "Two sources."}
  schooling:
    - {value: "Gammelholm Grammar School, Copenhagen (student examination 1903)", stage: "grammar or secondary school", years: "1891–1903", certainty: 1.0, cites: [{source: S3, locator: "paragraph 2"}, {source: S2, locator: "school paragraph ('Grammelholms school')"}], how_known: "Two sources; MacTutor spells it 'Grammelholms'."}
    - {value: "University of Copenhagen: physics, with mathematics, astronomy and chemistry; MSc 1909, doctorate 1911 (electron theory of metals)", stage: university, years: "1903–1911", certainty: 1.0, cites: [{source: S3, locator: "paragraph 2"}, {source: S2, locator: "university paragraph"}], how_known: "Two sources."}
  early_mathematics: {value: "other", note: "Specialised in mathematics and physics in his last two school years; level not stated.", certainty: 0.7, cites: [{source: S2, locator: "school paragraph"}], how_known: "MacTutor only."}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure:
    - {value: "His father's influence: 'My interest in the study of physics was awakened while I was still in school, largely owing to the influence of my father.'", certainty: 0.7, cites: [{source: S2, locator: "school paragraph (Bohr, 1922)"}], how_known: "Bohr's 1922 words as quoted by MacTutor."}
  key_early_reading:
    - {value: "Icelandic sagas and Fenimore Cooper's tales, by his widow's recollection that he read them as a schoolboy", certainty: 0.7, cites: [{source: S7, locator: "Session I (reading)"}], how_known: "One recollection, hedged ('I think')."}
  childhood_mentors:
    - {value: "His father Christian Bohr", certainty: 1.0, cites: [{source: S2, locator: "school paragraph"}, {source: S4, locator: "p. 20"}], how_known: "Two sources."}
    - {value: "Harald Høffding (philosopher) and Christian Christiansen (physicist), friends of his father and later his teachers", certainty: 1.0, cites: [{source: S2, locator: "university paragraph"}, {source: S4, locator: "p. 32"}], how_known: "Two sources."}
  languages_in_childhood: {value: [Danish], certainty: 0.7, cites: [{source: S2, locator: "paragraph 1"}], how_known: "Danish home and school."}
  notable_events:
    - {value: "Lost his faith in early adolescence after a period of taking religion seriously; told his father, whose smile he took as approval", year: "c. 1899–1900", certainty: 0.7, cites: [{source: S4, locator: "p. 20"}, {source: S7, locator: "Session I (religious training)"}], how_known: "Heilbron and Margrethe Bohr agree; Margrethe put his age at 14 or 15. Dates approximate."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1913–1939", certainty: 0.7, cites: [{source: S2, locator: "1913 papers; 'other major contributions'"}, {source: S3, locator: "paragraphs 5–8"}], how_known: "Equal to timing.major_work_period (P30 addendum f; span check 2026-10-02). Was 1906–1962: From the prize essay to his death."}
  nominal_affiliations:
    - {value: "Christened in the Lutheran Church of Denmark; formally resigned from it in April 1912 so that his wedding could not be religious; civil wedding 1 August 1912", years: "c. 1898–1912", role: "former member", certainty: 1.0, cites: [{source: S4, locator: "p. 20"}, {source: S5, locator: "1912, 'Apr 16'"}, {source: S2, locator: "'christened in the Christian Church'"}], how_known: "Heilbron (both Niels and Margrethe 'formally resigned from the Danish State Church') and the Halvorson chronology (16 April 1912) agree. Margrethe Bohr recalled that the children were christened at about 13 or 14 (S7); Heilbron says only that their mother agreed to it."}
  self_described_science_religion_relation:
    value: "None stated in published form in what was read. In 1911–12 letters he called his conviction 'that everything that is of any value is true' almost 'my religion', and set 'so-called scientific truths' beside the truths of literature as of 'a somewhat different kind'; in explaining his rejection of religion he wrote that life 'would be so infinitely trivial if I thought I could understand it'."
    certainty: 0.5
    cites: [{source: S4, locator: "pp. 32, 34"}]
    how_known: "Letters known only as quoted in English by Heilbron (secondary quotation), so 0.5."
  primary_system:
    value: BELOW_THRESHOLD
    cites: [{source: S4, locator: "pp. 20, 24"}, {source: S8, locator: "p. 110 (via S11)"}, {source: S7, locator: "Session I (religion)"}, {source: S13, locator: "Aaserud interview"}]
    how_known: "Positive evidence of rejection of religion and of a personal God-bond, but not of which non-theist position at ≥0.5. Heilbron: he realised 'Christian theology was nonsense' (S4, p. 20) and, citing Margrethe Bohr (n. 30), wanted for a time to warn that religion 'was not true' (p. 24). Aaserud & Heilbron 2013 (S8, p. 110, quoted via Wikipedia S11): 'well-fortified atheism' and 'Bohr ended with no religious belief and a dislike of all religions that claimed to base their teachings on revelations' — scholarly characterisation, not his self-label. Finn Aaserud (S13): he was an atheist though he never used the word, and held a door ajar for 'something greater' outside understanding. ATHE needs positive naturalism (v7.1); AGNOS needs explicit suspension. Own words deny union with God (S8 pp. 159–160) but do not affirm naturalism or name suspension. Same treatment as Curie (batch 2, #108)."
    note: "Candidates: ATHE (leading, via S8 p. 110 and S13) or AGNOS (ajar-door / never self-labelled atheist). Stub system files (flag)."
  secondary_system: {value: UNKNOWN, how_known: "No second system in S1–S13."}
  candidate_codes_considered:
    - {code: ATHE, reason: "Leading candidate, not coded (BELOW_THRESHOLD): S8 p. 110 'well-fortified atheism' / 'no religious belief'; S13 Aaserud 'ateist' though Bohr never used the word; theology 'nonsense' (S4, p. 20). Not coded: no positive naturalism in his own words (v7.1). Stub system file (flag).", cites: [{source: S8, locator: "p. 110 (via S11)"}, {source: S13, locator: "Aaserud interview"}, {source: S4, locator: "pp. 20, 24"}]}
    - {code: AGNOS, reason: "Candidate, not coded: S13 Aaserud says a possible God would be beyond reach, so Bohr 'holds a door ajar for something greater'; he never self-labelled atheist. Not coded: no explicit suspension statement of his own. Stub system file (flag).", cites: [{source: S13, locator: "Aaserud interview ('dør på klem')"}, {source: S4, locator: "p. 32"}]}
    - {code: CHRIST, reason: "Rejected: christening and nominal Lutheran upbringing only; he left the church in 1912 on his own convictions. Church membership is never a code.", cites: [{source: S4, locator: "p. 20"}, {source: S5, locator: "1912"}]}
    - {code: JUDA, reason: "Rejected: Jewish maternal heritage only; the family did not attend synagogue and he did not think of himself as a Jew (S7). Heritage is never a code.", cites: [{source: S7, locator: "Session I (Jewish background)"}]}
  lio_axes:
    A_locus:
      value: 4
      basis: consistent_private_letters
      certainty: 0.5
      support: corroborated
      cites: [{source: S8, locator: "pp. 159–160 (via S11)"}, {source: S12, locator: "pp. 138–139"}, {source: S4, locator: "p. 20"}, {source: S13, locator: "Aaserud interview (ajar-door alt)"}]
      how_known: "Two independent private documents (Kierkegaard loose notes; fiancée letter), known only as secondary quotations (P26); primary check of Aaserud & Heilbron 2013 pending (lending). 0.5 also for the ajar-door alternative (S13). S13 is cited on the value so the BELOW alternative does not alone introduce a source (P48)."
      rationale: "No personal God-bond (P20/P38 logic): in loose notes on Kierkegaard, 'I, who do not feel in any way united with, and even less, bound to a God' (S8, pp. 159–160, via S11); to his fiancée he ruled out that a person 'must beg from and bargain with fancied powers infinitely stronger than himself' (S12, pp. 138–139). Theology rejection (S4, p. 20) alone would not score A (Turing/Curie pattern); these are locus denials. Named alternative: BELOW_THRESHOLD — notes unpublished and undated in what was read; Aaserud (S13) holds a door ajar for something greater; secondary quotation only (P26)."
      alternatives:
        - {value: BELOW_THRESHOLD, note: "P38-style caution: ajar door (S13); unpublished notes; secondary quotation.", cites: [{source: S13, locator: "Aaserud interview"}, {source: S8, locator: "pp. 159–160 (via S11)"}]}
    B_cause:
      value: 4
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S9, locator: "pp. 293–297"}, {source: S10, locator: "p. 41"}, {source: S4, locator: "pp. 30, 49"}]
      how_known: "Two independent published essays of his own (S9 1937; S10 Discussion with Einstein in APHK 1958). Named alternative keeps certainty at 0.7. Independent source ids → corroborated (P48). Was B 3@0.5 under P35 until this pass."
      rationale: "Scored on his account of nature (P6), his working physics and his philosophy of it. Complementarity is 'a rational generalization of the very ideal of causality' (S10, p. 41); the 1937 essay speaks of 'deeper lying laws of nature' and a 'new type of laws' (S9, pp. 294–295), renounces classical causal description for atomic phenomena while rejecting mysticism and holding that 'any violation of physico-chemical laws in organic life … would be excluded' (S9, p. 297). Statistical / complementary lawfulness, not miracle or exemption — same pattern as Heisenberg B 4. Named alternative: 3, if the forced 'renunciation of the ideal of causality' (S9, p. 293) is read as a standing exception rather than a generalization of lawfulness."
      alternatives:
        - {value: 3, note: "If renunciation of classical causality is read as a limited exception inside nature.", cites: [{source: S9, locator: "p. 293"}]}
    C_ledger:
      value: 4
      basis: scholarly_reconstruction
      certainty: 0.5
      support: corroborated
      cites: [{source: S4, locator: "p. 20"}, {source: S7, locator: "Session I (religion)"}]
      how_known: "Heilbron's reconstruction from family letters and interviews; no statement in Bohr's own published words. Rechecked under decision P8 (2026-10-02): the score rests on Heilbron (S4); the AIP interview (S7) is his widow's reported speech and can only be paraphrased, so it only supports the score, which P8 allows. Unchanged."
      rationale: "Impersonal consequence or none. Heilbron reports that he questioned 'not only the doctrine but also the concept' of salvation ('what could it mean to have a saved soul?') and concluded that 'Christian theology was nonsense' (S4, p. 20); Margrethe Bohr said he held religion untrue all the years she knew him (S7). No judgement, afterlife or personal reckoning is affirmed anywhere read."
    D_authority:
      value: 4
      basis: scholarly_reconstruction
      certainty: 0.5
      support: single
      cites: [{source: S4, locator: "pp. 20, 24 (n. 30)"}]
      how_known: "Heilbron's reconstruction (scholarly_reconstruction, 0.5): one letter phrase of Bohr's quoted by him (secondary quotation, p. 20) and one item of reported speech, Margrethe Bohr's 1963 account as Heilbron gives it (p. 24, n. 30). Lens audit batch 3 (#5): p. 34 dropped as support, since it is about truth in literature and science, not about which authority decides. 0.5 is already the lowest scored level."
      rationale: "Observation and reason outrank revelation. On Heilbron's account he reached his rejection of theology by his own reasoning, and he took his father's smile to show 'that I too could think' (S4, p. 20, his letter of 1911). By his widow's 1963 account, as Heilbron reports it, he wanted for a time to write a book on religion to warn people 'that it was not true' (S4, p. 24, n. 30; reported speech, not his words). No authority above reason is acknowledged in anything read."
    E_scope: {value: BELOW_THRESHOLD, how_known: "Scored on the world's order (P7). Nothing read addresses favour for a group in events; not scored from working science alone (same treatment as Fermi and Curie). The rejection of salvation is scored on C."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus ≥ 3 (value 4) but only at 0.5: the A ≥ 3 branch reads A only (P10) and needs 0.7, as for Crick, Skinner and Shannon. B is 4 at 0.7 and does not lift the branch."}
  statements:
    - text: "That smile. . . showed me that I too could think."
      cites: [{source: S4, locator: "p. 20 (n. 2: Niels to Margrethe, 21 Dec 1911, in Aaserud & Heilbron, p. 161)"}]
      date: "1911-12-21"
      context: "Letter to his fiancée Margrethe Nørlund, recalling his father's smile when he reported that he had rejected Christian theology. The ellipsis is Heilbron's."
      axes: [D_authority]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-02
    - text: "[life] would be so infinitely trivial if I thought I could understand it."
      cites: [{source: S4, locator: "p. 32 (n. 57: Bohr to Sophie Nørlund, 1 May 1912, in Aaserud & Heilbron, p. 77)"}]
      date: "1912-05-01"
      context: "Letter to Margrethe's mother 'in attempting an explanation of his rejection of religion' (Heilbron). The bracketed word is Heilbron's."
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-02
    - text: "[I]t is something I feel very strongly about; I can almost call it my religion, that I think that everything that is of any value is true."
      cites: [{source: S4, locator: "p. 34"}]
      date: "1912-01-15"
      context: "Letter to Margrethe Nørlund on truth in literature and science, as quoted by Heilbron in English translation."
      note: "Not tagged to D_authority since the lens audit (batch 3, #5): the passage is about truth in literature and science, not about which authority decides."
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-02
  changes_over_life:
    - {value: "A period of taking religion seriously in early adolescence, then complete rejection of Christian theology", year: "c. 1899–1900", certainty: 0.7, cites: [{source: S4, locator: "p. 20"}, {source: S7, locator: "Session I (religious training)"}], how_known: "Two accounts agree; dates approximate."}
    - {value: "Left the Danish State Church before his civil wedding", year: "1912", certainty: 1.0, cites: [{source: S4, locator: "p. 20"}, {source: S5, locator: "1912, 'Apr 16'"}], how_known: "Two sources."}
  coder_notes: "ATHE and AGNOS are stub system files (flag). 1911–12 letter quotations remain secondary (Heilbron / Witham). Kierkegaard notes (S8) and the fiancée 'fancied powers' letter (S12) are secondary quotations; Aaserud & Heilbron 2013 not opened this pass (lending). S9 and S10 are Bohr's own published English essays (primary facsimile). S7 AIP remains paraphrase-only under P8 and does not score axes alone. S13 (Ingeniøren / Aaserud) is a newspaper interview used for primary_system candidates and the A alternative, not as written_profession."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Danish; mother's family Jewish (the Adlers), assimilated", certainty: 1.0, cites: [{source: S2, locator: "paragraph 1"}, {source: S4, locator: "p. 20"}], how_known: "Two sources."}
  religious_heritage_by_birth: {value: "Lutheran (father's side; children christened) and Jewish (mother's family)", certainty: 1.0, cites: [{source: S4, locator: "p. 20"}, {source: S2, locator: "'christened in the Christian Church'"}], how_known: "Two sources."}
  baptism_or_initiation: {value: "Christened in the Danish Lutheran church, at about 13 or 14 by Margrethe Bohr's recollection", certainty: 0.7, cites: [{source: S2, locator: "'christened in the Christian Church'"}, {source: S4, locator: "p. 20"}, {source: S7, locator: "Session I (religious training)"}], how_known: "The christening is in three sources; the age is in one recollection only."}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1913–1939", certainty: 0.7, cites: [{source: S2, locator: "1913 papers; 'other major contributions'"}, {source: S3, locator: "paragraphs 5–8"}], how_known: "From the atomic model (1913) to the fission work (1939), as the two sources date them."}
  age_at_first_lasting_contribution: {value: 28, certainty: 1.0, cites: [{source: S1, locator: "Quick Facts; 'Bohr model of the atom' paragraph"}], how_known: "Born October 1885; the trilogy appeared in 1913. P30 (rule 5): 1913 − 1885 = 28, with no month adjustment; was 27 until the P30 age sweep (2026-10-02)."}
  first_evidence_of_lio_type_views: {value: "Rejection of Christian theology, including the concept of a saved soul", year: "c. 1899–1900", certainty: 0.5, cites: [{source: S4, locator: "p. 20"}], how_known: "Heilbron's reconstruction; a loss of faith, not an LIO statement as such."}
  lio_views_relative_to_major_work: {value: "before major work", rationale: "The rejection of theology (adolescence) and the 1911–12 letters predate the 1913 atom.", certainty: 0.5, cites: [{source: S4, locator: "pp. 20, 34"}], how_known: "Dates."}
  worldview_during_major_work: {value: "Outside the church from April 1912, on his own convictions; religion judged untrue throughout", certainty: 0.7, cites: [{source: S4, locator: "pp. 20, 24"}, {source: S5, locator: "1912"}, {source: S7, locator: "Session I (religion)"}], how_known: "Three sources agree."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", certainty: 0.5, cites: [{source: S1, locator: "'Bohr model of the atom' paragraph"}], how_known: "Coder's reading: the 1913 atom is built from stated postulates and their consequences, but Bohr's method as Heilbron describes it works from impasses ('irrationals'), not definitions."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S4, locator: "p. 32"}], how_known: "Høffding's epistemology shaped his idea of truth (Heilbron); nothing on a deductive form."}
  circle_present: {value: "no", rationale: "No God-Nature identity in anything read.", certainty: 0.5, cites: [{source: S4, locator: "pp. 20, 24"}], how_known: "Absence in the sources read."}
  reading: "As belief, not finding: form partly present, no circle. The record does not test H1."
  notes: ""

institutions:
  - {value: "University of Copenhagen", role: "lecturer (1913–1914); professor of theoretical physics (1916–)", years: "1913–1962", kind: university, certainty: 1.0, cites: [{source: S3, locator: "paragraph 6"}, {source: S1, locator: "'Bohr's Institute for Theoretical Physics'"}], how_known: "Two sources."}
  - {value: "Institute for Theoretical Physics, Copenhagen", role: director, years: "1921–1962", kind: "research institute", certainty: 0.7, cites: [{source: S2, locator: "opening in 1921"}, {source: S3, locator: "paragraph 6"}], how_known: "Start date 1920 (Nobel) or 1921 (MacTutor, Britannica)."}
  - {value: "Victoria University of Manchester", role: "research with Rutherford (1912); lecturer (1914–1916)", years: "1912–1916", kind: university, certainty: 1.0, cites: [{source: S3, locator: "paragraphs 5–6"}, {source: S2, locator: "Manchester paragraphs"}], how_known: "Two sources."}
  - {value: "Royal Danish Academy of Sciences and Letters", role: "member from 1917; later president", years: "1917–1962", kind: "academy or learned society", certainty: 0.7, cites: [{source: S2, locator: "1917"}, {source: S3, locator: "paragraph 11"}], how_known: "Membership in MacTutor; presidency in the Nobel biography (years not given)."}
  - {value: "British and American atomic bomb projects (including Los Alamos)", role: consultant, years: "1943–1945", kind: "government or state body", certainty: 0.7, cites: [{source: S3, locator: "paragraph 10"}, {source: S2, locator: "1943 paragraph"}], how_known: "Two sources, in outline."}
collaborators:
  - {value: "Ernest Rutherford", roster_id: rutherford-ernest, relation: "mentor or employer", note: "Manchester 1912 and 1914–16; Bohr saw him as his teacher", certainty: 1.0, cites: [{source: S2, locator: "Manchester paragraphs"}, {source: S3, locator: "paragraph 5"}], how_known: "Two sources."}
  - {value: "J. J. Thomson", roster_id: thomson-j-j, relation: "mentor or employer", note: "Cambridge 1911; they did not get on", certainty: 1.0, cites: [{source: S2, locator: "Cambridge paragraph"}, {source: S3, locator: "paragraph 5"}], how_known: "Two sources."}
  - {value: "Harald Høffding", relation: teacher, note: "philosophy teacher and family friend", certainty: 1.0, cites: [{source: S2, locator: "university paragraph"}, {source: S4, locator: "p. 32"}], how_known: "Two sources."}
  - {value: "Werner Heisenberg", roster_id: heisenberg-werner, relation: collaborator, note: "complementarity was proposed as an interpretation of Heisenberg's uncertainty relations", certainty: 0.7, cites: [{source: S2, locator: "Como 1927 paragraph"}], how_known: "MacTutor."}
  - {value: "Harald Bohr", relation: family, note: "brother, mathematician", certainty: 1.0, cites: [{source: S2, locator: "paragraph 1"}, {source: S3, locator: "paragraph 1"}], how_known: "Two sources."}

review:
  roster_status_reason: {value: "Core in v8 (F 5, all five models).", certainty: 0.7, cites: [{source: S6, locator: "roster.csv, rank 60"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Institute start: 'since 1920' (Nobel biography) vs opened 1921 (MacTutor; Britannica gives the inauguration 3 March 1921)."
    - "School name: Gammelholm (Nobel biography) vs 'Grammelholms' (MacTutor)."
    - "Christening age: Margrethe Bohr recalled about 13 or 14 (S7); Heilbron does not give an age."
    - "Britannica was read as its first page only."
    - "Aaserud & Heilbron 2013 (S8) not opened; pp. 110 and 159–160 quoted via Wikipedia (S11)."
    - "S7 is the AIP transcript as archived by the Wayback Machine (the live AIP page now redirects to a repository that refused the fetch); AIP's notice restricts quotation, so it is paraphrased."
  open_questions:
    - "Primary check of Aaserud & Heilbron, Love, Literature and the Quantum Atom (2013), pp. 110, 159–160 (and surrounding letters) — IA lending-only this pass; now cited via Wikipedia quotation."
    - "Primary text of the fiancée 'fancied powers' letter (Witham 2006 quotes it; likely in Aaserud & Heilbron)."
    - "Heisenberg's Der Teil und das Ganze reports Bohr's 1927 remarks on religion; reported speech, reconstructed decades later, not used for A."
    - "Published religion essay Witham mentions (psychological experience, not deities) — identify and read for A/primary_system."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Finn Aaserud"
    citation: "Aaserud, Finn. \"Niels Bohr.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Niels-Bohr."
    url: "https://www.britannica.com/biography/Niels-Bohr"
    accessed: 2026-10-02
    source_quality: "reference entry"
    reliability_note: "Signed article by the former director of the Niels Bohr Archive; first page only. Sections cited by heading."
    used_for: [identity, basics, contribution, institutions, timing, lane_b]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "J J O'Connor and E F Robertson"
    citation: "O'Connor, J. J., and E. F. Robertson. \"Niels Henrik David Bohr.\" MacTutor History of Mathematics, University of St Andrews. https://mathshistory.st-andrews.ac.uk/Biographies/Bohr_Niels/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Bohr_Niels/"
    accessed: 2026-10-02
    source_quality: "reference entry"
    reliability_note: "Biography drawing on Pais and Kennedy; no paragraph numbers, so located by topic."
    used_for: [basics, contribution, childhood, worldview, heritage, timing, institutions, collaborators]
  - id: S3
    type: tertiary
    kind: "institutional page"
    author: "Nobel Foundation"
    year: 1965
    citation: "\"Niels Bohr – Biographical.\" From Nobel Lectures, Physics 1922–1941. Amsterdam: Elsevier, 1965. NobelPrize.org. https://www.nobelprize.org/prizes/physics/1922/bohr/biographical/."
    url: "https://www.nobelprize.org/prizes/physics/1922/bohr/biographical/"
    accessed: 2026-10-02
    source_quality: "reference entry"
    reliability_note: "Official biography; paragraphs counted from 'Niels Henrik David Bohr was born'."
    used_for: [identity, basics, contribution, childhood, worldview, timing, institutions, collaborators]
  - id: S4
    type: secondary
    kind: "journal article"
    author: "J. L. Heilbron"
    year: 2013
    citation: "Heilbron, J. L. \"The Mind that Created the Bohr Atom.\" Séminaire Poincaré XVII (2013): 19–58. https://seminaire-poincare.pages.math.cnrs.fr/heilbron.pdf."
    url: "https://seminaire-poincare.pages.math.cnrs.fr/heilbron.pdf"
    accessed: 2026-10-02
    source_quality: "scholarly edition or monograph"
    reliability_note: "Scholarly essay by a leading Bohr historian, quoting Bohr's 1911–12 letters in English from Aaserud & Heilbron (2013) and Margrethe Bohr's 1963 interview. Page numbers are the journal's printed pages (running heads)."
    used_for: [basics, childhood, worldview, heritage, timing, lane_b, collaborators]
  - id: S5
    type: secondary
    kind: other
    author: "Hans Halvorson"
    citation: "Halvorson, Hans. \"Niels Bohr chronology.\" https://hanshalvorson.dk/bohr/chronology.html."
    url: "https://hanshalvorson.dk/bohr/chronology.html"
    accessed: 2026-10-02
    source_quality: "unofficial web copy"
    reliability_note: "Chronology by a philosopher of physics; used only for the date of leaving the church (1912, 'Apr 16'), which agrees with Heilbron's undated account."
    used_for: [worldview, timing]
  - id: S6
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    source_quality: "study roster"
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
  - id: S7
    type: primary
    kind: "archive record"
    author: "Margrethe Bohr, Aage Bohr and Léon Rosenfeld, interviewed by Thomas S. Kuhn"
    year: 1963
    citation: "Interview with Margrethe Bohr by Thomas S. Kuhn, Aage Bohr, and Leon Rosenfeld, Copenhagen, 23 January 1963, Session I. Niels Bohr Library & Archives, American Institute of Physics. Archived copy of the AIP page: https://web.archive.org/web/20140911200150/http://www.aip.org/history/ohilist/4514_1.html."
    url: "https://web.archive.org/web/20140911200150/http://www.aip.org/history/ohilist/4514_1.html"
    accessed: 2026-10-02
    source_quality: "archive scan (OCR only)"
    reliability_note: "Official AIP transcript (as archived in 2014); reported speech by his widow, son and a colleague. Some speaker labels are missing in the scanned typescript. AIP restricts quotation without permission, so the record paraphrases. Located by topic within Session I."
    used_for: [childhood, worldview, heritage, timing]
  - id: S8
    type: secondary
    kind: "scholarly book"
    author: "Finn Aaserud and J. L. Heilbron"
    year: 2013
    citation: "Aaserud, Finn, and J. L. Heilbron. Love, Literature and the Quantum Atom: Niels Bohr's 1913 Trilogy Revisited. Oxford: Oxford University Press, 2013."
    url: "https://global.oup.com/academic/product/love-literature-and-the-quantum-atom-9780199680283"
    accessed: 2026-10-24
    source_quality: "scholarly edition or monograph"
    reliability_note: "Scholarly edition of Bohr's 1911–12 letters and notes. Book not opened this pass (IA lending-only); Kierkegaard-note quotation (pp. 159–160) and 'well-fortified atheism' (p. 110) taken from Wikipedia EN (S11) and Celebrity Atheist List, which cite those pages. Secondary quotation (P26)."
    used_for: [worldview]
  - id: S9
    type: primary
    kind: "journal article"
    author: "Niels Bohr"
    year: 1937
    citation: 'Bohr, Niels. "Causality and Complementarity." Philosophy of Science 4, no. 3 (July 1937): 289–298. https://www.jstor.org/stable/184445 (PDF via informationphilosopher.com).'
    url: "https://www.informationphilosopher.com/solutions/scientists/bohr/Causality_and_Complementarity.pdf"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "Bohr's own English essay; PDF checked page-for-page (running heads 289–298). Used for B_cause."
    used_for: [worldview]
  - id: S10
    type: primary
    kind: "published work by the subject"
    author: "Niels Bohr"
    year: 1958
    citation: 'Bohr, Niels. Atomic Physics and Human Knowledge. New York: John Wiley & Sons, 1958. Essay "Discussion with Einstein on Epistemological Problems in Atomic Physics" (pp. 32–66).'
    url: "https://digitalcommons.bard.edu/cgi/viewcontent.cgi?article=1219&context=community_of_scholars_archive"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "1958 Wiley collection PDF (Bard digitalcommons). Complementarity-as-generalization sentence on printed p. 41. Used for B_cause."
    used_for: [worldview, contribution]
  - id: S11
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: '"Niels Bohr." Wikipedia. https://en.wikipedia.org/wiki/Niels_Bohr.'
    url: "https://en.wikipedia.org/wiki/Niels_Bohr"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Used for dual-source biography and as the quotation vehicle for S8 pp. 159–160 and p. 110 (footnotes cite Aaserud & Heilbron 2013). Not used alone for axis scores (P50)."
    used_for: [worldview, basics]
  - id: S12
    type: secondary
    kind: "scholarly book"
    author: "Larry Witham"
    year: 2006
    citation: "Witham, Larry. The Measure of God: History's Greatest Minds Wrestle with Reconciling Science and Religion. New York: HarperCollins, 2006, pp. 138–139."
    accessed: 2026-10-24
    source_quality: "other"
    reliability_note: "Popular secondary; quotes Bohr's letter to his fiancée on 'fancied powers'. Used only as a second private-document quotation for A_locus corroboration; primary letter not checked."
    used_for: [worldview]
  - id: S13
    type: secondary
    kind: other
    author: "Thomas Djursing, interviewing Finn Aaserud"
    year: 2015
    citation: 'Djursing, Thomas. "Ny minister spreder usandheder om Niels Bohr: Han var ateist." Ingeniøren, 9 July 2015. https://ing.dk/artikel/ny-minister-spreder-usandheder-om-niels-bohr-han-var-ateist.'
    url: "https://ing.dk/artikel/ny-minister-spreder-usandheder-om-niels-bohr-han-var-ateist"
    accessed: 2026-10-24
    source_quality: "newspaper interview"
    reliability_note: "Interview with the then director of the Niels Bohr Archive. Used for primary_system candidates and the A_locus BELOW alternative ('dør på klem' / door ajar); not as written_profession."
    used_for: [worldview]

---

# Niels Bohr

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Niels Bohr (1885–1962), Danish physicist, built the quantum model of the atom in 1913, proposed complementarity in 1927 and won the 1922 Nobel Prize in Physics [S1, opening; S2, Como 1927 paragraph; S3, paragraph 6]. Christened Lutheran in a non-religious home, he rejected Christian theology in adolescence and left the Danish State Church in 1912 [S4, p. 20; S5, 1912]. System below threshold (ATHE leading, AGNOS named); A 4 at 0.5 (alt BELOW); B 4 at 0.7 written_profession (alt 3); C 4 and D 4 at 0.5; E below threshold; mid_basin below threshold (A≥3 needs 0.7).

## Life and work

Born in Copenhagen to the physiologist Christian Bohr and Ellen Adler [S3, paragraph 1]. He studied at the University of Copenhagen (doctorate 1911), worked with J. J. Thomson at Cambridge and with Rutherford at Manchester (1911–12), held a Manchester lectureship (1914–16) and took the Copenhagen chair of theoretical physics in 1916 [S3, paragraphs 2–6]. He directed the Institute for Theoretical Physics from its opening in 1921 to his death [S2, 1921; S1, 'Bohr's Institute for Theoretical Physics']. He escaped occupied Denmark in 1943 and joined the atomic bomb projects, then argued for international control of atomic weapons [S2, 1943 paragraph; S3, paragraph 10].

## Contribution and impact

The 1913 atom, with stationary states and radiation only in jumps between them [S1, 'Bohr model of the atom' paragraph]; complementarity (1927) [S2, Como 1927 paragraph]; the compound-nucleus model and the role of uranium-235 in fission (1936–39) [S2, 'other major contributions'; S3, paragraph 7].

## Childhood and education

His father was an atheist who "exposed his son to the state religion so that he would not feel himself different from other boys" [S4, p. 20]. His mother, from an assimilated Jewish family, "was not religious and agreed to baptizing her children" [S4, p. 20]. After a period of taking religion seriously he realised "that Christian theology was nonsense" [S4, p. 20; S7, Session I]. His interest in physics was "awakened while I was still in school, largely owing to the influence of my father" [S2, school paragraph].

## Adult working worldview

To make sure the wedding could not be religious, he and Margrethe "formally resigned from the Danish State Church" [S4, p. 20], on 16 April 1912 by Halvorson's chronology [S5, 1912]. Heilbron, citing Margrethe Bohr's 1963 interview, writes that for a time he wanted to write a book on religion "to warn people that it was not true" [S4, p. 24, n. 30]; in that interview his widow said he still spoke of such a book in his last autumn [S7, Session I]. Loose notes on Kierkegaard: "I, who do not feel in any way united with, and even less, bound to a God" [S8, pp. 159–160, via S11]. To his fiancée he ruled out begging from "fancied powers infinitely stronger than himself" [S12, pp. 138–139]. On nature: complementarity is "a rational generalization of the very ideal of causality" [S10, p. 41]; "any violation of physico-chemical laws in organic life … would be excluded" [S9, p. 297]. Scores: A 4 at 0.5 (alt BELOW); B 4 at 0.7 (alt 3); C 4 and D 4 at 0.5; E below threshold; mid_basin below threshold.

## Heritage (context only)

Danish, with a Jewish maternal family; christened Lutheran [S2, paragraph 1; S4, p. 20]. Context only.

## Timing

First lasting contribution 1913, at 28 [S1]. His rejection of theology predates the major work [S4, p. 20].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form partly present (postulates and consequences); no circle.

## Open questions

- Primary check of Aaserud & Heilbron (2013) pp. 110, 159–160; primary fiancée "fancied powers" letter; Witham's unnamed published religion essay.

## Research log

- 2026-10-02: Read Britannica (Aaserud, first page), MacTutor, the Nobel biography, Heilbron (2013, PDF), the Halvorson chronology and the AIP interview with Margrethe Bohr (Session I, Wayback copy). Bohr's Collected Works and essays, Pais and Aaserud & Heilbron are lending-only on archive.org and were not read. Quotations checked against the downloaded texts.
- 2026-10-24 (D1 deepen, queue #60): Read Bohr, Causality and Complementarity (Phil. Sci. 1937 PDF, S9); Atomic Physics and Human Knowledge Discussion with Einstein (Wiley 1958 PDF, S10, p. 41); Wikipedia EN religion notes quoting Aaserud & Heilbron 2013 pp. 159–160 and p. 110 (S8 via S11); Witham 2006 pp. 138–139 via Celebrity Atheist List (S12); Ingeniøren 2015 Aaserud interview (S13). Aaserud & Heilbron 2013 book still IA lending-only — not opened. A 4@0.5 corroborated; B 4@0.7 written_profession corroborated. Chart-moving NO.
