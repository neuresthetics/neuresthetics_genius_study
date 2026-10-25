---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 4
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Y; deepen catch-up)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen catch-up 2/13 (F 4, rank 132): firm A/primary if sources allow; do not force plot. Read Isaacson Steve Jobs (2011) primary OCR (S5; IA steve-jobs-walter-isaacson_202601) — RQ-Y1 path. primary BELOW→AGNOS @0.5 recorded_interview, alt BELOW (P8; after-span interviews; Zen/BUDDH lead). A stays BELOW (P20 explicit suspension, no locus). B stays UNKNOWN (not scientist; no nature-order). mid UNKNOWN (B UNKNOWN precedence). Childhood Lutheran + Biafra exit (S5 pp.14–15). Heritage bio/adoptive from S5+S6. Stanford re-verified (S2). Playboy 1985 opened (allaboutstevejobs) — no God/system score. P47 on all. No fallacy_catalog; figures not refreshed. Not plotted. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Audit note (gs_ca27fcf_KK run 1, KK17): the iPhone's lasting wording restored to the article body's 'into the telecommunications business'; the added product list dropped. No score changes."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Audit fixes for batch Y (gs_7b46f24_Y run 1): (JO12) definition_fit and the iPhone's lasting note now cite Britannica's article body ('a charismatic pioneer of the personal computer era'; 'near-messianic belief in the computer revolution'), not the 'Why is Steve Jobs significant?' question box (P26). Ruling Y1 (v8's call on the auditor's advice): primary_system stays BELOW_THRESHOLD (recorded under P43, beside V3). No score changes."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Y, order P32: F 4, rank 132; roster status provisional). Basics from Britannica (Steven Levy, updated 29 Sep 2026). Own voice read in the prepared text of the 2005 Stanford commencement address (in the span). His words on God reach us only as the Washington Post's quotations of Isaacson's 2011 biography (secondary quotation, after the span): 'I'm about fifty-fifty on believing in God'. Not a scientist (P33). Span 1977–2007 at 0.7 (Apple II to iPhone). primary_system BELOW_THRESHOLD (AGNOS lead, BUDDH lead; RQ-Y1); A BELOW_THRESHOLD; B, C, E UNKNOWN; D BELOW_THRESHOLD; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}

identity:
  id: jobs-steve
  display_name: "Steve Jobs"
  roster:
    canonical_name: "Steve Jobs"
    rank: 132
    F: 4
    models: [DeepSeek, Gemini, GPT, Grok]
    band: "core (3–4)"
    status: provisional
    field: technology
    field_bucket: "invention / engineering"
  full_name: {value: "Steven Paul Jobs", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts (Also Known As)"}, {source: S6, locator: "lead / Early life"}], how_known: "Britannica; Wikipedia dual bio agrees (P50)."}
  native_name: {value: "Steven Paul Jobs", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}], how_known: "English is his own language."}
  aliases:
    - {name: "Jobs-Steve", kind: "roster alias"}
    - {name: "Steve-Jobs", kind: "roster alias"}

basics:
  birth:
    date: {value: "1955-02-24", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "Quick Facts (Born)"}, {source: S6, locator: "infobox / Early life"}], how_known: "Britannica; Wikipedia dual bio agrees (P50)."}
    place: {value: "San Francisco, California", modern_name: "San Francisco, California, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts (Born)"}, {source: S6, locator: "infobox"}], how_known: "Britannica; Wikipedia dual bio agrees (P50)."}
  death:
    date: {value: "2011-10-05", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "Quick Facts (Died)"}, {source: S6, locator: "infobox"}], how_known: "Britannica; Wikipedia dual bio agrees (P50)."}
    place: {value: "Palo Alto, California", modern_name: "Palo Alto, California, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts (Died)"}, {source: S6, locator: "infobox"}], how_known: "Britannica; Wikipedia dual bio agrees (P50)."}
  first_lasting_contribution_year: {value: 1977, certainty: 0.7, cites: [{source: S1, locator: "'Founding of Apple'"}], how_known: "The Apple II, completed in 1977, 'an immediate success, becoming synonymous with the boom in personal computers' (S1). The Apple I (1976) is not called lasting. Designed by Wozniak 'with Jobs's encouragement', so attribution is shared (roster note)."}
  era_bucket: {value: "1950 on", certainty: 1.0, cites: [{source: S1, locator: "'Founding of Apple'"}], how_known: "From 1977 (P2)."}
  region_of_birth: {value: "North America", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}], how_known: "United States (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "'Founding of Apple'"}], how_known: "Silicon Valley."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S2, locator: "text"}], how_known: "His address."}
  occupations: {value: ["businessman", "cofounder and CEO of Apple", "founder of NeXT", "owner of Pixar"], certainty: 0.7, cites: [{source: S1, locator: "opening; 'NeXT and Pixar'"}], how_known: "Britannica."}

