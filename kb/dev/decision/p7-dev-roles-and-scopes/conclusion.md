---
id: https://agentic-knowledge-base.dev/id/chunk/f1d4cbae-2b57-4b96-826f-536b132cd624
type: decision
level: concrete
title_ko: 개발 KB의 쓰기 권한은 네 역할에 나뉘고 developer는 확정된 것만 본다
title: Write access to the development KB is split across four roles; developers see only what is fixed
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: hci/claude-opus-5, at: 2026-09-10T20:00:00+09:00}
verified: [{by: orchestrator/claude-fable-5, at: 2026-09-11T18:20:00+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/f29f5a66-774b-48b3-bda1-fc2529e611af, https://agentic-knowledge-base.dev/id/chunk/42fde00d-395f-4193-9eef-5c86f0d4abc7]
composite: {id: https://agentic-knowledge-base.dev/id/composite/92f76b7c-3bd8-4e3c-a014-61c6aec60af4, title_ko: 개발 역할과 스코프, title: Development roles and scopes}
part_of: https://agentic-knowledge-base.dev/id/composite/92f76b7c-3bd8-4e3c-a014-61c6aec60af4
---
**결론** — 개발 KB에 쓰기 권한을 갖는 역할과 범위. 11.2절 카탈로그를 개발 KB 관점에서 (노트 7.7절).

| 역할 | 쓰기 | 읽기 | conditional |
|---|---|---|---|
| design | `requirement`(유저와 공동), `decision`, `contract`, `schema`, ODD, T-Box 제안 | 전부 | — |
| developer | `artifact` | `decision` concrete, `contract`, `schema` | 결정이 concrete일 때만 `artifact` 쓰기 |
| orchestrator | `decision` (dispatch 결정) | 전부 | — |
| V&V | 없음 (`annotation`만) | 전부 | — |

design 역할이 `-space`를 만들고, 유저가 체크박스 파일(13.5절)로 확정하며, developer는 확정된 것만 본다.
