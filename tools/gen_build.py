#!/usr/bin/env python3
"""BUILD 생성기 — frontmatter·owl:imports 에서 패키지별 BUILD.bazel 을 생성한다 (bazel-dependency-review 2단계).

원본은 그래프(frontmatter 링크, owl:imports)이고 BUILD 는 커밋되는 뷰다. 링크 변화가 PR diff 에 보이도록
커밋하며, //:build_drift_test 가 생성기를 다시 돌려 커밋본과 비교한다 — frontmatter 를 고치고 BUILD 를 안 돌린
경우를 잡는다. 사용: gen_build.py [--check] [--root .] [--residency defs/kb.bzl]
출력·종료: 생성 시점 거부(세 청크 없는 결정 디렉토리·끊긴 링크·`_check_bundle` 의 패키지 밖 부분·중복 선언·이질·상한·
`composite.ordered` 와 부분 집합의 불일치)는 `FAIL [gen-build] <경로>: …`, frontmatter 위반은
chunk2kg 의 규칙이므로 `FAIL [chunk2kg] …`, --check 의 어긋남은 `FAIL [build-drift] <BUILD>: …` — 모두 EXIT_FAIL.
읽을 수 없는 입력은 EXIT_CONFIG.
"""
import argparse
import difflib
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from chunk2kg import (EXIT_CONFIG, EXIT_FAIL, ORDERED_KEY, SPACE_TYPE, apply_plane_level_state,  # noqa: E402 — 종료 코드는 chunk2kg 가 kb_lib 에서 가져온 것
                      load_plane_level_state, parse_chunk)


class GenBuildError(Exception):
    """생성 시점 거부 — 메시지가 `<경로>: <근거>` 다."""


HEADER ="# 생성 파일 — 손으로 고치지 않는다. 원본은 각 청크의 frontmatter (tools/gen_build.py). 검사: //:build_drift_test\n"
LINKS = ("refines", "serves", "supersedes", "verifies")
ONTO_BASE = "https://agentic-knowledge-base.dev/ontology/"
MEMORY_PKG = "kb/dev/memory"  # 관측 패키지 — 비어 있어도 BUILD 는 생성한다 (//kb/dev:bodies·//kg:chunks_kg 의 끝점)
# V&V KB — 코어의 두 번째 인스턴스 (p8-vv-plane-instances): 디렉토리 = plane 실체 (pe-storage-layout 의 vv/ 번들). 패키지마다 kb_chunk 타깃,
# 비어 있어도 BUILD 는 생성한다. 편집은 vnv 만(kg/catalog-kg.ttl agt:writesIn "kb/vv"), verifies 링크만 KB 를 가로지른다 (defs/kb.bzl).
# 경로 접두는 kb_lib.KB_VV 와 같다 — 이 도구는 rdflib 없이 돌므로 자체 상수로 둔다
VV_ROOT = "kb/vv"
VV_PKGS = {"goal": "requirement", "scenario": "decision", "criteria": "contract", "case": "schema", "verifier": "artifact",
           "verdict": "annotation", "run": "memory"}
SCENARIO_PKG = f"{VV_ROOT}/scenario"  # 시나리오 실체의 패키지 — 역할 접미 규약이 걸리는 자리다
# 시나리오 세 청크의 파일 접미 — 정의처는 kb_lib.SCENARIO_ROLE_MARKERS 의 키이고 이 도구는 rdflib 없이 돌아 kb_lib 를
# 의존할 수 없으므로 VV_ROOT 와 같은 사유로 자체 상수를 갖는다. 표지 낱말(자극·요인·배제 자극)은 게이트 `decision-role` 의 몫이다
SCENARIO_ROLE_SUFFIXES = ("stimulus", "factors", "excluded")
# 결정 복합체의 읽기 순서 — 결론 없이 근거를 읽지 않고 대안은 결론을 전제한다. 이것을 생성기가 `ordered` 인자로 **선언**하고
# chunk2kg 는 추측하지 않는다 (유저 승인 2026-09-29, p4-composite-order-is-declared). ADR 뷰(weave)의 조립 순서와 같다
DECISION_READING_ORDER = ("conclusion", "rationale", "alternatives")
# 키는 plane 이름이 아니라 실체 이름이다 — verdict = 판정 주석 (p8-vv-plane-instances 의 annotation 실체). `verdict` 는
# kb_lib.RUN_VERDICTS(pass·fail·skip)가 이미 쓰는 낱말이라 지어낸 용어가 아니다 (STYLEGUIDE §0 표준어 우선).
# run = 실행 기록 (agt:Run, append-only) — vv_run --record 가 만든다 (kb_lib.VV_RUN_DIR)


