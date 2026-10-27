---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 5
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch N)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-17
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to 19c. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-25, by: "Grok Bot", summary: "Perpetual deepen: religious_heritage_by_birth / baptism / catechism / family_religion TODO→UNKNOWN (no explicit birth denomination; refuse Danzig-Protestant invention). Chart-moving NO."}
    - {date: 2026-10-17, by: "Grok Bot", summary: "Record created (stage 3 batch N, order P32: F 4, rank 85). Basics from Britannica (Arthur Hübscher, signed; body only). Worldview from The World as Will and Idea (Haldane and Kemp translation, Gutenberg #38427 and #40868: vol. 1 §§55, 63, 68; vol. 3 ch. L) and SEP 'Arthur Schopenhauer' (Wicks, 2021). primary_system IDEAL (0.5, alt ATHE); A 4 (0.7); B 4 (0.5, alt 3: his own named exception, freedom appearing in the phenomenon in the denial of the will); C 3 (0.5, alt 4); E 3 (0.5, alt 4); mid_basin false (0.7). Plotted (faded). Draft, not reviewed."}
    - {date: 2026-10-17, by: "Grok Bot", summary: "Batch N audit fixes (#7, #8; v8's ruling on RQ1, on the auditor's advice): B 4 → 3 at 0.5, alternative 4. His own named exception, freedom appearing directly in the phenomenon in the denial of the will (§68), is a free will not bound by natural law, so the B 3 rule (CODING_GUIDE §6, P30) gives 3 as the value, as with Kant's noumenal freedom, even though §55 says nature 'admits of no exception'. C 3 now cites the §63 transmigration passage and is labelled the coder's analogy (P44(d) is a systems rule). mid_basin unchanged (false, 0.7)."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #84, F4 rank 85). Needs: corroborate B (and C/E if cheap) so faded→dark if certainty ≥0.7 corroborated. Re-verified WWR Haldane–Kemp Gutenberg #38427/#40868 (§§1, 55, 63, 68; vol. 3 ch. L Epiphilosophy); SEP Wicks 2021 (Freedom of the Will essay summary; §5.3 asceticism 'freedom struggles against nature'; atheism §4); Britannica Hübscher via Wayback 20261001181634 / 20260926092729 (will as thing-in-itself; causality/appearance; ascetic negation); Wikipedia EN (S5, P50 dual-bio). P47 source_quality on S1–S5. A 4 @0.7 labelled support corroborated (S2+S3). B 3 @0.5 single → 3 @0.7 corroborated, alt 4 (aligned with Kant / P30 #14: free will appearing in the phenomenon in denial of the will is B 3 as value; SEP corroborates phenomenal necessity + freedom-exception; named alt 4 remains the pure §55 no-exception reading). E 3 @0.5 → 3 @0.7 corroborated, alt 4 (same passages). C 3 @0.5 stays single (SEP silent on eternal justice / transmigration). primary_system IDEAL @0.5 alt ATHE unchanged (CHRIST not a candidate). mid_basin false @0.7 unchanged (A ≥ 3). Chart-moving YES: faded→dark and hollow→filled. No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: schopenhauer-arthur
  display_name: "Arthur Schopenhauer"
  roster:
    canonical_name: "Arthur Schopenhauer"
    rank: 85
    F: 4
    models: [Claude, Gemini, GPT, Grok]
    band: "core (3–4)"
    status: core
    field: philosophy
    field_bucket: philosophy
  full_name: {value: "Arthur Schopenhauer", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  native_name: {value: "Arthur Schopenhauer", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "German; same spelling."}
  aliases:
    - {name: "Arthur-Schopenhauer", kind: "roster alias"}
    - {name: "Schopenhauer-Arthur", kind: "roster alias"}

basics:
  birth:
    date: {value: "1788-02-22", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Danzig, Prussia", modern_name: "Gdańsk, Poland", polity_then: "Polish–Lithuanian Commonwealth (Crown of the Kingdom of Poland)", certainty: 0.7, cites: [{source: S1, locator: "opening; 'In 1793, when Danzig came under Prussian sovereignty'"}, {source: S5, locator: "infobox (Born)"}], how_known: "Britannica gives 'Danzig, Prussia [now Gdańsk, Poland]' but notes Prussian sovereignty only from 1793; Wikipedia infobox gives Crown of the Kingdom of Poland / Polish–Lithuanian Commonwealth at birth — polity_then follows that."}
  death:
    date: {value: "1860-09-21", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    place: {value: "Frankfurt am Main", modern_name: "Frankfurt am Main, Germany", polity_then: "Free City of Frankfurt", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica; polity_then is the coder's addition."}
  first_lasting_contribution_year: {value: 1819, certainty: 0.5, cites: [{source: S1, locator: "'Active maturity'"}], how_known: "Die Welt als Wille und Vorstellung (1819), 'his main work'; 'The book marked the summit of Schopenhauer's thought' (S1). On the Fourfold Root (1813) is dated but not marked as lasting (P13)."}
  era_bucket: {value: "1750 to 1849", certainty: 0.5, cites: [{source: S1, locator: "'Active maturity'"}], how_known: "From 1819 (P2)."}
  region_of_birth: {value: "Eastern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Poland (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "'Active maturity'; 'Scholarly retirement in Frankfurt'"}], how_known: "Dresden, Berlin, Frankfurt (Germany)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [German], certainty: 0.7, cites: [{source: S1, locator: "titles"}], how_known: "Britannica (German titles)."}
  occupations: {value: ["philosopher", "privatdozent (University of Berlin)"], certainty: 0.7, cites: [{source: S1, locator: "opening; 'Active maturity'"}], how_known: "Britannica."}

contribution:
  era_bucket: 19c
  fields: {value: ["metaphysics", "aesthetics", "ethics"], certainty: 0.7, cites: [{source: S1, locator: "'Active maturity'"}], how_known: "Britannica (the four books of the main work)."}
  lasting_original_contributions:
    - {value: "The World as Will and Idea (Die Welt als Wille und Vorstellung): the metaphysics of the will", year: 1819, kind: work, lasting: "'The book marked the summit of Schopenhauer's thought' (S1); influenced existential philosophy and Freudian psychology (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Active maturity'"}], how_known: "Britannica."}
    - {value: "Parerga und Paralipomena", year: 1851, kind: work, lasting: "'brought the beginning of worldwide recognition' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Scholarly retirement in Frankfurt'"}], how_known: "Britannica."}
  evidence_of_impact:
    - {value: "'His writings influenced later existential philosophy and Freudian psychology'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works:
    - {value: "Die Welt als Wille und Vorstellung (2nd ed. with a second volume, 1844)", year: 1819, kind: book, certainty: 0.7, cites: [{source: S1, locator: "'Active maturity'; 'Scholarly retirement in Frankfurt'"}], how_known: "Britannica."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated in sources read."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father Heinrich Floris Schopenhauer, wealthy merchant (died April 1805)", role: father, certainty: 0.7, cites: [{source: S1, locator: "'Early life and education'"}], how_known: "Britannica."}
    - {value: "Mother Johanna Schopenhauer, later a novelist and travel writer", role: mother, certainty: 0.7, cites: [{source: S1, locator: "'Early life and education'"}], how_known: "Britannica."}
  household_circumstances: {value: "Wealthy merchant family; moved from Danzig to Hamburg in 1793", certainty: 0.7, cites: [{source: S1, locator: "'Early life and education'"}], how_known: "Britannica."}
  schooling:
    - {value: "Private education, then a private business school (where he met 'a Pietistic attitude')", stage: tutor, years: UNKNOWN, certainty: 0.5, cites: [{source: S1, locator: "'Early life and education'"}], how_known: "Britannica ('a gentlemanly private education'); stage is the coder's reading."}
    - {value: "University of Göttingen (medicine, then humanities), 1809–1811; Berlin 1811–1813; PhD Jena 1813", stage: university, years: "1809–1813", certainty: 0.7, cites: [{source: S1, locator: "'Early life and education'"}], how_known: "Britannica."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure:
    - {value: "Lectures mainly on the natural sciences at Göttingen (age 21)", certainty: 0.7, cites: [{source: S1, locator: "'Early life and education'"}], how_known: "Britannica; adult, not childhood."}
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [German], certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  notable_events:
    - {value: "Death of his father, April 1805", year: 1805, age: 17, certainty: 0.7, cites: [{source: S1, locator: "'Early life and education'"}], how_known: "Britannica."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1819–1851", certainty: 0.5, cites: [{source: S1, locator: "'Active maturity'; 'Scholarly retirement in Frankfurt'"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not scored at this reading."}
  primary_system:
    value: IDEAL
    basis: written_profession
    certainty: 0.5
    cites: [{source: S2, locator: "vol. 1, §1"}, {source: S1, locator: "'Active maturity'"}]
    rationale: "The main work opens: '\"The world is my idea:\"—this is a truth which holds good for everything that lives' (S2, §1); Britannica: the world 'is only comprehensible with the aid of the constructs of man's intellect—space, time, and causality', showing it 'only as appearance' (S1). Named alternative: ATHE. He denies God (A below), but the ATHE label adds that nature is all there is, and for him the thing-in-itself, the will, lies outside the phenomenal world."
    how_known: "Published main work in a web copy of a translation (0.7 ceiling); 0.5 because an alternative is named and Britannica says the doctrine arose 'in immediate reaction against Hegelian idealism', so the IDEAL label is the coder's fit."
  secondary_system: {value: UNKNOWN, how_known: "Affinity with Vedanta and Buddhism (S1) is influence, not membership."}
  candidate_codes_considered:
    - {code: IDEAL, reason: "Transcendental idealism: the world as representation."}
    - {code: ATHE, reason: "Explicit atheism (S3), but not naturalism."}
    - {code: KANT, reason: "Builds on Kant (S1) but rejects Kant's moral theology."}
    - {code: BUDDH, reason: "Affinity only, no membership."}
  lio_axes:
    A_locus:
      value: 4
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S2, locator: "vol. 3, ch. L ('Epiphilosophy')"}, {source: S3, locator: "§4"}]
      rationale: "No God (P38): 'With the Pantheists, then, I have certainly that ἑν και παν in common, but not the παν θεος; because I do not go beyond experience' (vol. 3, ch. L), and 'the world exists, with me as with Spinoza, by its inner power and through itself' (same chapter). SEP: 'Within Schopenhauer's vision of the world as Will, there is no God to be comprehended', and his thought 'assumed an explicitly atheistic quality' from 1814 (S3)."
      how_known: "Published main work (vol. 3 of the translation = the 1844 second volume), web copy of a translation, 0.7 ceiling; SEP agrees. Independent source ids S2+S3 → corroborated (P48)."
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S2, locator: "vol. 1, §55; §68"}, {source: S3, locator: "Freedom of the Will essay summary; §5.3"}]
      rationale: "Account of nature (P6 / P16). Phenomenal necessity without exception: 'The whole content of Nature, the collective sum of its phenomena, is thus throughout necessary ... This admits of no exception: it follows from the unrestricted validity of the principle of sufficient reason' (§55). He names one exception himself, in man: the denial of the will 'by no means proceeds from suffering with the necessity of an effect from its cause, but the will remains free; for this is indeed the one point at which its freedom appears directly in the phenomenon' (§68); freedom 'contradicts the phenomenon' yet 'may yet possibly, in his case, appear in the phenomenon also' (§55). A free will not bound by natural law is the B 3 case (CODING_GUIDE §6, P30 #14), as for Kant's noumenal freedom — 3 as the value, not as an alternative. SEP corroborates: 'everything that happens, happens necessarily' / every act determined by motives (Freedom of the Will, 1839), and in denial 'freedom struggles against nature' (§5.3). Alternative 4: the pure §55 no-exception claim if §68 freedom is read as outside nature. Deepen D1 aligns certainty with Kant (named alt 4 → 0.7)."
      how_known: "Published main work (web copy of translation) plus SEP; named alternative (4), so 0.7 (Kant pattern). Independent source ids S2+S3 → corroborated (P48)."
      alternatives:
        - {value: 4, note: "§55: 'This admits of no exception' (P40), if the §68 freedom is read as outside nature.", cites: [{source: S2, locator: "vol. 1, §55"}]}
    C_ledger:
      value: 3
      basis: written_profession
      certainty: 0.5
      support: single
      cites: [{source: S2, locator: "vol. 1, §63 (eternal justice; transmigration passage)"}]
      rationale: "An impersonal moral ledger with no judge: 'eternal justice ... rules not the state but the world ... infallible, fixed, and sure'; 'The punishment must here be so bound up with the offence that both are one'; 'the world itself is the judgment of the world'. He quotes Euripides against a Zeus who records and punishes sins. In the same section he gives the myth of transmigration as the people's figurative form of this truth, 'sufficient as a guide for conduct': 'all sufferings which in life one inflicts upon other beings must be expiated in a subsequent life in this world, through precisely the same sufferings' (§63). An impersonal karma-type law with no judge reads as C 3 at 0.5, alternative 4; this is the coder's analogy (P44(d) is a rule for systems, not people). He presents the transmigration myth as figurative, not literal, which is another reason for 0.5. SEP (S3) is silent on eternal justice / transmigration this pass — stays single."
      how_known: "Published main work, web copy; scored by analogy, so 0.5. Single source id → single (P48)."
      alternatives:
        - {value: 4, note: "If 'the world itself is the judgment of the world' is read as no ledger at all rather than an impersonal one.", cites: [{source: S2, locator: "vol. 1, §63"}]}
    D_authority: {value: UNKNOWN, how_known: "Not scored at this reading; his critique of revelation in vol. 2 (ch. XVII) is a lead."}
    E_scope:
      value: 3
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S2, locator: "vol. 1, §55"}, {source: S3, locator: "§5.3"}]
      rationale: "Scored on the world's order (P7). Necessity holds for every phenomenon, but man 'is distinguished from all the other phenomena of will by the fact that freedom ... may yet possibly, in his case, appear in the phenomenon also' (§55): one kind of being has an exception in this-world events. SEP frames denial as 'freedom struggles against nature' (§5.3). Alternative 4 if that freedom is read as outside nature."
      how_known: "Published main work plus SEP; named alternative (4), so 0.7. Independent source ids S2+S3 → corroborated (P48)."
      alternatives:
        - {value: 4, note: "If §55/§68 freedom is read as outside nature / outside this-world events.", cites: [{source: S2, locator: "vol. 1, §55"}]}
  mid_basin: {value: false, certainty: 0.7, cites: [{source: S2, locator: "vol. 3, ch. L"}, {source: S3, locator: "§4"}], how_known: "A 4 at 0.7: the A ≥ 3 branch reads A only (P10)."}
  statements:
    - text: "The whole content of Nature, the collective sum of its phenomena, is thus throughout necessary, and the necessity of every part, of every phenomenon, of every event, can always be proved, because it must be possible to find the reason from which it follows as a consequent. This admits of no exception: it follows from the unrestricted validity of the principle of sufficient reason."
      cites: [{source: S2, locator: "vol. 1, §55"}]
      date: "1819"
      context: "The World as Will and Idea, Book IV, §55 (first edition 1819; Haldane and Kemp translation)."
      axes: [B_cause, E_scope]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Checked word for word against the Gutenberg text of the translation."
    - text: "In general, the denial of the will to live by no means proceeds from suffering with the necessity of an effect from its cause, but the will remains free; for this is indeed the one point at which its freedom appears directly in the phenomenon"
      cites: [{source: S2, locator: "vol. 1, §68"}]
      date: "1819"
      context: "Book IV, §68, on the saint's denial of the will."
      axes: [B_cause, E_scope]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "His own named exception; basis of the alternatives."
    - text: "What is here referred to is the myth of the transmigration of souls. It teaches that all sufferings which in life one inflicts upon other beings must be expiated in a subsequent life in this world, through precisely the same sufferings"
      cites: [{source: S2, locator: "vol. 1, §63"}]
      date: "1819"
      context: "Book IV, §63: the myth in which, he says, the truth behind eternal justice ('Tat twam asi', 'This thou art') was given to the people as a figurative substitute, 'sufficient as a guide for conduct'."
      axes: [C_ledger]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Checked word for word against the Gutenberg text of the translation (#38427)."
    - text: "the world itself is the judgment of the world"
      cites: [{source: S2, locator: "vol. 1, §63"}]
      date: "1819"
      context: "Book IV, §63, on eternal justice."
      axes: [C_ledger]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
    - text: "With the Pantheists, then, I have certainly that ἑν και παν in common, but not the παν θεος; because I do not go beyond experience (taken in its widest sense), and still less do I put myself in contradiction with the data which lie before me."
      cites: [{source: S2, locator: "vol. 3, ch. L ('Epiphilosophy')"}]
      date: "1844"
      context: "Supplements to Book IV, chapter 50, second edition (1844)."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
  changes_over_life:
    - {value: "Called himself an 'illuminated theist' in his notebooks in 1812; explicitly atheistic from about 1814", year: 1814, age: 26, certainty: 0.5, cites: [{source: S3, locator: "§4 (Manuscript Remains, vol. 2, p. 373)"}], how_known: "SEP's reconstruction; notebooks not read."}
  coder_notes: "Gutenberg is a web copy of the Haldane–Kemp translation (1883–86), so 0.7 is the ceiling for translation-only checks. Deepen D1 (2026-10-24): B reconciled as 3 @0.7 alt 4 (not the pre-audit 4 @0.5 alt 3, and not the post-audit 3 @0.5): free will appearing in the phenomenon in denial of the will is B 3 as value under P30 #14 / Kant parallel; SEP corroborates; named alt 4 is the pure §55 reading. A/B/E labelled support corroborated; C stays single. Verified_against remains 'scholarly edition' for the published translation."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "German of Dutch family origin (Danzig merchant family)", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Early life and education'"}, {source: S3, locator: "§1"}, {source: S5, locator: "Categories / Early life"}], how_known: "SEP: family of Dutch heritage; Wikipedia agrees; Britannica on Danzig merchant family."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated as childhood confession in S1–S5 / Wikipedia Early life (Danzig German merchant family; denomination not named). Refuse Lutheran-milieu invention."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "No baptism record opened."}
  childhood_catechism: {value: UNKNOWN, how_known: "No childhood catechism curriculum named."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1819–1851", certainty: 0.5, cites: [{source: S1, locator: "'Active maturity'; 'Scholarly retirement in Frankfurt'"}], how_known: "First to last listed lasting contribution (P29, P30)."}
  age_at_first_lasting_contribution: {value: 31, certainty: 0.5, cites: [{source: S1, locator: "opening; 1819"}], how_known: "1819 − 1788 = 31 (P30)."}
  first_evidence_of_lio_type_views: {value: "1819: nature necessary without exception (WWR §55)", year: 1819, certainty: 0.5, cites: [{source: S2, locator: "vol. 1, §55"}], how_known: "SEP dates explicit atheism to about 1814 (notebooks, not read)."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.7, cites: [{source: S2, locator: "vol. 1, §55; vol. 3, ch. L"}], how_known: "Stated in the main work itself (1819, 1844)."}
  worldview_during_major_work: {value: "No God; the will as thing-in-itself; phenomena necessary without exception, except freedom in the denial of the will", certainty: 0.5, cites: [{source: S2, locator: "vol. 1, §§55, 68; vol. 3, ch. L"}], how_known: "Coder's summary."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Not read for this.", certainty: 0.5, cites: [{source: S2, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "text"}], how_known: "Not read."}
  circle_present: {value: "no", rationale: "No God as source or end; the will 'with no end in view' (S3).", certainty: 0.5, cites: [{source: S3, locator: "§4"}], how_known: "Coder's reading."}
  reading: "No God; one blind will behind necessary appearances."
  notes: ""

institutions:
  - {value: "University of Berlin", role: "lecturer (privatdozent)", years: "1820–1831", kind: university, certainty: 0.5, cites: [{source: S1, locator: "'Active maturity'"}], how_known: "Britannica: qualified March 1820, 'a member of the university for 24 semesters', only his first lecture held; end year computed."}
collaborators:
  - {value: "Johann Wolfgang von Goethe", relation: "influenced by", note: "discussed philosophy with him in Weimar, 1813–14; On Vision and Colours (1816) supports Goethe against Newton", certainty: 0.7, cites: [{source: S1, locator: "'Active maturity'"}], how_known: "Britannica."}
  - {value: "G.W.F. Hegel", relation: "rival or critic", note: "scheduled his lectures against Hegel's", certainty: 0.7, cites: [{source: S1, locator: "'Active maturity'"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 85"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Main work read in a web copy of a 19th-century translation (Haldane–Kemp); German original (Löhneysen / Hübscher) not compared this pass."
    - "Essay on the Freedom of the Will (1839) used via SEP summary (S3), not a primary transcription this pass."
  open_questions:
    - "Settled for value: B 3 (alt 4) under P30 #14 / batch N RQ1 — free will in denial of the will is B 3 as value. Deepen D1 lifts certainty 0.5 → 0.7 with SEP corroboration (Kant pattern)."
    - "German original of §55, §68 and Epiphilosophy (Löhneysen or Hübscher) for wording of 'erscheint ... in der Erscheinung'."
    - "Primary text of the 1839 Prize Essay on the Freedom of the Will (SEP summary only this pass)."
    - "Secondary corroboration for C (eternal justice / transmigration) — SEP silent this pass."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Arthur Hübscher"
    citation: "Hübscher, Arthur. \"Arthur Schopenhauer.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Arthur-Schopenhauer. Read in Wayback snapshots: main page 20261001181634; 'Scholarly retirement in Frankfurt' 20260926092729."
    url: "https://www.britannica.com/biography/Arthur-Schopenhauer"
    accessed: 2026-10-24
    reliability_note: "Signed article (director, Schopenhauer Archives). Body only; Top Questions not cited for worldview. Deepen D1 re-opened Wayback copies for will / causality / asceticism."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, institutions, collaborators]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Arthur Schopenhauer"
    citation: "Schopenhauer, Arthur. The World as Will and Idea. Translated by R. B. Haldane and J. Kemp. 3 vols. London: Trübner, 1883–86. Project Gutenberg #38427 (vol. 1), #40097 (vol. 2), #40868 (vol. 3). https://www.gutenberg.org/ebooks/38427"
    url: "https://www.gutenberg.org/ebooks/38427"
    accessed: 2026-10-24
    reliability_note: "Web copy of a published translation (0.7 ceiling). Deepen D1 re-checked §1, §55, §63, §68 and vol. 3 ch. L word for word."
    source_quality: "primary / own words"
    used_for: [worldview, timing, lane_b]
  - id: S3
    type: tertiary
    kind: encyclopedia
    author: "Robert Wicks"
    citation: "Wicks, Robert. \"Arthur Schopenhauer.\" Stanford Encyclopedia of Philosophy (substantive revision 9 September 2021). https://plato.stanford.edu/entries/schopenhauer/"
    url: "https://plato.stanford.edu/entries/schopenhauer/"
    accessed: 2026-10-24
    reliability_note: "Signed SEP entry, read directly. Deepen D1 used §4 (atheism), Freedom of the Will essay summary, and §5.3 (asceticism / freedom vs nature) for B/E corroboration."
    source_quality: "reference entry"
    used_for: [worldview, heritage, lane_b]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-17
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S5
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia contributors. \"Arthur Schopenhauer.\" Wikipedia, The Free Encyclopedia. https://en.wikipedia.org/wiki/Arthur_Schopenhauer. Dual biography with S1 Britannica under P50 (frozen roster)."
    url: "https://en.wikipedia.org/wiki/Arthur_Schopenhauer"
    accessed: 2026-10-24
    reliability_note: "P50 dual-bio companion to Britannica; used for Early life / family Dutch heritage and birth polity (Polish–Lithuanian Commonwealth). Categories 'German atheists' / 'Atheist philosophers' are tags, not scored alone for A. Not used alone for worldview scores."
    source_quality: "reference entry"
    used_for: [basics, heritage]
---

# Arthur Schopenhauer

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Arthur Schopenhauer (1788–1860), German philosopher of the will [S1]. Deepen D1: primary_system IDEAL (0.5, alt ATHE); A 4 @0.7 corroborated; B 3 @0.7 corroborated (alt 4); C 3 @0.5 single (alt 4); E 3 @0.7 corroborated (alt 4); mid_basin false (0.7). Plotted (now dark filled — chart-moving).

## Life and work

Dresden, Berlin, then Frankfurt from 1833 [S1].

## Contribution and impact

The World as Will and Idea (1819), Parerga und Paralipomena (1851) [S1].

## Childhood and education

Son of a Danzig merchant and the writer Johanna Schopenhauer [S1].

## Adult working worldview

Nature's phenomena necessary without exception [S2, vol. 1, §55], save freedom appearing in the phenomenon in the denial of the will [S2, §68; S3, §5.3] — B 3 @0.7 corroborated, alt 4. No God [S2, vol. 3, ch. L; S3, §4] — A 4 @0.7 corroborated. Eternal justice / transmigration myth as figurative guide [S2, §63] — C 3 @0.5 single.

## Heritage (context only)

Danzig merchant family of Dutch origin [S1; S3; S5].

## Timing

First lasting contribution 1819, at 31 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No circle [S3].

## Open questions

- German original of §55 / §68 / Epiphilosophy; primary text of the 1839 Freedom of the Will essay; secondary for C.

## Research log

- 2026-10-17: Read Britannica (Hübscher) in Wayback copies, SEP (Wicks) and the Gutenberg translation (vols. 1 and 3) directly; quotations checked word for word.
- 2026-10-24 (D1): Re-verified WWR §§1, 55, 63, 68 and vol. 3 ch. L (Gutenberg); SEP Freedom essay + §5.3 + atheism §4; Britannica Wayback; Wikipedia EN (S5, P50). P47 on S1–S5. A/B/E support corroborated; B and E certainty 0.5 → 0.7 (Kant / P30 #14 pattern); C stays single @0.5. Chart-moving YES (faded→dark, hollow→filled).
