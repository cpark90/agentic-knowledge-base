---
id: https://agentic-knowledge-base.dev/id/chunk/0ad858ee-8ce8-4e5b-89f5-c28ca1285207
type: decision
level: logical
title_ko: 평평한 타입 목록·족 안 수치 신뢰도·족 신설·코드 엣지의 코어 편입은 기각된다
title: A flat type list, numeric confidence within a family, new families, and code edges in the core are rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-dependency-graph-design}, {resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T14:40:00+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/b6248cd7-b607-4c13-adde-c2ee0f57a5a3
---
**대안** — 넷을 기각한다.

| 대안 | 기각 이유 |
|---|---|
| 기존 타입을 족 없이 평평하게 둔다 | 참조·관련성 족이 비어 있다는 사실이 드러나지 않는다. 전파와 우선순위를 타입마다 따로 적어야 한다 |
| 같은 족 안에서 LARGER의 엣지 신뢰도 ω로 순위를 매긴다 | 수치 신뢰도를 폐기했다(`confidence` deprecated). 선호는 증거 종류의 서열에서 파생된다 |
| 필요할 때 족을 새로 만든다 | 2026-09-23 유저 승인이 잎으로만 확장하도록 정했다. 족 단위 질의가 새 잎을 자동으로 보는 성질이 유지된다 |
| `imports`·`invokes`를 코어의 의미 의존 잎으로 둔다 | 코드 저장소 그래프(LARGER)의 엣지라 골격이 아니라 개발 프로파일의 몫으로 정했다. 코어에 없다 |
