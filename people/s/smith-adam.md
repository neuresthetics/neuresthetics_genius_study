---
record:
  record_type: person
  schema_version: "1.3"
  record_version: 1
  review_status: "draft — unreviewed"
  collected_by: "Grok Bot (agent run for Jason, stage 3 batch C)"
  model_used: "Grok Bot executor agent; web search plus direct reads of the cited pages"
  collected_on: 2026-10-08
  last_updated: 2026-10-08
  change_log:
    - {date: 2026-10-08, by: "Grok Bot", summary: "Record created (stage 3 batch C, order P32). Basics from Britannica (Heilbroner) and SEP (Fleischacker); worldview from The Theory of Moral Sentiments, 6th edition (1790), read on the archive.org scan of the 1790 printing (vol. 1 pp. 412–415; vol. 2 pp. 113–118). Not a scientist (P30). primary_system BELOW_THRESHOLD (candidates CHRIST, STOIC, CLASS_THEISM; DEISM rejected under P27); A_locus 1 (0.5); B_cause 4 (0.5); E_scope 4 (0.5); C, D BELOW_THRESHOLD; mid_basin BELOW_THRESHOLD. Draft, not reviewed."}
    - {date: 2026-10-08, by: "Grok Bot", summary: "Lens audit of batch C (dd91009), run 1: #6 A_locus 1 → 0 at 0.5, alternative 1 (no limiting feature named; Boyle pattern). #4 B_cause 4 → 3 at 0.5, alternative 4, re-anchored on vol. 1 pp. 412–415 (laws of motion; general rules of reward; 'extraordinary favour' as the stated exception), with vol. 2 pp. 114–115 as context; two vol. 1 statements added. mid_basin unchanged (BELOW_THRESHOLD)."}

identity:
  id: smith-adam
  display_name: "Adam Smith"
  roster:
    canonical_name: "Adam Smith"
    rank: 2
    F: 5
    models: [Claude, DeepSeek, Gemini, GPT, Grok]
    band: "high (5)"
    status: core
    field: economics
    field_bucket: "social science"
  full_name: {value: "Adam Smith", certainty: 1.0, cites: [{source: S1, locator: "heading"}, {source: S2, locator: "title"}, {source: S3, locator: "title page"}], how_known: "Three sources."}
  native_name: {value: "Adam Smith", certainty: 1.0, cites: [{source: S3, locator: "title page ('By Adam Smith')"}], how_known: "His own title page."}
  aliases:
    - {name: "Adam-Smith", kind: "roster alias"}
    - {name: "Smith-Adam", kind: "roster alias"}

basics:
  birth:
    date: {value: "1723", certainty: 0.7, cites: [{source: S1, locator: "Baptized line ('baptized June 5, 1723')"}], how_known: "Only the baptism date is recorded (5 June 1723, Britannica); the birth day is not known, so the year only. Britannica alone gives the date, so 0.7 (P15). Scotland still used the Julian calendar in 1723; Britannica does not say which style it gives."}
    place: {value: "Kirkcaldy, Fife, Scotland", modern_name: "Kirkcaldy, Scotland, UK", polity_then: "Kingdom of Great Britain", certainty: 0.7, cites: [{source: S1, locator: "Baptized line"}], how_known: "Britannica alone (P15)."}
  death:
    date: {value: "1790-07-17", calendar: gregorian, certainty: 0.7, cites: [{source: S1, locator: "Died line"}], how_known: "Britannica alone (P15); after 1752, so Gregorian."}
    place: {value: "Edinburgh", modern_name: "Edinburgh, Scotland, UK", polity_then: "Kingdom of Great Britain", certainty: 0.7, cites: [{source: S1, locator: "Died line"}], how_known: "Britannica alone (P15)."}
  first_lasting_contribution_year: {value: 1759, certainty: 1.0, cites: [{source: S1, locator: "Glasgow section (1759)"}, {source: S2, locator: "opening ('Theory of Moral Sentiments (1759, TMS)')"}], how_known: "The Theory of Moral Sentiments, published 1759 (P30). Two sources."}
  era_bucket: {value: "1750 to 1849", certainty: 1.0, cites: [{source: S2, locator: "opening"}], how_known: "From 1759 under P2."}
  region_of_birth: {value: "Northern Europe", certainty: 1.0, cites: [{source: S1, locator: "Baptized line"}, {source: S2, locator: "§1 (Scottish Enlightenment context)"}], how_known: "UK is Northern Europe in data/reference/regions.csv (P3)."}
  region_of_work: {value: "Northern Europe", certainty: 1.0, cites: [{source: S1, locator: "Glasgow and Edinburgh sections"}, {source: S3, locator: "title page (Edinburgh)"}], how_known: "Glasgow, Kirkcaldy and Edinburgh."}
  sex_as_recorded: {value: "male", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "throughout"}], how_known: "As the sources record it."}
  languages_of_work: {value: [English], certainty: 1.0, cites: [{source: S3, locator: "title page"}, {source: S2, locator: "throughout"}], how_known: "His books are in English."}
  occupations: {value: ["moral philosopher", "economist", "university professor"], certainty: 1.0, cites: [{source: S1, locator: "opening; Glasgow section"}, {source: S2, locator: "opening"}], how_known: "Two sources."}

