---
id: https://agentic-knowledge-base.dev/id/chunk/5d6b01cd-e551-4242-93d1-f2095e158f2a
type: decision
level: concrete
title_ko: 주석과 산출물을 분리하는 도구가 필요하다
title: A tool is needed to keep annotation out of the artifact
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/11e18898-7eae-41f7-8fb3-f1e2ccbfcbc4]
part_of: https://agentic-knowledge-base.dev/id/composite/67157f22-93ba-4abe-a303-d058de25ef7f
composite: {id: https://agentic-knowledge-base.dev/id/composite/67157f22-93ba-4abe-a303-d058de25ef7f, title_ko: 주석과 산출물의 분리, title: Separating annotation from artifact}
---
**결론** — **주석과 산출물을 분리하는 도구가 필요하다.** 주석이 산출물에
인라인으로 박혀 있는 한(코드 주석, 문서의 여백 메모) 두 plane은 항상 함께
적재된다.

`annotation` 청크는 대상 청크 IRI를 갖는 **standoff 앵커**로 붙고(5.1절 청크
ID의 해석), 산출물 파일과 설명 문서는 각각 다른 뷰 질의의 결과다(4.6절).
