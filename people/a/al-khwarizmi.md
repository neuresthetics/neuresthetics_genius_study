---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch C)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-08
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to mathematics. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-08, by: "Grok Bot", summary: "Record created (stage 3 batch C, order P32). Basics from MacTutor and Britannica (editors); worldview from the Author's Preface of the Algebra in Rosen's 1831 translation (archive.org scan, pp. 1–4), with Rosen's own doubt about the preface noted. Works dated only 'after 813', so first-lasting year, span and age UNKNOWN (P12). primary_system ISLAM 0.7 (written_profession; alternative BELOW_THRESHOLD as a conventional formula); A_locus 0 (0.7); C_ledger 1 (0.5); B BELOW_THRESHOLD (coder's call); D BELOW_THRESHOLD; E UNKNOWN; mid_basin BELOW_THRESHOLD. Draft, not reviewed."}
    - {date: 2026-10-08, by: "Grok Bot", summary: "Lens audit of batch C (dd91009), run 1: #11 A_locus 0 certainty 0.7 → 0.5 (the p. 4 line follows Q 9:129). #12 C_ledger 1 at 0.5 re-anchored on pp. 3–4 (mercy through others' prayers), with p. 1 marked contested (Notes, pp. 175–176); p. 3–4 statement added. Statements: verified_against 'primary facsimile' → 'scholarly edition'; copyist's frame and the 1342 manuscript date added to the p. 1 context. mid_basin unchanged (BELOW_THRESHOLD)."}

    - {date: 2026-10-23, by: "Grok Bot", summary: "Deepen pass D1 (queue #4). P47 source_quality on every source. Re-read MacTutor; added S5 Biographical Encyclopedia of Astronomers (Brentjes 2007) and S6 Rashed French Algebra preface (hist-math.fr). A_locus 0: support single → corroborated (S3+S1 Toomer+S6 cross-check); certainty stays 0.5 (Q 9:129 formula). B_cause BELOW_THRESHOLD → 3 @ 0.5 inference_from_work corroborated (S1+S5; P30/P35; Kepler precedent that astrological tables do not block B from mathematical astronomy). C_ledger 1 @ 0.5 → BELOW_THRESHOLD (Rosen mercy-through-prayers reading not supported by modern French preface). E UNKNOWN → BELOW_THRESHOLD (scientist, no statement; P19). mid_basin still BELOW_THRESHOLD (A and B at 0.5). Chart: unplotted → faded filled. Native name filled. No fallacy_catalog (Jason 2026-10-23). Draft, not reviewed."}

identity:
  id: al-khwarizmi
  display_name: "Al-Khwarizmi"
  roster:
    canonical_name: "Al-Khwarizmi"
    rank: 4
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: mathematics
    field_bucket: mathematics
  full_name: {value: "Abu Jaʿfar Muḥammad ibn Mūsā al-Khwārizmī", certainty: 0.7, cites: [{source: S1, locator: "heading ('Abu Ja'far Muhammad ibn Musa Al-Khwarizmi')"}, {source: S2, locator: "In full ('Muḥammad ibn Mūsā al-Khwārizmī')"}], how_known: "Two sources; the kunya Abu Jaʿfar is MacTutor's alone."}
  native_name: {value: "Abū Jaʿfar Muḥammad ibn Mūsā al-Khwārizmī", certainty: 0.7, cites: [{source: S1, locator: "heading"}, {source: S2, locator: "In full"}], how_known: "Transliterated Arabic matching the scored full_name (MacTutor + Britannica); same pattern as al-Ghazali / al-Razi."}
  aliases:
    - {name: "Muhammad ibn Musa al-Khwarizmi", kind: "roster alias"}
    - {name: "Algoritmi", kind: latinized}
    - {name: "Mohammed ben Musa", kind: transliteration}