contribution:
  fields: {value: ["moral philosophy", "political economy"], certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "opening"}], how_known: "Two sources."}
  lasting_original_contributions:
    - {value: "The Theory of Moral Sentiments: moral judgement explained through sympathy and the impartial spectator", year: "1759", kind: theory, lasting: "a standard text of moral philosophy, now read alongside WN (S2)", certainty: 1.0, cites: [{source: S1, locator: "Glasgow section"}, {source: S2, locator: "opening; §2"}], how_known: "Two sources."}
    - {value: "An Inquiry into the Nature and Causes of the Wealth of Nations: division of labour, the market order and the case against mercantilism", year: "1776", kind: theory, lasting: "founding text of classical economics", certainty: 1.0, cites: [{source: S1, locator: "The Wealth of Nations section"}, {source: S2, locator: "opening; §5"}], how_known: "Two sources."}
    - {value: "The Theory of Moral Sentiments, 6th edition, with the new Part VI on the character of virtue", year: "1790", kind: work, lasting: "the standard text of TMS; Part VI 'added in the last edition' (S2)", certainty: 1.0, cites: [{source: S3, locator: "title page ('The Sixth Edition, with considerable additions and corrections', 1790)"}, {source: S2, locator: "§2 (Part VI)"}], how_known: "The printed book and SEP."}
  evidence_of_impact:
    - {value: "Wealth of Nations is treated as the foundation of modern economics", kind: "scholarly consensus", certainty: 0.7, cites: [{source: S1, locator: "opening"}], how_known: "Britannica."}
  major_works:
    - {value: "The Theory of Moral Sentiments", year: 1759, kind: book, certainty: 1.0, cites: [{source: S1, locator: "Glasgow section"}, {source: S2, locator: "opening"}], how_known: "Two sources."}
    - {value: "An Inquiry into the Nature and Causes of the Wealth of Nations", year: 1776, kind: book, certainty: 1.0, cites: [{source: S1, locator: "WN section"}, {source: S2, locator: "opening"}], how_known: "Two sources."}
  honours: []
  definition_fit: {value: "clearly meets", rationale: "Founder of classical political economy and author of a lasting moral theory.", certainty: 1.0, cites: [{source: S1, locator: "opening"}, {source: S2, locator: "opening"}], how_known: "Two sources."}

childhood:
  family_religion: {value: TODO}
  family_religious_practice: {value: TODO}
  parents_and_household:
    - {value: "Father, also Adam Smith, a comptroller of customs, died about five months before he was born", role: father, certainty: 0.7, cites: [{source: S1, locator: "Early life"}], how_known: "Britannica alone (P15)."}
    - {value: "Brought up by his mother, Margaret Douglas", role: mother, certainty: 0.7, cites: [{source: S1, locator: "Early life"}], how_known: "Britannica alone (P15)."}
  household_circumstances: {value: TODO}
  schooling:
    - {value: "Burgh school of Kirkcaldy", stage: "grammar or secondary school", run_by: "state or municipal", certainty: 0.7, cites: [{source: S1, locator: "Early life"}], how_known: "Britannica alone (P15)."}
    - {value: "University of Glasgow, under Francis Hutcheson", stage: university, run_by: other, years: "1737–1740", ages: "14–17", certainty: 0.7, cites: [{source: S1, locator: "Early life (entered at 14 in 1737)"}], how_known: "Britannica alone (P15)."}
    - {value: "Balliol College, Oxford, as a Snell Exhibitioner", stage: university, run_by: other, years: "1740–1746", ages: "17–23", certainty: 0.7, cites: [{source: S1, locator: "Early life"}], how_known: "Britannica alone (P15)."}
  early_mathematics: {value: TODO}
  early_geometric_style_reasoning: {value: TODO}
  early_science_exposure: []
  key_early_reading: []
  childhood_mentors: []
  languages_in_childhood: {value: TODO}
  notable_events: []

