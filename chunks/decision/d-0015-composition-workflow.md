---
iri: https://agentic-knowledge-base.dev/id/chunk-d0015
plane: decision
level: concrete
label_ko: 조립 워크플로 — 투영에서 검증까지
label_en: Composition workflow from pack to validation
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-harness-ontology]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — 새 구성물(하네스)의 조립은 고정된 절차를 따른다: ① 요청으로
컨텍스트 팩을 투영받고 ② 최상위 후보를 템플릿으로 삼아 ③ 요구
capability마다 제공 컴포넌트를 바인딩해 결핍을 메우고 ④ 조립한 뒤
⑤ 출처(derivedFrom)·성숙도(draft)와 함께 그래프에 기록하고 ⑥ 검증
게이트를 다시 돌린다. 새 노드도 같은 반-고아·반-drift 불변식에 잡히므로
그래프는 부패하는 대신 복리로 쌓인다.

**근거** (harness-concrete CLAUDE.md의 조립 워크플로 + harness-functional 구 docs/DESIGN.md)
- 컨텍스트 팩이 조립에 필요한 입력 전부가 되도록 설계되어 있다 — 팩의
  capability gaps 목록이 메워야 할 것을 명시한다.
- 템플릿 출처를 남기는 것이 손실 내성의 온톨로지판이다 (어디서 왔는지
  복원 가능).

**coverage-audit 게이트** — 검증 통과가 곧 반영 완료가 아니다. 소스의
구조 요소를 하나도 빠짐없이 열거해 각각을 표현에 매핑하는 감사가
통과해야 done이다: 모든 요소는 표현으로 매핑되거나 모델 밖에 두는
명시적·수용 가능한 사유를 가져야 하고, 담을 어휘 범주 자체가 없으면
조용히 건너뛰지 말고 스키마 확장을 먼저 트리거한다. (그래프 정합성
게이트는 source-fidelity를 보지 않는다 — 이 감사가 그 축이다.)
