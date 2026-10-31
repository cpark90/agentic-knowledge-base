---
id: https://agentic-knowledge-base.dev/id/chunk/5c3a7f0a-bb54-4b9c-8bcd-626ab770e047
type: decision
level: concrete
title_ko: 목록은 손으로 복제하지 않고 생성하고 대조한다
title: Lists are generated and checked, never copied by hand
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}, {resource: git:aeb0a58:chunks/decision/d-0159-generated-index-drift-guard.md, id: https://agentic-knowledge-base.dev/id/chunk-d0159, title_ko: "목록은 손으로 복제하지 않고 생성하고 대조한다", title: "Generate indexes from disk and diff them in CI"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/973f5595-b22c-48d1-ad19-976a0408497b]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0159]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/6348f062-c916-4bb7-9e3c-14fc848c8b54
composite: {id: https://agentic-knowledge-base.dev/id/composite/6348f062-c916-4bb7-9e3c-14fc848c8b54, title_ko: 생성하고 대조하는 목록, title: Lists generated and checked for drift}
---
**결론** — 같은 목록(색인, 카탈로그, 매니페스트)이 두 곳 이상에 필요하면 손으로 복제하지 않고 **디스크의 실물에서 결정론적으로 생성**한다. CI는 생성기를 검사 모드로 돌려 커밋된 산출물과 어긋나면 실패시킨다. 각 항목의 값은 실물 파일이 스스로 선언한 것을 읽고 **경로에서 추측하지 않는다**.
