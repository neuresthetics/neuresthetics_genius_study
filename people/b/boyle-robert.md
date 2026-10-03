---
record:
  record_type: person
  schema_version: "1.2"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, fourth batch: physical science 1600–1950)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-02
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (fourth batch, RUNBOOK §1 order). Basics from Britannica (Principe) and the Stanford Encyclopedia of Philosophy (MacIntosh and Anstey). Worldview from his own A Free Enquiry into the Vulgarly Receiv'd Notion of Nature (1686) and The Christian Virtuoso (1690), read in the Text Creation Partnership transcriptions of the EEBO page images. primary_system CHRIST at 0.7 (CLTHEI named alternative; CLASS_THEISM rejected). A 0, B 3, C 0, D 2, E 3, all at 0.7; mid_basin true (0.7). Not reviewed."}

identity:
  id: boyle-robert
  display_name: "Robert Boyle"
  roster:
    canonical_name: "Robert Boyle"
    rank: 214
    F: 3
    models: [Claude, DeepSeek, Grok]
    band: "core (3–4)"
    status: core
    field: chemistry
    field_bucket: chemistry
  full_name: {value: "Robert Boyle", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "§1 Life"}], how_known: "Two sources."}
  native_name: {value: "Robert Boyle (English)", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "English name."}
  aliases: []

basics:
  birth:
    date: {value: "1627-01-25", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica; England and Ireland used the Julian calendar in 1627, and Britannica does not say which style it gives."}
    place: {value: "Lismore Castle, County Waterford", modern_name: "Lismore, County Waterford, Ireland", polity_then: "Kingdom of Ireland", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "§1 Life"}], how_known: "Two sources."}
  death:
    date: {value: "1691-12-31", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica; calendar style as for the birth date."}
    place: {value: "London", modern_name: "London, England, UK", polity_then: "Kingdom of England", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1660, certainty: 1.0, cites: [{source: S1, locator: "'Scientific career', paragraph 1"}], how_known: "New Experiments Physico-Mechanicall, Touching the Spring of the Air (1660), the air-pump work with Hooke."}
  era_bucket: {value: "1600 to 1749", certainty: 1.0, cites: [{source: S1, locator: "'Scientific career', paragraph 1"}], how_known: "From first_lasting_contribution_year (P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "Ireland is Northern Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 1.0, cites: [{source: S1, locator: "'Scientific career'; 'Mature years in London'"}], how_known: "Oxford and London."}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "As the sources record it."}
  languages_of_work: {value: [English, Latin], certainty: 0.7, cites: [{source: S3, locator: "title page"}, {source: S2, locator: "§1 Life"}], how_known: "His books were written in English (S3, S4); Latin editions and his French (S2) noted; Latin as a working language is the coder's reading of the period, not checked title by title."}
  occupations: {value: ["natural philosopher", "chemist", "theological writer"], certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "§1 Life"}], how_known: "Two sources."}

