---
record:
  record_type: person
  schema_version: "1.4"
  record_version: 6
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch W)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-27
  change_log:
    - {date: 2026-10-27, by: "Grok Bot", summary: "Schema 1.4: contribution.era_bucket set to ancient. Coarse band for when the main work landed; not a claim. basics.era_bucket and scores unchanged."}
    - {date: 2026-10-25, by: "Grok Bot", summary: "Perpetual deepen: religious_heritage_by_birth / baptism / catechism / family_religion TODO→UNKNOWN (no explicit birth-religion line; refuse milieu invention). Chart-moving NO."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Audit fixes for batch X (gs_a1ff932_X run 1): (XW3) era_bucket 'before -500' (0.5) -> UNKNOWN: under a strict P39 his adult life (ca. 570–490 BCE) crosses the -500 edge, and P39 has no candidate-year clause (corrects the batch W PY4 advice; Gautama treated alike). Not plotted either way."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Audit fixes for batch W (gs_2584730_W run 1): (PY4) era_bucket 'before -500' 0.7 -> 0.5, how_known based on the candidate years (Croton, ca. 530–510 BCE) under P39, at the certainty of the life dates. (Note) 'forged' wording corrected: SEP says books were forged in his name; the Golden Verses circulated in his name and were later compiled; the Sacred Discourse attribution rests on a misreading. SEP typed tertiary. No scored value changes."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch W, order P32: F 4, rank 125). All facts from SEP (Carl Huffman). Pythagoras wrote nothing; everything about his views is later report (doxography), which is reported speech and cannot score alone (P42, CODING_GUIDE §7). Not a scientist (P30): SEP doubts he did mathematics or rational cosmology. primary_system BELOW_THRESHOLD; A, B, C BELOW_THRESHOLD; D, E UNKNOWN; mid_basin BELOW_THRESHOLD. First lasting contribution and span UNKNOWN (undated, P39). Not plotted. Draft, not reviewed."}
    - {date: 2026-10-24, by: "Grok Bot", summary: "Deepen pass D1 (queue #124 / F4 rank 125). Goals: check SEP/Huffman updates and fragment attribution debates; document leads; keep honest BELOW (Confucius/Hippocrates P42 precedent; no authentic own words expected). Re-read SEP Pythagoras (Huffman; first pub. 2005, substantive revision still 5 Feb 2024 — Fall 2026 archive confirms same revision date, no newer update) and SEP Pythagoreanism (Huffman; substantive revision 5 Mar 2024). Wikipedia EN dual bio (S3, P50): birth ca. 570 Samos agrees; death ca. 495 Wikipedia vs ca. 490 SEP (both approximate). Consensus unchanged: he wrote nothing; Riedweg 2005 attempt to argue books rejected by Huffman 2008a (S1 §3); Golden Verses / Sacred Discourse / pseudo-Pythagorean corpus are forgeries or later compilations, not his words. All worldview evidence remains doxography / reported speech (P42) — Xenophanes Fr. 7, Aristotle acusmata, Dicaearchus VP 19, etc. Did not stretch P49 to lift A/B (standing rule: keep BELOW unless authentic own words). primary_system / A / B / C / mid stay BELOW_THRESHOLD; D/E UNKNOWN; span UNKNOWN (P39); not a scientist (P30). Chart-moving NO. P47 source_quality on S1–S4. No fallacy_catalog. No figures/. Draft, not reviewed."}

