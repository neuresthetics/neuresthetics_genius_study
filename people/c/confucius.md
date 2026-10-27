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
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to ancient. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-17, by: "Grok Bot", summary: "Record created (stage 3 batch O, order P32: F 4, rank 90). Basics from Britannica (Annping Chin, signed; body only) and SEP 'Confucius' (Csikszentmihalyi, 2024). He wrote nothing that survives as his; the Analects was compiled by first- and second-generation disciples (SEP), so its sayings are reported speech (P42, §7) and cannot score alone. primary_system BELOW_THRESHOLD (CONFUC leading candidate); A BELOW_THRESHOLD (Heaven sayings, reported); B UNKNOWN; mid_basin UNKNOWN (P19). Not plotted. Draft, not reviewed."}
    - {date: 2026-10-17, by: "Grok Bot", summary: "Batch O audit fix (#20): statement dated to the span 498–484 BCE in its context, noted as undated; the placeholder -492 removed and the date field left out (the schema's date field takes one year, not a span). v8's ruling on RQ O1 (on the auditor's advice): the Analects stays reported speech under P42 (recorded in OPEN_DECISIONS). Values unchanged."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #89, F4 rank 90). Needs: A BELOW_THRESHOLD (Analects Heaven = reported speech, P42); B UNKNOWN; primary BELOW (CONFUC candidate). Dual bio: Britannica Chin (S1) + Wikipedia EN (S5) + SEP Csikszentmihalyi (S2) (P50). Added IEP Confucius (Richey, S4). P47 source_quality on S1–S5. Analects stays disciples' reported speech (P42 RQ O1); scores for A rest on scholars' reconstructions (P49), not Analects wording alone — same path as Socrates D1. A_locus BELOW_THRESHOLD → 0 @0.5 scholarly_reconstruction (alt 1): SEP Mandate/Tian section and IEP Theodicy independently reconstruct the Confucius of the Analects as inheriting Zhou theistic Tian / Mandate of Heaven as anthropomorphized or deity-like cosmic power that backs, forsakes, or protects persons (Heaven gave virtue; culture not yet abandoned; 'Heaven has abandoned me'); IEP (via Graham) notes personal protection vs despair and a threefold assumption about Tian (moral alignment; dependence on human agents; variable mortal associations). Named alt 1: Eno naturalization and IEP's fate/nature/deity blend (Tian increasingly naturalized; 'what need does Heaven have to speak?' 17.19) still as moral-cosmic warrant leaning A 1, not atheism. Support corroborated (S2+S4). Illustrative Analects Heaven sayings (S1/S2) and 7.21 silence on spirits (S4) kept as kind reported speech. B_cause stays UNKNOWN: Heaven-as-agent for persons ≠ P16 nature order (CODING_GUIDE / standing rule); 7.21 is silence on prodigies/spirits, not a lawful-nature claim; Analects 17.2 human nature (xing) is about people, not physical law; no scholarly consensus P16 reconstruction for historical Confucius stretched. primary_system stays BELOW_THRESHOLD with CONFUC lead (Founders rule needs own-voice ≥0.5; disciples' record only — Gautama/RQ O1 precedent). mid_basin stays UNKNOWN (B UNKNOWN, P19). Chart-moving NO (still unplotted; A at P49 0.5 cannot darken). Filled family_religion / heritage from Zhou Tian context (IEP). No fallacy_catalog (Jason). Draft, not reviewed."}

identity:
  id: confucius
  display_name: "Confucius"
  roster:
    canonical_name: "Confucius"
    rank: 90
    F: 4
    models: [Claude, DeepSeek, Gemini, Grok]
    band: "core (3–4)"
    status: core
    field: philosophy
    field_bucket: philosophy
  full_name: {value: "Confucius", certainty: 0.7, cites: [{source: S2, locator: "opening"}, {source: S5, locator: "lead"}], how_known: "SEP Latinization; Wikipedia Kong Qiu / Confucius. Britannica Quick Facts not cited."}
  native_name: {value: "Kong Qiu (孔丘); Kongzi / Kong fuzi (孔子 / 孔夫子)", certainty: 0.7, cites: [{source: S2, locator: "opening"}, {source: S4, locator: "opening (Kongzi)"}, {source: S5, locator: "infobox / Name"}], how_known: "SEP, IEP, Wikipedia agree on Kongzi / Kong Qiu forms."}
  aliases: []

basics:
  birth:
    date: {value: "-551", calendar: julian, certainty: 0.5, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "lead (c. 551 BCE)"}, {source: S2, locator: "opening (trad. 551–479)"}], how_known: "Britannica 551 BCE; Wikipedia c. 551; SEP traditional. Approximate (0.5). Proleptic Julian."}
    place: {value: "Zou / Qufu, state of Lu", modern_name: "Qufu, Shandong, China", polity_then: "State of Lu (Zhou dynasty)", certainty: 0.5, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "infobox (Zou, Lu now Qufu)"}], how_known: "Britannica Qufu; Wikipedia Zou, Lu."}
  death:
    date: {value: "-479", calendar: julian, certainty: 0.5, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "lead (c. 479 BCE)"}, {source: S2, locator: "opening"}], how_known: "Britannica; Wikipedia c. 479; SEP traditional."}
    place: {value: "Lu", modern_name: "Shandong, China", polity_then: "State of Lu (Zhou dynasty)", certainty: 0.5, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "infobox (Si River, Lu)"}], how_known: "Britannica Lu; Wikipedia Si River, Lu."}
  first_lasting_contribution_year: {value: UNKNOWN, how_known: "His teaching is undated in the body; the Analects was compiled after his death (P39)."}
  era_bucket: {value: UNKNOWN, how_known: "No dated lasting work (P39), and his adult years (c. 530s–479 BCE) straddle the -500 edge, so no single bucket holds them all."}
  region_of_birth: {value: "East Asia", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "lead"}], how_known: "China (P3)."}
  region_of_work: {value: "East Asia", certainty: 0.7, cites: [{source: S1, locator: "journey paragraph"}, {source: S5, locator: "Life"}], how_known: "Lu, Wei, Song, Chen, Cai."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "text"}], how_known: "As recorded."}
  languages_of_work: {value: ["Classical Chinese"], certainty: 0.5, cites: [{source: S1, locator: "text"}], how_known: "Coder's reading."}
  occupations: {value: ["teacher", "philosopher", "political theorist", "official in Lu"], certainty: 0.7, cites: [{source: S1, locator: "opening; Jisun paragraph"}, {source: S5, locator: "lead"}], how_known: "Britannica; Wikipedia."}

