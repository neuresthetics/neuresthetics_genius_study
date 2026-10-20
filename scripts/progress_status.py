#!/usr/bin/env python3
"""Write the progress status table in README.md from the repo's own files.

Usage:
    python scripts/progress_status.py            # rewrite the table in README.md
    python scripts/progress_status.py --stdout   # print the table instead
    python scripts/progress_status.py --check    # exit 1 if the README table is out of date

The table sits between the markers <!-- BEGIN GENERATED: progress --> and
<!-- END GENERATED: progress --> in README.md. The caption of the person chart sits between
<!-- BEGIN GENERATED: people_chart_caption --> and <!-- END GENERATED: people_chart_caption -->;
it is computed by lib.records.people_chart_caption() from the same records the chart plots.
Everything outside the markers is hand-written.

Where each row comes from:
    roster counts      data/roster/roster.csv (status column)
    people coded       person files in people/ whose roster status is core
    systems sourced    systems/*.md whose review_status is not "stub"
    decisions          the summary table in docs/OPEN_DECISIONS.md (rows marked "decided")
    latest tag         `git tag --sort=-creatordate` (falls back to "none" outside a git checkout)
    audits, next steps MANUAL: the AUDITS and NEXT_STEPS constants below. Update them by hand.
"""
import argparse, collections, os, re, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib.records import REPO, read_record, read_csv, person_files, system_files, people_chart_caption  # noqa: E402

README = os.path.join(REPO, "README.md")
BEGIN, END = "<!-- BEGIN GENERATED: progress -->", "<!-- END GENERATED: progress -->"
CAP_BEGIN, CAP_END = "<!-- BEGIN GENERATED: people_chart_caption -->", "<!-- END GENERATED: people_chart_caption -->"

# MANUAL rows. No file in the repo records these as data, so they are kept here by hand.
AUDITS = ("9 blind lens runs on four batches: 3 on a 115-claim packet (eff4700), 2 on a 147-claim packet (e648145), 2 on a "
          "124-claim packet (d9903b7/43cecc4; fixes at 6f37cd6) and 2 on a 165-claim packet (b21655b; run 1 155 hold / 10 weaken, "
          "run 2 160 hold / 5 weaken, 0 wrong; agreement 156/165, κ 0.37; fixes applied at 3bcd59c); see "
          "[reports/audit_2026-10-02.md](reports/audit_2026-10-02.md). Stage 3: 4 blind runs on the first 12 records (stage 3-a: "
          "561 claims at 59a8371; stage 3-b: 420 claims at 3db6511); their method rulings are decisions P14–P28; one blind run on the stage 3-b rulings (93 claims at 6155174: 88 hold, 4 weaken, 1 fail, fixed at 4c10399) gave P29; lens's runs on the v8.a rulings packet (34a73c4) and the v8.b P29 packet (e930597) gave P30; the P30 span-alignment audit (7a52a3f) gave P31; one blind run on stage 3 batch C (14 claims at dd91009: 8 hold, 6 weaken, 0 fail; no second run needed under P30 #16) gave P35 and P36; one blind run on batch D (16 claims at 3f4817e: 14 hold, 2 weaken, 0 fail) gave P41, and one on batch E (18 claims at 2332880: 17 hold, 1 weaken, 0 fail); their fixes are applied; one on batch F (15 claims at 64605bd: 15 hold, 0 weaken, 0 fail) passed; its fixes are applied; one on batch G (13 claims at 5ff29b4: 13 hold, 0 weaken, 0 fail) passed and gave P43 (Jason's ruling on RQ1); its fixes are applied. Batch H (Marx, Tolstoy, Leonardo da Vinci, Beethoven; 7 claims at cae9cb2: 6 hold, 1 weaken, 0 fail) passed and extended P41 to miracle rejection; its fixes are applied; batch I (Wittgenstein, Maimonides, Michelangelo, Tesla; 10 claims at bbb26f8: 8 hold, 2 weaken, 0 fail) passed; its fixes are applied; batch J (Omar Khayyam, Picasso, Plato, Raphael; 13 claims at 81b9098: 10 hold, 3 weaken, 0 fail) passed; its fixes are applied; batch K (Rembrandt, Rosalind Franklin, Salvador Dalí, Simone de Beauvoir; 10 claims at 2d75649: 9 hold, 1 weaken, 0 fail) passed; its fixes are applied; batch L (Socrates, Stephen Hawking, Thomas Edison, Tim Berners-Lee; 11 claims at 2742382: 10 hold, 1 weaken, 0 fail) passed; its fixes are applied at 55d6956; all of batches H–L have passed their audits with fixes applied; batch M (Vincent van Gogh, Virginia Woolf, William Shakespeare, Wolfgang Amadeus Mozart; 19 claims at 159d60d: 16 hold, 3 weaken, 0 fail) passed; its fixes are applied, and v8's ruling on its RQ1 (on the auditor's advice) added the P42 will-preamble addendum; batch N (Andrew Wiles, Arthur Schopenhauer, B.F. Skinner, Carl Jung; 23 claims at 041f54b: 17 hold, 5 weaken, 1 fail) passed; its fixes are applied, and v8's rulings on its RQ1–RQ3 (on the auditor's advice) set Schopenhauer's B 3 and Skinner's B 4 and added the P35 addendum on theories of mind and behaviour; batch O (Carl Sagan, Claude Shannon, Confucius, David Hilbert; 23 claims at ee3d463: 19 hold, 3 weaken, 1 fail) passed; its fixes are applied, and v8's rulings on its RQ O1 and O2 (on the auditor's advice) added the P42 addendum on disciples' records of sayings and the P16 addendum on a general remark on lawful nature; batch P (Donald Knuth, Francis Crick, Franz Kafka, Galen; 45 claims at 08be43b: 39 hold, 6 weaken, 0 fail) passed; its fixes are applied, and v8's picks on its P1–P3 (on the auditor's advice) cap Knuth's post-span evidence at 0.5 rather than excluding it, keep Galen's B 3 at 0.5 and keep Kafka BELOW_THRESHOLD; batch Q (Georg Wilhelm Friedrich Hegel, Georgia O'Keeffe, Henry Ford, Ibn Khaldun; 48 claims at 0b3023d: 43 hold, 4 weaken, 1 fail) passed; its fixes are applied, the Knuth span is 1968–2023 under P30 addendum d (Jason's call), and Jason's ruling on its RQ Q1 gives Hegel B 2 at 0.5 (Encyclopaedia §§248, 250); batch R (Ibn Rushd (Averroes), Jacques Derrida, James Joyce, James Watson; 43 claims at 0454445: 39 hold, 4 weaken, 0 fail) passed; its fixes are applied, and v8's call on its RQ R1 (on the auditor's advice) keeps Watson's post-span 'lifelong atheist' at the P1 cap of 0.5; batch S (Jane Austen, Jane Goodall, Jean Piaget, Jean-Jacques Rousseau; 48 claims at c5d448a: 43 hold, 4 weaken, 1 fail) passed with fixes applied; v8's calls on its RQ S1–S3 (on the auditor's advice) keep Rousseau CHRIST under P27, add the P42 addendum on a character's words adopted in the author's own voice (Rousseau stays at 0.7), and count Austen's prayers under P42 at 0.5 (A 0; she stays unplotted, B UNKNOWN); under P30 #16 its FAIL calls for a second blind run")
