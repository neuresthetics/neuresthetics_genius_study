---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 4
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch N)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-17
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to mathematics. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-17, by: "Grok Bot", summary: "Record created (stage 3 batch N, order P32: F 4, rank 83). Basics from Britannica (Britannica Editors, unsigned; body only) and MacTutor (O'Connor and Robertson). Worldview: the 2016 Heidelberg Laureate Forum press conference (Plus magazine transcript), where he declines the question 'Who created this landscape?' and calls mathematics 'discovered'. primary_system UNKNOWN; A UNKNOWN; B BELOW_THRESHOLD (a view on mathematical truth alone, P30); mid_basin UNKNOWN (P19). Not plotted. Draft, not reviewed."}
    - {date: 2026-10-17, by: "Grok Bot", summary: "Batch N audit fix (#18): B BELOW_THRESHOLD now cites P16 (a view on mathematical truth alone), not P30; value unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #82, F4 rank 83). Needs: A UNKNOWN; B BELOW_THRESHOLD (math-truth alone, P16). Read Abel laureate interview Raussen/Skau EMS Newsletter 101 (2016) = AMS Notices 64:3 (2017) reprint (S5); Wikipedia EN dual-bio (S6, P50) with S1 Britannica; re-opened Plus HLF (S3), MacTutor (S2), Britannica Wayback (S1); skimmed PBS/NOVA Fermat interview and Hannah Fry / Science Museum accounts (finding aids only). P47 source_quality on S1–S6. Gap fills: Leys School; key_early_reading E.T. Bell / Hardy & Wright / Davenport (own voice S5); Coates PhD; Oxford Regius / return years; marriage Nada Canaan 1988 (S6). A stays UNKNOWN (HLF creator Q declined; Abel interview and Fry/NOVA searches yield no God/faith/church locus of his own; father Anglican theologian remains heritage context only). B stays BELOW_THRESHOLD (P16): 'discovered' math ontology (S3) and Abel remark that classical mathematics has sources in the physical sciences and in number theory are about math's origins/ontology, not a claim about the physical world's causal order; astrophysics interest is qualitative relaxation only (S5); not a P30 scientist (lasting contribution is number-theoretic, not a theory of physical systems). primary_system UNKNOWN; mid_basin UNKNOWN. Chart-moving NO (still unplotted). ODNB 403 this pass. No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: wiles-andrew
  display_name: "Andrew Wiles"
  roster:
    canonical_name: "Andrew Wiles"
    rank: 83
    F: 4
    models: [Claude, DeepSeek, GPT, Grok]
    band: "core (3–4)"
    status: core
    field: mathematics
    field_bucket: mathematics
  full_name: {value: "Sir Andrew John Wiles", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts ('In full')"}, {source: S6, locator: "lead / infobox"}], how_known: "Britannica; Wikipedia EN dual-bio (P50)."}
  native_name: {value: UNKNOWN, how_known: "English."}
  aliases:
    - {name: "Andrew-Wiles", kind: "roster alias"}

basics:
  birth:
    date: {value: "1953-04-11", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "infobox"}], how_known: "Britannica; Wikipedia EN (P50)."}
    place: {value: "Cambridge, England", modern_name: "Cambridge, United Kingdom", polity_then: "United Kingdom", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S6, locator: "Early life"}], how_known: "Britannica; Wikipedia EN (P50)."}
  death:
    date: {value: UNKNOWN, how_known: "Living (Britannica gives 'age 73')."}
    place: {value: UNKNOWN, how_known: "Living."}
  first_lasting_contribution_year: {value: 1995, certainty: 0.5, cites: [{source: S1, locator: "Fermat paragraphs"}], how_known: "The proof of Fermat's last theorem: announced in June 1993 with gaps, completed in 1995 with Richard Taylor and published in Annals of Mathematics 141:3 (1995) (S1). His earlier work on Iwasawa theory and Birch–Swinnerton-Dyer is named but not dated in the body (P39). 1995 is the coder's pick (the completed proof); 1993 is the alternative."}
  era_bucket: {value: "1950 on", certainty: 0.5, cites: [{source: S1, locator: "Fermat paragraphs"}], how_known: "From 1995 (P2); 1993 gives the same bucket."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "United Kingdom (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "career paragraph"}, {source: S6, locator: "Career"}], how_known: "Princeton from 1982, where the proof was done (S1); Oxford later (2011–; Regius 2018) (S6)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [English], certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading (English-language posts and papers)."}
  occupations: {value: ["mathematician", "professor"], certainty: 0.7, cites: [{source: S1, locator: "opening; career paragraph"}], how_known: "Britannica."}

contribution:
  primary_domain: mathematics
  fields: {value: ["number theory"], certainty: 0.7, cites: [{source: S1, locator: "'Wiles worked on a number of outstanding problems in number theory'"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Proof of Fermat's last theorem (via the semistable case of the Shimura–Taniyama–Weil conjecture; gap closed with Richard Taylor)", year: 1995, kind: theory, lasting: "'a British mathematician who proved Fermat's last theorem' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; Fermat paragraphs"}], how_known: "Britannica; a mathematical result, not a theory about physical or natural systems (P30)."}
  evidence_of_impact:
    - {value: "IMU special silver plaque (1998), Wolf Prize (1995–96), Abel Prize (2016), Copley Medal (2017); knighted 2000", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "opening; last paragraph"}], how_known: "Britannica."}
  major_works:
    - {value: "Modular Elliptic Curves and Fermat's Last Theorem", year: 1995, kind: "paper or paper series", certainty: 0.7, cites: [{source: S1, locator: "last paragraph"}], how_known: "Britannica (Annals of Mathematics 141:3, pp. 443–551)."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Proof of a centuries-old conjecture (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Church of England (father an ordained clergyman and theologian)", certainty: 0.5, cites: [{source: S2, locator: "opening paragraph"}, {source: S6, locator: "Early life"}], how_known: "MacTutor: father 'trained for ordination at Ridley Hall', curate, chaplain, later lecturer in New Testament studies and dean of Clare College; Wikipedia: later Regius Professor of Divinity at Oxford. The denomination is the coder's reading of Ridley Hall (an Anglican college); context only — not Andrew's adult locus."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father Maurice Frank Wiles (1923–2005), theologian and clergyman", role: father, certainty: 0.7, cites: [{source: S2, locator: "opening paragraph"}, {source: S6, locator: "Early life"}], how_known: "MacTutor; Wikipedia EN (P50)."}
    - {value: "Mother Patricia Margaret Mowll (1927–2005)", role: mother, certainty: 0.7, cites: [{source: S2, locator: "opening paragraph"}], how_known: "MacTutor."}
  household_circumstances: {value: "Lived in Ibadan, Nigeria, 1955–1959, where his father lectured; returned to Cambridge in 1959", certainty: 0.7, cites: [{source: S2, locator: "opening paragraph"}], how_known: "MacTutor."}
  schooling:
    - {value: "King's College School, Cambridge", stage: "elementary school", years: "1959–", certainty: 0.7, cites: [{source: S2, locator: "opening paragraph"}, {source: S6, locator: "Early life"}], how_known: "MacTutor ('a preparatory school'); Wikipedia EN."}
    - {value: "The Leys School, Cambridge", stage: "grammar or secondary school", years: UNKNOWN, certainty: 0.7, cites: [{source: S6, locator: "Early life"}], how_known: "Wikipedia EN."}
  early_mathematics: {value: "advanced mathematics", certainty: 0.5, cites: [{source: S1, locator: "'fascinated by the problem from the age of 10'"}, {source: S5, locator: "early interest / E.T. Bell"}], how_known: "Fascinated by Fermat's problem from age 10 (S1); Abel interview: pulled Bell's The Last Problem from library shelves at age ten (S5)."}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading:
    - {value: "E. T. Bell, The Last Problem (Fermat)", certainty: 0.7, cites: [{source: S5, locator: "early interest"}, {source: S6, locator: "Early life / WGBH-TV 1999"}], how_known: "Own voice in Abel interview (S5); Wikipedia cites WGBH-TV 1999 (S6)."}
    - {value: "G. H. Hardy and E. M. Wright, An Introduction to the Theory of Numbers", certainty: 0.7, cites: [{source: S5, locator: "Oxford / high-school teachers"}], how_known: "Own voice: a high-school teacher with a PhD in number theory gave him Hardy and Wright (S5)."}
    - {value: "H. Davenport, The Higher Arithmetic", certainty: 0.7, cites: [{source: S5, locator: "Oxford / high-school teachers"}], how_known: "Own voice in Abel interview (S5)."}
  childhood_mentors:
    - {value: "Mary Briggs (King's College School mathematics teacher)", role: teacher, certainty: 0.7, cites: [{source: S2, locator: "opening paragraph"}], how_known: "MacTutor."}
    - {value: "High-school teacher with a PhD in number theory (gave Hardy and Wright)", role: teacher, certainty: 0.5, cites: [{source: S5, locator: "before college"}], how_known: "Own voice in Abel interview; name not given."}
  languages_in_childhood: {value: [English], certainty: 0.5, cites: [{source: S2, locator: "opening paragraph"}], how_known: "Coder's reading."}
  notable_events:
    - {value: "Met Fermat's last theorem at about age 10 (E.T. Bell, The Last Problem)", year: 1963, age: 10, certainty: 0.7, cites: [{source: S1, locator: "'from the age of 10'"}, {source: S5, locator: "early interest"}], how_known: "Britannica; Abel interview own voice; year computed."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1995", certainty: 0.5, cites: [{source: S1, locator: "Fermat paragraphs"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing read."}
  primary_system: {value: UNKNOWN, how_known: "(interview) No statement on God or religion found across Plus HLF (S3), Abel EMS interview (S5), or secondary bios (S1, S2, S6). Asked 'Who created this landscape?' he declines ('mathematicians are not that philosophical') (S3). His father's Anglican theology career is heritage context only."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: PLATO, reason: "Mathematics 'discovered' is a view on mathematical truth only, not a worldview code (P16)."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "(interview) The one question about a creator was declined: 'Well, mathematicians are not that philosophical. (Laughter) We're artists, we just enjoy it and we leave it' (S3). Abel interview (S5) and Fry/NOVA-style public talks searched this pass contain no God, faith, church, Christian, atheist, or agnostic self-description. Father's clergy career is context only. Researched silence → UNKNOWN (P19)."}
    B_cause: {value: BELOW_THRESHOLD, how_known: "(interview) A mathematician with no lasting contribution about physical or natural systems, so not a scientist for working-science B (P30), and neither P33 nor P35 applies; B needs a statement about nature's order (P16). Statements read are on mathematical truth/ontology: 'I don't think I know a mathematician who doesn't think that it's discovered' (S3); Abel: classical mathematics has 'two sources: one of them coming from the physical sciences and the other one from… number theoretical speculations' (S5) — history of math's sources, not a claim that the physical world is lawfully ordered. Interest in 'animal behaviour or astrophysics… from a qualitative point of view' as relaxation (S5) is not a nature-order claim. Math discovery/invention alone → BELOW_THRESHOLD (P16)."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read."}
    D_authority: {value: UNKNOWN, how_known: "Nothing read."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7)."}
  mid_basin: {value: UNKNOWN, how_known: "A is UNKNOWN (P19)."}
  statements:
    - text: "To tell you the truth, I don't think I know a mathematician who doesn't think that it's discovered. So we're all on one side, I think. In some sense perhaps the proofs are created because they're more fallible and there are many options, but certainly in terms of the actual things we find we just think of it as discovered."
      cites: [{source: S3, locator: "answer to 'Do you think maths is discovered or invented?'"}]
      date: "2016-09"
      context: "Press conference at the Heidelberg Laureate Forum, September 2016, as published by Plus magazine (S3)."
      axes: [B_cause]
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "On mathematical truth / ontology only (P16); does not score B."
    - text: "Well, mathematicians are not that philosophical. (Laughter) We're artists, we just enjoy it and we leave it. There are philosophers and people at the more philosophical end of mathematics, there are some who do worry about that kind of thing, but we're not Bertrand Russells. We really aren't. (Laughter) We actually want to do [the maths]. We're the working artists."
      cites: [{source: S3, locator: "answer to 'Who created this landscape?'"}]
      date: "2016-09"
      context: "Same press conference; a reply to 'Who created this landscape?'"
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "A declined question; not scored. Researched silence → A UNKNOWN (P19)."
    - text: "Classical mathematics has, roughly speaking, two sources: one of them coming from the physical sciences and the other one from, let's for simplicity call it number theoretical speculations, with number theory not associated to applications."
      cites: [{source: S5, locator: "Investing in mathematics"}]
      date: "2016-05-23"
      context: "Abel Prize interview, Oslo, 23 May 2016 (Raussen and Skau); EMS Newsletter 101 / AMS Notices reprint."
      axes: [B_cause]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "History of mathematics' sources; not a claim about the physical world's causal order (P16). Kept as evidence that was checked and rejected for B."
  changes_over_life: []
  coder_notes: "Deepen D1 2026-10-24. Working year remains 1995; interviews are 2016 (after span). Under P31, no changes_over_life documenting a shift, but there is still no scoreable A or nature-order B statement in any year. Father Maurice Wiles (Anglican theologian / Regius Professor of Divinity) is heritage only. PLATO candidate noted and rejected for coding (math ontology ≠ worldview). No fallacy_catalog (Jason)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "English", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading of 'British', born in Cambridge."}
  religious_heritage_by_birth: {value: "Church of England (clergy family)", certainty: 0.5, cites: [{source: S2, locator: "opening paragraph"}, {source: S6, locator: "Early life"}], how_known: "As family_religion."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1995", certainty: 0.5, cites: [{source: S1, locator: "Fermat paragraphs"}], how_known: "Only one dated lasting contribution (P29, P30, P39)."}
  age_at_first_lasting_contribution: {value: 42, certainty: 0.5, cites: [{source: S1, locator: "opening; 1995"}], how_known: "1995 − 1953 = 42 (P30)."}
  first_evidence_of_lio_type_views: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S3, locator: "press conference"}, {source: S5, locator: "whole interview"}], how_known: "Plus HLF and Abel interview read; no God/nature-order LIO scores."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S3, locator: "press conference"}, {source: S5, locator: "whole interview"}], how_known: "As above."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Nothing read from 1995 on God or nature's order."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Nothing read tying geometric form to a worldview.", certainty: 0.5, cites: [{source: S3, locator: "press conference"}, {source: S5, locator: "whole interview"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S3, locator: "press conference"}], how_known: "Nothing read."}
  circle_present: {value: "unclear", rationale: "Nothing read on God.", certainty: 0.5, cites: [{source: S3, locator: "press conference"}, {source: S5, locator: "whole interview"}], how_known: "Coder's reading."}
  reading: "Mathematics as a discovered landscape; creator question declined; no theology and no nature-order claim stated."
  notes: "Lane B labeled belief only. Math discovered ≠ physical-world order (P16)."

