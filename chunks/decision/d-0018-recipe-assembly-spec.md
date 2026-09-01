---
iri: https://agentic-knowledge-base.dev/id/chunk-d0018
plane: decision
level: concrete
label_ko: 레시피는 중립 부품의 조립 명세다
label_en: A recipe is an assembly spec over neutral parts
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-harness-recipes]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — 중앙 라이브러리와 레시피의 역할을 나눈다. 중앙은 일반화된
도메인 독립 부품(guardrail·pattern·workflow·prompt·tool·capability·
concept)만 담는 **중립 부품 라이브러리**로 두고, "부품이 어떻게 조합되어
쓰이는가"는 레시피가 담는다. 레시피는 중앙 부품을 IRI로 참조해 완성물
하나를 조립하는 **조립 명세**이며, 자기 전문화에 필요한 도메인 특수
바인딩만 로컬로 선언한다.

**근거** (harness-recipes README)
- 중앙 라이브러리는 의도적으로 중립을 유지한다 — 특정 하네스 하나를
  기술하는 순간 중립성이 깨지고 재사용이 막힌다.
- 중앙은 도메인을 결코 알지 못한다: 모든 도메인 노드는 레시피 쪽에
  산다. 도메인 지식의 유입 방향이 한쪽이므로 중앙의 어휘가 오염되지
  않는다.
- 부품 결합은 복사가 아니라 IRI 참조다 — 중앙 부품이 개선되면 모든
  레시피가 그 개선을 받는다.

**이 저장소와의 관계** — 온톨로지 코어+확장 원칙(노트 2.3절: 최상위는
import만, 확장은 새 모듈 추가로만)의 A-Box판이다. 도메인 프로파일
(2.11절)이 골격과 분리되는 것과 같은 구도다.
