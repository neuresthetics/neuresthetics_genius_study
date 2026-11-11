---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z5)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to 20c_late. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z5, order P32: F 3, rank 156; Caroline Herschel at rank 155 already coded). Basics from the Paris Review interview (Jerome Brooks, Art of Fiction No. 139, Winter 1994) and Innes's Cambridge study (chapter 'Origins', via excerpt). Own words: memoir There Was a Country (2012) as excerpted in Guernica (15 October 2012): 'I often had periods of oscillating faith as I grew older, periods of doubt'; struggled with 'the certitude of Christianity'; Igbo proverbs 'far more valuable to me ... than the doctrinaire, self-righteous strain of the Christian faith I was taught'. After the span (P20). Not a scientist. Span 1958 at 0.5. primary_system BELOW_THRESHOLD (lead CHRIST); A BELOW_THRESHOLD; B UNKNOWN; C, D, E UNKNOWN; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen D1 (queue #150, F 3, rank 156). Opened Paris Review Art of Fiction No. 139 in full (parents CMS evangelists; Ibadan comparative West African religions — cultural/academic, not profession). PN Review interview with Brenda Lyons (pub. 2014 from earlier conversation): chi as spark from Supreme God; Chukwu appropriated by Christians; crossroads of Christianity and traditional religion — after-span lead only (P20). CBC Writers & Company 1994 (Eleanor Wachtel): writing as 'act of atonement' for father's generation abandoning ancestral faith — cultural/political, not a scored profession. Guernica 2012 memoir re-confirmed (oscillating faith / Igbo proverbs preferred). Wikipedia EN dual bio (S5; P50): death 21 March 2013 Boston; birth Albert Chinụalụmọgụ; parents Isaiah Okafo / Janet Anaenechi Iloegbunam; TFA lastingness corroboration. Named for Victoria (1973) still unread (IA print-disabled; no free full text). Britannica blocked. P42: Okonkwo/Ezeulu not coded as authorial. P47 source_quality on S1–S7. primary_system BELOW_THRESHOLD (lead CHRIST); A BELOW_THRESHOLD; B UNKNOWN (not a scientist, P30; no nature-order own-voice); mid UNKNOWN. Chart-moving NO. Draft, not reviewed."}

identity:
  id: achebe-chinua
  display_name: "Chinua Achebe"
  roster:
    canonical_name: "Chinua Achebe"
    rank: 156
    F: 3
    models: [Gemini, GPT, Grok]
    band: "core (3–4)"
    status: core
    field: literature
    field_bucket: literature
  full_name: {value: "Albert Chinụalụmọgụ Achebe", certainty: 1.0, cites: [{source: S3, locator: "opening"}, {source: S5, locator: "infobox / lead"}], how_known: "Innes: 'christened Albert Chinualumogu'; Wikipedia: Albert Chinụalụmọgụ Achebe (dual bio, P50)."}
  native_name: {value: "Chinua Achebe", certainty: 0.7, cites: [{source: S1, locator: "headnote"}], how_known: "Paris Review."}
  aliases:
    - {name: "Achebe-Chinua", kind: "roster alias"}
    - {name: "Chinua-Achebe", kind: "roster alias"}

