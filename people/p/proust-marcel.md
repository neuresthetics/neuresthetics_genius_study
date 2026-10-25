---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, deepen D1 queue #191)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA6, order P32: F 3, rank 203). Source: Britannica, signed by George Duncan Painter (scholars edition, read in full). Lasting work: À la recherche du temps perdu (1913–27); 'The entire climate of the 20th-century novel was affected' by it (S1). First volume November 1913; the last three volumes are posthumous, so the span ends at his death, 1922 (posthumous rule; P29 never past death). Span 1913–1922, age 42. Worldview: no own words on belief read; S1 reads the novel as 'set in the context of human religious experience', its subject 'salvation' (a critic's reading of fiction, not a profession). Catholic father, Jewish mother (S1). primary_system UNKNOWN; A UNKNOWN; not a scientist; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #191/228, F3 rank 203). Goals: letters/essays own words if any; keep silence if none; do not force plot. Dual bio Wikipedia EN (S3, P50): baptized 5 Aug 1871 Saint-Louis-d'Antin, confirmed, never formally practised; White 'mystical atheist' is biographer label only. Opened de Vendeuvre RHLF 2008 (S4) and Mimouni 2024 (S6) quoting Kolb Corr. XIV p. 218 letter to Lionel Hauser, early Sept 1915 (in-span): 'si je n'ai pas la Foi, comme tu dis, en revanche la préoccupation religieuse n'est jamais absente un jour de ma vie' and refusal to affirm beyond what one believes. Opened Topping ch. 'Religion' in Watt (ed.) Marcel Proust in Context (S5): 1908 letter to Mme Straus denying belief in Heaven (Corr. viii, 278; pre-span, P31); 1906 Lauris consolation-in-prayer line addressee-inflected. Montesquiou May 1896 Catholic-like-father line is heritage identity, not adult creed. Guermantes Way 'highest praise of God… atheist' is novel narrator (P42 unused). L'Irréligion d'État 1892 is political anti-fanaticism, not personal creed. Kolb print volumes unread (secondary quotations only). primary_system UNKNOWN→BELOW_THRESHOLD (leads AGNOS/ATHE/SECHUM; P19). A UNKNOWN→BELOW_THRESHOLD (no Faith ≠ God locus/denial; Joyce pattern). B stays UNKNOWN (not a scientist; P16/P30). mid_basin UNKNOWN. Not plotted. Chart-moving NO. P47 on S1–S6. No fallacy_catalog. No figures/. Draft, not reviewed."}

identity:
  id: proust-marcel
  display_name: "Marcel Proust"
  roster:
    canonical_name: "Marcel Proust"
    rank: 203
    F: 3
    models: [Claude, Gemini, GPT]
    band: "core (3–4)"
    status: "core"
    field: "literature"
    field_bucket: "literature"
  full_name: {value: "Valentin Louis Georges Eugène Marcel Proust", certainty: 0.7, cites: [{source: S3, locator: "infobox / lead"}, {source: S1, locator: "opening (Marcel Proust)"}], how_known: "Wikipedia EN full form; Britannica short form Marcel Proust."}
  native_name: {value: "Marcel Proust", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "lead"}], how_known: "French in Latin script."}
  aliases:
    - {name: "Marcel-Proust", kind: "roster alias"}
    - {name: "Proust-Marcel", kind: "roster alias"}

basics:
  birth:
    date: {value: "1871-07-10", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "infobox"}], how_known: "Britannica + Wikipedia EN."}
    place: {value: "Auteuil, near Paris", modern_name: "Auteuil, Paris, France", polity_then: "France", certainty: 1.0, cites: [{source: S1, locator: "opening / Early life"}, {source: S3, locator: "infobox (Paris)"}], how_known: "Britannica Auteuil; Wikipedia Paris (same commune)."}
  death:
    date: {value: "1922-11-18", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "infobox"}], how_known: "Britannica + Wikipedia EN."}
    place: {value: "Paris", modern_name: "Paris, France", polity_then: "France", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "infobox"}], how_known: "Britannica + Wikipedia EN."}
  first_lasting_contribution_year: {value: 1913, certainty: 0.7, cites: [{source: S1, locator: "Works"}, {source: S3, locator: "Notable work / In Search of Lost Time"}], how_known: "Du côté de chez Swann, November 1913 (S1); publication (P30)."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "Works"}], how_known: "1913 (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "infobox"}], how_known: "France (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "Works"}, {source: S3, locator: "Biography"}], how_known: "Paris."}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S1, locator: "text"}, {source: S3, locator: "lead"}], how_known: "As recorded."}
  languages_of_work: {value: ["French"], certainty: 1.0, cites: [{source: S1, locator: "Works"}, {source: S3, locator: "infobox"}], how_known: "French titles."}
  occupations: {value: ["novelist", "essayist", "critic", "translator"], certainty: 0.7, cites: [{source: S1, locator: "opening; Works"}, {source: S3, locator: "lead / Occupations"}], how_known: "Britannica + Wikipedia; translated Ruskin."}

