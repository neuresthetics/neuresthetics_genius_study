---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch D)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to visual_arts. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch D, order P32: F 5, rank 19). Basics and works from Britannica (Seitz), first part of the article only. No statement of his on religion, God or nature's order was read. Not a scientist. primary_system UNKNOWN; all axes UNKNOWN; mid_basin UNKNOWN. Draft, not reviewed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #19, F5 rank 19). P47 source_quality on every source. Dual-sourced birth/death/baptism (S1 Britannica prior read + S3 Wikipedia EN + S4 Wildenstein Tome I OCR). Adult religion: no Monet letter denying God found (ARTIC Wildenstein letter PDFs 403); Blanche Hoschedé posthumous notes via Wildenstein IV n.1327 (S5) — civil burial wish, non-practice, family free to follow their religion (reported speech); Levine 1994 p.66 and Butler 2008 p.202 call him atheist without quoting him (S6, S7 via Wikipedia footnote sentences). Clemenceau «pas de noir pour Monet» is Clemenceau's funeral act, not Monet's creed (S5). primary_system BELOW_THRESHOLD (lead ATHE); A_locus BELOW_THRESHOLD (no own locus/denial; P38 needs published disbelief); B_cause UNKNOWN (not a scientist; nothing on law/exception, P16); C/D/E UNKNOWN; mid_basin UNKNOWN (B UNKNOWN takes precedence, P19). Chart: still unplotted. No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: monet-claude
  display_name: "Claude Monet"
  roster:
    canonical_name: "Claude Monet"
    rank: 19
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: art
    field_bucket: arts
  full_name: {value: "Oscar-Claude Monet", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts ('In full')"}, {source: S3, locator: "infobox / Birth and childhood (Oscar-Claude)"}, {source: S4, locator: "baptism register note (Oscar-Claude)"}], how_known: "Britannica + Wikipedia EN + Wildenstein Tome I (dual/triple-source)."}
  native_name: {value: "Oscar-Claude Monet", certainty: 0.7, cites: [{source: S4, locator: "baptism; parents called him Oscar"}], how_known: "French birth/baptismal name as in Wildenstein; same Latin orthography as English."}
  aliases:
    - {name: "Claude-Monet", kind: "roster alias"}
    - {name: "Monet-Claude", kind: "roster alias"}
    - {name: "Oscar Monet", kind: "other"}

basics:
  birth:
    date: {value: "1840-11-14", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Quick Facts; opening sentence"}, {source: S3, locator: "infobox; Birth and childhood"}, {source: S4, locator: "Né le 14 novembre 1840"}], how_known: "Britannica + Wikipedia EN + Wildenstein Tome I."}
    place: {value: "Paris (45 rue Laffitte)", modern_name: "Paris, France", polity_then: "Kingdom of France (July Monarchy)", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S3, locator: "Birth and childhood (45 rue Laffitte)"}, {source: S4, locator: "rue Laffitte / Notre-Dame-de-Lorette"}], how_known: "Britannica + Wikipedia EN + Wildenstein Tome I."}
  death:
    date: {value: "1926-12-05", calendar: gregorian, certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S3, locator: "infobox; Death"}, {source: S5, locator: "Havas telegram note; funeral narrative 5–8 Dec 1926"}], how_known: "Britannica + Wikipedia EN + Wildenstein Tome IV."}
    place: {value: "Giverny", modern_name: "Giverny, France", polity_then: "French Third Republic", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S3, locator: "infobox; Death"}, {source: S5, locator: "Giverny property; cemetery"}], how_known: "Britannica + Wikipedia EN + Wildenstein Tome IV."}
  first_lasting_contribution_year: {value: 1865, certainty: 0.5, cites: [{source: S1, locator: "Early work ('In the beach and sea pictures of 1865–67...')"}, {source: S3, locator: "Return to Paris / Impressionism (Salon debuts 1865; Impression, Sunrise exhibited 1874)"}], how_known: "Start year of the range Britannica gives for the pictures that show his advance toward the Impressionist style (P12). Dated by painting years, not by first public showing of Impression, Sunrise (1874), so 0.5; the coder's choice of these pictures as the first lasting item is an inference (P24). Alternative dating event: 1874 First Impressionist Exhibition."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "Early work"}, {source: S3, locator: "Years active 1865–1926"}], how_known: "Every candidate year (1865–1874) is in this bucket (P2); birth dual-sourced."}
  region_of_birth: {value: "Western Europe", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts"}, {source: S3, locator: "Birth and childhood"}], how_known: "France (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "opening; Early work"}, {source: S3, locator: "Giverny; Argenteuil; Normandy"}], how_known: "Paris, Normandy, Giverny (main career); short trips to London/Italy noted but not a second region of work."}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S1, locator: "text"}, {source: S3, locator: "infobox"}], how_known: "As recorded."}
  languages_of_work: {value: [French], certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S5, locator: "letters cited in French"}], how_known: "French painter; letters in French (Wildenstein)."}
  occupations: {value: ["painter"], certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "opening"}], how_known: "Britannica + Wikipedia EN."}

