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
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to mathematics. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-23, by: "Grok Bot", summary: "Deepen pass D1 (queue #8). P47 source_quality on every source. Added Heath Works of Archimedes (1897; S3 scholarly edition) and Method supplement (1912; S4): own postulates/propositions for statics and hydrostatics (Equilibrium I Posts. 1–7 and Props. 6–7; Floating Bodies I Post. 1 and Prop. 2). B_cause stays 3 @ 0.5 (P16 Hilbert / P35: lawful physical regularities, no no-exception claim) but basis inference_from_work → written_profession; support single → corroborated (S3+S1). A_locus stays UNKNOWN after Heath treatises/prefaces, Method, Sand-Reckoner, MacTutor, and DSB (S5 Clagett via Complete Dictionary of Scientific Biography): no god/divine statement of his. Basics dual-sourced MacTutor+DSB (full_name, birth/death dates and places → 1.0). Chart: still unplotted (A UNKNOWN; B faded @ 0.5). No fallacy_catalog (Jason 2026-10-23). Draft, not reviewed."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch D, order P32: F 5, rank 8). Basics and works from MacTutor (O'Connor and Robertson). No statement by Archimedes on gods, religion or the order of nature was found; the surviving works are mathematical and mechanical treatises. primary_system UNKNOWN; B_cause 3 at 0.5 from working science (P24, P35; alternative 4); A, C, D UNKNOWN; E BELOW_THRESHOLD (P19); mid_basin UNKNOWN. Draft, not reviewed."}

identity:
  id: archimedes
  display_name: "Archimedes"
  roster:
    canonical_name: "Archimedes"
    rank: 8
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: mathematics
    field_bucket: mathematics
  full_name: {value: "Archimedes of Syracuse", certainty: 1.0, cites: [{source: S1, locator: "Biography, paragraph 1 ('a native of Syracuse')"}, {source: S5, locator: "heading ('b. Syracuse…')"}], how_known: "Two sources (P15)."}
  native_name: {value: "Ἀρχιμήδης", certainty: 0.7, cites: [{source: S3, locator: "title page / Greek lemmas in notes"}], how_known: "Greek form in Heath's edition; single scholarly edition, so 0.7."}
  aliases: []

basics:
  birth:
    date: {value: "-287", approx: true, certainty: 1.0, cites: [{source: S1, locator: "Quick Info ('Born 287 BC')"}, {source: S5, locator: "heading ('b. Syracuse, ca. 287 b.c.'); Tzetzes 75-year remark"}], how_known: "Two sources; traditional estimate from Tzetzes (age 75 at death in 212), so approx."}
    place: {value: "Syracuse, Sicily", modern_name: "Syracuse, Italy", polity_then: "Syracuse (Greek city-state)", certainty: 1.0, cites: [{source: S1, locator: "Quick Info; Biography paragraph 1"}, {source: S5, locator: "heading"}], how_known: "Two sources."}
  death:
    date: {value: "-212", certainty: 1.0, cites: [{source: S1, locator: "Quick Info; final paragraphs (killed in 212 BC during the capture of Syracuse)"}, {source: S5, locator: "heading ('d. Syracuse, 212 b.c.')"}], how_known: "Two sources. Ancient accounts differ on how he was killed, not when."}
    place: {value: "Syracuse, Sicily", modern_name: "Syracuse, Italy", polity_then: "Syracuse (under Roman siege)", certainty: 1.0, cites: [{source: S1, locator: "Quick Info"}, {source: S5, locator: "heading; death during Roman capture"}], how_known: "Two sources."}
  first_lasting_contribution_year: {value: UNKNOWN, how_known: "No work of his is dated in the sources read; MacTutor says 'The order in which Archimedes wrote his works is not known for certain' (S1). Every candidate year lies between his adulthood and his death in 212 BC (P30 death cap)."}
  era_bucket: {value: "-500 to 499", certainty: 1.0, cites: [{source: S1, locator: "Quick Info (287–212 BC)"}, {source: S5, locator: "heading (ca. 287–212 b.c.)"}], how_known: "Every candidate year (his adult life, c. 270–212 BC) falls in '-500 to 499', so the bucket holds although the year is unknown (P2, §3 derived-field rule); two sources."}
  region_of_birth: {value: "Southern Europe", certainty: 1.0, cites: [{source: S1, locator: "Quick Info"}, {source: S5, locator: "heading"}], how_known: "Italy is Southern Europe in data/reference/regions.csv (P3); two sources."}
  region_of_work: {value: "Southern Europe", certainty: 0.5, cites: [{source: S1, locator: "Biography, paragraphs 1–2"}], how_known: "He worked in Syracuse; a stay in Alexandria is 'highly likely' but conjecture (S1), so 0.5."}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S1, locator: "Biography ('his father')"}, {source: S5, locator: "throughout"}], how_known: "As the sources record it."}
  languages_of_work: {value: [Greek], certainty: 1.0, cites: [{source: S1, locator: "last paragraph (Dorian dialect)"}, {source: S3, locator: "Greek text lemmas; Dorian dialect notes"}], how_known: "Heath preserves Dorian dialect; MacTutor notes the same."}
  occupations: {value: ["mathematician", "engineer"], certainty: 1.0, cites: [{source: S1, locator: "Summary"}, {source: S5, locator: "heading fields ('mathematics, mechanics')"}], how_known: "Two sources."}

