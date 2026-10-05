---
id: https://agentic-knowledge-base.dev/id/chunk/ce8d3eb5-ad6e-4c2a-a5f5-812d366c8e06
type: decision
level: concrete
title_ko: 분할·병합 신호는 재사용·가정·변경 단위와 자립성에서 온다
title: Split and merge signals come from reuse, assumption, change granularity and self-containment
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-10-05T23:48:01+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-05T23:48:02+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/33419d0a-16bb-46ee-b5c0-7a84026523fd, https://agentic-knowledge-base.dev/id/chunk/166b54ec-3988-4fa3-87c4-8ab006ed9a08]
part_of: https://agentic-knowledge-base.dev/id/composite/bef41c67-e767-4eac-8a76-338d9a83913b
composite: {id: https://agentic-knowledge-base.dev/id/composite/bef41c67-e767-4eac-8a76-338d9a83913b, title_ko: 청크 분할과 병합, title: Chunk split and merge}
---
**결론** — 토큰 상한 초과 외에도 분할·병합 신호가 있다.

| 분할 신호 | 이유 |
|---|---|
| 라벨을 하나로 쓸 수 없음 | 두 주제 |
| 본문 일부만 다른 복합체에서 재사용하고 싶음 | 재사용 단위가 청크보다 작음 |
| 본문 일부에만 가정이 붙음 | 가정 입도가 청크보다 작음 |
| 본문 일부만 `suspect`가 됨 | 변경 단위가 청크보다 작음 |

| 병합 신호 | 이유 |
|---|---|
| 두 청크가 항상 함께 읽힘 | 분리가 조망만 방해 |
| 한 청크가 다른 청크 없이 이해 불가 | 자립성 위반 |
| 합쳐도 토큰 상한 이하 | 해당 없음 |

**분할·병합의 IRI 처리는 `p10-split-keeps-work-identity`가 정한다**(Q57-a).
