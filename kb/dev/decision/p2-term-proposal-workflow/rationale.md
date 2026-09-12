---
id: https://agentic-knowledge-base.dev/id/chunk/a4c6c588-8b4e-4c18-a603-098425b72609
type: decision
level: logical
title_ko: 어휘 확장만 예외로 두면 어휘가 가장 약한 고리가 된다
title: Exempting vocabulary growth would make the vocabulary the weakest link
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
verified: [{by: process:label-judge-20260911, at: 2026-09-11T18:50:00+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/07c94f4c-0307-4273-9c25-f90fc5152e7b
---
**근거** (노트 2.5절 용어 제안 워크플로) — 어휘는 그 위의 모든 문장을 규정하므로 가장 통제가 강해야 하는데, 관측에서 개념을 뽑는 일은 에이전트만 할 수 있다. 제안과 판정을 분리하면 두 사실이 동시에 성립한다 — 에이전트가 어휘를 자라게 하되 어휘를 바꾸지는 못한다.

template 행을 청크 규칙 아래 두면 제안이 곧 검토 가능한 지식 항목이 된다. 형식이 다르면 42줄 상한·라벨 규칙·출처 강제가 어휘 확장 경로에서만 빠져나간다.

코어가 아닌 확장 모듈에 병합하는 것은 2.3절 "확장은 새 모듈 추가로만"의 직접 적용이다. `prov:wasDerivedFrom` 연결이 있어야 "이 개념은 어느 관측에서 왔는가"(CQ8)에 답한다.
