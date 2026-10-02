---
id: https://agentic-knowledge-base.dev/id/chunk/a6fc9e1e-c79d-4e36-ac7b-36d17aaf0a0a
type: artifact
level: executable
title_ko: 함수 _confirmed_links (tools/kb_lib.py)
title: function _confirmed_links in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/bfce2c4b-b446-4dc4-897c-a67193985671
---
**함수** — `_confirmed_links(g)` 다. 확정 링크 개체 → [(링크, 종류, 출발, 도착)].

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _confirmed_links(g: Graph) -> list:
    """확정 링크 개체 → [(링크, 종류, 출발, 도착)]. 후보·배제는 전파의 대상이 아니다."""
    out = []
    for link in sorted(g.subjects(RDF.type, AGT.Link), key=str):
        if str(next(g.objects(link, AGT.linkState), "")) != LINK_STATE_CONFIRMED:
            continue
        kind = str(next(g.objects(link, AGT.linkKind), "")).split("/")[-1]
        f, t = next(g.objects(link, AGT.linkFrom), None), next(g.objects(link, AGT.linkTo), None)
        if f is not None and t is not None:
            out.append((link, kind, f, t))
    return out
```
<!-- 인용 끝 -->
