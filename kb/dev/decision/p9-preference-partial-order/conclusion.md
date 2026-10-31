---
id: https://agentic-knowledge-base.dev/id/chunk/c6c78803-bdb6-4ca2-9b07-bba7878f3a01
type: decision
level: concrete
title_ko: 선호는 후보를 기각하지 않고 순서만 정한다
title: Preferences order candidates; they never reject them
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}, {resource: git:aeb0a58:chunks/decision/d-0104-preference-partial-order.md, id: https://agentic-knowledge-base.dev/id/chunk-d0104, title_ko: "선호는 후보를 기각하지 않고 순서만 정한다", title: "Preferences order candidates without rejecting them"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-10-24T18:07:48+09:00}
verified: [{by: process:label-judge-20260911, at: 2026-09-11T18:50:00+09:00}, {by: human:cpark, at: 2026-09-11T18:50:00+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/f715c53f-c9bd-49cc-b580-6e2d2343cd5c]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0104]
part_of: https://agentic-knowledge-base.dev/id/composite/d019ef5c-899b-459f-98cb-80d0fd72a0c4
composite: {id: https://agentic-knowledge-base.dev/id/composite/d019ef5c-899b-459f-98cb-80d0fd72a0c4, title_ko: 선호는 후보를 기각하지 않고 순서만 정한다, title: Preferences order candidates; they never reject them}
---
**결론** — 선호는 부분순서로 적고, 설계 공간 파일의 `preferences` 블록에 이유와 함께 둔다. 순서의 원본은 부분순서이고 믿음 정도는 동률만 깬다.

```
space :auth-space
  candidates ... (8.4절과 동일)
  preferences
    :oauth2 > :mtls        reason: "운영 경험 있음"
    -- :apikey는 순서 없음 (이미 기각)
```

**선호는 후보를 기각하지 않는다.** 선호는 후보가 여럿 남았을 때 유저에게 보여 주는 순서만 정하고, 기각은 제약만이 한다. 부분순서에서 순서가 없는 두 후보는 다음 두 단으로 동률을 깬다.

1. 믿음 정도가 높은 후보를 앞에 둔다. 믿음 정도는 증거 기록에서 계산한 값이다(`p9-evidence-ledger-with-belief`).
1. 믿음 정도가 같거나 어느 한쪽에 없으면 언어모델의 제안이 동률을 깬다(`p9-language-model-place`).

믿음 정도는 이 동률 깨기에만 들고, 기각과 확정, 상태 전이에는 들지 않는다(유저 결정 Q-0055 Q109-b, 2026-10-24).