worldview:
  unit: "adult working worldview"
  working_years: {value: "1759–1790", certainty: 1.0, cites: [{source: S2, locator: "opening; §2"}, {source: S3, locator: "title page"}], how_known: "Equals timing.major_work_period (P29, P30)."}
  nominal_affiliations: []
  self_described_science_religion_relation: {value: UNKNOWN, how_known: "No statement of his on science and religion as such was read. TMS compares moral rules with 'the laws of motion' (vol. 1, pp. 412–413) but that is a remark on the word 'law', not on science and religion."}
  primary_system:
    value: BELOW_THRESHOLD
    note: "His 1790 text speaks of 'that great, benevolent, and all-wise Being, who directs all the movements of nature' and of resignation to 'the great Conductor of the universe' (vol. 2, pp. 114, 117), and calls moral rules 'the commands and laws of the Deity' (vol. 1, p. 412). SEP reads him as anticipating 'Kant's moral argument for belief in God, without ever quite saying that there is a God' (§2), and much of the language is framed as what the virtuous man must be 'convinced' of or what 'the idea of' God gives. No source read settles whether this is his own creed. Draft judgment (one line): not coded; candidates CHRIST, STOIC and CLASS_THEISM."
    how_known: "BELOW_THRESHOLD under P19: evidence exists but no code clears 0.5 over its rivals."
  secondary_system: {value: UNKNOWN, how_known: "No second system."}
  candidate_codes_considered:
    - {code: CHRIST, reason: "Nominal background and providential language. Against: nothing read mentions Christ, scripture or church; SEP stresses his hostility to religion that puts 'ritual or creed over morality' (§2).", cites: [{source: S2, locator: "§2"}]}
    - {code: STOIC, reason: "Resignation to the 'great Director of the universe' and the soldier on the 'forlorn station' (vol. 2, pp. 116–117), with Marcus Antoninus as the model (p. 118); SEP notes 'a strong Stoic component to TMS'. Against: he distances himself from Stoic indifference elsewhere (not read here) and the text is framed as moral psychology.", cites: [{source: S3, locator: "vol. 2, pp. 116–118"}, {source: S2, locator: "§5 ('There is a strong Stoic component to TMS')"}]}
    - {code: CLASS_THEISM, reason: "An all-wise, benevolent Being who 'contrived and conducted the immense machine of the universe' (vol. 2, pp. 117–118). Against: same caution as SEP's.", cites: [{source: S3, locator: "vol. 2, pp. 117–118"}]}
    - {code: DEISM, reason: "Rejected under P27: DEISM needs a rejection of revelation, and nothing read rejects it.", cites: [{source: S3, locator: "vol. 2, pp. 113–118"}]}
  lio_axes:
    A_locus:
      value: 0
      basis: written_profession
      certainty: 0.5
      cites: [{source: S3, locator: "vol. 2, pp. 114, 115, 117–118"}, {source: S2, locator: "§2"}]
      how_known: "His own published book. Held at 0.5, below the basis ceiling: SEP's caution ('without ever quite saying that there is a God') and the conditional framing make the attribution contested (coder's call, CODING_GUIDE §8)."
      rationale: "Draft judgment (one line): God is a governor over the universe, 'the immediate administrator and director' of 'that great society of all sensible and intelligent beings' (p. 115), 'the great Conductor of the universe' (p. 117), who has 'contrived and conducted the immense machine of the universe' (pp. 117–118): a designer of a machine and a commander outside it, the Boyle pattern, so 0 (lens audit of batch C, #6). No feature that limits the pole (an immanence or presence in nature) is named in the text read; 'directs all the movements of nature' (p. 114) is governance, not locus. Named alternative: 1, if that continual direction is read as a presence in nature."
    B_cause:
      value: 3
      basis: written_profession
      certainty: 0.5
      cites: [{source: S3, locator: "vol. 1, pp. 412–415; vol. 2, pp. 114–115 (context)"}]
      how_known: "His own published book, a statement about nature (P16). Held at 0.5 for the same contested-attribution reason as A. Re-anchored on vol. 1 (lens audit of batch C, #4); the vol. 2 theodicy passages are context only."
      rationale: "Draft judgment (one line): nature runs by general rules: 'the general rules which bodies observe in the communication of motion, are called the laws of motion' (vol. 1, pp. 412–413), and under 'the general rules by which external prosperity and adversity are commonly distributed in this life' 'every virtue naturally meets with its proper reward', so surely 'that it requires a very extraordinary concurrence of circumstances entirely to disappoint it' (p. 415). One stated, limited exception: we are 'encouraged to hope for his extraordinary favour and reward' (pp. 414–415), a particular providence beside the general rules, so 3 (coder's call). Named alternative: 4, if the 'extraordinary favour' is read as the afterlife (scored on C), not as an exception in nature."
    C_ledger: {value: BELOW_THRESHOLD, note: "Mixed: moral faculties 'never fail to punish the violation' of their rules 'by the torments of inward shame' (vol. 1, p. 413) and 'every virtue naturally meets with its proper reward' in this life (p. 415), but we are 'encouraged to hope for his extraordinary favour and reward' and 'to dread his vengeance and punishment' (pp. 414–415). SEP reads the afterlife passages as moral psychology (§2). Draft judgment (one line): too mixed to score.", how_known: "BELOW_THRESHOLD under P19."}
    D_authority: {value: BELOW_THRESHOLD, note: "Moral rules are 'the commands and laws of the Deity, promulgated by those vicegerents which he has thus set up within us' (vol. 1, p. 412): authority in conscience, not scripture. Nothing read on revelation itself. Draft judgment (one line): too indirect to score.", how_known: "BELOW_THRESHOLD under P19."}
    E_scope:
      value: 4
      basis: written_profession
      certainty: 0.5
      cites: [{source: S3, locator: "vol. 2, pp. 114–115"}]
      how_known: "His own published book; held at 0.5 for the contested attribution."
      rationale: "Scored on the world's order (P7). 'All the inhabitants of the universe, the meanest as well as the greatest, are under the immediate care and protection' of God (p. 114); the wise man sacrifices lesser interests 'to the greater interest of the universe, to the interest of that great society of all sensible and intelligent beings' (p. 115). One order for all, no favoured people. Named alternative: 3, since the passage is about rational and sensible beings, not all of nature."
  mid_basin: {value: BELOW_THRESHOLD, how_known: "A_locus 0 and B_cause 3 are both scored only at 0.5, so the P4 test is not met (§6, P19)."}
  statements:
    - text: "This universal benevolence, how noble and generous soever, can be the source of no solid happiness to any man who is not thoroughly convinced that all the inhabitants of the universe, the meanest as well as the greatest, are under the immediate care and protection of that great, benevolent, and all-wise Being, who directs all the movements of nature; and who is determined, by his own unalterable perfections, to maintain in it, at all times, the greatest possible quantity of happiness."
      cites: [{source: S3, locator: "vol. 2, p. 114 (Part VI, sect. II, ch. III; Glasgow VI.ii.3.2)"}]
      date: "1790"
      context: "Part VI, new in the 6th edition: 'Of universal Benevolence'."
      axes: [A_locus, B_cause, E_scope]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-08
    - text: "If he is deeply impressed with the habitual and thorough conviction that this benevolent and all-wise Being can admit into the system of his government, no partial evil which is not necessary for the universal good, he must consider all the misfortunes which may befal himself, his friends, his society, or his country, as necessary for the prosperity of the universe"
      cites: [{source: S3, locator: "vol. 2, p. 115"}]
      date: "1790"
      context: "Same chapter, following 'of which God himself is the immediate administrator and director'."
      axes: [B_cause, E_scope]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-08
    - text: "No conductor of an army can deserve more unlimited trust, more ardent and zealous affection, than the great Conductor of the universe."
      cites: [{source: S3, locator: "vol. 2, p. 117"}]
      date: "1790"
      context: "The soldier on the 'forlorn station' as the model of resignation."
      axes: [A_locus]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-08
    - text: "The idea of that divine Being, whose benevolence and wisdom have, from all eternity, contrived and conducted the immense machine of the universe, so as at all times to produce the greatest possible quantity of happiness, is certainly of all the objects of human contemplation by far the most sublime."
      cites: [{source: S3, locator: "vol. 2, pp. 117–118"}]
      date: "1790"
      context: "Leads into Marcus Antoninus' Meditations as the model."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-08
    - text: "The happiness of mankind, as well as of all other rational creatures, seems to have been the original purpose intended by the Author of nature, when he brought them into existence."
      cites: [{source: S3, locator: "vol. 1, pp. 413–414 (Part III, ch. V)"}]
      date: "1790"
      context: "'Of the influence and authority of the general Rules of Morality, and that they are justly regarded as the Laws of the Deity'. The chapter was in earlier editions, but only the 1790 text was read."
      axes: [A_locus, B_cause]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-08
    - text: "All general rules are commonly denominated laws: thus the general rules which bodies observe in the communication of motion, are called the laws of motion."
      cites: [{source: S3, locator: "vol. 1, pp. 412–413 (Part III, ch. V)"}]
      date: "1790"
      context: "Same chapter: moral rules are more justly called laws than the laws of motion."
      axes: [B_cause]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-08
      note: "Checked on the archive.org OCR of the vol. 1 scan (running heads 'Chap. V. of Duty. 413'); page image not viewed."
    - text: "Hence we are naturally encouraged to hope for his extraordinary favour and reward in the one case, and to dread his vengeance and punishment in the other. There are besides many other reasons, and many other natural principles, which all tend to confirm and inculcate the same salutary doctrine. If we consider the general rules by which external prosperity and adversity are commonly distributed in this life, we shall find, that notwithstanding the disorder in which all things appear to be in this world, yet even here every virtue naturally meets with its proper reward, with the recompense which is most fit to encourage and promote it; and this too so surely, that it requires a very extraordinary concurrence of circumstances entirely to disappoint it."
      cites: [{source: S3, locator: "vol. 1, pp. 414–415 (Part III, ch. V)"}]
      date: "1790"
      context: "Same chapter, after acting against the moral rules is said to 'obstruct, in some measure, the scheme which the Author of nature has established'."
      axes: [B_cause, C_ledger]
      kind: "written profession (public)"
      verified_against: "primary facsimile"
      verified_on: 2026-10-08
      note: "Checked on the archive.org OCR of the vol. 1 scan; the page turns after 'encouraged' (p. 415 begins 'to hope'); line-end hyphens removed; page image not viewed."
  changes_over_life: []
  coder_notes: "Long s normalised silently in all quotations. Quotations were taken from the archive.org OCR and checked by eye against the page images of vol. 2 pp. 114 and 117 (PDF pages 122 and 125); page numbers are those printed in the 1790 volumes. Coder's call (CODING_GUIDE §8): A, B and E held at 0.5 despite a written_profession basis, because SEP (§2) says he never 'quite' says there is a God and the key passages are framed as what a virtuous man must be convinced of; the conservative option is taken. The Wealth of Nations was not read for worldview. Not a scientist (P30): his lasting work is moral philosophy and economics."

