---
id: https://agentic-knowledge-base.dev/id/chunk-d0055
type: decision
level: concrete
title_ko: 온톨로지 결함 카탈로그로 설계 결함을 주기 평가한다
title: Periodic ontology evaluation via a pitfall catalogue
status: deprecated
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 2.5절 위생 검사 외에, 표준 온톨로지 결함 카탈로그(pitfall
catalogue)로 설계 결함을 주기적으로 검사한다.

**근거** (노트 2.10절)
- 위생 검사는 파일이 형식을 지켰는지만 본다. 정의 없는 개념, 잘못된 계층
  (`agt:Scope subClassOf agt:Chunk`), 순환 계층, 다의어 개념, 클래스와 개체
  혼동은 형식상 유효해도 설계가 틀린 것이다.
- 검출 수단이 이미 체계 안에 있다: 계층 오류는 상위 온톨로지 준수 검사와
  추론기, 관계 방향 혼동·정의역 치역 미지정은 TIM 검사(8.2절), 고립 개념과
  과설계는 경쟁 질문 대조(2.7절), 동의어를 별개 클래스로 둔 것은 0.8절
  `altLabel` 통합, 클래스와 개체 혼동은 4.2절 "후보는 개체", 미사용 import는
  모듈 의존 검사. 카탈로그는 이 검사들을 부르는 목록이다.
- **역관계 누락은 이 체계에서 결함이 아니다.** 8.2절이 링크를 한 방향만
  저장하고 역방향은 질의로 얻기로 정했다 — 카탈로그를 그대로 적용하지 않고
  체계의 결정에 맞춰 해석한다.
