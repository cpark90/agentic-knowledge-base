---
id: https://agentic-knowledge-base.dev/id/chunk/6dabb4bb-30f5-4716-b694-e88a78da51f1
type: artifact
level: executable
title_ko: 함수 shingles (tools/consistency.py)
title: function shingles in tools/consistency.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-consistency}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/d9f90265-3bbb-4012-993c-a471cd52933e
---
**함수** — `shingles(text, n)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def shingles(text: str, n: int = 5) -> set:
    s = re.sub(r"\s+", " ", text)
    return {s[i:i + n] for i in range(max(0, len(s) - n + 1))}
```
<!-- 인용 끝 -->
