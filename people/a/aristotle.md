---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch D)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-15
  change_log:
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch D, order P32: F 5, rank 9). Basics from SEP (Shields 2020). Worldview from Metaphysics XII (Ross trans.), Physics II (Hardie and Gaye trans.) and Nicomachean Ethics III (Ross trans.), read in the MIT Internet Classics Archive web copies. primary_system ARIST (0.7, founder rule); A_locus 1 (0.7, alternative 2); B_cause 3 (0.7, alternative 4); mid_basin true (0.7). C, D, E TODO. Draft, not reviewed."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Audit fixes (fallacy_catalog audit of 3f4817e, run 1). B_cause 3 kept (0.7, alternative 4) but reframed: free will placed in nature (§6 B 3 anchor), not an exception to lawful cause; added EN 1113b17-19, Met. Θ.2 1046b4-7, Θ.5 1048a5-11 and the compatibilist alternative EN 1114a13-21; chance noted as incidental cause. Bekker numbers verified, approximate caveats removed. mid_basin true (0.7) unchanged."}

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
  full_name: {value: "Aristotle", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}
  native_name: {value: "Aristotelēs (Ἀριστοτέλης)", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's transliteration of the standard Greek name; SEP gives only the English form."}
  aliases:
    - {name: "the Stagirite", kind: "title or honorific"}

basics:
  birth:
    date: {value: "-384", certainty: 0.7, cites: [{source: S1, locator: "§1 ('Born in 384 B.C.E.')"}], how_known: "SEP alone was read (P15)."}
    place: {value: "Stagira, Macedonian region of northeastern Greece", modern_name: "Stagira, Greece", polity_then: "Stagira (Chalcidice)", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP alone."}
  death:
    date: {value: "-322", certainty: 0.7, cites: [{source: S1, locator: "§1 ('died there of natural causes the following year, in 322')"}], how_known: "SEP alone."}
    place: {value: "Chalcis, Euboea", modern_name: "Chalcis, Greece", polity_then: "Chalcis", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP alone."}
  first_lasting_contribution_year: {value: UNKNOWN, how_known: "SEP does not date the treatises; it says the surviving works read like lecture notes and drafts 'first written and then reworked' (§2). Every candidate year lies between c. 367 BC (arrival at the Academy at about seventeen) and his death in 322 BC (P30 death cap)."}
  era_bucket: {value: "-500 to 499", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "Every candidate year (c. 367–322 BC) is in '-500 to 499' (P2); SEP alone, so 0.7."}
  region_of_birth: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "Greece is Southern Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "§1 (Athens, Assos, Lesbos, Pella)"}], how_known: "Mostly Athens; Assos (now Turkey, Middle East and North Africa) for about three years. Coder's reading of where most work was done."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "As the source records it."}
  languages_of_work: {value: [Greek], certainty: 0.7, cites: [{source: S1, locator: "§§2–5 (Greek terms)"}], how_known: "SEP."}
  occupations: {value: ["philosopher", "teacher (head of the Lyceum)", "naturalist"], certainty: 0.7, cites: [{source: S1, locator: "§1; opening (empirical biology)"}], how_known: "SEP."}

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
    - {value: "Father named Nicomachus", name: "Nicomachus", role: father, certainty: 0.7, cites: [{source: S1, locator: "§1 ('Nicomachus, named for Aristotle's father')"}], how_known: "SEP alone."}
  household_circumstances: {value: TODO}
  schooling:
    - {value: "Plato's Academy, Athens, from about age seventeen until Plato's death in 347", stage: university, run_by: private, years: "c. 367–347 BC", ages: "c. 17–37", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP; 'university' is the nearest stage value, and 'private' the coder's reading of the Academy."}
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
    cites: [{source: S2, locator: "Met. XII (Λ) ch. 8 (Ross part 8, closing paragraph; Bekker 1074a38–b14)"}]
    how_known: "His own text in Ross's translation, read in an unofficial web copy, so capped at 0.7 (§7)."
  primary_system:
    value: ARIST
    basis: written_profession
    certainty: 0.7
    cites: [{source: S2, locator: "Met. XII (Λ) chs. 6–10"}, {source: S1, locator: "§§2, 7–9"}]
    how_known: "Founder rule (§1): he founded Aristotelianism. Capped at 0.7: the texts were read in an unofficial web copy of Ross, and CLASS_THEISM is a named alternative."
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
      cites: [{source: S2, locator: "Met. XII (Λ) ch. 7 (Ross part 7; Bekker 1072b26–1073a5); ch. 10 (Ross part 10, opening; Bekker 1075a11–15)"}]
      how_known: "His text in an unofficial web copy of Ross (0.7 cap); a named alternative also caps it at 0.7."
      rationale: "Leans to the interventionist pole with limits. The first mover is 'a living being, eternal, most good' and 'a substance which is eternal and unmovable and separate from sensible things' (Λ.7): a living, thinking god outside the world. The limits: it moves things only 'as being loved', it is 'impassive and unalterable', and its thinking 'is a thinking on thinking' (Λ.7, Λ.9), so it does not act on or attend to the world as a person would. Same pattern and score as Aquinas and Ibn Sina (A 1). Named alternative 2: Λ.10 says the universe holds the good 'both' as 'something separate' and 'as the order of the parts', though 'more in the latter' sense of the leader."
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.7
      cites: [{source: S3, locator: "Phys. II ch. 8 (Hardie and Gaye trans., Bekker 199b24–26)"}, {source: S4, locator: "EN III ch. 5 (Ross trans., Bekker 1113b6–8, 1113b17–19; alternative reading 1114a13–21)"}, {source: S2, locator: "Met. IX (Θ) ch. 2, Bekker 1046b4–7; ch. 5, Bekker 1048a5–11"}]
      how_known: "His texts in unofficial web copies (0.7 cap); a named alternative also caps it at 0.7."
      rationale: "Scored on his account of nature (P6). Nature is regular: 'In natural products the sequence is invariable, if there is no impediment', and what happens 'always or for the most part' is not by chance (Phys. II.8). No miracle, petition or divine exemption appears: the first mover acts only as final cause. Chance in 'always or for the most part' is an incidental cause (Phys. II.5), not an exemption from nature's order. B 3 comes from free will placed in nature (CODING_GUIDE §6 B 3 anchor, P30 #14), not from an exception to lawful cause: 'virtue also is in our own power, and so too vice. For where it is in our power to act it is also in our power not to act' (EN III.5, 1113b6–8), with the agent as the 'originator and begetter' of his actions (1113b17–19); rational powers, unlike natural ones, are 'of contraries' (Met. Θ.2 1046b4–7; Θ.5 1048a5–11). On his own framing this is a different kind of principle from nature, not a suspension of it. Named alternative 4: on a compatibilist reading (EN III.5, 1114a13–21: character, once formed, makes action necessary in its turn), the impediment clause is the only qualifier and nothing is exempt. Framing corrected after the fallacy_catalog audit of 3f4817e."
    C_ledger: {value: TODO}
    D_authority: {value: TODO}
    E_scope: {value: TODO}
  mid_basin:
    value: true
    certainty: 0.7
    cites: [{source: S2, locator: "Met. XII (Λ) ch. 7"}, {source: S3, locator: "Phys. II ch. 8"}, {source: S4, locator: "EN III ch. 5"}]
    how_known: "P4/P6: A_locus 1 (0.7) and B_cause 3 (0.7) meet A ≤ 1 and B ≥ 3 at ≥ 0.7. B's alternative 4 is on the same side; A's alternative 2 is not, so the cap is A's 0.7 (P10, P30)."
  statements:
    - text: "It is clear then from what has been said that there is a substance which is eternal and unmovable and separate from sensible things."
      cites: [{source: S2, locator: "Met. XII (Λ) ch. 7, Ross part 7, last paragraph (Bekker 1073a3–5)"}]
      date: "-322"
      context: "Conclusion of the argument for the first unmoved mover."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "Ross translation read on the MIT Internet Classics Archive (unofficial web copy; Bekker numbers are not printed there and were added by the coder, verified by the fallacy_catalog audit of 3f4817e). Date is the death cap; the treatise is undated."
    - text: "We say therefore that God is a living being, eternal, most good, so that life and duration continuous and eternal belong to God; for this is God."
      cites: [{source: S2, locator: "Met. XII (Λ) ch. 7, Ross part 7 (Bekker 1072b28–30)"}]
      date: "-322"
      context: "Same chapter: the first mover's life is thought."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-15
      note: "Same web copy; Bekker numbers verified."
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
  coder_notes: "Translations named: Ross (Metaphysics, Nicomachean Ethics) and Hardie and Gaye (Physics), all read on the MIT Internet Classics Archive, which prints no Bekker numbers; Bekker locators were added by the coder and verified by the fallacy_catalog audit of 3f4817e. The quotes are marked 'secondary quotation' because the archive is an unofficial web copy, not an edition; that caps every worldview field at 0.7 (§7). Basis written_profession: SEP §2 calls the surviving works lecture notes and in-house compilations for auditors; they are written for others, but if read as unpublished the private ceiling (0.7) gives the same certainty. Coder's call: C, D and E left TODO (not researched in this run)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Greek, from the Macedonian region", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
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
  - {value: "Lyceum, Athens", role: "founder and head", years: "335–323 BC", kind: "other", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
collaborators:
  - {value: "Plato", relation: teacher, certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
  - {value: "Theophrastus", relation: collaborator, certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
  - {value: "Alexander the Great", relation: "student or assistant", note: "tutored from about age 13 to 15", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}

review:
  roster_status_reason: {value: "Core in v8 (F 5: Claude, DeepSeek, Gemini, GPT, Grok).", certainty: 0.7, cites: [{source: S5, locator: "roster.csv, rank 9"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Britannica blocked (Cloudflare, 2026-10-15); basics from SEP alone, so 0.7."
  open_questions:
    - "Check all quotations against Barnes (ed.), The Complete Works of Aristotle (1984)."
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
    accessed: 2026-10-15
    reliability_note: "Peer-reviewed reference article."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Aristotle"
    citation: "Aristotle. Metaphysics, Book XII. Translated by W. D. Ross. Internet Classics Archive (MIT). https://classics.mit.edu/Aristotle/metaphysics.12.xii.html."
    url: "https://classics.mit.edu/Aristotle/metaphysics.12.xii.html"
    accessed: 2026-10-15
    reliability_note: "Unofficial web copy of Ross's Oxford translation; no Bekker numbers. 0.7 cap (§7)."
    used_for: [worldview, timing, lane_b]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "Aristotle"
    citation: "Aristotle. Physics, Book II. Translated by R. P. Hardie and R. K. Gaye. Internet Classics Archive (MIT). https://classics.mit.edu/Aristotle/physics.2.ii.html."
    url: "https://classics.mit.edu/Aristotle/physics.2.ii.html"
    accessed: 2026-10-15
    reliability_note: "Unofficial web copy of the Oxford translation. 0.7 cap."
    used_for: [worldview]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "Aristotle"
    citation: "Aristotle. Nicomachean Ethics, Book III. Translated by W. D. Ross. Internet Classics Archive (MIT). https://classics.mit.edu/Aristotle/nicomachaen.3.iii.html."
    url: "https://classics.mit.edu/Aristotle/nicomachaen.3.iii.html"
    accessed: 2026-10-15
    reliability_note: "Unofficial web copy of Ross's translation. 0.7 cap."
    used_for: [worldview]
  - id: S5
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
---

# Aristotle

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Aristotle (384–322 BC), student of Plato and founder of the Lyceum, created the first formal logic and the four-cause scheme of explanation and did extensive empirical biology [S1]. In Metaphysics XII he argues for 'a substance which is eternal and unmovable and separate from sensible things', 'a living being, eternal, most good' [S2, Λ.7]. Draft: primary_system ARIST (0.7); A 1 (0.7, alternative 2); B 3 (0.7, alternative 4); mid_basin true (0.7).

## Life and work

Born at Stagira; at Plato's Academy from about seventeen until 347; Assos and Lesbos; tutor to Alexander; the Lyceum in Athens from 335; died at Chalcis in 322 [S1].

## Contribution and impact

Syllogistic logic, four causes, hylomorphism, biology [S1].

## Childhood and education

Father Nicomachus; the Academy [S1].

## Adult working worldview

A separate first mover that moves as an object of love [S2, Λ.7]; nature regular 'if there is no impediment' [S3, II.8]; human choice 'in our own power', free will placed in nature [S4, III.5].

## Heritage (context only)

Greek, Macedonian region [S1].

## Timing

Treatises undated.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form present; circle partly [S1; S2].

## Open questions

- Check quotations against Barnes 1984; score C, D, E.

## Research log

- 2026-10-15: Read SEP (Shields 2020) and the MIT Internet Classics Archive texts of Met. XII, Phys. II and EN III. Britannica blocked.