contribution:
  fields: {value: ["literature"], certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "lead"}], how_known: "Britannica + Wikipedia EN."}
  lasting_original_contributions:
    - {value: "À la recherche du temps perdu (In Search of Lost Time)", year: 1913, kind: "work", lasting: "'The entire climate of the 20th-century novel was affected by À la recherche du temps perdu, which is one of the supreme achievements of modern fiction' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Works; Legacy"}, {source: S3, locator: "Notable work"}], how_known: "Britannica: volumes 1913–27; the last three posthumous."}
  evidence_of_impact:
    - {value: "Prix Goncourt (1919) for À l'ombre des jeunes filles en fleurs", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "Works"}], how_known: "Britannica: December 1919."}
  major_works:
    - {value: "Les Plaisirs et les jours", year: 1896, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "Works"}], how_known: "Britannica."}
    - {value: "Contre Sainte-Beuve", year: 1909, kind: "other", certainty: 0.5, cites: [{source: S1, locator: "Works"}], how_known: "Britannica: written c. 1908–09, published 1954; aesthetic essay, not a creed statement opened this pass."}
    - {value: "Correspondance (Kolb edition)", year: 1970, kind: "other", certainty: 0.5, cites: [{source: S4, locator: "note 1 (Kolb XIV)"}, {source: S5, locator: "Corr. citations"}], how_known: "Worldview letters cited via Kolb; print unread this pass."}
  honours:
    - {value: "Prix Goncourt", year: 1919, certainty: 0.7, cites: [{source: S1, locator: "Works"}], how_known: "Britannica."}
  definition_fit: {value: "clearly meets", rationale: "Affected the entire climate of the 20th-century novel (S1).", certainty: 0.7, cites: [{source: S1, locator: "Legacy"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "Father Catholic; mother Jewish (non-converting); Marcel baptized and confirmed Catholic", certainty: 0.7, cites: [{source: S1, locator: "Early life and education"}, {source: S3, locator: "Biography (baptized 5 Aug 1871 Saint-Louis-d'Antin; confirmed; never formally practised)"}], how_known: "Britannica + Wikipedia EN."}
  family_religious_practice: {value: "Raised in father's Catholic faith; later said he had not been to mass since first communion (adult letter; practice thin)", certainty: 0.5, cites: [{source: S3, locator: "Biography"}, {source: S6, locator: "letter to Rosny aîné, before 23 Dec 1919"}], how_known: "Wikipedia practice claim; Mimouni quotes Rosny letter (secondary)."}
  parents_and_household:
    - {value: "Father Adrien Proust, eminent physician of provincial French Catholic descent; mother Jeanne Clémence (Weil), from a wealthy German–Jewish family from Alsace", role: "family", certainty: 1.0, cites: [{source: S1, locator: "Early life and education"}, {source: S3, locator: "Biography / Parent(s)"}], how_known: "Britannica + Wikipedia EN."}
    - {value: "Brother Robert Proust", role: "sibling", certainty: 0.7, cites: [{source: S3, locator: "Relatives"}], how_known: "Wikipedia EN."}
  household_circumstances: {value: "Wealthy bourgeois Paris household; childhood holidays Illiers and Auteuil; asthma from childhood", certainty: 0.7, cites: [{source: S1, locator: "Early life and education"}, {source: S3, locator: "Biography"}], how_known: "Britannica + Wikipedia EN."}
  schooling:
    - {value: "Lycée Condorcet (1882–89; philosophy master Alphonse Darlu); School of Political Sciences; licences in law (1893) and literature (1895)", stage: "grammar or secondary school", certainty: 0.7, cites: [{source: S1, locator: "Early life and education"}, {source: S3, locator: "Education"}], how_known: "Britannica + Wikipedia EN."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading:
    - {value: "Ruskin (from c. 1899; translated Bible of Amiens and Sesame and Lilies); Carlyle; Emerson", certainty: 0.7, cites: [{source: S1, locator: "Works"}, {source: S3, locator: "Early writing"}], how_known: "Britannica + Wikipedia EN."}
  childhood_mentors:
    - {value: "Alphonse Darlu, philosophy master at Lycée Condorcet", certainty: 0.7, cites: [{source: S1, locator: "Early life and education"}], how_known: "Britannica."}
  languages_in_childhood: {value: ["French"], certainty: 0.7, cites: [{source: S3, locator: "infobox"}], how_known: "Wikipedia EN."}
  notable_events:
    - {value: "Baptized Catholic at Saint-Louis-d'Antin", year: 1871, age: 0, certainty: 0.7, cites: [{source: S3, locator: "Biography (5 August 1871)"}], how_known: "Wikipedia EN (citing White)."}
    - {value: "Mother's death left him grief-stricken and financially independent", year: 1905, certainty: 0.7, cites: [{source: S1, locator: "Works"}, {source: S3, locator: "Biography"}], how_known: "Britannica + Wikipedia EN."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1913–1922", certainty: 0.7, cites: [{source: S1, locator: "Works"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing read equating science and religion; L'Irréligion d'État (1892) is political anti-fanaticism about state irreligion, not a science–religion equation (S3)."}
  primary_system:
    value: BELOW_THRESHOLD
    how_known: "In-span letter to Lionel Hauser (early Sept 1915, Kolb Corr. XIV p. 218 via S4/S6): accepts the addressee's 'you haven't the Faith' and answers that religious preoccupation is never absent a day, and that the more religious one is the less one dares affirm beyond what one believes — lack of Faith without a scored denial of God, plus refusal of over-affirmation. Pre-span Straus 1908 denies belief in Heaven (S5; P31 continuity; afterlife, not God-locus). White/Wikipedia 'mystical atheist' is biographer label, not own words (S3). Candidates AGNOS (lead), ATHE (lead from biographer + Heaven line), SECHUM (no church practice; Rosny 1919 mass line) remain below 0.5 for the code (P19; Joyce pattern). CHRIST rejected for adult working years (baptism/confirmation are heritage; never formally practised)."
    note: "Named alternatives AGNOS / ATHE / SECHUM stay leads only. Novel narrator lines unused (P42)."
  secondary_system: {value: UNKNOWN, how_known: "No second system. Aesthetic mysticism / involuntary memory is a literary method, not a worldview code."}
  candidate_codes_considered:
    - {code: AGNOS, reason: "Lead: Hauser 1915 no-Faith + refuses affirmation beyond belief + continuous religious preoccupation; Topping notes correspondence 'frictions' rather than a pinned creed (S5)."}
    - {code: ATHE, reason: "Lead only: White 'mystical atheist' (S3) is biographer; Straus Heaven denial is afterlife, not God; Guermantes atheist-praise line is novel (P42 unused)."}
    - {code: SECHUM, reason: "Lead: no formal practice (S3; Rosny 1919); L'Irréligion d'État criticizes anti-clerical fanaticism without stating a humanist creed."}
    - {code: CHRIST, reason: "Rejected for adult working years: baptized/confirmed Catholic (heritage); never formally practised (S3); Hauser accepts lacking Faith."}
    - {code: JUDA, reason: "Heritage only: Jewish mother (S1; S3); Montesquiou 1896 names mother's Jewishness against his Catholic like father/brother — identity, not adult creed."}
  lio_axes:
    A_locus:
      value: BELOW_THRESHOLD
      how_known: "Hauser 1915 states lack of Faith and continuous religious preoccupation without locating God or denying God's existence (S4; S6). Straus 1908 denies Heaven, not God (S5). No first-person 'there is no God' / personal-God / acosmic identity read. Guermantes Way atheist-praise sentence is novel narrator (P42 unused). Not enough to score A 0–4 (P19; Joyce pattern)."
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P30); novelist — P16 only on own-voice nature/physical-world claims. Nothing read on nature's causal order. Contre Sainte-Beuve aesthetic method and Ruskin Gothic symbolism are art, not B."}
    C_ledger: {value: UNKNOWN, how_known: "Straus Heaven denial is a lead against personal afterlife; Bergotte 'not dead forever' novel line unused (P42). Not scored."}
    D_authority: {value: UNKNOWN, how_known: "Hauser refusal to affirm beyond belief is a lead against dogmatic authority; no scored D."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7)."}
  mid_basin: {value: UNKNOWN, how_known: "B is UNKNOWN, which takes precedence (P19); A is BELOW_THRESHOLD."}
  statements:
    - text: "… si je n'ai pas la Foi, comme tu dis, en revanche la préoccupation religieuse n'est jamais absente un jour de ma vie. … Mais plus on est religieux, moins on ose aller dans l'affirmation, au-delà de ce qu'on croit."
      cites: [{source: S4, locator: "quoting Kolb Corr. XIV p. 218"}, {source: S6, locator: "Hauser Sept 1915 / Corr. XIV p. 218"}]
      date: "1915-09"
      context: "Letter to cousin/financial adviser Lionel Hauser, early September 1915 (Kolb Correspondance tome XIV p. 218). In-span (major_work_period 1913–1922). Accepts addressee's 'you haven't the Faith'; affirms lifelong religious preoccupation; refuses affirmation beyond belief. Secondary quotations; Kolb print unread."
      axes: [A_locus, D_authority]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "French as given by de Vendeuvre (S4) and Mimouni (S6). AgoraVox/blog paraphrase adding 'je ne nie rien, je crois à la possibilité de tout' not used (not in S4/S6)."
    - text: "In Heaven's name, not a word about any of this to Mme Ganderax. In Heaven's name … in which, alas, neither of us believes."
      cites: [{source: S5, locator: "Corr. viii, 278 (1908 letter to Mme Straus)"}]
      date: "1908"
      context: "Letter to Mme Straus, 1908 (Kolb Corr. VIII p. 278), as quoted in English by Topping (S5). Pre-span; P31 continuity (no change_of_view documented). Denies belief in Heaven; Topping flags addressee-inflected 'frictions' in the correspondence. Secondary quotation; Kolb print unread."
      axes: [C_ledger, A_locus]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "English as Topping gives it; afterlife denial, not a God-locus statement."
    - text: "If I am Catholic like my father and brother, on the other hand, my mother is Jewish."
      cites: [{source: S3, locator: "citing Collège de France / Corr. II, 66 (Montesquiou, May 1896)"}]
      date: "1896-05"
      context: "Letter to Robert de Montesquiou, May 1896 (Kolb Corr. II p. 66), as summarized in English secondary sources via S3. Pre-span heritage identity statement; not used to score adult primary_system or A."
      axes: []
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Heritage context only; adult working years use Hauser/Straus instead."
    - text: "Je n'ai jamais été à la messe depuis ma première communion."
      cites: [{source: S6, locator: "letter to Rosny aîné, shortly before 23 Dec 1919 (Lettres, Plon, p. 926)"}]
      date: "1919-12"
      context: "Letter to Rosny aîné, late 1919 (in-span). Practice claim; Mimouni notes he exaggerated (wedding/funeral masses). Not a God-locus statement."
      axes: [D_authority]
      kind: "private letter"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "French as Mimouni quotes; Kolb/Lettres print unread."
  changes_over_life: []
  coder_notes: "Deepen D1 2026-10-24: queue need was A/B UNKNOWN with only Britannica. Own-words hunt found Hauser 1915 (in-span) and Straus 1908 (pre-span) via scholarly secondary quotations — enough to leave UNKNOWN→BELOW on primary and A, not enough to score AGNOS/ATHE or A 0–4 (P19; Joyce pattern). B left UNKNOWN (P16/P30). Guermantes Way atheist-praise and Bergotte immortality lines unused (P42). White 'mystical atheist' unused as biographer label. Kolb Correspondance print and Contre Sainte-Beuve full essay unread. Lane A separate from Lane B geometric labels. No fallacy_catalog (Jason)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "French bourgeois; maternal German–Jewish (Weil, Alsace); paternal provincial French Catholic", certainty: 0.7, cites: [{source: S1, locator: "Early life and education"}, {source: S3, locator: "Biography"}], how_known: "Britannica + Wikipedia EN."}
  religious_heritage_by_birth: {value: "Baptized and confirmed Roman Catholic (father's faith); mother Jewish", certainty: 0.7, cites: [{source: S1, locator: "Early life and education"}, {source: S3, locator: "Biography (baptized 5 Aug 1871 Saint-Louis-d'Antin; confirmed)"}], how_known: "Britannica + Wikipedia EN."}
  baptism_or_initiation: {value: "Baptized 5 August 1871, Church of Saint-Louis-d'Antin; later confirmed Catholic", certainty: 0.7, cites: [{source: S3, locator: "Biography (citing White)"}], how_known: "Wikipedia EN."}
  childhood_catechism: {value: "Raised in father's Catholic faith; later claimed no mass since first communion", certainty: 0.5, cites: [{source: S3, locator: "Biography"}, {source: S6, locator: "Rosny 1919"}], how_known: "Wikipedia + Mimouni secondary quote."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1913–1922", certainty: 0.7, cites: [{source: S1, locator: "Works"}, {source: S3, locator: "In Search of Lost Time"}], how_known: "Swann (1913) to his death (1922), his last act on the novel; the volumes of 1923–27 are posthumous (guide: posthumous work dated by the last act in life or the death year)."}
  age_at_first_lasting_contribution: {value: 42, certainty: 0.7, cites: [{source: S1, locator: "opening; Works"}], how_known: "1913 − 1871 = 42 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No axis scored at 3 or 4 (P27 anchor); Hauser 1915 is below-threshold lead only."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", rationale: "A BELOW_THRESHOLD; B UNKNOWN. Hauser 1915 is in-span but does not score an axis.", certainty: 0.5, cites: [{source: S4, locator: "Hauser 1915"}, {source: S5, locator: "Straus 1908"}], how_known: "Coder's reading."}
  worldview_during_major_work: {value: "No Faith (Hauser 1915) with continuous religious preoccupation and refusal to over-affirm; no scored God locus; no formal Catholic practice", certainty: 0.5, cites: [{source: S4, locator: "Hauser 1915"}, {source: S6, locator: "Rosny 1919"}, {source: S3, locator: "Biography"}], how_known: "In-span letters via secondary quotation; axes unscoreable (P19)."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "Novel of involuntary memory with circular construction and 'time regained' closure (S1); aesthetic, not a scored worldview geometry.", certainty: 0.5, cites: [{source: S1, locator: "Characters and themes"}], how_known: "Coder's reading of Britannica."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable to a scored LIO form."}
  circle_present: {value: "unclear", rationale: "Circular novel construction is literary architecture, not a return-to-God circle.", certainty: 0.5, cites: [{source: S1, locator: "Characters and themes"}], how_known: "Coder's reading."}
  reading: "No scored Lane A axes. Biographer 'mystical atheist' and novel religious allegory stay outside Lane A."
  notes: "Lane B separate from Lane A axis scores."

institutions: []
collaborators: []

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 203"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Worldview letters read only as secondary quotations (Kolb print unread)."
    - "AGNOS.md / ATHE.md / SECHUM.md remain stub system files if used as named alternatives (flag)."
  open_questions:
    - "Kolb Correspondance print (esp. XIV Hauser; VIII Straus) for full letter context."
    - "Contre Sainte-Beuve essay voice on metaphysics if any (beyond aesthetics)."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "George Duncan Painter"
    citation: "Painter, George Duncan. \"Marcel Proust.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Marcel-Proust. First read 2026-10-19 (scholars edition); deepen D1 re-read live body 2026-10-24 (AI Top Questions unused)."
    url: "https://www.britannica.com/biography/Marcel-Proust"
    accessed: 2026-10-24
    reliability_note: "Signed article. Body and header only; the AI-generated Top Questions are not cited. Novel's 'salvation' / 'human religious experience' framing is critic's reading of fiction, not a profession."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, heritage, timing, lane_b]
  - id: S2
    type: secondary
    kind: "database"
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [review]
  - id: S3
    type: tertiary
    kind: "encyclopedia"
    author: "Wikipedia contributors"
    citation: "Wikipedia contributors. \"Marcel Proust.\" Wikipedia. https://en.wikipedia.org/wiki/Marcel_Proust. Read live 2026-10-24 (P50 dual bio)."
    url: "https://en.wikipedia.org/wiki/Marcel_Proust"
    accessed: 2026-10-24
    reliability_note: "Dual-bio check against Britannica (P50). Agrees on birth 10 July 1871 Auteuil/Paris, death 18 Nov 1922 Paris, Swann 1913, Prix Goncourt 1919. Adds baptism 5 Aug 1871 Saint-Louis-d'Antin, confirmation, never formally practised; White 'mystical atheist' biographer label (note 8) — not own words, not scored. Guermantes Oxford-quote line is novel (P42)."
    source_quality: "reference entry"
    used_for: [identity, basics, childhood, heritage, worldview, review]
  - id: S4
    type: secondary
    kind: "journal article"
    author: "Isabelle de Vendeuvre"
    citation: "de Vendeuvre, Isabelle. \"Proust et l'Église. Grandeurs d'établissement et pouvoir du verbe.\" Revue d'histoire littéraire de la France 108, no. 2 (2008): 421–431. https://shs.cairn.info/revue-d-histoire-litteraire-de-la-france-2008-2-page-421. Quotes letter to Lionel Hauser, early Sept 1915, Kolb Correspondance XIV p. 218."
    url: "https://shs.cairn.info/revue-d-histoire-litteraire-de-la-france-2008-2-page-421?lang=fr"
    accessed: 2026-10-24
    reliability_note: "Peer-reviewed literary-history article; Hauser letter is secondary quotation from Kolb Plon edition (print unread this pass)."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview]
  - id: S5
    type: secondary
    kind: "book chapter"
    author: "Margaret Topping"
    citation: "Topping, Margaret. \"Religion.\" In Marcel Proust in Context, edited by Adam Watt, 137–144. Cambridge: Cambridge University Press, 2013. https://www.cambridge.org/core/books/marcel-proust-in-context/religion/4385292102D1D7A337C3858046CBABCA. English quotations of Corr. vi, 220 (Lauris 1906) and Corr. viii, 278 (Straus 1908)."
    url: "https://www.cambridge.org/core/books/marcel-proust-in-context/religion/4385292102D1D7A337C3858046CBABCA"
    accessed: 2026-10-24
    reliability_note: "Scholarly chapter; flags that Proust's desire to comfort addressees inflects belief evidence ('frictions'). Straus/Lauris lines are secondary English quotations; Kolb print unread."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview]
  - id: S6
    type: secondary
    kind: "other"
    author: "Patrick Mimouni"
    citation: "Mimouni, Patrick. \"Intellectuels et Anti-intellectuels chez Proust (IV).\" La Règle du Jeu, 1 July 2024. https://laregledujeu.org/2024/07/01/40734/intellectuels-et-anti-intellectuels-chez-proust-iv/. Corroborates Hauser Sept 1915 (Corr. XIV p. 218); quotes Rosny aîné letter before 23 Dec 1919 (Lettres, Plon, p. 926)."
    url: "https://laregledujeu.org/2024/07/01/40734/intellectuels-et-anti-intellectuels-chez-proust-iv/"
    accessed: 2026-10-24
    reliability_note: "Literary essay with Kolb/Lettres page cites; secondary quotation corroborating S4 on Hauser; Rosny mass line not independently verified in print."
    source_quality: "unofficial web copy"
    used_for: [worldview, childhood]
---

# Marcel Proust

## Summary

Marcel Proust (1871–1922), French novelist [S1; S3]. Deepen D1: primary_system and A BELOW_THRESHOLD; B UNKNOWN; mid_basin UNKNOWN. Not plotted. Chart-moving NO.

## Life and work

Auteuil / Paris; Lycée Condorcet; asthma; Dreyfusard; Ruskin translator; À la recherche 1913–27 (last three posthumous) [S1; S3].

## Contribution and impact

À la recherche du temps perdu; Prix Goncourt 1919 [S1].

## Childhood and education

Catholic father Adrien; Jewish mother Jeanne Weil; baptized 5 Aug 1871 Saint-Louis-d'Antin, confirmed; never formally practised [S1; S3].

## Adult working worldview

Hauser Sept 1915 (in-span): no Faith, lifelong religious preoccupation, refuses over-affirmation [S4; S6]. Straus 1908: neither believes in Heaven [S5]. White 'mystical atheist' biographer only [S3]. Novel lines unused (P42). primary and A BELOW_THRESHOLD; B UNKNOWN.

## Heritage (context only)

Catholic baptism/confirmation; Jewish mother [S1; S3]. Montesquiou 1896 Catholic-like-father identity line [S3].

## Timing

1913–1922, age 42 [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Circular novel construction; no scored Lane A axes.

## Open questions

- Kolb Correspondance print (Hauser XIV; Straus VIII).
- Contre Sainte-Beuve metaphysics if any.

## Research log

- 2026-10-19: Read Britannica (Painter).
- 2026-10-24: Deepen D1 — Wikipedia dual bio; de Vendeuvre Cairn Hauser quote; Topping Religion chapter Straus/Lauris; Mimouni Rosny/Hauser corroboration. Kolb print unread. Guermantes atheist-praise unused (P42).
