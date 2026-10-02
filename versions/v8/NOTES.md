# v8 notes

v8 is in progress. This file tracks what v8 consists of and what is still to do. Decisions are in `docs/OPEN_DECISIONS.md`; all 19 were made on 2026-10-01 and none is open.

## Done

- **Roster rebuilt** from the five raw model lists: 1,380 people, F = number of distinct models. Core 441, provisional 33, review 17; 889 new names (F 1–2) still need a status.
  - Script: `scripts/rebuild_roster.py`. `--check` reproduces the files byte for byte.
  - Diff against v7.1: [`roster_diff_v7_to_v8.md`](roster_diff_v7_to_v8.md).
- **Person ids** for every roster name (`data/roster/person_ids.csv`), with sharded file paths.
- **Schemas, templates and validators** for person and belief-system records (schema 1.1), plus the region table `data/reference/regions.csv`.
- **Belief-system records:** 77 files, carrying the v7.1 scores and notes verbatim. PANT is a cited worked example.
- **Person record:** Michael Faraday, a worked example. Unreviewed.
- **Docs:** METHOD, DATA_DICTIONARY, CODING_GUIDE, RUNBOOK, OPEN_DECISIONS.

## Next

1. First pool records, one per run: Maxwell, Newton, Aquinas, Ibn Sina, Gödel. Score Faraday's LIO axes so the mid-basin test (P4) can be applied to him.
2. Human review of the Faraday and PANT examples.
3. Systems most needed for the first pool: CLASS_THEISM, CLTHEI, CHRIST, ISLAM, JUDA, ATHE, AGNOS.
4. Statuses for the 889 new F 1–2 names, when sensitivity analyses need them (R6).
5. The v8 papers, once enough records exist.
