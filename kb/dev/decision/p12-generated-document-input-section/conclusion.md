---
id: https://agentic-knowledge-base.dev/id/chunk/762ecb04-03db-46c8-8854-e5bf06971613
type: decision
level: concrete
title_ko: 입력이 많은 생성 문서는 목록을 입력 파일 절로 접고 트리플 수에 union 구성을 붙인다
title: A generated document with many inputs folds the list into an input file section and states the union behind its triple count
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-generated-document-standards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/4ae7ad6d-fabc-4925-bc6a-4aa518eeab55]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T23:13:50+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T23:15:22+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/77024f86-3aeb-445d-ad01-6a1bcd9eee54
composite: {id: https://agentic-knowledge-base.dev/id/composite/77024f86-3aeb-445d-ad01-6a1bcd9eee54, title_ko: 생성 문서의 입력 파일 절, title: Input file section of a generated document}
---
**결론** — 머리 `입력` 줄의 형태는 입력 파일 수로 갈린다. 경계는 `kb_lib.GENDOC_INPUT_INLINE_MAX`(6) 하나다. 입력 파일이 **일곱 이상**이면 접는다(유저 답 Q6-a, 2026-10-03).

| 입력 파일 수 | `입력` 줄 | 본문 |
|---|---|---|
| 상한 이하 | 파일 목록 · 지문 · 규모 | 해당 없음 |
| 상한 초과 | 개수 · 지문 · 규모 · `## 입력 파일` 절로의 링크 | 문서 끝의 `## 입력 파일` 절에 파일 전부를 디렉토리로 묶어 적는다 |

목록을 생략하지 않는다. 게이트 `gendoc`의 G4가 판정한다 — 목록 없이 개수만 적은 줄, 지문 없는 줄, 가리킨 절이 없는 줄, 구성원 증분의 합이 총수와 다른 줄, 증분 없는 옛 표기(`union: chunks·base`)의 줄이 FAIL이다.

규모 자리의 트리플 수에는 union 구성을 함께 적는다. 꼴은 `트리플 <n> (union: chunks +a · base +b · …)`이고 `kb_lib.gendoc_union`이 만든다(유저 답 Q40-a, 2026-10-04). 구성원의 이름과 순서는 `kb_lib.GENDOC_UNION_MEMBERS`의 선언 순서이고, 표에 없는 그래프 파일은 stem으로 뒤에 붙는다. 구성원마다 붙는 수는 앞 구성원들의 합집합에 더한 **증분**이고 증분의 합이 총수다. 같은 이름의 수치가 도구마다 갈리는 이유가 문서 안에 있어야 한다(현상 `agt:metricVariesByLoadingOption`). 생성기 `metrics`·`link`·`weave`가 이 표기를 쓴다. union 표기의 유무는 판정하지 않는다 — 표기가 있으면 수치를 판정한다.

이 결정은 `p12-generated-document-header`의 `입력` 줄을 입력이 많은 경우로 넓힌다.
