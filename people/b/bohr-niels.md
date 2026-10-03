---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 4
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, third batch: physical science 1600–1950)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (third batch, RUNBOOK §1 order). Basics from Britannica (Aaserud, first page), MacTutor and the Nobel biography. Worldview from J. L. Heilbron, 'The Mind that Created the Bohr Atom' (Séminaire Poincaré 2013), which quotes Bohr's 1911–12 letters from Aaserud & Heilbron (2013), and from the AIP interview with Margrethe Bohr (1963, session I; reported speech). Rejected Christian theology in adolescence; left the Danish State Church in April 1912. primary_system BELOW_THRESHOLD (ATHE leading candidate, AGNOS named; both stub files). B 4, C 4, D 4, all at 0.5 (scholarly reconstruction); A, E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Rechecked under decision P8 (recorded interviews; schema 1.2): the AIP interview is Margrethe Bohr's reported speech and paraphrase only, so it scores nothing on its own; it only supports C_ledger, which rests on Heilbron. No score changed. Schema 1.1 → 1.2."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit, batch 3 (two blind runs at d9903b7). #1: primary_system how_known no longer quotes S7 (AIP no-quotation notice); it now paraphrases Margrethe Bohr and says the 'did not think of himself as anything' answer was to Kuhn's question whether he thought of himself as a Jew, not a question about religion; the 'not true' wording is Heilbron's (S4, p. 24). #5: D_authority 4 at 0.5 kept; the 'warn people that it was not true' item is now labelled Margrethe Bohr's 1963 account as reported by Heilbron (S4, p. 24, n. 30), not Bohr's words; p. 34 (truth in literature and science) dropped as D support and its statement untagged from D. D already at the 0.5 floor, so no certainty change; nothing downstream changes (mid_basin BELOW_THRESHOLD, A not scored). Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Stage 3 lens-audit rulings applied to the batch's other records (OPEN_DECISIONS P14–P28, v8's picks, 2026-10-02). Schema 1.2 → 1.3. One reliable source caps a fact at 0.7; derived fields take the lowest certainty of their inputs; kind lists (P21: research institute, school stage and run_by, scholarly edition); first lasting year per P13/P23, no coder's-choice wording. Full before → after list: reports/stage3_rulings_changes.csv. Not reviewed."}

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
  working_years: {value: "1906–1962", certainty: 0.7, cites: [{source: S3, locator: "paragraphs 3–12"}], how_known: "From the prize essay to his death."}
  nominal_affiliations:
    - {value: "Christened in the Lutheran Church of Denmark; formally resigned from it in April 1912 so that his wedding could not be religious; civil wedding 1 August 1912", years: "c. 1898–1912", role: "former member", certainty: 1.0, cites: [{source: S4, locator: "p. 20"}, {source: S5, locator: "1912, 'Apr 16'"}, {source: S2, locator: "'christened in the Christian Church'"}], how_known: "Heilbron (both Niels and Margrethe 'formally resigned from the Danish State Church') and the Halvorson chronology (16 April 1912) agree. Margrethe Bohr recalled that the children were christened at about 13 or 14 (S7); Heilbron says only that their mother agreed to it."}
  self_described_science_religion_relation:
    value: "None stated in published form in what was read. In 1911–12 letters he called his conviction 'that everything that is of any value is true' almost 'my religion', and set 'so-called scientific truths' beside the truths of literature as of 'a somewhat different kind'; in explaining his rejection of religion he wrote that life 'would be so infinitely trivial if I thought I could understand it'."
    certainty: 0.5
    cites: [{source: S4, locator: "pp. 32, 34"}]
    how_known: "Letters known only as quoted in English by Heilbron (secondary quotation), so 0.5."
  primary_system:
    value: BELOW_THRESHOLD
    cites: [{source: S4, locator: "pp. 20, 24"}, {source: S7, locator: "Session I (religion)"}]
    how_known: "Positive evidence of rejection of religion, but not of which non-theist position. Heilbron: he realised 'Christian theology was nonsense' (p. 20), and, citing Margrethe Bohr's 1963 interview (n. 30), that for a time he wanted to write a book on religion 'to warn people that it was not true' (p. 24). In that interview (S7, paraphrased because AIP restricts quotation) his widow said that he regretted the role religion played and held throughout the years she knew him that people should not build their lives on what is untrue; asked by Kuhn whether he thought of himself as a Jew, she said he did not, nor as anything else, which is about Jewish identity, not a religious self-description. ATHE needs positive naturalism and AGNOS explicit suspension (v7.1); the sources reject Christianity and religion in general but give no statement on God's existence or on naturalism as such."
    note: "Candidates: ATHE (leading) or AGNOS. Aaserud & Heilbron, Love, Literature and the Quantum Atom (2013), pp. 73–80 and 110, reportedly describe 'well-fortified atheism'; not read (seen only via a secondary summary), so not used. Same treatment as Curie (lens audit, batch 2, finding #108)."
  secondary_system: {value: UNKNOWN, how_known: "No second system in S1–S7."}
  candidate_codes_considered:
    - {code: ATHE, reason: "Leading candidate, not coded (BELOW_THRESHOLD): theology judged 'nonsense' (S4, p. 20) and religion 'not true' (Heilbron's wording, S4, p. 24, reporting Margrethe Bohr's 1963 account), but no statement of positive naturalism read. ATHE is a stub system file (flag).", cites: [{source: S4, locator: "pp. 20, 24"}]}
    - {code: AGNOS, reason: "Candidate, not coded: his stress on what human beings cannot understand (S4, p. 32) could suggest suspension, but it is about knowledge in general, and he called religion untrue rather than unknowable. AGNOS is a stub system file (flag).", cites: [{source: S4, locator: "p. 32"}]}
    - {code: CHRIST, reason: "Rejected: christening and nominal Lutheran upbringing only; he left the church in 1912 on his own convictions. Church membership is never a code.", cites: [{source: S4, locator: "p. 20"}, {source: S5, locator: "1912"}]}
    - {code: JUDA, reason: "Rejected: Jewish maternal heritage only; the family did not attend synagogue and he did not think of himself as a Jew (S7). Heritage is never a code.", cites: [{source: S7, locator: "Session I (Jewish background)"}]}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "No statement placing or denying God was found; the evidence is about Christian theology and religion, not about a divine locus.", note: "Gap: Aaserud & Heilbron (2013) and Bohr's essays (Atomic Physics and Human Knowledge) were not read (lending-only scans)."}
    B_cause:
      value: 4
      basis: scholarly_reconstruction
      certainty: 0.5
      cites: [{source: S1, locator: "'Bohr model of the atom' paragraph"}, {source: S4, locator: "pp. 30, 49"}]
      how_known: "Scored on his working science (P6), as reconstructed by Heilbron; his own essays on causality were not read, so 0.5."
      rationale: "Scored on his account of nature (P6). His atom runs on stated rules (stationary states fixed by the quantum of action; radiation only in jumps between them), and on Heilbron's account he placed radioactivity where particles originate 'spontaneously, by chance' (S4, p. 49). No miracle, petition or reserved exemption appears. Alternative named: 3, if the quantum jump that 'not even a Newton could follow' (S4, p. 49) is read as a standing exception to causal description; it is read here as a limit of description inside a law-governed theory, not an exemption from law."
    C_ledger:
      value: 4
      basis: scholarly_reconstruction
      certainty: 0.5
      cites: [{source: S4, locator: "p. 20"}, {source: S7, locator: "Session I (religion)"}]
      how_known: "Heilbron's reconstruction from family letters and interviews; no statement in Bohr's own published words. Rechecked under decision P8 (2026-10-02): the score rests on Heilbron (S4); the AIP interview (S7) is his widow's reported speech and can only be paraphrased, so it only supports the score, which P8 allows. Unchanged."
      rationale: "Impersonal consequence or none. Heilbron reports that he questioned 'not only the doctrine but also the concept' of salvation ('what could it mean to have a saved soul?') and concluded that 'Christian theology was nonsense' (S4, p. 20); Margrethe Bohr said he held religion untrue all the years she knew him (S7). No judgement, afterlife or personal reckoning is affirmed anywhere read."
    D_authority:
      value: 4
      basis: scholarly_reconstruction
      certainty: 0.5
      cites: [{source: S4, locator: "pp. 20, 24 (n. 30)"}]
      how_known: "Heilbron's reconstruction (scholarly_reconstruction, 0.5): one letter phrase of Bohr's quoted by him (secondary quotation, p. 20) and one item of reported speech, Margrethe Bohr's 1963 account as Heilbron gives it (p. 24, n. 30). Lens audit batch 3 (#5): p. 34 dropped as support, since it is about truth in literature and science, not about which authority decides. 0.5 is already the lowest scored level."
      rationale: "Observation and reason outrank revelation. On Heilbron's account he reached his rejection of theology by his own reasoning, and he took his father's smile to show 'that I too could think' (S4, p. 20, his letter of 1911). By his widow's 1963 account, as Heilbron reports it, he wanted for a time to write a book on religion to warn people 'that it was not true' (S4, p. 24, n. 30; reported speech, not his words). No authority above reason is acknowledged in anything read."
    E_scope: {value: BELOW_THRESHOLD, how_known: "Scored on the world's order (P7). Nothing read addresses favour for a group in events; not scored from working science alone (same treatment as Fermi and Curie). The rejection of salvation is scored on C."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD, so the P4 test cannot be applied (B_cause is also only at 0.5)."}
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
  coder_notes: "ATHE and AGNOS are stub system files (flag). All quotations of Bohr are from his Danish letters in the English translation used by Heilbron (from Aaserud & Heilbron 2013), so they are secondary quotations. The AIP transcript (S7) is reported speech (his widow and, in one passage, apparently Rosenfeld) and carries an AIP no-quotation notice, so it is paraphrased, not quoted at length, and it is never used as a written profession. Rechecked under decision P8 (2026-10-02): P8's recorded_interview basis covers only the person's own first-person words, so it does not apply to S7 (other people's words about Bohr); and as a paraphrase-only source S7 scores nothing on its own. It supports C_ledger, which rests on Heilbron, and appears in primary_system (BELOW_THRESHOLD), nominal_affiliations and changes_over_life as a fact source. No score changed."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Danish; mother's family Jewish (the Adlers), assimilated", certainty: 1.0, cites: [{source: S2, locator: "paragraph 1"}, {source: S4, locator: "p. 20"}], how_known: "Two sources."}
  religious_heritage_by_birth: {value: "Lutheran (father's side; children christened) and Jewish (mother's family)", certainty: 1.0, cites: [{source: S4, locator: "p. 20"}, {source: S2, locator: "'christened in the Christian Church'"}], how_known: "Two sources."}
  baptism_or_initiation: {value: "Christened in the Danish Lutheran church, at about 13 or 14 by Margrethe Bohr's recollection", certainty: 0.7, cites: [{source: S2, locator: "'christened in the Christian Church'"}, {source: S4, locator: "p. 20"}, {source: S7, locator: "Session I (religious training)"}], how_known: "The christening is in three sources; the age is in one recollection only."}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1913–1939", certainty: 0.7, cites: [{source: S2, locator: "1913 papers; 'other major contributions'"}, {source: S3, locator: "paragraphs 5–8"}], how_known: "From the atomic model (1913) to the fission work (1939), as the two sources date them."}
  age_at_first_lasting_contribution: {value: 27, certainty: 1.0, cites: [{source: S1, locator: "Quick Facts; 'Bohr model of the atom' paragraph"}], how_known: "Born October 1885; the trilogy appeared in 1913."}
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
    - "S7 is the AIP transcript as archived by the Wayback Machine (the live AIP page now redirects to a repository that refused the fetch); AIP's notice restricts quotation, so it is paraphrased."
  open_questions:
    - "Read Aaserud & Heilbron, Love, Literature and the Quantum Atom (2013), pp. 72–80, 110, 161, for the full letters and the 'atheism' characterisation."
    - "Read Bohr's essays (Atomic Physics and Human Knowledge, 1958; Essays 1958–1962) for any published statement on religion or causality."
    - "Heisenberg's Der Teil und das Ganze reports Bohr's 1927 remarks on religion; reported speech, reconstructed decades later, not used."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Finn Aaserud"
    citation: "Aaserud, Finn. \"Niels Bohr.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Niels-Bohr."
    url: "https://www.britannica.com/biography/Niels-Bohr"
    accessed: 2026-10-02
    reliability_note: "Signed article by the former director of the Niels Bohr Archive; first page only. Sections cited by heading."
    used_for: [identity, basics, contribution, institutions, timing, lane_b]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "J J O'Connor and E F Robertson"
    citation: "O'Connor, J. J., and E. F. Robertson. \"Niels Henrik David Bohr.\" MacTutor History of Mathematics, University of St Andrews. https://mathshistory.st-andrews.ac.uk/Biographies/Bohr_Niels/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Bohr_Niels/"
    accessed: 2026-10-02
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
    reliability_note: "Scholarly essay by a leading Bohr historian, quoting Bohr's 1911–12 letters in English from Aaserud & Heilbron (2013) and Margrethe Bohr's 1963 interview. Page numbers are the journal's printed pages (running heads)."
    used_for: [basics, childhood, worldview, heritage, timing, lane_b, collaborators]
  - id: S5
    type: secondary
    kind: other
    author: "Hans Halvorson"
    citation: "Halvorson, Hans. \"Niels Bohr chronology.\" https://hanshalvorson.dk/bohr/chronology.html."
    url: "https://hanshalvorson.dk/bohr/chronology.html"
    accessed: 2026-10-02
    reliability_note: "Chronology by a philosopher of physics; used only for the date of leaving the church (1912, 'Apr 16'), which agrees with Heilbron's undated account."
    used_for: [worldview, timing]
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
    kind: "archive record"
    author: "Margrethe Bohr, Aage Bohr and Léon Rosenfeld, interviewed by Thomas S. Kuhn"
    year: 1963
    citation: "Interview with Margrethe Bohr by Thomas S. Kuhn, Aage Bohr, and Leon Rosenfeld, Copenhagen, 23 January 1963, Session I. Niels Bohr Library & Archives, American Institute of Physics. Archived copy of the AIP page: https://web.archive.org/web/20140911200150/http://www.aip.org/history/ohilist/4514_1.html."
    url: "https://web.archive.org/web/20140911200150/http://www.aip.org/history/ohilist/4514_1.html"
    accessed: 2026-10-02
    reliability_note: "Official AIP transcript (as archived in 2014); reported speech by his widow, son and a colleague. Some speaker labels are missing in the scanned typescript. AIP restricts quotation without permission, so the record paraphrases. Located by topic within Session I."
    used_for: [childhood, worldview, heritage, timing]
---

# Niels Bohr

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Niels Bohr (1885–1962), Danish physicist, built the quantum model of the atom in 1913, proposed complementarity in 1927 and won the 1922 Nobel Prize in Physics [S1, opening; S2, Como 1927 paragraph; S3, paragraph 6]. Christened Lutheran in a non-religious home, he rejected Christian theology in adolescence and left the Danish State Church in 1912 [S4, p. 20; S5, 1912]. System below threshold (ATHE leading, AGNOS named); B 4, C 4, D 4, all at 0.5; A and E below threshold; mid_basin below threshold.

## Life and work

Born in Copenhagen to the physiologist Christian Bohr and Ellen Adler [S3, paragraph 1]. He studied at the University of Copenhagen (doctorate 1911), worked with J. J. Thomson at Cambridge and with Rutherford at Manchester (1911–12), held a Manchester lectureship (1914–16) and took the Copenhagen chair of theoretical physics in 1916 [S3, paragraphs 2–6]. He directed the Institute for Theoretical Physics from its opening in 1921 to his death [S2, 1921; S1, 'Bohr's Institute for Theoretical Physics']. He escaped occupied Denmark in 1943 and joined the atomic bomb projects, then argued for international control of atomic weapons [S2, 1943 paragraph; S3, paragraph 10].

## Contribution and impact

The 1913 atom, with stationary states and radiation only in jumps between them [S1, 'Bohr model of the atom' paragraph]; complementarity (1927) [S2, Como 1927 paragraph]; the compound-nucleus model and the role of uranium-235 in fission (1936–39) [S2, 'other major contributions'; S3, paragraph 7].

## Childhood and education

His father was an atheist who "exposed his son to the state religion so that he would not feel himself different from other boys" [S4, p. 20]. His mother, from an assimilated Jewish family, "was not religious and agreed to baptizing her children" [S4, p. 20]. After a period of taking religion seriously he realised "that Christian theology was nonsense" [S4, p. 20; S7, Session I]. His interest in physics was "awakened while I was still in school, largely owing to the influence of my father" [S2, school paragraph].

## Adult working worldview

To make sure the wedding could not be religious, he and Margrethe "formally resigned from the Danish State Church" [S4, p. 20], on 16 April 1912 by Halvorson's chronology [S5, 1912]. Heilbron, citing Margrethe Bohr's 1963 interview, writes that for a time he wanted to write a book on religion "to warn people that it was not true" [S4, p. 24, n. 30]; in that interview his widow said he still spoke of such a book in his last autumn [S7, Session I]. In 1912 he wrote that he could "almost call it my religion, that I think that everything that is of any value is true" [S4, p. 34]. Scores: B 4, C 4, D 4 (all 0.5); A, E below threshold.

## Heritage (context only)

Danish, with a Jewish maternal family; christened Lutheran [S2, paragraph 1; S4, p. 20]. Context only.

## Timing

First lasting contribution 1913, at 27 [S1]. His rejection of theology predates the major work [S4, p. 20].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form partly present (postulates and consequences); no circle.

## Open questions

- Aaserud & Heilbron (2013) for the letters in full; Bohr's own essays for any published statement on religion.

## Research log

- 2026-10-02: Read Britannica (Aaserud, first page), MacTutor, the Nobel biography, Heilbron (2013, PDF), the Halvorson chronology and the AIP interview with Margrethe Bohr (Session I, Wayback copy). Bohr's Collected Works and essays, Pais and Aaserud & Heilbron are lending-only on archive.org and were not read. Quotations checked against the downloaded texts.
