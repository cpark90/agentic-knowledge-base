---
id: https://agentic-knowledge-base.dev/id/chunk/3d7fb8e9-c078-4615-b4dd-d8325af0bffb
type: decision
level: concrete
title_ko: 계약이 구현보다 먼저 확정되고 계약 logical이 V&V 기준의 직접 재료다
title: Contracts are fixed before implementation, and contract logical is the direct material of V&V criteria
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/opus-5, at: 2026-09-10T20:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f4facde9-b206-4be7-8599-3e373e6d3bc0, https://agentic-knowledge-base.dev/id/chunk/63f17c2d-3fdf-4fd0-b05a-ca7b6b89ce46]
composite: {id: https://agentic-knowledge-base.dev/id/composite/5957a996-1394-4279-8e3c-31b55c586f62, title_ko: 계약 우선, title: Contract first}
part_of: https://agentic-knowledge-base.dev/id/composite/5957a996-1394-4279-8e3c-31b55c586f62
---
**결론** — **계약이 구현보다 먼저 확정된다.** `contract` abstract(시그니처)가 `decision` logical과 같은 단계에서 나오고, 구현은 그 시그니처를 구현한다. 계약 없이 구현하고 나중에 시그니처를 추출하는 것은 정제 단절이다.

계약의 logical(사전·사후조건, CEL)이 V&V KB 합격 기준의 **직접 재료**다. 사후조건이 곧 기준의 판정식이 되므로, 계약 logical이 비어 있으면 V&V가 기준을 만들 수 없다 (노트 7.5절). 게이트 총람의 "계약 선행"(verify)이 이를 검사한다 (6.7절).
