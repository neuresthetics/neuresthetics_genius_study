# Data dictionary

Every file and field in the v8 database. The roster CSVs are described by hand below. The person and system record fields are rendered from the JSON Schemas by `scripts/make_data_dictionary.py`, so they match what the validators enforce. To change a field description, edit the schema and rerun the script. Don't edit inside the generated blocks.

Contents:

1. [Conventions](#1-conventions)
2. [Roster files](#2-roster-files) (`data/roster/`)
3. [Person records](#3-person-records) (`people/<shard>/<id>.md`)
4. [System records](#4-system-records) (`systems/<CODE>.md`)
5. [Reports](#5-reports)

## 1. Conventions

- **Encoding:** UTF-8 everywhere. CSVs have a header row, comma separators, and RFC 4180 quoting.
- **Dates:** ISO 8601, `YYYY-MM-DD`. Partial dates are `YYYY` or `YYYY-MM`. Negative years are BCE: `-384` means 384 BCE, and astronomical year numbering (where 1 BCE = year 0) is *not* used. Old Style dates keep the source date and set `calendar: julian`.
- **Lists inside CSV cells** use `; ` (semicolon and space). `per_model_field` uses ` | ` between models.
- **Claim:** a field in a record that holds a researched fact. Its keys are:
  - `value`: the fact, or a sentinel;
  - `certainty`: 1.0, 0.7 or 0.5;
  - `cites`: a list of `{source, locator}`;
  - `how_known`: one or two sentences on the kind of evidence and why this certainty;
  - optional `note`;
  - optional `alternatives`: competing values, each cited.

  A filled value needs `certainty`, at least one cite, and `how_known`.
- **Sentinels:** these replace a value; they are never blank.
  - `TODO`: not researched yet.
  - `UNKNOWN`: researched and not findable. Say what was checked.
  - `BELOW_THRESHOLD`: evidence below 0.5, so the value is withheld. Describe the evidence.
- **Source ids** (`S1`, `S2`, ...) are local to each file.
- **Decision tags** such as P1 or S3 in a description point to the decided item in [OPEN_DECISIONS.md](OPEN_DECISIONS.md). No scale or list is still marked PROPOSED.
- **Reference tables:** `data/reference/regions.csv` maps each country or area (UN M49) to a study region (decision P3). See `data/reference/README.md`.

## 2. Roster files

### 2.1 `data/roster/roster.csv`

One row per person (1,380 rows). Written by `scripts/rebuild_roster.py`. Never edit by hand.

| column | type | meaning |
|---|---|---|
| `rank` | integer | Row order: sorted by F (high to low), then by de-accented name. **Not** a quality ranking. |
| `canonical_name` | text | Display name (see METHOD §2.6). The join key to `person_ids.csv`. |
| `field` | text | Most common normalized field string across models, one vote per model (METHOD §2.5). |
| `field_bucket` | text | One of 21 buckets from the keyword rules in the script, after the six R7 fixes (METHOD §2.5). |
| `F` | integer 1–5 | Number of distinct models listing the person. |
| `band` | text | `high (5)`, `core (3–4)`, `extended (2)`, `single-source (1)`. |
| `models` | list (`;`) | Which models list the person, in fixed order Claude;DeepSeek;Gemini;GPT;Grok. |
| `Claude`, `DeepSeek`, `Gemini`, `GPT`, `Grok` | 0/1 | 1 if that model lists the person. They sum to F. |
| `status` | text | `core`, `provisional`, `review` (carried from v7.1, or set in `status_overrides.csv` by a recorded decision), `needs status (blank in v7)` (none left in v8), or `new — needs status`. |
| `v7_name` | text | Name on the v7.1 roster, blank if new. |
| `v7_F` | integer | v7.1 frequency (could exceed 5 because of the v7 counting errors). Blank if new. |
| `v7_status` | text | v7.1 status, blank if new or blank in v7. |
| `F_change_vs_v7` | integer or `new` | v8 F minus v7 F; `new` if not in v7.1. |
| `aliases_merged` | list (`;`) | Raw name strings merged into this person (format variants and curated aliases). |
| `per_model_field` | text | Each model's raw field string, as `Model: field`, joined with ` \| `. |
| `v7_review_note` | text | Review reason copied from v7.1 data book section 10 (`tables[7]`), if any. |
| `notes` | text | Machine-written notes, joined with `; `. They cover field ties, flags, display fixes, collective prefixes, and v7 rows that were split. |

### 2.2 `data/roster/alias_map.csv`

One row per raw name string per model, plus keep-separate and flag rows.

| column | meaning |
|---|---|
| `variant` | The raw string as the model wrote it. |
| `model` | Which list it came from (blank for curated rows that are not tied to one list). |
| `variant_key` | The formatting key (METHOD §2.2). |
| `canonical` | The person it maps to, or `(EXCLUDED)`. |
| `rule` | How it was mapped. `identical`: same as the canonical name. `format`: differs only in formatting (same formatting key as the canonical name). `name_correction`: a curated `display_fix` that changes the name itself, not just its formatting (the corrected name has a different key); the note is the curated row's reason and the confidence is the curated row's. `curated alias` or `curated alias (target side)`: a merge row in `curated_aliases.csv`. `curated: keep separate`. `curated: flag`. `exclude`. |
| `confidence` | `high`, `medium`, `low` or `confirmed` (from the curated row; formatting merges are `high`). |
| `merged` | `yes` if the variant was folded into another string's person, `n/a` for the canonical string itself, `no` for keep-separate, flag and exclude rows. |
| `note` | Reason. |

### 2.3 `data/roster/merge_log.csv`

One row per merge event or review item.

| column | meaning |
|---|---|
| `canonical` | Person after the merge, or `(EXCLUDED)`. |
| `variant` | The string merged in. For exclusions, all strings joined with ` \| `. |
| `models` | Models involved. |
| `action` | `merged`, `same-model duplicate counted once`, `excluded`, or `NOT merged - review suggested`. |
| `rule` | `format`, `name_correction`, `curated alias`, `curated alias (target side)`, `distinct-model count`, `exclude`, `similar spelling`, `token subset`. |
| `confidence` | `high`/`medium`/`low`/`confirmed`, or `similarity 0.xx` for scan pairs. |
| `note` | Reason. |

### 2.4 `data/roster/curated_aliases.csv` (hand-maintained input)

| column | meaning |
|---|---|
| `variant` | A raw name (any formatting; it is keyed the same way as the lists). |
| `target` | The canonical person for `merge`, the other person for `separate`, the corrected display name for `display_fix`. Blank for `exclude`/`flag`. |
| `decision` | `merge`, `separate`, `exclude`, `flag`, `display_fix`. |
| `confidence` | `high`, `medium`, `low`, or `confirmed` (approved by Jason; the reason names the date and OPEN_DECISIONS item). |
| `reason` | Why. Required. |

### 2.5 `data/roster/person_ids.csv`

Written by `scripts/assign_ids.py`. Append-only.

| column | meaning |
|---|---|
| `id` | Stable person id (METHOD §3.1). Frozen once a person file exists or v8 is published. |
| `canonical_name` | Roster name the id was assigned to. |
| `shard` | First character of the id. |
| `path` | `people/<shard>/<id>.md`. |
| `status` | `active` or `retired` (left the roster; row kept, id never reused). |
| `assigned_in` | Roster version the id was first assigned in (`v8`). |
| `rule` | Which slug rule produced it: `family name first`, `mononym`, `written order (...)`, `... + suffix last`, or `override: <reason>`. |
| `note` | Clash notes or other remarks. |

### 2.6 `data/roster/id_overrides.csv` (hand-maintained input)

| column | meaning |
|---|---|
| `canonical_name` | Roster name. |
| `id` | Id to use instead of the slug rule. |
| `reason` | Why the rule would be wrong (e.g. `family name written first`). |

### 2.7 `data/roster/status_overrides.csv` (hand-maintained input)

Statuses set by a recorded decision. `rebuild_roster.py` applies them in place of the v7.1 carry-over and writes the decision into the person's `notes`. A name that isn't in the raw lists stops the rebuild.

| column | meaning |
|---|---|
| `name` | A roster name (any formatting; keyed the same way as the lists). |
| `status` | The status to set (`core`, `provisional`, `review`). |
| `decision` | OPEN_DECISIONS item id (e.g. `R1`). |
| `decided_on` | Date of the decision (YYYY-MM-DD). |
| `reason` | Why. Required. |

### 2.8 `data/sources/`

Raw inputs, read-only, with checksums. See `data/sources/README.md`.

## 3. Person records

A person record is `people/<shard>/<id>.md`. It has a YAML front-matter block that follows `schema/person.schema.json`, then a Markdown body. The body must contain these `##` sections, in any order: Summary, Contribution and impact, Childhood and education, Adult working worldview, Heritage (context only), Timing, Lane B notes (labeled belief model), Open questions, Research log. The template also has an optional "Life and work" section.

Front-matter sections, in file order:

| section | what it holds | lane |
|---|---|---|
| `record` | version, review status, who collected it, change log | — |
| `identity` | id, names, copy of the roster row (checked) | A |
| `basics` | birth/death, first lasting contribution year, era, regions, sex as recorded, languages, occupations | A |
| `contribution` | lasting original contributions, impact evidence, works, honours, definition fit | A |
| `childhood` | family religion and practice, household, schooling, early mathematics and geometric reasoning, early science, reading, mentors | A (read by B) |
| `worldview` | adult working worldview: affiliations, own words, system codes, LIO axes, mid-basin, verbatim statements | A |
| `heritage` | ethnic and religious heritage by birth: context only | context |
| `timing` | major work period, ages, when LIO-type views appear relative to the major work | A (read by B) |
| `lane_b` | geometric form, circle, H1 reading: labeled belief model | B |
| `institutions`, `collaborators` | employers, societies, teachers, collaborators (roster links checked) | A |
| `review` | status reason, controversies, data-quality flags, open questions | — |
| `sources` | every source cited, with type, kind, full citation, URL, access date, reliability note | — |

### 3.1 Person fields (generated)

<!-- BEGIN GENERATED: person -->

#### `record`

Bookkeeping for this file: version, review state, who collected it, change history.

| field | type / allowed values | required | meaning |
|---|---|---|---|
| `record` | object | yes |  |
| `record.record_type` | fixed: `person` | yes | Fixed: tells the validator which schema applies. |
| `record.schema_version` | fixed: `1.2` | yes | Version of the schema this file was written against. Bump in the schema and in every file together. 1.1 (2026-10-01): descriptions updated for decisions P1-P5 and S3-S4; no field or enum changes. 1.2 (2026-10-02): decision P8 adds basis recorded_interview (ceiling 0.7) and statement kind 'recorded interview'. |
| `record.record_version` | integer | yes | Integer, starts at 1. Add 1 every time the file's content changes in a commit. |
| `record.review_status` | one of: `stub`, `example — unreviewed`, `draft — unreviewed`, `in review`, `reviewed`, `needs revision` | yes | Where the file is in review. Only a named human reviewer may set 'reviewed', with reviewed_by and reviewed_on (decision P5). Agents set only 'draft — unreviewed' or 'example — unreviewed' ('stub' for generated stubs). 'example — unreviewed' marks the worked examples. |
| `record.collected_by` | string | yes | who ran the collection (person or agent) |
| `record.model_used` | string | yes | model and version used, or 'none (human)' |
| `record.collected_on` | string | yes | Date (YYYY-MM-DD) the first research run started. |
| `record.last_updated` | string | yes | Date of the latest content change. Must match the newest change_log entry. |
| `record.reviewed_by` | string |  | Name of the human reviewer. Required when review_status is 'reviewed'. |
| `record.reviewed_on` | string |  | Date of the review. Required when review_status is 'reviewed'. |
| `record.change_log` | list of `changeLogEntry` | yes | One entry per content change, oldest first: date, who, and a one-line summary. |

#### `identity`

Who this record is about and how they appear in the roster.

| field | type / allowed values | required | meaning |
|---|---|---|---|
| `identity` | object | yes |  |
| `identity.id` | string | yes | Person id from data/roster/person_ids.csv (lowercase ascii, family name first). Must equal the file name. Frozen once the file exists. |
| `identity.display_name` | string | yes | Name used in tables and prose. Usually the roster canonical_name. |
| `identity.roster` | object | yes | copy of this person's roster.csv row; the validator checks every value matches |
| `identity.roster.canonical_name` | string | yes | roster.csv canonical_name. |
| `identity.roster.rank` | integer | yes | roster.csv rank (row order in the roster; not a quality ranking). |
| `identity.roster.F` | integer | yes | roster.csv F: how many of the five model lists named this person (1-5). |
| `identity.roster.models` | list of one of: `Claude`, `DeepSeek`, `Gemini`, `GPT`, `Grok` | yes | roster.csv models: which of the five lists named the person. |
| `identity.roster.band` | string | yes | roster.csv band: frequency band derived from F. |
| `identity.roster.status` | string | yes | roster.csv status: core / provisional / review / new — needs status / needs status (blank in v7). |
| `identity.roster.field` | string | yes | roster.csv field (majority field across the model lists). |
| `identity.roster.field_bucket` | string | yes | roster.csv field_bucket (field grouped into ~20 buckets). |
| `identity.full_name` | claim; value string | yes | Full name as given in a reliable source, with titles removed. |
| `identity.native_name` | claim; value string | yes | Name in the person's own language and script, if different from display_name. |
| `identity.aliases` | list of object | yes | Other names: roster aliases, birth names, Latinized forms, transliterations, titles. |
| `identity.aliases[].name` | string | yes | The alternative name, spelled as in the source. |
| `identity.aliases[].kind` | one of: `roster alias`, `birth name`, `latinized`, `transliteration`, `title or honorific`, `pen or art name`, `religious name`, `other` | yes | What kind of alternative name this is. |
| `identity.aliases[].cites` | list of `citation` |  | Optional citation for the alias. Roster aliases need none. |

#### `basics`

Dates, places, era and region: the descriptive frame for era- and region-matched baselines.

| field | type / allowed values | required | meaning |
|---|---|---|---|
| `basics` | object | yes |  |
| `basics.birth` | object | yes | Birth date and place. |
| `basics.birth.date` | claim; value string; extra keys: `approx`, `calendar` | yes | Birth date. Record the calendar if the source gives an Old Style date. |
| `basics.birth.place` | claim; value string; extra keys: `modern_name`, `polity_then` | yes | Birth place as named at the time, with modern_name and polity_then where useful. |
| `basics.death` | object | yes | Death date and place. For a living person use UNKNOWN with how_known 'living as of <date>'. |
| `basics.death.date` | claim; value string; extra keys: `approx`, `calendar` | yes | Death date. |
| `basics.death.place` | claim; value string; extra keys: `modern_name`, `polity_then` | yes | Death place. |
| `basics.first_lasting_contribution_year` | claim; value integer; extra keys: `approx` | yes | Year of the earliest contribution listed in contribution.lasting_original_contributions; a contribution dated as a range counts from its start year (decisions P12, P13). Drives era_bucket. |
| `basics.era_bucket` | claim; value one of: `before -500`, `-500 to 499`, `500 to 1399`, `1400 to 1599`, `1600 to 1749`, `1750 to 1849`, `1850 to 1949`, `1950 on` | yes | Bucket of first_lasting_contribution_year (decision P2). A year on an edge goes to the later bucket (1950 is '1950 on'). Birth year stays in basics.birth.date, so a birth-year version can be computed for a sensitivity check. |
| `basics.region_of_birth` | claim; value one of: `Northern Europe`, `Western Europe`, `Southern Europe`, `Eastern Europe`, `Middle East and North Africa`, `Sub-Saharan Africa`, `Central Asia`, `South Asia`, `East Asia`, `Southeast Asia`, `North America`, `Latin America and Caribbean`, `Oceania` | yes | Macro-region of the birth place, on modern borders, from data/reference/regions.csv (decision P3: UN M49 sub-regions; MENA = Northern Africa + Western Asia + Iran). |
| `basics.region_of_work` | claim; value one of: `Northern Europe`, `Western Europe`, `Southern Europe`, `Eastern Europe`, `Middle East and North Africa`, `Sub-Saharan Africa`, `Central Asia`, `South Asia`, `East Asia`, `Southeast Asia`, `North America`, `Latin America and Caribbean`, `Oceania` | yes | Macro-region where the major work was done. If split, pick where the main contribution was made and explain in note. |
| `basics.sex_as_recorded` | claim; value string | yes | Sex as recorded in the sources. Descriptive, for baseline matching only. |
| `basics.languages_of_work` | claim; value list | yes | Languages the person published or worked in. |
| `basics.occupations` | claim; value list | yes | Occupations held, in the words of the sources (e.g. bookbinder's apprentice, chemical assistant, professor). |

#### `contribution`

What the person did that earns a place on the roster (Lane A definition: lasting original impact).

| field | type / allowed values | required | meaning |
|---|---|---|---|
| `contribution` | object | yes |  |
| `contribution.fields` | claim; value list | yes | Fields of work, in the sources' terms. |
| `contribution.lasting_original_contributions` | list of claims (claim; value string; extra keys: `year`, `kind`, `lasting`) | yes | Each original contribution that is still used or built on, with year, kind, and what rests on it now. |
| `contribution.evidence_of_impact` | list of claims (claim; value string; extra keys: `kind`) | yes | Evidence that the impact is lasting: named laws or units, textbook canon, assessments by later major figures, honours. |
| `contribution.major_works` | list of claims (claim; value string; extra keys: `year`, `kind`) | yes | Main published works, lecture series, artworks or devices, with year. |
| `contribution.honours` | list of claims (claim; value string; extra keys: `year`, `years`, `age`, `kind`, `role`, `name`) | yes | Honours, prizes, fellowships, offices; note any declined. |
| `contribution.definition_fit` | claim; value one of: `clearly meets`, `arguable`, `does not meet`; extra keys: `rationale` | yes | Lane A: lasting original impact on documented criteria (not mastery without originality, transient fame, collectives). |

#### `childhood`

Childhood and education up to the start of independent work. Lane A facts; Lane B's H1 test reads them.

| field | type / allowed values | required | meaning |
|---|---|---|---|
| `childhood` | object | yes |  |
| `childhood.family_religion` | claim; value string | yes | Religion of the household the person grew up in (denomination, congregation). |
| `childhood.family_religious_practice` | claim; value string | yes | How the family practised: attendance, observance, offices held. |
| `childhood.parents_and_household` | list of claims (claim; value string; extra keys: `year`, `years`, `age`, `kind`, `role`, `name`) | yes | Parents, siblings and household members, with occupations. |
| `childhood.household_circumstances` | claim; value string | yes | Economic and social situation of the household. |
| `childhood.schooling` | list of claims (claim; value string; extra keys: `stage`, `institution`, `years`, `ages`) | yes | Each stage of formal or informal education, with stage, institution, years and ages. |
| `childhood.early_mathematics` | claim; value one of: `none known`, `arithmetic only`, `basic algebra`, `geometry (Euclid-style proof)`, `advanced mathematics`, `other`; extra keys: `ages`, `description` | yes | Highest level of mathematics met before about age 18, with ages and description. |
| `childhood.early_geometric_style_reasoning` | claim; value string | yes | Any documented early exposure to definition-to-consequence reasoning (Euclid, formal logic, proof). Facts only; Lane B interpretation goes in lane_b. |
| `childhood.early_science_exposure` | list of claims (claim; value string; extra keys: `year`, `age`) | yes | Lectures, books, experiments or apprenticeships with scientific content before independent work. |
| `childhood.key_early_reading` | list of claims (claim; value string; extra keys: `year`, `years`, `age`, `kind`, `role`, `name`) | yes | Books the sources say mattered in childhood or adolescence. |
| `childhood.childhood_mentors` | list of claims (claim; value string; extra keys: `year`, `years`, `age`, `kind`, `role`, `name`) | yes | Adults outside the family who taught or encouraged the person. |
| `childhood.languages_in_childhood` | claim; value list | yes | Languages spoken or learned in childhood. |
| `childhood.notable_events` | list of claims (claim; value string; extra keys: `year`, `age`) | yes | Other events in childhood the sources treat as formative. |

#### `worldview`

The adult working worldview: the unit of coding. Not childhood religion, not heritage.

| field | type / allowed values | required | meaning |
|---|---|---|---|
| `worldview` | object | yes |  |
| `worldview.unit` | fixed: `adult working worldview` | yes | Fixed reminder of the unit of coding. |
| `worldview.working_years` | claim; value string | yes | Years of the adult working life the coding refers to (e.g. 1820-1860). |
| `worldview.nominal_affiliations` | list of claims (claim; value string; extra keys: `year`, `years`, `age`, `kind`, `role`, `name`) | yes | Memberships and affiliations (church, synagogue, society), with years and offices. Membership is not ideology. |
| `worldview.self_described_science_religion_relation` | claim; value string | yes | How the person said science and religion relate, in their own words where possible. |
| `worldview.primary_system` | claim; value string; extra keys: `basis`, `rationale` | yes | Dominant working metaphysics, as one of the 77 system codes. Needs basis; certainty may not exceed the basis ceiling, and is at most 0.7 if the record names a plausible alternative code (CODING_GUIDE §3). |
| `worldview.secondary_system` | claim; value string; extra keys: `basis`, `rationale` | yes | Only if the person published in two systems. Otherwise leave TODO, or UNKNOWN with how_known 'no second system'. |
| `worldview.candidate_codes_considered` | list of `candidateCode` | yes | Codes the coder weighed, with the reason for and against each. Fill this even when the code is still TODO. |
| `worldview.lio_axes` | object | yes | Position on the five LIO axes (0-4 scale, decision P1). Each score needs basis, certainty, cites and a rationale. |
| `worldview.lio_axes.A_locus` | claim; value integer 0–4; extra keys: `basis`, `rationale` | yes | A Locus: transcendent person outside the world (0) ... immanent in or identical with the world (4). |
| `worldview.lio_axes.B_cause` | claim; value integer 0–4; extra keys: `basis`, `rationale` | yes | B Cause: miracle, petition, reserved exemption (0) ... law, regularity, no special cases (4). |
| `worldview.lio_axes.C_ledger` | claim; value integer 0–4; extra keys: `basis`, `rationale` | yes | C Ledger: reward and punishment of persons (0) ... impersonal consequence, or none (4). |
| `worldview.lio_axes.D_authority` | claim; value integer 0–4; extra keys: `basis`, `rationale` | yes | D Authority: revelation outranks observation (0) ... observation and reason outrank revelation (4). |
| `worldview.lio_axes.E_scope` | claim; value integer 0–4; extra keys: `basis`, `rationale` | yes | E Scope: hidden exceptions for an in-group (0) ... same rules for stars, insects, humans (4). Scored on the world's order: the same rules for every kind of being and event, and no hidden in-group exceptions in this-world events (fortune, protection, answered petition, miracles for the favoured). Salvation, reward and punishment, and moral-community scope are scored on C_ledger, not here (decision P7, 2026-10-02). |
| `worldview.mid_basin` | claim; value boolean; extra keys: `rationale` | yes | v7.1 'mid-basin theist', by the test of decision P4 (2026-10-01): true when lio_axes A_locus <= 1 and B_cause >= 3, B scored on the person's account of nature (decision P6, 2026-10-02), both at certainty >= 0.7; false when A_locus >= 3, or A_locus <= 1 with B_cause <= 1; otherwise TODO (a needed axis is TODO, or both are scored at >= 0.7 but fall between the branches: A_locus = 2, or A_locus <= 1 with B_cause = 2), UNKNOWN (only if a needed axis is UNKNOWN) or BELOW_THRESHOLD (a needed axis is BELOW_THRESHOLD or scored only at 0.5). Deists usually pass (see METHOD). 'First-rank' is F >= 3, applied separately. TODO until the axes are scored. |
| `worldview.statements` | list of `quote` | yes | Verbatim quotations that bear on the worldview, each with citation, context, kind, axes touched, and how it was verified. |
| `worldview.changes_over_life` | list of claims (claim; value string; extra keys: `year`, `age`) | yes | Documented shifts in worldview, with year or age. |
| `worldview.coder_notes` | string |  | Free text: reasoning, doubts, what would change the coding. |

#### `heritage`

Ethnic, communal and religious heritage by birth. Context only: never an outcome and never a worldview code.

| field | type / allowed values | required | meaning |
|---|---|---|---|
| `heritage` | object | yes |  |
| `heritage.use` | fixed: `context only — never an outcome and never a worldview code` | yes | Fixed reminder: heritage is context only. |
| `heritage.ethnic_or_communal_heritage` | claim; value string | yes | Ethnic or communal background as the sources describe it. |
| `heritage.religious_heritage_by_birth` | claim; value string | yes | Religion of birth family (may differ from the household practice in childhood). |
| `heritage.baptism_or_initiation` | claim; value string | yes | Baptism, circumcision, bar mitzvah or other rite, with date if known. |
| `heritage.childhood_catechism` | claim; value string | yes | Religious instruction received as a child. |

#### `timing`

When things happened relative to each other. Lane A facts; Lane B's H1 timing test reads them.

| field | type / allowed values | required | meaning |
|---|---|---|---|
| `timing` | object | yes |  |
| `timing.lane` | fixed: `A — descriptive facts; Lane B's H1 timing test reads them` | yes | Fixed reminder of which lane these fields belong to. |
| `timing.major_work_period` | claim; value string | yes | Years of the main contribution (e.g. 1831-1855). |
| `timing.age_at_first_lasting_contribution` | claim; value integer | yes | Age in the year of first_lasting_contribution_year. |
| `timing.first_evidence_of_lio_type_views` | claim; value string; extra keys: `year`, `age` | yes | Earliest dated evidence of lawful-order views (law without exemption), with year and age. |
| `timing.lio_views_relative_to_major_work` | claim; value one of: `held from childhood`, `before major work`, `during major work`, `after major work`, `no LIO-type views found`, `unclear`; extra keys: `rationale` | yes | Whether LIO-type views are documented before, during or after the major work. |
| `timing.worldview_during_major_work` | claim; value string | yes | Worldview as documented during the major work period, in one to three sentences. |

#### `lane_b`

Lane B: the labeled belief model. Values here are inputs to a model that can fail, not findings.

| field | type / allowed values | required | meaning |
|---|---|---|---|
| `lane_b` | object | yes |  |
| `lane_b.label` | fixed: `Lane B — labeled belief model, not a finding` | yes | Fixed reminder that Lane B is a belief model. |
| `lane_b.geometric_form_present` | claim; value one of: `yes`, `partly`, `no`, `unclear`; extra keys: `rationale` | yes | did the person practise definition-to-consequence form without a reserved clause |
| `lane_b.form_acquired` | claim; value one of: `childhood or adolescence`, `adulthood, before major work`, `through the profession`, `unclear`; extra keys: `rationale` | yes | When the geometric form was acquired. |
| `lane_b.circle_present` | claim; value one of: `yes`, `partly`, `no`, `unclear`; extra keys: `rationale` | yes | the PANT circle (entity in Nature, Nature in entity), as distinct from form alone |
| `lane_b.reading` | string |  | what this case means for H1, stated as belief |
| `lane_b.notes` | string |  | Free text. |

#### `institutions`

Employers, societies, patrons, religious bodies and universities, with role, years and kind.

| field | type / allowed values | required | meaning |
|---|---|---|---|
| `institutions` | list of claims (claim; value string; extra keys: `role`, `years`, `kind`) | yes |  |

#### `collaborators`

Teachers, mentors, collaborators, students, rivals and correspondents. roster_id links to another roster person and is checked.

| field | type / allowed values | required | meaning |
|---|---|---|---|
| `collaborators` | list of claims (claim; value string; extra keys: `roster_id`, `relation`, `years`) | yes |  |

#### `review`

Data quality notes and open questions for the reviewer.

| field | type / allowed values | required | meaning |
|---|---|---|---|
| `review` | object | yes |  |
| `review.roster_status_reason` | claim; value string | yes | Why the roster status (core / provisional / review) fits or does not fit this person, with evidence. |
| `review.controversies` | list of claims (claim; value string; extra keys: `year`, `years`, `age`, `kind`, `role`, `name`) | yes | Disputed claims about the person (priority disputes, contested biography), each cited. |
| `review.data_quality_flags` | list of string | yes | Plain statements of conflicts between sources, doubtful dates, or anything a reader should distrust. |
| `review.open_questions` | list of string | yes | Questions this run could not settle, phrased so the next run can act on them. |

#### `sources`

Every source cited in this file. Ids are S1, S2, ... and are local to the file. Every source must be cited somewhere, and every citation must point here.

| field | type / allowed values | required | meaning |
|---|---|---|---|
| `sources` | list of `source` | yes |  |

#### Shared person building blocks

Object types referenced above. Claim types share the claim keys (`value`, `certainty`, `cites`, `how_known`, `note`, `alternatives`) and add the extra keys listed.

| type | field | type / allowed values | required | meaning |
|---|---|---|---|---|
| `sentinel` | | one of: `TODO`, `UNKNOWN`, `BELOW_THRESHOLD` | | TODO = not researched yet. UNKNOWN = researched, no reliable source gives it (say what was checked in how_known). BELOW_THRESHOLD = some evidence, but under certainty 0.5, so the value is withheld (describe the evidence in note). |
| `certainty` | | one of: `1.0`, `0.7`, `0.5` | | See docs/CODING_GUIDE.md. Worldview claims: 1.0 written profession, 0.7 consistent private letters, 0.5 scholarly reconstruction. Other facts: 1.0 established, 0.7 probable, 0.5 contested. Below 0.5: withhold the value (BELOW_THRESHOLD). |
| `isoDate` | | string | | YYYY-MM-DD. |
| `citation` | | object | |  |
| | `source` | string | yes | id of an entry in the sources list |
| | `locator` | string | yes | page, folio, section, letter number, paragraph, or URL anchor |
| | `note` | string |  | Optional remark (e.g. 'quoting the 1844 letter'). |
| `cites` | | list of `citation` | |  |
| `alternative` | | object | | A competing value from another source, with its citation. |
| | `value` | any | yes | The competing value. |
| | `cites` | list of `citation` | yes | Citation for the competing value. |
| | `note` | string |  | Why it differs, or why it was not preferred. |
| `basis` | | one of: `written_profession`, `consistent_private_letters`, `recorded_interview`, `scholarly_reconstruction` | | Evidence basis for a worldview claim. Sets the certainty ceiling: written_profession 1.0, consistent_private_letters 0.7, recorded_interview 0.7 (the person's own first-person words in a recorded or transcribed interview, decision P8), scholarly_reconstruction 0.5. Certainty may sit below the ceiling (e.g. at most 0.7 when the record names a plausible alternative score; CODING_GUIDE §3), never above it. |
| `lioScore` | | integer | | 0-4 ordinal scale (decision P1, 2026-10-01): 0 interventionist pole, 1 leans interventionist, 2 mixed, 3 leans LIO, 4 LIO pole. Certainty is recorded separately. |
| `source` | | object | |  |
| | `id` | string | yes | S1, S2, ... local to the file. |
| | `type` | one of: `primary`, `secondary`, `tertiary` | yes | primary = by the subject or contemporary record; secondary = scholarship; tertiary = encyclopedias and reference pages. |
| | `kind` | one of: `letter`, `diary or notebook`, `published work by the subject`, `archive record`, `scholarly edition`, `scholarly book`, `journal article`, `book chapter`, `encyclopedia`, `institutional page`, `database`, `other` | yes | Form of the source. |
| | `citation` | string | yes | full citation, Chicago author-date or notes style |
| | `author` | string |  | Author(s), family name first for the first author. |
| | `year` | integer or string |  | Year of publication or of the document. |
| | `url` | string |  | Stable URL if online. |
| | `archive_url` | string |  | Archived copy (e.g. Wayback Machine) if available. |
| | `accessed` | string |  | Date the online source was read. |
| | `reliability_note` | string |  | Why this source is trusted, and any limits (e.g. 'title only consulted'). |
| | `used_for` | list of string |  | Which sections rely on this source. |
| `changeLogEntry` | | object | |  |
| | `date` | string | yes | YYYY-MM-DD. |
| | `by` | string | yes | Who made the change (person, agent, or script). |
| | `summary` | string | yes | One line. |
| `text` | | claim | |  |
| | `value` | string | yes | The value, or a sentinel (TODO, UNKNOWN, BELOW_THRESHOLD). |
| `int` | | claim | |  |
| | `value` | integer | yes | The value, or a sentinel (TODO, UNKNOWN, BELOW_THRESHOLD). |
| `bool` | | claim | |  |
| | `value` | boolean | yes | The value, or a sentinel (TODO, UNKNOWN, BELOW_THRESHOLD). |
| `list` | | claim | |  |
| | `value` | list | yes | The value, or a sentinel (TODO, UNKNOWN, BELOW_THRESHOLD). |
| `date` | | claim | | YYYY, YYYY-MM or YYYY-MM-DD; negative year = BCE (astronomical numbering is NOT used: -384 means 384 BCE) |
| | `value` | string | yes | The value, or a sentinel (TODO, UNKNOWN, BELOW_THRESHOLD). |
| | `approx` | boolean |  | True if the source says 'about' or 'c.'. |
| | `calendar` | one of: `gregorian`, `julian`, `other` |  | Calendar of the source date if not Gregorian. |
| `year` | | claim | | negative = BCE |
| | `value` | integer | yes | The value, or a sentinel (TODO, UNKNOWN, BELOW_THRESHOLD). |
| | `approx` | boolean |  | True if approximate. |
| `place` | | claim | |  |
| | `value` | string | yes | The value, or a sentinel (TODO, UNKNOWN, BELOW_THRESHOLD). |
| | `modern_name` | string |  | Modern name and country. |
| | `polity_then` | string |  | State or polity at the time. |
| `era` | | claim | | Buckets on the year of the first lasting contribution (decision P2, 2026-10-01). Each bucket includes its lower edge: 1600 is '1600 to 1749', 1950 is '1950 on'. |
| | `value` | one of: `before -500`, `-500 to 499`, `500 to 1399`, `1400 to 1599`, `1600 to 1749`, `1750 to 1849`, `1850 to 1949`, `1950 on` | yes | The value, or a sentinel (TODO, UNKNOWN, BELOW_THRESHOLD). |
| `region` | | claim | | Macro-regions on modern borders (decision P3, 2026-10-01). Country-to-region table: data/reference/regions.csv. |
| | `value` | one of: `Northern Europe`, `Western Europe`, `Southern Europe`, `Eastern Europe`, `Middle East and North Africa`, `Sub-Saharan Africa`, `Central Asia`, `South Asia`, `East Asia`, `Southeast Asia`, `North America`, `Latin America and Caribbean`, `Oceania` | yes | The value, or a sentinel (TODO, UNKNOWN, BELOW_THRESHOLD). |
| `item` | | claim | | generic dated fact; value is the statement |
| | `value` | string | yes | The value, or a sentinel (TODO, UNKNOWN, BELOW_THRESHOLD). |
| | `year` | integer or string |  | Year, if the fact is dated. |
| | `years` | string |  | Range of years. |
| | `age` | integer or string |  | Age at the time. |
| | `kind` | string |  | Free label. |
| | `role` | string |  | Role (for people). |
| | `name` | string |  | Name (for people or books). |
| `contribution` | | claim | |  |
| | `value` | string | yes | The value, or a sentinel (TODO, UNKNOWN, BELOW_THRESHOLD). |
| | `year` | integer or string |  | Year (or range) of the contribution. |
| | `kind` | one of: `discovery`, `theory`, `law or principle`, `invention`, `method`, `work`, `body of work`, `concept or term`, `institution`, `other` |  | Kind of contribution. |
| | `lasting` | string |  | what still uses or rests on it |
| `impact` | | claim | |  |
| | `value` | string | yes | The value, or a sentinel (TODO, UNKNOWN, BELOW_THRESHOLD). |
| | `kind` | one of: `named after them`, `standard textbook canon`, `assessment by a later major figure`, `honours in lifetime`, `institutional or technological lineage`, `scholarly consensus`, `other` |  | Kind of impact evidence. |
| `work` | | claim | |  |
| | `value` | string | yes | The value, or a sentinel (TODO, UNKNOWN, BELOW_THRESHOLD). |
| | `year` | integer or string |  | Year of publication or completion. |
| | `kind` | one of: `book`, `paper or paper series`, `lecture series`, `artwork`, `composition`, `device`, `notebook`, `other` |  | Kind of work. |
| `schooling` | | claim | |  |
| | `value` | string | yes | The value, or a sentinel (TODO, UNKNOWN, BELOW_THRESHOLD). |
| | `stage` | one of: `home`, `dame or charity school`, `religious school`, `grammar or secondary school`, `apprenticeship`, `tutor`, `university`, `self-directed`, `other` |  | Stage of education. |
| | `institution` | string |  | Name of the school, master or university. |
| | `years` | string |  | Years attended. |
| | `ages` | string |  | Ages attended. |
| `mathExposure` | | claim | |  |
| | `value` | one of: `none known`, `arithmetic only`, `basic algebra`, `geometry (Euclid-style proof)`, `advanced mathematics`, `other` | yes | The value, or a sentinel (TODO, UNKNOWN, BELOW_THRESHOLD). |
| | `ages` | string |  | Ages. |
| | `description` | string |  | What was studied and how. |
| `event` | | claim | |  |
| | `value` | string | yes | The value, or a sentinel (TODO, UNKNOWN, BELOW_THRESHOLD). |
| | `year` | integer or string |  | Year of the event. |
| | `age` | integer or string |  | Age at the event. |
| `systemCode` | | claim | | code from systems/ (the 77 abbr codes). Validator checks the code exists and certainty does not exceed the basis ceiling. |
| | `value` | string | yes | The value, or a sentinel (TODO, UNKNOWN, BELOW_THRESHOLD). |
| | `basis` | one of: `written_profession`, `consistent_private_letters`, `recorded_interview`, `scholarly_reconstruction` |  | written_profession (1.0), consistent_private_letters (0.7), recorded_interview (0.7), or scholarly_reconstruction (0.5). |
| | `rationale` | string |  | Why this code, in terms of coding_guidance. |
| `axis` | | claim | |  |
| | `value` | integer 0–4 | yes | The value, or a sentinel (TODO, UNKNOWN, BELOW_THRESHOLD). |
| | `basis` | one of: `written_profession`, `consistent_private_letters`, `recorded_interview`, `scholarly_reconstruction` |  | Evidence basis; certainty may not exceed its ceiling. |
| | `rationale` | string |  | why this score, in terms of the axis poles |
| `quote` | | object | |  |
| | `text` | string | yes | verbatim, with original spelling; mark cuts with [...] |
| | `cites` | list of `citation` | yes | Citations: source id plus locator. |
| | `date` | string |  | Date of the passage (letter date, publication year). |
| | `context` | string |  | addressee / occasion / what the passage is answering |
| | `axes` | list of one of: `A_locus`, `B_cause`, `C_ledger`, `D_authority`, `E_scope` |  |  |
| | `kind` | one of: `written profession (public)`, `private letter`, `notebook or diary`, `recorded interview`, `reported speech`, `other` |  |  |
| | `verified_against` | one of: `primary transcription`, `primary facsimile`, `scholarly edition`, `secondary quotation` | yes |  |
| | `verified_on` | string | yes | Date the quotation was checked against the source. |
| | `note` | string |  | Free remark. |
| `institution` | | claim | |  |
| | `value` | string | yes | The value, or a sentinel (TODO, UNKNOWN, BELOW_THRESHOLD). |
| | `role` | string |  | Role held. |
| | `years` | string |  | Years. |
| | `kind` | one of: `employer`, `patron or funder`, `academy or learned society`, `religious body`, `university`, `government or state body`, `commercial`, `other` |  | Kind of institution. |
| `collaborator` | | claim | |  |
| | `value` | string | yes | The value, or a sentinel (TODO, UNKNOWN, BELOW_THRESHOLD). |
| | `roster_id` | string |  | Person id if this person is on the roster (checked against person_ids.csv). |
| | `relation` | one of: `teacher`, `mentor or employer`, `collaborator`, `student or assistant`, `rival or critic`, `correspondent`, `influenced by`, `influenced`, `family`, `other` |  | Relation to the subject. |
| | `years` | string |  | Years of the relationship. |
| `candidateCode` | | object | |  |
| | `code` | string | yes | A system code from systems/. |
| | `reason` | string | yes | Why it is a candidate, and what argues against it. |
| | `cites` | list of `citation` |  | Citations behind the reason. |

<!-- END GENERATED: person -->

## 4. System records

A system record is `systems/<CODE>.md`, where the code is the v7.1 abbreviation (e.g. `PANT`, `CLASS_THEISM`). It has YAML front matter following `schema/system.schema.json`, then a body with these `##` sections: Summary, Core metaphysics, Position on the LIO axes, Schools and variants, Science, Coding guidance, v7.1 scoring note, Open questions, Research log.

Front-matter sections:

| section | what it holds |
|---|---|
| `record` | as for persons |
| `identity` | code, v7.1 number and label (verbatim), display label and its approval status, aliases |
| `classification` | kind, family, parent traditions, related codes with relation type |
| `origins` | founding era and region, founders or key figures, key texts |
| `metaphysics` | ten stance claims (God–nature relation, personal deity, intervention, miracles, petition, afterlife, moral ledger, authority, reserved exemptions, teleology), plus necessity and freedom |
| `lio_axes` | five axis positions with rationale (0–4 scale, decision P1) |
| `epistemology`, `ethics` | one claim each |
| `practice` | ritual and practice, community form |
| `science` | historical and current stance on natural science |
| `schools_and_variants` | internal schools and forms (scholastic / popular / mystical / modern ...), with how each moves on the LIO axes |
| `adherents` | estimate, context only, never a denominator |
| `v7_1_rubric` | authorial v7.1 scores L, P, E, V, X, total, and verbatim scoring note, checked against the data book |
| `revised_rubric` | slot for revised scores with per-axis rationale |
| `coding_guidance` | when to use the code, when not, neighbors |
| `review`, `sources` | as for persons |

The v7.1 rubric is described in the data book as an "Authorial five-axis rubric. Axes: logical self-consistency, resolution of known paradoxes, direct empirical compatibility, evidence vs revelation authority, predictive/explanatory success. Each 0–10. Total / 50. This is a map of official schemas, not a population parameter and not an IQ test." Its column key reads: "L logical consistency · P paradox resolution · E empirical compatibility · V evidence vs revelation · X predictive/explanatory success."

### 4.1 System fields (generated)

<!-- BEGIN GENERATED: system -->

#### `record`

Bookkeeping for this file: version, review state, who collected it, change history.

| field | type / allowed values | required | meaning |
|---|---|---|---|
| `record` | object | yes |  |
| `record.record_type` | fixed: `system` | yes | Fixed: tells the validator which schema applies. |
| `record.schema_version` | fixed: `1.1` | yes | Version of the schema this file was written against. Bump in the schema and in every file together. 1.1 (2026-10-01): descriptions updated for decisions P1, P5, S3, S4 and S5; no field or enum changes. |
| `record.record_version` | integer | yes | Integer, starts at 1. Add 1 every time the file's content changes in a commit. |
| `record.review_status` | one of: `stub`, `example — unreviewed`, `draft — unreviewed`, `in review`, `reviewed`, `needs revision` | yes | Where the file is in review. Only a named human reviewer may set 'reviewed', with reviewed_by and reviewed_on (decision P5). Agents set only 'draft — unreviewed' or 'example — unreviewed' ('stub' for generated stubs). 'example — unreviewed' marks the worked examples. |
| `record.collected_by` | string | yes | who ran the collection (person or agent) |
| `record.model_used` | string | yes | model and version used, or 'none (human)' |
| `record.collected_on` | string | yes | Date (YYYY-MM-DD) the first research run started. |
| `record.last_updated` | string | yes | Date of the latest content change. Must match the newest change_log entry. |
| `record.reviewed_by` | string |  | Name of the human reviewer. Required when review_status is 'reviewed'. |
| `record.reviewed_on` | string |  | Date of the review. Required when review_status is 'reviewed'. |
| `record.change_log` | list of `changeLogEntry` | yes | One entry per content change, oldest first: date, who, and a one-line summary. |

#### `identity`

Code, v7.1 label, display label and aliases.

| field | type / allowed values | required | meaning |
|---|---|---|---|
| `identity` | object | yes |  |
| `identity.id` | string | yes | The v7.1 abbreviation code (e.g. PANT, CLASS_THEISM). Must equal the file name. One of the 77. The list is closed for v8 (decision S4): proposed new codes are collected in a list (code, why, example people, and for a split the people it would move) and added in one batch with one schema bump and Jason's approval. |
| `identity.v7_1_number` | integer | yes | Row number (#) in the v7.1 data book rubric table. |
| `identity.v7_1_label` | string | yes | System name exactly as in the data book section 7 scoring note, or the section 6 score table (tables[4]) if the note has none. Never edited. |
| `identity.display_label` | string | yes | label used in v8 tables |
| `identity.label_status` | one of: `as in v7.1`, `proposed — pending Jason's OK`, `approved` | yes |  |
| `identity.aliases` | list of string | yes | Other names for the system, including names used in the sources. |

#### `classification`

What kind of thing the system is and how it relates to the other codes.

| field | type / allowed values | required | meaning |
|---|---|---|---|
| `classification` | object | yes |  |
| `classification.kind` | claim; value one of: `religion`, `philosophical school or method`, `metaphysical thesis`, `ethical or civic movement`, `epistemic stance`, `esoteric or occult tradition`, `new religious movement`, `indigenous or traditional religion`, `reconstructionist religion`, `family of positions` | yes | e.g. organized religion, philosophical school, family of positions, metaphysical stance, movement. |
| `classification.family` | claim; value string | yes | The larger family it belongs to (e.g. Abrahamic monotheism; monism; Indian dharmic traditions). |
| `classification.parent_traditions` | claim; value list | yes | Traditions it grew out of. |
| `classification.related_codes` | list of `relatedCode` | yes | Other codes among the 77 and how they relate (scholastic form of, popular form of, neighbor, offshoot, ...). |

#### `origins`

When, where and from whom the system came.

| field | type / allowed values | required | meaning |
|---|---|---|---|
| `origins` | object | yes |  |
| `origins.founding_era` | claim; value string | yes | Era of origin, with dates where the sources give them. |
| `origins.founding_region` | claim; value string | yes | Region of origin. |
| `origins.founders_or_key_figures` | claim; value list | yes | Founders, or the key figures if there is no single founder. |
| `origins.key_texts` | list of claims (claim; value string; extra keys: `year`, `author`) | yes | Foundational and authoritative texts, with author and year. |

#### `metaphysics`

Core metaphysics. Each item: value (one to three sentences) plus a short stance label from the allowed list.

| field | type / allowed values | required | meaning |
|---|---|---|---|
| `metaphysics` | object | yes |  |
| `metaphysics.god_nature_relation` | claim; value string; extra keys: `stance` | yes |  value = the position in one to three sentences; stance = short label from the list |
| `metaphysics.deity_personal` | claim; value string; extra keys: `stance` | yes |  value = the position in one to three sentences; stance = short label from the list |
| `metaphysics.intervention` | claim; value string; extra keys: `stance` | yes |  value = the position in one to three sentences; stance = short label from the list |
| `metaphysics.miracles` | claim; value string; extra keys: `stance` | yes |  value = the position in one to three sentences; stance = short label from the list |
| `metaphysics.petition_and_prayer` | claim; value string; extra keys: `stance` | yes |  value = the position in one to three sentences; stance = short label from the list |
| `metaphysics.afterlife` | claim; value string; extra keys: `stance` | yes |  value = the position in one to three sentences; stance = short label from the list |
| `metaphysics.moral_ledger` | claim; value string; extra keys: `stance` | yes |  value = the position in one to three sentences; stance = short label from the list |
| `metaphysics.authority` | claim; value string; extra keys: `stance` | yes |  value = the position in one to three sentences; stance = short label from the list |
| `metaphysics.reserved_exemptions` | claim; value string; extra keys: `stance` | yes |  value = the position in one to three sentences; stance = short label from the list |
| `metaphysics.teleology_in_nature` | claim; value string; extra keys: `stance` | yes |  value = the position in one to three sentences; stance = short label from the list |
| `metaphysics.necessity_and_freedom` | claim; value string | yes | Determinism, free will, fate, necessity. |

#### `lio_axes`

Position on the five LIO axes (0-4 scale, decision P1), for the system's official or scholarly form. Variants that differ are described in schools_and_variants.

| field | type / allowed values | required | meaning |
|---|---|---|---|
| `lio_axes` | object | yes |  |
| `lio_axes.A_locus` | claim; value integer 0–4; extra keys: `rationale` | yes | A Locus: transcendent person outside the world (0) ... immanent in or identical with the world (4). |
| `lio_axes.B_cause` | claim; value integer 0–4; extra keys: `rationale` | yes | B Cause: miracle, petition, reserved exemption (0) ... law, regularity, no special cases (4). |
| `lio_axes.C_ledger` | claim; value integer 0–4; extra keys: `rationale` | yes | C Ledger: reward and punishment of persons (0) ... impersonal consequence, or none (4). |
| `lio_axes.D_authority` | claim; value integer 0–4; extra keys: `rationale` | yes | D Authority: revelation outranks observation (0) ... observation and reason outrank revelation (4). |
| `lio_axes.E_scope` | claim; value integer 0–4; extra keys: `rationale` | yes | E Scope: hidden exceptions for an in-group (0) ... same rules for stars, insects, humans (4). Scored on the world's order: the same rules for every kind of being and event, and no hidden in-group exceptions in this-world events (fortune, protection, answered petition, miracles for the favoured). Salvation, reward and punishment, and moral-community scope are scored on C_ledger, not here (decision P7, 2026-10-02). |

#### `epistemology`

How the system says knowledge is gained and checked.

| field | type / allowed values | required | meaning |
|---|---|---|---|
| `epistemology` | claim; value string | yes |  |

#### `ethics`

Core ethical teaching, in one to three sentences.

| field | type / allowed values | required | meaning |
|---|---|---|---|
| `ethics` | claim; value string | yes |  |

#### `practice`

Ritual, practice and community form.

| field | type / allowed values | required | meaning |
|---|---|---|---|
| `practice` | object | yes |  |
| `practice.ritual_and_practice` | claim; value string | yes | Required or typical practices (prayer, worship, meditation, none). |
| `practice.community_form` | claim; value string | yes | Organization: church, sangha, school, informal, none. |

#### `science`

Stance on natural science, historically and now.

| field | type / allowed values | required | meaning |
|---|---|---|---|
| `science` | object | yes |  |
| `science.historical_stance` | claim; value string | yes | Stance on natural inquiry in the periods the roster covers. |
| `science.current_stance` | claim; value string | yes | Stance today (official bodies or leading scholars). |

#### `schools_and_variants`

Internal schools and forms, e.g. a scholarly and a popular form inside one tradition. Say which LIO axes move.

| field | type / allowed values | required | meaning |
|---|---|---|---|
| `schools_and_variants` | list of `variant` | yes |  |

#### `adherents`

Adherent estimate. Context only: never a genius-rate denominator (v7.1 rule: no present-day religion stock as a denominator).

| field | type / allowed values | required | meaning |
|---|---|---|---|
| `adherents` | object | yes |  |
| `adherents.use` | fixed: `context only — never a genius-rate denominator` | yes | Fixed reminder. |
| `adherents.estimate` | claim; value string; extra keys: `year`, `scope` | yes | Estimate with year and scope (world, country), cited. |

#### `v7_1_rubric`

copied from the v7.1 data book; the validator checks it against data/sources/v7_1/neuresthetics_v7_combined.json

| field | type / allowed values | required | meaning |
|---|---|---|---|
| `v7_1_rubric` | object | yes |  |
| `v7_1_rubric.label` | fixed: `authorial v7.1 scores` | yes | Fixed label. |
| `v7_1_rubric.L` | integer | yes | v7.1 axis L: logical self-consistency (0–10, data book wording). |
| `v7_1_rubric.P` | integer | yes | v7.1 axis P: resolution of known paradoxes (0–10, data book wording). |
| `v7_1_rubric.E` | integer | yes | v7.1 axis E: direct empirical compatibility (0–10, data book wording). |
| `v7_1_rubric.V` | integer | yes | v7.1 axis V: evidence vs revelation authority (0–10, data book wording). |
| `v7_1_rubric.X` | integer | yes | v7.1 axis X: predictive/explanatory success (0–10, data book wording). |
| `v7_1_rubric.total` | integer | yes | Sum of L+P+E+V+X as printed in the data book (checked). |
| `v7_1_rubric.scoring_note` | string | yes | verbatim from data book section 7 |
| `v7_1_rubric.source` | string | yes | Where in the data book the scores come from. |

#### `revised_rubric`

Slot for revised scores (decision S3, 2026-10-01). Not started until the first coding pool is done and Jason opens it. Then: a cite for each axis score, two scorers score a sample independently and report agreement before the rest are scored, and Jason approves the final numbers. Revised scores sit beside v7_1_rubric and never overwrite it.

| field | type / allowed values | required | meaning |
|---|---|---|---|
| `revised_rubric` | object | yes |  |
| `revised_rubric.status` | one of: `not started`, `draft`, `reviewed` | yes | not started / draft / reviewed. |
| `revised_rubric.L` | object (`rubricAxis`) | yes | Revised L (logical self-consistency): score 0–10 and rationale. |
| `revised_rubric.L.score` |  | yes | Revised 0-10 score, or TODO. |
| `revised_rubric.L.rationale` | string | yes | Why this score. |
| `revised_rubric.L.cites` | list of `citation` |  | Citations: source id plus locator. |
| `revised_rubric.P` | object (`rubricAxis`) | yes | Revised P (resolution of known paradoxes): score 0–10 and rationale. |
| `revised_rubric.P.score` |  | yes | Revised 0-10 score, or TODO. |
| `revised_rubric.P.rationale` | string | yes | Why this score. |
| `revised_rubric.P.cites` | list of `citation` |  | Citations: source id plus locator. |
| `revised_rubric.E` | object (`rubricAxis`) | yes | Revised E (direct empirical compatibility): score 0–10 and rationale. |
| `revised_rubric.E.score` |  | yes | Revised 0-10 score, or TODO. |
| `revised_rubric.E.rationale` | string | yes | Why this score. |
| `revised_rubric.E.cites` | list of `citation` |  | Citations: source id plus locator. |
| `revised_rubric.V` | object (`rubricAxis`) | yes | Revised V (evidence vs revelation authority): score 0–10 and rationale. |
| `revised_rubric.V.score` |  | yes | Revised 0-10 score, or TODO. |
| `revised_rubric.V.rationale` | string | yes | Why this score. |
| `revised_rubric.V.cites` | list of `citation` |  | Citations: source id plus locator. |
| `revised_rubric.X` | object (`rubricAxis`) | yes | Revised X (predictive/explanatory success): score 0–10 and rationale. |
| `revised_rubric.X.score` |  | yes | Revised 0-10 score, or TODO. |
| `revised_rubric.X.rationale` | string | yes | Why this score. |
| `revised_rubric.X.cites` | list of `citation` |  | Citations: source id plus locator. |
| `revised_rubric.revised_by` | string |  | Who revised. |
| `revised_rubric.revised_on` | string |  | Date of revision. |

#### `coding_guidance`

How to decide whether a person gets this code.

| field | type / allowed values | required | meaning |
|---|---|---|---|
| `coding_guidance` | object | yes |  |
| `coding_guidance.use_when` | string | yes | When to use the code. Where the v7.1 coding rules name the code, the rule is quoted verbatim. |
| `coding_guidance.do_not_use_when` | string | yes | Common mistakes and the code to use instead. |
| `coding_guidance.neighbors` | list of `relatedCode` | yes | Codes easily confused with this one. |

#### `review`

Data quality notes and open questions for the reviewer.

| field | type / allowed values | required | meaning |
|---|---|---|---|
| `review` | object | yes |  |
| `review.data_quality_flags` | list of string | yes | Plain statements of conflicts between sources, doubtful dates, or anything a reader should distrust. |
| `review.open_questions` | list of string | yes | Questions this run could not settle, phrased so the next run can act on them. |

#### `sources`

Every source cited in this file. Ids are S1, S2, ... and are local to the file. Every source must be cited somewhere, and every citation must point here.

| field | type / allowed values | required | meaning |
|---|---|---|---|
| `sources` | list of `source` | yes |  |

#### Shared system building blocks

Object types referenced above. Claim types share the claim keys (`value`, `certainty`, `cites`, `how_known`, `note`, `alternatives`) and add the extra keys listed.

| type | field | type / allowed values | required | meaning |
|---|---|---|---|---|
| `sentinel` | | one of: `TODO`, `UNKNOWN`, `BELOW_THRESHOLD` | | TODO = not researched yet. UNKNOWN = researched, no reliable source gives it (say what was checked in how_known). BELOW_THRESHOLD = some evidence, but under certainty 0.5, so the value is withheld (describe the evidence in note). |
| `certainty` | | one of: `1.0`, `0.7`, `0.5` | | See docs/CODING_GUIDE.md. Worldview claims: 1.0 written profession, 0.7 consistent private letters, 0.5 scholarly reconstruction. Other facts: 1.0 established, 0.7 probable, 0.5 contested. Below 0.5: withhold the value (BELOW_THRESHOLD). |
| `isoDate` | | string | | YYYY-MM-DD. |
| `citation` | | object | |  |
| | `source` | string | yes | id of an entry in the sources list |
| | `locator` | string | yes | page, folio, section, letter number, paragraph, or URL anchor |
| | `note` | string |  | Optional remark (e.g. 'quoting the 1844 letter'). |
| `cites` | | list of `citation` | |  |
| `alternative` | | object | | A competing value from another source, with its citation. |
| | `value` | any | yes | The competing value. |
| | `cites` | list of `citation` | yes | Citation for the competing value. |
| | `note` | string |  | Why it differs, or why it was not preferred. |
| `basis` | | one of: `written_profession`, `consistent_private_letters`, `scholarly_reconstruction` | | Evidence basis for a worldview claim. Sets the certainty ceiling: written_profession 1.0, consistent_private_letters 0.7, scholarly_reconstruction 0.5. Certainty may sit below the ceiling (e.g. at most 0.7 when the record names a plausible alternative score; CODING_GUIDE §3), never above it. |
| `lioScore` | | integer | | 0-4 ordinal scale (decision P1, 2026-10-01): 0 interventionist pole, 1 leans interventionist, 2 mixed, 3 leans LIO, 4 LIO pole. Certainty is recorded separately. |
| `source` | | object | |  |
| | `id` | string | yes | S1, S2, ... local to the file. |
| | `type` | one of: `primary`, `secondary`, `tertiary` | yes | primary = by the subject or contemporary record; secondary = scholarship; tertiary = encyclopedias and reference pages. |
| | `kind` | one of: `letter`, `diary or notebook`, `published work by the subject`, `archive record`, `scholarly edition`, `scholarly book`, `journal article`, `book chapter`, `encyclopedia`, `institutional page`, `database`, `other` | yes | Form of the source. |
| | `citation` | string | yes | full citation, Chicago author-date or notes style |
| | `author` | string |  | Author(s), family name first for the first author. |
| | `year` | integer or string |  | Year of publication or of the document. |
| | `url` | string |  | Stable URL if online. |
| | `archive_url` | string |  | Archived copy (e.g. Wayback Machine) if available. |
| | `accessed` | string |  | Date the online source was read. |
| | `reliability_note` | string |  | Why this source is trusted, and any limits (e.g. 'title only consulted'). |
| | `used_for` | list of string |  | Which sections rely on this source. |
| `changeLogEntry` | | object | |  |
| | `date` | string | yes | YYYY-MM-DD. |
| | `by` | string | yes | Who made the change (person, agent, or script). |
| | `summary` | string | yes | One line. |
| `text` | | claim | |  |
| | `value` | string | yes | The value, or a sentinel (TODO, UNKNOWN, BELOW_THRESHOLD). |
| `list` | | claim | |  |
| | `value` | list | yes | The value, or a sentinel (TODO, UNKNOWN, BELOW_THRESHOLD). |
| `work` | | claim | |  |
| | `value` | string | yes | The value, or a sentinel (TODO, UNKNOWN, BELOW_THRESHOLD). |
| | `year` | integer or string |  | Year of publication or completion. |
| | `author` | string |  | Author of the text. |
| `axis` | | claim | |  |
| | `value` | integer 0–4 | yes | The value, or a sentinel (TODO, UNKNOWN, BELOW_THRESHOLD). |
| | `rationale` | string |  | justification in terms of the axis poles, for the system's official or scholarly form |
| `rubricAxis` | | object | |  |
| | `score` |  | yes | Revised 0-10 score, or TODO. |
| | `rationale` | string | yes | Why this score. |
| | `cites` | list of `citation` |  | Citations: source id plus locator. |
| `variant` | | object | |  |
| | `name` | string | yes | Name of the school or form. |
| | `code` | string |  | if this variant has its own code among the 77 |
| | `form` | one of: `scholastic or philosophical`, `popular`, `mystical`, `reform`, `modern`, `regional`, `other` | yes | Form of the variant. |
| | `how_it_differs` | string | yes | How it differs from the main form. |
| | `lio_difference` | string |  | which LIO axes move, and which way |
| | `certainty` | one of: `1.0`, `0.7`, `0.5` |  | See docs/CODING_GUIDE.md. Worldview claims: 1.0 written profession, 0.7 consistent private letters, 0.5 scholarly reconstruction. Other facts: 1.0 established, 0.7 probable, 0.5 contested. Below 0.5: withhold the value (BELOW_THRESHOLD). |
| | `cites` | list of `citation` |  | Citations: source id plus locator. |
| `relatedCode` | | object | |  |
| | `code` | string | yes | A code among the 77. |
| | `relation` | one of: `parent tradition`, `offshoot`, `scholastic form of`, `popular form of`, `neighbor (easily confused)`, `contrast case`, `overlaps` | yes | Read as: '<code> is <relation> this system'. E.g. in PANT.md, {code: STOIC, relation: 'parent tradition'} means Stoicism is a parent tradition of PANT. CLTHEI and CLASS_THEISM are 'neighbor (easily confused)' to each other (decision S5). |
| | `note` | string |  | Optional remark. |

<!-- END GENERATED: system -->

## 5. Reports

| file | written by | content |
|---|---|---|
| `reports/coverage.md` | `scripts/coverage_report.py` | Person-file coverage by band and bucket, review statuses, fill rates, first-pool checklist, system coverage. |
| `versions/v8/roster_diff_v7_to_v8.md` | `scripts/rebuild_roster.py` | What changed between the v7.1 and v8 rosters and why. |
| `README.md` (progress table only) | `scripts/progress_status.py` | The status table between the `BEGIN/END GENERATED: progress` markers: roster counts, people coded, systems sourced, decisions settled, latest tag. The Audits and Next steps rows are manual constants in the script. `--check` reports whether the table is up to date. |
| `figures/*.png` | `scripts/make_figures.py` | Four descriptive charts: list overlap, core roster by region and field bucket, the coded people on B_cause and A_locus, and the sourced systems on the LIO axes. These are not results. |