def parse_item(path: str):
    """청크 파일 하나 → (메타, 본문 줄 수). 설계 공간 청크는 여기서 거부한다.

    `-space` 는 청크 패키지에 살지 않는다 — kb_chunk 타깃이 되면 후보 링크가 deps 로 새기 때문이다
    (결정 p9-candidate-storage). 올리는 곳은 `//space:design_space`(tools/space2kg.py)다.
    """
    meta, n = parse_chunk(path)
    if meta["type"] == SPACE_TYPE:
        raise GenBuildError(f"{path}: 설계 공간 청크(type: {SPACE_TYPE})는 청크 패키지에 둘 수 없다 — space/ 에 두면 "
                            f"//space:design_space 가 올린다. 후보는 결코 deps 가 되지 않는다 (p9-candidate-storage)")
    return meta, n


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
        meta, _ = parse_item(str(f))
        lab = f"//kb/dev/requirement:{f.stem}"
        items[lab] = {"kind": "chunk", "meta": meta, "src": f.name, "pkg": "kb/dev/requirement"}
        iri_to_label[meta["id"]] = lab
    for d in sorted(p for p in (root / "kb/dev/decision").iterdir() if p.is_dir()):
        parts = {n: parse_item(str(d / f"{n}.md"))[0] for n in ("conclusion", "rationale", "alternatives") if (d / f"{n}.md").exists()}
        if set(parts) != {"conclusion", "rationale", "alternatives"}:
            raise GenBuildError(f"{d}: 결론·근거·대안 세 청크가 있어야 한다 (7.4절 대안 기록) — 있는 것: {sorted(parts)}")
        comp = parts["conclusion"].get("composite") or {}
        lab = f"//kb/dev/decision:{d.name}"
        items[lab] = {"kind": "decision", "parts": parts, "dir": d.name, "pkg": "kb/dev/decision", "comp_iri": comp.get("id", "")}
        for m in parts.values():
            iri_to_label[m["id"]] = lab
        if comp.get("id"):
            iri_to_label[comp["id"]] = lab
    for f in sorted((root / "chunks/decision").glob("*.md")):
        meta, _ = parse_item(str(f))
        lab = f"//chunks/decision:{f.stem}"
        items[lab] = {"kind": "chunk", "meta": meta, "src": f.name, "pkg": "chunks/decision"}
        iri_to_label[meta["id"]] = lab
    for f in sorted((root / MEMORY_PKG).glob("*.md")):  # 관측 (memory plane, append-only) — assume_check --record 가 만든다
        meta, _ = parse_item(str(f))
        if meta["type"] != "memory":
            raise GenBuildError(f"{f}: {MEMORY_PKG} 의 청크는 type: memory 여야 한다 — 실제 {meta['type']!r} (수준 허용표 6.4절)")
        lab = f"//{MEMORY_PKG}:{f.stem}"
        items[lab] = {"kind": "chunk", "meta": meta, "src": f.name, "pkg": MEMORY_PKG}
        iri_to_label[meta["id"]] = lab
    for sub, plane in VV_PKGS.items():  # V&V KB — 디렉토리가 plane 을 정한다. 없는 디렉토리는 빈 패키지다
        pkg = f"{VV_ROOT}/{sub}"
        for f in sorted((root / pkg).glob("*.md")):
            meta, _ = parse_item(str(f))
            if meta["type"] != plane:
                raise GenBuildError(f"{f}: {pkg} 의 청크는 type: {plane} 이어야 한다 — 실제 {meta['type']!r} (V&V KB 의 plane 실체, 결정 p8-vv-plane-instances)")
            lab = f"//{pkg}:{f.stem}"
            items[lab] = {"kind": "chunk", "meta": meta, "src": f.name, "pkg": pkg}
            iri_to_label[meta["id"]] = lab
    return group_composites(items, iri_to_label)  # 청크 전부를 본 뒤에 묶는다 — 묶음은 패키지 × composite.id 다


MAX_PARTS = 9  # 직접 부분의 상한 (7±2, 4.5절) — defs/kb.bzl 의 MAX_PARTS·composite-shapes.ttl 과 같은 수


