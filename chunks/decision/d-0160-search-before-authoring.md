---
iri: https://agentic-knowledge-base.dev/id/chunk-d0160
plane: decision
level: concrete
label_ko: 만들기 전에 검색한다 — 노드는 단일 책임
label_en: Search before authoring - one node, one responsibility
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-harness-ontology]
generated_at: 2026-09-02T00:00:00+09:00
---
**결론** — 한 노드는 한 가지만 담고(한 페르소나·한 정책·한 능력), 새 노드를
만들기 전에 **검색 도구로 같은 것이 이미 있는지 먼저 찾는다**. 없어서 만드는
것과 못 찾아서 만드는 것을 구분한다.

**근거** (harness-functional ONTOLOGYSTYLE §1)
- 여러 정책·페르소나를 한 노드에 섞으면 재사용·검색·예산 계산이 한꺼번에
  나빠진다 — 그 노드의 절반만 필요해도 통째로 실어야 하고, 검색은 두 주제가
  섞인 텍스트에 대해 어느 쪽으로도 정확히 맞지 않는다.
- **같은 뜻의 노드를 둘 만드는 것이 곧 drift다**(d-0014). 검색이 그 drift의
  1차 방어이며, 저작 도구가 검색을 저작 흐름의 **첫 단계**로 두어야 실제로
  지켜진다 — 규칙만 적어두면 새로 만드는 쪽이 언제나 더 빠르다.
- 서술 길이 상한(d-0016)을 넘는 노드는 대개 단일 책임 위반의 증상이다. 상한은
  이 규칙의 기계적 대리 지표이고, 초과의 처방은 자르기가 아니라 분해다.
- **영리한 모델링을 경계한다**: "스키마가 금지하지 않았다"는 "써도 된다"가
  아니다. 등록된 관용 패턴을 먼저 따르고, 벗어나야 한다면 그 노드나 커밋에
  사유를 한 문장 남긴다 — 말없이 머지하지 않는다.
