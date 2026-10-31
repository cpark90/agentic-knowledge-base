---
id: https://agentic-knowledge-base.dev/id/chunk/28fe3081-ef50-4aed-8c68-05a2cd771193
type: decision
level: logical
title_ko: 등급의 재료는 OKF의 실제 필드이고 검증 시각 검사가 그래프 밖이던 승인을 기계 검사로 내린다
title: The tier is built from actual OKF fields, and the verification-time check brings approval, once outside the graph, down to a machine check
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}, {by: developer/claude-opus-5-5, at: 2026-10-24T22:08:51+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/3255e515-87cf-431e-8910-100f7849129f
---
**근거** — 등급의 재료는 OKF v0.2의 실제 필드다. 노트 부록 E.2는 판정 이력을 `verified` 목록으로 사상하고 사람 검토를 `human:` 접두어로 적는다(2026-09-10 결정). 목록이 곧 이력이므로 별도 `trust` 키를 두지 않는다(`p2-judgement-history-in-verified`).

둘째 검사가 요점이다(`docs/rules.md` 신뢰 등급 절). 결정은 유저 승인이 `stable` 전이의 조건인데 그 승인이 그래프에 기록되지 않았고 채널의 승인 표지는 그래프 밖이었다. `verified`가 둘을 잇고 쓰기 지식 종류 경계가 규약에서 기계 검사로 내려온다. 이 검사는 사람이 검증한 항목을 에이전트가 고치고 재검증하지 않는 경우를 잡는다.

shape는 2026-09-10에 들어왔다. 그날 측정에서 생성자는 `claude/fable-5`·`claude/opus-5`뿐이었고 사람 검토는 0건이었다. 현재 수는 `metrics`가 `human:` 접두를 세어 낸다. 검토를 마친 쓰기 권한 역할이 `verified`를 붙이는 수단은 `endorse`다.

`artifact` 예외의 근거는 `p7-code-extraction-direction`(2026-09-30)에 있다. 코드는 수정마다 재검증이 자동이다.

**개정** — 유저는 판정 이력을 `verified` 목록에 누적하기로 했다(Q-0064#Q159-a, 2026-10-24). 옛 검사는 생성 시각을 모든 검증 시각과 비교해, 내용을 고치면 옛 판정 항목이 모두 위반이 되었다. 그래서 재검증이 목록을 덮어썼고 지식 파일 150개에서 판정 항목 158개가 지워졌으며, 그중 유저 승인이 둘이었다. 검사는 이제 가장 늦은 검증 시각 하나와 생성 시각을 비교한다. 받아들이는 그래프가 늘어나므로 검사 약화이고 유저가 승인했다. "내용이 바뀐 뒤 재검증 없이 신뢰를 주장할 수 없다"는 불변식은 그대로 지켜진다. 등급도 같은 불변식을 따르도록 현재 내용 이후의 항목만 센다.
