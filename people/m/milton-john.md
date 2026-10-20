---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA3)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Correction found while coding AA4: region_of_birth and region_of_work are Northern Europe, not Western Europe; the United Kingdom is M49 Northern Europe (P3, data/reference/regions.csv)."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA3, order P32: F 3, rank 191). Source: Britannica, signed by Albert C. Labriola (scholars edition, read in full). Lasting work: 'Lycidas' (published 1638; 'often considered the most outstanding example of the genre') and Paradise Lost ('widely regarded as the greatest epic poem in English', first published 1667); span 1638–1667 by publication (P30 #1), age 30. Own words: the opening invocation of Paradise Lost, Book 1, in the poet's own voice (not a character's, P42 addendum), read in the Dartmouth John Milton Reading Room (ed. Thomas H. Luxon): 'I may assert Eternal Providence, / And justifie the wayes of God to men'; within the span (1667). primary_system CHRIST 0.7 (written_profession), alt none at 0.7 (his anti-trinitarian leanings, per Labriola, stay within Christianity); A 1 at 0.5 (a creator Spirit who 'from the first / Wast present' and brooded on the Abyss, and an 'Eternal Providence': God beyond and acting on the world; poetic and indirect), alt 0; not a scientist, B UNKNOWN; C, D, E UNKNOWN; mid_basin UNKNOWN (A 1 at 0.5 and B UNKNOWN). Not plotted (B UNKNOWN). Draft, not reviewed."}

