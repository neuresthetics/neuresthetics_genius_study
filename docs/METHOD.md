# Method

How the v8 database is built: where the names come from, how they are counted and merged, how people get ids and files, and what stays outside the data. For field definitions see [DATA_DICTIONARY.md](DATA_DICTIONARY.md). For how to code a person or a system see [CODING_GUIDE.md](CODING_GUIDE.md). For the step-by-step research run see [RUNBOOK.md](RUNBOOK.md). Choices that still need Jason's sign-off are in [OPEN_DECISIONS.md](OPEN_DECISIONS.md).

## 1. What the study is measuring

The study has two lanes, carried over from v7.1:

- **Lane A** is descriptive. Who is on the roster, what they did, when and where, and what their adult working worldview was, each with sources and a certainty grade. Lane A makes no claim about causes.
- **Lane B** is a belief model, labelled so it can fail. It says that early exposure to the "circle" (Deus sive Natura: entity applied to Nature, Nature rendered in entity) together with geometric form (definition → consequence, no reserved clause) reduces split-model load. Lane B fields in a person record are inputs to that model. They are not findings.

"Genius" here means lasting original impact on stated achievement criteria. It is not an IQ score. Collectives are out (teams, "the Wright Brothers"), and so are transient fame and mastery without originality.

## 2. The roster

### 2.1 Inputs

The roster starts from five lists made once, in the V6 period, by asking five models (Claude, DeepSeek, Gemini, ChatGPT, Grok) for a list of geniuses with fields. The lists are in `data/sources/model_lists/` as byte-for-byte copies, with checksums in `data/sources/SHA256SUMS`. They are never re-generated. They are the fixed starting point for every roster build, so any change to the roster has to come from a change in method, which is visible in git.

| List | Rows |
|---|---|
| Claude | 374 |
| DeepSeek | 997 |
| Gemini | 669 |
| GPT | 376 |
| Grok | 330 |
| **total** | **2,746** |

The v7.1 combined JSON (`data/sources/v7_1/neuresthetics_v7_combined.json`) supplies the v7.1 roster (data book section 9, `tables[6]` in the JSON) for comparison and status carry-over, plus the v7.1 merges, exclusions and review flags (section 10, `tables[7]`). The v7 500-row aggregate (`geniiAggregateSortFreq.csv`) is kept only to show where the v7 numbers came from.

### 2.2 Normalization (automatic)

`scripts/rebuild_roster.py` turns each raw name into a formatting key:

