# Open decisions

Choices that need Jason's sign-off. Nothing here has been decided. Where the repo needs *some* value to work, it uses the stated proposal and marks it PROPOSED, and nothing downstream treats it as settled. When a decision is made:

1. record it here under "Decided", with the date;
2. update the files it touches;
3. note it in `CHANGELOG.md`.

## Summary of recommendations (v8 agent, 2026-10-01)

These are recommendations only. Every item below is still open, and nothing has been moved to "Decided". No data that depends on an open item has been changed. Evidence files are in `reports/` (`r7_bucket_spotcheck.csv`, `r7_field_string_review.csv`).

| ID | Recommendation | Confidence | Needs Jason |
|---|---|---|---|
| R1 | O'Keeffe: core | high | yes |
| R2 | Wrights: exclude both, as v7.1 did | medium-high | yes |
| R3 | "Brian Maynard Smith": display fix to John Maynard Smith | high | yes |
| R4 | Confirm all four merges | high | yes |
| R5 | Confirm the three pairs are different people | high | yes |
| R6 | Approve the F ≥ 3 plan; all 9 core (Vint Cerf is the judgment call) | high (count), medium (Cerf) | yes |
| R7 | Accept the keyword rules plus six small rule fixes; v7 mapping not on disk | medium-high | yes |
| R8 | Approve the id freeze rule as written | high | yes |
| P1 | Approve the 0–4 scale | medium-high | yes |
| P2 | Approve; key on first lasting contribution, keep birth year too | medium-high | yes |
| P3 | Approve, with a country-to-region table (settle MENA, Iran, Afghanistan) | medium | yes |
| P4 | Axis test: A_locus ≤ 1 and B_cause (in the work) ≥ 3, both at certainty ≥ 0.7 | medium | yes |
| P5 | Approve: only a named human sets "reviewed" | high | yes |
| S1 | Approve "Interventionist personal theism" | medium-high | yes |
| S2 | Use the full original label, found in V6: "Pantheism (Spinozistic/naturalistic 'God = Universe')" | high | yes |
| S3 | Freeze v7.1 scores as baseline; open revised scoring after the first pool, with cites per axis and two scorers | medium | yes |
| S4 | Keep the 77 codes closed for v8; batch any new codes into one schema bump | medium-high | yes |
| S5 | Change both to "neighbor (easily confused)" | medium | yes |
| S6 | Two-part PANT test; host tradition or PANENT for Advaita/Kabbalah; STOIC for Stoics | medium | yes |

**Ready to approve in one go** (factual, backed by sources or v7.1 records): R1, R2, R3, R4, R5, S2. Each needs only a small input change (`curated_aliases.csv`, a status input for R1, or `display_label` for S2) and a rebuild, as listed under each item.

The rest are judgment calls. R8 and P5 are low-risk policy approvals. R6, R7, P1–P4, S1 and S3–S6 need Jason's view.

## Roster

### R1. Georgia O'Keeffe's status
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
The automatic scan flagged these pairs. They are left as different people, which looks right, but a human should confirm:
- Ken Thompson / E.P. Thompson
- Edward Said / Edward Sapir
- Marc Bloch / Maurice Bloch

**Recommendation (v8 agent, 2026-10-01):** **confirm: all three pairs are different people.** Confidence: high.

