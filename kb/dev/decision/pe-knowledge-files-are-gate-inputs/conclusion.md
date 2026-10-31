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
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T19:33:43+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-06T11:26:48+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T19:33:43+09:00}]
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
| glob | `glob`은 패키지 안 한 디렉토리 깊이만 대상으로 한다. 깊은 glob이 필요하면 패키지를 나눈다 | 권장 |

소통 채널의 파일은 그래프 밖이고 이 규약에서 제외되는 유일한 문서군이다. 그 형식은 게이트 `channel`이 따로 강제한다.

`bazel test //...`가 게이트 전체 실행이므로, 이 규약이 지켜지면 지식 파일 하나하나가 재검증 시점에 적어도 한 게이트를 거친다.

게이트 입력 규약은 게이트 `gate-input`(`gen_build --gate-inputs`, `//:gate_input_test`, 실행 계층 test, 노트 6.7절, 유저 답 Q80-a, 2026-10-15)이 강제한다. `kb/` 아래 지식 파일 가운데 소유 패키지(가장 가까운 BUILD의 디렉토리)의 BUILD가 이름으로도 glob으로도 담지 않은 파일이 FAIL이다. 이 모드는 생성·`--check` 모드와 따로 돌아, 음성 시험의 최소 트리처럼 BUILD 없는 입력으로 생성기를 부르는 자리를 막지 않는다. 찾는 것이 선언되지 않은 파일이므로 runfiles가 아니라 입력 `defs/kb.bzl`의 링크를 따라간 소스 트리를 걷고, 입력 해시로는 새 파일을 알 수 없어 캐시하지 않는다(`external`). 해소는 developer가 파일을 `gen_build`가 아는 패키지로 옮기거나 그 디렉토리를 생성기에 더하는 것이다.
