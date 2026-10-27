---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 4
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Y)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to 20c_late. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #133, F4 rank 136). Opened primary self-labels: Nation Institute abridged transcript (The Nation, 6 May 2004) — 'Now, you know, I'm a Catholic, right' (S5); VIBE May 1998 (S6) — 'I'm a Catholic' / 'ended up nowhere' / 'deeply religious person'; Antonio Monda Do You Believe? (2007, S7) — 'intelligence interested in what exists' / order-and-harmony (quotes checked via Ron Slate 2008 and SF Bay Guardian 2007 excerpts). Y2 path met: primary_system BELOW_THRESHOLD → CHRIST @0.5 (interview; after span P1/P20; alt BELOW — U2 membership concern, VIBE 'ended up nowhere', Monda religions-reduce-God). A_locus BELOW → 1 @0.5 (Monda transcendent intelligence; support single). B stays BELOW (order/harmony leans 3 but P16 no exception). C/E UNKNOWN; D BELOW; mid BELOW. Still not plotted. P47 on S1–S8; P50 Wikipedia EN (S8) dual bio; parents Ramah/George named. Prefer Nation/VIBE/Monda over Ripatrazone. No fallacy_catalog; no figures/. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Ruling Y2 (v8's call on the auditor's advice, batch Y audit gs_7b46f24_Y run 1): primary_system stays BELOW_THRESHOLD, CHRIST the lead (recorded under P43, beside V3). No score changes."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Y, order P32: F 4, rank 136; Thomas Aquinas, rank 135, already coded). Basics from Britannica (Britannica Editors, 12 Oct 2026). Own voice read in the NPR Fresh Air transcript (20 April 2015, after the span): raised in her mother's AME church, Catholic from 12, 'took it seriously for years and years and years', now 'Not a structured one'. Other statements only as Nick Ripatrazone's secondary quotations (Lit Hub, 2020). Not a scientist. Span 1970–1987 at 0.7 (The Bluest Eye to Beloved). primary_system BELOW_THRESHOLD (CHRIST lead; RQ-Y2); A, B, D BELOW_THRESHOLD with readings named; C, E UNKNOWN; mid_basin BELOW_THRESHOLD. Not plotted. Draft, not reviewed."}

