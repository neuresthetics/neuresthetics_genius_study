---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z1 audit fixes (blind audit /workspace/genius_study_audit/gs_8813a47_Z1/run1/): Z1-41 (FAIL): primary_system, A_locus and B_cause BELOW_THRESHOLD -> UNKNOWN, with AGNOS and BUDDH kept as leads (V3: second-hand quotations alone do not move a value off UNKNOWN); mid_basin -> UNKNOWN. Still not plotted."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z1, order P32: F 3, rank 139). Basics from Britannica (Tadao Sato and Britannica Editors, signed). Own voice on religion only in interviews about Ran, both as secondary quotations: to Michael Sragow (1986, reprinted in Sight & Sound, 2010), 'the gods or God or whoever it is observing human events is feeling sadness ... and powerlessness to affect human beings' behaviour'; to Cineaste (quoted in a Dallas Baptist University study guide), 'how God and Buddha, if they actually exist, perceive this human life'. Not a scientist. Span 1950–1985 at 0.7 (Rashomon to Ran). primary_system BELOW_THRESHOLD (leads AGNOS, BUDDH); A, B BELOW_THRESHOLD with readings named; C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD. Not plotted. Draft, not reviewed."}

identity:
  id: kurosawa-akira
  display_name: "Akira Kurosawa"
  roster:
    canonical_name: "Akira Kurosawa"
    rank: 139
    F: 3
    models: [Gemini, GPT, Grok]
    band: "core (3–4)"
    status: core
    field: film
    field_bucket: arts
  full_name: {value: "Kurosawa Akira", certainty: 0.7, cites: [{source: S1, locator: "title; opening"}], how_known: "Britannica (Japanese order)."}
  native_name: {value: "黒澤明", certainty: 0.5, cites: [{source: S1, locator: "title"}], how_known: "Coder's; the kanji are not in the source read."}
  aliases:
    - {name: "Akira-Kurosawa", kind: "roster alias"}
    - {name: "Kurosawa-Akira", kind: "roster alias"}

