---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to architecture. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen D1 (queue #187/228, F 3, rank 199): hunted first-person God/nature statements. Own words via Purdy (Open Hand / Jean Petit) + McNamara: 'not a churchgoer' / work 'almost religious'; 'not a pagan' / Ronchamp as contact with the unknown; 'not experienced the miracle of faith' but 'miracle of inexpressible space'. Architecture / ineffable-space / nature-as-setting metaphors do not score pantheism or B (standing rule; Wright P16 path). A UNKNOWN; B UNKNOWN; primary UNKNOWN (CHRIST heritage only; Wikipedia 'avowed atheist' is secondary characterization — own words incomplete for ATHE). Mid UNKNOWN. Dual bio P50 (Britannica + Wikipedia); P47 on all. Not plotted. Fallacy audit none; figures not refreshed."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "AA5 audit fix (v8's call on the auditor's advice): full Choay text read (Britannica scholars edition); lasting work is the books 1923–1948 ('a bible for succeeding generations of architects'); span 1923–1948; Villa Savoye and Ronchamp added as major works."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA5, order P32: F 3, rank 199). Source: Britannica, signed by Françoise Choay (scholars edition, read in full after the AA5 audit). Lasting work: Vers une architecture (Toward a New Architecture, 1923); his books 'constituted a bible for succeeding generations of architects' (S1); the books from Vers une architecture (1923) to Le Modulor (1948) are the body of work S1 calls 'a bible', so the span is 1923–1948 by publication (P30 #1), age 36. Buildings (Villa Savoye 1929–31, Ronchamp 1950–55) are major works, not listed as lasting, since S1's lasting phrase covers the books. Worldview: no own words read; raised in 'the puritanism of a Protestant environment' (S1). primary_system UNKNOWN; A UNKNOWN; not a scientist; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}

identity:
  id: corbusier-le
  display_name: "Le Corbusier"
  roster:
    canonical_name: "Le Corbusier"
    rank: 199
    F: 3
    models: [Claude, DeepSeek, Gemini]
    band: "core (3–4)"
    status: "core"
    field: "architecture"
    field_bucket: "arts"
  full_name: {value: "Charles-Édouard Jeanneret-Gris", certainty: 1.0, cites: [{source: S1, locator: "Also known as; Introduction"}, {source: S5, locator: "infobox / Born"}], how_known: "Britannica and Wikipedia EN agree (P50)."}
  native_name: {value: "Charles-Édouard Jeanneret", certainty: 0.7, cites: [{source: S5, locator: "lead / Born"}, {source: S1, locator: "Also known as"}], how_known: "Birth name; 'Le Corbusier' is the adopted professional name (S1; S5)."}
  aliases:
    - {name: "Charles-Édouard Jeanneret", kind: "birth name"}
    - {name: "Le Corbusier", kind: "pen or art name"}

basics:
  birth:
    date: {value: "1887-10-06", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S5, locator: "infobox"}], how_known: "Britannica and Wikipedia EN agree (P50)."}
    place: {value: "La Chaux-de-Fonds", modern_name: "La Chaux-de-Fonds, Switzerland", polity_then: "Switzerland", certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S5, locator: "infobox"}], how_known: "Two sources (P50)."}
  death:
    date: {value: "1965-08-27", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S5, locator: "infobox"}], how_known: "Two sources (P50)."}
    place: {value: "Cap Martin", modern_name: "Roquebrune-Cap-Martin, France", polity_then: "France", certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S5, locator: "infobox"}], how_known: "Two sources (P50)."}
  first_lasting_contribution_year: {value: 1923, certainty: 0.7, cites: [{source: S1, locator: "Education and early years"}], how_known: "Vers une architecture (Toward a New Architecture, 1923) (S1); publication (P30 #1)."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "Education and early years"}], how_known: "1923 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 1.0, cites: [{source: S1, locator: "Introduction"}, {source: S5, locator: "infobox"}], how_known: "Switzerland (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "Education and early years"}, {source: S5, locator: "lead (France from 1930; India Chandigarh)"}], how_known: "Paris / France primary; Chandigarh later — Western Europe lead at 0.7.", alternatives: [{value: "South Asia", note: "Chandigarh master plan and buildings (S5).", cites: [{source: S5, locator: "Chandigarh"}]}]}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["French"], certainty: 0.7, cites: [{source: S1, locator: "Education and early years"}], how_known: "French titles."}
  occupations: {value: ["architect", "city planner", "painter", "writer"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S5, locator: "infobox"}], how_known: "Britannica and Wikipedia."}

