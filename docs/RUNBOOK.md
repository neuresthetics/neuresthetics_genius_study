# Runbook

Step by step: how to add or extend one record. The database grows **one person per run**. A run picks one person, researches them, writes or extends their file, validates it, and commits. The same procedure, with small changes, applies to belief systems (Part 2).

Read [CODING_GUIDE.md](CODING_GUIDE.md) first. Field definitions are in [DATA_DICTIONARY.md](DATA_DICTIONARY.md).

## 0. Setup (once)

```bash
git clone https://github.com/neuresthetics/neuresthetics_genius_study.git
cd neuresthetics_genius_study
python3 -m venv .venv && . .venv/bin/activate
pip install -r scripts/requirements.txt     # PyYAML, jsonschema (validators and coverage report)
```

The roster scripts (`rebuild_roster.py`, `assign_ids.py`, `make_data_dictionary.py`) use only the standard library.

Check that everything is consistent before you start:

```bash
python3 scripts/rebuild_roster.py --check
python3 scripts/assign_ids.py --check
python scripts/validate_people.py
python scripts/validate_systems.py
```

---

# Part 1: One person per run

## 1. Pick the person

Order of work (from the v7.1 rules, "First pool" and "Frequency cut"):

1. The first pool, in this order: Faraday (done as the worked example), Maxwell, Newton, Aquinas, Ibn Sina, Gödel. These are "mid-basin theists coded first as a stress test".
2. Physical science 1600–1950 with F ≥ 3.
3. Everyone else with F ≥ 3 (the primary analysis cut).
4. F = 2, then F = 1. These are for sensitivity analysis and stay out of the primary table.

`reports/coverage.md` shows which first-pool people have files. Find the person's id:

```bash
grep -i "maxwell" data/roster/person_ids.csv
# maxwell-james-clerk,James Clerk Maxwell,m,people/m/maxwell-james-clerk.md,active,v8,family name first,
```

If the id looks wrong (e.g. family name order), fix it now with a row in `data/roster/id_overrides.csv` and run `python3 scripts/assign_ids.py`. This is only possible before the file exists (METHOD §3.2).

## 2. Create the file

```bash
mkdir -p people/m
cp templates/person.template.md people/m/maxwell-james-clerk.md
```

Then fill in:

- `record`: set `review_status: draft — unreviewed`, `collected_by`, `model_used` (model name and version, or `none (human)`), the dates, and a first `change_log` entry.
- `identity`: copy the roster row exactly from `roster.csv`:
  - `canonical_name`, `rank`, `F`;
  - `models` as a YAML list;
  - `band`, `status`, `field`, `field_bucket`.

  The validator compares every value with `roster.csv`.

## 3. Research

### 3.1 Source hierarchy

Use the best source available for each claim, in this order:

1. **Primary sources.** The person's published works, letters, notebooks and diaries, in a scholarly edition or a reliable transcription (e.g. the Ɛpsilon edition of Faraday's correspondence). Also contemporary records: parish registers, institutional minutes.
2. **Scholarly secondary sources.** Biographies from academic presses, peer-reviewed articles, the Oxford Dictionary of National Biography and the national equivalents (Dictionary of Scientific Biography, Neue Deutsche Biographie, ...), and the Stanford Encyclopedia of Philosophy.
3. **Signed reference works and institutional pages.** Encyclopaedia Britannica articles with a named author, and pages from museums, academies and the person's own institutions. These are usually *tertiary*. Use them for undisputed basics, and look for a better source on anything contested.
4. **Wikipedia and other unsigned wikis.** Use them only to find leads (names of letters, editions, biographers). **Never cite them.** Follow the lead to the source and cite that.

Don't cite AI model output, including the model lists. The roster is cited only as "study roster" for the roster block.

### 3.2 What to look for

Work through the sections in this order. Each one makes the next easier:

1. **Basics and contribution.** Dates, places, the main contributions and evidence of impact.
2. **Childhood.** Family religion and practice, schooling, early mathematics, early science, early reading, mentors.
3. **Worldview.** Own words first: public professions of faith or unbelief, then letters. Then scholarly analyses. Collect verbatim quotations with locators.
4. **Heritage.** Ethnic and religious background by birth, baptism, catechism.
5. **Timing.** When the views are first documented, relative to the major work.
6. **Lane B.** Only after the Lane A facts are in.

### 3.3 Reading online sources

- Record the access date for every online source (`accessed`). Add an archived copy (`archive_url`, e.g. web.archive.org) where one exists.
- If you only saw a title, abstract or catalogue entry, say so in `reliability_note` ("title only consulted"). Don't cite such a source for anything beyond what you actually read.
- PDFs: read the actual pages and cite page numbers.

## 4. Write

