# Changelog

## v8 (in progress)

### Roster

The roster is rebuilt from the five raw model lists (`scripts/rebuild_roster.py`; `--check` reproduces it byte for byte).

- **1,380 people** (v7.1: 482). 898 added, 0 dropped. Every v7.1 person is found and kept. (1,382 and 900 before the 2026-10-01 decisions below.)
- **F distribution:** F = 5: 82; F = 3–4: 149 (F = 4: 55, F = 3: 94); F = 2: 183; F = 1: 966. F is now the number of distinct models (1–5), so values above 5 no longer occur.
- **Inputs and merges:**
  - 2,746 raw rows, which reduce to 1,416 distinct names after formatting normalization;
  - 32 curated merges, plus 26 keep-separate rows, 27 display fixes and no flags (`data/roster/curated_aliases.csv`);
  - 4 excluded keys (Wright Brothers as a collective, plus Orville and Wilbur Wright listed individually; Anderson localization);
  - no fuzzy merging.
- **Statuses:** v7.1 statuses are carried over (core 431, provisional 33, review 17). Georgia O'Keeffe, blank in v7.1, is core by decision R1 (`data/roster/status_overrides.csv`), so core is 432. The 9 new names with F ≥ 3 are core by decision R6 (same file), so core is 441. The other 889 new names have `new — needs status`. None were invented. Totals: core 441, provisional 33, review 17, new — needs status 889.
- **Why v7 frequencies were wrong** (confirmed by reproducing the v7 aggregate 500/500):
  1. Claude's list was never read.
  2. Rows were counted, not models.
  3. Hyphens and accents were deleted rather than normalized.
  4. The aggregate was truncated at 500 rows, which dropped Hegel, Cantor, Boltzmann, Babbage, Rawls, Dijkstra and John Nash, among others.
  5. A 0.9 fuzzy merge joined Arthur Schlesinger Sr. and Jr. (and Kolmogorov spellings, which are now merged explicitly).
- **Field buckets:** keyword rules in `rebuild_roster.py` (21 buckets), with six fixes from decision R7. 31 rows changed bucket (`reports/r7_bucket_changes.csv`). To compare with v7.1, v8's "politics / law / military" maps to v7.1's "social science / politics".
- **Changes against v7.1:** see `versions/v8/roster_diff_v7_to_v8.md`.

### New layout and databases

- `data/sources/`: read-only raw inputs with checksums. `data/roster/`: roster, alias map, merge log, curated merges, person ids and id overrides.
- **Person ids**: a stable family-name-first slug for each of the 1,380 roster names (`scripts/assign_ids.py`), with 30 hand overrides. Three ids from the first run are retired, not deleted. Files are sharded by the first letter of the id (`people/<shard>/<id>.md`).
- **Person records**: JSON Schema, template and validator. Every fact is a claim with value, certainty (1.0 / 0.7 / 0.5), citations with locators, and a how_known note. The sentinels are TODO / UNKNOWN / BELOW_THRESHOLD. The sections are:
  - identity (checked against the roster)
  - basics
  - contribution
  - childhood
  - adult working worldview (codes, LIO axes, verbatim statements)
  - heritage (context only)
  - timing
  - Lane B (labeled belief model)
  - institutions
  - collaborators
  - review
  - sources
- **Worked example:** Michael Faraday (unreviewed). Worldview codes and Lane B fields are left TODO.
- **Belief-system records:** 77 files (`systems/<CODE>.md`) with schema, template and validator.
  - Each carries the v7.1 rubric scores and scoring note verbatim, labelled "authorial v7.1 scores" and checked against the data book.
  - Each has a slot for revised scores and fields for metaphysics, LIO axes, schools and variants, science, practice, adherents (context only), coding guidance and sources.
  - 76 are stubs. PANT is a cited worked example (unreviewed).
