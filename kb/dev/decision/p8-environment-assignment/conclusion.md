---
id: https://agentic-knowledge-base.dev/id/chunk/225ea6bb-00d7-4447-a0b3-2ae33d5f4880
type: decision
level: concrete
title_ko: 검증 청크는 판정 가능한 가장 낮은 단계에 할당한다
title: Each verification chunk goes to the lowest step that can judge it
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f715c53f-c9bd-49cc-b580-6e2d2343cd5c, https://agentic-knowledge-base.dev/id/chunk/5fa5f214-c074-42b7-b2a1-fadba6620193]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0134]
part_of: https://agentic-knowledge-base.dev/id/composite/12df135b-c37d-48d8-b768-8279da163438
composite: {id: https://agentic-knowledge-base.dev/id/composite/12df135b-c37d-48d8-b768-8279da163438, title_ko: 검증 청크의 환경 할당, title: Assigning verification chunks to environments}
---
**결론** — **각 검증 청크는 그것을 판정할 수 있는 가장 낮은 단계에 할당한다.** 할당은 태그(0.5절)에 `env:` 범주로 기록한다.

- 청크 하나의 동작 → 1 단위 · 계약 정합 → 2 모델
- 여러 모듈의 상호작용, 순서·동기화 요인 → 3 소프트웨어 루프
- 실제 인프라의 성능·용량 특성 → 4 하드웨어 루프
- 실제 외부 서비스의 실제 응답 → 5 격리 실환경
- 실제 사용자 행동 분포 → 6 실환경 (관측만)

**할당 근거는 검증 청크의 결함 요인 태그다** — 실행 요인은 1~2단계에서 잡히고, 상호작용 요인은 3단계 이상이 필요하며, 인지 요인은 에이전트 검증 3단계가 필요하다. 요인 분류가 환경 할당을 결정한다.

**logical 공간 커버는 단계별로 합산한다.** ODD의 한 값 조합이 어느 단계에서든 한 번 검증되면 커버된 것이다. 단, **6단계 관측은 커버리지에 넣지 않는다.**