def group_composites(items, iri_to_label):
    """같은 패키지에서 `composite.id` 를 공유하는 청크들 → 복합체 항목 하나 (kb_composite).

    묶음의 판별 기준은 **같은 패키지 + 같은 `composite.id`** 다. 디렉토리가 기준인 결정(kb_decision)과 달리 일반
    복합체는 평평한 패키지 하나에 여러 개 설 수 있어 디렉토리로는 가를 수 없고, `composite.id` 는 이미 선언이 한 번뿐임을
    chunk2kg 가 강제하는 값이다. 패키지가 기준의 한 축인 것은 Bazel 타깃의 `srcs` 가 자기 패키지 안에만 있을 수 있기
    때문이다 — 묶음은 액션의 입력 집합이고 입력 집합은 패키지를 넘지 못한다.

    부분 청크의 개별 `kb_chunk` 타깃은 사라지고 복합체 타깃 하나가 그 파일 전부를 갖는다 (결정과 같은 형식). 링크는
    부분들의 것을 복합체 타깃으로 올린다. 타깃 이름은 `composite:` 를 선언한 청크의 파일 이름이다.
    """
    decl, members = {}, {}
    for lab, it in items.items():
        if it["kind"] != "chunk":
            continue
        comp = it["meta"].get("composite") or {}
        if comp.get("id"):
            if comp["id"] in decl:  # chunk2kg 는 한 묶음 안의 중복만 본다 — 패키지를 가로지르는 중복은 여기서 거부한다
                raise GenBuildError(f"{it['pkg']}/{it['src']}: 복합체 {comp['id']} 가 {items[decl[comp['id']]]['pkg']}/"
                                    f"{items[decl[comp['id']]]['src']} 와 중복 선언됐다 — 선언은 복합체마다 한 번이다 (4.5절)")
            decl[comp["id"]] = lab
        if it["meta"].get("part_of"):
            members.setdefault(it["meta"]["part_of"], []).append(lab)
    for comp_iri, labs in sorted(members.items()):
        if comp_iri not in decl:
            raise GenBuildError(f"{items[sorted(labs)[0]]['pkg']}/{items[sorted(labs)[0]]['src']}: part_of 대상 복합체 {comp_iri} 를 "
                                f"선언한 청크(composite:)가 없다 — 선언은 부분 중 하나의 frontmatter 에 둔다 (4.5절)")
    for comp_iri, dlab in sorted(decl.items()):
        labs = sorted(set(members.get(comp_iri, []) + [dlab]))
        pkg = items[dlab]["pkg"]
        _check_bundle(comp_iri, dlab, labs, items, pkg)
        parts = [l for l in labs if items[l]["meta"].get("part_of") == comp_iri]
        order = (items[dlab]["meta"].get("composite") or {}).get(ORDERED_KEY)
        part_iris = [items[l]["meta"]["id"] for l in parts]
        if order:  # 순서가 선언됐으면 part_iris 가 그 순서다 — BUILD 가 순서를 보이는 뷰다 (p4-composite-order-is-declared)
            part_iris = sorted(part_iris, key=order.index)
        comp = {"kind": "composite", "pkg": pkg, "comp_iri": comp_iri, "ordered": order or [],
                "srcs": [items[l]["src"] for l in labs], "metas": [items[l]["meta"] for l in labs],
                "part_iris": part_iris, "status": items[dlab]["meta"]["status"],
                "plane": items[parts[0]]["meta"]["type"], "level": items[parts[0]]["meta"]["level"]}
        for l in labs:  # 부분의 개별 청크 타깃은 사라진다 — 복합체 타깃 하나가 그 파일 전부를 갖는다
            iri_to_label[items[l]["meta"]["id"]] = dlab
            del items[l]
        items[dlab] = comp  # 타깃 이름 = 선언 청크의 파일 이름이라 라벨이 바뀌지 않는다
        iri_to_label[comp_iri] = dlab
    return items, iri_to_label


