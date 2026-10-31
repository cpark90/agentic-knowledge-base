---
id: https://agentic-knowledge-base.dev/id/chunk/267316e8-efa5-48d5-be40-69ec0182ec9a
type: decision
level: concrete
title_ko: 손으로 복제한 목록이 실제로 드리프트해 게이트가 줄어든 입력을 통과시켰다
title: Hand-copied lists did drift, and the gate passed a silently shrunken input
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-ontology}, {resource: git:aeb0a58:chunks/decision/d-0159-generated-index-drift-guard.md}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:37:33+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T04:37:33+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/6348f062-c916-4bb7-9e3c-14fc848c8b54
---
**근거** — 출처는 harness-functional `docs/federation-design.md`의 카탈로그 생성 절이다.

- 손으로 세 곳에 목록을 복제하던 시절 실제로 드리프트가 났다. 카탈로그에서 한 유닛이 빠져 **union이 부분만 로드된 채 검증이 통과**했다. 게이트는 초록인데 검사 대상이 조용히 줄어 있었으므로 이것은 실패 가운데 가장 나쁜 종류다. 그래서 게이트를 믿으려면 게이트의 입력 범위가 먼저 보증돼야 한다.
- 생성기는 중복 자체를 없애고, 검사 모드는 생성물이 실물과 일치하는가를 게이트 조건으로 만든다. 따라서 정합성을 사람의 주의력에 맡기지 않는다.
- 항목 값을 경로에서 추측하면 파일 이동이 곧 의미 변경이 된다. 반면 실물의 선언을 읽으면 디렉토리 배치는 사람이 읽는 조직화로만 남고 도구에는 투명해진다.

이 결정은 세 실패 모드(`p6-three-failure-mode-defences`) 가운데 drift의 **생성물판**이다. 어휘의 drift는 통제 어휘가 막고, 생성물의 drift는 생성기와 대조 게이트가 막는다.
