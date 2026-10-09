# Open decisions

Choices that need Jason's sign-off. Items under "Decided" were signed off by Jason, except those marked "DECIDED (v8's pick)": method details that Jason delegated, decided for him on 2026-10-02 (P9, P11, P12, P13, P14–P31, S7) and 2026-10-08 (P32, P33). P8 and P10 were first v8's picks and were signed off by Jason on 2026-10-02 (P8 with one addition: interview-based fields are flagged). As of 2026-10-02 no item is open. When a new question comes up, add it under "Open". Where the repo needs *some* value to work before a decision, it uses the stated proposal and marks it PROPOSED, and nothing downstream treats it as settled. When a decision is made:

1. record it here under "Decided", with the date;
2. update the files it touches;
3. note it in `CHANGELOG.md`.

## Summary of recommendations (v8 agent, 2026-10-01)

The 19 recommendations below were decided on 2026-10-01; P6 and P7, added later, were decided on 2026-10-02. P8, P9 and S7 came out of the third people batch and were decided the same day as v8's picks (7:24 PM PT); Jason then signed off P8, adding the interview flag. P10 came out of the batch 3 lens audit, was a v8's pick, and was signed off by Jason on 2026-10-02 (8:23 PM PT). P11, P12 and P13 came out of the batch 4 lens audit and were decided the same day as v8's picks. P14–P28 came out of the two stage 3 lens audits (stage 3-a and 3-b, 2026-10-02) and were decided the same day as v8's picks, with the parent agent's rulings. P29 came out of the lens run on the stage 3-b rulings and was decided the same day as v8's pick. P30 came out of lens's runs on the two rulings packets (v8.a and v8.b's P29) and was decided the same day as v8's pick; it also corrects one P29 date and replaces P29's list of scientists. Evidence files are in `reports/` (`r7_bucket_spotcheck.csv`, `r7_field_string_review.csv`).