- Ken Thompson (born 1943): American computer scientist, co-creator of Unix, 1983 Turing Award (https://www.britannica.com/biography/Kenneth-Lane-Thompson). E. P. Thompson (1924–1993): British social historian, *The Making of the English Working Class* (1963) (https://www.britannica.com/biography/E-P-Thompson).
- Edward Said (1935–2003): Palestinian American literary critic (https://www.britannica.com/biography/Edward-Said). Edward Sapir (1884–1939): American linguist and anthropologist (https://www.britannica.com/biography/Edward-Sapir).
- Marc Bloch (1886–1944): French medieval historian, killed by the Germans in 1944 (https://www.britannica.com/biography/Marc-Bloch). Maurice Bloch (born 1939): British anthropologist, LSE emeritus (https://www.lse.ac.uk/people/maurice-bloch).
- No data change needed. They are already `separate` in effect (never merged).

### R6. Statuses for the 900 new names
v8 adds 900 people with status `new — needs status`.
**Proposal:** assign a status now only to the new names with F ≥ 3, because only they enter the primary analysis. There are 9: Georg Wilhelm Friedrich Hegel (F 4), Duns Scotus, Edward O. Wilson, John Nash, Jorge Luis Borges, Laozi, Ludwig Mies van der Rohe, Paul Cézanne and Vint Cerf (F 3). The other 891 (F 1–2) would stay `new — needs status` until sensitivity analyses need them.

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
**Proposal (in force in METHOD §3.2):** an id freezes when its person file is created, or when v8 is published, whichever comes first. Before that, overrides may change ids.

**Recommendation (v8 agent, 2026-10-01):** **approve as written.** Confidence: high. Freezing an id once anything points at it (a person file) is standard practice for stable identifiers, and it's the simplest rule that never breaks a link. Before that point nothing depends on the id, so overrides are free. Add one line to METHOD §3.2: retired ids stay in `person_ids.csv` with a status other than `active`, so old links still resolve. The current `status` column already supports this.

## Persons schema

### P1. LIO axis scale: PROPOSED 0–4
- 0 = interventionist pole
- 1 = leans interventionist
- 2 = mixed
- 3 = leans LIO
- 4 = LIO pole

v7.1 defined the poles but no scale. Used in `worldview.lio_axes` and `systems/*/lio_axes`. PANT is scored on it as a demonstration. No person is scored yet.
**Options:** approve; use 0–2 or −2…+2; use the poles only, with a free-text position.

**Recommendation (v8 agent, 2026-10-01):** **approve 0–4.** Confidence: medium-high. v7.1 gives two poles per axis and no scale. Five ordered points with a "mixed" middle are the usual minimum for an ordinal rating that keeps a midpoint. 0–2 is too coarse to separate "leans" from "pole", which is exactly the difference the mid-basin test (P4) needs on B_cause. −2…+2 carries the same information, but the signs read as good and bad. Keep the certainty field separate from the score, as the schema already does.

### P2. Era buckets: PROPOSED
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

### P3. Regions: PROPOSED
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
**Proposal:** only a named human reviewer. Agents stop at `draft — unreviewed`.

**Recommendation (v8 agent, 2026-10-01):** **approve.** Confidence: high. This is the standard two-person rule for research data: the producer doesn't sign off its own work. It also keeps the provenance trail honest, because `reviewed` then always names a person. Suggest recording the reviewer's name and date in the existing `review` fields, and letting agents set `draft — unreviewed` and `example — unreviewed` only.

## Belief systems

### S1. CLTHEI display label
The v7.1 label is "Classical Theism (personal, interventionist Creator God)". It shares the words "Classical Theism" with CLASS_THEISM, which the v7.1 rules say it must not be confused with.
**Proposed display label:** "Interventionist personal theism". The code stays `CLTHEI` and `v7_1_label` is kept verbatim. Status in the file: `proposed — pending Jason's OK`.

**Recommendation (v8 agent, 2026-10-01):** **approve "Interventionist personal theism" as the display label.** Confidence: medium-high. The full original label is confirmed in V6: "Classical Theism (personal, interventionist Creator God)" (`V6_(history)/V6/beliefCoherence.json`, CLTHEI entry). The rubric scores there match the v7.1 data book for all 77 systems, so it is the same source table. The v7.1 rule itself separates the two codes ("CLASS_THEISM … is not CLTHEI (popular interventionist personal God)"), and the proposed label uses the rule's own words. The code and `v7_1_label` stay unchanged.

### S2. PANT display label
The v7.1 label is cut off mid-word in both the data book table and the Word file: "Pantheism (Spinozistic/naturalistic 'God = Univers…".
**Proposed display label:** "Pantheism (Spinozistic/naturalistic)", trimmed at the last whole phrase. If the full original label exists elsewhere, use it instead.

**Recommendation (v8 agent, 2026-10-01):** **use the full original label: "Pantheism (Spinozistic/naturalistic 'God = Universe')".** Confidence: high. It's in `V6_(history)/V6/beliefCoherence.json` (PANT entry, `belief_system`) and in the V6 paper's table (`V6: The Impact of Ideology on Intelligence….md`, line 390). This is the source of the v7.1 table. All 77 systems' L/P/E/V/X scores in the V6 JSON match the v7.1 data book exactly, and every truncated v7.1 label is a prefix of its V6 label. The truncation ("Univers…") happened in v7.1. The Word data book and the combined JSON are both truncated, and nothing in the v7 repo has the full text. The same V6 file also gives the full form of the other labels that v7.1 cut off (ATHE, CLASS_THEISM, PANENT, KEMET, ABORIG, MORMON, CLTHEI), if those are ever needed. If approved: set PANT's `display_label` to the full label and `label_status` to approved, and note the V6 source. Not changed here.

### S3. Expanding the rubric
The data book defines L, P, E, V and X (see DATA_DICTIONARY §4). `revised_rubric` exists in every file with status `not started`.
**Decide:** whether and when to open revised scoring, who scores, and whether revised scores need cites per axis (the schema allows it).

**Recommendation (v8 agent, 2026-10-01):** **keep the v7.1 scores frozen as the baseline, and don't open revised scoring until the first coding pool (P4) is done.** Confidence: medium. When it opens: (1) require a cite for each axis score (the schema already allows it), since the v7.1 scores are authorial and uncited; (2) have two scorers score a sample of systems independently and report agreement before anyone scores the rest; (3) Jason approves the final numbers. Revised scores sit beside the v7.1 scores and never overwrite them. That is the simplest way to keep v7.1 results reproducible.

### S4. New belief systems
Schema 1.0 allows only the 77 v7.1 codes. The validator rejects others. Adding a system (for example, splitting a popular form out of an existing code) needs a schema version bump and Jason's approval.

**Recommendation (v8 agent, 2026-10-01):** **keep the 77 codes closed for v8. Collect proposed new codes in a plain list (code, why, example people) and add them in one batch with a single schema bump.** Confidence: medium-high. A fixed code list is what makes v7.1 and v8 counts comparable, and one bump is cheaper than several. Splitting an existing code changes every count that used it, so each split should list the people it would move.

### S5. related_codes direction
`relation` reads "<code> is <relation> this system". So CLTHEI lists CLASS_THEISM as its "scholastic form of", and CLASS_THEISM lists CLTHEI as its "popular form of". Treating the two as scholastic and popular forms of one tradition is a reading of the v7.1 rule "CLASS_THEISM ... is not CLTHEI (popular interventionist personal God)".
**Options:** confirm; change both to "neighbor (easily confused)".

**Recommendation (v8 agent, 2026-10-01):** **change both to "neighbor (easily confused)".** Confidence: medium. The v7.1 rule says only that the two codes are different and easy to confuse: "CLASS_THEISM (Aristotelian-Thomistic-Falsafa) is not CLTHEI (popular interventionist personal God) and not generic CHRIST/ISLAM/JUDA." It doesn't say they are the scholastic and popular forms of one tradition. That is a further historical claim, and arguable: CLASS_THEISM spans Christian, Muslim and Jewish thinkers, while CLTHEI is defined by intervention. "Neighbor" records what the rule says and nothing more. If approved: edit `related_codes` in `systems/CLTHEI.md` and `systems/CLASS_THEISM.md`.

### S6. PANT boundaries (raised by the PANT worked example)
- Modern scientific or naturalistic pantheism: PANT (the circle) or ATHE with reverent language? v7.1 says "not atheism-plus-poetry", but this needs a test that can be applied.
- Advaita Vedanta and some Kabbalah: v7.1's PANENT label names "some Kabbalah/Advaita forms", while the Stanford Encyclopedia of Philosophy lists them among pantheist strands.
- Stoic pantheists: STOIC or PANT?

**Recommendation (v8 agent, 2026-10-01):** Confidence: medium on all three. The relevant rules are the v7.1 coding rule ("Use PANT only for the circle: Deus sive Natura, entity-in-Nature and Nature-in-entity. Not atheism-plus-poetry. Not every nature-mystic.") and the founders rule ("Code the system they founded"). The source is SEP, "Pantheism" (William Mander, rev. 2023, https://plato.stanford.edu/entries/pantheism/).

- **Scientific or naturalistic pantheism.** SEP describes it as worldviews that "make no ontological commitments beyond those sanctioned by empirical science". Its §8 explains why "atheism-plus-poetry" is a fair worry: if the only mark of divinity is feeling, then "all that distinguishes a pantheist from an atheist is feeling". SEP §§9–13 then go through the other marks that might make the whole divine: its place as the universe at large (§9), infinity, eternity or necessity (§10), ineffability (§11), being personal (§12) and value (§13). The unity of the cosmos is treated in §5. Proposed test: code PANT only if the person's own writing (1) identifies God or the divine with Nature as a whole, as a claim about what exists, not as a figure of speech, **and** (2) gives the whole at least one mark beyond feeling, such as unity as one substance or order (§5), necessity or eternity (§10), something mind-like (§12) or value (§13). Reverent language with neither of these is ATHE (positive naturalism), or SECHUM if the person's public identity is the humanist movement. Einstein-style "Spinoza's God" statements pass (1); "nature is awe-inspiring" alone does not.
- **Advaita Vedanta and some Kabbalah.** SEP lists them among traditions "marked by pantheistic ideas and feelings", while v7.1's PANENT label names "some Kabbalah/Advaita forms". SEP also says the lines between immanence, pantheism and panentheism "are vague and porous". Proposed rule: by default, code the host tradition (HINDU, JUDA) as primary, under "Primary = dominant working metaphysics". Use PANENT when the person's writing keeps a divine reality that includes but exceeds the world, which is how v7.1 labels these forms. Use PANT only if they pass the two-part test above. Don't code PANT just because they belong to the tradition.
- **Stoic pantheists.** SEP calls Stoic physicalism "an ancient form of pantheism". It also reports the argument (Baltzly 2003) that the Stoic God was personal and providential, someone "to whom we might approach in prayer". That clashes with the PANT circle on petition and the B axis. Proposed rule: code STOIC for ancient Stoics and for anyone whose avowed school is Stoicism. This follows the founders and "dominant working metaphysics" rules, and STOIC is its own code with its own score. Reserve PANT for later thinkers who take the Stoic or Spinozist identity without the providential, prayer-hearing deity.

## Decided

(none yet)
