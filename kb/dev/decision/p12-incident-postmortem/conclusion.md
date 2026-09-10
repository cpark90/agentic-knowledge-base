---
id: https://agentic-knowledge-base.dev/id/chunk/cae1f4ce-1a3d-492c-ae12-04302a5e8d49
type: decision
level: concrete
title_ko: 사후분석은 일반화을 실행하는 자리이고 산출 없는 사후분석은 실패다
title: The postmortem is where ascent executes; one yielding nothing is a failure
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/ae4f5c32-39ac-4bc0-b16b-ae8d96dfd901, https://agentic-knowledge-base.dev/id/chunk/875062b6-2c26-4933-a43e-1b8c3699aa2b]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0153]
part_of: https://agentic-knowledge-base.dev/id/composite/48ce0d53-db1b-4b0f-9ef3-cded88f22d8b
composite: {id: https://agentic-knowledge-base.dev/id/composite/48ce0d53-db1b-4b0f-9ef3-cded88f22d8b, title_ko: 인시던트 사후분석 절차, title: Incident postmortem procedure}
---
**결론** — 사후분석은 이 체계의 일반화(6.3절)을 실행하는 자리다. 여섯 단계를
밟고, **3~5 중 하나도 산출하지 않는 사후분석은 실패로 본다.**

```
1. 실행 기록에서 인시던트 구간의 관측 청크를 뽑는다
2. defect-rules로 요인을 추론한다 (7.17절 하위 유형·한정자·트리거)
3. 요인이 어휘에 없으면 — 새 요인 청크 → defect 어휘 확장 후보
4. 요인은 있으나 조합이 케이스에 없으면
   — 새 요구 또는 logical 기준 후보 (origin:observed)
5. 깨진 가정이 있으면 — ODD 속성 재검토 후보 (3.6절)
6. 결론을 design 청크로, 관측을 memory 청크로.
   둘의 복합체가 사후분석 문서
```
