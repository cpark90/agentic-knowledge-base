---
id: https://agentic-knowledge-base.dev/id/chunk/a9505b08-0ae3-41e9-8f98-d6f6fe4a2ac9
type: decision
level: logical
title_ko: 스키마의 상향 귀속과 변경 전파는 파생 링크로만 성립한다
title: Schema ascription and change propagation exist only through derivation links
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/opus-5, at: 2026-09-10T20:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/d7435609-eefb-48a3-bab6-2cab0f56476e
---
**근거** (노트 7.6절, 7.1절, 10.11절) — 스키마가 결정 없이 생기면 상향 귀속(7.1절)이 끊긴다 — 어느 요구가 이 필드를 요구했는지 답할 수 없다. `constrains`가 있어야 비호환 변경이 어느 계약을 재판정 대상으로 만드는지 계산되고(10.11절), 호환/비호환을 `wasRevisionOf`/`supersedes`로 나누는 것은 4.10절 정체성 규칙(같은 것의 개정 vs 새 것)의 적용이다.
