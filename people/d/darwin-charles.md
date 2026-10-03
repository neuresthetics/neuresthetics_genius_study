---
record:
  record_type: person
  schema_version: "1.2"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch B)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (stage 3 batch B). Basics from Britannica (Desmond, first page). Worldview from the Autobiography (Barlow ed. 1958, Darwin Online; pp. 87 and 94 checked on the page scans), three letters in the Darwin Correspondence Project (Gray 1860, Fordyce 1879, McDermott 1880), the DCP essay 'What did Darwin believe?', the Origin (1859, p. 488 checked on the scan) and the Descent (1871). primary_system BELOW_THRESHOLD (AGNOS candidate, stub). A 2 (0.7), B 4 (0.7), C 4 (0.7), D 4 (0.7), E 4 (0.7); mid_basin TODO (A = 2). All scores are drafts for v8's review. Not reviewed."}

identity:
  id: darwin-charles
  display_name: "Charles Darwin"
  roster:
    canonical_name: "Charles Darwin"
    rank: 16
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: biology
    field_bucket: "biology / life science"
  full_name: {value: "Charles Robert Darwin", certainty: 0.7, cites: [{source: S8, locator: "'Also known as' line"}], how_known: "Britannica only."}
  native_name: {value: "Charles Robert Darwin (English)", certainty: 0.7, cites: [{source: S8, locator: "'Also known as' line"}], how_known: "English name."}
  aliases:
    - {name: "Charles-Darwin", kind: "roster alias"}
    - {name: "Darwin-Charles", kind: "roster alias"}

