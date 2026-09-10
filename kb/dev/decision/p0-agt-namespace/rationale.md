---
id: https://agentic-knowledge-base.dev/id/chunk/19a56942-730c-49fc-80cb-c07cc7ee05f7
type: decision
level: logical
title_ko: 접두어가 이름에 붙어 있으면 출처와 미등록이 동시에 드러난다
title: A prefix on every name reveals both provenance and non-registration
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/d0df4af3-434f-43de-ac31-927b6cf902a8
---
**근거** (노트 0.3절)

- 접두어가 이름에 붙어 있으면 그 개념이 어느 어휘에서 왔는지가 드러나, 낯선
  이름을 아는 이름으로 오인하는 학습자료 종속(1.2절)이 차단된다.
- 외부 어휘의 정의를 이 체계에 맞춰 바꾸면 **같은 IRI를 읽는 외부 도구와
  추론기가 다른 뜻으로 동작한다.** 가져오되 고치지 않는다.
- 고유 개념에만 `agt:`가 붙으므로, 접두어 없는 이름이 나오면 그것이 아직
  어휘에 등록되지 않은 용어라는 것이 즉시 드러난다 — 어휘 밖 지식 거부의
  가장 싼 검사다.