def _check_bundle(comp_iri, dlab, labs, items, pkg):
    """묶음의 생성 시점 거부 — 패키지 밖 부분·부분 수·동질성·선언된 순서. 동질성이 여기서 판정되므로 규칙은 plane·level 을 한 쌍만 받는다."""
    for l in labs:
        if items[l]["pkg"] != pkg:
            raise GenBuildError(f"{items[l]['pkg']}/{items[l]['src']}: 복합체 {comp_iri} 의 선언은 {pkg} 에 있다 — 부분과 선언은 같은 "
                                f"패키지여야 한다 (묶음 = 액션의 입력 집합, defs/kb.bzl kb_composite)")
    parts = [l for l in labs if items[l]["meta"].get("part_of") == comp_iri]
    if len(parts) < 2:
        raise GenBuildError(f"{pkg}/{items[dlab]['src']}: 복합체 {comp_iri} 의 부분이 {len(parts)}개다 — 복합체는 부분 둘 이상의 "
                            f"묶음이고 부분 하나면 청크다 (4.5절)")
    if len(parts) > MAX_PARTS:
        raise GenBuildError(f"{pkg}/{items[dlab]['src']}: 복합체 {comp_iri} 의 직접 부분이 {len(parts)}개다 — 최대 {MAX_PARTS}개(7±2, 4.5절)")
    order = (items[dlab]["meta"].get("composite") or {}).get(ORDERED_KEY)
    if order is None and pkg == SCENARIO_PKG and any(
            Path(items[l]["src"]).stem.endswith("-" + s) for l in parts for s in SCENARIO_ROLE_SUFFIXES):
        raise GenBuildError(f"{pkg}/{items[dlab]['src']}: 복합체 {comp_iri} 에 composite.{ORDERED_KEY} 가 없다 — 시나리오는 "
                            f"자극 → 요인 → 배제 자극의 읽기 순서를 가지므로(p8-scenario-authoring) 선언 없는 시나리오 묶음은 거짓 "
                            f"무순서다. 선언 청크(`-{SCENARIO_ROLE_SUFFIXES[0]}`)의 composite: 에 "
                            f"`{ORDERED_KEY}: [<자극 IRI>, <요인 IRI>, <배제 자극 IRI>]` 를 적는다 (p4-composite-order-is-declared)")
    if order is not None and sorted(order) != sorted(items[l]["meta"]["id"] for l in parts):
        raise GenBuildError(f"{pkg}/{items[dlab]['src']}: 복합체 {comp_iri} 의 composite.{ORDERED_KEY} 가 부분 집합과 다르다 — "
                            f"선언 {sorted(order)} · 부분 {sorted(items[l]['meta']['id'] for l in parts)}. 순서 목록은 부분 전부를 "
                            f"빠짐없이 한 번씩 담는다 (p4-composite-order-is-declared)")
    planes = sorted({items[l]["meta"]["type"] for l in parts})
    levels = sorted({items[l]["meta"]["level"] for l in parts})
    if len(planes) > 1 or len(levels) > 1:
        raise GenBuildError(f"{pkg}/{items[dlab]['src']}: 복합체 {comp_iri} 의 부분이 이질이다 — plane {planes} · level {levels}. "
                            f"부분의 plane·level 은 서로 같다 (동질성 4.5절). 수준 혼합은 결정 복합체의 예외뿐이다 "
                            f"(p7-decision-spans-three-levels)")


def links_of(meta, iri_to_label, where):
    out = {}
    for key in LINKS:
        labs = []
        for iri in meta.get(key, []) or []:
            if iri not in iri_to_label:
                raise GenBuildError(f"{where}: {key} 대상 {iri} 가 타깃이 아니다 — 끊긴 링크 (참조 무결성)")
            labs.append(iri_to_label[iri])
        if labs:
            out[key] = labs
    return out


def render_composite(lab, it, iri_to_label):
    """복합체 묶음 하나 → kb_composite 호출. 형식은 kb_decision 과 같다 — 부분의 링크를 타깃 하나로 올린다.

    `ordered` 는 선언 청크 frontmatter 의 `composite.ordered` 를 그대로 옮긴 뷰다 (p4-composite-order-is-declared).
    선언이 없으면 인자도 없다 — 생성기는 순서를 추측하지 않는다.
    """
    links = {}
    for m in it["metas"]:
        for k, v in links_of(m, iri_to_label, lab).items():
            links.setdefault(k, []).extend(v)
    return ("kb_composite(\n" + f"    name = {q(lab.split(':')[1])},\n"
            + label_list("srcs", it["srcs"])
            + f"    iri = {q(it['comp_iri'])},\n"
            + ("    ordered = [" + ", ".join(q(i) for i in it["ordered"]) + "],\n" if it["ordered"] else "")
            + "    part_iris = [" + ", ".join(q(i) for i in it["part_iris"]) + "],\n"
            + f"    plane = {q(it['plane'])},\n" + f"    level = {q(it['level'])},\n" + f"    status = {q(it['status'])},\n"
            + "".join(label_list(k, sorted(set(v))) for k, v in sorted(links.items())) + ")\n")


