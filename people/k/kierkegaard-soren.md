---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA9)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to philosophy. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen D1 (queue #205/228, F 3, rank 218): score A from signed Upbuilding Discourses / journals if clear; leave UNKNOWN/BELOW if still thin; do not force plot. Re-read SEP Lippitt/Evans (S1). Own-voice signed: Two Upbuilding Discourses 1843 via Hong quotations on Wikiquote (S4) — 'Every Good and Every Perfect Gift Is from Above' (James 1:17); expectancy 'not in the world but in God'. The Unchangeableness of God (delivered 1851, published 1855; Lowrie tr., S3) — 'In His omnipotence He created this visible world — and made Himself invisible'; 'father of lights' dwelling above, unchanged. Works of Love 1847 (Hong via Storm commentary quotations, S5) — signed Christian deliberations; 'God in heaven'; God as middle term. primary CHRIST scholarly_reconstruction 0.5 → written_profession 0.7. A UNKNOWN→0 @0.7 written_profession, support corroborated (S3+S4; P48); P42: Anti-Climacus / Sickness Unto Death still unused for A. B UNKNOWN→BELOW_THRESHOLD (not a scientist, P30; omnipotent-intervention language in S3 is theological, not a clear account of nature's lawfulness vs special cases at ≥0.5). Mid BELOW. Not plotted. P47 source_quality on all. No fallacy_catalog; figures not refreshed. Draft, not reviewed."}
    - {date: 2026-10-20, by: "Grok Bot", summary: "AA9 audit fixes: span certainty 0.7 (weakest-work rule); note that the P42 pseudonym treatment rests on analogy."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA9, order P32: F 3, rank 218). Source: SEP 'Søren Kierkegaard' (John Lippitt and C. Stephen Evans, 2023, read in full). Lasting: the authorship, 'almost all of which was written in the 1840s', from Either/Or (1843), which 'he considered properly to begin his authorship'; 'often dubbed the \"father of existentialism\"', it influenced Heidegger, Sartre, Jaspers, Wittgenstein and others (S1). Span 1843–1850 at 0.7 (Either/Or to Practice in Christianity), alternative 1843–1855 (The Moment), age 30. Worldview: CHRIST at 0.5 (scholarly_reconstruction; S1: 'known as a defender of Christian faith'; in [The Point of View], in his own voice, he 'claims that he was from first to last a religious author'; S1 paraphrase, not quoted). A UNKNOWN: the one quoted line on God (Sickness Unto Death) is pseudonymous (Anti-Climacus), so not his own voice (P42, applied by analogy: P42 has no explicit pseudonym clause; this follows its character-voice addendum). Not a scientist; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}

identity:
  id: kierkegaard-soren
  display_name: "Søren Kierkegaard"
  roster:
    canonical_name: "Søren Kierkegaard"
    rank: 218
    F: 3
    models: [Claude, Gemini, Grok]
    band: "core (3–4)"
    status: "core"
    field: "philosophy"
    field_bucket: "philosophy"
  full_name: {value: "Søren Aabye Kierkegaard", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}
  native_name: {value: "Søren Aabye Kierkegaard", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}
  aliases:
    - {name: "Soren Kierkegaard", kind: "transliteration"}

