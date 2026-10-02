# Genius roster: v7.1 → v8 (step 1: roster and frequency rebuild)

Built by `scripts/rebuild_roster.py` from the five raw model lists in `data/sources/model_lists/` (byte-for-byte copies of `V6_(history)/V6/GeniiLists/` in the v7 repo; checksums in `data/sources/SHA256SUMS`).

## Summary

- Raw input: 2746 rows across five lists (Claude 374, DeepSeek 997, Gemini 669, GPT 376, Grok 330).
- 1715 distinct raw name strings after lowercasing/de-accenting; 1416 distinct names after automatic formatting normalization (hyphens, 'Last-First' order, accents, initials); 1384 after 32 curated alias merges; 4 non-person/collective entries excluded.
- **v8 roster: 1380 unique people** (v7.1: 482).
- F is now the number of distinct models (1–5) that list the person. Maximum observed F = 5; no value above 5.
- Matched to a v7 row: 482 people. New (not in v7): 898. v7 rows not kept as their own row: 0 (0 merged into another v7 person, 0 excluded, 0 unmatched).
- Of the 482 matched people, F went up for 159, down for 104, unchanged for 219.

## Why v7 frequencies were wrong (checked by re-running the v6 script logic)

A re-run of `aggregateGeniiListsByFreq.py`'s logic reproduces the v7 500-row aggregate exactly (500/500 names identical), so the causes below are confirmed, not guessed.

1. **geniiClaude.csv was never read.** The script's file list has only Grok, Gemini, DeepSeek and GPT. So the maximum for a clean name was 4 (Newton, Darwin, Maxwell, Faraday, Spinoza all got 4), and Claude-only names could not appear.
2. **It counts rows, not models.** Gemini repeats most of its list a second time in 'Last-First' form, and DeepSeek repeats many names (DeepSeek: 997 rows for 854 people). A person listed twice by one model got 2. This is how F>5 arose (Ibn Sina 9 = Avicenna 5 + Ibn Sina 4) and why some DeepSeek-only names had F=3–5 in v7 (e.g. Donna Haraway: DeepSeek lists her 5 times, v7 F=5, v8 F=1).
3. **Hyphens and accented letters were deleted, not turned into spaces or plain letters.** 'John-Nash' became 'johnnash' (≠ 'john nash'), 'René' became 'ren'. A 0.9 string-similarity step rescued some long names but not short ones ('John Nash' vs 'John-Nash' scores 0.89).
4. **The list was cut at 500 rows.** After sorting by count then name, the cut fell inside the count-1 tail at 'Attar-Farid ud-Din', so 1143 later entries were dropped. Hegel (split into four count-1 variants: 'G-W-F Hegel', 'Georg Wilhelm Friedrich Hegel', 'Georg-Wilhelm-Friedrich-Hegel', 'Hegel-G-W-F'), Cantor, Boltzmann, Babbage, Rawls, Dijkstra and John Nash were all lost this way (most of them are also Claude names).
5. The 0.9 similarity step made 172 unreviewed merges. Nearly all joined hyphen/accent variants of the same person; 2 joined names that differ beyond formatting: Andrey Kolmogorov → Andrei Kolmogorov; Arthur Schlesinger Sr. → Arthur Schlesinger Jr. — Arthur Schlesinger Jr. and Sr. are different people (father and son); v8 keeps them apart.

## Distribution by F

| F | v8 people | v7.1 people |
|---|---|---|
| 9 | 0 | 1 |
| 8 | 0 | 1 |
| 7 | 0 | 3 |
| 6 | 0 | 2 |
| 5 | 82 | 24 |
| 4 | 55 | 72 |
| 3 | 94 | 84 |
| 2 | 183 | 221 |
| 1 | 966 | 74 |
| total | 1380 | 482 |

| Band | v8 | v7.1 |
|---|---|---|
| high (≥5; in v8 exactly 5) | 82 | 31 |
| core (3–4) | 149 | 156 |
| extended (2) | 183 | 221 |
| single-source (1) | 966 | 74 |

