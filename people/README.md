# people/

One file per person: `people/<shard>/<id>.md`.

- **id**: from `data/roster/person_ids.csv`. ASCII, lowercase, family name first (`newton-isaac`). Frozen once the file exists.
- **shard**: the first character of the id. Two reasons: the GitHub web view lists at most 1,000 entries per folder, and the roster has 1,380 people. The shard can always be worked out from the id.
- **format**: Markdown with YAML front matter, following `schema/person.schema.json`. Start from `templates/person.template.md`.

Files are added one person per run (`docs/RUNBOOK.md`). Not every roster person has a file yet. `reports/coverage.md` shows which do.

| file | status |
|---|---|
| [`f/faraday-michael.md`](f/faraday-michael.md) | worked example, unreviewed |

Validate:

```bash
python scripts/validate_people.py              # all files
python scripts/validate_people.py people/f/faraday-michael.md
```

Rules that matter most:

- Every filled fact has a certainty, a citation with a locator, and a how_known note.
- Unresearched fields say `TODO`.
- The worldview is the *adult working* worldview. Heritage is context only.
- Lane B fields are a labeled belief model, not findings.
- No Wikipedia citations, and no invented facts.