heritage:
  use: "context only — never an outcome and never a worldview code"
  ethnic_or_communal_heritage: {value: "Scottish; son of a customs official", certainty: 0.7, cites: [{source: S1, locator: "Early life"}], how_known: "Britannica."}
  religious_heritage_by_birth: {value: TODO}
  baptism_or_initiation: {value: "Baptized 5 June 1723 at Kirkcaldy", certainty: 0.7, cites: [{source: S1, locator: "Baptized line"}], how_known: "Britannica alone; the church is not named there."}
  childhood_catechism: {value: TODO}

timing:
  lane: "A — descriptive facts; Lane B's H1 timing test reads them"
  major_work_period: {value: "1759–1790", certainty: 1.0, cites: [{source: S2, locator: "opening; §2"}, {source: S3, locator: "title page"}], how_known: "TMS (1759) to TMS 6th edition with Part VI (1790), which is also the year he died (P29, P30)."}
  age_at_first_lasting_contribution: {value: 36, certainty: 0.7, cites: [{source: S1, locator: "Baptized line; Glasgow section"}, {source: S2, locator: "opening"}], how_known: "1759 − 1723 = 36 (P30); birth year from the baptism record, Britannica alone, so 0.7."}
  first_evidence_of_lio_type_views: {value: "TMS 6th edition: God 'determined, by his own unalterable perfections, to maintain' the greatest happiness in nature (E_scope 4); the general rules of vol. 1, pp. 412–415 (B_cause 3)", year: 1790, age: 67, certainty: 0.5, cites: [{source: S3, locator: "vol. 2, p. 114; vol. 1, pp. 413–414"}], how_known: "The earliest dated text read with statements scored at 3 or 4 (P27). The 1759 first edition was not read ('earlier works not read'), though the Part III chapter quoted appears to go back to it, so 0.5."}
  lio_views_relative_to_major_work: {value: "during major work", rationale: "The 1790 edition is the last item of the 1759–1790 period; earlier editions were not read.", certainty: 0.5, cites: [{source: S3, locator: "title page"}, {source: S2, locator: "§2"}], how_known: "Dated texts only."}
  worldview_during_major_work: {value: "Providential theism in TMS language (God as all-wise 'Conductor' of a system maximising happiness), which SEP treats as moral psychology rather than a stated creed", certainty: 0.5, cites: [{source: S3, locator: "vol. 2, pp. 114–118"}, {source: S2, locator: "§2"}], how_known: "His text plus SEP's caution."}

