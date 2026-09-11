#!/usr/bin/env python3
"""청크 파일 → head 그래프(-kg) 생성.

한 청크는 한 파일이다. head 메타데이터(타입·plane·level·라벨·상태·출처)는
청크 파일의 frontmatter에 있고, 본문(assertion)은 그 아래 있다 (노트 4.3절).
`-kg`의 head 그래프는 손으로 쓰지 않고 이 도구가 청크 파일들에서 생성한다 —
agt:lineCount 와 agt:assertionLocation 은 파일에서 계산되므로 어긋날 수 없다.

frontmatter 형식 (YAML 부분집합 — key: value, 목록은 [a, b], 인라인 맵은 {k: v}).
OKF v0.2 번들이므로 type·status·generated·verified 는 그 스펙의 필드명을 쓴다:
  iri:          항목 IRI (필수)
  type:         requirement | decision | contract | schema | artifact | annotation | memory (필수, OKF)
  level:        functional | abstract | logical | concrete | executable (필수)
  title_ko:     한글 라벨 (필수) — OKF 확장 키
  title:        영어 라벨 (필수) — OKF title
  status:       draft | stable | suspect | invalidated | deprecated (필수, OKF + 확장 2)
  generated:    {by: <행위자>, at: <ISO 8601>} (필수, OKF)
  verified:     [{by: <행위자>, at: <ISO 8601>}, ...] (선택, OKF) — human: 접두어가 사람 검토
  assumes:      가정 IRI 목록 (선택)
  sources:      OKF v0.2 sources — [{resource: IRI, id?, title?, author?}] (선택). resource → prov:wasDerivedFrom
  refines:      이 항목이 정제하는 상위 항목 IRI 목록 (선택, 수직 링크 9.2절)
  supersedes:   이 항목이 대체하는 항목 IRI 목록 (선택)
  coUpdatesWith: 같은 내용을 담아 함께 갱신되어야 하는 청크 IRI 목록 (선택, relatedTo 족 — 안전율 중복의 표시)
  part_of:      소속 복합체 IRI (선택) — 복합체는 멤버 중 하나가 composite: 로 선언
  composite:    {id: …, title_ko: …, title: …} (선택) — 복합체 개체 선언

사용: chunk2kg.py --out <생성.ttl> <청크 파일들...>
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path

PLANE_CLASS = {
    "requirement": "agt:RequirementChunk",
    "decision": "agt:DecisionChunk",
    "contract": "agt:ContractChunk",
    "schema": "agt:SchemaChunk",
    "artifact": "agt:ArtifactChunk",
    "annotation": "agt:AnnotationChunk",
    "memory": "agt:MemoryChunk",
}
LEVELS = {"functional", "abstract", "logical", "concrete", "executable"}
STATES = {"draft", "stable", "suspect", "invalidated", "deprecated"}
REQUIRED = ("id", "type", "level", "title_ko", "title", "status", "generated")

PREAMBLE = """\
# 생성 파일 — 손으로 고치지 않는다. 원본은 각 청크 파일의 frontmatter다.
# 생성: tools/chunk2kg.py (bazel build //kg:chunks_kg)
@prefix agt: <https://agentic-knowledge-base.dev/agt/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
"""


def parse_chunk(path: str) -> tuple[dict, int]:
    """frontmatter dict와 본문 줄 수를 돌려준다."""
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError(f"{path}: frontmatter가 없다 — 한 청크는 한 파일이고 head는 frontmatter다")
    try:
        end = lines[1:].index("---") + 1
    except ValueError:
        raise ValueError(f"{path}: frontmatter가 닫히지 않았다")

    meta: dict = {}
    for i, raw in enumerate(lines[1:end], start=2):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if ":" not in raw:
            raise ValueError(f"{path}:{i}: 'key: value' 형식이 아니다: {raw!r}")
        key, _, val = raw.partition(":")
        key, val = key.strip(), val.strip()
        meta[key] = parse_value(val)

    body = lines[end + 1 :]
    while body and not body[-1].strip():
        body.pop()
    while body and not body[0].strip():
        body.pop(0)
    meta["_content_hash"] = hashlib.sha256("\n".join(body).encode("utf-8")).hexdigest()[:12]

    for k in REQUIRED:
        if not meta.get(k):
            raise ValueError(f"{path}: frontmatter에 {k} 가 없다")
    if meta["type"] not in PLANE_CLASS:
        raise ValueError(f"{path}: 알 수 없는 type {meta['type']!r} — plane 이름이어야 한다")
    if meta["level"] not in LEVELS:
        raise ValueError(f"{path}: 알 수 없는 level {meta['level']!r}")
    if meta["status"] not in STATES:
        raise ValueError(f"{path}: 알 수 없는 status {meta['status']!r}")
    gen = meta["generated"]
    if not isinstance(gen, dict) or not gen.get("by") or not gen.get("at"):
        raise ValueError(f"{path}: generated 는 {{by: …, at: …}} 여야 한다 (OKF 행위자 표기)")
    for v in meta.get("verified", []):
        if not isinstance(v, dict) or not v.get("by") or not v.get("at"):
            raise ValueError(f"{path}: verified 항목은 {{by: …, at: …}} 여야 한다")

    return meta, len(body)


def parse_map(text: str) -> dict:
    """인라인 맵 {k: v, k: v} — 값에 콤마·콜론이 없다는 전제."""
    out = {}
    for part in text.strip().strip("{}").split(","):
        if not part.strip():
            continue
        k, _, v = part.partition(":")
        out[k.strip()] = v.strip().strip("'\"")
    return out


def parse_value(val: str):
    """key: value 의 값 — 인라인 맵, 목록(스칼라 또는 맵), 스칼라."""
    if val.startswith("{") and val.endswith("}"):
        return parse_map(val)
    if val.startswith("[") and val.endswith("]"):
        inner = val[1:-1].strip()
        if inner.startswith("{"):
            return [parse_map(m) for m in re.findall(r"\{[^{}]*\}", inner)]
        return [v.strip().strip("'\"") for v in inner.split(",") if v.strip()]
    return val.strip("'\"")


def esc(s: str) -> str:
    return s.replace("\\", "\\\\").replace('"', '\\"')


def emit_chunk(path: str, meta: dict, line_count: int) -> str:
    stmts = [
        f"a {PLANE_CLASS[meta['type']]}",
        f'rdfs:label "{esc(meta["title"])}"@en',
        f'rdfs:label "{esc(meta["title_ko"])}"@ko',
        f"agt:hasLevel agt:{meta['level']}",
        f"agt:lineCount {line_count}",
        f'agt:status "{meta["status"]}"',
        f'agt:contentHash "{meta["_content_hash"]}"',
        f'agt:generatedBy "{esc(meta["generated"]["by"])}"',
        f'prov:generatedAtTime "{meta["generated"]["at"]}"^^xsd:dateTime',
        f'agt:assertionLocation "{esc(path)}"',
    ]
    for a in meta.get("assumes", []):
        stmts.append(f"agt:assumes <{a}>")
    for d in meta.get("sources", []):
        res = d.get("resource") if isinstance(d, dict) else d  # OKF: 객체 목록. 옛 문자열 목록도 읽는다
        if not res:
            raise ValueError(f"{path}: sources 항목에 resource 가 없다 (OKF v0.2 §5.1)")
        stmts.append(f"prov:wasDerivedFrom <{res}>")
    for r in meta.get("refines", []):
        stmts.append(f"agt:refines <{r}>")
    for s in meta.get("supersedes", []):
        stmts.append(f"agt:supersedes <{s}>")
    for c in meta.get("coUpdatesWith", []):  # 알고 둔 중복 — 안전율 (p4-redundancy-as-safety-margin). 대칭·relatedTo 족
        stmts.append(f"agt:coUpdatesWith <{c}>")
    for v in meta.get("verified", []):
        stmts.append(f'agt:verifiedBy "{esc(v["by"])}"')
        stmts.append(f'agt:verifiedAt "{v["at"]}"^^xsd:dateTime')

    lines = [f"<{meta['id']}>"]
    for i, s in enumerate(stmts):
        sep = " ." if i == len(stmts) - 1 else " ;"
        lines.append(f"    {s}{sep}")
    return "\n".join(lines)


LINK_KEYS = ("refines", "serves", "supersedes", "verifies", "satisfies", "constrains", "derivesFrom", "allocates", "generates")
ID_BASE = "https://agentic-knowledge-base.dev/id/"


def emit_links(meta: dict) -> list:
    """frontmatter 링크 하나 = agt:Link 개체 하나 + 구축 기록 증거 하나 (9.11절, 10.10절).

    링크는 청크를 저작할 때 편집 연산의 부산물로 생겼으므로(10.3절 구축) 증거 종류는 구축 기록이고,
    참조는 그 청크 자신(생성 기록 generatedBy·generatedAtTime 을 지닌다). 상태는 확정이며 증거 기록이
    있어야 확정이 유효하다 — verify 질의 confirmed-without-evidence 가 검사한다. IRI 는 (출발, 종류, 도착)의 해시라 결정적이다.
    """
    out = []
    for key in LINK_KEYS:
        for to in meta.get(key, []) or []:
            h = hashlib.sha256(f"{meta['id']}|{key}|{to}".encode("utf-8")).hexdigest()[:12]
            link, ev = f"{ID_BASE}link/{h}", f"{ID_BASE}evidence/{h}"
            out.append((link, f"<{link}>\n    a agt:Link , agt:ConfirmedLink ;\n    agt:linkFrom <{meta['id']}> ;\n    agt:linkTo <{to}> ;\n"
                              f"    agt:linkKind agt:{key} ;\n    agt:linkState \"confirmed\" ;\n    agt:hasEvidence <{ev}> ."))
            out.append((ev, f"<{ev}>\n    a agt:Evidence ;\n    agt:evidenceKind agt:constructionRecord ;\n    agt:evidenceRef <{meta['id']}> ;\n    agt:polarity \"+\" ."))
    return out


def merge(out: str, fragments: list) -> int:
    """타깃별 head 조각(--fragment 출력)을 하나의 -kg 로 병합한다. IRI 중복 검사는 여기서 한다 (한 청크는 한 파일)."""
    chunks, comps, seen, errors = [], [], {}, []
    for frag in fragments:
        text = Path(frag).read_text(encoding="utf-8").strip("\n")
        for block in (b for b in text.split("\n\n") if b.strip()):
            iri = block.split("\n", 1)[0].strip("<>")
            if iri in seen:
                errors.append(f"{frag}: IRI {iri} 가 {seen[iri]} 와 중복 — 한 청크는 한 파일이다")
                continue
            seen[iri] = frag
            (comps if "\n    a agt:Composite" in block else chunks).append((iri, block))
    if errors:
        for e in errors:
            print(f"FAIL [chunk2kg merge] {e}", file=sys.stderr)
        return 1
    blocks = [b for _, b in sorted(chunks)] + [b for _, b in sorted(comps)]
    Path(out).write_text(PREAMBLE + "\n" + "\n\n".join(blocks) + "\n", encoding="utf-8")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", required=True)
    ap.add_argument("--fragment", action="store_true", help="타깃 하나의 조각 — 전문(preamble) 없이 블록만 (kb_chunk·kb_decision 액션)")
    ap.add_argument("--merge", action="store_true", help="조각들을 병합해 -kg 를 만든다 (kb_kg_merge)")
    ap.add_argument("files", nargs="*")
    args = ap.parse_args()
    if args.merge:
        return merge(args.out, args.files)

    blocks, seen = [], {}
    composites: dict = {}   # iri -> {labels, members[]}
    part_refs: list = []    # (chunk_iri, composite_iri, path)
    errors = []
    for path in sorted(args.files):
        try:
            meta, n = parse_chunk(path)
        except ValueError as e:
            errors.append(str(e))
            continue
        if meta["id"] in seen:
            errors.append(f"{path}: IRI {meta['id']} 가 {seen[meta['id']]} 와 중복 — 한 청크는 한 파일이다")
            continue
        seen[meta["id"]] = path
        comp = meta.get("composite")
        if comp:
            if not (isinstance(comp, dict) and comp.get("id") and comp.get("title_ko") and comp.get("title")):
                errors.append(f"{path}: composite 는 {{id, title_ko, title}} 이어야 한다")
            elif comp["id"] in composites:
                errors.append(f"{path}: 복합체 {comp['id']} 가 중복 선언됨")
            else:
                composites[comp["id"]] = {"ko": comp["title_ko"], "en": comp["title"], "members": []}
        if meta.get("part_of"):
            part_refs.append((meta["id"], meta["part_of"], path))
        blocks.append((meta["id"], emit_chunk(path, meta, n)))
        blocks.extend(emit_links(meta))
    for chunk_iri, comp_iri, path in part_refs:
        if comp_iri not in composites:
            errors.append(f"{path}: part_of 대상 복합체 {comp_iri} 가 이 묶음 안에 선언되지 않았다")
        else:
            composites[comp_iri]["members"].append(chunk_iri)
    comp_blocks = []
    for iri, c in sorted(composites.items()):
        if not c["members"]:
            errors.append(f"복합체 {iri} 에 부분이 없다")
            continue
        parts = " ,\n        ".join(f"<{m}>" for m in sorted(c["members"]))
        comp_blocks.append(
            f"<{iri}>\n    a agt:Composite ;\n"
            f'    rdfs:label "{esc(c["en"])}"@en ;\n'
            f'    rdfs:label "{esc(c["ko"])}"@ko ;\n'
            f"    agt:hasDirectPart {parts} ."
        )

    if errors:
        for e in errors:
            print(f"FAIL [chunk2kg] {e}", file=sys.stderr)
        return 1

    body = "\n\n".join([b for _, b in sorted(blocks)] + comp_blocks)  # 정규 순서: 청크 IRI 순, 그다음 복합체 IRI 순 — union 과 merge 가 바이트 동일
    Path(args.out).write_text((body if args.fragment else PREAMBLE + "\n" + body) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
