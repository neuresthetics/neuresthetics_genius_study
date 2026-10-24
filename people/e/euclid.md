---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 2
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch E)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-15
  last_updated: 2026-10-24
  change_log:
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #25, pause-batch close). P47 source_quality on every source. Added MacTutor (S3), Burton Optics JOSA 1945 scholarly English of Optica (S4; OCR of Definitions 1–4 and Props. 1–3), DSB Toomer via encyclopedia.com/MacTutor PDF (S5), Heath Elements CUP 1908 Vol. I (S6; scholarly edition of Elements for contribution and A-negative). Listed Optics as lasting contribution about vision → scientist under P30. B_cause UNKNOWN → 3 @ 0.5 written_profession, support corroborated (S4+S3; alt 4; P16 Hilbert / P35). A_locus stays UNKNOWN: no god/divine statement in Optics (Burton), Elements (no prefaces; MacTutor; Heath corpus), or DSB; Proclus 'Platonist' is late reported speech and DSB judges it not necessarily conclusive (P42, P19). primary_system UNKNOWN; C/D UNKNOWN; E BELOW_THRESHOLD (P19); mid_basin UNKNOWN. Chart: still unplotted (A UNKNOWN; B faded @ 0.5). No fallacy_catalog (Jason 2026-10-23). Draft, not reviewed."}
    - {date: 2026-10-15, by: "Grok Bot", summary: "Record created (stage 3 batch E, order P32: F 5, rank 25). Britannica (van der Waerden): 'Of Euclid's life nothing is known' beyond Proclus. Undated works (P39). Mathematician with no listed contribution about natural systems; no worldview statement survives in the source read. All worldview fields UNKNOWN. Draft, not reviewed."}

identity:
  id: euclid
  display_name: "Euclid"
  roster:
    canonical_name: "Euclid"
    rank: 25
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: mathematics
    field_bucket: mathematics
  full_name: {value: "Euclid of Alexandria", certainty: 1.0, cites: [{source: S1, locator: "header / Life (taught at Alexandria)"}, {source: S3, locator: "Quick Info; Biography opening ('Euclid of Alexandria')"}], how_known: "Two reference biographies (P15); Alexandria is where he taught, not a proven birthplace."}
  native_name: {value: "Eukleides", certainty: 0.7, cites: [{source: S1, locator: "Quick Facts ('Greek: Eukleides')"}], how_known: "Britannica's transliteration; single source, 0.7."}
  aliases:
    - {name: "Euclid of Alexandria", kind: "other"}
    - {name: "Euclides", kind: "latinized"}

basics:
  birth:
    date: {value: UNKNOWN, how_known: "Only flourished dates: Britannica 'c. 300 bce'; MacTutor 'about 325 BC (probably)'; DSB middle of active career ~295 BC with wide uncertainty (S1; S3; S5). No exact birth year."}
    place: {value: UNKNOWN, how_known: "DSB: birthplace unknown (S5). MacTutor Quick Info guesses Alexandria; that is where he taught, not a proven birthplace (S3). Arabian Tyre / Megara traditions rejected as fiction or confusion with Euclid of Megara (S3; S5)."}
  death:
    date: {value: UNKNOWN, how_known: "MacTutor 'about 265 BC' and DSB '~270 BC' are conjectures from the Apollonius pupil timeline, not documented (S3; S5)."}
    place: {value: UNKNOWN, how_known: "Not recorded; Alexandria is the natural assumption only (S5)."}
  first_lasting_contribution_year: {value: UNKNOWN, how_known: "Elements, Optics, Phaenomena and other works are undated; only a terminus in the reign of Ptolemy I / flourished c. 300 BC (P39; S1; S3; S5)."}
  era_bucket: {value: "-500 to 499", certainty: 1.0, cites: [{source: S1, locator: "Quick Facts; Life (Ptolemy I, 323–285 BC)"}, {source: S3, locator: "Quick Info (~325–265 BC)"}, {source: S5, locator: "heading (fl. ca. 295 B.C.)"}], how_known: "Every candidate working year falls in '-500 to 499' (P2, P39); three sources."}
  region_of_birth: {value: UNKNOWN, how_known: "Birthplace unknown (S5)."}
  region_of_work: {value: "Middle East and North Africa", certainty: 1.0, cites: [{source: S1, locator: "Life (taught at Alexandria)"}, {source: S3, locator: "Biography (Alexandria)"}, {source: S5, locator: "Alexandrian residence (Pappus)"}], how_known: "Egypt / Northern Africa in data/reference/regions.csv (P3); three sources."}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S1, locator: "text"}, {source: S3, locator: "throughout"}], how_known: "As the sources record it."}
  languages_of_work: {value: [Greek], certainty: 1.0, cites: [{source: S1, locator: "text (Greek terms)"}, {source: S4, locator: "Greek Optica; Burton from Greek"}, {source: S6, locator: "Heath from Heiberg Greek"}], how_known: "Surviving works in Greek."}
  occupations: {value: ["mathematician", "teacher"], certainty: 1.0, cites: [{source: S1, locator: "opening; Life"}, {source: S3, locator: "Summary; Biography"}], how_known: "Two sources."}

