---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Q; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-18
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to 20c_early. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-18, by: "Grok Bot", summary: "Record created (stage 3 batch Q, order P32: F 4, rank 100). Basics from Britannica (Carol W. Gelderman, signed; body through the 1914 wage, read live). Worldview from two interviews: William L. Stidger's syndicated interview (Universal Service, printed 4 February 1923; OCR page image text on historyworm.com) and the San Francisco Examiner interview of 26 August 1928 as quoted by The Henry Ford (museum blog). Inventor, not a scientist (P33). primary_system BELOW_THRESHOLD (candidates CHRIST, THEOS); A 1 (0.5, alt 0); B UNKNOWN; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}
    - {date: 2026-10-18, by: "Grok Bot", summary: "Batch Q audit notes (gs_0b3023d_Q run 1). Masthead reasoning added: most likely Hearst's Washington Herald (Universal Service was Hearst's wire; 'Washington Radio Herald' items on the page; the Times-Herald dates from 1939); the running head's '1928' is a slip (4 February 1923 was a Sunday). Creation entry's 'reincarnation belief' aligned to the candidate code THEOS. Values unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #99 / F4 rank 100). Needs: corroborate/lift A; hunt P16 B; inventor not scientist (P33). Dual bio Wikipedia EN (S5, P50). P47 source_quality on S1–S8. Primary checks: Stidger 1923 book Henry Ford: The Man and His Motives (IA OCR, S6) Ch. III 'Ford's Religious Views' — same 'I believe in God and in Jesus Christ' and Gardener design-inference (names Burroughs; newspaper OCR said Muir); Pew Preaches (1930, S7) reprints/elaborates same interviewer chain ('I belong to the Church'); Gutenberg My Life and Work (S8) — 'Nature vetoes' is social-economic natural law vs Soviet decree, not P16 physical order; 'God's great open spaces' is advertising rhetoric. A 1 lifted 0.5→0.7 (recorded_interview ceiling P8) support corroborated (distinct ids S2/S6/S7; same interviewer Stidger noted; contested alt 0 also caps ≤0.7). B stays UNKNOWN (no P16 nature-order/exception own-voice; Gardener off-point). primary BELOW (CHRIST vs THEOS/reincarnation); mid UNKNOWN. Chart-moving NO. Episcopal family/church from S5/S6/S7. Dearborn Independent noted in controversies (not axis-coded). Draft deepen report in drafts/ (untracked). No fallacy_catalog. No figures refresh."}

identity:
  id: ford-henry
  display_name: "Henry Ford"
  roster:
    canonical_name: "Henry Ford"
    rank: 100
    F: 4
    models: [Claude, DeepSeek, GPT, Grok]
    band: "core (3–4)"
    status: core
    field: invention
    field_bucket: "invention / engineering"
  full_name: {value: "Henry Ford", certainty: 1.0, cites: [{source: S1, locator: "title"}, {source: S5, locator: "lead / infobox"}], how_known: "Britannica and Wikipedia agree (P15)."}
  native_name: {value: UNKNOWN, how_known: "English."}
  aliases: []

