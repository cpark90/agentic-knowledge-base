---
id: https://agentic-knowledge-base.dev/id/chunk/4bcdf854-9ebe-4cb0-a55a-a670b491c3d3
type: decision
level: logical
title_ko: 적지 않은 것과 검토한 뒤 제외한 것은 다르다
title: Unmentioned is not the same as reviewed-and-excluded
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/80a7e3df-fc4f-452e-94fc-4acead84d77b
---
**근거** (노트 3.2절) — restrictive 모드에서는 적지 않은 것이 전부 제외되지만, "적지 않은 것"과 "검토한 뒤 제외한 것"은 다르다. 후자를 기록하지 않으면 다음 검토자가 같은 검토를 반복하고, 제외 이유가 유효한지도 재판정할 수 없다.

판정 방법이 필수인 이유는 그것 없는 속성으로는 3.5절 실행 시 모니터링을 할 수 없기 때문이다. 0.4절 "모든 조건은 객관적 판정 방법을 갖는다"가 ODD에서 강제되는 자리다.

3갈래(정적·환경·동적)는 온톨로지 `related/condition`의 분류를 그대로 쓴 것이므로 절 구성이 어휘와 어긋나지 않는다.
