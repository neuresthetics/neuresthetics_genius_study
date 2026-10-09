---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch C)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-08
  last_updated: 2026-10-08
  change_log:
    - {date: 2026-10-08, by: "Grok Bot", summary: "Record created (stage 3 batch C, order P32). Basics from Britannica (Hochfelder) and the Dictionary of Canadian Biography (Surtees); worldview from his letter to Mabel Bell of 12 March 1901 (Library of Congress TEI transcription) and his letter to Mabel Hubbard of 17 January 1876 (as transcribed by the Bell Homestead curator in the Brantford Expositor; secondary quotation). Not a scientist under P33 (inventions are not theories or results about natural systems). primary_system AGNOS 0.7 (consistent_private_letters; alternative CHRIST, nominal Unitarian); A, C, D BELOW_THRESHOLD; B, E UNKNOWN; mid_basin UNKNOWN. Draft, not reviewed."}

identity:
  id: bell-alexander-graham
  display_name: "Alexander Graham Bell"
  roster:
    canonical_name: "Alexander Graham Bell"
    rank: 7
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: invention
    field_bucket: "invention / engineering"
  full_name: {value: "Alexander Graham Bell", certainty: 1.0, cites: [{source: S1, locator: "heading"}, {source: S2, locator: "heading"}], how_known: "Two sources."}
  native_name: {value: "Alexander Graham Bell", certainty: 1.0, cites: [{source: S2, locator: "heading"}, {source: S1, locator: "heading"}], how_known: "English; two sources."}
  aliases:
    - {name: "Alexander-Graham-Bell", kind: "roster alias"}
    - {name: "Bell-Alexander Graham", kind: "roster alias"}

