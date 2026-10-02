---
id: https://agentic-knowledge-base.dev/id/chunk/6571b574-6129-4cb6-8626-ee254df01e2a
type: artifact
level: executable
title_ko: 함수 revision_note (tools/vv_run.py)
title: function revision_note in tools/vv_run.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/9c609b2d-87cb-474b-9ee8-9a132ba26991
---
**함수** — `revision_note(dirty)` 다. 리비전 줄의 워킹트리 칸 — 변경된 추적 파일 수를 함께 적는다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def revision_note(dirty: int) -> str:
    """리비전 줄의 워킹트리 칸 — 변경된 추적 파일 수를 함께 적는다. 표기 하나(실행 기록·보고가 같은 꼴)."""
    return f"있음 {dirty}건" if dirty else kb_lib.NONE_MARK
```
<!-- 인용 끝 -->
