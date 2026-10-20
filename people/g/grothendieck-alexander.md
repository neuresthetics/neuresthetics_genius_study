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
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z3, order P32: F 3, rank 144). Basics from MacTutor (O'Connor and Robertson). Own voice: La Clef des songes (1987; typescript transcribed by Mateo Carmona), his retrospective of his relation to God: atheist parents; in March 1944, aged nearly 16, he accepted 'cette Intelligence souveraine, infinie, créatrice de la Vie et ... de l'Univers tout entier, et des lois qui le régissent' and called himself 'déiste' (§§30–31), a view held 'ma vie durant' without doubt; he saw 'aucun signe d'une intervention de Dieu dans le présent' but an Intelligence that 'intervient' at each great evolutionary leap (§30). Span 1953–1970 (end at 0.5), age 25. primary_system DEISM (0.5, alt BELOW_THRESHOLD); A 1 (0.5, alt 0); B 3 (0.5, alt 4); C UNKNOWN; D BELOW_THRESHOLD; E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Plotted (faded) at the next chart refresh. Draft, not reviewed."}

identity:
  id: grothendieck-alexander
  display_name: "Alexander Grothendieck"
  roster:
    canonical_name: "Alexander Grothendieck"
    rank: 144
    F: 3
    models: [Claude, Gemini, GPT]
    band: "core (3–4)"
    status: core
    field: mathematics
    field_bucket: mathematics
  full_name: {value: "Alexander Grothendieck", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor; birth registered as Alexander Raddatz."}
  native_name: {value: "Alexander Grothendieck", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor; 'Alexandre' in France."}
  aliases:
    - {name: "Alexander-Grothendieck", kind: "roster alias"}
    - {name: "Grothendieck-Alexander", kind: "roster alias"}
    - {name: "Alexandre Grothendieck", kind: transliteration}
    - {name: "Alexander Raddatz", kind: "birth name"}

basics:
  birth:
    date: {value: "1928-03-28", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "Quick Info"}], how_known: "MacTutor."}
    place: {value: "Berlin", modern_name: "Berlin, Germany", polity_then: "Germany (Weimar Republic)", certainty: 0.7, cites: [{source: S1, locator: "Quick Info; Biography"}], how_known: "MacTutor."}
  death:
    date: {value: "2014-11-13", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "Quick Info"}], how_known: "MacTutor."}
    place: {value: "Saint-Girons", modern_name: "Saint-Girons, Ariège, France", polity_then: "France", certainty: 0.7, cites: [{source: S1, locator: "Quick Info"}], how_known: "MacTutor."}
  first_lasting_contribution_year: {value: 1953, certainty: 0.7, cites: [{source: S1, locator: "Biography (thesis defended 28 February 1953)"}], how_known: "Doctoral thesis on topological tensor products and nuclear spaces, defended 1953; first on the list of his best-known contributions quoted by MacTutor."}
  era_bucket: {value: "1950 on", certainty: 1.0, cites: [{source: S1, locator: "Biography"}], how_known: "1953 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "Quick Info"}], how_known: "Germany (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "Nancy, Paris (IHES), Montpellier."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "As recorded."}
  languages_of_work: {value: ["French"], certainty: 0.7, cites: [{source: S1, locator: "Biography (titles)"}], how_known: "MacTutor."}
  occupations: {value: ["mathematician", "researcher (CNRS; IHES)", "professor (Montpellier)"], certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}

contribution:
  fields: {value: ["algebraic geometry", "functional analysis", "homological algebra", "category theory"], certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
  lasting_original_contributions:
    - {value: "Topological tensor products and nuclear spaces (thesis)", year: 1953, kind: theory, lasting: "first in the list of his best-known contributions quoted by MacTutor", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
    - {value: "Schemes, topoi, étale cohomology and the Séminaire de Géométrie Algébrique at the IHES", year: 1970, kind: "body of work", lasting: "'established the IHES as a world centre of algebraic geometry'; schemes allowed Weil's conjectures to be solved (S1)", certainty: 0.5, cites: [{source: S1, locator: "Biography (IHES 1959–70)"}], how_known: "MacTutor; a body of work across 1959–1970, dated by its end (P30 addendum on ranges); 0.5."}
  evidence_of_impact:
    - {value: "Fields Medal 1966", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
  major_works:
    - {value: "Récoltes et Semailles", year: 1985, kind: book, certainty: 0.7, cites: [{source: S1, locator: "Biography (1983–85)"}], how_known: "MacTutor."}
    - {value: "La Clef des songes", year: 1987, kind: book, certainty: 0.7, cites: [{source: S2, locator: "§1 (dated 30 April 1987)"}], how_known: "The text itself (MacTutor gives 1986)."}
  honours:
    - {value: "Fields Medal", year: 1966, certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor; declined the Crafoord Prize 1988."}
  definition_fit: {value: "clearly meets", rationale: "Founder of modern algebraic geometry (S1).", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "None: his parents were atheists", certainty: 0.7, cites: [{source: S2, locator: "§27 ('Mes parents étaient athées')"}], how_known: "His own words (1987)."}
  family_religious_practice: {value: "Fostered 1934–39 by the Hamburg pastor Wilhelm Heydorn", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
  parents_and_household:
    - {value: "Alexander Schapiro (Tanaroff), Russian Jewish anarchist, died at Auschwitz 1942", role: father, certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
    - {value: "Johanna (Hanka) Grothendieck, left-wing writer from Hamburg", role: mother, certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
  household_circumstances: {value: "Revolutionary émigré parents; foster family in Hamburg; internment camps in France", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
  schooling:
    - {value: "Elementary school and Gymnasium in Hamburg", stage: "grammar or secondary school", run_by: other, years: "1934–1939", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
    - {value: "Collège Cévenol, Le Chambon-sur-Lignon (baccalauréat 1945)", stage: "grammar or secondary school", run_by: private, years: "1942–1945", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
    - {value: "University of Montpellier; ENS Paris; Nancy (doctorate 1953)", stage: university, run_by: "state or municipal", years: "1945–1953", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
  early_mathematics: {value: "other", note: "dissatisfied with school definitions of length, area and volume; rediscovered the Lebesgue integral at Montpellier", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["German", "French"], certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "Berlin and Hamburg, then France from 1939."}
  notable_events:
    - {value: "In March 1944, aged nearly 16, after a talk on evolution by his science teacher Monsieur Friedel, became a 'déiste' and wrote so to his mother", year: 1944, certainty: 0.5, cites: [{source: S2, locator: "§§30–31"}], how_known: "His own retrospective (1987)."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1953–1970", certainty: 0.5, cites: [{source: S1, locator: "Biography"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "Mathematical laws are 'part of the very nature of God', accessible to reason alone (1987)", certainty: 0.5, cites: [{source: S2, locator: "§31, note 72"}], how_known: "His own words, after the span."}
  primary_system:
    value: DEISM
    basis: written_profession
    certainty: 0.5
    cites: [{source: S2, locator: "§§30–31"}]
    how_known: "'Alors que je me disais “athée” jusque-là, me voilà donc soudain changé de catégorie - dorénavant, je me dirai “déiste” !' (1944, as told in 1987); a Creator known by reason from the evolution of life, 'très loin du Dieu de la Promesse et de la Rétribution dont parle l'Ancien Testament'; the knowledge held 'ma vie durant'. Retrospective written 17 years after the span (P20), so 0.5."
    rationale: "DEISM use_when: a creator known by reason (design), with no ongoing involvement seen. P27: he set the Creator apart from the God of the Testaments but did not discuss revelation; alternative BELOW_THRESHOLD. Not coded on his post-1976 mystical theism (outside the span)."
  secondary_system: {value: UNKNOWN, how_known: "None for the span."}
  candidate_codes_considered:
    - {code: DEISM, reason: "Coded at 0.5 (S2 §§30–31)."}
    - {code: ATHE, reason: "Rejected: atheist only before 1944, by his account."}
    - {code: BUDDH, reason: "Rejected: contact with Buddhist monks in the 1970s, after the span (S2)."}
  lio_axes:
    A_locus:
      value: 1
      basis: written_profession
      certainty: 0.5
      cites: [{source: S2, locator: "§31"}]
      how_known: "'cette Intelligence souveraine, infinie, créatrice de la Vie et (cela allait alors de soi) créatrice aussi de l'Univers tout entier, et des lois qui le régissent' (§31). Retrospective (P20), 0.5."
      rationale: "A transcendent creator who stays apart from daily life: 1 (as DEISM). Alternative 0: an 'Intelligence' with an 'Intention'."
      alternatives:
        - {value: 0, note: "A personal creator with a Design.", cites: [{source: S2, locator: "§30"}]}
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.5
      cites: [{source: S2, locator: "§§30–31"}]
      how_known: "The Creator made the laws (§31) and he saw 'aucun signe d'une intervention de Dieu dans le présent' (§31); but the same Intelligence 'intervient de façon irrécusable, pour le moins, lors de chacun des grands “sauts” qualitatifs' of evolution (§30). Retrospective, 0.5."
      rationale: "Lawful nature with stated exceptions (evolutionary leaps): 3. Alternative 4: no intervention in the present."
      alternatives:
        - {value: 4, note: "'aucun signe d'une intervention de Dieu dans le présent'.", cites: [{source: S2, locator: "§31"}]}
    C_ledger: {value: UNKNOWN, how_known: "The Creator was far from 'the God of ... Retribution' (§31), a lead only (P19)."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "Reason alone grasps the Creator (§30); revelation not discussed for this period."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Nothing further read for the span."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A 1 and B 3 at 0.5 (P10)."}
  statements:
    - text: "Je comprenais bien que ce “Dieu” qu’on mettait à toutes les sauces pour Lui faire avaliser tout ce qu’on voulait, Il était en tous cas cette Intelligence souveraine, infinie, créatrice de la Vie et (cela allait alors de soi) créatrice aussi de l’Univers tout entier, et des lois qui le régissent."
      cites: [{source: S2, locator: "§31"}]
      date: "1987"
      context: "La Clef des songes, 'Les retrouvailles perdues': his conversion of March 1944, aged nearly 16."
      axes: [A_locus, B_cause]
      kind: "unpublished manuscript"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "Typescript transcribed by Carmona (provisional edition). Retrospective (P20)."
    - text: "Rien dans mon expérience directe ne me conduisait à penser que le Créateur, une fois mis en marche l’immense Manège de la Création, continuait encore à s’occuper de ce qui s’y passe et à y participer si peu que ce soit. [...] je ne percevais aucun signe d’une intervention de Dieu dans le présent."
      cites: [{source: S2, locator: "§31"}]
      date: "1987"
      context: "Same passage, on the deism of 1944 onward."
      axes: [B_cause]
      kind: "unpublished manuscript"
      verified_against: "primary transcription"
      verified_on: 2026-10-19
      note: "As above."
  changes_over_life:
    - {value: "Atheist upbringing; deist from 1944; mystical theism from 1976 (meditation, dreams: 'Dieu est le Rêveur')", certainty: 0.5, cites: [{source: S2, locator: "§§17, 27, 31"}], how_known: "His own retrospective."}
  coder_notes: "Span end 1970 (IHES body of work) at 0.5; Esquisse d'un programme (1983) is a later candidate (MacTutor lists it as a manuscript), which would put the post-1976 theism inside the span; flagged, not applied."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Russian Jewish (father) and German (mother)", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
  religious_heritage_by_birth: {value: "Jewish (paternal); none in practice", certainty: 0.5, cites: [{source: S1, locator: "Biography"}, {source: S2, locator: "§27"}], how_known: "MacTutor; his own account."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1953–1970", certainty: 0.5, cites: [{source: S1, locator: "Biography"}], how_known: "Thesis (1953) to the end of the IHES period (1970) (P29, P30); end at 0.5."}
  age_at_first_lasting_contribution: {value: 25, certainty: 0.7, cites: [{source: S1, locator: "Quick Info"}], how_known: "1953 − 1928 = 25 (P30 year difference; he was 24 at the February 1953 defence)."}
  first_evidence_of_lio_type_views: {value: "1944 (by his 1987 account)", certainty: 0.5, cites: [{source: S2, locator: "§31"}], how_known: "Retrospective."}
  lio_views_relative_to_major_work: {value: "before major work", certainty: 0.5, cites: [{source: S2, locator: "§31"}], how_known: "Deist from 1944."}
  worldview_during_major_work: {value: "Deist, of little personal consequence to him", certainty: 0.5, cites: [{source: S2, locator: "§31"}], how_known: "Retrospective."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "Algebraic geometry (S1).", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
  form_acquired: {value: "adulthood, before major work", certainty: 0.5, cites: [{source: S1, locator: "Biography"}], how_known: "Montpellier and Nancy."}
  circle_present: {value: "no", rationale: "A creator apart from daily life during the span (S2 §31).", certainty: 0.5, cites: [{source: S2, locator: "§31"}], how_known: "Coder's reading."}
  reading: "Deist creator of the laws; mathematics as 'part of the nature of God' only in 1987."
  notes: ""

institutions:
  - {value: "Institut des Hautes Études Scientifiques", role: professor, years: "1959–1970", kind: other, certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
  - {value: "University of Montpellier", role: professor, years: "1973–1988", kind: university, certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
collaborators:
  - {value: "Jean Dieudonné", relation: teacher, note: "Nancy", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
  - {value: "Laurent Schwartz", relation: teacher, note: "Nancy", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
  - {value: "Jean-Pierre Serre", relation: collaborator, note: "fellow student; Fields report", certainty: 0.7, cites: [{source: S1, locator: "Biography; references"}], how_known: "MacTutor."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 144"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Worldview for the span known only from a 1987 retrospective."
  open_questions:
    - "Span end (1970 or 1983)."

sources:
  - id: S1
    type: secondary
    kind: database
    author: "J J O'Connor and E F Robertson"
    citation: "O'Connor, J J, and E F Robertson. \"Alexander Grothendieck.\" MacTutor History of Mathematics, University of St Andrews (updated November 2014). https://mathshistory.st-andrews.ac.uk/Biographies/Grothendieck/"
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Grothendieck/"
    accessed: 2026-10-19
    reliability_note: "Signed biographical database entry."
    used_for: [identity, basics, contribution, childhood, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Alexandre Grothendieck"
    citation: "Grothendieck, Alexandre. La Clef des songes, ou Dialogue avec le bon Dieu (typescript, 1987). Provisional transcription ed. Mateo Carmona. https://geotoppos.org/divers/clef.pdf"
    url: "https://geotoppos.org/divers/clef.pdf"
    accessed: 2026-10-19
    reliability_note: "His own text, circulated in typescript; cited by section number."
    used_for: [childhood, worldview, heritage, timing, lane_b]
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

# Alexander Grothendieck

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Alexander Grothendieck (1928–2014), mathematician [S1]. Draft: DEISM (0.5, alt BELOW_THRESHOLD); A 1 (0.5, alt 0); B 3 (0.5, alt 4); C UNKNOWN; D, E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Plotted (faded) at the next chart refresh.

## Life and work

Berlin, Hamburg, French camps, Montpellier, Nancy, IHES [S1].

## Contribution and impact

Nuclear spaces; schemes and the IHES school; Fields Medal 1966 [S1].

## Childhood and education

Atheist parents; deist at nearly 16 by his own account [S2, §§27, 31].

## Adult working worldview

Deist during the span, by his 1987 retrospective [S2, §31].

## Heritage (context only)

Russian Jewish and German [S1].

## Timing

1953–1970, from age 25 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No circle in the span [S2].

## Open questions

- Span end.

## Research log

- 2026-10-19: Read MacTutor and La Clef des songes §§27–31.
