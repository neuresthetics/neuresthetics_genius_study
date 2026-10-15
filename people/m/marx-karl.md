---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch H)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-15
  change_log:
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch H, order P32: F 5, rank 48). Basics from Britannica (Feuer) and SEP (Wolff and Leopold). Worldview from the Introduction to A Contribution to the Critique of Hegel's Philosophy of Right (1844), read in the marxists.org English web copy (0.7 cap). Not a scientist under P30. primary_system ATHE 0.7; A 4 at 0.7 (alt BELOW_THRESHOLD); B UNKNOWN (no statement on the order of nature read, P16); C, D, E UNKNOWN; mid_basin false at 0.7 (A ≥ 3 branch). Not plotted. Draft, not reviewed."}

identity:
  id: marx-karl
  display_name: "Karl Marx"
  roster:
    canonical_name: "Karl Marx"
    rank: 48
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: philosophy
    field_bucket: philosophy
  full_name: {value: "Karl Heinrich Marx", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  native_name: {value: UNKNOWN, how_known: "German in Latin script."}
  aliases: []

basics:
  birth:
    date: {value: "1818-05-05", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica; SEP gives the year 1818 only."}
    place: {value: "Trier, Rhine province, Prussia", modern_name: "Trier, Germany", polity_then: "Kingdom of Prussia", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "1883-03-14", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica; SEP gives the year 1883 only."}
    place: {value: "London, England", modern_name: "London, United Kingdom", polity_then: "United Kingdom", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1844, certainty: 0.7, cites: [{source: S1, locator: "'Early years' (Deutsch-französische Jahrbücher)"}, {source: S3, locator: "header ('First published: in Deutsch-Französische Jahrbücher, 7 & 10 February 1844')"}], how_known: "The Critique of Hegel's Philosophy of Right: Introduction, with its 'oft-quoted' opium remark (S1), first published February 1844 (S3) (P13, P30). The 1844 Manuscripts were unpublished for about 100 years (S1)."}
  era_bucket: {value: "1750 to 1849", certainty: 0.7, cites: [{source: S3, locator: "header"}], how_known: "From 1844 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Germany is Western Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.5, cites: [{source: S1, locator: "'Early years'"}], how_known: "Cologne, Paris, Brussels, then London from 1850 (Northern Europe); the early works are Western European (0.5)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [German], certainty: 0.7, cites: [{source: S1, locator: "'Early years' (German titles)"}], how_known: "Britannica."}
  occupations: {value: ["philosopher", "economist", "journalist", "revolutionary"], certainty: 0.7, cites: [{source: S1, locator: "opening; 'Early years'"}], how_known: "Britannica."}

contribution:
  fields: {value: ["political philosophy", "economics", "theory of history"], certainty: 0.7, cites: [{source: S2, locator: "contents (§§1–3)"}], how_known: "SEP."}
  lasting_original_contributions:
    - {value: "Critique of Hegel's Philosophy of Right: Introduction (religion as 'the opium of the people')", year: 1844, kind: work, lasting: "'oft-quoted' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}, {source: S3, locator: "header"}], how_known: "Britannica; publication date from the marxists.org header."}
    - {value: "The Communist Manifesto (with Engels)", year: 1848, kind: work, lasting: "'the most celebrated pamphlet in the history of the socialist movement' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    - {value: "Das Kapital", kind: work, lasting: "'the movement's most important book' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica; the year is not given in the passages read, so the period ends at 1848 (P30)."}
  evidence_of_impact:
    - {value: "Basis of the body of thought known as Marxism", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Founder of Marxism (S1, S2).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Jewish by descent; father baptized in the Evangelical Established Church about a year before Karl's birth", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father Heinrich, a lawyer and 'man of the Enlightenment'; mother Henrietta Pressburg, from Holland", role: parents, certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  household_circumstances: {value: "Successful lawyer's household, eldest surviving son of nine children", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  schooling:
    - {value: "High school in Trier", stage: "grammar or secondary school", run_by: "state or municipal", years: "1830–1835", ages: "12–17", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica; run_by is the coder's reading."}
    - {value: "University of Bonn, then University of Berlin (law and philosophy)", stage: university, run_by: "state or municipal", years: "1835–", ages: "17–", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: TODO}
  notable_events:
    - {value: "Baptized", year: 1824, age: 6, certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica: baptized when he was six."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1844–1848", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing read on natural science and religion."}
  primary_system:
    value: ATHE
    basis: written_profession
    certainty: 0.7
    cites: [{source: S3, locator: "paragraphs 1–4"}, {source: S1, locator: "'Early years'"}]
    rationale: "Religion is a human product ('Man makes religion, religion does not make man'), heaven a 'fantastic reality' in which man finds 'only the reflection of himself', and its abolition 'the demand for their real happiness' (S3); combined with Feuerbach's materialism (S1). Atheism with naturalism. Web copy, so 0.7."
    how_known: "Published essay read in an English web copy (marxists.org); German original not read."
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: ATHE, reason: "Chosen: religion as a human projection; materialism (S1)."}
    - {code: SECHUM, reason: "Alternative: 'man is the highest essence for man' (S3) is humanist; not chosen because the text is a critique of religion as such."}
  lio_axes:
    A_locus:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S3, locator: "paragraphs 1–2"}]
      how_known: "Published essay in an English web copy, 0.7 cap; alternative named."
      rationale: "No separate God: God and heaven are man's reflection ('Man makes religion'; 'the fantastic reality of heaven, where he sought a superman'). Scored like Pauling's rejection of the supernatural (A 4). Named alternative: BELOW_THRESHOLD, since the passage criticizes religion rather than stating 'there is no God' in so many words."
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30); no statement on the order of nature read (P16). His materialism (S1) is not a statement on exceptions in nature."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read."}
    D_authority: {value: UNKNOWN, how_known: "Nothing read on revelation against observation."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7)."}
  mid_basin: {value: false, certainty: 0.7, cites: [{source: S3, locator: "paragraphs 1–2"}], how_known: "A_locus 4 (≥ 3): the A ≥ 3 branch reads A only (P10), so 0.7."}
  statements:
    - text: "The foundation of irreligious criticism is: Man makes religion, religion does not make man."
      cites: [{source: S3, locator: "paragraph 2"}]
      date: "1844"
      context: "Opening of the Introduction, after 'the criticism of religion is the prerequisite of all criticism'."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "marxists.org English web copy (transcription source unknown; proofed by Andy Blunden, 2005); emphasis marks dropped; 0.7 cap. TODO: check against MECW 3 or the German (MEW 1)."
    - text: "Religion is the sigh of the oppressed creature, the heart of a heartless world, and the soul of soulless conditions. It is the opium of the people."
      cites: [{source: S3, locator: "paragraph 4"}]
      date: "1844"
      context: "Same text."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "Web copy; TODO MECW check."
  changes_over_life:
    - {value: "School writings showed 'a spirit of Christian devotion'; moved toward atheism with the Young Hegelians in Berlin", year: 1836, certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica; the scored worldview is the adult one."}
  coder_notes: "Coder's call: one published essay read; ATHE at 0.7 (web copy). B UNKNOWN keeps him off the chart."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "German-Jewish (descended from rabbis)", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Jewish by descent; Evangelical (Prussian Protestant) by family conversion", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  baptism_or_initiation: {value: "Baptized at age six (Evangelical)", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1844–1848", certainty: 0.5, cites: [{source: S1, locator: "opening; 'Early years'"}], how_known: "1844 to 1848, first to last dated listed contribution (P29, P30); Das Kapital is undated in the passages read, so the end year is too early (0.5)."}
  age_at_first_lasting_contribution: {value: 26, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "1844 − 1818 = 26 (P30)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "B is UNKNOWN."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S3, locator: "text"}], how_known: "No statement on the order of nature read."}
  worldview_during_major_work: {value: "ATHE", certainty: 0.7, cites: [{source: S3, locator: "paragraphs 1–4"}], how_known: "As primary_system."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Nothing read on mathematics.", certainty: 0.5, cites: [{source: S1, locator: "'Early years'"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "'Early years'"}], how_known: "Humanities courses at Bonn (S1)."}
  circle_present: {value: "no", rationale: "God as human projection.", certainty: 0.5, cites: [{source: S3, locator: "paragraph 2"}], how_known: "Coder's reading."}
  reading: "Religion as a human product; no lawful-God circle."
  notes: ""

institutions:
  - {value: "Rheinische Zeitung, Cologne", role: editor, years: "1842–1843", kind: employer, certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}
collaborators:
  - {value: "Friedrich Engels", relation: collaborator, note: "lifelong collaborator from 1844", certainty: 0.7, cites: [{source: S1, locator: "'Early years'"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 48"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags: []
  open_questions:
    - "Check the quotes against MECW 3 / MEW 1; date Das Kapital vol. 1 from a source read."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Lewis S. Feuer"
    citation: "Feuer, Lewis S. \"Karl Marx.\" Encyclopaedia Britannica, updated 4 September 2026. https://www.britannica.com/biography/Karl-Marx."
    url: "https://www.britannica.com/biography/Karl-Marx"
    accessed: 2026-10-15
    reliability_note: "Signed article body (opening and 'Early years'); the Top Questions box is not used."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: secondary
    kind: encyclopedia
    author: "Jonathan Wolff and David Leopold"
    year: 2025
    citation: "Wolff, Jonathan, and David Leopold. \"Karl Marx.\" Stanford Encyclopedia of Philosophy, first published 26 August 2003, substantive revision 27 March 2025. https://plato.stanford.edu/entries/marx/."
    url: "https://plato.stanford.edu/entries/marx/"
    accessed: 2026-10-15
    reliability_note: "Peer-reviewed reference article; authors as shown in the citation information on the page."
    used_for: [contribution]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "Karl Marx"
    year: 1844
    citation: "Marx, Karl. \"A Contribution to the Critique of Hegel's Philosophy of Right: Introduction.\" Deutsch-Französische Jahrbücher, February 1844. English web copy, Marxists Internet Archive."
    url: "https://www.marxists.org/archive/marx/works/1843/critique-hpr/intro.htm"
    accessed: 2026-10-15
    reliability_note: "Unofficial web copy; transcription source unknown; §7 cap 0.7."
    used_for: [basics, contribution, worldview, timing, lane_b]
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

# Karl Marx

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Karl Marx (1818–1883), German philosopher, economist and revolutionary: The Communist Manifesto, Das Kapital [S1]. Draft: primary_system ATHE 0.7; A 4 at 0.7; B, C, D, E UNKNOWN; mid_basin false. Not plotted.

## Life and work

Trier, Bonn, Berlin; Rheinische Zeitung; Paris, Brussels, London [S1].

## Contribution and impact

Critique of Hegel's Philosophy of Right: Introduction (1844), Manifesto (1848), Das Kapital [S1, S3].

## Childhood and education

Jewish family; father baptized before his birth; Karl baptized at six [S1].

## Adult working worldview

'Man makes religion, religion does not make man'; religion 'is the opium of the people' [S3].

## Heritage (context only)

German-Jewish, Evangelical by conversion [S1].

## Timing

First lasting contribution 1844, at 26 [S1, S3].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No circle [S3].

## Open questions

- MECW check; Kapital date.

## Research log

- 2026-10-15: Read Britannica (Feuer, opening and 'Early years'), SEP contents, and the marxists.org Introduction.
