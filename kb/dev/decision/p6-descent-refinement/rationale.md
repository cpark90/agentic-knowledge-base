---
id: https://agentic-knowledge-base.dev/id/chunk/bae9ece6-74f9-4c58-a832-e4a3bc91e4e5
type: decision
level: logical
title_ko: 왜 이 값인가가 기록되지 않으면 정제 단절이 재현된다
title: Without recorded value rationale the descent break recurs
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/3eec3426-b051-4594-8d32-be0867520885
---
**근거** (노트 6.2절) — 특히 logical → concrete에서 "왜 이 값인가"가 기록되지 않으면 정제 단절이 그대로 재현된다. 값만 남고 근거가 사라지면 다음 세션은 그 값을 검증할 수도 바꿀 수도 없다.

- 표본 추출 근거(등가분할·경계값·조합)는 커버리지(7.7절 logical 공간 커버)의 재료이기도 하다. 근거가 없으면 **무엇이 시험되지 않았는지도** 계산되지 않는다.
- 도메인을 온톨로지 하위 개념으로 묶는 이유는 후보 목록이 세션마다 달라지는 것을 막기 위해서다. 어휘를 먼저 늘리게 하면 후보 추가가 검토를 거친다 (r-017).
- 각 전이의 통과 조건은 6.8절 전이 게이트가 판정한다. 근거를 남기라는 규약과 링크 생성을 게이트에 묶는 강제가 짝이다.
