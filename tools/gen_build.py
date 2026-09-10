#!/usr/bin/env python3
"""BUILD 생성기 — frontmatter·owl:imports 에서 패키지별 BUILD.bazel 을 생성한다 (bazel-dependency-review 2단계).

원본은 그래프(frontmatter 링크, owl:imports)이고 BUILD 는 커밋되는 뷰다. 링크 변화가 PR diff 에 보이도록
커밋하며, //:build_drift_test 가 생성기를 다시 돌려 커밋본과 비교한다 — frontmatter 를 고치고 BUILD 를 안 돌린
경우를 잡는다. 사용: gen_build.py [--check] [--root .]
"""
import argparse
import difflib
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from chunk2kg import parse_chunk  # noqa: E402

HEADER = "# 생성 파일 — 손으로 고치지 않는다. 원본은 각 청크의 frontmatter (tools/gen_build.py). 검사: //:build_drift_test\n"
LINKS = ("refines", "serves", "supersedes", "verifies")
ONTO_BASE = "https://agentic-knowledge-base.dev/ontology/"


def q(s):
    return '"' + s.replace('"', '\\"') + '"'


def label_list(name, labels, indent="    "):
    if not labels:
        return ""
    return f"{indent}{name} = [\n" + "".join(f"{indent}    {q(l)},\n" for l in sorted(labels)) + f"{indent}],\n"


def scan(root: Path):
    """청크 파일 → (메타, 패키지, 타깃 이름). IRI → 라벨 사상을 만든다."""
    items = {}  # label -> dict
    iri_to_label = {}
    for f in sorted((root / "kb/dev/requirement").glob("*.md")):
        meta, _ = parse_chunk(str(f))
        lab = f"//kb/dev/requirement:{f.stem}"
        items[lab] = {"kind": "chunk", "meta": meta, "src": f.name, "pkg": "kb/dev/requirement"}
        iri_to_label[meta["id"]] = lab
    for d in sorted(p for p in (root / "kb/dev/decision").iterdir() if p.is_dir()):
        parts = {n: parse_chunk(str(d / f"{n}.md"))[0] for n in ("conclusion", "rationale", "alternatives") if (d / f"{n}.md").exists()}
        if set(parts) != {"conclusion", "rationale", "alternatives"}:
            raise SystemExit(f"gen_build: {d} 는 결론·근거·대안 세 청크가 있어야 한다 (7.4절): {sorted(parts)}")
        comp = parts["conclusion"].get("composite") or {}
        lab = f"//kb/dev/decision:{d.name}"
        items[lab] = {"kind": "decision", "parts": parts, "dir": d.name, "pkg": "kb/dev/decision", "comp_iri": comp.get("id", "")}
        for m in parts.values():
            iri_to_label[m["id"]] = lab
        if comp.get("id"):
            iri_to_label[comp["id"]] = lab
    for f in sorted((root / "chunks/decision").glob("*.md")):
        meta, _ = parse_chunk(str(f))
        lab = f"//chunks/decision:{f.stem}"
        items[lab] = {"kind": "chunk", "meta": meta, "src": f.name, "pkg": "chunks/decision"}
        iri_to_label[meta["id"]] = lab
    return items, iri_to_label


def links_of(meta, iri_to_label, where):
    out = {}
    for key in LINKS:
        labs = []
        for iri in meta.get(key, []) or []:
            if iri not in iri_to_label:
                raise SystemExit(f"gen_build: {where}: {key} 대상 {iri} 가 타깃이 아니다 — 끊긴 링크")
            labs.append(iri_to_label[iri])
        if labs:
            out[key] = labs
    return out


def render_chunks(pkg, items, iri_to_label, visibility):
    body = [HEADER, 'load("//defs:kb.bzl", "kb_chunk")', "", f"package(default_visibility = [{q(visibility)}])", "",
            'exports_files(["BUILD.bazel"])', "", 'filegroup(\n    name = "bodies",\n    srcs = glob(["*.md"]),\n)', ""]
    for lab, it in sorted(items.items()):
        if it["pkg"] != pkg:
            continue
        m = it["meta"]
        links = links_of(m, iri_to_label, lab)
        body.append("kb_chunk(\n" + f"    name = {q(lab.split(':')[1])},\n" + f"    src = {q(it['src'])},\n" + f"    iri = {q(m['id'])},\n"
                    + f"    plane = {q(m['type'])},\n" + f"    level = {q(m['level'])},\n" + f"    status = {q(m['status'])},\n"
                    + "".join(label_list(k, v) for k, v in sorted(links.items())) + ")\n")
    return "\n".join(body)


