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
    - {date: 2026-10-17, by: "Grok Bot", summary: "Record created (stage 3 batch O, order P32: F 4, rank 91). Basics from Britannica (Irving Kaplansky, signed; body only) and MacTutor (O'Connor and Robertson). Worldview from his Königsberg address 'Naturerkennen und Logik' (1930; Die Naturwissenschaften, pp. 959–963), read in a web transcription. Mathematician, not counted a scientist (P30). primary_system UNKNOWN; A UNKNOWN; B 3 (0.5, alt 4) from an explicit remark on nature ('überall die Einheit der Naturgesetze'); mid_basin UNKNOWN (P19). Not plotted. Draft, not reviewed."}
    - {date: 2026-10-17, by: "Grok Bot", summary: "Batch O audit fix (#23): S2 relabelled an unofficial web copy (cap 0.7; verified_against 'secondary quotation'), print check pending. v8's ruling on RQ O2 (on the auditor's advice): B 3 at 0.5, alternative 4, is allowed under P16 (recorded in OPEN_DECISIONS). Values unchanged."}

identity:
  id: hilbert-david
  display_name: "David Hilbert"
  roster:
    canonical_name: "David Hilbert"
    rank: 91
    F: 4
    models: [Claude, Gemini, GPT, Grok]
    band: "core (3–4)"
    status: core
    field: mathematics
    field_bucket: mathematics
  full_name: {value: "David Hilbert", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  native_name: {value: "David Hilbert", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "German; same spelling."}
  aliases:
    - {name: "David-Hilbert", kind: "roster alias"}
    - {name: "Hilbert-David", kind: "roster alias"}

basics:
  birth:
    date: {value: "1862-01-23", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Königsberg, Prussia", modern_name: "Kaliningrad, Russia", polity_then: "Kingdom of Prussia", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "1943-02-14", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Göttingen, Germany", modern_name: "Göttingen, Germany", polity_then: "Germany", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1897, certainty: 0.5, cites: [{source: S1, locator: "Zahlbericht sentence"}], how_known: "The Zahlbericht (1897), which 'consolidated what was known' and 'pointed the way to the developments that followed' (S1). The finiteness theorem for invariants is undated in the body (P39) and may be earlier. 1899 (Grundlagen der Geometrie, 'a turning point') is the alternative. Coder's pick (P13)."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "From 1897 (P2); every candidate year falls in the same bucket."}
  region_of_birth: {value: "Eastern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Russia (P3), as for Kant."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "career paragraph"}], how_known: "Göttingen from 1895 (Germany)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [German], certainty: 0.7, cites: [{source: S1, locator: "titles"}], how_known: "Britannica."}
  occupations: {value: ["mathematician", "professor"], certainty: 0.7, cites: [{source: S1, locator: "opening; career paragraph"}], how_known: "Britannica."}

