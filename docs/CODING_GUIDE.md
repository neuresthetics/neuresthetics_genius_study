# Coding guide

How to fill person and system records consistently. Part 1 covers people, Part 2 belief systems. The v7.1 coding rules are quoted verbatim. Rules that v8 added were decided by Jason on 2026-10-01 and are tagged with their item in [OPEN_DECISIONS.md](OPEN_DECISIONS.md) (P1, P4, S6 and so on). Field definitions are in [DATA_DICTIONARY.md](DATA_DICTIONARY.md), and the research procedure is in [RUNBOOK.md](RUNBOOK.md).

---

# Part 1: People

## 1. The v7.1 coding rules (verbatim)

From the v7.1 data book, section 5 "Coding rules" (`tables[3]` in the combined JSON). These are binding.

| Rule | Content |
|---|---|
| Unit of coding | Avowed or reconstructable worldview of the adult working years, not childhood religion and not ethnic heritage. |
| Heritage column | Separate. Einstein is PANT + Jewish heritage. Mixing these is what made the published Judaism rate incomparable. |
| Split theisms | CLASS_THEISM (Aristotelian-Thomistic-Falsafa) is not CLTHEI (popular interventionist personal God) and not generic CHRIST/ISLAM/JUDA. |
| Pantheism | Use PANT only for the circle: Deus sive Natura, entity-in-Nature and Nature-in-entity. Not atheism-plus-poetry. Not every nature-mystic. |
| Atheism vs Agnosticism | ATHE = positive naturalism. AGNOS = explicit suspension. SECHUM if the public identity is humanist movement rather than metaphysics. |
| Certainty | 1.0 written profession; 0.7 consistent private letters; 0.5 scholarly reconstruction; <0.5 leave blank and exclude from primary per-capita table. |
| Multiple systems | Primary = dominant working metaphysics. Secondary only if they published in two systems. |
| Founders | Code the system they founded (Buddha → BUDDH) even if later scholastic versions diverge. |
| Scientists with church membership | Church tax / baptism ≠ ideology. Need writings. Faraday and Maxwell pass; many 19th-c names will be CHRIST-nominal / AGNOS-working. |
| Do not code yet | Anyone with certainty <0.5 stays in the roster but drops out of the ideology×rate table. |
| Frequency cut | Primary LIO composition on frequency ≥ 3; sensitivity on ≥ 4 and ≥ 2. Frequency 1 stays on roster, out of primary table. |
| First pool | Physical science 1600–1950; mid-basin theists coded first (Faraday, Maxwell, Newton, Aquinas, Ibn Sina, Gödel). |
| No G/P_2025 | No present-day religion stock as a denominator. |

How the rules map onto fields:

