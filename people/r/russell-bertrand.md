---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 5
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch D)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-25
  change_log:
    - {date: 2026-10-25, by: "Grok Bot", summary: "Perpetual deepen: native_name TODO→Bertrand Arthur William Russell @0.7 (matches full_name / SEP). Chart-moving NO."}
    - {date: 2026-10-25, by: "Grok Bot", summary: "Perpetual deepen: religious_heritage_by_birth / baptism / catechism / family_religion TODO→UNKNOWN (grandmother upbringing; denomination not named on file). Chart-moving NO."}
    - {date: 2026-10-25, by: "Grok Bot", summary: "Perpetual deepen: score E_scope 4 (0.7) from What I Believe / Free Man's Worship in S5 plus WINaC Natural-Law (S2/S5) — man part of nature under same laws as stars and atoms; no in-group miracles. P7 world's order. C/D already 4. Chart-moving: no (A/B plotted). No figures/; no fallacy_catalog."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch D, order P32: F 5, rank 13). Basics from SEP (Irvine 2024). Worldview from 'Why I Am Not a Christian' (lecture 6 March 1927; Bertrand Russell Society web copy) and 'Am I an Atheist or an Agnostic?' (1947; web copy). Not a scientist (P30): logic and philosophy. primary_system AGNOS (0.5, alternative ATHE); A_locus 4 (0.5, P38); B_cause 4 (0.5, alternative 3); C 4 (0.7); D 4 (0.5); E TODO; mid_basin BELOW_THRESHOLD. Draft, not reviewed."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Audit fixes (fallacy_catalog audit of 3f4817e, run 1). B_cause 4 -> 3 (0.5, alternative 4) under P41. D_authority source titled ('Has Religion Made Useful Contributions to Civilization?', 1930, as quoted in SEP from A1957, p. 23). S3 redated 1947 -> 1949: first printed in The Literary Guide and Rationalist Review 64(7), July 1949, pp. 115-16 (Collected Papers vol. 11, no. 5); no change to age or period fields (earliest evidence is still 1927)."}
    - {date: 2026-10-23, by: "Grok Bot", summary: "Deepen pass D1 (queue #13). P47 source_quality on every source. Added S5 Why I Am Not a Christian and Other Essays (ed. Paul Edwards, Simon & Schuster / Allen & Unwin 1957; archive.org OCR of sixth paperback printing 1965) verifying WIANC p.5 disbelief, Natural-Law Argument pp.7–9, Free Man's Worship p.107 (1903; 'accidental collocations of atoms'; 'nature, omnipotent but blind'; no individual life beyond the grave), What I Believe ~p.48 ('Man is a part of nature'), and Has Religion… Objections ~p.30 ('no reason to suppose any religion true'). Added S6 MacTutor for dual-source basics (birth/death/Nobel). A_locus already multi-cited (S2+S3): labelled support corroborated; cites +S5; value/certainty stay 4 @ 0.5 (P38). B_cause was single on S2: cites +S5 → support single → corroborated; value/certainty stay 3 @ 0.5 (P41, alt 4). C support single → corroborated (S2+S5 Free Man). D primary-checked in S5 → certainty 0.5 → 0.7, support corroborated (S1+S5). first_evidence_of_lio_type_views 1927 → 1903 (Free Man's Worship, age 31); lio_views_relative_to_major_work after → during (at start of 1903–1913 span). Chart: faded hollow → faded filled (fill cue). Collected Papers vols. 10–11 still not opened; S3 web still 404 this pass. No fallacy_catalog (Jason 2026-10-23). Draft, not reviewed."}

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
  native_name: {value: "Bertrand Arthur William Russell", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Same as full_name (English); SEP."}
  aliases:
    - {name: "Bertrand-Russell", kind: "roster alias"}
    - {name: "Russell-Bertrand", kind: "roster alias"}
    - {name: "third Earl Russell", kind: "title or honorific"}

basics:
  birth:
    date: {value: "1872-05-18", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "§1 chronology (1872)"}, {source: S6, locator: "Born: 18 May 1872, Ravenscroft, Trelleck, Monmouthshire, Wales"}], how_known: "SEP + MacTutor (dual reference)."}
    place: {value: "Ravenscroft, Trelleck, Monmouthshire", modern_name: "Trellech, Monmouthshire, Wales, UK", polity_then: "United Kingdom", certainty: 0.7, cites: [{source: S1, locator: "§1 chronology"}, {source: S6, locator: "Born line"}], how_known: "SEP + MacTutor."}
  death:
    date: {value: "1970-02-02", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "§1 chronology (1970)"}, {source: S6, locator: "Died: 2 February 1970, Penrhyndeudraeth, Merioneth, Wales"}], how_known: "SEP + MacTutor."}
    place: {value: "Penrhyndeudraeth, Wales", modern_name: "Penrhyndeudraeth, Wales, UK", polity_then: "United Kingdom", certainty: 0.7, cites: [{source: S1, locator: "§1 chronology"}, {source: S6, locator: "Died line"}], how_known: "SEP + MacTutor."}
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
    - {value: "Nobel Prize in Literature, 1950", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "§1"}, {source: S6, locator: "Honours: Nobel Prize 1950"}], how_known: "SEP + MacTutor."}
  major_works:
    - {value: "Principia Mathematica (with A. N. Whitehead), 3 vols.", year: "1910–1913", kind: book, certainty: 0.7, cites: [{source: S1, locator: "bibliography"}], how_known: "SEP."}
  honours:
    - {value: "Order of Merit", year: 1949, certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
  definition_fit: {value: "clearly meets", rationale: "Paradox, type theory, descriptions; co-founder of analytic philosophy.", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated (grandmother Frances raised him; denomination not named in S1–S6)."}
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
      support: corroborated
      cites: [{source: S2, locator: "opening section ('why I do not believe in God and in immortality')"}, {source: S3, locator: "paragraph 6"}, {source: S5, locator: "Why I Am Not a Christian, p.5 ('why I do not believe in God and in immortality')"}]
      how_known: "His own published lecture (web S2) checked in the 1957 Edwards collection (S5, p.5) plus the 1949 agnostic essay (S3 web). P38 (v8's pick, 2026-10-15): stated disbelief in God scores A 4 at most 0.5 when the person also calls himself agnostic. Independent source ids → corroborated (P48); value/certainty unchanged."
      rationale: "At the LIO pole on the reading 'no separate God': he does 'not believe in God' (1927; S2/S5 p.5) and holds God's existence not 'sufficiently probable to be worth serious consideration' (1949; S3). This is a stated non-belief, not a locus view, and he declines to deny God outright ('I cannot prove that either the Christian God or the Homeric gods do not exist'), so 0.5 under P38. Alternative: BELOW_THRESHOLD as explicit suspension (§6, P20). Independent sources → corroborated (P48)."
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.5
      support: corroborated
      cites: [{source: S2, locator: "section 'The Natural-Law Argument'"}, {source: S5, locator: "Why I Am Not a Christian, Natural-Law Argument, pp.7–9; also A Free Man's Worship (1903) p.107; What I Believe (~1925) ~p.48"}]
      how_known: "His own published lecture ('Why I Am Not a Christian', 1927) in web copy (S2) checked in the 1957 Edwards collection (S5, pp.7–9); Free Man's Worship and What I Believe in the same volume add nature-without-lawgiver wording. P41 (v8's pick, 2026-10-15) caps a lawgiver denial without a stated no-exception claim at B 3, and he calls part of his account 'the momentary state of science that may change tomorrow', so 0.5. Independent source ids S2+S5 → support single → corroborated (P48); value/certainty unchanged."
      rationale: "Scored on his account of nature (P6, P16; not a scientist under P30). Natural laws 'are a description of how things do in fact behave' (S2; S5 pp.7–9), which denies a lawgiver but does not state that nature is exceptionless; the same passage says atoms are 'much less subject to law than people thought' and laws are 'statistical averages of just the sort that would emerge from chance'. Free Man's Worship (1903, S5 p.107): man's origin is 'accidental collocations of atoms' and 'nature, omnipotent but blind'; What I Believe (S5 ~p.48): 'Man is a part of nature' whose motions 'follow the same laws that describe the motions of stars and atoms'. Under P41 (extending P35), B 4 needs a stated no-exception claim, so 3. Named alternative 4: no exception or intervention is named, and chance is not a divine exemption. Independent sources → corroborated (P48)."
    C_ledger:
      value: 4
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S2, locator: "opening section"}, {source: S5, locator: "Why I Am Not a Christian, p.5; A Free Man's Worship, p.107"}]
      how_known: "His own published lecture (S2 web) checked in S5 p.5; Free Man's Worship (1903) in the same volume restates no individual survival. Web copy cap 0.7 for S2; S5 is a scholarly edition. Independent source ids → corroborated (P48)."
      rationale: "No personal reward or punishment after death: he does not believe 'in immortality' (1927; S2/S5 p.5); Free Man's Worship: 'no fire, no heroism, no intensity of thought and feeling, can preserve an individual life beyond the grave' (S5 p.107)."
    D_authority:
      value: 4
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S1, locator: "§6 (quoting A1957: 'there is no reason to suppose any religion true'; essay 'Has Religion Made Useful Contributions to Civilization?', 1930)"}, {source: S5, locator: "Has Religion Made Useful Contributions to Civilization?, The Objections to Religion, ~p.30"}]
      how_known: "SEP quote (S1) checked in the 1957 Edwards collection (S5 ~p.30; TOC places the essay at p.24; this printing's running head shows p.30 near the Objections section). Primary check done; certainty 0.7. Independent source ids → corroborated (P48). SEP's A1957 p.23 may be a different printing's pagination."
      rationale: "Observation and reason outrank revelation, which keeps no domain: 'The intellectual objection is that there is no reason to suppose any religion true' (S5 ~p.30; also via SEP)."
    E_scope:
      value: 4
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S5, locator: "What I Believe (~p.48; man part of nature; same laws as stars and atoms)"}, {source: S2, locator: "The Natural-Law Argument"}, {source: S5, locator: "Why I Am Not a Christian, Natural-Law Argument, pp.7–9"}]
      how_known: "Own published essays in the 1957 Edwards collection (S5) plus the 1927 lecture (S2 web, checked in S5). Written profession. Certainty 0.7 (web-copy ceiling on S2; S5 scholarly edition). Independent source ids → corroborated (P48)."
      rationale: "Scored on the world's order (decision P7). At the LIO pole: same rules for stars, atoms, and humans. What I Believe: 'Man is a part of nature' whose motions 'follow the same laws that describe the motions of stars and atoms' (S5). Natural-Law Argument: laws are descriptions of how things behave, with no lawgiver and no favoured-group exemption (S2/S5 pp.7–9). Free Man's Worship's blind nature (S5 p.107) fits the same pole. No hidden in-group miracles or answered petitions in the account of nature. Under P7, immortality denial is scored on C (already C 4)."
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus 4 is scored only at 0.5, under the 0.7 bar for the A ≥ 3 branch (P10).", note: "If A reached 0.7 the result would be false."}
  statements:
    - text: "first, why I do not believe in God and in immortality; and, secondly, why I do not think that Christ was the best and wisest of men"
      cites: [{source: S2, locator: "opening section"}, {source: S5, locator: "p.5"}]
      date: "1927-03-06"
      context: "Lecture at Battersea Town Hall for the South London Branch of the National Secular Society, issued as a booklet (Watts, 1927); reprinted in Edwards 1957."
      axes: [A_locus, C_ledger]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-23
      note: "Web copy (S2) checked against Why I Am Not a Christian and Other Essays, ed. Paul Edwards (Simon & Schuster / Allen & Unwin 1957), p.5 (S5). Collected Papers vol. 10 still not opened."
    - text: "natural laws are a description of how things do in fact behave"
      cites: [{source: S2, locator: "section 'The Natural-Law Argument'"}, {source: S5, locator: "pp.7–9"}]
      date: "1927-03-06"
      context: "Reply to the argument that natural law implies a lawgiver."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-23
      note: "Web copy (S2) checked against S5, Natural-Law Argument, pp.7–9 (fuller wording: 'natural laws are a description of how things do in fact behave, and being a mere description of what they in fact do, you cannot argue that there must be somebody who told them to do that')."
    - text: "That man is the product of causes which had no prevision of the end they were achieving; that his origin, his growth, his hopes and fears, his loves and his beliefs, are but the outcome of accidental collocations of atoms; that no fire, no heroism, no intensity of thought and feeling, can preserve an individual life beyond the grave"
      cites: [{source: S5, locator: "A Free Man's Worship, p.107"}]
      date: "1903"
      context: "Essay 'A Free Man's Worship' (Independent Review, 1903); reprinted in Edwards 1957 at pp.104–116."
      axes: [B_cause, C_ledger]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-23
      note: "Earliest dated LIO-type evidence read inside the major-work span. Same essay: 'nature, omnipotent but blind' (p.107) and closing 'omnipotent matter rolls on its relentless way' (~p.116)."
    - text: "Man is a part of nature, not something contrasted with nature. His thoughts and his bodily movements follow the same laws that describe the motions of stars and atoms."
      cites: [{source: S5, locator: "What I Believe, Nature and Man, ~p.48"}]
      date: "1925"
      context: "Essay 'What I Believe' (1925); reprinted in Edwards 1957 (TOC p.48)."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-23
      note: "Supports B as nature-law without a separate lawgiver; does not by itself state no-exception (P41)."
    - text: "The intellectual objection is that there is no reason to suppose any religion true"
      cites: [{source: S5, locator: "Has Religion Made Useful Contributions to Civilization?, The Objections to Religion, ~p.30"}, {source: S1, locator: "§6 (A1957 quote)"}]
      date: "1930"
      context: "Essay 'Has Religion Made Useful Contributions to Civilization?' (1930); reprinted in Edwards 1957."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-23
      note: "Primary check of the SEP quote; this printing's running head near the passage is p.30 (SEP cited A1957 p.23 — different pagination)."
    - text: "As a philosopher, if I were speaking to a purely philosophic audience I should say that I ought to describe myself as an Agnostic, because I do not think that there is a conclusive argument by which one prove that there is not a God."
      cites: [{source: S3, locator: "paragraph 3"}]
      date: "1949"
      context: "Essay 'Am I an Atheist or an Agnostic? A Plea for Tolerance in the Face of New Dogmas'."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "Web copy (dhspriory.org) was 404 this pass (2026-10-23); wording retained from prior read, including 'by which one prove'. First printed in The Literary Guide and Rationalist Review 64(7), July 1949, pp. 115-16 (Collected Papers vol. 11, no. 5). Authoritative reprint still pending."
  changes_over_life: []
  coder_notes: "Deepen D1 (queue #13): A labelled support corroborated (S2+S3+S5); B support single → corroborated (S2+S5); both stay @ 0.5 (P38 / P41). Free Man's Worship (1903, S5 p.107) moves first LIO-type evidence inside the major-work span. C support corroborated (S2+S5); D primary-checked in S5 → 0.7, support corroborated. S3 agnostic-essay URL 404 this pass — retained prior wording. Collected Papers vols. 10–11 still not opened. Coder's call: primary_system stays 0.5 for AGNOS/ATHE label wavering. Not a scientist (P30): B on his own account of nature (P16). E left TODO. No fallacy_catalog (Jason 2026-10-23)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "English aristocratic family; grandson of Prime Minister Lord John Russell", certainty: 0.7, cites: [{source: S1, locator: "§1 chronology"}], how_known: "SEP."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Orphaned and raised by grandmother Frances; Wikipedia/Britannica on file do not name the childhood household denomination. Adult agnostic/atheist is not birth-heritage (P19)."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "No baptism record opened in sources read."}
  childhood_catechism: {value: UNKNOWN, how_known: "No childhood catechism curriculum named."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1903–1913", certainty: 0.7, cites: [{source: S1, locator: "§2; bibliography"}], how_known: "Principles (1903) to Principia vol. 3 (1913) (P29, P30)."}
  age_at_first_lasting_contribution: {value: 31, certainty: 0.7, cites: [{source: S1, locator: "§1; §2"}], how_known: "1903 − 1872 = 31 (P30)."}
  first_evidence_of_lio_type_views: {value: "A Free Man's Worship: 'accidental collocations of atoms'; 'nature, omnipotent but blind'; no individual life beyond the grave (B/C); later WIANC Natural-Law (B 3) and 'I do not believe in God' (A 4)", year: 1903, age: 31, certainty: 0.7, cites: [{source: S5, locator: "A Free Man's Worship, p.107"}, {source: S2, locator: "opening; 'The Natural-Law Argument'"}], how_known: "Free Man's Worship (1903) read in Edwards 1957 (S5); earliest dated LIO-type evidence at 3/4. 1927 WIANC remains the clearest numbered-axis wording for A 4 and B 3."}
  lio_views_relative_to_major_work: {value: "during major work", rationale: "Free Man's Worship (1903) falls at the start of the 1903–1913 major-work span; WIANC (1927) is after the span end.", certainty: 0.7, cites: [{source: S5, locator: "A Free Man's Worship, 1903 / p.107"}, {source: S1, locator: "§2 (major work 1903–1913)"}], how_known: "Dated texts read."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "Principia derives mathematics from logical axioms.", certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "SEP."}
  form_acquired: {value: "childhood or adolescence", certainty: 0.5, cites: [{source: S1, locator: "§1 chronology (1883 geometry)"}], how_known: "Coder's reading of the 1883 geometry lessons."}
  circle_present: {value: "no", rationale: "No God–Nature identity; laws are descriptions with no lawgiver; Free Man's Worship has blind omnipotent nature, not God=Nature.", certainty: 0.5, cites: [{source: S2, locator: "'The Natural-Law Argument'"}, {source: S5, locator: "Natural-Law pp.7–9; Free Man's Worship p.107"}], how_known: "Coder's reading."}
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
    - "Britannica blocked (Cloudflare, 2026-10-15); basics now SEP + MacTutor."
    - "S2 and S3 remain unofficial web copies (0.7 cap where they are sole); WIANC / Free Man / What I Believe / Has Religion passages checked in S5 1957 Edwards collection (scholarly edition)."
    - "S3 URL (dhspriory.org) returned 404 on 2026-10-23; prior wording retained pending Collected Papers vol. 11."
  open_questions:
    - "Check WIANC and the 1949 agnostic essay against Collected Papers vols. 10 and 11 (McMaster)."
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
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Bertrand Russell"
    year: 1927
    citation: "Russell, Bertrand. Why I Am Not a Christian. Lecture at Battersea Town Hall, 6 March 1927. London: Watts & Co. for the Rationalist Press Association, 1927. Web copy: Bertrand Russell Society, https://users.drew.edu/jlenz/whynot.html."
    url: "https://users.drew.edu/jlenz/whynot.html"
    accessed: 2026-10-15
    reliability_note: "Unofficial web copy of the 1927 pamphlet; 0.7 cap (§7). Wording checked against S5 1957 edition."
    source_quality: "unofficial web copy"
    used_for: [worldview, timing, lane_b]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "Bertrand Russell"
    year: 1949
    citation: "Russell, Bertrand. \"Am I an Atheist or an Agnostic? A Plea for Tolerance in the Face of New Dogmas\" (1949). Web copy: https://dhspriory.org/kenny/PhilTexts/Russell/AtheistOrAgnostic.htm."
    url: "https://dhspriory.org/kenny/PhilTexts/Russell/AtheistOrAgnostic.htm"
    accessed: 2026-10-15
    reliability_note: "Unofficial web copy (taken from Positive Atheism). First printed July 1949 in The Literary Guide and Rationalist Review 64(7): 115-16 (Collected Papers vol. 11, no. 5; Routledge 2024 headnote). 0.7 cap. URL 404 on 2026-10-23 re-check."
    source_quality: "unofficial web copy"
    used_for: [worldview]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S5
    type: primary
    kind: "published work by the subject"
    author: "Bertrand Russell"
    year: 1957
    citation: "Russell, Bertrand. Why I Am Not a Christian and Other Essays on Religion and Related Subjects. Edited by Paul Edwards. New York: Simon and Schuster; London: George Allen & Unwin, 1957 (sixth paperback printing 1965 observed). Internet Archive identifier why-i-am-not-a-christian (OCR)."
    url: "https://archive.org/details/why-i-am-not-a-christian"
    accessed: 2026-10-23
    reliability_note: "Edited collection of Russell's own essays (Edwards). Used as scholarly edition check of WIANC (pp.3–23), Has Religion… (from p.24), What I Believe (from p.48), A Free Man's Worship (from p.104). OCR of a 1965 paperback printing; page numbers from running heads / TOC."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview, timing, lane_b]
  - id: S6
    type: secondary
    kind: encyclopedia
    author: "J J O'Connor and E F Robertson"
    year: 2003
    citation: "O'Connor, J. J., and E. F. Robertson. \"Bertrand Russell.\" MacTutor History of Mathematics Archive, University of St Andrews. https://mathshistory.st-andrews.ac.uk/Biographies/Russell/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Russell/"
    accessed: 2026-10-23
    reliability_note: "Standard mathematics-history reference biography; used for birth/death/Nobel dual-source with SEP."
    source_quality: "reference entry"
    used_for: [basics, contribution]
