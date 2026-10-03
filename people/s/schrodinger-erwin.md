---
record:
  record_type: person
  schema_version: "1.2"
  record_version: 5
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, second batch: physical science 1600–1950)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages and transcriptions"
  collected_on: 2026-10-02
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (second batch, RUNBOOK §1 order). Basics from Britannica (Bernstein), MacTutor and the Nobel biography. Worldview from the epilogue of What is Life? (1944) and Mind and Matter (1958), read in two web transcriptions of the Cambridge edition, plus Britannica on My View of the World. Coded HINDU at 0.5 (stub system; PANT, IDEAL and PANENT named). A 4 (0.7), B 4 (1.0), C 4 (0.5), D 3 (0.5), E 4 (0.7). mid_basin false. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit, batch 2 (two blind runs at e648145). Finding #47: MacTutor's 'Although he was a Catholic' is about the adult in 1933, so family_religion and religious_heritage_by_birth are now TODO (were 'Catholic, per MacTutor' at 0.5); the adult nominal affiliation keeps the MacTutor statement at 0.7 (one reliable source, no dispute). Finding #45: region_of_work certainty 1.0 → 0.7, value unchanged (Western Europe, where wave mechanics was done); the 1935 cat paper (Oxford) and What is Life? (Dublin) were Northern Europe, now an alternative. region_of_birth stays 1.0 (Vienna, documented). Leading cut marked with [...] in one statement. Worldview scores unchanged. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "CODING_GUIDE §7 rule on unofficial web copies (Jason's decision, 2026-10-02): B_cause certainty 1.0 → 0.7. It rests on the rapeutation.com copy of the What is Life? epilogue (S4), and no authoritative edition was reachable to check the wording. mid_basin recomputed: value false (P4 test, A = 4) and certainty 0.7 = min(A 0.7, B 0.7), both unchanged; how_known updated."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Schema 1.1 → 1.2 (decision P8 adds basis recorded_interview and statement kind 'recorded interview'); no content change."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Decision P10 (lens audit batch 3, #25): mid_basin how_known reworded; the A ≥ 3 branch reads A only, so certainty is A's (0.7). Value and certainty unchanged. Not reviewed."}

identity:
  id: schrodinger-erwin
  display_name: "Erwin Schrödinger"
  roster:
    canonical_name: "Erwin Schrödinger"
    rank: 24
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: physics
    field_bucket: physics
  full_name: {value: "Erwin Rudolf Josef Alexander Schrödinger", certainty: 0.7, cites: [{source: S2, locator: "heading"}], how_known: "MacTutor gives the full name; Britannica gives Erwin Schrödinger."}
  native_name: {value: "Erwin Schrödinger (German)", certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}], how_known: "Austrian; same spelling."}
  aliases:
    - {name: "Erwin-Schrödinger", kind: "roster alias"}
    - {name: "Schrödinger-Erwin", kind: "roster alias"}
    - {name: "Erwin Schroedinger", kind: transliteration}

basics:
  birth:
    date: {value: "1887-08-12", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S3, locator: "first paragraph"}], how_known: "Two sources agree."}
    place: {value: "Vienna", modern_name: "Vienna, Austria", polity_then: "Austria-Hungary", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S3, locator: "first paragraph"}], how_known: "Two sources agree."}
  death:
    date: {value: "1961-01-04", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S3, locator: "last paragraph"}], how_known: "Two sources agree."}
    place: {value: "Vienna", modern_name: "Vienna, Austria", polity_then: "Austria", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}], how_known: "Britannica; the Nobel biography says he returned to Vienna after retiring."}
  first_lasting_contribution_year: {value: 1926, certainty: 1.0, cites: [{source: S1, locator: "Zürich paragraph"}, {source: S3, locator: "paragraph 5"}], how_known: "The wave equation, first half of 1926; two sources."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S3, locator: "paragraph 5"}], how_known: "From first_lasting_contribution_year (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts ('Vienna, Austria')"}], how_known: "Austria is Western Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "Zürich paragraph"}, {source: S3, locator: "paragraph 5"}], how_known: "Main contribution (wave mechanics, 1926) was made in Zürich (Switzerland, Western Europe), so that is the value (DATA_DICTIONARY: if split, pick where the main contribution was made). Two other contributions listed in this record were made in Northern Europe: the cat paper (1935) while he was at Oxford (1933–36) and What is Life? (1944) in Dublin. Two regions, so 0.7, as for Einstein, Fermi and Meitner.", alternatives: [{value: "Northern Europe", cites: [{source: S2, locator: "Biography (Oxford, November 1933; Dublin from autumn 1939)"}], note: "Oxford (UK) and Dublin (Ireland) are Northern Europe in data/reference/regions.csv."}]}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S3, locator: "first paragraph ('the only child')"}], how_known: "As the sources record it."}
  languages_of_work: {value: [German, English], certainty: 1.0, cites: [{source: S1, locator: "later life paragraph"}, {source: S2, locator: "Biography"}], how_known: "German papers; English books from Dublin; English learned in childhood."}
  occupations: {value: [physicist, "university professor", "institute director"], certainty: 1.0, cites: [{source: S3, locator: "paragraphs 5–7"}], how_known: "Nobel biography."}

