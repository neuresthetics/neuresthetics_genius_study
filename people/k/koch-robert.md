---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA9)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-20, by: "Grok Bot", summary: "AA10 audit fix: postulates item year stays UNKNOWN, with 1884 as the candidate only (catalogue record, paper not read)."}
    - {date: 2026-10-20, by: "Grok Bot", summary: "AA9 audit fixes: postulates candidate year 1884 (S4), span alternative 1876–1884; death 27 May 1910 at 0.7 (NobelPrize.org, S5); region of work Eastern Europe (Wollstein), alternative Western Europe."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA9, order P32: F 3, rank 215). Source: Britannica scholars edition, signed by Lloyd Grenfell Stevenson (read in full); Britannica students edition (S3) for the death-day conflict. Lasting: the anthrax life cycle (announced at Breslau, 1876), which 'afforded for the first time convincing proof of the definite causal relation of a particular microorganism to a particular disease' (S1); Koch's postulates (named after him; S1 gives no year; candidate 1884, Die Aetiologie der Tuberkulose, Mitt. Kaiserl. Gesundheitsamte II, S4). Tuberculosis (1882) and cholera (1883) discoveries carry prize-time praise only in S1 (Nobel 1905), so not listed as lasting (P13). Span 1876 at 0.5, alternative 1876–1884 (postulates candidate year), age 33. Death 27 May 1910 at 0.7 (NobelPrize.org, S5). Region of work Eastern Europe (Wollstein, now Wolsztyn, Poland, where the span took place: AA6 rule, P3 modern country), alternative Western Europe. Scientist: B 3 at 0.5, alt 4 (P35). Worldview UNKNOWN. Not plotted. Draft, not reviewed."}

