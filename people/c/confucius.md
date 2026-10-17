---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch O)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-17
  last_updated: 2026-10-17
  change_log:
    - {date: 2026-10-17, by: "Grok Bot", summary: "Record created (stage 3 batch O, order P32: F 4, rank 90). Basics from Britannica (Annping Chin, signed; body only) and SEP 'Confucius' (Csikszentmihalyi, 2024). He wrote nothing that survives as his; the Analects was compiled by first- and second-generation disciples (SEP), so its sayings are reported speech (P42, §7) and cannot score alone. primary_system BELOW_THRESHOLD (CONFUC leading candidate); A BELOW_THRESHOLD (Heaven sayings, reported); B UNKNOWN; mid_basin UNKNOWN (P19). Not plotted. Draft, not reviewed."}
    - {date: 2026-10-17, by: "Grok Bot", summary: "Batch O audit fix (#20): statement dated to the span 498–484 BCE in its context, noted as undated; the placeholder -492 removed and the date field left out (the schema's date field takes one year, not a span). v8's ruling on RQ O1 (on the auditor's advice): the Analects stays reported speech under P42 (recorded in OPEN_DECISIONS). Values unchanged."}

identity:
  id: confucius
  display_name: "Confucius"
  roster:
    canonical_name: "Confucius"
    rank: 90
    F: 4
    models: [Claude, DeepSeek, Gemini, Grok]
    band: "core (3–4)"
    status: core
    field: philosophy
    field_bucket: philosophy
  full_name: {value: "Confucius", certainty: 0.7, cites: [{source: S2, locator: "opening"}], how_known: "SEP: 'a Latinized combination of the surname Kong 孔 with an honorific suffix \"Master\" (fuzi 夫子)'. His personal name is given only in Britannica's Quick Facts, which are not cited."}
  native_name: {value: "Kong fuzi (孔夫子)", certainty: 0.5, cites: [{source: S2, locator: "opening"}], how_known: "Coder's combination of the surname and honorific SEP gives; SEP also writes Kongzi 孔子 in a title."}
  aliases: []

