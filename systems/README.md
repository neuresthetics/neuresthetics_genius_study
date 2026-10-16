# systems/

One file per belief system: `systems/<CODE>.md`, where the code is the v7.1 abbreviation (`PANT`, `CLASS_THEISM`, `CLTHEI`, ...). There are 77, one for each system in the v7.1 data book.

- **Format:** Markdown with YAML front matter, following `schema/system.schema.json`. The template is `templates/system.template.md`.
- **v7.1 scores:** each file carries the authorial v7.1 rubric scores (L logical consistency, P paradox resolution, E empirical compatibility, V evidence vs revelation, X predictive/explanatory success) and the verbatim scoring note. `scripts/validate_systems.py` checks them against the data book, so they can't drift. Revised scores go in `revised_rubric`, which stays not started until the first coding pool is done (decision S3).
- **Status:** 1 file is a stub (4THWAY) (scores and note only, everything else `TODO`). Under P46(a), 10 more are sourced but unscored (all axes UNKNOWN) and count with the stubs in the headline: BON, CYNIC, DRUZE, EFFALT, HEDON, HELLEN, PHENOM, RODNOV, SOLIP, THSAT. [`PANT.md`](PANT.md) is the worked example, cited from the Stanford Encyclopedia of Philosophy and unreviewed. Sourced drafts (unreviewed): [`CLASS_THEISM.md`](CLASS_THEISM.md), [`CLTHEI.md`](CLTHEI.md), [`CHRIST.md`](CHRIST.md), [`ISLAM.md`](ISLAM.md), [`DEISM.md`](DEISM.md), [`STOIC.md`](STOIC.md), [`JUDA.md`](JUDA.md), [`PLATO.md`](PLATO.md); from systems batch S1 (2026-10-15, roster order): [`ATHE.md`](ATHE.md) (*sourced*, batch S1), [`AGNOS.md`](AGNOS.md) (*sourced*, batch S1), [`BRGHTS.md`](BRGHTS.md), [`EMPIR.md`](EMPIR.md) (*sourced*, batch S1), [`ETHCUL.md`](ETHCUL.md) (*sourced*, batch S1), [`RATN.md`](RATN.md); batch S2: [`SECHUM.md`](SECHUM.md), [`SUNASM.md`](SUNASM.md), [`PRAG.md`](PRAG.md), [`ARIST.md`](ARIST.md), [`EFFALT.md`](EFFALT.md), [`TRNSHM.md`](TRNSHM.md); batch S3: [`ABSURD.md`](ABSURD.md), [`CYNIC.md`](CYNIC.md), [`EPICUR.md`](EPICUR.md), [`EXIST.md`](EXIST.md), [`NIHIL.md`](NIHIL.md), [`OBJCT.md`](OBJCT.md); batch S4: [`SCEPT.md`](SCEPT.md), [`KANT.md`](KANT.md), [`PHENOM.md`](PHENOM.md), [`UTIL.md`](UTIL.md) ([`PANDEI.md`](PANDEI.md) and [`PANEND.md`](PANEND.md) stay stubs: no SEP, IEP or Britannica text found); batch S5: [`DETERM.md`](DETERM.md), [`LVSAT.md`](LVSAT.md), [`PANENT.md`](PANENT.md), [`HEDON.md`](HEDON.md), [`PANPSY.md`](PANPSY.md), [`IDEAL.md`](IDEAL.md); batch S6: [`PANDEI.md`](PANDEI.md) and [`PANEND.md`](PANEND.md) (P45 lower tier, capped at 0.5), [`BUDDH.md`](BUDDH.md), [`JAIN.md`](JAIN.md), [`SOLIP.md`](SOLIP.md); batch S7: [`BAHAI.md`](BAHAI.md), [`ANIM.md`](ANIM.md), [`CAODAI.md`](CAODAI.md), [`CHNFOLK.md`](CHNFOLK.md), [`HYLO.md`](HYLO.md), [`CONFUC.md`](CONFUC.md); batch S8: [`SHINTO.md`](SHINTO.md), [`TAO.md`](TAO.md), [`HINDU.md`](HINDU.md), [`HEATH.md`](HEATH.md), [`HELLEN.md`](HELLEN.md) and [`KEMET.md`](KEMET.md) (the last two thin: one sentence in a general article); batch S9: [`RODNOV.md`](RODNOV.md) (thin), [`WICCA.md`](WICCA.md), [`ABORIG.md`](ABORIG.md), [`BON.md`](BON.md) (thin), [`NATAM.md`](NATAM.md), [`SANTER.md`](SANTER.md); batch S10: [`VODUN.md`](VODUN.md), [`ANTHRO.md`](ANTHRO.md) (thin), [`CHAOSM.md`](CHAOSM.md) (P45), [`HERMET.md`](HERMET.md) (thin), [`SIKH.md`](SIKH.md); `4THWAY` kept as a stub; batch S11: [`THEOS.md`](THEOS.md), [`DRUZE.md`](DRUZE.md) (thin, unscored), [`MANDAE.md`](MANDAE.md) (thin), [`YAZID.md`](YAZID.md) (thin), [`ZORO.md`](ZORO.md), [`MORMON.md`](MORMON.md); `4THWAY` P45 search logged, still a stub; batch S12: [`THSAT.md`](THSAT.md) (thin, unscored), [`THELEM.md`](THELEM.md), [`FALUNG.md`](FALUNG.md), [`RAEL.md`](RAEL.md) (P45), [`SCIENT.md`](SCIENT.md). The systems pass is complete: all 77 files were worked in batches S1–S12 in v7.1 number order (Jason, 2026-10-15), and every batch was blind-audited with its fixes applied. Final counts (P46): 66 sourced, 10 sourced but unscored, 1 stub (4THWAY).
- **Labels:** `v7_1_label` is verbatim. Two display labels differ from v7.1, both approved on 2026-10-01 (`docs/OPEN_DECISIONS.md`): CLTHEI → "Interventionist personal theism" (S1), and PANT → the full V6 label "Pantheism (Spinozistic/naturalistic 'God = Universe')" (S2).
- **Code list:** closed at 77 for v8 (decision S4). New codes are added in one batch with one schema bump.
- **Adherent numbers** are context only. They are never a denominator for genius rates.

