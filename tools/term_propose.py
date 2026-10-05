#!/usr/bin/env python3
"""용어 제안 워크플로 (노트 2.5절) — 일반화가 온톨로지에 닿을 때의 절차.

에이전트는 신뢰할 수 없는 센서다: 제안은 하되 판정하지 않는다. 이 도구는
template 행(ID·라벨 ko/en·정의·상위·역량 질문 기여·근거 관측)을 받아 검사를 통과한
제안만 승인 큐(kb/ontology/proposals/)에 남긴다. 승인 큐는 //kb/ontology:modules
밖이라 병합 전에는 그래프에 들어가지 않는다.

  1. 에이전트가 관측에서 개념 후보를 뽑아 이 도구로 제안
  2. 검사: 상위 개념 실재, 항·라벨 중복 없음, 정의 존재, 케밥 ID, 근거 실재
     (근거는 관측·판정 주석 청크 둘 이상 — 일반화는 반복에서 온다)
  3. 통과한 것만 proposals/<slug>-proposal.ttl 로 (실패는 비영 종료).
     근거는 prov:wasDerivedFrom 트리플로 제안에 함께 적힌다
  4. 유저 승인 → 해당 모듈 파일로 이동

종류는 넷이다: class(⊑ 상위 클래스) · object-property · datatype-property(⊑ 상위 속성) ·
individual(상위 클래스의 개체 — 결함 현상처럼 닫힌 열거의 한 값).

사용: term_propose.py --id retry-policy --kind class --parent agt:Condition \\
        --label-ko "재시도 정책" --label-en "retry policy" \\
        --definition "…인 조건. (속+종차)" --cq CQ12 \\
        --derived-from <관측 IRI> --derived-from <관측 IRI>
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

from rdflib import Graph, OWL, RDF, RDFS

try:
    from tools import kb_lib
except ImportError:
    import kb_lib

KIND_TYPE = {
    "class": "owl:Class",
    "object-property": "owl:ObjectProperty",
    "datatype-property": "owl:DatatypeProperty",
    "individual": "owl:NamedIndividual",
}
KIND_PARENT_PRED = {
    "class": "rdfs:subClassOf",
    "object-property": "rdfs:subPropertyOf",
    "datatype-property": "rdfs:subPropertyOf",
}
# 근거가 될 수 있는 청크 종류 — 일반화의 입력은 관측과 판정 주석이다 (노트 14.1)
EVIDENCE_TYPES = ("memory", "annotation")
MIN_EVIDENCE = 2
ONTOLOGY_DIR = Path("kb") / "ontology"
EXCLUDED_SUBDIRS = ("proposals", "shapes")  # 큐 자신과 shape 는 어휘의 원본이 아니다


def ontology_graph(repo: Path) -> Graph:
    """승인된 T-Box — kb/ontology 아래의 TTL 전부(승인 큐·shape 제외)."""
    g = Graph()
    root = repo / ONTOLOGY_DIR
    for f in sorted(root.rglob("*.ttl")):
        if f.relative_to(root).parts[0] in EXCLUDED_SUBDIRS:
            continue
        g.parse(f)
    return g


def chunk_types(repo: Path) -> dict[str, str]:
    """청크 IRI → frontmatter `type` (kb/ 아래 Markdown 청크)."""
    out = {}
    for f in (repo / "kb").rglob("*.md"):
        lines = f.read_text(encoding="utf-8").splitlines()
        fm = lines[1:kb_lib.frontmatter_end(lines) - 1]
        meta = dict(ln.split(":", 1) for ln in fm if re.match(r"^(id|type):", ln))
        if "id" in meta:
            out[meta["id"].strip()] = meta.get("type", "").strip()
    return out


# ── 용어 후보를 검사해 승인 큐에 제안한다 ────────────────────

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--id", required=True, help="영어 소문자 케밥 슬러그")
    ap.add_argument("--kind", required=True, choices=sorted(KIND_TYPE))
    ap.add_argument("--parent", required=True,
                    help="상위 개념 (agt:PascalCase 또는 agt:camelCase). individual 이면 그 개체의 클래스")
    ap.add_argument("--label-ko", required=True)
    ap.add_argument("--label-en", required=True)
    ap.add_argument("--definition", required=True, help="속 + 종차 형식의 한글 정의")
    ap.add_argument("--cq", required=True, help="기여하는 역량 질문 (예: CQ12)")
    ap.add_argument("--derived-from", action="append", default=[],
                    help=f"근거 관측·판정 주석 청크 IRI — 반복해 {MIN_EVIDENCE}개 이상")
    ap.add_argument("--repo", default=os.environ.get("BUILD_WORKSPACE_DIRECTORY")  # bazel run 은 워크스페이스에 쓴다
                    or str(Path(__file__).resolve().parent.parent))
    args = ap.parse_args()

    errors = []
    if not re.fullmatch(r"[a-z][a-z0-9]*(-[a-z0-9]+)*", args.id):
        errors.append(f"id가 케밥이 아니다: {args.id}")
    # PascalCase(클래스) / camelCase(속성·개체) 항 이름
    words = args.id.split("-")
    term = ("".join(w.capitalize() for w in words) if args.kind == "class"
            else words[0] + "".join(w.capitalize() for w in words[1:]))
    term_iri = kb_lib.AGT[term]

    repo = Path(args.repo)
    onto = ontology_graph(repo)
    if len(onto) == 0:
        print(f"FAIL [propose] 온톨로지가 비었다: {repo / ONTOLOGY_DIR} — --repo 를 확인한다")
        return kb_lib.EXIT_CONFIG

    parent = args.parent.split(":", 1)[-1]
    parent_iri = kb_lib.AGT[parent]
    if (parent_iri, None, None) not in onto:
        errors.append(f"상위 개념이 온톨로지에 없다: {args.parent} — 지어낸 상위에 매달 수 없다")
    elif args.kind == "individual" and (parent_iri, RDF.type, OWL.Class) not in onto:
        errors.append(f"individual 의 상위는 클래스여야 한다: {args.parent}")
    if (term_iri, None, None) in onto:
        errors.append(f"항이 이미 존재한다: agt:{term}")
    dup = [str(s) for s, o in onto.subject_objects(RDFS.label) if str(o) in (args.label_ko, args.label_en)]
    if dup:
        errors.append(f"같은 라벨의 항이 이미 있다: {dup[0]} — 동의어는 altLabel로 등록한다 (0.8절)")
    if len(args.definition) < 10:
        errors.append("정의가 너무 짧다 — 속 + 종차로 쓴다 (0.9절)")

    evidence = list(dict.fromkeys(args.derived_from))
    if len(evidence) < MIN_EVIDENCE:
        errors.append(f"근거가 {len(evidence)}개다 — 반복을 보이는 관측·판정 주석 {MIN_EVIDENCE}개 이상을 --derived-from 으로 준다")
    types = chunk_types(repo) if evidence else {}
    for iri in evidence:
        if iri not in types:
            errors.append(f"근거 IRI 가 kb/ 의 청크가 아니다: {iri}")
        elif types[iri] not in EVIDENCE_TYPES:
            errors.append(f"근거가 관측·판정 주석이 아니다 ({types[iri]}): {iri}")

    if errors:
        for e in errors:
            print(f"FAIL [propose] {e}")
        return kb_lib.EXIT_FAIL

    out_dir = repo / ONTOLOGY_DIR / "proposals"
    out_dir.mkdir(exist_ok=True)
    head = (f"agt:{term} a owl:NamedIndividual , agt:{parent} ;" if args.kind == "individual" else
            f"agt:{term} a {KIND_TYPE[args.kind]} ;\n    {KIND_PARENT_PRED[args.kind]} agt:{parent} ;")
    derived = " ,\n        ".join(f"<{iri}>" for iri in evidence)
    body = f"""# 용어 제안 — 승인 전. //kb/ontology:modules 밖이라 그래프에 들어가지 않는다 (2.5절).
# 기여 역량 질문: {args.cq}
@prefix agt: <https://agentic-knowledge-base.dev/agt/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

{head}
    rdfs:label "{args.label_en}"@en , "{args.label_ko}"@ko ;
    skos:definition "{args.definition}"@ko ;
    prov:wasDerivedFrom {derived} .
"""
    out = out_dir / f"{args.id}-proposal.ttl"
    out.write_text(body, encoding="utf-8")
    Graph().parse(out)  # 자기 구문 검사
    print(f"PASS — 제안이 승인 큐에 올랐다: {out}")
    print("승인 시: 해당 모듈 파일로 옮기고 proposals에서 제거한 뒤 bazel test //... 를 돌린다.")
    return kb_lib.EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
