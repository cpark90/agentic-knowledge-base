---
id: https://agentic-knowledge-base.dev/id/chunk/371c29fe-df8e-4b81-b5c4-937b6e00eab5
type: decision
level: logical
title_ko: 푸는 문제는 의도와 산출물의 단절 하나다
title: The single problem is the intent-artifact break
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T21:30:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/4a312eca-5b3b-40e5-9f0a-c141039ac7c1
---
**근거** (노트 산출물 정의) — 이 체계가 푸는 문제는 하나다: **추상적인 의도와 실제
산출물이 끊어져 있다.** 의도는 문서에, 결정의 근거는 사람 머릿속에, 실제 결과는
산출물에 흩어져 있고, 그 사이를 잇는 것은 사람의 기억뿐이다. 에이전트는 그 기억을
갖지 못한다.

구성요소가 여덟이 아니라 "두 기반 + 다섯 메커니즘 + 두 KB"로 층이 갈리는 이유:
판정 방식·판정 도구·조건 어휘는 작업 종류마다 다르므로 골격과 프로파일을 나누고,
어휘(온톨로지)와 그 어휘로 쓴 첫 문서(ODD)는 메커니즘의 전제이므로 기반이라
부른다. 메커니즘을 하나라도 빼면 단절 중 하나가 복구되지 않는다 — 한 줄 요약이
그 연결을 고정한다: 공통 어휘로 운영 조건을 명세하고, 42줄 청크를 plane×수준
거주표로 배치하며, 각 항목의 가정 조건을 명시하고, 조건이 깨지면 의존 항목이
자동으로 무효화된다.
