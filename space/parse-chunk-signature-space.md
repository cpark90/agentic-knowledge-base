---
id: https://agentic-knowledge-base.dev/id/chunk/6e7ec459-6bdf-4563-ba4d-cf20b6379426
type: agt:Space
level: logical
title_ko: parse_chunk 함수는 어느 시그니처로 위반을 알리는가
title: Which signature the parse_chunk function uses to report violations
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: developer/claude-opus-5-5, at: 2026-10-15T18:37:22+09:00}
---
함수 `parse_chunk`의 시그니처 후보 가운데 파일 복합체 `tools/chunk2kg.py`가 어느 것을 정제하는가가 변수다. 코드 링크의 자리가 파일 복합체이기 때문이다(결정 `p7-code-links-on-file-composite`). 후보는 셋이다. 예외를 던지는 형태, 결과 객체를 반환하는 형태, 오류 목록을 반환하는 형태다. 세 형태는 저장소의 다른 함수에 이미 공존한다.

현재 코드는 예외를 던지는 형태다. 그 확정의 증거는 파일 복합체의 구축 기록이고, 후보는 결정 `p6-gate-catalogue`의 결론(실패 메시지·종료 코드)을 `satisfies`로 가리킨다. 결과 객체와 오류 목록을 직접 기각한 결정 문장은 없어 두 후보는 열려 있다. 결정 `p6-gate-tool-code-structure`의 `check_* -> list[str]`는 검사 함수의 권장이고 파서인 이 함수를 정하지 않는다.

```yaml
variable:
  from: https://agentic-knowledge-base.dev/id/composite/f7d6eec7-bef4-4e94-ac55-36e7dda654ce
  kind: refines
status: open
candidates:
  - to: https://agentic-knowledge-base.dev/id/chunk/ed5b49af-8e81-4f81-b74e-9f795c588072
    state: confirmed
    evidence: [{kind: constructionRecord, ref: https://agentic-knowledge-base.dev/id/composite/f7d6eec7-bef4-4e94-ac55-36e7dda654ce}]
  - to: https://agentic-knowledge-base.dev/id/chunk/7d400d4e-5ef5-4ec7-9efa-3c9fb35c0aea
    state: open
  - to: https://agentic-knowledge-base.dev/id/chunk/438d6c82-6afd-421b-bd64-8343053438ce
    state: open
```