contribution:
  primary_domain: mathematics
  fields: {value: ["geometry", "mechanics", "hydrostatics"], certainty: 1.0, cites: [{source: S1, locator: "Biography (works)"}, {source: S3, locator: "treatise titles; On Floating Bodies; On the Equilibrium of Planes"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "Method of exhaustion applied to areas, volumes and surfaces (sphere and cylinder: volume and surface two-thirds of the circumscribed cylinder; quadrature of the parabola)", year: "undated (before 212 BC)", kind: "law or principle", lasting: "Chasles: it 'gave birth to the calculus of the infinite'", certainty: 1.0, cites: [{source: S1, locator: "Biography (On the sphere and cylinder; Quadrature of the parabola; Chasles quotation)"}, {source: S3, locator: "On the Sphere and Cylinder; Quadrature of the Parabola"}], how_known: "Heath edition of the treatises plus MacTutor; works undated."}
    - {value: "Archimedes' principle and the basic principles of hydrostatics (On floating bodies)", year: "undated (before 212 BC)", kind: "law or principle", lasting: "standard law of hydrostatics", certainty: 1.0, cites: [{source: S1, locator: "Biography (On floating bodies)"}, {source: S3, locator: "On Floating Bodies I, Postulate 1; Props. 3–7"}], how_known: "Heath primary text plus MacTutor."}
    - {value: "Fundamental theorems on centres of gravity and the principles of mechanics (On plane equilibriums)", year: "undated (before 212 BC)", kind: "law or principle", lasting: "basis of statics", certainty: 1.0, cites: [{source: S1, locator: "Biography (On plane equilibriums)"}, {source: S3, locator: "On the Equilibrium of Planes I, Postulates 1–7; Props. 6–7"}], how_known: "Heath primary text plus MacTutor."}
  evidence_of_impact:
    - {value: "Archimedes' principle", kind: "named after them", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}
  major_works:
    - {value: "On the sphere and cylinder", year: "undated", kind: book, certainty: 0.7, cites: [{source: S1, locator: "list of surviving works"}], how_known: "MacTutor."}
    - {value: "The Sandreckoner", year: "undated", kind: book, certainty: 0.7, cites: [{source: S1, locator: "list of surviving works"}], how_known: "MacTutor; dedicated to Gelon, son of Hieron II."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Exhaustion-method results and hydrostatics still taught and built on.", certainty: 0.7, cites: [{source: S1, locator: "Biography"}], how_known: "MacTutor."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "MacTutor says nothing on it."}
  family_religious_practice: {value: UNKNOWN, how_known: "Same."}
  parents_and_household:
    - {value: "Father Phidias, an astronomer", name: "Phidias", role: father, certainty: 1.0, cites: [{source: S3, locator: "The Sand-Reckoner ('Pheidias my father')"}, {source: S5, locator: "opening ('That his father was the astronomer Phidias… Sandreckoner (Sect. I.9)')"}], how_known: "His own statement in The Sand-Reckoner (Heath); DSB concurs."}
  household_circumstances: {value: TODO}
  schooling: []
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: TODO}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: UNKNOWN, how_known: "No work is dated (S1); equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing of his on religion in Heath's treatises/prefaces (S3; S4), MacTutor, or DSB."}
  primary_system:
    value: UNKNOWN
    cites: [{source: S1, locator: "whole article"}, {source: S3, locator: "prefaces and treatises scanned for gods/religion"}, {source: S4, locator: "Method letter/body"}, {source: S5, locator: "biographical opening"}]
    how_known: "Deepen D1: no statement of his on gods, religion or a worldview system in Heath (S3), Method (S4), MacTutor (S1) or DSB (S5). Plutarch's portrait (pure mathematics as the only worthy pursuit) is reported character, not a worldview (P19)."
    note: "Still useful: Dijksterhuis, Archimedes (1956/1987) if a fuller monograph pass is wanted; Heath already opened for LIO."
  secondary_system: {value: UNKNOWN, how_known: "No system evidence."}
  candidate_codes_considered: []
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Deepen D1 checked Heath Works (prefaces to Dositheus; Sand-Reckoner; Equilibrium; Floating Bodies), Method (S4), MacTutor and DSB: nothing of his on gods or the divine (P19). Cicero/Plutarch 'divine genius' praise is later rhetorical, not his view."}
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.5
      support: corroborated
      cites: [{source: S3, locator: "On the Equilibrium of Planes I, Postulates 1–7 and Props. 6–7; On Floating Bodies I, Postulate 1 and Prop. 2"}, {source: S1, locator: "Biography (On plane equilibriums; On floating bodies)"}]
      how_known: "His own published treatises in Heath's scholarly edition (S3), corroborated by MacTutor's account of the same works (S1). Scientist under P30 (results about physical systems). Named alternative 4, so 0.5 (P16 Hilbert addendum / P35). Independent sources → corroborated (P48)."
      rationale: "Scored on his account of nature (P6). Equilibrium postulates state general weight/distance regularities ('Equal weights at equal distances are in equilibrium…'); Props. 6–7: magnitudes 'balance at distances reciprocally proportional to the magnitudes.' Floating Bodies Postulate 1 states the character of a fluid; Prop. 2: 'The surface of any fluid at rest is the surface of a sphere whose centre is the same as that of the earth.' These are lawful physical regularities in his own words, with no stated no-exception / miracle claim → B 3 at 0.5, alternative 4 (P16 Hilbert; P35). Named alternative: 4."
    C_ledger: {value: UNKNOWN, how_known: "Nothing in the sources read (P19)."}
    D_authority: {value: UNKNOWN, how_known: "Nothing on revelation; working science does not bear on D (P19)."}
    E_scope: {value: BELOW_THRESHOLD, note: "Scored on the world's order (P7). Working science / Sand-Reckoner cosmology assumptions bear on E's first question but E is not scored from them alone (P19).", how_known: "BELOW_THRESHOLD under P19: not scored from working science alone."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, which takes precedence (§6, P19)."}
  statements:
    - text: "I postulate the following: 1. Equal weights at equal distances are in equilibrium, and equal weights at unequal distances are not in equilibrium but incline towards the weight which is at the greater distance. … 6. If magnitudes at certain distances be in equilibrium, (other) magnitudes equal to them will also be in equilibrium at the same distances."
      cites: [{source: S3, locator: "On the Equilibrium of Planes I, Postulates 1 and 6 (pp. 189–190 Heath)"}]
      date: "-212"
      context: "Opening postulates of On the Equilibrium of Planes, Book I. Date is terminus ante quem (death 212 BC); works undated."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-23
    - text: "Two magnitudes, whether commensurable [Prop. 6] or incommensurable [Prop. 7], balance at distances reciprocally proportional to the magnitudes."
      cites: [{source: S3, locator: "On the Equilibrium of Planes I, Props. 6–7 (p. 192 Heath)"}]
      date: "-212"
      context: "Law of the lever. Date terminus ante quem (death 212 BC)."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-23
    - text: "Let it be supposed that a fluid is of such a character that, its parts lying evenly and being continuous, that part which is thrust the less is driven along by that which is thrust the more; and that each of its parts is thrust by the fluid which is above it in a perpendicular direction if the fluid be sunk in anything and compressed by anything else."
      cites: [{source: S3, locator: "On Floating Bodies I, Postulate 1 (p. 253 Heath)"}]
      date: "-212"
      context: "Opening postulate of On Floating Bodies, Book I. Date terminus ante quem (death 212 BC)."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-23
    - text: "The surface of any fluid at rest is the surface of a sphere whose centre is the same as that of the earth."
      cites: [{source: S3, locator: "On Floating Bodies I, Proposition 2 (p. 254 Heath)"}]
      date: "-212"
      context: "Hydrostatics; derives rest-surface geometry from Postulate 1. Date terminus ante quem (death 212 BC)."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-23
  changes_over_life: []
  coder_notes: "Deepen D1: B now rests on Heath's scholarly edition of his own statics/hydrostatics (written_profession), still capped at 0.5 with alt 4 (no no-exception claim). A stays UNKNOWN — no god/divine line in the works opened. Plutarch/Cicero 'divine' praise is later rhetoric, unused for A. Ancient-source caution: biography outside his prefaces is Plutarch, Livy, Cicero, Tzetzes."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Greek of Syracuse", certainty: 0.7, cites: [{source: S1, locator: "Biography"}, {source: S5, locator: "opening (Syracuse; Greek mathematical culture)"}], how_known: "City and Dorian Greek of the treatises (S3); two bios."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not in the source read."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not in the source read."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not in the source read."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: UNKNOWN, how_known: "No work is dated in the sources read (S1: order of works 'not known for certain'); the period ends by 212 BC at the latest (P30)."}
  age_at_first_lasting_contribution: {value: UNKNOWN, how_known: "First-lasting year unknown."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No statement scored at 3 or 4; B rests on working science (P27)."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", rationale: "B 3 @ 0.5 rests on lawful regularities without a no-exception claim and is not an LIO-type view at 3/4 with ≥0.7 (P27). Nothing on gods.", certainty: 0.5, cites: [{source: S3, locator: "Equilibrium; Floating Bodies"}, {source: S1, locator: "whole article"}], how_known: "Scored B is below the LIO-type-view bar (P27)."}
  worldview_during_major_work: {value: TODO}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "His treatises proceed by definition, postulate and proof; he discovered some results by mechanics then proved them by geometry (Method preface, S4; Quadrature preface, S3).", certainty: 1.0, cites: [{source: S3, locator: "Quadrature of the Parabola preface to Dositheus"}, {source: S4, locator: "Method preface"}], how_known: "Two Heath editions."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "Biography paragraph 2 (likely study with Euclid's successors)"}], how_known: "Training is conjecture."}
  circle_present: {value: "unclear", rationale: "No God–Nature statement read.", certainty: 0.5, cites: [{source: S1, locator: "whole article"}], how_known: "No evidence either way."}
  reading: "As belief, not finding: form present, circle unclear. The record does not test H1."
  notes: ""

