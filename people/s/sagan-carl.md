---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch O)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-17
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-17, by: "Grok Bot", summary: "Record created (stage 3 batch O, order P32: F 4, rank 88). Basics from Britannica (Helge Kragh, signed; body only). Worldview from the 1981 U.S. Catholic interview ('God and Carl Sagan', 1 May 1981), read on the U.S. Catholic site. Scientist (P30: planetary atmospheres, nuclear winter). primary_system AGNOS (0.5, alt SECHUM); A BELOW_THRESHOLD (agnostic, no locus view, P20); B 3 (0.5, alt 4; P35); D 4 (0.5); mid_basin BELOW_THRESHOLD. Not plotted. Draft, not reviewed."}
    - {date: 2026-10-17, by: "Grok Bot", summary: "Batch O audit: A BELOW_THRESHOLD now also cites P38 (explicit suspension with no stated disbelief). Value unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #87, F4 rank 88). Needs: keep A honest unless clear place/deny (Pale Blue Dot, Demon-Haunted World, Cosmos, Ted interviews); corroborate/lift B if nature-order statements exist. Re-read U.S. Catholic 1981 (S2) full; Cosmos Ep.3 'Harmony of the Worlds' via Wikiquote transcript (S5); U.S. News 1991 'Scientists & Their Gods' quote via Wikiquote (S6, secondary); DHW IA djvu OCR (S7) — laws of Nature not absolutely certain / may break down in new circumstances, PLUS same electromagnetism laws ten billion light years away / 'different laws in every province, but we do not'; Wikipedia EN Naturalism + Early life (S4, P50 dual-bio: Reform Jewish parents Samuel/Rachel; 1996 self-label agnostic). Varieties (Gifford 1985 / 2006) borrow-locked on IA — Protagoras / full lecture text unread (blocker). A stays BELOW_THRESHOLD (P20/P38): consistent AGNOS across 1981+1996; 'does not exclude' traditional god; no clear place or deny of locus. Named A alt 4 only if 'ludicrous'/'no compelling evidence for anthropomorphic patriarch' is over-read as deny of personal intervening God (rejected: he refuses atheist certainty and keeps exclusion open). B 3 @0.5 alt 4: basis inference_from_work → written_profession; support single → corroborated (P48) via S2+S5+S7 own-voice lawful nature without exceptionless claim (P16 addendum; DHW hedge blocks B 4 / P40). E UNKNOWN → 4 @0.7 corroborated (S5+S7; same rules Earth/skies and across cosmic distance). D unchanged 4 @0.5. primary_system AGNOS @0.5 alt SECHUM unchanged (SECHUM remains definitional/semantic alt from God=laws conditional, not self-membership). mid_basin stays BELOW_THRESHOLD (A BELOW). P47 source_quality on S1–S7. Chart-moving NO (still not plotted: A BELOW). No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: sagan-carl
  display_name: "Carl Sagan"
  roster:
    canonical_name: "Carl Sagan"
    rank: 88
    F: 4
    models: [Claude, DeepSeek, GPT, Grok]
    band: "core (3–4)"
    status: core
    field: astronomy
    field_bucket: astronomy
  full_name: {value: "Carl Edward Sagan", certainty: 0.7, cites: [{source: S4, locator: "lede / infobox"}, {source: S1, locator: "opening"}], how_known: "Wikipedia EN gives Carl Edward Sagan; Britannica opening 'Carl Sagan' without middle name."}
  native_name: {value: UNKNOWN, how_known: "English."}
  aliases:
    - {name: "Carl-Sagan", kind: "roster alias"}

basics:
  birth:
    date: {value: "1934-11-09", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Brooklyn, New York, U.S.", modern_name: "Brooklyn, New York, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "1996-12-20", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Seattle, Washington", modern_name: "Seattle, Washington, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1977, certainty: 0.5, cites: [{source: S1, locator: "awards paragraph"}], how_known: "The Dragons of Eden, Pulitzer Prize for nonfiction 1978 (S1); 1977 is its publication year, not given in S1 (coder's inference from the 1978 prize; may be earlier). His research on planetary atmospheres is undated in the body (P39). The Cosmic Connection (1973) 'earned him prominence' but is not marked as lasting. Coder's pick (P13)."}
  era_bucket: {value: "1950 on", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "From 1977 (P2); every candidate year (1973–1983) gives the same bucket."}
  region_of_birth: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "United States (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Berkeley, Harvard, Cornell."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [English], certainty: 0.7, cites: [{source: S1, locator: "titles"}], how_known: "Britannica."}
  occupations: {value: ["astronomer", "science writer", "professor"], certainty: 0.7, cites: [{source: S1, locator: "opening; Cornell paragraph"}], how_known: "Britannica."}

