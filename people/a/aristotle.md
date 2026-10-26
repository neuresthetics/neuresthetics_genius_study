---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch D)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: '2026-10-25'
  change_log:
    - {date: 2026-10-25, by: "Grok Bot", summary: "Perpetual deepen: score C_ledger 4 (0.5), D_authority 4 (0.7), E_scope 4 (0.7) from EN X (Ross MIT, new S9) and Met. XII tradition/myth (S2/S6/S7). C impersonal eudaimonia with named alt 1 (EN X.8 gods-reward philosopher). D reason over mythic tradition (Met Λ). E same natural order (Phys II.8 + Met Λ divine encloses nature); P7 sends EN X.8 reward to C. Mid_basin unchanged true. Chart-moving: no (A/B already plotted). No figures/; no fallacy_catalog."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch D, order P32: F 5, rank 9). Basics from SEP (Shields 2020). Worldview from Metaphysics XII (Ross trans.), Physics II (Hardie and Gaye trans.) and Nicomachean Ethics III (Ross trans.), read in the MIT Internet Classics Archive web copies. primary_system ARIST (0.7, founder rule); A_locus 1 (0.7, alternative 2); B_cause 3 (0.7, alternative 4); mid_basin true (0.7). C, D, E TODO. Draft, not reviewed."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Audit fixes (fallacy_catalog audit of 3f4817e, run 1). B_cause 3 kept (0.7, alternative 4) but reframed: free will placed in nature (§6 B 3 anchor), not an exception to lawful cause; added EN 1113b17-19, Met. Θ.2 1046b4-7, Θ.5 1048a5-11 and the compatibilist alternative EN 1114a13-21; chance noted as incidental cause. Bekker numbers verified, approximate caveats removed. mid_basin true (0.7) unchanged."}
    - {date: 2026-10-23, by: "Grok Bot", summary: "Deepen pass D1 (queue #9). P47 source_quality on every source. A_locus was single (S2 MIT unofficial Ross only): added Tredennick Loeb Metaphysics XII via Perseus (S6 scholarly edition) and Ross Oxford Works VIII Metaphysica 1908 (S7 scholarly edition, archive.org OCR) confirming the same Λ.7/Λ.10 passages; support single → corroborated (S6+S7); value/certainty stay 1 @ 0.7 (named alt 2). B_cause already multi-cited (S3+S4+S2); labelled support corroborated. Basics dual-sourced SEP+MacTutor (S8): birth/death dates and places → 1.0. A statements verified_against → scholarly edition. Chart: dark hollow → dark filled (fill cue). No fallacy_catalog (Jason 2026-10-23). Draft, not reviewed."}

identity:
  id: aristotle
  display_name: "Aristotle"
  roster:
    canonical_name: "Aristotle"
    rank: 9
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: philosophy
    field_bucket: philosophy
  full_name: {value: "Aristotle", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S8, locator: "title / Quick Info"}], how_known: "SEP and MacTutor agree."}
  native_name: {value: "Aristotelēs (Ἀριστοτέλης)", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S8, locator: "opening (Greek form in secondary accounts)"}], how_known: "Standard Greek name; SEP English form; MacTutor biography of the same person."}
  aliases:
    - {name: "the Stagirite", kind: "title or honorific"}

