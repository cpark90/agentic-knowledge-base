---
id: https://agentic-knowledge-base.dev/id/chunk/14782c7c-bf50-47a8-ab11-62715aeeb63e
type: decision
level: concrete
title_ko: 프로젝트를 넘는 것은 어휘·제약·ODD 코어이고 청크는 넘지 않는다
title: Vocabulary, constraints, and the ODD skeleton cross projects; chunks do not
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/d8e8aa97-d95c-4962-a88a-94e047702e4d, https://agentic-knowledge-base.dev/id/chunk/20148952-30c4-4f76-8cbf-4d9b32c68b25]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0149]
part_of: https://agentic-knowledge-base.dev/id/composite/8dbf8cd0-81dd-478f-b73e-3aeea905768f
composite: {id: https://agentic-knowledge-base.dev/id/composite/8dbf8cd0-81dd-478f-b73e-3aeea905768f, title_ko: 프로젝트 간 재사용의 단위, title: The unit of cross-project reuse}
---
**결론** — 3.7절 "이전 ODD 복사"의 확장. 프로젝트를 넘는 것은 **어휘·제약·
ODD 코어**이고, **청크는 재사용하지 않는다.**

| 재사용 대상 | 방식 | 조건 |
|---|---|---|
| 온톨로지 | 공유. 프로젝트별 확장 모듈만 추가 | 코어 수정 금지 |
| ODD | 복사 후 축소·확장 | 3.6절 변경 유형 |
| 일반화으로 올라간 제약 | 온톨로지 공리로 자동 상속 | — |
| `defect` 어휘 | 공유 | — |
| 청크 | 재사용하지 않음 | 프로젝트 ODD 안에서만 유효 |