identity:
  id: pythagoras
  display_name: "Pythagoras"
  roster:
    canonical_name: "Pythagoras"
    rank: 125
    F: 4
    models: [Claude, DeepSeek, GPT, Grok]
    band: "core (3–4)"
    status: core
    field: mathematics
    field_bucket: mathematics
  full_name: {value: "Pythagoras of Samos", certainty: 0.7, cites: [{source: S1, locator: "opening; §3"}], how_known: "SEP; Heraclitus calls him 'the son of Mnesarchus' (Fr. 129, quoted in S1 §3)."}
  native_name: {value: "Πυθαγόρας", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Greek form; coder's transcription (0.5)."}
  aliases: []

basics:
  birth:
    date: {value: "-570", calendar: julian, certainty: 0.5, cites: [{source: S1, locator: "opening ('ca. 570'); §3"}, {source: S3, locator: "infobox (c. 570 BC)"}], how_known: "SEP 'ca. 570' (Aristoxenus / Polycrates); Wikipedia c. 570 agrees (P50). Proleptic Julian."}
    place: {value: "Samos", modern_name: "Samos, Greece", polity_then: "Samos", certainty: 0.7, cites: [{source: S1, locator: "§3 ('there is agreement that he grew up on the island of Samos')"}], how_known: "SEP gives where he grew up; his origin is controversial (S1 §3), so 0.7."}
  death:
    date: {value: "-490", calendar: julian, certainty: 0.5, cites: [{source: S1, locator: "opening ('ca. 490'); §3"}, {source: S3, locator: "infobox (c. 495 BC)"}], how_known: "SEP 'around 490 BCE'; Wikipedia c. 495. Both approximate (0.5); kept SEP's figure."}
    place: {value: "Metapontum", modern_name: "Metaponto, Basilicata, Italy", polity_then: "Metapontum (Greek city in southern Italy)", certainty: 0.5, cites: [{source: S1, locator: "§3"}], how_known: "SEP: 'There are a variety of stories about his death', the most reliable putting it at Metapontum; 0.5."}
  first_lasting_contribution_year: {value: UNKNOWN, how_known: "He wrote nothing and his teaching is undated (P39)."}
  era_bucket: {value: UNKNOWN, how_known: "First-lasting year UNKNOWN (P39). P39 fills era only when every year of the adult life falls in one bucket; his adult life (born ca. 570, died ca. 490 BCE; S1) crosses the -500 edge, so the bucket is UNKNOWN (batch X audit, XW3, correcting the batch W PY4 advice; the Gautama record treats the same case alike). The Croton years (ca. 530–510 BCE, S1 §3) would all fall in 'before -500', but P39 has no candidate-year clause."}
  region_of_birth: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "§3"}], how_known: "Samos, Greece (P3)."}
  region_of_work: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening; §3"}], how_known: "Croton in southern Italy, where 'most of his philosophical activity occurred' (S1)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "§3"}], how_known: "As recorded."}
  languages_of_work: {value: ["Ancient Greek"], certainty: 0.5, cites: [{source: S1, locator: "§3"}], how_known: "Coder's reading (0.5); he wrote nothing."}
  occupations: {value: ["teacher of a way of life", "expert on the fate of the soul and religious ritual"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP's list of what he was famous for."}

contribution:
  era_bucket: ancient
  fields: {value: ["philosophy (the soul and its fate)", "religious ritual", "number and cosmos (disputed)"], certainty: 0.5, cites: [{source: S1, locator: "opening; §5"}], how_known: "SEP; the mathematical side is disputed (§5)."}
  lasting_original_contributions:
    - {value: "Doctrine of the immortal soul and its reincarnation (metempsychosis)", kind: other, lasting: "'Pythagoras succeeded in promulgating a new more optimistic view of the fate of the soul after death' (S1, opening); attested by his contemporary Xenophanes and 'emphatically confirmed' by Dicaearchus (S1 §4.1)", certainty: 0.7, cites: [{source: S1, locator: "opening; §4.1"}], how_known: "SEP. Undated (P39)."}
    - {value: "The Pythagorean way of life (dietary rules, ritual, self-discipline) and its community of followers", kind: institution, lasting: "'founding a way of life that was attractive for its rigor and discipline and that drew to him numerous devoted followers' (S1, opening); for Plato and Aristotle he was 'the founder of a way of life' (S1 §2.3)", certainty: 0.7, cites: [{source: S1, locator: "opening; §2.3; §4.3"}], how_known: "SEP. Undated (P39)."}
  evidence_of_impact:
    - {value: "The so-called Pythagorean theorem bears his name, though 'it is not likely that he proved the theorem'", kind: "named after them", certainty: 0.7, cites: [{source: S1, locator: "opening; §5"}], how_known: "SEP. Named after him, not shown to be his."}
    - {value: "His cosmos 'was developed in a more scientific and mathematical direction by his successors in the Pythagorean tradition, Philolaus and Archytas'", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}
  major_works: []
  honours: []
  definition_fit: {value: "arguable", rationale: "Famous in his day and after, but for the soul's fate, ritual, wonders and a way of life, not mathematics; the later image of a master mathematician is the 'false glorification' SEP warns against (S1).", certainty: 0.5, cites: [{source: S1, locator: "opening; §5"}], how_known: "Coder's reading of SEP."}

childhood:
  family_religion: {value: UNKNOWN, how_known: "Not stated in sources read."}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father: Mnesarchus", certainty: 0.5, cites: [{source: S1, locator: "§3 (Heraclitus Fr. 129)"}], how_known: "Only from Heraclitus's phrase 'the son of Mnesarchus', quoted by SEP."}
  household_circumstances: {value: TODO}
  schooling: []
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: ["Ancient Greek"], certainty: 0.5, cites: [{source: S1, locator: "§3"}], how_known: "Coder's reading (Samos)."}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: UNKNOWN, how_known: "Equals timing.major_work_period (UNKNOWN, P39)."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "He wrote nothing."}
  primary_system: {value: BELOW_THRESHOLD, how_known: "Deepen D1 reconfirmed: he wrote nothing (S1 §3; S3; S4 §1). Pseudo-Pythagorean books, Golden Verses, and Sacred Discourse attribution are forgeries or later compilations / misreadings — not his words (P42). Riedweg 2005 argued he wrote books; Huffman 2008a rejects (S1 §3). What is known is reports: Xenophanes Fr. 7 and Dicaearchus on metempsychosis; Aristotle's acusmata on ritual and a moralized cosmos (S1 §4–5). Reports cannot score alone (P42; Confucius / Hippocrates deepen precedents). SEP: 'Pythagoreanism was not a religion' (S1 §4.3). Leads: HELLEN (ritual/gods in acusmata), plus reincarnation with no listed code fit. Honest BELOW_THRESHOLD."}
  secondary_system: {value: UNKNOWN, how_known: "None (P29)."}
  candidate_codes_considered:
    - {code: HELLEN, reason: "Lead: acusmata on libations and sacrifice to the gods (S1 §4.3); reported only — cannot score alone (P42).", cites: [{source: S1, locator: "§4.3"}]}
    - {code: PLATO, reason: "Rejected: Platonism comes after him; later tradition made him the source of Plato's ideas — unhistorical (S1 opening; S4 §4 Neopythagoreanism).", cites: [{source: S1, locator: "opening"}, {source: S4, locator: "§4"}]}
    - {code: HINDU, reason: "Rejected: reincarnation alone is not a code; no source links him to Indian teaching."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "Deepen D1: still reported only. Acusmata 'the planets are the hounds of Persephone' (Aristotle in Porphyry, S1 §5) is a lead toward 0–1 (gods acting in the cosmos). No authentic own words; doxography cannot score alone (P42). Did not stretch P49 scholarly_reconstruction to lift A (standing rule for this deepen: keep BELOW unless authentic own words — Confucius/Hippocrates path when nothing attributable).", note: "Lead 0–1 remains; Zhmud challenges some cosmological acusmata but that debate is still report-vs-report, not own voice."}
    B_cause: {value: BELOW_THRESHOLD, how_known: "Not a scientist (P30): SEP still doubts he engaged in rational cosmology or proved the theorem (S1 opening, §5; S4). Reported nature: thunder 'is a threat to those in Tartarus'; earthquake 'a meeting of the dead' (acusmata, S1 §5) — lead toward 1; musical ratios of heavenly motions reported beside it. All reported → BELOW_THRESHOLD (P42; Hippocrates deepen precedent). Named alt: still nothing attributable that would open P35 working-science scoring."}
    C_ledger: {value: BELOW_THRESHOLD, how_known: "Reported only: immortal/reborn soul; sun and moon as 'Isles of the Blest' for a good life (S1 §4.1; §5) — lead toward personal ledger 0–1. Reported speech (P42)."}
    D_authority: {value: UNKNOWN, how_known: "Nothing attributable on revelation vs observation (P19)."}
    E_scope: {value: UNKNOWN, how_known: "Nothing attributable on the world's order for groups (P7, P19)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A and B are BELOW_THRESHOLD; no branch of the P4 test is met. Deepen D1 did not darken."}
  statements:
    - text: "once when he [Pythagoras] was present at the beating of a puppy, he pitied it and said 'stop, don't keep hitting him, since it is the soul of a man who is dear to me, which I recognized, when I heard it yelping'"
      cites: [{source: S1, locator: "§4.1 (Xenophanes Fr. 7)"}]
      date: "-500"
      context: "Xenophanes, his contemporary, mocking the doctrine of reincarnation."
      axes: [C_ledger]
      kind: "reported speech"
      verified_against: "secondary quotation"
      verified_on: 2026-10-19
      note: "SEP's translation. A hostile contemporary's anecdote; scores nothing (P42). Date is the coder's rough placing of Xenophanes (ca. 570–475 BCE, S1 §3)."
  changes_over_life: []
  coder_notes: "Deepen D1 (2026-10-24). P42 path (Confucius / Hippocrates): no authentic own words → keep A/B/C/primary BELOW. SEP Pythagoras revision date unchanged (5 Feb 2024). Attribution debate documented: Riedweg 2005 (books) rejected by Huffman 2008a; Zhmud challenges Burkert consensus on math/cosmos but still supplies no own text. Pseudo-Pythagorean corpus and Golden Verses are not his. Did not use P49 to lift A from acusmata reconstructions (unlike Confucius Tian D1) — brief required honest BELOW. Chart unplotted. No fallacy_catalog."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Greek of Samos", certainty: 0.7, cites: [{source: S1, locator: "§3"}], how_known: "SEP."}
  religious_heritage_by_birth: {value: UNKNOWN, how_known: "Not stated; Samos Archaic Greek cult milieu is not coded as scored heritage without an explicit source line (cf. Aristotle UNKNOWN)."}
  baptism_or_initiation: {value: UNKNOWN, how_known: "No initiation record opened for birth household (Pythagorean initiation is adult/school, not birth-heritage)."}
  childhood_catechism: {value: UNKNOWN, how_known: "No childhood catechism curriculum named."}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: UNKNOWN, how_known: "Undated (P39). He was active at Croton from c. 530 BCE until the violence of c. 510 BCE (S1 §3), but no contribution is dated."}
  age_at_first_lasting_contribution: {value: UNKNOWN, how_known: "Undated (P39)."}
  first_evidence_of_lio_type_views: {value: UNKNOWN, how_known: "None attributable."}
  lio_views_relative_to_major_work: {value: "no LIO-type views found", certainty: 0.5, cites: [{source: S1, locator: "§4"}], how_known: "None attributable."}
  worldview_during_major_work: {value: UNKNOWN, how_known: "Not attributable."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "unclear", rationale: "He 'valued relationships between numbers' (S1), but proofs are not his.", certainty: 0.5, cites: [{source: S1, locator: "opening; §5"}], how_known: "Coder's reading."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "§3"}], how_known: "Not known."}
  circle_present: {value: "unclear", rationale: "A cosmos 'structured according to moral principles and significant numerical relationships' (S1) is reported, not his text.", certainty: 0.5, cites: [{source: S1, locator: "opening"}], how_known: "Coder's reading."}
  reading: "A moralized cosmos of numbers, souls and punishment, known only from reports."
  notes: ""

