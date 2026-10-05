---
id: https://agentic-knowledge-base.dev/id/chunk/2f788be8-0d51-4cda-ae66-d1de6348cae8
type: decision
level: concrete
title_ko: shape는 강화만 하고 기존 제약을 약화하는 변경은 유저 승인 사항이다
title: Shapes are only strengthened, and a change that weakens an existing constraint needs user approval
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/f987e08c-fba7-43d8-9e0a-903edbd9375a]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T14:00:00+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/38cd00fb-321b-43e9-8261-b1cfbd910e35
composite: {id: https://agentic-knowledge-base.dev/id/composite/38cd00fb-321b-43e9-8261-b1cfbd910e35, title_ko: shape는 강화만 한다, title: Shapes are only strengthened}
---
**결론** — shape는 **강화만** 한다. 기존 제약을 약화하는 변경은 유저 승인 사항이다.

- 약화의 예는 `sh:maxCount` 완화와 `sh:in` 확장이다.
- 게이트가 실패하면 shape가 아니라 고친 파일을 수정한다. 게이트가 틀렸다고 판단되면 게이트를 고치지 않고 `question`을 보낸다(`AGENTS.md` 황금률 1, §작업).
- 위반을 집계에서 빼는 수단은 shape 약화가 아니라 `docs/waivers.md`의 면제 선언이다. 면제가 적용되면 shape는 그대로이고 `WAIVED [shacl]` 줄이 남는다(`tools/validate.py`).

이 규약을 판정하는 게이트는 없다. 리뷰 규범이다.