NEXT_STEPS = ("Stage 3 (everyone else with F ≥ 3) has started: the first 12 records (Spinoza, Descartes, Pascal, Leibniz, Kant, "
              "Hume, Darwin, Gauss, Riemann, Turing, Noether, von Neumann) are drafts that still need to apply P29 and P30 (the stage 3-b six "
              "follow P14–P28 on main; the stage 3-a six also still need P14–P28); the other 79 records follow P14–P28 (schema 1.3) and "
              "P30's age rule, and their worldview.working_years now equals timing.major_work_period (P30 addendum); under P31 (continuity rule) all 55 values the span audit flagged stand; the strict-period alternative is in reports/period_rule_sensitivity.md; batch C (Wu, Lovelace, Smith, al-Farabi, al-Khwarizmi, Bell) is drafted in P32 order and its blind lens run is applied (P35, P36); batch D (Archimedes, Aristotle, McClintock, Russell, Debussy, Monet) is drafted and its blind audit is applied (P41); batch E (Dante, Euclid, Francis Bacon, Kahlo, Nietzsche, Dostoevsky) is drafted (P40) and its blind audit is applied; batch F (García Márquez, Hopper, Arendt, Poincaré, Hippocrates, Homer) is drafted (P42) and passed its blind audit (15/15 hold; fixes applied); batch G (Hypatia, Stravinsky, Bach, Locke) is drafted (P43) and passed its blind audit (13/13 hold; fixes applied); batch H (Marx, Tolstoy, Leonardo da Vinci, Beethoven) passed its blind audit (6 hold, 1 weaken; fixed); batch I (Wittgenstein, Maimonides, Michelangelo, Tesla) passed its blind audit (8 hold, 2 weaken; fixed); batch J (Omar Khayyam, Picasso, Plato, Raphael) passed its blind audit (10 hold, 3 weaken; fixed); batch K (Rembrandt, Rosalind Franklin, Salvador Dalí, Simone de Beauvoir) passed its blind audit (9 hold, 1 weaken; fixed); batch L (Socrates, Stephen Hawking, Thomas Edison, Tim Berners-Lee) passed its blind audit (10 hold, 1 weaken; fixed); batch M (Vincent van Gogh, Virginia Woolf, William Shakespeare, Wolfgang Amadeus Mozart) passed its blind audit (16 hold, 3 weaken; fixed; RQ1 gave the P42 will-preamble addendum); batch N (Andrew Wiles, Arthur Schopenhauer, B.F. Skinner, Carl Jung) passed its blind audit (17 hold, 5 weaken, 1 fail; fixed; RQ3 gave the P35 addendum on theories of mind and behaviour); batch O (Carl Sagan, Claude Shannon, Confucius, David Hilbert) passed its blind audit (19 hold, 3 weaken, 1 fail; fixed; RQ O1 and O2 gave the P42 and P16 addenda); the chart images were refreshed after batches M–O; batch P (Donald Knuth, Francis Crick, Franz Kafka, Galen) passed its blind audit (39 hold, 6 weaken, 0 fail; fixed; P1–P3 kept Knuth capped at 0.5, Galen B 3, Kafka BELOW_THRESHOLD); batch Q (Georg Wilhelm Friedrich Hegel, Georgia O'Keeffe, Henry Ford, Ibn Khaldun) passed its blind audit (43 hold, 4 weaken, 1 fail; fixed; Knuth span 1968–2023, Jason's call; Jason's ruling puts Hegel at B 2); batch R (Ibn Rushd (Averroes), Jacques Derrida, James Joyce, James Watson) passed its blind audit (39 hold, 4 weaken, 0 fail; fixed; R1 keeps Watson at 0.5: 'lifelong' does not lift the P1 cap); batch S (Jane Austen, Jane Goodall, Jean Piaget, Jean-Jacques Rousseau) passed its blind audit (43 hold, 4 weaken, 1 fail; fixed; S1 keeps Rousseau CHRIST, S2 adds the P42 addendum on adopted characters' words, S3 counts Austen's prayers at 0.5); batch T (Johann Wolfgang von Goethe, John Maynard Keynes, Jonas Salk, Leonhard Euler) is drafted and its blind audit is applied (rulings T1, T2, RQ-AU1); batch U (Martin Heidegger, Martin Luther King Jr., Michel Foucault, Miguel de Cervantes; Louis Pasteur already coded) passed its blind audit (38 hold, 6 weaken, 0 fail; fixed; U2 puts Cervantes BELOW_THRESHOLD; U1 on King's B and Kant's B 3 were settled by Jason's rulings on 2026-10-19: King B 3 at 0.7 from Strength to Love, mid_basin true; Kant B 3 at 0.7, alt 4); batch V (Miles Davis, Milton Friedman, Nelson Mandela, Niccolò Machiavelli) passed its blind audit (42 hold, 6 weaken, 0 fail; fixed; V1 sets Mandela's B UNKNOWN, V2 and V3 keep Machiavelli and Davis as coded); batch W (Nicolaus Copernicus, Pythagoras, Richard Wagner, Roger Penrose; Paul Dirac already coded) passed its blind audit (35 hold, 5 weaken, 0 fail; fixed; W1 keeps Copernicus BELOW_THRESHOLD, W2 adds IDEAL as a lead for Wagner, W3 keeps Penrose ATHE at 0.5); batch X (Samuel Morse, Siddhartha Gautama, Sigmund Freud, Srinivasa Ramanujan) passed its blind audit (45 hold, 7 weaken, 0 fail; fixed; X1 keeps Morse's B BELOW_THRESHOLD, X2 keeps Gautama BELOW_THRESHOLD with BUDDH the lead, X3 makes Freud not a scientist, X4 keeps Ramanujan as coded; Pythagoras's era now UNKNOWN under a strict P39); batch Y (Steve Jobs, Sun Tzu, Terence Tao, Toni Morrison; Thomas Aquinas already coded), the last batch of this run, passed its blind audit (64 hold, 3 weaken, 0 fail; fixed; Y1 and Y2 keep Jobs and Morrison BELOW_THRESHOLD, Y3 makes Tao not a scientist; Sun Tzu's era now UNKNOWN); the chart images were refreshed after batch Y and again after Jason's 2026-10-19 rulings and the label fix (57 plotted, 86 not scorable; no overlapping labels); batch Z1 (Virgil, Ada Yonath, Akira Kurosawa, Al-Biruni), the first of Jason's ten queued batches Z1–Z10, is drafted and awaits its blind audit; batch Z2 (Noam Chomsky, filling the P32 gap at rank 62, then Al-Ghazali, Al-Razi, Alexander Fleming) is drafted and awaits its blind audit (61 plotted, 90 not scorable at the next chart refresh; chart images not regenerated); no other F ≥ 4 person is uncoded; batch Z3 (Alexander Grothendieck, Alfred North Whitehead, Amartya Sen, Andreas Vesalius) passed its blind audit (20 hold, 3 weaken, 1 fail; fixed; RQ-Z3-1 puts Whitehead on his agnostic phase under P31, not plotted; 62 plotted, 93 not scorable at the next chart refresh); batch Z4 (Arnold Schoenberg, Aryabhata, Augustine of Hippo, Bill Gates) passed its blind audit (20 hold, 1 weaken, 2 fail; fixed; RQ-Z4-1 keeps Aryabhata's invocation at 0.5, RQ-Z4-2 keeps Augustine at B 2, RQ-Z4-N1 keeps Grothendieck at 0.5 with Scharlau's backing; 64 plotted, 95 not scorable at the next chart refresh); batch Z5 (Brahmagupta, Caravaggio, Carl Linnaeus, Chinua Achebe; Caroline Herschel already coded) is audited with fixes applied; RQ-Z5-N1 (Linnaeus span end 1758, result-changing) awaits v8's call; batch Z6 (Claude Levi-Strauss, Daniel Kahneman, Demis Hassabis, Donatello) is audited with fixes applied (Kahneman ATHE 0.5, A 4 at 0.5, now plotted faded; 66 plotted, 101 not scorable); batch Z7 (Duke Ellington, Duns Scotus, Edward O. Wilson, Epicurus; Edwin Hubble already coded) is audited with fixes applied (mid_basin P10 fixes; RQ-Z7-N1 artworks dated by unveiling or installation; 69 plotted, 102 not scorable); batch Z8 (Évariste Galois, Ferdinand de Saussure, Frank Lloyd Wright, Franz Schubert) is audited with fixes applied (Wright checked against the Ransom Center transcript, PANT and A 4 at 0.5 stand; Schubert BELOW_THRESHOLD, span 1814); batch Z9 (Geoffrey Chaucer, Geoffrey Hinton, George Boole, George Orwell) is audited with fixes applied (RQ-Z9-N1: manuscript-era composition ranges date pre-print works; Boole BELOW_THRESHOLD, still plotted); batch Z10 (Gregor Mendel, Grigori Perelman, Guglielmo Marconi, Hedy Lamarr) is audited with fixes applied (Mendel 1865, age 43; Marconi span 1896; Lamarr span UNKNOWN; 70 plotted, 113 not scorable); batch AA1 (Henri Matisse, Heraclitus, Herbert Simon, Ibn al-Haytham; Henrietta Swan Leavitt already coded), the first of Jason's ten queued batches AA1–AA10, is audited with fixes applied (Heraclitus newly plotted, faded; era UNKNOWN; Ibn al-Haytham span 1028–1038 under RQ-Z9-N1; 71 plotted, 116 not scorable at the next chart refresh); batch AA2 (Ibn Battuta, Ivan Pavlov, J.M.W. Turner, Jean-Paul Sartre; J. Robert Oppenheimer already coded) is audited with fixes applied (Ibn Battuta span 1355; none newly plotted; 71 plotted, 120 not scorable at the next chart refresh); batch AA3 (Johannes Brahms, Johannes Gutenberg, John McCarthy, John Milton) is audited with fixes applied (Brahms span 0.7; none newly plotted; 71 plotted, 124 not scorable at the next chart refresh); batch AA4 (John Nash, John Stuart Mill, Jorge Luis Borges, Joseph-Louis Lagrange) is audited with fixes applied (Nash span 1950–1952; none newly plotted; 71 plotted, 128 not scorable at the next chart refresh); next in order after rank 195: Judith Butler, Katherine Johnson; systems were sourced in batches of six in v7.1 number order "
              "(S1 passed its blind audit, 5 hold, 2 weaken; fixed under P44; S2 passed its blind audit, 9 hold, 1 weaken; fixed; S3 passed its blind audit, 10 hold, 1 weaken; fixed; S4 passed its blind audit, 11 hold, 1 weaken; fixed; S5 passed its blind audit, 13/13 hold; follow-ups applied; S6 passed its blind audit, 14 hold, 1 weaken; fixed; S7 passed its blind audit, 13 hold, 3 weaken; fixed "
              "(P44(e)); S8 passed audit with fixes (SHINTO B, HINDU C, HELLEN and KEMET re-sourced under P45(a)); S9 passed audit with fixes (RODNOV A and BON A, B to UNKNOWN; P46 added); S10 passed audit with fixes (VODUN scope, ANTHRO D 1, quote-backed P46 checks); S11 passed audit with fixes (THEOS B 3; summary-only sources are leads); S12 passed audit with fixes (P45(b) amended; RAEL stays sourced). Systems pass complete: all 77 worked in batches S1–S12, every batch blind-audited with fixes applied; 66 sourced, 10 sourced but unscored (P46), 1 stub (4THWAY, until a full text is read)); the revised rubric has not started")


