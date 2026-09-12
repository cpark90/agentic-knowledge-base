---
id: https://agentic-knowledge-base.dev/id/chunk/c6c78803-bdb6-4ca2-9b07-bba7878f3a01
type: decision
level: concrete
title_ko: 선호는 후보를 기각하지 않고 순서만 정한다
title: Preferences order candidates; they never reject them
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
verified: [{by: process:label-judge-20260911, at: 2026-09-11T18:50:00+09:00}, {by: human:cpark, at: 2026-09-11T18:50:00+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/f715c53f-c9bd-49cc-b580-6e2d2343cd5c]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0104]
part_of: https://agentic-knowledge-base.dev/id/composite/d019ef5c-899b-459f-98cb-80d0fd72a0c4
composite: {id: https://agentic-knowledge-base.dev/id/composite/d019ef5c-899b-459f-98cb-80d0fd72a0c4, title_ko: 선호는 후보를 기각하지 않고 순서만 정한다, title: Preferences order candidates; they never reject them}
---
**결론** — 선호는 **수치 없이 부분순서로만** 적는다. 설계 공간 파일의 `preferences` 블록에 이유와 함께 둔다.

```
space :auth-space
  candidates ... (8.4절과 동일)
  preferences
    :oauth2 > :mtls        reason: "운영 경험 있음"
    -- :apikey는 순서 없음 (이미 기각)
```

**선호는 후보를 기각하지 않는다.** 후보가 여럿 남았을 때 유저에게 보여 주는 순서만 정한다. 기각은 제약만이 한다.
