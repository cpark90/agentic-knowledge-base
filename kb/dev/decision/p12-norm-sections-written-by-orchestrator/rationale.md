---
id: https://agentic-knowledge-base.dev/id/chunk/19371556-8119-45d0-a140-f025efc8677b
type: decision
level: logical
title_ko: 절 청크는 결정의 규약 줄을 가리키는 골격이고 그 줄의 저자가 orchestrator다
title: A section chunk is a skeleton pointing at the convention lines of decisions, and the orchestrator is the author of those lines
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T04:28:04+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/1129e152-2ac3-4104-94c7-9642040ca3a3
---
**근거** — 유저 답 Q21-a(2026-10-04)가 절 청크의 자리를 새 plane `norm`으로 정했다. 그 답은 plane을 정했고 쓰기 역할을 정하지 않았다. 쓰기 역할은 카탈로그에 `agt:writes agt:DocumentSectionChunk`로 orchestrator에 더해졌다. 역할 표는 그 날짜를 2026-10-04로 적는다. 카탈로그의 주석은 그 근거로 `p12-norm-documents-from-section-chunks`를 든다.

확인한 사실은 셋이다.

- 절 청크의 `items`는 결정의 `conventions.md` 줄을 `slug#k`로 가리킨다(`p12-norm-documents-from-section-chunks`). 절 청크는 줄을 새로 쓰지 않고 순서와 묶음만 정한다.
- 그 줄이 사는 결정 plane의 쓰기 역할은 orchestrator다(`p7-dev-roles-and-scopes`).
- 규범 문서의 원본 문장 이행은 orchestrator가 한다(`p12-norm-documents-from-section-chunks`).

게이트 `writer`의 판정 방식은 `tools/validate.py`의 `check_writer` docstring이 적는다. 생성자 역할의 `agt:writesIn`과 `agt:writes`로 판정하고, 쓰기 권한이 없는 역할의 청크는 권한 있는 역할의 `verified`로 통과한다.

미확정: 쓰기 역할을 orchestrator로 정한 판단을 비교·기록한 자리는 확인하지 못했다. 위 세 사실은 그 판단과 정합하지만 판단의 기록은 아니다.