contribution:
  fields: {value: ["personal computing", "consumer electronics", "product design"], certainty: 0.7, cites: [{source: S1, locator: "opening; 'Reinventing Apple'"}], how_known: "Britannica; labels the coder's."}
  lasting_original_contributions:
    - {value: "Apple II personal computer (with Steve Wozniak)", year: 1977, kind: invention, lasting: "'becoming synonymous with the boom in personal computers' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Founding of Apple'"}], how_known: "Britannica; Wozniak designed it, Jobs pushed the design and case and found financing (S1)."}
    - {value: "Macintosh, with its graphical user interface", year: 1984, kind: invention, lasting: "'the model for all subsequent computer interfaces' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Insanely great'"}], how_known: "Britannica: Jobs headed the project and introduced it in January 1984."}
    - {value: "iPod and the iTunes ecosystem", year: 2001, kind: invention, lasting: "'quickly became the market leader' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Reinventing Apple'"}], how_known: "Britannica."}
    - {value: "iPhone", year: 2007, kind: invention, lasting: "took Apple 'into the telecommunications business' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Reinventing Apple'"}], how_known: "Britannica. Latest dated lasting item, so it ends the span (P30 addendum b); the iPad (2010) appears only in a photo caption, so it is not listed."}
  evidence_of_impact:
    - {value: "Presidential Medal of Freedom (2022, posthumous)", kind: "other", certainty: 0.7, cites: [{source: S1, locator: "'Health issues'"}], how_known: "Britannica; after his death."}
    - {value: "The Mac interface became 'the model for all subsequent computer interfaces'", kind: "institutional or technological lineage", certainty: 0.7, cites: [{source: S1, locator: "'Insanely great'"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "arguable", rationale: "Britannica's body calls him 'a charismatic pioneer of the personal computer era' and notes his 'near-messianic belief in the computer revolution'; the roster flags 'attribution vs. team' (S4).", certainty: 0.5, cites: [{source: S1, locator: "introduction; 'Founding of Apple'"}, {source: S4, locator: "roster.csv, rank 132"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Lutheran (adoptive household practice)", certainty: 0.7, cites: [{source: S5, locator: "ch. 1 / childhood religion (print ~p. 14)"}, {source: S6, locator: "Infancy (Lutheran church; cites Isaacson p. 14)"}], how_known: "Isaacson: adoptive parents took him to the Lutheran church most Sundays until age 13 (S5). Wikipedia dual bio cites the same locus (S6)."}
  family_religious_practice: {value: "Lutheran church most Sundays until age 13; then none in the household (he never went back)", certainty: 0.7, cites: [{source: S5, locator: "Biafra / pastor confrontation (~pp. 14–15)"}], how_known: "Isaacson: ended at thirteen after the Biafra Life-cover confrontation with the pastor (S5)."}
  parents_and_household:
    - {value: "Adopted at birth by Paul Reinhold Jobs and Clara (née Hagopian) Jobs; he regarded them as his parents '1,000%'", role: family, certainty: 0.7, cites: [{source: S5, locator: "ch. 1 adoption"}, {source: S2, locator: "first story"}, {source: S6, locator: "Family"}], how_known: "Isaacson; his Stanford address; Wikipedia."}
    - {value: "Biological mother Joanne Carole Schieble (American, Swiss-German / Catholic family background); biological father Abdulfattah 'John' Jandali (Syrian, from a Muslim household)", role: family, certainty: 0.7, cites: [{source: S5, locator: "ch. 1 / Joanne Schieble and Jandali"}, {source: S6, locator: "Family"}], how_known: "Isaacson; Wikipedia dual bio (P50). Heritage context only — not a worldview code."}
    - {value: "Adoptive father Paul Jobs, machinist and tinkerer (cars, lasers at Spectra-Physics)", role: family, certainty: 0.7, cites: [{source: S5, locator: "ch. 1"}, {source: S1, locator: "'Founding of Apple'"}], how_known: "Isaacson; Britannica."}
  household_circumstances: {value: "Working-class adoptive home: 'my mother had never graduated from college, and ... my father had never graduated from high school'", certainty: 0.7, cites: [{source: S2, locator: "first story"}], how_known: "His own address."}
  schooling:
    - {value: "Reed College, Portland, Oregon (dropped out after six months; stayed as a drop-in for about 18 months, including a calligraphy class)", stage: university, run_by: private, years: "c. 1972–1974", certainty: 0.5, cites: [{source: S2, locator: "first story"}, {source: S1, locator: "'Founding of Apple'"}], how_known: "His address and Britannica; years the coder's (college at 17; Atari job early 1974)."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading:
    - {value: "The Whole Earth Catalog ('one of the bibles of my generation')", certainty: 0.7, cites: [{source: S2, locator: "closing"}], how_known: "His own address."}
    - {value: "Zen Mind, Beginner's Mind (Suzuki); Autobiography of a Yogi; Cutting Through Spiritual Materialism (Trungpa) — shared with Kottke at Reed", certainty: 0.5, cites: [{source: S5, locator: "Reed / Zen books"}], how_known: "Isaacson (reported from Jobs/Kottke circle); formative reading, not a system code."}
  childhood_mentors: []
  languages_in_childhood: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  notable_events:
    - {value: "At age 13 left the Lutheran church after confronting the pastor with a Life magazine cover of starving children in Biafra; 'he never went back to church'", year: 1968, certainty: 0.7, cites: [{source: S5, locator: "~pp. 14–15"}], how_known: "Isaacson (childhood, P31 for later worldview)."}
    - {value: "Pilgrimage to India seeking enlightenment / Neem Karoli Baba (about seven months; with Daniel Kottke)", year: 1974, certainty: 0.7, cites: [{source: S5, locator: "Atari and India / seven months"}, {source: S1, locator: "'Founding of Apple'"}], how_known: "Isaacson: 'For me it was a serious search' (S5); Britannica notes the trip. Adult formative event (age 19), not BUDDH adherence (do_not_use_when)."}
    - {value: "Years of Zen practice with Kobun Chino Otogawa (Los Altos / Tassajara retreats); Isaacson: 'faithful follower' of Kobun", year: UNKNOWN, certainty: 0.5, cites: [{source: S5, locator: "Zen / Kobun Chino"}], how_known: "Isaacson; practice and study, not a stated BUDDH self-identification (BUDDH do_not_use_when)."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1977–2007", certainty: 0.7, cites: [{source: S1, locator: "'Founding of Apple'; 'Reinventing Apple'"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing read on science and religion as a paired claim (P19)."}
  primary_system:
    value: AGNOS
    basis: recorded_interview
    certainty: 0.5
    cites: [{source: S5, locator: "doors/house and great mystery (~p. 15); Coda fifty-fifty (~p. 570)"}, {source: S3, locator: "WaPo secondary quotation of same biography (support only)"}]
    how_known: "(interview) Isaacson 2011 is the interviewer's own first publication of Jobs's first-person words (P8; RQ-Y1 path). Explicit suspension: 'Sometimes I think the house exists, and sometimes I don't. It's the great mystery' and 'I'm about fifty-fifty on believing in God' (S5). 0.5: interviews fall after the span (P1; Isaacson sessions ~2009–2011); retrospective about lifelong spiritual feelings (P20); named alt BELOW for Zen-practice lead without an in-span AGNOS self-label. Support single for the score (S5); S3 WaPo is the same book via secondary quotation, not independent corroboration (P48)."
    rationale: "AGNOS = explicit suspension (systems/AGNOS use_when; v7.1). He states no settled yes/no on God or on whether 'the house' of religion exists, and prefers spiritual experience over received dogma. Named alternative BELOW_THRESHOLD: after-span timing + years of Zen practice (BUDDH lead) without a public AGNOS self-label inside 1977–2007; Stanford 2005 names only 'gut, destiny, life, karma, whatever' (S2)."
    alternatives:
      - {value: BELOW_THRESHOLD, note: "If after-span Isaacson interviews are held too late to set primary_system, or if Zen practice during the working years is read as the lead without a scored suspension code.", cites: [{source: S5, locator: "Zen practice; Coda"}, {source: S2, locator: "karma / dogma lines"}]}
  secondary_system: {value: UNKNOWN, how_known: "BUDDH rejected as a second code: meditation/Zen interest alone is not BUDDH (do_not_use_when); no self-identification as Buddhist read in his words."}
  candidate_codes_considered:
    - {code: AGNOS, reason: "Coded @0.5: explicit suspension in Isaacson interviews (doors/house; fifty-fifty) (S5; P8).", cites: [{source: S5, locator: "~p. 15; ~p. 570"}]}
    - {code: BUDDH, reason: "Rejected: years of Zen study/practice and India search (S5); BUDDH do_not_use_when — practice/interest alone, no stated adherence as Buddhist.", cites: [{source: S5, locator: "Zen / Kobun; India"}]}
    - {code: ATHE, reason: "Rejected: no denial of God; fifty-fifty and 'sometimes the house exists' are suspension, not denial (AGNOS do_not_use_when / neighbor).", cites: [{source: S5, locator: "Coda; doors"}]}
    - {code: CHRIST, reason: "Rejected: left Lutheran church at 13; critiques faith-based Christianity; no adult Christian profession (S5).", cites: [{source: S5, locator: "Biafra exit; juice goes out of Christianity"}]}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "(interview) Explicit suspension with no stated locus (P20): 'fifty-fifty on believing in God'; 'Sometimes I think the house exists, and sometimes I don't' (S5). AGNOS-compatible; does not place or deny God in/above/as Nature. Childhood rejection of 'worshipping such a God' (Biafra, age 13) is P31 and targets a theodicy-God, not an adult locus score. Stanford mentions heaven only as others' hope (S2)."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P33: products/design, not theories of nature). No own-voice statement on law and exception in the physical world read in Isaacson, Stanford, or Playboy 1985 (P16, P19). 'Karma' in the 2005 address is something to trust alongside gut/destiny, not a nature-order claim."}
    C_ledger: {value: UNKNOWN, how_known: "(interview) Hope that 'something survives after you die' against 'perhaps it's like an on-off switch' (S5 Coda) concerns survival/consciousness, not reward or punishment of persons (P19)."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "Lead from his own address (2005, in the span): 'Don't be trapped by dogma, which is living with the results of other people's thinking. Don't let the noise of others' opinions drown out your own inner voice' (S2). Sets inner voice against received dogma, not observation against revelation, so it does not reach a value. Isaacson: religion best when it emphasizes spiritual experience rather than received dogma (S5) — same lead, still under threshold."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7, P19)."}
  mid_basin: {value: UNKNOWN, how_known: "B_cause is UNKNOWN, which takes precedence for the P4 test (§6, P19); A_locus is also BELOW_THRESHOLD. Not plotted."}
  statements:
    - text: "You have to trust in something: your gut, destiny, life, karma, whatever. Because believing that the dots will connect down the road will give you the confidence to follow your heart, even when it leads you off the well-worn path."
      cites: [{source: S2, locator: "first story"}]
      date: "2005-06-12"
      context: "Stanford commencement address, 12 June 2005, on dropping out of Reed."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Stanford Report prepared text; Wayback snapshot re-checked this pass. Off-point for scored axes; in-span system-like wording only."
    - text: "Don't be trapped by dogma, which is living with the results of other people's thinking. Don't let the noise of others' opinions drown out your own inner voice."
      cites: [{source: S2, locator: "third story"}]
      date: "2005-06-12"
      context: "Same address, after his account of the 2004 cancer diagnosis."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "As above."
    - text: "The juice goes out of Christianity when it becomes too based on faith rather than on living like Jesus or seeing the world as Jesus saw it. I think different religions are different doors to the same house. Sometimes I think the house exists, and sometimes I don't. It's the great mystery."
      cites: [{source: S5, locator: "ch. 1 reflecting on spiritual feelings (~p. 15)"}]
      date: "2011"
      context: "Told to Walter Isaacson; placed in the biography after the childhood church exit and Zen note. Interview year not separately dated; published 2011 (after the span)."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Isaacson 'he told me' — interviewer's own first publication (P8). OCR of IA scan; wording matches WaPo secondary quotation (S3). After the span (P1)."
    - text: "I'm about fifty-fifty on believing in God. For most of my life, I've felt that there must be more to our existence than meets the eye."
      cites: [{source: S5, locator: "Coda (~p. 570)"}, {source: S3, locator: "closing paragraphs (secondary quotation of same)"}]
      date: "2011"
      context: "Garden conversation with Isaacson when Jobs 'wasn't feeling well', reflecting on death, India, Buddhism, reincarnation; he also floated an 'on-off switch' alternative and hoped 'something survives'."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Primary in S5 Coda; S3 is secondary quotation of the same book. After the span (P1). Retrospective 'for most of my life' noted under P20."
  changes_over_life:
    - {value: "Age 13 (1968): left Lutheran church after the Biafra confrontation; never returned to church (S5).", certainty: 0.7, cites: [{source: S5, locator: "~pp. 14–15"}], how_known: "Isaacson childhood narrative."}
    - {value: "Young adult (Reed / India / Kobun): intense Zen practice and India search; formative, not coded BUDDH (S5).", certainty: 0.5, cites: [{source: S5, locator: "Zen; India"}], how_known: "Isaacson; practice not BUDDH adherence."}
    - {value: "Late life (Isaacson interviews, after the span): explicit fifty-fifty suspension and doors/house mystery (S5 Coda / ~p. 15); scored as AGNOS @0.5 with BELOW alt (P1, P20).", certainty: 0.5, cites: [{source: S5, locator: "Coda; doors"}], how_known: "(interview) Isaacson primary; after the span."}
  coder_notes: "Deepen 2026-10-24: RQ-Y1 path taken — Isaacson read as P8 primary; primary_system AGNOS @0.5 interview, alt BELOW. A stays BELOW (P20). B UNKNOWN — do not force plot. Span unchanged 1977–2007. Not a scientist (P33). Playboy 1985 opened; no God/system score. Britannica live re-fetch Cloudflare this pass; prior S1 read kept; Wikipedia dual bio (S6) for identity facts (P50)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Biological: Swiss-German (mother) and Syrian (father); adoptive household German (Paul) and Armenian (Clara)", certainty: 0.7, cites: [{source: S5, locator: "ch. 1"}, {source: S6, locator: "Family"}], how_known: "Isaacson; Wikipedia. Context only."}
  religious_heritage_by_birth: {value: "Biological mother from a Catholic family background; biological father from a Muslim household; raised in an adoptive Lutheran-practicing home until age 13", certainty: 0.7, cites: [{source: S5, locator: "ch. 1 Schieble/Jandali; Lutheran"}, {source: S6, locator: "Family; Infancy"}], how_known: "Isaacson; Wikipedia. Context only — not a code."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated in sources read."}
  childhood_catechism: {value: "Lutheran Sunday school until age 13", certainty: 0.5, cites: [{source: S5, locator: "Sunday school / Biafra"}], how_known: "Isaacson implies Sunday-school attendance; not a formal catechism record."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1977–2007", certainty: 0.7, cites: [{source: S1, locator: "'Founding of Apple'; 'Reinventing Apple'"}], how_known: "Apple II (1977) to iPhone (2007) (P29, P30)."}
  age_at_first_lasting_contribution: {value: 22, certainty: 0.7, cites: [{source: S1, locator: "Quick Facts; 'Founding of Apple'"}], how_known: "1977 − 1955 = 22 (P30)."}
  first_evidence_of_lio_type_views: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S5, locator: "doors; Coda"}, {source: S2, locator: "text"}], how_known: "A is BELOW_THRESHOLD (suspension, no locus); nothing scored at 3 or 4."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S5, locator: "text"}, {source: S2, locator: "text"}], how_known: "As above."}
  worldview_during_major_work: {value: AGNOS, certainty: 0.5, cites: [{source: S5, locator: "doors/house; Coda 'for most of my life'"}], how_known: "(interview) As primary_system; retrospective Isaacson interviews about lifelong spiritual feelings, capped @0.5 (P1, P20). Alternative BELOW if after-span interviews are refused for the working years."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S2, locator: "text"}], how_known: "Not assessed."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "text"}], how_known: "Not assessed."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S2, locator: "text"}], how_known: "Not assessed."}
  reading: "Lane B only: AGNOS suspension (Isaacson) plus Zen practice lead; A BELOW and B UNKNOWN → mid UNKNOWN; not plotted."
  notes: ""