lane_b:
  label: "Lane B — labeled belief model, not a finding"
  geometric_form_present: {value: "no", rationale: "TMS and WN argue from observation, history and moral psychology, not from definitions and axioms.", certainty: 0.5, cites: [{source: S2, locator: "§1 (methodology)"}], how_known: "Coder's reading of SEP's account of his method."}
  form_acquired: {value: "unclear", certainty: 0.5, cites: [{source: S1, locator: "Early life"}], how_known: "Nothing read on mathematics at school."}
  circle_present: {value: "partly", rationale: "God and nature are tied through one designed system ('directs all the movements of nature'), but God remains its external 'Conductor'.", certainty: 0.5, cites: [{source: S3, locator: "vol. 2, pp. 114, 117"}], how_known: "Coder's reading."}
  reading: "As belief, not finding: form absent, circle partly present."
  notes: ""

institutions:
  - {value: "University of Glasgow", role: "professor of logic (1751), then of moral philosophy (1752)", years: "1751–", kind: university, certainty: 0.7, cites: [{source: S1, locator: "Glasgow section"}], how_known: "Britannica (P15)."}
collaborators:
  - {value: "Francis Hutcheson", relation: teacher, note: "Glasgow", certainty: 1.0, cites: [{source: S1, locator: "Early life"}, {source: S2, locator: "§1 ('his teacher, Frances Hutcheson')"}], how_known: "Britannica; SEP §1 also calls Hutcheson 'his teacher'. Two sources."}
  - {value: "David Hume (hume-david)", relation: collaborator, note: "close friend", certainty: 1.0, cites: [{source: S1, locator: "Glasgow section"}, {source: S2, locator: "§2 ('like Shaftesbury and Hume')"}], how_known: "Britannica for the friendship; SEP for the intellectual tie."}
  - {value: "James Watt (watt-james)", relation: correspondent, note: "friend at Glasgow", certainty: 0.7, cites: [{source: S1, locator: "Glasgow section"}], how_known: "Britannica (P15); 'correspondent' is the nearest relation value for a friend."}

