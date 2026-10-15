---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch D)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-15
  change_log:
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch D, order P32: F 5, rank 13). Basics from SEP (Irvine 2024). Worldview from 'Why I Am Not a Christian' (lecture 6 March 1927; Bertrand Russell Society web copy) and 'Am I an Atheist or an Agnostic?' (1947; web copy). Not a scientist (P30): logic and philosophy. primary_system AGNOS (0.5, alternative ATHE); A_locus 4 (0.5, P38); B_cause 4 (0.5, alternative 3); C 4 (0.7); D 4 (0.5); E TODO; mid_basin BELOW_THRESHOLD. Draft, not reviewed."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Audit fixes (fallacy_catalog audit of 3f4817e, run 1). B_cause 4 -> 3 (0.5, alternative 4) under P41. D_authority source titled ('Has Religion Made Useful Contributions to Civilization?', 1930, as quoted in SEP from A1957, p. 23). S3 redated 1947 -> 1949: first printed in The Literary Guide and Rationalist Review 64(7), July 1949, pp. 115-16 (Collected Papers vol. 11, no. 5); no change to age or period fields (earliest evidence is still 1927)."}

identity:
  id: russell-bertrand
  display_name: "Bertrand Russell"
  roster:
    canonical_name: "Bertrand Russell"
    rank: 13
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: philosophy
    field_bucket: philosophy
  full_name: {value: "Bertrand Arthur William Russell", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP alone."}
  native_name: {value: TODO}
  aliases:
    - {name: "Bertrand-Russell", kind: "roster alias"}
    - {name: "Russell-Bertrand", kind: "roster alias"}
    - {name: "third Earl Russell", kind: "title or honorific"}

basics:
  birth:
    date: {value: "1872-05-18", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "§1 chronology (1872)"}], how_known: "SEP alone."}
    place: {value: "Ravenscroft, Trelleck, Monmouthshire", modern_name: "Trellech, Monmouthshire, Wales, UK", polity_then: "United Kingdom", certainty: 0.7, cites: [{source: S1, locator: "§1 chronology"}], how_known: "SEP alone."}
  death:
    date: {value: "1970-02-02", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "§1 chronology (1970)"}], how_known: "SEP alone."}
    place: {value: "Penrhyndeudraeth, Wales", modern_name: "Penrhyndeudraeth, Wales, UK", polity_then: "United Kingdom", certainty: 0.7, cites: [{source: S1, locator: "§1 chronology"}], how_known: "SEP alone."}
  first_lasting_contribution_year: {value: 1903, certainty: 0.7, cites: [{source: S1, locator: "§2 (paradox found 1901 while working on The Principles of Mathematics, 1903)"}], how_known: "Russell's paradox and logicism in The Principles of Mathematics (1903), the earliest documented public statement read (P30). SEP also names a 1901 article 'Recent Work on the Principles of Mathematics' defending logicism and a 1902 letter to Frege (private), so the year might be 1901 for logicism; SEP alone, 0.7."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "1901 and 1903 are both in this bucket (P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "UK is Northern Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "§1 (Trinity College, Cambridge)"}], how_known: "SEP."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "As recorded."}
  languages_of_work: {value: [English], certainty: 0.7, cites: [{source: S1, locator: "bibliography"}], how_known: "SEP."}
  occupations: {value: ["philosopher", "logician", "writer"], certainty: 0.7, cites: [{source: S1, locator: "opening; §1 ('Author' on his passport)"}], how_known: "SEP."}

