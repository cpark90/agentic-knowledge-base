---
id: https://agentic-knowledge-base.dev/id/chunk/4376dfe4-9993-470a-b563-24482a68f7b0
type: decision
level: concrete
title_ko: 규범 문서 규약 — 대안 청크 없는 결정은 shape 위반이고 대안이 없었다는 것도 기록한다
title: Normative-document conventions — A decision without an alternatives chunk violates the shape; "no alternative" is itself recorded
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T03:32:26+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/07096f39-a6f4-4727-a653-b8eafc5eff92
---
**규약** — `p7-alternatives-mandatory`의 결론을 규범 문서에 싣는 문장이다.

규약: [지킴] `decision`은 역할 태그 `**결론**` / `**근거**` / `**대안**`을 쓴다. 대안에는 기각 사유를 포함한다. 세 청크 전부 필수다 — `kb_decision` 규칙과 `gen_build`가 로드 시점에 강제한다(2026-09-11).
규약: 결정 복합체 | 항상 결론·근거·대안 세 청크. **대안 청크 없는 결정 = shape 위반**, "대안 없었음"도 기록
규약: [지킴] 평평한 `chunks/decision/`에서는 `<슬러그>-alternatives.md`가 그 결정 묶음의 대안 청크다.
