---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 4
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch O)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-17
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to 20c_early. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-17, by: "Grok Bot", summary: "Record created (stage 3 batch O, order P32: F 4, rank 91). Basics from Britannica (Irving Kaplansky, signed; body only) and MacTutor (O'Connor and Robertson). Worldview from his Königsberg address 'Naturerkennen und Logik' (1930; Die Naturwissenschaften, pp. 959–963), read in a web transcription. Mathematician, not counted a scientist (P30). primary_system UNKNOWN; A UNKNOWN; B 3 (0.5, alt 4) from an explicit remark on nature ('überall die Einheit der Naturgesetze'); mid_basin UNKNOWN (P19). Not plotted. Draft, not reviewed."}
    - {date: 2026-10-17, by: "Grok Bot", summary: "Batch O audit fix (#23): S2 relabelled an unofficial web copy (cap 0.7; verified_against 'secondary quotation'), print check pending. v8's ruling on RQ O2 (on the auditor's advice): B 3 at 0.5, alternative 4, is allowed under P16 (recorded in OPEN_DECISIONS). Values unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #90, F4 rank 91). Needs: A UNKNOWN; B 3 @0.5 alt 4 (1930 Einheit der Naturgesetze); mathematician not scientist (P30). Dual bio: Britannica Kaplansky (S1) + Wikipedia EN (S5) (P50). P47 source_quality on S1–S8. A_locus UNKNOWN → BELOW_THRESHOLD: baptized/raised Calvinist Prussian Evangelical / Reformed Protestant; Hilberts left that church c. 1902 (Reid 1970 p. 91 via Shaposhnikov S7 and Wikipedia S5); Shaposhnikov reconstructs him as seeming agnostic; 1927 Hamburg Foundations address (van Heijenoort / Marxists reprint S8) says mathematics is presuppositionless and 'To found it I do not need God, as does Kronecker' — math-foundations claim, not a place/deny of personal intervening God in nature (P20: agnostic with no stated locus → A BELOW; Curie/Meitner pattern). primary_system UNKNOWN → BELOW_THRESHOLD with AGNOS lead (no own-voice 'I am agnostic' / explicit suspension; biographer 'seemed' + church exit ≠ AGNOS at 0.5). B_cause stays 3 @0.5 alt 4 (RQ O2 / P16 addendum; after working years P20): print check completed against Die Naturwissenschaften 18 (1930) 959–963 PDF scan (S2 upgraded; Einheit passage confirmed); support single (same address, not two independent sources). mid_basin UNKNOWN → BELOW_THRESHOLD (A BELOW, P4 cannot apply; Sagan/Jung/Curie pattern). Chart-moving NO (need A≥0.7 and B≥0.7; A has no plottable value; B capped 0.5). Filled family_religion, nominal_affiliations, changes_over_life. Reid monograph pages unread (IA borrow 401). No fallacy_catalog. Draft, not reviewed."}

identity:
  id: hilbert-david
  display_name: "David Hilbert"
  roster:
    canonical_name: "David Hilbert"
    rank: 91
    F: 4
    models: [Claude, Gemini, GPT, Grok]
    band: "core (3–4)"
    status: core
    field: mathematics
    field_bucket: mathematics
  full_name: {value: "David Hilbert", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "lead"}], how_known: "Britannica and Wikipedia agree (P15)."}
  native_name: {value: "David Hilbert", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "lead"}], how_known: "German; same spelling."}
  aliases:
    - {name: "David-Hilbert", kind: "roster alias"}
    - {name: "Hilbert-David", kind: "roster alias"}

