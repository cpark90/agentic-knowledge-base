---
id: https://agentic-knowledge-base.dev/id/chunk/152657d9-8de4-4716-9783-5453903ec5b3
type: decision
level: logical
title_ko: 코어 결정의 규약 줄로 더하는 안과 절 청크 산문으로 두는 안은 기각된다
title: Adding a convention line to the skeleton decision and keeping the sentence as section prose are rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:12:48+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/2b47645a-4247-4eb8-a741-7a7a41d206cf
---
**대안** — 둘을 기각한다.

| 대안 | 기각 이유 |
|---|---|
| `p2-skeleton-and-domain-profile`의 `conventions.md`에 줄로 더한다 | 그 결론은 코어와 프로파일의 경계와 확장점을 진술할 뿐 답의 출처를 진술하지 않는다. 규약 줄은 그 결정의 결론이 진술하는 것의 세부만 담는다(`p4-convention-slot`). 결론에 없는 주장은 규약 줄이 아니다. 줄로 더하면 stable 결정의 결론을 승인 없이 넓힌다 |
| 문장을 `docs/method.md` 절 청크의 본문 산문으로 둔다 | 규범 문서를 결정의 투영으로 만드는 통일 기획의 전제는 규약마다 원본 결정이 있는 것이다. 산문으로 두면 이 절차 항목만 원본 없이 남는다 |