basics:
  birth:
    date: {value: "-384", certainty: 1.0, cites: [{source: S1, locator: "§1 ('Born in 384 B.C.E.')"}, {source: S8, locator: "Quick Info ('Born 384 BC Stagirus')"}], how_known: "SEP and MacTutor agree."}
    place: {value: "Stagira, Macedonian region of northeastern Greece", modern_name: "Stagira, Greece", polity_then: "Stagira (Chalcidice)", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S8, locator: "Quick Info; opening ('Stagirus, or Stagira… Chalcidic peninsula')"}], how_known: "SEP and MacTutor agree (Stagira/Stagirus)."}
  death:
    date: {value: "-322", certainty: 1.0, cites: [{source: S1, locator: "§1 ('died there of natural causes the following year, in 322')"}, {source: S8, locator: "Quick Info ('Died 322 BC Chalcis'); body ('died the following year… at the age of 62')"}], how_known: "SEP and MacTutor agree."}
    place: {value: "Chalcis, Euboea", modern_name: "Chalcis, Greece", polity_then: "Chalcis", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S8, locator: "Quick Info; body (retired to Chalcis, mother's family house)"}], how_known: "SEP and MacTutor agree."}
  first_lasting_contribution_year: {value: UNKNOWN, how_known: "SEP does not date the treatises; it says the surviving works read like lecture notes and drafts 'first written and then reworked' (§2). Every candidate year lies between c. 367 BC (arrival at the Academy at about seventeen) and his death in 322 BC (P30 death cap)."}
  era_bucket: {value: "-500 to 499", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S8, locator: "Quick Info (384–322 BC)"}], how_known: "Every candidate year (c. 367–322 BC) is in '-500 to 499' (P2); two sources."}
  region_of_birth: {value: "Southern Europe", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S8, locator: "Quick Info (Macedonia, Greece)"}], how_known: "Greece is Southern Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "§1 (Athens, Assos, Lesbos, Pella)"}, {source: S8, locator: "body (Academy, Assos, Lyceum)"}], how_known: "Mostly Athens; Assos (now Turkey, Middle East and North Africa) for about three years. Coder's reading of where most work was done."}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S8, locator: "throughout"}], how_known: "As the sources record it."}
  languages_of_work: {value: [Greek], certainty: 1.0, cites: [{source: S1, locator: "§§2–5 (Greek terms)"}, {source: S8, locator: "body (wrote fine Greek prose)"}], how_known: "SEP and MacTutor."}
  occupations: {value: ["philosopher", "teacher (head of the Lyceum)", "naturalist"], certainty: 1.0, cites: [{source: S1, locator: "§1; opening (empirical biology)"}, {source: S8, locator: "body (founded the Lyceum; detailed study of nature)"}], how_known: "SEP and MacTutor."}

