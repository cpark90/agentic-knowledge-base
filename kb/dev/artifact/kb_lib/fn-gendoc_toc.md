---
id: https://agentic-knowledge-base.dev/id/chunk/bc17f01c-656e-4b29-b6ac-74961f7b2024
type: artifact
level: executable
title_ko: 함수 gendoc_toc (tools/kb_lib.py)
title: function gendoc_toc in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
uses: [https://agentic-knowledge-base.dev/id/chunk/0a822cf9-05aa-4c0f-90e3-b293ed84a187]
part_of: https://agentic-knowledge-base.dev/id/composite/ce172a2a-c2c5-4b33-b5f6-71a19a8c5bd7
---
**함수** — `gendoc_toc(headings, note)` 다. G12 — 목차 절.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def gendoc_toc(headings: list[str], note: str = "") -> list[str]:
    """G12 — 목차 절. 앵커는 slug 로 만든다. headings 는 문서에 나오는 순서의 제목 텍스트다."""
    anchors = heading_anchors(headings)
    out = [f"## {GENDOC_TOC_HEADING}", ""] + ([note, ""] if note else [])
    return out + [f"- [{h}](#{a})" for h, a in zip(headings, anchors)] + [""]
```
<!-- 인용 끝 -->
