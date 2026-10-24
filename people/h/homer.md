---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch F)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch F, order P32: F 5, rank 37). Basics from Britannica (G. S. Kirk). Whether Homer existed is uncertain; nothing is known of him beyond the name attached to the poems (S1). The gods of the Iliad and Odyssey are narrative: characters' and the narrative's words are not the author's view. All worldview fields UNKNOWN; mid_basin UNKNOWN. Undated works (P39). Draft, not reviewed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #37, F5 rank 37). Needs: A UNKNOWN; B UNKNOWN; 1 source. Re-opened Britannica Kirk via Wayback (S1). New: Herodotus 2.53 Godley Loeb via Perseus (S3); Nagy CHS chapter on oral tradition and authorship (S4); Moran Journal of Classics Teaching summary of composition/transmission (S5); A. T. Murray Loeb Iliad 1.1 via Perseus for Muse-invocation context (S6). P47 source_quality on every source. Homeric Question / P42 reaffirmed: oral epic handed down under the name; Kirk's 'probable' shaping and unitarian vs analyst debate are not scholarly agreement attributing a specific text as the historical Homer's own words for scoring; characters' and narrative events still not the author's view (P42 addendum). Herodotus credits Homer and Hesiod with teaching the Greeks the gods' genealogy, names, offices and forms — influence of the poems, not a profession of belief. A stays UNKNOWN; B stays UNKNOWN. Chart: still unplotted. No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: homer
  display_name: "Homer"
  roster:
    canonical_name: "Homer"
    rank: 37
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: literature
    field_bucket: literature
  full_name: {value: "Homer", certainty: 0.7, cites: [{source: S1, locator: "opening ('name attached in antiquity…to the poems')"}], how_known: "Britannica: only the name attached to the poems is known."}
  native_name: {value: "Ὅμηρος (Homēros)", certainty: 0.5, cites: [{source: S4, locator: "etymology of Ὅμηρος as nomen loquens"}], how_known: "Standard Greek form; Nagy discusses the etymology. Not a documented signature of a historical individual."}
  aliases:
    - {name: "Homeros", kind: "transliteration"}

