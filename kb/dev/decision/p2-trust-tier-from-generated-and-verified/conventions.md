---
id: https://agentic-knowledge-base.dev/id/chunk/d65b0106-a805-4838-a729-85099d7b0206
type: decision
level: concrete
title_ko: 규범 문서 규약 — 신뢰 등급은 generated.by와 verified에서 질의로 얻고 검증 뒤에 바뀐 항목은 게이트가 거부한다
title: Normative-document conventions — The trust tier is queried from generated.by and verified, and the gate rejects items changed after verification
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:13:51+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/3255e515-87cf-431e-8910-100f7849129f
---
**규약** — `p2-trust-tier-from-generated-and-verified`의 결론을 규범 문서에 싣는 문장이다.

규약: [지킴] `generated: {by, at}`의 `by`는 OKF 행위자 표기다. 도구는 `<생성기>/<버전>`, 사람은 `human:<id>`로 적는다. **검증하지 않은 것을 `verified`에 적지 않는다.** 미검증이 정직한 상태다. 검증 뒤 내용을 고치면 게이트가 거부한다. **`artifact` plane은 예외다** — 코드 청크의 `verified`는 사람 도장이 아니라 **테스트 통과 도장**(`process:bazel-test` + 리비전)이고 수정마다 재판정이 자동이다 (`p7-code-extraction-direction`, 2026-09-30).
규약: 신뢰 등급 | `generated.by` 필수, `verified`가 없으면 미검증. `human:` 접두어가 사람 검토 등급. 상세는 §1의 신뢰 등급 절이다
규약: `generatedBy` 필수 | 누가 만들었는지 없는 항목을 만들 수 없다
규약: `generatedAtTime ≤ verifiedAt` | **검증 뒤에 내용이 바뀌면 FAIL** — 사람이 검증한 항목을 에이전트가 고치고 재검증하지 않는 경우를 잡는다
