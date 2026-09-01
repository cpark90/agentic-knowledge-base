---
iri: https://agentic-knowledge-base.dev/id/chunk-d0066
plane: decision
level: concrete
label_ko: 하위 ODD는 상위를 좁히기만 하고 이탈 전파는 비대칭이다
label_en: A child ODD only narrows the parent; exit propagation is asymmetric
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — 하위 ODD는 상위 ODD를 `import`하고 속성 값 범위를 **좁히기만**
한다. 넓히거나 새 속성을 추가하면 검사 실패다. 이탈 전파는 비대칭이다 —
하위 ODD의 이탈은 하위 범위 안에서만 무효화를 전파하고, 상위 ODD의 이탈은
모든 하위로 전파된다.

**근거** (노트 3.11절)
- 3.1절 "하위 시스템 ODD는 상위의 부분집합"을 기계가 검사할 수 있는 형태로
  구체화한 것이다. `import` + 범위 좁히기만 허용하면 부분집합 관계가
  구문 수준에서 보장된다.
- 부분집합이 보장되어야 상위 ODD에서 파생한 스코프·가정·시나리오가 하위
  안에서도 그대로 유효하다.
- 전파의 비대칭은 부분집합 관계의 귀결이다. 상위 속성이 이탈하면 그 속성을
  좁혀 쓰던 하위 전부가 함께 이탈한 것이 된다.