identity:
  id: morrison-toni
  display_name: "Toni Morrison"
  roster:
    canonical_name: "Toni Morrison"
    rank: 136
    F: 4
    models: [Claude, Gemini, GPT, Grok]
    band: "core (3–4)"
    status: core
    field: literature
    field_bucket: literature
  full_name: {value: "Chloe Ardelia Wofford (baptismal name Anthony; married name Morrison)", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts; 'Early life and education'"}], how_known: "Britannica: original name Chloe Ardelia Wofford; baptismal name Anthony; 'Toni' a nickname from Howard; married Harold Morrison in 1958."}
  native_name: {value: "Toni Morrison", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Pen name as published."}
  aliases:
    - {name: "Morrison-Toni", kind: "roster alias"}
    - {name: "Toni-Morrison", kind: "roster alias"}
    - {name: "Chloe Ardelia Wofford", kind: "birth name"}
    - {name: "Chloe Anthony Wofford", kind: "religious name"}

basics:
  birth:
    date: {value: "1931-02-18", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "Quick Facts; opening"}, {source: S8, locator: "infobox (18 February 1931)"}], how_known: "Britannica; Wikipedia EN agrees (P50)."}
    place: {value: "Lorain, Ohio", modern_name: "Lorain, Ohio, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}, {source: S8, locator: "infobox / Early years"}], how_known: "Britannica; Wikipedia EN agrees (P50)."}
  death:
    date: {value: "2019-08-05", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "Quick Facts; opening"}, {source: S8, locator: "infobox (5 August 2019)"}], how_known: "Britannica; Wikipedia EN agrees (P50)."}
    place: {value: "Bronx, New York", modern_name: "Bronx, New York City, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}, {source: S8, locator: "Death (Montefiore Medical Center, The Bronx)"}], how_known: "Britannica; Wikipedia EN agrees (P50)."}
  first_lasting_contribution_year: {value: 1970, certainty: 0.7, cites: [{source: S1, locator: "'The Bluest Eye'"}], how_known: "The Bluest Eye (1970), her first book, praised for 'a prose so precise ... that the novel becomes poetry' (S1)."}
  era_bucket: {value: "1950 on", certainty: 1.0, cites: [{source: S1, locator: "'The Bluest Eye'"}], how_known: "From 1970 (P2)."}
  region_of_birth: {value: "North America", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}], how_known: "United States (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "'Editing and teaching career'"}], how_known: "New York, Albany, Princeton."}
  sex_as_recorded: {value: "female", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
  occupations: {value: ["novelist", "editor at Random House", "professor (SUNY Albany; Princeton)"], certainty: 0.7, cites: [{source: S1, locator: "'Editing and teaching career'"}], how_known: "Britannica."}

contribution:
  era_bucket: 20c_late
  fields: {value: ["novel", "literary criticism"], certainty: 0.7, cites: [{source: S1, locator: "opening; 'Nonfiction works'"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "The Bluest Eye", year: 1970, kind: work, lasting: "praised by The New York Times as prose that 'becomes poetry' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'The Bluest Eye'"}], how_known: "Britannica."}
    - {value: "Song of Solomon", year: 1977, kind: work, lasting: "'brought Morrison to national attention'; National Book Critics Circle Award (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Sula, Song of Solomon, and Tar Baby'"}], how_known: "Britannica."}
    - {value: "Beloved", year: 1987, kind: work, lasting: "Pulitzer Prize; 'came to be regarded as a masterpiece of American literature' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Beloved'"}], how_known: "Britannica. Latest item the body calls lasting, so it ends the span (P30 addendum b)."}
  evidence_of_impact:
    - {value: "Nobel Prize in Literature (1993), the first Black woman so honoured", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Nobel Prize'"}], how_known: "Britannica."}
    - {value: "Presidential Medal of Freedom (2012)", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "'Legacy'"}], how_known: "Britannica."}
  major_works:
    - {value: "Sula", year: 1973, kind: book, certainty: 0.7, cites: [{source: S1, locator: "'Sula, Song of Solomon, and Tar Baby'"}], how_known: "Britannica."}
    - {value: "Jazz", year: 1992, kind: book, certainty: 0.7, cites: [{source: S1, locator: "'Nobel Prize'"}], how_known: "Britannica."}
    - {value: "Playing in the Dark: Whiteness and the Literary Imagination", year: 1992, kind: book, certainty: 0.7, cites: [{source: S1, locator: "'Nonfiction works and children's books'"}], how_known: "Britannica."}
    - {value: "Paradise", year: 1998, kind: book, certainty: 0.7, cites: [{source: S1, locator: "'Later novels'"}], how_known: "Britannica."}
  honours:
    - {value: "Pulitzer Prize for Fiction (Beloved)", year: 1988, certainty: 0.5, cites: [{source: S1, locator: "'Beloved'"}], how_known: "Britannica names the prize but not its year; 1988 is the coder's."}
    - {value: "Nobel Prize in Literature", year: 1993, certainty: 0.7, cites: [{source: S1, locator: "'Nobel Prize'"}], how_known: "Britannica."}
  definition_fit: {value: "clearly meets", rationale: "'Considered one of the greatest contemporary American novelists' (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "African Methodist Episcopal (her mother's church)", certainty: 0.7, cites: [{source: S2, locator: "Bible question ('African Methodist Episcopal, the AME church she belonged to')"}, {source: S3, locator: "conversion paragraph"}], how_known: "Her own words (2015) and Ripatrazone ('a devout member of the African Methodist Episcopal Church')."}
  family_religious_practice: {value: "Mother devout and a church singer; 'everybody read the Bible'; the lessons 'were like fairytales to me'", certainty: 0.7, cites: [{source: S2, locator: "Bible question"}], how_known: "Her own words (2015)."}
  parents_and_household:
    - {value: "Mother Ramah (née Willis) Wofford — homemaker; devout member of the African Methodist Episcopal Church; 'the most beautiful voice'", role: mother, certainty: 0.7, cites: [{source: S2, locator: "Bible question"}, {source: S8, locator: "Early years (Ramah née Willis)"}, {source: S3, locator: "conversion paragraph"}], how_known: "Her own words (2015); Wikipedia EN names Ramah Willis; Ripatrazone secondary."}
    - {value: "Father George Wofford — welder (U.S. Steel); grew up in Cartersville, Georgia; traumatized by a lynching he witnessed as a youth", role: father, certainty: 0.7, cites: [{source: S8, locator: "Early years (George Wofford)"}], how_known: "Wikipedia EN (P50 dual bio with Britannica household sketch)."}
    - {value: "A wing of the family Catholic, including a cousin she was very close to", role: family, certainty: 0.7, cites: [{source: S2, locator: "name question"}], how_known: "Her own words."}
  household_circumstances: {value: "A family with 'an intense love of and appreciation for Black culture'; storytelling, songs and folktales", certainty: 0.7, cites: [{source: S1, locator: "'Early life and education'"}], how_known: "Britannica."}
  schooling:
    - {value: "Hawthorne Junior High School, Lorain, Ohio", stage: "grammar or secondary school", run_by: "state or municipal", years: "c. 1943", certainty: 0.5, cites: [{source: S3, locator: "conversion paragraph"}], how_known: "Ripatrazone names the school at her conversion; run_by the coder's reading."}
    - {value: "Howard University, Washington, D.C. (BA English, 1953)", stage: university, run_by: private, years: "to 1953", certainty: 0.7, cites: [{source: S1, locator: "'Early life and education'"}], how_known: "Britannica."}
    - {value: "Cornell University (MA, 1955)", stage: university, run_by: private, years: "1953–1955", certainty: 0.7, cites: [{source: S1, locator: "'Early life and education'"}], how_known: "Britannica."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  notable_events:
    - {value: "Converted to Roman Catholicism at 12, taking the baptismal name Anthony after St. Anthony of Padua", year: 1943, certainty: 1.0, cites: [{source: S1, locator: "'Early life and education'"}, {source: S3, locator: "conversion paragraph ('in 1943')"}], how_known: "Britannica gives the age and the name; Ripatrazone gives 1943; her own account of the baptism and the Catholic cousin is in S2."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1970–1987", certainty: 0.7, cites: [{source: S1, locator: "'The Bluest Eye'; 'Beloved'"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Roman Catholic from 1943 (baptism); by 2015 'Not a structured' religion, though 'easily seduced' back to church by Pope Francis", certainty: 0.7, cites: [{source: S1, locator: "'Early life and education'"}, {source: S2, locator: "Bible question"}], how_known: "Britannica and her own words (2015). Membership, not a code."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing read on science and religion."}
  primary_system:
    value: CHRIST
    basis: recorded_interview
    certainty: 0.5
    rationale: "Y2 path met. First-person self-labels in primary transcripts: 'Now, you know, I'm a Catholic, right' (Nation Institute conversation with Cornel West, abridged in The Nation, 2004, S5); 'I'm a Catholic, and I have been very much involved in my mother's church, which is AME' (VIBE, May 1998, S6). NPR 2015 adds childhood conversion aesthetics then 'took it seriously for years and years and years' (S2). Branch: Roman Catholic (baptism 1943). Named alternative BELOW_THRESHOLD: CHRIST do_not_use_when / U2 — membership/self-label without Christ/scripture/creed profession; VIBE also 'ended up nowhere' between Catholicism and Protestantism; Monda 2007 (S7) affirms an 'intelligence' God while saying every religion 'reduces' him — idiosyncratic, not creedal CHRIST. All scored own-voice after the 1970–1987 span (P1/P20 → 0.5)."
    how_known: "(interview) Primary Nation (S5) + VIBE (S6) self-labels; NPR seriousness retrospective (S2). After span → 0.5. Ripatrazone (S3) demoted to corroborating secondary only."
    cites: [{source: S5, locator: "Passion of the Christ exchange ('I'm a Catholic, right')"}, {source: S6, locator: "'Are you religious?' answer"}, {source: S2, locator: "Bible question ('took it seriously for years')"}]
  secondary_system: {value: UNKNOWN, how_known: "None scored. Monda's intelligence-without-creed language is a CHRIST alternative reading, not a second code."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Scored @0.5: primary Catholic self-labels (S5, S6); Y2 path met. Named alt BELOW_THRESHOLD (not a system code): U2 membership vs belief; VIBE 'ended up nowhere'; Monda reducing-religion God."}
    - {code: DEISM, reason: "Rejected for primary: Monda order/intelligence language lacks P27 rejection of revelation (Bible 'necessarily inspirational', S2; 'marvelous book', S7)."}
  lio_axes:
    A_locus:
      value: 1
      basis: recorded_interview
      certainty: 0.5
      support: single
      rationale: "Monda (2007, S7): 'I believe in an intelligence interested in what exists and respectful of what is created'; when she thinks of 'the infiniteness of time' she senses 'the order and harmony that suggest an intelligence'. Transcendent intelligence distinct from the world (A toward 0), not clearly a personal intervenor — leans 1. Named alternative BELOW_THRESHOLD if the intelligence language is read as too thin for a locus score. After span → 0.5 (P1/P20)."
      cites: [{source: S7, locator: "Monda interview: intelligence / order and harmony (via Ron Slate 2008 and SF Bay Guardian 28 Nov 2007 excerpts of Do You Believe?)"}]
      how_known: "(interview) Primary interview book words, excerpt-checked; single source id → support single (P48). Ripatrazone (S3) secondary only."
    B_cause: {value: BELOW_THRESHOLD, how_known: "Not a scientist. Monda 'order and harmony that suggest an intelligence' (S7) leans to a lawful order (reading 3) but names no exception or its absence (P16). Stay BELOW; do not overclaim B 3."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read on reward and punishment of persons in her own view (P19); her novels' ghosts and preachers are characters (P42)."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "Lead from her own words (2015, after the span): she approaches the Bible 'as a scholar' because 'it's gone through so many hands, so many translations. Even the people who were writing it ... the scribes, were changing things' (S2): scripture as a human-transmitted text, a reading toward 3. But she calls it 'necessarily inspirational' in the same breath, and says nothing on revelation against observation. Monda (S7) calls the Bible 'marvelous' yet 'small and reductive' — still not a scored D."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7, P19)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A scored only at 0.5; B BELOW_THRESHOLD — mid-basin needs both at ≥0.7 (P4). Still not plotted."}
  statements:
    - text: "So at an early age I moved into this other religion and was perfectly content with its aesthetics. That's shallow, I understand (laughter). But that's what it was, until I grew up a little older and began to take it seriously and then - took it seriously for years and years and years."
      cites: [{source: S2, locator: "Bible question"}]
      date: "2015"
      context: "Fresh Air with Terry Gross, on God Help the Child; asked if there is any religion in her life now: 'Not a structured one.'"
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "NPR's transcript (web copy). After the span (P1)."
    - text: "I think as a scholar that it's necessarily inspirational because it's gone through so many hands, so many translations. Even the people who were writing it, you know, the scribes, were changing things, numbers changed."
      cites: [{source: S2, locator: "Bible question"}]
      date: "2015"
      context: "Same interview, on how she reads the Bible now."
      axes: [D_authority]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "As above."
    - text: "Now, you know, I'm a Catholic, right, so we're used to images of blood and gore."
      cites: [{source: S5, locator: "Passion of the Christ exchange"}]
      date: "2004-03-24"
      context: "Nation Institute conversation with Cornel West (NY Society for Ethical Culture); abridged in The Nation, 6 May 2004. On Mel Gibson's The Passion of the Christ."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Y2 path source. After the span (P1). Ripatrazone's longer Protestant-cross paraphrase not used — Nation text preferred."
    - text: "I'm a Catholic, and I have been very much involved in my mother's church, which is AME. And so I have always gone back and forth between Catholicism and Protestantism. And, I guess. ended up nowhere—except I feel nevertheless as though I am a deeply religious person."
      cites: [{source: S6, locator: "'Are you religious?'"}]
      date: "1998"
      context: "VIBE magazine interview by Robert Morales (May 1998 issue)."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "After the span (P1). Self-label plus 'ended up nowhere' — named in CHRIST alt BELOW."
    - text: "I believe in an intelligence interested in what exists and respectful of what is created."
      cites: [{source: S7, locator: "Monda: attitude toward God"}]
      date: "2007"
      context: "Antonio Monda, Do You Believe? Conversations on God and Religion (Vintage, 2007)."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Book unread this pass; sentence checked in Ron Slate's 6 Jan 2008 review excerpt of the same interview. After the span (P1)."
    - text: "I sense the order and harmony that suggest an intelligence, and I discover, with a slight shiver, that my own language becomes evangelical."
      cites: [{source: S7, locator: "Monda: infiniteness of time / order and harmony"}]
      date: "2007"
      context: "Same Monda interview; pressed about belief in an intelligent entity."
      axes: [A_locus, B_cause]
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Checked in SF Bay Guardian 28 Nov 2007 review excerpt. Used for A; B stays BELOW (P16). After the span."
  changes_over_life:
    - {value: "From content with Catholicism's aesthetics, to taking it 'seriously for years and years and years', to Catholic self-labels still used in 1998–2004, to 'Not a structured' religion by 2015 (though 'easily seduced' by Pope Francis)", certainty: 0.5, cites: [{source: S2, locator: "Bible question"}, {source: S5, locator: "I'm a Catholic"}, {source: S6, locator: "I'm a Catholic / ended up nowhere"}], how_known: "Her own words across interviews; stage years undated."}
  coder_notes: "Deepen D1 2026-10-24: Y2 path met via Nation primary (S5) + VIBE (S6). CHRIST @0.5 after-span; A 1 @0.5 from Monda (S7); B/C/D/E/mid unchanged in plot status (B still BELOW). Characters unused (P42). Prefer Nation/VIBE/Monda over Ripatrazone. Span still 1970–1987. No fallacy_catalog; figures not refreshed."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "African American", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Protestant (African Methodist Episcopal)", certainty: 0.7, cites: [{source: S2, locator: "Bible question"}], how_known: "Her mother's church."}
  baptism_or_initiation: {value: "Baptized Catholic at 12 (1943), name Anthony", certainty: 1.0, cites: [{source: S1, locator: "'Early life and education'"}, {source: S3, locator: "conversion paragraph"}], how_known: "Both sources."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1970–1987", certainty: 0.7, cites: [{source: S1, locator: "'The Bluest Eye'; 'Beloved'"}], how_known: "The Bluest Eye (1970) to Beloved (1987) (P29, P30)."}
  age_at_first_lasting_contribution: {value: 39, certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}], how_known: "1970 − 1931 = 39 (P30)."}
  first_evidence_of_lio_type_views: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S2, locator: "Bible question"}], how_known: "Nothing scored at 3 or 4."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S2, locator: "Bible question"}], how_known: "As above."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Her retrospective 'years and years' of serious Catholicism is undated."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S3, locator: "text"}], how_known: "Not assessed."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S3, locator: "text"}], how_known: "Not assessed."}
  circle_present: {value: "unclear", rationale: "'order and harmony that suggest an intelligence' (S3, secondary quotation).", certainty: 0.5, cites: [{source: S3, locator: "Beloved discussion"}], how_known: "Coder's reading."}
  reading: "Order and harmony suggesting an intelligence, in secondary quotation."
  notes: ""

