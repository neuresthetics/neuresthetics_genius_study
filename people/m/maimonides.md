---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch I)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to medieval. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch I, order P32: F 5, rank 55). Basics from Britannica (Bokser). Worldview from The Guide for the Perplexed, Part II chs. XXV and XXIX (Friedländer, 2nd ed., Gutenberg #73584; web copy, 0.7 cap). Physician, not a natural scientist under P30. primary_system JUDA 0.7; A 0 at 0.7 (alt 1); B 3 at 0.7 (alt 4): the universe keeps its created properties 'except by way of miracle in some individual instances', miracles not permanent (P27 B 3 anchor, rare past miracles); C, D, E UNKNOWN; mid_basin true at 0.7. Plotted. Draft, not reviewed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #55, F5 rank 55). Needs: A single source; B single source. P47 source_quality on S1–S7. Corroborated A via Friedländer Guide II.25/29 (S2) + Ibn Tibbon Hebrew Moreh Nevukhim II.25/29 (S4 Wikisource) + Mishneh Torah Yesodei haTorah 1 (S5 Mechon-mamre: מצוי ראשון ממציא כל הנמצא; שאינו גוף). A stays 0 @ 0.7 written_profession, support single→corroborated (P48); alt 1 retained. Corroborated B via S2 + S4 Hebrew II.29 (לא ישתנה … אלא בפרטיו על צד המופת; עולם כמנהגו הולך; זהו דעתי). B stays 3 @ 0.7 (P27 rare-miracle anchor; alt 4 retained). Dual-source Wikipedia (S7): death Fustat 12 Dec 1204; birth year 1135/1138 contested. Britannica S1 403 this pass — prior Bokser read retained. Pines unread (IA borrow-restricted). Chart-moving YES on fill cue (dark hollow → dark filled); darkness already ≥0.7. No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: maimonides
  display_name: "Maimonides"
  roster:
    canonical_name: "Maimonides"
    rank: 55
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: philosophy
    field_bucket: philosophy
  full_name: {value: "Moses ben Maimon", certainty: 0.7, cites: [{source: S1, locator: "header ('Original name')"}], how_known: "Britannica."}
  native_name: {value: "Abū ʿImran Mūsā ibn Maymūn ibn ʿUbayd Allāh", certainty: 0.7, cites: [{source: S1, locator: "header ('Also known as')"}], how_known: "Britannica (Arabic name, transliterated)."}
  aliases:
    - {name: "Moses Maimonides", kind: "roster alias"}
    - {name: "Rambam", kind: other}

basics:
  birth:
    date: {value: "1135-03-30", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "infobox (1135 or 1138 contested)"}], how_known: "Britannica 30 Mar 1135; Wikipedia notes 1135/1138 contest — keep Britannica date at 0.7."}
    place: {value: "Córdoba, Almoravid al-Andalus", modern_name: "Córdoba, Spain", polity_then: "Almoravid realm (al-Andalus)", certainty: 0.5, cites: [{source: S1, locator: "opening; 'Life'"}], how_known: "Britannica gives Córdoba, 'part of Islamic Spain'; the ruling dynasty is the coder's addition (0.5)."}
  death:
    date: {value: "1204-12-13", calendar: julian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S7, locator: "infobox / death 12 December 1204"}], how_known: "Two sources (Britannica; Wikipedia)."}
    place: {value: "Fustat (al-Fusṭāṭ), Egypt", modern_name: "Cairo area, Egypt", polity_then: "Ayyubid Egypt", certainty: 0.7, cites: [{source: S1, locator: "opening (Egypt); Life (al-Fusṭāṭ)"}, {source: S7, locator: "infobox death place Fustat"}], how_known: "Wikipedia Fustat; Britannica Egypt / al-Fusṭāṭ residence. Buried Tiberias (S1; S7)."}
  first_lasting_contribution_year: {value: 1168, certainty: 0.5, cites: [{source: S1, locator: "opening; 'Works'"}], how_known: "Commentary on the Mishna (with the Thirteen Articles of Faith), completed at age 33: 1135 + 33 = 1168 (derived, 0.5) (P13)."}
  era_bucket: {value: "500 to 1399", certainty: 1.0, cites: [{source: S1, locator: "opening"}], how_known: "His whole life (1135–1204) falls in the bucket (P2)."}
  region_of_birth: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Spain is Southern Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Middle East and North Africa", certainty: 0.7, cites: [{source: S1, locator: "'Life'; 'Works'"}], how_known: "Fez, then al-Fusṭāṭ, Egypt; Egypt is Middle East and North Africa in regions.csv."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [Arabic, Hebrew], certainty: 0.7, cites: [{source: S1, locator: "'Works'"}], how_known: "Britannica."}
  occupations: {value: ["philosopher", "jurist", "physician", "communal leader"], certainty: 0.7, cites: [{source: S1, locator: "opening; 'Life'"}], how_known: "Britannica."}

