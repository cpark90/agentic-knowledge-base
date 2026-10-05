---
id: https://agentic-knowledge-base.dev/id/chunk/cad7ce8a-694a-4ce3-9a9d-a507ceb3b1c6
type: artifact
level: executable
title_ko: 절 emit (tools/gates2kg.py)
title: section emit in tools/gates2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gates2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/cda496f2-c562-40ea-bde8-f3fa740db1b1
composite: {id: https://agentic-knowledge-base.dev/id/composite/cda496f2-c562-40ea-bde8-f3fa740db1b1, title_ko: 절 복합체 emit (tools/gates2kg.py), title: section composite emit in tools/gates2kg.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/cad7ce8a-694a-4ce3-9a9d-a507ceb3b1c6, https://agentic-knowledge-base.dev/id/chunk/5626d1aa-8b86-4c12-ab4c-ec1e76b25bb5, https://agentic-knowledge-base.dev/id/chunk/b8f959c8-3cb6-443b-828c-c3952f8b8020, https://agentic-knowledge-base.dev/id/chunk/7c84bccd-bce1-441d-ae3c-b5f960ab1dc8, https://agentic-knowledge-base.dev/id/chunk/cdf1f234-455a-45ff-aa45-cc7d4fb9f6cb], part_of: https://agentic-knowledge-base.dev/id/composite/4f1a7107-6da2-49a5-b29b-7bc2f257f90a}
---
**절** — `tools/gates2kg.py` 의 절 `emit` 다. 그래프 방출

**정의** — `emit` · `view_slug` · `emit_projections` · `main` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 그래프 방출 ────────────────────



PROJECTION_HEADER = (
    "# 투영 그래프 — 생성물이다. 손으로 쓰지 않는다 (tools/gates2kg.py --projections).\n"
    "# 원본은 defs/kb.bzl 의 VIEWS 와 tools/kb_lib.py 의 SKILLS 이고 개체 하나가 뷰 또는 skill 하나다.\n"
    "# 투영은 층을 갖지 않는다 — 층은 prov:wasDerivedFrom 이 가리키는 원본 청크만 갖는다 (유저 답 Q9-a).\n"
    "@prefix agt: <https://agentic-knowledge-base.dev/agt/> .\n"
    "@prefix id: <%s> .\n"
    "@prefix prov: <http://www.w3.org/ns/prov#> .\n"
    "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n"
    "@prefix skos: <http://www.w3.org/2004/02/skos/core#> .\n" % ID_BASE
)








if __name__ == "__main__":
    sys.exit(main())
```
<!-- 인용 끝 -->
