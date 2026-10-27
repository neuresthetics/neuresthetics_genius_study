---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch P; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-18
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to biology. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-18, by: "Grok Bot", summary: "Record created (stage 3 batch P, order P32: F 4, rank 95). Basics from Britannica (Britannica Editors, unsigned; body only) and the two Nature papers' publisher pages (dates). Worldview from his own letters as quoted in Mark Goldie, Storm over a Chapel (Churchill College, 2024) and Chris Beckett, Medical History 48 (2004): to Churchill, 12 October 1961 ('atheists and agnostics such as myself'), to Cockcroft, n.d. [1961] (a university furthering 'superstitions' is 'shameful'), and of 14 December 1965 ('I am an atheist'); secondary quotations, primary check pending. Scientist (P30). primary_system ATHE (0.5); A 4 (0.5, alt BELOW_THRESHOLD, P38); B 3 (0.5, alt 4; P35); D 4 (0.5); mid_basin BELOW_THRESHOLD. Plotted (faded). Draft, not reviewed."}
    - {date: 2026-10-18, by: "Grok Bot", summary: "Batch P audit fixes (gs_08be43b_P run 1: 39 hold, 6 weaken). Cockcroft letter quoted in full as Goldie prints it, restoring the sentences 'this point of view' refers to (C4). Context added: the 1961 Churchill letter's 'atheists and agnostics such as myself' sits inside his satirical 'Hetairae fund' offer (note 1); the 1965 sentence is credited to Beckett in full, with Goldie quoting only from 'I am an atheist' (note 3); P38 noted as applied by analogy to private letters (note 2). Values unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #94, F4 rank 95). Needs: A 4 @0.5 alt BELOW (P38 atheist/agnostic); B 3 @0.5 alt 4 (P35); primary ATHE @0.5; mid BELOW; plotted faded (B single → hollow). Dual bio: Britannica (S1) + Wikipedia EN (S7) (P50). P47 source_quality on S1–S12. Primary/near-primary: Wellcome Collection catalogue PP/CRI/E/1/14/5 (S8) prints the 1965 Danz-venue paragraph in full ('I am an atheist'); Goldie (S4) prints the 12 Oct 1961 Churchill letter in full (CHUR 2/571). What Mad Pursuit extracts (S9 Positive Atheism reprint of autobiography): 'skeptic, an agnostic with a strong inclination toward atheism' (age ~12 onward) + science making religious beliefs untenable / Argument from Design shattered by Darwin; Wikiquote WMP p. 138 'not designed, but rather evolved' (S10). Of Molecules and Men (1966) anti-vitalism via multi-secondary page agreement (S10 Wikiquote p. 10 physics-and-chemistry aim; p. 99 vitalists/cranks; S11 Wellcome blog OMM p. 16 vitalism definition; S4 Goldie paraphrase 'other than chemistry and mechanics') — full OMM/AH IA borrow-restricted. Astonishing Hypothesis (S12 wiki synopsis): mental activities entirely due to nerve cells etc.; Wellcome blog AH p. 261 disembodied soul as unnecessary as Life Force. Telegraph 2003 Ridley interview (S13): 'The god hypothesis is rather discredited' (late; P8). A stays 4 @0.5 alt BELOW (P38: published disbelief/atheist label together with agnostic self-description in WMP and 1961 pairing; Russell pattern); support corroborated S4+S5+S8+S9. B 3 @0.5 → 4 @0.7 written_profession (OMM physics/chemistry + deny vital-force exception; P35 no longer binds); alt 3 if 'ultimate aim of the modern movement' read as method-only; support corroborated S10+S11+S4 (+ WMP S9/S10 design/evolved). primary ATHE @0.5 (AGNOS alt). D 4 @0.5 → @0.7 (Cockcroft + WMP superstition/vestiges; support corroborated). mid_basin BELOW (A 0.5 blocks P10 0.7 bar). Chart-moving YES: B single→corroborated hollow→filled; still faded (min(A,B)=0.5). Childhood Congregational filled from WMP. No fallacy_catalog. Draft, not reviewed."}

identity:
  id: crick-francis
  display_name: "Francis Crick"
  roster:
    canonical_name: "Francis Crick"
    rank: 95
    F: 4
    models: [Claude, DeepSeek, Gemini, Grok]
    band: "core (3–4)"
    status: core
    field: biology
    field_bucket: "biology / life science"
  full_name: {value: "Francis Harry Compton Crick", certainty: 1.0, cites: [{source: S1, locator: "header ('Also known as')"}, {source: S7, locator: "lead"}], how_known: "Britannica and Wikipedia agree (P15)."}
  native_name: {value: UNKNOWN, how_known: "English."}
  aliases:
    - {name: "Crick-Francis", kind: "roster alias"}