contribution:
  fields: {value: ["planetary science", "astrobiology", "science popularization"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Research on planetary atmospheres (Venus, Jupiter) and prebiotic synthesis of amino and nucleic acids", year: UNKNOWN, kind: theory, lasting: "'Sagan did important research on planetary atmospheres, in astrobiology, and on the origin of life on Earth' (S1)", certainty: 0.7, cites: [{source: S1, locator: "early work paragraph; reputation paragraph"}], how_known: "Britannica; undated. A theory or result about natural systems, so he is a scientist (P30)."}
    - {value: "The Dragons of Eden", year: 1977, kind: work, lasting: "Pulitzer Prize for nonfiction, 1978 (S1)", certainty: 0.5, cites: [{source: S1, locator: "awards paragraph"}], how_known: "Britannica gives the prize year; the publication year is the coder's inference."}
    - {value: "Cosmos (television series and book, with Ann Druyan)", year: 1980, kind: work, lasting: "'the height of his public fame'; the book 'became a best seller' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Planetary Society paragraph"}], how_known: "Britannica."}
    - {value: "Nuclear winter (co-author of the paper introducing the concept)", year: 1983, kind: "concept or term", lasting: "'introduced the concept of \"nuclear winter\"' (S1)", certainty: 0.7, cites: [{source: S1, locator: "political paragraph"}], how_known: "Britannica."}
    - {value: "The Demon-Haunted World", year: 1996, kind: work, lasting: "'his last major book' (S1)", certainty: 0.5, cites: [{source: S1, locator: "pseudoscience paragraph"}], how_known: "Britannica; lasting status is the coder's reading; closes the period."}
  evidence_of_impact:
    - {value: "Pulitzer Prize (1978), NASA Distinguished Public Service Medal (1977, 1981), Ørsted Medal (1990), NAS Public Welfare Medal (1994)", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "awards paragraph"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "arguable", rationale: "Britannica says 'he made his reputation primarily as a spokesman for science and a popularizer of astronomy' (S1), though his research is called important.", certainty: 0.5, cites: [{source: S1, locator: "reputation paragraph"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Reform Judaism", certainty: 0.7, cites: [{source: S4, locator: "Early life"}], how_known: "Wikipedia EN: he later described his family as Reform Jews; mother 'definitely believed in God' and was active in the temple; father not especially religious (P50 dual-bio)."}
  family_religious_practice: {value: "Mother active in temple / kosher meat; father not especially religious", certainty: 0.5, cites: [{source: S4, locator: "Early life"}], how_known: "Wikipedia EN paraphrase of family recollection."}
  parents_and_household:
    - {value: "Rachel Molly Gruber (mother); Samuel Sagan (father, Ukrainian-born garment worker)", certainty: 0.7, cites: [{source: S4, locator: "Early life"}], how_known: "Wikipedia EN (P50)."}
  household_circumstances: {value: "Modest apartment in Bensonhurst, Brooklyn; Depression-era (father worked as movie-theater usher in worst years)", certainty: 0.5, cites: [{source: S4, locator: "Early life"}], how_known: "Wikipedia EN."}
  schooling:
    - {value: "University of Chicago (B.A., M.A. physics 1955–56; Ph.D. astronomy and astrophysics 1960)", stage: university, years: "–1960", certainty: 0.7, cites: [{source: S1, locator: "education paragraph"}], how_known: "Britannica."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [English], certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1977–1996", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "'In my view, they nearly don't communicate at all'; science has 'a fair amount to say to religion mainly about the nature of evidence'", certainty: 0.7, cites: [{source: S2, locator: "science and religion exchange"}], how_known: "(interview) His own words (P8)."}
  primary_system:
    value: AGNOS
    basis: recorded_interview
    certainty: 0.5
    cites: [{source: S2, locator: "God and 'first cause' exchanges"}, {source: S4, locator: "Naturalism / 1996 agnostic reply"}, {source: S1, locator: "religion sentence"}]
    rationale: "1981 (S2): 'An atheist is someone who is certain that God does not exist ... I know of no such compelling evidence'; 'I am extremely uncomfortable with dogmatic atheists ... I'm also uncomfortable with dogmatic believers'; 'If we don't know the answer, why are we under so much pressure to make up our minds'. Wikipedia (S4): in 1996 he said he was agnostic. Britannica: 'he denied that he was an atheist'. Named alternative SECHUM: conditional God=laws wording (S2 Spinoza/Einstein contrast; S6 U.S. News 1991 'if by God one means the set of physical laws... clearly there is such a God') is definitional/semantic, not a self-claimed scientifically based religion membership."
    how_known: "(interview) Own-voice U.S. Catholic 1981 (S2) plus 1996 self-label via Wikipedia (S4). Named alternative → 0.5."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: AGNOS, reason: "Explicit suspension of judgement on God (1981 and 1996)."}
    - {code: SECHUM, reason: "Conditional God=laws wording and Britannica's 'scientifically based belief system'; no membership read."}
    - {code: ATHE, reason: "He denies being an atheist and refuses certainty that God does not exist."}
  lio_axes:
    A_locus:
      value: BELOW_THRESHOLD
      cites: [{source: S2, locator: "God / old man / does-not-exclude exchanges"}, {source: S4, locator: "Naturalism / 1996 agnostic"}, {source: S6, locator: "U.S. News 1991 ludicrous / physical-laws God"}]
      how_known: "Deepen D1. Consistent AGNOS without a stated locus (P20) and explicit suspension with no stated disbelief (P38). 1981: no compelling evidence for 'the old man in the sky', yet 'a universe that does not exclude a traditional Western or Eastern god, but that does not require one either' (S2). 1996: self-label agnostic (S4). U.S. News 1991 (S6, secondary): anthropomorphic sparrow-tallying God is 'ludicrous', but that is paired with the conditional physical-laws God and does not place or deny a locus for a traditional deity he still refuses to rule out. Named alternative 4: only if the 'ludicrous' / no-evidence-for-anthropomorphic-patriarch lines are over-read as a clear deny of personal intervening God — rejected for scoring (he refuses atheist certainty and keeps exclusion open)."
      note: "Named alternative 4 (deny of personal intervening God) live as a rejected over-read; A stays BELOW_THRESHOLD."
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.5
      support: corroborated
      cites: [{source: S2, locator: "laws of nature exchange"}, {source: S5, locator: "Harmony of the Worlds, ~8–10 min"}, {source: S7, locator: "Science and Hope / laws not absolutely certain; Newton's Sleep / same laws across cosmic distance"}]
      rationale: "Own-voice on physical nature (P16), not working-science default alone (P35 still available as floor). 1981 (S2): 'I can't imagine anyone denying the existence of the laws of nature'. Cosmos Ep.3 (S5): 'scientific laws pervade all of nature', 'the same rules apply on Earth as in the skies', and we live where things change 'according to patterns, rules or as we call them, laws of nature'. DHW (S7): 'a handful of comparatively simple laws' predict phenomena 'through the entire Universe'; order of the Universe is 'an observed fact'. Explicit lawful order without a no-exception claim → B 3 at 0.5, alternative 4 (P16 addendum). DHW also hedges: 'even laws of Nature are not absolutely certain' and 'may... break down' in never-examined circumstances (black holes, inside the electron, near light speed) → blocks B 4 (P40 necessity without exceptions). Working science (P35) remains consistent floor."
      how_known: "Own published/broadcast words (S2 interview; S5 Cosmos; S7 DHW OCR). Independent source ids → corroborated (P48). Named alternative → 0.5 ceiling with alt."
      alternatives:
        - {value: 4, note: "If the DHW epistemic hedge (laws not absolutely certain / may need correction in new regimes) is read as only about knowledge of the laws, not about exceptions in nature's order — then exceptionless LIO (B 4) would fit the Cosmos/DHW universality wording. Kept as named alt; scored value stays 3.", cites: [{source: S5, locator: "Harmony of the Worlds"}, {source: S7, locator: "Newton's Sleep"}]}
    C_ledger: {value: UNKNOWN, how_known: "(interview) He would be 'delighted if there were a life after death' and calls near-death reports 'anecdotal'; nothing on reward or punishment (P19)."}
    D_authority:
      value: 4
      basis: recorded_interview
      certainty: 0.5
      cites: [{source: S2, locator: "science and religion exchange"}]
      rationale: "Evidence over authority: 'science has a fair amount to say to religion mainly about the nature of evidence. The idea of putting faith in an ancient argument from authority which is not to be questioned seems to me to have dire and dangerous implications'; 'I'm afraid religion doesn't throw away enough trust.'"
      how_known: "(interview) His own words; 0.5 because the remark mixes epistemic and political concerns. DHW skepticism of prayer/faith-healing not used to lift certainty this pass."
    E_scope:
      value: 4
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S5, locator: "Harmony of the Worlds, ~8–10 min"}, {source: S7, locator: "Newton's Sleep / quasars and same laws"}]
      rationale: "World's order (P7): same rules for every kind of being/event. Cosmos Ep.3 (S5): 'the same rules apply on Earth as in the skies'. DHW (S7): light from distant quasars detected 'only because the laws of electromagnetism are the same ten billion light years away as here'; spectra recognizable because 'the same chemical elements' and 'the same laws of quantum mechanics apply'; 'We could have lived in a Universe with different laws in every province, but we do not' — 'observed fact', not preconception. No hidden in-group exceptions stated."
      how_known: "Own broadcast + published book (S5, S7). Two independent source ids → corroborated (P48). No named alternative → 0.7."
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD, so the P4 test cannot be applied (Pavlov/James pattern)."}
  statements:
    - text: "Those who raise questions about the God hypothesis and the soul hypothesis are by no means all atheists. An atheist is someone who is certain that God does not exist, someone who has compelling evidence against the existence of God. I know of no such compelling evidence."
      cites: [{source: S2, locator: "reply to 'That seems to leave the question up in the air'"}]
      date: "1981-05-01"
      context: "Interview, U.S. Catholic, May 1981 (S2)."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
    - text: "We see a universe that does not exclude a traditional Western or Eastern god, but that does not require one either."
      cites: [{source: S2, locator: "reply to 'Where does God fit into this view?'"}]
      date: "1981-05-01"
      context: "Same interview — keeps traditional God neither required nor excluded (A stays BELOW)."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
    - text: "To others—for example, Baruch Spinoza and Albert Einstein—God is essentially the sum total of the physical laws which describe the universe. I can't imagine anyone denying the existence of the laws of nature, but I don't know of any compelling evidence for the old man in the sky."
      cites: [{source: S2, locator: "reply on what 'God' means"}]
      date: "1981-05-01"
      context: "Same interview — nature-order (B) plus suspension on anthropomorphic God (A)."
      axes: [A_locus, B_cause]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
    - text: "I also think science has a fair amount to say to religion mainly about the nature of evidence. The idea of putting faith in an ancient argument from authority which is not to be questioned seems to me to have dire and dangerous implications for politics."
      cites: [{source: S2, locator: "science and religion exchange"}]
      date: "1981-05-01"
      context: "Same interview."
      axes: [D_authority]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
    - text: "We have found that scientific laws pervade all of nature, that the same rules apply on Earth as in the skies, that we can find a resonance, a harmony, between the way we think and the way the world works… …we live in an in-between universe where things change, all right but according to patterns, rules or as we call them, laws of nature."
      cites: [{source: S5, locator: "Harmony of the Worlds, ~8 min 45 sec and ~9 min 51 sec"}]
      date: "1980"
      context: "Cosmos: A Personal Voyage, Episode 3 'The Harmony of the Worlds' (S5 Wikiquote transcript with timestamps)."
      axes: [B_cause, E_scope]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Broadcast words; Wikiquote transcript, not studio script page images."
    - text: "The order of the Universe is not an assumption; it's an observed fact. We detect the light from distant quasars only because the laws of electromagnetism are the same ten billion light years away as here. … We could have lived in a Universe with different laws in every province, but we do not."
      cites: [{source: S7, locator: "Newton's Sleep chapter"}]
      date: "1995"
      context: "The Demon-Haunted World (S7 IA djvu OCR)."
      axes: [B_cause, E_scope]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
    - text: "But even laws of Nature are not absolutely certain. There may be new circumstances never before examined — inside black holes, say, or within the electron, or close to the speed of light — where even our vaunted laws of Nature break down and, however valid they may be in ordinary circumstances, need correction."
      cites: [{source: S7, locator: "Science and Hope chapter"}]
      date: "1995"
      context: "Same book — epistemic hedge that blocks scoring B 4 (P40)."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
    - text: "The idea that God is an oversized white male with a flowing beard who sits in the sky and tallies the fall of every sparrow is ludicrous. But if by God one means the set of physical laws that govern the universe, then clearly there is such a God. This God is emotionally unsatisfying... it does not make much sense to pray to the law of gravity."
      cites: [{source: S6, locator: "Scientists & Their Gods, U.S. News & World Report Vol. 111 (1991)"}]
      date: "1991"
      context: "As quoted in U.S. News & World Report (S6 via Wikiquote). Parallel to the 1981 Spinoza/Einstein contrast; supports SECHUM as named primary_system alt and B nature-order; does not clear A (paired with emotional unsatisfying / no prayer)."
      axes: [A_locus, B_cause]
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Original U.S. News pages unread (P26); wording matches the 1981 U.S. Catholic contrast closely enough to use as secondary support only."
  changes_over_life: []
  coder_notes: "Deepen D1: A kept BELOW_THRESHOLD on purpose — 1981 does-not-exclude + 1996 agnostic + refusal of atheist certainty outweigh 'ludicrous' anthropomorphic-God rhetoric. B lifted in basis/support only (still 3 @0.5 alt 4); DHW 'laws not absolutely certain' blocks B 4. E newly scored 4 @0.7 from Cosmos Ep.3 + DHW universality. Varieties of Scientific Experience (Gifford 1985 / Druyan 2006) still unread (IA borrow-locked); Ted Turner interview thin/unrecovered. Chart still not plotted."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "American (Jewish family; father Ukrainian-born)", certainty: 0.7, cites: [{source: S4, locator: "Early life"}, {source: S1, locator: "opening"}], how_known: "Wikipedia EN parents; Britannica American."}
  religious_heritage_by_birth: {value: "Reform Judaism", certainty: 0.7, cites: [{source: S4, locator: "Early life"}], how_known: "As family_religion (P50)."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1977–1996", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "First to last dated listed lasting contribution (P29, P30)."}
  age_at_first_lasting_contribution: {value: 43, certainty: 0.5, cites: [{source: S1, locator: "opening; 1977"}], how_known: "1977 − 1934 = 43 (P30)."}
  first_evidence_of_lio_type_views: {value: "1981: agnostic on God; lawful nature; evidence over authority", year: 1981, certainty: 0.5, cites: [{source: S2, locator: "interview"}], how_known: "Cosmos 1980 (S5) is earlier on B/E; 1981 remains first clear A/D evidence in sources read (P30 #7)."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.5, cites: [{source: S2, locator: "interview"}, {source: S5, locator: "1980"}, {source: S7, locator: "1995"}], how_known: "1980–1995 inside 1977–1996."}
  worldview_during_major_work: {value: "Agnostic on God; lawful universal nature; evidence over authority", certainty: 0.5, cites: [{source: S2, locator: "interview"}, {source: S5, locator: "Harmony"}, {source: S7, locator: "DHW"}], how_known: "Coder's summary from D1 sources."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Not read for this.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Not read."}
  circle_present: {value: "unclear", rationale: "Agnostic; awe at lawful cosmos is Lane B color, not a scored circle claim.", certainty: 0.5, cites: [{source: S2, locator: "interview"}, {source: S7, locator: "Newton's Sleep awe"}], how_known: "Coder's reading."}
  reading: "Agnostic; awe at a lawful cosmos; evidence over authority."
  notes: "Lane B only. SECHUM-style God=laws is a labeled semantic alternative, not a finding that he belonged to a scientifically based religion."

institutions:
  - {value: "Harvard University and Smithsonian Astrophysical Observatory", role: "researcher", years: "1962–1968", kind: university, certainty: 0.7, cites: [{source: S1, locator: "education paragraph"}], how_known: "Britannica."}
  - {value: "Cornell University (Laboratory for Planetary Studies)", role: "director; professor", years: "1968–1996", kind: university, certainty: 0.7, cites: [{source: S1, locator: "Cornell paragraph"}], how_known: "Britannica."}
  - {value: "The Planetary Society", role: "co-founder", years: "1980–", kind: other, certainty: 0.7, cites: [{source: S1, locator: "Planetary Society paragraph"}], how_known: "Britannica."}
collaborators:
  - {value: "Ann Druyan", relation: family, note: "wife; co-writer of Cosmos", certainty: 0.7, cites: [{source: S1, locator: "Planetary Society paragraph"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 88"}], how_known: "Study roster."}
  controversies:
    - {value: "Critics called his arguments against traditional religion simplistic", certainty: 0.7, cites: [{source: S1, locator: "religion sentence"}], how_known: "Britannica."}
  data_quality_flags:
    - "U.S. News 1991 quote only via Wikiquote secondary quotation; original magazine pages unread."
    - "Cosmos Ep.3 via Wikiquote timestamped transcript, not studio script or episode page images."
    - "DHW read as Internet Archive djvu OCR only."
    - "Varieties of Scientific Experience (Gifford 1985 / 2006) unread — IA item borrow-locked this pass."
  open_questions:
    - "Read The Varieties of Scientific Experience (Penguin 2006 / Gifford 1985) for Protagoras / 'no means of knowing' and any tighter A or B wording."
    - "Recover Ted Turner / Charlie Rose interview page images for the 1996 agnostic self-label (now only via Wikipedia)."
    - "Optional: Pale Blue Dot (1994) for any A place/deny (unlikely)."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Helge Kragh"
    citation: "Kragh, Helge. \"Carl Sagan.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Carl-Sagan. Read in Wayback snapshot 20261004211412; re-checked 2026-10-24."
    url: "https://www.britannica.com/biography/Carl-Sagan"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Signed article. Body only; Top Questions not cited."
    used_for: [identity, basics, contribution, childhood, worldview, timing, institutions, collaborators, review]
  - id: S2
    type: primary
    kind: other
    author: "Carl Sagan (interviewed by U.S. Catholic)"
    citation: "\"God and Carl Sagan: Is the cosmos big enough for both of them?\" A U.S. Catholic interview, published 1 May 1981. https://uscatholic.org/articles/198105/god-and-carl-sagan-is-the-cosmos-big-enough-for-both-of-them/ Re-read in full 2026-10-24."
    url: "https://uscatholic.org/articles/198105/god-and-carl-sagan-is-the-cosmos-big-enough-for-both-of-them/"
    accessed: 2026-10-24
    source_quality: "newspaper interview"
    reliability_note: "The publisher's own archive text of a question-and-answer interview, read directly (P8). Interviewer not named on the page (Edward Wakin per secondary attributions)."
    used_for: [worldview, timing, lane_b]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-17
    source_quality: "study roster"
    reliability_note: "Study's own roster."
    used_for: [identity, review]
  - id: S4
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia. \"Carl Sagan.\" https://en.wikipedia.org/wiki/Carl_Sagan Read 2026-10-24 (P50 dual-bio with Britannica): Early life (parents Samuel Sagan / Rachel Molly Gruber; Reform Jewish family); Naturalism (1981 God-definition paraphrase; 1996 agnostic self-label; Dorion on Spinoza/Einstein God — family report, not used to score)."
    url: "https://en.wikipedia.org/wiki/Carl_Sagan"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Used for identity/parents/heritage and the 1996 agnostic reply pointer; worldview axis scores do not rest on Wikipedia alone."
    used_for: [identity, basics, childhood, heritage, worldview]
  - id: S5
    type: primary
    kind: "published work by the subject"
    author: "Carl Sagan"
    citation: "Sagan, Carl. Cosmos: A Personal Voyage, Episode 3 \"The Harmony of the Worlds\" (1980). Timestamped quotations as collected on Wikiquote \"Carl Sagan\" (Harmony section, ~8:45 and ~9:51). https://en.wikiquote.org/wiki/Carl_Sagan Read 2026-10-24."
    url: "https://en.wikiquote.org/wiki/Carl_Sagan"
    accessed: 2026-10-24
    source_quality: "unofficial web copy"
    reliability_note: "Wikiquote transcript of broadcast words with minute marks; not studio script or episode video check this pass."
    used_for: [worldview, timing]
  - id: S6
    type: secondary
    kind: other
    author: "Carl Sagan (as quoted in U.S. News & World Report)"
    citation: "Sagan, Carl. As quoted in \"Scientists & Their Gods,\" U.S. News & World Report Vol. 111 (1991), via Wikiquote \"Carl Sagan\" (ludicrous / physical-laws God passage). https://en.wikiquote.org/wiki/Carl_Sagan Read 2026-10-24."
    url: "https://en.wikiquote.org/wiki/Carl_Sagan"
    accessed: 2026-10-24
    source_quality: "other"
    reliability_note: "Secondary quotation only; original U.S. News pages unread (P26). Parallel to the 1981 U.S. Catholic contrast (S2); used as support, not sole locus."
    used_for: [worldview]
  - id: S7
    type: primary
    kind: "published work by the subject"
    author: "Carl Sagan"
    citation: "Sagan, Carl. The Demon-Haunted World: Science as a Candle in the Dark (1995/1996). Internet Archive djvu full text: https://ia803209.us.archive.org/0/items/DemonHauntedWorld_carlSagan/Sagan_-_The_Demon-Haunted_World___Science_as_a_candle_in_the_dark_djvu.txt Read 2026-10-24 for Science and Hope (laws not absolutely certain) and Newton's Sleep (same laws across cosmic distance)."
    url: "https://archive.org/details/DemonHauntedWorld_carlSagan"
    accessed: 2026-10-24
    source_quality: "archive scan (OCR only)"
    reliability_note: "OCR of a library scan; page images not viewed. Chapter headings visible in OCR (Science and Hope; Newton's Sleep)."
    used_for: [worldview, timing]
---

# Carl Sagan

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Carl Sagan (1934–1996), American astronomer and science writer [S1]. Deepen D1: primary_system AGNOS (0.5, alt SECHUM); A BELOW_THRESHOLD (agnostic, no locus; P20/P38); B 3 at 0.5 corroborated alt 4 (own-voice nature-order; DHW hedge blocks 4); D 4 at 0.5; E 4 at 0.7 corroborated; mid_basin BELOW_THRESHOLD. Not plotted.

## Life and work

Chicago PhD 1960; Harvard, then Cornell from 1968 [S1]. Reform Jewish family (parents Samuel Sagan, Rachel Molly Gruber) [S4].

## Contribution and impact

Planetary atmospheres, Cosmos (1980), nuclear winter (1983), Demon-Haunted World (1995/96) [S1].

## Childhood and education

Reform Jewish household in Bensonhurst; Chicago degrees through PhD 1960 [S4, S1].

## Adult working worldview

Agnostic on God (1981 interview; 1996 self-label) with no clear locus place or deny [S2, S4]. Own-voice lawful universal nature (Cosmos Ep.3; DHW) without exceptionless claim [S5, S7]. Evidence over authority [S2].

## Heritage (context only)

American; Reform Jewish by birth [S4, S1].

## Timing

First lasting contribution 1977, at 43 [S1]. LIO-type evidence during major work (1980–1995).

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Agnostic; awe at a lawful cosmos [S2, S7]. God=laws is a semantic alternative, not membership.

## Open questions

- Varieties of Scientific Experience (Gifford 1985 / 2006) for Protagoras / tighter A–B wording.
- Charlie Rose / Ted Turner page images for the 1996 agnostic self-label.
- Optional Pale Blue Dot (1994) for any A place/deny.

## Research log

- 2026-10-17: Read Britannica (Kragh, Wayback 20261004211412) and the 1981 U.S. Catholic interview directly.
- 2026-10-24 (D1): Re-read U.S. Catholic full; Cosmos Ep.3 via Wikiquote; U.S. News 1991 via Wikiquote; DHW IA djvu OCR (Science and Hope; Newton's Sleep); Wikipedia EN Early life + Naturalism (P50). Varieties IA borrow-locked. No fallacy_catalog. Figures not touched.