basics:
  birth:
    date: {value: "1863-07-30", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "header dates; 'Early life'"}, {source: S5, locator: "infobox"}], how_known: "Britannica and Wikipedia agree; born on the family farm near Dearborn."}
    place: {value: "Wayne county, Michigan (family farm near Dearborn)", modern_name: "Dearborn, Michigan, United States", polity_then: "United States", certainty: 1.0, cites: [{source: S1, locator: "'Early life'"}, {source: S5, locator: "Early life"}], how_known: "Britannica and Wikipedia."}
  death:
    date: {value: "1947-04-07", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "header dates"}, {source: S5, locator: "infobox"}], how_known: "Britannica and Wikipedia; age 83."}
    place: {value: "Dearborn, Michigan", modern_name: "Dearborn, Michigan, United States", polity_then: "United States", certainty: 1.0, cites: [{source: S1, locator: "header dates"}, {source: S5, locator: "Death"}], how_known: "Britannica and Wikipedia; funeral at Cathedral Church of St. Paul (S5)."}
  first_lasting_contribution_year: {value: 1908, certainty: 0.7, cites: [{source: S1, locator: "'Early life' (Model T announced October 1908)"}, {source: S5, locator: "Ford Motor Company / Model T"}], how_known: "Model T, announced October 1908; the 1896 Quadricycle is not called lasting in the body read (P23)."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "First lasting year 1908 (P2)."}
  region_of_birth: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}, {source: S5, locator: "infobox"}], how_known: "United States (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}, {source: S5, locator: "Ford Motor Company"}], how_known: "Detroit and Highland Park, Michigan."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S5, locator: "lead"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  occupations: {value: ["industrialist", "engineer", "automobile manufacturer"], certainty: 0.7, cites: [{source: S1, locator: "opening; 'Early life'"}, {source: S5, locator: "lead"}], how_known: "Britannica and Wikipedia."}

