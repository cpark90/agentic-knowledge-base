---
id: https://agentic-knowledge-base.dev/id/chunk/0ab35aa5-30f6-4c8f-bad6-683509ab787a
type: artifact
level: executable
title_ko: 함수 _gendoc_headings (tools/kb_lib.py)
title: function _gendoc_headings in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
uses: [https://agentic-knowledge-base.dev/id/chunk/07b69002-1dea-4097-9ab5-18b1bc332898]
part_of: https://agentic-knowledge-base.dev/id/composite/ce172a2a-c2c5-4b33-b5f6-71a19a8c5bd7
---
**함수** — `_gendoc_headings(lines)` 다. 펜스 밖 제목들의 (수준, 텍스트) — 문서 순서.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _gendoc_headings(lines: list[str]) -> list[tuple[int, str]]:
    """펜스 밖 제목들의 (수준, 텍스트) — 문서 순서."""
    return [(len(m.group(1)), m.group(2).strip()) for _, line in md_lines(lines) if (m := MD_HEADING.match(line))]
```
<!-- 인용 끝 -->
