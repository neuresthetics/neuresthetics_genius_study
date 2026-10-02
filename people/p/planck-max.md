---
record:
  record_type: person
  schema_version: "1.1"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, second batch: physical science 1600–1950)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (second batch, RUNBOOK §1 order). Basics from Britannica (Stuewer, first page), MacTutor and the Nobel biography. Worldview from the German text of 'Religion und Naturwissenschaft' (1937 lecture; copy of the 1938 second edition), the English Where Is Science Going? (1933, Murphy) and Heilbron (1986) as quoted on the web. Coded DEISM at 0.5 (PANT and CHRIST named). A 2 (0.7), B 4 (0.7), D 2 (0.7), E 3 (0.7); C BELOW_THRESHOLD. mid_basin TODO: the P4 test has no branch for A_locus = 2. Not reviewed."}

identity:
  id: planck-max
  display_name: "Max Planck"
  roster:
    canonical_name: "Max Planck"
    rank: 57
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: physics
    field_bucket: physics
  full_name: {value: "Max Karl Ernst Ludwig Planck", certainty: 1.0, cites: [{source: S1, locator: "early life paragraph"}, {source: S3, locator: "paragraph 1"}], how_known: "Two sources agree."}
  native_name: {value: "Max Planck (German)", certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}], how_known: "Same spelling."}
  aliases:
    - {name: "Max-Planck", kind: "roster alias"}
    - {name: "Planck-Max", kind: "roster alias"}

basics:
  birth:
    date: {value: "1858-04-23", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S3, locator: "paragraph 1"}], how_known: "Two sources agree."}
    place: {value: "Kiel", modern_name: "Kiel, Germany", polity_then: "Kiel, Schleswig (as Britannica gives it); German Confederation", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts ('Kiel, Schleswig [Germany]')"}, {source: S3, locator: "paragraph 1 ('Kiel, Germany')"}], how_known: "The town is certain. The polity in 1858 is not stated beyond Britannica's 'Schleswig'; Kiel lay in Holstein, so the polity label is 0.7 (flag)."}
  death:
    date: {value: "1947-10-04", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S3, locator: "final paragraph"}], how_known: "Two sources agree."}
    place: {value: "Göttingen", modern_name: "Göttingen, Germany", polity_then: "British occupation zone of Germany", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S3, locator: "final paragraph"}], how_known: "Two sources agree on the town; the occupation zone is the coder's label."}
  first_lasting_contribution_year: {value: 1900, certainty: 0.7, cites: [{source: S1, locator: "'What were Max Planck's contributions?'; blackbody paragraphs"}, {source: S3, locator: "paragraph 4"}], how_known: "The quantum of action and the radiation law (October–December 1900). His earlier thermodynamics papers from 1879 (S3, paragraph 3) could count, so 0.7; both years fall in the same era."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "blackbody paragraphs"}], how_known: "Either candidate year falls in 1850 to 1949 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts ('Kiel, Schleswig [Germany]')"}], how_known: "Germany is Western Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Western Europe", certainty: 1.0, cites: [{source: S1, locator: "university paragraph"}, {source: S3, locator: "paragraph 2"}], how_known: "Munich, Kiel and Berlin (Germany)."}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S3, locator: "paragraph 1"}], how_known: "As the sources record it."}
  languages_of_work: {value: [German], certainty: 1.0, cites: [{source: S3, locator: "paragraph 5 (Annalen der Physik; Thermodynamik; Theorie der Wärmestrahlung)"}], how_known: "Nobel biography."}
  occupations: {value: ["theoretical physicist", "university professor", "permanent secretary of the Prussian Academy of Sciences", "president of the Kaiser Wilhelm Society"], certainty: 1.0, cites: [{source: S3, locator: "paragraph 2"}, {source: S2, locator: "Kaiser Wilhelm Gesellschaft paragraph"}], how_known: "Two sources."}