contribution:
  fields: {value: ["logic", "metaphysics", "natural philosophy", "biology", "ethics", "politics", "rhetoric", "poetics"], certainty: 0.7, cites: [{source: S1, locator: "opening; §2"}], how_known: "SEP."}
  lasting_original_contributions:
    - {value: "First systematic formal logic: the syllogistic, with a modal syllogistic and meta-theorems", year: "undated (before 322 BC)", kind: theory, lasting: "Kant: logic 'has not had to go a single step backwards' since Aristotle (quoted in S1 §4.1)", certainty: 0.7, cites: [{source: S1, locator: "§4.1"}], how_known: "SEP; treatise undated."}
    - {value: "Four-cause scheme of explanation and hylomorphism", year: "undated (before 322 BC)", kind: theory, lasting: "SEP: 'surely one of his most significant philosophical contributions'", certainty: 0.7, cites: [{source: S1, locator: "§§7–8"}], how_known: "SEP."}
    - {value: "Detailed empirical plant and animal observation and description (biology)", year: "undated (before 322 BC)", kind: "body of work", lasting: "SEP: he 'excelled at detailed plant and animal observation'", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}
  evidence_of_impact:
    - {value: "His works shaped philosophy from Late Antiquity through the Renaissance; only Plato is his peer in influence", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}
  major_works:
    - {value: "Metaphysics", year: "undated", kind: book, certainty: 0.7, cites: [{source: S1, locator: "§2 (list)"}], how_known: "SEP."}
    - {value: "Physics", year: "undated", kind: book, certainty: 0.7, cites: [{source: S1, locator: "§2 (list)"}], how_known: "SEP."}
    - {value: "Nicomachean Ethics", year: "undated", kind: book, certainty: 0.7, cites: [{source: S1, locator: "§2 (list)"}], how_known: "SEP."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Founded formal logic; lasting influence across philosophy and science.", certainty: 0.7, cites: [{source: S1, locator: "opening; §4.1"}], how_known: "SEP."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "SEP §1 says nothing on it."}
  family_religious_practice: {value: UNKNOWN, how_known: "Same."}
  parents_and_household:
    - {value: "Father named Nicomachus, a physician", name: "Nicomachus", role: father, certainty: 1.0, cites: [{source: S1, locator: "§1 ('Nicomachus, named for Aristotle's father')"}, {source: S8, locator: "opening ('His father was Nicomachus, a medical doctor')"}], how_known: "SEP and MacTutor."}
  household_circumstances: {value: TODO}
  schooling:
    - {value: "Plato's Academy, Athens, from about age seventeen until Plato's death in 347", stage: university, run_by: private, years: "c. 367–347 BC", ages: "c. 17–37", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S8, locator: "body ('In 367 BC Aristotle, at the age of seventeen, became a student at Plato's Academy')"}], how_known: "SEP and MacTutor; 'university' is the nearest stage value, and 'private' the coder's reading of the Academy."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: TODO}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: UNKNOWN, how_known: "Treatises undated; equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation:
    value: "Inherited myth that the heavenly bodies are gods and 'the divine encloses the whole of nature' is kept as 'an inspired utterance'; the anthropomorphic rest was 'added later in mythical form with a view to the persuasion of the multitude'"
    certainty: 0.7
    cites: [{source: S7, locator: "Met. XII ch. 8 (Ross Oxford 1908; Bekker 1074a38–b14 region)"}, {source: S2, locator: "Met. XII (Λ) ch. 8 (Ross part 8, closing paragraph; Bekker 1074a38–b14)"}]
    how_known: "His own text in Ross Oxford 1908 (S7), matching the MIT web copy (S2)."
  primary_system:
    value: ARIST
    basis: written_profession
    certainty: 0.7
    cites: [{source: S6, locator: "Met. XII (Λ) 1072b–1075a"}, {source: S7, locator: "Met. XII chs. 6–10"}, {source: S1, locator: "§§2, 7–9"}]
    how_known: "Founder rule (§1): he founded Aristotelianism. Capped at 0.7: CLASS_THEISM is a named alternative."
    rationale: "Founders are coded with the system they founded. ARIST is a stub system file, which does not block the code (P14)."
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: ARIST, reason: "Founder of the system (founders rule). Chosen."}
    - {code: CLASS_THEISM, reason: "The Aristotelian-Thomistic-Falsafa God (simple, unchanging, reached by reason from motion) starts from his Met. XII; rejected for primary because the founders rule codes the founded system, and his god neither creates nor knows the world."}
    - {code: HELLEN, reason: "He keeps the old belief that the heavenly bodies are gods as 'an inspired utterance' (S2, Λ.8); rejected because he calls the human-shaped gods later myth for persuading the multitude."}
  lio_axes:
    A_locus:
      value: 1
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S6, locator: "Met. XII (Λ) 1072b (Tredennick: 'God is a living being, eternal, most good'); 1073a ('eternal and immovable and separate from sensible things'; impassive and unalterable)"}, {source: S7, locator: "Met. XII ch. 7–8 (Ross Oxford 1908: same Λ.7 lines; 'living being, eternal, most good'; 'eternal and unmovable and separate from sensible things'; 'impassive and unalterable'); ch. 10 (1075a army/leader)"}]
      how_known: "His Metaphysics XII in two independent scholarly editions (Tredennick Loeb via Perseus; Ross Oxford 1908). Named alternative 2 still caps certainty at 0.7 (CODING_GUIDE §3)."
      rationale: "Leans to the interventionist pole with limits. The first mover is 'a living being, eternal, most good' and 'a substance which is eternal and unmovable and separate from sensible things' (Λ.7): a living, thinking god outside the world. The limits: it moves things only 'as being loved' / 'as an object of love', it is 'impassive and unalterable', and its thinking 'is a thinking on thinking' (Λ.7, Λ.9), so it does not act on or attend to the world as a person would. Same pattern and score as Aquinas and Ibn Sina (A 1). Named alternative 2: Λ.10 says the universe holds the good 'both' as 'something separate' and 'as the order of the parts', though 'more in the latter' sense of the leader (Ross 1908 / Tredennick). Independent editions → corroborated (P48)."
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S3, locator: "Phys. II ch. 8 (Hardie and Gaye trans., Bekker 199b24–26)"}, {source: S4, locator: "EN III ch. 5 (Ross trans., Bekker 1113b6–8, 1113b17–19; alternative reading 1114a13–21)"}, {source: S2, locator: "Met. IX (Θ) ch. 2, Bekker 1046b4–7; ch. 5, Bekker 1048a5–11"}]
      how_known: "His Physics II, EN III and Met. Θ in the MIT Ross/Hardie–Gaye web copies (S3, S4, S2); three distinct source ids → corroborated (P48). Named alternative 4 caps certainty at 0.7."
      rationale: "Scored on his account of nature (P6). Nature is regular: 'In natural products the sequence is invariable, if there is no impediment', and what happens 'always or for the most part' is not by chance (Phys. II.8). No miracle, petition or divine exemption appears: the first mover acts only as final cause. Chance in 'always or for the most part' is an incidental cause (Phys. II.5), not an exemption from nature's order. B 3 comes from free will placed in nature (CODING_GUIDE §6 B 3 anchor, P30 #14), not from an exception to lawful cause: 'virtue also is in our own power, and so too vice. For where it is in our power to act it is also in our power not to act' (EN III.5, 1113b6–8), with the agent as the 'originator and begetter' of his actions (1113b17–19); rational powers, unlike natural ones, are 'of contraries' (Met. Θ.2 1046b4–7; Θ.5 1048a5–11). On his own framing this is a different kind of principle from nature, not a suspension of it. Named alternative 4: on a compatibilist reading (EN III.5, 1114a13–21: character, once formed, makes action necessary in its turn), the impediment clause is the only qualifier and nothing is exempt. Framing corrected after the fallacy_catalog audit of 3f4817e."
    C_ledger:
      value: 4
      basis: written_profession
      certainty: 0.5
      support: corroborated
      cites: [{source: S10, locator: "EN I.7–9 (happiness as virtuous activity; not primarily god-sent)"}, {source: S9, locator: "EN X.6–8 (happiness as contemplative activity; gods' life is contemplation)"}]
      how_known: "Own Nicomachean Ethics I (S10) and X (S9, Ross MIT). Independent book-ids → corroborated (P48). Certainty 0.5: named alternative 1 (CODING_GUIDE §3)."
      rationale: "At the LIO pole: reward and punishment of persons is not the ledger. Happiness is an activity of soul in accordance with perfect virtue and, at its peak, contemplation (EN I; EN X.7–8) — a consequence of the agent's activity and character, not a personal divine judgment. EN I.9 treats happiness as coming by virtue/learning rather than primarily as a gift of the gods. Named alternative 1: EN X.8's conditional 'if the gods have any care for human affairs… they should reward those who love and honour this most' (the philosopher 'dearest to the gods') can be read as a personal divine ledger; kept as alt, not the value (same pattern as ARIST system C 4 @0.5)."
      alternatives:
        - {value: 1, note: "EN X.8 gods-reward the philosopher (conditional care).", cites: [{source: S9, locator: "EN X.8"}]}
    D_authority:
      value: 4
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S2, locator: "Met. XII (tradition in myth; anthropomorphic additions for persuasion of the multitude)"}, {source: S6, locator: "Met. XII ch. 8 (Tredennick; same tradition/myth passage)"}, {source: S7, locator: "Met. XII (Ross Oxford; same)"}]
      how_known: "Own Metaphysics XII in three independent scholarly editions (MIT Ross S2; Tredennick S6; Ross Oxford S7). Written profession. Certainty 0.7 for named alternative 3."
      rationale: "At the LIO pole: observation and reason outrank revelation. Forefathers handed down 'in the form of a myth' that the heavenly bodies are gods and 'the divine encloses the whole of nature'; 'the rest of the tradition has been added later in mythical form with a view to the persuasion of the multitude and to its legal and utilitarian expediency' (anthropomorphic gods) — and that rest is to be stripped away, keeping only the first point (Met. XII). Philosophy seeks causes and first principles (Met. I); no revealed corpus outranks demonstration. Named alternative 3: traditional cult kept for civic/legal expediency as a limited domain of its own would lean D 3 (two domains)."
      alternatives:
        - {value: 3, note: "If civic cult/tradition is read as a domain with its own authority alongside philosophy.", cites: [{source: S2, locator: "Met. XII (legal and utilitarian expediency)"}]}
    E_scope:
      value: 4
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S3, locator: "Phys. II.8 (natural products invariable if no impediment; always or for the most part)"}, {source: S2, locator: "Met. XII (divine encloses the whole of nature)"}, {source: S6, locator: "Met. XII ch. 8 (Tredennick; same)"}]
      how_known: "Own Physics II (S3) and Metaphysics XII (S2/S6). Written profession. Certainty 0.7 for named alternative 3. Scored on the world's order (P7), not from working science alone (P19)."
      rationale: "Scored on the world's order (decision P7). At the LIO pole: same rules for the kinds of being in nature. 'In natural products the sequence is invariable, if there is no impediment' and what happens 'always or for the most part' is not by chance (Phys. II.8) — a general account of natural regularity, not an in-group exemption. Met. XII keeps the inherited point that 'the divine encloses the whole of nature' while rejecting anthropomorphic favour-myths. Named alternative 3: if EN X.8's gods-care/reward for philosophers is read as this-world favour for an in-group; under P7 that reward language is scored on C (see C_ledger alt 1), not here."
      alternatives:
        - {value: 3, note: "EN X.8 gods-care/reward read as this-world in-group favour (P7: prefer C; S9). No exclusive alt cite — disagreement is a reading rule, not a second primary contesting Phys II / Met Λ.", cites: []}
  mid_basin:
    value: true
    certainty: 0.7
    cites: [{source: S2, locator: "Met. XII (Λ) ch. 7"}, {source: S3, locator: "Phys. II ch. 8"}, {source: S4, locator: "EN III ch. 5"}]
    how_known: "P4/P6: A_locus 1 (0.7) and B_cause 3 (0.7) meet A ≤ 1 and B ≥ 3 at ≥ 0.7. B's alternative 4 is on the same side; A's alternative 2 is not, so the cap is A's 0.7 (P10, P30)."
  statements:
    - text: "It is clear then from what has been said that there is a substance which is eternal and unmovable and separate from sensible things."
      cites: [{source: S7, locator: "Met. XII ch. 7 closing / 1073a (Ross Oxford 1908)"}, {source: S6, locator: "Met. XII 1073a (Tredennick: 'eternal and immovable and separate from sensible things')"}, {source: S2, locator: "Met. XII (Λ) ch. 7, Ross part 7, last paragraph (Bekker 1073a3–5)"}]
      date: "-322"
      context: "Conclusion of the argument for the first unmoved mover. Date is death-cap terminus; treatise undated."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-23
      note: "Verified against Ross Oxford Works VIII Metaphysica (1908) OCR and Tredennick Loeb on Perseus; MIT web copy (S2) matches Ross 1908 wording."
    - text: "We say therefore that God is a living being, eternal, most good, so that life and duration continuous and eternal belong to God; for this is God."
      cites: [{source: S7, locator: "Met. XII ch. 7 (Ross Oxford 1908, 1072b28–30)"}, {source: S6, locator: "Met. XII 1072b (Tredennick: 'God is a living being, eternal, most good')"}, {source: S2, locator: "Met. XII (Λ) ch. 7, Ross part 7 (Bekker 1072b28–30)"}]
      date: "-322"
      context: "Same chapter: the first mover's life is thought. Date death-cap terminus."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-23
      note: "Ross 1908 and Tredennick Loeb both carry the line; MIT (S2) matches Ross 1908."
    - text: "In natural products the sequence is invariable, if there is no impediment."
      cites: [{source: S3, locator: "Phys. II ch. 8 (Hardie and Gaye; Bekker 199b25–26)"}]
      date: "-322"
      context: "Argument that nature acts for an end; what happens always or for the most part is not by chance."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "Hardie and Gaye translation on the MIT Internet Classics Archive; Bekker numbers verified."
    - text: "Therefore virtue also is in our own power, and so too vice. For where it is in our power to act it is also in our power not to act, and vice versa"
      cites: [{source: S4, locator: "EN III ch. 5 (Ross; Bekker 1113b6–8)"}]
      date: "-322"
      context: "Voluntary action and responsibility."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "Ross translation on the MIT Internet Classics Archive; Bekker numbers verified."
    - text: "originator and begetter"
      cites: [{source: S4, locator: "EN III ch. 5 (Ross; Bekker 1113b17–19)"}]
      date: "-322"
      context: "The agent as origin of his own actions: free will placed in nature (B 3 anchor), not an exception to it."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "Phrase quoted in the fallacy_catalog audit of 3f4817e at this locator (Ross translation)."
  changes_over_life: []
  coder_notes: "Deepen D1: A now rests on Tredennick Loeb (Perseus) and Ross Oxford 1908 (archive.org OCR) — two scholarly editions — so support corroborated; certainty stays 0.7 for the named alt 2 (Λ.10 army/leader). B stays 3 @ 0.7 with support corroborated (S3+S4+S2); Physics/EN still MIT unofficial copies. MIT Ross Met. XII wording matches Ross 1908. Basis written_profession: SEP §2 lecture-notes character noted; still written for auditors. C, D, E left TODO. No fallacy_catalog (Jason 2026-10-23)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Greek, from the Macedonian region", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S8, locator: "opening (Stagirus, Macedonia)"}], how_known: "SEP and MacTutor."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not in SEP."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not in SEP."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not in SEP."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: UNKNOWN, how_known: "Treatises undated (S1 §2); the period ends by 322 BC (P30)."}
  age_at_first_lasting_contribution: {value: UNKNOWN, how_known: "First-lasting year unknown."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "The B 3 statements are undated (S3, S4), so no year can be given."}
  lio_views_relative_to_major_work: {value: "unclear", rationale: "The statements are in the major works themselves, which are undated.", certainty: 0.5, cites: [{source: S1, locator: "§2"}], how_known: "Undated texts."}
  worldview_during_major_work: {value: "Aristotelian: a separate, living unmoved mover as final cause of a regular nature", certainty: 0.7, cites: [{source: S2, locator: "Met. XII chs. 7–10"}], how_known: "His text (web copy cap)."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "Science is demonstration from necessary first principles (Posterior Analytics).", certainty: 0.7, cites: [{source: S1, locator: "§4.2"}], how_known: "SEP."}
  form_acquired: {value: "adulthood, before major work", certainty: 0.5, cites: [{source: S1, locator: "§1 (Academy from about seventeen)"}], how_known: "Coder's reading: twenty years at Plato's Academy."}
  circle_present: {value: "partly", rationale: "The good is in the order of the parts as well as in the separate mover (Λ.10), but God stays separate.", certainty: 0.5, cites: [{source: S2, locator: "Met. XII ch. 10"}], how_known: "Coder's reading."}
  reading: "As belief, not finding: form present, circle partly present."
  notes: ""

