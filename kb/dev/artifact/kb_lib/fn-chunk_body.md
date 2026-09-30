---
id: https://agentic-knowledge-base.dev/id/chunk/cdaa7848-3ca1-4cc0-a72c-836fd556f15e
type: artifact
level: executable
title_ko: 함수 chunk_body (tools/kb_lib.py)
title: function chunk_body in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/6d4f42a2-870a-44fb-9a63-05749c2b9dcd
---
**함수** — `chunk_body(text)` 다. 청크 파일의 본문 — frontmatter 를 뺀 나머지, 앞뒤 빈 줄 제거.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def chunk_body(text: str) -> str:
    """청크 파일의 본문 — frontmatter 를 뺀 나머지, 앞뒤 빈 줄 제거. frontmatter 가 없으면 전문이 본문이다."""
    lines = text.splitlines()
    start = 0
    if lines and lines[0].strip() == "---":
        try:
            start = lines[1:].index("---") + 2
        except ValueError:
            start = 0
    return "\n".join(lines[start:]).strip("\n")
```
<!-- 인용 끝 -->