contribution:
  fields: {value: ["theoretical physics", thermodynamics, "quantum theory"], certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}, {source: S3, locator: "paragraphs 3–4"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Planck's radiation law and the quantum of action (Planck's constant h); energy of a resonator comes in discrete quanta hν", year: "1900", kind: theory, lasting: "foundation of quantum theory", certainty: 1.0, cites: [{source: S1, locator: "blackbody paragraphs"}, {source: S3, locator: "paragraphs 3–4"}], how_known: "Two sources."}
    - {value: "Work on entropy and the second law, thermoelectricity and dilute solutions", year: "1879–1897", kind: theory, lasting: "Thermodynamik (1897), a standard text", certainty: 0.7, cites: [{source: S3, locator: "paragraphs 3, 5"}, {source: S2, locator: "doctorate and habilitation paragraphs"}], how_known: "Nobel biography and MacTutor; how lasting is the coder's reading, 0.7."}
  evidence_of_impact:
    - {value: "Max Planck Medal, with Planck as first recipient; the Kaiser Wilhelm Society renamed the Max Planck Society", kind: "named after them", certainty: 1.0, cites: [{source: S2, locator: "Kaiser Wilhelm Gesellschaft paragraph"}], how_known: "MacTutor."}
    - {value: "Nobel Prize in Physics 1918", kind: "honours in lifetime", certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}, {source: S2, locator: "Nobel paragraph"}], how_known: "Two sources."}
  major_works:
    - {value: "Vorlesungen über Thermodynamik", year: 1897, kind: book, certainty: 1.0, cites: [{source: S3, locator: "paragraph 5"}], how_known: "Nobel biography."}
    - {value: "Vorlesungen über die Theorie der Wärmestrahlung", year: 1906, kind: book, certainty: 1.0, cites: [{source: S3, locator: "paragraph 5"}], how_known: "Nobel biography."}
  honours:
    - {value: "Nobel Prize in Physics", year: 1918, certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}, {source: S3, locator: "heading"}], how_known: "Two sources."}
    - {value: "Copley Medal of the Royal Society", year: 1928, certainty: 1.0, cites: [{source: S3, locator: "paragraph 6"}], how_known: "Nobel biography."}
  definition_fit: {value: "clearly meets", rationale: "Originated quantum theory.", certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}], how_known: "Sources agree."}