### 4.1 Claims

Each fact goes in its field as a claim:

Example (from `people/f/faraday-michael.md`):

```yaml
birth:
  date:
    value: "1791-09-22"
    certainty: 1.0
    cites: [{source: S1, locator: "opening sentence and Quick Facts"}, {source: S4, locator: "letter text: 'next Sabbath day (the 22nd) I shall complete my 70th year'"}]
    how_known: "Encyclopedia date, matched by Faraday's own statement in a letter of 19 Sept 1861."
```

- `locator` must let a reader find the passage: page, section heading, letter number, paragraph, folio, or URL anchor.
- `how_known` is one or two sentences: the kind of evidence, and why this certainty.
- Conflicting sources: give the best-supported value, add an `alternatives` entry for each competitor with its own cite, and lower certainty to 0.5 if the dispute is real (P25). Add a line to `review.data_quality_flags`. A detail that only one of two sources gives goes in its own note at 0.7, or the field is capped at 0.7.
- One reliable source gives at most 0.7 (P15). 1.0 needs two independent reliable sources or a primary document.
- Do not cite Britannica's AI-generated "Top Questions" boxes; check a quote found in SEP or another secondary source against the primary text before citing it as the person's words (P26).
- Not found after searching, or only off-point items found: write `value: UNKNOWN` and a `how_known` listing what you checked (P19).
- Not researched in this run: leave `value: TODO`.
- Evidence that bears on the point but is too weak (below 0.5: reported speech, a single letter, a paraphrase, an implication): write `value: BELOW_THRESHOLD`, with the evidence described in `note` (P19).

### 4.2 Sources

Add each source to `sources` once, with ids S1, S2, ... in the order you add them:

Example (from the Faraday record):

```yaml
- id: S3
  type: primary
  kind: letter
  author: "Michael Faraday"
  year: 1844
  citation: "Faraday, Michael. Letter to Augusta Ada Lovelace, 24 October 1844. Record Faraday1631 in Ɛpsilon: The Michael Faraday Collection. https://epsilon.ac.uk/view/faraday/letters/Faraday1631. Source of text: Bodleian Library, MS dep Lovelace-Byron 171, ff. 44–5, and Faraday's copy, IEE MS SC 3. Also published in The Correspondence of Michael Faraday, vol. 3 (1996)."
  url: "https://epsilon.ac.uk/view/faraday/letters/Faraday1631"
  accessed: 2026-10-01
  reliability_note: "Scholarly transcription from the edited correspondence (Faraday Project). ..."
  used_for: [worldview, collaborators]
```

Citation style is Chicago (notes or author-date). Give author, title, publication or edition, date, and pages. For journal articles give volume(issue): pages, plus a DOI if there is one.

### 4.3 Body

Fill each required `##` section in plain prose, with inline cites `[S3, letter 1631]`. The body explains and connects. It doesn't add facts that the front matter lacks. The **Research log** records what you did in this run: sources read, searches that found nothing, and what is left.

### 4.4 Uncertainty, in short

| situation | what to write |
|---|---|
| two independent reliable sources agree, or a primary document | certainty 1.0 (P15) |
| one good source, dependent sources, or a name-order or name-form disagreement | 0.7 |
| reliable sources disagree | 0.5 + `alternatives` (alternative named) + data-quality flag (P25) |
| inferred from the person's work or conduct, no direct statement | 0.5; worldview basis `inference_from_work` (P24) |
| worldview from public writing / letters or recorded interview / scholar's reconstruction | 1.0 / 0.7 / 0.5 with matching `basis` |
| some evidence that bears on the point but is weaker than 0.5 | `BELOW_THRESHOLD` + `note` (P19) |
| searched, the sources say nothing on the point | `UNKNOWN` + `how_known` listing what was checked (P19) |
| not looked at yet | `TODO` |

## 5. Validate

```bash
python scripts/validate_people.py people/m/maxwell-james-clerk.md
python scripts/validate_people.py --strict people/m/maxwell-james-clerk.md   # warnings become errors
python scripts/recompute_ages.py --check people/m/maxwell-james-clerk.md    # ages = event year − birth year (P30)
```

The validator checks:

- the schema (claim shape, enums, sentinels);
- that the file is at the path listed in `person_ids.csv`;
- that `identity.roster` equals the `roster.csv` row;
- that worldview codes exist in `systems/`;
- that `basis` agrees with `certainty`;
- that every cite, in front matter and in the body, points at a listed source, and warns about unused sources;
- that collaborator `roster_id`s exist;
- that the required body sections are present.

Fix every error. Fix warnings, or explain them in the research log.

Then refresh the coverage report:

```bash
python scripts/coverage_report.py
```

## 6. Commit

One person per commit, for example:

