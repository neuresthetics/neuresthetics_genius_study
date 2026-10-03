---
record:
  record_type: person
  schema_version: "1.2"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (executor agent for v8, RUNBOOK stage 3, batch A: early modern philosophers)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (stage 3, batch A). Basics from SEP 'David Hume' (Qu), Britannica (Cranston, first page) and My Own Life; religion from SEP 'Hume on Religion' (Russell). Worldview quotations from the edited texts at Hume Texts Online (Millican and Merivale): Enquiry §§9–12, Dialogues Part 12, Natural History §15. DRAFT SCORES for v8's review: primary_system BELOW_THRESHOLD (candidates AGNOS, SCEPT, ATHE, EMPIR are stubs; DEISM rejected); A 3 and C 4 at 0.5; B 4, D 4, E 4 at 0.7; mid_basin BELOW_THRESHOLD (A only 0.5). Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit fixes, stage 3 batch A (two blind runs at 59a8371). #512: SCEPT locator is E 12.24–25 (SBN 161–2), not E 12.34. #539: Advocates Library 1752–1757; end year from Britannica 'Adam Ferguson' (new S9), not inferred as 1763. #518, #527: the Enquiry 11 conclusion is the friend in his own person after the Epicurus speech (E 11.9–23). #524: 'most scholars' wording replaced by SEP §10. #545: Britannica's 1744 noted beside SEP's 1745 and flagged; 1.0 left pending v8 (conflict rule). Bylines: SEP Hume now Qu and Radcliffe; SEP religion now Russell and Kraal; Britannica now Cranston and Jessop. #510 left (stub-system rule awaits v8). Not reviewed."}

identity:
  id: hume-david
  display_name: "David Hume"
  roster:
    canonical_name: "David Hume"
    rank: 21
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: philosophy
    field_bucket: philosophy
  full_name: {value: "David Hume", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S3, locator: "opening"}], how_known: "Two sources."}
  native_name: {value: "David Hume", certainty: 1.0, cites: [{source: S3, locator: "opening"}], how_known: "As given."}
  aliases:
    - {name: "David-Hume", kind: "roster alias"}
    - {name: "Hume-David", kind: "roster alias"}

