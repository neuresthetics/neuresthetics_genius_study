---
record:
  record_type: person
  schema_version: "1.0"
  record_version: 1
  review_status: "example — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, repo setup)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-01
  last_updated: 2026-10-01
  change_log:
    - {date: 2026-10-01, by: "Grok Bot", summary: "Worked example created to show the record structure. Only well-sourced fields filled; everything else TODO. Not reviewed."}

identity:
  id: faraday-michael
  display_name: "Michael Faraday"
  roster:
    canonical_name: "Michael Faraday"
    rank: 58
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: physics
    field_bucket: physics
  full_name: {value: "Michael Faraday", certainty: 1.0, cites: [{source: S1, locator: "opening sentence"}, {source: S2, locator: "Biography"}], how_known: "Both sources use this name; no other given names reported."}
  native_name: {value: "Michael Faraday", certainty: 1.0, cites: [{source: S1, locator: "opening sentence"}], how_known: "English was his language, so the native form is the roster name."}
  aliases:
    - {name: "Faraday-Michael", kind: "roster alias"}
    - {name: "Michael-Faraday", kind: "roster alias"}

basics:
  birth:
    date:
      value: "1791-09-22"
      certainty: 1.0
      cites: [{source: S1, locator: "opening sentence and Quick Facts"}, {source: S4, locator: "letter text: 'next Sabbath day (the 22nd) I shall complete my 70th year'"}]
      how_known: "Encyclopedia date, matched by Faraday's own statement in a letter of 19 Sept 1861."
      alternatives:
        - {value: "1791-09-21", cites: [{source: S5, locator: "p. 4, gravestone transcription"}], note: "Russell's transcription of the gravestone reads 'Born 21 September 1791'. Not checked against the stone or a photograph."}
    place:
      value: "Newington Butts, Surrey, England"
      modern_name: "Southwark, South London"
      polity_then: "Kingdom of Great Britain"
      certainty: 1.0
      cites: [{source: S1, locator: "opening sentence; Early life"}, {source: S2, locator: "Biography"}]
      how_known: "S1 says Newington, Surrey, 'now a part of South London'; S2 says Newington Butts, Southwark."
  death:
    date: {value: "1867-08-25", certainty: 1.0, cites: [{source: S1, locator: "opening sentence"}, {source: S5, locator: "p. 4"}], how_known: "Encyclopedia and a historian's paper agree."}
    place:
      value: "His house at Hampton Court, Surrey, England"
      modern_name: "Hampton Court, London Borough of Richmond upon Thames"
      certainty: 1.0
      cites: [{source: S1, locator: "opening sentence; Later life"}, {source: S2, locator: "Biography: 'a Grace and Favour House at Hampton Court where he died'"}]
      how_known: "Two independent summaries agree."
  first_lasting_contribution_year: {value: 1821, certainty: 1.0, cites: [{source: S1, locator: "Early life (electromagnetic rotation, 'the first electric motor')"}, {source: S2, locator: "Biography: 'electro-magnetic rotations (1821)'"}], how_known: "Both list the 1821 electromagnetic rotations as his first major discovery in electricity."}
  era_bucket: {value: "1750 to 1849", certainty: 1.0, cites: [{source: S1, locator: "Early life"}], how_known: "Derived from first_lasting_contribution_year (1821) under the proposed era buckets."}
  region_of_birth: {value: "Northern Europe", certainty: 1.0, cites: [{source: S1, locator: "opening sentence"}], how_known: "Born in England; England is Northern Europe under the proposed (UN M49-based) region list."}
  region_of_work: {value: "Northern Europe", certainty: 1.0, cites: [{source: S2, locator: "Ri positions"}], how_known: "His whole working life was at the Royal Institution in London."}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S2, locator: "Biography: 'the son of a Sandemanian blacksmith'"}, {source: S1, locator: "throughout ('he', 'his')"}], how_known: "As the sources record it."}
  languages_of_work: {value: [English], certainty: 1.0, cites: [{source: S2, locator: "Publications"}], how_known: "All his published books and paper collections are in English."}
  occupations:
    value: ["bookbinder (apprentice)", "chemist", "physicist", "public lecturer", "scientific adviser"]
    certainty: 1.0
    cites: [{source: S2, locator: "Biography and Ri positions"}, {source: S1, locator: "opening sentence"}]
    how_known: "From the Royal Institution's own list of his posts and the encyclopedia summary."

