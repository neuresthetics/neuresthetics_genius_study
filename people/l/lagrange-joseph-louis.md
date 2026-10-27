---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA4; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to mathematics. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA4, order P32: F 3, rank 195). Source: Britannica, signed by Dirk Jan Struik (scholars edition, read in full). Lasting work: the equations that bear his name, first used in his prize essay on the libration of the Moon (1764, French Academy prize), and Mécanique analytique (1788), 'the basis for all later work in this field'; span 1764–1788 by the prize award and publication (P30 #1), age 28. His earlier calculus of variations (praised by Euler) is undated in the source; 0.5 on the first year, alternative earlier. Scientist (P30): analytic and celestial mechanics are results about physical systems; no statement of his own, so B 3 at 0.5, alt 4 (P35). No worldview source: primary_system UNKNOWN; A UNKNOWN; mid_basin UNKNOWN. Not plotted. Draft, not reviewed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #184 / 228, F 3 rank 195). Goals: add sources; firm B; leave A silence if none; do not force plot. Read Mécanique analytique 2nd ed. 1811 (IA OCR mcaniqueanalyt01lagr, S4) for own-voice least-action remark (p. 246); Delambre 1816 Notice (FR Wikisource, S5) for reported reserve about culte and deathbed body-rest remark; Wikipedia EN (S3, P50 dual bio) and HSM/Conifold quotation of Boissonnade & Vagliente translators' bio (S6) for heritage/leads. P47 source_quality on S1–S6. A stays UNKNOWN (P19): Kline 'agnostic', Marechal Dictionnaire des Athées, Napoleon-at-Mass, and Mass-regularly claims are secondary or reported; no first-person locus. primary_system UNKNOWN; AGNOS rejected as code (lead only). B 3 @0.5 inference_from_work → 3 @0.5 written_profession support corroborated (S4+S1): 'je regarde non comme un principe métaphysique, mais comme un résultat simple et général des lois de la Mécanique' (MA p. 246); alt 4 (P16/P35/P40: lawful remark, no no-exception). first_evidence_of_lio_type_views UNKNOWN→1788. mid_basin UNKNOWN. Chart-moving NO (A UNKNOWN). No fallacy_catalog. No figures/. Draft, not reviewed."}

identity:
  id: lagrange-joseph-louis
  display_name: "Joseph-Louis Lagrange"
  roster:
    canonical_name: "Joseph-Louis Lagrange"
    rank: 195
    F: 3
    models: [Claude, Gemini, Grok]
    band: "core (3–4)"
    status: "core"
    field: "mathematics"
    field_bucket: "mathematics"
  full_name: {value: "Joseph-Louis Lagrange, comte de l'Empire", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  native_name: {value: "Giuseppe Luigi Lagrangia", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S7, locator: "baptism name Giuseppe Lodovico Lagrangia"}], how_known: "Britannica; MacTutor baptism form Lodovico."}
  aliases:
    - {name: "Lagrange-Joseph-Louis", kind: "roster alias"}
    - {name: "Giuseppe Luigi Lagrangia", kind: "birth name"}
    - {name: "Giuseppe Lodovico Lagrangia", kind: "other"}

