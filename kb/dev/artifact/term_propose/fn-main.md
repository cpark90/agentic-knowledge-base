---
id: https://agentic-knowledge-base.dev/id/chunk/d66b4063-3aaf-4298-a354-558d89f03dc6
type: artifact
level: executable
title_ko: 함수 main (tools/term_propose.py)
title: function main in tools/term_propose.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-term-propose}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/0f329565-00ac-4268-a110-cf18eaef3332, https://agentic-knowledge-base.dev/id/chunk/2d62de0c-4e57-4e6c-ba4e-85fe1ebdc37f]
part_of: https://agentic-knowledge-base.dev/id/composite/f37f3044-d076-4e57-b68f-4a03d2ad16d5
---
**함수** — `main()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
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
```
<!-- 인용 끝 -->
