---
id: https://agentic-knowledge-base.dev/id/chunk/4807a67c-1e98-40b3-b10d-937b9de41cfc
type: decision
level: logical
title_ko: 규칙 이름이 근거이므로 생성은 결정론적이어야 한다
title: Because the rule name is the ground, generation must be deterministic
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: hci/claude-opus-5, at: 2026-09-10T20:00:00+09:00}
verified: [{by: orchestrator/claude-fable-5, at: 2026-09-11T18:20:00+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/b70975e0-3013-4480-8885-6b0ea69cf97b
---
**근거** (노트 8.23절, 8.7절, 8.12절) — 케이스의 "왜 이 값인가"가 규칙 이름이어야 concrete 게이트의 표본 근거(6.8절)를 통과하고, 경계값이 별도 집계되어야 등가분할만으로 커버가 높아 보이는 착시를 막는다(8.7절). 규칙 + seed가 provenance에 남으면 같은 리비전에서 같은 케이스가 재생성되어 재현성(8.12절)이 환경이 아니라 생성 단계에서부터 확보된다.