basics:
  birth:
    date: {value: "-551", calendar: julian, certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Britannica gives 551 BCE; SEP gives 'trad. 551–479 BCE' (traditional dates), so 0.5. Proleptic Julian."}
    place: {value: "Qufu, state of Lu", modern_name: "Qufu, Shandong, China", polity_then: "State of Lu (Zhou dynasty)", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "-479", calendar: julian, certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Britannica; traditional date (S2)."}
    place: {value: "Lu", modern_name: "Shandong, China", polity_then: "State of Lu (Zhou dynasty)", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: UNKNOWN, how_known: "His teaching is undated in the body; the Analects was compiled after his death (P39)."}
  era_bucket: {value: UNKNOWN, how_known: "No dated lasting work (P39), and his adult years (c. 530s–479 BCE) straddle the -500 edge, so no single bucket holds them all."}
  region_of_birth: {value: "East Asia", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "China (P3)."}
  region_of_work: {value: "East Asia", certainty: 0.7, cites: [{source: S1, locator: "journey paragraph"}], how_known: "Lu, Wei, Song, Chen, Cai."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Classical Chinese"], certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  occupations: {value: ["teacher", "philosopher", "political theorist", "official in Lu"], certainty: 0.7, cites: [{source: S1, locator: "opening; Jisun paragraph"}], how_known: "Britannica."}

contribution:
  fields: {value: ["ethics", "political philosophy", "education"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Teaching on virtue, ritual and government, transmitted in the Analects", year: UNKNOWN, kind: "body of work", lasting: "'whose ideas have profoundly influenced the civilizations of China and other East Asian countries' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Analects sources section"}], how_known: "Britannica; the text was compiled by disciples (S2)."}
  evidence_of_impact:
    - {value: "Ideas 'profoundly influenced the civilizations of China and other East Asian countries'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father Shu-liang He, a warrior and district steward in Lu, already old at his birth; he died soon after it, leaving his young widow to fend for herself", role: father, certainty: 0.7, cites: [{source: S1, locator: "family paragraph"}], how_known: "Britannica."}
  household_circumstances: {value: "The Kongs of Lu were common gentlemen (shi), 'just a notch higher than the common folk'; he later called himself 'poor and from a lowly station' (Analects 9:6)", certainty: 0.7, cites: [{source: S1, locator: "family paragraph; Analects 9:6"}], how_known: "Britannica."}
  schooling: []
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["Old Chinese"], certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  notable_events:
    - {value: "Death of his father soon after his birth", year: UNKNOWN, certainty: 0.7, cites: [{source: S1, locator: "family paragraph"}], how_known: "Britannica."}

worldview:
  unit: "adult working worldview"
  working_years: {value: UNKNOWN, how_known: "Equals timing.major_work_period (UNKNOWN, P39)."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing in his own hand."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "Leading candidate CONFUC (the tradition named after him), but everything attributed to him is reported speech: SEP gives the conventional account that the Analects was 'compiled by first and second generation disciples of Confucius', notes that some of its quotations appear 'in the mouths of other historical figures', and that the text was fixed only in the second century BCE (S2). Reported speech cannot score alone (§7, P42)."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CONFUC, reason: "Founder figure; nothing attributable in his own words (P42)."}
    - {code: CHNFOLK, reason: "Heaven and ancestor rites of his time (S2); context only."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "Reported speech only (§7, P42). The Analects has him say 'Heaven has given me this power—this virtue. What can Huan Tui do to me!' (7:23) and 'Heaven has not destroyed this culture' (9:5) (S1), and 'Heaven has forsaken me!' (11.9) (S2): Heaven as an agent that backs or abandons a person, which would lean to A 0–1, but the words are the disciples' record."}
    B_cause: {value: UNKNOWN, how_known: "Nothing read on law and exception in nature; the Analects passages read concern Heaven's backing of persons, not nature's order (P16)."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read on reward or punishment; SEP says early discussions stressed benefits of ritual 'beyond the propitiation of spirits, rewards from the ancestors' (S2), a lead only."}
    D_authority: {value: UNKNOWN, how_known: "Nothing read."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7)."}
  mid_basin: {value: UNKNOWN, how_known: "B is UNKNOWN (P19)."}
  statements:
    - text: "Heaven has given me this power—this virtue. What can Huan Tui do to me!"
      cites: [{source: S1, locator: "Huan Tui and Kuang paragraph (Analects 7:23)"}]
      context: "Analects 7:23, on Huan Tui's plan to ambush him during his years of travel, 498–484 BCE (S1). Undated: S1 gives no year for the event, only the span of the travels, so the date field is left out (the schema's date takes a single year, not a span)."
      axes: [A_locus]
      kind: "reported speech"
      verified_against: "secondary quotation"
      verified_on: 2026-10-17
      note: "Recorded by disciples (S2); reported speech (§7, P42). Britannica calls the Analects 'the most reliable source on Confucius's life'."
  changes_over_life: []
  coder_notes: "Coder's call. Treated like Hippocrates under P42: the doctrine is known only through a later compilation, so nothing scores. v8's ruling on RQ O1 (on the auditor's advice) confirms the Analects stays reported speech under P42. The Analects 7.21 line on not discussing prodigies and spirits is the lead for B but was not read in a cited source."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Kong family of Lu, descended from the Kongs of Song", certainty: 0.5, cites: [{source: S1, locator: "family paragraph ('According to some reports')"}], how_known: "Britannica, hedged."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: UNKNOWN, how_known: "No dated lasting contribution (P39)."}
  age_at_first_lasting_contribution: {value: UNKNOWN, how_known: "No dated lasting contribution (P39)."}
  first_evidence_of_lio_type_views: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S2, locator: "Analects sources section"}], how_known: "Nothing attributable (P42)."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S2, locator: "Analects sources section"}], how_known: "As above."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Nothing attributable."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Not read for this.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Not read."}
  circle_present: {value: "unclear", rationale: "Reported speech only.", certainty: 0.5, cites: [{source: S2, locator: "Analects sources section"}], how_known: "Coder's reading."}
  reading: "Heaven as moral backer, in reported speech."
  notes: ""

institutions:
  - {value: "Jisun clan (hereditary chief counselors of Lu)", role: "keeper of granaries and other modest posts", years: UNKNOWN, kind: employer, certainty: 0.7, cites: [{source: S1, locator: "Jisun paragraph"}], how_known: "Britannica."}
collaborators:
  - {value: "Zigong", relation: "student or assistant", note: "early disciple", certainty: 0.7, cites: [{source: S1, locator: "disciples paragraph"}], how_known: "Britannica."}
  - {value: "Zilu", relation: "student or assistant", note: "early disciple", certainty: 0.7, cites: [{source: S1, locator: "disciples paragraph"}], how_known: "Britannica."}
  - {value: "Yan Hui", relation: "student or assistant", note: "favourite disciple", certainty: 0.7, cites: [{source: S1, locator: "disciples paragraph"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 90"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Traditional life dates; nothing in his own hand."
  open_questions:
    - "Settled (v8's ruling on RQ O1 of the batch O audit, on the auditor's advice; OPEN_DECISIONS P42): the Analects, a disciples' record of his sayings, stays reported speech; P42's scholarly-agreement clause covers who wrote a text, not a record of sayings."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Annping Chin"
    citation: "Chin, Annping. \"Confucius.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Confucius. Read in Wayback snapshot 20260919161320."
    url: "https://www.britannica.com/biography/Confucius"
    accessed: 2026-10-17
    reliability_note: "Signed article. Body only; Top Questions not cited."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, institutions, collaborators]
  - id: S2
    type: tertiary
    kind: encyclopedia
    author: "Mark Csikszentmihalyi"
    citation: "Csikszentmihalyi, Mark. \"Confucius.\" Stanford Encyclopedia of Philosophy (substantive revision 2 May 2024). https://plato.stanford.edu/entries/confucius/"
    url: "https://plato.stanford.edu/entries/confucius/"
    accessed: 2026-10-17
    reliability_note: "Signed SEP entry, read directly."
    used_for: [identity, basics, contribution, worldview, timing, lane_b]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-17
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Confucius

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Confucius (trad. 551–479 BCE), Chinese teacher and political theorist [S1; S2]. Draft: primary_system BELOW_THRESHOLD (CONFUC candidate); A BELOW_THRESHOLD (reported speech); B UNKNOWN; mid_basin UNKNOWN. Not plotted.

## Life and work

Lu; fourteen years of travel from 498 BCE; returned 484 BCE [S1].

## Contribution and impact

Teaching transmitted in the Analects [S1; S2].

## Childhood and education

Father Shu-liang He died soon after his birth [S1].

## Adult working worldview

Only reported speech: Heaven as his backer [S1; S2].

## Heritage (context only)

Kong family of Lu [S1].

## Timing

Undated (P39).

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Reported speech only [S2].

## Open questions

- P42 status of the Analects.

## Research log

- 2026-10-17: Read Britannica (Chin, Wayback 20260919161320) and SEP (Csikszentmihalyi) directly.
