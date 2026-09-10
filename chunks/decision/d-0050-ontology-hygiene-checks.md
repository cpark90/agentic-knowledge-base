---
id: https://agentic-knowledge-base.dev/id/chunk-d0050
type: decision
level: concrete
title_ko: 온톨로지 위생 — 커밋 전 자동 검사와 정규화 직렬화
title: Ontology hygiene - pre-commit checks and canonical serialization
status: deprecated
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 온톨로지 파일 자체가 커밋 전에 통과해야 하는 자동 검사를 둔다:
상위 온톨로지 준수, 정의 완전성, 모듈 경계, 정규화 직렬화. LLM 출력에 대한
검사 게이트(6.7절)와는 별개의 관문이다.

**근거** (노트 2.5절)
- 상위 온톨로지 준수는 모든 개념이 상위 분류 아래에 있는지를, 정의 완전성은
  모든 개념에 한/영 `rdfs:label`과 정의가 있는지를 본다.
- 모듈 경계 검사가 2.3절의 "다른 모듈 개념 재정의 금지"를 실제로 강제한다.
- **정규화 직렬화가 특히 중요하다.** 직렬화 순서가 불안정하면 git diff가
  의미 없는 변경으로 가득 차서 5.5절 무효화 판정의 입력이 오염된다. 출력
  순서를 고정해 diff가 의미 변화만 보여주게 한다.