basics:
  birth:
    date: {value: "1916-06-08", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "infobox / lead"}], how_known: "Britannica and Wikipedia agree."}
    place: {value: "Northampton, Northamptonshire, England", modern_name: "Northampton, United Kingdom", polity_then: "United Kingdom", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "Early life and education"}], how_known: "Britannica and Wikipedia agree."}
  death:
    date: {value: "2004-07-28", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "infobox / lead"}], how_known: "Britannica and Wikipedia agree."}
    place: {value: "San Diego, California, U.S.", modern_name: "San Diego, California, United States", polity_then: "United States", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "Death"}], how_known: "Britannica and Wikipedia agree."}
  first_lasting_contribution_year: {value: 1953, certainty: 0.7, cites: [{source: S2, locator: "citation metadata"}, {source: S1, locator: "Watson paragraph"}], how_known: "The double-helix model (S1, undated there), published as Watson and Crick, Nature 171 (April 1953), p. 737 (S2)."}
  era_bucket: {value: "1950 on", certainty: 0.7, cites: [{source: S2, locator: "citation metadata"}], how_known: "From 1953 (P2); 1961 gives the same bucket."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "United Kingdom (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "Strangeways and Cavendish paragraph"}], how_known: "Cambridge during the working years (1953–1961); the Salk Institute from 1977 (S1)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [English], certainty: 0.7, cites: [{source: S1, locator: "titles"}], how_known: "Britannica."}
  occupations: {value: ["biophysicist", "molecular biologist", "neuroscientist"], certainty: 0.7, cites: [{source: S1, locator: "opening; Salk sentence"}, {source: S7, locator: "lead"}], how_known: "Britannica and Wikipedia."}

