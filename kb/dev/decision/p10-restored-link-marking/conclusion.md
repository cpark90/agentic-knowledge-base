---
id: https://agentic-knowledge-base.dev/id/chunk/491041cd-b9d0-4cbd-be0b-97dff25b20c5
type: decision
level: concrete
title_ko: 복원 링크는 frontmatter의 restored 목록으로 표시하고 증거에 proposal을 더한다
title: Restored links are marked by the frontmatter restored list and add proposal evidence
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-09-19T16:10:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f715c53f-c9bd-49cc-b580-6e2d2343cd5c]
part_of: https://agentic-knowledge-base.dev/id/composite/66d847e5-4837-43ea-8498-da00a8fb92f3
composite: {id: https://agentic-knowledge-base.dev/id/composite/66d847e5-4837-43ea-8498-da00a8fb92f3, title_ko: 복원 링크 표시 = restored 목록, title: Restored-link marking = restored list}
---
**결론** — 복원(사후에 되짚어 이은) 링크는 링크 키에 그대로 적되, 같은 청크의 선택 키 **`restored: [<대상 IRI>…]`**에
대상을 한 번 더 적는다. `restored`의 IRI는 그 청크의 링크 키(`refines`·`serves`·`supersedes`·`verifies`·`satisfies`·
`constrains`·`derivesFrom`·`allocates`·`generates`) 어딘가에 대상으로 있어야 하고, 없으면 `chunk2kg`가 `FAIL [restored]`로
거부한다.

효과는 하나다 — 그 링크 개체(`agt:Link`)의 증거가 두 줄이 된다. `constructionRecord`(사람이 frontmatter에 적은 확정 기록)에
**`agt:proposal`**(후보의 출처 — 도구·에이전트의 제안)을 더한다. 상태는 `confirmed`다. 확정에는 구축 또는 실행의 양성 증거가
있어야 한다는 게이트(`confirmed-without-evidence`)는 그대로 성립한다. 복원 링크 = 구축 기록 아닌 증거를 하나라도 가진 링크이고,
복원 비율은 복원 링크 수를 전체 링크 수(구축 + 복원)로 나눈 값이며 `metrics`·`audit`가 `kb_lib.link_origins`의 같은 정의로 센다.

| 링크 | 증거 종류 | 상태 |
|---|---|---|
| 편집 부산물(구축) | `constructionRecord` | `confirmed` |
| 본문 식별자 추출(`cites`·`usesConcept`) | `constructionRecord` | 직접 술어 |
| `restored` 표시 | `constructionRecord` + `proposal` | `confirmed` |

2026-09-13에 옛 결정 27건과 `p12-documents-are-generated`에 사후로 이은 `refines` 28건이 첫 복원 링크다. 후보 생성기
`link`(`bazel build //kg:link_candidates`)가 제안한 링크를 사람이 채택할 때도 같은 표시를 쓴다. `relatedTo` 후보는 링크 키가
없어(`coUpdatesWith`뿐) 직접 술어로만 남고 복원 비율에 들지 않는다.
