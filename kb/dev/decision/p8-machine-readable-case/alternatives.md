---
id: https://agentic-knowledge-base.dev/id/chunk/1909dc69-9b0b-4cf9-a63d-12d8a65bf5a1
type: decision
level: logical
title_ko: 자극을 별도 파일로·케이스마다 스크립트·수동 실행 안은 기각된다
title: A separate fixture file, a script per case, and manual execution are rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5, at: 2026-09-23T10:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/e2064625-339c-4cef-8f06-5e775874f177
---
**대안** — 넷을 기각한다.

| 대안 | 기각 이유 |
|---|---|
| 자극을 `kb/vv/` 밖의 고정물 파일로 둔다 | 케이스와 자극이 갈라져 한쪽만 고쳐진다. `defs/tests`의 고정물이 그 방식인데 그것은 분석 시점 전용이고 커밋되는 입력이다. 임시 자극은 커밋하지 않는 것이 요지다 |
| 케이스마다 실행 스크립트를 둔다 | 스크립트가 `artifact`가 되어 검증기와 구분이 사라진다. 케이스는 자극과 기대이지 실행 절차가 아니다 |
| 사람이 음성 절반을 손으로 돌린다 | 지금 상태이고 그래서 둘이 `skip`이다. 사람 실행은 기록에 남지 않아 감사가 볼 것이 없다 |
| 기대 문구 대신 출력 해시를 대조한다 | 메시지가 조금만 바뀌어도 깨지고, 무엇이 달라졌는지 알려주지 않는다. 게이트 메시지는 수정 방향이므로 문구가 판정의 대상이다 |
