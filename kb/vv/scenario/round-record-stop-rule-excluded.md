---
id: https://agentic-knowledge-base.dev/id/chunk/ec96760a-2ac4-5171-b341-e40143ce058a
type: decision
level: logical
title_ko: 논리 시나리오 배제 자극 — 신규 결함이 줄지 않은 두 라운드 뒤 셋째 라운드 기록의 정지 규칙 판정에서 다루지 않는 것
title: Logical scenario excluded stimuli — what judging the stop rule on a third round record after two rounds whose new defects did not fall does not cover
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-04T23:16:12+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/90e4464e-15dc-5cdc-9105-ba97d62261a8
---
**배제 자극** — 다루지 않는 자극은 둘이다.

- 저장소의 실제 라운드 기록은 다루지 않는다. 기록을 쓰는 `vv_run --round` 는 저장소에 파일을 남기므로 케이스의 명령이 될 수 없다.
- 판정 결과 주석(`process:judge`)의 제외는 다루지 않는다. 자극의 주석은 전부 리뷰 결함이다.
