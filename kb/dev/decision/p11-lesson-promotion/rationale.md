---
id: https://agentic-knowledge-base.dev/id/chunk/59d82bb0-70da-41be-9d91-a3e6de770855
type: decision
level: concrete
title_ko: 에이전트는 매번 처음부터 시작하므로 쓰기를 지켜야 교훈이 이어지고 반복이 승격의 기준이다
title: Agents start cold, so lessons carry over only if they are written, and recurrence is the promotion criterion
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}, {resource: git:aeb0a58:chunks/decision/d-0017-lesson-promotion.md}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:18:36+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:18:36+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/8bfb469f-8a22-4afb-9348-80b2c95875b3
---
**근거** — 출처는 harness-functional `CLAUDE.md`의 lesson-capture와 lesson-reuse, lesson-promotion guardrail이다.

- 각 에이전트는 콜드 스타트(cold-start)이므로 세션을 시작할 때 역할 메모리를 읽어 특화하고, 끝나기 전에 재사용 지식을 자기 폴더에 써서 축적한다. 쓰기는 자기 역할 폴더에만 하고 파일 하나와 색인 한 줄을 더하며, 이미 있으면 갱신한다.
- 읽기는 세션 시작에 이미 하므로, 쓰기만 지키면 다음 세션이 교훈을 안고 시작한다.
- 반복이 승격의 판정 기준이다. 그래서 한 번 나온 교훈은 메모리에, 두 번 나온 교훈은 규칙에 둔다.

이 규칙은 노트 9.4절 메모리 승격 규칙의 실행 형태다. 승격은 `memory` 지식 종류에서 주제의 지식 종류로 가며, 이것이 일반화의 최소 단위다(`p6-ascent-generalization`).
