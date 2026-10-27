---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 4
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AB1; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to medieval. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #214/228, F 3, rank 227). Opened Ordinatio Prologue (Peter L.P. Simpson EN, aristotelophile PDF) nn.11, 60, 70, 77 (mediate→immediate efficient cause; absolute power separability; intuitive knowledge conserved of non-existent; theological truths including 'God is'); Kilcullen PhTh documenting Quodl. 6 q.1 ordinate/absolute and the famous proposition (secondary causes → God can produce immediately); IEP Kaye (divine command; fideism); Wikipedia EN dual bio (P50). Lifted CLASS_THEISM, A 1, B 3 from scholarly_reconstruction @0.5 to written_profession @0.7 (alts kept: A alt 0; B alt 2). P48 support corroborated on A and B. mid_basin BELOW_THRESHOLD → true @0.7. Chart-moving YES (would-be faded hollow → dark filled at next figures refresh; mid newly true). RQ-AA8-1 B 3 value kept; basis lifted off reconstruction by own-voice (Scotus pattern). P47 source_quality; P49 not silently raised. No fallacy_catalog; no figures/. Draft, not reviewed."}
    - {date: 2026-10-21, by: "Grok Bot", summary: "RQ-AA8-1 resolved yes by Jason (2026-10-21, P49): B 3 at 0.5 from SEP's reconstruction (basis scholarly_reconstruction), alternative 2. Newly plottable (A 1 / B 3, both 0.5); mid_basin BELOW_THRESHOLD."}
    - {date: 2026-10-20, by: "Grok Bot", summary: "AB1 audit note: A 1 now rests on §6.2/§7.2; B stays UNKNOWN, held with Plotinus and Duns Scotus under RQ-AA8-1 pending Jason."}
    - {date: 2026-10-20, by: "Grok Bot", summary: "Record created (stage 3 batch AB1, order P32: F 3, rank 227). Source: SEP 'William of Ockham' (Spade, Panaccio and Pelletier, 2024, read in full). Lasting: metaphysical nominalism, for which he is 'probably best known today', and 'Ockham's Razor', 'named after him' (S1). Dated by the academic writings, begun with the Sentences commentary (1317–18) and largely finished by about 1325 (S1): composition range 1317–1325 at 0.5 (RQ-Z9-N1), age 30 (born c. 1287). Worldview: Franciscan friar and theologian; CLASS_THEISM at 0.5 (scholarly_reconstruction; Duns Scotus precedent); A 1 at 0.5 (God's power can override natural causes; divine command ethics; S1). B: S1 §5–6 sets out his natural philosophy (natural causes act 'in the natural order and in the absence of divine intervention'; God 'can always' neutralize a natural effect), but that is a scholar's reconstruction for a non-scientist, so B stays UNKNOWN pending RQ-AA8-1 (Jason undecided). Note for Jason: the Duns Scotus record already carries a reconstruction-based B 3 (0.5). Not plotted. Draft, not reviewed."}

identity:
  id: william-of-ockham
  display_name: "William of Ockham"
  roster:
    canonical_name: "William of Ockham"
    rank: 227
    F: 3
    models: [Claude, DeepSeek, Grok]
    band: "core (3–4)"
    status: "core"
    field: "philosophy"
    field_bucket: "philosophy"
  full_name: {value: "William of Ockham", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "lead"}], how_known: "SEP and Wikipedia agree."}
  native_name: {value: "Guillelmus de Ockham", certainty: 0.5, cites: [{source: S5, locator: "lead / Latin form"}], how_known: "Standard Latin form used in critical editions and Wikipedia; SEP does not print it. 0.5."}
  aliases:
    - {name: "Occam", kind: "transliteration"}
    - {name: "William Ockham", kind: "roster alias"}
    - {name: "Venerable Inceptor", kind: "title or honorific"}
    - {name: "Doctor Invincibilis", kind: "title or honorific"}

