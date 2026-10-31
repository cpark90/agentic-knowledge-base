---
id: https://agentic-knowledge-base.dev/id/chunk/d4612105-5fef-4f38-bc63-1ba04d56d94e
type: decision
level: concrete
title_ko: 검증 선행이 빌드를 정직하게 하고 바이트 동일성은 순서와 출처의 고정에서 나온다
title: Validating first keeps the build honest, and byte identity comes from fixing order and provenance
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}, {resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}, {resource: git:aeb0a58:chunks/decision/d-0162-deterministic-build-projection.md}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:45:53+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:45:53+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/00a6593d-57a6-445d-8e50-3dbb23b9df1b
---
**근거** — 출처는 harness-functional `docs/materialize-design.md`의 검증 게이트 절과 EMIT 절이다.

- 검증 선행이 빌드를 정직하게 만든다. 산출물은 연결되고 타입이 정합하며 능력이 충족된 그래프에서만 나온다. 부분 카탈로그로 union을 불완전하게 만들면 빌드가 거부되고 출력 디렉토리조차 생기지 않는 것을 확인했다. 반쪽 산출물이 없으므로 빌드가 됐다는 사실이 곧 검증됐다는 뜻이다.
- 바이트 동일성을 위해 **고정해야 하는 것**이 있다. 섹션 순서를 명세로 고정하고, 한 섹션 안의 여러 항목은 IRI로 정렬하며, 타임스탬프를 산출물에 넣지 않는다. 출처는 시각이 아니라 **값**으로 남기며, 무엇에서 파생됐고 어떤 부품이 묶였는지와 요구와 제공의 짝이 어떻게 맞았는지를 적는다.
- 해석되지 않은 참조는 **조용히 빠뜨리지 않는다**. 자리표시 스텁(stub)을 내고 항목마다 상태를 빌드 기록에 남기므로, 빌드는 언제나 나오되 결손이 보인다. 그래서 오프라인이나 부분 체크아웃이 실패가 아니라 표시된 결손이 된다.
- 읽기 뷰와 빌드 뷰는 같은 union의 **반대 방향 뷰**다. 읽기는 컨텍스트 상한으로 rot를 막고, 빌드는 검증 선행으로 고아와 drift를 막는다. 저장 그래프는 어느 쪽으로도 통째로 나가지 않는다(`p1-store-formal-read-narrow`).

이 저장소에서 문서를 생성하는 결정(`p12-documents-are-generated`)은 사본이 원본으로 오인되지 않도록 생성 시각을 적게 한다. 반면 재현 가능한 빌드는 시각을 빼고, 대신 무엇으로 만들었는지를 값으로 남겨 같은 목적을 달성한다.