basics:
  birth:
    date: {value: "1930-11-16", calendar: gregorian, certainty: 1.0, cites: [{source: S3, locator: "opening"}, {source: S5, locator: "infobox"}], how_known: "Innes and Wikipedia agree (P50)."}
    place: {value: "near Ogidi (Saint Simon's Church, Nneobi), Colonial Nigeria", modern_name: "Ogidi / Nnobi area, Anambra State, Nigeria", polity_then: "British colony of Nigeria", certainty: 0.7, cites: [{source: S5, locator: "Youth and background"}, {source: S3, locator: "opening"}, {source: S2, locator: "Magical Years"}], how_known: "Wikipedia: born/baptised at Saint Simon's Church, Nneobi, near Ogidi. Memoir (S2): 'Nnobi, near my hometown of Ogidi'. Innes places the family at Ogidi after the fifth child's birth (birthplace detail 0.7)."}
  death:
    date: {value: "2013-03-21", calendar: gregorian, certainty: 0.7, cites: [{source: S5, locator: "infobox / Later years and death"}], how_known: "Wikipedia EN (tertiary; Britannica blocked this deepen — P50 dual bio incomplete for death; CBC S7 confirms year 2013 age 82 without day/place)."}
    place: {value: "Boston, Massachusetts, U.S.", modern_name: "Boston, Massachusetts, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S5, locator: "infobox / Later years and death"}], how_known: "Wikipedia EN (single tertiary for place; open question until a second independent source)."}
  first_lasting_contribution_year: {value: 1958, certainty: 1.0, cites: [{source: S1, locator: "headnote"}, {source: S5, locator: "lead"}], how_known: "Things Fall Apart, 1958; Wikipedia calls it his magnum opus (dual, P50)."}
  era_bucket: {value: "1950 on", certainty: 1.0, cites: [{source: S1, locator: "headnote"}], how_known: "1958 (P2)."}
  region_of_birth: {value: "Sub-Saharan Africa", certainty: 1.0, cites: [{source: S3, locator: "opening"}, {source: S5, locator: "infobox"}], how_known: "Nigeria (P3)."}
  region_of_work: {value: "Sub-Saharan Africa", certainty: 0.7, cites: [{source: S1, locator: "headnote"}, {source: S5, locator: "lead"}], how_known: "Nigerian Broadcasting Corporation, Lagos / Enugu through the span; later U.S. teaching is after the coded work period.", alternatives: [{value: "North America", cites: [{source: S5, locator: "Later years"}], note: "Bard / Brown professorships after 1990; outside major_work_period 1958."}]}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Paris Review; he defended writing in English."}
  occupations: {value: ["novelist", "radio producer", "editor", "professor"], certainty: 1.0, cites: [{source: S1, locator: "headnote"}, {source: S5, locator: "lead"}], how_known: "Paris Review and Wikipedia."}

contribution:
  era_bucket: 20c_late
  fields: {value: ["literature"], certainty: 1.0, cites: [{source: S1, locator: "headnote"}, {source: S5, locator: "lead"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Things Fall Apart", year: 1958, kind: work, lasting: "most widely studied, translated, and read African novel; magnum opus of the African Trilogy", certainty: 1.0, cites: [{source: S1, locator: "headnote"}, {source: S5, locator: "lead"}], how_known: "Paris Review lists it; Wikipedia states lastingness (dual, P50)."}
  evidence_of_impact:
    - {value: "Often called the father of modern African literature (a tag he rejected); Things Fall Apart translated into dozens of languages with tens of millions of copies", certainty: 0.7, cites: [{source: S5, locator: "lead / Overview"}], how_known: "Wikipedia EN (tertiary)."}
    - {value: "Man Booker International Prize (2007); founding general editor of the Heinemann African Writers Series", certainty: 0.7, cites: [{source: S5, locator: "Awards; Voice of Nigeria and African Writers Series"}, {source: S1, locator: "headnote"}], how_known: "Wikipedia; Paris Review headnote on the series."}
  major_works:
    - {value: "No Longer at Ease", year: 1960, kind: book, certainty: 0.7, cites: [{source: S1, locator: "headnote"}, {source: S5, locator: "lead"}], how_known: "Paris Review; Wikipedia African Trilogy."}
    - {value: "Arrow of God", year: 1964, kind: book, certainty: 0.7, cites: [{source: S1, locator: "headnote"}, {source: S5, locator: "lead"}], how_known: "Paris Review; Wikipedia."}
    - {value: "A Man of the People", year: 1966, kind: book, certainty: 0.7, cites: [{source: S1, locator: "headnote"}, {source: S5, locator: "lead"}], how_known: "Paris Review; Wikipedia."}
    - {value: "Anthills of the Savannah", year: 1987, kind: book, certainty: 0.7, cites: [{source: S1, locator: "headnote"}, {source: S5, locator: "lead"}], how_known: "Paris Review; Wikipedia."}
  honours:
    - {value: "Man Booker International Prize", year: 2007, certainty: 0.7, cites: [{source: S5, locator: "Awards"}], how_known: "Wikipedia."}
    - {value: "Nigerian National Merit Award / Order of the Federal Republic (1979); later refused Commander of the Federal Republic (2004, 2011)", year: 1979, certainty: 0.7, cites: [{source: S5, locator: "Awards"}], how_known: "Wikipedia."}
  definition_fit: {value: "clearly meets", rationale: "Founding novelist of modern African literature in English; Things Fall Apart is a lasting work under the study definition.", certainty: 0.7, cites: [{source: S1, locator: "headnote"}, {source: S5, locator: "lead"}], how_known: "Coder's reading of two sources."}

childhood:
  family_religion: {value: "Anglican (Church Missionary Society) converts", certainty: 1.0, cites: [{source: S1, locator: "first answer"}, {source: S3, locator: "opening"}, {source: S5, locator: "Youth and background"}, {source: S6, locator: "opening answers"}], how_known: "(Paris Review) 'My parents were early converts to Christianity'; father a CMS evangelist/catechist (Innes; Wikipedia; PN Review)."}
  family_religious_practice: {value: "Bible readings at prayer time, memorization, hymns, Sunday school, parish work at St. Philip's Church Ogidi", certainty: 0.7, cites: [{source: S2, locator: "Magical Years"}, {source: S6, locator: "opening answers"}], how_known: "Memoir (2012) and PN Review interview (after-span practice description of childhood)."}
  parents_and_household:
    - {value: "Isaiah Okafo Achebe (also Okafor in Innes), father, CMS teacher and evangelist / catechist", name: "Isaiah Okafo Achebe", role: father, certainty: 0.7, cites: [{source: S5, locator: "Youth and background"}, {source: S3, locator: "opening"}, {source: S1, locator: "first answer"}], how_known: "Wikipedia Okafo; Innes Okafor (spelling alternative); Paris Review: evangelist, religious teacher."}
    - {value: "Janet Anaenechi Iloegbunam Achebe, mother, Christian convert; daughter of an Awka blacksmith; church women's leader", name: "Janet Anaenechi Iloegbunam", role: mother, certainty: 0.7, cites: [{source: S5, locator: "Youth and background"}, {source: S3, locator: "opening"}], how_known: "Wikipedia full name; Innes 'Janet Achebe'."}
  household_circumstances: {value: "Fifth of six surviving children; father retired to the ancestral village of Ogidi; Christian compound beside a non-Christian village world", certainty: 0.7, cites: [{source: S1, locator: "first answer"}, {source: S6, locator: "opening answers"}], how_known: "(interviews)."}
  schooling:
    - {value: "St Philips' Central School, Ogidi", stage: "elementary school", run_by: "religious body", years: "1930s", certainty: 0.7, cites: [{source: S5, locator: "Youth and background"}], how_known: "Wikipedia."}
    - {value: "Government College Umuahia", stage: "grammar or secondary school", run_by: "state or municipal", years: "1940s", certainty: 0.7, cites: [{source: S5, locator: "Youth and background"}], how_known: "Wikipedia."}
    - {value: "University College, Ibadan (London degree); English, history, and religion after leaving medicine", stage: university, run_by: "state or municipal", years: "1948–1953", certainty: 0.7, cites: [{source: S1, locator: "Ibadan answer"}, {source: S5, locator: "University"}], how_known: "Paris Review; Wikipedia."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading:
    - {value: "Igbo translation of The Pilgrim's Progress; prose Midsummer Night's Dream; Bible", certainty: 0.7, cites: [{source: S2, locator: "Magical Years"}, {source: S5, locator: "Youth and background"}], how_known: "Memoir; Wikipedia."}
  childhood_mentors:
    - {value: "Udoh Osinyi, great-uncle, ozo titleholder who refused conversion", certainty: 0.7, cites: [{source: S2, locator: "excerpt"}, {source: S5, locator: "Youth and background"}], how_known: "Memoir; Wikipedia."}
  languages_in_childhood: {value: ["Igbo", "English"], certainty: 0.7, cites: [{source: S1, locator: "first answer"}, {source: S6, locator: "first language answer"}], how_known: "Interviews; PN Review: first language Igbo."}
  notable_events:
    - {value: "Grew up at the 'crossroads' of CMS Christianity and still-active Igbo traditional religion", certainty: 0.7, cites: [{source: S2, locator: "Magical Years"}, {source: S6, locator: "crossroads answers"}], how_known: "Memoir and PN Review (after-span descriptions of childhood)."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1958", certainty: 0.5, cites: [{source: S1, locator: "headnote"}], how_known: "Equals timing.major_work_period (Things Fall Apart only lasting at the coder's call; later novels are candidates, not expanded this pass)."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not a scientist; no science–religion statement read."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "Raised Anglican (S1; S3; S5; S6). After-span own voice (P20): oscillating faith / doubt of Christian 'certitude' (S2, 2012); writing framed as cultural 'atonement' for ancestral-faith abandonment (S7, 1994); chi/Chukwu discussion is explanatory of Igbo cosmology, not a profession of belief (S6). No clear adult profession of CHRIST, ANIM, or another system in or near the 1958 span. Lead CHRIST (upbringing). Okonkwo/Ezeulu and other fiction figures not used as authorial (P42)."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Lead only: CMS upbringing and parish childhood; after-span doubt and cultural critique of missionary Christianity without a clear adult reaffirmation or renunciation in span."}
    - {code: ANIM, reason: "Rejected for scoring: admiration for Igbo traditional religion is artistic, cultural, and comparative (S2; S6); not stated as his adult worship or profession."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "After-span memoir and interviews show doubt/oscillation and comparative interest in Chukwu/chi (S2; S6; S7) without locating God for his own adult belief. No in-span locus statement. Too thin to score (P19)."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30); novelist — no own-voice claim about nature's causal order (P16). Fiction cosmology (chi, gods) is not scored as his physics (P42)."}
    C_ledger: {value: UNKNOWN, how_known: "Not read as a scored own-voice claim."}
    D_authority: {value: UNKNOWN, how_known: "Critical of missionary absolutism after the span (S2); no scored revelation-vs-observation profession in span."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: UNKNOWN, how_known: "B_cause is UNKNOWN, which takes precedence (§6, P19). Chart-moving NO (deepen 2026-10-24)."}
  statements:
    - text: "My parents were early converts to Christianity in my part of Nigeria. They were not just converts; my father was an evangelist, a religious teacher. He and my mother traveled for thirty-five years to different parts of Igboland, spreading the gospel."
      cites: [{source: S1, locator: "first answer"}]
      date: "1994"
      context: "Paris Review Art of Fiction No. 139; after the span (P20) — childhood heritage lead."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
    - text: "Studying religion was new to me and interesting because it wasn't only Christian theology; we also studied West African religions. … For the first time, I was able to see the systems—including my own—compared and placed side by side, which was really exciting."
      cites: [{source: S1, locator: "Ibadan answer"}]
      date: "1994"
      context: "Paris Review; after the span — academic comparative interest at Ibadan, not a profession of belief."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
    - text: "Chi is something very, very old, as old as the Supreme God, I think, because it seems to me that chi is perhaps a manifestation of the Supreme God himself in every individual. Each individual is given a little spark from the abundance of the supreme deity to accompany him or her through their life in this world."
      cites: [{source: S6, locator: "chi answers"}]
      date: "2014"
      context: "PN Review conversation with Brenda Lyons (interview date not stated on page; published 2014). After the span (P20). Explanatory of Igbo cosmology, not a first-person profession of worship."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
    - text: "The history of Africa is such that our business should be to restore what was lost. … My father, for instance, became a first-generation Christian. He abandoned the faith of his fathers. … And so, in redefining ourselves, we were making amends for this betrayal."
      cites: [{source: S7, locator: "ON WRITING THINGS FALL APART AS AN \"ACT OF ATONEMENT\""}]
      date: "1994"
      context: "CBC Writers & Company interview with Eleanor Wachtel; after the span (P20). Cultural/political framing of the novel, not a scored personal return to traditional religion."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
    - text: "I often had periods of oscillating faith as I grew older, periods of doubt, when I quietly pondered, and deeply questioned, the absolutist teachings or the interpretations of religion. I struggled with the certitude of Christianity—“I am the Way, the Truth and the Life”—not its accuracy, because as a writer one understands that there should be such latitude, but the desolation, the acerbity of its meaning, the lack of options for the outsider, the other."
      cites: [{source: S2, locator: "excerpt"}]
      date: "2012"
      context: "There Was a Country (2012), excerpt in Guernica; after the span (P20)."
      axes: [A_locus]
      kind: "autobiography"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
    - text: "Igbo sayings and proverbs are far more valuable to me as a human being in understanding the complexity of the world than the doctrinaire, self-righteous strain of the Christian faith I was taught. This other religion is also far more artistically satisfying to me."
      cites: [{source: S2, locator: "excerpt"}]
      date: "2012"
      context: "Guernica excerpt of There Was a Country; after the span (P20). Artistic/cultural preference, not scored as ANIM profession."
      axes: [A_locus]
      kind: "autobiography"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
  changes_over_life: []
  coder_notes: "Deepen D1 2026-10-24: Paris Review opened in full; PN Review (S6) and CBC 1994 (S7) added; Guernica memoir re-confirmed; Wikipedia dual bio (S5). All own-voice religion material is after the 1958 span (P20) — lead only. Named for Victoria, Queen of England (New Letters 1973; Morning Yet / Hopes and Impediments) still unread (IA borrow-only / no free full text). Britannica blocked. Do not code Okonkwo, Ezeulu, or other fiction as authorial (P42). Keep BELOW/UNKNOWN; do not force plot. Chart-moving NO."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Igbo", certainty: 1.0, cites: [{source: S1, locator: "first answer"}, {source: S5, locator: "Youth and background"}], how_known: "Interviews and Wikipedia."}
  religious_heritage_by_birth: {value: "Anglican Christian (CMS)", certainty: 1.0, cites: [{source: S3, locator: "opening"}, {source: S5, locator: "Youth and background"}, {source: S6, locator: "opening"}], how_known: "Innes; Wikipedia; PN Review."}
  baptism_or_initiation: {value: "Christened Albert Chinụalụmọgụ", certainty: 1.0, cites: [{source: S3, locator: "opening"}, {source: S5, locator: "lead"}], how_known: "Innes; Wikipedia."}
  childhood_catechism: {value: "Sunday school; family Bible readings; parish assistance at St. Philip's, Ogidi", certainty: 0.7, cites: [{source: S2, locator: "excerpt"}, {source: S6, locator: "opening"}], how_known: "Memoir; PN Review."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1958", certainty: 0.5, cites: [{source: S1, locator: "headnote"}, {source: S5, locator: "lead"}], how_known: "Things Fall Apart, the only work taken as lasting for the span this pass (P29, P30); African Trilogy later novels remain candidates if lastingness is raised later."}
  age_at_first_lasting_contribution: {value: 28, certainty: 1.0, cites: [{source: S3, locator: "opening"}, {source: S1, locator: "headnote"}, {source: S5, locator: "infobox"}], how_known: "1958 − 1930 = 28 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No in-span LIO statement; after-span interviews/memoir are P20 leads only."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None in span."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None in span."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Fiction and essays; no geometric cosmology claimed as his belief model.", certainty: 0.5, cites: [{source: S1, locator: "headnote"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "headnote"}], how_known: "Coder's reading."}
  reading: "No Lane B finding. Igbo chi / Chukwu explanations in interviews are cultural exposition, not a coded belief model for him."
  notes: "P42: do not import Okonkwo's or Ezeulu's gods as Achebe's locus."

institutions:
  - {value: "Nigerian Broadcasting Corporation", role: "radio producer; Director of External Broadcasting", years: "1954–1960s", kind: "government or state body", certainty: 0.7, cites: [{source: S1, locator: "headnote"}, {source: S5, locator: "Teaching and producing"}], how_known: "Paris Review; Wikipedia."}
  - {value: "Heinemann African Writers Series", role: "founding / general editor", years: "1960s–", kind: "commercial", certainty: 0.7, cites: [{source: S1, locator: "headnote"}, {source: S5, locator: "Voice of Nigeria and African Writers Series"}], how_known: "Paris Review; Wikipedia."}
collaborators:
  - {value: "Geoffrey Parrinder", relation: teacher, note: "West African religions at Ibadan", certainty: 0.7, cites: [{source: S1, locator: "Ibadan answer"}], how_known: "(interview)."}
  - {value: "James Welch", relation: teacher, note: "religion department, Ibadan; later helped him into broadcasting", certainty: 0.7, cites: [{source: S1, locator: "Ibadan / broadcasting answers"}], how_known: "(interview)."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 156"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Britannica would not load this deepen (403); death day/place and some basics rest on Wikipedia EN plus CBC year-of-death — P50 dual bio incomplete for death place."
    - "Named for Victoria, Queen of England (1973) flagged since creation; still no free full text (IA print-disabled)."
    - "All religion own-voice so far is after the 1958 span (P20)."
  open_questions:
    - "Full text of Named for Victoria (1973) and other Morning Yet on Creation Day essays for any nearer-span religion profession."
    - "Second independent source for death place (Boston) beyond Wikipedia."
    - "Any 1957–1960 interview or essay with a clear personal religious profession."

sources:
  - id: S1
    type: primary
    kind: other
    author: "Chinua Achebe, interviewed by Jerome Brooks"
    citation: "Brooks, Jerome. \"Chinua Achebe, The Art of Fiction No. 139.\" The Paris Review 133 (Winter 1994). https://www.theparisreview.org/interviews/1720/the-art-of-fiction-no-139-chinua-achebe"
    url: "https://www.theparisreview.org/interviews/1720/the-art-of-fiction-no-139-chinua-achebe"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "Published interview transcript (P8) with an editorial headnote. After the span for worldview use (P20)."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Chinua Achebe"
    citation: "Achebe, Chinua. \"How Things Fell Apart\" (excerpt from There Was a Country, Penguin 2012). Guernica, 15 October 2012. https://www.guernicamag.com/how-things-fell-apart/"
    url: "https://www.guernicamag.com/how-things-fell-apart/"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "Authorized excerpt of his memoir; after the span (P20)."
    used_for: [basics, childhood, worldview, heritage]
  - id: S3
    type: secondary
    kind: "book chapter"
    author: "C. L. Innes"
    citation: "Innes, C. L. \"Origins.\" In Chinua Achebe (Cambridge University Press, 1990). doi:10.1017/cbo9780511554407.003"
    url: "https://doi.org/10.1017/cbo9780511554407.003"
    accessed: 2026-10-19
    source_quality: "scholarly edition or monograph"
    reliability_note: "Scholarly monograph; opening read via excerpt."
    used_for: [identity, basics, childhood, heritage, timing]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    source_quality: "study roster"
    reliability_note: "Study's own roster."
    used_for: [review]
  - id: S5
    type: secondary
    kind: "encyclopedia"
    author: "Wikipedia contributors"
    citation: "Chinua Achebe. Wikipedia. https://en.wikipedia.org/wiki/Chinua_Achebe"
    url: "https://en.wikipedia.org/wiki/Chinua_Achebe"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Unsigned tertiary; dual-source bio (P50) against Innes/Paris Review for birth, parents, career; death day/place lack a second independent source this pass (Britannica 403)."
    used_for: [identity, basics, contribution, childhood, heritage, timing, institutions, review]
  - id: S6
    type: primary
    kind: other
    author: "Chinua Achebe, interviewed by Brenda Lyons"
    citation: "Lyons, Brenda. \"In Conversation with Chinua Achebe.\" PN Review 219, vol. 41 no. 1 (September–October 2014). https://www.pnreview.co.uk/archive/in-conversation-with-chinua-achebe/9167"
    url: "https://www.pnreview.co.uk/archive/in-conversation-with-chinua-achebe/9167"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "Published interview transcript (P8). Interview date not stated on the page; published 2014 after his death — treat as after-span for worldview (P20)."
    used_for: [childhood, worldview, heritage]
  - id: S7
    type: primary
    kind: other
    author: "Chinua Achebe, interviewed by Eleanor Wachtel"
    citation: "Wachtel, Eleanor. \"Chinua Achebe on redefining Nigeria with his writing.\" CBC Radio Writers & Company (interview 1994; page updated 2016). https://www.cbc.ca/radio/writersandcompany/chinua-achebe-on-redefining-nigeria-with-his-writing-1.3689009"
    url: "https://www.cbc.ca/radio/writersandcompany/chinua-achebe-on-redefining-nigeria-with-his-writing-1.3689009"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "Broadcast interview transcript excerpts on the CBC page (P8). 1994 — after the span (P20)."
    used_for: [worldview, review]
---

## Summary

Chinua Achebe (1930–2013), Nigerian novelist [S1; S5]. Deepen D1: primary_system and A BELOW_THRESHOLD (lead CHRIST); B UNKNOWN; mid_basin UNKNOWN. Not plotted. Chart-moving NO.

## Life and work

Born near Ogidi (Nneobi), Colonial Nigeria; CMS catechist's son; University College Ibadan; Nigerian Broadcasting Corporation; later Bard and Brown [S1; S5]. Died Boston, 21 March 2013 [S5].

## Contribution and impact

Things Fall Apart (1958) — magnum opus; African Writers Series editor; Man Booker International 2007 [S1; S5].

## Childhood and education

Anglican compound beside a still-active Igbo traditional world; great-uncle Udoh Osinyi (ozo) refused conversion; Ibadan comparative religion with Parrinder [S1; S2; S5; S6].

## Adult working worldview

No in-span profession. After-span leads only (P20): oscillating faith and preference for Igbo proverbial complexity over Christian certitude [S2]; chi/Chukwu as cultural exposition [S6]; novel as cultural atonement for ancestral-faith abandonment [S7]. Fiction characters not coded (P42). Lead CHRIST (upbringing). B not scored — not a scientist (P30).

## Heritage (context only)

Igbo; Anglican CMS [S1; S3; S5; S6].

## Timing

1958, age 28 [S1; S3; S5]. Span not expanded this pass.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No geometric belief model. P42: Okonkwo/Ezeulu gods are not Achebe's locus.

## Open questions

- Named for Victoria (1973) and other near-span essays.
- Second source for death place.
- Any 1957–1960 personal religious profession.

## Research log

- 2026-10-19: Read Paris Review interview; Guernica memoir excerpt; Innes excerpt.
- 2026-10-24: Deepen D1 — Paris Review re-opened; Guernica re-confirmed; Wikipedia S5; PN Review S6; CBC 1994 S7. Named for Victoria still unread. Scores unchanged; chart NO.
