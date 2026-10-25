---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA4)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #182, F 3, rank 193). Hunt: firm AGNOS/A from Autobiography + Three Essays on Religion with composition timing (Helen Taylor: Nature and Utility of Religion composed 1850–1858, in span; Theism 1868–1870, after span; all published posthumously 1874). New primary: Nature (S5) and Utility of Religion (S6) via UT Austin Classical Utilitarianism transcription of 1874 Longmans text; Helen Taylor Introductory Notice (S7) for dating; Wikipedia EN Mill + Three Essays (S8, S9) dual bio / composition corroboration (P50). primary_system AGNOS 0.5→0.7 written_profession (in-span Nature/Utility + Autobiography corroboration); named alt SECHUM (Religion of Humanity). A stays BELOW_THRESHOLD (P20/P38: suspension, no 'I do not believe in God'; Nature's limited-power design phrase + Theism limited-creator reading are leads only — do not force A up). B stays UNKNOWN (philosopher not scientist P30; Logic Book III unread; do not force B from method-of-science or Nature's moral critique of imitating nature). mid BELOW_THRESHOLD; not plotted. Chart-moving NO. Dual bio P50; P47 source_quality on S1–S9; death day Britannica 8 May vs Wikipedia 7 May → 0.5 contested (P25). No fallacy_catalog. No figures/. Draft, not reviewed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "AA4 audit fix (v8's call on the auditor's advice): span certainty lowered to 0.5 (On Liberty lasting only at 0.5), alternative 1843 alone; the 1858 end of his India House post is now cited to the Autobiography (ch. III, ch. VII) and the 'Company's dissolution' wording is dropped."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA4, order P32: F 3, rank 193). Sources: Britannica, signed by Richard Paul Anschutz (main article; the fetched copy covers the summary and 'Early life and career' only), Britannica students edition (read in full) for publication years, and his Autobiography (1873; Project Gutenberg transcription, chapter 2 read). Lasting work: A System of Logic (1843) and On Liberty (1859); Anschutz: 'remains of lasting interest as a logician and an ethical theorist'; span 1843–1859, age 37 (span 0.5 after the AA4 audit, as On Liberty is lasting only at 0.5). Own words: Autobiography ch. 2, 'one who has not thrown off religious belief, but never had it: I grew up in a negative state with regard to it', with his father's teaching that 'Who made me?' 'cannot be answered'. Published 1873, after the span and describing his upbringing, so P20 caps it at 0.5. primary_system AGNOS 0.5 (written_profession), alt BELOW_THRESHOLD (the passage reports absence of belief, not a settled stance; his posthumous Theism, not read, is a lead the other way). A BELOW_THRESHOLD (no locus stated); philosopher, not a scientist, B UNKNOWN; C, D, E UNKNOWN; mid_basin BELOW_THRESHOLD (Pavlov pattern). Not plotted. Draft, not reviewed."}

identity:
  id: mill-john-stuart
  display_name: "John Stuart Mill"
  roster:
    canonical_name: "John Stuart Mill"
    rank: 193
    F: 3
    models: [Claude, DeepSeek, Grok]
    band: "core (3–4)"
    status: "core"
    field: "philosophy"
    field_bucket: "philosophy"
  full_name: {value: "John Stuart Mill", certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S8, locator: "infobox"}], how_known: "Britannica + Wikipedia EN (P50 dual bio)."}
  native_name: {value: "John Stuart Mill", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  aliases: []

basics:
  birth:
    date: {value: "1806-05-20", certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S8, locator: "infobox"}], how_known: "Britannica + Wikipedia EN."}
    place: {value: "Pentonville, London", modern_name: "London, United Kingdom", polity_then: "United Kingdom of Great Britain and Ireland", certainty: 1.0, cites: [{source: S1, locator: "Early life and career"}, {source: S8, locator: "infobox"}], how_known: "Britannica + Wikipedia EN (Pentonville, Middlesex)."}
  death:
    date: {value: "1873-05-08", certainty: 0.5, cites: [{source: S1, locator: "Introduction"}, {source: S8, locator: "infobox"}], how_known: "Britannica 'May 8, 1873'; Wikipedia '7 May 1873' — day contested (P25); year and month agree."}
    place: {value: "Avignon", modern_name: "Avignon, France", polity_then: "French Third Republic", certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S8, locator: "infobox"}], how_known: "Britannica + Wikipedia EN."}
  first_lasting_contribution_year: {value: 1843, certainty: 0.7, cites: [{source: S3, locator: "para. 4"}], how_known: "'He published his System of Logic (1843)' (S3); publication (P30 #1)."}
  era_bucket: {value: "1750 to 1849", certainty: 0.7, cites: [{source: S3, locator: "para. 4"}], how_known: "Keyed on the first lasting year, 1843 (P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "United Kingdom (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "Early life and career"}], how_known: "London, India House."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["English"], certainty: 0.7, cites: [{source: S3, locator: "para. 4"}], how_known: "English books."}
  occupations: {value: ["philosopher", "economist", "civil servant", "member of Parliament"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S3, locator: "para. 3–4"}, {source: S8, locator: "lead"}], how_known: "Britannica + Wikipedia."}

