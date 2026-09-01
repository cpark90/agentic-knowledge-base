---
iri: https://agentic-knowledge-base.dev/id/chunk-d0136
plane: decision
level: concrete
label_ko: 합격 기준은 시나리오와 별도 청크
label_en: Pass criteria live in a chunk separate from the scenario
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — 시나리오마다 합격 기준을 **별도 청크로** 두고, `verifies` 링크의
속성으로 시나리오에 붙인다. 기준 없는 `verifies` 링크는 검사 게이트가
거부한다.

**근거** (노트 10.1절)
- 자극(시나리오)과 판정(기준)을 한 청크에 두면 **기준 변경이 시나리오
  변경으로 보인다.** 그러면 같은 자극에 대한 판정 강화가 이력에서 사라진다.
- "검증했다"는 주장에 "무엇으로"가 없으면 검증이 아니다 — 그래서 게이트가
  기준 없는 링크를 막는다.
- 기준 유형 — **명세 대조**(출력이 `contract`·`schema` 청크와 일치),
  **불변식**(실행 전후로 유지될 조건: 총량 보존, 참조 무결성), **임계**
  (측정값이 범위 안: 응답 시간 < 200ms), **가정 유지**(실행 중
  `agt:Assumption`이 깨지지 않음: ODD 이탈 0회).
- 에이전트 대상의 기준 — **산출물 품질**(산출 청크가 shape 통과, `refines`
  연쇄 완결, 고아율 0)과 **인지**(situation 대비 누락률, 10.3절).
