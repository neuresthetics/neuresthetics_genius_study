---
record:
  record_type: person
  schema_version: "1.1"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, second batch: physical science 1600–1950)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (second batch, RUNBOOK §1 order). Basics from Britannica, the Jewish Women's Archive encyclopedia (Rife) and a 2024 Society of Catholic Scientists article (Moritz), which quotes her letters through Schweighofer (2013) and Sime (1997). Baptized Protestant (Lutheran) in 1908; no own statement of Christian doctrine found. primary_system BELOW_THRESHOLD (CHRIST candidate). B 4 and D 3 at 0.5; A, C, E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit, batch 2 (two blind runs at e648145). Finding #99/#100: the JWA baptism sentence is paragraph 7 counting the In Brief summary as 1 (the sixth body paragraph after it), not paragraph 3; locators fixed and the counting rule stated in S2. Finding #106: the 1942 quotation joins two fragments around 'she exclaimed', now marked with [...]. Finding #107: Sime's translation reads 'deep awe and joy' (Sime 1996, p. 375), seen as reproduced on todayinsci.com (new S5); S3's 'deep joy and awe' is noted as a variant. Finding #95: D_authority 3 (0.5) → BELOW_THRESHOLD, because the exception rested on S3's paraphrase about Bible verses, not her own words (§6). primary_system (BELOW_THRESHOLD) and mid_basin (BELOW_THRESHOLD) unchanged. Not reviewed."}

identity:
  id: meitner-lise
  display_name: "Lise Meitner"
  roster:
    canonical_name: "Lise Meitner"
    rank: 52
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: physics
    field_bucket: physics
  full_name: {value: "Lise Meitner", certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}, {source: S2, locator: "heading"}], how_known: "Sources agree. The full given name (Elise) was not in the sources read."}
  native_name: {value: "Lise Meitner (German)", certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}], how_known: "Austrian; same spelling."}
  aliases:
    - {name: "Lise-Meitner", kind: "roster alias"}
    - {name: "Meitner-Lise", kind: "roster alias"}

basics:
  birth:
    date: {value: "1878-11-07", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S2, locator: "paragraph 3"}], how_known: "Two sources agree."}
    place: {value: "Vienna", modern_name: "Vienna, Austria", polity_then: "Austria-Hungary", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S2, locator: "paragraph 3"}], how_known: "Two sources agree."}
  death:
    date: {value: "1968-10-27", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S2, locator: "final paragraph"}], how_known: "Two sources agree."}
    place: {value: "Cambridge, England", modern_name: "Cambridge, United Kingdom", polity_then: "United Kingdom", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S2, locator: "final paragraph"}], how_known: "Two sources agree."}
  first_lasting_contribution_year: {value: 1918, certainty: 0.7, cites: [{source: S1, locator: "paragraph 2 (protactinium-231, which they named)"}, {source: S3, locator: "note 6 (Hahn and Meitner, Physikalische Zeitschrift 19, 1918)"}], how_known: "Protactinium with Hahn; the year comes from the 1918 paper cited in S3. Earlier radioactivity work (from 1907) is not singled out as lasting in the sources, so 0.7."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "paragraph 2"}], how_known: "From first_lasting_contribution_year (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts ('Vienna, Austria-Hungary [now in Austria]')"}], how_known: "Austria is Western Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "paragraphs 2–3"}, {source: S2, locator: "paragraphs 5–12"}], how_known: "Protactinium, isomerism and beta decay were done in Berlin (Germany, Western Europe). The physical explanation of fission (1938–39) was done in Sweden (Northern Europe). Two regions, so 0.7.", alternatives: [{value: "Northern Europe", cites: [{source: S2, locator: "fission paragraphs"}], note: "Stockholm and Kungälv, 1938–1960."}]}
  sex_as_recorded: {value: "female", certainty: 1.0, cites: [{source: S2, locator: "opening"}], how_known: "As the sources record it."}
  languages_of_work: {value: [German, English], certainty: 0.7, cites: [{source: S3, locator: "notes 6, 18"}], how_known: "German papers (1918) and English (Nature, 1939)."}
  occupations: {value: [physicist, "university lecturer", "head of physics section, Kaiser Wilhelm Institute for Chemistry"], certainty: 1.0, cites: [{source: S2, locator: "paragraphs 5–8"}], how_known: "JWA."}

