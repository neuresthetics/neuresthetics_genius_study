# systems/

One file per belief system: `systems/<CODE>.md`, where the code is the v7.1 abbreviation (`PANT`, `CLASS_THEISM`, `CLTHEI`, ...). There are 77, one for each system in the v7.1 data book.

- **Format:** Markdown with YAML front matter, following `schema/system.schema.json`. The template is `templates/system.template.md`.
- **v7.1 scores:** each file carries the authorial v7.1 rubric scores (L logical consistency, P paradox resolution, E empirical compatibility, V evidence vs revelation, X predictive/explanatory success) and the verbatim scoring note. `scripts/validate_systems.py` checks them against the data book, so they can't drift. Revised scores go in `revised_rubric`, which is not started yet.
- **Status:** 76 files are stubs (scores and note only, everything else `TODO`). [`PANT.md`](PANT.md) is the worked example, cited from the Stanford Encyclopedia of Philosophy and unreviewed.
- **Labels:** `v7_1_label` is verbatim. Two display labels are proposed and wait on Jason's OK (`docs/OPEN_DECISIONS.md`): CLTHEI → "Interventionist personal theism", and PANT trimmed to "Pantheism (Spinozistic/naturalistic)".
- **Adherent numbers** are context only. They are never a denominator for genius rates.

To regenerate stubs, if a stub file is lost:

```bash
python scripts/make_system_stubs.py --dry-run   # shows what it would write; never overwrites a non-stub file
python scripts/make_system_stubs.py
```

The full code list is in `docs/CODING_GUIDE.md` §10. How to extend a record is in `docs/RUNBOOK.md`, Part 2.