People listed by each model (after merging): Claude 360, DeepSeek 854, Gemini 336, GPT 371, Grok 323.

## Top of the v8 roster (F = 5)

82 people are on all five lists:

Ada Lovelace (mathematics), Adam Smith (economics), Al-Farabi (philosophy), Al-Khwarizmi (mathematics), Alan Turing (mathematics), Albert Einstein (physics), Alexander Graham Bell (invention), Archimedes (mathematics), Aristotle (philosophy), Barbara McClintock (genetics), Baruch Spinoza (philosophy), Bernhard Riemann (mathematics), Bertrand Russell (philosophy), Blaise Pascal (mathematics), Carl Friedrich Gauss (mathematics), Charles Darwin (biology), Chien-Shiung Wu (physics), Claude Debussy (music), Claude Monet (art), Dante Alighieri (literature), David Hume (philosophy), Emmy Noether (mathematics), Enrico Fermi (physics), Erwin Schrödinger (physics), Euclid (mathematics), Francis Bacon (philosophy), Frida Kahlo (art), Friedrich Nietzsche (philosophy), Fyodor Dostoevsky (literature), Gabriel García Márquez (literature), Galileo Galilei (physics), Gottfried Wilhelm Leibniz (polymath), Grace Hopper (computer science), Hannah Arendt (philosophy), Henri Poincaré (mathematics), Hippocrates (medicine), Homer (literature), Hypatia (mathematics), Ibn Sina (Avicenna) (polymath), Igor Stravinsky (music), Immanuel Kant (philosophy), Isaac Newton (physics), James Clerk Maxwell (physics), Johann Sebastian Bach (music), Johannes Kepler (astronomy), John Locke (philosophy), John von Neumann (mathematics), Karl Marx (philosophy), Kurt Gödel (mathematics), Leo Tolstoy (literature), Leonardo da Vinci (polymath), Lise Meitner (physics), Ludwig van Beethoven (music), Ludwig Wittgenstein (philosophy), Maimonides (philosophy), Marie Curie (physics), Max Planck (physics), Michael Faraday (physics), Michelangelo (art), Niels Bohr (physics), Nikola Tesla (invention), Noam Chomsky (linguistics), Omar Khayyam (mathematics), Pablo Picasso (art), Plato (philosophy), Raphael (art), Rembrandt (art), René Descartes (philosophy), Richard Feynman (physics), Rosalind Franklin (biology), Salvador Dalí (art), Simone de Beauvoir (philosophy), Socrates (philosophy), Stephen Hawking (physics), Subrahmanyan Chandrasekhar (physics), Thomas Edison (invention), Tim Berners-Lee (computer science), Vincent van Gogh (art), Virginia Woolf (literature), Werner Heisenberg (physics), William Shakespeare (literature), Wolfgang Amadeus Mozart (music)

## F changes for names called out in the v7 problem list

| Person | v7 F | v8 F | v8 models |
|---|---|---|---|
| Isaac Newton | 4 | 5 | Claude;DeepSeek;Gemini;GPT;Grok |
| Charles Darwin | 4 | 5 | Claude;DeepSeek;Gemini;GPT;Grok |
| James Clerk Maxwell | 4 | 5 | Claude;DeepSeek;Gemini;GPT;Grok |
| Michael Faraday | 4 | 5 | Claude;DeepSeek;Gemini;GPT;Grok |
| Baruch Spinoza | 4 | 5 | Claude;DeepSeek;Gemini;GPT;Grok |
| Ibn Sina (Avicenna) | 9 | 5 | Claude;DeepSeek;Gemini;GPT;Grok |
| Ibn Rushd (Averroes) | 8 | 4 | Claude;DeepSeek;Gemini;Grok |
| Blaise Pascal | 7 | 5 | Claude;DeepSeek;Gemini;GPT;Grok |
| Francis Bacon | 7 | 5 | Claude;DeepSeek;Gemini;GPT;Grok |
| Hannah Arendt | 7 | 5 | Claude;DeepSeek;Gemini;GPT;Grok |
| Maimonides | 6 | 5 | Claude;DeepSeek;Gemini;GPT;Grok |
| Michel Foucault | 6 | 4 | Claude;DeepSeek;Gemini;Grok |
| Albert Einstein | 5 | 5 | Claude;DeepSeek;Gemini;GPT;Grok |
| Al-Khwarizmi | 5 | 5 | Claude;DeepSeek;Gemini;GPT;Grok |
| Georg Wilhelm Friedrich Hegel | missing | 4 | Claude;Gemini;GPT;Grok |
| Georg Cantor | missing | 2 | Claude;DeepSeek |
| Ludwig Boltzmann | missing | 2 | Claude;DeepSeek |
| Charles Babbage | missing | 2 | Claude;GPT |
| John Rawls | missing | 2 | Claude;DeepSeek |
| Edsger Dijkstra | missing | 2 | Claude;GPT |
| John Nash | missing | 3 | Claude;GPT;Grok |