institutions:
  - {value: "Lyceum, Athens", role: "founder and head", years: "335–323 BC", kind: "other", certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S8, locator: "body ('In 335 BC Aristotle founded his own school the Lyceum')"}], how_known: "SEP and MacTutor."}
collaborators:
  - {value: "Plato", relation: teacher, certainty: 1.0, cites: [{source: S1, locator: "§1"}, {source: S8, locator: "body (Academy under Plato)"}], how_known: "SEP and MacTutor."}
  - {value: "Theophrastus", relation: collaborator, certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP; MacTutor does not stress the Lesbos collaboration in the same terms."}
  - {value: "Alexander the Great", relation: "student or assistant", note: "SEP: tutored from about age 13 to 15; MacTutor reports Jaeger/Grayeff doubt the tutor story", certainty: 0.5, cites: [{source: S1, locator: "§1"}, {source: S8, locator: "body (Jaeger; often-quoted tutor story 'almost certainly a later invention')"}], how_known: "Sources disagree on whether and how long he tutored Alexander."}

review:
  roster_status_reason: {value: "Core in v8 (F 5: Claude, DeepSeek, Gemini, GPT, Grok).", certainty: 0.7, cites: [{source: S5, locator: "roster.csv, rank 9"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Britannica blocked (Cloudflare); basics dual-sourced SEP + MacTutor (2026-10-23)."
    - "B statements still rest on MIT unofficial web copies of Physics/EN (S3, S4); A now on scholarly editions."
  open_questions:
    - "Optional: check B quotations against Barnes 1984 / Oxford Physics Hardie–Gaye print."
    - "Score C, D and E (providence, afterlife of nous in De Anima III.5, status of myth)."
    - "Scholarly reading of 'up to us' (Meyer, Bobzien) to settle B 3 vs the alternative 4."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Christopher Shields"
    year: 2020
    citation: "Shields, Christopher. \"Aristotle.\" Stanford Encyclopedia of Philosophy, first published 25 September 2008, substantive revision 25 August 2020. https://plato.stanford.edu/entries/aristotle/."
    url: "https://plato.stanford.edu/entries/aristotle/"
    accessed: 2026-10-23
    reliability_note: "Peer-reviewed reference article."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Aristotle"
    citation: "Aristotle. Metaphysics, Book XII. Translated by W. D. Ross. Internet Classics Archive (MIT). https://classics.mit.edu/Aristotle/metaphysics.12.xii.html."
    url: "https://classics.mit.edu/Aristotle/metaphysics.12.xii.html"
    accessed: 2026-10-23
    reliability_note: "Unofficial web copy of Ross's Oxford translation; no Bekker numbers. Wording checked against Ross Oxford 1908 (S7) in deepen D1."
    source_quality: "unofficial web copy"
    used_for: [worldview, timing, lane_b]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "Aristotle"
    citation: "Aristotle. Physics, Book II. Translated by R. P. Hardie and R. K. Gaye. Internet Classics Archive (MIT). https://classics.mit.edu/Aristotle/physics.2.ii.html."
    url: "https://classics.mit.edu/Aristotle/physics.2.ii.html"
    accessed: 2026-10-23
    reliability_note: "Unofficial web copy of the Oxford translation. Still the B carrier; not re-checked against print in this deepen."
    source_quality: "unofficial web copy"
    used_for: [worldview]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "Aristotle"
    citation: "Aristotle. Nicomachean Ethics, Book III. Translated by W. D. Ross. Internet Classics Archive (MIT). https://classics.mit.edu/Aristotle/nicomachaen.3.iii.html."
    url: "https://classics.mit.edu/Aristotle/nicomachaen.3.iii.html"
    accessed: 2026-10-23
    reliability_note: "Unofficial web copy of Ross's translation."
    source_quality: "unofficial web copy"
    used_for: [worldview]
  - id: S5
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-23
    reliability_note: "Study's own roster; used only for rank, F and status."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "Aristotle"
    year: 1933
    citation: "Aristotle. Metaphysics, Book XII (Lambda). Translated by Hugh Tredennick. Aristotle in 23 Volumes, Vols. 17–18. Cambridge, MA: Harvard University Press; London: William Heinemann, 1933, 1989. Read on Perseus Digital Library: https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0052:book=12."
    url: "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0052%3Abook%3D12%3Asection%3D1072b"
    accessed: 2026-10-23
    reliability_note: "Loeb Classical Library scholarly edition (Tredennick), via Perseus. Independent English of the A_locus passages."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview]
  - id: S7
    type: primary
    kind: "published work by the subject"
    author: "Aristotle"
    year: 1908
    citation: "Aristotle. Metaphysica. Translated by W. D. Ross. The Works of Aristotle Translated into English, vol. VIII. Oxford: Clarendon Press, 1908. Archive.org scan/OCR: https://archive.org/details/worksofaristotle0008unse."
    url: "https://archive.org/details/worksofaristotle0008unse"
    accessed: 2026-10-23
    reliability_note: "Oxford scholarly translation (Ross). OCR of the 1908 printing used to verify MIT web-copy wording for Λ.7 and Λ.10."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview]
  - id: S8
    type: secondary
    kind: encyclopedia
    author: "J. J. O'Connor and E. F. Robertson"
    year: 1999
    citation: "O'Connor, J. J., and E. F. Robertson. \"Aristotle.\" MacTutor History of Mathematics Archive, University of St Andrews. https://mathshistory.st-andrews.ac.uk/Biographies/Aristotle/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Aristotle/"
    accessed: 2026-10-23
    reliability_note: "Signed reference biography; used for basics dual-source (Britannica blocked)."
    source_quality: "reference entry"
    used_for: [identity, basics, childhood, heritage, institutions, collaborators]
  - id: S9
    type: primary
    kind: "published work by the subject"
    author: "Aristotle"
    citation: "Aristotle. Nicomachean Ethics, Book X. Translated by W. D. Ross. Internet Classics Archive (MIT)."
    url: "https://classics.mit.edu/Aristotle/nicomachaen.10.x.html"
    accessed: 2026-10-25
    source_quality: "unofficial web copy"
    reliability_note: "Ross MIT web copy of EN X; used for C (contemplation / gods-reward alt) and cross-check E."
    used_for: [worldview]
  - id: S10
    type: primary
    kind: "published work by the subject"
    author: "Aristotle"
    citation: "Aristotle. Nicomachean Ethics, Book I. Translated by W. D. Ross. Internet Classics Archive (MIT)."
    url: "https://classics.mit.edu/Aristotle/nicomachaen.1.i.html"
    accessed: 2026-10-25
    source_quality: "unofficial web copy"
    reliability_note: "Ross MIT web copy of EN I; used for C (eudaimonia as virtuous activity)."
    used_for: [worldview]
---

# Aristotle

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Aristotle (384–322 BC), student of Plato and founder of the Lyceum, created the first formal logic and the four-cause scheme of explanation and did extensive empirical biology [S1; S8]. In Metaphysics XII he argues for 'a substance which is eternal and unmovable and separate from sensible things', 'a living being, eternal, most good' [S6; S7; S2, Λ.7]. Deepen D1 (P47–P50): A 1 @ 0.7, written_profession, support single → corroborated (S6 Tredennick Loeb + S7 Ross Oxford 1908); B 3 @ 0.7, support corroborated (S3+S4+S2); mid_basin true (0.7). Chart: dark hollow → dark filled.

## Life and work

Born at Stagira; at Plato's Academy from about seventeen until 347; Assos and Lesbos; association with Alexander disputed in degree; the Lyceum in Athens from 335; died at Chalcis in 322 [S1; S8].

## Contribution and impact

Syllogistic logic, four causes, hylomorphism, biology [S1].

## Childhood and education

Father Nicomachus; the Academy [S1].

## Adult working worldview

A separate first mover that moves as an object of love — verified in Tredennick Loeb and Ross Oxford 1908 [S6; S7; S2, Λ.7]; nature regular 'if there is no impediment' [S3, II.8]; human choice 'in our own power', free will placed in nature [S4, III.5].

## Heritage (context only)

Greek, Macedonian region [S1; S8].

## Timing

Treatises undated.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form present; circle partly [S1; S2].

## Open questions

- Optional Barnes 1984 check for B; score C, D, E.

## Research log

- 2026-10-15: Read SEP (Shields 2020) and the MIT Internet Classics Archive texts of Met. XII, Phys. II and EN III. Britannica blocked.
- 2026-10-23: Deepen D1 (queue #9). Tredennick Loeb Met. XII on Perseus (S6); Ross Oxford 1908 Metaphysica OCR (S7); MacTutor (S8). A support single → corroborated; chart fill hollow → filled. P47 labels. No fallacy_catalog (Jason 2026-10-23).
