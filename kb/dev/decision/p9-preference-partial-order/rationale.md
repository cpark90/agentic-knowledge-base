---
id: https://agentic-knowledge-base.dev/id/chunk/67571819-4620-4639-9e59-46e9fe4e7e29
type: decision
level: logical
title_ko: 순서와 기각을 분리해야 임의 선택이 다시 열리지 않는다
title: Separating ranking from rejection keeps arbitrary choice closed
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/d019ef5c-899b-459f-98cb-80d0fd72a0c4
---
**근거** (노트 9.9절·8.2절) — 선호에 기각 권한을 주면 근거 없는 수치가 후보를 지우게 되고, 등급을 미채택한 이유(캘리브레이션 부재)가 뒷문으로 돌아온다. 순서만 갖는 선호는 후보 집합을 바꾸지 않으므로 제약 전파의 결과를 오염시키지 않는다.

이유(`reason`)를 함께 적게 하는 것은 선호 자체가 나중에 제약으로 승격될 수 있는지 판단할 재료를 남기기 위해서다.
