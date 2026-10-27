---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch S; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-18
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to biology. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-18, by: "Grok Bot", summary: "Record created (stage 3 batch S, order P32: F 4, rank 107). Basics from Britannica (Britannica Editors, unsigned; body only, read live) and Nature's page for her 1964 paper. Worldview from two interviews in her own words, both after the working years (1964–1986): On Being with Krista Tippett (recorded 2020; producer's transcript) and The Guardian (Stephen Moss, 13 January 2010). Scientist (P30). primary_system BELOW_THRESHOLD (candidates CHRIST, DEISM blocked by P27, PANENT, AGNOS); A 2 (0.5, interview; alt BELOW_THRESHOLD); B 3 (0.5, P35; alt 4); C UNKNOWN; D BELOW_THRESHOLD; E BELOW_THRESHOLD (P19); mid_basin BELOW_THRESHOLD. Plotted (faded) at A2/B3; A 2 sits between the branches of the mid-basin test. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Audit fixes for batch S (blind audit of c5d448a, run 1: GO5 WEAKEN; note). The 'just chance' line is marked as reported: it is what 'all of these great brains have said' (after Francis Collins), not her own argument. A 1 named as a second alternative. No value changes."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #106 / F4 rank 107). Goals: lift A/B to 0.7 if in-span or stronger own-voice; chart-moving if both ≥0.7 and/or corroboration. Dual bio: Britannica (S1) + Wikipedia EN (S6) (P50). P47 source_quality on S1–S8. Reason for Hope (1999) still unread as a book (IA borrow-restricted); long chain of her own words recovered via Orion Magazine republication of the RFH chapter 'In the Forests of Gombe' (S7) and NYT Books first-chapter excerpt (S8), plus Wikipedia secondary quotations of RFH Notre Dame / Reader's Digest / Laszlo foreword (S6 religion section). PANENT use_when now met: 'Great Spirit in Whom we live and move and have our being' (includes) + guiding / extra-cosmic Creator (exceeds). primary BELOW_THRESHOLD → PANENT @0.5 (written_profession; P20/P1 post-span cap; alt CHRIST). A stays 2 @0.5 (hedges on form: 'haven't the faintest idea' / 'don't have any idea of who or what God is'); basis interview → written_profession; support single→corroborated (P48: S2 + S7 + S6 Reader's Digest / RFH Notre Dame). B stays 3 @0.5 alt 4 (P35); RFH anti-chance / guiding power is extra-cosmic purpose, no P16 exception within nature — does not move B. mid BELOW; plotted faded hollow→faded filled. Chart-moving YES (fill only; darkness no). Full RFH book and Africa In My Blood letters unread. No fallacy_catalog. No figures refresh. Draft, not reviewed."}

