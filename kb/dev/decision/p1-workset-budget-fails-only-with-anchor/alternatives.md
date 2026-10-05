---
id: https://agentic-knowledge-base.dev/id/chunk/3fab0678-5d4b-46d0-9d0d-f585a3530f25
type: decision
level: logical
title_ko: 항상 실패시키는 안과 V&V 문구 대조에 맡기는 안은 기각된다
title: Always failing and leaving it to V&V phrase matching are rejected
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T14:33:11+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/e341786c-ca43-4e4f-bea4-83b4719901ae
---
**대안** — 둘을 기각한다(유저 답 2026-09-22).

| 대안 | 기각 이유 |
|---|---|
| 앵커 유무와 상관없이 예산을 넘으면 항상 비영 종료한다 | 앵커 없는 기본 `//kg:workset`이 언제나 깨진다. 기본 설정을 앵커 있는 것으로 바꾸고 라벨 목록 뷰를 별도 타깃으로 떼어야 해 비용이 더 크다. 얻는 검사 범위는 조건의 문언("앵커별")을 넘는다 |
| 지금대로 두고 `vv_run`의 기대 문구 대조로 V&V 케이스가 판정한다 | 2단계 조건이 `metrics`의 대리 수치로만 남고 게이트 밖이다. 그날 `vv_run`은 종료 코드만 보았고 문구 대조는 로드맵 7단계의 남은 일이라 판정 수단이 없었다 |
