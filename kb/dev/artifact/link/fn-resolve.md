---
id: https://agentic-knowledge-base.dev/id/chunk/aff29f4a-80e3-4986-a736-70f7ada9fa55
type: artifact
level: executable
title_ko: 함수 resolve (tools/link.py)
title: function resolve in tools/link.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-link}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/e3fd5c02-635a-402a-ad7b-f2cbc4d10b46, https://agentic-knowledge-base.dev/id/chunk/f1f06f16-947e-47c4-b831-f8359170bfed, https://agentic-knowledge-base.dev/id/chunk/f6a3aa93-d0de-4c63-b007-96fc8167809a]
part_of: https://agentic-knowledge-base.dev/id/composite/35504745-0bb4-47e0-ae4a-3da6e0e07b3d
---
**함수** — `resolve(u, key, prefer, hint)` 다. 쌍 → (앵커, 종류, 대상) 또는 탈락 사유.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def resolve(u: Units, key: frozenset, prefer: dict, hint: dict | None = None):
    """쌍 → (앵커, 종류, 대상) 또는 탈락 사유. 인용 방향(없으면 IRI 순)을 먼저, 다음 역방향, TIM 칸이 없으면 같은 KB 안에서 overlapsWith.

    hint(쌍 → 종류)는 승계 후보의 원 링크 종류다 — 인용 방향에서 제약을 통과하면 TIM 우선순위보다 먼저 쓴다.
    """
    a, b = prefer.get(key) or tuple(sorted(key, key=str))
    kind = (hint or {}).get(key)
    if kind and kind in tim_kinds(u.plane[a], u.plane[b]) and violation(u, kind, a, b) is None:
        return (a, kind, b)
    had_cell = False
    for x, y in ((a, b), (b, a)):
        for kind in tim_kinds(u.plane[x], u.plane[y]):
            had_cell = True
            if violation(u, kind, x, y) is None:
                return (x, kind, y)
    if had_cell:
        return R_DIRECTION
    if u.kb(a) != u.kb(b):
        return R_CROSS_KB
    return (a, RELATED, b)
```
<!-- 인용 끝 -->
