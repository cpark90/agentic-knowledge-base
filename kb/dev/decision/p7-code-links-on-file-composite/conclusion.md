---
id: https://agentic-knowledge-base.dev/id/chunk/120eba0b-c9d8-433e-9f52-d35502589c23
type: decision
level: concrete
title_ko: 코드 단위 지식의 링크는 부분 없는 파일 항목이 갖는다
former_title_ko: ["코드 청크의 링크는 파일 복합체가 갖고 함수 청크는 부분으로만 존재한다", "코드 지식 항목의 링크는 파일 복합체가 갖고 함수는 부분으로만 존재한다", "코드 단위 지식의 링크는 파일 복합체가 갖고 함수는 부분으로만 존재한다"]
title: Links on code belong to the file chunk, which has no parts
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/f4facde9-b206-4be7-8599-3e373e6d3bc0]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-11-28T16:57:43+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-06T10:57:27+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T19:33:52+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T23:00:30+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-11-28T16:59:05+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/b9ff4ae2-fb83-447d-9aae-73d5264cfae3
composite: {id: https://agentic-knowledge-base.dev/id/composite/b9ff4ae2-fb83-447d-9aae-73d5264cfae3, title_ko: 코드 링크의 높이, title: The height of links on code}
---
**결론** — 코드의 `refines`·`serves`·`verifies`의 대상과 출발점은 **파일 항목**이다. 파일 항목은 코드 파일의 모듈 항목과 질의 파일의 질의 항목이다. 코드 파일은 부분 없는 파일 항목 하나로 추출되므로(Q191-a, `p7-code-extraction-direction`) 함수와 절에는 링크를 달 자리가 없다.

| 단 | 무엇이 있는가 | 누가 쓰는가 |
|---|---|---|
| 파일 항목 | 결정·요구로의 `refines`/`serves`, 검증기의 `verifies` 도착점, 가정 | 사람 — 등록부 또는 선언 파일에 적고 추출기가 단위 지식 파일로 옮긴다 |

함수를 고치거나 쪼개거나 합쳐도 **링크가 움직이지 않는다** — 링크의 끝인 파일 항목의 정체성(IRI)이 그대로다. 그래서 리팩터링 한 번이 수십 건의 재검증을 부르지 않는다.

**게이트** — 함수와 절을 부분으로 추출하던 동안에는 부분이 링크의 끝이면 `validate`의 `check_code_part_link`가 거부했고 게이트 id는 `code-part-link`였다(Q47-b, 2026-10-05). 추출기는 부분이 9를 넘는 파일에 절 주석을 요구했다. 코드 파일에 부분이 없으면 두 검사는 판정할 대상이 없으므로 없앤다(Q191-a). 링크를 파일 항목에만 둔다는 규칙은 추출기가 등록부의 `refines`·`serves`를 파일 항목에만 옮기는 것으로 선다.
