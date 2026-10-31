---
id: https://agentic-knowledge-base.dev/id/chunk/5527d1e0-08e2-47ea-ade8-5322f5dc9fc0
type: norm
level: logical
title_ko: docs/rules.md 절 — 신뢰 등급과 그 위의 두 검사
title: docs/rules.md section — Trust tiers and the two checks on them
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T01:17:27+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/a57b18df-3b8b-4579-a0f8-db4655159538
heading: 신뢰 등급 — 누가 만들고 누가 검증했는가
depth: 3
form: table
columns: [검사, 강제하는 것]
items: [p2-trust-tier-from-generated-and-verified#3, p2-trust-tier-from-generated-and-verified#4]
---
행위자 표기는 OKF의 행위자 규약을 그대로 써서, 도구는 `<생성기>/<버전>`, 사람은 `human:<id>`, 프로세스는
`process:<id>`로 적는다. 신뢰 등급은 저장하지 않고 질의로 얻는다. `verified`가 없으면 등급은 **미검증**이고,
`human:` 없는 검증만 있으면 **기계 확인**, `human:`이 있는 검증이 있으면 **사람 검토**다.

게이트 둘이 이 등급 위에서 검사한다.
