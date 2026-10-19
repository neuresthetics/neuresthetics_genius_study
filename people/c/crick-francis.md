---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch P)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-18
  last_updated: 2026-10-18
  change_log:
    - {date: 2026-10-18, by: "Grok Bot", summary: "Record created (stage 3 batch P, order P32: F 4, rank 95). Basics from Britannica (Britannica Editors, unsigned; body only) and the two Nature papers' publisher pages (dates). Worldview from his own letters as quoted in Mark Goldie, Storm over a Chapel (Churchill College, 2024) and Chris Beckett, Medical History 48 (2004): to Churchill, 12 October 1961 ('atheists and agnostics such as myself'), to Cockcroft, n.d. [1961] (a university furthering 'superstitions' is 'shameful'), and of 14 December 1965 ('I am an atheist'); secondary quotations, primary check pending. Scientist (P30). primary_system ATHE (0.5); A 4 (0.5, alt BELOW_THRESHOLD, P38); B 3 (0.5, alt 4; P35); D 4 (0.5); mid_basin BELOW_THRESHOLD. Plotted (faded). Draft, not reviewed."}

identity:
  id: crick-francis
  display_name: "Francis Crick"
  roster:
    canonical_name: "Francis Crick"
    rank: 95
    F: 4
    models: [Claude, DeepSeek, Gemini, Grok]
    band: "core (3–4)"
    status: core
    field: biology
    field_bucket: "biology / life science"
  full_name: {value: "Francis Harry Compton Crick", certainty: 0.7, cites: [{source: S1, locator: "header ('Also known as')"}], how_known: "Britannica header line, not Quick Facts or Top Questions."}
  native_name: {value: UNKNOWN, how_known: "English."}
  aliases:
    - {name: "Crick-Francis", kind: "roster alias"}

basics:
  birth:
    date: {value: "1916-06-08", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Northampton, Northamptonshire, England", modern_name: "Northampton, United Kingdom", polity_then: "United Kingdom", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "2004-07-28", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "San Diego, California, U.S.", modern_name: "San Diego, California, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1953, certainty: 0.7, cites: [{source: S2, locator: "citation metadata"}, {source: S1, locator: "Watson paragraph"}], how_known: "The double-helix model (S1, undated there), published as Watson and Crick, Nature 171 (April 1953), p. 737 (S2)."}
  era_bucket: {value: "1950 on", certainty: 0.7, cites: [{source: S2, locator: "citation metadata"}], how_known: "From 1953 (P2); 1961 gives the same bucket."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "United Kingdom (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "Strangeways and Cavendish paragraph"}], how_known: "Cambridge during the working years (1953–1961); the Salk Institute from 1977 (S1)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [English], certainty: 0.7, cites: [{source: S1, locator: "titles"}], how_known: "Britannica."}
  occupations: {value: ["biophysicist", "molecular biologist", "neuroscientist"], certainty: 0.5, cites: [{source: S1, locator: "opening; Salk sentence"}], how_known: "Britannica calls him a biophysicist; the other two are the coder's labels for the DNA and consciousness work it describes."}