contribution:
  fields: {value: ["chemistry", "pneumatics", "experimental philosophy", "natural theology"], certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "opening"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Air-pump experiments with Robert Hooke on air pressure and the vacuum (air's role in combustion, respiration and sound)", year: "1659–1660", kind: discovery, lasting: "founding work of experimental pneumatics", certainty: 1.0, cites: [{source: S1, locator: "'Scientific career', paragraph 1"}], how_known: "Britannica."}
    - {value: "Boyle's law: pressure and volume of a gas vary inversely", year: "1662", kind: "law or principle", lasting: "standard physics and chemistry", certainty: 1.0, cites: [{source: S1, locator: "'Scientific career', paragraph 1"}], how_known: "Britannica."}
    - {value: "The Sceptical Chymist: critique of Aristotelian and Paracelsian elements and of chemical analysis; corpuscular chemistry", year: "1661", kind: work, lasting: "earned him the name 'father of chemistry'", certainty: 1.0, cites: [{source: S1, locator: "'Scientific career', paragraph 2"}], how_known: "Britannica."}
  evidence_of_impact:
    - {value: "Called 'the leading natural philosopher in England before Newton' and 'the father of experimental philosophy'", kind: "scholarly consensus", certainty: 1.0, cites: [{source: S2, locator: "§1 Life and opening"}, {source: S1, locator: "'Scientific career', paragraph 2 ('father of chemistry')"}], how_known: "Two sources."}
  major_works:
    - {value: "New Experiments Physico-Mechanicall, Touching the Spring of the Air and Its Effects", year: 1660, kind: book, certainty: 1.0, cites: [{source: S1, locator: "'Scientific career', paragraph 1"}], how_known: "Britannica."}
    - {value: "The Sceptical Chymist", year: 1661, kind: book, certainty: 1.0, cites: [{source: S1, locator: "'Scientific career', paragraph 2"}], how_known: "Britannica."}
    - {value: "The Origine of Formes and Qualities", year: 1666, kind: book, certainty: 1.0, cites: [{source: S1, locator: "'Scientific career', paragraph 2"}], how_known: "Britannica."}
    - {value: "A Free Enquiry into the Vulgarly Receiv'd Notion of Nature", year: 1686, kind: book, certainty: 1.0, cites: [{source: S3, locator: "title page"}], how_known: "The book itself."}
    - {value: "The Christian Virtuoso", year: 1690, kind: book, certainty: 1.0, cites: [{source: S4, locator: "title page"}, {source: S1, locator: "'Theological activities'"}], how_known: "Two sources."}
  honours:
    - {value: "Founding member of the Royal Society of London", year: 1660, certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "Britannica ('In 1660 he helped found the Royal Society')."}
  definition_fit: {value: "clearly meets", rationale: "Founder of experimental pneumatics and of modern chemistry's corpuscular programme; Boyle's law.", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: TODO, note: "The family's Protestant (Church of Ireland) practice is not stated in the sources read."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father, Richard Boyle, 1st Earl of Cork", name: "Richard Boyle", role: father, certainty: 1.0, cites: [{source: S1, locator: "'Early life and education'"}, {source: S2, locator: "§1 Life"}], how_known: "Two sources."}
    - {value: "Mother, Catherine Fenton, daughter of Sir Geoffrey Fenton, secretary of state for Ireland", name: "Catherine Boyle (née Fenton)", role: mother, certainty: 1.0, cites: [{source: S1, locator: "'Early life and education'"}, {source: S2, locator: "§1 Life"}], how_known: "Two sources."}
  household_circumstances: {value: "One of the wealthiest families in Britain; he was the 14th child and 7th son (SEP: second youngest of fifteen)", certainty: 1.0, cites: [{source: S1, locator: "'Early life and education'"}, {source: S2, locator: "§1 Life"}], how_known: "Two sources."}
  schooling:
    - {value: "Eton College, from age eight", stage: "grammar or secondary school", years: "1635–1638", certainty: 0.7, cites: [{source: S1, locator: "'Early life and education'"}], how_known: "Britannica gives 'at age eight'; end year is the coder's reading (grand tour from 1639)."}
    - {value: "Grand tour with his brother Francis and tutor Isaac Marcombes; studies in Geneva; in Florence when Galileo died", stage: tutor, years: "1639–1644", certainty: 1.0, cites: [{source: S1, locator: "'Early life and education'"}, {source: S2, locator: "§1 Life"}], how_known: "Two sources."}
  early_mathematics: {value: TODO, note: "Not stated in the sources read."}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "Isaac Marcombes, tutor on the grand tour and in Geneva", certainty: 1.0, cites: [{source: S1, locator: "'Early life and education'"}], how_known: "Britannica."}
  languages_in_childhood: {value: [English, French], certainty: 0.7, cites: [{source: S2, locator: "§1 Life ('mastered the French language')"}], how_known: "SEP; French learned in Geneva in his teens."}
  notable_events:
    - {value: "Christian conversion experience in Geneva during the grand tour", year: "1639–1644", certainty: 1.0, cites: [{source: S2, locator: "§1 Life"}], how_known: "SEP; year range from the Geneva stay (S1)."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1644–1691", certainty: 1.0, cites: [{source: S1, locator: "'Early life and education' to 'Mature years in London'"}], how_known: "Return to England and Stalbridge to death."}
  nominal_affiliations:
    - {value: "Church of England ('a devout and pious Anglican')", years: "–1691", role: "member", certainty: 1.0, cites: [{source: S1, locator: "'Theological activities'"}, {source: S2, locator: "§1 Life ('Christian Virtuoso because of his piety')"}], how_known: "Two sources; he declined a bishopric (S1)."}
  self_described_science_religion_relation:
    value: "Mutually supporting: studying nature as God's handiwork is a religious duty; nature is matter moved by laws God established and upholds by his 'ordinary and general concourse'; God's providence over bodies can be 'a Bridge' from natural to revealed religion."
    certainty: 1.0
    cites: [{source: S3, locator: "pp. 8, 10–11"}, {source: S4, locator: "p. 42"}, {source: S1, locator: "'Theological activities'"}]
    how_known: "His own published books in a scholarly transcription, agreeing with Britannica's summary."
  primary_system:
    value: CHRIST
    basis: written_profession
    certainty: 0.7
    cites: [{source: S3, locator: "pp. 15–16, 157–160"}, {source: S4, locator: "pp. 41–42, 117–118"}, {source: S1, locator: "'Theological activities'"}]
    how_known: "His own published books: Christ's and the apostles' miracles 'pleaded by Christians on the behalf of their Religion' (S3, pp. 15–16), revealed religion with its explicit law, penalties and rewards (S4, pp. 41–42), and a Divine testimony to be 'Believ'd, in what it clearly Teaches' (S4, p. 118)."
    rationale: "CHRIST: a Christian apologist writing as a Christian (the Christian Virtuoso), with revealed religion, scripture and miracles affirmed. Named alternative: CLTHEI, since his God is a free personal Lord who can 'recede' from the laws of nature in miracles and who intervenes 'divers times (and perhaps oftner than mere Philosophers imagine)' (S3, pp. 160, 239–240). CLASS_THEISM rejected: he attacks the Aristotelian and scholastic 'Nature' (S3) and makes the laws God's free gift 'to Matter, not to Himself' (S3, p. 158), which is voluntarist, not Thomist. Capped at 0.7 for the CLTHEI alternative."
  secondary_system: {value: UNKNOWN, how_known: "No second system: his natural philosophy is written inside his Christian theology."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Coded at 0.7: revealed Christianity, miracles of Christ and the apostles, revealed law with rewards and penalties.", cites: [{source: S3, locator: "pp. 15–16"}, {source: S4, locator: "pp. 41–42, 117–118"}]}
    - {code: CLTHEI, reason: "Named alternative, not coded: a free personal God who works miracles and providential interpositions where men are 'nearly and highly concern'd'. Not coded because his books argue for revealed Christianity specifically, not a generic interventionist God.", cites: [{source: S3, locator: "pp. 157–160, 239–240"}]}
    - {code: CLASS_THEISM, reason: "Rejected: he rejects the scholastic notion of Nature and grounds laws in God's free will (voluntarism), not in Aristotelian-Thomist natures.", cites: [{source: S3, locator: "pp. 8, 158"}, {source: S2, locator: "§3.4.1"}]}
    - {code: DEISM, reason: "Rejected: he affirms revelation and miracles.", cites: [{source: S3, locator: "pp. 157, 160"}]}
  lio_axes:
    A_locus:
      value: 0
      basis: written_profession
      certainty: 0.7
      cites: [{source: S3, locator: "p. 158"}]
      how_known: "His own book; a named alternative, so 0.7."
      rationale: "Transcendent person outside the world: God is 'the Supream and Absolute Lord, and, if I may so speak, the Proprietor of the whole Creation', who 'established the Laws of Motion' and 'gave them to Matter, not to Himself' (p. 158); the world is his artefact, not his body. Named alternative: 1, since God continues his 'ordinary and general concourse' in the world (p. 10)."
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.7
      cites: [{source: S3, locator: "pp. 8, 10–11, 160, 239–240"}, {source: S1, locator: "'Scientific career', paragraph 2"}]
      how_known: "His own book; a named alternative, so 0.7."
      rationale: "Scored on his account of nature (P6). Law and regularity with a stated, limited exception. Brute matter 'managed by certain Laws of Local Motion, and upheld by his ordinary and general concourse' does what was designed (p. 8); the world was so contrived that 'there will be no necessity of extraordinary interpositions' (p. 10); his working science is mechanical and experimental (S1). The exception is stated: God 'sometimes (as in Divine Miracles)' recedes 'from what Men call the Laws of Nature' (p. 160). Named alternative: 2, since he also says God acts by miracles and, 'perhaps oftner than mere Philosophers imagine', through rational minds 'where Men [...] are nearly and highly concern'd' (pp. 239–240)."
    C_ledger:
      value: 0
      basis: written_profession
      certainty: 0.7
      cites: [{source: S4, locator: "pp. 41–42"}]
      how_known: "His own book, but the passage states the content of revealed law rather than arguing it, so 0.7 (indirect)."
      rationale: "Reward and punishment of persons: God has given man 'an explicite and poſitive Law, enforc'd by Threatning ſevere Penalties to the Stubborn Tranſgreſſors; and Promiſing, to the ſincere Obeyers, Rewards' (pp. 41–42)."
    D_authority:
      value: 2
      basis: written_profession
      certainty: 0.7
      cites: [{source: S4, locator: "pp. 117–118"}, {source: S2, locator: "§4.8"}]
      how_known: "His own book; a named alternative, so 0.7."
      rationale: "Mixed. Reason keeps the judging role: the understanding is to 'Examine, whether the Teſtimony be indeed Divine', and reason takes help 'from Experience, whether Natural, or Supernatural' (p. 118); in nature, experiment rules (S1). But once a testimony is judged divine it 'ought to be [...] Believ'd, in what it clearly Teaches' (p. 118), including truths above reason such as the resurrection (S2, §4.8). Two domains, each with its own authority, so D 2 (same-pattern rule). Named alternative: 1, if the duty to believe a divine testimony above reason is read as revelation outranking observation."
    E_scope:
      value: 3
      basis: written_profession
      certainty: 0.7
      cites: [{source: S3, locator: "pp. 15–16, 160, 239–240"}]
      how_known: "His own book; a named alternative, so 0.7."
      rationale: "Scored on the world's order (P7). The same mechanical laws govern all bodies (pp. 8, 10–11), with a stated exception for people: miracles 'in reference to Man, the Noblest Visible Object of His Providence' (p. 160) and miracles 'pleaded by Christians on the behalf of their Religion' (pp. 15–16). Named alternative: 2, given the further providential interventions 'where Men [...] are nearly and highly concern'd' (pp. 239–240). The revealed law's rewards and penalties are scored on C."
  mid_basin:
    value: true
    certainty: 0.7
    cites: [{source: S3, locator: "pp. 8, 10–11, 158, 160"}]
    how_known: "P4 test: A_locus = 0 (≤ 1) at 0.7 and B_cause = 3 (≥ 3) at 0.7, B scored on his account of nature (P6). Both at certainty ≥ 0.7, so true. Certainty 0.7: no surer than the less certain of A and B (CODING_GUIDE §3). F = 3, so first-rank is met. If B's named alternative (2) were taken, the test would have no branch (TODO)."
  statements:
    - text: "if He but continue his ordinary and general concourse, there will be no necessity of extraordinary interpositions"
      cites: [{source: S3, locator: "p. 10"}]
      date: "1686"
      context: "Free Enquiry, Section II: the wisdom of God in the first fabric of the universe, against the scholastic idea of Nature as an intelligent overseer."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "who is not only a self-existent and Independent Being, but the Supream and Absolute Lord, and, if I may so speak, the Proprietor of the whole Creation"
      cites: [{source: S3, locator: "p. 158"}]
      date: "1686"
      context: "Free Enquiry, on why God was not bound to make or govern bodies 'after the best manner'."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "And Who, when He made the World, and established the Laws of Motion, gave them to Matter, not to Himself."
      cites: [{source: S3, locator: "p. 158"}]
      date: "1686"
      context: "Same passage."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "in sometimes (as in Divine Miracles) receding from what Men call the Laws of Nature, as He did at first in establishing them"
      cites: [{source: S3, locator: "p. 160"}]
      date: "1686"
      context: "Free Enquiry: God may show as much wisdom and providence 'in reference to Man, the Noblest Visible Object of His Providence' in miracles as in setting the laws."
      axes: [B_cause, E_scope]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "an explicite and poſitive Law, enforc'd by Threatning ſevere Penalties to the Stubborn Tranſgreſſors; and Promiſing, to the ſincere Obeyers, Rewards ſuitable to his own Greatneſs and Goodneſs"
      cites: [{source: S4, locator: "p. 42"}]
      date: "1690"
      context: "Christian Virtuoso: what God has 'vouchſafed to Man' beyond natural religion; the passage continues that providence in bodies may be 'a Bridge' to revealed religion."
      axes: [C_ledger]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "For here alſo the Underſtanding is to Examine, whether the Teſtimony be indeed Divine; and, whether a Divine Teſtimony ought to be (as It will eaſily perceive it ſhould) Believ'd, in what it clearly Teaches"
      cites: [{source: S4, locator: "pp. 117–118"}]
      date: "1690"
      context: "Christian Virtuoso: the use of reason applied to supernatural revelation."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
  changes_over_life:
    - {value: "Christian conversion experience in Geneva in his teens; devotional writing first, then mature works on reason, nature and revelation", year: "1639–1690", certainty: 1.0, cites: [{source: S2, locator: "§1 Life"}, {source: S1, locator: "'Theological activities'"}], how_known: "Two sources."}
  coder_notes: "S3 and S4 are read in the Text Creation Partnership's keyboarded transcriptions of the EEBO page images (released CC0 on the TCP GitHub). The TCP is a library partnership (Michigan, Oxford and others) transcribing a library scan, so it is treated as a primary transcription, not an unofficial web copy; the long s (ſ) and spelling of S4 are kept as transcribed. Page numbers are the printed page numbers that TCP records. Every axis names an alternative score, so all are at 0.7 even though the basis would allow 1.0. CLTHEI and CLASS_THEISM are draft system files; CHRIST is a draft."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Anglo-Irish aristocracy", certainty: 1.0, cites: [{source: S1, locator: "opening; 'Early life and education'"}, {source: S2, locator: "§1 Life"}], how_known: "Two sources."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1659–1668", certainty: 1.0, cites: [{source: S1, locator: "'Scientific career' ('Much of Boyle's best-known work dates from this period')"}], how_known: "The Oxford years."}
  age_at_first_lasting_contribution: {value: 33, certainty: 0.7, cites: [{source: S1, locator: "opening; 'Scientific career', paragraph 1"}], how_known: "Born January 1627; Spring of the Air published 1660 (month not given)."}
  first_evidence_of_lio_type_views: {value: "Free Enquiry: laws of motion upheld by God's ordinary concourse", year: 1686, certainty: 1.0, cites: [{source: S3, locator: "pp. 8, 10"}], how_known: "Earliest dated statement read; his earlier theological writings were not read."}
  lio_views_relative_to_major_work: {value: "unclear", rationale: "The texts read (1686, 1690) are after the Oxford work; when they were drafted was not checked.", certainty: 0.5, cites: [{source: S3, locator: "title page (1685/6)"}, {source: S4, locator: "title page (1690)"}], how_known: "Dates of the texts read."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "His method relies on experiment and observation and is reluctant to formulate general theories (S1).", certainty: 0.7, cites: [{source: S1, locator: "'Scientific career', paragraph 2"}], how_known: "Britannica."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "'Early life and education'"}], how_known: "Nothing on method in his schooling."}
  circle_present: {value: "no", rationale: "God is the Lord and Proprietor of a creation distinct from him; the laws were given 'to Matter, not to Himself' (S3, p. 158).", certainty: 0.7, cites: [{source: S3, locator: "p. 158"}], how_known: "His own words."}
  reading: "As belief, not finding: form absent (experimental method); circle absent (creator distinct from creation). The record does not test H1."
  notes: ""

institutions:
  - {value: "Hartlib Circle", role: "member and correspondent", years: "1647–c.1655", kind: other, certainty: 1.0, cites: [{source: S1, locator: "'Early life and education'"}], how_known: "Britannica."}
  - {value: "University of Oxford (Experimental Philosophy Club)", role: "resident natural philosopher; the club met at times in his lodgings", years: "c.1656–1668", kind: university, certainty: 1.0, cites: [{source: S1, locator: "'Scientific career', paragraph 1"}], how_known: "Britannica."}
  - {value: "Royal Society of London", role: "founding member; declined the presidency (1680)", years: "1660–1691", kind: "academy or learned society", certainty: 1.0, cites: [{source: S1, locator: "opening; 'Mature years in London'"}], how_known: "Britannica."}
collaborators:
  - {value: "Robert Hooke", roster_id: hooke-robert, relation: "student or assistant", note: "built the air pump with him (1659); later curator of experiments of the Royal Society", certainty: 1.0, cites: [{source: S1, locator: "'Scientific career', paragraph 1"}], how_known: "Britannica."}
  - {value: "George Starkey", relation: collaborator, note: "chemist of the Hartlib Circle who heightened his interest in experimental chemistry", certainty: 1.0, cites: [{source: S1, locator: "'Early life and education'"}], how_known: "Britannica."}
  - {value: "John Locke", roster_id: locke-john, relation: collaborator, note: "fellow member of the Oxford group", certainty: 0.7, cites: [{source: S1, locator: "'Scientific career', paragraph 1"}], how_known: "Britannica names Locke among the Oxford natural philosophers he was associated with."}
  - {value: "Katherine Jones, Viscountess Ranelagh", relation: family, note: "his sister; he lived and worked in her London house from 1668", certainty: 1.0, cites: [{source: S1, locator: "'Mature years in London'"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3: Claude, DeepSeek, Grok).", certainty: 0.7, cites: [{source: S5, locator: "roster.csv, rank 214"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Birth and death dates as printed by Britannica, which does not say whether they are Old Style; Old Style is assumed in the calendar field."
    - "S3 and S4 read in TCP transcriptions, not in the page images; gaps marked 〈gap〉 by TCP (Hebrew in S3, p. 158) are not quoted."
  open_questions:
    - "Read the Hunter and Davis Works of Robert Boyle (BW) text of the Free Enquiry and Christian Virtuoso for the modern edition's pages."
    - "Read Boyle's Account of Philaretus (autobiography) for the Geneva conversion in his own words."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Lawrence M. Principe"
    citation: "Principe, Lawrence M. \"Robert Boyle.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Robert-Boyle."
    url: "https://www.britannica.com/biography/Robert-Boyle"
    accessed: 2026-10-02
    reliability_note: "Signed article by a leading Boyle scholar (one page). Sections cited by heading."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: secondary
    kind: encyclopedia
    author: "J. J. MacIntosh and Peter Anstey"
    citation: "MacIntosh, J. J., and Peter Anstey. \"Robert Boyle.\" The Stanford Encyclopedia of Philosophy (first published 2002; substantive revision 2025). https://plato.stanford.edu/entries/boyle/."
    url: "https://plato.stanford.edu/entries/boyle/"
    accessed: 2026-10-02
    reliability_note: "Peer-reviewed reference article. Cited by section number."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "Robert Boyle"
    year: 1686
    citation: "Boyle, Robert. A Free Enquiry into the Vulgarly Receiv'd Notion of Nature. London: printed by H. Clark for John Taylor, 1685/6 [i.e. 1686]; published as 'by R.B., Fellow of the Royal Society'. Text Creation Partnership transcription of the EEBO page images, TCP A28982, https://raw.githubusercontent.com/textcreationpartnership/A28982/master/A28982.xml."
    url: "https://github.com/textcreationpartnership/A28982"
    accessed: 2026-10-02
    reliability_note: "His own book in the TCP keyboarded transcription (CC0). Page numbers are the printed numbers recorded by TCP."
    used_for: [basics, contribution, worldview, timing, lane_b]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "Robert Boyle"
    year: 1690
    citation: "Boyle, Robert. The Christian Virtuoso. London: printed by Edw. Jones for John Taylor, 1690; published as 'by T.H.R.B., Fellow of the Royal Society'. Text Creation Partnership transcription of the EEBO page images, TCP A28945, https://raw.githubusercontent.com/textcreationpartnership/A28945/master/A28945.xml."
    url: "https://github.com/textcreationpartnership/A28945"
    accessed: 2026-10-02
    reliability_note: "His own book in the TCP keyboarded transcription (CC0), with long s as printed. Page numbers are the printed numbers recorded by TCP."
    used_for: [contribution, worldview]
  - id: S5
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
---

# Robert Boyle

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Robert Boyle (1627–1691), Anglo-Irish natural philosopher, built the air pump with Hooke, gave his name to the gas law and attacked the Aristotelian and Paracelsian theories of matter in The Sceptical Chymist [S1]. A devout Anglican and Christian apologist [S1; S2], he held that God made the world a lawful machine upheld by his "ordinary and general concourse" and sometimes recedes from its laws in miracles [S3, pp. 10, 160]. primary_system CHRIST at 0.7 (CLTHEI named). A 0, B 3, C 0, D 2, E 3, all at 0.7; mid_basin true (0.7).

## Life and work

Eton, a grand tour with a tutor (Geneva, Florence), Stalbridge and the Hartlib Circle, Oxford (c.1656–68), then London with his sister Lady Ranelagh [S1].

## Contribution and impact

Air-pump experiments (1659–60), Boyle's law (1662), The Sceptical Chymist (1661) and the corpuscular philosophy [S1].

## Childhood and education

Fourteenth child of the 1st Earl of Cork; a Christian conversion in Geneva in his teens [S1; S2, §1].

## Adult working worldview

Laws of motion given by God "to Matter, not to Himself" [S3, p. 158]; miracles as the stated exception [S3, p. 160]; revealed law with rewards and penalties [S4, p. 42]; reason judges whether a testimony is divine, then believes what it clearly teaches [S4, p. 118].

## Heritage (context only)

Anglo-Irish aristocracy [S1]. Context only.

## Timing

First lasting contribution 1660, at about 33 [S1]. The worldview texts read are from 1686 and 1690.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form absent; circle absent.

## Open questions

- The Hunter and Davis edition; the Account of Philaretus.

## Research log

- 2026-10-02: Read Britannica (Principe), SEP (MacIntosh and Anstey), and the TCP transcriptions of the Free Enquiry (A28982) and The Christian Virtuoso (A28945).
