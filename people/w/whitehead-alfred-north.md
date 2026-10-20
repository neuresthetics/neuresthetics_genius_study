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
  primary_system:
    value: PANENT
    basis: written_profession
    certainty: 0.5
    cites: [{source: S1, locator: "§6 (1929c [1985: 67, 88, 105, 108, 247]); §7 (1925 [1967: 191–192])"}]
    how_known: "His published metaphysics (1925–1929, inside the span), as quoted in SEP: God is 'the organ of novelty' and order, whose initial aim is felt by every occasion; religion is 'the vision of something which stands beyond, behind, and within, the passing flux of immediate things' (1925). Secondary quotations, and agnostic for most of the span (S2), so 0.5. SEP's PANENT record lists Whitehead's process philosophy as a source of modern panentheism."
    rationale: "PANENT use_when: a divine reality that includes the world and also exceeds it ('beyond, behind, and within'). Alternative BELOW_THRESHOLD: agnostic from the mid-1890s to the 1920s (RQ-Z3-1)."
  secondary_system: {value: UNKNOWN, how_known: "AGNOS for 1890s–1920s; see changes_over_life."}
  candidate_codes_considered:
    - {code: PANENT, reason: "Coded at 0.5 (S1 §6–§7)."}
    - {code: AGNOS, reason: "His stance for most of the span by MacTutor's account (S2); RQ-Z3-1."}
    - {code: CHRIST, reason: "Rejected: chose neither Anglican nor Catholic Church (S2)."}
  lio_axes:
    A_locus:
      value: 2
      basis: written_profession
      certainty: 0.5
      cites: [{source: S1, locator: "§6 (PR 105, 108, 247); §7 (SMW 191–192)"}]
      how_known: "Secondary quotations: God supplies each occasion's 'initial subjective aim' as 'the ground of all order and originality' (PR 108), and 'His tenderness is directed towards each actual occasion, as it arises' (PR 105). Primary check pending."
      rationale: "God in the world and beyond it, neither a separate creator nor identical with nature: the middle, 2. Alternative 1: God as a distinct actual entity with a purpose."
      alternatives:
        - {value: 1, note: "God as a distinct, purposing entity.", cites: [{source: S1, locator: "§6"}]}
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.5
      cites: [{source: S1, locator: "§6 (PR 88, 108, 247); §3"}]
      how_known: "Two routes at 0.5: (1) a scientist (P30: applied mathematics, an alternative theory of gravitation to Einstein's, S1 §3), B 3 alt 4 (P35); (2) his own words via SEP: 'Apart from the intervention of God, there could be nothing new in the world, and no order in the world' (PR 247), but each occasion is 'conditioned, though not determined' by God's aim and 'finally responsible for the decision' (PR 88, 108): lawful order with persuasive divine input and self-determination (P30 #14 by analogy)."
      rationale: "Not 4: God's 'intervention' and self-determination are named. Not 2: no miracles, the input is the ground of order. Alternative 4."
      alternatives:
        - {value: 4, note: "P35 alternative.", cites: [{source: S1, locator: "§3"}]}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read on reward and punishment (P19)."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "Seeks integration of science and religion (S1 §7); no ranking."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "God's aim reaches 'each actual occasion' (PR 105), a lead toward a universal order, but read only via SEP."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A 2 is in neither branch; certainties 0.5 (P10)."}
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
    - {value: "Process theism in the Harvard works of 1925–1929", certainty: 0.5, cites: [{source: S1, locator: "§6; §7"}], how_known: "SEP."}
  coder_notes: "RQ-Z3-1 for v8: the span (1898–1929) holds an agnostic phase (mid-1890s to the 1920s, S2) and a process-theist phase (1925–1929, the works that define his metaphysics). Coded on the published theism, the only written religious position read, at 0.5. Under the agnostic reading all three are BELOW_THRESHOLD and he is not plotted (result-changing)."

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
  first_evidence_of_lio_type_views: {value: "1925 (Science and the Modern World)", certainty: 0.5, cites: [{source: S1, locator: "§7"}], how_known: "Secondary quotation."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.5, cites: [{source: S1, locator: "§6"}], how_known: "The metaphysics is itself the last lasting work."}
  worldview_during_major_work: {value: "Agnostic, then process theist from the mid-1920s", certainty: 0.5, cites: [{source: S2, locator: "Biography"}, {source: S1, locator: "§6"}], how_known: "MacTutor; SEP."}

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

Alfred North Whitehead (1861–1947), British mathematician and philosopher [S1]. Draft: PANENT (0.5, alt BELOW_THRESHOLD); A 2 (0.5, alt 1); B 3 (0.5, alt 4); C UNKNOWN; D, E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Plotted (faded) at the next chart refresh. RQ-Z3-1.

## Life and work

Ramsgate, Cambridge, London, Harvard [S1].

## Contribution and impact

Universal Algebra (1898), Principia (1910–13), Process and Reality (1929) [S1].

## Childhood and education

Anglican vicarage; Sherborne; Trinity [S2].

## Adult working worldview

Agnostic from the mid-1890s; process theism from 1925 [S2; S1, §6–§7].

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
