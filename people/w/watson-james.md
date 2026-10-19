---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch R)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-18
  last_updated: 2026-10-18
  change_log:
    - {date: 2026-10-18, by: "Grok Bot", summary: "Record created (stage 3 batch R, order P32: F 4, rank 105). Basics from Britannica (Britannica Editors, unsigned; body only, read live) and the 1953 Nature paper's publisher page (date). Worldview from his own signed op-ed in Time, 25 March 2016 ('a lifelong atheist'; 'my God-rejecting views'; 'secular Christianity'), read directly; written profession, after the working years (1953–1965), so capped at 0.5 (P20, Shannon and Hawking precedent). Scientist (P30). primary_system ATHE (0.5); A 4 (0.5); B 3 (0.5, alt 4; P35); mid_basin BELOW_THRESHOLD. Plotted (faded), like Crick. Draft, not reviewed."}
    - {date: 2026-10-18, by: "Grok Bot", summary: "Batch R audit fixes (gs_0454445_R run 1). Op-ed locators corrected: the 'I never go to Sunday services' statement is paragraph 7, and primary_system and A cite paragraphs 2, 4 and 7 (WA4). Ruling R1 recorded (v8's call on the auditor's advice): 'lifelong' does not lift the P1 cap, so ATHE and A 4 stay at 0.5. Span 1953–1965 with 1968 as the alternative recorded as v8's call. The 2003 Scientific American interview noted as an unread lead (still post-span if confirmed). No value changed."}

identity:
  id: watson-james
  display_name: "James Watson"
  roster:
    canonical_name: "James Watson"
    rank: 105
    F: 4
    models: [Claude, DeepSeek, Gemini, Grok]
    band: "core (3–4)"
    status: core
    field: biology
    field_bucket: "biology / life science"
  full_name: {value: "James Dewey Watson", certainty: 0.7, cites: [{source: S1, locator: "header ('Also known as')"}], how_known: "Britannica header line, not Quick Facts."}
  native_name: {value: UNKNOWN, how_known: "English; same as the display name."}
  aliases:
    - {name: "Watson-James", kind: "roster alias"}

