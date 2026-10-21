---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AB1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-20
  change_log:
    - {date: 2026-10-20, by: "Grok Bot", summary: "AB1 audit fix: S1's bibliography dates the Philosophical Letters to 1734; wording corrected (no score change)."}
    - {date: 2026-10-20, by: "Grok Bot", summary: "Record created (stage 3 batch AB1, order P32: F 3, rank 223). Sources: SEP 'Voltaire' (J.B. Shank, 2024, read in full); Britannica students edition (S3) for full birth and death dates. Lasting: the philosophe authorship from Lettres philosophiques (1734), 'the key turning point', with which he 'pointed modern philosophy down several paths that it subsequently followed' and 'remains today an iconic hero' (S1); Candide (1759), 'Voltaire's most widely known text' (S1). Span 1734–1759 at 0.5 (alternative end 1778, his death, since the campaign for philosophie ran to the end), age 40. Worldview: S1 says 'it would be wrong to call Voltaire an atheist, or even an anti-Christian', that his 'personal religious views were subtle', and places him among debates of 'the so-called deists' while distancing him 'from more radical deists like Toland'; no own words on God quoted. primary_system BELOW_THRESHOLD (DEISM lead); A UNKNOWN (P19). Not a scientist (defender and popularizer of Newtonian science, not a contributor; P33 logic); B UNKNOWN. Not plotted. Draft, not reviewed."}