contribution:
  primary_domain: architecture
  fields: {value: ["architecture", "urban planning"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Books from Vers une architecture (1923) to Le Modulor (1948)", year: 1923, kind: "body of work", lasting: "his books, 'whose essential lines of thought ... hardly changed at all in 45 years, constituted a bible for succeeding generations of architects' (S1); 'A house is a machine for living in'", certainty: 0.7, cites: [{source: S1, locator: "Education and early years"}], how_known: "Britannica; the named books run from 1923 to Le Modulor (1948)."}
  evidence_of_impact:
    - {value: "17 architectural works named UNESCO World Heritage sites (2016)", kind: "other", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S5, locator: "lead"}], how_known: "Britannica and Wikipedia."}
  major_works:
    - {value: "Villa Savoye, Poissy", year: 1931, kind: "other", certainty: 0.7, cites: [{source: S1, locator: "The first period"}, {source: S5, locator: "infobox"}], how_known: "Britannica: 1929–31."}
    - {value: "Notre-Dame-du-Haut, Ronchamp", year: 1955, kind: "other", certainty: 0.7, cites: [{source: S1, locator: "The second period"}, {source: S5, locator: "Religious architecture"}], how_known: "Britannica: 1950–55; commissioned through Fr. Couturier."}
    - {value: "Après le cubisme (with Amédée Ozenfant)", year: 1918, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "Education and early years"}], how_known: "Britannica: the Purist manifesto."}
    - {value: "Urbanisme", year: 1925, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "Education and early years"}], how_known: "Britannica."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Internationally influential architect; first studied use of rough-cast concrete (S1).", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "Protestant (Calvinist Swiss Jura environment)", certainty: 0.7, cites: [{source: S1, locator: "Education and early years"}, {source: S5, locator: "Early life (La Chaux-de-Fonds Protestant / Jura culture)"}], how_known: "Britannica: 'puritanism of a Protestant environment'. Heritage context only."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated beyond the Protestant environment (S1)."}
  parents_and_household:
    - {value: "Family of watchmakers; father an enameller and engraver of watch faces; mother taught piano (S5)", role: "family", certainty: 0.7, cites: [{source: S1, locator: "Education and early years"}, {source: S5, locator: "Early life"}], how_known: "Britannica and Wikipedia."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling:
    - {value: "École des Arts Décoratifs, La Chaux-de-Fonds (under Charles L'Eplattenier); no formal architectural training", certainty: 0.7, cites: [{source: S1, locator: "Education and early years"}], how_known: "Britannica."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated; later Modulor is adult work, not childhood exposure."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1923–1948", certainty: 0.7, cites: [{source: S1, locator: "Education and early years"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No clear self-description of science vs religion as such; ineffable-space vs faith contrast is architectural (S3), not scored here."}
  primary_system: {value: UNKNOWN, how_known: "No scored adult system. Protestant upbringing is heritage only (S1). Own words: not a churchgoer; has not experienced the miracle of faith; work becomes 'almost religious'; 'not a pagan' (S3 via Jean Petit). That package rejects institutional CHRIST practice without a clear ATHE/NONE profession (denies churchgoing and faith-miracle, affirms religious consciousness / contact with the unknown). Wikipedia's 'avowed atheist' (S5) is secondary characterization — not used alone to code ATHE. No lead strong enough to name."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Heritage only: Protestant / Calvinist Swiss Jura upbringing (S1). Adult: not a churchgoer; no miracle of faith (S3). Rejected as primary."}
    - {code: ATHE, reason: "Wikipedia calls him an 'avowed atheist' (S5 Religious architecture). Not coded: secondary label; own quoted words stop short of denying God and keep 'religious consciousness' / 'not a pagan' (S3)."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "First-person statements found (S3) do not fix divine locus: denial of churchgoing and of the 'miracle of faith', plus 'almost religious' work and 'contact with the unknown', without identifying God with Nature, a transcendent person, or absence of God (P19). Architecture / ineffable-space talk is not an A score. Do not invent."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30). Ville radieuse 'laws of nature' and landscape-as-program remarks (S3) are urbanism / site design, not P16 cause-order claims about how events happen. Standing rule: architecture/nature metaphors alone do not score B. Do not invent."}
    C_ledger: {value: UNKNOWN, how_known: "Not scored."}
    D_authority: {value: UNKNOWN, how_known: "Not scored."}
    E_scope: {value: UNKNOWN, how_known: "Not scored."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, so the P4 test cannot be applied (P19)."}
  statements:
    - text: "I am not a churchgoer myself, but one thing I do know is that every man has the religious consciousness of belonging to a greater mankind, to a greater or lesser degree, but in the end he is part of it. Into my work I bring so much effusion and intense inner life that it becomes something almost religious."
      cites: [{source: S3, locator: "p. 289 (quoting Jean Petit, Le Corbusier lui-même, Geneva 1970)"}, {source: S4, locator: "same quotation via Purdy"}]
      date: "1970"
      context: "English via Purdy (Open Hand); French source Jean Petit 1970 compilation. Date is Petit publication year, not composition date (unknown here)."
      axes: []
      kind: "other"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Does not unlock primary_system or A: 'almost religious' names architectural inner life, not a God locus. Axes left empty."
    - text: "People were at times surprised to see me participating in a sacred art. I am not a pagan. Ronchamp is a response to the desire that one occasionally has to extend beyond oneself, and to seek contact with the unknown."
      cites: [{source: S3, locator: "near end of theological-program discussion (Petit via Purdy)"}]
      context: "On Ronchamp / sacred art; secondary quotation via Purdy."
      axes: []
      kind: "other"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "'Not a pagan' + unknown contact ≠ CHRIST or pantheism. Not scored."
    - text: "I have not experienced the miracle of faith, but I have often known the miracle of inexpressible space, the apotheosis of plastic emotion."
      cites: [{source: S3, locator: "Ronchamp section (Purdy paraphrase/translation of Le Corbusier)"}, {source: S4, locator: "closing quotation"}]
      context: "On Ronchamp / ineffable space; architectural sacred, not doctrinal faith."
      axes: []
      kind: "other"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Standing rule: architecture/ineffable-space metaphors do not score pantheism or A/B."
  changes_over_life: []
  coder_notes: "Deepen D1 2026-10-24: Purdy (S3) and McNamara (S4) supply the main first-person package; Britannica heritage unchanged. Keep silence on A/B/primary. Optional unread: Petit Le Corbusier lui-même pages in French; Flora Samuel on spirituality; Modulor 1 primary pages for 'divine' mathematics (still architecture proportion — would not unlock B alone)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "French-speaking Swiss (Romandie); French citizenship from 1930", certainty: 0.7, cites: [{source: S5, locator: "lead / Citizenship"}], how_known: "Wikipedia EN."}
  religious_heritage_by_birth: {value: "Protestant (Swiss Jura)", certainty: 0.7, cites: [{source: S1, locator: "Education and early years"}], how_known: "Britannica: 'the puritanism of a Protestant environment'."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1923–1948", certainty: 0.7, cites: [{source: S1, locator: "Education and early years"}], how_known: "Body of work from Vers une architecture (1923) to Le Modulor (1948), the books S1 calls 'a bible for succeeding generations of architects' (P29, P30 #1)."}
  age_at_first_lasting_contribution: {value: 36, certainty: 0.7, cites: [{source: S1, locator: "Introduction; Education and early years"}], how_known: "1923 − 1887 = 36 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "Spiritual / almost-religious remarks found; none scored as LIO axes."}
  lio_views_relative_to_major_work: {value: UNKNOWN, how_known: "None scored."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "None scored."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "Classical proportion and pure geometric forms (S1); later the Modulor golden-section system (S5).", certainty: 0.5, cites: [{source: S1, locator: "Education and early years"}, {source: S5, locator: "Modulor"}], how_known: "Coder's reading; Lane B only."}
  form_acquired: {value: "adulthood, before major work", rationale: "Mediterranean/Palladian proportion discoveries on 1907–1911 travels precede 1923 books (S1).", certainty: 0.5, cites: [{source: S1, locator: "Education and early years"}], how_known: "Lane B labeled belief."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "Lane B: strong geometric/proportion path (Modulor). Not a chart finding."
  notes: "Do not promote Lane B geometry into Lane A A/B scores."

institutions: []
collaborators:
  - {value: "Amédée Ozenfant", relation: "collaborator", note: "Purism; L'Esprit Nouveau", certainty: 0.7, cites: [{source: S1, locator: "Education and early years"}], how_known: "Britannica."}
  - {value: "Charles L'Eplattenier", relation: "teacher", note: "'his only teacher'", certainty: 0.7, cites: [{source: S1, locator: "Education and early years"}], how_known: "Britannica."}
  - {value: "Marie-Alain Couturier, O.P.", relation: "other", note: "Dominican who steered Ronchamp and La Tourette commissions; 'betting on genius' regardless of personal faith (S3; S4)", certainty: 0.7, cites: [{source: S3, locator: "Ronchamp / Couturier sections"}, {source: S4, locator: "throughout"}], how_known: "Purdy and McNamara."}
  - {value: "Pierre Jeanneret", relation: "collaborator", note: "cousin; long practice partner", certainty: 0.7, cites: [{source: S5, locator: "Painting, Cubism, Purism"}], how_known: "Wikipedia EN."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 199"}], how_known: "Study roster."}
  controversies:
    - {value: "Political controversies (fascism ties, antisemitic remarks) noted in Wikipedia; not used for worldview codes this pass", certainty: 0.5, cites: [{source: S5, locator: "Controversies"}], how_known: "Wikipedia EN; out of deepen scope."}
  data_quality_flags:
    - "Worldview: first-person spiritual remarks found; A/B/primary remain UNKNOWN (architecture metaphors not scored)."
    - "Key quotes known via secondary (Petit 1970 / Purdy); French primary pages unread."
  open_questions:
    - "Petit Le Corbusier lui-même French pages for the churchgoer / faith / pagan quotations."
    - "Whether any Modulor or Poème de l'angle droit passage states a scorable God locus (unlikely to clear standing-rule bar alone)."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Françoise Choay"
    citation: "Choay, Françoise. 'Le Corbusier.' Encyclopaedia Britannica. https://www.britannica.com/biography/Le-Corbusier. Re-checked 2026-10-24 (scholars/body text; Top Questions not cited)."
    url: "https://www.britannica.com/biography/Le-Corbusier"
    accessed: 2026-10-24
    reliability_note: "Signed article, read in full. Top Questions AI boxes not cited (P26)."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, heritage, timing, collaborators, worldview]
  - id: S2
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-24
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S3
    type: secondary
    kind: book chapter
    author: "Martin Purdy"
    citation: "Purdy, Martin. 'Le Corbusier and the Theological Program.' In The Open Hand: Essays on Le Corbusier, ed. Russell Walden. MIT Press. Open-access chapter https://mitp-arch.mitpress.mit.edu/pub/0jclpgmq (read 2026-10-24). Quotes Jean Petit, Le Corbusier lui-même (Geneva, 1970)."
    url: "https://mitp-arch.mitpress.mit.edu/pub/0jclpgmq"
    accessed: 2026-10-24
    reliability_note: "Signed scholarly chapter; main warrant for first-person sacred-art quotations (via Petit)."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview, collaborators, review]
  - id: S4
    type: secondary
    kind: journal article
    author: "Denis R. McNamara"
    citation: "McNamara, Denis R. 'Almost Religious: Couturier, Le Corbusier and the Monastery of La Tourette.' Sacred Architecture Journal. https://www.sacredarchitecture.org/articles/almost_religious_couturier_lecorbusier_and_the_monastery_of_la_tourette"
    url: "https://www.sacredarchitecture.org/articles/almost_religious_couturier_lecorbusier_and_the_monastery_of_la_tourette"
    accessed: 2026-10-24
    reliability_note: "Signed article; corroborates Purdy quotations and Couturier context. Catholic-critical frame noted; used for quotes and commission facts, not for coding ATHE."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview, collaborators, review]
  - id: S5
    type: secondary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia. 'Le Corbusier.' https://en.wikipedia.org/wiki/Le_Corbusier. Read 2026-10-24."
    url: "https://en.wikipedia.org/wiki/Le_Corbusier"
    accessed: 2026-10-24
    reliability_note: "Dual-bio second source (P50). 'Avowed atheist' line not used alone for primary_system (own-words package in S3 preferred)."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, heritage, collaborators, review]
---

## Summary

Le Corbusier (1887–1965), architect [S1]. Deepen D1: first-person spiritual remarks found; A/B/primary stay UNKNOWN (architecture metaphors not scored). Not plotted.

## Life and work

La Chaux-de-Fonds; Paris; later Chandigarh [S1; S5].

## Contribution and impact

Books 1923–1948; UNESCO works [S1].

## Childhood and education

Protestant Jura environment; École des Arts Décoratifs [S1].

## Adult working worldview

Not a churchgoer; work 'almost religious'; no miracle of faith but ineffable space; not a pagan [S3]. Protestant heritage only. A/B UNKNOWN. Primary UNKNOWN.

## Heritage (context only)

Protestant Swiss Jura [S1]. Never a worldview code.

## Timing

1923–1948, age 36 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Geometry/Modulor present; not promoted to Lane A.

## Open questions

- Petit French pages; Flora Samuel; Modulor primary for any God-locus line.

## Research log

- 2026-10-24: Deepen D1. Britannica re-check; Purdy Open Hand; McNamara Sacred Architecture; Wikipedia EN P50. Wrote drafts/deepen_corbusier-le.md (untracked). Person-file-only commit.
- 2026-10-19: AA5 audit fix; Choay scholars edition.
- 2026-10-19: Read Britannica (Choay).
