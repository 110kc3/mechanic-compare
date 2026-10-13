#!/usr/bin/env python3
"""Validate, render and filter reviewed implementation metadata; never run upstream code."""
import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import sys
from urllib.parse import quote
from urllib.request import Request, urlopen

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
START, END = "<!-- comparison:start -->", "<!-- comparison:end -->"


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def unique(values, label):
    if len(values) != len(set(values)):
        raise ValueError(f"Duplicate {label}")


def validate(data):
    schema = read_json(ROOT / "schema/implementations.schema.json")
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema, format_checker=FormatChecker()).validate(data)
    unique([r["id"] for r in data["implementations"]], "implementation IDs")
    for r in data["implementations"]:
        unique([e["id"] for e in r["evidence"]], f"evidence IDs in {r['id']}")
        unique([m["id"] for m in r["mechanics"]], f"mechanic IDs in {r['id']}")
        evidence = {e["id"]: e for e in r["evidence"]}
        facts = [r["integration"], *r["mechanics"], *r["requirements"], *r["limitations"], *r["license"]["declarations"], {"evidence": r["context_evidence"]}]
        for fact in facts:
            for ref in fact["evidence"]:
                if ref not in evidence:
                    raise ValueError(f"Unknown evidence {ref} in {r['id']}")
        for e in evidence.values():
            if e["kind"] == "external-listing":
                if e["path"] is not None or e["sha256"] is not None or e["symbols"]:
                    raise ValueError(f"External listing must be a dated unpinned observation: {r['id']}/{e['id']}")
            else:
                if not e["path"] or e["path"].startswith("/") or ".." in Path(e["path"]).parts or not e["sha256"]:
                    raise ValueError(f"Missing or unsafe evidence path/hash in {r['id']}/{e['id']}")
                expected = f"https://github.com/{r['repository']}/blob/{r['revision']}/{quote(e['path'], safe='/')}"
                if e["url"] != expected:
                    raise ValueError(f"Evidence is not pinned to record revision: {r['id']}/{e['id']}")
        for mechanic in r["mechanics"]:
            if not any(evidence[ref]["kind"] == "code" for ref in mechanic["evidence"]):
                raise ValueError(f"Mechanic needs reviewed code evidence: {r['id']}/{mechanic['id']}")
        declarations = r["license"]["declarations"]
        status = r["license"]["status"]
        if (status == "unknown" and declarations) or (status == "declared" and not declarations):
            raise ValueError(f"Inconsistent license status in {r['id']}")
        if status == "conflicting" and len({d["identifier"] for d in declarations}) < 2:
            raise ValueError(f"Conflicting license needs differing declarations in {r['id']}")
        check = r["runtime_check"]
        if (check["status"] == "not-run") != (check["evidence"] is None):
            raise ValueError(f"Runtime observation needs evidence, not-run must have none: {r['id']}")
    if (ROOT / "AGENTS.md").read_bytes() != (ROOT / "CLAUDE.md").read_bytes():
        raise ValueError("AGENTS.md and CLAUDE.md differ")
    briefs = read_json(ROOT / "evaluation/briefs.json")
    if briefs.get("status") != "not-run" or len(briefs.get("briefs", [])) != 10:
        raise ValueError("Seed evaluation must contain ten unrun briefs")
    unique([b["id"] for b in briefs["briefs"]], "evaluation IDs")
    ids = {r["id"] for r in data["implementations"]}
    for b in briefs["briefs"]:
        if not b.get("prompt") or not b.get("expected"):
            raise ValueError("Every brief needs a prompt and reviewer expectations")
        if not set(b.get("relevant_records", [])) <= ids:
            raise ValueError(f"Unknown comparison record in brief {b['id']}")


def refs(r, fact):
    sources = {e["id"]: e for e in r["evidence"]}
    return " ".join(f"[{ref}]({sources[ref]['url']})" for ref in fact["evidence"])


def cell(value):
    return value.replace("|", "\\|").replace("\n", " ")


def table(data):
    lines = ["| Implementation | Source context | Reviewed mechanics | Integration shape | Declared terms | Runtime check |", "| --- | --- | --- | --- | --- | --- |"]
    for r in data["implementations"]:
        declared = ", ".join(d["identifier"] for d in r["license"]["declarations"]) or "Unknown"
        if r["license"]["status"] == "conflicting":
            declared += " (conflicting)"
        values = [f"[{r['name']}](comparisons/parkour.md#{r['id']})", f"{r['engine']} / {', '.join(r['languages'])}", ", ".join(m["id"] for m in r["mechanics"]), r["shape"], declared, r["runtime_check"]["status"]]
        lines.append("| " + " | ".join(cell(v) for v in values) + " |")
    return "\n".join(lines)


