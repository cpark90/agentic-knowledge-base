---
id: https://agentic-knowledge-base.dev/id/chunk-d0033
type: decision
level: concrete
title_ko: 동의어는 없애지 않고 SKOS 라벨로 등록한다
title: Register synonyms as SKOS labels instead of removing them
status: deprecated
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 0.6절의 "동의어 사용 금지"를 어휘 수준에서 강제하는 방법은
동의어를 **없애는 것이 아니라 등록하는 것**이다. SKOS 라벨 구분을 쓴다.

| 라벨 | 용도 |
|---|---|
| `skos:prefLabel` | 유일한 공식 이름. 한/영 각 하나 |
| `skos:altLabel` | 허용되는 대체 표기. 검색에는 쓰이되 산문에는 쓰지 않음 |
| `skos:hiddenLabel` | 과거 표기, 오타 변형. 검색에만 |

**근거** (노트 0.8절)
- 등록하면 두 방향이 동시에 성립한다 — 에이전트가 **옛 표기로 검색해도
  찾고**, 산문 생성 시에는 `prefLabel`만 쓰도록 **검사할 수 있다**.
- 동의어를 아예 제거하면 옛 표기로 쓰인 기존 문서와 실행 기록이 검색에서
  사라진다. 금지만으로는 이미 존재하는 표기를 처리할 수 없다.
- 오타 변형을 `hiddenLabel`에 두는 것은 학습자료 종속(1.2절) 대응이다 —
  에이전트가 아는 이름으로 잘못 쓴 경우에도 올바른 개념에 도달한다.
