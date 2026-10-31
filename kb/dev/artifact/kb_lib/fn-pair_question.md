---
id: https://agentic-knowledge-base.dev/id/chunk/674eca0b-5a5b-45f5-b382-4fa958bafcdc
type: artifact
level: executable
title_ko: 함수 pair_question (tools/kb_lib.py)
title: function pair_question in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/6309baee-3513-4835-affe-e76a4382e7d5
---
**함수** — `pair_question(kind)` 다. 링크 종류 → 그 후보를 묻는 판정 질문의 지역명.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def pair_question(kind: str) -> str:
    """링크 종류 → 그 후보를 묻는 판정 질문의 지역명."""
    return JUDGE_PAIR_QUESTIONS.get(kind, JUDGE_PAIR_DEFAULT)
```
<!-- 인용 끝 -->
