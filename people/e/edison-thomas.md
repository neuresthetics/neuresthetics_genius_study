---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 4
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch L; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to invention. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-25, by: "Grok Bot", summary: "Perpetual deepen: religious_heritage_by_birth / baptism / catechism / family_religion TODO→UNKNOWN after Wikipedia Religion section + Early life re-read (no childhood denomination). Chart-moving NO."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch L, order P32: F 5, rank 76). Basics from Britannica (Robert E. Conot), signed body through the Newark years; Top Questions not cited. Worldview from Edward Marshall's interview, 'No Immortality of the Soul', New York Times, 2 October 1910 (transcript on sundaymagazine.org; NYT archive abstract; Edison Papers bibliography). primary_system BELOW_THRESHOLD; A BELOW_THRESHOLD; B 4 (0.5, alt 3; interview, partly the interviewer's paraphrase); mid_basin BELOW_THRESHOLD. Not plotted. Draft, not reviewed."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Audit fixes (fallacy_catalog audit of 2742382, run 1). B_cause 4 -> BELOW_THRESHOLD: the strict wording is Marshall's paraphrase (reported speech cannot score alone, §7) and he is an inventor (P33). If the full NYT p. 15 text gives a line in his own voice, B becomes 3 (0.5, alternative 4) under P41. Timing fields updated."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #75, F5 rank 76). Needs: A BELOW_THRESHOLD; B BELOW_THRESHOLD. Primaries/own words: 1885 diary (S7 ariwatch facsimile transcript) 'unchangeable laws' / Almighty who forgot this mote; NYT Marshall 1910 own-voice Nature vs gods of religions (S2/S4/S6); clarifying letter Nature = Supreme Intelligence that rules matter (S6 via Israel); Columbian Magazine Jan 1911 denial of Being throned above directing affairs (S8 secondary quotation). Dual bio Wikipedia EN (S6, P50) + Britannica (S1). P47 on S1–S11. Inventor not scientist (P33). primary_system BELOW→DEISM @0.5 (Israel freethinker/scientific deism; Paine defense; P27 revelation/theology rejected; alt PANT/ATHE). A BELOW→4 @0.5 support corroborated (Nature=God + no Being throned above; alt 1 diary deist Almighty). B BELOW→4 @0.5 support corroborated (diary unchangeable laws P40; 1910/1911 reject intervening personal God; alt 3 P41). C UNKNOWN→3 @0.5 (no personal heaven reward / immortality). D UNKNOWN→3 @0.5 (theologians' theories unprovable). mid_basin stays BELOW (A≥3 branch needs 0.7). Span 1874→1877–1910 (phonograph/lamp/Pearl Street + battery). Chart-moving YES (A&B leave BELOW; faded hollow). No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: edison-thomas
  display_name: "Thomas Edison"
  roster:
    canonical_name: "Thomas Edison"
    rank: 76
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: invention
    field_bucket: "invention / engineering"
  full_name: {value: "Thomas Alva Edison", certainty: 0.7, cites: [{source: S1, locator: "header ('In full')"}, {source: S6, locator: "infobox"}], how_known: "Britannica and Wikipedia."}
  native_name: {value: UNKNOWN, how_known: "English."}
  aliases:
    - {name: "Wizard of Menlo Park", kind: other}

basics:
  birth:
    date: {value: "1847-02-11", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "infobox"}], how_known: "Britannica and Wikipedia agree (P15)."}
    place: {value: "Milan, Ohio, U.S.", modern_name: "Milan, Ohio, United States", polity_then: "United States", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "infobox"}], how_known: "Britannica and Wikipedia."}
  death:
    date: {value: "1931-10-18", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "infobox"}], how_known: "Britannica and Wikipedia."}
    place: {value: "West Orange, New Jersey, U.S.", modern_name: "West Orange, New Jersey, United States", polity_then: "United States", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "infobox"}], how_known: "Britannica and Wikipedia."}
  first_lasting_contribution_year: {value: 1877, certainty: 0.7, cites: [{source: S6, locator: "Phonograph; Years active 1877–1930"}, {source: S1, locator: "opening / Newark"}], how_known: "Phonograph (1877) is the first lasting invention dated in the dual bios for the Menlo Park fame span; quadruplex sale 1874 remains listed (0.7)."}
  era_bucket: {value: "1750 to 1849", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "Birth year bucket (P2)."}
  region_of_birth: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "United States (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S6, locator: "Menlo Park; West Orange"}], how_known: "New Jersey labs."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [English], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
  occupations: {value: ["inventor", "entrepreneur"], certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "infobox"}], how_known: "Britannica and Wikipedia."}
