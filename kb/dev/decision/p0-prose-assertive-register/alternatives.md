---
id: https://agentic-knowledge-base.dev/id/chunk/44009da6-b682-4541-8444-f60e416529cd
type: decision
level: logical
title_ko: 추측·구어의 게이트화와 기존 청크 본문의 문체 일괄 재작성은 기각된다
title: Gating hedges and colloquialisms and rewriting existing chunk bodies for style in bulk are rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-spec-writing-standard}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T15:00:00+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/b1717fd1-9b2e-419a-8fc5-21184b6941a7
---
**대안** — 둘을 기각한다.

| 대안 | 기각 이유 |
|---|---|
| 추측·구어도 게이트로 거부한다 | 판정이 필요한 규칙이다. 판정 가능한 것만 게이트로 만든다는 원칙(`docs/tools.md`)에 따라 보고로 둔다 |
| 기존 청크 본문을 문체만을 이유로 일괄 재작성한다 | 본문이 바뀌면 `contentHash`가 바뀌고 그 청크의 링크가 재판정 대상이 된다(노트 4.3절). 2026-09-13의 문체 정리 커밋은 `kb/dev/`의 청크를 한 파일만 고쳤다 |