basics:
  birth:
    date: {value: "1711-05-07", calendar: gregorian, certainty: 1.0, cites: [{source: S3, locator: "opening ('May 7 [April 26, Old Style], 1711')"}, {source: S7, locator: "MOL 2 ('the 26th of April 1711, old style')"}], how_known: "Britannica gives both styles; his own account gives 26 April Old Style (Julian)."}
    place: {value: "Edinburgh", modern_name: "Edinburgh, Scotland, United Kingdom", polity_then: "Kingdom of Scotland (Kingdom of Great Britain from 1707)", certainty: 1.0, cites: [{source: S7, locator: "MOL 2"}, {source: S1, locator: "§1"}, {source: S3, locator: "opening"}], how_known: "Three sources agree. Polity: 1711 is after the 1707 Union, so Great Britain (coder's gloss)."}
  death:
    date: {value: "1776-08-25", calendar: gregorian, certainty: 1.0, cites: [{source: S3, locator: "opening"}, {source: S1, locator: "§1 (1776)"}], how_known: "Britannica gives the day; SEP the year."}
    place: {value: "Edinburgh", modern_name: "Edinburgh, Scotland, United Kingdom", polity_then: "Kingdom of Great Britain", certainty: 1.0, cites: [{source: S3, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1739, certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S7, locator: "MOL 5 (published 'In the end of 1738')"}], how_known: "A Treatise of Human Nature, Books 1–2, 1739 (SEP); Hume dates publication to the end of 1738. Either year gives the same era bucket."}
  era_bucket: {value: "1600 to 1749", certainty: 1.0, cites: [{source: S1, locator: "§1"}], how_known: "From first_lasting_contribution_year (P2); 1738 or 1739."}
  region_of_birth: {value: "Northern Europe", certainty: 1.0, cites: [{source: S1, locator: "§1"}], how_known: "United Kingdom is Northern Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "§1"}, {source: S7, locator: "MOL 4–5"}], how_known: "Mainly Edinburgh and London; the Treatise was written in France (1734–1737) and he was in Paris 1763–1766, so a Western Europe secondary region is arguable."}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S1, locator: "§1"}], how_known: "As the sources record it."}
  languages_of_work: {value: [English], certainty: 1.0, cites: [{source: S1, locator: "§1"}], how_known: "All works named are in English."}
  occupations: {value: [philosopher, historian, essayist, librarian, "diplomatic secretary"], certainty: 1.0, cites: [{source: S3, locator: "opening"}, {source: S1, locator: "§1"}], how_known: "Britannica: 'Scottish philosopher, historian, economist, and essayist'; SEP: Advocates Library, embassy secretary."}

contribution:
  fields: {value: [philosophy, epistemology, ethics, "philosophy of religion", history, economics], certainty: 1.0, cites: [{source: S3, locator: "opening"}, {source: S1, locator: "§1"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Empiricist theory of causation and induction (causal inference from constant conjunction and custom)", year: "1739–1748", kind: theory, lasting: "the problem of induction; regularity theories of causation", certainty: 1.0, cites: [{source: S3, locator: "opening"}, {source: S1, locator: "§2"}], how_known: "Two sources."}
    - {value: "Argument against belief in miracles on testimony", year: "1748", kind: concept or term, lasting: "standard in philosophy of religion", certainty: 1.0, cites: [{source: S2, locator: "§6"}, {source: S4, locator: "E 10"}], how_known: "SEP and the text."}
    - {value: "Critique of the design argument (Dialogues concerning Natural Religion)", year: "1779", kind: work, lasting: "standard in philosophy of religion", certainty: 1.0, cites: [{source: S2, locator: "§4"}, {source: S1, locator: "§5.3"}], how_known: "Two SEP entries."}
    - {value: "Sentimentalist ethics ('reason is...the slave of the passions')", year: "1740", kind: theory, lasting: "a main tradition in moral philosophy", certainty: 1.0, cites: [{source: S3, locator: "opening; 'Mature works'"}, {source: S1, locator: "§4"}], how_known: "Two sources."}
  evidence_of_impact:
    - {value: "Woke Kant from his 'dogmatic slumber', as Kant admitted", kind: "assessment by a later major figure", certainty: 0.7, cites: [{source: S3, locator: "opening"}], how_known: "Britannica."}
  major_works:
    - {value: "A Treatise of Human Nature", year: 1739, kind: book, certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S7, locator: "MOL 5–6"}], how_known: "SEP and his own account."}
    - {value: "An Enquiry concerning Human Understanding (first titled Philosophical Essays concerning Human Understanding)", year: 1748, kind: book, certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S4, locator: "title"}], how_known: "SEP and the text."}
    - {value: "An Enquiry concerning the Principles of Morals", year: 1751, kind: book, certainty: 1.0, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
    - {value: "The Natural History of Religion (in Four Dissertations)", year: 1757, kind: book, certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S6, locator: "title"}], how_known: "SEP and the text."}
    - {value: "The History of England (6 vols.)", year: 1754, kind: book, certainty: 1.0, cites: [{source: S1, locator: "§1 (1754–1762)"}], how_known: "SEP."}
    - {value: "Dialogues concerning Natural Religion (posthumous)", year: 1779, kind: book, certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S5, locator: "title"}], how_known: "SEP and the text."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Theory of causation and induction; foundational in philosophy of religion and ethics.", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "opening"}], how_known: "Sources agree."}

