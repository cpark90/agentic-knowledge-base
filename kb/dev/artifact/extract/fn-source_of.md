---
id: https://agentic-knowledge-base.dev/id/chunk/a489355a-ef09-4411-ac19-0d5203bc0d58
type: artifact
level: executable
title_ko: 함수 source_of (tools/extract.py)
title: function source_of in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T07:35:51Z}
part_of: https://agentic-knowledge-base.dev/id/composite/019eb57b-f2ff-48bf-a135-886b1f348685
---
**함수** — `source_of(lines, node)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def source_of(lines: list[str], node) -> list[str]:
    start = min([d.lineno for d in node.decorator_list] + [node.lineno])
    return lines[start - 1:node.end_lineno]
```
<!-- 인용 끝 -->
