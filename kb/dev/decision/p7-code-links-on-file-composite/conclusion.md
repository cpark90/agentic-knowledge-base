---
id: https://agentic-knowledge-base.dev/id/chunk/120eba0b-c9d8-433e-9f52-d35502589c23
type: decision
level: concrete
title_ko: 코드 청크의 링크는 파일 복합체가 갖고 함수 청크는 부분으로만 존재한다
title: Links on code belong to the file composite, and function chunks exist only as parts
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/f4facde9-b206-4be7-8599-3e373e6d3bc0]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-09-30T14:00:00+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/b9ff4ae2-fb83-447d-9aae-73d5264cfae3
composite: {id: https://agentic-knowledge-base.dev/id/composite/b9ff4ae2-fb83-447d-9aae-73d5264cfae3, title_ko: 코드 링크의 높이, title: The height of links on code}
---
**결론** — 함수 청크에는 링크를 달지 않는다. `refines`·`serves`·`verifies`의 대상과 출발점은 **파일 복합체**(선언 청크 = 파일 청크)다. 함수 청크는 `part_of`로만 존재한다.

| 층 | 무엇이 있는가 | 누가 쓰는가 |
|---|---|---|
| 파일 복합체 | 결정·요구로의 `refines`/`serves`, 검증기의 `verifies` 도착점, 가정 | 사람 — 등록부 또는 선언 파일에 적고 추출기가 파일 청크로 옮긴다 |
| 절 복합체(소스의 절 주석 단위) | `part_of` 파일, `ordered` = 소스 순서 | 추출기 |
| 함수 청크 | `part_of` 절, 본문 = 소스 인용, `contentHash` | 추출기 |

함수를 고치거나 쪼개거나 합쳐도 **링크가 움직이지 않는다** — 바뀌는 것은 복합체의 부분 목록과 함수 청크의 해시뿐이다. 그래서 리팩터링 한 번이 수십 건의 재판정을 부르지 않는다. 결정 밖 복합체 규칙(`kb_composite`, 2026-09-29)이 이것의 전제다.

부분이 9를 넘는 파일은 소스의 절 주석으로 중간 복합체를 세운다 — 절이 없으면 추출기가 요구한다(FAIL). 9개씩 자르는 것은 순서에 뜻이 없는 묶음이라 하지 않는다.
