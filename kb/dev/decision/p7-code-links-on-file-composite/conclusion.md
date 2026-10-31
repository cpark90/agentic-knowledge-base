---
id: https://agentic-knowledge-base.dev/id/chunk/120eba0b-c9d8-433e-9f52-d35502589c23
type: decision
level: concrete
title_ko: 코드 단위 지식의 링크는 파일 복합체가 갖고 함수는 부분으로만 존재한다
former_title_ko: ["코드 청크의 링크는 파일 복합체가 갖고 함수 청크는 부분으로만 존재한다", "코드 지식 항목의 링크는 파일 복합체가 갖고 함수는 부분으로만 존재한다"]
title: Links on code belong to the file composite, and function chunks exist only as parts
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/f4facde9-b206-4be7-8599-3e373e6d3bc0]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-06T10:57:27+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T19:33:52+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T23:00:30+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/b9ff4ae2-fb83-447d-9aae-73d5264cfae3
composite: {id: https://agentic-knowledge-base.dev/id/composite/b9ff4ae2-fb83-447d-9aae-73d5264cfae3, title_ko: 코드 링크의 높이, title: The height of links on code}
---
**결론** — 함수에는 링크를 달지 않는다. `refines`·`serves`·`verifies`의 대상과 출발점은 **파일 복합체**(선언 단위 지식 = 단위 지식 파일)다. 함수는 `part_of`로만 존재한다.

| 단 | 무엇이 있는가 | 누가 쓰는가 |
|---|---|---|
| 파일 복합체 | 결정·요구로의 `refines`/`serves`, 검증기의 `verifies` 도착점, 가정 | 사람 — 등록부 또는 선언 파일에 적고 추출기가 단위 지식 파일로 옮긴다 |
| 절 복합체(소스의 절 주석 단위) | `part_of` 파일, `ordered` = 소스 순서 | 추출기 |
| 함수 | `part_of` 절, 본문 = 소스 인용, `contentHash` | 추출기 |

함수를 고치거나 쪼개거나 합쳐도 **링크가 움직이지 않는다** — 바뀌는 것은 복합체의 부분 목록과 함수의 해시뿐이다. 그래서 리팩터링 한 번이 수십 건의 재검증을 부르지 않는다. 결정 밖 복합체 규칙(`kb_composite`, 2026-09-29)이 이것의 전제다.

부분이 9를 넘는 파일은 소스의 절 주석으로 중간 복합체를 세운다 — 절이 없으면 추출기가 요구한다(FAIL). 9개씩 자르는 것은 순서에 뜻이 없는 묶음이라 하지 않는다.

**게이트** (Q47-b, verify) — 추출 트리 `kb/dev/artifact/` 안에서 복합체의 부분인 단위 지식(정의 단위 지식, 절·장·모듈 머리의 구역 단위 지식)이 `refines`·`serves`·`verifies`의 주어나 대상이면 `validate`의 `check_code_part_link`가 거부하고 게이트 id는 `code-part-link`다(2026-10-05). 판정에 부분 관계(`agt:hasDirectPart`)와 단위 지식 위치가 함께 필요해 병합 그래프를 보는 `validate`가 자리다. 판정 함수 `kb_lib.code_part`는 복원 후보 생성기 `link`가 코드 부분 끝점의 후보를 거르는 데에도 쓴다. 추출기는 구역 단위 지식에 링크를 복사하지 않고, 연결은 선언 단위 지식과 복합체의 합침(Q49-a)과 `part_of`로 선다. 해소는 developer가 링크를 등록부의 `refines`·`serves`로 옮기고 재추출하는 것이다.
