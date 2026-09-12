---
id: https://agentic-knowledge-base.dev/id/chunk/6b7ed24a-88b6-4acf-8ac7-285cee097957
type: decision
level: concrete
title_ko: ODD 변경은 확장·축소·정밀화 셋이고 온톨로지가 선행한다
title: ODD changes are widen, narrow, or refine, and the ontology comes first
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
verified: [{by: process:label-judge-20260911, at: 2026-09-11T18:50:00+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/fd0d3d18-4aab-4c4c-8f72-41702860b68c, https://agentic-knowledge-base.dev/id/chunk/33419d0a-16bb-46ee-b5c0-7a84026523fd]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0062]
part_of: https://agentic-knowledge-base.dev/id/composite/d53cfcf9-c765-4bfe-b787-a420967a6f35
composite: {id: https://agentic-knowledge-base.dev/id/composite/d53cfcf9-c765-4bfe-b787-a420967a6f35, title_ko: ODD 유지 관리, title: Maintaining the ODD}
---
**결론** — ODD는 살아 있는 문서다. 버전 관리되고, 변경은 검토 대상이다. 변경 유형은 셋뿐이다.

| 유형 | 내용 | 파급 |
|---|---|---|
| **확장** | 속성이나 값 범위 추가 (이탈 반복·일반화·유저 요구) | 새 속성의 logical 범위·케이스 확장 필요 |
| **축소** | 명시 제외 추가 또는 범위 축소 | 축소된 범위에 의존하던 항목 무효화 |
| **정밀화** | 판정 방법 개선 (`unverified` 감소) | 대조 정확도 향상. 파급 없음 |

**확장은 온톨로지 어휘 안에서만 가능하다.** ODD에 새 속성을 추가하려면 그 속성이 `related/condition`에 먼저 있어야 하고, 없으면 온톨로지 확장(2.3절)이 선행한다. **순서: 온톨로지 → ODD → 파생물.**

ODD 변경은 전파의 트리거다 — 변경된 속성을 참조하는 **스코프·가정·기준·케이스 전부가 재검토 목록에 오른다.** 편집 권한은 설계 에이전트에게만, 승인은 유저에게 둔다.