def render_chunks(pkg, items, iri_to_label, visibility, allow_empty=False):
    glob_ = 'glob(\n        ["*.md"],\n        allow_empty = True,\n    )' if allow_empty else 'glob(["*.md"])'
    rules = ["kb_bundle", "kb_chunk"] + (["kb_composite"] if any(it["pkg"] == pkg and it["kind"] == "composite" for it in items.values()) else [])
    body = [HEADER, 'load("//defs:kb.bzl", ' + ", ".join(q(r) for r in sorted(rules)) + ")", "",
            f"package(default_visibility = [{q(visibility)}])", "",
            'exports_files(["BUILD.bazel"])', "", f'filegroup(\n    name = "bodies",\n    srcs = {glob_},\n)', ""]
    for lab, it in sorted(items.items()):
        if it["pkg"] != pkg:
            continue
        if it["kind"] == "composite":  # 복합체 = 타깃 하나, 부분 청크의 개별 타깃은 없다 (p4-all-knowledge-is-composite)
            body.append(render_composite(lab, it, iri_to_label))
            continue
        m = it["meta"]
        links = links_of(m, iri_to_label, lab)
        body.append("kb_chunk(\n" + f"    name = {q(lab.split(':')[1])},\n" + f"    src = {q(it['src'])},\n" + f"    iri = {q(m['id'])},\n"
                    + f"    plane = {q(m['type'])},\n" + f"    level = {q(m['level'])},\n" + f"    status = {q(m['status'])},\n"
                    + "".join(label_list(k, v) for k, v in sorted(links.items())) + ")\n")
    names = sorted(lab.split(":")[1] for lab, it in items.items() if it["pkg"] == pkg)
    body.append("# 이 패키지의 head 그래프 조각 묶음 — //kg:chunks_kg 가 병합한다\nkb_bundle(\n    name = \"kg\",\n"
                + (label_list("items", [":" + n for n in names]) or "    items = [],\n") + ")\n")
    return "\n".join(body)


def render_decisions(items, iri_to_label):
    body = [HEADER, 'load("//defs:kb.bzl", "kb_bundle", "kb_decision")', "", 'package(default_visibility = ["//kb:decision_readers"])', "",
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
                    # 순서는 선언이다 (유저 승인 2026-09-29: 결정도 예외 없음). 결정은 역할이 순서를 정하므로 생성기가 그 선언을
                    # 넣는다 — 205개 conclusion.md 의 frontmatter 를 손으로 고치는 것은 첨가이고, 순서의 원본은 추측이 아니라 이 인자다
                    + "    ordered = [" + ", ".join(q(p[n]["id"]) for n in DECISION_READING_ORDER) + "],\n"
                    + "    part_iris = [" + ", ".join(q(p[n]["id"]) for n in ("conclusion", "rationale", "alternatives")) + "],\n"
                    + "    part_levels = [" + ", ".join(q(p[n]["level"]) for n in ("conclusion", "rationale", "alternatives")) + "],\n"
                    + f"    status = {q(p['conclusion']['status'])},\n"
                    + "".join(label_list(k, sorted(set(v))) for k, v in sorted(links.items())) + ")\n")
    names = sorted(it["dir"] for it in items.values() if it["kind"] == "decision")
    body.append("# 이 패키지의 head 그래프 조각 묶음 — //kg:chunks_kg 가 병합한다\nkb_bundle(\n    name = \"kg\",\n" + label_list("items", [":" + n for n in names]) + ")\n")
    return "\n".join(body)


