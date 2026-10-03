---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 7
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, second batch: physical science 1600–1950)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (second batch, RUNBOOK §1 order). Basics from Britannica (Stuewer, first page), MacTutor and the Nobel biography. Worldview from the German text of 'Religion und Naturwissenschaft' (1937 lecture; copy of the 1938 second edition), the English Where Is Science Going? (1933, Murphy) and Heilbron (1986) as quoted on the web. Coded DEISM at 0.5 (PANT and CHRIST named). A 2 (0.7), B 4 (0.7), D 2 (0.7), E 3 (0.7); C BELOW_THRESHOLD. mid_basin TODO: the P4 test has no branch for A_locus = 2. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit, batch 2 (two blind runs at e648145). Pages: 'heiligste Symbol' is copy p. 5 and 'wesensgleich' copy p. 12. Framing: 'regiert er die Welt' is a question he poses and the 'almighty hand / Gläubige und Ungläubige' passage is the religious person's answer; A and E rationales no longer treat them as his own views. Glosses that are Gaynor's wording are marked 'cross-checked with Gaynor'. Heilbron: 'deism' unconfirmed in the book; Wikipedia's p. 198 is the 2000 Harvard printing; S6 citation fixed and the label no longer used as support. New S9 (Gladigow 1986) confirms the 1947 letter in German (citing Herneck 1952) and reports a 1945 letter (Bertholet 1948) that seems to show a more personal God; added as counter-evidence on A and on DEISM vs CHRIST (no certainty change: A stays 2 at 0.7 with alternative 1 strengthened; DEISM already at 0.5). Finding #127: DEISM rationale rewritten for 'einzig und allein Sache des Glaubens' and the non-rational direct link with God. Finding #132: E_scope 3 → 4 (0.7). Finding #135: nominal affiliation role 'member' → 'other' (membership unsourced). Two statements added (p. 6 faith-alone sentence; p. 11 world order). mid_basin unchanged (TODO, A = 2). primary_system unchanged (DEISM 0.5). Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "CODING_GUIDE §7 rule on unofficial web copies (Jason's decision, 2026-10-02): self_described_science_religion_relation certainty 1.0 → 0.7. Its main claims rest on the 1937 lecture, read only in a typed web copy (S4) and a blog (S7), and no authoritative edition was reachable to check the wording. No mid_basin change (A and B were already 0.7)."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Schema 1.1 → 1.2 (decision P8 adds basis recorded_interview and statement kind 'recorded interview'); no content change."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit, batch 4 (two blind runs at b21655b). Decision P13 recheck: first_lasting_contribution_year 1900 → 1879, the start year of the earliest listed contribution (work on entropy and the second law, 1879–1897); age 42 → 21; era unchanged. If that item is judged not lasting it should be removed and the year returns to 1900 (noted in how_known). Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Stage 3 lens-audit rulings applied to the batch's other records (OPEN_DECISIONS P14–P28, v8's picks, 2026-10-02). Schema 1.2 → 1.3. One reliable source caps a fact at 0.7; derived fields take the lowest certainty of their inputs; BELOW_THRESHOLD vs UNKNOWN per P19; DEISM revelation test recorded (P27). Full before → after list: reports/stage3_rulings_changes.csv. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "P30 rule 5 age sweep: ages recomputed as event year − birth year, with no month adjustment (scripts/recompute_ages.py; every change is in reports/p30_age_changes.csv). No other value changed."}

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
  native_name: {value: "Max Planck (German)", certainty: 0.7, cites: [{source: S1, locator: "opening paragraph"}], how_known: "Same spelling."}
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
  first_lasting_contribution_year: {value: 1879, certainty: 0.7, cites: [{source: S3, locator: "paragraph 3"}, {source: S2, locator: "doctorate and habilitation paragraphs"}], how_known: "Start year of the earliest listed contribution, the work on entropy and the second law (1879–1897, beginning with his 1879 doctoral thesis), under decisions P12 and P13. 0.7 because that item's lasting status is the coder's reading (Thermodynamik, 1897, a standard text); if it is judged not lasting it should be removed from the list, and the year returns to 1900, the quantum of action and radiation law (October–December 1900; S1, blackbody paragraphs; S3, paragraph 4). Both years fall in the same era. Was 1900 until the batch 4 lens audit."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S1, locator: "blackbody paragraphs"}], how_known: "Either candidate year falls in 1850 to 1949 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts ('Kiel, Schleswig [Germany]')"}], how_known: "Germany is Western Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Western Europe", certainty: 1.0, cites: [{source: S1, locator: "university paragraph"}, {source: S3, locator: "paragraph 2"}], how_known: "Munich, Kiel and Berlin (Germany)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S3, locator: "paragraph 1"}], how_known: "As the sources record it."}
  languages_of_work: {value: [German], certainty: 0.7, cites: [{source: S3, locator: "paragraph 5 (Annalen der Physik; Thermodynamik; Theorie der Wärmestrahlung)"}], how_known: "Nobel biography."}
  occupations: {value: ["theoretical physicist", "university professor", "permanent secretary of the Prussian Academy of Sciences", "president of the Kaiser Wilhelm Society"], certainty: 1.0, cites: [{source: S3, locator: "paragraph 2"}, {source: S2, locator: "Kaiser Wilhelm Gesellschaft paragraph"}], how_known: "Two sources."}