contribution:
  fields: {value: ["nuclear physics", radioactivity], certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}, {source: S2, locator: "opening"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Isolation of the isotope protactinium-231 (with Hahn), which they named", year: "1918", kind: discovery, lasting: "a named element isotope", certainty: 1.0, cites: [{source: S1, locator: "paragraph 2"}, {source: S3, locator: "note 6"}], how_known: "Two sources."}
    - {value: "Physical explanation of nuclear fission (with Otto Frisch), and the term 'fission'", year: "1939", kind: theory, lasting: "foundation of nuclear energy", certainty: 1.0, cites: [{source: S1, locator: "paragraph 3"}, {source: S2, locator: "fission paragraphs"}, {source: S3, locator: "note 18 (Nature 143, 1939)"}], how_known: "Three sources."}
  evidence_of_impact:
    - {value: "Element meitnerium named in her honour", kind: "named after them", certainty: 1.0, cites: [{source: S1, locator: "paragraph 4"}], how_known: "Britannica."}
    - {value: "Enrico Fermi Award 1966 (with Hahn and Strassmann)", kind: "honours in lifetime", certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}, {source: S2, locator: "final paragraph"}], how_known: "Two sources."}
    - {value: "Einstein called her 'our Madame Curie'", kind: "assessment by a later major figure", certainty: 0.7, cites: [{source: S2, locator: "paragraph 2"}], how_known: "JWA."}
  major_works:
    - {value: "Disintegration of Uranium by Neutrons: a New Type of Nuclear Reaction (with O. R. Frisch), Nature 143", year: 1939, kind: "paper or paper series", certainty: 1.0, cites: [{source: S3, locator: "note 18"}], how_known: "Full reference in S3."}
  honours:
    - {value: "Enrico Fermi Award", year: 1966, certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}], how_known: "Britannica."}
  definition_fit: {value: "clearly meets", rationale: "Co-discoverer of protactinium; the physics of fission.", certainty: 1.0, cites: [{source: S1, locator: "paragraphs 2–3"}], how_known: "Sources agree."}

