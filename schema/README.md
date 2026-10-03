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

Person schema versions: 1.1 (2026-10-01, descriptions only), 1.2 (2026-10-02, P8: basis `recorded_interview`, kind `recorded interview`), 1.3 (2026-10-02, P18, P21, P24, P28: statement kinds `autobiography`, `unpublished manuscript`, `document in own hand`, `published letter`; institution kind `research institute`; schooling stage `elementary school` and optional `run_by`; basis `inference_from_work`). `record.schema_version` accepts "1.2" and "1.3". 1.2 files stay valid; `validate_people.py` rejects 1.3-only values in a 1.2 file and the retired stages `religious school` / `dame or charity school` in a 1.3 file.
