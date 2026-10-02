# data/reference

Reference tables that coders and validators read. Hand-maintained; change them only through a decision in `docs/OPEN_DECISIONS.md`.

## regions.csv

Country-to-region table for `basics.region_of_birth` and `basics.region_of_work` (decision P3, 2026-10-01).

- Source: UN M49 standard country or area codes, overview table, https://unstats.un.org/unsd/methodology/m49/overview/ (read 2026-10-01). 247 countries or areas; Antarctica has no M49 region and is left out.
- Each row maps an M49 sub-region to one of the 13 study regions (column `rule` says how):
  - Northern, Western, Southern and Eastern Europe, Central Asia, Sub-Saharan Africa, Northern America (→ North America), Latin America and the Caribbean, Eastern Asia (→ East Asia), South-eastern Asia (→ Southeast Asia) and Southern Asia (→ South Asia) map one to one.
  - Australia and New Zealand, Melanesia, Micronesia and Polynesia → Oceania.
  - M49 has no "Middle East and North Africa". The study region is M49 Northern Africa plus M49 Western Asia. Western Asia includes Armenia, Azerbaijan, Georgia, Cyprus and Türkiye, so they are MENA here too.
  - One exception: Iran → Middle East and North Africa (M49: Southern Asia).
  - Afghanistan stays in South Asia, as in M49. So someone born at Balkh (for example Rumi) has `region_of_birth` South Asia, and the work region follows where the work was done.
- Use modern borders. A place that is not its own row in M49 (Taiwan, Kosovo) takes the region of the M49 sub-region it lies in (Taiwan → East Asia, Kosovo → Southern Europe). The historical polity goes in `place.polity_then`, not in the region.

`scripts/validate_people.py` checks that every `study_region` in the table is one of the schema's region values and that each schema value is used at least once.