contribution:
  era_bucket: 20c_early
  fields: {value: ["automotive engineering", "mass production"], certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "lead / Model T"}], how_known: "Britannica and Wikipedia."}
  lasting_original_contributions:
    - {value: "Model T automobile, 'the ordinary man's utility'", year: 1908, kind: invention, lasting: "'the chief instrument of one of the greatest and most rapid changes in the lives of the common people in history' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}, {source: S5, locator: "Model T"}], how_known: "Britannica and Wikipedia."}
    - {value: "Moving assembly line system at Highland Park (with his engineers)", year: "1913–1914", kind: method, lasting: "'the most advanced production technology yet conceived' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}, {source: S5, locator: "Assembly line"}], how_known: "Britannica ('the system that had evolved by 1913–14'); Wikipedia."}
    - {value: "Five-dollar day and eight-hour shift", year: 1914, kind: method, lasting: "'these innovations changed the very structure of society' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}, {source: S5, locator: "Five-dollar day"}], how_known: "Britannica and Wikipedia."}
  evidence_of_impact:
    - {value: "15,500,000 Model Ts sold in the United States over 19 years", kind: other, certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}
  major_works:
    - {value: "My Life and Work (with Samuel Crowther)", year: 1922, kind: "book", certainty: 0.7, cites: [{source: S8, locator: "title page / Gutenberg"}, {source: S5, locator: "References / Ford & Crowther 1922"}], how_known: "Autobiography co-written with Crowther; Gutenberg text read deepen D1."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1; S5).", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "lead"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Episcopal — father William Ford was warden of the Episcopal church at Dearborn; at about twenty Ford walked miles to 'their Episcopal church' every Sunday", certainty: 0.7, cites: [{source: S6, locator: "Ch. III (father as Episcopal warden)"}, {source: S5, locator: "Early life (Episcopal church at twenty)"}, {source: S7, locator: "'Henry Ford Talks Religion' (belongs to Episcopalian Church in Detroit)"}], how_known: "Stidger 1923 book (S6); Wikipedia Early life (S5); Stidger in Pew Preaches (S7) states adult Episcopal belonging — heritage/affiliation context, not a scored creed."}
  family_religious_practice: {value: "Sunday Episcopal church attendance in young adulthood; father a church warden", certainty: 0.5, cites: [{source: S5, locator: "Early life"}, {source: S6, locator: "Ch. III"}], how_known: "Wikipedia and Stidger 1923."}
  parents_and_household:
    - {value: "One of eight children of William and Mary Ford, farmers near Dearborn", role: parents, certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}, {source: S5, locator: "Early life"}], how_known: "Britannica and Wikipedia."}
  household_circumstances: {value: "Family farm", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}
  schooling:
    - {value: "One-room school for eight years", stage: "elementary school", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}
    - {value: "Detroit machine shops from 16", stage: apprenticeship, run_by: other, certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  notable_events:
    - {value: "Walked to Detroit to work in machine shops", year: 1879, certainty: 0.7, cites: [{source: S1, locator: "opening ('left his father's farm in 1879')"}], how_known: "Britannica."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1908–1914", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "'I was brought up in the church'; Pew Preaches (same interviewer): belongs to the Episcopalian Church in Detroit", certainty: 0.5, cites: [{source: S2, locator: "column 1"}, {source: S6, locator: "Ch. III"}, {source: S7, locator: "'Henry Ford Talks Religion'"}], how_known: "(interview) Stidger chain; denomination named in S7, not in the 1923 newspaper OCR."}
    - {value: "Freemason (Palestine Lodge No. 357, Detroit, raised 1894; 33rd degree Scottish Rite 1940)", certainty: 0.5, cites: [{source: S5, locator: "Personal interests"}], how_known: "Wikipedia citing Grand Lodge of New York; affiliation context only — not a scored A/B system."}
  self_described_science_religion_relation: {value: "Religion is 'like electricity': he does not understand it but sees its results", certainty: 0.5, cites: [{source: S2, locator: "'Reaction electric'"}, {source: S6, locator: "Ch. III"}, {source: S7, locator: "'Henry Ford Talks Religion'"}], how_known: "(interview) Stidger chain, 1923/1930; OCR / archive scan."}
  primary_system:
    value: BELOW_THRESHOLD
    basis: recorded_interview
    cites: [{source: S2, locator: "column 1; closing paragraph"}, {source: S6, locator: "Ch. III"}, {source: S3, locator: "quoted interview"}]
    how_known: "(interview) Two interview clusters point different ways: 'I believe in God and in Jesus Christ' (1923 Stidger, checked in S6 book OCR) against 'I adopted the theory of Reincarnation when I was twenty six. Religion offered nothing to the point' (1928; The Henry Ford). Candidates CHRIST and THEOS; no system file fits a Christian with a reincarnation belief. Stidger 1923 book also notes reincarnation as an 'eccentricity' he will admit when questioned. Neither interview is a page-image facsimile of the newspaper/Examiner (P19)."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "'I believe in God and in Jesus Christ' (1923); Sermon on the Mount as industrial constitution (S6/S7); Episcopal belonging (S7)."}
    - {code: THEOS, reason: "Reincarnation as 'a universal plan' (1928 S3; Marquis via S5; Stidger S6 eccentricity chapter); coder's nearest neighbour, not named by him."}
  lio_axes:
    A_locus:
      value: 1
      basis: recorded_interview
      certainty: 0.7
      support: corroborated
      cites: [{source: S6, locator: "Ch. III 'Ford's Religious Views'"}, {source: S2, locator: "column 1; closing paragraph"}, {source: S7, locator: "'Henry Ford Talks Religion'"}]
      rationale: "A maker distinct from his work: 'I believe in God and in Jesus Christ', and the Gardener design-inference — of John Burroughs (S6/S7; newspaper OCR S2 said Muir), 'There must be a Gardener, you know, for all this beauty' / 'If there is a Garden, there is always a Gardener'. Features of the transcendent pole present but limited: nothing on God's acting in events. Named alternative 0 (a personal God, from 'I believe in God and in Jesus Christ' and Episcopal belonging)."
      how_known: "(interview) Distinct source ids S6 (1923 book OCR), S2 (1923 newspaper OCR), S7 (1930 Pew Preaches OCR) → corroborated (P48 mechanical). Same interviewer (Stidger) across all three — noted, but ids differ. Certainty 0.7 = recorded_interview ceiling (P8); contested alt 0 also caps ≤0.7 (P25). Not facsimile of the newspaper page."
      alternatives:
        - {value: 0, note: "Personal Christian God ('I believe in God and in Jesus Christ'; Episcopal belonging in S7).", cites: [{source: S6, locator: "Ch. III"}, {source: S2, locator: "column 1"}, {source: S7, locator: "'Henry Ford Talks Religion'"}]}
    B_cause: {value: UNKNOWN, how_known: "(interview / autobiography) Inventor, not a scientist (P33: a device is not a theory or result); no statement of his about nature's physical order or exceptions in the sources read (P16). The Gardener remark concerns nature's origin and beauty, not law or exception (off-point, P19). My Life and Work 'Nature vetoes' those [social] laws (S8) is social-economic natural law vs Soviet decree, not P16 physical order. 'Masters of Nature' / work-as-natural-course language likewise off-point."}
    C_ledger: {value: UNKNOWN, how_known: "(interview) Reincarnation ('the experience we collect in one life in the next') bears on C; not scored at this reading (coder's call)."}
    D_authority: {value: UNKNOWN, how_known: "Nothing scored; Sermon-on-the-Mount-as-industrial-constitution (S6/S7) is ethics/practice, not a D ranking of revelation vs reason."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7)."}
  mid_basin: {value: UNKNOWN, how_known: "B_cause is UNKNOWN (§6, P19). A 1 @0.7 alone cannot darken mid-basin."}
  statements:
    - text: "I believe in God and in Jesus Christ. I was brought up in the church."
      cites: [{source: S6, locator: "Ch. III pp. 34–35 (IA OCR)"}, {source: S2, locator: "column 1"}, {source: S7, locator: "'Henry Ford Talks Religion' pp. 42–43"}]
      date: "1923-02-04"
      context: "William L. Stidger (pastor, St. Mark's Methodist Church, Detroit), syndicated Universal Service interview, datelined Detroit 3 February 1923; newspaper page 4 February 1923. Book form in Stidger, Henry Ford: The Man and His Motives (1923), Ch. III. Pew Preaches (1930) elaborates: 'I belong to the Church. I attend Church.'"
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Deepen D1: checked against IA OCR of Stidger 1923 book (S6) and Pew Preaches (S7); newspaper OCR (S2) agrees. Facsimile of the newspaper page still open. Same interviewer across S2/S6/S7 noted; distinct source ids still yield corroborated under P48 mechanical rule."
    - text: "No, Mr. Burroughs didn't seem to find the Gardener. It's too bad. There must be a Gardener, you know, for all this beauty."
      cites: [{source: S6, locator: "Ch. III closing (IA OCR)"}, {source: S7, locator: "'Henry Ford Talks Religion' (Burroughs / Gardener)"}, {source: S2, locator: "closing paragraph (OCR reads Muir)"}]
      date: "1923-02-04"
      context: "Same Stidger interview, replying to Bishop Quayle's remark that John Burroughs 'knew the Garden but he never found the Gardener.' Book and Pew Preaches name Burroughs (Ford's friend); newspaper OCR (S2) reads Muir — prefer book reading."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Deepen D1: S6/S7 Burroughs preferred over S2 Muir OCR. Design inference to a Gardener distinct from the garden → A 1. Off-point for B (P16)."
    - text: "Religion is like electricity. I do not understand electricity, but I am greatly interested in it. … I see its results even though I do not understand it. That is about the way I feel about religion."
      cites: [{source: S6, locator: "Ch. III"}, {source: S7, locator: "'Henry Ford Talks Religion'"}, {source: S2, locator: "'Reaction electric'"}]
      date: "1923-02-04"
      context: "Same Stidger interview; self-described science/religion analogy."
      axes: []
      kind: "recorded interview"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Context for self_described_science_religion_relation; not scored on A/B."
    - text: "It's all in the Sermon on the Mount. You can take that, put it into industry anywhere and it will work. … That Sermon on the Mount is action."
      cites: [{source: S6, locator: "Ch. III"}, {source: S7, locator: "'Henry Ford Talks Religion'"}]
      date: "1923"
      context: "Stidger interviews; industrial ethics claim."
      axes: []
      kind: "recorded interview"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Ethics/practice; not used to score D or primary_system alone."
    - text: "I adopted the theory of Reincarnation when I was twenty six. Religion offered nothing to the point. Even work could not give me complete satisfaction. Work is futile if we cannot utilise [sic] the experience we collect in one life in the next."
      cites: [{source: S3, locator: "quoted interview"}]
      date: "1928-08-26"
      context: "San Francisco Examiner interview, 26 August 1928, as quoted by The Henry Ford (Patrice Fisher, 2015). Stidger 1923 (S6) independently notes reincarnation as an eccentricity Ford will admit when questioned closely. Marquis 1923 (via S5) claimed he believed or 'once believed'."
      axes: [C_ledger]
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-18
      note: "Museum blog quotation; the '[sic]' is the blog's; Examiner facsimile still pending. Stidger S6 corroborates belief-in-reincarnation as a fact about him without giving this wording."
    - text: "While men may decree social laws in conflict with natural laws, Nature vetoes those laws more ruthlessly than did the Czars. Nature has vetoed the whole Soviet Republic."
      cites: [{source: S8, locator: "Ch. I / early chapters (Gutenberg)"}]
      date: "1922"
      context: "My Life and Work; argument against Soviet social engineering."
      axes: []
      kind: "autobiography"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Social-economic 'natural laws' vs decree — off-point for P16 physical nature-order (B). Recorded to document the B hunt and the rejection of this line as a B score."
  changes_over_life:
    - {value: "Adopted reincarnation at about 26 (c. 1889), by his own 1928 account", certainty: 0.5, cites: [{source: S3, locator: "quoted interview"}], how_known: "(interview) Before the span; does not split it (P31)."}
  coder_notes: "Deepen D1. A cites distinct ids S2/S6/S7 (Stidger newspaper, 1923 book, Pew Preaches) → support corroborated (P48); same interviewer noted. Certainty 0.7 recorded_interview ceiling with contested alt 0. B silence honest: inventor P33; MLAW Nature-vetoes and Gardener are off-point for P16. primary stays BELOW (CHRIST vs THEOS). Antisemitic Dearborn Independent campaign noted in controversies — not coded on LIO axes. Britannica question boxes not cited (P26)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "American, Michigan farm family (father William of Irish descent per common bios)", certainty: 0.5, cites: [{source: S1, locator: "'Early life'"}, {source: S5, locator: "Early life"}], how_known: "Britannica farm family; Wikipedia Early life for parental detail."}
  religious_heritage_by_birth: {value: "Episcopal (family church; father a warden)", certainty: 0.7, cites: [{source: S6, locator: "Ch. III"}, {source: S5, locator: "Early life"}], how_known: "Stidger 1923 and Wikipedia; context only."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1908–1914", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Model T (1908) to the assembly line and five-dollar day (1913–14) (P30)."}
  age_at_first_lasting_contribution: {value: 45, certainty: 0.7, cites: [{source: S1, locator: "header dates; 'Early life'"}], how_known: "1908 − 1863 = 45 (P30)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No axis scored at 3 or 4 (P27 anchor). A 1 is not LIO-type for this field."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", rationale: "A 1 @0.7; B UNKNOWN; nothing else scored.", certainty: 0.5, cites: [{source: S6, locator: "Ch. III"}], how_known: "Coder's reading."}
  worldview_during_major_work: {value: BELOW_THRESHOLD, how_known: "As primary_system."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Not read as a geometric-form claim.", certainty: 0.5, cites: [{source: S1, locator: "'Early life'"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "'Early life'"}], how_known: "Not read."}
  circle_present: {value: "unclear", rationale: "Reincarnation as a 'universal plan' (1928) — Lane B lead only.", certainty: 0.5, cites: [{source: S3, locator: "quoted interview"}], how_known: "Coder's reading."}
  reading: "Lane B only: designer-Gardener God (A 1) plus reincarnation 'plan' from interviews; Episcopal heritage and Freemason affiliation are context."
  notes: "Do not treat inventor mastery-of-nature rhetoric as P16 B."

institutions:
  - {value: "Detroit Edison Company", role: "chief engineer", years: "1893–", kind: commercial, certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}, {source: S5, locator: "Early career"}], how_known: "Britannica and Wikipedia."}
  - {value: "Ford Motor Company", role: founder, years: "1903–", kind: commercial, certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}, {source: S5, locator: "Ford Motor Company"}], how_known: "Britannica and Wikipedia."}
