---
id: https://agentic-knowledge-base.dev/id/chunk/80ec3ede-99a3-4e75-9ade-f3934e00a52a
type: artifact
level: executable
title_ko: 함수 resolve (tools/assume_check.py)
title: function resolve in tools/assume_check.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-assume-check}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/b33ba404-d208-425c-9ca3-34d8bec67ead
---
**함수** — `resolve(path, root)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def resolve(path: str, root: Path) -> Path | None:
    for cand in (Path(path), root / "bazel-bin" / path, root / path):
        if cand.is_file():
            return cand
    return None
```
<!-- 인용 끝 -->
