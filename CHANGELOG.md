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
- **Statuses:** v7.1 statuses are carried over (core 431, provisional 33, review 17). Georgia O'Keeffe, blank in v7.1, is core by decision R1 (`data/roster/status_overrides.csv`), so core is 432. The 898 new names have `new — needs status`. None were invented.
- **Why v7 frequencies were wrong** (confirmed by reproducing the v7 aggregate 500/500):
  1. Claude's list was never read.
  2. Rows were counted, not models.
  3. Hyphens and accents were deleted rather than normalized.
  4. The aggregate was truncated at 500 rows, which dropped Hegel, Cantor, Boltzmann, Babbage, Rawls, Dijkstra and John Nash, among others.
  5. A 0.9 fuzzy merge joined Arthur Schlesinger Sr. and Jr. (and Kolmogorov spellings, which are now merged explicitly).
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
- **Labels:** CLTHEI → "Interventionist personal theism" (proposed, pending sign-off). PANT uses the full V6 label (approved 2026-10-01, S2).
- **Docs:** METHOD, DATA_DICTIONARY (field tables generated from the schemas), CODING_GUIDE (v7.1 coding rules verbatim), RUNBOOK, OPEN_DECISIONS.
- **Reports:** `reports/coverage.md` from `scripts/coverage_report.py`.

### Open

Decisions that need sign-off are listed in `docs/OPEN_DECISIONS.md`: the LIO 0–4 scale, era buckets, regions, the mid-basin definition, statuses for new names, field buckets, the CLTHEI label and more.

- **2026-10-01:** each of the 19 open items in `docs/OPEN_DECISIONS.md` now has an agent recommendation with evidence, plus a summary table at the top. All items stay open, and no roster or system data was changed. The full PANT label ("Pantheism (Spinozistic/naturalistic 'God = Universe')") was found in the V6 history (`beliefCoherence.json`). Field-bucket evidence for R7 is in `reports/r7_bucket_spotcheck.csv` and `reports/r7_field_string_review.csv`. Faraday's 1844 exclusion is updated (record version 2): the reason (a church-discipline dispute) and the few-week duration come from Cantor 2020 and Brooke 1991, and the restoration is confirmed in Gladstone 1873. The exact readmission date is still open.
- **2026-10-01, decisions R1–R5 and S2** (approved by Jason, applied through the pipeline inputs and a rebuild):
  - R1: Georgia O'Keeffe is core, set in the new input `data/roster/status_overrides.csv`;
  - R2: Orville and Wilbur Wright are excluded with the Wright Brothers collective (`exclude` rows; ids retired);
  - R3: "Brian-Maynard-Smith" (GPT) displays as John Maynard Smith (`display_fix`; new id `maynard-smith-john`);
  - R4: the four merges are marked `confirmed`;
  - R5: the three similarity pairs are `separate` rows marked `confirmed`, so the scan no longer lists them;
  - S2: PANT `display_label` is the full V6 label, `label_status` approved.
  - Roster: 1,382 → 1,380 people; F = 2: 185 → 183; F = 5, 3–4 and 1 unchanged (82, 149, 966). `rebuild_roster.py` now reads `status_overrides.csv` and its diff text follows the inputs.

## v7.1 (2026-09-14 data freeze)

- Published in [neuresthetics_v7](https://github.com/neuresthetics/neuresthetics_v7).
