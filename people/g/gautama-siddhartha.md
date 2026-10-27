---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 4
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch X)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to ancient. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #128). Refresh SEP Siderits (rev. 2023) and Britannica Lopez (1 Oct 2026); both reaffirm nothing in his own hand and discourses written centuries later. P47 source_quality on S1–S4. P50: Wikipedia EN The Buddha (S4) agrees traditional birth Lumbini / death Kushinagar (Kasia) with Britannica; life years still UNKNOWN (P39). P49 considered and not stretched: SEP §1 explicitly declines to reconstruct the historical Gautama apart from later tradition (unlike Confucius D1 SEP+IEP Tian path), so A/B/C/D stay BELOW_THRESHOLD with named readings only; primary stays BELOW with BUDDH lead (Ruling X2 / P42). E UNKNOWN; mid BELOW; not plotted. No fallacy_catalog; no figures/. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Audit fixes for batch X (gs_a1ff932_X run 1): (GA6) the SEP lines 'governed by the causal laws of karma', 'good actions cause pleasant fruit' and gods undergoing rebirth relocated to §1 and labelled as the Upaniṣadic and śramaṇa milieu, not his teaching; the B and C karma readings rest on the §4 line ('What the Buddha teaches is instead the far stricter view that each action has its own specific consequence ...'). Ruling X2 (v8's call on the auditor's advice): primary_system stays BELOW_THRESHOLD with BUDDH as the lead (recorded under P42). No scored value changes."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch X, order P32: F 4, rank 129). Basics from Britannica 'Buddha' (Donald S. Lopez with Britannica Editors, 1 Oct 2026; body only) and SEP 'Buddha' (Mark Siderits, rev. 2023). Nothing survives in his own hand; the discourses were not written down until several centuries after his death (both sources), so everything attributed to him is reported speech (P42 addendum, Confucius precedent). primary_system BELOW_THRESHOLD (BUDDH lead; the Founders rule names Buddha → BUDDH, RQ-X2); A, B, C, D BELOW_THRESHOLD with readings named; E UNKNOWN; mid_basin BELOW_THRESHOLD. Life dates, era and span UNKNOWN (P39). Not plotted. Draft, not reviewed."}

identity:
  id: gautama-siddhartha
  display_name: "Siddhartha Gautama"
  roster:
    canonical_name: "Siddhartha Gautama"
    rank: 129
    F: 4
    models: [Claude, DeepSeek, Gemini, Grok]
    band: "core (3–4)"
    status: core
    field: philosophy
    field_bucket: philosophy
  full_name: {value: "Siddhartha Gautama", certainty: 0.7, cites: [{source: S1, locator: "'General considerations'"}], how_known: "Britannica: clan name Gautama (Pali Gotama), given name Siddhartha (Pali Siddhattha)."}
  native_name: {value: "Siddhattha Gotama (Pali); Siddhartha Gautama (Sanskrit)", certainty: 0.7, cites: [{source: S1, locator: "'General considerations'"}], how_known: "Britannica."}
  aliases:
    - {name: "Buddha", kind: "roster alias"}
    - {name: "Siddhartha Gautama-Buddha", kind: "roster alias"}
    - {name: "Shakyamuni", kind: "title or honorific"}