contribution:
  primary_domain: visual_arts
  fields: {value: ["painting"], certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "opening"}], how_known: "Britannica + Wikipedia EN."}
  lasting_original_contributions:
    - {value: "Impressionist method: recording on the spot the impression of a momentary view, in broken touches", year: "1865–67", kind: method, lasting: "he was 'the initiator, leader, and unswerving advocate of the Impressionist style' (S1); name of the movement from Impression, Sunrise (1874) (S3)", certainty: 0.5, cites: [{source: S1, locator: "opening; Early work"}, {source: S3, locator: "opening; Impressionism"}], how_known: "Britannica + Wikipedia EN; the start year is the range Britannica gives for the pictures that show the advance (inference, 0.5)."}
    - {value: "Series painting: repeated studies of one motif under changing light (stacks of wheat, Rouen Cathedral)", year: "1890–1894", kind: method, lasting: "exhibited in groups; a model for later serial art", certainty: 0.7, cites: [{source: S1, locator: "opening ('stacks of wheat (1890/91 [...]) and the Rouen Cathedral (1894)')"}, {source: S3, locator: "Giverny / Method (haystacks, Rouen Cathedral)"}], how_known: "Britannica + Wikipedia EN."}
    - {value: "Water-lily paintings from his pond at Giverny, his last series", year: "before 1926", kind: "body of work", lasting: "his last series; Orangerie decorative cycle", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "Water lilies; Death"}], how_known: "Britannica + Wikipedia EN; the span end is the death cap (P30)."}
  evidence_of_impact:
    - {value: "Name 'Impressionism' taken from his Impression, Sunrise at the 1874 independent exhibition", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S3, locator: "opening; Impressionism (Leroy review)"}], how_known: "Wikipedia EN summarizing the standard account."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Initiator of Impressionism; series and water lilies.", certainty: 0.7, cites: [{source: S1, locator: "opening sentence"}, {source: S3, locator: "opening"}], how_known: "Britannica + Wikipedia EN."}

