---
id: https://agentic-knowledge-base.dev/id/chunk/0a822cf9-05aa-4c0f-90e3-b293ed84a187
type: artifact
level: executable
title_ko: 함수 heading_anchors (tools/kb_lib.py)
title: function heading_anchors in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
uses: [https://agentic-knowledge-base.dev/id/chunk/a9138ecc-8714-414e-a8f3-69d0c646e65d]
part_of: https://agentic-knowledge-base.dev/id/composite/5c506aa2-9c1f-48ba-b959-5260d60d13ac
---
**함수** — `heading_anchors(headings)` 다. 제목들의 GitHub 앵커 — 문서 순서로 같은 slug 는 -1, -2 … 로 구분한다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def heading_anchors(headings: list[str]) -> list[str]:
    """제목들의 GitHub 앵커 — 문서 순서로 같은 slug 는 -1, -2 … 로 구분한다."""
    seen: dict[str, int] = {}
    out = []
    for h in headings:
        s = slug(h)
        n = seen.get(s, 0)
        seen[s] = n + 1
        out.append(s if n == 0 else f"{s}-{n}")
    return out
```
<!-- 인용 끝 -->
