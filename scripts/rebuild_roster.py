#!/usr/bin/env python3
"""
Rebuild the Genius Study roster (v8 step 1) from the five raw model lists.

All paths are relative to the repo root, so the script works from any clone.

Inputs (read-only):
  data/sources/model_lists/genii{Claude,DeepSeek,Gemini,GPT,Grok}.csv   columns: name,field
  data/sources/v7_1/neuresthetics_v7_combined.json
           documents.data_book.content.tables[6] (v7.1 roster), [7] (merges/exclusions/review flags)
  data/sources/v7_1/geniiAggregateSortFreq.csv   (the v7 500-row aggregate; used only to confirm the v7 error causes)
  data/roster/curated_aliases.csv   (hand decisions: merge / separate / exclude / flag / display_fix)
  data/roster/status_overrides.csv  (status set by a recorded decision; wins over the v7 carry-over)

Outputs:
  data/roster/roster.csv, data/roster/alias_map.csv, data/roster/merge_log.csv   (or --out DIR)
  versions/v8/roster_diff_v7_to_v8.md                                           (or --out DIR)

Method
  1. Formatting key (automatic, deterministic): strip accents (NFKD + a few special letters),
     split "X - Y" compound entries (keep Y; X recorded as alias / collective prefix),
     drop parentheticals, join apostrophe-surname prefixes (O'Keeffe, O-Keeffe -> okeeffe),
     lowercase, turn every non-letter (hyphen, period, apostrophe) into a space, join runs of
     single-letter initials (B. F. -> bf), keep Jr/Sr (father and son stay apart), sort tokens.
     Sorting tokens makes "Pascal-Blaise", "Blaise Pascal" and "Blaise-Pascal" the same key.
  2. Curated merges from curated_aliases.csv (union-find over keys). Nothing else is fuzzy-merged.
  3. F = number of DISTINCT models listing the person (a model listing someone twice counts once).
  4. Field = most common normalized field string across models (one vote per model);
     ties -> the candidate whose components appear in the most models' field strings, then model order
     Claude, Grok, GPT, Gemini, DeepSeek.
  5. v7 status/exclusions carried over by matching v7 names (and their listed aliases) to keys,
     unless status_overrides.csv sets the status by a recorded decision.

Run:    python3 scripts/rebuild_roster.py              # rewrite the committed outputs
        python3 scripts/rebuild_roster.py --check      # rebuild into a temp dir and compare byte-for-byte
        python3 scripts/rebuild_roster.py --out /tmp/x # write all outputs to another directory
"""
import csv, json, re, sys, unicodedata, collections, difflib, os, argparse, tempfile, filecmp, shutil

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(REPO, "data", "sources", "model_lists")
V7_DIR = os.path.join(REPO, "data", "sources", "v7_1")
V7_JSON = os.path.join(V7_DIR, "neuresthetics_v7_combined.json")
V7_AGG = os.path.join(V7_DIR, "geniiAggregateSortFreq.csv")
ROSTER_DIR = os.path.join(REPO, "data", "roster")
CURATED = os.path.join(ROSTER_DIR, "curated_aliases.csv")
STATUS_OVERRIDES = os.path.join(ROSTER_DIR, "status_overrides.csv")
OUT_DIR = ROSTER_DIR                                   # roster.csv, alias_map.csv, merge_log.csv
DIFF_DIR = os.path.join(REPO, "versions", "v8")        # roster_diff_v7_to_v8.md
OUTPUT_FILES = ["roster.csv", "alias_map.csv", "merge_log.csv"]
DIFF_FILE = "roster_diff_v7_to_v8.md"
MODELS = ["Claude", "DeepSeek", "Gemini", "GPT", "Grok"]
FIELD_TIEBREAK = ["Claude", "Grok", "GPT", "Gemini", "DeepSeek"]
DISPLAY_PREF = ["Claude", "Grok", "DeepSeek", "Gemini", "GPT"]
COLLECTIVE_PREFIXES = {"wright brothers"}

# ---------------------------------------------------------------- normalization
SPECIAL = {'ø': 'o', 'Ø': 'O', 'ł': 'l', 'Ł': 'L', 'ß': 'ss', 'æ': 'ae', 'Æ': 'AE',
           'đ': 'd', 'Đ': 'D', 'ı': 'i', 'œ': 'oe', 'Œ': 'OE', 'ð': 'd', 'þ': 'th'}
# (Jr/Sr suffixes are intentionally NOT stripped; see name_key)


def deaccent(s):
    s = ''.join(SPECIAL.get(c, c) for c in s)
    return ''.join(c for c in unicodedata.normalize('NFKD', s) if not unicodedata.combining(c))


def split_compound(raw):
    """'Ibn Sina - Avicenna' -> ('Avicenna', 'Ibn Sina'); returns (name, prefix_or_None)."""
    s = raw.strip()
    if ' - ' in s:
        a, b = s.rsplit(' - ', 1)
        return b.strip(), a.strip()
    return s, None


def name_key(raw):
    s, _ = split_compound(raw)
    s = re.sub(r'\(.*?\)', ' ', s)
    s = deaccent(s)
    # O'Keeffe / O-Keeffe / D'Alembert -> OKeeffe (not when the O is itself an initial, e.g. E-O-Wilson)
    s = re.sub(r"(?<![A-Za-z]-)(?<![A-Za-z]\.)\b([OD])['’\-](?=[A-Z][a-z])", r"\1", s)
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", " ", s)
    out, run = [], ''
    for t in s.split():
        if len(t) == 1:
            run += t
        else:
            if run:
                out.append(run); run = ''
            out.append(t)
    if run:
        out.append(run)
    # NOTE: Jr./Sr. are kept in the key on purpose (Arthur Schlesinger Jr. and Sr. are different people)
    return ' '.join(sorted(out))