basics:
  birth:
    date: {value: UNKNOWN, how_known: "Britannica: flourished 9th or 8th century BCE with a question mark; no birth date (S1). Moran/Nagy: name attached later to oral tradition (S4, S5)."}
    place: {value: UNKNOWN, how_known: "Britannica 'Ionia?' with question mark; Smyrna and Chios competed in antiquity; 'no authenticated local memory' (S1). WHE lists Smyrna/Chios/Ios as traditional claims (S5 context via S1)."}
  death:
    date: {value: UNKNOWN, how_known: "Nothing historical; Vita legends (Ios etc.) are mythic (S4)."}
    place: {value: UNKNOWN, how_known: "Nothing historical (S1, S4)."}
  first_lasting_contribution_year: {value: UNKNOWN, how_known: "Poems undated; quotations by mid-7th century BCE (S1). P39."}
  era_bucket: {value: "before -500", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts; Early references (mid-7th c. BCE quotations)"}, {source: S3, locator: "2.53 (Homer ≤400 years before Herodotus)"}], how_known: "Every possible working year (9th–8th c. BCE tradition; Herodotus ≤400 years before 5th c.; poems quoted by mid-7th c.) is before 500 BCE (P39); Britannica + Herodotus, 0.7."}
  region_of_birth: {value: UNKNOWN, how_known: "Birthplace uncertain ('Ionia?'); not coded to a study region."}
  region_of_work: {value: UNKNOWN, how_known: "Ionic-dialect poems and Ionian tradition (S1, S4) are not a documented place of work for a historical person."}
  sex_as_recorded: {value: "male", certainty: 0.5, cites: [{source: S1, locator: "text / traditional portrayal"}], how_known: "Recorded as male by tradition; existence itself uncertain (S1)."}
  languages_of_work: {value: [Greek], certainty: 0.7, cites: [{source: S1, locator: "opening; Ionic dialect"}], how_known: "Poems in predominantly Ionic Greek (S1)."}
  occupations: {value: ["epic poet"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Presumed author / oral poet of the epics (S1)."}

contribution:
  fields: {value: ["epic poetry"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Iliad (traditional attribution)", year: UNKNOWN, kind: work, lasting: "basis of Greek education and culture; 'the most important poems of the classical European tradition' (S1)", certainty: 0.5, cites: [{source: S1, locator: "opening ('probable' primary shaping)"}, {source: S5, locator: "§1 name later; unity vs multiple poets"}], how_known: "Authorship probable but disputed (S1); Homeric Question open (S4, S5). Certainty 0.5. Not used to score worldview under P42."}
    - {value: "Odyssey (traditional attribution)", year: UNKNOWN, kind: work, lasting: "as above (S1)", certainty: 0.5, cites: [{source: S1, locator: "opening; Q&A authorship disputed"}, {source: S5, locator: "probably not same poet for both series"}], how_known: "As above; many scholars treat Iliad and Odyssey as different poets (S5 summary of common view)."}
  evidence_of_impact:
    - {value: "Basis of Greek education; model for Virgil's Aeneid; revived in Byzantium and the Renaissance", kind: "standard textbook canon", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
    - {value: "Herodotus: Homer and Hesiod taught the Greeks the gods' descent, names, spheres/functions and forms", kind: "assessment by a later major figure", certainty: 0.7, cites: [{source: S3, locator: "2.53.2–3"}, {source: S1, locator: "Early references (Herodotus theology)"}], how_known: "Herodotus 2.53 (Godley); Britannica paraphrases. Influence of the poems, not a scored worldview of Homer."}
  major_works: []
  honours: []
  definition_fit: {value: "arguable", rationale: "The poems clearly meet the bar; whether a single historical person 'Homer' made them remains uncertain (S1, S4, S5).", certainty: 0.5, cites: [{source: S1, locator: "opening; Q&A"}, {source: S4, locator: "questions of authorship in oral tradition"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Nothing historical of a person (S1)."}
  family_religious_practice: {value: UNKNOWN, how_known: "Nothing."}
  parents_and_household: []
  household_circumstances: {value: UNKNOWN, how_known: "Nothing."}
  schooling: []
  early_mathematics: {value: UNKNOWN, how_known: "Nothing."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Nothing."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Nothing documented for a historical childhood."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: UNKNOWN, how_known: "Undated works (P39)."}
  nominal_affiliations:
    - {value: "Name attached in antiquity to the Iliad and Odyssey (Homeric tradition / Homeridae lore)", role: other, certainty: 0.7, cites: [{source: S1, locator: "opening; Homeridae"}, {source: S4, locator: "Homēridai of Chios; Panathenaic Homer"}], how_known: "Traditional attribution and guild lore, not a worldview profession."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No statement in a voice separable from narrative under P42 (S1, S4, S5, S6)."}
  primary_system: {value: UNKNOWN, how_known: "Nothing in the poet's own voice separable from narrative (P42). Herodotus credits the poems with formulating Greek theology (S3 via S1) — describes cultural influence, not the poet's belief. HELLEN rejected as modern reconstructionist code."}
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: HELLEN, reason: "Modern reconstructionist code; the poems are a source for Greek religion as later practiced, not a profession of HELLEN by a historical Homer. Rejected.", cites: [{source: S1, locator: "text"}, {source: S3, locator: "2.53 (poems taught the gods)"}]}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "P19 researched silent / P42: gods in the Iliad and Odyssey are narrative characters; their words and the narrative's events are not the author's view (P42 addendum). Muse invocation (S6) is a poetic convention, not a locus profession. Herodotus 2.53 is about the poems' cultural effect, not Homer's belief. Named alternative: none without an attributable non-narrative text.", note: "Homeric Question: even unitarian attribution of one epic would not by itself convert narrative theology into authorial A (P42 addendum)."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist; divine interventions and Zeus's plan in the plot are narrative, not a statement about nature by an attributable author (P42). Sources read say nothing on a personal account of nature (P19). Named alternative: BELOW_THRESHOLD only if a non-narrative authorial remark on nature were found — none this pass.", note: "Contrast Hippocrates: Meno disease theory supplied weak scientist evidence; Homer has no such doxography on nature."}
    C_ledger: {value: UNKNOWN, how_known: "As for A — narrative only."}
    D_authority: {value: UNKNOWN, how_known: "Muse invocation is convention (coder's call; S6 context). No attributable stance on revelation vs observation."}
    E_scope: {value: UNKNOWN, how_known: "As for A (P7)."}
  mid_basin: {value: UNKNOWN, how_known: "A and B are UNKNOWN (P19)."}
  statements:
    - text: "The wrath sing, goddess, of Peleus' son, Achilles, that destructive wrath which brought countless woes upon the Achaeans, and sent forth to Hades many valiant souls of heroes, and made them themselves spoil for dogs and every bird; thus the plan of Zeus came to fulfillment…"
      cites: [{source: S6, locator: "Iliad 1.1–5 (Murray Loeb English)"}]
      date: "-750"
      context: "Opening of the Iliad: Muse invocation and Zeus's plan. Narrative/poetic convention; author of this wording not established as the historical Homer under P42 (Homeric Question). Context only; not used to score."
      axes: [A_locus, D_authority, B_cause]
      kind: "other"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "A. T. Murray, Iliad Loeb English via Perseus this pass. Date '-750' is a conventional mid-point for the oral-epic tradition (S1 flourished 9th/8th c.), not a documented composition year. P42 / Homeric Question: scores nothing."
    - text: "for I suppose Hesiod and Homer flourished not more than four hundred years earlier than I; and these are the ones who taught the Greeks the descent of the gods, and gave the gods their names, and determined their spheres and functions, and described their outward forms."
      cites: [{source: S3, locator: "Histories 2.53.2"}]
      date: "-440"
      context: "Herodotus on Homer and Hesiod as teachers of Greek theology. Reported assessment of the poems' influence, not Homer's own words. Cannot score A/B alone (§7 / P42 doxography)."
      axes: [A_locus]
      kind: "reported speech"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "A. D. Godley, Herodotus Loeb (1920), Perseus. Date conventional for Herodotus's work, not for Homer."
  changes_over_life: []
  coder_notes: "Deepen D1: Homeric Question / P42 block stands. Kirk (S1): existence uncertain; 'probable' that a poet Homer shaped both epics — not the P42 scholarly-agreement bar for scoring own words. Nagy (S4): authorship questions belong to oral tradition; classical Homer = Iliad+Odyssey only; Lives are myth. Moran (S5): 'Homer' a name given later; likely different poets for Iliad and Odyssey series; unity of each poem vs multitext debate. Narrative theology and Muse convention stay context. A UNKNOWN; B UNKNOWN. Chart unplotted."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Greek (Ionian, by tradition)", certainty: 0.5, cites: [{source: S1, locator: "Quick Facts; Ionic dialect / Ionia conjecture"}], how_known: "Britannica with a question mark; Ionic dialect of the poems."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Nothing known of a historical childhood religion."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Nothing known."}
  childhood_catechism: {value: UNKNOWN, how_known: "Nothing known."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: UNKNOWN, how_known: "Undated works (P39)."}
  age_at_first_lasting_contribution: {value: UNKNOWN, how_known: "Undated (P39)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No attributable LIO-type statement (P42)."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Nothing known of the person separable from narrative."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Nothing known."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "Oral-formulaic composition (Parry/Lord line via S4, S5); nothing on a historical person's geometry training.", certainty: 0.5, cites: [{source: S4, locator: "oral poetic composition / Parry and Lord"}, {source: S5, locator: "§17 Parry and Lord oral hypothesis"}], how_known: "Scholarly reconstruction of the tradition, not the person."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Nothing known."}
  circle_present: {value: "unclear", rationale: "Nothing in a separable authorial voice.", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  reading: "No reading possible. Homeric Question / P42: poems are authorial tradition, not scored own words."
  notes: "H1 not tested. Lane B separate from Lane A."

institutions: []
collaborators: []

review:
  roster_status_reason: {value: "Core in v8 (F 5). Existence uncertain; roster treats 'Homer' as a person (Jason's call).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 37"}], how_known: "Study roster."}
  controversies:
    - {value: "Homeric Question: whether Homer existed; single vs multiple authorship of each epic; whether one poet made both Iliad and Odyssey; oral vs written fixation", certainty: 0.7, cites: [{source: S1, locator: "Q&A; opening"}, {source: S4, locator: "questions of authorship"}, {source: S5, locator: "throughout (Wolf; Parry/Lord; multitext)"}], how_known: "Britannica, Nagy, Moran."}
  data_quality_flags:
    - "Existence uncertain; roster treats 'Homer' as a person. Raised for Jason (roster status is his call)."
    - "P42 oral-epic case: no scored A/B without specific scholarly attribution of a non-narrative text."
  open_questions:
    - "Print/page-check Kirk, The Songs of Homer, and M. L. West Making of the Iliad / Odyssey for any claim that would meet P42's specific-attribution bar for a non-narrative passage."
    - "If a unitarian scholarly consensus on one epic emerges with attributable didactic asides, re-open A/D under P42 addendum — narrative theology still would not score."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Geoffrey S. Kirk"
    citation: "Kirk, Geoffrey S. \"Homer.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Homer-Greek-poet."
    url: "https://www.britannica.com/biography/Homer-Greek-poet"
    accessed: 2026-10-24
    reliability_note: "Signed article by a Homer scholar (Regius Professor Emeritus of Greek, Cambridge; author of The Songs of Homer). Re-read this pass via Wayback full-page capture (live site JS wall). Q&A header used only for authorship facts the body repeats."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, worldview, heritage, timing, lane_b, review]
  - id: S2
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S3
    type: primary
    kind: other
    author: "Herodotus; trans. A. D. Godley"
    year: 1920
    citation: "Herodotus. Histories 2.53. Trans. A. D. Godley. Loeb Classical Library. Cambridge, MA: Harvard University Press, 1920. Perseus Digital Library."
    url: "https://www.perseus.tufts.edu/hopper/text?doc=Hdt.+2.53"
    accessed: 2026-10-24
    reliability_note: "Scholarly Loeb English of Herodotus on Homer/Hesiod as teachers of Greek theology. Primary for Herodotus; for Homer it is later assessment of the poems' influence (reported speech / doxography under P42) — cannot score Homer's A/B alone."
    source_quality: "scholarly edition or monograph"
    used_for: [basics, contribution, worldview]
  - id: S4
    type: secondary
    kind: book chapter
    author: "Gregory Nagy"
    year: 2015
    citation: "Nagy, Gregory. \"Oral Traditions, Written Texts, and Questions of Authorship.\" In The Greek Epic Cycle and its Ancient Reception: A Companion, ed. Marco Fantuzzi and Christos Tsagalis, 59–77. Cambridge: Cambridge University Press, 2015. Online at Center for Hellenic Studies."
    url: "https://chs.harvard.edu/curated-article/gregory-nagy-oral-traditions-written-texts-and-questions-of-authorship/"
    accessed: 2026-10-24
    reliability_note: "Leading oralist; authorship of Cycle and Homeric poems framed in oral tradition; Lives of Homer as myth; classical Homer = Iliad and Odyssey only. Used for Homeric Question / P42 limits, not for scoring LIO."
    source_quality: "scholarly edition or monograph"
    used_for: [identity, contribution, worldview, lane_b, review]
  - id: S5
    type: secondary
    kind: journal article
    author: "Jerome Moran"
    year: 2021
    citation: "Moran, Jerome. \"The Composition and Transmission of the Homeric Poems: A Summary.\" Journal of Classics Teaching 23, no. 45 (2022): 33–34. First published online 3 August 2021. https://doi.org/10.1017/S2058631021000416"
    url: "https://www.cambridge.org/core/journals/journal-of-classics-teaching/article/composition-and-transmission-of-the-homeric-poems-a-summary/7B43B135E0A2951CBEE87CA1D80F5EF2"
    accessed: 2026-10-24
    reliability_note: "Open Cambridge Core summary of oral hypothesis, Wolf, Parry/Lord, multitext, and likely separate poets for Iliad and Odyssey series. Pedagogical but cites the scholarly line; used for Homeric Question framing."
    source_quality: "scholarly edition or monograph"
    used_for: [contribution, worldview, lane_b, review]
  - id: S6
    type: primary
    kind: other
    author: "Homeric Iliad (traditional attribution); trans. A. T. Murray"
    year: 1924
    citation: "Homer. Iliad 1.1–5. Trans. A. T. Murray. Loeb Classical Library. Cambridge, MA: Harvard University Press. Perseus Digital Library English text."
    url: "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0134%3Abook%3D1%3Acard%3D1"
    accessed: 2026-10-24
    reliability_note: "Scholarly Loeb English of the Iliad opening (Muse / Zeus's plan). Tradition only under P42 / Homeric Question — context quotation, not scored as Homer's own words."
    source_quality: "unofficial web copy"
    used_for: [worldview]
---

# Homer

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Homer, the name antiquity attached to the *Iliad* and the *Odyssey*, flourished perhaps in the 9th or 8th century BCE in Ionia [S1]. Whether a single historical poet existed, and who composed which epic, remains the Homeric Question [S1, S4, S5]. Deepen D1: all LIO axes UNKNOWN; mid_basin UNKNOWN; chart still unplotted.

## Life and work

Nothing historical beyond the name attached to the poems [S1]. Biographical *Lives* are mythic appropriations of performance traditions [S4]. Oral composition and later written fixation are the scholarly frame [S4, S5].

## Contribution and impact

The two epics, basis of Greek education and of the classical European tradition [S1]. Herodotus says Homer and Hesiod taught the Greeks the gods' descent, names, offices and forms [S3] — cultural influence of the poems, not a scored belief of Homer.

## Childhood and education

Nothing known of a historical childhood [S1].

## Adult working worldview

**Lane A.** Gods and Muse are narrative/convention; not the author's view under P42 [S1, S6]. Herodotus is later assessment of the poems [S3]. A UNKNOWN.

**Lane B (separate).** No scientist account of nature; plot theology does not score [S1, S4]. B UNKNOWN.

## Heritage (context only)

Ionian Greek by tradition / Ionic dialect [S1].

## Timing

Undated (P39) [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form and circle unclear. Oral-formulaic tradition is about the poems, not a documented person [S4, S5].

## Open questions

- Kirk *Songs of Homer*; West *Making of the Iliad* / *Odyssey* page-check for any P42-meeting non-narrative attribution.
- Roster status if existence remains too uncertain.

## Research log

- 2026-10-15: Read Britannica (Kirk).
- 2026-10-24 (D1): Britannica Kirk (Wayback); Herodotus 2.53 Godley; Nagy CHS authorship chapter; Moran JCT composition summary; Murray Loeb *Iliad* 1.1 (Perseus). Homeric Question / P42 reaffirmed. A UNKNOWN→UNKNOWN; B UNKNOWN→UNKNOWN. Chart-moving no.