contribution:
  fields: {value: ["theoretical physics", thermodynamics, "quantum theory"], certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}, {source: S3, locator: "paragraphs 3–4"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Planck's radiation law and the quantum of action (Planck's constant h); energy of a resonator comes in discrete quanta hν", year: "1900", kind: theory, lasting: "foundation of quantum theory", certainty: 1.0, cites: [{source: S1, locator: "blackbody paragraphs"}, {source: S3, locator: "paragraphs 3–4"}], how_known: "Two sources."}
    - {value: "Work on entropy and the second law, thermoelectricity and dilute solutions", year: "1879–1897", kind: theory, lasting: "Thermodynamik (1897), a standard text", certainty: 0.7, cites: [{source: S3, locator: "paragraphs 3, 5"}, {source: S2, locator: "doctorate and habilitation paragraphs"}], how_known: "Nobel biography and MacTutor; how lasting is the coder's reading, 0.7."}
  evidence_of_impact:
    - {value: "Max Planck Medal, with Planck as first recipient; the Kaiser Wilhelm Society renamed the Max Planck Society", kind: "named after them", certainty: 0.7, cites: [{source: S2, locator: "Kaiser Wilhelm Gesellschaft paragraph"}], how_known: "MacTutor."}
    - {value: "Nobel Prize in Physics 1918", kind: "honours in lifetime", certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}, {source: S2, locator: "Nobel paragraph"}], how_known: "Two sources."}
  major_works:
    - {value: "Vorlesungen über Thermodynamik", year: 1897, kind: book, certainty: 0.7, cites: [{source: S3, locator: "paragraph 5"}], how_known: "Nobel biography."}
    - {value: "Vorlesungen über die Theorie der Wärmestrahlung", year: 1906, kind: book, certainty: 0.7, cites: [{source: S3, locator: "paragraph 5"}], how_known: "Nobel biography."}
  honours:
    - {value: "Nobel Prize in Physics", year: 1918, certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}, {source: S3, locator: "heading"}], how_known: "Two sources."}
    - {value: "Copley Medal of the Royal Society", year: 1928, certainty: 0.7, cites: [{source: S3, locator: "paragraph 6"}], how_known: "Nobel biography."}
  definition_fit: {value: "clearly meets", rationale: "Originated quantum theory.", certainty: 0.7, cites: [{source: S1, locator: "opening paragraph"}], how_known: "Sources agree."}

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
    - {value: "The law of conservation of energy, learned at the Gymnasium, was the 'first instance of an absolute in nature that impressed Planck deeply'", certainty: 0.7, cites: [{source: S1, locator: "blackbody section, first paragraph"}], how_known: "Britannica."}
  key_early_reading:
    - {value: "Rudolf Clausius's writings on thermodynamics", certainty: 1.0, cites: [{source: S1, locator: "university paragraph"}, {source: S3, locator: "paragraph 3"}], how_known: "Two sources."}
  childhood_mentors:
    - {value: "Hermann Müller, Gymnasium teacher", certainty: 0.7, cites: [{source: S1, locator: "early life paragraph"}], how_known: "Britannica."}
  languages_in_childhood: {value: [German], certainty: 0.7, cites: [{source: S1, locator: "early life paragraph"}], how_known: "German family and schooling."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1879–1947", certainty: 0.7, cites: [{source: S3, locator: "paragraphs 2, 9"}], how_known: "Doctorate to death; he lectured on religion and science into old age."}
  nominal_affiliations:
    - {value: "Protestant church tradition of his family; in 1947 he denied a rumoured conversion to Catholicism", years: "1858–1947", role: other, certainty: 0.5, cites: [{source: S1, locator: "early life paragraph"}, {source: S9, locator: "p. 327; nn. 47–48"}, {source: S6, locator: "Heilbron quotation"}], how_known: "Family tradition (S1: 'devotion to church and state') and the 1947 denial only. Church membership or office is unsourced: neither membership (Lutheran) nor the commonly reported church-elder role was found in the sources read, so the role is 'other', not 'member' (lens audit, batch 2, finding #135)."}
  self_described_science_religion_relation:
    value: "Religion and natural science 'mutually supplement and condition each other'; both need belief in God, for religion at the start and for science at the end of all thought; science is for knowing, religion for acting. Belief in nature-miracles must retreat before science."
    certainty: 0.7
    cites: [{source: S4, locator: "copy pp. 2, 11–13"}, {source: S7, locator: "1937 lecture transcription"}, {source: S5, locator: "pp. 159, 168"}]
    how_known: "His own public lecture (1937) and book (1933 English edition). 'mutually supplement and condition each other' is the coder's gloss of 'sie ergänzen und bedingen einander' (copy p. 12), cross-checked with Gaynor (S7), whose wording it is. Certainty 0.7 under CODING_GUIDE §7: the 1937 lecture, which carries the main claims, was read only in unofficial web copies (S4, a typed copy on a private site; S7, a blog). No authoritative edition could be reached to check the wording; the Internet Archive has no library scan of the 1938 Barth edition or of Vorträge und Erinnerungen (1949). S5 (a library scan) supports only the 1933 statements on chance, miracle and causality, not the 1937 wording."
  primary_system:
    value: DEISM
    basis: written_profession
    certainty: 0.5
    cites: [{source: S4, locator: "copy pp. 2, 5, 6, 11–12"}, {source: S9, locator: "p. 327; n. 48"}, {source: S6, locator: "Heilbron quotation"}]
    how_known: "His 1937 lecture says belief in nature-miracles must retreat before science (copy p. 2) and that even the holiest symbol is of human origin (copy p. 5); religion and science agree that a rational world order independent of humans exists, and the scientist approaches 'Gott und seiner Weltordnung' by inductive research (copy pp. 11–12). His 1947 letter denies belief 'in a personal God, let alone a Christian God' (Heilbron via S6; the German in Gladigow, S9, citing Herneck 1952). 0.5, below the 0.7 cap: two codes are named; Heilbron's 'deism' is unconfirmed in the book and is not used as support; and a 1945 letter (Bertholet 1948, known only through S9, n. 48) seems to show a more personal God. DEISM is a sourced system file (draft)."
    rationale: "English phrases from S4 are the coder's glosses, cross-checked with Gaynor (S7). DEISM use_when: own writing affirms a creator known by reason and rejects revelation, miracles and church authority as sources of religious knowledge. Met: belief in nature-miracles must retreat (copy p. 2); symbols and rite are indispensable but 'auch das heiligste Symbol menschlichen Ursprungs ist' (copy p. 5); the world order that science reaches is to be identified with God (copy p. 11). Only partly met, 'known by reason': whether God rules the world independently of belief 'läßt sich nie und nimmer auf wissenschaftlichem Wege … aufklären' and is 'einzig und allein Sache des Glaubens' (copy p. 6), and for action he relies on 'die bestimmte und klare Weisung … aus der unmittelbaren Verbindung mit Gott' (copy p. 12), a non-rational link, where DEISM has reason and nature only. So DEISM fits his rejection of miracle and doctrine, not a reasoned proof of God. Heilbron's 'Planck's deism' (S6) is unconfirmed in the book and is loose: it describes a religion that 'omitted all reference to established religions', and DEISM's do-not-use note warns against coding from a label. Alternatives: PANT (the identification sentence and 'wesensgleich', copy pp. 11–12; part 1 of the PANT test not clearly met, since the same lecture speaks of 'der über die Natur regierenden allmächtigen Vernunft', copy p. 11); CHRIST (Protestant tradition; valued religious symbols; the 1945 letter reported by Bertholet seems to show a more personal God, S9 n. 48; against it, the 1947 denial of a personal and a Christian God, now confirmed in German, S9). Held at 0.5. P27 test (DEISM needs rejection of revelation as a source of truth): met for doctrine and miracle, since even the holiest symbol is of human origin (copy p. 5) and belief in nature-miracles must retreat (copy p. 2); his 'Weisung' from a direct link with God (copy p. 12) concerns action, not truth claims. If that link is read as revelation, DEISM fails and PANT is next; one reason the code stays at 0.5."
  secondary_system: {value: UNKNOWN, how_known: "No second system settled; PANT and CHRIST are named alternatives."}
  candidate_codes_considered:
    - {code: DEISM, reason: "Chosen at 0.5: miracles rejected, symbols and creeds of human origin, God identified with the world order; but God's independent rule is a matter of faith alone for him, and action rests on a direct link with God. Heilbron's label is unconfirmed in the book and not used as support.", cites: [{source: S4, locator: "copy pp. 2, 5, 6, 11–12"}, {source: S6, locator: "Heilbron quotation"}]}
    - {code: PANT, reason: "Named alternative: the world order of science and the God of religion are to be identified. Not chosen: the same lecture speaks of the omnipotent Reason that rules over Nature (his own voice). PANT is a sourced system file.", cites: [{source: S4, locator: "copy pp. 11–12"}]}
    - {code: CHRIST, reason: "Named alternative: Protestant family and church tradition; a 1945 letter quoted by Bertholet (1948) seems to show a more personal God (S9, n. 48; not read). Not chosen: in 1947 he denied a personal and a Christian God (S6; German in S9) and expected belief in miracles to vanish. CHRIST is a sourced system file.", cites: [{source: S1, locator: "early life paragraph"}, {source: S9, locator: "p. 327; n. 48"}, {source: S6, locator: "Heilbron quotation"}]}
  lio_axes:
    A_locus:
      value: 2
      basis: written_profession
      certainty: 0.7
      cites: [{source: S4, locator: "copy pp. 6, 11–12"}, {source: S9, locator: "p. 327; n. 48"}, {source: S6, locator: "Heilbron quotation"}]
      how_known: "His own lecture holds both sides; contested, so 0.7. The 1945 counter-evidence is known only through Gladigow's note, so it strengthens a named alternative rather than moving the score."
      rationale: "English phrases from S4 are the coder's glosses, cross-checked with Gaynor (S7). Mixed. Toward the LIO pole, in his own voice: the world order of natural science and the God of religion are to be identified (copy p. 11), and the deity is 'wesensgleich' (Gaynor: 'consubstancial') with the power acting by natural law (copy p. 12); in 1947 he did not believe 'in a personal God' (S6; S9). Toward the other pole, also his own voice: 'the omnipotent Reason which rules over Nature' (Gaynor's wording for 'der über die Natur regierenden allmächtigen Vernunft', copy p. 11), and religion and science agree that 'eine von den Menschen unabhängige vernünftige Weltordnung existiert' (copy p. 11). Reported views, not scored as his own: whether God 'rules the world' independently of belief is a question he poses and says only faith can answer, and God holding 'believers and unbelievers' 'in his almighty hand' is the religious person's answer (copy p. 6). Counter-evidence: a 1945 letter quoted by Bertholet (Physikalische Blätter 4, 1948, p. 162) seems to show a more personal conception of God (S9, n. 48: 'eine persönlichere Gottesvorstellung zu vertreten scheint'; not read). Alternatives: 3 if the identification sentence is his settled view; 1 on the 1945 letter."
    B_cause:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S5, locator: "p. 159; p. 168"}, {source: S4, locator: "copy pp. 2, 7"}]
      how_known: "Published book and public lecture state it directly; 0.7 because the free-will passage is a named alternative."
      rationale: "English phrases from S4 are the coder's glosses. Scored on his account of nature (P6), which is his working physics and his philosophy of it. 'chance and miracle in the absolute sense are fundamentally excluded from science' (1933); religion must not oppose 'the sequence of cause and effect in all external phenomena' (1933); all physical events 'without exception' reduce to mechanical or electrical processes, and belief in nature-miracles must retreat step by step (1937). No miracle or answered petition appears. Alternative: 3, if the individual ego, where 'every causal method of research is inapplicable' (1933, p. 161), is read as an exemption; he treats it as a limit of self-observation, not an uncaused event, so 4."
    C_ledger: {value: UNKNOWN, how_known: "Nothing read on judgement, afterlife or moral reckoning. He puts ethics outside science and gives religion the guidance of action (copy p. 12), which is not a ledger.", note: "Gap: Scientific Autobiography and Other Papers (1949) and Heilbron 1986 not read in full."}
    D_authority:
      value: 2
      basis: written_profession
      certainty: 0.7
      cites: [{source: S4, locator: "copy pp. 5, 6, 12"}, {source: S7, locator: "1937 lecture transcription ('Natural science wants man to learn, religion wants him to act')"}]
      how_known: "Coder's reading of his lecture; 0.7."
      rationale: "English phrases from S4 are the coder's glosses, cross-checked with Gaynor (S7). Two domains, each with its own authority, so D 2 (the guide's same-pattern rule, as for Einstein and Galileo). For knowledge, only sense data and measurement count, and belief in miracles must yield to science. For action and ethics, the guide is 'die bestimmte und klare Weisung' gained 'aus der unmittelbaren Verbindung mit Gott' (Gaynor: 'definite and clear instruction', 'a direct inner link to God'; copy p. 12), a non-rational authority; and whether God rules the world independently of belief is 'einzig und allein Sache des Glaubens' (copy p. 6). He also says even 'the holiest symbol is of human origin' (copy p. 5). Alternative 3 if the direct link with God is read as conscience rather than revelation."
    E_scope:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S4, locator: "copy pp. 6, 11"}, {source: S7, locator: "1937 lecture transcription"}]
      how_known: "His own lecture; one named alternative, so 0.7."
      rationale: "English phrases from S4 are the coder's glosses. Scored on the world's order (P7). In his own voice the rational world order is one 'der Natur und Menschheit unterworfen sind' (to which Nature and humanity are subject, copy p. 11): the same rules for all, and nothing he asserts keeps favour in events for a group. The passage on believers is reported, not his own claim: the religious person's answer has God hold 'Gläubige und Ungläubige' alike in his hand, and the truly religious 'feel secure under the protection of the Almighty against all dangers of life' (copy p. 6). That is a felt security ('sich … gesichert fühlen') inside his account of what religion asks its adherents to accept, not favour in events, which is all P7 counts. So 4 (lens audit, batch 2, finding #132; was 3). Named alternative 3, if that protection is read as a promise of favour in events."
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
      context: "'into the workings of the omnipotent Reason that rules over Nature' (coder's gloss, cross-checked with Gaynor's 'the omnipotent Reason which rules over Nature'): the transcendent-leaning phrase, in his own voice at the end of section III."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "daß er von Ewigkeit her die ganze Welt, Gläubige und Ungläubige, in seiner allmächtigen Hand hält"
      cites: [{source: S4, locator: "copy p. 6"}]
      date: "1937-05"
      context: "Reported view, not his own assertion: 'Der religiöse Mensch beantwortet die Frage dahin, …' God holds the whole world, believers and unbelievers, in his almighty hand from eternity. It answers the question he has just posed (does God rule the world independently of belief?), which he says only faith can answer; he sums it up as what religion asks its adherents to accept ('deren Anerkennung die Religion von ihren Anhängern fordert') and then compares it with science."
      axes: [A_locus, E_scope]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "sondern nur die bestimmte und klare Weisung, die wir aus der unmittelbaren Verbindung mit Gott gewinnen"
      cites: [{source: S4, locator: "copy p. 12"}]
      date: "1937-05"
      context: "On action: long reflection cannot guide decisions, 'only the definite and clear direction that we gain from the direct link with God' (coder's gloss, cross-checked with Gaynor: 'definite and clear instruction', 'a direct inner link to God')."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "Vielmehr ist die Beantwortung dieser Frage einzig und allein Sache des Glaubens, des religiösen Glaubens."
      cites: [{source: S4, locator: "copy p. 6"}]
      date: "1937-05"
      context: "The question is whether God lives only in believers' souls or rules the world independently of belief; the sentence before says it 'läßt sich nie und nimmer auf wissenschaftlichem Wege … aufklären'. 'Rather, answering this question is solely a matter of faith, of religious faith' (coder's gloss)."
      axes: [A_locus, D_authority]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "Sie stellt also eine vernünftige Weltordnung dar, der Natur und Menschheit unterworfen sind [...]"
      cites: [{source: S4, locator: "copy p. 11"}]
      date: "1937-05"
      context: "On the lawfulness that holds in the whole of nature: 'It thus represents a rational world order to which Nature and humanity are subject' (coder's gloss); the sentence goes on that its real nature stays unknowable to us."
      axes: [E_scope]
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
      context: "Heilbron's report of Planck's reply to an engineer who asked about a rumoured conversion to Catholicism; read only as quoted on a blog. Wikipedia's p. 198 refers to the 2000 Harvard printing, not checked in either edition. The German is confirmed independently by Gladigow (S9), next statement."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-02
    - text: "Obwohl von Jugend an tief religiös gestimmt, glaube ich nicht an einen persönlichen Gott, geschweige denn an einen christlichen Gott."
      cites: [{source: S9, locator: "p. 327; nn. 47–48 (p. 335)"}]
      date: "1947"
      context: "Letter of 1947 answering the Neue Zeitung's false report that he had converted to Catholicism (S9, n. 47). Gladigow cites F. Herneck, 'Ein Brief Max Plancks über sein Verhältnis zum Gottesglauben', Forschungen und Fortschritte 32 (1952), 364–366 (not read)."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-02
  changes_over_life: []
  coder_notes: "DEISM, PANT and CHRIST are sourced system files. The 1937 lecture is quoted from the German (a web copy of the 1938 second edition; 'copy p.' is the copy's own page numbering, not checked against the printed edition). English glosses are the coder's, cross-checked against an incomplete blog transcription of Gaynor's translation (S7). Heilbron (S6) was not read directly. The 1913 letter on 'the teachings of Jesus' quoted on the S7 blog (via Heilbron p. 67) was not used. Gladigow (S9) gives the German of the 1947 letter and reports (n. 48) a 1945 letter, quoted by Bertholet (Physikalische Blätter 4, 1948, p. 162), that seems to show a more personal God; Bertholet and Herneck were not read."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "German academic family of jurists and theologians", certainty: 0.7, cites: [{source: S2, locator: "paragraph 1"}], how_known: "MacTutor."}
  religious_heritage_by_birth: {value: "Protestant", certainty: 0.7, cites: [{source: S2, locator: "paragraph 1"}, {source: S1, locator: "early life paragraph"}], how_known: "Theologian forebears at Göttingen and family devotion to the church; denomination not named."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated in S1–S7."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated in S1–S7."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1879–1906", certainty: 0.7, cites: [{source: S3, locator: "paragraphs 2–5"}], how_known: "Thermodynamics papers to the radiation book."}
  age_at_first_lasting_contribution: {value: 21, certainty: 0.7, cites: [{source: S1, locator: "Quick Facts; blackbody paragraphs"}], how_known: "Born 23 April 1858; doctorate and first thermodynamics work in 1879 (month not given here), so 21 for most of the year. 42 if the year is the quantum paper of December 1900. Was 42 until the batch 4 lens audit. P30 (rule 5): 1879 − 1858 = 21, with no month adjustment; was 42 until the P30 age sweep (2026-10-02)."}
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
  - {value: "University of Munich", role: "Privatdozent", years: "1880–1885", kind: employer, certainty: 0.7, cites: [{source: S3, locator: "paragraph 2"}], how_known: "Nobel biography."}
  - {value: "University of Kiel", role: "associate professor of theoretical physics", years: "1885–1889", kind: employer, certainty: 1.0, cites: [{source: S3, locator: "paragraph 2"}, {source: S1, locator: "university paragraph"}], how_known: "Two sources."}
  - {value: "University of Berlin", role: "professor (successor to Kirchhoff)", years: "1889–1926", kind: employer, certainty: 0.7, cites: [{source: S3, locator: "paragraph 2"}, {source: S2, locator: "Berlin paragraph"}], how_known: "Retirement 1926 (S3) or 1 October 1927 (S2)."}
  - {value: "Prussian Academy of Sciences", role: "member 1894; permanent secretary 1912", years: "1894–", kind: "academy or learned society", certainty: 0.7, cites: [{source: S3, locator: "paragraph 2"}], how_known: "Nobel biography."}
  - {value: "Kaiser Wilhelm Society", role: president, years: "1930–1937; 1945–1946", kind: other, certainty: 0.7, cites: [{source: S2, locator: "Kaiser Wilhelm Gesellschaft paragraph"}, {source: S3, locator: "paragraph 2"}], how_known: "MacTutor gives 1930–1937 and 1945–46; the Nobel biography gives the end year 1937 only."}
collaborators:
  - {value: "Gustav Kirchhoff", relation: teacher, note: "teacher in Berlin; Planck succeeded him", certainty: 0.7, cites: [{source: S3, locator: "paragraphs 2–3"}], how_known: "Nobel biography."}
  - {value: "Hermann von Helmholtz", relation: "mentor or employer", note: "teacher, later venerated mentor and colleague", certainty: 1.0, cites: [{source: S1, locator: "university paragraph"}, {source: S3, locator: "paragraph 2"}], how_known: "Two sources."}
  - {value: "Albert Einstein", roster_id: einstein-albert, relation: influenced, note: "light quanta (1905) built on the quantum hypothesis", certainty: 0.7, cites: [{source: S1, locator: "quantum-reception paragraph"}], how_known: "Britannica."}
  - {value: "Ludwig Boltzmann", relation: "influenced by", note: "Planck adopted his statistical reading of the second law to derive the radiation law", certainty: 0.7, cites: [{source: S1, locator: "blackbody paragraphs"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v7.1 (F 4) and v8 (F 5, all five models).", certainty: 0.7, cites: [{source: S8, locator: "roster.csv, rank 57"}], how_known: "Study roster."}
  controversies:
    - {value: "Stayed in Germany as head of German science under the Nazi government while opposing some of its policies", certainty: 1.0, cites: [{source: S3, locator: "paragraph 7"}, {source: S2, locator: "Nazi period paragraphs"}], how_known: "Two sources."}
  data_quality_flags:
    - "Britannica places Kiel in 'Schleswig'; Kiel was in Holstein."
    - "Retirement from Berlin: 1926 (Nobel biography) vs 1927 (MacTutor). First marriage: 1885 (Nobel) vs 31 March 1887 (MacTutor)."
    - "MacTutor says 'In 1945 his other son was executed' after describing Erwin's execution; its own text has Karl killed in 1916, so this reads as an error in MacTutor."
    - "Heilbron read only through a blog quotation and Wikipedia's quotation; 'Planck's deism' is not confirmed in the book. Wikipedia's p. 198 refers to the 2000 Harvard University Press printing (Google Books d5zKH2Bx2AwC), not the 1986 University of California Press edition."
    - "Gladigow (S9, n. 45) puts the identification sentence on p. 29 of the 1938 edition (= Vorträge und Erinnerungen p. 331); the web copy (S4) has it on its own p. 11."
    - "The German lecture text is a web copy of the 1938 edition; page numbers are the copy's."
  open_questions:
    - "Read Heilbron, The Dilemmas of an Upright Man (1986), pp. 182–198, and Scientific Autobiography and Other Papers (1949) for the 1947 letter and his church role."
    - "Settle how mid_basin treats A_locus = 2 (no P4 branch)."
    - "Read Bertholet, 'Erinnerungen an Max Planck', Physikalische Blätter 4 (1948), p. 162, for the 1945 letter, and Herneck 1952 and 1960; also 'Max Planck – ein Gegner des Christentums?', Berichte zur Wissenschaftsgeschichte (2012), doi:10.1002/bewi.201201176."

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
    citation: "Heilbron, J. L. The Dilemmas of an Upright Man: Max Planck as Spokesman for German Science. Berkeley: University of California Press, 1986. Wikipedia's p. 198 refers to the reissue, The Dilemmas of an Upright Man: Max Planck and the Fortunes of German Science (Cambridge, MA: Harvard University Press, 2000; Google Books d5zKH2Bx2AwC); neither edition was checked. Quoted in \"John .L. Heilbron about Max Planck and God,\" Space Theology (blog), 13 February 2012. http://spacetheology.blogspot.com/2012/02/max-planck-about-god.html."
    url: "http://spacetheology.blogspot.com/2012/02/max-planck-about-god.html"
    accessed: 2026-10-02
    reliability_note: "Scholarly biography read only through a blog's quotation (with typos such as 'Plankc's'); the same passage appears in Wikipedia's citation of Heilbron (2000 printing). Treat as a secondary quotation. The 'deism' wording is not confirmed in the book, and Heilbron uses the word loosely (a religion that 'omitted all reference to established religions'), so it is not used to support the code. The 1947 denial is confirmed independently in German by S9."
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
  - id: S9
    type: secondary
    kind: "book chapter"
    author: "Burkhard Gladigow"
    year: 1986
    citation: "Gladigow, Burkhard. \"'Wir gläubigen Physiker': Zur Religionsgeschichte physikalischer Entwicklungen im 20. Jahrhundert.\" In Der Untergang von Religionen, edited by Hartmut Zinser, 321–336. Berlin, 1986. Repository PDF, Universität Tübingen. https://doi.org/10.15496/publikation-63319."
    url: "https://publikationen.uni-tuebingen.de/xmlui/bitstream/handle/10900/121955/Gladigow_059.pdf"
    accessed: 2026-10-02
    reliability_note: "Peer scholarship by a historian of religion (Tübingen), read as the repository scan of the printed chapter; page numbers are the chapter's (321–336), endnotes on pp. 331–336. Quotes the 1947 letter in German from Herneck 1952 and reports Bertholet's 1945 letter in note 48; neither was read."
    used_for: [worldview]
---

# Max Planck

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Max Planck (1858–1947), German theoretical physicist, found the radiation law and the quantum of action in 1900 and won the 1918 Nobel Prize in Physics [S1, opening paragraph; S3, paragraph 4]. In his 1937 lecture "Religion und Naturwissenschaft" he identified "die Weltordnung der Naturwissenschaft und den Gott der Religion" and said belief in nature-miracles must retreat before science [S4, copy pp. 2, 11]. In 1947 he wrote that he did not believe "an einen persönlichen Gott, geschweige denn an einen christlichen Gott" [S9, p. 327]. Coded DEISM at 0.5 (PANT and CHRIST named; Heilbron's "deism" label [S6] is not confirmed in the book and is not used as support). A 2, B 4, D 2, E 4 (all 0.7); C UNKNOWN; mid_basin TODO (no P4 branch for A = 2).

## Life and work

Doctorate at Munich in 1879 at 21; professor at Kiel (1885) and Berlin (1889), permanent secretary of the Prussian Academy (1912) and president of the Kaiser Wilhelm Society [S1, university paragraph; S3, paragraph 2; S2].

## Contribution and impact

Planck's radiation law and constant h (1900), the foundation of quantum theory [S1; S3, paragraphs 3–4].

## Childhood and education

His family had a "long family tradition of devotion to church and state" [S1, early life paragraph]; his grandfather and great-grandfather were professors of theology at Göttingen [S2, paragraph 1].

## Adult working worldview

He wrote that "chance and miracle in the absolute sense are fundamentally excluded from science" [S5, p. 159] and that religion must not oppose "the sequence of cause and effect in all external phenomena" [S5, p. 168]. In 1937 God stands "für die eine am Anfang, für die andere am Ende alles Denkens" [S4, copy p. 12]. Heilbron reports that he did not believe "in a personal God, let alone a Christian God" [S6]; Gladigow gives the German of the 1947 letter and notes a 1945 letter that seems to show a more personal God [S9, p. 327, n. 48]. Scores: A 2, B 4, D 2, E 4 (0.7 each); C UNKNOWN.

## Heritage (context only)

Protestant academic family [S1; S2]. Context only.

## Timing

First lasting contribution 1879, the start of his work on entropy and the second law, at 21 [S2; S3]; the quantum of action followed in 1900, at 42 [S1]. The worldview texts read are from 1932–1947.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form unclear; circle partial (God identified with the world order but also ruling over Nature).

## Open questions

- Heilbron (1986) and Scientific Autobiography and Other Papers (1949), for the 1947 letter and church membership.
- Bertholet (1948) for the 1945 letter, and Herneck (1952, 1960).
- mid_basin for A_locus = 2 needs a decision.

## Research log

- 2026-10-02: Read Britannica (Stuewer, first page), MacTutor, the Nobel biography, the German 1937 lecture (web copy of the 1938 edition), Where Is Science Going? (1933, DLI scan on archive.org), and two blogs (Heilbron quotation; partial Gaynor transcription). Scientific Autobiography (1949) is lending-only on archive.org; the socraticdictum.com PDF of the Gaynor translation failed to download. Quotations checked against the downloaded texts.
