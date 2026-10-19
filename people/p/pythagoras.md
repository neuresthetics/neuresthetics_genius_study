---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 3
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch W)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-19
  last_updated: 2026-10-19
  change_log:
    - {date: 2026-10-19, by: "Grok Bot", summary: "Audit fixes for batch X (gs_a1ff932_X run 1): (XW3) era_bucket 'before -500' (0.5) -> UNKNOWN: under a strict P39 his adult life (ca. 570–490 BCE) crosses the -500 edge, and P39 has no candidate-year clause (corrects the batch W PY4 advice; Gautama treated alike). Not plotted either way."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Audit fixes for batch W (gs_2584730_W run 1): (PY4) era_bucket 'before -500' 0.7 -> 0.5, how_known based on the candidate years (Croton, ca. 530–510 BCE) under P39, at the certainty of the life dates. (Note) 'forged' wording corrected: SEP says books were forged in his name; the Golden Verses circulated in his name and were later compiled; the Sacred Discourse attribution rests on a misreading. SEP typed tertiary. No scored value changes."}
    - {date: 2026-10-19, by: "Grok Bot", summary: "Record created (stage 3 batch W, order P32: F 4, rank 125). All facts from SEP (Carl Huffman). Pythagoras wrote nothing; everything about his views is later report (doxography), which is reported speech and cannot score alone (P42, CODING_GUIDE §7). Not a scientist (P30): SEP doubts he did mathematics or rational cosmology. primary_system BELOW_THRESHOLD; A, B, C BELOW_THRESHOLD; D, E UNKNOWN; mid_basin BELOW_THRESHOLD. First lasting contribution and span UNKNOWN (undated, P39). Not plotted. Draft, not reviewed."}

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
    date: {value: "-570", calendar: julian, certainty: 0.5, cites: [{source: S1, locator: "opening ('ca. 570'); §3"}], how_known: "SEP: 'ca. 570', inferred from Aristoxenus's report that he left Samos at forty under Polycrates (c. 535). Proleptic Julian."}
    place: {value: "Samos", modern_name: "Samos, Greece", polity_then: "Samos", certainty: 0.7, cites: [{source: S1, locator: "§3 ('there is agreement that he grew up on the island of Samos')"}], how_known: "SEP gives where he grew up; his origin is controversial (S1 §3), so 0.7."}
  death:
    date: {value: "-490", calendar: julian, certainty: 0.5, cites: [{source: S1, locator: "opening ('ca. 490'); §3"}], how_known: "SEP: 'around 490 BCE'."}
    place: {value: "Metapontum", modern_name: "Metaponto, Basilicata, Italy", polity_then: "Metapontum (Greek city in southern Italy)", certainty: 0.5, cites: [{source: S1, locator: "§3"}], how_known: "SEP: 'There are a variety of stories about his death', the most reliable putting it at Metapontum; 0.5."}
  first_lasting_contribution_year: {value: UNKNOWN, how_known: "He wrote nothing and his teaching is undated (P39)."}
  era_bucket: {value: UNKNOWN, how_known: "First-lasting year UNKNOWN (P39). P39 fills era only when every year of the adult life falls in one bucket; his adult life (born ca. 570, died ca. 490 BCE; S1) crosses the -500 edge, so the bucket is UNKNOWN (batch X audit, XW3, correcting the batch W PY4 advice; the Gautama record treats the same case alike). The Croton years (ca. 530–510 BCE, S1 §3) would all fall in 'before -500', but P39 has no candidate-year clause."}
  region_of_birth: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "§3"}], how_known: "Samos, Greece (P3)."}
  region_of_work: {value: "Southern Europe", certainty: 0.7, cites: [{source: S1, locator: "opening; §3"}], how_known: "Croton in southern Italy, where 'most of his philosophical activity occurred' (S1)."}
  sex_as_recorded: {value: "male", certainty: 0.7, cites: [{source: S1, locator: "§3"}], how_known: "As recorded."}
  languages_of_work: {value: ["Ancient Greek"], certainty: 0.5, cites: [{source: S1, locator: "§3"}], how_known: "Coder's reading (0.5); he wrote nothing."}
  occupations: {value: ["teacher of a way of life", "expert on the fate of the soul and religious ritual"], certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "SEP's list of what he was famous for."}

