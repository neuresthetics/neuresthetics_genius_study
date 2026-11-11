---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z4)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to ancient. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen D1 (queue #145, F 3, rank 150). Primary-check beyond New Advent web copy: NPNF 1st ser. vol. 2 Dods City of God via IA OCR (S4) confirms XXI.8 (Creator's will = nature of each created thing; portent not contrary to nature but to what we know as nature; 'laws so sure and inflexible' yet God alters a star's course / Joshua's sun) and XXII.8 ('even now miracles are wrought in the name of Christ'). Latin De civitate Dei XXI.8 / XXII.8 via Wikisource Latin (S5) corroborates independently ('uoluntas tanti … conditoris conditae rei cuiusque natura sit'; 'Portentum ergo fit non contra naturam, sed contra quam est nota natura'; 'Nam etiam nunc fiunt miracula in eius nomine…'). Confessions XII.7 creatio ex nihilo via NPNF vol. 1 IA OCR (S6). B 2 lifted 0.5→0.7 (written_profession; support corroborated S4+S5; contested alt 1 caps ≤0.7); A 0 stays 0.7 support corroborated (S4+S5+S6); primary CHRIST @0.7 kept. mid_basin BELOW→TODO (A≤1 with B=2 both ≥0.7 falls between P4 branches — not true; true needs B≥3). Chart-moving YES: faded→dark (min cert 0.7); hollow→filled (A and B both corroborated). P47 source_quality on S1–S6. Not a scientist. No figures/; no fallacy_catalog. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z4 audit fixes (blind audit /workspace/genius_study_audit/gs_a19c474_Z4/run1/): Z4-33 (FAIL): span start is the range's start year (P12, addendum d), so 396–426 at 0.5 and age 42 (was 400, 46). RQ-Z4-2: B 2 upheld; B rationale now cites the XXI.8 'laws so sure and inflexible' sentence. Still plotted."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z4, order P32: F 3, rank 150). Basics from SEP (Christian Tornau, 2019, rev. 2024). Own words from City of God in Marcus Dods' translation (NPNF 1st ser. vol. 2) as reproduced on New Advent: XXI.8 (a portent 'happens not contrary to nature, but contrary to what we know as nature'; 'the will of so mighty a Creator is certainly the nature of each created thing') and XXII.8 ('even now miracles are wrought in the name of Christ'). Web copy of a translation, secondary quotation (Ibn Khaldun precedent). Not a scientist. Span 400–426 (Confessions ca. 396–400, latest year per P30 #4; City of God 412–426). primary_system CHRIST (0.7); A 0 (0.7, alt 1); B 2 (0.5, alt 1); C, E UNKNOWN; D BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Plotted (faded), left of B 3. Draft, not reviewed."}

identity:
  id: augustine-of-hippo
  display_name: "Augustine of Hippo"
  roster:
    canonical_name: "Augustine of Hippo"
    rank: 150
    F: 3
    models: [Claude, DeepSeek, Grok]
    band: "core (3–4)"
    status: core
    field: philosophy
    field_bucket: philosophy
  full_name: {value: "Aurelius Augustinus", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Conventional Latin name; 'Aurelius' not in the section read, so 0.5."}
  native_name: {value: "Augustinus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}
  aliases:
    - {name: "Saint Augustine", kind: "title or honorific"}

basics:
  birth:
    date: {value: "0354-11-13", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP: 13 November 354."}
    place: {value: "Thagaste, Numidia", modern_name: "Souk Ahras, Algeria", polity_then: "Roman Empire", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP."}
  death:
    date: {value: "0430-08-28", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP."}
    place: {value: "Hippo Regius", modern_name: "Annaba, Algeria", polity_then: "Roman Empire", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP (bishop of Hippo; died during the Vandal siege)."}
  first_lasting_contribution_year: {value: 396, certainty: 0.5, cites: [{source: S1, locator: "§2 Works ('Confessiones (ca. 396–400)')"}], how_known: "Confessions dated ca. 396–400; a range's start year starts the span (P12, addendum d); range, so 0.5."}
  era_bucket: {value: "-500 to 499", certainty: 1.0, cites: [{source: S1, locator: "§2 Works"}], how_known: "396 (P2)."}
  region_of_birth: {value: "Middle East and North Africa", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "Algeria (P3; regions.csv)."}
  region_of_work: {value: "Middle East and North Africa", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "Hippo, bishop c. 396–430, covers the span."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Latin"], certainty: 0.7, cites: [{source: S1, locator: "§2 Works"}], how_known: "Latin titles."}
  occupations: {value: ["rhetor", "priest", "bishop of Hippo", "philosopher", "theologian"], certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP."}

contribution:
  era_bucket: ancient
  fields: {value: ["philosophy", "theology"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}
  lasting_original_contributions:
    - {value: "Confessiones", year: 396, kind: work, lasting: "'probably his most original work'; 'greatly influenced the modern tradition of autobiography' (S1)", certainty: 0.5, cites: [{source: S1, locator: "opening; §2 Works"}], how_known: "SEP; dated ca. 396–400."}
    - {value: "De civitate dei", year: 426, kind: work, lasting: "one of the 'five long treatises' of wide scope (S1)", certainty: 0.7, cites: [{source: S1, locator: "§2 Works"}], how_known: "SEP: 412–426."}
  evidence_of_impact:
    - {value: "Often listed as the first medieval philosopher", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}
  major_works:
    - {value: "De trinitate", year: 419, kind: book, certainty: 0.5, cites: [{source: S1, locator: "§2 Works"}], how_known: "SEP: 399–419 (or 426)."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Foundational for medieval philosophy (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Mixed: mother Monnica a devout Christian; father Patricius baptized only on his deathbed", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP."}
  family_religious_practice: {value: "Made a catechumen as a child", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP."}
  parents_and_household:
    - {value: "Monnica, mother, devout Christian", role: mother, certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP."}
    - {value: "Patricius, father", role: father, certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated in the section read."}
  schooling: []
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["Latin"], certainty: 0.5, cites: [{source: S1, locator: "§1 Life"}], how_known: "Inferred."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "396–426", certainty: 0.5, cites: [{source: S1, locator: "§2 Works"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Catholic Church (bishop of Hippo)", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not scored."}
  primary_system:
    value: CHRIST
    basis: written_profession
    certainty: 0.7
    cites: [{source: S1, locator: "§1 Life"}, {source: S4, locator: "XXII.8"}, {source: S6, locator: "Conf. XII.7"}]
    how_known: "Converted 386, baptized 387, bishop c. 396 (S1); City of God professes Christ (S4 NPNF Dods); Confessions creatio ex nihilo prayer to the Lord (S6). Named alternatives none that displace CHRIST; 0.7."
    rationale: "CHRIST: public written profession across the span."
  secondary_system: {value: UNKNOWN, how_known: "None scored (Neoplatonist influence is philosophical, not a second profession)."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Coded at 0.7."}
    - {code: PANENT, reason: "Rejected: SEP reports creation out of nothing (Conf. 12.6)."}
  lio_axes:
    A_locus:
      value: 0
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S4, locator: "City of God XXI.8"}, {source: S5, locator: "De civitate Dei XXI.8 (Latin)"}, {source: S6, locator: "Conf. XII.7"}]
      how_known: "Dods NPNF (S4): 'the will of so mighty a Creator is certainly the nature of each created thing.' Latin (S5): 'uoluntas tanti utique conditoris conditae rei cuiusque natura sit.' Confessions XII.7 (S6): 'out of nothing didst Thou create heaven and earth.' Independent English + Latin + Confessions → corroborated (P48). Contested alt 1 caps ≤0.7."
      rationale: "A personal Creator distinct from creation (creatio ex nihilo; Creator's will as each thing's nature). Alternative 1: nature identified with the Creator's will could be read as closer immanence."
      alternatives:
        - {value: 1, note: "Nature as God's will.", cites: [{source: S4, locator: "XXI.8"}, {source: S5, locator: "XXI.8 Latin"}]}
    B_cause:
      value: 2
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S4, locator: "City of God XXI.8; XXII.8"}, {source: S5, locator: "De civitate Dei XXI.8; XXII.8 (Latin)"}]
      how_known: "NPNF Dods (S4) + Latin (S5) agree: XXI.8 lawfulness with divine exceptions ('laws so sure and inflexible' yet God alters a star's course; portent not contrary to nature but to what we know as nature); XXII.8 live recurring miracles ('even now miracles are wrought' / 'etiam nunc fiunt miracula'). No longer web-copy-only. Contested alt 1 caps ≤0.7 (P25). Independent English + Latin → corroborated (P48)."
      rationale: "Account of nature (P6): lawfulness with exceptions that are not limited (P27 B 2 anchor; RQ-Z4-2 upheld; Ibn Khaldun precedent). XXI.8 states sure inflexible stellar laws and God's sovereign alteration of them; XXII.8 asserts miracles continue now by sacraments, prayers, saints' memorials. Rules out B 1 as sole reading (lawfulness is real) and B 3 (exceptions are live and recurring, not limited). Alternative 1: nature is itself the Creator's will, every event His act."
      alternatives:
        - {value: 1, note: "Nature as the Creator's will.", cites: [{source: S4, locator: "XXI.8"}, {source: S5, locator: "XXI.8 Latin"}]}
    C_ledger: {value: UNKNOWN, how_known: "Eternal punishment (City of God XXI) not scored at this reading (coder's call)."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "SEP: 'committed to the truth of biblical revelation' yet 'surprisingly undogmatic'; no own passage on ranking authorities read."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: TODO, how_known: "A_locus = 0 at 0.7 (corroborated) and B_cause = 2 at 0.7 (corroborated). A ≤ 1 but B = 2 falls between the branches of the P4 test (CODING_GUIDE §6): true needs B ≥ 3; false via the A≤1 branch needs B ≤ 1.", note: "Needs a decision on whether B 2 mid-basin cases count, not more evidence. B 3 would make mid_basin true; B 1 would make it false."}
  statements:
    - text: "For how is that contrary to nature which happens by the will of God, since the will of so mighty a Creator is certainly the nature of each created thing? A portent, therefore, happens not contrary to nature, but contrary to what we know as nature."
      cites: [{source: S4, locator: "City of God XXI.8 (NPNF Dods)"}, {source: S2, locator: "XXI.8"}]
      date: "426"
      context: "City of God XXI (books 412–426). Dods NPNF via IA OCR matches New Advent."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Date is the work's completion year."
    - text: "Quo modo est enim contra naturam, quod Dei fit uoluntate, cum uoluntas tanti utique conditoris conditae rei cuiusque natura sit? Portentum ergo fit non contra naturam, sed contra quam est nota natura."
      cites: [{source: S5, locator: "De civitate Dei XXI.8"}]
      date: "426"
      context: "Latin of City of God XXI.8 (Wikisource Latin; matches The Latin Library). Independent of Dods."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
    - text: "What is there so arranged by the Author of the nature of heaven and earth as the exactly ordered course of the stars? What is there established by laws so sure and inflexible? And yet, when it pleased Him who with sovereignty and supreme power regulates all He has created, a star conspicuous among the rest by its size and splendor changed its color, size, form, and, most wonderful of all, the order and law of its course!"
      cites: [{source: S4, locator: "City of God XXI.8"}]
      date: "426"
      context: "Lawfulness with divine exception (Venus portent); continues to Joshua's sun standing still."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
    - text: "For even now miracles are wrought in the name of Christ, whether by His sacraments or by the prayers or relics of His saints; but they are not so brilliant and conspicuous as to cause them to be published with such glory as accompanied the former miracles."
      cites: [{source: S4, locator: "City of God XXII.8"}, {source: S2, locator: "XXII.8"}]
      date: "426"
      context: "City of God XXII.8; Dods NPNF via IA OCR matches New Advent."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
    - text: "Nam etiam nunc fiunt miracula in eius nomine, sive per sacramenta eius sive per orationes vel memorias sanctorum eius; sed non eadem claritate illustrantur, ut tanta quanta illa gloria diffamentur."
      cites: [{source: S5, locator: "De civitate Dei XXII.8"}]
      date: "426"
      context: "Latin of City of God XXII.8 (Wikisource Latin)."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
    - text: "And therefore, out of nothing didst Thou create heaven and earth, — a great thing and a small, because Thou art Almighty and Good, to make all things good, even the great heaven and the small earth. Thou wast, and there was naught else from which Thou didst create heaven and earth."
      cites: [{source: S6, locator: "Confessions XII.7 (NPNF Outler/Pilkington)"}]
      date: "400"
      context: "Confessions Book XII ch. 7; creatio ex nihilo. Date is end of the ca. 396–400 range."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
  changes_over_life:
    - {value: "Manichean 'hearer' c. 373 for nine years; conversion summer 386; baptism Easter 387", year: 386, certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP; before the span."}
  coder_notes: "B 2 vs 1 upheld at 0.7 after Latin+NPNF corroboration (RQ-Z4-2). mid_basin TODO: P4 has no branch for A≤1 with B=2 (Pascal/Planck pattern); true would need B≥3. De Genesi ad litteram on rationes seminales still unread."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Roman North African", certainty: 0.5, cites: [{source: S1, locator: "§1 Life"}], how_known: "Coder's summary."}
  religious_heritage_by_birth: {value: "Christian mother, pagan father", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP."}
  baptism_or_initiation: {value: "Catechumen as a child; baptized Easter 387 by Ambrose in Milan", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "396–426", certainty: 0.5, cites: [{source: S1, locator: "§2 Works"}], how_known: "Confessions (ca. 396–400, start year per P12 addendum d) to City of God (412–426) (P29, P30)."}
  age_at_first_lasting_contribution: {value: 42, certainty: 0.5, cites: [{source: S1, locator: "§1 Life; §2 Works"}], how_known: "396 − 354 = 42 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: "400", certainty: 0.5, cites: [{source: S6, locator: "Conf. XII.7"}], how_known: "Confessions creatio ex nihilo within span start range; City of God XXI–XXII is later (412–426)."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.7, cites: [{source: S6, locator: "Conf. XII.7"}, {source: S4, locator: "XXI.8; XXII.8"}], how_known: "Confessions and City of God are the lasting works that bound the span."}
  worldview_during_major_work: {value: "CHRIST", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}, {source: S4, locator: "XXII.8"}], how_known: "Bishop throughout; City of God and Confessions profess CHRIST."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Philosophy and theology (S1).", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions:
  - {value: "Church of Hippo", role: "priest (391), bishop (c. 396–430)", years: "391–430", kind: "religious body", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP."}
collaborators:
  - {value: "Ambrose of Milan", relation: "influenced by", note: "baptized him", certainty: 0.7, cites: [{source: S1, locator: "§1 Life"}], how_known: "SEP."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 150"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "English readings from NPNF Dods via IA OCR; Latin from Wikisource (unofficial web copy of Latin)."
  open_questions:
    - "De Genesi ad litteram on rationes seminales for B (still unread)."
    - "Critical Latin edition (CCSL) page-check of XXI.8 / XXII.8."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Christian Tornau"
    citation: "Tornau, Christian. \"Saint Augustine.\" Stanford Encyclopedia of Philosophy (first published 25 September 2019; revised 26 April 2024). https://plato.stanford.edu/entries/augustine/"
    url: "https://plato.stanford.edu/entries/augustine/"
    accessed: 2026-10-24
    reliability_note: "Signed scholarly encyclopedia article."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Augustine of Hippo, tr. Marcus Dods"
    citation: "Augustine. The City of God, tr. Marcus Dods. Nicene and Post-Nicene Fathers, First Series, vol. 2 (1887), via New Advent. https://www.newadvent.org/fathers/1201.htm"
    url: "https://www.newadvent.org/fathers/1201.htm"
    accessed: 2026-10-24
    reliability_note: "Public-domain translation, web copy; readings confirmed against S4 NPNF IA OCR."
    source_quality: "unofficial web copy"
    used_for: [worldview]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [review]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "Augustine of Hippo, tr. Marcus Dods; ed. Philip Schaff"
    citation: "Augustine. The City of God and Christian Doctrine. Nicene and Post-Nicene Fathers, First Series, vol. 2, tr. Marcus Dods, ed. Philip Schaff (1887). Internet Archive TheCityOfGodAndOnChristianDoctrineVolume2FirstSeriesOfThe (djvu OCR)."
    url: "https://archive.org/details/TheCityOfGodAndOnChristianDoctrineVolume2FirstSeriesOfThe"
    accessed: 2026-10-24
    reliability_note: "Scholarly NPNF edition; IA OCR used this pass for XXI.8 and XXII.8."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview, timing]
  - id: S5
    type: primary
    kind: "published work by the subject"
    author: "Augustine of Hippo"
    citation: "Augustine. De civitate Dei, Liber XXI and Liber XXII (Latin). Wikisource Latin. https://la.wikisource.org/wiki/De_civitate_Dei/Liber_XXI ; https://la.wikisource.org/wiki/De_civitate_Dei/Liber_XXII (cross-checked The Latin Library civ21/civ22)."
    url: "https://la.wikisource.org/wiki/De_civitate_Dei/Liber_XXI"
    accessed: 2026-10-24
    reliability_note: "Latin text of the treatise; unofficial web transcription, not a critical CCSL page-check."
    source_quality: "unofficial web copy"
    used_for: [worldview]
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "Augustine of Hippo; NPNF translators"
    citation: "Augustine. The Confessions and Letters of Augustin. Nicene and Post-Nicene Fathers, First Series, vol. 1. Internet Archive TheConfessionsAndLettersOfAugustinWithASketchOfHisLifeAndWork (djvu OCR), Confessions Book XII ch. 7."
    url: "https://archive.org/details/TheConfessionsAndLettersOfAugustinWithASketchOfHisLifeAndWork"
    accessed: 2026-10-24
    reliability_note: "Scholarly NPNF edition; IA OCR used for Conf. XII.7 creatio ex nihilo."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview, timing]
---

## Summary

Augustine of Hippo (354–430), bishop and philosopher [S1]. Draft: CHRIST (0.7); A 0 @0.7; B 2 @0.7 (alt 1). Plotted (dark, filled after deepen).

## Life and work

Thagaste, Carthage, Rome, Milan, Hippo [S1].

## Contribution and impact

Confessions; City of God [S1].

## Childhood and education

Christian mother, catechumen [S1].

## Adult working worldview

Creator whose will is nature; laws sure yet God alters them; miracles continue now [S4, S5]; creatio ex nihilo [S6].

## Heritage (context only)

Roman North African [S1].

## Timing

396–426, age 42 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- De Genesi ad litteram on rationes seminales.
- CCSL Latin page-check of XXI.8 / XXII.8.

## Research log

- 2026-10-24: Deepen D1 — NPNF Dods City of God (IA S4); Latin XXI.8/XXII.8 (Wikisource/Latin Library S5); Confessions XII.7 (NPNF IA S6). B 2 0.5→0.7 corroborated; A corroborated; mid TODO (between branches); chart-moving YES (faded→dark, hollow→filled).
- 2026-10-19: Read SEP (Tornau); City of God XXI.8, XXII.8 (Dods).