---

# Bertrand Russell

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Bertrand Russell (1872–1970), British philosopher and logician, found the paradox named after him, wrote Principia Mathematica with Whitehead and gave the theory of descriptions [S1; S6]. In A Free Man's Worship (1903) he wrote that man's origin is "accidental collocations of atoms" and that "nature, omnipotent but blind" rolls on [S5, p.107]; in 1927 he said he did "not believe in God and in immortality" and that natural laws are "a description of how things do in fact behave" [S2; S5, pp.5, 7–9]; in 1949 he called himself an agnostic to philosophers and an atheist to the public [S3]. Deepen D1 (P47–P50): primary_system AGNOS (0.5, alternative ATHE); A 4 @ 0.5, written_profession, support corroborated (S2+S3+S5; P38); B 3 @ 0.5, written_profession, support single → corroborated (S2+S5; P41, alt 4); C 4 @ 0.7 support corroborated; D 4 @ 0.7 support corroborated; mid_basin BELOW_THRESHOLD. Chart: faded hollow → faded filled (fill cue).

## Life and work

Born 18 May 1872 at Ravenscroft, Trelleck; died 2 February 1970 at Penrhyndeudraeth [S1; S6]. Cambridge; dismissed 1916 and imprisoned 1918 for anti-war writing; Nobel Prize in Literature 1950 [S1; S6].

