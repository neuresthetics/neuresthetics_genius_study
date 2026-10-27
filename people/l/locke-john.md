---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch G)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to early_modern. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch G, order P32: F 5, rank 46). Basics from SEP (Uzgalis) and Britannica (Rogers). Worldview from his Essay Concerning Human Understanding, Book IV, read in Gutenberg #10616 (web copy, 0.7 cap). Not a scientist under P30 (no lasting theory or result about natural systems listed). primary_system CHRIST 0.7; A 0 at 0.7 (alt 1); B 3 at 0.7 (alt 2) from his own statement on miracles and the course of nature (P16); D 2 at 0.7; C, E UNKNOWN; mid_basin true at 0.7. Draft, not reviewed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #46). Needs: A single source; B single source (both @0.7 written_profession; dark hollow). Verified Essay IV.x.6 / IV.xvi.13 / IV.xviii.10 against Fraser Clarendon 1894 scholarly edition vol. 2 (S5: pp. 309, 382, 425). Added A Discourse of Miracles (S6; Works 1823 via Hanover) as independent primary for B and CHRIST. Reasonableness of Christianity Messiah profession (S7; archive.org OCR) for CHRIST. P47 source_quality on S1–S7. P48 support: A/B/D corroborated (A S3+S5; B S3+S5+S6; D S3+S5). Values/certs unchanged (A 0, B 3, D 2 @0.7; named alts). Statements verified_against → scholarly edition. Chart-moving YES: dark hollow → dark filled. No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: locke-john
  display_name: "John Locke"
  roster:
    canonical_name: "John Locke"
    rank: 46
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: philosophy
    field_bucket: philosophy
  full_name: {value: "John Locke", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "opening"}], how_known: "SEP and Britannica agree."}
  native_name: {value: UNKNOWN, how_known: "English; no other form."}
  aliases:
    - {name: "John-Locke", kind: "roster alias"}
    - {name: "Locke-John", kind: "roster alias"}