institutions:
  - {value: "Atari", role: "video game designer", years: "1974", kind: employer, certainty: 0.7, cites: [{source: S1, locator: "'Founding of Apple'"}], how_known: "Britannica."}
  - {value: "Apple Computer, Inc. (Apple Inc.)", role: "cofounder; CEO from 1997", years: "1976–1985; 1997–2011", kind: employer, certainty: 0.7, cites: [{source: S1, locator: "'Founding of Apple'; 'Saving Apple'; 'Health issues'"}], how_known: "Britannica."}
  - {value: "NeXT Inc.", role: "founder", years: "1985–1997", kind: employer, certainty: 0.7, cites: [{source: S1, locator: "'NeXT and Pixar'; 'Saving Apple'"}], how_known: "Britannica."}
  - {value: "Pixar", role: "controlling owner", years: "1986–2006", kind: employer, certainty: 0.7, cites: [{source: S1, locator: "'NeXT and Pixar'"}], how_known: "Britannica."}
collaborators:
  - {value: "Steve Wozniak", relation: collaborator, note: "cofounder; designed the Apple I and II", certainty: 0.7, cites: [{source: S1, locator: "'Founding of Apple'"}], how_known: "Britannica."}
  - {value: "Daniel Kottke", relation: collaborator, note: "Reed friend; fellow India pilgrim; early Apple employee", certainty: 0.5, cites: [{source: S5, locator: "Characters; India"}], how_known: "Isaacson."}

