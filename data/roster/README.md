# data/roster

The roster: one row per person, built from the five model lists. `scripts/rebuild_roster.py` writes three of the files here. The other three are maintained by hand or by `scripts/assign_ids.py`.

| File | Written by | What it is |
| :--- | :--- | :--- |
| `roster.csv` | `rebuild_roster.py` | One row per person (1,380 in v8). Rank, name, field, F, models, status, v7 comparison. Columns are listed in `docs/DATA_DICTIONARY.md`. |
| `alias_map.csv` | `rebuild_roster.py` | Every raw name string per model, mapped to its canonical name, with the rule and confidence. Also has keep-separate rows and flag rows. |
| `merge_log.csv` | `rebuild_roster.py` | Every merge, same-model duplicate, exclusion, and "not merged, review suggested" pair. |
| `curated_aliases.csv` | by hand | The hand decisions the rebuild reads: `merge`, `separate`, `exclude`, `flag`, `display_fix`. To change a merge, edit this file and re-run. |
| `status_overrides.csv` | by hand | Statuses set by a recorded decision (name, status, decision id, date, reason). They win over the v7.1 carry-over. |
| `person_ids.csv` | `assign_ids.py` | Stable person id, slug, shard, and file path for every roster name. Append-only: a name that leaves the roster keeps its row with status `retired`. |
| `id_overrides.csv` | by hand | Ids that the slug rule would get wrong (family name written first, compound family names). |

Rebuild and check:

```bash
python3 scripts/rebuild_roster.py --check   # rebuilds in a temp dir and compares byte-for-byte
python3 scripts/assign_ids.py --check       # person_ids.csv matches roster.csv
```

Don't hand-edit `roster.csv`, `alias_map.csv` or `merge_log.csv`. Change the inputs (`curated_aliases.csv`, `status_overrides.csv`, or the script) and rebuild, so every change can be reproduced.