identity:
  id: voltaire
  display_name: "Voltaire"
  roster:
    canonical_name: "Voltaire"
    rank: 223
    F: 3
    models: [DeepSeek, GPT, Grok]
    band: "core (3–4)"
    status: "core"
    field: "philosophy"
    field_bucket: "philosophy"
  full_name: {value: "François-Marie d’Arouet", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP; pen name Voltaire. Britannica students edition writes 'Arouet' (S3)."}
  native_name: {value: "François-Marie Arouet", certainty: 0.7, cites: [{source: S3, locator: "para. 2"}], how_known: "Britannica."}
  aliases:
    - {name: "François-Marie Arouet", kind: "birth name"}

basics:
  birth:
    date: {value: "1694-11-21", certainty: 0.7, cites: [{source: S3, locator: "para. 2"}, {source: S1, locator: "opening"}], how_known: "Britannica students edition; SEP gives 1694."}
    place: {value: "Paris", modern_name: "Paris, France", polity_then: "Kingdom of France", certainty: 0.7, cites: [{source: S3, locator: "para. 2"}], how_known: "Britannica."}
  death:
    date: {value: "1778-05-30", certainty: 0.7, cites: [{source: S3, locator: "para. 4"}, {source: S1, locator: "1.6"}], how_known: "Britannica students edition; SEP gives 1778."}
    place: {value: "Paris", modern_name: "Paris, France", polity_then: "Kingdom of France", certainty: 0.5, cites: [{source: S3, locator: "para. 4"}], how_known: "Britannica: returned to Paris in February 1778 and died on May 30; place implied, not stated."}
  first_lasting_contribution_year: {value: 1734, certainty: 0.7, cites: [{source: S1, locator: "1. Voltaire's Life; 1.3"}], how_known: "Lettres philosophiques, 'published in 1734 ... the key turning point' (S1); P30 publication. S1's bibliography also dates the Philosophical Letters (Letters on the English Nation) to 1734."}
  era_bucket: {value: "1600 to 1749", certainty: 1.0, cites: [{source: S1, locator: "1.3"}], how_known: "1734 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "1.1"}], how_known: "France (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "1.3–1.6"}], how_known: "Cirey, Paris, Berlin, Geneva and Ferney: France, Prussia and Switzerland all fall in Western Europe."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["French", "English"], certainty: 0.7, cites: [{source: S1, locator: "1.2; Bibliography"}], how_known: "French works; English Essays of 1727 (S1)."}
  occupations: {value: ["writer", "philosopher", "playwright", "historian"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}

contribution:
  fields: {value: ["philosophy", "literature", "history"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}
  lasting_original_contributions:
    - {value: "The philosophe authorship and campaign: a new conception of philosophy and the philosopher, beginning with Lettres philosophiques", year: 1734, kind: "body of work", lasting: "'At the center of his work was a new conception of philosophy and the philosopher that in several crucial respects influenced the modern concept of each'; he 'pointed modern philosophy down several paths that it subsequently followed' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; 1.3"}], how_known: "From Lettres philosophiques, 1734 (S1)."}
    - {value: "Candide, ou l'Optimisme", year: 1759, kind: "work", lasting: "'Voltaire's most widely known text' (S1)", certainty: 0.5, cites: [{source: S1, locator: "2"}], how_known: "First published 1759 (S1); 0.5 because 'most widely known' is thin lasting wording (P13)."}
  evidence_of_impact:
    - {value: "'Voltaire remains today an iconic hero for everyone who sees a positive linkage between critical reason and political resistance'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "1.7"}], how_known: "SEP."}
  major_works:
    - {value: "Philosophical Dictionary", year: 1764, kind: "book", certainty: 0.7, cites: [{source: S3, locator: "para. 5"}], how_known: "Britannica students edition."}
    - {value: "The Century of Louis XIV", year: 1751, kind: "book", certainty: 0.7, cites: [{source: S3, locator: "para. 5"}], how_known: "Britannica students edition."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Defined the Enlightenment philosophe (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Fourth of five children of a well-to-do public official and an aristocratic mother", role: "family", certainty: 0.7, cites: [{source: S1, locator: "1.1"}], how_known: "SEP."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling:
    - {value: "Jesuit Collège Louis-le-Grand, Paris", certainty: 0.7, cites: [{source: S1, locator: "1.1"}], how_known: "SEP."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1734–1759", certainty: 0.5, cites: [{source: S1, locator: "1.3; 2"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "S1: 'it would be wrong to call Voltaire an atheist, or even an anti-Christian so long as one accepts a broad understanding of what Christianity can entail'; his 'personal religious views were subtle'; he worked within the debates of 'the so-called deists' but distanced himself 'from more radical deists like Toland'. No own words on God quoted; no system reaches 0.5. DEISM is the lead."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: DEISM, reason: "Lead from S1's placing among the deist debates; not quoted."}
    - {code: CHRIST, reason: "S1: not anti-Christian on a broad reading."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "No own words on God quoted in S1 (P19)."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30): a defender and popularizer of Newtonian science, not a contributor to it (P33 logic). Held UNKNOWN: Jason has not ruled on RQ-AA8-1 (whether a scholar's reconstruction of a non-scientist's account of nature gives B), so no reconstruction-based B is applied."}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, so the P4 test cannot be applied (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "Leads for own words: Philosophical Dictionary ('Theist'), Traité sur la tolérance (1763), Poème sur le désastre de Lisbonne (1756)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated in S1 (Jesuit schooling only)."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1734–1759", certainty: 0.5, cites: [{source: S1, locator: "1.3; 2"}], how_known: "Lettres philosophiques (1734) to Candide (1759), first and last lasting items (P29, P30); 0.5 following Candide (weakest-work rule). Alternative 1734–1778."}
  age_at_first_lasting_contribution: {value: 40, certainty: 0.7, cites: [{source: S1, locator: "1. Voltaire's Life"}], how_known: "S1: 'published in 1734 when he was forty years old'; 1734 − 1694 = 40."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Enlightenment critique (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "Court of Frederick II of Prussia", role: "guest and chamberlain", years: "1750–1753", kind: "patron or funder", certainty: 0.5, cites: [{source: S1, locator: "1.5"}, {source: S3, locator: "para. 4"}], how_known: "Britannica students edition gives 1750 and 'three years later'."}
collaborators:
  - {value: "Émilie du Châtelet", relation: "collaborator", note: "companion and fellow Newtonian, from 1733", certainty: 0.7, cites: [{source: S1, locator: "1.3–1.4"}], how_known: "SEP."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 223"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Worldview BELOW_THRESHOLD (DEISM lead)."
    - "Candide lasting at 0.5."
  open_questions:
    - "Own words on God (Philosophical Dictionary; Lisbon poem)."
    - "Span end: 1759 (Candide) or 1778?"

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "J.B. Shank"
    citation: "Shank, J.B. 'Voltaire.' Stanford Encyclopedia of Philosophy (substantive revision 21 August 2024). https://plato.stanford.edu/entries/voltaire/"
    url: "https://plato.stanford.edu/entries/voltaire/"
    accessed: 2026-10-19
    reliability_note: "Signed encyclopedia entry, read in full."
    used_for: [identity, basics, contribution, childhood, worldview, timing, institutions, collaborators]
  - id: S2
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [review]
  - id: S3
    type: tertiary
    kind: "encyclopedia"
    author: "Encyclopaedia Britannica"
    citation: "'Voltaire.' Britannica (students edition). https://kids.britannica.com/students/article/Voltaire/277627"
    url: "https://kids.britannica.com/students/article/Voltaire/277627"
    accessed: 2026-10-19
    reliability_note: "Read in full; used for full dates and a few works."
    used_for: [basics, contribution]
---

## Summary

Voltaire (1694–1778), French writer and philosophe [S1]. Draft: worldview BELOW_THRESHOLD. Not plotted.

## Life and work

Paris; England; Cirey; Berlin; Ferney [S1].

## Contribution and impact

Lettres philosophiques 1734; Candide 1759 [S1].

## Childhood and education

Louis-le-Grand [S1].

## Adult working worldview

Deist debates; not an atheist (scholar's reading) [S1].

## Heritage (context only)

Not stated.

## Timing

1734–1759, age 40 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Own words; span end.

## Research log

- 2026-10-20: AB1 audit fix: S1's bibliography dates the Philosophical Letters to 1734; wording corrected (no score change).
- 2026-10-20: Read SEP (Shank, 2024) and Britannica students edition.
