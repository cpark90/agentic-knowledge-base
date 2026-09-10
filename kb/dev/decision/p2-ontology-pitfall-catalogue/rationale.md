---
id: https://agentic-knowledge-base.dev/id/chunk/92f3ee19-8cd7-4659-a695-3e1a382d651a
type: decision
level: logical
title_ko: 3계층이 잡는 것과 설계 결함은 다르다
title: Design defects are not what the three tiers catch
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/e2647f3b-9122-4cad-93ea-8f5bd85b2a51
---
**근거** (노트 2.10절) — 3계층은 커밋마다 도는 형식 검사다. 다의어·과설계·고립 개념 같은 설계 결함은 어느 커밋 하나가 만든 것이 아니라 시간이 지나며 쌓인 것이므로, 주기 평가가 따로 필요하다.

카탈로그를 쓰는 이유는 결함 목록을 매번 다시 발명하지 않기 위해서다. 각 결함에 검출 수단이 붙어 있어야 평가가 의견이 아니라 질의가 된다 — 검출 수단이 없는 결함 항목은 카탈로그에 넣지 않는다.

역관계 누락을 결함 목록에서 빼는 것은 명시적 판정이다. 양방향 저장은 두 트리플의 일관성을 유지할 책임을 낳고, 질의로 얻으면 그 책임이 없다.
