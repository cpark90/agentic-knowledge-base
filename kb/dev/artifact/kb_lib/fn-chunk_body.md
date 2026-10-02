---
id: https://agentic-knowledge-base.dev/id/chunk/cdaa7848-3ca1-4cc0-a72c-836fd556f15e
type: artifact
level: executable
title_ko: 함수 chunk_body (tools/kb_lib.py)
title: function chunk_body in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/6d4f42a2-870a-44fb-9a63-05749c2b9dcd
---
**함수** — `chunk_body(text)` 다. 청크 파일의 본문 — frontmatter 를 뺀 나머지, 앞뒤 빈 줄 제거.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def chunk_body(text: str) -> str:
    """청크 파일의 본문 — frontmatter 를 뺀 나머지, 앞뒤 빈 줄 제거. frontmatter 가 없으면 전문이 본문이다.

    판정처는 `body_text` 하나다 (정의처 chunk2kg). 경로를 받지 않는 호출자를 위한 이름이고 규칙은 같다 —
    토큰을 세는 자리와 본문을 읽는 자리가 같은 문자열을 봐야 크기 규칙이 뜻을 갖는다.
    """
    return body_text("chunk.md", text)
```
<!-- 인용 끝 -->
