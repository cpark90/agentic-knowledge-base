---
id: https://agentic-knowledge-base.dev/id/chunk/d03d5d30-7866-4aa8-b13d-de5f3967bd9f
type: decision
level: concrete
title_ko: 규범 문서 규약 — 지식 파일은 모듈 패키지의 filegroup으로 묶여 게이트 매크로의 입력이 된다
title: Normative-document conventions — Knowledge files enter the gates through a module package's filegroup and the gate macros
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-06T11:26:44+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-06T11:26:48+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/5adbc91e-1e33-46f6-bf34-c2d5f037c068
---
**규약** — `pe-knowledge-files-are-gate-inputs`의 결론을 규범 문서에 싣는 문장이다.

규약: [지킴] 지식 파일은 반드시 어떤 `filegroup`에 속하고, 그 filegroup은 어떤 게이트 테스트의 입력이다. 어느 게이트도 검사하지 않는 지식 파일이 이 하네스의 orphan이다.
규약: [지킴] 게이트는 `defs/knowledge.bzl`의 매크로로만 선언한다. `py_test`를 직접 쓰지 않는다.
규약: [지킴] 모듈 디렉토리가 Bazel 패키지다. 패키지의 `filegroup` 이름은 디렉토리 이름과 같게 한다.
규약: [권장] `glob`은 패키지 안 한 디렉토리 깊이만 대상으로 한다.
규약: 채널 파일은 그래프 밖이고 지식 파일의 게이트 입력 규약에서 제외되는 유일한 문서군이다. 어휘·shape 검사 대상이 아니고, 그 형식은 게이트 `channel`이 따로 강제한다.