contribution:
  fields: {value: ["mathematical logic", "philosophy of mathematics", "analytic philosophy"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}
  lasting_original_contributions:
    - {value: "Russell's paradox and the logicist programme (The Principles of Mathematics)", year: 1903, kind: discovery, lasting: "prompted 'a large amount of work in logic, set theory, and the philosophy and foundations of mathematics' (S1 §2)", certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "SEP."}
    - {value: "Theory of definite descriptions ('On Denoting', Mind)", year: 1905, kind: theory, lasting: "standard analysis in philosophy of language", certainty: 0.7, cites: [{source: S1, locator: "§4; bibliography (1905)"}], how_known: "SEP."}
    - {value: "Theory of types and Principia Mathematica (with Whitehead)", year: "1910–1913", kind: work, lasting: "basis of type theory", certainty: 0.7, cites: [{source: S1, locator: "§2; bibliography"}], how_known: "SEP."}
  evidence_of_impact:
    - {value: "Nobel Prize in Literature, 1950", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
  major_works:
    - {value: "Principia Mathematica (with A. N. Whitehead), 3 vols.", year: "1910–1913", kind: book, certainty: 0.7, cites: [{source: S1, locator: "bibliography"}], how_known: "SEP."}
  honours:
    - {value: "Order of Merit", year: 1949, certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
  definition_fit: {value: "clearly meets", rationale: "Paradox, type theory, descriptions; co-founder of analytic philosophy.", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}

childhood:
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Orphaned young (mother 1874, father 1876); grandparents won custody 'rather than have them raised as free-thinkers'; raised by his grandmother at Pembroke Lodge", role: other, certainty: 0.7, cites: [{source: S1, locator: "§1 chronology (1874, 1876, 1878)"}], how_known: "SEP."}
  household_circumstances: {value: TODO}
  schooling: []
  early_mathematics: {value: "geometry (Euclid-style proof)", certainty: 0.7, cites: [{source: S1, locator: "§1 chronology (1883: first lessons in geometry from his brother Frank)"}], how_known: "SEP."}
  early_geometric_style_reasoning: {value: "First geometry lessons from his brother Frank at about 11 (1883)", certainty: 0.7, cites: [{source: S1, locator: "§1 chronology"}], how_known: "SEP."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: TODO}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1903–1913", certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "'As a philosopher [...] I ought to describe myself as an Agnostic', but to 'the ordinary man in the street' an Atheist (1949)", certainty: 0.7, cites: [{source: S3, locator: "paragraphs 3–4"}], how_known: "His own published essay, read in an unofficial web copy (0.7 cap)."}
  primary_system:
    value: AGNOS
    basis: written_profession
    certainty: 0.5
    cites: [{source: S3, locator: "paragraphs 3–6"}, {source: S1, locator: "§6 (prison form: 'agnostic')"}]
    how_known: "His own published text (web copy cap 0.7), lowered to 0.5 because he says 'sometimes I have said one and sometimes the other without any clear principle'."
    rationale: "AGNOS (explicit suspension): he holds there is no conclusive argument either way and gave 'agnostic' as his religion at Brixton (S1 §6). Named alternative ATHE: he says he 'ought to say \"Atheist\"' on official forms because the existence of God is not 'sufficiently probable to be worth serious consideration' (S3). AGNOS is a stub system file (P14)."
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: AGNOS, reason: "Self-description to a philosophical audience. Chosen at 0.5."}
    - {code: ATHE, reason: "His 'popular' self-description; SEP calls his atheism 'evangelical'. Named alternative."}
    - {code: SECHUM, reason: "Public humanist and rationalist activity (the 1927 lecture was for the National Secular Society), but his metaphysics is stated directly; rejected."}
  lio_axes:
    A_locus:
      value: 4
      basis: written_profession
      certainty: 0.5
      cites: [{source: S2, locator: "opening section ('why I do not believe in God and in immortality')"}, {source: S3, locator: "paragraph 6"}]
      how_known: "His own published lecture and essay (web copies). P38 (v8's pick, 2026-10-15): stated disbelief in God scores A 4 at most 0.5 when the person also calls himself agnostic."
      rationale: "At the LIO pole on the reading 'no separate God': he does 'not believe in God' (1927) and holds God's existence not 'sufficiently probable to be worth serious consideration' (1949). This is a stated non-belief, not a locus view, and he declines to deny God outright ('I cannot prove that either the Christian God or the Homeric gods do not exist'), so 0.5 under P38. Alternative: BELOW_THRESHOLD as explicit suspension (§6, P20)."
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.5
      cites: [{source: S2, locator: "section 'The Natural-Law Argument'"}]
      how_known: "His own published lecture ('Why I Am Not a Christian', 1927), read in a web copy (0.7 cap); P41 (v8's pick, 2026-10-15) caps a lawgiver denial without a stated no-exception claim at B 3, and he calls part of his account 'the momentary state of science that may change tomorrow', so 0.5."
      rationale: "Scored on his account of nature (P6, P16; not a scientist under P30). Natural laws 'are a description of how things do in fact behave', which denies a lawgiver but does not state that nature is exceptionless; the same passage says atoms are 'much less subject to law than people thought' and laws are 'statistical averages of just the sort that would emerge from chance'. Under P41 (extending P35), B 4 needs a stated no-exception claim, so 3. Named alternative 4: no exception or intervention is named, and chance is not a divine exemption."
    C_ledger:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S2, locator: "opening section"}]
      how_known: "His own published lecture; web copy cap 0.7."
      rationale: "No personal reward or punishment after death: he does not believe 'in immortality' (1927)."
    D_authority:
      value: 4
      basis: written_profession
      certainty: 0.5
      cites: [{source: S1, locator: "§6 (quoting A1957, p. 23: 'there is no reason to suppose any religion true'; essay 'Has Religion Made Useful Contributions to Civilization?', 1930, attribution probable)"}]
      how_known: "Quoted in SEP from 'Has Religion Made Useful Contributions to Civilization?' (1930; reprinted in Why I Am Not a Christian, 1957 = A1957, p. 23; attribution of the page to that essay is probable, not checked); primary check pending, so 0.5 (§7, P26)."
      rationale: "Observation and reason outrank revelation, which keeps no domain: 'The intellectual objection is that there is no reason to suppose any religion true' (via SEP)."
    E_scope: {value: TODO}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus 4 is scored only at 0.5, under the 0.7 bar for the A ≥ 3 branch (P10).", note: "If A reached 0.7 the result would be false."}
  statements:
    - text: "first, why I do not believe in God and in immortality; and, secondly, why I do not think that Christ was the best and wisest of men"
      cites: [{source: S2, locator: "opening section"}]
      date: "1927-03-06"
      context: "Lecture at Battersea Town Hall for the South London Branch of the National Secular Society, issued as a booklet (Watts, 1927)."
      axes: [A_locus, C_ledger]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "Read on the Bertrand Russell Society website (users.drew.edu/jlenz), an unofficial web copy; check against the 1927 Watts pamphlet or Collected Papers vol. 10 pending."
    - text: "natural laws are a description of how things do in fact behave"
      cites: [{source: S2, locator: "section 'The Natural-Law Argument'"}]
      date: "1927-03-06"
      context: "Reply to the argument that natural law implies a lawgiver."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "Same web copy."
    - text: "As a philosopher, if I were speaking to a purely philosophic audience I should say that I ought to describe myself as an Agnostic, because I do not think that there is a conclusive argument by which one prove that there is not a God."
      cites: [{source: S3, locator: "paragraph 3"}]
      date: "1949"
      context: "Essay 'Am I an Atheist or an Agnostic? A Plea for Tolerance in the Face of New Dogmas'."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "Web copy (dhspriory.org); wording as printed there, including 'by which one prove'. First printed in The Literary Guide and Rationalist Review 64(7), July 1949, pp. 115-16, as an untitled report of his speech (Collected Papers vol. 11, no. 5)."
  changes_over_life: []
  coder_notes: "Evidence dates from 1927 and 1949, after the 1903–1913 span; no change of view between them is documented in the sources read (SEP §1 notes he failed to get a Liberal nomination in 1910 'because of his atheism'), so it counts for the span at its normal certainty (P31). Coder's call: primary_system lowered to 0.5 because of his own wavering between the labels. Not a scientist (P30): his lasting contributions are in logic and philosophy, so B rests on his own statement (P16). E left TODO."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "English aristocratic family; grandson of Prime Minister Lord John Russell", certainty: 0.7, cites: [{source: S1, locator: "§1 chronology"}], how_known: "SEP."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1903–1913", certainty: 0.7, cites: [{source: S1, locator: "§2; bibliography"}], how_known: "Principles (1903) to Principia vol. 3 (1913) (P29, P30)."}
  age_at_first_lasting_contribution: {value: 31, certainty: 0.7, cites: [{source: S1, locator: "§1; §2"}], how_known: "1903 − 1872 = 31 (P30)."}
  first_evidence_of_lio_type_views: {value: "'natural laws are a description of how things do in fact behave' (B 3) and 'I do not believe in God' (A 4)", year: 1927, age: 55, certainty: 0.5, cites: [{source: S2, locator: "opening; 'The Natural-Law Argument'"}], how_known: "Earliest dated statement read that is scored at 3 or 4. Earlier works (A Free Man's Worship, 1903) were not read: 'earlier works not read'."}
  lio_views_relative_to_major_work: {value: "after major work", rationale: "The earliest statement read (1927) is after the 1913 end; SEP's 1910 note suggests earlier views, so this may move.", certainty: 0.5, cites: [{source: S2, locator: "date"}, {source: S1, locator: "§1 (1910)"}], how_known: "Dated texts read."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "Principia derives mathematics from logical axioms.", certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "SEP."}
  form_acquired: {value: "childhood or adolescence", certainty: 0.5, cites: [{source: S1, locator: "§1 chronology (1883 geometry)"}], how_known: "Coder's reading of the 1883 geometry lessons."}
  circle_present: {value: "no", rationale: "No God–Nature identity; laws are descriptions with no lawgiver.", certainty: 0.5, cites: [{source: S2, locator: "'The Natural-Law Argument'"}], how_known: "Coder's reading."}
  reading: "As belief, not finding: form present, circle absent. A case that does not fit H1's circle."
  notes: ""

