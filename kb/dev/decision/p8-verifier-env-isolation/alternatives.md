---
id: https://agentic-knowledge-base.dev/id/chunk/b4f447d2-da8a-4f8c-84df-57e6ad692c77
type: decision
level: logical
title_ko: 환경을 그대로 두거나 케이스가 선언하거나 실행 경로를 하나로 막는 안은 기각된다
title: Leaving the environment intact, declaring it per case, and allowing one entry point only are rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5, at: 2026-09-23T12:00:00+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/2a051063-7217-4597-b03f-4a4346e85b0e
---
**대안** — 넷을 기각한다.

| 대안 | 기각 이유 |
|---|---|
| 환경을 그대로 두고 실행기를 한 방식으로만 부르게 한다 | 규약이 코드 밖에 있어 지켜지는지 검사할 수 없다. 실측에서 이미 두 방식이 다른 답을 냈다 |
| 케이스가 필요한 환경을 선언한다 | 케이스마다 환경이 달라져 재현의 단위가 흩어진다. 자극은 케이스의 것이고 환경은 실행기의 것이다 |
| `bazel run` 형태를 허용 목록에 남기고 상대 경로를 쓴 명령만 거부한다 | 상대 경로는 `$(ls …)`와 glob으로 **실행 시점에** 생기므로 실행 전에 판별할 수 없다. 실행 뒤에는 이미 거짓 통과가 난 뒤다 |
| 걷어내는 변수를 `PYTHONSAFEPATH` 하나로 좁힌다 | `PYTHONPATH`가 남으면 검증기가 runfiles 사본의 모듈을 읽어 검사 대상이 소스 트리가 아니게 된다. 환경 문제가 아니라 판정의 오류다 |