identity:
  id: goodall-jane
  display_name: "Jane Goodall"
  roster:
    canonical_name: "Jane Goodall"
    rank: 107
    F: 4
    models: [Claude, Gemini, GPT, Grok]
    band: "core (3–4)"
    status: core
    field: biology
    field_bucket: "biology / life science"
  full_name: {value: "Dame Jane Goodall", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts ('In full')"}, {source: S6, locator: "lead / infobox"}], how_known: "Britannica and Wikipedia agree (P15)."}
  native_name: {value: "Valerie Jane Morris-Goodall", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts ('Original name')"}, {source: S6, locator: "infobox / Early life"}], how_known: "Britannica and Wikipedia agree."}
  aliases:
    - {name: "Goodall-Jane", kind: "roster alias"}
    - {name: "Jane-Goodall", kind: "roster alias"}

basics:
  birth:
    date: {value: "1934-04-03", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "infobox"}], how_known: "Britannica and Wikipedia agree."}
    place: {value: "London, England", modern_name: "London, United Kingdom", polity_then: "United Kingdom", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "infobox (Hampstead, London)"}], how_known: "Britannica and Wikipedia agree (Wikipedia specifies Hampstead)."}
  death:
    date: {value: "2025-10-01", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "programme note"}, {source: S6, locator: "Death"}], how_known: "Britannica, On Being memorial note, and Wikipedia agree."}
    place: {value: "Beverly Hills, California, U.S.", modern_name: "Beverly Hills, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S6, locator: "Death"}, {source: S1, locator: "opening"}], how_known: "Wikipedia (Beverly Hills, at a friend's home on a speaking tour); Britannica says Los Angeles (metro). Dual-bio note; Wikipedia more specific."}
  first_lasting_contribution_year: {value: 1964, certainty: 0.5, cites: [{source: S4, locator: "article page"}], how_known: "Her paper on chimpanzee tool-using in Nature, published 28 March 1964 (S4); the earliest dated item listed (P13, P30). The paper cites her own earlier papers (Ann. N.Y. Acad. Sci. 102, 1962; Symp. Zool. Soc. Lond. 10, 1963), not read, so the year might be 1962 or 1963 (named alternatives; coder's call at 0.5).", alternatives: [{value: 1963, note: "Symposium paper (unread).", cites: [{source: S4, locator: "references 7"}]}, {value: 1962, note: "Annals paper (unread).", cites: [{source: S4, locator: "references 12"}]}]}
  era_bucket: {value: "1950 on", certainty: 0.7, cites: [{source: S4, locator: "article page"}], how_known: "1964 and both alternatives fall in the same bucket (P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "United Kingdom (P3)."}
  region_of_work: {value: "Sub-Saharan Africa", certainty: 0.7, cites: [{source: S1, locator: "camp paragraph"}, {source: S6, locator: "Research at Gombe"}], how_known: "Gombe Stream, Tanzania (P3); writing done partly in Cambridge."}
  sex_as_recorded: {value: "female", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "books paragraph"}], how_known: "English titles (S1)."}
  occupations: {value: ["ethologist", "primatologist", "conservationist"], certainty: 0.7, cites: [{source: S1, locator: "opening; books paragraph"}, {source: S6, locator: "lead"}], how_known: "Britannica and Wikipedia."}

contribution:
  primary_domain: biology
  fields: {value: ["ethology", "primatology"], certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "Scientific career"}], how_known: "Britannica and Wikipedia."}
  lasting_original_contributions:
    - {value: "Chimpanzees make and use tools: 'Tool-Using and Aimed Throwing in a Community of Free-Living Chimpanzees' (Nature)", year: 1964, kind: discovery, lasting: "Britannica lists tool-making among the misunderstandings she corrected (S1)", certainty: 0.5, cites: [{source: S4, locator: "article page"}, {source: S1, locator: "findings paragraph"}], how_known: "Britannica does not date the finding; the Nature page dates the paper (28 March 1964). Earlier papers not read (see first_lasting_contribution_year). A result about animal behaviour from field observation, so she is a scientist (P30, P35 addendum)."}
    - {value: "Long-term field findings on chimpanzees: omnivorous diet and 'complex and highly developed social behaviors'", year: "1960s–1986", kind: "body of work", lasting: "corrected 'a number of misunderstandings about chimpanzees' (S1)", certainty: 0.7, cites: [{source: S1, locator: "findings paragraph"}, {source: S6, locator: "Research at Gombe"}], how_known: "Britannica / Wikipedia; not used for the span (CODING_GUIDE §8)."}
    - {value: "In the Shadow of Man", year: 1971, kind: work, lasting: "named as notable (S1)", certainty: 0.7, cites: [{source: S1, locator: "books paragraph"}, {source: S6, locator: "Works"}], how_known: "Britannica and Wikipedia."}
    - {value: "The Chimpanzees of Gombe: Patterns of Behavior, the summary of her years of observation", year: 1986, kind: work, lasting: "her summary work (S1)", certainty: 0.7, cites: [{source: S1, locator: "books paragraph"}, {source: S6, locator: "Works"}], how_known: "Britannica; the latest listed lasting contribution (P30 addendum). Her later work was advocacy (S1, S2)."}
  evidence_of_impact:
    - {value: "Templeton Prize (2021); DBE (2003, investiture 2004); Stephen Hawking Medal for Science Communication (2022); Presidential Medal of Freedom (2025)", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "honours paragraph"}, {source: S6, locator: "Awards and recognition"}], how_known: "Britannica and Wikipedia agree on the prizes; Wikipedia dates the DBE investiture to 2004."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Long-term field research that changed the scientific account of chimpanzees (S1).", certainty: 0.7, cites: [{source: S1, locator: "findings paragraph"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Christian (Congregational): grandfather a Congregational minister", certainty: 0.7, cites: [{source: S2, locator: "childhood exchange"}, {source: S3, locator: "Christian paragraph"}, {source: S6, locator: "Religion and spirituality"}], how_known: "(interview) 'my grandfather was a Congregational minister. I never met him' (S2); 'I was raised as a Christian' (S3); Wikipedia concurs."}
  family_religious_practice: {value: "Occasional churchgoing; more regular as a teenager under minister Trevor Davies (RFH, via S6)", certainty: 0.5, cites: [{source: S6, locator: "Religion and spirituality"}], how_known: "Wikipedia secondary quotation of Reason for Hope; book not read page-by-page."}
  parents_and_household:
    - {value: "Lived in Bournemouth with her mother, sister, grandmother and her mother's two sisters", certainty: 0.7, cites: [{source: S2, locator: "childhood exchange"}], how_known: "(interview) Her own account (S2)."}
  household_circumstances: {value: TODO}
  schooling:
    - {value: "Left school at 18; no undergraduate degree; later Ph.D. Cambridge without a bachelor's (eighth such case)", stage: "grammar or secondary school", years: "–1952", certainty: 0.7, cites: [{source: S1, locator: "early-life paragraph"}, {source: S6, locator: "Education"}], how_known: "Britannica; Wikipedia adds Cambridge without B.A."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure:
    - {value: "'interested in animal behavior from an early age'", certainty: 0.7, cites: [{source: S1, locator: "early-life paragraph"}], how_known: "Britannica."}
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["English"], certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1964–1986", certainty: 0.5, cites: [{source: S4, locator: "article page"}, {source: S1, locator: "books paragraph"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "'I suppose so; I was raised as a Christian' (asked if she was still a Christian, 2010)", certainty: 0.5, cites: [{source: S3, locator: "Christian paragraph"}], how_known: "(interview) Her words; the interviewer calls the answer 'somewhat ambiguous'. Context only: upbringing gives no code (CHRIST do_not_use_when)."}
  self_described_science_religion_relation: {value: "(written) RFH / Orion: 'HOW SAD THAT SO MANY PEOPLE seem to think that science and religion are mutually exclusive' and evolution-compatible Christian parable (seven days as millions of years; Spirit breathed into Homo sapiens) (S7). (interview) She 'sees no contradiction between evolution and a belief in God' (2010, interviewer's paraphrase); 'there are some answers that, at least on this planet, this life, this life-form, we will not be able to answer' (2020)", certainty: 0.5, cites: [{source: S7, locator: "science-and-religion section"}, {source: S8, locator: "Beginnings (mind that can contemplate God)"}, {source: S3, locator: "Christian paragraph"}, {source: S2, locator: "closing exchange"}], how_known: "Orion republication of RFH chapter (S7) plus interviews after the working years (P20 ruling P1)."}
  primary_system:
    value: PANENT
    basis: written_profession
    certainty: 0.5
    cites: [{source: S7, locator: "Cambridge / Great Spirit paragraphs"}, {source: S6, locator: "Religion and spirituality (RFH Notre Dame; Laszlo foreword)"}]
    rationale: "PANENT use_when (v8): a divine reality that includes the world and also exceeds it. Own words in the RFH chapter republished by Orion: God is 'the Great Spirit in Whom \"we live and move and have our being\"' (world in God) and she had already believed, as a Christian, in 'the spiritual power' she called God before Cambridge (S7). Exceeds: RFH Notre Dame ('guiding power in the universe… I must believe in God'; anti-chance) and the 2017 Laszlo foreword ('unknown and unknowable Creator, a Supreme Being, a Great Spiritual Power' / Intelligence driving evolution) (S6 secondary quotations). Spiritual power felt 'particularly when I'm out in nature' / 'in every living thing' (Reader's Digest via S6; Templeton title echo). Named alternative CHRIST: she says she called God as a Christian and uses Holy-Ghost parable language (S7), but she also names Allah, Tao, Brahma, Creator as One God — broader than CHRIST's use_when alone. DEISM still blocked (no rejection of revelation, P27). AGNOS ruled out by 'I'm absolutely sure that there is something' (S2) and 'I must believe in God' (RFH). Certainty 0.5: Reason for Hope (1999) and later interviews/forewords are after the working years (1964–1986), so P20 ruling P1 (Shannon/Watson) caps at 0.5; hedges on form ('haven't the faintest idea' / 'don't have any idea of who or what God is') also keep 0.5."
    how_known: "Written profession in Reason for Hope (1999), read via Orion Magazine republication of the Gombe chapter (S7), NYT Books ch.1 excerpt (S8), plus Wikipedia secondary quotations of the Notre Dame and Laszlo passages (S6). Book itself unread page-by-page (IA borrow-restricted)."
    note: "Cambridge beliefs 'already moulded' by age 27 (S7) — retrospective about the start of the working years. Brief waver / denial after Derek Bryceson's death (1980), then return via the forest (S7); P31: lasting contributions before and through 1986 keep the PANENT reading for the span. May 1981 Gombe 'outsight' (merge with 'spirit power of life itself') is dated inside the span but narrated in 1999."
  secondary_system: {value: UNKNOWN, how_known: "One system (P29). CHRIST kept as named alternative on primary, not a second published system."}
  candidate_codes_considered:
    - {code: PANENT, reason: "Adopted at 0.5: Great Spirit in Whom we live and move (S7) + guiding / extra-cosmic Creator (S6 RFH Notre Dame; Laszlo). Prior rejection ('no includes-and-exceeds') overturned by RFH own words."}
    - {code: CHRIST, reason: "Named alternative: 'as a Christian, I called God' and Holy-Ghost parable (S7); hedged 'I suppose so; I was raised as a Christian' (S3). Not primary: she explicitly expands to One God under many names."}
    - {code: DEISM, reason: "Intelligence / guiding power behind the universe; blocked: revelation is not rejected (P27); she affirms spiritual experience and scripture-as-parable (S7)."}
    - {code: AGNOS, reason: "'I haven't the faintest idea' what it is (S2); rejected: she is 'absolutely sure that there is something' and 'must believe in God'."}
  lio_axes:
    A_locus:
      value: 2
      basis: written_profession
      certainty: 0.5
      support: corroborated
      cites: [{source: S7, locator: "Cambridge / Great Spirit; May 1981 outsight"}, {source: S2, locator: "closing exchange; 1986 exchange"}, {source: S6, locator: "Religion and spirituality (RFH Notre Dame; Reader's Digest 2010)"}]
      rationale: "Mixed (2): transcendent / beyond-the-world features ('intelligence behind the universe', 'guiding power in the universe', 'extra-cosmic' / Creator of the Big Bang, 'Supreme Being') sit with immanent features ('Great Spirit in Whom we live and move and have our being', spiritual power 'in every living thing', May 1981 merge with 'spirit power of life itself', 'deep, spiritual connection to the natural world'). Neither pole is stated as limited. Named alternatives: BELOW_THRESHOLD (she has not 'the faintest idea' / 'don't have any idea of who or what God is') and 1 ('behind the universe' / guiding power read as a transcendent locus). Deepen D1: RFH own-voice strengthens the mixed reading but does not resolve the hedge on form, so certainty stays 0.5 (P20/P1 post-span + hedged self-report)."
      how_known: "Written profession (RFH via Orion S7) plus recorded interviews (S2, Reader's Digest via S6). All first-person worldview texts read are from 1999 onward, after 1964–1986, so 0.5 (P20 ruling P1). Support corroborated (P48): S7 (RFH chapter), S2 (On Being), and S6's Reader's Digest / Notre Dame quotations agree on a spiritual power / God that is both beyond and felt in nature."
      alternatives:
        - {value: BELOW_THRESHOLD, note: "'I haven't the faintest idea' / 'don't have any idea of who or what God is'.", cites: [{source: S2, locator: "closing exchange"}, {source: S6, locator: "Reader's Digest 2010"}]}
        - {value: 1, note: "'behind the universe' / 'guiding power' / Creator read as a transcendent locus; mid_basin stays BELOW_THRESHOLD at 0.5.", cites: [{source: S2, locator: "closing exchange"}, {source: S6, locator: "RFH Notre Dame"}]}
    B_cause:
      value: 3
      basis: inference_from_work
      certainty: 0.5
      support: corroborated
      cites: [{source: S4, locator: "article page"}, {source: S1, locator: "findings paragraph"}, {source: S7, locator: "science window / evolution parable"}]
      rationale: "Scored on her account of nature (P6). She is a scientist (P30), so B comes from her working science: lawful field observation of animal behaviour, B 3 with 4 as the named alternative, never 4 (P35). Deepen D1: RFH 'anti-chance' / 'guiding power' / Intelligence driving evolution (S6, S7) state purpose at the cosmic / cultural level, not an exception inside natural law as observed in the field; they do not move B under P16. The On Being 'just chance' line remains reported speech (what 'great brains have said'), not her own argument."
      how_known: "Inferred from her working science (P24, P35). Support corroborated (P48): Nature paper page (S4) and Britannica findings (S1) independently document lawful field ethology; S7 confirms she kept the scientific window alongside the spiritual one."
      alternatives:
        - {value: 4, note: "P35 alternative.", cites: [{source: S4, locator: "article page"}]}
    C_ledger: {value: UNKNOWN, how_known: "Nothing on reward and punishment in the sources read (S1–S8)."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "She says some questions 'we will not be able to answer' and is 'peeved' by scientists who think the Big Bang settles origins (S2); RFH treats scripture as parable compatible with evolution (S7). No source is named that outranks observation; revelation is not ranked. Too indirect (P19)."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Not scored from working science alone (P19); no statement on the world's order as same-rules-for-all read."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "P4 test: A 2 sits between the branches and is scored only at 0.5, under the 0.7 bar; B 3 at 0.5. A needed axis is scored only at 0.5, so BELOW_THRESHOLD (§6). Deepen D1: unchanged."}
  statements:
    - text: "I believed in the spiritual power that, as a Christian, I called God. But as I grew older and learned about different faiths I came to believe that there was, after all, but One God with different names: Allah, Tao, the Creator, and so on. God, for me, was the Great Spirit in Whom \"we live and move and have our being.\""
      cites: [{source: S7, locator: "Cambridge paragraph"}]
      date: "1999"
      context: "Reason for Hope chapter 'In the Forests of Gombe', republished by Orion Magazine (S7). Retrospective: beliefs 'already moulded' by the time she reached Cambridge (early 1960s), i.e. at the start of the working years."
      axes: [A_locus]
      kind: "autobiography"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Orion attributes the essay to Jane Goodall; wording matches the RFH religion section as summarized on Wikipedia (S6). Book page images not viewed (IA borrow-restricted)."
    - text: "Since I cannot believe that this was the result of chance, I have to admit anti-chance. And so I must believe in a guiding power in the universe – in other words, I must believe in God."
      cites: [{source: S6, locator: "Religion and spirituality (RFH Notre Dame, 1977 experience)"}]
      date: "1999"
      context: "Reason for Hope, on a mystical experience at Notre Dame Cathedral (Wikipedia dates the experience 1977; inside the working years). Known here as a secondary quotation (S6); JGI 2019 re-post of the passage was not recoverable (site now serves a different index)."
      axes: [A_locus]
      kind: "autobiography"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "P26: secondary quotation; used with Orion primary text (S7) for corroboration, not alone for a lift past 0.5."
    - text: "What that intelligence behind the universe is — what it is, who it is; probably what it is — I haven’t the faintest idea, but I’m absolutely sure that there is something. And seeking for that something is part of being human."
      cites: [{source: S2, locator: "closing exchange"}]
      date: "2020"
      context: "On Being with Krista Tippett, recorded over Zoom from Bournemouth in 2020 (original air date 6 August 2020); her closing answer on what it means to be human, straight after she reports that 'all of these great brains have said there is no way that what’s happened is just chance' (reported, after Francis Collins; not her own argument)."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-18
      note: "The producer's own transcript on onbeing.org (official site of the producing institution)."
    - text: "And that’s where I felt that deep, spiritual connection to the natural world, and also came to understand the interconnectedness of all living things in this tapestry of life where each species, no matter how insignificant, plays a probably vital role in the whole pattern."
      cites: [{source: S2, locator: "1986 exchange"}]
      date: "2020"
      context: "Same interview (2020), looking back on the years up to 1986; on her years in the rainforest before the 1986 Chicago conference. A retrospective self-report about the working years."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-18
      note: ""
    - text: "I don’t have any idea of who or what God is. But I do believe in some great spiritual power. I feel it particularly when I’m out in nature. It’s just something that’s bigger and stronger than what I am or what anybody is. I feel it. And it’s enough for me."
      cites: [{source: S6, locator: "Religion and spirituality (Reader's Digest, September 2010, p. 128)"}]
      date: "2010-09"
      context: "Reader's Digest Q&A (September 2010), as quoted by Wikipedia. Hedge on form; affirms spiritual power felt in nature."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Print issue not opened; wording taken from Wikipedia's citation of Reader's Digest."
    - text: "I suppose so; I was raised as a Christian."
      cites: [{source: S3, locator: "Christian paragraph"}]
      date: "2010"
      context: "The Guardian, Stephen Moss, 13 January 2010; asked whether she is still a Christian. Context only (nominal_affiliations)."
      axes: []
      kind: "recorded interview"
      verified_against: "newspaper interview"
      verified_on: 2026-10-18
      note: "Quoted in the interviewer's article, read on the publisher's site."
    - text: "Lost in awe at the beauty around me, I must have slipped into a state of heightened awareness. … It seemed to me, as I struggled afterward to recall the experience, that self was utterly absent: I and the chimpanzees, the earth and trees and air, seemed to merge, to become one with the spirit power of life itself."
      cites: [{source: S7, locator: "May 1981 Gombe storm / outsight"}]
      date: "1999"
      context: "RFH / Orion: dated May 1981 at Gombe (inside the working years), narrated in 1999. Mystical merge with spirit power of life."
      axes: [A_locus]
      kind: "autobiography"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Ellipsis marks omitted middle sentences about sensory detail; merge sentence verified in Orion text."
  changes_over_life:
    - {value: "Brief rejection / denial of God after second husband Derek Bryceson's death (1980), then return to belief via the forest at Gombe (S7); not a lasting change of system for the span", year: 1980, certainty: 0.5, cites: [{source: S7, locator: "Derek / forest healing paragraphs"}], how_known: "RFH via Orion; P31 — rare waver, then return; lasting contributions span 1964–1986."}
    - {value: "1986: from field science to conservation advocacy after the Chicago conference (her 'Road to Damascus moment' in the interviewer's words); not a documented change of religious view", year: 1986, certainty: 0.7, cites: [{source: S2, locator: "1986 exchange"}], how_known: "(interview) Her account (S2); off-point for A–E."}
  coder_notes: "Coder's call throughout. Deepen D1 recovered RFH own-voice (Orion S7 + Wikipedia secondary quotations S6) and moved primary BELOW → PANENT @0.5. A and B certainties stay 0.5 under P20/P1 (post-span) and P35 (B); hedges on God's form keep A from 0.7. Chart fill hollow→filled via A corroboration; darkness unchanged (min(A,B)=0.5). Full Reason for Hope book and Africa In My Blood / Beyond Innocence letters remain leads."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "English", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica ('British')."}
  religious_heritage_by_birth: {value: "Congregationalist family", certainty: 0.7, cites: [{source: S2, locator: "childhood exchange"}, {source: S3, locator: "Christian paragraph"}], how_known: "(interview) Two interviews."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1964–1986", certainty: 0.5, cites: [{source: S4, locator: "article page"}, {source: S1, locator: "books paragraph"}], how_known: "Nature paper (1964) to The Chimpanzees of Gombe (1986), first to last listed lasting contribution (P29, P30). Start might be 1962 or 1963 (see first_lasting_contribution_year)."}
  age_at_first_lasting_contribution: {value: 30, certainty: 0.5, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "article page"}], how_known: "1964 − 1934 = 30 (P30); 28 or 29 under the alternatives."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No statement of hers is scored at 3 or 4 (A 2; B 3 is inferred from working science, so not an LIO-type view, P27)."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S2, locator: "closing exchange"}, {source: S7, locator: "Cambridge / Great Spirit"}], how_known: "A 2 is mixed, not LIO-pole."}
  worldview_during_major_work: {value: "PANENT-leaning spiritual theism already moulded by Cambridge (early 1960s), with a brief waver after 1980 (S7); scored only at 0.5 (post-span narration)", certainty: 0.5, cites: [{source: S7, locator: "Cambridge paragraph; Derek paragraphs"}], how_known: "RFH retrospective (S7)."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Field naturalist; no definition-to-consequence work read.", certainty: 0.5, cites: [{source: S1, locator: "findings paragraph"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "early-life paragraph"}], how_known: "Not read."}
  circle_present: {value: "no", rationale: "A Great Spirit / Creator that includes the world (panentheist) but is not identified with Nature as a whole (PANT do_not_use).", certainty: 0.5, cites: [{source: S7, locator: "Great Spirit paragraph"}], how_known: "Coder's reading of RFH via Orion."}
  reading: "A field scientist whose working-years beliefs (by her later account) were already a Christian-rooted, multi-name panentheism; science and religion held as compatible windows. Lane B only."
  notes: ""

institutions:
  - {value: "Gombe Stream Game Reserve camp (now Gombe Stream National Park), Tanzania", role: "founder of the research camp", years: "1960–", kind: "research institute", certainty: 0.7, cites: [{source: S1, locator: "camp paragraph"}, {source: S6, locator: "Research at Gombe"}], how_known: "Britannica and Wikipedia."}
  - {value: "University of Cambridge", role: "Ph.D. in ethology", years: "–1965", kind: university, certainty: 0.7, cites: [{source: S1, locator: "Ph.D. paragraph"}, {source: S4, locator: "affiliation"}, {source: S6, locator: "Education (thesis 1966)"}], how_known: "Britannica; Nature lists her at Madingley; Wikipedia dates the thesis 1966."}
  - {value: "Jane Goodall Institute", role: founder, years: "1977–", kind: other, certainty: 0.7, cites: [{source: S6, locator: "Jane Goodall Institute"}, {source: S2, locator: "guest note"}], how_known: "Wikipedia dates founding 1977; On Being guest note."}
collaborators:
  - {value: "Louis Leakey", relation: "mentor or employer", note: "she began by assisting him", certainty: 0.7, cites: [{source: S1, locator: "early-life paragraph"}, {source: S6, locator: "Africa"}], how_known: "Britannica and Wikipedia."}
  - {value: "Hugo van Lawick", relation: other, note: "photographer who filmed her work; husband 1964, later divorced", certainty: 0.7, cites: [{source: S1, locator: "camp paragraph"}, {source: S6, locator: "Personal life"}], how_known: "Britannica and Wikipedia."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S5, locator: "roster.csv, rank 107"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Britannica article is unsigned (Britannica Editors); read live; Top Questions box not used."
    - "Reason for Hope (1999) not read as a bound book (IA borrow-restricted / 403 on djvu.txt); worldview lifts rest on Orion Magazine republication of one RFH chapter (S7), NYT Books ch.1 excerpt (S8), and Wikipedia secondary quotations (S6)."
    - "Every scored worldview certainty remains at 0.5 under P20/P1 (post-span narration) despite stronger own-voice."
    - "Death place: Wikipedia Beverly Hills vs Britannica Los Angeles — Beverly Hills adopted as more specific at 0.7."
  open_questions:
    - "Read the full Reason for Hope (1999) page-by-page (Notre Dame chapter, Cambridge, Gombe outsight) against a library or purchased copy."
    - "Read Africa In My Blood / Beyond Innocence (letters) for any in-span religion statements."
    - "Read her 1962 and 1963 papers to fix the first-lasting year."
    - "Open Reader's Digest September 2010 in print (currently secondary quotation via S6)."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "Britannica Editors. \"Jane Goodall.\" Encyclopaedia Britannica (revised 27 September 2026). https://www.britannica.com/biography/Jane-Goodall. Read live 2026-10-18; re-checked 2026-10-24."
    url: "https://www.britannica.com/biography/Jane-Goodall"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Unsigned article. Body and Quick Facts only; the AI-generated Top Questions are not cited."
    used_for: [identity, basics, contribution, childhood, heritage, timing, institutions, collaborators, lane_b]
  - id: S2
    type: primary
    kind: other
    author: "Jane Goodall, with Krista Tippett"
    citation: "Tippett, Krista. \"Jane Goodall, in Memoriam — What It Means to Be Human.\" On Being (The On Being Project); conversation recorded over Zoom in 2020, original air date 6 August 2020; transcript on the programme page. https://onbeing.org/programs/jane-goodall-what-it-means-to-be-human/"
    url: "https://onbeing.org/programs/jane-goodall-what-it-means-to-be-human/"
    accessed: 2026-10-18
    source_quality: "primary / own words"
    reliability_note: "Producer's transcript of a recorded conversation; her first-person words (P8). An editor's note in the transcript corrects one of her remarks (on Francis Collins)."
    used_for: [worldview, childhood, heritage, institutions, timing, lane_b]
  - id: S3
    type: primary
    kind: other
    author: "Stephen Moss"
    citation: "Moss, Stephen. \"Jane Goodall: 'My job is to give people hope'.\" The Guardian, 13 January 2010 (online 12 January 2010, 19.05 EST). https://www.theguardian.com/science/2010/jan/13/jane-goodall"
    url: "https://www.theguardian.com/science/2010/jan/13/jane-goodall"
    accessed: 2026-10-18
    source_quality: "newspaper interview"
    reliability_note: "Interview article: her quoted words count as hers (P8); the interviewer's paraphrases do not."
    used_for: [worldview, childhood, heritage]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "Jane Goodall"
    citation: "Goodall, Jane. \"Tool-Using and Aimed Throwing in a Community of Free-Living Chimpanzees.\" Nature 201 (1964): 1264–1266; published 28 March 1964. https://www.nature.com/articles/2011264a0"
    url: "https://www.nature.com/articles/2011264a0"
    accessed: 2026-10-18
    source_quality: "primary / own words"
    reliability_note: "Publisher's article page (title, date, affiliation, reference list); the article text is paywalled and was not read."
    used_for: [basics, contribution, timing, institutions, worldview]
  - id: S5
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-18
    source_quality: "study roster"
    reliability_note: "Study's own roster."
    used_for: [identity, review]
  - id: S6
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia contributors. \"Jane Goodall.\" Wikipedia, The Free Encyclopedia. Religion and spirituality section cites Reason for Hope (Notre Dame; Cambridge moulding), Reader's Digest September 2010 p. 128, Guardian 2010, and Laszlo 2017 foreword. https://en.wikipedia.org/wiki/Jane_Goodall. Read live 2026-10-24."
    url: "https://en.wikipedia.org/wiki/Jane_Goodall"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Dual bio with Britannica (P50). Religion quotations used as secondary quotation (P26) unless matched in Orion (S7). Death place Beverly Hills vs Britannica Los Angeles noted."
    used_for: [identity, basics, contribution, childhood, worldview, institutions, collaborators, review]
  - id: S7
    type: primary
    kind: "published work by the subject"
    author: "Jane Goodall"
    citation: "Goodall, Jane. \"In the Forests of Gombe.\" Orion Magazine (online republication of the Reason for Hope chapter; page dated 6 October 2025 in the fetch). https://orionmagazine.org/article/jane-goodall-legacy-chimpanzees-in-the-forests-of-gombe/. Read live 2026-10-24."
    url: "https://orionmagazine.org/article/jane-goodall-legacy-chimpanzees-in-the-forests-of-gombe/"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "Magazine republication of her RFH chapter in her own name. Unofficial web copy of a published primary text for ceiling purposes (§7 / P21): worldview fields that rest only on this copy stay ≤0.7; P20/P1 already caps post-span at 0.5. Book page images not viewed."
    used_for: [worldview, timing, lane_b]
  - id: S8
    type: primary
    kind: "published work by the subject"
    author: "Jane Goodall, with Phillip Berman"
    citation: "Goodall, Jane, with Phillip Berman. Reason for Hope: A Spiritual Journey. New York: Warner Books, 1999. Chapter One ('Beginnings') excerpt on The New York Times Books site. https://archive.nytimes.com/www.nytimes.com/books/first/g/goodall-hope.html. Read live 2026-10-24."
    url: "https://archive.nytimes.com/www.nytimes.com/books/first/g/goodall-hope.html"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "Publisher-hosted first-chapter excerpt (NYT Books). Confirms RFH voice and framing (mind that can contemplate God; evolution vs destiny); the Notre Dame / Great Spirit passages are not in this excerpt — those rest on S7 and S6."
    used_for: [worldview]
---

# Jane Goodall

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Jane Goodall (1934–2025), British ethologist of the Gombe chimpanzees [S1, S6]. Deepen D1: primary_system PANENT at 0.5 (RFH own-voice via Orion); A 2 at 0.5 support corroborated; B 3 at 0.5 (P35); mid_basin BELOW_THRESHOLD. Plotted faded filled.

## Life and work

London, Gombe (from 1960), Cambridge Ph.D. (thesis 1966) [S1, S6].

## Contribution and impact

Tool use (Nature, 1964) [S4]; In the Shadow of Man (1971); The Chimpanzees of Gombe (1986) [S1, S6].

## Childhood and education

Grandfather a Congregational minister [S2]; left school at 18; Cambridge Ph.D. without a bachelor's [S1, S6].

## Adult working worldview

RFH / Orion: 'Great Spirit in Whom we live and move and have our being'; beliefs moulded before Cambridge [S7]. Notre Dame: 'I must believe in a guiding power… in God' [S6]. Hedge: 'I haven’t the faintest idea' what that intelligence is [S2]; 'don’t have any idea of who or what God is' [S6].

## Heritage (context only)

Congregationalist family [S2, S3, S6].

## Timing

1964–1986, from age 30 [S1, S4].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No circle (PANENT, not PANT) [S7].

## Open questions

- Read full Reason for Hope (1999) against a library copy.
- Read Africa In My Blood / Beyond Innocence letters.

## Research log

- 2026-10-18: Read Britannica (live), the On Being transcript, The Guardian interview and Nature's article page. Reason for Hope lending-only on the Internet Archive.
- 2026-10-24 (deepen D1): Dual bio Wikipedia EN (S6). Orion RFH chapter (S7). NYT Books RFH ch.1 (S8). Wikipedia religion quotations (Notre Dame, Reader's Digest, Laszlo). IA RFH still blocked. primary BELOW → PANENT @0.5; A support single → corroborated; B unchanged P35. Chart fill hollow → filled; still faded.
