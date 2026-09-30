---
id: https://agentic-knowledge-base.dev/id/chunk/f6a3aa93-d0de-4c63-b007-96fc8167809a
type: artifact
level: executable
title_ko: 함수 tim_kinds (tools/link.py)
title: function tim_kinds in tools/link.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-link}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/570df80b-916d-466e-a9fe-8a9ac66eea54
---
**함수** — `tim_kinds(pa, pb)` 다. (출발 plane, 도착 plane) 칸이 허용하는 링크 종류 — supersedes 제외, KIND_PREFERENCE 순.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def tim_kinds(pa: str, pb: str) -> list:
    """(출발 plane, 도착 plane) 칸이 허용하는 링크 종류 — supersedes 제외, KIND_PREFERENCE 순."""
    kinds = {k for k, x, y in kb_lib.TIM_CELLS if x == pa and y == pb and k != "supersedes"}
    return sorted(kinds, key=lambda k: KIND_PREFERENCE.index(k) if k in KIND_PREFERENCE else len(KIND_PREFERENCE))
```
<!-- 인용 끝 -->
