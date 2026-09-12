---
id: https://agentic-knowledge-base.dev/id/chunk/d69c38aa-659d-48fe-9a65-2b8b04d1d8fd
type: decision
level: concrete
title_ko: 정제는 네 전이이며 전이마다 근거와 refines를 남긴다
title: Descent is four transitions, each leaving rationale and refines
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/f4facde9-b206-4be7-8599-3e373e6d3bc0, https://agentic-knowledge-base.dev/id/chunk/f715c53f-c9bd-49cc-b580-6e2d2343cd5c]
part_of: https://agentic-knowledge-base.dev/id/composite/3eec3426-b051-4594-8d32-be0867520885
composite: {id: https://agentic-knowledge-base.dev/id/composite/3eec3426-b051-4594-8d32-be0867520885, title_ko: 정제 — 구체화의 네 전이, title: Descent - the four refinement transitions}
---
**결론** — 정제(구체화)은 네 전이다.

- **functional → abstract 형식화** — 요구를 온톨로지 어휘의 형식 문장으로 옮긴다
- **abstract → logical 전개** — 변수에 범위·제약·판정식을 준다
- **logical → concrete 표본 추출** — 범위에서 값을 고른다
- **concrete → executable 생성** — 산출물을 만들고 합격 기준을 바인딩한다

**각 전이는 근거를 남기고 `refines` 링크를 남긴다** (9.2절). 계층은 링크로 구현되며 전이의 근거는 링크의 속성이다.

**도메인은 임의 목록이 아니라 온톨로지의 하위 개념이고 값 범위는 ODD 안이다.** 새 후보를 추가하려면 온톨로지에 개념을 먼저 추가해야 한다.