collaborators: []

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 100"}], how_known: "Study roster."}
  controversies:
    - {value: "Antisemitic Dearborn Independent campaign and The International Jew (1920s); later public apology/retraction narratives contested by historians", certainty: 0.7, cites: [{source: S5, locator: "Antisemitism and The Dearborn Independent"}], how_known: "Wikipedia section; noted for honesty — not used to score LIO axes or primary_system."}
  data_quality_flags:
    - "The 1923 interview is now checked in Stidger's 1923 book OCR (S6) and Pew Preaches 1930 (S7); newspaper page facsimile (S2) still open; Muir vs Burroughs name variance resolved toward book."
    - "The 1928 Examiner reincarnation interview is still museum-blog quotation (S3), not facsimile."
    - "Only the first part of Britannica's article (through 1914) was returned on create; Wikipedia dual bio (S5) supplies later basics."
    - "Marquis 1923 Henry Ford: An Interpretation borrow-restricted on IA this pass — reincarnation claim via Wikipedia only."
  open_questions:
    - "Facsimile of Universal Service / Washington Herald 1923-02-04 and SF Examiner 1928-08-26; Benson Ford Research Center religion files; Marquis 1923 page-check if borrow opens."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Carol W. Gelderman"
    citation: "Gelderman, Carol W. \"Henry Ford.\" Encyclopaedia Britannica (updated 29 September 2026). https://www.britannica.com/biography/Henry-Ford. Read live 2026-10-18 (the Wayback Machine was rate-limiting); the fetch returned the introduction and 'Early life'. Deepen D1 2026-10-24: body retained; dual bio with S5."
    url: "https://www.britannica.com/biography/Henry-Ford"
    accessed: 2026-10-18
    source_quality: "reference entry"
    reliability_note: "Signed article. Body only; question boxes not cited (P26)."
    used_for: [identity, basics, contribution, childhood, heritage, timing, institutions]
  - id: S2
    type: secondary
    kind: other
    author: "William L. Stidger (Universal Service), via historyworm.com"
    citation: "Stidger, William L. \"Ford Affirms Faith in God.\" Universal Service, Detroit, 3 February 1923; newspaper page of 4 February 1923, p. 10, OCR text at https://www.historyworm.com/gazete/washington_post/1923-02-04/10"
    url: "https://www.historyworm.com/gazete/washington_post/1923-02-04/10"
    accessed: 2026-10-18
    source_quality: "newspaper interview"
    reliability_note: "OCR of a newspaper page; first-person quotations reported by the interviewer. Same interviewer as S6/S7 (noted); distinct id from S6/S7 for P48."
    used_for: [worldview, timing]
  - id: S3
    type: secondary
    kind: "institutional page"
    author: "Patrice Fisher (The Henry Ford)"
    citation: "Fisher, Patrice. \"Henry Ford and Reincarnation.\" The Henry Ford, 13 August 2015. https://www.thehenryford.org/collections/explore/articles/henry-ford-and-reincarnation"
    url: "https://www.thehenryford.org/collections/explore/articles/henry-ford-and-reincarnation"
    accessed: 2026-10-18
    source_quality: "unofficial web copy"
    reliability_note: "Museum blog quoting the 1928 Examiner interview; secondary quotation. Examiner facsimile pending."
    used_for: [worldview, lane_b]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-18
    source_quality: "study roster"
    reliability_note: "Study's own roster."
    used_for: [identity, review]
  - id: S5
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia contributors. \"Henry Ford.\" Wikipedia. https://en.wikipedia.org/wiki/Henry_Ford. Dual bio (P50). Read 2026-10-24 (Early life Episcopal; Personal interests Freemason / Marquis reincarnation; Antisemitism and The Dearborn Independent)."
    url: "https://en.wikipedia.org/wiki/Henry_Ford"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Used for dual-bio basics, Episcopal church at twenty, Freemasonry, Marquis reincarnation claim, Dearborn Independent controversy note. Worldview A/B scoring does not rest on Wikipedia paraphrases alone."
    used_for: [identity, basics, contribution, childhood, heritage, institutions, review, worldview]
  - id: S6
    type: secondary
    kind: other
    author: "William L. Stidger"
    citation: "Stidger, William L. Henry Ford: The Man and His Motives. New York: George H. Doran, 1923. Internet Archive OCR: https://archive.org/details/henryfordmanhism0000will (Ch. III 'Ford's Religious Views'; reincarnation noted among eccentricities)."
    url: "https://archive.org/details/henryfordmanhism0000will"
    accessed: 2026-10-24
    source_quality: "archive scan (OCR only)"
    reliability_note: "Interviewer's own 1923 book; OCR of scan. Best available check of the 1923 God/Jesus and Gardener lines. Same interviewer as S2/S7 (noted); distinct id contributes to A corroborated (P48)."
    used_for: [worldview, childhood, heritage, timing]
  - id: S7
    type: secondary
    kind: other
    author: "William L. Stidger"
    citation: "Stidger, William L. \"Henry Ford Talks Religion.\" In The Pew Preaches, 1930. Internet Archive OCR. Same interviewer; elaborates Episcopal belonging and Sermon on the Mount."
    url: "https://archive.org/details/pewpreaches00stid"
    accessed: 2026-10-24
    source_quality: "archive scan (OCR only)"
    reliability_note: "Later Stidger reprint/elaboration of the same interview relationship (noted); distinct id from S2/S6 for P48."
    used_for: [worldview, childhood]
  - id: S8
    type: primary
    kind: "published work by the subject"
    author: "Henry Ford (with Samuel Crowther)"
    citation: "Ford, Henry, with Samuel Crowther. My Life and Work. Garden City, NY: Doubleday, Page & Co., 1922. Project Gutenberg transcription. https://www.gutenberg.org/ebooks/7213"
    url: "https://www.gutenberg.org/ebooks/7213"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "Autobiography; Crowther as collaborator. Used for B hunt (Nature vetoes = social-economic, off-point P16) and major_works. Antisemitic 'Christian America' passages in later chapters noted but not used to score A."
    used_for: [contribution, worldview]
