---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 7
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, second batch: physical science 1600–1950)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages and essay transcriptions"
  collected_on: 2026-10-02
  last_updated: 2026-10-02
  change_log:
    - {date: 2026-10-02, by: "Grok Bot", summary: "Record created (second batch, RUNBOOK §1 order). Basics, contribution and childhood from Britannica (Kaku) and MacTutor. Worldview from the 1929 cable to Rabbi Goldstein (JTA print), the 1930 essay 'Religion and Science' and the 1939/1941 'Science and Religion' (Ideas and Opinions transcription), and SEP 'Pantheism' §12. Coded PANT at 0.7 (AGNOS and ATHE named). A 4 (0.7), B 4 (1.0), C 4 (0.7), D 3 (0.7), E 4 (1.0). mid_basin false. Lane B and minor fields partly TODO. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Lens audit, batch 2 (two blind runs at e648145): D_authority 3 → 2 (both runs, finding #5): the 1939 address puts the highest ends under revelation and tradition and the 1941 paper limits science to what is, which is two domains under two authorities (§3 same pattern, as Planck and Galileo); named alternative 3. B_cause and E_scope certainty 1.0 → 0.7: the key sentences are in the third person, the reason C was already 0.7 (pattern check). Trailing and leading cuts marked with [...] (findings #16, #18; same fix to two more statements). Two statements added (1939 revelation sentence; 1941 'science can only ascertain what is'). mid_basin unchanged (false at 0.7). Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "CODING_GUIDE §7 rule on unofficial web copies (Jason's decision, 2026-10-02): self_described_science_religion_relation certainty 1.0 → 0.7. It rests on the sacred-texts.com copy of the 1930 and 1941 essays (S3), and no authoritative edition was reachable to check the wording. No mid_basin change (it depends on A and B only)."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Schema 1.1 → 1.2 (decision P8 adds basis recorded_interview and statement kind 'recorded interview'); no content change."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Decision P10 (lens audit batch 3, #25): mid_basin how_known reworded; the A ≥ 3 branch reads A only, so certainty is A's (0.7). Value and certainty unchanged. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Stage 3 lens-audit rulings applied to the batch's other records (OPEN_DECISIONS P14–P28, v8's picks, 2026-10-02). Schema 1.2 → 1.3. One reliable source caps a fact at 0.7; derived fields take the lowest certainty of their inputs; kind lists (P21: research institute, school stage and run_by, scholarly edition); Britannica Top Questions cites removed (P26). Full before → after list: reports/stage3_rulings_changes.csv. Not reviewed."}
    - {date: 2026-10-02, by: "Grok Bot", summary: "Span alignment (P29, P30 and its addendum): timing.major_work_period 1905–1915 → 1905–1925; worldview.working_years 1905–1955 → 1905–1925, equal to the span (P30 addendum f); lasting item added: Bose–Einstein statistics for atoms and the prediction of Bose–Einstein condensation (1924–1925); source S7 added; 7 headline values rest on evidence outside the span and are left unchanged for a ruling (open questions). Listed in reports/p30_span_alignment.csv. Not reviewed."}

identity:
  id: einstein-albert
  display_name: "Albert Einstein"
  roster:
    canonical_name: "Albert Einstein"
    rank: 6
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: physics
    field_bucket: physics
  full_name: {value: "Albert Einstein", certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}, {source: S2, locator: "heading"}], how_known: "Two sources agree."}
  native_name: {value: "Albert Einstein (German)", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}], how_known: "Same spelling in German; born in Ulm, Württemberg."}
  aliases:
    - {name: "Albert-Einstein", kind: "roster alias"}
    - {name: "Einstein-Albert", kind: "roster alias"}