basics:
  birth:
    date: {value: UNKNOWN, how_known: "Britannica: 'c. 6th–4th century bce'; SEP: dates 'thought to be approximately 560–480 BCE' until recently, many scholars now placing his death around 405 BCE; tradition has him live to 80. Wikipedia lists competing long/short chronologies (c. 563/480 vs c. 483/400). No single year reaches 0.5 (P39)."}
    place: {value: "Lumbini, near Kapilavastu", modern_name: "Lumbini, southern Nepal", polity_then: "Shakya republic, Kosala kingdom", certainty: 0.5, cites: [{source: S1, locator: "opening; 'Historical context'"}, {source: S4, locator: "infobox (Born); Birth and early life"}], how_known: "Britannica and Wikipedia EN, from tradition (his life 'is known largely through legend'); Ashoka Lumbini pillar is early attestation of the birthplace tradition, not a dated birth year."}
  death:
    date: {value: UNKNOWN, how_known: "Britannica: scholarly opinion divided between about 480 BCE and as much as a century later; SEP: c. 480 or around 405 BCE; Wikipedia: competing chronologies. No single year reaches 0.5."}
    place: {value: "Kusinara", modern_name: "Kasia / Kushinagar, Uttar Pradesh, India", polity_then: "Malla republic, Magadha kingdom", certainty: 0.5, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "infobox (Died)"}], how_known: "Britannica and Wikipedia EN, from tradition."}
  first_lasting_contribution_year: {value: UNKNOWN, how_known: "His teaching is undated, and its texts were fixed centuries later (P39)."}
  era_bucket: {value: UNKNOWN, how_known: "No dated lasting work (P39). The candidate years do not fall in one bucket: on the older chronology (c. 560–480 BCE, SEP) his adult life crosses the -500 edge; on the later one (death c. 405 BCE) it lies in '-500 to 499'."}
  region_of_birth: {value: "South Asia", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Present-day Nepal (P3)."}
  region_of_work: {value: "South Asia", certainty: 0.7, cites: [{source: S1, locator: "opening ('a teacher who lived in northern India')"}], how_known: "Northern India."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: UNKNOWN, how_known: "SEP: the texts are in languages 'other than the one he is likely to have spoken' and does not name it."}
  occupations: {value: ["wandering teacher", "ascetic (śramana)"], certainty: 0.7, cites: [{source: S2, locator: "§1"}], how_known: "SEP: he left household life and 'took up with a number of different wandering ascetics'."}

contribution:
  era_bucket: ancient
  fields: {value: ["ethics", "philosophy of mind", "soteriology"], certainty: 0.5, cites: [{source: S2, locator: "opening; §§2–3"}], how_known: "SEP: claims 'concerning the nature of persons, as well as how we acquire knowledge'; field labels the coder's."}
  lasting_original_contributions:
    - {value: "Teaching of the Four Noble Truths, non-self (anātman) and the middle path, the basis of Buddhism", year: UNKNOWN, kind: "body of work", lasting: "'the individual whose teachings form the basis of the Buddhist tradition' (S2); founder of 'one of the major religions and philosophical systems of southern and eastern Asia and of the world' (S1)", certainty: 0.7, cites: [{source: S2, locator: "opening; §2 ('Four Nobles' Truths'); §3"}, {source: S1, locator: "opening"}], how_known: "Both sources; known only through later texts (S2 §1). Undated (P39)."}
  evidence_of_impact:
    - {value: "Founder of Buddhism, one of the world's major religions and philosophical systems", kind: "institutional or technological lineage", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    - {value: "His teachings 'formed the basis of a philosophical tradition that developed and defended a variety of sophisticated theories in metaphysics and epistemology'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S2, locator: "opening"}], how_known: "SEP."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1, S2).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated in the bodies read; Britannica says only that his family 'is said to have belonged to the warrior (Kshatriya) caste'."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Family 'of some wealth and power', of the Śākya clan", role: family, certainty: 0.5, cites: [{source: S2, locator: "§1"}], how_known: "SEP, from tradition."}
  household_circumstances: {value: "Wealthy Shakya family; Britannica notes the grand palaces of the traditional accounts 'are not evident among the archaeological remains'", certainty: 0.5, cites: [{source: S2, locator: "§1"}, {source: S1, locator: "'Historical context'"}], how_known: "Both sources."}
  schooling: []
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events:
    - {value: "Left household life, wife and young son in early adulthood to seek an end to suffering", year: UNKNOWN, certainty: 0.5, cites: [{source: S2, locator: "§1 ('The story is that')"}], how_known: "SEP, hedged as a story."}

worldview:
  unit: "adult working worldview"
  working_years: {value: UNKNOWN, how_known: "Equals timing.major_work_period (UNKNOWN, P39)."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing in his own hand."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "Lead BUDDH, the tradition he founded. The Founders rule (CODING_GUIDE §1 table: 'Buddha → BUDDH') points to BUDDH, but everything attributed to him is reported speech: SEP says the texts 'were not written down until several centuries after his death, are in languages ... other than the one he is likely to have spoken, and disagree in important respects' (§1); Britannica says the earliest were 'not committed to writing until shortly before the beginning of the Common Era, several centuries after his death'. A disciples' record of sayings is reported speech (P42 addendum; v8's ruling on RQ O1, Confucius), which cannot score alone (§7). Ruling X2 (v8's call on the auditor's advice): the P42 addendum governs, so BELOW_THRESHOLD with BUDDH as the lead; the Founders rule picks the code once own-voice evidence reaches 0.5, and a founder known only through followers' records keeps the founded system as the lead (Confucius precedent). Deepen D1: SEP §1 reaffirmed; P49 not stretched to unlock BUDDH."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: BUDDH, reason: "Founder (Founders rule); nothing in his own words (P42 addendum); the lead under ruling X2."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "Reported speech only (P42 addendum). Named reading (not scored): in the Tevijja Sutta (D I.235–52) 'the Buddha rejects the claim of certain Brahmins to know the path to oneness with Brahman, on the grounds that no one has actually observed this Brahman' (S2 §3) — would lean A 3–4 (no creator person scored from observation). SEP §1 lists gods among beings that undergo rebirth as Upaniṣadic/śramaṇa milieu, not his teaching (GA6). P49 not stretched: SEP §1 declines to reconstruct historical Gautama apart from later tradition ('No position will be taken on this dispute here'), unlike the Confucius D1 SEP+IEP path for Tian."}
    B_cause: {value: BELOW_THRESHOLD, how_known: "Not a scientist. Named reading (not scored): SEP §4 'What the Buddha teaches is instead the far stricter view that each action has its own specific consequence for the agent, the hedonic nature of which is determined in accordance with causal laws' — would lean B 3–4 (lawful karma). Against it, M I.68 claims 'superhuman cognitive powers', which 'some scholars take ... to be not the Buddha's own words but an expression of later devotionalist concerns' (S2 §5). Milieu 'causal laws of karma' (S2 §1) is not his teaching (GA6). Reported speech (P42); P49 not stretched to score B."}
    C_ledger: {value: BELOW_THRESHOLD, how_known: "Named reading (not scored): karma rule P44(d) would give C 3 @0.5 alt 4 from SEP §4 impersonal consequence-by-causal-laws (no judging person). It is the reconstructed teaching of texts fixed centuries later (P42), so stays a reading; P49 not stretched."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "Named reading (not scored): Tevijja argument from non-observation (S2 §3) and attitude toward reason (S2 §5) would lean D 3–4; M I.68 superhuman cognition (disputed authenticity) pulls the other way. Reported speech (P42); P49 not stretched."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read on special exceptions in this-world events (P7, P19)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A and B both BELOW_THRESHOLD (P19)."}
  statements: []
  changes_over_life: []
  coder_notes: "Coder's call. Treated like Confucius and Hippocrates under P42: the doctrine survives only in later compilations, so nothing scores. Unlike Confucius D1 (where SEP+IEP independently reconstruct Tian for Analects Confucius under P49), SEP Buddha §1 explicitly treats later-tradition understanding and declines a separate historical-Gautama reconstruction — so P49 was labeled as considered and not stretched to score A/B/C/D (deepen brief: keep honest BELOW). Ruling X2 keeps primary BELOW with BUDDH lead. Only primary_system is result-changing in principle; A and B stay BELOW either way, so he is unplotted under both. No quotation recorded as a statement: sutta wording read only through SEP paraphrase. No fallacy_catalog; figures not refreshed."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Shakya clan; family 'said to have belonged to the warrior (Kshatriya) caste'", certainty: 0.5, cites: [{source: S1, locator: "'Historical context'"}, {source: S2, locator: "§1"}], how_known: "Both sources; Britannica hedged."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated; Britannica says it is 'unclear to what extent' the region's peoples were incorporated into the caste system."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: UNKNOWN, how_known: "No dated lasting contribution (P39)."}
  age_at_first_lasting_contribution: {value: UNKNOWN, how_known: "No dated lasting contribution (P39)."}
  first_evidence_of_lio_type_views: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S2, locator: "§1"}], how_known: "Nothing attributable (P42 addendum)."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S2, locator: "§1"}], how_known: "As above."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Nothing attributable."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Not read for this.", certainty: 0.5, cites: [{source: S2, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "text"}], how_known: "Not read."}
  circle_present: {value: "unclear", rationale: "Reported teaching only; karma-as-causal-law is a named reading under B/C, not a scored finding.", certainty: 0.5, cites: [{source: S2, locator: "§4"}], how_known: "Coder's reading."}
  reading: "Karma as impersonal causal law, in the reconstructed teaching (named lead only; P49 not stretched)."
  notes: "Lane B labeled model. Deepen D1 keeps all scored axes BELOW under X2/P42."