basics:
  birth:
    date: {value: "1287", certainty: 0.5, cites: [{source: S1, locator: "opening; §1.1"}, {source: S5, locator: "infobox"}], how_known: "SEP and Wikipedia: c. 1287. IEP (S4) gives 1280–85 from the 1306 ordination; dual-bio range kept at 0.5 (P50)."}
    place: {value: "Ockham, Surrey", modern_name: "Ockham, Surrey, United Kingdom", polity_then: "Kingdom of England", certainty: 0.7, cites: [{source: S1, locator: "§1.1"}, {source: S5, locator: "infobox"}], how_known: "SEP and Wikipedia agree on Ockham, Surrey."}
  death:
    date: {value: "1347-04-10", calendar: julian, certainty: 0.7, cites: [{source: S1, locator: "§1.3"}, {source: S5, locator: "infobox"}], how_known: "SEP: 'on the night of April 9/10, 1347'; Wikipedia 9/10 April 1347. Coded as 1347-04-10 (end of night); alternative 1347-04-09. IEP (S4) death range 1347–49 is the outlier."}
    place: {value: "Munich", modern_name: "Munich, Germany", polity_then: "Holy Roman Empire (Duchy of Bavaria)", certainty: 0.7, cites: [{source: S1, locator: "§1.3"}, {source: S5, locator: "infobox"}], how_known: "SEP and Wikipedia agree on Munich."}
  first_lasting_contribution_year: {value: 1317, certainty: 0.5, cites: [{source: S1, locator: "§2. Writings"}], how_known: "Commentary on the Sentences (1317–18), the first of the academic writings where his nominalism is set out (S1); composition range start (RQ-Z9-N1); 0.5."}
  era_bucket: {value: "500 to 1399", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "infobox"}], how_known: "1317, and every year of his life, falls in 500 to 1399 (P2). Two independent sources."}
  region_of_birth: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "§1.1"}, {source: S5, locator: "infobox"}], how_known: "England (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 0.7, cites: [{source: S1, locator: "§1.1; §2"}], how_known: "Oxford and London, where the academic writings were done (AA6 rule); alternatives Western Europe (Avignon, Munich)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Latin"], certainty: 0.7, cites: [{source: S1, locator: "notes"}, {source: S3, locator: "title page"}], how_known: "Latin works; English translations used for deepen."}
  occupations: {value: ["Franciscan friar", "philosopher", "theologian"], certainty: 0.7, cites: [{source: S1, locator: "opening; §1.1"}, {source: S5, locator: "lead"}], how_known: "SEP and Wikipedia."}