basics:
  birth:
    date: {value: "1879-03-14", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S2, locator: "Quick Info"}], how_known: "Two sources agree."}
    place:
      value: "Ulm, Württemberg"
      modern_name: "Ulm, Baden-Württemberg, Germany"
      polity_then: "Kingdom of Württemberg, German Empire"
      certainty: 1.0
      cites: [{source: S1, locator: "Quick Facts"}, {source: S2, locator: "Quick Info"}]
      how_known: "Two sources agree."
  death:
    date: {value: "1955-04-18", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S2, locator: "Quick Info"}], how_known: "Two sources agree."}
    place:
      value: "Princeton, New Jersey"
      modern_name: "Princeton, New Jersey, United States"
      polity_then: "United States"
      certainty: 1.0
      cites: [{source: S1, locator: "Quick Facts"}, {source: S2, locator: "Quick Info"}]
      how_known: "Two sources agree."
  first_lasting_contribution_year: {value: 1905, certainty: 1.0, cites: [{source: S2, locator: "Biography (three papers of 1905)"}, {source: S1, locator: "opening paragraph"}], how_known: "The 1905 papers on light quanta, special relativity and statistical mechanics; the photoelectric explanation won the 1921 Nobel Prize."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S2, locator: "Biography"}], how_known: "From first_lasting_contribution_year (decision P2)."}
  region_of_birth: {value: "Western Europe", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts ('Ulm, Württemberg (now Baden-Württemberg), Germany')"}], how_known: "Germany is Western Europe in data/reference/regions.csv (decision P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "The 1905 papers were written at the Bern patent office and general relativity (1915) in Berlin (Switzerland and Germany are Western Europe in regions.csv). From 1933 he worked in Princeton (North America). Two regions, so 0.7.", alternatives: [{value: "North America", cites: [{source: S1, locator: "Quick Facts"}], note: "Institute for Advanced Study, Princeton, 1933–1955."}]}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "opening paragraph"}], how_known: "As the sources record it."}
  languages_of_work: {value: [German, English], certainty: 0.7, cites: [{source: S2, locator: "Biography"}, {source: S3, locator: "headnotes"}], how_known: "The physics papers are in German; the later essays appear in English (S3 headnotes give US publication)."}
  occupations: {value: [physicist, "patent examiner", "university professor"], certainty: 1.0, cites: [{source: S2, locator: "Biography"}, {source: S1, locator: "opening paragraph"}], how_known: "Two sources."}