basics:
  birth:
    date: {value: "1736-01-25", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
    place: {value: "Turin", modern_name: "Turin, Italy", polity_then: "Kingdom of Sardinia (Sardinia-Piedmont)", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  death:
    date: {value: "1813-04-10", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
    place: {value: "Paris", modern_name: "Paris, France", polity_then: "French Empire", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  first_lasting_contribution_year: {value: 1764, certainty: 0.5, cites: [{source: S1, locator: "para. 3"}], how_known: "Prize essay on the libration of the Moon, 1764, in which 'he used the equations that now bear his name' (S1); the award year stands for the essay's submission (P30 #1). 0.5: his calculus of variations, praised by Euler, is earlier but undated in S1; alternative an earlier year for that."}
  era_bucket: {value: "1750 to 1849", certainty: 0.7, cites: [{source: S1, locator: "para. 3"}, {source: S1, locator: "Introduction"}], how_known: "1764–1788 (P2); an earlier alternative stays after 1750 (he was born 1736 and taught from about age 19)."}
  region_of_birth: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Italy (P3)."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "para. 4–5"}], how_known: "Berlin 1766–1787; Paris."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["French", "Latin"], certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "French titles; Latin early papers (coder's reading)."}
  occupations: {value: ["mathematician", "professor"], certainty: 0.7, cites: [{source: S1, locator: "Introduction; para. 6"}], how_known: "Britannica."}

contribution:
  primary_domain: mathematics
  fields: {value: ["analytic mechanics", "celestial mechanics", "number theory", "algebra"], certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Lagrange's equations (libration of the Moon essay)", year: 1764, kind: "law or principle", lasting: "'the equations that now bear his name' (S1)", certainty: 0.5, cites: [{source: S1, locator: "para. 3"}], how_known: "Britannica; French Academy prize 1764 (0.5, see first-lasting year)."}
    - {value: "Réflexions sur la résolution algébrique des équations", year: 1770, kind: "work", lasting: "'inaugurated a new period in algebra and inspired Évariste Galois to his group theory' (S1)", certainty: 0.7, cites: [{source: S1, locator: "para. 4"}], how_known: "Britannica."}
    - {value: "Mécanique analytique", year: 1788, kind: "work", lasting: "'the basis for all later work in this field' (S1); own-voice least-action remark as result of mechanical laws, not metaphysics (S4)", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S4, locator: "p. 246 (2nd ed. 1811)"}], how_known: "Britannica; IA OCR of 1811 edition."}
  evidence_of_impact:
    - {value: "Lagrangian equations; generalized coordinates", kind: "named after them", certainty: 0.7, cites: [{source: S1, locator: "para. 5"}], how_known: "Britannica."}
  major_works:
    - {value: "Théorie des fonctions analytiques", year: 1797, kind: "book", certainty: 0.7, cites: [{source: S1, locator: "para. 6"}], how_known: "Britannica."}
  honours:
    - {value: "Senator and count of the empire (Napoleon)", kind: "other", certainty: 0.7, cites: [{source: S1, locator: "para. 7"}], how_known: "Britannica; year not given."}
  definition_fit: {value: "clearly meets", rationale: "Mécanique analytique the basis for all later work (S1).", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}], how_known: "Britannica."}

childhood:
  family_religion: {value: "Roman Catholic", certainty: 0.5, cites: [{source: S3, locator: "Early years (raised Roman Catholic; Kline quote)"}, {source: S7, locator: "baptised Giuseppe Lodovico Lagrangia"}], how_known: "Wikipedia cites Kline for Catholic parentage/raised Catholic; MacTutor baptism in Turin. Heritage only (P50 dual bio)."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated beyond baptism/raised Catholic."}
  parents_and_household:
    - {value: "Father treasurer to the king of Sardinia, who lost his fortune in speculation", role: "father", certainty: 0.7, cites: [{source: S1, locator: "para. 2"}], how_known: "Britannica."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling: []
  early_mathematics: {value: UNKNOWN, how_known: "Not stated in S1; MacTutor has more (unread for a full childhood fill this pass)."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated (Italian birth; French later work)."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1764–1788", certainty: 0.5, cites: [{source: S1, locator: "para. 3"}, {source: S1, locator: "Introduction"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: "Least action is not a metaphysical principle but a simple general result of the laws of Mechanics; he kept clear of cult discussions (reported)", certainty: 0.5, cites: [{source: S4, locator: "p. 246"}, {source: S5, locator: "étranger à toute discussion sur le culte"}], how_known: "Own MA profession (S4) at 0.7 ceiling but paired with Delambre reported speech on culte reserve → overall 0.5 for the combined relation claim."}
  primary_system: {value: UNKNOWN, how_known: "No first-person system affiliation. Kline 'agnostic', Marechal Dictionnaire des Athées listing, and Mass attendance are secondary or reported (S3, S6); AGNOS remains a lead only, not a code (P19)."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: AGNOS, reason: "Rejected as coded primary: Kline (via Wikipedia) and Marechal (via Boissonnade translators' bio) are secondary reconstructions; no first-person suspension of judgement about God. Mass attendance and Napoleon-at-Mass cuts against a scored atheist/agnostic code from those leads alone. Heritage Catholic ≠ adult AGNOS.", cites: [{source: S3, locator: "Early years (Kline p. 214)"}, {source: S6, locator: "Marechal / Mass regularly / agnosticism better than atheism"}]}
    - {code: ATHE, reason: "Rejected: Marechal listed him among 'atheists' but Boissonnade/Vagliente note agnosticism would be more accurate; Delambre reports reserve about culte, not denial of God; no own-words denial.", cites: [{source: S6, locator: "Marechal Dictionnaire des Athées passage"}]}
    - {code: CHRIST, reason: "Rejected: Catholic baptism/raised Catholic is heritage only. Regular Mass (translators' bio) is practice report, not an adult Christ-locus profession.", cites: [{source: S3, locator: "Early years"}, {source: S6, locator: "attended Mass regularly"}]}
  lio_axes:
    A_locus: {value: UNKNOWN, how_known: "P19 researched silent on locus. S4 (MA) places least action in mechanical laws, not God; S5 deathbed 'la mort n'est que le repos absolu du corps' is about bodily functions, not where God is; S5 'étranger à toute discussion sur le culte' is reserve about cult talk, not a locus. Secondary AGNOS/ATHE leads (S3, S6) unused for A. Named alternative: BELOW_THRESHOLD if a first-person suspension letter or a stronger scholarly monograph on adult belief is later treated as AGNOS under P20.", note: "Blockers: full Boissonnade & Vagliente Analytical Mechanics translators' preface (PDF was 403); Fraser monograph; family letters; any own-words God/locus statement."}
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.5
      support: corroborated
      cites: [{source: S4, locator: "p. 246 (2nd ed. 1811): 'je regarde non comme un principe métaphysique, mais comme un résultat simple et général des lois de la Mécanique'"}, {source: S1, locator: "para. 4–5 (analytic/celestial mechanics; solar-system stability)"}]
      how_known: "Own published Mécanique analytique (1788/1811), within working years; IA OCR of 1811 ed. read at the Delambre-cited page. Second stream: Britannica documents lasting mechanics program (P48 corroborated). Certainty 0.5 because P40 is not met (alt 4)."
      rationale: "Scientist under P30 (Lagrange equations; Mécanique analytique; celestial mechanics). MA § on least action: he regards the principle 'non comme un principe métaphysique, mais comme un résultat simple et général des lois de la Mécanique' — an explicit nature-order / lawful-mechanics remark (P16), rejecting Maupertuis-style metaphysical framing. No statement that rules out exceptions or miracles for all of nature (P40). Per P16 addendum / P35 logic: lawful remark without no-exception → B 3 @ 0.5, alternative 4, never 4."
      alternatives:
        - {value: 4, note: "No stated exceptionless / no-miracle claim (P40); MA demotes least action from metaphysics to a corollary of mechanical laws without claiming nature admits no exceptions.", cites: [{source: S4, locator: "p. 246"}]}
    C_ledger: {value: UNKNOWN, how_known: "Deathbed 'repos absolu du corps' (S5, reported) is physiological, not a reward/punishment or afterlife ledger (P19)."}
    D_authority: {value: UNKNOWN, how_known: "Nothing scored on revelation versus observation (P19). Metaphysics-rejection in MA is about least-action framing, not scripture."}
    E_scope: {value: BELOW_THRESHOLD, note: "Working science and MA's 'lois de la Mécanique' bear on E's first question but E is not scored from them alone without the in-group-exception question (P19).", how_known: "BELOW_THRESHOLD under P19."}
  mid_basin: {value: UNKNOWN, how_known: "A_locus is UNKNOWN, which takes precedence (§6, P19)."}
  statements:
    - text: "Tel est le principe auquel je donne ici, quoiqu'improprement, le nom de moindre action, et que je regarde non comme un principe métaphysique, mais comme un résultat simple et général des lois de la Mécanique."
      cites: [{source: S4, locator: "Mécanique analytique, 2nd ed. 1811, p. 246 (IA OCR); Delambre cites also 1st ed. p. 189"}]
      date: "1788"
      context: "Seconde Partie, opening discussion of the fourth principle (least action), rejecting Maupertuis-style metaphysical status in favour of a corollary of mechanical laws. Date: first edition 1788; wording verified in 1811 second edition OCR at the page Delambre names."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "archive scan (OCR only)"
      verified_on: 2026-10-24
      note: "IA djvu.txt of mcaniqueanalyt01lagr (1811). OCR hyphenates métaphysique/improprement; wording matches Delambre 1816 paraphrase and modern scholarly quotations (Images des mathématiques; Magnenet 2004)."
    - text: "…moi je restais étranger à toute discussion sur le culte, et ne contrariais les opinions de personne."
      cites: [{source: S5, locator: "Notice: Frederick preferred him to Euler who was 'un peu dévot'"}]
      date: "1816"
      context: "Delambre reports Lagrange's own account of why Frederick preferred him to the more devout Euler. Reserve about cult discussion; not coded as locus."
      axes: []
      kind: "reported speech"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "FR Wikisource of Œuvres de Lagrange, Notice sur la vie et les ouvrages. Used for science–religion reserve, not A."
    - text: "la mort n'est que le repos absolu du corps."
      cites: [{source: S5, locator: "deathbed conversation near end of Notice"}]
      date: "1813-04"
      context: "Delambre reports Lagrange's deathbed physiological account of dying (functions failing everywhere). Not a locus or afterlife ledger claim."
      axes: []
      kind: "reported speech"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Unused for A/C; kept as the create-record open lead now checked."
  changes_over_life: []
  coder_notes: "Deepen D1: A stays UNKNOWN (no locus). B stays 3 @ 0.5 with basis upgraded inference_from_work → written_profession (MA p. 246), support corroborated (S4+S1), alt 4. P40 not applied. Secondary AGNOS (Kline/Marechal) and Mass attendance are heritage/leads only. Antommarchi Napoleon anecdote that God appears endlessly in Lagrange is false (S6 / Conifold); Laplace 'je n'ai pas eu besoin de cette hypothèse' stays misattribution, unused. Chart still unplotted (A UNKNOWN; B faded)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Italian (Turin / Piedmont); later naturalized French", certainty: 0.7, cites: [{source: S1, locator: "Introduction"}, {source: S3, locator: "infobox / Early years"}], how_known: "Britannica and Wikipedia."}
  religious_heritage_by_birth: {value: "Roman Catholic", certainty: 0.5, cites: [{source: S3, locator: "Early years (raised as a Roman Catholic; Kline)"}, {source: S7, locator: "baptised Giuseppe Lodovico Lagrangia"}], how_known: "Wikipedia + MacTutor baptism; Kline via Wikipedia. Heritage only."}
  baptism_or_initiation: {value: "Baptised Giuseppe Lodovico Lagrangia (Turin)", certainty: 0.5, cites: [{source: S7, locator: "opening biography"}], how_known: "MacTutor."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1764–1788", certainty: 0.5, cites: [{source: S1, locator: "para. 3"}, {source: S1, locator: "Introduction"}], how_known: "From the libration essay (1764) to Mécanique analytique (1788), the listed lasting works (P29, P30 #1); start at 0.5."}
  age_at_first_lasting_contribution: {value: 28, certainty: 0.5, cites: [{source: S1, locator: "Introduction; para. 3"}], how_known: "1764 − 1736 = 28 (P30 year difference); younger on an earlier alternative."}
  first_evidence_of_lio_type_views: {value: "1788: Mécanique analytique — least action as result of mechanical laws, not metaphysics", year: 1788, certainty: 0.7, cites: [{source: S4, locator: "p. 246 (2nd ed.; wording in 1st ed. per Delambre p. 189)"}], how_known: "LIO-type nature-order remark (P27) in own published words at the close of the listed major-work span."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.7, cites: [{source: S4, locator: "p. 246"}, {source: S1, locator: "Introduction"}], how_known: "Mécanique analytique 1788 is the span end; the least-action profession is inside it."}
  worldview_during_major_work: {value: "A UNKNOWN; B 3 @ 0.5 from MA least-action profession (written_profession) plus working analytic/celestial mechanics; secondary AGNOS lead unused", certainty: 0.5, cites: [{source: S4, locator: "p. 246"}, {source: S1, locator: "para. 4–5"}], how_known: "Synthesis of D1 primaries; not a stronger code."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "'one cannot find any figures in this work' (S1): analytic, not geometric.", certainty: 0.5, cites: [{source: S1, locator: "para. 5"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable (analytic form)."}
  circle_present: {value: "unclear", rationale: "MA rejects metaphysical framing of least action; no God–Nature identity statement read.", certainty: 0.5, cites: [{source: S4, locator: "p. 246"}], how_known: "Coder's reading."}
  reading: "As belief, not finding: analytic (not geometric) form; circle unclear. Worldview still unplottable (A UNKNOWN; B faded). The record does not test H1."
  notes: ""

institutions:
  - {value: "Prussian Academy of Sciences, Berlin", role: "director of mathematics (post vacated by Euler)", years: "1766–1787", kind: "academy or learned society", certainty: 0.7, cites: [{source: S1, locator: "para. 3–4"}], how_known: "Britannica."}
  - {value: "École Polytechnique", role: "professor of mathematics", years: "1794", kind: "university", certainty: 0.5, cites: [{source: S1, locator: "para. 6"}], how_known: "Britannica: from its opening in 1794; end year not given."}
collaborators:
  - {value: "Leonhard Euler", relation: "correspondent", note: "praised his theory of variations; recommended him to Berlin", certainty: 0.5, cites: [{source: S1, locator: "para. 2–3"}], how_known: "Britannica; correspondence not stated as such."}
  - {value: "Gaspard Monge", relation: "collaborator", note: "fellow leading professor at the École Polytechnique", certainty: 0.7, cites: [{source: S1, locator: "para. 6"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 195"}], how_known: "Study roster."}
  controversies:
    - {value: "Antommarchi / Napoleon anecdote that 'the name of God appeared endlessly' in Lagrange's works is contradicted by Analytical Mechanics (no God) and by the translators' bio; often paired with the Laplace 'hypothesis' anecdote, which belongs to Laplace not Lagrange.", certainty: 0.5, cites: [{source: S6, locator: "Conifold answer quoting Boissonnade & Vagliente"}], how_known: "HSM secondary path into translators' preface."}
  data_quality_flags:
    - "Boissonnade & Vagliente Analytical Mechanics translators' biographical preface not read as a file (PDF 403); used via HSM/Conifold quotation (S6)."
    - "Mécanique analytique least-action sentence verified in IA OCR of 1811 ed.; print page-image check pending."
    - "Kline 1986 p. 214 'agnostics' not opened as a monograph this pass (cited via Wikipedia)."
  open_questions:
    - "Read full Boissonnade & Vagliente (1997) translators' preface and any Fraser monograph on Lagrange's religious views."
    - "Family letters for consolation language or God-talk (Boissonnade notes none even at deaths)."
    - "Any first-person locus or no-exception claim that would score A or apply P40 to B."
    - "Print facsimile check of MA 1788 p. 189 / 1811 p. 246."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Dirk Jan Struik"
    citation: "Struik, Dirk Jan. 'Joseph-Louis Lagrange, comte de l'Empire.' Encyclopaedia Britannica (scholars edition). https://kids.britannica.com/scholars/article/Joseph-Louis-Lagrange-comte-de-lEmpire/46837"
    url: "https://kids.britannica.com/scholars/article/Joseph-Louis-Lagrange-comte-de-lEmpire/46837"
    accessed: 2026-10-19
    reliability_note: "Signed article, read in full at create; reused for working-science corroboration of B."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, timing, institutions, collaborators]
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
    year: 2026
    citation: "Wikipedia. \"Joseph-Louis Lagrange.\" English Wikipedia. Dual-bio check (P50). Early years: raised Roman Catholic; Kline 1986 p. 214 'Lagrange and Laplace, though of Catholic parentage, were agnostics.'"
    url: "https://en.wikipedia.org/wiki/Joseph-Louis_Lagrange"
    accessed: 2026-10-24
    reliability_note: "Unsigned encyclopedia; used for heritage leads and to locate Kline; not for scoring A."
    source_quality: "reference entry"
    used_for: [identity, childhood, worldview, heritage]
  - id: S4
    type: primary
    kind: "published work by the subject"
    author: "Joseph-Louis Lagrange"
    year: 1811
    citation: "Lagrange, Joseph-Louis. Mécanique analytique. 2nd ed. Paris, 1811. Internet Archive identifier mcaniqueanalyt01lagr (djvu.txt OCR). Least-action profession at p. 246 (Delambre also cites 1st ed. 1788 p. 189)."
    url: "https://archive.org/details/mcaniqueanalyt01lagr"
    accessed: 2026-10-24
    reliability_note: "Primary treatise; OCR of 1811 printing; hyphenation cleaned against Delambre and modern scholarly quotations."
    source_quality: "archive scan (OCR only)"
    used_for: [contribution, worldview, timing, lane_b]
  - id: S5
    type: secondary
    kind: "scholarly edition"
    author: "Jean-Baptiste Joseph Delambre"
    year: 1816
    citation: "Delambre, Jean-Baptiste Joseph. \"Notice sur la vie et les ouvrages de M. le Comte J. L. Lagrange.\" In Œuvres de Lagrange. FR Wikisource transcription."
    url: "https://fr.wikisource.org/wiki/%C5%92uvres_de_Lagrange/Notice_sur_la_vie_et_les_ouvrages_de_Lagrange"
    accessed: 2026-10-24
    reliability_note: "Contemporary éloge; reports Lagrange's words on culte reserve and deathbed; points to MA p. 246 / 189 for least-action reading."
    source_quality: "scholarly edition or monograph"
    used_for: [worldview]
  - id: S6
    type: secondary
    kind: "scholarly book"
    author: "Augustine Boissonnade and Victor N. Vagliente (translators); quoted via Conifold on HSM"
    year: 1997
    citation: "Boissonnade, Augustine, and Victor N. Vagliente, trans. Analytical Mechanics (English of Lagrange's Mécanique analytique), translators' biographical remarks. Quoted at length in Conifold, answer to 'Does the word \"God\" appear regularly in the works of Joseph Lagrange?', History of Science and Mathematics Stack Exchange (2020). Covers: no God in AM; Mass regularly / Napoleon-at-Mass; Marechal Dictionnaire des Athées; agnosticism more accurate than atheism; no Maupertuis deity; science/religion reconciliation 'inappropriate'."
    url: "https://hsm.stackexchange.com/questions/11524/does-the-word-god-appear-regularly-in-the-works-of-joseph-lagrange"
    accessed: 2026-10-24
    reliability_note: "Secondary path: translators' preface not opened as a file (PDF 403); HSM quotation used for leads and the Antommarchi controversy flag only, not for scoring A or B."
    source_quality: "unofficial web copy"
    used_for: [worldview, review]
  - id: S7
    type: secondary
    kind: "encyclopedia"
    author: "J. J. O'Connor and E. F. Robertson"
    year: 1999
    citation: "O'Connor, J. J., and E. F. Robertson. \"Joseph-Louis Lagrange.\" MacTutor History of Mathematics, University of St Andrews. Baptism name Giuseppe Lodovico Lagrangia."
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Lagrange/"
    accessed: 2026-10-24
    reliability_note: "Signed biography; used for baptism/heritage."
    source_quality: "reference entry"
    used_for: [identity, childhood, heritage]
---

## Summary

Joseph-Louis Lagrange (1736–1813), mathematician [S1]. Deepen D1: A UNKNOWN (no locus); B 3 at 0.5 written_profession from Mécanique analytique least-action remark (alternative 4; P16/P35/P40); mid_basin UNKNOWN. Chart still unplotted.

## Life and work

Turin; Berlin (Prussian Academy); Paris (École Polytechnique; senator/count under Napoleon) [S1].

## Contribution and impact

Lagrange's equations (1764); algebraic resolution memoir (1770); Mécanique analytique (1788), basis for later analytic mechanics [S1, S4].

## Childhood and education

Turin; baptised Giuseppe Lodovico Lagrangia; raised Roman Catholic (heritage) [S3, S7]. Father lost fortune in speculation [S1].

## Adult working worldview

**Lane A.** No citable own-words placing or denying of God. Secondary AGNOS (Kline via Wikipedia; Marechal via Boissonnade/Vagliente) unused for a code [S3, S6]. Delambre reports reserve about cult discussion and a physiological deathbed remark, not a locus [S5]. Mass attendance is practice report, not Christ-locus [S6]. A UNKNOWN; primary_system UNKNOWN.

**Lane B (separate).** Mécanique analytique: least action regarded "non comme un principe métaphysique, mais comme un résultat simple et général des lois de la Mécanique" [S4]. Lawful nature-order remark without no-exception (P40 not met) → B 3 @ 0.5, alt 4. Corroborated by Britannica's lasting mechanics program [S1].

## Heritage (context only)

Italian (Turin); Roman Catholic by birth/baptism [S3, S7]. Never a worldview code.

## Timing

First lasting contribution 1764, at 28 (0.5) [S1]. MA 1788 least-action profession is an LIO-type nature-order remark during major work [S4].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Analytic (not geometric) form [S1]; circle unclear. H1 not tested.

## Open questions

- Full Boissonnade & Vagliente translators' preface; Fraser or other monograph on religious views.
- Family letters; any first-person locus or no-exception claim.
- Print facsimile of MA 1788/1811 least-action page.

## Research log

- 2026-10-19: Read Britannica (Struik).
- 2026-10-24: Deepen D1 — MA 1811 IA OCR (S4); Delambre Notice Wikisource (S5); Wikipedia EN (S3); HSM/Conifold → Boissonnade & Vagliente (S6); MacTutor baptism (S7). No fallacy_catalog. No figures/.
