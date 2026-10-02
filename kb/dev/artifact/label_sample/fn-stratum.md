---
id: https://agentic-knowledge-base.dev/id/chunk/e4f07e46-7a6b-4f61-81c0-8bec7cc4a0f7
type: artifact
level: executable
title_ko: 함수 stratum (tools/label_sample.py)
title: function stratum in tools/label_sample.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-label-sample}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
layer: process
verified: [{by: process:bazel-test, at: 2026-09-30T15:34:48Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/f8d4f7c1-457b-4464-a913-96c62e1fcb28
---
**함수** — `stratum(path, meta)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def stratum(path: str, meta: dict) -> str:
    if meta["type"] == "requirement":
        return "req"
    if meta["type"] == "decision":
        name = Path(path).name
        if name == "conclusion.md":
            return "conc"
        if name == "rationale.md":
            return "rat"
        if name == "alternatives.md":
            return "alt"
    return ""
```
<!-- 인용 끝 -->