---

# Henry Ford

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Henry Ford (1863–1947), American industrialist [S1; S5]. Deepen D1: primary_system BELOW_THRESHOLD (CHRIST vs THEOS); A 1 at 0.7 support corroborated (alt 0); B UNKNOWN; mid_basin UNKNOWN. Not plotted. Chart-moving NO.

## Life and work

Dearborn farm, Detroit machine shops, Edison Company, Ford Motor Company (1903) [S1; S5]. Autobiography *My Life and Work* (1922) [S8].

## Contribution and impact

Model T (1908); moving assembly line (1913–14); five-dollar day (1914) [S1; S5].

## Childhood and education

One-room school; machine shops at 16 [S1]. Episcopal family church; father a warden [S6; S5].

## Adult working worldview

'I believe in God and in Jesus Christ' and Gardener design-inference (1923 Stidger; book OCR S6) [S2; S6; S7]; reincarnation (1928) [S3]. No P16 B in MLAW or interviews [S8].

## Heritage (context only)

Michigan farm family; Episcopal heritage [S1; S5; S6].

## Timing

1908–1914 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Designer-Gardener and reincarnation 'plan' [S6; S3]. Inventor mastery rhetoric is not P16 B.

## Open questions

- Facsimile checks of 1923 newspaper and 1928 Examiner; Marquis 1923 if borrow opens.

## Research log

- 2026-10-18: Read Britannica (live), the 1923 interview OCR page and The Henry Ford's blog.
- 2026-10-24: Deepen D1 — Stidger 1923 book OCR (IA), Pew Preaches 1930 OCR, Gutenberg MLAW, Wikipedia dual bio; A lift 0.5→0.7 single; B UNKNOWN kept; person-file-only commit.