basics:
  birth:
    date: {value: "1632-08-29", calendar: julian, certainty: 0.7, cites: [{source: S2, locator: "opening"}], how_known: "Britannica gives 29 August 1632; SEP gives the year only (1632). England used the Julian calendar until 1752, so the source date is kept as julian (data dictionary). One source for the day."}
    place: {value: "Wrington, Somerset, England", modern_name: "Wrington, England, United Kingdom", polity_then: "Kingdom of England", certainty: 1.0, cites: [{source: S1, locator: "§1.1"}, {source: S2, locator: "opening"}], how_known: "SEP and Britannica agree."}
  death:
    date: {value: "1704-10-28", calendar: julian, certainty: 0.7, cites: [{source: S2, locator: "opening"}], how_known: "Britannica gives 28 October 1704; SEP gives the year only. Julian, as above."}
    place: {value: "High Laver, Essex, England", modern_name: "High Laver, England, United Kingdom", polity_then: "Kingdom of England", certainty: 0.7, cites: [{source: S2, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1689, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "An Essay Concerning Human Understanding (1689) in SEP (P13); one source for the year. Earlier writings (Two Tracts 1660, Essays on the Law of Nature 1663-4) were first published in the 20th century (S2), so they are not the first public statement (P30)."}
  era_bucket: {value: "1600 to 1749", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "From 1689 (P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 1.0, cites: [{source: S1, locator: "§1.1"}, {source: S2, locator: "opening"}], how_known: "England; the United Kingdom is Northern Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "Oxford and London; years of exile in the Netherlands (SEP §1.2), so 0.7."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [English, Latin], certainty: 0.7, cites: [{source: S2, locator: "'Oxford' (Essays on the Law of Nature; Westminster curriculum)"}], how_known: "Britannica; English works plus Latin early writings."}
  occupations: {value: ["philosopher", "Oxford academic", "physician and medical researcher", "government official"], certainty: 0.7, cites: [{source: S1, locator: "opening; §1.2"}], how_known: "SEP."}

contribution:
  era_bucket: early_modern
  fields: {value: ["epistemology", "political philosophy", "philosophy of religion", "education"], certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "opening"}], how_known: "SEP and Britannica."}
  lasting_original_contributions:
    - {value: "An Essay Concerning Human Understanding: empiricist account of the origin and limits of knowledge", year: 1689, kind: work, lasting: "'one of the first great defenses of modern empiricism' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP gives the year; Britannica's lead names his empiricism (S2)."}
    - {value: "Two Treatises of Government: political authority from natural rights and consent", year: 1689, kind: work, lasting: "political liberalism; an inspirer of the U.S. Constitution (S2, lead)", certainty: 0.7, cites: [{source: S2, locator: "'Oxford' (Two Treatises of Government (1689))"}], how_known: "Britannica's signed body gives 1689; the first edition is often dated 1690 (title-page date, not checked), so 0.7."}
    - {value: "Some Thoughts Concerning Education", year: 1693, kind: work, lasting: "'enormously influential' (S2)", certainty: 0.7, cites: [{source: S2, locator: "'Early years'"}], how_known: "Britannica."}
  evidence_of_impact:
    - {value: "His works 'lie at the foundation of modern philosophical empiricism and political liberalism'; an inspirer of the European Enlightenment and the U.S. Constitution", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S2, locator: "opening"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Foundational work in empiricism and liberalism (S1, S2).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Church of England, sympathetic to Puritanism", certainty: 0.7, cites: [{source: S2, locator: "'Early years'"}, {source: S1, locator: "§1.1 ('Puritan parents')"}], how_known: "Britannica: 'sympathetic to Puritanism but remained within the Church of England'; SEP: 'Puritan parents'. They differ in emphasis, so 0.7."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father a country lawyer who served as a cavalry captain on the parliamentary side", role: parents, certainty: 1.0, cites: [{source: S1, locator: "§1.1"}, {source: S2, locator: "'Early years'"}], how_known: "SEP and Britannica agree."}
  household_circumstances: {value: "Modest means", certainty: 0.7, cites: [{source: S1, locator: "§1.1"}], how_known: "SEP."}
  schooling:
    - {value: "Westminster School, London", stage: "grammar or secondary school", run_by: "state or municipal", years: "1647–1652", ages: "15–20", certainty: 0.7, cites: [{source: S1, locator: "§1.1"}, {source: S2, locator: "'Early years'"}], how_known: "Both give 1647; run_by is the coder's reading (taken over by the republican government, S2)."}
    - {value: "Christ Church, Oxford", stage: university, run_by: "other", years: "1652–", ages: "20–", certainty: 1.0, cites: [{source: S1, locator: "§1.1"}, {source: S2, locator: "'Oxford'"}], how_known: "Both give autumn 1652."}
  early_mathematics: {value: "other", certainty: 0.7, cites: [{source: S2, locator: "'Early years'"}], how_known: "Mathematics was in the Westminster curriculum (S2); level not stated."}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "Richard Busby, headmaster of Westminster", certainty: 0.7, cites: [{source: S2, locator: "'Early years'"}], how_known: "Britannica."}
  languages_in_childhood: {value: TODO}
  notable_events:
    - {value: "English Civil Wars begin", year: 1642, age: 10, certainty: 0.7, cites: [{source: S2, locator: "'Early years'"}], how_known: "Britannica: 10 years old at the start."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1689–1693", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "'Early years'"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Church of England", certainty: 0.5, cites: [{source: S1, locator: "§2 (Ashcraft on Anglican comprehension)"}], how_known: "Inferred: SEP discusses whether his views were Latitudinarian Anglican; membership not stated in the passages read."}
  self_described_science_religion_relation: {value: "Reason judges whether a revelation is divine, and nothing contrary to the clear dictates of reason may be urged as faith; but where reason reaches only probability, clear revelation may determine assent, and what God has revealed is certainly true.", certainty: 0.7, cites: [{source: S3, locator: "Book IV, ch. XVIII, §§9–10"}, {source: S5, locator: "vol. 2, Book IV, ch. XVIII, §10, p. 425"}], how_known: "Published work (written_profession) checked in Fraser Clarendon 1894 (S5) against Gutenberg web copy (S3); §7 / named alts keep 0.7. Nidditch (Clarendon, 1975) not opened."}
  primary_system:
    value: CHRIST
    basis: written_profession
    certainty: 0.7
    cites: [{source: S3, locator: "Book IV, ch. XVI, §13; ch. XVIII, §10"}, {source: S5, locator: "vol. 2, pp. 382, 425"}, {source: S6, locator: "definition; Moses and Christ attested by miracles"}, {source: S7, locator: "pp. 17–19 (Messiah as the great proposition)"}, {source: S1, locator: "§2 (The Reasonableness of Christianity)"}]
    rationale: "Accepts revelation: 'Whatever God hath revealed is certainly true' and divine revelation once judged by reason (IV.xviii.10; S5 p. 425); well-attested miracles 'give it also to other truths, which need such confirmation' (IV.xvi.13; S5 p. 382). Discourse of Miracles: a miracle is 'contrary to the established course of nature' and credentials for messengers from the one true God; Moses and Christ (not Mahomet) come attested by miracles (S6). Reasonableness: the faith that distinguishes believers is that Jesus is the Messiah (S7 pp. 17–19). So not DEISM (P27). Named alternative: a minimal or anti-Trinitarian Christianity (not fully read), so 0.7."
    how_known: "Essay in Gutenberg (S3) + Fraser Clarendon 1894 (S5); Discourse of Miracles (S6); Reasonableness OCR (S7). Independent source ids → corroborated (P48)."
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Chosen: accepts revelation and miracles as confirming it; Messiah profession in Reasonableness."}
    - {code: DEISM, reason: "Rejected: does not reject revelation (P27)."}
    - {code: CLASS_THEISM, reason: "Rejected: God known by demonstration but revelation retained; empiricist, not scholastic."}
    - {code: CLTHEI, reason: "Not chosen: miracles are a special case that confirms revelation, not the ordinary course of events."}
  lio_axes:
    A_locus:
      value: 0
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S3, locator: "Book IV, ch. X, §§6, 13"}, {source: S5, locator: "vol. 2, Book IV, ch. X, §6, p. 309; §13, p. 316"}]
      how_known: "Published work in Gutenberg web copy (S3) verified against Fraser Clarendon 1894 scholarly edition (S5 pp. 309, 316). Named alternative (1). Independent source ids → corroborated (P48); value/certainty unchanged."
      rationale: "A transcendent knowing person who made the world: reason proves 'an eternal, most powerful, and most knowing Being' (IV.x.6; S5 p. 309), and materialists who make all matter 'deny a God, that is, an eternal cogitative Being' (IV.x.13; S5 p. 316). Same pattern as Boyle and Bacon, scored 0. Named alternative: 1 (he allows in IV.x.13 that the argument holds 'whether you imagine that Being to be material or no')."
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S3, locator: "Book IV, ch. XVI, §13"}, {source: S5, locator: "vol. 2, Book IV, ch. XVI, §13, p. 382"}, {source: S6, locator: "definition of miracle; credentials for revelation"}]
      how_known: "Essay IV.xvi.13 in Gutenberg (S3) verified in Fraser Clarendon 1894 (S5 p. 382); independent Discourse of Miracles (S6). Named alternative (2). Independent source ids → corroborated (P48); value/certainty unchanged."
      rationale: "Scored on his account of nature (P6, P16). 'The common experience and the ordinary course of things' rightly govern belief, but God 'has the power to change the course of nature', and well-attested miracles are 'the proper case' where strangeness does not lessen assent (IV.xvi.13; S5 p. 382). Discourse: a miracle is a sensible operation 'contrary to the established course of nature' taken as divine, and such signs are the credentials of a messenger from God (S6). Lawful course of nature with a stated, limited exception (miracles that confirm revelation): the B 3 anchor (P27). Named alternative: 2, since he does not say the miracles are rare or past."
    C_ledger: {value: UNKNOWN, how_known: "Passages read do not treat reward and punishment of persons."}
    D_authority:
      value: 2
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S3, locator: "Book IV, ch. XVIII, §§9–10"}, {source: S5, locator: "vol. 2, Book IV, ch. XVIII, §10, p. 425"}]
      how_known: "Gutenberg (S3) verified against Fraser Clarendon 1894 (S5 p. 425). Independent source ids → corroborated (P48)."
      rationale: "Two domains each with its own authority (D 2 anchor, P27; same pattern as Boyle): whether a revelation is divine 'reason must judge', and nothing contrary to reason may be urged as faith; but where reason reaches only probability, 'clear revelation, as another principle of truth and ground of assent, may determine' (IV.xviii.9–10; S5 p. 425)."
    E_scope: {value: UNKNOWN, how_known: "Scored on the world's order (P7); nothing read on in-group exceptions in events."}
  mid_basin: {value: true, certainty: 0.7, cites: [{source: S3, locator: "Book IV, ch. X, §6; ch. XVI, §13"}, {source: S5, locator: "vol. 2, pp. 309, 382"}], how_known: "A_locus 0 (≤ 1) and B_cause 3 (≥ 3), both at 0.7 and now corroborated (P4, P6, P48). A's alternative 1 meets the condition; B's alternative 2 does not, so the cap is the certainty of B 3 itself, 0.7 (P10, P30). F = 5."}
  statements:
    - text: "THAT THERE IS AN ETERNAL, MOST POWERFUL, AND MOST KNOWING BEING; which whether any one will please to call God, it matters not."
      cites: [{source: S3, locator: "Book IV, ch. X, §6"}, {source: S5, locator: "vol. 2, p. 309"}]
      date: "1689"
      context: "Conclusion of his demonstration of God's existence from our own existence and knowledge."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Gutenberg #10616 capitals matched to Fraser Clarendon 1894 wording (S5 p. 309: 'That there is an eternal, most powerful, and most knowing Being'). Nidditch (1975) not opened."
    - text: "For where such supernatural events are suitable to ends aimed at by Him who has the power to change the course of nature, there, UNDER SUCH CIRCUMSTANCES, that may be the fitter to procure belief, by how much the more they are beyond or contrary to ordinary observation. This is the proper case of MIRACLES, which, well attested, do not only find credit themselves, but give it also to other truths, which need such confirmation."
      cites: [{source: S3, locator: "Book IV, ch. XVI, §13"}, {source: S5, locator: "vol. 2, p. 382"}]
      date: "1689"
      context: "Section titled 'One Case where contrary Experience lessens not the Testimony', after he says 'the common experience and the ordinary course of things' rightly influence assent."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Verified in Fraser Clarendon 1894 (S5 p. 382). Capitals follow Gutenberg; Fraser has 'supernatural events' / 'miracles' without the eBook's full-caps emphasis."
    - text: "Whatever God hath revealed is certainly true: no doubt can be made of it. This is the proper object of faith: but whether it be a DIVINE revelation or no, reason must judge"
      cites: [{source: S3, locator: "Book IV, ch. XVIII, §10"}, {source: S5, locator: "vol. 2, p. 425"}]
      date: "1689"
      context: "Chapter 'Of Faith and Reason, and their distinct Provinces'."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Verified in Fraser Clarendon 1894 (S5 p. 425). §10 heading in Fraser: matters where reason can afford certain knowledge."
    - text: "A miracle then I take to be a sensible operation, which, being above the comprehension of the spectator, and in his opinion contrary to the established course of nature, is taken by him to be divine."
      cites: [{source: S6, locator: "opening definition (Works 1823, 9:256)"}]
      date: "1702"
      context: "A Discourse of Miracles; definition that grounds miracles as credentials of divine revelation (Moses and Christ)."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Hanover Historical Texts Project excerpt of Works (London, 1823) vol. 9; unofficial web copy, §7. Independent work corroborating Essay IV.xvi.13 on nature's course and miracles."
  changes_over_life: []
  coder_notes: "Coder's call: Book IV of the Essay is the main primary for A/B/D, now dual-sourced (Gutenberg + Fraser Clarendon 1894). Discourse of Miracles and Reasonableness of Christianity read in unofficial web/OCR copies for B and CHRIST. Locke worked with Boyle and Sydenham as a medical researcher (S1) but no lasting theory or result of his about natural systems is listed, so he is not a scientist under P30, and B rests on his own statements about nature (P16). Nidditch Clarendon 1975 still unread."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "English", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "opening"}], how_known: "Two sources."}
  religious_heritage_by_birth: {value: "Church of England, Puritan-leaning", certainty: 0.7, cites: [{source: S2, locator: "'Early years'"}], how_known: "Britannica."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1689–1693", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "'Early years'"}], how_known: "1689 to 1693, first to last listed lasting contribution (P29, P30)."}
  age_at_first_lasting_contribution: {value: 57, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "1689 − 1632 = 57 (P30)."}
  first_evidence_of_lio_type_views: {value: "1689", certainty: 0.7, cites: [{source: S3, locator: "Book IV, ch. XVI, §13"}, {source: S5, locator: "vol. 2, p. 382"}], how_known: "Earliest work read (P30); the Essay states a lawful ordinary course of nature with miracles as the stated exception. Earlier unpublished writings not read."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.7, cites: [{source: S3, locator: "Book IV"}, {source: S5, locator: "vol. 2, Book IV"}], how_known: "In the first listed lasting work."}
  worldview_during_major_work: {value: "CHRIST", certainty: 0.7, cites: [{source: S3, locator: "Book IV, ch. XVIII"}, {source: S5, locator: "vol. 2, p. 425"}], how_known: "As primary_system."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "Models knowledge on demonstration: God's existence is proved 'as clear as demonstration can make it' (IV.x.13), with triangle analogies (IV.x.5).", certainty: 0.5, cites: [{source: S3, locator: "Book IV, ch. X, §§5, 13"}, {source: S5, locator: "vol. 2, Book IV, ch. X"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "'Early years'"}], how_known: "Mathematics at Westminster; nothing on its effect."}
  circle_present: {value: "yes", rationale: "God demonstrated by reason; nature runs on an ordinary course; reason judges revelation.", certainty: 0.5, cites: [{source: S3, locator: "Book IV, ch. X, XVI, XVIII"}, {source: S5, locator: "vol. 2, Book IV"}], how_known: "Coder's reading."}
  reading: "A demonstrated transcendent God with a lawful ordinary course of nature and attested miracles as the exception."
  notes: ""

institutions:
  - {value: "Christ Church, Oxford", role: "student, then senior censor (1663)", years: "1652–", kind: university, certainty: 0.7, cites: [{source: S2, locator: "'Oxford'"}], how_known: "Britannica."}
  - {value: "Board of Trade", role: member, years: "1696–1700", kind: "government or state body", certainty: 0.7, cites: [{source: S1, locator: "§1.3"}], how_known: "SEP."}
collaborators:
  - {value: "Anthony Ashley Cooper, 1st Earl of Shaftesbury", relation: "mentor or employer", note: "patron and employer from 1666", certainty: 0.7, cites: [{source: S1, locator: "§1.2"}], how_known: "SEP."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 46"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags: []
  open_questions:
    - "Nidditch (Clarendon, 1975) critical text still unread; Fraser 1894 used as scholarly check."
    - "Full Reasonableness beyond Messiah profession (anti-Trinitarian debate) and Vindication unread."
    - "Birth/death day still single-source (Britannica); SEP gives years only."
    - "C_ledger and E_scope still UNKNOWN."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "William Uzgalis"
    year: 2022
    citation: "Uzgalis, William. \"John Locke.\" Stanford Encyclopedia of Philosophy, first published 2 September 2001, substantive revision 7 July 2022. https://plato.stanford.edu/entries/locke/."
    url: "https://plato.stanford.edu/entries/locke/"
    accessed: 2026-10-15
    reliability_note: "Peer-reviewed reference article."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, institutions, collaborators]
  - id: S2
    type: secondary
    kind: encyclopedia
    author: "Graham A. J. Rogers"
    citation: "Rogers, Graham A. J. \"John Locke.\" Encyclopaedia Britannica, updated 25 August 2026. https://www.britannica.com/biography/John-Locke."
    url: "https://www.britannica.com/biography/John-Locke"
    accessed: 2026-10-15
    reliability_note: "Signed article body, first pages ('Early years', 'Oxford'); the Top Questions box is not used."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, heritage, timing, lane_b, institutions]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "John Locke"
    year: 1689
    citation: "Locke, John. An Essay Concerning Humane Understanding, Volume 2 (Books III–IV). Project Gutenberg eBook #10616."
    url: "https://www.gutenberg.org/ebooks/10616"
    accessed: 2026-10-15
    reliability_note: "Unofficial web copy; source edition not named in the eBook; §7 cap 0.7. Quotes checked against S5 Fraser Clarendon 1894."
    source_quality: "unofficial web copy"
    used_for: [worldview, timing, lane_b]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S5
    type: primary
    kind: "scholarly edition"
    author: "John Locke"
    year: 1894
    citation: "Locke, John. An Essay Concerning Human Understanding. Ed. Alexander Campbell Fraser. Vol. 2. Oxford: Clarendon Press, 1894. (Book IV, chs. X, XVI, XVIII.)"
    url: "https://s3.us-west-1.wasabisys.com/luminist/EB/L/Locke%20-%20Human%20Understanding%20Vol%202.pdf"
    accessed: 2026-10-24
    reliability_note: "Clarendon Press scholarly edition with Fraser notes; used to verify Gutenberg Essay quotes (IV.x.6 p. 309; IV.xvi.13 p. 382; IV.xviii.10 p. 425)."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview, timing, lane_b]
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "John Locke"
    year: 1702
    citation: "Locke, John. A Discourse of Miracles (written 1701/2). In The Works of John Locke, 10 vols. (London, 1823), 9:256–265. Excerpts via Hanover Historical Texts Project."
    url: "https://history.hanover.edu/courses/excerpts/347jlmir.html"
    accessed: 2026-10-24
    reliability_note: "Unofficial web excerpt of the 1823 Works text; §7. Independent primary for miracles vs course of nature and revelation credentials."
    source_quality: "unofficial web copy"
    used_for: [worldview]
  - id: S7
    type: primary
    kind: "published work by the subject"
    author: "John Locke"
    year: 1695
    citation: "Locke, John. The Reasonableness of Christianity, as Delivered in the Scriptures (1695). Archive.org OCR of an early printed edition (thereasonablenes00lockuoft)."
    url: "https://archive.org/details/thereasonablenes00lockuoft"
    accessed: 2026-10-24
    reliability_note: "OCR of a printed edition; unofficial web copy, §7. Used for Messiah / belief profession (printed pp. 17–19 in that scan)."
    source_quality: "unofficial web copy"
    used_for: [worldview]
