---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch K; deepen D1 queue #69)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to biology. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch K, order P32: F 5, rank 70). Basics from Britannica (Britannica Editors, unsigned; Top Questions not cited) and NIH/NLM Profiles in Science. Worldview from her 1940 letter to her father, quoted by NLM and in Brenda Maddox's New Humanist article (2007), both secondary quotations of a private letter. Scientist under P30 (coal micro-structure, DNA, virus structure). primary_system AGNOS (0.5, alt ATHE); A 4 (0.5, alt 3); B 3 (0.5, alt 4) from working science (P35); mid_basin BELOW_THRESHOLD. Plotted (faded). Draft, not reviewed."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Audit fixes (fallacy_catalog audit of 2d75649, run 1). The 'faith is essential' wording is cited to Maddox (S3) only, with a note on NLM's shorter variant; added her line 'faith in this world is perfectly possible without faith in another world' (S3). A stays 4 (0.5, alternative 3)."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #69). P47 source_quality on S1–S9. Added Maddox Dark Lady of DNA (2002) S5 (letter pp. 60–61 per todayinsci; IA borrow 401); Wikipedia dual bio S6 (P50); Humanists UK Heritage S7 (fuller letter + this-world faith); Patricia Fara / Rosalind Franklin Institute S8 ('agnostic by inclination'); NLM OCR of Franklin & Gosling Nature draft 17 Mar 1953 S9 (primary / own words). Extended major_work_period / working_years to 1945–1958 (virus TMV lasting work through Birkbeck; Nature 1955 Structure of Tobacco Mosaic Virus bibliographic). A_locus stays 4 @0.5; support single → corroborated (S5+S3+S7 cite the 1940 letter; P18 ceiling still 0.5; P38 AGNOS-compatible 'if such there be' + denial of interested personal God; named alt 3). B_cause stays 3 @0.5; basis inference_from_work → written_profession via S9 least-energy / helical physical structure; support single → corroborated (S9 + S2; P48). primary_system AGNOS @0.5 backed by Fara S8 + letter; secondary_system SECHUM @0.5 from this-world faith. mid_basin BELOW_THRESHOLD (A cert < 0.7). Chart: faded filled (A and B both corroborated at 0.5; darkness = min cert still faded). A corroboration is multi-citation of one letter (S5/S3/S7). No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: franklin-rosalind
  display_name: "Rosalind Franklin"
  roster:
    canonical_name: "Rosalind Franklin"
    rank: 70
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: biology
    field_bucket: "biology / life science"
  full_name: {value: "Rosalind Elsie Franklin", certainty: 0.7, cites: [{source: S1, locator: "header ('In full')"}], how_known: "Britannica."}
  native_name: {value: UNKNOWN, how_known: "English."}
  aliases: []

