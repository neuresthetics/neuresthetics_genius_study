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
    - {date: 2026-10-18, by: "Grok Bot", summary: "Record created (stage 3 batch P, order P32: F 4, rank 96). Basics from Britannica (Britannica Editors, unsigned; body only). Worldview from the Zürau aphorisms (notebooks of 1917–18), published by Max Brod and H. J. Schoeps as 'Betrachtungen über Sünde, Leid, Hoffnung und den wahren Weg' in Beim Bau der Chinesischen Mauer (Berlin: Kiepenheuer, 1931), read in the proofread Wikisource transcription. Not a scientist (P30). primary_system BELOW_THRESHOLD; A BELOW_THRESHOLD (alt 3); B BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Not plotted. Draft, not reviewed."}
    - {date: 2026-10-18, by: "Grok Bot", summary: "Batch P audit fixes (gs_08be43b_P run 1: 39 hold, 6 weaken). Page cites corrected from each Wikisource page's own source: no. 50 on p. 234 (KA4), no. 54 on p. 235 (KA5), and the aphorism printed as '70. 71' on pp. 238–239 (KA6, also in the A_locus cites). Ruling P3 (v8's pick on the auditor's advice): A and B stay BELOW_THRESHOLD. Values unchanged; not plotted."}

identity:
  id: kafka-franz
  display_name: "Franz Kafka"
  roster:
    canonical_name: "Franz Kafka"
    rank: 96
    F: 4
    models: [Claude, Gemini, GPT, Grok]
    band: "core (3–4)"
    status: core
    field: literature
    field_bucket: literature
  full_name: {value: "Franz Kafka", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  native_name: {value: "Franz Kafka", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "German; same spelling."}
  aliases:
    - {name: "Franz-Kafka", kind: "roster alias"}
    - {name: "Kafka-Franz", kind: "roster alias"}

basics:
  birth:
    date: {value: "1883-07-03", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Prague, Bohemia, Austria-Hungary", modern_name: "Prague, Czechia", polity_then: "Austria-Hungary", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "1924-06-03", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Kierling, near Vienna, Austria", modern_name: "Kierling, Austria", polity_then: "Austria", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1913, certainty: 0.7, cites: [{source: S1, locator: "father paragraph"}], how_known: "Das Urteil (1913; The Judgment), the earliest dated work S1 names (P13, P17)."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "From 1913 (P2); every listed year gives the same bucket."}
  region_of_birth: {value: "Eastern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Czechia (P3)."}
  region_of_work: {value: "Eastern Europe", certainty: 0.7, cites: [{source: S1, locator: "double life paragraph"}], how_known: "Prague; Berlin only in 1923–24."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [German], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "'a German-language writer' (S1)."}
  occupations: {value: ["writer", "insurance official", "lawyer by training"], certainty: 0.7, cites: [{source: S1, locator: "double life paragraph"}], how_known: "Britannica."}

contribution:
  fields: {value: ["fiction"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Das Urteil (The Judgment)", year: 1913, kind: work, lasting: "'reflected directly' the father conflict central to his work (S1)", certainty: 0.5, cites: [{source: S1, locator: "father paragraph"}], how_known: "Britannica; lasting status is the coder's reading."}
    - {value: "Die Verwandlung (The Metamorphosis)", year: 1915, kind: work, lasting: "named in the opening as one of the works that 'express the anxieties and alienation felt by many in 20th-century Europe and North America' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    - {value: "Der Prozess (The Trial)", year: 1925, kind: work, lasting: "named in the opening with The Metamorphosis (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica; published after his death (1924)."}
    - {value: "Das Schloss (The Castle)", year: 1926, kind: work, lasting: "one of the novels that portray 'a man's desperate struggle with an overwhelming power' (S1)", certainty: 0.5, cites: [{source: S1, locator: "father paragraph"}], how_known: "Britannica; posthumous; lasting status the coder's reading."}
  evidence_of_impact:
    - {value: "Works 'express the anxieties and alienation felt by many in 20th-century Europe and North America'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Jewish; his father 'held only perfunctorily to the religious practices and social formalities of the Jewish community'", certainty: 0.7, cites: [{source: S1, locator: "father paragraph"}], how_known: "Britannica."}
  family_religious_practice: {value: "Perfunctory (father)", certainty: 0.7, cites: [{source: S1, locator: "father paragraph"}], how_known: "Britannica."}
  parents_and_household:
    - {value: "Hermann Kafka, merchant", role: father, certainty: 0.7, cites: [{source: S1, locator: "Life paragraph"}], how_known: "Britannica."}
    - {value: "Julie Löwy", role: mother, certainty: 0.7, cites: [{source: S1, locator: "Life paragraph"}], how_known: "Britannica."}
  household_circumstances: {value: "Prosperous middle-class Jewish family; eldest surviving child", certainty: 0.7, cites: [{source: S1, locator: "Life paragraph"}], how_known: "Britannica."}
  schooling:
    - {value: "Altstädter Staatsgymnasium, Prague", stage: "grammar or secondary school", years: UNKNOWN, certainty: 0.7, cites: [{source: S1, locator: "father paragraph"}], how_known: "Britannica."}
    - {value: "University of Prague (doctorate in law, 1906)", stage: university, years: "–1906", certainty: 0.7, cites: [{source: S1, locator: "double life paragraph"}], how_known: "Britannica."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [German], certainty: 0.7, cites: [{source: S1, locator: "father paragraph"}], how_known: "'German in both language and culture' (S1)."}
  notable_events:
    - {value: "As an adolescent declared himself a socialist and an atheist", year: UNKNOWN, certainty: 0.7, cites: [{source: S1, locator: "father paragraph"}], how_known: "Britannica. Adolescent evidence, off-point for the working years (P29)."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1913–1924", certainty: 0.7, cites: [{source: S1, locator: "opening; father paragraph"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing read."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "The aphorisms read are private and figurative: belief in a personal God is 'one of the possible expressions' of a hidden trust in 'something indestructible' in oneself (no. 50), and 'There is nothing but a spiritual world' (no. 54). They fit no code clearly; candidates JUDA (heritage and later sympathy for Zionism, S1), EXIST (lead only). Britannica's paraphrase of his isolation 'with God, or, as he put it, with true indestructible Being' is a lead, not his wording."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: JUDA, reason: "Heritage; 'marked interest and sympathy for a socialized Zionism' (S1), which is political, not doctrinal."}
    - {code: EXIST, reason: "Lead only; no statement read."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, cites: [{source: S2, locator: "no. 50 (p. 234); no. 70. 71 (pp. 238–239)"}], how_known: "Private aphorism, figurative: 'Der Mensch kann nicht leben ohne ein dauerndes Vertrauen zu etwas Unzerstörbarem in sich ... Eine der Ausdrucksmöglichkeiten dieses Verborgenbleibens ist der Glaube an einen persönlichen Gott' (no. 50; a person cannot live without lasting trust in something indestructible in himself ... one way this stays hidden is belief in a personal God), and 'Das Unzerstörbare ist eines; jeder einzelne Mensch ist es und gleichzeitig ist es allen gemeinsam' (no. '70. 71'; the indestructible is one; each person is it and it is common to all). That places what is ultimate within persons and treats a personal God as one expression of it, which leans to A 3, but no view on God's existence or locus is stated outright. Named alternative: 3. Translation the coder's. Ruling P3 (v8's pick on the auditor's advice): stays BELOW_THRESHOLD, not 0.5 as for van Gogh, whose premise (God as author) was asserted in his own voice; no. 50 describes what belief in a personal God expresses without asserting or denying God, and no. '70. 71' never identifies the indestructible with God (that identification is only in Britannica's paraphrase, a lead). Re-open (alt 3 at 0.5) only if the diaries equate God with the indestructible in his own words."}
    B_cause: {value: BELOW_THRESHOLD, cites: [{source: S2, locator: "no. 54"}], how_known: "Not a scientist (P30). The one remark on nature read, 'Es gibt nichts anderes als eine geistige Welt; was wir sinnliche Welt nennen, ist das Böse in der geistigen' (no. 54; there is nothing but a spiritual world; what we call the sensory world is the evil in the spiritual one), is about the status of the sensible world, not its law or exceptions, so it bears on B only indirectly (P16, P19)."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read; no. 40 ('Nur unser Zeitbegriff läßt uns das Jüngste Gericht so nennen, eigentlich ist es ein Standrecht', S2) is a lead."}
    D_authority: {value: UNKNOWN, how_known: "Nothing read."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A and B are both BELOW_THRESHOLD (P19)."}
  statements:
    - text: "Der Mensch kann nicht leben ohne ein dauerndes Vertrauen zu etwas Unzerstörbarem in sich, wobei sowohl das Unzerstörbare als auch das Vertrauen ihm dauernd verborgen bleiben können. Eine der Ausdrucksmöglichkeiten dieses Verborgenbleibens ist der Glaube an einen persönlichen Gott."
      cites: [{source: S2, locator: "no. 50 (p. 234)"}]
      context: "Zürau notebooks, 1917–18 (inside the working years); published posthumously in 1931 (S2). Undated within that span, so no single year is given."
      axes: [A_locus]
      kind: "notebook or diary"
      verified_against: "secondary quotation"
      verified_on: 2026-10-18
      note: "Wikisource transcription of the 1931 edition, proofread twice against page scans; web copy, cap 0.7. Page from the Wikisource page markers."
    - text: "Es gibt nichts anderes als eine geistige Welt; was wir sinnliche Welt nennen, ist das Böse in der geistigen, und was wir böse nennen, ist nur eine Notwendigkeit eines Augenblicks unserer ewigen Entwicklung."
      cites: [{source: S2, locator: "no. 54 (p. 235)"}]
      context: "Same notebooks."
      axes: [B_cause]
      kind: "notebook or diary"
      verified_against: "secondary quotation"
      verified_on: 2026-10-18
      note: "As above."
    - text: "Das Unzerstörbare ist eines; jeder einzelne Mensch ist es und gleichzeitig ist es allen gemeinsam, daher die beispiellos untrennbare Verbindung der Menschen."
      cites: [{source: S2, locator: "no. 70. 71 (pp. 238–239)"}]
      context: "Same notebooks."
      axes: [A_locus]
      kind: "notebook or diary"
      verified_against: "secondary quotation"
      verified_on: 2026-10-18
      note: "As above."
  changes_over_life: []
  coder_notes: "Coder's call. The aphorisms are figurative and were never published by him; A and B are left BELOW_THRESHOLD rather than scored. The adolescent atheism (S1) is before the working years (P29). Leads: the diaries and the Zürau notebooks in the critical edition; Brod's biography (his religious reading of Kafka is contested). The span ends at his death in 1924 (P30), although The Trial and The Castle appeared in 1925–26."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Jewish, German-speaking, of Prague", certainty: 0.7, cites: [{source: S1, locator: "father paragraph"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Jewish", certainty: 0.7, cites: [{source: S1, locator: "Life paragraph"}], how_known: "Britannica."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1913–1924", certainty: 0.7, cites: [{source: S1, locator: "opening; father paragraph"}], how_known: "From the first listed lasting contribution (1913) to his death (1924): the span never runs past death (P30), though two listed works appeared posthumously."}
  age_at_first_lasting_contribution: {value: 30, certainty: 0.7, cites: [{source: S1, locator: "opening; father paragraph"}], how_known: "1913 − 1883 = 30 (P30)."}
  first_evidence_of_lio_type_views: {value: "1917–18: Zürau aphorisms on the indestructible and a personal God", year: 1917, certainty: 0.5, cites: [{source: S2, locator: "no. 50"}], how_known: "Earlier diaries not read (P30 #7); the start year of the notebooks."}
  lio_views_relative_to_major_work: {value: "during major work", rationale: "1917–18 falls inside 1913–1924.", certainty: 0.5, cites: [{source: S2, locator: "no. 50"}], how_known: "Dates of what was read."}
  worldview_during_major_work: {value: "Figurative: trust in an 'indestructible' within persons; the sensible world as evil within the spiritual (1917–18)", certainty: 0.5, cites: [{source: S2, locator: "nos. 50, 54, 71"}], how_known: "His notebooks."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Not a geometric style.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Not read."}
  circle_present: {value: "unclear", rationale: "The indestructible within persons; figurative.", certainty: 0.5, cites: [{source: S2, locator: "no. 50; no. 70. 71"}], how_known: "Coder's reading."}
  reading: "An indestructible core in each person; the personal God as one of its expressions."
  notes: ""

institutions:
  - {value: "Assicurazioni Generali (Prague)", role: "insurance clerk", years: "1907–1908", kind: commercial, certainty: 0.5, cites: [{source: S1, locator: "double life paragraph"}], how_known: "Britannica (1907; left for the Institute in 1908)."}
  - {value: "Workers' Accident Insurance Institute for the Kingdom of Bohemia", role: "official", years: "1908–1922", kind: "government or state body", certainty: 0.7, cites: [{source: S1, locator: "double life paragraph"}], how_known: "Britannica ('seminationalized')."}
collaborators:
  - {value: "Max Brod", relation: other, note: "closest friend, literary executor and biographer", certainty: 0.7, cites: [{source: S1, locator: "double life paragraph"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 96"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Britannica article is unsigned (Britannica Editors); read live (Wayback rate-limited)."
    - "Worldview rests on figurative private aphorisms."
  open_questions:
    - "Read the diaries (1910–23) for statements on God and nature in his own voice."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "Britannica Editors. \"Franz Kafka.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Franz-Kafka. Read live 2026-10-18 (the Wayback Machine was rate-limiting)."
    url: "https://www.britannica.com/biography/Franz-Kafka"
    accessed: 2026-10-18
    reliability_note: "Unsigned article. Body only; the Top Questions and Quick Facts are not cited."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Franz Kafka"
    citation: "Kafka, Franz. \"Betrachtungen über Sünde, Leid, Hoffnung und den wahren Weg.\" In Beim Bau der Chinesischen Mauer, ed. Max Brod and Hans Joachim Schoeps (Berlin: Gustav Kiepenheuer, 1931). Read in the Wikisource transcription: https://de.wikisource.org/wiki/Betrachtungen_%C3%BCber_S%C3%BCnde,_Leid,_Hoffnung_und_den_wahren_Weg"
    url: "https://de.wikisource.org/wiki/Betrachtungen_%C3%BCber_S%C3%BCnde,_Leid,_Hoffnung_und_den_wahren_Weg"
    accessed: 2026-10-18
    reliability_note: "Volunteer transcription of the 1931 edition, marked as proofread twice against the page scans; treated as a web copy (cap 0.7)."
    used_for: [worldview, timing, lane_b]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-18
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Franz Kafka

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Franz Kafka (1883–1924), German-language writer of Prague [S1]. Draft: primary_system BELOW_THRESHOLD; A BELOW_THRESHOLD (alt 3); B BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Not plotted.

## Life and work

Law doctorate 1906; insurance official 1907–1922; died 1924 [S1].

## Contribution and impact

Das Urteil (1913), Die Verwandlung (1915), Der Prozess (1925), Das Schloss (1926) [S1].

## Childhood and education

Prosperous Jewish family; Altstädter Staatsgymnasium; adolescent atheism [S1].

## Adult working worldview

Zürau aphorisms on the indestructible and a personal God [S2, nos. 50 (p. 234), 54 (p. 235), 70. 71 (pp. 238–239)].

## Heritage (context only)

Jewish, German-speaking [S1].

## Timing

First lasting contribution 1913, at 30 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Figurative [S2].

## Open questions

- Diaries.

## Research log

- 2026-10-18: Read Britannica (live) and the Wikisource transcription of the 1931 aphorisms directly.