basics:
  birth:
    date: {value: "1847-03-03", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Born line"}, {source: S2, locator: "header ('b. 3 March 1847 in Edinburgh')"}], how_known: "Two sources agree."}
    place: {value: "Edinburgh, Scotland", modern_name: "Edinburgh, Scotland, UK", polity_then: "United Kingdom of Great Britain and Ireland", certainty: 1.0, cites: [{source: S1, locator: "Born line"}, {source: S2, locator: "header"}], how_known: "Two sources agree."}
  death:
    date: {value: "1922-08-02", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Died line"}, {source: S2, locator: "header ('d. 2 Aug. 1922')"}], how_known: "Two sources agree."}
    place: {value: "Beinn Bhreagh, near Baddeck, Cape Breton Island, Nova Scotia", modern_name: "near Baddeck, Nova Scotia, Canada", polity_then: "Canada", certainty: 1.0, cites: [{source: S1, locator: "Died line"}, {source: S2, locator: "header ('near Baddeck, N.S.')"}], how_known: "Two sources agree."}
  first_lasting_contribution_year: {value: 1876, certainty: 1.0, cites: [{source: S1, locator: "telephone section (patent filed 14 February, granted 7 March 1876)"}, {source: S2, locator: "telephone paragraphs (US application 14 February; patent 7 March)"}], how_known: "The telephone patent application of 14 February 1876 is the first documented public statement (P30). Two sources."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "telephone section"}, {source: S2, locator: "telephone paragraphs"}], how_known: "From 1876 under P2."}
  region_of_birth: {value: "Northern Europe", certainty: 1.0, cites: [{source: S1, locator: "Born line"}, {source: S2, locator: "header"}], how_known: "UK is Northern Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "North America", certainty: 1.0, cites: [{source: S1, locator: "Boston; Washington; Nova Scotia sections"}, {source: S2, locator: "Boston; Volta Laboratory; Baddeck paragraphs"}], how_known: "Boston, Washington and Nova Scotia; USA and Canada are North America."}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S1, locator: "throughout"}, {source: S2, locator: "throughout"}], how_known: "As the sources record it."}
  languages_of_work: {value: [English], certainty: 1.0, cites: [{source: S2, locator: "throughout"}, {source: S3, locator: "letter"}], how_known: "English."}
  occupations: {value: ["teacher of the deaf", "inventor", "scientist"], certainty: 1.0, cites: [{source: S2, locator: "header ('teacher of the deaf, inventor, and scientist')"}, {source: S1, locator: "opening"}], how_known: "Two sources; 'scientist' is DCB's word, not the P30 test (see coder_notes)."}

contribution:
  fields: {value: ["telecommunications", "acoustics and speech", "education of the deaf", "aeronautics"], certainty: 1.0, cites: [{source: S1, locator: "opening; later sections"}, {source: S2, locator: "throughout"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "The telephone (US patent 174,465, 'Improvements in Telegraphy')", year: "1876", kind: invention, lasting: "the telephone; 'the single most lucrative patent ever awarded' (S2)", certainty: 1.0, cites: [{source: S1, locator: "telephone section"}, {source: S2, locator: "telephone paragraphs"}], how_known: "Two sources; application filed 14 February 1876."}
    - {value: "The photophone: speech transmitted on a beam of light (with Charles Sumner Tainter)", year: "1880", kind: invention, lasting: "'presaged modern fibre optics' (S2)", certainty: 1.0, cites: [{source: S1, locator: "photophone (1880)"}, {source: S2, locator: "photophone paragraph ('I have heard a ray of the sun', 26 February [1880])"}], how_known: "Two sources."}
    - {value: "The graphophone: recording on a wax cylinder with a floating stylus (with Chichester A. Bell and Charles Sumner Tainter)", year: "1886", kind: invention, lasting: "wax-cylinder recording", certainty: 0.7, cites: [{source: S1, locator: "Volta Laboratory (Graphophone patents granted 1886)"}, {source: S2, locator: "graphophone paragraph ('developed ... in 1882')"}], how_known: "DCB says developed in 1882; Britannica gives the patents of 1886. Under P30 the first documented public statement read is the 1886 patent, so 1886; the 1882 date is private development. 0.7 for the conflict."}
  evidence_of_impact:
    - {value: "The decibel is named after him (from his 1879 audiometer)", kind: "named after them", certainty: 0.7, cites: [{source: S2, locator: "audiometer paragraph"}], how_known: "DCB alone."}
    - {value: "Volta Prize of the French government (1880)", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "Volta Prize paragraph"}], how_known: "Britannica alone."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Inventor of the telephone.", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "telephone paragraphs"}], how_known: "Two sources."}

childhood:
  family_religion: {value: TODO}
  family_religious_practice: {value: "His mother, Eliza, 'imbued her three sons with her deep piety, which influenced Aleck \"at least until I reached years of discretion\"'", certainty: 0.7, cites: [{source: S2, locator: "childhood paragraph"}], how_known: "DCB alone, quoting Bell (secondary quotation)."}
  parents_and_household:
    - {value: "Father Alexander Melville Bell, elocutionist and author of Visible Speech", role: father, certainty: 1.0, cites: [{source: S2, locator: "header; early paragraphs"}, {source: S1, locator: "early life"}], how_known: "Two sources."}
    - {value: "Mother Eliza Grace Symonds, a miniature painter, who was deaf", role: mother, certainty: 0.7, cites: [{source: S2, locator: "header; family paragraph"}], how_known: "DCB."}
  household_circumstances: {value: "Family 'steeped in liberalism'; his grandfather 'despised dogma'", certainty: 0.7, cites: [{source: S2, locator: "childhood paragraph"}], how_known: "DCB alone."}
  schooling:
    - {value: "Hamilton Place Academy, Edinburgh", stage: "grammar or secondary school", run_by: private, years: "1857–", ages: "10–", certainty: 0.7, cites: [{source: S2, locator: "schooling paragraph"}], how_known: "DCB alone; run_by is the coder's reading of 'academy'."}
    - {value: "Royal High School, Edinburgh, entered at 11 and left at 15", stage: "grammar or secondary school", run_by: "state or municipal", certainty: 0.7, cites: [{source: S1, locator: "early life"}], how_known: "Britannica alone; run_by is the coder's reading."}
    - {value: "A year with his grandfather in London, at about 15, which made him 'ashamed of his gross ignorance'", stage: other, run_by: family, certainty: 0.7, cites: [{source: S2, locator: "grandfather paragraph"}], how_known: "DCB alone."}
    - {value: "Courses in anatomy and physiology at University College London (no degree)", stage: university, run_by: other, years: "1868–1870", ages: "21–23", certainty: 1.0, cites: [{source: S2, locator: "1868–1870 paragraph"}, {source: S1, locator: "early life (UCL 1868)"}], how_known: "Two sources."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: TODO}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1876–1886", certainty: 0.7, cites: [{source: S1, locator: "telephone section; Volta Laboratory"}, {source: S2, locator: "telephone; graphophone paragraphs"}], how_known: "Equals timing.major_work_period (P29, P30); end year carries the graphophone date conflict."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Neither letter read speaks of science and religion together."}
  primary_system:
    value: AGNOS
    basis: consistent_private_letters
    certainty: 0.7
    cites: [{source: S3, locator: "letter text, item 5"}, {source: S4, locator: "letter text, religion paragraph"}]
    how_known: "Two private letters 25 years apart say the same: 'Concerning Death – & Immortality – Salvation – Faith and all the other points of theoretical religion, – I know absolutely nothing – & can frame no beliefs whatever' (1876, S4) and 'On matters unknowable I don't profess to know. I have always considered myself as an Agnostic' (1901, S3). The 1876 letter is inside the working years; the 1901 letter is later but says 'always', and no change is documented (P31). Ceiling 0.7 for private letters, and a named alternative."
    rationale: "Draft judgment (one line): AGNOS at 0.7. Named alternative: CHRIST (Unitarian, nominal), since in 1901 he found 'that I was myself a Unitarian and did not know it' and called himself 'a Unitarian Agnostic' (S3). AGNOS is a stub system file (flag, sourcing backlog)."
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: AGNOS, reason: "Coded at 0.7: own self-description, two letters (S3; S4). AGNOS is a stub system file.", cites: [{source: S3, locator: "item 5"}, {source: S4, locator: "religion paragraph"}]}
    - {code: CHRIST, reason: "Named alternative: 'a Unitarian Agnostic' (1901). Against: he joins the Unitarians only because 'I don't have any beliefs' (S3); no membership is recorded in the sources read.", cites: [{source: S3, locator: "item 5"}]}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, note: "He speaks of beliefs that 'belong between himself & his Maker' (1876, S4) and quotes Pope, 'Say first, of God above, or man below What can we reason, but from what we KNOW' (1901, S3): God is named but nothing is affirmed of where God is. Draft judgment (one line): too indirect to score.", how_known: "BELOW_THRESHOLD under P19."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist under P33 (his lasting contributions are inventions), so B needs a statement of his about nature (P16); none was found in the sources read."}
    C_ledger: {value: BELOW_THRESHOLD, note: "'Concerning Death – & Immortality – Salvation ... I know absolutely nothing' and 'I cannot believe in the inherent wickedness of man' (S4, 1876): suspension of judgment on reward and afterlife, with a rejection of innate sin. Draft judgment (one line): too indirect to score.", how_known: "BELOW_THRESHOLD under P19; the letter is a secondary transcription."}
    D_authority: {value: BELOW_THRESHOLD, note: "He would rather be said to have lived 'a pure and upright life – than that I had attended church three times on Sunday – or that I believed everything that the church teaches' (S4): church teaching has no hold on him, but nothing is said of revelation against reason. Draft judgment (one line): too indirect to score.", how_known: "BELOW_THRESHOLD under P19."}
    E_scope: {value: UNKNOWN, how_known: "Nothing on the world's order in the sources read (P7, P19). The 1876 remark that a good man 'whether he be Christian, Pagan or Mahomedan' is to be admired concerns the moral community (C under P7), not the world's order."}
  mid_basin: {value: UNKNOWN, how_known: "B_cause is UNKNOWN, which takes precedence (§6, P19)."}
  statements:
    - text: "As I had never seen any exposition of the beliefs of the Unitarian, I thought I would dip into it and see what it was all about, and made the discovery that I was myself a Unitarian and did not know it, for I don't have any beliefs and agree thoroughly with Pope when he says:— “Say first, of God above, or man below What can we reason, but from what we KNOW”. On matters unknowable I don't profess to know. I have always considered myself as an Agnostic — which of course I am, but I have now discovered that I am a Unitarian Agnostic."
      cites: [{source: S3, locator: "letter text, item 5"}]
      date: "1901-03-12"
      context: "After finding a tract by Rev. James T. Bixby, 'Our Beliefs and Some of the Reasons for them' (American Unitarian Association)."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "primary transcription"
      verified_on: 2026-10-08
    - text: "My religion is all of the practical kind. I hold no theories nor beliefs whatever. I cannot believe in the inherent wickedness of man."
      cites: [{source: S4, locator: "letter text, religion paragraph"}]
      date: "1876-01-17"
      context: "Letter from 5 Exeter Place, Boston, to his fiancée Mabel Hubbard."
      axes: [C_ledger]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-08
      note: "Primary check pending (P26): transcription by Brian Wood, curator, Bell Homestead National Historic Site, in the Brantford Expositor; the manuscript was not found among the digitised LOC items."
    - text: "Concerning Death – & Immortality – Salvation – Faith and all the other points of theoretical religion, – I know absolutely nothing – & can frame no beliefs whatever. I can only see what is before me – my life – & my duty here."
      cites: [{source: S4, locator: "letter text, religion paragraph"}]
      date: "1876-01-17"
      context: "Same letter."
      axes: [C_ledger]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-08
      note: "Primary check pending (P26)."
    - text: "It seems to me that a man’s beliefs are too sacred to be talked much about – they are things that belong between himself & his Maker – and not between man & fellow-man."
      cites: [{source: S4, locator: "letter text, following paragraph"}]
      date: "1876-01-17"
      context: "Same letter."
      axes: [A_locus, D_authority]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-08
      note: "Primary check pending (P26)."
  changes_over_life:
    - {value: "Raised in his mother's 'deep piety', which influenced him 'at least until I reached years of discretion'; by 1876 he described 'breaking out of the prejudices of my childhood' and held 'no theories nor beliefs whatever'", certainty: 0.5, cites: [{source: S2, locator: "childhood paragraph"}, {source: S4, locator: "religion paragraph"}], how_known: "DCB's secondary quotation of Bell and the 1876 letter (secondary transcription); no year is given for the change, so it is not dated (P12)."}
  coder_notes: "Not a scientist under P33 (decided 2026-10-08, v8's pick): his listed lasting contributions are inventions (telephone, photophone, graphophone), not theories or results about physical or natural systems; DCB's 'scientist' is a job description, not the P30 test. So B needs a statement about nature (P16), and none was found: B UNKNOWN. The 1876 letter is a secondary transcription; the LOC Bell papers were searched by folder id for it without success (loc.gov pages blocked by Cloudflare; tile.loc.gov TEI used for the 1901 letter). AGNOS is a stub system file. No LIO-type views found: nothing of his is scored 3 or 4."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Scottish; family of elocutionists", certainty: 1.0, cites: [{source: S1, locator: "early life"}, {source: S2, locator: "opening paragraphs"}], how_known: "Two sources."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1876–1886", certainty: 0.7, cites: [{source: S1, locator: "telephone section; Volta Laboratory"}, {source: S2, locator: "telephone; graphophone paragraphs"}], how_known: "Telephone (1876) to graphophone patents (1886) (P29, P30); 0.7 because DCB dates the graphophone to 1882."}
  age_at_first_lasting_contribution: {value: 29, certainty: 1.0, cites: [{source: S1, locator: "Born line; telephone section"}, {source: S2, locator: "header; telephone paragraphs"}], how_known: "1876 − 1847 = 29 (P30)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No statement of his scored at 3 or 4 (P27)."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", rationale: "His letters suspend judgment; nothing on nature's order was read.", certainty: 0.5, cites: [{source: S3, locator: "item 5"}, {source: S4, locator: "religion paragraph"}], how_known: "Absence in what was read."}
  worldview_during_major_work: {value: "Practical religion without beliefs; agnostic on death, immortality and salvation (1876)", certainty: 0.5, cites: [{source: S4, locator: "religion paragraph"}], how_known: "One letter inside the working years, secondary transcription."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "His work was experimental invention, not derivation from definitions.", certainty: 0.5, cites: [{source: S2, locator: "telephone paragraphs"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "schooling paragraph"}], how_known: "A self-described poor student; nothing on mathematics."}
  circle_present: {value: "no", rationale: "He declines to frame beliefs about God; no God–Nature tie.", certainty: 0.5, cites: [{source: S3, locator: "item 5"}], how_known: "Coder's reading."}
  reading: "As belief, not finding: form absent, circle absent."
  notes: ""

institutions:
  - {value: "Boston University", role: "professor of vocal physiology", years: "1873–", kind: university, certainty: 0.7, cites: [{source: S2, locator: "Boston University paragraph (early 1873)"}], how_known: "DCB alone."}
  - {value: "Volta Laboratory, Washington", role: founder, years: "1880–", kind: "research institute", certainty: 1.0, cites: [{source: S1, locator: "Volta Prize paragraph"}, {source: S2, locator: "graphophone paragraph"}], how_known: "Two sources."}
  - {value: "Aerial Experiment Association", role: "coordinator and promoter", years: "1907–", kind: "research institute", certainty: 1.0, cites: [{source: S1, locator: "aeronautics section (1907)"}, {source: S2, locator: "Aerial Experiment Association paragraph"}], how_known: "Two sources; the year is Britannica's."}
collaborators:
  - {value: "Thomas A. Watson", relation: "student or assistant", note: "assistant from January 1875", certainty: 1.0, cites: [{source: S2, locator: "Watson paragraph"}, {source: S1, locator: "telephone section"}], how_known: "Two sources."}
  - {value: "Charles Sumner Tainter", relation: collaborator, note: "photophone; graphophone", certainty: 1.0, cites: [{source: S2, locator: "photophone and graphophone paragraphs"}, {source: S1, locator: "photophone; Volta Laboratory"}], how_known: "Two sources."}
  - {value: "Chichester A. Bell", relation: collaborator, note: "cousin; graphophone", certainty: 1.0, cites: [{source: S2, locator: "graphophone paragraph"}, {source: S1, locator: "Volta Laboratory"}], how_known: "Two sources."}
  - {value: "Gardiner Greene Hubbard", relation: family, note: "father-in-law; filed the US telephone application", certainty: 1.0, cites: [{source: S2, locator: "Hubbard paragraphs"}, {source: S1, locator: "telephone section"}], how_known: "Two sources."}
  - {value: "Elisha Gray", relation: "rival or critic", note: "filed a rival application hours later on 14 February 1876", certainty: 0.7, cites: [{source: S2, locator: "patent paragraph"}], how_known: "DCB."}
  - {value: "Thomas Edison (edison-thomas)", relation: "rival or critic", note: "beat him to market with the phonograph", certainty: 0.7, cites: [{source: S2, locator: "graphophone paragraph"}], how_known: "DCB."}

review:
  roster_status_reason: {value: "Core in v8 (F 5: Claude, DeepSeek, Gemini, GPT, Grok).", certainty: 0.7, cites: [{source: S5, locator: "roster.csv, rank 7"}], how_known: "Study roster."}
  controversies:
    - {value: "Priority dispute with Elisha Gray over the telephone", certainty: 0.7, cites: [{source: S2, locator: "patent paragraph"}], how_known: "DCB."}
  data_quality_flags:
    - "Graphophone: developed 1882 (DCB) vs patents 1886 (Britannica); 1886 used under P30."
    - "National Geographic Society: DCB says he was named its first president in 1888 and held the post until 1903; Britannica gives president 1898–1903. Not used for any field."
    - "The 1876 letter is a secondary transcription (curator, newspaper); primary check pending."
  open_questions:
    - "Find the 17 January 1876 letter in the LOC Bell family papers."
    - "Any statement of his on nature's order (e.g. in his speeches on discovery) that would let B be scored."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "David Hochfelder"
    citation: "Hochfelder, David. \"Alexander Graham Bell.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Alexander-Graham-Bell."
    url: "https://www.britannica.com/biography/Alexander-Graham-Bell"
    accessed: 2026-10-08
    reliability_note: "Signed encyclopedia article; locators are section topics."
    used_for: [identity, basics, contribution, childhood, heritage, timing, institutions, collaborators]
  - id: S2
    type: secondary
    kind: encyclopedia
    author: "Lawrence Surtees"
    citation: "Surtees, Lawrence. \"BELL, ALEXANDER GRAHAM.\" In Dictionary of Canadian Biography, vol. 15. University of Toronto/Université Laval, 2003–. https://www.biographi.ca/en/bio/bell_alexander_graham_15E.html."
    url: "https://www.biographi.ca/en/bio/bell_alexander_graham_15E.html"
    accessed: 2026-10-08
    reliability_note: "Signed scholarly biography with archival bibliography; locators are paragraph topics."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S3
    type: primary
    kind: letter
    author: "Alexander Graham Bell"
    year: 1901
    citation: "Bell, Alexander Graham, to Mabel Hubbard Bell, 12 March 1901. Alexander Graham Bell Family Papers, Library of Congress, item magbell 04100410 (machine-readable transcription, National Digital Library Program)."
    url: "https://tile.loc.gov/storage-services/service/mss/magbell/041/04100410/04100410.xml"
    accessed: 2026-10-08
    reliability_note: "Library of Congress TEI transcription of the manuscript; the loc.gov viewer page was blocked, the XML was read."
    used_for: [basics, worldview, timing, lane_b]
  - id: S4
    type: primary
    kind: letter
    author: "Alexander Graham Bell"
    year: 1876
    citation: "Bell, Alexander Graham, to Mabel Hubbard, 17 January 1876, as transcribed in \"Bell shares with Mabel thoughts on religion,\" Brantford Expositor, 21 January 2021 (Bell Letters annotated by Brian Wood, curator, Bell Homestead National Historic Site)."
    url: "https://www.brantfordexpositor.ca/opinion/bell-shares-with-mabel-thoughts-on-religion"
    accessed: 2026-10-08
    reliability_note: "Secondary quotation (newspaper transcription by a museum curator); primary check pending (P26)."
    used_for: [worldview, timing]
  - id: S5
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-08
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
---

# Alexander Graham Bell

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Alexander Graham Bell (1847–1922), Scottish-born teacher of the deaf and inventor, patented the telephone in 1876 and went on to the photophone and the graphophone [S1; S2]. In private letters he wrote that on 'Death – & Immortality – Salvation' he knew 'absolutely nothing' (1876) and that he had 'always considered myself as an Agnostic', now 'a Unitarian Agnostic' (1901) [S3; S4]. Draft: AGNOS 0.7; A, C, D BELOW_THRESHOLD; B, E UNKNOWN; mid_basin UNKNOWN.

## Life and work

Edinburgh childhood; London; Canada 1870; Boston 1871; telephone 1876; Volta Laboratory in Washington; Beinn Bhreagh in Nova Scotia [S1; S2].

## Contribution and impact

Telephone (1876), photophone (1880), graphophone (1886 patents; developed 1882) [S1; S2]; the decibel [S2].

## Childhood and education

His mother's piety influenced him 'until I reached years of discretion' [S2]; Hamilton Place Academy, the Royal High School, a year with his grandfather in London, UCL courses [S1; S2].

## Adult working worldview

Agnostic by his own description [S3; S4].

## Heritage (context only)

Scottish [S1; S2].

## Timing

First lasting contribution 1876, at 29. No LIO-type views found.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form absent; circle absent [S2; S3].

## Open questions

- Primary check of the 1876 letter.

## Research log

- 2026-10-08: Read Britannica (Hochfelder), DCB (Surtees), the LOC TEI transcription of the 12 March 1901 letter, and the Brantford Expositor transcription of the 17 January 1876 letter. loc.gov viewer pages were blocked or timed out.