contribution:
  primary_domain: biology
  fields: {value: ["molecular biology", "genetics", "neuroscience"], certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S7, locator: "lead"}], how_known: "Britannica and Wikipedia."}
  lasting_original_contributions:
    - {value: "Double-helix model of DNA (with James Watson)", year: 1953, kind: discovery, lasting: "'a cornerstone of genetics and ... widely regarded as one of the most important discoveries of 20th-century biology' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; Watson paragraph"}, {source: S2, locator: "citation metadata"}], how_known: "Britannica; year from the Nature paper (S2). A result about natural systems, so he is a scientist (P30)."}
    - {value: "Triplet codons: each group of three bases designates an amino acid", year: 1961, kind: discovery, lasting: "'helped clarify the way in which the cell eventually uses the DNA \"message\" to build proteins' (S1)", certainty: 0.7, cites: [{source: S1, locator: "codon paragraph"}, {source: S3, locator: "citation metadata"}], how_known: "Britannica ('By 1961'); dated by Crick, Barnett, Brenner and Watts-Tobin, Nature 192 (December 1961), p. 1227 (S3)."}
  evidence_of_impact:
    - {value: "Nobel Prize for Physiology or Medicine (1962, with Watson and Wilkins); Order of Merit (1991)", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "opening; last paragraph"}], how_known: "Britannica."}
  major_works:
    - {value: "Of Molecules and Men", year: 1966, kind: "book", certainty: 0.7, cites: [{source: S4, locator: "p. 3"}, {source: S8, locator: "description (Danz Lectures → Of Molecules and Men)"}], how_known: "John Danz Lectures 1966, published as Of Molecules and Men; anti-vitalism."}
    - {value: "What Mad Pursuit: A Personal View of Scientific Discovery", year: 1988, kind: "book", certainty: 0.7, cites: [{source: S9, locator: "headnote (Basic Books)"}, {source: S7, locator: "Views on religion / Crick 1990 p. 10 note"}], how_known: "Autobiography; religion chapter extracted in S9."}
    - {value: "The Astonishing Hypothesis: The Scientific Search for the Soul", year: 1994, kind: "book", certainty: 0.7, cites: [{source: S12, locator: "infobox / Synopsis"}], how_known: "Late neuroscience book; IA borrow-restricted this pass."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Congregational (nonconformist Protestant); parents religious in a quiet way, not especially devout", certainty: 0.7, cites: [{source: S9, locator: "opening extracts (WMP)"}], how_known: "His autobiography: Congregational Church on Abington Avenue; father briefly church secretary; mother admired the clergyman."}
  family_religious_practice: {value: "Sunday church attendance with parents when old enough; no family prayers", certainty: 0.7, cites: [{source: S9, locator: "opening extracts (WMP)"}], how_known: "WMP."}
  parents_and_household:
    - {value: "Harry Crick (father) and Annie Wilkins (mother)", certainty: 0.5, cites: [{source: S14, locator: "Life"}], how_known: "Humanists UK heritage page (secondary)."}
  household_circumstances: {value: TODO}
  schooling:
    - {value: "Mill Hill School (boarding); compulsory chapel; sang in choir until voice broke", stage: "grammar or secondary school", years: UNKNOWN, certainty: 0.7, cites: [{source: S9, locator: "school paragraph (WMP)"}, {source: S14, locator: "Life (Mill Hill)"}], how_known: "WMP; school name from Humanists UK."}
    - {value: "University College London; B.Sc. (University of London) 1937; physics", stage: university, years: "1934–1937", certainty: 0.7, cites: [{source: S7, locator: "Early life and education"}, {source: S14, locator: "Life"}], how_known: "Wikipedia and Humanists UK."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure:
    - {value: "Growing interest in science before puberty; preferred scientific answers over church", certainty: 0.7, cites: [{source: S9, locator: "loss-of-faith paragraph (WMP)"}], how_known: "WMP."}
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [English], certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  notable_events:
    - {value: "About age twelve: told his mother he no longer wished to go to church; from then on 'a skeptic, an agnostic with a strong inclination toward atheism'", year: UNKNOWN, certainty: 0.7, cites: [{source: S9, locator: "loss-of-faith paragraph (WMP)"}], how_known: "WMP autobiography (retrospective; P20 cap would apply if used alone for adult A)."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1953–1961", certainty: 0.7, cites: [{source: S2, locator: "citation metadata"}, {source: S3, locator: "citation metadata"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "A college 'with a special emphasis on science' should not 'tacitly endorse' Christian beliefs with a chapel (1961); scientific knowledge makes certain religious beliefs untenable; unexplained areas can be a 'refuge for religious superstition' (WMP)", certainty: 0.7, cites: [{source: S4, locator: "pp. 4–5"}, {source: S9, locator: "science-and-religion paragraph (WMP)"}], how_known: "1961 Churchill letter (Goldie full text) plus WMP autobiography extracts."}
  primary_system:
    value: ATHE
    basis: consistent_private_letters
    certainty: 0.5
    cites: [{source: S4, locator: "pp. 4–5; p. 12"}, {source: S5, locator: "text at note 18"}, {source: S8, locator: "description (1965-12-14 paragraph)"}, {source: S9, locator: "agnostic/atheism sentence (WMP)"}]
    rationale: "Self-description: 'I am an atheist' (14 Dec 1965, Wellcome catalogue transcription of PP/CRI/E/1/14/5) and 'atheists and agnostics such as myself' (12 Oct 1961). WMP: 'agnostic with a strong inclination toward atheism'. Named alternatives: AGNOS (pairing) and SECHUM (humanist identity; essay prize / Humanists UK — no full humanist essay primary read)."
    how_known: "1961 letters inside working years; 1965 letter four years after. 0.5 under P38 (published/lettered disbelief together with agnostic self-description; Russell pattern) even after Wellcome catalogue upgrade of the 1965 letter."
  secondary_system: {value: UNKNOWN, how_known: "SECHUM is a lead (Cambridge Humanist Society essay prize; Humanists UK; Wikipedia humanist definition) — full essay primary unread."}
  candidate_codes_considered:
    - {code: ATHE, reason: "'I am an atheist' (1965); 'god hypothesis is rather discredited' (2003 interview, late)."}
    - {code: AGNOS, reason: "'atheists and agnostics such as myself' (1961); WMP 'agnostic with a strong inclination toward atheism'."}
    - {code: SECHUM, reason: "Lead: Cambridge Humanist Society essay prize (S4); Humanists UK supporter page (S14); Wikipedia humanist definition quote — primary essay unread."}
  lio_axes:
    A_locus:
      value: 4
      basis: consistent_private_letters
      certainty: 0.5
      support: corroborated
      cites: [{source: S4, locator: "pp. 4–5"}, {source: S5, locator: "text at note 18"}, {source: S8, locator: "description (1965-12-14 paragraph)"}, {source: S9, locator: "agnostic/atheism sentence (WMP)"}]
      rationale: "No God (P38): 'I am an atheist' (1965, Wellcome catalogue) and Christianity among 'superstitions' (Cockcroft 1961). P38 binds: stated disbelief / atheist label together with an agnostic self-description (1961 'atheists and agnostics such as myself'; WMP 'agnostic with a strong inclination toward atheism') scores A 4 at most 0.5, with BELOW_THRESHOLD as the named alternative (Russell pattern). Telegraph 2003 'god hypothesis is rather discredited' (S13) agrees but is late interview (P8) and does not lift the P38 cap."
      how_known: "Private letters now backed by Wellcome Collection catalogue transcription (S8) and Goldie full print of Churchill letter (S4); WMP published autobiography (S9). Independent source ids → corroborated (P48). Certainty stays 0.5 under P38."
      alternatives:
        - {value: BELOW_THRESHOLD, note: "P38: agnostic pairing (1961 letter and WMP) as explicit suspension.", cites: [{source: S4, locator: "p. 5"}, {source: S9, locator: "agnostic/atheism sentence (WMP)"}]}
    B_cause:
      value: 4
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S10, locator: "Of Molecules and Men p. 10; p. 99"}, {source: S11, locator: "OMM p. 16 vitalism definition"}, {source: S4, locator: "p. 3 (OMM vitalism paraphrase)"}, {source: S9, locator: "Argument from Design / Darwin paragraph (WMP)"}, {source: S10, locator: "What Mad Pursuit p. 138 ('not designed, but rather evolved')"}]
      rationale: "Scored on his account of nature (P6, P16). Of Molecules and Men (1966, John Danz Lectures immediately after the span): 'The ultimate aim of the modern movement in biology is in fact to explain all biology in terms of physics and chemistry' (p. 10); vitalism defined as 'some special force directing the growth or the behaviour of living systems which cannot be understood by our ordinary notions of physics and chemistry' (p. 16) and rejected — 'only cranks will believe tomorrow' (p. 99). That is a stated no-exception-to-physics/chemistry claim for living systems (denies vital-force exemptions), so B 4; P35's working-science-only cap no longer binds. WMP agrees: Argument from Design shattered by Darwin; 'what they see was not designed, but rather evolved' (p. 138). Named alternative 3: if 'ultimate aim of the modern movement' is read as method-aim only without an ontological no-exception claim."
      how_known: "OMM full PDF IA borrow-restricted this pass; page-cited quotes agree across Wikiquote (S10), Wellcome Library blog (S11), and Goldie (S4). WMP extracts (S9) and Wikiquote WMP p. 138 (S10) are independent. Multi-secondary agreement on a short published own book → 0.7 written_profession; P26 full-page primary check of OMM still open. Independent source ids → corroborated (P48)."
      alternatives:
        - {value: 3, note: "If OMM's 'ultimate aim of the modern movement' is method-aim only (no ontological no-exception) and anti-vitalism is read as research program rather than nature's order.", cites: [{source: S10, locator: "Of Molecules and Men p. 10"}]}
    C_ledger: {value: UNKNOWN, how_known: "Nothing on judgement or moral reckoning read. AH denies a persisting non-material soul (S11/S12) but that is locus/mind, not a ledger claim."}
    D_authority:
      value: 4
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S4, locator: "p. 12"}, {source: S9, locator: "science-and-religion paragraph (WMP)"}]
      rationale: "Religion keeps no say of its own: Cockcroft letter (1961) — furtherance of 'superstitions' by a university is 'shameful'. WMP: scientific knowledge makes certain religious beliefs untenable; unexplained areas as 'refuge for religious superstition'; task to remove 'unfortunate vestiges of earlier beliefs'. No alternative domain of religious authority is allowed."
      how_known: "Private letter (Goldie from Olby) plus published autobiography extracts. Independent streams → corroborated (P48); 0.7."
    E_scope: {value: UNKNOWN, how_known: "Nothing read on in-group favour in the world's order (P7)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A 4 but at 0.5: the A ≥ 3 branch reads A only (P10) and needs 0.7, as for Skinner and Shannon before their A lifts. B is now 4 @0.7 but does not decide this branch."}
  statements:
    - text: "Moreover it would be open (conscience permitting) not merely to members of the Church of England, but also to Catholics, Non-Conformists, Jews, Muslims, Hindus, Zen Buddhists and even to atheists and agnostics such as myself."
      cites: [{source: S4, locator: "pp. 4–5"}]
      date: "1961-10-12"
      context: "Letter to Winston Churchill, 12 October 1961, after Churchill's reply to his resignation over the proposed chapel; the sentence sits inside a satirical offer: Crick encloses 'a cheque for ten guineas to open the Churchill College Hetairae fund' (a college brothel, by parody of Churchill's 'amenity which many … may enjoy, and none need enter it unless they wish'). Churchill Papers 2/571, as printed in full by Goldie (S4, pp. 4–5). The self-label 'atheists and agnostics such as myself' is his own even inside the satire."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Deepen D1: Goldie prints the letter in full with archive reference; Bloomsbury Churchill Archive paywalled — facsimile not opened. Photograph noted in Pagnamenta (2008), p. 263 (unread)."
    - text: "I am sure there are many people in Cambridge, especially scientists, who believe that nowadays Christianity is a firm superstition, and who feel that this will become increasingly obvious to most educated people in the future. Apparently this does not prevent unbelievers from accepting college fellowships. Indeed some of them go so far as to have their children christened, which seems to me ridiculous. One can only conclude that they regard Christianity as a completely harmless set of beliefs and that they tolerate it as one might humour a somewhat eccentric aunt. I cannot agree with this point of view. It seems to me shameful that a great university should be used for the furtherance of superstitions and although Christianity is no longer virulent, it is surely not yet harmless."
      cites: [{source: S4, locator: "p. 12"}]
      context: "Letter to John Cockcroft, Master of Churchill College, undated (1961), explaining his resignation; Crick Papers, quoted by Goldie from Olby (2009), pp. 318–19 (S4)."
      axes: [A_locus, D_authority]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-18
      note: "Undated in S4; the resignation is 1961. Quoted in full as Goldie prints it. Primary check of Crick Papers still pending."
    - text: "You may not know that I am an atheist and a few years ago resigned my Fellowship at Churchill College because they threatened to build a College Chapel."
      cites: [{source: S8, locator: "description (1965-12-14 paragraph)"}, {source: S5, locator: "text at note 18 (PP/CRI/E/1/14/5)"}]
      date: "1965-12-14"
      context: "Letter on the venue for his John Danz Lectures (Seattle, 1966; published as Of Molecules and Men). Wellcome Collection catalogue for PP/CRI/E/1/14/5 prints the surrounding paragraph: lectures 'will not be militantly anti-Christian, but nevertheless will be directed against the sort of ideas at present held by many religious people'; he has 'not the slightest objection to lecturing in the Presbyterian Church' but thinks Church Authorities might not want the building used for what they might regard as 'anti-Christian propaganda'. Venue changed to Roosevelt High School Auditorium after this letter."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Deepen D1: Wellcome Collection works page quotes the paragraph under CC-BY for Crick-created archive material; image of the letter itself not opened. Beckett (S5) agrees."
    - text: "Whatever the reason, from then on I was a skeptic, an agnostic with a strong inclination toward atheism."
      cites: [{source: S9, locator: "loss-of-faith paragraph (WMP)"}]
      context: "What Mad Pursuit (1988 autobiography), recalling loss of Christian faith about age twelve; continues that loss of faith and attachment to science shaped his choice of problems (gene; later consciousness) because unexplained areas can be a 'refuge for religious superstition'."
      axes: [A_locus]
      kind: autobiography
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "IA borrow-restricted for full WMP; long extracts match Wikipedia's WMP p. 10 cite (S7 n. 103). P38 pairing."
    - text: "The ultimate aim of the modern movement in biology is in fact to explain all biology in terms of physics and chemistry."
      cites: [{source: S10, locator: "Of Molecules and Men (1966), p. 10"}]
      date: "1966"
      context: "Of Molecules and Men (John Danz Lectures). Anti-vitalism book; paired with the p. 16 definition of vitalism as a special force beyond ordinary physics and chemistry, and the p. 99 prophecy that only cranks will believe vitalism tomorrow."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Full OMM PDF IA borrow-restricted; P26 primary page-check open. Independent Wellcome blog (S11) and Goldie (S4) agree on the anti-vitalism thesis."
    - text: "Biologists must constantly keep in mind that what they see was not designed, but rather evolved."
      cites: [{source: S10, locator: "What Mad Pursuit, p. 138"}]
      context: "What Mad Pursuit, on biological mechanism and the danger of using elegance as a guide; evolutionary origin of DNA near the origin of life."
      axes: [B_cause]
      kind: autobiography
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Supports natural selection against design; not by itself a no-exception claim."
  changes_over_life:
    - {value: "Childhood Congregational practice → loss of faith ~age 12 (agnostic with strong inclination toward atheism) → adult militant anti-chapel atheism (1961–65) → late 'god hypothesis is rather discredited' / 'bankrupt' (2003–04)", certainty: 0.5, cites: [{source: S9, locator: "WMP"}, {source: S4, locator: "p. 5"}, {source: S13, locator: "Crick quotations"}], how_known: "Consistent anti-theism; P38 pairing never fully dropped in published self-description."}
  coder_notes: "Deepen D1 2026-10-24: Wellcome catalogue upgrades 1965 letter; Goldie full Churchill letter retained; WMP extracts (Positive Atheism) and OMM multi-secondary page quotes added. A stays P38 @0.5 (cannot reach 0.7 while agnostic pairing stands). B lifted off P35 by OMM anti-vitalism. OMM/AH/WMP full IA borrow-restricted — residual P26. Churchill Archive (Bloomsbury) paywalled. No fallacy_catalog."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "English", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  religious_heritage_by_birth: {value: "Congregational (nonconformist Protestant)", certainty: 0.7, cites: [{source: S9, locator: "opening extracts (WMP)"}], how_known: "WMP family church."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1953–1961", certainty: 0.7, cites: [{source: S2, locator: "citation metadata"}, {source: S3, locator: "citation metadata"}], how_known: "First to last listed lasting contribution (P29, P30)."}
  age_at_first_lasting_contribution: {value: 37, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "citation metadata"}], how_known: "1953 − 1916 = 37 (P30)."}
  first_evidence_of_lio_type_views: {value: "1961: 'atheists and agnostics such as myself'; the furtherance of 'superstitions' by a university 'shameful'", year: 1961, certainty: 0.7, cites: [{source: S4, locator: "pp. 4–5; p. 12"}], how_known: "Goldie full print of Churchill letter; Cockcroft letter. Earlier WMP loss-of-faith is childhood."}
  lio_views_relative_to_major_work: {value: "during major work", rationale: "1961 falls inside 1953–1961.", certainty: 0.7, cites: [{source: S4, locator: "pp. 4–5"}], how_known: "Dates of what was read."}
  worldview_during_major_work: {value: "Atheist or agnostic, hostile to college religion (1961); anti-vitalist biology published 1966 immediately after the span", certainty: 0.5, cites: [{source: S4, locator: "pp. 4–5; p. 12"}, {source: S10, locator: "OMM p. 10"}], how_known: "Letters as printed; OMM just after span."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "Structural model-building of molecules (S1).", certainty: 0.5, cites: [{source: S1, locator: "Watson paragraph"}], how_known: "Coder's reading."}
  form_acquired: {value: "through the profession", certainty: 0.5, cites: [{source: S1, locator: "Strangeways and Cavendish paragraph"}], how_known: "Coder's reading."}
  circle_present: {value: "no", rationale: "No God; anti-vitalist physicalism.", certainty: 0.7, cites: [{source: S8, locator: "1965-12-14 paragraph"}, {source: S10, locator: "OMM p. 10"}], how_known: "Coder's reading."}
  reading: "Atheist / agnostic molecular biologist; anti-vitalist; later consciousness as neurons."
  notes: "Lane B only."

