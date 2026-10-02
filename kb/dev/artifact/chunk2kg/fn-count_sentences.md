---
id: https://agentic-knowledge-base.dev/id/chunk/a3fa56bc-c50d-4d10-98ed-d101ae5102ce
type: artifact
level: executable
title_ko: 함수 count_sentences (tools/chunk2kg.py)
title: function count_sentences in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/992d5e5a-5efc-4108-a5c8-1e75dd96807a
---
**함수** — `count_sentences(text)` 다. 문장 수 — 코드 스팬과 IRI 를 지운 뒤 공백·줄끝 앞의 종결 부호를 센다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def count_sentences(text: str) -> int:
    """문장 수 — 코드 스팬과 IRI 를 지운 뒤 공백·줄끝 앞의 종결 부호를 센다. 주석 본문의 상한(4)을 재는 자다."""
    return len(COMMENT_SENTENCE_END.findall(COMMENT_IRI.sub(" ", COMMENT_CODE_SPAN.sub(" ", text))))
```
<!-- 인용 끝 -->
