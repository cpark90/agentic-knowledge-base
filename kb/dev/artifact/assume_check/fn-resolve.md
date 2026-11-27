---
id: https://agentic-knowledge-base.dev/id/chunk/80ec3ede-99a3-4e75-9ade-f3934e00a52a
type: artifact
level: executable
title_ko: 함수 resolve (tools/assume_check.py)
title: function resolve in tools/assume_check.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-assume-check}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-31T18:06:07Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/f05d76f0-e96f-4c89-a78e-86eeb1bf91d1]
part_of: https://agentic-knowledge-base.dev/id/composite/b33ba404-d208-425c-9ca3-34d8bec67ead
---
**함수** — `resolve(path, root)` 다. 작업 트리 기준 탐색과 이 모듈의 코어 폴백 — `kb_lib.resolve_path` 하나를 쓴다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def resolve(path: str, root: Path) -> Path | None:
    """작업 트리 기준 탐색과 이 모듈의 코어 폴백 — `kb_lib.resolve_path` 하나를 쓴다 (task 0327 손질 5)."""
    return kb_lib.resolve_path(path, root)
```
<!-- 인용 끝 -->