childhood:
  family_religion: {value: "Protestant (family of theologians; grandfather and great-grandfather were professors of theology at Göttingen)", certainty: 0.7, cites: [{source: S2, locator: "paragraph 1"}, {source: S1, locator: "early life paragraph ('devotion to church and state')"}], how_known: "The theologian forebears and the church tradition are stated; the denomination (Lutheran) is not named in the sources read, so 0.7."}
  family_religious_practice: {value: "A 'long family tradition of devotion to church and state'", certainty: 0.7, cites: [{source: S1, locator: "early life paragraph"}, {source: S2, locator: "paragraph 1 ('utmost respect for the institutions of state and church')"}], how_known: "Two sources, both general."}
  parents_and_household:
    - {value: "Father, Julius Wilhelm Planck, professor of constitutional law at Kiel, then Munich (and later Göttingen per S3)", name: "Julius Wilhelm Planck", role: father, certainty: 1.0, cites: [{source: S2, locator: "paragraph 1"}, {source: S3, locator: "paragraph 1"}], how_known: "Two sources."}
    - {value: "Mother, Emma Patzig, his father's second wife", name: "Emma Planck (née Patzig)", role: mother, certainty: 1.0, cites: [{source: S2, locator: "paragraph 1"}, {source: S3, locator: "paragraph 1"}], how_known: "Two sources."}
  household_circumstances: {value: "Sixth child of a large academic family; moved to Munich in 1867", certainty: 1.0, cites: [{source: S1, locator: "early life paragraph"}, {source: S2, locator: "paragraph 1"}], how_known: "Two sources."}
  schooling:
    - {value: "Elementary school in Kiel; Maximilian Gymnasium, Munich, where Hermann Müller stirred his interest in physics and mathematics", stage: "grammar or secondary school", years: "to 1874", certainty: 1.0, cites: [{source: S1, locator: "early life paragraph"}, {source: S2, locator: "schooling paragraphs"}], how_known: "Two sources."}
    - {value: "Universities of Munich and Berlin; doctorate at Munich, July 1879, aged 21, on the second law of thermodynamics; habilitation 1880", stage: university, years: "1874–1880", certainty: 1.0, cites: [{source: S1, locator: "university paragraph"}, {source: S2, locator: "doctorate and habilitation paragraphs"}, {source: S3, locator: "paragraph 2"}], how_known: "Three sources."}
  early_mathematics: {value: "other", note: "Excelled in all subjects; interest in physics and mathematics from his Gymnasium teacher (S1)", certainty: 0.7, cites: [{source: S1, locator: "early life paragraph"}], how_known: "Britannica; level not stated."}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure:
    - {value: "The law of conservation of energy, learned at the Gymnasium, was the 'first instance of an absolute in nature that impressed Planck deeply'", certainty: 1.0, cites: [{source: S1, locator: "blackbody section, first paragraph"}], how_known: "Britannica."}
  key_early_reading:
    - {value: "Rudolf Clausius's writings on thermodynamics", certainty: 1.0, cites: [{source: S1, locator: "university paragraph"}, {source: S3, locator: "paragraph 3"}], how_known: "Two sources."}
  childhood_mentors:
    - {value: "Hermann Müller, Gymnasium teacher", certainty: 1.0, cites: [{source: S1, locator: "early life paragraph"}], how_known: "Britannica."}
  languages_in_childhood: {value: [German], certainty: 1.0, cites: [{source: S1, locator: "early life paragraph"}], how_known: "German family and schooling."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1879–1947", certainty: 1.0, cites: [{source: S3, locator: "paragraphs 2, 9"}], how_known: "Doctorate to death; he lectured on religion and science into old age."}
  nominal_affiliations:
    - {value: "Protestant church tradition; Heilbron's account shows him denying a rumoured conversion to Catholicism in 1947", years: "1858–1947", role: member, certainty: 0.5, cites: [{source: S1, locator: "early life paragraph"}, {source: S6, locator: "Heilbron quotation"}], how_known: "Membership itself (Lutheran, and the commonly reported church-elder role) was not found in the sources read; family tradition and the 1947 denial only, so 0.5."}
  self_described_science_religion_relation:
    value: "Religion and natural science 'mutually supplement and condition each other'; both need belief in God, for religion at the start and for science at the end of all thought; science is for knowing, religion for acting. Belief in nature-miracles must retreat before science."
    certainty: 1.0
    cites: [{source: S4, locator: "copy pp. 2, 11–13"}, {source: S7, locator: "1937 lecture transcription"}, {source: S5, locator: "pp. 159, 168"}]
    how_known: "His own public lecture (1937) and book (1933 English edition)."
  primary_system:
    value: DEISM
    basis: written_profession
    certainty: 0.5
    cites: [{source: S4, locator: "copy pp. 2, 6, 11–12"}, {source: S6, locator: "Heilbron quotation"}]
    how_known: "His 1937 lecture affirms a God reached by reason through the lawful 'world order' and says belief in nature-miracles must vanish; creeds and symbols are of human origin. Heilbron calls this 'Planck's deism' and reports a 1947 reply denying belief 'in a personal God, let alone a Christian God'. Heilbron was read only through a web quotation (S6), and two codes are named, so 0.5, below the 0.7 cap. DEISM is a sourced system file (draft)."
    rationale: "DEISM's test: own writing affirms a God known by reason from order and rejects miracles and the absolute authority of church teaching. Planck meets the first two directly (S4, pp. 2, 11–12) and the third in part (symbols are human, never absolute, S4 p. 6). Alternatives: PANT, because the lecture 'identifies' the world order of natural science with the God of religion and calls the deity 'wesensgleich' (consubstantial) with the power acting by natural law (part 1 of the PANT test is close but the lecture also has God 'ruling over Nature', so not clearly met); CHRIST, because he stayed in the Protestant church, valued religious symbols and cited 'the teachings of Jesus' (blog, not used). DEISM's own do-not-use note (God identified with the universe) is why certainty is held at 0.5."
  secondary_system: {value: UNKNOWN, how_known: "No second system settled; PANT and CHRIST are named alternatives."}
  candidate_codes_considered:
    - {code: DEISM, reason: "Chosen at 0.5: a God reached by reason through the world order, no miracles, creeds of human origin; Heilbron's label.", cites: [{source: S4, locator: "copy pp. 2, 11–12"}, {source: S6, locator: "Heilbron quotation"}]}
    - {code: PANT, reason: "Named alternative: the world order of science and the God of religion are to be identified. Not chosen: the same lecture keeps God 'ruling over Nature' and holding the world 'in his almighty hand'. PANT is a sourced system file.", cites: [{source: S4, locator: "copy pp. 11–12"}]}
    - {code: CHRIST, reason: "Named alternative: Protestant family and church tradition. Not chosen: he denied a personal and a Christian God (S6) and expected belief in miracles to vanish. CHRIST is a sourced system file.", cites: [{source: S1, locator: "early life paragraph"}, {source: S6, locator: "Heilbron quotation"}]}
  lio_axes:
    A_locus:
      value: 2
      basis: written_profession
      certainty: 0.7
      cites: [{source: S4, locator: "copy pp. 6, 11–12"}, {source: S6, locator: "Heilbron quotation"}]
      how_known: "His own lecture holds both sides. Contested, so 0.7."
      rationale: "English phrases from S4 are the coder's glosses. Mixed. Toward the LIO pole: God is to be identified with 'the world order of natural science' and is consubstantial with the power acting by natural law (copy p. 11); he did not believe in a personal God (S6). Toward the other pole: God 'rules the world' independently of belief and holds it 'in his almighty hand' (copy p. 6), and the 'omnipotent Reason' rules 'over Nature' (copy p. 11). Alternatives: 3 if the identification sentence is taken as his settled view; 1 on Heilbron's deist reading."
    B_cause:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S5, locator: "p. 159; p. 168"}, {source: S4, locator: "copy pp. 2, 7"}]
      how_known: "Published book and public lecture state it directly; 0.7 because the free-will passage is a named alternative."
      rationale: "Scored on his account of nature (P6), which is his working physics and his philosophy of it. 'Chance and miracle in the absolute sense are fundamentally excluded from science' (1933); religion must not oppose 'the sequence of cause and effect in all external phenomena' (1933); all physical events 'without exception' reduce to mechanical or electrical processes, and belief in nature-miracles must retreat step by step (1937). No miracle or answered petition appears. Alternative: 3, if the individual ego, where 'every causal method of research is inapplicable' (1933, p. 161), is read as an exemption; he treats it as a limit of self-observation, not an uncaused event, so 4."
    C_ledger: {value: BELOW_THRESHOLD, how_known: "Nothing read on judgement, afterlife or moral reckoning. He puts ethics outside science and gives religion the guidance of action (copy p. 12), which is not a ledger.", note: "Gap: Scientific Autobiography and Other Papers (1949) and Heilbron 1986 not read in full."}
    D_authority:
      value: 2
      basis: written_profession
      certainty: 0.7
      cites: [{source: S4, locator: "copy pp. 6, 12"}, {source: S7, locator: "1937 lecture transcription ('Natural science wants man to learn, religion wants him to act')"}]
      how_known: "Coder's reading of his lecture; 0.7."
      rationale: "English phrases from S4 are the coder's glosses. Two domains, each with its own authority, so D 2 (the guide's same-pattern rule). For knowledge, only sense data and measurement count, and belief in miracles must yield to science. For action and ethics, the guide is 'the definite and clear direction' gained from 'the direct link with God' (copy p. 12), a non-rational authority. He also says even 'the holiest symbol is of human origin' (copy p. 6). Alternative 3 if the direct link with God is read as conscience rather than revelation."
    E_scope:
      value: 3
      basis: written_profession
      certainty: 0.7
      cites: [{source: S4, locator: "copy pp. 6, 11"}, {source: S7, locator: "1937 lecture transcription"}]
      how_known: "Coder's reading of his lecture; one named alternative, so 0.7."
      rationale: "English phrases from S4 are the coder's glosses. Scored on the world's order (P7). The rational world order is one 'to which Nature and humanity are subject' (copy p. 11), and God holds 'believers and unbelievers' alike in his hand (copy p. 6): the same rules for all. The stated limited exception: the truly religious 'feel secure under the protection of the Almighty against all dangers of life' (copy p. 6), a protection kept for believers. Alternative 4, if that protection is a felt security and not favour in events."
  mid_basin: {value: TODO, how_known: "A_locus = 2 at 0.7 and B_cause = 4 at 0.7. Both axes are scored at 0.7 but A falls between the branches: the P4 test has no branch for A_locus = 2 (CODING_GUIDE §6).", note: "A deist code would usually pass (METHOD §1.1); here the A score is 2 because his God is not personal and is identified with the world order. Needs a decision, not more evidence."}
  statements:
    - text: "Schritt für Schritt muß der Glaube an Naturwunder vor der stetig und sicher voranschreitenden Wissenschaft zurückweichen"
      cites: [{source: S4, locator: "copy p. 2"}]
      date: "1937-05"
      context: "'Step by step, belief in nature-miracles must retreat before steadily and surely advancing science'; he adds that it must come to an end sooner or later. Coder's English gloss."
      axes: [B_cause, D_authority]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "Nichts hindert uns also, und unser nach einer einheitlichen Weltanschauung verlangender Erkenntnistrieb fordert es, die beiden überall wirksamen und doch geheimnisvollen Mächte, die Weltordnung der Naturwissenschaft und den Gott der Religion, miteinander zu identifizieren."
      cites: [{source: S4, locator: "copy p. 11"}, {source: S7, locator: "1937 lecture transcription (Gaynor's English)"}]
      date: "1937-05"
      context: "The PANT-leaning sentence: the world order of natural science and the God of religion are to be identified. The original breaks 'Weltanschau-ung' across a line."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "in das Walten der über die Natur regierenden allmächtigen Vernunft"
      cites: [{source: S4, locator: "copy p. 11"}]
      date: "1937-05"
      context: "'into the workings of the omnipotent Reason that rules over Nature' (coder's gloss): the transcendent-leaning phrase."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "daß er von Ewigkeit her die ganze Welt, Gläubige und Ungläubige, in seiner allmächtigen Hand hält"
      cites: [{source: S4, locator: "copy p. 6"}]
      date: "1937-05"
      context: "The religious person's answer, which he goes on to reconcile with science: God holds the whole world, believers and unbelievers, in his almighty hand from eternity."
      axes: [A_locus, E_scope]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "sondern nur die bestimmte und klare Weisung, die wir aus der unmittelbaren Verbindung mit Gott gewinnen"
      cites: [{source: S4, locator: "copy p. 12"}]
      date: "1937-05"
      context: "On action: long reflection cannot guide decisions, 'only the definite and clear direction that we gain from the direct link with God' (coder's gloss)."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "Though chance and miracle in the absolute sense are fundamentally excluded from science"
      cites: [{source: S5, locator: "p. 159"}]
      date: "1933"
      context: "Where Is Science Going?, Murphy's translation; he goes on to the popular belief in miracle and magic."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "so long as it does not make the mistake of opposing its own dogmas to the fundamental law upon which scientific research is based, namely the sequence of cause and effect in all external phenomena."
      cites: [{source: S5, locator: "p. 168"}]
      date: "1933"
      context: "The scientist 'must recognize the value of religion as such, no matter what may be its forms', on this condition."
      axes: [B_cause, D_authority]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "He had always been deeply religious, Planck said, but he did not believe \"in a personal God, let alone a Christian God."
      cites: [{source: S6, locator: "Heilbron quotation"}]
      date: "1947"
      context: "Heilbron's report of Planck's reply to an engineer who asked about a rumoured conversion to Catholicism; read only as quoted on a blog (Wikipedia gives Heilbron p. 198)."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-02
  changes_over_life: []
  coder_notes: "DEISM, PANT and CHRIST are sourced system files. The 1937 lecture is quoted from the German (a web copy of the 1938 second edition; 'copy p.' is the copy's own page numbering, not checked against the printed edition). English glosses are the coder's, cross-checked against an incomplete blog transcription of Gaynor's translation (S7). Heilbron (S6) was not read directly. The 1913 letter on 'the teachings of Jesus' quoted on the S7 blog (via Heilbron p. 67) was not used."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "German academic family of jurists and theologians", certainty: 1.0, cites: [{source: S2, locator: "paragraph 1"}], how_known: "MacTutor."}
  religious_heritage_by_birth: {value: "Protestant", certainty: 0.7, cites: [{source: S2, locator: "paragraph 1"}, {source: S1, locator: "early life paragraph"}], how_known: "Theologian forebears at Göttingen and family devotion to the church; denomination not named."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated in S1–S7."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated in S1–S7."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1879–1906", certainty: 0.7, cites: [{source: S3, locator: "paragraphs 2–5"}], how_known: "Thermodynamics papers to the radiation book."}
  age_at_first_lasting_contribution: {value: 42, certainty: 0.7, cites: [{source: S1, locator: "Quick Facts; blackbody paragraphs"}], how_known: "Born April 1858; the quantum paper of December 1900. 21 if the 1879 thesis is counted."}
  first_evidence_of_lio_type_views: {value: "Where Is Science Going? (German original 1932): chance and miracle excluded from science", year: 1932, certainty: 0.5, cites: [{source: S5, locator: "p. 159"}], how_known: "Earliest text read; the 1933 English edition. Britannica quotes an earlier autobiographical statement that the laws of reasoning match the laws of nature (date not given)."}
  lio_views_relative_to_major_work: {value: "after major work", rationale: "The texts read are from 1932–1947, after the quantum work; earlier views not read.", certainty: 0.5, cites: [{source: S5, locator: "p. 159"}, {source: S4, locator: "copy p. 2"}], how_known: "Dates of the texts read."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "university and blackbody paragraphs"}], how_known: "Theoretical physicist working from absolute laws (thermodynamics); no deductive geometric form noted."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "early life paragraph"}], how_known: "Nothing read."}
  circle_present: {value: "partly", rationale: "The 1937 lecture identifies the world order of natural science with the God of religion, but also has God ruling over Nature; not a full God-Nature circle.", certainty: 0.5, cites: [{source: S4, locator: "copy p. 11"}], how_known: "Coder's reading of one lecture."}
  reading: "As belief, not finding: form unclear, circle partly present. The record does not test H1."
  notes: ""

