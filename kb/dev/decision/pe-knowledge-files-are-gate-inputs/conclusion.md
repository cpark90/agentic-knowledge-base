---
id: https://agentic-knowledge-base.dev/id/chunk/6c577bf6-3cc0-4d1d-9cae-2d0260349c7a
type: decision
level: concrete
title_ko: 지식 파일은 모듈 패키지의 filegroup으로 묶여 게이트 매크로의 입력이 된다
title: Knowledge files enter the gates through a module package's filegroup and the gate macros
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/f987e08c-fba7-43d8-9e0a-903edbd9375a]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T16:40:00+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/5adbc91e-1e33-46f6-bf34-c2d5f037c068
composite: {id: https://agentic-knowledge-base.dev/id/composite/5adbc91e-1e33-46f6-bf34-c2d5f037c068, title_ko: 지식 파일은 게이트 입력이다, title: Knowledge files are gate inputs}
---
**결론** — 지식 파일이 검사에 들어가는 길은 하나다. 규약은 넷이고 `STYLEGUIDE.md` §6이 2026-09-01 초기 구축부터 적었다.

| 규약 | 내용 | 등급 |
|---|---|---|
| 게이트 입력 | 지식 파일은 어떤 `filegroup`에 속하고, 그 filegroup은 어떤 게이트 테스트의 입력이다. 어느 게이트도 검사하지 않는 지식 파일이 이 하네스의 orphan이다 | 지킴 |
| 게이트 선언 | 게이트는 `defs/knowledge.bzl`의 매크로로만 선언한다. `py_test`를 직접 쓰지 않는다 | 지킴 |
| 패키지 | 모듈 디렉토리가 Bazel 패키지다. 패키지의 `filegroup` 이름은 디렉토리 이름과 같다 | 지킴 |
| glob | `glob`은 패키지 안 한 계층만 대상으로 한다. 깊은 glob이 필요하면 패키지를 나눈다 | 권장 |

소통 채널의 파일은 그래프 밖이고 이 규약에서 제외되는 유일한 문서군이다. 그 형식은 게이트 `channel`이 따로 강제한다.

`bazel test //...`가 게이트 전체 실행이므로, 이 규약이 지켜지면 지식 파일 하나하나가 재검증 시점에 적어도 한 게이트를 거친다.
