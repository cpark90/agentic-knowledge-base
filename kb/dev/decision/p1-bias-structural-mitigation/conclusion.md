---
id: https://agentic-knowledge-base.dev/id/chunk/9d8897c0-9466-4e86-b27c-60451367d0c9
type: decision
level: concrete
title_ko: 편향마다 대응하는 구조적 장치를 표로 고정한다
title: Fix a table mapping each bias to a structural mitigation
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T21:30:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f715c53f-c9bd-49cc-b580-6e2d2343cd5c, https://agentic-knowledge-base.dev/id/chunk/0c3ad8ca-9415-4261-a748-55d6db29f1c7]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0038, https://agentic-knowledge-base.dev/id/chunk-d0039]
part_of: https://agentic-knowledge-base.dev/id/composite/d3a0bc2e-b147-4eca-ad4a-3649472ea570
composite: {id: https://agentic-knowledge-base.dev/id/composite/d3a0bc2e-b147-4eca-ad4a-3649472ea570, title_ko: 편향의 구조적 완화, title: Structural bias mitigation}
---
**결론** — 에이전트 편향 각각에 이 체계의 어느 장치가 대응하는지를 표로 고정한다.

| 편향 | 발현 | 구조적 완화 |
|---|---|---|
| 학습자료 종속 | 낯선 이름을 아는 것으로 오인 | 0.3절 접두어, 온톨로지 밖 어휘 거부 |
| 과도한 순응 | 근거 없이 후보 하나를 고름 | Part IX — 후보 여럿이 정상 상태 |
| 최신성 편향 | 마지막 청크 과대평가 | 라벨 목록은 순서 없음 — 순서는 복합체가 결정 |
| 첫 정보 고착 | 처음 읽은 결정에 묶임 | 후보 링크가 남아 있는 한 재검토 가능 |
| 확인 편향 | 일치하는 증거만 봄 | `verifies` 없는 결정이 커버리지에 드러남 |
| 자기 검토 실패 | 자기 출력을 검증했다고 믿음 | 검사 게이트는 에이전트 밖 — 규칙·shape가 판정 |

공통 원리 — **명시적 구조가 내부 추론을 부분 대체한다.** 구조에 쓰는 비용은
추론에 쓰는 토큰을 줄인다.
