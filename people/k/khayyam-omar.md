---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 4
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch J)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to medieval. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-25, by: "Grok Bot", summary: "Perpetual deepen: religious_heritage_by_birth TODO→Muslim (Seljuq Nishapur) @0.7 from SEP S4 + MacTutor S5; baptism/catechism UNKNOWN; family_religion filled at 0.5. Context only. Chart-moving NO. No figures/; no fallacy_catalog."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch J, order P32: F 5, rank 63). Basics from Britannica (Britannica Editors, unsigned). Scientist under P30 (algebra, astronomy). The quatrains are not scored: Britannica says some scholars doubt he wrote poetry and that the verses appeared under his name only two centuries after his death (P42). primary_system UNKNOWN; A UNKNOWN; B 3 at 0.5 (alt 4) from working science only (P35); C, D, E UNKNOWN; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Audit fixes (fallacy_catalog audit of 81b9098, run 1). mid_basin BELOW_THRESHOLD -> UNKNOWN (P19). Note added: a single quatrain needs a specific scholarly attribution; his treatise on existence is the lead for A."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #62, F5 rank 63). Needs: A UNKNOWN; B single source; B faded; 1 source. Primaries: Aminrazavi Wine of Wisdom 2007 Appendix A English of six philosophical treatises (new S3) — Principles of Existence (Necessary Being = God Most High), On Existence §20 (Necessary Being essence), Necessity of Contradiction (causal series to Necessary Being; evil accidental). SEP Mousavian et al. 2023 (new S4) corroborates Avicennan Necessary Existent / treatises as his. MacTutor (new S5) bio/math. Quatrains still unscored (P42). A UNKNOWN→1@0.7 written_profession support corroborated (alt BELOW if poetry corpus counted); B 3@0.5 single→3@0.7 written_profession support corroborated (alt 4); primary_system CLASS_THEISM@0.7 (ISLAM nominal); mid_basin true@0.7. P47 on S1–S5. Chart-moving YES (newly dark filled). No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: khayyam-omar
  display_name: "Omar Khayyam"
  roster:
    canonical_name: "Omar Khayyam"
    rank: 63
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: mathematics
    field_bucket: mathematics
  full_name: {value: "Ghiyāth al-Dīn Abū al-Fatḥ ʿUmar ibn Ibrāhīm al-Nīsābūrī al-Khayyāmī", certainty: 0.7, cites: [{source: S5, locator: "opening (full name)"}, {source: S1, locator: "header ('Also known as')"}], how_known: "MacTutor full form; Britannica 'Also known as' agrees in substance."}
  native_name: {value: UNKNOWN, how_known: "Persian script not in the sources read."}
  aliases:
    - {name: "Omar Khayyám", kind: transliteration}
    - {name: "Umar Khayyam", kind: transliteration}

