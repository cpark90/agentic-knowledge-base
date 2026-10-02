---
id: https://agentic-knowledge-base.dev/id/chunk/adf4efcc-f323-49f3-87da-e81bb49bf4f5
type: artifact
level: executable
title_ko: 함수 body_token_limit (tools/kb_lib.py)
title: function body_token_limit in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/6b96d312-0c81-452d-8431-76ec85445dda
---
**함수** — `body_token_limit(plane)` 다. plane 의 본문 토큰 수 상한 — 표에 없으면 기본 1,092 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def body_token_limit(plane: str | None) -> int:
    """plane 의 본문 토큰 수 상한 — 표에 없으면 기본 1,092 다. 이 함수가 단일 판정처다.

    shape(kb/ontology/shapes/token-budget-shapes.ttl)는 이 표의 RDF 표현이고 게이트 `token-budget`
    (validate check_token_budget)이 둘의 동일성을 강제한다 — `residency` 와 같은 형이다 (M1 단일 정의처).
    """
    return BODY_TOKEN_LIMITS.get(plane or "", MAX_BODY_TOKENS)
```
<!-- 인용 끝 -->
