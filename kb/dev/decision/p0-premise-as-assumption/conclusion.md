---
id: https://agentic-knowledge-base.dev/id/chunk/58f3cbc1-59c8-452f-b97a-6df0ec78c801
type: decision
level: concrete
title_ko: 전제는 가정으로 만들어 assumes로 가리키고 고유 전제를 적기 전에는 기본 가정을 가리킨다
title: A premise becomes an assumption referenced by assumes, and the default assumption holds the place until the item's own premise is written
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-dependency-graph-design}, {resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/e5c0cbc6-cabf-4594-8733-fa2e045f1249]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T15:00:00+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/c6086cf0-0a2c-47d6-96d4-644307e4529c
composite: {id: https://agentic-knowledge-base.dev/id/composite/c6086cf0-0a2c-47d6-96d4-644307e4529c, title_ko: 가정 — 전제의 기록, title: Assumptions — recording premises}
---
**결론** — 항목에 전제가 있으면 가정을 만들고 `assumes`로 가리킨다. 가정은 ODD 조건 위의 명제다(`p0-odd-scope-assumption`).

**기본 가정 후 좁힘**이 규칙이다(유저 수용 2026-09-12). 고유 전제를 아직 적지 않은 청크는 기본 가정 `id:asm-chunk-conventions`를 `assumes`한다. 기본 가정은 저장소 구조와 언어 정책의 두 조건 위의 명제다. 항목의 실제 전제가 드러나면 고유 가정을 앞에 더한다. 기본 가정은 항목이 청크 규약에도 기대는 한 남는다.

기본 가정만 가진 항목은 전제를 아직 적지 않은 것이다. 그것을 잡는 것은 리뷰다. 좁힘의 진행은 `metrics`의 가정 절이 잰다.
