---
id: https://agentic-knowledge-base.dev/id/chunk/47ba1172-488a-4f7b-ba4b-bc63fdf39b88
type: decision
level: concrete
title_ko: 관측된 실행은 kb/vv/run/의 append-only memory 청크인 agt:Run이고 대응 절차는 agt:Runbook으로 가른다
title: Observed runs are agt:Run stored as append-only memory chunks under kb/vv/run/, and response procedures are agt:Runbook
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/8117429b-5245-4a0a-8628-a46fb78dd65d, https://agentic-knowledge-base.dev/id/chunk/ae4f5c32-39ac-4bc0-b16b-ae8d96dfd901]
supersedes: [https://agentic-knowledge-base.dev/id/chunk/9f79d119-83cf-46a7-89c0-680e8f203296]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T18:12:39+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/34f0e33e-c23d-42fe-bcb2-1a7d1e3ba33c
composite: {id: https://agentic-knowledge-base.dev/id/composite/34f0e33e-c23d-42fe-bcb2-1a7d1e3ba33c, title_ko: 실행 기록은 kb/vv/run/의 append-only memory 청크다, title: The run record is an append-only memory chunk under kb/vv/run/}
---
**결론** — 관측과 대응 절차를 두 어휘로 가른다.

- **`agt:Run`** — 관측된 실행 기록. 자극·환경·결과를 담는다. **concrete 전용, append-only**이고 `kb/vv/run/`의 `memory` 청크 파일 하나가 기록 하나다. IRI는 청크의 `id/chunk/<uuid4>`이고 head는 생성 `chunks-kg.ttl`에 오른다(`p0-entity-iri-forms`).
- **`agt:Runbook`** — 대응 절차. 일반화로 승격된 스킬. `-kg`에 저장한다.

**관측은 이미 일어난 것이라 concrete에만 존재하고 수준을 갖지 못한다.** 관측을 명세로 올리는 일반화(6.3절)의 목적지는 개발 KB에서는 **요구·결정·규칙**, V&V KB에서는 **시나리오·합격 기준**이다(Part VIII).

이 결정은 `p0-run-as-observation`을 대체한다(유저 답 Q8-a, 2026-10-03). 바뀐 것은 실행 기록의 저장 자리 하나다. 옛 결론의 "`run-kg`에 저장한다"를 `kb/vv/run/`의 memory 청크로 바로잡고 나머지 진술은 그대로 잇는다.
