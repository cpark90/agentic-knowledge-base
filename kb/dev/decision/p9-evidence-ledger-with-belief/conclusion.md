---
id: https://agentic-knowledge-base.dev/id/chunk/9deed62a-70ad-4a87-99a2-73c11e1a4453
type: decision
level: concrete
title_ko: 링크의 증거는 극성 있는 항목의 증거 기록이고 상태 전이 규칙은 그것을 읽으며 믿음 정도는 병기하고 동률만 깬다
title: Link evidence is a ledger of signed entries read by the transition rules; a degree of belief sits alongside and only breaks ties
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T19:33:51+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T19:33:51+09:00}]
layer: methodology
refines: [https://agentic-knowledge-base.dev/id/chunk/f715c53f-c9bd-49cc-b580-6e2d2343cd5c, https://agentic-knowledge-base.dev/id/chunk/33419d0a-16bb-46ee-b5c0-7a84026523fd, https://agentic-knowledge-base.dev/id/chunk/2c574d24-71bb-4ea1-9812-0b2d0dc22395]
supersedes: [https://agentic-knowledge-base.dev/id/chunk/d3a36010-25a1-417b-b2e7-875ccc6955ce]
composite: {id: https://agentic-knowledge-base.dev/id/composite/724d0dfe-3f2e-4bc6-bf43-8a3580b089d7, title_ko: 믿음 정도를 병기하는 증거 기록, title: The evidence ledger with belief alongside}
part_of: https://agentic-knowledge-base.dev/id/composite/724d0dfe-3f2e-4bc6-bf43-8a3580b089d7
---
**결론** — 후보에는 증거 항목의 목록이 붙고, 항목은 종류와 참조, 극성의 세 값을 갖는다. 종류는 10.8절의 근거 유형에 실행과 판정, 유저 결정을 더한 것이고, 극성은 지지나 반박이다. **상태 전이 규칙은 증거 기록을 읽고, 확률로 합산한 값을 읽지 않는다.** 증거 기록에서 계산한 믿음 정도는 후보와 링크 곁에 병기하고 선호의 동률을 깨지만, 상태를 바꾸지 않는다(r-011 개정, Q90-a, Q109-b). 동률 깨기의 규칙은 `p9-preference-partial-order`가, 계산과 보정은 설계 공간 '믿음 정도의 계산과 보정'이 정한다.

| 규칙 | 조건 | 결과 |
|---|---|---|
| 유저 확정 | 유저 결정의 지지 | 확정 |
| 확정 가능 | 구축이나 실행의 지지가 하나 이상이고, 반박이 없고, `when`이 참이고, 다른 후보가 전부 배제됨 | 확정 제안 |
| 보류 | 판정, 임베딩, 세션 공동 읽기의 지지만 있음 | 확정 근거가 부족해 열린 채로 둠 (10.4절) |
| 반박 | 실행의 반박이 하나 이상 | 후보면 배제하고 `eliminated_by: run`을 적음, 확정이면 무효 |
| 충돌 | 같은 후보에 지지와 반박이 함께 있음 | 열린 채로 두고 유저 큐에 올린다. 자동으로 풀지 않는다 |

**유저 결정은 서열 밖의 확정 권한이다.** 유저 결정은 `p10-candidate-and-confirmed-link`가 말하는 유저의 확인이고, 참조는 `Q-NNNN#Qn`이며 질문 번호 이전의 기록은 `legacy/<파일 이름>.md`다(Q111-a). **판정은 확정 근거가 아니다.** 판정은 `p8-judge-session-agreement`의 판정자 세션이 낸 결과이고 확신도를 함께 적으며, 성립이면 지지, 불성립이면 반박이다. 서열은 구축, 실행, 동시 편집, 공동 커버, 판정, 임베딩, 세션의 차례다(Q118-a).

**실행 증거가 특별하다.** 검증기의 통과는 `verifies`뿐 아니라 그것이 검증하는 `satisfies` 후보에도 지지를, 실패는 반박을 적는다. 이것은 링크가 아니라 증거 기록 항목이어서 8.5절의 방향 규칙을 깨지 않는다. 확정 링크도 증거 기록을 유지하고, "왜 아직 유효한가"에 마지막 지지 증거로 답한다. 이 저장소는 `agt:Evidence`에 종류와 참조, 극성을 두고, `agt:confidence`는 폐기한 채로 두며 믿음 정도는 새 속성으로 둔다.

**게이트** `verify`(노트 9.10절 할당 근거) — 증거 기록 규칙의 verify 질의 둘 `confirmed-without-evidence`·`confirmed-with-refutation`이 증거 없는 확정과 반박을 가진 확정을 거부하고, 질의 `link-state-class-mismatch`가 링크의 상태와 클래스의 불일치를 거부한다. 후보가 둘 이상인데 확정된 링크를 직접 거부하는 질의는 없으므로 이 기계화는 부분이다. 확정·구축·복원·후보 링크의 수는 문서에 적지 않고 `bazel build //kg:metrics`의 링크 절과 `//kg:link_candidates`가 낸다. 2026-10-01 측정에서 손으로 적은 넷이 전부 낡아 있었기 때문이다. 해소는 저작자가 증거 항목을 더하거나 확정을 후보로 되돌리는 것이다.