basics:
  birth:
    date: {value: "1048-05-18", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "Quick Info"}], how_known: "Britannica and MacTutor; Julian-era date."}
    place: {value: "Neyshābūr, Khorāsān", modern_name: "Nishapur, Iran", polity_then: "Khorasan (Seljuq period)", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "Quick Info"}], how_known: "Britannica and MacTutor."}
  death:
    date: {value: "1131-12-04", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "Quick Info"}], how_known: "Britannica and MacTutor."}
    place: {value: "Neyshābūr", modern_name: "Nishapur, Iran", polity_then: "Khorasan", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "Quick Info"}], how_known: "Britannica and MacTutor."}
  first_lasting_contribution_year: {value: 1070, certainty: 0.5, cites: [{source: S5, locator: "Samarkand / Algebra paragraphs"}, {source: S1, locator: "calendar paragraph"}], how_known: "MacTutor: Algebra treatise written at Samarkand after move in 1070, before age 25 he had already written earlier works; Jalālī calendar adopted 1075 (S1). Earliest lasting public math work dated around the Samarkand Algebra (P13); 0.5."}
  era_bucket: {value: "500 to 1399", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "Quick Info"}], how_known: "Whole life in the bucket (P2)."}
  region_of_birth: {value: "Middle East and North Africa", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Iran is Middle East and North Africa in regions.csv (P3)."}
  region_of_work: {value: "Middle East and North Africa", certainty: 0.5, cites: [{source: S1, locator: "text"}, {source: S5, locator: "Samarkand; Esfahan paragraphs"}], how_known: "Neyshābūr and Eṣfahān (Iran); also Samarkand (Central Asia); 0.5."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [Arabic, Persian], certainty: 0.7, cites: [{source: S4, locator: "§2 (treatise titles; Principles of Existence in Persian)"}, {source: S3, locator: "Appendix A treatise list"}], how_known: "Philosophical and mathematical treatises in Arabic; Principles of Existence (Risālah dar ʿilm kulliyāt-i wujūd) in Persian (S4/S3). Quatrains disputed (P42) and not used for language score."}
  occupations: {value: ["mathematician", "astronomer", "philosopher"], certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "§2"}, {source: S5, locator: "Summary"}], how_known: "Britannica mathematician/astronomer; SEP and MacTutor add philosophical treatises and poet label (poetry unscored, P42)."}

