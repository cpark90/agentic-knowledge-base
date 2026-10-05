---
id: https://agentic-knowledge-base.dev/id/chunk/5e266d09-8bfc-4a5c-a079-8b2d632ac257
type: decision
level: logical
title_ko: head는 frontmatter가 원본이라 생성하고 손 TTL의 경계는 초판부터 청크가 아닌 개체였다
title: The head is generated because the frontmatter is its source, and the hand-written TTL boundary has been non-chunk entities since the first edition
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T14:10:00+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/3b6eaa94-2497-48bd-96c7-2b84963394d7
---
**근거** — 한 청크는 한 파일이고 frontmatter가 head다(`pe-three-layer-binding`의 OKF 필드 사상). `base-kg.ttl` 배너가 이 이유로 head를 손으로 쓰지 않는다고 적는다. 노트 4.9절은 head·provenance·pubinfo가 `-kg`에 있어 청크 메타데이터 질의에 본문을 열 필요가 없다고 적는다. 그 `-kg`가 생성물 `chunks-kg.ttl`이다.

손 TTL의 경계는 초판(2026-09-01)부터 "청크가 아닌 개체"였다. 초판 목록은 가정·출처 문서·역할·스코프·하네스였고 복합체·채널은 뒤에 더해졌다.

복합체의 손 자리는 지금 비어 있다. 손으로 쓴 복합체 41건은 2026-09-29에 생성 경로(`kb_decision`·`kb_composite`)로 옮겨졌다(유저 답 "도구를 고친다"). 파일은 union 그래프의 입력으로 남고, 생성 경로가 표현하지 못하는 복합체가 다시 생기면 그 이유와 함께 쓴다(`composite-kg.ttl` 배너).

`catalog-kg.ttl` 배너는 `AGENTS.md`의 역할 표와 그래프가 일치해야 한다고 적는다. 문서가 산문이고 그래프가 형식이다.

개체 라벨 한/영의 초판 근거는 "라벨 목록 읽기가 기본 접근이다"(노트 4.4절)다. 라벨 수를 보는 shape는 청크(`chunk-shapes.ttl`)와 게이트(`gate-shapes.ttl`)의 것뿐이다. 가정·출처 문서·역할·스코프의 라벨과 모든 배너는 검사 없는 규약이다.

미확정: 배너 규약의 이유는 초판 문구 밖의 기록에서 확인하지 못했다.
