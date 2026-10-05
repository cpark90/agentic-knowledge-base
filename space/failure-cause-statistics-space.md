---
id: https://agentic-knowledge-base.dev/id/chunk/166eeb2d-0cfa-4d72-8e70-3002b1347a97
type: agt:Space
level: logical
title_ko: 실패의 다수는 어휘 문제인가 커버리지 문제인가
title: Whether most failures are vocabulary or coverage problems
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-06T01:15:39+09:00}
---
유저는 미결을 "개선 및 확장이 이루어지는 frontier 포인트"로 보았다(Q54-a).

질문 — 알려지지 않은 위험은 두 원인에서 온다. 어휘에 없는 요인이 어휘 문제이고 알려진 요인의 시험되지 않은 조합이 커버리지 문제다. 대응이 다르다. 전자는 일반화로 어휘를 확장하고 후자는 조합 테스팅으로 시나리오를 넓힌다. 실제 실패에서 어느 쪽이 다수인지 모르면 어디에 투자할지 정할 수 없다. 요구 `r-004`(반복 관측을 어휘·규칙으로 승격한다)에서 이 판정의 기록 방식으로 가는 `refines`가 열려 있다.

이미 정해진 것 — 두 원인의 구분과 각각의 대응은 `p8-unknown-risk-cases`가 정했다. 사후분석이 이 구분을 절차로 쓴다(`p12-incident-postmortem`). 인지·상호작용·실행의 요인 3갈래와 ODC 하위 분류가 알려진 요인 어휘의 초기 집합이다(`p8-defect-factor-taxonomy`·`p8-odc-defect-subtypes`).

현재 상태(2026-10-06 실측) — `defect` 어휘 모듈은 있다. 온톨로지 파일 17개(`kb/ontology/related/defect/`)와 규칙 파일 3개(`kb/ontology/related/defect-rules/`)다. V&V 실행 기록(`run-*`)은 5건이고(`kb/vv/run/` 전체는 충실도·판정 기록을 합쳐 9건) 실패가 있는 것은 1건(fail 24)이다. 실행 기록에 실패 원인을 어휘 공백과 커버리지 공백으로 가르는 자리는 없고 사후분석 사례는 0건이다. 답할 데이터가 아직 없다. 이 저장소가 겪은 실패 두 건은 참고가 된다. 첫째는 ODD 동시 에이전트 한도와 카탈로그 합의의 불일치다. 알려진 요인의 알려진 조합인데 게이트가 없어 검출되지 않았다. 둘째는 분해 시 `p3-out-of-odd-case-tagging`(옛 d-0067)의 누락이다. "절이 기존 항목에 반영됨으로 분류되면 그 절의 모든 확정이 옮겨졌다"는 인지 요인이다. 둘 다 알려지지 않은 요인이 아니었고 첫째는 두 범주 어디에도 들지 않는다.

답이 가르는 것 — 어휘와 시나리오 중 어디에 먼저 투자하는지가 갈린다. 어휘 쪽은 `defect`·일반화이고 시나리오 쪽은 조합 테스팅이다. 실측 전 결정은 추측이다.

선택지 — A는 3분류 기록 형식을 지금 확정하는 안이다(`p8-failure-cause-three-way-record`). 세 분류는 어휘·커버리지·검출 장치 부재다. B는 실측 전 판단을 미루는 안이다. 형식만 정하고 판단은 데이터가 쌓인 뒤에 한다. `p8-unknown-risk-cases`의 대안 청크가 같은 안(실행 기록이 쌓여야 알고 그동안 한쪽에 자원을 몰지 않는다)을 적어 그 청크를 후보로 든다(Q63-a). C는 문헌의 일반 결과를 초기 가설로 두는 안이고 근거가 외부에 있다(`p8-failure-cause-literature-prior`). 세 후보 모두 열려 있다.

```yaml
variable:
  from: https://agentic-knowledge-base.dev/id/chunk/ae4f5c32-39ac-4bc0-b16b-ae8d96dfd901
  kind: refines
status: open
candidates:
  - to: https://agentic-knowledge-base.dev/id/chunk/fa20492f-939f-40a5-994f-04aeec09f90a
    state: open
  - to: https://agentic-knowledge-base.dev/id/chunk/ae25b989-da6d-41f4-9918-fb177c185358
    state: open
  - to: https://agentic-knowledge-base.dev/id/chunk/c5806de1-c235-40ad-b7b0-83cfebac5f1c
    state: open
```