contribution:
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
  family_religion: {value: TODO}
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
  primary_system: {value: BELOW_THRESHOLD, how_known: "He wrote nothing; a large collection of books was later forged in his name and other early Pythagoreans' (S1, opening and §2); the Golden Verses are hexameter lines that circulated in his name by the third century BCE and were later compiled, and the idea that he wrote a Sacred Discourse 'seems to arise from a misreading of the early evidence' (S1 §3). Either way they are not his words (P42). What is known comes from reports: Xenophanes's joke about the puppy (Fr. 7) and Dicaearchus show he taught reincarnation; Aristotle's acusmata show interest in ritual and a moralized cosmos (S1 §4.1, §4.3, §5). Reports cannot score alone (P42, CODING_GUIDE §7; Hippocrates and Confucius precedents). SEP adds that 'Pythagoreanism was not a religion' (S1 §4.3). Leads: HELLEN (Greek ritual and gods), with a reincarnation doctrine no listed code fits."}
  secondary_system: {value: UNKNOWN, how_known: "None (P29)."}
  candidate_codes_considered:
    - {code: HELLEN, reason: "Lead: acusmata on libations and sacrifice to the gods (S1 §4.3); reported only."}
    - {code: PLATO, reason: "Rejected: Platonism comes after him; the later tradition made him the source of Plato's ideas, which SEP calls unhistorical (S1 opening)."}
    - {code: HINDU, reason: "Rejected: reincarnation alone is not a code; no source links him to Indian teaching."}
  lio_axes:
    A_locus: {value: BELOW_THRESHOLD, how_known: "Reported only: in the acusmata 'the planets are the hounds of Persephone', agents of vengeance (Aristotle in Porphyry, S1 §5), a lead toward 0–1 (gods acting in the cosmos). Doxography cannot score alone (P42)."}
    B_cause: {value: BELOW_THRESHOLD, how_known: "Not a scientist (P30): SEP doubts he engaged in rational cosmology or proved the theorem (S1 opening, §5). Reported account of nature: thunder 'is a threat to those in Tartarus' and 'an earthquake is nothing other than a meeting of the dead' (acusmata, S1 §5), a lead toward 1; beside it, heavenly motions perhaps in musical ratios. Reported, so below threshold (P42; Hippocrates precedent)."}
    C_ledger: {value: BELOW_THRESHOLD, how_known: "Reported only: the soul is immortal and reborn, and the sun and moon are 'the Isles of the Blest' where we may go 'if we lived a good life' (S1 §4.1; §5), a lead toward a personal ledger (0–1). Reported speech (P42)."}
    D_authority: {value: UNKNOWN, how_known: "Nothing read (P19)."}
    E_scope: {value: UNKNOWN, how_known: "Nothing read on the world's order (P7, P19)."}
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A and B are BELOW_THRESHOLD; no branch of the P4 test is met."}
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
  coder_notes: "Coder's call, following the Socrates, Hippocrates and Confucius precedents: no text of his own exists (S1 §3), so all worldview fields rest on reports and stay below threshold or UNKNOWN. SEP notes 'recent scholarship' has challenged the consensus view (opening, §5); the record follows the consensus SEP sets out."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Greek of Samos", certainty: 0.7, cites: [{source: S1, locator: "§3"}], how_known: "SEP."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: TODO}
  childhood_catechism: {value: TODO}

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
    - {value: "Whether he was a mathematician or cosmologist at all; recent scholarship challenges the consensus", certainty: 0.7, cites: [{source: S1, locator: "opening; §5"}], how_known: "SEP."}
    - {value: "Forged treatises in his name and the later 'semi-divine' image", certainty: 0.7, cites: [{source: S1, locator: "opening; §3"}], how_known: "SEP."}
  data_quality_flags:
    - "Single source (SEP); every worldview item is doxography."
  open_questions:
    - "Read Burkert (1972) or Huffman's Pythagoreanism entry for any view securely attributable to Pythagoras himself."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Carl Huffman"
    citation: "Huffman, Carl. \"Pythagoras.\" Stanford Encyclopedia of Philosophy (first published 23 February 2005; substantive revision 5 February 2024). https://plato.stanford.edu/entries/pythagoras/"
    url: "https://plato.stanford.edu/entries/pythagoras/"
    accessed: 2026-10-19
    reliability_note: "Signed scholarly encyclopedia entry; quotes the ancient reports in translation."
    used_for: [identity, basics, contribution, childhood, worldview, heritage, timing, lane_b, collaborators, review]
  - id: S2
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-19
    reliability_note: "Study's own roster."
    used_for: [identity, review]
---

# Pythagoras

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Pythagoras of Samos (ca. 570–ca. 490 BCE), Greek teacher of the soul's immortality and of a way of life at Croton [S1]. Draft: everything is reported; primary_system and A–C BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Not plotted.

## Life and work

Samos, then Croton (c. 530 BCE), then Metapontum [S1].

## Contribution and impact

Reincarnation doctrine and the Pythagorean way of life [S1].

## Childhood and education

Not known [S1].

## Adult working worldview

Known only from reports (Xenophanes, Aristotle's acusmata) [S1].

## Heritage (context only)

Greek of Samos [S1].

## Timing

Undated [S1].

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. A moralized cosmos of numbers [S1].

## Open questions

- Securely attributable views.

## Research log

- 2026-10-19: Read SEP (Huffman).
