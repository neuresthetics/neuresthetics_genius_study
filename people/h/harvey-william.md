---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 4
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AB1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to medicine. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-25, by: "Grok Bot", summary: "Perpetual deepen: A_locus support single→corroborated (P48) via D'Arcy Power 1897 (S7) quoting Generation essay 54 Creator-and-Father / Almighty first-cause diction agreeing with Willis S3. B already corroborated. Certainty stays 0.5 (named alt 0). Chart cue: faded hollow→faded filled. No fallacy_catalog; no figures/."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen D1 (queue #212/228, F 3, rank 225). Goals: firm B with corroboration; seek any A from De Motu / letters / will; P35 if applicable; do not force plot. Opened Willis 1847 Works via Gutenberg (S3: De Motu fabric-of-nature + De Generatione first-agent / Omnipotent Creator); will text (S4) — P42 formulaic preamble → nominal_affiliations only; Galileo Project Westfall (S5) Anglican; Wikipedia dual-bio (S6). primary_system UNKNOWN → CLASS_THEISM @ 0.5 written_profession (alt CHRIST). A_locus UNKNOWN → 1 @ 0.5 written_profession, support single (alt 0). B_cause stays 3 @ 0.5 inference_from_work (P35); support single → corroborated (S1+S3); alt 4. E UNKNOWN → BELOW_THRESHOLD (P19). mid_basin UNKNOWN → BELOW_THRESHOLD (shape would pass; both axes only 0.5). Will Christ/Maker line not scored (P42). Chart-moving YES: not plotted → faded hollow at next figure refresh (A now scored; B faded; A single → hollow). No fallacy_catalog; figures/ untouched. Draft, not reviewed."}
    - {date: 2026-10-20, by: "Grok Bot", summary: "AB1 audit note: 'later Renaissance' framing (S1) added as a lead (no score change)."}
    - {date: 2026-10-20, by: "Grok Bot", summary: "Record created (stage 3 batch AB1, order P32: F 3, rank 225). Source: Britannica scholars edition, signed by Andrew Gregory (read in full). Lasting: the circulation of the blood, De Motu Cordis (1628); he 'was the first to recognize the full circulation of the blood in the human body'; the theory 'was well established by the time of his death' (S1). Discovery probably 1618–19 but published 1628 (P30 publication). The generation work (1651) has no lasting wording. Span 1628, age 50. Scientist: B 3 at 0.5, alt 4 (P35); S1 notes his vitalism (blood with 'an irreducible life force of its own') and opposition to mechanism, which does not bear on law and exception. Worldview: no own words on God (the 'household-god' line is a metaphor for the heart); UNKNOWN. Not plotted. Draft, not reviewed."}

identity:
  id: harvey-william
  display_name: "William Harvey"
  roster:
    canonical_name: "William Harvey"
    rank: 225
    F: 3
    models: [Claude, DeepSeek, Gemini]
    band: "core (3–4)"
    status: "core"
    field: "medicine"
    field_bucket: "medicine"
  full_name: {value: "William Harvey", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S6, locator: "lead"}], how_known: "Britannica + Wikipedia dual-bio (P50)."}
  native_name: {value: "William Harvey", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  aliases: []

basics:
  birth:
    date: {value: "1578-04-01", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S5, locator: "§1 Dates"}], how_known: "Britannica; Galileo Project."}
    place: {value: "Folkestone, Kent", modern_name: "Folkestone, Kent, United Kingdom", polity_then: "Kingdom of England", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  death:
    date: {value: "1657-06-03", certainty: 0.7, cites: [{source: S1, locator: "Introduction; Later life"}, {source: S5, locator: "§1 Dates"}], how_known: "Britannica; Galileo Project."}
    place: {value: "London", modern_name: "London, United Kingdom", polity_then: "Commonwealth of England", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica. Galileo Project: London or Roehampton, Surrey."}
  first_lasting_contribution_year: {value: 1628, certainty: 0.7, cites: [{source: S1, locator: "Discovery of circulation"}], how_known: "De Motu Cordis 'published in 1628' (S1); P30 publication. The discovery itself was likely 'about 1618–19' (S1), not public."}
  era_bucket: {value: "1600 to 1749", certainty: 1.0, cites: [{source: S1, locator: "Discovery of circulation"}], how_known: "1628 (P2)."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "England (P3: UK is Northern Europe)."}
  region_of_work: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "Education; Physician to the king"}], how_known: "London."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Latin"], certainty: 0.7, cites: [{source: S1, locator: "Discovery of circulation"}], how_known: "Latin works; English version 1653."}
  occupations: {value: ["physician", "anatomist"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}

contribution:
  primary_domain: medicine
  fields: {value: ["medicine", "physiology"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Circulation of the blood, with the heart as pump (De Motu Cordis)", year: 1628, kind: "discovery", lasting: "'the first to recognize the full circulation of the blood in the human body'; the theory 'was well established by the time of his death' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Introduction; Discovery of circulation"}, {source: S3, locator: "De Motu Cordis, Willis pp. 3–86"}], how_known: "De Motu Cordis, 1628 (S1; S3)."}
  evidence_of_impact: []
  major_works:
    - {value: "Exercitationes de Generatione Animalium", year: 1651, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "Later life; Studies of reproduction"}, {source: S3, locator: "On Animal Generation, Willis"}], how_known: "Britannica; Willis Works. Not a lasting contribution under the roster wording (create-pass)."}
    - {value: "De Circulatione Sanguinis (reply to Riolan)", year: 1649, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "Discovery of circulation"}], how_known: "Britannica."}
  honours:
    - {value: "Lumleian lecturer in surgery, Royal College of Physicians", year: 1615, certainty: 0.7, cites: [{source: S1, locator: "Education and appointment as Lumleian lecturer"}], how_known: "Britannica."}
  definition_fit: {value: "clearly meets", rationale: "Discovered the circulation (S1).", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated beyond English Protestant setting (King's School Canterbury; Cambridge). Westfall: Anglican affiliation as adult (S5)."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated (P19)."}
  parents_and_household:
    - {value: "Father Thomas Harvey, farmer and landowner; seven brothers and two sisters", role: "family", certainty: 0.7, cites: [{source: S1, locator: "Education"}], how_known: "Britannica."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling:
    - {value: "King's School, Canterbury (1588–93); Gonville and Caius College, Cambridge (1593–99); University of Padua (doctorate 25 April 1602, under Fabricius)", certainty: 0.7, cites: [{source: S1, locator: "Education"}, {source: S5, locator: "§4 Education"}], how_known: "Britannica; Galileo Project."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated (P19)."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated (P19)."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated (P19)."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1628", certainty: 0.7, cites: [{source: S1, locator: "Discovery of circulation"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Church of England (Anglican)", certainty: 0.5, cites: [{source: S5, locator: "§5 Religion"}, {source: S4, locator: "will preamble"}], how_known: "Westfall: 'Affiliation: Anglican' — conformed to the established church (S5). Will formula 'In the name of the Almighty and Eternal God' / soul to Maker and Saviour Christ Jesus is P42 context only (lawyer set form), logged here not as A or primary_system evidence."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No statement pairing science with religion as such. De Generatione first-agent discussion is metaphysics of generation, not a science–religion relation claim (S3)."}
  primary_system:
    value: CLASS_THEISM
    basis: written_profession
    certainty: 0.5
    cites: [{source: S3, locator: "On Animal Generation, Willis pp. 370, 343, ~generation exercises (Omnipotent Creator / first agent)"}, {source: S5, locator: "§5 Religion"}]
    how_known: "Own published De Generatione (1651; P31: adult evidence counts for 1628 span — no documented change of view): 'he takes the right and pious view ... who derives all generation from the same eternal and omnipotent Deity'; first agent may be called 'God, Nature, or the Soul of the universe' but is 'beginning and the end of all things', 'author or creator', 'omnipresent' (S3, Willis p. 370). Naming flexibility + philosophical Creator/preserver without Christ/revelation discussion → CLASS_THEISM rather than CHRIST. Capped at 0.5: (a) named alt CHRIST; (b) Westfall notes no evidence of serious religious commitment and gossip of free thought (S5); (c) Generation is not a lasting contribution."
    rationale: "Philosophical Creator theism in his own Generation treatise: eternal omnipotent Deity as author/creator and preserver, omnipresent in natural operations; name God/Nature/Soul of universe interchangeable for that first agent (S3). Not CHRIST as primary: no working Christology, scripture, or revealed-religion profession in the sources read (will Christ-line is P42 formula). Not ARIST alone: he adds Creator and Father language 'as is seeming in these days' (S3)."
    note: "Will preamble not used for this code (P42)."
  secondary_system: {value: UNKNOWN, how_known: "No second system (P29)."}
  candidate_codes_considered:
    - {code: CLASS_THEISM, reason: "Coded at 0.5: De Generatione first-agent / Omnipotent Creator metaphysics (S3)."}
    - {code: CHRIST, reason: "Named alternative: Anglican conformity (S5); will names Christ Jesus as Saviour (S4) but that is P42 formulaic; Generation's 'Creator and Father' is Christian diction without a Christ-centered working metaphysics."}
    - {code: CLTHEI, reason: "Rejected as primary: some scholars read Generation as direct divine intervention in epigenesis, but that is a generation-mechanism debate, not a scored popular-interventionist creed; A stays at classical-theist 1."}
    - {code: ARIST, reason: "Rejected as primary: Aristotelian natural philosophy is the scientific frame (S1), not the worldview code; Generation's Creator language goes beyond unmoved-mover ARIST."}
    - {code: DEISM, reason: "Rejected: he does not reject revelation; Generation affirms an omnipresent creating/preserving Deity active in generation (S3)."}
  lio_axes:
    A_locus:
      value: 1
      basis: written_profession
      certainty: 0.5
      support: corroborated
      cites: [{source: S3, locator: "On Animal Generation, Willis p. 370 (first agent); p. 343 (adore Omnipotent Creator); generation exercises ('We acknowledge God, the supreme and omnipotent creator')"}, {source: S7, locator: "ch. III / treatise-on-development discussion: quotes Generation essay 54 Creator and Father / Almighty first-cause; omnipotent Creator reflex line"}]
      how_known: "Own De Generatione (Willis 1847 English of the 1651 Latin; S3). Perpetual deepen 2026-10-25: D'Arcy Power 1897 Masters of Medicine biography (S7, Gutenberg) independently quotes the same Generation Creator-and-Father / Almighty first-cause diction and the 'image or reflex of the omnipotent Creator' line — scholarly secondary agreeing with primary → corroborated (P48). Certainty stays 0.5: named alt 0; naming flexibility (God/Nature/Soul of universe); Westfall free-thought gossip (S5); Generation post-dates the 1628 lasting span (allowed under P31 with no documented change)."
      rationale: "Transcendent Creator distinct from the world, also omnipresent as sustaining/generating cause — classical-theist lean (A 1), not the bare interventionist pole. 'Eternal and omnipotent Deity, on whose nod the universe itself depends'; 'author or creator'; 'omnipresent, not less in the single and several operations of natural things, than in the infinite universe'; 'We acknowledge God, the supreme and omnipotent creator, to be present in the production of all animals' (S3; Power S7). Named alternative: 0, if 'Creator and Father' / personal Saviour diction is read as full personal interventionist theism (CHRIST/CLTHEI pole). Household-god / sun-of-microcosm lines in De Motu are metaphors for the heart, not locus evidence (create-pass)."
      alternatives:
        - {value: 0, note: "Personal transcendent Creator at the interventionist pole, if Father/Saviour diction outweighs the God/Nature/Soul naming flexibility. Will Saviour diction (S4) is P42 context only — not cited here for score support.", cites: [{source: S3, locator: "Willis p. 370; Creator and Father passage"}, {source: S7, locator: "Creator and Father / Almighty first-cause quote"}]}
    B_cause:
      value: 3
      basis: inference_from_work
      certainty: 0.5
      support: corroborated
      cites: [{source: S1, locator: "Discovery of circulation"}, {source: S3, locator: "De Motu Cordis, Willis p. 7 (fabric of nature); circulation demonstration chapters"}]
      how_known: "Scientist (P30). B from lasting working science (circulation) with no own no-exception claim in De Motu, so 3 at 0.5, alternative 4, never 4 (P35). Two independent source ids (Britannica + Willis De Motu) → corroborated (P48)."
      rationale: "Scored on his account of nature in the lasting contribution (P6, P35). De Motu argues circulation by ocular demonstration, vivisection, and quantitative blood-volume estimates under uniform physiology; he professes 'to learn and to teach anatomy, not from books but from dissections; not from the positions of philosophers but from the fabric of nature' (S3, Willis ~p. 7; S1). Vitalism / anti-mechanism (S1) concerns the kind of cause, not law vs exception. Generation's divine first-agent language (S3) is not used to lift B off P35: it is not the lasting work, and if read as ongoing special divine action in epigenesis would pull toward alt 2, not toward 4. Named alternative: 4, if an own no-exception claim appears."
      alternatives:
        - {value: 4, note: "P35: if an own statement shows exceptionless natural order beyond working-science fabric-of-nature language.", cites: [{source: S3, locator: "De Motu, Willis p. 7"}]}
        - {value: 2, note: "If De Generatione's God-as-present-efficient in every generation is read as frequent special divine action inside nature (scholarly interventionist reading).", cites: [{source: S3, locator: "Willis p. 370; acknowledge God present in production of all animals"}]}
    C_ledger: {value: UNKNOWN, how_known: "Nothing on judgement, afterlife reward, or moral ledger in the sources read (P19). Will's soul-to-Maker line is P42 formula, not scored."}
    D_authority: {value: UNKNOWN, how_known: "No statement on revelation vs observation in the sources read (P19)."}
    E_scope: {value: BELOW_THRESHOLD, how_known: "Working science bears on same-laws-everywhere but not on favour for a group in events; not scored from working science alone (P19)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus 1 ≤ 1 and B_cause 3 ≥ 3 would satisfy P4's shape test, but both are only at 0.5, under the test's 0.7 bar (§6, P19)."}
  statements:
    - text: "Wherefore, according to my opinion, he takes the right and pious view of the matter, who derives all generation from the same eternal and omnipotent Deity, on whose nod the universe itself depends. Nor do I think that we are greatly to dispute about the name by which this first agent is to be called or worshipped; whether it be God, Nature, or the Soul of the universe,—whatever the name employed,—all still intend by it that which is the beginning and the end of all things; which exists from eternity and is almighty; which is author or creator, and, by means of changing generations, the preserver and perpetuator of the fleeting things of mortal life; which is omnipresent, not less in the single and several operations of natural things, than in the infinite universe."
      cites: [{source: S3, locator: "On Animal Generation, Willis p. 370 (Gutenberg Works of William Harvey)"}]
      date: "1651"
      context: "Exercitationes de Generatione Animalium; after the 1628 lasting span; no documented change of view (P31)."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "TODO: map Gutenberg page 370 to a printed Willis 1847 Sydenham Society page check (P30 Gutenberg rule)."
    - text: "Lastly, when we were discussing the efficient causes of the fœtus, we were not inattentive to its admirable structure, to the functions and uses of all its parts and members; neither did we overlook the foresight, the art, the intelligence, the divine inspiration with which all things were ordained and skilfully continued for the ends of life. It is not enough that we inquire what is the 'efficient,' the architect, the adviser, but that we likewise venerate and adore the omnipotent Creator and preserver of a work, which has been well entitled a microcosm."
      cites: [{source: S3, locator: "On Animal Generation, Willis p. 343"}]
      date: "1651"
      context: "De Generatione; adore Omnipotent Creator."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "TODO: map Gutenberg page 343 to printed Willis 1847 (P30)."
    - text: "I profess both to learn and to teach anatomy, not from books but from dissections; not from the positions of philosophers but from the fabric of nature."
      cites: [{source: S3, locator: "De Motu Cordis, dedication to colleagues, Willis ~p. 7"}]
      date: "1628"
      context: "De Motu Cordis epistle; during the lasting-contribution year."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Working-science method claim; does not lift B off P35 (no no-exception / miracle claim). TODO: map Gutenberg ~p. 7 to printed Willis (P30)."
  changes_over_life: []
  coder_notes: "D1 coder's calls: (1) Will Christ/Maker preamble → nominal_affiliations only (P42), not A/primary. (2) CLASS_THEISM over CHRIST as primary from Generation naming flexibility. (3) B stays P35-capped; Generation interventionist reading logged as B alt 2 only. (4) Chart-moving YES to faded hollow — figures/ not refreshed. Letters unread; Prelectiones Jove/Augustine lines unread this pass (Boyle PMC notes them)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Not stated."}
  religious_heritage_by_birth: {value: "Christian (Church of England setting)", certainty: 0.5, cites: [{source: S5, locator: "§5 Religion"}, {source: S1, locator: "Education"}], how_known: "English Protestant schooling (King's School Canterbury; Cambridge); Westfall Anglican affiliation. Not a worldview code."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated in sources read; Boyle PMC asserts baptism as ecclesiastical milestone without a primary locator used here (P19)."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated (P19)."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1628", certainty: 0.7, cites: [{source: S1, locator: "Discovery of circulation"}], how_known: "The one lasting item (P29, P30)."}
  age_at_first_lasting_contribution: {value: 50, certainty: 0.7, cites: [{source: S1, locator: "Introduction; Discovery of circulation"}], how_known: "1628 − 1578 = 50 (P30 year difference)."}
  first_evidence_of_lio_type_views: {value: "1651", certainty: 0.5, cites: [{source: S3, locator: "On Animal Generation, Willis p. 370"}], how_known: "First scored LIO-type view (A 1 from Generation first-agent profession). De Motu fabric-of-nature is working science, not an LIO-type view (P27)."}
  lio_views_relative_to_major_work: {value: "after major work", rationale: "Generation Creator profession is 1651; lasting circulation work is 1628. No documented change, so axes still use Generation under P31; relative timing is after.", certainty: 0.7, cites: [{source: S3, locator: "Willis p. 370"}, {source: S1, locator: "Discovery of circulation"}], how_known: "Publication years."}
  worldview_during_major_work: {value: "CLASS_THEISM (0.5); A 1 / B 3 both @ 0.5", certainty: 0.5, cites: [{source: S3, locator: "Willis pp. 7, 370"}, {source: S1, locator: "Discovery of circulation"}], how_known: "P31 continuity: Generation evidence counted for the 1628 span; B from De Motu working science."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Physiology / experimental anatomy (S1; S3).", certainty: 0.5, cites: [{source: S1, locator: "text"}, {source: S3, locator: "De Motu"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Macrocosm/microcosm heart–sun analogy (S1) is analogy, not assessed as geometric circle training.", certainty: 0.5, cites: [{source: S1, locator: "Renaissance influences"}], how_known: "Coder's reading."}
  reading: "Belief model only. Circulation as lawful fabric-of-nature science; Generation first-agent theism is Lane A."
  notes: "H1 not tested."

institutions:
  - {value: "Royal College of Physicians of London", role: "fellow; Lumleian lecturer", years: "1607–1657", kind: "academy or learned society", certainty: 0.7, cites: [{source: S1, locator: "Education"}], how_known: "Britannica."}
  - {value: "St Bartholomew's Hospital", role: "physician", years: "1609–1643", kind: "employer", certainty: 0.7, cites: [{source: S1, locator: "Education"}], how_known: "Britannica."}
collaborators:
  - {value: "Hieronymus Fabricius", relation: "teacher", note: "Padua", certainty: 0.7, cites: [{source: S1, locator: "Education"}], how_known: "Britannica."}
  - {value: "Thomas Hobbes", relation: "other", note: "friend", certainty: 0.7, cites: [{source: S1, locator: "Physician to the king"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 225"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Deepen D1: A single-source @ 0.5; B corroborated but P35-capped @ 0.5; will unused for scores (P42)."
  open_questions:
    - "Prelectiones anatomie universalis (Jove antiphon; Augustine resurrection line) unread in full."
    - "Latin 1651 De Generatione page-check of Willis English; McMullen Use of Purpose (1998) unread."
    - "Aubrey Brief Lives gossip of free thought — primary page unread beyond Westfall summary (S5)."
    - "If a second independent source corroborates the Generation Creator locus, A support can become corroborated (fill cue)."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Andrew Gregory"
    citation: "Gregory, Andrew. 'William Harvey.' Encyclopaedia Britannica (scholars edition). https://kids.britannica.com/scholars/article/William-Harvey/106277"
    url: "https://kids.britannica.com/scholars/article/William-Harvey/106277"
    accessed: 2026-10-19
    source_quality: "reference entry"
    reliability_note: "Signed article, scholars edition, read in full."
    used_for: [identity, basics, contribution, childhood, worldview, timing, institutions, collaborators, lane_b]
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
    author: "William Harvey; English translation by Robert Willis"
    year: 1847
    citation: "Harvey, William. The Works of William Harvey, M.D. Translated from the Latin by Robert Willis. London: Sydenham Society, 1847. Project Gutenberg ebook #58857 (accessed 2026-10-24). Contains De Motu Cordis (1628) and Exercitationes de Generatione Animalium (1651)."
    url: "https://www.gutenberg.org/files/58857/58857-h/58857-h.htm"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "Scholarly 1847 English of Harvey's Latin; Gutenberg HTML used this pass. Page numbers are Willis/Gutenberg page markers. Each statement citing Gutenberg pages carries a TODO to map to a printed Willis check (P30)."
    used_for: [contribution, worldview, timing, lane_b]
  - id: S4
    type: primary
    kind: "other"
    author: "William Harvey"
    year: 1657
    citation: "Harvey, William. Last Will and Testament (proved Prerogative Court of Canterbury, 2 May 1659). Text via Starvard Books appendix (from the registry extract also printed in Willis Works)."
    url: "https://starvard.org/books/on-the-motion-of-the-heart-and-blood-in-animals/chapter-33/"
    accessed: 2026-10-24
    source_quality: "primary / own words"
    reliability_note: "Will text. Religious preamble is P42 formulaic set form — used only for nominal_affiliations / heritage context, never for A or primary_system scores."
    used_for: [worldview, heritage]
  - id: S5
    type: secondary
    kind: "encyclopedia"
    author: "Richard S. Westfall (Galileo Project)"
    citation: "Westfall, Richard S. 'Harvey, William.' The Galileo Project catalogue of the scientific community. https://galileo.library.rice.edu/Catalog/NewFiles/harvey.html"
    url: "https://galileo.library.rice.edu/Catalog/NewFiles/harvey.html"
    accessed: 2026-10-24
    source_quality: "reference entry"
    reliability_note: "Scholarly catalogue entry. Religion §5: Anglican conformity; no evidence of serious religious commitment; gossip of free thought."
    used_for: [basics, childhood, worldview, heritage]
  - id: S6
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia. 'William Harvey.' English Wikipedia. Dual-biography use only (P50)."
    url: "https://en.wikipedia.org/wiki/William_Harvey"
    accessed: 2026-10-24
    source_quality: "other"
    reliability_note: "P50 dual-bio only; not used for worldview scores."
    used_for: [identity]
  - id: S7
    type: secondary
    kind: scholarly book
    author: "D'Arcy Power"
    citation: "Power, D'Arcy. William Harvey (Masters of Medicine). London: T. Fisher Unwin, 1897. Project Gutenberg eBook #46664."
    url: "https://www.gutenberg.org/files/46664/46664-h/46664-h.htm"
    accessed: 2026-10-25
    source_quality: "scholarly edition or monograph"
    reliability_note: "Standard late-Victorian medical biography; quotes Generation Creator diction at length. Used to corroborate A (P48), not to set values."
    used_for: [worldview]

---

## Summary

William Harvey (1578–1657), English physician [S1]. Deepen D1 + perpetual 2026-10-25: primary_system CLASS_THEISM @ 0.5; A 1 @ 0.5 corroborated (S3+S7); B 3 @ 0.5 corroborated (P35); mid_basin BELOW_THRESHOLD. Chart cue at next refresh: faded filled. Will unused for scores (P42).

## Life and work

Folkestone; Cambridge; Padua; London; physician to James I and Charles I [S1; S5].

## Contribution and impact

Circulation of the blood, De Motu Cordis, 1628 [S1; S3]. Generation treatise 1651 is major but not lasting under roster wording [S1].

## Childhood and education

King's School Canterbury; Gonville and Caius, Cambridge; Padua under Fabricius [S1; S5].

## Adult working worldview

De Generatione first-agent profession: eternal omnipotent Deity as creator/preserver, nameable as God, Nature, or Soul of the universe [S3]. CLASS_THEISM @ 0.5; A 1 @ 0.5. Anglican conformity is nominal [S5]. Circulation working science keeps B at 3 @ 0.5 under P35, now corroborated [S1; S3].

## Heritage (context only)

English Church of England setting; baptism not sourced here [S5].

## Timing

Lasting span 1628, age 50 [S1]. First LIO-type view 1651 (Generation); relative to major work: after [S3].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Physiology; H1 not tested.

## Open questions

- Prelectiones; Latin page-check of Willis; McMullen 1998; Aubrey free-thought gossip beyond Westfall.

## Research log

- 2026-10-24: Deepen D1. Willis Works / Gutenberg (S3); will (S4, P42); Galileo Project (S5); Wikipedia dual-bio (S6). A scored; B corroborated; CLASS_THEISM @ 0.5.
- 2026-10-20: AB1 audit note: 'later Renaissance' framing (S1) added as a lead (no score change).
- 2026-10-20: Read Britannica (Gregory, scholars edition).