childhood:
  family_religion: {value: "Jewish by registration; assimilated parents who did not practise Judaism", certainty: 1.0, cites: [{source: S2, locator: "paragraph 3"}, {source: S3, locator: "Meitner section ('enrolled all their children in the Jewish Community')"}], how_known: "Two sources."}
  family_religious_practice: {value: "No Jewish practice; a liberal, largely secular education in a culturally Christian setting", certainty: 0.7, cites: [{source: S2, locator: "paragraph 3"}, {source: S3, locator: "Meitner section"}], how_known: "Two sources (S3 not peer reviewed)."}
  parents_and_household:
    - {value: "Father, Philipp Meitner, a lawyer from a Moravian family", name: "Philipp Meitner", role: father, certainty: 1.0, cites: [{source: S2, locator: "paragraph 3"}], how_known: "JWA."}
    - {value: "Mother, Hedwig Skovran", name: "Hedwig Meitner (née Skovran)", role: mother, certainty: 1.0, cites: [{source: S2, locator: "paragraph 3"}], how_known: "JWA."}
  household_circumstances: {value: "Eight children; the father insisted daughters get the same education as sons", certainty: 1.0, cites: [{source: S2, locator: "paragraphs 3–4"}], how_known: "JWA."}
  schooling:
    - {value: "Private tutoring, because girls could not attend the boys' Gymnasium; university entrance examination", stage: tutor, certainty: 1.0, cites: [{source: S2, locator: "paragraph 4"}], how_known: "JWA."}
    - {value: "University of Vienna, with Boltzmann; doctorate 1906", stage: university, years: "1901–1906", certainty: 1.0, cites: [{source: S2, locator: "paragraphs 4–5"}, {source: S1, locator: "paragraph 2"}], how_known: "Two sources."}
  early_mathematics: {value: "other", note: "'an early propensity for mathematics' (S2); level not stated", certainty: 0.7, cites: [{source: S2, locator: "paragraph 4"}], how_known: "JWA."}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [German], certainty: 0.7, cites: [{source: S2, locator: "paragraph 3"}], how_known: "Viennese family."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1906–1960", certainty: 1.0, cites: [{source: S1, locator: "paragraphs 2–4"}], how_known: "Doctorate to retirement."}
  nominal_affiliations:
    - {value: "Baptized Protestant (Evangelical/Lutheran) in 1908; member of St.-Annenkirche, Berlin-Dahlem, and later of the Lutheran congregation of Engelbrektskyrkan, Stockholm", years: "1908–1968", role: member, certainty: 0.7, cites: [{source: S2, locator: "paragraph 7 ('In 1908 on a visit to Vienna…')"}, {source: S3, locator: "Sweden section"}], how_known: "Baptism in two sources; congregations from S3 only. S3 spells the church 'Engelbrechtskyrkan'."}
  self_described_science_religion_relation:
    value: "Awe at life and at the natural order is 'also a part of being religious'; science teaches 'truth and objectivity' and the 'deep awe and joy that the natural order of things brings to the true scientist' (1953 lecture)."
    certainty: 0.5
    cites: [{source: S3, locator: "Sweden section, notes 20, 31"}, {source: S5, locator: "1953 UNESCO lecture entry"}]
    how_known: "A 1955 letter and a 1953 lecture, both in English translation: the letter quoted by a non-peer-reviewed article (through Schweighofer 2013), the lecture in Sime's translation (1996, p. 375) as reproduced by S5 and S3, so 0.5."
  primary_system:
    value: BELOW_THRESHOLD
    cites: [{source: S3, locator: "Sweden section"}, {source: S2, locator: "paragraph 7"}]
    how_known: "Church membership is recorded, but membership is not ideology. The only words of hers read speak of awe and respect for life as religious, without doctrine; S3 says she 'always felt uncomfortable when confronted with dogmatic concepts'. Nothing reaches a code at 0.5."
    note: "Candidate: CHRIST (Lutheran member; S3 reports that 'some bible verses accompanied her throughout her life', and a friend called her 'thoroughly Lutheran'). Needs her own words on Christ, scripture or creed (Schweighofer 2013; Sime 1997)."
  secondary_system: {value: UNKNOWN, how_known: "No second system in S1–S3."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Leading candidate, not coded: baptism and membership only, plus a friend's description. CHRIST is a sourced system file.", cites: [{source: S3, locator: "Sweden section"}]}
    - {code: JUDA, reason: "Rejected: she formally left the Jewish community in 1908. Heritage is never a code.", cites: [{source: S2, locator: "paragraph 7 ('In 1908 on a visit to Vienna…')"}]}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "No statement about God read.", note: "Gap: Sime 1997; Schweighofer 2013."}
    B_cause:
      value: 4
      basis: scholarly_reconstruction
      certainty: 0.5
      cites: [{source: S1, locator: "paragraphs 2–3"}, {source: S3, locator: "note 31 (1953 lecture)"}]
      how_known: "Coder's reading of her working science (P6), with one translated lecture passage on 'the natural order of things', so 0.5."
      rationale: "Scored on her account of nature (P6). Her working physics (radioactive decay, beta spectra, fission from E = mc² and nuclear forces) admits no special cases, and her 1953 lecture speaks of 'the natural order of things'. Her phrase 'the miracle of life' (1942 letter) is wonder, not an exemption from law. No miracle or petition appears."
    C_ledger: {value: BELOW_THRESHOLD, how_known: "Nothing on judgement or afterlife read."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "Her own words read (1953 lecture, 1955 letter) praise science's 'truth and objectivity' and call awe at life religious, but say nothing about revelation, scripture or church authority. The only evidence on the revelation side is S3's paraphrase that she 'acknowledged that some bible verses accompanied her throughout her life', and S3's own reading that she 'always felt uncomfortable when confronted with dogmatic concepts'. Axes are scored from the person's own words (§6), so below 0.5.", note: "Was 3 at 0.5 (lens audit, batch 2, finding #95). Same treatment as Fermi and Curie. Gap: Sime 1996; Schweighofer 2013, for her own words on the Bible."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Scored on the world's order (P7). Her physics is universal, but nothing read addresses favour for a group in events.", note: "Same treatment as Fermi: not scored from working science alone."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD and B_cause is only 0.5, under the P4 test's 0.7 bar."}
  statements:
    - text: "cannot tell us what 'life' means, and I am referring not only to the complexity of human life but the simplest living organism. In front of this, we can only stand in awe and respect, in the same way as when seeing a wonderful landscape or when listening to a beautiful piece of music — is this not also a part of being religious?"
      cites: [{source: S3, locator: "Sweden section, note 20"}]
      date: "1955-02-22"
      context: "Letter to Carola Allers (her sister), on what physics and chemistry cannot tell us. English translation in S3, from Schweighofer 2013, p. 277."
      axes: [D_authority]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-02
    - text: "If respect for the miracle of life were deeper, [...] world history would look very different!"
      cites: [{source: S3, locator: "Sweden section, note 21"}]
      date: "1942-06-02"
      context: "Letter to Max von Laue, on Albert Schweitzer's reverence for life. S3 prints it as 'If respect for the miracle of life were deeper,' she exclaimed, 'world history would look very different!'"
      axes: [B_cause]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-02
    - text: "Science makes people reach selflessly for truth and objectivity; it teaches people to accept reality, with wonder and admiration, not to mention the deep awe and joy that the natural order of things brings to the true scientist."
      cites: [{source: S5, locator: "1953 UNESCO lecture entry"}, {source: S3, locator: "closing paragraph, note 31"}]
      date: "1953-03-30"
      context: "Lecture to the Austrian UNESCO Commission, printed in Atomenergie und Frieden (1953), pp. 23–24. English as translated by Sime, Lise Meitner: A Life in Physics (University of California Press, 1996), p. 375, seen only as reproduced on todayinsci.com (S5), not in the book."
      note: "S3 transposes the words to 'deep joy and awe' and dates Sime's book 1997; the wording here follows S5's reproduction of Sime."
      axes: [B_cause, D_authority]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-02
  changes_over_life:
    - {value: "Left the Jewish community and was baptized Protestant", year: "1908", certainty: 1.0, cites: [{source: S2, locator: "paragraph 7 ('In 1908 on a visit to Vienna…')"}, {source: S3, locator: "Meitner section"}], how_known: "Two sources."}
  coder_notes: "The English quotations are S3's renderings of German letters via Schweighofer; S3 is a Catholic scientists' society article by a biochemist, not peer reviewed. CHRIST is a sourced system file. Washington Post's online excerpt of Sime's chapter 1 (on the 1908 baptisms) did not download."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Assimilated Viennese Jewish family", certainty: 1.0, cites: [{source: S2, locator: "paragraph 3"}], how_known: "JWA."}
  religious_heritage_by_birth: {value: "Jewish (registered with the Vienna Jewish community)", certainty: 1.0, cites: [{source: S2, locator: "paragraphs 3, 7"}, {source: S3, locator: "Meitner section"}], how_known: "Two sources."}
  baptism_or_initiation: {value: "Baptized Protestant (Evangelical) in Vienna, 1908, aged about 30", certainty: 1.0, cites: [{source: S2, locator: "paragraph 7 ('In 1908 on a visit to Vienna…')"}, {source: S3, locator: "Meitner section"}], how_known: "Two sources."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not given in S1–S3."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1918–1939", certainty: 1.0, cites: [{source: S1, locator: "paragraphs 2–3"}], how_known: "Protactinium to fission."}
  age_at_first_lasting_contribution: {value: 39, certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}, {source: S3, locator: "note 6"}], how_known: "Born November 1878; the 1918 protactinium paper."}
  first_evidence_of_lio_type_views: {value: "Letter on reverence for the 'miracle of life'", year: 1942, certainty: 0.5, cites: [{source: S3, locator: "note 21"}], how_known: "Earliest dated statement read; weak as an LIO view."}
  lio_views_relative_to_major_work: {value: "unclear", rationale: "Statements read are 1942–1955, after the major work, and are not clearly LIO-type.", certainty: 0.5, cites: [{source: S3, locator: "notes 20, 21, 31"}], how_known: "Dates."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "paragraph 4"}], how_known: "Experimental physicist; nothing on deductive form read."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "paragraph 4"}], how_known: "Nothing read."}
  circle_present: {value: "no", rationale: "No God-Nature identity in anything read.", certainty: 0.5, cites: [{source: S3, locator: "Sweden section"}], how_known: "Absence in the sources read."}
  reading: "As belief, not finding: form unclear, no circle. The record does not test H1."
  notes: ""