institutions:
  - {value: "Trinity College, Cambridge", role: "student, lecturer, fellow", years: "1890–1916; 1944–", kind: university, certainty: 0.7, cites: [{source: S1, locator: "§1 chronology"}], how_known: "SEP."}
collaborators:
  - {value: "Alfred North Whitehead", relation: collaborator, certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "SEP."}
  - {value: "Ludwig Wittgenstein", relation: "student or assistant", certainty: 0.7, cites: [{source: S1, locator: "§§1, 8"}], how_known: "SEP."}
  - {value: "Gottlob Frege", relation: correspondent, certainty: 0.7, cites: [{source: S1, locator: "§1 chronology (1902)"}], how_known: "SEP."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 13"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Britannica blocked (Cloudflare, 2026-10-15); basics from SEP alone, 0.7."
    - "Both worldview texts read in unofficial web copies; authoritative edition check pending."
  open_questions:
    - "Check the quotes against Collected Papers vols. 10 and 11 (McMaster) and read A Free Man's Worship (1903) for evidence inside the span."
    - "Score E."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Andrew David Irvine"
    year: 2024
    citation: "Irvine, Andrew David. \"Bertrand Russell.\" Stanford Encyclopedia of Philosophy, first published 7 December 1995, substantive revision 15 October 2024. https://plato.stanford.edu/entries/russell/."
    url: "https://plato.stanford.edu/entries/russell/"
    accessed: 2026-10-15
    reliability_note: "Peer-reviewed reference article."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Bertrand Russell"
    year: 1927
    citation: "Russell, Bertrand. Why I Am Not a Christian. Lecture at Battersea Town Hall, 6 March 1927. London: Watts & Co. for the Rationalist Press Association, 1927. Web copy: Bertrand Russell Society, https://users.drew.edu/jlenz/whynot.html."
    url: "https://users.drew.edu/jlenz/whynot.html"
    accessed: 2026-10-15
    reliability_note: "Unofficial web copy of the 1927 pamphlet; 0.7 cap (§7)."
    used_for: [worldview, timing, lane_b]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "Bertrand Russell"
    year: 1949
    citation: "Russell, Bertrand. \"Am I an Atheist or an Agnostic? A Plea for Tolerance in the Face of New Dogmas\" (1949). Web copy: https://dhspriory.org/kenny/PhilTexts/Russell/AtheistOrAgnostic.htm."
    url: "https://dhspriory.org/kenny/PhilTexts/Russell/AtheistOrAgnostic.htm"
    accessed: 2026-10-15
    reliability_note: "Unofficial web copy (taken from Positive Atheism). First printed July 1949 in The Literary Guide and Rationalist Review 64(7): 115-16 (Collected Papers vol. 11, no. 5; Routledge 2024 headnote). 0.7 cap."
    used_for: [worldview]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Bertrand Russell

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Bertrand Russell (1872–1970), British philosopher and logician, found the paradox named after him, wrote Principia Mathematica with Whitehead and gave the theory of descriptions [S1]. In 1927 he said he did 'not believe in God and in immortality' [S2]; in 1949 he called himself an agnostic to philosophers and an atheist to the public [S3]. Draft: primary_system AGNOS (0.5, alternative ATHE); A 4 (0.5, P38); B 3 (0.5, alternative 4; P41); mid_basin BELOW_THRESHOLD.

## Life and work

Cambridge; dismissed 1916 and imprisoned 1918 for anti-war writing; Nobel Prize in Literature 1950 [S1].

## Contribution and impact

Paradox and logicism (1903), descriptions (1905), Principia (1910–1913) [S1].

## Childhood and education

Orphaned, raised by his grandmother; geometry from his brother at 11 [S1].

## Adult working worldview

Disbelief in God and immortality; laws of nature as descriptions with no lawgiver [S2; S3].

## Heritage (context only)

Aristocratic English family [S1].

## Timing

First lasting contribution 1903, at 31. Earliest dated LIO-type statement read: 1927.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form present; circle absent [S1; S2].

## Open questions

- Collected Papers check; A Free Man's Worship.

## Research log

- 2026-10-15: Read SEP (Irvine 2024), the BRS web copy of Why I Am Not a Christian and a web copy of the 1947 essay. Britannica blocked.
