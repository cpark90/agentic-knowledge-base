---
id: https://agentic-knowledge-base.dev/id/chunk/1c918cdf-d80a-4d97-be99-915bb8ee7e17
type: artifact
level: executable
title_ko: 함수 body_of (tools/workset.py)
title: function body_of in tools/workset.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-workset}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/cdaa7848-3ca1-4cc0-a72c-836fd556f15e]
part_of: https://agentic-knowledge-base.dev/id/composite/efdb6344-03eb-4727-97ba-fe8aadcc7424
---
**함수** — `body_of(path)` 다. 청크 본문 — 판정처는 `kb_lib.chunk_body` 하나다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def body_of(path: str) -> str:
    """청크 본문 — 판정처는 `kb_lib.chunk_body` 하나다 (정의처 chunk2kg 의 `body_text`)."""
    return kb_lib.chunk_body(Path(path).read_text(encoding="utf-8"))
```
<!-- 인용 끝 -->