institutions: []
collaborators:
  - {value: "Philolaus", relation: influenced, note: "later Pythagorean who developed the cosmos mathematically", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}
  - {value: "Archytas", relation: influenced, note: "later Pythagorean", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP."}
  - {value: "Xenophanes", relation: "rival or critic", note: "contemporary who mocked his doctrine of reincarnation (Fr. 7)", certainty: 0.7, cites: [{source: S1, locator: "§4.1"}], how_known: "SEP."}
  - {value: "Heraclitus", relation: "rival or critic", note: "called his wisdom 'polymathy, an evil conspiracy' (Fr. 129)", certainty: 0.7, cites: [{source: S1, locator: "§3"}], how_known: "SEP."}

review:
  roster_status_reason: {value: "Core in v8 (F 4); v7 kept him core despite debated historicity (OPEN_DECISIONS R6 note).", certainty: 0.7, cites: [{source: S2, locator: "roster.csv, rank 125"}], how_known: "Study roster."}
  controversies:
    - {value: "Whether he was a mathematician or cosmologist at all; Zhmud and others challenge the Burkert/Huffman consensus that he was mainly a religious/way-of-life figure", certainty: 0.7, cites: [{source: S1, locator: "opening; §5"}, {source: S4, locator: "§2–3"}], how_known: "SEP Pythagoras and Pythagoreanism."}
    - {value: "Forged treatises in his name, Golden Verses compilation, and the later 'semi-divine' Neopythagorean image", certainty: 0.7, cites: [{source: S1, locator: "opening; §3"}, {source: S4, locator: "§4.2"}], how_known: "SEP."}
    - {value: "Riedweg (2005) argued he wrote books; Huffman (2008a) rejects — consensus remains that he wrote nothing", certainty: 0.7, cites: [{source: S1, locator: "§3"}, {source: S3, locator: "Life ('No authentic writings… have survived')"}], how_known: "SEP; Wikipedia."}
  data_quality_flags:
    - "Every worldview item is doxography / reported speech (P42); no authentic text."
    - "Death year approximate: SEP ca. 490 vs Wikipedia c. 495."
  open_questions:
    - "Settled for scoring: he wrote nothing; Riedweg writing claim rejected (Huffman 2008a). Keep BELOW unless a securely attributed own text appears (none expected)."
    - "Optional deeper secondary: Burkert Lore and Science (1972) page-check; Zhmud Pythagoras and the Early Pythagoreans (2012) for the challenge to Burkert — still will not yield own words."
    - "Philolaus / Archytas are separate roster candidates if/when collected; do not back-score Pythagoras from their fragments."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Carl Huffman"
    citation: "Huffman, Carl. \"Pythagoras.\" Stanford Encyclopedia of Philosophy (first published 23 February 2005; substantive revision 5 February 2024). https://plato.stanford.edu/entries/pythagoras/"
    url: "https://plato.stanford.edu/entries/pythagoras/"
    accessed: 2026-10-24
    reliability_note: "Signed scholarly encyclopedia entry; quotes ancient reports in translation. Deepen D1: Fall 2026 archive confirms substantive revision still 5 Feb 2024 (no newer update)."
    source_quality: "reference entry"
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, collaborators, review]
  - id: S2
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    source_quality: "study roster"
    used_for: [identity, review]
  - id: S3
    type: tertiary
    kind: encyclopedia
    author: "Wikipedia contributors"
    citation: "\"Pythagoras.\" Wikipedia. https://en.wikipedia.org/wiki/Pythagoras."
    url: "https://en.wikipedia.org/wiki/Pythagoras"
    accessed: 2026-10-24
    reliability_note: "P50 dual bio: birth c. 570 Samos agrees with SEP; death c. 495 vs SEP ca. 490 (both approximate). States 'No authentic writings of Pythagoras have survived.' Not used alone to score worldview (P42)."
    source_quality: "reference entry"
    used_for: [basics, review]
  - id: S4
    type: tertiary
    kind: encyclopedia
    author: "Carl Huffman"
    citation: "Huffman, Carl. \"Pythagoreanism.\" Stanford Encyclopedia of Philosophy (first published 29 March 2006; substantive revision 5 March 2024). https://plato.stanford.edu/entries/pythagoreanism/"
    url: "https://plato.stanford.edu/entries/pythagoreanism/"
    accessed: 2026-10-24
    reliability_note: "Companion SEP entry: Pythagoras vs so-called Pythagoreans (Philolaus, Archytas); Neopythagorean forgeries; who counts as Pythagorean. Confirms no authentic Pythagoras text; mathematical cosmology belongs mainly to later Pythagoreans."
    source_quality: "reference entry"
    used_for: [worldview, review, collaborators]