- **Labels:** CLTHEI → "Interventionist personal theism" (approved 2026-10-01, S1). PANT uses the full V6 label (approved 2026-10-01, S2).
- **Reference data:** `data/reference/regions.csv`, the country-to-region table for `region_of_birth` (UN M49, decision P3).
- **Docs:** METHOD, DATA_DICTIONARY (field tables generated from the schemas), CODING_GUIDE (v7.1 coding rules verbatim), RUNBOOK, OPEN_DECISIONS.
- **Reports:** `reports/coverage.md` from `scripts/coverage_report.py`.

### Decisions

All 19 items in `docs/OPEN_DECISIONS.md` were decided by Jason on 2026-10-01. None is open. The entries below are in order.

- **2026-10-01:** each of the 19 open items in `docs/OPEN_DECISIONS.md` now has an agent recommendation with evidence, plus a summary table at the top. All items stay open, and no roster or system data was changed. The full PANT label ("Pantheism (Spinozistic/naturalistic 'God = Universe')") was found in the V6 history (`beliefCoherence.json`). Field-bucket evidence for R7 is in `reports/r7_bucket_spotcheck.csv` and `reports/r7_field_string_review.csv`. Faraday's 1844 exclusion is updated (record version 2): the reason (a church-discipline dispute) and the few-week duration come from Cantor 2020 and Brooke 1991, and the restoration is confirmed in Gladstone 1873. The exact readmission date is still open.
- **2026-10-01, decisions R1–R5 and S2** (approved by Jason, applied through the pipeline inputs and a rebuild):
  - R1: Georgia O'Keeffe is core, set in the new input `data/roster/status_overrides.csv`;
  - R2: Orville and Wilbur Wright are excluded with the Wright Brothers collective (`exclude` rows; ids retired);
  - R3: "Brian-Maynard-Smith" (GPT) displays as John Maynard Smith (`display_fix`; new id `maynard-smith-john`);
  - R4: the four merges are marked `confirmed`;
  - R5: the three similarity pairs are `separate` rows marked `confirmed`, so the scan no longer lists them;
  - S2: PANT `display_label` is the full V6 label, `label_status` approved.
  - Roster: 1,382 → 1,380 people; F = 2: 185 → 183; F = 5, 3–4 and 1 unchanged (82, 149, 966). `rebuild_roster.py` now reads `status_overrides.csv` and its diff text follows the inputs.
- **2026-10-01, alias_map labels** (approved by Jason): display fixes that change the name itself, not just its formatting, now get rule `name_correction` in `alias_map.csv` and `merge_log.csv`, with the curated row's reason and confidence. Before, all of them read `format` / "differs only in spacing…". 6 of the 27 display-fix rows are name corrections (Brian-Maynard-Smith → John Maynard Smith, Lee-Smolins → Lee Smolin, Albert Hofman → Albert Hofmann, Gabriel Marcell → Gabriel Marcel, Gabriel Mistral → Gabriela Mistral, Tenzin Gyatso-Dalai Lama → Tenzin Gyatso (14th Dalai Lama)); 21 stay `format`. Labels only: people, counts and ids are unchanged.

