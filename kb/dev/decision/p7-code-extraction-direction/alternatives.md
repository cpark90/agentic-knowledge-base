---
id: https://agentic-knowledge-base.dev/id/chunk/47d04ec1-666e-4532-86d9-807b2a2be6dd
type: decision
level: logical
title_ko: tangle·전부 한 번에·검증기 대상 규칙 완화·미루기는 기각된다
title: Tangle, all-at-once, relaxing the verifier target rule, and deferral are rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-09-30T14:00:00+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/cfdffdf2-c863-4f22-bdfc-2d58e26550be
---
**대안** — 넷을 기각한다.

| 대안 | 기각 이유 |
|---|---|
| tangle — 청크가 원본, 파일이 생성물 | 코드 편집이 청크 편집이 된다. 잦은 변경 조건에서 가장 약하다. 로드맵 6단계가 tangle을 적고 있었으나 그것은 청크가 원본일 때의 장치다 |
| 34 파일을 한 번에 올린다 | churn 실측 없이 수백 청크가 생기고 실패의 되돌릴 범위가 전부다. 표본 뒤 넓히는 것이 순서일 뿐 목표는 같다 |
| 올리지 않고 `verifies`가 concrete 결정을 대상으로 허용 | 검사 약화다. 사다리 대응(c→e)의 뜻이 느슨해지고 전방 추적 상한이 고정된다 |
| tangle 뒤에 판단한다 | 검증기 셋이 대상 없이 남고 CQ19 34.8%의 상한이 그대로다. 추출은 tangle을 전제하지 않는다 |