contribution:
  fields: {value: ["geometry", "number theory", "optics", "astronomy"], certainty: 1.0, cites: [{source: S1, locator: "Sources and contents"}, {source: S3, locator: "Elements; Optics; Phaenomena"}, {source: S5, locator: "Optics; Phaenomena sections"}], how_known: "Elements, Optics and Phaenomena survive; three sources."}
  lasting_original_contributions:
    - {value: "The Elements: axiomatic geometry from definitions, postulates and common notions; Euclidean algorithm; infinitude of primes; five regular solids", year: "undated (c. 300 BC)", kind: work, lasting: "'one of the most influential books ever written'; 'the whole design of his work was his own' (S1); Heath: 'the greatest mathematical textbook of all time' (S3 quoting Heath)", certainty: 1.0, cites: [{source: S1, locator: "opening; Sources and contents"}, {source: S3, locator: "Biography (Elements)"}, {source: S6, locator: "Heath ed., Books I–XIII"}], how_known: "Three sources. Pure mathematics alone would not make him a scientist (P30); Optics does (below)."}
    - {value: "Optics (Optica): axiomatic geometrical theory of vision (visual rays from the eye; visual cone; apparent size by visual angle)", year: "undated (c. 300 BC; before Phaenomena)", kind: "law or principle", lasting: "First Greek treatise on perspective/optics; remained the only one until Ptolemy (S5); foundational for later optics and Renaissance perspective (S3; S5)", certainty: 1.0, cites: [{source: S4, locator: "Definitions 1–7; Props. 1–3 (Burton)"}, {source: S5, locator: "Optics section (earlier recension Euclid's; Theon's later)"}, {source: S3, locator: "surviving works list (Optics)"}], how_known: "His Optica in Burton's scholarly English (S4) plus DSB/MacTutor. Theory about vision → lasting contribution about natural/physical systems → scientist under P30. Catoptrica excluded (not his; S5)."}
  evidence_of_impact:
    - {value: "Contemporaries 'considered his work final and authoritative'; Elements primary source of geometric reasoning until non-Euclidean geometry", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "Sources and contents, end"}, {source: S3, locator: "van der Waerden quotation"}], how_known: "Britannica and MacTutor."}
  major_works:
    - {value: "Elements (13 books)", year: "undated (c. 300 BC)", kind: book, certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S3, locator: "Biography"}, {source: S6, locator: "title"}], how_known: "Three sources."}
    - {value: "Optics (Optica)", year: "undated (c. 300 BC)", kind: book, certainty: 1.0, cites: [{source: S4, locator: "title / Definitions"}, {source: S5, locator: "Optics section"}], how_known: "Two sources; earlier recension authentic (S5)."}
    - {value: "Phaenomena", year: "undated (c. 300 BC)", kind: book, certainty: 0.7, cites: [{source: S3, locator: "surviving works"}, {source: S5, locator: "Astronomy: Phaenomena"}], how_known: "Textbook of sphaeric; preface cites Optics (S5)."}
    - {value: "Data", year: "undated", kind: book, certainty: 0.7, cites: [{source: S3, locator: "surviving works"}], how_known: "MacTutor."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Elements and Optics still foundational; axiomatic method.", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "Optics section"}], how_known: "Britannica and DSB."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Nothing known of his life beyond Alexandria teaching (S1; S3; S5)."}
  family_religious_practice: {value: UNKNOWN, how_known: "Nothing known (S1; S3; S5)."}
  parents_and_household: []
  household_circumstances: {value: UNKNOWN, how_known: "Arabic Naucrates/Tyre stories are fictitious (S3; S5)."}
  schooling: []
  early_mathematics: {value: UNKNOWN, how_known: "MacTutor/DSB conjecture Academy training from knowledge of Eudoxus/Theaetetus; not documented (S3; S5)."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Nothing known."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Nothing known."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: UNKNOWN, how_known: "Undated works (P39); equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No statement of his on religion or science–religion. The 'no royal road' and threepence anecdotes are Proclus/Stobaeus reported speech, not about religion (S3; S5; P42)."}
  primary_system:
    value: UNKNOWN
    cites: [{source: S3, locator: "Proclus quotation ('In his aim he was a Platonist')"}, {source: S5, locator: "Life (Proclus Platonist claim; 'not… necessarily conclusive')"}, {source: S4, locator: "Optics Definitions and Props. 1–3 scanned for gods/religion"}, {source: S6, locator: "Elements: no authorial preface; mathematical content only"}]
    how_known: "Deepen D1: Proclus's 'Platonist' label is late doxography (reported speech) and DSB explicitly says the testimony of so zealous a Neoplatonist is not necessarily conclusive (S5; P42). No own-words system claim in Optics (S4), Elements (S6; MacTutor: no prefaces), or the bios. Lead toward PLATO kept in open_questions only."
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: PLATO, reason: "Proclus aim-Platonist / Book XIII regular solids — reported and inconclusive (S5); not scored (P42)."}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "Deepen D1 checked Burton Optics Definitions and Props. 1–3 (S4), MacTutor/DSB accounts of the Elements and life (S3; S5), and Heath Elements as the scholarly edition of the mathematical corpus (S6): nothing of his on gods or the divine (P19). Proclus 'Platonist' and 'God is for ever doing geometry' Academy motto (DSB note) are not his words (P42)."}
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.5
      support: corroborated
      cites: [{source: S4, locator: "Optics Definitions 1–4 (Burton, JOSA 35:357)"}, {source: S3, locator: "Biography (Optics surviving; first Greek work on perspective)"}]
      how_known: "His Optica in Burton's scholarly English (S4), corroborated by MacTutor's account of the same work (S3). Scientist under P30 once Optics is listed (theory of vision). Named alternative 4, so 0.5 (P16 Hilbert addendum / P35). Independent sources → corroborated (P48)."
      rationale: "Scored on his account of nature (P6). Optics Definitions postulate lawful regularities of vision: rectilinear rays from the eye through space; the visual field a cone with apex at the eye; things seen iff rays fall on them; apparent size by visual angle. Props. 1–3 derive distance and clarity consequences from those postulates. These are physical regularities in his own words, with no stated no-exception / miracle claim → B 3 at 0.5, alternative 4 (P16 Hilbert; P35). Pure-math Platonism alone would have been BELOW_THRESHOLD; Optics supplies the physics-facing work. Named alternative: 4."
    C_ledger: {value: UNKNOWN, how_known: "Nothing in the sources read (P19)."}
    D_authority: {value: UNKNOWN, how_known: "Nothing on revelation; working science does not bear on D (P19)."}
    E_scope: {value: BELOW_THRESHOLD, note: "Scored on the world's order (P7). Optics/Phaenomena working science bears on E's first question but E is not scored from working science alone (P19).", how_known: "BELOW_THRESHOLD under P19: not scored from working science alone."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, which takes precedence (§6, P19)."}
  statements:
    - text: "1. Let it be assumed that lines drawn directly from the eye pass through a space of great extent; 2. and that the form of the space included within our vision is a cone, with its apex in the eye and its base at the limits of our vision; 3. and that those things upon which the vision falls are seen, and that those things upon which the vision does not fall are not seen; 4. and that those things seen within a larger angle appear larger, and those seen within a smaller angle appear smaller, and those seen within equal angles appear to be of the same size."
      cites: [{source: S4, locator: "Optics Definitions 1–4 (Burton, JOSA 35 (1945): 357)"}]
      date: "-300"
      context: "Opening definitions/postulates of Optica. Date is conventional flourished c. 300 BC; works undated (P39). Visual-ray theory of vision."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
    - text: "Nothing that is seen is seen at once in its entirety. … So AD will not be seen in its entirety at the same time. But it seems to be seen all at once because the rays of vision shift rapidly."
      cites: [{source: S4, locator: "Optics Proposition 1 (Burton, JOSA 35:357)"}]
      date: "-300"
      context: "Prop. 1 derives non-simultaneous whole-object vision from discrete diverging visual rays. Date conventional flourished."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
  changes_over_life: []
  coder_notes: "Deepen D1: B now rests on Optics (written_profession), still capped at 0.5 with alt 4 (no no-exception claim). A stays UNKNOWN — Proclus Platonist is P42 reported speech; DSB says not conclusive. Phaenomena preface (universe as sphere) not opened this pass; Berggren & Thomas 1996 is the lead if a cosmology quote is wanted. Catoptrica excluded as not his (S5)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Greek", certainty: 0.7, cites: [{source: S1, locator: "opening ('mathematician of Greco-Roman antiquity')"}, {source: S3, locator: "Biography (Greek mathematician)"}], how_known: "Language and mathematical culture; two bios."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Nothing known."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Nothing known."}
  childhood_catechism: {value: UNKNOWN, how_known: "Nothing known."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: UNKNOWN, how_known: "Works undated (P39); flourished c. 300 BC under Ptolemy I (S1; S3; S5)."}
  age_at_first_lasting_contribution: {value: UNKNOWN, how_known: "Birth and work years unknown (P39)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No statement scored at 3 or 4 with ≥0.7; B rests on working science / Optics postulates without a no-exception claim (P27)."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", rationale: "B 3 @ 0.5 rests on lawful vision regularities without a no-exception claim and is not an LIO-type view at 3/4 with ≥0.7 (P27). Nothing on gods.", certainty: 0.5, cites: [{source: S4, locator: "Optics Definitions"}, {source: S3, locator: "whole article"}], how_known: "Scored B is below the LIO-type-view bar (P27)."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "primary_system UNKNOWN."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "yes", rationale: "Elements and Optics proceed by definition/postulate and proof; he is the source of the axiomatic geometric textbook tradition.", certainty: 1.0, cites: [{source: S1, locator: "Sources and contents"}, {source: S4, locator: "Optics Definitions → propositions"}, {source: S6, locator: "Elements structure"}], how_known: "Three sources."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S3, locator: "Biography (Academy conjecture)"}, {source: S5, locator: "probable Academy attendance"}], how_known: "Training is conjecture from Eudoxus/Theaetetus content."}
  circle_present: {value: "unclear", rationale: "No God–Nature statement of his; Proclus Platonist is reported only.", certainty: 0.5, cites: [{source: S5, locator: "Proclus Platonist paragraph"}, {source: S4, locator: "Optics (no gods)"}], how_known: "No own-words evidence either way."}
  reading: "As belief, not finding: form present, circle unclear. The record does not test H1."
  notes: ""

institutions: []
collaborators: []

review:
  roster_status_reason: {value: "Core in v8 (F 5).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 25"}], how_known: "Study roster."}
  controversies:
    - {value: "How much of the Elements is his own versus compiled from predecessors", certainty: 0.7, cites: [{source: S1, locator: "Sources and contents, end"}, {source: S3, locator: "Biography (compilation vs organisation)"}], how_known: "Britannica and MacTutor."}
    - {value: "Itard hypotheses (historical individual / team under his name / Bourbaki-style fiction); MacTutor assumes historical individual (i)", certainty: 0.5, cites: [{source: S3, locator: "Itard three hypotheses"}], how_known: "MacTutor; record treats him as historical author of Optica/Elements (S4; S5)."}
  data_quality_flags:
    - "Medieval editors confused him with Eukleides of Megara (S1; S3)."
    - "No work of his is dated; first-lasting year, period and age remain UNKNOWN (P39)."
    - "B certainty stays 0.5 (faded): P16/P35 bar without a no-exception claim; cannot darken from deepen alone."
    - "Britannica body still used from the 2026-10-15 create-pass read (S1); deepen dual-sourced MacTutor + DSB for basics."
  open_questions:
    - "Phaenomena preface (universe as sphere) — Berggren & Thomas 1996 — if a cosmology quote is wanted for B/E."
    - "Any god/divine remark outside Optics/Elements (unlikely; none found)."
    - "Proclus Platonist lead toward PLATO if a ruling ever allows late doxography (currently P42 blocks)."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Bartel Leendert van der Waerden"
    citation: "van der Waerden, B. L. \"Euclid.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Euclid-Greek-mathematician."
    url: "https://www.britannica.com/biography/Euclid-Greek-mathematician"
    accessed: 2026-10-15
    reliability_note: "Signed article body; 'Top Questions' not used. Create-pass read; deepen used MacTutor+DSB as fresh dual sources."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, review]
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
    type: secondary
    kind: "institutional page"
    author: "J. J. O'Connor and E. F. Robertson"
    year: 1999
    citation: "O'Connor, J. J., and E. F. Robertson. \"Euclid.\" MacTutor History of Mathematics Archive, University of St Andrews, last update January 1999. https://mathshistory.st-andrews.ac.uk/Biographies/Euclid/."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Euclid/"
    accessed: 2026-10-24
    reliability_note: "Standard reference biography; quotes Proclus, Heath, van der Waerden, Itard; lists Optics and Phaenomena among surviving works."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, review]
  - id: S4
    type: primary
    kind: "scholarly edition"
    author: "Euclid; Harry Edwin Burton (trans.)"
    year: 1945
    citation: "Burton, Harry Edwin, trans. \"The Optics of Euclid.\" Journal of the Optical Society of America 35, no. 5 (May 1945): 357–372. Read in the philomatica.org PDF scan; Definitions 1–7 and Props. 1–3 OCR'd 2026-10-24."
    url: "https://philomatica.org/wp-content/uploads/2013/01/Optics-of-Euclid.pdf"
    accessed: 2026-10-24
    reliability_note: "Scholarly English translation of Euclid's Optica (earlier recension) published in JOSA; Greek base is the Heiberg tradition. Definitions 1–4 and Prop. 1 quoted from OCR of this scan (verified_against scholarly edition)."
    source_quality: "scholarly edition or monograph"
    used_for: [contribution, worldview, lane_b]
  - id: S5
    type: secondary
    kind: encyclopedia
    author: "G. J. Toomer (Complete Dictionary of Scientific Biography)"
    year: 2008
    citation: "Toomer, G. J. \"Euclid.\" Complete Dictionary of Scientific Biography. Encyclopedia.com / MacTutor DSB PDF reprint. https://mathshistory.st-andrews.ac.uk/DSB/Euclid.pdf."
    url: "https://mathshistory.st-andrews.ac.uk/DSB/Euclid.pdf"
    accessed: 2026-10-24
    reliability_note: "DSB Life and Works + Optics/Phaenomena sections; authenticity of Optics earlier recension; Catoptrica rejected; Proclus Platonist judged not necessarily conclusive."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, review]
  - id: S6
    type: primary
    kind: "scholarly edition"
    author: "Euclid; Thomas L. Heath (ed. and trans.)"
    year: 1908
    citation: "Heath, T. L., ed. and trans. The Thirteen Books of Euclid's Elements, Vol. I. Cambridge: Cambridge University Press, 1908 (from Heiberg). Google Books / Wikimedia scan used for edition identity; Book I–XIII mathematical corpus — no authorial preface or god/divine statement (MacTutor confirms no prefaces survive)."
    url: "https://archive.org/details/thirteenbookseu01heibgoog"
    accessed: 2026-10-24
    reliability_note: "Standard English scholarly edition from Heiberg. Used for Elements contribution citation and A-negative (mathematical corpus; no worldview preface)."
    source_quality: "scholarly edition or monograph"
    used_for: [contribution, worldview, lane_b]