## Sourcing backlog

Stubs to source next, in this order (now superseded for sourcing by the roster-order batches above; items marked *sourced* are drafts) (decision S7, 2026-10-02; extended by P22, 2026-10-02). A stub can still be coded: under P14 a person is coded at the certainty the evidence supports, the record flags the stub, and the stub goes on this list. These are the candidate codes the people records most often need while the file is still a stub:

1. [`ATHE.md`](ATHE.md), Atheism: candidate or code for Bohr, Chandrasekhar and Dirac; named alternative for Feynman and Pauling (batch 4); code for Turing (at 0.5), candidate for Hume, named alternative for Spinoza (stage 3).
2. [`AGNOS.md`](AGNOS.md), Agnosticism: named alternative for Bohr and Dirac; code for Feynman and candidate for Hubble and Fermi (batch 4); Darwin's later self-description, after the major work (his record codes DEISM at 0.5 and puts agnosticism in changes_over_life); first-listed candidate for Hume, whose record leaves primary_system BELOW_THRESHOLD and still gives the stub as the reason (pre-P14 wording, for its coder); named alternative for Turing; considered for von Neumann (stage 3).
3. [`KANT.md`](KANT.md) (*sourced*, batch S4), Kantianism: best fit for Kant (founders rule); his record leaves primary_system BELOW_THRESHOLD and still gives the stub as the reason (pre-P14 wording, for its coder; stage 3).
4. [`SCEPT.md`](SCEPT.md) (*sourced*, batch S4), Scepticism: candidate for Hume (his own 'mitigated' scepticism; stage 3).
5. [`RATN.md`](RATN.md) (*sourced*, batch S1), Rationalism: considered and not coded for Descartes and Leibniz, whose records code CLASS_THEISM (Descartes at 0.5, Leibniz at 0.7); rejected for Darwin under P22 (stage 3). Has a one-line use_when against CLASS_THEISM (v8's pick, P22); the rest is unsourced.
6. [`EMPIR.md`](EMPIR.md), Empiricism: considered for Hume (stage 3).
7. [`IDEAL.md`](IDEAL.md) (*sourced*, batch S5), Idealism: candidate for Pasteur.

After these, the other stubs, in the order the people records need them:

- [`SECHUM.md`](SECHUM.md) (*sourced*, batch S2), Secular humanism: code for Pauling.
- [`ETHCUL.md`](ETHCUL.md), Ethical Culture: candidate for Oppenheimer.
- [`PANPSY.md`](PANPSY.md) (*sourced*, batch S5), Panpsychism: considered for Riemann (stage 3).
- [`DETERM.md`](DETERM.md) (*sourced*, batch S5), Determinism: considered for Spinoza (stage 3).
- [`HINDU.md`](HINDU.md): rejected for Oppenheimer (so it matters less).

Extending a record: `docs/RUNBOOK.md` §8.

## Systems to consider (proposed codes, decision S4)

The code list is closed for v8, so these are not files. Each entry gives the code idea, why, and example people; they would be added in one batch with one schema bump and Jason's approval.

| Proposed system | Why | Example people |
|---|---|---|
| French spiritualism (*spiritualisme*; Victor Cousin's school: God, the soul, freedom) | Pasteur's 1882 Académie française speech defends "la doctrine spiritualiste" by name; none of the 77 codes fits it well (CHRIST and IDEAL are only partial fits). Added by decision S7. | Louis Pasteur |
| Marxist or communist humanism (socialist ethics without religion) | Dorothy Hodgkin's memoir (Dodson 2002, pp. 213–215) describes her socialist sympathies and her sympathy for 'the communist regime's social ideas and aspirations'; none of the 77 codes is a political creed, and political views are not coded now. Proposed in batch 4 (optional; Jason to decide). | Dorothy Hodgkin |

To regenerate stubs, if a stub file is lost:

```bash
python scripts/make_system_stubs.py --dry-run   # shows what it would write; never overwrites a non-stub file
python scripts/make_system_stubs.py
```

The full code list is in `docs/CODING_GUIDE.md` §10. How to extend a record is in `docs/RUNBOOK.md`, Part 2.