review:
  roster_status_reason: {value: "Provisional in v8 (F 4; four models, not Claude); roster note 'Product/design synthesis; attribution vs. team'.", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 132"}], how_known: "Study roster."}
  controversies:
    - {value: "Attribution of Apple's products to Jobs rather than his engineers", certainty: 0.5, cites: [{source: S4, locator: "roster.csv, rank 132 (note)"}, {source: S1, locator: "'Founding of Apple'"}], how_known: "Roster note; Britannica credits Wozniak with the design."}
  data_quality_flags:
    - "God/system words now from Isaacson primary OCR (S5); page numbers cross-checked with secondary cites (Wiki p.14 Lutheran; common p.570 Coda)."
    - "Isaacson interviews after the span (P1); AGNOS held at 0.5 with BELOW alternative."
  open_questions:
    - "RQ-Y1 closed this pass: AGNOS @0.5 (interview), BELOW alt."
    - "Any own-voice nature-order remark that could open B for a non-scientist (P16) — none found in Isaacson/Stanford/Playboy this pass."
    - "Print page-check Isaacson Simon & Schuster 2011 hardcover for pp. 14–15 and 570 if OCR pagination is disputed."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Steven Levy (Britannica)"
    citation: "Levy, Steven. \"Steve Jobs.\" Encyclopaedia Britannica (updated 29 Sep 2026). https://www.britannica.com/money/Steve-Jobs. Read live 2026-10-19; live re-fetch 2026-10-24 hit Cloudflare — prior read kept."
    url: "https://www.britannica.com/money/Steve-Jobs"
    accessed: 2026-10-19
    reliability_note: "Signed article, fact-checked by the Editors; most recently revised by the Editors. Body cited; question boxes not cited (P26)."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, timing, institutions, collaborators, review]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Steve Jobs"
    citation: "Jobs, Steve. Commencement address, Stanford University, 12 June 2005. Prepared text, \"'You've got to find what you love,' Jobs says\", Stanford Report. https://news.stanford.edu/stories/2005/06/youve-got-find-love-jobs-says (Wayback Machine snapshot 20251219224344)."
    url: "https://news.stanford.edu/stories/2005/06/youve-got-find-love-jobs-says"
    accessed: 2026-10-24
    reliability_note: "His prepared public text, published by the university; read in a Wayback snapshot because the live page refuses the fetch (403). Web copy. Re-verified this deepen pass."
    source_quality: "primary / own words"
    used_for: [childhood, worldview, lane_b]
  - id: S3
    type: secondary
    kind: other
    author: "Peter Whoriskey and Ariana Eunjung Cha"
    citation: "Whoriskey, Peter, and Ariana Eunjung Cha. \"Steve Jobs opens up about adoption, loves, faith in new biography.\" The Washington Post, 21 October 2011."
    url: "https://www.washingtonpost.com/business/economy/steve-jobs-opens-up-about-adoption-loves-faith-in-new-biography/2011/10/21/gIQAMZpu4L_story.html"
    accessed: 2026-10-19
    reliability_note: "Newspaper report quoting Isaacson's biography on release; secondary quotation of S5 — kept for path history, not as independent corroboration (P26, P48)."
    source_quality: "other"
    used_for: [worldview]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, contribution, review]
  - id: S5
    type: primary
    kind: other
    author: "Walter Isaacson (interviewing Steve Jobs)"
    year: 2011
    citation: "Isaacson, Walter. Steve Jobs. New York: Simon & Schuster, 2011. Read in Internet Archive OCR text (item steve-jobs-walter-isaacson_202601; DjVuTXT), 2026-10-24. Print page numbers for childhood religion ~14–15 and Coda ~570 follow Wikipedia/secondary cites of the same edition."
    url: "https://archive.org/details/steve-jobs-walter-isaacson_202601"
    accessed: 2026-10-24
    reliability_note: "Authorized biography based on more than forty interviews with Jobs. His first-person words first published here count under P8 as recorded_interview. OCR line-breaks cleaned when quoting; page numbers cross-checked (Wiki S6: Lutheran p.14; multiple reviews: fifty-fifty p.570)."
    source_quality: "primary / own words"
    used_for: [childhood, worldview, heritage, collaborators, timing]
  - id: S6
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia. \"Steve Jobs.\" https://en.wikipedia.org/wiki/Steve_Jobs (Early life / Family / Infancy sections; API wikitext read 2026-10-24)."
    url: "https://en.wikipedia.org/wiki/Steve_Jobs"
    accessed: 2026-10-24
    reliability_note: "P50 dual bio for identity/heritage facts; cites Isaacson for Lutheran p.14 and adoption. Not used alone for worldview scores."
    source_quality: "reference entry"
    used_for: [identity, basics, childhood, heritage]
