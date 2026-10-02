# v8 notes

v8 is in progress. This file tracks what v8 consists of and what is still to do. Decisions waiting on Jason are in `docs/OPEN_DECISIONS.md`.

## Done

- **Roster rebuilt** from the five raw model lists: 1,382 people, F = number of distinct models.
  - Script: `scripts/rebuild_roster.py`. `--check` reproduces the files byte for byte.
  - Diff against v7.1: [`roster_diff_v7_to_v8.md`](roster_diff_v7_to_v8.md).
- **Person ids** for every roster name (`data/roster/person_ids.csv`), with sharded file paths.
- **Schemas, templates and validators** for person and belief-system records.
- **Belief-system records:** 77 files, carrying the v7.1 scores and notes verbatim. PANT is a cited worked example.
- **Person record:** Michael Faraday, a worked example. Unreviewed.
- **Docs:** METHOD, DATA_DICTIONARY, CODING_GUIDE, RUNBOOK, OPEN_DECISIONS.

## Next

1. Decisions in OPEN_DECISIONS, especially the LIO scale (P1), mid-basin definition (P4), statuses for new names (R6) and labels (S1, S2).
2. First pool records, one per run: Maxwell, Newton, Aquinas, Ibn Sina, Gödel.
3. Human review of the Faraday and PANT examples.
4. Systems most needed for the first pool: CLASS_THEISM, CLTHEI, CHRIST, ISLAM, JUDA, ATHE, AGNOS.
5. The v8 papers, once enough records exist.
