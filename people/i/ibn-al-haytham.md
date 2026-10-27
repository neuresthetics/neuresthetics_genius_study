---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA1; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to physics. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #172/228, F 3, rank 182). Goals: open A/primary if Optics or settled own words allow; do not force plot. Read Sabra Optics I–III English translation (S5, Monoskop PDF of Warburg 1989): Book I preface basmala 'In the Name of God the Compassionate and Merciful'; 'From God we derive support in all things'; methodological 'seek the truth and not to be swayed by opinion' (D lead). No prophet/Throne/Creator-locus doctrine (contrast al-Khwarizmi Algebra preface). Copyist colophon praise of God/Muhammad is the scribe Ahmad ibn Muhammad ibn Ja'far, not the Optics author. Attribution dispute unsettled (P42): Britannica still 'plausibly argued' two Ibn al-Haythams (optics mathematician vs Muhammad who wrote the autobiography) (S1); Sabra rejects Rashed as 'unfortunate' (S6 Encyclopedia.com DSB); Hogendijk notes Sabra vs Rashed open (S7). Autobiography youth religion claim NOT scored as Optics author's voice. primary UNKNOWN → BELOW_THRESHOLD (ISLAM lead from Optics basmala + Fatimid/Cairo setting; not ISLAM @0.5). A stays UNKNOWN (basmala off-point for locus). B stays 3 @0.5 alt 4 (P35); support labelled corroborated (S1+S5, P48). mid UNKNOWN. Not plotted. P47 on S1–S7. No fallacy_catalog. No figures/. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "AA1 audit fixes: era certainty 0.7 -> 0.5 (P39, c. life dates; WEAKEN). Span set from Smith's critical edition, 'Sometime between 1028 and 1038' (S3, added), under RQ-Z9-N1: start 1028 (P12), span 1028–1038, age 63 (1028 − c. 965); v8's call on the auditor's advice. Coder note corrected: the 1011–1021 date (Tbakhi and Amr 2007) is not used. Still not plotted (A UNKNOWN)."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA1, order P32: F 3, rank 182). Basics from Britannica (Richard Lorch, signed; body) and MacTutor (O'Connor and Robertson). No own-voice religious text read. MacTutor reports that in his autobiography he concluded as a youth that none of the religious movements 'represented the truth'; Britannica notes it 'has recently been plausibly argued' that the autobiography is by a different Ibn al-Haytham (Muhammad ibn al-Hasan), so its attribution is disputed (P42) and it is a lead only. primary_system UNKNOWN (lead ISLAM); A UNKNOWN. Scientist: the Optics gives a theory of vision and the laws of reflection and refraction (P30), so B 3 at 0.5 from working science, alt 4 (P24, P35). C, D, E UNKNOWN; mid_basin UNKNOWN. Span 1028–1038 (Smith's composition range, RQ-Z9-N1; AA1 audit fix), age 63. Not plotted. Draft, not reviewed."}