basics:
  birth:
    date: {value: "1910-03-23", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "Quick Facts; opening"}], how_known: "Britannica."}
    place: {value: "Tokyo", modern_name: "Tokyo, Japan", polity_then: "Empire of Japan", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}], how_known: "Britannica."}
  death:
    date: {value: "1998-09-06", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "Quick Facts; opening"}], how_known: "Britannica."}
    place: {value: "Tokyo", modern_name: "Tokyo, Japan", polity_then: "Japan", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1950, certainty: 0.7, cites: [{source: S1, locator: "'Films of the 1950s'"}], how_known: "Rashomon (1950): 'the first time a Japanese film had won such high international acclaim' (S1). Drunken Angel (1948), which 'made Kurosawa's name famous', is listed as a major work, not as lasting (coder's call); taking 1948 would not change any score."}
  era_bucket: {value: "1950 on", certainty: 0.7, cites: [{source: S1, locator: "'Films of the 1950s'"}], how_known: "From 1950 (P2: an edge year goes to the later bucket); 1948 would give '1850 to 1949', so 0.7 rests on the coder's call above."}
  region_of_birth: {value: "East Asia", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}], how_known: "Japan (P3)."}
  region_of_work: {value: "East Asia", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Japan."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Japanese"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
  occupations: {value: ["film director", "screenwriter", "painter (early)"], certainty: 0.7, cites: [{source: S1, locator: "'Early life'; 'First films'"}], how_known: "Britannica."}

contribution:
  fields: {value: ["film"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Rashomon", year: 1950, kind: work, lasting: "Venice Grand Prix and Academy Award; 'advanced the idea of cinema as a means of probing a metaphysical problem' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Films of the 1950s'"}], how_known: "Britannica."}
    - {value: "Ikiru", year: 1952, kind: work, lasting: "'regarded by many critics as one of the finest works in the history of the cinema' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Films of the 1950s'"}], how_known: "Britannica."}
    - {value: "Seven Samurai", year: 1954, kind: work, lasting: "his 'greatest commercial success'; inspiration for The Magnificent Seven (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Films of the 1950s'"}], how_known: "Britannica."}
    - {value: "Throne of Blood", year: 1957, kind: work, lasting: "'called the best film of all the countless cinematized Shakespearean dramas' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Films of the 1950s'"}], how_known: "Britannica."}
    - {value: "Ran", year: 1985, kind: work, lasting: "named in Britannica's opening among the films that won him 'international acclaim' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica; latest listed, so it ends the span (P30 addendum). The later sections were not read (fetch truncated)."}
  evidence_of_impact:
    - {value: "First Japanese film director to win international acclaim", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works:
    - {value: "Drunken Angel (Yoidore tenshi)", year: 1948, kind: other, certainty: 0.7, cites: [{source: S1, locator: "'First films'"}], how_known: "Britannica: 'made Kurosawa's name famous'."}
    - {value: "Kagemusha", year: 1980, kind: other, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  honours:
    - {value: "Golden Lion (Grand Prix), Venice, for Rashomon", year: 1951, certainty: 0.7, cites: [{source: S1, locator: "'Films of the 1950s'"}], how_known: "Britannica."}
  definition_fit: {value: "clearly meets", rationale: "'The first Japanese film director to win international acclaim' (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated in the sources read."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Father a former army officer, then a teacher who helped develop athletics instruction in Japan", role: father, certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated beyond the father's career."}
  schooling:
    - {value: "Art school after secondary school; painting in the Western style", stage: other, run_by: other, years: "c. 1927–1936", certainty: 0.5, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica (undated); years the coder's estimate."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["Japanese"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1950–1985", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Films of the 1950s'"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing read."}
  primary_system: {value: UNKNOWN, how_known: "(interview) Leads AGNOS and BUDDH. On Ran he spoke of 'wondering how God and Buddha, if they actually exist, perceive this human life' (S3, Cineaste, secondary quotation): a conditional, not a stated suspension of belief (AGNOS) or a profession (BUDDH). The Sragow remark (S2) describes what the film tries 'to get at'. Both are secondary quotations (§7). Under V3 (Miles Davis), second-hand quotations alone do not move a value off UNKNOWN (Z1 audit, Z1-41); revisit once Sragow 1986 or the Cineaste interview is read."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: AGNOS, reason: "'if they actually exist' (S3). Against: secondary quotation; conditional, not a stated suspension."}
    - {code: BUDDH, reason: "'God and Buddha' as the imagined observers (S3); Japanese setting. Against: no profession."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "(interview) Leads AGNOS and BUDDH: 'if they actually exist' (S3): no locus stated; secondary quotation (P20, §7). Under V3 (Miles Davis), second-hand quotations alone do not move a value off UNKNOWN (Z1 audit, Z1-41); revisit once Sragow 1986 or the Cineaste interview is read."}
    B_cause: {value: UNKNOWN, how_known: "(interview) Leads AGNOS and BUDDH. Not a scientist. The observing divinity feels 'powerlessness to affect human beings' behaviour' (S2): a reading toward no intervention (3–4), but it concerns human conduct in a film's viewpoint, not nature (P6, P16), and is a secondary quotation. Under V3 (Miles Davis), second-hand quotations alone do not move a value off UNKNOWN (Z1 audit, Z1-41); revisit once Sragow 1986 or the Cineaste interview is read."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read (P19); characters' words in Ran are not his (P42)."}
    D_authority: {value: UNKNOWN, how_known: "Nothing read (P19)."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read on the world's order (P7, P19)."}
  mid_basin: {value: UNKNOWN, how_known: "A and B both UNKNOWN (P19)."}
  statements:
    - text: "What I was trying to get at in Ran – and this was there from the script stage – was that the gods or God or whoever it is observing human events is feeling sadness about how human beings destroy each other, and powerlessness to affect human beings' behaviour."
      cites: [{source: S2, locator: "section 13, Ran"}]
      date: "1986"
      context: "As told to Michael Sragow, 1986; reprinted in Sight & Sound's 'Kurosawa on Kurosawa' (July 2010)."
      axes: [A_locus, B_cause]
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-19
      note: "Original 1986 publication not seen. Within the span (Ran, 1985) by a year: after it."
    - text: "What I meant was that some of the essential scenes of this film are based on my wondering how God and Buddha, if they actually exist, perceive this human life, this mankind stuck in the same absurd behavior patterns."
      cites: [{source: S3, locator: "Cineaste quotation"}]
      date: "1985"
      context: "Cineaste interview on Ran, correcting a Japanese magazine's report that he wanted a 'heavenly' viewpoint."
      axes: [A_locus]
      kind: "recorded interview"
      verified_against: "secondary quotation"
      verified_on: 2026-10-19
      note: "Quoted in a study guide; the Cineaste issue and year are not given there (1985 is the coder's estimate from the film's release; primary check pending)."
  changes_over_life: []
  coder_notes: "Coder's calls: (1) span from Rashomon (1950), not Drunken Angel (1948); (2) Ran (1985) ends the span from Britannica's opening list, since the later sections of the article were not read; Madadayo (1993) and Dreams (1990) are not listed; (3) both statements are secondary quotations, so nothing scores; (4) Something Like an Autobiography (1981/1982) not read for religion."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Japanese", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1950–1985", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Films of the 1950s'"}], how_known: "Rashomon (1950) to Ran (1985) (P29, P30)."}
  age_at_first_lasting_contribution: {value: 40, certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}], how_known: "1950 − 1910 = 40 (P30)."}
  first_evidence_of_lio_type_views: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S2, locator: "section 13"}], how_known: "Nothing scored at 3 or 4."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S2, locator: "section 13"}], how_known: "As above."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Only the Ran interviews read."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Not assessed."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Not assessed."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S2, locator: "section 13"}], how_known: "Not assessed."}
  reading: "Not assessed."
  notes: ""