contribution:
  era_bucket: medieval
  fields: {value: ["algebra", "geometry", "astronomy", "philosophy"], certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S4, locator: "§2; §4"}, {source: S5, locator: "Summary"}], how_known: "Britannica math/astronomy; SEP and MacTutor philosophy and cubic geometry."}
  lasting_original_contributions:
    - {value: "Treatise on Demonstration of Problems of Algebra (cubic equations by intersecting conics)", year: 1070, kind: work, lasting: "his mathematical reputation 'principally rests' on it (S1); geometric solution of cubics (S5)", certainty: 0.5, cites: [{source: S1, locator: "Samarkand paragraph"}, {source: S5, locator: "Algebra paragraphs"}], how_known: "MacTutor places composition at Samarkand after 1070; undated in Britannica (P39/P13); 0.5."}
    - {value: "Jalālī calendar", year: 1075, kind: discovery, lasting: "'more accurate than the present Gregorian calendar' (S1)", certainty: 0.7, cites: [{source: S1, locator: "calendar paragraph"}, {source: S5, locator: "calendar / Malik-Shah paragraphs"}], how_known: "Adopted 1075 (S1); MacTutor concurs on calendar reform under Malik-Shah."}
    - {value: "Commentary on Difficulties in the Postulates of Euclid's Elements (parallels)", kind: work, lasting: "Critique of Euclid's parallels influenced John Wallis (S1)", certainty: 0.5, cites: [{source: S1, locator: "Eṣfahān paragraph"}, {source: S4, locator: "§4 (Euclid commentary)"}], how_known: "Undated (P39); lasting via later reception (S1)."}
  evidence_of_impact:
    - {value: "Critique of Euclid's parallels influenced John Wallis", kind: "assessment by a later major figure", certainty: 0.7, cites: [{source: S1, locator: "Eṣfahān paragraph"}], how_known: "Britannica."}
    - {value: "Geometric theory of cubic equations via intersecting conics, foundational in medieval Islamic algebra", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S5, locator: "Algebra / cubic paragraphs"}, {source: S4, locator: "§4.1"}], how_known: "MacTutor and SEP."}
  major_works:
    - {value: "Treatise on Demonstration of Problems of Algebra", year: 1070, kind: other, certainty: 0.5, cites: [{source: S5, locator: "Algebra paragraphs"}, {source: S1, locator: "Samarkand paragraph"}], how_known: "Samarkand composition ~1070 (S5); 0.5."}
    - {value: "On the Knowledge of the Universal Principles of Existence (Risālah dar ʿilm kulliyāt-i wujūd)", kind: other, certainty: 0.7, cites: [{source: S3, locator: "Appendix A, item 4; pp. 309ff"}, {source: S4, locator: "§2 (Principles of Existence)"}], how_known: "English in Aminrazavi Appendix A; listed among his philosophical treatises (S4)."}
    - {value: "On Existence (Risālah fi’l-wujūd)", kind: other, certainty: 0.7, cites: [{source: S3, locator: "Appendix A, item 5; pp. 317ff"}, {source: S4, locator: "§2 (On Existence)"}], how_known: "English in Aminrazavi Appendix A; SEP §2.1."}
    - {value: "The Necessity of Contradiction in the World, Determinism and Subsistence", kind: other, certainty: 0.7, cites: [{source: S3, locator: "Appendix A, item 2; pp. 292ff"}, {source: S4, locator: "§2 (The Necessity of Contrariety)"}], how_known: "English in Aminrazavi Appendix A; SEP §2.4–2.5."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1; S5).", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "Summary"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Muslim (inferred from birth milieu)", certainty: 0.5, cites: [{source: S4, locator: "§1"}, {source: S5, locator: "opening"}], how_known: "Same as religious_heritage_by_birth; parents not named as clerics."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father possibly a tentmaker (source of the name Khayyam / al-Khayyāmī)", role: father, certainty: 0.5, cites: [{source: S1, locator: "name paragraph"}, {source: S5, locator: "name paragraph"}], how_known: "Britannica 'may have been derived'; MacTutor: literal 'tent maker' may have been Ibrahim's trade."}
  household_circumstances: {value: TODO}
  schooling:
    - {value: "Education in the sciences and philosophy in Neyshābūr", stage: other, run_by: other, certainty: 0.7, cites: [{source: S1, locator: "name paragraph"}, {source: S5, locator: "philosophy at Naishapur"}], how_known: "Britannica and MacTutor."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: TODO}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1070–1075", certainty: 0.5, cites: [{source: S5, locator: "Algebra; calendar paragraphs"}, {source: S1, locator: "calendar paragraph"}], how_known: "Equals timing.major_work_period (Algebra ~1070 to Jalālī calendar 1075); philosophical treatises undated (P39)."}
  nominal_affiliations:
    - {value: "Islam (Muslim under Seljuq rule; treatises praise God and the Prophet)", certainty: 0.7, cites: [{source: S3, locator: "Appendix A openings; epilogue pp. 280–281"}, {source: S4, locator: "§2; §2.3"}], how_known: "Philosophical treatises written in Islamic Peripatetic idiom and invoke God and Muḥammad (S3/S4); Aminrazavi: life-long adherence to sharīʿah (S3 epilogue). Working metaphysics coded CLASS_THEISM, not ISLAM (falsafa rule)."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No direct self-description of the science–religion relation read; Algebra preface complains of obstacles to learning, not of religion vs science (S5)."}
  primary_system:
    value: CLASS_THEISM
    basis: written_profession
    certainty: 0.7
    cites: [{source: S3, locator: "Principles of Existence p. 309; On Existence §20 p. 317; Necessity of Contradiction pp. 292, 297"}, {source: S4, locator: "§2.1"}]
    how_known: "Own philosophical treatises in Aminrazavi's English (S3) plus SEP (S4): God as Necessary Being / Necessary Existent, simple and one, cause of contingent existents by a causal series that cannot go to infinity — Avicennan falsafa. Certainty 0.7: named alternative ISLAM as confessed religion; poetry/philosophy tension noted but quatrains unscored (P42)."
    rationale: "CODING_GUIDE CLASS_THEISM = Aristotelian-Thomistic-Falsafa God: simple, immutable, known through reason. Khayyam: 'existence is of two types, one is the Necessary Being and that is God Most High and the other is a contingent being' (S3, p. 309); Necessary Being's essence 'not possible to be conceived of except as an existent' and unity in all aspects (S3, p. 317); SEP: he 'completely follows Avicenna's view on God's existence and His attributes' (S4, §2.1). ISLAM system guidance sends falsafa to CLASS_THEISM. Quatrains barred (P42)."
  secondary_system: {value: UNKNOWN, how_known: "None coded."}
  candidate_codes_considered:
    - {code: CLASS_THEISM, reason: "Chosen. Necessary Being = God; Avicennan attributes, causality, emanationist hierarchy; SEP places him in Avicennan tradition (S4, §2.1).", cites: [{source: S3, locator: "pp. 309, 317, 292"}, {source: S4, locator: "§2.1"}]}
    - {code: ISLAM, reason: "Rejected as primary. Nominal Muslim affiliation and treatise piety are real (S3 epilogue; S4 §2.3), but working metaphysics is falsafa Necessary Existent — ISLAM do_not_use_when sends that to CLASS_THEISM.", cites: [{source: S3, locator: "epilogue pp. 280–281"}, {source: S4, locator: "§2.3"}]}
    - {code: AGNOS, reason: "Rejected. Aminrazavi notes the Rubāʿiyyāt can read as agnostic (S3, p. 280), but those verses are unscored under P42 without specific attribution; the philosophical treatises affirm God as Necessary Being.", cites: [{source: S3, locator: "epilogue p. 280"}, {source: S1, locator: "poetry attribution doubt"}]}
  lio_axes:
    A_locus:
      value: 1
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S3, locator: "Principles of Existence (6), p. 309; On Existence §20, p. 317"}, {source: S4, locator: "§2.1 (On Existence; Principles of Existence)"}]
      how_known: "Own treatises in Aminrazavi English (S3) plus SEP independent account with matching Necessary Existent quotations (S4). Independent agreeing sources → corroborated (P48). Written profession; certainty 0.7 because the record names BELOW_THRESHOLD as alternative if the disputed poetry corpus were taken as the adult worldview (P42 bars that scoring; CODING_GUIDE §3 contested-reading cap)."
      rationale: "Leans to the transcendent pole. God is the Necessary Being / Necessary Existent, whose essence cannot be conceived except as existent, one in all aspects, neither substance nor accident in the ordinary sense, cause of all contingent existents (S3, pp. 309, 317; S4, §2.1). That is the Avicennan transcendent source, less personal than the 0 pole, so 1 — same score as CLASS_THEISM / Ibn Sina. Named alternative BELOW_THRESHOLD: if authentic Rubāʿiyyāt skepticism about providence were scored as his adult locus (Aminrazavi notes philosophy vs poetry tension, S3 p. 280; Britannica attribution doubt, S1), A would fall below 0.5; P42 keeps those verses out."
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S3, locator: "Necessity of Contradiction pp. 292, 297; Principles of Existence p. 309"}, {source: S4, locator: "§2.1 (causality; chain of causes); §2.4–2.5"}, {source: S5, locator: "Algebra; calendar; Euclid paragraphs"}]
      how_known: "Own theodicy/causality treatises in Aminrazavi (S3) plus SEP (S4) on causal series and Avicennan order; working mathematical astronomy and algebra (S5/S1) agree on a regular natural order. Independent agreeing sources → corroborated (P48). Written profession; certainty capped at 0.7 for named alternative 4 (CODING_GUIDE §3)."
      rationale: "Leans to law. Scored on his account of nature (P6): a contingent being must have a cause and 'this causal series comes to an end with the Necessary Being' (S3, p. 292); contingent essences are made necessary by the Necessary Being and evil is accidental not essential (S3, p. 297); existence divides into Necessary Being (God) and contingent beings (S3, p. 309). SEP: he discusses causality and the impossibility of an infinite chain of causes and effects (S4, §2.1). Working science (cubics, calendar, Euclid) fits that order (S5). So 3. Named alternative 4: no stated miracle-exception in the nature account comparable to Ibn Sina's prophet clause; if the causal order is read as exceptionless, B would be 4 (P16/P35-style)."
    C_ledger: {value: UNKNOWN, how_known: "Eschatology: SEP says philosophical treatises affirm life after death in line with Islamic doctrine, while poetry plays with doubt (S4, §2.3); poetry unscored (P42). No clear desert/consequence score from the treatises read this pass."}
    D_authority: {value: UNKNOWN, how_known: "Treatises use demonstration and Avicennan reason; also invoke prophetic law and prayer (S3 Being/Necessity closing; S4). Not enough this pass to place 2 vs 3."}
    E_scope: {value: UNKNOWN, how_known: "Not scored (P7); no clear in-group exception statement read beyond general prophetic/legal remarks."}
  mid_basin:
    value: true
    certainty: 0.7
    cites: [{source: S3, locator: "pp. 309, 317, 292, 297"}, {source: S4, locator: "§2.1"}]
    how_known: "P4 test: A_locus = 1 (≤ 1) at 0.7 and B_cause = 3 (≥ 3) at 0.7, B scored on his account of nature (philosophy + mathematical astronomy). Both ≥ 0.7 → true. Certainty 0.7: no surer than the less certain of A and B (CODING_GUIDE §3); named B alternative 4 also satisfies B ≥ 3. F = 5."
  statements:
    - text: "Know that existence is of two types, one is the Necessary Being and that is God Most High and the other is a contingent being."
      cites: [{source: S3, locator: "Appendix A, Principles of Existence (6), p. 309"}]
      context: "On the Knowledge of the Universal Principles of Existence (Persian treatise). Division of existence into Necessary Being (= God) and contingent being; follows discussion that all contingent paths lead to God."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "English translation by Mehdi Aminrazavi (Wine of Wisdom, 2007 Appendix A) from the Persian/Arabic tradition; page from printed page markers in the IA PDF OCR. Primary Arabic/Persian edition not collated this pass."
    - text: "The Necessary Being, may glory be upon Him, is He whose essence is not possible to be conceived of except as an existent. So, the attribute of existence present in the intellect is intrinsic to its intellectual essence and not because one has placed it there. If the attribute of existence is a notion that is added to its essence, indeed in the essence of the Necessary Being, there will be multiplicity. While it has been argued before that the Necessary Being is a unity in all its aspects and in no way can multiplicity enter into it unless multiplicity is [in its] abstract sense in which case it is numerically infinite."
      cites: [{source: S3, locator: "Appendix A, On Existence §20, p. 317"}]
      context: "On Existence, section 'On the Essence of the Necessary Being and His attributes'. Ontological characterization of God as Necessary Being, simple and one."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Aminrazavi English; brackets in source. SEP §2.1 quotes a closely parallel Necessary Existent formulation from On Existence (Jamshīd Nijād Awwal ed.)."
    - text: "The necessity of contradiction [implies that] a contingent being must have a cause and this causal series comes to an end with the Necessary Being. If the contingent being exists necessarily, [then it must] exist in its essence, then there comes a multiplicity in the essence of the Necessary Beings, but it is argued that the Necessary Being is One in all respects."
      cites: [{source: S3, locator: "Appendix A, Necessity of Contradiction, p. 292"}]
      context: "Opening of The Necessity of Contradiction in the World, Determinism and Subsistence — reply on whether contradiction/evil implicates the Necessary Being as cause."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Aminrazavi English; brackets in source. SEP §2.4 frames the same treatise's theodicy question from Qāḍī Abū Naṣr."
    - text: "Evil therefore cannot be attributed in any way to the creator of blackness, for the primary purpose of the Eternal Being was the creation of the primary and good, but this particular form of species of good cannot possibly be devoid of evil and non-existence. [...] It follows from all this that evil cannot be attributed to Him except by way of accident. [...] If that is the case, then it is shown that evil exists in the accidents and not essences of God's creatures, and that evil according to the primary wisdom of creation was very little which qualitatively or quantitatively is not comparable to the good [present in creation]."
      cites: [{source: S3, locator: "Appendix A, Necessity of Contradiction, p. 297"}]
      context: "Same treatise: theodicy — Necessary Being creates contingent essences (good); opposition/evil is accidental."
      axes: [B_cause, A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Aminrazavi English; '[...]' marks omitted middle sentences on the same page; final brackets in source."
  changes_over_life: []
  coder_notes: "Deepen D1 2026-10-24 (queue #62): P42 still bars the Rubāʿiyyāt as a body (Britannica S1 attribution doubt; Aminrazavi S3 epilogue notes philosophy vs poetry tension and that most of ~1200 quatrains are inauthentic). A and primary_system rest on the philosophical treatises SEP lists as his (S4 §2) in Aminrazavi's first complete English (S3 Appendix A). Thin prior source count (queue: 1 source) — do not raise A/B to 1.0 without Arabic/Persian critical-edition page-check. C/D/E left UNKNOWN. No fallacy_catalog (Jason)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Persian", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "opening"}], how_known: "Britannica and MacTutor."}
  religious_heritage_by_birth: {value: "Muslim (Seljuq Nishapur / Islamic intellectual milieu)", certainty: 0.7, cites: [{source: S4, locator: "§1 Formative Period; Islamic intellectual tradition"}, {source: S5, locator: "opening (Islamic scholar); Seljuq orthodox Muslim state"}], how_known: "SEP places him in the Islamic intellectual tradition of Nishapur; MacTutor calls him an Islamic scholar raised in the Seljuq attempt at an orthodox Muslim state. Context only — not a scored adult primary_system (P19)."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not applicable / not stated for a Muslim birth-heritage coding."}
  childhood_catechism: {value: UNKNOWN, how_known: "No childhood religious curriculum named in S1–S5."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1070–1075", certainty: 0.5, cites: [{source: S5, locator: "Algebra; calendar paragraphs"}, {source: S1, locator: "calendar paragraph"}], how_known: "From Samarkand Algebra (~1070, S5) through Jalālī calendar adoption 1075 (S1); philosophical treatises undated (P39). 0.5."}
  age_at_first_lasting_contribution: {value: 22, certainty: 0.5, cites: [{source: S5, locator: "opening; Algebra paragraphs"}, {source: S1, locator: "opening"}], how_known: "1070 − 1048 = 22 (P30); 0.5 with the Algebra year."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "Philosophical treatises undated (P39); evidence dates use death year in statements' source book (2007 translation of earlier Arabic/Persian)."}
  lio_views_relative_to_major_work: {value: "unclear", certainty: 0.5, cites: [{source: S3, locator: "Appendix A"}, {source: S5, locator: "Algebra paragraphs"}], how_known: "Treatises undated relative to 1070–1075 math span."}
  worldview_during_major_work: {value: "CLASS_THEISM (Avicennan Necessary Being) as coded from the philosophical treatises; relation of those undated treatises to the 1070–1075 math span is unclear", certainty: 0.5, cites: [{source: S3, locator: "pp. 309, 317"}, {source: S4, locator: "§2.1"}], how_known: "Same evidence as primary_system; timing unclear (P39)."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "Geometric solution of cubics by intersecting conics; Euclid parallels commentary (S5; S1).", certainty: 0.7, cites: [{source: S5, locator: "Algebra / cubic paragraphs"}, {source: S1, locator: "Eṣfahān paragraph"}], how_known: "Coder's reading of mathematical work."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S5, locator: "education paragraphs"}], how_known: "Education in sciences at Nishapur noted; no clear childhood geometry story."}
  circle_present: {value: "unclear", rationale: "Worldview statements are Avicennan metaphysics, not a circle-form belief story.", certainty: 0.5, cites: [{source: S3, locator: "Appendix A"}, {source: S4, locator: "§2"}], how_known: "Coder's reading."}
  reading: "Lane B only: geometric form present in the cubic/Euclid work; no H1 claim. Avicennan Necessary Being worldview is Lane A."
  notes: "Do not treat Lane B geometry as evidence for A/B scores."