basics:
  birth:
    date:
      value: "780"
      approx: true
      certainty: 0.5
      cites: [{source: S1, locator: "Quick Info ('about 780')"}, {source: S2, locator: "Born line ('c. 780')"}]
      how_known: "Both sources give an approximate year; approximate, so 0.5."
    place:
      value: "possibly Baghdad"
      modern_name: "Baghdad, Iraq"
      polity_then: "Abbasid Caliphate"
      certainty: 0.5
      cites: [{source: S1, locator: "Quick Info ('possibly Baghdad'); Biography, paragraph 1"}]
      how_known: "MacTutor hedges ('possibly'); Toomer, quoted there, suggests the name may point to Khwarizm, or to forebears from there, with the epithet al-Qutrubbulli pointing to a district near Baghdad. 0.5."
      alternatives:
        - {value: "Khwarizm, south of the Aral Sea", cites: [{source: S1, locator: "Biography, paragraph 1 (Toomer)"}], note: "From the name al-Khwarizmi."}
  death:
    date: {value: "850", approx: true, certainty: 0.5, cites: [{source: S1, locator: "Quick Info ('about 850')"}, {source: S2, locator: "Died line ('c. 850')"}], how_known: "Approximate in both sources, so 0.5."}
    place: {value: UNKNOWN, how_known: "Neither source gives a place of death."}
  first_lasting_contribution_year: {value: UNKNOWN, how_known: "The Algebra and the astronomical tables are dedicated to the caliph al-Ma'mun, who ruled from 813 (S1), so both are after 813; no source read gives a year (P12: undated items do not set the year)."}
  era_bucket: {value: "500 to 1399", certainty: 1.0, cites: [{source: S1, locator: "Biography (al-Ma'mun from 813)"}, {source: S2, locator: "opening (c. 780–c. 850)"}], how_known: "Any year between 813 and his death about 850 gives the same bucket (P2)."}
  region_of_birth:
    value: "Middle East and North Africa"
    certainty: 0.5
    cites: [{source: S1, locator: "Quick Info ('possibly Baghdad (now in Iraq)')"}]
    how_known: "Iraq is Middle East and North Africa in regions.csv (P3). The birthplace itself is uncertain, so 0.5."
    alternatives:
      - {value: "Central Asia", cites: [{source: S1, locator: "Biography, paragraph 1 (Khwarizm 'in central Asia')"}], note: "If born in Khwarizm (modern Uzbekistan/Turkmenistan)."}
  region_of_work: {value: "Middle East and North Africa", certainty: 1.0, cites: [{source: S1, locator: "Biography (House of Wisdom, Baghdad)"}, {source: S2, locator: "paragraph 2 ('lived in Baghdad')"}], how_known: "Two sources."}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S1, locator: "throughout"}, {source: S2, locator: "throughout"}], how_known: "As the sources record it."}
  languages_of_work: {value: [Arabic], certainty: 1.0, cites: [{source: S1, locator: "Biography ('wrote in Arabic')"}, {source: S2, locator: "paragraph 2 (Arabic title)"}], how_known: "Two sources."}
  occupations: {value: ["mathematician", "astronomer", "geographer", "scholar at the House of Wisdom"], certainty: 1.0, cites: [{source: S1, locator: "Biography"}, {source: S2, locator: "opening; paragraph 2"}], how_known: "Two sources."}