### All v7 rows with F > 5

- Ibn Sina (Avicenna): v7 F=9 (Avicenna (5); Ibn Sina (4)) → v8 F=5 (Claude;DeepSeek;Gemini;GPT;Grok)
- Ibn Rushd (Averroes): v7 F=8 (Averroes (6); Ibn Rushd (2)) → v8 F=4 (Claude;DeepSeek;Gemini;Grok)
- Blaise Pascal: v7 F=7 (Pascal-Blaise (2)) → v8 F=5 (Claude;DeepSeek;Gemini;GPT;Grok)
- Francis Bacon: v7 F=7 (Bacon-Francis (2)) → v8 F=5 (Claude;DeepSeek;Gemini;GPT;Grok)
- Hannah Arendt: v7 F=7 (Arendt-Hannah (2)) → v8 F=5 (Claude;DeepSeek;Gemini;GPT;Grok)
- Maimonides: v7 F=6 (no alias note) → v8 F=5 (Claude;DeepSeek;Gemini;GPT;Grok)
- Michel Foucault: v7 F=6 (no alias note) → v8 F=4 (Claude;DeepSeek;Gemini;Grok)

### Largest F increases (matched people)

- Gabriel García Márquez: 3 → 5
- Gottfried Wilhelm Leibniz: 3 → 5
- Henri Poincaré: 3 → 5
- John Maynard Keynes: 2 → 4
- John von Neumann: 3 → 5
- Salvador Dalí: 3 → 5
- Siddhartha Gautama: 2 → 4
- Vincent van Gogh: 3 → 5
- Ada Lovelace: 4 → 5
- Adam Smith: 4 → 5
- Al-Biruni: 2 → 3
- Al-Farabi: 4 → 5
- Al-Razi: 2 → 3
- Alan Turing: 4 → 5
- Alessandro Volta: 1 → 2
- Alexander Fleming: 2 → 3
- Alexander Graham Bell: 4 → 5
- Alexander Grothendieck: 2 → 3
- Alfred Wegener: 1 → 2
- Allen Newell: 1 → 2
- Amartya Sen: 2 → 3
- Andrea Palladio: 1 → 2
- Andreas Vesalius: 2 → 3
- Andrew Wiles: 3 → 4
- Andy Warhol: 1 → 2
- Antoine Lavoisier: 3 → 4
- Arnold Schoenberg: 2 → 3
- Arthur Schopenhauer: 3 → 4
- Aryabhata: 2 → 3
- Augustine of Hippo: 2 → 3
- B.F. Skinner: 3 → 4
- Barbara McClintock: 4 → 5
- Baruch Spinoza: 4 → 5
- Bernhard Riemann: 4 → 5
- Bertrand Russell: 4 → 5
- Brahmagupta: 2 → 3
- Caravaggio: 2 → 3
- Carl Friedrich Gauss: 4 → 5
- Carl Jung: 3 → 4
- Carl Linnaeus: 2 → 3

### All F decreases (104)