| ID | Recommendation | Confidence | Status |
|---|---|---|---|
| R1 | O'Keeffe: core | high | decided 2026-10-01 |
| R2 | Wrights: exclude both, as v7.1 did | medium-high | decided 2026-10-01 |
| R3 | "Brian Maynard Smith": display fix to John Maynard Smith | high | decided 2026-10-01 |
| R4 | Confirm all four merges | high | decided 2026-10-01 |
| R5 | Confirm the three pairs are different people | high | decided 2026-10-01 |
| R6 | Approve the F ≥ 3 plan; all 9 core (Vint Cerf is the judgment call) | high (count), medium (Cerf) | decided 2026-10-01 |
| R7 | Accept the keyword rules plus six small rule fixes; v7 mapping not on disk | medium-high | decided 2026-10-01 |
| R8 | Approve the id freeze rule as written | high | decided 2026-10-01 |
| P1 | Approve the 0–4 scale | medium-high | decided 2026-10-01 |
| P2 | Approve; key on first lasting contribution, keep birth year too | medium-high | decided 2026-10-01 |
| P3 | Approve, with a country-to-region table (settle MENA, Iran, Afghanistan) | medium | decided 2026-10-01 |
| P4 | Axis test: A_locus ≤ 1 and B_cause (in the work) ≥ 3, both at certainty ≥ 0.7 | medium | decided 2026-10-01; B amended by P6 |
| P5 | Approve: only a named human sets "reviewed" | high | decided 2026-10-01 |
| S1 | Approve "Interventionist personal theism" | medium-high | decided 2026-10-01 |
| S2 | Use the full original label, found in V6: "Pantheism (Spinozistic/naturalistic 'God = Universe')" | high | decided 2026-10-01 |
| S3 | Freeze v7.1 scores as baseline; open revised scoring after the first pool, with cites per axis and two scorers | medium | decided 2026-10-01 |
| S4 | Keep the 77 codes closed for v8; batch any new codes into one schema bump | medium-high | decided 2026-10-01 |
| S5 | Change both to "neighbor (easily confused)" | medium | decided 2026-10-01 |
| S6 | Two-part PANT test; host tradition or PANENT for Advaita/Kabbalah; STOIC for Stoics | medium | decided 2026-10-01 |
| P6 | P4: score B_cause on the person's account of nature; TODO (not UNKNOWN) when the test has no branch | medium | decided 2026-10-02 (added by the people run) |
| P7 | E_scope domain: score on the world's order (this-world events); salvation and election go to C | medium | decided 2026-10-02, option 1 (added by the lens audit, run 2) |
| P8 | Recorded interviews: the person's own first-person words, basis recorded_interview, ceiling 0.7; paraphrase-only cannot score alone; interview-based fields flagged "(interview)" | medium-high | DECIDED by Jason 2026-10-02: keep, flag interview-based fields (added by the people run, batch 3) |
| P9 | Batch 3 record calls: keep Heisenberg's §7 cap; Pasteur era literal from 1848; Pasteur died at Marnes-la-Coquette (alt. Saint-Cloud); Herschel unchanged | medium-high | decided 2026-10-02, v8's pick (added by the people run, batch 3) |
| P10 | mid_basin certainty is capped only by the axes its branch uses (false via A ≥ 3: A only) | medium-high | DECIDED by Jason 2026-10-02 (first v8's pick; added by the lens audit, batch 3) |
| P11 | Text Creation Partnership (EEBO-, ECCO-, Evans-TCP) transcriptions are authoritative copies under CODING_GUIDE §7; cite the TCP id and the original edition | medium-high | DECIDED (v8's pick) 2026-10-02 (added by the lens audit, batch 4) |
| P12 | A contribution dated as a range sets first_lasting_contribution_year by its start year | medium-high | DECIDED (v8's pick) 2026-10-02 (added by the lens audit, batch 4) |
| P13 | first_lasting_contribution_year is the earliest year among the listed lasting contributions; unlisted early work counts only once it is listed, with a source, as itself lasting | medium-high | DECIDED (v8's pick) 2026-10-02 (added by the lens audit, batch 4) |
| P14 | Stub systems: no "stub, so don't code" rule; code at the evidence's certainty, flag the stub, add it to the S7 backlog | medium-high | DECIDED (v8's pick) 2026-10-02 (stage 3 lens audit, ruling 1) |
| P15 | Fact certainty: one reliable source gives at most 0.7; 1.0 needs two independent reliable sources or a primary document; name-order or name-form disagreement gives 0.7 | medium-high | DECIDED (v8's pick) 2026-10-02 (stage 3 lens audit, ruling 2) |
| P16 | B_cause needs a statement about nature or the physical world; pure-mathematics Platonism alone gives BELOW_THRESHOLD | medium-high | DECIDED (v8's pick) 2026-10-02 (stage 3 lens audit, ruling 3) |
| P17 | First lasting year: P12 and P13 stand; the list must include the earliest lasting contribution the sources read name | medium-high | DECIDED (v8's pick) 2026-10-02 (stage 3 lens audit, ruling 4) |
| P18 | Quote kinds: add autobiography, unpublished manuscript, document in own hand; reported speech cannot score alone; kind does not change the basis table | medium-high | DECIDED (v8's pick) 2026-10-02 (stage 3 lens audit, ruling 5) |
| P19 | Sentinels: UNKNOWN = sources say nothing on the point; BELOW_THRESHOLD = some weak or indirect evidence; precedence rules for mid_basin and E/D | medium-high | DECIDED (v8's pick) 2026-10-02 (stage 3 lens audit, ruling 6) |
| P20 | A_locus when belief changed: primary_system and the axes describe the worldview during the major work (the working years), later shifts go in changes_over_life, a retrospective self-report about an earlier period is capped at 0.7; agnostic with no locus view is BELOW_THRESHOLD; an explicit denial is scored | medium-high | DECIDED (v8's pick) 2026-10-02 (stage 3 lens audit, ruling 7) |
| P21 | Kind lists: institution kind research institute; schooling stage is the level (adds elementary school) plus optional run_by; scholarly edition vs primary facsimile defined | medium-high | DECIDED (v8's pick) 2026-10-02 (stage 3 lens audit, ruling 8) |
| P22 | Stage 3-a stub cases: ruling 1 covers them; SCEPT, KANT, RATN, EMPIR and every stub a stage 3 record leads with go on the S7 backlog; "from the world" means a posteriori arguments; RATN gets a one-line use_when | medium-high | DECIDED (v8's pick) 2026-10-02 (stage 3 lens audit, ruling 9) |
| P23 | First lasting year: no coder-chosen defining work; the earliest listed item that is itself lasting sets the year; no pruning to move the year | high | DECIDED (v8's pick) 2026-10-02 (stage 3 lens audit, ruling 10) |
| P24 | Certainty 0.5 also covers inference from the person's work or conduct with no direct statement, with the basis recorded as an inference (inference_from_work) | medium-high | DECIDED (v8's pick) 2026-10-02 (stage 3 lens audit, ruling 11) |
| P25 | Source conflicts: reliable sources that disagree give 0.5 with the alternative named; a one-source detail inside a two-source 1.0 value goes in its own note at 0.7, or the field is capped at 0.7 | medium-high | DECIDED (v8's pick) 2026-10-02 (stage 3 lens audit, ruling 12) |
| P26 | Sources: Spinoza's Ethics standard is Kisner (0.7 until checked; "Kisner check pending"); TTP by chapter and Bruder section (Gutenberg only with a label and a TODO); Britannica's AI "Top Questions" boxes cannot be cited; secondary-reached quotes must be checked against the primary text | medium-high | DECIDED (v8's pick) 2026-10-02 (stage 3 lens audit, ruling 13) |
| P27 | Coding: DEISM requires rejecting revelation as a source of truth; anchor sentences for "LIO-type view", D 2 and the B 2/B 3 line | medium | DECIDED (v8's pick) 2026-10-02 (stage 3 lens audit, ruling 14) |
| P28 | Kinds: letter written for circulation is "published letter" (counts as published work); unpublished finished treatise and the Pensées are "unpublished manuscript" | medium-high | DECIDED (v8's pick) 2026-10-02 (stage 3 lens audit, ruling 15) |
| P29 | Stage 3-b follow-ups: §1 governs secondary_system; hedged self-reports stay at 0.5; a later disavowal caps the disowned wording at 0.5; contributions dated by first publication (replaced by P30's dating rule); one period per record (first to last listed lasting contribution); "scientist" = a listed lasting contribution in natural science, same for B and E (test refined by P30); derived sources are not independent | medium | DECIDED (v8's pick) 2026-10-02 (from the v8.b rulings audit) |
| P30 | Stage 3 rulings round 3: corrects P29's coral-reef date to 1837; contributions dated by the earliest documented public statement (classified and posthumous work, period ends); age = event year − birth year; real-dispute test; first LIO-type view checks the earliest works; tense rule; same-evidence rule only for the same point; mid_basin cap with alternatives; scientist = a lasting theory or result about physical or natural systems (Noether is one); Kisner cap scope; published letter; B 3's free-will exception; one Gutenberg TODO per field; ruling questions only for primary_system, A, B, mid_basin or the passes; addendum (11:20 PM PT): E follows P19 for scientists, the latest lasting work must be listed, undated items by composition date, range ends, posthumous items, major_work_period is the one span | medium-high | DECIDED (v8's pick) 2026-10-02 (from lens's runs on the v8.a and v8.b rulings packets) |
| P31 | Continuity rule: the span dates the worldview being coded; evidence from any adult year counts at its normal certainty unless changes_over_life documents a change of view between the span and the evidence (then retrospective cap or changes_over_life); a change inside the span: code the phase with the most listed lasting contributions (tie to the later), the other phase in changes_over_life plus a coder_notes delta; childhood evidence stays off-point; replaces P29's out-of-span clause and P30 addendum e's posthumous restriction; a change splits the span only if it bears on primary_system or A–E (Newton ruling), phases counted with P30 #1 dates | medium-high | DECIDED (v8's pick) 2026-10-02 (from the P30 span-alignment audit) |
| P32 | Work order after the first 12 stage 3 records: finish the stage 2 leftovers (physical science 1600–1950, F ≥ 3), then everyone else with F ≥ 3 by F descending, then roster rank; no hand-picking | medium-high | DECIDED (v8's pick) 2026-10-08 (stage 3 batch C) |
| P33 | Inventors and the scientist test (P30): a device or invention is not a theory or result about physical or natural systems; an inventor is a scientist only if a listed lasting contribution is a theory or result, otherwise B needs a statement about nature (P16) | medium | DECIDED (v8's pick) 2026-10-08 (stage 3 batch C, Bell) |
| P34 | Denominators: people who can't be scored for an analysis are excluded from its denominator and reported separately as not scorable | high | DECIDED (Jason) 2026-10-08 |
| P35 | B from working science only: a scientist's B inferred only from their work (the coder's inference or a scholar's reconstruction), with no statement of their own on law and exception, is B 3 at 0.5 with 4 as the named alternative, never 4 | medium-high | DECIDED (v8's pick) 2026-10-08 (lens audit of batch C, ruling R1) |
| P36 | A scholar's reconstruction of the person's free will or contingency triggers the B 3 anchor (P30 #14) like the person's own statement, capped at 0.5 | medium | DECIDED (v8's pick) 2026-10-08 (lens audit of batch C, ruling R2) |
| P37 | The README and person chart mark no focus region | high | DECIDED (Jason) 2026-10-08 |
| S7 | System backlog: ATHE, AGNOS, IDEAL first; French spiritualism listed as a system to consider, no file | medium-high | decided 2026-10-02, v8's pick (added by the people run, batch 3) |

**Decided 2026-10-01:** R1, R2, R3, R4, R5 and S2 were approved together as recommended. The other 13 were decided later the same day (10:55 PM PT): R6 with all 9 names core, Vint Cerf included; R7 with the six fixes; the rest as recommended. For P4, deists pass the test, and this is recorded as a stated consequence with no exclusion. Each item is under "Decided" with what changed.

## Open

None. P8–P31 and S7 were decided on 2026-10-02, and P32–P37 on 2026-10-08; all are listed under "Decided".


## Decided

All 52 items, in id order (P6–P37 are placed after P5, S7 after S6).

### R1. Georgia O'Keeffe's status
**Decided 2026-10-01 by Jason (approved as recommended):** Georgia O'Keeffe is `core`. Set in `data/roster/status_overrides.csv`; the rebuild writes the decision into her `notes`.

The original question and the recommendation are kept below for the record.
v7.1 left her status blank. Its headline count says 432 core, but only 431 rows are tagged core, which suggests she was meant to be core. v8 marks her `needs status (blank in v7)` and assumes nothing.
**Options:** core / provisional / review.

**Recommendation (v8 agent, 2026-10-01):** **core.** Confidence: high.

- The v7.1 headline is "Status: core / provisional / review" = "432 / 33 / 17" (data book, Headline counts; in `data/sources/v7_1/neuresthetics_v7_combined.json`). 432 + 33 + 17 = 482, the whole roster. The roster table itself has 431 core, 33 provisional, 17 review and one blank, which is O'Keeffe (rank 57: `["57", "Georgia O'Keeffe", "art", "4", "core (3–4)", "", "Georgia O-Keeffe (4)"]`). The headline only adds up if she is core. Note that "core (3–4)" in that row is the frequency band, not the status.
- No v7 or V6 list gives her any other status. The definition-pass notes table that follows the roster (19 review notes, 2 exclusions, merges) does not name her. The Word data book has the same blank. In V6 she appears in the raw lists, the aggregate (`V6_(history)/V6/GeniiLists/geniiAggregateSortFreq.csv`, F 4), `geniiTotalByAlpha.csv` and the name list in the V6 paper. None of these has a status column.
- A likely cause: she is the only name in the v7 roster with an apostrophe. No raw list uses an apostrophe ("O-Keeffe", "OKeeffe"), because the generation prompt said names must contain no `'` (`V6_(history)/V6/geniusDefinition.json`, csv_compilation_guidelines). The data book says statuses "from the definition pass" were joined onto the master list. A blank on the one name whose spelling changed at display time looks like a failed join. This is an inference, not a record.
- v7.1's status rules don't point anywhere else. She is not a contemporary (1887–1986, https://www.britannica.com/biography/Georgia-OKeeffe), and there is no "paradigm-shift bar is arguable" note.
- v8: F 4 (DeepSeek, Gemini, GPT, Grok; Claude does not list her), rank 99, so she is in the F ≥ 3 primary analysis. Raw strings: "Georgia O-Keeffe" (DeepSeek, Gemini, Grok), "Georgia-OKeeffe" (GPT), "O-Keeffe-Georgia" (Gemini, second listing).
- If approved: add a status input to `rebuild_roster.py` (for example a small `status_overrides.csv`), since statuses are currently only carried from v7. Not done here.

### R2. Wilbur and Orville Wright
**Decided 2026-10-01 by Jason (approved as recommended):** Orville and Wilbur Wright are excluded as part of the collective, as in v7.1. Two `exclude` rows in `curated_aliases.csv` (the old `separate` row is removed); the rebuild lists them under exclusions in `merge_log.csv` and the v7→v8 diff. Ids `wright-orville` and `wright-wilbur` are retired.

The original question and the recommendation are kept below for the record.
v7.1 excluded "Wright Brothers" as a collective. In the raw lists, Claude names them as two individuals under a "Wright Brothers - " prefix, and Gemini also lists them individually. v8 keeps them as two people with status `new — needs status`.
**Options:** keep both as individuals; exclude both as a collective; keep one record for joint credit (not supported by the schema).

**Recommendation (v8 agent, 2026-10-01):** **exclude both, as v7.1 did.** Confidence: medium-high.

- v7.1 rule: "Excluded: mastery without originality, transient fame, collectives, non-persons" (two-lane paper, Genius). The data book's notes table has `["exclude", "Wright Brothers", "invention", "Collective/team — excluded by operational definition"]`.
- The prompt the five models were given names this exact case: "Groups or collaborative entities: Achievements attributed to collectives rather than individual contributions (e.g., bands or teams like the Beatles or the Wright Brothers)" (`V6_(history)/V6/geniusDefinition.json`, exclusion_criteria).
- How the raw lists name them: DeepSeek "Wright Brothers"; GPT "Wright-Brothers"; Claude "Wright Brothers - Wilbur Wright" and "Wright Brothers - Orville Wright"; Gemini "Orville Wright", "Wilbur Wright", "Wright-Orville", "Wright-Wilbur"; Grok does not list them. So 4 of 5 models listed them, and 3 of those 4 framed them as "the Wright Brothers".
- The airplane is credited to the pair, and nothing on the lists separates one brother's contribution from the other's. That is the case the rule was written for. Pairs with separable work (Marie and Pierre Curie) are a different case and are already listed individually.
- Effect: none on the primary analysis today. Both are F 2. If the collective rows were credited to each brother, each would be F 4 and would enter the F ≥ 3 analysis, so the choice matters if the rule changes later.
- If approved: add `Orville Wright` and `Wilbur Wright` as `exclude` rows in `curated_aliases.csv` (replacing the `separate` row), rebuild, and retire the ids `wright-orville` and `wright-wilbur` (no person files, so not frozen).

### R3. "Brian Maynard Smith"
**Decided 2026-10-01 by Jason (approved as recommended):** GPT's "Brian-Maynard-Smith" displays as John Maynard Smith. The `flag` row became a `display_fix` row; the raw string stays in `alias_map.csv` and `aliases_merged`. Id `smith-brian-maynard` is retired and `maynard-smith-john` added through `id_overrides.csv`.

The original question and the recommendation are kept below for the record.
Listed by GPT only. Probably means John Maynard Smith, the evolutionary biologist. Kept as listed and flagged.
**Options:** treat as John Maynard Smith (add a `display_fix` or merge if he appears elsewhere); exclude as a model error; keep as is.

**Recommendation (v8 agent, 2026-10-01):** **treat as John Maynard Smith with a `display_fix`.** Confidence: high that this is who GPT meant; medium on whether to correct a model's error rather than exclude it.

- John Maynard Smith (1920–2004), British evolutionary biologist, evolutionarily stable strategies (https://www.nature.com/articles/429258a; https://www.kyotoprize.org/en/laureates/john_maynard_smith/).
- He is on none of the five raw lists. "Maynard" appears only as "John Maynard Keynes" (Claude, DeepSeek, GPT, Gemini) and as GPT's "Brian-Maynard-Smith" (field `evolutionary-biology`). So a merge has no target. Only a display fix is possible.
- A web search found no notable "Brian Maynard Smith". The only hits were private individuals in company registers and a lost-contact notice.
- GPT's field matches John Maynard Smith exactly, and the curated file already corrects model misspellings with `display_fix` (for example "Gabriel Mistral" → "Gabriela Mistral", "Albert Hofman" → "Albert Hofmann").
- Effect: F stays 1 (GPT only), so this doesn't touch the primary analysis. The raw string stays in `alias_map.csv`.
- If approved: change the `flag` row for `Brian-Maynard-Smith` in `curated_aliases.csv` to `display_fix` → `John Maynard Smith`, with the reason "GPT wrote 'Brian'; field matches John Maynard Smith; no Brian Maynard Smith found". Then rebuild and re-run `assign_ids.py`. The unused id `smith-brian-maynard` would be retired. "Maynard Smith" is a compound family name, so the new id needs an `id_overrides.csv` row (`maynard-smith-john`). No person file exists, so under R8 the id isn't frozen.

### R4. Merges to confirm
**Decided 2026-10-01 by Jason (approved as recommended):** The four merges are confirmed. Their rows in `curated_aliases.csv` now have confidence `confirmed`, and the reason names the date and R4.

The original question and the recommendation are kept below for the record.
These are in `curated_aliases.csv` with confidence `high`. Each one decides that two names are one person, so they should get a human look:
- Bob Kahn → Robert Kahn
- Elizabeth Anscombe → G.E.M. Anscombe
- Benedict de Spinoza → Baruch Spinoza
- Buddha → Siddhartha Gautama

**Recommendation (v8 agent, 2026-10-01):** **confirm all four merges.** Confidence: high.

| merge | how the raw lists name them | effect on F | source |
|---|---|---|---|
| Bob Kahn → Robert Kahn | Claude "Robert Kahn"; DeepSeek "Bob Kahn" (both computer science) | 1 + 1 → 2 | Britannica, "Robert Kahn": "one of the principal architects, with Vinton Cerf, of the Internet", 2004 Turing Award for TCP/IP (https://www.britannica.com/biography/Robert-Elliot-Kahn). ACM lists him as "Robert E Kahn" (https://amturing.acm.org/award_winners/kahn_4598637.cfm). |
| Elizabeth Anscombe / G.E.M. Anscombe | DeepSeek only, listed twice: "Elizabeth Anscombe" and "G.E.M. Anscombe" | stays 1 (same-model duplicate removed) | SEP, "Gertrude Elizabeth Margaret Anscombe", which calls her "G. E. M. Anscombe" (https://plato.stanford.edu/entries/anscombe/). |
| Benedict de Spinoza → Baruch Spinoza | Claude, DeepSeek, Gemini, GPT, Grok all "Baruch Spinoza" (with hyphen and order variants); DeepSeek also "Benedict de Spinoza" | stays 5 (same-model duplicate removed) | SEP: "Bento (in Hebrew, Baruch; in Latin, Benedictus) Spinoza" (https://plato.stanford.edu/entries/spinoza/). Britannica titles him "Benedict de Spinoza" (https://www.britannica.com/biography/Benedict-de-Spinoza). |
| Buddha → Siddhartha Gautama | Claude "Buddha"; Gemini "Siddhartha Gautama-Buddha"; DeepSeek and Grok "Siddhartha Gautama" | 3 → 4 (adds Claude) | Britannica, "Buddha": clan name Gautama, personal name Siddhartha (https://www.britannica.com/biography/Buddha-founder-of-Buddhism). |

- Only two of the four change a count: Kahn (1 → 2) and Buddha (3 → 4). Buddha is in the F ≥ 3 analysis either way.
- One small thing: the merge keeps "Elizabeth Anscombe" as the display name (v8 canonical-name rule 3), while the curated row lists "G.E.M. Anscombe" as the target. Both name the same person. If Jason prefers the form most of the literature uses, add a `display_fix` to "G.E.M. Anscombe". This is cosmetic.
- No data change is needed if approved. Mark the four rows as confirmed (for example in the `reason` column).

### R5. Similarity pairs left separate
**Decided 2026-10-01 by Jason (approved as recommended):** The three pairs are different people. Each is a `separate` row with confidence `confirmed`, so the similarity scan no longer lists them.

The original question and the recommendation are kept below for the record.
The automatic scan flagged these pairs. They are left as different people, which looks right, but a human should confirm:
- Ken Thompson / E.P. Thompson
- Edward Said / Edward Sapir
- Marc Bloch / Maurice Bloch

**Recommendation (v8 agent, 2026-10-01):** **confirm: all three pairs are different people.** Confidence: high.

- Ken Thompson (born 1943): American computer scientist, co-creator of Unix, 1983 Turing Award (https://www.britannica.com/biography/Kenneth-Lane-Thompson). E. P. Thompson (1924–1993): British social historian, *The Making of the English Working Class* (1963) (https://www.britannica.com/biography/E-P-Thompson).
- Edward Said (1935–2003): Palestinian American literary critic (https://www.britannica.com/biography/Edward-Said). Edward Sapir (1884–1939): American linguist and anthropologist (https://www.britannica.com/biography/Edward-Sapir).
- Marc Bloch (1886–1944): French medieval historian, killed by the Germans in 1944 (https://www.britannica.com/biography/Marc-Bloch). Maurice Bloch (born 1939): British anthropologist, LSE emeritus (https://www.lse.ac.uk/people/maurice-bloch).
- No data change needed. They are already `separate` in effect (never merged).

### R6. Statuses for the 898 new names
**Decided 2026-10-01 by Jason (approved as recommended, Vint Cerf included):** all 9 new F ≥ 3 names are `core`. Nine rows in `data/roster/status_overrides.csv`; the other 889 new names stay `new — needs status`. Core is now 441.

The original question and the recommendation are kept below for the record.
v8 adds 898 people with status `new — needs status` (900 before R2 excluded the two Wrights on 2026-10-01).
**Proposal:** assign a status now only to the new names with F ≥ 3, because only they enter the primary analysis. There are 9: Georg Wilhelm Friedrich Hegel (F 4), Duns Scotus, Edward O. Wilson, John Nash, Jorge Luis Borges, Laozi, Ludwig Mies van der Rohe, Paul Cézanne and Vint Cerf (F 3). The other 889 (F 1–2) would stay `new — needs status` until sensitivity analyses need them.

**Recommendation (v8 agent, 2026-10-01):** **approve the plan (status only for the F ≥ 3 new names): 9 core, with Vint Cerf the one judgment call.** Confidence: high on the count, high on 8 statuses, medium on Cerf.

- Count verified against `data/roster/roster.csv`: exactly 9 rows have status `new — needs status` and F ≥ 3. They match the list above (Hegel F 4; the other eight F 3).
- The v7.1 status rules, verbatim:
  - Two-lane paper, Genius: "Inclusion needs lasting original impact on documented criteria. Excluded: mastery without originality, transient fame, collectives, non-persons. Contemporaries may be provisional."
  - Data book, Dictionary: `["Core / provisional / review", "Definition-fit tags. Review = paradigm-shift bar is arguable.", "A"]`.
  - The generation prompt behind the lists adds the time test: "For contemporary figures lacking 50+ year distance, use provisional inclusion based on expert consensus, citation trajectories, or projected impact via historiometric methods" (`V6_(history)/V6/geniusDefinition.json`).
- How v7 applied them: the 33 provisional names are all recent (Hinton, Doudna, Tao, Perelman, Musk...), but some living people were core (Tim Berners-Lee, Roger Penrose, Donald Knuth, Andrew Wiles). So the working rule looks like "recent contribution", not "alive". (`docs/METHOD.md` §2.7 glosses provisional as "definition fit arguable"; the v7.1 text ties it to contemporaries.)

| name | dates | proposal | reason |
|---|---|---|---|
| Georg Wilhelm Friedrich Hegel | 1770–1831 | core | Canonical philosopher; no arguable note. |
| Duns Scotus | c. 1266–1308 | core | Canonical scholastic. |
| Edward O. Wilson | 1929–2021 | core | Main work (*Sociobiology*, 1975) is over 50 years old. |
| John Nash | 1928–2015 | core | Game-theory work from 1950; Nobel 1994. |
| Jorge Luis Borges | 1899–1986 | core | *Ficciones* (1944). |
| Laozi | fl. 6th c. BCE (traditional) | core, with a note | Britannica: "remains an obscure figure". Historicity is debated, but v7 kept Homer, Pythagoras and Sun Tzu as core, so the precedent is core. |
| Ludwig Mies van der Rohe | 1886–1969 | core | |
| Paul Cézanne | 1839–1906 | core | |
| Vint Cerf | born 1943 | core (alternative: provisional) | Living, but TCP/IP dates from 1973–74, over 50 years ago, and v7 kept Berners-Lee (living, 1989) as core. Credit is shared with Robert Kahn, but both are named individuals, so this is not a collective. |

Sources: Britannica biographies (https://www.britannica.com/biography/ plus Georg-Wilhelm-Friedrich-Hegel, Blessed-John-Duns-Scotus, Edward-O-Wilson, John-Nash, Jorge-Luis-Borges, Laozi, Ludwig-Mies-van-der-Rohe, Paul-Cezanne, Vinton-Cerf).

- If approved: this needs the same status input as R1.

### R7. Field buckets
**Decided 2026-10-01 by Jason (approved as recommended):** the keyword rules stay, with six fixes in `rebuild_roster.py`: science studies with philosophy → philosophy; explor/astronaut wins over space; political thought and social thought → politics / law / military; David Harvey → social science; Jan Swammerdam → biology. 31 rows changed bucket, listed in `reports/r7_bucket_changes.csv`.

The original question and the recommendation are kept below for the record.
v7's hand mapping of fields to buckets is not on disk. v8 uses keyword rules in `rebuild_roster.py` (21 buckets).
**Options:** accept the rules; supply the v7 mapping; revise the bucket list.

**Recommendation (v8 agent, 2026-10-01):** **accept the keyword rules, with six small rule fixes made as one reviewed change.** Confidence: medium-high.

- The v7 hand mapping is not on disk. I searched the v7 repo, the V6 history, the combined JSON, the Word files and the other copies under `/workspace`. The only bucket data is the v7.1 summary table ("11. Field distribution (coarse buckets)": 19 buckets with counts, for example philosophy 87, social science 49, "social science / politics" 7). No per-person mapping exists.
- Random spot-check of 30 roster rows (seed 20261001): 29 right, 1 wrong. Harriet Tubman's field "social thought-activism" lands in social science, while other activists (Malcolm X, Desmond Tutu) land in politics / law / military. Error rate 1/30 = 3% (95% interval about 0.1–17%). File: `reports/r7_bucket_spotcheck.csv`.
- Because 30 rows is a small sample, I also checked all 145 distinct field strings (`reports/r7_field_string_review.csv`). About 25 people (1.8%) are clearly in the wrong bucket, and about 20 more are debatable:
  - "science studies-philosophy" (12: Hempel, Nagel, Sellars, van Fraassen, Hacking...) → history, but "philosophy of science" (Popper, Kuhn) → philosophy;
  - "space-exploration" (5 astronauts) → invention / engineering, because "space" matches before "explor";
  - "political thought" puts rulers (Ashoka, Hammurabi, Cyrus, Qin Shi Huang, Ashurbanipal) in social science, while "politics" sends Lincoln and Washington to politics / law / military. Mandela, Gandhi and Martin Luther King Jr. (F 3–4) are in social science for the same reason;
  - Jan Swammerdam (microscopy → physics), David Harvey (geography-sociology → earth science), Jane Marcet and Mary Somerville ("science" → other).
- Only 4 F ≥ 3 people are affected (Mandela, Machiavelli, Gandhi, King), and all of those are debatable rather than clearly wrong.
- Proposed fixes, to be reviewed before applying, since they change `field_bucket` for about 45 rows: move "science studies" when paired with philosophy to philosophy; let "explor"/"astronaut" win over "space"; send "political thought", "social thought" and activism to one bucket (politics / law / military); add hand buckets for the handful of one-off strings. To compare with v7, map v8's "politics / law / military" to v7's "social science / politics".

### R8. Id freeze point
**Decided 2026-10-01 by Jason (approved as recommended):** an id freezes when its person file is created or when v8 is published, whichever comes first. Retired ids stay in `person_ids.csv` with a status other than `active`. Recorded in METHOD §3.2.

The original question and the recommendation are kept below for the record.
**Proposal (in force in METHOD §3.2):** an id freezes when its person file is created, or when v8 is published, whichever comes first. Before that, overrides may change ids.

**Recommendation (v8 agent, 2026-10-01):** **approve as written.** Confidence: high. Freezing an id once anything points at it (a person file) is standard practice for stable identifiers, and it's the simplest rule that never breaks a link. Before that point nothing depends on the id, so overrides are free. Add one line to METHOD §3.2: retired ids stay in `person_ids.csv` with a status other than `active`, so old links still resolve. The current `status` column already supports this.

### P1. LIO axis scale
**Decided 2026-10-01 by Jason (approved as recommended):** the LIO axes use the 0–4 scale (0 interventionist pole … 4 LIO pole), with certainty kept as a separate field. Schemas 1.1.

The original question and the recommendation are kept below for the record.
- 0 = interventionist pole
- 1 = leans interventionist
- 2 = mixed
- 3 = leans LIO
- 4 = LIO pole

v7.1 defined the poles but no scale. Used in `worldview.lio_axes` and `systems/*/lio_axes`. PANT is scored on it as a demonstration. No person is scored yet.
**Options:** approve; use 0–2 or −2…+2; use the poles only, with a free-text position.

**Recommendation (v8 agent, 2026-10-01):** **approve 0–4.** Confidence: medium-high. v7.1 gives two poles per axis and no scale. Five ordered points with a "mixed" middle are the usual minimum for an ordinal rating that keeps a midpoint. 0–2 is too coarse to separate "leans" from "pole", which is exactly the difference the mid-basin test (P4) needs on B_cause. −2…+2 carries the same information, but the signs read as good and bad. Keep the certainty field separate from the score, as the schema already does.

### P2. Era buckets
**Decided 2026-10-01 by Jason (approved as recommended):** era buckets as listed, keyed on the year of first lasting contribution. An edge year goes to the later bucket, so 1950 is in "1950 on". Birth year stays in the record for a sensitivity check. Schemas 1.1.

The original question and the recommendation are kept below for the record.
The buckets are keyed on the year of the first lasting contribution:

| bucket | years |
|---|---|
| before -500 | before 500 BCE |
| -500 to 499 | 500 BCE to 499 CE |
| 500 to 1399 | |
| 1400 to 1599 | |
| 1600 to 1749 | |
| 1750 to 1849 | |
| 1850 to 1949 | |
| 1950 on | |

The edges are chosen so that the v7.1 first pool window (physical science 1600–1950) is a union of buckets.
**Options:** approve; key on birth year instead; use different edges.

**Recommendation (v8 agent, 2026-10-01):** **approve, keyed on first lasting contribution, and keep birth year in the record so a birth-year version can be computed for a sensitivity check.** Confidence: medium-high. The v7.1 first pool is defined by when the work was done ("Physical science 1600–1950"), so keying on the contribution year matches the study's own window. The proposed edges make that window a union of buckets (1600–1749, 1750–1849, 1850–1949). The one mismatch: "1950 on" starts at 1950, while the v7.1 window says "1600–1950". Write down that 1950 belongs to the later bucket.

### P3. Regions
**Decided 2026-10-01 by Jason (approved as recommended):** the 13 regions on modern borders, with the country-to-region table `data/reference/regions.csv` (UN M49). MENA = M49 Northern Africa + Western Asia + Iran; Afghanistan stays South Asia, as in M49. `validate_people.py` checks the table against the schema. Schemas 1.1.

The original question and the recommendation are kept below for the record.
The list is based on UN M49, applied to modern borders. It has 13 regions:

- Europe: Northern, Western, Southern, Eastern
- Middle East and North Africa
- Sub-Saharan Africa
- Asia: Central, South, East, Southeast
- North America
- Latin America and Caribbean
- Oceania

**Options:** approve; use historical cultural regions instead; use fewer regions.

**Recommendation (v8 agent, 2026-10-01):** **approve, with a published country-to-region table so coders don't guess.** Confidence: medium. UN M49 is the standard reproducible scheme, and modern borders avoid arguments over historical polities (the record already has `polity_then` for that). Two points to fix in the table: (1) M49 has no "Middle East and North Africa" region; it splits Northern Africa (Africa) from Western Asia (Asia). The proposed list merges them, which is common practice but should be listed country by country. (2) M49 puts Iran and Afghanistan in Southern Asia. So Persian-born figures, and Rumi (born at Balkh), would be "South Asia" unless the table moves Iran and Afghanistan to MENA or Central Asia. Decide that once, in the table.

### P4. Mid-basin: operational definition
**Decided 2026-10-01 by Jason (approved as recommended); B wording amended by P6 on 2026-10-02:** `mid_basin` is true when A_locus ≤ 1 and B_cause ≥ 3 (B scored for the domain of the work; since P6, on the person's account of nature), both at certainty ≥ 0.7; false when A_locus ≥ 3, or A_locus ≤ 1 with B_cause ≤ 1; otherwise UNKNOWN or BELOW_THRESHOLD (P6 split this branch: TODO with a note when the test has no branch, UNKNOWN only for an UNKNOWN axis, BELOW_THRESHOLD for an axis below 0.7). Deists pass the test; this is recorded in METHOD §1.1 as a stated consequence, with no exclusion.

The original question and the recommendation are kept below for the record.
The v7.1 papers use "mid-basin theists" and name the first pool (Faraday, Maxwell, Newton, Aquinas, Ibn Sina, Gödel) as a stress test, but give no test for membership. `worldview.mid_basin` stays `TODO` everywhere until there is one. That includes Faraday, even though v7.1 treats him as one.
**Possible definition, for discussion only:** primary system is theistic (CLASS_THEISM, CLTHEI, CHRIST, ISLAM, JUDA or similar) at certainty ≥ 0.7, *and* B_cause ≥ 3 in the domain of their scientific work.

**Recommendation (v8 agent, 2026-10-01):** **adopt an axis-based test, not a hand label.** Confidence: medium.

Every use of "mid-basin" in the v7.1 texts (two-lane paper, data book and neurology paper; the neurology paper has none):

1. "First coding pool: frequency ≥ 3, physical science 1600–1950, mid-basin theists coded first as a stress test." (two-lane paper, A3)
2. "Four limited claims Lane A is willing to carry now: […] the existence of first-rank mid-basin theists." (A3)
3. "May claim: Composition, timing, mid-basin exceptions, living-sample r." (lane table)
4. "Falsified by: […] mid-basin theists with early LIO-low childhoods who still compound." (lane table, Lane B)
5. "Mid-basin theists with first-rank physics had lawful form early, even if the word God stayed." / hurt by: "Faraday/Maxwell look like late professional lawfulness only." (predictions table)
6. "First pool: Physical science 1600–1950; mid-basin theists coded first (Faraday, Maxwell, Newton, Aquinas, Ibn Sina, Gödel)." (data book, coding rules)

None of these is a definition. The closest are the passages that say what the theists have in common: "Faraday and Maxwell are devout and lawful; they force the phrase working metaphysics rather than baptism" (A1), "Classical theism can sit mid-to-high on lawfulness without identity of God and world" (Lawful immanent order), "lawful form early, even if the word God stayed" (item 5), and the neurology paper's "A devout lawful physicist is predicted, not forbidden." Together they say: God is kept as a person distinct from the world, but the person's working model of nature has no exemptions.

Proposed test, using only fields the schema already has:

- `mid_basin = true` when A_locus ≤ 1 (God is a transcendent person, not the world) **and** B_cause ≥ 3 (law and regularity, no special cases) scored for the domain of the person's work, both at certainty ≥ 0.7.
- `false` when A_locus ≥ 3 (not a theist in this sense), or A_locus ≤ 1 with B_cause ≤ 1 (an interventionist working model).
- Otherwise `UNKNOWN` (axis scores missing or below 0.7) or `BELOW_THRESHOLD`.

Notes:
- "B_cause in the domain of the work" is the key part. Faraday may accept biblical miracles and still allow no exemptions in electromagnetism. Since `lio_axes` holds one score per axis, either score B for the working science and say so in the rationale, or add a `B_cause_in_work` field in a later schema version.
- The test doesn't require "first-rank". Use F ≥ 3 alongside it, since items 2 and 5 say "first-rank".
- Deists (DEISM) would usually pass this test. Jason should say whether they count as mid-basin theists or are reported separately.
- v7.1 gates its analysis at "certainty ≥ 0.6" (A3), but the coding scale has only 1.0 / 0.7 / 0.5, so ≥ 0.6 means ≥ 0.7 in practice. The proposed test uses 0.7.
- The first pool names Aquinas and Ibn Sina, who aren't physical scientists. So the term isn't limited to physics, and B should be scored for whatever their work was.

### P5. Who may set "reviewed"
**Decided 2026-10-01 by Jason (approved as recommended):** only a named human sets `reviewed`, with name and date in the `review` fields. Agents set `draft — unreviewed` or `example — unreviewed` only.

The original question and the recommendation are kept below for the record.
**Proposal:** only a named human reviewer. Agents stop at `draft — unreviewed`.

**Recommendation (v8 agent, 2026-10-01):** **approve.** Confidence: high. This is the standard two-person rule for research data: the producer doesn't sign off its own work. It also keeps the provenance trail honest, because `reviewed` then always names a person. Suggest recording the reviewer's name and date in the existing `review` fields, and letting agents set `draft — unreviewed` and `example — unreviewed` only.

### P6. P4: is B_cause scored on the person's account of nature?
**Decided 2026-10-02 (12:36 AM PT) by Jason (approved as proposed):** for the P4 test, B_cause is scored on the person's account of nature; theology-wide readings go in the B rationale. When both axes are scored at ≥ 0.7 but the test has no branch (A_locus = 2, or A_locus ≤ 1 with B_cause = 2), `mid_basin` is `TODO` with a note; `UNKNOWN` is used only when a needed axis is itself `UNKNOWN`, and `BELOW_THRESHOLD` when a needed axis is `BELOW_THRESHOLD` or only at 0.5. Updated: METHOD §1.1, CODING_GUIDE §6, the `mid_basin` schema description, the person template comment, `systems/CHRIST.md` coding guidance, and the Aquinas record (B 3, `mid_basin` true).

The original question and the proposal are kept below for the record.

P4 says B_cause is "scored for the domain of the person's work" (METHOD §1.1). For a natural scientist that domain is nature. For a theologian it is unclear: is the domain the person's account of the natural order, or their whole theology, miracles and grace included? The P4 recommendation note says "B should be scored for whatever their work was", which points to the whole theology, but the v7.1 passages it rests on ("devout and lawful", "Classical theism can sit mid-to-high on lawfulness") are about lawful nature.

The case that raised it is Thomas Aquinas (`people/a/aquinas-thomas.md`):

- Scored on his whole theology, B_cause = 2 at 1.0. He holds an order of secondary causes, and petition does not change God, but God "can do something outside this order created by Him, when He chooses" (ST I q. 105 a. 6), and the miracles are evidence for the faith. A = 1, so P4 gives neither true nor false.
- Scored on his account of nature only, B_cause = 3. That is the score the CLASS_THEISM system record gives Thomism, and with A = 1 the test gives true.

A second, smaller gap: P4's "otherwise UNKNOWN or BELOW_THRESHOLD" also catches B = 2 at high certainty. The recommendation note meant UNKNOWN for scores that are "missing or below 0.7". In the coding guide UNKNOWN means "researched, not in any reliable source", which does not fit a case where the evidence is in and the test has no branch for it. Until this was decided, the Aquinas record had `mid_basin: TODO` with a note.

**Options:**
1. Score B on the person's account of the natural order, for everyone. Theological miracles count against B only when they reach into the person's account of nature.
2. Score B on the whole of the person's work, as now. Then decide what a B = 2 result is: false, a new "mixed" outcome, or TODO/UNKNOWN.
3. Keep one B score, but add a `B_cause_in_nature` field in a later schema version (the P4 note already floated a `B_cause_in_work` field) and run the test on that field.

**Proposal (people run, 2026-10-02, PROPOSED only):** option 1, with the theology-wide reading kept in the B rationale. The v7.1 texts that define the group are about lawful nature. Under option 1, Aquinas would be B 3 and mid_basin true; Ibn Sina is unchanged (B 3 either way). Confidence: medium. Also settle the label for "evidence complete, test has no branch" (suggest TODO with a note, not UNKNOWN).

### P7. Which domain is E_scope scored on?
**Decided 2026-10-02 (1:52 AM PT) by Jason (option 1):** E_scope is scored on the world's order: which beings and events, from stars to insects to humans, fall under one set of rules, and whether the person's account of this-world events keeps hidden exceptions for an in-group (for example in-group fortune, or favour in nature or providence). Salvation, reward and punishment, and the scope of the moral community are not scored on E. They belong to C_ledger. This avoids counting reward and punishment twice and matches P6 (B_cause scored on the account of nature). The v7.1 poles are unchanged: 0 "Hidden exceptions for an in-group", 4 "Same rules for stars, insects, humans". Closes lens audit run 2 finding #23 (raised 2026-10-02 by the independent audit, lens, run 2).

Updated: CODING_GUIDE §6 (the interim rule replaced by the final rule, with examples), METHOD §1.1, the `E_scope` descriptions in both schemas (DATA_DICTIONARY regenerated), the person and system templates, and the stub generator (every stub's E_scope now carries a note). E_scope rescored from the sources already in each record:

| Record | before | after | note |
|---|---|---|---|
| Aquinas | 2 (0.7) | 3 (0.7) | universal providence over individual creatures (ST I q. 22 a. 2); miracles the limited exception; 2 is the named alternative (providence over the just, I q. 22 a. 2 ad 4) |
| Faraday | 1 (0.5) | 3 (0.5) | God's "definite laws" for all matter; no favour in events in his own words; biblical miracles accepted |
| Newton | 3 (0.7) | 3 (0.7) | unchanged; capped by a named alternative (2: petition for "blessings of this life" in a private manuscript) |
| Ibn Sina | 3 (0.5) | 3 (0.7) | the heavens do not act "for our sake" (his own text); the prophet the limited exception; 4 the named alternative |
| Maxwell | TODO | 3 (0.5) | the same laws in Sirius and on earth, human will within law; no text on favour in events |
| Gödel | TODO | 3 (0.5) | "order reign in everything"; the same psychic capacities in every human; letters few |
| CHRIST, ISLAM, JUDA | 1 (0.5) | 1 (0.5) | same value, rescored on this-world acts for particular people (miracles, answered petition, acts in Israel's history); salvation, election and community moved to C |
| CLTHEI | 1 (0.5) | 1 (0.5) | unchanged; already scored on answered petition |
| CLASS_THEISM | 3 (0.5) | 3 (0.5) | same value; salvation dropped from the rationale; miracles and immaterial souls the limits |
| DEISM | 3 (0.7) | 3 (0.7) | same value, rescored on non-intervention instead of universal natural religion |
| STOIC | 3 (0.7) | 4 (0.7), then 3 (0.7) | under P7 the moral-community limit moves to C, giving 4. Later the same day (lens runs 2–3, #97), Seneca's effective prayer (SEP Seneca §5.3) was counted as the stated, limited exception on both B and E, so 3, with 4 the named alternative (see `reports/audit_2026-10-02.md`, Runs 2–3 combined) |
| PLATO, PANT | 3, 4 | unchanged | already scored on the world's order; not edited |

No `mid_basin` result changed (the P4 test uses only A_locus and B_cause). The 0.7 interim caps are gone; where a certainty is still 0.7, it is because of a named alternative under the new rule (CODING_GUIDE §3).

The original question and the recommendation are kept below for the record.

**The question.** E_scope is the fifth LIO axis. The records do not score it on the same domain:

- Newton's E is scored on natural philosophy only (the same causes for man and beast, Europe and America, kitchen fire and sun). His judgement theology is scored on C.
- Faraday's E is scored on the scope of salvation and church membership (a "very small & despised sect").
- Aquinas's E is scored on both, and the salvation side (reprobation; revealed truths needed for salvation) pulls it to 2.

So the axis is not comparable across records.

**What v7.1 says.** Verbatim, from the data book, section 4 "LIO axes (person-level)", table row "E Scope" (`data/sources/v7_1/neuresthetics_v7_combined.json`, `documents.data_book.content.tables[2]`):

| Axis | Interventionist pole | LIO pole |
|---|---|---|
| E Scope | Hidden exceptions for an in-group | Same rules for stars, insects, humans |

That is the only definition. The two papers do not name the axis, but they use the same idea:

- The two-lane paper, "Lawful immanent order": "High LIO: regular, non-intervening cosmos, no personal moral ledger, observation outranks revelation, no reserved exemptions."
- The neurology sister paper (V7.1-N), on the interventionist prior: "some observations are allowed to stand outside the lawful generative model. Weather, illness, victory, and in-group fortune can be attributed to an agent who is not bound by the rest of the model. That is high precision on exemptions."

v8 adds only the 0–4 scale (P1): 0 at the interventionist pole, 1 leans interventionist, 2 mixed or both poles in different domains, 3 leans LIO with a stated, limited exception, and 4 at the LIO pole. The schema and `docs/DATA_DICTIONARY.md` describe `E_scope` as "E Scope: hidden exceptions for an in-group (0) ... same rules for stars, insects, humans (4)." None of these texts says whether salvation is in scope.

**How E is scored now** (record, score, certainty, domain):

| Record | E | certainty | domain scored |
|---|---|---|---|
| Newton | 3 | 1.0 → 0.7 (interim) | natural philosophy only; judgement theology put on C |
| Aquinas | 2 | 1.0 → 0.7 (interim) | both: one providence and natural law for all (LIO side), plus reprobation and salvation by revealed truth (in-group side) |
| Faraday | 1 | 0.5 | salvation and church membership (sect); science noted only as "not 0" |
| Ibn Sina | 3 | 0.5 | both: one graded order of nature, and knowledge and bliss open to all who work for them; prophet as the limited exception |
| Maxwell | TODO | | note covers both: the same laws for stars, earth and human will; nothing read on believers' exemption |
| Gödel | TODO | | note: religions vs religion, and "same psychic capacities" for every human |
| PANT | 4 | 1.0 | the natural order, human emotions included (no salvation concept) |
| CLASS_THEISM | 3 | 0.5 | both: one natural order; souls, creation ordered for rational beings, and salvation needing revealed truths as the limits |
| CLTHEI | 1 | 0.5 | this-world divine action for particular people (answered prayer) |
| CHRIST | 1 | 0.5 | salvation through Christ and the church, plus particular acts (prayer, incarnation) |
| ISLAM | 1 | 0.5 | revelation, prophecy and community (best community; people of the Book) |
| JUDA | 1 | 0.5 | covenant: the chosen people |
| DEISM | 3 | 0.7 | access to religious truth: natural religion open to all |
| STOIC | 3 | 0.7 | both: one causal order, and a moral community limited to gods and humans |
| PLATO | 3 | 0.7 | the order of forms and cosmos, with theurgy and the gods' help as partial exceptions |

**Options:**

1. **The world's order, this-world events only.** E asks two things:
   - Do the same rules govern every kind of thing, humans included ("stars, insects, humans")?
   - Does the person's account of what happens reserve exceptions for an in-group: fortune, protection, healing, answered petition or miracles for the favoured?

   Salvation, election and afterlife are scored on C (reward and punishment of persons), and the E rationale notes them. This parallels P6 for B.
2. **Salvation and moral community only.** E asks whether salvation, divine favour and moral standing are the same for all, or reserved for an in-group (the elect, a church, a chosen people). The natural order is left to B.
3. **Both, in one score.** Score the natural order and salvation together. If they differ, the score is 2 ("both poles in different domains"), or the more in-group of the two. This is what the Aquinas record does now.
4. **Split the axis** in a later schema version: `E_scope_nature` (option 1) and `E_scope_salvation` (option 2). The test and the tables use whichever is named.

**Effect on each person** (the scores under options 1–3 are the coder's estimates from evidence already in the records; each needs a rescore):

| Person | now | option 1 (world order) | option 2 (salvation) | option 3 (both) |
|---|---|---|---|---|
| Newton | 3 | 3, unchanged; can return to 1.0 (published texts) | about 2–3, at most 0.7: all are raised and "rewarded according to their deeds", and gentiles are judged by the law in their hearts, but redemption is through Christ, and this rests on private manuscripts | about 2, at most 0.7 |
| Aquinas | 2 | about 3: one providence over all things and one natural law, with miracles and immaterial souls as the limited exceptions (as CLASS_THEISM) | about 1: "God does reprobate some", and salvation needs revealed truths | 2, unchanged |
| Faraday | 1 | about 3, at 0.5: no petition or intervention in nature in his own words, and the same laws for all matter; no source addresses the axis directly | 1, unchanged | about 2 |
| Ibn Sina | 3 | 3 | 3 | 3 (unchanged under every option) |
| Maxwell | TODO | scorable now, about 3 (the same laws for stars and earth; human will acts at singular points within law) | stays TODO until Theerman 1986 and the 1884 Life are read | TODO |
| Gödel | TODO | TODO; the 1952 "same psychic capacities" letter points high | TODO until Wang 1996 is read | TODO |

No option changes a `mid_basin` result, since the P4 test uses only A_locus and B_cause. Under option 1, the systems scored on salvation or covenant scope would need a rescore: CHRIST, ISLAM, JUDA and the salvation part of CLASS_THEISM. CLTHEI would stay 1 (answered prayer is a this-world in-group exception), and STOIC might move to 4 (its named alternative). Under option 2, PANT, PLATO and the natural-order parts of CLASS_THEISM and STOIC would need a salvation reading that the sources barely give.

**Recommendation (people run, 2026-10-02, PROPOSED only): option 1.** Confidence: medium.

- The v7.1 LIO pole names kinds of beings under one set of rules ("stars, insects, humans"), which is the natural order.
- The papers place the interventionist pole in this-world events. "In-group fortune" is "attributed to an agent who is not bound by the rest of the model", and LIO means "no reserved exemptions" in a "regular, non-intervening cosmos".
- Reward and punishment of persons is already axis C, so scoring election and salvation on E would count the same feature twice.
- Option 1 matches P6 (B scored on the person's account of nature), so the five axes stay about the working model of the world.

The cost: "hidden exceptions for an in-group" can fairly be read to include election, and option 1 then scores Aquinas 3 and Faraday about 3, where a salvation reading gives 1. If Jason wants salvation scope tracked, option 4 keeps both without mixing them.

**If adopted:**
- Update CODING_GUIDE §6, the `E_scope` schema descriptions (then regenerate DATA_DICTIONARY) and METHOD.
- Rescore E for Aquinas and Faraday. Score Maxwell. Restore Newton's E certainty if nothing else caps it.
- Recheck E in the nine sourced system files.

### P8. Recorded interviews as evidence
**DECIDED by Jason 2026-10-02: keep, flag interview-based fields.** (First decided as v8's pick earlier the same day; Jason kept the rule and the 0.7 ceiling, and added the flag.) **Flag:** every field with basis `recorded_interview` starts its `how_known` with "(interview)", and the validator enforces this. A field whose main evidence is an interview under another basis (for example a paraphrase-only interview, held at 0.5) carries the same flag. The flag also shows wherever scores are listed: the record's Summary and score lines, the person chart's point labels ("A 0.5 interview") and legend (`scripts/make_figures.py`), and the primary-system table in `reports/coverage.md` ("(interview)" after the code). Applied in CODING_GUIDE §7, `scripts/lib/records.py` (`is_interview`, validator check), `make_figures.py`, `coverage_report.py`, the README chart caption and RUNBOOK. After the batch 3 lens audit no field uses basis `recorded_interview`; Chandrasekhar's interview-based fields (scholarly_reconstruction, 0.5) carry the flag.

The rule as first decided (v8's pick): a recorded or transcribed interview in the person's own words counts as their own words, with a 0.7 ceiling. A remark made in passing during an interview gets no extra cap beyond that, as long as it is in the first person. If only a paraphrase can be published (for example because of an AIP no-quotation notice), the interview cannot score an axis on its own; it may support an axis already scored from other evidence. Applied as: new basis `recorded_interview` (ceiling 0.7) and new statement kind `recorded interview` in `person.schema.json`, which goes to schema 1.2 (every person file and the template bumped; `system.schema.json` unchanged, since system records have no basis field); the validator ceiling table (`scripts/lib/records.py`); CODING_GUIDE §3 and §7; METHOD §4.2; RUNBOOK; DATA_DICTIONARY regenerated. Other people's words in an interview (a widow, a colleague) stay reported speech.

Rechecked under the rule (superseded for Chandrasekhar by the batch 3 lens audit, below):
- Chandrasekhar (record version 2): primary_system ATHE 0.5 → 0.7 (basis scholarly_reconstruction → recorded_interview); A_locus 4 at 0.5 → 0.7; self-described relation 0.5 → 0.7; B_cause 4 stays 0.5 (it rests on Parker; the interview remark speaks to it only indirectly); mid_basin BELOW_THRESHOLD → false at 0.5 (A ≥ 3 at 0.7; certainty capped by B under CODING_GUIDE §3). His two quotes are verbatim, so the paraphrase limit does not apply.
- Bohr (record version 2): no change. The AIP interview is Margrethe Bohr's reported speech and is paraphrased; it supports C_ledger, which rests on Heilbron, and scores nothing on its own.
- Lens audit, batch 3 (2026-10-02, #19, #20, #25): Chandrasekhar's S5 carries AIP's no-quotation notice, so under this rule's last sentence it can only be paraphrased and cannot score on its own. Record version 3 reverts primary_system ATHE, A_locus 4 and the self-described relation to 0.5 (basis scholarly_reconstruction), removes the two verbatim quotations, and sets mid_basin false (0.5) → BELOW_THRESHOLD. A strict reading (paraphrase-only cannot score at all) would make ATHE and A BELOW_THRESHOLD; 0.5 keeps the pre-P8 value and is v8's pick.

The question as raised (batch 3 report, 2026-10-02): the three basis types (written profession, consistent private letters, scholarly reconstruction) had no place for a subject's own tape-recorded speech. Chandrasekhar's "he knew I was an atheist" (AIP, 1987) had been coded scholarly_reconstruction at 0.5 by analogy with the single-letter rule, and AIP no-quotation notices meant some interviews could only be paraphrased.

### P9. Batch 3 record-level calls
**DECIDED (v8's pick, 2026-10-02):**
1. **Heisenberg:** keep the CODING_GUIDE §7 cap of 0.7 on fields read from the Internet Archive copy of the JSTOR PDF of "Scientific Truth and Religious Truth" (CrossCurrents, 1975). The copy's provenance cannot be confirmed from the copy itself. Reading the article directly on JSTOR would lift the cap. Record notes updated (record version 3); no score changed.
2. **Pasteur's era:** apply P2 literally to the recorded first lasting contribution (1848), so `1750 to 1849`, and note that he is on the boundary. Membership in the 1600–1950 pool is not affected. Value unchanged; how_known rewritten.
3. **Pasteur's death place:** Marnes-la-Coquette (the Villeneuve-l'Étang estate), with Saint-Cloud (Britannica) as the alternative; both cited. (Batch 3 lens audit: the uncited "the form most sources give" was dropped. The Île-de-France heritage inventory, dossier IA00051396, records that part of the estate's park was incorporated into the national domain of Saint-Cloud in 1895, the likely reason for Britannica's form; EPHE lists the ENS portrait among its sources, so it is not independent of it.) New source: the EPHE prosopographical notice (Dupressoir), "Villeneuve-l'Etang (act. Marnes-la-Coquette)". Certainty 0.7 → 0.5, because reliable sources name different communes (CODING_GUIDE §3, other facts).
4. **Caroline Herschel:** left as coded (CHRIST at 0.5 from brief devotional phrases in three letters); the lens audit will test it.

### P10. Which axes cap mid_basin certainty
**DECIDED by Jason 2026-10-02 (first proposed as v8's pick):** the CODING_GUIDE §3 cap on `mid_basin` certainty counts only the axes the branch actually uses. `false` via A_locus ≥ 3 uses A_locus only, so its certainty is at most A_locus's. `false` via A_locus ≤ 1 with B_cause ≤ 1 uses both, and so does `true`: at most the lower of the two. `TODO`, `UNKNOWN` and `BELOW_THRESHOLD` carry no certainty and follow their own inputs (§6). Applied in CODING_GUIDE §3 and §6, and in the mid_basin notes of Einstein, Schrödinger and Pauling (no value change). The validator does not check this cap, so no code changed.

No current value changes. Einstein, Schrödinger and Pauling (false via A 4) are at 0.7, which is both A's certainty and the lower of the two; every `true` is at the lower of A and B (0.7). The only case it would have changed, Chandrasekhar (false at 0.5, capped by B), is now BELOW_THRESHOLD after the same audit.

The question as raised (lens audit, batch 3, #25, 2026-10-02): §3 said "mid_basin certainty is at most the lower of the A_locus and B_cause certainties", but the false branch for A ≥ 3 does not use B at all. Chandrasekhar's false at 0.5 was therefore held down by an axis the test never read. Both runs agreed the value followed from the rule as written; one run noted the rule itself was the problem.

### P11. Text Creation Partnership transcriptions under §7
**DECIDED (v8's pick, 2026-10-02), from the batch 4 lens audit:** Text Creation Partnership transcriptions (EEBO-TCP, ECCO-TCP, Evans-TCP) count as authoritative copies under CODING_GUIDE §7, so the 0.7 cap on unofficial web copies does not apply to fields read in them. They are scholarly keyed transcriptions of a named printed edition, made by a library partnership (Michigan, Oxford and others) and tied to the page images of that edition, with printed page numbers recorded. Cite the TCP id and the original edition (printer, place and year), and quote with the TCP's spelling; gaps the TCP marks are not quoted. Applied in CODING_GUIDE §7 and the Boyle record (record version 2: the coder notes and the self-described relation cite this decision; no value changes, because Boyle's fields were already treated this way).

The question as raised: the batch 4 coding run (CHANGELOG, batch 4, open decision 3) treated the TCP texts of Boyle's Free Enquiry (A28982) and Christian Virtuoso (A28945) as authoritative and asked whether that was right. Lens batch 4 run 2 noted the open question at #33 and treated TCP as adequate; run 1 checked every Boyle quotation against the TCP XML and found them verbatim (one dropped comma, #22).

### P12. A contribution dated as a range
**DECIDED (v8's pick, 2026-10-02), from the batch 4 lens audit:** when a listed contribution spans a date range, `first_lasting_contribution_year` uses the range's start year. A start that the sources do not date (a decade such as "1920s", or a cumulative "by 1921") is not guessed: the item's `year` is written as the sources give it, the item sets the first-lasting year only once a source dates its start, and the how_known says that the true year might be earlier. Age and era are recomputed from the result. Applied in CODING_GUIDE §8, the schema description of the field (DATA_DICTIONARY regenerated) and the person template.

The question as raised (lens batch 4 run 1, note on #161): Hodgkin's record used the completion year of a range (penicillin, 1942–1945 → 1945), while Hubble's used the start year (1923–1924 → 1923); §8 did not say which.

Rechecked in all 31 person records (with P13):

| Record | before | after | why |
|---|---|---|---|
| Hodgkin | 1945, age 35 | 1942, age 32 | penicillin structure, research begun 1942 (Nobel biography, paragraph 7) |
| Boyle | 1660, age 33 | 1659, age 32 | air pump completed and used in 1659 (Britannica) |
| Galileo | 1610, age 46 | 1609, age 45 | telescopic discoveries, 1609–1610 |
| Hubble | 1923 | unchanged | already the start of 1923–1924; galaxy classification ("1920s") has no dated start in the source read |
| Leavitt | 1912 | unchanged | the variable-star item's year "1900s–1921" was the coder's guess; the sources give only her total by her death, so it is now "by 1921" and does not set the year (flagged) |
| Chandrasekhar, Dirac, Lavoisier, Ibn Sina and others | | unchanged | already the start year, or undated items that cannot be earlier on the sources read |

### P13. Which contributions can set the first-lasting year
**DECIDED (v8's pick, 2026-10-02), from the batch 4 lens audit:** `first_lasting_contribution_year` is the earliest year among the contributions listed in `contribution.lasting_original_contributions` (CODING_GUIDE §8, restated). Early work that is not listed (a doctoral thesis, early papers) can set it only if it is added to the list with a source and is itself a lasting contribution under §8 (still used or built on, with `lasting` saying what rests on it). A listed item sets the year whether or not the coder sees it as the main work; if it is not lasting, remove it from the list instead. Applied in CODING_GUIDE §8.

The question as raised (lens batch 4 run 1, #63, #89, #148): Feynman's 1939 and Pauling's 1925 matched no listed item, and Libby's 1947 was not the earliest listed item (the gaseous-diffusion barrier, 1941–1945).

Rechecked in all 31 person records (with P12):

| Record | before | after | why |
|---|---|---|---|
| Feynman | 1939, age 21 | 1939, age 21 | the MIT thesis is now listed: Britannica calls it "an original and enduring approach to calculating forces in molecules" |
| Pauling | 1925, age 24 (0.5) | 1931, age 30 (0.7) | no source read calls the PhD crystal-structure papers lasting, so they are not listed; the earliest listed item, the chemical bond, starts with his first "Nature of the Chemical Bond" paper (JACS, April 1931; new source) |
| Libby | 1947, age 38 | 1941, age 32 | the earliest listed item is the gaseous-diffusion barrier, Manhattan Project 1941–45 (Britannica), lasting per his widow's memorial |
| Caroline Herschel | 1786, age 36 | 1783, age 33 | the listed three nebulae of 1783 (Britannica) |
| Planck | 1900, age 42 | 1879, age 21 | the listed work on entropy and the second law (1879–1897), beginning with his 1879 doctorate; if that item is judged not lasting it should be removed, and the year returns to 1900 |
| The other 26 | | unchanged by P13 | already the earliest listed year (Hodgkin, Boyle and Galileo changed under P12, above) |

No era bucket changes: every new year is in the same bucket as before.

### P14. Coding a person whose best-fit system is a stub
**DECIDED (v8's pick, 2026-10-02, from the stage 3 lens audit; ruling 1):** there is no rule that a stub system file blocks a code. Code the person at the certainty the evidence supports (§4 and §3, as the Feynman, Pauling and Chandrasekhar records already do), flag that the system file is a stub, and put the system on the S7 sourcing backlog (`systems/README.md`). A record that withheld a code only because the file is a stub ("batch rule", "not coded because X is a stub") should be recoded. Applied in CODING_GUIDE §5 and the S7 backlog. None of the 31 batch 1–4 records withheld a code for this reason alone. The stage 3 records that did (Darwin AGNOS, Kant KANT, Hume) are for their own coders.

### P15. How many sources a fact needs
**DECIDED (v8's pick, 2026-10-02, from the stage 3 lens audit; ruling 2):** the §3 table rules. One reliable source gives at most 0.7. 1.0 needs two independent reliable sources, or a primary document (a birth, baptism or death record, or the person's own text). A primary document read as printed in a secondary work counts as primary; the how_known says "primary document printed in S#". When sources disagree on name order or name form, the field gets 0.7. Derived fields (era_bucket, age_at_first_lasting_contribution, region_of_birth) take the lowest certainty of their inputs. The one exception is an era bucket where every candidate year falls in the same bucket. Removed: the CODING_GUIDE §3 sentence "A signed encyclopedia can support 1.0 for a birth date that nobody disputes", and RUNBOOK §4.4's "sources agree, primary or well-established → 1.0". The validator now warns on a non-worldview 1.0 that rests on one non-primary source.

Applied to the 31 batch 1–4 records: 377 claims went from 1.0 to 0.7 for resting on one source, and 18 derived fields went from 1.0 to 0.7. Chandrasekhar's full_name went to 0.7 for a name-form disagreement (Nobel: "Subramanyan"). Details are in `reports/stage3_rulings_changes.csv`. Kept at 1.0: Lavoisier's baptism, religious heritage and nominal affiliation, which come from the parish record printed by Grimaux.

### P16. B_cause for mathematicians
**DECIDED (v8's pick, 2026-10-02, from the stage 3 lens audit; ruling 3):** B_cause needs a statement about nature or the physical world. Pure-mathematics Platonism, or a view on mathematical truth alone, gives `BELOW_THRESHOLD` (evidence that bears on the axis only indirectly, P19). A mathematician's physics-facing work is scored only with an explicit remark of theirs on nature. P6's wording ("the person's account of nature; for a scientist, their working science") is made consistent in CODING_GUIDE §6, METHOD §1.1 and the mid_basin schema description. Among the 31, only Gödel's record needed a change: his B 3 already rests on statements about the world, and its rationale now says that logic and set theory do not score B.

### P17. Completeness of the contribution list
**DECIDED (v8's pick, 2026-10-02, from the stage 3 lens audit; ruling 4):** P12 and P13 stand. The list of lasting contributions need not be complete, but it must include the earliest lasting contribution that the sources read name. For example, Darwin's Journal (1839) or Coral Reefs (1842) belongs on the list if the sources call it lasting. Applied in CODING_GUIDE §8. Among the 31, Kepler's Mysterium cosmographicum (1596) is a listed major work that is not on the lasting list. Whether S1 and S2 call it lasting is open, so Kepler's first-lasting year stays at 0.7 (P23).

### P18. Kinds of quoted text
**DECIDED (v8's pick, 2026-10-02, from the stage 3 lens audit; ruling 5):**
- New statement kinds `autobiography`, `unpublished manuscript` and `document in own hand` (schema 1.3). All count as the person's own words.
- A contemporary's summary of what the person said (Sartorius on Gauss) is `reported speech`. Under §1 it cannot score an axis on its own.
- The kind does not change the basis table. An unpublished or private document takes the private ceiling: consistent_private_letters, 0.7, and more than one document is needed. An autobiography the person published counts as written_profession.

Applied in the schema (with a validator version check), DATA_DICTIONARY and CODING_GUIDE §7. Relabelled:
- Newton statements 17–21 (a draft rebuttal and Keynes MSS 3, 7, 8) → unpublished manuscript;
- Lavoisier #2 (the 1791 Réflexions) → unpublished manuscript;
- Maxwell #6 (the Eranus essay) → unpublished manuscript, and #10 (the prayer fragment) → document in own hand;
- Gödel #0 (the Grandjean questionnaire) → document in own hand, and #7 (the c. 1960 list) → unpublished manuscript.

Faraday's two `other` quotes stay `other`, since their origin is not known. No basis or score changed.

### P19. UNKNOWN or BELOW_THRESHOLD
**DECIDED (v8's pick, 2026-10-02, from the stage 3 lens audit; ruling 6):**
- `UNKNOWN`: the sources read were searched and say nothing on the point. Items that were checked and found off-point count as nothing.
- `BELOW_THRESHOLD`: some evidence bears on the point but is too weak or indirect. Examples are reported speech, a single letter, a paraphrase, an implication, an ambiguous text, or working science that covers only part of the axis.

Precedence:
1. `mid_basin` is `UNKNOWN` if any needed axis is `UNKNOWN`. Otherwise it is `BELOW_THRESHOLD` when an axis is `BELOW_THRESHOLD` or only at 0.5.
2. A scientist's working science bears on E's first question (the same laws everywhere), so E without a statement stays `BELOW_THRESHOLD`. It does not bear on D (revelation against observation), so D without a statement is `UNKNOWN`.

Applied in CODING_GUIDE §4 and §6. Records changed, with each body summary updated to match:

| Record | → UNKNOWN | stays BELOW_THRESHOLD (why) |
|---|---|---|
| Clausius | primary_system, A, C, D, mid_basin | E (working science) |
| Curie | C, D | A, E |
| Dirac | C, D | A (Heisenberg's reported Solvay remarks, Pauli's quip) |
| Fermi | primary_system, A, C, D, mid_basin | E |
| Heisenberg | C | E |
| Hodgkin | C, D | A (Perutz's remark), E |
| Hubble | C | A (P20), E |
| Kepler | C | E |
| Leavitt | C, D | A (Bailey's sketch), E |
| Libby | primary_system, A, C, D, mid_basin | E |
| Meitner | C | A, D, E |
| Mendeleev | C | A, D (the ambiguous triad), E |
| Oppenheimer | A, C, D, mid_basin | primary_system (Ethical Culture schooling), E |
| Pasteur | C | A, E |
| Planck | C | — |
| Chandrasekhar | D (the Gita remark was not read) | C, E |

Ibn Sina's changes_over_life went from UNKNOWN to BELOW_THRESHOLD, because the IEP notes a debate.

### P20. A_locus when belief changed
**DECIDED (v8's pick, 2026-10-02, from the stage 3 lens audit; ruling 7, with the parent's 9:37 PM PT correction):** `primary_system` and the LIO axes both describe the same period: the worldview during the major work, that is, the working years (CODING_GUIDE §5, Changes over life). Score A_locus for that period, and record the change of belief in notes and `worldview.changes_over_life`, where later shifts go. A retrospective self-report about an earlier period is capped at 0.7. An agnostic with no stated locus view gets A `BELOW_THRESHOLD`. An explicit denial of a personal, intervening God is scored. Applied in CODING_GUIDE §6. Feynman's A stays BELOW_THRESHOLD: its how_known now says that "seems to be inadequate" (p. 22) is a hedged rejection, not an explicit denial. Hubble's A carries a note. Darwin's A = 2 is for his record's coder to check.

### P21. Institution, school and edition kinds
**DECIDED (v8's pick, 2026-10-02, from the stage 3 lens audit; ruling 8):**
- New institution kind `research institute` (IAS, the Kaiser Wilhelm and Max Planck institutes, Dublin IAS and similar).
- Schooling `stage` is now the level, with `elementary school` added. Who ran the school goes in a new optional `run_by` field (religious body, state or municipal, private, charity, family, other). The old `religious school` and `dame or charity school` mixed the two and are valid only in schema 1.2 files.
- `primary facsimile` means page images of the document itself (a manuscript, a letter, or a printing of the work as issued), with no editor in between.
- `scholarly edition` means a text an editor prepared (collected works such as Riemann's Werke, edited letters, a Life-and-letters, a posthumous collection), even when read as a library scan.
- `primary transcription` means a keyed transcription of the original (TCP, Newton Project, Darwin Online).

Applied in the schema (1.3), DATA_DICTIONARY and CODING_GUIDE §7–8. Relabelled:
- research institute: Einstein, Gödel and Oppenheimer (IAS); Heisenberg (KWI and MPI for Physics); Meitner (KWI for Chemistry, Nobel Institute); Schrödinger (Dublin IAS); Bohr (Institute for Theoretical Physics); Curie (Radium Institute); Pasteur (Institut Pasteur); Faraday (Royal Institution); Hubble (Mount Wilson Observatory).
- schooling: Aquinas, Clausius, Dirac, Faraday, Fermi, Gödel, Heisenberg, Ibn Sina and Pasteur → elementary school, and Galileo and Kepler → grammar or secondary school, each with run_by where the source says who ran the school.
- verified_against: Maxwell statements 0, 1 and 6–10 (printed in Campbell and Garnett 1882) and Hubble's three statements (the posthumous 1954 collection) → scholarly edition.

### P22. Stage 3-a stub cases (Hume, Kant, Descartes, Leibniz)
**DECIDED (v8's pick, 2026-10-02, from the second stage 3 lens audit; ruling 9):**
- P14 covers these cases.
- SCEPT, KANT, RATN and EMPIR go on the S7 backlog, together with every stub a stage 3 record leads with (ATHE, AGNOS, PANPSY, DETERM).
- "Argues to God from the world" in the CLASS_THEISM use_when means an a posteriori argument (cosmological or design). Ontological and idea-based arguments do not count. Code to what the system file definitions say.
- RATN was a stub with use_when TODO, so the CLASS_THEISM/RATN line was ambiguous. The RATN stub now carries one line, marked as v8's pick and kept in `scripts/make_system_stubs.py` so a regeneration keeps it:

> use RATN when the person's own writing makes reason working from innate ideas or first principles the main route to God and the world, and argues to God from the idea of God or from reason alone (ontological or idea-based arguments); a person whose main argument for God runs from the world, a posteriori (first cause, contingency, design), to the simple, immutable God of the Aristotelian-Thomistic-Falsafa line is CLASS_THEISM.

Applied in CODING_GUIDE §5, `systems/RATN.md` (record version 3) and `systems/README.md`. None of the 31 batch 1–4 records changed.

### P23. No coder-chosen first lasting year
**DECIDED (v8's pick, 2026-10-02, from the second stage 3 lens audit; ruling 10):** P13 is the rule. No coder-chosen "defining work" is allowed. The year is that of the earliest listed item that is itself a lasting contribution. The list is not pruned to move the year. An item may be removed only if it is not lasting, and the reason is stated. Applied in CODING_GUIDE §8, which now says exactly this.

"Coder's choice" wording was removed from the 31 records:
- Lavoisier: 1772 is the source-dated start of the earliest listed lasting item. It stays at 0.5 because the sources read leave open whether that item starts in 1772 or with the 1775 memoir, which is named as the alternative.
- Kepler: 1604 (the listed optics) stands. The 1609 "if the planetary laws are taken" alternative is removed. It stays at 0.7 pending the Mysterium check (P17).
- Bohr: major_work_period's "end date is the coder's choice" now cites the sources' dates.

### P24. What certainty 0.5 means
**DECIDED (v8's pick, 2026-10-02, from the second stage 3 lens audit; ruling 11):** existing practice uses 0.5 for inference from a person's work or conduct with no direct statement (for example B 4 at 0.5 from working science). §3 now says that 0.5 means contested, or inferred from the person's work or conduct with no direct statement. The basis is recorded as an inference: a new basis `inference_from_work` with a 0.5 ceiling (schema 1.3). For other facts, the how_known says it is an inference and from what. No record is recoded to UNKNOWN for this. The B_cause basis went from scholarly_reconstruction to inference_from_work for Clausius, Dirac, Fermi, Hodgkin, Leavitt, Libby, Meitner and Oppenheimer ("coder's reading of the working science"). Scores and certainties are unchanged.

### P25. Source conflicts
**DECIDED (v8's pick, 2026-10-02, from the second stage 3 lens audit; ruling 12):** when reliable sources disagree, the value gets 0.5 and the alternative is named in `alternatives`, as the Pasteur and Hodgkin records already do. When a 1.0 value rests on two sources but contains a detail backed by only one, the detail goes in its own note at 0.7, or the whole field is capped at 0.7. Applied in CODING_GUIDE §3. In the 31 records this came up where Top Questions cites were removed (P26). Aquinas's "official philosophy of the Church in 1917" detail was dropped, and Capreolus moved to the how_known.

### P26. Sources and locators
**DECIDED (v8's pick, 2026-10-02, from the second stage 3 lens audit; ruling 13), all in CODING_GUIDE §7:**
- **Spinoza's Ethics.** The project standard is the Cambridge edition edited by Matthew J. Kisner (Cambridge Texts in the History of Philosophy). A field that quotes another translation stays capped at 0.7 until it has been checked against Kisner. Its how_known or note says "Kisner check pending".
- **TTP locators** give the chapter and the standard (Bruder) section numbers (preferred). Gutenberg sentence numbers may be used only with a "Gutenberg" label and a TODO to map them to a printed edition (handoff line below).
- **Britannica's AI-generated "Top Questions" boxes** cannot be cited.
- **A quote reached through SEP or any other secondary source** must be checked against the primary text before it is cited as the person's words. Until then it stays `secondary quotation`, with a note saying the primary check is pending, and it cannot support 1.0 (§7).

Applied to the 31 records. Top Questions cites were removed from Aquinas, Einstein, Ibn Sina, Lavoisier and Pasteur, and values left without support were lowered or reworded. For Einstein, the 1926 Born letter rested only on the box: first_evidence_of_lio_type_views is now the 1929 cable (S4), and the Max Born collaborator entry was removed. Spinoza (Kisner, TTP) is a stage 3 record and is for its own coder.

### P27. DEISM and three anchor sentences
**DECIDED (v8's pick, 2026-10-02, from the second stage 3 lens audit; ruling 14):**
- DEISM requires rejecting revelation as a source of truth. Someone who does not reject it (who accepts it, or declines to contest it) is not DEISM. Applied in CODING_GUIDE §5 and `systems/DEISM.md` do_not_use_when (record version 6). Planck is the only DEISM code among the 31. His rationale now records the test: it is met for doctrine and miracle, and his "Weisung" from a direct link with God concerns action, not truth claims. The code stays at 0.5.
- Anchor sentences, each v8's pick, added to CODING_GUIDE §6 and §8. The existing definitions are quoted there first.
  - **LIO-type view:** a dated statement of the person's own that is scored, or used as evidence for a score, at 3 or 4 on any LIO axis.
  - **D 2:** two domains, each with its own authority. Observation and reason decide questions of fact about nature. Revelation, faith or religious tradition has the final say in another domain (doctrine, the divine, or the ends of action and ethics). Neither may overrule the other. If religion's say shrinks to one stated dogma, that is D 3. v8 chose this over the lens audit's alternative ("two domains each with authority over truth claims") because it keeps the existing D 2 scores. Under the alternative, the ethics-domain D 2s (Einstein, Feynman, Heisenberg, Hubble, Planck) would become D 3.
  - **B 3:** a stated general lawfulness of nature, with one stated, limited exception (for example, accepted miracles as rare past events, or a creation act).
  - **B 2:** lawfulness with exceptions that are not limited (miracles or special providence as a live, recurring part of how events go), or lawfulness that covers only part of nature.

No score among the 31 changed under the anchors. Every D 2 there (Boyle, Einstein, Faraday, Feynman, Galileo, Heisenberg, Hubble, Maxwell, Newton, Pasteur, Planck) gives religion a domain of its own.

### P28. Published letters, finished manuscripts, notes
**DECIDED (v8's pick, 2026-10-02, from the second stage 3 lens audit; ruling 15):**
- A letter written for circulation (Leibniz to Clarke) is the new kind `published letter`, and it counts like a published work (written_profession).
- An unpublished finished treatise (the Monadology) is `unpublished manuscript`.
- The Pensées are `unpublished manuscript` (notes), not letters.

Applied in the schema (1.3), DATA_DICTIONARY and CODING_GUIDE §7. None of the 31 records has such a text. The Leibniz and Pascal stage 3 records are for their coders.

### Further stage 3-a handoff questions, covered by the rulings above (2026-10-02, v8's picks, no new numbers)
- **DEISM and revelation:** DEISM means "rejects revelation", so someone who simply doesn't reject it isn't DEISM (P27). This covers Kant (who declines to contest revelation) and Descartes (who accepts it).
- **Long s (ſ):** normalise it to "s" silently in quotations, and add one coder_notes line saying so. This is the one exception to §7's verbatim rule.
- **Kant's region:** regions use present-day borders (P3), so Königsberg is Kaliningrad, Russia (Eastern Europe), with the polity then in `place.polity_then`.
- **Secondary sources that mislabel a primary locator** (SEP gives "Pr II 62" for Principles II.42, and "EU 11.12" for E 10.12): cite the primary locator and note the error in the field's note or data_quality_flags (P26).
- **Gutenberg locators:** they may be used only with a "Gutenberg" label (for example "Gutenberg ch. 6 (40)") and a TODO in the note to map them to a printed edition. For the TTP, Bruder sections are preferred (P26).
- **Roster links:** cites of the roster that point to `blob/main` will be pinned to a commit SHA in a later sweep. No change now.
- **Era bucket:** era_bucket follows the first lasting year, as §8 and P2 say (Darwin's era is not keyed to 1859).


### P29. Stage 3-b follow-up rulings
**DECIDED (v8's pick, 2026-10-02), from lens's blind run on the v8.b rulings packet (6155174):**
- **secondary_system:** CODING_GUIDE §1 governs. A secondary system needs published work in two systems; otherwise it is UNKNOWN, and any evidence stays in the notes.
- **Hedged self-reports:** a self-report hedged in its own words ("as far as I can remember") stays at 0.5 and does not reach P20's 0.7 cap. The same evidence gets the same certainty on every field it supports (primary_system and A together).
- **Later disavowal:** when the person later disowns their own public wording (Darwin to Hooker, 1863: "truckled to public opinion"), that wording supports at most 0.5. The disavowal itself is cited.
- **Dating a contribution:** a contribution is dated by its first publication. A dated public reading counts as publication only if it is documented. Darwin's coral-reef theory: 1837, read to the Geological Society on 31 May 1837 with abstracts printed that year, and this is the listed item. Era unchanged. (Corrected in P30: this bullet first gave 1839, from the Journal, p. 557. P30 rule 1 now replaces the "first publication" rule.)
- **One period per record (P20):** the period runs from the first to the last listed lasting contribution. Every axis and primary_system use that span. ~~Statements from outside it count only as retrospective self-reports (0.7 cap, or 0.5 if hedged) or go in changes_over_life.~~ (Superseded by P31, 2026-10-02: evidence from any adult year counts unless a change of view is documented.)
- **Who is a scientist (P16, P19, P24):** anyone with a listed lasting contribution in natural or physical science, applied the same way to B and E. Working science can then support B and E at 0.5 as inference_from_work. A pure mathematician with no such contribution needs a statement about nature. Who counts is now set by P30 rule 11 (a listed lasting contribution that is a theory or result about physical or natural systems), which replaces the names first given here.
- **P15:** no exception lets a single source give 1.0.
- **Source independence:** a source that draws on another (MacTutor's Riemann biography on Dedekind's Lebenslauf) is not independent of it, so the pair gives 0.7.
- **Two sources naming different people** (Fekete and Fejér as tutors) are not a P25 conflict. Each name gets its own entry at 0.7.
- **Antinomy layouts:** a Thesis column is not the person's own view unless the text endorses it. It is discounted the same way on every axis.
- **Childhood religious schooling** is evidence for the family and heritage fields only. It is off-point for the person's own axes A–E.
- **Answers first given only inside records**, now recorded here: Riemann's A at 0.5 on the antinomy layout (consistent with the antinomy rule above); fields resting only on Dedekind's Lebenslauf at 0.7 (it is a friend's memoir, not a primary document); Noether's E UNKNOWN (no statement and no listed natural-science contribution; superseded by P30 rule 11, under which Noether is a scientist: her B follows P24 and her E follows P19, so E needs a statement).

### P30. Stage 3 rulings round 3
**DECIDED (v8's pick, 2026-10-02)**, from lens's runs on the v8.a rulings packet (34a73c4) and the v8.b P29 packet (e930597). Applied in CODING_GUIDE §3, §5–8, DATA_DICTIONARY §1 and METHOD. Rule 5 was applied by script to the 31 records outside stage 3 (27 age values in 16 records; every change is in `reports/p30_age_changes.csv`). The 12 stage 3 records are for their coders.

**Correction to P29.** Darwin's coral-reef theory dates to 1837. It was read to the Geological Society on 31 May 1837, and abstracts were printed in Proc. Geol. Soc. 2: 552–554 and in the Athenaeum (17 June 1837) (Coral Reefs, p. 4 footnote). First lasting year 1837, age 28, era 1750–1849 (unchanged). P29's "first publication" rule is replaced by rule 1 below.

Dating and periods:
- **1. Dating a contribution.** Use the year of the person's earliest documented public statement of the result. That can be in print (the full work, a printed abstract, or a printed notice that states the result, such as Gauss's 17-gon notice of 1 June 1796 in the Intelligenzblatt), a documented public lecture or reading, or a formal submission. So Gauss's year is 1796, if the 17-gon is a listed lasting contribution.
- **2. Classified work** kept out of print by secrecy (von Neumann's implosion work, Turing at Bletchley) is dated by its documented work years. This is the only exception. Other unpublished work is dated by rule 1.
- **3. Posthumous publication.** Date the item by its last documented act in life (a submission, a lecture, a dated manuscript). If there is none, use the death year. A period never ends after death (CODING_GUIDE §1, Unit of coding). Riemann's 1854 Habilitation lecture is dated 1854.
- **4. Period end with a bound or a range.** Use the latest year the sources allow: the end of a range (Noether, 1927–1933, gives 1933), or one year inside an exclusive bound ("before 1831" gives 1830). Note the bound.
- **5. Age convention.** Age = event year − birth year, with no month adjustment. This applies to every age field in every record. `scripts/recompute_ages.py` recomputes them.

Evidence:
- **6. A real dispute (P25 and CODING_GUIDE §8).** A dispute is real when reliable sources give different values for the same event and both can't be true. That gives 0.5, with the alternative named. If the values may refer to different events, it is not a dispute: record each as its own entry at its own certainty, as with the tutors in P29. Spinoza #5 and Pascal #67 are to be fixed under this test.
- **7. First LIO-type view (P27).** Before setting the year, the coder checks the person's earliest major works up to the first quote found. A quote found in a secondary source counts once its locator is checked against the primary. If the earlier works weren't read, the year's certainty is capped at 0.5, with the note "earlier works not read". This covers Kant (check 1755 and 1781) and Descartes (check SEP's 1629 quote).
- **8. Tense in retrospective narrative.** Present tense describes the time of writing, and past tense describes the past. A sentence is read the same way on every axis: if Darwin p. 87 is time-of-writing for B, it is for C too.
- **9. Same evidence, same certainty** (P29) applies only when the same passage bears on the same point. Each axis is still scored separately (CODING_GUIDE §6). Atheism alone doesn't settle A, so Turing's ATHE at 0.5 with A `BELOW_THRESHOLD` is consistent.
- **10. mid_basin with alternatives.** The cap uses the certainty that the tested condition holds. If the value and every named alternative meet the condition (B 3 and alternative B 4 both meet B ≥ 3), use the certainty of the evidence for the condition itself (for Darwin, his published lawfulness, never disowned), not the certainty of the exact value.
- **11. Who is a scientist** (replaces P29's names). A scientist is anyone with a listed lasting contribution that is a theory or result about physical or natural systems. Noether's theorem (symmetries and conservation laws in physics) qualifies, so Noether is a scientist. Her B follows P24 and her E follows P19, as von Neumann's and Gauss's do (wording corrected by the addendum below; it first said "her B and E follow P24").
- **12. Kisner cap (P26)** applies to quotations and locators from the Ethics, not to bibliographic facts confirmed in the Latin original. SEP plus the Latin Gutenberg title page can give 1.0 (Spinoza #17).
- **13. Published letter (P28, general).** A letter counts as published work if it was printed in the person's lifetime, or if it was written for circulation, as shown by the person's own statement or by copies circulated in their lifetime.
- **14. B 3's one exception (P27)** includes a free will not bound by natural law, whether it is placed in nature or outside it. Descartes' free mind and Kant's noumenal freedom both count, so Kant is B 3 as the value, not as an alternative.
- **15. Gutenberg TODO (P26).** Every field that cites a Gutenberg locator carries its own TODO, so a sweep can find each one.

Process:
- **16. Ruling questions.** A question goes to v8 only if the answer could change a record's `primary_system`, A, B or `mid_basin` value (not just a certainty) or the 8 passes. Coders decide everything else themselves: they take the more conservative option (the lower certainty, or UNKNOWN over a guess), log it in `coder_notes` as "coder's call", and list it in the handoff. Lens reports such items as notes, not ruling questions. Each batch gets one blind lens run on the changed claims, plus a second run only if the first finds a FAIL.

**P30 addendum (v8's picks, 2026-10-02 11:20 PM PT).** Applied in CODING_GUIDE §6 and §8, DATA_DICTIONARY §1, METHOD, the schema descriptions (description only) and `scripts/validate_people.py`. No record was changed; the 12 stage 3 records are for their coders.
- **a. E for scientists.** P19 governs E: E needs a statement, and without one it stays `BELOW_THRESHOLD`. Working science supports B only, at 0.5 under P24. Rule 11's wording is corrected to match. No E sweep.
- **b. The latest lasting work must be listed.** The contribution list must include the latest lasting work the sources name, as P17 requires for the earliest. A published letter (rule 13) can be such a work. So the period end can't leave out a major late public work just because it wasn't listed. The Leibniz–Clarke correspondence (1715–16) is the case that raised this.
- **c. No documented public statement in life.** An item with no public statement in life (rule 1) is dated by its documented composition date, and the note says so. The death cap (rule 3) still applies.
- **d. Ranges.** A range gives its start year for the period start (P12) and its end year for the period end (rule 4). Kant's period ends in 1788.
- **e. Posthumous items.** The period never runs past death. ~~A late private writing published after death counts only if its composition is dated within the period.~~ (Superseded by P31, 2026-10-02: as evidence, such a writing counts like any other adult evidence. The death cap stays.) So Pascal's period ends in 1662 at the latest, and Hume's in 1776 at the latest.
- **f. One span, two fields.** `timing.major_work_period` is the authoritative span. `worldview.working_years` must equal it, and "working years" in the docs means that span. `validate_people.py` now warns when the two differ: 38 of the 43 records warn (29 of the 31 outside stage 3, 9 of the 12 stage 3 records). This round fixes none of them. (Follow-up, 2026-10-02: the 29 outside stage 3 are aligned; spans checked and evidence dates audited in `reports/p30_span_alignment.csv`.)
- **g. Schema descriptions.** "published letter" now says printed in the person's lifetime or written for circulation (rule 13), and the mid_basin description includes the alternatives rule (rule 10). DATA_DICTIONARY was regenerated. No enum changed.

### P31. Continuity rule
**DECIDED (v8's pick, 2026-10-02, 11:50 PM PT)**, from the P30 span-alignment audit (7a52a3f, `reports/p30_span_alignment.csv`). That audit found that P29's out-of-span clause would set aside most worldview evidence, because most people state their worldview late in life. Applied in CODING_GUIDE §1 and §5, DATA_DICTIONARY §1 and METHOD. Re-check of the audit's 55 flagged values: 49 resolved at first, and Newton's 6 (plus his borderline B) after the Newton ruling below; every row is marked in the CSV. Sensitivity: [`reports/period_rule_sensitivity.md`](../reports/period_rule_sensitivity.md) lists the 55 values that would change under P29's original strict clause. The 12 stage 3 records are for their coders.
- **Span.** The span (`timing.major_work_period`, which `worldview.working_years` equals) dates the worldview being coded.
- **Evidence from outside the span.** Evidence from any year of the person's adult life counts for the span at its normal certainty, unless the record documents a change of view between the span and the evidence. A documented change means a sourced entry in `worldview.changes_over_life`.
- **After a documented change**, the evidence counts only as a retrospective self-report (0.7 cap, or 0.5 if hedged), or it goes in `changes_over_life`.
- **A change inside the span.** When a documented change of view falls inside the span, `primary_system` and the axes follow the phase that covers the most listed lasting contributions; a tie goes to the later phase. The other phase goes in `changes_over_life`, plus a one-line `coder_notes` delta saying what would change. Example: Kant is coded KANT from the critical works, with CLASS_THEISM noted as the earlier-phase alternative.
- **Which changes split the span** (Newton ruling, v8's pick, 2026-10-02). A change of view splits the span into phases only if it bears on a coded field: `primary_system` or A–E. A change in a doctrine that none of those fields depends on is logged in `changes_over_life` and does not split the span. Newton's antitrinitarianism (about 1672) leaves CHRIST and every axis unchanged, so his span is not split and his values stand. When phases are counted, the items are dated by the P30 #1 dating rules.
- **Childhood evidence** stays off-point for the person's own axes (P29, childhood religious schooling bullet).
- **Replaces** P29's clause "statements from outside the span count only as retrospective self-reports or go in changes_over_life" and P30 addendum e's restriction on posthumous private writings. The death cap on the span stays, and so do the other span rules: the dating rules (P30 #1–4, addendum c and d), the latest lasting work (addendum b) and the working_years equality (addendum f).

### P32. Work order after the first 12 stage 3 records
**DECIDED (v8's pick, 2026-10-08)**, while choosing stage 3 batch C. RUNBOOK gives the pools (first pool, then physical science 1600–1950 with F ≥ 3, then everyone else with F ≥ 3, then F = 2 and 1) but not the order inside a pool or when a pool counts as finished.
- **Order.** First any uncoded person left in an earlier pool (Chien-Shiung Wu was the last physical-science person with F ≥ 3 whose first lasting contribution falls in 1600–1950). Then everyone else with F ≥ 3, by F descending, then roster rank ascending.
- **Why.** The order is mechanical, so no coder picks who is coded next. That matters for the representation question: a chart of hand-picked people has no base rate.
- **Batch C** (2026-10-08): Wu, Lovelace, Smith, al-Farabi, al-Khwarizmi, Bell. Next in order: Archimedes, Aristotle, McClintock, Russell.

### P33. Inventors and the scientist test
**DECIDED (v8's pick, 2026-10-08)**, while coding Alexander Graham Bell. P30 makes a scientist anyone with a listed lasting contribution that is "a theory or result about physical or natural systems". It does not say whether a device counts.
- **Rule.** A device or invention is not a theory or result about physical or natural systems. An inventor counts as a scientist only if a listed lasting contribution is itself a theory or result. Otherwise B needs a statement of the person's own about nature (P16), as for any non-scientist.
- **Why.** Building a working device shows the builder relied on regularities, but it does not state a view of nature's order, and nearly everyone relies on regularities. Counting devices would let B be scored from almost any practical work.
- **Applied to:** Bell (telephone, photophone, graphophone): not a scientist; no statement about nature was found, so B is UNKNOWN. Lovelace (Notes on the Analytical Engine) is treated the same way. Effect: B for inventors is scored less often.

### P34. Denominators: unscorable people are left out
**DECIDED (Jason, 2026-10-08): people who can't be scored for an analysis are excluded from its denominator and reported separately as not scorable.**
- **What counts as not scorable.** For the person chart: A_locus or B_cause is not a 0–4 score (`TODO`, `UNKNOWN` or `BELOW_THRESHOLD`). For any other test or share: a field the test needs is not scored. Such a person is not inside the analysis at all, so they are not counted as outside the focus box, or as failing the test.
- **Focus count (superseded by P37: no focus box is drawn or counted now).** The focus box (A_locus ≥ 3 and B_cause ≥ 3) is counted only among people at certainty ≥ 0.7 on both axes, and the base is stated as those people. People plotted in the box at lower certainty are named as a separate number, not counted.
- **Reporting.** The not-scorable people are given as a plain count, with which axis is missing, so they are visible and not hidden.
- **Not an analysis.** Coding progress against the roster (e.g. people coded of core) and claim fill rates in reports/coverage.md are coverage figures, so they keep the full roster or claim count as the base.
- **Where it is applied.** `people_axis_points` and `people_chart_caption` (`focus_counts` was removed under P37) in `scripts/lib/records.py`, used by `scripts/make_figures.py` and `scripts/progress_status.py`.

### P35. B from working science only
**DECIDED (v8's pick, 2026-10-08)**, from ruling question R1 of the blind lens audit of stage 3 batch C (commit dd91009, run 1). R1 there is the audit's own label, not decision R1 above.
- **Rule.** B inferred only from a scientist's work, with no statement of their own on law and exception, is B 3 at 0.5 with 4 as the named alternative, never 4. This covers `inference_from_work` and a scholar's reconstruction of the working science (`scholarly_reconstruction`). It changes P24's example ("B 4 from a scientist's working science").
- **Why.** Working science cannot separate B 4 from B 3. Faraday, Maxwell and Newton did the same law-testing science and are B 3 from their own statements. A flat 4 would credit a person with "no exceptions" that they never stated.
- **Effect on mid_basin.** None: the test is B ≥ 3, and these values are at 0.5, under its 0.7 bar.
- **Applied to (B_cause 4 → 3 at 0.5, alternative 4):** Bohr, Chandrasekhar, Clausius, Dirac, Fermi, Hodgkin, Leavitt, Libby, Meitner, Oppenheimer, Pasteur and Wu. Meitner's 1953 phrase 'the natural order of things' says nothing on exceptions, so her B still rests on her work (coder's call). Curie, Hubble, Mendeleev and others scored from their own statements are unchanged.

### P36. A scholar's reconstruction of free will triggers B 3
**DECIDED (v8's pick, 2026-10-08)**, from ruling question R2 of the same audit.
- **Rule.** A scholar's reconstruction of the person's view of free will or contingency (a will not bound by natural law) triggers the B 3 anchor (P30 #14, CODING_GUIDE §6) the same way as the person's own statement does for Descartes and Kant, capped at 0.5 (the scholarly_reconstruction ceiling).
- **Why.** The B 3 anchor is about what the view contains. When the only evidence for the view is a scholar's account, that lowers the certainty, not the value.
- **Applied to:** al-Farabi, B_cause 4 → 3 at 0.5 with alternative 4 (Germann, SEP §3.1: 'While everything else executes its function by nature, human beings, equipped with reason and free will, must choose to do so'). No other record has a reconstructed free-will passage behind a B 4.

### P37. No focus region on the README or person chart
**DECIDED (Jason, 2026-10-08): the README and person chart mark no focus region; a favored region is a projected interpretation and premature until the roster is coded as a sample with era base rates.**
- **Applied.** The shaded top-right box, its label and the focus count are removed from `figures/people_cause_locus.png` (`scripts/make_figures.py`) and its caption (`people_chart_caption` in `scripts/lib/records.py`); the README's Focus paragraph is removed. The chart shows where coded people fall and nothing more.
- **Unchanged.** The method rules, including P4 (mid-basin test), stand.

### S1. CLTHEI display label
**Decided 2026-10-01 by Jason (approved as recommended):** CLTHEI `display_label` is "Interventionist personal theism", `label_status` `approved`. The code and `v7_1_label` are unchanged.

The original question and the recommendation are kept below for the record.
The v7.1 label is "Classical Theism (personal, interventionist Creator God)". It shares the words "Classical Theism" with CLASS_THEISM, which the v7.1 rules say it must not be confused with.
**Proposed display label:** "Interventionist personal theism". The code stays `CLTHEI` and `v7_1_label` is kept verbatim. Status in the file: `proposed — pending Jason's OK`.

**Recommendation (v8 agent, 2026-10-01):** **approve "Interventionist personal theism" as the display label.** Confidence: medium-high. The full original label is confirmed in V6: "Classical Theism (personal, interventionist Creator God)" (`V6_(history)/V6/beliefCoherence.json`, CLTHEI entry). The rubric scores there match the v7.1 data book for all 77 systems, so it is the same source table. The v7.1 rule itself separates the two codes ("CLASS_THEISM … is not CLTHEI (popular interventionist personal God)"), and the proposed label uses the rule's own words. The code and `v7_1_label` stay unchanged.

### S2. PANT display label
**Decided 2026-10-01 by Jason (approved as recommended):** PANT `display_label` is "Pantheism (Spinozistic/naturalistic 'God = Universe')", `label_status` `approved`, source `V6_(history)/V6/beliefCoherence.json` (v7 repo). `v7_1_label` is unchanged.

The original question and the recommendation are kept below for the record.
The v7.1 label is cut off mid-word in both the data book table and the Word file: "Pantheism (Spinozistic/naturalistic 'God = Univers…".
**Proposed display label:** "Pantheism (Spinozistic/naturalistic)", trimmed at the last whole phrase. If the full original label exists elsewhere, use it instead.

**Recommendation (v8 agent, 2026-10-01):** **use the full original label: "Pantheism (Spinozistic/naturalistic 'God = Universe')".** Confidence: high. It's in `V6_(history)/V6/beliefCoherence.json` (PANT entry, `belief_system`) and in the V6 paper's table (`V6: The Impact of Ideology on Intelligence….md`, line 390). This is the source of the v7.1 table. All 77 systems' L/P/E/V/X scores in the V6 JSON match the v7.1 data book exactly, and every truncated v7.1 label is a prefix of its V6 label. The truncation ("Univers…") happened in v7.1. The Word data book and the combined JSON are both truncated, and nothing in the v7 repo has the full text. The same V6 file also gives the full form of the other labels that v7.1 cut off (ATHE, CLASS_THEISM, PANENT, KEMET, ABORIG, MORMON, CLTHEI), if those are ever needed. If approved: set PANT's `display_label` to the full label and `label_status` to approved, and note the V6 source. Not changed here.

### S3. Expanding the rubric
**Decided 2026-10-01 by Jason (approved as recommended):** the v7.1 rubric scores are a frozen baseline. Revised scoring opens only after the first coding pool, with a cite per axis, two independent scorers on a sample with agreement reported, and Jason's approval. Revised scores sit beside v7.1's and never overwrite them. Recorded in METHOD §5.1 and the system schema.

The original question and the recommendation are kept below for the record.
The data book defines L, P, E, V and X (see DATA_DICTIONARY §4). `revised_rubric` exists in every file with status `not started`.
**Decide:** whether and when to open revised scoring, who scores, and whether revised scores need cites per axis (the schema allows it).

**Recommendation (v8 agent, 2026-10-01):** **keep the v7.1 scores frozen as the baseline, and don't open revised scoring until the first coding pool (P4) is done.** Confidence: medium. When it opens: (1) require a cite for each axis score (the schema already allows it), since the v7.1 scores are authorial and uncited; (2) have two scorers score a sample of systems independently and report agreement before anyone scores the rest; (3) Jason approves the final numbers. Revised scores sit beside the v7.1 scores and never overwrite them. That is the simplest way to keep v7.1 results reproducible.

### S4. New belief systems
**Decided 2026-10-01 by Jason (approved as recommended):** the 77 codes are closed for v8. Proposed new codes go in a plain list (code, why, example people) and are added in one batch with one schema bump; a split must list the people it would move. Recorded in METHOD §5.1 and the system schema.

The original question and the recommendation are kept below for the record.
Schema 1.0 allows only the 77 v7.1 codes. The validator rejects others. Adding a system (for example, splitting a popular form out of an existing code) needs a schema version bump and Jason's approval.

**Recommendation (v8 agent, 2026-10-01):** **keep the 77 codes closed for v8. Collect proposed new codes in a plain list (code, why, example people) and add them in one batch with a single schema bump.** Confidence: medium-high. A fixed code list is what makes v7.1 and v8 counts comparable, and one bump is cheaper than several. Splitting an existing code changes every count that used it, so each split should list the people it would move.

### S5. related_codes direction
**Decided 2026-10-01 by Jason (approved as recommended):** CLTHEI and CLASS_THEISM now relate to each other as "neighbor (easily confused)", set in `scripts/make_system_stubs.py`.

The original question and the recommendation are kept below for the record.
`relation` reads "<code> is <relation> this system". So CLTHEI lists CLASS_THEISM as its "scholastic form of", and CLASS_THEISM lists CLTHEI as its "popular form of". Treating the two as scholastic and popular forms of one tradition is a reading of the v7.1 rule "CLASS_THEISM ... is not CLTHEI (popular interventionist personal God)".
**Options:** confirm; change both to "neighbor (easily confused)".

**Recommendation (v8 agent, 2026-10-01):** **change both to "neighbor (easily confused)".** Confidence: medium. The v7.1 rule says only that the two codes are different and easy to confuse: "CLASS_THEISM (Aristotelian-Thomistic-Falsafa) is not CLTHEI (popular interventionist personal God) and not generic CHRIST/ISLAM/JUDA." It doesn't say they are the scholastic and popular forms of one tradition. That is a further historical claim, and arguable: CLASS_THEISM spans Christian, Muslim and Jewish thinkers, while CLTHEI is defined by intervention. "Neighbor" records what the rule says and nothing more. If approved: edit `related_codes` in `systems/CLTHEI.md` and `systems/CLASS_THEISM.md`.

### S6. PANT boundaries (raised by the PANT worked example)
**Decided 2026-10-01 by Jason (approved as recommended):** PANT needs the two-part test (identity with Nature as a whole, plus a mark beyond feeling); Advaita Vedanta and Kabbalah default to the host tradition, PANENT if a God beyond the world is kept; ancient and avowed Stoics are STOIC. Added to the coding guidance of PANT, ATHE, STOIC and PANENT, and to CODING_GUIDE §5.

The original question and the recommendation are kept below for the record.
- Modern scientific or naturalistic pantheism: PANT (the circle) or ATHE with reverent language? v7.1 says "not atheism-plus-poetry", but this needs a test that can be applied.
- Advaita Vedanta and some Kabbalah: v7.1's PANENT label names "some Kabbalah/Advaita forms", while the Stanford Encyclopedia of Philosophy says only that they are "marked by pantheistic ideas and feelings" (wording corrected 2026-10-02, lens audit #56; the earlier text said SEP lists them among pantheist strands).
- Stoic pantheists: STOIC or PANT?

**Recommendation (v8 agent, 2026-10-01):** Confidence: medium on all three. The relevant rules are the v7.1 coding rule ("Use PANT only for the circle: Deus sive Natura, entity-in-Nature and Nature-in-entity. Not atheism-plus-poetry. Not every nature-mystic.") and the founders rule ("Code the system they founded"). The source is SEP, "Pantheism" (William Mander, rev. 2023, https://plato.stanford.edu/entries/pantheism/).

- **Scientific or naturalistic pantheism.** SEP describes it as worldviews that "make no ontological commitments beyond those sanctioned by empirical science". Its §8 explains why "atheism-plus-poetry" is a fair worry: if the only mark of divinity is feeling, then "all that distinguishes a pantheist from an atheist is feeling". SEP §§9–13 then go through the other marks that might make the whole divine: its place as the universe at large (§9), infinity, eternity or necessity (§10), ineffability (§11), being personal (§12) and value (§13). The unity of the cosmos is treated in §5. Proposed test: code PANT only if the person's own writing (1) identifies God or the divine with Nature as a whole, as a claim about what exists, not as a figure of speech, **and** (2) gives the whole at least one mark beyond feeling, such as unity as one substance or order (§5), necessity or eternity (§10), something mind-like (§12) or value (§13). Reverent language with neither of these is ATHE (positive naturalism), or SECHUM if the person's public identity is the humanist movement. Einstein-style "Spinoza's God" statements pass (1); "nature is awe-inspiring" alone does not.
- **Advaita Vedanta and some Kabbalah.** SEP says only that these traditions are "marked by pantheistic ideas and feelings" (§1), not that they are pantheist, while v7.1's PANENT label names "some Kabbalah/Advaita forms". SEP also says the lines between immanence, pantheism and panentheism "are vague and porous". Proposed rule: by default, code the host tradition (HINDU, JUDA) as primary, under "Primary = dominant working metaphysics". Use PANENT when the person's writing keeps a divine reality that includes but exceeds the world, which is how v7.1 labels these forms. Use PANT only if they pass the two-part test above. Don't code PANT just because they belong to the tradition.
- **Stoic pantheists.** SEP calls Stoic physicalism "an ancient form of pantheism". It also reports the argument (Baltzly 2003) that the Stoic God was personal and providential, someone "to whom we might approach in prayer". That clashes with the PANT circle on petition and the B axis. Proposed rule: code STOIC for ancient Stoics and for anyone whose avowed school is Stoicism. This follows the founders and "dominant working metaphysics" rules, and STOIC is its own code with its own score. Reserve PANT for later thinkers who take the Stoic or Spinozist identity without the providential, prayer-hearing deity.

### S7. System-sourcing backlog and French spiritualism
**DECIDED (v8's pick, 2026-10-02):** no system file for French spiritualism now (the code list stays closed under S4). It is recorded in Pasteur's record as a named candidate in the primary_system note, and listed under "Systems to consider" in `systems/README.md`, a new short section with the code idea, why and example people, as S4 asks. The ATHE, AGNOS and IDEAL stubs are the next system-sourcing job, listed first under "Sourcing backlog" in `systems/README.md`; they were not sourced in this change.

The question as raised (batch 3 report, 2026-10-02): Pasteur's 1882 speech defends "la doctrine spiritualiste" (Cousin's school), which no system file covers; and ATHE, AGNOS and IDEAL, still stubs, were the candidate codes for Bohr, Chandrasekhar, Dirac and Pasteur.
