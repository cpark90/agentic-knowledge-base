---
id: https://agentic-knowledge-base.dev/id/chunk/8754e66e-76e0-4af1-b3f3-da03f803135d
type: decision
level: logical
title_ko: 커밋의 크기가 크면 동시 편집이 관계의 근거가 되지 않고 git은 밀폐 빌드 밖에 있다
title: Large commits do not ground relations, and git lies outside the hermetic build
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T03:40:23+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/59017e3e-2652-43b4-9918-0b6b91e8dce3
---
**근거** — 2026-10-22에 developer가 측정한 결과, 단위 지식 파일을 건드린 커밋은 39개였다. 커밋당 바뀐 파일 수는 중앙값이 29이고 최대가 1,284였다. 상한 없이 쌍을 뽑으면 241만 쌍이 나오지만, 파일 20개 이하인 커밋 18개만 쓰면 857쌍이다. 큰 커밋은 용어 치환이나 생성물 재생성처럼 관계와 무관한 일괄 변경이므로, 그 쌍을 증거로 쓰면 근거 없는 후보가 쏟아진다. 그래서 상한을 결정으로 먼저 세운다.

git의 이력은 Bazel 밀폐 실행의 입력이 아니다. 그래서 링크 후보 뷰가 git을 직접 읽으면 같은 리비전에서도 결과가 달라질 수 있다. 그래서 실행 기록이 추가 전용 관측으로 남는 것처럼 동시 편집의 쌍도 관측으로 고정한 뒤에 읽는다(`p0-run-is-an-append-only-memory-chunk`).

유저는 반박 증거 경로를 정하면서 동시 편집을 (가)안으로 쓰기로 했다(Q96-a). 동시 편집은 서열이 높은 증거이므로 믿음 정도를 계산하는 후보들의 재료가 된다.
