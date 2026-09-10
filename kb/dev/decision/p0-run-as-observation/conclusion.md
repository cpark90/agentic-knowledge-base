---
id: https://agentic-knowledge-base.dev/id/chunk/9f79d119-83cf-46a7-89c0-680e8f203296
type: decision
level: concrete
title_ko: agt:Run과 agt:Runbook
title: agt:Run and agt:Runbook
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/8117429b-5245-4a0a-8628-a46fb78dd65d, https://agentic-knowledge-base.dev/id/chunk/ae4f5c32-39ac-4bc0-b16b-ae8d96dfd901]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0012]
part_of: https://agentic-knowledge-base.dev/id/composite/696b52ee-952f-478e-9af1-cd83c82c9b88
composite: {id: https://agentic-knowledge-base.dev/id/composite/696b52ee-952f-478e-9af1-cd83c82c9b88, title_ko: 실행 기록은 concrete 전용 append-only 관측이다, title: The run record is a concrete-only append-only observation}
---
**결론** — 관측과 대응 절차를 두 어휘로 가른다.

- **`agt:Run`** — 관측된 실행 기록. 자극·환경·결과를 담는다. **concrete
  전용, append-only**, `run-kg`에 저장한다
- **`agt:Runbook`** — 대응 절차. 일반화으로 승격된 스킬. `-kg`에 저장한다

**관측은 이미 일어난 것이라 concrete에만 존재하고 수준을 갖지 못한다.**
관측을 명세로 올리는 일반화(6.3절)의 목적지는 개발 KB에서는 **요구·결정·
규칙**, V&V KB에서는 **시나리오·합격 기준**이다 (Part VIII).