contribution:
  era_bucket: ancient
  fields: {value: ["ethics", "political philosophy", "education"], certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S5, locator: "infobox (Main interests)"}], how_known: "Britannica; Wikipedia."}
  lasting_original_contributions:
    - {value: "Teaching on virtue, ritual and government, transmitted in the Analects", year: UNKNOWN, kind: "body of work", lasting: "'whose ideas have profoundly influenced the civilizations of China and other East Asian countries' (S1)", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "Analects sources section"}], how_known: "Britannica; the text was compiled by disciples (S2)."}
  evidence_of_impact:
    - {value: "Ideas 'profoundly influenced the civilizations of China and other East Asian countries'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}, {source: S4, locator: "opening"}], how_known: "Britannica; IEP."}
  major_works: []
  honours: []
  definition_fit: {value: "clearly meets", rationale: "(S1, S4).", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}

childhood:
  family_religion: {value: "Late Zhou ritual religion (Tian / Mandate of Heaven; ancestor and spirit sacrifices)", certainty: 0.5, cites: [{source: S4, locator: "§3 Theodicy"}, {source: S2, locator: "Mandate of Heaven section"}], how_known: "IEP: child of late Zhou world inheriting theistic Tian / Shangdi legacy and obligations to divinities, local spirits, and ancestors. Not a personal confession (0.5)."}
  family_religious_practice: {value: "Ancestor sacrifice and spirit rites as noble/shi tradition (context)", certainty: 0.5, cites: [{source: S4, locator: "§3 Theodicy"}, {source: S1, locator: "family paragraph"}], how_known: "IEP on network of religious obligations; Britannica on shi status. Specific household rites not read."}
  parents_and_household:
    - {value: "Father Shu-liang He, a warrior and district steward in Lu, already old at his birth; he died soon after it, leaving his young widow to fend for herself", role: father, certainty: 0.7, cites: [{source: S1, locator: "family paragraph"}], how_known: "Britannica."}
  household_circumstances: {value: "The Kongs of Lu were common gentlemen (shi), 'just a notch higher than the common folk'; he later called himself 'poor and from a lowly station' (Analects 9:6)", certainty: 0.7, cites: [{source: S1, locator: "family paragraph; Analects 9:6"}], how_known: "Britannica."}
  schooling: []
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["Old Chinese"], certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  notable_events:
    - {value: "Death of his father soon after his birth", year: UNKNOWN, certainty: 0.7, cites: [{source: S1, locator: "family paragraph"}], how_known: "Britannica."}

worldview:
  unit: "adult working worldview"
  working_years: {value: UNKNOWN, how_known: "Equals timing.major_work_period (UNKNOWN, P39)."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "Nothing in his own hand."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "Leading candidate CONFUC (the tradition named after him). Founders rule (CODING_GUIDE §1) picks the founded code once own-voice evidence reaches 0.5; he is known only through followers' records (Analects = disciples' compilation, P42 RQ O1), so CONFUC stays lead and primary stays BELOW_THRESHOLD (Gautama / Confucius RQ O1 precedent). Scholarly reconstructions of Tian piety (S2, S4) score A under P49 but do not supply own-voice for the system code."}
  secondary_system: {value: UNKNOWN, how_known: "None."}
  candidate_codes_considered:
    - {code: CONFUC, reason: "Founder figure; founded system is the lead. Rejected for scoring: nothing attributable in his own words (P42); Founders needs own-voice ≥0.5."}
    - {code: CHNFOLK, reason: "Zhou Tian, ancestor and spirit rites of his time (S2, S4); context / heritage only, not a scored adult system."}
  lio_axes:
    A_locus:
      value: 0
      basis: scholarly_reconstruction
      certainty: 0.5
      support: corroborated
      cites: [{source: S2, locator: "Mandate of Heaven / Heaven passages (7.23, 9.5, 11.9, 17.19)"}, {source: S4, locator: "§3 Theodicy"}, {source: S1, locator: "Huan Tui and Kuang paragraph (Analects 7:23, 9:5)"}]
      how_known: "P49: scholars' reconstructions score at most 0.5. He wrote nothing; Analects wording is disciples' reported speech (P42 RQ O1) and cannot score alone. Two independent scholarly reconstructions (SEP Csikszentmihalyi; IEP Richey) attribute to the Confucius of the Analects a Tian / Heaven that is deity-like or anthropomorphized cosmic power, drawn from Zhou Mandate of Heaven, that backs, forsakes, or protects persons. Chin (S1) quotes the same Heaven sayings as the life tradition; scores rest on S2+S4."
      rationale: "Interventionist pole (A 0): Heaven as agent that gives virtue and protects him from Huan Tui (7.23), has not yet abandoned Zhou culture (9.5), and can forsake him at Yan Hui's death (11.9) (S1, S2); IEP reconstructs inherited theistic Tian and, via Graham, personal divine backing vs despair, with a threefold assumption (moral alignment; need for human agents; variable mortal associations) (S4). Named alternative: 1 (leans interventionist) — Eno naturalization and IEP's note that Tian also functions as fate and nature (17.19 'what need does Heaven have to speak?') treat Heaven more as moral-cosmic warrant than as a personal god, still not atheism or A ≥ 3. Certainty stays 0.5 (scholarly_reconstruction ceiling + disciples'-record gap)."
    B_cause: {value: UNKNOWN, how_known: "Nothing read that is a P16 statement about nature or the physical world's law and exception. Standing rule: Heaven-as-agent for persons ≠ nature order unless the text says so. Analects 7.21 ('The Master does not speak of prodigies, force, disorder, or spirits') is silence on spirits/prodigies (S4), not a lawful-nature claim. Analects 17.2 on human nature (xing) concerns people, not physical law (S2). No scholarly consensus reconstruction of a P16 exceptionless natural-order account for historical Confucius was stretched (P49 not stretched to B)."}
    C_ledger: {value: UNKNOWN, how_known: "Lead only: SEP notes early discussions stressed benefits of ritual 'beyond the propitiation of spirits, rewards from the ancestors' (S2); not scored this pass."}
    D_authority: {value: UNKNOWN, how_known: "Nothing scored this pass."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read (P7)."}
  mid_basin: {value: UNKNOWN, how_known: "A 0 at 0.5 would lean A ≤ 1, but B_cause is UNKNOWN, which takes precedence (P19)."}
  statements:
    - text: "Heaven has given me this power—this virtue. What can Huan Tui do to me!"
      cites: [{source: S1, locator: "Huan Tui and Kuang paragraph (Analects 7:23)"}, {source: S2, locator: "Heaven passages (7.23)"}]
      context: "Analects 7:23, on Huan Tui's plan to ambush him during his years of travel, 498–484 BCE (S1). Undated: S1 gives no year for the event, only the span of the travels, so the date field is left out (the schema's date takes a single year, not a span)."
      axes: [A_locus]
      kind: "reported speech"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "Recorded by disciples (S2); reported speech (P42). Score rests on scholarly reconstruction (P49), not on this quotation alone. Britannica calls the Analects 'the most reliable source on Confucius's life' — that does not override P42."
    - text: "If Heaven is about to abandon this culture, those who die afterwards will not get to share in it; if Heaven has not yet abandoned this culture, what can the men of Guang do to me?"
      cites: [{source: S4, locator: "§3 Theodicy (Analects 9.5)"}, {source: S2, locator: "Heaven passages (9.5)"}, {source: S1, locator: "Huan Tui and Kuang paragraph (Analects 9:5)"}]
      context: "Analects 9.5 as quoted in IEP Theodicy and SEP; Britannica paraphrase 'Heaven has not destroyed this culture'."
      axes: [A_locus]
      kind: "reported speech"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "P42; P49 score rests on S2+S4 reconstructions."
    - text: "Heaven has abandoned me! Heaven has abandoned me!"
      cites: [{source: S4, locator: "§3 Theodicy (Analects 11.9)"}, {source: S2, locator: "Heaven passages (11.9)"}]
      context: "Analects 11.9 on the death of Yan Hui; SEP 'Heaven has forsaken me!'; IEP wording above."
      axes: [A_locus]
      kind: "reported speech"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "P42; illustrates the forsaking side of reconstructed Tian agency."
    - text: "The Master does not speak of prodigies, force, disorder, or spirits."
      cites: [{source: S4, locator: "§3 Theodicy (Analects 7.21; also 5.13, 11.12 silence cluster)"}]
      context: "Analects 7.21 as attested in IEP (silence on the divine / spirits). Lead for B in create-pass coder_notes; read here — silence, not a P16 nature-order claim."
      axes: [B_cause]
      kind: "reported speech"
      verified_against: "secondary quotation"
      verified_on: 2026-10-24
      note: "P42. Documented as B lead that does not clear P16; B stays UNKNOWN."
  changes_over_life: []
  coder_notes: "Coder's call. P49 used for A only (Socrates D1 pattern). Did not stretch P49 to B from 7.21 silence, human-xing remarks, or Eno naturalization of Tian. RQ O1 / P42 Analects disciples' record unchanged. No fallacy_catalog (Jason). Figures not refreshed."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Kong family of Lu, descended from the Kongs of Song", certainty: 0.5, cites: [{source: S1, locator: "family paragraph ('According to some reports')"}], how_known: "Britannica, hedged."}
  religious_heritage_by_birth: {value: "Late Zhou Tian / ritual religion (context)", certainty: 0.5, cites: [{source: S4, locator: "§3 Theodicy"}, {source: S2, locator: "Mandate of Heaven section"}], how_known: "IEP/SEP Zhou context (0.5)."}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: UNKNOWN, how_known: "No dated lasting contribution (P39)."}
  age_at_first_lasting_contribution: {value: UNKNOWN, how_known: "No dated lasting contribution (P39)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "No dated own text; P49 reconstructions place Tian piety in the adult Analects tradition, years unknown."}
  lio_views_relative_to_major_work: {value: "unclear", certainty: 0.5, cites: [{source: S2, locator: "Heaven passages"}, {source: S4, locator: "§3"}], how_known: "Working views reconstructed for adult teaching life; major work undated (P39)."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "primary_system BELOW_THRESHOLD; A scored only via P49 reconstruction."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "Wrote nothing; teaching is ethical/ritual/political, not geometric demonstration (S1, S2).", certainty: 0.5, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "opening"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Not known."}
  circle_present: {value: "yes", rationale: "Reconstructed Tian as moral/cosmic agent that backs or forsakes persons (S2, S4).", certainty: 0.5, cites: [{source: S2, locator: "Heaven passages"}, {source: S4, locator: "§3"}], how_known: "Lane B reading of P49 reconstructions; not a finding."}
  reading: "Reconstructed Analects Tian piety: intervening Heaven; A 0 @0.5; B UNKNOWN; primary BELOW (CONFUC lead); unplotted."
  notes: "Lane B only. Chart-moving NO."

institutions:
  - {value: "Jisun clan (hereditary chief counselors of Lu)", role: "keeper of granaries and other modest posts", years: UNKNOWN, kind: employer, certainty: 0.7, cites: [{source: S1, locator: "Jisun paragraph"}], how_known: "Britannica."}
collaborators:
  - {value: "Zigong", relation: "student or assistant", note: "early disciple", certainty: 0.7, cites: [{source: S1, locator: "disciples paragraph"}], how_known: "Britannica."}
  - {value: "Zilu", relation: "student or assistant", note: "early disciple", certainty: 0.7, cites: [{source: S1, locator: "disciples paragraph"}], how_known: "Britannica."}
  - {value: "Yan Hui", relation: "student or assistant", note: "favourite disciple", certainty: 0.7, cites: [{source: S1, locator: "disciples paragraph"}], how_known: "Britannica."}

review:
  roster_status_reason: {value: "Core in v8 (F 4).", certainty: 0.7, cites: [{source: S3, locator: "roster.csv, rank 90"}], how_known: "Study roster."}
  controversies:
    - {value: "Analects authorship and layers: compiled by disciples; some sayings appear in other mouths; text fixed only in the second century BCE (S2)", certainty: 0.7, cites: [{source: S2, locator: "Analects sources section"}, {source: S4, locator: "opening"}], how_known: "SEP; IEP."}
    - {value: "Nature of Tian for Confucius: anthropomorphic deity vs naturalized moral-cosmic force (Eno naturalization; IEP fate/nature/deity blend)", certainty: 0.5, cites: [{source: S2, locator: "Heaven passages (Eno)"}, {source: S4, locator: "§3 Theodicy"}], how_known: "Named A alt 1; does not raise certainty above P49 0.5."}
  data_quality_flags:
    - "No own writings; Analects evidence is disciples' reported speech (P42 RQ O1)."
    - "A scored only via scholarly reconstruction (P49), certainty 0.5."
    - "Traditional life dates (c. 551–479 BCE)."
  open_questions:
    - "Settled (RQ O1 / P42): Analects stays disciples' reported speech; does not score alone. P49 path used for A this pass (Socrates D1 precedent)."
    - "Optional: Robert Eno The Confucian Creation of Heaven (1990) monograph pages for a tighter naturalization alt."
    - "Optional: Annping Chin book-length Confucius biography pages beyond the Britannica article."
    - "B remains blocked unless a P16 nature-order reconstruction for historical Confucius appears (unlikely; Heaven-as-agent ≠ nature order)."

sources:
  - id: S1
    type: secondary
    kind: encyclopedia
    author: "Annping Chin"
    citation: "Chin, Annping. \"Confucius.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Confucius. Create-pass body from Wayback snapshot 20260919161320; re-checked 2026-10-24."
    url: "https://www.britannica.com/biography/Confucius"
    accessed: 2026-10-24
    reliability_note: "Signed article. Body only; Top Questions not cited."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, institutions, collaborators]
  - id: S2
    type: secondary
    kind: encyclopedia
    author: "Mark Csikszentmihalyi"
    citation: "Csikszentmihalyi, Mark. \"Confucius.\" Stanford Encyclopedia of Philosophy (substantive revision 2 May 2024). https://plato.stanford.edu/entries/confucius/"
    url: "https://plato.stanford.edu/entries/confucius/"
    accessed: 2026-10-24
    reliability_note: "Signed SEP entry, read directly. Mandate of Heaven / Heaven passages used for P49 A."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, worldview, timing, lane_b, childhood, heritage, review]
  - id: S3
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-17
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S4
    type: secondary
    kind: encyclopedia
    author: "Jeff Richey"
    citation: "Richey, Jeff. \"Confucius (551—479 B.C.E.).\" Internet Encyclopedia of Philosophy. https://iep.utm.edu/confucius/."
    url: "https://iep.utm.edu/confucius/"
    accessed: 2026-10-24
    reliability_note: "Signed IEP entry. §3 Theodicy is the main P49 warrant with S2; opening states scholars can extract views safely attributable to Confucius from the Analects."
    source_quality: "reference entry"
    used_for: [identity, contribution, childhood, worldview, heritage, timing, lane_b, review]
  - id: S5
    type: secondary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "Wikipedia. \"Confucius.\" https://en.wikipedia.org/wiki/Confucius. Read 2026-10-24."
    url: "https://en.wikipedia.org/wiki/Confucius"
    accessed: 2026-10-24
    reliability_note: "Dual-bio second source (P50) for dates/place/names; philosophy section notes Heaven views remained indeterminate — not used alone for A (P49 rests on S2+S4)."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution]