contribution:
  fields: {value: ["algebra and invariant theory", "number theory", "foundations of geometry", "foundations of mathematics", "analysis"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Theorem of invariants (finite basis)", year: UNKNOWN, kind: theory, lasting: "'Hilbert proved the theorem of invariants' (S1)", certainty: 0.7, cites: [{source: S1, locator: "invariants paragraph"}], how_known: "Britannica; undated."}
    - {value: "Zahlbericht (report on algebraic number theory)", year: 1897, kind: work, lasting: "'pointed the way to the developments that followed' (S1)", certainty: 0.5, cites: [{source: S1, locator: "Zahlbericht sentence"}], how_known: "Britannica; lasting status is the coder's reading."}
    - {value: "Grundlagen der Geometrie (axioms for Euclidean geometry)", year: 1899, kind: work, lasting: "'marked a turning point in the axiomatic treatment of geometry' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Grundlagen sentence"}], how_known: "Britannica."}
    - {value: "The 23 problems (Paris address)", year: 1900, kind: other, lasting: "'A substantial part of Hilbert's fame rests on' them (S1)", certainty: 0.7, cites: [{source: S1, locator: "problems paragraph"}], how_known: "Britannica."}
    - {value: "Integral equations; the basis of Hilbert space", year: 1909, kind: theory, lasting: "'led directly to 20th-century research in functional analysis' (S1)", certainty: 0.7, cites: [{source: S1, locator: "integral equations paragraph"}], how_known: "Britannica ('in about 1909'). Mathematics: Hilbert space is 'useful in mathematical analysis and quantum mechanics' but is not itself a theory about physical systems; S1 also credits 'important memoirs on kinetic gas theory and the theory of radiations' to mathematical physics, but they are not listed as lasting here (coder's call), so he is not counted a scientist (P30)."}
  evidence_of_impact:
    - {value: "Bolyai Prize (1910), Mittag-Leffler Prize (1939, with Picard); Göttingen's eminence 'largely because of Hilbert'", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
  parents_and_household: []
  household_circumstances: {value: TODO}
  schooling:
    - {value: "University of Königsberg (Ph.D. 1885)", stage: university, years: "–1885", certainty: 0.7, cites: [{source: S1, locator: "career paragraph"}], how_known: "Britannica."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [German], certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1897–1909", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing read on religion; MacTutor's biography has no passage on religion."}
  primary_system: {value: UNKNOWN, how_known: "Nothing read on God or religion."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered: []
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing read on God; the 1930 address does not mention God."}
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.5
      cites: [{source: S2, locator: "'Parallelismus von Natur und Denken' passage"}]
      rationale: "A mathematician needs an explicit remark on nature (P16). The 1930 address gives one: 'wir beobachten die Einheit des Stoffes in der Materie, und wir konstatieren überall die Einheit der Naturgesetze' (we observe the unity of matter, and we find everywhere the unity of the laws of nature), and nature 'comes to meet us ... as if it were ready to reveal its secrets'. A lawful nature everywhere, with no stated no-exception claim (P40) and no denial of miracles: B 3 at 0.5, alternative 4 (P16, as ruled on RQ O2: an explicit remark on nature that states a lawful order with no stated no-exception claim gives B 3 at 0.5, alternative 4; this follows P35's logic without being a P35 case)."
      how_known: "Published address read in an unofficial web copy (cap 0.7, print check pending); translation the coder's. Dated 1930, after the working years (P20), so 0.5 either way. Allowed under P16 by v8's ruling on RQ O2 of the batch O audit (on the auditor's advice)."
      alternatives:
        - {value: 4, note: "No stated exceptionless law (P40).", cites: [{source: S2, locator: "'Parallelismus von Natur und Denken' passage"}]}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read."}
    D_authority: {value: UNKNOWN, how_known: "Nothing read; 'Wir müssen wissen, wir werden wissen' is about knowability, not revelation."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7)."}
  mid_basin: {value: UNKNOWN, how_known: "A is UNKNOWN (P19)."}
  statements:
    - text: "Noch einen anderen Parallelismus nehmen wir wahr: unser Denken geht auf Einheit aus und sucht Einheit zu bilden; wir beobachten die Einheit des Stoffes in der Materie, und wir konstatieren überall die Einheit der Naturgesetze. Dabei kommt uns die Natur in Wirklichkeit bei unserer Forschung sehr entgegen, als wäre sie bereit, ihre Geheimnisse gern zu enthüllen."
      cites: [{source: S2, locator: "'Parallelismus von Natur und Denken' passage"}]
      date: "1930"
      context: "Address 'Naturerkennen und Logik' to the Society of German Scientists and Physicians, Königsberg, 1930, printed in Die Naturwissenschaften (28 November 1930), pp. 959–963 (S1 names the address)."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-17
      note: "Unofficial web copy of the printed address (its header gives the Naturwissenschaften citation); web-copy cap 0.7 (CODING_GUIDE §7); print check pending. Coder's translation in the B rationale."
  changes_over_life: []
  coder_notes: "Coder's call. B 3 rests on one sentence of a 1930 address, after the working years (1897–1909). If his physics memoirs (kinetic gas theory, radiation; S1) are listed as lasting, he becomes a scientist and P35 gives the same B 3 at 0.5. Lead for A: Constance Reid's Hilbert (1970), not read."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "German (East Prussian)", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1897–1909", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "First to last dated listed lasting contribution (P29, P30)."}
  age_at_first_lasting_contribution: {value: 35, certainty: 0.5, cites: [{source: S1, locator: "opening; 1897"}], how_known: "1897 − 1862 = 35 (P30)."}
  first_evidence_of_lio_type_views: {value: "1930: 'überall die Einheit der Naturgesetze'", year: 1930, certainty: 0.5, cites: [{source: S2, locator: "address"}], how_known: "Earlier writings not read for this (P30 #7)."}
  lio_views_relative_to_major_work: {value: "after major work", certainty: 0.5, cites: [{source: S2, locator: "address"}], how_known: "1930, after 1909; earlier writings not read."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Nothing read from 1897–1909."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "Axiomatic method in geometry (S1); a mathematical style, not a theology.", certainty: 0.5, cites: [{source: S1, locator: "Grundlagen sentence"}], how_known: "Coder's reading."}
  form_acquired: {value: "through the profession", certainty: 0.5, cites: [{source: S1, locator: "Grundlagen sentence"}], how_known: "Coder's reading."}
  circle_present: {value: "unclear", rationale: "Nothing read on God.", certainty: 0.5, cites: [{source: S2, locator: "address"}], how_known: "Coder's reading."}
  reading: "Unity of nature's laws; mathematics as their 'pre-established harmony'."
  notes: ""

institutions:
  - {value: "University of Königsberg", role: "Privatdozent, then professor", years: "1886–1895", kind: university, certainty: 0.7, cites: [{source: S1, locator: "career paragraph"}], how_known: "Britannica."}
  - {value: "University of Göttingen", role: "professor of mathematics", years: "1895–1930", kind: university, certainty: 0.7, cites: [{source: S1, locator: "career paragraph; 1930 retirement"}], how_known: "Britannica."}
collaborators:
  - {value: "Hermann Minkowski", relation: collaborator, note: "colleague and friend; mathematics applied to physics", certainty: 0.7, cites: [{source: S1, locator: "physics paragraph"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 91"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "B rests on one sentence read in a web transcription; translation the coder's."
  open_questions:
    - "Read Reid's biography for his religion (A)."
    - "Print check pending: check the address against Die Naturwissenschaften (1930), pp. 959–963."
    - "Lead: the same sentence may bear on E (the same laws everywhere); not scored."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Irving Kaplansky"
    citation: "Kaplansky, Irving. \"David Hilbert.\" Encyclopaedia Britannica. https://www.britannica.com/biography/David-Hilbert. Read in Wayback snapshot 20260131000341 (the 20260923142914 snapshot was empty)."
    url: "https://www.britannica.com/biography/David-Hilbert"
    accessed: 2026-10-17
    reliability_note: "Signed article. Body only; Quick Facts not cited."
    used_for: [identity, basics, contribution, childhood, timing, lane_b, institutions, collaborators]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "David Hilbert"
    citation: "Hilbert, David. \"Naturerkennen und Logik.\" Die Naturwissenschaften (28 November 1930), pp. 959–963. Read in the transcription at https://www.rschr.de/Htm/David_Hilbert_Naturerkennen_und_Logik.htm"
    url: "https://www.rschr.de/Htm/David_Hilbert_Naturerkennen_und_Logik.htm"
    accessed: 2026-10-17
    reliability_note: "Unofficial web copy of the printed address, read directly; web-copy cap 0.7 (CODING_GUIDE §7); print check pending."
    used_for: [worldview, timing, lane_b]
  - id: S3
    type: secondary
    kind: other
    author: "J J O'Connor and E F Robertson"
    citation: "O'Connor, J. J., and E. F. Robertson. \"David Hilbert.\" MacTutor History of Mathematics Archive (last update November 2014). https://mathshistory.st-andrews.ac.uk/Biographies/Hilbert/"
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Hilbert/"
    accessed: 2026-10-17
    reliability_note: "Signed biography; searched for religion, nothing found."
    used_for: [worldview]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-17
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# David Hilbert

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

David Hilbert (1862–1943), German mathematician [S1]. Draft: primary_system UNKNOWN; A UNKNOWN; B 3 at 0.5 (alt 4); mid_basin UNKNOWN. Not plotted.

## Life and work

Königsberg, then Göttingen from 1895 [S1].

## Contribution and impact

Invariants, Zahlbericht (1897), Grundlagen der Geometrie (1899), the 23 problems (1900), integral equations (1909) [S1].

## Childhood and education

Not read.

## Adult working worldview

'überall die Einheit der Naturgesetze' (1930) [S2]; nothing read on religion [S3].

## Heritage (context only)

East Prussian [S1].

## Timing

First lasting contribution 1897, at 35 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Axiomatic style [S1].

## Open questions

- Reid's biography for A.

## Research log

- 2026-10-17: Read Britannica (Kaplansky; Wayback 20260131000341), MacTutor and a transcription of 'Naturerkennen und Logik' directly; the psiquadrat.de scan timed out from the box.