institutions:
  - {value: "Princeton University", role: professor, years: "1982–2010", kind: university, certainty: 0.7, cites: [{source: S1, locator: "career paragraph"}, {source: S6, locator: "Career"}], how_known: "Britannica (emeritus 2012); Wikipedia: at Princeton 1982–2010 except short leaves, Eugene Higgins Professor 1994–2009."}
  - {value: "University of Oxford", role: "Royal Society Research Professor; Regius Professor of Mathematics (from 2018)", years: "2011–", kind: university, certainty: 0.7, cites: [{source: S6, locator: "Career"}, {source: S1, locator: "career paragraph"}], how_known: "Wikipedia EN; Britannica ('subsequently joined the faculty at Oxford'). Earlier Oxford Royal Society Research Professor 1988–1990 (S6)."}
  - {value: "University of Cambridge (Clare College)", role: "PhD student; junior research fellow", years: "1974–1980", kind: university, certainty: 0.7, cites: [{source: S1, locator: "education"}, {source: S2, locator: "PhD / Coates"}], how_known: "Britannica PhD 1980; MacTutor."}
collaborators:
  - {value: "Richard Taylor", relation: collaborator, note: "helped close the gap in the proof; co-author of the Hecke algebras paper", certainty: 0.7, cites: [{source: S1, locator: "Fermat paragraphs"}], how_known: "Britannica."}
  - {value: "John Coates", relation: "mentor or employer", note: "elliptic curves / Iwasawa theory", certainty: 0.7, cites: [{source: S2, locator: "PhD / Coates"}, {source: S5, locator: "Elliptic curves"}], how_known: "MacTutor; Abel interview own voice."}
  - {value: "Barry Mazur", relation: collaborator, note: "main conjecture of Iwasawa theory", certainty: 0.7, cites: [{source: S2, locator: "Harvard / Mazur"}, {source: S6, locator: "Career"}], how_known: "MacTutor; Wikipedia EN."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 83"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Britannica article is unsigned (Britannica Editors)."
    - "ODNB unreachable this pass (HTTP 403)."
  open_questions:
    - "Any later interview with an explicit God / atheism / agnosticism self-description (none found in Abel, HLF, Fry, NOVA this pass)."
    - "Any nature-order / laws-of-nature remark beyond math ontology (P16 bar); none found."
    - "ODNB entry if access becomes available."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "Britannica Editors. \"Andrew Wiles.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Andrew-Wiles. Read in Wayback snapshot 20260603100827."
    url: "https://www.britannica.com/biography/Andrew-Wiles"
    accessed: 2026-10-24
    reliability_note: "Unsigned article. Body only; Quick Facts used for the full name; Top Questions not cited."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, timing, institutions, collaborators]
  - id: S2
    type: secondary
    kind: other
    author: "J J O'Connor and E F Robertson"
    citation: "O'Connor, J. J., and E. F. Robertson. \"Andrew Wiles.\" MacTutor History of Mathematics Archive, University of St Andrews (last update December 2023). https://mathshistory.st-andrews.ac.uk/Biographies/Wiles/"
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Wiles/"
    accessed: 2026-10-24
    reliability_note: "Signed biography, read directly."
    source_quality: "reference entry"
    used_for: [childhood, heritage, institutions, collaborators]
  - id: S3
    type: secondary
    kind: other
    author: "The Plus Team"
    citation: "The Plus Team. \"Andrew Wiles: what does it feel like to do maths?\" Plus magazine, 1 December 2016. Based on a press conference at the Heidelberg Laureate Forum, September 2016. https://plus.maths.org/andrew-wiles-what-does-if-feel-do-maths"
    url: "https://plus.maths.org/andrew-wiles-what-does-if-feel-do-maths"
    accessed: 2026-10-24
    reliability_note: "Published transcript of his own first-person answers (P8), read directly."
    source_quality: "primary / own words"
    used_for: [worldview, timing, lane_b]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-17
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S5
    type: primary
    kind: other
    author: "Martin Raussen and Christian Skau (interviewers); Andrew Wiles (answers)"
    citation: "Raussen, Martin, and Christian Skau. \"Interview with Abel Laureate Sir Andrew Wiles.\" EMS Newsletter 101 (September 2016): 29–38. https://www.ems-ph.org/journals/newsletter/pdf/2016-09-101.pdf (also EMS Press article file; reprinted Notices of the AMS 64, no. 3 (March 2017): 198–207)."
    url: "https://ems.press/journals/mag/articles/14009"
    accessed: 2026-10-24
    reliability_note: "Abel Prize interview, Oslo, 23 May 2016; own-voice answers in a published mathematical-society newsletter (P8). Read from the EMS PDF extract; AMS Notices reprint cross-checked for the same text."
    source_quality: "primary / own words"
    used_for: [worldview, childhood, collaborators, timing, lane_b]
  - id: S6
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia contributors. \"Andrew Wiles.\" Wikipedia, The Free Encyclopedia. https://en.wikipedia.org/wiki/Andrew_Wiles. Dual biography with S1 Britannica under P50 (frozen roster)."
    url: "https://en.wikipedia.org/wiki/Andrew_Wiles"
    accessed: 2026-10-24
    reliability_note: "P50 dual-bio companion to Britannica; used for Early life / Career facts corroborated or gap-filled (Leys School, marriage, Oxford return / Regius). Not used alone for worldview scores."
    source_quality: "reference entry"
    used_for: [identity, basics, childhood, heritage, institutions, collaborators]
