# Period rule sensitivity (2026-10-02)

This report shows how much the coded worldview values depend on one method choice: what to do with evidence from outside a person's working years (`timing.major_work_period`, which `worldview.working_years` equals).

- **The rule in use, P31 (continuity rule).** Evidence from any adult year counts for the period at its normal certainty, unless `changes_over_life` documents a change of view between the period and the evidence. A change splits the period only if it bears on `primary_system` or A–E. Every value in the records follows this rule.
- **The strict reading, P29's original clause** (superseded by P31). Statements from outside the period count only as retrospective self-reports (0.7 cap, or 0.5 if hedged) or go in `changes_over_life`. A statement written later in the tense of its writing is not a retrospective self-report, so under this reading it drops out.

The comparison covers the 31 records outside stage 3, after the period alignment of 7a52a3f. The 12 stage 3 records are not included. Source of the rows: the span audit (`reports/p30_span_alignment.csv`), where each row also carries its P31 resolution.

## Result

- **55 values in 13 records** would change under the strict reading: B_cause 10, D_authority 10, A_locus 9, mid_basin 8, primary_system 7, E_scope 6, C_ledger 5. 34 of them would become BELOW_THRESHOLD or UNKNOWN outright; most of the rest would drop to 0.5 or depend on a further call. The full list is in [`period_rule_sensitivity.csv`](period_rule_sensitivity.csv).
- **Passes:** mid_basin would flip for 2 of the 8 passes (Boyle and Gödel, true → BELOW_THRESHOLD); Faraday and Newton would flip only if A's certainty fell below 0.7; Aquinas, Galileo, Ibn Sina and Maxwell are unaffected.
- 18 records have no value that depends on the choice.
- Four more rows were borderline in the audit (Bohr C and D, Faraday C and E, Kepler A, D and primary_system, Newton B) and are not counted; they would probably not change under either reading.

The main reason for the gap is that most people state their worldview late in life: for Boyle, Einstein and Pauling all of the worldview evidence read is dated after the period.

## By record

| record | period | values that would change | evidence outside the period (main items) |
|---|---|---|---|
| Boyle (pass) | 1659–1666 | 7: primary_system CHRIST 0.7; A_locus 0 at 0.7; B_cause 3 at 0.7; C_ledger 0 at 0.7; D_authority 2 at 0.7; E_scope 3 at 0.7; mid_basin true at 0.7 (pass) | Free Enquiry (1686), Christian Virtuoso (1690) |
| Einstein | 1905–1925 | 7: primary_system PANT 0.7; A_locus 4 at 0.7; B_cause 4 at 0.7; C_ledger 4 at 0.7; D_authority 2 at 0.7; E_scope 4 at 0.7; mid_basin false at 0.7 | 1929 cable; essays of 1930, 1939, 1941 |
| Faraday (pass) | 1821–1850 | 5: primary_system CHRIST 0.7; A_locus 0 at 0.7; B_cause 3 at 0.7; D_authority 2 at 0.7; mid_basin true at 0.7 (pass) | 1854 lecture, 1857 discourse, 1861 letter, letters of his last years, 1862 evidence |
| Gödel (pass) | 1929–1958 | 6: A_locus 1 at 0.7; B_cause 3 at 0.7; C_ledger 3 at 0.5; D_authority 3 at 0.7; E_scope 3 at 0.5; mid_basin true at 0.7 (pass) | letters of 1961, ontological proof (1970), questionnaire (1974–75), list (c. 1960) |
| Heisenberg | 1925–1932 | 4: A_locus 2 at 0.7; B_cause 4 at 0.7; D_authority 2 at 0.7; mid_basin TODO | Guardini Prize lecture (1973) |
| Herschel | 1783–1828 | 2: primary_system CHRIST 0.5; A_locus 0 at 0.5 | letters of 1829 and 1835 |
| Hubble | 1923–1936 | 2: B_cause 4 at 0.7; D_authority 2 at 0.7 | Caltech address (1938), 'The Nature of Science' (1948) |
| Mendeleev | 1869–1871 | 1: B_cause 4 at 0.7 | lectures against spiritualism (1876) |
| Newton (pass) | 1665–1704 | 6: primary_system CHRIST 0.7; A_locus 1 at 1.0; C_ledger 0 at 0.7; D_authority 2 at 0.7; E_scope 3 at 0.7; mid_basin true at 0.7 (pass) | General Scholium (1713), Query 31 (1717), private manuscripts after 1710 |
| Pauling | 1931–1951 | 7: primary_system SECHUM 0.7; A_locus 4 at 0.7; B_cause 4 at 0.7; C_ledger 4 at 0.7; D_authority 4 at 0.7; E_scope 4 at 0.7; mid_basin false at 0.7 | 'Humanism and Peace' (1961), letter (1963) |
| Planck | 1879–1900 | 6: primary_system DEISM 0.5; A_locus 2 at 0.7; B_cause 4 at 0.7; D_authority 2 at 0.7; E_scope 4 at 0.7; mid_basin TODO | lectures of 1933 and 1937, letter (1947) |
| Schrödinger | 1926–1944 | 1: D_authority 3 at 0.5 | Mind and Matter (1958) |
| Curie | 1898–1910 | 1: B_cause 4 at 0.7 | Pierre Curie (1923); a letter of 1887, before the period |

Values in the table are the current (P31) values. The strict value for each, and the cited evidence, are in the CSV.

## Files

- `reports/period_rule_sensitivity.csv`: one row per value. Columns: record, pass_record, period, field, p31_value (the value in the record), strict_value (the value under P29's original clause, as the audit gave it; some name two outcomes), evidence_outside_period.
- `reports/p30_span_alignment.csv`: the span audit, with every row's P31 resolution.
- `docs/OPEN_DECISIONS.md`, P29 and P31: the two rules.