- Donna Haraway: 5 → 1 (DeepSeek)
- Ibn Rushd (Averroes): 8 → 4 (Claude;DeepSeek;Gemini;Grok)
- Ibn Sina (Avicenna): 9 → 5 (Claude;DeepSeek;Gemini;GPT;Grok)
- Jurgen Habermas: 4 → 1 (DeepSeek)
- Octavio Paz: 4 → 1 (Gemini)
- Paul Feyerabend: 4 → 1 (DeepSeek)
- Pierre Bourdieu: 5 → 2 (DeepSeek;GPT)
- Thomas Kuhn: 5 → 2 (DeepSeek;Gemini)
- Anthony Giddens: 3 → 1 (DeepSeek)
- Blaise Pascal: 7 → 5 (Claude;DeepSeek;Gemini;GPT;Grok)
- Bruno Latour: 3 → 1 (DeepSeek)
- Charles Tilly: 3 → 1 (DeepSeek)
- Fernand Braudel: 3 → 1 (DeepSeek)
- Francis Bacon: 7 → 5 (Claude;DeepSeek;Gemini;GPT;Grok)
- Hannah Arendt: 7 → 5 (Claude;DeepSeek;Gemini;GPT;Grok)
- Immanuel Wallerstein: 3 → 1 (DeepSeek)
- Imre Lakatos: 4 → 2 (DeepSeek;Gemini)
- Karen Barad: 3 → 1 (DeepSeek)
- Mary Douglas: 3 → 1 (DeepSeek)
- Michael Polanyi: 3 → 1 (DeepSeek)
- Michel Foucault: 6 → 4 (Claude;DeepSeek;Gemini;Grok)
- Simon Schaffer: 3 → 1 (DeepSeek)
- Steven Shapin: 3 → 1 (DeepSeek)
- Theda Skocpol: 3 → 1 (DeepSeek)
- Victor Turner: 3 → 1 (DeepSeek)
- Akira Yoshino: 2 → 1 (DeepSeek)
- Alexander Koyre: 2 → 1 (DeepSeek)
- Arthur Schlesinger Jr.: 2 → 1 (DeepSeek)
- Basho: 2 → 1 (Gemini)
- Byung-Chul Han: 2 → 1 (DeepSeek)
- Charles Taylor: 2 → 1 (DeepSeek)
- Chinua Achebe: 4 → 3 (Gemini;GPT;Grok)
- Clifford Geertz: 2 → 1 (DeepSeek)
- David Lindberg: 2 → 1 (DeepSeek)
- David Noble: 2 → 1 (DeepSeek)
- Derek Parfit: 2 → 1 (DeepSeek)
- Donald MacKenzie: 2 → 1 (DeepSeek)
- Donatello: 4 → 3 (Gemini;GPT;Grok)
- Dorothy Hodgkin: 5 → 4 (Claude;DeepSeek;Gemini;Grok)
- E. E. Evans-Pritchard: 2 → 1 (DeepSeek)
- Edmund Leach: 2 → 1 (DeepSeek)
- Edward Gibbon: 2 → 1 (DeepSeek)
- Edward Grant: 2 → 1 (DeepSeek)
- El Greco: 2 → 1 (Gemini)
- Emmanuel Le Roy Ladurie: 2 → 1 (DeepSeek)
- Emmanuelle Charpentier: 3 → 2 (DeepSeek;Grok)
- Evelyn Fox Keller: 2 → 1 (DeepSeek)
- Frances Arnold: 3 → 2 (DeepSeek;Grok)
- Fredrik Barth: 2 → 1 (DeepSeek)
- Georges Duby: 2 → 1 (DeepSeek)
- Hafez: 3 → 2 (Gemini;GPT)
- Helen Longino: 2 → 1 (DeepSeek)
- Hua Tuo: 2 → 1 (DeepSeek)
- Jacob Burckhardt: 2 → 1 (DeepSeek)
- Jacques Le Goff: 2 → 1 (DeepSeek)
- James Coleman: 2 → 1 (DeepSeek)
- Jami: 2 → 1 (Gemini)
- Jennifer Doudna: 3 → 2 (DeepSeek;Grok)
- Johannes Gutenberg: 4 → 3 (Gemini;GPT;Grok)
- John B. Goodenough: 2 → 1 (DeepSeek)
- John Bardeen: 2 → 1 (DeepSeek)
- John Dupré: 2 → 1 (DeepSeek)
- John Hedley Brooke: 2 → 1 (DeepSeek)
- Joseph Lister: 2 → 1 (DeepSeek)
- Kalidasa: 2 → 1 (Gemini)
- Karl Popper: 3 → 2 (DeepSeek;Gemini)
- Katharine Park: 2 → 1 (DeepSeek)
- Lawrence Kohlberg: 2 → 1 (DeepSeek)
- Leopold von Ranke: 2 → 1 (DeepSeek)
- Londa Schiebinger: 2 → 1 (DeepSeek)
- Lorraine Daston: 2 → 1 (DeepSeek)
- Lucien Febvre: 2 → 1 (DeepSeek)
- M. Stanley Whittingham: 2 → 1 (DeepSeek)
- Maimonides: 6 → 5 (Claude;DeepSeek;Gemini;GPT;Grok)
- Manuel Castells: 2 → 1 (DeepSeek)
- Marc Bloch: 2 → 1 (DeepSeek)
- Margaret Rossiter: 2 → 1 (DeepSeek)
- Maria Gaetana Agnesi: 3 → 2 (Gemini;Grok)
- Mario Biagioli: 2 → 1 (DeepSeek)
- Martha Nussbaum: 2 → 1 (DeepSeek)
- Nancy Cartwright: 2 → 1 (DeepSeek)
- Nelson Mandela: 5 → 4 (DeepSeek;Gemini;GPT;Grok)
- Niklas Luhmann: 2 → 1 (DeepSeek)
- Pamela Long: 2 → 1 (DeepSeek)
- Paul Edwards: 2 → 1 (DeepSeek)
- Peter Debye: 2 → 1 (DeepSeek)
- Peter Galison: 2 → 1 (DeepSeek)
- Peter Singer: 2 → 1 (DeepSeek)
- Philip Kitcher: 2 → 1 (DeepSeek)
- Pierre Duhem: 2 → 1 (DeepSeek)
- R.G. Collingwood: 2 → 1 (DeepSeek)
- Randall Collins: 2 → 1 (DeepSeek)
- Robert Merton: 2 → 1 (DeepSeek)
- Robert Putnam: 2 → 1 (DeepSeek)
- Ronald Numbers: 2 → 1 (DeepSeek)
- Sana'i: 2 → 1 (Gemini)
- Sandra Harding: 2 → 1 (DeepSeek)
- Seymour Martin Lipset: 2 → 1 (DeepSeek)
- Slavoj Zizek: 2 → 1 (DeepSeek)
- Thomas Hughes: 2 → 1 (DeepSeek)
- Thomas Nagel: 2 → 1 (DeepSeek)
- Tiruvalluvar: 2 → 1 (Gemini)
- Trevor Pinch: 2 → 1 (DeepSeek)
- Wiebe Bijker: 2 → 1 (DeepSeek)