---

# Confucius

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Confucius (trad. 551–479 BCE), Chinese teacher and political theorist [S1; S2; S5]. Deepen D1: primary_system BELOW_THRESHOLD (CONFUC lead; P42 disciples' record); A 0 @0.5 scholarly_reconstruction (alt 1; SEP+IEP P49); B UNKNOWN; mid_basin UNKNOWN. Not plotted. Chart-moving NO.

## Life and work

Lu; fourteen years of travel from 498 BCE; returned 484 BCE [S1]. Traditional dates c. 551–479 BCE [S1; S5].

## Contribution and impact

Teaching transmitted in the Analects, compiled by disciples [S1; S2; S4].

## Childhood and education

Father Shu-liang He died soon after his birth [S1]. Late Zhou Tian / ritual religion as heritage context [S4; S2].

## Adult working worldview

Analects Heaven sayings are reported speech (P42) and do not score alone [S2]. SEP and IEP reconstruct Tian as intervening moral-cosmic power → A 0 @0.5 (P49); named alt 1 naturalized Tian [S2; S4]. B UNKNOWN (no P16 nature-order reconstruction). primary_system BELOW_THRESHOLD with CONFUC lead.

## Heritage (context only)

Kong family of Lu [S1]. Zhou Tian / ritual religion [S4; S2].

## Timing

Undated (P39).

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Reconstructed Tian piety; A 0 @0.5; B UNKNOWN; unplotted [S2; S4].

## Open questions

- P42 Analects settled (RQ O1); P49 used for A.
- Optional Eno 1990 / Chin book pages.
- B blocked without P16 nature-order reconstruction.

## Research log

- 2026-10-17: Read Britannica (Chin, Wayback 20260919161320) and SEP (Csikszentmihalyi) directly.
- 2026-10-24: Deepen D1. Re-read SEP Heaven / Mandate; IEP Richey Theodicy; Wikipedia dual bio. Wrote drafts/deepen_confucius.md (untracked). No figures refresh. No fallacy_catalog.