---

# John Locke

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

John Locke (1632–1704), English philosopher: An Essay Concerning Human Understanding, Two Treatises of Government, Some Thoughts Concerning Education [S1, S2]. Deepen D1: primary_system CHRIST 0.7 corroborated; A 0, B 3, D 2 at 0.7 corroborated (Fraser Clarendon + Discourse / Reasonableness); C, E UNKNOWN; mid_basin true at 0.7 — dark filled.

## Life and work

Westminster School and Christ Church, Oxford; physician and secretary to Shaftesbury; exile in the Netherlands; Board of Trade [S1, S2].

## Contribution and impact

The Essay (1689), Two Treatises (1689), Some Thoughts Concerning Education (1693) [S1, S2].

## Childhood and education

Born at Wrington to a lawyer's family sympathetic to Puritanism; Westminster from 1647, Oxford from 1652 [S1, S2].

## Adult working worldview

Reason demonstrates 'an eternal, most powerful, and most knowing Being' [S3, IV.x.6; S5, p. 309]. The ordinary course of things governs belief, but well-attested miracles by Him 'who has the power to change the course of nature' confirm revealed truths [S3, IV.xvi.13; S5, p. 382]; a miracle is 'contrary to the established course of nature' and a credential of divine mission [S6]. Reason judges whether a revelation is divine; clear revelation decides where reason reaches only probability [S3, IV.xviii.9–10; S5, p. 425]. The Reasonableness takes believing that Jesus is the Messiah as the distinguishing Christian profession [S7, pp. 17–19].

## Heritage (context only)

English; Church of England with Puritan sympathies [S2].

## Timing

First lasting contribution 1689, at 57 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Demonstrative style on God; circle present [S3, S5].

## Open questions

- Nidditch (Clarendon, 1975) still unread; Fraser 1894 used as scholarly check.
- Fuller Reasonableness / anti-Trinitarian debate; C and E still UNKNOWN.
- Birth/death day still Britannica-only.

## Research log

- 2026-10-15: Read SEP and Britannica (first pages); read Essay Book IV, chs. X, XVI, XVIII in Gutenberg #10616.
- 2026-10-24: Deepen D1 — verified Essay quotes in Fraser Clarendon 1894 vol. 2 (S5); read Discourse of Miracles (S6 Hanover/Works 1823) and Reasonableness Messiah profession (S7 archive OCR). P47/P48; A/B hollow → filled.