def comparison(data):
    not_run = sum(r['runtime_check']['status'] == 'not-run' for r in data['implementations'])
    lines = ["# Parkour implementation comparison", "", "Generated from [data/implementations.json](../data/implementations.json).", "", f"Source review: {data['reviewed_at']}. Runtime checks unperformed: {not_run} of {len(data['implementations'])}. Navigation anchors do not establish portable functionality or fidelity.", ""]
    for r in data["implementations"]:
        lines += [f"<a id=\"{r['id']}\"></a>", "", f"## {r['name']}", "", f"{r['summary']} {refs(r, {'evidence': r['context_evidence']})}", "", f"Source context: **{r['engine']}**; languages: **{', '.join(r['languages'])}**; shape: **{r['shape']}**.", "", f"Reviewed [{r['revision'][:12]}](https://github.com/{r['repository']}/tree/{r['revision']}) on {r['reviewed_at']}. Runtime check: **{r['runtime_check']['status']}**.", "", "### Reviewed mechanics", ""]
        for m in r["mechanics"]:
            lines.append(f"- **{m['id']}**: {m['text']} {refs(r, m)}")
        lines += ["", "### Integration", "", f"{r['integration']['text']} {refs(r, r['integration'])}", "", "### Requirements", ""]
        lines += [f"- {f['text']} {refs(r, f)}" for f in r["requirements"]]
        lines += ["", "### Limitations", ""]
        lines += [f"- {f['text']} {refs(r, f)}" for f in r["limitations"]]
        lines += ["", "### Declared terms", "", f"Status: **{r['license']['status']}**. {r['license']['note']}", ""]
        lines += [f"- {d['identifier']}. {refs(r, d)}" for d in r["license"]["declarations"]]
        if not r["license"]["declarations"]:
            lines += [f"- No root license file found in the [reviewed repository tree](https://github.com/{r['repository']}/tree/{r['revision']})."]
        lines += ["", "### Source navigation", "", "| Evidence | Path | Symbols to inspect |", "| --- | --- | --- |"]
        for e in r["evidence"]:
            lines.append(f"| [{e['id']}]({e['url']}) | {cell(e['path'] or 'External listing; dated observation')} | {cell(', '.join(e['symbols']) or '—')} |")
        lines += [""]
    return "\n".join(lines)


def rendered(data):
    path = ROOT / "README.md"
    readme = path.read_text(encoding="utf-8")
    if readme.count(START) != 1 or readme.count(END) != 1:
        raise ValueError("README comparison markers missing or duplicated")
    before, rest = readme.split(START)
    _, after = rest.split(END)
    return {path: before + START + "\n" + table(data) + "\n" + END + after, ROOT / "comparisons/parkour.md": comparison(data)}


def verify_sources(data):
    jobs = [(r, e) for r in data["implementations"] for e in r["evidence"] if e["kind"] != "external-listing"]
    def verify(job):
        r, e = job
        url = f"https://raw.githubusercontent.com/{r['repository']}/{r['revision']}/{quote(e['path'], safe='/')}"
        with urlopen(Request(url, headers={"User-Agent": "mechanic-compare-evidence-check"}), timeout=30) as response:
            body = response.read()
        if hashlib.sha256(body).hexdigest() != e["sha256"]:
            raise ValueError(f"Source hash mismatch: {r['id']}/{e['id']}")
        text = body.decode("utf-8")
        for symbol in e["symbols"]:
            if symbol not in text:
                raise ValueError(f"Navigation symbol missing: {r['id']}/{e['id']}/{symbol}")
    with ThreadPoolExecutor(max_workers=6) as pool:
        list(pool.map(verify, jobs))
    print(f"Verified {len(jobs)} pinned source files; external listing claims require manual review.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    check = sub.add_parser("check")
    check.add_argument("--verify-sources", action="store_true")
    sub.add_parser("render")
    query = sub.add_parser("query")
    query.add_argument("--engine")
    query.add_argument("--language")
    query.add_argument("--mechanic")
    query.add_argument("--json", action="store_true")
    args = parser.parse_args()
    data = read_json(ROOT / "data/implementations.json")
    validate(data)
    if args.command == "query":
        records = [r for r in data["implementations"] if (not args.engine or r["engine"].casefold() == args.engine.casefold()) and (not args.language or args.language.casefold() in [l.casefold() for l in r["languages"]]) and (not args.mechanic or args.mechanic in [m["id"] for m in r["mechanics"]])]
        if args.json:
                print(json.dumps({"coverage": f"{len(data['implementations'])}-record seed; matches are source references, not compatibility guarantees", "matches": records}, indent=2))
        else:
            for r in records:
                print(f"{r['name']}: {r['engine']} / {', '.join(r['languages'])}; license={r['license']['status']}; runtime={r['runtime_check']['status']}")
            if not records:
                print("No seed match. This does not establish that no implementation exists.")
        return
    for path, content in rendered(data).items():
        if args.command == "render":
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        elif not path.exists() or path.read_text(encoding="utf-8") != content:
            raise ValueError(f"Generated content stale: {path.relative_to(ROOT)}; run render")
    if args.command == "check":
        if args.verify_sources:
            verify_sources(data)
        print(f"Checked {len(data['implementations'])} records, evidence references, ten briefs and generated comparisons.")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)
