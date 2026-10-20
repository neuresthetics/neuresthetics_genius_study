---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z3)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z3 audit fixes (blind audit /workspace/genius_study_audit/gs_0b45e66_Z3/run1/), v8's call on the auditor's advice: Z3-23 (FAIL, RQ-Z3-1): under P31 the agnostic phase covers 2 of 3 listed lasting works, so primary_system PANENT 0.5 -> BELOW_THRESHOLD (lead AGNOS), A 2 -> BELOW_THRESHOLD, B 3 -> UNKNOWN, D and E -> UNKNOWN, mid_basin -> UNKNOWN; process theism (PANENT 0.5, A 2, B 3) moved to changes_over_life with the delta in coder_notes. Z3-21: the agnostic phase's end is marked as the coder's inference. Z3-22: not a scientist under P30 #11. No longer plotted."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z3, order P32: F 3, rank 145). Sources: SEP 'Alfred North Whitehead' (Desmet and Irvine, rev. 2022) with his own words as secondary quotations (primary check pending, §7); MacTutor (O'Connor and Robertson). Anglican upbringing; agnostic from the mid-1890s (MacTutor); process theism in Science and the Modern World (1925), Religion in the Making (1926) and Process and Reality (1929), all inside the span: 'Apart from the intervention of God, there could be nothing new in the world, and no order in the world' (PR 247); each occasion 'conditioned, though not determined' by God's initial aim (PR 108). A scientist (P30: applied mathematics, an alternative theory of gravitation). Span 1898–1929. primary_system PANENT (0.5, alt BELOW_THRESHOLD); A 2 (0.5, alt 1); B 3 (0.5, alt 4); C UNKNOWN; D BELOW_THRESHOLD; E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Plotted (faded) at the next chart refresh. RQ-Z3-1: which phase of the span governs. Draft, not reviewed."}

identity:
  id: whitehead-alfred-north
  display_name: "Alfred North Whitehead"
  roster:
    canonical_name: "Alfred North Whitehead"
    rank: 145
    F: 3
    models: [Claude, DeepSeek, Gemini]
    band: "core (3–4)"
    status: core
    field: mathematics
    field_bucket: mathematics
  full_name: {value: "Alfred North Whitehead", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}
  native_name: {value: "Alfred North Whitehead", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}
  aliases:
    - {name: "Whitehead-Alfred North", kind: "roster alias"}

basics:
  birth:
    date: {value: "1861-02-15", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "§1 chronology"}, {source: S2, locator: "Quick Info"}], how_known: "SEP; MacTutor."}
    place: {value: "Ramsgate, Isle of Thanet, Kent, England", modern_name: "Ramsgate, Kent, United Kingdom", polity_then: "United Kingdom", certainty: 0.7, cites: [{source: S1, locator: "§1 chronology"}], how_known: "SEP."}
  death:
    date: {value: "1947-12-30", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "§1 chronology"}], how_known: "SEP."}
    place: {value: "Cambridge, Massachusetts", modern_name: "Cambridge, Massachusetts, United States", polity_then: "United States", certainty: 0.7, cites: [{source: S1, locator: "§1 chronology"}], how_known: "SEP."}
  first_lasting_contribution_year: {value: 1898, certainty: 0.7, cites: [{source: S1, locator: "§2 ('Whitehead's 1898 A Treatise on Universal Algebra had resulted in his election to the Royal Society')"}], how_known: "A Treatise on Universal Algebra (1898)."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "§2"}], how_known: "1898 (P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "United Kingdom (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.5, cites: [{source: S1, locator: "§1"}], how_known: "Cambridge and London 1884–1924; Harvard (North America) from 1924, which holds the last five years of the span; 0.5."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "SEP."}
  occupations: {value: ["mathematician", "philosopher", "professor (Trinity College Cambridge; University College London; Imperial College; Harvard)"], certainty: 0.7, cites: [{source: S1, locator: "opening; §1"}], how_known: "SEP."}

