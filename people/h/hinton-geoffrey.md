---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z9)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to computer_science. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen D1 (skip catch-up 9/13): On Point WBUR 2025-01-10 (S4) corroborates atheist-family / school 'nonsense' own-voice; Wikipedia EN (S5) dual bio (P50). primary ATHE and A 4 stay at 0.5 with support corroborated (S2+S4; P48); after span → P20. B UNKNOWN held (RQ-Z9-1 / P33; no new lasting natural-system theory listed; no P16 own-voice). mid BELOW_THRESHOLD; not plotted. Chart-moving NO. P47 source_quality on all sources."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z9 audit (RQ-Z9-1, v8's call on the auditor's advice): not a scientist as listed; B stays UNKNOWN, not plotted. Leads added: prize motivation 'discoveries and inventions'; interview 'theory' and 'for discovering how the brain worked'."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z9, order P32: F 3, rank 171). Basics from NobelPrize.org facts (Physics 2024). Own words: Nobel Prize interview, 6 December 2024 (NobelPrize.org transcript), after the span: parents 'both atheists'; at his Christian school belief in God 'seemed to me it was just obvious nonsense, and it turns out I was right'; 'other people also don't believe in God'. primary_system ATHE (0.5, alt AGNOS); A 4 (0.5, alts BELOW_THRESHOLD and 3; P20, Chomsky and Kahneman precedents). Not a scientist as listed: the Boltzmann machine is called an 'invention' (S1; P33; Hassabis precedent), so B UNKNOWN pending RQ-Z9-1. C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD (A ≥ 3 only at 0.5, P10). Span 1983–1985, age 36. Not plotted (no B). Draft, not reviewed."}

identity:
  id: hinton-geoffrey
  display_name: "Geoffrey Hinton"
  roster:
    canonical_name: "Geoffrey Hinton"
    rank: 171
    F: 3
    models: [Claude, DeepSeek, GPT]
    band: "core (3–4)"
    status: "provisional"
    field: "computer science"
    field_bucket: "computer science / AI"
  full_name: {value: "Geoffrey Everest Hinton", certainty: 0.7, cites: [{source: S5, locator: "infobox / lead"}], how_known: "Wikipedia EN (dual bio, P50); NobelPrize.org facts use Geoffrey Hinton (S1)."}
  native_name: {value: "Geoffrey Hinton", certainty: 0.7, cites: [{source: S1, locator: "heading"}], how_known: "NobelPrize.org."}
  aliases:
    - {name: "Geoffrey-Hinton", kind: "roster alias"}
    - {name: "Geoffrey Everest Hinton", kind: "birth name"}

basics:
  birth:
    date: {value: "1947-12-06", certainty: 0.7, cites: [{source: S1, locator: "Born"}, {source: S5, locator: "infobox"}], how_known: "NobelPrize.org; Wikipedia EN."}
    place: {value: "London", modern_name: "London, United Kingdom", polity_then: "United Kingdom", certainty: 0.7, cites: [{source: S1, locator: "Born"}, {source: S5, locator: "infobox"}], how_known: "NobelPrize.org; Wikipedia EN (Wimbledon, England)."}
  death:
    date: {value: UNKNOWN, how_known: "Living (not stated as dead in the sources read)."}
    place: {value: UNKNOWN, how_known: "Living."}
  first_lasting_contribution_year: {value: 1983, certainty: 0.7, cites: [{source: S1, locator: "Work"}], how_known: "Boltzmann machine, 1983–1985 (range start, P12)."}
  era_bucket: {value: "1950 on", certainty: 1.0, cites: [{source: S1, locator: "Work"}], how_known: "1983 (P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "Born"}], how_known: "UK (P3)."}
  region_of_work: {value: "North America", certainty: 0.7, cites: [{source: S1, locator: "Affiliation"}, {source: S5, locator: "Career / Carnegie Mellon; Toronto"}], how_known: "Boltzmann / PDP-era work at Carnegie Mellon (S5); Toronto affiliation at the award (S1)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Inferred."}
  occupations: {value: ["computer scientist", "cognitive scientist", "professor"], certainty: 0.7, cites: [{source: S1, locator: "Affiliation"}, {source: S5, locator: "lead"}], how_known: "NobelPrize.org; Wikipedia EN."}

contribution:
  primary_domain: computer_science
  fields: {value: ["machine learning", "artificial neural networks"], certainty: 0.7, cites: [{source: S1, locator: "Prize motivation"}], how_known: "NobelPrize.org."}
  lasting_original_contributions:
    - {value: "Boltzmann machine", year: 1983, kind: "invention", lasting: "'The invention became significant, for example, for classifying and creating images' (S1); Nobel Prize 2024", certainty: 0.7, cites: [{source: S1, locator: "Work"}], how_known: "NobelPrize.org: 'In 1983–1985, Geoffrey Hinton used tools from statistical physics to create the Boltzmann machine'."}
  evidence_of_impact:
    - {value: "Nobel Prize in Physics 2024 'for foundational discoveries and inventions that enable machine learning with artificial neural networks'", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "Prize motivation"}], how_known: "NobelPrize.org."}
    - {value: "ACM A.M. Turing Award 2018 (with Bengio and LeCun) for deep learning", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S5, locator: "Honours and awards"}], how_known: "Wikipedia EN."}
  major_works: []
  honours:
    - {value: "Nobel Prize in Physics", year: 2024, certainty: 0.7, cites: [{source: S1, locator: "heading"}], how_known: "NobelPrize.org."}
    - {value: "ACM A.M. Turing Award", year: 2018, certainty: 0.7, cites: [{source: S5, locator: "Honours and awards"}], how_known: "Wikipedia EN."}
  definition_fit: {value: "clearly meets", rationale: "Foundational work on neural-network learning (S1).", certainty: 0.7, cites: [{source: S1, locator: "Prize motivation"}], how_known: "NobelPrize.org."}