institutions:
  - {value: "PCL (Photo Chemical Laboratories) studio", role: "assistant director", years: "1936–1943", kind: employer, certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica (the PCL expansion is the coder's)."}
collaborators:
  - {value: "Mifune Toshirō", relation: collaborator, note: "lead actor in most of his films from Drunken Angel", certainty: 0.7, cites: [{source: S1, locator: "'First films'"}], how_known: "Britannica."}
  - {value: "Yamamoto Kajirō", relation: "mentor or employer", note: "director he assisted until 1943", certainty: 0.7, cites: [{source: S1, locator: "'Early life'"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 139"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Britannica's later sections (1960s on, Legacy) were not returned by the fetch; Ran's place as the last lasting item rests on the opening list."
    - "Both own-voice statements are secondary quotations."
  open_questions:
    - "Read Something Like an Autobiography and the original Cineaste and Sragow interviews."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Tadao Sato; Britannica Editors"
    citation: "Sato, Tadao, and Britannica Editors. \"Kurosawa Akira.\" Encyclopaedia Britannica (15 Oct 2026). https://www.britannica.com/biography/Kurosawa-Akira. Read live 2026-10-19."
    url: "https://www.britannica.com/biography/Kurosawa-Akira"
    accessed: 2026-10-19
    reliability_note: "Signed article; body cited, AI question boxes not cited (P26)."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, institutions, collaborators]
  - id: S2
    type: secondary
    kind: other
    author: "Sight & Sound (BFI)"
    citation: "\"Kurosawa on Kurosawa.\" Sight & Sound, July 2010 (BFI). Archived https://web.archive.org/web/20190520121122/old.bfi.org.uk/sightandsound/feature/49625"
    url: "https://web.archive.org/web/20190520121122/old.bfi.org.uk/sightandsound/feature/49625"
    accessed: 2026-10-19
    reliability_note: "Magazine anthology of his interview remarks (Richie 1964; Rayns 1981; Sragow 1986); secondary quotation."
    used_for: [worldview, timing, lane_b]
  - id: S3
    type: secondary
    kind: other
    author: "Dallas Baptist University, Mitchell Center (study guide)"
    citation: "\"Akira Kurosawa's Lear: Ran and the Failure of the Samurai Ethic.\" Global film resources, Dallas Baptist University. https://www.dbu.edu/mitchell/global-film-resources/_documents/ranandthefailureofthesamuraiethic.pdf"
    url: "https://www.dbu.edu/mitchell/global-film-resources/_documents/ranandthefailureofthesamuraiethic.pdf"
    accessed: 2026-10-19
    reliability_note: "Unsigned teaching guide quoting a Cineaste interview without issue details; secondary quotation."
    used_for: [worldview]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Akira Kurosawa

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Kurosawa Akira (1910–1998), Japanese film director [S1]. Draft: primary_system UNKNOWN (leads AGNOS, BUDDH; interview); A, B UNKNOWN; C, D, E UNKNOWN; mid_basin UNKNOWN. Not plotted.

## Life and work

Painter, then assistant director at PCL from 1936; director from 1943 [S1].

## Contribution and impact

Rashomon, Ikiru, Seven Samurai, Throne of Blood, Ran [S1].

## Childhood and education

Father an army officer turned teacher; art school [S1].

## Adult working worldview

On Ran he spoke of how "God and Buddha, if they actually exist" see human life, and of an observer's "powerlessness" (interview, secondary quotations) [S2; S3].

## Heritage (context only)

Japanese [S1].

## Timing

1950–1985, from age 40 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Not assessed [S1].

## Open questions

- The autobiography and the original interviews.

## Research log

- 2026-10-19: Read Britannica (Sato), the Sight & Sound anthology and a study guide quoting Cineaste.