- **2026-10-01, the remaining 13 decisions** (decided by Jason at 10:55 PM PT; applied through the pipeline inputs, the schemas and the docs, then rebuilt):
  - R6: the 9 new names with F ≥ 3 are core, Vint Cerf included (`status_overrides.csv`). Core 432 → 441; new — needs status 898 → 889.
  - R7: the keyword rules stay, with six fixes: science studies with philosophy → philosophy; explor/astronaut wins over space; political thought and social thought → politics / law / military; David Harvey → social science; Jan Swammerdam → biology. 31 rows changed `field_bucket`, 4 of them F ≥ 3 (Mandela, Machiavelli, Gandhi, King). List: `reports/r7_bucket_changes.csv`.
  - R8: the id freeze rule is approved as written; retired ids stay in `person_ids.csv` (METHOD §3.2).
  - P1: the LIO 0–4 scale is approved. The PANT scores (all 4) were rechecked and stand.
  - P2: era buckets approved, keyed on first lasting contribution. An edge year goes to the later bucket (1950 is in "1950 on"). Birth year stays in the record.
  - P3: regions approved, with the new table `data/reference/regions.csv` (247 countries and areas from UN M49). MENA = Northern Africa + Western Asia + Iran; Afghanistan stays South Asia. `validate_people.py` now checks that the table's regions match the schema list exactly and that no country appears twice.
  - P4: the mid-basin test is A_locus ≤ 1 and B_cause ≥ 3 (B for the domain of the work), both at certainty ≥ 0.7. Deists pass; METHOD §1.1 states this as a consequence, with no exclusion. Faraday's `mid_basin` stays TODO until his axes are scored.
  - P5: only a named human sets `reviewed`.
  - S1: the CLTHEI label is approved.
  - S3: the v7.1 rubric scores are a frozen baseline; revised scoring opens after the first pool, with cites per axis and two scorers (METHOD §5.1, system schema).
  - S4: the 77 codes are closed for v8; new codes go in one batch with one schema bump (METHOD §5.1, system schema, RUNBOOK).
  - S5: CLTHEI and CLASS_THEISM relate as "neighbor (easily confused)".
  - S6: PANT boundary rules (two-part test; Advaita and Kabbalah default to the host tradition; Stoics are STOIC) in the coding guidance of PANT, ATHE, STOIC and PANENT, and in CODING_GUIDE §5.
  - **Schema versions:** `person.schema.json` and `system.schema.json` go from 1.0 to 1.1. Only descriptions changed (P1–P5, S3–S5); no field, type or enum changed. Both templates, `make_system_stubs.py`, the 76 stubs, PANT (record version 4) and Faraday (record version 3) are at 1.1. The stubs changed by S1, S5 and S6 (CLTHEI, CLASS_THEISM, ATHE, STOIC, PANENT) are at record version 2.
  - PROPOSED is gone from the schemas, templates, DATA_DICTIONARY, CODING_GUIDE and METHOD. `label_status` still allows `proposed — pending Jason's OK` for future label changes.
  - No person id changed.

### System records (drafts)

Sourced drafts of the systems the first-pool people are most likely to be coded under. v7.1 scores and notes unchanged; LIO axes on the 0–4 scale (P1); every quotation checked word for word against the fetched source page. All `draft — unreviewed`.

