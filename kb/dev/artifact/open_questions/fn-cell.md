---
id: https://agentic-knowledge-base.dev/id/chunk/524a116b-45f4-4802-ba70-3d9426371ad6
type: artifact
level: executable
title_ko: 함수 cell (tools/open_questions.py)
title: function cell in tools/open_questions.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-open-questions}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T11:38:01Z}
layer: process
verified: [{by: process:bazel-test, at: 2026-09-30T15:34:48Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/ee1861ba-64c4-4bbb-8da8-cfc4336823c0
---
**함수** — `cell(s)` 다. 표 셀 — 줄바꿈과 파이프를 없앤다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def cell(s: str) -> str:
    """표 셀 — 줄바꿈과 파이프를 없앤다. 빈 값은 세 빈 값의 첫 값이다."""
    return " ".join(str(s).split()).replace("|", "\\|") or kb_lib.NONE_MARK
```
<!-- 인용 끝 -->
