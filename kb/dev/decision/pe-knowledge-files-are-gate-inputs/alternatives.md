---
id: https://agentic-knowledge-base.dev/id/chunk/56a57985-0b14-42a7-a26d-bac8490da282
type: decision
level: logical
title_ko: 지식 파일을 Bazel에 들이는 다른 방식은 비교된 기록이 없다
title: No other way of bringing knowledge files into Bazel was recorded as compared
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:13:20+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/5adbc91e-1e33-46f6-bf34-c2d5f037c068
---
**대안 없음** — 네 규약은 2026-09-01 초기 구축의 `STYLEGUIDE.md`에 처음부터 함께 적혔고, 그때 비교한 안의 기록이 없다. 노트 부록 E가 Bazel을 의존 그래프·검사·뷰의 바인딩으로 고정했으므로 지식 파일을 Bazel 밖에서 검사하는 안은 다루지 않았다.

2026-10-03까지 있던 이탈 셋(직접 쓴 `py_test`, 이름이 `bodies`인 filegroup, 결정 패키지의 깊은 glob)은 대안으로 채택된 것이 아니었다. 유저 답 Q5-a가 그 셋을 규약에 맞추기로 정했고 같은 날 시행됐다.