- **2026-10-01, CLASS_THEISM** (record version 3): filled from 11 SEP entries. LIO A 1 (0.7), B 3 (0.7), C 2 (0.5), D 2 (0.7), E 3 (0.5). Flags: the v7.1 note lists Aristotle (ARIST by the founders rule; no creation ex nihilo) and Leibniz (unchecked).
- **2026-10-01, CLTHEI** (record version 3): filled from 6 SEP entries and Britannica "Theism" and "Deism". LIO A 0 (1.0), B 1 (0.7), C 1 (0.5), D 1 (0.5), E 1 (0.7). Flag: the v7.1 note blames the problem of evil, which SEP treats as a problem for traditional theism as a whole, CLASS_THEISM included.
- **2026-10-01, CHRIST** (record version 2): filled from 4 SEP entries, the multi-author Britannica "Christianity" article (11 pages) and Pew Research Center (2025, adherents only). Catholic, Orthodox, Protestant, mystical, fundamentalist and integration wings described. LIO A 0 (0.7), B 1 (0.5), C 1 (0.5), D 1 (0.5), E 1 (0.5). Flag: SEP describes mostly integration, not conflict, in the scholarly literature; the v7.1 note stresses revelation over evidence.
- **2026-10-01, ISLAM** (record version 2): filled from 6 SEP entries, the multi-author Britannica "Islam" article (11 pages), Britannica "Salat" and Pew Research Center (2025, adherents only). Sunni (Ashʿarite, Māturīdite), Shiʿi, Muʿtazilite, falsafa, Sufi and modern reform wings described. LIO A 0 (0.7), B 1 (0.5), C 0 (0.7), D 1 (0.5), E 1 (0.5). Flag: SEP describes a long period of Islamic scientific leadership and questions the theology-caused-decline story; the v7.1 note stresses revelation over evidence.
- **2026-10-01, DEISM** (record version 2): filled from Britannica "Deism" (D. A. Pailin, 2 pages) and 7 SEP entries (Enlightenment, Samuel Clarke, God and Other Ultimates, Religion and Science, Paine, Jefferson, Collins). English, French, German, American and stark modern forms described; coding guidance notes that deists usually pass (METHOD §1.1). LIO A 1 (0.7), B 3 (0.7), C 2 (0.5), D 3 (0.7), E 3 (0.7). Flags: Britannica says the stark non-interfering view was held by very few deists; SEP and Britannica both say Newton was not a deist.
- **2026-10-01, STOIC** (record version 3): filled from 5 SEP entries (Stoicism, Pantheism, Seneca, Epictetus, Marcus Aurelius), IEP "Stoicism" and Britannica "Stoicism" (J. L. Saunders). S6 coding rule and PANT neighbor kept. LIO A 3 (0.5), B 4 (0.7), C 3 (0.5), D 3 (0.7), E 4 (0.7). Flag: IEP says Stoic natural study was subordinate to ethics and included divination, a weaker empirical tie than the v7.1 note suggests.
- **2026-10-01, JUDA** (record version 2): filled from 3 SEP entries (Religion and Science, Maimonides, Petitionary Prayer), the multi-author Britannica "Judaism" article (9 pages) and Pew Research Center (2025, adherents only). Rabbinic, medieval philosophical, Kabbalistic and Hasidic, Orthodox, Reform, Conservative and Reconstructionist forms described; Kabbalah coded per S6. LIO A 0 (0.7), B 1 (0.5), C 1 (0.5), D 1 (0.5), E 1 (0.5). Flag: SEP describes non-literal rabbinic reading and an explicit Reform anti-conflict view, a more open picture than the v7.1 note.
- **2026-10-01, PLATO** (record version 2): filled from 6 SEP entries (plato, plato-timaeus, plotinus, cambridge-platonists, god-ultimates, platonism), IEP Plato and Britannica Platonism (9 pages). Covers the Academy, Middle Platonism, Neoplatonism, Christian and Islamic Platonism and the Cambridge Platonists. v7.1 label, scores and note kept verbatim. LIO A 2 (0.5), B 3 (0.7), C 2 (0.5), D 2 (0.5), E 3 (0.7). Flag: mathematical platonism (Gödel) is not by itself PLATO.

### People

- **2026-10-02, James Clerk Maxwell** (`people/m/maxwell-james-clerk.md`, draft — unreviewed): new person record from his letters, essays and 1873 "Molecules" lecture (via Campbell and Garnett 1882 and the 1890 Scientific Papers), Britannica, MacTutor and Hutchinson. Primary system CHRIST (0.7). A_locus 0 and B_cause 3 (physics) at 1.0, so `mid_basin` is true under P4; C_ledger 1 and D_authority 2 at 0.7; E_scope TODO. Quotes checked word for word against the fetched texts.
- **2026-10-02, Isaac Newton** (`people/n/newton-isaac.md`, draft — unreviewed): new person record from the General Scholium, Opticks Query 31, the Principia's Rules of Reasoning, two letters to Bentley and three private theological manuscripts (Newton Project), plus Britannica, MacTutor and two SEP entries. Primary system CHRIST (0.7), CLTHEI a close second. A_locus 1, B_cause 3 (natural philosophy) and E_scope 3 at 1.0, so `mid_basin` is true under P4; C_ledger 0 and D_authority 2 at 0.7. Quotes checked word for word against the fetched texts.
- **2026-10-02, Thomas Aquinas** (`people/a/aquinas-thomas.md`, draft — unreviewed): new person record from thirteen questions of the Summa theologiae (1920 English Dominican translation, New Advent), Britannica (Chenu), SEP (Pasnau) and IEP (Brown). Primary system CLASS_THEISM (1.0). A_locus 1, B_cause 2, C_ledger 1, D_authority 1, E_scope 2, all at 1.0 from written profession. `mid_basin` UNKNOWN: P4 has no branch for B_cause = 2 at high certainty (flagged as an open question). Quotes checked word for word against the fetched texts.

## v7.1 (2026-09-14 data freeze)

- Published in [neuresthetics_v7](https://github.com/neuresthetics/neuresthetics_v7).