institutions:
  - {value: "Court of the Seljuq sultan Malik-Shāh, Eṣfahān (observatory / calendar commission)", role: astronomer, kind: "patron or funder", certainty: 0.7, cites: [{source: S1, locator: "calendar paragraph"}, {source: S5, locator: "Malik-Shah / Esfahan paragraphs"}], how_known: "Britannica and MacTutor."}
  - {value: "Patronage of Abū Ṭāhir, Samarkand (during Algebra composition)", role: mathematician, kind: "patron or funder", certainty: 0.7, cites: [{source: S5, locator: "Samarkand paragraph"}], how_known: "MacTutor."}
collaborators:
  []

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 63"}], how_known: "Study roster."}
  controversies:
    - {value: "Authorship of the Rubāʿiyyāt (quatrains): many scholars doubt he wrote the poetry later circulated under his name; verses appear centuries after his death; FitzGerald translation is free (S1). Philosophical treatises are treated as his by SEP and Aminrazavi (S4, S3). Quatrains unscored (P42).", certainty: 0.7, cites: [{source: S1, locator: "poetry paragraphs"}, {source: S3, locator: "epilogue pp. 280–281"}, {source: S4, locator: "§2; §2.3"}], how_known: "Britannica, Aminrazavi, SEP."}
  data_quality_flags: []
  open_questions:
    - "Page-check Arabic/Persian critical editions (Malik 1998; Jamshīd Nijād Awwal / Farhang) against Aminrazavi English for A/B quote wording."
    - "Date the philosophical treatises relative to 1070–1075 for timing.lio_views_relative_to_major_work."
    - "C_ledger / D_authority / E_scope from On Being and Obligation and eschatology passages (S4 §2.3; S3)."
    - "Any single quatrain with specific scholarly attribution strong enough to score under P42 (optional; not required if treatises hold)."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "Britannica Editors. \"Omar Khayyam.\" Encyclopaedia Britannica, updated 29 September 2026. https://www.britannica.com/biography/Omar-Khayyam-Persian-poet-and-astronomer."
    url: "https://www.britannica.com/biography/Omar-Khayyam-Persian-poet-and-astronomer"
    accessed: 2026-10-15
    reliability_note: "Unsigned editors' article body; Top Questions not cited. Body re-checked 2026-10-24 where reachable; fetch sometimes thin/paywalled."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, review]
  - id: S2
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S3
    type: primary
    kind: "scholarly edition"
    author: "Omar Khayyam (trans. Mehdi Aminrazavi)"
    year: 2007
    citation: "Aminrazavi, Mehdi. The Wine of Wisdom: The Life, Poetry and Philosophy of Omar Khayyam. Oxford: Oneworld, 2007. Appendix A: Translations of the Philosophical Treatises (pp. 287–317 cited). Internet Archive text/PDF (wineofwisdomlife0000raza / libgen.li mirror used for OCR)."
    url: "https://archive.org/details/wineofwisdomlife0000raza"
    accessed: 2026-10-24
    reliability_note: "First complete English of the six philosophical treatises (translator's claim in Appendix A introduction). Page numbers from printed markers in the PDF OCR. Epilogue (pp. 280–281) is Aminrazavi's commentary, not Khayyam's words. Arabic/Persian critical editions not collated this pass."
    source_quality: "primary / own words"
    used_for: [contribution, worldview, timing, review]
  - id: S4
    type: secondary
    kind: encyclopedia
    author: "Seyed N. Mousavian, Suzanne Sumner, Mehdi Aminrazavi, and Glen Van Brummelen"
    year: 2023
    citation: "Mousavian, Seyed N., Suzanne Sumner, Mehdi Aminrazavi, and Glen Van Brummelen. \"Umar Khayyam.\" Stanford Encyclopedia of Philosophy, first published 6 September 2011, substantive revision 18 April 2023. https://plato.stanford.edu/entries/umar-khayyam/."
    url: "https://plato.stanford.edu/entries/umar-khayyam/"
    accessed: 2026-10-24
    reliability_note: "Peer-reviewed SEP entry. Philosophy sections quote Arabic editions (Malik; Jamshīd Nijād Awwal; etc.). Aminrazavi is also translator of S3 — treat S3 treatise English and S4 analysis as agreeing but not fully independent on wording; independence for P48 rests on S3 primary text vs S4's use of separate Arabic editions plus MacTutor/Britannica for biography/science."
    source_quality: "reference entry"
    used_for: [basics, contribution, worldview, timing, lane_b, review]
  - id: S5
    type: secondary
    kind: encyclopedia
    author: "J. J. O'Connor and E. F. Robertson"
    year: 1999
    citation: "O'Connor, J. J., and E. F. Robertson. \"Omar Khayyam.\" MacTutor History of Mathematics Archive, University of St Andrews. https://mathshistory.st-andrews.ac.uk/Biographies/Khayyam/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Khayyam/"
    accessed: 2026-10-24
    reliability_note: "University reference archive; strongest on mathematics, Samarkand Algebra preface quote, and calendar/Euclid. Poetry remarks not used for worldview (P42)."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions]
