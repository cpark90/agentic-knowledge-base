---
id: https://agentic-knowledge-base.dev/id/chunk/55535378-f5cd-4f01-a5ce-54d438529104
type: decision
level: concrete
title_ko: 본문에서 추출한 참조는 후보 링크 개체이고 확정은 frontmatter에 적는 것이다
title: References extracted from bodies are candidate link entities and confirmation is written in the frontmatter
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T19:33:51+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}]
layer: methodology
refines: [https://agentic-knowledge-base.dev/id/chunk/f715c53f-c9bd-49cc-b580-6e2d2343cd5c]
part_of: https://agentic-knowledge-base.dev/id/composite/91fabd55-5c34-4d7e-a663-4dc72e486767
composite: {id: https://agentic-knowledge-base.dev/id/composite/91fabd55-5c34-4d7e-a663-4dc72e486767, title_ko: 본문 추출 참조 = 후보 링크, title: Extracted references = candidate links}
---
**결론** — `extract_refs`가 본문에서 뽑는 참조(`agt:cites` — 단위 지식 식별자, `agt:usesConcept` — 온톨로지 용어)는 **후보 링크**
개체(`agt:CandidateLink`, `agt:linkState "candidate"`)로 방출한다. 증거는 `constructionRecord`(저자가 본문에 적은 식별자는
구축 기록이다 — `p10-link-by-construction`, 유저 결정 2026-09-12)이고 `evidenceRef`는 그 단위 지식이다. 직접 술어(`agt:cites`·
`agt:usesConcept`)는 그대로 둔다 — 질의·지표가 쓴다.

확정은 사람이 앵커 단위 지식의 frontmatter 링크 키에 대상을 적는 행위다. 후보 생성기 `link`(`//kg:link_candidates`)가 후보 중
frontmatter 링크가 없는 쌍을 판정 대상으로 낸다. `assumes`(조건)와 `part_of`(구성)는 링크가 아니므로 후보로 만들지 않는다.

| 링크의 출처 | 개체 | 상태 | 증거 |
|---|---|---|---|
| frontmatter 링크 키 | `agt:Link` | `confirmed` | `constructionRecord` (+ `proposal` — `restored`) |
| 본문 추출 참조 | `agt:CandidateLink` | `candidate` | `constructionRecord` |

지표(`kb_lib.link_origins`)는 후보를 구축과 따로 세고, 복원 비율은 복원 / (확정 구축 + 복원)이다. 이로써 10.4절의
"후보 → 제약 검사 → 판정 → 확정"이 처음으로 데이터를 갖는다(2026-09-19, 후보 30 — `usesConcept`는 치역이 단위 지식이
아니라 후보 개체가 아니다).

**게이트** `extract-refs`·`dangling`(노트 4.8절 참조 무결성, 실행 계층 verify와 생성 시점) — `extract_refs`가 생성 시점에, `validate`의 dangling 검사가 그래프에서 대상이 실재하지 않는 인용·부분·가정·요구를 거부한다. 2026-09-30부터는 정의의 호출 대상(`agt:usesDefinition`, 추출기가 내는 frontmatter `uses`)도 본다. 이 관계는 링크 개체가 없는 참조 족이므로 이 검사가 유일한 실재 검사다. 해소는 저작자가 인용 대상을 정정하는 것이다.