def latest_tag():
    try:
        out = subprocess.run(["git", "-C", REPO, "tag", "--sort=-creatordate"], capture_output=True, text=True, check=True)
        tags = [t for t in out.stdout.split() if t]
        return f"`{tags[0]}`" if tags else "none"
    except (OSError, subprocess.CalledProcessError):
        return "none"


def decisions():
    rows = re.findall(r"^\| ([RPS]\d+) \|.*\|\s*([^|]*?)\s*\|\s*$",
                      open(os.path.join(REPO, "docs", "OPEN_DECISIONS.md"), encoding="utf-8").read(), re.M)
    ids = {}
    for i, status in rows:
        ids.setdefault(i, status)
    settled = sum(1 for s in ids.values() if s.lower().startswith("decided"))
    return settled, len(ids)


def table():
    roster = read_csv(os.path.join(REPO, "data", "roster", "roster.csv"))
    st = collections.Counter(r["status"] for r in roster)
    core_names = {r["canonical_name"] for r in roster if r["status"] == "core"}
    coded = 0
    for f in person_files():
        d, _ = read_record(f)
        if d["identity"]["roster"]["canonical_name"] in core_names:
            coded += 1
    systems = [read_record(f)[0] for f in system_files()]
    past_stub = [d for d in systems if d["record"]["review_status"] != "stub"]
    # P46(a): sourced only with at least one value or BELOW_THRESHOLD; all-UNKNOWN = "sourced, unscored"
    unscored = sum(1 for d in past_stub if all((n or {}).get("value") == "UNKNOWN" for n in d["lio_axes"].values()))
    sourced = len(past_stub) - unscored
    settled, n_dec = decisions()
    tag = latest_tag()
    other = len(roster) - st["core"] - st["provisional"] - st["review"]
    rows = [
        ("Roster people", f"{len(roster):,}: {st['core']} core, {st['provisional']} provisional, {st['review']} review"
                          + (f", {other} new names still need a status" if other else "")),
        ("People coded (of core)", f"{coded} / {st['core']} (draft, unreviewed)"),
        ("Belief systems sourced", f"{sourced} / {len(systems)} (P46; plus {unscored} sourced, unscored; the rest are stubs)"),
        ("Decisions settled", f"{settled} / {n_dec}"),
        ("Audits", AUDITS),
        ("Latest tag", tag + (" (prerelease)" if re.search(r"alpha|beta|rc", tag) else "")),
        ("Next steps", NEXT_STEPS),
    ]
    out = [BEGIN,
           "<!-- Generated by scripts/progress_status.py; the Audits and Next steps rows are manual constants in that script. -->",
           "", "| Item | Status |", "|---|---|"]
    out += [f"| {k} | {v} |" for k, v in rows]
    out += ["", END]
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stdout", action="store_true")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    new = table()
    if a.stdout:
        print(new)
        return
    text = open(README, encoding="utf-8").read()
    if BEGIN not in text or END not in text:
        sys.exit(f"README.md has no {BEGIN} ... {END} block")
    i, j = text.index(BEGIN), text.index(END) + len(END)
    updated = text[:i] + new + text[j:]
    if CAP_BEGIN not in updated or CAP_END not in updated:
        sys.exit(f"README.md has no {CAP_BEGIN} ... {CAP_END} block")
    i, j = updated.index(CAP_BEGIN), updated.index(CAP_END) + len(CAP_END)
    updated = updated[:i] + CAP_BEGIN + "\n" + people_chart_caption() + "\n" + CAP_END + updated[j:]
    if a.check:
        if updated != text:
            print("README.md progress table or person-chart caption is out of date; run scripts/progress_status.py")
            sys.exit(1)
        print("README.md progress table up to date")
        return
    if updated != text:
        open(README, "w", encoding="utf-8").write(updated)
        print("updated README.md progress table")
    else:
        print("README.md progress table already up to date")


if __name__ == "__main__":
    main()