contribution:
  era_bucket: medieval
  fields: {value: ["Jewish law", "philosophy", "medicine"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Commentary on the Mishna, with the creed of Thirteen Articles of Faith", year: 1168, kind: work, lasting: "creed 'became part of the orthodox liturgy' (S1)", certainty: 0.5, cites: [{source: S1, locator: "'Works'; 'Significance'"}], how_known: "Completed at 33 (derived year)."}
    - {value: "Mishne Torah (code of Jewish law)", kind: work, lasting: "'a brilliant systematization of all Jewish law and doctrine' (S1)", certainty: 0.7, cites: [{source: S1, locator: "'Works'"}], how_known: "Ten years after the commentary; no exact year given (P39)."}
    - {value: "The Guide for the Perplexed", year: 1191, kind: work, lasting: "'exerted a marked influence on the history of religious thought' (S1)", certainty: 0.5, cites: [{source: S1, locator: "'Works'"}], how_known: "Begun 1176 and laboured on for 15 years: 1176 + 15 = 1191 (derived, 0.5)."}
  evidence_of_impact:
    - {value: "Influenced the Scholastics, Spinoza and Leibniz", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "'Significance'"}], how_known: "Britannica."}
  major_works:
    - {value: "Commentary on the Mishna (with Thirteen Articles of Faith)", year: 1168, kind: "book", certainty: 0.5, cites: [{source: S1, locator: "'Works'"}, {source: S7, locator: "Works"}], how_known: "Completed at age 33 (derived year)."}
    - {value: "Mishneh Torah (incl. Yesodei haTorah)", kind: "book", certainty: 0.7, cites: [{source: S1, locator: "'Works'"}, {source: S5, locator: "Yesodei haTorah ch. 1"}], how_known: "Two sources."}
    - {value: "The Guide for the Perplexed (Dalālat al-Ḥāʾirīn / Moreh Nevukhim)", year: 1190, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "'Works'"}, {source: S6, locator: "completed 1190"}, {source: S7, locator: "Guide"}], how_known: "SEP 1190; Britannica ~1191 derived; Wikipedia."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "'the foremost intellectual figure of medieval Judaism' (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Jewish", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica."}
  family_religious_practice: {value: "Practised Judaism privately while appearing Muslim in public under the Almohads, from 1148", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica."}
  parents_and_household:
    - {value: "Father Maimon, a learned man and his first teacher", role: father, certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica."}
  household_circumstances: {value: "Distinguished family; persecution after the Almohad capture of Córdoba (1148)", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica."}
  schooling:
    - {value: "Studied with his father and other masters; Judaic studies and the sciences", stage: tutor, run_by: family, certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: TODO}
  notable_events:
    - {value: "Almohads capture Córdoba", year: 1148, age: 13, certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica; age 1148 − 1135."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1168–1191", certainty: 0.5, cites: [{source: S1, locator: "'Works'"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Judaism (rabbinic)", certainty: 0.7, cites: [{source: S1, locator: "opening; 'Significance'"}], how_known: "Britannica."}
  self_described_science_religion_relation: {value: "Agrees 'with Aristotle in one half of his theory' (the universe keeps its properties) but holds it had a beginning; Aristotle's eternity would oppose 'the foundation of our religion'.", certainty: 0.7, cites: [{source: S2, locator: "Part II, chs. XXV and XXIX"}], how_known: "Published work in a web-copy translation."}
  primary_system:
    value: JUDA
    basis: written_profession
    certainty: 0.7
    cites: [{source: S2, locator: "Part II, ch. XXV"}, {source: S4, locator: "חלק ב פרק כה / כט"}, {source: S5, locator: "Yesodei haTorah 1"}, {source: S1, locator: "'Works'; 'Significance'"}]
    rationale: "Creation, revelation and miracles as foundation of the religion (Guide II.25/29 EN+HE); Yesodei haTorah 1 commands knowledge of the First Existent; author of Thirteen Articles and Mishneh Torah (S1)."
    how_known: "Guide Friedländer + Ibn Tibbon Hebrew + Yesodei; 0.7 web-copy cap."
  secondary_system: {value: ARIST, certainty: 0.5, basis: written_profession, cites: [{source: S2, locator: "Part II, ch. XXIX"}, {source: S4, locator: "חלק ב פרק כט: נאות לאריסטו בחצי מדעתו"}], rationale: "Half-agreement with Aristotle on a stable created order (EN+HE).", how_known: "Coder's reading of a partial agreement, 0.5."}
  candidate_codes_considered:
    - {code: JUDA, reason: "Chosen."}
    - {code: ARIST, reason: "Secondary: half-agreement with Aristotle on a stable universe."}
  lio_axes:
    A_locus:
      value: 0
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S2, locator: "Part II, chs. XXV and XXIX"}, {source: S4, locator: "חלק ב פרק כה–כט"}, {source: S5, locator: "Yesodei haTorah 1:1–7 (מצוי ראשון; שאינו גוף)"}]
      how_known: "Guide EN (Friedländer) + Guide HE (Ibn Tibbon) + Mishneh Torah Yesodei. Web copies → 0.7. Independent streams → support corroborated (P48)."
      rationale: "Creator distinct from the universe: Guide — power to change/annihilate the whole; creation makes revelation and miracles possible (II.25/29). Yesodei 1: foundation is to know there is a First Existent who brings forth all else; He is not a body. Named alternative: 1 (incorporeal Primal Cause read in Aristotelian terms)."
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S2, locator: "Part II, ch. XXIX"}, {source: S4, locator: "חלק ב פרק כט (לא ישתנה … אלא בפרטיו על צד המופת; עולם כמנהגו הולך; זהו דעתי)"}]
      how_known: "Guide EN Friedländer + HE Ibn Tibbon (independent translation streams of the same chapter). Web copies → 0.7. Support corroborated (P48)."
      rationale: "P27 B 3 anchor, rare past miracles: universe keeps created properties 'except by way of miracle in some individual instances' (Friedländer); Hebrew: existence eternal on this nature God willed — nothing changes except in particulars by way of מופת; rod/water/hand changes 'לא ימשכו' and 'עולם כמנהגו הולך' — 'זהו דעתי'. Sages' built-in-miracle view reported, not claimed as his sole view. Named alternative: 4 (if built-in view is read as his own)."
    C_ledger: {value: UNKNOWN, how_known: "Not read."}
    D_authority: {value: UNKNOWN, how_known: "Ch. XXV says the eternity theory 'has not been proved' and so 'we take the text of the Bible literally'; this concerns unproved theory, not observation against revelation. Not scored."}
    E_scope: {value: UNKNOWN, how_known: "Not read (P7)."}
  mid_basin: {value: true, certainty: 0.7, cites: [{source: S2, locator: "Part II, chs. XXV, XXIX"}, {source: S4, locator: "חלק ב פרק כה–כט"}], how_known: "A 0 (≤ 1) and B 3 (≥ 3), both at 0.7; support now corroborated on both axes (P48 fill)."}
  statements:
    - text: "For we believe that this Universe remains perpetually with the same properties with which the Creator has endowed it, and that none of these will ever be changed except by way of miracle in some individual instances, although the Creator has the power to change the whole Universe, to annihilate it, or to remove any of its properties."
      cites: [{source: S2, locator: "Part II, ch. XXIX"}, {source: S4, locator: "חלק ב פרק כט (Hebrew parallel)"}]
      context: "After discussing the Sages' view of miracles."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Friedländer via Gutenberg #73584; corroborated by Ibn Tibbon Hebrew (S4)."
    - text: "שאנחנו נאות לאריסטו בחצי מדעתו ונאמין שזה המציאות לעולם נצחי על זה הטבע אשר רצהו ית' לא ישתנה ממנו דבר בשום פנים אלא בפרטיו על צד המופת — אף על פי שיש לו ית' היכולת לשנותו כולו או להעדירו … זהו דעתנו ויסוד תורתנו."
      cites: [{source: S4, locator: "חלק ב פרק כט"}, {source: S2, locator: "Part II, ch. XXIX (Friedländer parallel)"}]
      date: "1190"
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Ibn Tibbon Hebrew of Guide II.29; primary-language stream vs Friedländer EN."
    - text: "כי אף על פי שנהפך המטה לנחש ונהפכו המים לדם והיד הטהורה הנכבדת — לבנה מבלתי סיבה טבעית מחיבת אותם — העניינים ההם והדומה להם לא ימשכו ולא שבו טבע אחר אבל כמו שאמרו ז״ל עולם כמנהגו הולך. זהו דעתי והוא שצריך שיאמן."
      cites: [{source: S4, locator: "חלק ב פרק כט"}, {source: S2, locator: "Part II, ch. XXIX (rod / blood / hand; 'This is my opinion')"}]
      date: "1190"
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
    - text: "Accepting the Creation, we find that miracles are possible, that Revelation is possible, and that every difficulty in this question is removed."
      cites: [{source: S2, locator: "Part II, ch. XXV"}, {source: S4, locator: "חלק ב פרק כה (עם האמנת חידוש העולם יהיו האותות כולם אפשריות)"}]
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
    - text: "יסוד היסודות ועמוד החכמות, לידע שיש שם מצוי ראשון. והוא ממציא כל הנמצא; וכל הנמצאים מן שמיים וארץ ומה ביניהם, לא נמצאו אלא מאמיתת הימצאו."
      cites: [{source: S5, locator: "Yesodei haTorah 1:1"}]
      date: "1180"
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Mishneh Torah; independent work stream from the Guide."
    - text: "שאינו גוף וגווייה, יתבאר שלא יארעו ולא אחד ממאורעות הגוף…"
      cites: [{source: S5, locator: "Yesodei haTorah 1 (incorporeality)"}]
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
  changes_over_life: []
  coder_notes: "Deepen D1: A 0 @ 0.7 support corroborated (S2+S4+S5); B 3 @ 0.7 support corroborated (S2+S4). Pines unread. No fallacy_catalog."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Andalusian Jewish", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: "Jewish", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1168–1191", certainty: 0.5, cites: [{source: S1, locator: "'Works'"}], how_known: "First to last dated (derived) contribution (P29, P30)."}
  age_at_first_lasting_contribution: {value: 33, certainty: 0.7, cites: [{source: S1, locator: "'Works'"}], how_known: "Britannica: completed at the age of 33."}
  first_evidence_of_lio_type_views: {value: "Yesodei haTorah 1 (First Existent / incorporeal); Guide II.29 for B", year: 1180, certainty: 0.5, cites: [{source: S5, locator: "Yesodei 1"}, {source: S2, locator: "Part II, ch. XXIX"}, {source: S6, locator: "Guide completed 1190"}], how_known: "Yesodei earlier in Mishneh Torah decade; Guide ~1190 (SEP). Years approximate."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.5, cites: [{source: S1, locator: "'Works'"}], how_known: "The Guide is itself a major work."}
  worldview_during_major_work: {value: "JUDA", certainty: 0.7, cites: [{source: S2, locator: "Part II, ch. XXV"}], how_known: "As primary_system."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Not read.", certainty: 0.5, cites: [{source: S1, locator: "'Works'"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "'Life'"}], how_known: "Not read."}
  circle_present: {value: "yes", rationale: "Creator outside the world; created order runs regularly (עולם כמנהגו הולך) with rare past מופת exceptions.", certainty: 0.7, cites: [{source: S2, locator: "Part II, ch. XXIX"}, {source: S4, locator: "חלק ב פרק כט"}], how_known: "Coder's reading of EN+HE."}
  reading: "Creator plus stable created order with rare miracles."
  notes: ""

institutions:
  - {value: "Court of Saladin and al-Afḍal", role: "court physician", kind: "government or state body", certainty: 0.7, cites: [{source: S1, locator: "'Life'"}], how_known: "Britannica."}
collaborators:
  - {value: "Joseph ibn ʿAqnīn", relation: "student or assistant", note: "the Guide was sent to him as a private communication", certainty: 0.7, cites: [{source: S1, locator: "'Works'"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 55"}], how_known: "Study roster."}
  controversies:
    - {value: "The Guide was burned by church authorities at Montpellier in 1233 at a rabbi's instigation", certainty: 0.7, cites: [{source: S1, locator: "'Significance'"}], how_known: "Britannica."}
  data_quality_flags:
    - "Axis quotes rest on unofficial web copies (Gutenberg Friedländer; Wikisource Ibn Tibbon; Mechon-mamre Yesodei); certainties capped at 0.7."
    - "Britannica S1 re-access Cloudflare/403 on 2026-10-24; prior Bokser signed-body read retained."
    - "Birth year 1135 vs 1138 contested (Wikipedia); Britannica 1135-03-30 kept."
  open_questions:
    - "Pines (1963) or Goodman–Lieberman (2024) Guide translation for a third EN stream."
    - "Judeo-Arabic Dalālat critical edition (poor IA OCR this pass)."
    - "C/D/E lanes unread."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Ben Zion Bokser"
    citation: "Bokser, Ben Zion. 'Moses Maimonides.' Encyclopaedia Britannica, updated 21 September 2026. https://www.britannica.com/biography/Moses-Maimonides."
    url: "https://www.britannica.com/biography/Moses-Maimonides"
    accessed: 2026-10-15
    reliability_note: "Signed article body ('Life', 'Works', 'Significance'); Top Questions not cited. Re-access Cloudflare/403 on 2026-10-24; prior Bokser read retained."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, institutions, collaborators, review]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "Moses Maimonides; trans. M. Friedländer"
    citation: "Maimonides, Moses. The Guide for the Perplexed. Trans. M. Friedländer. Second edition, revised throughout. Project Gutenberg eBook #73584."
    url: "https://www.gutenberg.org/ebooks/73584"
    accessed: 2026-10-24
    reliability_note: "Translation from the Arabic in an unofficial web copy; §7 / P47 cap 0.7. Part II chs. XXV and XXIX rechecked this pass."
    source_quality: "unofficial web copy"
    used_for: [worldview, timing, lane_b]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "Moses Maimonides; Hebrew trans. Samuel ibn Tibbon"
    citation: "Maimonides, Moses. Moreh Nevukhim (Guide of the Perplexed), Part II chs. 25 and 29. Hebrew translation of Samuel ibn Tibbon. Wikisource."
    url: "https://he.wikisource.org/wiki/%D7%9E%D7%95%D7%A8%D7%94_%D7%A0%D7%91%D7%95%D7%9B%D7%99%D7%9D_(%D7%90%D7%91%D7%9F_%D7%AA%D7%99%D7%91%D7%95%D7%9F)/%D7%97%D7%9C%D7%A7_%D7%91/%D7%A4%D7%A8%D7%A7_%D7%9B%D7%98"
    accessed: 2026-10-24
    reliability_note: "Medieval Hebrew translation of the Judeo-Arabic Guide; independent language stream from Friedländer EN. Unofficial web copy (Wikisource)."
    source_quality: "primary / own words"
    used_for: [worldview, timing, lane_b]
  - id: S5
    type: primary
    kind: "published work by the subject"
    author: "Moses Maimonides"
    citation: "Maimonides, Moses. Mishneh Torah, Sefer Madda, Hilkhot Yesodei haTorah, chapters 1 and 8. Mechon Mamre digital Hebrew text. https://www.mechon-mamre.org/i/1101.htm"
    url: "https://www.mechon-mamre.org/i/1101.htm"
    accessed: 2026-10-24
    reliability_note: "Hebrew legal code in Maimonides' own Hebrew; unofficial web edition (Mechon Mamre). Used for A (First Existent; incorporeality), not for B scoring."
    source_quality: "primary / own words"
    used_for: [worldview, contribution]
  - id: S6
    type: secondary
    kind: encyclopedia
    author: "Kenneth Seeskin"
    citation: "Seeskin, Kenneth. 'Maimonides.' Stanford Encyclopedia of Philosophy. https://plato.stanford.edu/entries/maimonides/."
    url: "https://plato.stanford.edu/entries/maimonides/"
    accessed: 2026-10-24
    reliability_note: "Peer-reviewed reference entry; Guide completion 1190; Thirteen Principles summary; not used alone for axis scores."
    source_quality: "reference entry"
    used_for: [contribution, timing, worldview]
  - id: S7
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia contributors. 'Maimonides.' Wikipedia. https://en.wikipedia.org/wiki/Maimonides."
    url: "https://en.wikipedia.org/wiki/Maimonides"
    accessed: 2026-10-24
    reliability_note: "Dual-source biography: death Fustat 12 Dec 1204; birth year 1135/1138 contested; Tiberias tomb. Not used alone for axis scores."
    source_quality: "other"
    used_for: [identity, basics, contribution, timing]
---

# Maimonides

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Moses Maimonides (1135–1204), Jewish philosopher, jurist and physician [S1; S7]. Deepen D1 (P47–P50): primary_system JUDA 0.7; A 0 at 0.7 written_profession, support corroborated (S2+S4+S5; alt 1); B 3 at 0.7 written_profession, support corroborated (S2+S4; alt 4); mid_basin true at 0.7. Chart: dark hollow → dark filled (fill cue).

## Life and work

Córdoba; Fez; al-Fusṭāṭ (Fustat); physician to Saladin; died Fustat 1204, buried Tiberias [S1; S7].

## Contribution and impact

Mishna commentary, Mishne Torah, Guide for the Perplexed [S1].

## Childhood and education

Taught by his father; persecution under the Almohads [S1].

## Adult working worldview

Guide II.29: universe keeps created properties except by miracle in individual instances; Hebrew: לא ישתנה … אלא בפרטיו על צד המופת; עולם כמנהגו הולך — זהו דעתי [S2; S4]. Yesodei 1: מצוי ראשון ממציא כל הנמצא; שאינו גוף [S5]. A 0 / B 3 at 0.7, both support corroborated.

## Heritage (context only)

Andalusian Jewish [S1].

## Timing

First lasting contribution 1168 (derived), at 33 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Circle present [S2].

## Open questions

- Pines (1963) / Goodman–Lieberman (2024) Guide; Judeo-Arabic critical edition; C/D/E unread.

## Research log

- 2026-10-15: Read Britannica (Bokser) and Guide Part II chs. XXV, XXIX (Gutenberg #73584).
- 2026-10-24 (deepen D1, queue #55): Ibn Tibbon Hebrew Moreh II.25/29 (S4 Wikisource); Yesodei haTorah 1 & 8 (S5 Mechon-mamre); SEP (S6); Wikipedia (S7). Britannica 403. P47 on S1–S7; A and B support single→corroborated; values stay 0.7. Chart-moving YES (fill only). No fallacy_catalog (Jason).
