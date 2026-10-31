---
id: https://agentic-knowledge-base.dev/id/chunk/464fe842-81a3-438f-901c-e9cef6f1dc88
type: artifact
level: executable
title_ko: 함수 space_candidate_of (tools/kb_lib.py)
title: function space_candidate_of in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/d7f34b4e-71f9-47c7-8540-4f10c1a663db
---
**함수** — `space_candidate_of(g, space, link)` 다. 후보 링크 개체 → 후보 — 두 끝 가운데 변수의 출발 항목(agt:variableFrom)이 아닌 쪽이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def space_candidate_of(g: Graph, space, link):
    """후보 링크 개체 → 후보 — 두 끝 가운데 변수의 출발 항목(agt:variableFrom)이 아닌 쪽이다. 없으면 None."""
    var_from = next(g.objects(space, AGT.variableFrom), None)
    frm, to = next(g.objects(link, AGT.linkFrom), None), next(g.objects(link, AGT.linkTo), None)
    return frm if to == var_from and frm != var_from else to
```
<!-- 인용 끝 -->