- **Unit of coding** → `worldview.*` describes the adult working years (`worldview.working_years`). Childhood religion goes in `childhood.family_religion`, and ethnic or communal background goes in `heritage.*`. Neither may decide a worldview code.
- **Heritage column** → `heritage.*`, with the fixed reminder "context only — never an outcome and never a worldview code". Einstein would be coded PANT, with Jewish heritage recorded in `heritage`, not in `worldview`.
- **Split theisms** → choose among `CLASS_THEISM`, `CLTHEI`, and `CHRIST`/`ISLAM`/`JUDA` explicitly, and list the ones you rejected in `worldview.candidate_codes_considered` with reasons.
- **Pantheism** → `PANT` only for the circle (see §5).
- **Certainty** → `certainty` together with `basis` on every worldview code and LIO axis score (see §3).
- **Multiple systems** → `primary_system` is the dominant working metaphysics. `secondary_system` is used only if the person published in two systems. Otherwise it stays `TODO`, or `UNKNOWN` with how_known "no second system".
- **Founders** → code the system they founded.
- **Church membership** → membership goes in `worldview.nominal_affiliations`. It is never enough on its own for a code. You need the person's writings.
- **Do not code yet / below 0.5** → `BELOW_THRESHOLD`. The person stays on the roster.
- **Frequency cut, first pool, no G/P_2025** → analysis rules. They govern which people are coded first ([RUNBOOK.md](RUNBOOK.md#1-pick-the-person)) and forbid adherent counts as denominators (systems `adherents.use`).

## 2. Lanes

- **Lane A** (descriptive): `basics`, `contribution`, `childhood`, `worldview`, `timing`, `institutions` and `collaborators` hold facts with sources. Write them so that someone who rejects Lane B can still use them.
- **Lane B** (labeled belief model): only `lane_b.*` and the body section "Lane B notes (labeled belief model)". Lane B language stays out of Lane A fields. Write "geometric form present: yes, because ...". Don't write "this explains the genius".
- **Heritage** is context only.

Glossary (v7.1 data book, section 3 "Dictionary", verbatim):

| Term | Meaning | Lane |
|---|---|---|
| Genius | Lasting original impact on stated achievement criteria. Not an IQ score. | A |
| Frequency | Inter-model consensus after alias merge. Not intensity. | A |
| Core / provisional / review | Definition-fit tags. Review = paradigm-shift bar is arguable. | A |
| Coherence rubric | Five 0–10 axes on official schemas. Authorial. Not hidden IQ. | shared |
| LIO | Lawful immanent order: regular, non-intervening, no personal moral ledger. Pantheism is the circle — entity applied to Nature and Nature rendered in entity. The work is reducing dissonance between mapping and mapped. | shared |
| Heritage | Ethnicity, baptism, childhood catechism. Off the outcome. | shared |
| Working ontology | Adult reconstructable metaphysics of the work. | A/B |
| H1 Cultivation | Early circle (map of out-there, mapping in-there) plus geometric form reduces split-model load. Lane B model. | B |
| H2 Selection | Integrative intelligence independently drops petitionary gods. | open |
| H3 Attractor | World is approximately Spinoza-shaped: one order, modeled out-there, rendered in-there. Accurate maps converge. | open |
| Exception prior | High-precision reserved exemption (miracle, petition). Functionally a second map of the same mapped. | B-N |
| Bottleneck | Scarce integration channel. PCC and callosum are instances. | B-N |
| Geometric method | Definition → consequence, no reserved clause. Makes a mismatch between mapping and mapped expensive. | B |
| Lane A | Public descriptive track. No fertility table. | A |
| Lane B | Belief/cultivation model: the circle, labeled so it can fail. | B |

## 3. Certainty

Every filled claim carries one of three certainty values. Anything below 0.5 is withheld.

**Worldview claims.** This covers `worldview.primary_system`, `secondary_system`, the LIO axes, and statements used as evidence. It uses the v7.1 scale. The `basis` records the evidence type and sets the highest certainty allowed:

| certainty | `basis` | meaning |
|---|---|---|
| 1.0 | `written_profession` | The person stated it in writing for others: a published work, public lecture text, or formal statement of faith. |
| 0.7 | `consistent_private_letters` | Private letters or notebooks, consistent across more than one document. |
| 0.5 | `scholarly_reconstruction` | A scholar's reconstruction from indirect evidence. |
| <0.5 | value = `BELOW_THRESHOLD` | Leave the value blank. The person drops out of the ideology × rate table. |

A single private letter is not "consistent private letters". Use 0.5 if a scholar backs the reading. Otherwise use `BELOW_THRESHOLD`.

**Contested readings** (lens audit, 2026-10-02). If the record itself names a plausible alternative score or code (in a rationale, how_known, candidate list or coder note), certainty is at most 0.7, whatever the source type. Name the alternative in the rationale. Certainty may also sit below the basis ceiling when the evidence speaks to the axis only indirectly; say why in `how_known`. Certainty never goes above the ceiling. This applies to person and system LIO axes and to `primary_system`. `mid_basin` certainty is at most the lower of the A_locus and B_cause certainties. Apply the scale the same way across files: the same pattern of evidence gets the same score (for example, two domains each with its own authority is D 2 for every person).

**Other facts** (dates, places, schooling, contributions):

| certainty | meaning | typical evidence |
|---|---|---|
| 1.0 | established | Primary record, or agreement across independent reliable sources with no known dispute. |
| 0.7 | probable | One reliable source, or sources that agree but depend on each other. |
| 0.5 | contested | Reliable sources disagree. Put the competitors in `alternatives`, each with its own cite. |

Certainty is about the claim, not the source. A signed encyclopedia can support 1.0 for a birth date that nobody disputes. A primary letter can support only 0.7 for a worldview, because it is private.

## 4. Sentinels and empty values

- Never leave a value blank and never write "n/a". Use one of:
  - `TODO`: not researched.
  - `UNKNOWN`: researched, not in any reliable source. `how_known` lists what was checked.
  - `BELOW_THRESHOLD`: evidence exists but is below 0.5. `note` describes it.
- For lists with nothing in them after research (e.g. no known childhood mentors), use `UNKNOWN` with a how_known note, not an empty list.
- `TODO` is fine in a committed file. The record is honest about what is missing, and the coverage report counts it.

## 5. Choosing a worldview code

1. Read the person's own words first (`worldview.statements`). Quote verbatim, with a cite and the context.
2. Fill `worldview.self_described_science_religion_relation` in their words.
3. List every plausible code in `worldview.candidate_codes_considered`, with the reasons for and against each. Do this even if the final code stays `TODO`.
4. Use each candidate system's `coding_guidance` (`systems/<CODE>.md`): `use_when`, `do_not_use_when`, neighbors.
5. Pick `primary_system`. Set `basis` and `certainty` together, and write a `rationale` in terms of the coding guidance.

Hard cases:

- **PANT vs ATHE** (two-part test, decision S6, 2026-10-01). PANT needs the circle: the person identifies God and Nature (Deus sive Natura), with entity in Nature and Nature in entity. ("Not atheism-plus-poetry. Not every nature-mystic.") Code PANT only if the person's own writing
  1. identifies God or the divine with Nature as a whole, as a claim about what exists, not as a figure of speech, **and**
  2. gives the whole at least one mark beyond feeling: unity as one substance or order, necessity or eternity, something mind-like, or value (SEP "Pantheism", §5, §10, §12, §13).

  Reverent language that meets neither part is ATHE (positive naturalism), or SECHUM if the person's public identity is the humanist movement. Explicit suspension is AGNOS. Einstein-style "Spinoza's God" statements pass part 1 and still need part 2; "nature is awe-inspiring" alone fails both.
- **Advaita Vedanta and some Kabbalah** (decision S6). By default code the host tradition (HINDU, JUDA) as primary ("Primary = dominant working metaphysics"). Use PANENT when the person's writing keeps a divine reality that includes the world but exceeds it, which is how v7.1 labels these forms. Use PANT only if the person passes the two-part test above. Belonging to the tradition is never enough for PANT.
- **Stoics** (decision S6). Code STOIC for ancient Stoics and for anyone whose avowed school is Stoicism (founders rule and "Primary = dominant working metaphysics"). The Stoic God is argued to be personal and providential, one "to whom we might approach in prayer" (SEP "Pantheism", citing Baltzly 2003), which is not the PANT circle. Use PANT for a later thinker who takes the Stoic or Spinozist identity of God and Nature without the providential, prayer-hearing deity, and who passes the two-part test.
- **CLASS_THEISM vs CLTHEI vs CHRIST/ISLAM/JUDA.**
  - CLASS_THEISM is the Aristotelian-Thomistic-Falsafa God: simple, immutable, known through reason.
  - CLTHEI (display label "Interventionist personal theism", approved S1) is the popular interventionist personal God who answers petition and works miracles. The two codes are neighbors that are easily confused (S5), not two forms of one tradition.
  - CHRIST/ISLAM/JUDA are for when the person's working worldview is the religion as practised and confessed, and neither theism split fits better.
  - Write down why the others were rejected.
- **Nominal vs working.** Many 19th-century scientists are "CHRIST-nominal / AGNOS-working" (v7.1). Code the working worldview, and record the nominal one in `nominal_affiliations`.
- **Changes over life.** Code the worldview of the working years, and list documented shifts in `worldview.changes_over_life`. If the major work falls in a different phase from later life, say so in `timing.worldview_during_major_work`.
- **Founders.** Code the founded system, even where later scholastic versions diverge.

## 6. The LIO axes

Axis poles from the v7.1 data book, section 4 "LIO axes (person-level)", verbatim:

| Axis | Interventionist pole | LIO pole |
|---|---|---|
| A Locus | Transcendent person outside the world | Immanent in or identical with the world |
| B Cause | Miracle, petition, reserved exemption | Law, regularity, no special cases |
| C Ledger | Reward and punishment of persons | Impersonal consequence, or none |
| D Authority | Revelation outranks observation | Observation and reason outrank revelation |
| E Scope | Hidden exceptions for an in-group | Same rules for stars, insects, humans |

**Scale: 0–4** (decision P1, 2026-10-01). Certainty is recorded separately from the score:

| score | meaning |
|---|---|
| 0 | at the interventionist pole |
| 1 | leans interventionist: the pole's features are present but limited |
| 2 | mixed, or the person holds both in different domains |
| 3 | leans LIO: the LIO pole with a stated, limited exception |
| 4 | at the LIO pole |

Rules:

- Score each axis separately from the person's own words. A code does not set the axes: two CHRIST people can differ on B.
- Every score needs `basis` and `certainty` (same scale as worldview codes), at least one cite, and a `rationale` that names the pole features present.
- If the evidence does not reach 0.5, use `BELOW_THRESHOLD`.
- Put quotations that bear on an axis in `worldview.statements` and tag them with `axes`.

**Mid-basin** (`worldview.mid_basin`, true/false). The v7.1 papers use "mid-basin theists" for first-rank theists whose work runs on lawful order. They name Faraday, Maxwell, Newton, Aquinas, Ibn Sina and Gödel as the first pool, "coded first as a stress test". The test (decision P4, 2026-10-01) uses the LIO axes only:

- `true` when `A_locus` ≤ 1 (God is a transcendent person, not the world) **and** `B_cause` ≥ 3 (law and regularity, no special cases), with B scored on the person's account of nature (decision P6, 2026-10-02), both at certainty ≥ 0.7;
- `false` when `A_locus` ≥ 3, or `A_locus` ≤ 1 with `B_cause` ≤ 1;
- otherwise:
  - `TODO`, with a note, if a needed axis is still `TODO`, or if both axes are scored at ≥ 0.7 but fall between the branches (A_locus = 2, or A_locus ≤ 1 with B_cause = 2); the note says the test has no branch for the case;
  - `UNKNOWN` only if a needed axis is itself `UNKNOWN` (researched, no reliable source gives it), keeping the meaning of §4;
  - `BELOW_THRESHOLD` if a needed axis is `BELOW_THRESHOLD` or scored only at 0.5, under the test's 0.7 bar; the note says which.

Notes:
- Score `B_cause` on the person's account of nature (P6), and say so in its `rationale`. For a scientist that is their working science. For a theologian or philosopher it is their account of the natural order: miracles and grace count against B only where they reach into it. If a theology-wide reading would differ, give it in the rationale. Someone may accept scriptural miracles and still allow no exemptions in nature.
- "First-rank" is not part of the test. Apply F ≥ 3 alongside it.
- The scale has only 1.0 / 0.7 / 0.5, so v7.1's "certainty ≥ 0.6" means ≥ 0.7.
- Deists (DEISM) usually pass. This is a stated consequence of the test, not an exception (see METHOD §1.1).
- Leave `mid_basin` as `TODO` until both axes are scored. Being in the first pool is not evidence of mid-basin status.

## 7. Quotations

- Copy quotations verbatim, with original spelling. Mark cuts with `[...]`. Don't modernize or correct.
- Each quote needs:
  - `cites` (source and locator: letter number, page, paragraph);
  - `context` (addressee, occasion, what the passage answers);
  - `kind` (public written profession, private letter, notebook, reported speech);
  - `verified_against` (primary transcription, primary facsimile, scholarly edition, secondary quotation);
  - `verified_on`.
- Prefer a primary transcription or scholarly edition. A quote known only from a secondary source is marked `secondary quotation` and cannot by itself support certainty 1.0.
- Reported speech (someone else's memory of what the person said) is never a written profession.
- Never paraphrase inside quotation marks.

## 8. Other sections

**Identity.** `identity.roster` is a copy of the roster row, and the validator checks it. If the roster looks wrong, raise it in `review.data_quality_flags` and fix it through `curated_aliases.csv`, not in the person file.

**Basics.**
- Dates follow the conventions in [DATA_DICTIONARY.md](DATA_DICTIONARY.md#1-conventions). When sources disagree, give the best-supported value, put the others in `alternatives`, and set certainty 0.5 if the dispute is real.
- `first_lasting_contribution_year` is the year of the earliest item in `contribution.lasting_original_contributions`.
- `era_bucket` (decision P2) follows from that year. A year on an edge goes to the later bucket: 1600 is `1600 to 1749`, 1950 is `1950 on`. Birth year stays in `basics.birth.date`, so a birth-year version can be computed for a sensitivity check:

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

- `region_of_birth` / `region_of_work` (decision P3): Northern Europe, Western Europe, Southern Europe, Eastern Europe, Middle East and North Africa, Sub-Saharan Africa, Central Asia, South Asia, East Asia, Southeast Asia, North America, Latin America and Caribbean, Oceania. Find the place's modern country and look it up in [`data/reference/regions.csv`](../data/reference/regions.csv) (UN M49 sub-regions; MENA = Northern Africa + Western Asia + Iran; Afghanistan stays South Asia). Record the historical polity in `place.polity_then`.
- `sex_as_recorded` is descriptive, for baseline matching only.

**Contribution.**
- List only original contributions that are still used or built on, with `lasting` saying what rests on them.
- `evidence_of_impact` uses concrete markers: named laws or units, textbook canon, assessments by later major figures, honours.
- `definition_fit` is `clearly meets`, `arguable` or `does not meet` against the Lane A definition (lasting original impact; not collectives, transient fame, or mastery without originality). It feeds roster status decisions, which are Jason's.

**Childhood.**
- Record facts only. `early_mathematics` is the highest level reached before about 18.
- `early_geometric_style_reasoning` records documented exposure to definition-to-consequence reasoning (Euclid, formal logic, proof). It does not record whether this "worked". That is Lane B.

**Timing.**
- `lio_views_relative_to_major_work` is one of: `held from childhood`, `before major work`, `during major work`, `after major work`, `no LIO-type views found`, `unclear`.
- Base it on dated evidence (`first_evidence_of_lio_type_views` with year and age).

**Lane B.**
- `geometric_form_present` and `circle_present` are `yes` / `partly` / `no` / `unclear`. `form_acquired` is `childhood or adolescence` / `adulthood, before major work` / `through the profession` / `unclear`.
- Each needs cites like any claim.
- `reading` states what the case means for H1, *as belief*. A case that cuts against H1 should be recorded just as carefully as one that fits.

**Institutions and collaborators.** Use `roster_id` when the other person is on the roster (the validator checks it).

**Review.**
- `data_quality_flags` lists every source conflict you found, even small ones.
- `open_questions` lists what the next run should do.

## 9. Writing style

- Plain, short sentences. No hype, no "genius of geniuses".
- Facts in front matter. The body explains and connects them, with inline cites `[S2, §3]`.
- Don't put a fact in the body that isn't backed by a cited source.

---

# Part 2: Belief systems

## 10. What a system record is for

Each of the 77 v7.1 belief systems has a file `systems/<CODE>.md`. It serves two purposes:

1. It is the reference coders use to decide whether a person gets the code (`coding_guidance`).
2. It is a sourced description of the system's metaphysics and its position on the LIO axes. Revised rubric scores can later be argued from it.

The 77 codes (display labels; two differ from v7.1, both approved: CLTHEI by S1, PANT by S2):

| # | code | display label | v7.1 total |
|---|---|---|---|
| 1 | [`ATHE`](../systems/ATHE.md) | Atheism (naturalistic/materialistic – no gods + philosophical naturalism) | 50 |
| 2 | [`AGNOS`](../systems/AGNOS.md) | Agnosticism | 49 |
| 3 | [`BRGHTS`](../systems/BRGHTS.md) | Brights (The Brights Movement) | 49 |
| 4 | [`EMPIR`](../systems/EMPIR.md) | Empiricism | 49 |
| 5 | [`ETHCUL`](../systems/ETHCUL.md) | Ethical Culture (Ethical Humanism) | 49 |
| 6 | [`PANT`](../systems/PANT.md) | Pantheism (Spinozistic/naturalistic 'God = Universe') | 49 |
| 7 | [`RATN`](../systems/RATN.md) | Rationalism | 49 |
| 8 | [`SECHUM`](../systems/SECHUM.md) | Secular Humanism | 49 |
| 9 | [`SUNASM`](../systems/SUNASM.md) | Sunday Assembly | 49 |
| 10 | [`PRAG`](../systems/PRAG.md) | Pragmatism | 48 |
| 11 | [`ARIST`](../systems/ARIST.md) | Aristotelianism | 47 |
| 12 | [`EFFALT`](../systems/EFFALT.md) | Effective Altruism | 47 |
| 13 | [`TRNSHM`](../systems/TRNSHM.md) | Transhumanism | 47 |
| 14 | [`ABSURD`](../systems/ABSURD.md) | Absurdism | 46 |
| 15 | [`CYNIC`](../systems/CYNIC.md) | Cynicism | 46 |
| 16 | [`EPICUR`](../systems/EPICUR.md) | Epicureanism | 46 |
| 17 | [`EXIST`](../systems/EXIST.md) | Existentialism | 46 |
| 18 | [`NIHIL`](../systems/NIHIL.md) | Nihilism | 46 |
| 19 | [`OBJCT`](../systems/OBJCT.md) | Objectivism (Ayn Rand's philosophy) | 46 |
| 20 | [`SCEPT`](../systems/SCEPT.md) | Scepticism (Skepticism) | 46 |
| 21 | [`STOIC`](../systems/STOIC.md) | Stoicism | 46 |
| 22 | [`KANT`](../systems/KANT.md) | Kantianism | 45 |
| 23 | [`PHENOM`](../systems/PHENOM.md) | Phenomenology | 45 |
| 24 | [`UTIL`](../systems/UTIL.md) | Utilitarianism | 45 |
| 25 | [`PANDEI`](../systems/PANDEI.md) | Pandeism | 44 |
| 26 | [`PANEND`](../systems/PANEND.md) | Panendeism | 44 |
| 27 | [`CLASS_THEISM`](../systems/CLASS_THEISM.md) | Classical Theism (Aristotelian-Thomistic-Islamic Peripatetic) | 43 |
| 28 | [`DETERM`](../systems/DETERM.md) | Determinism | 43 |
| 29 | [`LVSAT`](../systems/LVSAT.md) | LaVeyan Satanism (Church of Satan) | 43 |
| 30 | [`PANENT`](../systems/PANENT.md) | Panentheism (Process Theology, some Kabbalah/Advaita forms) | 42 |
| 31 | [`DEISM`](../systems/DEISM.md) | Deism | 41 |
| 32 | [`HEDON`](../systems/HEDON.md) | Hedonism | 41 |
| 33 | [`PANPSY`](../systems/PANPSY.md) | Panpsychism (consciousness inherent in matter) | 39 |
| 34 | [`IDEAL`](../systems/IDEAL.md) | Idealism | 38 |
| 35 | [`BUDDH`](../systems/BUDDH.md) | Buddhism | 37 |
| 36 | [`PLATO`](../systems/PLATO.md) | Platonism | 37 |
| 37 | [`JAIN`](../systems/JAIN.md) | Jainism | 36 |
| 38 | [`SOLIP`](../systems/SOLIP.md) | Solipsism | 35 |
| 39 | [`BAHAI`](../systems/BAHAI.md) | Bahá’í Faith | 34 |
| 40 | [`ANIM`](../systems/ANIM.md) | Animism | 32 |
| 41 | [`CAODAI`](../systems/CAODAI.md) | Caodaism | 32 |
| 42 | [`CHNFOLK`](../systems/CHNFOLK.md) | Chinese Folk Religion (Shenism) | 32 |
| 43 | [`HYLO`](../systems/HYLO.md) | Hylozoism | 32 |
| 44 | [`CONFUC`](../systems/CONFUC.md) | Philosophical Confucianism | 32 |
| 45 | [`SHINTO`](../systems/SHINTO.md) | Shinto | 32 |
| 46 | [`TAO`](../systems/TAO.md) | Taoism (Daoism) | 32 |
| 47 | [`HINDU`](../systems/HINDU.md) | Hinduism (Sanatana Dharma) | 28 |
| 48 | [`HEATH`](../systems/HEATH.md) | Heathenry (Ásatrú/Norse-Germanic Paganism) | 27 |
| 49 | [`HELLEN`](../systems/HELLEN.md) | Hellenismos (Greek Reconstructionist Paganism) | 27 |
| 50 | [`KEMET`](../systems/KEMET.md) | Kemetism (Kemetic Orthodoxy/Egyptian Reconstructionism) | 27 |
| 51 | [`RODNOV`](../systems/RODNOV.md) | Rodnovery (Slavic Native Faith) | 27 |
| 52 | [`WICCA`](../systems/WICCA.md) | Wicca | 27 |
| 53 | [`ABORIG`](../systems/ABORIG.md) | Aboriginal Traditions (Australian Aboriginal Dreamtime) | 26 |
| 54 | [`BON`](../systems/BON.md) | Bön (Tibetan indigenous religion) | 26 |
| 55 | [`NATAM`](../systems/NATAM.md) | Native American Traditions | 26 |
| 56 | [`SANTER`](../systems/SANTER.md) | Santería (Lucumí/Regla de Ocha) | 26 |
| 57 | [`VODUN`](../systems/VODUN.md) | Vodun (Voodoo/West African Vodun) | 26 |
| 58 | [`ANTHRO`](../systems/ANTHRO.md) | Anthroposophy | 25 |
| 59 | [`CHAOSM`](../systems/CHAOSM.md) | Chaos Magick | 25 |
| 60 | [`4THWAY`](../systems/4THWAY.md) | Fourth Way (Gurdjieff's teachings) | 25 |
| 61 | [`HERMET`](../systems/HERMET.md) | Hermeticism | 25 |
| 62 | [`SIKH`](../systems/SIKH.md) | Sikhism | 25 |
| 63 | [`THEOS`](../systems/THEOS.md) | Theosophy | 25 |
| 64 | [`DRUZE`](../systems/DRUZE.md) | Druze Faith | 23 |
| 65 | [`MANDAE`](../systems/MANDAE.md) | Mandaeism | 23 |
| 66 | [`YAZID`](../systems/YAZID.md) | Yazidism (Yezidism) | 23 |
| 67 | [`ZORO`](../systems/ZORO.md) | Zoroastrianism (Mazdayasna) | 23 |
| 68 | [`CHRIST`](../systems/CHRIST.md) | Christianity | 22 |
| 69 | [`ISLAM`](../systems/ISLAM.md) | Islam | 22 |
| 70 | [`JUDA`](../systems/JUDA.md) | Judaism | 22 |
| 71 | [`MORMON`](../systems/MORMON.md) | Mormonism (The Church of Jesus Christ of Latter-day Saints) | 21 |
| 72 | [`CLTHEI`](../systems/CLTHEI.md) | Interventionist personal theism | 20 |
| 73 | [`THSAT`](../systems/THSAT.md) | Theistic Satanism (Joy of Satan or similar) | 20 |
| 74 | [`THELEM`](../systems/THELEM.md) | Thelema (Crowley/Ordo Templi Orientis) | 20 |
| 75 | [`FALUNG`](../systems/FALUNG.md) | Falun Gong (Falun Dafa) | 17 |
| 76 | [`RAEL`](../systems/RAEL.md) | Raëlism (Raëlian Movement) | 17 |
| 77 | [`SCIENT`](../systems/SCIENT.md) | Scientology | 17 |

## 11. Rules for system records

- **v7.1 scores are frozen.** `v7_1_rubric` (L, P, E, V, X, total, scoring note) is copied from the data book and labelled "authorial v7.1 scores". The validator checks it character for character. Don't fix typos or totals there. Raise problems in `review.data_quality_flags`.
- **Revised scores** go in `revised_rubric` (decision S3). Its `status` stays `not started` until the first coding pool is done and Jason opens the revision. Then each axis score needs a rationale and a cite, two scorers score a sample independently and report agreement before the rest are scored, and Jason approves the final numbers. Revised scores sit beside the v7.1 scores and never overwrite them.
- **The code list is closed** for v8 (decision S4). Propose a new code, or a split of an existing one, in a list with the code, why, example people and (for a split) the people it would move. New codes are added in one batch with one schema bump and Jason's approval.
- **Labels.** `identity.v7_1_label` is verbatim from v7.1. `display_label` is what v8 tables show. A change needs `label_status: proposed — pending Jason's OK` and an entry in OPEN_DECISIONS.
- **Describe the official or scholarly form.** Metaphysics and LIO axes describe the system as its authoritative texts or leading scholars present it. Popular forms, regional forms and schools go in `schools_and_variants`, each with `form` and `lio_difference`. If the popular form differs enough to have its own code (CLASS_THEISM vs CLTHEI), link the two in `related_codes` as `neighbor (easily confused)` (S5).
- **Stance labels.** Each metaphysics item has a sentence `value` and a short `stance` from a fixed list. Use `varies by school` when there is no single answer, and explain in `value`:

  | item | allowed stances |
  |---|---|
  | god_nature_relation | identity · God in Nature and beyond it · creator distinct from creation · many gods within nature · no God · not addressed · varies by school |
  | deity_personal | personal · impersonal · both / disputed · no deity · not addressed · varies by school |
  | intervention | none · rare · regular · not addressed · varies by school |
  | miracles | denied · reinterpreted as natural · affirmed · not addressed · varies by school |
  | petition_and_prayer | no petition · contemplative only · petition answered · not addressed · varies by school |
  | afterlife | none · impersonal survival or eternity · personal afterlife · rebirth · not addressed · varies by school |
  | moral_ledger | none · impersonal consequence · personal reward and punishment · karma-type law · varies by school |
  | authority | observation and reason · both, reason first · both, revelation first · revelation · tradition or ancestors · founder · varies by school |
  | reserved_exemptions | none · some · central · varies by school |
  | teleology_in_nature | none · immanent ends · designer's purposes · varies by school |

- **LIO axes** use the same 0–4 scale as people (P1), scored for the official or scholarly form, with a `rationale`. System records have no `basis` field. Use certainty 1.0 for positions the sources state directly, 0.7 for a coder's reading of what they say, and 0.5 where scholars disagree.
- **Adherents** are context only. Give year and scope, and cite a demographic source. Never use them as a denominator.
- **Science stance**: historical (in the periods the roster covers) and current (official bodies or leading scholars). Cite both, and keep them separate.
- **Coding guidance**: `use_when` quotes the v7.1 rule verbatim where one names the code, then adds detail. `do_not_use_when` names the usual mistakes and the code to use instead. `neighbors` lists codes that are easily confused with this one.
- **Certainty and cites** follow the same claim rules as person records.

## 12. Worked example

`systems/PANT.md` shows a filled record. Everything in it is from two Stanford Encyclopedia of Philosophy entries. Things the sources don't give stay `TODO`. Contested points, such as Spinoza on the eternity of the mind, use certainty 0.5 with an `alternatives` entry.