childhood:
  family_religion: {value: "Roman Catholic (baptized)", certainty: 0.5, cites: [{source: S3, locator: "Birth and childhood (baptised Catholic)"}, {source: S4, locator: "baptême Notre-Dame de Lorette, 20 mai 1841"}], how_known: "Baptism in a Catholic parish is recorded; household practice not described. Certainty 0.5 (heritage inference from baptism, not a family creed statement)."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father Claude-Adolphe Monet (wholesale merchant / ship-chandler and grocer); mother Louise-Justine Aubrée Monet (singer); family moved to Le Havre area when he was about five; after mother's death (1857) lived with aunt Marie-Jeanne Lecadre", certainty: 0.7, cites: [{source: S1, locator: "Childhood section"}, {source: S3, locator: "Birth and childhood"}, {source: S4, locator: "parents; Lecadre"}], how_known: "Britannica + Wikipedia EN + Wildenstein Tome I."}
  household_circumstances: {value: "Father in family grocery and ship-chandlering near Le Havre; mother supported art ambitions; father preferred business career", certainty: 0.7, cites: [{source: S1, locator: "Childhood section"}, {source: S3, locator: "Birth and childhood"}], how_known: "Britannica + Wikipedia EN."}
  schooling:
    - {value: "Drawing lessons with a local artist (Jacques-François Ochard); later the Académie Suisse and Gleyre's atelier in Paris", stage: other, certainty: 0.7, cites: [{source: S1, locator: "Childhood section; Early work"}, {source: S3, locator: "Birth and childhood; First stay in Paris / Return to Paris"}], how_known: "Britannica + Wikipedia EN."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors:
    - {value: "Eugène Boudin, who introduced him to painting in the open air", certainty: 0.7, cites: [{source: S1, locator: "Childhood section"}, {source: S3, locator: "Birth and childhood"}], how_known: "Britannica + Wikipedia EN."}
  languages_in_childhood: {value: [French], certainty: 0.7, cites: [{source: S4, locator: "Paris / Le Havre household"}], how_known: "French household."}
  notable_events:
    - {value: "Baptized 20 May 1841 at Notre-Dame-de-Lorette, Paris, as Oscar-Claude", certainty: 1.0, cites: [{source: S3, locator: "Birth and childhood"}, {source: S4, locator: "extrait du registre paroissial; 20 mai 1841"}], how_known: "Wikipedia EN + Wildenstein Tome I (parish register)."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1865–1926", certainty: 0.5, cites: [{source: S1, locator: "Early work; opening"}, {source: S3, locator: "Years active 1865–1926"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No first-person statement of his equating or opposing science and religion was read. ARTIC Wildenstein letter PDFs blocked (403); IA OCR of catalogue volumes searched for athée / religion / Dieu as creed claims — only conventional 'mon Dieu' exclamations and scholarly narrative of 'réserve en matière de religion' (S4)."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "Scholarly labels (Levine; Butler) plus family memoir of non-practice and civil burial (Blanche Hoschedé via Wildenstein IV), all without a Monet letter or published denial of God.", note: "Lead ATHE from Levine ('Monet's own atheism') and Butler ('the atheist Claude Monet') and from civil burial / non-practice reported by Blanche Hoschedé-Monet. Not scored ATHE: no own written or recorded 'I do not believe in God' (P38 needs that for A 4 even at 0.5). Baptism alone does not make adult CHRIST. Clemenceau's funeral cloth is Clemenceau's act."}
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: ATHE, reason: "Lead: Levine 1994 p.66 and Butler 2008 p.202 assert atheism; Blanche Hoschedé notes (Wildenstein IV n.1327) — civil burial because he did not practice. Rejected as scored code: no Monet own-words denial of God read."}
    - {code: CHRIST, reason: "Rejected for adult working years: Catholic baptism 1841 is heritage; adult civil funeral and non-practice (reported) contradict practicing CHRIST."}
    - {code: AGNOS, reason: "No suspension-of-judgment language from Monet read; scholars use 'atheist', not 'agnostic'."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, note: "Scholarly 'atheist' labels and reported non-practice / civil burial speak to disbelief without locating God (in / above / as Nature) and without Monet's own published denial. Named reading: 4 (ATHE locus) if a letter or interview with explicit disbelief is opened; Joyce precedent (church/practice rejection without God-view → BELOW).", how_known: "BELOW_THRESHOLD under P19 (weak/indirect; reported speech and scholarly reconstruction)."}
    B_cause: {value: UNKNOWN, how_known: "Not a scientist (P16). Researched: Britannica, Wikipedia, Wildenstein I/IV OCR — no statement of his about nature's causal order (law vs exception). Impressionist light/atmosphere painting is method, not a B claim."}
    C_ledger: {value: UNKNOWN, how_known: "Nothing scored on reward or afterlife in the sources read."}
    D_authority: {value: UNKNOWN, how_known: "Nothing on revelation vs observation as authority (P19)."}
    E_scope: {value: UNKNOWN, how_known: "Nothing on the world's order as one/many (P7)."}
  mid_basin: {value: UNKNOWN, how_known: "B_cause is UNKNOWN, which takes precedence (§6, P19); A_locus is BELOW_THRESHOLD."}
  statements:
    - text: "Il avait toujours dit qu'il voulait être enterré civilement, car il ne pratiquait pas, mais n'empêchait pas les siens de suivre leur religion. Il avait aussi recommandé que ses obsèques soient aussi simples que possible et dans la plus stricte intimité."
      cites: [{source: S5, locator: "note 1327 (Notes posthumes de Blanche Hoschedé-Monet, p. 164)"}]
      date: "1926"
      context: "Blanche Hoschedé-Monet posthumous notes as quoted by Wildenstein Tome IV n.1327, reporting Monet's lifelong wish for a civil burial and non-practice. Reported speech / family memoir, not Monet's own hand. Funeral Dec 1926 was civil."
      kind: "reported speech"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Underwrites BELOW_THRESHOLD for A / primary lead ATHE; not scored ATHE/A4 (no Monet-authored denial of God)."
    - text: "Much closer to Monet's own atheism and pessimism is Schopenhauer, already introduced to the impressionist circle in the criticism of Theodore Duret in the 1870s and whose influence in France was at its peak in 1886, the year of The World as Will and Idea."
      cites: [{source: S6, locator: "ch. 6, p. 66 (sentence as printed in Wikipedia EN footnote citing Levine)"}, {source: S3, locator: "Birth and childhood footnote [5]"}]
      date: "1994"
      context: "Steven Z. Levine, Monet, Narcissus, and Self-Reflection (University of Chicago Press, 1994). Page not opened this pass; wording taken from the Wikipedia EN footnote that cites Levine p.66."
      kind: "other"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Scholarly assertion of Monet's atheism without a Monet quotation in the cited sentence. Ceiling scholarly_reconstruction 0.5; does not by itself score ATHE/A4."
    - text: "Then Monet took the end of his brush and drew some long straight strokes in the wet pigment across her chest. It's not clear, and probably not consciously intended by the atheist Claude Monet, but somehow the suggestion of a Cross lies there on her body."
      cites: [{source: S7, locator: "p. 202 (sentence as printed in Wikipedia EN footnote citing Butler)"}, {source: S3, locator: "Birth and childhood footnote [6]"}]
      date: "2008"
      context: "Ruth Butler, Hidden in the Shadow of the Master (Yale, 2008), on Camille's deathbed portrait. Page not opened this pass; wording from Wikipedia EN footnote."
      kind: "other"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Passing scholarly 'atheist' label; no Monet quotation."
    - text: "Claude, sans se départir de sa réserve en matière de religion, fait une concession importante qui permet à Mme Hoschedé d'exercer une sorte d'apostolat."
      cites: [{source: S4, locator: "Vétheuil / baptism of Michel narrative"}]
      date: "1879"
      context: "Wildenstein Tome I narrative of Monet consenting to a child's baptism while keeping his reserve on religion (Vétheuil period). Scholarly narrative, not Monet's own words."
      kind: "other"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Context for adult reserve; not a locus claim."
  changes_over_life: []
  coder_notes: "Deepen 2026-10-24: Wikipedia atheism cites Levine/Butler — both unread as full pages; sentences only via wiki footnotes. ARTIC letter PDFs 403. No Monet 'je ne crois' found in Wildenstein I/IV OCR. Chart stays unplotted (A BELOW, B UNKNOWN)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "French", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "opening"}], how_known: "Britannica + Wikipedia EN."}
  religious_heritage_by_birth: {value: "Roman Catholic (baptized)", certainty: 0.5, cites: [{source: S3, locator: "Birth and childhood"}, {source: S4, locator: "baptême 20 mai 1841"}], how_known: "Baptism recorded; family creed not separately stated (0.5)."}
  baptism_or_initiation: {value: "Baptized Oscar-Claude, Notre-Dame-de-Lorette, Paris, 20 May 1841", certainty: 1.0, cites: [{source: S3, locator: "Birth and childhood"}, {source: S4, locator: "registre paroissial"}], how_known: "Wikipedia EN + Wildenstein Tome I (parish register extract)."}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1865–1926", certainty: 0.5, cites: [{source: S1, locator: "Early work; opening"}, {source: S3, locator: "Years active 1865–1926"}], how_known: "First listed item (1865, start of 1865–67) to the water lilies, whose end is the death cap 1926 (P29, P30); 0.5 because both ends are inferred / roster-style active years."}
  age_at_first_lasting_contribution: {value: 25, certainty: 0.5, cites: [{source: S1, locator: "Quick Facts; Early work"}, {source: S3, locator: "birth 1840; 1865 works"}], how_known: "1865 − 1840 = 25 (P30); takes the 0.5 of the year."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No statement scored at 3 or 4 (P27); A and B not plottable."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", rationale: "A BELOW_THRESHOLD and B UNKNOWN — nothing scored as a LIO-type view at plottable certainty.", certainty: 0.5, cites: [{source: S5, locator: "n.1327"}, {source: S6, locator: "p. 66"}], how_known: "Absence of scored axes."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "No childhood geometry/mathematics evidence read beyond ordinary schooling mention.", certainty: 0.5, cites: [{source: S1, locator: "Childhood section"}], how_known: "No evidence."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "Childhood section"}], how_known: "No evidence."}
  circle_present: {value: "unclear", rationale: "Impressionist circle is artistic, not a geometric-form belief circle.", certainty: 0.5, cites: [{source: S3, locator: "Impressionism"}], how_known: "No Lane B circle evidence."}
  reading: "As belief, not finding: unclear. Does not test H1."
  notes: "Lane A worldview deepen does not supply Lane B geometric-form evidence."

