---
id: https://agentic-knowledge-base.dev/id/chunk/f04f26e1-a284-4a1d-a16a-a9ba90bde65e
type: artifact
level: executable
title_ko: 함수 _cell (tools/weave.py)
title: function _cell in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T02:39:25Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/0a90a335-aba9-44bf-b3c0-2b57ec12feaa
---
**함수** — `_cell(text)` 다. 표 칸 하나 — 칸 안의 `|` 는 이스케이프하고(GFM, kb_lib._gendoc_cells 와 같은 규칙) 빈 값은 없음이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _cell(text: str) -> str:
    """표 칸 하나 — 칸 안의 `|` 는 이스케이프하고(GFM, kb_lib._gendoc_cells 와 같은 규칙) 빈 값은 없음이다."""
    return text.replace("|", "\\|") if text else kb_lib.NONE_MARK
```
<!-- 인용 끝 -->