institutions: []
collaborators: []

review:
  roster_status_reason: {value: "Core in v8 (F 4), with the Buddha alias merged (OPEN_DECISIONS R4).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 129"}], how_known: "Study roster."}
  controversies:
    - {value: "Life dates: death c. 480 BCE or about a century later (long vs short chronologies)", certainty: 0.7, cites: [{source: S1, locator: "'General considerations'"}, {source: S2, locator: "§1"}, {source: S4, locator: "Dating"}], how_known: "Britannica, SEP, Wikipedia."}
    - {value: "Whether historical Gautama's own thought is recoverable apart from later Buddhist philosophy (SEP §1 declines; Gombrich/Shulman more sanguine)", certainty: 0.5, cites: [{source: S2, locator: "§1"}], how_known: "SEP; blocks P49 stretch this pass."}
  data_quality_flags:
    - "Life 'known largely through legend' (S1); nothing in his own hand."
    - "P49 reconstruction considered and not stretched (SEP declines historical-Gautama reconstruction)."
  open_questions:
    - "Settled by ruling X2: BELOW_THRESHOLD, BUDDH the lead."
    - "Optional unread leads: Gombrich What the Buddha Thought (2009); Rahula What the Buddha Taught — could revisit P49 only if a dual scholarly reconstruction of historical Gautama (not later tradition) appears; do not stretch from SEP alone."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Donald S. Lopez with Britannica Editors"
    citation: "Lopez, Donald S., and Britannica Editors. \"Buddha.\" Encyclopaedia Britannica (updated 1 October 2026). https://www.britannica.com/biography/Buddha-founder-of-Buddhism. Re-read live 2026-10-24."
    url: "https://www.britannica.com/biography/Buddha-founder-of-Buddhism"
    accessed: 2026-10-24
    reliability_note: "Signed article. Body only; the AI-generated Top Questions are not cited. Reaffirms: life known largely through legend; earliest texts written centuries after death."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, review]
  - id: S2
    type: tertiary
    kind: encyclopedia
    author: "Mark Siderits"
    citation: "Siderits, Mark. \"Buddha.\" Stanford Encyclopedia of Philosophy (first published 17 Feb 2011; substantive revision 6 Mar 2023). https://plato.stanford.edu/entries/buddha/. Re-read live 2026-10-24."
    url: "https://plato.stanford.edu/entries/buddha/"
    accessed: 2026-10-24
    reliability_note: "Signed SEP entry, read directly. §1: texts written centuries later; entry treats later-tradition understanding and declines a separate historical-Gautama reconstruction — warrant for not stretching P49."
    source_quality: "reference entry"
    used_for: [basics, contribution, childhood, worldview, heritage, timing, lane_b, review]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S4
    type: secondary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: '"The Buddha." Wikipedia (English). https://en.wikipedia.org/wiki/The_Buddha'
    url: "https://en.wikipedia.org/wiki/The_Buddha"
    accessed: 2026-10-24
    reliability_note: "P50 dual bio for traditional birthplace Lumbini and death place Kushinagar/Kasia (agree with Britannica S1). Dating section documents long/short chronologies — years stay UNKNOWN. Teachings section used only as leads, not for axis scores (P42/P49)."
    source_quality: "reference entry"
    used_for: [basics, review]
