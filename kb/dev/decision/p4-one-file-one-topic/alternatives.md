---
id: https://agentic-knowledge-base.dev/id/chunk/e28252ce-4993-47eb-b8c9-dacbc0c68963
type: decision
level: logical
title_ko: 라벨 대표성의 기계 판정과 코드 청크의 파일 내 심볼 범위 해석은 기각된다
title: Machine-judging label representativeness and resolving code chunks to symbol ranges inside a file are rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T15:00:00+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/f56035ce-db13-4b21-a3a2-5f5a173f7e03
---
**대안** — 둘을 기각한다.

| 대안 | 기각 이유 |
|---|---|
| 라벨이 본문을 대표하는지 게이트로 판정한다 | 의미 판정이라 기계가 판정하지 못한다. `docs/rules.md`의 라벨 행이 "검사 불가, 규약"으로 적는다 |
| 코드 청크를 소스 파일 안의 심볼 범위로 두고 별도 파일을 만들지 않는다 | 노트 4.9절의 원래 해석이다. 코드 청크는 추출 방향의 결정(`p7-code-extraction-direction`)으로 함수 하나가 청크 파일 하나가 되었고, 그 결정이 tangle과 추출의 비교를 다룬다 |
