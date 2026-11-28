---
id: https://agentic-knowledge-base.dev/id/chunk/95847571-b231-48af-adef-10ab457dbaa3
type: artifact
level: executable
title_ko: 함수 stakeholder_of (tools/weave.py)
title: function stakeholder_of in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T18:25:23Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/8330a4d7-2140-46ed-b107-9196a6c03aa2
---
**함수** — `stakeholder_of(body)` 다. 요구 본문의 `- **이해관계자**: <값> · **관심사**: …` 칸 값 — 칸이 없거나 값이 비면 없음.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def stakeholder_of(body: str) -> str:
    """요구 본문의 `- **이해관계자**: <값> · **관심사**: …` 칸 값 — 칸이 없거나 값이 비면 없음."""
    mt = STAKEHOLDER_LINE.search(body or "")
    return mt.group(1).strip() if mt and mt.group(1).strip() else kb_lib.NONE_MARK
```
<!-- 인용 끝 -->
