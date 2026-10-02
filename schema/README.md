# schema/

JSON Schemas (draft 2020-12) for the YAML front matter of record files.

| file | applies to |
|---|---|
| `person.schema.json` | `people/<shard>/<id>.md` |
| `system.schema.json` | `systems/<CODE>.md` |

Both use the same claim pattern:

- `value`, `certainty` (1.0 / 0.7 / 0.5), `cites` (`{source, locator}`), `how_known`, and optional `note` and `alternatives`;
- the sentinels `TODO`, `UNKNOWN` and `BELOW_THRESHOLD`.

The validators (`scripts/validate_people.py`, `scripts/validate_systems.py`) apply the schema plus checks the schema can't express: roster match, citation resolution, basis/certainty agreement, v7.1 scores against the data book, and required body sections.

The field reference in `docs/DATA_DICTIONARY.md` is generated from these files by `scripts/make_data_dictionary.py`. To change a field:

1. edit the schema and the template;
2. bump `schema_version`;
3. rerun the generator and the validators.