contribution:
  fields: {value: ["theoretical physics", "quantum mechanics", "statistical mechanics", "colour theory", "theoretical biology", "philosophy"], certainty: 1.0, cites: [{source: S1, locator: "opening paragraph; later life"}, {source: S3, locator: "paragraph 5"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Wave mechanics and the Schrödinger equation", year: "1926", kind: theory, lasting: "the basic equation of non-relativistic quantum mechanics (S1); Nobel Prize 1933, shared with Dirac", certainty: 1.0, cites: [{source: S1, locator: "opening paragraph; Zürich paragraph"}, {source: S3, locator: "paragraph 5"}], how_known: "Two sources."}
    - {value: "Schrödinger's cat thought experiment", year: "1935", kind: "concept or term", lasting: "standard illustration of the measurement problem", certainty: 1.0, cites: [{source: S1, locator: "cat paragraph"}], how_known: "Britannica."}
    - {value: "What is Life? (physics applied to living matter and heredity)", year: "1944", kind: work, lasting: "its influence on biology is often stated but is not given in S1–S3 (gap)", certainty: 0.5, cites: [{source: S3, locator: "paragraph 8"}, {source: S1, locator: "later life"}], how_known: "Both sources name the book; neither states its lasting influence, so 0.5."}
  evidence_of_impact:
    - {value: "Nobel Prize for Physics 1933", kind: "honours in lifetime", certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}, {source: S3, locator: "paragraph 5"}], how_known: "Two sources."}
    - {value: "The Schrödinger equation", kind: "named after them", certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}], how_known: "Britannica."}
  major_works:
    - {value: "What is Life?", year: 1944, kind: book, certainty: 1.0, cites: [{source: S1, locator: "later life"}, {source: S3, locator: "paragraph 8"}], how_known: "Two sources."}
    - {value: "Meine Weltansicht (My View of the World)", year: 1961, kind: book, certainty: 1.0, cites: [{source: S1, locator: "later life"}], how_known: "Britannica."}
  honours:
    - {value: "Nobel Prize for Physics (shared with P. A. M. Dirac)", year: 1933, certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}], how_known: "Britannica."}
  definition_fit: {value: "clearly meets", rationale: "Founder of wave mechanics.", certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}], how_known: "Sources agree."}

