---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch F)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-15
  change_log:
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch F, order P32: F 5, rank 35). Basics from SEP (Heinzmann and Stump) and MacTutor (O'Connor and Robertson). A scientist under P30 (three-body problem, celestial mechanics). No statement of his own on God or on exceptions in nature was read; the 'free thinker at 18' claim is from an unsigned popular site and is not cited. primary_system and A UNKNOWN; B 3 at 0.5 from working science (P24, P35; alternative 4); C, D UNKNOWN; E BELOW_THRESHOLD (P19); mid_basin UNKNOWN. Draft, not reviewed."}

identity:
  id: poincare-henri
  display_name: "Henri Poincaré"
  roster:
    canonical_name: "Henri Poincaré"
    rank: 35
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: mathematics
    field_bucket: mathematics
  full_name: {value: "Jules Henri Poincaré", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP alone."}
  native_name: {value: UNKNOWN, how_known: "French in Latin script."}
  aliases:
    - {name: "Henri-Poincare", kind: "roster alias"}
    - {name: "Poincaré-Henri", kind: "roster alias"}

basics:
  birth:
    date: {value: "1854-04-29", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "Quick Info"}], how_known: "SEP and MacTutor agree (P15)."}
    place: {value: "Nancy, Lorraine, France", modern_name: "Nancy, France", polity_then: "France (Second Empire)", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "Quick Info"}], how_known: "SEP and MacTutor agree (P15)."}
  death:
    date: {value: "1912-07-17", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "Quick Info"}], how_known: "SEP and MacTutor agree (P15)."}
    place: {value: "Paris, France", modern_name: "Paris, France", polity_then: "France (Third Republic)", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "Quick Info"}], how_known: "SEP and MacTutor agree (P15)."}
  first_lasting_contribution_year: {value: 1882, certainty: 0.7, cites: [{source: S1, locator: "§5 ('theory of Fuchsian functions in 1882 (Poincaré 1882: 1167)')"}], how_known: "Earliest listed lasting contribution (P13). SEP cites a 1882 publication; his first Comptes rendus notes may be earlier (not read), so the year might be earlier."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S1, locator: "§5"}], how_known: "From 1882 (P2); any earlier note would also fall after 1850."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "France (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "Caen, then Paris."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [French], certainty: 0.7, cites: [{source: S1, locator: "§2 (La Science et l'hypothèse)"}], how_known: "SEP."}
  occupations: {value: ["mathematician", "mathematical physicist", "philosopher of science", "mine engineer"], certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}

contribution:
  fields: {value: ["mathematics", "celestial mechanics", "mathematical physics", "philosophy of science"], certainty: 0.7, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "Biography"}], how_known: "SEP and MacTutor."}
  lasting_original_contributions:
    - {value: "Theory of Fuchsian (automorphic) functions", year: 1882, kind: theory, lasting: "later called automorphic functions (S2)", certainty: 0.7, cites: [{source: S1, locator: "§5"}, {source: S2, locator: "Biography (Fuchsian functions)"}], how_known: "SEP dates it 1882; MacTutor describes it."}
    - {value: "Prize memoir on the three-body problem: stability of such systems cannot in general be demonstrated; recurrence theorem", year: 1889, kind: theory, lasting: "'a founding document in chaos theory' (S1)", certainty: 0.7, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "Biography (Birthday Competition)"}], how_known: "SEP gives the 1889 prize; the submission was earlier but its date was not read, so the year might be earlier (§8)."}
    - {value: "La Science et l'hypothèse (Science and Hypothesis), conventionalism", year: 1902, kind: work, lasting: "his geometric conventionalism is still debated (S1)", certainty: 0.7, cites: [{source: S1, locator: "§2, §4"}], how_known: "SEP."}
    - {value: "Poincaré conjecture", year: 1904, kind: other, lasting: "a major unsolved problem until Perelman (S1)", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
    - {value: "The three philosophical books (Science and Hypothesis, The Value of Science, Science and Method) completed", year: 1908, kind: work, lasting: "basis of his election to the Académie française in 1908 (S1)", certainty: 0.5, cites: [{source: S1, locator: "§1 ('elected to the Académie Française in 1908 on the basis of his three books')"}], how_known: "Listed so the span does not leave out his last major public work (P30 addendum). SEP gives 1908 for the election; the third book's year is inferred to be no later than 1908 (0.5)."}
  evidence_of_impact:
    - {value: "Prize of the King of Sweden (1889); President of the Academy of Sciences (1906); Académie française (1908)", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Founding work in topology and chaos theory (S1, S2).", certainty: 0.7, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "Summary"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father Léon Poincaré, professor of medicine at Nancy; mother Eugénie Launois", role: parents, certainty: 0.7, cites: [{source: S1, locator: "§1"}, {source: S2, locator: "Biography"}], how_known: "SEP and MacTutor."}
  household_circumstances: {value: TODO}
  schooling:
    - {value: "Lycée in Nancy", stage: "grammar or secondary school", run_by: "state or municipal", years: "1862–1873", ages: "8–19", certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor ('eleven years at the Lycée')."}
    - {value: "École Polytechnique, then École des Mines", stage: university, run_by: "state or municipal", years: "1873–", ages: "19–", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP (graduated Polytechnique 1875)."}
  early_mathematics: {value: "other", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP: preparatory classes in mathematics and first in the national concours général in elementary mathematics after 1871, before entering Polytechnique in 1873; level beyond that not stated."}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: TODO}
  notable_events:
    - {value: "German occupation of Nancy; family billeted a German official", year: 1870, age: 16, certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1882–1908", certainty: 0.5, cites: [{source: S1, locator: "§1, §5"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "SEP and MacTutor read; neither gives a statement of his on religion. A 2024 article (Transversal) reports his 1909 remarks on Catholics and secularists (via search excerpt) but they are about the freedom of inquiry, not his own belief."}
  primary_system: {value: UNKNOWN, how_known: "No statement of his own on God read. A popular site (famousscientists.org, unsigned) says he called himself a free thinker by 18; not citable (RUNBOOK §3.1) and not followed to a source."}
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: AGNOS, reason: "Possible from the unsourced 'free thinker' report; not coded."}
    - {code: CHRIST, reason: "Catholic family per the same popular site; heritage only."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Nothing in his own words read."}
    B_cause:
      value: 3
      basis: inference_from_work
      certainty: 0.5
      cites: [{source: S1, locator: "§1 (three-body problem; recurrence theorem)"}, {source: S2, locator: "Biography (celestial mechanics, physics topics)"}]
      how_known: "Coder's reading of his working science (P24, P30): celestial mechanics and mathematical physics are results about physical systems, so he is a scientist. No statement of his own on law and exception read."
      rationale: "Scored on his account of nature (P6), which for a scientist is the working science: deterministic mechanics with no exception, miracle or petition. P35: B inferred only from working science is B 3 at 0.5 with 4 as the named alternative, never 4. P40 does not apply: no statement read that rules out exceptions or chance. Named alternative: 4."
    C_ledger: {value: UNKNOWN, how_known: "Nothing read (P19)."}
    D_authority: {value: UNKNOWN, how_known: "Nothing on revelation; working science does not bear on D (P19)."}
    E_scope: {value: BELOW_THRESHOLD, note: "Scored on the world's order (P7). Working science bears on E's first question but E is not scored from it alone (P19).", how_known: "BELOW_THRESHOLD under P19: not scored from working science alone."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, which takes precedence (§6, P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "Coder's call: his essay on chance (Science and Method) and the 1909 remarks on religion were not read in a citable text, so no statement is used. His conventionalism about geometry and laws is not a claim about exceptions in nature and does not move B."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "French (Lorraine)", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1882–1908", certainty: 0.5, cites: [{source: S1, locator: "§1, §5"}], how_known: "1882 to 1908, first to last listed lasting contribution (P29, P30); the end year is inferred (0.5)."}
  age_at_first_lasting_contribution: {value: 28, certainty: 0.7, cites: [{source: S1, locator: "§1, §5"}], how_known: "1882 − 1854 = 28 (P30)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "B is inferred from working science, which is not an LIO-type view (P27)."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "No statement read."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Nothing read."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "Top of his class in mathematics; École Polytechnique.", certainty: 0.5, cites: [{source: S1, locator: "§1"}], how_known: "Coder's reading."}
  form_acquired: {value: "childhood or adolescence", certainty: 0.5, cites: [{source: S1, locator: "§1 (teacher's remark at age 13)"}], how_known: "Coder's reading."}
  circle_present: {value: "unclear", rationale: "No statement on God and nature.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No reading possible: worldview not documented in the sources read."
  notes: ""

institutions:
  - {value: "University of Paris, Faculty of Sciences", role: professor, years: "1881–1912", kind: university, certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
  - {value: "Bureau des Longitudes", role: member, years: "1893–1912", kind: "government or state body", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
  - {value: "French Academy of Sciences", role: "member (1887), president (1906)", years: "1887–1912", kind: "academy or learned society", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
collaborators:
  - {value: "Gösta Mittag-Leffler", relation: correspondent, note: "fifty letters on the prize memoir, 1887–1890", certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 35"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags: []
  open_questions:
    - "Read Rollet's biographical work and Dernières pensées / 1909 remarks for any statement on religion; read 'Le hasard' (Science and Method) for P40."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Gerhard Heinzmann and David Stump"
    year: 2026
    citation: "Heinzmann, Gerhard, and David Stump. \"Henri Poincaré.\" Stanford Encyclopedia of Philosophy, first published 3 September 2013, substantive revision 10 September 2026. https://plato.stanford.edu/entries/poincare/."
    url: "https://plato.stanford.edu/entries/poincare/"
    accessed: 2026-10-15
    reliability_note: "Peer-reviewed reference article."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions]
  - id: S2
    type: secondary
    kind: encyclopedia
    author: "J. J. O'Connor and E. F. Robertson"
    year: 2003
    citation: "O'Connor, J. J., and E. F. Robertson. \"Henri Poincaré.\" MacTutor History of Mathematics, University of St Andrews, last update October 2003. https://mathshistory.st-andrews.ac.uk/Biographies/Poincare/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Poincare/"
    accessed: 2026-10-15
    reliability_note: "Signed biography."
    used_for: [basics, contribution, childhood, worldview, collaborators]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Henri Poincaré

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Henri Poincaré (1854–1912), French mathematician, physicist and philosopher of science: Fuchsian functions, the three-body problem, the Poincaré conjecture, conventionalism [S1, S2]. No statement of his own on God was read. Draft: primary_system and A UNKNOWN; B 3 at 0.5 from working science (alternative 4, P35); E BELOW_THRESHOLD; mid_basin UNKNOWN.

## Life and work

Nancy, Polytechnique, Mines; Caen, then the University of Paris; Academy of Sciences and Académie française [S1].

## Contribution and impact

Fuchsian functions (1882), the prize memoir on the three-body problem (1889), Science and Hypothesis (1902), the conjecture (1904) [S1, S2].

## Childhood and education

Lycée at Nancy; first in the concours général in mathematics [S1, S2].

## Adult working worldview

Not documented in the sources read. B rests on his working science only [S1].

## Heritage (context only)

French, from Lorraine [S1].

## Timing

First lasting contribution 1882, at 28 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Mathematical training from adolescence [S1]; circle unclear.

## Open questions

- Rollet; 1909 remarks; 'Le hasard'.

## Research log

- 2026-10-15: Read SEP and MacTutor; web search on his religion found only an unsigned popular site and a 2024 article excerpt; neither used for a score.
