---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch S)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-18
  last_updated: 2026-10-18
  change_log:
    - {date: 2026-10-18, by: "Grok Bot", summary: "Record created (stage 3 batch S, order P32: F 4, rank 106). Basics from Britannica (Brian C. Southam, signed; body only, read live). Worldview from her letters to Fanny Knight in the Brabourne edition (1884), read in the Republic of Pemberley's web transcription (unofficial web copy, 0.7 cap). Not a scientist. primary_system CHRIST (0.7, consistent private letters); A BELOW_THRESHOLD; B UNKNOWN (P16, P19); C BELOW_THRESHOLD; D, E UNKNOWN; mid_basin UNKNOWN. Not plotted. The three prayers attributed to her are context only (attribution not settled, P42). Draft, not reviewed."}

identity:
  id: austen-jane
  display_name: "Jane Austen"
  roster:
    canonical_name: "Jane Austen"
    rank: 106
    F: 4
    models: [DeepSeek, Gemini, GPT, Grok]
    band: "core (3–4)"
    status: core
    field: literature
    field_bucket: literature
  full_name: {value: "Jane Austen", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  native_name: {value: "Jane Austen", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "English; same as the display name."}
  aliases:
    - {name: "Austen-Jane", kind: "roster alias"}
    - {name: "Jane-Austen", kind: "roster alias"}

basics:
  birth:
    date: {value: "1775-12-16", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica body."}
    place: {value: "Steventon, Hampshire, England", modern_name: "Steventon, United Kingdom", polity_then: "Kingdom of Great Britain", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Early life and family'"}], how_known: "Britannica."}
  death:
    date: {value: "1817-07-18", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening; 'Unfinished works and death'"}], how_known: "Britannica body."}
    place: {value: "Winchester, Hampshire, England", modern_name: "Winchester, United Kingdom", polity_then: "United Kingdom of Great Britain and Ireland", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1811, certainty: 0.7, cites: [{source: S1, locator: "'Move to Chawton and publishing success'"}], how_known: "Sense and Sensibility, published November 1811, the earliest listed novel (P13, P30: first publication is its first public statement; drafts from about 1795 were not public)."}
  era_bucket: {value: "1750 to 1849", certainty: 0.7, cites: [{source: S1, locator: "'Move to Chawton and publishing success'"}], how_known: "1811 (P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "United Kingdom (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "'Move to Chawton and publishing success'"}], how_known: "Chawton, Hampshire."}
  sex_as_recorded: {value: "female", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica ('English writer')."}
  occupations: {value: ["novelist"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

contribution:
  fields: {value: ["the novel"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Sense and Sensibility", year: 1811, kind: work, lasting: "'timeless classics that remained critical and popular successes for more than two centuries' (S1, of the novels)", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Move to Chawton and publishing success'"}], how_known: "Britannica (November 1811)."}
    - {value: "Pride and Prejudice", year: 1813, kind: work, lasting: "as above (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Move to Chawton and publishing success'"}], how_known: "Britannica (January 1813)."}
    - {value: "Mansfield Park", year: 1814, kind: work, lasting: "as above (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Move to Chawton and publishing success'"}], how_known: "Britannica."}
    - {value: "Emma", year: 1815, kind: work, lasting: "as above (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Move to Chawton and publishing success'"}], how_known: "Britannica (December 1815)."}
    - {value: "Persuasion", year: 1816, kind: work, lasting: "as above (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Move to Chawton and publishing success'; 'Unfinished works and death'"}], how_known: "Published posthumously in December 1817; dated by its last documented act in life, the end of writing in August 1816 ('written August 1815–August 1816'; P30 posthumous rule). The latest listed lasting contribution (P30 addendum). Northanger Abbey (written about 1798–99, looked at again in 1816, published with Persuasion) is not listed separately; its 1816 revisit gives the same end year."}
  evidence_of_impact:
    - {value: "'first gave the novel its distinctly modern character'; Scott's review of Emma (1816) and Whately's (1821) 'provided the foundation for serious criticism'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Unfinished works and death'"}], how_known: "Britannica (signed)."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Church of England: father the Anglican rector of Steventon", certainty: 0.7, cites: [{source: S1, locator: "'Early life and family'"}], how_known: "Britannica."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father George Austen, Anglican rector and scholar who 'encouraged the love of learning in his children'; mother Cassandra Austen (née Leigh); seventh of eight children; closest companion her sister Cassandra", certainty: 0.7, cites: [{source: S1, locator: "'Early life and family'"}], how_known: "Britannica."}
  household_circumstances: {value: "Steventon rectory; family theatricals ('The great family amusement was acting')", certainty: 0.7, cites: [{source: S1, locator: "'Early life and family'"}], how_known: "Britannica."}
  schooling: []
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["English"], certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  notable_events:
    - {value: "Juvenilia in three manuscript notebooks, about 1787–1793", certainty: 0.7, cites: [{source: S1, locator: "'Early writings'"}], how_known: "Britannica."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1811–1816", certainty: 0.7, cites: [{source: S1, locator: "'Move to Chawton and publishing success'"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Church of England (rector's daughter)", certainty: 0.7, cites: [{source: S1, locator: "'Early life and family'"}], how_known: "Context only; the code rests on her letters."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing on science in the letters read (Brabourne letters LXXX–LXXXIV, S2)."}
  primary_system:
    value: CHRIST
    basis: consistent_private_letters
    certainty: 0.7
    cites: [{source: S2, locator: "letters LXXX (18 November 1814) and LXXXI (30 November 1814)"}]
    rationale: "CHRIST's v8 note: Christian belief (Christ, scripture, creeds, church) shown in her own writing, with no more specific philosophical position. Two private letters to her niece, twelve days apart and consistent: she is 'by no means convinced that we ought not all to be evangelicals', the suitor's 'acting more strictly up to the precepts of the New Testament' is no objection, and 'I cannot suppose we differ in our ideas of the Christian religion'. No other code was considered plausible: CLTHEI needs a God who intervenes beyond the creeds, which the letters do not show."
    how_known: "Two consistent private letters (0.7 ceiling), inside the working years; read in an unofficial web copy of the Brabourne edition, which is also capped at 0.7."
  secondary_system: {value: UNKNOWN, how_known: "One system (P29)."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Letters of November 1814 (S2)."}
    - {code: CLTHEI, reason: "Rejected: no petition or intervention beyond ordinary Christian piety in the letters read; the Evening Prayer's petitions for travellers are in a text whose attribution is not settled (P42)."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, cites: [{source: S2, locator: "letter LXXXIII"}, {source: S3, locator: "opening; manuscript paragraph"}], how_known: "The only locus-bearing line read is 'I hope Heaven, in its mercy, will take her soon' (letter LXXXIII, 13 March 1817, of her dying niece Harriot): one private letter, conventional wording, after the working years (P20). The Evening Prayer ('Thou art every where present') is context only: Todd and Bree's Cambridge edition prints the prayers in an appendix and the attribution rests on the inscription 'Prayers Composed by my ever dear Sister Jane' (S3) (P42; lead).", note: "Lead: the prayers, if the attribution were accepted, would place a personal, everywhere-present God who hears petition (A 0 or 1)."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30), and no statement on nature or the physical world in the letters read (P16, P19). The 1817 hope that 'Heaven, in its mercy' will take Harriot is about a death, not an account of nature's order; checked and found off-point."}
    C_ledger: {value: BELOW_THRESHOLD, how_known: "Evangelicals 'from reason and feeling must be happiest and safest' (letter LXXX) may refer to salvation, but the sense is not explicit; 'if we believe the doctrine of original sin' (letter LXXXII, February 1817) is playful. Too indirect (P19)."}
    D_authority: {value: UNKNOWN, how_known: "Nothing on revelation against observation or reason in the letters read (S2)."}
    E_scope: {value: UNKNOWN, how_known: "Nothing on the world's order in the letters read (S2)."}
  mid_basin: {value: UNKNOWN, how_known: "P4 test: B is UNKNOWN, which takes precedence (P19); A is BELOW_THRESHOLD."}
  statements:
    - text: "And, as to there being any objection from his goodness, from the danger of his becoming even evangelical, I cannot admit that.  I am by no means convinced that we ought not all to be evangelicals, and am at least persuaded that they who are so from reason and feeling must be happiest and safest."
      cites: [{source: S2, locator: "letter LXXX, Chawton, Friday 18 November 1814"}]
      date: "1814-11-18"
      context: "Letter to her niece Fanny Knight, advising on a suitor whose religious seriousness Fanny feared; she goes on 'don't be frightened by the idea of his acting more strictly up to the precepts of the New Testament than others.'"
      axes: [C_ledger]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-18
      note: "Brabourne edition (1884), read in the Republic of Pemberley's web transcription; Le Faye numbering not checked (TODO)."
    - text: "I cannot suppose we differ in our ideas of the Christian religion.  You have given an excellent description of it.  We only affix a different meaning to the word evangelical."
      cites: [{source: S2, locator: "letter LXXXI, 23 Hans Place, Wednesday 30 November 1814"}]
      date: "1814-11-30"
      context: "Letter to Fanny Knight, answering Fanny's account of the Christian religion."
      axes: []
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-18
      note: "As above. Supports primary_system only."
    - text: "I hope Heaven, in its mercy, will take her soon."
      cites: [{source: S2, locator: "letter LXXXIII, Chawton, Thursday 13 March [1817]"}]
      date: "1817-03-13"
      context: "Letter to Fanny Knight, of her niece Harriot, diagnosed with 'water on the brain'. Brabourne dates it 1816; the transcription's note says it is 1817. After the working years."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "scholarly edition"
      verified_on: 2026-10-18
      note: "As above."
  changes_over_life: []
  coder_notes: "Coder's call. CHRIST rests on two private letters of November 1814; nothing read bears on nature, so B is UNKNOWN and she is not plotted. The Evening Prayer and two other prayers (Mills College manuscript) are a lead only: the attribution rests on the inscription 'Prayers Composed by my ever dear Sister Jane' (JASNA, Stovel), and the Cambridge Later Manuscripts edition prints them as Appendix D. Words that the Pemberley transcription restores from outside the Brabourne text are not quoted."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "English (Hampshire gentry and clergy)", certainty: 0.7, cites: [{source: S1, locator: "'Early life and family'"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Church of England", certainty: 0.7, cites: [{source: S1, locator: "'Early life and family'"}], how_known: "Britannica (father a rector)."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1811–1816", certainty: 0.7, cites: [{source: S1, locator: "'Move to Chawton and publishing success'"}], how_known: "Sense and Sensibility (1811) to Persuasion (finished August 1816; published posthumously December 1817), first to last listed lasting contribution (P29, P30 posthumous rule)."}
  age_at_first_lasting_contribution: {value: 36, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "1811 − 1775 = 36 (P30)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No statement of hers is scored at 3 or 4."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S2, locator: "letters LXXX–LXXXIV"}], how_known: "In the sources read."}
  worldview_during_major_work: {value: "Anglican Christian, sympathetic to evangelical seriousness", certainty: 0.7, cites: [{source: S2, locator: "letters LXXX, LXXXI"}], how_known: "Her letters of November 1814."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Novelist; no definition-to-consequence work.", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "'Early life and family'"}], how_known: "Not read."}
  circle_present: {value: "no", rationale: "No identification of God and Nature in the letters read.", certainty: 0.5, cites: [{source: S2, locator: "letters LXXX–LXXXIV"}], how_known: "Coder's reading."}
  reading: "An Anglican novelist with no stated view of nature: off the H1 axes."
  notes: ""

institutions: []
collaborators:
  - {value: "Henry Austen", relation: family, note: "brother; go-between with her publishers, announced her authorship", certainty: 0.7, cites: [{source: S1, locator: "'Move to Chawton'; 'Unfinished works and death'"}], how_known: "Britannica."}
  - {value: "Fanny Knight", relation: correspondent, note: "niece", certainty: 0.7, cites: [{source: S2, locator: "letters LXXX–LXXXIV"}], how_known: "The letters."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 106"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Letters read in an unofficial web transcription of the Brabourne edition (1884), which cuts some passages; the transcription restores some cut words in brackets (not quoted). Not checked against Le Faye's edition."
    - "Brabourne misdates letters LXXXII–LXXXIV to 1816; the transcription notes they are of 1817."
    - "Cassandra destroyed many letters; 'Only 160 out of thousands' survive (S1)."
  open_questions:
    - "Check the letters against Le Faye (4th ed.) and read the letters to Cassandra for religious remarks."
    - "Read Todd and Bree on the prayers' attribution (Later Manuscripts, pp. cxviii–cxxvi)."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Brian C. Southam"
    citation: "Southam, Brian C. \"Jane Austen.\" Encyclopaedia Britannica (revised 18 October 2026). https://www.britannica.com/biography/Jane-Austen. Read live 2026-10-18."
    url: "https://www.britannica.com/biography/Jane-Austen"
    accessed: 2026-10-18
    reliability_note: "Signed article. Body only; the AI-generated question boxes are not cited."
    used_for: [identity, basics, contribution, childhood, heritage, timing, collaborators, lane_b, worldview]
  - id: S2
    type: primary
    kind: "scholarly edition"
    author: "Jane Austen; ed. Edward, Lord Brabourne"
    citation: "Austen, Jane. Letters of Jane Austen, ed. Edward, Lord Brabourne (London: Richard Bentley, 1884), letters to Fanny Knight LXXX–LXXXIV. Web transcription: Republic of Pemberley, https://pemberley.com/janeinfo/brablt15.html"
    url: "https://pemberley.com/janeinfo/brablt15.html"
    accessed: 2026-10-18
    reliability_note: "Unofficial web copy of a Victorian edition (0.7 cap, §7); the edition omits some passages, which the transcription restores in brackets."
    used_for: [worldview, timing, collaborators, lane_b]
  - id: S3
    type: secondary
    kind: "journal article"
    author: "Bruce Stovel"
    citation: "Stovel, Bruce. \"'A Nation Improving in Religion': Jane Austen's Prayers and Their Place in Her Life and Art.\" Persuasions 16 (1994): 185–196. https://jasna.org/persuasions/printed/number16/stovel.htm"
    url: "https://jasna.org/persuasions/printed/number16/stovel.htm"
    accessed: 2026-10-18
    reliability_note: "Read the opening and the manuscript description only; lead for the prayers."
    used_for: [worldview]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-18
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Jane Austen

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Jane Austen (1775–1817), English novelist [S1]. Draft: primary_system CHRIST (0.7); A BELOW_THRESHOLD; B UNKNOWN; mid_basin UNKNOWN. Not plotted.

## Life and work

Steventon, Bath, Southampton, Chawton [S1].

## Contribution and impact

Six novels, 1811–1817 [S1].

## Childhood and education

Rector's daughter [S1].

## Adult working worldview

'I am by no means convinced that we ought not all to be evangelicals' (1814) [S2, letter LXXX].

## Heritage (context only)

Church of England [S1].

## Timing

1811–1816, from age 36 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Off the axes [S2].

## Open questions

- Le Faye check; prayers.

## Research log

- 2026-10-18: Read Britannica (live) and the Brabourne letters to Fanny Knight (Pemberley transcription). Prayers known from search extracts only.