institutions:
  - {value: "Kaiser Wilhelm Institute for Chemistry, Berlin", role: "head of the physics section", years: "1918–1938", kind: employer, certainty: 1.0, cites: [{source: S2, locator: "paragraph 7"}, {source: S3, locator: "Berlin section"}], how_known: "Two sources."}
  - {value: "Nobel Institute of Physics, Stockholm", role: "researcher", years: "1938–1940s", kind: employer, certainty: 0.7, cites: [{source: S2, locator: "Stockholm paragraph"}], how_known: "JWA."}
collaborators:
  - {value: "Otto Hahn", relation: collaborator, note: "thirty-year research partner; sole 1944 Nobel laureate for fission", certainty: 1.0, cites: [{source: S1, locator: "paragraphs 2–3"}, {source: S2, locator: "paragraphs 2, 5"}], how_known: "Two sources."}
  - {value: "Otto Robert Frisch", relation: family, note: "nephew; co-author of the fission explanation", certainty: 1.0, cites: [{source: S1, locator: "paragraph 3"}, {source: S2, locator: "fission paragraphs"}], how_known: "Two sources."}
  - {value: "Max Planck", roster_id: planck-max, relation: "mentor or employer", note: "invited her to Berlin; she was his assistant", certainty: 1.0, cites: [{source: S2, locator: "paragraphs 5–6"}], how_known: "JWA."}
  - {value: "Ludwig Boltzmann", relation: teacher, certainty: 1.0, cites: [{source: S2, locator: "paragraph 4"}], how_known: "JWA."}
  - {value: "Niels Bohr", roster_id: bohr-niels, relation: other, note: "organized her escape; confirmed fission", certainty: 1.0, cites: [{source: S2, locator: "escape and fission paragraphs"}], how_known: "JWA."}

