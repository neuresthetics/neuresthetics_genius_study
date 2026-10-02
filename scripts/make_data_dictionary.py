#!/usr/bin/env python3
"""Render the field reference tables in docs/DATA_DICTIONARY.md from the JSON Schemas.

The prose in DATA_DICTIONARY.md is hand-written. The tables between the markers
    <!-- BEGIN GENERATED: person -->  ...  <!-- END GENERATED: person -->
    <!-- BEGIN GENERATED: system -->  ...  <!-- END GENERATED: system -->
are produced from schema/person.schema.json and schema/system.schema.json, so the
dictionary cannot drift from what the validators enforce. Edit descriptions in the
schema, then rerun.

Usage:
    python scripts/make_data_dictionary.py           # rewrite the generated blocks
    python scripts/make_data_dictionary.py --check   # exit 1 if they are out of date
Standard library only.
"""
import argparse, json, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOC = os.path.join(REPO, "docs", "DATA_DICTIONARY.md")
CLAIM_KEYS = {"certainty", "cites", "how_known", "note", "alternatives"}


def esc(s):
    return str(s).replace("|", "\\|").replace("\n", " ")


class R:
    def __init__(self, schema):
        self.s = schema
        self.defs = schema.get("$defs", {})

    def deref(self, node):
        while "$ref" in node:
            node = self.defs[node["$ref"].split("/")[-1]]
        return node

    def is_claim(self, node):
        node = self.deref(node)
        props = node.get("properties", {})
        return "value" in props and "certainty" in props

    def value_desc(self, v):
        """Describe the non-sentinel part of a claim's value."""
        v = self.deref(v)
        opts = v.get("anyOf", [v])
        out = []
        for o in opts:
            if "$ref" in o and o["$ref"].endswith("/sentinel"):
                continue
            o = self.deref(o)
            if "enum" in o:
                out.append("one of: " + ", ".join(f"`{x}`" for x in o["enum"]))
            elif "const" in o:
                out.append(f"`{o['const']}`")
            elif o.get("type") == "array":
                out.append("list")
            elif o.get("type") == "integer" and "maximum" in o:
                out.append(f"integer {o.get('minimum', '')}–{o['maximum']}")
            elif "type" in o:
                t = o["type"]
                out.append(" or ".join(t) if isinstance(t, list) else t)
        return "; ".join(out) or "any"

    def typ(self, node):
        name = node["$ref"].split("/")[-1] if "$ref" in node else None
        n = self.deref(node)
        if "const" in n:
            return f"fixed: `{n['const']}`"
        if "enum" in n:
            return "one of: " + ", ".join(f"`{x}`" for x in n["enum"])
        if self.is_claim(n):
            extra = [k for k in n.get("properties", {}) if k not in CLAIM_KEYS | {"value"}]
            s = "claim; value " + self.value_desc(n["properties"]["value"])
            if extra:
                s += "; extra keys: " + ", ".join(f"`{k}`" for k in extra)
            return s
        t = n.get("type")
        if t == "array":
            it = n.get("items", {})
            if self.is_claim(it):
                return "list of claims (" + self.typ(it) + ")"
            iname = it["$ref"].split("/")[-1] if "$ref" in it else None
            if iname:
                return f"list of `{iname}`"
            return "list of " + self.typ(it)
        if t == "object":
            return f"object (`{name}`)" if name else "object"
        if isinstance(t, list):
            return " or ".join(t)
        return t or (f"`{name}`" if name else "")

    def rows(self, node, prefix, out):
        node = self.deref(node)
        req = set(node.get("required", []))
        for k, v in node.get("properties", {}).items():
            path = prefix + k
            vv = self.deref(v)
            desc = v.get("description") or vv.get("description", "")
            out.append((path, self.typ(v), "yes" if k in req else "", desc))
            if vv.get("type") == "object" and not self.is_claim(vv) and "properties" in vv:
                self.rows(vv, path + ".", out)
            elif vv.get("type") == "array":
                it = self.deref(vv.get("items", {}))
                if it.get("type") == "object" and not self.is_claim(it) and "properties" in it and "$ref" not in vv.get("items", {}):
                    self.rows(it, path + "[].", out)

    def render(self, title):
        L = []
        top = self.s["properties"]
        for sec in top:
            out = []
            v = self.deref(top[sec])
            L += [f"#### `{sec}`", ""]
            d = top[sec].get("description") or v.get("description")
            if d:
                L += [esc(d), ""]
            L += ["| field | type / allowed values | required | meaning |", "|---|---|---|---|"]
            out.append((sec, self.typ(top[sec]), "yes" if sec in self.s.get("required", []) else "", ""))
            if v.get("type") == "object" and not self.is_claim(v):
                self.rows(v, sec + ".", out)
            elif v.get("type") == "array":
                it = self.deref(v.get("items", {}))
                if "properties" in it and not self.is_claim(it) and "$ref" not in v.get("items", {}):
                    self.rows(it, sec + "[].", out)
            for p, t, r, d in out:
                L.append(f"| `{p}` | {esc(t)} | {r} | {esc(d)} |")
            L.append("")
        # shared definitions used as list items or nested objects
        L += [f"#### Shared {title} building blocks", "",
              "Object types referenced above. Claim types share the claim keys (`value`, `certainty`, `cites`, `how_known`, `note`, `alternatives`) and add the extra keys listed.", "",
              "| type | field | type / allowed values | required | meaning |", "|---|---|---|---|---|"]
        for name, d in self.defs.items():
            if name in ("claimRules",):
                continue
            d2 = self.deref(d)
            if "properties" not in d2:
                L.append(f"| `{name}` | | {esc(self.typ(d))} | | {esc(d2.get('description', ''))} |")
                continue
            req = set(d2.get("required", []))
            keys = [k for k in d2["properties"] if not (self.is_claim(d2) and k in CLAIM_KEYS)]
            L.append(f"| `{name}` | | {esc('claim' if self.is_claim(d2) else 'object')} | | {esc(d2.get('description', ''))} |")
            for k in keys:
                pv = d2["properties"][k]
                L.append(f"| | `{k}` | {esc(self.typ(pv) if k != 'value' else self.value_desc(pv))} | {'yes' if k in req else ''} | {esc(pv.get('description') or self.deref(pv).get('description', ''))} |")
        L.append("")
        return "\n".join(L)


def generate():
    blocks = {}
    for name in ("person", "system"):
        with open(os.path.join(REPO, "schema", f"{name}.schema.json"), encoding="utf-8") as fh:
            blocks[name] = R(json.load(fh)).render(name)
    return blocks


def splice(text, blocks):
    for name, body in blocks.items():
        pat = re.compile(rf"(<!-- BEGIN GENERATED: {name} -->\n).*?(<!-- END GENERATED: {name} -->)", re.S)
        if not pat.search(text):
            raise SystemExit(f"markers for '{name}' not found in docs/DATA_DICTIONARY.md")
        text = pat.sub(lambda m: m.group(1) + "\n" + body + "\n" + m.group(2), text)
    return text


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    cur = open(DOC, encoding="utf-8").read()
    new = splice(cur, generate())
    if a.check:
        if new != cur:
            print("docs/DATA_DICTIONARY.md field tables are out of date; run scripts/make_data_dictionary.py")
            sys.exit(1)
        print("docs/DATA_DICTIONARY.md field tables up to date")
    else:
        open(DOC, "w", encoding="utf-8").write(new)
        print("updated docs/DATA_DICTIONARY.md")


if __name__ == "__main__":
    main()
