---
id: https://agentic-knowledge-base.dev/id/chunk/fbacedd4-94d7-4da3-8ab4-01316db02668
type: decision
level: logical
title_ko: 등록하면 옛 표기로 찾고 산문에서는 공식 이름만 쓰게 검사한다
title: Registration lets old spellings be found while prose is checked against the official name
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/8a718aed-4f88-4847-9d00-800c0f14a0e7
---
**근거** (노트 0.8절)

- 등록하면 두 방향이 동시에 성립한다 — 에이전트가 **옛 표기로 검색해도 찾고**,
  산문 생성 시에는 `prefLabel`만 쓰도록 **검사할 수 있다**.
- 라벨 목록이 읽기 응답의 기본 표면이므로(r-013), 어느 이름이 목록에 나타나는
  이름인지가 `prefLabel` 하나로 확정되어야 한다.
- 오타 변형을 `hiddenLabel`에 두는 것은 학습자료 종속(1.2절) 대응이다 —
  에이전트가 아는 이름으로 잘못 쓴 경우에도 올바른 개념에 도달한다.
