---
id: https://agentic-knowledge-base.dev/id/chunk/d466db7b-bff0-428c-9bbf-4dc8c618e67d
type: decision
level: logical
title_ko: 붕괴한 링크는 없는 링크보다 해롭다
title: A decayed link is worse than no link
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/c88e9891-e992-4e33-a891-0dcba05746b3
---
**근거** (노트 10.6절) — **링크는 만드는 것보다 유지하는 것이 어렵다.** 유지된 링크를 가진 개발자는 유지 작업을 더 빠르고 정확하게 수행하지만, 오래된 링크는 시스템의 실제 구조를 **오도한다.** 그래서 붕괴를 숨기지 않고 상태로 드러낸다.

여기서 6.5절 무효화와 만난다 — 가정 위반은 `assumes` 링크를 통해 항목을 무효화하고, 산출물 변경은 그 항목의 다른 링크를 `suspect`로 만든다. 두 메커니즘이 같은 링크 모델 위에서 동작한다.

전파의 성립 조건 셋 — 링크가 존재할 것, 보정이 plane 경계를 넘을 것, 전파가 멈출 것(5.2절 단방향 규칙).
