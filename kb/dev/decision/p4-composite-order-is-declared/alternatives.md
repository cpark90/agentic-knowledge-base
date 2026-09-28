---
id: https://agentic-knowledge-base.dev/id/chunk/4ac5d37d-7107-4de6-9dbf-f7adce3349b9
type: decision
level: logical
title_ko: 파일명 순서·전 복합체 순서 부여·별도 순서 파일은 기각된다
title: File-name order, order on every composite, and a separate order file are rejected
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-09-29T11:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/c15bc5d0-4f85-4d7b-bdd2-85cca14af3ba
---
**대안** — 셋을 기각한다.

| 대안 | 기각 이유 |
|---|---|
| 파일명 정렬을 순서로 삼는다 | 파일명은 식별자이지 순서가 아니다. 순서를 바꾸려면 파일을 개명해야 하고 개명은 타깃 이름과 라벨을 바꾼다 — 순서 하나를 고치는 데 의존 그래프가 흔들린다 |
| 모든 복합체에 순서를 붙인다 | 순서를 요구하지 않는 묶음(요구의 관심사)에 색인이 붙어 거짓 정보가 된다. 옛 결정이 그것을 명시적으로 금했다 |
| 순서를 별도 파일(`kg/`)에 손으로 쓴다 | 손 복합체 42건을 생성 경로로 옮긴 2026-09-29의 방향과 반대다. 선언과 부분이 다른 파일에 갈리면 어느 날 하나만 고쳐진다 |

부분 청크마다 `index` 키를 두는 안은 검토했으나 기각한다 — 순서는 묶음의 성질이지 부분의 성질이 아니고, 한 부분이 두 묶음에 들 때 색인이 충돌한다(지금은 한 청크가 한 복합체에만 속하지만 규칙이 그것을 금하지는 않는다).