contribution:
  era_bucket: medieval
  fields: {value: ["philosophy", "logic", "theology", "political philosophy"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}
  lasting_original_contributions:
    - {value: "Metaphysical nominalism and ontological reduction to substance and quality (academic writings, Sentences commentary to Summa of Logic)", year: 1317, kind: "theory", lasting: "'He is probably best known today for his espousal of metaphysical nominalism' (S1)", certainty: 0.5, cites: [{source: S1, locator: "opening; §2; §4.2–4.3"}], how_known: "Academic writings 1317–c.1325 (S1); composition range start (RQ-Z9-N1)."}
    - {value: "Ockham's Razor (methodological principle of parsimony)", year: UNKNOWN, kind: "law or principle", lasting: "'the principle known as \"Ockham's Razor\" is named after him' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening; §4.1"}], how_known: "S1 does not date his fullest formulation."}
  evidence_of_impact:
    - {value: "Ockham's Razor", kind: "named after them", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}
    - {value: "Among the most prominent Late Medieval philosophers with Aquinas and Scotus", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "lead"}], how_known: "SEP and Wikipedia."}
  major_works:
    - {value: "Ordinatio (Commentary on the Sentences)", year: 1318, kind: "book", certainty: 0.5, cites: [{source: S1, locator: "§2"}, {source: S3, locator: "title"}], how_known: "SEP: begun 1317–18; Prologue translation read this pass."}
    - {value: "Summa of Logic", year: 1323, kind: "book", certainty: 0.5, cites: [{source: S1, locator: "§2"}], how_known: "SEP: 'c. 1323–25'."}
    - {value: "Seven Quodlibets", year: 1322, kind: "book", certainty: 0.5, cites: [{source: S1, locator: "§2"}, {source: S6, locator: "Qdl.6 q.1 cites"}], how_known: "SEP: London disputations 1322–24, revised 1324–25; Quodl. 6 q.1 documented in S6."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Among the most prominent late-medieval philosophers (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household:
    - {value: "Given to the Franciscan Order as an oblate between ages seven and thirteen", role: "other", certainty: 0.7, cites: [{source: S1, locator: "§1.1"}], how_known: "SEP."}
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling:
    - {value: "London Greyfriars; theology from about 1310; Oxford by 1318–19", certainty: 0.7, cites: [{source: S1, locator: "§1.1"}, {source: S5, locator: "Education"}], how_known: "SEP and Wikipedia."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1317–1325", certainty: 0.5, cites: [{source: S1, locator: "§2"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Franciscan (Order of Friars Minor); Roman Catholic", years: "–1347", role: "friar; Venerable Inceptor (theology inceptor, not completed master)", certainty: 0.7, cites: [{source: S1, locator: "§1.1"}, {source: S5, locator: "lead"}], how_known: "SEP and Wikipedia."}
  self_described_science_religion_relation:
    value: "Some truths naturally known or knowable are theological (that God is, is wise, good); others are supernaturally knowable (Trinity, Incarnation). Theology is not a demonstrative science for the wayfarer; belief in God is largely a matter of faith (fideism, S4), while natural philosophy proceeds by experience under the ordained order."
    certainty: 0.7
    cites: [{source: S3, locator: "Ordinatio Prologue n.11"}, {source: S4, locator: "§6.a Fideism"}, {source: S1, locator: "§6; §7"}]
    how_known: "Own Ordinatio Prologue plus IEP/SEP. Written profession, 0.7."
  primary_system:
    value: CLASS_THEISM
    basis: written_profession
    certainty: 0.7
    cites: [{source: S3, locator: "Ordinatio Prologue nn.11, 70, 77"}, {source: S1, locator: "§1.1; §4.4; §6.2; §7.2"}, {source: S4, locator: "§6–7"}]
    how_known: "His own Ordinatio Prologue (translated teaching work) plus SEP and IEP. Written profession ceiling 1.0; held at 0.7 because he is not the namesake founder of the coded tradition (Aquinas is), CHRIST remains a considered broader label, and his fideism / voluntarism is contested."
    rationale: "Franciscan theologian whose metaphysics, epistemology and ethics turn on a personal God's power and decrees within Catholic theology: CLASS_THEISM, as for Scotus and Aquinas. Divine command ethics and absolute/ordinate power are classical-theist apparatus, not a separate code. Classical Theism label already split historically — keep CLASS_THEISM as coded."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CLASS_THEISM, reason: "Coded. Own-voice personal God ('God is', Prologue n.11); nature ordered through secondary causes with a stated absolute-power exception (Prologue n.70; Quodl. 6 q.1 via S6); divine command ethics (S1, S4).", cites: [{source: S3, locator: "Ordinatio Prologue nn.11, 70"}, {source: S1, locator: "§4.4; §6.2; §7.2"}]}
    - {code: CHRIST, reason: "Rejected as primary. He was a Franciscan friar whose theology serves the Catholic faith, but CLASS_THEISM is the closer system (as Aquinas/Scotus); the coding guide reserves CHRIST when neither theism split fits better.", cites: [{source: S1, locator: "§1.1"}]}
    - {code: CLTHEI, reason: "Rejected. Absolute power can produce without secondary causes and can neutralize natural effects, but the ordinary course is the ordained natural order ('in the natural order and in the absence of divine intervention', S1 §4.4); miracles are special dispensation within ordinances, not the ordinary course (S6).", cites: [{source: S1, locator: "§4.4; §6.2"}, {source: S6, locator: "Qdl.6 q.1"}]}
  lio_axes:
    A_locus:
      value: 1
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S3, locator: "Ordinatio Prologue nn.11, 70, 77"}, {source: S1, locator: "§6.2; §7.2"}, {source: S4, locator: "§7.a Divine Command Theory"}]
      how_known: "Ordinatio Prologue in Simpson translation (own teaching work) plus SEP and IEP. Written profession; certainty 0.7 because the record names a plausible alternative score (CODING_GUIDE §3). P48: corroborated (S3+S1+S4)."
      rationale: "Leans to the transcendent-person pole. Own-voice: 'some truths naturally known or knowable are theological, as that God is, God is wise, good, etc.' (Ord. Prol. n.11); God of absolute power can act immediately without mediate efficient causes (n.70) and separate absolute things (n.77). SEP: God can 'neutralize the natural causal effect', 'something He can always do' (§6.2); 'certain intentions, become morally obligatory ... simply because God decrees so' (§7.2). IEP: divine command theorist. A personal God outside the world who acts in it: A 1, as CLASS_THEISM. Alternative 0 if strong voluntarism is read as making God wholly outside ordinary personhood."
      alternatives:
        - {value: 0, note: "Strong voluntarism / divine command read as a God wholly outside the world, if decree-based ethics collapses worldly person-talk.", cites: [{source: S1, locator: "§7.2"}, {source: S4, locator: "§7.a"}]}
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.7
      support: corroborated
      cites: [{source: S3, locator: "Ordinatio Prologue nn.60, 70, 77"}, {source: S1, locator: "§4.4; §6.2"}, {source: S6, locator: "Qdl.6 q.1; famous proposition Qdl.6 q.6"}]
      how_known: "Ordinatio Prologue (Simpson) plus SEP plus Kilcullen documenting Quodl. 6. Account of nature (P6). Written profession; certainty 0.7 because the record names a plausible alternative score (CODING_GUIDE §3). RQ-AA8-1 had set B 3 from scholarly_reconstruction @0.5; own-voice now lifts basis (Scotus pattern), value kept. P48: corroborated (S3+S1+S6)."
      rationale: "Scored on his account of nature (P6). Ordinary natural causal order with a stated, limited divine exception — B 3 (Duns Scotus pattern). Own-voice: 'whatever God can do through a mediate efficient cause he can do immediately' (Ord. Prol. n.70); 'every absolute thing ... can, by divine absolute power, exist without it' (n.77); intuitive knowledge 'by divine power, conserved about a non-existent thing' (n.60). SEP: essential parts unite 'In the natural order and in the absence of divine intervention' (§4.4); God can 'neutralize the natural causal effect' (§6.2). Quodl. 6 q.1 (via S6): one power ad extra, distinguished as ordinate (according to laws ordained) vs absolute (everything non-contradictory); famous proposition that whatever God produces by secondary causes he can produce immediately without them. Miracles are special dispensation within ordinances, not the ordinary course. Alternative 2 if absolute power / strong voluntarism is read as reaching ordinarily into nature."
      alternatives:
        - {value: 2, note: "Absolute power read as unlimited/ordinary override of natural order; strong voluntarism.", cites: [{source: S1, locator: "§6.2"}, {source: S3, locator: "Ordinatio Prologue n.70"}]}
    C_ledger: {value: UNKNOWN, how_known: "Not scored this pass (soul, afterlife, Eucharist loci not opened as a full axis)."}
    D_authority: {value: UNKNOWN, how_known: "Prologue on theological vs natural knowability read in outline; fideism noted under self_described; not scored as a full axis this pass."}
    E_scope: {value: UNKNOWN, how_known: "Not read."}
  mid_basin:
    value: true
    certainty: 0.7
    cites: [{source: S3, locator: "Ordinatio Prologue nn.11, 60, 70, 77"}, {source: S1, locator: "§4.4; §6.2; §7.2"}, {source: S6, locator: "Qdl.6 q.1"}]
    how_known: "P4 test as amended by P6: A_locus = 1 at 0.7 and B_cause = 3 at 0.7, B scored on his account of nature. Both at certainty >= 0.7, so true. Certainty 0.7: mid_basin is no surer than the less certain of A and B (CODING_GUIDE §3). F = 3, so first-rank is met."
  statements:
    - text: "some truths naturally known or knowable are theological, as that God is, God is wise, good, etc., since these are necessary for salvation; and some are supernaturally knowable, such as: God is three, incarnate, and the like."
      cites: [{source: S3, locator: "Ordinatio Prologue n.11"}]
      context: "Ordinatio Prologue, Question 1: what counts as a theological truth for the wayfarer."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "Translated wording (Simpson). Unofficial web copy of the translation PDF; cannot alone support certainty 1.0 (CODING_GUIDE §7)."
    - text: "whatever God can do through a mediate efficient cause he can do immediately"
      cites: [{source: S3, locator: "Ordinatio Prologue n.70"}]
      context: "Against Scotus on intuitive knowledge: if the existent object is only an efficient cause of the vision, God can produce the vision without it. Parallel to the 'famous proposition' on secondary causes (Quodl. 6 q.6, S6)."
      axes: [B_cause, A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
    - text: "every absolute thing, distinct in place and subject from another absolute thing, can, by divine absolute power, exist without it"
      cites: [{source: S3, locator: "Ordinatio Prologue n.77"}]
      context: "Corollary: intuitive knowledge of a non-existent thing is possible — vision of a star can remain when the star is destroyed."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
    - text: "if such perfect knowledge were, by divine power, conserved about a non-existent thing, it would by virtue of that non-propositional knowledge know evidently that the thing was not."
      cites: [{source: S3, locator: "Ordinatio Prologue n.60"}]
      context: "Definition of intuitive vs abstractive knowledge; divine conservation of intuitive cognition without the object."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
    - text: "In the natural order and in the absence of divine intervention, the essential parts of a material substance under particular conditions have an intrinsic disposition to unite in such a way that they form that one single material substance."
      cites: [{source: S1, locator: "§4.4"}]
      context: "SEP reconstruction of Ockham's account of material substance / natural order; corroborates the ordinary-course side of B 3."
      axes: [B_cause]
      kind: "other"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Scholar's wording (Spade/Panaccio/Pelletier), not Ockham's Latin; used as corroboration of the ordinary natural order, not alone for the score."
  changes_over_life: []
  coder_notes: "D1 2026-10-24: Ordinatio Prologue (Simpson) primary-checked for A/B; Quodl. 6 q.1/q.6 via Kilcullen PhTh secondary. Freddoso Quodlibetal Questions hard copy / critical Latin OTh IX not opened. C/D/E still UNKNOWN. RQ-AA8-1 value B 3 kept; basis lifted to written_profession by own-voice (unlike Plotinus, where B stayed reconstruction-labeled)."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "English", certainty: 0.7, cites: [{source: S1, locator: "§1.1"}, {source: S5, locator: "infobox"}], how_known: "SEP and Wikipedia: Ockham, Surrey, England."}
  religious_heritage_by_birth: {value: "Christian (Catholic)", certainty: 0.5, cites: [{source: S1, locator: "§1.1"}], how_known: "Oblate to the Franciscans as a child (S1); inferred."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated; ordination 1306 (S4) is adult initiation into orders, not childhood baptism."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1317–1325", certainty: 0.5, cites: [{source: S1, locator: "§2"}], how_known: "Academic writings from the Sentences commentary (1317–18) to the Summa of Logic (c. 1323–25) (P29, P30, RQ-Z9-N1); the Razor is undated. 0.5."}
  age_at_first_lasting_contribution: {value: 30, certainty: 0.5, cites: [{source: S1, locator: "opening; §2"}], how_known: "1317 − 1287 = 30 (P30 year difference); birth year 'c.'."}
  first_evidence_of_lio_type_views: {value: "1317", certainty: 0.7, cites: [{source: S3, locator: "Ordinatio Prologue"}, {source: S1, locator: "§2"}], how_known: "Ordinatio Prologue / Sentences commentary: personal God, mediate→immediate causation, absolute power."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.7, cites: [{source: S3, locator: "Ordinatio Prologue"}], how_known: "The scored views are in the major teaching work itself."}
  worldview_during_major_work: {value: "same as adult working worldview", certainty: 0.7, cites: [{source: S3, locator: "Ordinatio Prologue"}], how_known: "Adult working unit is the academic-writings span."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Logic, metaphysics, and theology (S1); no Euclidean-style geometric method scored.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No data beyond the ordered natural-philosophy / absolute-power structure."
  notes: ""

institutions:
  - {value: "Franciscan Order", role: "friar; Venerable Inceptor", years: "c.1294/1300–1347", kind: "religious body", certainty: 0.7, cites: [{source: S1, locator: "§1.1"}, {source: S5, locator: "lead"}], how_known: "SEP and Wikipedia."}
  - {value: "University of Oxford", role: "theology student / Sentences commentator", years: "c.1317–1324", kind: "university", certainty: 0.5, cites: [{source: S1, locator: "§1.1"}, {source: S5, locator: "Education"}], how_known: "SEP and Wikipedia; never completed the mastership."}
  - {value: "Court of Ludwig of Bavaria, Munich", role: "refugee and polemicist", years: "1328/29–1347", kind: "patron or funder", certainty: 0.7, cites: [{source: S1, locator: "§1.3"}, {source: S5, locator: "infobox"}], how_known: "SEP and Wikipedia."}
collaborators:
  - {value: "Michael of Cesena", relation: "collaborator", note: "Franciscan minister general; fled Avignon with him in 1328", certainty: 0.7, cites: [{source: S1, locator: "§1.3"}], how_known: "SEP."}
  - {value: "John Duns Scotus", relation: "rival or critic", note: "Ordinatio Prologue argues against Scotus on intuitive/abstractive knowledge; absolute-power apparatus shared in outline", certainty: 0.7, cites: [{source: S3, locator: "Ordinatio Prologue nn.65–70"}, {source: S1, locator: "opening"}], how_known: "Own Prologue; SEP."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 227"}], how_known: "Study roster."}
  controversies:
    - {value: "Birth and death years: SEP/Wikipedia c. 1287 – night of 9/10 April 1347; IEP 1280–85 to 1347–49 from ordination and Black Death dating.", certainty: 0.7, cites: [{source: S1, locator: "opening; §1.3"}, {source: S5, locator: "infobox"}, {source: S4, locator: "§1 Life and Works"}], how_known: "P50 dual-bio disagreement."}
  data_quality_flags:
    - "Ordinatio Prologue read in Simpson unofficial web PDF; Quodl. 6 via Kilcullen secondary documenting Freddoso QQ; critical Latin OTh I / OTh IX and Freddoso hard copy not opened this pass."
    - "RQ-AA8-1 B 3 value retained; basis lifted to written_profession by own-voice (not left reconstruction-labeled as Plotinus)."
  open_questions:
    - "Freddoso Quodlibetal Questions (Yale) and critical Latin for Ord. Prol. / Quodl. 6 q.1, q.6."
    - "Score C, D, E from Quodlibets and Reportatio on soul / authority / scope."
    - "Date of the Razor's fullest formulation."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Paul Vincent Spade; Claude Panaccio; Jenny Pelletier"
    citation: "Spade, Paul Vincent, Claude Panaccio, and Jenny Pelletier. 'William of Ockham.' Stanford Encyclopedia of Philosophy (substantive revision 11 September 2024). https://plato.stanford.edu/entries/ockham/"
    url: "https://plato.stanford.edu/entries/ockham/"
    accessed: 2026-10-24
    reliability_note: "Signed encyclopedia entry, re-read this pass for §4.4 / §6.2 / §7.2."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, institutions, collaborators, review]
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
    type: primary
    kind: "published work by the subject"
    author: "William of Ockham"
    year: 2021
    citation: "William of Ockham. The Ordinatio of the Venerable Inceptor, William of Ockham. Prologue. Translated by Peter L.P. Simpson. PDF at aristotelophile.com (Ockham_Prologue; translator dated October 2021, revision note November 2025). Sections read: nn.7–11, 60–79 (esp. nn.11, 60, 70, 77). https://www.aristotelophile.com/Books/Translations/Ockham%20Prologue.pdf"
    url: "https://www.aristotelophile.com/Books/Translations/Ockham%20Prologue.pdf"
    accessed: 2026-10-24
    reliability_note: "His own teaching work in a scholar's English translation. Unofficial web copy: under CODING_GUIDE §7 it cannot by itself support certainty 1.0; A/B held at 0.7 with named alternatives and SEP/Kilcullen corroboration."
    source_quality: "unofficial web copy"
    used_for: [contribution, worldview, timing, collaborators]
  - id: S4
    type: tertiary
    kind: "encyclopedia"
    author: "Sharon Kaye"
    citation: "Kaye, Sharon. 'William of Ockham (Occam, c. 1280—c. 1349).' Internet Encyclopedia of Philosophy. https://iep.utm.edu/ockham/. Read live 2026-10-24."
    url: "https://iep.utm.edu/ockham/"
    accessed: 2026-10-24
    reliability_note: "Signed IEP entry. Birth/death range differs from SEP/Wikipedia (P50). Used for fideism and divine-command corroboration of A; not alone for B."
    source_quality: "reference entry"
    used_for: [basics, worldview, review]
  - id: S5
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia contributors. 'William of Ockham.' Wikipedia, The Free Encyclopedia. https://en.wikipedia.org/wiki/William_of_Ockham. Read live 2026-10-24."
    url: "https://en.wikipedia.org/wiki/William_of_Ockham"
    accessed: 2026-10-24
    reliability_note: "P50 dual bio with SEP (S1): birth c. 1287, death 9/10 April 1347 Munich, and Ockham Surrey agree; IEP birth/death range is the outlier. Worldview scores do not rest on Wikipedia."
    source_quality: "reference entry"
    used_for: [identity, basics, heritage, institutions, review]
  - id: S6
    type: secondary
    kind: "book chapter"
    author: "John Kilcullen"
    year: 2019
    citation: "Kilcullen, John. 'Philosophy and Theology in William of Ockham' (PhTh PDF, Australian National University / Centre for Applied Philosophy and Public Ethics materials). Sections read: God's power and freedom — famous proposition (Qdl.6 q.6) and ordinate vs absolute power (Qdl.6 q.1, quoting Freddoso QQ pp.491–2)."
    url: "https://openresearch-repository.anu.edu.au/"
    accessed: 2026-10-24
    reliability_note: "Secondary documenting Quodlibet 6 primary loci with Freddoso English; not a substitute for Freddoso/OTh IX themselves. Used to corroborate B's absolute/ordinate and secondary-causes exception."
    source_quality: "scholarly edition or monograph"
    used_for: [contribution, worldview]
---

## Summary

William of Ockham (c. 1287–1347), Franciscan philosopher-theologian [S1; S5]. CLASS_THEISM (0.7, written_profession); A 1 and B 3 at 0.7, corroborated; mid_basin true. Would plot dark filled at next figures refresh.

## Life and work

Ockham, Surrey; London Greyfriars; Oxford; Avignon trial; Munich under Ludwig of Bavaria [S1, S5].

## Contribution and impact

Metaphysical nominalism; Ockham's Razor; Summa of Logic; Quodlibets; political writings against papal claims [S1].

## Childhood and education

Franciscan oblate; Greyfriars; Oxford theology [S1, S5].

## Adult working worldview

Classical theism: personal God; ordinary natural order under ordinate power; absolute power can produce immediately without secondary causes and conserve intuitive cognition of non-existents; divine command ethics; fideist about demonstrative theology [S3, S1, S4, S6].

## Heritage (context only)

English; Catholic (inferred from Franciscan oblation) [S1, S5].

## Timing

1317–1325 academic writings; LIO-type views in the Ordinatio Prologue itself [S3].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No geometric-form data.

## Open questions

- Freddoso Quodlibetal Questions / critical Latin OTh IX.
- Score C, D, E.
- Date of the Razor's fullest formulation.

## Research log

- 2026-10-24: Deepen D1. Ordinatio Prologue (Simpson aristotelophile); Kilcullen PhTh (Quodl. 6); IEP Kaye; Wikipedia EN dual bio; SEP re-read §4.4/§6.2/§7.2. Lifted CLASS_THEISM / A 1 / B 3 to written_profession @0.7, support corroborated; mid true. Chart-moving YES. No fallacy_catalog; figures not refreshed. Person-file-only commit.
- 2026-10-21: RQ-AA8-1 resolved yes by Jason (2026-10-21, P49): B 3 at 0.5 from SEP's reconstruction (basis scholarly_reconstruction), alternative 2. Newly plottable (A 1 / B 3, both 0.5); mid_basin BELOW_THRESHOLD.
- 2026-10-20: AB1 audit note: A 1 now rests on §6.2/§7.2; B stays UNKNOWN, held with Plotinus and Duns Scotus under RQ-AA8-1 pending Jason.
- 2026-10-20: Read SEP (Spade, Panaccio, Pelletier, 2024).