institutions:
  - {value: "University of Munich", role: "Privatdozent", years: "1880–1885", kind: employer, certainty: 1.0, cites: [{source: S3, locator: "paragraph 2"}], how_known: "Nobel biography."}
  - {value: "University of Kiel", role: "associate professor of theoretical physics", years: "1885–1889", kind: employer, certainty: 1.0, cites: [{source: S3, locator: "paragraph 2"}, {source: S1, locator: "university paragraph"}], how_known: "Two sources."}
  - {value: "University of Berlin", role: "professor (successor to Kirchhoff)", years: "1889–1926", kind: employer, certainty: 0.7, cites: [{source: S3, locator: "paragraph 2"}, {source: S2, locator: "Berlin paragraph"}], how_known: "Retirement 1926 (S3) or 1 October 1927 (S2)."}
  - {value: "Prussian Academy of Sciences", role: "member 1894; permanent secretary 1912", years: "1894–", kind: "academy or learned society", certainty: 1.0, cites: [{source: S3, locator: "paragraph 2"}], how_known: "Nobel biography."}
  - {value: "Kaiser Wilhelm Society", role: president, years: "1930–1937; 1945–1946", kind: other, certainty: 0.7, cites: [{source: S2, locator: "Kaiser Wilhelm Gesellschaft paragraph"}, {source: S3, locator: "paragraph 2"}], how_known: "MacTutor gives 1930–1937 and 1945–46; the Nobel biography gives the end year 1937 only."}