contribution:
  fields: {value: ["molecular biology", "genetics", "neuroscience"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Double-helix model of DNA (with James Watson)", year: 1953, kind: discovery, lasting: "'a cornerstone of genetics and ... widely regarded as one of the most important discoveries of 20th-century biology' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; Watson paragraph"}, {source: S2, locator: "citation metadata"}], how_known: "Britannica; year from the Nature paper (S2). A result about natural systems, so he is a scientist (P30)."}
    - {value: "Triplet codons: each group of three bases designates an amino acid", year: 1961, kind: discovery, lasting: "'helped clarify the way in which the cell eventually uses the DNA \"message\" to build proteins' (S1)", certainty: 0.7, cites: [{source: S1, locator: "codon paragraph"}, {source: S3, locator: "citation metadata"}], how_known: "Britannica ('By 1961'); dated by Crick, Barnett, Brenner and Watts-Tobin, Nature 192 (December 1961), p. 1227 (S3)."}
  evidence_of_impact:
    - {value: "Nobel Prize for Physiology or Medicine (1962, with Watson and Wilkins); Order of Merit (1991)", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "opening; last paragraph"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
  parents_and_household: []
  household_circumstances: {value: TODO}
  schooling: []
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [English], certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1953–1961", certainty: 0.7, cites: [{source: S2, locator: "citation metadata"}, {source: S3, locator: "citation metadata"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "A college 'with a special emphasis on science' should not 'tacitly endorse' Christian beliefs with a chapel (1961)", certainty: 0.5, cites: [{source: S4, locator: "pp. 4–5"}], how_known: "His letter to Churchill, 12 October 1961, as quoted by Goldie (S4); primary check pending (Churchill Papers 2/571)."}
  primary_system:
    value: ATHE
    basis: consistent_private_letters
    certainty: 0.5
    cites: [{source: S4, locator: "pp. 4–5; p. 12"}, {source: S5, locator: "text at note 18"}]
    rationale: "Self-description: 'atheists and agnostics such as myself' (12 October 1961) and 'I am an atheist' (14 December 1965); in 1961 he reports that many scientists 'believe that nowadays Christianity is a firm superstition' and adds that 'It seems to me shameful that a great university should be used for the furtherance of superstitions' (letter to Cockcroft). Named alternatives: AGNOS (the 1961 phrase pairs the two labels) and SECHUM."
    how_known: "Private letters quoted in secondary works (S4, S5); primary check pending. The 1961 letters fall inside the working years; the 1965 letter is four years after. 0.5 for the mixed 1961 label (P38) and the secondary quotation (P26)."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: ATHE, reason: "'I am an atheist' (1965)."}
    - {code: AGNOS, reason: "'atheists and agnostics such as myself' (1961)."}
    - {code: SECHUM, reason: "Lead only: his Humanist Society essay prize (S4); no statement read."}
  lio_axes:
    A_locus:
      value: 4
      basis: consistent_private_letters
      certainty: 0.5
      cites: [{source: S4, locator: "pp. 4–5"}, {source: S5, locator: "text at note 18"}]
      rationale: "No God (P38): 'I am an atheist' (1965), and in 1961 he calls Christianity among 'superstitions' a university should not further. P38: stated disbelief together with an agnostic label ('atheists and agnostics such as myself', 1961) is A 4 at most 0.5, with BELOW_THRESHOLD as the named alternative."
      how_known: "Private letters, secondary quotations, primary check pending (P26)."
      alternatives:
        - {value: BELOW_THRESHOLD, note: "P38: the 1961 letter pairs atheist and agnostic.", cites: [{source: S4, locator: "p. 5"}]}
    B_cause:
      value: 3
      basis: inference_from_work
      certainty: 0.5
      cites: [{source: S1, locator: "Watson and codon paragraphs"}]
      rationale: "A scientist (P30: the double helix and the triplet code are results about natural systems) with no statement of his own on law and exception read, so working science gives B 3 at 0.5, alternative 4 (P35). Goldie's summary that Of Molecules and Men (1966) declared the end of 'vitalism' (S4, p. 3) is a lead, not his wording."
      how_known: "P35."
      alternatives:
        - {value: 4, note: "P35 alternative: no stated exceptionless law.", cites: [{source: S1, locator: "Watson and codon paragraphs"}]}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read."}
    D_authority:
      value: 4
      basis: consistent_private_letters
      certainty: 0.5
      cites: [{source: S4, locator: "p. 12"}]
      rationale: "Religion keeps no say of its own: after reporting that many scientists think 'Christianity is a firm superstition', he adds 'It seems to me shameful that a great university should be used for the furtherance of superstitions' (letter to Cockcroft, 1961). Coder's reading; no alternative domain of religious authority is allowed."
      how_known: "Private letter, secondary quotation (Goldie quoting Olby), primary check pending."
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A 4 but at 0.5: the A ≥ 3 branch reads A only (P10) and needs 0.7, as for Skinner and Shannon."}
  statements:
    - text: "Moreover it would be open (conscience permitting) not merely to members of the Church of England, but also to Catholics, Non-Conformists, Jews, Muslims, Hindus, Zen Buddhists and even to atheists and agnostics such as myself."
      cites: [{source: S4, locator: "pp. 4–5"}]
      date: "1961-10-12"
      context: "Letter to Winston Churchill resigning his Churchill College fellowship over the proposed chapel; Churchill Papers 2/571, as quoted by Goldie (S4)."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-18
      note: "Primary check pending; Goldie notes a photograph of the letter in Pagnamenta (2008), p. 263."
    - text: "I am sure there are many people in Cambridge, especially scientists, who believe that nowadays Christianity is a firm superstition, and who feel that this will become increasingly obvious to most educated people in the future. [...] I cannot agree with this point of view. It seems to me shameful that a great university should be used for the furtherance of superstitions and although Christianity is no longer virulent, it is surely not yet harmless."
      cites: [{source: S4, locator: "p. 12"}]
      context: "Letter to John Cockcroft, Master of Churchill College, undated (1961), explaining his resignation; Crick Papers, quoted by Goldie from Olby (2009), pp. 318–19 (S4)."
      axes: [A_locus, D_authority]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-18
      note: "Undated in S4; the resignation is 1961. Primary check pending."
    - text: "You may not know that I am an atheist and a few years ago resigned my Fellowship at Churchill College because they threatened to build a College Chapel."
      cites: [{source: S5, locator: "text at note 18 (PP/CRI/E/1/14/5)"}]
      date: "1965-12-14"
      context: "Letter on the venue for his John Danz Lectures (Seattle, 1966; published as Of Molecules and Men), Wellcome Library, Crick Papers PP/CRI/E/1/14/5, as quoted by Beckett (S5); Goldie (S4, p. 5) quotes the same words."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-18
      note: "Primary check pending (Wellcome digitized Crick papers)."
  changes_over_life: []
  coder_notes: "Coder's call. The letters agree from 1961 to 1965; 'The God hypothesis is bankrupt' (2004, quoted by Goldie from Olby) is consistent but late. Leads not read: Of Molecules and Men (1966) on vitalism (B) and The Astonishing Hypothesis (1994); both are lending-only on the Internet Archive."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "English", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1953–1961", certainty: 0.7, cites: [{source: S2, locator: "citation metadata"}, {source: S3, locator: "citation metadata"}], how_known: "First to last listed lasting contribution (P29, P30)."}
  age_at_first_lasting_contribution: {value: 37, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "citation metadata"}], how_known: "1953 − 1916 = 37 (P30)."}
  first_evidence_of_lio_type_views: {value: "1961: 'atheists and agnostics such as myself'; the furtherance of 'superstitions' by a university 'shameful'", year: 1961, certainty: 0.5, cites: [{source: S4, locator: "pp. 4–5; p. 12"}], how_known: "Earlier writings not read (P30 #7); secondary quotations."}
  lio_views_relative_to_major_work: {value: "during major work", rationale: "1961 falls inside 1953–1961.", certainty: 0.5, cites: [{source: S4, locator: "pp. 4–5"}], how_known: "Dates of what was read."}
  worldview_during_major_work: {value: "Atheist or agnostic, hostile to college religion (1961)", certainty: 0.5, cites: [{source: S4, locator: "pp. 4–5; p. 12"}], how_known: "His letters as quoted."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "Structural model-building of molecules (S1).", certainty: 0.5, cites: [{source: S1, locator: "Watson paragraph"}], how_known: "Coder's reading."}
  form_acquired: {value: "through the profession", certainty: 0.5, cites: [{source: S1, locator: "Strangeways and Cavendish paragraph"}], how_known: "Coder's reading."}
  circle_present: {value: "no", rationale: "No God.", certainty: 0.5, cites: [{source: S5, locator: "text at note 18"}], how_known: "Coder's reading."}
  reading: "Atheist molecular biologist."
  notes: ""