## People added (not in v7.1)

898 new people: F=4: 1, F=3: 8, F=2: 74, F=1: 815. All have status `new — needs status`. Many are Claude-only names (Claude was never aggregated) or names cut by the 500-row truncation.

New people with F ≥ 3:

- Georg Wilhelm Friedrich Hegel — philosophy — F=4 (Claude;Gemini;GPT;Grok)
- Duns Scotus — philosophy — F=3 (Claude;DeepSeek;Grok)
- Edward O. Wilson — biology — F=3 (Claude;Gemini;GPT)
- John Nash — mathematics — F=3 (Claude;GPT;Grok)
- Jorge Luis Borges — literature — F=3 (Claude;Gemini;GPT)
- Laozi — philosophy — F=3 (Claude;DeepSeek;Gemini)
- Ludwig Mies van der Rohe — architecture — F=3 (Claude;DeepSeek;Gemini)
- Paul Cézanne — art — F=3 (Claude;Gemini;GPT)
- Vint Cerf — computer science — F=3 (Claude;DeepSeek;GPT)

New people with F = 2 (count by field bucket): mathematics 12, physics 10, arts 9, philosophy 8, social science 6, invention / engineering 6, computer science / AI 5, polymath 4, literature 4, politics / law / military 2, earth science 2, music 2, astronomy 1, psychology / neuroscience 1, linguistics 1, medicine 1.
New people with F = 1 (count by field bucket): physics 89, philosophy 86, social science 76, medicine 72, history 68, chemistry 62, mathematics 39, literature 39, arts 39, music 37, invention / engineering 37, biology / life science 35, politics / law / military 35, psychology / neuroscience 35, computer science / AI 26, astronomy 13, polymath 8, linguistics 8, exploration 5, earth science 4, other 2.