---

# Andrew Wiles

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Andrew Wiles (born 1953), British mathematician who proved Fermat's last theorem [S1]. Deepen D1: primary_system UNKNOWN; A UNKNOWN (interview decline + researched silence); B BELOW_THRESHOLD (math ontology / sources of mathematics, not nature-order — P16); mid_basin UNKNOWN. Not plotted.

## Life and work

Educated Merton College, Oxford (B.A. 1974) and Clare College, Cambridge (Ph.D. 1980, advisor John Coates) [S1; S2; S5]. Princeton professor from 1982 (proof years); Royal Society Research Professor at Oxford 1988–1990 and again from 2011; first Regius Professor of Mathematics at Oxford from 2018 [S1; S6]. Married Nada Canaan in 1988 [S6].

## Contribution and impact

Proof of Fermat's last theorem, completed 1995 with Taylor's help [S1]. Earlier lasting number-theory work includes cases of Birch–Swinnerton-Dyer and the main conjecture of Iwasawa theory (with Mazur) [S2; S6]. Abel Prize 2016; Copley Medal 2017; knighted 2000 [S1].

## Childhood and education

Son of the Anglican theologian Maurice Wiles; early years in Ibadan, Nigeria (1955–1959); King's College School and The Leys School, Cambridge [S2; S6]. At about age 10 found E. T. Bell's *The Last Problem* and was captivated by Fermat [S5; S1]. Before college read Hardy and Wright and Davenport [S5].

