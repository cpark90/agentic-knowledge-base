---
id: https://agentic-knowledge-base.dev/id/chunk/f860a9f0-61ec-4291-806a-383773a42204
type: decision
level: logical
title_ko: level을 상황의 추상화 높이로 두는 정의를 버린다
title: Rejecting level as abstraction height of a situation
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/5ef6f4a9-343a-4f00-8e88-172521022d6b
---
**대안** — level을 "개념에서 동작하는 형태까지의 추상화 높이"로 정의하고 모든 plane이 같은 다섯 단계를 갖게 하는 v1 정의(옛 d-0005).

배제 이유 — 그 정의에서는 `requirement` plane이 따로 없어 functional이 `decision`에 얹히고, 산출물의 executable과 결정의 executable이 같은 뜻이 되어 사다리가 **무엇에서 무엇으로 가는 사슬인지** 말하지 못한다. 정제 높이로 정의하면 양 끝이 plane 전용이 되고, 격자가 성기다는 결과(6.4절)와 검증 KB가 executable을 나눠 갖는다는 결과(7.2절)가 따라 나온다.