institutions:
  - {value: "Strangeways Research Laboratory, University of Cambridge", role: "biologist", years: "1947–1949", kind: "research institute", certainty: 0.7, cites: [{source: S1, locator: "Strangeways and Cavendish paragraph"}], how_known: "Britannica."}
  - {value: "Medical Research Council Unit, Cavendish Laboratory, Cambridge", role: "researcher", years: "1949–", kind: "research institute", certainty: 0.5, cites: [{source: S1, locator: "Strangeways and Cavendish paragraph"}], how_known: "Britannica gives the start; end year not read."}
  - {value: "Churchill College, Cambridge", role: "fellow (resigned 1961); later honorary fellow (1965)", years: "1960–1961", kind: university, certainty: 0.7, cites: [{source: S4, locator: "pp. 3–5"}, {source: S7, locator: "Views on religion"}], how_known: "Goldie; Wikipedia."}
  - {value: "Salk Institute for Biological Studies", role: "distinguished professor", years: "1977–2004", kind: "research institute", certainty: 0.7, cites: [{source: S1, locator: "Salk sentence"}], how_known: "Britannica."}
collaborators:
  - {value: "James Watson", relation: collaborator, note: "double helix", certainty: 0.7, cites: [{source: S1, locator: "Watson paragraph"}], how_known: "Britannica."}
  - {value: "Maurice Wilkins", relation: collaborator, note: "X-ray diffraction of DNA; Nobel 1962", certainty: 0.7, cites: [{source: S1, locator: "opening; Watson paragraph"}], how_known: "Britannica."}
  - {value: "Rosalind Franklin", relation: other, note: "her X-ray diffraction pictures were used for the model", certainty: 0.7, cites: [{source: S1, locator: "Watson paragraph"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S6, locator: "roster.csv, rank 95"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Britannica article is unsigned (Britannica Editors); read live (Wayback rate-limited)."
    - "OMM / WMP / AH full texts IA borrow-restricted; OMM and WMP quotes are multi-secondary with page numbers (P26 primary page-check open for OMM PDF)."
    - "Churchill Papers CHUR 2/571 facsimile behind Bloomsbury paywall; Goldie full transcription used."
  open_questions:
    - "Open OMM (1966) and AH (1994) full text for P26 page-check of B quotes; WMP full for surrounding religion chapter."
    - "Churchill Archive facsimile of CHUR 2/571; Crick Papers Cockcroft letter primary."
    - "Primary humanist essay ('human problems… without invoking supernatural authority') for possible SECHUM."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "Britannica Editors. \"Francis Crick.\" Encyclopaedia Britannica (revised 31 August 2026). https://www.britannica.com/biography/Francis-Crick. Read live 2026-10-18 (the Wayback Machine was rate-limiting)."
    url: "https://www.britannica.com/biography/Francis-Crick"
    accessed: 2026-10-18
    source_quality: "reference entry"
    reliability_note: "Unsigned article. Body and header only; the AI-generated Top Questions are not cited."
    used_for: [identity, basics, contribution, timing, lane_b, institutions, collaborators]
  - id: S2
    type: primary
    kind: "journal article"
    author: "J. D. Watson and F. H. C. Crick"
    citation: "Watson, J. D., and F. H. C. Crick. \"Molecular Structure of Nucleic Acids: A Structure for Deoxyribose Nucleic Acid.\" Nature 171 (April 1953): 737. https://www.nature.com/articles/171737a0"
    url: "https://www.nature.com/articles/171737a0"
    accessed: 2026-10-18
    source_quality: "primary / own words"
    reliability_note: "Publisher's page; used for the date only (citation metadata)."
    used_for: [basics, contribution, timing]
  - id: S3
    type: primary
    kind: "journal article"
    author: "F. H. C. Crick, Leslie Barnett, S. Brenner and R. J. Watts-Tobin"
    citation: "Crick, F. H. C., L. Barnett, S. Brenner and R. J. Watts-Tobin. \"General Nature of the Genetic Code for Proteins.\" Nature 192 (December 1961): 1227. https://www.nature.com/articles/1921227a0"
    url: "https://www.nature.com/articles/1921227a0"
    accessed: 2026-10-18
    source_quality: "primary / own words"
    reliability_note: "Publisher's page; used for the date only (citation metadata)."
    used_for: [contribution, timing]
  - id: S4
    type: secondary
    kind: "scholarly book"
    author: "Mark Goldie"
    citation: "Goldie, Mark. Storm over a Chapel: A History of the Chapel at Churchill College Cambridge. Cambridge: Churchill College, 2024. PDF: https://chapel.chu.cam.ac.uk/wp-content/uploads/2025/01/STORM-OVER-A-CHAPEL-2024-locked.pdf"
    url: "https://chapel.chu.cam.ac.uk/wp-content/uploads/2025/01/STORM-OVER-A-CHAPEL-2024-locked.pdf"
    accessed: 2026-10-24
    source_quality: "scholarly edition or monograph"
    reliability_note: "Signed college history by a Cambridge historian, read directly; prints the 12 Oct 1961 Churchill letter in full with CHUR 2/571 reference; Cockcroft letter via Olby 2009; OMM vitalism paraphrase p. 3."
    used_for: [worldview, timing, institutions, contribution]
  - id: S5
    type: secondary
    kind: "journal article"
    author: "Chris Beckett"
    citation: "Beckett, Chris. \"For the Record: The Francis Crick Archive at the Wellcome Library.\" Medical History 48, no. 2 (2004): 245–260. doi:10.1017/s0025727300007419. https://pmc.ncbi.nlm.nih.gov/articles/PMC546341/"
    url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC546341/"
    accessed: 2026-10-18
    source_quality: "scholarly edition or monograph"
    reliability_note: "Article by the archive's project archivist, read directly on PMC; quotes the 1965 letter with its catalogue number. Superseded for that letter's wording by S8 catalogue transcription."
    used_for: [worldview, lane_b]
  - id: S6
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-18
    source_quality: "study roster"
    reliability_note: "Study's own roster."
    used_for: [identity, review]
  - id: S7
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia contributors. \"Francis Crick.\" Wikipedia. https://en.wikipedia.org/wiki/Francis_Crick. Dual bio (P50). Read 2026-10-24."
    url: "https://en.wikipedia.org/wiki/Francis_Crick"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Used for dual-bio basics and as a finding aid to WMP p. 10 / OMM / humanist quotes; worldview coding rests on S4/S8/S9/S10, not on Wikipedia paraphrases."
    used_for: [identity, basics, contribution, institutions, childhood]
  - id: S8
    type: primary
    kind: letter
    author: "Francis Crick (via Wellcome Collection catalogue)"
    citation: "Wellcome Collection. \"John Danz Lectures, University of Washington, Seattle\" (PP/CRI/E/1/14/5), catalogue description quoting Crick's letter of 14 December 1965. https://wellcomecollection.org/works/v547ss3c"
    url: "https://wellcomecollection.org/works/v547ss3c"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "Archival catalogue transcription of Crick-created correspondence (CC-BY for Crick works); letter image not opened. Agrees with Beckett S5."
    used_for: [worldview]
  - id: S9
    type: secondary
    kind: "other"
    author: "Francis Crick (extracts); Atheist Centre / Positive Atheism reprint"
    citation: "Crick, Francis. Extracts from What Mad Pursuit: A Personal View of Scientific Discovery (Basic Books, 1988), reprinted as \"How I Got Inclined Towards Atheism,\" Atheist Centre Golden Jubilee International Conference Souvenir (Vijayawada, 1990), via Positive Atheism. Wayback: https://web.archive.org/web/20201216203835/http://www.positiveatheism.org/india/s1990a01.htm"
    url: "https://web.archive.org/web/20201216203835/http://www.positiveatheism.org/india/s1990a01.htm"
    accessed: 2026-10-24
    source_quality: "unofficial web copy"
    reliability_note: "Long first-person extracts presented as from WMP; IA full book borrow-restricted. Cross-checked against Wikipedia's WMP p. 10 cite for the agnostic/atheism sentence."
    used_for: [worldview, childhood, heritage, timing]
  - id: S10
    type: secondary
    kind: "other"
    author: "Wikiquote contributors"
    citation: "Wikiquote contributors. \"Francis Crick.\" Wikiquote. https://en.wikiquote.org/wiki/Francis_Crick (Of Molecules and Men pp. 10, 99; What Mad Pursuit pp. 59–60, 138; Life Itself p. 88)."
    url: "https://en.wikiquote.org/wiki/Francis_Crick"
    accessed: 2026-10-24
    source_quality: "unofficial web copy"
    reliability_note: "Page-cited quotations of Crick's published books; OMM/WMP full texts IA borrow-restricted — P26 primary page-check open. Cross-checked against todayinsci for OMM p. 10 / p. 99 and vitalism lines."
    used_for: [worldview, contribution]
  - id: S11
    type: secondary
    kind: "other"
    author: "Wellcome Library blog (archived)"
    citation: "\"Francis Crick: anti-vitalist crusader.\" Wellcome Library blog, September 2016. Archived: https://wayback.archive-it.org/16107/20210312182512/http:/blog.wellcomelibrary.org/2016/09/francis-crick-anti-vitalist-crusader/"
    url: "https://wayback.archive-it.org/16107/20210312182512/http:/blog.wellcomelibrary.org/2016/09/francis-crick-anti-vitalist-crusader/"
    accessed: 2026-10-24
    source_quality: "other"
    reliability_note: "Library staff blog; quotes OMM p. 16 vitalism definition and AH p. 261 on disembodied soul / Life Force with page numbers."
    used_for: [worldview]
  - id: S12
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia contributors. \"The Astonishing Hypothesis.\" Wikipedia. https://en.wikipedia.org/wiki/The_Astonishing_Hypothesis. Read 2026-10-24."
    url: "https://en.wikipedia.org/wiki/The_Astonishing_Hypothesis"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Synopsis only; full AH IA borrow-restricted. Used as lead for neuron/soul thesis, not as sole A/B scorer."
    used_for: [contribution, worldview]
  - id: S13
    type: secondary
    kind: other
    author: "Roger Highfield (interviewing Francis Crick; quotations via Matt Ridley)"
    citation: "Highfield, Roger. \"Do our genes reveal the hand of God?\" The Telegraph, 20 March 2003. https://www.telegraph.co.uk/news/science/science-news/3306329/Do-our-genes-reveal-the-hand-of-God.html"
    url: "https://www.telegraph.co.uk/news/science/science-news/3306329/Do-our-genes-reveal-the-hand-of-God.html"
    accessed: 2026-10-24
    source_quality: "newspaper interview"
    reliability_note: "Late (2003) interview; Crick: 'The god hypothesis is rather discredited.' Supporting only for A; P8 ceiling; does not lift P38."
    used_for: [worldview]
  - id: S14
    type: secondary
    kind: "other"
    author: "Humanists UK"
    citation: "Humanists UK. \"Francis Crick (1916-2004).\" Humanist Heritage. https://heritage.humanists.uk/francis-crick/"
    url: "https://heritage.humanists.uk/francis-crick/"
    accessed: 2026-10-24
    source_quality: "other"
    reliability_note: "Movement heritage page; used for parents' names and Mill Hill / UCL schooling only — not for worldview codes."
    used_for: [childhood]
---

# Francis Crick

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Francis Crick (1916–2004), British biophysicist [S1; S7]. Deepen D1: primary_system ATHE (0.5, AGNOS alt); A 4 at 0.5 alt BELOW_THRESHOLD (P38; Wellcome catalogue + WMP pairing); B 4 at 0.7 alt 3 (OMM anti-vitalism / physics-and-chemistry; support corroborated); D 4 at 0.7; mid_basin BELOW_THRESHOLD. Plotted faded; chart-moving YES (B single→corroborated, hollow→filled; still faded because A stays 0.5).

## Life and work

Cambridge from 1947; resigned Churchill College fellowship over the chapel (1961) [S4]; Salk Institute from 1977 [S1].

## Contribution and impact

The double helix (1953) and the triplet code (1961) [S1; S2; S3]. Of Molecules and Men (1966); What Mad Pursuit (1988); The Astonishing Hypothesis (1994) [S4; S9; S12].

## Childhood and education

Congregational family practice; lost faith about age twelve — 'agnostic with a strong inclination toward atheism' [S9]. Mill Hill; UCL B.Sc. 1937 [S7; S14].

## Adult working worldview

'atheists and agnostics such as myself' (1961) [S4]; 'I am an atheist' (1965, Wellcome catalogue) [S8]; WMP agnostic/atheism pairing keeps A at 0.5 under P38. OMM: all biology as physics and chemistry; reject vital force [S10; S11].

## Heritage (context only)

English; Congregational by upbringing [S1; S9].

## Timing

First lasting contribution 1953, at 37 [S1; S2].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No God; anti-vitalist physicalism [S8; S10].

## Open questions

- P26 page-check of OMM / AH / full WMP (IA borrow-restricted).
- Churchill Archive facsimile CHUR 2/571; Cockcroft letter primary.
- Humanist essay primary for SECHUM.

## Research log

- 2026-10-18: Read Britannica (live), the Nature citation pages, Goldie (Churchill College PDF) and Beckett (PMC) directly. Of Molecules and Men and The Astonishing Hypothesis are lending-only on the Internet Archive.
- 2026-10-24: Deepen D1. Wellcome Collection PP/CRI/E/1/14/5 catalogue; Goldie PDF re-read; WMP Positive Atheism extracts (Wayback); Wikiquote; Wellcome anti-vitalist blog (Archive-It); AH Wikipedia synopsis; Telegraph 2003; Humanists UK; Wikipedia EN dual bio. OMM/WMP/AH full IA borrow-restricted. Wrote drafts/deepen_crick-francis.md (untracked). No figures refresh. No fallacy_catalog.
