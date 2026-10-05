---
id: https://agentic-knowledge-base.dev/id/chunk/1da98819-3151-461b-b68f-fcb080f3fbee
type: artifact
level: executable
title_ko: 함수 baseline (tools/case_gen.py)
title: function baseline in tools/case_gen.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-case-gen}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-04T04:52:48Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/c6c4a5c0-8ba7-4c89-a79a-bc2544a590be
---
**함수** — `baseline(keep)` 다. 나머지 변수의 기준값 — 범위 변수는 lo, 열거 변수는 values 의 첫째.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def baseline(keep: dict) -> dict:
    """나머지 변수의 기준값 — 범위 변수는 lo, 열거 변수는 values 의 첫째. 규칙이 건드리지 않는 변수의 값이다."""
    return {k: (v["range"][0] if "range" in v else v["values"][0]) for k, v in keep.items()}
```
<!-- 인용 끝 -->