review:
  roster_status_reason: {value: "Core in v8 (F 5: Claude, DeepSeek, Gemini, GPT, Grok).", certainty: 0.7, cites: [{source: S4, locator: "roster.csv, rank 2"}], how_known: "Study roster."}
  controversies: []
  data_quality_flags:
    - "Britannica could not be re-read on 2026-10-08 (Cloudflare check); its facts were taken from an earlier read the same day. Locators are section names, not paragraph numbers."
    - "Birth: baptism date only (5 June 1723), style not stated."
  open_questions:
    - "Read the 1759 first edition for the Part III chapter and any variants; read the Glasgow edition apparatus on the 1790 changes to religious passages."

sources:
  - id: S1
    type: tertiary
    kind: encyclopedia
    author: "Robert L. Heilbroner"
    citation: "Heilbroner, Robert L. \"Adam Smith.\" Encyclopaedia Britannica. https://www.britannica.com/biography/Adam-Smith."
    url: "https://www.britannica.com/biography/Adam-Smith"
    accessed: 2026-10-08
    reliability_note: "Signed encyclopedia article."
    used_for: [identity, basics, contribution, childhood, heritage, timing, institutions, collaborators]
  - id: S2
    type: secondary
    kind: encyclopedia
    author: "Samuel Fleischacker"
    year: 2025
    citation: "Fleischacker, Samuel. \"Adam Smith's Moral and Political Philosophy.\" Stanford Encyclopedia of Philosophy, first published 15 February 2013, substantive revision 29 May 2025. https://plato.stanford.edu/entries/smith-moral-political/."
    url: "https://plato.stanford.edu/entries/smith-moral-political/"
    accessed: 2026-10-08
    reliability_note: "Peer-reviewed reference article by a leading Smith scholar."
    used_for: [identity, basics, contribution, worldview, timing, lane_b, collaborators]
  - id: S3
    type: primary
    kind: "published work by the subject"
    author: "Adam Smith"
    year: 1790
    citation: "Smith, Adam. The Theory of Moral Sentiments. The Sixth Edition, with considerable additions and corrections. 2 vols. London: A. Strahan and T. Cadell; Edinburgh: W. Creech and J. Bell, 1790. Scan: archive.org, bim_eighteenth-century_the-theory-of-moral-sent_smith-adam_1790_1 and _2."
    url: "https://archive.org/details/bim_eighteenth-century_the-theory-of-moral-sent_smith-adam_1790_2"
    accessed: 2026-10-08
    reliability_note: "Facsimile of the 1790 printing (the last edition in his lifetime); OCR checked against page images for quoted passages."
    used_for: [identity, basics, contribution, worldview, timing, lane_b]
  - id: S4
    type: secondary
    kind: database
    author: "Neuresthetics Genius Study"
    citation: "Neuresthetics Genius Study. data/roster/roster.csv (v8 roster)."
    url: "https://github.com/neuresthetics/neuresthetics_genius_study/blob/main/data/roster/roster.csv"
    accessed: 2026-10-08
    reliability_note: "Study's own roster; used only for rank, F and status."
    used_for: [identity, review]
