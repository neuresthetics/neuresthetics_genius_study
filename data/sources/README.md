# data/sources

Raw inputs. Treat everything here as read-only. If a source ever has to change, add a new file next to it and say why in `CHANGELOG.md`; don't edit these in place.

| Path | What it is | Where it came from |
| :--- | :--- | :--- |
| `model_lists/geniiClaude.csv` | Claude's list (`name,field`), 374 rows | `V6_(history)/V6/GeniiLists/` in [neuresthetics_v7](https://github.com/neuresthetics/neuresthetics_v7), commit `220e18e` |
| `model_lists/geniiDeepSeek.csv` | DeepSeek's list, 997 rows | same |
| `model_lists/geniiGemini.csv` | Gemini's list, 669 rows | same |
| `model_lists/geniiGPT.csv` | ChatGPT's list, 376 rows | same |
| `model_lists/geniiGrok.csv` | Grok's list, 330 rows | same |
| `v7_1/geniiAggregateSortFreq.csv` | The 500-row v7 aggregate. Kept only so the rebuild script can show where the v7 numbers came from. Not a source of truth. | same folder |
| `v7_1/neuresthetics_v7_combined.json` | v7.1 combined JSON: two-lane paper, neurology sister paper, data book (all tables). The rebuild reads the v7.1 roster (table 6) and merges/exclusions (table 7). The system stubs were made from table 4 and data book section 7. | repo root of neuresthetics_v7, commit `220e18e` |

`SHA256SUMS` has a checksum for each file. To check them:

```bash
cd data/sources && sha256sum -c SHA256SUMS
```

The five model lists were made once, in the V6 period, by asking each model for a list of geniuses. They aren't re-generated. They're the fixed starting point for every roster build. See `docs/METHOD.md`.