identity:
  id: milton-john
  display_name: "John Milton"
  roster:
    canonical_name: "John Milton"
    rank: 191
    F: 3
    models: [Claude, GPT, Grok]
    band: "core (3–4)"
    status: "core"
    field: "literature"
    field_bucket: "literature"
  full_name: {value: "John Milton", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  native_name: {value: "John Milton", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  aliases:
    - {name: "John-Milton", kind: "roster alias"}

basics:
  birth:
    date: {value: "1608-12-09", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
    place: {value: "London (Bread Street)", modern_name: "London, United Kingdom", polity_then: "Kingdom of England", certainty: 0.7, cites: [{source: S1, locator: "Introduction; Travel abroad"}], how_known: "Britannica."}
  death:
    date: {value: "1674-11-08", certainty: 0.5, cites: [{source: S1, locator: "Introduction; later years"}], how_known: "Britannica: 'November 8?, 1674'; 'likely died in London on November 8'."}
    place: {value: "London", modern_name: "London, United Kingdom", polity_then: "Kingdom of England", certainty: 0.5, cites: [{source: S1, locator: "later years"}], how_known: "Britannica: 'London?'."}
  first_lasting_contribution_year: {value: 1638, certainty: 0.7, cites: [{source: S1, locator: "Comus and Lycidas"}], how_known: "'Lycidas', 'Published in 1638 in Justa Edouardo King Naufrago' (S1); publication (P30 #1)."}
  era_bucket: {value: "1600 to 1749", certainty: 1.0, cites: [{source: S1, locator: "Comus and Lycidas; Paradise Lost"}], how_known: "1638–1667 (P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "United Kingdom (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "London."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English", "Latin"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
  occupations: {value: ["poet", "pamphleteer", "historian", "civil servant"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}

contribution:
  fields: {value: ["poetry", "political and religious prose"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Lycidas", year: 1638, kind: "work", lasting: "'often considered the most outstanding example of the genre'; with Comus, 'major literary achievements' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Comus and Lycidas"}], how_known: "Britannica; published 1638."}
    - {value: "Paradise Lost", year: 1667, kind: "work", lasting: "'widely regarded as the greatest epic poem in English' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Introduction; Paradise Lost"}], how_known: "Britannica; first published in 10 books, 1667."}
  evidence_of_impact:
    - {value: "'Considered the most significant English author after William Shakespeare'; influence on the American and French revolutions", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  major_works:
    - {value: "Areopagitica", year: 1644, kind: "other", certainty: 0.7, cites: [{source: S1, locator: "Tracts on education and free expression"}], how_known: "Britannica: 'The most renowned tract by Milton'."}
    - {value: "Paradise Regained and Samson Agonistes", year: 1671, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "Paradise Regained"}], how_known: "Britannica: published in one volume, 1671."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "The most significant English author after Shakespeare (S1).", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Father a scrivener and composer, disinherited by a Roman Catholic grandfather for reading an English (Protestant) Bible", role: "family", certainty: 0.7, cites: [{source: S1, locator: "Early life and education"}], how_known: "Britannica."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling:
    - {value: "St Paul's School; Christ's College, Cambridge (BA 1629, MA 1632)", certainty: 0.7, cites: [{source: S1, locator: "Early life and education"}], how_known: "Britannica."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1638–1667", certainty: 0.7, cites: [{source: S1, locator: "Comus and Lycidas; Paradise Lost"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: 
    value: CHRIST
    basis: written_profession
    certainty: 0.7
    cites: [{source: S2, locator: "Book 1, lines 17–26"}]
    how_known: "His own epic voice in the invocation of Paradise Lost (1667, within the span), read in a scholarly edition; the poet speaks for himself, not through a character (P42 addendum). Labriola's account of his theology agrees (S1)."
    rationale: "He prays to the Spirit who 'from the first / Wast present' to help him 'assert Eternal Providence, / And justifie the wayes of God to men' (S2); Labriola: 'the paramount importance of Scripture as a guide in matters of faith' (S1). His tendency 'to subordinate the Son to the Father' (S1, on De Doctrina Christiana, whose authorship is disputed) is a variant within CHRIST, not an alternative system."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Coded at 0.7: the Paradise Lost invocation."}
  lio_axes:
    A_locus: 
      value: 1
      basis: written_profession
      certainty: 0.5
      cites: [{source: S2, locator: "Book 1, lines 17–26"}]
      how_known: "His own verse, within the span; poetic and indirect, so 0.5."
      rationale: "A Spirit present 'from the first' who brooded on 'the vast Abyss / And mad'st it pregnant', and an 'Eternal Providence' (S2): a creator distinct from and acting on the world, 1. Alternative 0: providence read as a God wholly above the world."
      alternatives:
        - {value: 0, note: "Providence as wholly transcendent rule (S2).", cites: [{source: S2, locator: "Book 1, line 25"}]}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30); no statement on nature read."}
    C_ledger: {value: UNKNOWN, how_known: "Lead: Lycidas's St Peter 'will smite' the corrupt clergy 'in an act of retributive justice' (S1, Labriola's reading); not scored."}
    D_authority: {value: UNKNOWN, how_known: "Lead: 'the primacy of Scripture and ... the conscience of each believer as the guide to interpretation' (S1); not scored."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is 1 only at 0.5 and B_cause is UNKNOWN, so the P4 test cannot be completed."}
  statements:
    - text: "And chiefly Thou O Spirit, that dost prefer / Before all Temples th' upright heart and pure, / Instruct me, for Thou know'st; Thou from the first / Wast present, and with mighty wings outspread / Dove-like satst brooding on the vast Abyss / And mad'st it pregnant: What in me is dark / Illumin, what is low raise and support; / That to the highth of this great Argument / I may assert Eternal Providence, / And justifie the wayes of God to men."
      cites: [{source: S2, locator: "Book 1, lines 17–26"}]
      date: "1667"
      context: "Paradise Lost, Book 1, opening invocation; first published 1667 (the edition follows the 1674 text, the same lines)."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-19
      note: "The John Milton Reading Room, ed. Thomas H. Luxon (Dartmouth); spelling as there."
  changes_over_life: []
  coder_notes: "Read De Doctrina Christiana (authorship disputed: Hunter 1998) only as a lead; Areopagitica (1644, in span) and the antiprelatical tracts for D; Paradise Lost Book 3 for providence and C."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: "Protestant (father disinherited for reading an English Bible)", certainty: 0.7, cites: [{source: S1, locator: "Early life and education"}], how_known: "Britannica."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1638–1667", certainty: 0.7, cites: [{source: S1, locator: "Comus and Lycidas; Paradise Lost"}], how_known: "From Lycidas (1638) to Paradise Lost (1667), the listed lasting works (P29, P30 #1)."}
  age_at_first_lasting_contribution: {value: 30, certainty: 0.7, cites: [{source: S1, locator: "Introduction; Comus and Lycidas"}], how_known: "1638 − 1608 = 30 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Epic and polemic, not geometric argument (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "Council of State of the Commonwealth", role: "secretary for foreign tongues (Latin secretary)", years: "1649–1660", kind: "government or state body", certainty: 0.5, cites: [{source: S1, locator: "Antimonarchical tracts"}], how_known: "Britannica; end year the Restoration (coder's reading)."}
collaborators:
  - {value: "Andrew Marvell", relation: "collaborator", note: "assisted him as Latin secretary", certainty: 0.7, cites: [{source: S1, locator: "Fame and reputation"}], how_known: "Britannica."}
  - {value: "Thomas Young", relation: "teacher", note: "Presbyterian tutor", certainty: 0.7, cites: [{source: S1, locator: "Early life and education"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 191"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Scored lines are verse; the speaker is the poet (P42 addendum)."
  open_questions:
    - "Book 3 on providence; Areopagitica for D."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Albert C. Labriola"
    citation: "Labriola, Albert C. 'John Milton.' Encyclopaedia Britannica (scholars edition). https://kids.britannica.com/scholars/article/John-Milton/108731"
    url: "https://kids.britannica.com/scholars/article/John-Milton/108731"
    accessed: 2026-10-19
    reliability_note: "Signed article, read in full."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, institutions, collaborators]
  - id: S2
    type: primary
    kind: "scholarly edition"
    author: "John Milton (ed. Thomas H. Luxon)"
    citation: "Milton, John. Paradise Lost, Book 1 (1667; 1674 text). The John Milton Reading Room, ed. Thomas H. Luxon, Dartmouth College. https://milton.host.dartmouth.edu/reading_room/pl/book_1/text.shtml"
    url: "https://milton.host.dartmouth.edu/reading_room/pl/book_1/text.shtml"
    accessed: 2026-10-19
    reliability_note: "Edited scholarly online text; Book 1 opening read."
    used_for: [worldview]
  - id: S3
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

John Milton (1608–1674), poet and pamphleteer [S1]. Draft: CHRIST (0.7); A 1 at 0.5; B UNKNOWN. Not plotted.

## Life and work

London; Cambridge; Italy [S1].

## Contribution and impact

Lycidas (1638); Paradise Lost (1667) [S1].

## Childhood and education

St Paul's; Cambridge [S1].

## Adult working worldview

'Justifie the wayes of God to men' (1667) [S2].

## Heritage (context only)

Protestant family [S1].

## Timing

1638–1667, age 30 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Book 3; Areopagitica.

## Research log

- 2026-10-19: Correction found while coding AA4: region_of_birth and region_of_work are Northern Europe, not Western Europe; the United Kingdom is M49 Northern Europe (P3, data/reference/regions.csv).
- 2026-10-19: Read Britannica (Labriola); Paradise Lost Book 1 (Dartmouth).
