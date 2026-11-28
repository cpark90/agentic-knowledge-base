---
id: https://agentic-knowledge-base.dev/id/chunk/84edf144-5585-40a3-af74-67eb25e0f52c
type: decision
level: logical
title_ko: 함수마다 링크·파일 본문 통째 인용·함수와 절을 부분으로 두기는 기각된다
former_title_ko: ["함수 청크마다 링크·9개씩 자르기·파일을 단일 청크로는 기각된다", "함수마다 링크·9개씩 자르기·파일을 단일 지식 항목으로는 기각된다", "함수마다 링크·9개씩 자르기·파일을 단일 단위 지식으로는 기각된다"]
title: Links on every function, quoting a whole file body, and keeping functions and sections as parts are rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-11-28T16:57:43+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-05T00:30:20+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T23:00:30+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-11-28T16:59:05+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/b9ff4ae2-fb83-447d-9aae-73d5264cfae3
---
**대안** — 넷을 기각한다.

| 대안 | 기각 이유 |
|---|---|
| 함수마다 링크를 단다 | 리팩터링마다 수십 건의 재검증 후보. 생성물에 손으로 쓴 링크는 다음 추출에서 지워진다 |
| 파일 본문 전체를 한 단위 지식으로 인용한다 | 2026-11-28 측정에서 소스 46개 가운데 34개가 인용 상한 2,856토큰을 넘었다. 파일 항목은 본문이 아니라 모듈 docstring과 import를 담고 원문은 소스에 둔다 |
| 함수와 절을 파일 복합체의 부분으로 두고 링크는 복합체가 갖는다(2026-10-05부터 2026-11-28까지의 결론) | 부분에는 결정으로 가는 링크가 없었고 바깥에서 가리키는 곳은 절 하나뿐이었다. 링크를 달지 않는 항목을 생성해 유지할 까닭이 없어 유저가 함수와 절의 항목을 두지 않기로 했다(Q191-a) |
| 부분을 9개씩 순서대로 자른다 | 순서에 뜻이 없는 묶음이 생긴다 — "순서를 요구하지 않는 것에 순서를 붙이면 거짓 정보"와 같은 오류다. 함수 하나를 더하면 모든 묶음의 경계가 밀린다 |
