---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA1; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #171/228, F 3, rank 181). Goals: adult ATHE/AGNOS own words; open A if warranted; do not force plot. Re-read CMU Models of My Life typescript OCR in full for religion (S3): schoolboy Christian Endeavor 'while insisting on his agnosticism'; grammar-school Milwaukee Journal letter 'in defense of atheism'; Congregational communion — remained seated at 'Will all Christians please rise?'; Chicago 'neither of us being swept up by the theologies we encountered'; lifelong 'logical positivism … (I would prefer to call it empiricism now)'. No adult first-person 'I am an atheist/agnostic' in the OCR. Read Velupillai & Venkatachalam 2018 Open Access PDF in full (S5): 'He described himself as an atheist' with general debt to Models (1996) but no page locator for that claim. Crowther-Heyck 2005 p.22 (S6): by high school 'certain' he was 'religiously an atheist' — wording from Wikipedia EN cite-book quote attribute; page images unread; 'a conviction that never wavered' is biographer framing outside Simon quotes. Primary stays BELOW_THRESHOLD (leads AGNOS, ATHE; schoolboy before span, P29; secondary ATHE paraphrase insufficient). A stays BELOW_THRESHOLD. B stays 3 @0.5 alt 4 (P35); support labelled corroborated (S1+S2, P48). mid_basin BELOW. Not plotted. P47 on S1–S6. No fallacy_catalog. No figures/. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "AA1 audit fix (WEAKEN, P21): the Models of My Life statement was read only in OCR of the CMU archive scan, so verified_against 'primary facsimile' -> new value 'archive scan (OCR only)'. Unscored; no effect."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA1, order P32: F 3, rank 181). Basics from NobelPrize.org (facts; autobiography 1978) and Britannica (archived 2020, body: 'his influential book Administrative Behavior (1947)'). Own words: Models of My Life (draft, Carnegie Mellon University Libraries, Simon papers), after the span: as a schoolboy in Christian Endeavor 'while insisting on his agnosticism' (before the span); at Chicago, 'neither of us being swept up by the theologies we encountered'; 'a logical positivism that I have never relinquished (I would prefer to call it empiricism now)'. A secondary account (Velupillai and Venkatachalam) says he 'described himself as an atheist' (no locator). No adult statement on God read, so primary_system BELOW_THRESHOLD (leads AGNOS, ATHE); A BELOW_THRESHOLD. Scientist: his decision theory makes testable claims about decision behaviour in organizations (P35 addendum), so B 3 at 0.5 from working science, alt 4. C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD. Span 1947, age 31. Not plotted. Draft, not reviewed."}

identity:
  id: simon-herbert
  display_name: "Herbert Simon"
  roster:
    canonical_name: "Herbert Simon"
    rank: 181
    F: 3
    models: [Claude, DeepSeek, GPT]
    band: "core (3–4)"
    status: "core"
    field: "computer science"
    field_bucket: "computer science / AI"
  full_name: {value: "Herbert Alexander Simon", certainty: 0.7, cites: [{source: S2, locator: "opening"}], how_known: "Britannica."}
  native_name: {value: "Herbert A. Simon", certainty: 0.7, cites: [{source: S1, locator: "heading"}], how_known: "NobelPrize.org."}
  aliases:
    - {name: "Simon-Herbert", kind: "roster alias"}

basics:
  birth:
    date: {value: "1916-06-15", certainty: 0.7, cites: [{source: S1, locator: "Born"}], how_known: "NobelPrize.org."}
    place: {value: "Milwaukee, Wisconsin", modern_name: "Milwaukee, Wisconsin, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "Born"}], how_known: "NobelPrize.org."}
  death:
    date: {value: "2001-02-09", certainty: 0.7, cites: [{source: S1, locator: "Died"}], how_known: "NobelPrize.org."}
    place: {value: "Pittsburgh, Pennsylvania", modern_name: "Pittsburgh, Pennsylvania, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "Died"}], how_known: "NobelPrize.org."}
  first_lasting_contribution_year: {value: 1947, certainty: 0.7, cites: [{source: S2, locator: "para. 3"}], how_known: "'his influential book Administrative Behavior (1947)' (S2, body); publication (P30 #1)."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S2, locator: "para. 3"}], how_known: "1947 (P2)."}
  region_of_birth: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "Born"}], how_known: "USA (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "Life"}], how_known: "Chicago; Pittsburgh."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S3, locator: "text"}], how_known: "English text."}
  occupations: {value: ["economist", "political scientist", "psychologist", "computer scientist"], certainty: 0.7, cites: [{source: S2, locator: "opening"}], how_known: "Britannica."}