childhood:
  family_religion: {value: TODO, note: "Not stated in SEP §1, SEP 'Hume on Religion', Britannica's first page or My Own Life."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father, Joseph Hume, laird of Ninewells near Chirnside, Berwickshire; died in David's third year", name: "Joseph Hume", role: father, certainty: 1.0, cites: [{source: S3, locator: "'Early life and works'"}, {source: S7, locator: "MOL 3 ('died when I was an infant')"}], how_known: "Britannica and his own account."}
    - {value: "Mother, Catherine, daughter of Sir David Falconer, President of the College of Justice; raised and educated her children", name: "Catherine Falconer", role: mother, certainty: 1.0, cites: [{source: S7, locator: "MOL 2–3"}, {source: S3, locator: "'Early life and works'"}], how_known: "His own account and Britannica. The surname Falconer is inferred from her father's name (flag)."}
  household_circumstances: {value: "A good but not rich family; a younger son with a slender patrimony, raised with an elder brother and a sister by his widowed mother", certainty: 1.0, cites: [{source: S7, locator: "MOL 2–3"}, {source: S1, locator: "§1"}], how_known: "His own account and SEP."}
  schooling:
    - {value: "Educated by his mother at home", stage: home, years: "to c. 1722", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP: 'His mother was responsible for his education'."}
    - {value: "University of Edinburgh", stage: university, years: "c. 1722–1726", certainty: 0.7, cites: [{source: S1, locator: "§1 (ages eleven to fifteen)"}, {source: S3, locator: "'Early life and works' (about 12 to 14 or 15)"}], how_known: "Two sources; ages differ slightly; years are the coder's arithmetic."}
  early_mathematics: {value: UNKNOWN, how_known: "Checked SEP §1, Britannica's first page and My Own Life: none says what mathematics he learned."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Same sources checked; none mentions it."}
  early_science_exposure:
    - {value: "Student at Edinburgh in the 1720s while the Newtonian Colin Maclaurin was professor there", year: "1720s", age: "11–15", certainty: 0.5, cites: [{source: S2, locator: "§1"}], how_known: "SEP Russell states both facts; that Hume was taught by Maclaurin is not claimed."}
  key_early_reading:
    - {value: "Cicero and Virgil, read secretly instead of the law books (Voet and Vinnius)", certainty: 1.0, cites: [{source: S7, locator: "MOL 3"}], how_known: "His own account."}
  childhood_mentors:
    - {value: "His mother", certainty: 0.7, cites: [{source: S7, locator: "MOL 3"}, {source: S1, locator: "§1"}], how_known: "His own account and SEP."}
  languages_in_childhood: {value: [English, Latin], certainty: 0.5, cites: [{source: S7, locator: "MOL 3"}], how_known: "Latin implied by his reading of Cicero, Virgil and the Latin law books; Scots/English home language is the coder's inference."}
  notable_events:
    - {value: "Father's death", year: "1713/1714", age: 2, certainty: 0.7, cites: [{source: S3, locator: "'Early life and works' ('In his third year')"}, {source: S7, locator: "MOL 3"}], how_known: "Britannica; year is the coder's arithmetic."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1734–1776", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S7, locator: "MOL 4–5"}], how_known: "From the Treatise years in France to his death."}
  nominal_affiliations: []
  self_described_science_religion_relation:
    value: "'A wise man [...] proportions his belief to the evidence' (E 10.4). A miracle is 'a violation of the laws of nature', against which uniform experience is a full proof, so 'no testimony is sufficient to establish a miracle' unless its falsehood would be more miraculous (E 10.12–13), and a miracle 'can never be proved, so as to be the foundation of a system of religion' (E 10.36). On religion as a whole: 'The whole is a riddle, an ænigma, an inexplicable mystery' (N 15.13)."
    certainty: 0.7
    cites: [{source: S4, locator: "E 10.4, 10.12–13, 10.36"}, {source: S6, locator: "N 15.13"}]
    how_known: "His own published words in an edited text; 0.7 because SEP notes that open atheism could still provoke the authorities, so 'Caution and subterfuge' were essential and his professions of orthodoxy should not be read as entirely sincere (S2 §10)."
  primary_system:
    value: BELOW_THRESHOLD
    cites: [{source: S2, locator: "§§10–11"}, {source: S6, locator: "N 15.13"}, {source: S5, locator: "D 12.33"}]
    how_known: "SEP Russell sets out the main readings: a 'soft' sceptic endorsing neither theism nor atheism (most dominant in the past century), thin theism or 'attenuated deism' (Gaskin, Kraal), atheism, and Russell's own 'irreligion' (S2 §§10–11). The codes that fit the leading readings (AGNOS, SCEPT, ATHE, EMPIR) are all stub system files, so primary_system is BELOW_THRESHOLD under the stub rule."
    note: "Candidates: AGNOS (stub), SCEPT (stub), ATHE (stub), EMPIR (stub; an epistemology). DEISM (sourced) considered and rejected: its use_when needs a creator affirmed by reason, but the Dialogues reduce natural theology to the proposition that the cause of order 'probably bear[s] some remote analogy to human intelligence' (D 12.33), in Philo's voice. Russell's 'irreligion' has no system file. Backlog: AGNOS and ATHE are S7 backlog items; SCEPT also needed."
  secondary_system: {value: UNKNOWN, how_known: "No second system in what was read."}
  candidate_codes_considered:
    - {code: AGNOS, reason: "Leading candidate for the 'soft sceptic' reading (S2 §10) and his 'suspence of judgment' (N 15.13). Not coded: stub system file.", cites: [{source: S2, locator: "§10"}, {source: S6, locator: "N 15.13"}]}
    - {code: SCEPT, reason: "Candidate: his own 'mitigated scepticism' (E 12.24–25) and the sceptic reading. Not coded: stub system file.", cites: [{source: S4, locator: "E 12.24–25 (SBN 161–2)"}, {source: S2, locator: "§10"}]}
    - {code: ATHE, reason: "Candidate: many contemporaries regarded him as an atheist (S2 §10; S1 §1, the 1745 Edinburgh chair); Russell says the label 'atheism' is 'potentially misleading' (S2 §11). Not coded: stub system file.", cites: [{source: S2, locator: "§§10–11"}]}
    - {code: EMPIR, reason: "Considered: Britannica names his 'philosophical empiricism and skepticism'. Not coded: stub, and an epistemology rather than a God-world view.", cites: [{source: S3, locator: "opening"}]}
    - {code: DEISM, reason: "Considered (thin theism or 'attenuated deism', Gaskin 1988 and Kraal 2023 per S2 §10) and rejected: DEISM needs a creator affirmed by reason; Hume's texts allow at most a 'remote analogy' in Philo's voice (D 12.33).", cites: [{source: S2, locator: "§10"}, {source: S5, locator: "D 12.33"}]}
  lio_axes:
    A_locus:
      value: 3
      basis: scholarly_reconstruction
      certainty: 0.5
      cites: [{source: S2, locator: "§§10–11"}, {source: S5, locator: "D 12.33"}, {source: S6, locator: "N 15.13"}]
      how_known: "Scholarly reconstruction (SEP Russell) from texts in other speakers' voices and from his suspense of judgment; 0.5 is the basis ceiling."
      rationale: "DRAFT, judgment call. Leans away from a transcendent person: at most 'the cause or causes of order in the universe probably bear some remote analogy to human intelligence', an analogy that 'cannot be transferred [...] to the other qualities of the mind' (D 12.33, Philo); 'Doubt, uncertainty, suspence of judgment' about religion (N 15.13); Russell argues his attitude to religion (as robust theism) is 'systematic hostility' (S2 §11). Named alternatives: 2 (thin theism, 'attenuated deism', S2 §10) and 4 (atheism; or BELOW_THRESHOLD if suspense of judgment means no locus is held)."
    B_cause:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S4, locator: "E 10.12–13, 10.36"}, {source: S2, locator: "§6"}]
      how_known: "His own published words in an edited text; a named alternative (3)."
      rationale: "DRAFT. Scored on his account of nature (P6). At the LIO pole: 'a firm and unalterable experience has established these laws' and 'Nothing is esteemed a miracle, if it ever happen in the common course of nature' (E 10.12); no miracle can ground a religion (E 10.36). SEP: the argument turns on the 'uniform experience' that tells against a miracle (S2 §6). Named alternative: 3, because he grants that 'there may possibly be miracles, or violations of the usual course of nature, of such a kind as to admit of proof from human testimony' (E 10.36, the eight days of darkness)."
    C_ledger:
      value: 4
      basis: scholarly_reconstruction
      certainty: 0.5
      cites: [{source: S2, locator: "§7"}, {source: S4, locator: "E 11.27"}]
      how_known: "SEP reconstruction plus a passage in the voice of the Enquiry's sceptical friend; indirect, so 0.5."
      rationale: "DRAFT. At the 'none' pole: he rejects the metaphysical arguments for the immortality of the soul (S2 §7); in Enquiry 11 the sceptical friend, speaking in his own person after his speech for Epicurus (E 11.9–23), concludes that from the religious hypothesis there is 'no reward or punishment expected or dreaded, beyond what is already known by practice and observation' (E 11.27). Both indirect: the second is not in Hume's narrating voice. Named alternative: 3."
    D_authority:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S4, locator: "E 10.4, 10.40–41, 12.34"}, {source: S2, locator: "§10"}]
      how_known: "His own published words in an edited text; a named alternative (a face-value fideist reading)."
      rationale: "DRAFT. At the reason pole: belief is proportioned to evidence (E 10.4); any volume of divinity with neither abstract reasoning about quantity nor experimental reasoning about fact should be committed 'to the flames: For it can contain nothing but sophistry and illusion' (E 12.34). Named alternative: 0–1, if E 10.40–41 ('Our most holy religion is founded on Faith, not on reason'; faith as 'a continued miracle in his own person') is read at face value as fideism; SEP warns against reading his 'professions of orthodoxy as entirely sincere' given the 'awkward conditions in which he had to express his views' (S2 §10)."
    E_scope:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S4, locator: "E 9.1, 9.5–9.6; 10.12; 11.20–27"}]
      how_known: "His own published words in an edited text; 0.7 because the denial of a particular providence (E 11) is in another speaker's voice."
      rationale: "DRAFT. Scored on the world's order (P7). At the LIO pole: the same principle of experimental reasoning operates 'in all the higher, as well as lower classes of sensitive beings' (E 9.5) and is one 'which we possess in common with beasts' (E 9.6); anatomical findings for one animal are extended to all (E 9.1); and from the order of nature no 'particular reward of the good, and punishment of the bad, beyond the ordinary course of events' can be inferred (E 11.20, the friend speaking for Epicurus; restated in his own person at E 11.27). No in-group exception in events. The afterlife is a C matter (P7)."
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is scored only at 0.5, under the P4 test's 0.7 bar (B_cause 4 is at 0.7).", note: "If A were raised to ≥ 3 at 0.7 the result would be false; if A were 2 (thin theism) it would be TODO (no branch)."}
  statements:
    - text: "A wise man, therefore, proportions his belief to the evidence."
      cites: [{source: S4, locator: "E 10.4 (SBN 110–11)"}]
      date: "1748"
      context: "Enquiry, Section 10, 'Of Miracles', Part 1, in his own voice. Text as edited at Hume Texts Online."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "A miracle is a violation of the laws of nature; and as a firm and unalterable experience has established these laws, the proof against a miracle, from the very nature of the fact, is as entire as any argument from experience can possibly be imagined."
      cites: [{source: S4, locator: "E 10.12 (SBN 114–15)"}]
      date: "1748"
      context: "Same section."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "For I own, that otherwise, there may possibly be miracles, or violations of the usual course of nature, of such a kind as to admit of proof from human testimony; though, perhaps, it will be impossible to find any such in all the records of history."
      cites: [{source: S4, locator: "E 10.36 (SBN 127–8)"}]
      date: "1748"
      context: "Same section, Part 2, before the example of eight days of darkness; the sentence before says a miracle 'can never be proved, so as to be the foundation of a system of religion'."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "Our most holy religion is founded on Faith, not on reason; and it is a sure method of exposing it to put it to such a trial as it is, by no means, fitted to endure."
      cites: [{source: S4, locator: "E 10.40 (SBN 129–30)"}]
      date: "1748"
      context: "Same section, close; italics in the edition not reproduced. SEP warns against reading his 'professions of orthodoxy as entirely sincere' (S2 §10); the face-value fideist reading is the named alternative on D."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "Commit it then to the flames: For it can contain nothing but sophistry and illusion."
      cites: [{source: S4, locator: "E 12.34 (SBN 165)"}]
      date: "1748"
      context: "Enquiry, last paragraph, on any volume 'of divinity or school metaphysics' with neither abstract reasoning about quantity nor experimental reasoning about fact."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "No other explication can be given of this operation, in all the higher, as well as lower classes of sensitive beings, which fall under our notice and observation"
      cites: [{source: S4, locator: "E 9.5 (SBN 106–7)"}]
      date: "1748"
      context: "Enquiry, Section 9, 'Of the Reason of Animals': inference from custom in animals and humans. The edition's page-break mark is omitted."
      axes: [E_scope]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "No new fact can ever be inferred from the religious hypothesis; no event foreseen or foretold; no reward or punishment expected or dreaded, beyond what is already known by practice and observation."
      cites: [{source: S4, locator: "E 11.27 (SBN 145–7)"}]
      date: "1748"
      context: "Enquiry, Section 11: spoken by the friend 'who loves sceptical paradoxes' (E 11.1), in his own person after his speech for Epicurus (E 11.9–23), not in Hume's narrating voice."
      axes: [C_ledger, E_scope]
      kind: "other"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "That the cause or causes of order in the universe probably bear some remote analogy to human intelligence"
      cites: [{source: S5, locator: "D 12.33 (KS 227–8)"}]
      date: "1779"
      context: "Dialogues, Part 12, Philo's summary of what natural theology can establish; a character's speech, published posthumously."
      axes: [A_locus]
      kind: "other"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "The whole is a riddle, an ænigma, an inexplicable mystery. Doubt, uncertainty, suspence of judgment appear the only result of our most accurate scrutiny, concerning this subject."
      cites: [{source: S6, locator: "N 15.13 (Bea 87)"}]
      date: "1757"
      context: "The Natural History of Religion, closing 'General Corollary', in his own voice; spelling as in the edition."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
  changes_over_life: []
  coder_notes: "DRAFT SCORES for v8's review. Quotations are from the edited texts at Hume Texts Online (Millican and Merivale), cited by their paragraph numbers with the page references the site gives (SBN, KS, Bea, Mil); page-break marks '|' shown by the site are omitted. Treated as a scholarly edition, so the §7 cap does not apply, but every axis names an alternative or rests on indirect evidence. Voice matters: E 10, E 12, N 15 and My Own Life are Hume's own voice; E 11 is a friend's speech and the Dialogues are a dialogue, so they are kind 'other' and cannot alone support 0.7. SEP Russell's in-text cite 'EU, 11.12/114' for the miracle definition looks like a slip for 10.12 (the text is E 10.12)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Scottish gentry: a branch of the Earl of Home's family; mother's family legal nobility (Falconer of Halkerton)", certainty: 1.0, cites: [{source: S7, locator: "MOL 2"}, {source: S3, locator: "'Early life and works'"}], how_known: "His own account and Britannica."}
  religious_heritage_by_birth: {value: TODO, note: "Not stated in the sources read."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1734–1776", certainty: 1.0, cites: [{source: S1, locator: "§1"}], how_known: "Treatise written from 1734; revisions until his death."}
  age_at_first_lasting_contribution: {value: 27, certainty: 0.7, cites: [{source: S1, locator: "§1"}, {source: S7, locator: "MOL 5"}], how_known: "Born April/May 1711; Treatise published end of 1738 (his account) or 1739 (SEP): 27 either way."}
  first_evidence_of_lio_type_views: {value: "Lawful nature and the critique of miracle reports in the Enquiry", year: 1748, age: 37, certainty: 0.5, cites: [{source: S4, locator: "E 10"}], how_known: "Earliest text read; the Treatise (1739–1740) was not read, so earlier evidence is likely (flag)."}
  lio_views_relative_to_major_work: {value: "during major work", rationale: "The Enquiry (1748) falls in the middle of the major-work period; the Treatise was not read.", certainty: 0.5, cites: [{source: S4, locator: "E 10"}], how_known: "Dates of what was read."}
  worldview_during_major_work: {value: "Sceptical or irreligious throughout (no coded system: the candidates are stubs)", certainty: 0.5, cites: [{source: S2, locator: "§§10–11"}], how_known: "SEP reconstruction."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "His method is experimental and probabilistic ('A wise man [...] proportions his belief to the evidence', E 10.4), not definition-to-consequence demonstration.", certainty: 0.5, cites: [{source: S4, locator: "E 10.4"}, {source: S3, locator: "opening"}], how_known: "Coder's reading of his method."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "§1"}], how_known: "No source on early mathematics."}
  circle_present: {value: "no", rationale: "No God identified with Nature; suspense of judgment on the cause of order (N 15.13; D 12.33).", certainty: 0.5, cites: [{source: S6, locator: "N 15.13"}, {source: S5, locator: "D 12.33"}], how_known: "Coder's reading."}
  reading: "As belief, not finding: lawful nature with no geometric form and no circle. A sceptic case at the LIO pole on B, D and E without a mid-basin God."
  notes: ""

