---
id: https://agentic-knowledge-base.dev/id/chunk/aafaca3e-cac9-44c9-a274-7593f821c38b
type: decision
level: logical
title_ko: 횡단 개념을 plane에 넣으면 분류가 무너지고 규칙 변경이 어휘를 흔든다
title: Cross-cutting concepts break plane classification; rule churn must not shake the vocabulary
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/301046f4-6db7-42f5-aea0-ffe4599d4a15
---
**근거** (노트 2.3절) — 스코프·가정 같은 횡단 개념을 억지로 plane 안에 넣으면 plane 분류 자체가 무너진다. plane은 판정 방식으로 정의되는데 이것들은 판정 대상이 아니라 판정의 조건이기 때문이다.

어휘는 안정적이고 규칙은 자주 바뀐다. 둘을 한 모듈에 두면 규칙이 바뀔 때마다 어휘 사용자가 영향을 받는다. 분리하면 `defect`를 import한 쪽은 `defect-rules`의 변경과 무관하다.

기존 모듈 수정을 금지하고 확장만 허용하면 import한 쪽의 가정이 깨지지 않는다 — 2.11절 프로파일 규칙이 이 규칙의 특수화다.