contribution:
  fields: {value: ["theoretical physics", "relativity", "quantum theory", "statistical mechanics"], certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}, {source: S2, locator: "Biography"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Light quanta and the explanation of the photoelectric effect", year: "1905", kind: theory, lasting: "Nobel Prize for Physics 1921 (S1)", certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}, {source: S2, locator: "Biography"}], how_known: "Two sources."}
    - {value: "Special theory of relativity and mass–energy equivalence", year: "1905", kind: theory, lasting: "standard physics", certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}, {source: S2, locator: "Biography"}], how_known: "Two sources."}
    - {value: "General theory of relativity", year: "1915", kind: theory, lasting: "MacTutor: 'still regarded as the most satisfactory model of the large-scale universe that we have'", certainty: 1.0, cites: [{source: S1, locator: "opening paragraph"}, {source: S2, locator: "Summary; Biography"}], how_known: "Two sources."}
    - {value: "Bose–Einstein statistics for atoms and the prediction of Bose–Einstein condensation", year: "1924–1925", kind: "theory", lasting: "Bose–Einstein condensates, first made in 1995 (Nobel Prize 2001)", certainty: 0.7, cites: [{source: S1, locator: "Legacy ('In 1995 a Nobel Prize was awarded to the discoverers of Bose-Einstein condensates')"}, {source: S7, locator: "press release ('In 1924 [...] Bose [...] sent his results to Einstein who extended the theory'; 'Seventy years were to pass')"}], how_known: "Britannica names it among his results that later won Nobel Prizes (its year for that prize is loose: the condensate was made in 1995 and the prize came in 2001, S7). The years are the Nobel Foundation's: Bose's 1924 work, then Einstein's extension, seventy years before 1995. Two sources, but the dates rest on one, so 0.7. Added 2026-10-02 under the P30 addendum (the latest lasting work must be listed)."}
  evidence_of_impact:
    - {value: "Nobel Prize for Physics 1921; Copley Medal 1925", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}], how_known: "Britannica."}
    - {value: "MacTutor: 'Einstein contributed more than any other scientist to the modern vision of physical reality.'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S2, locator: "Summary"}], how_known: "MacTutor."}
  major_works: []
  honours:
    - {value: "Nobel Prize for Physics", year: 1921, certainty: 0.7, cites: [{source: S1, locator: "Quick Facts"}], how_known: "Britannica."}
  definition_fit: {value: "clearly meets", rationale: "Several lasting original theories, each standard physics.", certainty: 0.7, cites: [{source: S1, locator: "opening paragraph"}], how_known: "Sources agree."}

childhood:
  family_religion: {value: "Jewish; his parents were secular", certainty: 1.0, cites: [{source: S1, locator: "Childhood and education ('Einstein's parents were secular, middle-class Jews')"}, {source: S2, locator: "Biography (taught Judaism at home)"}], how_known: "Two sources."}
  family_religious_practice: {value: "Secular household, but he was given Jewish religious instruction at home and later at the Gymnasium", certainty: 0.7, cites: [{source: S1, locator: "Childhood and education"}, {source: S2, locator: "Biography"}], how_known: "Two sources, each giving one half."}
  parents_and_household:
    - {value: "Father, Hermann Einstein, a featherbed salesman who later ran an electrochemical factory", name: "Hermann Einstein", role: father, certainty: 0.7, cites: [{source: S1, locator: "Childhood and education"}], how_known: "Britannica; undisputed."}
    - {value: "Mother, Pauline Koch, ran the household", name: "Pauline Einstein (née Koch)", role: mother, certainty: 0.7, cites: [{source: S1, locator: "Childhood and education"}], how_known: "Britannica; undisputed."}
  household_circumstances: {value: "Middle-class; his father's business failures disrupted his schooling (1894 move of the family to Milan)", certainty: 0.7, cites: [{source: S1, locator: "Childhood and education"}, {source: S2, locator: "Biography"}], how_known: "Two sources."}
  schooling:
    - {value: "School in Munich from about 1886", stage: "grammar or secondary school", years: "c. 1886–1888", certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor; the elementary school is not named in the sources read."}
    - {value: "Luitpold Gymnasium, Munich; left in 1894–95", stage: "grammar or secondary school", years: "1888–1894", certainty: 1.0, cites: [{source: S1, locator: "Childhood and education"}, {source: S2, locator: "Biography"}], how_known: "Two sources."}
    - {value: "Cantonal school at Aarau, Switzerland; graduated 1896", stage: "grammar or secondary school", years: "1895–1896", certainty: 1.0, cites: [{source: S1, locator: "Childhood and education"}, {source: S2, locator: "Biography"}], how_known: "Two sources."}
    - {value: "Swiss Federal Polytechnic, Zürich; teaching diploma 1900", stage: university, years: "1896–1900", certainty: 1.0, cites: [{source: S1, locator: "Childhood and education"}, {source: S2, locator: "Biography"}], how_known: "Two sources."}
  early_mathematics: {value: "geometry (Euclid-style proof)", note: "At 12 he devoured a geometry book he called his 'sacred little geometry book'; calculus from about 1891 (age 12)", certainty: 1.0, cites: [{source: S1, locator: "Childhood and education"}, {source: S2, locator: "Biography"}], how_known: "Two sources."}
  early_geometric_style_reasoning: {value: "Euclidean geometry book at 12, then higher mathematics with Max Talmud", certainty: 0.7, cites: [{source: S1, locator: "Childhood and education"}], how_known: "Britannica."}
  early_science_exposure:
    - {value: "Compass at age five; Bernstein's popular science books via Max Talmud; light-beam thought experiment at 16", age: 5, certainty: 0.7, cites: [{source: S1, locator: "Childhood and education"}], how_known: "Britannica."}
  key_early_reading:
    - {value: "Aaron Bernstein, Naturwissenschaftliche Volksbücher", certainty: 0.7, cites: [{source: S1, locator: "Childhood and education"}], how_known: "Britannica."}
  childhood_mentors:
    - {value: "Max Talmud (Talmey), medical student and informal tutor", certainty: 0.7, cites: [{source: S1, locator: "Childhood and education"}], how_known: "Britannica."}
  languages_in_childhood: {value: [German], certainty: 0.7, cites: [{source: S1, locator: "Childhood and education"}], how_known: "Born and schooled in Germany."}
  notable_events:
    - {value: "Became 'deeply religious at age 12', composing songs in praise of God; this changed after he read science books", age: 12, certainty: 0.7, cites: [{source: S1, locator: "Childhood and education"}], how_known: "Britannica (one source)."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1905–1925", certainty: 0.7, cites: [{source: S2, locator: "Biography"}, {source: S1, locator: "Legacy (Bose-Einstein condensates)"}, {source: S7, locator: "press release"}], how_known: "Equal to timing.major_work_period (P30 addendum f; span check 2026-10-02). Was 1905–1955: From the 1905 papers to his death."}
  nominal_affiliations:
    - {value: "Jewish by descent; no synagogue membership is reported in the sources read", role: "other", certainty: 0.7, cites: [{source: S1, locator: "Childhood and education"}], how_known: "One source."}
  self_described_science_religion_relation:
    value: "Science and religion need each other and should not conflict: 'science without religion is lame, religion without science is blind' (1941). Science says what is; religion deals with valuations of human thought and action. The conflict comes from the idea of a personal God, which religion should give up. The 'cosmic religious feeling' is, in his view, the strongest motive for research (1930)."
    certainty: 0.7
    cites: [{source: S3, locator: "'Science and Religion' part II (1941)"}, {source: S3, locator: "'Religion and Science' (1930)"}]
    how_known: "His own published essays; quotations in statements. Certainty 0.7 under CODING_GUIDE §7: the essays were read only in an unofficial web copy (sacred-texts.com, S3), and no authoritative edition could be reached to check the wording (Ideas and Opinions and Out of My Later Years are lending-only on the Internet Archive; the 1941 symposium volume too)."
  primary_system:
    value: PANT
    basis: written_profession
    certainty: 0.7
    cites: [{source: S4, locator: "cable text, 28 April 1929"}, {source: S3, locator: "'Religion and Science' (1930)"}, {source: S5, locator: "§12 Personal"}]
    how_known: "His published cable and essays, plus a scholar (SEP, Mander) who calls him a pantheist. Capped at 0.7: the record names AGNOS and ATHE as alternatives (contested reading, §3), and the cable text reaches us through a newspaper print (secondary quotation)."
    rationale: "Two-part test (PANT use_when). Part 1: 'I believe in Spinoza's God who reveals Himself in the orderly harmony of what exists' (S4) names the God of Deus sive Natura as his God, and rejects a God concerned with human fates. Strictly the wording is 'reveals Himself in', not 'is', the whole; SEP nonetheless reads him as a pantheist (S5). Part 2: the whole has marks beyond feeling, namely order and rationality: 'the orderly harmony of what exists' (S4), 'What a deep conviction of the rationality of the universe' (S3, 1930), 'the ordered regularity of all events' (S3, 1941). Alternatives named: AGNOS (he also speaks of a 'cosmic religious feeling' that 'can give rise to no definite notion of a God and no theology', S3 1930) and ATHE (naturalism with reverent language)."
  secondary_system: {value: UNKNOWN, how_known: "No second system in S1–S5."}
  candidate_codes_considered:
    - {code: AGNOS, reason: "Named alternative. The 1930 essay says the cosmic religious feeling gives 'no definite notion of a God and no theology'. AGNOS is a stub system file (flag).", cites: [{source: S3, locator: "'Religion and Science' (1930)"}]}
    - {code: ATHE, reason: "Named alternative: reverent language without an entity-term. Not chosen, because he keeps the term 'Spinoza's God' and gives it order. ATHE is a stub system file (flag).", cites: [{source: S4, locator: "cable text"}]}
    - {code: JUDA, reason: "Rejected. Jewish descent and childhood instruction only; his adult writing rejects a God who rewards and punishes. Heritage is never a code.", cites: [{source: S1, locator: "Childhood and education"}]}
  lio_axes:
    A_locus:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S4, locator: "cable text"}, {source: S3, locator: "'Science and Religion' part II (1941)"}, {source: S5, locator: "§12"}]
      how_known: "Published cable and essay; capped at 0.7 because a 3 is named below and the cable is a newspaper print."
      rationale: "At the LIO pole: God is 'Spinoza's God who reveals Himself in the orderly harmony of what exists' (S4), and religion should 'give up the doctrine of a personal God' (S3, 1941). Named alternative 3: the 1930 essay's 'marvelous order which reveal themselves both in nature and in the world of thought' and 'reveals Himself in' leave room for a reading where the divine shows itself in the world rather than being identical with it."
    B_cause:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S3, locator: "'Religion and Science' (1930); 'Science and Religion' part II (1941)"}]
      how_known: "Two published essays eleven years apart. Below the 1.0 ceiling for the same reason as C: the key sentences are put in the third person ('the man who is thoroughly convinced', 'for him'), which speaks for his own view only indirectly (§3 same pattern, lens audit batch 2)."
      rationale: "Scored on his account of nature (P6). At the law pole: such a man 'cannot for a moment entertain the idea of a being who interferes in the course of events' (S3, 1930); 'neither the rule of human nor the rule of divine will exists as an independent cause of natural events' (S3, 1941); 'there is no room left by the side of this ordered regularity for causes of a different nature' (S3, 1941). No exception is stated."
    C_ledger:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S3, locator: "'Religion and Science' (1930)"}, {source: S4, locator: "cable text"}]
      how_known: "Published essay and cable. Below the 1.0 ceiling because the key sentence is put in the third person (the man of cosmic religious feeling), which speaks for his view only indirectly."
      rationale: "At the impersonal pole: 'A God who rewards and punishes is inconceivable to him for the simple reason that a man's actions are determined by necessity, external and internal' (S3, 1930); not 'a God who concerns Himself with fates and actions of human beings' (S4). No afterlife judgement in what was read."
    D_authority:
      value: 2
      basis: written_profession
      certainty: 0.7
      cites: [{source: S3, locator: "'Science and Religion' parts I (1939) and II (1941)"}]
      how_known: "Published essays; capped at 0.7 because a 3 is named below. Same pattern of evidence as Planck and Galileo (two domains, each with its own authority), so the same score (§3)."
      rationale: "Mixed, two domains under two authorities. For facts, observation and reason rule: 'science can only ascertain what is, but not what should be' (S3, 1941), and religion that claims 'the absolute truthfulness of all statements recorded in the Bible' intrudes on science (S3, 1941). For the highest ends, another authority: they 'come into being not through demonstration but through revelation, through the medium of powerful personalities', and 'The highest principles for our aspirations and judgments are given to us in the Jewish-Christian religious tradition' (S3, 1939); science 'can teach us nothing else beyond how facts are related to, and conditioned by, each other' (S3, 1939). Named alternative 3: revelation here governs values only and never outranks observation about facts."
    E_scope:
      value: 4
      basis: written_profession
      certainty: 0.7
      cites: [{source: S3, locator: "'Religion and Science' (1930); 'Science and Religion' part II (1941)"}]
      how_known: "Two published essays. Below the 1.0 ceiling because the key sentences are in the third person ('the man who is thoroughly convinced', 'for him'), the same reason C and B are at 0.7 (§3 same pattern)."
      rationale: "Scored on the world's order (P7). One order for all: 'the universal operation of the law of causation' (S3, 1930) covers humans too, since 'a man's actions are determined by necessity' like an inanimate object's motions (S3, 1930), and 'neither the rule of human nor the rule of divine will' is an independent cause (S3, 1941). No favour for a group in events."
  mid_basin:
    value: false
    certainty: 0.7
    cites: [{source: S4, locator: "cable text"}, {source: S3, locator: "1930; 1941"}]
    how_known: "P4 test: A_locus = 4 (≥ 3), so false. Certainty is A's (0.7): the A ≥ 3 branch reads A only (decision P10)."
  statements:
    - text: "Ich glaube an Spinozas Gott der sich in gesetzlicher Harmonie des Seienden offenbart, nicht an Gott der Sich mit Schicksalen und Handlungen der Menschen abgibt."
      note: "English as printed in S4: I believe in Spinoza's God who reveals Himself in the orderly harmony of what exists, not in a God who concerns Himself with fates and actions of human beings."
      cites: [{source: S4, locator: "cable text (German and English as printed)"}]
      date: "1929"
      context: "Cable reply to a New York rabbi (S4 spells him 'Hebert G. Goldstein' of the Institutional Synagogue) who asked 'Do you believe in God?'; printed by the JTA Daily Bulletin of 28 April 1929. S4 does not give the cable's own date."
      axes: [A_locus, C_ledger]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-02
    - text: "The man who is thoroughly convinced of the universal operation of the law of causation cannot for a moment entertain the idea of a being who interferes in the course of events [...]"
      cites: [{source: S3, locator: "'Religion and Science' (1930), Ideas and Opinions pp. 36–40"}]
      date: "1930-11-09"
      context: "New York Times Magazine essay, reprinted in Ideas and Opinions."
      axes: [B_cause, E_scope]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "A God who rewards and punishes is inconceivable to him for the simple reason that a man's actions are determined by necessity, external and internal [...]"
      cites: [{source: S3, locator: "'Religion and Science' (1930)"}]
      date: "1930-11-09"
      axes: [C_ledger, E_scope]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "What a deep conviction of the rationality of the universe [...]"
      cites: [{source: S3, locator: "'Religion and Science' (1930)"}]
      date: "1930-11-09"
      context: "On Kepler and Newton."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "For him neither the rule of human nor the rule of divine will exists as an independent cause of natural events."
      cites: [{source: S3, locator: "'Science and Religion' part II (1941), Ideas and Opinions pp. 41–49"}]
      date: "1941"
      context: "Paper for the 1940 Conference on Science, Philosophy and Religion, published 1941."
      axes: [B_cause, E_scope]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "science without religion is lame, religion without science is blind"
      cites: [{source: S3, locator: "'Science and Religion' part II (1941)"}]
      date: "1941"
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "[...] teachers of religion must have the stature to give up the doctrine of a personal God [...]"
      cites: [{source: S3, locator: "'Science and Religion' part II (1941)"}]
      date: "1941"
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "The highest principles for our aspirations and judgments are given to us in the Jewish-Christian religious tradition."
      cites: [{source: S3, locator: "'Science and Religion' part I (1939 address)"}]
      date: "1939-05-19"
      context: "Address at Princeton Theological Seminary."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "They come into being not through demonstration but through revelation, through the medium of powerful personalities."
      cites: [{source: S3, locator: "'Science and Religion' part I (1939 address)"}]
      date: "1939-05-19"
      context: "On the 'fundamental ends' of conduct, which 'cannot be stated and justified merely by reason'; the next sentences name the Jewish-Christian tradition."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
    - text: "For science can only ascertain what is, but not what should be, and outside of its domain value judgments of all kinds remain necessary."
      cites: [{source: S3, locator: "'Science and Religion' part II (1941)"}]
      date: "1941"
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "primary transcription"
      verified_on: 2026-10-02
  changes_over_life:
    - {value: "Deeply religious at 12, then turned away after reading science books", year: "c. 1891", certainty: 0.7, cites: [{source: S1, locator: "Childhood and education"}], how_known: "Britannica."}
  coder_notes: "PANT is a sourced system file. AGNOS and ATHE (named alternatives) are stub system files: flagged, not sourced in this run. The S3 transcription (sacred-texts) reproduces Ideas and Opinions; page numbers within pp. 36–40 and 41–49 were not checked against the book."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "German Jewish", certainty: 0.7, cites: [{source: S1, locator: "Childhood and education"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Jewish (secular parents)", certainty: 0.7, cites: [{source: S1, locator: "Childhood and education"}], how_known: "Britannica."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: "Jewish religious instruction at home, then at the Luitpold Gymnasium", certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1905–1925", certainty: 0.7, cites: [{source: S2, locator: "Biography"}, {source: S1, locator: "Legacy (Bose-Einstein condensates)"}, {source: S7, locator: "press release"}], how_known: "From light quanta and special relativity (1905) to Bose–Einstein statistics and condensation (1924–1925; range end, P30 #4), the first and last listed lasting contributions (P29). Span check 2026-10-02 (P29, P30 and its addendum): was 1905–1915. S1 (Legacy) names Bose–Einstein condensates among his results that later won Nobel Prizes, so the item was added, dated by the Nobel Foundation's account (S7). Open: S1 also names the 1935 EPR argument, which would end the span in 1935 if listed."}
  age_at_first_lasting_contribution: {value: 26, certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S2, locator: "Biography"}], how_known: "Born March 1879; the 1905 papers."}
  first_evidence_of_lio_type_views: {value: "Cable to Rabbi Goldstein: 'I believe in Spinoza's God'", year: 1929, certainty: 0.7, cites: [{source: S4, locator: "cable text"}], how_known: "Earliest dated statement in the citable sources read. The December 1926 letter to Born ('He does not play dice') is known here only from Britannica's AI-generated Top Questions box, which is not cited (P26). Britannica's childhood account (science books contradicting religion at 12) is earlier but not an LIO view as such."}
  lio_views_relative_to_major_work: {value: "unclear", rationale: "The dated statements read (1929, 1930, 1941) are after the major work. Whether he held them during the 1905–1925 span is not shown in S1–S7.", certainty: 0.5, cites: [{source: S4, locator: "cable text"}, {source: S3, locator: "1930; 1941"}], how_known: "Coder's reading of dates."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "Theory built from two postulates (relativity principle, constancy of light speed) to consequences (S2).", certainty: 0.5, cites: [{source: S2, locator: "Biography"}], how_known: "Coder's reading."}
  form_acquired: {value: "childhood or adolescence", rationale: "The 'sacred little geometry book' at 12 (S1).", certainty: 0.5, cites: [{source: S1, locator: "Childhood and education"}], how_known: "Coder's reading."}
  circle_present: {value: "partly", rationale: "Spinoza's God revealed in the harmony of what exists (S4) is the Deus sive Natura term; the 'reveals Himself in' wording stops short of the full identity.", certainty: 0.5, cites: [{source: S4, locator: "cable text"}], how_known: "Coder's reading."}
  reading: "As belief, not finding: form present and acquired in adolescence; circle partly present. The record does not test H1."
  notes: ""

