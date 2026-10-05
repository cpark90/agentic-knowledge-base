---
id: https://agentic-knowledge-base.dev/id/chunk/cc84d77c-5e58-4d54-88ff-a126f9606f85
type: decision
level: logical
title_ko: 손 TTL 선언 유지·디렉토리 단위 복합체·부분 하나 복합체·패키지 횡단 부분은 기각된다
title: Keeping hand-written TTL declarations, one composite per directory, single-part composites, and cross-package parts are rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T14:50:00+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/7130e6d8-2b81-49eb-b1a3-96d3c7f93ff3
---
**대안** — 넷을 기각한다.

| 대안 | 기각 이유 |
|---|---|
| 복합체를 `composite-kg.ttl`에 손으로 계속 선언한다 | 2026-09-29 유저 답이 도구를 고치는 쪽을 골랐다. 41건이 생성 경로로 옮겨졌다 |
| 디렉토리 하나를 복합체 하나로 둔다 | 평평한 패키지 하나에 복합체 여럿이 서므로 디렉토리로는 가를 수 없다. 결정만 디렉토리 단위다 |
| 부분 하나짜리 복합체를 허용한다 | 부분이 하나면 청크이지 복합체가 아니다(2026-09-29 판정) |
| 패키지를 넘는 부분을 허용한다 | 타깃의 `srcs`가 패키지를 넘지 못해 묶음이 한 액션의 입력 집합이 될 수 없다 |