---

# Euclid

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Euclid of Alexandria (flourished c. 300 BC), author of the *Elements* and of the *Optics* [S1; S3; S4; S5]. Deepen D1 (P47–P50): *Optics* Definitions give B 3 at 0.5, written_profession, corroborated (S4+S3); A stays UNKNOWN (no god statement; Proclus Platonist is P42 reported speech); mid_basin UNKNOWN. Still unplotted (A UNKNOWN; B faded).

## Life and work

Taught at Alexandria under Ptolemy I; almost nothing else of his life is securely known [S1; S3; S5]. Confused in medieval sources with Euclid of Megara [S1; S3].

## Contribution and impact

*Elements* (axiomatic geometry); *Optics* (geometrical theory of vision); also *Data*, *Phaenomena*, and lost works [S1; S3; S4; S5; S6]. *Catoptrica* under his name is not his [S5].

## Childhood and education

Unknown [S1; S3; S5]. Academy training is conjecture from Eudoxus/Theaetetus content [S3; S5].

## Adult working worldview

No own-words system or god statement survives [S3; S4; S5; S6]. *Optics* postulates lawful visual-ray regularities → B 3 @ 0.5 (alt 4) [S4; S3]. Proclus's Platonist label is late doxography, not scored [S5; P42].

## Heritage (context only)

Greek-speaking mathematical culture [S1; S3].

## Timing

Undated works; flourished c. 300 BC (P39) [S1; S3; S5].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Geometric form yes (*Elements*, *Optics*) [S1; S4; S6]. Circle unclear.

## Open questions

- *Phaenomena* preface (Berggren & Thomas).
- Proclus Platonist lead (P42).

## Research log

- 2026-10-15: Read Britannica.
- 2026-10-24: Deepen D1 (queue #25). MacTutor; Burton *Optics* JOSA 1945 (OCR Defs 1–4, Prop. 1); DSB Toomer; Heath Elements ed. identity. B UNKNOWN → 3 @ 0.5 corroborated; A stays UNKNOWN. No fallacy_catalog.