---

# Pythagoras

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Pythagoras of Samos (ca. 570–ca. 490 BCE), Greek teacher of the soul's immortality and of a way of life at Croton [S1; S3]. Deepen D1: he wrote nothing; all evidence is doxography (P42). primary_system and A–C BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD; span UNKNOWN (P39); not a scientist (P30). Not plotted. Chart-moving NO.

## Life and work

Samos, then Croton (c. 530 BCE), then Metapontum [S1; S3].

## Contribution and impact

Reincarnation doctrine and the Pythagorean way of life [S1]. Mathematical/scientific image is later glorification; Philolaus and Archytas developed the mathematical side [S1; S4].

## Childhood and education

Not known [S1].

## Adult working worldview

Known only from reports (Xenophanes Fr. 7; Aristotle's acusmata; Dicaearchus) [S1]. Pseudo-Pythagorean books and Golden Verses are not his [S1; S4]. Honest BELOW on A/B/C/primary (P42).

## Heritage (context only)

Greek of Samos [S1]. Context only.

## Timing

Undated; first lasting contribution and major_work_period UNKNOWN (P39) [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. A moralized cosmos of numbers, known only from reports [S1].

## Open questions

- Optional Burkert / Zhmud page-checks (will not yield own words).
- Philolaus / Archytas as separate persons if collected.

## Research log

- 2026-10-19: Read SEP Pythagoras (Huffman).
- 2026-10-24: Deepen D1. Re-read SEP Pythagoras (revision still 5 Feb 2024) and SEP Pythagoreanism (5 Mar 2024); Wikipedia EN dual bio. Attribution: Riedweg writing claim rejected; consensus wrote nothing. Kept honest BELOW. Wrote drafts/deepen_pythagoras.md (untracked).
