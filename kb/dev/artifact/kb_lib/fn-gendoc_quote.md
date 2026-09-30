---
id: https://agentic-knowledge-base.dev/id/chunk/6dab97ca-f033-4314-aaff-01ed32eab6d5
type: artifact
level: executable
title_ko: 함수 gendoc_quote (tools/kb_lib.py)
title: function gendoc_quote in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/6af6ae14-6a58-40bd-b9fc-9454588817cd
---
**함수** — `gendoc_quote(body)` 다. 청크 본문을 그대로 옮긴 구역 — 서식 규칙의 판정 밖임을 표시한다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def gendoc_quote(body: str) -> list[str]:
    """청크 본문을 그대로 옮긴 구역 — 서식 규칙의 판정 밖임을 표시한다 (원문을 고쳐 쓰지 않는다)."""
    return [GENDOC_QUOTE_OPEN, "", body, "", GENDOC_QUOTE_CLOSE, ""]
```
<!-- 인용 끝 -->