contribution:
  fields: {value: ["logic", "ethics", "political philosophy", "political economy"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "A System of Logic (inductive methods)", year: 1843, kind: "work", lasting: "'remains of lasting interest as a logician' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S3, locator: "para. 4"}], how_known: "Anschutz; published 1843 (S3)."}
    - {value: "On Liberty", year: 1859, kind: "work", lasting: "'remains of lasting interest as ... an ethical theorist' (S1); listed among his notable works (S1)", certainty: 0.5, cites: [{source: S1, locator: "Introduction"}, {source: S3, locator: "para. 4"}], how_known: "Published 1859 (S3). Anschutz's lasting phrase is about him as an ethical theorist, not this book by name, so 0.5."}
  evidence_of_impact:
    - {value: "'Remains of lasting interest as a logician and an ethical theorist'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Anschutz."}
  major_works:
    - {value: "Principles of Political Economy", year: 1848, kind: "book", certainty: 0.7, cites: [{source: S3, locator: "para. 4"}], how_known: "Britannica students."}
    - {value: "The Subjection of Women", year: 1869, kind: "book", certainty: 0.7, cites: [{source: S3, locator: "para. 4"}], how_known: "Britannica students."}
    - {value: "Three Essays on Religion (Nature; Utility of Religion; Theism)", year: 1874, kind: "book", certainty: 0.7, cites: [{source: S7, locator: "Introductory Notice"}, {source: S9, locator: "lead"}], how_known: "Posthumous 1874; Nature and Utility composed 1850–1858; Theism 1868–1870 (S7, S9). Not a lasting-contribution item for span end."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Lasting as logician and ethical theorist (S1).", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "none in household (father had rejected Scotch Presbyterianism)", certainty: 0.7, cites: [{source: S2, locator: "ch. 2"}], how_known: "Autobiography: brought up without religious belief."}
  family_religious_practice: {value: "no religious instruction; father taught that the origin of things is unknowable", certainty: 0.7, cites: [{source: S2, locator: "ch. 2"}], how_known: "Autobiography."}
  parents_and_household:
    - {value: "Eldest son of James Mill, historian, economist and philosopher, who educated him exclusively", role: "father", certainty: 0.7, cites: [{source: S1, locator: "Early life and career"}, {source: S8, locator: "Early life"}], how_known: "Britannica + Wikipedia."}
    - {value: "Mother Harriet Barrow (Wikipedia); household detail beyond father's tutoring not scored", role: "mother", certainty: 0.5, cites: [{source: S8, locator: "infobox"}], how_known: "Wikipedia only."}
    - {value: "Brought up 'without any religious belief'; his father, raised a Scotch Presbyterian, held that 'concerning the origin of things nothing whatever can be known'", role: "family", certainty: 0.7, cites: [{source: S2, locator: "ch. 2"}], how_known: "Autobiography."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated beyond father's intensive home education."}
  schooling:
    - {value: "Educated at home by his father", stage: "tutor", run_by: other, certainty: 0.7, cites: [{source: S1, locator: "Early life and career"}, {source: S8, locator: "Early life"}], how_known: "Britannica + Wikipedia."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated in sources read this pass."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "James Mill", role: "father / tutor", certainty: 0.7, cites: [{source: S1, locator: "Early life and career"}], how_known: "Britannica."}
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1843–1859", certainty: 0.5, cites: [{source: S3, locator: "para. 4"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No scored own-voice science–religion relation line beyond Logic method (not read for that) and Nature/Utility on supernatural credentials."}
  primary_system:
    value: AGNOS
    basis: written_profession
    certainty: 0.7
    cites: [{source: S5, locator: "closing; limited power / design"}, {source: S6, locator: "evidences insufficient; Religion of Humanity; hypotheses cannot be known to be false"}, {source: S2, locator: "ch. 2"}, {source: S7, locator: "composition 1850–1858"}]
    how_known: "Nature and Utility of Religion composed 1850–1858 (Helen Taylor S7), inside the working span, though published 1874; unofficial web transcription of the 1874 text (0.7 ceiling). Autobiography (1873) corroborates lifelong 'never had' religious belief and origin-unknowable teaching."
    rationale: "Explicit suspension / non-reliance on supernatural religion during the working years: Utility treats religion's supernatural credentials as 'so insufficient' that they fail many of the strongest minds and advances a Religion of Humanity that can fulfil religion's functions without supernatural belief; it allows imaginative theistic 'hypotheses which cannot be known to be false' without asserting them (S6). Nature rejects nature-as-moral-standard and holds that any beneficent design in nature implies only limited power (S5). Autobiography: he 'never had' religious belief and grew up knowing 'Who made me?' 'cannot be answered' (S2). Named alternative SECHUM: Religion of Humanity is the constructive proposal in Utility (S6) but his metaphysics is suspension/unknowability, not a humanist-movement public identity. Theism (composed 1868–1870, after span; published 1874) limited-creator reading is a lead only — Helen Taylor reports he held the essays fundamentally consistent (S7); do not recode primary or force A up."
  secondary_system: {value: UNKNOWN, how_known: "SECHUM kept as named alternative on primary, not scored as secondary."}
  candidate_codes_considered:
    - {code: AGNOS, reason: "Coded at 0.7: in-span Nature/Utility + Autobiography corroboration."}
    - {code: SECHUM, reason: "Named alternative: Religion of Humanity in Utility (S6); not chosen as primary (metaphysics is suspension, not movement identity)."}
    - {code: ATHE, reason: "Rejected: no in-span 'I do not believe in God'; Utility leaves imaginative God-hypotheses open (S6); P38 would cap A 4 at 0.5 even if such a line existed alongside AGNOS."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "P20: agnostic / suspension with no stated locus. Autobiography: 'Who made me?' 'cannot be answered' (S2). Utility: supernatural evidences insufficient; theistic hypotheses planted as imagination-possibilities 'which cannot be known to be false' — not a locus claim (S6). Nature: if there is beneficent design, power is limited (S5) — lead toward A 1 / limited creator, not scored. Theism (1868–1870, after span) limited-creator reading likewise lead only. No 'I do not believe in God' → do not apply P38 A 4. A stays BELOW_THRESHOLD."}
    B_cause: {value: UNKNOWN, how_known: "Philosopher, not a scientist (P30): A System of Logic treats inductive method, not a lasting result about natural systems. Nature critiques imitating nature as a moral standard (S5) — not a P16 nature-order / law-and-exception claim for B. System of Logic Book III (causation) unread this pass. Do not force B from method-of-science alone."}
    C_ledger: {value: UNKNOWN, how_known: "Not scored this pass; Utility discusses posthumous rewards/punishments as weak inducements — lead only."}
    D_authority: {value: UNKNOWN, how_known: "Lead: duty of collecting and weighing evidence for himself (S1); not scored."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD, so the P4 test cannot be applied."}
  statements:
    - text: "I am thus one of the very few examples, in this country, of one who has not thrown off religious belief, but never had it: I grew up in a negative state with regard to it. I looked upon the modern exactly as I did upon the ancient religion, as something which in no way concerned me."
      cites: [{source: S2, locator: "ch. 2"}]
      date: "1873"
      context: "Autobiography, ch. 2, on his upbringing; published 1873, after the span (P20 retrospective; corroborates in-span Nature/Utility)."
      axes: [A_locus]
      kind: "autobiography"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Project Gutenberg eBook #10378; re-checked D1."
    - text: "he impressed upon me from the first, that the manner in which the world came into existence was a subject on which nothing was known: that the question, \"Who made me?\" cannot be answered, because we have no experience or authentic information from which to answer it"
      cites: [{source: S2, locator: "ch. 2"}]
      date: "1873"
      context: "Autobiography, ch. 2: his father's teaching, which he reports he grew up within."
      axes: [A_locus]
      kind: "autobiography"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "Reports father's teaching; backs AGNOS together with the first statement."
    - text: "the divine message, assuming it to be such, has been authenticated by credentials so insufficient, that they fail to convince a large proportion of the strongest and most cultivated minds, and the tendency to disbelieve them appears to grow with the growth of scientific knowledge and critical discrimination."
      cites: [{source: S6, locator: "Utility of Religion"}]
      date: "1858"
      context: "Utility of Religion; composed in span (Helen Taylor S7)."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "UT Austin Classical Utilitarianism site; 1874 Longmans text."
    - text: "This condition is fulfilled by the Religion of Humanity in as eminent a degree, and in as high a sense, as by the supernatural religions even in their best manifestations, and far more so than in any of their others."
      cites: [{source: S6, locator: "Utility of Religion"}]
      date: "1858"
      context: "Utility of Religion: Religion of Humanity as fulfilling religion's essence without supernatural belief (SECHUM lead)."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Supports SECHUM alternative; does not by itself place a locus."
    - text: "Apart from all dogmatic belief, there is for those who need it, an ample domain in the region of the imagination which may be planted with possibilities, with hypotheses which cannot be known to be false"
      cites: [{source: S6, locator: "Utility of Religion"}]
      date: "1858"
      context: "Utility of Religion: theistic/afterlife hypotheses as imaginative possibilities, not asserted truths — suspension-compatible."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Key AGNOS-compatible line; not a scored locus."
    - text: "Whatsoever, in nature, gives indication of beneficent design, proves this beneficence to be armed only with limited power; and the duty of man is to co-operate with the beneficent powers, not by imitating but by perpetually striving to amend the course of nature"
      cites: [{source: S5, locator: "Nature, closing"}]
      date: "1858"
      context: "Nature, leading conclusions; composed in span (S7). Lead toward limited-creator / A 1 — not scored as locus (do not force A up)."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Also: 'If the maker of the world can all that he will, he wills misery' (omnipotent-Creator critique in same essay)."
  changes_over_life:
    - {value: "Essay on Theism composed after the working span. Secondary accounts and the create-pass lead read it as more open to a limited creator / design hypothesis than Nature/Utility alone. Helen Taylor: Mill considered the three essays fundamentally consistent and intended to publish Nature in 1873. Not used to recode primary_system or A for the 1843–1859 span (P20/P31); lead only.", year: 1870, certainty: 0.5, cites: [{source: S7, locator: "Introductory Notice"}, {source: S9, locator: "Essays / Theism"}], how_known: "Helen Taylor: Theism written 1868–1870 (S7); Wikipedia corroborates (S9). Full Theism primary unread this pass."}
  coder_notes: "Theism full primary still unread this pass (UT Austin has Nature + Utility only). System of Logic Book III (causation) unread — B stays UNKNOWN. Do not refresh chart figures. No fallacy_catalog."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: "none (father had rejected Scotch Presbyterianism)", certainty: 0.7, cites: [{source: S2, locator: "ch. 2"}], how_known: "Autobiography."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated; upbringing without religious belief (S2)."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1843–1859", certainty: 0.5, cites: [{source: S3, locator: "para. 4"}], how_known: "From A System of Logic (1843) to On Liberty (1859), the listed lasting works (P29, P30 #1). 0.5 because On Liberty is lasting only at 0.5; alternative 1843 alone (v8's call on the auditor's advice, AA4)."}
  age_at_first_lasting_contribution: {value: 37, certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S3, locator: "para. 4"}], how_known: "1843 − 1806 = 37 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: "1850–1858 (Nature and Utility of Religion composed)", certainty: 0.7, cites: [{source: S5, locator: "Nature"}, {source: S6, locator: "Utility of Religion"}, {source: S7, locator: "Introductory Notice"}], how_known: "Helen Taylor: both essays written 1850–1858, between Principles of Political Economy and On Liberty (S7)."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.7, cites: [{source: S7, locator: "Introductory Notice"}], how_known: "Nature and Utility composed 1850–1858 inside 1843–1859; published 1874. Autobiography 1873 is after-span corroboration (P20)."}
  worldview_during_major_work: {value: "AGNOS (suspension / non-supernatural Religion of Humanity); A BELOW_THRESHOLD; B UNKNOWN", certainty: 0.7, cites: [{source: S5, locator: "Nature"}, {source: S6, locator: "Utility of Religion"}, {source: S2, locator: "ch. 2"}], how_known: "Coded above."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Inductive logic and ethics (S1); no geometric form claimed.", certainty: 0.5, cites: [{source: S1, locator: "Introduction"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No chart-moving A/B change this pass. Lane B only."
  notes: "Do not derive B from Logic method or Nature's moral critique of imitating nature."

institutions:
  - {value: "East India Company (India House)", role: "clerk; Examiner of India Correspondence from 1856", years: "1823–1858", kind: "employer", certainty: 0.7, cites: [{source: S1, locator: "Early life and career"}, {source: S2, locator: "ch. III; ch. VII"}], how_known: "Britannica (entered 1823; chief of the examiner's office 1856). Autobiography: he held the examinership 'a little more than two years' until Parliament ended the Company's government of India, which 'determined my retirement'; the winter of '1858-9' was 'the first after my retirement' (S2)."}
collaborators:
  - {value: "James Mill", relation: "family", note: "father and teacher", certainty: 0.7, cites: [{source: S1, locator: "Early life and career"}], how_known: "Britannica."}
  - {value: "Jeremy Bentham", relation: "influenced by", note: "utilitarianism", certainty: 0.7, cites: [{source: S1, locator: "Early life and career"}], how_known: "Britannica."}
  - {value: "Harriet Taylor Mill", relation: "family", note: "wife from 1851; helped revise On Liberty", certainty: 0.7, cites: [{source: S3, locator: "para. 3–4"}, {source: S8, locator: "infobox"}], how_known: "Britannica students + Wikipedia."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 193"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Nature/Utility composed in span, published 1874 posthumously — composition dating from Helen Taylor (S7)."
    - "Theism after span; unread in full this pass — limited-creator lead only."
    - "Death day contested (Britannica 8 May vs Wikipedia 7 May)."
  open_questions:
    - "Full primary read of Theism (1868–1870) for changes_over_life detail; do not move span A without P31 warrant."
    - "System of Logic Book III on causation for a possible B score (P16 nature-order)."
    - "Anschutz later Britannica sections / SEP John Stuart Mill for scholarly corroboration."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Richard Paul Anschutz"
    citation: "Anschutz, Richard Paul. 'John Stuart Mill.' Encyclopaedia Britannica. https://www.britannica.com/biography/John-Stuart-Mill"
    url: "https://www.britannica.com/biography/John-Stuart-Mill"
    accessed: 2026-10-19
    reliability_note: "Signed article; the fetched copy covers the summary and 'Early life and career' only."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, institutions, collaborators]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "John Stuart Mill"
    citation: "Mill, John Stuart. Autobiography (London, 1873). Project Gutenberg eBook #10378. https://www.gutenberg.org/ebooks/10378"
    url: "https://www.gutenberg.org/ebooks/10378"
    accessed: 2026-10-24
    reliability_note: "Transcription of the 1873 text; chapter 2 re-read D1. After-span retrospective; corroborates in-span Nature/Utility."
    source_quality: "primary / own words"
    used_for: [childhood, worldview, heritage, institutions]
  - id: S3
    type: tertiary
    kind: "encyclopedia"
    author: "Britannica Editors"
    citation: "'John Stuart Mill.' Britannica (students edition). https://kids.britannica.com/students/article/John-Stuart-Mill/275842"
    url: "https://kids.britannica.com/students/article/John-Stuart-Mill/275842"
    accessed: 2026-10-19
    reliability_note: "Encyclopedia article, read in full; unsigned."
    source_quality: "reference entry"
    used_for: [basics, contribution, timing]
  - id: S4
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [review]
  - id: S5
    type: primary
    kind: "published work by the subject"
    author: "John Stuart Mill"
    citation: "Mill, John Stuart. 'Nature.' In Three Essays on Religion (London: Longmans, Green, Reader, and Dyer, 1874; 2nd ed.). Classical Utilitarianism Web Site (UT Austin) transcription. https://www.laits.utexas.edu/poltheory/mill/three/nature.html"
    url: "https://www.laits.utexas.edu/poltheory/mill/three/nature.html"
    accessed: 2026-10-24
    reliability_note: "Unofficial web copy of 1874 text; composed 1850–1858 per Helen Taylor (S7). Read in full D1."
    source_quality: "unofficial web copy"
    used_for: [worldview, timing]
  - id: S6
    type: primary
    kind: "published work by the subject"
    author: "John Stuart Mill"
    citation: "Mill, John Stuart. 'The Utility of Religion.' In Three Essays on Religion (London: Longmans, Green, Reader, and Dyer, 1874; 2nd ed.). Classical Utilitarianism Web Site (UT Austin) transcription. https://www.laits.utexas.edu/poltheory/mill/three/utilrelig.html"
    url: "https://www.laits.utexas.edu/poltheory/mill/three/utilrelig.html"
    accessed: 2026-10-24
    reliability_note: "Unofficial web copy of 1874 text; composed 1850–1858 per Helen Taylor (S7). Read in full D1."
    source_quality: "unofficial web copy"
    used_for: [worldview, timing]
  - id: S7
    type: secondary
    kind: "published work by the subject"
    author: "Helen Taylor"
    citation: "Taylor, Helen. 'Introductory Notice.' In John Stuart Mill, Three Essays on Religion (London: Longmans, Green, Reader, and Dyer, 1874; 2nd ed.). Classical Utilitarianism Web Site (UT Austin). https://www.laits.utexas.edu/poltheory/mill/three/intro.html"
    url: "https://www.laits.utexas.edu/poltheory/mill/three/intro.html"
    accessed: 2026-10-24
    reliability_note: "Stepdaughter/editor; composition dates Nature & Utility 1850–1858, Theism 1868–1870; notes Mill intended to publish Nature in 1873 and held essays fundamentally consistent."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview, timing, contribution, review]
  - id: S8
    type: tertiary
    kind: "encyclopedia"
    author: "Wikipedia contributors"
    citation: "'John Stuart Mill.' Wikipedia (English). https://en.wikipedia.org/wiki/John_Stuart_Mill"
    url: "https://en.wikipedia.org/wiki/John_Stuart_Mill"
    accessed: 2026-10-24
    reliability_note: "P50 dual bio with S1. Birth/death/place; mother Harriet Barrow; religion overview (secondary paraphrase — not used alone to score)."
    source_quality: "reference entry"
    used_for: [identity, basics, childhood, collaborators, review]
  - id: S9
    type: tertiary
    kind: "encyclopedia"
    author: "Wikipedia contributors"
    citation: "'Three Essays on Religion.' Wikipedia (English). https://en.wikipedia.org/wiki/Three_Essays_on_Religion"
    url: "https://en.wikipedia.org/wiki/Three_Essays_on_Religion"
    accessed: 2026-10-24
    reliability_note: "Composition/publication dating corroborates Helen Taylor (S7); essay summaries only."
    source_quality: "reference entry"
    used_for: [contribution, worldview, timing, review]
---

## Summary

John Stuart Mill (1806–1873), philosopher and economist [S1, S8]. Deepen D1: AGNOS @0.7; A BELOW_THRESHOLD; B UNKNOWN. Not plotted.

## Life and work

London; India House; Avignon [S1, S8]. Death day contested (8 vs 7 May 1873).

## Contribution and impact

A System of Logic (1843); On Liberty (1859) [S1, S3]. Three Essays on Religion published 1874 (Nature/Utility composed 1850–1858) [S7, S9].

## Childhood and education

At home, by his father; without religious belief [S1, S2].

## Adult working worldview

AGNOS @0.7 from in-span Nature and Utility of Religion (composed 1850–1858) plus Autobiography corroboration [S5, S6, S2, S7]. A BELOW_THRESHOLD (suspension; no P38 disbelief line; limited-creator leads not scored). B UNKNOWN (not a scientist; Logic III unread). Religion of Humanity = SECHUM alternative. Theism after span — lead only.

## Heritage (context only)

No religion; father ex-Presbyterian [S2].

## Timing

1843–1859, age 37 [S3]. LIO evidence during span via Nature/Utility composition [S7].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No B from Logic method or Nature's moral critique.

## Open questions

- Full Theism primary; Logic Book III causation; Anschutz later sections / SEP.

## Research log

- 2026-10-24 (D1): Read Nature + Utility (UT Austin 1874 text); Helen Taylor intro; Wikipedia Mill + Three Essays. Firm AGNOS 0.5→0.7; A stays BELOW_THRESHOLD; B UNKNOWN. Chart-moving NO. No fallacy_catalog; no figures/.
- 2026-10-19: AA4 audit fix (v8's call on the auditor's advice): span certainty lowered to 0.5 (On Liberty lasting only at 0.5), alternative 1843 alone; the 1858 end of his India House post is now cited to the Autobiography (ch. III, ch. VII) and the 'Company's dissolution' wording is dropped.
- 2026-10-19: Read Britannica (Anschutz, partly; students); Autobiography ch. 2.