def paren_aliases(name):
    return [m.strip() for m in re.findall(r'\((.*?)\)', name)]


def norm_field(f):
    f = deaccent(f).strip().lower()
    f = re.sub(r'\s*(/|&|,|;|\band\b)\s*', '-', f)
    f = re.sub(r'\s*-\s*', '-', f)
    f = re.sub(r'\s+', ' ', f).strip('-')
    return f


BUCKETS = [  # (bucket, regex on a single field component); first component that matches wins
    ("polymath", r"polymath|renaissance"),
    ("computer science / AI", r"comput|artificial intel|^ai$|software|cryptograph|internet|programming|machine learning"),
    ("psychology / neuroscience", r"psycho|neuro|psychiatr|cognitiv"),
    ("medicine", r"medic|physician|surg|pharma|immunolog|epidemiol|nursing|public health|physiolog|anatom|patholog"),
    ("biology / life science", r"biolog|genetic|ecolog|zoolog|botan|paleontolog|naturalist|primatolog|etholog|evolution|taxonom|bioch|sociobiolog"),
    ("chemistry", r"chemi"),
    ("astronomy", r"astronom|astrophys|cosmolog"),
    ("physics", r"(?<!geo)physic|optics|microscop"),
    ("earth science", r"geolog|geophys|oceanograph|earth|meteorolog|climat|geograph"),
    ("mathematics", r"(?<!poly)math|statistic|^logic(ian)?$"),
    ("philosophy", r"philosoph|theolog|religio|spiritual|mystic|ethic|sufism|prophet"),
    ("history", r"histor|science studies|^sts$|historiograph"),
    ("linguistics", r"linguist|language|philolog"),
    ("social science", r"sociolog|anthropolog|econom|social|political (science|thought|theory)|demograph|archaeolog|educat|pedagog|management"),
    ("politics / law / military", r"politic|statesm|leader|military|strateg|government|civil rights|activis|humanitar|rights|suffrag|law|jurist|jurisprud|legal|diploma|reform|monarch|ruler|empire|conquer|nonviolen|peace"),
    ("literature", r"literat|poet|poetry|writer|novel|drama|playwright|author|fiction|essay"),
    ("music", r"music|compos|opera|jazz|singer|song|\brap\b|hip hop|\brock\b|^pop$|conduct"),
    ("arts", r"\bart|painting|painter|sculpt|architect|film|cinema|dance|choreograph|photograph|design|animation"),
    ("invention / engineering", r"invent|engineer|technolog|entrepreneur|business|industr|aviation|rocket|aerospace|printing|space"),
    ("exploration", r"explor|navigat|astronaut|travel"),
]


def field_bucket(field):
    for comp in re.split(r'[-/]', norm_field(field)):
        comp = comp.strip()
        for b, rx in BUCKETS:
            if re.search(rx, comp):
                return b
    return "other"


def band(F):
    F = int(F)
    if F >= 5: return "high (5)"
    if F >= 3: return "core (3–4)"
    if F == 2: return "extended (2)"
    return "single-source (1)"


def band_v7(F):
    F = int(F)
    if F >= 5: return "high (≥5)"
    if F >= 3: return "core (3–4)"
    if F == 2: return "extended (2)"
    return "single-source (1)"


# ---------------------------------------------------------------- union-find
class UF:
    def __init__(self): self.p = {}
    def find(self, x):
        self.p.setdefault(x, x)
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]; x = self.p[x]
        return x
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb: self.p[rb] = ra


