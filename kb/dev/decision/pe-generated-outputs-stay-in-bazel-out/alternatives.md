---
id: https://agentic-knowledge-base.dev/id/chunk/efee433a-d1c5-481f-9042-be422272dfd0
type: decision
level: logical
title_ko: 생성 BUILD와 skill을 커밋하지 않고 매번 생성하는 안은 기각된다
title: Not committing the generated BUILD files and skills, and generating them on every run, is rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T16:40:00+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/444519a5-c8d8-416b-88a5-b1bc2fd92ccc
---
**대안** — 하나를 기각한다.

| 대안 | 기각 이유 |
|---|---|
| 생성 BUILD와 skill도 `bazel-out`에만 두고 매번 생성한다 | BUILD는 Bazel이 로드 전에 읽어야 하므로 빌드의 출력이 될 수 없다. 커밋하지 않으면 링크 변화가 PR diff에 보이지 않고, skill은 도구를 돌리지 않는 세션에서 읽히지 않는다 |