def render_decisions(items, iri_to_label):
    body = [HEADER, 'load("//defs:kb.bzl", "kb_decision")', "", 'package(default_visibility = ["//kb:decision_readers"])', "",
            'exports_files(["BUILD.bazel"])', "", 'filegroup(\n    name = "bodies",\n    srcs = glob(["**/*.md"]),\n)', ""]
    for lab, it in sorted(items.items()):
        if it["kind"] != "decision":
            continue
        p = it["parts"]
        links = {}
        for m in p.values():
            for k, v in links_of(m, iri_to_label, lab).items():
                links.setdefault(k, []).extend(v)
        body.append("kb_decision(\n" + f"    name = {q(it['dir'])},\n"
                    + "".join(f"    {n} = {q(it['dir'] + '/' + n + '.md')},\n" for n in ("conclusion", "rationale", "alternatives"))
                    + f"    iri = {q(it['comp_iri'])},\n"
                    + "    part_iris = [" + ", ".join(q(p[n]["id"]) for n in ("conclusion", "rationale", "alternatives")) + "],\n"
                    + "    part_levels = [" + ", ".join(q(p[n]["level"]) for n in ("conclusion", "rationale", "alternatives")) + "],\n"
                    + f"    status = {q(p['conclusion']['status'])},\n"
                    + "".join(label_list(k, sorted(set(v))) for k, v in sorted(links.items())) + ")\n")
    return "\n".join(body)


def ontology(root: Path):
    """모듈 디렉토리 → BUILD, project-ontology.ttl 의 owl:imports → modules.bzl"""
    text = (root / "kb/ontology/project-ontology.ttl").read_text(encoding="utf-8")
    imports = re.findall(r"<" + re.escape(ONTO_BASE) + r"([\w/-]+)>", text)
    imports = [i for i in imports if i != "project" and not i.startswith("project/")]
    outputs = {}
    mod_dirs = sorted(p for p in root.glob("kb/ontology/*/*") if p.is_dir() and list(p.glob("*.ttl")))
    for d in mod_dirs:
        rel = d.relative_to(root / "kb/ontology").as_posix()
        outputs[str(d / "BUILD.bazel")] = (HEADER + 'load("//defs:kb.bzl", "kb_ontology_module")\n\n'
                                           'package(default_visibility = ["//visibility:public"])\n\n'
                                           f'# 모듈 = 디렉토리, 청크 = 파일 (2.3절). IRI {ONTO_BASE}{rel}\n'
                                           f"kb_ontology_module(\n    name = {q(d.name)},\n    srcs = glob([\"*.ttl\"]),\n    iri = {q(ONTO_BASE + rel)},\n)\n")
    labels = [f"//kb/ontology/{i}" for i in imports]
    outputs[str(root / "kb/ontology/modules.bzl")] = (HEADER.replace("각 청크의 frontmatter", "project-ontology.ttl 의 owl:imports")
                                                      + '"""project-ontology.ttl 이 가져오는 모듈 — owl:imports 에서 생성."""\n\nPROJECT_IMPORTS = [\n'
                                                      + "".join(f"    {q(l)},\n" for l in sorted(labels)) + "]\n")
    return outputs


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--check", action="store_true", help="생성하지 않고 커밋본과 비교. 어긋나면 1")
    a = ap.parse_args()
    root = Path(a.root)
    items, iri_to_label = scan(root)
    outputs = {
        str(root / "kb/dev/requirement/BUILD.bazel"): render_chunks("kb/dev/requirement", items, iri_to_label, "//kb:requirement_readers"),
        str(root / "kb/dev/decision/BUILD.bazel"): render_decisions(items, iri_to_label),
        str(root / "chunks/decision/BUILD.bazel"): render_chunks("chunks/decision", items, iri_to_label, "//kb:decision_readers"),
    }
    outputs.update(ontology(root))
    drift = []
    for path, content in outputs.items():
        p = Path(path)
        old = p.read_text(encoding="utf-8") if p.exists() else ""
        if old != content:
            drift.append(path)
            if a.check:
                sys.stdout.writelines(difflib.unified_diff(old.splitlines(True), content.splitlines(True), f"{path} (커밋본)", f"{path} (생성)", n=1))
            else:
                p.write_text(content, encoding="utf-8")
    if a.check:
        if drift:
            print(f"FAIL [build-drift] BUILD {len(drift)}개가 frontmatter 와 어긋난다 — tools/gen_build.py 를 돌려 커밋하라: " + ", ".join(drift))
            return 1
        print(f"OK build-drift: 생성 BUILD {len(outputs)}개가 원본과 일치")
        return 0
    print(f"생성 {len(outputs)}개, 변경 {len(drift)}개: " + ", ".join(Path(d).relative_to(root).as_posix() for d in drift))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
