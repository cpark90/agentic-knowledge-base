---
id: https://agentic-knowledge-base.dev/id/chunk/4962e5fe-9d28-4f18-b054-95670b51808e
type: decision
level: concrete
title_ko: 대안 없는 결정은 shape 위반이고 대안이 없었다는 것도 기록한다
former_title_ko: ["대안 청크 없는 결정은 shape 위반이고 대안이 없었다는 것도 기록한다", "대안 지식 항목 없는 결정은 shape 위반이고 대안이 없었다는 것도 기록한다"]
title: A decision without an alternatives chunk violates the shape; "no alternative" is itself recorded
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-05T00:30:20+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T19:33:51+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}]
layer: methodology
refines: [https://agentic-knowledge-base.dev/id/chunk/f715c53f-c9bd-49cc-b580-6e2d2343cd5c]
composite: {id: https://agentic-knowledge-base.dev/id/composite/07096f39-a6f4-4727-a653-b8eafc5eff92, title_ko: 대안 필수, title: Alternatives chunk is mandatory, former_title_ko: ["대안 청크 필수", "대안 지식 항목 필수"]}
part_of: https://agentic-knowledge-base.dev/id/composite/07096f39-a6f4-4727-a653-b8eafc5eff92
---
**결론** — 개발 KB의 중심 개체는 결정이고, 결정은 항상 세 단위 지식(결론·근거·대안)의 복합체다. **대안 단위 지식이 없는 결정은 shape 위반이다.** "대안이 없었다"도 대안에 적는다 — 후보가 하나뿐이었다는 것 자체가 기록할 사실이다 (노트 7.4절).

| 단위 지식 | 내용 | 토큰 상한에 들어가는 것 |
|---|---|---|
| 결론 | 무엇으로 정했는가 | 값 + 한 문단 |
| 근거 | 왜 — 어느 요구의 어느 관심사에 기여하는가, 어느 제약이 대안을 배제했는가 | `serves` + 제약 ID + 설명 |
| 대안 | 배제된 후보와 배제 근거. `-space`의 eliminated 항목이 여기로 승격 | 후보당 한 줄 |

**게이트** `gen-build`(노트 7.4절 대안 기록) — `kb_decision`의 `alternatives`는 필수 속성이고, 세 단위 지식이 없는 디렉토리는 `gen_build`가 `FAIL [gen-build]`로 거부한다. 해소는 orchestrator가 `alternatives.md`를 쓰는 것이다.