childhood:
  family_religion: {value: "Atheist parents", certainty: 0.7, cites: [{source: S2, locator: "'What personal qualities are important'"}, {source: S4, locator: "atheist family / Christian school"}], how_known: "(interview) Nobel 'my parents who were both atheists' (S2); On Point 'I came from an atheist family' (S4)."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Father Howard Everest Hinton, entomologist", certainty: 0.7, cites: [{source: S5, locator: "Personal life / Father"}, {source: S4, locator: "father was a biologist"}], how_known: "Wikipedia EN; On Point (interview) father as biologist / entomologist."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling:
    - {value: "Christian private school, from age seven to about seventeen or eighteen", stage: "other", years: "1954–", certainty: 0.7, cites: [{source: S2, locator: "'What personal qualities are important'"}, {source: S4, locator: "seven to seventeen or eighteen"}], how_known: "(interview) Nobel and On Point; start year from his age.", run_by: "religious body"}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure:
    - {value: "Weekend insect collecting with entomologist father; many cold-blooded animals kept at home", certainty: 0.5, cites: [{source: S4, locator: "insects / animals"}], how_known: "(interview) On Point."}
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1983–1985", certainty: 0.7, cites: [{source: S1, locator: "Work"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system:
    value: ATHE
    basis: recorded_interview
    certainty: 0.5
    cites: [{source: S2, locator: "'What personal qualities are important'"}, {source: S4, locator: "atheist family / nonsense"}]
    how_known: "(interview) Nobel 2024-12-06 (S2) and On Point 2025-01-10 (S4); both after the span (P20), so 0.5."
    rationale: "Stated non-belief: schoolroom belief in God 'seemed to me it was just obvious nonsense, and it turns out I was right'; 'other people also don't believe in God' (S2). On Point restates the same adult retrospective: atheist family; school belief 'seemed like nonsense'; 'more and more people agreed with me that it was nonsense' (S4). Not mere childhood anecdote — adult affirmation that God-belief is nonsense and that he was right. Alternative AGNOS (no general claim beyond rejecting the schoolroom God). Support corroborated (P48): S2+S4. Certainty stays 0.5 (after span; named alt)."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: ATHE, reason: "Chosen: adult own-voice non-belief (S2, S4); Chomsky/Kahneman ATHE pattern."}
    - {code: AGNOS, reason: "Named alternative: no explicit suspension wording; could be read as rejecting only the schoolroom God."}
  lio_axes:
    A_locus:
      value: 4
      basis: recorded_interview
      certainty: 0.5
      support: corroborated
      cites: [{source: S2, locator: "'What personal qualities are important'"}, {source: S4, locator: "atheist family / nonsense"}]
      how_known: "(interview) Nobel (S2) and On Point (S4); after the span; P20 cap 0.5."
      rationale: "Stated disbelief in God scored as A 4, as Chomsky and Kahneman (P20, P38). Adult affirmation that belief in God is nonsense and that he was right (S2); On Point corroborates (S4). Alternatives BELOW_THRESHOLD (no locus view as such) and 3 (denies only the schoolroom God). Support corroborated (P48): two independent interviews."
      alternatives:
        - {value: BELOW_THRESHOLD, note: "Disbelief without a locus view.", cites: [{source: S2, locator: "'What personal qualities are important'"}, {source: S4, locator: "nonsense"}]}
        - {value: 3, note: "Denies only the schoolroom God.", cites: [{source: S2, locator: "'What personal qualities are important'"}, {source: S4, locator: "nonsense"}]}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist as listed: the Boltzmann machine is called an 'invention' (S1); P33 and the Hassabis precedent. RQ-Z9-1 HOLD (OPEN_DECISIONS): not a scientist as listed, so B stays UNKNOWN and he does not plot. Deepen found no own P16 nature-order statement (lawful order / laws of nature in his words). Backpropagation (1986) remains a training method / algorithm popularisation (S5), not listed here as a lasting theory of natural systems — listing it as such would reopen RQ-Z9-1; not done this pass. Leads only: prize motivation 'discoveries and inventions' (S1); interview 'theory' of Boltzmann machines 'for discovering how the brain worked' (S2). Were a lasting natural-system theory listed, B would be 3 at 0.5 (P35) and he would plot, faded, at A 4 / B 3."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is at least 3 only at 0.5; B_cause UNKNOWN; P10/P4 under the 0.7 bar → BELOW_THRESHOLD. Chart-moving NO (deepen 2026-10-24)."}
  statements:
    - text: "One was my parents who were both atheists sent me to a Christian school, a Christian private school, from the age of seven. Everybody at the school believed in God. The teachers believed in God and the other kids believed in God. It seemed to me it was just obvious nonsense, and it turns out I was right."
      cites: [{source: S2, locator: "'What personal qualities are important'"}]
      date: "2024-12-06"
      context: "Nobel Prize interview, Stockholm; after the span."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
    - text: "So I came from an atheist family. And they sent me to a private Christian school. So when I arrived there at the age of seven, everybody else believed in God. And it seemed like nonsense to me. And as time went by, more and more people agreed with me that it was nonsense."
      cites: [{source: S4, locator: "atheist family / nonsense"}]
      date: "2025-01-10"
      context: "On Point (WBUR) interview with Meghna Chakrabarti; after the span; same school story restated as adult affirmation."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
  changes_over_life: []
  coder_notes: "RQ-Z9-1 HOLD (Z9 audit; Hassabis, Knuth, Tao precedents): Boltzmann machine is an invention (P33); Nobel's 'inspired by the structure of the brain' is not a testable claim about organisms. Deepen: no P16 own-voice nature-order remark found; backpropagation not added as a lasting natural-system theory. A/primary firmed by On Point corroboration (support corroborated) but certainty stays 0.5 (after span). Do not force plot."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: "None (atheist parents)", certainty: 0.7, cites: [{source: S2, locator: "'What personal qualities are important'"}, {source: S4, locator: "atheist family"}], how_known: "(interview)."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1983–1985", certainty: 0.7, cites: [{source: S1, locator: "Work"}], how_known: "Boltzmann machine, 1983–1985 (P29, P30)."}
  age_at_first_lasting_contribution: {value: 36, certainty: 0.7, cites: [{source: S1, locator: "Born; Work"}], how_known: "1983 − 1947 = 36 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: "c. 1954 onward (disbelief at his Christian school from age seven)", certainty: 0.5, cites: [{source: S2, locator: "'What personal qualities are important'"}, {source: S4, locator: "seven to seventeen or eighteen"}], how_known: "(interview)."}
  lio_views_relative_to_major_work: {value: "before major work", certainty: 0.5, cites: [{source: S2, locator: "'What personal qualities are important'"}, {source: S4, locator: "school years"}], how_known: "(interview)."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None in-span; adult interviews after the span affirm the school-formed non-belief."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Statistical learning models (S1).", certainty: 0.5, cites: [{source: S1, locator: "Work"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "University of Toronto", role: "professor", years: "1987–", kind: "university", certainty: 0.7, cites: [{source: S1, locator: "Affiliation"}, {source: S5, locator: "Career"}], how_known: "NobelPrize.org (affiliation at the award); Wikipedia EN (affiliated since 1987)."}
  - {value: "Carnegie Mellon University", role: "faculty", years: "1980s", kind: "university", certainty: 0.5, cites: [{source: S5, locator: "Career / PDP group"}], how_known: "Wikipedia EN; Boltzmann/PDP era."}
collaborators:
  - {value: "John J. Hopfield", relation: "other", note: "co-laureate 2024", certainty: 0.7, cites: [{source: S1, locator: "heading"}], how_known: "NobelPrize.org."}
  - {value: "Terrence J. Sejnowski", relation: "collaborator", note: "Boltzmann machines (Ackley–Hinton–Sejnowski)", certainty: 0.5, cites: [{source: S2, locator: "Terry Sinofsky / prize money"}, {source: S5, locator: "Research"}], how_known: "Nobel interview 'Terry'; Wikipedia EN Sejnowski."}

review:
  roster_status_reason: {value: "Provisional in v8 (F 3).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 171"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Own creed words from interviews long after the span (P20 → 0.5)."
    - "B UNKNOWN under RQ-Z9-1; no P16 nature-order own-voice found this pass."
  open_questions:
    - "In-span own-voice on belief (would lift A/primary toward 0.7 if found)."
    - "Any lasting natural-system theory to list (would reopen RQ-Z9-1 / B); backpropagation kept as method, not listed as theory of brains."
    - "P16 lawful-order own-voice (would score B without scientist status)."

sources:
  - id: S1
    type: tertiary
    kind: "institutional page"
    author: "Nobel Prize Outreach"
    citation: "'Geoffrey Hinton – Facts – 2024.' NobelPrize.org. https://www.nobelprize.org/prizes/physics/2024/hinton/facts/"
    url: "https://www.nobelprize.org/prizes/physics/2024/hinton/facts/"
    accessed: 2026-10-19
    reliability_note: "Official prize facts page."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, timing, lane_b, institutions, collaborators]
  - id: S2
    type: primary
    kind: "other"
    author: "Geoffrey Hinton, interviewed for NobelPrize.org"
    citation: "'Transcript from an interview with Geoffrey Hinton.' NobelPrize.org (recorded 6 December 2024). https://www.nobelprize.org/prizes/physics/2024/hinton/1925103-interview-transcript/"
    url: "https://www.nobelprize.org/prizes/physics/2024/hinton/1925103-interview-transcript/"
    accessed: 2026-10-19
    reliability_note: "Official interview transcript (recorded_interview, P8)."
    source_quality: "primary / own words"
    used_for: [childhood, worldview, heritage, timing, collaborators]
  - id: S3
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [review]
  - id: S4
    type: primary
    kind: "other"
    author: "Geoffrey Hinton, interviewed by Meghna Chakrabarti"
    citation: "'The \\'Godfather of AI\\' says we can\\'t afford to get it wrong.' On Point, WBUR (aired 10 January 2025). https://www.wbur.org/onpoint/2025/01/10/ai-geoffrey-hinton-physics-nobel-prize"
    url: "https://www.wbur.org/onpoint/2025/01/10/ai-geoffrey-hinton-physics-nobel-prize"
    accessed: 2026-10-24
    reliability_note: "Radio interview transcript on WBUR (recorded_interview, P8); own-voice school/atheism restatement."
    source_quality: "newspaper interview"
    used_for: [childhood, worldview, heritage, timing]
  - id: S5
    type: tertiary
    kind: "encyclopedia"
    author: "Wikipedia contributors"
    citation: "'Geoffrey Hinton.' Wikipedia (English). https://en.wikipedia.org/wiki/Geoffrey_Hinton"
    url: "https://en.wikipedia.org/wiki/Geoffrey_Hinton"
    accessed: 2026-10-24
    reliability_note: "Dual bio (P50); not used alone to score creed axes. Tertiary claim 'atheist since childhood' not scored (own voice is S2/S4)."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, institutions, collaborators]
---

## Summary

Geoffrey Hinton (b. 1947), computer scientist [S1][S5]. Deepen D1: ATHE (0.5, interview; corroborated S2+S4); A 4 (0.5, interview; support corroborated); B UNKNOWN (RQ-Z9-1 HOLD; no P16). Not plotted. Chart-moving NO.

## Life and work

London-born British-Canadian; Carnegie Mellon (Boltzmann/PDP era); University of Toronto since 1987 [S1][S5].

## Contribution and impact

Boltzmann machine (invention, 1983–1985); neural-network learning; Nobel Physics 2024; Turing Award 2018 [S1][S5].

## Childhood and education

Atheist parents; Christian private school from age seven; entomologist father [S2][S4][S5].

## Adult working worldview

Belief in God 'obvious nonsense' / 'nonsense'; adult affirmation he was right [S2][S4]. ATHE and A 4 at 0.5 (interview). B UNKNOWN — not a scientist as listed; no P16 nature-order own-voice.

## Heritage (context only)

None religious (atheist parents) [S2][S4].

## Timing

1983–1985, age 36 [S1]. Creed evidence after the span.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data for H1 timing from B (B UNKNOWN).

## Open questions

- In-span own-voice on belief.
- Lasting natural-system theory listing (would reopen RQ-Z9-1).
- P16 lawful-order own-voice for non-scientist B.

## Research log

- 2026-10-19: Read NobelPrize.org facts and interview transcript.
- 2026-10-24: Deepen D1 — On Point WBUR 2025-01-10 transcript (S4); Wikipedia EN dual bio (S5). Searched for further own-voice God/religion and P16 nature-order remarks; no solid P16 found. Taxi-driver "I don't actually think there's a God" remains LinkedIn paraphrase of an unnamed talk — not used. Nobel podcast host paraphrase ("fake news" / "deluded") is third-party — not used to score. RQ-Z9-1 held. Local commit person file only.