---

# Adam Smith

> Status: draft — unreviewed. Cite every factual sentence with a source id from the front matter, like `[S1, p. 12]`.

## Summary

Adam Smith (1723–1790), Scottish moral philosopher and founder of classical economics, wrote The Theory of Moral Sentiments (1759) and The Wealth of Nations (1776) [S1; S2]. The 1790 sixth edition of TMS speaks of an all-wise Being 'who directs all the movements of nature' and of 'the great Conductor of the universe' [S3, vol. 2, pp. 114, 117], though SEP notes he never 'quite' says there is a God [S2, §2]. Draft: primary_system BELOW_THRESHOLD; A 0, B 3, E 4, all at 0.5; mid_basin BELOW_THRESHOLD.

## Life and work

Baptized at Kirkcaldy in 1723; Glasgow under Hutcheson and Balliol, Oxford; professor at Glasgow from 1751; died in Edinburgh in 1790 [S1].

## Contribution and impact

TMS (1759), WN (1776), TMS 6th edition (1790) [S1; S2; S3].

## Childhood and education

Father died before his birth; burgh school of Kirkcaldy; Glasgow at 14 [S1].

## Adult working worldview

Providential language throughout TMS [S3]; SEP's caution [S2, §2]. Scores held at 0.5.

## Heritage (context only)

Scottish [S1].

## Timing

First lasting contribution 1759, age 36. First LIO-type view read: 1790 (0.5; earlier works not read).

## Lane B notes (labeled belief model)

Everything in this section is Lane B: labeled belief, not a finding. Form absent; circle partly [S2; S3].

## Open questions

- The 1759 first edition.

## Research log

- 2026-10-08: Read Britannica (Heilbroner), SEP (Fleischacker 2025), and TMS 1790 on the archive.org scans (vol. 1 Part III ch. V; vol. 2 Part VI sect. II ch. III). The Liberty Fund (OLL) text was blocked (CloudFront 403); ECCO-TCP was blocked (Cloudflare).
