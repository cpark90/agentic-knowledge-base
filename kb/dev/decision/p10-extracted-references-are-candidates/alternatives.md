---
id: https://agentic-knowledge-base.dev/id/chunk/6dd38a8c-9ce8-40df-9c66-c1254967330c
type: decision
level: logical
title_ko: 추출 참조를 확정으로 승격하거나 제안 증거로 다는 안은 기각된다
title: Promoting extracted references to confirmed or tagging them as proposal evidence is rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-09-19T17:20:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/91fabd55-5c34-4d7e-a663-4dc72e486767
---
**대안** — 넷을 기각한다.

| 대안 | 기각 이유 |
|---|---|
| 추출 참조를 확정 링크(`agt:Link`, `confirmed`)로 | 저자 확인 없는 확정은 근거 없는 할당이다(r-011). 확정은 frontmatter에 적는 행위다 |
| 증거 종류를 `proposal`로(조사 원안) | 저자가 적은 식별자는 제안이 아니라 기록이다 — 유저 결정 2026-09-12 (b)와 충돌한다 |
| `assumes`·`part_of`도 후보로 | 조건과 구성은 링크가 아니다(4.5절). 두 메커니즘이 겹친다 |
| 추출을 없애고 frontmatter 링크만 | 본문의 식별자가 산문으로만 남아 후보 생성의 가장 강한 근거를 버린다 |