---
# Siddhartha Gautama

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Siddhartha Gautama, the Buddha (c. 6th–4th century BCE), founder of Buddhism [S1; S2]. Deepen D1: primary_system BELOW_THRESHOLD (BUDDH lead, Ruling X2); A–D BELOW_THRESHOLD (P42 reported speech; P49 not stretched); E UNKNOWN; mid_basin BELOW_THRESHOLD. Not plotted. Chart-moving NO.

## Life and work

Born at Lumbini, died at Kusinara/Kushinagar; teacher in northern India [S1; S4]. Life known largely through legend; nothing in his own hand [S1; S2].

## Contribution and impact

Four Noble Truths, non-self, middle path — basis of the Buddhist tradition [S2]. Texts fixed centuries later [S1; S2].

## Childhood and education

Shakya family of some wealth [S2].

## Adult working worldview

Only the tradition's record [S1; S2]. Named readings (not scored): Tevijja non-observation of Brahman (A lead); karma as impersonal causal law (B/C leads) [S2 §§3–4]. SEP declines a historical-Gautama reconstruction apart from later tradition — P49 not stretched [S2 §1]. primary BELOW with BUDDH lead (X2).

## Heritage (context only)

Shakya clan [S1].

## Timing

Undated (P39).

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Karma-as-causal-law is a named lead only [S2].

## Open questions

- RQ-X2 settled (BELOW_THRESHOLD, BUDDH the lead).
- Optional: Gombrich / Rahula if a dual scholarly reconstruction of historical Gautama (not later tradition) appears — do not stretch from SEP alone.

## Research log

- 2026-10-19: Read Britannica 'Buddha' and SEP 'Buddha'.
- 2026-10-24: Deepen D1 — re-read SEP Siderits (rev. 2023) and Britannica Lopez (1 Oct 2026); Wikipedia EN The Buddha (P50); documented named A/B/C/D leads; P49 considered and not stretched; kept honest BELOW under X2/P42. No figures/. No fallacy_catalog.
