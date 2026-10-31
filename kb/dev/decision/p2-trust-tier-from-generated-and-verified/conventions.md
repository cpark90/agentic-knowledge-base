---
id: https://agentic-knowledge-base.dev/id/chunk/d65b0106-a805-4838-a729-85099d7b0206
type: decision
level: concrete
title_ko: 규범 문서 규약 — 신뢰 등급은 generated.by와 verified에서 질의로 얻고 검증 뒤에 바뀐 항목은 게이트가 거부한다
title: Normative-document conventions — The trust tier is queried from generated.by and verified, and the gate rejects items changed after verification
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T01:24:08+09:00}, {by: developer/claude-opus-5-5, at: 2026-10-24T22:08:51+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/3255e515-87cf-431e-8910-100f7849129f
---
**규약** — `p2-trust-tier-from-generated-and-verified`의 결론을 규범 문서에 싣는 문장이다.

규약: [지킴] `generated: {by, at}`의 `by`는 OKF 행위자 표기이며, 도구는 `<생성기>/<버전>`, 사람은 `human:<id>`로 적는다. **검증하지 않은 것을 `verified`에 적지 않는다.** 미검증이 정직한 상태이고, 검증 뒤 내용을 고치면 재검증 항목을 덧붙일 때까지 게이트가 거부한다. `verified`는 판정 이력이라 덮어쓰지 않고 누적한다. **다만 `artifact` 지식 종류는 예외다.** 코드 단위 지식의 `verified`는 사람 도장이 아니라 `process:bazel-test`와 리비전으로 된 **테스트 통과 도장**이고, 수정마다 재검증이 자동으로 일어난다(`p7-code-extraction-direction`, 2026-09-30).
규약: 신뢰 등급 | `generated.by`가 필수이고 현재 내용 이후(`at ≥ generated.at`)의 `verified` 항목이 없으면 미검증이다. 그 항목에 `human:` 접두어가 있으면 사람 검토 등급이며, 상세는 §1의 신뢰 등급 절에 있다
규약: `generatedBy` 필수 | 누가 만들었는지 없는 항목을 만들 수 없다
규약: 가장 늦은 `verifiedAt` ≥ `generatedAtTime` | **검증 뒤에 내용이 바뀌고 재검증 항목이 없으면 FAIL이다.** 사람이 검증한 항목을 에이전트가 고치고 재검증하지 않는 경우를 잡는다