contribution:
  fields: {value: [chemistry, physics, electromagnetism, electrochemistry], certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}], how_known: "Encyclopedia summary."}
  lasting_original_contributions:
    - {value: "Electromagnetic rotation: the first electric motor", year: 1821, kind: invention, lasting: "the principle of the electric motor", certainty: 1.0, cites: [{source: S1, locator: "Early life"}, {source: S2, locator: "Biography"}], how_known: "Two summaries agree."}
    - {value: "Isolated and described benzene", year: 1825, kind: discovery, certainty: 1.0, cites: [{source: S1, locator: "Early life"}, {source: S2, locator: "Biography"}], how_known: "Two summaries agree."}
    - {value: "Electromagnetic induction (iron-ring experiment of 29 August 1831), then the first dynamo", year: 1831, kind: discovery, lasting: "generators and transformers rest on induction", certainty: 1.0, cites: [{source: S1, locator: "Early life (end)"}, {source: S2, locator: "Biography"}], how_known: "Two summaries agree; S1 gives the date of the experiment."}
    - {value: "Two laws of electrochemistry (electrolysis), and the words electrode, cathode, ion", year: "early 1830s", kind: "law or principle", certainty: 1.0, cites: [{source: S1, locator: "Theory of electrochemistry"}, {source: S2, locator: "Biography"}], how_known: "Two summaries agree."}
    - {value: "Specific inductive capacity of insulating materials", year: "by 1839", kind: discovery, certainty: 0.7, cites: [{source: S1, locator: "Theory of electrochemistry"}], how_known: "One encyclopedia source."}
    - {value: "Magneto-optical effect (rotation of polarized light by a magnetic field) and diamagnetism", year: 1845, kind: discovery, certainty: 1.0, cites: [{source: S1, locator: "Later life"}, {source: S2, locator: "Biography"}], how_known: "Two summaries agree."}
    - {value: "Field conception of electric and magnetic force: space as a medium carrying the strains of force", year: "by 1850", kind: theory, lasting: "Maxwell built his field equations on it", certainty: 1.0, cites: [{source: S1, locator: "Later life"}, {source: S2, locator: "Biography: 'thereafter formulating the field theory of electro-magnetism'"}], how_known: "Two summaries agree."}
  evidence_of_impact:
    - {value: "Maxwell took the basic ideas for his mathematical field theory from Faraday, and said so", kind: "assessment by a later major figure", certainty: 0.7, cites: [{source: S1, locator: "Later life"}], how_known: "Reported by the encyclopedia article; Maxwell's own words not checked here."}
    - {value: "Effects and laws carry his name: Faraday effect, Faraday's law of induction, Faraday's laws of electrolysis", kind: "named after them", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts: Subjects of study"}], how_known: "Listed by the encyclopedia."}
    - {value: "Founded the Royal Institution's Friday Evening Discourses and Christmas Lectures in the mid-1820s", kind: "institutional or technological lineage", certainty: 1.0, cites: [{source: S2, locator: "Biography"}], how_known: "The institution's own record."}
  major_works:
    - {value: "Chemical Manipulation, Being Instructions to Students in Chemistry", year: 1827, kind: book, certainty: 1.0, cites: [{source: S2, locator: "Publications"}], how_known: "Institution's bibliography; his only book."}
    - {value: "Experimental Researches in Electricity, vols I–III", year: "1837, 1844, 1855", kind: "paper or paper series", certainty: 1.0, cites: [{source: S2, locator: "Publications"}], how_known: "Institution's bibliography."}
    - {value: "Experimental Researches in Chemistry and Physics", year: 1859, kind: "paper or paper series", certainty: 1.0, cites: [{source: S2, locator: "Publications"}], how_known: "Institution's bibliography."}
    - {value: "A Course of Six Lectures on the Chemical History of a Candle (ed. W. Crookes)", year: 1861, kind: "lecture series", certainty: 1.0, cites: [{source: S2, locator: "Publications"}], how_known: "Institution's bibliography."}
  honours:
    - {value: "Copley Medal", year: "1832, 1838", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts: Awards and honors"}], how_known: "Encyclopedia fact box."}
    - {value: "Civil List pension", year: 1836, certainty: 1.0, cites: [{source: S2, locator: "Biography"}], how_known: "Institution's record."}
    - {value: "Twice offered the Presidency of the Royal Society; declined both times", certainty: 1.0, cites: [{source: S2, locator: "Biography"}, {source: S5, locator: "p. 4"}], how_known: "Two sources agree."}
    - {value: "Use of a Grace and Favour house at Hampton Court from the Queen", year: 1858, certainty: 1.0, cites: [{source: S2, locator: "Biography"}, {source: S1, locator: "Later life"}], how_known: "Two sources agree; S2 gives the year."}
  definition_fit: {value: "clearly meets", rationale: "Several discoveries still in use (induction, electrolysis laws, field concept), named effects, and Maxwell's acknowledged debt.", certainty: 1.0, cites: [{source: S1, locator: "opening paragraph; Later life"}], how_known: "Lane A definition (lasting original impact on documented criteria) applied to the contributions listed above."}

childhood:
  family_religion: {value: "Sandemanian (Glasite) Christian. The family had belonged to this small dissenting sect since his grandfather's generation.", certainty: 1.0, cites: [{source: S1, locator: "Early life"}, {source: S2, locator: "Biography: 'son of a Sandemanian blacksmith'"}, {source: S5, locator: "p. 1, 'The roots of Faraday's beliefs'"}], how_known: "Three sources agree on a Sandemanian family; S5 traces it to his grandfather Robert Faraday."}
  family_religious_practice: {value: "Attended the Sandemanian chapel in Paul's Alley, City of London, as a child (Russell calls it his 'childhood habit').", certainty: 0.7, cites: [{source: S5, locator: "p. 1"}], how_known: "One historian's summary; detail on frequency and form not given."}
  parents_and_household:
    - {value: "Father, James Faraday, a blacksmith who moved to London from the north of England in 1791", name: "James Faraday", role: father, certainty: 1.0, cites: [{source: S1, locator: "Early life"}, {source: S2, locator: "Biography"}, {source: S5, locator: "p. 1"}], how_known: "Three sources agree."}
    - {value: "Mother, Margaret; Michael was named after her father", name: "Margaret Faraday", role: mother, certainty: 0.7, cites: [{source: S5, locator: "p. 1"}], how_known: "One source gives her name and the naming."}
    - {value: "One of four children; the third child", role: sibling position, certainty: 0.7, cites: [{source: S1, locator: "Early life: 'one of four children'"}, {source: S5, locator: "p. 1: 'their third child'"}], how_known: "S1 gives four children; only S5 gives birth order."}
  household_circumstances: {value: "Poor: the father was often ill and unable to work steadily, and the children were often short of food.", certainty: 1.0, cites: [{source: S1, locator: "Early life"}, {source: S5, locator: "p. 1: 'early years of penury'"}], how_known: "Two sources agree."}
  schooling:
    - {value: "Only the rudiments: reading, writing and ciphering, learned in a church Sunday school", stage: "religious school", certainty: 0.7, cites: [{source: S1, locator: "Early life"}], how_known: "One encyclopedia source gives the content; S5 p. 1 confirms 'limited schooling' without detail."}
    - {value: "Apprenticed to the bookbinder and bookseller George Riebau", stage: apprenticeship, institution: "George Riebau, bookbinder", years: "1805–1812", ages: "14–21", certainty: 1.0, cites: [{source: S2, locator: "Biography"}, {source: S1, locator: "Early life: 'at the age of 14'"}], how_known: "Two sources agree."}
    - {value: "Educated himself during the apprenticeship by reading books brought in for rebinding", stage: self-directed, years: "1805–1812", certainty: 1.0, cites: [{source: S1, locator: "Early life"}, {source: S5, locator: "p. 1: 'attempts at self-education'"}], how_known: "Two sources agree."}
  early_mathematics: {value: "arithmetic only", description: "'ciphering' at Sunday school; no consulted source reports geometry or algebra teaching in childhood", certainty: 0.7, cites: [{source: S1, locator: "Early life"}], how_known: "Inferred from the only description of his schooling. Later limits on his mathematics are reported elsewhere but not checked here."}
  early_geometric_style_reasoning: {value: TODO, note: "Wikipedia says he read Isaac Watts's The Improvement of the Mind during his apprenticeship. Check that in Cantor 1991 or James 2010 before entering it, and say whether it involved definition-to-consequence practice."}
  early_science_exposure:
    - {value: "Read the article on electricity in the third edition of the Encyclopaedia Britannica", year: "1805–1812", age: "14–21", certainty: 0.7, cites: [{source: S1, locator: "Early life"}], how_known: "One source."}
    - {value: "Built a crude electrostatic generator from old bottles and lumber, and a weak voltaic pile for electrochemistry experiments", year: "1805–1812", age: "14–21", certainty: 0.7, cites: [{source: S1, locator: "Early life"}], how_known: "One source."}
    - {value: "Attended Humphry Davy's chemistry lectures at the Royal Institution, took notes, and sent Davy a bound copy with a request for work", year: 1812, age: "about 20–21", certainty: 0.7, cites: [{source: S1, locator: "Early life"}, {source: S2, locator: "Biography (apprenticeship ended 1812)"}], how_known: "S1 describes the lectures as happening during the apprenticeship, which S2 dates as ending in 1812; the year is therefore inferred."}
  key_early_reading:
    - {value: "Encyclopaedia Britannica, 3rd edition, article 'Electricity'", certainty: 0.7, cites: [{source: S1, locator: "Early life"}], how_known: "One source."}
  childhood_mentors:
    - {value: "George Riebau, the master bookbinder he was apprenticed to, and who first employed him to deliver newspapers", name: "George Riebau", years: "1805–1812", certainty: 0.7, cites: [{source: S2, locator: "Biography"}, {source: S1, locator: "Early life"}], how_known: "S2 names Riebau; S1 says he first delivered newspapers for the book dealer he was later apprenticed to. That this is the same man is read across the two sources."}
  languages_in_childhood: {value: TODO}
  notable_events:
    - {value: "Delivered newspapers for a book dealer and bookbinder before his apprenticeship", age: "before 14", certainty: 0.7, cites: [{source: S1, locator: "Early life"}], how_known: "One source."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1813–1865", certainty: 1.0, cites: [{source: S2, locator: "Ri positions"}, {source: S5, locator: "p. 4: stepped down as Superintendent in 1865"}], how_known: "From his appointment at the Royal Institution in 1813 to his last posts in 1865."}
  nominal_affiliations:
    - {value: "Joined the Sandemanian church by confession of faith within days of his marriage (12 June 1821)", year: 1821, role: member, certainty: 0.7, cites: [{source: S5, locator: "p. 2"}], how_known: "One historian's account."}
    - {value: "Deacon", year: 1832, role: deacon, certainty: 0.7, cites: [{source: S5, locator: "p. 2"}], how_known: "One source."}
    - {value: "Elder; he preached ('exhortations') at Sandemanian meetings", year: 1840, role: elder, certainty: 0.7, cites: [{source: S5, locator: "p. 2"}], how_known: "One source."}
    - {value: "Excluded from the Sandemanians in 1844", year: 1844, certainty: 0.7, cites: [{source: S6, locator: "article title"}], how_known: "Stated in the title of a history-of-science journal article. The article body (reasons, and the readmission) was not read."}
    - {value: "Resigned his eldership", year: 1864, certainty: 0.7, cites: [{source: S5, locator: "p. 4"}], how_known: "One source."}
  self_described_science_religion_relation:
    value: "In conversation and correspondence he kept religion and natural philosophy apart ('two distinct things'), while holding that the works of God cannot contradict the higher things of faith."
    certainty: 0.7
    cites: [{source: S3, locator: "final paragraph"}]
    how_known: "His own words in a private letter (see statements). How far the separation went in his scientific thinking is disputed by historians."
    alternatives:
      - {value: "Convergent reading: his science and faith interacted (vocation, unity of forces, point-centre atoms and fields).", cites: [{source: S5, locator: "pp. 2–3"}], note: "Russell's argument against taking the 'two distinct things' sentence as the whole story."}
  primary_system: {value: TODO, note: "Not coded in this example. Coding needs a reviewed pass under docs/CODING_GUIDE.md. See candidate_codes_considered."}
  secondary_system: {value: TODO}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Practising member and elder of a Christian church; hope 'founded on the faith that is in Christ' (S3).", cites: [{source: S3, locator: "final paragraph"}, {source: S5, locator: "p. 2"}]}
    - {code: CLTHEI, reason: "Russell describes the church as evangelical and strongly Calvinist, appealing to biblical authority (p. 1), and quotes J. M. Thomas that Faraday accepted the literal truth of the Bible (p. 2). Check whether his written views include petition, providence or miracle.", cites: [{source: S5, locator: "pp. 1–2"}]}
    - {code: CLASS_THEISM, reason: "Listed only to rule in or out. Nothing consulted shows an Aristotelian-Thomistic or falsafa framework; Russell reads 'no philosophy in my religion' as denying that natural knowledge could lead to God.", cites: [{source: S5, locator: "p. 2, 'Natural theology'"}]}
  lio_axes:
    A_locus: {value: TODO}
    B_cause: {value: TODO, note: "Evidence to weigh: his search for one convertible force behind all phenomena (S1 Later life) and the point-centre memorandum invoking God (S5 p. 3), against acceptance of the literal truth of the Bible (S5 p. 2)."}
    C_ledger: {value: TODO, note: "Evidence to weigh: his hope of a future life and 'the rest' (S4); his exhortations as elder (S5 p. 2) and Bible markings (S5 p. 4)."}
    D_authority: {value: TODO, note: "Evidence to weigh: S5 p. 2 says he held revelation 'through the Bible or through experiment' and rejected natural theology."}
    E_scope: {value: TODO}
  mid_basin: {value: TODO, note: "The v7.1 coding rules name Faraday among the 'mid-basin theists coded first'. That is the study's starting designation, not a coded result, so it is not entered as a value here."}
  statements:
    - text: "There is no philosophy in my religion[.] I am of a very small & despised sect of christians known, if known at all, as Sandemanians and our hope is founded on the faith that is in Christ. But though the natural works of God can never by any possibility come in contradiction with the higher things that belong to our future existence, and must with every thing concerning Him ever glorify him still I do not think it at all necessary to tie the study of the natural sciences & religion together and in my intercourse with my fellow creatures that which is religious & that which is philosophical have ever been two distinct things[.]"
      cites: [{source: S3, locator: "final paragraph (from Faraday's own copy, IEE MS SC 3, per the edition's note 4)"}]
      date: "1844-10-24"
      context: "Reply to Ada Lovelace, who had asked about his religion and offered to work through his experiments with him."
      axes: [D_authority, A_locus]
      kind: "private letter"
      verified_against: "primary transcription"
      verified_on: 2026-10-01
    - text: "I am, I hope, very thankful that in the withdrawal of the powers & things of this life,- the good hope is left with me, which makes the contemplation of death a comfort - not a fear. Such peace is alone in the gift of God; and as it is he who gives it, why should we be afraid? His unspeakable gift in his beloved son is the ground of no doubtful hope;- and there is the rest for those who like you & me are drawing near the latter end of our terms here below.-"
      cites: [{source: S4, locator: "first paragraph"}]
      date: "1861-09-19"
      context: "Letter to his friend and fellow physicist Auguste De La Rive, three days before his 70th birthday."
      axes: [C_ledger]
      kind: "private letter"
      verified_against: "primary transcription"
      verified_on: 2026-10-01
  changes_over_life: []
  coder_notes: "Example record. No code or axis score has been entered. The quotes are transcriptions from the edited correspondence (Epsilon), not checked against the manuscripts."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "English", certainty: 1.0, cites: [{source: S1, locator: "opening sentence"}], how_known: "Encyclopedia."}
  religious_heritage_by_birth: {value: "Sandemanian family, from at least his grandfather Robert Faraday; part of a long family tradition of religious dissent from the Church of England", certainty: 0.7, cites: [{source: S5, locator: "p. 1"}], how_known: "One historian's account of the family."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1821–c. 1855", certainty: 0.7, cites: [{source: S1, locator: "Early life (1821); Later life ('About 1855, Faraday's mind began to fail')"}], how_known: "Coder's summary of the dates in S1."}
  age_at_first_lasting_contribution: {value: 29, certainty: 0.7, cites: [{source: S1, locator: "opening sentence; Early life"}], how_known: "1821 minus 1791. The month of the rotation experiment was not checked, so it may be 30."}
  first_evidence_of_lio_type_views: {value: TODO}
  lio_views_relative_to_major_work: {value: TODO}
  worldview_during_major_work: {value: "A practising Sandemanian throughout: member from 1821, deacon 1832, elder 1840.", certainty: 0.7, cites: [{source: S5, locator: "p. 2"}], how_known: "One historian's account; matches his 1844 and 1861 letters."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: TODO}
  form_acquired: {value: TODO}
  circle_present: {value: TODO}
  reading: "Not assessed. The v7.1 two-lane paper uses Faraday as the case where the no-exemption form is present without the pantheist metaphysics (Lane B, B3 and V7.1-N B5). This record collects the facts that claim would be tested on; it does not test it."
  notes: ""

institutions:
  - {value: "Royal Institution of Great Britain", role: "Laboratory Assistant (1813, 1815–1826); Director of the Laboratory (1825–1867); Fullerian Professor of Chemistry (1833–1867); Superintendent of the House (1852–1867)", years: "1813–1867", kind: employer, certainty: 1.0, cites: [{source: S2, locator: "Ri positions"}], how_known: "The institution's own record."}
  - {value: "Royal Military Academy, Woolwich", role: "Professor of Chemistry", years: "1830–1851", kind: employer, certainty: 1.0, cites: [{source: S2, locator: "Biography"}], how_known: "Institution's record."}
  - {value: "The Admiralty", role: "Scientific Adviser", years: "from 1829", kind: "government or state body", certainty: 1.0, cites: [{source: S2, locator: "Biography"}], how_known: "Institution's record."}
  - {value: "Trinity House (lighthouse authority)", role: "Scientific Adviser", years: "1836–1865", kind: "government or state body", certainty: 1.0, cites: [{source: S2, locator: "Biography"}, {source: S5, locator: "p. 3"}], how_known: "Two sources agree."}
  - {value: "Sandemanian church, London (Paul's Alley meeting house)", role: "member, deacon, elder", years: "1821–1867, with an exclusion in 1844", kind: "religious body", certainty: 0.7, cites: [{source: S5, locator: "pp. 1–2, 4"}], how_known: "One historian's account."}
  - {value: "The Crown (Queen Victoria): Civil List pension (1836) and a Grace and Favour house at Hampton Court (1858)", kind: "patron or funder", years: "1836–1867", certainty: 1.0, cites: [{source: S2, locator: "Biography"}], how_known: "Institution's record."}

collaborators:
  - {value: "Humphry Davy", roster_id: davy-humphry, relation: "mentor or employer", years: "1812–1820", certainty: 1.0, cites: [{source: S1, locator: "Early life"}], how_known: "Encyclopedia; S1 calls 1812–1820 his 'second apprenticeship, under Davy'."}
  - {value: "Charles Wheatstone", relation: collaborator, years: "1831", note: "worked together on the theory of sound", certainty: 0.7, cites: [{source: S1, locator: "Early life"}], how_known: "One source."}
  - {value: "William Thomson (later Lord Kelvin)", roster_id: thomson-william-kelvin, relation: correspondent, years: "1845", note: "suggested the magnetic-field experiment that led to the magneto-optical effect", certainty: 0.7, cites: [{source: S1, locator: "Later life"}], how_known: "One source."}
  - {value: "James Clerk Maxwell", roster_id: maxwell-james-clerk, relation: influenced, certainty: 1.0, cites: [{source: S1, locator: "opening paragraph; Later life"}], how_known: "Encyclopedia."}
  - {value: "John Tyndall", relation: other, note: "Royal Institution colleague and contemporary biographer", certainty: 0.7, cites: [{source: S5, locator: "pp. 2, 4"}], how_known: "One source."}
  - {value: "Ada Lovelace", roster_id: lovelace-ada, relation: correspondent, years: "1844", certainty: 1.0, cites: [{source: S3, locator: "whole letter"}], how_known: "Primary letter."}
  - {value: "Auguste De La Rive", relation: correspondent, years: "to 1861", certainty: 1.0, cites: [{source: S4, locator: "whole letter"}], how_known: "Primary letter."}

review:
  roster_status_reason: {value: "Core in v7.1 (no v7 review note) and carried into v8 unchanged; F rose from 4 to 5 when the Claude list was counted.", certainty: 1.0, cites: [{source: S7, locator: "roster.csv, rank 58"}], how_known: "Study roster."}
  controversies:
    - {value: "Whether he was ever offered a knighthood", certainty: 0.5, cites: [{source: S1, locator: "Later life"}, {source: S2, locator: "Biography"}, {source: S5, locator: "p. 4"}], how_known: "S1 and S5 say he declined one; S2 (summarising the Oxford DNB) says he said publicly he would not accept one but no evidence has been found that one was offered."}
  data_quality_flags:
    - "Start at the Royal Institution: S1 says he 'joined Davy in 1812'; S2 and S5 give 1813. 1813 is used (two sources)."
    - "Birth date: S5's gravestone transcription gives 21 September 1791; S1 and Faraday's own letter (S4) give 22 September."
    - "A second term as elder (often given as 1860–1864) is reported elsewhere but not confirmed in the sources consulted."
  open_questions:
    - "Primary code: CHRIST, CLTHEI, or something else? Needs a reviewed coding pass (docs/CODING_GUIDE.md)."
    - "Does the v7.1 'mid-basin theist' label hold once his written views on providence, prayer and miracle are checked?"
    - "Early reading (Watts, The Improvement of the Mind; Marcet, Conversations on Chemistry) is widely reported; confirm in Cantor 1991 or James 2010."
    - "Read Cantor 1989 (S6) for why he was excluded in 1844 and when he was readmitted."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "L. Pearce Williams"
    citation: "Williams, L. Pearce. \"Michael Faraday.\" Encyclopaedia Britannica. Last updated September 18, 2026. https://www.britannica.com/biography/Michael-Faraday (article pages: main page with Early life; Theory of electrochemistry; Later life)."
    url: "https://www.britannica.com/biography/Michael-Faraday"
    accessed: 2026-10-01
    reliability_note: "Signed article by a Faraday biographer (author of Michael Faraday, 1965), fact-checked by Britannica editors."
    used_for: [identity, basics, contribution, childhood, collaborators, review]
  - id: S2
    type: tertiary
    kind: "institutional page"
    author: "Royal Institution of Great Britain"
    citation: "Royal Institution of Great Britain. \"Michael Faraday (1791-1867).\" Explore biographies. https://www.rigb.org/explore-science/explore/person/michael-faraday-1791-1867."
    url: "https://www.rigb.org/explore-science/explore/person/michael-faraday-1791-1867"
    accessed: 2026-10-01
    reliability_note: "Faraday's own institution, which holds his papers. The page names the Oxford Dictionary of National Biography as its source."
    used_for: [basics, contribution, childhood, institutions, review]
  - id: S3
    type: primary
    kind: letter
    author: "Michael Faraday"
    year: 1844
    citation: "Faraday, Michael. Letter to Augusta Ada Lovelace, 24 October 1844. Record Faraday1631 in Ɛpsilon: The Michael Faraday Collection. https://epsilon.ac.uk/view/faraday/letters/Faraday1631. Source of text: Bodleian Library, MS dep Lovelace-Byron 171, ff. 44–5, and Faraday's copy, IEE MS SC 3. Also published in The Correspondence of Michael Faraday, vol. 3 (1996)."
    url: "https://epsilon.ac.uk/view/faraday/letters/Faraday1631"
    accessed: 2026-10-01
    reliability_note: "Scholarly transcription from the edited correspondence (Faraday Project). Note 4 of the edition says the closing part of the letter, which holds the religion passage, is taken from Faraday's copy."
    used_for: [worldview, collaborators]
  - id: S4
    type: primary
    kind: letter
    author: "Michael Faraday"
    year: 1861
    citation: "Faraday, Michael. Letter to Arthur-Auguste De La Rive, 19 September 1861. Record Faraday4061 in Ɛpsilon: The Michael Faraday Collection. https://epsilon.ac.uk/view/faraday/letters/Faraday4061. Source of text: BPUG MS 2361, ff. 93–4. Also published in The Correspondence of Michael Faraday, vol. 6 (2011)."
    url: "https://epsilon.ac.uk/view/faraday/letters/Faraday4061"
    accessed: 2026-10-01
    reliability_note: "Scholarly transcription from the edited correspondence."
    used_for: [basics, worldview, collaborators]
  - id: S5
    type: secondary
    kind: "journal article"
    author: "Colin Russell"
    year: 2007
    citation: "Russell, Colin. \"Science and Faith in the Life of Michael Faraday.\" The Faraday Papers, no. 13. Cambridge: The Faraday Institute for Science and Religion, April 2007. 4 pp. https://www.faraday.cam.ac.uk/wp-content/uploads/resources/Faraday%20Papers/Faraday%20Paper%2013%20Russell_EN.pdf."
    url: "https://www.faraday.cam.ac.uk/wp-content/uploads/resources/Faraday%20Papers/Faraday%20Paper%2013%20Russell_EN.pdf"
    accessed: 2026-10-01
    reliability_note: "Short paper by a historian of science (Emeritus Professor, Open University; author of Michael Faraday: Physics and Faith, 2000), drawing on Cantor 1991. Published by a science-and-religion institute; the author argues a 'convergent' reading, so treat interpretation as his."
    used_for: [basics, childhood, worldview, heritage, timing, institutions, collaborators]
  - id: S6
    type: secondary
    kind: "journal article"
    author: "Geoffrey Cantor"
    year: 1989
    citation: "Cantor, Geoffrey. \"Why Was Faraday Excluded from the Sandemanians in 1844?\" The British Journal for the History of Science 22, no. 4 (1989): 433–37. https://doi.org/10.1017/S0007087400026388."
    url: "https://doi.org/10.1017/S0007087400026388"
    accessed: 2026-10-01
    reliability_note: "Peer-reviewed. Only the title and bibliographic record were consulted (paywalled); used only for the fact of the 1844 exclusion."
    used_for: [worldview]
  - id: S7
    type: tertiary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. v8 roster, data/roster/roster.csv, built by scripts/rebuild_roster.py from the five model lists."
    used_for: [review]
---

# Michael Faraday

> Status: example — unreviewed. This file shows the record structure. Only fields with good public sources are filled; everything else is TODO. No worldview code or LIO score has been entered.

## Summary

Michael Faraday (1791–1867) was an English chemist and physicist who spent his working life at the Royal Institution in London [S1; S2]. His lasting work includes the electromagnetic rotation behind the electric motor (1821), electromagnetic induction (1831), the laws of electrolysis, the magneto-optical effect and diamagnetism (1845), and a field conception of force that Maxwell later put into equations [S1, Early life, Later life; S2]. He had almost no formal schooling [S1, Early life]. He was a lifelong Sandemanian, a small Christian sect, and served it as deacon and elder [S5, p. 2]. In a private letter he described his religion and his natural philosophy as "two distinct things" [S3].

## Life and work

Born at Newington Butts, Surrey, the son of a blacksmith who had moved to London from the north of England [S1, Early life; S2]. He was apprenticed to the bookbinder George Riebau from 1805 to 1812 and taught himself from the books that passed through the shop [S2; S1, Early life]. After attending Humphry Davy's lectures he sent Davy his bound notes, and in 1813 he became Davy's assistant at the Royal Institution [S1, Early life; S2; S5, p. 1]. Britannica dates his joining Davy to 1812 [S1, Early life]. That conflict is logged under review.

At the Royal Institution he became Director of the Laboratory (1825), Fullerian Professor of Chemistry (1833) and Superintendent of the House [S2]. He also advised the Admiralty and Trinity House and taught chemistry at Woolwich [S2]. His health broke down in 1839, and he did little creative science until 1845 [S1, Theory of electrochemistry]. From about 1855 his memory and powers declined [S1, Later life]. In 1858 the Queen gave him the use of a house at Hampton Court, where he died on 25 August 1867. He was buried at Highgate [S1, Later life; S2; S5, p. 4].

## Contribution and impact

- 1821: electromagnetic rotation, the first electric motor [S1, Early life; S2].
- 1825: isolated benzene [S1, Early life; S2].
- 1831: electromagnetic induction, then the first dynamo [S1, Early life].
- 1830s: the two laws of electrochemistry, and the terms electrode, cathode and ion [S1, Theory of electrochemistry; S2].
- 1845: rotation of polarized light by magnetism, and diamagnetism [S1, Later life; S2].
- By 1850: space as a medium carrying electric and magnetic strain, which became field theory. Maxwell acknowledged that the basic ideas of his field equations were Faraday's [S1, Later life].

He founded the Friday Evening Discourses and the Christmas Lectures [S2]. His name is on the Faraday effect, Faraday's law of induction and Faraday's laws of electrolysis [S1, Quick Facts].

## Childhood and education

The household was poor. His father was often ill, and the four children went hungry [S1, Early life]. The family was Sandemanian [S1, Early life; S2], a dissenting tradition that went back at least to his grandfather [S5, p. 1]. As a child he went to the Sandemanian chapel in Paul's Alley [S5, p. 1]. His schooling was reading, writing and ciphering at a church Sunday school [S1, Early life]. No consulted source mentions geometry or algebra in childhood, so early mathematics is entered as "arithmetic only" at certainty 0.7. Whether he had any early practice in definition-to-consequence reasoning is still TODO.

From age 14 he was apprenticed to a bookbinder. He read what came in for binding, including the electricity article in the third edition of the Encyclopaedia Britannica, and built a simple electrostatic machine and a voltaic pile [S1, Early life].

## Adult working worldview

He joined the Sandemanian church by confession of faith in 1821, within days of his marriage to Sarah Barnard. He became a deacon in 1832 and an elder in 1840 [S5, p. 2]. He was excluded in 1844 [S6], and he resigned his eldership in 1864 [S5, p. 4].

In his own words to Ada Lovelace in 1844: "There is no philosophy in my religion", the works of God "can never by any possibility come in contradiction" with the things of faith, and "that which is religious & that which is philosophical have ever been two distinct things" [S3]. In 1861 he wrote to De La Rive of the "good hope" that made death "a comfort - not a fear" [S4]. Russell argues that despite that separation, his faith shaped his sense of vocation and his search for a unity of forces, and that a private memorandum on atoms and fields invokes God [S5, pp. 2–3]. Whether that counts as a lawful-order worldview, and which system code applies, has not been coded here.

## Heritage (context only)

English, from a Sandemanian family with a long history of dissent from the Church of England [S1; S5, p. 1]. Heritage is recorded for context only. It is not a worldview code.

## Timing

His first lasting contribution came in 1821, at about age 29 [S1, Early life]. That same year he joined the Sandemanian church [S5, p. 2]. Throughout his major work (1821 to about 1855) he was a practising Sandemanian [S5, p. 2; S1, Later life]. When LIO-type views appear relative to the major work is TODO until his worldview is coded.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. The v7.1 papers use Faraday as the test case of the form without the metaphysics: a devout physicist whose working method leaves no reserved clause. This record does not assess that claim yet. The fields `geometric_form_present`, `form_acquired` and `circle_present` are TODO.

## Open questions

- Primary code: CHRIST, CLTHEI, or something else? (See `candidate_codes_considered`.)
- Does the "mid-basin theist" starting label survive a reading of his views on providence, prayer and miracle?
- Was a knighthood ever offered? Sources disagree [S1, Later life; S2; S5, p. 4].
- Confirm his early reading (Watts, Marcet) in a full biography.

## Research log

- 2026-10-01: Read Britannica (S1: main, Theory of electrochemistry, Later life), the Royal Institution biography (S2), two letters in Epsilon (S3, S4), Russell's Faraday Paper 13 (S5), and the bibliographic record of Cantor 1989 (S6). Did not use Wikipedia as a citation. Its leads (Watts, Marcet, second eldership, FRS 1824, farad unit) are recorded as TODO or open questions. No worldview code, axis score or mid-basin value entered.
