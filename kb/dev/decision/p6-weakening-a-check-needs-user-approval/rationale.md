---
id: https://agentic-knowledge-base.dev/id/chunk/962b8177-1fdd-445b-90a6-cec2e6b751df
type: decision
level: logical
title_ko: 게이트를 약화해 통과시키면 FAIL에 산출물을 고친다는 규칙이 무력해지고 숨은 면제는 보이지 않는다
title: Passing a gate by weakening it voids the rule that a FAIL fixes the output, and a hidden waiver cannot be seen
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}, {resource: https://agentic-knowledge-base.dev/id/doc-agrtls-practices-review}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T18:15:25+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/4d357229-2256-4521-a837-0444b804d2a0
---
**근거** — 확인한 사실은 다섯이다.

- `AGENTS.md` 황금률 1은 FAIL이면 고친 파일을 수정하고 shape·게이트 코드를 약화하지 않는다고 정한다. 유저 승인은 그 금지를 여는 유일한 경로다.
- 2026-09-12 실측에서 면제가 코드에 숨어 있었다(`channel_lint.EXEMPT`, `consistency`의 "검증" 예외). 같은 날 유저가 수렴 규칙 C("오탐은 침묵이 아니라 선언으로")를 채택해 면제를 `docs/waivers.md`로 옮겼다. 선언된 면제는 사유와 판정자를 갖고 집계 밖에서도 목록에 남는다.
- 2026-09-21 `p8-agent-verification-target`은 `verifies`의 대상을 카탈로그 개체로 넓히는 안을 검사 약화로 판정했다. 그 안은 유저 승인 사항이었고 결정은 규칙을 바꾸지 않는 쪽을 택했다.
- 게이트 등록부 `GATES`에서 id를 지우면 그 이름을 쓰는 도구가 적재 시점에 죽는다(음성 시험, 유저 지시 2026-10-01). 검사를 조용히 빼는 길이 기계적으로 막혀 있다.
- 면제를 약화에서 빼는 근거는 유저 답 Q7-b(2026-10-03)다. 면제는 이미 선언으로 공개되고 판정자와 사유가 기록되므로 유저는 사후에 `docs/waivers.md`에서 본다. 면제 표 여섯 행(2026-09-12~10-01)의 판정자가 전부 orchestrator인 실물이 그 규약에 맞는다.

미확정: 2026-09-01 원문이 약화를 유저 승인 사항으로 둔 이유는 무엇인가 — 원문은 이유를 적지 않았다.
