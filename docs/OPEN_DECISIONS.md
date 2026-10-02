# Open decisions

Choices that need Jason's sign-off. Nothing here has been decided. Where the repo needs *some* value to work, it uses the stated proposal and marks it PROPOSED, and nothing downstream treats it as settled. When a decision is made:

1. record it here under "Decided", with the date;
2. update the files it touches;
3. note it in `CHANGELOG.md`.

## Roster

### R1. Georgia O'Keeffe's status
v7.1 left her status blank. Its headline count says 432 core, but only 431 rows are tagged core, which suggests she was meant to be core. v8 marks her `needs status (blank in v7)` and assumes nothing.
**Options:** core / provisional / review.

### R2. Wilbur and Orville Wright
v7.1 excluded "Wright Brothers" as a collective. In the raw lists, Claude names them as two individuals under a "Wright Brothers - " prefix, and Gemini also lists them individually. v8 keeps them as two people with status `new — needs status`.
**Options:** keep both as individuals; exclude both as a collective; keep one record for joint credit (not supported by the schema).

### R3. "Brian Maynard Smith"
Listed by GPT only. Probably means John Maynard Smith, the evolutionary biologist. Kept as listed and flagged.
**Options:** treat as John Maynard Smith (add a `display_fix` or merge if he appears elsewhere); exclude as a model error; keep as is.

### R4. Merges to confirm
These are in `curated_aliases.csv` with confidence `high`. Each one decides that two names are one person, so they should get a human look:
- Bob Kahn → Robert Kahn
- Elizabeth Anscombe → G.E.M. Anscombe
- Benedict de Spinoza → Baruch Spinoza
- Buddha → Siddhartha Gautama

### R5. Similarity pairs left separate
The automatic scan flagged these pairs. They are left as different people, which looks right, but a human should confirm:
- Ken Thompson / E.P. Thompson
- Edward Said / Edward Sapir
- Marc Bloch / Maurice Bloch

### R6. Statuses for the 900 new names
v8 adds 900 people with status `new — needs status`.
**Proposal:** assign a status now only to the new names with F ≥ 3, because only they enter the primary analysis. There are 9: Georg Wilhelm Friedrich Hegel (F 4), Duns Scotus, Edward O. Wilson, John Nash, Jorge Luis Borges, Laozi, Ludwig Mies van der Rohe, Paul Cézanne and Vint Cerf (F 3). The other 891 (F 1–2) would stay `new — needs status` until sensitivity analyses need them.

### R7. Field buckets
v7's hand mapping of fields to buckets is not on disk. v8 uses keyword rules in `rebuild_roster.py` (21 buckets).
**Options:** accept the rules; supply the v7 mapping; revise the bucket list.

### R8. Id freeze point
**Proposal (in force in METHOD §3.2):** an id freezes when its person file is created, or when v8 is published, whichever comes first. Before that, overrides may change ids.

## Persons schema

### P1. LIO axis scale: PROPOSED 0–4
- 0 = interventionist pole
- 1 = leans interventionist
- 2 = mixed
- 3 = leans LIO
- 4 = LIO pole

v7.1 defined the poles but no scale. Used in `worldview.lio_axes` and `systems/*/lio_axes`. PANT is scored on it as a demonstration. No person is scored yet.
**Options:** approve; use 0–2 or −2…+2; use the poles only, with a free-text position.

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

### P4. Mid-basin: operational definition
The v7.1 papers use "mid-basin theists" and name the first pool (Faraday, Maxwell, Newton, Aquinas, Ibn Sina, Gödel) as a stress test, but give no test for membership. `worldview.mid_basin` stays `TODO` everywhere until there is one. That includes Faraday, even though v7.1 treats him as one.
**Possible definition, for discussion only:** primary system is theistic (CLASS_THEISM, CLTHEI, CHRIST, ISLAM, JUDA or similar) at certainty ≥ 0.7, *and* B_cause ≥ 3 in the domain of their scientific work.

### P5. Who may set "reviewed"
**Proposal:** only a named human reviewer. Agents stop at `draft — unreviewed`.

## Belief systems

### S1. CLTHEI display label
The v7.1 label is "Classical Theism (personal, interventionist Creator God)". It shares the words "Classical Theism" with CLASS_THEISM, which the v7.1 rules say it must not be confused with.
**Proposed display label:** "Interventionist personal theism". The code stays `CLTHEI` and `v7_1_label` is kept verbatim. Status in the file: `proposed — pending Jason's OK`.

### S2. PANT display label
The v7.1 label is cut off mid-word in both the data book table and the Word file: "Pantheism (Spinozistic/naturalistic 'God = Univers…".
**Proposed display label:** "Pantheism (Spinozistic/naturalistic)", trimmed at the last whole phrase. If the full original label exists elsewhere, use it instead.

### S3. Expanding the rubric
The data book defines L, P, E, V and X (see DATA_DICTIONARY §4). `revised_rubric` exists in every file with status `not started`.
**Decide:** whether and when to open revised scoring, who scores, and whether revised scores need cites per axis (the schema allows it).

### S4. New belief systems
Schema 1.0 allows only the 77 v7.1 codes. The validator rejects others. Adding a system (for example, splitting a popular form out of an existing code) needs a schema version bump and Jason's approval.

### S5. related_codes direction
`relation` reads "<code> is <relation> this system". So CLTHEI lists CLASS_THEISM as its "scholastic form of", and CLASS_THEISM lists CLTHEI as its "popular form of". Treating the two as scholastic and popular forms of one tradition is a reading of the v7.1 rule "CLASS_THEISM ... is not CLTHEI (popular interventionist personal God)".
**Options:** confirm; change both to "neighbor (easily confused)".

### S6. PANT boundaries (raised by the PANT worked example)
- Modern scientific or naturalistic pantheism: PANT (the circle) or ATHE with reverent language? v7.1 says "not atheism-plus-poetry", but this needs a test that can be applied.
- Advaita Vedanta and some Kabbalah: v7.1's PANENT label names "some Kabbalah/Advaita forms", while the Stanford Encyclopedia of Philosophy lists them among pantheist strands.
- Stoic pantheists: STOIC or PANT?

## Decided

(none yet)
