---
id: https://agentic-knowledge-base.dev/id/chunk-d0158
type: decision
level: concrete
title_ko: 개체 이름공간을 소유자 세그먼트로 나눈다
title: Partition the entity namespace by owner segment
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-02T03:51:12+09:00}
---
**결론** — 독립 저장소가 각자 개체를 민팅하는 연합에서는 개체 IRI에 **소유자
세그먼트**를 넣어 `…/id/<owner>/<slug>` 꼴로 민팅한다. 공용 중립 부품용
세그먼트 하나를 예약하고, 저장 형식에서는 prefix 바인딩으로만 표현해 노드
본문의 이름은 slug 그대로 둔다.

**근거** (harness-functional docs/federation-design.md D3)
- 세그먼트가 없으면 두 기여자가 우연히 같은 이름을 쓴 순간 union에서 **같은
  IRI로 병합**되어 서로 다른 두 개체가 조용히 뒤섞인다. 세그먼트가 곧 소유권
  경계이며, 이름 충돌을 사회적 합의가 아니라 구조로 막는다.
- 본문을 prefix로만 다루면 소유자가 바뀌어도 노드 블록은 그대로다. 다른
  소유자의 노드를 참조할 땐 그 소유자용 prefix를 하나 더 선언하며, 두 prefix가
  같은 네임스페이스를 가리키므로 union에서 같은 IRI로 해석돼 **저장소를
  가로지르는 간선이 실제로 성립**한다.
- **개체 IRI와 그 개체를 담는 문서 IRI는 다르다.** import·카탈로그가 다루는
  것은 문서 IRI다. 둘을 섞으면 파일을 쪼개는 순간 개체 IRI가 따라 바뀐다.
  실제로 공용 부품을 타입별 문서로 분할할 때 문서 IRI만 늘고 개체 IRI는
  그대로였다 — 이것이 분할을 값싸게 만든다.

**이 저장소와의 관계** — IRI 설계(d-0032)가 정한 지속성 축과 직교하는 축이다.
d-0032는 한 저장소 안에서 이름이 바뀌어도 정체성이 유지되게 하고, 이 규칙은
여러 저장소가 서로의 이름을 침범하지 않게 한다.
