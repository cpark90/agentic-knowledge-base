---
id: https://agentic-knowledge-base.dev/id/chunk/bc0492c3-6e12-40ae-87db-73152143cee8
type: decision
level: concrete
title_ko: 그래프 검증만으로 명세를 검증된 것으로 보는 안은 택하지 않는다
title: Treating graph validation alone as verifying the specification is not taken
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-harness-recipes}, {resource: git:aeb0a58:chunks/decision/d-0190-verifiable-spec-alternatives.md}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T05:08:10+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T05:08:10+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/bff15384-be48-4304-95be-bcc0f46ef542
---
**대안** — 원천(harness-concrete `docs/odr-contract-verify.md`)이 대비한 안 하나를 택하지 않는다.

| 대안 | 택하지 않는 이유 |
|---|---|
| 그래프 검증(`validate.py`)만으로 명세를 검증된 것으로 본다 | 그래프가 잘 형성되었다는 것은 산출물이 능력의 계약을 만족한다는 것을 보이지 않는다. 그래서 명세에서 산출로 가는 방향의 판정기(`verify_contract.py`)를 둔다(문서 머리 절) |
