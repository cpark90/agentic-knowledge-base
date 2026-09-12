---
id: https://agentic-knowledge-base.dev/id/chunk/ea6fd937-f144-4fb0-8157-5b8ed5322307
type: decision
level: logical
title_ko: 상한 없는 후보 집합은 라벨 인터페이스를 깨뜨린다
title: An unbounded candidate set breaks the label interface
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/24a2256b-3151-4896-a1f5-712d76f8b4fc
---
**근거** (노트 9.7절) — 읽기 응답은 청크 라벨 목록이 기본이고(4.4절), 후보 링크는 그 목록에 함께 실려야 유저와 에이전트가 무엇이 열려 있는지 본다. 후보가 무제한이면 목록이 본문 예산을 먹고, 라벨 우선 인터페이스가 무너진다.

복원의 `k`에 같은 상한을 두는 이유도 같다 — 임베딩 검색은 항상 순위를 내놓으므로 자르는 지점을 밖에서 정해 주지 않으면 잘리지 않는다.
