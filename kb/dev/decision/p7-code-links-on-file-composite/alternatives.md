---
id: https://agentic-knowledge-base.dev/id/chunk/84edf144-5585-40a3-af74-67eb25e0f52c
type: decision
level: logical
title_ko: 함수 청크마다 링크·9개씩 자르기·파일을 단일 청크로는 기각된다
title: Links on every function chunk, cutting nine at a time, and one chunk per file are rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-09-30T14:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/b9ff4ae2-fb83-447d-9aae-73d5264cfae3
---
**대안** — 셋을 기각한다.

| 대안 | 기각 이유 |
|---|---|
| 함수 청크마다 링크를 단다 | 리팩터링마다 수십 건의 재판정 후보. 생성물에 손으로 쓴 링크는 다음 추출에서 지워진다 |
| 부분을 9개씩 순서대로 자른다 | 순서에 뜻이 없는 묶음이 생긴다 — "순서를 요구하지 않는 것에 순서를 붙이면 거짓 정보"와 같은 오류다. 함수 하나를 더하면 모든 묶음의 경계가 밀린다 |
| 파일 하나를 단일 청크로 둔다 | 1,681줄이 한 청크가 되어 42줄 자립 단위의 뜻을 잃고, 검증기가 함수 단위로 `verifies`할 자리가 없다 |
