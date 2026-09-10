---
id: https://agentic-knowledge-base.dev/id/chunk/816b1ccf-fcbc-489c-9fde-cff6cf7d1379
type: decision
level: logical
title_ko: 임베딩을 1차 인덱스로 두는 안과 전문 검색을 기본으로 두는 안은 배제
title: Embedding as the primary index and full-text as the default are both ruled out
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/5133b9c7-e45d-462d-ad99-20e3b49ef15c
---
**대안**

- **임베딩 유사도를 1차 인덱스로 쓰는 안** — 배제. 순위가 곧 답이 되어 판정
  근거가 사라지고, 반환량이 KB 크기를 따라 커져 예산 상한이 깨진다. 후보
  추림에만 쓰고 결과는 라벨 목록으로 낸다.
- **본문 전문 검색을 기본으로 두는 안** — 배제. 라벨 부패와 잘못된 분할이라는
  신호를 가린다.
