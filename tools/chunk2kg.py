#!/usr/bin/env python3
"""청크 파일 → head 그래프(-kg) 생성.

한 청크는 한 파일이다. head 메타데이터(타입·plane·level·라벨·상태·출처)는
청크 파일의 frontmatter에 있고, 본문(assertion)은 그 아래 있다 (노트 4.3절).
`-kg`의 head 그래프는 손으로 쓰지 않고 이 도구가 청크 파일들에서 생성한다 —
agt:lineCount 와 agt:assertionLocation 은 파일에서 계산되므로 어긋날 수 없다.

frontmatter 형식 (YAML 부분집합 — key: value, 목록은 [a, b]):
  iri:          청크 IRI (필수)
  plane:        decision | contract | schema | artifact | annotation | memory (필수)
  level:        functional | abstract | logical | concrete | executable (필수)
  label_ko:     한글 라벨 (필수)
  label_en:     영어 라벨 (필수)
  state:        draft | valid | suspect | invalidated | deprecated (필수)
  assumes:      가정 IRI 목록 (선택)
  derived_from: 출처 IRI 목록 (선택, prov:wasDerivedFrom)
  generated_at: ISO 8601 시각 (선택, prov:generatedAtTime)

사용: chunk2kg.py --out <생성.ttl> <청크 파일들...>
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

PLANE_CLASS = {
    "decision": "agt:DecisionChunk",
    "contract": "agt:ContractChunk",
    "schema": "agt:SchemaChunk",
    "artifact": "agt:ArtifactChunk",
    "annotation": "agt:AnnotationChunk",
    "memory": "agt:MemoryChunk",
}
LEVELS = {"functional", "abstract", "logical", "concrete", "executable"}
STATES = {"draft", "valid", "suspect", "invalidated", "deprecated"}
REQUIRED = ("iri", "plane", "level", "label_ko", "label_en", "state")

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
        if val.startswith("[") and val.endswith("]"):
            items = [v.strip().strip("'\"") for v in val[1:-1].split(",") if v.strip()]
            meta[key] = items
        else:
            meta[key] = val.strip("'\"")

    body = lines[end + 1 :]
    while body and not body[-1].strip():
        body.pop()
    while body and not body[0].strip():
        body.pop(0)

    for k in REQUIRED:
        if not meta.get(k):
            raise ValueError(f"{path}: frontmatter에 {k} 가 없다")
    if meta["plane"] not in PLANE_CLASS:
        raise ValueError(f"{path}: 알 수 없는 plane {meta['plane']!r}")
    if meta["level"] not in LEVELS:
        raise ValueError(f"{path}: 알 수 없는 level {meta['level']!r}")
    if meta["state"] not in STATES:
        raise ValueError(f"{path}: 알 수 없는 state {meta['state']!r}")

    return meta, len(body)


def esc(s: str) -> str:
    return s.replace("\\", "\\\\").replace('"', '\\"')


def emit_chunk(path: str, meta: dict, line_count: int) -> str:
    stmts = [
        f"a {PLANE_CLASS[meta['plane']]}",
        f'rdfs:label "{esc(meta["label_en"])}"@en',
        f'rdfs:label "{esc(meta["label_ko"])}"@ko',
        f"agt:hasLevel agt:{meta['level']}",
        f"agt:lineCount {line_count}",
        f'agt:state "{meta["state"]}"',
        f'agt:assertionLocation "{esc(path)}"',
    ]
    for a in meta.get("assumes", []):
        stmts.append(f"agt:assumes <{a}>")
    for d in meta.get("derived_from", []):
        stmts.append(f"prov:wasDerivedFrom <{d}>")
    if meta.get("generated_at"):
        stmts.append(f'prov:generatedAtTime "{meta["generated_at"]}"^^xsd:dateTime')

    lines = [f"<{meta['iri']}>"]
    for i, s in enumerate(stmts):
        sep = " ." if i == len(stmts) - 1 else " ;"
        lines.append(f"    {s}{sep}")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", required=True)
    ap.add_argument("files", nargs="*")
    args = ap.parse_args()

    blocks, seen = [], {}
    errors = []
    for path in sorted(args.files):
        try:
            meta, n = parse_chunk(path)
        except ValueError as e:
            errors.append(str(e))
            continue
        if meta["iri"] in seen:
            errors.append(f"{path}: IRI {meta['iri']} 가 {seen[meta['iri']]} 와 중복 — 한 청크는 한 파일이다")
            continue
        seen[meta["iri"]] = path
        blocks.append(emit_chunk(path, meta, n))

    if errors:
        for e in errors:
            print(f"FAIL [chunk2kg] {e}", file=sys.stderr)
        return 1

    Path(args.out).write_text(PREAMBLE + "\n" + "\n\n".join(blocks) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
