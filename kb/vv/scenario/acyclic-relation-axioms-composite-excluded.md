---
id: https://agentic-knowledge-base.dev/id/chunk/83be3942-7ea8-5794-9336-b2c110a39690
type: decision
level: logical
title_ko: 논리 시나리오 배제 자극 — 자기 참조 부분관계 하나를 더한 그래프의 검증에서 다루지 않는 것
title: Logical scenario excluded stimuli — what validating a graph with one self-referencing part relation added does not cover
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-04T21:22:42+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/8b1ba340-919d-55cc-b0f0-ab499caf96bc
---
**배제 자극** — 다루지 않는 자극은 둘이다.

- `refines` 비반사 공리의 위반은 시나리오 `acyclic-relation-axioms`가 덮는다.
- 길이 둘 이상의 부분관계 순환은 다루지 않는다. 질의는 순환의 길이를 가리지 않으므로 최소 자극인 자기 참조 하나로 그 분기를 연다.