childhood:
  family_religion: {value: TODO, note: "Not settled from the sources read. MacTutor's 'Although he was a Catholic' (S2, Biography) is about the adult in 1933, not his family. A Catholic father and a Lutheran mother are commonly reported but were not found in S1–S5; needs the Autobiographical Sketches in full or Moore's biography."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father, Rudolf Schrödinger, ran a small linoleum factory and studied botany and Italian painting", name: "Rudolf Schrödinger", role: father, certainty: 1.0, cites: [{source: S2, locator: "Biography"}, {source: S3, locator: "paragraphs 1–2"}], how_known: "Two sources."}
    - {value: "Mother, Emily Bauer, half English, daughter of the chemist Alexander Bauer", name: "Emily Bauer", role: mother, certainty: 1.0, cites: [{source: S2, locator: "Biography"}, {source: S3, locator: "first paragraph"}], how_known: "Two sources."}
  household_circumstances: {value: "Educated Viennese household; only child; English and German both spoken", certainty: 1.0, cites: [{source: S2, locator: "Biography"}, {source: S3, locator: "first paragraph"}], how_known: "Two sources."}
  schooling:
    - {value: "Private tutor at home to age ten", stage: tutor, ages: "to 10", certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor."}
    - {value: "Akademisches Gymnasium, Vienna", stage: "grammar or secondary school", years: "1898–1906", certainty: 1.0, cites: [{source: S2, locator: "Biography"}, {source: S3, locator: "paragraph 3"}], how_known: "Two sources."}
    - {value: "University of Vienna; doctorate 1910", stage: university, years: "1906–1910", certainty: 1.0, cites: [{source: S1, locator: "Zürich paragraph"}, {source: S2, locator: "Biography"}, {source: S3, locator: "paragraph 4"}], how_known: "Three sources."}
  early_mathematics: {value: "advanced mathematics", note: "Loved mathematics and physics at the Gymnasium; solved problems at the board 'with playful facility'", certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor, quoting him and a schoolmate."}
  early_geometric_style_reasoning: {value: "Loved 'the strict logic of the ancient grammars'", certainty: 0.7, cites: [{source: S2, locator: "Biography"}, {source: S3, locator: "paragraph 3"}], how_known: "His own later account (S2) and the Nobel biography."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [German, English], certainty: 1.0, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1910–1961", certainty: 1.0, cites: [{source: S2, locator: "Biography"}], how_known: "Doctorate to death."}
  nominal_affiliations:
    - {value: "Catholic as an adult, per MacTutor ('Although he was a Catholic', 1933); no church practice reported", role: other, certainty: 0.7, cites: [{source: S2, locator: "Biography (1933)"}], how_known: "One reliable source on the adult, so 0.7. It says nothing about his family's church (see childhood.family_religion)."}
  self_described_science_religion_relation:
    value: "His metaphysics of one mind is 'religion, not a science -- a religion, however, not opposed to science, but supported by what disinterested scientific research has brought to the fore' (Mind and Matter, 1958). In What is Life? he presents the conclusion that 'I' control the atoms 'according to the Laws of Nature' as the closest a biologist can get to proving God and immortality."
    certainty: 0.7
    cites: [{source: S5, locator: "Mind and Matter ch. 4, p. 135"}, {source: S4, locator: "Epilogue, pp. 86–87"}]
    how_known: "His published books, read in unofficial web transcriptions, so 0.7."
  primary_system:
    value: HINDU
    basis: written_profession
    certainty: 0.5
    cites: [{source: S4, locator: "Epilogue, p. 87"}, {source: S5, locator: "Mind and Matter ch. 4, p. 129"}, {source: S1, locator: "later life ('closely paralleled the mysticism of the Vedanta')"}]
    how_known: "His published epilogue endorses the Upanishadic 'ATHMAN = BRAHMAN' as the deepest insight, and Mind and Matter calls one-mind 'the doctrine of the Upanishads'; Britannica says his outlook closely paralleled the Vedanta. Certainty 0.5, below the 0.7 cap: the HINDU system file is a stub with use_when TODO, so the code's test cannot be applied, and three alternatives are named."
    rationale: "Coded to the Vedanta tradition he names as the source of his view (Advaita: the self is the one eternal self). He was not a member; the code follows the writing, not membership. Alternatives: PANT (the divine is identified with the one mind, not stated as Nature as a whole, so part 1 of the PANT test is not clearly met); IDEAL (consciousness is the one reality, plurality is maya); PANENT (the one mind is 'indestructible' and 'always now', which could exceed the world). HINDU, IDEAL and PANENT are stub system files (flag)."
  secondary_system: {value: UNKNOWN, how_known: "No second system in S1–S5."}
  candidate_codes_considered:
    - {code: PANT, reason: "Named alternative. Part 2 is met (one mind, eternal), but part 1 identifies God with consciousness ('Hence I am God Almighty'), not explicitly with Nature as a whole.", cites: [{source: S4, locator: "Epilogue, p. 87"}]}
    - {code: IDEAL, reason: "Named alternative: 'in truth there is only one mind'. Stub system file (flag).", cites: [{source: S5, locator: "Mind and Matter ch. 4, p. 129"}]}
    - {code: PANENT, reason: "Named alternative: mind is 'indestructible' and timeless. Stub system file (flag).", cites: [{source: S5, locator: "Mind and Matter ch. 4, p. 135"}]}
    - {code: CHRIST, reason: "Rejected: he calls the plurality of souls, 'common to all official Western creeds', a hypothesis to be suspicious of.", cites: [{source: S4, locator: "Epilogue, p. 88"}]}
  lio_axes:
    A_locus:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S4, locator: "Epilogue, p. 87"}, {source: S5, locator: "Mind and Matter ch. 4, p. 129"}]
      how_known: "Published book; capped at 0.7 because 3 is named below."
      rationale: "At the immanent pole: the divine is the one self that every conscious mind is, 'the personal self equals the omnipresent, all-comprehending eternal self'; in Christian terms 'Hence I am God Almighty'. No transcendent person. Named alternative 3: the one mind is timeless and 'indestructible' (S5, p. 135), which on a panentheist reading exceeds the world."
    B_cause:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S4, locator: "Epilogue, p. 86"}]
      how_known: "Published book, his own words, explicit. Certainty 0.7 under CODING_GUIDE §7: the epilogue was read only in an unofficial web copy (rapeutation.com, S4), and no authoritative edition could be reached to check the wording (the only unrestricted Internet Archive copies are re-uploaded PDFs, not library scans)."
      rationale: "Scored on his account of nature (P6). At the law pole: 'My body functions as a pure mechanism according to the Laws of Nature'; bodily events are 'if not strictly deterministic at any rate statistico-deterministic', and 'quantum indeterminacy plays no biologically relevant role in them'. Even the self's agency controls the atoms 'according to the Laws of Nature'. No exception."
    C_ledger:
      value: 4
      basis: written_profession
      certainty: 0.5
      cites: [{source: S4, locator: "Epilogue, pp. 88–90"}]
      how_known: "Published book, but it speaks to the ledger only indirectly (no statement on reward or punishment), so 0.5."
      rationale: "Impersonal or none: there is no judged individual soul; separate souls are an 'invention' and 'gross superstitions'; 'In no case is there a loss of personal existence to deplore. Nor will there ever be.' Mocking whether 'women, or only men, have souls' is a moral-community point and is scored here, not on E (P7)."
    D_authority:
      value: 3
      basis: written_profession
      certainty: 0.5
      cites: [{source: S5, locator: "Mind and Matter ch. 4, p. 135"}, {source: S1, locator: "later life"}]
      how_known: "Published book through one transcription only, and the D reading is indirect, so 0.5."
      rationale: "Leans to reason. No revelation outranks observation; his religion is 'supported by what disinterested scientific research has brought to the fore'. The stated limited exception: 'incontrovertible direct experience' and the mystics' testimony carry weight beside science, and Britannica reports 'a skepticism toward the relevance of science as a unique tool' for ultimate questions."
    E_scope:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S4, locator: "Epilogue, pp. 86–87"}]
      how_known: "Published book; it addresses one order for all minds and bodies, but not group favour in events directly, so 0.7."
      rationale: "Scored on the world's order (P7). Same rules for all: every body is a mechanism under the Laws of Nature, and the self is 'every conscious mind that has ever said or felt 'I''. No favour or exception for a group in events."
  mid_basin:
    value: false
    certainty: 0.7
    cites: [{source: S4, locator: "Epilogue, p. 87"}]
    how_known: "P4 test: A_locus = 4 (≥ 3), so false. Certainty is A's (0.7): the A ≥ 3 branch reads A only (decision P10)."
  statements:
    - text: "My body functions as a pure mechanism according to the Laws of Nature."
      cites: [{source: S4, locator: "Epilogue 'On Determinism and Free Will', p. 86"}]
      date: "1944"
      axes: [B_cause, E_scope]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
      note: "Unofficial web transcription of the Cambridge edition; page from the edition's pagination as cited in S5."
    - text: "[...] am the person, if any, who controls the 'motion of the atoms' according to the Laws of Nature."
      cites: [{source: S4, locator: "Epilogue, p. 86–87"}]
      date: "1944"
      context: "The subject is 'I – I in the widest meaning of the word, that is to say, every conscious mind that has ever said or felt 'I''."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "In Christian terminology to say: 'Hence I am God Almighty' sounds both blasphemous and lunatic."
      cites: [{source: S4, locator: "Epilogue, p. 87"}]
      date: "1944"
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "From the early great Upanishads the recognition ATHMAN = BRAHMAN (the personal self equals the omnipresent, all-comprehending eternal self) was in Indian thought considered, far from being blasphemous, to represent the quintessence of deepest insight into the happenings of the world."
      cites: [{source: S5, locator: "What is Life?, Epilogue, p. 87, paragraph 4"}, {source: S4, locator: "Epilogue"}]
      date: "1944"
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
      note: "S4 has an OCR insertion ('upheld in') before the parenthesis; S5 matches the wording given here."
    - text: "In no case is there a loss of personal existence to deplore. Nor will there ever be."
      cites: [{source: S4, locator: "Epilogue, p. 90"}]
      date: "1944"
      axes: [C_ledger]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
      note: "Page inferred from the epilogue's span (pp. 86–90); not checked against the book."
    - text: "Their multiplicity is only apparent, in truth there is only one mind."
      cites: [{source: S5, locator: "Mind and Matter ch. 4, p. 129, paragraph 2"}]
      date: "1958"
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "I am now talking religion, not a science -- a religion, however, not opposed to science, but supported by what disinterested scientific research has brought to the fore."
      cites: [{source: S5, locator: "Mind and Matter ch. 4, p. 135, paragraph 1"}]
      date: "1958"
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
      note: "The transcription writes the dash as '--'."
  changes_over_life: []
  coder_notes: "HINDU (primary) and the alternatives IDEAL, PANENT are stub system files: flagged, not sourced in this run. PANT is sourced. Both transcriptions (S4, S5) are unofficial websites; the passages used agree between them where both have them. The strangebeautiful.com scan of the Cambridge edition timed out twice. My View of the World (1961) was not read."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Viennese; father's family Bavarian in origin, mother half English", certainty: 1.0, cites: [{source: S2, locator: "Biography"}, {source: S3, locator: "paragraph 2"}], how_known: "Two sources."}
  religious_heritage_by_birth: {value: TODO, note: "MacTutor's 'a Catholic' (1933) describes the adult, not his birth family; see childhood.family_religion."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1926", certainty: 1.0, cites: [{source: S1, locator: "Zürich paragraph ('a six-month period in 1926')"}], how_known: "Britannica."}
  age_at_first_lasting_contribution: {value: 38, certainty: 0.7, cites: [{source: S3, locator: "paragraph 5 ('during the first half of 1926')"}], how_known: "Born August 1887; the wave equation in the first half of 1926, so 38. Britannica says 'at the age of 39' (flag)."}
  first_evidence_of_lio_type_views: {value: "What is Life? epilogue: the body as a mechanism under the Laws of Nature, and ATHMAN = BRAHMAN", year: 1944, certainty: 0.7, cites: [{source: S4, locator: "Epilogue, pp. 86–87"}], how_known: "Earliest verified statement in the sources read. An earlier date (the first essay of My View of the World is often dated 1925) was not checked; see open questions."}
  lio_views_relative_to_major_work: {value: "unclear", rationale: "Verified statements are from 1944 and 1958, after the 1926 work. If an earlier essay (often dated 1925, not checked) holds the same view, the answer would be 'before major work'.", certainty: 0.5, cites: [{source: S4, locator: "Epilogue"}, {source: S1, locator: "later life"}], how_known: "Coder's reading of dates."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "The epilogue argues from two premises to 'the only possible inference' (S4), a deductive form; his physics is not axiomatic.", certainty: 0.5, cites: [{source: S4, locator: "Epilogue, p. 86"}], how_known: "Coder's reading."}
  form_acquired: {value: "childhood or adolescence", rationale: "He loved 'the strict logic of the ancient grammars' at the Gymnasium (S2).", certainty: 0.5, cites: [{source: S2, locator: "Biography"}], how_known: "Coder's reading."}
  circle_present: {value: "partly", rationale: "God identified with the one self of all minds, not stated as Nature.", certainty: 0.5, cites: [{source: S4, locator: "Epilogue, p. 87"}], how_known: "Coder's reading."}
  reading: "As belief, not finding: partial form, partial circle. The record does not test H1."
  notes: ""

institutions:
  - {value: "University of Zürich", role: "professor", years: "1921–1927", kind: university, certainty: 1.0, cites: [{source: S1, locator: "Zürich paragraph"}, {source: S3, locator: "paragraph 5"}], how_known: "Two sources."}
  - {value: "University of Berlin", role: "professor (Planck's successor)", years: "1927–1933", kind: university, certainty: 1.0, cites: [{source: S1, locator: "Berlin paragraph"}, {source: S3, locator: "paragraph 7"}], how_known: "Two sources."}
  - {value: "Dublin Institute for Advanced Studies", role: "director, School for Theoretical Physics", years: "1940–1955", kind: employer, certainty: 1.0, cites: [{source: S1, locator: "Berlin paragraph"}, {source: S3, locator: "paragraph 7"}], how_known: "Two sources."}
collaborators:
  - {value: "Fritz Hasenöhrl", relation: teacher, certainty: 1.0, cites: [{source: S2, locator: "Biography"}, {source: S3, locator: "paragraph 4"}], how_known: "Two sources."}
  - {value: "Max Planck", roster_id: planck-max, relation: other, note: "succeeded him in Berlin", certainty: 1.0, cites: [{source: S1, locator: "Berlin paragraph"}], how_known: "Britannica."}
  - {value: "Arthur Schopenhauer", relation: "influenced by", note: "named in the epilogue as a Western voice for the one-self view", certainty: 0.7, cites: [{source: S4, locator: "Epilogue, p. 88"}], how_known: "His own mention."}

review:
  roster_status_reason: {value: "Core in v7.1 (F 4) and v8 (F 5, all five models).", certainty: 0.7, cites: [{source: S6, locator: "roster.csv, rank 24"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Family religion: MacTutor's 'Although he was a Catholic' is about the adult in 1933, not his family (lens audit, batch 2). A Catholic father and Lutheran mother are commonly reported but not found in the sources read, so family_religion and religious_heritage_by_birth are TODO."
    - "Age at the wave equation: Britannica says 39; birth date and 'first half of 1926' give 38."
    - "S4 and S5 are unofficial transcriptions; S4 has OCR errors (e.g. 'upheld in', a garbled line in the maya passage). Only clean passages are quoted."
  open_questions:
    - "Read My View of the World (1961) and the Autobiographical Sketches, for the 1925 essay and his upbringing."
    - "Source the HINDU system file, then retest HINDU against PANT and IDEAL."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Jeremy Bernstein"
    citation: "Bernstein, Jeremy. \"Erwin Schrödinger.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Erwin-Schrodinger."
    url: "https://www.britannica.com/biography/Erwin-Schrodinger"
    accessed: 2026-10-02
    reliability_note: "Signed encyclopedia article by a physicist-writer."
    used_for: [identity, basics, contribution, worldview, timing, institutions, collaborators]
  - id: S2
    type: tertiary
    kind: encyclopedia
    author: "J. J. O'Connor and E. F. Robertson"
    citation: "O'Connor, J. J. and E. F. Robertson. \"Erwin Rudolf Josef Alexander Schrödinger.\" MacTutor History of Mathematics Archive. https://mathshistory.st-andrews.ac.uk/Biographies/Schrodinger/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Schrodinger/"
    accessed: 2026-10-02
    reliability_note: "Standard biographical archive; draws on Moore's biography."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, lane_b, collaborators]
  - id: S3
    type: tertiary
    kind: "institutional page"
    author: "Nobel Foundation"
    citation: "\"Erwin Schrödinger – Biographical.\" NobelPrize.org (from Nobel Lectures, Physics 1922–1941). https://www.nobelprize.org/prizes/physics/1933/schrodinger/biographical/."
    url: "https://www.nobelprize.org/prizes/physics/1933/schrodinger/biographical/"
    accessed: 2026-10-02
    reliability_note: "Official biography; paragraphs counted from the top."
    used_for: [basics, contribution, childhood, timing, institutions, collaborators]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "Erwin Schrödinger"
    year: 1944
    citation: "Schrödinger, Erwin. What is Life? The Physical Aspect of the Living Cell. Cambridge University Press, 1944; ch. 7 and Epilogue 'On Determinism and Free Will' (pp. 86–90 in the 1992 Canto edition with Mind and Matter and Autobiographical Sketches). Web transcription at rapeutation.com."
    url: "https://rapeutation.com/cult.whatislife.7.htm"
    accessed: 2026-10-02
    reliability_note: "Unofficial transcription with some OCR errors; used only for clean passages."
    used_for: [worldview, lane_b, collaborators]
  - id: S5
    type: primary
    kind: "published work by the subject"
    author: "Erwin Schrödinger"
    year: 1958
    citation: "Schrödinger, Erwin. What is Life? (1944) with Mind and Matter (1958) and Autobiographical Sketches. Cambridge University Press (Canto), 16th printing 2006. Excerpts with page and paragraph locators at advaitism.com ('Latter Day Buddhism')."
    url: "https://www.advaitism.com/latterdaybuddhists/life.html"
    accessed: 2026-10-02
    reliability_note: "Unofficial excerpt page; gives page and paragraph of the Cambridge edition for each passage."
    used_for: [worldview]
  - id: S6
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-02
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
---

# Erwin Schrödinger

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Erwin Schrödinger (1887–1961), Austrian physicist, created wave mechanics in 1926 and shared the 1933 Nobel Prize with Dirac [S1, opening paragraph; S3, paragraph 5]. In What is Life? (1944) and Mind and Matter (1958) he held that the body runs by the laws of nature and that all minds are one eternal self, citing the Upanishads [S4, Epilogue; S5, p. 129]. Coded HINDU at 0.5 (stub system), with PANT, IDEAL and PANENT named; not mid-basin.

## Life and work

Born in Vienna, tutored at home and schooled at the Akademisches Gymnasium, he took his doctorate at Vienna in 1910 [S2, Biography]. He worked in Zürich (1921–1927), Berlin (1927–1933), Graz, and Dublin (1940–1955), then returned to Vienna [S3, paragraphs 5–9].

## Contribution and impact

The Schrödinger equation (1926), the cat thought experiment (1935) and What is Life? (1944) [S1, opening paragraph; cat paragraph; later life].

## Childhood and education

Only child of Rudolf Schrödinger and Emily Bauer; English and German were spoken at home [S2, Biography]. He loved mathematics, physics and "the strict logic of the ancient grammars" [S2, Biography]. MacTutor calls the adult a Catholic (1933); his family's church is not settled from the sources read [S2, Biography].

## Adult working worldview

"My body functions as a pure mechanism according to the Laws of Nature" [S4, Epilogue, p. 86]. From this and direct experience he concludes that every conscious "I" controls the atoms according to those laws, which in Christian terms reads "Hence I am God Almighty", and he links it to "ATHMAN = BRAHMAN" [S4, p. 87; S5, p. 87]. "In truth there is only one mind" [S5, p. 129]. Britannica: his outlook "closely paralleled the mysticism of the Vedanta" [S1, later life]. Scores: A 4 (0.7), B 4 (1.0), C 4 (0.5), D 3 (0.5), E 4 (0.7); mid_basin false.

## Heritage (context only)

Viennese, half-English mother [S2, Biography]. Context only.

## Timing

First lasting contribution 1926, at 38 [S3, paragraph 5]. Verified worldview statements are from 1944 and 1958.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Partial deductive form; partial circle (God as the one self, not stated as Nature) [S4, Epilogue].

## Open questions

- My View of the World and the Autobiographical Sketches; the HINDU system file.

## Research log

- 2026-10-02: Read Britannica (Bernstein), MacTutor, Nobel biography; the What is Life? epilogue in a web transcription (rapeutation.com) and Cambridge-edition excerpts with page numbers (advaitism.com). The scanned Cambridge edition (strangebeautiful.com) timed out twice. All quotations checked against S1–S5 text.
