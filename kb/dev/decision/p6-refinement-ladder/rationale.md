---
id: https://agentic-knowledge-base.dev/id/chunk/45e43552-9031-4883-94e7-a05309a79dcc
type: decision
level: logical
title_ko: abstract는 기계가독의 경계이고 logical은 기준의 보존소다
title: Abstract is the machine-readable boundary, logical the store of criteria
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/5ef6f4a9-343a-4f00-8e88-172521022d6b
---
**근거** (노트 6.1절) — 두 지점이 이 계층의 핵심이다.

- **abstract는 기계가독의 경계다.** functional → abstract 전이가 자연어를 형식 언어로 옮기는 단계이고, 이 단계를 지나야 나머지가 기계 처리 대상이 된다. 형식화의 어려움과 범위 전개의 어려움이 이 경계에서 갈라진다.
- **logical은 근거와 기준의 보존소다.** 선택되지 않은 대안과 배제 이유, 그리고 **무엇으로 합격을 판정할 것인가**가 여기 있다. 합격 기준은 logical에서 판정식으로 태어나 executable의 검증 역할에 바인딩된다.
- 각 level의 판정 방식이 6.8절 전이 게이트의 근거다. 게이트는 "이 단계가 상위 단계에 무엇을 빚지고 있는가"를 그 판정 방식으로 묻는다.

인증 예 — functional "외부 클라이언트가 인증을 요청하면 시스템은 토큰을 검증해야 한다" → abstract `variable = agt:AuthenticationMethod` → logical `domain = {OAuth2, mTLS}`, `¬APIKey`, 기준 "만료 토큰 → 401", 판정식 `status == 401` → concrete OAuth2, 만료 토큰 3종(경계값) → executable `verify_token()`[구현]·`test_expired_token()`[검증].