institutions:
  - {value: "Swiss Patent Office, Bern", role: "technical expert", years: "1902–1909", kind: employer, certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor; Britannica agrees."}
  - {value: "Institute for Advanced Study, Princeton", role: "professor", years: "1933–1955", kind: "research institute", certainty: 0.7, cites: [{source: S2, locator: "Biography (offer of a post at Princeton after the 1932 visit)"}, {source: S1, locator: "Quick Facts"}], how_known: "MacTutor gives a post at Princeton from 1933 and death there (S1). The Institute is not named in the text read, so 0.7 (gap)."}
collaborators:
  - {value: "Marcel Grossmann", relation: collaborator, note: "fellow student at Zürich; helped with the mathematics of general relativity", certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor."}
  - {value: "Max Planck", roster_id: planck-max, relation: "influenced by", note: "Einstein's 1905 light-quantum paper used Planck's quantum hypothesis", certainty: 0.7, cites: [{source: S2, locator: "Biography"}], how_known: "MacTutor."}

review:
  roster_status_reason: {value: "Core in v7.1 (F 5) and v8 (F 5, all five models).", certainty: 0.7, cites: [{source: S6, locator: "roster.csv, rank 6"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "S4 prints the 1929 cable in German and English; the original cablegram was not seen. S4 does not give the cable's own date; S4 spells the rabbi 'Hebert G. Goldstein' (usually Herbert S. Goldstein)."
    - "S3 is a web transcription of Ideas and Opinions; page locators are the book's page ranges given in S3's headnotes."
    - "Britannica (S1) was read as the first page only, plus the Legacy and 'Nazi backlash and coming to America' pages for the span check (2026-10-02); the other later sections were not read."
  open_questions:
    - "Read Jammer, Einstein and Religion (1999), for the 'agnostic' self-descriptions and the full record of his statements, to test AGNOS against PANT."
    - "Check whether any LIO-type religious statement predates 1925, the end of the span (lio_views_relative_to_major_work is unclear)."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Michio Kaku"
    citation: "Kaku, Michio. \"Albert Einstein.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Albert-Einstein."
    url: "https://www.britannica.com/biography/Albert-Einstein"
    accessed: 2026-10-02
    reliability_note: "Signed encyclopedia article; first page read, plus the Legacy and 'Nazi backlash and coming to America' pages (2026-10-02, span check: Bose–Einstein condensates and EPR)."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: tertiary
    kind: encyclopedia
    author: "J. J. O'Connor and E. F. Robertson"
    citation: "O'Connor, J. J. and E. F. Robertson. \"Albert Einstein.\" MacTutor History of Mathematics Archive, University of St Andrews. https://mathshistory.st-andrews.ac.uk/Biographies/Einstein/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Einstein/"
    accessed: 2026-10-02
    reliability_note: "Standard biographical archive."
    used_for: [identity, basics, contribution, childhood, heritage, timing, lane_b, institutions, collaborators]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "Albert Einstein"
    year: 1954
    citation: "Einstein, Albert. \"Religion and Science\" (New York Times Magazine, 9 November 1930) and \"Science and Religion\" (part I, address at Princeton Theological Seminary, 19 May 1939; part II, Science, Philosophy and Religion, A Symposium, 1941). In Ideas and Opinions, New York: Crown, 1954, pp. 36–40 and 41–49. Web transcription at sacred-texts.com."
    url: "https://sacred-texts.com/aor/einstein/einsci.htm"
    accessed: 2026-10-02
    reliability_note: "Transcription of the published essays; headnotes give the original publication. Wording matches the standard English texts."
    used_for: [worldview]
  - id: S4
    type: primary
    kind: other
    author: "Jewish Telegraphic Agency"
    year: 1929
    citation: "\"Professor Einstein Declares His Faith in Spinoza's God.\" Jewish Telegraphic Agency Daily Bulletin, 28 April 1929 (archive page)."
    url: "https://www.jta.org/archive/professor-einstein-declares-his-faith-in-spinozas-god"
    accessed: 2026-10-02
    reliability_note: "Contemporary news report printing the cable in German with an English translation."
    used_for: [worldview, lane_b]
  - id: S5
    type: tertiary
    kind: encyclopedia
    author: "William Mander"
    citation: "Mander, William. \"Pantheism.\" Stanford Encyclopedia of Philosophy. https://plato.stanford.edu/entries/pantheism/."
    url: "https://plato.stanford.edu/entries/pantheism/"
    accessed: 2026-10-02
    reliability_note: "Peer-reviewed entry. §12: 'Einstein was a pantheist but rejected any notion of a personal God'."
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
  - id: S7
    type: tertiary
    kind: "institutional page"
    author: "Royal Swedish Academy of Sciences"
    year: 2001
    citation: "Royal Swedish Academy of Sciences. \"The Nobel Prize in Physics 2001.\" Press release, 9 October 2001. NobelPrize.org. https://www.nobelprize.org/prizes/physics/2001/press-release/."
    url: "https://www.nobelprize.org/prizes/physics/2001/press-release/"
    accessed: 2026-10-02
    reliability_note: "The prize-awarding body's own press release; used only to date the Bose–Einstein item."
    used_for: [contribution]
---

# Albert Einstein

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Albert Einstein (1879–1955) was a German-born theoretical physicist [S1, opening paragraph]. His 1905 papers on light quanta and special relativity and his 1915 general theory of relativity are lasting original contributions; the photoelectric explanation won the 1921 Nobel Prize [S1, opening paragraph; S2, Biography]. His published working worldview rejects a personal God who rewards, punishes or interferes, and names "Spinoza's God" revealed in the order of what exists [S4, cable text; S3, 1930 and 1941]. Coded PANT at 0.7, with AGNOS and ATHE as named alternatives; not mid-basin.

## Life and work

Born in Ulm, Württemberg, he grew up in Munich, finished school at Aarau and trained at the Zürich Polytechnic [S1, Childhood and education; S2, Biography]. He worked at the Bern patent office from 1902 to 1909, where the 1905 papers were written, then held chairs in Zürich, Prague and Berlin, and from 1933 worked in Princeton [S2, Biography; S1, Quick Facts].

## Contribution and impact

Light quanta (1905), special relativity and mass–energy equivalence (1905), and general relativity (1915) [S2, Biography]. MacTutor: "Einstein contributed more than any other scientist to the modern vision of physical reality" [S2, Summary].

## Childhood and education

His parents were secular, middle-class Jews [S1, Childhood and education]; he had Jewish religious instruction at home and then at the Luitpold Gymnasium [S2, Biography]. He became deeply religious at 12, then turned away after reading science books [S1, Childhood and education]. At 12 he read a geometry book he called his "sacred little geometry book"; the medical student Max Talmud tutored him in mathematics and philosophy [S1, Childhood and education].

## Adult working worldview

In 1929 he cabled: "I believe in Spinoza's God who reveals Himself in the orderly harmony of what exists, not in a God who concerns Himself with fates and actions of human beings" [S4, cable text]. The 1930 essay says the man convinced of universal causation "cannot for a moment entertain the idea of a being who interferes in the course of events", and that "A God who rewards and punishes is inconceivable to him" [S3, 1930]. In 1941 he asked teachers of religion to "give up the doctrine of a personal God" and wrote that "science without religion is lame, religion without science is blind" [S3, 1941]. SEP's pantheism entry calls him a pantheist [S5, §12]. Scores: A 4 (0.7), B 4 (0.7), C 4 (0.7), D 2 (0.7), E 4 (0.7); mid_basin false.

## Heritage (context only)

German Jewish, secular parents [S1, Childhood and education]. Context only.

## Timing

First lasting contribution 1905, at 26 [S2, Biography]. The religious statements read date from 1929 on [S4, cable text; S3]; timing relative to the major work is unclear.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Deductive form from postulates is present and a geometry book at 12 is recorded [S1, Childhood and education]; the circle is partly present through "Spinoza's God" [S4, cable text].

## Open questions

- Span check (2026-10-02, P29/P30): primary_system (PANT 0.7), A_locus (4 at 0.7), B_cause (4 at 0.7), C_ledger (4 at 0.7), D_authority (2 at 0.7), E_scope (4 at 0.7), mid_basin (false at 0.7) rest on evidence outside the new span 1905–1925. Values left unchanged pending a ruling; details in reports/p30_span_alignment.csv.
- Read Jammer, Einstein and Religion, to test AGNOS against PANT.
- Check for religious statements before 1925, the end of the span.

## Research log

- 2026-10-02: Read Britannica (first page), MacTutor, SEP "Einstein's Philosophy of Science" (no religion content, not cited), the sacred-texts transcription of the 1930 and 1939/1941 essays, the JTA 1929 report and SEP "Pantheism" §12. All quotations checked word for word against these pages. Not read: Jammer, the Collected Papers, the later Britannica sections.