```
Add James Clerk Maxwell person record (draft)

Sources: <short list>. Worldview coded <CODE> at <certainty> / left TODO.
Open: <one line>.
```

- When extending an existing file, raise `record.record_version` by 1, add a `change_log` entry, and update `last_updated`. Use the subject `Extend <name> record: <what>`.
- Commit `reports/coverage.md` in the same commit.
- Don't change roster files, schemas or other people's files in a person commit. Make a separate commit for those.

## 7. Review

A human reviewer:

1. checks every filled claim against its cite;
2. reads the quotes against the source;
3. checks the worldview reasoning against [CODING_GUIDE.md](CODING_GUIDE.md);
4. then sets `review_status: reviewed`, `reviewed_by` and `reviewed_on`.

The validator requires both review fields when the status is `reviewed`. Agents never set `reviewed`. If a check fails, the status becomes `needs revision`, with the reasons in `review.open_questions`.

---

# Part 2: Belief systems

## 8. Extending a system record

1. Open `systems/<CODE>.md`. All 77 exist as stubs. Set `review_status: draft — unreviewed`, raise `record_version`, and add a `change_log` entry.
2. **Don't touch `v7_1_rubric`, `identity.v7_1_number` or `identity.v7_1_label`.** The validator checks the rubric scores, the number and the scoring note against the data book. The label is verbatim from v7.1 by convention, so propose any change through `display_label`.
3. Sources for systems, in order of preference:
   1. the system's own authoritative texts, in scholarly editions or translations;
   2. scholarly reference works (Stanford Encyclopedia of Philosophy, Encyclopedia of Religion, Routledge Encyclopedia of Philosophy, Oxford Handbooks);
   3. scholarly monographs.

   For adherent numbers, use demographic sources (e.g. Pew Research Center, World Religion Database) with year and scope. Wikipedia is a lead only.
4. Fill, in order:
   1. `classification` and `origins`;
   2. `metaphysics` (value plus stance for each item);
   3. `lio_axes` with rationale;
   4. `epistemology`, `ethics`, `practice`, `science`;
   5. `schools_and_variants` (always split the scholastic and popular forms where they differ);
   6. `coding_guidance`.

   Leave anything unsourced as `TODO`.
5. Describe the official or scholarly form in the main fields. Variants go in `schools_and_variants`.
6. A display label change gets `label_status: proposed — pending Jason's OK` and a line in `docs/OPEN_DECISIONS.md`.
7. Validate and commit:

```bash
python scripts/validate_systems.py systems/<CODE>.md
python scripts/coverage_report.py
git commit -m "Extend <CODE> system record: <what>"
```

`scripts/make_system_stubs.py` regenerates stubs from the data book. It never overwrites a file whose status is not `stub`, but it is only needed if a stub is lost.

## 9. Changing schemas

- A new field or enum value needs a change in both `schema/*.schema.json` and the template, plus a `schema_version` bump in every file and a CHANGELOG entry.
- Then run `python3 scripts/make_data_dictionary.py` and all the validators.
- A new belief system (beyond the 77) is not added during v8 (decision S4). Add it to the list of proposed codes with the reason and example people; new codes go in together, in one batch with one schema bump and Jason's approval.

## 10. Troubleshooting

| message (abridged) | fix |
|---|---|
| `identity/roster/<field>: file has ..., roster.csv has ...` | Copy the roster row again. If the roster changed, rebuild first. |
| `file is at ... but person_ids.csv says ...` | Move the file to the listed path. |
| `filled claim without citations` | Add a cite, or set the value back to `TODO`. |
| `a filled worldview claim needs basis` | Add `basis` (written_profession / consistent_private_letters / recorded_interview / scholarly_reconstruction). |
| `basis recorded_interview needs how_known to start with '(interview)'` | Start the field's `how_known` with "(interview)" (P8 flag, CODING_GUIDE §7). |
| `basis ... allows certainty at most ..., got ...` | Ceilings: `written_profession` 1.0, `consistent_private_letters` 0.7, `recorded_interview` 0.7, `scholarly_reconstruction` 0.5. |
| `front matter cites S9, which is not in sources` / `body cites [S9] ...` | Add the source, or fix the id. |
| `source S4 is listed but never cited` (warning) | Cite it or remove it. `--strict` turns this into an error. |
| `body is missing the section '## ...'` | Add the heading, spelled exactly as listed. |
| `code 'XYZ' is not a file in systems/` | Use one of the 77 codes. |
| `v7_1_rubric/... data book has ...` / `scoring_note is not verbatim` | Restore the v7.1 values. Regenerate the stub if needed. |
| `rebuild_roster.py --check` reports a difference | Someone edited a generated roster file by hand. Rebuild from `curated_aliases.csv`. |