institutions: []
collaborators:
  - {value: "Conon of Samos", relation: correspondent, note: "mathematician at Alexandria and close friend", certainty: 0.7, cites: [{source: S1, locator: "Biography paragraph 2"}], how_known: "MacTutor."}

review:
  roster_status_reason: {value: "Core in v8 (F 5: Claude, DeepSeek, Gemini, GPT, Grok).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 8"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Britannica still blocked (Cloudflare, 2026-10-23); basics now dual-sourced MacTutor + DSB (encyclopedia.com)."
    - "No work of his is dated; first-lasting year, period and age remain UNKNOWN."
    - "B certainty stays 0.5 (faded): P16/P35 bar without a no-exception claim; cannot darken from deepen alone."
  open_questions:
    - "Dated chronology of the works (Netz; Dijksterhuis) if a first-lasting year is needed."
    - "Any god/divine remark outside the Heath corpus (unlikely; none found in Method or main treatises)."

sources:
  - id: S1
    type: secondary
    kind: "institutional page"
    author: "J. J. O'Connor and E. F. Robertson"
    year: 1999
    citation: "O'Connor, J. J., and E. F. Robertson. \"Archimedes.\" MacTutor History of Mathematics Archive, University of St Andrews, last update January 1999. https://mathshistory.st-andrews.ac.uk/Biographies/Archimedes/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Archimedes/"
    accessed: 2026-10-15
    reliability_note: "Standard reference biography; draws on Heath, Clagett and Dijksterhuis."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, collaborators]
  - id: S2
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-15
    reliability_note: "Study's own roster; used only for rank, F and status."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S3
    type: primary
    kind: "scholarly edition"
    author: "Archimedes; Thomas L. Heath (ed. and trans.)"
    year: 1897
    citation: "Heath, T. L., ed. and trans. The Works of Archimedes. Cambridge: Cambridge University Press, 1897. Internet Archive scan (worksofarchimede00arch)."
    url: "https://archive.org/details/worksofarchimede00arch"
    accessed: 2026-10-23
    reliability_note: "Standard English scholarly edition from Heiberg's Greek. Equilibrium I postulates/Props. 6–7 and Floating Bodies I Post. 1 / Prop. 2 read in the OCR text of this scan."
    source_quality: "scholarly edition or monograph"
    used_for: [identity, basics, contribution, childhood, worldview, timing, lane_b]
  - id: S4
    type: primary
    kind: "scholarly edition"
    author: "Archimedes; Thomas L. Heath (ed. and trans.)"
    year: 1912
    citation: "Heath, T. L., ed. The Method of Archimedes, Recently Discovered by Heiberg: A Supplement to The Works of Archimedes, 1897. Cambridge: Cambridge University Press, 1912."
    url: "https://www.ms.uky.edu/~sohum/ma330/files/archimedes_method_heath.pdf"
    accessed: 2026-10-23
    reliability_note: "Heath's Method supplement; preface and body checked for god/divine language (none). Used for Lane B form and A-negative check."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview, lane_b]
  - id: S5
    type: secondary
    kind: encyclopedia
    author: "Marshall Clagett (Complete Dictionary of Scientific Biography)"
    year: 2008
    citation: "\"Archimedes.\" Complete Dictionary of Scientific Biography. Encyclopedia.com (Gale). https://www.encyclopedia.com/people/science-and-technology/mathematics-biographies/archimedes."
    url: "https://www.encyclopedia.com/people/science-and-technology/mathematics-biographies/archimedes"
    accessed: 2026-10-23
    reliability_note: "DSB article (Gale Complete DSB reprint); scholarly biography. Britannica remained Cloudflare-blocked."
    source_quality: "reference entry"
    used_for: [identity, basics, childhood, worldview, heritage]
