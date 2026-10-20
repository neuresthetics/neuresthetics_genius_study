---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z10)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z10 audit fix (FAIL; v8's call on the auditor's advice, P30 #1): dated by the public readings of 8 February and 8 March 1865 (Sitzungs-Berichte of the same volume), not the 1866 printing. Span 1866 -> 1865, age 44 -> 43. Not plotted."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z10, order P32: F 3, rank 174). Basics from Britannica (Robert Olby, signed; body, not the Top Questions box); the paper from its printing (Verhandlungen des naturforschenden Vereines in Brünn IV, für das Jahr 1865, Brünn 1866, pp. 3–47; Deutsches Textarchiv). Worldview: Augustinian friar, priest (ordained 1846) and abbot (1868); Richter (2015, journal article) says he 'was deeply rooted in his Christian faith' and cites surviving sermon outlines from his later years. The sermon text itself was seen only as a secondary quotation (Graney, Vatican Observatory, from Der Imkerfreund 1972), V3, so it is a lead, not a scoring statement. primary_system CHRIST (0.5, scholarly_reconstruction; alt BELOW_THRESHOLD); A UNKNOWN (lead 1); scientist (laws of heredity: testable claims about organisms), so B 3 at 0.5 from working science, alt 4 (P24, P35); C, D, E UNKNOWN; mid_basin UNKNOWN (A UNKNOWN). Span 1866, age 44. Not plotted (no A). Draft, not reviewed."}

identity:
  id: mendel-gregor
  display_name: "Gregor Mendel"
  roster:
    canonical_name: "Gregor Mendel"
    rank: 174
    F: 3
    models: [Claude, Gemini, Grok]
    band: "core (3–4)"
    status: "core"
    field: "biology"
    field_bucket: "biology / life science"
  full_name: {value: "Gregor Johann Mendel", certainty: 0.7, cites: [{source: S1, locator: "heading"}], how_known: "Britannica: born Johann Mendel; 'Gregor' given on entering the Augustinian order."}
  native_name: {value: "Gregor Johann Mendel", certainty: 0.7, cites: [{source: S1, locator: "heading"}], how_known: "Britannica."}
  aliases:
    - {name: "Mendel-Gregor", kind: "roster alias"}
    - {name: "Johann Mendel", kind: "birth name"}
    - {name: "Gregor", kind: "religious name"}

basics:
  birth:
    date: {value: "1822-07-20", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Heinzendorf, Silesia", modern_name: "Hynčice, Czech Republic", polity_then: "Austrian Empire", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "1884-01-06", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Brünn", modern_name: "Brno, Czech Republic", polity_then: "Austria-Hungary", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1865, certainty: 0.7, cites: [{source: S2, locator: "Inhalts-Verzeichniss (Sitzungs-Berichte, 8 February and 8 March 1865); p. 3"}], how_known: "Versuche über Pflanzen-Hybriden was read in public at the society's sessions of 8 February and 8 March 1865 (listed in the volume's Sitzungs-Berichte; 'Vorgelegt in den Sitzungen vom 8. Februar und 8. März 1865', p. 3); a public reading is the P30 #1 dating event, earlier than the 1866 printing (Z10 audit)."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S2, locator: "p. 3"}], how_known: "1865 (P2)."}
  region_of_birth: {value: "Eastern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Czech Republic (P3)."}
  region_of_work: {value: "Eastern Europe", certainty: 0.7, cites: [{source: S1, locator: "Education and early career"}], how_known: "Brünn (Brno), Moravia."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["German"], certainty: 0.7, cites: [{source: S2, locator: "p. 3"}], how_known: "German text."}
  occupations: {value: ["botanist", "teacher", "Augustinian friar and priest", "abbot"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

contribution:
  fields: {value: ["genetics", "botany"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Laws of heredity from pea hybrids (Mendelism)", year: 1865, kind: "law or principle", lasting: "'the first person to lay the mathematical foundation of the science of genetics, in what came to be called Mendelism' (S1, body)", certainty: 0.7, cites: [{source: S1, locator: "opening; Experimental period"}], how_known: "Britannica body; dated by the 1865 public readings (S2, p. 3; P30 #1)."}
  evidence_of_impact:
    - {value: "Mendelism; the law of independent assortment named by his successors", kind: "named after them", certainty: 0.7, cites: [{source: S1, locator: "opening; Experimental period"}], how_known: "Britannica."}
  major_works:
    - {value: "Versuche über Pflanzen-Hybriden", year: 1866, kind: "paper or paper series", certainty: 0.7, cites: [{source: S2, locator: "pp. 3–47"}], how_known: "The printing."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Founder of the mathematical science of genetics (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Small farming family of limited means; he was his father's only son", role: "family", certainty: 0.7, cites: [{source: S1, locator: "Education and early career"}], how_known: "Britannica."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling: []
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1865", certainty: 0.7, cites: [{source: S2, locator: "p. 3"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: 
    value: CHRIST
    basis: scholarly_reconstruction
    certainty: 0.5
    cites: [{source: S3, locator: "text"}]
    how_known: "Richter (2015), a journal article by a member of his order and family: 'Mendel was deeply rooted in his Christian faith ... Testimony of this attitude is shown in various outlines of sermons that are still preserved'; he cites a sermon from 'his latter years' (after the span). Scholar's account, so at most 0.5; the sermon itself was read only as a secondary quotation (S4, V3)."
    rationale: "Augustinian priest and abbot whose surviving sermon outlines speak of grace, the sacraments and the risen Christ (S3, S4). Alternative BELOW_THRESHOLD: Iltis, his first biographer, held that he entered the monastery for economic reasons without religious interest (as reported in the Wikiquote discussion, not read in Iltis); Britannica gives the economic motive for entry (S1)."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Coded at 0.5 on Richter's account."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Lead 1: the Easter sermon outline ('So muss Natur und Übernatur sich vereinigen ... und Gott gibt das Gedeihen'; S4) speaks of a personal God acting with nature. Seen only as a secondary quotation (V3), undated, probably after the span, so not scored."}
    B_cause: 
      value: 3
      basis: inference_from_work
      certainty: 0.5
      cites: [{source: S2, locator: "pp. 3–4; Schluss-Bemerkungen"}]
      how_known: "Scientist (P30): his laws of heredity are testable claims about organisms. B inferred from his working science with no statement of his own on law and exception, so 3 at 0.5 with 4 as the named alternative, never 4 (P24, P35)."
      rationale: "Seeks an 'allgemein giltiges Gesetz' for hybrids (S2, p. 3): lawful nature in his science. Alternative 4."
      alternatives:
        - {value: 4, note: "Working science cannot tell lawful-with-exceptions from exceptionless (P35).", cites: [{source: S2, locator: "p. 3"}]}
    C_ledger: {value: UNKNOWN, how_known: "Not read at first hand (the sermon's grace and Eucharist are a lead, V3)."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, so the P4 test cannot be applied (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "Sermon lead (S4, secondary quotation, undated): 'Es ist wahr, den Samen, das Talent, die Gnade gibt der liebe Gott, und der Mensch hat bloß die Arbeit'. Find Orel's or Zumkeller's edition of the sermon outlines (1970 Brno symposium) to check the wording and date; read Iltis on the motive for entry; Mendel's 1866–1873 letters to Nägeli for statements on nature."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: "Catholic (German-speaking Silesian peasant family)", certainty: 0.5, cites: [{source: S3, locator: "text"}], how_known: "Richter: 'deeply religious peasant family'."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1865", certainty: 0.7, cites: [{source: S2, locator: "p. 3"}], how_known: "Versuche über Pflanzen-Hybriden, read 1865 (printed 1866), the one listed lasting work (P29, P30 #1)."}
  age_at_first_lasting_contribution: {value: 43, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "p. 3"}], how_known: "1865 − 1822 = 43 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "Combinatorial, mathematical treatment of hybrid ratios (S1).", certainty: 0.5, cites: [{source: S1, locator: "Experimental period"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "Augustinian monastery of St Thomas, Altbrünn", role: "friar, priest; abbot from 1868", years: "1843–1884", kind: "religious body", certainty: 0.7, cites: [{source: S1, locator: "Education and early career"}], how_known: "Britannica; elected abbot 14 years after 1854."}
  - {value: "Brünn Realschule", role: "teacher", years: "1854–1868", kind: "employer", certainty: 0.7, cites: [{source: S1, locator: "Education and early career"}], how_known: "Britannica."}
collaborators:
  - {value: "Cyril Napp", relation: "mentor or employer", note: "abbot; permitted the experiments", certainty: 0.7, cites: [{source: S1, locator: "Experimental period"}], how_known: "Britannica."}
  - {value: "Franz Unger", relation: "teacher", note: "Vienna", certainty: 0.7, cites: [{source: S1, locator: "Education and early career"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S5, locator: "roster.csv, rank 174"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Sermon text seen only as a secondary quotation."
  open_questions:
    - "Orel/Zumkeller edition of the sermons; Iltis on motive."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Robert Olby"
    citation: "Olby, Robert. 'Gregor Mendel.' Encyclopaedia Britannica (rev. 29 August 2026). https://www.britannica.com/biography/Gregor-Mendel"
    url: "https://www.britannica.com/biography/Gregor-Mendel"
    accessed: 2026-10-19
    reliability_note: "Signed article; body cited, question boxes not used (P26)."
    used_for: [identity, basics, contribution, childhood, institutions, collaborators, lane_b]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Gregor Mendel"
    citation: "Mendel, Gregor. 'Versuche über Pflanzen-Hybriden.' Verhandlungen des naturforschenden Vereines in Brünn IV (für das Jahr 1865), Abhandlungen, pp. 3–47. Brünn, 1866. Deutsches Textarchiv. https://www.deutschestextarchiv.de/book/show/mendel_pflanzenhybriden_1866"
    url: "https://www.deutschestextarchiv.de/book/show/mendel_pflanzenhybriden_1866"
    accessed: 2026-10-19
    reliability_note: "Transcription of the 1866 printing (title page and opening read)."
    used_for: [basics, contribution, worldview, timing]
  - id: S3
    type: secondary
    kind: "journal article"
    author: "Clemens Richter"
    citation: "Richter, Clemens, OSA. 'Remembering Johann Gregor Mendel: a human, a Catholic priest, an Augustinian monk, and abbot.' Molecular Genetics & Genomic Medicine 3(6) (2015): 483–485. https://pmc.ncbi.nlm.nih.gov/articles/PMC4694133/"
    url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC4694133/"
    accessed: 2026-10-19
    reliability_note: "Commemorative address by a member of his order and family; published article, read in full."
    used_for: [worldview, heritage]
  - id: S4
    type: secondary
    kind: "other"
    author: "J. H. Graney"
    citation: "Graney, J. H. (trans.). 'A brief portion of an Easter sermon by Gregor Mendel.' Vatican Observatory (2017), from Der Imkerfreund 27–28 (1972), p. 254. https://www.vaticanobservatory.org/wp-content/uploads/2017/10/Mendel-Easter-Sermon-JHG.pdf"
    url: "https://www.vaticanobservatory.org/wp-content/uploads/2017/10/Mendel-Easter-Sermon-JHG.pdf"
    accessed: 2026-10-19
    reliability_note: "Secondary quotation of the sermon outline (V3); lead only."
    used_for: [worldview]
  - id: S5
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [review]
---

## Summary

Gregor Mendel (1822–1884), botanist and Augustinian abbot [S1]. Draft: CHRIST (0.5); A UNKNOWN; B 3 (0.5). Not plotted.

## Life and work

Brünn monastery and Realschule [S1].

## Contribution and impact

Laws of heredity, read 1865, printed 1866 [S1, S2].

## Childhood and education

Farming family; Olmütz; Vienna [S1].

## Adult working worldview

'Deeply rooted in his Christian faith' [S3]; sermon outline (lead) [S4].

## Heritage (context only)

Catholic [S3].

## Timing

1865, age 43 [S2].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Sermon edition; Iltis.

## Research log

- 2026-10-19: Read Britannica (Olby); the 1866 printing (DTA); Richter 2015; Graney's sermon excerpt.