collaborators:
  - {value: "Gustav Kirchhoff", relation: teacher, note: "teacher in Berlin; Planck succeeded him", certainty: 1.0, cites: [{source: S3, locator: "paragraphs 2–3"}], how_known: "Nobel biography."}
  - {value: "Hermann von Helmholtz", relation: "mentor or employer", note: "teacher, later venerated mentor and colleague", certainty: 1.0, cites: [{source: S1, locator: "university paragraph"}, {source: S3, locator: "paragraph 2"}], how_known: "Two sources."}
  - {value: "Albert Einstein", roster_id: einstein-albert, relation: influenced, note: "light quanta (1905) built on the quantum hypothesis", certainty: 1.0, cites: [{source: S1, locator: "quantum-reception paragraph"}], how_known: "Britannica."}
  - {value: "Ludwig Boltzmann", relation: "influenced by", note: "Planck adopted his statistical reading of the second law to derive the radiation law", certainty: 1.0, cites: [{source: S1, locator: "blackbody paragraphs"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v7.1 (F 4) and v8 (F 5, all five models).", certainty: 0.7, cites: [{source: S8, locator: "roster.csv, rank 57"}], how_known: "Study roster."}
  controversies:
    - {value: "Stayed in Germany as head of German science under the Nazi government while opposing some of its policies", certainty: 1.0, cites: [{source: S3, locator: "paragraph 7"}, {source: S2, locator: "Nazi period paragraphs"}], how_known: "Two sources."}
  data_quality_flags:
    - "Britannica places Kiel in 'Schleswig'; Kiel was in Holstein."
    - "Retirement from Berlin: 1926 (Nobel biography) vs 1927 (MacTutor). First marriage: 1885 (Nobel) vs 31 March 1887 (MacTutor)."
    - "MacTutor says 'In 1945 his other son was executed' after describing Erwin's execution; its own text has Karl killed in 1916, so this reads as an error in MacTutor."
    - "Heilbron (1986) read only through a blog quotation; the page (198) is from Wikipedia's citation."
    - "The German lecture text is a web copy of the 1938 edition; page numbers are the copy's."
  open_questions:
    - "Read Heilbron, The Dilemmas of an Upright Man (1986), pp. 182–198, and Scientific Autobiography and Other Papers (1949) for the 1947 letter and his church role."
    - "Settle how mid_basin treats A_locus = 2 (no P4 branch)."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Roger H. Stuewer"
    citation: "Stuewer, Roger H. \"Max Planck.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Max-Planck."
    url: "https://www.britannica.com/biography/Max-Planck"
    accessed: 2026-10-02
    reliability_note: "Signed article by a historian of physics; first page only. Paragraphs cited by topic."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: tertiary
    kind: encyclopedia
    author: "J. J. O'Connor and E. F. Robertson"
    citation: "O'Connor, J. J., and E. F. Robertson. \"Max Karl Ernst Ludwig Planck.\" MacTutor History of Mathematics Archive, University of St Andrews. https://mathshistory.st-andrews.ac.uk/Biographies/Planck/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Planck/"
    accessed: 2026-10-02
    reliability_note: "Signed biography; paragraphs cited by topic. One internal error noted (second son's execution)."
    used_for: [basics, contribution, childhood, heritage, institutions, review]
  - id: S3
    type: tertiary
    kind: "institutional page"
    author: "Nobel Foundation"
    year: 1967
    citation: "\"Max Planck – Biographical.\" From Nobel Lectures, Physics 1901–1921. Amsterdam: Elsevier, 1967. NobelPrize.org. https://www.nobelprize.org/prizes/physics/1918/planck/biographical/."
    url: "https://www.nobelprize.org/prizes/physics/1918/planck/biographical/"
    accessed: 2026-10-02
    reliability_note: "Short official biography; paragraphs counted from the start of the text."
    used_for: [identity, basics, contribution, childhood, worldview, timing, institutions, collaborators, review]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "Max Planck"
    year: 1938
    citation: "Planck, Max. Religion und Naturwissenschaft: Vortrag gehalten im Baltikum (Mai 1937). 2nd unchanged ed. Leipzig: Johann Ambrosius Barth, 1938. Web copy: https://alkastar.de/medien/pdf/max-planck.pdf."
    url: "https://alkastar.de/medien/pdf/max-planck.pdf"
    accessed: 2026-10-02
    reliability_note: "Typed copy of the 1938 edition on a private website (13 numbered pages); text checked line by line for the passages quoted, page numbers are the copy's. Planck died in 1947, so the German text is public domain."
    used_for: [worldview, timing, lane_b]
  - id: S5
    type: primary
    kind: "published work by the subject"
    author: "Max Planck"
    year: 1933
    citation: "Planck, Max. Where Is Science Going? Translated and edited by James Murphy, with a preface by Albert Einstein. London: George Allen & Unwin, 1933. Digital Library of India scan, Internet Archive in.ernet.dli.2015.222321."
    url: "https://archive.org/details/in.ernet.dli.2015.222321"
    accessed: 2026-10-02
    reliability_note: "OCR text of the first English edition; page numbers from the running heads. Murphy's translation of Planck's essays (German 1932)."
    used_for: [worldview, timing]
  - id: S6
    type: secondary
    kind: other
    author: "J. L. Heilbron (as quoted on the Space Theology blog)"
    year: 1986
    citation: "Heilbron, J. L. The Dilemmas of an Upright Man: Max Planck as Spokesman for German Science. Berkeley: University of California Press, 1986 (p. 198 per Wikipedia's citation). Quoted in \"John .L. Heilbron about Max Planck and God,\" Space Theology (blog), 13 February 2012. http://spacetheology.blogspot.com/2012/02/max-planck-about-god.html."
    url: "http://spacetheology.blogspot.com/2012/02/max-planck-about-god.html"
    accessed: 2026-10-02
    reliability_note: "Scholarly biography read only through a blog's quotation (with typos such as 'Plankc's'); the same passage appears in Wikipedia's citation of Heilbron. Treat as a secondary quotation."
    used_for: [worldview, review]
  - id: S7
    type: secondary
    kind: other
    author: "Intelectual Believers (anonymous blog)"
    year: 2014
    citation: "\"Max Planck: Religion & Science.\" Intelectual Believers (blog), 25 October 2014. Incomplete transcription of Planck's 1937 lecture in Frank Gaynor's English translation (Scientific Autobiography and Other Papers). http://intelectualbelievers.blogspot.com/2014/10/max-planck-religion-science.html."
    url: "http://intelectualbelievers.blogspot.com/2014/10/max-planck-religion-science.html"
    accessed: 2026-10-02
    reliability_note: "Anonymous, incomplete transcription with typing errors; used only to cross-check the coder's English glosses of S4."
    used_for: [worldview]
  - id: S8
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
---

# Max Planck

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Max Planck (1858–1947), German theoretical physicist, found the radiation law and the quantum of action in 1900 and won the 1918 Nobel Prize in Physics [S1, opening paragraph; S3, paragraph 4]. In his 1937 lecture "Religion und Naturwissenschaft" he identified "die Weltordnung der Naturwissenschaft und den Gott der Religion" and said belief in nature-miracles must retreat before science [S4, copy pp. 2, 11]. Heilbron calls this deism [S6]. Coded DEISM at 0.5 (PANT and CHRIST named). A 2, B 4, D 2, E 3 (all 0.7); C below threshold; mid_basin TODO (no P4 branch for A = 2).

## Life and work

Doctorate at Munich in 1879 at 21; professor at Kiel (1885) and Berlin (1889), permanent secretary of the Prussian Academy (1912) and president of the Kaiser Wilhelm Society [S1, university paragraph; S3, paragraph 2; S2].

## Contribution and impact

Planck's radiation law and constant h (1900), the foundation of quantum theory [S1; S3, paragraphs 3–4].

## Childhood and education

His family had a "long family tradition of devotion to church and state" [S1, early life paragraph]; his grandfather and great-grandfather were professors of theology at Göttingen [S2, paragraph 1].

## Adult working worldview

He wrote that "chance and miracle in the absolute sense are fundamentally excluded from science" [S5, p. 159] and that religion must not oppose "the sequence of cause and effect in all external phenomena" [S5, p. 168]. In 1937 God stands "für die eine am Anfang, für die andere am Ende alles Denkens" [S4, copy p. 12]. Heilbron reports that he did not believe "in a personal God, let alone a Christian God" [S6]. Scores: A 2, B 4, D 2, E 3 (0.7 each); C below threshold.

## Heritage (context only)

Protestant academic family [S1; S2]. Context only.

## Timing

First lasting contribution 1900, at 42 [S1]. The worldview texts read are from 1932–1947.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form unclear; circle partial (God identified with the world order but also ruling over Nature).

## Open questions

- Heilbron (1986) and Scientific Autobiography and Other Papers (1949), for the 1947 letter and church membership.
- mid_basin for A_locus = 2 needs a decision.

## Research log

- 2026-10-02: Read Britannica (Stuewer, first page), MacTutor, the Nobel biography, the German 1937 lecture (web copy of the 1938 edition), Where Is Science Going? (1933, DLI scan on archive.org), and two blogs (Heilbron quotation; partial Gaynor transcription). Scientific Autobiography (1949) is lending-only on archive.org; the socraticdictum.com PDF of the Gaynor translation failed to download. Quotations checked against the downloaded texts.