institutions:
  - {value: "Random House", role: "textbook editor (Syracuse), then editor in New York", years: "1965–1983", kind: employer, certainty: 0.7, cites: [{source: S1, locator: "'Editing and teaching career'"}], how_known: "Britannica."}
  - {value: "Howard University", role: "teacher", years: "1957–1964", kind: university, certainty: 0.7, cites: [{source: S1, locator: "'Early life and education'"}], how_known: "Britannica."}
  - {value: "Princeton University", role: "professor", years: "1989–2006", kind: university, certainty: 0.7, cites: [{source: S1, locator: "'Editing and teaching career'"}], how_known: "Britannica."}
collaborators:
  - {value: "Slade Morrison", relation: family, note: "son; co-author of children's books", certainty: 0.7, cites: [{source: S1, locator: "'Nonfiction works and children's books'"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 136"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "All scored religion own-voice (Nation 2004, VIBE 1998, Monda 2007, NPR 2015) is after the 1970–1987 span (P1/P20 → 0.5)."
    - "Monda Do You Believe? book unread as a physical/ebook this pass; key sentences checked in contemporaneous review excerpts (Ron Slate; SF Bay Guardian)."
    - "Washington Post 2003 'disaffected Catholic' still not opened in primary."
  open_questions:
    - "Optional: open Monda book itself (not only excerpts) and Washington Post 2003 for 'disaffected Catholic'."
    - "Optional: in-span (1970–1987) religion self-label — none found this pass; would be needed to lift past P20 0.5."
    - "Optional: Nobel lecture (1993), Paris Review (1993), The Source of Self-Regard (2019) — unlikely to move B without a P16 exception claim."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "Britannica Editors. \"Toni Morrison.\" Encyclopaedia Britannica (12 Oct 2026). https://www.britannica.com/biography/Toni-Morrison. Read live 2026-10-19."
    url: "https://www.britannica.com/biography/Toni-Morrison"
    accessed: 2026-10-19
    reliability_note: "Editors' article; body cited, question boxes not cited (P26)."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, institutions, collaborators]
  - id: S2
    type: primary
    kind: other
    author: "Toni Morrison, interviewed by Terry Gross"
    citation: "Gross, Terry. \"Interview: Toni Morrison, Author Of 'God Help The Child'.\" Fresh Air, NPR, 20 April 2015. Transcript. https://www.npr.org/transcripts/400394947"
    url: "https://www.npr.org/transcripts/400394947"
    accessed: 2026-10-19
    reliability_note: "Broadcaster's transcript of a recorded interview (her own words; recorded_interview, P8); web copy."
    source_quality: "newspaper interview"
    used_for: [childhood, worldview, heritage, timing]
  - id: S3
    type: secondary
    kind: other
    author: "Nick Ripatrazone"
    citation: "Ripatrazone, Nick. \"On the Paradoxes of Toni Morrison's Catholicism.\" Literary Hub, 2 March 2020. https://lithub.com/on-the-paradoxes-of-toni-morrisons-catholicism/"
    url: "https://lithub.com/on-the-paradoxes-of-toni-morrisons-catholicism/"
    accessed: 2026-10-19
    reliability_note: "Essay by a critic and author; quotes her interviews, often without dates or sources (secondary quotation). Deepen D1: demoted — Nation/VIBE/Monda preferred for the same lines."
    source_quality: "other"
    used_for: [childhood, worldview, heritage, lane_b]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S5
    type: primary
    kind: other
    author: "Toni Morrison and Cornel West; The Nation (abridged transcript)"
    citation: "Morrison, Toni, and Cornel West. \"'We Better Do Something': Toni Morrison and Cornel West in Conversation.\" The Nation, 6 May 2004 (conversation 24 March 2004, Nation Institute / NY Society for Ethical Culture). https://www.thenation.com/article/archive/toni-morrison-cornel-west-politics/. Read live 2026-10-24."
    url: "https://www.thenation.com/article/archive/toni-morrison-cornel-west-politics/"
    accessed: 2026-10-24
    reliability_note: "Publisher's abridged/adapted transcript of a recorded public conversation — her own words (P8). Y2 path source for 'I'm a Catholic'."
    source_quality: "newspaper interview"
    used_for: [worldview]
  - id: S6
    type: primary
    kind: other
    author: "Toni Morrison, interviewed by Robert Morales"
    citation: "Morales, Robert. \"The VIBE Q: Toni Morrison.\" Vibe, May 1998; republished vibe.com 6 August 2019. https://www.vibe.com/features/editorial/toni-morrison-interview-may-1998-659803/. Read live 2026-10-24."
    url: "https://www.vibe.com/features/editorial/toni-morrison-interview-may-1998-659803/"
    accessed: 2026-10-24
    reliability_note: "Magazine interview (her own words). After the span."
    source_quality: "newspaper interview"
    used_for: [worldview]
  - id: S7
    type: primary
    kind: other
    author: "Toni Morrison, interviewed by Antonio Monda"
    citation: "Monda, Antonio. Do You Believe? Conversations on God and Religion. Vintage, 2007 (Morrison interview). Key sentences verified 2026-10-24 against Ron Slate, On the Seawall, 6 Jan 2008 (intelligence / intellectual experience) and Ari Messer, SF Bay Guardian, 28 Nov 2007 (order and harmony)."
    url: "https://www.ronslate.com/on-do-you-believe-conversations-on-god-and-religion-by-antonio-monda-vintage/"
    accessed: 2026-10-24
    reliability_note: "Published interview book — her words. Book itself unread this pass; quoted sentences checked in two contemporaneous review excerpts of the same interview. After the span. Used for A; not for overclaiming B (P16)."
    source_quality: "newspaper interview"
    used_for: [worldview]
  - id: S8
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia contributors. \"Toni Morrison.\" Wikipedia, The Free Encyclopedia. https://en.wikipedia.org/wiki/Toni_Morrison. Read live 2026-10-24."
    url: "https://en.wikipedia.org/wiki/Toni_Morrison"
    accessed: 2026-10-24
    reliability_note: "P50 dual bio with Britannica (S1): birth Lorain 1931-02-18 and death Bronx 2019-08-05 agree. Parents Ramah (Willis) and George Wofford. Worldview scores do not rest on Wikipedia."
    source_quality: "reference entry"
    used_for: [basics, childhood, heritage, review]
---

# Toni Morrison

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`. Deepen D1: CHRIST @0.5; A 1 @0.5; B/D BELOW; C/E UNKNOWN; mid BELOW. Not plotted.

## Summary

Toni Morrison (1931–2019), American novelist, Nobel Prize 1993 [S1; S8]. Deepen D1 (queue #133): primary_system CHRIST @0.5 (Nation 2004 + VIBE 1998 Catholic self-labels; Y2 path met; after span); A 1 @0.5 (Monda intelligence / order-and-harmony); B BELOW (P16); mid BELOW. Still not plotted.

## Life and work

Lorain, Howard, Cornell, Random House, Princeton [S1].

## Contribution and impact

The Bluest Eye, Song of Solomon, Beloved [S1].

## Childhood and education

AME mother; Catholic at 12 [S1; S2].

## Adult working worldview

Catholic self-labels in primary (1998, 2004) [S5; S6]; NPR retrospective seriousness then unstructured religion [S2]; Monda 2007 affirms a transcendent intelligence [S7]. CHRIST @0.5; A 1 @0.5; B BELOW. Characters unused [P42].

## Heritage (context only)

African American [S1].

## Timing

1970–1987, from age 39 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Not assessed [S3].

## Open questions

- Optional in-span religion self-label to lift past P20 0.5.
- Optional full Monda book + Washington Post 2003.

## Research log

- 2026-10-19: Read Britannica, the 2015 Fresh Air transcript and Ripatrazone's Lit Hub essay.
- 2026-10-24 (D1): Nation 2004 transcript (S5); VIBE 1998 (S6); Monda 2007 via Ron Slate + SF Bay Guardian excerpts (S7); Wikipedia EN dual bio (S8). Y2 path met → CHRIST @0.5; A 1 @0.5; B stays BELOW. Chart-moving NO. No fallacy_catalog; no figures/.
