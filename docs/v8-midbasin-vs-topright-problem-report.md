# Problem report: mid-basin shading vs the stated goal

Date: 2026-10-03
Repo: neuresthetics/neuresthetics_genius_study
Scope: figure `figures/people_cause_locus.png`, decision P4, Lane B
Status: observation only. No record was edited for this note.

## Problem

The chart a reader meets first shades the mid-basin box. The stated goal for this pass is the top right: A high and B high (lawful order, God identified with the order, not a person outside it). The shade marks the other bin. Scores were not moved. The instrument around them was aimed at the membership test.

## What the two regions are

Axes on `figures/people_cause_locus.png`:

- B_cause (x): 0 interventionist cause, 4 lawful cause with no reserved exceptions.
- A_locus (y): 0 God as a person outside the world, 4 God as the order / no separate God.

P4 mid-basin (the green box): A ≤ 1 and B ≥ 3, both at certainty ≥ 0.7. Source of the test: v7.1 lines about Faraday and Maxwell as devout and lawful, classical theism lawful without identity of God and world, "lawful form early, even if the word God stayed." Stated consequence in METHOD §1.1: deists pass. No exclusion.

Top right, the region wanted for this pass: A ≥ 3 and B ≥ 3. This is the Lane B circle (Deus sive Natura) plus lawful form. P4 marks this cell mid_basin false on purpose. The two tests do not share a cell.

## What the current chart shows

23 of 43 coded person records have both axes scored. Drafts, unreviewed, not a sample. Footer already says descriptive only.

In the green box and passing: Galileo, Leibniz, Ibn Sina, Newton, Gödel, Descartes, Aquinas, Kant, Maxwell, Faraday, Boyle.

In the same cells but not passing: Darwin (A 0.5), Kepler (B 0.5), Riemann (both 0.5). Pascal is B 2, so left of the box, TODO.

Top right, A 4 and B 4, mid_basin false: Einstein, Spinoza, Schrödinger, Pauling. Chandrasekhar is in that cell at 0.5 and BELOW_THRESHOLD. Hume is A 3, B 4, BELOW_THRESHOLD.

Einstein is off the box because A is 4, not because the plot dropped him. Record `people/e/einstein-albert.md`: PANT at 0.7 from the 1929 Goldstein cable ("Spinoza's God who reveals Himself in the orderly harmony of what exists") plus SEP Pantheism §12. B 4. mid_basin false at 0.7. Still draft — unreviewed. Several certainties capped at 0.7 because essays were read from an unofficial web copy. P31 let later essays stand for a 1905–1925 working span. Those are review items. They are not a reason to place him in the green box.

## Why this will keep being misread

- The shaded region is the only region defined on the figure. The caption defines the box and does not define the top right.
- The first pool (Faraday, Maxwell, Newton, Aquinas, Ibn Sina, Gödel) is the green box by construction. Coverage: all six files exist, all unreviewed, all mid_basin true on the drafts.
- Lane B fields on the 43 person files are 97.7% filled. Worldview claims are 61.1% filled (303/496; 99 UNKNOWN, 91 BELOW_THRESHOLD). Belief-model inputs are ahead of the descriptive codes.
- Zero person files are `reviewed`. P5 allows that status only from a named human.

Leaving only the box shaded will be read as the target, including by the author.

## What this is not

Not a corrupted score. P4 does not pull a pantheist into the box or a mid-basin theist into the corner. Not a study result. No frequency, rate, or ranking is supported. The roster rebuild (1,380 people, F as distinct models, v7 aggregate reproduced 500/500) is a separate correction and is not the problem in this note.

## Fix when this is picked up

1. Second shade for A ≥ 3 and B ≥ 3, same certainty rule, or no shade. Caption must name both regions and say which one is the membership test and which one is the Lane B cell.
2. Count the top-right cell the same way the box is counted. On this chart: four people at A 4, B 4, all unreviewed.
3. Do not edit Einstein into the green box.
4. Optional: a human review of one top-right record and one box record before any more rulings. P31 and the unofficial-copy cap are the Einstein review items.

## Sources in repo

- `figures/people_cause_locus.png`
- `docs/METHOD.md` §1.1 (P4, deist consequence)
- `docs/OPEN_DECISIONS.md` P4
- `reports/coverage.md` (43 files, 0 reviewed, Lane B vs worldview fill)
- `people/e/einstein-albert.md` (record version 8, draft — unreviewed)