identity:
  id: koch-robert
  display_name: "Robert Koch"
  roster:
    canonical_name: "Robert Koch"
    rank: 215
    F: 3
    models: [Claude, DeepSeek, Gemini]
    band: "core (3–4)"
    status: "core"
    field: "medicine"
    field_bucket: "medicine"
  full_name: {value: "Robert Heinrich Hermann Koch", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  native_name: {value: "Robert Koch", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  aliases: []

basics:
  birth:
    date: {value: "1843-12-11", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
    place: {value: "Clausthal, Hannover", modern_name: "Clausthal-Zellerfeld, Germany", polity_then: "Kingdom of Hanover", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  death:
    date: {value: "1910-05-27", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S5, locator: "Died"}, {source: S3, locator: "para. 6"}], how_known: "Britannica scholars edition and NobelPrize.org (S5): 27 May. The students edition (S3, para. 6) says 28 May; not a real dispute."}
    place: {value: "Baden-Baden", modern_name: "Baden-Baden, Germany", polity_then: "German Empire", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1876, certainty: 0.7, cites: [{source: S1, locator: "Anthrax research"}], how_known: "The anthrax life cycle 'was announced and illustrated at Breslau in 1876' (S1); P30 first public statement."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "Anthrax research"}], how_known: "1876 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Germany (P3)."}
  region_of_work: {value: "Eastern Europe", certainty: 0.7, cites: [{source: S1, locator: "Early training; Anthrax research"}], how_known: "The 1876 span work was done at Wollstein, now Wolsztyn, Poland (AA6 rule; P3 modern country; regions.csv puts Poland in Eastern Europe). Alternative Western Europe (Berlin, home region)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["German"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading: German papers and Berlin societies."}
  occupations: {value: ["physician", "bacteriologist"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}

contribution:
  fields: {value: ["medicine", "bacteriology"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica: 'one of the founders of bacteriology'."}
  lasting_original_contributions:
    - {value: "Life cycle of the anthrax bacillus (spore formation), the first proof that a specific microorganism causes a specific disease", year: 1876, kind: "discovery", lasting: "'The anthrax work afforded for the first time convincing proof of the definite causal relation of a particular microorganism to a particular disease' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Anthrax research"}], how_known: "Announced at Breslau, 1876 (S1)."}
    - {value: "Koch's postulates (four criteria for proving that a disease is caused by a specific organism)", year: UNKNOWN, kind: "method", lasting: "'called Koch's postulates' (S1): named after him", certainty: 0.5, cites: [{source: S1, locator: "Contributions to general bacteriology and pathology"}, {source: S4, locator: "bibliographic record"}], how_known: "Item year UNKNOWN: S1 places them after his move to the Imperial Health Office in Berlin but gives no year. Candidate year 1884 (not set: the catalogue record shows the paper exists, not that it states the postulates; read the paper or a historian first): Die Aetiologie der Tuberkulose, Mittheilungen aus dem Kaiserlichen Gesundheitsamte II, pp. 1–88 (S4; the paper that presents them, after Loeffler's 1883 formulation per the AA9 audit; text not read here)."}
  evidence_of_impact:
    - {value: "Koch's postulates", kind: "named after them", certainty: 0.7, cites: [{source: S1, locator: "Contributions to general bacteriology and pathology"}], how_known: "Britannica."}
    - {value: "Nobel Prize for Physiology or Medicine (1905), for tuberculosis", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
    - {value: "'his place in the history of science was universally recognized'; his pupils 'were the creators of the new era of bacteriology'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "Historical assessment"}], how_known: "Stevenson."}
  major_works:
    - {value: "Paper on the investigation, preservation and photographing of bacteria", year: 1877, kind: "paper or paper series", certainty: 0.7, cites: [{source: S1, locator: "Contributions to general bacteriology and pathology"}], how_known: "Britannica."}
    - {value: "Etiology of wound infection", year: 1878, kind: "paper or paper series", certainty: 0.7, cites: [{source: S1, locator: "Contributions to general bacteriology and pathology"}], how_known: "Britannica."}
    - {value: "Announcement of the tubercle bacillus (Physiological Society of Berlin, 24 March 1882)", year: 1882, kind: "paper or paper series", certainty: 0.7, cites: [{source: S1, locator: "Studies of tuberculosis and cholera"}], how_known: "Britannica."}
  honours:
    - {value: "Nobel Prize for Physiology or Medicine", year: 1905, certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  definition_fit: {value: "clearly meets", rationale: "Founder of bacteriology (S1).", certainty: 0.7, cites: [{source: S1, locator: "Historical assessment"}], how_known: "Britannica."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household: []
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling:
    - {value: "University of Göttingen, medicine (graduated 1866; teacher Jacob Henle)", certainty: 0.7, cites: [{source: S1, locator: "Early training; Anthrax research"}], how_known: "Britannica."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1876", certainty: 0.5, cites: [{source: S1, locator: "Anthrax research"}], how_known: "Equals timing.major_work_period; alternative 1876–1884."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system: {value: UNKNOWN, how_known: "No own words on belief read in S1."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered: []
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing first-hand read (P19)."}
    B_cause: 
      value: 3
      basis: inference_from_work
      certainty: 0.5
      cites: [{source: S1, locator: "Anthrax research; Contributions"}]
      how_known: "Scientist (P30). B from working science with no statement of their own on law and exception, so 3 at 0.5, alternative 4, never 4 (P35)."
      rationale: "Experimental bacteriology: a specific organism always produces a specific disease (the postulates, S1): lawful nature in his science. Alternative 4."
      alternatives:
        - {value: 4, note: "Working science cannot tell lawful-with-exceptions from exceptionless (P35).", cites: [{source: S1, locator: "Anthrax research; Contributions"}]}
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, so the P4 test cannot be applied (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "Lead: Brock, Robert Koch: A Life in Medicine and Bacteriology (1988) for any statement on religion."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated in S1."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1876", certainty: 0.5, cites: [{source: S1, locator: "Anthrax research"}], how_known: "The one dated lasting item (P29, P30); 0.5 under the weakest-work rule. Alternative 1876–1884 (postulates candidate year, S4)."}
  age_at_first_lasting_contribution: {value: 33, certainty: 0.7, cites: [{source: S1, locator: "Introduction; Anthrax research"}], how_known: "1876 − 1843 = 33 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Bacteriology (S1).", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "Imperial Health Office, Berlin", role: "head of bacteriology laboratory", years: UNKNOWN, kind: "government or state body", certainty: 0.7, cites: [{source: S1, locator: "Contributions to general bacteriology and pathology"}], how_known: "Britannica; years not given."}
collaborators:
  - {value: "Ferdinand Cohn", relation: "collaborator", note: "published the 1876 anthrax paper", certainty: 0.7, cites: [{source: S1, locator: "Anthrax research"}], how_known: "Britannica."}
  - {value: "Jacob Henle", relation: "teacher", note: "Göttingen", certainty: 0.7, cites: [{source: S1, locator: "Anthrax research"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 215"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Worldview: no source."
    - "Postulates candidate year 1884; span alternative 1876–1884."
  open_questions:
    - "Read the 1884 paper to confirm the postulates and fix the span end."
    - "Own words on belief (Brock 1988)."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Lloyd Grenfell Stevenson"
    citation: "Stevenson, Lloyd Grenfell. 'Robert Koch.' Encyclopaedia Britannica (scholars edition). https://kids.britannica.com/scholars/article/Robert-Koch/45848"
    url: "https://kids.britannica.com/scholars/article/Robert-Koch/45848"
    accessed: 2026-10-19
    reliability_note: "Signed article, scholars edition, read in full."
    used_for: [identity, basics, contribution, childhood, timing, institutions, collaborators]
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
    citation: "'Robert Koch.' Britannica (students edition). https://kids.britannica.com/students/article/Robert-Koch/275309"
    url: "https://kids.britannica.com/students/article/Robert-Koch/275309"
    accessed: 2026-10-19
    reliability_note: "Read in full; used only for the death-day note."
    used_for: [basics]
  - id: S4
    type: secondary
    kind: "database"
    author: "WorldCat"
    citation: "WorldCat record: Koch, Robert. 'Die Aetiologie der Tuberkulose.' Mittheilungen aus dem Kaiserlichen Gesundheitsamte 2 (Berlin: Hirschwald, 1884), pp. 1–88. OCLC 880639195. https://search.worldcat.org/title/880639195"
    url: "https://search.worldcat.org/title/880639195"
    accessed: 2026-10-19
    reliability_note: "Bibliographic record read; the paper itself not read."
    used_for: [contribution]
  - id: S5
    type: secondary
    kind: "institutional page"
    author: "NobelPrize.org"
    citation: "'Robert Koch – Facts.' NobelPrize.org. https://www.nobelprize.org/prizes/medicine/1905/koch/facts/"
    url: "https://www.nobelprize.org/prizes/medicine/1905/koch/facts/"
    accessed: 2026-10-19
    reliability_note: "Facts page, read in full."
    used_for: [basics]
---

## Summary

Robert Koch (1843–1910), physician and bacteriologist [S1]. Draft: worldview UNKNOWN. Not plotted.

## Life and work

Clausthal; Wollstein; Berlin [S1].

## Contribution and impact

Anthrax cycle 1876; postulates [S1].

## Childhood and education

Göttingen [S1].

## Adult working worldview

None read.

## Heritage (context only)

Not stated.

## Timing

1876, age 33 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Postulates year; own words.

## Research log

- 2026-10-20: AA9 audit fixes: postulates candidate year 1884 (S4), span alternative 1876–1884; death 27 May 1910 at 0.7 (NobelPrize.org, S5); region of work Eastern Europe (Wollstein), alternative Western Europe.
- 2026-10-20: AA10 audit fix: postulates item year stays UNKNOWN, with 1884 as the candidate only (catalogue record, paper not read).
- 2026-10-20: Read Britannica (Stevenson, scholars edition) and the students edition.
