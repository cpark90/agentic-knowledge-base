---
id: https://agentic-knowledge-base.dev/id/chunk/07201b14-1b46-4994-8d76-3f7334f06262
type: artifact
level: executable
title_ko: 함수 _names_cell (tools/weave.py)
title: function _names_cell in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T02:39:25Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/0a90a335-aba9-44bf-b3c0-2b57ec12feaa
---
**함수** — `_names_cell(names)` 다. 이름 목록 칸 — 수와 앞 QUESTION_CELL_SHOW 개.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _names_cell(names) -> str:
    """이름 목록 칸 — 수와 앞 QUESTION_CELL_SHOW 개. 넘는 것은 `외 n` 으로 수를 적는다."""
    names = sorted(names)
    if not names:
        return kb_lib.NONE_MARK
    shown = " · ".join(f"`{x}`" for x in names[:QUESTION_CELL_SHOW])
    return f"{len(names)}: {shown}" + (f" 외 {len(names) - QUESTION_CELL_SHOW}" if len(names) > QUESTION_CELL_SHOW else "")
```
<!-- 인용 끝 -->
