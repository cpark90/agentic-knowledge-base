---
id: https://agentic-knowledge-base.dev/id/chunk/09ffb551-1b31-4d30-8a60-1f049bf7aa3e
type: decision
level: logical
title_ko: 에이전트가 제약을 스스로 풀면 판정이 에이전트 안으로 들어온다
title: If an agent loosens a constraint itself, judgement moves inside the agent
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T18:15:16+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/38cd00fb-321b-43e9-8261-b1cfbd910e35
---
**근거** — 출처는 저장소 구축(2026-09-01) 때의 `STYLEGUIDE.md` §2다. 그 원문은 승인 규칙의 원본으로 `AGENTS.md` 워크플로를 가리켰다. 지금 `AGENTS.md` 황금률 1은 "shape·게이트 코드를 약화시키지 않는다"를 적는다.

이 결정의 요구는 "편집은 게이트가 판정한다"다. 그 요구는 판정을 에이전트 밖의 규칙과 shape에 둔다. 에이전트가 제약을 스스로 풀면 판정이 에이전트 안으로 들어온다. 노트 2.5절은 같은 원칙을 온톨로지에 적용한다. 에이전트는 신뢰할 수 없는 센서이고 판정은 컴파일러와 승인자의 몫이다(`p2-term-proposal-workflow`).

면제가 shape를 바꾸지 않는 까닭은 `docs/waivers.md`가 적는다. 면제는 코드에 숨기지 않고 선언한다(agrtls 공통 규칙, 유저 채택 2026-09-12).

면제는 약화가 아니다. 유저 답 Q7-b(2026-10-03)가 면제는 orchestrator가 판정하고 `docs/waivers.md`의 선언으로 공개하며, 약화는 shape·게이트 코드의 변경만이라고 정했다. 면제 표의 판정자 열이 전부 orchestrator인 실물이 이 규약에 맞는다.

미확정: 새 shape의 첫 실행에서 범위를 좁히는 판정(`p6-mass-fail-suspects-the-rule`)이 이 결정의 약화에 드는지 정한 기록이 없다.