def render_vv_root(items):
    """//kb/vv — 하위 plane 패키지의 bodies 를 모으고, 청크가 하나라도 있으면 lint_test 를 켠다 (빈 filegroup 은 $(rootpaths) 확장이 분석 에러다)."""
    subs = sorted(VV_PKGS)
    nonempty = any(it["pkg"].startswith(VV_ROOT + "/") for it in items.values())
    body = [HEADER]
    if nonempty:
        body.append('load("//defs:knowledge.bzl", "kb_chunk_lint_test")\n')
    body += ["# V&V KB — 시나리오 기반 확인의 지식 (노트 7.1절). 개발 KB 와 같은 코어의 두 번째 인스턴스 (p8-vv-plane-instances): 디렉토리 = plane.\n"
             "# 편집은 vnv 만(kg/catalog-kg.ttl agt:writesIn \"kb/vv\"), 개발 역할은 읽기만. verifies 링크만 KB 를 가로지른다 (V&V → 개발, 같은 level).",
             'package(default_visibility = ["//visibility:public"])', "", 'exports_files(["BUILD.bazel"])', "",
             'filegroup(\n    name = "bodies",\n    srcs = [\n' + "".join(f'        "//{VV_ROOT}/{s}:bodies",\n' for s in subs)
             + '    ] + glob(\n        ["*.md"],\n        allow_empty = True,\n    ),\n)\n']
    if nonempty:
        body.append('kb_chunk_lint_test(\n    name = "lint_test",\n    chunks = [":bodies"],\n    waivers = "//docs:waivers",  # prose 면제 선언 (docs/waivers.md)\n)\n')
    else:
        body.append("# lint_test 는 첫 청크가 들어오면 생성기가 켠다 — 빈 filegroup 은 $(rootpaths) 확장이 분석 에러다\n")
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
        outputs[str(d / "BUILD.bazel")] = (HEADER.replace("각 청크의 frontmatter", "모듈 디렉토리의 온톨로지 TTL")
                                           + 'load("//defs:kb.bzl", "kb_ontology_module")\n\n'
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
    ap.add_argument("--residency", default="", help="PLANES·LEVELS·STATES 값 어휘의 원본 defs/kb.bzl — 안 주면 --root 기준")
    a = ap.parse_args()
    root = Path(a.root)
    try:
        apply_plane_level_state(*load_plane_level_state(a.residency or root / "defs" / "kb.bzl"))
    except (OSError, ValueError) as e:
        print(f"FAIL [chunk2kg] {a.residency or root / 'defs/kb.bzl'}: 읽을 수 없다 — {e}")
        return EXIT_CONFIG
    try:
        items, iri_to_label = scan(root)
        outputs = {
            str(root / "kb/dev/requirement/BUILD.bazel"): render_chunks("kb/dev/requirement", items, iri_to_label, "//kb:requirement_readers"),
            str(root / "kb/dev/decision/BUILD.bazel"): render_decisions(items, iri_to_label),
            str(root / "chunks/decision/BUILD.bazel"): render_chunks("chunks/decision", items, iri_to_label, "//kb:decision_readers"),
            str(root / MEMORY_PKG / "BUILD.bazel"): render_chunks(MEMORY_PKG, items, iri_to_label, "//kb:memory_readers", allow_empty=True),
            str(root / VV_ROOT / "BUILD.bazel"): render_vv_root(items),
        }
        for sub in VV_PKGS:  # V&V plane 패키지 — 개발 청크는 볼 수 없다 (//kb:vv_readers, 8.5절 독립성)
            outputs[str(root / VV_ROOT / sub / "BUILD.bazel")] = render_chunks(f"{VV_ROOT}/{sub}", items, iri_to_label, "//kb:vv_readers", allow_empty=True)
        outputs.update(ontology(root))
    except GenBuildError as e:
        print(f"FAIL [gen-build] {e}")
        return EXIT_FAIL
    except ValueError as e:  # parse_chunk 의 frontmatter·본문 규칙 — chunk2kg 의 판정
        print(f"FAIL [chunk2kg] {e}")
        return EXIT_FAIL
    except OSError as e:
        print(f"FAIL [gen-build] {getattr(e, 'filename', root)}: 읽을 수 없다 — {e}")
        return EXIT_CONFIG
    drift = []
    for path, content in outputs.items():
        p = Path(path)
        old = p.read_text(encoding="utf-8") if p.exists() else ""
        if old != content:
            drift.append(path)
            if a.check:
                sys.stdout.writelines(difflib.unified_diff(old.splitlines(True), content.splitlines(True), f"{path} (커밋본)", f"{path} (생성)", n=1))
            else:
                p.parent.mkdir(parents=True, exist_ok=True)  # 비어 있는 관측 패키지의 첫 BUILD
                p.write_text(content, encoding="utf-8")
    if a.check:
        if drift:
            for path in drift:
                print(f"FAIL [build-drift] {path}: frontmatter 와 어긋난다 — tools/gen_build.py 를 돌려 커밋하라 (BUILD 는 뷰, frontmatter 가 원본)")
            print(f"\nFAIL [build-drift] — {len(drift)}건 / 생성 BUILD {len(outputs)}개")
            return EXIT_FAIL
        print(f"PASS [build-drift] — 생성 BUILD {len(outputs)}개가 원본과 일치")
        return 0
    print(f"생성 {len(outputs)}개, 변경 {len(drift)}개: " + ", ".join(Path(d).relative_to(root).as_posix() for d in drift))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