---

# Steve Jobs

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Steve Jobs (1955–2011), cofounder of Apple [S1]. Deepen catch-up: primary_system AGNOS @0.5 (interview), alt BELOW_THRESHOLD [S5]; A and D BELOW_THRESHOLD; B, C, E UNKNOWN; mid_basin UNKNOWN. Not plotted.

## Life and work

Apple, NeXT, Pixar, and Apple again from 1997 [S1].

## Contribution and impact

Apple II, Macintosh, iPod, iPhone [S1].

## Childhood and education

Adopted; Reed College dropout [S1; S2]. Adoptive Lutheran Sundays until age 13 (Biafra confrontation); then Zen practice and a 1974 India search [S5].

## Adult working worldview

Isaacson interviews (after the span): doors/house suspension and fifty-fifty on God → AGNOS @0.5 with BELOW alternative [S5]. Stanford 2005 trusts gut/destiny/karma and rejects dogma without scoring a locus [S2]. No nature-order remark for B [S5; S2].

## Heritage (context only)

Biological Swiss-German Catholic-background mother and Syrian Muslim-household father; adoptive German/Armenian Lutheran-practicing home [S5; S6]. Context only.

## Timing

1977–2007, from age 22 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. AGNOS suspension plus Zen lead; A BELOW and B UNKNOWN leave mid UNKNOWN — not plotted [S5; S2].

## Open questions

- RQ-Y1 closed: AGNOS @0.5 (interview), BELOW alt [S5].
- Own-voice nature-order for B still absent [S5; S2].

## Research log

- 2026-10-19: Read Britannica (Levy), the 2005 Stanford address and the Washington Post report on the Isaacson biography.
- 2026-10-24: Deepen catch-up 2/13. Read Isaacson 2011 via IA OCR (S5); re-verified Stanford Wayback (S2); Wikipedia Early life API (S6); Playboy 1985 (allaboutstevejobs) — no God score. RQ-Y1 → AGNOS @0.5. No figures/. Person file only committed.