institutions: []
collaborators:
  - {value: "Eugène Boudin", relation: teacher, certainty: 0.7, cites: [{source: S1, locator: "Childhood section"}, {source: S3, locator: "Birth and childhood"}], how_known: "Britannica + Wikipedia EN."}
  - {value: "Frédéric Bazille, Alfred Sisley and Pierre-Auguste Renoir", relation: collaborator, note: "met in Gleyre's atelier", certainty: 0.7, cites: [{source: S1, locator: "Childhood section"}, {source: S3, locator: "Return to Paris"}], how_known: "Britannica + Wikipedia EN."}
  - {value: "Georges Clemenceau", relation: other, note: "friend/patron; at deathbed and funeral; 'pas de noir pour Monet' is Clemenceau's act", certainty: 0.7, cites: [{source: S3, locator: "Death; Patrons"}, {source: S5, locator: "n.1334"}], how_known: "Wikipedia EN + Wildenstein Tome IV."}

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 19"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Britannica live fetch 403 this deepen; S1 claims rest on the 2026-10-15 partial read (through Early work) plus dual-sourcing from Wikipedia/Wildenstein for basics."
    - "ARTIC Wildenstein letter PDF volumes 403 — Monet's own letters on religion not read in scholarly letter edition."
    - "Levine 1994 and Butler 2008 pages not opened; atheism sentences known only via Wikipedia footnotes quoting them."
  open_questions:
    - "Open Wildenstein letter volumes (ARTIC OCR PDFs or print) for any first-person creed statement."
    - "Open Levine p.66 and Butler p.202 in the books themselves; check whether either cites a Monet letter."
    - "Blanche Hoschedé-Monet notes / J.-P. Hoschedé 1961 memoir — primary family texts beyond Wildenstein's footnote."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "William C. Seitz"
    citation: "Seitz, William C. \"Claude Monet.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Claude-Monet."
    url: "https://www.britannica.com/biography/Claude-Monet"
    accessed: 2026-10-15
    reliability_note: "Signed encyclopedia article; read through the 'Early work' section on 2026-10-15. Live fetch 403 on deepen 2026-10-24 — prior partial read stands for contribution/childhood; basics dual-sourced elsewhere."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, collaborators]
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
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia. \"Claude Monet.\" https://en.wikipedia.org/wiki/Claude_Monet (accessed 2026-10-24)."
    url: "https://en.wikipedia.org/wiki/Claude_Monet"
    accessed: 2026-10-24
    reliability_note: "Used for dual-source basics, baptism date/place, Impressionism exhibition history, and funeral narrative; atheism claim not taken from Wikipedia alone — followed to Levine/Butler footnote sentences (S6, S7)."
    source_quality: "other"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, collaborators, review]
  - id: S4
    type: secondary
    kind: scholarly book
    author: "Daniel Wildenstein"
    citation: "Wildenstein, Daniel. Claude Monet: Biographie et catalogue raisonné, Tome I. Lausanne/Paris: Bibliothèque des Arts / Wildenstein Institute. Internet Archive OCR: c.rclaudemonettomeiwildensteininstitute."
    url: "https://archive.org/details/c.rclaudemonettomeiwildensteininstitute"
    accessed: 2026-10-24
    reliability_note: "Scholarly catalogue raisonné biography; baptism from parish register extract. Archive OCR only — typos possible (P47 archive scan)."
    source_quality: "archive scan (OCR only)"
    used_for: [identity, basics, childhood, worldview, heritage]
  - id: S5
    type: secondary
    kind: scholarly book
    author: "Daniel Wildenstein"
    citation: "Wildenstein, Daniel. Claude Monet: Biographie et catalogue raisonné, Tome IV: 1899–1926, Peintures. Wildenstein Institute. Internet Archive OCR: c.rclaudemonettomeivwildensteininstitute."
    url: "https://archive.org/details/c.rclaudemonettomeivwildensteininstitute"
    accessed: 2026-10-24
    reliability_note: "Funeral narrative; n.1327 quotes Blanche Hoschedé-Monet posthumous notes on civil burial / non-practice; n.1334 Clemenceau 'pas de noir pour Monet'. Archive OCR only."
    source_quality: "archive scan (OCR only)"
    used_for: [basics, worldview, timing, collaborators]
  - id: S6
    type: secondary
    kind: scholarly book
    author: "Steven Z. Levine"
    citation: "Levine, Steven Z. Monet, Narcissus, and Self-Reflection: The Modernist Myth of the Self. University of Chicago Press, 1994, ch. 6, p. 66."
    url: "https://press.uchicago.edu/ucp/books/book/chicago/M/bo3621518.html"
    accessed: 2026-10-24
    reliability_note: "Scholarly monograph. Page not opened this pass (IA borrow 401); the atheism sentence is known as quoted in the Wikipedia EN footnote citing Levine p.66."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview]
  - id: S7
    type: secondary
    kind: scholarly book
    author: "Ruth Butler"
    citation: "Butler, Ruth. Hidden in the Shadow of the Master: The Model-Wives of Cézanne, Monet, and Rodin. Yale University Press, 2008, p. 202."
    url: "https://yalebooks.yale.edu/book/9780300164503/hidden-in-the-shadow-of-the-master/"
    accessed: 2026-10-24
    reliability_note: "Scholarly monograph. Page not opened this pass; 'atheist Claude Monet' sentence known as quoted in the Wikipedia EN footnote citing Butler p.202."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview]
