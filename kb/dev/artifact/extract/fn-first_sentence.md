---
id: https://agentic-knowledge-base.dev/id/chunk/aada6cbe-8da7-42be-b193-af12f3127b37
type: artifact
level: executable
title_ko: 함수 first_sentence (tools/extract.py)
title: function first_sentence in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T07:35:51Z}
part_of: https://agentic-knowledge-base.dev/id/composite/019eb57b-f2ff-48bf-a135-886b1f348685
---
**함수** — `first_sentence(node)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def first_sentence(node) -> str:
    doc = (ast.get_docstring(node) or "").strip()
    if not doc:
        return ""
    head = doc.split("\n\n")[0].replace("\n", " ").strip()
    m = re.search(r"^(.{1,160}?[다\.])(?:\s|$)", head)
    return (m.group(1) if m else head[:160]).strip()
```
<!-- 인용 끝 -->
