---
id: https://agentic-knowledge-base.dev/id/chunk/84731d3e-234e-4938-bfee-125be1dcde19
type: decision
level: logical
title_ko: 복원 링크를 구축으로 세면 복원 비율이 거짓 0이 된다
title: Counting restored links as construction makes the restoration ratio a false zero
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-09-19T16:10:00+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/66d847e5-4837-43ea-8498-da00a8fb92f3
---
**근거** (노트 9.3절·10.4절; `p10-link-by-construction`·`p10-link-judgement-evidence`) — 복원 비율 < 20%는 3단계와 8단계의
통과 조건인데, 도구가 frontmatter 링크를 모두 구축 기록으로 표기하면 비율은 항상 0이고 조건은 검사되지 않는다. 링크 개체의
증거 종류는 이미 어휘(`agt:EvidenceKind`)에 있으므로 표시 하나면 된다.

`proposal`은 "에이전트가 후보를 제안했고 확정 근거가 아니다"라는 뜻이라 사후 복원의 출처와 같다. 확정 자체는 사람이
frontmatter에 적는 행위이고 그 기록이 `constructionRecord`다 — 그래서 증거는 두 줄이며, 구축 또는 실행의 양성 증거 없이 확정을
금하는 게이트(`confirmed-without-evidence`, 노트 9.11절)가 `proposal` 한 줄이었다면 29건을 거부했을 것이다(2026-09-19 실측).
표시를 링크 키와 분리해 목록으로 두면 링크의 해석(deps·TIM·수준 규칙)은 바뀌지 않는다. 검사 가능성은 높다 — 목록의 IRI가
링크 대상에 있는가는 기계 검사다.