contribution:
  primary_domain: invention
  fields: {value: ["electrical engineering", "telegraphy", "sound recording", "electric lighting", "motion pictures"], certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "Known for"}], how_known: "Dual bio."}
  lasting_original_contributions:
    - {value: "Quadruplex telegraph (four messages on one wire)", year: 1874, kind: invention, lasting: "'one of the larger payments for any invention up to that time' (S1)", certainty: 0.5, cites: [{source: S1, locator: "Newark paragraph"}], how_known: "Britannica; dated by the December 1874 sale (0.5)."}
    - {value: "Phonograph (sound recording and playback)", year: 1877, kind: invention, lasting: "International fame as 'Wizard of Menlo Park' (S6)", certainty: 0.7, cites: [{source: S6, locator: "Phonograph"}], how_known: "Wikipedia; years-active start 1877."}
    - {value: "Practical carbon-filament incandescent lamp and electric lighting system", year: 1879, kind: invention, lasting: "Patent filed 4 Nov 1879 / granted 27 Jan 1880; commercial system at Pearl Street 1882 (S6)", certainty: 0.7, cites: [{source: S6, locator: "Electric light; Electric power distribution"}], how_known: "Wikipedia."}
    - {value: "First industrial research laboratory (Menlo Park; later West Orange)", kind: "body of work", lasting: "Model for industrial R&D (S6)", certainty: 0.7, cites: [{source: S6, locator: "Research and development facility"}, {source: S1, locator: "opening"}], how_known: "Dual bio."}
    - {value: "Early motion-picture camera (Kinetograph) and peep-hole viewer (Kinetoscope)", year: 1891, kind: invention, lasting: "First public exhibition 20 May 1891; studio film business through ~1911 (S6)", certainty: 0.7, cites: [{source: S6, locator: "Motion pictures"}], how_known: "Wikipedia."}
    - {value: "Nickel–iron rechargeable (storage) battery", year: 1901, kind: invention, lasting: "US/European patent 1901; Edison Storage Battery Company (S6)", certainty: 0.7, cites: [{source: S6, locator: "Rechargeable battery"}], how_known: "Wikipedia; mature demonstration ~1910."}
  evidence_of_impact:
    - {value: "1,093 U.S. patents; General Electric formed from Edison General Electric merger", kind: "other", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "opening"}], how_known: "Dual bio."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1, S6).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated in sources read (mother taught reading/writing; denomination not named)."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father Samuel Edison, Jr., lighthouse keeper and carpenter at Fort Gratiot from 1854; mother Nancy Elliot Edison (former schoolteacher)", role: parents, certainty: 0.7, cites: [{source: S1, locator: "family paragraph; 'Early years'"}, {source: S6, locator: "Early life"}], how_known: "Dual bio."}
  household_circumstances: {value: "Seventh and last child, fourth surviving; early hearing problems; family owned a set of Thomas Paine books that influenced him lifelong (S6)", certainty: 0.7, cites: [{source: S1, locator: "family paragraph"}, {source: S6, locator: "Early life"}], how_known: "Dual bio."}
  schooling:
    - {value: "School at Port Huron, attended sporadically for five years; left 1859", stage: "elementary school", run_by: other, certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
    - {value: "Avid and omnivorous reading; mother taught reading, writing, arithmetic", stage: "self-directed", run_by: family, certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}, {source: S6, locator: "Early life"}], how_known: "Dual bio."}
    - {value: "Apprentice telegrapher (1863)", stage: apprenticeship, run_by: other, certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure:
    - {value: "A School Compendium of Natural and Experimental Philosophy (gift from mother); tinkered with electricity", certainty: 0.7, cites: [{source: S6, locator: "Early life"}], how_known: "Wikipedia."}
  key_early_reading:
    - {value: "Thomas Paine (family set; lifelong influence; later defended Paine's scientific deism)", certainty: 0.7, cites: [{source: S6, locator: "Early life; Religion and metaphysics"}], how_known: "Wikipedia citing Israel."}
  childhood_mentors: []
  languages_in_childhood: {value: [English], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1877–1910", certainty: 0.7, cites: [{source: S6, locator: "Years active; Phonograph; Rechargeable battery"}], how_known: "Equals timing.major_work_period (P29)."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "Science / proof over theological assertion; Nature or Supreme Intelligence in place of the personal God of the religions", certainty: 0.5, cites: [{source: S2, locator: "Nature is what we know"}, {source: S8, locator: "theories of the theologians cannot be proved"}], how_known: "1910 interview and 1911 Columbian (secondary quotation)."}
  primary_system:
    value: DEISM
    basis: recorded_interview
    certainty: 0.5
    cites: [{source: S2, locator: "Nature / gods of religions"}, {source: S6, locator: "Religion and metaphysics; Israel freethinker / scientific deism"}, {source: S7, locator: "21 July 1885 unchangeable laws"}, {source: S9, locator: "clarifying letter Nature = Supreme Intelligence"}]
    rationale: "Scientific deism / freethinker reading (Israel via S6): affirms a Supreme Intelligence / Nature that rules matter and made unchangeable laws; denies the personal intervening God of the religions and a Being throned above directing mundane affairs; rejects theologians' unprovable theories as a source of knowledge (P27 revelation/theology). Defended Paine's scientific deism against the atheist label (S6). Named alternatives: PANT (God identified with Nature in the clarifying letter) and ATHE (public label he denied)."
    how_known: "(interview) 1910 NYT + 1911 Columbian; 1885 diary and clarifying letter (secondary quotation) plus Israel via Wikipedia in support; contested PANT reading keeps 0.5."
    note: "Not ATHE: he denied that the 1910 article denied God's existence. Not plain DETERM: Supreme Intelligence / Almighty language remains."
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: DEISM, reason: "Coded @0.5: Israel freethinker / scientific deism; Paine defense; unchangeable laws + non-intervening Supreme Intelligence; rejection of personal God of theologies and of theologians' proofs (P27).", cites: [{source: S6, locator: "Religion and metaphysics"}, {source: S7, locator: "21 July 1885"}, {source: S2, locator: "Nature quote"}]}
    - {code: PANT, reason: "Named alternative: clarifying letter 'what you call God I call Nature, the Supreme intelligence that rules matter' identifies deity with Nature (A toward 4).", cites: [{source: S9, locator: "clarifying letter"}, {source: S6, locator: "Religion and metaphysics"}]}
    - {code: ATHE, reason: "Named alternative rejected as primary: public atheist label after 1910; he clarified there was 'no such denial' of God (S9/S6).", cites: [{source: S6, locator: "Religion and metaphysics"}]}
    - {code: DETERM, reason: "Candidate from Marshall's materialist paraphrase and cell-aggregate lines; not coded — Supreme Intelligence / Almighty language cuts against plain materialism, and the strict no-supernatural wording is reported speech (§7).", cites: [{source: S2, locator: "transcript (opening paraphrase)"}]}
  lio_axes:
    A_locus:
      value: 4
      basis: recorded_interview
      certainty: 0.5
      support: corroborated
      cites: [{source: S2, locator: "Nature is what we know"}, {source: S4, locator: "NYT 1910 archive"}, {source: S9, locator: "what you call God I call Nature"}, {source: S8, locator: "Being throned above us"}, {source: S6, locator: "Religion and metaphysics"}, {source: S7, locator: "21 July 1885 (alt 1 evidence)"}]
      how_known: "(interview) NYT 1910 own-voice Nature line (S2/S4/S6); clarifying letter identifying God with Nature (S9 via Wikipedia/Israel); Columbian 1911 denial of a Being throned above directing affairs (S8 secondary quotation). Contested diary A1 reading caps at 0.5. Corroborated: interview cluster + letter."
      rationale: "Locus of divinity is Nature / Supreme Intelligence identical with or immanent in the order of the world, not a personal intervening God of the religions (P20/P38): 'nature made us—nature did it all—not the gods of the religions' (S2); 'what you call God I call Nature, the Supreme intelligence that rules matter' (S9); denial of 'a Being throned above us as a god, directing our mundane affairs in detail' (S8). Named alternative: 1 — 1885 diary 'Almighty' who made unchangeable laws and 'forgotten even the existence of this little mote' (classic remote deist person; S7)."
      alternatives:
        - {value: 1, note: "Diary 21 July 1885: transcendent Almighty who made laws and withdrew/forgot this world (DEISM system A).", cites: [{source: S7, locator: "21 July 1885"}]}
    B_cause:
      value: 4
      basis: recorded_interview
      certainty: 0.5
      support: corroborated
      cites: [{source: S7, locator: "unchangeable laws"}, {source: S2, locator: "nature made us / not the gods"}, {source: S8, locator: "not directing our mundane affairs in detail"}]
      how_known: "(interview) Inventor not scientist (P33): needs own words. 1910/1911 reject personal intervention; diary states unchangeable laws (P40) in corroboration. Contested 3-vs-4 keeps 0.5."
      rationale: "Scored on his account of nature (P6). Strict lawful order: 'he has made unchangeable laws to govern this and billions of other worlds' (S7, P40). Combined with rejection of a personal God who directs mundane affairs in detail or shows mercy to individuals (S2, S8) — non-scientist reject-intervention path (P41) would alone be B 3@0.5 alt 4; the diary supplies the exceptionless claim. Named alternative: 3 — if 'unchangeable laws' is read as soft deist design language without an explicit no-miracle claim, leaving only P41."
      alternatives:
        - {value: 3, note: "P41 path only (reject intervention / personal direction without counting diary as exceptionless).", cites: [{source: S2, locator: "Nature quote"}, {source: S8, locator: "Being throned above"}]}
    C_ledger:
      value: 3
      basis: recorded_interview
      certainty: 0.5
      support: single
      cites: [{source: S2, locator: "immortality of the soul; heaven reward"}]
      how_known: "(interview) One 1910 recorded interview (S2/S4); Forum 1926 softens to unknowable (S10) after the span — changes_over_life, not the score."
      rationale: "Denies personal immortality and heaven as reward for goodness: 'I cannot believe in the immortality of the soul'; 'Shall I, if I am good and earn reward, go to heaven when I die? No — no'; 'I cannot see any use of a future life' (S2). No personal post-mortem ledger. Named alternative: 4 — if cell-aggregate / phonograph-cylinder analogies are read as full denial of any surviving moral account."
      alternatives:
        - {value: 4, note: "Aggregate-of-cells / phonograph-cylinder analogies deny any surviving personal entity that could be judged.", cites: [{source: S2, locator: "aggregate of cells; phonographic cylinders"}]}
    D_authority:
      value: 3
      basis: recorded_interview
      certainty: 0.5
      support: corroborated
      cites: [{source: S8, locator: "theories of the theologians cannot be proved"}, {source: S2, locator: "Nature is what we know"}]
      how_known: "(interview) Columbian 1911 (S8 secondary quotation) plus 1910 Nature-vs-gods line; two source ids; 0.5 for secondary quotation / contested alt."
      rationale: "Observation/proof over theological assertion: 'I cannot accept as final any theory which is not provable. The theories of the theologians cannot be proved. Proof, proof!' (S8); 'Nature is what we know. We do not know the gods of religions' (S2). Not 4: he still affirms Supreme Intelligence / Almighty by reason, not pure observation-only naturalism."
      alternatives:
        - {value: 4, note: "If Nature-only knowledge is read as excluding any rational affirmation of Supreme Intelligence.", cites: [{source: S2, locator: "Nature is what we know"}]}
    E_scope: {value: UNKNOWN, how_known: "Not read (P7)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus ≥ 3 (value 4) but only at 0.5: the A ≥ 3 branch reads A only (P10) and needs 0.7. B is 4 at 0.5 and does not lift the branch."}
  statements:
    - text: "I cannot believe in the immortality of the soul."
      cites: [{source: S2, locator: "transcript"}]
      date: "1910-10-02"
      context: "Edward Marshall interview, New York Times Magazine, 2 October 1910."
      axes: [C_ledger]
      kind: "recorded interview"
      verified_against: "newspaper interview"
      verified_on: 2026-10-24
    - text: "Nature is what we know. We do not know the gods of religions. And nature is not kind, or merciful, or loving. If God made me—the fabled God of the three qualities of which I spoke: mercy, kindness, love—He also made the fish I catch and eat. And where do His mercy, kindness, and love for that fish come in? No; nature made us—nature did it all—not the gods of the religions."
      cites: [{source: S2, locator: "Nature paragraph"}, {source: S4, locator: "NYT archive page"}, {source: S6, locator: "Religion and metaphysics blockquote"}, {source: S11, locator: "Wikiquote 1910s Nature"}]
      date: "1910-10-02"
      context: "Same Marshall NYT interview; own-voice lines (not Marshall's materialist paraphrase)."
      axes: [A_locus, B_cause, D_authority]
      kind: "recorded interview"
      verified_against: "newspaper interview"
      verified_on: 2026-10-24
      note: "Wikiquote/Wikipedia/sundaymagazine agree on wording; NYT paywalled facsimile not opened this pass."
    - text: "You have misunderstood the whole article, because you jumped to the conclusion that it denies the existence of God. There is no such denial, what you call God I call Nature, the Supreme intelligence that rules matter."
      cites: [{source: S9, locator: "clarifying letter"}, {source: S6, locator: "Religion and metaphysics"}]
      date: "1910-10"
      context: "Private clarifying letter after the 1910 NYT interview (to H. Toyer / correspondent; quoted via Israel 1998 in Wikipedia)."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Israel 1998 pp. 8–9 not opened this pass; wording from Wikipedia Religion section / Deism page."
    - text: "What a wonderfully small idea mankind has of the Almighty. My impression is that he has made unchangeable laws to govern this and billions of other worlds and that he has forgotten even the existence of this little mote of ours ages ago."
      cites: [{source: S7, locator: "21 July 1885"}]
      date: "1885-07-21"
      context: "Personal diary, Woodside Villa / Boston Harbor vacation."
      axes: [A_locus, B_cause]
      kind: "notebook or diary"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "ariwatch.com complete diary from facsimile; Edison Papers digital diary project confirms the volume (12–21 July 1885). Page images on edisonpapers.github.io not opened this pass."
    - text: "I never have denied Supreme Intelligence. What I have denied and what my reason compels me to deny, is the existence of a Being throned above us as a god, directing our mundane affairs in detail, regarding us as individuals, punishing us, rewarding us as human judges might."
      cites: [{source: S8, locator: "Columbian paraphrase/quote"}]
      date: "1911-01"
      context: "Interview, The Columbian Magazine, January 1911 ('Thomas A. Edison on Immortality')."
      axes: [A_locus, B_cause, C_ledger]
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Wording from secondary web quotation (notable-quotes / blog extracts); Columbian pages unread."
    - text: "I cannot accept as final any theory which is not provable. The theories of the theologians cannot be proved. Proof, proof! That is what I always have been after; that is what my mind requires before it can accept a theory as fact."
      cites: [{source: S8, locator: "Proof, proof"}]
      date: "1911-01"
      context: "Same Columbian Magazine interview."
      axes: [D_authority]
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
    - text: "Searching the inner structure of all things for the fundamental, Edison told me he had come to the conclusion that there is no \"supernatural,\" or \"supernormal,\" as the psychic researchers put it -- that all there is, that all there has been, all there ever will be, can or will, soon or late, be explained along material lines"
      cites: [{source: S2, locator: "transcript (opening)"}]
      date: "1910-10-02"
      context: "Marshall's paraphrase in the same interview — kept for context; cannot score alone (§7)."
      axes: [B_cause]
      kind: "reported speech"
      verified_against: "newspaper interview"
      verified_on: 2026-10-24
      note: "Not used alone for B (create-pass FAIL; P33 inventor)."
    - text: "There are two reasons why we do not possess positive knowledge on the difficult subject of the soul and immortality. Principal of these is the fact that we do not at present know how even to begin investigation of them."
      cites: [{source: S10, locator: "Forum 1926 quotation"}, {source: S3, locator: "Communicating with the Dead exhibit"}]
      date: "1926-11"
      context: "Edward Marshall, 'Has Man an Immortal Soul', The Forum, November 1926; after the coded span."
      axes: [C_ledger]
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Softens the 1910 flat denial toward investigative agnosticism; logged in changes_over_life (P20/P31)."
  changes_over_life:
    - {value: "Forum interview (1926) softens 1910 flat denial of soul immortality toward investigative agnosticism ('we do not at present know how even to begin investigation'). After major_work_period end (1910); C for working years stays on the 1910 interview.", certainty: 0.5, cites: [{source: S10, locator: "Forum 1926"}, {source: S3, locator: "exhibit"}], how_known: "Edison Papers quotation of Marshall Forum Nov 1926; after span (P31)."}
  coder_notes: "Deepen D1: inventor under P33 (no listed theory/result about natural systems). B uses diary unchangeable laws (P40) plus interview reject-intervention (P41 alt). A contested 4 vs diary 1 — Nature=God / no Being throned above preferred for public working-years cluster (1910–11). primary DEISM @0.5 with PANT alt (no PANT system file under that id; system id is PANT). Philosophy of Thomas Paine (1925) essay URL 404 this pass — Paine defense taken from Wikipedia/Israel. NYT and Columbian page images unread. No fallacy_catalog (Jason)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "American", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated as childhood confession in sources read; adult freethinker / scientific deism is not birth-heritage (P19)."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "No baptism record opened."}
  childhood_catechism: {value: UNKNOWN, how_known: "No childhood catechism curriculum named."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1877–1910", certainty: 0.7, cites: [{source: S6, locator: "Phonograph; Electric light; Rechargeable battery"}, {source: S1, locator: "Newark paragraph"}], how_known: "First lasting listed contribution phonograph 1877 through storage-battery maturation ~1910 (P29/P30); quadruplex 1874 listed but years-active start 1877 (S6)."}
  age_at_first_lasting_contribution: {value: 30, certainty: 0.7, cites: [{source: S6, locator: "Phonograph; birth"}], how_known: "1877 − 1847 = 30 (P30)."}
  first_evidence_of_lio_type_views: {value: "1885", certainty: 0.5, cites: [{source: S7, locator: "21 July 1885"}], how_known: "Diary unchangeable-laws / Almighty line; A or B scored ≥3 (P27 anchor)."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.7, cites: [{source: S7, locator: "1885"}, {source: S2, locator: "1910"}], how_known: "Diary 1885 and NYT/Columbian 1910–11 fall inside 1877–1910."}
  worldview_during_major_work: {value: DEISM, certainty: 0.5, cites: [{source: S6, locator: "Religion and metaphysics"}, {source: S2, locator: "Nature quote"}, {source: S7, locator: "unchangeable laws"}], how_known: "As primary_system."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Inventor; no geometric-form evidence read.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Not read."}
  circle_present: {value: "no", rationale: "Denies personal intervening God; Nature/Supreme Intelligence is not a petitionary personal circle.", certainty: 0.5, cites: [{source: S2, locator: "Nature quote"}, {source: S8, locator: "Being throned above"}], how_known: "Coder's reading of Lane B labels."}
  reading: "Scientific deism / freethinker: Nature or Supreme Intelligence, unchangeable laws, no personal intervening God, no personal immortality."
  notes: "Lane B only — not a finding. Chart darkness from Lane A certainties."

institutions:
  - {value: "Western Union Telegraph Company", role: inventor, kind: "patron or funder", certainty: 0.7, cites: [{source: S1, locator: "Newark paragraph"}], how_known: "Britannica."}
  - {value: "Menlo Park laboratory", role: founder, kind: "research institute", certainty: 0.7, cites: [{source: S6, locator: "Research and development facility"}], how_known: "Wikipedia."}
collaborators:
  - {value: "Frank L. Pope", relation: collaborator, certainty: 0.7, cites: [{source: S1, locator: "New York paragraph"}], how_known: "Partnership."}
  - {value: "Charles Batchelor", relation: collaborator, certainty: 0.7, cites: [{source: S6, locator: "Telegraphy; Phonograph"}], how_known: "Wikipedia."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S5, locator: "roster.csv, rank 76"}], how_known: "Study roster."}
  controversies:
    - {value: "1910 NYT interview labeled him an atheist; he clarified privately that he denied personal immortality, not God (Nature = Supreme Intelligence).", certainty: 0.7, cites: [{source: S6, locator: "Religion and metaphysics"}, {source: S9, locator: "clarifying letter"}], how_known: "Wikipedia Religion section summarizing the controversy and Israel letter."}
  data_quality_flags:
    - "NYT 1910 and Columbian 1911 page images unread; Columbian wording is secondary quotation."
    - "Clarifying letter and Israel 1998 pp. 8–9 unread as page images; Nature=God letter via Wikipedia/Israel secondary quotation."
    - "Diary verified against unofficial facsimile transcript (ariwatch), not Edison Papers IIIF page images this pass."
    - "Philosophy of Thomas Paine (1925) essay URL 404; Paine defense via Wikipedia/Israel only."
  open_questions:
    - "Open NYT 1910 p. 15 facsimile and Columbian Magazine Jan 1911 pages for primary check (upgrade verified_against)."
    - "Read Israel, Edison: A Life of Invention (1998) pp. 8–9 and the clarifying letter text in the Edison Papers."
    - "Recover Philosophy of Thomas Paine (1925) for written_profession DEISM/Paine defense."
    - "Forum 1926 full text for changes_over_life / late C."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Robert E. Conot"
    citation: "Conot, Robert E. \"Thomas Edison.\" Encyclopaedia Britannica, updated 14 October 2026. https://www.britannica.com/biography/Thomas-Edison."
    url: "https://www.britannica.com/biography/Thomas-Edison"
    accessed: 2026-10-15
    source_quality: "reference entry"
    reliability_note: "Signed body (Conot, with Britannica Editors) through the Newark years; Top Questions not cited. Live page was JS-heavy this deepen pass; prior create-pass reading retained for Newark/family; Wikipedia used for phonograph/lamp dates (P50)."
    used_for: [identity, basics, contribution, childhood, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: secondary
    kind: other
    author: "The Sunday Magazine (sundaymagazine.org)"
    citation: "\"'No Immortality Of The Soul' Says Thomas A. Edison.\" Excerpt of Edward Marshall's New York Times interview of 2 October 1910. https://www.sundaymagazine.org/p/no-immortality-of-the-soul-says-thomas-a-edison."
    url: "https://www.sundaymagazine.org/p/no-immortality-of-the-soul-says-thomas-a-edison"
    accessed: 2026-10-24
    source_quality: "newspaper interview"
    reliability_note: "Web transcription of the Marshall NYT interview with ellipses; own-voice Nature / immortality lines cross-checked against Wikipedia and Wikiquote. Marshall's opening materialist paraphrase kept as reported speech only."
    used_for: [worldview, timing, lane_b]
  - id: S3
    type: secondary
    kind: "institutional page"
    author: "Thomas A. Edison Papers, Rutgers University"
    citation: "Thomas A. Edison Papers. \"Communicating with the Dead\" (digital exhibit) and published-articles bibliography. https://edison.rutgers.edu/digital-exhibits/edison-science-fiction/science-fiction-10."
    url: "https://edison.rutgers.edu/digital-exhibits/edison-science-fiction/science-fiction-10"
    accessed: 2026-10-24
    source_quality: "scholarly edition or monograph"
    reliability_note: "Scholarly editing project; Forum 1926 quotation and context for the 1910 controversy."
    used_for: [worldview]
  - id: S4
    type: secondary
    kind: other
    author: "The New York Times"
    citation: "Marshall, Edward. \"'No Immortality of the Soul' Says Thomas A. Edison.\" New York Times, 2 October 1910, pp. 1, 15. https://www.nytimes.com/1910/10/02/archives/-no-immortality-of-the-soul-says-thomas-a-edison-in-fact-he-doesnt-.html."
    url: "https://www.nytimes.com/1910/10/02/archives/-no-immortality-of-the-soul-says-thomas-a-edison-in-fact-he-doesnt-.html"
    accessed: 2026-10-24
    source_quality: "newspaper interview"
    reliability_note: "Archive page; paywalled facsimile not opened this pass. Used with S2/S6 for the same interview."
    used_for: [worldview]
  - id: S5
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    source_quality: "study roster"
    reliability_note: "Study's own roster."
    used_for: [identity, review]
  - id: S6
    type: secondary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "\"Thomas Edison.\" Wikipedia. https://en.wikipedia.org/wiki/Thomas_Edison (Religion and metaphysics; Phonograph; Electric light; Rechargeable battery; Early life)."
    url: "https://en.wikipedia.org/wiki/Thomas_Edison"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Dual bio with Britannica (P50). Religion section quotes NYT 1910 and the clarifying letter via Israel 1998; used for dates and for secondary quotation of Israel/letter pending primary check."
    used_for: [identity, basics, contribution, childhood, worldview, timing, review]
  - id: S7
    type: primary
    kind: "diary or notebook"
    author: "Thomas A. Edison"
    year: 1885
    citation: "Edison, Thomas A. Personal diary, 12–21 July 1885, entry for 21 July 1885. Complete text transcribed from facsimile at https://ariwatch.com/VS/TheDiaryOfThomasEdison.htm; volume confirmed by Edison Papers diary sampler / edisonpapers.github.io/diaries/."
    url: "https://ariwatch.com/VS/TheDiaryOfThomasEdison.htm"
    accessed: 2026-10-24
    source_quality: "unofficial web copy"
    reliability_note: "Unofficial complete transcript claiming facsimile basis; Edison Papers confirms the diary exists. IIIF page images on edisonpapers.github.io not opened this pass — treat as unofficial web copy (0.7 cap for private text already at 0.5 for one document)."
    used_for: [worldview, timing]
  - id: S8
    type: secondary
    kind: other
    author: "The Columbian Magazine (via secondary quotation)"
    year: 1911
    citation: "\"Thomas A. Edison on Immortality.\" The Columbian Magazine, January 1911. Wording as quoted in secondary web extracts (e.g. notable-quotes.com; wherelivingbegins.wordpress.com, 2024)."
    url: "https://wherelivingbegins.wordpress.com/2024/06/27/thomas-edison/"
    accessed: 2026-10-24
    source_quality: "newspaper interview"
    reliability_note: "Secondary quotation only; Columbian pages unread. Cross-checked across two web extracts for the Supreme Intelligence / Being throned above and Proof proof lines."
    used_for: [worldview]
  - id: S9
    type: secondary
    kind: "scholarly book"
    author: "Paul Israel"
    year: 1998
    citation: "Israel, Paul. Edison: A Life of Invention. Wiley, 1998, pp. 8–9. Clarifying-letter quotation ('what you call God I call Nature…') as given in Wikipedia 'Thomas Edison' Religion and metaphysics (citing Israel)."
    url: "https://en.wikipedia.org/wiki/Thomas_Edison"
    accessed: 2026-10-24
    source_quality: "scholarly edition or monograph"
    reliability_note: "Scholarly biography; pages unread this pass. Letter wording used as secondary quotation via Wikipedia cite. Also source of freethinker / scientific-deism characterization."
    used_for: [worldview, review]
  - id: S10
    type: secondary
    kind: "institutional page"
    author: "Thomas A. Edison Papers, Rutgers University"
    year: 1926
    citation: "Thomas A. Edison Papers. \"Communicating with the Dead\" — quotation from Edward Marshall, \"Has Man an Immortal Soul,\" The Forum, November 1926. https://edison.rutgers.edu/digital-exhibits/edison-science-fiction/science-fiction-10."
    url: "https://edison.rutgers.edu/digital-exhibits/edison-science-fiction/science-fiction-10"
    accessed: 2026-10-24
    source_quality: "scholarly edition or monograph"
    reliability_note: "Same Edison Papers exhibit as S3; separate id for the 1926 Forum quotation used in changes_over_life."
    used_for: [worldview]
  - id: S11
    type: secondary
    kind: other
    author: "Wikiquote contributors"
    citation: "\"Thomas Edison.\" Wikiquote. https://en.wikiquote.org/wiki/Thomas_Edison (1910 Nature quote cross-check)."
    url: "https://en.wikiquote.org/wiki/Thomas_Edison"
    accessed: 2026-10-24
    source_quality: "unofficial web copy"
    reliability_note: "Cross-check only for 1910 Nature wording; not used alone to score."
    used_for: [worldview]
---

# Thomas Edison

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Thomas Edison (1847–1931), American inventor [S1, S6]. Deepen D1: primary_system DEISM @0.5; A 4 @0.5 corroborated (alt 1); B 4 @0.5 corroborated (alt 3); C 3 @0.5; D 3 @0.5; mid_basin BELOW_THRESHOLD. Chart: faded filled if plotted (min(A,B) cert 0.5; both A and B support corroborated). Chart-moving YES (A&B leave BELOW).

## Life and work

Port Huron; telegrapher; Newark; Menlo Park laboratory; West Orange; phonograph, electric light and power, motion pictures, storage battery [S1, S6].

## Contribution and impact

Quadruplex (1874); phonograph (1877); carbon-filament lamp (1879) and Pearl Street system (1882); Kinetograph/Kinetoscope (1891); nickel–iron battery (1901–~1910); 1,093 U.S. patents [S1, S6].

## Childhood and education

Sporadic schooling; self-taught reader; Paine in the household library [S1, S6].

## Adult working worldview

Scientific deism / freethinker [S6, S9]. 1885 diary: Almighty made unchangeable laws and forgot this mote [S7]. 1910: Nature vs gods of religions; no immortality of the soul [S2]. Clarifying letter: God = Nature, Supreme Intelligence [S9]. 1911 Columbian: never denied Supreme Intelligence; denies Being throned above directing affairs; theologians' theories unprovable [S8]. 1926 Forum softens soul knowledge (after span) [S10].

## Heritage (context only)

See front matter [S1].

## Timing

Major work 1877–1910; first lasting contribution phonograph 1877 at age 30; LIO-type views evidenced 1885 (during) [S6, S7].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Scientific deism; circle absent [S2, S8].

## Open questions

- NYT / Columbian facsimiles; Israel pp. 8–9; Philosophy of Thomas Paine 1925; Forum 1926 full text.

## Research log

- 2026-10-15: Read Britannica (Conot) through Newark; the 1910 interview transcript (sundaymagazine.org).
- 2026-10-24: Deepen D1 — Wikipedia dual bio; ariwatch 1885 diary; Columbian secondary quotes; Edison Papers Forum exhibit; Nature clarifying letter via Wikipedia/Israel. No fallacy audit.
