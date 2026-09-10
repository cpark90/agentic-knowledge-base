---
id: https://agentic-knowledge-base.dev/id/chunk/79bcc1dd-4036-43ef-b30d-f4dff07be513
type: decision
level: concrete
title_ko: 가정에는 판정 유형과 판정 식을 함께 적는다
title: Every assumption records its verification kind and expression
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/e5c0cbc6-cabf-4594-8733-fa2e045f1249]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0087]
part_of: https://agentic-knowledge-base.dev/id/composite/674dc862-8a79-40df-a50e-9643d9caca63
composite: {id: https://agentic-knowledge-base.dev/id/composite/674dc862-8a79-40df-a50e-9643d9caca63, title_ko: 가정 판정 방법의 유형, title: Kinds of assumption verification method}
---
**결론** — 6.5절 "기계적으로 판정 가능한 형태"의 유형은 다섯이며 3.9절 판정 방법 등급과 짝을 이룬다.

- **그래프 질의** — `project-kg`에 특정 개체·관계가 존재하는가 ("`agt:ExternalClient` 개체가 있다")
- **파일 검사** — 특정 파일·값이 존재하는가 ("lockfile에 FastAPI ≥ 0.110")
- **실행 검사** — 명령이 특정 결과를 내는가 ("헬스체크 200")
- **외부 조회** — 외부 시스템 상태 ("device-harvest API가 v2")
- **사람 확인** — 유저가 참이라고 답함 ("고객이 여전히 이 기능을 원한다")

가정 청크의 assertion에 **판정 유형과 판정 식을 함께 적는다.** 판정 식이 없는 가정은 `unverified`로만 존재한다.
