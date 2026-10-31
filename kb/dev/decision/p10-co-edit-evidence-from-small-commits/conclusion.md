---
id: https://agentic-knowledge-base.dev/id/chunk/5967869a-2c73-4666-847a-af969e7e6caf
type: decision
level: concrete
title_ko: 동시 편집 증거는 파일 20개 이하의 커밋에서만 뽑고 그 결과를 관측으로 고정한 뒤에 읽는다
title: Co-edit evidence is drawn only from commits of at most 20 files and is read only after being fixed as an observation
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/f715c53f-c9bd-49cc-b580-6e2d2343cd5c]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T03:40:23+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/59017e3e-2652-43b4-9918-0b6b91e8dce3
composite: {id: https://agentic-knowledge-base.dev/id/composite/59017e3e-2652-43b4-9918-0b6b91e8dce3, title_ko: 동시 편집 증거의 상한과 자리, title: Bound and place of co-edit evidence}
---
**결론** — 증거 종류 `coEditHistory`인 동시 편집 이력은 같은 커밋에서 함께 바뀐 두 단위 지식을 링크 후보의 근거로 쓰는 증거다. 이 증거는 다음 규칙으로만 만든다(유저 답 Q96-a, 2026-10-24).

1. 쌍은 단위 지식 파일을 바꾼 커밋 가운데 바뀐 파일이 20개 이하인 커밋에서만 뽑는다. 그보다 큰 커밋은 일괄 정리나 생성물 갱신이어서 함께 바뀌었다는 사실이 관계의 근거가 되지 않는다.
1. git은 Bazel의 밀폐 빌드 밖에 있으므로, 쌍은 `bazel run` 모드가 git에서 뽑아 `memory` 지식 종류의 관측(`kb/dev/memory/`, 추가 전용)으로 고정한다. 관측은 읽은 커밋의 범위와 상한, 쌍의 목록을 적는다.
1. 링크 후보 뷰와 증거 기록은 git을 직접 읽지 않고 그 관측만 읽는다. 그래서 같은 리비전에서 같은 후보가 나온다.
1. 동시 편집 증거의 극성은 지지이고, 서열은 `p9-evidence-ledger-with-belief`가 정한 대로 실행 다음이다. 이 증거만으로는 확정하지 않는다.
