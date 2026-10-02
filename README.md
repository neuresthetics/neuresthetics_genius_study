# Neuresthetics Genius Study

A study of where remembered genius sits on a scale of lawful, non-intervening order, plus a labeled belief model of how learning that order early might pay off. All versions live here. The version number is a detail, not the name.

**Current version:** v8 (in progress). Until v8 is published, the latest complete release is [v7.1](https://github.com/neuresthetics/neuresthetics_v7).

## What changes in v8

v8 starts by fixing the data in v7.1:

- The genius roster is rebuilt from the five original model lists, which v7.1 didn't fully use. It now has 1,382 people, up from 482.
- Frequency (F) is now the number of distinct models that list a person (1 to 5), so alias counts no longer get added together.
- Each person and each belief system gets its own record, with sources and a certainty grade for every fact.
- The two belief systems that were both labeled "Classical Theism" get separate display names (proposed, pending sign-off).

See [CHANGELOG.md](CHANGELOG.md) for details.

## Repo layout

| Path | What's there |
| :--- | :--- |
| `data/sources/` | Raw inputs, read-only, with checksums: the five model lists and the v7.1 combined JSON. |
| `data/roster/` | The v8 roster (`roster.csv`), alias map, merge log, hand-curated merges, and person ids. |
| `people/` | One Markdown file per person, `people/<first letter>/<id>.md`. |
| `systems/` | One Markdown file per belief system (77), named by the v7.1 code. |
| `schema/` | JSON Schemas for person and system records. |
| `templates/` | Blank person and system records to copy. |
| `scripts/` | Roster rebuild, id assignment, validators, coverage report, data dictionary generator. |
| `docs/` | Method, data dictionary, coding guide, runbook, open decisions. |
| `reports/` | Generated reports (coverage). |
| `versions/` | Per-version notes and the v7.1 → v8 roster diff. |
| `papers/` | v8 papers, once written. |

## How the database grows

One person per run. Each run picks the next person, researches them from primary and scholarly sources, fills their record (leaving `TODO` where nothing is sourced yet), validates it, and commits. Belief-system records are extended the same way. Michael Faraday (`people/f/faraday-michael.md`) and Pantheism (`systems/PANT.md`) are the worked examples.

```bash
pip install -r scripts/requirements.txt
python3 scripts/rebuild_roster.py --check   # roster reproduces from the raw lists
python3 scripts/assign_ids.py --check       # person ids are up to date
python scripts/validate_people.py           # person records
python scripts/validate_systems.py          # belief-system records
python scripts/coverage_report.py           # writes reports/coverage.md
```

## Docs

- [Method](docs/METHOD.md): how the roster, ids and records are built, and why.
- [Data dictionary](docs/DATA_DICTIONARY.md): every file, column and field.
- [Coding guide](docs/CODING_GUIDE.md): the v7.1 coding rules, certainty, worldview codes, LIO axes, and system records.
- [Runbook](docs/RUNBOOK.md): step by step for one person (or system) per run.
- [Open decisions](docs/OPEN_DECISIONS.md): choices waiting on sign-off.
- [Coverage](reports/coverage.md): what exists so far.

## History

Past versions stay in their own repos so their history doesn't change.

> **Content warning: everything before V7.** V5 and V6 use methods that are now retired, including V6's ranking of religions by dividing counts of historical geniuses by 2025 religious population figures. Their results are not findings, and they compare specific faiths in ways the current study no longer does. They're kept only so the path to the current method stays visible.

| Version | Where | Notes |
| :--- | :--- | :--- |
| V5 | [V5 PDF](https://github.com/neuresthetics/neuresthetics_v7/blob/main/V6_(history)/V5/Genius%20Data%20Analysis%20V5%20(as%20dev%20history%20only).pdf) | Content warning. Dev history only. |
| V6 | [NEUR-V6-DATA](https://github.com/neuresthetics/NEUR-V6-DATA) | Content warning. Retired rate-table approach. |
| V7 / V7.1 | [neuresthetics_v7](https://github.com/neuresthetics/neuresthetics_v7) | Two-lane paper, neurology sister paper, data book, combined JSON. |

## Site

[neuresthetic.net](https://neuresthetic.net)