identity:
  id: ibn-al-haytham
  display_name: "Ibn al-Haytham (Alhazen)"
  roster:
    canonical_name: "Ibn al-Haytham (Alhazen)"
    rank: 182
    F: 3
    models: [Claude, DeepSeek, Grok]
    band: "core (3–4)"
    status: "core"
    field: "polymath"
    field_bucket: "polymath"
  full_name: {value: "Abū ʿAlī al-Ḥasan ibn al-Haytham", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica ('in full'); Britannica names the optics author al-Ḥasan ibn al-Ḥasan."}
  native_name: {value: "ابن الهيثم", certainty: 0.5, cites: [{source: S1, locator: "heading"}], how_known: "Arabic spelling the coder's."}
  aliases:
    - {name: "Ibn al-Haytham", kind: "roster alias"}
    - {name: "Alhazen", kind: "latinized"}

basics:
  birth:
    date: {value: "965", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Britannica: c. 965."}
    place: {value: "Basra", modern_name: "Basra, Iraq", polity_then: "Buyid emirate (Abbasid caliphate)", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  death:
    date: {value: "1040", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Britannica: c. 1040."}
    place: {value: "Cairo", modern_name: "Cairo, Egypt", polity_then: "Fatimid caliphate", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1028, certainty: 0.5, cites: [{source: S3, locator: "Preface"}], how_known: "Smith: 'Sometime between 1028 and 1038, Ibn al-Haytham completed his monumental optical synthesis, Kitab al-Manazir'; a specialist's composition range in article text dates a manuscript-era work, start as the year (RQ-Z9-N1, P12); v8's call on the auditor's advice (AA1)."}
  era_bucket: {value: "500 to 1399", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Britannica c. 965–1040 (P2); certainty of the c. life dates (P39; AA1 audit)."}
  region_of_birth: {value: "Middle East and North Africa", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Iraq (P3)."}
  region_of_work: {value: "Middle East and North Africa", certainty: 0.7, cites: [{source: S1, locator: "Life"}], how_known: "Cairo."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Arabic"], certainty: 0.7, cites: [{source: S1, locator: "Major works"}, {source: S5, locator: "title page / Book I heading"}], how_known: "Britannica; Arabic Optics in Sabra translation."}
  occupations: {value: ["mathematician", "astronomer", "physicist"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}

contribution:
  primary_domain: physics
  fields: {value: ["optics", "mathematics", "astronomy"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Kitāb al-manāẓir (Optics): theory of vision by received light; laws of reflection; refraction", year: 1028, kind: "theory", lasting: "'Ibn al-Haytham's most important work is Kitāb al-manāẓir (\"Optics\") ... it contains the correct model of vision' (S1, body)", certainty: 0.7, cites: [{source: S1, locator: "Major works"}, {source: S5, locator: "Book I preface and plan of seven books"}], how_known: "Britannica body; Sabra translation of Optics I–III; dated 1028–1038 by Smith (S3), start 1028 (P12)."}
  evidence_of_impact:
    - {value: "Made significant contributions to the principles of optics and the use of scientific experiments", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works:
    - {value: "al-Shukūk ʿalā Baṭlamyūs (Doubts about Ptolemy)", year: UNKNOWN, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "Major works"}], how_known: "Britannica."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Optics: correct model of vision (S1).", certainty: 0.7, cites: [{source: S1, locator: "Major works"}], how_known: "Britannica."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household: []
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling: []
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1028–1038", certainty: 0.5, cites: [{source: S3, locator: "Preface"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Optics preface is methodological (truth over opinion), not an explicit science–religion relation."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "Optics own words (S5, settled as al-Ḥasan's): basmala and 'From God we derive support in all things' — conventional pious framing, not a prophet/creed profession like al-Khwarizmi's Algebra preface (ISLAM @0.7). Fatimid Cairo / al-Azhar setting (S2) is milieu, not a code. Autobiography youth claim that no religious movement 'represented the truth' (S2 via Ibn Abī Uṣaybiʿa) is disputed attribution (S1 two-person thesis; S6 Sabra rejection; S7 Hogendijk open controversy) and is NOT scored as the Optics author's voice (P42; standing deepen rule). Lead ISLAM remains; not opened at ≥0.5. Do not force."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: ISLAM, reason: "Lead: Optics basmala and God-support formula (S5); Fatimid/Cairo Muslim setting (S1, S2). Too thin for ISLAM @0.5 without prophet/creed profession."}
    - {code: AGNOS, reason: "Disputed lead only: autobiography youth rejection of sectarian religions (S2 paraphrase; Sabra intro paraphrase of seeking 'one truth' closer to God then turning to Aristotle). Not scored while attribution remains unsettled (P42)."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Searched Optics I–III (Sabra translation, S5): basmala and 'From God we derive support in all things' are pious framing, off-point for locus (where God stands relative to the world); no Creator/Throne/transcendence doctrine like al-Khwarizmi's 'Lord of the Sublime Throne'. Autobiography not used (P42). Checked and off-point → UNKNOWN (P19)."}
    B_cause:
      value: 3
      basis: inference_from_work
      certainty: 0.5
      support: corroborated
      cites: [{source: S1, locator: "Major works (Optics: vision; reflection; refraction)"}, {source: S5, locator: "Book I preface §§1–7; experimental survey of visible objects"}]
      how_known: "Scientist (P30, P35): Optics states a physical-mathematical theory of vision and plans reflection/refraction books, with experimental induction (S1, S5). No statement of his own on law and exception, so 3 at 0.5, alternative 4, never 4 (P24, P35). Britannica + Sabra translation → corroborated (P48)."
      rationale: "Laws of light and vision treated as uniform and experimentally checkable (S5 I.2: survey of visible objects 'uniform, unchanging, manifest'). Alternative 4."
      alternatives:
        - {value: 4, note: "Working science cannot tell lawful-with-exceptions from exceptionless (P35).", cites: [{source: S5, locator: "Book I preface / I.2"}]}
    C_ledger: {value: UNKNOWN, how_known: "Nothing in Optics I–III on afterlife or judgement (S5 searched)."}
    D_authority: {value: UNKNOWN, how_known: "Lead only (not scored): Optics preface 'seek the truth and not to be swayed by opinion' / criticizing premises (S5 I.1 §6). Methodological; does not alone score revelation vs observation."}
    E_scope: {value: UNKNOWN, how_known: "Scientist under P30; working optics alone does not score E without a statement (P19)."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, so the P4 test cannot be applied (P19)."}
  statements:
    - text: "In the Name of God the Compassionate and Merciful"
      cites: [{source: S5, locator: "Book I opening (basmala); Book II opening"}]
      date: "1030"
      context: "Kitāb al-Manāẓir Book openings; Sabra English translation of the Arabic. Date is mid-span of Smith's 1028–1038 composition range (approximate)."
      axes: []
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Conventional Islamic basmala. Lead for ISLAM / heritage only; not scored for A or primary (contrast al-Khwarizmi's fuller prophet preface)."
    - text: "our aim in all that we make subject to inspection and review being to employ justice, not to follow prejudice, and to take care in all that we judge and criticize that we seek the truth and not to be swayed by opinion. … From God we derive support in all things."
      cites: [{source: S5, locator: "Book I, ch. 1 (Preface), §6"}]
      date: "1030"
      context: "Optics methodological preface; Sabra translation. Date mid-span of Smith's 1028–1038 range (approximate)."
      axes: [D_authority]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Truth-over-opinion is a D lead only. 'From God we derive support' is pious formula, not a locus doctrine."
  changes_over_life: []
  coder_notes: "D1 2026-10-24: Sabra Optics I–III read (translation). Autobiography still not scored (Rashed two-person vs Sabra one-person unsettled; Britannica still 'plausibly argued'). Do not force A/plot on basmala alone. Smith's 1028–1038 span kept."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Worked in Fatimid Cairo; lived near al-Azhar (biographical reports)", certainty: 0.5, cites: [{source: S2, locator: "al-Qifṭī / al-Azhar paragraphs"}, {source: S1, locator: "Life"}], how_known: "MacTutor (via Ibn al-Qifṭī); Britannica Life. Context only."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated in the sources read."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1028–1038", certainty: 0.5, cites: [{source: S3, locator: "Preface"}], how_known: "Smith's composition range for the Optics, the one listed lasting work (RQ-Z9-N1, P12, P30 end); v8's call on the auditor's advice (AA1)."}
  age_at_first_lasting_contribution: {value: 63, certainty: 0.5, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "Preface"}], how_known: "1028 − 965 = 63 (P30 year difference); birth c. 965, so about 63."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "Optics basmala is formulaic, not an LIO locus view; autobiography disputed (P42)."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "No scored adult LIO view."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None scored for 1028–1038."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "Geometrical optics; conic sections (S1, S5).", certainty: 0.5, cites: [{source: S1, locator: "Major works"}, {source: S5, locator: "Book I preface (mathematical sciences)"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data."
  notes: ""

institutions: []
collaborators:
  - {value: "al-Ḥākim", relation: "mentor or employer", note: "Fatimid caliph; Nile scheme", certainty: 0.7, cites: [{source: S2, locator: "text"}], how_known: "MacTutor (Ibn al-Qifṭī's account)."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 182"}], how_known: "Study roster."}
  controversies:
    - {value: "One vs two Ibn al-Haythams (autobiography attribution): Rashed two-person thesis vs Sabra one-person reply; unsettled (P42).", certainty: 0.7, cites: [{source: S1, locator: "Life / writings lists"}, {source: S6, locator: "Rashed 1993 / Sabra 1998 discussion"}, {source: S7, locator: "controversy note"}], how_known: "Britannica 'plausibly argued'; Sabra DSB rejection; Hogendijk summary."}
  data_quality_flags:
    - "Autobiography attribution disputed (P42) — not scored as Optics author's voice."
    - "Optics religion language is formulaic basmala only."
  open_questions:
    - "Scholarly settlement of autobiography attribution (full Sabra ZGAW 1998/2002–3 + Rashed MI2 pp. 1–19)."
    - "Any Optics-author theological treatise with settled attribution that states locus of God."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Richard Lorch"
    citation: "Lorch, Richard. 'Ibn al-Haytham.' Encyclopaedia Britannica. https://www.britannica.com/biography/Ibn-al-Haytham (archived body also checked: https://web.archive.org/web/20240207095445/https://www.britannica.com/biography/Ibn-al-Haytham)"
    url: "https://www.britannica.com/biography/Ibn-al-Haytham"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Signed article. Archived body retains: 'It has recently been plausibly argued that there were two Ibn al-Haythams' (optics mathematician vs Muḥammad who wrote the autobiography). Question boxes not used (P26)."
    used_for: [identity, basics, contribution, worldview, lane_b, collaborators, review]
  - id: S2
    type: tertiary
    kind: "encyclopedia"
    author: "J. J. O'Connor and E. F. Robertson"
    citation: "O'Connor, J. J., and E. F. Robertson. 'Abu Ali al-Hasan ibn al-Haytham.' MacTutor History of Mathematics. https://mathshistory.st-andrews.ac.uk/Biographies/Al-Haytham/"
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Al-Haytham/"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Signed reference biography. Presents the 1027 autobiography as Ibn al-Haytham's without flagging the Rashed/Sabra dispute — use only as paraphrase of the traditional attribution, not as settlement."
    used_for: [worldview, heritage, collaborators]
  - id: S3
    type: secondary
    kind: "scholarly edition"
    author: "A. Mark Smith"
    citation: "Smith, A. Mark. Alhacen's Theory of Visual Perception, vol. 1. Transactions of the American Philosophical Society 91, no. 4 (2001), Preface and Introduction pp. xvi–xviii. https://dlib.biblhertz.it/perspectiva/doc01.html"
    url: "https://dlib.biblhertz.it/perspectiva/doc01.html"
    accessed: 2026-10-24
    source_quality: "scholarly edition or monograph"
    reliability_note: "Critical edition by a specialist; preface read (Bibliotheca Hertziana). Composition range 1028–1038 kept."
    used_for: [basics, contribution, timing]
  - id: S4
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-24
    source_quality: "study roster"
    reliability_note: "Study's own roster."
    used_for: [review]
  - id: S5
    type: primary
    kind: "scholarly edition"
    author: "Ibn al-Haytham; A. I. Sabra (trans.)"
    citation: "Sabra, A. I., trans. The Optics of Ibn al-Haytham: Books I–III On Direct Vision. Vol. 1: Translation. London: Warburg Institute, 1989. PDF: https://monoskop.org/images/f/ff/The_Optics_of_Ibn_Al-Haytham_Books_I-III_On_Direct_Vision_Sabra_1989.pdf"
    url: "https://monoskop.org/images/f/ff/The_Optics_of_Ibn_Al-Haytham_Books_I-III_On_Direct_Vision_Sabra_1989.pdf"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "Scholarly English translation of the Arabic Optics (optics author al-Ḥasan). Book I preface and Book openings re-read this pass for religion/method language. Copyist colophons distinguished from author text."
    used_for: [worldview, contribution, lane_b]
  - id: S6
    type: secondary
    kind: "encyclopedia"
    author: "A. I. Sabra"
    citation: "Sabra, A. I. 'Ibn Al-Haytham, Abu ‘Ali Alhasan Ibn Al-Hasan.' Complete Dictionary of Scientific Biography (via Encyclopedia.com). https://www.encyclopedia.com/science/dictionaries-thesauruses-pictures-and-press-releases/ibn-al-haytham-abu-ali-alhasan-ibn-al-hasan"
    url: "https://www.encyclopedia.com/science/dictionaries-thesauruses-pictures-and-press-releases/ibn-al-haytham-abu-ali-alhasan-ibn-al-hasan"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Sabra's DSB entry (body read). Rejects Rashed's two-person split as 'an unfortunate proposition' citing Sabra 1998; treats Optics author as also natural philosopher. Does not by itself settle the dispute for scoring the autobiography (Britannica still presents Rashed as plausible)."
    used_for: [worldview, review]
  - id: S7
    type: secondary
    kind: "other"
    author: "Jan P. Hogendijk"
    citation: "Hogendijk, Jan P. 'Ibn al-Haytham (ca. 965-1041).' https://www.jphogendijk.nl/ibnalhaytham.html (controversy note at end: Rashed MI2 pp. 1–19 two-person thesis; Sabra ZGAW 12 (1998) and 15 (2002–3) disagreement)."
    url: "https://www.jphogendijk.nl/ibnalhaytham.html"
    accessed: 2026-10-24
    source_quality: "other"
    reliability_note: "Specialist's bibliography page summarizing the open Sabra/Rashed controversy; not a new primary read of either monograph."
    used_for: [review, worldview]
---

## Summary

Ibn al-Haytham (c. 965–c. 1040), mathematician and physicist [S1]. Deepen D1: primary BELOW_THRESHOLD (ISLAM lead); A UNKNOWN; B 3 (0.5, corroborated). Not plotted.

## Life and work

Basra; Cairo under the Fatimids [S1, S2].

## Contribution and impact

Kitāb al-Manāẓir (Optics) [S1, S5].

## Childhood and education

Not read in settled own words.

## Adult working worldview

Optics: basmala and God-support formula only — not enough for ISLAM or A [S5]. Autobiography attribution disputed — not scored [S1, S6, S7].

## Heritage (context only)

Fatimid Cairo / al-Azhar reports [S1, S2].

## Timing

1028–1038, age about 63 [S3].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No data.

## Open questions

- Settlement of autobiography attribution.
- Settled Optics-author theological treatise on locus of God.

## Research log

- 2026-10-24: Deepen D1. Sabra Optics I–III translation (S5); Britannica archive attribution; Sabra DSB via Encyclopedia.com (S6); Hogendijk controversy note (S7). Primary UNKNOWN→BELOW; A stays UNKNOWN; B support corroborated. No fallacy_catalog. No figures/.
- 2026-10-19: AA1 audit fixes: era certainty 0.7 -> 0.5 (P39, c. life dates; WEAKEN). Span set from Smith's critical edition, 'Sometime between 1028 and 1038' (S3, added), under RQ-Z9-N1: start 1028 (P12), span 1028–1038, age 63 (1028 − c. 965); v8's call on the auditor's advice. Coder note corrected: the 1011–1021 date (Tbakhi and Amr 2007) is not used. Still not plotted (A UNKNOWN).
- 2026-10-19: Read Britannica (Lorch); MacTutor; Smith's edition (preface).
