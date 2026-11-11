---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 4
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch Z2; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to medieval. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-25, by: "Grok Bot", summary: "Perpetual deepen: A_locus P48 fill. SEP §2 (S1) also attests intervening Creator/theodicy (God intervenes to make the world as good as it can be; bestows intellect; wise-father learning) that agrees with A 0 Master/Creator own voice — add S1 to A value cites. Alt 1 five-eternals/design reading kept (S1 still on alt, no longer exclusive of main). A support single→corroborated; B already corroborated → hollow→filled (still faded: B @0.5). mid_basin unchanged (B 0.5). Chart-moving YES (fill). No figures/; no fallacy_catalog."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen D1 (queue #138): opened Butterworth Philosophic Life (Interpretation 20.3, 1993) and Arberry Spiritual Physick (1950). A 1 @0.5 scholarly_reconstruction → A 0 @0.7 written_profession (Master/reward/Creator-master; alt 1 = five-eternals design cosmology, P49 SEP). B stays 3 @0.5 (P35/P16: nature-necessity line too thin for cause-order lift; Doubts about Galen unread; alt 4 kept). primary_system stays BELOW_THRESHOLD (religion dispute honest). mid_basin stays BELOW. Chart-moving NO. P47 source_quality; P48 A corroborated / B single; P50 Wikipedia EN dual bio (birth 864/865; death 925/935). No figures/; no fallacy_catalog."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Z2 audit fixes (blind audit /workspace/genius_study_audit/gs_f70a593_Z2/run1/): the 0.5 ceiling now cites the scholarly-reconstruction ceiling (CODING_GUIDE §3), not P36. No score changed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch Z2, order P32: F 3, rank 142). Source: SEP 'Abu Bakr al-Razi' (Peter Adamson, rev. 2025). Scholarly reconstruction only: five eternal principles; God's existence 'demonstrated on the basis of the good design of the universe'; 'God intervenes to make the world as good as it can be'; creation ex nihilo impossible. His religion is disputed: the hostile Abū Ḥātim has him reject prophecy and miracles, but Doubts about Galen acknowledges 'books sent by God'. A scientist (P30: medicine; alchemy is described as chemical procedure, so it does not cut the inference). Span UNKNOWN (P12, P39: no lasting work dated in the source); era '500 to 1399'. primary_system BELOW_THRESHOLD (leads PLATO, DEISM, ISLAM); A 1 (0.5, alt 0); B 3 (0.5, alt 4); C UNKNOWN; D BELOW_THRESHOLD; E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Plotted (faded) at the next chart refresh. Draft, not reviewed."}

identity:
  id: al-razi
  display_name: "Al-Razi"
  roster:
    canonical_name: "Al-Razi"
    rank: 142
    F: 3
    models: [Claude, DeepSeek, Grok]
    band: "core (3–4)"
    status: core
    field: medicine
    field_bucket: medicine
  full_name: {value: "Abū Bakr Muḥammad ibn Zakariyyāʾ al-Rāzī", certainty: 0.7, cites: [{source: S1, locator: "§1"}, {source: S5, locator: "lead"}], how_known: "SEP; Wikipedia EN."}
  native_name: {value: "Abū Bakr Muḥammad ibn Zakariyyāʾ al-Rāzī", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP (transliterated Arabic)."}
  aliases:
    - {name: "Razi", kind: "roster alias"}
    - {name: "Rhazes", kind: "latinized"}

basics:
  birth:
    date: {value: "865", calendar: gregorian, certainty: 0.5, cites: [{source: S1, locator: "heading (865–925 CE)"}, {source: S5, locator: "lead (864 or 865)"}], how_known: "P50 dual bio: SEP 865 vs Wikipedia EN 864 or 865. Real dispute, so 0.5.", alternatives: [{value: "864", note: "Wikipedia EN alternative.", cites: [{source: S5, locator: "lead"}]}]}
    place: {value: "Rayy", modern_name: "Rey, near Tehran, Iran", polity_then: "Abbasid caliphate", certainty: 0.7, cites: [{source: S1, locator: "§1"}, {source: S5, locator: "Biography"}], how_known: "SEP 'hailed from' Rayy; Wikipedia EN born in Ray — lifted from 0.5."}
  death:
    date: {value: "925", calendar: gregorian, certainty: 0.5, cites: [{source: S1, locator: "heading"}, {source: S5, locator: "lead (925 or 935); Biruni 925"}], how_known: "P50: SEP 925; Wikipedia EN 925 or 935 (Biruni: died in Rey 925 at sixty). Dispute, so 0.5.", alternatives: [{value: "935", note: "Wikipedia EN alternative.", cites: [{source: S5, locator: "lead"}]}]}
    place: {value: "Rayy", modern_name: "Rey, near Tehran, Iran", polity_then: "Abbasid caliphate", certainty: 0.7, cites: [{source: S5, locator: "Biography (Biruni)"}], how_known: "Wikipedia EN citing Biruni."}
  first_lasting_contribution_year: {value: UNKNOWN, how_known: "No lasting work is dated in SEP; the Book for al-Manṣūr is dedicated to a governor who died in 914, so it is before 914 (P12: undated items do not set the year)."}
  era_bucket: {value: "500 to 1399", certainty: 1.0, cites: [{source: S1, locator: "heading"}], how_known: "Every work falls between 865 and 925 (P2, P39)."}
  region_of_birth: {value: "Middle East and North Africa", certainty: 0.7, cites: [{source: S1, locator: "§1"}, {source: S5, locator: "Biography"}], how_known: "Iran, placed in MENA (P3)."}
  region_of_work: {value: "Middle East and North Africa", certainty: 0.7, cites: [{source: S1, locator: "§1"}, {source: S5, locator: "Biography"}], how_known: "Hospitals in Rayy and Baghdad."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "As recorded."}
  languages_of_work: {value: ["Arabic"], certainty: 0.7, cites: [{source: S1, locator: "§1 (Arabic editions)"}, {source: S5, locator: "lead (native speaker of Persian)"}], how_known: "SEP Arabic editions; Wikipedia notes Persian native speech — Arabic remains the coded working language of the surviving philosophical works."}
  occupations: {value: ["physician and hospital director", "philosopher", "alchemist"], certainty: 0.7, cites: [{source: S1, locator: "§1"}, {source: S5, locator: "lead"}], how_known: "SEP; Wikipedia EN."}

contribution:
  era_bucket: medieval
  fields: {value: ["medicine", "philosophy", "alchemy"], certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
  lasting_original_contributions:
    - {value: "Doubts about Galen", year: UNKNOWN, kind: work, lasting: "his critique of Galen, 'the most significant surviving work for his philosophy' (S1)", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP; undated; English/French primary unread this pass."}
    - {value: "The Book for al-Manṣūr", year: UNKNOWN, kind: work, lasting: "'a substantial medical treatise' (S1)", certainty: 0.5, cites: [{source: S1, locator: "§1"}], how_known: "SEP; before 914; lasting is the coder's call."}
  evidence_of_impact:
    - {value: "Made his fame mostly as a doctor", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
    - {value: "Latin Continens / Liber Almansoris printed and taught in medieval Europe", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S5, locator: "lead / Works"}], how_known: "Wikipedia EN."}
  major_works:
    - {value: "The Spiritual Medicine (Spiritual Physick)", year: UNKNOWN, kind: book, certainty: 0.7, cites: [{source: S4, locator: "title / Ch. I"}, {source: S1, locator: "§1"}], how_known: "Arberry 1950; SEP."}
    - {value: "The Philosophical Way of Life (Book of the Philosophic Life)", year: UNKNOWN, kind: book, certainty: 0.7, cites: [{source: S3, locator: "title"}, {source: S1, locator: "§1"}], how_known: "Butterworth 1993; SEP."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "A leading physician whose medical and philosophical works survive and are studied (S1).", certainty: 0.7, cites: [{source: S1, locator: "§1; §6"}], how_known: "Coder's reading."}

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
  working_years: {value: UNKNOWN, how_known: "Equals timing.major_work_period (UNKNOWN)."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "Reason discovers the Creator; a revelatory text's truth must accord with reason (Adamson minimum, S1 §5) — own voice confirms Reason's primacy for knowing the Creator (S4 Ch. I), not a settled D score", certainty: 0.5, cites: [{source: S4, locator: "Ch. I pp. 20–21"}, {source: S1, locator: "§5"}], how_known: "Own voice on Reason; religion dispute still open (S1 §5)."}
  primary_system:
    value: BELOW_THRESHOLD
    how_known: "Deepen D1: own-voice Creator/Master language (S3, S4) does not settle the dispute. Hostile Abū Ḥātim still has him reject prophecy and miracles (S1 §5); Doubts about Galen 'books sent by God' remains SEP-only (unread). Leads unchanged: PLATO (five eternals + Theaetetus 'likeness to God' quote in S3 §29), DEISM (design demonstration, S1 §2; P27 fails if he accepted revelation), ISLAM (books sent by God; Muslim milieu). Do not force a code."
  secondary_system: {value: UNKNOWN, how_known: "See primary."}
  candidate_codes_considered:
    - {code: DEISM, reason: "Lead only: P27 requires rejecting revelation, which is disputed (S1 §5)."}
    - {code: PLATO, reason: "Lead: five eternals with Soul (S1 §2); Philosophic Life quotes Theaetetus likeness-to-God (S3 §29). No source codes him PLATO as primary."}
    - {code: ISLAM, reason: "Lead only: 'books sent by God' (S1 §5 on Doubts); milieu Muslim (S5)."}
    - {code: CLASS_THEISM, reason: "Lead only from Creator/Master own voice (S3, S4); five-eternals cosmology and religion dispute block a forced code."}
  lio_axes:
    A_locus:
      value: 0
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S3, locator: "§§9.iv, 15, 29 (Kraus pp. 102–108)"}, {source: S4, locator: "Ch. I pp. 20–21"}, {source: S1, locator: "§2 (God intervenes; bestows intellect; wise-father theodicy)"}]
      how_known: "Own-voice Master/Creator (S3 Philosophic Life; S4 Spiritual Physick) plus SEP §2 reconstruction that the same God 'intervenes to make the world as good as it can be', bestows intellect on the Soul, and acts as a wise father in theodicy (S1) — personal intervening Creator language that agrees with A 0. Named alt 1 (five-eternals / design-demonstration as more distant) still cites S1, but S1 is now also on the value → no alt-exclusive source (P48). Independent source ids S3/S4/S1 → corroborated. Ceiling 0.7 from named alt."
      rationale: "A separate personal God who rewards, punishes, looks over, and is Master/Creator (S3/S4), with SEP §2 also reporting intervention and intellect-gift (not mere absentee design): 0. Alternative 1: five-eternals cosmology with design-demonstration and creation-via-Soul (S1 §2) read as a more distant ordering God."
      alternatives:
        - {value: 1, note: "Five-eternals / design-demonstration God (SEP scholarly reconstruction, P49); kept as contested reading of the same SEP §2.", cites: [{source: S1, locator: "§2"}]}
    B_cause:
      value: 3
      basis: scholarly_reconstruction
      certainty: 0.5
      support: corroborated
      cites: [{source: S1, locator: "§1; §5"}, {source: S3, locator: "§15 (nature-necessity of pain)"}]
      how_known: "Deepen D1: still at scholarly-reconstruction / P35 ceiling 0.5. Physician (P30) whose medical theory works within Galenic humours; alchemy as chemical procedure (S1). Philosophic Life §15 — pain that 'pertains to nature is thus due to a necessity and occurred inevitably' — is own-voice natural necessity, but it is about pain ethics, not an explicit account of physical causation or miracles (P16/P35: working science alone does not lift B to 0.7). Doubts about Galen unread. Abū Ḥātim's miracle-rejection report points to alt 4 but is hostile and unverified (S1 §5)."
      rationale: "P35 working-science B 3 at 0.5; alt 4 named. Not raised."
      alternatives:
        - {value: 4, note: "P35 alternative; Abū Ḥātim's report that he rejected miracles.", cites: [{source: S1, locator: "§5"}]}
    C_ledger: {value: UNKNOWN, how_known: "Philosophic Life has reward/punishment and a praiseworthy/blameworthy state after death (S3 §9.i, §9.iv) — C lead only; mechanism of the ledger not scored (P19)."}
    D_authority: {value: BELOW_THRESHOLD, how_known: "Spiritual Physick Ch. I elevates Reason for knowing the Creator (S4); leads toward 4, but religion/revelation dispute and hostile reports block a score (S1 §5; P19)."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Not scored from science alone (P19)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A now 0 @0.7, but B still 3 @0.5 — both need ≥0.7 (P10)."}
  statements:
    - text: "Our Master, from whom we hope for reward and fear punishment, looking over us and having compassion for us, does not want us to cause pain; detesting injustice and ignorance on our part, He loves for us to be knowledgeable and just; indeed, this Master punishes the one among us who causes pain and who deserves to be pained according to what he deserves."
      cites: [{source: S3, locator: "§9.iv (Kraus p. 102)"}]
      context: "Book of the Philosophic Life, principles of the philosophic life."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Butterworth 1993 translation from Kraus Rasāʾil."
    - text: "Since the Creator, may He be glorified and magnified, is a knower who is not ignorant and a doer of justice who does no injustice; and since He is unqualified knowledge, justice, and compassion; and since He is a creator and master to us, whereas we are slaves and vassals to Him… the slaves closest to God… are those who are most learned, most just, most compassionate, and most kindly. … “Philosophy is making oneself similar to God… to the extent possible for a human being.”"
      cites: [{source: S3, locator: "§29 (Kraus pp. 108–109)"}]
      context: "Philosophic Life, sum of the philosophic life (Theaetetus 176b)."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Butterworth; Plato likeness-to-God."
    - text: "Any pain befalling us that is not by our enterprise or choices but pertains to nature is thus due to a necessity and occurred inevitably."
      cites: [{source: S3, locator: "§15 (Kraus pp. 103–104)"}]
      context: "Philosophic Life, about pain — used as thin B lead only."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Not enough alone to lift B past 0.5 (P16/P35)."
    - text: "The Creator (Exalted be His Name) gave and bestowed upon us Reason to the end that we might thereby attain and achieve every advantage… By Reason we have achieved even the knowledge of the Almighty, our Creator, the most majestic of all that we have sought to reach and our most profitable attainment."
      cites: [{source: S4, locator: "Ch. I pp. 20–21"}]
      context: "Spiritual Physick, Of the Excellence and Praise of Reason."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Arberry 1950; corroborates A."
  changes_over_life: []
  coder_notes: "Deepen D1: A flipped 1→0 on own voice; B deliberately not lifted (P35/P16). 2026-10-25: A P48 fill via SEP §2 intervention/theodicy agreeing with Master/Creator — hollow→filled (faded). Doubts about Galen and On Divine Science still unread. Religion dispute kept honest — primary_system BELOW. Span UNKNOWN."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Persian (Rayy)", certainty: 0.7, cites: [{source: S1, locator: "§1 ('the Persian city of Rayy')"}, {source: S5, locator: "Biography (Persian stock)"}], how_known: "SEP; Wikipedia EN."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated; Wikipedia calls him a Persian Muslim physician — milieu, not childhood religion."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not applicable or not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: UNKNOWN, how_known: "No lasting work is dated in the sources read (P12, P29, P39)."}
  age_at_first_lasting_contribution: {value: UNKNOWN, how_known: "First-lasting year UNKNOWN (P12)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "Philosophic Life and Spiritual Physick undated."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "Works undated."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Works undated."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Wrote on mathematics and logic (S1); nothing on method.", certainty: 0.5, cites: [{source: S1, locator: "§1"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not stated."}
  circle_present: {value: "no", rationale: "God is Master/Creator distinct from creatures (S3 §29); one of five distinct eternals in SEP cosmology (S1 §2), not identified with nature.", certainty: 0.7, cites: [{source: S3, locator: "§29"}, {source: S1, locator: "§2"}], how_known: "Own voice + SEP."}
  reading: "No circle."
  notes: "Lane A and Lane B kept separate (P49)."

institutions:
  - {value: "Hospital in Rayy", role: "director (per biographers)", years: UNKNOWN, kind: other, certainty: 0.5, cites: [{source: S1, locator: "§1"}], how_known: "SEP: 'His biographers report'."}
  - {value: "Hospital in Baghdad", role: "director (per biographers)", years: UNKNOWN, kind: other, certainty: 0.5, cites: [{source: S1, locator: "§1"}, {source: S5, locator: "Biography"}], how_known: "SEP; Wikipedia EN."}
collaborators:
  - {value: "Abū Ṣāliḥ al-Manṣūr", relation: "mentor or employer", note: "governor of Rayy, patron", certainty: 0.7, cites: [{source: S1, locator: "§1"}], how_known: "SEP."}
  - {value: "Abū Ḥātim al-Rāzī", relation: "rival or critic", note: "Ismāʿīlī opponent, The Proofs of Prophecy", certainty: 0.7, cites: [{source: S1, locator: "§1; §5"}], how_known: "SEP."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 142"}], how_known: "Study roster."}
  controversies:
    - {value: "Whether he rejected prophecy and revelation (hostile Abū Ḥātim vs Doubts 'books sent by God')", certainty: 0.7, cites: [{source: S1, locator: "§5"}], how_known: "SEP."}
    - {value: "Birth 864/865 and death 925/935 (P50)", certainty: 0.7, cites: [{source: S1, locator: "heading"}, {source: S5, locator: "lead"}], how_known: "SEP; Wikipedia EN."}
  data_quality_flags:
    - "Doubts about Galen still unread in primary; 'books sent by God' is SEP-only."
    - "Five-eternals cosmology remains SEP scholarly reconstruction (P49), not own-voice cosmology treatise."
    - "Butterworth from archive.org OCR of Interpretation 20.3; Arberry from OLL PDF."
  open_questions:
    - "Open Doubts about Galen (Koetschet 2019 or McGinnis/Reisman anthology) for books-sent-by-God and any cause/miracle lines."
    - "Open On Divine Science / cosmology fragments if available."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Peter Adamson"
    citation: "Adamson, Peter. \"Abu Bakr al-Razi.\" Stanford Encyclopedia of Philosophy (first published 2021; revised 14 May 2025). https://plato.stanford.edu/entries/abu-bakr-al-razi/"
    url: "https://plato.stanford.edu/entries/abu-bakr-al-razi/"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Signed scholarly reference by the author of the standard monograph (Adamson 2021). Cosmology and religion sections used as P49 reconstruction where own voice is missing."
    used_for: [identity, basics, contribution, worldview, heritage, lane_b, institutions, collaborators, review]
  - id: S2
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    source_quality: "study roster"
    reliability_note: "Study's own roster."
    used_for: [review]
  - id: S3
    type: primary
    kind: scholarly edition
    author: "Al-Rāzī; Charles E. Butterworth (trans.)"
    citation: "Al-Rāzī, Abū Bakr Muḥammad ibn Zakariyyāʾ. \"The Book of the Philosophic Life.\" Translated by Charles E. Butterworth. Interpretation 20, no. 3 (Spring 1993): 227–236. Based on Kraus, Rasāʾil Falsafiyya (Beirut reprint 1973), pp. 98–111."
    url: "https://archive.org/stream/razi-book-of-philosophic-life-butterworth/Razi%20-%20Book%20of%20Philosophic%20Life%20%5BButterworth%5D_djvu.txt"
    accessed: 2026-10-24
    source_quality: "archive scan (OCR only)"
    reliability_note: "Standard English translation of Kitāb al-Sīra al-Falsafiyya; read from Internet Archive OCR of the Interpretation printing."
    used_for: [contribution, worldview, lane_b]
  - id: S4
    type: primary
    kind: scholarly edition
    author: "Al-Rāzī (Rhazes); Arthur J. Arberry (trans.)"
    citation: "Arberry, Arthur J., trans. The Spiritual Physick of Rhazes. London: John Murray, 1950 (Wisdom of the East Series)."
    url: "https://oll-resources.s3.us-east-2.amazonaws.com/oll3/store/titles/1791/0955_Bk.pdf"
    accessed: 2026-10-24
    source_quality: "scholarly edition or monograph"
    reliability_note: "Public-domain Arberry translation of al-Ṭibb al-rūḥānī; OLL facsimile PDF."
    used_for: [contribution, worldview]
  - id: S5
    type: secondary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia. \"Abu Bakr al-Razi.\" English Wikipedia (accessed 2026-10-24). https://en.wikipedia.org/wiki/Abu_Bakr_al-Razi"
    url: "https://en.wikipedia.org/wiki/Abu_Bakr_al-Razi"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "P50 dual bio (birth 864/865; death 925/935; death at Rey per Biruni); reception notes."
    used_for: [identity, basics, contribution, heritage, institutions, review]
---

# Al-Razi

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Abū Bakr al-Rāzī (c. 865–925), physician and philosopher of Rayy [S1; S5]. Deepen D1: primary_system BELOW_THRESHOLD; A 0 (0.7, alt 1, corroborated); B 3 (0.5, alt 4, single); C UNKNOWN; D, E BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Would remain plotted faded (figures/ not touched).

## Life and work

Hospitals in Rayy and Baghdad [S1; S5].

## Contribution and impact

Doubts about Galen; Book for al-Manṣūr; Spiritual Physick; Philosophic Life [S1; S3; S4].

## Childhood and education

Not recorded in the sources read.

## Adult working worldview

Own-voice Creator/Master who rewards and punishes [S3; S4]. Five-eternals cosmology still SEP reconstruction [S1]. Religion disputed [S1 §5].

## Heritage (context only)

Persian [S1; S5].

## Timing

UNKNOWN (works undated) [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No circle [S3; S1].

## Open questions

- Doubts about Galen primary; On Divine Science / cosmology fragments.

## Research log

- 2026-10-19: Read SEP (Adamson) in full.
- 2026-10-24: Deepen D1 — Butterworth Philosophic Life (Interpretation 20.3 OCR); Arberry Spiritual Physick (OLL PDF); Wikipedia EN dual bio.