basics:
  birth:
    date: {value: "1862-01-23", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "lead"}], how_known: "Britannica; Wikipedia."}
    place: {value: "Königsberg, Prussia", modern_name: "Kaliningrad, Russia", polity_then: "Kingdom of Prussia", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "lead"}], how_known: "Britannica; Wikipedia."}
  death:
    date: {value: "1943-02-14", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "Death"}], how_known: "Britannica; Wikipedia."}
    place: {value: "Göttingen, Germany", modern_name: "Göttingen, Germany", polity_then: "Germany", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "Death"}], how_known: "Britannica; Wikipedia."}
  first_lasting_contribution_year: {value: 1897, certainty: 0.5, cites: [{source: S1, locator: "Zahlbericht sentence"}], how_known: "The Zahlbericht (1897), which 'consolidated what was known' and 'pointed the way to the developments that followed' (S1). The finiteness theorem for invariants is undated in the body (P39) and may be earlier. 1899 (Grundlagen der Geometrie, 'a turning point') is the alternative. Coder's pick (P13)."}
  era_bucket: {value: "1850 to 1949", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "From 1897 (P2); every candidate year falls in the same bucket."}
  region_of_birth: {value: "Eastern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Russia (P3), as for Kant."}
  region_of_work: {value: "Western Europe", certainty: 0.7, cites: [{source: S1, locator: "career paragraph"}], how_known: "Göttingen from 1895 (Germany)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: [German], certainty: 0.7, cites: [{source: S1, locator: "titles"}], how_known: "Britannica."}
  occupations: {value: ["mathematician", "professor"], certainty: 0.7, cites: [{source: S1, locator: "opening; career paragraph"}], how_known: "Britannica."}

contribution:
  era_bucket: 20c_early
  fields: {value: ["algebra and invariant theory", "number theory", "foundations of geometry", "foundations of mathematics", "analysis"], certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
  lasting_original_contributions:
    - {value: "Theorem of invariants (finite basis)", year: UNKNOWN, kind: theory, lasting: "'Hilbert proved the theorem of invariants' (S1)", certainty: 0.7, cites: [{source: S1, locator: "invariants paragraph"}], how_known: "Britannica; undated."}
    - {value: "Zahlbericht (report on algebraic number theory)", year: 1897, kind: work, lasting: "'pointed the way to the developments that followed' (S1)", certainty: 0.5, cites: [{source: S1, locator: "Zahlbericht sentence"}], how_known: "Britannica; lasting status is the coder's reading."}
    - {value: "Grundlagen der Geometrie (axioms for Euclidean geometry)", year: 1899, kind: work, lasting: "'marked a turning point in the axiomatic treatment of geometry' (S1)", certainty: 0.7, cites: [{source: S1, locator: "Grundlagen sentence"}], how_known: "Britannica."}
    - {value: "The 23 problems (Paris address)", year: 1900, kind: other, lasting: "'A substantial part of Hilbert's fame rests on' them (S1)", certainty: 0.7, cites: [{source: S1, locator: "problems paragraph"}], how_known: "Britannica."}
    - {value: "Integral equations; the basis of Hilbert space", year: 1909, kind: theory, lasting: "'led directly to 20th-century research in functional analysis' (S1)", certainty: 0.7, cites: [{source: S1, locator: "integral equations paragraph"}], how_known: "Britannica ('in about 1909'). Mathematics: Hilbert space is 'useful in mathematical analysis and quantum mechanics' but is not itself a theory about physical systems; S1 also credits 'important memoirs on kinetic gas theory and the theory of radiations' to mathematical physics, but they are not listed as lasting here (coder's call), so he is not counted a scientist (P30)."}
  evidence_of_impact:
    - {value: "Bolyai Prize (1910), Mittag-Leffler Prize (1939, with Picard); Göttingen's eminence 'largely because of Hilbert'", kind: "honours in lifetime", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "Britannica."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Prussian Evangelical / Reformed Protestant (Calvinist)", certainty: 0.5, cites: [{source: S5, locator: "Life (baptized and raised a Calvinist)"}, {source: S7, locator: "Reid 1970 p. 91 quotation"}, {source: S6, locator: "Religious Denomination evangelisch"}], how_known: "Wikipedia: baptized and raised Calvinist in the Prussian Evangelical Church; Reid (via Shaposhnikov) on Reformed Protestant Church of baptism and marriage; Deutsche Biographie evangelisch (registry). Heritage, not adult confession (0.5)."}
  family_religious_practice: {value: "Church membership through baptism and (later) marriage in the Reformed Protestant Church", certainty: 0.5, cites: [{source: S7, locator: "Reid 1970 p. 91 quotation"}, {source: S5, locator: "Life"}], how_known: "Reid via Shaposhnikov; left that church c. 1902 (adult change)."}
  parents_and_household: []
  household_circumstances: {value: TODO}
  schooling:
    - {value: "University of Königsberg (Ph.D. 1885)", stage: university, years: "–1885", certainty: 0.7, cites: [{source: S1, locator: "career paragraph"}], how_known: "Britannica."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: [German], certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1897–1909", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations:
    - {value: "Reformed Protestant / Prussian Evangelical Church (baptized and married; left c. 1902)", years: "–c. 1902", certainty: 0.5, cites: [{source: S7, locator: "Reid 1970 p. 91 quotation"}, {source: S5, locator: "Life / note b"}], how_known: "Reid via Shaposhnikov and Wikipedia. Affiliation only; not a scored system."}
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing of his own framing science vs religion as such; Galileo martyrdom remark (S5) is about scientific proof, not his creed."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "Leading candidate AGNOS: left the Reformed Protestant Church c. 1902 (Reid 1970 p. 91 via S7/S5); Shaposhnikov (S7) writes he 'seemed to be agnostic and had nothing to do with theology proper or even religion'; Wikipedia states he 'became an agnostic' (S5). No own-voice 'I am agnostic' or explicit suspension of judgment on God's existence read (CODING_GUIDE: explicit suspension → AGNOS). 1927 'I do not need God' is about founding mathematics, not a creed label. Kept BELOW_THRESHOLD with AGNOS lead (Curie / von Neumann pattern)."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: AGNOS, reason: "Lead: church exit c. 1902; Shaposhnikov/Wikipedia 'agnostic'. Rejected for scoring: no own-voice explicit suspension."}
    - {code: ATHE, reason: "Lead: 'I do not need God' (1927). Rejected: the sentence rejects God as a foundation for mathematics (vs Kronecker), not positive naturalism / denial of God (P38)."}
    - {code: CHRIST, reason: "Heritage: baptized Reformed Protestant. Rejected: left the church c. 1902; working worldview not Christian confession."}
  lio_axes:
    A_locus:
      value: BELOW_THRESHOLD
      cites: [{source: S5, locator: "Life (baptized / agnostic)"}, {source: S7, locator: "Reid 1970 p. 91 / seemed agnostic"}, {source: S8, locator: "presuppositionless / I do not need God"}, {source: S2, locator: "full address (no God)"}, {source: S3, locator: "biography (no religion)"}]
      note: "Evidence of non-affiliation and math-without-God exists but does not place or deny a personal intervening God as locus. P20: an agnostic with no stated locus view gets A BELOW_THRESHOLD. Named alternative if a later own-voice denial is found: A 4 at 0.5 with BELOW as alt (P38)."
      how_known: "Checked: Reid church-exit story (S7/S5); Shaposhnikov agnostic reconstruction (S7); 1927 Foundations 'To found it I do not need God, as does Kronecker' (S8) — foundations of mathematics, not nature's agency; 1930 Naturerkennen und Logik does not mention God (S2); MacTutor (S3) silent on religion. No published 'I do not believe in God' / locus statement read. Curie/Meitner pattern."
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.5
      support: single
      cites: [{source: S2, locator: "Parallelismus / Einheit der Naturgesetze passage (print PDF pp. corresponding to Naturwissenschaften 959–963)"}]
      rationale: "A mathematician needs an explicit remark on nature (P16). The 1930 address gives one: 'wir beobachten die Einheit des Stoffes in der Materie, und wir konstatieren überall die Einheit der Naturgesetze' (we observe the unity of matter, and we find everywhere the unity of the laws of nature), and nature 'comes to meet us ... as if it were ready to reveal its secrets'. A lawful nature everywhere, with no stated no-exception claim (P40) and no denial of miracles: B 3 at 0.5, alternative 4 (P16 addendum / RQ O2). Print check completed (S2 PDF scan of Die Naturwissenschaften). Certainty stays 0.5: after working years (P20) and P16 alt-4 rule."
      how_known: "Published address; print-checked against Die Naturwissenschaften 18 (28 Nov 1930), pp. 959–963 via Wayback PDF of the psiquadrat journal scan (S2). Translation the coder's. Support single: one address (web transcription matches print; not two independent sources)."
      alternatives:
        - {value: 4, note: "No stated exceptionless law (P40).", cites: [{source: S2, locator: "Einheit der Naturgesetze passage"}]}
    C_ledger: {value: UNKNOWN, how_known: "Nothing read."}
    D_authority: {value: UNKNOWN, how_known: "Nothing read; 'Wir müssen wissen, wir werden wissen' is about knowability, not revelation."}
    E_scope: {value: UNKNOWN, how_known: "Lead: 'überall die Einheit der Naturgesetze' may bear on same laws everywhere (E); not scored this pass (P7 / open question)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD, so the P4 test cannot be applied (Sagan/Jung/Curie pattern). B is scored (3 @0.5) but cannot alone decide mid_basin."}
  statements:
    - text: "Noch einen anderen Parallelismus nehmen wir wahr: unser Denken geht auf Einheit aus und sucht Einheit zu bilden; wir beobachten die Einheit des Stoffes in der Materie, und wir konstatieren überall die Einheit der Naturgesetze. Dabei kommt uns die Natur in Wirklichkeit bei unserer Forschung sehr entgegen, als wäre sie bereit, ihre Geheimnisse gern zu enthüllen."
      cites: [{source: S2, locator: "Parallelismus / Einheit der Naturgesetze passage"}]
      date: "1930"
      context: "Address 'Naturerkennen und Logik' to the Society of German Scientists and Physicians, Königsberg, 1930, printed in Die Naturwissenschaften 18 (28 November 1930), pp. 959–963."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Print check: Einheit passage confirmed in Die Naturwissenschaften PDF scan (S2). Coder's translation in the B rationale."
    - text: "Already at this time I should like to assert what the final outcome will be: mathematics is a presuppositionless science. To found it I do not need God, as does Kronecker, or the assumption of a special faculty of our understanding attuned to the principle of mathematical induction, as does Poincaré, or the primal intuition of Brouwer, or, finally, as do Russell and Whitehead, axioms of infinity, reducibility, or completeness, which in fact are actual, contentual assumptions that cannot be compensated for by consistency proofs."
      cites: [{source: S8, locator: "closing Foundations of Mathematics 1927 passage"}, {source: S7, locator: "1927 Hamburg / van Heijenoort p. 479 quotation"}]
      date: "1927"
      context: "Hilbert, 'Die Grundlagen der Mathematik' (Hamburg 1927); English in van Heijenoort 1967 p. 479 as quoted by Shaposhnikov; full English paragraph from The Emergence of Logical Empiricism reprint (S8)."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "scholarly edition"
      verified_on: 2026-10-24
      note: "Math-foundations claim (vs Kronecker), not a locus place/deny of personal intervening God. Documented for A lead; A stays BELOW_THRESHOLD."
  changes_over_life:
    - {value: "Left the Reformed Protestant Church in which he had been baptized and married, c. 1902 (during/near working years); son Franz reportedly could not answer 'What religion are you?' at school", year: "1902", certainty: 0.5, cites: [{source: S7, locator: "Reid 1970 p. 91 quotation"}, {source: S5, locator: "Life / note b"}], how_known: "Reid via Shaposhnikov; Wikipedia. Affiliation change, not a scored locus statement."}
  coder_notes: "Coder's call. Did not score AGNOS or A 4 from church exit + 'I do not need God' for math foundations (overclaim). Did not list kinetic-gas/radiation memoirs as lasting to flip P30 scientist (same B 3 @0.5 under P35 anyway). Did not score E from 'überall'. Reid monograph pages unread (IA 401). No fallacy_catalog (Jason). Figures not refreshed."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "German (East Prussian)", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  religious_heritage_by_birth: {value: "Prussian Evangelical / Reformed Protestant (Calvinist)", certainty: 0.5, cites: [{source: S5, locator: "Life"}, {source: S7, locator: "Reid 1970 p. 91"}], how_known: "Baptized in that church (0.5)."}
  baptism_or_initiation: {value: "Baptized in the Prussian Evangelical / Reformed Protestant Church", certainty: 0.5, cites: [{source: S5, locator: "Life"}, {source: S7, locator: "Reid 1970 p. 91"}, {source: S6, locator: "evangelisch"}], how_known: "Wikipedia; Reid via Shaposhnikov; Deutsche Biographie."}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1897–1909", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "First to last dated listed lasting contribution (P29, P30)."}
  age_at_first_lasting_contribution: {value: 35, certainty: 0.5, cites: [{source: S1, locator: "opening; 1897"}], how_known: "1897 − 1862 = 35 (P30)."}
  first_evidence_of_lio_type_views: {value: "1930: 'überall die Einheit der Naturgesetze' (B); church exit c. 1902 is affiliation only", year: 1930, certainty: 0.5, cites: [{source: S2, locator: "address"}, {source: S7, locator: "Reid 1970 p. 91"}], how_known: "B statement 1930; earlier physics memoirs not read for nature-order claims (P30 #7)."}
  lio_views_relative_to_major_work: {value: "after major work", certainty: 0.5, cites: [{source: S2, locator: "address"}], how_known: "1930 B remark after 1909; church exit c. 1902 is during/near working years but not a locus score."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "primary_system BELOW_THRESHOLD; A BELOW; no locus statement from 1897–1909 read."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "partly", rationale: "Axiomatic method in geometry (S1); a mathematical style, not a theology.", certainty: 0.5, cites: [{source: S1, locator: "Grundlagen sentence"}], how_known: "Coder's reading."}
  form_acquired: {value: "through the profession", certainty: 0.5, cites: [{source: S1, locator: "Grundlagen sentence"}], how_known: "Coder's reading."}
  circle_present: {value: "no", rationale: "Left church; no scored personal intervening God; A BELOW (S5, S7, S8).", certainty: 0.5, cites: [{source: S7, locator: "Reid / agnostic paragraph"}, {source: S5, locator: "Life"}], how_known: "Lane B reading; not a finding."}
  reading: "Unity of nature's laws (B 3 @0.5); A BELOW; AGNOS lead unscored; unplotted."
  notes: "Lane B only. Chart-moving NO."

institutions:
  - {value: "University of Königsberg", role: "Privatdozent, then professor", years: "1886–1895", kind: university, certainty: 0.7, cites: [{source: S1, locator: "career paragraph"}], how_known: "Britannica."}
  - {value: "University of Göttingen", role: "professor of mathematics", years: "1895–1930", kind: university, certainty: 0.7, cites: [{source: S1, locator: "career paragraph; 1930 retirement"}], how_known: "Britannica."}
collaborators:
  - {value: "Hermann Minkowski", relation: collaborator, note: "colleague and friend; mathematics applied to physics", certainty: 0.7, cites: [{source: S1, locator: "physics paragraph"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 91"}], how_known: "Study roster."}
  controversies:
    - {value: "Whether 'I do not need God' (1927) is only anti-Kronecker foundations rhetoric or a broader irreligion claim — coded as foundations-only (A stays BELOW)", certainty: 0.5, cites: [{source: S8, locator: "presuppositionless science passage"}, {source: S7, locator: "1927 quotation"}], how_known: "Coder's call."}
  data_quality_flags:
    - "B rests on one 1930 address (print-checked); certainty capped 0.5 by P16/P20."
    - "Reid Hilbert (1970) monograph pages unread this pass (IA borrow 401); Reid quoted via Shaposhnikov."
    - "A BELOW: no own-voice locus statement."
  open_questions:
    - "Optional: Constance Reid Hilbert (1970/1996) print pages beyond the p. 91 quotation (may confirm AGNOS wording or add locus)."
    - "Optional: Ewald From Kant to Hilbert vol. 2 pp. 1157–1165 English of the full 1930 address (secondary scholarly edition of same text)."
    - "Optional: kinetic gas / radiation memoirs for earlier nature-order claims during working years (could interact with P20 timing; unlikely to lift B above 0.5 under P16 alt 4)."
    - "Lead: Einheit sentence may bear on E; not scored."
    - "Settled this pass: print check of Naturwissenschaften 1930 completed (S2 PDF)."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Irving Kaplansky"
    citation: "Kaplansky, Irving. \"David Hilbert.\" Encyclopaedia Britannica. https://www.britannica.com/biography/David-Hilbert. Create-pass body from Wayback snapshot 20260131000341; live fetch 2026-10-24 thin."
    url: "https://www.britannica.com/biography/David-Hilbert"
    accessed: 2026-10-24
    reliability_note: "Signed article. Body only; Quick Facts not cited."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, timing, lane_b, institutions, collaborators]
  - id: S2
    type: primary
    kind: "published work by the subject"
    author: "David Hilbert"
    citation: "Hilbert, David. \"Naturerkennen und Logik.\" Die Naturwissenschaften 18 (28 November 1930): 959–963. Print-checked via Wayback PDF of the psiquadrat.de journal scan (http://www.psiquadrat.de/downloads/hilbert_naturwissenschaft1930.pdf); web transcription https://www.rschr.de/Htm/David_Hilbert_Naturerkennen_und_Logik.htm matches the Einheit passage."
    url: "http://www.psiquadrat.de/downloads/hilbert_naturwissenschaft1930.pdf"
    accessed: 2026-10-24
    reliability_note: "Primary published address. Print check completed 2026-10-24 against journal PDF scan (OCR noisy but Einheit der Naturgesetze passage confirmed). Web transcription retained as readable double-check of the same text — not a second independent source for P48."
    source_quality: "archive scan (OCR only)"
    used_for: [worldview, timing, lane_b]
  - id: S3
    type: secondary
    kind: other
    author: "J J O'Connor and E F Robertson"
    citation: "O'Connor, J. J., and E. F. Robertson. \"David Hilbert.\" MacTutor History of Mathematics Archive (last update November 2014). https://mathshistory.st-andrews.ac.uk/Biographies/Hilbert/"
    url: "https://mathshistory.st-andrews.ac.uk/Biographies/Hilbert/"
    accessed: 2026-10-24
    reliability_note: "Signed biography; searched for religion, nothing found."
    source_quality: "reference entry"
    used_for: [worldview]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-17
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S5
    type: secondary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia. \"David Hilbert.\" https://en.wikipedia.org/wiki/David_Hilbert. Read 2026-10-24."
    url: "https://en.wikipedia.org/wiki/David_Hilbert"
    accessed: 2026-10-24
    reliability_note: "Dual-bio second source (P50) for dates/places; Life section on baptism, church exit, agnostic label (cites Reid / Shaposhnikov)."
    source_quality: "reference entry"
    used_for: [identity, basics, childhood, worldview, heritage, review]
  - id: S6
    type: secondary
    kind: encyclopedia
    author: "Deutsche Biographie"
    citation: "\"Hilbert, David.\" Deutsche Biographie. https://www.deutsche-biographie.de/11855090X.html"
    url: "https://www.deutsche-biographie.de/11855090X.html"
    accessed: 2026-10-24
    reliability_note: "Lists Religious Denomination evangelisch (nominal/registry; not used to override church-exit evidence)."
    source_quality: "reference entry"
    used_for: [heritage]
  - id: S7
    type: secondary
    kind: "journal article"
    author: "Vladislav Shaposhnikov"
    citation: "Shaposhnikov, Vladislav. \"Theological Underpinnings of the Modern Philosophy of Mathematics. Part II: The Quest for Autonomous Foundations.\" Studies in Logic, Grammar and Rhetoric 44, no. 1 (2016): 147–168. https://doi.org/10.1515/slgr-2016-0009. PDF via Sciendo."
    url: "https://doi.org/10.1515/slgr-2016-0009"
    accessed: 2026-10-24
    reliability_note: "Peer-reviewed article. Quotes Reid 1970 p. 91 (church exit) and the 1927 lieben Gott line via van Heijenoort; 'seemed to be agnostic' is the author's reconstruction."
    source_quality: "scholarly reconstruction"
    used_for: [worldview, childhood, heritage, review]
  - id: S8
    type: primary
    kind: "published work by the subject"
    author: "David Hilbert"
    citation: "Hilbert, David. \"The Foundations of Mathematics\" (1927). English in The Emergence of Logical Empiricism (Garland, 1996), reproduced at https://www.marxists.org/reference/subject/philosophy/works/ge/hilbert.htm; German/van Heijenoort 1967 p. 479 as cited by Shaposhnikov (S7)."
    url: "https://www.marxists.org/reference/subject/philosophy/works/ge/hilbert.htm"
    accessed: 2026-10-24
    reliability_note: "English reprint of the 1927 Hamburg Foundations address; 'presuppositionless science' / 'I do not need God, as does Kronecker' passage. Unofficial web reprint of a published translation — used with S7's van Heijenoort pointer."
    source_quality: "unofficial web copy"
    used_for: [worldview]
---

# David Hilbert

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

David Hilbert (1862–1943), German mathematician [S1; S5]. Deepen D1: primary_system BELOW_THRESHOLD (AGNOS lead); A BELOW_THRESHOLD; B 3 @0.5 alt 4 (print-checked 1930 address); mid_basin BELOW_THRESHOLD. Not plotted. Chart-moving NO.

## Life and work

Königsberg, then Göttingen from 1895 [S1]. Baptized Reformed Protestant; left that church c. 1902 [S5; S7].

## Contribution and impact

Invariants, Zahlbericht (1897), Grundlagen der Geometrie (1899), the 23 problems (1900), integral equations (1909) [S1].

## Childhood and education

Prussian Evangelical / Calvinist heritage [S5; S7]. University of Königsberg (Ph.D. 1885) [S1].

## Adult working worldview

'überall die Einheit der Naturgesetze' (1930, print-checked) → B 3 @0.5 alt 4 [S2]. No stated locus for A; church exit + 'I do not need God' for math foundations → A BELOW [S5; S7; S8].

## Heritage (context only)

East Prussian; Reformed Protestant baptism [S1; S5; S7].

## Timing

First lasting contribution 1897, at 35 [S1]. B remark 1930 after major work.

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Axiomatic style [S1]; A BELOW; B 3 @0.5; unplotted.

## Open questions

- Reid monograph pages; Ewald English; E from Einheit; gas/radiation memoirs.

## Research log

- 2026-10-17: Read Britannica (Kaplansky; Wayback 20260131000341), MacTutor and a transcription of 'Naturerkennen und Logik' directly; the psiquadrat.de scan timed out from the box.
- 2026-10-24: Deepen D1. Print-checked 1930 address (Wayback PDF). Wikipedia dual bio; Shaposhnikov 2016; 1927 Foundations reprint. Reid IA borrow 401. Wrote drafts/deepen_hilbert-david.md (untracked). No figures refresh. No fallacy_catalog.