basics:
  birth:
    date: {value: "1813-05-05", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Works"}], how_known: "SEP."}
    place: {value: "Copenhagen", modern_name: "Copenhagen, Denmark", polity_then: "Denmark–Norway", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Works"}], how_known: "SEP."}
  death:
    date: {value: "1855-11-11", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Works"}], how_known: "SEP."}
    place: {value: "Copenhagen", modern_name: "Copenhagen, Denmark", polity_then: "Denmark", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Works"}], how_known: "SEP: died in hospital in Copenhagen."}
  first_lasting_contribution_year: {value: 1843, certainty: 0.7, cites: [{source: S1, locator: "1. Life and Works"}], how_known: "Either/Or 'was published in 1843' (S1); P30 publication."}
  era_bucket: {value: "1750 to 1849", certainty: 1.0, cites: [{source: S1, locator: "1. Life and Works"}], how_known: "1843 (P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Works"}], how_known: "Denmark (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Works"}], how_known: "Copenhagen."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Danish"], certainty: 0.7, cites: [{source: S1, locator: "Bibliography"}], how_known: "Works in Danish (SKS)."}
  occupations: {value: ["philosopher", "theologian", "writer"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}

contribution:
  primary_domain: philosophy
  fields: {value: ["philosophy", "theology", "psychology"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}
  lasting_original_contributions:
    - {value: "The authorship of 1843–1850 (pseudonymous and signed works, from Either/Or and Fear and Trembling to The Sickness Unto Death and Practice in Christianity)", year: 1843, kind: "body of work", lasting: "'often dubbed the \"father of existentialism\"'; it 'has certainly influenced thinkers in the phenomenological and existential traditions (including Heidegger, Sartre, Jaspers, Marcel, and Lévinas)' and Wittgenstein (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; 1. Life and Works"}], how_known: "Either/Or 1843 to Practice in Christianity 1850 (S1)."}
  evidence_of_impact:
    - {value: "Wittgenstein called him 'by far the most profound thinker' of the nineteenth century", kind: "assessment by a later major figure", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}
    - {value: "'father of existentialism'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP, which notes the label 'obscures at least as much as it reveals'."}
  major_works:
    - {value: "Either/Or", year: 1843, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Works"}], how_known: "SEP."}
    - {value: "Eighteen Upbuilding Discourses (signed; Two through Four, 1843–1844)", year: 1843, kind: "book", certainty: 0.7, cites: [{source: S4, locator: "Two Upbuilding Discourses, 1843 (Hong quotations)"}, {source: S1, locator: "1. Life and Works"}], how_known: "Signed discourses concurrent with Either/Or (S1; S4)."}
    - {value: "Concluding Unscientific Postscript", year: 1846, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Works"}], how_known: "SEP."}
    - {value: "Works of Love", year: 1847, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Works"}, {source: S5, locator: "title / foreword"}], how_known: "SEP; signed Christian deliberations (S5)."}
    - {value: "The Sickness Unto Death", year: 1849, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Works"}], how_known: "SEP; pseudonym Anti-Climacus (P42 — not used for A)."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Wide influence across philosophy, theology, literature and psychotherapy (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}

childhood:
  family_religion: {value: "Christian (Lutheran, with Moravian influence)", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Works"}], how_known: "SEP: brought up as a Lutheran; also shaped by a Moravian congregation."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated beyond heritage."}
  parents_and_household:
    - {value: "Father Michael Pedersen Kierkegaard, wealthy Copenhagen merchant, 'devoutly religious'; mother Anne (Lund); youngest of seven", role: "family", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Works"}], how_known: "SEP."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling:
    - {value: "University of Copenhagen: first degree in theology; Magister in philosophy (On the Concept of Irony); pastoral seminary, never ordained", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Works"}], how_known: "SEP."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1843–1850", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Works"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Lutheran (Danish state church); attacked the established church in the name of New Testament Christianity", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Works"}], how_known: "SEP; not used alone for primary_system."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not a scientist; no science–religion relation scored."}
  primary_system:
    value: CHRIST
    basis: written_profession
    certainty: 0.7
    cites: [{source: S4, locator: "Two Upbuilding Discourses, 1843 (Hong)"}, {source: S5, locator: "Works of Love, 1847 foreword / Christian reflections"}, {source: S3, locator: "The Unchangeableness of God (signed discourse)"}, {source: S1, locator: "1. Life and Works (Point of View paraphrase)"}]
    how_known: "Deepen D1: signed own-voice Christian discourses within/near the working years — Two Upbuilding Discourses 1843 (S4; James 1:17 gift-from-God discourse; faith expectancy in God not the world); Works of Love 1847 subtitled Christian deliberations, signed (S5); The Unchangeableness of God (delivered 1851 / published 1855; S3) is a signed Christian discourse with prayer and Scripture. SEP (S1): known as a defender of Christian faith; Point of View (own voice) claims he was from first to last a religious author; affirmed to Emil Boesen he was still a believer in Christ. Raised scholarly_reconstruction 0.5 → written_profession 0.7. Contested ceiling 0.7 held (Point of View unity contested among scholars, S1) — still CHRIST, not a rival code."
    rationale: "CHRIST: public written profession of Christian faith in signed upbuilding and Christian discourses; Lutheran state-church affiliation is nominal context, not the code by itself."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Coded; raised to written_profession 0.7 on signed discourses (S3–S5)."}
    - {code: CLASS_THEISM, reason: "Rejected as primary: his signed works are explicitly Christian (Christ, New Testament, Christian love), not bare classical theism."}
  lio_axes:
    A_locus:
      value: 0
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S3, locator: "The Unchangeableness of God (Lowrie tr.)"}, {source: S4, locator: "Two Upbuilding Discourses, 1843 — Expectancy of Faith; Every Good and Every Perfect Gift (Hong via Wikiquote)"}, {source: S5, locator: "Works of Love — God as middle term"}]
      how_known: "Signed discourses only (P42: Anti-Climacus / Sickness Unto Death unused). S3: 'In His omnipotence He created this visible world — and made Himself invisible. He clothed Himself in the visible world as in a garment; He changes it as one who shifts a garment — Himself unchanged'; speaks of a 'father of lights' who 'dwells above', unchangeable, sender of good and perfect gifts. S4 (1843, within span): James 1:17 discourse; 'my expectancy was not in the world but in God'; gifts received 'from his hand as a good and perfect gift'. S5: God as personal middle term in Christian love. Independent works → corroborated (P48). Named alternative 1 (God as middle term / present to the single individual) caps ≤0.7; alt cites stay inside main source set. Adult-life evidence after span end (1851 discourse) counts at normal certainty under P31 — no documented change away from personal Creator God."
      rationale: "Transcendent personal Creator (A 0): God created the visible world and remains distinct from it; Father of lights above; expectancy and gifts from God, not from the world. Alternative 1: strong inwardness / God as middle term in Works of Love could be read toward immanent presence without collapsing Creator into creation."
      alternatives:
        - {value: 1, note: "God as middle term / inward presence to the single individual (Works of Love), without world=God.", cites: [{source: S5, locator: "Works of Love — God as middle term"}]}
    B_cause: {value: BELOW_THRESHOLD, how_known: "Deepen D1: not a scientist (P30). S3 states omnipotent presence in every event and readiness to change everything — intervening special causation in theological discourse, not a clear scored account of nature's lawfulness vs special cases at ≥0.5 (P6/P19). Leave thin; do not force plot."}
    C_ledger: {value: UNKNOWN, how_known: "Not scored this pass."}
    D_authority: {value: UNKNOWN, how_known: "Not scored this pass."}
    E_scope: {value: UNKNOWN, how_known: "Not scored this pass."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "B_cause is BELOW_THRESHOLD, so the P4 test cannot be applied (Pavlov / Herschel pattern; P19)."}
  statements:
    - text: "In His omnipotence He created this visible world — and made Himself invisible. He clothed Himself in the visible world as in a garment; He changes it as one who shifts a garment — Himself unchanged. … He speaks of a 'father of lights', who dwells above, with whom there is no variableness, not even the shadow of any change. He speaks of good and perfect gifts that come to us from above, from this father…"
      cites: [{source: S3, locator: "The Unchangeableness of God (Lowrie tr.)"}]
      date: "1851"
      context: "Signed discourse delivered Citadel Church 18 May 1851; published 1855 during the attack on Christendom. Favorite James 1:17 text he says he used from the first. Creator distinct from the visible world."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Lowrie English via jesuswords.net archive of Attacks on Christendom materials; delivery 1851 (just after span end 1850) counts under P31."
    - text: "There is an expectancy that the whole world cannot take from me; it is the expectancy of faith, and this is victory. I am not deceived, since I did not believe that the world would keep the promise it seemed to be making to me, my expectancy was not in the world but in God."
      cites: [{source: S4, locator: "Two Upbuilding Discourses, 1843 — The Expectancy of Faith (Hong, Eighteen Upbuilding Discourses pp. 23–24 via Wikiquote)"}]
      date: "1843"
      context: "Signed Two Upbuilding Discourses (16 May 1843), concurrent with Either/Or. Expectancy grounded in God, not the world."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Hong English quotations as hosted on Wikiquote (Two Upbuilding Discourses, 1843)."
    - text: "When you had doubts about what came from God or about what was a good and perfect gift, did you risk the venture? … Did you thank God? … have you taken the wrong and insult to God and by your thanksgiving received it from his hand as a good and perfect gift?"
      cites: [{source: S4, locator: "Two Upbuilding Discourses, 1843 — Every Good and Every Perfect Gift Is from Above (Hong p. 43 via Wikiquote)"}]
      date: "1843"
      context: "Signed discourse on James 1:17; gifts from God's hand."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
    - text: "These are Christian reflections; therefore they are not about love but about the works of love."
      cites: [{source: S5, locator: "Works of Love, foreword (Hong 1962 via Storm commentary, p. 19)"}]
      date: "1847"
      context: "Signed Works of Love — Christian deliberations; own-voice Christian framing for primary_system."
      axes: []
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Used for CHRIST written_profession; not alone for A."
    - text: "Worldly wisdom thinks that love is a relationship between man and man. Christianity teaches that love is a relationship between: man-God-man, that is, that God is the middle term."
      cites: [{source: S5, locator: "Works of Love (Hong via Storm commentary, p. 112f.)"}]
      date: "1847"
      context: "Signed; God as personal middle term in Christian love — supports A 0 with named alt 1."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24

  changes_over_life: []
  coder_notes: "Deepen D1: P42 — prefer signed discourses; Anti-Climacus unused for A. Lane A public-record only. B left BELOW (thin theological intervention language, not a nature account). Do not force plot. Unchangeableness 1851 delivery is just after span end 1850; P31 allows it; 1843 discourses already carry A within span."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: "Christian (Lutheran, with Moravian influence)", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Works"}], how_known: "SEP: 'brought up as a Lutheran but was also shaped by a Moravian congregation'."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1843–1850", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Works"}], how_known: "The body of work runs from Either/Or (1843) to Practice in Christianity (1850) (P29, P30); 0.7, following the one lasting item (AA4 weakest-work rule); both ends are dated in S1. Alternative 1843–1855 (the 1854–55 attack on the church, The Moment)."}
  age_at_first_lasting_contribution: {value: 30, certainty: 0.7, cites: [{source: S1, locator: "1. Life and Works"}], how_known: "1843 − 1813 = 30 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: "1843", certainty: 0.7, cites: [{source: S4, locator: "Two Upbuilding Discourses, 1843"}], how_known: "Signed Two Upbuilding Discourses (May 1843) place expectancy in God not the world; James 1:17 gift discourse."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.7, cites: [{source: S4, locator: "1843 discourses"}, {source: S5, locator: "Works of Love 1847"}], how_known: "Signed discourses inside the 1843–1850 span; 1851 Unchangeableness counts under P31."}
  worldview_during_major_work: {value: "CHRIST; A 0; B BELOW_THRESHOLD", certainty: 0.7, cites: [{source: S4, locator: "1843"}, {source: S5, locator: "1847"}, {source: S3, locator: "1851"}], how_known: "Equals deepen D1 coding."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Existence, faith, inwardness (S1); no geometric form claimed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed for a circle claim.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "Lane B unused: A scored; B/mid BELOW; no H1 timing claim."
  notes: ""

institutions:
  - {value: "University of Copenhagen", role: "student (theology; Magister in philosophy)", years: UNKNOWN, kind: "university", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Works"}], how_known: "SEP."}
collaborators:
  - {value: "Regine Olsen", relation: "other", note: "fiancée 1840–1841", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Works"}], how_known: "SEP."}
  - {value: "Emil Boesen", relation: "other", note: "lifelong friend, priest", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Works"}], how_known: "SEP."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 218"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "A rests on unofficial-web copies of Hong/Lowrie translations (S3, S4); Hong print not opened this pass."
    - "Span end 1850 vs 1855; Unchangeableness delivered 1851 (P31)."
    - "Point of View unity contested among scholars (S1); CHRIST still fits signed discourses."
    - "B BELOW: no clear nature account; not a scientist."
  open_questions:
    - "Optional: corroborate A against Hong print / SKS Danish of Eighteen Upbuilding Discourses."
    - "Span end: 1850 or 1855?"
    - "Optional: score C/D/E from Works of Love / Christian Discourses if a later pass needs them."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "John Lippitt; C. Stephen Evans"
    citation: "Lippitt, John, and C. Stephen Evans. 'Søren Kierkegaard.' Stanford Encyclopedia of Philosophy (first published 22 May 2023). https://plato.stanford.edu/entries/kierkegaard/"
    url: "https://plato.stanford.edu/entries/kierkegaard/"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Signed encyclopedia entry, read in full (re-read deepen D1)."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, institutions, collaborators]
  - id: S2
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    source_quality: "study roster"
    reliability_note: "Study's own roster."
    used_for: [review]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "Søren Kierkegaard (tr. Walter Lowrie)"
    citation: "Kierkegaard, Søren. 'The Unchangeableness of God' (discourse delivered 18 May 1851; published 1855). English: Walter Lowrie translation, as archived at jesuswords.net (from Attacks on Christendom materials / For Self-Examination context)."
    url: "https://jesuswords.net/resources/archived/kierkegaard/attacks/unchange.shtml"
    accessed: 2026-10-24
    source_quality: "unofficial web copy"
    reliability_note: "Signed Christian discourse in own name; Lowrie English on an unofficial archive page. Creator / Father-of-lights language for A."
    used_for: [worldview]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "Søren Kierkegaard (tr. Howard V. Hong and Edna H. Hong)"
    citation: "Kierkegaard, Søren. Two Upbuilding Discourses (16 May 1843), in Eighteen Upbuilding Discourses (Princeton University Press, 1990), Hong translation. Quotations as hosted on Wikiquote 'Two Upbuilding Discourses, 1843' (Expectancy of Faith; Every Good and Every Perfect Gift Is from Above)."
    url: "https://en.wikiquote.org/wiki/Two_Upbuilding_Discourses,_1843"
    accessed: 2026-10-24
    source_quality: "unofficial web copy"
    reliability_note: "Signed discourses; Hong English via Wikiquote (not the Princeton print opened this pass). Within-span A evidence."
    used_for: [worldview, contribution, timing]
  - id: S5
    type: secondary
    kind: "other"
    author: "D. Anthony Storm (quoting Hong Works of Love)"
    citation: "Storm, D. Anthony. Commentary on Works of Love (Kjerlighedens Gjerninger, 1847), quoting Hong/Harper Torchback 1962. https://sorenkierkegaard.org/works-of-love.html"
    url: "https://sorenkierkegaard.org/works-of-love.html"
    accessed: 2026-10-24
    source_quality: "unofficial web copy"
    reliability_note: "Secondary commentary hosting substantial Hong quotations from the signed Works of Love; used for CHRIST written_profession and A alt 1 (God as middle term)."
    used_for: [worldview, contribution]
---

## Summary

Søren Kierkegaard (1813–1855), Danish philosopher and theologian [S1]. Deepen D1: CHRIST 0.7 (written_profession, signed Upbuilding Discourses / Works of Love / Unchangeableness of God); A 0 @0.7 (corroborated S3+S4; P42 signed only); B BELOW_THRESHOLD; mid BELOW. Not plotted.

## Life and work

Copenhagen; brief stays in Berlin [S1]. Signed religious discourses ran beside the pseudonymous authorship from 1843 [S1, S4].

## Contribution and impact

Authorship 1843–1850 [S1]. Signed Works of Love (1847) and Eighteen Upbuilding Discourses (1843–44) [S1, S4, S5].

## Childhood and education

University of Copenhagen [S1]. Lutheran / Moravian upbringing [S1].

## Adult working worldview

Christian written profession in signed discourses [S3–S5]. A 0: personal Creator / Father of lights distinct from the world [S3, S4]. B unscored (BELOW). Anti-Climacus unused for A (P42).

## Heritage (context only)

Lutheran (with Moravian influence) [S1].

## Timing

1843–1850, age 30 [S1]. First LIO-type evidence 1843 (Two Upbuilding Discourses) [S4].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Unused this pass (B/mid BELOW).

## Open questions

- Hong print / SKS Danish check for A.
- Span end 1850 vs 1855.

## Research log

- 2026-10-24: Deepen D1 — SEP re-read; Unchangeableness of God (Lowrie, S3); Two Upbuilding Discourses Hong via Wikiquote (S4); Works of Love Hong via Storm (S5). CHRIST → 0.7 written_profession; A → 0 @0.7 corroborated; B/mid → BELOW. Person file only local commit; drafts/deepen_kierkegaard-soren.md untracked; no figures/; no fallacy_catalog.
- 2026-10-20: AA9 audit fixes: span certainty 0.7 (weakest-work rule); note that the P42 pseudonym treatment rests on analogy.
- 2026-10-20: Read SEP (Lippitt and Evans, 2023).
