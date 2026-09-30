---
id: https://agentic-knowledge-base.dev/id/chunk/ecb06437-81f9-480c-90ba-0b78a8fde56b
type: artifact
level: executable
title_ko: 함수 md_anchors (tools/kb_lib.py)
title: function md_anchors in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/5c506aa2-9c1f-48ba-b959-5260d60d13ac
---
**함수** — `md_anchors(lines)` 다. 파일의 제목 앵커 집합.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def md_anchors(lines: list[str]) -> set[str]:
    """파일의 제목 앵커 집합."""
    return set(heading_anchors([m.group(2).strip() for _, line in md_lines(lines) if (m := MD_HEADING.match(line))]))
```
<!-- 인용 끝 -->
