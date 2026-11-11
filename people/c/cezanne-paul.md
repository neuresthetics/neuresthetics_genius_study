---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA7; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to 20c_early. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA7, order P32: F 3, rank 208). Source: Britannica, signed by René Huyghe (scholars edition, read in full). Lasting work: the last Bathers (1900–05), 'groundbreaking'; identified as Bathers (Les Grandes Baigneuses), National Gallery, London, NG6359, which the Gallery says 'was finished in 1905' and calls 'hugely influential on early twentieth-century modern art, particularly Cubism' (S3; the Barnes and Philadelphia versions run to 1906), which clearly inspired Picasso's Les Demoiselles d'Avignon (1907); his approach 'laid the foundation for Picasso and other artists' subsequent explorations with Cubism' (S1). Not exhibited in his life (the 1907 retrospective was posthumous), so dated by the last documented act, completion 1905 (posthumous rule), at 0.5; alternatives 1906 (death) and 1907 (first showing). Span 1905, age 66. 'Most significant precursor of 20th-century formal abstraction' is body-of-work praise, undated, not used to extend the span. Worldview: no own words on belief read. primary_system UNKNOWN; A UNKNOWN; not a scientist; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #195/228, F3 rank 208). Goals: letters own words if any (Gasquet careful — contested); keep silence if none; do not force plot. Dual bio Wikipedia EN (S4, P50) + Britannica create-pass (S1): baptism Église de la Madeleine 1839; 1891 turn to Catholicism; Saint-Pierre burial. Own words: Courtauld MS letter to Émile Bernard, 15 Apr 1904 (S5; Danchev Letters no. 233 / Rewald stream) — 'Spectacle que le Pater omnipotens [oeterne Deus] étale devant nos yeux' (Mass/Credo language, in-span). Artforum Reff 1977 (S6) notes regular worship at Aix cathedral in last years and that the phrase may be liturgical habit / deference to devout Bernard. Merleau-Ponty 'Cézanne's Doubt' (S7) and Telegraph Sacred Mysteries (S8) report Alexis fear-of-hell speech ('roasting in aeternum') — reported speech only, not scored alone. Gasquet Cézanne 1921 conversations contested (Doran Conversations preface: imperious editing / unscholarly) — aesthetic 'one with my picture' / pantheist leads unused (P42; standing: painting/nature ≠ PANT or B). primary UNKNOWN→CHRIST @0.5 Roman Catholic (letter + late practice; alt BELOW). A UNKNOWN→0 @0.5 (Pater Omnipotens spreads spectacle = transcendent personal; alt BELOW deference/naming-without-locus Bach parallel). B UNKNOWN (not scientist; P16/P30). C/D/E UNKNOWN. mid UNKNOWN (B UNKNOWN, P19). Chart-moving NO. P47 S1–S8. No fallacy_catalog; no figures/. Draft, not reviewed."}

identity:
  id: cezanne-paul
  display_name: "Paul Cézanne"
  roster:
    canonical_name: "Paul Cézanne"
    rank: 208
    F: 3
    models: [Claude, Gemini, GPT]
    band: "core (3–4)"
    status: "core"
    field: "art"
    field_bucket: "arts"
  full_name: {value: "Paul Cézanne", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S4, locator: "lede"}], how_known: "Britannica + Wikipedia."}
  native_name: {value: "Paul Cézanne", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S4, locator: "lede"}], how_known: "French form."}
  aliases:
    - {name: "Cézanne-Paul", kind: "roster alias"}
    - {name: "Paul-Cezanne", kind: "roster alias"}
    - {name: "Pau Cesana", kind: "other"}