---

# Archimedes

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Archimedes of Syracuse (c. 287–212 BC), mathematician and engineer, found areas, volumes and surfaces by the method of exhaustion, set out the principles of statics and hydrostatics, and stated Archimedes' principle [S1; S3; S5]. Deepen D1 (P47–P50): his own Equilibrium and Floating Bodies texts (Heath) give B 3 at 0.5, written_profession, corroborated (S3+S1); A stays UNKNOWN (no god statement in Heath/Method/DSB); mid_basin UNKNOWN. Still unplotted (A UNKNOWN; B faded).

## Life and work

Son of the astronomer Phidias, native of Syracuse, probably in touch with Euclid's successors in Alexandria; killed in 212 BC when the Romans took Syracuse [S1; S3; S5].

## Contribution and impact

On the sphere and cylinder, Quadrature of the parabola, On the equilibrium of planes, On floating bodies, The Method [S1; S3; S4].

## Childhood and education

Nothing beyond his father's name and profession [S3; S5].

## Adult working worldview

No system or A statement. B is scored 3 at 0.5 from his own statics and hydrostatics in Heath (written_profession; alt 4 under P16/P35), corroborated by MacTutor [S3; S1].

## Heritage (context only)

Greek of Syracuse [S1; S5].

## Timing

No work is dated; first-lasting year unknown.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form present (Heath Method / Quadrature prefaces); circle unclear [S3; S4].

## Open questions

- Dated chronology of the works (Netz; Dijksterhuis) if a first-lasting year is needed.
- Any god/divine remark outside the Heath corpus (none found in Method or main treatises).

## Research log

- 2026-10-15: Read MacTutor. Britannica blocked (Cloudflare). Web search for his religious views found nothing citable.
- 2026-10-23: Deepen D1 (queue #8). Heath Works (S3) and Method (S4); DSB via encyclopedia.com (S5). B support single → corroborated; A stays UNKNOWN. P47 labels. No fallacy_catalog (Jason 2026-10-23).
