---
id: https://agentic-knowledge-base.dev/id/chunk-d0157
type: decision
level: concrete
title_ko: 불변식은 union 위에서만 성립하므로 union을 검증한다
title: Invariants hold only over the union, so validate the union
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-harness-ontology]
generated: {by: claude/fable-5, at: 2026-09-02T03:51:12+09:00}
---
**결론** — 반-고아·반-drift·조립가능 같은 보장은 **합쳐 추론한 그래프**에서만
판정되므로, 검증은 언제나 조립된 union을 대상으로 하고 파일 하나를 홀로
검증하지 않는다. 게이트는 두 단 — 기여자 로컬과 데이터 저장소 CI — 이며 둘 다
같은 union을 본다.

**근거** (harness-functional docs/federation-design.md D4)
- 저장소를 가로지르는 간선(A의 개체가 B의 개체를 참조)은 양쪽이 union에
  들어와야 도달성·타입 검사가 성립한다. 그래서 조립(d-0156)과 검증은 한 설계의
  양면이다 — 조립 방식이 "검증할 union이 하나 있다"를 보존해야 한다.
- **좁은 게이트가 초록인 것은 파급이 없다는 증거가 아니다.** 어휘만 있는
  저장소의 단독 게이트는 개체가 0이라 연결성 축이 공허하게 통과한다. 개체가
  있어야 걸리는 불변식은 개체가 사는 쪽의 union 게이트가 강제한다.
- 따라서 어휘가 바뀌면 데이터가 한 줄도 안 바뀌어도 데이터 쪽 **전량 재검증**이
  필요하다 — 이 파급을 ODD의 조건부 규정으로 명문화해 잊히지 않게 한다.
- 어휘는 fork하지 않는다. 데이터 저장소가 중앙 어휘에 **conform**하는 것이
  저장소를 가로지르는 anti-drift의 실체다 — 어휘를 복사하는 순간 사본마다
  뜻이 갈라지고 union은 같은 이름의 다른 개념을 담게 된다.

**이 저장소와의 관계** — 세 방어선(d-0014)의 적용 대상을 정한다: 방어선은
파일이 아니라 union에 건다.