basics:
  birth:
    date: {value: "1839-01-19", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S4, locator: "infobox"}], how_known: "Britannica + Wikipedia."}
    place: {value: "Aix-en-Provence", modern_name: "Aix-en-Provence, France", polity_then: "France", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S4, locator: "Early years"}], how_known: "Two sources."}
  death:
    date: {value: "1906-10-22", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S4, locator: "infobox / Death"}], how_known: "Two sources."}
    place: {value: "Aix-en-Provence", modern_name: "Aix-en-Provence, France", polity_then: "France", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S4, locator: "Death"}], how_known: "Two sources; buried Saint-Pierre Cemetery (S4)."}
  first_lasting_contribution_year: {value: 1905, certainty: 0.5, cites: [{source: S1, locator: "Final years; Legacy"}, {source: S3, locator: "Overview"}], how_known: "Bathers NG6359, 'finished in 1905' (S3), not shown in his life; dated by completion (posthumous rule). Alternatives 1906 (death year) and 1907 (Salon d'Automne retrospective)."}
  era_bucket: {value: "1850 to 1949", certainty: 1.0, cites: [{source: S1, locator: "Final years"}], how_known: "1905 and each alternative (P2)."}
  region_of_birth: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "France (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "Final years"}], how_known: "Aix-en-Provence."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["French"], certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S5, locator: "letter French"}], how_known: "French letters and life."}
  occupations: {value: ["painter"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}

contribution:
  era_bucket: 20c_early
  fields: {value: ["painting"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Bathers (Les Grandes Baigneuses), National Gallery, London, NG6359", year: 1905, kind: "work", lasting: "'Picasso created his seminal Les Demoiselles d'Avignon ... clearly inspired by Cézanne's groundbreaking Bathers of 1900–05'; his approach 'laid the foundation for ... Cubism' (S1)", certainty: 0.5, cites: [{source: S1, locator: "Final years; Legacy"}, {source: S3, locator: "Overview"}], how_known: "Britannica; National Gallery: 'may date from 1898–9 and was finished in 1905'; 'had a lasting impact on Picasso and Matisse' (S3). Dated by completion (posthumous rule), alternatives 1906 and 1907."}
  evidence_of_impact:
    - {value: "Picasso: 'the father of us all'", kind: "assessment by a later major figure", certainty: 0.7, cites: [{source: S1, locator: "Legacy"}, {source: S4, locator: "Influence"}], how_known: "Britannica + Wikipedia."}
    - {value: "'the most significant precursor of 20th-century formal abstraction in painting'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "Legacy"}], how_known: "Britannica."}
  major_works:
    - {value: "The House of the Suicide", year: 1873, kind: "artwork", certainty: 0.7, cites: [{source: S1, locator: "Impressionist years"}], how_known: "Britannica."}
    - {value: "The Card Players", year: 1892, kind: "artwork", certainty: 0.7, cites: [{source: S1, locator: "Development of his mature style"}], how_known: "Britannica: 1890–92."}
    - {value: "Mont Sainte-Victoire paintings", year: 1902, kind: "artwork", certainty: 0.7, cites: [{source: S1, locator: "Final years"}], how_known: "Britannica: 1898–1902."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Foundation for Cubism (S1).", certainty: 0.7, cites: [{source: S1, locator: "Legacy"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "Roman Catholic (baptized)", certainty: 0.5, cites: [{source: S4, locator: "Early years (baptized Église de la Madeleine, 22 February)"}], how_known: "Infant baptism recorded; household creed not separately described (0.5)."}
  family_religious_practice: {value: UNKNOWN, how_known: "Sister Marie later devout; childhood practice not stated beyond baptism (S4; S8)."}
  parents_and_household:
    - {value: "Father Louis-Auguste Cézanne (milliner, later banker); mother Anne-Élisabeth-Honorine Aubert; sisters Marie and Rose", role: "family", certainty: 0.7, cites: [{source: S1, locator: "Early life and work"}, {source: S4, locator: "Early years"}], how_known: "Britannica + Wikipedia."}
  household_circumstances: {value: "Well-to-do bourgeois; father's bank secured his income", certainty: 0.7, cites: [{source: S1, locator: "Early life and work"}, {source: S4, locator: "Early years"}], how_known: "Two sources."}
  schooling:
    - {value: "Saint Joseph school; Collège Bourbon, Aix (classical education; friendship with Zola); law school, Aix (two years); Académie Suisse, Paris", certainty: 0.7, cites: [{source: S1, locator: "Early life and work"}, {source: S4, locator: "Early years / Studies in Paris"}], how_known: "Two sources."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["French"], certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Inferred from Aix bourgeois household."}
  notable_events:
    - {value: "Baptized 22 February 1839, Église de la Madeleine, Aix (godparents grandmother and uncle Louis)", year: 1839, age: 0, certainty: 0.7, cites: [{source: S4, locator: "Early years"}], how_known: "Wikipedia."}

worldview:
  unit: "adult working worldview"
  working_years: {value: "1905", certainty: 0.5, cites: [{source: S1, locator: "Final years"}], how_known: "Equals timing.major_work_period; Bernard letter 1904 sits at the edge of the Bathers completion year."}
  nominal_affiliations:
    - {value: "Roman Catholic (baptized; returned to regular practice c. 1891; Mass/cathedral attendance in last years reported)", certainty: 0.5, cites: [{source: S4, locator: "Early years; 1891 turn to Catholicism"}, {source: S6, locator: "cathedral worship note"}, {source: S8, locator: "return to practising faith"}], how_known: "Wikipedia + Reff + Telegraph; practice is secondary report, not a score by itself (CHRIST do_not_use membership alone)."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing read equating science and religion."}
  primary_system:
    value: CHRIST
    basis: consistent_private_letters
    certainty: 0.5
    cites: [{source: S5, locator: "Courtauld MS 15 Apr 1904 Pater Omnipotens"}, {source: S4, locator: "1891 turn to Catholicism"}, {source: S6, locator: "cathedral worship; deference note"}]
    rationale: "In-span own letter to Bernard (15 Apr 1904, Courtauld MS / Danchev no. 233) uses Mass/Credo language — 'Spectacle que le Pater omnipotens oeterne Deus étale devant nos yeux' — naming the Almighty Father who spreads nature's spectacle (S5). Secondary sources place a return to Catholic practice around 1891 and regular worship at Aix cathedral in the last years (S4; S6; S8). Branch: Roman Catholic. Cap 0.5: single letter (not a run of creed letters); Reff notes possible liturgical habit / deference to devout Bernard (S6); Merleau-Ponty/Alexis fear-of-hell motive is reported speech (S7; S8)."
    alternatives:
      - {value: BELOW_THRESHOLD, note: "If the Mass phrase is courtesy to Bernard and practice is fear-driven convention without professed Christian belief beyond habit.", cites: [{source: S6, locator: "deference / liturgical habit"}, {source: S7, locator: "fear of death motive"}]}
    how_known: "Own private letter (S5) plus secondary practice reports (S4; S6; S8). CHRIST use_when: own writing shows Christian belief; baptism alone rejected (do_not_use)."
    note: "Gasquet conversations unused for primary (contested; Doran). Painting/nature subject ≠ PANT."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Scored @0.5: Bernard 1904 Mass language + late Catholic practice (S5; S4; S6)."}
    - {code: PANT, reason: "Rejected: Mont Sainte-Victoire / nature painting and Gasquet 'become one with my picture' aesthetic fusion are not a professed God-as-nature creed (standing rule; Gasquet contested)."}
    - {code: CLTHEI, reason: "Rejected: no own writing stressing interventionist petition beyond creedal Mass language."}
    - {code: ATHE, reason: "Rejected for adult working years: earlier anti-clerical reports (secondary) contradicted by 1891 practice and 1904 letter."}
  lio_axes:
    A_locus:
      value: 0
      basis: consistent_private_letters
      certainty: 0.5
      support: corroborated
      cites: [{source: S5, locator: "Courtauld MS 15 Apr 1904"}, {source: S6, locator: "Rewald EN + deference reading"}]
      rationale: "Bernard letter: nature as the spectacle that 'Pater Omnipotens Aeterne Deus' spreads before our eyes — personal Almighty Father distinct from the spectacle (transcendent lean, CHRIST A 0 direction). Cap 0.5: single letter; Reff deference/habit reading (S6); Bach parallel (naming God without a full locus essay) keeps alt BELOW."
      alternatives:
        - {value: BELOW_THRESHOLD, note: "Liturgical courtesy to Bernard / naming without locating God relative to the world.", cites: [{source: S6, locator: "deference to Bernard"}]}
      how_known: "Own letter S5; not Gasquet."
    B_cause:
      value: UNKNOWN
      how_known: "Not a scientist (P30). Cylinder/sphere/cone and nature-observation lines are painting method, not a P16 account of nature's causal order. Standing rule: painting/nature subject alone does not score B. Gasquet unused."
    C_ledger: {value: UNKNOWN, how_known: "Alexis 'roasting in aeternum' / afterlife fear is reported speech via Merleau-Ponty and Telegraph (S7; S8) — cannot score an axis alone (statement kind reported speech)."}
    D_authority: {value: UNKNOWN, how_known: "Church attendance reported; no own writing ranking revelation vs reason."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read on exemptions from natural order (P7)."}
  mid_basin: {value: UNKNOWN, how_known: "B_cause is UNKNOWN, which takes precedence (P19); A is 0 at 0.5."}
  statements:
    - text: "Traiter la nature par le cylindre, la sphère, le cone, le tout mis en perspective… Les lignes parallèles à l'horizon donnent l'étendue, soit une section de la nature ou si vous aimez mieux du Spectacle que le Pater omnipotens [oeterne Deus] étale devant nos yeux."
      cites: [{source: S5, locator: "Courtauld MS.1932.SC.1.1, Aix 15 avril 1904 (inscriptions)"}, {source: S6, locator: "Rewald Letters 4th ed. p. 301 EN tr."}]
      context: "Letter to Émile Bernard, 15 April 1904 — painting advice with Mass/Credo phrase naming Almighty Eternal God as spreader of nature's spectacle. In-span relative to Bathers completion 1905."
      axes: [A_locus]
      kind: "private letter"
      verified_against: "primary transcription"
      verified_on: 2026-10-24
      note: "French from Courtauld online transcription; EN via Rewald/Danchev stream. Phrase added above the line in the MS. Reff (S6): may be liturgical habit or deference to Bernard."
    - text: "It is fear… I feel I have only a few days left on earth — and then what? I believe I shall survive and do not want to risk roasting in eternam."
      cites: [{source: S8, locator: "Sacred Mysteries (to Paul Alexis)"}, {source: S7, locator: "Cézanne's Doubt (to a friend)"}]
      context: "Reported explanation of return to Catholic practice (fear of death / hell). Secondary / reported speech only."
      axes: [C_ledger]
      kind: "reported speech"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Cannot score C alone (CODING_GUIDE reported speech). Kept for context of late practice motive."
    - text: "The landscape becomes human, becomes a thinking, living being within me. I become one with my picture.…We merge in an iridescent chaos."
      cites: [{source: S1, locator: "Final years"}]
      context: "Aesthetic fusion line as printed in Britannica (create-pass). Likely Gasquet-stream; contested as creed."
      axes: []
      kind: "other"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "UNUSED for PANT/A/B (Gasquet contested; standing painting≠pantheism). Logged so the lead is closed."
  changes_over_life:
    - {value: "Baptized Catholic 1839; mid-life often anti-clerical in secondary reports; c. 1891 returned to practising Catholicism (sister Marie influence / fear of death in reports); 1904 letter uses Mass language; buried Saint-Pierre, Aix", year: 1891, age: 52, certainty: 0.5, cites: [{source: S4, locator: "1891 turn"}, {source: S8, locator: "return / Marie"}, {source: S5, locator: "1904 letter"}], how_known: "Wikipedia + Telegraph + letter; motive contested."}
  coder_notes: "Deepen D1 2026-10-24: create-pass had no own words. Hunt found Courtauld Bernard letter (own words) and late Catholic practice reports. Gasquet deliberately unused for scores (Doran: imperious editing). Painting/nature ≠ PANT or B. Not a scientist — B UNKNOWN. Chart-moving NO (B UNKNOWN). Lane A separate from Lane B sphere/cone geometry (method). No fallacy_catalog (Jason)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "French Provençal (Aix / family roots Saint-Sauveur Hautes-Alpes)", certainty: 0.5, cites: [{source: S4, locator: "Early years"}], how_known: "Wikipedia."}
  religious_heritage_by_birth: {value: "Roman Catholic (baptized Église de la Madeleine, Aix)", certainty: 0.7, cites: [{source: S4, locator: "Early years"}], how_known: "Wikipedia."}
  baptism_or_initiation: {value: "Baptized 22 February 1839, Église de la Madeleine, Aix-en-Provence", certainty: 0.7, cites: [{source: S4, locator: "Early years"}], how_known: "Wikipedia."}
  childhood_catechism: {value: UNKNOWN, how_known: "Religious instruction at school reported in secondary summaries; no named catechism text read."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1905", certainty: 0.5, cites: [{source: S1, locator: "Final years; Legacy"}], how_known: "The one listed lasting item, dated by completion (posthumous rule); 0.5."}
  age_at_first_lasting_contribution: {value: 66, certainty: 0.5, cites: [{source: S1, locator: "Introduction"}], how_known: "1905 − 1839 = 66 (P30 year difference); alternatives 67 (1906) and 68 (1907)."}
  first_evidence_of_lio_type_views: {value: "1904", certainty: 0.5, cites: [{source: S5, locator: "15 Apr 1904"}], how_known: "Scored A evidence in the Bernard letter; practice turn 1891 is secondary."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.5, cites: [{source: S5, locator: "1904"}, {source: S1, locator: "Bathers 1900–05"}], how_known: "Letter year abuts Bathers completion 1905."}
  worldview_during_major_work: {value: "Late practising Roman Catholic with Mass language in painting letters; God as Pater Omnipotens of nature's spectacle; not a scientist account of nature", certainty: 0.5, cites: [{source: S5, locator: "1904 letter"}, {source: S4, locator: "1891"}, {source: S6, locator: "cathedral"}], how_known: "Letter + secondary practice."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "'Treat nature by the cylinder, the sphere, the cone' (Bernard letter S5; also S1 mature-style paraphrase).", certainty: 0.5, cites: [{source: S5, locator: "15 Apr 1904"}, {source: S1, locator: "Development of his mature style"}], how_known: "Own letter + Britannica."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable as a scored acquisition path for theology."}
  circle_present: {value: "unclear", rationale: "Not assessed as Deus-sive-Natura circle.", certainty: 0.5, cites: [{source: S5, locator: "letter"}], how_known: "Coder's reading."}
  reading: "A 0 @0.5; B UNKNOWN — no mid-basin. Sphere/cone are painting construction, not Lane A B."
  notes: "Gasquet unused. Painting ≠ pantheism."

institutions: []
collaborators:
  - {value: "Camille Pissarro", relation: "teacher", note: "taught him Impressionist technique", certainty: 0.7, cites: [{source: S1, locator: "Impressionist years"}, {source: S4, locator: "Pissarro"}], how_known: "Two sources."}
  - {value: "Émile Zola", relation: "other", note: "school friend; friendship cooled after L'Œuvre", certainty: 0.7, cites: [{source: S1, locator: "Early life and work"}, {source: S4, locator: "Break with Zola"}], how_known: "Two sources."}
  - {value: "Émile Bernard", relation: "correspondent", note: "1904–06 letters including Pater Omnipotens letter", certainty: 0.7, cites: [{source: S5, locator: "MS letter"}, {source: S4, locator: "Last years"}], how_known: "Courtauld + Wikipedia."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 208"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Worldview: single in-span letter for A/primary; practice secondary; Gasquet contested and unused."
    - "Lasting item posthumous; dated 1905 at 0.5."
    - "B UNKNOWN — not a scientist; chart unplottable."
  open_questions:
    - "Full Rewald/Danchev Letters corpus for further creed statements (only Bernard 1904 opened end-to-end)."
    - "Independent primary for Alexis fear quote (presently Merleau-Ponty / Telegraph secondary)."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "René Huyghe"
    citation: "Huyghe, René. 'Paul Cézanne.' Encyclopaedia Britannica (scholars edition). https://kids.britannica.com/scholars/article/Paul-C%C3%A9zanne/22192"
    url: "https://kids.britannica.com/scholars/article/Paul-C%C3%A9zanne/22192"
    accessed: 2026-10-24
    reliability_note: "Signed article, scholars edition, re-read at D1. Aesthetic 'one with my picture' line treated as Gasquet-stream, unused for creed."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, timing, collaborators, worldview]
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
    type: secondary
    kind: "institutional page"
    author: "The National Gallery, London"
    citation: "'Paul Cezanne, Bathers (Les Grandes Baigneuses), about 1894–1905.' National Gallery, London, NG6359. https://www.nationalgallery.org.uk/paintings/paul-cezanne-bathers-les-grandes-baigneuses"
    url: "https://www.nationalgallery.org.uk/paintings/paul-cezanne-bathers-les-grandes-baigneuses"
    accessed: 2026-10-19
    reliability_note: "Holder of the painting; collection page read."
    source_quality: "other"
    used_for: [basics, contribution, timing]
  - id: S4
    type: tertiary
    kind: "encyclopedia"
    author: "Wikipedia contributors"
    citation: "Wikipedia. 'Paul Cézanne' (English). https://en.wikipedia.org/wiki/Paul_C%C3%A9zanne"
    url: "https://en.wikipedia.org/wiki/Paul_C%C3%A9zanne"
    accessed: 2026-10-24
    reliability_note: "Dual-bio check against Britannica (P50). Baptism, 1891 Catholicism turn, death/burial, Deanchev Letters cite. Not used alone for worldview codes."
    source_quality: "reference entry"
    used_for: [identity, basics, childhood, heritage, collaborators, worldview]
  - id: S5
    type: primary
    kind: "letter"
    author: "Paul Cézanne"
    citation: "Cézanne, Paul. Letter to Émile Bernard, Aix-en-Provence, 15 April 1904. Courtauld Gallery, MS.1932.SC.1.1 (online transcription). Also Danchev, The Letters of Paul Cézanne, no. 233, pp. 334–336; Rewald Letters 4th ed. p. 301."
    url: "https://gallerycollections.courtauld.ac.uk/object-ms-1932-sc-1-1"
    accessed: 2026-10-24
    reliability_note: "Autograph letter; French inscription transcribed on Courtauld page; Pater Omnipotens phrase added above the line. Decisive own-words source for A/primary."
    source_quality: "primary / own words"
    used_for: [worldview, collaborators, timing]
  - id: S6
    type: secondary
    kind: "journal article"
    author: "Theodore Reff"
    citation: "Reff, Theodore. 'Cézanne on Solids and Spaces.' Artforum 16.2 (October 1977). https://www.artforum.com/features/cezanne-on-solids-and-spaces-209329/"
    url: "https://www.artforum.com/features/cezanne-on-solids-and-spaces-209329/"
    accessed: 2026-10-24
    reliability_note: "Scholarly art-historical essay; prints Rewald EN of the Bernard letter; notes cathedral worship and possible deference to Bernard."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview]
  - id: S7
    type: secondary
    kind: "other"
    author: "Maurice Merleau-Ponty"
    citation: "Merleau-Ponty, Maurice. 'Cézanne's Doubt' (1945). English in Sense and Non-Sense / standard reprints (e.g. faculty.uml.edu/rinnis/cezannedoubt.pdf)."
    url: "https://faculty.uml.edu/rinnis/cezannedoubt.pdf"
    accessed: 2026-10-24
    reliability_note: "Philosopher's essay; quotes reported fear-of-hell speech. Reported speech — context only, not sole axis warrant."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview]
  - id: S8
    type: secondary
    kind: "other"
    author: "Christopher Howse"
    citation: "Howse, Christopher. 'Sacred Mysteries: Cézanne's empathy with an old woman.' The Telegraph, 7 Jan 2018. https://www.telegraph.co.uk/opinion/2018/01/07/sacred-mysteriescezannes-empathy-old-woman/"
    url: "https://www.telegraph.co.uk/opinion/2018/01/07/sacred-mysteriescezannes-empathy-old-woman/"
    accessed: 2026-10-24
    reliability_note: "Newspaper column summarizing Rewald and Alexis line on return to practice / fear motive; Gasquet old-woman story flagged as unreliable in same piece."
    source_quality: "other"
    used_for: [worldview]
---

## Summary

Paul Cézanne (1839–1906), French Post-Impressionist painter [S1; S4]. Deepen D1: primary_system CHRIST @0.5 (Roman Catholic); A 0 @0.5; B UNKNOWN; mid_basin UNKNOWN. Not plotted. Chart-moving NO.

## Life and work

Aix-en-Provence; Paris; Bathers / Mont Sainte-Victoire / Card Players [S1; S4].

## Contribution and impact

Bathers finished 1905 (NG6359); foundation for Cubism; Picasso 'father of us all' [S1; S3].

## Childhood and education

Baptized Madeleine, Aix, 1839; Collège Bourbon; law then Académie Suisse [S1; S4].

## Adult working worldview

c. 1891 return to Catholic practice (secondary) [S4; S8]. Own letter to Bernard 15 Apr 1904: nature as spectacle Pater Omnipotens Aeterne Deus spreads [S5]. Gasquet contested — unused for PANT [S1 aesthetic line logged closed]. primary CHRIST @0.5; A 0 @0.5; B UNKNOWN.

## Heritage (context only)

Roman Catholic baptism; French Provençal [S4].

## Timing

1905 (0.5), age 66; worldview letter 1904 during major-work edge [S1; S5].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Cylinder / sphere / cone = painting method [S5], not scientist B.

## Open questions

- Broader Danchev/Rewald letter corpus.
- Primary source for Alexis fear quote.

## Research log

- 2026-10-19: Read Britannica (Huyghe).
- 2026-10-24 (D1): Wikipedia dual; Courtauld Bernard letter; Reff Artforum; Merleau-Ponty Doubt; Telegraph Sacred Mysteries. Gasquet unused. primary CHRIST @0.5; A 0 @0.5; B UNKNOWN. Chart-moving NO. No fallacy_catalog; no figures/.