basics:
  birth:
    date: {value: "1928-04-06", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica body."}
    place: {value: "Chicago, Illinois, U.S.", modern_name: "Chicago, Illinois, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "2025-11-06", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica body."}
    place: {value: "East Northport, New York, U.S.", modern_name: "East Northport, New York, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1953, certainty: 0.7, cites: [{source: S1, locator: "'Research' (spring 1953; Nature, April–May 1953)"}, {source: S2, locator: "citation metadata"}], how_known: "The double-helix model, published in Nature in April 1953 (S2) (P13, P17)."}
  era_bucket: {value: "1950 on", certainty: 0.7, cites: [{source: S2, locator: "citation metadata"}], how_known: "1953 (P2)."}
  region_of_birth: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "United States (P3)."}
  region_of_work: {value: "North America", certainty: 0.5, cites: [{source: S1, locator: "'Research'"}], how_known: "Harvard and Cold Spring Harbor; the double helix itself was found at Cambridge (Northern Europe); coder's call on the main region."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.5, cites: [{source: S1, locator: "'Research'"}], how_known: "Coder's reading."}
  occupations: {value: ["geneticist", "biophysicist", "professor of biology", "laboratory director"], certainty: 0.7, cites: [{source: S1, locator: "opening; 'Research'"}], how_known: "Britannica."}

contribution:
  fields: {value: ["genetics", "molecular biology"], certainty: 0.7, cites: [{source: S1, locator: "opening; 'Research'"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Double-helix model of DNA, with specific base pairing (with Francis Crick)", year: 1953, kind: discovery, lasting: "'Their research answered one of the fundamental questions in genetics'; Nobel Prize 1962 (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Research'"}, {source: S2, locator: "citation metadata"}], how_known: "Britannica; year from the Nature paper (S2). A result about natural systems, so he is a scientist (P30)."}
    - {value: "Molecular Biology of the Gene (textbook)", year: 1965, kind: work, lasting: "'one of the most extensively used modern biology texts' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Research'"}], how_known: "Britannica. The latest listed lasting work (P30 addendum b); The Double Helix (1968), which Britannica describes only as an account that 'aroused some controversy', is not listed (coder's call; alternative end 1968)."}
  evidence_of_impact:
    - {value: "Nobel Prize for Physiology or Medicine, 1962, with Crick and Wilkins", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Mixed: Irish Catholic mother ('modestly religious'), Episcopalian father who lost his belief", certainty: 0.5, cites: [{source: S3, locator: "paragraph 1"}], how_known: "His own account, 2016 (S3); neither parent went to church."}
  family_religious_practice: {value: "Neither parent attended church; he went to Sunday mass with his 'very religious grandmother' for a few years", certainty: 0.5, cites: [{source: S3, locator: "paragraphs 1–2"}], how_known: "His own account (S3)."}
  parents_and_household: []
  household_circumstances: {value: "South Side of Chicago in the 1930s", certainty: 0.5, cites: [{source: S3, locator: "paragraph 1"}], how_known: "His own account (S3)."}
  schooling:
    - {value: "University of Chicago, entered at 15, graduated 1947", stage: university, run_by: private, years: "1943–1947", ages: "15–19", certainty: 0.7, cites: [{source: S1, locator: "'Research'"}], how_known: "Britannica; start year from his age at entry; run_by the coder's."}
    - {value: "Indiana University, PhD 1950 (virus research)", stage: university, run_by: "state or municipal", years: "–1950", certainty: 0.7, cites: [{source: S1, locator: "'Research'"}], how_known: "Britannica; run_by the coder's."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["English"], certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  notable_events:
    - {value: "First Communion; stopped going to services by age 11", year: 1939, certainty: 0.5, cites: [{source: S3, locator: "paragraph 2"}], how_known: "His own retrospective account (S3); year from 'by age 11'."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1953–1965", certainty: 0.7, cites: [{source: S1, locator: "'Research'"}, {source: S2, locator: "citation metadata"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "Darwinian evolution and DNA-based genetics a 'very compelling alternative framework' to religion; 'most scientists see no need to postulate the existence of God-like entities' (2016)", certainty: 0.5, cites: [{source: S3, locator: "paragraph 3"}], how_known: "His op-ed (S3), after the working years (P20)."}
  primary_system:
    value: ATHE
    basis: written_profession
    certainty: 0.5
    cites: [{source: S3, locator: "paragraphs 2, 4 and 7"}]
    rationale: "Self-description: 'a reply that I am a lifelong atheist'; 'my God-rejecting views'; by 11 he was 'rejecting the need for an all-knowing God-like creator of our physical world'. Named alternative: SECHUM ('I don't need sermons to maintain my secular Christianity'; faith 'in the unchanging, universal aspects of human nature')."
    how_known: "His own signed op-ed, Time, 25 March 2016, read directly. After the working years (1953–1965), so 0.5 (P20, Shannon and Hawking precedent). 'Lifelong' does not lift the cap: ruling R1 (v8's call on the auditor's advice, 2026-10-18; OPEN_DECISIONS P20) keeps post-span evidence at 0.5 under P1, since no change of view is documented (P31) and the present-tense label describes the time of writing (P30)."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: ATHE, reason: "'I am a lifelong atheist' (2016)."}
    - {code: SECHUM, reason: "'my secular Christianity'; faith in human nature and in 'scientific and humanistic knowledge' (2016)."}
    - {code: CHRIST, reason: "Rejected: 'secular Christianity' is offered with 'my God-rejecting views'; he never goes to services."}
  lio_axes:
    A_locus:
      value: 4
      basis: written_profession
      certainty: 0.5
      cites: [{source: S3, locator: "paragraphs 2, 4 and 7"}]
      rationale: "No God (P38): 'a lifelong atheist'; 'my God-rejecting views'; faith 'not ... in an all-powerful, life-instructions-providing God'. No agnostic label, so P38's cap does not apply; the cap is P20's."
      how_known: "Signed op-ed, his own words; 2016, after the working years, so 0.5 (P20)."
    B_cause:
      value: 3
      basis: inference_from_work
      certainty: 0.5
      cites: [{source: S1, locator: "'Research'"}]
      rationale: "A scientist (P30: the double helix is a result about natural systems) with no statement of his own on law and exception read, so working science gives B 3 at 0.5, alternative 4 (P35). His remark that science 'possibly never will' explain the origin of life (S3) is about knowledge, not exceptions."
      how_known: "P35."
      alternatives:
        - {value: 4, note: "P35 alternative: no stated exceptionless law.", cites: [{source: S1, locator: "'Research'"}]}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read; the remark that 'the fear of going to hell has effectively disappeared' for many Americans (S3) is about others."}
    D_authority: {value: UNKNOWN, how_known: "Lead only: religious edicts 'at the root cause of much human violence', yet sermons 'must embrace the moral challenges of the present' (S3); mixed and after the working years, not scored (coder's call)."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A 4 but at 0.5: the A ≥ 3 branch reads A only (P10) and needs 0.7, as for Crick, Shannon and Skinner."}
  statements:
    - text: "By age 11, just a year after my First Communion, I, too, stopped going to services, rejecting the need for an all-knowing God-like creator of our physical world."
      cites: [{source: S3, locator: "paragraph 2"}]
      date: "2016-03-25"
      context: "Op-ed 'Nobel Scientist: I Place My Faith in Human Gods', Time (Ideas), 25 March 2016; retrospective account of c. 1939."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-18
      note: "Read on time.com, the publisher's own text of the op-ed (marked primary transcription as the nearest value); the page also carries unrelated sponsored newsletter text, ignored."
    - text: "The obvious sincerity of the questioner demanded more than a reply that I am a lifelong atheist."
      cites: [{source: S3, locator: "paragraph 4"}]
      date: "2016-03-25"
      context: "Same op-ed; he goes on: 'faith was essential to my life, but it was not faith in an all-powerful, life-instructions-providing God.'"
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-18
      note: ""
    - text: "I never go to Sunday services; I don’t need sermons to maintain my secular Christianity. Nowadays my God-rejecting views are much more broadly accepted by educated men and women than when World War II ended and my father would have seriously jeopardized his job in business if he ever publicly expressed the atheistic view he passed on to me."
      cites: [{source: S3, locator: "paragraph 7"}]
      date: "2016-03-25"
      context: "Same op-ed."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-18
      note: ""
  changes_over_life: []
  coder_notes: "Coder's call. Only the 2016 op-ed was read; it is after the working years, so the codes sit at 0.5 even though it calls him a 'lifelong atheist'. Leads not read: the 2003 Scientific American interview ('I never thought there was a spiritual basis for life', seen in search results only; an unread lead, not used for any value, and if confirmed it would still be after the working years, so capped at 0.5 under P1; R audit note) and the Web of Stories recordings; The Double Helix (1968) and Avoid Boring People (2007) for earlier statements."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "American; mother Irish Catholic", certainty: 0.5, cites: [{source: S3, locator: "paragraph 1"}], how_known: "His own account."}
  religious_heritage_by_birth: {value: "Roman Catholic (mother) and Episcopalian (father)", certainty: 0.5, cites: [{source: S3, locator: "paragraph 1"}], how_known: "His own account."}
  baptism_or_initiation: {value: "First Communion (c. age 10)", certainty: 0.5, cites: [{source: S3, locator: "paragraph 2"}], how_known: "His own account; age from 'a year' before 11."}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1953–1965", certainty: 0.7, cites: [{source: S1, locator: "'Research'"}, {source: S2, locator: "citation metadata"}], how_known: "Double helix (1953) to Molecular Biology of the Gene (1965), first to last listed lasting contribution (P29, P30); alternative end 1968 (The Double Helix), not listed: Britannica calls it only 'an informal personal account' that 'aroused some controversy', so P30 addendum b does not force it onto the list. Span end 1965 with 1968 as the alternative is v8's call (2026-10-18; OPEN_DECISIONS P20, with R1); either end leaves the 2016 op-ed after the span."}
  age_at_first_lasting_contribution: {value: 25, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "citation metadata"}], how_known: "1953 − 1928 = 25 (P30; birthday 6 April, paper 25 April)."}
  first_evidence_of_lio_type_views: {value: "2016: 'a lifelong atheist'; rejecting a creator 'by age 11'", year: 2016, certainty: 0.5, cites: [{source: S3, locator: "paragraphs 2, 4"}], how_known: "Only the 2016 op-ed read (P30 #7); it dates the rejection to c. 1939 retrospectively."}
  lio_views_relative_to_major_work: {value: "after major work", certainty: 0.5, cites: [{source: S3, locator: "paragraph 4"}], how_known: "Date of what was read (2016), as for Shannon; by his own retrospective account the views come before (c. 1939), so 'before major work' is the named alternative."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Nothing written in 1953–1965 read; his later 'lifelong' claim is noted under primary_system."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "Structural model-building of DNA (S1).", certainty: 0.5, cites: [{source: S1, locator: "'Research'"}], how_known: "Coder's reading."}
  form_acquired: {value: "through the profession", certainty: 0.5, cites: [{source: S1, locator: "'Research' (X-ray diffraction at the Cavendish)"}], how_known: "Coder's reading."}
  circle_present: {value: "no", rationale: "No God.", certainty: 0.5, cites: [{source: S3, locator: "paragraph 4"}], how_known: "Coder's reading."}
  reading: "Atheist molecular biologist who calls himself a secular Christian."
  notes: ""

institutions:
  - {value: "University of Copenhagen", role: researcher, years: UNKNOWN, kind: university, certainty: 0.7, cites: [{source: S1, locator: "'Research'"}], how_known: "Britannica (before 1951; years not given)."}
  - {value: "Cavendish Laboratory, University of Cambridge", role: researcher, years: "1951–1953", kind: "research institute", certainty: 0.7, cites: [{source: S1, locator: "'Research'"}], how_known: "Britannica."}
  - {value: "Harvard University", role: "teacher; professor of biology 1961–76", years: "1955–1976", kind: university, certainty: 0.7, cites: [{source: S1, locator: "'Research'"}], how_known: "Britannica."}
  - {value: "Laboratory of Quantitative Biology, Cold Spring Harbor", role: director, years: "1968–2007", kind: "research institute", certainty: 0.7, cites: [{source: S1, locator: "'Research'; 'Controversy'"}], how_known: "Britannica (assumed leadership 1968; resigned 2007); end year from the resignation in 'Controversy'."}
  - {value: "National Institutes of Health (Human Genome Project)", role: "helped direct the Human Genome Project", years: "1988–1992", kind: "government or state body", certainty: 0.7, cites: [{source: S1, locator: "'Research'"}], how_known: "Britannica."}
collaborators:
  - {value: "Francis Crick", relation: collaborator, note: "double helix; Nobel 1962", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Research'"}], how_known: "Britannica."}
  - {value: "Maurice Wilkins", relation: collaborator, note: "shared the 1962 Nobel Prize", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Britannica names him as co-laureate; 'collaborator' is the coder's reading."}
  - {value: "Oswald Avery", relation: "influenced by", note: "his experiments showing DNA affects heredity", certainty: 0.7, cites: [{source: S1, locator: "'Research'"}], how_known: "Britannica."}
  - {value: "John Tooze", relation: collaborator, note: "co-author of The DNA Story (1981)", certainty: 0.7, cites: [{source: S1, locator: "'Research'"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 105"}], how_known: "Study roster."}
  controversies:
    - {value: "2007 statement on race and intelligence, denounced as racist; resigned from Cold Spring Harbor; honorary titles removed in 2019", certainty: 0.7, cites: [{source: S1, locator: "'Controversy'"}], how_known: "Britannica."}
  data_quality_flags:
    - "Britannica article is unsigned (Britannica Editors); read live."
    - "Worldview rests on one public statement from 2016, after the working years."
  open_questions:
    - "Find a statement from 1953–1965 (letters, interviews, The Double Helix, 1968) on God or on law in nature."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "Britannica Editors. \"James Watson.\" Encyclopaedia Britannica (revised 2 September 2026, by Amy Tikkanen). https://www.britannica.com/biography/James-Dewey-Watson. Read live 2026-10-18."
    url: "https://www.britannica.com/biography/James-Dewey-Watson"
    accessed: 2026-10-18
    reliability_note: "Unsigned article. Body and header only; the AI-generated questions and At a Glance are not cited."
    used_for: [identity, basics, contribution, childhood, timing, lane_b, institutions, collaborators, review]
  - id: S2
    type: primary
    kind: "journal article"
    author: "J. D. Watson and F. H. C. Crick"
    citation: "Watson, J. D., and F. H. C. Crick. \"Molecular Structure of Nucleic Acids: A Structure for Deoxyribose Nucleic Acid.\" Nature 171 (April 1953): 737. https://www.nature.com/articles/171737a0"
    url: "https://www.nature.com/articles/171737a0"
    accessed: 2026-10-18
    reliability_note: "Publisher's page; used for the date only (citation metadata), as in the Crick record."
    used_for: [basics, contribution, timing]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "James Watson"
    citation: "Watson, James. \"Nobel Scientist: I Place My Faith in Human Gods.\" Time (Ideas), 25 March 2016. https://time.com/4259269/nobel-scientist-religion/"
    url: "https://time.com/4259269/nobel-scientist-religion/"
    accessed: 2026-10-18
    reliability_note: "His own signed op-ed, read directly. Paragraph numbers count the op-ed's text only; the page also carries unrelated sponsored newsletter material, ignored."
    used_for: [childhood, worldview, heritage, timing, lane_b]
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

# James Watson

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

James Watson (1928–2025), American geneticist and biophysicist [S1]. Draft: primary_system ATHE (0.5); A 4 at 0.5; B 3 at 0.5 (alt 4; P35); mid_basin BELOW_THRESHOLD. Plotted (faded).

## Life and work

Chicago, Indiana, Copenhagen, Cambridge, Harvard, Cold Spring Harbor [S1].

## Contribution and impact

The double helix (1953) and Molecular Biology of the Gene (1965) [S1; S2].

## Childhood and education

Catholic mother, Episcopalian father; stopped going to mass by 11 [S3].

## Adult working worldview

'a lifelong atheist' (2016) [S3].

## Heritage (context only)

Irish Catholic and Episcopalian [S3].

## Timing

1953–1965, from age 25 [S1; S2].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No God [S3].

## Open questions

- Statements from 1953–1965.

## Research log

- 2026-10-18: Read Britannica (live) and the Time op-ed directly; Nature citation as in the Crick record.