basics:
  birth:
    date: {value: "1920-07-25", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "paragraph 1"}], how_known: "Britannica and NLM agree."}
    place: {value: "London, England", modern_name: "London, United Kingdom", polity_then: "United Kingdom", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "paragraph 1"}], how_known: "Two sources."}
  death:
    date: {value: "1958-04-16", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "cancer paragraph"}], how_known: "Two sources."}
    place: {value: "London, England", modern_name: "London, United Kingdom", polity_then: "United Kingdom", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "cancer paragraph"}], how_known: "Two sources."}
  first_lasting_contribution_year: {value: 1945, certainty: 0.5, cites: [{source: S2, locator: "BCURA paragraph"}, {source: S1, locator: "paragraph 2"}], how_known: "Coal micro-structure ('molecular sieves') work at BCURA, 1942–46, documented in her 1945 Cambridge doctoral thesis; the thesis is the earliest dated public record read (P30); the papers are not individually dated in what was read (0.5)."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "Birth year bucket (P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "United Kingdom (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "London and Cambridge; Paris 1947–50."}
  sex_as_recorded: {value: "female", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [English, French], certainty: 0.5, cites: [{source: S2, locator: "paragraph 1; Paris paragraph"}], how_known: "Coder's reading (0.5)."}
  occupations: {value: ["physical chemist", "crystallographer"], certainty: 0.7, cites: [{source: S2, locator: "paragraph 1"}], how_known: "NLM."}
contribution:
  primary_domain: biology
  fields: {value: ["physical chemistry", "X-ray crystallography", "structural biology"], certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "text"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Micro-structure of coals: pores with molecular-level constrictions acting as 'molecular sieves'", year: 1945, kind: discovery, lasting: "'made it possible to classify coals and predict their performance' (S2)", certainty: 0.5, cites: [{source: S2, locator: "BCURA paragraph"}], how_known: "Dated by the 1945 thesis (0.5)."}
    - {value: "X-ray evidence that DNA is helical; both forms with phosphate groups outward; B-form dimensions", year: 1953, kind: discovery, lasting: "'laid the foundation' for the Watson–Crick double helix (S1); Nature note with Gosling (S9)", certainty: 0.7, cites: [{source: S1, locator: "King's College paragraph"}, {source: S2, locator: "King's paragraph"}, {source: S9, locator: "draft 17 Mar 1953 (helical structure B; phosphates on ~20 Å helix)"}], how_known: "NLM OCR of her Nature draft read; conclusion reached by early 1953 (S2)."}
    - {value: "Tobacco mosaic virus structure: uniform particle length; RNA placement relative to protein helix", year: 1955, kind: discovery, lasting: "First major structural account of TMV; model work continued through 1956–58 with Klug (S2 viruses feature; Nature 175, 379 bibliographic)", certainty: 0.5, cites: [{source: S2, locator: "viruses feature (Birkbeck 1953–1958)"}, {source: S6, locator: "Birkbeck / TMV"}, {source: S8, locator: "tobacco mosaic virus"}], how_known: "NLM viruses feature and Fara; 1955 Nature paper not opened this pass (0.5)."}
  evidence_of_impact:
    - {value: "Crick 'later admitted that Franklin was two steps away from realizing the correct structure'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S2, locator: "Cavendish paragraph"}], how_known: "NLM."}
  major_works:
    - {value: "Molecular Configuration in Sodium Thymonucleate (Nature 171: 740–741, with R. G. Gosling)", year: 1953, kind: "paper or paper series", certainty: 0.7, cites: [{source: S9, locator: "draft title / 17 Mar 1953"}, {source: S2, locator: "King's paragraph"}], how_known: "NLM draft OCR; published Nature citation standard."}
    - {value: "Structure of Tobacco Mosaic Virus (Nature 175: 379, 1955)", year: 1955, kind: "paper or paper series", certainty: 0.5, cites: [{source: S2, locator: "viruses feature"}], how_known: "Bibliographic via NLM narrative; full text unread."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1, S2).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Anglo-Jewish", certainty: 0.7, cites: [{source: S2, locator: "paragraph 1"}, {source: S3, locator: "family paragraph"}], how_known: "NLM; Maddox: 'not overly religious', father expected the rituals to be followed."}
  family_religious_practice: {value: "Observant of rituals by the father's expectation, 'not overly religious'", certainty: 0.5, cites: [{source: S3, locator: "family paragraph"}], how_known: "Maddox (0.5)."}
  parents_and_household:
    - {value: "Father Ellis Franklin, partner at Keyser's Bank; mother Muriel", role: parents, certainty: 0.7, cites: [{source: S2, locator: "paragraph 1"}], how_known: "NLM."}
  household_circumstances: {value: "Second of five children in a prominent Anglo-Jewish banking and publishing family", certainty: 0.7, cites: [{source: S2, locator: "paragraph 1"}], how_known: "NLM."}
  schooling:
    - {value: "St Paul's Girls' School, London", stage: "grammar or secondary school", run_by: private, certainty: 0.7, cites: [{source: S1, locator: "paragraph 2"}, {source: S2, locator: "paragraph 1"}], how_known: "Two sources."}
    - {value: "Newnham College, Cambridge (1938–41), physical chemistry", stage: university, run_by: other, certainty: 0.7, cites: [{source: S1, locator: "paragraph 2"}, {source: S2, locator: "paragraph 2"}], how_known: "Two sources."}
  early_mathematics: {value: "other", note: "Early aptitude for mathematics and science; took science at sixteen (level not specified).", certainty: 0.5, cites: [{source: S2, locator: "paragraphs 1–2"}], how_known: "NLM, quoting her mother."}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure:
    - {value: "Early aptitude for math and science; took science 'at sixteen'", certainty: 0.7, cites: [{source: S2, locator: "paragraphs 1–2"}], how_known: "NLM, quoting her mother."}
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [English], certainty: 0.5, cites: [{source: S2, locator: "paragraph 1"}], how_known: "Coder's reading."}
  notable_events:
    - {value: "As a young child refused to believe in the existence of God; asked 'how do you know He isn't She?' (mother's recollection)", certainty: 0.5, cites: [{source: S6, locator: "Personal life (Glynn p. 12)"}], how_known: "Wikipedia citing Glynn; childhood, off-point for adult A (P29)."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1945–1958", certainty: 0.5, cites: [{source: S2, locator: "BCURA; King's; viruses feature"}], how_known: "Equals timing.major_work_period (coal thesis through Birkbeck virus work to death)."}
  nominal_affiliations:
    - {value: "Joined the Jewish Society at Cambridge 'to please her grandfather, but disliked it'", years: "1938", role: "nominal member", certainty: 0.5, cites: [{source: S3, locator: "family paragraph"}], how_known: "Maddox (0.5)."}
  self_described_science_religion_relation: {value: "'Science and everyday life cannot and should not be separated. Science, for me, gives a partial explanation of life. In so far as it goes, it is based on fact, experience and experiment' (letter to her father, 1940).", certainty: 0.5, cites: [{source: S5, locator: "pp. 60–61 (per todayinsci)"}, {source: S3, locator: "letter quotation"}, {source: S2, locator: "epigraph (shorter variant)"}, {source: S7, locator: "letter block"}], how_known: "Private letter, secondary quotation; wording checked across Maddox New Humanist (S3), Humanists UK (S7), and NLM epigraph (S2); printed scholarly source Maddox 2002 pp. 60–61 (S5; page images not opened). One letter, so 0.5 (P18)."}
  primary_system:
    value: AGNOS
    basis: scholarly_reconstruction
    certainty: 0.5
    cites: [{source: S5, locator: "pp. 60–61 ('a creator ..., if such there be')"}, {source: S3, locator: "letter quotation"}, {source: S8, locator: "'agnostic by inclination'"}, {source: S6, locator: "Personal life ('best described as an agnostic')"}]
    rationale: "1940 letter leaves a creator open ('if such there be') while denying any interest in us; rejects afterlife-faith. Fara (S8) and Wikipedia (S6, citing Fara) reconstruct her as agnostic; Maddox calls her 'passionately secular'. Named alternatives: ATHE (no positive belief; deathbed refusal of religious comfort is Maddox's narration, not her words) and SECHUM ('faith in this world')."
    how_known: "Single private letter (P18 → 0.5) plus independent scholarly reconstructions (Fara S8; Wiki S6). Letter predates the working years; no change documented through death (P31); Maddox deathbed episode (S3) is continuity colour, not a second A document."
  secondary_system:
    value: SECHUM
    basis: scholarly_reconstruction
    certainty: 0.5
    cites: [{source: S3, locator: "letter quotation ('faith in this world')"}, {source: S7, locator: "humanist framing / this-world faith"}]
    how_known: "Letter's this-world faith and improvement of mankind; Humanists UK reads it as humanist. Not the primary code (AGNOS fits the open creator clause better)."
  candidate_codes_considered:
    - {code: AGNOS, reason: "'if such there be' leaves a creator open; Fara: 'agnostic by inclination'."}
    - {code: ATHE, reason: "Rejects an afterlife and any interested creator; Maddox: 'passionately secular'; Humanists paraphrase 'disbelief in … a god'."}
    - {code: SECHUM, reason: "'faith in this world is perfectly possible without faith in another world'; improvement of the lot of mankind (S3, S7)."}
  lio_axes:
    A_locus:
      value: 4
      basis: scholarly_reconstruction
      certainty: 0.5
      support: corroborated
      cites: [{source: S5, locator: "pp. 60–61 (creator 'if such there be' / no reason to be interested)"}, {source: S3, locator: "letter quotation"}, {source: S7, locator: "letter block"}]
      how_known: "One private letter, secondary quotation (P18 single-letter ceiling 0.5 with scholar backing). Adult evidence with no documented change (P31). Distinct source ids S5+S3+S7 → corroborated under P48 count; same letter text. Named alternative 3."
      rationale: "Explicit denial of a personal, interested God (§ A_locus, P20 / P38): 'I see no reason to believe that a creator of protoplasm or primeval matter, if such there be, has any reason to be interested in our insignificant race'. Positive view is this-world only. AGNOS-compatible open clause + disbelief in interested personal God → A 4 at most 0.5 (P38), alternative 3 (remote creator left open)."
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.5
      support: corroborated
      cites: [{source: S9, locator: "draft 17 Mar 1953 (helical structure B; least-energy configuration; phosphates on ~20 Å helix)"}, {source: S2, locator: "BCURA; King's; viruses feature (coal–DNA–TMV working science)"}]
      how_known: "Her own Nature draft (S9) plus NLM's documented coal–DNA–virus program (S2). Scientist under P30. Named alternative 4, so 0.5 (P16 Hilbert / P35). Two independent source ids → corroborated (P48)."
      rationale: "Scored on her account of nature (P6). S9: structure B fibres take a least-energy configuration; helical form highly probable; phosphate geometry fixed by X-ray regularities — lawful physical structure in her own words, with no stated miracle / no-exception claim → B 3 at 0.5, alternative 4 (P16 Hilbert; P35). Letter line 'Science … is based on fact, experience and experiment' is method, not B (P16). Named alternative: 4."
    C_ledger: {value: UNKNOWN, how_known: "She rejects 'belief in life after death' as the definition of faith, but says nothing of moral reckoning; not scored."}
    D_authority: {value: UNKNOWN, how_known: "Not read."}
    E_scope: {value: BELOW_THRESHOLD, note: "Scored on the world's order (P7); not scored from working science alone (P19).", how_known: "The creator would not be interested 'in our insignificant race' concerns A, not group favour (P7); working science does not fill E."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A 4 is scored only at 0.5, under the 0.7 bar for the A ≥ 3 branch (P10).", note: "If A reached 0.7 the result would be false."}
  statements:
    - text: "I agree that faith is essential to success in life (success of any sort) but I do not accept your definition of faith, i.e. belief in life after death."
      cites: [{source: S3, locator: "letter quotation"}, {source: S5, locator: "pp. 60–61"}, {source: S7, locator: "letter block"}]
      date: "1940"
      context: "Letter to her father Ellis Franklin, summer 1940, at Cambridge (S3, S5, S7)."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Wording as in Maddox New Humanist (S3) / Humanists UK (S7). Printed scholarly source Maddox 2002 pp. 60–61 (S5; todayinsci locator; book page images not opened — IA 401). NLM epigraph (S2) prints a shorter variant."
    - text: "Anyone able to believe in all that religion implies obviously must have such faith, but I maintain that faith in this world is perfectly possible without faith in another world"
      cites: [{source: S3, locator: "letter quotation"}, {source: S7, locator: "letter block"}]
      date: "1940"
      context: "Same letter, next sentences."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
    - text: "I see no reason to believe that a creator of protoplasm or primeval matter, if such there be, has any reason to be interested in our insignificant race in a tiny corner of the universe, and still less in us, as still more insignificant individuals."
      cites: [{source: S3, locator: "letter quotation"}, {source: S5, locator: "p. 61 (per todayinsci)"}, {source: S6, locator: "Personal life"}]
      date: "1940"
      context: "Same letter; Maddox prints an ellipsis before it in New Humanist."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Full creator passage in S3; locator to Maddox 2002 p. 61 via todayinsci and Wikipedia (S6)."
    - text: "Again, I see no reason why the belief that we are insignificant or fortuitous should lessen our faith – as I have defined it."
      cites: [{source: S3, locator: "letter quotation"}, {source: S7, locator: "letter block"}]
      date: "1940"
      context: "Same letter, closing the creator passage."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
    - text: "Structure B is derived from the crystalline structure A when the sodium thymonucleate (NaDNA) fibres take up quantities of water in excess of about 40% of their weight. … each unit being shielded by a sheath of water. Each unit is therefore free to take up its least-energy configuration independently of its neighbours and, in view of the nature of the long-chain molecules involved, it is highly likely that the general form will be helical."
      cites: [{source: S9, locator: "draft pp. 1–2 (OCR)"}]
      date: "1953-03-17"
      context: "Rough draft of the Nature note with Gosling, dated 17 March 1953 (S9)."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-24
      note: "NLM Profiles OCR of the draft manuscript (collections.nlm.nih.gov/ocr/…); published as Nature 171: 740–741 (25 Apr 1953)."
  changes_over_life: []
  coder_notes: "Coder's call; one 1940 letter remains the sole A document (P18/P48). Maddox's deathbed narration (surgeon urged religion; she was furious) is continuity colour under P31, not a second A statement. Maddox 2002 ch. 4 / pp. 60–61 page images still unread (IA 401). Glynn My Sister Rosalind Franklin (2012) unread beyond Wikipedia locators. No fallacy_catalog (Jason)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Anglo-Jewish", certainty: 0.7, cites: [{source: S2, locator: "paragraph 1"}, {source: S8, locator: "Anglo-Jewish network"}], how_known: "NLM; Fara."}
  religious_heritage_by_birth: {value: "Jewish", certainty: 0.7, cites: [{source: S2, locator: "paragraph 1"}, {source: S3, locator: "family paragraph"}], how_known: "Two sources."}
  baptism_or_initiation: {value: "none (Jewish; Hebrew lessons at Lindores School while friends went to church)", certainty: 0.5, cites: [{source: S6, locator: "Personal life (Glynn p. 19)"}], how_known: "Wikipedia citing Glynn; no Christian baptism."}
  childhood_catechism: {value: "Family expected Jewish rituals; she was 'always consciously a Jew' as an adult cultural identity without religious faith", certainty: 0.5, cites: [{source: S6, locator: "Personal life ('always consciously a Jew'; Maddox p. 61)"}, {source: S3, locator: "family paragraph"}], how_known: "Wikipedia / Maddox; cultural identity, not a creed."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1945–1958", certainty: 0.5, cites: [{source: S2, locator: "BCURA; King's; viruses feature"}], how_known: "First to last dated listed contribution (P29, P30): 1945 coal thesis through Birkbeck virus work ending at her death 1958."}
  age_at_first_lasting_contribution: {value: 25, certainty: 0.5, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "BCURA paragraph"}], how_known: "1945 − 1920 = 25 (P30)."}
  first_evidence_of_lio_type_views: {value: "1940, age 20: a creator, 'if such there be', has no reason 'to be interested in our insignificant race'", year: 1940, age: 20, certainty: 0.5, cites: [{source: S5, locator: "p. 61"}, {source: S3, locator: "letter quotation"}], how_known: "Earliest document read; nothing earlier known (childhood God-refusal is off-point, P29)."}
  lio_views_relative_to_major_work: {value: "before major work", certainty: 0.5, cites: [{source: S3, locator: "letter quotation"}], how_known: "1940 letter; work dated from 1945; no later worldview document read (P31 continuity assumed)."}
  worldview_during_major_work: {value: AGNOS, certainty: 0.5, cites: [{source: S5, locator: "pp. 60–61"}, {source: S8, locator: "'agnostic by inclination'"}], how_known: "As primary_system; adult letter + Fara; no change documented."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Crystallographic helices in DNA/TMV are scientific form, not a Lane B geometric theology.", certainty: 0.5, cites: [{source: S9, locator: "helical structure B"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "text"}], how_known: "Not read."}
  circle_present: {value: "no", rationale: "No God placed as source or end in what was read.", certainty: 0.5, cites: [{source: S3, locator: "letter quotation"}], how_known: "Coder's reading."}
  reading: "Secular / agnostic; one letter plus scholarly AGNOS label; this-world faith (SECHUM alt)."
  notes: "Deathbed fury at religious comfort (Maddox S3) is biographer narration."

institutions:
  - {value: "British Coal Utilisation Research Association", role: researcher, kind: "research institute", certainty: 0.7, cites: [{source: S1, locator: "paragraph 2"}], how_known: "Britannica."}
  - {value: "King's College London (Biophysics Unit)", role: "research fellow", kind: university, certainty: 0.7, cites: [{source: S1, locator: "King's College paragraph"}], how_known: "Britannica."}
  - {value: "Birkbeck College, London", role: researcher, kind: university, certainty: 0.7, cites: [{source: S1, locator: "Birkbeck paragraph"}], how_known: "Britannica."}
collaborators:
  - {value: "Raymond Gosling", relation: "student or assistant", certainty: 0.7, cites: [{source: S2, locator: "King's paragraph"}, {source: S9, locator: "co-author"}], how_known: "NLM; Nature draft."}
  - {value: "Aaron Klug", relation: collaborator, certainty: 0.7, cites: [{source: S2, locator: "Birkbeck / viruses paragraph"}], how_known: "NLM."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 70"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags: []
  open_questions:
    - "Page-check Maddox, The Dark Lady of DNA (2002), pp. 60–61 and ch. 4 (IA borrow blocked)."
    - "Read Glynn, My Sister Rosalind Franklin (2012), esp. pp. 12, 19, 62."
    - "Open Franklin & Gosling, Nature 172: 156–157 (1953) and Nature 175: 379 (1955 TMV) for a second B own-word paper."
    - "Willesden tomb English inscription wording beyond Wikipedia (secular scientist memorial with Hebrew name line)."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "Britannica Editors. \"Rosalind Franklin.\" Encyclopaedia Britannica, updated 14 October 2026. https://www.britannica.com/biography/Rosalind-Franklin."
    url: "https://www.britannica.com/biography/Rosalind-Franklin"
    accessed: 2026-10-15
    source_quality: "reference entry"
    reliability_note: "Unsigned editors' body; Top Questions not cited."
    used_for: [identity, basics, contribution, childhood, timing, institutions]
  - id: S2
    type: secondary
    kind: "institutional page"
    author: "U.S. National Library of Medicine"
    citation: "U.S. National Library of Medicine. \"Biographical Overview\"; also \"The DNA Riddle\" and \"Envisioning Viruses\" features. Rosalind Franklin Papers, Profiles in Science. https://profiles.nlm.nih.gov/spotlight/kr/feature/biographical."
    url: "https://profiles.nlm.nih.gov/spotlight/kr/feature/biographical"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Unsigned institutional overview; quotes the 1940 letter with an ellipsis; viruses feature used for Birkbeck TMV span."
    used_for: [basics, contribution, childhood, worldview, heritage, timing, collaborators]
  - id: S3
    type: secondary
    kind: other
    author: "Brenda Maddox"
    citation: "Maddox, Brenda. \"Mother of DNA.\" New Humanist, 31 May 2007. https://newhumanist.org.uk/articles/mother-of-dna/."
    url: "https://newhumanist.org.uk/articles/mother-of-dna/"
    accessed: 2026-10-24
    source_quality: "scholarly reconstruction"
    reliability_note: "By her biographer, in a humanist magazine; quotes the 1940 letter at length; deathbed surgeon episode is her narration."
    used_for: [childhood, worldview, heritage, timing, lane_b]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    source_quality: "study roster"
    reliability_note: "Study's own roster."
    used_for: [identity, review]
  - id: S5
    type: secondary
    kind: "scholarly book"
    author: "Brenda Maddox"
    year: 2002
    citation: "Maddox, Brenda. Rosalind Franklin: The Dark Lady of DNA. New York: HarperCollins, 2002, pp. 60–61 (1940 letter excerpts)."
    accessed: 2026-10-24
    source_quality: "scholarly edition or monograph"
    reliability_note: "Standard scholarly biography; letter locators pp. 60–61 via todayinsci and Wikipedia. Full page images not opened this pass (Archive.org borrow 401). Same author as S3."
    used_for: [worldview, timing]
  - id: S6
    type: secondary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia. \"Rosalind Franklin,\" Personal life; Illness, death, and burial. https://en.wikipedia.org/wiki/Rosalind_Franklin."
    url: "https://en.wikipedia.org/wiki/Rosalind_Franklin"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Dual bio (P50). 'Best described as an agnostic' cites Fara/RFI (S8). Childhood God-refusal and Hebrew lessons cite Glynn; letter cites Maddox p. 61; tomb at Willesden United Synagogue."
    used_for: [contribution, childhood, worldview, heritage, timing]
  - id: S7
    type: secondary
    kind: "institutional page"
    author: "Humanists UK (Humanist Heritage)"
    citation: "Humanists UK. \"Rosalind Franklin (1920–1958).\" Humanist Heritage. https://heritage.humanists.uk/rosalind-franklin/."
    url: "https://heritage.humanists.uk/rosalind-franklin/"
    accessed: 2026-10-24
    source_quality: "scholarly reconstruction"
    reliability_note: "Institutional humanist heritage page; prints long 1940 letter excerpts and frames this-world faith as humanist. Not independent of Maddox for the letter text."
    used_for: [worldview]
  - id: S8
    type: secondary
    kind: "institutional page"
    author: "Patricia Fara"
    citation: "Fara, Patricia. \"Rosalind Franklin's Life.\" The Rosalind Franklin Institute. https://www.rfi.ac.uk/discover-learn/rosalind-franklins-life/."
    url: "https://www.rfi.ac.uk/discover-learn/rosalind-franklins-life/"
    accessed: 2026-10-24
    source_quality: "scholarly reconstruction"
    reliability_note: "Signed essay by a historian of science (ex-President, British Society for the History of Science): 'even though she was agnostic by inclination, she was proud of her Jewish identity'."
    used_for: [contribution, worldview, heritage, timing]
  - id: S9
    type: primary
    kind: "published work by the subject"
    author: "Rosalind E. Franklin and R. G. Gosling"
    year: 1953
    citation: "Franklin, Rosalind E., and R. G. Gosling. Rough draft of \"A Note on Molecular Configuration in Sodium Thymonucleate,\" 17 March 1953 (published Nature 171: 740–741, 25 April 1953). NLM Profiles in Science OCR: https://collections.nlm.nih.gov/ocr/nlm:nlmuid-101584586X136-doc."
    url: "https://profiles.nlm.nih.gov/spotlight/kr/catalog/nlm:nlmuid-101584586X136-doc"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "NLM OCR of her draft manuscript co-authored with Gosling; used for B written_profession. Published Nature PDF paywalled this pass."
    used_for: [contribution, worldview, collaborators, lane_b]
---

# Rosalind Franklin

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Rosalind Franklin (1920–1958), British physical chemist and crystallographer [S1, S2]. Deepen D1: primary_system AGNOS (0.5, alt ATHE/SECHUM); secondary_system SECHUM (0.5); A 4 at 0.5 support corroborated; B 3 at 0.5 support corroborated (written_profession); mid_basin BELOW_THRESHOLD. Plotted (faded filled).

## Life and work

Cambridge; BCURA; Paris; King's College; Birkbeck (TMV) [S1, S2].

## Contribution and impact

Coal micro-structure; DNA helical structure (Nature 1953 with Gosling) [S9]; virus structure [S2].

## Childhood and education

St Paul's Girls' School; Newnham College [S2]. Anglo-Jewish; Hebrew lessons at Lindores; no Christian baptism [S6].

## Adult working worldview

1940 letter: faith 'in this world is perfectly possible without faith in another world'; creator 'if such there be' uninterested [S3, S5, S7]. Fara: 'agnostic by inclination' [S8].

## Heritage (context only)

Anglo-Jewish; 'always consciously a Jew' culturally; Willesden United Synagogue burial [S2, S6].

## Timing

First lasting contribution dated 1945, at 25; major work through virus research to 1958 [S2].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No circle [S3].

## Open questions

- Maddox 2002 pp. 60–61 page images; Glynn 2012; Nature 172 / 175 full text.

## Research log

- 2026-10-15: Read Britannica (Editors), NLM Profiles in Science overview and Maddox in New Humanist (2007).
- 2026-10-24: Deepen D1. Maddox 2002 locators; Wikipedia Personal life; Humanists UK Heritage; Fara/RFI; NLM OCR Nature draft 17 Mar 1953; NLM DNA and viruses features. No fallacy_catalog.
