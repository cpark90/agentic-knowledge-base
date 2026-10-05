---
id: https://agentic-knowledge-base.dev/id/chunk/fcf08153-571e-425c-92ce-dda33cc4c022
type: decision
level: logical
title_ko: 입력을 개수만 적는 안과 union 구성을 입력 줄 밖에 두는 안은 기각된다
title: Stating only the input count and keeping the union composition outside the input line are rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-generated-document-standards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T23:13:50+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T23:15:22+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/77024f86-3aeb-445d-ad01-6a1bcd9eee54
---
**대안** — 넷을 기각한다. 뒤의 둘은 유저 답 Q40(2026-10-04)의 기각안이다.

| 대안 | 기각 이유 |
|---|---|
| 입력이 많으면 개수와 지문만 적는다 | 어느 파일이 들어갔는지 문서 안에서 판별되지 않는다. `p12-generated-document-header`가 "개수만 적지 않는다"를 이미 정했다 |
| union 구성은 도구 문서(`docs/tools.md`)에만 적는다 | 2026-09-19 실측의 상태다. 사본만 손에 든 독자가 세 트리플 수의 차이를 판별하지 못했다 |
| 트리플 차를 별도 절 `## union 구성`에 적는다(Q40-b) | 생성 문서 규약에 절 하나가 는다. 증분은 `입력` 줄의 총수와 한 줄에 있어야 합이 총수인지 G4가 그 줄 하나로 판정한다 |
| 트리플 차를 비교 뷰 하나로 새로 낸다(Q40-c) | 차의 원본이 `kb_lib.gendoc_union` 밖에 하나 더 생긴다. 사본만 손에 든 독자는 뷰 없이 차를 판별하지 못한다 |