institutions:
  - {value: "Strangeways Research Laboratory, University of Cambridge", role: "biologist", years: "1947–1949", kind: "research institute", certainty: 0.7, cites: [{source: S1, locator: "Strangeways and Cavendish paragraph"}], how_known: "Britannica."}
  - {value: "Medical Research Council Unit, Cavendish Laboratory, Cambridge", role: "researcher", years: "1949–", kind: "research institute", certainty: 0.5, cites: [{source: S1, locator: "Strangeways and Cavendish paragraph"}], how_known: "Britannica gives the start; end year not read."}
  - {value: "Churchill College, Cambridge", role: "fellow (resigned 1961)", years: "–1961", kind: university, certainty: 0.5, cites: [{source: S4, locator: "pp. 3–5"}], how_known: "Goldie."}
  - {value: "Salk Institute for Biological Studies", role: "distinguished professor", years: "1977–2004", kind: "research institute", certainty: 0.7, cites: [{source: S1, locator: "Salk sentence"}], how_known: "Britannica."}
collaborators:
  - {value: "James Watson", relation: collaborator, note: "double helix", certainty: 0.7, cites: [{source: S1, locator: "Watson paragraph"}], how_known: "Britannica."}
  - {value: "Maurice Wilkins", relation: collaborator, note: "X-ray diffraction of DNA; Nobel 1962", certainty: 0.7, cites: [{source: S1, locator: "opening; Watson paragraph"}], how_known: "Britannica."}
  - {value: "Rosalind Franklin", relation: other, note: "her X-ray diffraction pictures were used for the model", certainty: 0.7, cites: [{source: S1, locator: "Watson paragraph"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S6, locator: "roster.csv, rank 95"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Britannica article is unsigned (Britannica Editors); read live (Wayback rate-limited)."
    - "All worldview quotations are secondary quotations of private letters; primary check pending."
  open_questions:
    - "Check the 1961 and 1965 letters in the Churchill Papers (CHUR 2/571) and the Wellcome Crick Papers (PP/CRI/E/1/14/5)."
    - "Read Of Molecules and Men (1966) for a statement of his own on law in nature (B)."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "Britannica Editors. \"Francis Crick.\" Encyclopaedia Britannica (revised 31 August 2026). https://www.britannica.com/biography/Francis-Crick. Read live 2026-10-18 (the Wayback Machine was rate-limiting)."
    url: "https://www.britannica.com/biography/Francis-Crick"
    accessed: 2026-10-18
    reliability_note: "Unsigned article. Body and header only; the AI-generated Top Questions are not cited."
    used_for: [identity, basics, contribution, timing, lane_b, institutions, collaborators]
  - id: S2
    type: primary
    kind: "journal article"
    author: "J. D. Watson and F. H. C. Crick"
    citation: "Watson, J. D., and F. H. C. Crick. \"Molecular Structure of Nucleic Acids: A Structure for Deoxyribose Nucleic Acid.\" Nature 171 (April 1953): 737. https://www.nature.com/articles/171737a0"
    url: "https://www.nature.com/articles/171737a0"
    accessed: 2026-10-18
    reliability_note: "Publisher's page; used for the date only (citation metadata)."
    used_for: [basics, contribution, timing]
  - id: S3
    type: primary
    kind: "journal article"
    author: "F. H. C. Crick, Leslie Barnett, S. Brenner and R. J. Watts-Tobin"
    citation: "Crick, F. H. C., L. Barnett, S. Brenner and R. J. Watts-Tobin. \"General Nature of the Genetic Code for Proteins.\" Nature 192 (December 1961): 1227. https://www.nature.com/articles/1921227a0"
    url: "https://www.nature.com/articles/1921227a0"
    accessed: 2026-10-18
    reliability_note: "Publisher's page; used for the date only (citation metadata)."
    used_for: [contribution, timing]
  - id: S4
    type: secondary
    kind: "scholarly book"
    author: "Mark Goldie"
    citation: "Goldie, Mark. Storm over a Chapel: A History of the Chapel at Churchill College Cambridge. Cambridge: Churchill College, 2024. PDF: https://chapel.chu.cam.ac.uk/wp-content/uploads/2025/01/STORM-OVER-A-CHAPEL-2024-locked.pdf"
    url: "https://chapel.chu.cam.ac.uk/wp-content/uploads/2025/01/STORM-OVER-A-CHAPEL-2024-locked.pdf"
    accessed: 2026-10-18
    reliability_note: "Signed college history by a Cambridge historian, read directly; quotes the letters with archive references (Churchill Papers 2/571; Crick Papers via Olby 2009)."
    used_for: [worldview, timing, institutions]
  - id: S5
    type: secondary
    kind: "journal article"
    author: "Chris Beckett"
    citation: "Beckett, Chris. \"For the Record: The Francis Crick Archive at the Wellcome Library.\" Medical History 48, no. 2 (2004): 245–260. doi:10.1017/s0025727300007419. https://pmc.ncbi.nlm.nih.gov/articles/PMC546341/"
    url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC546341/"
    accessed: 2026-10-18
    reliability_note: "Article by the archive's project archivist, read directly on PMC; quotes the letter with its catalogue number."
    used_for: [worldview, lane_b]
  - id: S6
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-18
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Francis Crick

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Francis Crick (1916–2004), British biophysicist [S1]. Draft: primary_system ATHE (0.5); A 4 at 0.5 (alt BELOW_THRESHOLD); B 3 at 0.5 (alt 4; P35); D 4 at 0.5; mid_basin BELOW_THRESHOLD. Plotted (faded).

## Life and work

Cambridge from 1947; Salk Institute from 1977 [S1].

## Contribution and impact

The double helix (1953) and the triplet code (1961) [S1; S2; S3].

## Childhood and education

Not read.

## Adult working worldview

'atheists and agnostics such as myself' (1961) [S4, pp. 4–5]; 'I am an atheist' (1965) [S5].

## Heritage (context only)

English [S1].

## Timing

First lasting contribution 1953, at 37 [S1; S2].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No God [S5].

## Open questions

- Primary checks of the letters.

## Research log

- 2026-10-18: Read Britannica (live), the Nature citation pages, Goldie (Churchill College PDF) and Beckett (PMC) directly. Of Molecules and Men and The Astonishing Hypothesis are lending-only on the Internet Archive.