review:
  roster_status_reason: {value: "Core in v7.1 (F 5) and v8 (F 5, all five models).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 52"}], how_known: "Study roster."}
  controversies:
    - {value: "Left out of the 1944 Nobel Prize for fission, awarded to Hahn alone", certainty: 1.0, cites: [{source: S1, locator: "paragraph 3"}, {source: S2, locator: "paragraph 2"}], how_known: "Two sources."}
  data_quality_flags:
    - "Worldview quotations are English translations reached through a non-peer-reviewed article (S3) citing Schweighofer (2013) and Sime (1997)."
    - "Region of work splits between Berlin and Sweden."
  open_questions:
    - "Read Sime, Lise Meitner: A Life in Physics (1997), and Schweighofer (2013) on her conversion and faith, for her own words on God."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "\"Lise Meitner.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Lise-Meitner."
    url: "https://www.britannica.com/biography/Lise-Meitner"
    accessed: 2026-10-02
    reliability_note: "Unsigned editorial article."
    used_for: [identity, basics, contribution, worldview, timing, collaborators, review]
  - id: S2
    type: tertiary
    kind: encyclopedia
    author: "Patricia Rife"
    citation: "Rife, Patricia. \"Lise Meitner.\" Shalvi/Hyman Encyclopedia of Jewish Women, Jewish Women's Archive. https://jwa.org/encyclopedia/article/meitner-lise."
    url: "https://jwa.org/encyclopedia/article/meitner-lise"
    accessed: 2026-10-02
    reliability_note: "Signed encyclopedia article by a Meitner biographer. Paragraphs counted from the start of the article text, with the 'In Brief' summary as paragraph 1 (so the baptism, 'In 1908 on a visit to Vienna…', is paragraph 7, the sixth paragraph after In Brief)."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, lane_b, institutions, collaborators]
  - id: S3
    type: secondary
    kind: "journal article"
    author: "Berta M. Moritz"
    year: 2024
    citation: "Moritz, Berta M. \"Three pioneering women in science: a story of science, faith, and the power of friendship.\" Society of Catholic Scientists, 1 April 2024. https://catholicscientists.org/articles/three-pioneering-women-in-science-a-story-of-science-faith-and-the-power-of-friendship/."
    url: "https://catholicscientists.org/articles/three-pioneering-women-in-science-a-story-of-science-faith-and-the-power-of-friendship/"
    accessed: 2026-10-02
    reliability_note: "Society article with full notes, by a biochemist; not peer reviewed and written from a faith perspective. Used for her congregations and translated quotations, each with its note."
    used_for: [basics, contribution, childhood, worldview, heritage, timing, institutions]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
  - id: S5
    type: tertiary
    kind: other
    author: "Ian Ellis (Today in Science History)"
    citation: "\"Lise Meitner Quotes.\" Today in Science History (todayinsci.com). Quotation from the 1953 Austrian UNESCO Commission lecture, citing Atomenergie und Frieden (1953), pp. 23–24, trans. Ruth Lewin Sime, Lise Meitner: A Life in Physics (Berkeley: University of California Press, 1996), p. 375. https://todayinsci.com/M/Meitner_Lise/MeitnerLise-Quotations.htm."
    url: "https://todayinsci.com/M/Meitner_Lise/MeitnerLise-Quotations.htm"
    accessed: 2026-10-02
    reliability_note: "Quotation site that gives full references; used only to check the wording of Sime's translation, which was not read in the book."
    used_for: [worldview]
