# systems/

One file per belief system: `systems/<CODE>.md`, where the code is the v7.1 abbreviation (`PANT`, `CLASS_THEISM`, `CLTHEI`, ...). There are 77, one for each system in the v7.1 data book.

- **Format:** Markdown with YAML front matter, following `schema/system.schema.json`. The template is `templates/system.template.md`.
- **v7.1 scores:** each file carries the authorial v7.1 rubric scores (L logical consistency, P paradox resolution, E empirical compatibility, V evidence vs revelation, X predictive/explanatory success) and the verbatim scoring note. `scripts/validate_systems.py` checks them against the data book, so they can't drift. Revised scores go in `revised_rubric`, which stays not started until the first coding pool is done (decision S3).
- **Status:** 68 files are stubs (scores and note only, everything else `TODO`). [`PANT.md`](PANT.md) is the worked example, cited from the Stanford Encyclopedia of Philosophy and unreviewed. Sourced drafts (unreviewed): [`CLASS_THEISM.md`](CLASS_THEISM.md), [`CLTHEI.md`](CLTHEI.md), [`CHRIST.md`](CHRIST.md), [`ISLAM.md`](ISLAM.md), [`DEISM.md`](DEISM.md), [`STOIC.md`](STOIC.md), [`JUDA.md`](JUDA.md), [`PLATO.md`](PLATO.md).
- **Labels:** `v7_1_label` is verbatim. Two display labels differ from v7.1, both approved on 2026-10-01 (`docs/OPEN_DECISIONS.md`): CLTHEI → "Interventionist personal theism" (S1), and PANT → the full V6 label "Pantheism (Spinozistic/naturalistic 'God = Universe')" (S2).
- **Code list:** closed at 77 for v8 (decision S4). New codes are added in one batch with one schema bump.
- **Adherent numbers** are context only. They are never a denominator for genius rates.

## Sourcing backlog

Stubs to source next, in this order (decision S7, 2026-10-02). These three are the candidate codes the people records most often cannot use because the file is still a stub:

1. [`ATHE.md`](ATHE.md), Atheism: candidate or code for Bohr, Chandrasekhar and Dirac.
2. [`AGNOS.md`](AGNOS.md), Agnosticism: named alternative for Bohr and Dirac.
3. [`IDEAL.md`](IDEAL.md), Idealism: candidate for Pasteur.

After these, the other stubs, in the order the people records need them. Extending a record: `docs/RUNBOOK.md` §8.

## Systems to consider (proposed codes, decision S4)

The code list is closed for v8, so these are not files. Each entry gives the code idea, why, and example people; they would be added in one batch with one schema bump and Jason's approval.

| Proposed system | Why | Example people |
|---|---|---|
| French spiritualism (*spiritualisme*; Victor Cousin's school: God, the soul, freedom) | Pasteur's 1882 Académie française speech defends "la doctrine spiritualiste" by name; none of the 77 codes fits it well (CHRIST and IDEAL are only partial fits). Added by decision S7. | Louis Pasteur |

To regenerate stubs, if a stub file is lost:

```bash
python scripts/make_system_stubs.py --dry-run   # shows what it would write; never overwrites a non-stub file
python scripts/make_system_stubs.py
```

The full code list is in `docs/CODING_GUIDE.md` §10. How to extend a record is in `docs/RUNBOOK.md`, Part 2.