basics:
  birth:
    date: {value: "1809-02-12", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "p. 21"}, {source: S8, locator: "Born line"}], how_known: "His own statement and Britannica agree."}
    place: {value: "Shrewsbury", modern_name: "Shrewsbury, Shropshire, England, UK", polity_then: "United Kingdom", certainty: 1.0, cites: [{source: S1, locator: "p. 21"}, {source: S8, locator: "Born line"}], how_known: "Two sources agree."}
  death:
    date: {value: "1882-04-19", calendar: gregorian, certainty: 0.7, cites: [{source: S8, locator: "Died line"}], how_known: "Britannica only."}
    place: {value: "Downe, Kent", modern_name: "Downe, London Borough of Bromley, England, UK", polity_then: "United Kingdom", certainty: 0.7, cites: [{source: S8, locator: "Died line"}], how_known: "Britannica only."}
  first_lasting_contribution_year:
    value: 1859
    certainty: 0.7
    cites: [{source: S8, locator: "opening ('formulated his bold theory in private in 1837–39 ... On the Origin of Species (1859)')"}, {source: S6, locator: "title page"}]
    how_known: "Public statement of the theory of evolution by natural selection in the Origin. Judgment call (draft): the public, lasting statement is used rather than the private formulation."
    alternatives:
      - {value: 1837, cites: [{source: S8, locator: "opening"}], note: "Private formulation 1837–39 (Britannica). This would move era_bucket to '1750 to 1849'. Earlier published work (e.g. the Beagle geology) was not checked in a source read."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S8, locator: "opening"}], how_known: "From first_lasting_contribution_year (P2). Sits on an era boundary; see the alternative year (flagged as a method question)."}
  region_of_birth: {value: "Northern Europe", certainty: 1.0, cites: [{source: S8, locator: "Born line"}], how_known: "UK is Northern Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 1.0, cites: [{source: S8, locator: "opening; Died line"}], how_known: "Worked in England (Down House, Kent) after the Beagle voyage."}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S8, locator: "opening"}], how_known: "As the sources record it."}
  languages_of_work: {value: [English], certainty: 1.0, cites: [{source: S6, locator: "title page"}], how_known: "His books are in English."}
  occupations: {value: ["naturalist", "geologist"], certainty: 0.7, cites: [{source: S8, locator: "opening"}], how_known: "Britannica."}

contribution:
  fields: {value: ["natural history", "evolutionary biology", "geology"], certainty: 0.7, cites: [{source: S8, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Theory of evolution by natural selection", year: "1859", kind: theory, lasting: "foundation of modern biology", certainty: 1.0, cites: [{source: S6, locator: "pp. 488–490"}, {source: S8, locator: "opening"}], how_known: "His own book and Britannica."}
    - {value: "Descent of humans from earlier, less highly organised forms", year: "1871", kind: theory, lasting: "standard biology", certainty: 1.0, cites: [{source: S7, locator: "vol. 2, p. 385"}], how_known: "His own book."}
  evidence_of_impact:
    - {value: "Burial in Westminster Abbey", kind: other, certainty: 0.7, cites: [{source: S8, locator: "opening ('accorded the ultimate British accolade of burial in Westminster Abbey')"}], how_known: "Britannica; a posthumous honour."}
  major_works:
    - {value: "On the Origin of Species by Means of Natural Selection", year: 1859, kind: book, certainty: 1.0, cites: [{source: S6, locator: "title page"}, {source: S8, locator: "opening"}], how_known: "Read on Darwin Online."}
    - {value: "The Descent of Man, and Selection in Relation to Sex", year: 1871, kind: book, certainty: 1.0, cites: [{source: S7, locator: "vol. 2"}], how_known: "Read on Darwin Online."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Founder of the theory of evolution by natural selection.", certainty: 1.0, cites: [{source: S8, locator: "opening"}], how_known: "Sources agree."}

childhood:
  family_religion: {value: "Mixed: Unitarian mother; the children christened in the Church of England", certainty: 0.7, cites: [{source: S1, locator: "pp. 22–23, Francis Darwin's note"}, {source: S8, locator: "'Early life and education'"}], how_known: "Francis Darwin's note in the Autobiography: 'Mrs. Darwin was a Unitarian'; 'both he and his brother were christened and intended to belong to the Church of England'. Britannica: mother the daughter of 'the Unitarian pottery industrialist Josiah Wedgwood'."}
  family_religious_practice: {value: "As a small child he went to the school of the Unitarian minister, Mr Case", certainty: 0.7, cites: [{source: S1, locator: "pp. 22–23"}], how_known: "Autobiography and Francis Darwin's note."}
  parents_and_household:
    - {value: "Father, Robert Waring Darwin, society doctor", name: "Robert Waring Darwin", role: father, certainty: 0.7, cites: [{source: S8, locator: "'Early life and education'"}], how_known: "Britannica."}
    - {value: "Mother, Susannah Wedgwood, daughter of Josiah Wedgwood; died July 1817, when he was eight", name: "Susannah Darwin (née Wedgwood)", role: mother, certainty: 0.7, cites: [{source: S8, locator: "'Early life and education'"}, {source: S1, locator: "p. 22"}], how_known: "Britannica (name); Autobiography (death)."}
  household_circumstances: {value: "Prosperous medical family; second son", certainty: 0.7, cites: [{source: S8, locator: "'Early life and education'"}], how_known: "Britannica."}
  schooling:
    - {value: "Shrewsbury School (Anglican; classics by rote)", stage: "grammar or secondary school", years: "1818–1825", certainty: 0.7, cites: [{source: S8, locator: "'Early life and education'"}], how_known: "Britannica."}
    - {value: "Euclid with a private tutor", stage: tutor, years: TODO, certainty: 1.0, cites: [{source: S1, locator: "p. 43"}], how_known: "His own account."}
    - {value: "University of Edinburgh, medicine", stage: university, years: "1825–1827", certainty: 0.7, cites: [{source: S8, locator: "'Early life and education'"}], how_known: "Britannica ('his two years at Edinburgh')."}
    - {value: "Christ's College, Cambridge (intended for the church)", stage: university, years: "1828–", certainty: 0.7, cites: [{source: S8, locator: "'Early life and education'"}], how_known: "Britannica."}
  early_mathematics: {value: "geometry (Euclid-style proof)", note: "'I was taught Euclid by a private tutor, and I distinctly remember the intense satisfaction which the clear geometrical proofs gave me.'", certainty: 1.0, cites: [{source: S1, locator: "p. 43"}], how_known: "His own account."}
  early_geometric_style_reasoning: {value: "Euclid with a tutor at school; at Cambridge, Paley's Evidences and Natural Theology, whose logic 'gave me as much delight as did Euclid'", certainty: 0.7, cites: [{source: S1, locator: "pp. 43, 59"}], how_known: "His own account; the Cambridge reading falls just after 17."}
  early_science_exposure:
    - {value: "Edinburgh: dissenting science and Robert Edmond Grant", year: 1825, age: 16, certainty: 0.7, cites: [{source: S8, locator: "'Early life and education'"}], how_known: "Britannica."}
  key_early_reading:
    - {value: "Paley, Evidences of Christianity and Natural Theology (Cambridge)", certainty: 1.0, cites: [{source: S1, locator: "p. 59"}], how_known: "His own account."}
  childhood_mentors: []
  languages_in_childhood: {value: [English], certainty: 0.7, cites: [{source: S8, locator: "'Early life and education'"}], how_known: "English family."}
  notable_events:
    - {value: "Death of his mother", year: "1817", age: 8, certainty: 1.0, cites: [{source: S1, locator: "p. 22"}], how_known: "His own account."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1831–1882", certainty: 0.7, cites: [{source: S8, locator: "opening"}], how_known: "From the Beagle voyage to his death."}
  nominal_affiliations: []
  self_described_science_religion_relation:
    value: "Laws of nature leave no room for design in variation or for miracles ('Everything in nature is the result of fixed laws'; 'the more we know of the fixed laws of nature the more incredible do miracles become'), while the first cause stays an open question: 'The mystery of the beginning of all things is insoluble by us'. He held his theory compatible with theism ('absurd to doubt that a man may be an ardent Theist & an evolutionist')."
    certainty: 0.7
    cites: [{source: S1, locator: "pp. 86, 87, 94"}, {source: S2, locator: "letter text"}]
    how_known: "His own private writing (Autobiography for his family; private letter)."
  primary_system:
    value: BELOW_THRESHOLD
    cites: [{source: S1, locator: "pp. 92–94"}, {source: S2, locator: "letter text"}]
    how_known: "Best fit is AGNOS: 'I for one must be content to remain an Agnostic' (S1, p. 94) and 'an agnostic would be the most correct description of my state of mind' (S2, 1879). AGNOS is a stub system file, so it is not coded (batch rule); on the evidence it would be AGNOS at 0.7 (consistent_private_letters)."
    note: "Draft judgment (one line): coded BELOW_THRESHOLD only because the AGNOS file is a stub; backlog note raised."
  secondary_system: {value: UNKNOWN, how_known: "No second system in what was read."}
  candidate_codes_considered:
    - {code: AGNOS, reason: "Best fit, not coded because AGNOS is a stub system file (flag): his own late self-description in private writing (S1, p. 94; S2). The DCP editors add: 'Is he then an agnostic? Yes, but not all of the time' (S5).", cites: [{source: S1, locator: "p. 94"}, {source: S2, locator: "letter text"}, {source: S5, locator: "section on the Fordyce letter"}]}
    - {code: DEISM, reason: "Considered: in the Origin species arise by 'secondary causes' under 'laws impressed on matter by the Creator' (S6, p. 488), and he wrote to Gray of 'designed laws' (S3); around the Origin he 'deserve[d] to be called a Theist' (S1, p. 93). Rejected as his adult working view: that conclusion 'very gradually with many fluctuations become weaker' (S1, p. 93), and he did not describe himself as a deist.", cites: [{source: S6, locator: "p. 488"}, {source: S3, locator: "letter text"}, {source: S1, locator: "pp. 92–93"}]}
    - {code: CHRIST, reason: "Rejected: 'quite orthodox' only on the Beagle (S1, p. 85); later 'I do not believe in the Bible as a divine revelation, & therefore not in Jesus Christ as the son of God' (S4).", cites: [{source: S1, locator: "p. 85"}, {source: S4, locator: "letter text"}]}
    - {code: ATHE, reason: "Rejected: 'In my most extreme fluctuations I have never been an atheist in the sense of denying the existence of a God' (S2). ATHE is a stub system file (flag).", cites: [{source: S2, locator: "letter text"}]}
  lio_axes:
    A_locus:
      value: 2
      basis: consistent_private_letters
      certainty: 0.7
      cites: [{source: S1, locator: "pp. 92–94"}, {source: S2, locator: "letter text"}, {source: S3, locator: "letter text"}]
      how_known: "His own private writing, consistent across the Autobiography and two letters (ceiling 0.7); named alternatives also cap it at 0.7."
      rationale: "Draft judgment (one line): mixed, because his view moved between a First Cause 'having an intelligent mind in some degree analogous to that of man' acting only through 'designed laws' (S1, pp. 92–93; S3) and suspended judgment ('insoluble by us', S1, p. 94; S2). Named alternatives: 1, if the Origin-era theism is taken as the working view; BELOW_THRESHOLD, if late agnosticism is read as declining to place God at all."
    B_cause:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S6, locator: "pp. 488–490"}, {source: S1, locator: "pp. 86–87"}, {source: S3, locator: "letter text"}]
      how_known: "His own published book (p. 488 checked on the scan), matched by his private writing. A named alternative, so 0.7, not 1.0 (CODING_GUIDE §3)."
      rationale: "Scored on his account of nature (P6). Species arise by 'secondary causes, like those determining the birth and death of the individual' (S6, p. 488) and 'have all been produced by laws acting around us' (S6, p. 489); privately, 'Everything in nature is the result of fixed laws' (S1, p. 87). No miracle, petition or exemption in his account of living things after their beginning, so the LIO pole. Named alternative: 3, because the same book leaves the beginning outside the laws: 'the first creature [...] was created' (S6, p. 488) and life was 'originally breathed into a few forms or into one' (S6, p. 490)."
    C_ledger:
      value: 4
      basis: consistent_private_letters
      certainty: 0.7
      cites: [{source: S1, locator: "pp. 87, 94"}, {source: S3, locator: "letter text"}]
      how_known: "His own private writing; a named alternative, so 0.7 in any case."
      rationale: "Draft judgment (one line): no moral reckoning in events or after death. 'The lightning kills a man, whether a good one or bad one, owing to the excessively complex action of natural laws' (S3); everlasting punishment is 'a damnable doctrine' (S1, p. 87). Named alternative: 3, since he did not deny a future life outright; he only lacked an 'assured and ever present belief in [...] a future existence with retribution and reward' (S1, p. 94)."
    D_authority:
      value: 4
      basis: consistent_private_letters
      certainty: 0.7
      cites: [{source: S1, locator: "pp. 85–86"}, {source: S4, locator: "letter text"}]
      how_known: "His own private writing (Autobiography and a private letter), ceiling 0.7."
      rationale: "Draft judgment (one line): revelation has no authority for him. The Old Testament 'was no more to be trusted than the sacred books of the Hindoos' (S1, p. 85); miracles become more incredible as we know 'the fixed laws of nature' (S1, p. 86); 'I do not believe in the Bible as a divine revelation' (S4)."
    E_scope:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S6, locator: "pp. 488–489"}, {source: S7, locator: "vol. 2, p. 385"}, {source: S3, locator: "letter text"}]
      how_known: "His published books for humans under the same laws as other organisms; the 'no favour in events' part comes from a private letter, and there is a named alternative, so 0.7 (not 1.0)."
      rationale: "Scored on the world's order (P7). The same laws for all kinds, humans included: 'Light will be thrown on the origin of man and his history' (S6, p. 488); 'man is descended from some less highly organised form' (S7, p. 385); and events fall on the good and the bad alike (S3). Named alternative: 3, because in 1860 he still allowed that all these laws 'may have been expressly designed by an omniscient Creator' (S3); design of the whole is not favour for a group, so it is not preferred."
  mid_basin: {value: TODO, how_known: "A_locus = 2: the P4 test has no branch for A = 2 (false needs A ≥ 3, or A ≤ 1 with B ≤ 1), so TODO by the batch rule. If v8 takes the named alternative A = 1 at 0.7 with B 4 at 0.7, mid_basin would be true."}
  statements:
    - text: "Whilst on board the Beagle I was quite orthodox"
      cites: [{source: S1, locator: "p. 85"}]
      date: "1876"
      context: "Autobiography, section 'Religious Belief'; written late in life for his family (S5). Date: the main narrative was written May–August 1876 (Barlow's preface, p. 5); later addenda were inserted up to 1882, and which passages are addenda was not checked page by page."
      axes: [D_authority]
      kind: "notebook or diary"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "But I had gradually come, by this time, to see that the Old Testament from its manifestly false history of the world, with the Tower of Babel, the rainbow as a sign, etc., etc., and from its attributing to God the feelings of a revengeful tyrant, was no more to be trusted than the sacred books of the Hindoos, or the beliefs of any barbarian."
      cites: [{source: S1, locator: "p. 85"}]
      date: "1876"
      context: "Same section; on 1836–1839 ('these two years')."
      axes: [D_authority]
      kind: "notebook or diary"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "that the more we know of the fixed laws of nature the more incredible do miracles become"
      cites: [{source: S1, locator: "p. 86"}]
      date: "1876"
      context: "Same section; one of the reflections that led to disbelief in Christianity."
      axes: [B_cause, D_authority]
      kind: "notebook or diary"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "Thus disbelief crept over me at a very slow rate, but was at last complete. The rate was so slow that I felt no distress, and have never since doubted even for a single second that my conclusion was correct. I can indeed hardly see how anyone ought to wish Christianity to be true; for if so the plain language of the text seems to show that the men who do not believe, and this would include my Father, Brother and almost all my best friends, will be everlastingly punished. And this is a damnable doctrine."
      cites: [{source: S1, locator: "p. 87 (checked on the page scan)"}]
      date: "1876"
      context: "Same section. Emma Darwin's annotation (footnote on the same page) asked that this passage not be published; it was restored in the 1958 edition."
      axes: [C_ledger]
      kind: "notebook or diary"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
    - text: "There seems to be no more design in the variability of organic beings and in the action of natural selection, than in the course which the wind blows. Everything in nature is the result of fixed laws."
      cites: [{source: S1, locator: "p. 87 (checked on the page scan)"}]
      date: "1876"
      context: "Same section; on Paley's argument from design."
      axes: [B_cause]
      kind: "notebook or diary"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
    - text: "When thus reflecting I feel compelled to look to a First Cause having an intelligent mind in some degree analogous to that of man; and I deserve to be called a Theist."
      cites: [{source: S1, locator: "pp. 92–93"}]
      date: "1876"
      context: "Same section. The next sentence: this conclusion 'was strong in my mind about the time, as far as I can remember, when I wrote the Origin of Species; and it is since that time that it has very gradually with many fluctuations become weaker.'"
      axes: [A_locus]
      kind: "notebook or diary"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "I cannot pretend to throw the least light on such abstruse problems. The mystery of the beginning of all things is insoluble by us; and I for one must be content to remain an Agnostic."
      cites: [{source: S1, locator: "p. 94 (checked on the page scan)"}]
      date: "1876"
      context: "Same section, closing the discussion of a First Cause."
      axes: [A_locus]
      kind: "notebook or diary"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
    - text: "I cannot persuade myself that a beneficent & omnipotent God would have designedly created the Ichneumonidæ with the express intention of their feeding within the living bodies of caterpillars, or that a cat should play with mice."
      cites: [{source: S3, locator: "letter text"}]
      date: "1860-05-22"
      context: "Private letter to Asa Gray; DCP dates it 22 May [1860]."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "I am inclined to look at everything as resulting from designed laws, with the details, whether good or bad, left to the working out of what we may call chance. Not that this notion at all satisfies me. I feel most deeply that the whole subject is too profound for the human intellect."
      cites: [{source: S3, locator: "letter text"}]
      date: "1860-05-22"
      context: "Same letter."
      axes: [A_locus, B_cause]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "The lightning kills a man, whether a good one or bad one, owing to the excessively complex action of natural laws"
      cites: [{source: S3, locator: "letter text"}]
      date: "1860-05-22"
      context: "Same letter; he goes on that 'all these laws may have been expressly designed by an omniscient Creator, who foresaw every future event & consequence.'"
      axes: [C_ledger, E_scope]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "In my most extreme fluctuations I have never been an atheist in the sense of denying the existence of a God.— I think that generally (& more and more so as I grow older) but not always, that an agnostic would be the most correct description of my state of mind."
      cites: [{source: S2, locator: "letter text"}]
      date: "1879-05-07"
      context: "Private letter to John Fordyce, who had asked about his views; it opens 'It seems to me absurd to doubt that a man may be an ardent Theist & an evolutionist.—'"
      axes: [A_locus]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "I am sorry to have to inform you that I do not believe in the Bible as a divine revelation, & therefore not in Jesus Christ as the son of God."
      cites: [{source: S4, locator: "letter text"}]
      date: "1880-11-24"
      context: "Private letter to Frederick McDermott, who had asked whether he believed in the New Testament (DCP footnote)."
      axes: [D_authority]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "To my mind it accords better with what we know of the laws impressed on matter by the Creator, that the production and extinction of the past and present inhabitants of the world should have been due to secondary causes, like those determining the birth and death of the individual."
      cites: [{source: S6, locator: "p. 488 (checked on the page scan)"}]
      date: "1859"
      context: "Origin of Species, first edition, final chapter."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-02
    - text: "have all been produced by laws acting around us."
      cites: [{source: S6, locator: "p. 489"}]
      date: "1859"
      context: "Origin, first edition, the 'entangled bank' passage."
      axes: [B_cause, E_scope]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
    - text: "The main conclusion arrived at in this work, and now held by many naturalists who are well competent to form a sound judgment, is that man is descended from some less highly organised form."
      cites: [{source: S7, locator: "vol. 2, p. 385"}]
      date: "1871"
      context: "Descent of Man, first edition, 'General summary and conclusion'."
      axes: [E_scope]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-02
  changes_over_life:
    - {value: "Orthodox Christian on the Beagle; disbelief in Christianity came slowly over the following years 'but was at last complete'", year: "1836–1839 onward", certainty: 0.7, cites: [{source: S1, locator: "pp. 85–87"}], how_known: "His own retrospective account (private writing)."}
    - {value: "Theist (a First Cause with an intelligent mind) around the writing of the Origin; this 'very gradually with many fluctuations' became weaker afterwards", year: "c. 1859 onward", certainty: 0.7, cites: [{source: S1, locator: "pp. 92–93"}], how_known: "His own retrospective account."}
    - {value: "Generally, 'but not always', agnostic in later life", year: "by 1879", certainty: 0.7, cites: [{source: S2, locator: "letter text"}, {source: S1, locator: "p. 94"}], how_known: "Private letter and Autobiography agree."}
  coder_notes: "AGNOS and ATHE are stub system files (flag); DEISM and CHRIST are drafts. The Autobiography is treated as private writing (basis consistent_private_letters): the DCP editors say it was 'intended for the highly select audience of his family and immediate social circle' and should not be read 'as a neutral account' (S5); flagged as a method question. The DCP essay also notes that 'His published writings are particularly reserved or altogether silent on religion' (S5). Darwin Online (Barlow 1958 and the Origin) and the DCP are scholarly editions, not unofficial web copies. Statement dates: Barlow's preface (S1, p. 5) says the main narrative was finished 'between May and August, 1876' and addenda were added during his last six years; a footnote on p. 92 marks one addendum near the First Cause passage, so that passage may be later than 1876."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "English; the Darwin and Wedgwood families", certainty: 0.7, cites: [{source: S8, locator: "'Early life and education'"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Unitarian mother; Church of England by christening", certainty: 0.7, cites: [{source: S1, locator: "pp. 22–23, Francis Darwin's note"}], how_known: "Francis Darwin's note."}
  baptism_or_initiation: {value: "Christened in the Church of England", certainty: 0.7, cites: [{source: S1, locator: "pp. 22–23, Francis Darwin's note"}], how_known: "Francis Darwin's note."}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1837–1871", certainty: 0.7, cites: [{source: S8, locator: "opening"}, {source: S7, locator: "vol. 2"}], how_known: "From the private formulation to the Descent."}
  age_at_first_lasting_contribution: {value: 50, certainty: 0.7, cites: [{source: S8, locator: "Born line; opening"}], how_known: "Born 12 February 1809; the Origin appeared in 1859, so 50 whatever the month (month not checked)."}
  first_evidence_of_lio_type_views: {value: "Late 1830s: disbelief in Christian revelation and miracles began after the Beagle voyage", certainty: 0.7, cites: [{source: S1, locator: "pp. 85–87"}], how_known: "His own retrospective account."}
  lio_views_relative_to_major_work: {value: "during major work", rationale: "Law-only account of nature from the private formulation (1837–39) through the Origin; doubts about revelation in the same years.", certainty: 0.7, cites: [{source: S1, locator: "pp. 85–87"}, {source: S8, locator: "opening"}], how_known: "Autobiography and Britannica."}
  worldview_during_major_work: {value: "Theist (First Cause) acting through laws, with growing agnosticism", certainty: 0.7, cites: [{source: S1, locator: "pp. 92–93"}], how_known: "His own account."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "He took 'intense satisfaction' in Euclid's proofs and delight in the logic of Paley (S1, pp. 43, 59), but his books argue from observation, not from definitions and axioms.", certainty: 0.5, cites: [{source: S1, locator: "pp. 43, 59"}], how_known: "Coder's reading."}
  form_acquired: {value: "childhood or adolescence", certainty: 0.5, cites: [{source: S1, locator: "p. 43"}], how_known: "Euclid at school."}
  circle_present: {value: "partly", rationale: "Laws 'impressed on matter by the Creator' (S6, p. 488) tie God and nature through law, but he later left the first cause 'insoluble' (S1, p. 94).", certainty: 0.5, cites: [{source: S6, locator: "p. 488"}, {source: S1, locator: "p. 94"}], how_known: "Coder's reading."}
  reading: "As belief, not finding: form partly present (early Euclid), circle partly present in the Origin years and fading after. The record does not test H1."
  notes: ""

institutions:
  - {value: "HMS Beagle survey voyage", role: "naturalist", years: "1831–1836", kind: other, certainty: 0.7, cites: [{source: S8, locator: "map caption 'HMS Beagle in 1831–36'"}], how_known: "Britannica."}
collaborators:
  - {value: "Asa Gray", relation: correspondent, note: "1860 letter on design", certainty: 1.0, cites: [{source: S3, locator: "letter text"}], how_known: "The letter."}
  - {value: "Robert Edmond Grant", relation: teacher, note: "Edinburgh", certainty: 0.7, cites: [{source: S8, locator: "'Early life and education'"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 5: Claude, DeepSeek, Gemini, GPT, Grok).", certainty: 0.7, cites: [{source: S9, locator: "roster.csv, rank 16"}], how_known: "Study roster."}
  controversies:
    - {value: "Whether his late view is agnostic or a fluctuating theism; the DCP editors answer 'Is he then an agnostic?' with 'Yes, but not all of the time'", certainty: 0.7, cites: [{source: S5, locator: "section on the Fordyce letter"}], how_known: "Project editors' essay."}
  data_quality_flags:
    - "Britannica read as its first page only."
    - "The Autobiography is private writing for his family (S5); it is treated as consistent_private_letters, not as a public profession."
    - "first_lasting_contribution_year sits on an era boundary (1859 public vs 1837–39 private)."
  open_questions:
    - "Should AGNOS be drafted so that Darwin can be coded (backlog)?"
    - "Which religion passages of the Autobiography are 1876 text and which are later addenda (Barlow, p. 5; footnote p. 92)."

sources:
  - id: S1
    type: primary
    kind: "scholarly edition"
    author: "Charles Darwin; ed. Nora Barlow"
    year: 1958
    citation: "Darwin, Charles. The Autobiography of Charles Darwin 1809–1882. With the original omissions restored. Edited by Nora Barlow. London: Collins, 1958. Darwin Online, item F1497. http://darwin-online.org.uk/content/frameset?itemID=F1497&viewtype=text&pageseq=1."
    url: "http://darwin-online.org.uk/content/frameset?itemID=F1497&viewtype=text&pageseq=1"
    accessed: 2026-10-02
    reliability_note: "Main narrative May–August 1876, addenda to 1882 (preface, p. 5). Darwin Online transcription of the printed edition; pp. 87 and 94 checked on the page scans (image seq 89 and 96). Written for his family, so private writing."
    used_for: [basics, childhood, worldview, heritage, timing, lane_b]
  - id: S2
    type: primary
    kind: letter
    author: "Charles Darwin"
    year: 1879
    citation: "Darwin, Charles. Letter to John Fordyce, 7 May 1879. Darwin Correspondence Project, letter no. DCP-LETT-12041 (source of text: Linnean Society of London, Quentin Keynes Collection). https://www.darwinproject.ac.uk/letter/DCP-LETT-12041.xml."
    url: "https://www.darwinproject.ac.uk/letter/DCP-LETT-12041.xml"
    accessed: 2026-10-02
    reliability_note: "Scholarly edition (Cambridge University Library)."
    used_for: [worldview]
  - id: S3
    type: primary
    kind: letter
    author: "Charles Darwin"
    year: 1860
    citation: "Darwin, Charles. Letter to Asa Gray, 22 May [1860]. Darwin Correspondence Project, letter no. DCP-LETT-2814. https://www.darwinproject.ac.uk/letter/DCP-LETT-2814.xml."
    url: "https://www.darwinproject.ac.uk/letter/DCP-LETT-2814.xml"
    accessed: 2026-10-02
    reliability_note: "Scholarly edition."
    used_for: [worldview, collaborators]
  - id: S4
    type: primary
    kind: letter
    author: "Charles Darwin"
    year: 1880
    citation: "Darwin, Charles. Letter to Frederick McDermott, 24 November 1880. Darwin Correspondence Project, letter no. DCP-LETT-12851 (source of text: Bonhams, New York, 2015). https://www.darwinproject.ac.uk/letter/DCP-LETT-12851.xml."
    url: "https://www.darwinproject.ac.uk/letter/DCP-LETT-12851.xml"
    accessed: 2026-10-02
    reliability_note: "Scholarly edition; text from a dealer's catalogue."
    used_for: [worldview]
  - id: S5
    type: secondary
    kind: "institutional page"
    author: "Darwin Correspondence Project (editors)"
    citation: "Darwin Correspondence Project. \"What did Darwin believe?\" University of Cambridge. https://www.darwinproject.ac.uk/commentary/religion/what-did-darwin-believe."
    url: "https://www.darwinproject.ac.uk/commentary/religion/what-did-darwin-believe"
    accessed: 2026-10-02
    reliability_note: "Unsigned essay by the project editors."
    used_for: [worldview, review]
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "Charles Darwin"
    year: 1859
    citation: "Darwin, Charles. On the Origin of Species by Means of Natural Selection. London: John Murray, 1859 (first edition). Darwin Online, item F373. http://darwin-online.org.uk/content/frameset?itemID=F373&viewtype=text&pageseq=1."
    url: "http://darwin-online.org.uk/content/frameset?itemID=F373&viewtype=text&pageseq=1"
    accessed: 2026-10-02
    reliability_note: "Darwin Online transcription; p. 488 checked on the page scan."
    used_for: [basics, contribution, worldview, lane_b]
  - id: S7
    type: primary
    kind: "published work by the subject"
    author: "Charles Darwin"
    year: 1871
    citation: "Darwin, Charles. The Descent of Man, and Selection in Relation to Sex. Vol. 2. London: John Murray, 1871. Darwin Online, item F937.2. http://darwin-online.org.uk/content/frameset?itemID=F937.2&viewtype=text&pageseq=1."
    url: "http://darwin-online.org.uk/content/frameset?itemID=F937.2&viewtype=text&pageseq=1"
    accessed: 2026-10-02
    reliability_note: "Darwin Online transcription (text only; scan not checked)."
    used_for: [contribution, worldview, timing]
  - id: S8
    type: tertiary
    kind: encyclopedia
    author: "Adrian J. Desmond"
    citation: "Desmond, Adrian J. \"Charles Darwin.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Charles-Darwin."
    url: "https://www.britannica.com/biography/Charles-Darwin"
    accessed: 2026-10-02
    reliability_note: "Signed article; first page only. Cited by section."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, institutions, collaborators]
  - id: S9
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
---

# Charles Darwin

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Charles Robert Darwin (1809–1882), English naturalist, set out the theory of evolution by natural selection in the Origin of Species (1859) [S6; S8]. In private writing he said that disbelief in Christianity "crept over me at a very slow rate, but was at last complete" [S1, p. 87], that he was a theist about the time of the Origin and later "content to remain an Agnostic" [S1, pp. 93–94], and that he had "never been an atheist in the sense of denying the existence of a God" [S2]. primary_system BELOW_THRESHOLD (best fit AGNOS, a stub). Draft scores: A 2 (0.7), B 4 (0.7), C 4 (0.7), D 4 (0.7), E 4 (0.7); mid_basin TODO because A = 2.

## Life and work

Born in Shrewsbury, he studied medicine at Edinburgh (1825) and went to Christ's College, Cambridge (1828), sailed on HMS Beagle (1831–36), formulated his theory privately in 1837–39 and published it in 1859 [S8]. The Descent of Man followed in 1871 [S7].

## Contribution and impact

Evolution by natural selection [S6, pp. 488–490] and the descent of humans from "some less highly organised form" [S7, vol. 2, p. 385]. He was buried in Westminster Abbey [S8].

## Childhood and education

His mother, a Wedgwood, was a Unitarian and died in 1817; the boys were christened in the Church of England [S1, pp. 22–23; S8]. He was taught Euclid by a private tutor and remembered "the intense satisfaction which the clear geometrical proofs gave me" [S1, p. 43]; at Cambridge, Paley's logic "gave me as much delight as did Euclid" [S1, p. 59].

## Adult working worldview

His account of nature is lawful throughout: species arise by "secondary causes" under "laws impressed on matter by the Creator" [S6, p. 488], and "Everything in nature is the result of fixed laws" [S1, p. 87]. He rejected revelation [S1, p. 85; S4] and eternal punishment [S1, p. 87]. On God he wavered between a First Cause "having an intelligent mind" [S1, pp. 92–93] and agnosticism [S1, p. 94; S2]. The Autobiography was written for his family and should not be read as a neutral account [S5].

## Heritage (context only)

Unitarian mother; Church of England by christening [S1, pp. 22–23]. Context only.

## Timing

First lasting contribution 1859 (public), or 1837–39 (private formulation) [S8]; the year sits on an era boundary.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form partly present (early Euclid [S1, p. 43]); circle partly present in the Origin years [S6, p. 488].

## Open questions

- AGNOS needs a sourced system file before Darwin can be coded.
- Which religion passages of the Autobiography are later addenda [S1, p. 5].

## Research log

- 2026-10-02: Read Britannica (Desmond, first page); the Autobiography on Darwin Online (pp. 87 and 94 checked on the scans); DCP letters 2814, 12041 and 12851 and the essay 'What did Darwin believe?'; the Origin (p. 488 checked on the scan) and the Descent, vol. 2.