## People dropped / v7 rows that do not carry over as their own row

None. Every v7.1 roster person is found in the raw lists and kept.

## Exclusions applied

- Wilbur Wright / Wright Brothers - Wilbur Wright / Wright-Wilbur (Claude, Gemini): collective - one of the Wright Brothers (joint credit); excluded with 'Wright Brothers' by the operational definition as in v7.1; decided by Jason Burns 2026-10-01 (OPEN_DECISIONS R2)
- Orville Wright / Wright Brothers - Orville Wright / Wright-Orville (Claude, Gemini): collective - one of the Wright Brothers (joint credit); excluded with 'Wright Brothers' by the operational definition as in v7.1; decided by Jason Burns 2026-10-01 (OPEN_DECISIONS R2)
- Wright Brothers / Wright-Brothers (DeepSeek, GPT): collective/team - excluded by operational definition (same as v7)
- Anderson localization (DeepSeek): not a person (physics phenomenon) - same as v7; physicist Philip Anderson is listed separately
- v7 table 7 exclusions were Wright Brothers and Anderson localization; both are excluded again. Claude lists Wilbur and Orville Wright as two individuals (under a 'Wright Brothers - ' prefix); Gemini also lists them individually. Those individual entries are excluded too, as part of the collective (decision R2, 2026-10-01, rows in `curated_aliases.csv`).
- No other collectives or non-person entries were found in the raw lists (checked for 'brothers', 'and', '&', team/group/school/effect/theory etc.).

## Status carry-over

| Status | v8 count |
|---|---|
| new — needs status | 898 |
| core | 432 |
| provisional | 33 |
| review | 17 |

- Georgia O'Keeffe: status `core` from `status_overrides.csv` (v7 status: blank).
- No other statuses were set. v7 statuses are carried over as they are. Review reasons from v7 table 7 are copied into `v7_review_note`.

## Field buckets

Buckets are assigned by keyword rules in the script (first field component that matches). v7's own bucket table (table 8) used a hand mapping that is not in the repo, so the v7 column below is the v7 roster re-bucketed with the same rules, for a like-for-like comparison.

| Bucket | v8 N | v8 share | v7.1 N (same rules) | change |
|---|---|---|---|---|
| philosophy | 174 | 12.6% | 75 | +99 |
| physics | 134 | 9.7% | 33 | +101 |
| social science | 130 | 9.4% | 49 | +81 |
| history | 111 | 8.0% | 47 | +64 |
| medicine | 97 | 7.0% | 25 | +72 |
| mathematics | 91 | 6.6% | 38 | +53 |
| chemistry | 84 | 6.1% | 21 | +63 |
| literature | 82 | 5.9% | 39 | +43 |
| arts | 75 | 5.4% | 25 | +50 |
| invention / engineering | 63 | 4.6% | 19 | +44 |
| music | 56 | 4.1% | 17 | +39 |
| psychology / neuroscience | 55 | 4.0% | 19 | +36 |
| biology / life science | 53 | 3.8% | 18 | +35 |
| computer science / AI | 48 | 3.5% | 15 | +33 |
| politics / law / military | 48 | 3.5% | 12 | +36 |
| astronomy | 27 | 2.0% | 14 | +13 |
| polymath | 21 | 1.5% | 8 | +13 |
| linguistics | 12 | 0.9% | 3 | +9 |
| earth science | 9 | 0.7% | 2 | +7 |
| exploration | 8 | 0.6% | 3 | +5 |
| other | 2 | 0.1% | 0 | +2 |