## Adult working worldview

Calls mathematics "discovered" and declines the question who created the mathematical landscape [S3]. Abel interview discusses sources of classical mathematics (physical sciences vs number-theoretic speculation) and qualitative interest in other sciences as relaxation — not a scored nature-order claim [S5]. No own-voice statement on God or personal religion found [S3; S5]. Father's clergy career is heritage context only [S2; S6].

## Heritage (context only)

Clergy family; Church of England by father [S2; S6].

## Timing

First lasting contribution 1995, at 42 [S1]. Worldview interviews are 2016 (after span); no LIO-type scores found in any year [S3; S5].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Mathematics-as-discovered and math's historical sources in physical science do **not** meet P16's nature-order bar [S3; S5]. Nothing read on God [S3; S5].

## Open questions

- Later interview with an explicit religious / non-religious self-description.
- Any laws-of-nature / physical-order remark that could score B under P16.
- ODNB if reachable.

## Research log

- 2026-10-17: Read Britannica (Wayback 20260603100827), MacTutor and the Plus transcript directly. Web search for any statement on religion found none.
- 2026-10-24 (D1): Read Abel EMS Newsletter 101 / AMS Notices reprint (S5); Wikipedia EN (S6, P50); re-opened Plus HLF, MacTutor, Britannica Wayback. Skimmed PBS/NOVA Fermat interview and Hannah Fry / Science Museum / Oxford evening accounts as finding aids (no A/B scores). Web search for God/faith/atheist/agnostic interviews: none. ODNB 403. A UNKNOWN and B BELOW_THRESHOLD unchanged. No fallacy_catalog (Jason).
