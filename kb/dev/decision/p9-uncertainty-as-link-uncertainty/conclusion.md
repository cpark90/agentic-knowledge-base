---
id: https://agentic-knowledge-base.dev/id/chunk/5b6ac70d-af5e-48ed-8e23-c7a66921493f
type: decision
level: concrete
title_ko: 모든 미확정은 연결의 미확정이다
title: All uncertainty is uncertainty about links
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f715c53f-c9bd-49cc-b580-6e2d2343cd5c]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0096]
part_of: https://agentic-knowledge-base.dev/id/composite/d85fdc0a-47c2-499e-9379-813c5a5cc167
composite: {id: https://agentic-knowledge-base.dev/id/composite/d85fdc0a-47c2-499e-9379-813c5a5cc167, title_ko: 모든 미확정은 연결의 미확정이다, title: All uncertainty is uncertainty about links}
---
**결론** — 이 체계에서 미확정은 언제나 **두 지식 항목이 연결되는가**의 미확정이다. 값이 미정인 것처럼 보이는 경우도 연결로 환원한다.

"인증 방식이 미정이다"는 functional 항목 `인증 필요`에서 concrete 후보 `OAuth2`·`mTLS`·`APIKey`로 가는 `refines` 링크 셋 중 **어느 것이 성립하는가**의 문제다. 결정한다는 것은 값을 고르는 일이 아니라 **링크 하나를 확정하고 나머지를 기각하는 일**이다.

이 환원은 사다리의 특정 단계에 갇히지 않는다. 수직 링크(`refines`)의 후보는 주로 logical에 열거되지만, 수평 링크(`satisfies`·`constrains`·`verifies`)의 후보는 확정된 concrete 항목 사이에도 생긴다 — 확정된 시그니처가 어느 확정된 결정을 충족하는지 아직 모를 수 있다. **연결이 있는 곳이면 어디든 가능성이 표현된다.**
