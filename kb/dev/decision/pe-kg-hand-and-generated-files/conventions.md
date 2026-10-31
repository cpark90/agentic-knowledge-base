---
id: https://agentic-knowledge-base.dev/id/chunk/91a7d914-16df-4747-83b8-e97be2d9fa3c
type: decision
level: concrete
title_ko: 규범 문서 규약 — 단위 지식 head는 생성하고 손으로 쓰는 지식그래프 TTL 셋은 지식이 아닌 개체만 한/영 라벨과 배너를 갖춰 담는다
title: Normative-document conventions — Chunk heads are generated, and the three hand-written knowledge graph TTL files hold only non-chunk entities, with ko/en labels and a banner
former_title_ko: ["규범 문서 규약 — 지식 항목 head는 생성하고 손으로 쓰는 지식그래프 TTL 셋은 지식 항목이 아닌 개체만 한/영 라벨과 배너를 갖춰 담는다"]
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T01:24:40+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/3b6eaa94-2497-48bd-96c7-2b84963394d7
---
**규약** — `pe-kg-hand-and-generated-files`의 결론을 규범 문서에 싣는 문장이다.

규약: [지킴] head는 생성 산출물이므로 손으로 쓰지 않는다. 여기 두는 것은 가정과 출처 문서, 복합체, 역할, 적용 범위, 채널, 하네스다.
규약: [지킴] 라벨 목록 읽기가 기본 접근이므로 개체에도 한글과 영어 라벨을 단다.
규약: [지킴] 파일 상단 배너에 담는 개체 종류와 "손으로 쓰지 않는 것"을 적는다.
규약: 지식 head | `bazel-bin/kg/chunks-kg.ttl` | **생성**
규약: 복합체 | `kg/composite-kg.ttl` | 손
규약: 가정·출처 문서 | `kg/base-kg.ttl` | 손
규약: 역할과 적용 범위, 채널, 하네스 (입력) | `kg/catalog-kg.ttl` | 손
규약: **생성 산출물을 손으로 고치지 않는다.** head 그래프인 `//kg:chunks_kg`는 frontmatter에서 생성되므로 고칠 것은 원본 파일이다.
