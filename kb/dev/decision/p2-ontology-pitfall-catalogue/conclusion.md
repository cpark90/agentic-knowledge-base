---
id: https://agentic-knowledge-base.dev/id/chunk/37e80683-8360-469c-9d06-79e62b8071cc
type: decision
level: concrete
title_ko: 설계 결함은 카탈로그로 주기 평가한다
title: Design defects are assessed periodically against a catalogue
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/27699a04-a588-4c4b-89c6-b7be0c173ced]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0055]
part_of: https://agentic-knowledge-base.dev/id/composite/e2647f3b-9122-4cad-93ea-8f5bd85b2a51
composite: {id: https://agentic-knowledge-base.dev/id/composite/e2647f3b-9122-4cad-93ea-8f5bd85b2a51, title_ko: 온톨로지 결함 카탈로그, title: Ontology pitfall catalogue}
---
**결론** — 2.5절 3계층 검사 외에 **주기적으로 설계 결함을 검사한다.** 온톨로지 결함 카탈로그(pitfall catalogue)를 쓰며, 결함마다 검출 수단을 지정한다.

- 정의 없는 개념 · 동의어를 별개 클래스로 → 위생 검사, 0.8절 `altLabel` 통합
- 잘못된 계층 · 순환 계층 → 상위 온톨로지 준수 검사, 추론기
- 관계 방향 혼동 · 정의역·치역 미지정 → 정의역·치역 검사, TIM 검사
- 다의어 개념 → 경쟁 질문에서 모순 답 · 과설계 → 2.7절 대조
- 고립 개념 · 미사용 import → 그래프 질의, 모듈 의존 검사
- 클래스와 개체 혼동 → 4.2절. 후보는 개체다

**역관계 누락은 결함이 아니다.** 한 방향으로만 저장하고 역방향은 질의로 얻는 것이 정책이다 (9.2절).