contribution:
  fields: {value: ["mathematics", "logic", "philosophy of science", "metaphysics", "philosophy of education"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}
  lasting_original_contributions:
    - {value: "A Treatise on Universal Algebra", year: 1898, kind: work, lasting: "led to his election to the Royal Society (S1)", certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "SEP."}
    - {value: "Principia Mathematica (with Bertrand Russell)", year: 1910, kind: work, lasting: "'the landmark three-volume Principia Mathematica (1910, 1912, 1913)' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}
    - {value: "Process philosophy (Process and Reality)", year: 1929, kind: theory, lasting: "'pioneering the approach to metaphysics now known as process philosophy' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; §6"}], how_known: "SEP."}
  evidence_of_impact:
    - {value: "Order of Merit, 1945", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "§1 chronology"}], how_known: "SEP."}
  major_works:
    - {value: "Science and the Modern World", year: 1925, kind: book, certainty: 0.7, cites: [{source: S1, locator: "§7"}], how_known: "SEP."}
    - {value: "Religion in the Making", year: 1926, kind: book, certainty: 0.7, cites: [{source: S1, locator: "§6; §7"}], how_known: "SEP."}
  honours:
    - {value: "Fellow of the Royal Society", year: 1903, certainty: 0.7, cites: [{source: S1, locator: "§1 chronology"}], how_known: "SEP."}
  definition_fit: {value: "clearly meets", rationale: "Co-author of Principia Mathematica and founder of process philosophy (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Anglican (father an Anglican clergyman)", certainty: 0.7, cites: [{source: S2, locator: "Biography, opening"}], how_known: "MacTutor."}
  family_religious_practice: {value: "Raised in his father's vicarage", certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor: 'brought up as an Anglican'."}
  parents_and_household:
    - {value: "Canon Alfred Whitehead, Anglican clergyman of Ramsgate", role: father, certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor."}
    - {value: "Maria Sarah Buckmaster", role: mother, certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor."}
  household_circumstances: {value: "Youngest of four children in a vicarage", certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor."}
  schooling:
    - {value: "Taught at home by his father until 14", stage: home, run_by: family, years: "to 1875", certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor."}
    - {value: "Sherborne School", stage: "grammar or secondary school", run_by: other, years: "1875–1880", certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor ('Sherbourne Independent School')."}
    - {value: "Trinity College, Cambridge", stage: university, run_by: other, years: "1880–1884", certainty: 0.7, cites: [{source: S1, locator: "§1 chronology"}], how_known: "SEP."}
  early_mathematics: {value: "other", note: "a little from his father; special gift shown at Sherborne", certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["English", "Latin", "Greek"], certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor: Latin from 10, Greek from 12."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1898–1929", certainty: 0.7, cites: [{source: S1, locator: "§2; §6"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "'You cannot shelter theology from science, or science from theology' (Religion in the Making, 1926); aims at their integration", certainty: 0.5, cites: [{source: S1, locator: "§7 (1926 [1996: 79])"}], how_known: "Secondary quotation."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "P31 (v8's call on the auditor's advice, RQ-Z3-1): the change from agnostic to process theist falls inside the span 1898–1929, so the codes follow the phase covering most listed lasting works: agnostic, 2 (1898, 1910) against theist, 1 (1929). Lead AGNOS, supported only by MacTutor's summary ('became an agnostic around the mid 1890s', S2); no own words of that phase read."}
  secondary_system: {value: UNKNOWN, how_known: "None; process theism is recorded in changes_over_life."}
  candidate_codes_considered:
    - {code: AGNOS, reason: "Lead for the coded agnostic phase (S2); summary only, so BELOW_THRESHOLD (P31, RQ-Z3-1)."}
    - {code: PANENT, reason: "The 1925–1929 process theism (S1 §6–§7); the minority phase under P31, kept in changes_over_life."}
    - {code: CHRIST, reason: "Rejected: chose neither Anglican nor Catholic Church (S2)."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "Agnostic phase coded (P31): an agnostic with no stated locus view (P20). The theist phase's A 2 (0.5) is in coder_notes."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist under P30 #11: his listed lasting works (Universal Algebra, Principia Mathematica, process philosophy) are mathematics, logic and metaphysics; the 1922 gravitation theory and 1925 atom outline are not listed or called lasting (as Tao, Hilbert). His own statements on nature belong to the theist phase."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read on reward and punishment (P19)."}
    D_authority: {value: UNKNOWN, how_known: "Nothing read from the agnostic phase; the integration view (S1 §7) is the theist phase."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read from the agnostic phase."}
  mid_basin: {value: UNKNOWN, how_known: "B_cause is UNKNOWN, which takes precedence (§6, P19)."}
  statements:
    - text: "Apart from the intervention of God, there could be nothing new in the world, and no order in the world. The course of creation would be a dead level of ineffectiveness, with all balance and intensity progressively excluded by the cross currents of incompatibility."
      cites: [{source: S1, locator: "§6 (1929c [1985: 247])"}]
      date: "1929"
      context: "Process and Reality, Part V; quoted in SEP."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-19
      note: "Primary check pending."
    - text: "Religion is the vision of something which stands beyond, behind, and within, the passing flux of immediate things"
      cites: [{source: S1, locator: "§7 (1925 [1967: 191–192])"}]
      date: "1925"
      context: "Science and the Modern World; quoted in SEP."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-19
      note: "Primary check pending."
  changes_over_life:
    - {value: "Anglican upbringing; drawn toward Rome c. 1889–90, debating for seven years; 'chose neither and became an agnostic around the mid 1890s', mainly because of developments in science", certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor."}
    - {value: "Process theism in the Harvard works of 1925–1929 (would code PANENT 0.5, A 2 at 0.5, B 3 at 0.5); the agnostic phase's end before 1925 is the coder's inference, not MacTutor's", year: 1925, certainty: 0.5, cites: [{source: S1, locator: "§6; §7"}], how_known: "SEP; the end date of the agnostic phase is inferred."}
  coder_notes: "RQ-Z3-1 answered (v8's call on the auditor's advice, P31): coded on the agnostic phase (mid-1890s per MacTutor; its running into the 1920s is the coder's inference, MacTutor gives no end date), which covers 2 of 3 listed lasting works. Delta if the theist phase were coded: primary PANENT 0.5, A 2 (alt 1), B 3 (alt 4), mid_basin BELOW_THRESHOLD, plotted. The result flips only if Science and the Modern World (1925) and Religion in the Making (1926) were both listed as lasting."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "English", certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor."}
  religious_heritage_by_birth: {value: "Anglican", certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1898–1929", certainty: 0.7, cites: [{source: S1, locator: "§2; §6"}], how_known: "Universal Algebra (1898) to Process and Reality (1929) (P29, P30)."}
  age_at_first_lasting_contribution: {value: 37, certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "1898 − 1861 = 37 (P30)."}
  first_evidence_of_lio_type_views: {value: "1925 (Science and the Modern World), after the coded phase", certainty: 0.5, cites: [{source: S1, locator: "§7"}], how_known: "Secondary quotation."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.5, cites: [{source: S1, locator: "§6"}], how_known: "Process theism arrives with the last listed lasting work (1929); the coded phase is agnostic (P31)."}
  worldview_during_major_work: {value: "Agnostic (coder's inference that it ran to the mid-1920s), then process theist", certainty: 0.5, cites: [{source: S2, locator: "Biography"}, {source: S1, locator: "§6"}], how_known: "MacTutor; SEP; end of agnostic phase inferred."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "Universal algebra, logic and geometry (S1 §2).", certainty: 0.7, cites: [{source: S1, locator: "§2"}], how_known: "SEP."}
  form_acquired: {value: "adulthood, before major work", certainty: 0.5, cites: [{source: S2, locator: "Biography"}], how_known: "Cambridge Tripos."}
  circle_present: {value: "partly", rationale: "God 'within' the flux and beyond it (panentheist, not identity with nature).", certainty: 0.5, cites: [{source: S1, locator: "§7"}], how_known: "Coder's reading."}
  reading: "Formal mathematics followed by a God-in-and-beyond-the-world metaphysics."
  notes: ""

institutions:
  - {value: "Trinity College, Cambridge", role: "Fellow and lecturer in mathematics", years: "1884–1910", kind: university, certainty: 0.7, cites: [{source: S1, locator: "§1 chronology"}], how_known: "SEP."}
  - {value: "Imperial College of Science and Technology", role: "Professor of Applied Mathematics", years: "1914–1924", kind: university, certainty: 0.7, cites: [{source: S1, locator: "§1 chronology"}], how_known: "SEP."}
  - {value: "Harvard University", role: "Professor of Philosophy", years: "1924–1937", kind: university, certainty: 0.7, cites: [{source: S1, locator: "§1 chronology"}], how_known: "SEP."}
collaborators:
  - {value: "Bertrand Russell", roster_id: russell-bertrand, relation: collaborator, note: "Principia Mathematica", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 145"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Religious views read only via SEP quotations and MacTutor."
  open_questions:
    - "RQ-Z3-1; check the PR and SMW quotations in print."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Ronald Desmet and Andrew David Irvine"
    citation: "Desmet, Ronald, and Andrew David Irvine. \"Alfred North Whitehead.\" Stanford Encyclopedia of Philosophy (first published 1996; substantive revision 10 November 2022). https://plato.stanford.edu/entries/whitehead/"
    url: "https://plato.stanford.edu/entries/whitehead/"
    accessed: 2026-10-19
    reliability_note: "Signed scholarly reference; quotes his works with page references."
    used_for: [identity, basics, contribution, childhood, worldview, timing, lane_b, institutions, collaborators]
  - id: S2
    type: secondary
    kind: database
    author: "J J O'Connor and E F Robertson"
    citation: "O'Connor, J J, and E F Robertson. \"Alfred North Whitehead.\" MacTutor History of Mathematics, University of St Andrews. https://mathshistory.st-andrews.ac.uk/Biographies/Whitehead/"
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Whitehead/"
    accessed: 2026-10-19
    reliability_note: "Signed biographical database entry, drawing on Lowe's biography."
    used_for: [basics, childhood, worldview, heritage, timing, lane_b]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [review]
---

# Alfred North Whitehead

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Alfred North Whitehead (1861–1947), British mathematician and philosopher [S1]. Draft: primary BELOW_THRESHOLD (lead AGNOS); A BELOW_THRESHOLD; B UNKNOWN (not a scientist, P30 #11); C, D, E UNKNOWN; mid_basin UNKNOWN. Not plotted (P31, RQ-Z3-1).

## Life and work

Ramsgate, Cambridge, London, Harvard [S1].

## Contribution and impact

Universal Algebra (1898), Principia (1910–13), Process and Reality (1929) [S1].

## Childhood and education

Anglican vicarage; Sherborne; Trinity [S2].

## Adult working worldview

Agnostic from the mid-1890s (its end before 1925 is the coder's inference); process theism from 1925 [S2; S1, §6–§7]. Coded on the agnostic phase under P31.

## Heritage (context only)

Anglican [S2].

## Timing

1898–1929, from age 37 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Partly a circle [S1].

## Open questions

- RQ-Z3-1.

## Research log

- 2026-10-19: Read SEP (Desmet and Irvine) and MacTutor.