---

# Omar Khayyam

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`. Deepen D1 2026-10-24: CLASS_THEISM; A 1 @ 0.7 / B 3 @ 0.7, both support corroborated (P48); mid_basin true; quatrains unscored (P42).

## Summary

Omar Khayyam (1048–1131), Persian mathematician, astronomer, and Avicennan philosopher [S1; S5; S4]. Working metaphysics: God as Necessary Being / Necessary Existent [S3, pp. 309, 317; S4, §2.1]. Algebra (cubics by conics) and Jalālī calendar [S1; S5]. Rubāʿiyyāt authorship disputed — not scored [S1; P42].

## Life and work

Born and died at Neyshābūr; worked also at Samarkand (Algebra under Abū Ṭāhir) and at Eṣfahān for Malik-Shāh’s calendar/observatory [S1; S5]. Philosophical treatises in the Peripatetic/Avicennan line [S4, §2; S3, Appendix A].

## Contribution and impact

Cubic equations by intersecting conics; Jalālī calendar; Euclid parallels commentary later used by Wallis [S1; S5; S4, §4]. Six philosophical treatises in English in Aminrazavi 2007 Appendix A [S3].

## Childhood and education

Sciences and philosophy at Neyshābūr; father possibly a tentmaker (name) [S1; S5].

## Adult working worldview

**Lane A.** primary_system CLASS_THEISM at 0.7. A 1 @ 0.7 (Necessary Being = God Most High; simple unity) [S3, pp. 309, 317; S4, §2.1]. B 3 @ 0.7 (causal series to Necessary Being; contingent order; evil accidental) [S3, pp. 292, 297; S4, §2.1]. mid_basin true @ 0.7 (P4). Quatrains not scored [S1; P42]. C, D, E UNKNOWN.

## Heritage (context only)

Persian [S1; S5]. Religious heritage by birth: Muslim / Islamic intellectual milieu of Seljuq Nishapur [S4; S5].

## Timing

Major work span ~1070–1075 (Algebra to Jalālī calendar) at 0.5 [S5; S1]. Philosophical treatises undated relative to that span [P39].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Geometric form present in cubic/Euclid work [S5; S1]. No H1 claim from worldview texts.

## Open questions

- Collate Aminrazavi English against Arabic/Persian critical editions.
- Date philosophical treatises vs 1070–1075.
- C / D / E from remaining treatises.
- Optional: any single attributed quatrain under P42.

## Research log

- 2026-10-15: Read Britannica (Editors) body.
- 2026-10-24 (D1): Aminrazavi *Wine of Wisdom* 2007 Appendix A (IA PDF/OCR); SEP “Umar Khayyam” (Mousavian et al., rev. 2023); MacTutor Khayyam. Anthology of Philosophy in Persia vol. 1 (Nasr/Aminrazavi) consulted for chapter presence; Tirtha/Rahman Contrariety reprint not used as primary quote source (S3 preferred). Quatrains left unscored (P42).
