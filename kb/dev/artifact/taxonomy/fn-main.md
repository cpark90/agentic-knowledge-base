---
id: https://agentic-knowledge-base.dev/id/chunk/e21634c7-d333-426d-a551-d2cc433059ca
type: artifact
level: executable
title_ko: 함수 main (tools/taxonomy.py)
title: function main in tools/taxonomy.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-taxonomy}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-12T07:47:38Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/9027036d-a39d-4b9e-b7c2-40b3cddb625f
---
**함수** — `main()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("files", nargs="+")
    args = ap.parse_args()
    g = Graph()
    for f in args.files:
        try:
            g.parse(f, format="turtle")
        except Exception as e:  # rdflib 파서·OSError — 판정 불가 입력
            print(f"FAIL [taxonomy] {f}: 읽거나 파싱할 수 없다 — {e}", file=sys.stderr)
            return EXIT_CONFIG
    out = ["# 생성 파일 — 손으로 고치지 않는다. 원본은 kb/ontology/related/condition (tools/taxonomy.py).",
           "# ASAM OpenODD YAML 매핑: TAXONOMY 아래 개념 레코드. 범주 3 = agt:Condition 의 하위 클래스. 속성은 ODD 문서의 TAXONOMY 확장이 같은 키 아래에 둔다.",
           "TAXONOMY:"]
    for cls in sorted(g.subjects(RDFS.subClassOf, AGT.Condition), key=lambda c: list(KEYS).index(c) if c in KEYS else 99):
        if (cls, RDF.type, OWL.Class) not in g:
            continue
        ko = next((str(o) for o in g.objects(cls, RDFS.label) if o.language == "ko"), "")
        en = next((str(o) for o in g.objects(cls, RDFS.label) if o.language == "en"), "")
        dfn = next((str(o) for o in g.objects(cls, SKOS.definition)), "").replace("\n", " ")
        key = KEYS.get(cls, str(cls).split("/")[-1].lower())
        out.append(f"  {key}: {{}}    # agt:{str(cls).split('/')[-1]} — {en} · {ko}: {dfn}")
    Path(args.out).write_text("\n".join(out) + "\n", encoding="utf-8")
    return 0
```
<!-- 인용 끝 -->