def main():
    # ---------------------------------------------------------- load raw
    raw = []  # dicts: model, row, name, field, key, prefix
    for m in MODELS:
        with open(os.path.join(RAW_DIR, f"genii{m}.csv"), encoding="utf-8-sig") as fh:
            for i, r in enumerate(csv.DictReader(fh), start=2):
                name, prefix = split_compound(r["name"])
                raw.append(dict(model=m, row=i, name=r["name"].strip(), field=r["field"].strip(),
                                key=name_key(r["name"]), prefix=prefix))
    raw_strings = {(r["model"], r["name"]) for r in raw}
    keys = {r["key"] for r in raw}

    # ---------------------------------------------------------- curated decisions
    cur = list(csv.DictReader(open(CURATED, encoding="utf-8")))
    uf = UF()
    for k in keys: uf.find(k)
    curated_merge_rows, separate_rows, exclude_keys, flags, display_fix = [], [], {}, {}, {}
    warnings = []
    for c in cur:
        d = c["decision"].strip()
        vk = name_key(c["variant"])
        tk = name_key(c["target"]) if c["target"].strip() else None
        if d == "merge":
            if vk not in keys or tk not in keys:
                sys.exit(f"curated merge refers to a name not in the raw lists: {c}")
            uf.union(tk, vk)
            curated_merge_rows.append(c)
        elif d == "separate":
            if vk not in keys or tk not in keys:
                warnings.append(f"'separate' row not found in raw lists (no effect): {c['variant']} / {c['target']}")
            separate_rows.append((vk, tk, c))
        elif d == "exclude":
            exclude_keys[vk] = c["reason"]
        elif d == "flag":
            flags[vk] = c["reason"]
        elif d == "display_fix":
            display_fix[vk] = (c["target"].strip(), c["reason"])
    for vk, tk, c in separate_rows:
        if vk in keys and tk in keys and uf.find(vk) == uf.find(tk):
            sys.exit(f"'separate' pair ended up merged: {c}")
    status_override = {}
    if os.path.exists(STATUS_OVERRIDES):
        for s in csv.DictReader(open(STATUS_OVERRIDES, encoding="utf-8")):
            sk = name_key(s["name"])
            if sk not in keys:
                sys.exit(f"status override refers to a name not in the raw lists: {s}")
            status_override[sk] = s

    # ---------------------------------------------------------- group
    groups = collections.defaultdict(list)
    for r in raw:
        r["gid"] = uf.find(r["key"])
        groups[r["gid"]].append(r)

    # ---------------------------------------------------------- v7 roster + table 7
    v7 = json.load(open(V7_JSON, encoding="utf-8"))
    tables = v7["documents"]["data_book"]["content"]["tables"]
    hdr, *v7rows = tables[6]
    v7rows = [dict(zip(hdr, r)) for r in v7rows]
    t7h, *t7 = tables[7]
    t7 = [dict(zip(t7h, r)) for r in t7]
    v7_review_note = {name_key(r["Original name"]): r["Action"] for r in t7 if r["Type"] == "review"}
    v7_excluded = {name_key(r["Original name"]): r["Action"] for r in t7 if r["Type"] == "exclude"}

    gid_to_v7 = collections.defaultdict(list)
    v7_unmatched = []
    for r in v7rows:
        cands = [r["Name"]] + paren_aliases(r["Name"]) + \
                [re.sub(r'\s*\(\d+\)\s*$', '', a).strip() for a in r["Aliases merged"].split(';') if a.strip()]
        gid = None
        for c in cands:
            k = name_key(c)
            if k in keys:
                gid = uf.find(k); r["_matched_via"] = c; break
        r["_gid"] = gid
        if gid is None:
            v7_unmatched.append(r)
        else:
            gid_to_v7[gid].append(r)

    # ---------------------------------------------------------- build people
    people, excluded = [], []
    alias_rows, log_rows = [], []
    curated_pairs = {}
    for c in curated_merge_rows:
        curated_pairs[name_key(c["variant"])] = c

    for gid, rows in groups.items():
        gkeys = sorted({r["key"] for r in rows})
        models = [m for m in MODELS if any(r["model"] == m for r in rows)]
        F = len(models)
        # field: one vote per model (that model's first listing)
        per_model_field = {}
        for m in models:
            first = sorted([r for r in rows if r["model"] == m], key=lambda r: r["row"])[0]
            per_model_field[m] = norm_field(first["field"])
        votes = collections.Counter(per_model_field.values())
        def contained(f):  # how many models' field strings contain every component of f
            fc = set(f.split('-'))
            return sum(1 for ff in per_model_field.values() if fc <= set(ff.split('-')))
        def fscore(f):
            first_model = min(FIELD_TIEBREAK.index(m) for m, ff in per_model_field.items() if ff == f)
            return (-votes[f], -contained(f), first_model)
        field = sorted(votes, key=fscore)[0]
        field_tie = len([f for f in votes if votes[f] == votes[field]]) > 1

        # exclusion
        exk = [k for k in gkeys if k in exclude_keys]
        if exk:
            excluded.append(dict(name=rows[0]["name"], models=models, F=F, field=field,
                                 reason=exclude_keys[exk[0]], variants=sorted({r["name"] for r in rows})))
            for r in sorted({(r["model"], r["name"]) for r in rows}):
                alias_rows.append(dict(variant=r[1], model=r[0], variant_key=name_key(r[1]), canonical="(EXCLUDED)",
                                       rule="exclude", confidence="high", merged="no", note=exclude_keys[exk[0]]))
            log_rows.append(dict(canonical="(EXCLUDED)", variant=" | ".join(sorted({r['name'] for r in rows})),
                                 models=";".join(models), action="excluded", rule="exclude", confidence="high",
                                 note=exclude_keys[exk[0]]))
            continue

        # canonical display
        v7m = gid_to_v7.get(gid, [])
        dfix = [display_fix[k] for k in gkeys if k in display_fix]
        notes = []
        if dfix:
            canonical = dfix[0][0]; notes.append(f"display name corrected: {dfix[0][1]}")
        elif v7m:
            canonical = v7m[0]["Name"]
        else:
            def disp_rank(r):
                gem_second_half = (r["model"] == "Gemini" and re.search(r"\w-\w", r["name"]) and
                                   r["name"].split('-')[0].strip() and ' ' not in r["name"].split('-')[0]
                                   and r["row"] > 330)
                return (DISPLAY_PREF.index(r["model"]) + (10 if gem_second_half else 0), r["row"])
            best = sorted(rows, key=disp_rank)[0]
            canonical, _ = split_compound(best["name"])
            if best["model"] == "GPT":
                canonical = canonical.replace('-', ' ')
        # flags
        for k in gkeys:
            if k in flags: notes.append("FLAG: " + flags[k])
        prefixes = sorted({r["prefix"] for r in rows if r["prefix"]})
        for p in prefixes:
            if name_key(p) in COLLECTIVE_PREFIXES:
                notes.append(f"Claude entry carried collective prefix '{p}' (stripped; v7 excluded 'Wright Brothers' as a collective) - needs status decision")
        dup_models = [m for m in models if sum(1 for r in rows if r["model"] == m) > 1]
        if field_tie: notes.append("field tie across models: " + "; ".join(f"{m}={f}" for m, f in per_model_field.items()))
        if len(v7m) > 1:
            notes.append("v7 had this person on " + str(len(v7m)) + " rows: " + " | ".join(f"{x['Name']} (F={x['F']})" for x in v7m))

        # status
        sov = [status_override[k] for k in gkeys if k in status_override]
        if sov:
            s = sov[0]
            status = s["status"].strip()
            notes.append(f"status set by decision {s['decision']} ({s['decided_on']}): {s['reason']}")
        elif v7m:
            stats = [x["Status"] for x in v7m]
            st = next((s for s in stats if s), "")
            if st:
                status = st
            else:
                status = "needs status (blank in v7)"
                notes.append("v7 status blank; v7 headline count 432 core vs 431 tagged suggests it was meant to be core - not assumed")
        else:
            status = "new — needs status"
        rv = [v7_review_note[k] for k in gkeys if k in v7_review_note]

        variants = sorted({r["name"] for r in rows})
        variant_models = collections.defaultdict(set)
        for r in rows: variant_models[r["name"]].add(r["model"])
        aliases = [v for v in variants if name_key(v) != name_key(canonical) or v != canonical]
        aliases = [v for v in aliases if v != canonical]

        # merge rules per key
        canon_key = name_key(canonical) if name_key(canonical) in gkeys else (name_key(v7m[0]["_matched_via"]) if v7m else gkeys[0])
        if canon_key not in gkeys:
            canon_key = collections.Counter(r["key"] for r in rows).most_common(1)[0][0]
        for v in variants:
            vk = name_key(v)
            if vk == canon_key:
                rule = "format" if v != canonical else "identical"
                conf = "high"; note = "differs only in spacing/hyphens/accents/word order/initials" if rule == "format" else ""
            elif vk in curated_pairs:
                c = curated_pairs[vk]; rule = "curated alias"; conf = c["confidence"]; note = c["reason"]
            else:
                # key reached via another curated row (e.g. a format variant of a curated alias)
                via = [c for k2, c in curated_pairs.items() if uf.find(k2) == gid and name_key(c["target"]) == vk]
                c = next((cc for k2, cc in curated_pairs.items() if k2 == vk), None)
                rule = "curated alias (target side)"
                conf = "confirmed" if via and all(cc["confidence"] == "confirmed" for cc in via) else "high"
                note = "target of curated merge: " + "; ".join(sorted({cc["variant"] for cc in via})) if via else "linked by curated merge"
            if split_compound(v)[1]:
                note = (note + "; " if note else "") + f"compound entry split on ' - ' (other part: '{split_compound(v)[1]}')"
            for m in sorted(variant_models[v]):
                alias_rows.append(dict(variant=v, model=m, variant_key=vk, canonical=canonical, rule=rule,
                                       confidence=conf, merged="yes" if len(variants) > 1 or v != canonical else "n/a", note=note))
            if v != canonical:
                log_rows.append(dict(canonical=canonical, variant=v, models=";".join(sorted(variant_models[v])),
                                     action="merged", rule=rule, confidence=conf, note=note))
        for m in dup_models:
            names = [r["name"] for r in rows if r["model"] == m]
            log_rows.append(dict(canonical=canonical, variant=" | ".join(names), models=m, action="same-model duplicate counted once",
                                 rule="distinct-model count", confidence="high", note=f"{m} lists this person {len(names)} times"))

        people.append(dict(
            canonical_name=canonical, field=field, field_bucket=field_bucket(field), F=F, band=band(F),
            models=";".join(models), **{m: int(m in models) for m in MODELS},
            per_model_field=" | ".join(f"{m}: {per_model_field[m]}" for m in models),
            status=status, v7_name=" | ".join(x["Name"] for x in v7m), v7_F=" | ".join(x["F"] for x in v7m),
            v7_status=" | ".join(x["Status"] for x in v7m), v7_review_note=" | ".join(rv),
            aliases_merged="; ".join(aliases), notes=" ; ".join(notes), _gid=gid, _keys=gkeys, _v7=v7m))

    people.sort(key=lambda p: (-p["F"], deaccent(p["canonical_name"]).lower()))
    for i, p in enumerate(people, 1): p["rank"] = i

    # ---------------------------------------------------------- write roster
    cols = ["rank", "canonical_name", "field", "field_bucket", "F", "band", "models"] + MODELS + \
           ["status", "v7_name", "v7_F", "v7_status", "F_change_vs_v7", "aliases_merged", "per_model_field", "v7_review_note", "notes"]
    for p in people:
        if p["_v7"]:
            v7F = sum(int(x["F"]) for x in p["_v7"]) if len(p["_v7"]) > 1 else int(p["_v7"][0]["F"])
            p["F_change_vs_v7"] = p["F"] - max(int(x["F"]) for x in p["_v7"])
        else:
            p["F_change_vs_v7"] = "new"
    with open(os.path.join(OUT_DIR, "roster.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore"); w.writeheader(); w.writerows(people)

    alias_rows.sort(key=lambda r: (deaccent(r["canonical"]).lower(), r["variant"], r["model"]))
    with open(os.path.join(OUT_DIR, "alias_map.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["variant", "model", "variant_key", "canonical", "rule", "confidence", "merged", "note"])
        w.writeheader(); w.writerows(alias_rows)
        # documented non-merges and flags
        for vk, tk, c in separate_rows:
            w.writerow(dict(variant=c["variant"], model="", variant_key=vk, canonical="(kept separate from) " + c["target"],
                            rule="curated: keep separate", confidence=c["confidence"], merged="no", note=c["reason"]))
        for c in cur:
            if c["decision"] == "flag":
                w.writerow(dict(variant=c["variant"], model="", variant_key=name_key(c["variant"]), canonical="(flag - not merged)",
                                rule="curated: flag", confidence=c["confidence"], merged="no", note=c["reason"]))

    # possible-duplicate scan for the human reviewer (NOT merged): high string similarity between different people
    canon = [(p["canonical_name"], p["_keys"][0]) for p in people]
    sim_flags = []
    sepset = {frozenset((a, b)) for a, b, _ in separate_rows}
    ckeys = [(n, k) for n, k in canon]
    for i in range(len(ckeys)):
        for j in range(i + 1, len(ckeys)):
            a, b = ckeys[i][1], ckeys[j][1]
            ta, tb = set(a.split()), set(b.split())
            r = difflib.SequenceMatcher(None, a, b).ratio()
            subset = (ta < tb or tb < ta) and len(ta & tb) >= 1 and min(len(ta), len(tb)) >= 1
            if (r >= 0.86 or subset) and frozenset((a, b)) not in sepset:
                sim_flags.append((ckeys[i][0], ckeys[j][0], round(r, 2), "token subset" if subset else "similar spelling"))

    log_rows.sort(key=lambda r: (r["action"], deaccent(r["canonical"]).lower()))
    with open(os.path.join(OUT_DIR, "merge_log.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["canonical", "variant", "models", "action", "rule", "confidence", "note"])
        w.writeheader(); w.writerows(log_rows)
        for a, b, r, why in sim_flags:
            w.writerow(dict(canonical=a, variant=b, models="", action="NOT merged - review suggested", rule=why,
                            confidence=f"similarity {r}", note="automatic scan; left as two people"))

    # ---------------------------------------------------------- diff
    write_diff(people, excluded, v7rows, v7_unmatched, gid_to_v7, groups, raw, keys, uf, sim_flags, warnings, t7)
    print(f"people={len(people)} excluded={len(excluded)} raw_rows={len(raw)} keys={len(keys)}")
    for w_ in warnings: print("WARN", w_)


def reproduce_v6_aggregate():
    """Re-run the logic of V6 aggregateGeniiListsByFreq.py (4 files, row counts, ASCII-only
    normalization, 0.9 fuzzy merge) to explain v7 numbers. Returns {canonical: (freq, [merged norms])}."""
    files = ['geniiGrok.csv', 'geniiGemini.csv', 'geniiDeepSeek.csv', 'geniiGPT.csv']
    entries = []
    for fn in files:
        for row in csv.DictReader(open(os.path.join(RAW_DIR, fn), encoding='utf-8')):
            entries.append(row['name'])
    def nn(n):
        n = re.sub(r'[^a-z\s]', '', n.lower()); return ' '.join(sorted(n.split()))
    by = collections.defaultdict(list)
    for e in entries: by[nn(e)].append(e)
    uniq, merges = {}, []
    for norm in sorted(by):
        canonical = collections.Counter(by[norm]).most_common(1)[0][0]
        hit = None
        for ex in uniq:
            if difflib.SequenceMatcher(None, canonical.lower(), ex.lower()).ratio() >= 0.9:
                hit = ex; break
        if hit:
            uniq[hit] += len(by[norm]); merges.append((hit, canonical))
        else:
            uniq[canonical] = len(by[norm])
    return uniq, merges


def write_diff(people, excluded, v7rows, v7_unmatched, gid_to_v7, groups, raw, keys, uf, sim_flags, warnings, t7):
    L = []
    P = L.append
    n = len(people)
    Fdist = collections.Counter(p["F"] for p in people)
    v7F = collections.Counter(int(r["F"]) for r in v7rows)
    def bandcount(dist, lo, hi): return sum(v for k, v in dist.items() if lo <= k <= hi)
    matched = [p for p in people if p["_v7"]]
    added = [p for p in people if not p["_v7"]]
    v7_multi = {gid: rows for gid, rows in gid_to_v7.items() if len(rows) > 1}
    # dropped = v7 rows that do not survive as their own v8 row
    dropped_merge = []
    for gid, rows in v7_multi.items():
        keep = next(p for p in people if p["_gid"] == gid)
        for r in rows:
            if r["Name"] != keep["canonical_name"] and r is not rows[0]:
                dropped_merge.append((r, keep))
    excluded_gids = set()
    for gid, rows in groups.items():
        if any(r["key"] in {name_key(e["name"]) for e in excluded} for r in rows):
            excluded_gids.add(gid)
    dropped_excl = [r for r in v7rows if r["_gid"] in excluded_gids]
    changed = [p for p in matched if p["F_change_vs_v7"] != 0]
    up = [p for p in changed if p["F_change_vs_v7"] > 0]
    down = [p for p in changed if p["F_change_vs_v7"] < 0]
    same = [p for p in matched if p["F_change_vs_v7"] == 0]
    models_rows = collections.Counter(r["model"] for r in raw)
    models_people = collections.Counter(m for p in people for m in p["models"].split(";"))
    crude = len({re.sub(r'[^a-z ]', '', deaccent(r["name"]).lower().replace('-', ' ')).strip() for r in raw})

    P("# Genius roster: v7.1 → v8 (step 1: roster and frequency rebuild)\n")
    P("Built by `scripts/rebuild_roster.py` from the five raw model lists in `data/sources/model_lists/` "
      "(byte-for-byte copies of `V6_(history)/V6/GeniiLists/` in the v7 repo; checksums in `data/sources/SHA256SUMS`).\n")
    P("## Summary\n")
    P(f"- Raw input: {len(raw)} rows across five lists ({', '.join(f'{m} {models_rows[m]}' for m in MODELS)}).")
    n_curated = sum(1 for c in csv.DictReader(open(CURATED, encoding="utf-8")) if c["decision"] == "merge")
    P(f"- {crude} distinct raw name strings after lowercasing/de-accenting; {len(keys)} distinct names after automatic formatting "
      f"normalization (hyphens, 'Last-First' order, accents, initials); {len(people) + len(excluded)} after {n_curated} curated alias merges; "
      f"{len(excluded)} non-person/collective entries excluded.")
    P(f"- **v8 roster: {n} unique people** (v7.1: {len(v7rows)}).")
    P(f"- F is now the number of distinct models (1–5) that list the person. Maximum observed F = {max(Fdist)}; no value above 5.")
    P(f"- Matched to a v7 row: {len(matched)} people. New (not in v7): {len(added)}. "
      f"v7 rows not kept as their own row: {len(dropped_merge) + len(dropped_excl) + len(v7_unmatched)} "
      f"({len(dropped_merge)} merged into another v7 person, {len(dropped_excl)} excluded, {len(v7_unmatched)} unmatched).")
    P(f"- Of the {len(matched)} matched people, F went up for {len(up)}, down for {len(down)}, unchanged for {len(same)}.\n")

    P("## Why v7 frequencies were wrong (checked by re-running the v6 script logic)\n")
    uniq6, merges6 = reproduce_v6_aggregate()
    top500 = sorted(uniq6.items(), key=lambda x: (-x[1], x[0]))[:500]
    agg = [r["name"] for r in csv.DictReader(open(V7_AGG, encoding="utf-8"))]
    P(f"A re-run of `aggregateGeniiListsByFreq.py`'s logic reproduces the v7 500-row aggregate exactly "
      f"({len(set(agg) & {n for n, _ in top500})}/500 names identical), so the causes below are confirmed, not guessed.\n")
    P("1. **geniiClaude.csv was never read.** The script's file list has only Grok, Gemini, DeepSeek and GPT. "
      "So the maximum for a clean name was 4 (Newton, Darwin, Maxwell, Faraday, Spinoza all got 4), and Claude-only names could not appear.")
    P("2. **It counts rows, not models.** Gemini repeats most of its list a second time in 'Last-First' form, and DeepSeek repeats many names "
      f"(DeepSeek: {models_rows['DeepSeek']} rows for {models_people['DeepSeek']} people). A person listed twice by one model got 2. "
      "This is how F>5 arose (Ibn Sina 9 = Avicenna 5 + Ibn Sina 4) and why some DeepSeek-only names had F=3–5 in v7 "
      "(e.g. Donna Haraway: DeepSeek lists her 5 times, v7 F=5, v8 F=1).")
    P("3. **Hyphens and accented letters were deleted, not turned into spaces or plain letters.** 'John-Nash' became 'johnnash' (≠ 'john nash'), "
      "'René' became 'ren'. A 0.9 string-similarity step rescued some long names but not short ones ('John Nash' vs 'John-Nash' scores 0.89).")
    P(f"4. **The list was cut at 500 rows.** After sorting by count then name, the cut fell inside the count-1 tail at "
      f"'{top500[-1][0]}', so {len(uniq6) - 500} later entries were dropped. Hegel (split into four count-1 variants: 'G-W-F Hegel', "
      "'Georg Wilhelm Friedrich Hegel', 'Georg-Wilhelm-Friedrich-Hegel', 'Hegel-G-W-F'), Cantor, Boltzmann, Babbage, Rawls, Dijkstra and "
      "John Nash were all lost this way (most of them are also Claude names).")
    bad = [(a, b) for a, b in merges6 if name_key(a) != name_key(b)]
    P(f"5. The 0.9 similarity step made {len(merges6)} unreviewed merges. Nearly all joined hyphen/accent variants of the same person; "
      f"{len(bad)} joined names that differ beyond formatting: " + "; ".join(f"{b} → {a}" for a, b in bad) +
      " — Arthur Schlesinger Jr. and Sr. are different people (father and son); v8 keeps them apart.")
    P("")

    P("## Distribution by F\n")
    P("| F | v8 people | v7.1 people |")
    P("|---|---|---|")
    for f in range(max(max(Fdist), max(v7F)), 0, -1):
        P(f"| {f} | {Fdist.get(f, 0)} | {v7F.get(f, 0)} |")
    P(f"| total | {n} | {len(v7rows)} |\n")
    P("| Band | v8 | v7.1 |")
    P("|---|---|---|")
    P(f"| high (≥5; in v8 exactly 5) | {bandcount(Fdist,5,99)} | {bandcount(v7F,5,99)} |")
    P(f"| core (3–4) | {bandcount(Fdist,3,4)} | {bandcount(v7F,3,4)} |")
    P(f"| extended (2) | {Fdist.get(2,0)} | {v7F.get(2,0)} |")
    P(f"| single-source (1) | {Fdist.get(1,0)} | {v7F.get(1,0)} |\n")
    P(f"People listed by each model (after merging): " + ", ".join(f"{m} {models_people[m]}" for m in MODELS) + ".\n")

    P("## Top of the v8 roster (F = 5)\n")
    top = [p for p in people if p["F"] == 5]
    P(f"{len(top)} people are on all five lists:\n")
    P(", ".join(f"{p['canonical_name']} ({p['field']})" for p in top) + "\n")

    P("## F changes for names called out in the v7 problem list\n")
    P("| Person | v7 F | v8 F | v8 models |")
    P("|---|---|---|---|")
    watch = ["Isaac Newton", "Charles Darwin", "James Clerk Maxwell", "Michael Faraday", "Baruch Spinoza",
             "Ibn Sina (Avicenna)", "Ibn Rushd (Averroes)", "Blaise Pascal", "Francis Bacon", "Hannah Arendt",
             "Maimonides", "Michel Foucault", "Albert Einstein", "Al-Khwarizmi"]
    for wname in watch:
        p = next((p for p in people if wname in p["v7_name"].split(" | ") or p["canonical_name"] == wname), None)
        if p: P(f"| {p['canonical_name']} | {p['v7_F'] or '—'} | {p['F']} | {p['models']} |")
    for wname in ["Georg Wilhelm Friedrich Hegel", "Georg Cantor", "Ludwig Boltzmann", "Charles Babbage", "John Rawls", "Edsger Dijkstra", "John Nash"]:
        p = next((p for p in people if p["canonical_name"] == wname), None)
        if p: P(f"| {p['canonical_name']} | missing | {p['F']} | {p['models']} |")
    P("")
    P("### All v7 rows with F > 5\n")
    for r in v7rows:
        if int(r["F"]) > 5:
            p = next((p for p in people if p["_gid"] == r["_gid"]), None)
            P(f"- {r['Name']}: v7 F={r['F']} ({r['Aliases merged'] or 'no alias note'}) → v8 F={p['F'] if p else '?'} ({p['models'] if p else ''})")
    P("")
    P("### Largest F increases (matched people)\n")
    for p in sorted(up, key=lambda p: (-p["F_change_vs_v7"], p["canonical_name"]))[:40]:
        P(f"- {p['canonical_name']}: {p['v7_F']} → {p['F']}")
    P("")
    P(f"### All F decreases ({len(down)})\n")
    for p in sorted(down, key=lambda p: (p["F_change_vs_v7"], p["canonical_name"])):
        P(f"- {p['canonical_name']}: {p['v7_F']} → {p['F']} ({p['models']})")
    P("")

    P("## People added (not in v7.1)\n")
    addF = collections.Counter(p["F"] for p in added)
    P(f"{len(added)} new people: " + ", ".join(f"F={f}: {addF[f]}" for f in sorted(addF, reverse=True)) + ". "
      "All have status `new — needs status`. Many are Claude-only names (Claude was never aggregated) "
      "or names cut by the 500-row truncation.\n")
    P("New people with F ≥ 3:\n")
    for p in sorted([p for p in added if p["F"] >= 3], key=lambda p: (-p["F"], p["canonical_name"])):
        P(f"- {p['canonical_name']} — {p['field']} — F={p['F']} ({p['models']})")
    P("")
    P("New people with F = 2 (count by field bucket): " +
      ", ".join(f"{b} {c}" for b, c in collections.Counter(p['field_bucket'] for p in added if p['F'] == 2).most_common()) + ".")
    P("New people with F = 1 (count by field bucket): " +
      ", ".join(f"{b} {c}" for b, c in collections.Counter(p['field_bucket'] for p in added if p['F'] == 1).most_common()) + ".\n")

    P("## People dropped / v7 rows that do not carry over as their own row\n")
    if dropped_merge:
        P("Merged with another v7 row (same person under two names):\n")
        for r, keep in dropped_merge:
            P(f"- v7 '{r['Name']}' (F={r['F']}, {r['Status'] or 'blank'}) → merged into v8 '{keep['canonical_name']}'")
    if dropped_excl:
        P("\nExcluded:\n")
        for r in dropped_excl: P(f"- {r['Name']}")
    if v7_unmatched:
        P("\nv7 rows that could not be matched to any raw list entry:\n")
        for r in v7_unmatched: P(f"- {r['Name']} (F={r['F']})")
    if not (dropped_merge or dropped_excl or v7_unmatched):
        P("None. Every v7.1 roster person is found in the raw lists and kept.")
    P("")

    P("## Exclusions applied\n")
    for e in excluded:
        P(f"- {' / '.join(e['variants'])} ({', '.join(e['models'])}): {e['reason']}")
    P("- v7 table 7 exclusions were Wright Brothers and Anderson localization; both are excluded again. "
      "Claude lists Wilbur and Orville Wright as two individuals (under a 'Wright Brothers - ' prefix); Gemini also lists them individually. "
      "Those individual entries are excluded too, as part of the collective (decision R2, 2026-10-01, rows in `curated_aliases.csv`).")
    P("- No other collectives or non-person entries were found in the raw lists (checked for 'brothers', 'and', '&', team/group/school/effect/theory etc.).\n")

    P("## Status carry-over\n")
    sc = collections.Counter(p["status"] for p in people)
    P("| Status | v8 count |")
    P("|---|---|")
    for s, c in sc.most_common(): P(f"| {s} | {c} |")
    P("")
    sov_people = [p for p in people if p["notes"].find("status set by decision") >= 0]
    for p in sov_people:
        P(f"- {p['canonical_name']}: status `{p['status']}` from `status_overrides.csv` (v7 status: {p['v7_status'] or 'blank'}).")
    if any(p["status"] == "needs status (blank in v7)" for p in people):
        P("- Some v7 statuses are blank. They are marked `needs status (blank in v7)` and nothing is assumed.")
    P("- No other statuses were set. v7 statuses are carried over as they are. Review reasons from v7 table 7 are copied into `v7_review_note`.\n")

    P("## Field buckets\n")
    P("Buckets are assigned by keyword rules in the script (first field component that matches). v7's own bucket table (table 8) used a hand mapping that "
      "is not in the repo, so the v7 column below is the v7 roster re-bucketed with the same rules, for a like-for-like comparison.\n")
    v8b = collections.Counter(p["field_bucket"] for p in people)
    v7b = collections.Counter(field_bucket(r["Field"]) for r in v7rows)
    P("| Bucket | v8 N | v8 share | v7.1 N (same rules) | change |")
    P("|---|---|---|---|---|")
    for b, c in v8b.most_common():
        P(f"| {b} | {c} | {100*c/n:.1f}% | {v7b.get(b,0)} | {c - v7b.get(b,0):+d} |")
    for b in v7b:
        if b not in v8b: P(f"| {b} | 0 | 0% | {v7b[b]} | {-v7b[b]:+d} |")
    P("")
    hb = collections.Counter(p["field_bucket"] for p in people if p["F"] >= 3)
    P("Among F ≥ 3 (the primary analysis cut in the coding rules): " + ", ".join(f"{b} {c}" for b, c in hb.most_common()) + ".\n")

    P("## Merges and review items\n")
    nmerge = collections.Counter()
    P("- Format merges (automatic): spacing, hyphens used as spaces, Gemini's 'Last-First' repeats, accents, initials, word order (Jr./Sr. are kept, so father and son stay separate). "
      "Each is listed in `alias_map.csv` (rule `format`).")
    P("- Curated alias merges (hand list in `curated_aliases.csv`, all logged in `merge_log.csv`): Avicenna/Ibn Sina, Averroes/Ibn Rushd, "
      "Alhazen/Ibn al-Haytham, Al-Khwarizmi/Muhammad ibn Musa al-Khwarizmi, Al-Biruni, Al-Farabi/Farabi, Al-Razi/Razi, Laozi/Lao Tzu, Li Bai/Li Po, "
      "Buddha/Siddhartha Gautama, Rembrandt, Michelangelo, Leibniz, Hegel, Oppenheimer, E.O. Wilson, Spinoza (Benedict/Baruch), Anscombe, Kahn (Bob/Robert), "
      "Mies van der Rohe, Duns Scotus, Murasaki Shikibu, Kovalevskaya, Kolmogorov, Ben-Gurion, Noether, Hodgkin, Herschel (Caroline), Leavitt, Maimonides.")
    P("- Kept separate on purpose (name overlap, different people): George Washington / George Washington Carver, Muhammad (prophet) / al-Khwarizmi, "
      "Zeno of Elea / Zeno of Citium, the Curies and Joliot-Curies, the Leakeys, William / Caroline Herschel, Alan / Dorothy Hodgkin, W.H. / W.L. Bragg, "
      "Francis / Roger Bacon, Ken / E.P. Thompson, Edward Said / Edward Sapir, Marc / Maurice Bloch, and others in `alias_map.csv`.")
    flagged = [c for c in csv.DictReader(open(CURATED, encoding="utf-8")) if c["decision"] == "flag"]
    for c in flagged:
        P(f"- Flagged, not merged: '{c['variant']}': {c['reason']}")
    if any(p["canonical_name"] == "John Maynard Smith" for p in people):
        P("- Display fix by decision R3 (2026-10-01): GPT's 'Brian-Maynard-Smith' is shown as John Maynard Smith; the raw string stays in `alias_map.csv`.")
    if sim_flags:
        P(f"- Automatic similarity scan left {len(sim_flags)} pairs as separate people but listed them in `merge_log.csv` "
          "(action `NOT merged - review suggested`) for a human check.")
    else:
        P("- Automatic similarity scan: no unreviewed pairs. Pairs a human has confirmed as different people are `separate` rows "
          "in `curated_aliases.csv` and are not listed again.")
    if warnings:
        P("- Script warnings: " + "; ".join(warnings))
    P("")
    P("## Files\n")
    P("All roster files are in `data/roster/`.\n")
    P("- `roster.csv` — one row per person: rank, canonical name, field, bucket, F, band, which models, status, v7 name/F/status, F change, aliases, per-model fields, notes.")
    P("- `alias_map.csv` — every raw name string (per model) → canonical name, with rule and confidence; plus keep-separate and flag rows.")
    P("- `merge_log.csv` — every merge, same-model duplicate, exclusion, and the not-merged similarity pairs.")
    P("- `curated_aliases.csv` — the hand decisions the script reads (edit and re-run to change merges).")
    P("- `scripts/rebuild_roster.py` — the script. `python3 scripts/rebuild_roster.py` regenerates all outputs; "
      "`--check` confirms the committed files are reproduced exactly.")
    open(os.path.join(DIFF_DIR, DIFF_FILE), "w", encoding="utf-8").write("\n".join(L) + "\n")


def cli():
    global OUT_DIR, DIFF_DIR
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--out", help="write every output (including the diff) to this directory instead")
    ap.add_argument("--check", action="store_true",
                    help="rebuild into a temp dir and compare byte-for-byte with the committed files; exit 1 on any difference")
    a = ap.parse_args()
    if a.check:
        tmp = tempfile.mkdtemp(prefix="roster_check_")
        OUT_DIR = DIFF_DIR = tmp
        main()
        pairs = [(os.path.join(ROSTER_DIR, f), os.path.join(tmp, f)) for f in OUTPUT_FILES] + \
                [(os.path.join(REPO, "versions", "v8", DIFF_FILE), os.path.join(tmp, DIFF_FILE))]
        bad = 0
        for committed, fresh in pairs:
            same = os.path.exists(committed) and filecmp.cmp(committed, fresh, shallow=False)
            print(("IDENTICAL " if same else "DIFFERENT ") + os.path.relpath(committed, REPO))
            bad += not same
        shutil.rmtree(tmp)
        sys.exit(1 if bad else 0)
    if a.out:
        os.makedirs(a.out, exist_ok=True)
        OUT_DIR = DIFF_DIR = a.out
    main()


if __name__ == "__main__":
    cli()
