---
id: https://agentic-knowledge-base.dev/id/chunk-d0047
type: decision
level: concrete
title_ko: 표준 상위 온톨로지 위에 구축한다
title: Build on a standard upper ontology
status: deprecated
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 프로젝트 온톨로지를 맨바닥에서 짓지 않고 표준 상위 온톨로지 위에
구축한다. 후보는 ISO/IEC 21838-2로 표준화된 BFO다.

**근거** (노트 2.2절)
- 0.0절 표준어 원칙의 연장이다. "결정은 정보 내용 개체인가 과정인가",
  "하네스는 인공물인가 역할인가" 같은 최상위 분류를 프로젝트가 처음부터
  정하지 않는다 — 상위 온톨로지가 이미 정해 두었다.
- 같은 상위 온톨로지 위에 선 외부 온톨로지를 가져올 때 개념 충돌이 줄어든다.
- 상위 온톨로지 준수 여부를 기계적으로 검사하는 도구가 이미 존재한다. 그
  검사가 온톨로지 위생(2.5절)의 항목이 된다.
