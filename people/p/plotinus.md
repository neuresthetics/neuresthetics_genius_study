---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 4
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch AA8; deepen D1)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.primary_domain set to philosophy. Lane A craft label only; scores unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen D1 (queue #198/228, F 3, rank 211): firm A if a clear reading ≥0.5; corroborate B; leave B reconstruction-labeled (RQ-AA8-1); do not force plot. Re-read SEP Kalligas (S1); Wikipedia EN dual bio (S3); IEP Moore (S4); MacKenna MIT Enneads V.2.1 and III.1.10 (S5). A stays BELOW_THRESHOLD: primary V.2.1 'The One is all things and no one of them' + overflow emanation (A 2–4 lead) against SEP/IEP 'beyond being' / not a being / not strict pantheist (A 1 lead); IEP: no creatio ex nihilo; PLATO system file Neoplatonic One toward 2–3. No reading reaches 0.5 over the other (Gandhi/Plotinus pattern). B stays 3 @0.5 scholarly_reconstruction (RQ-AA8-1 leave reconstruction-labeled); support single→corroborated (S1 §2 + S4 + S5 III.1.10 two-kinds causation / exogenous proviso). primary PLATO @0.5 scholarly_reconstruction unchanged. Mid BELOW. Dual bio P50 (SEP + Wikipedia EN; Britannica Cloudflare-blocked). P47 source_quality on all. Not plotted. Fallacy audit none; figures not refreshed."}
    - {date: 2026-10-21, by: "Grok Bot", summary: "RQ-AA8-1 resolved yes by Jason (2026-10-21, P49): B 3 at 0.5 from SEP's reconstruction (basis scholarly_reconstruction), alternative 2. Still not plotted (A BELOW_THRESHOLD)."}
    - {date: 2026-10-20, by: "Grok Bot", summary: "AA8 audit fixes: B reason corrected (SEP §2 does set out a view of nature); B stays UNKNOWN pending RQ-AA8-1; SEP summary dropped as a statement (not a scholarly edition); 'mature age of fifty' cited."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch AA8, order P32: F 3, rank 211). Source: SEP 'Plotinus' (Paul Kalligas, 2024, read in full). Born 204 CE (inferred from Porphyry, S1); settled in Rome late 244; his treatises 'began to be composed ten years after his arrival in Rome' (about 254) and continued until his death in 270 (S1). Lasting work: the treatises collected by Porphyry as the Enneads; he 'is generally regarded as the founder of Late Antique Platonism, sometimes termed Neoplatonism' (S1). Span 254–270 at 0.5 (composition range, RQ-Z9-N1; start inferred), age 50. Worldview: PLATO at 0.5 (scholarly_reconstruction): 'Plato's figure dominates Plotinus' thought' (S1). A BELOW_THRESHOLD: the One is 'beyond being' and transcendent (A 1 lead), but everything proceeds from it by emanation (A 2 lead); no source read settles the reading. Not a scientist; B UNKNOWN pending RQ-AA8-1 (held for Jason): S1 §2 does reconstruct his account of nature (laws 'constant and immutable'; the same causes 'inexorably produce the same effects, provided that no other exogenous factor enters into play'); mid_basin BELOW_THRESHOLD. Not plotted. Draft, not reviewed."}

identity:
  id: plotinus
  display_name: "Plotinus"
  roster:
    canonical_name: "Plotinus"
    rank: 211
    F: 3
    models: [Claude, DeepSeek, Grok]
    band: "core (3–4)"
    status: "core"
    field: "philosophy"
    field_bucket: "philosophy"
  full_name: {value: "Plotinus", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Writings"}, {source: S3, locator: "infobox / lead"}], how_known: "SEP and Wikipedia EN."}
  native_name: {value: "Πλωτῖνος", certainty: 0.7, cites: [{source: S3, locator: "lead (Ancient Greek: Πλωτῖνος)"}], how_known: "Wikipedia EN prints the Greek form."}
  aliases: []

basics:
  birth:
    date: {value: "204", certainty: 0.5, cites: [{source: S1, locator: "1. Life and Writings"}, {source: S3, locator: "infobox (c. 204/5)"}], how_known: "SEP: 'we may infer that he was born in 204 CE' (from Porphyry); Wikipedia c. 204/5."}
    place:
      value: "Lycopolis (Asyut), Egypt"
      modern_name: "Asyut, Egypt"
      polity_then: "Roman Egypt"
      certainty: 0.5
      cites: [{source: S3, locator: "infobox (Asyut or Lycopolis)"}, {source: S1, locator: "1. Life and Writings ('a native of Egypt')"}]
      how_known: "Wikipedia EN: Asyut or Lycopolis; SEP Egypt only (town not given). Dual bio; 0.5 for the town."
      alternatives:
        - {value: "Egypt (town unknown)", cites: [{source: S1, locator: "1. Life and Writings"}], note: "SEP does not name the town."}
  death:
    date: {value: "270", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Writings"}, {source: S3, locator: "infobox"}], how_known: "SEP and Wikipedia EN."}
    place: {value: "Campania", modern_name: "Campania, Italy", polity_then: "Roman Empire", certainty: 0.5, cites: [{source: S3, locator: "infobox"}], how_known: "Wikipedia EN only among sources read this pass (SEP: taught in Rome until death; place not stated)."}
  first_lasting_contribution_year: {value: 254, certainty: 0.5, cites: [{source: S1, locator: "1. Life and Writings"}], how_known: "Treatises 'began to be composed ten years after his arrival in Rome' (late 244), so about 254; 'Plotinus began composing his works approximately in the last sixteen years of his life, which means he started when he was already at the mature age of fifty' (S1); composition range (RQ-Z9-N1); 0.5."}
  era_bucket: {value: "-500 to 499", certainty: 1.0, cites: [{source: S1, locator: "1. Life and Writings"}], how_known: "254, and every year of his life, falls in -500 to 499 (P2)."}
  region_of_birth: {value: "Middle East and North Africa", certainty: 0.5, cites: [{source: S1, locator: "1. Life and Writings"}, {source: S3, locator: "infobox"}], how_known: "Egypt (P3)."}
  region_of_work: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Writings"}], how_known: "Rome, where the span took place (AA6 rule); home-region alternative MENA."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S3, locator: "throughout"}], how_known: "As recorded."}
  languages_of_work: {value: ["Ancient Greek"], certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S3, locator: "lead (Ancient Greek)"}], how_known: "Treatises in Greek; Wikipedia prints Greek native name."}
  occupations: {value: ["philosopher", "teacher"], certainty: 0.7, cites: [{source: S1, locator: "1. Life and Writings"}, {source: S3, locator: "lead"}], how_known: "SEP and Wikipedia EN."}

contribution:
  primary_domain: philosophy
  fields: {value: ["philosophy", "metaphysics"], certainty: 0.7, cites: [{source: S1, locator: "text"}, {source: S4, locator: "opening"}], how_known: "SEP and IEP."}
  lasting_original_contributions:
    - {value: "The treatises collected by Porphyry as the Enneads (the One, Intellect, Soul)", year: 254, kind: "body of work", lasting: "'Plotinus is generally regarded as the founder of Late Antique Platonism, sometimes termed Neoplatonism'; 'one of the supreme intellectual achievements of the period that has come to be called Late Antiquity' (S1)", certainty: 0.5, cites: [{source: S1, locator: "1. Life and Writings; opening"}, {source: S3, locator: "lead"}], how_known: "Composed from about 254 to 270 (S1)."}
  evidence_of_impact:
    - {value: "Founder of Neoplatonism; influence on the Middle Ages and Renaissance", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "opening"}], how_known: "SEP and IEP."}
  major_works:
    - {value: "Enneads (Porphyry's collection of the treatises)", kind: book, certainty: 0.7, cites: [{source: S1, locator: "1. Life and Writings"}, {source: S5, locator: "MIT Classics MacKenna translation"}], how_known: "SEP; MacKenna translation used this pass."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Founder of Neoplatonism (S1).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated."}
  family_religious_practice: {value: UNKNOWN, how_known: "Not stated."}
  parents_and_household: []
  household_circumstances: {value: UNKNOWN, how_known: "Not stated."}
  schooling:
    - {value: "Studied with Ammonius Saccas in Alexandria from age 28, for eleven years", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Writings"}, {source: S4, locator: "1. Life and Work"}], how_known: "SEP and IEP."}
  early_mathematics: {value: UNKNOWN, how_known: "Not stated."}
  early_geometric_style_reasoning: {value: UNKNOWN, how_known: "Not stated."}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: UNKNOWN, how_known: "Not stated."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "254–270", certainty: 0.5, cites: [{source: S1, locator: "1. Life and Writings"}], how_known: "Equals timing.major_work_period."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Not read."}
  primary_system:
    value: PLATO
    basis: scholarly_reconstruction
    certainty: 0.5
    cites: [{source: S1, locator: "opening; 1. Life and Writings"}]
    how_known: "Scholar's reconstruction: SEP (Kalligas)."
    rationale: "'Plato's figure dominates Plotinus' thought, constituting the key source of inspiration for [his] worldview' (S1); founder of Late Antique Platonism. 0.5: reconstruction from one scholarly source (P49). PLATO system file scores Neoplatonic One toward A 2–3; person A left BELOW on the mixed primary reading."
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: PLATO, reason: "Coded at 0.5 (S1); deepen D1 reconfirms."}
    - {code: PANT, reason: "Lead only, rejected: IEP 'not a strict pantheist'; V.2.1 'all things and no one of them' / source is not all things; standing rule blocks a pantheism code on the mixed A."}
    - {code: CLASS_THEISM, reason: "Lead only (emanationist First Cause pattern as in al-Farabi); rejected for Plotinus because the One is beyond being/personhood and V.2.1 affirms both poles; not a creatio-ex-nihilo theism (IEP)."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "Deepen D1: primary MacKenna V.2.1 (S5) — 'The One is all things and no one of them; the source of all things is not all things'; 'has overflowed, and its exuberance has produced the new' (emanation / overflow). SEP (S1): One 'beyond being', radically different from what proceeds; emanation of Intellect and Soul. IEP (S4): One transcends beings, 'not itself a being'; 'not a strict pantheist' yet 'does not permit creatio ex nihilo'; all existence emanates. A 1 lead (transcendent source beyond being, not identical with the world) against A 2–4 lead (overflow, all-pervasive unity, 'all things'). PLATO system file: Neoplatonic One toward 2–3. No reading reaches 0.5 over the other (Gandhi/Plotinus pattern; deepen standing rule). Do not invent certainty; do not force plot.", note: "Own-words MacKenna is an unofficial web copy of a published translation (P21 unofficial-web cap); the mix itself, not the edition status, blocks the score."}
    B_cause:
      value: 3
      basis: scholarly_reconstruction
      certainty: 0.5
      support: corroborated
      cites: [{source: S1, locator: "§2 (III 1.10)"}, {source: S4, locator: "opening / cosmology"}, {source: S5, locator: "Third Ennead, First Tractate (III.1) §10"}]
      how_known: "Scholarly reconstruction (P49, RQ-AA8-1 resolved yes by Jason, 2026-10-21; deepen D1: leave reconstruction-labeled). Not a scientist (P30). SEP §2 reconstructs his account of nature: laws 'constant and immutable'; same causes 'inexorably produce the same effects, provided that no other exogenous factor enters into play'. MacKenna III.1.10 (S5) states the primary two-kinds causation (Soul's own motion vs environment/Fate). IEP (S4) corroborates the emanationist cosmology frame. 0.5 is the scholarly_reconstruction ceiling. Support corroborated: three distinct ids, alternatives cite only S1/S5 (P48)."
      rationale: "Account of nature (P6): constant laws and fixed causation, with the stated proviso of an 'exogenous factor' / Soul's free motion as the limited exception, so B 3. Alternative 2 if the proviso is read as an open door for the soul's and higher principles' action in nature."
      alternatives:
        - {value: 2, note: "Proviso / Soul's own motion read as an unlimited exception rather than a limited carve-out.", cites: [{source: S1, locator: "§2"}, {source: S5, locator: "III.1.10"}]}
    C_ledger: {value: UNKNOWN, how_known: "Not scored this pass."}
    D_authority: {value: UNKNOWN, how_known: "Not scored this pass."}
    E_scope: {value: UNKNOWN, how_known: "Not scored this pass."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus is BELOW_THRESHOLD, so the P4 test cannot be applied (Pavlov pattern / P19)."}
  statements:
    - text: "The One is all things and no one of them; the source of all things is not all things; all things are its possession- running back, so to speak, to it- or, more correctly, not yet so, they will be. … Seeking nothing, possessing nothing, lacking nothing, the One is perfect and, in our metaphor, has overflowed, and its exuberance has produced the new: this product has turned again to its begetter and been filled and has become its contemplator and so an Intellectual-Principle."
      cites: [{source: S5, locator: "Fifth Ennead, Second Tractate (V.2) §1"}]
      date: "254"
      context: "Enneads V.2.1 On the Origin and Order of the Beings; MacKenna translation. Composition within the treatise span."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "MIT Classics MacKenna HTML. Documents the A mix (all-and-none + overflow); does not by itself settle A ≥0.5. P21 unofficial-web cap."
    - text: "To sum the results of our argument: All things and events are foreshown and brought into being by causes; but the causation is of two Kinds; there are results originating from the Soul and results due to other causes, those of the environment. In the action of our Souls all that is done of their own motion in the light of sound reason is the Soul's work, while what is done where they are hindered from their own action is not so much done as suffered. Unwisdom, then, is not due to the Soul, and, in general- if we mean by Fate a compulsion outside ourselves- an act is fated when it is contrary to wisdom."
      cites: [{source: S5, locator: "Third Ennead, First Tractate (III.1) §10"}]
      date: "254"
      context: "Enneads III.1 On Fate, closing summary; MacKenna translation. Primary warrant behind SEP §2's reconstruction of constant laws with exogenous proviso."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "unofficial web copy"
      verified_on: 2026-10-24
      note: "MIT Classics MacKenna HTML. Corroborates B 3 reconstruction; basis left scholarly_reconstruction per RQ-AA8-1. P21 unofficial-web cap."
  changes_over_life: []
  coder_notes: "Deepen D1. A left BELOW on primary mix (V.2.1), not forced to PLATO-system 2–3 or al-Farabi A 1. B support lifted to corroborated; basis/certainty left scholarly_reconstruction @0.5 (RQ-AA8-1). Britannica Plotinus page Cloudflare-blocked this pass; dual bio = SEP + Wikipedia EN (+ IEP). Armstrong Loeb / hard-copy MacKenna not opened. Do not force plot. No fallacy_catalog; figures/ untouched."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: UNKNOWN, how_known: "Egyptian birthplace only; ethnic label not stated."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "Not stated."}
  childhood_catechism: {value: UNKNOWN, how_known: "Not stated."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "254–270", certainty: 0.5, cites: [{source: S1, locator: "1. Life and Writings"}], how_known: "Composition range of the treatises, about 254 to his death in 270 (RQ-Z9-N1); start inferred, 0.5."}
  age_at_first_lasting_contribution: {value: 50, certainty: 0.5, cites: [{source: S1, locator: "1. Life and Writings"}], how_known: "254 − 204 = 50 (P30 year difference); S1: 'he started when he was already at the mature age of fifty'."}
  first_evidence_of_lio_type_views: {value: "254–270", certainty: 0.5, cites: [{source: S5, locator: "V.2.1; III.1.10"}], how_known: "MacKenna V.2.1 (A mix) and III.1.10 (B two-kinds causation) fall inside the composition span; exact treatise years within 254–270 not fixed this pass."}
  lio_views_relative_to_major_work: {value: "during major work", certainty: 0.5, cites: [{source: S5, locator: "V.2.1; III.1.10"}, {source: S1, locator: "1. Life and Writings"}], how_known: "Treatises composed in the span."}
  worldview_during_major_work: {value: "PLATO @0.5; A BELOW_THRESHOLD; B 3 @0.5 scholarly_reconstruction", certainty: 0.5, cites: [{source: S1, locator: "opening; §2"}, {source: S5, locator: "V.2.1; III.1.10"}], how_known: "As coded."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Metaphysics of the One and hypostases (S1; S4); not a geometric method claim.", certainty: 0.5, cites: [{source: S1, locator: "text"}, {source: S4, locator: "opening"}], how_known: "Coder's reading."}
  form_acquired: {value: UNKNOWN, how_known: "Not applicable."}
  circle_present: {value: "unclear", rationale: "Not assessed.", certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  reading: "No geometric-form claim scored. Lane B here is the labeled belief model only."
  notes: ""

institutions: []
collaborators:
  - {value: "Ammonius Saccas", relation: "teacher", note: "Alexandria", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Writings"}, {source: S4, locator: "1. Life and Work"}], how_known: "SEP and IEP."}
  - {value: "Porphyry", relation: "student or assistant", note: "editor of the Enneads; Life of Plotinus", certainty: 0.7, cites: [{source: S1, locator: "1. Life and Writings"}, {source: S3, locator: "lead"}], how_known: "SEP and Wikipedia EN."}

review:
  roster_status_reason: {value: "Core in v8 (F 3).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 211"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Span and age inferred (0.5)."
    - "MacKenna via MIT Classics unofficial web copy (P21); Armstrong Loeb not opened."
    - "B left scholarly_reconstruction-labeled per RQ-AA8-1 despite primary III.1.10 corroboration."
  open_questions:
    - "A_locus: whether a future Loeb/Armstrong reading or a settled scholarly consensus could push one pole (transcendent source vs overflow immanence) to ≥0.5 without inventing certainty."
    - "Death place Campania rests on Wikipedia alone among sources opened this pass."

sources:
  - id: S1
    type: tertiary
    kind: "encyclopedia"
    author: "Paul Kalligas"
    citation: "Kalligas, Paul. 'Plotinus.' Stanford Encyclopedia of Philosophy (2024). https://plato.stanford.edu/entries/plotinus/"
    url: "https://plato.stanford.edu/entries/plotinus/"
    accessed: 2026-10-24
    reliability_note: "Signed entry, re-read in full this pass (§2 Nature; One/emanation)."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, timing, collaborators]
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
    citation: "Wikipedia. 'Plotinus.' https://en.wikipedia.org/wiki/Plotinus"
    url: "https://en.wikipedia.org/wiki/Plotinus"
    accessed: 2026-10-24
    reliability_note: "Dual bio (P50) with SEP: birth Lycopolis/Asyut, death Campania, Greek name Πλωτῖνος."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, collaborators]
  - id: S4
    type: tertiary
    kind: "encyclopedia"
    author: "Edward Moore"
    citation: "Moore, Edward. 'Plotinus.' Internet Encyclopedia of Philosophy. https://iep.utm.edu/plotinus/"
    url: "https://iep.utm.edu/plotinus/"
    accessed: 2026-10-24
    reliability_note: "Signed IEP entry; One transcends beings; not strict pantheist; no creatio ex nihilo; emanation."
    source_quality: "reference entry"
    used_for: [contribution, childhood, worldview, collaborators]
  - id: S5
    type: primary
    kind: "published work by the subject"
    author: "Plotinus (tr. Stephen MacKenna and B. S. Page)"
    citation: "Plotinus. The Six Enneads. Tr. Stephen MacKenna and B. S. Page. Internet Classics Archive (MIT). https://classics.mit.edu/Plotinus/enneads.html"
    url: "https://classics.mit.edu/Plotinus/enneads.html"
    accessed: 2026-10-24
    reliability_note: "Public-domain MacKenna translation HTML; V.2.1 and III.1.10 read this pass. Unofficial web copy (P21)."
    source_quality: "unofficial web copy"
    used_for: [worldview, contribution, timing]
---

## Summary

Plotinus (204–270), founder of Neoplatonism [S1; S3]. Deepen D1: PLATO 0.5 (scholarly_reconstruction); A BELOW_THRESHOLD (One transcendent / beyond being vs overflow emanation; primary V.2.1 affirms both); B 3 @0.5 scholarly_reconstruction, support corroborated (SEP + IEP + MacKenna III.1.10); mid BELOW. Not plotted.

## Life and work

Egypt (Lycopolis/Asyut); Alexandria under Ammonius Saccas; Rome; died Campania [S1; S3; S4].

## Contribution and impact

Enneads, c. 254–270; founder of Late Antique Platonism / Neoplatonism [S1; S3].

## Childhood and education

Studied with Ammonius Saccas in Alexandria from age 28 for eleven years [S1; S4].

## Adult working worldview

Plato dominates his thought [S1]. Primary V.2.1: One is all things and no one of them, overflow produces Intellect [S5]. Nature/Fate: two kinds of causation, Soul vs environment [S5 III.1.10; S1 §2]. A left BELOW; B reconstruction-labeled @0.5 with corroborated support.

## Heritage (context only)

Not stated beyond Egyptian birthplace.

## Timing

254–270 (0.5), age 50 [S1]. LIO-type views during major work (treatise span).

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. No geometric-form claim scored.

## Open questions

- Whether a future Loeb/Armstrong reading could settle A without inventing certainty.
- Death place Campania: Wikipedia alone among sources opened this pass.

## Research log

- 2026-10-24: Deepen D1. Re-read SEP Kalligas; Wikipedia EN dual bio; IEP Moore; MacKenna MIT V.2.1 and III.1.10. A stays BELOW (primary mix). B support corroborated; basis left scholarly_reconstruction (RQ-AA8-1). Britannica Cloudflare-blocked. No fallacy_catalog; figures not refreshed. Person-file-only commit.
- 2026-10-21: RQ-AA8-1 resolved yes by Jason (2026-10-21, P49): B 3 at 0.5 from SEP's reconstruction (basis scholarly_reconstruction), alternative 2. Still not plotted (A BELOW_THRESHOLD).
- 2026-10-20: AA8 audit fixes: B reason corrected (SEP §2 does set out a view of nature); B stays UNKNOWN pending RQ-AA8-1; SEP summary dropped as a statement (not a scholarly edition); 'mature age of fifty' cited.
- 2026-10-19: Read SEP (Kalligas).
