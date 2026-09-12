---
id: https://agentic-knowledge-base.dev/id/chunk/8e83391e-5fd2-499b-881c-37e6f9cb60f1
type: decision
level: concrete
title_ko: 실행 시 모니터링이 이탈을 잡고 이탈은 결함이 아니라 신호다
title: Runtime comparison catches the exit; the exit is a signal, not a defect
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/e0d0bf5c-8c1c-4638-9f64-89f94185d366, https://agentic-knowledge-base.dev/id/chunk/fd0d3d18-4aab-4c4c-8f72-41702860b68c]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0061]
part_of: https://agentic-knowledge-base.dev/id/composite/ce551363-f48f-40a3-95f8-b35a0ddd377d
composite: {id: https://agentic-knowledge-base.dev/id/composite/ce551363-f48f-40a3-95f8-b35a0ddd377d, title_ko: ODD 이탈은 신호다, title: An ODD exit is a signal}
---
**결론** — ODD는 설계 시점의 조건이다. 실행 시점의 **실제 조건**은 `run-kg`에 관측으로 기록되며, 둘을 대조한다.

- 모든 속성이 ODD 안 → 정상
- 속성 하나 이상이 ODD 밖 → **ODD 이탈**
- 판정 불가 속성 존재 → `unverified`. 판정 방법 보완 대상

**ODD 이탈은 결함이 아니라 신호다.** 설계 범위 밖 상황에 들어섰다는 뜻이고, 대응은 둘 중 하나다.

1. **작업 중단 + 유저 에스컬레이션** — 기본값. 이탈한 속성에 의존하는 **모든** 항목이 무효화 대상이 된다. 가정 위반이 항목 하나를 무효화하는 것보다 범위가 넓다
2. **ODD 확장 제안** — 이탈 조건이 반복되면 설계 범위를 넓힐 후보다 (3.6절)

이탈 감지는 판정 방법이 있는 속성에서만 가능하다. **이것이 판정 방법이 필수인 두 번째 이유다.**