---

# Lise Meitner

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Lise Meitner (1878–1968), Austrian-born physicist, co-discovered protactinium-231 with Otto Hahn and, with Otto Frisch, gave the physical explanation of nuclear fission (1939) [S1, paragraphs 2–3]. Born to assimilated Jewish parents, she was baptized Protestant in 1908 [S2, paragraphs 3, 7]. Her recorded words speak of awe at life and the natural order but not of doctrine, so her system is below threshold; B 4 at 0.5, the other axes below threshold.

## Life and work

Privately tutored, she entered the University of Vienna at 23 and studied with Boltzmann; from 1907 she worked in Berlin with Planck and Hahn, led the physics section of the Kaiser Wilhelm Institute for Chemistry, and fled to Sweden in 1938 [S2, paragraphs 4–12].

## Contribution and impact

Protactinium (1918) and the physics of fission (1939); meitnerium is named for her [S1, paragraphs 2–4].

## Childhood and education

Her parents "were assimilated Viennese Jews, who did not practice Judaism" [S2, paragraph 3]; her father insisted his daughters be educated like his sons [S2, paragraph 4].

## Adult working worldview

A Lutheran church member in Berlin and Stockholm [S3, Sweden section]. In a 1955 letter she asked whether awe at life "is this not also a part of being religious?" [S3, note 20]. In 1953 she spoke of "the deep awe and joy that the natural order of things brings to the true scientist" [S5; S3, note 31]. Scores: B 4 (0.5); A, C, D, E below threshold; mid_basin below threshold.

## Heritage (context only)

Assimilated Viennese Jewish family; baptized Protestant at about 30 [S2, paragraphs 3, 7]. Context only.

## Timing

First lasting contribution 1918, at 39 [S1; S3, note 6]. Statements read are from 1942–1955.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form unclear; no circle.

## Open questions

- Sime 1997 and Schweighofer 2013 for her own words on God.

## Research log

- 2026-10-02: Read Britannica, the JWA article (Rife) and the 2024 Society of Catholic Scientists article (Moritz). MacTutor has no full Meitner biography (short page). The Washington Post excerpt of Sime's first chapter did not download. Quotations checked against S3's text.