1. Split "X - Y" compound entries and keep Y. X is recorded as an alias, or as a collective prefix (e.g. Claude's "Wright Brothers - Orville Wright").
2. Drop parentheticals.
3. Strip accents (Unicode NFKD, plus a short table for letters like ø, ł, ß, æ, þ).
4. Join apostrophe surname prefixes (O'Keeffe, O-Keeffe → okeeffe).
5. Lowercase, and turn every non-letter (hyphen, period, apostrophe) into a space.
6. Join runs of single-letter initials (B. F. → bf).
7. Keep Jr./Sr., so father and son stay apart.
8. Sort the tokens, so "Pascal-Blaise", "Blaise Pascal" and "Blaise-Pascal" give the same key.

Names with the same key are the same person. This step only removes formatting differences. It never guesses.

Result: 1,715 distinct raw name strings (after lowercasing and de-accenting) became 1,416 distinct keys.

### 2.3 Curated merges (by hand)

The rebuild does no fuzzy merging. Every merge beyond formatting is a row in `data/roster/curated_aliases.csv` with a decision, a confidence and a reason:

| decision | count | meaning |
|---|---|---|
| `merge` | 32 | two keys are the same person (Avicenna → Ibn Sina, Buddha → Siddhartha Gautama, Benedict de Spinoza → Baruch Spinoza, ...) |
| `separate` | 26 | keys that look alike but are different people (George Washington / George Washington Carver, Zeno of Elea / Zeno of Citium, W.H. / W.L. Bragg, ...) |
| `exclude` | 4 | not a person, or a collective (Wright Brothers, plus Orville and Wilbur Wright listed individually; Anderson localization) |
| `flag` | 0 | kept as listed, but a human should look (none left) |
| `display_fix` | 27 | the display spelling is corrected; identity is unchanged (includes GPT's "Brian-Maynard-Smith" → John Maynard Smith). In `alias_map.csv`, a fix that only changes formatting (same key) keeps rule `format`; a fix that changes the name itself gets rule `name_correction`, with the curated reason as the note (6 of 27) |

`confidence` is `high`, `medium` or `low` for the agent's judgment, or `confirmed` when Jason has approved the row. A confirmed row names the date and the OPEN_DECISIONS item in its reason (R2–R5, 2026-10-01).

After the 32 curated merges there are 1,384 keys. With the 4 excluded keys, that leaves **1,380 people**.

The script also runs a similarity scan (string ratio ≥ 0.86, or one name's tokens being a subset of the other's). Pairs it finds are **not** merged. They are written to `merge_log.csv` with action `NOT merged - review suggested` for a human check. The first v8 scan found three pairs (Ken / E.P. Thompson, Edward Said / Edward Sapir, Marc / Maurice Bloch). All three were confirmed as different people (decision R5) and are now `separate` rows, so the scan lists none.

### 2.4 Frequency F

F is the number of **distinct models** that list the person, from 1 to 5. A model that lists someone twice still counts once (452 same-model duplicates are logged). F measures agreement between models after alias merging. It does not measure how great someone is.

| F | people | band |
|---|---|---|
| 5 | 82 | high (5) |
| 4 | 55 | core (3–4) |
| 3 | 94 | core (3–4) |
| 2 | 183 | extended (2) |
| 1 | 966 | single-source (1) |

The v7.1 coding rules set the primary analysis cut at F ≥ 3, with sensitivity runs at F ≥ 4 and F ≥ 2. F = 1 people stay on the roster but out of the primary table.

### 2.5 Field and field bucket

`field` is the most common normalized field string across models, with one vote per model. Ties go to the candidate whose components appear in the most models' field strings, then to model order Claude, Grok, GPT, Gemini, DeepSeek. Ties are noted in `notes`.

`field_bucket` comes from keyword rules in the script (the `BUCKETS` table), applied to the first field component that matches. There are 21 buckets. Six fixes run first (decision R7, 2026-10-01; `BUCKET_FIXES` and `PERSON_BUCKETS` in the script):

1. "science studies" paired with philosophy → philosophy (philosophers of science such as Hempel and Nagel; "philosophy of science" already went there);
2. "space" with "explor…" or "astronaut" → exploration (the five astronauts);
3. "political thought" → politics / law / military (rulers and statesmen, which "politics" already sent there);
4. "social thought" → politics / law / military (King, Tubman, Mother Teresa);
5. "geography-sociology" → social science (David Harvey);
6. Jan Swammerdam → biology / life science (his field string "microscopy" also covers Robert Hooke, who stays in physics).

They moved 31 people (`reports/r7_bucket_changes.csv`). Four have F ≥ 3: Mandela, Machiavelli, Gandhi and King, all from social science to politics / law / military. The evidence for the fixes is in `reports/r7_bucket_spotcheck.csv` and `reports/r7_field_string_review.csv`. Strings marked "arguable" there (for example "science studies-sociology", "paleoanthropology") were left as the rules put them.

To compare with v7.1's published bucket table, read v8's `politics / law / military` against v7.1's `social science / politics`. v7's own bucket mapping is not in the repo, so the v7→v8 diff re-buckets the v7 roster with the same rules for a like-for-like comparison.

### 2.6 Canonical name

The display name comes from three sources, in this order of preference:

1. a curated `display_fix`;
2. the v7.1 roster name, if the person was in v7.1;
3. the best-formatted raw string, with model preference Claude, Grok, DeepSeek, Gemini, GPT. Gemini's second-half "Last-First" repeats are deprioritized, and GPT's hyphens become spaces.

### 2.7 Status

v7.1 tagged people `core`, `provisional` ("Contemporaries may be provisional", two-lane paper) or `review` ("Review = paradigm-shift bar is arguable", data book). These tags are carried over by matching v7.1 names and their listed aliases to v8 keys. A status set by a recorded decision goes in `data/roster/status_overrides.csv` and wins over the carry-over. No other status is invented:

| status | count |
|---|---|
| core | 441 (431 from v7.1; Georgia O'Keeffe, whose v7.1 status was blank, decision R1; and the 9 new F ≥ 3 names, decision R6) |
| provisional | 33 |
| review | 17 |
| new — needs status | 889 |

Decision R6 (2026-10-01): only the new names with F ≥ 3 get a status now, because only they enter the primary analysis. All 9 are core: Hegel, Duns Scotus, Edward O. Wilson, John Nash, Jorge Luis Borges, Laozi, Ludwig Mies van der Rohe, Paul Cézanne and Vint Cerf. The 889 new names with F 1–2 stay `new — needs status` until a sensitivity analysis needs them. A name that later reaches F ≥ 3 gets a status the same way, through `status_overrides.csv`.

### 2.8 Why the v7 frequencies were wrong

The rebuild re-ran the logic of the V6 aggregation script and reproduced the v7 500-row aggregate exactly (500/500 names). So these causes are confirmed, not guessed:

1. **Claude's list was never read.** The script's file list left it out, so a clean name could reach at most 4, and Claude-only names could not appear at all.
2. **It counted rows, not models.** Gemini repeats most of its list in "Last-First" form, and DeepSeek repeats many names. This is how F > 5 arose (Ibn Sina 9 = Avicenna 5 + Ibn Sina 4).
3. **Hyphens and accents were deleted** instead of becoming spaces or plain letters. "John-Nash" became "johnnash" and "René" became "ren". The 0.9 similarity step rescued long names but not short ones.
4. **The aggregate was cut at 500 rows.** The cut fell inside the count-1 tail at "Attar-Farid ud-Din", which dropped 1,143 entries. Hegel (split into four variants), Cantor, Boltzmann, Babbage, Rawls, Dijkstra and John Nash were lost this way.
5. **The 0.9 fuzzy merge joined different people.** Arthur Schlesinger Sr. was merged into Jr. The same step also joined Andrey/Andrei Kolmogorov, which v8 keeps merged, but by an explicit curated row.

Full detail is in `versions/v8/roster_diff_v7_to_v8.md`.

### 2.9 Reproducing the roster

```bash
python3 scripts/rebuild_roster.py --check    # rebuild in a temp dir; byte-compare roster.csv, alias_map.csv, merge_log.csv and the diff
python3 scripts/rebuild_roster.py            # rewrite the committed outputs (after changing curated_aliases.csv or the script)
```

`roster.csv`, `alias_map.csv` and `merge_log.csv` are never edited by hand. To change the roster, edit `curated_aliases.csv`, `status_overrides.csv` (or the script) and rebuild. The run takes about 30 seconds because the similarity scan compares every pair.

## 3. Person ids, files and sharding

### 3.1 Ids

Every roster name gets a stable id in `data/roster/person_ids.csv`, made by `scripts/assign_ids.py`:

- ASCII, lowercase, hyphen-separated, family name first: `newton-isaac`, `van-gogh-vincent`, `king-martin-luther-jr`.
- Mononyms stay as they are: `aristotle`, `hypatia`.
- Written order is kept for "X of Y", "X the Great", Ibn/Al-/Abu names and Italian da/di names: `augustine-of-hippo`, `ibn-sina`, `leonardo-da-vinci`.
- Particles (van, von, de, du, der, den, la, le, ten, ter, y, del, della, dos, das) stay attached to the family name, so `ramon-y-cajal-santiago`.
- Exceptions that the rule would get wrong are listed in `data/roster/id_overrides.csv` (30 rows), each with a reason. They cover: family name written first (Sun Tzu, Zhang Heng, Li Bai and other Chinese names); court and art names in conventional order (Murasaki Shikibu, Katsushika Hokusai); compound or double family names (`mies-van-der-rohe-ludwig`, `garcia-marquez-gabriel`); a title in the roster name (`thomson-william-kelvin`, `byron-lord`); a religious name (`tenzin-gyatso`); a compound family name added by decision R3 (`maynard-smith-john`).
- A clash gets `-2`, `-3` and is reported so that someone can add an override instead.

**The ids are heuristic.** They were made by rule plus a reviewed list of overrides, not by checking each name against an authority file. Before a person file exists, a wrong id can be fixed by adding an override and rerunning.

### 3.2 Id freeze policy

- An id is **frozen** once a person file exists for it, or once v8 is published, whichever comes first. After that it is never renamed or reused, even if the spelling turns out to be wrong. Fix the display name instead.
- This policy was approved as written (decision R8, 2026-10-01).
- `assign_ids.py` only appends. A name that leaves the roster keeps its row with status `retired`, so old links still resolve, and a retired id is never reused. Three ids are retired so far: `wright-orville`, `wright-wilbur` (R2) and `smith-brian-maynard` (R3). If a roster name is renamed, add the old→new pair to `id_overrides.csv` with the old id, so the id follows the person.
- `python3 scripts/assign_ids.py --check` fails if `person_ids.csv` is out of date with `roster.csv`.

### 3.3 Sharding

Person files live at `people/<shard>/<id>.md`, where the shard is the first character of the id. Two reasons:

1. The GitHub web interface shows at most 1,000 entries when listing a directory. A single `people/` folder with 1,380 files would hide some of them in the browser.
2. A first-letter shard can be worked out from the id alone, and it never changes, because the id never changes. No lookup table is needed to find a file. The largest shard is `s`, with 126 ids.

## 4. Record format

Each person and each belief system is one Markdown file with a YAML front-matter block:

- **Front matter** holds the structured, machine-checked fields. Every factual field is a *claim*: `value`, `certainty`, `cites` (source id plus locator), `how_known`, and optional `note` and `alternatives`.
- **Body** holds the prose: summary, narrative and research log, with inline `[S#, locator]` citations.

Why this format:

- One file per person keeps long prose and checkable structure together, with no paired files to drift apart.
- It renders on GitHub.
- It diffs line by line in review.
- It can be validated against a JSON Schema.

Schemas are in `schema/`. Templates are in `templates/`. `scripts/validate_people.py` and `scripts/validate_systems.py` check the schema and much more (see [RUNBOOK.md](RUNBOOK.md#5-validate)).

### 4.1 Sentinels

A value that is not a real value is one of three words, never blank:

- `TODO`: not researched yet.
- `UNKNOWN`: researched, and no reliable source gives it. `how_known` says what was checked.
- `BELOW_THRESHOLD`: some evidence exists, but it is below certainty 0.5, so the value is withheld. `note` describes the evidence.

### 4.2 Certainty

There are three grades. Worldview claims use the v7.1 scale:

| grade | basis |
|---|---|
| 1.0 | written profession |
| 0.7 | consistent private letters |
| 0.5 | scholarly reconstruction |

Other facts use 1.0 established, 0.7 probable, 0.5 contested. Below 0.5, the value is withheld. Details are in [CODING_GUIDE.md](CODING_GUIDE.md#3-certainty).

## 5. Belief systems

The v7.1 data book scored 77 belief systems on a five-axis coherence rubric (L, P, E, V, X, each 0–10). v8 gives each system its own record in `systems/<CODE>.md`, where the code is the v7.1 abbreviation. Each record carries:

- the v7.1 scores unchanged, labelled "authorial v7.1 scores" and checked against the data book;
- a slot for revised scores with a rationale per axis;
- metaphysics, LIO-axis positions, schools and variants, stance on science, coding guidance and sources.

`scripts/make_system_stubs.py` made the 77 stubs from the data book section 6 score table (`tables[4]`) and the section 7 scoring notes. PANT is the worked example. Adherent numbers are context only and **never** a denominator for genius rates. This follows the v7.1 rule "No G/P_2025: no present-day religion stock as a denominator."

## 6. What stays out

- No per-capita genius rates by religion. The old 1,200-per-million table is retired.
- No present-day adherent counts as denominators.
- Heritage (ethnicity, baptism, childhood catechism) is recorded as context. It is never an outcome and never a worldview code.
- No invented facts or citations. Unsourced fields stay `TODO`.
- Wikipedia may be used to find leads but is never cited.

## 7. Coverage

`scripts/coverage_report.py` writes `reports/coverage.md`. It covers:

- person files against the roster, by F band and field bucket;
- review-status counts;
- claim fill rates by section;
- the first-pool checklist;
- the same figures for systems.