institutions:
  - {value: "Advocates Library, Edinburgh (Faculty of Advocates)", role: librarian, years: "1752–1757", kind: employer, certainty: 0.7, cites: [{source: S1, locator: "§1"}, {source: S7, locator: "MOL 11"}, {source: S9, locator: "opening"}], how_known: "Start: SEP and My Own Life ('In 1752, the Faculty of Advocates chose me their librarian'). End: Britannica's 'Adam Ferguson' says that in 1757 Ferguson succeeded 'his friend David Hume as keeper of the Advocates’ Library'. The earlier end year 1763 was the coder's inference from SEP and was wrong (lens audit #539)."}
  - {value: "British embassy in Paris", role: "private secretary to the British Ambassador", years: "1763–1766", kind: "government or state body", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP; end year from his return in 1766."}
collaborators:
  - {value: "Jean-Jacques Rousseau", roster_id: rousseau-jean-jacques, relation: other, note: "Hume hosted him in 1766; the relationship 'turned remarkably sour'", certainty: 1.0, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
  - {value: "Immanuel Kant", roster_id: kant-immanuel, relation: influenced, note: "woke Kant from his 'dogmatic slumber' (Kant's own admission)", certainty: 0.7, cites: [{source: S3, locator: "opening"}], how_known: "Britannica."}
  - {value: "Isaac Newton", roster_id: newton-isaac, relation: "influenced by", note: "took Newton's scientific method as his model", certainty: 0.7, cites: [{source: S3, locator: "opening"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 5: all five models).", certainty: 0.7, cites: [{source: S8, locator: "roster.csv, rank 21"}], how_known: "Study roster."}
  controversies:
    - {value: "His application for the Edinburgh Chair of Ethics and Pneumatical Philosophy (1745) was publicly opposed; his reputation as an atheist and sceptic dated from the Treatise. He failed again in 1751 for the Chair of Logic at Glasgow", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S3, locator: "'Early life and works'"}], how_known: "SEP. Britannica dates his candidacy for 'the chair of moral philosophy at Edinburgh' to 1744, with objectors alleging 'heresy and even atheism' (flagged; lens audit #545). Certainty left at 1.0 pending v8's ruling on whether such a date difference forces 0.7."}
  data_quality_flags:
    - "Age at Edinburgh University: eleven to fifteen (SEP) vs about 12 to 14 or 15 (Britannica)."
    - "Treatise publication: end of 1738 (My Own Life) vs 1739 (SEP)."
    - "Move to France: SEP says La Flèche in 1734; My Own Life says Rheims first, then chiefly La Flèche."
    - "Britannica read as its first page only. The Treatise and the essay 'Of the Immortality of the Soul' were not read."
    - "Edinburgh chair: Britannica dates his candidacy to 1744; SEP dates the opposed application to 1745 (lens audit #545)."
  open_questions:
    - "Fill AGNOS, SCEPT and ATHE; then recode primary_system."
    - "Read 'Of the Immortality of the Soul' to put C on his own words."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Hsueh Qu and Elizabeth S. Radcliffe"
    year: 2026
    citation: "Qu, Hsueh, and Elizabeth S. Radcliffe. \"David Hume.\" Stanford Encyclopedia of Philosophy (first published 16 Jun 2026). https://plato.stanford.edu/entries/hume/."
    url: "https://plato.stanford.edu/entries/hume/"
    accessed: 2026-10-02
    reliability_note: "Scholarly reference work; §1 and §5 read. Cited by section."
    used_for: [identity, basics, contribution, childhood, worldview, timing, lane_b, institutions, collaborators, review]
  - id: S2
    type: secondary
    kind: encyclopedia
    author: "Paul Russell and Anders Kraal"
    year: 2024
    citation: "Russell, Paul, and Anders Kraal. \"Hume on Religion.\" Stanford Encyclopedia of Philosophy (substantive revision 15 Nov 2024). https://plato.stanford.edu/entries/hume-religion/."
    url: "https://plato.stanford.edu/entries/hume-religion/"
    accessed: 2026-10-02
    reliability_note: "Scholarly reference work; §§4, 6, 7, 10, 11 read. Cited by section."
    used_for: [contribution, childhood, worldview, timing]
  - id: S3
    type: tertiary
    kind: encyclopedia
    author: "Maurice Cranston and Thomas Edmund Jessop"
    citation: "Cranston, Maurice, and Thomas Edmund Jessop. \"David Hume.\" Encyclopaedia Britannica. https://www.britannica.com/biography/David-Hume."
    url: "https://www.britannica.com/biography/David-Hume"
    accessed: 2026-10-02
    reliability_note: "Signed article; first page only. Cited by section heading."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, lane_b, collaborators]
  - id: S4
    type: primary
    kind: "scholarly edition"
    author: "David Hume"
    year: 1748
    citation: "Hume, David. An Enquiry concerning Human Understanding. Edited text at Hume Texts Online, ed. Peter Millican and Amyas Merivale. https://davidhume.org/texts/e/."
    url: "https://davidhume.org/texts/e/10"
    accessed: 2026-10-02
    reliability_note: "Edited scholarly text with paragraph numbers (E section.paragraph) and SBN page references; Sections 9–12 read."
    used_for: [contribution, worldview, timing, lane_b]
  - id: S5
    type: primary
    kind: "scholarly edition"
    author: "David Hume"
    year: 1779
    citation: "Hume, David. Dialogues concerning Natural Religion. Edited text at Hume Texts Online. https://davidhume.org/texts/d/12."
    url: "https://davidhume.org/texts/d/12"
    accessed: 2026-10-02
    reliability_note: "Edited scholarly text with paragraph numbers (D part.paragraph) and Kemp Smith (KS) page references; Parts 2 and 12 read."
    used_for: [contribution, worldview, lane_b]
  - id: S6
    type: primary
    kind: "scholarly edition"
    author: "David Hume"
    year: 1757
    citation: "Hume, David. The Natural History of Religion. Edited text at Hume Texts Online. https://davidhume.org/texts/n/15."
    url: "https://davidhume.org/texts/n/15"
    accessed: 2026-10-02
    reliability_note: "Edited scholarly text with paragraph numbers (N section.paragraph) and Beauchamp (Bea) page references; Section 15 read."
    used_for: [contribution, worldview, lane_b]
  - id: S7
    type: primary
    kind: "scholarly edition"
    author: "David Hume"
    year: 1777
    citation: "Hume, David. \"My Own Life\" (1776, published 1777). Edited text at Hume Texts Online. https://davidhume.org/texts/mol."
    url: "https://davidhume.org/texts/mol"
    accessed: 2026-10-02
    reliability_note: "Edited text with paragraph numbers (MOL n) and Miller (Mil) page references; paragraphs 1–6 read. Autobiography, so self-report."
    used_for: [basics, contribution, childhood, worldview, heritage, timing]
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
    type: tertiary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "Britannica Editors. \"Adam Ferguson.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Adam-Ferguson."
    url: "https://www.britannica.com/biography/Adam-Ferguson"
    accessed: 2026-10-02
    reliability_note: "Short article written by Britannica Editors (main text, not an AI box); used only for the year Ferguson succeeded Hume as keeper of the Advocates' Library (lens audit #539)."
    used_for: [institutions]
---

# David Hume

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

David Hume (1711–1776), Scottish philosopher, historian and essayist, gave the classic empiricist accounts of causation and induction and the classic critiques of miracle reports and the design argument [S1; S2; S3]. Laws of nature rest on uniform experience, and no testimony can ground a religion on a miracle [S4, E 10.12, 10.36]. primary_system BELOW_THRESHOLD (candidate codes are stubs). Axes A 3 and C 4 at 0.5; B 4, D 4, E 4 at 0.7; mid_basin BELOW_THRESHOLD (draft).

## Life and work

Edinburgh University in his early teens; the Treatise written in France (1734–1737); Essays, Enquiries and the History of England; Advocates Library 1752–1757 [S9]; Paris embassy 1763–1766; Dialogues published after his death [S1, §1; S7].

## Contribution and impact

Causation and induction; miracles; the Dialogues; sentimentalist ethics [S1; S2; S3].

## Childhood and education

His father died when he was about two; his widowed mother raised and taught him; he preferred Cicero and Virgil to law [S3; S7, MOL 3].

## Adult working worldview

"A wise man [...] proportions his belief to the evidence" [S4, E 10.4]. On religion: "Doubt, uncertainty, suspence of judgment" [S6, N 15.13]. Scholars read him as sceptic, thin theist, atheist or irreligious [S2, §§10–11].

## Heritage (context only)

Scottish gentry family [S7, MOL 2]. Context only.

## Timing

First lasting contribution: the Treatise (1738/1739) [S1; S7].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No geometric form; no circle [S4; S6].

## Open questions

- Fill AGNOS, SCEPT, ATHE; read the Treatise and "Of the Immortality of the Soul".

## Research log

- 2026-10-02: Read SEP "David Hume" (Qu, §1, §5), SEP "Hume on Religion" (Russell, §§4, 6, 7, 10, 11), Britannica (Cranston, first page) and, at Hume Texts Online, Enquiry §§9–12, Dialogues Parts 2 and 12, Natural History §15 and My Own Life 1–6. Wikipedia not used.
- 2026-10-02 (lens audit fixes): Read Britannica "Adam Ferguson" (Britannica Editors) for the 1757 succession, Enquiry E 11.24–25 and E 12.24–25 (Hume Texts Online), and the Britannica 1744 candidacy sentence ("Early life and works").
