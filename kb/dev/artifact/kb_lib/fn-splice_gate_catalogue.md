---
id: https://agentic-knowledge-base.dev/id/chunk/a7114439-153f-4210-a8f9-965a33ad05f4
type: artifact
level: executable
title_ko: 함수 splice_gate_catalogue (tools/kb_lib.py)
title: function splice_gate_catalogue in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/4b222206-08d6-4720-9b58-644cd8cdd017]
part_of: https://agentic-knowledge-base.dev/id/composite/81809a6f-d845-4673-8a0f-b53283ae332c
---
**함수** — `splice_gate_catalogue(text, table)` 다. 문서의 생성 구간을 표로 바꾼 전문 — 표지가 없거나 겹치면 None 이다(손 산문을 덮어쓰지 않는다).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def splice_gate_catalogue(text: str, table: list[str]) -> str | None:
    """문서의 생성 구간을 표로 바꾼 전문 — 표지가 없거나 겹치면 None 이다(손 산문을 덮어쓰지 않는다)."""
    span = gate_catalogue_block(text)
    if span is None:
        return None
    lines = text.split("\n")
    return "\n".join(lines[: span[0] + 1] + [""] + table + [""] + lines[span[1]:])
```
<!-- 인용 끝 -->