Among F ≥ 3 (the primary analysis cut in the coding rules): philosophy 41, mathematics 34, literature 21, physics 19, arts 18, music 12, invention / engineering 11, computer science / AI 11, social science 10, biology / life science 10, medicine 9, astronomy 8, chemistry 8, polymath 7, psychology / neuroscience 7, linguistics 2, exploration 2, politics / law / military 1.

## Merges and review items

- Format merges (automatic): spacing, hyphens used as spaces, Gemini's 'Last-First' repeats, accents, initials, word order (Jr./Sr. are kept, so father and son stay separate). Each is listed in `alias_map.csv` (rule `format`).
- Display fixes that change the name itself, not just its formatting (rule `name_correction` in `alias_map.csv`, with the curated reason as the note): Albert Hofman → Albert Hofmann, Gabriel Marcell → Gabriel Marcel, Marcell-Gabriel → Gabriel Marcel, Gabriel Mistral → Gabriela Mistral, Mistral-Gabriel → Gabriela Mistral, Brian-Maynard-Smith → John Maynard Smith, Lee-Smolins → Lee Smolin, Gyatso-Tenzin-Dalai Lama → Tenzin Gyatso (14th Dalai Lama), Tenzin Gyatso-Dalai Lama → Tenzin Gyatso (14th Dalai Lama).
- Curated alias merges (hand list in `curated_aliases.csv`, all logged in `merge_log.csv`): Avicenna/Ibn Sina, Averroes/Ibn Rushd, Alhazen/Ibn al-Haytham, Al-Khwarizmi/Muhammad ibn Musa al-Khwarizmi, Al-Biruni, Al-Farabi/Farabi, Al-Razi/Razi, Laozi/Lao Tzu, Li Bai/Li Po, Buddha/Siddhartha Gautama, Rembrandt, Michelangelo, Leibniz, Hegel, Oppenheimer, E.O. Wilson, Spinoza (Benedict/Baruch), Anscombe, Kahn (Bob/Robert), Mies van der Rohe, Duns Scotus, Murasaki Shikibu, Kovalevskaya, Kolmogorov, Ben-Gurion, Noether, Hodgkin, Herschel (Caroline), Leavitt, Maimonides.
- Kept separate on purpose (name overlap, different people): George Washington / George Washington Carver, Muhammad (prophet) / al-Khwarizmi, Zeno of Elea / Zeno of Citium, the Curies and Joliot-Curies, the Leakeys, William / Caroline Herschel, Alan / Dorothy Hodgkin, W.H. / W.L. Bragg, Francis / Roger Bacon, Ken / E.P. Thompson, Edward Said / Edward Sapir, Marc / Maurice Bloch, and others in `alias_map.csv`.
- Display fix by decision R3 (2026-10-01): GPT's 'Brian-Maynard-Smith' is shown as John Maynard Smith; the raw string stays in `alias_map.csv`.
- Automatic similarity scan: no unreviewed pairs. Pairs a human has confirmed as different people are `separate` rows in `curated_aliases.csv` and are not listed again.

## Files

All roster files are in `data/roster/`.

- `roster.csv` — one row per person: rank, canonical name, field, bucket, F, band, which models, status, v7 name/F/status, F change, aliases, per-model fields, notes.
- `alias_map.csv` — every raw name string (per model) → canonical name, with rule and confidence; plus keep-separate and flag rows.
- `merge_log.csv` — every merge, same-model duplicate, exclusion, and the not-merged similarity pairs.
- `curated_aliases.csv` — the hand decisions the script reads (edit and re-run to change merges).
- `scripts/rebuild_roster.py` — the script. `python3 scripts/rebuild_roster.py` regenerates all outputs; `--check` confirms the committed files are reproduced exactly.