## Contribution and impact

Paradox and logicism (1903), descriptions (1905), Principia (1910–1913) [S1].

## Childhood and education

Orphaned, raised by his grandmother; geometry from his brother at 11 [S1].

## Adult working worldview

Disbelief in God and immortality; laws of nature as descriptions with no lawgiver; Free Man's Worship (1903) already places man in blind nature without personal survival [S2; S3; S5].

## Heritage (context only)

Aristocratic English family [S1].

## Timing

First lasting contribution 1903, at 31. Earliest dated LIO-type statement read: A Free Man's Worship, 1903 (during major work) [S5].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form present; circle absent [S1; S2; S5].

## Open questions

- Collected Papers vols. 10–11 check; Score E.

## Research log

- 2026-10-15: Read SEP (Irvine 2024), the BRS web copy of Why I Am Not a Christian and a web copy of the 1947/1949 essay. Britannica blocked.
- 2026-10-23: Deepen D1 (queue #13). Edwards 1957 WIANC collection archive OCR (S5): WIANC pp.5, 7–9; Free Man's Worship p.107; What I Believe ~p.48; Has Religion Objections ~p.30. MacTutor (S6) for birth/death/Nobel. A labelled corroborated; B single → corroborated; chart fill hollow → filled. P47 labels. S3 URL 404 this pass. No fallacy_catalog (Jason 2026-10-23).
