---
id: https://agentic-knowledge-base.dev/id/chunk-d0104
type: decision
level: concrete
title_ko: 선호는 후보를 기각하지 않고 순서만 정한다
title: Preferences order candidates without rejecting them
status: deprecated
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 선호는 설계 공간 파일의 `preferences` 절에 **수치 없이
부분순서로만** 적고 이유를 함께 남긴다. 선호는 **후보를 기각하지
않는다** — 후보가 여럿 남았을 때 유저에게 보여 주는 순서만 정한다.

```
space :auth-space
  candidates ... (7.4절과 동일)
  preferences
    :oauth2 > :mtls        reason: "운영 경험 있음"
    -- :apikey는 순서 없음 (이미 기각)
```

**근거** (노트 7.9·7.2절)
- 7.2절이 "선호는 필요 시 확장"으로 남긴 연성 제약의 구체 형태다.
- 후보의 기각은 제약 검사(가능 / 불가능)만이 한다. 선호에 수치를 넣으면
  7.2절이 미채택한 등급 표현으로 되돌아간다.
- 이미 제약으로 기각된 후보에는 순서를 매기지 않는다.