contribution:
  fields: {value: ["economics", "organization theory", "cognitive psychology", "artificial intelligence"], certainty: 0.7, cites: [{source: S2, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Theory of decision making in organizations and satisficing (Administrative Behavior)", year: 1947, kind: "theory", lasting: "'his influential book Administrative Behavior (1947)' (S2); Nobel Prize 1978 'for his pioneering research into the decision-making process within economic organizations' (S1)", certainty: 0.7, cites: [{source: S2, locator: "para. 3–4"}, {source: S1, locator: "Prize motivation"}], how_known: "Britannica body (archived) and NobelPrize.org."}
  evidence_of_impact:
    - {value: "Nobel Prize in Economic Sciences 1978; Turing Award 1975 (with Newell)", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S2, locator: "opening"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Nobel and Turing laureate (S2).", certainty: 0.7, cites: [{source: S2, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated as a family creed; heritage notes Jewish father-side and Lutheran/Jewish/Catholic mother-side forebears (S1, S5)."}
  family_religious_practice: {value: "Congregational Sunday school and church attendance in childhood/adolescence (not a synagogue)", certainty: 0.5, cites: [{source: S3, locator: "ch. 1, 'On Being Different'"}], how_known: "Own words in Models draft (OCR): 'not a religious Jew … attended Congregational Sunday school through his grammar and high school years'."}
  parents_and_household:
    - {value: "Father an electrical engineer (Technische Hochschule Darmstadt diploma), an immigrant from Germany", role: "father", certainty: 0.7, cites: [{source: S1, locator: "autobiography"}], how_known: "NobelPrize.org autobiography."}
    - {value: "Mother an accomplished pianist, third-generation American", role: "mother", certainty: 0.7, cites: [{source: S1, locator: "autobiography"}], how_known: "NobelPrize.org autobiography."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling: []
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events:
    - {value: "Grammar-school letter to the Milwaukee Journal 'in defense of atheism' (published); father forbade further letters", year: "before 1933", certainty: 0.5, cites: [{source: S3, locator: "ch. 8, 'Liberalism: Depression Style'"}], how_known: "Own words in Models draft (OCR); before the span (P29)."}
    - {value: "High-school Christian Endeavor membership 'while insisting on his agnosticism'", year: "before 1933", certainty: 0.5, cites: [{source: S3, locator: "ch. 1, high-school clubs"}], how_known: "Own words in Models draft (OCR), third-person childhood voice; before the span (P29)."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1947", certainty: 0.7, cites: [{source: S2, locator: "para. 3"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read as an explicit science–religion relation; lifelong logical positivism/empiricism is a D lead only."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "No adult first-person profession on God inside or about the span (P19, P29). Own words in Models of My Life typescript (S3, OCR): schoolboy AGNOS (Christian Endeavor) and a grammar-school letter 'in defense of atheism' — both before the span; Chicago years not 'swept up by the theologies'; lifelong logical positivism renamed empiricism (D lead, not A). Secondary: Velupillai & Venkatachalam (S5) 'He described himself as an atheist' (no locator); Crowther-Heyck (S6) schoolboy 'religiously an atheist' with biographer 'never wavered' outside Simon quotes. Leads AGNOS and ATHE remain; neither is a verified adult own-words score."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: AGNOS, reason: "Lead: schoolboy Christian Endeavor 'insisting on his agnosticism' (S3, before span); adult positivism/empiricism is only a D lead."}
    - {code: ATHE, reason: "Lead: schoolboy letter 'in defense of atheism' (S3); Crowther-Heyck schoolboy 'religiously an atheist' (S6); Velupillai secondary 'described himself as an atheist' (S5, no locator). No adult own-words locator verified."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "No adult locus view on God read (P19). Schoolboy AGNOS/ATHE evidence is before the span (P29). Logical positivism is a lead that God-talk is meaningless, not a stated view scoring A. Secondary ATHE claims (S5, S6) do not alone open A."}
    B_cause:
      value: 3
      basis: inference_from_work
      certainty: 0.5
      support: corroborated
      cites: [{source: S2, locator: "para. 3–4"}, {source: S1, locator: "Prize motivation"}]
      how_known: "Scientist (P30, P35 addendum): his decision theory makes testable empirical claims about decision processes in organizations (S1, S2). B from working science with no statement of his own on law and exception, so 3 at 0.5, alternative 4, never 4 (P24, P35). Two independent source ids (Britannica + Nobel) → corroborated (P48)."
      rationale: "Theory of how people actually decide in organizations (S1, S2); lawful, empirically testable behaviour. Alternative 4."
      alternatives:
        - {value: 4, note: "Working science cannot tell lawful-with-exceptions from exceptionless (P35).", cites: [{source: S2, locator: "para. 3–4"}]}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not scored. Lead only: lifelong logical positivism/empiricism (S3) and Chicago philosophy-of-science circle where 'Logical positivism was the dominant, perhaps exclusive, religion' (metaphor; S3)."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD, so the P4 test cannot be applied."}
  statements:
    - text: "He was active in a debating society, a science club, the Christian Endeavor (while insisting on his agnosticism), the Latin club, and the student council"
      cites: [{source: S3, locator: "ch. 1, high-school clubs"}]
      date: "1991"
      context: "Models of My Life typescript (CMU); childhood third-person voice about high school (before the span)."
      axes: []
      kind: "autobiography"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Schoolboy AGNOS lead only (P29). Not scored for primary/A."
    - text: "While yet in grammar school, I wrote a letter to the Milwaukee Journal (it was published) in defense of atheism, and signed my name and address."
      cites: [{source: S3, locator: "ch. 8, 'Liberalism: Depression Style'"}]
      date: "1991"
      context: "Models of My Life typescript (CMU); adult autobiography recalling grammar school (before the span)."
      axes: []
      kind: "autobiography"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Schoolboy ATHE lead only (P29). Not scored for primary/A."
    - text: "Then the minister would ask, \"Will all Christians please rise?\" Only the boy remained seated. It was very difficult, but he would have felt ashamed if he had falsified his beliefs publicly."
      cites: [{source: S3, locator: "ch. 1, Congregational communion"}]
      date: "1991"
      context: "Models of My Life typescript (CMU); childhood nonconformity at Congregational communion (before the span)."
      axes: []
      kind: "autobiography"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "Refusal to identify as Christian; does not alone score ATHE/AGNOS for the adult working unit."
    - text: "I had already embraced a logical positivism that I have never relinquished (I would prefer to call it empiricism now)"
      cites: [{source: S3, locator: "ch. 3, 'Education in Chicago, 1933–1937'"}]
      date: "1991"
      context: "Models of My Life typescript (CMU); about Chicago years; written after the span; lifelong claim."
      axes: [D_authority]
      kind: "autobiography"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "D lead only; not a stated locus view on God (A stays BELOW). Read in OCR; page images not viewed (P21)."
  changes_over_life: []
  coder_notes: "D1 2026-10-24: Published Basic Books / MIT Press Models of My Life still not borrowed page-by-page; CMU 1990 typescript OCR is the only continuous own-words text read. Crowther-Heyck's quoted 'religiously an atheist' / biographer 'never wavered' not found in that OCR — page-image or published-edition locator still needed before any adult ATHE open. Do not force plot without A."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Lutheran and Jewish forebears; attended Congregational Sunday school", certainty: 0.5, cites: [{source: S1, locator: "autobiography"}, {source: S3, locator: "ch. 1"}, {source: S5, locator: "opening logistics paragraph"}], how_known: "Nobel autobiography lists the Lutheran Merkels and Prague Goldschmidts; Models: 'not a religious Jew … attended Congregational Sunday school'; Velupillai notes Jewish father-side and partly Lutheran/Jewish/Catholic mother-side."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated as a birth creed."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1947", certainty: 0.7, cites: [{source: S2, locator: "para. 3"}], how_known: "Administrative Behavior (1947), the one listed lasting work (P29, P30)."}
  age_at_first_lasting_contribution: {value: 31, certainty: 0.7, cites: [{source: S1, locator: "Born"}, {source: S2, locator: "para. 3"}], how_known: "1947 − 1916 = 31 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: "schoolboy (pre-1933): Christian Endeavor agnosticism; Milwaukee Journal atheism letter", certainty: 0.5, cites: [{source: S3, locator: "ch. 1; ch. 8"}], how_known: "Own words about childhood; before the span (P29) — not timing for the adult working code."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "No adult working-years profession verified."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None verified for 1947."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "Formal models of decision (S2).", certainty: 0.5, cites: [{source: S2, locator: "para. 3–4"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "Carnegie Institute of Technology (Carnegie Mellon University)", role: "professor", years: "1949–2001", kind: "university", certainty: 0.7, cites: [{source: S2, locator: "para. 2"}], how_known: "Britannica; end year his death."}
collaborators:
  - {value: "Allen Newell", relation: "collaborator", note: "Turing Award 1975", certainty: 0.7, cites: [{source: S2, locator: "opening"}], how_known: "Britannica."}
  - {value: "Harold Guetzkow", relation: "collaborator", note: "Chicago friend; organizational studies", certainty: 0.7, cites: [{source: S3, locator: "ch. 3"}], how_known: "Own words."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 181"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "No adult first-person ATHE/AGNOS verified in published Models; Crowther-Heyck p.22 page images unread."
    - "Models of My Life read only as CMU typescript OCR (P21 / P47 archive scan)."
  open_questions:
    - "Published Models of My Life (Basic Books 1991 / MIT Press 1996) page for Crowther-Heyck's 'religiously an atheist' wording — not found in CMU OCR."
    - "Any adult interview or questionnaire self-label ATHE/AGNOS inside or about the span."

sources:
  - id: S1
    type: tertiary
    kind: "institutional page"
    author: "Nobel Foundation"
    citation: "'Herbert A. Simon – Facts' and 'Biographical.' NobelPrize.org. https://www.nobelprize.org/prizes/economic-sciences/1978/simon/facts/"
    url: "https://www.nobelprize.org/prizes/economic-sciences/1978/simon/facts/"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Official prize pages; autobiography written at the award. No adult religion self-label in the Facts/Biographical pages read."
    used_for: [identity, basics, contribution, childhood, worldview]
  - id: S2
    type: tertiary
    kind: "encyclopedia"
    author: "The Editors of Encyclopaedia Britannica (rev. William L. Hosch)"
    citation: "'Herbert A. Simon.' Encyclopaedia Britannica (last updated 11 June 2020). Archived 2020-07-31. https://web.archive.org/web/20200731075041/https://www.britannica.com/biography/Herbert-A-Simon"
    url: "https://web.archive.org/web/20200731075041/https://www.britannica.com/biography/Herbert-A-Simon"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Archived article body, read in full."
    used_for: [identity, basics, contribution, timing, institutions, collaborators, worldview]
  - id: S3
    type: primary
    kind: "archive record"
    author: "Herbert A. Simon"
    citation: "Simon, Herbert A. Models of My Life (typescript draft, 2 June 1990). Herbert A. Simon Papers, Carnegie Mellon University Libraries, box 76, folder 5972. https://iiif.library.cmu.edu/file/Simon_box00076_fld05972_bdl0001_doc0001/Simon_box00076_fld05972_bdl0001_doc0001.pdf"
    url: "https://iiif.library.cmu.edu/file/Simon_box00076_fld05972_bdl0001_doc0001/Simon_box00076_fld05972_bdl0001_doc0001.pdf"
    accessed: 2026-10-24
    source_quality: "archive scan (OCR only)"
    reliability_note: "Institution's scan of his typescript; religion passages re-read in OCR this pass; page images not viewed. Published 1991/1996 edition not borrowed page-by-page."
    used_for: [worldview, heritage, collaborators, childhood]
  - id: S4
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-24
    source_quality: "study roster"
    reliability_note: "Study's own roster."
    used_for: [review]
  - id: S5
    type: secondary
    kind: "journal article"
    author: "K. Vela Velupillai; Ragupathy Venkatachalam"
    citation: "Velupillai, K. V., and R. Venkatachalam. 'Herbert Alexander Simon: 15th June, 1916–9th February, 2001 A Life.' Computational Economics (2018). Open Access PDF: https://research.gold.ac.uk/id/eprint/23181/1/Simon_Life_Vela_Ragu.pdf"
    url: "https://research.gold.ac.uk/id/eprint/23181/1/Simon_Life_Vela_Ragu.pdf"
    accessed: 2026-10-24
    source_quality: "scholarly edition or monograph"
    reliability_note: "Read in full (short essay). Opening: 'He described himself as an atheist.' Essay says it is indebted to Models of My Life (Simon 1996) for most personal details, but gives no page locator for the atheist claim. Secondary paraphrase only."
    used_for: [worldview, heritage]
  - id: S6
    type: secondary
    kind: "scholarly book"
    author: "Hunter Crowther-Heyck"
    citation: "Crowther-Heyck, Hunter. Herbert A. Simon: The Bounds of Reason in Modern America. Johns Hopkins University Press, 2005, p. 22. (Wording as reproduced in the Wikipedia EN cite-book quote attribute for Herbert A. Simon, Early life and education.)"
    url: "https://en.wikipedia.org/wiki/Herbert_A._Simon"
    accessed: 2026-10-24
    source_quality: "scholarly edition or monograph"
    reliability_note: "Page images of Crowther-Heyck p.22 not obtained this pass. Wikipedia cite-book quote: by high school he was 'certain' he was 'religiously an atheist', 'a conviction that never wavered' — the last clause is outside Simon quotation marks (biographer framing). Schoolboy claim; not used to open primary/A."
    used_for: [worldview]
---

## Summary

Herbert A. Simon (1916–2001), social scientist and AI pioneer [S1, S2]. Draft deepen D1: primary_system BELOW_THRESHOLD (leads AGNOS, ATHE); A BELOW_THRESHOLD; B 3 (0.5, corroborated). Not plotted.

## Life and work

Milwaukee; Chicago; Carnegie Mellon [S1, S2].

## Contribution and impact

Decision making and satisficing; Administrative Behavior (1947) [S2].

## Childhood and education

Milwaukee public schools; Congregational Sunday school; schoolboy Christian Endeavor with insisted agnosticism; Milwaukee Journal letter in defense of atheism [S1, S3].

## Adult working worldview

No verified adult first-person ATHE/AGNOS for the 1947 span. Autobiography recalls schoolboy nonconformity and a lifelong logical positivism/empiricism (D lead) [S3]. Secondary ATHE claims (Velupillai; Crowther-Heyck) remain leads [S5, S6].

## Heritage (context only)

Jewish father-side; Lutheran/Jewish/Catholic mother-side forebears; Congregational Sunday school [S1, S3, S5].

## Timing

1947, age 31 [S2].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Published Models of My Life page for Crowther-Heyck's "religiously an atheist" wording.
- Adult interview or other first-person ATHE/AGNOS about the working years.

## Research log

- 2026-10-24: Deepen D1. Re-read Models typescript OCR (S3); Velupillai PDF full (S5); Crowther-Heyck p.22 via Wikipedia cite-book quote (S6). Primary/A stay BELOW; B support corroborated. No fallacy_catalog. No figures/.
- 2026-10-19: AA1 audit fix (WEAKEN, P21): the Models of My Life statement was read only in OCR of the CMU archive scan, so verified_against 'primary facsimile' -> new value 'archive scan (OCR only)'. Unscored; no effect.
- 2026-10-19: Read NobelPrize.org; Britannica (archived); Models of My Life typescript.
