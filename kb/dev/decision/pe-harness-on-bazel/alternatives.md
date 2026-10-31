---
id: https://agentic-knowledge-base.dev/id/chunk/769522bb-af31-4b5a-a1e6-fd01b6025a7d
type: decision
level: concrete
title_ko: Makefile과 스크립트 직접 실행은 택하지 않는다
title: Makefile and direct script execution are not taken
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}, {resource: git:aeb0a58:chunks/decision/d-0001-bazel-harness.md}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T03:59:32+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T03:59:32+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/da7b19bc-5643-490f-9a51-3c45c7d06273
---
**대안** — 둘을 택하지 않는다.

| 대안 | 택하지 않는 이유 |
|---|---|
| Makefile(참조 저장소의 방식) | 단순하지만 캐시와 의존 그래프가 없어 전수 재검사가 기본이 된다 |
| 스크립트 직접 실행 | 게이트를 우회하기 쉬워 6.7절의 강제력이 사라진다 |
