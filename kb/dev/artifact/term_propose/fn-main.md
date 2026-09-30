---
id: https://agentic-knowledge-base.dev/id/chunk/d66b4063-3aaf-4298-a354-558d89f03dc6
type: artifact
level: executable
title_ko: 함수 main (tools/term_propose.py)
title: function main in tools/term_propose.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-term-propose}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-10T17:03:35Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/f37f3044-d076-4e57-b68f-4a03d2ad16d5
---
**함수** — `main()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--id", required=True, help="영어 소문자 케밥 슬러그")
    ap.add_argument("--kind", required=True, choices=sorted(KIND_TYPE))
    ap.add_argument("--parent", required=True, help="상위 개념 (agt:PascalCase 또는 agt:camelCase)")
    ap.add_argument("--label-ko", required=True)
    ap.add_argument("--label-en", required=True)
    ap.add_argument("--definition", required=True, help="속 + 종차 형식의 한글 정의")
    ap.add_argument("--cq", required=True, help="기여하는 역량 질문 (예: CQ12)")
    ap.add_argument("--derived-from", default="", help="근거 관측·청크 IRI")
    ap.add_argument("--repo", default=str(Path(__file__).resolve().parent.parent))
    args = ap.parse_args()

    errors = []
    if not re.fullmatch(r"[a-z][a-z0-9]*(-[a-z0-9]+)*", args.id):
        errors.append(f"id가 케밥이 아니다: {args.id}")
    # PascalCase(클래스) / camelCase(속성) 항 이름
    term = ("".join(w.capitalize() for w in args.id.split("-")) if args.kind == "class"
            else args.id.split("-")[0] + "".join(w.capitalize() for w in args.id.split("-")[1:]))
    term_iri = kb_lib.AGT[term]

    repo = Path(args.repo)
    onto = Graph()
    for f in sorted((repo / "ontology").rglob("*-ontology.ttl")):
        onto.parse(f)

    parent_iri = kb_lib.AGT[args.parent.split(":", 1)[-1]]
    if (parent_iri, None, None) not in onto:
        errors.append(f"상위 개념이 온톨로지에 없다: {args.parent} — 지어낸 상위에 매달 수 없다")
    if (term_iri, None, None) in onto:
        errors.append(f"항이 이미 존재한다: agt:{term}")
    for lbl in (args.label_ko, args.label_en):
        for s in onto.subjects(RDFS.label, None):
            pass
    dup = [str(s) for s, o in onto.subject_objects(RDFS.label) if str(o) in (args.label_ko, args.label_en)]
    if dup:
        errors.append(f"같은 라벨의 항이 이미 있다: {dup[0]} — 동의어는 altLabel로 등록한다 (0.8절)")
    if len(args.definition) < 10:
        errors.append("정의가 너무 짧다 — 속 + 종차로 쓴다 (0.9절)")

    if errors:
        for e in errors:
            print(f"FAIL [propose] {e}")
        return 1

    out_dir = repo / "ontology" / "proposals"
    out_dir.mkdir(exist_ok=True)
    derived = f"# derived-from: {args.derived_from}\n" if args.derived_from else ""
    body = f"""# 용어 제안 — 승인 전. //kb/ontology:modules 밖이라 그래프에 들어가지 않는다 (2.5절).
# 기여 역량 질문: {args.cq}
{derived}@prefix agt: <https://agentic-knowledge-base.dev/agt/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

agt:{term} a {KIND_TYPE[args.kind]} ;
    {KIND_PARENT_PRED[args.kind]} agt:{args.parent.split(':', 1)[-1]} ;
    rdfs:label "{args.label_en}"@en , "{args.label_ko}"@ko ;
    skos:definition "{args.definition}"@ko .
"""
    out = out_dir / f"{args.id}-proposal.ttl"
    out.write_text(body, encoding="utf-8")
    Graph().parse(out)  # 자기 구문 검사
    print(f"PASS — 제안이 승인 큐에 올랐다: {out}")
    print("승인 시: 해당 모듈 파일로 옮기고 proposals에서 제거한 뒤 bazel test //... 를 돌린다.")
    return 0
```
<!-- 인용 끝 -->