---

# Claude Monet

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Claude Monet (1840–1926), French painter, initiator and leader of Impressionism, known for series paintings of one motif under changing light and for the water lilies of Giverny [S1][S3]. Baptized Catholic (1841); adult years: scholars call him an atheist without quoting him, and family notes report non-practice and a civil-burial wish — no Monet letter denying God was read [S4][S5][S6][S7]. Draft deepen: primary_system BELOW_THRESHOLD (lead ATHE); A BELOW_THRESHOLD; B UNKNOWN; mid_basin UNKNOWN — still unplotted.

## Life and work

Born Paris 14 November 1840; baptized Notre-Dame-de-Lorette 20 May 1841; raised near Le Havre; Boudin; Paris (Académie Suisse, Gleyre); Argenteuil; Giverny from 1883; died Giverny 5 December 1926; civil funeral [S1][S3][S4][S5].

## Contribution and impact

Impressionist method; *Impression, Sunrise* (exhibited 1874) named the movement; series (haystacks, Rouen Cathedral); water lilies [S1][S3].

## Childhood and education

Son of Claude-Adolphe and Louise-Justine; drawing lessons; Boudin; Académie Suisse and Gleyre [S1][S3][S4].

## Adult working worldview

No first-person creed letter read. Blanche Hoschedé-Monet notes (via Wildenstein IV): civil burial because he did not practice, while not stopping the family from their religion [S5]. Levine and Butler label him an atheist in passing [S6][S7]. Clemenceau's «pas de noir pour Monet» is Clemenceau's funeral gesture [S5]. Not a scientist; no law/exception claim for B [P16]. A BELOW_THRESHOLD; B UNKNOWN; primary BELOW_THRESHOLD (lead ATHE).

## Heritage (context only)

French; baptized Roman Catholic 1841 [S3][S4].

## Timing

First lasting item 1865 (0.5), at 25; alternative public dating 1874. Working years 1865–1926 (0.5).

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Unclear. Does not test H1.

## Open questions

- ARTIC / print Wildenstein letter volumes for a first-person creed line.
- Levine p.66 and Butler p.202 in the books (does either cite a Monet letter?).
- Blanche Hoschedé notes / Hoschedé 1961 memoir beyond the Wildenstein footnote.

## Research log

- 2026-10-15: Read Britannica (Seitz) through 'Early work'. The Met essay fetch timed out.
- 2026-10-24: Deepen D1. Wikipedia EN full bio; Wildenstein Tome I and IV IA OCR; Levine/Butler sentences via wiki footnotes; ARTIC letter PDFs 403; Britannica live 403; Met 429. No fallacy_catalog (Jason).