contribution:
  primary_domain: mathematics
  fields: {value: ["algebra", "arithmetic", "astronomy", "geography"], certainty: 1.0, cites: [{source: S1, locator: "Summary; Biography"}, {source: S2, locator: "Top Questions; paragraphs 2–4"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Al-Kitāb al-mukhtaṣar fī ḥisāb al-jabr waʾl-muqābala: systematic, demonstrative rules for solving linear and quadratic equations", year: "after 813", kind: work, lasting: "the word 'algebra'; Latin translation in the 12th century; 'the first book to be written on algebra' (S1)", certainty: 1.0, cites: [{source: S1, locator: "Biography (algebra paragraphs)"}, {source: S2, locator: "paragraph 2"}, {source: S3, locator: "Author's Preface, pp. 1–4"}], how_known: "Three sources; dated only by the dedication to al-Ma'mun (caliph from 813)."}
    - {value: "Treatise on Hindu-Arabic numerals and their arithmetic (Algoritmi de numero Indorum)", kind: work, lasting: "introduced Hindu-Arabic numerals to the West; the word 'algorithm'", certainty: 1.0, cites: [{source: S1, locator: "Summary; Biography"}, {source: S2, locator: "paragraph 3"}], how_known: "Two sources; undated."}
    - {value: "Astronomical tables (Sindhind zij), including tables of sines and tangents", kind: "body of work", lasting: "translated into Latin by Adelard of Bath from al-Majriti's revision (S1)", certainty: 1.0, cites: [{source: S1, locator: "Biography (Sindhind zij)"}, {source: S2, locator: "paragraph 4"}], how_known: "Two sources; dated only by the dedication to al-Ma'mun (S1)."}
  evidence_of_impact:
    - {value: "The words 'algebra' and 'algorithm' derive from his book title and his name", kind: "named after them", certainty: 1.0, cites: [{source: S1, locator: "Summary"}, {source: S2, locator: "opening"}], how_known: "Two sources."}
  major_works:
    - {value: "Al-Kitāb al-mukhtaṣar fī ḥisāb al-jabr waʾl-muqābala", kind: book, certainty: 1.0, cites: [{source: S2, locator: "paragraph 2"}, {source: S3, locator: "title page"}], how_known: "Two sources."}
    - {value: "Geography giving latitudes and longitudes for 2402 localities", kind: book, certainty: 0.7, cites: [{source: S1, locator: "Biography (geography)"}], how_known: "MacTutor alone."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Author of the first systematic algebra and the vehicle of Hindu-Arabic numerals to Europe.", certainty: 1.0, cites: [{source: S1, locator: "Summary"}, {source: S2, locator: "opening"}], how_known: "Two sources."}

childhood:
  family_religion:
    value: BELOW_THRESHOLD
    note: "Toomer reads al-Tabari's epithet 'al-Majusi' as meaning that his forebears, and perhaps he in his youth, were Zoroastrians; Rashed says the epithet belongs to a second person, the word 'and' having dropped out of an early copy (S1). Draft judgment (one line): too disputed to score."
    how_known: "BELOW_THRESHOLD under P19: evidence exists but is disputed."
  family_religious_practice: {value: UNKNOWN, how_known: "Not in the sources read."}
  parents_and_household: []
  household_circumstances: {value: UNKNOWN, how_known: "Not in the sources read."}
  schooling: []
  early_mathematics: {value: UNKNOWN, how_known: "Not in the sources read."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not in the sources read."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not in the sources read."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: UNKNOWN, how_known: "Equals timing.major_work_period, which is UNKNOWN because no lasting work is dated (P12, P29)."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "The preface praises God and the caliph's 'fondness for science, by which God has distinguished' him (S3, p. 3), but says nothing on how science and religion relate."}
  primary_system:
    value: ISLAM
    basis: written_profession
    certainty: 0.7
    cites: [{source: S3, locator: "Author's Preface, pp. 1–2, 4"}, {source: S1, locator: "Biography, paragraph 1 (Toomer: 'an orthodox Muslim')"}]
    how_known: "His own published preface: praise of God who 'sent Mohammed ... with the mission of a prophet', 'besides whom there is no God', blessing on 'Mohammed the Prophet and on his descendants' (S3, pp. 1–2). A named alternative, so 0.7."
    rationale: "Draft judgment (one line): ISLAM at 0.7. Named alternative: BELOW_THRESHOLD, because a pious opening was a conventional formula for a book dedicated to the caliph and says little about his working metaphysics. Toomer reads it as showing 'an orthodox Muslim' (S1)."
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: ISLAM, reason: "Coded at 0.7 on the preface (S3, pp. 1–4). Against: possibly a conventional formula.", cites: [{source: S3, locator: "pp. 1–4"}]}
    - {code: ZORO, reason: "Rejected: rests on the epithet 'al-Majusi', which Toomer applies only to his forebears and Rashed to another person (S1).", cites: [{source: S1, locator: "Biography, paragraph 1"}]}
  lio_axes:
    A_locus:
      value: 0
      basis: written_profession
      certainty: 0.5
      support: corroborated
      cites: [{source: S3, locator: "Author's Preface, pp. 1–2, 4"}, {source: S6, locator: "French preface close ('Seigneur du Trône Sublime')"}, {source: S1, locator: "Biography, paragraph 1 (Toomer: 'orthodox Muslim' from the pious preface)"}]
      how_known: "His own Algebra preface (Rosen 1831, re-checked; Rashed French critical text agrees on the Throne closing). The p. 4 line follows the stock Qur'anic closing of Q 9:129, so the formula, not a developed locus doctrine, carries the score; held at 0.5 (lens audit of batch C, #11). Toomer (via S1) independently treats the preface as showing an orthodox Muslim, corroborating that the devotion is not empty boilerplate for scoring purposes (P48)."
      rationale: "Draft judgment (one line): God is the transcendent Lord who sends prophets: 'My confidence rests with God, in this as in every thing, and in Him I put my trust. He is the Lord of the Sublime Throne' (S3 p. 4; S6 French: 'Lui le Seigneur du Trône Sublime'). Named alternative: 1, since a short dedicatory formula need not express a full doctrine of transcendence."
    B_cause:
      value: 3
      basis: inference_from_work
      certainty: 0.5
      support: corroborated
      cites: [{source: S1, locator: "Biography (Sindhind zij: true positions of sun, moon and planets; calendars; eclipses)"}, {source: S5, locator: "throughout (Zīj al-Sindhind; mean motions, equations, ecliptic)"}]
      how_known: "Scientist under P30: the Sindhind zij is a listed lasting result on celestial motions (S1; S5 Brentjes). No statement of his own on law and exception, so B 3 at 0.5 with alternative 4, never 4 (P24, P35). Earlier BELOW_THRESHOLD coder's call (astrology/horoscopes in MacTutor) reversed on deepen: Kepler's record scores B from mathematical astronomy while listing astrology as an occupation; MacTutor's 'astrological tables' sit beside eclipse and planetary-position tables as applications of the same zij, and do not by themselves show that working science covers only part of B (P19)."
      rationale: "Draft judgment (one line): working mathematical astronomy — calculating true positions of sun, moon and planets, calendars, parallax and eclipses (S1; S5) — implies a lawful celestial order with no stated exception in what was read, so B 3 at 0.5. Named alternative: 4 (P35: working science cannot tell lawful-with-exceptions from exceptionless); also BELOW_THRESHOLD if a later primary read of the zij or the political-history horoscopes shows special causal channels that displace natural regularity."
      alternatives:
        - {value: 4, note: "P35 default alternative for inference_from_work.", cites: [{source: S1, locator: "Sindhind zij"}, {source: S5, locator: "Zīj al-Sindhind"}]}
    C_ledger: {value: BELOW_THRESHOLD, note: "Lens audit had scored C 1 at 0.5 on Rosen's 'through their prayers the excellence of the Divine mercy' (pp. 3–4). The modern French critical preface (S6) has a different sense at the same place: hoping men of letters grant the book its place 'grâce aux bienfaits de Dieu très haut' (by God's benefits), with no prayer-intercession clause. Rosen himself already doubted p. 1 (Notes, pp. 175–176). Draft judgment (one line): translation-dependent and contested; not scored.", how_known: "BELOW_THRESHOLD under P19 (contested translation; deepen 2026-10-23)."}
    D_authority: {value: BELOW_THRESHOLD, note: "The preface affirms prophecy ('He sent Mohammed ... with the mission of a prophet ... when the true way of life was sought for in vain', p. 1) but says nothing on revelation against reason or observation. Draft judgment (one line): too indirect to score.", how_known: "BELOW_THRESHOLD under P19."}
    E_scope: {value: BELOW_THRESHOLD, note: "Scientist under P30; working science bears on E's first question but E is not scored from working science alone (P19). No statement of his own on one world / one order.", how_known: "BELOW_THRESHOLD under P19 (scientist, no statement; deepen 2026-10-23). Was UNKNOWN."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus 0 ≤ 1 and B_cause 3 ≥ 3 would pass P4, but both are only at 0.5, under the test's 0.7 bar (§6, P19)."}
  statements:
    - text: "Praised be God for his bounty towards those who deserve it by their virtuous acts: in performing which, as by him prescribed to his adoring creatures, we express our thanks, and render ourselves worthy of the continuance (of his mercy), and preserve ourselves from change: acknowledging his might, bending before his power, and revering his greatness ! He sent Mohammed (on whom may the blessing of God repose !) with the mission of a prophet, long after any messenger from above had appeared, when justice had fallen into neglect, and when the true way of life was sought for in vain."
      cites: [{source: S3, locator: "Author's Preface, p. 1"}]
      context: "Opening of the Algebra, dedicated to the caliph al-Ma'mun. The page opens with the copyist's frame ('In the Name of God, gracious and merciful! This work was written by Mohammed ben Musa, of Khowarezm. He commences it thus:'); Rosen's text is the single manuscript Bodleian Hunt. 214, transcribed A.H. 743 / A.D. 1342 (p. xiii). Rosen doubts his reading of lines 2–5 (the bounty and virtuous-acts clause; Notes, pp. 175–176) and prints Shakespear's alternative rendering there; the lines on Mohammed are not among those he doubts."
      axes: [A_locus, C_ledger, D_authority]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-08
      note: "Rosen's edited translation (1831), read on the archive.org scan, not the Arabic; translator's doubt noted. C_ledger rests on pp. 3–4, not on this passage (contested)."
    - text: "My confidence rests with God, in this as in every thing, and in Him I put my trust. He is the Lord of the Sublime Throne. May His blessing descend upon all the prophets and heavenly messengers !"
      cites: [{source: S3, locator: "Author's Preface, p. 4"}]
      context: "Close of the preface."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-23
      note: "Rosen's translation; re-checked on archive.org OCR 2026-10-23. Wording follows Q 9:129. French critical text (S6) agrees on sense."
    - text: "relying on the goodness of my intention therein, and hoping that the learned will reward it, by obtaining (for me) through their prayers the excellence of the Divine mercy: in requital of which, may the choicest blessings and the abundant bounty of God be theirs !"
      cites: [{source: S3, locator: "Author's Preface, pp. 3–4"}]
      context: "End of the dedication, just before the closing line of the preface; the page turns inside 'good-ness'."
      axes: [C_ledger]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-08
      note: "Rosen 1831. Deepen 2026-10-23: modern French critical preface (S6) does not support this prayer-intercession sense; C demoted to BELOW_THRESHOLD. Kept as a contested Rosen reading."
    - text: "C'est de Dieu que me vient le succès en cela et en toutes autres choses. C'est à Lui que je m'en remets, Lui le Seigneur du Trône Sublime."
      cites: [{source: S6, locator: "French Algebra preface close (hist-math.fr text)"}]
      context: "Close of the author's preface in the modern French critical text of the Algebra."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-23
      note: "Rashed-tradition French text; agrees with Rosen p. 4 on the Throne closing (A). Undated (after 813)."
  changes_over_life: []
  coder_notes: "Deepen 2026-10-23: B now scored from the zij as working science (P30/P35), corroborated by MacTutor and Brentjes BEA; Algebra still not used for B (calculation, not nature). A stays 0.5 (Q 9:129 formula) but support is now corroborated (Rosen + Toomer + French Throne line). C dropped: Rosen's mercy-through-prayers line fails against the modern French preface. E set to BELOW_THRESHOLD for a scientist with no statement (P19). mid_basin still blocked by the 0.7 bar. Childhood still empty (sources: little known)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage:
    value: "Possibly of Khwarazmian (and possibly Zoroastrian) forebears; disputed"
    certainty: 0.5
    cites: [{source: S1, locator: "Biography, paragraph 1 (Toomer; Rashed)"}]
    how_known: "Toomer's reading of the name and the epithets; Rashed rejects the Zoroastrian inference."
  religious_heritage_by_birth: {value: BELOW_THRESHOLD, note: "See childhood.family_religion: Toomer's Zoroastrian reading vs Rashed.", how_known: "BELOW_THRESHOLD under P19."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not in the sources read."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not in the sources read."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: UNKNOWN, how_known: "Works dated only as after 813 (P12, P29)."}
  age_at_first_lasting_contribution: {value: UNKNOWN, how_known: "First-lasting year UNKNOWN (P12)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No statement of his scored at 3 or 4 (P27)."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", rationale: "The only worldview text read is the preface, which scores at the low end.", certainty: 0.5, cites: [{source: S3, locator: "pp. 1–4"}], how_known: "Absence in what was read."}
  worldview_during_major_work: {value: "Muslim devotional language in the preface of the Algebra", certainty: 0.7, cites: [{source: S3, locator: "pp. 1–4"}], how_known: "His own preface, in translation."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "The Algebra gives rules 'together with demonstrations' from 'intuitive geometric arguments' (S2), not axiomatic proof.", certainty: 0.5, cites: [{source: S2, locator: "paragraph 2"}], how_known: "Coder's reading of Britannica."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "Biography, paragraph 1"}], how_known: "Nothing known of his education."}
  circle_present: {value: "no", rationale: "The preface places God as transcendent Lord; B from working astronomy is not a stated God–nature link.", certainty: 0.5, cites: [{source: S3, locator: "pp. 1–4"}, {source: S1, locator: "Sindhind zij"}], how_known: "Coder's reading."}
  reading: "As belief, not finding: form partly, circle absent; A 0 and B 3 both only at 0.5, so no mid-basin / LIO-type pass."
  notes: ""

institutions:
  - {value: "House of Wisdom (Bayt al-Ḥikma), Baghdad", role: scholar, kind: "research institute", certainty: 1.0, cites: [{source: S1, locator: "Biography"}, {source: S2, locator: "paragraph 2"}], how_known: "Two sources."}
  - {value: "Caliph al-Ma'mun", role: "patron; dedicatee of the Algebra and the astronomy", years: "813–", kind: "patron or funder", certainty: 1.0, cites: [{source: S1, locator: "Biography"}, {source: S3, locator: "Author's Preface, p. 3"}], how_known: "MacTutor and his own preface."}
collaborators:
  - {value: "Banu Musa", relation: collaborator, note: "colleagues at the House of Wisdom", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor alone."}
  - {value: "Ptolemy (ptolemy)", relation: "influenced by", note: "the Geography and, probably, the tables in Theon's revision", certainty: 0.7, cites: [{source: S1, locator: "Biography (astronomy; geography)"}], how_known: "MacTutor alone, quoting Toomer ('highly likely')."}

review:
  roster_status_reason: {value: "Core in v8 (F 5: Claude, DeepSeek, Gemini, GPT, Grok).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 4"}], how_known: "Study roster."}
  controversies:
    - {value: "Whether al-Tabari's epithet 'al-Majusi' (Zoroastrian) belongs to him (Toomer) or to a second person (Rashed)", certainty: 0.7, cites: [{source: S1, locator: "Biography, paragraph 1"}], how_known: "MacTutor reports both."}
  data_quality_flags:
    - "MacTutor's page title gives 790–850 while its Quick Info gives about 780; Britannica gives c. 780."
    - "Rosen (1831) doubts his own translation of the preface (Notes, p. 175); modern French preface (S6) diverges on the C-critical dedication clause."
    - "Chart-moving this pass: newly plotted; point_cues None → ('faded','filled'); B BELOW→3 @0.5; A support single→corroborated."
    - "Britannica re-fetch blocked/timed out 2026-10-23; prior S2 facts retained."
  open_questions:
    - "Rashed 2009 English (Saqi) full preface for a published English critical text of C/A."
    - "Primary Latin/Hebrew zij (Neugebauer / Adelard tradition) for any B statement beyond inference_from_work."
    - "Any dating firmer than 'after 813' for Algebra / zij (P12)."


sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "J. J. O'Connor and E. F. Robertson"
    citation: "O'Connor, J. J., and E. F. Robertson. \"Abu Ja'far Muhammad ibn Musa Al-Khwarizmi.\" MacTutor History of Mathematics, University of St Andrews. https://mathshistory.st-andrews.ac.uk/Biographies/Al-Khwarizmi/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Al-Khwarizmi/"
    accessed: 2026-10-23
    source_quality: "reference entry"
    reliability_note: "Standard reference biography; quotes Toomer (DSB) and Rashed. Re-read 2026-10-23 for deepen (zij topics; orthodox-Muslim preface note)."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: tertiary
    kind: encyclopedia
    author: "Britannica Editors"
    citation: "Britannica Editors. \"al-Khwārizmī.\" Encyclopaedia Britannica. https://www.britannica.com/biography/al-Khwarizmi."
    url: "https://www.britannica.com/biography/al-Khwarizmi"
    accessed: 2026-10-08
    source_quality: "reference entry"
    reliability_note: "Unsigned editors' article; whole article read 2026-10-08. Re-fetch timed out / blocked 2026-10-23; prior facts retained."
    used_for: [identity, basics, contribution, lane_b, institutions]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "Muhammad ibn Musa al-Khwarizmi; tr. Frederic Rosen"
    year: 1831
    citation: "Mohammed ben Musa. The Algebra of Mohammed ben Musa. Edited and translated by Frederic Rosen. London: Oriental Translation Fund, 1831. Scan: archive.org, algebraofmohamme00khuwuoft."
    url: "https://archive.org/details/algebraofmohamme00khuwuoft"
    accessed: 2026-10-23
    source_quality: "primary / own words"
    reliability_note: "Arabic text with English translation; Author's Preface (pp. 1–4) and Notes (pp. 175–176) re-checked on archive.org OCR 2026-10-23. Translator's doubt about parts of the preface noted; C-critical clause contested by S6."
    used_for: [identity, contribution, worldview, timing, lane_b, institutions]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-08
    source_quality: "study roster"
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
  - id: S5
    type: secondary
    kind: encyclopedia
    author: "Sonja Brentjes"
    year: 2007
    citation: "Brentjes, Sonja. \"al-Khwārizmī (Muḥammad ibn Mūsā).\" In Biographical Encyclopedia of Astronomers, edited by Thomas Hockey et al. Springer, 2007. PDF via MacTutor: https://mathshistory.st-andrews.ac.uk/BEA/al_khwarizmi_bea.pdf."
    url: "https://mathshistory.st-andrews.ac.uk/BEA/al_khwarizmi_bea.pdf"
    accessed: 2026-10-23
    source_quality: "reference entry"
    reliability_note: "Peer-reviewed encyclopedia article on his astronomy (Zīj al-Sindhind contents, transmission, Indian/Sasanian/Ptolemaic mix). Used for B corroboration."
    used_for: [contribution, worldview, basics]
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "Muhammad ibn Musa al-Khwarizmi; French critical text (Rashed tradition)"
    year: 2009
    citation: "al-Khwārizmī. Livre d'algèbre et d'al-muqābala (French critical text of the Algebra preface and body). Posted as hist-math.fr/textes/alKhwarizmi830_Algebre.pdf (file metadata 2009; page headers 'AL-KHWĀRIZMĪ : LIVRE D'ALGÈBRE'; manuscript sigla). Same project family as Roshdi Rashed, Al-Khwārizmī: The Beginnings of Algebra (London: Saqi, 2009)."
    url: "https://www.hist-math.fr/textes/alKhwarizmi830_Algebre.pdf"
    accessed: 2026-10-23
    source_quality: "primary / own words"
    reliability_note: "Modern French critical text of the Algebra. Preface checked 2026-10-23: Throne closing agrees with Rosen (A); dedication clause does not support Rosen's prayer-intercession reading (C). Full English Rashed 2009 Saqi volume not obtained this pass."
    used_for: [worldview]

---

# Al-Khwarizmi

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Al-Khwarizmi (c. 780–c. 850), scholar at the House of Wisdom in Baghdad under al-Ma'mun, wrote the first systematic algebra, a treatise that carried Hindu-Arabic numerals to Europe, and the Sindhind zij [S1; S2; S5]. Worldview text: Algebra preface [S3; S6]. Draft: ISLAM 0.7; A 0 (0.5, corroborated); B 3 (0.5, corroborated, inference_from_work); C BELOW_THRESHOLD; D BELOW_THRESHOLD; E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Chart person-dot: faded filled (was unplotted).

## Life and work

Little is known [S1]. Worked in Baghdad after 813 [S1; S2].

## Contribution and impact

Algebra; Hindu-Arabic numerals; zij; geography [S1; S2].

## Childhood and education

Not known; Zoroastrian forebears disputed [S1].

## Adult working worldview

Muslim dedicatory preface [S3; S6]; A 0 at 0.5. B 3 at 0.5 from zij working science [S1; S5], not from the Algebra. C dropped on modern preface check.

## Heritage (context only)

Disputed [S1].

## Timing

Works after 813, undated; timing UNKNOWN.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form partly; circle absent [S2; S3].

## Open questions

- Rashed 2009 English (Saqi) full preface.
- Primary zij text for any B statement beyond inference_from_work.
- Firmer dating than after 813.

## Research log

- 2026-10-08: Read MacTutor, Britannica (editors) and Rosen 1831 (preface and notes, archive.org OCR).
- 2026-10-23: Deepen D1 (queue #4). Re-read MacTutor; Brentjes BEA 2007; Rashed-tradition French Algebra preface (hist-math.fr); Rosen OCR re-check. Britannica re-fetch failed. P47 labels. No fallacy_catalog (Jason 2026-10-23).
