---
id: https://agentic-knowledge-base.dev/id/chunk/f1d4cbae-2b57-4b96-826f-536b132cd624
type: decision
level: concrete
title_ko: 개발 KB의 쓰기 권한은 네 역할에 나뉘고 developer는 확정된 것만 본다
title: Write access to the development KB is split across four roles; developers see only what is fixed
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: hci/claude-opus-5, at: 2026-09-24T12:00:00+09:00}
layer: methodology
verified: [{by: orchestrator/claude-opus-5, at: 2026-09-24T12:10:00+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/f29f5a66-774b-48b3-bda1-fc2529e611af, https://agentic-knowledge-base.dev/id/chunk/42fde00d-395f-4193-9eef-5c86f0d4abc7]
composite: {id: https://agentic-knowledge-base.dev/id/composite/92f76b7c-3bd8-4e3c-a014-61c6aec60af4, title_ko: 개발 역할과 스코프, title: Development roles and scopes}
part_of: https://agentic-knowledge-base.dev/id/composite/92f76b7c-3bd8-4e3c-a014-61c6aec60af4
---
**결론** — 개발 KB에 쓰기 권한을 갖는 역할과 범위. 11.2절 카탈로그를 개발 KB 관점에서 (노트 7.7절).

| 역할 | 쓰기 | 읽기 | conditional |
|---|---|---|---|
| orchestrator | `requirement`(유저 관심사의 EARS), `decision`, `memory` | 전부 | 해당 없음 |
| developer | `artifact` + T-Box·ODD(design 겸임 — 유저 결정 C4) | `contract`·`schema`·`decision` | 결정이 concrete일 때만 `artifact` 쓰기 |
| vnv | `kb/vv/`의 전 plane (`agt:writesIn`) | `requirement`·`artifact`·`decision` | `verifies`의 주어는 V&V 청크뿐 |
| hci | 소통 채널과 자기 역할 메모리 | 저장소 전체 | 유저 요청 시 git 관리 |

**형식 원본은 `kg/catalog-kg.ttl`이다.** 이 표는 그것을 개발 KB 관점에서 재진술한 것이므로 역할·권한을 바꾸면 두 곳을 같은 커밋에서 바꾼다.

`-space`를 여는 역할은 설계 변수를 지닌 항목의 write plane 역할이다. 확정은 유저가 체크박스 뷰(`//space:choices`)로 하고, developer는 확정된 것만 본다.
